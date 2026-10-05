# -*- coding: utf-8 -*-
"""V12 R12 版本三件套：VERSION / app.js / 全站 site-version-val span（R12 起 17 处：16 + deep-dive-07 新页）。"""
import glob, io, re

OLD, NEW = '11.12.0', '11.13.0'

io.open('VERSION', 'w', encoding='utf-8', newline='\n').write(NEW)
print('VERSION ->', NEW)

app = io.open('app.js', encoding='utf-8').read()
app2, n = re.subn(r"SITE_VERSION = '11\.12\.0'", "SITE_VERSION = '" + NEW + "'", app)
assert n == 1, 'app.js SITE_VERSION hits=%d' % n
io.open('app.js', 'w', encoding='utf-8', newline='\n').write(app2)
print('app.js ->', NEW)

files = sorted(glob.glob('*.html'))
total = 0
touched = []
for f in files:
    t = io.open(f, encoding='utf-8').read()
    t2, n = re.subn(r'(<span class="site-version-val">)11\.12\.0(</span>)',
                    r'\g<1>' + NEW + r'\g<2>', t)
    if n:
        io.open(f, 'w', encoding='utf-8', newline='\n').write(t2)
        total += n
        touched.append(f)
print('span total =', total)
assert total == 17, 'expected 17 spans (16 + deep-dive-07), got %d' % total
assert 'deep-dive-07.html' in touched
print('BUMP OK ->', NEW)
