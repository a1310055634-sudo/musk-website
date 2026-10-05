# V12-20 任务书（颗粒度·内容扩容 · 复古杂志版式深化 · 一手信息增量）

> 「马斯克商业志 MUSK, INC.」V12-20 升级计划（2026-10-06 立项，共 20 轮，目标 v12.0.0）。
> 本文件是本计划唯一任务书正本，含定时任务提示词（见文末节）；轮次账本为 `V12-PROGRESS.md`（R01 建立）。
> 前序：V9-20 二十轮（v8.1.0→v10.0.0，V9-20-PROGRESS.md）、V10-15 十五轮（v10.1.0→v11.0.0，V10-15-PROGRESS.md）、
> v11.1.0 复古杂志美术增量（用户选定方向落地，58d0b85+ba47824）。**不继承 V9-20/V10-15 计数，不得因旧账本写「已完成」而退出。**

## 三大目标

1. **一手信息增量**：X 帖断代回捞（2025-08→2026-10 十五个月空白）+ 早期加密（2018–2019、2002–2010 账本）+ 访谈/email/文档消化 + 引语 101 块逐条核验。
2. **颗粒度与结构**：事件档案 2023–2026 补档、编年史近年补齐、深读专题新篇 2 篇、资源扩容（xAI/Grok 生态）、互链扩展。
3. **美术：复古杂志从令牌层推进到版式层**——v11.1.0 只落地了令牌（墙纸），本计划落家具：报头刊头、正文版式、图表复古化、封面构图、微交互统一。

## 本地模式（硬纪律）

- **只改本地**：每轮本地 git 提交，一律 **不 push、不 fetch 后合并远程、不改写已有历史、不做云端发布与 Pages 验证**。
  本地当前领先 origin/main 约 83 提交（含前序计划），全部待用户自行推送。
- 第 20 轮输出「待发布清单」等用户验收；20 轮全部本地验收通过后，后续触发**静默退出**（不改文件不加版本不提交）。
- 本任务无人值守：自主完成设计、代码、测试与本地提交，不逐轮询问；遇权限/来源/环境阻塞保存现场如实报告，不假装完成。

━━━━━━━━━━━━━━━━━━━━
一、项目位置与启动检查
━━━━━━━━━━━━━━━━━━━━

项目目录：`D:\vibe coding\musk-website`
本地预览：`python -m http.server 8766 --bind 127.0.0.1` → http://127.0.0.1:8766/

参考快照（**执行时必须核对实际，不可盲信**）：
- main @ ba47824 附近，VERSION `11.1.0`（复古杂志令牌已落地）；origin/main 停在 355fc0d（v7.9.0 时代）。
- 口径基线：38 页面 / 账本 119 / 一手文档 27 / 访谈 47 / X 帖 34 / 语录卡 107（引文块 109，白名单豁免 2）/
  事件档案 16 档 / 资源 49 条 / 检索索引 354 / 编年史 53 / 修订锚点 227 / verify.py 9 项。
- 关键路径：`tools/*.py` 生成器全家桶（build-events / build-timeline-events / build-network / build-company-files /
  build-capital / build-ledger-links / build-search-index / build-resources / resources-data / sync-changelog /
  build-revisions / build-epub / build-sitemap）、`style.css`、`app.js`、`cite.js`、`verify.py`、
  `EXPANSION.md`（卷首=缺口清单 v2，五项带重验条件）、`V12-TASKBOOK.md`（本文件）、`DEVLOG.md`。
- 美术试衣间：`preview-v12.html`（noindex，非正式页面）——美术轮先在试衣间出样，用户方向已定（复古杂志），
  美术轮直接按本任务书执行，before/after 用 `git stash push -- style.css` 取同取景真 before 配对。
- CDP 探针惯例：headless Chrome 端口从 **9333 起步递增**（9227 被 aDrive.exe 占用致挂死），全新 user-data-dir，
  探针脚本 `tools/v12rNN-probe.js`，断言数与结论记入账本。

每次触发固定启动序列：
1. `cd` 项目目录；`git branch --show-current` 须为 main；`git status` 若有未知改动，先识别归属
   （本计划未收尾工作 / 用户独立工作），保留用户工作，**禁止 reset --hard / clean -fd / 整仓 checkout**。
2. 读 `DEVLOG.md` 头部、`CHANGELOG.md` 顶部三条、`cat VERSION`。
3. 读 `V12-PROGRESS.md`（R01 建立后）判断本轮；检查 `.v12run.lock`，有效锁直接退出（不动轮次），
   确认旧实例已死（进程+仓库静默>15min）才可恢复遗留锁。
4. 建锁：`.v12run.lock` 写入运行标识/时间/轮次；结束必须删除。锁不入 git（R01 补 .gitignore；
   若被暂存立即 `git reset` 该文件）。
5. （进入美术轮 R15–R19 时）先读 `qa/v11/`（如无则 qa/v9-20/round-15..19）的令牌层成果记录，方向不回切。

━━━━━━━━━━━━━━━━━━━━
二、轮次、版本与 Git 规则
━━━━━━━━━━━━━━━━━━━━

- 每次触发完成一个未完成轮次；上轮中断先恢复。成功轮次共 20。
  失败/空触发/重复检查/仅补提交不增加轮次；一轮未验收不进下一轮。
- 20 轮全部本地验收通过后，后续触发静默退出。
- 版本步进：R01=`v11.2.0` → R19=`v11.20.0`（每轮 minor+1）→ R20=`v12.0.0`（收官升 major）。
  每轮必 bump，以 VERSION 实测为准不降级。版本三件套同步：VERSION 文件、app.js 内 SITE_VERSION、
  全部页面 site-version-val span（正则批量替换脚本模式，替换计数须打印；新页面纳入替换范围）。
- Git：直接在本地 main 逐轮提交，提交信息带 `[V12 Rxx]` 前缀+成果摘要；
  每轮原则上一个成果提交+一个账本回填提交。**绝不 push、不改写已有历史**。CRLF 警告无害，忽略。
- 账本 `V12-PROGRESS.md` 与 git 相互核验：已有成果提交的轮不重复实现；状态表列用「本地提交哈希」。

━━━━━━━━━━━━━━━━━━━━
三、内容纪律（沿用前序计划，全部硬约束）
━━━━━━━━━━━━━━━━━━━━

A. 第一手信息：
- 逐字引语必须有原文锚：elonmuskarchive.org 镜像详情页 / 官方 transcript（ted.com 页内 JSON "transcript"
  字段 / Rev.com / lexfidman.com 官方稿 / wordpress 六分册自架站 / stockanalysis.com 财报稿——该站
  Cloudflare 拦 curl 不拦 WebFetch）/ SEC EDGAR 原文。查不到原文不写，宁缺毋滥。
- 镜像管线已知坑：`/agents/index` 清单 2023+ 触 1000 上限且 offset 无效——**2023 以后深水区必须用
  `/agents/search` 精确短语检索**；正文逐词 span 序列化——去标签不插空格还原后检索；
  type=interviews 库 161 场 / keynote 60 场 / speech 21 场（全部 hasTranscript；video 类正文在详情页剥标签抽词）。
- X 帖日期用 snowflake 解码对表：(id>>22)+1288834974657 → UTC，条目内注明口径。
- 媒体转述需两源印证；引语保留英文原文+中文对照，永不混写。
- 弃收件写入 EXPANSION.md（含原因与重验条件）；模板逐字克隆站内既有结构（类名一个不改）。

B. 资源板块（增量轮沿用）：
- 只收「链接+一句话简介+元数据」，不复制外部正文；外链不构成运行时依赖，资源页 file:// 离线可读。
- 元数据字段：url / name(zh,en) / desc(zh,en) / category / 语言 / 活跃度(维护中|停更|存档) / 许可 /
  收录理由一句 / 关联公司 / 核活日期。
- 每条 URL 实访核活（curl http_code 或 WebFetch，路径如实注记）；GitHub 记 stars+最近提交年份
  （api.github.com 无认证，注意限流串行）；死链如实标「存档」不删。
- 数据单一事实来源 `tools/resources-data.py`（validate 不过拒生成），禁止手写 HTML 条目。

C. 美术（基线已变更，注意）：
- **基线 = v11.1.0 复古杂志令牌方向（奶油纸/暖黑/深棕强调），不回切旧深色基调，不再换向**；
  公司色标语义不变（可调值不可换语义）；不换技术栈；不加运行时 CDN/远程字体。
- 每个美术轮 before/after 截图（桌面 1440×900 + 390×844；四页样本 index/survival-2008/timeline/capital-evolution；
  取景教训：先滚到目标组件入画再拍，cap/net 在 390 是清单形态属回归证据非缺陷）。
- prefers-reduced-motion 全覆盖；正文默认可见；320/390/768 三视口零横向溢出；对比度每处改动实测 ≥4.5。

━━━━━━━━━━━━━━━━━━━━
四、20 轮实施计划（文件级细节）
━━━━━━━━━━━━━━━━━━━━

【R01 基建与缺口清单 v3｜v11.2.0】
建 `V12-PROGRESS.md`（基线快照+20 轮状态表+恢复指引，格式沿 V10-15）；.gitignore 补 `.v12run.lock`；
把三大缺口盘成可执行清单写入账本（EXPANSION 卷首清单 v2 升 v3）：①X 帖断代 2025-08→2026-10
（先用镜像 /agents/search 探 5 个主题短语确认可回捞量，写探明结果不立条）；②引语 101 块核验
（以 qa/v10-15/round-03/unmatched-itemized.tsv 为底册生成 v12 工作册 TSV：块id/现来源/重验路径/结论四列）；
③email 候选 30 封（清单源 qa/v9-20/round-06/sources/emails.json）核对在册状态。
验收：verify 9/9；账本+工作册齐备；提交 [V12 R01]。

【R02 X 帖断代回捞 III（2025-08→2026-10）｜v11.3.0】
文件：x-posts.html、build-search-index.py（X 帖断言 34→40±）、EXPANSION.md、CHANGELOG。
动作：镜像 /agents/search 主题短语制（xAI 融资、Grok 4、Grok 5、Optimus 量产、robotaxi、America Party 等），
逐条 /agents/transcript/{id} 或详情页取原文；snowflake 解码对表；候选 6–10 条择优 4–8 立卡。
新卡严格克隆 tweet-card 五件套，时间序插入（锚=下一张既有卡开标签，new=新卡块+anchor 拼回）；
断言每卡 tweet-zh==1、tweet-date 链接唯一。镜像 1000 上限坑：只走 search 不走 index。
验收：verify 9/9；索引断言一致；CDP 探针（新卡渲染+互链+双语+snowflake 口径注）≥8 断言全过。

【R03 X 帖早期加密 I（2018–2019）｜v11.4.0】
同 R02 管线。现有 2018–2019 仅 17 条：候选 "funding secured" 2018-08 前后系列（SEC 案语境）、
SolarCity 收购、Pravda 2018-12、2019-02 Model Y 发布、2019 星舰犹他滩涂首曝。
目标 x-posts 34→38±。年份分组归档正确（页内 2018/2019 组）。

【R04 账本早期加密（2002–2010）｜v11.5.0】
文件：primary.html（账本条目模板逐字克隆）、build-ledger-timeline.py、build-search-index.py（账本断言）、
build-epub、CHANGELOG。现有 2002–2010 仅 9 条。候选（全部走一手锚）：2002 SpaceX 创立内部备忘
（镜像/公开信源两源印证）、2004 Roadster 白皮书联名、2006 Master Plan 一号（已在文档馆，账本立行互链）、
2008 Falcon 1 第四次入轨（官方更新信原文）、2008 圣诞节 Tesla 险些破产（CNBC/SEC 8-K 两源）、
2010 IPO 敲钟（nasdaq 官方影像文字稿）。+5~8 条，条条有锚，找不到锚的写 EXPANSION 弃收。

【R05 访谈消化轮｜v11.6.0】
文件：interviews.html（article.iv-item 六件套克隆）、断言、CHANGELOG。
必做重验（缺口清单 v2①）：60-minutes-2012（CBS 官网/转写服务两源）、lex-438（lexfridman.com 官方稿）。
镜像 interviews 库挑 4–6 场有逐字稿且站内未收的（避开已收 i2016-09-27/i2022-04-14/i2023-11-29 等 47 场）。
目标 +4~6 条。日期锚官方库优先，无把握不立条；逐字源 URL 留档进账本「核实来源留档」节。

【R06 email 库双源核验 I｜v11.7.0】
文件：documents.html（doc-article 模板）、断言、CHANGELOG。以 R01 工作册为准，
处理 30 封候选的前 15 封：逐封双源（原始披露媒体+镜像/法庭文件），双源齐才立，单源降级留档。
重点：Twitter 私信库余量（2022 收购期）、OpenAI 诉讼披露邮件、Tesla/SpaceX 内部信。
目标 +5~8 条文档。

【R07 email 续 + 文档馆近年化｜v11.8.0】
email 后 15 封同 R06 管线；文档馆近年化：2024–2026 Tesla 10-K/proxy 关键段摘录（SEC EDGAR 直取）、
xAI 相关披露（若有）、SpaceX Starship 进展官方更新信 2025–2026。目标合计 +4~6。

【R08 引语 101 块逐条核验（质量轮）｜v11.9.0】
以 R01 工作册 TSV 逐条重验：other-official 73 / earnings-call 20 / edgar 6 / jre 1 / ted 1。
路径：官方页直取→镜像 search→EDGAR 全文检索→stockanalysis（earnings）。三态结论：
✅核到原文（补锚链接进 verify 白名单外正册）/ ⚠️降级标注（引语保留但注「转引，原文未获」）/
❌撤下（整块移除+EXPANSION 弃收记录）。**改 verify.py 断言须保留原约束精神并在 CHANGELOG 说明理由。**
验收：工作册 TSV 全 101 行有结论；verify 9/9；语录卡/引文块计数零漂移（撤下的同步删卡）。

【R09 质量节点①：第一手盘点总表 v3｜v11.10.0】
把 R02–R08 增量入册后的全量口径重新盘点：各类型计数、逐类型年份分布图（表）、缺口清单 v4 写回
EXPANSION 卷首（接替 v2/v3）。质量节点①验收：页面/索引/生成器三口径零漂移；主路径探针全过。

【R10 事件档案 2023–2026 补档｜v11.11.0】
文件：tools/events-data.py（EVENTS 追加，etype∈五类枚举、materials.kind∈枚举、validate() 过），
重跑 build-events / build-timeline-events / build-network / build-company-files / build-ledger-links /
build-search-index（断言同步）。候选四档：Grok 从聊天到 OS（2023-11→2026）、robotaxi 落地
（promises 页欠账→2025-06 Austin 首发→扩张）、Optimus 量产线、Musk 政治参与与 America Party（2024-07→）。
**口径红线：时间轴独立记录数=索引一手材料−被吸收数−events 档案记录（探针断言防漂移）**；
新建档卡深链 fetch 逐条验证。事件档案 16→20±。

【R11 编年史近年补齐 + 深读新篇 I｜v11.12.0】
chronicle.html 编年史 53 条的 2023–2026 段补齐（+8~12 条，从账本/事件档案派生口径）；
新建 deep-dive-06.html《xAI 三年志》（模板逐字克隆 deep-dive-05 结构）：**新页面接入全套管线**——
site-nav.py 注册重注入、build-search-index 新类型断言、verify.py 页面清单、sitemap 后 R20 统一更新、
版本 span 覆盖新页。验收：新页 verify 全绿+探针+三视口零溢出。

【R12 深读新篇 II｜v11.13.0】
deep-dive-07.html《Robotaxi 落地考》或《Musk 政治参与 2024–2026》（择素材更扎实者，另一篇进 EXPANSION）。
同 R11 接入全套管线。引用全部一手锚；争议内容正反并陈（controversy 体例）。

【R13 资源扩容（xAI/Grok 生态+官方补）｜v11.14.0】
文件：tools/resources-data.py + build-resources.py，断言同步。采集：Grok API 文档、x.ai 官方页、
开源模型/权重页、Musk 主题数据工具新;if 2025–2026 活跃、官方类补强（tesla.com 支持页/SpatialX? 择实核活者）。
每条核活+元数据齐备（纪律 B 全字段）。目标资源 49→60±（official 11→14、opensource 9→12、
community 21→24、tools 8→10 上下）。GitHub 记 stars+最近提交年。

【R14 质量节点②：互链扩展+检索审计｜v11.15.0】
互链扩展：资源↔新档案（R10 四档）互链、账本↔访谈↔事件三方共现扫描（同段共现取证法，V9-20 R98 模式），
+6 对以上；检索审计：354→增量后全量抽 30 条验证命中排序与高亮、Ctrl+K 键盘流复测。
质量节点②验收：全流程探针 ≥15 断言（互链跳转/检索/无 JS/390/file://）；verify 9/9。

【R15 美术·报头刊头体系｜v11.16.0】
文件：style.css（组件层）+ 各页 masthead 区微调（HTML 改动最小化，优先纯 CSS+既有 DOM）。
动作：刊头杂志化——Vol./No. 期号（版本号派生）、日期线、栏目眉（eyebrow 小字距排版）、
章节开篇题花（细双线+小帽字）；深浅双主题变量各配一套，对比度实测。
四页样本 before/after 八组截图；探针（期号=版本三件套一致/双主题/三视口）。

【R16 美术·正文杂志版式｜v11.17.0】
文件：style.css。drop cap 首字下沉（lr-* 长文首段，::first-letter，en/zh 双语形态都定义）、
引语块题花（大引号+出处竖线，三族容器 .lr-quote/.sv-node blockquote/.pv-case blockquote 统一升级）、
脚注/边注体例（编者注与引语区分再强化）、lr-* 长文阅读节奏（段距/标题层级复核，基线 16.5px/720px 不动）。
reduced-motion 与 print 形态复查。before/after 八组。

【R17 美术·图表复古化｜v11.18.0】
文件：style.css。gx-*/cap-*/net-* 三图雕刻风：hatch 纹理（SVG pattern 或 repeating-linear-gradient）、
单色阶+朱红/深棕强调的双色纪律、节点形状语言保持（R17 成果不动摇）、图例刻度等宽字深化。
**数据编码不动**（ribbon 线宽=生成器值断言、「示意非等比」「不伪装精确」标注保留）。
before/after 六组（390 清单形态组=回归证据）。

【R18 美术·专题封面化+首页封面故事｜v11.19.0】
deep-dive-01~07 + survival-2008 + grok 开篇封面构图（大标题+图版+题注三段式，纯 CSS+既有 DOM）；
index.html 首页改「本期封面故事」逻辑：导读区+目录页感的栏目索引（feature-lead/path-cards 既有骨架重排）。
三入口视觉不动摇（R16 成果）。EN 标题不破版；320/390/768 复扫。

【R19 美术·微交互统一+质量节点③｜v11.20.0】
transition 审计清单化（TSV 入 qa/v12/round-19）：归一到 --t-fast/--t-slow 两档；
hover/active/focus 三态一致（杂志语言：墨线 hover、按压态）；组件进场动效统一；
reduced-motion 逐组件 CDP 模拟实测；性能复测（五页 load/体积，本地条件如实记录）。
质量节点③：R15–R18 美术四轮 before/after 齐备入 qa/v12/。

【R20 全站验收与待发布清单｜v12.0.0】
1. 口径总核对入账本：页面数（38+新页）、账本/文档/访谈/X 帖/语录卡/索引/事件档案/资源/编年史分列统计。
2. 生成器全家桶幂等重跑；revisions/EPUB/sitemap.xml（全部页 URL）/CHANGELOG/DEVLOG（追加 V12 交接要点）/
   V12 账本收官。
3. 终验：verify.py 9/9；CDP 全站终检探针（主路径+双语+390+file://+资源页+新页）；三视口全站复扫零溢出。
4. 版本三件套 → 12.0.0；本地提交收官。
5. 输出「待发布清单」（不推送）：待推提交数与哈希范围、一条推送命令（git push origin main）、
   推送后 Pages 验证步骤（线上 VERSION=12.0.0；resources.html 与新专题页 200；span 抽查）。
完成条件：①20 轮全验收 ②15 个月 X 帖断代补齐且第一手缺口如实盘点 ③美术版式层四轮截图可辨
④桌面/手机/中英/离线通过 ⑤旧页锚点保留（断链零）⑥事实/资源/图表来源清楚 ⑦产物/版本/交接一致
⑧本地 v12.0.0 就绪+待发布清单已输出。

━━━━━━━━━━━━━━━━━━━━
五、每轮固定流程（十六步）
━━━━━━━━━━━━━━━━━━━━

锁/进度/分支/工作区检查 → 定本轮范围与验收 → 读相关文件+改前截图 → 实现 →
核对事实源/双语/旧链接/手机布局 → 同步数据与构建产物（改一手页必跑 build-ledger-timeline /
build-search-index（断言同步）/ build-epub；CHANGELOG 后 sync-changelog；提交后 build-revisions+EPUB
重刷为第二提交）→ CHANGELOG+版本三件套+账本 → 最后一次 HTML 改动后重建 EPUB → verify.py 9 项全绿 →
改 JS 跑 node --check → CDP 探针实测（断言数与结论记录在案）→ 修复复验 → QA 证据存 qa/v12/round-NN/
（桌面+390 截图+验收记录+来源留档；美术轮 before/after）→ 本地提交 [V12 Rxx]（**不 push**）→
账本回填第二提交 → 释放锁 → 输出简报（本轮编号/完成内容/验证结果/本地提交哈希/下一轮）。

红线：不能只查媒体查询就宣称手机通过；不能只数 data-en 就宣称双语通过；不能只跑 verify.py 就宣称
视觉交互正常；不改校验器掩盖缺陷（确需调整须保留原约束+CHANGELOG 说明理由）；复杂 Python 改动写成
.py 文件执行（heredoc 中文/引号必失真）；工作区 CRLF/LF 混合，行级比较 rstrip('\r')；
第 20 轮前任何情况下不得执行 git push / git remote 相关写操作；React 无涉——本站为静态页+原生 JS，
CDP 表单赋值直接改 value 后派发 input 事件即可。

异常：检查失败修复本轮重验，不跳轮不冒充；来源不足降表述强度或留档弃收，不编造；环境阻塞保存现场
如实报告。计划完成后再次触发：静默退出。

━━━━━━━━━━━━━━━━━━━━
六、定时任务提示词正本（注册时逐字使用）
━━━━━━━━━━━━━━━━━━━━

你是「马斯克商业志 MUSK, INC.」V12-20 计划的自主工程师。项目目录 D:\vibe coding\musk-website，
任务书正本 D:\vibe coding\musk-website\V12-TASKBOOK.md（20 轮实施计划/验收标准/红线全在其中），先完整读它再动手。

固定启动序列（每次触发）：
1. cd 项目目录；git branch --show-current 须为 main；git status 有未知改动先识别归属，保留用户工作，
   禁止 reset --hard / clean -fd。
2. cat VERSION；读 V12-PROGRESS.md 判断当前未完成轮次；检查 .v12run.lock，有效锁直接退出。
3. 按任务书执行当前轮（一次一轮，一轮未验收不进下一轮），走完十六步固定流程。

红线：纯本地模式——绝不 git push、不做任何 remote 写操作、不做云端发布；每轮 [V12 Rxx] 本地提交+
账本回填；verify.py 9 项全绿 + CDP 探针实测才算验收；美术基线=v11.1.0 复古杂志方向不回切。
20 轮全部完成后（VERSION=v12.0.0 且账本 20 轮全 complete）：静默退出，仅输出完结状态报告，
不改任何文件。环境阻塞（来源不可达/权限拒绝/限流）：保存现场如实报告，不假装完成，不编造来源。
