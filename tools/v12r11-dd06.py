# -*- coding: utf-8 -*-
"""V12 R11 II：生成 deep-dive-06.html《xAI 三年志》——逐字克隆 deep-dive-05.html
骨架（head/hero/section/footer/TOC/版本 span），只换内容。断言失败不落盘。"""
import io, re

src = io.open('deep-dive-05.html', encoding='utf-8').read()

# ---------- 1) head 区 ----------
s = src.replace('<title>深读 · 马斯克的 AI 战略布局 — 马斯克商业志 MUSK, INC.</title>',
                '<title>深读 · xAI 三年志 — 马斯克商业志 MUSK, INC.</title>')
s = s.replace('<meta name="description" content="从 OpenAI 捐资者到 AI 独立竞争者：动机链、三位一体与治理新变量——AI 战略的逻辑深读。" />',
              '<meta name="description" content="从一句话章程到 2300 亿估值：xAI 三年编年——成立、Grok、收购 X、All-Hands 与资本面。" />')
s = s.replace('<meta property="og:title" content="深读 · 马斯克的 AI 战略布局 — 马斯克商业志 MUSK, INC." />',
              '<meta property="og:title" content="深读 · xAI 三年志 — 马斯克商业志 MUSK, INC." />')

# ---------- 2) hero 区 ----------
s = s.replace('<div class="lr-kick">DEEP DIVE 05 · AI STRATEGY</div>',
              '<div class="lr-kick">DEEP DIVE 06 · XAI CHRONICLE</div>')
s = s.replace('<h1 data-en="His AI Strategy, Read as Logic">马斯克的 AI 战略布局</h1>',
              '<h1 data-en="xAI: A Three-Year Chronicle">xAI 三年志</h1>')
s = s.replace('<p class="lr-lead" data-en="OpenAI co-founder (2015) → exit (2018) → xAI (2023) → buying X (2025): this piece reads the strategy as logic — motive, the data×distribution×capital trinity, and the new governance variable. For the full timeline see the AI strategy page." style="font-family:Georgia,\'STSong\',serif">2015 OpenAI 联合创始 → 2018 退出 → 2023 xAI → 2025 收购 X：本篇把这段历程当作「逻辑」来读——动机链、数据×分发×资本的三位一体、以及治理新变量。完整时间线见 <a href="ai-strategy.html" style="color:var(--accent)">AI 战略布局页</a>，两页互为表里。</p>',
              '<p class="lr-lead" data-en="Founded 2023.07.12 with a one-line charter → Grok shipped that November → bought X (2025.03) → the first All-Hands report card (2026.02) → Series E at $230B: this piece reads the three years as a company chronicle — every node anchored to a first-hand record. For the strategy logic see the AI strategy page." style="font-family:Georgia,\'STSong\',serif">2023.07.12 一句话章程成立 → 当年 11 月 Grok 上线 → 2025.03 收购 X → 2026.02 首份成绩单 → 2300 亿估值的 E 轮：本篇把三年当作「公司志」来读——每个节点都有第一手记录可回溯。战略逻辑版见 <a href="ai-strategy.html" style="color:var(--accent)">AI 战略布局页</a>，姊妹篇互为表里。</p>')
s = s.replace('<b data-en="5 sections">5 个</b>', '<b data-en="5 sections">5 个</b>')
s = s.replace('<b data-en="≈ 900 chars">约 900 字</b>', '<b data-en="≈ 1,100 chars">约 1,100 字</b>')
s = s.replace('<b>v6.10.0 · 2026-09-29</b>', '<b>v<span class="site-version-val">11.11.0</span> · 2026-10-07</b>')
s = s.replace('<figcaption data-en="The Twitter HQ sign, November 2022 — two and a half years later the company was absorbed by xAI. Photo: osunpokeh / CC BY-SA 4.0, via Wikimedia Commons">2022 年 11 月的 Twitter 总部标牌——两年半后，这家公司被 xAI 反向吸收。</figcaption>',
              '<figcaption data-en="The Twitter HQ sign, November 2022 — the platform that became the data and distribution base of xAI in March 2025. Photo: osunpokeh / CC BY-SA 4.0, via Wikimedia Commons">2022 年 11 月的 Twitter 总部标牌——2025 年 3 月起，这块牌子背后的平台成了 xAI 的数据与分发底座。</figcaption>')

# ---------- 3) 五个 section ----------
def sec(n, new):
    global s
    pat = re.compile(r'<section class="lr-sec">\s*<h2[^>]*id="deep-dive-05-s' + str(n) + r'".*?</section>', re.S)
    m = pat.search(s)
    assert m, 'section %d not found' % n
    s = s[:m.start()] + new + s[m.end():]

sec(1, '''<section class="lr-sec">
    <h2 data-en="1. A one-line charter" id="deep-dive-06-s1">一、一句话章程（2023.07.12）</h2>
    <p data-en="On 2023.07.12 he announced xAI with a one-line charter and argued it as an AI-safety position on a Twitter Spaces session (<a href='primary.html#e2023-07-12'>ledger</a>):">2023 年 7 月 12 日，他以一句话章程官宣成立 xAI，并在 Twitter Spaces 上把它论证为一个 AI 安全命题（<a href="primary.html#e2023-07-12">账本</a>）：</p>
    <blockquote>“To understand the true nature of the universe.”
      <p class="lr-quote-zh">「理解宇宙的真实本质。」（<a href="primary.html#e2023-07-12">账本逐字</a>）</p>
    </blockquote>
    <p class="lr-note"><b data-en="Editor's note">编者注</b><span data-en="The charter is a mission statement, a recruiting pitch and an insurance policy in one sentence: a mission grand enough to justify the compute bill, and a safety framing pre-empting the regulatory question. (Editorial analysis, not his words.)">这句话同时是使命宣言、招聘广告与保险单：使命足够宏大以对冲算力账单，安全框架则提前回答监管之问。（编者分析，非其原话。）</span></p>
  </section>''')

sec(2, '''<section class="lr-sec">
    <h2 data-en="2. Grok in four months" id="deep-dive-06-s2">二、四个月出 Grok（2023.11）</h2>
    <p data-en="Four months after founding, Grok shipped to X Premium+ subscribers on 2023.11.04 (<a href='x-posts.html#p2023-11-04'>archived post</a>); Grok-1 weights went open-source in March 2024 — a small company shipping at consumer-company cadence. The event-archive view: <a href='events.html#e2023-11'>Grok: from chatbot toy to an OS layer</a>.">成立仅四个月，Grok 于 2023 年 11 月 4 日向 X Premium+ 订阅用户上线（<a href="x-posts.html#p2023-11-04">帖史存档</a>）；2024 年 3 月 Grok-1 权重开源——一家小公司跑出了消费级公司的发布节奏。事件档案视角见 <a href="events.html#e2023-11">Grok：从聊天玩具到操作系统层</a>。</p>
    <div class="lr-data-box" data-en="Cadence: Grok-1 (2023.11) → Grok-1.5 (2024.03) → Grok-2 (2024.08) → Grok 3 (2025.02) → Grok 4 (2025.07) → Grok 4.8 on a 2.5T C++ stack (2026.09, archived post)."><b>发布节奏</b>：Grok-1（2023.11）→ 1.5（2024.03）→ 2（2024.08）→ 3（2025.02）→ 4（2025.07）→ 4.8（2026.09，2.5T 参数 + C++ 推理栈，<a href="x-posts.html#p2026-09-14">帖史</a>）。</div>
  </section>''')

sec(3, '''<section class="lr-sec">
    <h2 data-en="3. Buying X: the company absorbs its own distribution" id="deep-dive-06-s3">三、收购 X：公司吞下自己的分发面（2025.03）</h2>
    <p data-en="On 2025.03.28 the all-stock merger folded X into xAI — announced in his own words (<a href='primary.html#e2025-03-28'>ledger</a>):">2025 年 3 月 28 日，全股票合并把 X 并入 xAI——以本人账号宣布（<a href="primary.html#e2025-03-28">账本</a>）：</p>
    <blockquote>“@xAI has acquired @X in an all-stock transaction.”
      <p class="lr-quote-zh">「@xAI 已全股票收购 @X。」（<a href="primary.html#e2025-03-28">账本逐字</a>）</p>
    </blockquote>
    <p data-en="For the company chronicle the merger is simpler than the strategy read: the AI company now owned its training data, its distribution surface and its own valuation story — and the Twitter-era chapter of this site (Platform) closed into the xAI chapter. See <a href='platform-x.html'>Platform: Twitter, X, and the xAI merger</a> for the deal arc.">对公司志而言，合并比战略解读更简单：AI 公司从此拥有了自己的训练数据、分发面与估值叙事——而本站的 Twitter 时代章节（平台变局）就此并入 xAI 章节。交易弧线见 <a href="platform-x.html">平台变局</a>。</p>
  </section>''')

sec(4, '''<section class="lr-sec">
    <h2 data-en="4. The first report card" id="deep-dive-06-s4">四、第一份成绩单（2026.02）</h2>
    <p data-en="At the first All-Hands on 2026.02.10 he called xAI 'a two-and-a-half-year-old toddler' and filed a full self-assessment — #1 in voice, image and video generation; Grokipedia positioned beyond Wikipedia; the first 100k-H100 cluster (<a href='primary.html#e2026-02-10'>ledger</a>).">2026 年 2 月 10 日首届 All-Hands 上，他以「两岁半的幼儿」自况并交出全景自评——语音/图像/视频生成第一、Grokkipedia 对标维基百科、首个 10 万张 H100 集群（<a href="primary.html#e2026-02-10">账本</a>）。</p>
    <blockquote>“xAI is only two and a half years old, basically a toddler, and we’ve nonetheless achieved number one in many arenas.”
      <p class="lr-quote-zh">「xAI 才两岁半，基本是个幼儿，但我们已经在很多领域做到了第一。」（<a href="primary.html#e2026-02-10">账本逐字</a>）</p>
    </blockquote>
    <p class="lr-note"><b data-en="Editor's note">编者注</b><span data-en="The self-assessment is checkable by design — forecasting benchmarks, generation volume and Grokipedia coverage can all be audited. That is the same bookkeeping instinct behind publishing the report card at all. (Editorial analysis, not his words.)">自评在设计上是可核的——预测基准、生成量与 Grokipedia 覆盖度都能逐项对账。这与「敢开成绩单」是同一种记账本能。（编者分析，非其原话。）</span></p>
  </section>''')

sec(5, '''<section class="lr-sec">
    <h2 data-en="5. The capital line, and what is not on file" id="deep-dive-06-s5">五、资本线，以及没有档案的部分</h2>
    <p data-en="Series E closed at $20B on a $230B post-money valuation, with NVIDIA and Cisco participating (<a href='documents.html#d2026-01'>the official announcement</a>; <a href='finance.html#xai'>finances</a>). Three years from a tweet to a top-tier valuation. What is not on file: xAI still has no independent public-disclosure channel of its own — its EDGAR footprints are the acquisition-era filings, and the disclosure pipeline for 2026 runs through related-party documents.">E 轮以 200 亿美元融资、投后 2300 亿估值收官，英伟达与思科参投（<a href="documents.html#d2026-01">官方公告</a>；<a href="finance.html#xai">财务全景</a>）。三年，从一条推文到一线估值。没有档案的部分：xAI 至今没有自己的独立公开披露通道——它在 EDGAR 的足迹是收购时代的关联文书，2026 年的披露管线仍经由关联方文件流转。</p>
    <p class="lr-note"><b data-en="Boundary condition">适用边界</b><span data-en="The three-year line is a bull-case chronicle written from announcements and ledger entries; the counterfactual (what the cadence cost, and what the related-party structure defers) has no public file yet. When xAI files its own first disclosure, this chronicle gets a chapter six. (Editorial analysis.)">这条三年线是一份用公告与账本写成的顺周期公司志；反事实（节奏的代价、关联结构的递延）尚无公开档案。等 xAI 交出第一份自己的披露文件，本志补第六章。（编者分析。）</span></p>
  </section>''')

# ---------- 4) lr-foot / TOC / 导航高亮 ----------
s = s.replace('DEEP DIVE 05', 'DEEP DIVE 06')
old_foot = s[s.find('<p class="lr-foot"'):]
old_foot = old_foot[:old_foot.find('</p>') + 4]
new_foot = '<p class="lr-foot" data-en="Maintained by the MUSK, INC. automation. Every node anchored to a first-hand record (ledger / archived posts / the official Series E announcement). Chinese translations are this site\'s own. Companion pieces: the AI strategy page (logic read) and grok.html. · <a href=\'ai-strategy.html\' style=\'color:var(--accent)\'>AI strategy →</a> · <a href=\'grok.html\' style=\'color:var(--accent)\'>xAI/Grok →</a> · <a href=\'finance.html#xai\' style=\'color:var(--accent)\'>xAI finances →</a>">本篇由马斯克商业志自动化迭代维护 · 每个节点都锚定第一手记录（账本/帖史存档/Series E 官方公告）· 中译为本站所译 · 非官方学习型网站 · 姊妹篇：<a href="ai-strategy.html" style="color:var(--accent)">AI 战略布局页（逻辑读法）</a> · <a href="grok.html" style="color:var(--accent)">xAI/Grok 专页</a> · <a href="finance.html#xai" style="color:var(--accent)">xAI 财务 →</a></p>'
s = s.replace(old_foot, new_foot)

old_toc = s[s.find('<aside class="lr-toc"'):s.find('</aside>') + 8]
new_toc = '''<aside class="lr-toc" aria-label="本篇目录">
      <div class="lr-toc-h" data-en="CONTENTS">目录 · CONTENTS</div>
    <a href="#deep-dive-06-s1" data-en="1. A one-line charter">一、一句话章程（2023.07.12）</a>
    <a href="#deep-dive-06-s2" data-en="2. Grok in four months">二、四个月出 Grok（2023.11）</a>
    <a href="#deep-dive-06-s3" data-en="3. Buying X">三、收购 X（2025.03）</a>
    <a href="#deep-dive-06-s4" data-en="4. The first report card">四、第一份成绩单（2026.02）</a>
    <a href="#deep-dive-06-s5" data-en="5. The capital line">五、资本线，以及没有档案的部分</a>
    </aside>'''
s = s.replace(old_toc, new_toc)

# ---------- 5) 断言 ----------
assert 'deep-dive-05' not in s.replace('deep-dive-05.html', ''), 'leftover dd05 section ids'
assert s.count('id="deep-dive-06-s') == 5
assert s.count('site-version-val') >= 1, 'version span missing'
for link in ['primary.html#e2023-07-12', 'x-posts.html#p2023-11-04', 'primary.html#e2026-02-10',
             'documents.html#d2026-01', 'events.html#e2023-11', 'x-posts.html#p2026-09-14',
             'primary.html#e2025-03-28']:
    assert link in s, 'interlink missing: ' + link
assert 'xAI 三年志' in s

io.open('deep-dive-06.html', 'w', encoding='utf-8', newline='\n').write(s)
print('OK: deep-dive-06.html written (%d bytes)' % len(s.encode('utf-8')))
