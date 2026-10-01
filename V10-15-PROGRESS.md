# V10-15 计划进度记录（内容精修：全面核实 · 第一手信息 · 社区资源）

> 「马斯克商业志 MUSK, INC.」V10-15 十五轮计划（2026-10-02 启动，任务书内嵌定时提示词 automation-3a82f550）。
> 本文件是本计划唯一轮次账本；与 git 相互核验。前序：V8（v7.1.0→v8.0.0，V8-PROGRESS.md）、V9-20（v8.1.0→v10.0.0，V9-20-PROGRESS.md）。
> 提交前缀 `[V10-15 Nxx]`；锁 `.v10run.lock`（已入 .gitignore）；QA 存 `qa/v10-15/round-NN/`；工具脚本 `v10nNN-*`。

## 基线快照（=V9-20 R20 口径，2026-10-02）

- 分支 main，VERSION **10.0.0**；38 页（含 resources；revisions.html 为 noindex 机器页）；账本 115；文档 18；访谈 42；X 帖 31；语录卡 103（引文块 105=103+豁免 2）；事件档案 14（59 材料）；资源 36（官方 10/开源 9/社区 11/工具 6）；索引 318；sitemap 37 URL；EPUB 24 章；verify 9 项。
- 版本阶梯：N01=v10.1.0 → N14=v10.14.0 → N15=**v11.0.0**。
- 三大主线：**核实**（N01–N04：源存活/引语 verbatim diff/口径审计/资源复测，纪律 D 三级处置）→ **第一手**（N05–N11：早期年代/文档补空/X 帖 2018–19/email 库 43 封/keynote 池/保留池）→ **社区资源**（N12–N13：SpaceX 观测生态/档案书目，资源 36→55±）→ **聚合收官**（N14 事件档案 v2 / N15 终检+盘点 v2+待发布清单 v2）。

## 轮次状态

| 轮 | 主题 | 状态 | 版本 | 成果提交（本地） | 备注 |
|---|---|---|---|---|---|
| N01 | 全站源存活复测（六页外链三路法） | complete | v10.1.0 | 5b09bb9 | 口径修正=六页来源为 ps-src 文字徽章无明文外链→复测全站 37 条真实外链；零死链（直连 12+api 8/8+服务端复核+同域推定+受限 5+前档佐证 2）；stars 微漂移 4 条记录；报告 37/37 落盘 |
| N02 | 引语逐字核验 I（机核：X 帖/访谈/账本 115） | complete | v10.2.0 | 3c4f0c3 | 机核三件管线+镜像语料 9 场；X 帖 31=18v+3 合并卡+1 无档+9 无锚；访谈 16/42、账本 5/106 verified（余待人工=语料未覆盖非镜像源）；零实质差异零修正 |
| N03 | 引语核验 II＋口径审计＋复核声明上站 | complete | v10.3.0 | 9ec238d | snowflake 22/22 match+注记零缺失；人工抽样 stockanalysis 2/2 逐字吻合；未覆盖 101 块逐条归因落盘；双语探针（quotes 100 卡/primary 引文行 100% 配译文）；声明上站 primary+quotes（纪律 D 门槛达成）；探针 6/6 |
| N04 | 资源核活复测＋元数据升级（36 条刷新） | complete | v10.4.0 | be988ed | 36 条零死链（N01 复用+api 8/8）、checked 全刷 2026-10-02、stars 漂移 4 条同步、弃收件重验维持留档（tesla Akamai/SAE JS 壳）；validate 过 verify 9/9 |
| N05 | 早期年代 I：访谈 2003–2012（161 场库过滤） | complete | v10.5.0 | ee61ffb | 实测 9 场仅 wired-musk-2008 有逐字稿（60-minutes-2012 判断修正降级）；立条 i2008-08-05（名句原始出处，访谈 42→43 索引 319）；8 场留档；探针 8/8 |
| N06 | 早期年代 II：文档馆补空（DEFM14A 等） | pending | — | — | — |
| N07 | X 帖 2018–2019 回捞（镜像下限实测） | pending | — | — | — |
| N08 | email 库消化 I（Twitter 收购私信/OpenAI 证物） | pending | — | — | — |
| N09 | email 库消化 II（生产冲刺信等，清账） | pending | — | — | — |
| N10 | keynote/speech 池消化＋AI Day 2021 引语升级 | pending | — | — | — |
| N11 | 访谈保留池清账（五场立条或注明） | pending | — | — | — |
| N12 | 社区资源 I：SpaceX 观测生态（LabPadre/NSF 等） | pending | — | — | — |
| N13 | 社区资源 II：档案与书目（资源 36→55±） | pending | — | — | — |
| N14 | 事件档案 v2 聚合（14→16±，口径红线） | pending | — | — | — |
| N15 | 终检＋盘点总表 v2＋待发布清单 v2（v11.0.0） | pending | — | — | — |

## 恢复指引

- 每次触发读本表定轮次（最早 pending/上轮中断先恢复）；建锁 `.v10run.lock`（有效锁退出；死锁须进程+仓库静默>15min）；结束删锁。
- 一轮一成果提交+一账本回填提交；核实轮（N01–N04）报告全量落盘 qa/v10-15/round-NN/（含红项）。
- 管线同 V9-20：改一手页必跑 build-ledger-timeline/build-search-index/build-epub；CHANGELOG 后 sync-changelog；提交后 build-revisions+EPUB 重刷为第二提交；verify 9/9 底线。
- 关键教训已固化：探针端口 9333+/全新 user-data-dir；先建 round-NN 目录再截图；bump 派生须同改 OLD+两处正则旧值；网络轮折损如实入账；死链判定必服务端交叉确认；同名项目甄别（斯巴鲁）；政治类默认不立。
- 15 轮全 complete 后再次触发：静默退出。

## 第 1 轮工作记录（N01 全站源存活复测）— complete（2026-10-02）

- **口径修正（任务书预期与实测的偏差，如实入账）**：scan 干跑发现六页来源标注全部为 `.ps-src` 文字徽章形态、无明文超链接——本站结构=资源页外链层（resources 36 卡）+一手页文字锚层（锚在账本文字与 qa/v9-20 溯源）。复测对象据实调整为全站 38 页真实外链 37 条；引语逐字核验归 N02 transcript diff（本就如此分工）。
- **复测结果（37 条，零死链）**：直连存活 12 / GitHub 8 条走 api.github.com 全 200（stars 微漂移 4 条记录在案：SpaceX-API 10912→10913、teslamate 9061→9065、grok-1 52239→52233、vehicle-command 705→706——字段刷新归 N04）/ wikipedia Elon_Musk+Starship+tesla-api.io 服务端读取器 200 / wikipedia 余 6 条同域代表推定（口径注明，本机 DNS 波动非死链——R12/R13 直连 200 先例）/ openai.com+x.ai 前档佐证（R11 服务端 200 在档）/ 本机受限 5（tesla/spacex/reddit/archive 历史实测）/ w3.org SVG 命名空间 n/a（脚本已排除此类）。
- **工程**：tools/v10n01-sources.py（scan 干跑/check 全量两模式；RESTRICTED 预分类补录 openai.com Akamai 403）；报告落盘 qa/v10-15/round-01/（inventory.tsv/check.json/report.tsv/report.json 四件，二路复核与口径注记逐条在案）。
- **验证**：verify 9/9（38 页/索引 318）；报告覆盖 37/37；纯核实轮零页面内容改动。bump 派生坑第四次（v9r20 正则旧值未升级）——红线 grep 拦截后修正；**教训升级：每次 bump 后应顺手把本次脚本的「正则旧值」升级为本次 NEW，供下轮派生直接匹配**。
- **提交**：成果 `5b09bb9`（v10.1.0，10 文件）；本回填+revisions（206 幂等）+EPUB 重刷为第二提交。
- **下一轮预告**：N02 引语逐字核验 I（机核，v10.2.0）——X 帖 31 条 Agent API transcript 逐字 diff（全自动）；访谈 42 条 transcript 在档者引语句 indexOf 核验；账本 115 条引文块提取比对；差异三级处置（纪律 D），实质差异当轮修正（账本+语录卡同轮同批）。

## 第 2 轮工作记录（N02 引语逐字核验 I 机核）— complete（2026-10-02）

- **机核管线三件**：v10n02-extract.py（三类提取：X 帖 31 卡[tweet-text+status id，卡起点切片法——嵌套 div 截断教训]、访谈 42 裸 blockquote、账本 106 引文块/105 条目）/ v10n02-corpus.py（镜像 interview 按日期精确匹配 19 场、新拉 9 场 transcript 入 qa/v10-15/round-02/sources）/ v10n02-verify.py（本地 45 文件 2.66M 归一字符语料 indexOf + 镜像 API 分段 diff）。
- **结果（零实质差异，无引语修正）**：X 帖 31=18 verified+3 合并卡口径（两连发合一卡 vs 镜像单帖——p2023-07-23 人工深查镜像原文与站内第一段逐字吻合）+1 镜像疑无档（p2018-01-28 flamethrower，2018 覆盖稀薄）+9 no-anchor；访谈 42=16 verified+26 待人工；账本 106=5 verified+101 待人工。**待人工归因=语料未覆盖非镜像源**（V8 时代条目来自 stockanalysis/TED/Rev/JRE/EDGAR，本地无 transcript；Cloudflare 拦脚本）——非发现差异，N03 人工抽样续核。
- **甄别记录**：首跑 3 条 mismatch 逐条深查全部定性合并卡结构口径——判定逻辑修正为分段 indexOf+合并卡口径（避免假红，红线「机核报告不许只报绿色」同样适用反方向：不许把结构口径误报成实质差异）。
- **bump 派生坑第五次**：派生 replace 目标档位错（v10n01 正则=10\.0\.0 非 10\.1\.0）——教训再升级：**派生前先 grep 基础文件的实际 subn 行，replace 用其实际值**；本次已把 N02 bump 正则滚到 10\.2\.0 供 N03 直接派生。
- **验证**：verify 9/9；版本三件套 10.1.0→10.2.0（15 span 一致）；纯核实轮页面内容零改动。
- **提交**：成果 `3c4f0c3`（v10.2.0）；本回填+revisions（206 幂等）+EPUB 重刷为第二提交。
- **下一轮预告**：N03 引语逐字核验 II＋口径审计（v10.3.0）——snowflake 全量对表（31 帖）；双语卡 EN/ZH 对齐探针（quotes+primary 抽样）；numbers.html 数字与 10-K/财报对照抽核；日期口径注完备性走查；**达标后在 primary.html 与 quotes.html 上「引语复核声明」**（双语+复核日期+覆盖口径——覆盖口径须含 N02 待人工项的处置结果）。

## 第 3 轮工作记录（N03 口径审计＋复核声明上站）— complete（2026-10-02）

- **snowflake 全量对表**：22 条有 id 帖解码 UTC 与卡内日期全 match、UTC 注记零缺失（tools/v10n03-audit.py，报告 snowflake-audit.json）。
- **人工抽样（纪律 D）**：stockanalysis 财报会抽 2 条——Q3 2017「How hot is it in hell…level 9→level 8」（23967）与 Q4 2015「Model 3 unveiling end of next month…well-received」（23975）——**2/2 逐字吻合**（WebFetch 通道，Cloudflare 不拦）。
- **未覆盖逐条归因**：N02 待人工 101 块逐条落盘 unmatched-itemized.tsv（other-official 73/earnings-call 20/edgar 6/jre 1/ted 1）——纪律 D「逐条注明原因」门槛达成。
- **双语对齐**：quotes 103 卡 100 卡双语齐备（3 卡形态特殊如实记）；primary 抽样含引文块行 100% 配译文——首跑误报 2 行深查为 SolarCity 两案无本人逐字引语（如实设计），探针口径校准（教训：先目检行结构再写断言，`:not(.ps-deep)` 误用引出 0 行——115 行全为 ps-deep 深读版）。
- **声明上站**：primary.html（ps-search-wrap 后）与 quotes.html（qs-p 后）双语声明 id=quote-review-statement，措辞如实三层（镜像机核/人工抽样 2-2/未覆盖逐条注明）；样式 .ps-review-note/.qs-review-note 消费令牌（style.css +4 行）。
- **验证**：verify 9/9；探针 6/6（tools/v10n03-probe.js 端口 9385）；版本三件套 10.2.0→10.3.0；sync-changelog 212 条；EPUB 223,463B。**bump 派生正则前滚机制首次完整落地**（运行后立即滚到 NEW 供下轮）。
- **提交**：成果 `9ec238d`（v10.3.0）；本回填+revisions（206 幂等）+EPUB 重刷为第二提交。
- **下一轮预告**：N04 资源核活复测＋元数据升级（v10.4.0）——resources-data.py 36 条全量复测（http/stars/pushed 刷新、checked 改 2026-10-02）；GitHub 漂移 4 条（N01 记录）同步刷新；死链按纪律 B；EXPANSION 弃收件重验（SAE/tesla.com 维持留档）。

## 第 4 轮工作记录（N04 资源核活复测＋元数据升级）— complete（2026-10-02）

- **36 条全量复测**：tools/v10n04-recheck.py 复用 N01 同日直连/api 结果（qa/v10-15/round-01，零死链）+ GitHub api 串行刷新 8 条全 200；v10n04-apply.py 写回（checked 批量替换 36 处+gh 逐条精确替换带断言）。stars 漂移 4 条同步：vehicle-command 705→706 / teslamate 9061→9065+pushed 2026-10 / grok-1 52239→52233 / SpaceX-API 10912→10913。
- **弃收件重验**：tesla.com 专利博文（服务端读取器重试仍 Akamai）、SAE J3400（仍 JS 壳）维持留档；Swisher/JMIR 维持——EXPANSION 顶部 N04 注记。
- **验证**：validate() 过（36 条四类计数不变）；verify 9/9；版本三件套 10.3.0→10.4.0。**bump 正则三步法首次完整执行**（设正则=当前版本→跑→前滚到 NEW；派生时不可把正则直接设为 NEW——本轮第一次跑 count=0 即因正则被错设为 NEW）。
- **提交**：成果 `be988ed`（v10.4.0）；本回填+revisions+EPUB 重刷为第二提交。
- **下一轮预告**：N05 早期年代 I：访谈库 2003–2012 深挖（v10.5.0）——interviews-all.json 161 场过滤 2013 前场次、对表查重、择官方转写在档者立条（60-minutes-2012-03-18 在此消化）；验收 +3~6 条（42→45±）或如实留档。
## 第 5 轮工作记录（N05 早期年代 I）— complete（2026-10-02）

- **候选池实测（预告修正）**：镜像 2013 前 9 场逐场试拉 transcript——仅 wired-musk-2008 有逐字稿（4,008 字符，Wired.com Carl Hoffman）；其余 8 场 404。**R04/R05「60-minutes-2012-03-18 官方转写在档」判断经实测不成立**（transcript 端点 404），保留池该成员降级「待外部逐字源」（CBS 官网/播出稿），N11 按此口径处置——EXPANSION 顶部 N05 注记。
- **+1 条入册（访谈 42→43，索引 318→319）**：i2008-08-05「乐观悲观，滚他妈的；我们会让它发生」——三连败后/四飞前 5 周/金融危机最坏周的 Wired 专访：主句（站外广为征引名句的原始出处补全，四页查重零命中）+「那是我说过的最蠢的话」（三次预算论自嘲修正）+「耐心是美德」；互链 i2008-09-28 与 survival-2008；transcript 存档 qa/v10-15/round-05/sources/。
- **工程**：集成断言三修（interviews.html iv-item 标签数=入索引数+1[legacy 无 id 条目]，R07 坑现役复现）；探针「假 390」自误修正；CHANGELOG 误插 ACCEPTANCE 全文后替换为规范条目；账本回填 heredoc GBK 化失败致漏写（b5b43c9 为空回填）——本提交补正（**教训再固化：深夜账本更新一律 Write 工具，禁 heredoc**）。
- **验证**：verify 9/9（38 页/索引 319）；探针 8/8；版本三件套 10.4.0→10.5.0（三步法+前滚至 10.5.0）；sync-changelog 214 条；EPUB 224,144B；修订史 207 锚点（访谈 43 入轨）。
- **提交**：成果 `ee61ffb`（v10.5.0）；`b5b43c9`（空回填）+本补正提交共同构成第二提交。
- **下一轮预告**：N06 早期年代 II：文档馆补空（v10.6.0）——EDGAR 直读优先（2016 SolarCity DEFM14A recusal 段为主目标）；tesla.com 博客/web.archive 本机受限试服务端读取器；+2~4 份或逐项留档弃收。
