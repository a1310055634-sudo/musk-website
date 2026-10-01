# R13 验收记录 · 社区与档案资源（v9.3.0）— complete

日期：2026-10-01 · 轮次：V9-20 R13/20

## 本轮范围与验收目标
- 目标：社区与档案资源扩容（计划指定 en.wikipedia.org 条目群、媒体档案库择要）+ R11–R13 元数据补全。
- R11–R13 合计目标 +30~50 条：R11 +8 / R12 +6 / **R13 +12** = **+26 条**（计划软目标区间内，见下注）。

## 成果
- **+12 条入库**：community 3→11（Wikipedia 8 条：Elon Musk / SpaceX / Tesla, Inc. / Starship / Twitter acquisition / List of SpaceX launches / Grok / Neuralink）· opensource 6→9（Tesla JSON API 文档站 / TeslaPy / Powerwall 2 本地网关 API）· tools 5→6（Jonathan McDowell 太空档案）。
- 全站资源 **24→36**；检索索引 **306→318**。

## 验证结果
| 项 | 结果 |
|---|---|
| verify.py | **9/9 全绿**（38 页 / 索引 318 / 版本 9.3.0 / 语录卡 103+2 豁免 / 修订史 206 / EPUB 新鲜） |
| node --check | app.js / search-index.js / companies-data.js / events-data.js / timeline-events.js / capital-data.js 全通过 |
| CDP 探针 | **35/35 全绿**（tools/v9r13-probe.js，端口 9357） |
| 版本三件套 | 9.2.0→9.3.0（VERSION + app.js SITE_VERSION + 15 页 span） |
| EPUB | 223,126 bytes / 24 章 |
| 截图 | qa/v9-20/round-13/：resources-community-desktop.png（1440×900）、resources-wikipedia-390.png（390×844） |

## 探针断言分布（35 项）
- 文件级 13：rs-item 锚=36 / 12 新卡 id 全在册 / community 节计数=11 / Reddit 假活两项不收 / R12 r/SpaceX wiki 保留 / wikipedia 证伪注记 / 版本 9.3.0 / xAI·Neuralink 公司标签 / 索引 318 / 资源索引 36 / 索引含 wikipedia-elon-musk / **revisions 导航治本保持** / 38/38 入站导航。
- 结构 9：hero（h1+版本）/ rs-item=36 / 四节 10·9·11·6 / wikipedia 证伪注记 / wikipedia 8 卡全在 community 节 / TeslaPy ★417+MIT+200 / Powerwall ★290+Apache+停更 / planet4589 tools 类无 gh / 外链 href 逐字。
- 筛选 3：社区与档案 11 条+三节隐藏 / wikipedia 8 卡可见 / 全部恢复 36 条。
- 双语 4：卡名切换 / 注记随语言（overturning）/ 节名 Community & Archives / 切回中文复原。
- 无 JS 1：禁脚本重载 36 条全量可见。
- 检索联动 3：维基百科 / TeslaPy / Grok 各命中。
- 390 零溢出 2：scrollWidth=390 / community 11 卡全渲染。

## 探针修正记录（1 项，非页面缺陷）
- 首跑 33/34：断言「页内无 reddit 条目 URL」用宽松正则 `https://[^"]*reddit\.com` 匹配，误命中 **R12 已核活收录的 r/SpaceX 社区维基**（其 URL 本就含 reddit.com，属正确保留，非本轮误收）。收敛为两条精确断言——「teslamotors/SpaceXLounge 假活 wiki 不在页」+「R12 r/SpaceX wiki 保留（回归不误删）」——修正后 35/35 全绿。**教训：排除类断言须锚定到具体目标项，勿用宽泛域名正则。**

## 弃收与留档（详见 EXPANSION.md R13 块与 sources/liveness.md）
- Reddit r/teslamotors 与 r/SpaceXLounge wiki：直连 200 但 8.4 KB JS 空壳、JSON API 403 → 不收。
- teslaownersonline.com：202 + JS proof-of-work 挑战软页 → 不收。
- web.archive.org / spaceflightnow / apnews / reuters / nytimes / science.org / sec.gov 搜索页：000 或 403 → 留档待重验。
- 媒体 hub 页（teslarati / electrek / arstechnica / nasaspaceflight / everydayastronaut / space.com / theverge / techcrunch / cnbc / BBC）：全部 200 真内容，入后续候选池（R14 起按检索联动需要择要）。

## 与计划目标的关系
- 计划 R13 点名「en.wikipedia.org 相关条目、Reuters/AP 专题页择要、媒体档案库」：Wikipedia 群 8 条全落（含 R10 污染判定证伪）；Reuters/AP 本轮 401/403 不可核活 → 留档（重验条件=用户环境实访）；媒体档案库入候选池。
- **R11–R13 合计 +26 条**（目标 +30~50 软区间下沿略低）：原因为媒体大型通讯社（Reuters/AP/NYT）本机全被 401/403、Wayback 000、Reddit 空壳三重阻塞，可核活的高质量条目池耗尽于 26 条。已如实盘点，不灌水凑数；R14 起若用户环境放宽可直接补媒体档案类。
