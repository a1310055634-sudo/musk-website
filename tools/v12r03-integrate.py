# -*- coding: utf-8 -*-
"""V12 R03: X 帖早期加密 I（2018–2019）四卡集成（五帖，两连发一卡×2）。
三插入点全用「下一块开标签作锚」：A=2018 组尾两张（锚=2019 年份条行）、
B=07-26 插 05-25 与 11-21 之间（锚=11-21 卡开标签行）、C=11-23 插 2020 条前（锚=2020 年份条行）。
"""
import io, re, sys

F = 'x-posts.html'
s = io.open(F, encoding='utf-8').read()

def card(pid, date_disp, text, zh, note):
    return (f'    <div class="tweet-card" id="{pid}">\n'
            f'      <div class="tweet-top"><span class="tweet-avatar">M</span><span class="tweet-who"><b>Elon Musk</b><span>@elonmusk</span></span>'
            f'<a class="tweet-date" href="#{pid}" title="定位到本帖 · Permalink">{date_disp}</a></div>\n'
            f'      <p class="tweet-text">{text}</p>\n'
            f'      <p class="tweet-zh">{zh}</p>\n'
            f'      <p class="tweet-note">{note}</p>\n'
            f'    </div>\n')

# ---- 卡 1：p2018-09-18 BFR 首个箭体段（碳纤维时代） ----
C1 = card('p2018-09-18', '2018.09.18',
    '@yousuck2020 @SpaceX That’s the first BFR airframe/tank barrel section made of a new carbon fiber material',
    '@yousuck2020 @SpaceX 这是第一段 BFR 箭体/贮箱筒段，用的是新型碳纤维材料。',
    '<b>背景/后续：</b>早期加密（V12 R03；原帖 status/1041953361908576256 · 镜像逐字存档；snowflake 解码 UTC 2018-09-18 07:33）。BFR（Starship 前身）第一段实体箭体上墙——彼时还是碳纤维路线；不到两个月后他 180° 转向不锈钢（2018-12 首照公开，「why I switched」复盘帖 2026-08-23 镜像逐字在档），材料豪赌的弧线起点即此卡。试验台首飞见 <a href="#p2019-07-26">p2019-07-26</a>。')

# ---- 卡 2：p2018-10-04 SEC「做空者致富委员会」typo 两连发 ----
C2 = card('p2018-10-04', '2018.10.04',
    'Just want to that the Shortseller Enrichment Commission is doing incredible work. And the name change is so on point!\n\n'
    '@Scobleizer @Tesla Sorry about the typo. That was unforgivable. Why would they be upset about their mission? It’s what they do.',
    '只是想说，「做空者致富委员会」的工作实在出色。这次改名改得也太到位了！\n\n'
    '@Scobleizer @Tesla 抱歉打错了字。这不可原谅。他们怎么会介意别人提起自己的使命呢？这就是他们的本职啊。',
    '<b>背景/后续：</b>早期加密（V12 R03；原帖 status/1047943670350020608 + status/1047953389743554560 · 镜像逐字存档；snowflake 解码 UTC 2018-10-04 20:16/20:55）。与 SEC 和解（2018-09-29：卸任董事长+2000 万罚金，Reuters/CNBC 广泛报道）落定五天后，他把 SEC（美国证券交易委员会）戏称「做空者致富委员会」——首帖漏了 say 的 typo 被网友围猎，他顺势再补一刀「他们怎么会介意自己的使命」（typo 原样保留，站内惯例）。funding secured 风暴最著名的余震；上半场见 <a href="#p2018-08-07">p2018-08-07</a>。')

# ---- 卡 3：p2019-07-26 Starhopper 150m ----
C3 = card('p2019-07-26', '2019.07.26',
    'Starhopper flight successful. Water towers *can* fly haha!!',
    'Starhopper 试飞成功。水塔真的*能*飞哈哈！！',
    '<b>背景/后续：</b>早期加密（V12 R03；原帖 status/1154599520711266305 · 镜像逐字存档；snowflake 解码 UTC 2019-07-26 03:49）。「星跳者」150 米悬停跳跃成功（NASA Spaceflight/LabPadre 直播口径）——不锈钢水塔造型被嘲了近两年，他只用一个动词回敬：水塔*能*飞。这台 20 米试验台直通后来的星舰轨道飞行；推进团队致谢见 <a href="#p2019-05-25">p2019-05-25</a>。')

# ---- 卡 4：p2019-11-23 Cybertruck 146k + 零广告两连发 ----
C4 = card('p2019-11-23', '2019.11.23',
    '146k Cybertruck orders so far, with 42% choosing dual, 41% tri &amp; 17% single motor\n\n'
    'With no advertising &amp; no paid endorsement',
    'Cybertruck 订单目前 14.6 万：42% 选双电机、41% 三电机、17% 单电机。\n\n'
    '没有投放任何广告，也没有付费代言。',
    '<b>背景/后续：</b>早期加密（V12 R03；原帖 status/1198344195317985280 + status/1198347240785338368 · 镜像逐字存档；snowflake 解码 UTC 2019-11-23 20:54/21:07）。发布晚会大锤砸玻璃翻车（<a href="#p2019-11-21">p2019-11-21</a>）48 小时后，他用数据把「翻车」叙事翻盘：14.6 万预订（100 美元可退订金，媒体广泛报道口径），次日追加 18.7 万（status/1198693994194014208 · 镜像逐字在档）。「零广告」自此成为 Cybertruck 营销的固定口径。')

A_2019YEAR = '      <div class="xp-year" aria-hidden="true">2019</div>'
A_2020YEAR = '      <div class="xp-year" aria-hidden="true">2020</div>'
A_1121CARD = '    <div class="tweet-card" id="p2019-11-21">'

for anchor in (A_2019YEAR, A_2020YEAR, A_1121CARD):
    if s.count(anchor) != 1:
        sys.exit(f'锚不唯一: {anchor!r} -> {s.count(anchor)}')

s = s.replace(A_2019YEAR, C1 + C2 + A_2019YEAR)
s = s.replace(A_1121CARD, C3 + A_1121CARD)
s = s.replace(A_2020YEAR, C4 + A_2020YEAR)

# ---- 断言 ----
n_cards = len(re.findall(r'<div class="tweet-card" id="', s))
n_perm = len(re.findall(r'<a class="tweet-date" href="#', s))
n_text = len(re.findall(r'<p class="tweet-text">', s))
n_zh = len(re.findall(r'<p class="tweet-zh">', s))
n_year = len(re.findall(r'xp-year" aria-hidden="true">', s))
for pid in ['p2018-09-18', 'p2018-10-04', 'p2019-07-26', 'p2019-11-23']:
    if s.count(f'id="{pid}"') != 1 or f'href="#{pid}"' not in s:
        sys.exit(f'卡 {pid} 异常')
assert n_cards == 44 and n_perm == 44, (n_cards, n_perm)
assert n_text == 44 and n_zh == 44, (n_text, n_zh)
assert n_year == 9, n_year

io.open(F, 'w', encoding='utf-8', newline='').write(s)
print('四卡集成 OK: cards=%d permalinks=%d text=%d zh=%d years=%d' % (n_cards, n_perm, n_text, n_zh, n_year))
