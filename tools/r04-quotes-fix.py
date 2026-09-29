# -*- coding: utf-8 -*-
"""R04 补充集成：quotes.html +10 卡（70→80，注意拼回 anchor）+ index.html 计数 83→93
+ build-search-index.py 断言 83→93。（primary.html 已由 r04-integrate.py 完成，本脚本不再触碰。）"""
import io, os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def sub1(s, old, new, tag):
    n = s.count(old)
    assert n == 1, f'[{tag}] 预期唯一匹配，实际 {n} 次'
    return s.replace(old, new)

def card(eid, date, en, zh, src):
    return (f'<a class="qs-card" href="primary.html#{eid}">\n'
            f'          <span class="qs-date">{date}</span>\n'
            f'          <p class="qs-en">{en}</p>\n'
            f'          <p class="qs-zh">{zh}</p>\n'
            f'          <span class="qs-src">{src} →</span>\n'
            f'        </a>\n\n        ')

# ============ quotes.html ============
p = 'quotes.html'
s = io.open(p, encoding='utf-8', newline='').read()
n0 = s.count('<a class="qs-card"')
assert n0 == 70, n0

s = sub1(s, '<a class="qs-card" href="primary.html#e2016">', card(
    'e2016-02-10', '2016.02.10',
    '“We’re really looking forward to the unveiling of the Model 3 at the end of next month. I think this is going to be really well-received.”',
    '我们非常期待下个月底的 Model 3 发布。我认为它会大受欢迎。',
    'Q4 2015 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2016">', 'q-e2016-02-10')

s = sub1(s, '<a class="qs-card" href="primary.html#e2016-07-20">', card(
    'e2016-05-04', '2016.05.04',
    '“The date we are setting with suppliers to get to a volume production capability with the Model 3 is July 1st next year.”',
    '我们与供应商约定的日期，是让 Model 3 在明年 7 月 1 日具备量产能力。',
    'Q1 2016 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2016-07-20">', 'q-e2016-05-04')

s = sub1(s, '<a class="qs-card" href="primary.html#e2016-09-01">', card(
    'e2016-08-03', '2016.08.03',
    '“Full autonomy is gonna come a hell of a lot faster than anyone thinks it will. … The hardware exists to create full autonomy.”',
    '完全自动驾驶的到来会快得超出所有人的想象。……实现完全自动驾驶的硬件已经存在。',
    'Q2 2016 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2016-09-01">', 'q-e2016-08-03')

s = sub1(s, '<a class="qs-card" href="primary.html#e2017-03-30">', card(
    'e2016-10-26', '2016.10.26',
    '“I expect SolarCity to be approximately cash neutral, all things considered, next year.”',
    '我预计明年，SolarCity 大致能做到现金流打平。',
    'Q3 2016 财报电话会 · stockanalysis.com 逐字稿') + card(
    'e2017-02-22', '2017.02.22',
    '“I currently think that we should be able to do 500,000 vehicles next year and 1 million vehicles by 2020.”',
    '我目前认为，明年（2018）应该能做到 50 万辆，到 2020 年做到 100 万辆。',
    'Q4 2016 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2017-03-30">', 'q-e2016-10-26+e2017-02-22')

s = sub1(s, '<a class="qs-card" href="primary.html#e2017-11-16">', card(
    'e2017-08-02', '2017.08.02',
    '“Yeah, when I said manufacturing hell and supply chain hell on Friday, I meant it.”',
    '是的，我周五说生产地狱、供应链地狱，是认真的。',
    'Q2 2017 财报电话会 · stockanalysis.com 逐字稿') + card(
    'e2017-11-01', '2017.11.01',
    '“We were in level 9. We’re now in level 8, and I think we’re close to exiting level 8.”',
    '我们曾在第 9 层。现在在第 8 层，而且我想我们快走出第 8 层了。',
    'Q3 2017 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2017-11-16">', 'q-e2017-pair')

s = sub1(s, '<a class="qs-card" href="primary.html#e2018-05-20">', card(
    'e2018-04-13', '2018.04.13',
    '“Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated.”',
    '是的，Tesla 的过度自动化是个错误。精确地说，是我的错误。人类被低估了。',
    '本人推文 · Gadgets360/NDTV · The Guardian') + card(
    'e2018-05-02', '2018.05.02',
    '“Boring, bonehead questions are not cool. Next. … We’re going to go to YouTube. … They’re killing me.”',
    '无聊的蠢问题不酷。下一个。……我们去 YouTube。……快把我无聊死了。',
    'Q1 2018 财报电话会 · BBC · Slate · The Verge') + '<a class="qs-card" href="primary.html#e2018-05-20">', 'q-e2018-pair')

s = sub1(s, '<a class="qs-card" href="primary.html#e2018-08-07">', card(
    'e2018-08-01', '2018.08.01',
    '“I’d like to apologize for being impolite on the prior call. … There’s no excuse for bad manners.”',
    '我想为上次电话会上的失礼道歉。……没礼貌没有任何借口。',
    'Q2 2018 财报电话会 · Business Insider · Bloomberg') + '<a class="qs-card" href="primary.html#e2018-08-07">', 'q-e2018-08-01')

n1 = s.count('<a class="qs-card"')
assert n1 == 80, n1
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK quotes.html: 70 → 80 卡')

# ============ index.html 计数 83→93 ============
p = 'index.html'
s = io.open(p, encoding='utf-8', newline='').read()
s = sub1(s, 'a 83-entry ledger, primary documents, interviews and posts', 'a 93-entry ledger, primary documents, interviews and posts', 'idx-en-186')
s = sub1(s, '83 条言行账本、一手文档、访谈与帖子', '93 条言行账本、一手文档、访谈与帖子', 'idx-zh-186')
s = sub1(s, 'Five entries picked from the 83-entry ledger', 'Five entries picked from the 93-entry ledger', 'idx-en-345')
s = sub1(s, '从 83 条言行账本里选出的五个节点', '从 93 条言行账本里选出的五个节点', 'idx-zh-345')
s = sub1(s, '<a href="primary.html" data-en="All 83 ledger entries →">账本全部 83 条 →</a>', '<a href="primary.html" data-en="All 93 ledger entries →">账本全部 93 条 →</a>', 'idx-395')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK index.html 计数 83→93 ×5')

# ============ build-search-index.py 断言 83→93 ============
p = 'tools/build-search-index.py'
s = io.open(p, encoding='utf-8', newline='').read()
s = sub1(s, "assert counts == {'言行实录': 83,", "assert counts == {'言行实录': 93,", 'si-assert')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK build-search-index.py 断言 83→93')
print('ALL DONE')
