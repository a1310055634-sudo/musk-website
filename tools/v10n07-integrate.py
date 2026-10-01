# -*- coding: utf-8 -*-
"""V10-15 N07：x-posts.html 插入 3 卡（时间序，年份分组锚点法）+ 索引断言 31→34。"""
import io
import re

p = 'x-posts.html'
s = io.open(p, encoding='utf-8').read()
before = s.count('<div class="tweet-card" id="p')
assert before == 31, f'tweet-card 计数: {before}'


def card(cid, date_disp, text, zh, note):
    return f'''    <div class="tweet-card" id="{cid}">
      <div class="tweet-top"><span class="tweet-avatar">M</span><span class="tweet-who"><b>Elon Musk</b><span>@elonmusk</span></span><a class="tweet-date" href="#{cid}" title="定位到本帖 · Permalink">{date_disp}</a></div>
      <p class="tweet-text">{text}</p>
      <p class="tweet-zh">{zh}</p>
      <p class="tweet-note"><b>背景/后续：</b>{note}</p>
    </div>
'''


# 1) p2018-08-14 插在 p2018-08-07 卡之后（2018 年份组内时间序：08-07 < 08-14，且 2019 年份条在 08-07 卡后）
anchor18 = '      <div class="xp-year" aria-hidden="true">2019</div>'
assert anchor18 in s
c18 = card(
    'p2018-08-14', '2018.08.14',
    '@Tesla I’m excited to work with Silver Lake and Goldman Sachs as financial advisors, plus Wachtell, Lipton, Rosen &amp; Katz and Munger, Tolles &amp; Olson as legal advisors, on the proposal to take Tesla private.',
    '@Tesla：我很高兴与银湖和高盛出任财务顾问、Wachtell, Lipton, Rosen &amp; Katz 与 Munger, Tolles &amp; Olson 出任法律顾问，共同推进把 Tesla 私有化的提案。',
    '私有化提案的顾问阵容官宣帖（<a href="#p2018-08-07">p2018-08-07</a>「funding secured」八天后）——与四大机构名单一并披露。此后 SEC 就马斯克推文展开调查，9 月末和解、马斯克卸任董事长；私有化提案最终搁置。镜像逐字存档 x-1029171381584314368；snowflake 解码与镜像日期一致。')
s = s.replace(anchor18, c18 + anchor18, 1)

# 2) p2019-03-14 与 p2019-05-25 插在 2019 年份条后（2019 组内时间序：03-14 < 05-25 < 11-21）
anchor19 = '      <div class="xp-year" aria-hidden="true">2019</div>\n'
i = s.find(anchor19, s.find('id="p2018-08-14"'))  # 在 2018 组后的 2019 条
assert i > 0
pos = i + len(anchor19)
c03 = card(
    'p2019-03-14', '2019.03.14',
    'S3XY https://t.co/3ECtKEL2BH',
    'S3XY（Sexy 谐音：Model S、3、X、Y 四车型字母拼合）。',
    'Model Y 发布日（加州 Hawthorne 设计中心发布会当晚）的命名梗帖——四车型字母恰好拼出「S3XY」。次日在评论区自曝「发布会其实藏了彩蛋但没人发现」。镜像逐字存档 x-1106063248581894144；snowflake 解码与镜像日期一致。')
c05 = card(
    'p2019-05-25', '2019.05.25',
    '@Erdayastronaut @SpaceX Super proud of SpaceX propulsion/test/materials team! One of hardest technology problems. New high temp superalloy &amp; internal foundry needed to make it work. Foundry iteration is how to get there fast. Big congrats to the whole team!',
    '@Erdayastronaut @SpaceX 为 SpaceX 推进/测试/材料团队感到无比自豪！这是最难的工程技术难题之一。为了让它成事，我们用了新的高温超合金和自建铸造厂。铸造厂快速迭代就是通往成功的路。向整个团队致以热烈祝贺！',
    'Starlink 首批 60 星（2019-05-24 发射）次日致团队帖：公开感谢推进/测试/材料三线，并披露关键工艺决策——新型高温超合金与自建内部铸造厂（Raptor 发动机量产路线的核心）。镜像逐字存档 x-1132429010514788352；snowflake 解码与镜像日期一致。')
s = s[:pos] + c03 + c05 + s[pos:]

after = s.count('<div class="tweet-card" id="p')
assert after == 34, after
assert s.count('id="p2018-08-14"') == 1 and s.count('id="p2019-03-14"') == 1 and s.count('id="p2019-05-25"') == 1
# 断言：每卡 tweet-zh==1、tweet-date href 唯一
for cid in ('p2018-08-14', 'p2019-03-14', 'p2019-05-25'):
    blk_start = s.find(f'id="{cid}"')
    blk_end = s.find('</div>', s.find('tweet-note', blk_start))
    blk = s[blk_start:blk_end]
    assert blk.count('tweet-zh') == 1, cid
    assert len(re.findall(f'<a class="tweet-date" href="#{cid}"', s)) == 1, cid

import re
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print(f'x-posts.html: {before} -> {after} tweet-card')

p2 = 'tools/build-search-index.py'
t = io.open(p2, encoding='utf-8').read()
old = "'X 帖': 31"
assert old in t
t = t.replace(old, "'X 帖': 34", 1)
io.open(p2, 'w', encoding='utf-8', newline='').write(t)
print('index assertion 31 -> 34')
