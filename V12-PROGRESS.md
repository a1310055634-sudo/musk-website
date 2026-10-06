# V12-20 计划进度记录（颗粒度·内容扩容 · 复古杂志版式深化 · 一手信息增量）

> 「马斯克商业志 MUSK, INC.」V12-20 升级计划（2026-10-06 立项，共 20 轮，目标 v12.0.0）。
> 任务书正本 `V12-TASKBOOK.md`（含四A速查节与定时提示词第六节）；本文件是唯一轮次账本，与 git 相互核验。
> 前序：V9-20 二十轮（v8.1.0→v10.0.0，V9-20-PROGRESS.md）、V10-15 十五轮（v10.1.0→v11.0.0，V10-15-PROGRESS.md）、v11.1.0 复古杂志美术增量（58d0b85+ba47824）。不继承其计数。

## 运行模式（重要）

- **纯本地模式**：每轮仅做本地 git 提交，**绝不 push、不 fetch 后合并远程、不改写已有历史、不做云端发布与 Pages 验证**。第 20 轮输出 RELEASE-CHECKLIST-v12.md「待发布清单」，由用户验收后自行推送。
- 每次触发完成一个未完成轮次；上轮中断先恢复。成功轮次共 20；失败/空触发/重复检查不增加轮次；一轮未验收不进下一轮。
- 20 轮全部本地验收通过后，后续触发**静默退出**（不改文件不加版本不提交）。
- 每轮锁：`.v12run.lock`（不入 git，已在 .gitignore）。有效锁直接退出；确认旧实例已死（进程+仓库静默>15min）才可恢复遗留锁。
- 版本步进：R01=v11.2.0 → R19=v11.20.0（每轮 minor+1）→ R20=v12.0.0。三件套=VERSION+app.js SITE_VERSION+16 处 site-version-val span（替换计数须打印）。

## 基线快照（2026-10-06 核对，=v11.1.0 收官态）

- 分支 main @ `097c10d`（任务书颗粒度修订版），VERSION `11.1.0`；origin/main 停在 `355fc0d`（v7.9.0 时代）——**本地领先 85 提交全待用户推送**。
- 工作区干净：38 个 HTML 页面（含 noindex 试衣间 preview-v12.html，正式 37）；账本 119 条（primary.html）；一手文档 27（documents.html）；访谈 47（interviews.html）；X 帖 34（x-posts.html，最新 2025-07）；语录卡 107（引文块 109，白名单豁免 2）；事件档案 16 档 67 材料；编年史 53；资源 49 条（official 11/opensource 9/community 21/tools 8）；检索索引 354（119+27+47+34+5+53+4+16+49）；修订锚点 227；EPUB 含 e2026-07-22；verify.py 9 项。

## 轮次状态

| 轮 | 主题 | 状态 | 版本 | 成果提交（本地） | 备注 |
|---|---|---|---|---|---|
| 01 | 基建：账本+缺口清单 v3+两份工作册 | complete | v11.2.0 | 0b7ab1c | 镜像五短语探明：断代期覆盖充足（Grok4 1105/Grok5 898/AP 178/robotaxi 37/Optimus 19，最新 2026-10-04）；quotes-worklog 101 行+emails-worklog 47 行（初判在册 14）；.gitignore 已含锁（前轮备好）；勘误 span=15 处非 16 |
| 02 | X 帖断代回捞 III（2025-08→2026-10） | complete | v11.3.0 | 74cb82a | +6 卡 34→40（robotaxi×4/Optimus 产线/Grok 4.8）；2026 年份条新建；snowflake 六卡全吻合；索引 360；探针 23/23；revisions 227→233（X 帖 40）；留档 3 条移交 R10 |
| 03 | X 帖早期加密 I（2018–2019） | complete | v11.4.0 | a874a79 | +4 卡 40→44（BFR 碳纤维首段/SEC typo 两连发/Starhopper/Cybertruck 146k）；逐字纠错「不锈钢首曝」讹传；索引 364；探针 20/20；revisions 237 |
| 04 | 账本早期加密（2002–2010） | complete | v11.5.0 | 53b7e76 | +5 条 119→124（全 424B4/EDGAR/NASA 转存一手锚，无引语节）；查重出局 F4/IPO/MasterPlan 已在册；索引 369；探针 20/20；revisions 242 |
| 05 | 访谈消化轮 | complete | v11.6.0 | 96ae77a | +4 场 47→51（全 2026 断代：Moonshots/Davos-Fink/Dwarkesh/Economist）；lex-438 维持降级+勘误编号；All-In/Bloomberg 空壳弃收；索引 373；探针 18/18；revisions 246 |
| 06 | email 库双源核验 I（前 15 封） | pending | v11.7.0 | | emails-worklog.tsv 为底册 |
| 07 | email 续 + 文档馆近年化 | pending | v11.8.0 | | EDGAR 直取 2024–2026 |
| 08 | 引语 101 块逐条核验（质量轮） | pending | v11.9.0 | | quotes-worklog.tsv 逐行填 verdict |
| 09 | 质量节点①：盘点总表 v3 | pending | v11.10.0 | | 三口径零漂移 |
| 10 | 事件档案 2023–2026 补档 | pending | v11.11.0 | | 口径红线探针；etype/kind 枚举勿扩 |
| 11 | 编年史近年+深读新篇 I（deep-dive-06 xAI 三年志） | pending | v11.12.0 | | 新页七件接入（nav/索引/verify/span/互链） |
| 12 | 深读新篇 II（Robotaxi 或 政治参与） | pending | v11.13.0 | | 同七件接入 |
| 13 | 资源扩容（xAI/Grok 生态） | pending | v11.14.0 | | 49→58±，validate 拒生成不可绕 |
| 14 | 质量节点②：互链扩展+检索审计 | pending | v11.15.0 | | 共现扫描 +6 对 |
| 15 | 美术·报头刊头体系 | pending | v11.16.0 | | masthead 走 site-nav.py 模板 |
| 16 | 美术·正文杂志版式（drop cap/引语题花） | pending | v11.17.0 | | 纯 CSS；基线 16.5px/720px 不动 |
| 17 | 美术·图表复古化（hatch 雕刻风） | pending | v11.18.0 | | 数据编码不动；390 清单形态=回归证据 |
| 18 | 美术·专题封面化+首页封面故事 | pending | v11.19.0 | | 纯 CSS+既有 DOM；三入口不动摇 |
| 19 | 美术·微交互统一+质量节点③ | pending | v11.20.0 | | transition TSV；四轮截图齐备 |
| 20 | 全站验收+待发布清单（v12.0.0） | pending | v12.0.0 | | 全家桶 14 脚本幂等；sitemap 40 URL |

状态取值：pending / in_progress / complete / blocked。失败不推进轮次。

## 缺口清单 v3（2026-10-06，接替 EXPANSION 卷首 v2；v2 五项保留原重验条款）

1. **X 帖断代 2025-08→2026-10（★★★）**：站内最新 2025-07，空白 15 个月。**R01 镜像探明**（/agents/search 精确短语，type=posts，2026-10-06 实测）：
   - `Grok 4` → total **1105**（首三条 2026-10-04/09-30/09-29——镜像覆盖至今天实锤）
   - `Grok 5` → total **898**（2026-09-14 起）
   - `America Party` → total **178**（2026-09-26 起）
   - `robotaxi Austin` → total **37**（2026-01-22/2025-11-26/2025-10-29）
   - `Optimus production` → total **19**（2026-10-01/2026-07-01）
   - `xAI funding` → total **7**（2025-07-11/2025-05-15/2024-05-27，断代期内较少）
   **结论：R02 可回捞量充足，五主题全部有断代期内帖子。** R02 立卡时每条仍须 transcript/{id} 取原文+snowflake 对表。
2. **引语 101 块非镜像来源待逐条核**：底册 qa/v10-15/round-03/unmatched-itemized.tsv（other-official 73/earnings-call 20/edgar 6/jre 1/ted 1）→ 工作册 `qa/v12/round-01/quotes-worklog.tsv`（101 行，verdict 列空待 R08 填）。
3. **email 候选库**：镜像 emails 全量 47 封（qa/v9-20/round-06/sources/emails.json）→ 工作册 `qa/v12/round-01/emails-worklog.tsv`（47 行；日精度日期命中 documents.html 在册 id 者 14 封初判在册，33 封待 R06/R07 双源核验；含 Fork in the Road 2022-11-16 等已收件正判 Y）。
4. 访谈早期断档（60-minutes-2012/lex-438 待外部逐字源）与 SAE J3400/tesla.com 重验条款：沿 v2，归 R05 与 R13。
5. 深读新篇候选池：xAI 三年志（R11）/Robotaxi 落地考、政治参与 2024–2026（R12 择一，落选者留档）。

## 恢复指引

- 每轮唯一成果提交信息带 `[V12 Rxx]` 前缀；工作记录追加在本文件末尾。每轮原则上一个成果提交+一个账本回填提交。
- 提交了但中断 → 账本行回填后直接进下一轮，不重做工作。
- 账本/一手页变动后必跑：`build-ledger-timeline.py` / `build-search-index.py`（断言同步）/ `build-epub.py`；CHANGELOG 更新后跑 `sync-changelog.py`；HTML 改动（含 span 批量替换）后 `build-revisions.py`+EPUB 重刷为第二提交内容；最后 `verify.py` 9 项全绿。
- 采料纪律与坑册：任务书第三节+四A速查节（模板结构/枚举/CDP 惯例全在）；复杂 Python 写 .py 文件执行；行级比较 rstrip('\r')；深夜中文一律 Write 工具。
- CDP 探针端口 9333 起步递增；断言值 JSON.stringify 包裹；轮询计数不 sleep。

## 工作记录

### R01（2026-10-06，v11.2.0）
- 建账本（本文件）；.gitignore 检查：`.v12run.lock` 已在前轮备好（无需改动，如实记录）。
- 镜像五短语探明（见缺口清单 v3 §1），结论=R02 弹药充足；探明数据不立条（立条归 R02）。
- 两份工作册：`tools/v12r01-worklogs.py` 生成 quotes-worklog.tsv（101 行：id/来源/重验路径/verdict 空）+ emails-worklog.tsv（47 行：id/日期/标题/org/初判在册 14/verdict 空）。
- 版本三件套 → 11.2.0（15 处 span 替换计数打印在案；**勘误：任务书 §9 原写 16 处系 grep -l 被正文
  字样提及污染——changelog.html 无 span，正确计数 15，任务书与 bump 脚本注释已同步修正**）；
  CHANGELOG 补条目；sync-changelog；build-revisions+EPUB 重刷（span 改动 15 页）。
- 基建轮无页面视觉改动，CDP 探针豁免（以 verify 9/9+基线快照核对代替，如实记录）。
- **验收**：verify 9/9 全绿（版本一致性 11.2.0/索引 354/EPUB 含 e2026-07-22）；node --check app.js+cite.js 过；
  全家桶子集 sync-changelog（228 条）/build-revisions（227 锚点）/build-epub（236,024B）重跑通过。
- **本轮新增教训（已入任务书 §9）**：grep -l 统计 span 会被正文「site-version-val」字样提及污染
  （changelog.html 无 span 元素但正文提及一次→虚增 1）；span 计数必须用 `site-version-val">` 精确模式。
- 下一轮预告：R02 X 帖断代回捞 III（2025-08→2026-10，v11.3.0）——只走 /agents/search，
  跨 2026 须仿既有年份组头新建组，立卡 4–6 条每条 transcript 原文+snowflake 对表。
- 成果提交 0b7ab1c（27 文件）；本回填为第二提交。

### R02（2026-10-06，v11.3.0）
- **六卡上墙（34→40）**：robotaxi 弧线四卡（p2025-08-16 服务面积超对手→p2025-10-29 大奥斯汀全区→p2026-01-22 **车内无安全监督员**+Optimus「100X」→p2026-10-03 延时 23 点+「灰色小猫」，首尾覆盖断代窗）+ p2026-07-01 Fremont Optimus 产线实拍（t.co 图链不入正文，Gamestonk 先例）+ p2026-09-14 Grok 4.8 2.5T/C++ 栈首曝（同日 Grok 5 次序确认帖在卡注）。
- **采料**：/agents/search 四短语→/agents/transcript 六帖全文；snowflake 解码六卡与镜像 date 全吻合（精确到分写进卡注）；2026 年份条新建（xp-year 扁平混排结构克隆，无新容器层；插锚=xp-grid 闭合+chapter-summary 拼回，v12r02-integrate.py 内建断言 cards/permalink/text/zh=40×3、years=9）。
- **验证**：verify 9/9（索引 360=…+40+…）；**CDP 探针 23/23**（tools/v12r02-probe.js 端口 9345：文件级 8/桌面 14/390 溢出 1——时序升序、逐字 3 条、双语 CJK、2026 组归位与卡序、互链 4 路、跨页锚真实存在）；QA 截图 2 张+ACCEPTANCE.md 入 qa/v12/round-02/。
- **工程记录**：①revisions 扫 git 历史——X 帖选辑 34→40 在**成果提交后重跑**才入册（227→233 锚点），“先提交再 revisions”顺序与 V9-20 惯例一致；②CHANGELOG 探针数预写 8 实际 23，提交前已如实修正（教训：验收数字一律跑完再写）；③策略取舍：America Party 2026 政治帖组（178 条池）整体移交 R10 双写语境，Grok 4 发布帖（2025-07-09 界外真空）留档 EXPANSION。
- 成果提交 74cb82a（31 文件）；下一轮预告：R03 X 帖早期加密 I（2018–2019，v11.4.0）——index 管线可用，先查重 17 条再扩。

### R03（2026-10-06，v11.4.0）
- **四卡上墙（40→44）**：p2018-09-18 BFR 首段实体箭体（**逐字甄别纠错：原文「new carbon fiber material」，网传不锈钢首曝不实**，卡注写转身伏笔）；p2018-10-04 SEC「做空者致富委员会」typo 两连发（漏 say 原样+补刀帖）；p2019-07-26 Starhopper 150m「水塔*能*飞」（星号原样）；p2019-11-23 Cybertruck 146k+零广告两连发（与大锤卡 48 小时翻盘弧线）。
- **查重与快照勘误**：既有 2018×3/2019×3（任务书「10+7」系日期字符串误估，如实勘误入 ACCEPTANCE）；Bitcoin 购车三连发实测 2021-03-24 出局；六帖 snowflake 全吻合。
- **验证**：verify 9/9（索引 364；EPUB 两度落后两度重刷——span 与 changelog 改动后必须最后重刷，构建顺序纪律再验证）；**CDP 探针 20/20**（tools/v12r03-probe.js 端口 9347：typo 原样断言/2019 组七卡卡序/水塔卡整卡 textContent 精确相等）；QA 截图 2 张+ACCEPTANCE.md。
- **工程记录**：①search 端点 year 参数未生效（返回全量）——2018 深挖改用 index 月切片（EXPANSION 在案）；②python -c 内嵌三引号中文再次失真——ACCEPTANCE 改 Write 工具（红线第 N 次验证）。
- 成果提交 a874a79（31 文件）；下一轮预告：R04 账本早期加密（2002–2010，v11.5.0）——锚=NASA CRS-1/Falcon 1 F4/Tesla S-1，注意 SpaceX 无 S-1/Tesla 2008 无 8-K。

### R04（2026-10-06，v11.5.0）
- **五条入账（119→124）**：e2002-05 SpaceX 成立（424B4「since May 2002」）/e2004 Musk 任 Tesla 董事长（424B4「since April 2004」）/e2008-12-23 NASA CRS-1 $1.6B（转存两源+OIG）/e2009-05-19 Daimler（424B4 Blackstar+Form D）/e2010-05-20 Toyota-Fremont（424B4 May 2010 段）。全无引语节——ps-quote 115 不变、语录卡不动。
- **查重纠偏**：任务书候选 F4/IPO/MasterPlan 均已在册（e2008-09-28/e2010-06-29/e2006-08）；e2008-12-24 是融资非合同——增量按实测五条。
- **验证**：verify 9/9（索引 369）；**CDP 探针 20/20**（tools/v12r04-probe.js 端口 9349；首跑 1 挂=textContent 中文模式读不到 data-en——N10 坑第三次，改属性断言即过）；revisions 提交后重跑 237→242（言行实录 127）。
- **工程记录**：①全页时序升序断言不成立（既有年精度条目插年份段中间）——改局部邻居检查；②&& 链断路时 heredoc 不执行的静默坑（首轮账本断言 119→124 实际未改，二次补改）；③sed 链式复用 bump 脚本自噬（两规则互相吃）——bump 必须 Write 全新；④_tmp_*.html 临时文件会被 verify 当页面扫描——下载件放项目外或即用即删。
- 成果提交 53b7e76（30 文件）；下一轮预告：R05 访谈消化轮（v11.6.0）——60-minutes-2012/lex-438 重验+镜像库查重后扩收 4–6 场。

### R05（2026-10-06，v11.6.0）
- **+4 场（47→51）**：镜像 161 场与站内对照——2013+ 未收 11 场**全部 2026 年**（访谈断代与 X 帖同源）。立：i2026-01-06 Moonshots #220（Grok 电路访谈）/i2026-01-22 达沃斯与 Fink（最大飞行器+今年证明全复用）/i2026-02-05 Dwarkesh（AI5 进 Optimus+电网错峰）/i2026-07-23 Economist（数字-物理智能两半论）。
- **双降级维持**：lex-438（Neuralink 专场）两猜测 URL 404；60-minutes CBS 404——均维持留档并勘误编号口径（v2① lex-438≠站内已收 #400 稿）。
- **弃收**：All-In 场详情页列表壳、Bloomberg 场空壳——如实留档（重验=查详情页 id 变体）；7 场候选池入 EXPANSION。
- **验证**：verify 9/9（索引 373）；**CDP 探针 18/18**（tools/v12r05-probe.js 端口 9351；首跑 1 挂=legacy 无 id 条目计入总数，修正）；QA 截图 2 张。
- **工程记录**：访谈 transcript 端点只回标题——全文在 /video/{id} 详情页（2.75MB 级，剥标签抽词）；bump 脚本 heredoc 生成再炸（换行字面量）——**版本脚本必须 Write 全新文件**（红线第三次验证）。
- 成果提交 96ae77a（31 文件）；下一轮预告：R06 email 库双源核验 I（前 15 封，v11.7.0）——emails-worklog.tsv 为底册。

### R06（2026-10-06，v11.7.0）
- **+4 条（文档馆 27→31）**：d2022-04-20 埃里森十亿承诺（"A billion … or whatever you recommend"——法庭披露件+SEC 2022-05-05 备案双源，与账本 e2022-04-20 互证互链）/d2022-11-09 Twitter 首封全员信（CNBC 全文双源）/d2023-01 bait-and-switch（**口径如实=2026 庭审宣誓作证当场追述，原始短信档未公开**）/d2023-02 my-hero（2026-01 解封展品+BI 逐字双源）。Bret Taylor 私信=在册复用（e2022-04-09 现场段已覆盖）不新立；N09 留档 30 封消化 5 封。
- **管线突破**：镜像 email 详情页**带浏览器 UA 的 curl 可取完整 SSR HTML**（26KB 级；裸 curl=404 壳、web_reader 渲染亦可）——正文在 Next.js RSC payload 内，tools/v12r06-extract.py 采料入册；镜像页脚自带第二源链接（法庭展品/CNBC/hardresetmedia）。四封镜像存档 qa/v12/round-06/sources/。
- **验证**：verify 9/9（索引 377=…+31+…）；**CDP 探针 24/24**（tools/v12r06-probe.js 端口 9352：三段时序邻居/四条五件套/逐字四组/口径戳/互链 e2022-04-20 与 d2023-01→02）；QA 截图 2 张。
- **工程记录**：①**documents.html 历史上无站点页脚**（无 site-version-val span，页尾=定制 doc-foot）——探针首跑 1 挂系断言写错非站点回归，15 span 口径从未含它；②集成断言教训：permalink 计数用 `href="#id" title=` 特征（裸 `href="#id"` 会被站内互链虚增）；③2023-01 庭审追述件的日期口径（镜像 2023-01-23=微软 $10B 公告时点 vs 庭审转述"late 2022"）取镜像元数据并在注释声明依据。
- 成果提交 eb28182（41 文件）；下一轮预告：R07 email 续+文档馆近年化（2024–2026 SEC/Starship 信，v11.8.0）——worklog 前 15 封余量+近年文书锚盘点。

### R07（2026-10-06，v11.8.0）
- **+6 条（文档馆 31→37）**：**重大发现——SpaceX 已上市（Nasdaq: SPCX），站内此前零覆盖**。EDGAR 全链：S-1（2026-05-20）→8-A12B（06-10）→424B4（06-12，555,555,555 股×$135.00≈750 亿募资，募资用途首位=AI 算力）→senior notes 8-K 三连（06-22/23/26，五档 2031–2056 合计 250 亿）→10-Q（08-04）。立 d2026-06-12（424B4）+d2026-06-22（notes 定价）。Tesla 近年化：d2025-09-17 万亿薪酬包 proxy（12 档 2T→8.5T+400B EBITDA，互链 e2025-11-06）+d2026-01-29 10-K FY2025（AI 定义句+Technoking 关键人句）。email 续：d2018-08-12 PIF 短信（诉讼展品+Fortune 双源，互链 e2018-08-07）+d2022-03-26 Dorsey 协议短信（法庭展品+danluu 汇编双源，互链 e2022-03-26）。
- **探测如实记录**：xAI 披露——EDGAR FTS "xAI Holdings" 56 命中实为 SpaceX 文件（333-296740=SpaceX IPO 注册号）；x.ai 关联 CIK×5 无可立条文书，记 EXPANSION。Starship 官方更新信——IPO 后披露通道已转 SEC 备案，任务书目标以 424B4/notes 8-K 达成。
- **验证**：verify 9/9（索引 383）；**CDP 探针 25/25 一次全绿**（tools/v12r07-probe.js 端口 9353：六新 id 索引/一手文档 37/总数 383/逐字 6/12 邻居时序链/互链 3/390 溢出）；QA 截图 2 张。
- **工程记录**：①跨轮累计型断言须计基线（口径戳全页=R06 4+R07 6=10）；②pricing 8-K 404 壳→accession 目录 index.json 查真实文件名 spcx-pricing8xk.htm；③RSC payload 长串截断→正则长度下限提到 400 修复（Dorsey "Super interesting idea" 完整版）；④EDGAR submissions 全史（2002–2026）Counter 扫描=近年化锚点速查法。
- 成果提交 e3169c7（45 文件）+1d9c298（revisions 250→256+EPUB 250,858B）；下一轮预告：R08 引语 101 块逐条核验（质量轮，v11.9.0）——quotes-worklog.tsv 三态结论，撤下须语录卡+账本同步防计数漂移。

### R08（2026-10-06，v11.9.0）——质量轮
- **101 块非镜像来源引语逐条机核**（quotes-worklog.tsv 全行 verdict+anchor_url 非空）：**✅15**（镜像 /agents/search 中段 6 词匹配 10——含镜像自建 earnings call 转录 2 场+Fork in the Road 邮件底本交叉确认；EDGAR FTS 3；stockanalysis WebFetch 抽样逐字吻合 2）/**⚠️86**（转引在册，分组注明原因：E-C 组 stockanalysis 底本+抽样吻合记录/EDGAR 组 3 条实为 SEC 起诉状与判词措辞非备案原文/ted transcript JSON 无逐字吻合/jre 未抓）/**❌0**（无反证不撤）。
- **quotes.html 上屏（零新 CSS 零新类）**：✓15 卡附原文核验标（title 悬停显锚，规避 a 嵌 a=并入 qs-src 行尾）；◎83 转引标；页脚核验口径段。107 卡恒定，**恒等式 107=109−2 保持**；e2021-07/e2025 两条账本块无语录卡（TSV 照填、卡标不适用）。
- **抽样人工复核 10 条**（SAMPLE-REVIEW.md）：含 e2013-05-08 口径不符如实记（stockanalysis 该季稿无此句，引语实为股东信口径——后续可换锚）与 e2019-02-19 镜像假命中甄别（年份词撞车致字串巧合，人工判非）。
- **验证**：verify 9/9（恒等式项绿）；**CDP 探针 14/14**（端口 9354：TSV 行数/三态分布/✅ 行锚非空/107 卡/15✓/83◎/title 锚/口径段/390 双视口）；QA 截图 2 张。
- **工程记录**：①探针断言口径两次修正（TSV 行数含 header=102；⚠️86 含 e2023-11-30 双行——worklog 一 id 两引语块）；②stockanalysis transcripts URL 带数字 id 前缀（23986-q1-2013 式），列表页先探 id 再抽；③www.sec.gov 页面 curl 403（data.sec.gov API UA 与页面 UA 政策不同）。
- 成果提交 dbec4af（34 文件）+生成物一笔；下一轮预告：R09 质量节点①盘点总表 v3（v11.10.0）。

### R09（2026-10-06，v11.10.0）——质量节点①
- **三口径零漂移（tools/v12r09-audit.py 脚本核对打印）**：九类型「页面 DOM/检索索引/生成器断言」并列全 OK——账本 124/文档 37/访谈 51/X 帖 44/深读 5/编年史 53/财务 4/事件 16/资源 49=383=383=383；审计数据 qa/v12/round-09/audit-data.json。
- **盘点总表 v3**（qa/v12/round-09/AUDIT-v3.md）：R02–R08 增量对账+四类型年份分布——X 帖 2018–2026 无断年（R02/R03 填补生效）；访谈 2009–2012 空白=硬约束；文档 2011–2014/2019 空白；**账本 2003/2005/2007 三整年空白=最大剩余缺口**（v4③ 列 SpaceX 早期候选：2003 F1 立项/2005 首静火/2007 Flight 2-3）。
- **缺口清单 v4** 写回 EXPANSION 卷首（接替 v2/v3，九项带重验条件：⚠️85 续核+e2013-05-08 换锚/email 余 10 封/xAI 首披露/SpaceX 10-Q 富矿/documents 页脚/X 帖 2020 加密等）。
- **主路径探针 15/15**（tools/v12r09-probe.js 端口 9355：首页→账本→语录→检索→资源五页，版本戳×2/ps-row 124/qs-card 107/✓15◎83/索引 383/rs-item 49/链接连通/390 零溢出）；QA 截图 2 张。
- **工程记录**：①三口径 DOM 锚点定位——深读 5=controversy.html 五章节 id（union/twitter/sec-sec/sec-pedo/autopilot）、财务 4=finance.html 四公司章节、编年史 53=cy-ev、X 帖=tweet-card；②search.html 索引变量探针用 typeof 链降级取值一次命中 383。
- 成果提交 1005b4a+生成物 384e812；下一轮预告：R10 事件档案 2023–2026 补档（etype 五类枚举硬约束，事件 16→20，v11.11.0）——America Party 政治帖组按 R02 留档整体移交本轮双写语境。

### R10（2026-10-07，v11.11.0）
- **EVENTS 四档（16→20）**：e2023-11 Grok 线（milestone/month，6 材料）/e2025-06-22 Robotaxi 落地（milestone/day，7 材料=R02 四卡弧线全接入）/e2026-07 Optimus 产线（milestone/month，5 材料）/e2024-07 政治参与与 America Party（risk/month，**正反并陈**：facts 双写立场与批评+external 三镜像帖 single-party state 逐字+178+ 池检索锚——R02 移交条款落地）。
- **口径红线闭环**：309（时间轴独立）+58（吸收）+20（档案记录）=387（索引）；etype 分布 milestone 8/risk 3/deal 5/gamble 3/start 1；材料 23 份 kind 全在八类；external 三帖 HTTP 200 实测+13 站内锚跨页断言。
- **验证**：verify 9/9（索引 387）；**CDP 探针 19/19**（端口 9356）；QA 截图 2 张。
- **工程记录**：①新档英文文案裸双引号三连炸+第一轮批量修复正则过宽误伤历史档 18 行——`git checkout --` 单文件还原后弯引号重写一次通过（教训：批量修复脚本必须先圈定作用范围）；②no_quote_note 必须 {zh,en} dict（render_event t() 取键）；③sed 链式自噬再现（以旧 bump 为底本 sed 生成新 bump 双规则互吃）——Write 全新（红线重申）；④探针首跑服务器未起（上轮清理后忘重启）DOM 全挂属环境非页面。
- 成果提交 d20972f+生成物 d612d1d；下一轮预告：R11 编年史近年补齐+deep-dive-06《xAI 三年志》新页七件接入（v11.12.0）——模板逐字克隆 deep-dive-05、site-nav 断言/verify 页数 38→39/sitemap 不动。

### R11（2026-10-07，v11.12.0）
- **chronicle +11 条（53→64）**：tesla 7/spacex 2（含 SpaceX IPO 定价）/x 2——全克隆 cy-year/cy-ev 结构逐条深链；Neuralink 无四段制归段弃收录 EXPANSION。
- **deep-dive-06.html《xAI 三年志》**：逐字克隆 dd05 全结构，公司志读法五章（章程/Grok 四个月/收购 X/成绩单/资本线与披露缺位）；引语全一手锚。
- **七件接入**：site-nav 注册+重注入 40/40；索引新类型「深读长文」五章入册+编年史断言 64；verify 锚点计数 n_dd（先例式）；新页含 span——**站点 span 15→16**；sitemap 未动；build-longread 幂等跳过；互链 7 处 fetch 验证。
- **验证**：verify 9/9（39 页/索引 403）；**CDP 探针 20/20**（端口 9357：含 aria-current 导航高亮/双语/TOC/互链跨页/390 双页）；QA 截图 2 张。
- **工程记录**：①dd05 克隆源无版本 span——按任务书④新页补 span，bump 断言 15→16；②dd06 索引初版单条页名 id 无页面锚（verify 差 1）→改五章 s1-s5 各录一条对齐锚点计数；③修正链：锚点计数与索引条目必须「同一套 id 口径」。
- 成果提交 bef4b63+生成物 d90d95f；下一轮预告：R12 深读新篇 II（deep-dive-07，页数 39→40，v11.13.0）——Robotaxi 落地考 vs Musk 政治参与 2024–2026 择素材扎实者，同七件接入。

### R12（2026-10-07，v11.13.0）
- **择题：Robotaxi 落地考开工**（素材扎实：账本逐字×2+R02 四卡+事件档 7 材料）；**政治主题落选入 EXPANSION 候选池**（e2024-07+三镜像帖+178+ 池已探明，待专属轮次，页数 40→41 时顺位第一）。
- **deep-dive-07.html《Robotaxi 落地考》**（18.3KB 克隆 dd05 骨架）：五章——欠账的形状（承诺簇+promises 五案不设 robotaxi 案的核查发现）/We,Robot（Cybercab 逐字）/奥斯汀弧线（四帖逐字）/一周年口径/**指控·回应·本站核查三段体**（「两半都真、分别可核」）。
- **promises 互链**：条件句「若有」实测不适用（五案无 robotaxi 卡，0 命中）——不造互链，制度性排除本身写入正文为核查发现。
- **七件接入**：site-nav 41/41（五组 40 页）/索引深读长文 5→10/verify n_dd 扩展/新页 span（**17 处**）/sitemap 未动/longread 幂等/互链 6 处 fetch。
- **验证**：verify 9/9（40 页/索引 408）；**CDP 探针 18/18**（端口 9358）；QA 截图 2 张。
- **工程记录**：①英文转义引号 `\\"` 字面反斜杠入 HTML——写入前弯引号化（R10 教训变体）；②误执行旧 bump 一次（同值无实害）；③「条件句互链」纪律：任务书「若有…则」实测不适用时如实记录不硬造。
- 成果提交 08c934b+生成物 d548ede；下一轮预告：R13 资源扩容（xAI/Grok 生态+官方补，49→58±，v11.14.0）——resources-data.py 字段 13 个一个不少，validate() 拒生成不许绕过，每条核活记 http 三路法。

### R13（2026-10-07，v11.14.0）
- **RESOURCES +5（49→54，validate() 全过零绕过）**：sec-edgar-spacex（official，SpaceX CIK 1181412 上市后披露通道）/docs-xai（Grok API 官方文档）/tesla-support（**三路法第三路**：curl·WebFetch 403、服务端读取器 200，同 xai-official 先例）/xai-org-github（org 入口；grok-1 实测 52,236 stars/push 2024-08）/spacex-ir。类别迁移 official 11→14、opensource 9→10、tools 8→9。
- **宁缺毋滥**：候选 7 实收 5（x.ai/models 000 弃、ownersmanual 403 弃、edgar/search 403 弃、xai-news 重复不收）；58± 以核活结果为准。
- **验证**：verify 9/9（索引 413）；**CDP 探针 14/14**（端口 9359：五新条 r- 锚/rs-item 54/EDGAR 外链/stars 在页/三路法注记/390）。
- **工程记录**：①插入锚 `\n    \},\n]` 匹配非列表尾结构写坏文件——git 单文件还原后锚改 `]\nACTIVITY_ENUM` 唯一化；②重插锚吃掉原条闭合 `},`——py_compile 定位按行补；③python -c 转义地狱再现——锚逻辑文件化（红线）；④资源索引 id 形态=r-<id> 前缀。
- 成果提交 377f599+生成物 f76a1d6；下一轮预告：R14 质量节点②互链+检索审计（v11.15.0）。

### R14（2026-10-07，v11.15.0）——质量节点②
- **互链路①**：companies 驱动自动增长核对（R13 新资源自动入三档案资源行；事件联动 24≥20+）。
- **互链路②**：三方共现扫描 tools/v12r14-xlinks.py 入册（Neuralink 簇 7 候选）→人工裁决 **6 对新增**（e2024-01-29 +3：e2019-07-16 弧线起点/i2024-01-29 同日访谈/i2019-11-12；e2026-02-10 +1：i2026-07-23；e2023-11 +1：i2026-02-05；e2024-07 +1：e2025-11-06）；材料 89→95；锚点跨页 fetch 全验证。
- **修 bug**：e2025-03-28 href=None→镜像检索锚；余 8 处 None=历史媒体占位体例如实保留（探针按档断言）。
- **检索审计**：抽 30 条——命中/<mark> 高亮/日期升序/类型过滤 aria-pressed/清除恢复 413/aria-live/URL 回填/**Ctrl+K 补齐**（页内聚焦+全局跳转，输入态不劫持）/**noscript 补齐**；双语；390 双页。
- **验证**：verify 9/9（索引 413）；**CDP 探针 21/21**（≥15 达标）。
- **工程记录**：①互链集成断言曾用磁盘旧文件验证内存态——改 exec(compile(s)) 内存验证后写盘；②探针断言范围纪律：全文件一刀切会误伤历史体例（8 处 None）——按档定位。
- 成果提交 606f2f3+生成物 5de34f6；下一轮预告：R15 美术·报头刊头体系（v11.16.0）——改刊头须改 site-nav.py 模板重注入，Vol./No. 期号由 __BUILD_COMMIT__/VERSION 派生。

### R15（2026-10-07，v11.16.0）——美术四轮 I
- **刊头三件套**（site-nav.py 模板一次改动 41/41 重注入，零逐页手改）：①Vol./No. 期号=Vol. XI（主版本罗马数字）·No.（VERSION 同源 site-version-val span，bump 自动覆盖）；②日期线=构建日北京时间中文+data-en 英文对称；③eyebrow 体系（dateline 0.22em 小帽字/issue 0.18em/volno 0.14em 细双线左缘）。
- **章节题花（纯 CSS）**：cy-co/fn-co/ct-ch/lr-sec 四族 h2 统一 3px double 细双线+0.05em 字距。
- **对比度实测**：mh-volno 浅 7.05/深 7.05（≥4.5，CDP computed-style 实算含背景上溯）。
- **before/after 八组**：四页样本×双视口入 qa/v12/round-15/{before,after}/。
- **span 口径演进**：刊头期号 span 上墙→全站 58（41 刊头+17 存量，随页数增长）——bump 改通用版（argv 传版本+无残留断言），R16–R19 复用。
- **验证**：verify 9/9（版本一致性 58 span 全量）；**CDP 探针 14/14**（≥6 达标）。
- **工程记录**：①期号初版纯文本→改 span 同源（bump 兜底防 stale）；②span 总数定死断言作废（随页数增长）——通用 bump「无残留」式；③node 宽匹配 site-version-val 会计入正文提及——计数须精确 span 模式（R01 教训跨语言复现）。
- 成果提交 ef9c143+生成物 7828766；下一轮预告：R16 美术·正文杂志版式（纯 CSS 零 HTML，v11.17.0）——drop cap 双语两形态/引语块题花三族/基线 16.5px/720px 锁定/print 媒体模拟。

### R16（2026-10-07，v11.17.0）——美术四轮 II
- **纯 CSS 零 HTML（style.css +1.8KB）**：①drop cap（lr-* 首段 ::first-letter 衬线 3.1em float 下沉+small-caps；390 降级加粗首字）；②引语题花三族统一（lr-sec/sv-node/pv-case blockquote 大引号 ::before+正文左移 30px+实线竖）；③边注分野（lr-note 虚线框纸底 vs 引语实线竖）；④基线 --fs-body 16.5px 锁定（探针 computed）+段距 12px。
- **print 模拟**：题花 content:none+首字降级；**reduced-motion** 显式压平。
- **验证**：verify 9/9；**CDP 探针 18/18**（首字 float/字号/衬线/题花三族/分野/基线/390/print/reduced-motion）；QA 截图 3 张（dropcap/print 模拟/390）。
- **工程记录**：①题花左移被既有 .lr-quote .lr-quote-zh 高特异性 margin 压制——并入选择器组提优先级（首跑 17/1 修正）；②en/zh 双形态实现口径：页面 lang=zh-CN 无 per-paragraph lang，CSS 无法按文种分支——单形双用如实注记。
- 成果提交 326ae5a+生成物 ae2a361；下一轮预告：R17 美术·图表 hatch 纹理（v11.18.0）——纯 CSS/SVG 纹理族。
