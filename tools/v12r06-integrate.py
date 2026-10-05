# -*- coding: utf-8 -*-
"""V12 R06：documents.html 新立 4 条 doc-article（email 库双源核验 I）。
锚前插：d2022-04-20 → ③b 前；d2022-11-09 → Extremely Hardcore 前；
d2023-01 + d2023-02 → ⑤ 2023 Part 3 前。带内建断言，失败即 exit 1 且不落盘。"""
import io, sys

PATH = 'documents.html'
s = io.open(PATH, encoding='utf-8').read()
orig = s

E2022_04_20 = '''  <!-- ③b2 2022.04.20 Ellison 十亿美元承诺（email 双源核验 I） -->
  <article class="doc-article" id="d2022-04-20">
    <h2>埃里森十亿美元承诺（马斯克 × 拉里·埃里森短信）</h2>
    <div class="doc-meta"><span class="doc-badge">私信 · Twitter v. Musk 法庭披露展品</span><a class="doc-badge" href="#d2022-04-20" title="定位到本文档 · Permalink">2022.04.20</a><span class="doc-badge">elonmuskarchive.org/email 底本 + SEC 2022-05-05 备案双源</span></div>
    <h4>原文摘录</h4>
    <blockquote>“Any interest in participating in the Twitter deal?” —— Elon Musk</blockquote>
    <p class="zh-line">有兴趣参与 Twitter 交易吗？——马斯克</p>
    <blockquote>“Yes … of course 👍” —— Larry Ellison</blockquote>
    <p class="zh-line">有……当然 👍——埃里森</p>
    <blockquote>“Roughly what dollar size? Not holding you to anything, but want to get a rough sense.” / “A billion … or whatever you recommend”</blockquote>
    <p class="zh-line">大概多大规模？不算数，只是想有个大致的感觉。——「10 亿……或者你说多少合适。」</p>
    <h4>本站注释</h4>
    <p class="note">整场收购里最省力的十亿美元：四行短信、一个 👍 敲定，不到一小时。埃里森（Oracle 联合创始人、Tesla 董事会同事）由此成为收购财团里最大的具名个人出资人——2022-05-05 马斯克以 SEC 修订备案公布 71.4 亿美元新增股权承诺，埃里森的 10 亿位列其中（Reuters/CNBC 当日报道）。短信原文经 Twitter v. Musk 诉讼披露（TIME/WaPo 逐字转载）。与言行实录 <a href="primary.html#e2022-04-20" style="color:var(--accent)">2022.04.20 条目</a>同源互证。口径：法庭披露件 + SEC 备案，双源 2026-10-06 核验。</p>
  </article>

'''

E2022_11_09 = '''  <!-- ③f2 2022.11.09 首封全员信（email 双源核验 I） -->
  <article class="doc-article" id="d2022-11-09">
    <h2>远程工作终结令（马斯克致 Twitter 全员第一封信）</h2>
    <div class="doc-meta"><span class="doc-badge">X 全员邮件</span><a class="doc-badge" href="#d2022-11-09" title="定位到本文档 · Permalink">2022.11.09</a><span class="doc-badge">elonmuskarchive.org/email 底本 + CNBC 全文双源</span></div>
    <h4>原文摘录</h4>
    <blockquote>“Remote work is no longer allowed, unless you have a specific exception. […] Starting tomorrow (Thursday), everyone is required to be in the office for a minimum of 40 hours per week. […]” —— 落款 “Thanks, Elon”</blockquote>
    <p class="zh-line">远程工作不再被允许，除非你获得特别例外。……从明天（周四）起，每个人都必须在办公室每周至少待满 40 小时。……——落款：谢谢，埃隆</p>
    <h4>本站注释</h4>
    <p class="note">交割（<a href="#d2022-10-27" style="color:var(--accent)">d2022-10-27</a>）后第十三天，第一封全员信定调两件事：远程工作终结，以及他对全员的直白警告——公司若无订阅收入便难以存续，经济环境「异常艰难」。CNBC 次日获全文刊发，一周后的「极其硬核」通牒（<a href="#d2022-11-16" style="color:var(--accent)">d2022-11-16</a>）正是这封信的延长线：先收回远程，再收回归属。口径：媒体获得（CNBC 全文）+ 镜像底本，双源 2026-10-06 核验。</p>
  </article>

'''

E2023_PAIR = '''  <!-- ⑤2 2023 OpenAI 短信两件（email 双源核验 I） -->
  <article class="doc-article" id="d2023-01">
    <h2>“This is a bait and switch”（马斯克致奥特曼短信）</h2>
    <div class="doc-meta"><span class="doc-badge">私信 · 庭审追述件（Musk v. OpenAI）</span><a class="doc-badge" href="#d2023-01" title="定位到本文档 · Permalink">2023.01</a><span class="doc-badge">elonmuskarchive.org/email 底本 + 2026 庭审证据双源</span></div>
    <h4>原文摘录</h4>
    <blockquote>“What the hell is going on? This is a bait and switch.”</blockquote>
    <p class="zh-line">到底在搞什么名堂？这是一次诱饵调包。</p>
    <h4>本站注释</h4>
    <p class="note">口径须先说明：这封短信的原始文本并未单独公开，此句出自马斯克 2026 年庭审宣誓作证的当场追述（2026-04-29 第二日作证，短信截图作为证据呈交陪审团；Business Insider/NYT/CNBC 均逐字报道）。时点在微软确认对 OpenAI 追加 100 亿美元投资前后——马斯克称此举背叛了非营利初心，并称之为自己对奥特曼「失去信任的时刻」；庭审展品显示奥特曼曾回「我也觉得这很糟」（“I agree this feels bad”）并提出让他参股，被马斯克一方指为安抚。这封短信与 <a href="#d2023-02" style="color:var(--accent)">d2023-02</a> 同属 2023 年初公开决裂的私下半场。口径：庭审证词追述，镜像如实标注（2026-10-06 核验）。</p>
  </article>

  <article class="doc-article" id="d2023-02">
    <h2>“You’re my hero … it really fucking hurts”（奥特曼致马斯克短信）</h2>
    <div class="doc-meta"><span class="doc-badge">私信 · Musk v. OpenAI 解封展品（2026）</span><a class="doc-badge" href="#d2023-02" title="定位到本文档 · Permalink">2023.02</a><span class="doc-badge">elonmuskarchive.org/email 底本 + Business Insider 引用双源</span></div>
    <h4>原文摘录</h4>
    <blockquote>“You’re my hero and that’s what it feels like when you attack openai … it really fucking hurts when you publicly attack openai.” —— Sam Altman</blockquote>
    <p class="zh-line">你是我的英雄——你攻击 OpenAI 时就是这种感觉……你公开攻击 OpenAI 真的很伤人。——奥特曼</p>
    <blockquote>“The fate of civilization is at stake.” —— Elon Musk</blockquote>
    <p class="zh-line">这是关乎文明存亡的事。——马斯克</p>
    <h4>本站注释</h4>
    <p class="note">2026 年 1 月庭审前解封文件曝光的这一来一回，是两人决裂最私人的一帧：马斯克公开炮轰 OpenAI 期间，奥特曼发去这条混杂崇敬与委屈的短信；马斯克的回复把赌注直接抬到文明高度（Business Insider 引用的解封版本更长——他在「文明」半句前还道了歉：「我听到了，伤害你不是我的本意，为此我道歉；但文明的存续系于此」）。据 WaPo，奥特曼同场还保证不会挖 Tesla 员工「伤害」Tesla。这批解封文件随后成为庭审主线之一。口径：法庭解封展品 + 媒体逐字引用，双源 2026-10-06 核验。</p>
  </article>

'''

ANCHORS = [
    ('  <!-- ③b 2022 Merger Agreement -->', E2022_04_20, ['d2022-04-20']),
    ('  <!-- ③ 2022 Extremely Hardcore -->', E2022_11_09, ['d2022-11-09']),
    ('  <!-- ⑤ 2023 Part 3 -->', E2023_PAIR, ['d2023-01', 'd2023-02']),
]

# 前置断言：锚唯一、新 id 不存在、基线 27 条
before_count = s.count('<article class="doc-article')
assert before_count == 27, 'baseline doc-article count %d != 27' % before_count
for anchor, block, ids in ANCHORS:
    assert s.count(anchor) == 1, 'anchor not unique: %r (%d)' % (anchor, s.count(anchor))
    for i in ids:
        assert s.count('id="%s"' % i) == 0, 'id already exists: %s' % i

for anchor, block, ids in ANCHORS:
    s = s.replace(anchor, block + anchor, 1)

# 后置断言
after_count = s.count('<article class="doc-article')
assert after_count == 31, 'after count %d != 31' % after_count
for anchor, block, ids in ANCHORS:
    for i in ids:
        assert s.count('id="%s"' % i) == 1, 'article id count != 1: %s' % i
        assert s.count('href="#%s" title=' % i) == 1, 'permalink count != 1: %s' % i
assert 'primary.html#e2022-04-20' in s, 'cross-link to ledger missing'
assert s.count('2026-10-06 核验') == 4, 'verification stamps != 4'
assert s == orig or len(s) > len(orig)

io.open(PATH, 'w', encoding='utf-8', newline='\n').write(s)
print('OK: 4 doc-articles inserted, %d -> %d' % (before_count, after_count))
