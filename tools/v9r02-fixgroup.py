# -*- coding: utf-8 -*-
"""V9-20 R02: 年份条归位修复。
①「2022」条被 R02 集成脚本误插到 p2021-05-05 之前（锚选在 p2022-03-26 卡标签，条在其前）——
  移回 p2022-03-26 之前，使 p2021-05-05/p2021-11-02 归入 2021 组；
②存量错位：「2023」条压在 p2022-12-18（2022.12.18 帖）之前——移到 p2023-07-23 之前。
每步替换计数必须打印，异常即中止（不改文件）。"""
import io, sys

PATH = 'x-posts.html'
raw = io.open(PATH, encoding='utf-8', newline='').read()
NL = '\r\n' if '\r\n' in raw else '\n'
D = NL
s = raw

def rep(text, old, new, label, expect=1):
    n = text.count(old)
    if n != expect:
        print(f'✗ {label}: 锚出现 {n} 次（期望 {expect}），中止（文件未改）')
        sys.exit(1)
    print(f'✓ {label}: 替换 {n} 处')
    return text.replace(old, new, expect)

# ① 2022 条归位（实况：条与 05-05 卡之间为 8 空格；03-26 卡行为零缩进）
s = rep(s,
        f'      <div class="xp-year" aria-hidden="true">2022</div>{D}        <div class="tweet-card" id="p2021-05-05">',
        f'<div class="tweet-card" id="p2021-05-05">',
        '摘除误插的 2022 条（p2021-05-05 前）')
s = rep(s,
        f'<div class="tweet-card" id="p2022-03-26">',
        f'      <div class="xp-year" aria-hidden="true">2022</div>{D}    <div class="tweet-card" id="p2022-03-26">',
        '2022 条归位到 p2022-03-26 之前')

# ② 存量：2023 条压住 p2022-12-18
s = rep(s,
        f'      <div class="xp-year" aria-hidden="true">2023</div>{D}    <div class="tweet-card" id="p2022-12-18">',
        f'<div class="tweet-card" id="p2022-12-18">',
        '摘除压线的 2023 条（p2022-12-18 前）')
s = rep(s,
        f'<div class="tweet-card" id="p2023-07-23">',
        f'      <div class="xp-year" aria-hidden="true">2023</div>{D}<div class="tweet-card" id="p2023-07-23">',
        '2023 条归位到 p2023-07-23 之前')

# 断言：年份分组与卡序一致
import re
seq = re.findall(r'<div class="(?:tweet-card" id="|xp-year" aria-hidden="true">)([\dp][\d-]*)', s)
cur, groups = None, {}
curyear = None
cards = []
for tok in seq:
    if tok.isdigit():
        curyear = tok
    else:
        cards.append((curyear, tok))
for y, cid in cards:
    assert cid[1:5] == y, f'分组错位：{cid} 在 {y} 组'
assert len(cards) == 27, f'卡数应 27，实际 {len(cards)}'

io.open(PATH, 'w', encoding='utf-8', newline='').write(s)
print('分组断言：27 卡全部与所属年份条一致')
print('DONE v9r02-fixgroup')
