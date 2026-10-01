# -*- coding: utf-8 -*-
"""V10-15 N08：documents.html 插入 4 封诉讼证物信（时间序）+ 索引断言 19→23。"""
import io

p = 'documents.html'
s = io.open(p, encoding='utf-8').read()
before = s.count('class="doc-article"')
assert before == 19, before


def doc(did, title, badge1, date_disp, badge3, blocks, note):
    bl = ''
    for h4, en, zh in blocks:
        bl += (f'    <h4>{h4}</h4>\n'
               f'    <blockquote>“{en}”</blockquote>\n'
               f'    <p class="zh-line">{zh}</p>\n')
    return f'''  <article class="doc-article" id="{did}">
    <h2>{title}</h2>
    <div class="doc-meta"><span class="doc-badge">{badge1}</span><a class="doc-badge" href="#{did}" title="定位到本文档 · Permalink">{date_disp}</a><span class="doc-badge">{badge3}</span></div>
{bl}    <p class="doc-note">{note}</p>
  </article>

'''


cards = ''
# —— d2015-11-22（时间序最早，插在 d2016-07-20 前）——
cards += doc(
    'd2015-11-22', 'OpenAI 创立期邮件（$1B 承诺 · 马斯克致 Brockman）',
    '邮件存档 · OpenAI 诉讼证物（Musk v. Altman 法庭公开文件）', '2015.11.22',
    'elonmuskarchive.org/email 底本 + muskvsaltman.com 法庭文件存档双源',
    [
        ('原文摘录 · 公告口径',
         'I think we should say that we are starting with a $1B funding commitment. This is real. I will cover whatever anyone else doesn’t provide.',
         '我认为我们应该对外宣布：我们是以 10 亿美元的资助承诺起步的。这是真的。别人没出的部分我来补齐。'),
        ('原文摘录 · 为什么必须比 1 亿大',
         'We need to go with a much bigger number than $100M … to avoid sounding hopeless relative to Google and Facebook.',
         '我们需要一个比 1 亿美元大得多的数字……免得跟谷歌和 Facebook 摆在一起听起来毫无希望。'),
    ],
    'OpenAI 创立期关键证物：公开宣布的「10 亿承诺」出自马斯克本人起草口径（他承诺兜底差额），2024 年 Musk v. Altman 诉讼中被 OpenAI 作为反驳证据公开。双源：镜像底本（elonmuskarchive.org/email）+ muskvsaltman.com 法庭文件存档（2026-10-02 核验逐字吻合）。口径：诉讼证物/法庭公开文件。')
# —— d2017-09-13 ——
cards += doc(
    'd2017-09-13', 'OpenAI 控制权邮件（马斯克致联合创始人）',
    '邮件存档 · OpenAI 诉讼证物（OpenAI 2024-12 官方公开）', '2017.09.13',
    'elonmuskarchive.org/email 底本 + OpenAI 官方博客公开文件双源',
    [
        ('原文摘录',
         'I would unequivocally have initial control of the company, but this will change quickly.',
         '我会毫无保留地拥有公司的初始控制权，但这会很快改变。'),
    ],
    '2017 年 9 月营利化谈判中马斯克对 OpenAI 联合创始人提出的控制权条款：初始控制+董事会任命权。2024 年 12 月 OpenAI 以官方博客「Elon Musk wanted an OpenAI for-profit」公开此邮件（Washington Post 同步报道），成为双方诉讼的核心证物之一。双源：镜像底本 + OpenAI 官方公开文件（2026-10-02 核验逐字吻合，含「but this will change quickly」后缀）。口径：诉讼证物。')
# —— d2017-09-21 ——
cards += doc(
    'd2017-09-21', 'OpenAI「最后一根稻草」邮件（马斯克宣布停止资助）',
    '邮件存档 · OpenAI 诉讼证物（法院判决引用件）', '2017.09.21',
    'elonmuskarchive.org/email 底本 + techemails.com 存档 + FindLaw 判决引用三源',
    [
        ('原文摘录',
         'Guys, I’ve had enough. This is the final straw. Either go do something on your own or continue with OpenAI as a nonprofit. I will no longer fund OpenAI until you have either made a firm commitment to stay nonprofit, or you’re going to do something else in terms of structure.',
         '各位，我受够了。这是最后一根稻草。要么你们自己单干，要么继续把 OpenAI 当非营利组织做下去。在你们要么坚定承诺保持非营利、要么拿出别的架构方案之前，我不会再资助 OpenAI。'),
    ],
    '「Honest Thoughts」邮件发出九分钟后，马斯克终结营利化谈判并宣布停止资助（2018-02 退出董事会）。此邮件成为 Musk v. Altman 诉讼关键证物——2026 年联邦法院判决书原文引用（FindLaw 在档）。三源：镜像底本 + techemails.com 邮件存档 + 法院判决引用（2026-10-02 核验逐字吻合）。口径：诉讼证物。')
# —— d2022-04-09 ——
cards += doc(
    'd2022-04-09', '马斯克致 Agrawal 短信（「你这周做成了什么？」）',
    '短信存档 · Twitter v. Musk 诉讼证物（Delaware 衡平法院解封文件）', '2022.04.09',
    'elonmuskarchive.org/email 底本 + BBC/Business Insider 法庭文件报道双源',
    [
        ('原文摘录 · 马斯克三连回复',
         'What did you get done this week? … I’m not joining the board. This is a waste of time. Will make an offer to take Twitter private.',
         '你这周做成了什么？……我不会加入董事会。这是浪费时间。我会发要约把 Twitter 私有化。'),
    ],
    'Agrawal 就「Twitter 正在死亡」推文劝马斯克克制后不到两分钟，马斯克回以三连短信——公开宣布放弃董事会席位并预示全面收购要约（4 月 14 日正式发起）。2022 年 9 月 Delaware 衡平法院诉讼解封的短信证物之一，BBC/Business Insider 等逐字引用。双源：镜像底本（elonmuskarchive.org/email）+ 法庭文件媒体报道逐字核对（2026-10-02）。口径：诉讼证物。')

# 插入锚：按时间序分布——d2015-11-22 在最前（d2006-08 后）；d2017-09-13/21 在 d2016-10-12 与 d2018-08-07 之间；d2022-04-09 在 d2022-02-07 与 d2022-04-11 之间
i6 = s.find('id="d2016-10-12')
j = s.rfind('  <!--', 0, i6)
# d2015 在 d2016-10-12 注释前插
s = s[:j] + cards.split('  <article class="doc-article" id="d2015-11-22">')[0].replace('', '') and s
# 简化：分别精确插入
c15_start = cards.find('  <article class="doc-article" id="d2015-11-22">')
c15_end = cards.find('  <article class="doc-article" id="d2017-09-13">')
c15 = cards[c15_start:c15_end]
c17a_start = cards.find('  <article class="doc-article" id="d2017-09-13">')
c17b_start = cards.find('  <article class="doc-article" id="d2017-09-21">')
c17a = cards[c17a_start:c17b_start]
c22_start = cards.find('  <article class="doc-article" id="d2022-04-09">')
c17b_end = cards.find('  <article class="doc-article" id="d2022-04-09">')
c17b = cards[c17b_start:c17b_end]
c22 = cards[c22_start:]

# d2015-11-22 → 插在 d2006-08 卡后（最前，找 id="d2006-08" 所在 article 结束……简化：插在 d2010-01-29 注释/article 前）
i10 = s.find('id="d2010-01-29"')
j10 = s.rfind('  <!--', 0, i10)
s = s[:j10] + c15 + s[j10:]
# d2017-09-13/21 → 插在 d2016-10-12 卡后（即 d2018-08-07 锚前）
i18 = s.find('id="d2018-08-07')
j18 = s.rfind('  <!--', 0, i18)
s = s[:j18] + c17a + c17b + s[j18:]
# d2022-04-09 → 插在 d2022-04-11 卡前
i22 = s.find('id="d2022-04-11"')
j22 = s.rfind('  <!--', 0, i22)
s = s[:j22] + c22 + s[j22:]

after = s.count('class="doc-article"')
assert after == 23, after
for did in ('d2015-11-22', 'd2017-09-13', 'd2017-09-21', 'd2022-04-09'):
    assert s.count(f'id="{did}"') == 1, did
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print(f'documents.html: {before} -> {after} doc-article')

p2 = 'tools/build-search-index.py'
t = io.open(p2, encoding='utf-8').read()
old = "'一手文档': 19"
assert old in t
t = t.replace(old, "'一手文档': 23", 1)
io.open(p2, 'w', encoding='utf-8', newline='').write(t)
print('index assertion 19 -> 23')
