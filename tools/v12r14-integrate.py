# -*- coding: utf-8 -*-
"""V12 R14：互链扩展——e2025-03-28 None href 修复 + 五档 materials 追加 6 对（扫描+人工裁决）。
锚=各档 materials 收尾。断言失败不落盘。"""
import io

PATH = 'tools/events-data.py'
s = io.open(PATH, encoding='utf-8').read()

# 0) None href 修复（镜像检索锚=先例同款）
old_none = '{"kind": "external", "href": None, "date": "2025.03",'
new_none = '{"kind": "external", "href": "https://elonmuskarchive.org/agents/search?q=xAI%20acquires%20X", "date": "2025.03",'
assert s.count(old_none) == 1
s = s.replace(old_none, new_none)

ADD = [
    # (事件 id, 新材料块, 唯一性锚=该档现有材料 href)
    ('e2024-01-29',
     '''            {"kind": "ledger", "href": "primary.html#e2019-07-16", "date": "2019.07.16",
             "label": {"zh": "言行账本 e2019-07-16 · 2019 首场技术发布会（弧线起点）", "en": "Ledger e2019-07-16 · the 2019 debut"},
             "note": {"zh": "R14 互链扩展：缝合线与缝纫机（1024 通道）的起点记录", "en": "R14 xlinks: where the thread-and-sewing-machine story starts"}},
''',
     '"href": "primary.html#e2020-08-28", "date": "2020.08.28"'),
    ('e2024-01-29',
     '''            {"kind": "interview", "href": "interviews.html#i2024-01-29", "date": "2024.01.29",
             "label": {"zh": "访谈 i2024-01-29 · 首植同日访谈", "en": "Interview i2024-01-29 · same-day interview"},
             "note": {"zh": "R14 互链扩展：同日双源（X 官宣+访谈口径）", "en": "R14 xlinks: same-day second source"}},
''',
     '"href": "primary.html#e2019-07-16", "date": "2019.07.16"'),
    ('e2024-01-29',
     '''            {"kind": "interview", "href": "interviews.html#i2019-11-12", "date": "2019.11.12",
             "label": {"zh": "访谈 i2019-11-12 · 2019 脑机访谈", "en": "Interview i2019-11-12 · the 2019 brain interview"},
             "note": {"zh": "R14 互链扩展：首植五年前的口径对读", "en": "R14 xlinks: the 2019 framing, read against 2024"}},
''',
     '"href": "interviews.html#i2024-01-29", "date": "2024.01.29"'),
    ('e2026-02-10',
     '''            {"kind": "interview", "href": "interviews.html#i2026-07-23", "date": "2026.07.23",
             "label": {"zh": "访谈 i2026-07-23 · Economist（AI 收入占比之问）", "en": "Interview i2026-07-23 · The Economist"},
             "note": {"zh": "R14 互链扩展：成绩单的同期外部口径", "en": "R14 xlinks: the同期 external read of the report card"}},
''',
     '"href": "x-posts.html#p2023-11-04", "date": "2023.11.04"'),
    ('e2023-11',
     '''            {"kind": "interview", "href": "interviews.html#i2026-02-05", "date": "2026.02.05",
             "label": {"zh": "访谈 i2026-02-05 · Dwarkesh（AI5 与 Grok 栈）", "en": "Interview i2026-02-05 · Dwarkesh on the stack"},
             "note": {"zh": "R14 互链扩展：模型栈的同期访谈口径", "en": "R14 xlinks: the stack, in his own interview words"}},
''',
     '"href": "documents.html#d2026-01", "date": "2026.01"'),
    ('e2024-07',
     '''            {"kind": "ledger", "href": "primary.html#e2025-11-06", "date": "2025.11.06",
             "label": {"zh": "言行账本 e2025-11-06 · 股东会与薪酬包通过", "en": "Ledger e2025-11-06 · the shareholder meeting"},
             "note": {"zh": "R14 互链扩展：政治参与与公司治理的交汇点", "en": "R14 xlinks: where politics meets corporate governance"}},
''',
     '"href": "https://elonmuskarchive.org/agents/search?q=America%20Party", "date": "2026"'),
]

for eid, block, anchor in ADD:
    # 定位该档 materials 数组内锚条目收尾 "}},\n" 后插入
    i = s.find('"id": "%s"' % eid)
    assert i > 0, eid
    j = s.find(anchor, i)
    assert j > 0, (eid, anchor)
    end = s.find('}},', j)
    assert end > 0
    ins = end + 3
    s = s[:ins] + '\n' + block.rstrip('\n') + s[ins:]

ns = {}
exec(compile(s, PATH, 'exec'), ns)
ed = ns
for qid, n in [('e2024-01-29', 8), ('e2026-02-10', 5), ('e2023-11', 7), ('e2024-07', 5), ('e2025-03-28', 4)]:
    e = [x for x in ed['EVENTS'] if x['id'] == qid][0]
    assert len(e['materials']) == n, (qid, len(e['materials']), n)
    errs = ed['validate']()
    assert not errs, errs[:3]

io.open(PATH, 'w', encoding='utf-8', newline='\n').write(s)
print('OK: None href fixed + 6 pairs appended, in-memory validate clean, written')
