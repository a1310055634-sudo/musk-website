# -*- coding: utf-8 -*-
"""N08 版本三件套（自动派生：从 N07 bump 读 OLD，运行后前滚）。"""
import glob, io, re, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
prev = io.open('tools/v10n07-bump.py', encoding='utf-8').read()
m = re.search(r"NEW = '([\d.]+)'", prev)
OLD = m.group(1)
NEW = '10.8.0'
print('OLD =', OLD, '-> NEW =', NEW)
io.open('VERSION', 'w', encoding='utf-8', newline='\n').write(NEW)
app = io.open('app.js', encoding='utf-8').read()
app2, n = re.subn(r"SITE_VERSION = '" + re.escape(OLD) + "'", "SITE_VERSION = '" + NEW + "'", app)
if n != 1:
    sys.exit('app.js 替换计数异常: %d' % n)
io.open('app.js', 'w', encoding='utf-8', newline='').write(app2)
total = 0
for f in sorted(glob.glob('*.html')):
    s = io.open(f, encoding='utf-8').read()
    s2, n = re.subn(r'(<span class="site-version-val">)' + re.escape(OLD) + r'(</span>)',
                    r'\g<1>' + NEW + r'\g<2>', s)
    if n:
        io.open(f, 'w', encoding='utf-8', newline='').write(s2)
        total += n
print('span 总替换数 =', total)
bad = [f for f in sorted(glob.glob('*.html'))
       for mm in re.finditer(r'site-version-val">([^<]+)<', io.open(f, encoding='utf-8').read()) if mm.group(1) != NEW]
print('复核:', '全部一致' if not bad else bad)
