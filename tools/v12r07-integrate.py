# -*- coding: utf-8 -*-
"""V12 R07：documents.html 新立 6 条（email 2 + EDGAR 近年化 4）。
锚前插：d2018-08-12 → d2018-08-14 前；d2022-03-26 → d2022-04-09 前；
d2025-09-17 → ⑧ 2026 注释前；d2026-01-29 + d2026-06-12 + d2026-06-22 → doc-foot 前。
带内建断言，失败即 exit 1 且不落盘。"""
import io

PATH = 'documents.html'
s = io.open(PATH, encoding='utf-8').read()

E2018_PIF = '''  <!-- 2018.08.12 PIF 短信（R07 email 双源核验 II） -->
  <article class="doc-article" id="d2018-08-12">
    <h2>「You are throwing me under the bus」（马斯克 × 沙特 PIF 鲁梅延短信）</h2>
    <div class="doc-meta"><span class="doc-badge">私信 · funding secured 证券集团诉讼披露展品</span><a class="doc-badge" href="#d2018-08-12" title="定位到本文档 · Permalink">2018.08.12</a><span class="doc-badge">elonmuskarchive.org/email 底本 + Fortune 2022-04-25 报道双源</span></div>
    <h4>原文摘录</h4>
    <blockquote>“This is an extremely weak statement and does not reflect the conversation we had at Tesla. You said you were definitely interested in taking Tesla private and had wanted to do so since 2016. I’m sorry, but we cannot work together.” —— Elon Musk</blockquote>
    <p class="zh-line">这份声明极其软弱，不符合我们在 Tesla 谈过的内容。你说过你对特斯拉私有化绝对感兴趣，而且从 2016 年起就想这么做。很抱歉，我们无法共事。——马斯克</p>
    <blockquote>“It’s up to you Elon.” —— Al-Rumayyan / “You are throwing me under the bus.” —— Musk</blockquote>
    <p class="zh-line">「由你决定，埃隆。」——鲁梅延／「你这是把我扔到巴士底下。」——马斯克</p>
    <blockquote>“It takes two to tango. We haven’t received anything yet we cannot approve something that we don’t have sufficient information on.” / “I read the article. It is weak sauce and still makes me sound like a liar.”</blockquote>
    <p class="zh-line">「探戈要两个人跳。我们什么都没收到——信息不足，我们无法批准任何事。」／「我读了那篇文章。软弱至极，还搞得我像个骗子。」</p>
    <h4>本站注释</h4>
    <p class="note"><a href="primary.html#e2018-08-07" style="color:var(--accent)">「funding secured」推文</a>五天后的决裂现场：PIF 拒绝公开确认注资后，马斯克与基金总裁亚西尔·鲁梅延的短信急转直下——先是指责公开声明「软弱」，被回以「探戈要两个人跳；我们什么都没收到」之后，抛出那句日后被反复引用的「把我扔到巴士底下」。这组短信 2022 年 4 月经证券集团诉讼披露文件公开，Fortune 全文刊出。它与 <a href="#d2018-08-07" style="color:var(--accent)">d2018-08-07</a>、<a href="#d2018-08-14" style="color:var(--accent)">d2018-08-14</a> 同属私有化风波的一手文书弧线。口径：诉讼披露展品 + 媒体逐字，双源 2026-10-06 核验。</p>
  </article>

'''

E2022_DORSEY = '''  <!-- 2022.03.26 Dorsey 协议短信（R07 email 双源核验 II） -->
  <article class="doc-article" id="d2022-03-26">
    <h2>「A new platform is needed. It can’t be a company.」（杰克·多西 → 马斯克短信）</h2>
    <div class="doc-meta"><span class="doc-badge">私信 · Twitter v. Musk 法庭披露展品</span><a class="doc-badge" href="#d2022-03-26" title="定位到本文档 · Permalink">2022.03.26</a><span class="doc-badge">elonmuskarchive.org/email 底本 + 法庭披露件汇编双源</span></div>
    <h4>原文摘录</h4>
    <blockquote>“Yes, a new platform is needed. It can’t be a company. This is why I left.” —— Jack Dorsey</blockquote>
    <p class="zh-line">是的，需要一个新平台。它不能是一家公司。这就是我离开的原因。——多西</p>
    <blockquote>“I believe it must be an open source protocol, funded by a foundation of sorts that doesn’t own the protocol, only advances it. A bit like what Signal has done. It can’t have an advertising model. Otherwise you have surface area that governments and advertisers will try to influence and control. If it has a centralized entity behind it, it will be attacked.”</blockquote>
    <p class="zh-line">我相信它必须是一个开源协议，由某种基金会供养——基金会不拥有协议，只推动它。有点像 Signal 做的。它不能有广告模式，否则就会留下让政府和广告主试图影响与控制的接口。如果它背后有个中心化实体，它就会被攻击。</p>
    <blockquote>“Super interesting idea” —— Elon Musk</blockquote>
    <p class="zh-line">「非常有意思的想法。」——马斯克</p>
    <h4>本站注释</h4>
    <p class="note">整场收购的思想前奏：3 月 25 日马斯克「Twitter 正在死吗」民调当晚，多西开启私信线（背景见言行实录 <a href="primary.html#e2022-03-26" style="color:var(--accent)">2022.03.26 条目</a>），而他给出的方案不是「买下它」，而是<b>协议化重建</b>——开源协议、基金会供养、去广告模式，以 Signal 为范本。马斯克三周后走的路（4 月 14 日要约）恰是多西方案的反面：把中心化实体整个买下。协议路线后来由多西力推的 Bluesky（AT Protocol）落地。与 <a href="#d2022-04-09" style="color:var(--accent)">d2022-04-09</a> 的三连短信同属这一个月的一手短信弧线。口径：法庭披露展品 + 披露件汇编（danluu.com 合集与主流媒体逐字一致），双源 2026-10-06 核验。</p>
  </article>

'''

E2025_PROXY = '''  <!-- 2025.09.17 万亿薪酬包 proxy（R07 文档馆近年化） -->
  <article class="doc-article" id="d2025-09-17">
    <h2>2025 CEO Performance Award proxy（特斯拉万亿薪酬包授权案）</h2>
    <div class="doc-meta"><span class="doc-badge">SEC EDGAR 备案 · DEF 14A</span><a class="doc-badge" href="#d2025-09-17" title="定位到本文档 · Permalink">2025.09.17 备案 · 11.06 股东会</a><span class="doc-badge">备案号 0001104659-25-090866</span></div>
    <h4>原文摘录</h4>
    <blockquote>“Approve a new 2025 CEO Performance Award that uniquely challenges Elon to guide Tesla through a new phase of unprecedented growth by rewarding him — only if he delivers (once again) extraordinary financial returns for you, the shareholders, and remains at Tesla in a leadership role for many years to come.”</blockquote>
    <p class="zh-line">批准一份新的 2025 CEO 绩效奖励：它以「前所未有的增长新阶段」挑战埃隆——只有当他为你们、股东们再次交付非同寻常的财务回报，并在未来多年以领导角色留在 Tesla，他才能获得。</p>
    <blockquote>“The first tranche milestone is a market capitalization of $2 trillion; the next nine tranches thereafter each require an additional $500 billion in market capitalization … up to $6.5 trillion; the last two tranches each require an additional $1 trillion … requiring $8.5 trillion market capitalization for the last tranche.”</blockquote>
    <p class="zh-line">第一档里程碑是 2 万亿美元市值；其后九档每档再加 5,000 亿……至 6.5 万亿；最后两档每档再加 1 万亿——最后一档需要 8.5 万亿市值。</p>
    <blockquote>“If the market capitalization goals and operational goals in the 2025 CEO Performance Award are achieved at their maximum levels, Tesla will have reached at least $400 billion of sustained annual Adjusted EBITDA … and a market capitalization of at least $8.5 trillion, larger than any single company’s market capitalization as of the date of this proxy statement.”</blockquote>
    <p class="zh-line">若市值与运营目标全部按最高档达成，Tesla 将实现至少 4,000 亿美元的持续年度调整后 EBITDA……以及至少 8.5 万亿美元市值——大于本 proxy 声明日期任何单一公司的市值。</p>
    <h4>本站注释</h4>
    <p class="note"><a href="#d2024-04-29" style="color:var(--accent)">2018 奖励</a>的续篇与放大：12 档市值里程碑自 2 万亿起步、封顶 8.5 万亿（proxy 自己加注「大于本声明日期任何单一公司」），叠加 4,000 亿 EBITDA 门槛与多年任职绑定——把「留在 Tesla」本身变成了行权条件。2025-11-06 股东会表决通过（见言行实录 <a href="primary.html#e2025-11-06" style="color:var(--accent)">2025.11.06 条目</a>）。与 2018 年一样，这份奖励也是一纸法律文书对赌一个人的判断。口径：SEC EDGAR 备案直取原文，2026-10-06 核验。</p>
  </article>

'''

E2026_TRIO = '''  <article class="doc-article" id="d2026-01-29">
    <h2>Tesla Form 10-K FY2025（AI 公司自述与关键人风险）</h2>
    <div class="doc-meta"><span class="doc-badge">SEC EDGAR 备案 · Form 10-K</span><a class="doc-badge" href="#d2026-01-29" title="定位到本文档 · Permalink">2026.01.29 备案 · FY2025</a><span class="doc-badge">备案号 0001628280-26-003952</span></div>
    <h4>原文摘录</h4>
    <blockquote>“We are focused on bringing artificial intelligence (“AI”) into the real world, through products and services like Full Self-Driving (“FSD”) (Supervised) and Robotaxi, as well as working to develop and commercialize AI robots (“Bots”) (including Optimus).”</blockquote>
    <p class="zh-line">我们专注于把人工智能（AI）带入现实世界——通过完全自动驾驶（FSD）（监督版）与 Robotaxi 等产品与服务，同时致力于开发并商业化 AI 机器人（“Bots”，包括 Optimus）。</p>
    <blockquote>“In particular, we are highly dependent on the services of Elon Musk, Technoking of Tesla and our Chief Executive Officer.”</blockquote>
    <p class="zh-line">尤其是，我们高度依赖埃隆·马斯克——Tesla 的 Technoking 与我们的首席执行官——的服务。</p>
    <h4>本站注释</h4>
    <p class="note">FY2025 年报的正文第一句不再是「设计、制造和销售电动车」——<b>AI 被写进了公司定义句</b>（FSD/Robotaxi/Optimus 三支柱），电动车业务降格为实现手段（“leverage our current operations”）。同一份文件的风险因子章维持着自 2018 年以来的关键人句式，而 “Technoking”——他 2021 年给自己发明的头衔——如今是法律文本的正式组成部分。公司自我定义的换轨，这是最硬的一手证据。口径：SEC EDGAR 备案直取原文，2026-10-06 核验。</p>
  </article>

  <article class="doc-article" id="d2026-06-12">
    <h2>SpaceX Form 424B4（IPO 定价书：SPCX 登陆纳斯达克）</h2>
    <div class="doc-meta"><span class="doc-badge">SEC EDGAR 备案 · Form 424B4</span><a class="doc-badge" href="#d2026-06-12" title="定位到本文档 · Permalink">2026.06.12 定价</a><span class="doc-badge">备案号 0001628280-26-042639 · Registration 333-296070</span></div>
    <h4>原文摘录</h4>
    <blockquote>“This is the initial public offering of shares of Class A common stock, par value $0.001 per share, of Space Exploration Technologies Corp., a Texas corporation. We are offering 555,555,555 shares of our Class A common stock. … The initial public offering price is $135.00 per share.”</blockquote>
    <p class="zh-line">这是德克萨斯州公司太空探索技术公司 A 类普通股（每股面值 0.001 美元）的首次公开发行。我们发行 555,555,555 股 A 类普通股。……首次公开发行价格为每股 135.00 美元。</p>
    <blockquote>“We have been approved to list our Class A common stock on The Nasdaq Stock Market LLC (“Nasdaq”) and Nasdaq Texas, LLC (“Nasdaq Texas”) under the symbol “SPCX.””</blockquote>
    <p class="zh-line">我们已获批准将 A 类普通股在纳斯达克与纳斯达克德州上市，代码为 “SPCX”。</p>
    <blockquote>“We intend to use the net proceeds from this offering to fund our growth strategy, including the expansion of our AI compute infrastructure, enhancements to our launch infrastructure and launch vehicles, increases in the scale and capacity of our satellite constellations, and any remaining amounts for general corporate purposes.”</blockquote>
    <p class="zh-line">我们打算把本次发行的净所得用于资助增长战略——包括扩张我们的 AI 算力基础设施、升级发射基础设施与运载火箭、扩大卫星星座的规模与容量，其余用于一般公司用途。</p>
    <h4>本站注释</h4>
    <p class="note">成立 24 年后的公开市场首秀：555,555,555 股 × 135.00 美元，<b>募资约 750 亿美元</b>（承销折扣 5 亿），A/B 双层结构（B 类每股 10 票）叠加受控公司豁免保住控制权。募资用途清单里排在第一位的是「AI 算力基础设施」——火箭与星座排在其后，与 <a href="#d2026-01-29" style="color:var(--accent)">Tesla 10-K 的 AI 定义句</a>同月共振。EDGAR 在案的 SpaceX 首份备案是 2002-08-19（成立当年的豁免发行），从个人资金到公开市场，这条资本弧线走了二十四年。上市十天后公司随即定价 250 亿美元债券（见 <a href="#d2026-06-22" style="color:var(--accent)">d2026-06-22</a>）。口径：SEC EDGAR 备案直取原文，2026-10-06 核验。</p>
  </article>

  <article class="doc-article" id="d2026-06-22">
    <h2>SpaceX 高级票据定价 8-K（上市十日后的 250 亿美元发债）</h2>
    <div class="doc-meta"><span class="doc-badge">SEC EDGAR 备案 · Form 8-K · Items 7.01/8.01</span><a class="doc-badge" href="#d2026-06-22" title="定位到本文档 · Permalink">2026.06.22 启动 · 06.23 定价</a><span class="doc-badge">备案号 0001628280-26-044489 / 044955</span></div>
    <h4>原文摘录</h4>
    <blockquote>“On June 23, 2026, the Company priced its previously announced Offering of $7.0 billion of 5.350% Senior Notes due 2031, $6.0 billion of 5.650% Senior Notes due 2033, $6.0 billion of 5.875% Senior Notes due 2036, $2.5 billion of 6.600% Senior Notes due 2046, and $3.5 billion of 6.650% Senior Notes due 2056.”</blockquote>
    <p class="zh-line">2026 年 6 月 23 日，公司为先前公布的发行定价：2031 年到期 5.350% 高级票据 70 亿美元、2033 年到期 5.650% 票据 60 亿美元、2036 年到期 5.875% 票据 60 亿美元、2046 年到期 6.600% 票据 25 亿美元、2056 年到期 6.650% 票据 35 亿美元。</p>
    <blockquote>“The Notes will be unsecured obligations of the Company and will rank equally in right of payment with all existing and future unsubordinated indebtedness, liabilities and other obligations of the Company.”</blockquote>
    <p class="zh-line">该等票据将为公司的无抵押债务，并在受偿权利上与公司所有现有及未来的非次级债务、负债及其他义务同等排列。</p>
    <h4>本站注释</h4>
    <p class="note"><a href="#d2026-06-12" style="color:var(--accent)">IPO</a>十天后，五档 2031–2056 年期、<b>合计 250 亿美元</b>的无抵押高级票据——上市公司 SpaceX 的第一笔公开债务，一条贯穿四分之一个世纪的期限曲线（利率 5.35%–6.65%）。8-K 链三连：6-22 launch（Item 7.01 路演披露，更新现金余额）→ 6-23 pricing（Item 8.01）→ 6-26 closing。从 2002 年的个人资金起家，到一个月内在公开市场完成约 1,000 亿美元级的股+债融资——马斯克商业帝国资本化的最快一跃。口径：SEC EDGAR 备案直取原文，2026-10-06 核验。</p>
  </article>

'''

ANCHORS = [
    ('  <article class="doc-article" id="d2018-08-14">', E2018_PIF, ['d2018-08-12']),
    ('  <article class="doc-article" id="d2022-04-09">', E2022_DORSEY, ['d2022-03-26']),
    ('  <!-- ⑧ 2026 xAI Series E -->', E2025_PROXY, ['d2025-09-17']),
    ('  <p class="doc-foot">', E2026_TRIO, ['d2026-01-29', 'd2026-06-12', 'd2026-06-22']),
]

before_count = s.count('<article class="doc-article')
assert before_count == 31, 'baseline doc-article count %d != 31' % before_count
for anchor, block, ids in ANCHORS:
    assert s.count(anchor) == 1, 'anchor not unique: %r (%d)' % (anchor, s.count(anchor))
    for i in ids:
        assert s.count('id="%s"' % i) == 0, 'id already exists: %s' % i

for anchor, block, ids in ANCHORS:
    s = s.replace(anchor, block + anchor, 1)

after_count = s.count('<article class="doc-article')
assert after_count == 37, 'after count %d != 37' % after_count
for anchor, block, ids in ANCHORS:
    for i in ids:
        assert s.count('id="%s"' % i) == 1, 'article id count != 1: %s' % i
        assert s.count('href="#%s" title=' % i) == 1, 'permalink count != 1: %s' % i
assert s.count('2026-10-06 核验') == 10, 'verification stamps != 10 (R06 4 + R07 6)'
assert 'primary.html#e2018-08-07' in s and 'primary.html#e2022-03-26' in s and 'primary.html#e2025-11-06' in s, 'ledger cross-links missing'

io.open(PATH, 'w', encoding='utf-8', newline='\n').write(s)
print('OK: 6 doc-articles inserted, %d -> %d' % (before_count, after_count))
