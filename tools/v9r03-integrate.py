# -*- coding: utf-8 -*-
"""V9-20 R03: x-posts.html 插入四张 2023–2025 帖卡（27→31）。

纪律：逐字克隆 tweet-card 五件套结构（R02 blk() 原样）；锚=下一张既有卡开标签
（末卡用容器闭合+chapter-summary 组合锚，全页唯一）；每步替换计数打印；
EOL 自适应。英文逐字出自 qa/v9-20/round-03/sources/*.json（镜像 transcript），
日期经 snowflake 解码对表（(id>>22)+1288834974657 → UTC，同日一致）。
"""
import io, re, sys

PATH = 'x-posts.html'
raw = io.open(PATH, encoding='utf-8', newline='').read()
NL = '\r\n' if '\r\n' in raw else '\n'
s = raw
D = NL

def rep(text, old, new, label, expect=1):
    n = text.count(old)
    if n != expect:
        print(f'FAIL {label}: anchor count={n} (expect {expect})')
        sys.exit(1)
    print(f'OK {label}: replaced {n}')
    return text.replace(old, new, expect)

# ---------- 改前断言 ----------
assert s.count('<div class="tweet-card" id="p') == 27, 'before: expect 27 cards'
ids_before = re.findall(r'<div class="tweet-card" id="(p[\d-]+)"', s)
print('before order:', ids_before)

def blk(card_id, date_disp, text_inner, zh_inner, note_inner):
    return (
        f'    <div class="tweet-card" id="{card_id}">{D}'
        f'      <div class="tweet-top"><span class="tweet-avatar">M</span><span class="tweet-who"><b>Elon Musk</b><span>@elonmusk</span></span><a class="tweet-date" href="#{card_id}" title="定位到本帖 · Permalink">{date_disp}</a></div>{D}'
        f'      <p class="tweet-text">{text_inner}</p>{D}'
        f'      <p class="tweet-zh">{zh_inner}</p>{D}'
        f'      <p class="tweet-note"><b>背景/后续：</b>{note_inner}</p>{D}'
        f'    </div>{D}'
    )

def para(txt):
    return txt.replace('\n\n', f'{D}{D}')

# ---------- 卡 1：p2023-11-30 Cybertruck 首交付 ----------
c1 = blk(
    'p2023-11-30', '2023.11.30',
    'First Cybertruck deliveries in 2 hours!',
    '首批 Cybertruck 两小时后交付！',
    '跳票四年的兑现时刻（原帖 status/1730283187127964138 · 镜像逐字存档；'
    'snowflake 解码 UTC 2023-11-30 17:50）——交付活动在得州超级工厂举行，'
    '首批仅十位左右车主提车（CNBC/AP 口径）。两小时后他补发致谢：'
    '「Massive congrats to the incredible Tesla team, from design through to manufacturing, '
    'for making Cybertruck real! I love you.」（status/1730342317993701521 · 镜像逐字在档）。'
    '从 2019.11 发布会防弹玻璃砸窗名场面到此整四年，起步价也从当年公布的 $39,900 走到 $60,990'
    '（CNBC 当日报道）——跳票与溢价一并入账，见账本 <a href="primary.html#e2023-11-30">e2023-11-30</a>。')

# ---------- 卡 2：p2024-01-30 特拉华判决怒斥 ----------
c2 = blk(
    'p2024-01-30', '2024.01.30',
    'Never incorporate your company in the state of Delaware',
    '永远不要在特拉华州注册你的公司。',
    '判决日怒斥（原帖 status/1752455348106166598 · 镜像逐字存档；snowflake 解码 UTC 2024-01-30 22:14）——'
    '数小时前，特拉华衡平法院 Chancellor Kathaleen McCormick 就 Tornetta 案裁定：2018 年那笔峰值约 560 亿美元'
    '的期权薪酬包批准程序失当，判决撤销（Reuters/AP 广泛报道）。动作链三连：次日发起投票'
    '「Should Tesla change its state of incorporation to Texas, home of its physical headquarters?」'
    '（01.31 · 镜像逐字在档），再次日宣布「The public vote is unequivocally in favor of Texas! '
    'Tesla will move immediately to hold a shareholder vote to transfer state of incorporation to Texas.」'
    '（02.01 · 镜像逐字在档）。弧线在 6.13 股东大会闭合：薪酬包重批与迁册德州双通过'
    '（账本 <a href="primary.html#e2024-06-13">e2024-06-13</a>）；当年 12 月初特拉华法院驳回翻案动议、'
    '维持原判（Reuters 报道）。')

# ---------- 卡 3：p2024-07-13 Trump 背书（V8 弃收件重验） ----------
c3 = blk(
    'p2024-07-13', '2024.07.13',
    'I fully endorse President Trump and hope for his rapid recovery',
    '我完全支持特朗普总统，并祝愿他迅速康复。',
    '巴特勒集会枪击约半小时后的站队帖（原帖 status/1812256998588662068 · 镜像逐字存档；'
    'snowflake 解码 UTC 2024-07-13 22:45，Reuters 记录枪响于 UTC 22:11 前后；帖尾附现场照片链接）。'
    'V8 期间因镜像覆盖率不足弃收，本轮以 Agent API 精确短语检索一击重验入册。此帖把数年「中间派」姿态'
    '一步切换为明确站队：同月 America PAC 成立接管战场州地面行动（FEC 文件 · Reuters 报道），'
    '大选周期他个人出资约 2.5 亿美元级（FEC 披露 · AP 汇总口径），10 月起直接登台集会；'
    'X 平台同步成为政治放大器（<a href="platform-x.html">平台变局</a>）。商业与政治自此合流——'
    '弧线下一站：决裂与建党，见 <a href="#p2025-07-05">p2025-07-05</a>。')

# ---------- 卡 4：p2025-07-05 America Party 建党宣言（逐字三段） ----------
ap_text = para(
    'By a factor of 2 to 1, you want a new political party and you shall have it!\n\n'
    'When it comes to bankrupting our country with waste & graft, we live in a one-party system, not a democracy.\n\n'
    'Today, the America Party is formed to give you back your freedom.')
ap_text = ap_text.replace('waste & graft', 'waste &amp; graft')
ap_zh = para(
    '以 2 比 1，你们想要一个新政党——那就给它！\n\n'
    '在以浪费与贪腐掏空国家这件事上，我们活在一体制之中，而非民主之中。\n\n'
    '今天，「美国党」成立，把你们的自由还给你们。')
c4 = blk(
    'p2025-07-05', '2025.07.05',
    ap_text, ap_zh,
    '从金主到组党的宣言帖（原帖 status/1941584569523732930 · 镜像逐字存档；'
    'snowflake 解码 UTC 2025-07-05 19:46）。前情：05 月底卸任 DOGE、06.05 与特朗普公开决裂'
    '（Reuters/AP 广泛报道）；06.30 他预告「If this insane spending bill passes, the America Party '
    'will be formed the next day」（status/1939806847504105683 · 镜像逐字在档）；07.04 独立日，'
    '大漂亮法案（One Big Beautiful Bill Act）签署同日，他发起独立日投票'
    '（status/1941119099532378580 · 镜像逐字在档）；本卡 2:1 宣言次日，他补上纲领——'
    '「The America Party is needed to fight the Republican/Democrat Uniparty」（07.06 · 镜像逐字在档）。'
    '市场当即计价政治风险：下一交易日（07.07）Tesla 股价收跌约 7%（Reuters 报道）。'
    '以个人公司版图为杠杆另立政党，美国商业史上几无先例；政治弧线起点见 <a href="#p2024-07-13">p2024-07-13</a>。')

# ---------- 插入 1：p2023-11-30 于 2024 年份条前 ----------
s = rep(s, '<div class="xp-year" aria-hidden="true">2024</div>',
        c1 + '<div class="xp-year" aria-hidden="true">2024</div>',
        'insert p2023-11-30 (before xp-year 2024)')

# ---------- 插入 2：p2024-01-30 于 p2024-03-11 前 ----------
anchor2 = '<div class="tweet-card" id="p2024-03-11">'
s = rep(s, anchor2, c2 + anchor2, 'insert p2024-01-30')

# ---------- 插入 3：p2024-07-13 于 p2024-10-13 前 ----------
anchor3 = '<div class="tweet-card" id="p2024-10-13">'
s = rep(s, anchor3, c3 + anchor3, 'insert p2024-07-13')

# ---------- 插入 4：p2025-07-05 于帖墙容器闭合前（末卡） ----------
anchor4 = f'  </div>{D}{D}  <div class="chapter-summary reveal">'
s = rep(s, anchor4, c4 + anchor4, 'insert p2025-07-05 (before wall close)')

# ---------- 帖墙小结补政治维度（EN+zh 同步） ----------
old_sum_en = ('The posting rhythm itself tells a story: 2018 was the year of maximum-volume promises; '
              '2022 was the year of owning the platform; 2024-2025 turned the feed into infrastructure '
              'announcements (cities, robots, robotaxis). The wall reads differently once you see it as '
              'one continuous negotiation with the public.')
new_sum_en = ('The posting rhythm itself tells a story: 2018 was the year of maximum-volume promises; '
              '2022 was the year of owning the platform; 2024-2025 turned the feed into infrastructure '
              'announcements (cities, robots, robotaxis) - and, from mid-2024, into a political weapon: '
              'endorsement, break, and a new party. The wall reads differently once you see it as one '
              'continuous negotiation with the public.')
old_sum_zh = ('发帖节奏本身就是故事：2018 年是最大音量的承诺之年；2022 年是拿下平台之年；'
              '2024-2025 年，信息流变成了基础设施公告（建市、机器人、Robotaxi）。'
              '把「与公众的一场连续谈判」看穿之后，这面墙读起来完全不同。')
new_sum_zh = ('发帖节奏本身就是故事：2018 年是最大音量的承诺之年；2022 年是拿下平台之年；'
              '2024-2025 年，信息流变成了基础设施公告（建市、机器人、Robotaxi），'
              '并在 2024 年中之后变成政治武器——背书、决裂、建党。'
              '把「与公众的一场连续谈判」看穿之后，这面墙读起来完全不同。')
s = rep(s, old_sum_en, new_sum_en, 'update summary EN')
s = rep(s, old_sum_zh, new_sum_zh, 'update summary zh')

# ---------- 改后断言 ----------
ids_after = re.findall(r'<div class="tweet-card" id="(p[\d-]+)"', s)
assert len(ids_after) == 31, f'after: expect 31 cards, got {len(ids_after)}'
assert len(set(ids_after)) == 31, 'card ids must be unique'
parsed = [tuple(int(x) for x in pid[1:].split('-')) for pid in ids_after]
assert parsed == sorted(parsed), f'cards must be in time order: {ids_after}'
for cid in ids_after:
    parts = re.split(r'(?=<div class="tweet-card" id=")', s)
    body = [p for p in parts if p.startswith(f'<div class="tweet-card" id="{cid}"')][0]
    assert body.count('<p class="tweet-zh">') == 1, f'{cid} tweet-zh must be exactly 1'
    assert body.count('<p class="tweet-text">') == 1, f'{cid} tweet-text must be exactly 1'
    assert body.count('<p class="tweet-note">') == 1, f'{cid} tweet-note must be exactly 1'
n_date = len(re.findall(r'<a class="tweet-date" href="#', s))
assert n_date == 31, f'tweet-date permalinks expect 31, got {n_date}'
# 年份条组一致性：每张卡归属年份与其前最近年份条一致
year_seq = re.findall(r'xp-year[^>]*>(\d{4})<', s)
assert year_seq == ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025'], year_seq
pos = 0
groups = []
for m in re.finditer(r'xp-year[^>]*>(\d{4})<|<div class="tweet-card" id="p(\d{4})-', s):
    if m.group(1):
        cur = m.group(1)
    else:
        assert m.group(2) == cur, f'card {m.group(2)} sits in year group {cur}'
# 页内互链目标在册
for ref in ('p2024-07-13', 'p2025-07-05', 'p2023-11-30', 'p2024-01-30'):
    assert f'id="{ref}"' in s, f'anchor target {ref} missing'
assert 'href="primary.html#e2023-11-30"' in s
assert 'href="primary.html#e2024-06-13"' in s
assert 'href="platform-x.html"' in s
assert 'waste &amp; graft' in s, 'HTML escape check'

io.open(PATH, 'w', encoding='utf-8', newline='').write(s)
print('after count:', len(ids_after))
print('after order:', ids_after)
print('DONE v9r03-integrate')
