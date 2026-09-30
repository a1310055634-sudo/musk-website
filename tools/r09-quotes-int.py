# -*- coding: utf-8 -*-
"""V8 R09: insert 6 qs-cards into quotes.html (chronological, anchor-preserved)."""
import io, re

PAGE = 'quotes.html'
SNIP = 'tools/r09-quotes.html'
NEW_IDS = ['e2017-09-29', 'e2019-07-16', 'e2020-08-28', 'e2021-04-09', 'e2022-02-10', 'e2025-02-18']

page = io.open(PAGE, encoding='utf-8', newline='').read()
raw = io.open(SNIP, encoding='utf-8', newline='').read()

crlf = page.count('\r\n')
lf = page.count('\n') - crlf
EOL = '\r\n' if crlf >= lf else '\n'
raw = raw.replace('\r\n', '\n').replace('\n', EOL)

cards = []
rest = raw
while True:
    i = rest.find('<a class="qs-card"')
    if i < 0:
        break
    j = rest.find('</a>', i)
    assert j > 0
    j += 4
    cards.append(rest[i:j])
    rest = rest[j:]
assert len(cards) == 6, 'got %d cards' % len(cards)
card_ids = [re.search(r'href="primary\.html#(e[\d-]+)"', c).group(1) for c in cards]
assert card_ids == NEW_IDS, 'order: %s' % card_ids
for c in cards:
    assert c.count('qs-date') == 1 and c.count('qs-en') == 1 and c.count('qs-zh') == 1 and c.count('qs-src') == 1

n0 = len(re.findall(r'qs-card" href="primary\.html#e', page))
assert n0 == 90, 'cards before=%d' % n0
for pid in NEW_IDS:
    assert ('primary.html#%s' % pid) not in page, 'dup card %s' % pid

GROUPS = [
    ('<a class="qs-card" href="primary.html#e2017-11-01">', ['e2017-09-29']),
    ('<a class="qs-card" href="primary.html#e2022-03-08">', ['e2019-07-16']),
    ('<a class="qs-card" href="primary.html#e2020-09-22">', ['e2020-08-28']),
    ('<a class="qs-card" href="primary.html#e2021-08">', ['e2021-04-09']),
    ('<a class="qs-card" href="primary.html#e2022-04-14">', ['e2022-02-10']),
    ('<a class="qs-card" href="primary.html#e2025-03-28">', ['e2025-02-18']),
]
by_id = dict(zip(NEW_IDS, cards))
for anchor, ids in GROUPS:
    assert page.count(anchor) == 1, 'anchor not unique: %s' % anchor
    block = EOL.join(by_id[i] for i in ids)
    page = page.replace(anchor, block + EOL + EOL + anchor)

n1 = len(re.findall(r'qs-card" href="primary\.html#e', page))
assert n1 == 96, 'cards after=%d' % n1
for a, _ in GROUPS:
    assert page.count(a) == 1

io.open(PAGE, 'w', encoding='utf-8', newline='').write(page)
print('OK: quotes.html 90 -> 96 cards')
