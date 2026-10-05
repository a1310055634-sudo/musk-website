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
建 `V12-PROGRESS.md`（基线快照+20 轮状态表+恢复指引，格式沿 V10-15-PROGRESS.md；状态表列含「本地提交哈希」）；
.gitignore 补 `.v12run.lock`（若已被前轮误建暂存则 git reset 该文件）。
把三大缺口盘成可执行清单，写入账本「缺口清单 v3」节（EXPANSION 卷首 v2 加一行指针指向 v3，不整段搬）：
①X 帖断代 2025-08→2026-10：先用镜像 `/agents/search` 探 5 个主题短语（xAI funding / Grok 4 / Optimus
production / robotaxi Austin / America Party）确认可回捞量，只写探明结果不立条（立条归 R02）；
②引语 101 块核验工作册：以 `qa/v10-15/round-03/unmatched-itemized.tsv` 为底册，生成
`qa/v12/round-01/quotes-worklog.tsv` 四列（块id/现来源类型/重验路径计划/结论空列）；
③email 候选 30 封：以 `qa/v9-20/round-06/sources/emails.json` 为底册，逐封核对「是否已在 documents.html 在册」，
输出 `qa/v12/round-01/emails-worklog.tsv`（emailid/双源计划/在册状态/结论空列）。
验收：verify 9/9（基线不动，跑通即可）；账本+两份工作册齐备；提交 [V12 R01]。

【R02 X 帖断代回捞 III（2025-08→2026-10）｜v11.3.0】
文件：x-posts.html、tools/build-search-index.py（X 帖断言 34→38±，同步改断言数字）、EXPANSION.md、CHANGELOG。
采料（全部一手锚）：镜像 API 免钥——列表 `https://elonmuskarchive.org/agents/search?q=<短语>`（2023+ 深水区
**只走 search 不走 index**：index 2023+ 触 1000 上限且 offset 无效）；帖子原文 `/agents/transcript/{id}`；
正文为逐词 span 序列化——**去标签后不插空格直接拼接还原**再检索短语。候选主题：xAI 融资轮、Grok 4/5 发布、
Optimus 量产、robotaxi Austin 首发与扩张、America Party。snowflake 对表：(id>>22)+1288834974657→UTC，
与镜像标注日期互证，口径写进 tweet-note。择优立 4–6 卡。
新卡**严格克隆 tweet-card 五件套**（结构见「速查」节 §1），id 规则 `p{YYYY-MM-DD}`；时间序插入法：
定位下一张（更新日期）既有卡的 `<div class="tweet-card"` 开标签作锚，new=新卡块+"\n"+anchor 拼回，
行级比较 rstrip('\r')。**注意页内年份分组头**：2025-08 以后若跨入 2026 年，须仿既有年份组头结构新建
2026 组（类名一个不改）；无 2026 帖则不动组。
断言：新卡所在页 tweet-card 总数=34+新卡数；每卡恰 1 个 tweet-text+1 个 tweet-zh；tweet-date 链接
href 与卡 id 一致；全局 `<a class="tweet-date" href="#` 数=卡数（Permalink 唯一）。
验收：verify 9/9；索引断言一致；CDP 探针 ≥8 断言（新卡渲染/互链锚点跳转/双语切换 data-en/年份组归位/
snowflake 口径注存在/检索命中新卡）全过；qa/v12/round-02 存截图+来源留档（镜像 URL+解码时间戳对照表）。

【R03 X 帖早期加密 I（2018–2019）｜v11.4.0】
同 R02 管线与断言。现有 2018 年 10 条、2019 年 7 条。候选（镜像 ?year=2018/2019&page=N&sort=old
全量翻页——2018–2022 不触 1000 上限可走 index 列表）：2018-08-07 "funding secured" 前后系列
（含后续 SEC 案语境帖，站内已有 2018-08 六条须查重）、2018-12 Pravda 系列（站内如已有则弃）、
2019-03 Model Y 发布、2019-05 星舰犹他滩涂首曝后表态、2019-11 Cybertruck 发布前预热。
目标 x-posts →38±（R02+R03 合计 +8 左右）。查重法：候选帖镜像 id/日期与页内既有 `id="p…"` 对照，
同日多帖须逐条比对正文首 40 字符。

【R04 账本早期加密（2002–2010）｜v11.5.0】
文件：primary.html（账本条目模板**逐字克隆 ps-row 结构**，见「速查」节 §4）、tools/build-ledger-timeline.py、
build-search-index.py（账本断言 119→124±）、build-ledger-links.py、build-epub.py、CHANGELOG。
现有 2002–2010 仅 9 条。候选（**每条一手锚先核实再立**，注意：SpaceX 从未上市无 S-1，Tesla 2010 年才 IPO、
2008 年无 8-K——早期锚只能走官方新闻稿/后来 IPO 文件回顾/公开信源两源印证）：
2002 SpaceX 创立（官网 about 存档+公开两源）；2004 Musk 出任 Tesla 董事长（Tesla 官方 PR 存档）；
2006-08 Master Plan 一号发布（文档馆已有 d2006-08，账本立行互链 `documents.html#d2006-08`）；
2008-09-28 Falcon 1 Flight 4 入轨（SpaceX 官方更新信，web.archive 取原文）；
2008-12 NASA CRS-1 合同 16 亿美元（**NASA 官方新闻稿**，SpaceX 濒死翻生硬锚）；
2010-06-29 Tesla IPO（NASDAQ 官方存档+Tesla S-1，EDGAR 直取）。
+5~6 条。插入法：定位下一条（更新日期）`<li class="ps-row` 开标签作锚拼回；断言：ps-date Permalink
唯一、ps-quote 与 ps-zh 成对、id 规则 e{YYYY-MM-DD} 不与既有 119 条冲突（先 grep 全库查重再定 id）。
找不到锚的候选写 EXPANSION 弃收，不硬立。

【R05 访谈消化轮｜v11.6.0】
文件：interviews.html（article.iv-item 六件套克隆，见「速查」节 §2）、build-search-index.py（访谈断言
47→51±）、CHANGELOG。必做重验（缺口清单 v2①）：60-minutes-2012（CBS 官网片段页/转写服务两源逐字比对）、
lex-438（lexfridman.com 官方稿直取）。镜像扩收：type=interviews 库 161 场全部 hasTranscript；
查重法：先从 interviews.html 提取全部既有条目 id（i{YYYY-MM} 或 iYYYY-MM-DD）与日期清单存
qa/v12/round-05/existing.json，候选与清单对照，避开 47 场已收。挑 4–6 场站内未收、逐字稿可得的
（官库优先，第三方逐字稿须勘定）。id 规则从既有惯例（i2006-08 月精度 / i2016-09-27 日精度，按可用
日期精度选）。断言：iv-item 总数=47+新数；每条六件套齐全（h2/iv-meta/ctx/blockquote/iv-zh/after）；
blockquote 英文原文与 iv-zh 中文对照一一对应。逐字源 URL 留档进账本「核实来源留档」节。

【R06 email 库双源核验 I｜v11.7.0】
文件：documents.html（doc-article 模板克隆，见「速查」节 §3）、build-search-index.py（文档断言
27→31±）、CHANGELOG。以 R01 的 emails-worklog.tsv 为准处理前 15 封：逐封双源（原始披露媒体+
镜像/法庭文件/官方存档），双源齐才立条；单源降级为「留档待续」写 EXPANSION。重点：Twitter 私信库
余量（2022 收购期，Platform X 专题有互链位）、OpenAI 诉讼披露邮件、Tesla/SpaceX 内部信。
id 规则 d{YYYY-MM}（先 grep documents.html 查重）。断言：doc-article 总数=27+新数；每条
blockquote 与 zh-line 成对；doc-meta 三 badge（来源/Permalink/作者注）结构完整。目标 +4~6 条。

【R07 email 续 + 文档馆近年化｜v11.8.0】
email 后 15 封同 R06 管线与断言；文档馆近年化（SEC EDGAR 直取原文）：2024–2026 Tesla 10-K 风险因子/
proxy 关键段摘录、xAI 相关披露（EDGAR 搜 xAI Holdings/X.AI，若无可核活文件则如实记 EXPANSION）、
SpaceX Starship 进展官方更新信 2025–2026（官网/web.archive）。目标合计 +4~6。所有摘录保持
「原文摘录（blockquote）+zh-line 对照+本站注释（note）」三段体例。

【R08 引语 101 块逐条核验（质量轮）｜v11.9.0】
以 R01 工作册 `quotes-worklog.tsv` 逐条重验（底册构成：other-official 73 / earnings-call 20 /
edgar 6 / jre 1 / ted 1）。核验路径按优先级：官方页直取→镜像 `/agents/search` 精确短语（引语前 8–12
英文词）→EDGAR 全文检索→stockanalysis.com 财报稿（**Cloudflare 拦 curl 不拦 WebFetch，用 WebFetch**）→
ted.com 页内 JSON "transcript" 字段。三态结论填 TSV：✅核到原文（quotes.html 卡补原文锚链接）/
⚠️降级标注（引语保留，卡内注「转引，原文未获，两源转述一致」）/ ❌撤下（语录卡与对应账本引文块
**同步移除**+EXPANSION 弃收记录，防计数漂移）。
**改 verify.py 白名单须保留原约束精神并在 CHANGELOG 说明理由；不许为让数字好看而放宽断言。**
验收：TSV 全 101 行结论非空；verify 9/9；语录卡数=账本引文块数−白名单豁免数恒等式保持；
抽样 10 条人工复核口径记录进 qa/v12/round-08/。

【R09 质量节点①：第一手盘点总表 v3｜v11.10.0】
R02–R08 增量入册后全量盘点：各类型计数（页面/索引/生成器三口径并列）、逐类型年份分布表
（X 帖按年、账本按年、访谈按年，标出填补后的薄弱区）、缺口清单 v4 写回 EXPANSION 卷首（接替 v2/v3）。
质量节点①验收：三口径零漂移（脚本核对打印）；主路径探针（首页→账本→语录→检索→资源）全过；
探针断言数记录在案。

【R10 事件档案 2023–2026 补档｜v11.11.0】
文件：tools/events-data.py（EVENTS 追加四档），重跑生成器链：build-events → build-timeline-events →
build-network → build-company-files → build-capital → build-ledger-links → build-search-index
（事件档案断言 16→20，同步改断言数字）→ verify.py。
**枚举硬约束**：etype ∈ start/deal/gamble/milestone/risk（创业起步/资本运作/豪赌翻身/产品里程碑/争议时刻，
五类，ETYPE_LABELS 已定义勿扩）；materials[].kind ∈ ledger/document/interview/post/chronicle/feature/
image/external（八类）；id 规则 e{YYYY-MM-DD} 且不与 EVENTS 既有冲突；precision ∈ day/month/year。
候选四档：Grok 从聊天玩具到 OS（2023-11 Grok-1→2026，etype=milestone 或 gamble）、robotaxi 落地
（promises.html 欠账→2025-06 Austin 首发→扩张，etype=milestone）、Optimus 量产线（etype=milestone）、
Musk 政治参与与 America Party（2024-07→，etype=risk 或 deal，争议内容正反并陈）。
每档 materials 4–8 条（kind 多样化，ledger 深链用 `primary.html#e…`、文档用 `documents.html#d…`、
X 帖用 `x-posts.html#p…`，**所有深链 href 先 fetch 验证 200 且锚点存在**）。
**口径红线（探针断言）**：时间轴独立记录数 = 索引一手材料总数 − 被吸收数 − events.html 档案记录数，
等式必须闭环（V8 R8 的 160 漂移教训）。

【R11 编年史近年补齐 + 深读新篇 I｜v11.12.0】
chronicle.html 2023–2026 段补齐 +8~12 条（口径从账本/事件档案派生，条目结构现场克隆页内既有条目类名）；
新建 deep-dive-06.html《xAI 三年志》——**模板逐字克隆 deep-dive-05.html 全部结构**（head/hero/章节/
footer/版本 span），只换内容。**新页接入全套管线（七件，缺一不可）**：
①tools/site-nav.py 的 NAV_GROUPS「专题」组追加 ("deep-dive-06.html", "深读·xAI 三年志", "Deep Dive: xAI")，
跑 `python tools/site-nav.py` 全站重注入（幂等，顺带更新其头注释页数）；
②build-search-index.py 增 deep-dive-06 类型断言并重跑；
③verify.py 若有页面清单/页数断言则同步（页数 38→39，verify 输出口径随之）；
④版本 span 替换脚本覆盖新页（新页须含 site-version-val span）；
⑤sitemap.xml 暂不动（R20 统一更新）；
⑥build-longread.py 若管辖 deep-dive 族则重跑；
⑦新页内互链（≥3 处指向 x-posts/events/documents 既有锚）全 fetch 验证。
验收：verify 9/9；新页 CDP 探针（渲染/双语/390 零溢出/导航高亮 aria-current）≥6 断言。

【R12 深读新篇 II｜v11.13.0】
deep-dive-07.html《Robotaxi 落地考》或《Musk 政治参与 2024–2026》（**择一手素材更扎实者**开工，
未选主题连同已探明素材写 EXPANSION 候选池）。同 R11 七件接入管线。内容纪律：引用全部带一手锚
（镜像/官方/EDGAR）；争议内容正反并陈（站内 controversy 体例：指控/回应/本站核查三段）；
promises.html 若有 robotaxi 承诺条目则互链（欠账→现状闭环）。页数 39→40。

【R13 资源扩容（xAI/Grok 生态+官方补）｜v11.14.0】
文件：tools/resources-data.py（RESOURCES 追加）+ tools/build-resources.py 重跑 + build-search-index.py
（资源断言 49→58±）。**字段 13 个一个不少**（见「速查」节 §6）：id（^[a-z0-9-]+$）/url/name{zh,en}/
desc{zh,en}/category/lang/activity/license{zh,en}/reason{zh,en}/companies/checked/http/gh（GitHub 专用），
note 可选。validate() 返回非空即拒生成——不许绕过校验手工改 HTML。
采集方向：Grok API 官方文档、x.ai 官方页（model card/公司页）、开源权重页（若开源）、Starlink/Grok
社区工具新活跃者（2025–2026 仍在维护）、官方类补强（tesla.com 支持/车主手册页等）。每条
curl/WebFetch 核活记 http（三路法路径如实注记）；GitHub 走 api.github.com/repos/… 记 stars+pushed
（无认证限流=串行+sleep）。目标 49→58±：official 11→13、opensource 9→11、community 21→24、tools 8→10
上下（以核活结果为准，宁缺毋滥）。死链如实标 activity=存档 不删。

【R14 质量节点②：互链扩展+检索审计｜v11.15.0】
互链扩展（两路）：①资源↔R10 新档案互链（resources-data.py 的 companies 字段驱动 build-resources
生成 cf-resl 行，核对 build-company-files 重跑后深链 16→20+）；②账本↔访谈↔事件三方同段共现扫描
（写 tools/v12r14-xlinks.py：对 primary/interviews/events 同段文本做实体共现取证，命中+人工裁决
+6 对以上，插入互链前逐对 fetch 验证锚点）。检索审计：全站索引（R13 后约 370±）抽 30 条验证命中
排序/高亮/Ctrl+K 键盘流（含焦点陷阱）；无 JS 降级可读。
质量节点②验收：全流程探针 ≥15 断言（互链跳转/检索命中/清除筛选/aria-live/双语/390/file://）；
verify 9/9。

【R15 美术·报头刊头体系｜v11.16.0】
文件：style.css（组件层为主）+ 各页 masthead 区 HTML 微调（改动最小化，优先纯 CSS+既有 DOM；
masthead 由 site-nav.py 生成——**改刊头结构须改 site-nav.py 模板后重注入，不逐页手改**）。
动作：①Vol./No. 期号元素（由 __BUILD_COMMIT__/VERSION 派生，与页脚版本戳同源）；②日期线
（中文版式年月日+英文对称）；③栏目眉 eyebrow（小字号大字距）；④章节开篇题花（细双线+小帽字）。
深浅双主题（复古纸面/夜间）各实测对比度 ≥4.5。before/after：四页样本（index/survival-2008/timeline/
capital-evolution）×双视口=八组，取景先滚目标组件入画。
探针：期号文本=版本三件套一致/双主题切换/三视口零溢出/reduced-motion，≥6 断言。

【R16 美术·正文杂志版式｜v11.17.0】
文件：style.css（纯 CSS 轮，零 HTML 改动）。
①drop cap 首字下沉：lr-* 长文首段 ::first-letter，**en/zh 双语各一形态**（英文衬线大写下沉、
中文首字下沉网格对齐），390 视口降级为加粗首字（防溢出）；
②引语块题花：三族容器统一升级——.lr-quote（长卷）/ .sv-node blockquote（survival-2008）/
.pv-case blockquote（promises），大引号装饰+出处竖线，区别于编者注（纸底虚线）体例；
③脚注/边注体例：.note 族与引语块的视觉分野再强化；
④lr-* 段距/标题层级复核，**基线 16.5px/720px 探针锁定不动摇**。
reduced-motion 逐项复核；print 媒体模拟截图（关影/关题花）。
before/after 八组（reading.html 加入样本页）。

【R17 美术·图表复古化｜v11.18.0】
文件：style.css（纯 CSS 轮）。gx-*（timeline）/cap-*（capital-evolution）/net-*（companies）三图雕刻风：
①hatch 纹理（repeating-linear-gradient 斜纹或 SVG pattern，双主题各配色）；
②单色阶+朱红/深棕强调的「双色纪律」（复古杂志双套色印刷语言，语义色不换）；
③节点形状语言保持 V9-20 R17 成果（圆方菱圆三角 etype 编码不动摇）、图例刻度等宽字深化；
④「示意非等比」「不伪装精确」口径注保留（不可删）。
**数据编码不动**：ribbon 线宽=生成器值的断言复跑；390 清单形态组（cap/net 被移动端规则隐藏）
拍同取景 before/after 逐像素一致=回归证据。
before/after 六组；探针 ≥6 断言（线宽 CSS 变量值/形状类名/图例文本/口径注存在/reduced-motion）。

【R18 美术·专题封面化+首页封面故事｜v11.19.0】
①专题封面：deep-dive-01~07 + survival-2008 + grok 开篇封面构图（大标题+图版+题注三段式；
纯 CSS+既有 DOM，hero 区类名不改）；②index.html 首页改「本期封面故事」逻辑：导读区
（本期看点=最近三轮成果）+目录页感栏目索引（feature-lead/path-cards 既有骨架重排，不删三入口
.act 编号条）。
EN 标题不破版（data-en 往返断言）；320/390/768 复扫零溢出；新旧首屏对比截图差异显著
（像素 diff 报告入 qa）。
探针 ≥8 断言。

【R19 美术·微交互统一+质量节点③｜v11.20.0】
①transition 审计清单化：grep 全站 transition 出 TSV 入 qa/v12/round-19/，归一到 --t-fast(150–250ms)/
--t-slow(300–500ms) 两档（白名单逐个注明理由，仿 V9-20 R19 慢档白名单 12 处的做法）；
②hover/active/focus 三态一致（杂志语言：墨线 hover、按压态 .btn:active、:focus-visible 统一出口）；
③组件进场动效统一（reveal 族节奏一致）；④reduced-motion 逐组件 CDP 模拟实测（压平后仍可用）；
⑤性能复测：五页 load/资源体积，本地条件如实记录。
质量节点③：R15–R18 四轮 before/after 全部齐备清点入 qa/v12/（缺哪轮补哪轮，不 retro-fit 假证据）。
探针 ≥10 断言。

【R20 全站验收与待发布清单｜v12.0.0】
1. 口径总核对入账本（分列统计）：页面数（38+新页=40，verify 口径含 noindex 试衣间；正式 39+1）/
   账本/文档/访谈/X 帖/语录卡/索引/事件档案/资源/编年史/修订锚点。
2. 生成器全家桶幂等重跑（顺序）：site-nav → build-events → build-timeline-events → build-network →
   build-company-files → build-capital → build-ledger-links → build-ledger-timeline → build-resources →
   build-search-index → sync-changelog → build-sitemap（**40 页 URL 全量**，R11/R12 欠账在此清偿）→
   build-revisions → build-epub；git status 应零 diff（幂等证据打印）。
3. 终验：verify.py 9/9；CDP 全站终检探针（主路径五步+双语+390+file:// 自包含+资源页+deep-dive-06/07
   新页+print 抽查）；三视口全站复扫零溢出；node --check app.js/cite.js。
4. 版本三件套 → 12.0.0（替换计数打印）；本地提交收官。
5. 输出 RELEASE-CHECKLIST-v12.md「待发布清单」（不推送）：待推提交数与哈希范围（含 V9-20/V10-15/
   v11.1.0/V12 全部本地提交，约 100+）、一条推送命令（git push origin main）、推送后 1–3 分钟 Pages
   验证步骤（curl 线上 VERSION=12.0.0；resources.html/deep-dive-06/07 与三个专题页 200；span 抽查）。
完成条件：①20 轮全验收 ②15 个月 X 帖断代补齐且第一手缺口如实盘点 ③美术版式层四轮截图可辨
④桌面/手机/中英/离线通过 ⑤旧页锚点保留（断链零）⑥事实/资源/图表来源清楚 ⑦产物/版本/交接一致
⑧本地 v12.0.0 就绪+待发布清单已输出。

━━━━━━━━━━━━━━━━━━━━
四A、站内模板与断言速查（2026-10-06 实测提取；执行轮免侦察，但动手前仍须现场复核类名未变）
━━━━━━━━━━━━━━━━━━━━

§1 X 帖卡（tweet-card 五件套，x-posts.html）
```html
<div class="tweet-card" id="p2018-01-28">
  <div class="tweet-top"><span class="tweet-avatar">M</span><span class="tweet-who"><b>Elon Musk</b><span>@elonmusk</span></span><a class="tweet-date" href="#p2018-01-28" title="定位到本帖 · Permalink">2018.01.28</a></div>
  <p class="tweet-text">英文原文…</p>
  <p class="tweet-zh">中文对照…</p>
  <p class="tweet-note"><b>背景/后续：</b>…（snowflake 口径注写在此）</p>
</div>
```
id 规则 `p{YYYY-MM-DD}`；显示日期格式 `YYYY.MM.DD`；年份分组头结构现场克隆既有组。

§2 访谈条目（iv-item 六件套，interviews.html）
```html
<article class="iv-item" id="i2006-08">
  <h2 data-en="…">标题中文…</h2>
  <div class="iv-meta"><span class="iv-badge" data-en="…">来源中文</span><a class="iv-badge" href="#i2006-08" title="定位到本条 · Permalink">2006.08</a></div>
  <p class="ctx" data-en="…">语境中文…</p>
  <blockquote>“英文原文…”</blockquote>
  <p class="iv-zh">中文对照…</p>
  <p class="after"><b>后续：</b>…（可含互链）</p>
</article>
```
id 规则 `i{YYYY-MM}`（月精度）或 `i{YYYY-MM-DD}`（日精度，站内既有 i2016-09-27 先例）。

§3 文档条目（doc-article，documents.html）
```html
<article class="doc-article" id="d2006-08">
  <h2>文档标题</h2>
  <div class="doc-meta"><span class="doc-badge">来源</span><a class="doc-badge" href="#d2006-08" title="定位到本文档 · Permalink">2006.08</a><span class="doc-badge">作者：Elon Musk</span></div>
  <h4>原文摘录 · …</h4>
  <blockquote>“…”</blockquote><p class="zh-line">对照…</p>（成对，可多组）
  <h4>本站注释</h4><p class="note">…</p>
</article>
```
id 规则 `d{YYYY-MM}`。

§4 账本条目（ps-row，primary.html，容器 `<ol class="ps-ledger">`）
```html
<li class="ps-row ps-deep reveal" id="e2002-10-03">
  <div class="ps-head"><span class="ps-date"><a class="ps-date" href="#e2002-10-03" title="定位到本条 · Permalink">2002.10.03</a></span><span class="ps-src">来源注…</span></div>
  <div class="ps-sec"><h4 class="ps-label" data-en="Background">背景</h4><p data-en="…">…</p></div>
  <div class="ps-sec"><h4 class="ps-label" data-en="The words">原话</h4><blockquote class="ps-quote">“…”</blockquote><p class="ps-zh">对照…</p></div>
  <div class="ps-sec"><h4 class="ps-label" data-en="On the ground">现场</h4><p data-en="…">…</p></div>
</li>
```
id 规则 `e{YYYY-MM-DD}`（月精度条目形如 e2006）；节标签三件惯用：背景 Background / 原话 The words /
现场 On the ground（可按需增减 ps-sec，类名不改）；**插入新条前先 grep 全站 `id="e…"` 查重**。

§5 事件档案（tools/events-data.py）
- `etype` 五类枚举（ETYPE_LABELS，**勿扩**）：`start`(创业起步/Origins) `deal`(资本运作/Capital moves)
  `gamble`(豪赌翻身/All-in) `milestone`(产品里程碑/Milestone) `risk`(争议时刻/Controversy)。
- `materials[].kind` 八类：`ledger` `document` `interview` `post` `chronicle` `feature` `image` `external`。
- `precision` ∈ day/month/year；id `e{YYYY-MM-DD}`；字段：id/date/precision/etype/companies[]/title{zh,en}/
  summary{zh,en}/background{zh,en}/facts[]/materials[]。
- 口径红线公式：时间轴独立记录数 = 索引一手材料 − 被吸收数 − events.html 档案记录数。

§6 资源条目（tools/resources-data.py，RESOURCES[]；validate() 非空即拒生成）
字段（13）：`id`(^[a-z0-9-]+$) / `url` / `name{zh,en}` / `desc{zh,en}` / `category`
(`official`|`opensource`|`community`|`tools` 四类) / `lang` / `activity`(维护中|停更|存档) /
`license{zh,en}` / `reason{zh,en}` / `companies[]` / `checked`(核活日期 YYYY-MM-DD) / `http`(状态码) /
`gh`(GitHub 专用 {stars,pushed})；`note{zh,en}` 可选。
样例锚：r-spacex-api（resources-data.py:367）。

§7 verify.py 九项（全绿才算验收）：断链（文件与跨页锚点）/ 重复 id / 版本一致性 / 检索索引一致
（分项和=总数）/ 时间轴节点一致 / 语录卡覆盖（卡数=引文块数−白名单豁免）/ 修订历史一致性 /
CHANGELOG 首条版本 / EPUB 新鲜度。

§8 生成器全家桶（幂等重跑顺序，R20 用；单轮按需子集）：site-nav → build-events →
build-timeline-events → build-network → build-company-files → build-capital → build-ledger-links →
build-ledger-timeline → build-resources → build-search-index → sync-changelog → build-sitemap →
build-revisions → build-epub。**改一手页（primary/quotes/documents/interviews/x-posts）必跑后四件中的
ledger-timeline/search-index/epub + 修订历史。**

§9 版本三件套：VERSION 文件 / app.js SITE_VERSION / 全站 site-version-val span（2026-10-06 实测
16 处=16 个文件各 1 处，新页纳入；批量替换脚本打印替换计数，tools/v9r02-versions.py 有现成模式可拷）。

§10 CDP 探针惯例：headless Chrome 端口 9333 起步递增（**9227 被 aDrive.exe 占用**）、全新
user-data-dir、timeout 杀 node 会留孤儿 Chrome（内存缓存旧页面→假红，须换端口重起）；探针导航后
**轮询关键计数而非定值 sleep**（冷加载慢→计数为 0 时 every() 恒真假红）；多语句 evaluate 须 IIFE；
断言值用 JSON.stringify 包裹防标量恒真。

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
