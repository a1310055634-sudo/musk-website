# -*- coding: utf-8 -*-
"""V12 R05: 访谈消化轮——四场 2026 访谈立条（47→51），镜像详情页逐字锚。
插入锚=页尾 iv-foot 前插（N06 先例）；iv-item 六件套逐字克隆。
逐字源：elonmuskarchive.org/video/{id} 详情页（hasTranscript 全量库）。
"""
import io, re, sys

F = 'interviews.html'
s = io.open(F, encoding='utf-8').read()

def item(iid, title_en, title_zh, src_zh, src_en, date_disp, ctx_en, ctx_zh, quote, iv_zh, after_en, after_zh):
    return (f'<article class="iv-item" id="{iid}">\n'
            f'    <h2 data-en="{title_en}">{title_zh}</h2>\n'
            f'    <div class="iv-meta"><span class="iv-badge" data-en="{src_en}">{src_zh}</span><a class="iv-badge" href="#{iid}" title="定位到本条 · Permalink">{date_disp}</a></div>\n'
            f'    <p class="ctx" data-en="{ctx_en}">{ctx_zh}</p>\n'
            f'    <blockquote>{quote}</blockquote>\n'
            f'    <p class="iv-zh">{iv_zh}</p>\n'
            f'    <p class="after"><b data-en="Aftermath:">后续：</b><span data-en="{after_en}">{after_zh}</span></p>\n'
            f'  </article>\n')

C1 = item('i2026-01-06',
    'Grok keeps updating', '「Grok 一直在更新」——Grok 5 前夜的电路访谈',
    'MOONSHOTS #220 播客', 'Moonshots Podcast #220', '2026.01.06',
    'A long-form podcast at the start of 2026; asked about using AI for real engineering work, he says he has already done circuit design with it &#8220;just a couple weeks ago&#8221;.',
    '2026 年开年的长谈播客。被问到用 AI 干真正的工程活，他说自己几周前刚用它做过电路设计——然后顺势给 Grok 现场出了一道题。',
    '&#8220;I think probably at this point, Grok, if you took a photo and submitted it to Grok, it could probably tell you if a circuit is&#8230;if there&#8217;s something wrong with it. &#8230; Grok keeps updating.&#8221;',
    '「我觉得到这个阶段，Grok——你拍张照片提交给它，它大概就能告诉你这块电路是不是……是不是有问题。……Grok 一直在更新。」',
    'Same session confirms Grok 5 is on the way — the version ladder that X posts p2026-09-14 (4.8, 2.5T, C++ stack) made concrete. See <a href="grok.html" data-en="xAI &amp; Grok">xAI·Grok</a>.',
    '同场确认 Grok 5 在路上——这条版本阶梯后来由 X 帖 <a href="x-posts.html#p2026-09-14">p2026-09-14</a>（4.8/2.5T/C++ 栈）坐实。谱系见 <a href="grok.html" data-en="xAI &amp; Grok">xAI·Grok</a>。')

C2 = item('i2026-01-22',
    'The largest flying machine ever made', '「有史以来最大的飞行器」——达沃斯谈完全复用',
    '达沃斯现场对话（与 Larry Fink）', 'Davos, with Larry Fink', '2026.01.22',
    'On the Davos stage, BlackRock&#8217;s Larry Fink asks about Mars. He answers with Falcon 9 numbers first: 500+ reflights of the booster, while the expended upper stage costs as much as a small-to-medium jet — then the punchline about Starship.',
    '达沃斯舞台上，贝莱德的 Larry Fink 把话题抛向火星。他先报了一组 Falcon 9 数字：助推器复用超 500 次，而一次性烧毁的上面板成本相当于一架中小型公务机——然后才是关于星舰的正题。',
    '&#8220;With Starship, which is a giant rocket, it&#8217;s the largest flying machine ever made. &#8230;hopefully this year we should prove full reusability for Starship.&#8221;',
    '「而星舰——一枚巨型火箭，是有史以来最大的飞行器。……希望今年，我们就能证明星舰的完全可复用。」',
    'Full reusability is the cost-structure quantum leap behind every Mars line he has ever written. The rocket that stuck the landing: <a href="x-posts.html#p2024-10-13">p2024-10-13</a>.',
    '完全可复用是他所有火星叙事背后的成本结构质变。那枚接住了的火箭：<a href="x-posts.html#p2024-10-13">p2024-10-13</a>。')

C3 = item('i2026-02-05',
    'AI5 goes into Optimus', '「AI5 要进 Optimus」——边缘算力与电网错峰',
    'DWARKESH PODCAST 深度访谈', 'Dwarkesh Podcast', '2026.02.05',
    'Dwarkesh Patel presses the power problem: chip output grows exponentially while electricity output is flat. His answer flips the frame from data centers to edge compute.',
    'Dwarkesh Patel 逼问电力难题：芯片产出指数增长而电力输出是平的。他的回答把框架从数据中心整个翻到边缘侧。',
    '&#8220;For Tesla, the AI5 chip is going into our Optimus robot&#8230;if you have an AI Edge compute, that&#8217;s distributed power. The power is distributed over a large area, it&#8217;s not concentrated. And if you can charge at night, you can actually use the grid much more effectively.&#8221;',
    '「对 Tesla 来说，AI5 芯片要进的是我们的 Optimus 机器人……AI 边缘算力意味着分布式供电——电力摊在大片区域上，不集中。而如果能夜里充电，你对电网的利用效率会高得多。」',
    'Same session on SpaceX &#8220;generating incremental revenue on the way to Mars&#8221;: Falcon 9 was Starlink, Starship is orbital data centers. AI line in full: <a href="ai-strategy.html" data-en="AI Landscape">AI 战略全景</a>.',
    '同场回应 SpaceX「去火星沿途创收」：Falcon 9 时代是 Starlink，星舰时代是轨道数据中心。AI 线全景：<a href="ai-strategy.html" data-en="AI Landscape">AI 战略全景</a>。')

C4 = item('i2026-07-23',
    'Digital and physical intelligence', '「数字智能与物理智能」——十年后靠什么赚钱',
    'THE ECONOMIST 专访', 'The Economist', '2026.07.23',
    'The Economist notes that in the SpaceX IPO prospectus the overwhelming share of future revenue looked like it would come from AI, from Grok — not from transporting things to space — and asks what his companies will be doing in ten years.',
    'The Economist 点破一件怪事：SpaceX 招股书里未来收入的压倒性大头居然是 AI/Grok，而不是把东西运上天——并追问十年后他的公司们究竟靠什么赚钱。',
    '&#8220;You can really think of the economy as digital and physical intelligence. What we have right now advancing very rapidly is digital intelligence.&#8221;',
    '「你可以把整个经济理解为数字智能与物理智能两半。当下高速狂奔的，是数字智能这一半。」',
    'The two-half frame is his cleanest answer yet to &#8220;what is this company actually&#8221; — rockets are the physical half; Grok is the digital one. AI 战略深读：<a href="deep-dive-05.html" data-en="Deep Dive: AI Strategy">深读·AI 战略</a>。',
    '「两半论」是他迄今对「这公司到底是干嘛的」最干净的回答——火箭是物理那一半，Grok 是数字那一半。AI 战略深读：<a href="deep-dive-05.html" data-en="Deep Dive: AI Strategy">深读·AI 战略</a>。')

ANCHOR = '<p class="iv-foot"'
if s.count(ANCHOR) != 1:
    sys.exit('锚不唯一: %d' % s.count(ANCHOR))
NEW = C1 + C2 + C3 + C4 + '  ' + ANCHOR
s2 = s.replace(ANCHOR, NEW)

# ---- 断言 ----
n_items = len(re.findall(r'<article class="iv-item" id="', s2))
for iid in ['i2026-01-06', 'i2026-01-22', 'i2026-02-05', 'i2026-07-23']:
    if s2.count(f'id="{iid}"') != 1 or f'href="#{iid}"' not in s2:
        sys.exit(f'条目 {iid} 异常')
n_q = len(re.findall(r'<blockquote>', s2))
n_zh = len(re.findall(r'<p class="iv-zh">', s2))
assert n_items == 51, n_items
assert n_q == n_zh, (n_q, n_zh)

io.open(F, 'w', encoding='utf-8', newline='').write(s2)
print('四场集成 OK: iv-item=%d blockquote=%d iv-zh=%d' % (n_items, n_q, n_zh))
