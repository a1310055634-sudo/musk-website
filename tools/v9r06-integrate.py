# -*- coding: utf-8 -*-
"""V9-20 R06 集成：documents.html 14 → 18 份（S-1 2010 / Acronyms 2010 / Raptor 2021 / 10-K 2022）
+ 计数口径（og + doc-path 双语）+ reading.html 计数。
原则：所有 replace 均带唯一性断言，防止静默失败假成功。"""
import io, os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SNIP_A = io.open('tools/v9r06-snippet.html', encoding='utf-8', newline='').read()
SNIP_B = io.open('tools/v9r06-snippet2.html', encoding='utf-8', newline='').read()
assert 'id="d2010-01-29"' in SNIP_A and 'id="d2010-05-04"' in SNIP_A
assert 'id="d2021-11-26"' in SNIP_B and 'id="d2022-02-07"' in SNIP_B

def sub1(s, old, new, tag):
    n = s.count(old)
    assert n == 1, f'[{tag}] 预期唯一匹配，实际 {n} 次'
    return s.replace(old, new)

# ---------- documents.html ----------
p = 'documents.html'
s = io.open(p, encoding='utf-8', newline='').read()

a1 = '  <!-- ② 2016 Part Deux -->'
a2 = '  <!-- ③d 2022.04.11 董事会撤销 8-K/A -->'
assert s.count(a1) == 1 and s.count(a2) == 1
s = s.replace(a1, SNIP_A + a1)
s = s.replace(a2, SNIP_B + a2)

s = sub1(s,
    '一手文档馆——秘密蓝图、私有化方案信、收购与退市备案、股东大会 proxy 等十四份原文。',
    '一手文档馆——秘密蓝图、IPO 招股书、SpaceX 全员信、私有化方案信、收购与退市备案、股东大会 proxy 等十八份原文。',
    'og')

s = sub1(s,
    'Read the fourteen documents in order and you get a 20-year strategy evolution in primary sources: 2006 the product ladder; 2016 the ecosystem expansion; 2018 the go-private attempt and its emergency brake; 2022 the full takeover arc (agreement, board interlude, proxy chronology, closing and delisting); 2022.11 the culture ultimatum; 2023.04 the energy ending and 2023.07 the AI charter; 2024 the Delaware reckoning, re-ratification and the Texas move; 2025.09 the AI ending continued.',
    'Read the eighteen documents in order and you get a 20-year strategy evolution in primary sources: 2006 the product ladder; 2010 the IPO prospectus (with the first key-man risk factor) and SpaceX\u2019s acronym ban; 2016 the ecosystem expansion; 2018 the go-private attempt and its emergency brake; 2021.11 the Raptor bankruptcy warning; 2022 the full takeover arc (agreement, board interlude, proxy chronology, closing and delisting) and the key-man risk retitled Technoking; 2022.11 the culture ultimatum; 2023.04 the energy ending and 2023.07 the AI charter; 2024 the Delaware reckoning, re-ratification and the Texas move; 2025.09 the AI ending continued.',
    'path-en')

s = sub1(s,
    '按时间顺序读完这十四份文档，你得到的就是一部用第一手材料写成的二十年战略演化史：2006 产品阶梯 → 2016 生态扩张 → 2018 私有化尝试与急刹车 → 2022 收购全案（协议、董事会插曲、proxy 全日程、交割退市）→ 2022.11 文化通牒 → 2023.04 能源终局与 2023.07 AI 章程 → 2024 特拉华清算后的再批与迁州 → 2025.09 的 AI 终局续章。',
    '按时间顺序读完这十八份文档，你得到的就是一部用第一手材料写成的二十年战略演化史：2006 产品阶梯 → 2010 IPO 招股书（含第一份「关键人风险」因子）与 SpaceX 缩写禁令信 → 2016 生态扩张 → 2018 私有化尝试与急刹车 → 2021.11 Raptor 破产警报 → 2022 收购全案（协议、董事会插曲、proxy 全日程、交割退市）与更名「Technoking」的关键人风险 → 2022.11 文化通牒 → 2023.04 能源终局与 2023.07 AI 章程 → 2024 特拉华清算后的再批与迁州 → 2025.09 的 AI 终局续章。',
    'path-zh')

n_docs = s.count('<article class="doc-article" id="d')
assert n_docs == 18, n_docs
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print(f'OK documents.html: 14 → {n_docs} 份')

# ---------- reading.html ----------
p = 'reading.html'
s = io.open(p, encoding='utf-8', newline='').read()
s = sub1(s, '<a href="documents.html">十四份一手文档</a>', '<a href="documents.html">十八份一手文档</a>', 'reading')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK reading.html 计数 14 → 18')

# ---------- 检索断言同步 ----------
p = 'tools/build-search-index.py'
s = io.open(p, encoding='utf-8', newline='').read()
s = sub1(s, "'一手文档': 14,", "'一手文档': 18,", 'assert-docs')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK build-search-index.py 断言 一手文档 14 → 18')
print('ALL INTEGRATION DONE')
