# -*- coding: utf-8 -*-
"""V10-15 N06：documents.html 插入 d2016-10-12（SolarCity 合并委托书 recusal 段）
+ 索引断言 18→19。"""
import io

p = 'documents.html'
s = io.open(p, encoding='utf-8').read()
before = s.count('class="doc-article"')
assert before == 18

# 插入点：按时间序应插在 2016 年条目附近——找 d2016-07-20（Master Plan Deux）卡后
anchor_m = None
for a in ['<!-- ②b', '<article class="doc-article" id="d2017', '<article class="doc-article" id="d2016']:
    i = s.find('id="d2017')
    if i > 0:
        anchor_m = i
        break
# 简化：找 id="d2017" 的卡起始（时间序 2016-10-12 < 2017），向前找其注释行起点
i = s.find('id="d2018-08-07')
assert i > 0
# 向前找最近的 <!-- 注释开始或 <article 前
j = s.rfind('  <!--', 0, i)
insert_at = j if j > 0 else i

card = '''  <!-- ⑦a 2016.10.12 SolarCity 合并委托书 recusal -->
  <article class="doc-article" id="d2016-10-12">
    <h2>SolarCity Form DEFM14A（合并委托书 · 马斯克回避表决记录）</h2>
    <div class="doc-meta"><span class="doc-badge">SEC EDGAR 备案 · DEFM14A（合并/收购委托书）</span><a class="doc-badge" href="#d2016-10-12" title="定位到本文档 · Permalink">2016.10.12</a><span class="doc-badge">备案号 0001193125-16-736379 · SolarCity Corp（CIK 1408356）</span></div>
    <h4>原文摘录 · 董事会的回避决定（Background of the Merger）</h4>
    <blockquote>“…that Messrs. Elon Musk and Antonio Gracias, as a result of their service on the SolarCity Board, should recuse themselves from any vote by the Tesla Board on matters relating to a potential acquisition of SolarCity, including evaluation, negotiation and approval of the economic terms of any such acquisition. The Tesla Board also determined that the members of the Tesla Board other than Messrs. Elon Musk and Antonio Gracias should have the opportunity to deliberate with respect to any potential SolarCity transaction outside the presence of Messrs. Elon Musk and Gracias.”</blockquote>
    <p class="zh-line">……马斯克与格拉西亚斯二人因在 SolarCity 董事会任职，应在 Tesla 董事会就收购 SolarCity 相关事项——包括评估、谈判与经济条款批准——的任何表决中回避；且 Tesla 董事会其余成员应有机会在二人不在场的情况下，就任何潜在 SolarCity 交易进行审议。</p>
    <h4>原文摘录 · 执行（首次批准非约束性提案）</h4>
    <blockquote>“Messrs. Elon Musk and Gracias recused themselves and left the meeting and, following further deliberation by the other members of the Tesla Board …, the Tesla Board (with Messrs. Elon Musk and Gracias absent, having recused themselves) approved the making of a preliminary, non-binding proposal … to acquire all of the SolarCity common stock at an exchange ratio of 0.122 to 0.131 shares of Tesla common stock.”</blockquote>
    <p class="zh-line">马斯克与格拉西亚斯回避并离席；在其余董事进一步审议后，Tesla 董事会（二人缺席、已回避）批准发出初步非约束性提案——以 0.122 至 0.131 股 Tesla 股票兑 1 股 SolarCity 的换股比例收购其全部流通股。</p>
    <h4>原文摘录 · 终局（合并协议批准表决）</h4>
    <blockquote>“After discussion, the Tesla Board, with Messrs. Elon Musk and Antonio Gracias absent, having recused themselves, (1) determined that the merger agreement and the transactions contemplated thereby … are fair to, advisable and in the best interests of Tesla and its stockholders, (2) approved the merger agreement …”</blockquote>
    <p class="zh-line">讨论之后，Tesla 董事会——马斯克与格拉西亚斯缺席、已回避——(1) 认定合并协议及其项下交易对 Tesla 及其股东公平、适当且符合最佳利益，(2) 批准了合并协议……</p>
    <p class="doc-note">委托书「Background of the Merger」整章系统记录了回避制度的执行：从 2016 年 4 月董事会作出回避决定，到 7 月多次特别会议二人「recused themselves and left the meeting」，再到 7 月 30 日批准合并协议时的表决回避。本条是马斯克关联交易治理争议（SolarCity 收购案）的第一手程序证据；股东批准与诉讼弧线见争议深读。委托书由被收购方 SolarCity 备案（CIK 1408356），特殊会议定于 2016-11-17。</p>
  </article>

'''
s = s[:insert_at] + card + s[insert_at:]
after = s.count('class="doc-article"')
assert after == 19, after
assert s.count('id="d2016-10-12"') == 1
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print(f'documents.html: {before} -> {after} doc-article, d2016-10-12 inserted')

# 索引断言 18 -> 19
p2 = 'tools/build-search-index.py'
t = io.open(p2, encoding='utf-8').read()
old = "'一手文档': 18"
assert old in t
t = t.replace(old, "'一手文档': 19", 1)
io.open(p2, 'w', encoding='utf-8', newline='').write(t)
print('index assertion 18 -> 19')
