# V9-20 计划进度记录（第一手信息扩充 + 开源社区资源板块 + 美术升级）

> 「马斯克商业志 MUSK, INC.」V9-20 升级计划（共 20 轮，2026-10-01 启动）。
> 本文件是本计划的唯一轮次账本；与 git 提交记录相互核验，不以提交总数推算轮次。
> 历史计划：V7 十九轮改版（v6.6.0→v7.0.0）见 `V7-19-PROGRESS.md`；V8 十轮扩充（v7.1.0→v8.0.0）见 `V8-PROGRESS.md`。不继承其计数。

## 运行模式（重要）

- **纯本地模式**：每轮仅做本地 git 提交，**绝不 push、不 fetch 后合并远程、不改写已有历史、不做云端发布与 Pages 验证**。第 20 轮输出「待发布清单」，由用户验收后自行推送。
- 每次触发完成一个未完成轮次；上轮中断先恢复。成功轮次共 20；失败/空触发/重复检查不增加轮次；一轮未验收不进下一轮。
- 20 轮全部本地验收通过后，后续触发**静默退出**（不改文件不加版本不提交）。
- 每轮锁：`.v9run.lock`（不入 git，已在 .gitignore）。有效锁直接退出；确认旧实例已死（进程+仓库静默>15min）才可恢复遗留锁。

## 基线快照（2026-10-01 核对）

- 分支 main @ `24020fe`（V8 R10 本地版收官提交），VERSION `8.0.0`；origin/main 停在 `355fc0d`（v7.9.0 时代）——**待用户推送**。
- 工作区干净：37 个 HTML 页面；账本 109 条；一手文档 14；访谈 33；X 帖 23；语录卡 96（引文块 99，豁免 3）；检索索引 250（109+14+33+23+5+53+4+9）；事件档案 9 档 37 材料；时间轴 109 节点 + 223 独立记录（吸收 18）；资本流向 18 笔；修订史 179 锚点；EPUB 24 章；verify.py 9 项。
- 每轮版本步进：R01=v8.1.0 → R19=v9.9.0 → R20=v10.0.0（每轮必 bump，以 VERSION 实测为准不降级）。版本三件套 = VERSION + app.js SITE_VERSION + 14 页 site-version-val span（替换计数须打印）。

## 轮次状态

| 轮 | 主题 | 状态 | 版本 | 成果提交（本地） | 备注 |
|---|---|---|---|---|---|
| 01 | V8 R10 收尾 + V9-20 基建（账本/锁/gitignore） | complete | v8.1.0 | 9cc5d46 | 含 V8 R10 本地版 24020fe |
| 02 | X 帖回捞 I（2020–2021），目标 23→27± | complete | v8.2.0 | d3c2a3c | +4 帖；Hertz 重验入册；年份分组两处修正；探针 24/24 |
| 03 | X 帖回捞 II（2022–2025 深水区），目标 31± | complete | v8.3.0 | c049610 | +4 帖（Cybertruck 首交付/特拉华判决/Trump 背书重验/America Party）；探针 32/32 |
| 04 | 访谈扩充 I（Code Conf 2016 / EA 星舰 / Swisher / Satellite 2020） | complete | v8.4.0 | 52a03fc | +4 条（Code 2016 仿真论证/Satellite 2020 双零/EA 2021 五步算法/All-In 2024 DMV 重验）；Decode 2018 弃收；探针 29/29 |
| 05 | 访谈扩充 II + Lex 候选消化（#252/#400 立条） | complete | v8.5.0 | c7431d1 | +5 条（#252 保险/#400 言论自由/TED2013/Code2014/MKBHD2018）；候选池收尾 6 场留档；探针 29/29 |
| 06 | 文档馆扩充（Master Plan 缺 / SpaceX 更新信 / SEC 文件） | complete | v8.6.0 | f319ee9 | +4 份（S-1 2010/Acronyms 2010/Raptor 2021/10-K Technoking 2022）；Master Plan 四部曲查缺=已全在册；email 库 43 封入候选池；探针 31/31 |
| 07 | 官方演讲扩充（Starship 更新会 / Neuralink demo / AI Day） | complete | v8.7.0 | c10775e | +6 条 109→115（COP21/BFR 月旅/Autonomy Day/AI Day 2022/Neuralink S&T/Starbase）；语录卡 102；索引 277；探针 42/42 |
| 08 | 事件档案聚合扩容（9→14±，口径红线探针） | complete | v8.8.0 | 7a55ca9 | +5 档案（Tesla IPO/万亿市值日/Raptor 危机翻身/Neuralink 首植/Autonomy→Optimus）；材料 37→59；吸收 18→39、独立 229，282=14+39+229 口径闭环；chronicle kind 新增；探针 35/35 |
| 09 | 语录卡补齐 + 质量节点①（盘点总表入账本） | complete | v8.9.0 | efe7bec | e2013 立卡 102→103（约 2013 广泛征引如实双标）；verify 白名单 3→2 收严；盘点总表+缺口清单（EXPANSION）；探针 25/25 |
| 10 | 资源页基建（resources-data.py + build-resources.py + 导航注册） | complete | v8.10.0 | fdf366e | 10 条种子核活入库（官2/开2/社2/工4）；索引 282→292；探针 27/27；不可核活 7 条留档 EXPANSION |
| 11 | 官方与标准类资源 | complete | v9.1.0 | 84ec1e8 | +8 条 official 2→10（资源 10→18、索引 300）；三路法核活（7 条服务端读取器路径如实注记）；SAE J3400/tesla.com 弃收留档；修复 R10 导航回归；探针 30/30 |
| 12 | 开源项目资源（Tesla API 生态 / Starlink 追踪 / 发射工具） | complete | v9.2.0 | 1bb278b | +6 条开源 2→6/社区 2→3/工具 4→5（资源 18→24、索引 306）；tesla-api.io 死链判断证伪（DNS 污染非死链）；治本修复 revisions 导航回归；探针 28/28 |
| 13 | 社区与档案资源 + 元数据补全（R11–13 合计 +30~50 条） | complete | v9.3.0 | ade8ed9 | +12 条 community 3→11/开源 6→9/工具 5→6（资源 24→36、索引 318）；Wikipedia 群 8 条（R10「DNS 污染」判定证伪，直连 200 实量）；Reddit 假活空壳+teslaownersonline 软页弃收；R11–13 合计 +26（下沿略低，环境阻塞如实盘点）；探针 35/35 |
| 14 | 资源交互与联动 + 质量节点②（≥15 断言） | complete | v9.4.0 | e8183f3 | 资源↔4 档案互链（.cf-resl 16 深链）+关系图面板行 +aria-live 状态行 +首页入口；质量节点②探针 30/30（八流程）；外链抽样 10/10；verify 9/9 |
| 15 | 设计系统升级（style.css :root tokens，四页样板） | complete | v9.5.0 | 210f443 | :root 令牌 37→113（三层：刻度/语义/焦点）；正文硬编码清零（字号 335/圆角 46/块影 8/描边 7/表面 26/类型色 12 处）；:focus-visible 统一出口；对比度复核修复 #8a857c(3.22)/#9a948b(2.64)/#6f6a62(3.47) 三类小字色共 21 处；公司色标 10 项未动；四页 before/after 各 16 张；探针 69/69 |
| 16 | 首页视觉迭代（封面构图/模块节奏/三入口） | complete | v9.6.0 | 6a0a5ae | 三入口 .btn 行 → .act 编号入口条（data-en 下沉 .act-txt 叶子）；封面照 cover-tag + 内衬双线框；strip-tag → 图上角标；firm-grid 6 等大 → 2 特大（span 2）+4 标准；feature-row 前三条朱红左标线；修复 .firm-tile--xl h3 同特异性被覆盖真缺陷；探针 43/43；像素差异 11.0–28.1%；verify 9/9 |
| 17 | 数据图形工业风（gx-*/cap-*/net-* 三图精修） | complete | v9.7.0 | 66c323d | 纯 CSS +71 行：etype 形状语言（圆方菱圆三角）+芯片 ::before 形状图例、年轴等宽+刻度线、标注层 tabular-nums、图例语法统一、cap/net 点阵网格；数据编码不动（ribbon 线宽=生成器值断言、口径注保留）；探针 34/34；before/after 6 组（390 组一致=清单形态未动的回归证据） |
| 18 | 排版与阅读体验（lr-*/ps-*） | pending | — | — | — |
| 19 | 动效与微交互 + 质量节点③ | pending | — | — | — |
| 20 | 全站验收 + 待发布清单（v10.0.0，不推送） | pending | — | — | — |

状态取值：pending / in_progress / complete / blocked。失败不推进轮次。备注列记本地提交哈希与要点。

## 恢复指引

- 每轮唯一成果提交信息带 `[V9-20 Rxx]` 前缀；工作记录追 加在本文件末尾。每轮原则上一个成果提交+一个账本回填提交。
- 提交了但中断 → 账本行回填后直接进下一轮，不重做工作。
- 账本/一手页变动后必跑：`build-ledger-timeline.py` / `build-search-index.py`（断言同步）/ `build-epub.py`；CHANGELOG 更新后跑 `sync-changelog.py`；提交后 `build-revisions.py` + EPUB 重刷为第二提交内容；最后 `verify.py` 9 项全绿。
- 采料纪律：查不到原文不写；媒体转述两源印证；引语保留英文原文+中文对照；X 帖 snowflake 解码对表；弃收件写入 EXPANSION.md。
- 复杂 Python 改动写成 .py 文件执行（heredoc 中文/引号必失真）；工作区 CRLF/LF 混合，行级比较 rstrip('\r')。

## 三大目标

1. **第一手信息**：R02–R07 回捞 X 帖/访谈/文档/演讲（锚：elonmuskarchive.org 镜像、官方 transcript、SEC EDGAR 等）；R08 事件聚合；R09 语录卡补齐。
2. **开源社区资源板块**：R10–R14 新建 resources.html（单一事实来源 tools/resources-data.py；只收链接+简介+元数据；外链不构成运行时依赖，file:// 离线可读；每条 URL 实访核活）。
3. **美术升级**：R15–R19 设计系统 tokens → 首页 → 数据图形 → 排版 → 动效（深色 #101316 / 暖白 #F3F0E8 / 朱红 #C84032 主基调不变；每轮 before/after 截图入 qa/v9-20/）。

## 第一手信息盘点总表（R09 质量节点①产出，2026-10-01 核数）

### 各类型计数（三口径零漂移核对：页面锚点 = 检索索引 = 生成器断言 = 282）

| 类型 | 页面 | 计数 | 年份覆盖 |
|---|---|---|---|
| 言行实录 | primary.html | 115 | 2002–2026（21 个年份有记录） |
| 一手文档 | documents.html | 18 | 2006–2026（10 个年份有记录） |
| 访谈 | interviews.html | 42 | 2006–2025（15 个年份有记录） |
| X 帖 | x-posts.html | 31 | 2018–2025（8 个年份有记录） |
| 争议深读 | controversy.html | 5 | 五专题（2018–2025） |
| 编年史 | chronicle.html | 53 | 2002–2026 全时段 |
| 财务全景 | finance.html | 4 | 2010/2014/2021/2024 |
| 事件档案 | events.html | 14 | 2008–2024 |
| **合计** | | **282** | 检索索引 282 = 115+18+42+31+5+53+4+14 ✓ |

### 账本逐年分布（115 条；▏=2 条）

| 年 | 条 | | 年 | 条 | | 年 | 条 |
|---|---|---|---|---|---|---|---|
| 2002 | 1 | | 2011 | 1 | | 2020 | 6 ▎▎▎ |
| 2003 | 0 | | 2012 | 2 | | 2021 | 5 ▎▎▏ |
| 2004 | 0 | | 2013 | 4 ▎ | | 2022 | 21 ▎▎▎▎▎▎▎▎▎▎▎ |
| 2005 | 0 | | 2014 | 2 | | 2023 | 7 ▎▎▎▏ |
| 2006 | 2 | | 2015 | 4 ▎ | | 2024 | 7 ▎▎▎▏ |
| 2007 | 0 | | 2016 | 10 ▎▎▎▎▎ | | 2025 | 7 ▎▎▎▏ |
| 2008 | 3 ▎▏ | | 2017 | 8 ▎▎▎▎ | | 2026 | 1 |
| 2009 | 1 | | 2018 | 13 ▎▎▎▎▎▎▏ | | 2019 | 9 ▎▎▎▎▏ |

重心在 2016–2022（68 条，59%）；2003–2005/2007 为零、2009–2011 各 1 条，为最大薄弱区（缺口清单已入 EXPANSION.md）。

### X 帖 / 访谈 / 文档年份覆盖

- **X 帖 31**：2018:2 / 2019:1 / 2020:3 / 2021:4 / 2022:8 / 2023:4 / 2024:6 / 2025:3。镜像库实测下限 2018；2019 仅 1 条为最薄弱年份。
- **访谈 42**：2006:1 / 2008:1 / 2013:1 / 2014:1 / 2015:1 / 2016:3 / 2017:2 / 2018:4 / 2019:5 / 2020:4 / 2021:5 / 2022:3 / 2023:5 / 2024:4 / 2025:2。镜像库 161 场全清单在档（qa/v9-20/round-04/interviews-all.json），保留池 6 场可随时立条。
- **文档 18**：2006:1 / 2010:2 / 2016:1 / 2018:2 / 2021:1 / 2022:6 / 2023:2 / 2024:1 / 2025:1 / 2026:1。2022 年最密（10-K/判决/私有化信等）。

### 语录卡覆盖（v8.9.0 后）

- 卡 103 vs 账本引文块 105，白名单豁免 2 项（e2021-07 媒体转述 / e2025 公司口径）——**结构性豁免，非缺口**。
- 卡逐年分布跟账本一致；e2013 卡（die on Mars，约 2013）本轮补齐，出处待考口径如实双标。

### 缺口清单

见 EXPANSION.md 顶部「R09 质量节点① · 第一手信息缺口清单」节（账本早期年代 / 访谈 2007–2012 / X 帖 ≤2019 / 文档馆五个年代空白，各附候选与重验条件）。

## 第 1 轮工作记录（V8 R10 收尾 + V9-20 基建）— complete（2026-10-01）

- **V8 R10 本地版**：R09 状态核对（已 complete+回填+推送确认 355fc0d，无需补）；口径总核对 250 = 109+14+33+23+5+53+4+9；生成器全家桶十件幂等重跑全过（events/timeline-events/network/company-files/capital/ledger-links/search-index/sync-changelog/revisions/epub）；verify.py 9/9（37 页/索引 250/8.0.0 一致）；版本三件套 → 8.0.0（14 span 替换计数打印）；CHANGELOG 补 v8.0.0 条目；changelog.html 189 条；修订史 179 锚点；EPUB 24 章 201,489 B。V8 账本 R10 行改 complete「本地提交/不推送（用户验收后自行推送）」并附工作记录。成果提交 `24020fe`（含 .gitignore 补 .v9run.lock——首次建锁曾被 `git add -A` 带入提交，已 amend 移除，锁文件从此不入 git）。
- **V9-20 基建**：本账本建立（基线快照 + 20 轮状态表 + 恢复指引）；`.v9run.lock` 锁机制就绪。
- **提交**：V8 R10 本地版成果 `24020fe`（v8.0.0，含 .gitignore 补 .v9run.lock）；R01 成果 `9cc5d46`（v8.1.0，verify 9/9）；本回填为第二提交。
- **下一轮预告**：R02 X 帖回捞 I（2020–2021）——镜像 elonmuskarchive.org 列表页 ?year=2020/2021&page=N&sort=old 全量回捞，候选 COVID 早期表态补充/卖房系列后续/2021 关键节点帖；重验 V8 弃收件 Hertz 对冲（2021-10-26 前后 8 页找 "no contract has been signed yet"）。

## 第 2 轮工作记录（X 帖回捞 I：2020–2021）— complete（2026-10-01）

- **回捞与选帖**：镜像站新增 Agent API（免钥无限流），全量回捞 2020=3,359 帖 / 2021=3,111 帖（tools/v9r02-walk-posts.py，按月切片绕开 1000 条上限；旧 span 分页管线退役，V8 R08「早期覆盖率有限」判断作废）。四卡入册：p2020-04-29 FREE AMERICA NOW / p2021-01-26 Gamestonk!! / p2021-05-05 Starship landing nominal! / **p2021-11-02 Hertz 对冲（V8 弃收件重验成功**——精确短语双命中 x-1455351085170823169，四段全文，same margin 第三句首录，互链账本 e2021-10-25）。四帖 transcript JSON+snowflake 字段存 qa/v9-20/round-02/sources/。
- **甄别**：Bitcoin 暂停购车帖（2021-05-12）镜像三短语 0 命中→弃收留档 EXPANSION；Trump 背书帖→R03 用 Agent API 重验；卖房后续以 p2020-05-01 既有卡注弧线为准未立卡。
- **结构修正**：两处存量年份错位（2020 条错标 2021；2023 条压 p2022-12-18）修正，全站分组与卡序逐卡一致。过程返工一次：集成脚本锚选 p2022-03-26 卡标签（其前即 2022 条）致两卡误入 2022 组，v9r02-fixgroup.py 归位+静态断言。
- **管线**：build-search-index（断言 X 帖 23→27，索引 250→254）/ build-ledger-timeline（109 幂等）/ sync-changelog（191 条）/ 版本三件套 8.1.0→8.2.0（span 14 处打印）/ build-epub（203,255 B）；提交后 build-revisions 179→183 锚点 + EPUB 重刷（第二提交）。
- **验证**：verify.py 9/9；**CDP 探针 24/24**（tools/v9r02-probe.js：渲染/时序/五件套唯一/Permalink 27 对/双语/年份分组/跨页锚真实存在/卡间互链/检索命中/390 零溢出）；node --check 通过；截图 before/after 入 qa/v9-20/round-02/（CDP scrollIntoView 定位三张）。
- **环境坑（供后续轮）**：9227 端口被 aDrive.exe 占用（连接通不响应→CDP 挂死），探针端口改 9333+ 且加 3s 超时；被 timeout 杀掉的 node 遗留孤儿 headless Chrome（占端口+内存缓存旧页面），须全新 user-data-dir+端口避让；headless --screenshot 不认锚点滚动，定位截图走 CDP scrollIntoView+captureScreenshot（tools/v9r02-shot.js）。
- **提交**：成果 `d3c2a3c`（v8.2.0，41 文件）；本回填+revisions+EPUB 为第二提交。
- **下一轮预告**：R03 X 帖回捞 II（2022–2025 深水区）——同管线（Agent API 按年按月全量+精确短语），重点：诉讼相关帖（SEC 后续/特拉华判决表态）、产品节点（Cybertruck 交付日/Grok 各版）、2024-07-13/14 Trump 背书重验；目标 27→31±。

## 第 3 轮工作记录（X 帖回捞 II：2022–2025 深水区）— complete（2026-10-01）

- **回捞与选帖**：四年清单回捞（tools/v9r03-walk-posts.py）得 2022=5,063 帖完整 / 2023=10,985 / 2024=12,000 / 2025=12,000+——**2023–2025 大量月份触及单次 1000 上限**（2024 十二个月全满、12 月仅至 12-12；offset 无效），深水区月内全量浏览不可得，**确立 /agents/search 精确短语检索为目标制主路径**（tools/v9r03-search.py 六组短语全命中、total 精确）。四卡入册：p2023-11-30 Cybertruck 首交付（+同日致谢帖在档）/ p2024-01-30 特拉华判决怒斥（01.31 投票帖+02.01 结果帖在档，弧线闭合于账本 e2024-06-13）/ **p2024-07-13 Trump 背书（V8 弃收件重验成功，计划指定项）**——距巴特勒枪响约 34 分钟（snowflake 解码）/ p2025-07-05 America Party 建党宣言三段全文（06.30 预告+07.04 投票+07.06 纲领逐字在档，07.07 Tesla -7% Reuters）。十帖 transcript 存 qa/v9-20/round-03/sources/（含 search-results.json），日期全部 snowflake 对表=镜像同日。
- **甄别**：Grok 3 发布帖不立卡（账本 e2025-02-18 已覆盖）；Nevada 变体句/碎片回复帖/07-14 帖不立；2025-12 段清单不完整留档（目标制检索不受影响）。EXPANSION 顶部 R03 块+R02 块交叉引用更新。
- **内容增补**：帖墙小结（chapter-summary）补政治维度一句（data-en 同步）；Trump↔America Party 卡间互链；Cybertruck/特拉华卡互链账本 e2023-11-30/e2024-06-13。
- **管线**：build-search-index（断言 X 帖 27→31，索引 254→258）/ build-ledger-timeline（109 幂等）/ sync-changelog（192 条）/ 版本三件套 8.2.0→8.3.0（span 14 处打印）/ build-epub（205,334 B）；提交后 build-revisions 183→187 锚点 + EPUB 重刷（第二提交）。
- **验证**：verify.py 9/9；**CDP 探针 32/32**（tools/v9r03-probe.js，端口 9334：渲染/时序/五件套唯一/Permalink 31 对/四新卡逐字含 Trump 卡整卡相等断言/双语/年份分组四卡归组+2024 组八卡序/卡间互链/跨页锚真实/检索 endorse 命中+Gamestonk 回归/390 零溢出）；node --check 通过；截图 6 张入 qa/v9-20/round-03/（before=HEAD 版 2023 组末尾+四新卡桌面+390）。
- **提交**：成果 `c049610`（v8.3.0，47 文件）；本回填+revisions+EPUB 为第二提交。
- **下一轮预告**：R04 访谈扩充 I——先查重站内 33 条（i2016-09-27/i2022-04-14/i2023-11-29 等在册），候选：Code Conference 2016（Recode 全文稿）/ Everyday Astronaut 星舰专访（2022-04、2023-06）/ Kara Swisher 2018/2020 / Satellite 2020；目标 +4~6 条，逐字源 URL 留档进账本「核实来源留档」节，无把握不立条。

## 第 4 轮工作记录（访谈扩充 I：镜像官方转写批次）— complete（2026-10-01）

- **采料管线升级（本轮最大发现）**：镜像站存在 **interview 类型库**——`/agents/index?type=interviews&list=1` 共 **161 场（2003 起全收录）**，`/agents/transcript/{id}` 直读官方转写全文（text/transcriptSource/date 三字段）。计划候选四场三场直接命中（code-conference-2016-06-01、satellite-2020-keynote-2020-03-09、starbase-tour 三部曲 2021-07-30），另有 all-in-summit-2024-musk 支撑弃收重验。全清单存 qa/v9-20/round-04/interviews-all.json，即 **R05 候选池**（MKBHD 2018、Code 2014/2021、TED 2013、D11 2013 等均在档）。
- **四条入册（33→37，六件套模板克隆+data-en 全配）**：i2016-06-01 Code Conference「one in billions chance…base reality」（本人转发推文 x-738470842695176192 佐证，snowflake 2016-06-02 20:42 UTC）；i2020-03-09 SATELLITE 2020「Zero impact whatsoever…Zero」双零承诺+「fully and rapidly reusable rocket」（BI 双源）；i2021-07-30 EA 星舰基地巡礼三部曲「a factory is underrated and design is overrated」+五步算法完整版（拍摄日锚；EA 官网编辑版变体已注明）；**i2024-09-08 All-In Summit「The government is the DMV at scale」——V8 R07 弃收件重验入册**（原单源笔记→镜像官方转写 53,865 字符，双源成立；日期以镜像锚 09-08 为准）。transcript 证据 7 份存 qa/v9-20/round-04/sources/。
- **甄别与弃收**：Kara Swisher Recode Decode 2018-11-02 **弃收**——镜像转写为主播事后复盘（全程间接转述），Vox/recode.net/web.archive.org 三路本机不可达，重验条件留档 EXPANSION；Code 2016 字幕平面化口径、EA 措辞两版、All-In 日期差异均卡内注明。
- **管线**：build-search-index（断言访谈 33→37，索引 258→262；**附带增强**：ctx 正则放宽兼容 data-en 版式，17 张卡此前恒空的 bg 字段补全——CHANGELOG 已注明理由，口径不变）/ sync-changelog（193 条）/ 版本三件套 8.3.0→8.4.0（span 14 处打印）/ build-epub（207,570 B）；提交后 build-revisions 187→191 锚点 + EPUB 重刷（第二提交）。
- **验证**：verify.py 9/9；**CDP 探针 29/29**（tools/v9r04-probe.js，端口 9335：索引文件级 6 断言/桌面结构+逐字+双语+互链 15 断言/检索 DMV+billions 命中+存量 blackmail 回归/390 零溢出）；node --check 通过；截图 7 张入 qa/v9-20/round-04/（before=33f5b2c 版经 git worktree 独立服务 8767 截取真改前首屏，四新卡桌面定位+390）。
- **环境记录**：web.archive.org 本机持续超时（与 V8 R08 记录一致）；vox.com/recode.net 不可达（Connect Timeout/500）。
- **提交**：成果 `52a03fc`（v8.4.0，52 文件）；本回填+revisions+EPUB 为第二提交。
- **下一轮预告**：R05 访谈扩充 II + Lex 候选消化——必做：把 V8 R06 已核实的 Lex #252（I love humanity / life insurance for life / bang or a whimper）与 #400（free-speech 段）已核实引语立条；候选池：镜像 interview 库 161 场官方转写（MKBHD 2018 计划点名、Code 2014/2021、TED 2013、D11 2013、ARK 2019 等），挑 2~4 场立条；Acquired 播客查官方稿；目标 EXPANSION 候选清零或逐条注明保留原因。

## 第 5 轮工作记录（访谈扩充 II：Lex 候选消化 + 官方转写新批次）— complete（2026-10-01）

- **计划必做项闭环**：V8 R06 留档的 Lex #252/#400 引语全部入册——**i2021-12-28-2**「给生命本身买保险」（life insurance for life 主引语 + foundationally, I love humanity 收束 + bang or a whimper 入编者注；Lex「电视购物」打趣往返在卡）+ **i2023-11-10-2**「言论自由的试金石」（free speech only matters… 01:43:13 + worst thing that happened on Earth today 媒体段 02:02:38，V8 R06 留档段一并落实）。同场多条为站内既有结构（#18/#49/#252/#400 各两条先例），新 id 用 `-2` 后缀。
- **三条新场次入册（镜像 interview 库 transcript 直读，37→42）**：i2013-02-27 TED2013「一枚完全且快速可复用的火箭」（目标宣言+航天飞机十亿美元对比；rapidly and fully reusable 十一年后塔接兑现互链 i2024-10-13）/ i2014-09-25 Code 2014「火星宪法草案」（直接民主/40% 可废法/日落条款；互链 p2025-07-05 America Party 弧线）/ i2018-08-15 MKBHD「我们不花一分钱广告费」（口碑哲学+自付全价购车；2.5 万美元车三年之约未兑现→promises.html#promises-s4）。
- **甄别与考证**：TED2013 官方转写**无**「die on Mars」句——存量无 id 条目维持原标注，新条独立锚定；Acquired 播客镜像 0 条目+官网抽查无本人出场（公司史叙事，非第一手）不适用留档；Lex #438 入候选池；字幕平面化口径三卡注明（Code2014 百分号脱漏编者补回/king of moss 误听未入引语）。
- **候选池收尾（计划验收要求）**：消化 3 场+Lex 留档全部落实；保留池 6 场逐条注明（d11-2013/60min-2012/code-2021/ark-2019/e3-2019/lex-438），161 场全清单在 qa/v9-20/round-04/。
- **管线**：build-search-index（断言访谈 37→42，索引 262→267）/ build-ledger-timeline（109 幂等）/ sync-changelog（194 条）/ 版本三件套 8.4.0→8.5.0（span 14 处打印）/ build-epub（211,383 B）；提交后 build-revisions 191→196 锚点 + EPUB 重刷（第二提交）。
- **验证**：verify.py 9/9；**CDP 探针 29/29**（tools/v9r05-probe.js，端口 9336：文件级 8/桌面结构 4/五卡逐字 5/双语/互链外链真实存在性 4 断言（x-posts#p2025-07-05、promises#promises-s4 等逐条 fetch 验证）/检索 censorship+insurance 命中+DMV 回归/390 零溢出）；node --check 通过；截图 8 张入 qa/v9-20/round-05/（before=worktree @9adff03 独立服务 8767 真改前双视口，after=五新卡桌面定位+R05 批次 390）。
- **提交**：成果 `c7431d1`（v8.5.0，40 文件）；本回填+revisions+EPUB 为第二提交。
- **下一轮预告**：R06 文档馆扩充——先查重站内 14 份（五份 SEC EDGAR 已在册），候选：Tesla 官方博客 Master Plan 系列查缺（Part 3/4 摘录页）、SpaceX 官方更新信（Starship 进展）、SEC 文件（Tesla S-1 2010 关键段、10-K 风险因子摘录、xAI 相关披露若有）；目标 +3~5，每份原文摘录+本站注释+与账本互链。

## 第 6 轮工作记录（文档馆扩充：SpaceX 全员信 + SEC 文件）— complete（2026-10-01）

- **+4 份入册（documents.html 14→18，doc-article 模板逐字克隆）**：**d2010-01-29** Tesla Form S-1（EDGAR 0001193125-10-017054 ds1.htm 直读：商业模式总纲/首份关键人风险因子/累亏 2.364 亿实况三段，互链 e2010-06-29/d2006-08/d2022-02-07）；**d2010-05-04**「Acronyms Seriously Suck」SpaceX 全员信（镜像底本+gist 全文转载逐字一致，Ashlee Vance 传记收录；互链 i2021-07-30 五步算法/d2022-11-16）；**d2021-11-26** Raptor「破产警报」全员信（镜像底本+Newsweek 全文报道关键句逐字一致，逗号异文照录；互链 e2019-09-28/p2024-10-13）；**d2022-02-07** Tesla Form 10-K FY2021「Technoking」风险段（EDGAR 0000950170-22-000796 直读；与 S-1 跨十二年同因子对照，互链 d2010-01-29/d2024-04-29/d2022-10-27）。员工外流文本口径如实标注。
- **采料管线升级（本轮发现）**：镜像站 **email 类型库 47 封**（/agents/index?type=email，全清单存 qa/v9-20/round-06/sources/emails.json）——SpaceX 全员信/OpenAI 诉讼证物/Twitter 收购私信/Tesla 生产冲刺信全在档；email 条目 hasTranscript=false，正文在 /email/{id} 详情页（transcript 端点对 email 返回 Unknown id）。Newsweek 直连超时改走 web reader 通道取回。
- **候选盘点（计划 R06 指定项全部回销）**：Master Plan 系列 Part 1/Deux/3/IV 已全在册无缺；SpaceX「官方更新信」以两封全员信落位（Raptor 信即 Starship 进展警报）；xAI 私营无 SEC 备案（Series E 已在册）。弃收：email 库其余 43 封入候选池（重验条件=逐封双源核验）；Epstein 两信弱相关不收；FY2021 10-K 无 key person life insurance 句（旧句式不可引）。
- **口径同步**：og:description + doc-path 双语十八份版；reading.html 计数；build-search-index 断言 14→18，索引 267→271（109+18+42+31+5+53+4+9）。
- **管线**：build-search-index / build-ledger-timeline（109 幂等）/ sync-changelog（195 条）/ 版本三件套 8.5.0→8.6.0（span 14 处打印）/ build-epub（215,265 B）；提交后 build-revisions 196→200 锚点 + EPUB 重刷（第二提交）。
- **验证**：verify.py 9/9；**CDP 探针 31/31**（tools/v9r06-probe.js，端口 9339：文件级 7/桌面 16（18 卡渲染/五件套/Permalink 18 对/四卡逐字/doc-path 口径/双语/互链目标逐条 fetch 存在性）/检索 4（Technoking/acronyms/Raptor 命中+wild swings 回归）/390 零溢出两项）；node --check 通过。首轮 28/31 三处失败均为探针口径（10-K 卡单摘录块不符多段先例→拆两段内容不变；Raptor bankruptcy 双词超 q 字段→单词；回归词换 wild swings），修复后全绿，迭代记录在 RECORD.md。
- **证据**：qa/v9-20/round-06/（四张截图 documents-desktop/mobile + d2010/d2021 锚点视图 + probe.txt + RECORD.md + sources/ 五件：镜像页×2、gist、EDGAR 摘录、Newsweek 摘要、email 全清单）。
- **提交**：成果 `f319ee9`（v8.6.0）；本回填+revisions+EPUB 为第二提交。
- **下一轮预告**：R07 官方演讲扩充——先查重 V8 R09 已收 6 条；候选：Starship 更新会系列（2019-09/2020-09/2021-02/2022-02 择逐字可得者）、Neuralink demo（2020-08/2021-04/2024-01）、Tesla AI Day 2021/2022；账本 +4~6 条；源=官方转播字幕/Numbski 等逐字站；镜像 keynote 库 60 场（type=keynote）与 speech 库 21 场是主矿。

## 核实来源留档（R07）

六场官方演讲（镜像 elonmuskarchive.org /video/{id} 详情页全场逐字转写；官方 YouTube 源字段在册；全文存 qa/v9-20/round-07/sources/）：
- **COP21 索邦演讲**（2015-12-02，1,632 词）：源 YouTube cousinHub 转播频道（youtube.com/watch?v=v3AmtjqqVvo）——非官方频道，转写与公开录像互证收录，ps-src 已注明
- **BFR 环月旅客发布会**（2018-09-17，Musk 3,204 词 + 前田 1,263 词）：23ABC News 直播录像（youtube.com/watch?v=n5EqUKNCGd0）
- **Tesla Autonomy Day**（2019-04-22，Musk 8,270 词全场）：Tesla 官方频道（youtube.com/watch?v=Ucp0TTmvqOE，13,940 秒）
- **Tesla AI Day 2022**（2022-09-30，Musk 6,458 词）：Tesla 官方频道（youtube.com/watch?v=ODSJsviD_SU）
- **Neuralink Show and Tell**（2022-11-30，Musk 4,716 词）：Neuralink 官方频道（youtube.com/watch?v=YreDYmXTYi4）
- **SpaceX Starship Update at Starbase**（镜像归档锚 2024-03-18，Musk 7,117 词单人演讲）：The Launch Pad 转播（youtube.com/watch?v=TUQzeUaGxBI）；日期口径=镜像归档锚照录，内容指向 IFT-3（2024-03-14）前夜展望，卡内双注
- **查重勘定**：We,Robot（e2024-10-10）/ Investor Day 2023（e2023-03-01）/ Battery Day（e2020-09-22）/ Cybertruck 交付（e2023-11-30）/ Boring 隧道（e2018-12-18）/ Semi·Roadster（e2017-11-16）/ Falcon Heavy（e2018-02-06）已在册不重复；**AI Day 2021（e2021-08 已有媒体口径条目）官方逐字留档待引语升级**
- **ASR 口径**：六场均为自动听写转写——Yusaku 误作 Usage、Falcon 9 误作 Belkin、Neuralink 分词 neural link；引语句均避开误差词或照录并卡内注明

## 第 7 轮工作记录（官方演讲扩充：镜像 keynote/speech 全档转写批次）— complete（2026-10-01）

- **+6 条入册（primary.html 109→115，四段五件套模板逐字克隆+data-en 全配）**：e2015-12-02 COP21「史上最愚蠢的实验」（碳税药方+NYC ±5 度对照，互链 e2015-04-30）/ e2018-09-17 BFR 前田环月「这很危险，可不是公园散步」（dearMoon 2024 取消入后续，互链 e2017-09-29/e2019-09-28）/ e2019-04-22 Autonomy Day「LIDAR is a fool's errand…doomed」（芯片冗余论+2020 承诺滑票注 promises.html）/ e2022-09-30 AI Day 2022「去年那就是个穿机器人服装的人」（Bumble C 真机+丰裕独白，互链 e2021-08）/ e2022-11-30 Neuralink S&T「六个月内首例人体植入」（Sake 意念打字+AI 对冲动机，兑现注 e2024-01-29，互链 e2020-08-28/e2021-04-09）/ e2024-03-18 Starbase「总有一天我们会真正在火星上安家」（96 发/年+八年火星钟，互链 e2024-10-13/p2024-10-13）。页内互链 13 处全部实存。
- **quotes.html +6 卡（96→102）**；index.html 计数 109→115 ×3 处（中英）；og 等历史条目不动。
- **采料管线（本轮新建）**：镜像 video 库 keynote 60 场+speech 21 场全部 hasTranscript（100% 覆盖）；抽取器三版迭代（v1/v2 逐词 span 截断乱序弃用，**v3 按 button 块整体剥标签保词序定稿**）——教训=抽前必须目检 DOM 实构；PowerShell 内联 $_ 被 bash 吞（.ps1 文件解决，记忆坑复验）；探针冷加载 1.8s 未完成致 24/18 假红（ps-row=0 时 every() 恒真），改轮询等待后 42/42——**后续轮探针导航后应轮询关键计数**。
- **甄别与候选池（EXPANSION.md R07 块详录）**：AI Day 2021 官方逐字在档（555 词独白）但账本已有媒体口径条目不重复立条；Starship 2025-05-29（4,836 词）/ Wisconsin town hall（12,095 词，政治类）/ xai-all-hands-2026 等入候选池；SpaceX IPO 敲钟 9 词不立；81 场全清单 JSON 存 qa。
- **管线**：build-ledger-timeline（115 节点）/ build-search-index（断言言行实录 109→115，索引 271→277）/ sync-changelog（196 条）/ 版本三件套 8.6.0→8.7.0（14 页 span 打印在案）/ build-epub（219,675 B）；提交后 build-revisions 200→206 锚点 + EPUB 重刷（第二提交）。
- **验证**：verify.py 9/9；node --check 通过；**CDP 探针 42/42**（tools/v9r07-probe.js，端口 9341：文件级 9/桌面结构+逐字+双语+口径注 19/互链与锚完整性 7/quotes 三断言/index 计数 2/检索命中 4+回归/390 零溢出 3）；截图 8 张入 qa/v9-20/round-07/（before=worktree@c556a2c 独立服务 8767 双视口，after=四新卡桌面定位+quotes 卡区+Neuralink 390）。
- **提交**：成果 `c10775e`（v8.7.0，qa sources 原始页快照 14MB 未入库——transcript 全文 txt+清单 JSON+官方源 tsv 已足证，抽取器可随时重现）；本回填+revisions+EPUB 为第二提交。
- **下一轮预告**：R08 事件档案聚合扩容——tools/events-data.py EVENTS 追加（etype 五类枚举/materials.kind 枚举/validate()），把 V8/V9 新材料聚合成 4~6 个新事件档案（9→14±）；重跑 build-events/build-timeline-events/build-network/build-company-files/build-capital/build-ledger-links/build-search-index；口径红线=时间轴独立记录数=索引一手材料−被吸收数−events.html 档案记录（防 160 漂移重演，探针断言 TIMELINE_V7.meta）；建档卡深链全在册（fetch 逐条验证）。

## 第 8 轮工作记录（事件档案聚合扩容：V8/V9 新材料归档，9→14）— complete（2026-10-01）

- **五个新档案入册（events-data.py 9→14，材料关联 37→59，逐字引语 18→24；全部由已入册材料聚合，零新增未核实事实）**：
  e2010-06-29 Tesla IPO（S-1 总纲+首份关键人风险因子+Q1 2013 首盈利+d2022-02-07「Technoking」十二年对照；账本当日无本人逐字原话，档案如实引 SEC 文件并注明公司文件口径）/
  e2021-10-25 万亿市值日（账本+p2021-11-02 same margin 帖+chronicle c2021-10-25 三方同框；snowflake 解码 UTC 2021.11.02 01:48=美国 11.01 晚双注）/
  e2021-11-26 Raptor 危机与星舰翻身（环月承诺→不锈钢转向→SN15 着陆→破产警报信→Starbase 演讲五材料；outcome 如实：每两周一飞未兑现/破产未发生/dearMoon 取消）/
  e2024-01-29 Neuralink 首例人体植入（三只小猪→MindPong→「大概六个月」→Telepathy 官宣五材料；probably ≠ 承诺书，实际约十四个月口径在案）/
  e2019-04-22 Autonomy Day→Optimus（LIDAR doomed→AI Day 2021→Q4 2021 排位→AI Day 2022 真机+promises 对账 feature；related 首链 controversy.html#autopilot）。
- **枚举扩充**：KIND_LABELS 新增 chronicle（编年史条目）——validate() 与 build-events.py 渲染同步通过，无 CSS 变更（非 ledger 类型共用默认样式）。
- **口径红线闭环（防 160 漂移重演）**：索引 277→282（事件档案断言 len(ED.EVENTS) 自动 9→14）；吸收 18→39（新档案 e2010-06-29=4/e2021-10-25=3/e2021-11-26=5/e2024-01-29=5/e2019-04-22=4）；独立记录 250→229；**282=14 档案记录+39 吸收+229 独立**，探针断言在案；建档卡 18→23 处。
- **选题边界留档**：xAI/Grok 线仅 2 条索引材料（e2023-07-12+p2023-11-04）未达聚合门槛不立档；Hertz 并入万亿市值日档案；Gamestonk 单材料不立。后续若 Grok 产品线材料增多可重启。
- **管线**：build-events/build-timeline-events/build-network/build-company-files/build-capital/build-ledger-links（23 处）/build-search-index（282）/sync-changelog（197 条）/版本三件套 8.7.0→8.8.0（VERSION+app.js+14 页 span，替换计数打印在案）/build-epub（220,559 B）。
- **验证**：verify.py 9/9（37 页/索引 282）；node --check 通过；**CDP 探针 35/35**（tools/v9r08-probe.js，端口 9351：文件级口径 11/events 结构+逐字 10/互链深链 4/timeline 口径 4/建档卡 2/检索 3/390 零溢出 2；events.html 14/14 深链锚全在册）；截图 3 张入 qa/v9-20/round-08/。
- **探针插曲**：TIMELINE_V7 meta 解析被非贪婪正则截断→改 indexOf/lastIndexOf 整体解析；events 卡选择器先假设后失配（.ev-sum→实构 .ev-summary、引语块实构 blockquote.lr-quote）——「先目检 DOM 再写断言」教训二次验证。
- **提交**：成果 `7a55ca9`（v8.8.0）；本回填+revisions+EPUB 重刷为第二提交。
- **下一轮预告**：R09 语录卡补齐+质量节点①——quotes.html 补卡至与账本引文块全覆盖（当前 102 卡 vs 账本引文块 105 个，白名单豁免 3 项；R06 文档页引语与 R08 档案引语不在账本引文块口径内）；verify.py 第 6 项白名单同步更新（改断言须在 CHANGELOG 说明理由并保留原约束精神）；产出「第一手信息盘点总表」入账本：各类型计数、时间覆盖、缺口清单（写回 EXPANSION 作为后续候选池）；质量节点①验收=三口径（页面/索引/生成器）零漂移+主路径探针全过。

## 第 9 轮工作记录（语录卡补齐 + 质量节点①）— complete（2026-10-01）

- **e2013 立卡**：quotes.html qs-grid 时间序补入 2013（约）卡（e2012-06-22 与 e2013-05-08 之间），语录卡 102→103；卡文与账本 e2013 逐字一致（“I would like to die on Mars. Just not on impact.”），日期/来源如实双标「约 2013 · 广泛征引」（R05 甄别留档：真实出处待考，TED2013 官方转写无此句——本卡锚账本口径不杜撰出处）；格言轮播五句与「待考」注记维持原状。至此账本引文块全覆盖收口：103 卡 + 2 结构性豁免 = 105 块。
- **verify.py 第 6 项白名单收窄（3→2，口径收严非放宽）**：e2013 移出（已立卡）；e2021-07（The Next Web 第三人称转述非本人逐字）/e2025（Boring 官网项目页统计口径非本人引语）保留豁免，注释更新理由，原约束精神（有引文必上卡/卡必有引文）不变，CHANGELOG 已按纪律说明。
- **盘点总表入账本**（本文件独立节）：八类型计数表（282=115+18+42+31+5+53+4+14）/账本逐年分布（重心 2016–2022 占 59%；2003–2005/2007 零、2009–2011 各 1）/X 帖·访谈·文档分类型年份覆盖/语录卡覆盖状态。
- **缺口清单入 EXPANSION.md**（顶部 R09 节）：账本早期年代稀薄、访谈 2007–2012 断档（保留池 6 场可立）、X 帖 ≤2019 未探（镜像下限 2018）、文档馆五个年代空白，各附候选与重验条件——后续轮候选池。
- **质量节点① · 三口径零漂移**：页面锚点=索引=生成器断言 282 一致；生成器全家桶幂等重跑（network 报幂等/search-index 282 断言全对/ledger-links 23 处）；verify 9/9（37 页/282/103 卡+2 豁免/EPUB 新鲜）。
- **管线**：sync-changelog（198 条）/版本三件套 8.8.0→8.9.0（VERSION+app.js+14 页 span，替换计数打印在案）/build-epub（220,597 B）。
- **验证**：**CDP 探针 25/25**（tools/v9r09-probe.js，端口 9353：文件级口径 7/主路径五页 index→quotes→primary→timeline→events→search 共 14/390 零溢出+新卡渲染 2）；node --check 通过；截图 3 张入 qa/v9-20/round-09/（before=stash 法取 HEAD 版）。
- **探针修正记录**：①「卡序与账本序一致」文件级断言过强——存量 qs-grid 卡序与账本序在 2017/2022 年代存在多处历史差异（verify 只查集合差不查顺序），收敛为「e2013 插入点局部时序」断言；存量卡序不动（如需全量对齐属独立轮次）。②pt-dot 时间轴条在 primary.html 页内（verify 第 5 项即查 primary），非 timeline.html——断言挪位后过。
- **提交**：成果 `efe7bec`（v8.9.0，24 文件）；本回填+revisions（206 锚点幂等）+EPUB 重刷为第二提交。
- **下一轮预告**：R10 资源页基建——新建 tools/resources-data.py（字段：url/name(zh,en)/desc(zh,en)/category/语言/活跃度/许可/收录理由/关联公司/核活日期；内置 validate 拒生成）+ tools/build-resources.py（幂等生成 resources.html：lr-hero 风格页头+分类筛选芯片+无 JS 完整可读+≤760 单列+print 保留）；site-nav.py「资料」组注册重注入全站；build-search-index 增类型断言；首批种子 8–12 条每类 1–2 条打通管线；验收=verify 9/9+资源页 CDP 探针 ≥10 断言。

## 第 10 轮工作记录（资源页基建）— complete（2026-10-01）

- **数据单一事实来源 tools/resources-data.py**：字段 url/name(zh,en)/desc(zh,en)/category/语言/活跃度（维护中|停更|存档）/许可/收录理由/关联公司/核活日期 + gh 实测与 note 可选；validate() 全字段强制（url 须 http(s)、双语完整、category∈四类枚举、companies ⊆ 检索实体词表、核活日期必填），不过拒生成。首批种子 10 条：官方与标准 2（SEC EDGAR Tesla 文件 / Tesla 官方开源 vehicle-command）· 开源项目 2（Teslamate ★9,061 / xAI Grok-1 权重 ★52,239）· 社区与档案 2（Elon Musk Archive / Wait But Why Neuralink 长文）· 工具与数据 4（Flight Club / Next Spaceflight / Launch Library 2 / starlink.sx）。**工具类 4 条为当批核活清单全量入库**，超「每类 1~2」软指引、在 8~12 硬区间内（CHANGELOG/账本/EXPANSION 三处注明）。
- **核活实测**：每条 URL 于 2026-10-01 实测（浏览器 UA curl → 失败则 WebFetch → GitHub 走 api.github.com 串行）；SEC 须合规 UA（含联系邮箱）才 200（浏览器 UA 403）；**grok 仓库已 301 迁移 grok-1**（API 跟随后建档，2024-08 后无提交属权重一次性发布，卡内注记「停更≠下线」）。**本机不可核活 7 条留档 EXPANSION.md R10 块**（tesla.com/spacex.com/developer.tesla.com 反爬 403、neuralink.com 000、en.wikipedia.org DNS 污染、tesla-api.io DNS 失效疑似死链、openai.com 未测），R11–R13 按重验条件逐条处理，未编造任何一条。
- **生成器 tools/build-resources.py**：幂等生成第 38 页 resources.html——lr-hero 页头 + 分类筛选芯片（复用 gx-fchip，min-height 28px 由既有移动层继承）+ 四分类清单 + 逐条详情字段行（网址/分类徽标/语言/活跃度徽标/许可/关联公司/GitHub 实测/核活码/口径备注/收录理由）；**无 JS 完整可读**（芯片惰性、全量可见，筛选仅做分类节显隐）；≤640 字段行纵向堆叠；print 隐藏筛选保留清单。rs-* 组件层 ~55 行入 style.css（**无新增过渡，reduced-motion 免复核**）。
- **管线**：site-nav.py「资料」组注册 resources.html，37 页重注入（探针实测入站导航 38/38 页）；build-search-index 增「社区资源」类型（companies 直接用 COMPANIES_VOCAB，检索按公司过滤即插即用；d=核活年月沉底属预期），索引 282→292；search.html 类型按钮 +1（共 10 枚）；**verify.py 第 4 项断言扩展 +rs-item 锚点计数**（原约束原样保留，同 V7-19 R15 事件档案先例，CHANGELOG 已说明理由）；sync-changelog 199 条；版本三件套 8.9.0→8.10.0（span 14 处打印在案，resources.html 以 8.10.0 直接建档）；build-epub（220,597 B）。
- **验证**：verify.py 9/9（38 页/索引 292）；node --check 通过；**CDP 探针 27/27**（tools/v9r10-probe.js，端口 9354 全新 profile：文件级 6/结构 8/筛选 2/双语 4/**无 JS 2（Emulation.setScriptExecutionDisabled 禁脚本实测）**/检索联动 3（q=Teslamate 命中类型社区资源、type=社区资源 URL 参数+深链）/390 零溢出 2）；截图 2 张入 qa/v9-20/round-10/（桌面芯片区+390 Teslamate 卡）；核活留档 sources/liveness.md；验收记录 ACCEPTANCE.md。
- **探针修正记录**：首跑 26/27——唯一失败为探针自身断言计数写错（类型按钮误写 11 枚，实际原 9+1=10），页面正确，修正断言后全绿。
- **提交**：成果 `fdf366e`（v8.10.0，56 文件）；本回填+revisions+EPUB 重刷为第二提交。
- **下一轮预告**：R11 官方与标准类资源——目标 tesla.com 专利开放博文落地页 / NACS 官方页 / SpaceX 官网 Starship/Falcon 页 / Tesla 车主手册与 API 文档 / OpenAI 早期博客 / Neuralink patient registry（R10 留档的反爬项重点重验：换 UA/代理路径或降表述留档）；每条 curl/WebFetch 核活并记录 http_code。

## 第 11 轮工作记录（官方与标准类资源）— complete（2026-10-01）

- **+8 条入册（official 2→10，全站资源 10→18，索引 292→300）**：SpaceX 官网三页（r-spacex-starship / r-spacex-falcon9 / r-spacex-updates）/ Tesla 官方开发者门户 Fleet API（r-tesla-fleet-api）/ Neuralink 患者登记（r-neuralink-registry）/ OpenAI 2015 官宣文 Introducing OpenAI（r-openai-2015，联合主席含马斯克——AI 弧线官方起点，活动度如实标「停更」+note 注明历史定稿）/ xAI 官网（r-xai-official）/ The Boring Company 官网（r-boringcompany-official，直连 200 无反爬注记）。COMPANIES_VOCAB 增 OpenAI 实体（仅资源条目，CO_MAP 透传进检索「按公司过滤」，存量 282 条实体推断零扰动）。
- **核活三路法（本轮方法论沉淀）**：浏览器 UA curl → WebFetch → 服务端读取器（web_reader 当日恢复可用）逐级复核。curl 直连：tesla.com/spacex.com/openai.com 全 403（Akamai 反爬）、neuralink.com 连接重置（WinError 10054）、x.ai 超时（WinError 10060）；服务端读取器对 7 条核活成功并取得官方 meta/正文——**卡内 note 逐条如实注明核活路径，不冒充直连**；核活全表存 qa/v9-20/round-11/sources/liveness.md（curl 层原始 liveness-r11.json 同目录）。
- **弃收留档（宁缺毋滥，EXPANSION.md R11 块）**：①SAE J3400（NACS 标准化文本）——WebSearch 确认标准存在（J3400/2_202504 尺寸 / J3400/1 适配器安全）但 sae.org 全站 JS 壳，构造 URL curl 200 属软页不可信、connect.sae.org 落地页猜测 404，内容级证据不可得，弃收（重验条件=用户环境实访定位产品页）；②**tesla.com 全站三路均被 Akamai 拦**（All Our Patent 博文 //nacs、/impact、/ownersmanuals 四 URL 全试），维持 R10 留档，重验条件=用户环境实访或代理。R10 反爬留档项除 tesla.com 外全部重验成功入册。
- **附带修复（R10 导航回归）**：R10 第二提交时 build-revisions.py 重建 revisions.html 丢失「资料」组链接（R10 探针在提交前跑、回归未暴露，本轮探针「38/38 入站导航」断言捕获）——site-nav.py 全站重注入恢复 38/38，断言留档防复发。
- **管线**：build-resources（18 条幂等重建）/ build-search-index（300）/ sync-changelog（200 条）/ 版本三件套 8.10.0→9.1.0（**15 页 span**——原 14 页+resources.html，替换计数打印在案）/ build-epub（220,597 B）；提交后 build-revisions（206 幂等，资源页不在修订追踪口径内属预期）+ EPUB 重刷（第二提交）。
- **验证**：verify.py 9/9（38 页/索引 300；EPUB 新鲜度修复后复跑两轮均绿）；node --check 通过；**CDP 探针 30/30**（tools/v9r11-probe.js，端口 9355 全新 profile：文件级 9（含 official 节 10 条、反爬注记 7 处、OpenAI 实体唯一、38/38 导航）/结构 9（OpenAI 卡实体+停更徽标+历史定稿注记、Starship 卡核活路径注记、外链三抽）/筛选 2/双语 3/无 JS 2/检索联动 4（q=OpenAI 命中+公司过滤按钮出现+过滤后保留+q=Starship 命中）/390 零溢出 2）；截图 2 张入 qa/v9-20/round-11/。
- **探针修正记录**：首跑 28/30——①「official 节 10 条」文件级断言用 data-cat 切分被筛选芯片同名属性干扰（页面 DOM 断言同口径已过，页面正确）改用 section id 定界；②「38/38 导航」为真回归（见上）。两处均非页面缺陷掩盖。
- **提交**：成果 `84ec1e8`（v9.1.0，29 文件）；本回填+revisions+EPUB 重刷为第二提交。
- **下一轮预告**：R12 开源项目资源——Tesla API 生态（tesla-api.io 重验：DNS ENOTFOUND 疑似死链，独立 DNS 确认后按纪律 B 标「存档」或弃收；Tessie、Tesla API 社区文档择主要）、Starlink 追踪 GitHub 观测项目、r/SpaceX 社区百科（编年史/统计帖）、火箭发射数据工具补缺（Flight Club/Next Spaceflight/LL2 已在册勿重）；GitHub 项目记 stars+最近提交年（api.github.com 无认证串行）；社区资源记性质（非官方）。

## 第 12 轮工作记录（开源项目资源）— complete（2026-10-01）

- **+6 条入册（opensource 2→6 / community 2→3 / tools 4→5，全站资源 18→24，索引 300→306）**：timdorr/tesla-api（2,065★ MIT，2026-03 活跃，近十年非官方 API 文档+Ruby gem）/ r-spacex/SpaceX-API（10,912★ Apache-2.0，**维护者 archived=true，2024-08 停更**——仓库态如实标「存档」，线上服务可用性不在断言范围）/ sparky8512/starlink-grpc-tools（710★ Unlicense，2026-09 活跃，星链终端 gRPC 遥测自采）/ tesla-api.io（社区文档站，2024-01 起停更）/ r/SpaceX 社区维基（发射编年史与 FAQ）/ Tessie（商业托管路线代表，与 Teslamate 自托管互为两端）。
- **重要重验：R10「tesla-api.io 疑似死链」判断证伪**——本机 resolver NXDOMAIN（R10 同结果）→ 独立解析尝试 8.8.8.8/1.1.1.1 UDP **全部被墙超时（本机独立 DNS 不可行）**→ dns.google DoH 直连亦超时 → **服务端读取器核活 HTTP 200 且站点在线**（自注 2024-01 起弃用由官方文档接管，deprecated ≠ 下线）。结论=本地运营商 DNS 污染（同 wikipedia 污染机制）非死链，按「停更」收录，判定全过程卡内注明。**教训：本机 DNS 对 .io 域名的 NXDOMAIN 不可作死链证据（污染前科两例），死链判定必须服务端路径交叉确认。**
- **择主要甄别**：GitHub 星数搜索混入同名无关项目——sgayou/subaru-starlink-research（**斯巴鲁**车载 StarLink 同名不同司）、Look4Sat（通用卫星追踪）、SmoothWAN（通用组网）均排除留档 EXPANSION R12 块。
- **治本修复 revisions.html 导航回归（R10/R11 连续两轮同处回归的根因）**：build-revisions.py 内联模板从不包含 site-nav 报头，每次重跑冲掉导航注入——本轮模板内嵌 `build_masthead('revisions.html')` + app.js（导航单一来源原则），重跑不再回归；探针新增「revisions.html 导航在册（含 resources 链接+site-nav+app.js）」文件级断言防复发，本轮两次重跑实测导航保留。
- **管线**：build-resources（24 条幂等重建）/ build-search-index（306）/ sync-changelog（201 条）/ 版本三件套 9.1.0→9.2.0（15 页 span 打印在案）/ build-epub（220,597 B）；提交后 build-revisions（206 幂等+导航在册验证）+ EPUB 重刷（第二提交）。
- **验证**：verify.py 9/9（38 页/索引 306）；node --check 通过；**CDP 探针 28/28**（tools/v9r12-probe.js，端口 9356 全新 profile：文件级 9（含治本断言）/结构 9（tesla-api.io 停更徽标+死链证伪注记、SpaceX-API 存档徽标+★10,912、starlink-grpc-tools ★710+Unlicense、Tessie 非官方口径）/筛选 2/双语 3/无 JS 1/检索联动 3（q=Tessie 命中、q=starlink 新旧双命中、q=发射数据 中文简介命中）/390 零溢出 2）；截图 2 张入 qa/v9-20/round-12/。
- **探针插曲**：首跑 17 项过即中断——qa/v9-20/round-12/ 目录不存在致截图写失败（mkdir 后重跑全绿），非页面缺陷。
- **提交**：成果 `1bb278b`（v9.2.0，27 文件）；本回填+revisions+EPUB 重刷为第二提交。
- **下一轮预告**：R13 社区与档案资源+元数据补全——elonmuskarchive.org 已在册（R10），候选：en.wikipedia.org 相关条目（DNS 污染项——本轮 tesla-api.io 教训表明可先试服务端读取器核活）、Wait But Why 已在册、媒体档案库（Reuters/AP 专题页择要）、Reddit 之外的社区档案（r/teslamotors 百科等择主要）；R11–R13 合计目标 +30~50 条（当前 +14，R13 需再收 6~10 条并补齐元数据）。

## 第 13 轮工作记录（社区与档案资源 + 元数据补全）— complete（2026-10-01）

- **+12 条入册（community 3→11 / opensource 6→9 / tools 5→6，全站资源 24→36，索引 306→318）**：Wikipedia 条目群 8 条（Elon Musk / SpaceX / Tesla, Inc. / Starship / Acquisition of Twitter by Elon Musk / List of SpaceX launches / Grok (chatbot) / Neuralink——全部以「公共参照系·二手」口径收录，卡内逐条注明非一手）/ Tesla JSON API 非官方文档（tesla-api.timdorr.com，与 R12 的 timdorr 仓库成对收：仓库管代码、本页管文档）/ TeslaPy（417★ MIT 2026-07 活跃）/ Powerwall 2 本地网关 API 文档（290★ Apache-2.0 2024-10 停更）/ Jonathan McDowell 太空档案（planet4589.org，独立学者口径）。**R11–R13 合计 +26 条**（计划软目标 +30~50 区间下沿略低，原因见下）。
- **重要重验：R10「en.wikipedia.org DNS 污染不可达」判定证伪**——R10 留档记解析被污染至 31.13.88.26 故与本机 .io 污染前科并列为不可核活项；本轮实测直连 **200 且内容为真**（Elon_Musk 页 2.68 MB、title「Elon Musk - Wikipedia」、正文 525 处命中；SpaceX 1.53 MB；Twitter 页正常 301 至 X (social network) 2.08 MB）。curl `%{remote_ip}` 返回 127.0.0.1（本机存在代理/hosts 接管路径），**当轮污染判断已被环境变化推翻**，8 条全部入册，卡内 note 记载判定全过程与所载 http 口径。**教训：本机 DNS 判定结论有时效性，须定期重验（与 R12 tesla-api.io 证伪同类）。**
- **Reddit 社区档案「假活」甄别（宁缺毋滥，本轮不收）**：www/old.reddit.com 的 r/teslamotors 与 r/SpaceXLounge wiki **直连返回 200 但响应体仅 8.4 KB JS 空壳**（`<title>Reddit</title>`，正文 0），WebFetch 服务端复验同为空壳，`…/wiki/index.json` API 403——不满足纪律 B「内容到手」门槛，本轮不收（R12 收 r/SpaceX wiki 的前提是服务端读取器取得正文；本轮服务端路径对两站亦为空壳）。留档 EXPANSION，重验条件=服务端读取器能取正文或 Reddit 放开 JSON API。
- **软页甄别**：teslaownersonline.com 返回 **HTTP 202 + `window.POW_CHALLENGE_DATA` JS proof-of-work 挑战**（bot 拦截软页），非真实内容，弃收；www.teslamotorsclub.com 000 留档。spaceflightnow.com / apnews.com / reuters.com（401）/ nytimes.com / science.org / sec.gov 查询页（403）全留档；web.archive.org 000（WebFetch 亦失败）留档。
- **大型通讯社本机全阻塞（R13 未完成项，如实盘点）**：计划 R13 点名的「Reuters/AP 专题页择要」因 reuters 401 / apnews 403 未落，属**环境阻塞非选题放弃**，重验条件=用户环境浏览器实访或代理路径。媒体 hub 页（teslarati / electrek / arstechnica / nasaspaceflight / everydayastronaut / space.com / theverge / techcrunch / cnbc / BBC，本轮实测全 200 真内容）入候选池留 R14 起按检索联动需要择要。
- **R11–R13 合计 +26 条下沿略低的原因**：非官方采料池中可核活的高质量条目因三重环境阻塞而耗尽——①大通讯社与机构站 401/403；②Internet Archive 000；③Reddit 空壳。守「宁缺毋滥」不灌水，如实收 26 条；用户环境若放宽，R14 起媒体档案类预计可再补 10~20 条。
- **治本保持验证**：R12 对 build-revisions 模板内嵌 masthead 的治本修复本轮**首次跨轮实测沿用成功**——本轮 build-revisions 重跑后 revisions.html 仍含 site-nav + resources 链接 + app.js（连续两轮回归问题未复现），探针保留「revisions.html 导航在册」防复发断言。
- **管线**：build-resources（36 条幂等重建）/ build-search-index（318）/ sync-changelog（202 条）/ build-ledger-links（23 处）/ build-events（14 事件）/ build-timeline-events（265 独立记录+39 吸收）/ build-network（幂等）/ build-company-files（4 档案）/ build-capital（幂等）/ 版本三件套 9.2.0→9.3.0（VERSION+app.js+15 页 span 打印在案）/ build-epub（223,126 B）。
- **验证**：verify.py 9/9（38 页 / 索引 318 / 版本 9.3.0 / 语录卡 103+2 豁免 / 修订史 206 / EPUB 新鲜）；node --check 全过；**CDP 探针 35/35**（tools/v9r13-probe.js，端口 9357 全新 profile：文件级 13（含 revisions 治本保持 + Reddit 假活不收 + R12 r/SpaceX wiki 保留回归）/结构 9（wikipedia 8 卡在 community 节、TeslaPy ★417、Powerwall ★290 停更、planet4589 无 gh 行、外链逐字）/筛选 3/双语 4/无 JS 1/检索联动 3（维基百科·TeslaPy·Grok 各命中）/390 零溢出 2）；截图 2 张入 qa/v9-20/round-13/。
- **探针修正记录（1 项，非页面缺陷）**：首跑 33/34——断言「页内无 reddit 条目 URL」用宽松正则 `https://[^"]*reddit\.com` 匹配，误命中 R12 已核活收录的 r/SpaceX 社区维基（其 URL 本就含 reddit.com，属正确保留非误收）。收敛为两条精确断言（teslamotors/SpaceXLounge 假活不在页 + R12 r/SpaceX wiki 保留）后 35/35 全绿。**教训：排除类断言须锚定具体目标项，勿用宽泛域名正则。**
- **提交**：成果 `ade8ed9`（v9.3.0，30 文件）；本回填+revisions（206 幂等+导航保持验证）+EPUB 重刷为第二提交。
- **下一轮预告**：R14 资源交互与联动+质量节点②——分类筛选 aria-live 状态行（R10 已设 rs-status，本轮补 aria-live）；资源↔公司档案/事件互链（companies 面板与 company-files 加「相关社区资源」行）；首页资料入口；检索命中（含类型筛选）；质量节点②验收=资源页全流程探针（筛选/清除/跳转/双语/无 JS/390/file://）≥15 断言 + 外链抽样 10 条核活 + verify 9/9。

## 第 14 轮工作记录（资源交互与联动 + 质量节点②）— complete（2026-10-01）

- **本轮定性**：资源板块从「有」（R10–R13 建成并扩容至 36 条）到「通」（接入站内导航网络）。无新增条目，资源仍 36 条 / 索引 318。
- **资源↔公司档案互链（单一事实来源驱动，零内容复制）**：resources-data.py 新增 `resources_for_company(company_name, limit)` 查询接口（按 companies 实体匹配、category 序稳定排序、「综合」类不参与匹配以防泛条污染每家档案）；build-company-files.py 新增 `COMPANY_TO_VOCAB`（档案 id→实体词表名：tesla→Tesla / spacex→SpaceX / x→X / Twitter / xai→xAI）并引入 RD，为 4 份完整档案各渲染「相关社区资源」节（`.cf-resl`，共 **16 条深链**，每公司上限 6：Tesla 6 / SpaceX 6 / xAI 3 / X 1）；同时向 companies-data.js 的 companies 注入 `resources: [{id,name}]` 字段。
- **公司关系图面板联动**：app.js 的 `netRender` 增「相关社区资源（N）」段（读 `c.resources`，中英双语 COMMUNITY RESOURCES）——点选图上节点即列出该公司相关社区资源并深链回资源页。
- **可访问性**：build-resources.py 模板源改，`#rs-status` 加 `role="status" aria-live="polite"`（切分类时读屏即时播报「显示 N 条资源 · 分类」；无脚本环境该行静态完整可读）。
- **首页资料入口**：index.html「查找资料」路径行第三入口由「文档馆」改指 resources.html（双语 data-en="Community resources"），资源板块升为首页主路径可见；文档馆仍在资料导航组内。
- **检索联动复核**：search.html 类型按钮「社区资源」+ 按公司过滤对资源条目可用（R10 接通，本轮验证命中与类型组合）。
- **管线**：build-resources（36 条·aria-live）/ build-company-files（4 档案·16 资源深链·companies-data.js resources 字段）/ build-network（幂等）/ build-search-index（318）/ sync-changelog（203 条）/ build-ledger-links（23 处）/ build-events（14 事件）/ build-timeline-events（265 独立+39 吸收）/ build-capital（幂等）/ 版本三件套 9.3.0→9.4.0（VERSION+app.js+15 页 span 打印在案）/ build-epub（223,127 B）。
- **验证**：verify.py 9/9（38 页 / 索引 318 / 版本 9.4.0 / 修订史 206 / EPUB 新鲜）；node --check 全过；**CDP 探针 30/30**（tools/v9r14-probe.js，端口 9358 全新 profile：文件级 8 / 筛选 4 / 清除 1 / 跳转闭环 5 / 双语 3 / 无 JS 2 / 390 零溢出 2 / file:// 2 / 关系图面板 3）；**外链抽样 10 条核活 10/10 可达**（官方 2/开源 2/社区 3/工具 3，SEC 依合规 UA 口径 200，qa/v9-20/round-14/sources/liveness-sample.md）；截图 4 张入 qa/v9-20/round-14/。
- **质量节点②达成**：计划要求「资源页全流程探针（筛选/清除/跳转/双语/无 JS/390/file://）≥15 断言」——实际 30 断言，八流程全覆盖（含 file:// 离线与公司关系图面板交互），无遗漏项。首跑即 30/30，无断言修正。
- **先目检 DOM 再写断言（教训第四次生效）**：写关系图面板交互断言前先 grep 实构，确认节点为 `<g class="net-node" data-net-node="tesla">`（非猜测选择器），一次通过。
- **提交**：成果 `e8183f3`（v9.4.0，32 文件）；本回填+revisions（206 幂等+导航保持）+EPUB 重刷为第二提交。另：已将误被 sed 改动的 tools/v9r13-bump.py 还原至 R13 原状（避免污染 R13 产物）。
- **下一轮预告**：R15 设计系统升级——style.css `:root` tokens 区：色阶（--coal/--paper/--accent 衍生 3-5 档）、字号阶梯（clamp）、间距标尺（4/8 基）、圆角/阴影/边框分层、:focus-visible 统一；深浅双主题变量一致性核对（--mist/--muted 对比度 ≥4.5 复测）；落地 index+survival-2008+timeline+capital-evolution 四页样板；before/after 八组截图（1440×900 + 390×844）；三视口零溢出复扫。本轮新增 rs-*/cf-res* 组件一并纳入 tokens 审计。

## 第 15 轮工作记录（设计系统升级）— complete（2026-10-01）

- **本轮定性**：美术**地基轮**——不改技术栈、不加运行时依赖、不动公司色标语义，把散落在 style.css 的 500+ 硬编码值收敛为三层令牌体系，并借「对比度复核」修掉 3 类真实不达标的小字色。视觉 delta 刻意克制（多为值等价令牌化），显著美术迭代由 R16–R18 承接。
- **`:root` 三层结构（令牌 37 → 113 项）**：① **刻度令牌**——`--hue-*` 五色相（olive/ochre/graphite/navy/red）、`--paper-0/50/100/150/200` 暖白 5 档、`--coal-soft/0/100/200` 近黑 4 档、`--tx-1…4` 浅底文字 4 阶、`--txd-1…6`+`--txd-cool` 深底文字 7 阶、`--accent-deep/accent/bright/soft/glow` 朱红 5 档、`--rule-*` 描边 6 阶、`--r-*` 圆角 6 档、`--shadow-*` 块影 6 档、`--fs-*` 字号 26 阶、`--space-*` 间距 18 阶（4/8 基主阶 + 半阶）；② **语义令牌**——`--ty-*` 六事件类型、`--paper/--coal/--ink/--card/--muted/--mist/--navy/--accent-text/--on-hue`；③ **焦点令牌**——`--focus-w(3px)/-tight(2px)`、`--focus-offset/-tight/-wide`、`--focus-color/-dark/-invert`。清单见 `qa/v9-20/round-15/token-inventory.md`（自动生成）。
- **正文硬编码清零（值等价、零视觉回归）**：事件类型色 12 处 → `--ty-*`；资源徽标色 6 处 → `--hue-*`（与事件类型同源）；纯白表面 `#fff` 26 处 → 暖白 `--paper-0`（统一暖纸体系）；描边 7 处、圆角 46 处（999px/50%/6/4/3/2px）、块影 8 处、**字号 335 处**（17.5/16.5/16/15.5/15/14.5/14/13.5/13/12.5/12/11.5/11/10.5/10/9 + 18/19/20/21/22/24/26/34/48px 全阶梯）、焦点环 8 处全部令牌化。正文区剩余色字面值 **仅 3 个**：`#101316`、`#F3F0E8`（底色）与 `#C84032`（即 `--accent` 定义处）。`@media print` **18 个块显式保护**（`#fff/#000/#999/#555` 印刷形态不动）。
- **公司色标红线未破**：`--co-*` 10 项（musk/tesla/spacex/x/xai/neuralink/boring/solarcity/paypal/history）语义与值一字未动，探针逐项断言通过。
- **对比度复核（WCAG 2.1，双路核验）**：静态（`tools/v9r15-contrast.py`，注释写进 `:root`）+ 动态（探针内浏览器实算同一公式）。达标基线：`--mist` 9.27、`--muted` 6.24、`--accent-text` 5.80、`--accent-bright` 6.26、`--ty-start` 5.34、`--ty-deal` 10.08、`--ty-milestone` 6.84、`--ty-risk` 5.20、`--ty-ok` 4.60、白字于类型色块 5.24–11.48。**查出并修复 3 类不达标**：① `#8a857c`（浅底 **3.22:1**）用于时间轴年份轴标、266 条 `gxl-q` 引语行、`pt-year` → 新增 `--tx-3`（`#6A665D`，浅底 **5.02:1** / 卡片 4.63:1）；② `#9a948b`（**2.64:1**）用于 `gx-empty` 空态、`cap-detail-empty`、`reading` 目录待办 → `--tx-3`；③ `#6f6a62`（深底页脚彩蛋行 **3.47:1**）→ `--txd-6`（`#8a857c`，深底 4.80:1）。合计修复 **21 处**（style.css 5 + 13 页内联页脚 + reading）。另把 `#98938a`/`#1e6b40`/`#8a5a19`/`#8a2b20` 一并归入令牌（`--txd-5`/`--ty-ok-text`/`--hue-ochre`/`--accent-text`）。**已知并文档化例外**：`--accent`（#C84032）浅底 4.35 / 深底 3.76——按设计只用于大字/边框/填充，小字一律走 `--accent-text`/`--accent-bright`（V7 起约定，本轮在 `:root` 注释显式写明）。
- **`:focus-visible` 统一出口**：全站 8 处焦点环改消费 `--focus-*`（文字控件 3px/3px、密集 SVG 节点 2px/2px、暗底 `--focus-color-dark`、反色 `--focus-color-invert`、锚点 `:target` 用 `--focus-offset-wide`）；正文区 outline 硬编码 0 残留。探针用**真实 Tab 键事件**（CDP `Input.dispatchKeyEvent`）触发 `:focus-visible` 后读取计算值——程序化 `.focus()` 不触发，此为探针要点。
- **四页样板落地**：index（封面/路径卡/资料入口）、survival-2008（`sv-*` 图形与阶段徽标）、timeline（`gx-*` 图 + `gxl-q` 引语行）、capital-evolution（`cap-*` 流向图与图例）全部消费新令牌。
- **before/after 证据**：各 16 张全页截图（4 页 × 桌面 1440×900 / 手机 390×844 × 中英），`tools/v9r15-shot.js` 生成（CDP 全页捕获 + localStorage 切语言 + 冻结入场动画）；`tools/v9r15-diff.py`（Pillow）逐像素量化：**timeline 桌面 14.67% 变化最大**（轴标与 266 条引语行 3.22→5.02 加深）、capital-evolution 8.58%（图节点纯白→暖白）、survival-2008 0.05–0.20%、index 0.03–0.07%（页脚字色阶梯 + 版本串）。中位 2.39%。拼图对照见 `compare/`。
- **治本一处**：`tools/build-revisions.py` 模板内 `#8a857c`/`#1f3a5f` 硬编码 → `var(--tx-3)`/`var(--navy)`（防重跑回归；本轮重跑实测 rv-foot 与 206 个「在册」span 均为令牌，`#8a857c` 残留 0）。
- **验证**：verify.py **9/9**（38 页 / 索引 318 / 版本 9.5.0 / 语录卡 103+2 豁免 / 修订史 206 / EPUB 新鲜）；node --check 全过；**CDP 探针 69/69**（`tools/v9r15-probe.js`，端口 9362：文件级 33〔令牌结构 + 8 组刻度 + 公司色标 10 项 + 硬编码清零 + 版本产物〕+ 语义别名等价性 14 + 元素级令牌消费 12 + 焦点环 4 + 对比度实算 5 + 三视口零溢出 3）；**320/390/768 × 四页 = 12 组合零横向溢出**；版本三件套 9.4.0→9.5.0（VERSION + app.js + 15 页 span 打印在案，changelog.html 由正文提及而非 span）；EPUB 223,127 B / 24 章。
- **探针修正 3 项（均为探针缺陷，非页面缺陷）**：① 断言「无 font-size px 字面值」误判 `0.5em`/`3.2em`/`11.5pt`——收敛为仅禁 `px`。② **对比度抽测 5 项首跑全红**：根因是 Node **模板字符串内 `\d` 被字符串转义吞成 `d`**，`/[\d.]+/g` 实际是 `/[d.]+/g`，匹配 null → IIFE 抛错返回 `undefined`；改用 `slice+split` 解析颜色后全过。**教训：CDP 探针里正则写进模板字符串必须 `\d`，或干脆避开转义。** ③ `.gx-empty` 是条件渲染元素（筛选无结果才出现），改用合成元素读计算样式。**另：`先目检 DOM 再写断言` 第五次生效——焦点环断言因程序化 focus 不触发 `:focus-visible` 而失败，改真实 Tab 键事件后通过。**
- **提交**：成果 `210f443`（41 文件）；本回填 + revisions（206 幂等·导航保持·模板治本生效）+ EPUB 重刷为第二提交。
- **下一轮预告**：R16 首页视觉迭代——封面 hero 构图（标题/肖像/业务画面主次）、模块节奏（feature-lead/feature-rows/path-cards 层级差异化，打破等尺寸卡片感）、三入口（阅读/版图/检索）视觉强化；消费本轮令牌（`--fs-clamp` 体系、`--r-*`、`--shadow-*`、`--paper-*` 阶梯）。验收=新旧首屏对比截图差异显著 + 320/390/768 复扫 + EN 标题不破版。

## 第 16 轮工作记录（首页视觉迭代）— complete（2026-10-01）

- **本轮定性**：美术升级**第一轮实质迭代**——不换技术栈、不加运行时依赖、不动公司色标语义，全部消费 R15 令牌（`--paper-*` 阶梯、`--fs-*` 阶梯、`--t-fast`、`--focus-*`、`--shadow-*`）。改动**收敛于首页**（探针实测 `firm-grid`/`path-list`/`feature-lead`/`hero-*` 等目标类**仅 index.html 使用**，零跨页波及）。三个方向：封面 hero 构图主次、模块节奏去均质化、三入口强化。
- **① 三入口视觉强化**：`hero-actions` 由 `.btn btn-ink + 2×.btn-ghost` 普通按钮行 → **编号入口条 `.act`**（衬线斜体编号 01/02/03 + 右细分隔线 + 文字 + 箭头；hover 反白填充 + 箭头 `translateX(4px)`；主入口 `.act-primary` 朱红实底 `--accent`/`--on-hue`）。**语言切换安全**：`data-en` 全部下沉到 `.act-txt` 叶子节点（app.js 的 i18n 约定「含 data-en 者必为叶子」，整体替换 innerHTML 不会破坏编号/箭头结构——探针专项断言）。移动端 640px 断点下三入口各占满一行（原 .btn 的 `flex:1 1 auto` 规则同步迁移到 `.act`）。
- **② 封面照报头处理**：肖像加朱红封面标 `.cover-tag`（`COVER · 2018`，aria-hidden 装饰，与 V7-R7 公司色标无关）+ `.hero-figure::before` 内衬细线双框（inset 10px `--hairline-paper`）——报刊封面照语言。
- **③ 业务画面横带图版化**：`strip-tag`（TESLA/SPACEX/X）自 `figcaption` **移至 `<img>` 后的 figure 直接子元素**，样式改绝对定位角标（图片左上，`--coal-200` 底 + `--accent-bright` 字）；图片 hover 微抬 3px + 朱红描边。说明区（figcaption）变为纯文字。
- **④ 封面数字行强化**：`.hero-stats` 顶分隔线 1px/40% → **2px/55%**，dd 色 `--paper` → `--paper-0` 提亮一档。
- **⑤ 模块节奏（打破等尺寸卡片感）**：`firm-grid` 6 等大瓦片 → **2 特大 + 4 标准**：Tesla/SpaceX 加 `firm-tile--xl`（`grid-column: span 2`），4 列网格下自动排布为**上行两大（Tesla+SpaceX）、下行四小（X/xAI/Neuralink/Boring）**——编号顺序 01 02 在上行，03–06 在下行，阅读顺序天然成立。特大瓦片：标题 26px、编号标 10.5px、padding 26/24、desc 14.5px/58ch。**真缺陷修复**：`.firm-tile--xl h3` 与 `.firm-tile h3` **特异性相同（0-1-1）**，被源码顺序靠后的基础规则覆盖（实测 20px 而非 26px）——改 `.firm-grid .firm-tile--xl h3` 提特异性（0-2-1）。900px 断点 xl 跨满 2 列整行，600px 单列。
- **⑥ 旗舰专题分层**：`.feature-row:nth-child(-n+3)`（三条 FEATURE 级：2008 生死役/平台变局/承诺与结果）加 **3px 朱红左标线 + padding-left 16px**，与后四条 DEEP DIVE 级行拉开层级（探针实测前三条 `border-left 3px rgb(200,64,50)`、后四条 `0px`）；全部行 hover 加 `--paper-50` 微底色。`.path-row` hover 标题转 `--accent-text`，与全站 hover 语言统一。
- **⑦ reduced-motion 全覆盖**：本轮新增微动效（`.act`/`.act-arr`/`.hero-strip img`/`.firm-tile`/`.feature-row`/`.path-row`）在 `prefers-reduced-motion: reduce` 下 `transition: none !important` + hover `transform: none !important`（新增独立块，探针文件级断言）。
- **before/after 证据**：`tools/v9r16-shot.js` 各 6 张（index × 桌面 1440×900 / 平板 768×900 / 手机 390×844 × 中英，CDP 全页 + 冻结动画 + localStorage 切语言）；`tools/v9r16-diff.py`（Pillow）逐像素量化：**11.03%–28.13%**（中位 22.3%），最小 index-desktop-en 11.03%、最大 index-tablet-en 28.13%——**远超「显著变化」10% 阈值**，验收达成。另生成 **首屏 900px 并排对比图 3 张**（`compare/cmp-firstscreen-{desktop,tablet,mobile}-zh.png`，BEFORE/AFTER 标签 + 中缝）。
- **验证**：**CDP 探针 43/43**（`tools/v9r16-probe.js`，端口 9364：文件级结构 6 + 样式规则 8 + 版本产物 3 + 几何〔xl 瓦片宽 501px = 2× 标准 244px、同行并排〕+ 计算样式 6 + FEATURE 分层 4 + EN 切换不破版 4 + 三视口溢出 6 + 键盘可达与焦点环 2 + 截图落盘）；verify.py **9/9**（38 页 / 索引 318 / 版本 9.6.0 / EPUB 新鲜）；node --check 全过；**320/390/768 × 四页 × 中英零横向溢出**；EN hero 标题 `scrollWidth ≤ clientWidth` 不破版；版本三件套 9.5.0→9.6.0（15 页 span）；EPUB 223,159 B / 24 章。
- **探针修正 4 项（首跑 38/43）**：① **真缺陷**（非探针问题）`.firm-tile--xl h3` 同特异性被覆盖 → 修 CSS 提特异性；② 期望值误写——`.act-primary` 文字色是 `--on-hue`（`#fff` 纯白）而非 `--paper-0`；③ reduce 模拟下断言 `transitionProperty`（被 `!important` 禁用后自然为 `none`）→ 改文件级断言 hover 规则存在；④ **Tab 循环上限 14 次不足**——导航下拉 `.nav-drop` 虽为 `display:none`，但 `.nav-group:focus-within` 会展开，键盘用户可穿越全部导航项（约 43 个）后到达正文；这是**刻意的键盘可达模式**（鼠标 hover ↔ 键盘 focus 对等），非缺陷，探针循环上限放宽至 60。**教训沉淀：断「动效已挂」不要在 reduce 模拟下做；断「Tab 第 N 次命中」必须先把导航可聚焦项数清点清楚。**
- **提交**：成果 `6a0a5ae`（26 文件）；本回填 + revisions（206 幂等）+ EPUB 重刷为第二提交。
- **下一轮预告**：R17 数据图形工业风——`gx-*`（timeline 年份轴）/`cap-*`（capital-evolution 流向图）/`net-*`（companies 关系图）三图精修：线宽与节点层级、网格与刻度统一、标签排版与碰撞避让、深底图形对比度复核；消费 R15 令牌；before/after 截图 + 三视口复扫。

## 第 17 轮工作记录（数据图形工业风）— complete（2026-10-02）

- **三图纯 CSS 精修（style.css +71 行，DOM/SVG 几何/生成器零改动）**：①etype 节点形状语言（start=圆/deal=方/gamble=菱 45°/milestone=满圆/risk=三角 clip-path；色标不变加形，补色盲可达性）+ 类型筛选芯片 ::before 形状图例（原纯文本无色点——TYPES 芯片与公司芯片是两组，公司芯片有 i 色点、类型芯片没有，教训=改图例前先查 JS 构建器 innerHTML）；②gx 年轴等宽（新令牌 --font-num 入 R15 字体层）+ ::after 6px 刻度线 + 清单日期等宽；③cap-elabel 改 sans+tabular-nums（标注层与 serif 节点名分层）；④cap/net 图例同字号同间距、虚线同构造；⑤cap-graph/net-graph 图底点阵网格（26px，不模拟坐标，print 关闭）。
- **数据编码不动（红线自查入探针断言）**：首条 ribbon 计算线宽=生成器 stroke-width 属性值（CSS 未覆盖数据编码）、gamble 核心仍 rgb(200,64,50)、「示意非等比」口径注原文保留、R17 段零新增 transition/animation（grep transition: 声明级检查）。
- **验证**：verify.py 9/9（38 页/索引 318）；**CDP 探针 34/34**（tools/v9r17-probe.js 端口 9365：文件级 5/桌面三图 17/三视口九宫格 320·390·768 零溢出 9/390 清单形态切换 3）；sync-changelog 206 条；版本三件套 9.6.0→9.7.0（15 页 span）；EPUB 223,159B。
- **探针修正三则（均为探针缺陷，页面正确）**：①「无新增 transition」被段头注释字样误命中→改查 `transition:` 声明；②图例同字号误在同页比较两页元素→跨页取值 Node 侧比较；③伪元素 ::before 写进 querySelector 抛异常→querySelector 与 getComputedStyle 第二参分离。
- **截图取景教训（R18/R19 复用）**：首拍 4 张 after 与 before 逐像素相同——①cap/net 在 390 被既有移动端规则整体隐藏（清单形态即移动形态，一致=正确且是「390 清单形态」回归证据）；②gx-board 高于视口，block:'center' 取景框进未改动的中部泳道→改滚 .gx-controls（芯片+年轴+事件道入画）+ `git stash push -- style.css` 取同取景真 before 配对，after 与 before 差异可辨（97,422B→98,649B）。
- **管线**：build-revisions（206 幂等，导航保持——R12 治本持续生效）+ EPUB 重刷为第二提交。
- **提交**：成果 `66c323d`（v9.7.0）；本回填+revisions+EPUB 重刷为第二提交。
- **下一轮预告**：R18 排版与阅读体验（v9.8.0）——lr-* 长文与 ps-* 账本：字体层级复核（正文 16-18px/阅读宽 640-760）、引语块与编者注视觉区分强化、数字/日期/金额等宽排版（--font-num 已入令牌层可直接消费）、EN 长文换行与行高、print 形态复查；before/after 截图注意本轮教训（取景框到改动元素、stash 法取真 before）。