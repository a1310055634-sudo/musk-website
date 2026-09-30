# -*- coding: utf-8 -*-
"""V8 R09 backfill: V8-PROGRESS.md status row + archive + work record."""
import io

P = 'V8-PROGRESS.md'
s = io.open(P, encoding='utf-8', newline='').read()

old_row = '| 09 | SpaceX / Neuralink / xAI 官方演讲 | in_progress | — | — | — |'
new_row = '| 09 | SpaceX / Neuralink / xAI 官方演讲 | complete | v7.9.0 | ff340bc | pending-push |'
assert s.count(old_row) == 1
s = s.replace(old_row, new_row)

ARCHIVE = """## 核实来源留档（R09）

六场官方发布会/demo/演讲（镜像+媒体双源；X 帖类复用 R08 镜像管线，演讲类以媒体逐字双源立条）：
- **IAC 2017**（2017-09-29 阿德莱德）：「The future is vastly more interesting and exciting if we're a space-faring civilization and a multiplanet species than if we're not.」= Business Insider https://www.businessinsider.com/elon-musk-iac-mars-colonization-presentation-2017-9 ；官方视频 SpaceX YouTube「Making Life Multiplanetary」（youtube.com/watch?v=tdUX3ypDVwI）；社区逐字稿 r/SpaceXLounge（transcript 帖）对勘
- **Neuralink 2019**（2019-07-16 旧金山）：「A monkey has been able to control a computer with his brain.」= CT Insider（2019-07-17）+ Mashable（2019-07-17）双源；同场宣布 2020 人体试验时间表与缝纫机机器人/1024 通道细节
- **Neuralink 2020**（2020-08-28 线上「三只小猪」）：「a Fitbit in your skull with tiny wires」= TechCrunch（2020-08-28，techcrunch.com 原文 URL 现已 404，检索摘要多源核对）+ The Globe and Mail（2020-08-28）+ Silicon Republic（2020-08-31）
- **Pager MindPong**（2021-04-09）：镜像回帖逐字 status/1380314267077894148 + status/1380314485324308482（snowflake 解码均为 2021-04-09 00:19 UTC；Neuralink 官号视频帖前一日）；转发语「A monkey is literally playing a video game telepathically」= CNBC（04-09）+ CNET（04-08）+ Reuters 广泛报道
- **Starbase 星舰更新**（2022-02-10）：「I feel, at this point, highly confident that we'll get to orbit this year.」+「We'll probably lose a few vehicles along the way.」= Space.com（Mike Wall，2022-02-11 刊）https://www.space.com/elon-musk-spacex-starship-update-orbital-launch-2022 ；Spaceflight Now（2022-02-10）与 Everyday Astronaut 同日记录佐证（均无直引，条目内如实区分）
- **Grok 3 发布**（2025-02-18）：镜像详情页直读 status/1891699076267217406（03:59 UTC「Grok 3 presentation starting shortly.」）+ status/1891933115502809320（19:29 UTC「Subscribe to Premium+ to get the world's smartest AI!」）；Grok 官号同日「grok 3 is the world's smartest AI now available to all Premium+ subscribers」（列表页逐字）
- **查重勘定**：IAC 2016（e2016-09-27/i2016-09-27）、Starship Mk1（e2019-09-28）、xAI 官宣（e2023-07-12）、xAI 收购 X（e2025-03-28）、Neuralink Telepathy（e2024-01-29/i2024-01-29）已在册，本轮不重复
- **甄别记录（宁缺毋滥）**：①Grok 3 直播内容逐字不可得（livestream 无公开转录），「smartest AI on Earth」现场口号版未采，条目只收帖文第一手；②Neuralink 2019 完整逐字稿无公开版，「symbiosis」表述多在后续访谈未采；③Neuralink JMIR 论文（d2020-10-16 文档候选）jmir.org 本机不可达未收录，文档馆本轮不动；④镜像 2021 年扫描用页码外推（p120≈Oct → 回推 Apr≈p36-44）两页命中，未绕路

"""

RECORD = """## 第 9 轮工作记录（SpaceX / Neuralink / xAI 官方演讲）— complete（2026-10-01）

- **交付**：账本 primary.html +6 条（103→109，严格克隆 `<li class="ps-row ps-deep reveal">` 四段深读双语）：e2017-09-29（IAC 2017 BFR——「一枚火箭养所有梦」路线图，互链 e2016-09-27/e2022-02-10）、e2019-07-16（Neuralink 2019 猴子句 + 2020 人体试验时间表，互链 e2021-04-09/e2024-01-29）、e2020-08-28（Gertrude 猪演示 + Fitbit 比喻）、e2021-04-09（Pager MindPong + 两句回帖「Sure.」「Hopefully, later this year.」——人体试验第二次跳票的锚点）、e2022-02-10（「今年入轨」承诺 +「烧掉几枚」预防针，IFT-1 晚十四个月字面兑现，互链 p2024-10-13）、e2025-02-18（Grok 3 发布日两帖 + 「world's smartest AI」付费墙文案化，互链 p2023-11-04/grok.html）。
- **quotes.html** +6 卡（90→96）。**index.html** 计数文案 103→109 ×3（含 data-en）。promises 挂接沿 R04/R05 先例留 R10 收官轮统一评估（e2022-02-10 的「今年入轨」与在册「六个月内入轨」挂起项同族）。
- **管线**：build-ledger-timeline（109 节点）/ build-search-index（断言 言行实录 103→109，索引 244→250 = 109+14+33+23+5+53+4+9）/ sync-changelog（188 条）/ build-epub（196,187 B，24 章）；版本 v7.8.0→v7.9.0（VERSION/app.js/14 页 span，node --check app.js cite.js 通过）；CHANGELOG 首条 v7.9.0；EXPANSION.md 顶部补 R09 入包块。**verify 首跑红一盏（账本 +6 未上语录卡——R04/R05 先例账本轮必加卡），补 6 张 qs-card 后全绿；EPUB 因 quotes 晚建重跑一次**。提交后 build-revisions（173→179 锚点）+ EPUB 重刷。
- **提交**：主成果 `ff340bc`；本回填+revisions/EPUB 刷新为第二个提交。
- **实现备注**：①**primary.html 行尾已转 LF**（crlf=0/lf=1579，与「工作区带 CRLF」旧认知不符——集成脚本改为探测目标文件行尾自适应，两文件各自归一）；②语录卡覆盖检查是账本轮的必过门：`qs-card` 数必须追平 `ps-quote` 数（豁免 3 项），本轮 verify 首跑即被拦，教训=账本条目与语录卡应同轮同批写入；③quotes 卡插入锚复用「下一张卡的开标签」拼回模式。
- **采料环境备注**：WebSearch 多次 429 限流——镜像扫描（2025 年页码二分外推：p130≈Feb1 → p232≈Feb18）与 WebFetch 直读（Space.com 逐字全文）成为主力；搜索限流窗口约 75-120 秒。
- **下一轮预告**：R10 全站验收与发布 v8.0.0（收官轮：重建全部索引与时间轴、EPUB、专题页交叉引用补齐——R04-R09 遗留的 promises 挂接在本轮统一评估、sitemap.xml 更新、CHANGELOG 首条、VERSION 升 v8.0.0、verify 全绿、DEVLOG.md 回填交接）。

"""

ANCHOR = '## 核实来源留档（R08）'
assert s.count(ANCHOR) == 1
s = s.replace(ANCHOR, ARCHIVE + ANCHOR, 1)
s = s.replace(ANCHOR, RECORD + ANCHOR, 1)

io.open(P, 'w', encoding='utf-8', newline='').write(s)
print('V8-PROGRESS.md backfilled: R09 complete (ff340bc)')
