# -*- coding: utf-8 -*-
"""V12 R02: X 帖断代回捞 III（2025-08→2026-10）六卡集成。
锚 = xp-grid 闭合 + chapter-summary 开标签（全页唯一），new = 2 张 2025 卡 + 2026 年份条 + 4 张 2026 卡 + 拼回。
每卡：镜像 transcript 逐字原文 + snowflake 解码 UTC（已对表与镜像 date 一致）+ 中译 + 背景注。
"""
import io, re, sys

F = 'x-posts.html'
s = io.open(F, encoding='utf-8').read()

CARDS_2025 = '''    <div class="tweet-card" id="p2025-08-16">
      <div class="tweet-top"><span class="tweet-avatar">M</span><span class="tweet-who"><b>Elon Musk</b><span>@elonmusk</span></span><a class="tweet-date" href="#p2025-08-16" title="定位到本帖 · Permalink">2025.08.16</a></div>
      <p class="tweet-text">The Tesla Robotaxi service area is already larger than any competitors in Austin and the Bay Area</p>
      <p class="tweet-zh">Tesla 的 Robotaxi 服务面积，现在已经比 Austin 和湾区任何一家对手都大。</p>
      <p class="tweet-note"><b>背景/后续：</b>断代回捞（V12 R02；原帖 status/1956765617517985951 · 镜像逐字存档；snowflake 解码 UTC 2025-08-16 17:10）。Austin 首发（2025-06-22）后近两个月的规模对标帖——「面积已超所有对手」是他给 Robotaxi 定的第一个横向基准。承诺与结果的逐案对账见 <a href="promises.html" data-en="Promises">承诺与结果</a>。</p>
    </div>
    <div class="tweet-card" id="p2025-10-29">
      <div class="tweet-top"><span class="tweet-avatar">M</span><span class="tweet-who"><b>Elon Musk</b><span>@elonmusk</span></span><a class="tweet-date" href="#p2025-10-29" title="定位到本帖 · Permalink">2025.10.29</a></div>
      <p class="tweet-text">Tesla Model Y robotaxi service now available in the greater Austin area!</p>
      <p class="tweet-zh">Tesla Model Y 的 robotaxi 服务，现在全大奥斯汀地区都能用了！</p>
      <p class="tweet-note"><b>背景/后续：</b>断代回捞（V12 R02；原帖 status/1983428037145432381 · 镜像逐字存档；snowflake 解码 UTC 2025-10-29 06:57）。首发四个月后服务区扩张到「greater Austin」全境（TechCrunch/CNBC 报道口径）——从试点小区到都会区，是监管与运营双线的实质跨步。</p>
    </div>
'''

YEAR_2026 = '      <div class="xp-year" aria-hidden="true">2026</div>\n'

CARDS_2026 = '''    <div class="tweet-card" id="p2026-01-22">
      <div class="tweet-top"><span class="tweet-avatar">M</span><span class="tweet-who"><b>Elon Musk</b><span>@elonmusk</span></span><a class="tweet-date" href="#p2026-01-22" title="定位到本帖 · Permalink">2026.01.22</a></div>
      <p class="tweet-text">Just started Tesla Robotaxi drives in Austin with no safety monitor in the car.

Congrats to the @Tesla_AI team!

If you’re interested in solving real-world AI, which is likely to lead to AGI imo, join Tesla AI. Solving real-world AI for Optimus will be 100X harder than cars.</p>
      <p class="tweet-zh">Tesla 的 Robotaxi 刚刚在 Austin 开始了车内无安全监督员的行驶。

恭喜 @Tesla_AI 团队！

如果你有兴趣解决真实世界的 AI——在我看来它大概率通向 AGI——来加入 Tesla AI。为 Optimus 解决真实世界 AI，会比汽车难上 100 倍。</p>
      <p class="tweet-note"><b>背景/后续：</b>断代回捞（V12 R02；原帖 status/2014397578352226423 · 镜像逐字存档；snowflake 解码 UTC 2026-01-22 17:59）。车内安全监督员撤除是 Robotaxi 弧线的关键节点（CBS/CNBC 报道口径）；同一帖把「真实世界 AI」的难度天平首次压向 Optimus——100X 于汽车。Robotaxi 时间线两端即本卡与本墙最新一卡 <a href="#p2026-10-03">p2026-10-03</a>。</p>
    </div>
    <div class="tweet-card" id="p2026-07-01">
      <div class="tweet-top"><span class="tweet-avatar">M</span><span class="tweet-who"><b>Elon Musk</b><span>@elonmusk</span></span><a class="tweet-date" href="#p2026-07-01" title="定位到本帖 · Permalink">2026.07.01</a></div>
      <p class="tweet-text">Walking the Optimus production line in Fremont</p>
      <p class="tweet-zh">在弗里蒙特工厂走 Optimus 产线。</p>
      <p class="tweet-note"><b>背景/后续：</b>断代回捞（V12 R02；原帖 status/2072214077372518657 · 镜像逐字存档；snowflake 解码 UTC 2026-07-01 07:01；原帖附产线现场照，t.co 图链不入正文——站内 Gamestonk 卡先例）。产线实拍首次上墙：Optimus 从原型叙事转入制造纪律的同帖语境下，他同日补发「初期产能会极其缓慢」的预期管理帖（status/2072448521513685263 · 镜像逐字在档）。三周后账本记下「Optimus 史上最大产品」表态，见 <a href="primary.html#e2026-07-22" data-en="Ledger">账本 e2026-07-22</a>。</p>
    </div>
    <div class="tweet-card" id="p2026-09-14">
      <div class="tweet-top"><span class="tweet-avatar">M</span><span class="tweet-who"><b>Elon Musk</b><span>@elonmusk</span></span><a class="tweet-date" href="#p2026-09-14" title="定位到本帖 · Permalink">2026.09.14</a></div>
      <p class="tweet-text">@techdevnotes Grok 4.8, which is a 2.5T model trained with our new C++ software stack, will finish training this week and start RL</p>
      <p class="tweet-zh">@techdevnotes Grok 4.8——一个用我们全新 C++ 软件栈训练的 2.5 万亿参数模型——本周完成训练，随即开始强化学习。</p>
      <p class="tweet-note"><b>背景/后续：</b>断代回捞（V12 R02；原帖 status/2099308197802631191 · 镜像逐字存档；snowflake 解码 UTC 2026-09-14 01:24）。Grok 4.8 技术规格首曝（2.5T 参数/C++ 自研栈/转 RL 训练）；同日他向网友确认「That will be Grok 5」的版本次序（status/2099455592670634034 · 镜像逐字在档）。注：Grok 4 发布（2025-07-09）在本墙断代窗界外未立卡，留档 EXPANSION。Grok 谱系见 <a href="grok.html" data-en="xAI &amp; Grok">xAI·Grok</a>，起点见账本 <a href="primary.html#e2025-02-18" data-en="Ledger">e2025-02-18</a>。</p>
    </div>
    <div class="tweet-card" id="p2026-10-03">
      <div class="tweet-top"><span class="tweet-avatar">M</span><span class="tweet-who"><b>Elon Musk</b><span>@elonmusk</span></span><a class="tweet-date" href="#p2026-10-03" title="定位到本帖 · Permalink">2026.10.03</a></div>
      <p class="tweet-text">Robotaxi operating hours moved from 10pm to 11pm.

The main thing we’re trying to solve is making sure that we don’t run over pets when they’re hard to see at night. Literally trying to avoid grey kittens on grey tarmac in the dark.</p>
      <p class="tweet-zh">Robotaxi 的运营时间从晚上 10 点延到 11 点。

我们现在要解决的主要问题，是确保车子不会在夜里撞上那些很难看清的小动物。字面意义上的：在黑暗里避开灰色路面上的灰色小猫。</p>
      <p class="tweet-note"><b>背景/后续：</b>断代回捞（V12 R02；原帖 status/2106239692866019479 · 镜像逐字存档；snowflake 解码 UTC 2026-10-03 04:27）。本墙最新一卡（回捞日前三天）：运营延时一小时看似微小，但「无监督夜间长尾场景」恰是 L4 的最后一程——他把工程焦点说成「灰色小猫」，是他一贯把长尾风险具象化的话术。Robotaxi 弧线起点见 <a href="#p2025-08-16">p2025-08-16</a>，承诺对账见 <a href="promises.html" data-en="Promises">承诺与结果</a>。</p>
    </div>
'''

ANCHOR = '  </div>\n\n  <div class="chapter-summary reveal">'
NEW = (CARDS_2025 + YEAR_2026 + CARDS_2026
       + '  </div>\n\n  <div class="chapter-summary reveal">')

if s.count(ANCHOR) != 1:
    sys.exit('锚不唯一: %d' % s.count(ANCHOR))
s2 = s.replace(ANCHOR, NEW)

# ---- 断言 ----
n_cards = len(re.findall(r'<div class="tweet-card" id="', s2))
n_perm = len(re.findall(r'<a class="tweet-date" href="#', s2))
n_text = len(re.findall(r'<p class="tweet-text">', s2))
n_zh = len(re.findall(r'<p class="tweet-zh">', s2))
n_year = len(re.findall(r'xp-year" aria-hidden="true">', s2))
for pid in ['p2025-08-16', 'p2025-10-29', 'p2026-01-22', 'p2026-07-01', 'p2026-09-14', 'p2026-10-03']:
    if f'id="{pid}"' not in s2:
        sys.exit(f'缺卡 {pid}')
    if s2.count(f'id="{pid}"') != 1:
        sys.exit(f'卡 {pid} 重复')
    if f'href="#{pid}"' not in s2:
        sys.exit(f'卡 {pid} 缺 Permalink')
assert n_cards == 40, n_cards
assert n_perm == 40, n_perm
assert n_text == 40 and n_zh == 40, (n_text, n_zh)
assert n_year == 9, n_year

io.open(F, 'w', encoding='utf-8', newline='').write(s2)
print('六卡集成 OK: cards=%d permalinks=%d text=%d zh=%d years=%d' % (n_cards, n_perm, n_text, n_zh, n_year))
