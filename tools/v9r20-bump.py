# -*- coding: utf-8 -*-
"""V9-20 R20 版本三件套：VERSION / app.js SITE_VERSION / 全站 site-version-val span。"""
import glob, io, re, sys

OLD, NEW = '9.9.0', '10.0.0'

io.open('VERSION', 'w', encoding='utf-8', newline='\n').write(NEW)
print('VERSION ->', NEW)

app = io.open('app.js', encoding='utf-8').read()
app2, n = re.subn(r"SITE_VERSION = '9\.9\.0'", "SITE_VERSION = '" + NEW + "'", app)
if n != 1:
    sys.exit('app.js SITE_VERSION 替换计数异常: %d' % n)
io.open('app.js', 'w', encoding='utf-8', newline='').write(app2)
print('app.js SITE_VERSION ->', NEW, '(count=%d)' % n)

total = 0
pages = []
for f in sorted(glob.glob('*.html')):
    s = io.open(f, encoding='utf-8').read()
    s2, n = re.subn(r'(<span class="site-version-val">)9\.9\.0(</span>)',
                    r'\g<1>' + NEW + r'\g<2>', s)
    if n:
        io.open(f, 'w', encoding='utf-8', newline='').write(s2)
        print('  %s: %d' % (f, n))
        pages.append(f)
        total += n
print('span 总替换数 =', total, '（预期 15 页各 1 处：原 14 页 + resources.html；'
      'resources.html 内生成器原生版本串随后由 build-resources.py 以 9.6.0 重建更新）')

v = io.open('VERSION', encoding='utf-8').read().strip()
bad = []
for f in sorted(glob.glob('*.html')):
    for m in re.finditer(r'site-version-val">([^<]+)<', io.open(f, encoding='utf-8').read()):
        if m.group(1) != v:
            bad.append((f, m.group(1)))
print('复核:', '全部一致' if not bad else bad)
