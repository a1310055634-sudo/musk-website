# -*- coding: utf-8 -*-
"""V8 R08 backfill: V8-PROGRESS.md status row + archive + work record."""
import io

P = 'V8-PROGRESS.md'
s = io.open(P, encoding='utf-8', newline='').read()

old_row = '| 08 | X 帖史扩容（含 Wayback 核对已删帖） | in_progress | — | — | — |'
new_row = '| 08 | X 帖史扩容（含 Wayback 核对已删帖） | complete | v7.8.0 | 8ba772d | pending-push |'
assert s.count(old_row) == 1, 'row'
s = s.replace(old_row, new_row)

ARCHIVE = """## 核实来源留档（R08）

采料方法（本轮确立的镜像直读管线）：web.archive.org 本机 TLS 中断不可用——改用 **elonmuskarchive.org 镜像**：`/posts/{statusID}` 详情页直读即逐字锚；列表页 `?year=YYYY&page=N&sort=old` 每页 20 帖、全量回溯（2022 年约 200 页最深）；status ID→UTC 日期用 **snowflake 解码** `(id>>22)+1288834974657` 对表复核；列表页正文为逐词 `<span>` 序列化——去标签**不插空格**还原连续文本再检索关键词。十条锚点（全部详情页直读验证，除 p2020-05-01/p2023-07-23 为列表页逐字+详情页关键 ID 验证）：
- **p2020-03-06** status/1236029449042198528（20:42 UTC）：CNBC https://www.cnbc.com/2020/03/06/teslas-elon-musk-says-the-coronavirus-panic-is-dumb.html + Reuters https://www.reuters.com/article/business/tesla-ceo-elon-musk-tweets-that-coronavirus-panic-is-dumb-idUSKBN20T2WK/
- **p2020-05-01** status/1256239554148724737（15:10 UTC）+ status/1256239815256797184（15:11 UTC）两连发；卖房后续媒体广泛报道；站内互链 i2020-05
- **p2022-03-26** status/1507777261654605828（2022-03-26 17:51 UTC——UTC 口径；美媒 3.25 为 ET 口径，条目内注明）：镜像详情页直读；3.25 投票 status/1507596559831101446（05:53 UTC）以引用嵌套完整存档
- **p2022-04-14** status/1514564966564651008（11:23 UTC）+ 同日 status/1514681422212128770（19:06 UTC）；要约条款/TED 表态=站内 i2022-04-14、d2022-04-25
- **p2022-05-13** status/1525049369552048129（09:44 UTC）；Reuters 当日报道
- **p2022-11-01** status/1587498907336118274（21:12 UTC）：镜像详情页直读（**此前猜测 ID 1587553180897927168 系误记，镜像 404 后已纠正**）；The Verge 等报道 $8 方案与仿冒风波
- **p2022-12-18** status/1604617643973124097（23:20 UTC）；57.5%/1750 万票=Reuters（2022-12-19）+BBC（12-20）+CNBC 口径
- **p2023-07-23** status/1682964919325724673（04:04 UTC）+ status/1682965462886535168（04:06 UTC）；执行时间线=站内 px-0723
- **p2024-04-05** status/1776351450542768368（20:49 UTC）；Reuters 等当日报道（R05 已核）；跳票后续=e2024-04-23 + promises
- **p2025-03-28** status/1905731750275510312（21:20 UTC）：镜像详情页直读（8 处关键词命中）；CNBC/Forbes/AP 多源已在册
- **甄别记录（宁缺毋滥）**：①Hertz 对冲推文（p2021-10-26 候选）镜像四页直读无「no contract has been signed yet」句，措辞存疑弃收；②「I endorse President Trump」（2024-07-13/14 候选）镜像七页未命中原帖，媒体虽广泛报道但无镜像逐字，弃收待补；③镜像站逐年覆盖不均（2020 约 55 页/2022 约 200 页/2025 约 160 页），早期帖可后续回捞；④p2022-11-01 教训：凭记忆写 status ID 必须镜像 404 复核——本轮即被拦一次。

"""

RECORD = """## 第 8 轮工作记录（X 帖史扩容）— complete（2026-09-30）

- **交付**：x-posts.html +10 张（13→23，严格克隆 `<div class="tweet-card" id="p…">` 五件套模板，按时间序分组插入六处）：p2020-03-06（coronavirus panic is dumb）、p2020-05-01（卖房+too high imo 两连发，仿 p2022-10-28 两帖合一卡先例）、p2022-03-26（de facto public town square，收购案公开起点）、p2022-04-14（I made an offer）、p2022-05-13（temporarily on hold）、p2022-11-01（lords & peasants $8）、p2022-12-18（step down 投票）、p2023-07-23（bid adieu 更名两连发）、p2024-04-05（Robotaxi 8/8）、p2025-03-28（xAI 收购 X）。卡内互链 9 处（i2020-05/i2022-04-14/e2024-04-23/e2025-03-28/d2022-04-25/d2022-10-27/promises/platform-x/px-0723 等）。
- **交叉引用**：platform-x px-0414 sv-links 补「帖史：三个字的要约帖」、px-0723 补「帖史：告别宣言原帖」（双语 data-en 同步）。
- **管线**：build-search-index（断言 X 帖 13→23，索引 234→244 = 103+14+33+23+5+53+4+9）/ sync-changelog（187 条）/ build-epub（191,490 B，24 章）；版本 v7.7.0→v7.8.0（VERSION/app.js/14 页 span，node --check app.js cite.js 通过）；CHANGELOG 首条 v7.8.0；EXPANSION.md 顶部补 R08 入包块。提交后 build-revisions（163→173 锚点，X 帖 23）+ EPUB 重刷。
- **验证**：verify.py 9/9 全绿（37 页，索引 244）；提交前后各验一次。
- **提交**：主成果 `8ba772d`（28 文件）；本回填+revisions/EPUB 刷新为第二个提交。
- **实现备注**：①集成断言拦截两处实错——片段里 p2022-12-18 卡 `tweet-zh">` 丢引号（逐卡结构断言 `tweet-zh==1` 抓住）、 permalink 断言初版口径过宽（`href="#p` 会被卡内互链干扰，收紧为 `<a class="tweet-date" href="#` 唯一）；②时间序插入用「下一张既有卡的开标签」作锚、new=新卡块+anchor 拼回，六组断言全过；③x-posts 页无页级计数文案，改动面仅 10 卡+2 处平台页互链。
- **采料环境备注**：Wayback 本机不可用（R04 已知），本轮确立 **elonmuskarchive.org 镜像直读管线**（详情页=逐字锚、snowflake 对表日期、列表页全量回溯）；镜像对 2020/2025 年覆盖较薄，两条强候选（Hertz 对冲、Trump 背书）因镜像无逐字弃收留档。
- **下一轮预告**：R09 SpaceX / Neuralink / xAI 官方演讲（账本/文档 +6~8 条：2016 IAC 多行星演讲、星舰更新、Neuralink demo、Grok 发布；IAC 2016 演讲已有 i2016-09-27 与 e2016 条目，开轮先查重；官方逐字稿源=spacex.com 传输/NASA 转播/Numbski 逐字站，需勘定）。

"""

ANCHOR = '## 核实来源留档（R07）'
assert s.count(ANCHOR) == 1
s = s.replace(ANCHOR, ARCHIVE + ANCHOR, 1)
ANCHOR2 = '## 核实来源留档（R07）'
assert s.count(ANCHOR2) == 1
s = s.replace(ANCHOR2, RECORD + ANCHOR2, 1)

io.open(P, 'w', encoding='utf-8', newline='').write(s)
print('V8-PROGRESS.md backfilled: R08 complete (8ba772d)')
