# -*- coding: utf-8 -*-
"""V10-15 N10：primary.html 插入 4 条 keynote 条目 + AI Day 2021 引语升级 + 索引断言 115→119。"""
import io

p = 'primary.html'
s = io.open(p, encoding='utf-8').read()
before = s.count('class="ps-row')
assert before == 119 or before == 115, before  # 115 条目+4 深读头？实测确认
print('ps-row 当前:', before)


def row(rid, date_disp, src, bg_en, bg_zh, quote_en, quote_zh, deed_en, deed_zh):
    return f'''        </li><li class="ps-row ps-deep reveal" id="{rid}">
          <div class="ps-head"><span class="ps-date"><a class="ps-date" href="#{rid}" title="定位到本条 · Permalink">{date_disp}</a></span><span class="ps-src">{src}</span></div>
          <div class="ps-sec"><h4 class="ps-label" data-en="Background">背景</h4>
            <p data-en="{bg_en}">{bg_zh}</p></div>
          <div class="ps-sec"><h4 class="ps-label" data-en="The words">原话</h4>
            <blockquote class="ps-quote">“{quote_en}”</blockquote>
            <p class="ps-zh">{quote_zh}</p></div>
          <div class="ps-sec"><h4 class="ps-label" data-en="Aftermath">后续</h4>
            <p data-en="{deed_en}">{deed_zh}</p></div>
        </li>'''


cards = []
# 1) e2024-06-13-2 股东会（同日 -2 惯例）——插在 e2024-06-13 卡之后
cards.append(row(
    'e2024-06-13-2', '2024.06.13',
    'Tesla 股东大会（elonmuskarchive.org 官方转写逐字）',
    'Same-day shareholder meeting after the Delaware vote: Musk frames the mission as hope plus acceleration, and calls FSD v12 &ldquo;profound&rdquo;.',
    '特拉华投票同日的股东大会上，马斯克把使命表述为「给人希望+加速这条路径」，并称 FSD v12「影响深远」。',
    'The goal is to give people hope that there is a path to a fully sustainable global economy. That we are on that path, that we are accelerating that path. Regarding FSD version 12, it&rsquo;s profound. The rate of improvement is rapid.',
    '目标是让人们相信：通往完全可持续的全球经济有一条路径，我们正在这条路上，而且在加速。至于 FSD v12——影响深远，进步速度飞快。',
    'Two days later the revised pay package was ratified at this meeting; the Delaware case continued separately.',
    '两天后，修订版薪酬方案在本场股东大会上获得批准；特拉华案件则另行继续。'))
# 2) e2025-05-29 Starship Update
cards.append(row(
    'e2025-05-29', '2025.05.29',
    'SpaceX Starship Update at Starbase（elonmuskarchive.org 官方转写逐字）',
    'At the newly incorporated Starbase Texas, he defines progress itself as a countdown to a self-sustaining Mars: about a million tons to the surface, so that civilization survives even if resupply ships from Earth stop coming.',
    '在正式建制的得州星基地（Starbase, Texas），他把「进步」本身定义为通往火星自给的倒计时：约一百万吨送达火星表面——即便地球补给船因任何原因停运，火星文明也能自己长大。',
    'Progress is measured by the timeline to establishing a self sustaining civilization on Mars. That&rsquo;s how we&rsquo;re gauging our progress here at Starbase. We need about a million tons to the surface of Mars so that Mars can continue to grow even if the supply ships from Earth stop coming for any reason.',
    '衡量进步的标尺，是建立火星自给文明的时间表——这就是我们在星基地评估进度的方式。我们需要把大约一百万吨送上火星表面，这样即使地球的补给船因任何原因停驶，火星也能继续生长。',
    'The million-ton target and the &ldquo;Mars self-sustaining&rdquo; test became the yardstick for every later Starship flight.',
    '「百万吨」目标与「火星自给」判据自此成为此后每一次星舰飞行的衡量标尺。'))
# 3) e2026-02-10 xAI All-Hands
cards.append(row(
    'e2026-02-10', '2026.02.10',
    'xAI All-Hands（elonmuskarchive.org 官方转写逐字）',
    'Two and a half years in, he sizes xAI against rivals five to twenty years older: number one in voice, image and video generation, plus Grokipedia positioned as an &ldquo;Encyclopedia Galactica&rdquo; beyond Wikipedia.',
    '成立两年半的 xAI 对标比它大五到二十岁的对手：语音、图像与视频生成第一，并把 Grokipedia 定位为超越维基百科的「银河百科全书」。',
    'xAI is only two and a half years old, basically a toddler, and we&rsquo;ve nonetheless achieved number one in many arenas — in voice, in image and video generation. Grokipedia is intended ultimately to be Encyclopedia Galactica, a distillation of all knowledge.',
    'xAI 才两岁半，基本是个幼儿，但我们已经在很多领域做到了第一——语音、图像与视频生成。Grokkipedia 的终极目标是成为「银河百科全书」——一切知识的蒸馏。',
    'The 100,000-H100 training cluster claim and the Galactica framing set the tone for the 2026 roadmap.',
    '「10 万张 H100 训练集群」的说法与「银河百科」的框架，为 2026 年的路线图定了调。'))
# 4) e2026-03-21 Terafab
cards.append(row(
    'e2026-03-21', '2026.03.21',
    'Terafab 发布会（elonmuskarchive.org 官方转写逐字）',
    'The chip-fab announcement opens not with specs but with Kardashev: Earth captures only a tiny fraction of the Sun&rsquo;s energy, and a terawatt of compute per year is merely one step on that scale.',
    '芯片工厂的发布不以参数开场，而是从卡尔达肖夫尺度讲起：地球只捕获了太阳能量的极小一部分，而每年 1 太瓦的算力只是该尺度上的一小步。',
    'This is the most epic chip building exercise in history by far. … A terafab, while it is enormous by our civilizational standards, is still just one step along the way — a combination of efforts of SpaceX, xAI and Tesla working together.',
    '这是迄今为止史上最宏大的芯片建造工程。……特法布（Terafab）以人类文明的尺度看固然庞大，但仍只是路上的一步——它是 SpaceX、xAI 与 Tesla 三家合力之作。',
    'The &ldquo;out of context problem&rdquo; phrasing — changing the context by orders of magnitude — became the project&rsquo;s slogan.',
    '「超纲问题」（out of context problem）——把参照系调高几个数量级——从此成为该项目的口号。'))

# AI Day 2021 升级：替换 e2021-08 引文块+ps-src+现场段
old_quote = '<blockquote class="ps-quote">“The Optimus robot will eventually be worth more than the car business, worth more than FSD.”</blockquote>'
assert old_quote in s
new_quote = '<blockquote class="ps-quote">“Tesla is arguably the world&rsquo;s biggest robotics company, because our cars are semi-sentient robots on wheels. … We think we&rsquo;ll probably have a prototype sometime next year. … At a mechanical level, you can run away from it and most likely overpower it.”</blockquote>'
s = s.replace(old_quote, new_quote, 1)
old_zh = '<p class="ps-zh">Optimus 机器人最终的价值将超过汽车业务，超过 FSD。</p>'
assert old_zh in s
new_zh = '<p class="ps-zh">Tesla 可以说是世界上最大的机器人公司——因为我们的车就是半感知的轮式机器人。……我们预计明年就能有原型机。……在机械层面，你可以跑赢它，多半也能徒手制住它。</p>'
s = s.replace(old_zh, new_zh, 1)
old_src = '<span class="ps-src">Tesla AI Day（CNBC · Reuters 报道，2022.09.30 复述）</span>'
assert old_src in s
new_src = '<span class="ps-src">Tesla AI Day 2021-08-19（elonmuskarchive.org 官方转写逐字；2026-10 复核升级，「worth more than」句为 2022.09.30 媒体口径）</span>'
s = s.replace(old_src, new_src, 1)
# 现场段补 2022 媒体口径句注记
old_ground = "and he repeated the claim: robots one day worth more than Tesla's car revenue."
assert old_ground in s
new_ground = 'and he repeated the claim (2022 AI Day, per CNBC/Reuters media caliber): the Optimus robot would eventually be worth more than the car business, worth more than FSD.'
s = s.replace(old_ground, new_ground, 1)

# 4 条新行插入：按时间序——e2024-06-13-2 在 e2024-06-13 卡后；e2025-05-29 在其后；e2026-02-10 与 e2026-03-21 在 e2025-09-01 文档后？primary 是账本（时间序）——找 e2026-07-22（最新账本条）前插
i_613 = s.find('id="e2024-06-13"')
end_613 = s.find('</li>', i_613) + len('</li>')
s = s[:end_613] + cards[0] + s[end_613:]
# e2025-05-29 / e2026-02-10 / e2026-03-21 / e2026-07-22 时间序：找 e2026-07-22 卡起点
i_722 = s.find('id="e2026-07-22"')
j_722 = s.rfind('</li>', 0, i_722) + len('</li>')
s = s[:j_722] + cards[1] + cards[2] + cards[3] + s[j_722:]

after = s.count('class="ps-row')
assert after == before + 4, (before, after)
for rid in ('e2024-06-13-2', 'e2025-05-29', 'e2026-02-10', 'e2026-03-21'):
    assert s.count(f'id="{rid}"') == 1, rid
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print(f'primary.html: {before} -> {after} ps-row; AI Day upgraded')

p2 = 'tools/build-search-index.py'
t = io.open(p2, encoding='utf-8').read()
old = "'言行实录': 115"
assert old in t
t = t.replace(old, "'言行实录': 119", 1)
io.open(p2, 'w', encoding='utf-8', newline='').write(t)
print('index assertion 115 -> 119')
