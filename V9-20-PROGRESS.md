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
| 07 | 官方演讲扩充（Starship 更新会 / Neuralink demo / AI Day） | pending | — | — | — |
| 08 | 事件档案聚合扩容（9→14±，口径红线探针） | pending | — | — | — |
| 09 | 语录卡补齐 + 质量节点①（盘点总表入账本） | pending | — | — | — |
| 10 | 资源页基建（resources-data.py + build-resources.py + 导航注册） | pending | — | — | — |
| 11 | 官方与标准类资源 | pending | — | — | — |
| 12 | 开源项目资源（Tesla API 生态 / Starlink 追踪 / 发射工具） | pending | — | — | — |
| 13 | 社区与档案资源 + 元数据补全（R11–13 合计 +30~50 条） | pending | — | — | — |
| 14 | 资源交互与联动 + 质量节点②（≥15 断言） | pending | — | — | — |
| 15 | 设计系统升级（style.css :root tokens，四页样板） | pending | — | — | — |
| 16 | 首页视觉迭代 | pending | — | — | — |
| 17 | 数据图形工业风（gx-*/cap-*/net-* 三图精修） | pending | — | — | — |
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
