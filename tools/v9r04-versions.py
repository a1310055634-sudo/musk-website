# -*- coding: utf-8 -*-
"""V9-20 R04: 版本三件套 8.3.0 → 8.4.0（VERSION / app.js SITE_VERSION / 全站 span）。
替换计数必须打印；任何一处计数异常即中止。"""
import glob, io, re, sys

OLD, NEW = '8.3.0', '8.4.0'

# 1) VERSION
v = io.open('VERSION', encoding='utf-8').read().strip()
assert v == OLD, f'VERSION 现值 {v} != {OLD}'
io.open('VERSION', 'w', encoding='utf-8', newline='').write(NEW + '\n')
print(f'VERSION: {OLD} -> {NEW}')

# 2) app.js
s = io.open('app.js', encoding='utf-8', newline='').read()
n = s.count(f"SITE_VERSION = '{OLD}'")
assert n == 1, f'app.js SITE_VERSION 命中 {n} 次（期望 1）'
s = s.replace(f"SITE_VERSION = '{OLD}'", f"SITE_VERSION = '{NEW}'", 1)
io.open('app.js', 'w', encoding='utf-8', newline='').write(s)
print(f'app.js SITE_VERSION: 替换 {n} 处')

# 3) 全站 span
total = 0
files = 0
for f in sorted(glob.glob('*.html')):
    t = io.open(f, encoding='utf-8', newline='').read()
    c = t.count(f'site-version-val">{OLD}<')
    if c:
        t = t.replace(f'site-version-val">{OLD}<', f'site-version-val">{NEW}<')
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        total += c
        files += 1
        print(f'  {f}: 替换 {c} 处')
print(f'span 总计：{total} 处 / {files} 页')
assert total == 14, f'span 应 14 处，实际 {total}'
print('DONE v9r04-versions')
