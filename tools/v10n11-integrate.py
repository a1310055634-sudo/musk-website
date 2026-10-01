# -*- coding: utf-8 -*-
"""V10-15 N11：interviews.html 插入保留池 4 卡（时间序）+ 索引断言 43→47。"""
import io
import sys

p = 'interviews.html'
s = io.open(p, encoding='utf-8').read()
before = s.count('<article class="iv-item"')
if before == 48:
    print('already integrated (48), only ensure index assertion')
    sys.exit(0), before  # 44 标签 = 43 入索引 + 1 legacy


def card(cid, title_en, title_zh, meta1, date_disp, meta3, ctx_en, ctx_zh, quote_en, quote_zh, after_note):
    return f'''  <article class="iv-item" id="{cid}">
    <h2 data-en="{title_en}">{title_zh}</h2>
    <div class="iv-meta"><span class="iv-badge" data-en="{meta1}">{meta1}</span><a class="iv-badge" href="#{cid}" title="定位到本条 · Permalink">{date_disp}</a><span class="iv-badge">{meta3}</span></div>
    <p class="ctx" data-en="{ctx_en}">{ctx_zh}</p>
    <blockquote>{quote_en}</blockquote>
    <p class="iv-zh">{quote_zh}</p>
    <p class="after"><b>注/后续：</b>{after_note}</p>
  </article>

'''


cards = {
    'i2013-05-29': card(
        'i2013-05-29',
        '&ldquo;That sense of freedom&rdquo;', '「那份自由感」',
        'AllThingsD D11 大会', '2013.05.29',
        'elonmuskarchive.org 官方转写（YouTube 源）',
        'On range anxiety, he answers with freedom rather than numbers: even commuters who never leave the city want to know they could drive from Boston to DC.',
        '被问到「里程焦虑」时，他给出的答案是自由感而非数字：即便只在市内通勤的人，也想知道自己随时可以开车从波士顿去华盛顿。',
        '“Even if you only drive your car, commuting to work well within the range of the car and a few errands and stuff, you always want that sense of freedom that if I had to, I could get in this car and go from Boston to DC or something.”',
        '「哪怕你只是开车通勤、里程完全够用、顺路办点事，你也始终想要那份自由感——万一需要，我可以钻进这辆车，从波士顿一路开到华盛顿。」',
        '「里程焦虑」的答案后来落进产品：超级充电网络与长续航车型把这份「自由感」做成标配。保留池成员，2026-10-02 官方转写核验后立条。'),
    'i2019-02-19': card(
        'i2019-02-19',
        '&ldquo;Full self-driving this year, with certainty&rdquo;', '「今年Feature Complete级自动驾驶，我确定」',
        'ARK Invest Podcast', '2019.02.19',
        'elonmuskarchive.org 官方转写（YouTube 源）',
        'Asked about the Autopilot roadmap, he stakes a personal claim — he runs Autopilot engineering week by week — and promises feature-complete FSD within the year. ASR flat-cased; capitalization and punctuation added by editor.',
        '被问到 Autopilot 路线图时，他押上个人背书——每周亲自过问 Autopilot 工程——并承诺年内达成 feature complete 级全自动驾驶。（语音转写为平文本，大小写与标点为编者所加。）',
        '“…there’s feature complete full self-driving this year with certainty. This is something that we control and I managed Autopilot and engineering directly every week in detail, so I’m certain of this.”',
        '「……年内就会有 feature complete 级全自动驾驶，这一点我确定。这是我们自己可控的事，我每周都在细节层面直接管着 Autopilot 与工程，所以我很确定。」',
        '承诺对账：2019 年末只达成「city streets beta」的一部分，正式 FSD beta 于 2020-10 推送——承诺未按年兑现，已列入承诺对账页口径。保留池成员，2026-10-02 官方转写核验后立条。'),
    'i2019-06-13': card(
        'i2019-06-13',
        '&ldquo;Uncharted territory will result in failures&rdquo;', '「未涉之地必然有失败」',
        'E3 Coliseum 对谈', '2019.06.13',
        'elonmuskarchive.org 官方转写（YouTube 源）',
        'On innovation and failure, in conversation at E3 Coliseum: trying something new means the odds of failure are high by definition. Transcript is all-caps ASR; case normalized by editor.',
        '在 E3 Coliseum 对谈中谈创新与失败：做创新的事就等于走进无人区，失败概率天然很高。（转写为全大写形态，大小写为编者归一。）',
        '“If you’re going to try something innovative, you are in unexplored territory, so the odds that something will go wrong are pretty high. … Uncharted territory will result in failures necessarily — or you’re not trying hard enough.”',
        '「你要做创新的事，就走进了未被勘探的地域，出问题的概率自然很高。……未经勘探之地必然带来失败——否则就是你还不够拼。」',
        '与 SpaceX 三连败后的「失败即数据」口径一脉相承（见 <a href="#i2008-08-05">i2008-08-05</a>）。保留池成员，2026-10-02 官方转写核验后立条。'),
    'i2021-09-28': card(
        'i2021-09-28',
        '&ldquo;It&rsquo;d be just freaking cool&rdquo;', '「就是觉得很酷，来吧」',
        'Code Conference 2021', '2021.09.28',
        'elonmuskarchive.org 官方转写（YouTube 源）',
        'On why a Moon base matters, he skips the science case and leads with the honest one — it would be freaking cool, and humanity should represent. ASR flat-cased; capitalization and punctuation added by editor.',
        '被问及月球基地的意义，他跳过科学论证先说大实话：就是觉得很酷，人类得去 represent。（语音转写为平文本，大小写与标点为编者所加。）',
        '“I think it’d be just freaking cool. I mean, come on — humanity, let’s have a base on the moon.”',
        '「我觉得那就是他妈的很酷。来吧——人类，我们在月球上建个基地吧。」',
        '同场他也点评了 Branson 与 Bezos 的亚轨道飞行：「他们把钱花在推进太空事业上，这是好事——人类终归要做航天文明、要去群星之间。」保留池成员，2026-10-02 官方转写核验后立条。'),
}

# 时间序插入锚：i2013-02-27 后插 i2013-05-29；i2016-09-27 后（2017-04 前）插 i2019-02-19？——时间序：2019-02-19 在 i2017-04-28 与 i2018 之间
# 精确锚：i2013-05-29 插在 id="i2013-02-27" 的卡结束（下一卡注释/article 前）——用下一卡 id 定位
# i2019-02-19 插在 id="i2017-04-28" 卡结束与 id="i2017-07-28" 卡开始之间
# i2019-06-13 插在 id="i2019-04-12" 卡结束与 id="i2019-11" 卡开始之间
# i2021-09-28 插在 id="i2021-07-30" 卡结束与 id="i2021-12" 卡开始之间
anchors = [
    ('i2013-02-27', 'i2014-09-25', cards['i2013-05-29']),
    ('i2017-04-28', 'i2017-07-28', cards['i2019-02-19']),
    ('i2019-04-12', 'i2019-11', cards['i2019-06-13']),
    ('i2021-07-30', 'i2021-12', cards['i2021-09-28']),
]
for prev_id, next_id, c in anchors:
    # 插入点 = 下一卡 <article 行首（不用注释锚——分组注释会 rfind 到远处）
    marker = f'<article class="iv-item" id="{next_id}">'
    i = s.find(marker)
    assert i > 0, next_id
    s = s[:i] + c + s[i:]

after = s.count('<article class="iv-item"')
assert after == 48, after
for cid in cards:
    assert s.count(f'id="{cid}"') == 1, cid
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print(f'interviews.html: {before} -> {after} iv-item')

p2 = 'tools/build-search-index.py'
t = io.open(p2, encoding='utf-8').read()
old = "'访谈与表态': 43"
if old in t:
    t = t.replace(old, "'访谈与表态': 47", 1)
io.open(p2, 'w', encoding='utf-8', newline='').write(t)
print('index assertion 43 -> 47')
