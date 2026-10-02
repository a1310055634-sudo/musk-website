# -*- coding: utf-8 -*-
"""v11.1.0 复古杂志最终色值抽查（打印版）。"""
import io, re

s = io.open('style.css', encoding='utf-8').read()
tokens = ['--paper-0','--paper-100','--tx-1','--accent','--accent-deep','--accent-bright','--hue-red']
print('=== 令牌终值 ===')
for t in tokens:
    m = re.search(re.escape(t) + r':\s*(#[0-9A-Fa-f]+)', s)
    if m:
        print(f'  {t}: {m.group(1)}')

html_check = 0
for f in ['index.html','primary.html','documents.html','interviews.html','resources.html']:
    h = io.open(f, encoding='utf-8').read()
    if '8B4513' in h:
        html_check += 1
print(f'HTML favicon 新棕覆盖: {html_check}/5 核心页')

old_left = 0
import glob
for f in glob.glob('*.html'):
    old_left += len(re.findall(r'C84032|7c2d2d', io.open(f, encoding='utf-8').read(), re.I))
css_left = len(re.findall(r'C84032|7c2d2d', s, re.I))
print(f'旧色残留: html {old_left} + style.css {css_left}（预期仅 changelog/revisions 历史文本内）')
