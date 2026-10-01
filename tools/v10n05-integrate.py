# -*- coding: utf-8 -*-
"""V10-15 N05：interviews.html 插入 i2008-08-05（Wired 逐字稿）+ 索引断言 42→43。"""
import io
import re
import sys

p = 'interviews.html'
s = io.open(p, encoding='utf-8').read()

before = s.count('<article class="iv-item"')
assert before == 43  # 43 标签 = 42 入索引 + 1 legacy 无 id 条目, f'iv-item 计数异常: {before}'

anchor = '  <!-- 2008 第四发 -->'
assert anchor in s, 'anchor missing'

card = '''  <!-- 2008 三连败后 Wired 专访 -->
  <article class="iv-item" id="i2008-08-05">
    <h2 data-en="&ldquo;Optimism, pessimism, fuck that; we&rsquo;re going to make it happen.&rdquo;">「乐观悲观，滚他妈的；我们会让它发生」</h2>
    <div class="iv-meta"><span class="iv-badge" data-en="Wired.com phone interview (Carl Hoffman)">Wired.com 电话专访（Carl Hoffman）</span><a class="iv-badge" href="#i2008-08-05" title="定位到本条 · Permalink">2008.08.05</a><span class="iv-badge">elonmuskarchive.org 官方转写 · Wired.com 逐字存档</span></div>
    <p class="ctx" data-en="Falcon 1 has failed three times in a row. Five weeks before the fourth launch — the make-or-break shot with the company&rsquo;s last money — he gives Wired the rawest interview of the year: owning the &ldquo;zero for three&rdquo; record, confirming the Founder&rsquo;s Fund bridge investment, and correcting his own famous line about having money for just three flights.">Falcon 1 已三连败。距离第四次发射——押上公司最后资金、不成则亡的那一炮——还有五周，他接受了 Wired 全年最生猛的一次专访：直面「零比三」战绩、确认 Founder's Fund 的过桥投资，并修正了自己那句著名的「钱只够烧三次」。</p>
    <blockquote>&ldquo;Optimism, pessimism, fuck that; we're going to make it happen. As God is my bloody witness, I'm hell-bent on making it work.&rdquo; &mdash; &ldquo;That was the dumbest thing I've ever said.&rdquo; &mdash; &ldquo;Patience is a virtue, and I'm learning patience. It's a tough lesson.&rdquo;</blockquote>
    <p class="iv-zh">「乐观也好，悲观也罢，滚他妈的；我们会让它发生。上帝作我的血证，我铁了心要让它成事。」——「那是我说过的最蠢的话。」——「耐心是一种美德，我正在学。这一课很疼。」</p>
    <p class="after"><b>注/后续：</b>「最蠢的话」指他早年「钱只够三次发射」的言论——他当场修正：三败后客户未弃、在手 12 发任务，没有理由放弃。专访同时确认 Founder's Fund（PayPal 旧部）注资到位。五周后第四次发射入轨，见 <a href="#i2008-09-28">i2008-09-28</a>；全程资金脉络见专题 <a href="survival-2008.html">survival-2008</a>。逐字稿存档 qa/v10-15/round-05/sources/。</p>
  </article>

'''
s = s.replace(anchor, card + anchor, 1)
after = s.count('<article class="iv-item"')
assert after == 44, after
# 结构自检
for token in ['id="i2008-08-05"', 'iv-meta', 'class="ctx"', '<blockquote>', 'iv-zh', 'class="after"']:
    assert token in card
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print(f'interviews.html: {before} -> {after} iv-item, i2008-08-05 inserted')

# 索引断言 42 -> 43
p2 = 'tools/build-search-index.py'
t = io.open(p2, encoding='utf-8').read()
old = "'访谈与表态': 42"
assert old in t
t = t.replace(old, "'访谈与表态': 43", 1)
io.open(p2, 'w', encoding='utf-8', newline='').write(t)
print('index assertion 42 -> 43')
