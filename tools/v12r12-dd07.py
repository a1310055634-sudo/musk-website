# -*- coding: utf-8 -*-
"""V12 R12：生成 deep-dive-07.html《Robotaxi 落地考》——克隆 deep-dive-05 骨架，只换内容。
择题依据：Robotaxi 素材（账本逐字×2+R02 四卡+事件档）较政治主题更扎实；政治主题连同已探明素材写 EXPANSION 候选池。"""
import io, re

src = io.open('deep-dive-05.html', encoding='utf-8').read()

s = src.replace('<title>深读 · 马斯克的 AI 战略布局 — 马斯克商业志 MUSK, INC.</title>',
                '<title>深读 · Robotaxi 落地考 — 马斯克商业志 MUSK, INC.</title>')
s = s.replace('<meta name="description" content="从 OpenAI 捐资者到 AI 独立竞争者：动机链、三位一体与治理新变量——AI 战略的逻辑深读。" />',
              '<meta name="description" content="八年欠账与一年运营：Robotaxi 从承诺到奥斯汀发车——指控、回应与本站核查三段体。" />')
s = s.replace('<meta property="og:title" content="深读 · 马斯克的 AI 战略布局 — 马斯克商业志 MUSK, INC." />',
              '<meta property="og:title" content="深读 · Robotaxi 落地考 — 马斯克商业志 MUSK, INC." />')
s = s.replace('<div class="lr-kick">DEEP DIVE 05 · AI STRATEGY</div>',
              '<div class="lr-kick">DEEP DIVE 07 · ROBOTAXI AUDIT</div>')
s = s.replace('<h1 data-en="His AI Strategy, Read as Logic">马斯克的 AI 战略布局</h1>',
              '<h1 data-en="Robotaxi, Audited">Robotaxi 落地考</h1>')
s = s.replace('<p class="lr-lead" data-en="OpenAI co-founder (2015) → exit (2018) → xAI (2023) → buying X (2025): this piece reads the strategy as logic — motive, the data×distribution×capital trinity, and the new governance variable. For the full timeline see the AI strategy page." style="font-family:Georgia,\'STSong\',serif">2015 OpenAI 联合创始 → 2018 退出 → 2023 xAI → 2025 收购 X：本篇把这段历程当作「逻辑」来读——动机链、数据×分发×资本的三位一体、以及治理新变量。完整时间线见 <a href="ai-strategy.html" style="color:var(--accent)">AI 战略布局页</a>，两页互为表里。</p>',
              '<p class="lr-lead" data-en="Eight years of slipped promises (2016 → 2024), then one year of real operations (Austin 2025.06 →): this piece audits both halves — the missed dates and the running service — in the site\'s charges/response/verification format. Every claim anchors to a first-hand record." style="font-family:Georgia,\'STSong\',serif">八年的跳票承诺（2016 → 2024），之后一年的真实运营（2025.06 奥斯汀 →）：本篇把两半都查一遍——欠掉的日期与跑起来的服务——用「指控/回应/本站核查」三段体。每一句都有第一手记录可回溯。</p>')
s = s.replace('<b data-en="≈ 900 chars">约 900 字</b>', '<b data-en="≈ 1,000 chars">约 1,000 字</b>')
s = s.replace('<b>v6.10.0 · 2026-09-29</b>', '<b>v<span class="site-version-val">11.12.0</span> · 2026-10-07</b>')
s = s.replace('<figcaption data-en="The Twitter HQ sign, November 2022 — two and a half years later the company was absorbed by xAI. Photo: osunpokeh / CC BY-SA 4.0, via Wikimedia Commons">2022 年 11 月的 Twitter 总部标牌——两年半后，这家公司被 xAI 反向吸收。</figcaption>',
              '<figcaption data-en="The Twitter HQ sign, November 2022 — the same man promised self-driving coast-to-coast in 2016, and shipped a paid robotaxi city service in 2025. Photo: osunpokeh / CC BY-SA 4.0, via Wikimedia Commons">2022 年 11 月的 Twitter 总部标牌——同一个人，2016 年承诺全自动驾驶横穿美国，2025 年发出了付费城市 Robotaxi 服务。</figcaption>')

def sec(n, new):
    global s
    pat = re.compile(r'<section class="lr-sec">\s*<h2[^>]*id="deep-dive-05-s' + str(n) + r'".*?</section>', re.S)
    m = pat.search(s)
    assert m, 'section %d not found' % n
    s = s[:m.start()] + new + s[m.end():]

sec(1, '''<section class="lr-sec">
    <h2 data-en="1. The shape of the debt" id="deep-dive-07-s1">一、欠账的形状（2016–2024）</h2>
    <p data-en="The promise cluster: a coast-to-coast autonomous drive “by the end of 2017” (announced 2016), and “a million robotaxis” by 2020 (Autonomy Day, 2019). Neither happened on any date he gave — and the site's promise-ledger deliberately keeps no robotaxi case: the five standing cases all carry checkable deadlines, and the robotaxi cluster kept moving theirs. The shape of the debt is not one broken date; it is a moving target.">承诺簇：2016 年宣布的「2017 年底前」全自主横穿美国，与 2019 年 Autonomy Day 的「2020 年百万台 robotaxi」。两个日期都没有兑现——而本站的承诺账（<a href="promises.html#promises-s3">promises 五案</a>）刻意不设 robotaxi 案：五案都有可判的日期下限，robotaxi 簇的日期一直在移动。欠账的形状不是某个跳票的日期，而是一个不断移动的靶子。</p>
    <p class="lr-note"><b data-en="Editor's note">编者注</b><span data-en="The 2016/2019 promise wording lives in public appearances rather than any verbatim archive this site holds, so those two quotes stay out of the ledger — same discipline as before. The event-archive entry records the debt narrative without quoting it.">2016/2019 两代承诺的原话出自公开活动而非本站持有的逐字档，故不入账本引语（同一纪律）。事件档案 <a href="events.html#e2025-06-22">e2025-06-22</a> 记录了欠账叙事本身。</span></p>
  </section>''')

sec(2, '''<section class="lr-sec">
    <h2 data-en="2. We, Robot" id="deep-dive-07-s2">二、We,Robot（2024.10.10）</h2>
    <p data-en="On a movie-studio lot in Los Angeles he unveiled Cybercab — the first car built specifically for unsupervised full self driving (<a href='primary.html#e2024-10-10'>ledger</a>):">在洛杉矶一个电影制片厂，他发布了 Cybercab——第一辆为无监督全自动驾驶专门打造的车（<a href="primary.html#e2024-10-10">账本</a>）：</p>
    <blockquote>“Cybercab: The Autonomous Robotaxi. And then we've got the first car that is specifically built for unsupervised full self driving to be a robotaxi.”
      <p class="lr-quote-zh">「Cybercab：自动驾驶 Robotaxi。这是第一辆为无监督全自动驾驶专门打造的车，它将成为 robotaxi。」（<a href="primary.html#e2024-10-10">账本逐字</a>）</p>
    </blockquote>
    <p class="lr-note"><b data-en="Editor's note">编者注</b><span data-en="Note the verb tense shift: for eight years the promise was about owners' cars earning money; Cybercab is a purpose-built fleet vehicle — the promise quietly changed shape. (Editorial analysis, not his words.)">注意动词时态的变化：八年来的承诺是「车主的车自己赚钱」；Cybercab 是专门打造的车队车辆——承诺悄悄换了形状。（编者分析，非其原话。）</span></p>
  </section>''')

sec(3, '''<section class="lr-sec">
    <h2 data-en="3. The Austin arc" id="deep-dive-07-s3">三、奥斯汀弧线（2025.06–2026.10）</h2>
    <p data-en="Paid service started in Austin in June 2025 (<a href='events.html#e2025-06-22'>event archive</a>), then the arc ran through four archived posts: service area past rivals (<a href='x-posts.html#p2025-08-16'>2025.08.16</a>), greater-Austin coverage (<a href='x-posts.html#p2025-10-29'>2025.10.29</a>), no in-car safety monitor (<a href='x-posts.html#p2026-01-22'>2026.01.22</a>), and late-night hours (<a href='x-posts.html#p2026-10-03'>2026.10.03</a>).">付费服务 2025 年 6 月在奥斯汀开跑（<a href="events.html#e2025-06-22">事件档案</a>），随后一年是一条四帖弧线：服务面积超对手（<a href="x-posts.html#p2025-08-16">2025.08.16</a>）→ 大奥斯汀全区（<a href="x-posts.html#p2025-10-29">2025.10.29</a>）→ 车内无安全监督员（<a href="x-posts.html#p2026-01-22">2026.01.22</a>）→ 延时至深夜（<a href="x-posts.html#p2026-10-03">2026.10.03</a>）。</p>
    <blockquote>“Just started Tesla Robotaxi drives in Austin with no safety monitor in the car.”
      <p class="lr-quote-zh">「Tesla 的 Robotaxi 刚刚在奥斯汀开始了车内无安全监督员的行驶。」（<a href="x-posts.html#p2026-01-22">帖史逐字</a>）</p>
    </blockquote>
  </section>''')

sec(4, '''<section class="lr-sec">
    <h2 data-en="4. One year in" id="deep-dive-07-s4">四、一周年口径（2026.07.22）</h2>
    <p data-en="A year into paid service, the earnings-call ledger entry reads: the questions had shifted from “whether” to “how fast” (<a href='primary.html#e2026-07-22'>ledger</a>). The same call pivoted to Optimus — “I think Optimus will be the biggest product ever” — a reminder that robotaxi is now one track in a larger autonomy story.">付费服务一年后，财报电话会账本条写着：问题已从「是否」变成「多快」（<a href="primary.html#e2026-07-22">账本</a>）。同一场电话会已把重心抛向 Optimus——「我认为 Optimus 将是有史以来最大的产品」——Robotaxi 如今只是更大自动驾驶叙事里的一条轨道。</p>
    <p class="lr-note"><b data-en="Checkable parameters">可核参数</b><span data-en="Geofence, monitors, hours and fares are all checkable — the debt was promises without dates; the service is operations with numbers. Whatever one believes, the two halves are now on different evidentiary footing.">地理围栏、监督员、时段与收费都可核——欠账是没有日期的承诺，服务是带数字的运营。无论立场如何，两半的证据地基已经不同。</span></p>
  </section>''')

sec(5, '''<section class="lr-sec">
    <h2 data-en="5. Charges, response, verification" id="deep-dive-07-s5">五、指控、回应与本站核查</h2>
    <p class="lr-note"><b data-en="The charges">指控</b><span data-en="Critics and short-sellers argue the robotaxi record is a decade of missed deadlines used to raise capital on autonomy narratives — 2016, 2019, and the FSD pricing history all predate a single paid driverless mile.">批评者与做空方认为：robotaxi 记录是十年跳票，被用来在自动驾驶叙事上融资——2016、2019 与 FSD 收费史都早于第一个付费无人里程。</span></p>
    <p class="lr-note"><b data-en="The response">回应</b><span data-en="His side's record: the service is live, expanding, and dropped its in-car monitors within seven months of launch — slower than promised, but real; and the Cybercab platform was built for exactly this.">他一方的记录：服务在跑、在扩张、发车七个月内撤掉了车内监督员——比承诺慢，但是真的；Cybercab 平台正是为此打造。</span></p>
    <p class="lr-note"><b data-en="This site's verification">本站核查</b><span data-en="Both halves are true and separately checkable: the missed dates (no verbatim archive, hence no ledger quote) and the running service (four archived posts, one earnings-call entry, one event file). The promise-ledger's five-case format excludes robotaxi precisely because its dates kept moving — see <a href='promises.html#promises-s3'>promises</a>. The audit stays open; the next checkable node is the fleet-size and city-count numbers on future earnings calls.">两半都真、分别可核：跳票的日期（无逐字档故不入账本引语）与跑起来的服务（四张存档帖+一条财报会账本+一份事件档案）。承诺账的五案制不收 robotaxi，恰因其日期一直移动——见 <a href="promises.html#promises-s3">promises</a>。本考保持开放；下一个可核节点是未来财报会上的车队规模与城市数。</span></p>
  </section>''')

s = s.replace('DEEP DIVE 05', 'DEEP DIVE 07')
old_foot_i = s.find('<p class="lr-foot"')
old_foot = s[old_foot_i:s.find('</p>', old_foot_i) + 4]
new_foot = '<p class="lr-foot" data-en="Maintained by the MUSK, INC. automation. Every claim anchors to a first-hand record (ledger entries, archived posts, the event file). Chinese translations are this site\'s own. Companion pieces: the event archive and the promise ledger. · <a href=\'events.html#e2025-06-22\' style=\'color:var(--accent)\'>Robotaxi event file →</a> · <a href=\'promises.html\' style=\'color:var(--accent)\'>Promise ledger →</a> · <a href=\'x-posts.html\' style=\'color:var(--accent)\'>X posts →</a>">本篇由马斯克商业志自动化迭代维护 · 每句都有第一手记录可回溯（账本/帖史存档/事件档案）· 中译为本站所译 · 非官方学习型网站 · 姊妹篇：<a href="events.html#e2025-06-22" style="color:var(--accent)">Robotaxi 事件档案 →</a> · <a href="promises.html" style="color:var(--accent)">承诺账 →</a> · <a href="x-posts.html" style="color:var(--accent)">X 帖史 →</a></p>'
s = s.replace(old_foot, new_foot)

old_toc = s[s.find('<aside class="lr-toc"'):s.find('</aside>') + 8]
new_toc = '''<aside class="lr-toc" aria-label="本篇目录">
      <div class="lr-toc-h" data-en="CONTENTS">目录 · CONTENTS</div>
    <a href="#deep-dive-07-s1" data-en="1. The shape of the debt">一、欠账的形状（2016–2024）</a>
    <a href="#deep-dive-07-s2" data-en="2. We, Robot">二、We,Robot（2024.10.10）</a>
    <a href="#deep-dive-07-s3" data-en="3. The Austin arc">三、奥斯汀弧线（2025.06–2026.10）</a>
    <a href="#deep-dive-07-s4" data-en="4. One year in">四、一周年口径（2026.07.22）</a>
    <a href="#deep-dive-07-s5" data-en="5. Charges, response, verification">五、指控、回应与本站核查</a>
    </aside>'''
s = s.replace(old_toc, new_toc)

assert 'deep-dive-05' not in s.replace('deep-dive-05.html', '')
assert s.count('id="deep-dive-07-s') == 5
assert s.count('site-version-val') >= 1
for link in ['primary.html#e2024-10-10', 'primary.html#e2026-07-22', 'x-posts.html#p2026-01-22',
             'x-posts.html#p2025-08-16', 'events.html#e2025-06-22', 'promises.html#promises-s3']:
    assert link in s, 'interlink missing: ' + link
assert 'Robotaxi 落地考' in s

io.open('deep-dive-07.html', 'w', encoding='utf-8', newline='\n').write(s)
print('OK: deep-dive-07.html written (%d bytes)' % len(s.encode('utf-8')))
