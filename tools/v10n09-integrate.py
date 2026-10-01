# -*- coding: utf-8 -*-
"""V10-15 N09：documents.html 插入 4 封 Tesla 冲刺信（时间序）+ 索引断言 23→27。"""
import io

p = 'documents.html'
s = io.open(p, encoding='utf-8').read()
before = s.count('class="doc-article"')
assert before == 23, before


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


c_sab = doc(
    'd2018-06-17', '「破坏者」全员信（马斯克致 Tesla 全体员工）',
    '全员邮件 · 媒体获得口径（CNBC 2018-06-18 全文报道）', '2018.06.17',
    'elonmuskarchive.org/email 底本 + CNBC 双源',
    [
        ('原文摘录 · 破坏行为定性',
         '…a Tesla employee who had conducted quite extensive and damaging sabotage to our operations.',
         '……一名 Tesla 员工对我们的运营实施了相当广泛且具破坏性的蓄意破坏。'),
        ('原文摘录 · 手段',
         '…making direct code changes to the Tesla Manufacturing Operating System under false usernames.',
         '……使用虚假用户名直接对 Tesla 制造操作系统（TMOS）做代码改动。'),
    ],
    'Model 3 产能爬坡黑暗周的内患信：马斯克通报一名员工因绩效处分未获升职而蓄意破坏（向 CNBC 提供细节），并预告「未来几周将是最难的一段」。口径：媒体获得（CNBC 全文报道+镜像底本，双源 2026-10-02 核验）。')

c_rq = doc(
    'd2020-09-20', '「冲刺创纪录季度」全员信（马斯克致 Tesla 员工）',
    '全员邮件 · 媒体获得口径（Electrek/CNBC 2020-09 报道）', '2020.09.20',
    'elonmuskarchive.org/email 底本双源',
    [
        ('原文摘录',
         'We have a shot at a record quarter for deliveries, but we’ll have to rally hard to achieve it. Please consider vehicle deliveries to be the absolute top priority.',
         '我们有机会创下单季度交付纪录，但必须全力冲刺才能实现。请把车辆交付当作绝对的第一优先级。'),
    ],
    '季度末十天的交付冲刺令：Q3 2020 最终交付 13.93 万辆创当时纪录（疫情后产能恢复的标志性一役）。口径：媒体获得（Electrek/CNBC 报道+镜像底本，2026-10-02 核验）。')

c_souffle = doc(
    'd2020-12-01', '「舒芙蕾与大锤」盈利警告全员信（马斯克致 Tesla 员工）',
    '全员邮件 · 媒体获得口径（CNBC 2020-12-01 报道）', '2020.12.01',
    'elonmuskarchive.org/email 底本 + CNBC 双源',
    [
        ('原文摘录 · 利润率现实',
         '…our profitability is very low at around 1%.',
         '……我们的盈利能力非常低，只有大约 1%。'),
        ('原文摘录 · 若投资者失去信心',
         '…our stock will immediately get crushed like a soufflé under a sledgehammer!',
         '……我们的股价会立刻被砸扁——像舒芙蕾碰上大锤！'),
    ],
    '入标普 500 当周的清醒剂信：在股价狂热的顶点警告利润率仅约 1%、投资者信心一旦动摇股价即崩（「舒芙蕾碰大锤」由此成为年度名句）。口径：媒体获得（CNBC 报道+镜像底本，双源 2026-10-02 核验）。')

c_rto = doc(
    'd2022-05-31', '「回到办公室」邮件（马斯克致 Tesla 行政员工）',
    '全员邮件 · 媒体获得口径（CNBC 2022-05-31 全文报道）', '2022.05.31',
    'elonmuskarchive.org/email 底本 + CNBC 双源',
    [
        ('原文摘录',
         'Everyone at Tesla is required to spend a minimum of 40 hours in the office per week. … If you don’t show up, we will assume you have resigned.',
         'Tesla 每个人每周必须在办公室至少待满 40 小时。……如果你不出勤，我们将视为你已辞职。'),
    ],
    '疫情后远程工作的终结令（对行政岗要求每周 40 小时在岗，远程需马斯克本人特批）。CNBC 拿到全文后 Tesla 人力资源与舆论风暴随之而来——此信成为 2022 年「大回归办公室」争论的标志文件。口径：媒体获得（CNBC 全文报道+镜像底本，双源 2026-10-02 核验）。')

# 时间序插入：d2018-06-17 在 d2018-08-07 前；d2020-09-20 与 d2020-12-01 在 d2021-11-26 前；d2022-05-31 在 d2022-07-26 前
i18 = s.find('id="d2018-08-07')
j18 = s.rfind('  <!--', 0, i18)
s = s[:j18] + c_sab + s[j18:]

i21 = s.find('id="d2021-11-26')
j21 = s.rfind('  <!--', 0, i21)
s = s[:j21] + c_rq + c_souffle + s[j21:]

i726 = s.find('id="d2022-07-26')
j726 = s.rfind('  <!--', 0, i726)
s = s[:j726] + c_rto + s[j726:]

after = s.count('class="doc-article"')
assert after == 27, after
for did in ('d2018-06-17', 'd2020-09-20', 'd2020-12-01', 'd2022-05-31'):
    assert s.count(f'id="{did}"') == 1, did
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print(f'documents.html: {before} -> {after} doc-article')

p2 = 'tools/build-search-index.py'
t = io.open(p2, encoding='utf-8').read()
old = "'一手文档': 23"
assert old in t
t = t.replace(old, "'一手文档': 27", 1)
io.open(p2, 'w', encoding='utf-8', newline='').write(t)
print('index assertion 23 -> 27')
