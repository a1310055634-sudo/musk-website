# -*- coding: utf-8 -*-
"""V8 R09: insert 6 ledger entries into primary.html (chronological, anchor-preserved)."""
import io, re

PAGE = 'primary.html'
SNIP = 'tools/r09-snippet.html'
NEW_IDS = ['e2017-09-29', 'e2019-07-16', 'e2020-08-28', 'e2021-04-09', 'e2022-02-10', 'e2025-02-18']

page = io.open(PAGE, encoding='utf-8', newline='').read()
raw = io.open(SNIP, encoding='utf-8', newline='').read()

crlf = page.count('\r\n')
lf = page.count('\n') - crlf
assert crlf > 0 or lf > 0, 'no newlines?'
EOL = '\r\n' if crlf >= lf else '\n'
raw = raw.replace('\r\n', '\n').replace('\n', EOL)

# split into 6 <li> entries
entries = []
rest = raw
while True:
    i = rest.find('<li class="ps-row ps-deep reveal"')
    if i < 0:
        break
    j = rest.find('</li>', i)
    assert j > 0
    j += len('</li>')
    entries.append(rest[i:j])
    rest = rest[j:]
assert len(entries) == 6, 'got %d entries' % len(entries)
entry_ids = [re.search(r'id="(e[^"]+)"', e).group(1) for e in entries]
assert entry_ids == NEW_IDS, 'order mismatch: %s' % entry_ids

# structural sanity: 4 ps-sec sections, 1 quote, 1 zh, 1 permalink
for e in entries:
    assert e.count('<div class="ps-sec">') == 4, 'ps-sec!=4: %s' % e[:60]
    assert e.count('<blockquote class="ps-quote">') == 1
    assert e.count('class="ps-zh"') == 1
    assert e.count('<a class="ps-date" href="#') == 1, 'permalink'
    assert e.count('<span class="ps-src">') == 1
    assert e.strip().endswith('</li>')

# pre assertions
n0 = page.count('<li class="ps-row ps-deep reveal"')
assert n0 == 103, 'rows before=%d' % n0
for pid in NEW_IDS:
    assert ('id="%s"' % pid) not in page, 'dup id %s' % pid

GROUPS = [
    ('<li class="ps-row ps-deep reveal" id="e2017-11-01">', ['e2017-09-29']),
    ('<li class="ps-row ps-deep reveal" id="e2019-09-28">', ['e2019-07-16']),
    ('<li class="ps-row ps-deep reveal" id="e2020-09-22">', ['e2020-08-28']),
    ('<li class="ps-row ps-deep reveal" id="e2021-07">', ['e2021-04-09']),
    ('<li class="ps-row ps-deep reveal" id="e2022-03-08">', ['e2022-02-10']),
    ('<li class="ps-row ps-deep reveal" id="e2025-03-28">', ['e2025-02-18']),
]
by_id = dict(zip(NEW_IDS, entries))
for anchor, ids in GROUPS:
    assert page.count(anchor) == 1, 'anchor not unique: %s' % anchor
    block = EOL.join(by_id[i] for i in ids)
    page = page.replace(anchor, block + EOL + EOL + anchor)

n1 = page.count('<li class="ps-row ps-deep reveal"')
assert n1 == 109, 'rows after=%d' % n1
for pid in NEW_IDS:
    assert page.count('id="%s"' % pid) == 1
for a, _ in GROUPS:
    assert page.count(a) == 1

io.open(PAGE, 'w', encoding='utf-8', newline='').write(page)
print('OK: primary.html 103 -> 109; ids:', ', '.join(NEW_IDS))
