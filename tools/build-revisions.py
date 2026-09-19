# -*- coding: utf-8 -*-
"""解析 git log，为每个第一手锚点生成修订轨迹 → revisions.html。

用法：python tools/build-revisions.py
（站点根目录执行。依赖 git 仓库完整提交历史。幂等重建。）

原理：对 primary/documents/interviews/x-posts 四个页面，逐 commit 比较新旧版本的锚点 id 集合，
  首次出现 = 创建；后续出现 = 该 commit 时仍存在（「续存」）。
  消失则标记为「移除」。
"""
import io
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

PAGES = {
    'primary.html': ('言行实录', r'id="(e\d[\d-]*)"'),
    'documents.html': ('一手文档馆', r'id="(d\d[\d-]*)"'),
    'interviews.html': ('访谈与表态', r'id="(i\d[\d-]*)"'),
    'x-posts.html': ('X 帖史选辑', r'id="(p\d[\d-]*)"'),
}

# ---------- 1) 逐 commit 提取各页锚点集合 ----------
raw = subprocess.run(
    ['git', 'log', '--format=%h|%ad|%s', '--date=short', '--reverse'] + list(PAGES.keys()),
    capture_output=True, text=True, encoding='utf-8'
).stdout.strip()

commits = []
for line in raw.splitlines():
    parts = line.split('|', 2)
    if len(parts) == 3:
        commits.append(parts)  # (hash, date, subject)
print(f'git log: {len(commits)} commits touching tracked pages')

# 对每个 commit，提取每个页面的锚点集合
def get_anchors(commit_hash):
    """返回 {page: set(anchor_ids)}"""
    out = {}
    for page, (label, pat) in PAGES.items():
        try:
            content = subprocess.run(
                ['git', 'show', f'{commit_hash}:{page}'],
                capture_output=True, text=True, encoding='utf-8', timeout=10
            ).stdout
            out[page] = set(re.findall(pat, content))
        except Exception:
            out[page] = set()
    return out

# 追踪每个锚点的生命周期
# anchor_key = (page_label, anchor_id)  →  events = [{type: created/alive/removed, hash, date, subject}]
lifetimes = {}
prev_anchors = {}  # page → set

for ch, date, subj in commits:
    cur = get_anchors(ch)
    for page, (label, pat) in PAGES.items():
        now = cur.get(page, set())
        prev = prev_anchors.get(page, set())
        for aid in now - prev:
            key = (label, aid)
            if key not in lifetimes:
                lifetimes[key] = {'created': (ch, date, subj), 'alive': [], 'removed': None}
        for aid in prev - now:
            key = (label, aid)
            if key in lifetimes and lifetimes[key]['removed'] is None:
                lifetimes[key]['removed'] = (ch, date, subj)
        prev_anchors[page] = now
        # 记录续存（非首 commit 的锚点）
        for aid in now & prev:
            key = (label, aid)
            if key in lifetimes and lifetimes[key]['removed'] is None:
                lifetimes[key]['alive'].append((ch, date, subj))

# ---------- 2) 生成 HTML ----------
html_rows = []
for (label, aid), data in sorted(lifetimes.items(), key=lambda x: x[0][1]):
    cr = data['created']
    alive_n = len(data['alive'])
    rm = data['removed']
    status = '<span style="color:#1f3a5f;font-weight:700">在册</span>' if rm is None else '<span style="color:#8a857c">已移除</span>'
    versions = f'<b>{cr[0]}</b>（{cr[1]}）创建'
    if alive_n > 0:
        versions += f' · {alive_n} 次提交续存'
    if rm:
        versions += f' · {rm[0]}（{rm[1]}）移除'
    page_file = [pg for pg, (lb, _) in PAGES.items() if lb == label][0]
    anchor_link = f'{page_file}#{aid}'
    html_rows.append(
        f'<tr><td style="white-space:nowrap">{label}</td>'
        f'<td style="font-family:Georgia,serif;color:#7c2d2d;font-weight:700">{aid}</td>'
        f'<td>{status}</td>'
        f'<td style="font-size:12.5px;line-height:1.7;color:#5c574e">{versions}</td>'
        f'<td><a href="{anchor_link}" style="color:#7c2d2d;text-decoration:none">→ 原文</a></td></tr>'
    )

# 过滤：只保留当前文件中仍存在的锚点
current_anchors = {}
for page, (label, pat) in PAGES.items():
    content = io.open(page, encoding='utf-8').read()
    current_anchors[page] = set(re.findall(pat, content))

filtered = []
for (label, aid), data in sorted(lifetimes.items(), key=lambda x: x[0][1]):
    page_file = [pg for pg, (lb, _) in PAGES.items() if lb == label][0]
    if aid not in current_anchors.get(page_file, set()):
        continue
    filtered.append(((label, aid), data))

html_rows = []
for (label, aid), data in filtered:
    cr = data['created']
    alive_n = len(data['alive'])
    rm = data['removed']
    status = '<span style="color:#1f3a5f;font-weight:700">在册</span>' if rm is None else '<span style="color:#8a857c">已移除</span>'
    versions = f'<b>{cr[0]}</b>（{cr[1]}）创建'
    if alive_n > 0:
        versions += f' · {alive_n} 次提交续存'
    if rm:
        versions += f' · {rm[0]}（{rm[1]}）移除'
    page_file = [pg for pg, (lb, _) in PAGES.items() if lb == label][0]
    anchor_link = f'{page_file}#{aid}'
    html_rows.append(
        f'<tr><td style="white-space:nowrap">{label}</td>'
        f'<td style="font-family:Georgia,serif;color:#7c2d2d;font-weight:700">{aid}</td>'
        f'<td>{status}</td>'
        f'<td style="font-size:12.5px;line-height:1.7;color:#5c574e">{versions}</td>'
        f'<td><a href="{anchor_link}" style="color:#7c2d2d;text-decoration:none">→ 原文</a></td></tr>'
    )

html_rows.reverse()  # 最新的在前

# ---------- 3) 生成 revisions.html ----------
total = len(html_rows)
counts = {}
for (label, aid) in lifetimes.keys():
    counts[label] = counts.get(label, 0) + 1
count_str = ' / '.join(f'{v}' for v in counts.values())

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>修订历史 · 马斯克商业志 MUSK, INC.</title>
<meta name="robots" content="noindex" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%237c2d2d'/%3E%3Ctext x='32' y='45' font-family='Georgia,serif' font-size='36' font-style='italic' fill='%23faf9f6' text-anchor='middle'%3EM%3C/text%3E%3C/svg%3E" />
<link rel="stylesheet" href="style.css" />
<style>
.rv-page {{ max-width: 1000px; margin: 0 auto; padding: 40px 20px 60px; }}
.rv-back {{ font-size: 13px; letter-spacing: .1em; color: #7c2d2d; text-decoration: none; }}
.rv-back:hover {{ text-decoration: underline; }}
.rv-head {{ border-bottom: 3px double #1a1a1a; padding: 14px 0 12px; margin-bottom: 14px; }}
.rv-head h1 {{ font-family: Georgia, "STSong", serif; font-size: clamp(28px, 5vw, 42px); }}
.rv-head p {{ color: #5c574e; font-size: 13.5px; font-style: italic; line-height: 1.8; }}
.rv-table {{ width: 100%; border-collapse: collapse; font-size: 13.5px; }}
.rv-table th, .rv-table td {{ text-align: left; padding: 8px 10px; border-bottom: 1px dotted rgba(26,26,26,.16); vertical-align: top; }}
.rv-table th {{ font-size: 11px; letter-spacing: .18em; color: #7c2d2d; font-weight: 700; border-bottom: 1px solid #1a1a1a; }}
.rv-foot {{ margin-top: 26px; font-size: 11px; color: #8a857c; line-height: 1.8; }}
@media print {{ .rv-page {{ padding: 20px; }} .rv-back {{ display: none; }} }}
</style>
</head>
<body>
<div class="rv-page">
  <a class="rv-back" href="index.html">← 返回网站主页 / Back to site</a>
  <header class="rv-head">
    <h1>修订历史</h1>
    <p>REVISION HISTORY — 每个第一手锚点的完整生命周期：从哪个版本创建、经历多少次提交续存、是否被移除。全部数据来自 git 提交历史（{len(commits)} 次相关提交逐条比对），自动生成、可复现。锚点共 {total} 个：{count_str}。</p>
  </header>
  <table class="rv-table">
    <tr><th>板块</th><th>锚点 ID</th><th>状态</th><th>修订轨迹</th><th>原文</th></tr>
{chr(10).join(html_rows)}
  </table>
  <p class="rv-foot">本页由 tools/build-revisions.py 自动生成（解析 git log），数据完全可复现 · 非官方学习型网站 · <a href="primary.html" style="color:#7c2d2d">言行实录 →</a> · <a href="search.html" style="color:#7c2d2d">第一手检索 →</a></p>
</div>
</body>
</html>'''

io.open('revisions.html', 'w', encoding='utf-8', newline='\n').write(html)
print(f'revisions.html: {total} 个锚点的修订轨迹（{counts}）')
