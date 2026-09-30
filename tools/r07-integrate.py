# -*- coding: utf-8 -*-
"""V8 R07: insert 7 interview entries into interviews.html before <p class="iv-foot".
Fixed-version pattern (r06): fragment file + single rebuild + uniqueness assertions."""
import io, re, sys

PAGE = 'interviews.html'
SNIP = 'tools/r07-snippet.html'
ANCHOR = '<p class="iv-foot"'
NEW_IDS = ['i2017-04-28', 'i2018-09-07', 'i2018-09', 'i2020-05-07', 'i2020-05', 'i2022-04-06', 'i2024-11-04']

page = io.open(PAGE, encoding='utf-8', newline='').read()
snip = io.open(SNIP, encoding='utf-8', newline='').read()

# CRLF normalization: match the target file's dominant ending
crlf = page.count('\r\n')
lf = page.count('\n') - crlf
assert crlf >= lf, 'unexpected: target file is LF-dominant'
snip = snip.replace('\r\n', '\n').replace('\n', '\r\n')

# --- pre assertions ---
assert page.count(ANCHOR) == 1, 'anchor <p class="iv-foot" not unique: %d' % page.count(ANCHOR)
n_before = page.count('<article class="iv-item"')
# 27 raw items, of which one legacy quote item has no stable id -> 26 indexable
assert n_before == 27, 'iv-item count before=%d (expect 27)' % n_before
idx_before = len(re.findall(r'<article class="iv-item" id="i', page))
assert idx_before == 26, 'indexed iv-item count before=%d (expect 26)' % idx_before
for i in NEW_IDS:
    assert ('id="%s"' % i) not in page, 'id already present: %s' % i
assert snip.count('<article class="iv-item"') == 7, 'snippet should hold 7 articles'
assert snip.rstrip().endswith('</article>'), 'snippet must end with a closed article'

# --- insert before anchor ---
new_page = page.replace(ANCHOR, snip.rstrip('\r\n') + '\r\n\r\n' + ANCHOR)
assert new_page != page, 'replace produced no change'

# --- post assertions ---
n_after = new_page.count('<article class="iv-item"')
assert n_after == n_before + 7, 'iv-item count after=%d (expect %d)' % (n_after, n_before + 7)
idx_after = len(re.findall(r'<article class="iv-item" id="i', new_page))
assert idx_after == idx_before + 7, 'indexed count after=%d (expect %d)' % (idx_after, idx_before + 7)
for i in NEW_IDS:
    assert new_page.count('id="%s"' % i) == 1, 'id not unique after insert: %s' % i
assert new_page.count(ANCHOR) == 1, 'anchor duplicated'
assert new_page.count('\r\n') > new_page.count('\n') - new_page.count('\r\n'), 'CRLF dominance broken'

io.open(PAGE, 'w', encoding='utf-8', newline='').write(new_page)
print('OK: interviews.html 26 -> 33 articles; ids:', ', '.join(NEW_IDS))
