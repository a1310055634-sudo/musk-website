# -*- coding: utf-8 -*-
"""马斯克商业志 · 全站一键体检

用法：python tools/verify.py
（站点根目录执行。部署前/每轮质量门运行；有任何 ✗ 时退出码为 1。）

检查项：断链（页面/锚点/CSS/JS/图片，递归）、每页重复 id、
版本一致性（VERSION / app.js / 页面 span）、检索索引条数与索引页计数一致。
不含浏览器与打印验证——那两项见 CHANGELOG 各轮质量门记录。
"""
import collections
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

FAIL = []

def check(name, errors):
    if errors:
        FAIL.append(name)
        print(f"✗ {name}: {len(errors)} 处")
        for e in errors[:12]:
            print("   ", e)
    else:
        print(f"✓ {name}")

# ---------- 收集文件 ----------
html_files = sorted(glob.glob('*.html'))
os_files = set()
for root, dirs, fs in os.walk('.'):
    if '.git' in root:
        continue
    for f in fs:
        rel = os.path.join(root, f).replace('\\', '/')
        os_files.add(rel[2:] if rel.startswith('./') else rel)

texts = {f: io.open(f, encoding='utf-8').read() for f in html_files}

# ---------- 1) 断链（页面/锚点/CSS/JS/图片） ----------
link_errors = []
page_ids = {f: set(re.findall(r'\bid="([^"]+)"', s)) for f, s in texts.items()}
for f, s in texts.items():
    for m in re.finditer(r'(href|src)="([^"#]+)(#[^"]*)?"', s):
        t = m.group(2)
        if t.startswith(('http', 'mailto:', 'data:')):
            continue
        if "'" in t:  # JS 模板字符串（运行期拼接），跳过
            continue
        if t.lower() not in os_files:
            link_errors.append(f'{f} -> {t}')
        anc = m.group(3)
        if anc and t.lower().endswith('.html'):
            tgt = t.lower()
            if tgt in page_ids and anc[1:] not in page_ids[tgt]:
                link_errors.append(f'{f} -> {t}{anc}（锚点不存在）')
check('断链（文件与跨页锚点）', link_errors)

# ---------- 2) 重复 id ----------
dup_errors = []
for f, s in texts.items():
    ids = re.findall(r'\bid="([^"]+)"', s)
    dups = [x for x, n in collections.Counter(ids).items() if n > 1]
    if dups:
        dup_errors.append(f'{f}: {dups}')
check('重复 id', dup_errors)

# ---------- 3) 版本一致性 ----------
version_errors = []
ver_file = io.open('VERSION', encoding='utf-8').read().strip()
app_ver = re.search(r"SITE_VERSION = '([^']+)'", io.open('app.js', encoding='utf-8').read()).group(1)
if ver_file != app_ver:
    version_errors.append(f'VERSION({ver_file}) != app.js({app_ver})')
for f, s in texts.items():
    m = re.search(r'site-version-val">([^<]+)<', s)
    if m and m.group(1) != ver_file:
        version_errors.append(f'{f}: span={m.group(1)}')
check(f'版本一致性（{ver_file}）', version_errors)

# ---------- 4) 检索索引一致性 ----------
idx_errors = []
sidx = io.open('search-index.js', encoding='utf-8').read()
n_items = len(re.findall(r'"id":\s*"', sidx))
# 类型计数断言在 tools/build-search-index.py 内；此处核对类型总数与账本条数一致
n_ps = len(re.findall(r'<li class="ps-row', texts.get('primary.html', '')))
n_docs = len(re.findall(r'<article class="doc-article" id="d', texts.get('documents.html', '')))
n_iv = len(re.findall(r'<article class="iv-item" id="i', texts.get('interviews.html', '')))
n_posts = len(re.findall(r'<div class="tweet-card" id="p', texts.get('x-posts.html', '')))
total_expected = n_ps + n_docs + n_iv + n_posts
if n_items != total_expected:
    idx_errors.append(f'索引 {n_items} 条 != 页面锚点 {total_expected} 条（先重跑 tools/build-search-index.py）')
check(f'检索索引一致（{n_items} 条 = {n_ps}+{n_docs}+{n_iv}+{n_posts}）', idx_errors)

# ---------- 5) 时间轴节点 = 账本条目 ----------
tl_errors = []
if os.path.exists('primary.html'):
    ps = len(re.findall(r'<li class="ps-row', texts.get('primary.html', '')))
    tl = len(re.findall(r'class="pt-dot"', texts.get('primary.html', '')))
    if ps != tl:
        tl_errors.append(f'账本 {ps} 条 != 时间轴 {tl} 节点（重跑 tools/build-ledger-timeline.py）')
check('时间轴节点一致', tl_errors)

# ---------- 6) 语录核实组卡 = 账本有引文条目（白名单精确核对） ----------
qs_errors = []
QS_EXEMPT = {'e2013', 'e2021-07', 'e2025'}  # e2013 在格言组；e2021-07 转述非第一人称；e2025 统计行非引语
if os.path.exists('quotes.html') and os.path.exists('primary.html'):
    ph = texts.get('primary.html', '')
    blocks = re.findall(r'(<li class="ps-row[^"]*" id="(e\d[\d-]*)".*?</li>)', ph, re.S)
    quoted_ids = {bid for full, bid in blocks if '<blockquote class="ps-quote">' in full}
    carded_ids = set(re.findall(r'qs-card" href="primary\.html#(e[\d-]+)"',
                                io.open('quotes.html', encoding='utf-8').read()))
    missing = sorted(quoted_ids - carded_ids - QS_EXEMPT)
    orphan = sorted(carded_ids - quoted_ids)
    if missing:
        qs_errors.append(f'有引文未上卡: {missing}')
    if orphan:
        qs_errors.append(f'卡片无对应引文块: {orphan}')
    print(f"  · 语录卡 {len(carded_ids)} 张，账本引文块 {len(quoted_ids)} 个，白名单豁免 {len(QS_EXEMPT & (quoted_ids - carded_ids))} 项")
check('语录卡覆盖（白名单核对）', qs_errors)

# ---------- 汇总 ----------
print()
if FAIL:
    print(f'体检未通过：{len(FAIL)} 项 → {", ".join(FAIL)}')
    sys.exit(1)
print(f'体检全部通过：{len(html_files)} 个页面，检索索引 {n_items} 条。')
