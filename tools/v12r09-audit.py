# -*- coding: utf-8 -*-
"""R09 质量节点①：三口径盘点（页面 DOM / 索引 / 生成器断言值）+ 年份分布。
零漂移断言 + 生成 qa/v12/round-09/AUDIT-v3.md 底稿数据。"""
import io, json, re
from collections import Counter

def count_page(path, pat):
    t = io.open(path, encoding='utf-8').read()
    return len(re.findall(pat, t))

PAGE_DOM = [
    ('言行实录', 'primary.html', r'class="ps-row ps-deep reveal" id="e'),
    ('一手文档', 'documents.html', r'<article class="doc-article" id="d'),
    ('访谈与表态', 'interviews.html', r'<article class="iv-item" id="i'),
    ('X 帖', 'x-posts.html', r'<div class="tweet-card" id="p20'),
    ('争议深读', 'controversy.html', r'id="(union|twitter|sec-sec|sec-pedo|autopilot)"'),
    ('编年史', 'chronicle.html', r'class="cy-ev"'),
    ('财务全景', 'finance.html', r'id="(tesla|spacex|x|xai)"'),
    ('事件档案', 'events.html', r'class="ev-item'),
    ('社区资源', 'resources.html', r'<article class="rs-item"'),
]

s = io.open('search-index.js', encoding='utf-8').read()
idx = json.loads(s[s.find('['):s.rfind(']') + 1])
idx_counts = Counter(d['t'] for d in idx)

# 生成器断言值（verify.py 的期望基线 = build-search-index.py 守护断言）
GEN = {'言行实录': 124, '一手文档': 37, '访谈与表态': 51, 'X 帖': 44, '争议深读': 5,
       '编年史': 53, '财务全景': 4, '事件档案': 16, '社区资源': 49}

rows, drift = [], 0
print('%-8s | %s | %s | %s' % ('类型', '页面DOM', '索引', '生成器'))
for name, page, pat in PAGE_DOM:
    dom = count_page(page, pat)
    ix = idx_counts.get(name, 0)
    gen = GEN[name]
    ok = (dom == ix == gen)
    if not ok:
        drift += 1
    rows.append((name, dom, ix, gen, ok))
    print('%-8s | %4d | %4d | %4d  %s' % (name, dom, ix, gen, 'OK' if ok else 'DRIFT!'))

total = sum(r[1] for r in rows)
print('合计 DOM=%d 索引=%d' % (total, len(idx)))
assert drift == 0, 'drift in %d types' % drift
assert total == len(idx) == 383

# ---- 年份分布 ----
def years_of(page, pat, gpos):
    t = io.open(page, encoding='utf-8').read()
    return Counter(m.group(gpos)[:4] for m in re.finditer(pat, t))

y_posts = years_of('x-posts.html', r'id="(p\d{4}-\d{2}(?:-\d{2})?)"', 1)
y_ledger = years_of('primary.html', r'class="ps-row ps-deep reveal" id="(e\d{4}(?:-\d{2}(?:-\d{2})?)?)"', 1)
y_iv = years_of('interviews.html', r'<article class="iv-item" id="(i\d{4}(?:-\d{2}(?:-\d{2})?)?)"', 1)
y_docs = years_of('documents.html', r'<article class="doc-article" id="(d\d{4}(?:-\d{2}(?:-\d{2})?)?)"', 1)

def show(title, yc):
    print('\n' + title + '（%d 条）' % sum(yc.values()))
    for y in sorted(yc):
        print('  %s: %s' % (y, '█' * yc[y] + ' %d' % yc[y]))

show('X 帖按年', y_posts)
show('账本按年', y_ledger)
show('访谈按年', y_iv)
show('文档按年', y_docs)

io.open('qa/v12/round-09/audit-data.json', 'w', encoding='utf-8', newline='\n').write(json.dumps({
    'rows': [{'type': r[0], 'dom': r[1], 'index': r[2], 'gen': r[3], 'ok': r[4]} for r in rows],
    'total_dom': total, 'total_index': len(idx),
    'years': {'x_posts': y_posts, 'ledger': y_ledger, 'interviews': y_iv, 'documents': y_docs},
}, ensure_ascii=False, indent=1))
print('\nAUDIT data written. ZERO-DRIFT confirmed.')
