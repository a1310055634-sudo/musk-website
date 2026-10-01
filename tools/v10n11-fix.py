# -*- coding: utf-8 -*-
"""V10-15 N11 修正：删除错位的 i2019-02-19 与 i2021-09-28 两卡，按正确时间序重插。"""
import io

p = 'interviews.html'
s = io.open(p, encoding='utf-8').read()


def remove_card(s, cid):
    i = s.find(f'<article class="iv-item" id="{cid}">')
    assert i > 0, cid
    start = s.rfind('\n', 0, i) + 1  # 行首
    end = s.find('</article>', i) + len('</article>\n')
    return s[:start] + s[end:]


def insert_before(s, next_cid, block):
    i = s.find(f'<article class="iv-item" id="{next_cid}">')
    assert i > 0, next_cid
    start = s.rfind('\n', 0, i) + 1
    return s[:start] + block + s[start:]


def extract_card(s, cid):
    i = s.find(f'<article class="iv-item" id="{cid}">')
    assert i > 0, cid
    start = s.rfind('\n', 0, i) + 1
    end = s.find('</article>\n', i) + len('</article>\n')
    return s[start:end]


# 1) 删除错位两卡
s = remove_card(s, 'i2019-02-19')
s = remove_card(s, 'i2021-09-28')
assert s.count('class="iv-item"') == 46, s.count('class="iv-item"')

# 2) 重插（行首形态照抄锚行）
c19 = extract_card(s, 'i2019-02-19-placeholder') if False else None
# 从当前文件抽出两卡内容（先抽出再删？已删——从上次版本无法抽，重新构造与 integrate 相同文本）
# 直接重新构造（与 integrate.py 的 card() 输出一致）
c19 = '''    <article class="iv-item" id="i2019-02-19">
    <h2 data-en="&ldquo;Full self-driving this year, with certainty&rdquo;">「今年Feature Complete级自动驾驶，我确定」</h2>
    <div class="iv-meta"><span class="iv-badge" data-en="ARK Invest Podcast">ARK Invest Podcast</span><a class="iv-badge" href="#i2019-02-19" title="定位到本条 · Permalink">2019.02.19</a><span class="iv-badge">elonmuskarchive.org 官方转写（YouTube 源）</span></div>
    <p class="ctx" data-en="Asked about the Autopilot roadmap, he stakes a personal claim — he runs Autopilot engineering week by week — and promises feature-complete FSD within the year. ASR flat-cased; capitalization and punctuation added by editor.">被问到 Autopilot 路线图时，他押上个人背书——每周亲自过问 Autopilot 工程——并承诺年内达成 feature complete 级全自动驾驶。（语音转写为平文本，大小写与标点为编者所加。）</p>
    <blockquote>“…there’s feature complete full self-driving this year with certainty. This is something that we control and I managed Autopilot and engineering directly every week in detail, so I’m certain of this.”</blockquote>
    <p class="iv-zh">「……年内就会有 feature complete 级全自动驾驶，这一点我确定。这是我们自己可控的事，我每周都在细节层面直接管着 Autopilot 与工程，所以我很确定。」</p>
    <p class="after"><b>注/后续：</b>承诺对账：2019 年末只达成「city streets beta」的一部分，正式 FSD beta 于 2020-10 推送——承诺未按年兑现，已列入承诺对账页口径。保留池成员，2026-10-02 官方转写核验后立条。</p>
  </article>
'''
c21 = '''  <article class="iv-item" id="i2021-09-28">
    <h2 data-en="&ldquo;It&rsquo;d be just freaking cool&rdquo;">「就是觉得很酷，来吧」</h2>
    <div class="iv-meta"><span class="iv-badge" data-en="Code Conference 2021">Code Conference 2021</span><a class="iv-badge" href="#i2021-09-28" title="定位到本条 · Permalink">2021.09.28</a><span class="iv-badge">elonmuskarchive.org 官方转写（YouTube 源）</span></div>
    <p class="ctx" data-en="On why a Moon base matters, he skips the science case and leads with the honest one — it would be freaking cool, and humanity should represent. ASR flat-cased; capitalization and punctuation added by editor.">被问及月球基地的意义，他跳过科学论证先说大实话：就是觉得很酷，人类得去 represent。（语音转写为平文本，大小写与标点为编者所加。）</p>
    <blockquote>“I think it’d be just freaking cool. I mean, come on — humanity, let’s have a base on the moon.”</blockquote>
    <p class="iv-zh">「我觉得那就是他妈的很酷。来吧——人类，我们在月球上建个基地吧。」</p>
    <p class="after"><b>注/后续：</b>同场他也点评了 Branson 与 Bezos 的亚轨道飞行：「他们把钱花在推进太空事业上，这是好事——人类终归要做航天文明、要去群星之间。」保留池成员，2026-10-02 官方转写核验后立条。</p>
  </article>
'''

# 锚行真实形态：i2017-07-28 无缩进（197 行）、i2021-12 无缩进（403 行）——但那是删除前的行号；用 marker（无缩进）插入
s = insert_before(s, 'i2017-07-28', c19)
s = insert_before(s, 'i2021-12', c21)

assert s.count('class="iv-item"') == 48, s.count('class="iv-item"')
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('re-inserted; positions to verify via probe')
