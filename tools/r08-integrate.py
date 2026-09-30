# -*- coding: utf-8 -*-
"""V8 R08: insert 10 tweet cards into x-posts.html chronologically (6 grouped inserts).
Pattern: fragment + per-anchor replace with new = fragment + anchor (anchor preserved)."""
import io, re

PAGE = 'x-posts.html'
SNIP = 'tools/r08-snippet.html'
NEW_IDS = ['p2020-03-06', 'p2020-05-01', 'p2022-03-26', 'p2022-04-14', 'p2022-05-13',
           'p2022-11-01', 'p2022-12-18', 'p2023-07-23', 'p2024-04-05', 'p2025-03-28']

page = io.open(PAGE, encoding='utf-8', newline='').read()
raw = io.open(SNIP, encoding='utf-8', newline='').read()

# CRLF normalization
crlf = page.count('\r\n')
lf = page.count('\n') - crlf
assert crlf >= lf and crlf > 0, 'target not CRLF'
raw = raw.replace('\r\n', '\n').replace('\n', '\r\n')

# split fragment into 10 cards
cards = []
rest = raw
while True:
    i = rest.find('<div class="tweet-card"')
    if i < 0:
        break
    j = rest.find('</div>', rest.find('tweet-note', i))
    assert j > 0, 'card not closed'
    j += len('</div>')
    card = rest[i:j]
    # capture trailing blank line as separator
    cards.append(card)
    rest = rest[j:]
assert len(cards) == 10, 'expected 10 cards, got %d' % len(cards)
card_ids = [re.search(r'id="(p[^"]+)"', c).group(1) for c in cards]
assert card_ids == NEW_IDS, 'card order mismatch: %s' % card_ids

# structural sanity per card
for c in cards:
    assert c.count('<p class="tweet-text">') == 1, 'tweet-text!=1: %s' % c[:60]
    assert c.count('<p class="tweet-zh">') == 1, 'tweet-zh!=1: %s' % c[:60]
    assert c.count('<p class="tweet-note">') == 1, 'tweet-note!=1: %s' % c[:60]
    assert c.count('<div class="tweet-top">') == 1 and c.count('tweet-date') == 1
    assert c.count('<a class="tweet-date" href="#') == 1, 'permalink badge needed'
    assert c.strip().endswith('</div>')

# pre assertions on page
n0 = page.count('<div class="tweet-card"')
assert n0 == 13, 'cards before=%d' % n0
for pid in NEW_IDS:
    assert ('id="%s"' % pid) not in page, 'dup id: %s' % pid

# grouped inserts: before-anchor -> card ids
GROUPS = [
    ('<div class="tweet-card" id="p2021-03-02">', ['p2020-03-06', 'p2020-05-01']),
    ('<div class="tweet-card" id="p2022-10-26">', ['p2022-03-26', 'p2022-04-14', 'p2022-05-13']),
    ('<div class="tweet-card" id="p2022-11-28">', ['p2022-11-01']),
    ('<div class="tweet-card" id="p2023-11-04">', ['p2022-12-18', 'p2023-07-23']),
    ('<div class="tweet-card" id="p2024-10-13">', ['p2024-04-05']),
    ('<div class="tweet-card" id="p2025-05-03">', ['p2025-03-28']),
]
by_id = dict(zip(NEW_IDS, cards))
for anchor, ids in GROUPS:
    assert page.count(anchor) == 1, 'anchor not unique: %s' % anchor
    block = '\r\n\r\n'.join(by_id[i] for i in ids)
    page = page.replace(anchor, block + '\r\n\r\n  ' + anchor)

# post assertions
n1 = page.count('<div class="tweet-card"')
assert n1 == 23, 'cards after=%d' % n1
for pid in NEW_IDS:
    assert page.count('id="%s"' % pid) == 1, 'id not unique after: %s' % pid
for a, _ in GROUPS:
    assert page.count(a) == 1, 'anchor duplicated: %s' % a
assert page.count('\r\n') > page.count('\n') - page.count('\r\n')

io.open(PAGE, 'w', encoding='utf-8', newline='').write(page)
print('OK: x-posts.html 13 -> 23 cards; ids:', ', '.join(NEW_IDS))
