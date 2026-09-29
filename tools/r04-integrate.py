# -*- coding: utf-8 -*-
"""R04 集成：primary.html +10 条财报电话会条目（83→93）+ quotes.html +10 卡（70→80）
+ index.html 计数文案 83→93 + build-search-index.py 断言 83→93。
原则：所有 replace 均带唯一性断言，防止静默失败假成功。条目结构严格克隆既有
<li class="ps-row ps-deep reveal" id="…"> 模板（背景/原话/现场/后续四段双语）。"""
import io, os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def sub1(s, old, new, tag):
    n = s.count(old)
    assert n == 1, f'[{tag}] 预期唯一匹配，实际 {n} 次'
    return s.replace(old, new)

def entry(eid, date, src, secs):
    head = f'<li class="ps-row ps-deep reveal" id="{eid}">\n'
    head += f'          <div class="ps-head"><span class="ps-date"><a class="ps-date" href="#{eid}" title="定位到本条 · Permalink">{date}</a></span><span class="ps-src">{src}</span></div>\n'
    body = ''
    for label_en, label_zh, inner in secs:
        body += f'          <div class="ps-sec"><h4 class="ps-label" data-en="{label_en}">{label_zh}</h4>\n'
        body += inner
        body += '</div>\n'
    return head + body + '        </li>        '

def sec_p(en, zh):
    return f'            <p data-en="{en}">{zh}</p>\n'

def sec_q(q, zh):
    return f'            <blockquote class="ps-quote">{q}</blockquote>\n            <p class="ps-zh">{zh}</p>\n'

def card(eid, date, en, zh, src):
    return (f'<a class="qs-card" href="primary.html#{eid}">\n'
            f'          <span class="qs-date">{date}</span>\n'
            f'          <p class="qs-en">{en}</p>\n'
            f'          <p class="qs-zh">{zh}</p>\n'
            f'          <span class="qs-src">{src} →</span>\n'
            f'        </a>\n\n        ')

# ============ primary.html ============
p = 'primary.html'
s = io.open(p, encoding='utf-8', newline='').read()
assert s.count('ps-row ps-deep') == 83, s.count('ps-row ps-deep')

# —— e2016-02-10（Q4 2015 call）→ 插在 id="e2016" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2016">', entry(
    'e2016-02-10', '2016.02.10', 'Tesla Q4 2015 财报电话会 · stockanalysis.com 逐字稿 · The Guardian',
    [('Background', '背景', sec_p(
        'Ten weeks before the Model 3 unveiling, Tesla was burning cash on the Model X ramp and 2015 had ended with a bigger loss. On the Q4 2015 call, Musk set the stage: the mass-market car was seven weeks from being shown.',
        'Model 3 发布会前十周，Tesla 正为 Model X 爬坡燃烧现金，2015 年以更大的亏损收官。在 Q4 2015 财报电话会上，马斯克铺垫了下一幕：大众市场汽车，七周后见。')),
     ('The words', '原话', sec_q(
        '“We’re really looking forward to the unveiling of the Model 3 at the end of next month. I think this is going to be really well-received, getting into production and delivery at the end of next year.”',
        '我们非常期待下个月底的 Model 3 发布。我认为它会大受欢迎，然后在明年底进入生产和交付。')),
     ('On the ground', '现场', sec_p(
        'He described a car designed around the factory instead of the other way round: “The 3 is really designed for ease of manufacturing” — about 20% lighter and, he said, considerably less complex to build than the Model S.',
        '他描述了一辆围绕工厂设计的汽车——而不是相反：「Model 3 真的是为易于制造而设计的」——比 Model S 轻约 20%，而且据他说，制造复杂度低得多。')),
     ('Aftermath', '后续', sec_p(
        'The unveiling seven weeks later produced the record-order night (see 2016.03.31); the “end of next year” production promise began a two-year slide of moving targets (see 2016.05.04 and 2017.07.28).',
        '七周后的发布会创下订单纪录之夜（见 2016.03.31 条目）；「明年底」的量产承诺，开始了为期两年的目标漂移（见 2016.05.04、2017.07.28 条目）。'))]
) + '<li class="ps-row ps-deep reveal" id="e2016">', 'ins-e2016-02-10')

# —— e2016-05-04（Q1 2016 call）→ 插在 id="e2016-07-20" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2016-07-20">', entry(
    'e2016-05-04', '2016.05.04', 'Tesla Q1 2016 财报电话会 · stockanalysis.com 逐字稿',
    [('Background', '背景', sec_p(
        'Five weeks after the record-order night, suppliers, analysts and short sellers were all asking the same question: could a company that had never built a car at volume actually do it? On the Q1 2016 call, Musk answered with a date.',
        '订单纪录之夜五周后，供应商、分析师与做空者都在问同一个问题：一家从未大规模造车的公司真的造得出来吗？在 Q1 2016 财报电话会上，马斯克用一个日期作答。')),
     ('The words', '原话', sec_q(
        '“The date we are setting with suppliers to get to a volume production capability with the Model 3 is July 1st next year. I would say we would aim to produce 100,000 to 200,000 Model 3s in the second half of next year.”',
        '我们与供应商约定的日期，是让 Model 3 在明年 7 月 1 日具备量产能力。我想我们的目标是明年下半年生产 10 万到 20 万辆 Model 3。')),
     ('On the ground', '现场', sec_p(
        'The commitment was framed as a supply-chain contract, not an aspiration — the number every supplier would program into its own production plans. He added that ordering early meant “a high probability you will actually receive your car in 2018.”',
        '这个承诺被框定为供应链契约而非愿景——是每家供应商会写进自己生产计划的数字。他还补充：现在下订的话，「有很高的概率你在 2018 年真能提到车」。')),
     ('Aftermath', '后续', sec_p(
        'The first Model 3 rolled off the line on 2017.07.09 — nine days past the supplier date. Tesla built 2,685 Model 3s in all of 2017; the 100,000–200,000 second-half target missed by a factor of roughly 50. The date was real; the ramp was not. (Counts: Tesla quarterly production reports.)',
        '首辆 Model 3 于 2017.07.09 下线——比供应商日期晚九天。Tesla 整个 2017 年只生产了 2,685 辆 Model 3，与下半年 10 万–20 万辆的目标落差约 50 倍。日期是真的，爬坡不是。（数量口径：Tesla 季度产量报告。）'))]
) + '<li class="ps-row ps-deep reveal" id="e2016-07-20">', 'ins-e2016-05-04')

# —— e2016-08-03（Q2 2016 call）→ 插在 id="e2016-09-01" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2016-09-01">', entry(
    'e2016-08-03', '2016.08.03', 'Tesla Q2 2016 财报电话会 · stockanalysis.com 逐字稿',
    [('Background', '背景', sec_p(
        'The world had just learned that a Tesla driver died in Florida with Autopilot engaged, and days earlier Mobileye said it would not renew the partnership. The question hanging over the Q2 2016 call was whether Autopilot would be pulled back. It was Musk’s first earnings call since the news broke.',
        '世界刚刚得知一位 Tesla 车主在佛罗里达州 Autopilot 状态下丧生，几天前 Mobileye 又宣布不再续约。悬在 Q2 2016 财报电话会上的问题是：Autopilot 会不会被收回。这是消息公开后马斯克的首次财报电话会。')),
     ('The words', '原话', sec_q(
        '“Full autonomy is gonna come a hell of a lot faster than anyone thinks it will. … It’s really a software limitation. The hardware is, I mean, the hardware exists to create full autonomy.”',
        '完全自动驾驶的到来会快得超出所有人的想象。……这其实只是软件的限制。硬件——我是说，实现完全自动驾驶的硬件已经存在。')),
     ('On the ground', '现场', sec_p(
        'Pressed on the fatality, he reframed the risk in aggregate: “Last year, there were 35,000 automotive deaths in the U.S. How many did you read about? … Tesla can’t sneeze without there being a national headline.” He named two priorities: “The focus really is on Model 3, followed by full autonomy.”',
        '被追问致死事故时，他把风险重新框定在总量层面：「去年美国有 35,000 人死于车祸，你读到过几条？……Tesla 打个喷嚏都能上全国头条。」他给出两个优先级：「重心真的是 Model 3，其次就是完全自动驾驶。」')),
     ('Aftermath', '后续', sec_p(
        'The “hardware already exists” line became the baseline of the self-driving promise: in 2019 Tesla reversed it, building the new FSD computer it said was required all along — and the full-autonomy timeline sketched here has been pushed back every year since. (Last sentence is editorial analysis, not his words.)',
        '「硬件已存在」成为自动驾驶承诺的基准口径：2019 年 Tesla 自己推翻了它，造了一块据称是一直必需的新型 FSD 计算机；而他在此勾勒的完全自动驾驶时间线，此后逐年顺延。（末句为编者分析，非其原话。）'))]
) + '<li class="ps-row ps-deep reveal" id="e2016-09-01">', 'ins-e2016-08-03')

# —— e2016-10-26（Q3 2016 call）→ 插在 id="e2016-11" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2016-11">', entry(
    'e2016-10-26', '2016.10.26', 'Tesla Q3 2016 财报电话会 · stockanalysis.com 逐字稿',
    [('Background', '背景', sec_p(
        'Two days before the solar-roof reveal, and three weeks before shareholders voted on the SolarCity merger he had championed against investor objections (see 2016.11), Musk used the Q3 2016 call to sell both at once.',
        '太阳能屋顶发布前两天、SolarCity 合并股东投票前三周（见 2016.11 条目）——马斯克在 Q3 2016 财报电话会上一口气为两件事站台。')),
     ('The words', '原话', sec_q(
        '“You’ll, I think you will be quite pleasantly surprised by what we debut on Friday. It’s exceeded my expectations. … I expect SolarCity to be approximately cash neutral, all things considered, next year.”',
        '我想，你会对我们周五发布的东西相当惊喜——它超出了我自己的预期。……我预计明年，SolarCity 大致能做到现金流打平。')),
     ('On the ground', '现场', sec_p(
        'He argued the deal was about product control, not rescue financing: “We do think it’s important to have tight control over the production of the solar panels in order to have a beautiful solar roof product.”',
        '他主张这笔合并关乎产品控制而非纾困输血：「我们确实认为，要做出漂亮的太阳能屋顶产品，就必须对太阳能板生产有紧密控制。」')),
     ('Aftermath', '后续', sec_p(
        'The Friday debut was the solar roof and Powerwall 2 event; shareholders approved the merger on 11.17 (see 2016.11). The cash-neutral call proved optimistic — the solar business kept consuming cash for years, though the roof product itself later reached volume production at the Buffalo factory.',
        '周五的发布就是太阳能屋顶 + Powerwall 2 发布会；股东于 11.17 批准合并（见 2016.11 条目）。「现金流打平」被证明过于乐观——太阳能业务此后多年仍在消耗现金，尽管屋顶产品本身后来在布法罗工厂进入了量产。'))]
) + '<li class="ps-row ps-deep reveal" id="e2016-11">', 'ins-e2016-10-26')

# —— e2017-02-22（Q4 2016 call）→ 插在 id="e2017-03-30" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2017-03-30">', entry(
    'e2017-02-22', '2017.02.22', 'Tesla Q4 2016 财报电话会 · stockanalysis.com 逐字稿',
    [('Background', '背景', sec_p(
        'Entering 2017, Tesla had never delivered more than 77,000 cars in a year. On the Q4 2016 call, Musk projected a 6.5x jump for 2018 — every unit of it hinging on a car that had not yet entered production.',
        '进入 2017 年时，Tesla 单年交付从未超过 7.7 万辆。在 Q4 2016 财报电话会上，马斯克预测 2018 年增长 6.5 倍——每一辆都押在一辆尚未投产的车上。')),
     ('The words', '原话', sec_q(
        '“I currently think that we should be able to do 500,000 vehicles next year and 1 million vehicles by 2020.”',
        '我目前认为，我们明年（2018）应该能做到 50 万辆，到 2020 年做到 100 万辆。')),
     ('On the ground', '现场', sec_p(
        'The demand side needed no help — which had become its own problem. Asked about the roughly 400,000-deep reservation queue, he quipped: “Yeah. We anti-sell the Model 3.”',
        '需求端从来不用操心——这本身成了新的问题。被问及近 40 万的预订队伍时，他打趣：「是啊。我们在反向销售 Model 3。」')),
     ('Aftermath', '后续', sec_p(
        '2018 ended at 245,240 deliveries — just under half the half-million. The half-million landed in 2020 (499,550), two years late, almost to the unit. The one-million year was 2022 (1,313,851). (Counts: Tesla annual delivery reports.)',
        '2018 年以 245,240 辆交付收官——不到 50 万的一半。50 万辆落在 2020 年（499,550），迟了两年，几乎精确到辆。百万辆之年是 2022（1,313,851）。（数量口径：Tesla 年度交付报告。）'))]
) + '<li class="ps-row ps-deep reveal" id="e2017-03-30">', 'ins-e2017-02-22')

# —— e2017-08-02 + e2017-11-01（合并一段）→ 插在 id="e2017-11-16" 前
two_2017 = entry(
    'e2017-08-02', '2017.08.02', 'Tesla Q2 2017 财报电话会 · stockanalysis.com 逐字稿',
    [('Background', '背景', sec_p(
        'Four days after telling the first 30 Model 3 owners “Welcome to production hell!” (see 2017.07.28), Musk faced analysts for the first time since. Q2 2017 had just set a record loss.',
        '对首批 30 位 Model 3 车主说完「欢迎来到生产地狱」四天后（见 2017.07.28 条目），马斯克首次面对分析师。Q2 2017 刚刚创下亏损纪录。')),
     ('The words', '原话', sec_q(
        '“Yeah, when I said manufacturing hell and supply chain hell on Friday, I meant it. … I’m very confident that we will be able to reach a production rate of 10,000 vehicles per week towards the end of next year.”',
        '是的，我周五说生产地狱、供应链地狱，是认真的。……我非常有信心，我们能在明年年底达到周产 10,000 辆。')),
     ('On the ground', '现场', sec_p(
        'He repeated the deadline ladder — 5,000 a week by December, now plus 10,000 a week by the end of 2018 — while conceding the thing ramp plans prefer to leave unsaid: “It’s just fundamentally impossible to predict the exponential part of the manufacturing S-curve.” (On stage he had said “production hell”; on the call he recast it as manufacturing and supply-chain hell.)',
        '他重申目标阶梯——12 月周产 5,000，再叠加 2018 年底周产 10,000——同时承认了爬坡计划不愿明说的事：「S 曲线的指数段，本质上是无法预测的。」（台上说的是「生产地狱」；电话会上他复述为「制造与供应链地狱」。）')),
     ('Aftermath', '后续', sec_p(
        'December came and went at a fraction of the promise: Tesla built 2,425 Model 3s in Q4 2017. The 10,000-a-week end-2018 target was never reached in Fremont. The S-curve, as he had warned, would not be predicted.',
        '12 月以承诺的零头收场：Tesla 2017 年 Q4 共生产 Model 3 2,425 辆。2018 年底周产 10,000 的目标在弗里蒙特从未达到。S 曲线，正如他警告过的，无法被预测。'))]
) + entry(
    'e2017-11-01', '2017.11.01', 'Tesla Q3 2017 财报电话会 · stockanalysis.com 逐字稿 · MediaPost',
    [('Background', '背景', sec_p(
        'Q3 2017 ended with 260 Model 3s built against a 1,500 target, a record $671 million loss, and a bottleneck nobody had named publicly. Morgan Stanley’s Adam Jonas opened his question like a weather report.',
        '2017 年 Q3 收官：Model 3 只造出 260 辆（目标 1,500），亏损创纪录的 6.71 亿美元，瓶颈却没人公开点破。摩根士丹利的 Adam Jonas 用天气预报的口吻开始提问。')),
     ('The words', '原话', sec_q(
        '“How hot is it in hell right now? Is it getting hotter or less hot?” — “We were in level 9. We’re now in level 8, and I think we’re close to exiting level 8.”',
        '「地狱现在有几热？是更热了还是没那么热了？」——「我们曾在第 9 层。现在在第 8 层，而且我想我们快走出第 8 层了。」')),
     ('On the ground', '现场', sec_p(
        'He named the constraint at last — battery module assembly at the Gigafactory: “The primary production constraint, really by far, is in battery module assembly.” The fix: “We had to rewrite all of the software from scratch and redo many of the mechanical and electrical elements.” New timeline: about 5,000 a week by late Q1 2018 — the third promised date in six months.',
        '他终于点破瓶颈——Gigafactory 的电池模组线：「目前最主要的产量约束，远远超过其他因素，就在电池模组组装。」修复方式：「我们不得不从零重写全部软件，并重做许多机械与电气部件。」新时间表：2018 年 Q1 末左右达到周产约 5,000——六个月里的第三个承诺日期。')),
     ('Aftermath', '后续', sec_p(
        'Level 8 lasted through the winter. By April 2018 Musk was tweeting that the automation itself had been the mistake (see 2018.04.13); the eventual fix included a tent (see the aftermath of 2017.07.28).',
        '第 8 层地狱过完了整个冬天。到 2018 年 4 月，马斯克发推承认自动化本身就是错误（见 2018.04.13 条目）；最终的修复方案里有一顶帐篷（见 2017.07.28 条目后续段）。'))]
)
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2017-11-16">', two_2017 + '<li class="ps-row ps-deep reveal" id="e2017-11-16">', 'ins-e2017-pair')

# —— e2018-04-13 + e2018-05-02（合并一段）→ 插在 id="e2018-05-20" 前
two_2018 = entry(
    'e2018-04-13', '2018.04.13', '本人推文 · Gadgets360/NDTV · The Guardian（2018 年表）',
    [('Background', '背景', sec_p(
        'Model 3 output had missed another weekly target, and Musk spent the evening on Twitter dissecting the automation doctrine his factory had been built on. The verdict came in three sentences.',
        'Model 3 产量又一次没过周目标，马斯克当晚在推特上逐条复盘他那座工厂赖以建立的自动化教条。结论只有三句。')),
     ('The words', '原话', sec_q(
        '“Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated.”',
        '是的，Tesla 的过度自动化是个错误。精确地说，是我的错误。人类被低估了。')),
     ('On the ground', '现场', sec_p(
        'It was a reversal delivered in his own voice: the company that had staked its ramp on robots conceded the machines were the bottleneck — and he owned it personally, in public, unprompted.',
        '这是一次用他本人声线完成的掉头：这家把爬坡押在机器人上的公司，承认机器才是瓶颈——而且由他本人在公开场合主动认领。')),
     ('Aftermath', '后续', sec_p(
        'Three weeks later he expanded the confession into the “flufferbot” story on the Q1 2018 call (see 2018.05.02); GA4, the tent line that finally hit 5,000 a week, was built around people, not robots.',
        '三周后，他在 Q1 2018 财报电话会上把这份认错展开成「flufferbot」的故事（见 2018.05.02 条目）；最终达到周产 5,000 的帐篷线 GA4，是围绕人、而不是机器人搭起来的。'))]
) + entry(
    'e2018-05-02', '2018.05.02', 'Tesla Q1 2018 财报电话会 · BBC · Slate · The Verge',
    [('Background', '背景', sec_p(
        'Tesla reported a record quarterly loss; Wall Street’s questions were about cash. Musk had other plans for the microphone.',
        'Tesla 交出创纪录的季度亏损；华尔街关心的是现金。马斯克对话筒另有安排。')),
     ('The words', '原话', sec_q(
        '“Excuse me. Next. Boring, bonehead questions are not cool. Next. … We’re going to go to YouTube. Sorry, these questions are so dry. They’re killing me.”',
        '抱歉，下一个。无聊的蠢问题不酷。下一个。……我们去 YouTube。抱歉，这些问题太干了，快把我无聊死了。')),
     ('On the ground', '现场', sec_p(
        'Bernstein’s Toni Sacconaghi had asked how Tesla would fund the ramp; RBC’s Joseph Spak got the “so dry” verdict. Musk took questions instead from Galileo Russell, a retail-side YouTuber — ten of them — while detailing the battery-line confession: “So we had this weird flufferbot. Which was really an incredibly difficult machine to make work. … Machines are not good at picking up pieces of fluff. Human hands are way better at doing that.” Shares fell more than 5% in late trading (BBC); Morgan Stanley’s Adam Jonas called it the most unusual call he had heard in 20 years (Business Insider).',
        '伯恩斯坦的 Toni Sacconaghi 问的是爬坡资金从哪来；RBC 的 Joseph Spak 得到「太干了」的评语。马斯克转而回答零售侧 YouTube 博主 Galileo Russell 的十个提问，边答边交代电池线的认错：「我们有台怪异的 flufferbot——一台极难伺候的机器。……机器不擅长捡绒毛，人手干这个好得多。」盘后股价跌逾 5%（BBC）；摩根士丹利的 Adam Jonas 说这是他 20 年来听过的最离奇的电话会（Business Insider）。')),
     ('Aftermath', '后续', sec_p(
        'Sacconaghi published a rebuttal noting the call “raises more ‘boring’ and ‘not cool’ questions than it answers.” Three months later, Musk opened the next call with an apology (see 2018.08.01).',
        'Sacconaghi 随后发文回敬：这场电话会「引出的『无聊』与『不酷』的问题，比它回答的还多」。三个月后，马斯克以下一次电话会的道歉开场（见 2018.08.01 条目）。'))]
)
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2018-05-20">', two_2018 + '<li class="ps-row ps-deep reveal" id="e2018-05-20">', 'ins-e2018-pair')

# —— e2018-08-01（Q2 2018 call）→ 插在 id="e2018-08-07" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2018-08-07">', entry(
    'e2018-08-01', '2018.08.01', 'Tesla Q2 2018 财报电话会 · Business Insider · Bloomberg',
    [('Background', '背景', sec_p(
        'Six days before the “funding secured” tweet (see 2018.08.07), Tesla’s Q2 report showed the cash burn slowing. Musk opened the call by returning to a wound of his own making.',
        '「funding secured」推文六天前（见 2018.08.07 条目），Tesla 的 Q2 财报显示现金燃烧放缓。马斯克以回望一道自己造成的伤口开场。')),
     ('The words', '原话', sec_q(
        '“I’d like to apologize for being impolite on the prior call. … There’s no excuse for bad manners.”',
        '我想为上次电话会上的失礼道歉。……没礼貌没有任何借口。')),
     ('On the ground', '现场', sec_p(
        'He cited 110–120-hour weeks and no days off as context, then dismissed his own excuse and let Sacconaghi — the “bonehead questions” analyst — ask first. Wall Street noticed: coverage framed it as Musk discovering “the power of a good apology” (Chief Executive), and the stock rallied in late trading (Bloomberg).',
        '他以每周 110–120 小时、无休作铺垫，随即亲自撇开这个借口，并让 Sacconaghi——那位问出「蠢问题」的分析师——先提问。华尔街注意到了：报道把它框成马斯克领会了「好好道歉的力量」（Chief Executive），盘后股价上涨（Bloomberg）。')),
     ('Aftermath', '后续', sec_p(
        'The humility lasted one week: on 08.07 came “funding secured” (see 2018.08.07), and the SEC complaint followed on 09.27. The apology and the tweet are the same month’s twin poles — editorial framing, not his words.',
        '谦卑持续了一周：08.07 而来的是「funding secured」（见 2018.08.07 条目），SEC 起诉则在 09.27 落地。道歉与推文是同一个月的两极——此句为编者框架，非其原话。'))]
) + '<li class="ps-row ps-deep reveal" id="e2018-08-07">', 'ins-e2018-08-01')

assert s.count('ps-row ps-deep') == 93, s.count('ps-row ps-deep')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK primary.html: 83 → 93 条')

# ============ quotes.html ============
p = 'quotes.html'
s = io.open(p, encoding='utf-8', newline='').read()
n0 = s.count('<a class="qs-card"')
assert n0 == 70, n0

s = sub1(s, '<a class="qs-card" href="primary.html#e2016">', card(
    'e2016-02-10', '2016.02.10',
    '“We’re really looking forward to the unveiling of the Model 3 at the end of next month. I think this is going to be really well-received.”',
    '我们非常期待下个月底的 Model 3 发布。我认为它会大受欢迎。',
    'Q4 2015 财报电话会 · stockanalysis.com 逐字稿'), 'q-e2016-02-10')

s = sub1(s, '<a class="qs-card" href="primary.html#e2016-07-20">', card(
    'e2016-05-04', '2016.05.04',
    '“The date we are setting with suppliers to get to a volume production capability with the Model 3 is July 1st next year.”',
    '我们与供应商约定的日期，是让 Model 3 在明年 7 月 1 日具备量产能力。',
    'Q1 2016 财报电话会 · stockanalysis.com 逐字稿'), 'q-e2016-05-04')

s = sub1(s, '<a class="qs-card" href="primary.html#e2016-09-01">', card(
    'e2016-08-03', '2016.08.03',
    '“Full autonomy is gonna come a hell of a lot faster than anyone thinks it will. … The hardware exists to create full autonomy.”',
    '完全自动驾驶的到来会快得超出所有人的想象。……实现完全自动驾驶的硬件已经存在。',
    'Q2 2016 财报电话会 · stockanalysis.com 逐字稿'), 'q-e2016-08-03')

s = sub1(s, '<a class="qs-card" href="primary.html#e2017-03-30">', card(
    'e2016-10-26', '2016.10.26',
    '“I expect SolarCity to be approximately cash neutral, all things considered, next year.”',
    '我预计明年，SolarCity 大致能做到现金流打平。',
    'Q3 2016 财报电话会 · stockanalysis.com 逐字稿') + card(
    'e2017-02-22', '2017.02.22',
    '“I currently think that we should be able to do 500,000 vehicles next year and 1 million vehicles by 2020.”',
    '我目前认为，明年（2018）应该能做到 50 万辆，到 2020 年做到 100 万辆。',
    'Q4 2016 财报电话会 · stockanalysis.com 逐字稿'), 'q-e2016-10-26+e2017-02-22')

s = sub1(s, '<a class="qs-card" href="primary.html#e2017-11-16">', card(
    'e2017-08-02', '2017.08.02',
    '“Yeah, when I said manufacturing hell and supply chain hell on Friday, I meant it.”',
    '是的，我周五说生产地狱、供应链地狱，是认真的。',
    'Q2 2017 财报电话会 · stockanalysis.com 逐字稿') + card(
    'e2017-11-01', '2017.11.01',
    '“We were in level 9. We’re now in level 8, and I think we’re close to exiting level 8.”',
    '我们曾在第 9 层。现在在第 8 层，而且我想我们快走出第 8 层了。',
    'Q3 2017 财报电话会 · stockanalysis.com 逐字稿'), 'q-e2017-pair')

s = sub1(s, '<a class="qs-card" href="primary.html#e2018-05-20">', card(
    'e2018-04-13', '2018.04.13',
    '“Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated.”',
    '是的，Tesla 的过度自动化是个错误。精确地说，是我的错误。人类被低估了。',
    '本人推文 · Gadgets360/NDTV · The Guardian') + card(
    'e2018-05-02', '2018.05.02',
    '“Boring, bonehead questions are not cool. Next. … We’re going to go to YouTube. … They’re killing me.”',
    '无聊的蠢问题不酷。下一个。……我们去 YouTube。……快把我无聊死了。',
    'Q1 2018 财报电话会 · BBC · Slate · The Verge'), 'q-e2018-pair')

s = sub1(s, '<a class="qs-card" href="primary.html#e2018-08-07">', card(
    'e2018-08-01', '2018.08.01',
    '“I’d like to apologize for being impolite on the prior call. … There’s no excuse for bad manners.”',
    '我想为上次电话会上的失礼道歉。……没礼貌没有任何借口。',
    'Q2 2018 财报电话会 · Business Insider · Bloomberg'), 'q-e2018-08-01')

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
print('ALL INTEGRATION DONE')
