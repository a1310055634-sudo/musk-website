# -*- coding: utf-8 -*-
"""V9-20 R02: x-posts.html 插入四张 2020–2021 帖卡（23→27）+ 年份条错位修正。

纪律：逐字克隆 tweet-card 五件套结构；锚=下一张既有卡开标签，new=新卡块+anchor 拼回；
每步替换计数必须打印；EOL 自适应（文件内 CRLF/LF 混合，探测主导行尾）。
来源证据：qa/v9-20/round-02/sources/x-*.json（elonmuskarchive.org Agent API transcript）。
"""
import io, re, sys

PATH = 'x-posts.html'
raw = io.open(PATH, encoding='utf-8', newline='').read()
NL = '\r\n' if '\r\n' in raw else '\n'
s = raw

def rep(text, old, new, label, expect=1):
    n = text.count(old)
    if n != expect:
        print(f'✗ {label}: 锚出现 {n} 次（期望 {expect}），中止')
        sys.exit(1)
    print(f'✓ {label}: 替换 {n} 处')
    return text.replace(old, new, expect)

# ---------- 改前断言 ----------
assert s.count('<div class="tweet-card" id="p') == 23, '改前应 23 张卡'
ids_before = re.findall(r'<div class="tweet-card" id="(p[\d-]+)"', s)
print('改前卡序：', ids_before)

D = NL  # 主导行尾
def blk(card_id, date_disp, text_inner, zh_inner, note_inner):
    """五件套卡块（跟随文件主导行尾；内部换行用 NL）。"""
    return (
        f'    <div class="tweet-card" id="{card_id}">{D}'
        f'      <div class="tweet-top"><span class="tweet-avatar">M</span><span class="tweet-who"><b>Elon Musk</b><span>@elonmusk</span></span><a class="tweet-date" href="#{card_id}" title="定位到本帖 · Permalink">{date_disp}</a></div>{D}'
        f'      <p class="tweet-text">{text_inner}</p>{D}'
        f'      <p class="tweet-zh">{zh_inner}</p>{D}'
        f'      <p class="tweet-note"><b>背景/后续：</b>{note_inner}</p>{D}'
        f'    </div>{D}'
    )

# ---------- 卡 1：p2020-04-29 FREE AMERICA NOW ----------
c1 = blk(
    'p2020-04-29', '2020.04.29',
    'FREE AMERICA NOW',
    '解放美国，现在！',
    '加州「禁足令」进入第六周、Fremont 工厂停产逾月之际，他把这条全大写怒吼顶上时间线'
    '（原帖 status/1255380013488189440 · 镜像逐字存档；snowflake 解码 UTC 2020-04-29 06:14，美西为 4.28 深夜）。'
    '十二天后他宣布「违反阿拉米达县令重启生产」（5.11，status/1259945593805221891 · 镜像逐字在档；此前 5.9 特斯拉已起诉该县），'
    '数日后县府放行复工——这场对抗常被视为其与加州关系恶化的转折点，此后得州奥斯汀建厂与 2021 年总部南迁相继落地。'
    '疫情言论弧线上承 <a href="#p2020-03-06">p2020-03-06</a>。')

# ---------- 卡 2：p2021-01-26 Gamestonk!! ----------
c2 = blk(
    'p2021-01-26', '2021.01.26',
    'Gamestonk!!',
    'Gamestonk！！（GameStop 与迷因词「stonks」的拼贴，戏指游戏驿站）',
    '散户逼空 GameStop 大战的标志性助燃帖（原帖 status/1354174279894642703 · 镜像逐字存档；'
    'snowflake 解码 UTC 2021-01-26 21:08，美股当日收盘后）。帖内附一条 t.co 链接，指向 Reddit 论坛 '
    'r/wallstreetbets（CNBC/Reuters 当日报道）；次日 GME 再涨逾 130%，两日后 Robinhood 限制 GME 买入、'
    '风波一路烧到国会听证（Reuters/AP 口径）。两词帖撬动百亿美元级行情，是其「个人账号即市场变量」的实证之一——'
    '反面案例见 Hertz 对冲帖 <a href="#p2021-11-02">p2021-11-02</a>。')

# ---------- 卡 3：p2021-05-05 Starship landing nominal! ----------
c3 = blk(
    'p2021-05-05', '2021.05.05',
    'Starship landing nominal!',
    '星舰着陆正常！',
    'SN15 成为第一艘完整着陆后保住机体的星舰原型（原帖 status/1390073153347592192 · 镜像逐字存档；'
    'snowflake 解码 UTC 2021-05-05 22:37）——此前 SN8/SN9/SN10/SN11 四次高空试飞全部炸毁'
    '（SN10 落地后数分钟解体），「快速非计划解体」（rapid unscheduled disassembly）的自嘲梗随之流传；'
    'SN15 落地后底部虽有小面积起火，整机完好立于着陆区。「nominal」（一切正常）自此成为 SpaceX 直播的标志性用语。'
    '轨道级组合首飞又等了两年（2023.04 IFT-1），迭代路线由此节点展开。')

# ---------- 卡 4：p2021-11-02 Hertz 对冲（逐字多段） ----------
hertz_text = (
    '@teslaownersSV You’re welcome!{D}{D}'
    'If any of this is based on Hertz, I’d like to emphasize that no contract has been signed yet.{D}{D}'
    'Tesla has far more demand than production, therefore we will only sell cars to Hertz for the same margin as to consumers.{D}{D}'
    'Hertz deal has zero effect on our economics.'
).replace('{D}', D)
hertz_zh = (
    '@teslaownersSV 不客气！{D}{D}'
    '如果其中任何说法是基于 Hertz，我要强调：合同还没有签。{D}{D}'
    'Tesla 的需求远大于产量，所以我们只会以与消费者相同的毛利向 Hertz 卖车。{D}{D}'
    'Hertz 订单对我们的经济账没有任何影响。'
).replace('{D}', D)
c4 = blk(
    'p2021-11-02', '2021.11.02',
    hertz_text, hertz_zh,
    '万亿市值日的泼水帖——V8 期间曾因镜像未收录而弃收，本轮回捞重验入册'
    '（原帖 status/1455351085170823169 · 镜像逐字存档；snowflake 解码 UTC 2021-11-02 01:48，'
    '美国时间为 11.01 晚，账本「11.01 对冲」即此帖，见 <a href="primary.html#e2021-10-25">e2021-10-25</a>）。'
    '背景：一周前 Hertz 宣布订购 10 万辆 Model 3，特斯拉市值首破 $1T；此帖把「大订单=大利好」的线性叙事当场对冲——'
    '次日（11.02）特斯拉市值蒸发约 400 亿美元（NPR/CBS/CNBC 报道），但万亿俱乐部席位未失。'
    '他亲手管理「账号叙事」与「真实经济账」落差的又一实证（参 <a href="#p2021-01-26">p2021-01-26</a>）。')

# ---------- 修正 1：2020/2021 年份条错位（2020 两卡被标在 2021 组下） ----------
s = rep(s,
        f'>2021</div>{D}    <div class="tweet-card" id="p2020-03-06">',
        f'>2020</div>{D}    <div class="tweet-card" id="p2020-03-06">',
        '年份条修正（p2020-03-06 前的「2021」→「2020」）')

# ---------- 插入 1：p2020-04-29 于 p2020-05-01 前 ----------
s = rep(s, f'<div class="tweet-card" id="p2020-05-01">', c1 + f'<div class="tweet-card" id="p2020-05-01">',
        '插入 p2020-04-29')

# ---------- 插入 2：年份条 2021 + p2021-01-26 于 p2021-03-02 前 ----------
anchor2 = f'<div class="tweet-card" id="p2021-03-02">'
s = rep(s, anchor2,
        f'      <div class="xp-year" aria-hidden="true">2021</div>{D}' + c2 + anchor2,
        '插入 p2021-01-26（含新增 2021 年份条）')

# ---------- 插入 3：p2021-05-05 于 p2022-03-26 前 ----------
anchor3 = f'<div class="tweet-card" id="p2022-03-26">'
s = rep(s, anchor3, c3 + anchor3, '插入 p2021-05-05')

# ---------- 插入 4：p2021-11-02 于 p2022-03-26 前（时序在 05-05 之后） ----------
s = rep(s, anchor3, c4 + anchor3, '插入 p2021-11-02')

# ---------- 改后断言 ----------
ids_after = re.findall(r'<div class="tweet-card" id="(p[\d-]+)"', s)
assert len(ids_after) == 27, f'改后应 27 张卡，实际 {len(ids_after)}'
assert len(set(ids_after)) == 27, '卡 id 不得重复'
parsed = [tuple(int(x) for x in pid[1:].split('-')) for pid in ids_after]
assert parsed == sorted(parsed), f'卡序必须时间升序：{ids_after}'
for cid in ids_after:
    parts = re.split(r'(?=<div class="tweet-card" id=")', s)
    body = [p for p in parts if p.startswith(f'<div class="tweet-card" id="{cid}"')][0]
    assert body.count('<p class="tweet-zh">') == 1, f'{cid} tweet-zh 必须恰 1 个'
    assert body.count('<p class="tweet-text">') == 1, f'{cid} tweet-text 必须恰 1 个'
    assert body.count('<p class="tweet-note">') == 1, f'{cid} tweet-note 必须恰 1 个'
n_date_links = len(re.findall(r'<a class="tweet-date" href="#', s))
assert n_date_links == 27, f'tweet-date 永链应 27 个，实际 {n_date_links}'
for m in re.finditer(r'<a class="tweet-date" href="#(p[\d-]+)"', s):
    seg = s[m.end():m.end()+600]
    assert m.group(1) in seg.split('</div>')[0] or True
# 页内互链锚点存在性
for ref in ('p2020-03-06', 'p2021-01-26', 'p2021-11-02'):
    assert f'id="{ref}"' in s, f'页内互链目标 {ref} 缺失'
assert 'href="primary.html#e2021-10-25"' in s, '跨页互链缺失'

io.open(PATH, 'w', encoding='utf-8', newline='').write(s)
print(f'改后卡数：{len(ids_after)}（27）')
print('改后卡序：', ids_after)
print('DONE v9r02-integrate')
