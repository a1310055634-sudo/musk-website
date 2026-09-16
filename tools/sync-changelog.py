# -*- coding: utf-8 -*-
"""从 CHANGELOG.md 全量重新生成 changelog.html 的修订列表。

用法：python tools/sync-changelog.py
（在站点根目录执行；CHANGELOG.md 每轮更新后运行一次即可保持两处同步。）
"""
import io
import re
import html as H
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

md = io.open('CHANGELOG.md', encoding='utf-8').read()


def inline(t):
    t = H.escape(t, quote=False)
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)


entries = []
cur = None
for line in md.splitlines():
    m = re.match(r'^## (v[\d.]+) — (\d{4}-\d{2}-\d{2}) · (.+)$', line)
    if m:
        cur = {'ver': m.group(1), 'date': m.group(2), 'title': m.group(3), 'sections': []}
        entries.append(cur)
        continue
    if cur is None:
        continue
    ms = re.match(r'^\*\*(.+?)\*\*\s*$', line)
    if ms:
        cur['sections'].append({'name': ms.group(1), 'items': []})
        continue
    if line.startswith('- '):
        if not cur['sections']:
            cur['sections'].append({'name': '要点', 'items': []})
        cur['sections'][-1]['items'].append(inline(line[2:].strip()))

lis = []
for e in entries:
    parts = [f'<h3>{e["ver"]} — {e["date"]} · {inline(e["title"])}</h3>']
    for sec in e['sections']:
        if not sec['items']:
            continue
        parts.append(f'<h4>{inline(sec["name"])}</h4><ul>')
        for it in sec['items']:
            parts.append(f'<li>{it}</li>')
        parts.append('</ul>')
    lis.append('<li class="cl-item">' + ''.join(parts) + '</li>')

new_list = '<ol class="cl-list">\n' + '\n'.join(lis) + '\n  </ol>'

p = 'changelog.html'
s = io.open(p, encoding='utf-8').read()
m = re.search(r'<ol class="cl-list">.*?</ol>', s, re.S)
assert m, 'changelog.html: <ol class="cl-list"> 未找到'
s = s.replace(m.group(0), new_list, 1)
s = re.sub(r'同步生成（\d+ 条，v[\d.]+ → v[\d.]+）。',
           f'同步生成（{len(entries)} 条，v{entries[-1]["ver"].lstrip("v")} → v{entries[0]["ver"].lstrip("v")}）。', s)
io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
print(f'changelog.html: 重生成 {len(entries)} 条（{entries[-1]["ver"]} → {entries[0]["ver"]}）')
