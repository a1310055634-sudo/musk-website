# -*- coding: utf-8 -*-
"""V8 R07 version bump 7.6.0 -> 7.7.0: VERSION, app.js SITE_VERSION, 14 page spans.
Span pattern follows the FIXED r02-spans approach (unique-count assertion per file)."""
import io, glob

OLD, NEW = '7.6.0', '7.7.0'
SPAN_OLD = 'site-version-val">' + OLD + '<'
SPAN_NEW = 'site-version-val">' + NEW + '<'

# 1) VERSION
v = io.open('VERSION', encoding='utf-8', newline='').read()
assert v.strip() == OLD, 'VERSION=%r' % v
io.open('VERSION', 'w', encoding='utf-8', newline='').write(v.replace(OLD, NEW))
print('VERSION ->', NEW)

# 2) app.js
a = io.open('app.js', encoding='utf-8', newline='').read()
pat_a = "var SITE_VERSION = '" + OLD + "';"
assert a.count(pat_a) == 1, 'app.js span not unique'
io.open('app.js', 'w', encoding='utf-8', newline='').write(a.replace(pat_a, "var SITE_VERSION = '" + NEW + "';"))
print('app.js ->', NEW)

# 3) 14 page spans
total = 0
for f in sorted(glob.glob('*.html')):
    s = io.open(f, encoding='utf-8', newline='').read()
    n = s.count(SPAN_OLD)
    if n:
        assert n == 1, 'span count %d in %s' % (n, f)
        io.open(f, 'w', encoding='utf-8', newline='').write(s.replace(SPAN_OLD, SPAN_NEW))
        total += 1
assert total == 14, 'page span files=%d (expect 14)' % total
print('page spans updated in %d files' % total)
