# -*- coding: utf-8 -*-
"""V12 R04: 账本早期加密（2002–2010）五条集成（全无引语节，不触发语录卡）。
锚全部一手：Tesla 424B4（2010-06-29 IPO 定价书，EDGAR 直读）/ EDGAR Form D / NASA 公告转存两源。
"""
import io, re, sys

F = 'primary.html'
s = io.open(F, encoding='utf-8').read()

def row(eid, date_disp, src, secs):
    head = (f'<li class="ps-row ps-deep reveal" id="{eid}">\n'
            f'          <div class="ps-head"><span class="ps-date"><a class="ps-date" href="#{eid}" title="定位到本条 · Permalink">{date_disp}</a></span><span class="ps-src">{src}</span></div>\n')
    body = ''
    for label_en, label_zh, en, zh in secs:
        body += (f'          <div class="ps-sec"><h4 class="ps-label" data-en="{label_en}">{label_zh}</h4>\n'
                 f'            <p data-en="{en}">{zh}</p></div>\n')
    return head + body + '        </li>\n'

C1 = row('e2002-05', '2002.05', 'SpaceX 成立 · Musk 出任 CEO/CTO · Tesla 424B4（2010）官方陈述',
    [('Background', '背景',
      'Space Exploration Technologies Corp. was founded in 2002; Tesla&#8217;s own IPO prospectus (424B4, 2010-06) states Musk &#8220;has also served as Chief Executive Officer, Chief Technology Officer and Chairman of Space Exploration Technologies Corporation&#8230;since May 2002.&#8221; He put $100M of the PayPal proceeds into it five months later (see 2002.10.03).',
      'SpaceX（太空探索技术公司）2002 年成立；Tesla 自己的 IPO 定价书（424B4，2010-06）官方陈述「马斯克自 2002 年 5 月起担任 SpaceX 首席执行官、首席技术官兼董事长」。五个月后，他把 PayPal 套现的 1 亿美元投了进去（见本页 2002.10.03 条）。'),
     ('On the ground', '现场',
      'A two-line prospectus sentence is the driest possible record of the wildest bet: a paying-customer-less rocket company, founded before the money that funded it even arrived.',
      '招股书里干巴巴的一句履历，是史上最狂赌注最干燥的官方记录：一家还没有付费客户的火箭公司，在资助它的那笔钱到账之前就已成立。')])

C2 = row('e2004', '2004', 'Musk 出任 Tesla 董事长 · Tesla 424B4 官方陈述 · Series A 细节=公司披露与传记口径',
    [('Background', '背景',
      'Tesla&#8217;s Series A ($7.5M, April 2004) was led by Musk with about $6.5M of his own money; the 424B4 (2010-06) states he has been &#8220;Chairman of our board of directors since April 2004.&#8221; Founders Eberhard and Tarpenning stayed on.',
      'Tesla A 轮融资（750 万美元，2004 年 4 月）由马斯克领投约 650 万美元，并出任董事长——424B4（2010-06）官方陈述「自 2004 年 4 月起担任董事会主席」。创始人 Eberhard 与 Tarpenning 留任。'),
     ('Aftermath', '后续',
      'Four years later he took over as CEO (October 2008, per the same prospectus) — the same autumn Falcon 1 kept failing (see 2008.08.02). The founder-vs-investor fallout of 2007-2009 ended in litigation and a mutual peace.',
      '四年后他接任 CEO（同一份招股书：2008 年 10 月起）——与 Falcon 1 连续坠毁是同一个秋天（见本页 2008.08.02 条）。2007–2009 年创始人出局风波以诉讼与和解收场。')])

C3 = row('e2008-12-23', '2008.12.23', 'NASA CRS 合同公告 · Spaceflight Now/NASA Watch 转存核读 · NASA OIG 2013 审计在档',
    [('Background', '背景',
      'One day before the Christmas Eve financing that saved Tesla (see 2008.12.24), NASA announced the Commercial Resupply Services awards: up to 12 flights for SpaceX valued at about $1.6 billion — the contract that pulled SpaceX out of salary-scrapping survival within five years of three consecutive Falcon 1 failures.',
      '就在救活 Tesla 的圣诞夜融资前一天（见本页 2008.12.24 条），NASA 宣布商业再补给服务（CRS）合同：SpaceX 获最多 12 次飞行、约 16 亿美元——Falcon 1 三连败后五年内，这份合同把 SpaceX 从「工资都发不出」的生存线里拉了出来。'),
     ('On the ground', '现场',
      'Two near-dead companies, bailed out by two different customers in the same week: a financing round closed by investors, a service contract won against an incumbent. Neither knew it was saving the other&#8217;s sibling.',
      '两家濒死公司，同一周被两个不同客户救起：一边是投资人凑齐的融资轮，一边是击败在位承包商拿到的服务合同。谁都不知道，自己正在救另一家的兄弟公司。')])

C4 = row('e2009-05-19', '2009.05.19', 'Daimler 战略投资 · Tesla 官方公告口径 · EDGAR Form D（2009-05-20 归档）· 424B4 Blackstar 陈述',
    [('Background', '背景',
      'Daimler made a strategic investment in Tesla (media caliber: about $50M for roughly 10%). Tesla&#8217;s 424B4 (2010-06) states: &#8220;Blackstar Investco LLC, an affiliate of Daimler, holds more than 5% of our outstanding capital stock&#8221;; a Regulation D filing was lodged with the SEC on 2009-05-20.',
      'Daimler 战略投资 Tesla（媒体口径：约 5000 万美元、约 10% 股权）。Tesla 424B4（2010-06）官方陈述：「Daimler 关联实体 Blackstar Investco LLC 持有公司超过 5% 的流通股本」；EDGAR 于 2009-05-20 归档 Reg D 备案佐证。'),
     ('On the ground', '现场',
      'For a startup fresh off a Roadster recall, the century-old automaker&#8217;s cheque was worth more as a verdict than as cash: the technology was real. The first fruit was up to 1,000 battery packs for Daimler&#8217;s Smart ED (relationship since March 2008, per 424B4).',
      '对一家刚经历 Roadster 召回的初创，百年车企这张支票与其说是现金，不如说是判决书：技术是真的。第一颗果实是为 Daimler Smart ED 供应最多 1000 套电池包（424B4：合作关系自 2008 年 3 月起）。')])

C5 = row('e2010-05-20', '2010.05.20', 'Tesla/Toyota 合作与 Fremont 工厂公告 · Tesla 424B4 官方陈述',
    [('Background', '背景',
      'Per the 424B4 (2010-06): &#8220;In May 2010, Tesla and Toyota Motor Corporation&#8230;announced their intention to cooperate on the development of electric vehicles, and for Tesla to receive Toyota&#8217;s support with sourcing parts and production and engineering expertise for the Model S&#8221; — alongside the plan to build Model S at the former NUMMI plant in Fremont (media caliber: Toyota to invest $50M at IPO).',
      '据 424B4（2010-06）：「2010 年 5 月，Tesla 与丰田宣布电动车开发合作意向，Tesla 将获得丰田在零部件采购、生产与工程上对 Model S 的支持」——同期宣布在弗里蒙特原 NUMMI 工厂生产 Model S 的计划（媒体口径：丰田于 IPO 时投资 5000 万美元）。'),
     ('On the ground', '现场',
      'The plant GM and Toyota had shut down months earlier became Model S&#8217;s birthplace: within weeks of the IPO, a bankrupt-era factory was staffing back up.',
      '几个月前刚被通用和丰田关停的工厂，成了 Model S 的产房：IPO 前后数周内，这座大萧条时代的厂房重新开始招人。')])

A1 = '<li class="ps-row ps-deep reveal" id="e2002-10-03">'
A2 = '<li class="ps-row ps-deep reveal" id="e2006">'
A3 = '<li class="ps-row ps-deep reveal" id="e2008-12-24">'
A4 = '<li class="ps-row ps-deep reveal" id="e2010-06-29">'

for a in (A1, A2, A3, A4):
    if s.count(a) != 1:
        sys.exit(f'锚不唯一: {a} -> {s.count(a)}')

s = s.replace(A1, C1 + A1)
s = s.replace(A2, C2 + A2)
s = s.replace(A3, C3 + A3)
s = s.replace(A4, C4 + C5 + A4)

# ---- 断言 ----
n_rows = len(re.findall(r'<li class="ps-row', s))
n_quote = len(re.findall(r'class="ps-quote"', s))
for eid in ['e2002-05', 'e2004', 'e2008-12-23', 'e2009-05-19', 'e2010-05-20']:
    if s.count(f'id="{eid}"') != 1 or f'href="#{eid}"' not in s:
        sys.exit(f'条目 {eid} 异常')
assert n_rows == 124, n_rows
assert n_quote == 115, n_quote  # 新条无引语，计数不变

# 局部邻居检查（全页升序不成立：站内既有年精度条目 e2013/e2016 插在年份段中间）
ids = re.findall(r'<li class="ps-row[^"]*" id="(e[\d-]+)"', s)
NEIGHBORS = {
    'e2002-05': ('e2002-10-03',),
    'e2004': ('e2006',),
    'e2008-12-23': ('e2008-12-24',),
    'e2009-05-19': ('e2010-05-20',),
    'e2010-05-20': ('e2010-06-29',),
}
def key(i):
    p = i[1:].split('-')
    return tuple(map(int, p + [0] * (3 - len(p))))
for eid, nxts in NEIGHBORS.items():
    for nxt in nxts:
        assert key(eid) < key(nxt), (eid, nxt)
idx = {i: n for n, i in enumerate(ids)}
for eid, nxts in NEIGHBORS.items():
    for nxt in nxts:
        assert idx[eid] < idx[nxt], ('位置反了', eid, nxt)

io.open(F, 'w', encoding='utf-8', newline='').write(s)
print('五条集成 OK: rows=%d ps-quote=%d（不变）时序升序' % (n_rows, n_quote))
