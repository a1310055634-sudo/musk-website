# -*- coding: utf-8 -*-
"""R03 集成：documents.html +5 份 EDGAR 文档（片段文件整块单次重建）+ 计数文案 + 交叉引用。
原则：所有 replace 均带唯一性断言，防止静默失败假成功。"""
import io, os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SNIP = io.open('tools/r03-snippet.html', encoding='utf-8', newline='').read()

# ---------- 拆分三段片段 ----------
m_a = SNIP.index('  <!-- ③c 2018.08.14 特别委员会 8-K -->')
m_b = SNIP.index('  <!-- ③e 2022.07.26 并购 proxy -->')
m_c = SNIP.index('  <!-- ⑤b 2024 薪酬再批与迁州 proxy -->')
SNIP_A = SNIP[m_a:m_b]   # d2018-08-14 + d2022-04-11
SNIP_B = SNIP[m_b:m_c]   # d2022-07-26 + d2022-10-27
SNIP_C = SNIP[m_c:]      # d2024-04-29
assert 'id="d2018-08-14"' in SNIP_A and 'id="d2022-04-11"' in SNIP_A
assert 'id="d2022-07-26"' in SNIP_B and 'id="d2022-10-27"' in SNIP_B
assert 'id="d2024-04-29"' in SNIP_C

def sub1(s, old, new, tag):
    n = s.count(old)
    assert n == 1, f'[{tag}] 预期唯一匹配，实际 {n} 次'
    return s.replace(old, new)

# ---------- documents.html ----------
p = 'documents.html'
s = io.open(p, encoding='utf-8', newline='').read()

a1 = '  <!-- ③b 2022 Merger Agreement -->'
a2 = '  <!-- ③ 2022 Extremely Hardcore -->'
a3 = '  <!-- ⑥ 2025 Part IV -->'
assert s.count(a1) == 1 and s.count(a2) == 1 and s.count(a3) == 1
s = s.replace(a1, SNIP_A + a1)
s = s.replace(a2, SNIP_B + a2)
s = s.replace(a3, SNIP_C + a3)

s = sub1(s, '收购协议条款等九份原文。', '收购与退市备案、股东大会 proxy 等十四份原文。', 'og')
s = sub1(s,
    'Read the nine documents in order and you get a 20-year strategy evolution in primary sources: 2006 the product ladder; 2016 the ecosystem expansion; 2018 the go-private attempt; 2022.04 the merger agreement and 2022.11 the culture ultimatum; 2023.04 the energy ending and 2023.07 the AI charter; 2025.09 the AI ending continued.',
    'Read the fourteen documents in order and you get a 20-year strategy evolution in primary sources: 2006 the product ladder; 2016 the ecosystem expansion; 2018 the go-private attempt and its emergency brake; 2022 the full takeover arc (agreement, board interlude, proxy chronology, closing and delisting); 2022.11 the culture ultimatum; 2023.04 the energy ending and 2023.07 the AI charter; 2024 the Delaware reckoning, re-ratification and the Texas move; 2025.09 the AI ending continued.',
    'path-en')
s = sub1(s,
    '按时间顺序读完这九份文档，你得到的就是一部用第一手材料写成的二十年战略演化史：2006 产品阶梯 → 2016 生态扩张 → 2018 私有化尝试 → 2022.04 收购协议与 2022.11 文化通牒 → 2023.04 能源终局与 2023.07 AI 章程 → 2025.09 的 AI 终局续章。',
    '按时间顺序读完这十四份文档，你得到的就是一部用第一手材料写成的二十年战略演化史：2006 产品阶梯 → 2016 生态扩张 → 2018 私有化尝试与急刹车 → 2022 收购全案（协议、董事会插曲、proxy 全日程、交割退市）→ 2022.11 文化通牒 → 2023.04 能源终局与 2023.07 AI 章程 → 2024 特拉华清算后的再批与迁州 → 2025.09 的 AI 终局续章。',
    'path-zh')
s = sub1(s,
    '链尾全文见 EDGAR 原件与 DEFM14A（0001193125-22-202163）。',
    '链尾全文见 EDGAR 原件与 DEFM14A（<a href="#d2022-07-26" style="color:var(--accent)">0001193125-22-202163，本站词条</a>）。',
    'd0425-link')
assert s.count('<article class="doc-article" id="d') == 14, s.count('<article class="doc-article" id="d')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK documents.html: 9 → 14 份')

# ---------- reading.html ----------
p = 'reading.html'
s = io.open(p, encoding='utf-8', newline='').read()
s = sub1(s, '<a href="documents.html">九份一手文档</a>', '<a href="documents.html">十四份一手文档</a>', 'reading')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK reading.html 计数')

# ---------- platform-x.html ----------
p = 'platform-x.html'
s = io.open(p, encoding='utf-8', newline='').read()
s = sub1(s,
    '<a href="primary.html#e2022-04-09" data-en="Ledger: the private text five days before the offer">账本：要约五天前的那条私信</a></p>',
    '<a href="primary.html#e2022-04-09" data-en="Ledger: the private text five days before the offer">账本：要约五天前的那条私信</a><a href="documents.html#d2022-04-11" data-en="8-K/A: the five-day board episode">文档：董事会提名五日始末</a><a href="documents.html#d2022-07-26" data-en="Proxy: the April 13 offer letter, full text">文档：4.13 要约信全文与全日程</a></p>',
    'px-0414')
s = sub1(s,
    '<a href="x-posts.html#p2022-10-28" data-en="Original posts">原帖收录</a><a href="capital-evolution.html#flow" data-en="Capital flow">资本流向图</a>',
    '<a href="x-posts.html#p2022-10-28" data-en="Original posts">原帖收录</a><a href="documents.html#d2022-10-27" data-en="Final 8-K: closing and delisting">文档：交割退市 8-K</a><a href="capital-evolution.html#flow" data-en="Capital flow">资本流向图</a>',
    'px-1028')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK platform-x.html 交叉引用 ×2')

# ---------- promises.html ----------
p = 'promises.html'
s = io.open(p, encoding='utf-8', newline='').read()
s = sub1(s,
    '<a href="documents.html#d2018-08-07" data-en="Privatization letter">私有化方案信</a>',
    '<a href="documents.html#d2018-08-07" data-en="Privatization letter">私有化方案信</a><a href="documents.html#d2018-08-14" data-en="Special committee 8-K">特别委员会 8-K</a>',
    'pv-links')
s = sub1(s,
    '<li><a href="documents.html#d2018-08-07">文档 d2018-08-07</a><span data-en="Privatization letter, full text">私有化方案信全文</span></li>',
    '<li><a href="documents.html#d2018-08-07">文档 d2018-08-07</a><span data-en="Privatization letter, full text">私有化方案信全文</span></li><li><a href="documents.html#d2018-08-14">文档 d2018-08-14</a><span data-en="Special-committee 8-K, one week later: no formal proposal yet received">一周后的特别委员会 8-K：尚无正式提案</span></li>',
    'pv-source')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK promises.html 交叉引用 ×2')
print('ALL INTEGRATION DONE')
