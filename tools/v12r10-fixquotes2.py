# -*- coding: utf-8 -*-
"""R10 修复 II：全文件扫描字符串值行内多余裸双引号（数引号>4 的 "zh"/"en" 值行）并修为单引号。"""
import io, re

p = 'tools/events-data.py'
lines = io.open(p, encoding='utf-8').read().split('\n')
fixed = 0
for i, ln in enumerate(lines):
    m = re.match(r'^(\s*"(?:zh|en)": ")(.*)("\s*,?\s*)$', ln)
    if not m:
        continue
    head, body, tail = m.groups()
    if body.count('"') >= 2:  # 值体内还有裸双引号
        nb = body.replace('"', "'")
        lines[i] = head + nb + tail
        print('fixed line', i + 1, ':', body[:70])
        fixed += 1
io.open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
print('total fixed:', fixed)
