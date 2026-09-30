# -*- coding: utf-8 -*-
"""V9-20 R05: 访谈扩充 II —— 五条新立/扩充条目插入 interviews.html。
锚点策略：i2021-12-28-2 插在 i2021-12（#252 金钱是信息）之后；
i2023-11-10-2 插在 i2023-11（#400 speciesist）之后；
TED2013/Code2014/MKBHD2018 三条作为「R05 批次」插在 R04 批次最后一条 i2024-09-08 之后。
模板逐字克隆 R04 批次条目结构（类名一个不改），data-en 全配。
"""
import io, re, sys

PATH = 'interviews.html'
s = io.open(PATH, encoding='utf-8').read()

def entry(idattr, html):
    return '<article class="iv-item" id="%s">\n%s\n  </article>' % (idattr, html)

# ---------------- i2021-12-28-2 · Lex #252 为文明买保险 ----------------
E_252B = entry('i2021-12-28-2', '''    <h2 data-en="&ldquo;Life insurance for life&rdquo;">「给生命本身买保险」</h2>
    <div class="iv-meta"><span class="iv-badge" data-en="Lex Fridman Podcast #252, on civilization &amp; Mars">Lex Fridman 播客 #252 · 文明与火星段</span><a class="iv-badge" href="#i2021-12-28-2" title="定位到本条 · Permalink">2021.12.28</a><span class="iv-badge">elonmuskarchive.org 官方转写 · 字幕源</span></div>
    <p class="ctx" data-en="Pressed on why a money-losing rocket company matters at all, he reaches for Stephen Hawking's number — a one-percent-per-century chance of a civilization-ending event — and lands the whole Mars case in one phrase: life insurance for life.">被追问「一家亏钱的火箭公司到底有什么意义」时，他搬出霍金的那个数字——每世纪百分之一的文明终结概率——然后用一个词组给整个火星命题收尾：给生命本身买保险。</p>
    <blockquote>&ldquo;There's, let's say for argument's sake, a 1% chance per century of a civilization ending event. Like that was Stephen Hawking's estimate. I think he might be right about that. We should basically think of this, being a multi-planet species, just like taking out insurance for life itself, like life insurance for life.&rdquo; &mdash; &ldquo;The reason I guess I care about us becoming a multi-planet species and a space bearing civilization is foundationally, I love humanity.&rdquo;</blockquote>
    <p class="iv-zh">比方说，仅为论证起见，每个世纪有 1% 的概率发生文明终结事件——那是霍金的估计，我觉得他可能说得对。我们基本上应该把「成为多行星物种」这件事，就当作给生命本身买保险——给生命的寿险。——我猜，我关心「我们成为多行星物种、成为航天文明」的根本原因，是我爱人类。</p>
    <p class="after"><b>后续：</b>同场他把文明灭绝的方式分成两种：&ldquo;civilization could die with a bang or a whimper&rdquo;——文明可能以巨响或呜咽告终：人口崩溃是呜咽，第三次世界大战是巨响。听到「life insurance for life」，Lex 笑称这场访谈「怎么突然变成电视购物了」，他认真地确认了一遍：&ldquo;Life insurance for life, yes.&rdquo; 转写说明：镜像为官方视频字幕源（civilization ending / space bearing 等处无连字符，逐字保留），与 V8 R06 核实所用 PodScript 全文逐字对表一致。</p>''')

# ---------------- i2023-11-10-2 · Lex #400 言论自由的试金石 ----------------
E_400B = entry('i2023-11-10-2', '''    <h2 data-en="&ldquo;Free speech only matters if&hellip;&rdquo;">「言论自由的试金石」</h2>
    <div class="iv-meta"><span class="iv-badge" data-en="Lex Fridman Podcast #400, on X &amp; the press">Lex Fridman 播客 #400 · 平台与媒体段</span><a class="iv-badge" href="#i2023-11-10-2" title="定位到本条 · Permalink">2023.11.10</a><span class="iv-badge">lexfridman.com 官方逐字稿（01:43 / 02:02 段）</span></div>
    <p class="ctx" data-en="Walking through the Twitter Files and the old moderation lists, he gives the compressed version of what he actually bought X for — then turns on the press. Lex offers him an out ('it's better than mainstream media'); he takes the other road.">从 Twitter Files 讲到旧审查名单，他用一句话说清自己当初买下 X 到底为了什么——随后把话头转向媒体。Lex 递了句台阶「（X）已经比主流媒体好了」，他没接，走向了另一头。</p>
    <blockquote>&ldquo;Free speech only matters if people you don't like are allowed to say things you don't like. Because if that's not the case, you don't have free speech and it's only a matter of time before the censorship has turned upon you.&rdquo; &mdash; &ldquo;Mainstream media is almost relentlessly negative about everything. I mean, really, the conventional news tries to answer the question, what is the worst thing that happened on Earth today? And it's a big world. So on any given day, something bad has happened.&rdquo;</blockquote>
    <p class="iv-zh">言论自由之所以有意义，恰恰在于你不喜欢的人也有权说你不爱听的话。如果不是这样，那就没有言论自由——而且审查早晚会轮到你头上。——主流媒体对一切都近乎无情地负面。说真的，传统新闻试图回答的问题是：「今天地球上发生的最糟糕的事是什么？」世界这么大，任何一天总有坏事发生。</p>
    <p class="after"><b>后续：</b>这是他 2022 年 10 月买下 Twitter 的第一性注脚——从「唯有卓越的表现才算及格」（见本页 <a href="#i2022-11-16">i2022-11-16</a>）到平台所有权本身（专题见 <a href="platform-x.html">platform-x.html</a>）。同场再往前四十分钟，是他当众认领「病态乐观」（见本页 <a href="#i2023-11-10">i2023-11-10</a>）。转写说明：lexfridman.com 官方逐字稿，时间戳 01:43:13 / 02:02:38 段；镜像库日期记 2023-11-09（时区口径），本条沿用站内 11-10 锚（官方页面发布日）。</p>''')

# ---------------- i2013-02-27 · TED 2013 ----------------
E_TED = entry('i2013-02-27', '''    <h2 data-en="&ldquo;A rapidly and fully reusable rocket&rdquo;">「一枚完全且快速可复用的火箭」</h2>
    <div class="iv-meta"><span class="iv-badge" data-en="TED2013, with Chris Anderson">TED2013 大会 · 与 Chris Anderson 对谈</span><a class="iv-badge" href="#i2013-02-27" title="定位到本条 · Permalink">2013.02.27</a><span class="iv-badge">elonmuskarchive.org 官方转写</span></div>
    <p class="ctx" data-en="SpaceX is five years old and Falcon 9 has flown twice. On the TED stage he frames the real mission — not Mars first, but making rockets reusable: today every rocket flies once, like cruise ships that burn their ships after each voyage. The goal statement he gives here will take eleven more years to prove, on a tower catch.">SpaceX 成立五岁，Falcon 9 刚飞过两次。他在 TED 讲台上把真正的使命摆上台面——火星还在其次，先让火箭可复用：今天的每一枚火箭都只飞一次，就像游轮每航一次就烧掉船。他在这里给出的目标宣言，要到十一年后的塔架接住那一刻才被证明。</p>
    <blockquote>&ldquo;The goal of SpaceX is to try to advance rocket technology, and in particular to try to crack a problem that I think is vital for humanity to become a space-faring civilization, which is to have a rapidly and fully reusable rocket.&rdquo; &mdash; &ldquo;The space shuttle was an attempt at a reusable rocket&hellip; the parts that were reusable took a 10,000-person group nine months to refurbish for flight. So the space shuttle ended up costing a billion dollars per flight.&rdquo;</blockquote>
    <p class="iv-zh">SpaceX 的目标，是推进火箭技术——尤其是攻克一个我认为对人类成为航天文明至关重要的难题：一枚完全且快速可复用的火箭。——航天飞机曾是可复用火箭的一次尝试……其可复用部件需要一万人的团队花九个月翻修才能再飞。所以航天飞机最终每次飞行的成本是十亿美元。</p>
    <p class="after"><b>后续：</b>主持人 Anderson 以「游轮烧船」作比，他笑着接茬：&ldquo;Certain cruises are apparently highly problematic.&rdquo;（某些航线显然问题很大）。&ldquo;rapidly and fully reusable&rdquo; 这五个词此后出现在他每一次火箭演讲里，直到 2024 年 10 月 13 日塔架接住超重助推器（见本页 <a href="#i2024-10-13">i2024-10-13</a>）。同场他还口述了三代车价格阶梯：Roadster 十万、Model S 五万、第三代「三四年后」三万美元——这条阶梯的最后一格至今空着（见本页 <a href="#i2018-08-15">i2018-08-15</a>）。转写说明：官方视频字幕源，标点为编者所加；日期以镜像库锚 2013-02-27（TED 官方日程）为准。</p>''')

# ---------------- i2014-09-25 · Code Conference 2014 ----------------
E_CODE14 = entry('i2014-09-25', '''    <h2 data-en="A draft constitution for Mars">「火星宪法草案」</h2>
    <div class="iv-meta"><span class="iv-badge" data-en="Code Conference, with Kara Swisher">Code Conference · 与 Kara Swisher 对谈</span><a class="iv-badge" href="#i2014-09-25" title="定位到本条 · Permalink">2014.09.25</a><span class="iv-badge">elonmuskarchive.org 官方转写</span></div>
    <p class="ctx" data-en="Kara Swisher saves her last question for Mars: what about government, law and courts up there? He opens with a joke about having just declared himself King of Mars — then delivers the most specific governance proposal he has ever given on a stage.">Kara Swisher 把最后一问留给火星：那上面的政府、法律和法院怎么办？他以「刚宣布自己是火星国王」的玩笑开场——随后给出了他历次登台以来最具体的一份治理方案。</p>
    <blockquote>&ldquo;I think most likely the form of government on Mars would be a direct democracy&hellip; people voting directly on issues&hellip; I would recommend some adjustment for the inertia of laws&hellip; it should probably be easier to remove a law than create one&hellip; My recommendation would be, let's say, 60 of people need to vote in a law, but at any point greater than 40 percent of people can remove it. And any law should come with a sunset&hellip; a built-in sunset provision.&rdquo;</blockquote>
    <p class="iv-zh">火星上最可能的政府形式是直接民主……由人民直接对议题投票……我建议对「法律的惯性」做些修正……废除一条法律应该比创设一条更容易。我的建议是：比方说，六成的人同意才能立一条法，但任何时候只要有超过四成的人同意，就可以废除它。而且任何法律都应自带日落条款——内建的到期失效条款。</p>
    <p class="after"><b>后续：</b>十一年后的 2025 年 7 月，他真的发布了政党纲领（见 X 帖史 <a href="x-posts.html#p2025-07-05">p2025-07-05</a> America Party）——对「立法只增不减」的批评，与这场「法律应有日落条款」的 2014 年设想互为镜像。转写说明：字幕平面化（口误与重复从略、标点为编者所加）；「60 of people」处字幕脱漏百分号，中文按 60% 对译；&ldquo;King of Mars&rdquo; 打趣的字幕作 &ldquo;king of moss&rdquo;（误听），未入引语块。</p>''')

# ---------------- i2018-08-15 · MKBHD Talking Tech ----------------
E_MKBHD = entry('i2018-08-15', '''    <h2 data-en="&ldquo;We're not spending money on advertising&rdquo;">「我们不花一分钱广告费」</h2>
    <div class="iv-meta"><span class="iv-badge" data-en="Talking Tech with Marques Brownlee (MKBHD), Tesla factory">Talking Tech · 与 Marques Brownlee，Tesla 工厂</span><a class="iv-badge" href="#i2018-08-15" title="定位到本条 · Permalink">2018.08.15</a><span class="iv-badge">elonmuskarchive.org 官方转写</span></div>
    <p class="ctx" data-en="Deep in 'production hell,' with the Model 3 ramp at full crisis pitch, he sits down on a factory balcony at Fremont with the biggest tech channel on YouTube — and explains why Tesla has never bought an ad.">「生产地狱」最深处，Model 3 爬坡正焦头烂额。他在弗里蒙特工厂的鸟瞰平台上，接待了 YouTube 最大的科技频道——并解释了 Tesla 为什么从来不买广告。</p>
    <blockquote>&ldquo;The way to sell any product is through word of mouth&hellip; the key is to have a product that people love&hellip; We're not spending money on advertising or endorsements&hellip; Anyone who buys our car, they just bought it because they like the car. And it's genuine. No discounts &mdash; I actually even pay full retail price for my own cars.&rdquo;</blockquote>
    <p class="iv-zh">卖任何产品，靠的都是口碑……关键是做出人们真正热爱的产品……我们不花钱做广告，也不花钱请代言人……买我们车的人，买它就是因为他们喜欢这辆车。这是真的。没有折扣——我自己的车，都是付全价买的。</p>
    <p class="after"><b>后续：</b>同场被问到「更便宜的 Tesla」，他给出的答案是「最终做到 2.5 万美元的车……如果真下狠功夫，也许三年」——那是 2018 年说的三年。这个价位档至今没有量产车兑现（标准续航 Model 3 曾短暂挂 3.5 万美元），「公开承诺、把期限当工程变量」的又一例，见专题 <a href="promises.html#promises-s4">承诺与结果 · 四</a>。六个月前他刚给「生产地狱」下过定义（见本页 <a href="#i2017-07-28">i2017-07-28</a>）。转写说明：官方视频字幕平面化，大小写与标点为编者所加；日期以镜像库锚 2018-08-15（视频发布日）为准。</p>''')

def insert_after_article(s, anchor_id, new_html, comment):
    m = re.search(r'<article class="iv-item" id="%s">' % re.escape(anchor_id), s)
    assert m, 'anchor not found: ' + anchor_id
    end = s.index('</article>', m.end()) + len('</article>')
    block = '\n<!-- %s -->\n%s' % (comment, new_html)
    return s[:end] + block + s[end:]

# 插入顺序：从后往前避免位置失效（本实现每次重新查找，顺序无关，但按逻辑排）
s = insert_after_article(s, 'i2021-12', E_252B, 'R05 · Lex #252 为文明买保险')
s = insert_after_article(s, 'i2023-11', E_400B, 'R05 · Lex #400 言论自由的试金石')
s = insert_after_article(s, 'i2024-09-08', E_TED + '\n\n' + E_CODE14 + '\n\n' + E_MKBHD,
                         'R05 批次：elonmuskarchive.org 官方转写（TED 2013 / Code 2014 / MKBHD 2018）')

io.open(PATH, 'w', encoding='utf-8', newline='').write(s)

# ---------------- 静态断言 ----------------
s2 = io.open(PATH, encoding='utf-8').read()
new_ids = ['i2013-02-27', 'i2014-09-25', 'i2018-08-15', 'i2021-12-28-2', 'i2023-11-10-2']
errors = []
for nid in new_ids:
    c = len(re.findall(r'id="%s"' % re.escape(nid), s2))
    p = len(re.findall(r'href="#%s"' % re.escape(nid), s2))
    if c != 1: errors.append('id %s 出现 %d 次' % (nid, c))
    if p < 1: errors.append('Permalink 缺失: %s' % nid)
n_arts = len(re.findall(r'<article class="iv-item"', s2))
n_bq = s2.count('<blockquote>')
n_zh = s2.count('class="iv-zh"')
if n_arts != 43: errors.append('article 计数 %d != 43' % n_arts)
if n_bq != 43: errors.append('blockquote 计数 %d != 43' % n_bq)
if n_zh != 43: errors.append('iv-zh 计数 %d != 43' % n_zh)
# data-en 覆盖：新增五条的 h2/ctx 必须有 data-en
for nid in new_ids:
    m = re.search(r'<article class="iv-item" id="%s">(.*?)</article>' % re.escape(nid), s2, re.S)
    blk = m.group(1)
    if '<h2 data-en=' not in blk: errors.append('%s h2 缺 data-en' % nid)
    if '<p class="ctx" data-en=' not in blk: errors.append('%s ctx 缺 data-en' % nid)
    if 'iv-meta' not in blk: errors.append('%s 缺 iv-meta' % nid)
    if 'class="after"' not in blk: errors.append('%s 缺 after' % nid)

if errors:
    print('FAIL'); [print(' -', e) for e in errors]; sys.exit(1)
print('OK: 五条插入完成，article=%d blockquote=%d iv-zh=%d，data-en 全配' % (n_arts, n_bq, n_zh))
