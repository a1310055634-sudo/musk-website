# -*- coding: utf-8 -*-
"""N06 版本三件套（正则旧值=当前版本 10.5.0；跑后前滚 10.6.0 由本脚本末尾自动完成）。"""
import glob, io, re, sys
OLD, NEW = '10.6.0', 'NEXT'
io.open('VERSION', 'w', encoding='utf-8', newline='\n').write(NEW)
print('VERSION ->', NEW)
app = io.open('app.js', encoding='utf-8').read()
app2, n = re.subn(r"SITE_VERSION = '" + re.escape(OLD) + "'", "SITE_VERSION = '" + NEW + "'", app)
if n != 1:
    sys.exit('app.js 替换计数异常: %d' % n)
io.open('app.js', 'w', encoding='utf-8', newline='').write(app2)
print('app.js ->', NEW)
total = 0
for f in sorted(glob.glob('*.html')):
    s = io.open(f, encoding='utf-8').read()
    s2, n = re.subn(r'(<span class="site-version-val">)' + re.escape(OLD) + r'(</span>)',
                    r'\g<1>' + NEW + r'\g<2>', s)
    if n:
        io.open(f, 'w', encoding='utf-8', newline='').write(s2)
        total += n
print('span 总替换数 =', total)
v = io.open('VERSION', encoding='utf-8').read().strip()
bad = [f for f in sorted(glob.glob('*.html'))
       for m in re.finditer(r'site-version-val">([^<]+)<', io.open(f, encoding='utf-8').read()) if m.group(1) != v]
print('复核:', '全部一致' if not bad else bad)
# 前滚正则到 NEW（本文件供下轮派生）
s = io.open(__file__, encoding='utf-8').read()
s = s.replace("OLD, NEW = '" + OLD + "', '" + NEW + "'", "OLD, NEW = '" + NEW + "', 'NEXT'")
s = s.replace(re.escape(OLD), NEW)
io.open(__file__, 'w', encoding='utf-8', newline='\n').write(s)
print('regex rolled fwd ->', NEW)
