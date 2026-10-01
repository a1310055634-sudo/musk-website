# -*- coding: utf-8 -*-
"""V9-20 R14 版本三件套：VERSION / app.js SITE_VERSION / 全站 site-version-val span。"""
import glob, io, re, sys

OLD, NEW = '9.3.0', '9.4.0'

io.open('VERSION', 'w', encoding='utf-8', newline='\n').write(NEW)
print('VERSION ->', NEW)

app = io.open('app.js', encoding='utf-8').read()
app2, n = re.subn(r"SITE_VERSION = '9\.3\.0'", "SITE_VERSION = '" + NEW + "'", app)
if n != 1:
    sys.exit('app.js SITE_VERSION 替换计数异常: %d' % n)
io.open('app.js', 'w', encoding='utf-8', newline='').write(app2)
print('app.js SITE_VERSION ->', NEW, '(count=%d)' % n)

total = 0
pages = []
pat = re.compile(r'(<span class="site-version-val">)' + re.escape(OLD) + r'(</span>)')
for f in sorted(glob.glob('*.html')):
    s = io.open(f, encoding='utf-8').read()
    s2, n = pat.subn(r'\g<1>' + NEW + r'\g<2>', s)
    if n:
        io.open(f, 'w', encoding='utf-8', newline='').write(s2)
        print('  %s: %d' % (f, n))
        pages.append(f)
        total += n
print('span 总替换数 =', total, '（页数 %d：原 14 页 + resources.html）' % len(pages))
