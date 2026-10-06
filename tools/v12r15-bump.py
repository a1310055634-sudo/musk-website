# -*- coding: utf-8 -*-
"""V12 版本三件套（R15 起通用版）：VERSION / app.js / 全站 site-version-val span。
断言=无残留旧版 span（masthead 期号 span 随页数增长，不定死总数）。"""
import glob, io, re, sys

OLD, NEW = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None
if not NEW:
    print('usage: v12r15-bump.py <OLD> <NEW>')
    raise SystemExit(2)

io.open('VERSION', 'w', encoding='utf-8', newline='\n').write(NEW)
print('VERSION ->', NEW)

app = io.open('app.js', encoding='utf-8').read()
app2, n = re.subn(r"SITE_VERSION = '" + re.escape(OLD) + "'", "SITE_VERSION = '" + NEW + "'", app)
assert n == 1, 'app.js hits=%d' % n
io.open('app.js', 'w', encoding='utf-8', newline='\n').write(app2)
print('app.js ->', NEW)

files = sorted(glob.glob('*.html'))
total = 0
for f in files:
    t = io.open(f, encoding='utf-8').read()
    t2, n = re.subn(r'(<span class="site-version-val">)' + re.escape(OLD) + r'(</span>)',
                    r'\g<1>' + NEW + r'\g<2>', t)
    if n:
        io.open(f, 'w', encoding='utf-8', newline='\n').write(t2)
        total += n
print('span total =', total)
# 无残留断言
left = 0
for f in files:
    t = io.open(f, encoding='utf-8').read()
    left += len(re.findall(r'(<span class="site-version-val">)' + re.escape(OLD) + r'(</span>)', t))
assert left == 0, 'residual OLD spans: %d' % left
assert total > 0
print('BUMP OK ->', NEW, '(no residual)')
