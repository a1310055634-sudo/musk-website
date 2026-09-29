# -*- coding: utf-8 -*-
"""R05 集成：primary.html +10 条财报电话会 II（2019–2026）条目（93→103）
+ quotes.html +10 卡（80→90）+ index.html 计数文案 93→103
+ build-search-index.py 断言 93→103 + EXPANSION.md 补 R05 入包块。
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
    return head + body + '        </li>'

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
assert s.count('ps-row ps-deep') == 93, s.count('ps-row ps-deep')

# —— e2019-04-24（Q1 2019 call）→ 插在 id="e2019-04-30" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2019-04-30">', entry(
    'e2019-04-24', '2019.04.24', 'Tesla Q1 2019 财报电话会 · stockanalysis.com 逐字稿 · Reuters',
    [('Background', '背景', sec_p(
        'Tesla came into the call amid its darkest stretch yet — Q1 deliveries down 31% from the previous quarter, a fresh round of store closures, and Wall Street openly asking whether the company could reach profitability without new money. Asked by Bernstein’s Toni Sacconaghi about a capital raise, Musk chose to lecture on finance itself.',
        'Tesla 带着最黑暗的一段走进这场电话会——Q1 交付环比下滑 31%、新一轮门店关停，华尔街公开讨论这家公司能否不靠新钱活到盈利。被伯恩斯坦的 Toni Sacconaghi 问到融资时，马斯克选择先上一堂金融课。')),
     ('The words', '原话', sec_q(
        '“I don’t think raising capital should be a substitute for making the company operate more effectively. … I think it is healthy to be on a Spartan diet for a while.”',
        '我不认为融资应当成为「让公司运转得更有效」的替代品。……我认为，斯巴达式的紧衣缩食对一段时间来说倒是健康的。')),
     ('On the ground', '现场', sec_p(
        'Easy money, he argued, destroys discipline: “If we just keep raising capital every time, then we don’t have the forcing function for improving the fundamental operation of the business.” Yet by the end of the same answer he had softened — the transcript records him saying that at this point there was some merit to raising capital, and that this was probably about the right timing (the exact wording differs between transcription services).',
        '他主张，轻而易举的钱会毁掉纪律：「如果我们每次都继续融资，那我们就失去了改善业务根本运营的强制函数。」但同一段回答的结尾他已经松口——按转写记录，他说此时融资确有一些好处、时机大概正合适（此句两家转写措辞略有出入）。')),
     ('Aftermath', '后续', sec_p(
        'The Spartan diet lasted eight days: on 05.02 Tesla announced a stock-and-convertible offering of up to $2.3 billion — Reuters’ headline read “Tesla ends ‘Spartan diet’” — and with options exercised the total reached $2.7 billion, with Musk personally buying in, about $25 million of stock and notes (Reuters, 05.03). What he says about capital on a call is a starting bid, not a pledge. (Last sentence is editorial analysis, not his words.)',
        '斯巴达饮食持续了八天：05.02，Tesla 宣布至多 23 亿美元的股票+可转债增发——路透的标题就叫「特斯拉结束斯巴达饮食」；含超额配售，总额达到 27 亿美元，马斯克本人认购约 2,500 万美元的股票与可转债（路透，05.03）。他在电话会上关于资本的表态是开价，不是承诺。（末句为编者分析，非其原话。）'))]
) + '<li class="ps-row ps-deep reveal" id="e2019-04-30">', 'ins-e2019-04-24')

# —— e2020-01-29（Q4 2019 call）→ 插在 id="e2020-05-11" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2020-05-11">', entry(
    'e2020-01-29', '2020.01.29', 'Tesla Q4 2019 财报电话会 · stockanalysis.com 逐字稿 · Fortune',
    [('Background', '背景', sec_p(
        'Six weeks after the Cybertruck unveiling — and the broken-window memes (see 2019.11.21) — Tesla’s shares had quietly gone vertical. On the Q4 2019 call Musk had two data points to report: one about the truck everyone was still laughing at, one about self-driving.',
        'Cybertruck 发布六周后（碎窗梗还在流传，见 2019.11.21 条目），Tesla 的股价悄然起飞。在 Q4 2019 财报电话会上，马斯克交出两个数据点：一个关于那辆仍被群嘲的皮卡，一个关于自动驾驶。')),
     ('The words', '原话', sec_q(
        '“The demand has been incredible. We’ve never seen actually such a level of demand. … We will sell as many as we can make. It’s going to be pretty nuts.”',
        '需求一直难以置信地强。我们其实从未见过这种 level 的需求。……我们能造多少就卖多少。场面会相当疯狂。')),
     ('On the ground', '现场', sec_p(
        'On autonomy he owned a missed deadline and issued a new one: “We’re aiming to be feature complete with both FSD by the end of last year. We got pretty close, it’s looking like we might be feature complete in a few months.” (Fortune, same day.) Feature-complete, he qualified, only meant “some chance of going from your home to work, let’s say, with no interventions.”',
        '在自动驾驶上，他承认错过了自己 2019 年底的期限并重立新约：「我们的目标是 FSD 在去年底 feature complete。我们很接近了——看起来几个月内可能就能 feature complete。」（Fortune 当日报道。）他补充限定：feature complete 只意味着「比如说，有一定的概率能从家开到公司、零接管」。')),
     ('Aftermath', '后续', sec_p(
        'The truck’s order book kept compounding — reservations passed 250,000 within five days of the reveal (Musk on X; CNBC, 2019.11). Feature-complete FSD did not arrive in a few months: FSD Beta began reaching customers in 2020.10, and the deadline has moved every year since (see 2016.08.03, 2020.07.22).',
        '皮卡的订单簿持续滚动——发布后五天内预订数突破 25 万（马斯克 X 帖口径；CNBC 2019.11 报道）。feature complete 并没有在几个月内到来：FSD Beta 于 2020.10 才开始小范围推送给客户，而这条期限此后每年都在移动（见 2016.08.03、2020.07.22 条目）。'))]
) + '<li class="ps-row ps-deep reveal" id="e2020-05-11">', 'ins-e2020-01-29')

# —— e2020-07-22（Q2 2020 call）→ 插在 id="e2020-09-22" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2020-09-22">', entry(
    'e2020-07-22', '2020.07.22', 'Tesla Q2 2020 财报电话会 · stockanalysis.com 逐字稿 · CNBC TV18',
    [('Background', '背景', sec_p(
        'Tesla had just become the world’s most valuable carmaker (2020.07, market cap passing Toyota), and two weeks earlier at a Shanghai AI conference Musk had said the company was “very close” to Level 5 autonomy. Profitability was the story of the day; autonomy was the story he wanted to tell.',
        'Tesla 刚刚成为全球市值最高的车企（2020.07 市值超越丰田）；两周前在上海的世界人工智能大会上，马斯克已放话 Tesla「非常接近」L5 自主驾驶。当天报纸上的故事是盈利，他想讲的故事是自动驾驶。')),
     ('The words', '原话', sec_q(
        '“This is why I’m very confident about Full Self-Driving functionality being complete by the end of this year.”',
        '这就是为什么我非常有信心：完全自动驾驶（Full Self-Driving）功能将在今年年底前完成。')),
     ('On the ground', '现场', sec_p(
        'He framed what remained as arithmetic, not research: “It’ll be a long march of nines, essentially.” — the rest was just adding nines of reliability. Two weeks earlier, at the World AI Conference in Shanghai, he had already said Tesla was “very close” to achieving Level 5 (CNBC TV18, 07.09).',
        '他把剩下的工作框定成算术题而非科研题：「本质上，这将是一场『九』的长征。」——剩下的只是不断添加可靠性的几个 9。两周前在上海世界人工智能大会上，他就已说过 Tesla「非常接近」实现 L5（CNBC TV18 报道，07.09）。')),
     ('Aftermath', '后续', sec_p(
        '2020 ended without complete FSD functionality. FSD Beta reached customers in 2020.10; “complete” kept sliding — through the vision-only rewrite, year after year. As of this ledger’s revision date, six years on, the product is sold as “Full Self-Driving (Supervised)” — the word “Supervised” doing the work the deadline didn’t. (Last sentence is editorial analysis, not his words.)',
        '2020 年结束，完全自动驾驶功能没有完成。FSD Beta 于 2020.10 到达客户手上；「完成」继续顺延——穿过纯视觉方案重写，一年又一年。截至本志修订日，六年过去，这个产品以「Full Self-Driving (Supervised)」之名销售——「Supervised」这个词，替那条期限干完了它没干的活。（末句为编者分析，非其原话。）'))]
) + '<li class="ps-row ps-deep reveal" id="e2020-09-22">', 'ins-e2020-07-22')

# —— e2022-01-26（Q4 2021 call）→ 插在 id="e2022-03-08" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2022-03-08">', entry(
    'e2022-01-26', '2022.01.26', 'Tesla Q4 2021 财报电话会 · stockanalysis.com 逐字稿 · CNN Business',
    [('Background', '背景', sec_p(
        'Optimus had been a one-slide surprise at AI Day in 2021.08 (see 2021.08). Five months later, on the Q4 2021 call, the humanoid robot got its first earnings-call billing — ranked above every car Tesla made.',
        'Optimus 在 2021.08 的 AI Day 上还只是一页幻灯片式的惊吓（见 2021.08 条目）。五个月后，在 Q4 2021 财报电话会上，这个人形机器人第一次拿到了财报电话会的排面——排位在 Tesla 所有车之上。')),
     ('The words', '原话', sec_q(
        '“In terms of priority of products, I think the most important product development we’re doing this year is actually the Optimus humanoid robot. … This I think has the potential to be more significant than the vehicle business over time.”',
        '论产品优先级，我认为我们今年最重要的产品开发，其实是 Optimus 人形机器人。……我认为它有潜力随时间变得比汽车业务更重要。')),
     ('On the ground', '现场', sec_p(
        'He grounded the ranking in an economics argument — “The economy, it is the foundation of the economy is labor. Capital equipment is distilled labor” — then posed the consequence as a riddle: “What happens if you don’t actually have a labor shortage? I’m not sure what an economy even means at that point.”',
        '他为这个排位给出了一套经济学论证——「经济，它的根基是劳动。资本设备是蒸馏过的劳动」——然后把后果抛成一个谜语：「如果你其实并没有劳动力短缺，那会发生什么？到那时我都不确定『经济』这个词还意味着什么。」')),
     ('Aftermath', '后续', sec_p(
        'The robot itself kept slipping: AI Day II (2022.09) showed a prototype that walked; factory-task pledges followed (see 2024.04.23); by 2025 Optimus was the centerpiece of a trillion-dollar pay package (see 2025.11.06). The “more significant than the vehicle business” thesis, though, never changed — only the dates did. (Last sentence is editorial analysis, not his words.)',
        '机器人本体不断顺延：AI Day II（2022.09）展示了会走路的原型；工厂作业承诺接踵而至（见 2024.04.23 条目）；到 2025 年，Optimus 成了万亿美元薪酬方案的主角（见 2025.11.06 条目）。「比汽车业务更重要」的论点从未变过——变的只是日期。（末句为编者分析，非其原话。）'))]
) + '<li class="ps-row ps-deep reveal" id="e2022-03-08">', 'ins-e2022-01-26')

# —— e2022-10-19（Q3 2022 call）→ 插在 id="e2022-10-26" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2022-10-26">', entry(
    'e2022-10-19', '2022.10.19', 'Tesla Q3 2022 财报电话会 · stockanalysis.com 逐字稿 · Business Insider',
    [('Background', '背景', sec_p(
        'Tesla had just missed its quarterly delivery estimates, and the market wanted to talk about a buyback. Musk was willing to discuss both — but first he escalated a claim he had been building for years: several years earlier he had said it was possible for Tesla to be worth more than Apple. Now, he said, the number had a bigger ceiling.',
        'Tesla 刚刚错过季度交付预期，市场想聊回购。马斯克两个都愿意聊——但他先升级了那个铺垫多年的论断：几年前他曾说 Tesla 有可能比 Apple 更值钱。现在他说，这个数字的天花板更高了。')),
     ('The words', '原话', sec_q(
        '“Now I’m of the opinion that we can far exceed Apple’s current market cap. … In fact, I see a potential path for Tesla to be worth more than Apple and Saudi Aramco combined.”',
        '现在我的看法是，我们可以远超 Apple 当前的市值。……事实上，我看到了一条路，能让 Tesla 比 Apple 与沙特阿美加起来还值钱。')),
     ('On the ground', '现场', sec_p(
        'He attached hedges his valuation talk rarely carried: “Now that doesn’t mean it will happen or that it will be easy” — it would require “a lot of work, some very creative new products, tremendous expansion, and always some luck.” At that moment Apple and Saudi Aramco were the world’s two most valuable companies, worth roughly $4.4 trillion combined; Tesla’s market cap was around $700 billion (Business Insider).',
        '他为这次估值表态配上了罕见的对冲：「这不意味着它会发生，也不意味着它会容易」——那需要「大量工作、一些极具创造性的新产品、巨大的扩张，还有永远的运气」。彼时 Apple 与沙特阿美是全球市值最高的两家公司，合计约 4.4 万亿美元；Tesla 市值约 7,000 亿美元（Business Insider）。')),
     ('Aftermath', '后续', sec_p(
        'Two years later, almost to the day, he raised the bar again on the next Q3 call (see 2024.10.23). In between: Tesla’s stock lost roughly 65% over 2022, and the Twitter acquisition closed on 10.27 (see d2022-10-27).',
        '两年之后，几乎到日，他在下一个 Q3 电话会上再度加码（见 2024.10.23 条目）。中间隔着的是：Tesla 股价 2022 全年跌去约 65%，以及 10.27 收官的 Twitter 收购（见 d2022-10-27 文档）。'))]
) + '<li class="ps-row ps-deep reveal" id="e2022-10-26">', 'ins-e2022-10-19')

# —— e2023-10-18（Q3 2023 call）→ 插在 id="e2023-11-29" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2023-11-29">', entry(
    'e2023-10-18', '2023.10.18', 'Tesla Q3 2023 财报电话会 · stockanalysis.com 逐字稿 · TechRadar',
    [('Background', '背景', sec_p(
        'Margins were compressed by the year’s aggressive price cuts, and the Cybertruck delivery event was 43 days out (see 2023.11.30). On this call, Musk’s task was to temper expectations — starting with the product he had promised would change everything.',
        '利润率被这一年的激进降价压薄，Cybertruck 交付活动只剩 43 天（见 2023.11.30 条目）。这场电话会上马斯克的任务是给预期降温——从他许诺将改变一切的那辆车开始。')),
     ('The words', '原话', sec_q(
        '“I do want to emphasize that there will be enormous challenges in reaching volume production with the Cybertruck. … I mean, we dug our own grave with Cybertruck, you know?”',
        '我确实想强调：Cybertruck 在达到量产这件事上会有巨大的挑战。……我是说，我们给自己挖了坟——就是 Cybertruck，你们知道吗？')),
     ('On the ground', '现场', sec_p(
        'He quantified the gap between demo and factory: “the difficulty of going from a prototype to volume production is like 10,000% harder” — and warned the truck would need “a year to 18 months before it is a significant positive cash flow contributor.” The rest of the call was macro: “If interest rates remain high or if they go even higher, it’s that much harder for people to buy the car.”',
        '他量化了从原型到工厂之间的落差：「从原型到量产的难度要难上 10,000%」——并警告这辆车需要「一年到十八个月，才能成为显著的 positive cash flow 贡献者」。电话会的其余部分是宏观：「如果利率维持高位或者更高，人们买车就要难得多。」')),
     ('Aftermath', '后续', sec_p(
        'Deliveries began on schedule on 2023.11.30 (see 2023.11.30); the ramp then matched his warning — third-party estimates put 2024 Cybertruck deliveries around 39,000 (Cox Automotive), a fraction of the 250,000-a-year ambition the truck launched with. The grave, as he described it, took years to climb out of. (Last sentence is editorial analysis, not his words.)',
        '交付如期于 2023.11.30 开始（见 2023.11.30 条目）；随后的爬坡印证了他的警告——第三方估算 2024 年 Cybertruck 交付约 3.9 万辆（Cox Automotive 口径），只是这辆车发布时年 25 万产量愿景的零头。按他的说法挖下的那座坟，爬出来花了好几年。（末句为编者分析，非其原话。）'))]
) + '<li class="ps-row ps-deep reveal" id="e2023-11-29">', 'ins-e2023-10-18')

# —— e2024-04-23（Q1 2024 call）→ 插在 id="e2024-06-13" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2024-06-13">', entry(
    'e2024-04-23', '2024.04.23', 'Tesla Q1 2024 财报电话会 · stockanalysis.com 逐字稿 · Seeking Alpha',
    [('Background', '背景', sec_p(
        'Tesla had just posted its worst quarter in years — revenue down year-on-year, a double-digit workforce cut announced a week earlier (2024.04.15), and Reuters reporting the $25,000 car shelved. The pivot Musk announced instead had two names: robotaxi, and Optimus.',
        'Tesla 刚交出多年来最差的一个季度——营收同比下滑、一周前（2024.04.15）宣布裁员超一成、路透报道 2.5 万美元车型被搁置。马斯克宣布的转向有两个名字：robotaxi，与 Optimus。')),
     ('The words', '原话', sec_q(
        '“As we’ve announced, we will be showcasing our purpose-built Robotaxi or Cybercab in August.”',
        '如我们所宣布的，我们将在八月展示我们专为 Robotaxi 打造的 Cybercab。')),
     ('On the ground', '现场', sec_p(
        'He had first thrown out the date himself, on X, three weeks earlier (“Tesla Robotaxi unveil on 8/8”, 2024.04.05 — Reuters, among others); on the call he confirmed it: “We’ll talk about this more on August 8th.” And he attached Optimus to a deadline too: “we do think we will have Optimus in limited production in the factory, in the actual factory itself, doing useful tasks before the end of this year,” with external sales “by the end of next year.”',
        '日期最早是他自己三周前在 X 上抛出的（「Tesla Robotaxi unveil on 8/8」，2024.04.05；路透等报道）；电话会上他确认：「8 月 8 日我们会展开讲。」他还给 Optimus 挂上了期限：「我们确实认为，今年年底前，Optimus 会以有限规模在工厂里投产——就在真正的工厂里，做有用的任务」，对外销售则「在明年年底之前」。')),
     ('Aftermath', '后续', sec_p(
        'August 8 did not hold: the unveil slipped to 10.10 and became the “We, Robot” event (see 2024.10.10). The Optimus deadline passed as well — no factory robots doing useful tasks by year’s end — with volume-production talk shifting to 2025 and beyond (see 2025.11.06). By then, “this year” had its own track record on this ledger (see 2016.08.03, 2020.07.22).',
        '8 月 8 日没有守住：发布活动顺延到 10.10，变成了「We, Robot」发布会（见 2024.10.10 条目）。Optimus 的期限同样过期——到年底，工厂里并没有出现「做有用任务」的机器人；量产叙事移向 2025 年及以后（见 2025.11.06 条目）。到这时，「今年」在这本账上已经有了自己的履约记录（见 2016.08.03、2020.07.22 条目）。'))]
) + '<li class="ps-row ps-deep reveal" id="e2024-06-13">', 'ins-e2024-04-23')

# —— e2024-10-23（Q3 2024 call）→ 插在 id="e2025" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2025">', entry(
    'e2024-10-23', '2024.10.23', 'Tesla Q3 2024 财报电话会 · stockanalysis.com 逐字稿 · Investopedia · Fortune',
    [('Background', '背景', sec_p(
        'Thirteen days after “We, Robot” (see 2024.10.10), Tesla posted a quarter that beat on margins, and the stock jumped about 22% the next day — its best session in over a decade (Fortune). On the call, Musk packaged the results and the event into a single prediction.',
        '「We, Robot」十三天后（见 2024.10.10 条目），Tesla 交出一份利润率超预期的季报，次日股价跳涨约 22%——十多年来最好的单日表现（Fortune）。电话会上，马斯克把财报和发布会打包成了一句预测。')),
     ('The words', '原话', sec_q(
        '“My prediction is Tesla will become the most valuable company in the world, and probably by a long shot.”',
        '我的预测是，Tesla 将成为世界上最有价值的公司——而且很可能遥遥领先。')),
     ('On the ground', '现场', sec_p(
        'The prediction leaned on two products. On the robotaxi: “I do feel confident of Cybercab reaching volume production in 2026,” at a scale of “at least 2 million units a year” — “maybe 4 million, ultimately.” On the humanoid: Optimus “has a good chance of being the most valuable product ever made.”',
        '这句预测压在两件产品上。关于 robotaxi：「我确实有信心 Cybercab 在 2026 年达到量产」，规模「至少每年 200 万台」——「最终可能 400 万」。关于人形机器人：Optimus「有很好的机会成为有史以来最有价值的产品」。')),
     ('Aftermath', '后续', sec_p(
        'The stock’s verdict was immediate — +22% the next day (Fortune, 10.24). The 2026 Cybercab pledge now has a countdown on this ledger: see 2026.07.22 for the next status report. Optimus production began in limited numbers in 2025 (see 2025.11.06).',
        '市场的裁决立即到来——次日 +22%（Fortune，10.24）。Cybercab 的 2026 之约从此在这本账上进入倒计时：下一次状态更新见 2026.07.22 条目。Optimus 于 2025 年开始小规模生产（见 2025.11.06 条目）。'))]
) + '<li class="ps-row ps-deep reveal" id="e2025">', 'ins-e2024-10-23')

# —— e2025-04-22（Q1 2025 call）→ 插在 id="e2025-05-03" 前
s = sub1(s, '<li class="ps-row ps-deep reveal" id="e2025-05-03">', entry(
    'e2025-04-22', '2025.04.22', 'Tesla Q1 2025 财报电话会 · stockanalysis.com 逐字稿 · The Hill',
    [('Background', '背景', sec_p(
        'Tesla’s Q1 net income had fallen 71% (USA Today), the brand was taking daily damage from his Washington role, and the question hanging over the call was simple: where is the CEO? His answer became the headline of the day.',
        'Tesla Q1 净利下滑 71%（USA Today 口径），品牌正因他在华盛顿的角色每天失血，悬在电话会上的问题很简单：CEO 到底在哪？他的回答成了当天的头条。')),
     ('The words', '原话', sec_q(
        '“I think starting probably next month, May, my time allocation to DOGE will drop significantly.”',
        '我想大概从下个月、五月开始，我分配给 DOGE 的时间将大幅减少。')),
     ('On the ground', '现场', sec_p(
        'He framed the government work as substantially done: “Starting next month, I’ll be allocating far more of my time to Tesla now that the major work of establishing the Department of Government Efficiency is done.” — while conceding involvement would continue “probably the remainder of the president’s term,” at “a day or two per week” (USA Today). Of the protests: “The protesters that you’ll see out there, they’re very organized. They’re paid for.”',
        '他把政府工作框定为基本完成：「从下个月开始，我会把远多于现在的时间分给 Tesla——政府效率部筹建的主要工作已经完成。」同时承认参与将延续「大概总统任期的剩余时间」，每周「一两天」（USA Today）。对于抗议者：「你们在外面看到的抗议者，组织度很高。他们是拿了钱的。」')),
     ('Aftermath', '后续', sec_p(
        'The market read it as a truce — the stock rose on the remark (Yahoo Finance). He did step back from DOGE at the end of 2025.05 (mainstream outlets, 05.28–29) — and within days was publicly feuding with the president he had helped fund, a fight that cut Tesla’s shares about 14% in a single day (2025.06.05, mainstream coverage).',
        '市场把这读作停战——表态一出股价上涨（Yahoo Finance）。他确实在 2025.05 底淡出 DOGE（主流媒体 05.28–29 报道）——而数日之内，他就与这位他出资扶持的总统公开决裂，那一架让 Tesla 股价单日再跌约 14%（2025.06.05，主流媒体）。'))]
) + '<li class="ps-row ps-deep reveal" id="e2025-05-03">', 'ins-e2025-04-22')

# —— e2026-07-22（Q2 2026 call）→ 追加为账本最后一条（e2025-11-06 条目收尾 </li> 之后）
last_entry = entry(
    'e2026-07-22', '2026.07.22', 'Tesla Q2 2026 财报电话会 · stockanalysis.com 逐字稿 · elonmuskarchive.org 转写存档',
    [('Background', '背景', sec_p(
        'The most recent call on this ledger. A year into paid robotaxi service in Austin (launched 2025.06), the questions had shifted from “whether” to “how fast” — and Optimus, the in-house AI chips and a new “Terafab” factory dominated the outlook.',
        '本账本上最新的一场电话会。奥斯汀的付费 robotaxi 服务已运营一年（2025.06 上线），问题已经从「能不能」变成「多快」——而 Optimus、自研 AI 芯片与新的「Terafab」工厂主导了整场展望。')),
     ('The words', '原话', sec_q(
        '“I think Optimus will be the biggest product ever.”',
        '我认为 Optimus 会是有史以来最大的产品。')),
     ('On the ground', '现场', sec_p(
        'On the fleet: “We’ll continue to scale, I think, very rapidly with more than 10% a week in terms of miles driven.” On capacity: “The Terafab, we expect to announce a location soon.” On the AI6 chip: “I think it’s going to be the best edge computing chip in the world.” And on the Semi: “We expect to get self-driving working on the Tesla Semi probably around the end of this year or early next year.” He kept his own caution about the robot ramp: “Optimus will follow the normal S-curve of a manufacturing ramp, but the initial portion of the S-curve will be quite flat and long.”',
        '关于车队：「我们会继续非常快速地扩张——以行驶里程计，每周超过 10%。」关于产能：「Terafab，我们预计很快会宣布选址。」关于 AI6 芯片：「我认为它会成为世界上最好的边缘计算芯片。」关于 Semi：「我们预计大概今年年底或明年初，让自动驾驶在 Tesla Semi 上跑起来。」他也保留了对爬坡的克制：「Optimus 会遵循正常的制造爬坡 S 曲线，但 S 曲线的初始段会相当平缓而漫长。」')),
     ('Aftermath', '后续', sec_p(
        'As of this ledger’s revision date (2026.09), this is the last word. The promises now on the clock: Cybercab volume production in 2026 (see 2024.10.23), a Terafab location, and “the biggest product ever.” Whether the “10,000% harder” lesson of 2023 (see 2023.10.18) applies to robots the way it did to trucks is the question this ledger leaves open. (Last sentence is editorial analysis, not his words.)',
        '截至本志修订日（2026.09），这是账上的最后一句话。正在计时的承诺：Cybercab 2026 年量产（见 2024.10.23 条目）、Terafab 选址官宣、以及「有史以来最大的产品」。2023 年那堂「难 10,000%」的挖坟课（见 2023.10.18 条目）用在机器人身上是否如同用在皮卡上——这是本账留下的问题。（末句为编者分析，非其原话。）'))]
)
lines = s.split('\n')
crlf = any(l.endswith('\r') for l in lines)
idx = next(i for i, l in enumerate(lines) if 'id="e2025-11-06"' in l)
j = idx
while lines[j].rstrip('\r') != '        </li>':
    j += 1
    assert j < idx + 40, 'e2025-11-06 条目收尾 </li> 未找到'
block = last_entry.split('\n')
if crlf:
    block = [b + '\r' for b in block]
lines[j + 1:j + 1] = block
s = '\n'.join(lines)

assert s.count('ps-row ps-deep') == 103, s.count('ps-row ps-deep')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK primary.html: 93 → 103 条')

# ============ quotes.html ============
p = 'quotes.html'
s = io.open(p, encoding='utf-8', newline='').read()
assert s.count('<a class="qs-card"') == 80, s.count('<a class="qs-card"')

s = sub1(s, '<a class="qs-card" href="primary.html#e2019-04-30">', card(
    'e2019-04-24', '2019.04.24',
    '“I don’t think raising capital should be a substitute for making the company operate more effectively.”',
    '我不认为融资应当成为「让公司运转得更有效」的替代品。',
    'Q1 2019 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2019-04-30">', 'q-e2019-04-24')

s = sub1(s, '<a class="qs-card" href="primary.html#e2020-05-30">', card(
    'e2020-01-29', '2020.01.29',
    '“The demand has been incredible. … We will sell as many as we can make. It’s going to be pretty nuts.”',
    '需求一直难以置信地强。……我们能造多少就卖多少。场面会相当疯狂。',
    'Q4 2019 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2020-05-30">', 'q-e2020-01-29')

s = sub1(s, '<a class="qs-card" href="primary.html#e2020-09-22">', card(
    'e2020-07-22', '2020.07.22',
    '“This is why I’m very confident about Full Self-Driving functionality being complete by the end of this year.”',
    '这就是为什么我非常有信心：完全自动驾驶功能将在今年年底前完成。',
    'Q2 2020 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2020-09-22">', 'q-e2020-07-22')

s = sub1(s, '<a class="qs-card" href="primary.html#e2022-04-14">', card(
    'e2022-01-26', '2022.01.26',
    '“In terms of priority of products, I think the most important product development we’re doing this year is actually the Optimus humanoid robot.”',
    '论产品优先级，我认为我们今年最重要的产品开发，其实是 Optimus 人形机器人。',
    'Q4 2021 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2022-04-14">', 'q-e2022-01-26')

s = sub1(s, '<a class="qs-card" href="primary.html#e2022-10-28">', card(
    'e2022-10-19', '2022.10.19',
    '“I see a potential path for Tesla to be worth more than Apple and Saudi Aramco combined.”',
    '我看到了一条路，能让 Tesla 比 Apple 与沙特阿美加起来还值钱。',
    'Q3 2022 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2022-10-28">', 'q-e2022-10-19')

s = sub1(s, '<a class="qs-card" href="primary.html#e2023-11-29">', card(
    'e2023-10-18', '2023.10.18',
    '“I mean, we dug our own grave with Cybertruck, you know?”',
    '我是说，我们给自己挖了坟——就是 Cybertruck，你们知道吗？',
    'Q3 2023 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2023-11-29">', 'q-e2023-10-18')

s = sub1(s, '<a class="qs-card" href="primary.html#e2024-06-13">', card(
    'e2024-04-23', '2024.04.23',
    '“As we’ve announced, we will be showcasing our purpose-built Robotaxi or Cybercab in August.”',
    '如我们所宣布的，我们将在八月展示我们专为 Robotaxi 打造的 Cybercab。',
    'Q1 2024 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2024-06-13">', 'q-e2024-04-23')

s = sub1(s, '<a class="qs-card" href="primary.html#e2025-03-28">', card(
    'e2024-10-23', '2024.10.23',
    '“My prediction is Tesla will become the most valuable company in the world, and probably by a long shot.”',
    '我的预测是，Tesla 将成为世界上最有价值的公司——而且很可能遥遥领先。',
    'Q3 2024 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2025-03-28">', 'q-e2024-10-23')

s = sub1(s, '<a class="qs-card" href="primary.html#e2025-05-03">', card(
    'e2025-04-22', '2025.04.22',
    '“I think starting probably next month, May, my time allocation to DOGE will drop significantly.”',
    '我想大概从下个月、五月开始，我分配给 DOGE 的时间将大幅减少。',
    'Q1 2025 财报电话会 · stockanalysis.com 逐字稿') + '<a class="qs-card" href="primary.html#e2025-05-03">', 'q-e2025-04-22')

last_card = card(
    'e2026-07-22', '2026.07.22',
    '“I think Optimus will be the biggest product ever.”',
    '我认为 Optimus 会是有史以来最大的产品。',
    'Q2 2026 财报电话会 · stockanalysis.com 逐字稿')
lines = s.split('\n')
crlf = any(l.endswith('\r') for l in lines)
idx = next(i for i, l in enumerate(lines) if 'href="primary.html#e2025-11-06"' in l)
j = idx
while lines[j].rstrip('\r') != '        </a>':
    j += 1
    assert j < idx + 20, 'e2025-11-06 卡片收尾 </a> 未找到'
block = last_card.rstrip().split('\n')
if crlf:
    block = [b + '\r' for b in block]
lines[j + 1:j + 1] = block
s = '\n'.join(lines)

assert s.count('<a class="qs-card"') == 90, s.count('<a class="qs-card"')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK quotes.html: 80 → 90 卡')

# ============ index.html 计数 93→103 ============
p = 'index.html'
s = io.open(p, encoding='utf-8', newline='').read()
s = sub1(s, 'a 93-entry ledger, primary documents, interviews and posts', 'a 103-entry ledger, primary documents, interviews and posts', 'idx-en-186')
s = sub1(s, '93 条言行账本、一手文档、访谈与帖子', '103 条言行账本、一手文档、访谈与帖子', 'idx-zh-186')
s = sub1(s, 'Five entries picked from the 93-entry ledger', 'Five entries picked from the 103-entry ledger', 'idx-en-345')
s = sub1(s, '从 93 条言行账本里选出的五个节点', '从 103 条言行账本里选出的五个节点', 'idx-zh-345')
s = sub1(s, '<a href="primary.html" data-en="All 93 ledger entries →">账本全部 93 条 →</a>', '<a href="primary.html" data-en="All 103 ledger entries →">账本全部 103 条 →</a>', 'idx-395')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK index.html 计数 93→103 ×5')

# ============ build-search-index.py 断言 93→103 ============
p = 'tools/build-search-index.py'
s = io.open(p, encoding='utf-8', newline='').read()
s = sub1(s, "assert counts == {'言行实录': 93,", "assert counts == {'言行实录': 103,", 'si-assert')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK build-search-index.py 断言 93→103')

# ============ EXPANSION.md 补 R05 入包块（最新在前） ============
p = 'EXPANSION.md'
s = io.open(p, encoding='utf-8', newline='').read()
R05_BLOCK = '''> **新事实入包（V8 R05 轮 / 2026-09-30 电话会逐字稿核实）**：账本 +10 条（93→103）——Tesla 财报电话会 II（2019–2026）。十条锚点：e2019-04-24（Q1 2019「斯巴达饮食」，八天后 23→27 亿美元增发）/ e2020-01-29（Q4 2019 Cybertruck 需求「难以置信」+ FSD「几个月 feature complete」）/ e2020-07-22（Q2 2020 FSD「年底完成」+「九的长征」）/ e2022-01-26（Q4 2021 Optimus 排位高于汽车业务）/ e2022-10-19（Q3 2022「比 Apple 与沙特阿美合计更值钱」）/ e2023-10-18（Q3 2023「我们给自己挖了坟」+「难 10,000%」）/ e2024-04-23（Q1 2024 Robotaxi 8/8 之约 + Optimus「年内工厂做有用任务」）/ e2024-10-23（Q3 2024「全球最有价值公司」+ Cybercab 2026 量产）/ e2025-04-22（Q1 2025「DOGE 时间大幅减少」）/ e2026-07-22（Q2 2026「Optimus 会是有史以来最大的产品」——账本 2026 首条）。逐字稿源（stockanalysis.com/stocks/tsla/transcripts/ 全文直读，Quartr 转写）：[/23954-q1-2019/][/459-q4-2019/][/7605-q2-2020/][/12798-q4-2021/][/27338-q3-2022/][/83764-q3-2023/][/161624-q1-2024/][/215125-q3-2024/][/310668-q1-2025/][/653184-q2-2026/]。两源印证：Reuters（2019-05-02/03 Spartan diet 与增发）、Fortune（2020-01-29 FSD feature complete）、CNBC TV18（07.09 WAIC「非常接近 L5」）、CNN Business（Optimus 排位）、Business Insider（Apple+Aramco）、TechRadar（自掘坟墓）、Seeking Alpha/Shacknews（8/8）、Investopedia/Fortune（最有价值公司 +22%）、The Hill（DOGE 减时）、elonmuskarchive.org（Q2 2026 转写存档）。甄别注：①「Tesla 工厂是印钞机」传闻经 Q2 2022 逐字稿查证不存在（「license to print money」原话实指锂精炼业务），弃收；②Q1 2020「goddamn freedom」逐字确凿（逐字稿在档）但与在册 e2020-05-11 复工弧线重叠，本轮未单独立条；③Q1 2019「有理由融资」一句两家转写有出入，以转写一致的两句立条、此句转述并如实注明。

'''
anchor = '> **新事实入包（V8 R03'
n = s.count(anchor)
assert n == 1, n
s = s.replace(anchor, R05_BLOCK + anchor)
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('OK EXPANSION.md R05 入包块')
print('ALL INTEGRATION DONE')
