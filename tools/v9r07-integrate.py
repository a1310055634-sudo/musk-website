#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V9-20 R07: 官方演讲扩充 —— 六条账本条目 + 六张语录卡 + index 计数。

- primary.html：六个 ps-row 按时间序插入（锚=下一条开标签，new=新块+锚拼回）
- quotes.html：六张 qs-card 按日期序插入（锚=下一张卡开标签）
- index.html：109→115 计数 ×3（含 data-en）
全部断言通过才写盘；替换/插入计数打印。
"""
import io
import sys

P_PRIMARY = "primary.html"
P_QUOTES = "quotes.html"
P_INDEX = "index.html"


def read(p):
    return io.open(p, encoding="utf-8", newline="").read()


def write(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def ps_row(eid, date, src, bg_en, bg_zh, quote_en, quote_zh, ground_en, ground_zh,
           after_en, after_zh):
    return (
        f'<li class="ps-row ps-deep reveal" id="{eid}">\n'
        f'          <div class="ps-head"><span class="ps-date"><a class="ps-date" href="#{eid}" title="定位到本条 · Permalink">{date}</a></span><span class="ps-src">{src}</span></div>\n'
        f'          <div class="ps-sec"><h4 class="ps-label" data-en="Background">背景</h4>\n'
        f'            <p data-en="{bg_en}">{bg_zh}</p></div>\n'
        f'          <div class="ps-sec"><h4 class="ps-label" data-en="The words">原话</h4>\n'
        f'            <blockquote class="ps-quote">“{quote_en}”</blockquote>\n'
        f'            <p class="ps-zh">{quote_zh}</p></div>\n'
        f'          <div class="ps-sec"><h4 class="ps-label" data-en="On the ground">现场</h4>\n'
        f'            <p data-en="{ground_en}">{ground_zh}</p></div>\n'
        f'          <div class="ps-sec"><h4 class="ps-label" data-en="Aftermath">后续</h4>\n'
        f'            <p data-en="{after_en}">{after_zh}</p></div>\n'
        f'        </li>\n'
    )


def qs_card(eid, date, en, zh, src):
    return (
        f'        <a class="qs-card" href="primary.html#{eid}">\n'
        f'          <span class="qs-date">{date}</span>\n'
        f'          <p class="qs-en">“{en}”</p>\n'
        f'          <p class="qs-zh">{zh}</p>\n'
        f'          <span class="qs-src">{src}</span>\n'
        f'        </a>\n'
    )


# ---------------------------------------------------------------- ledger rows
ROWS = [
    # 1 ------------------------------------------------------------- COP21
    dict(
        eid="e2015-12-02", anchor="e2015-12-21",
        date="2015.12.02",
        src="COP21 气候大会索邦演讲 · YouTube 公开录像 · 镜像全档转写",
        bg_en="Seven months after launching Tesla Energy, Musk took the Sorbonne stage during the Paris climate summit and reframed the question: humanity exiting the fossil-fuel era was never an if, only a how fast.",
        bg_zh="Tesla Energy 发布七个月后（<a href=\"primary.html#e2015-04-30\">e2015-04-30</a>），马斯克登上巴黎气候大会期间的索邦讲台，把问题重新框了一遍：人类退出化石燃料时代从来不是「是否」，只是「多快」。",
        quote_en="This is why I call it the dumbest experiment in history ever. Why would you do this?",
        quote_zh="这就是我为什么称它为「史上最愚蠢的实验」。你为什么要做这件事？",
        ground_en="His arithmetic was brutal: carbon buried for hundreds of millions of years was being re-added to the cycle at 35 gigatons a year, with the IMF's $5.3 trillion hidden subsidy left unpriced. The fix — a revenue-neutral carbon tax phased in over five years — was pitched straight at the politicians in the room, and climate sensitivity got one line: \u201cNew York City under ice would be minus 5 degrees. New York City underwater would be plus 5 degrees.\u201d",
        ground_zh="他的算术很残酷：埋藏数亿年的碳正以每年 350 亿吨的规模被加回碳循环，而 IMF 测算的每年 5.3 万亿美元隐性补贴从未计入价格。他开出的药方——五年内分阶段落地的税收中性碳税——直接说给在场的政客听；讲气候敏感性只用了一句：「冰封之下的纽约是零下 5 度；淹没之下的纽约是零上 5 度。」",
        after_en="\u201cIt is inevitable that we will exit the fossil fuel era\u201d became his standing climate answer — speed is the only variable. The energy business kept compounding: SolarCity, the Gigafactories, and a battery empire now priced against oil majors.",
        after_zh="「退出化石燃料时代不可避免」成了他此后谈气候的标准答案——唯一的变量是速度。能源生意继续复利：SolarCity、超级工厂，以及一家如今按石油巨头口径定价的电池帝国。",
    ),
    # 2 ------------------------------------------------- BFR lunar passenger
    dict(
        eid="e2018-09-17", anchor="e2018-09-27",
        date="2018.09.17",
        src="SpaceX BFR 环月旅客发布会（Hawthorne）· 23ABC 直播录像 · 镜像全档转写",
        bg_en="One year after the BFR roadmap at IAC 2017, SpaceX announced its first private passenger: Japanese billionaire Yusaku Maezawa, booked for a circumlunar flight \u201cin 2023\u201d — the payload, six to eight artists.",
        bg_zh="IAC 2017 公布 BFR 路线图一年后（<a href=\"primary.html#e2017-09-29\">e2017-09-29</a>），SpaceX 宣布首位私人旅客：日本亿万富翁前田裕二，订下「2023 年」环月之旅——载荷不是货物，是六到八位艺术家。",
        quote_en="It's dangerous. To be clear, this is dangerous. This is no, you know, walk in the park here.",
        quote_zh="这很危险。说明白点：这就是危险的事，可不是什么公园散步。",
        ground_en="Maezawa had bought the whole rocket — \u201cwhy did I purchase the entire BFR?\u201d — and planned to invite artists to create work from the trip. Musk matched the romance with an engineering disclaimer: pushing the frontier \u201cis not a sure thing,\u201d the training is real, and the point of BFR was \u201cto make people excited about the future.\u201d",
        ground_zh="前田买下的是整枚火箭——「我为什么要买整枚 BFR？」——他还计划邀请艺术家们为此行创作作品。马斯克用工程师式的免责声明接住这份浪漫：开拓边疆「没有稳赚的事」，训练货真价实，而 BFR 的本意是「让人们对未来感到兴奋」。",
        after_en="The rocket was renamed Starship within a month; the passenger's dearMoon project was cancelled by Maezawa in mid-2024 after years of slips. The 2023 date joined the timeline museum — direction right, digits decorative.",
        after_zh="一个月内火箭改名 Starship（<a href=\"primary.html#e2019-09-28\">e2019-09-28</a>）；dearMoon 项目在多年跳票后由前田于 2024 年年中取消（媒体广泛报道）。「2023」就此进了时间表博物馆——方向正确，数字装饰。",
    ),
    # 3 ------------------------------------------------------- Autonomy Day
    dict(
        eid="e2019-04-22", anchor="e2019-04-24",
        date="2019.04.22",
        src="Tesla Autonomy Day 投资者日（Palo Alto）· Tesla 官方直播录像 · 镜像全档转写",
        bg_en="Tesla's first autonomy investor day unveiled the in-house FSD computer (HW3) and set the promise that would define the decade: feature-complete self-driving in 2020.",
        bg_zh="Tesla 首场自动驾驶投资者日发布了自研 FSD 芯片（HW3），并立下定义未来十年的承诺：2020 年做到「功能完整」的自动驾驶。",
        quote_en="LIDAR is a fool's errand and anyone relying on LIDAR is doomed. Doomed. Expensive, expensive sensors that are unnecessary.",
        quote_zh="激光雷达是徒劳之举，谁依赖它谁注定失败。注定。又贵又没必要的传感器。",
        ground_en="The engineering case was redundancy, not camera romance: \u201cany part of this could fail and the car will keep driving\u201d — the FSD computer itself less likely to fail than a driver losing consciousness. The 2020 deadline was delivered with total confidence; the walking-back would take years.",
        ground_zh="工程论证的支点是冗余而非相机情怀：「系统任何一部分都可能失效，车照样继续开」——FSD 芯片本身失效的概率比司机失去意识还低。2020 年这个期限以百分之百的自信说出；往回收则花了好几年。",
        after_en="Feature-complete slipped into a running joke (now on this site's promises file); the sensor bet hardened into camera-only Tesla Vision in 2021, and every rival robotaxi with a spinning lidar bucket became his standing Exhibit A.",
        after_zh="「功能完整」滑成了连续剧（如今挂在本站承诺对账档案 <a href=\"promises.html\">promises.html</a>）；传感器路线之争在 2021 年固化为纯视觉的 Tesla Vision，而每一家顶着旋转激光雷达桶的对手 Robotaxi，都成了他例证展览的头号展品。",
    ),
    # 4 --------------------------------------------------------- AI Day 2022
    dict(
        eid="e2022-09-30", anchor="e2022-10-19",
        date="2022.09.30",
        src="Tesla AI Day 2022（Palo Alto）· Tesla 官方直播录像 · 镜像全档转写",
        bg_en="A year after AI Day 2021 introduced the Tesla Bot with a dancer in a suit, Musk opened by confessing it — and then the real robot walked.",
        bg_zh="一年前的 AI Day（<a href=\"primary.html#e2021-08\">e2021-08</a>）用一位穿机器人服的舞者介绍了 Tesla Bot；这一次马斯克开场先自首——然后真机走了出来。",
        quote_en="As you know, last year it was just a person in a robot suit. But we've come a long way.",
        quote_zh="如你所知，去年那就是个穿机器人服装的人。但我们已经走了很远。",
        ground_en="Bumble C, the development robot with semi off-the-shelf actuators, walked on stage; the fully Tesla-designed Optimus wasn't ready to walk \u201cbut I think it will walk in a few weeks.\u201d The goal was stated like a shipping spec: \u201cOur goal is to make a useful humanoid robot as quickly as possible\u201d — designed for manufacturing, same discipline as the car.",
        ground_zh="采用半现货执行器的开发机 Bumble C 当场行走；全自研执行器的 Optimus 还没准备好走路，「但我想几周内它就会走了」。目标讲得像出货规格：「我们的目标是尽快造出有用的人形机器人」——沿用造车那套面向量产的设计纪律。",
        after_en="The closer went further than the robot: labor is the foundation of the economy, so the endgame is \u201ca future of abundance\u201d — \u201ca fundamental transformation of civilization as we know it.\u201d Optimus has since become Tesla's standing answer to what the company is actually worth.",
        after_zh="压轴比机器人走得更远：经济的地基是劳动，所以终局是「丰裕的未来」——「我们所知文明的一场根本变革」。此后 Optimus 成了 Tesla 回答「这家公司到底值多少钱」的标准答案。",
    ),
    # 5 --------------------------------------------- Neuralink Show & Tell
    dict(
        eid="e2022-11-30", anchor="e2023-03-01",
        date="2022.11.30",
        src="Neuralink Show and Tell 发布会 · Neuralink 官方直播录像 · 镜像全档转写",
        bg_en="Two years after the Three Little Pigs (e2020-08-28) and eighteen months after Pager's telepathic Pong (e2021-04-09), Neuralink's first full Show &amp; Tell put the whole stack on stage: the R1 surgical robot, brain-typing monkeys — and a date, of sorts, for human implantation.",
        bg_zh="三只小猪发布会（<a href=\"primary.html#e2020-08-28\">e2020-08-28</a>）两年后、Pager 意念打乒乓（<a href=\"primary.html#e2021-04-09\">e2021-04-09</a>）十八个月后，Neuralink 首场全面 Show and Tell 把整套系统摆上台：R1 手术机器人、意念打字的猴子——还有一个（某种意义上的）人体植入日期。",
        quote_en="We've submitted, I think, most of our paperwork to the FDA and we think probably in about six months we should be able to have a first Neuralink in a human.",
        quote_zh="我们大概已经向 FDA 交了大部分申报材料，估计再过六个月左右，我们应该能把第一颗 Neuralink 植入人体。（镜像转写将产品名听写拆为 \u201cneural link\u201d，引语按镜像口径收录。）",
        ground_en="Sake the monkey demoed \u201ctelepathic typing,\u201d moving the cursor to highlighted letters by mind alone — with Musk applying the caveat himself: \u201cI don't want to oversell this thing.\u201d The founding motive got its clearest statement: \u201cWhat do we do about AI?… At a species level, how do we mitigate that risk?\u201d",
        ground_zh="猴子 Sake 表演「意念打字」，纯凭意念把光标移到高亮字母——马斯克亲自给自家演示踩刹车：「我不想过度吹这东西」。创始动机也得到最清晰的一次表述：「面对 AI 我们怎么办？……在物种层面上，我们如何对冲那个风险？」",
        after_en="The six-month promise landed in about eight: Noland Arbaugh received the first implant in late January 2024, product name Telepathy (e2024-01-29). For once, a Musk deadline arrived within the same fiscal quarter of its promise.",
        after_zh="「六个月」的钟走了大约八个月：Noland Arbaugh 于 2024 年 1 月底接受首例植入，产品定名 Telepathy（<a href=\"primary.html#e2024-01-29\">e2024-01-29</a>）。这大概是马斯克的期限第一次落在承诺的同一个财季附近。",
    ),
    # 6 ------------------------------------------- Starship Update Starbase
    dict(
        eid="e2024-03-18", anchor="e2024-04-23",
        date="2024.03.18",
        src="SpaceX Starship Update at Starbase 员工演讲 · The Launch Pad 转播录像 · 镜像全档转写（日期为镜像归档锚）",
        bg_en="Addressing the Starbase workforce, Musk reviewed two flights of Starship data and set expectations for the third: \u201ca really good shot of reaching orbit with Flight 3\u201d — noting, ironically, that the last vehicle would likely have made orbit with a payload aboard. The archive date (2024-03-18) is the mirror's; the content points at the eve of Flight 3 (2024-03-14), and the date is recorded as archived.",
        bg_zh="面对 Starbase 全体员工，马斯克复盘了 Starship 前两次试飞的数据，并给第三次定下预期：「Flight 3 很有希望入轨」——还点出反讽之处：上一发若带着载荷（氧化剂余量不同），其实已能入轨。镜像归档日期为 2024-03-18，正文内容指向第三次试飞（2024-03-14）前夜的展望，日期口径以镜像归档为准照录。",
        quote_en="And one day we will indeed occupy Mars.",
        quote_zh="总有一天，我们会真正在火星上安家。",
        ground_en="The doctrine was recited like arithmetic: reusability, \u201cjust like we have reusability for cars, for airplanes, for bicycles, for horses.\u201d The receipts: 96 Falcon launches in a single year — half again the Soviet record — \u201call made it to orbit, all landed.\u201d Then another clock: people to the moon, and \u201cmaybe, if we get lucky… people to Mars within eight years.\u201d",
        ground_zh="教义像乘法表一样背出：复用，「就像汽车、飞机、自行车、马都有复用一样」。成绩单：猎鹰一年 96 发——比苏联纪录再多五成——「全部入轨，全部回收」。然后又上了一口钟：载人登月，「运气好的话……八年内载人上火星」。",
        after_en="Eight months later the launch tower caught a returning booster out of the sky — the moment this site's ledger marks as Starship's proof of concept. The eight-year Mars clock is, as ever, running.",
        after_zh="八个月后，发射塔从空中接住了返回的助推器——本站账本将其记为 Starship 概念验证的时刻（<a href=\"primary.html#e2024-10-13\">e2024-10-13</a>、<a href=\"x-posts.html#p2024-10-13\">p2024-10-13</a>）。至于八年的火星钟——一如既往，在走。",
    ),
]

# ---------------------------------------------------------------- quote cards
CARDS = [
    dict(eid="e2015-12-02", anchor="e2015-12-21",
         date="2015.12.02",
         en="This is why I call it the dumbest experiment in history ever. Why would you do this?",
         zh="这就是我为什么称它为「史上最愚蠢的实验」。你为什么要做这件事？",
         src="COP21 索邦演讲 · 2015.12.02"),
    dict(eid="e2018-09-17", anchor="e2018-09-27",
         date="2018.09.17",
         en="It's dangerous. To be clear, this is dangerous. This is no, you know, walk in the park here.",
         zh="这很危险。说明白点：这就是危险的事，可不是什么公园散步。",
         src="BFR 环月旅客发布会 · 2018.09.17"),
    dict(eid="e2019-04-22", anchor="e2019-04-24",
         date="2019.04.22",
         en="LIDAR is a fool's errand and anyone relying on LIDAR is doomed. Doomed. Expensive, expensive sensors that are unnecessary.",
         zh="激光雷达是徒劳之举，谁依赖它谁注定失败。注定。又贵又没必要的传感器。",
         src="Autonomy Day · 2019.04.22"),
    dict(eid="e2022-09-30", anchor="e2022-10-19",
         date="2022.09.30",
         en="As you know, last year it was just a person in a robot suit. But we've come a long way.",
         zh="如你所知，去年那就是个穿机器人服装的人。但我们已经走了很远。",
         src="AI Day 2022 · 2022.09.30"),
    dict(eid="e2022-11-30", anchor="e2023-03-01",
         date="2022.11.30",
         en="We've submitted, I think, most of our paperwork to the FDA and we think probably in about six months we should be able to have a first Neuralink in a human.",
         zh="我们大概已经向 FDA 交了大部分申报材料，估计再过六个月左右，我们应该能把第一颗 Neuralink 植入人体。",
         src="Neuralink Show and Tell · 2022.11.30"),
    dict(eid="e2024-03-18", anchor="e2024-04-23",
         date="2024.03.18",
         en="And one day we will indeed occupy Mars.",
         zh="总有一天，我们会真正在火星上安家。",
         src="Starship 更新会（Starbase）· 2024.03.18"),
]


def insert_before(text, marker, block, where):
    n = text.count(marker)
    assert n == 1, f"anchor not unique ({n}) for {where}: {marker[:60]}"
    return text.replace(marker, block + marker)


def main():
    # ---- primary.html
    pr = read(P_PRIMARY)
    n0 = pr.count('ps-row ps-deep')
    for r in ROWS:
        marker = f'<li class="ps-row ps-deep reveal" id="{r["anchor"]}">'
        block = ps_row(r["eid"], r["date"], r["src"], r["bg_en"], r["bg_zh"],
                       r["quote_en"], r["quote_zh"], r["ground_en"], r["ground_zh"],
                       r["after_en"], r["after_zh"])
        pr = insert_before(pr, marker, block, f"primary#{r['eid']}")
    n1 = pr.count('ps-row ps-deep')
    print(f"primary.html rows: {n0} -> {n1}")
    assert n1 == n0 + 6
    for r in ROWS:
        eid = r["eid"]
        assert pr.count(f'id="{eid}"') == 1, eid
        assert pr.count(f'<a class="ps-date" href="#{eid}"') == 1, eid
        assert pr.count(f'blockquote class="ps-quote"') >= 1
    # 每新条 4 段 ps-sec、1 quote、1 zh
    for r in ROWS:
        i = pr.find(f'id="{r["eid"]}"')
        j = pr.find("</li>", i)
        seg = pr[i:j]
        assert seg.count('ps-sec') == 4, r["eid"]
        assert seg.count('ps-quote') == 1, r["eid"]
        assert seg.count('ps-zh') == 1, r["eid"]
        assert seg.count('data-en=') == 7, r["eid"]  # 4×h4 标签 + 3×正文 p（ps-zh 段无）
    write(P_PRIMARY, pr)

    # ---- quotes.html
    q = read(P_QUOTES)
    c0 = q.count('<a class="qs-card"')
    for cd in CARDS:
        marker = f'<a class="qs-card" href="primary.html#{cd["anchor"]}">'
        block = qs_card(cd["eid"], cd["date"], cd["en"], cd["zh"], cd["src"])
        q = insert_before(q, marker, block, f"quotes#{cd['eid']}")
    c1 = q.count('<a class="qs-card"')
    print(f"quotes.html cards: {c0} -> {c1}")
    assert c1 == c0 + 6
    for cd in CARDS:
        assert q.count(f'href="primary.html#{cd["eid"]}"') == 1, cd["eid"]
    write(P_QUOTES, q)

    # ---- index.html 计数 109 -> 115
    ix = read(P_INDEX)
    n_before = ix.count("109")
    pairs = [
        ("a 109-entry ledger, primary documents", "a 115-entry ledger, primary documents"),
        ("每个结论都能回到出处：109 条言行账本", "每个结论都能回到出处：115 条言行账本"),
        ("Five entries picked from the 109-entry ledger", "Five entries picked from the 115-entry ledger"),
        ("从 109 条言行账本里选出的五个节点", "从 115 条言行账本里选出的五个节点"),
        ('All 109 ledger entries', 'All 115 ledger entries'),
        ("账本全部 109 条 →", "账本全部 115 条 →"),
    ]
    total = 0
    for old, new in pairs:
        n = ix.count(old)
        assert n == 1, f"index pattern count {n}: {old[:50]}"
        ix = ix.replace(old, new)
        total += n
    print(f"index.html 109->115 replacements: {total} (patterns {len(pairs)})")
    write(P_INDEX, ix)

    print("OK: R07 integrate done")


if __name__ == "__main__":
    main()
