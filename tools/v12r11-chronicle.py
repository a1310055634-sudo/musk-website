# -*- coding: utf-8 -*-
"""V12 R11 I：chronicle.html 近年补齐 11 条（tesla 7/spacex 2/x 2）。
锚=段内既有条目整行。断言失败不落盘。"""
import io

PATH = 'chronicle.html'
s = io.open(PATH, encoding='utf-8').read()
orig = s

T = [
    # (锚行子串, 方向 before/after, 新条行)
    ('<div class="cy-year"><span class="cy-y">2025.11.06</span>', 'before',
     '    <div class="cy-year"><span class="cy-y">2023.03.01</span><div class="cy-ev" id="c2023-03-01">Investor Day 与 Master Plan Part 3：「地球全面电动化」的工程路线图（<a href="primary.html#e2023-03-01">账本条目</a>）。</div></div>\n'
     '    <div class="cy-year"><span class="cy-y">2023.05.15</span><div class="cy-ev" id="c2023-05-15">第二巡回法院三法官庭终审：SolarCity 收购案马斯克胜诉，六年诉讼法律程序终结（<a href="primary.html#e2023-05-15">账本条目</a>）。</div></div>\n'
     '    <div class="cy-year"><span class="cy-y">2023.10.18</span><div class="cy-ev" id="c2023-10-18">Q3 财报电话会：降价压毛利，Cybertruck 交付倒计时 43 天（<a href="primary.html#e2023-10-18">账本条目</a>）。</div></div>\n'
     '    <div class="cy-year"><span class="cy-y">2024.10.10</span><div class="cy-ev" id="c2024-10-10">「We,Robot」发布会：Cybercab 无人出租与 Robovan 亮相（<a href="primary.html#e2024-10-10">账本条目</a>）。</div></div>\n'
     '    <div class="cy-year"><span class="cy-y">2025.06.22</span><div class="cy-ev" id="c2025-06-22">Robotaxi 奥斯汀付费服务开跑——八年欠账后第一次真发车（<a href="events.html#e2025-06-22">事件档案</a>）。</div></div>\n'
     '    <div class="cy-year"><span class="cy-y">2025.09.17</span><div class="cy-ev" id="c2025-09-17">万亿薪酬包 proxy 备案：12 档市值里程碑 2 万亿→8.5 万亿（<a href="documents.html#d2025-09-17">proxy 摘录</a>）。</div></div>'),
    ('<div class="cy-year"><span class="cy-y">2025.11.06</span>', 'after',
     '    <div class="cy-year"><span class="cy-y">2026.07</span><div class="cy-ev" id="c2026-07">Fremont Optimus 产线实拍与 AI5 上机口径——「能不能做」变成「能不能造」（<a href="events.html#e2026-07">事件档案</a>）。</div></div>'),
    ('<div class="cy-year"><span class="cy-y">2024.10.13</span>', 'before',
     '    <div class="cy-year"><span class="cy-y">2024.03.18</span><div class="cy-ev" id="c2024-03-18">Starbase 员工会：两飞数据复盘与第三次试飞预期（<a href="primary.html#e2024-03-18">账本条目</a>）。</div></div>'),
    ('<div class="cy-year"><span class="cy-y">2024.10.13</span>', 'after',
     '    <div class="cy-year"><span class="cy-y">2026.06.12</span><div class="cy-ev" id="c2026-06-12">SpaceX IPO 定价：555,555,555 股 × $135.00，SPCX 登陆纳斯达克，募资约 750 亿美元（<a href="documents.html#d2026-06-12">424B4 摘录</a>）。</div></div>'),
    ('<div class="cy-year"><span class="cy-y">2023.07.23</span>', 'after',
     '    <div class="cy-year"><span class="cy-y">2023.11.29</span><div class="cy-ev" id="c2023-11-29">DealBook 峰会回应广告主抵制：「别想勒索我用广告费」（<a href="primary.html#e2023-11-29">账本条目</a>）。</div></div>\n'
     '    <div class="cy-year"><span class="cy-y">2024.07</span><div class="cy-ev" id="c2024-07">政治参与升级：大选背书入场，后演变为 America Party（2025.07）（<a href="events.html#e2024-07">事件档案</a>）。</div></div>'),
]

before_cy = s.count('class="cy-year"')
for anchor, where, block in T:
    assert s.count(anchor) == 1, 'anchor not unique: %s (%d)' % (anchor[:60], s.count(anchor))
for qid in ['c2023-03-01', 'c2023-05-15', 'c2023-10-18', 'c2024-10-10', 'c2025-06-22',
            'c2025-09-17', 'c2026-07', 'c2024-03-18', 'c2026-06-12', 'c2023-11-29', 'c2024-07']:
    assert ('id="%s"' % qid) not in s, 'id exists: ' + qid

for anchor, where, block in T:
    i = s.index(anchor)
    line_start = s.rfind('\n', 0, i) + 1
    line_end = s.index('\n', i)
    line = s[line_start:line_end]
    if where == 'before':
        s = s[:line_start] + block + '\n' + line + s[line_end:]
    else:
        s = s[:line_end] + '\n' + block + s[line_end:]

after_cy = s.count('class="cy-year"')
assert after_cy == before_cy + 11, 'cy-year %d -> %d != +11' % (before_cy, after_cy)
assert s.count('id="c2025-11-06"') == 1  # 既有锚条无恙
io.open(PATH, 'w', encoding='utf-8', newline='\n').write(s)
print('OK: chronicle %d -> %d entries (+11)' % (before_cy, after_cy))
