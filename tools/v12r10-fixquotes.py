# -*- coding: utf-8 -*-
"""R10 修复：events-data.py 两处英文串内裸双引号 → 单引号（1073/1201 行）。"""
import io

p = 'tools/events-data.py'
lines = io.open(p, encoding='utf-8').read().split('\n')
fixed = 0
for i, ln in enumerate(lines):
    if 'The "firsts" are' in ln:
        lines[i] = ln.replace('The "firsts" are', "The 'firsts' are")
        fixed += 1
    if 'sliding toward a "single-party state" and' in ln:
        lines[i] = ln.replace('sliding toward a "single-party state" and',
                              "sliding toward a 'single-party state' and")
        fixed += 1
io.open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
print('fixed lines:', fixed)
assert fixed == 2
