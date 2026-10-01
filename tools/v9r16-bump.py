# -*- coding: utf-8 -*-
"""V9-20 R16 版本三件套：VERSION / app.js SITE_VERSION / 全站 site-version-val span。
自动探测当前版本（不硬编码 OLD），替换计数全部打印。"""
import glob, io, re, sys

NEW = '9.6.0'

cur = io.open('VERSION', encoding='utf-8').read().strip()
OLD = cur
if OLD == NEW:
    sys.exit('FATAL: VERSION 已是 %s' % NEW)
print('VERSION: %s -> %s' % (OLD, NEW))
io.open('VERSION', 'w', encoding='utf-8', newline='\n').write(NEW)

app = io.open('app.js', encoding='utf-8').read()
app2, n = re.subn(r"SITE_VERSION = '" + re.escape(OLD) + r"'", "SITE_VERSION = '" + NEW + "'", app)
if n != 1:
    sys.exit('app.js SITE_VERSION 替换计数异常: %d' % n)
io.open('app.js', 'w', encoding='utf-8', newline='').write(app2)
print('app.js SITE_VERSION -> %s (count=%d)' % (NEW, n))

total, pages = 0, []
pat = re.compile(r'(<span class="site-version-val">)' + re.escape(OLD) + r'(</span>)')
for f in sorted(glob.glob('*.html')):
    s = io.open(f, encoding='utf-8').read()
    s2, k = pat.subn(r'\g<1>' + NEW + r'\g<2>', s)
    if k:
        io.open(f, 'w', encoding='utf-8', newline='').write(s2)
        print('  %-24s %d' % (f, k))
        pages.append(f)
        total += k
print('span 总替换数 = %d（页数 %d）' % (total, len(pages)))

# 交叉校验：全站不应再残留旧版本串（排除历史 CHANGELOG/账本）
leftover = []
for f in sorted(glob.glob('*.html')) + ['app.js']:
    if re.search(re.escape('>' + OLD + '<'), io.open(f, encoding='utf-8').read()):
        leftover.append(f)
print('残留 >%s< 的页面: %s' % (OLD, leftover or '无'))
if leftover:
    sys.exit('FATAL: 仍有页面残留旧版本')
