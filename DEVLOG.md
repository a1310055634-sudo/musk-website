# 马斯克商业志 MUSK, INC. — 开发日志与交接文档

> 本文档供新会话接手时快速了解项目全貌。最后更新：v10.0.0（2026-10-02，V9-20 二十轮收官，本地待推送）。
>
> **技术增补**：2026-09-26 的 17 轮自动化冲刺（v5.89.0→v6.5.0）架构变更、作业模板与坑位清单见 `DEVLOG-SPRINT17.md`（接手 agent 必读第二篇）。

> **技术增补（二）**：2026-09-29/30 的 **V7 十九轮改版（v6.6.0→v7.0.0）已完成并发布**。接手必读第三篇：本节末尾的「V7-19 交接要点」+ `V7-19-PROGRESS.md`（19 轮全记录）+ `qa/v7-19/`（每轮探针与截图）。

> **技术增补（三）**：2026-10-01/02 的 **V8/V9-20 三十轮扩充与升级（v7.1.0→v10.0.0）已完成（纯本地，未推送）**。接手必读：「V9-20 交接要点」节 + `V9-20-PROGRESS.md`（20 轮全记录）+ `qa/v9-20/`（每轮探针与截图）；V8 十轮见 `V8-PROGRESS.md`。

---

## 〇-bis、V9-20 交接要点（v10.0.0，2026-10-02 本地收官，待用户推送）

**三十轮成果地图**（V8 v7.1.0→v8.0.0 十轮：财报会逐字/X 帖/访谈/文档第一手回捞；V9-20 v8.1.0→v10.0.0 二十轮：细节见 V9-20-PROGRESS.md，qa/v9-20/round-NN/）：
- **第一手信息**：账本 67→115（财报会 10+官方演讲 6+早期访谈批次）；文档馆 14→18（S-1/Acronyms/Raptor 信/Technoking 10-K）；访谈 26→42（镜像 interview 库 161 场管线）；X 帖 13→31（镜像 Agent API 管线，snowflake 对表）；语录卡 103（账本引文块全覆盖，豁免 2）；事件档案 9→14（59 材料/口径闭环）。
- **资源板块（第 38 页）**：resources.html 36 条（官方 10/开源 9/社区 11/工具 6，以 resources-data.py 为准），单一事实来源 tools/resources-data.py + build-resources.py；三路法核活（curl→WebFetch→服务端读取器）；**两大判定证伪**：tesla-api.io 与 en.wikipedia.org 本机 DNS 故障≠死链（服务端核活 200 在线）；检索「社区资源」类型+公司过滤+资源↔档案互链（.cf-resl）。
- **美术四轮**：R15 令牌层 37→113（三层：刻度/语义/焦点，对比度修复 21 处）→R16 首页（2 特大+4 标准瓦片/act 入口条）→R17 三图工业风（etype 形状语言圆方菱圆三角+点阵网格，数据编码不动）→R18 排版（数字 tabular-nums 12 选择器/引语三族容器 5px 实线+块影 vs 编者注纸底/EN 行高 1.78）→R19 动效（58 处 transition 审计 TSV、归一 8 处、.btn:active 闭环、reduce 14 块实测、性能落盘）。
- **工程资产**：tools/ 生成器 20+（新增 build-resources/build-sitemap——sitemap 37 URL=38 页−noindex revisions）；verify.py 9 项（第 4 项动态含 rs-item）；探针脚本 v9rNN-probe.js 系列（CDP 端口 9333+ 避让 aDrive/孤儿 Chrome 坑全记录在各账本与 EXPANSION）。

**数据单一事实来源（增量）**：resources-data.py→build-resources.py；interviews-all.json/emails.json（qa/v9-20/round-04、round-06）=后续采料候选池；transition-audit.tsv（round-19）=动效基线。

**已知限制**：V7 时代深色页正文双语长尾仍在；tesla.com 全站本机不可核活（Akamai 三路拦），SAE J3400 标准页 JS 壳——均有 EXPANSION 留档重验条件；Reddit/wikipedia 类站点核活须走服务端读取器。

**续作指南**：V10-15 内容精修计划已开工（账本 `V10-15-PROGRESS.md`，N01–N15：核实/早期年代/email 库/keynote 池/社区资源扩容/事件档案 v2，终点 v11.0.0）；新触发读该账本定轮次，锁 `.v10run.lock`。

---

## 〇、V7-19 交接要点（v7.0.0，2026-09-30 发布）

**十九轮成果地图**（细节见 V7-19-PROGRESS.md 每轮记录，qa/v7-19/round-NN/ 有探针+截图）：
- 视觉（R1–R4）：深色纪实封面 + 浅色长文 + 统一色标字体；素材体系（8 图全溯源）；首页「把未来做成生意」+ 五组导航（开始/公司/事件/专题/资料，site-nav.py 单一来源）；
- 阅读（R5/R11–R13）：lr-* 长文模板；三个旗舰专题——`survival-2008.html`（144 天逐节点）、`platform-x.html`（平台三阶段+所有权图+口径三分列）、`promises.html`（承诺-结果五案对账+四类归类+排除项声明）；
- 数据（R6–R10/R15）：`events-data.py` 9 事件档案（37 材料关联）→ events.html/events-data.js；时间轴聚合（151 独立+18 吸收，timeline-events.py）；公司关系图（companies-data.py）；公司档案 4+6（company-files-data.py）；资本流向 18 笔（capital-data.py → capital-evolution.html#flow）；检索 178 条含事件聚合与命中解释（search.html ?q=&type=&co=）；
- 资料（R14）：cite.js 复制引用（107 单元三级退路）；账本关联建档卡（build-ledger-links.py）；四层结构图例；
- 工程收尾（R16–R18）：320/390/768 全站 111 组合扫描零溢出；双语审计修复（controversy 五篇/interviews/reading 全量 data-en；已知限制：深色页叙事正文长尾以中文为主）；性能实测五页 load<1500ms（本地）+defer+reduced-motion/焦点/对比度实测达标。

**数据单一事实来源清单**（改数据只改 .py 再重跑生成器）：events-data.py（事件+材料）→ build-events.py / build-timeline-events.py（151+18 口径）/ companies-data.py 交叉引用；company-files-data.py → build-company-files.py；capital-data.py → build-capital.py；site-nav.py → 全站导航；search-index 由 build-search-index.py（178 = 169 一手 + 9 事件档案）。verify.py 9 项是发布底线。

**已知限制**：money/ai-strategy/grok/capital-evolution 深色页叙事正文与 changelog 条目以中文为主（结构性元素已双语）；money/quotes 两页有历史存量未闭合标签（浏览器容错正常，HEAD 时代即如此）；changelog.html 无脚本（静态日志页）。

**续作指南**：新触发先查 V7-19-PROGRESS.md 末行与 git log——若 v7.0.0 已发布且线上验证过，则**静默退出勿再改**；若要做 v7.1，从「已知限制」的正文层双语与新增专题选题入手；每轮仍走「扫描→修复→探针→截图→verify→提交推送」闭环。

---

## 一、项目概况

**定位**：埃隆·马斯克的商业逻辑与行为研究——离线、双语（中文为主）、纯静态、零外部依赖。

**当前版本**：v6.5.0（git 172 次提交，从 v0.1 到 v6.5.0）

**核心数字**（截至 v5.88.0）：
- 32 个 HTML 页面
- 账本 67 条第一手言行（2002→2026，全部有逐字引语或行为描述）
- 一手文档 9 份（秘密蓝图系列/私有化方案信/收购协议 SEC 条款/Series E 公告等）
- 访谈 18 条 / X 帖 13 张
- 检索索引 169 条锚点（七类型：言行实录 67 / 一手文档 9 / 访谈 18 / X 帖 13 / 争议深读 5 / 编年史 53 / 财务全景 4）
- 语录核实组 54 张卡（vs 账本引文块 57 个，白名单豁免 3 项）
- 修订历史 107 锚点（覆盖全部在册锚点的 git 生命周期）
- 争议板块 5 篇完整深读

## 二、打开方式

- 双击 `index.html` 即可（纯静态，file:// 协议全功能可用）
- 或 `python -m http.server 8765` 后访问 `http://127.0.0.1:8765`
- 在线版：<https://a1310055634-sudo.github.io/musk-website/>（GitHub Pages，随 main 自动部署）

## 三、目录结构

```
index.html              封面 + 章节目录（全站入口）
primary.html            言行实录账本（核心，67 条 + 页顶时间轴）
documents.html          一手文档馆（9 份）
interviews.html         访谈与表态（18 条）
x-posts.html            X 帖史选辑（13 张）
quotes.html             语录页（格言轮播 + 53 张核实卡）
reading.html            长卷阅读版（十章书籍形态）
chronicle.html          四公司编年史（Tesla 21行/SpaceX 15行/X/xAI）
finance.html            财务资本全景（Tesla/SpaceX/X/xAI）
controversy.html        争议与批评（5 篇完整深读）
revisions.html          修订历史（100 锚点，自动生成）
search.html             跨页检索（关键词/类型/公司/年份/排序）
timeline.html           商业时间线（含全局泳道大时间轴）
money.html              资本解剖
capital-evolution.html  资本模式演化（含资本流向 Sankey）
ai-strategy.html        AI 战略布局
pricing.html            定价与需求管理
supplychain.html        供应链与工厂哲学
...（其余：profile/timeline/companies/indepth/stories/persona/playbook/numbers/grok）
style.css               全站设计系统（纸面底/衬线标题/酒红强调）
app.js                  交互（双语切换/检索/轮播/时间轴/动效/汉堡菜单）
search-index.js         检索索引（由 tools/build-search-index.py 生成）
assets/                 图片
tools/                  六个自动化工具脚本（见下表）
CHANGELOG.md            修订记录（160 条）
EXPANSION.md            事实扩展包（每条新事实的核实来源）
ROADMAP.md              历史规则
VERSION                 当前版本号
README.md               项目介绍与部署要点
```

## 四、tools/ 自动化工具（六个脚本）

| 脚本 | 作用 | 何时运行 |
|---|---|---|
| `verify.py` | **一键体检**：断链/重复id/版本一致/索引一致/时间轴一致/修订历史一致/语录卡覆盖（白名单核对）/CHANGELOG 首条版本/EPUB 新鲜度 | **每轮必跑** |
| `build-search-index.py` | 从四个第一手页重建检索索引（search-index.js） | 账本/文档/访谈/帖史变动后 |
| `build-ledger-timeline.py` | 从账本重建页顶时间轴（primary.html） | 账本变动后 |
| `build-revisions.py` | 从 git log 生成修订历史（revisions.html） | 需要更新修订历史时 |
| `sync-changelog.py` | 从 CHANGELOG.md 重生成 changelog.html | CHANGELOG.md 更新后 |
| `build-epub.py` | 将全部页面编译为离线 EPUB 电子书 | 需要生成电子书时 |

## 五、核心约定（新会话必须继承）

1. **第一手锚点**：所有内容必须有日期+出处+逐字原句。档案文本（Wayback/SEC EDGAR）优先于二手转述，媒体转载需至少两源印证。查不到不写。
2. **深度纪律**：每条账本至少 3-4 段（背景→逐字原话→现场→后续），反对过度概括。
3. **准确性高于一切**：编者分析与原话严格区分（编者分析显式标注）；争议内容正反两面呈现。
4. **禁感情家庭内容**。
5. **纯离线**：禁外部库/CDN/运行时联网/图表库。
6. **双语**：data-en 叶子节点；独立新页可整页双语并列。
7. **先查账本再 WebSearch**：避免重复核实（Cybertruck 教训）。
8. **版本步进脚本必须 import io, re, glob 三件套**（glob 漏 import 已两次被抓）。
9. **批量插入 HTML 用「片段文件 + 整块单次重建」** 避免多字节切坏。
10. **版本步进后必须跑 verify.py** 确认版本一致性。

## 六、账本锚点体系

每个第一手条目都有稳定锚点，格式 `e{YYYY}-{MM}-{DD}` 或 `e{YYYY}`（年份级）。

示例：
- `primary.html#e2002-10-03` → PayPal 交割与资金分配
- `primary.html#e2018-08-07` → funding secured 推文
- `primary.html#e2025-03-28` → xAI 收购 X

新增条目时：
1. 写入 primary.html（四段深读：背景→逐字原话→现场→后续）
2. 在 quotes.html 补语录卡（如有逐字引语）
3. 在 chronicle.html 补编年史行（如有对应公司）
4. 重跑 build-search-index.py + build-ledger-timeline.py
5. 更新 tools/build-search-index.py 内的数量断言与 search.html 计数文案

## 七、自动维护管线

每轮账本/文档变动后，依次运行：

```bash
python tools/build-search-index.py     # 重建检索索引
python tools/build-ledger-timeline.py  # 重建账本时间轴
python tools/sync-changelog.py         # 同步修订记录页
python tools/verify.py                 # 一键体检（必须全绿）
```

verify.py 会自动检查：
- 断链（页面/锚点/CSS/JS/图片）
- 重复 id
- 版本一致性（VERSION / app.js / 页面 span）
- 检索索引一致（条数 = 各页锚点之和）
- 时间轴节点一致（= 账本条目数）
- 语录卡覆盖（白名单精确核对，允许 3 项豁免）
- 修订历史一致性（≥50 锚点）
- 修订历史页存在

## 八、当前账本覆盖（67 条，2002→2026）

| 年份 | 条目 | 事件 |
|---|---|---|
| 2002 | 1 | PayPal 交割与资金分配 |
| 2006 | 2 | SolarCity 创立、秘密蓝图 |
| 2008 | 4 | Flight 3 失败、Flight 4 入轨、NASA CRS、圣诞夜融资 |
| 2012 | 3 | Dragon 对接 ISS、Model S 交付、首次盈利 |
| 2013 | 3 | DOE 贷款还清、Hyperloop 白皮书、die on Mars 访谈 |
| 2014 | 2 | 开放专利、Dragon V2 |
| 2015 | 4 | Google/Fidelity 入股、Powerwall、Falcon 着陆、Model X |
| 2016 | 7 | Model 3 预订夜、SolarCity、Amos-6、IAC 火星、Part Deux、SES-10 |
| 2017 | 4 | Model 3 首辆、生产地狱、SES-10 复飞、Semi |
| 2018 | 6 | 猎鹰重型、pedo guy、funding secured、工会、Semi+Roadster、Boring 隧道 |
| 2019 | 3 | Crew Dragon 事故、Mk1、Demo-1 对接 ISS |
| 2020 | 3 | Crew Dragon 载人、Fremont 复工、Battery Day |
| 2021 | 3 | Hertz/万亿、工会推文、Optimus |
| 2022 | 7 | Heavy 已录、收购协议、SolarCity 判决、bird is freed、X 帖系列 |
| 2023 | 6 | Investor Day、xAI、X 更名、DealBook、Cybertruck、X 帖 |
| 2024 | 4 | Neuralink、Robotaxi、Starship 接塔、X 帖 |
| 2025 | 5 | Starbase、Part IV、万亿薪酬、Optimus、xAI 收购 X |
| 2026 | 1 | Series E（编年史/文档/财务均覆盖） |

## 九、待做事项（按优先级）

1. **账本扩容候选序列已关闭**（v6.0.0 裁定）：最后一个候选 2010 Fremont/NUMMI 因三轮搜索无逐字引语放弃（Gruber 先例）；存量覆盖 67 条视为完整。未来仅当出现两源逐字的新事件时再开新条。
2. **争议板块第五篇 Twitter 内容审核**已有——但 Autopilot/工会/Twitter 三篇可继续深化
3. **search.html 公司过滤纳入新页**——controversy/chronicle/finance 目前不在索引中
4. **排版与 QA 已完成**（v6.0-6.4）：深读五页/长卷/争议 480px 块、时间轴横滑、打印防拆、五页打印抽检、双语覆盖核查、og 全站覆盖（v6.1.0）——后续可按需增量优化

## 十、已知技术债务

1. **~~search.html 匹配文本~~（v6.3.0 核销）**：经诊断，bg 字段已在全部 169 条索引条目非空（primary 背景段/文档 note/访谈 ctx/帖史 note/编年史与争议摘要），match() 已含 bg——抽样 6 条「仅存于 bg 的词」全部命中，技术债已在历轮迭代中自然消化
2. **build-search-index.py 断言**：每轮新增条目后需手动更新数量断言
3. **打印缓存**：IAB 内嵌浏览器对 style.css 有顽固缓存——QA 用「服务器端 curl 确认 + 页内注入等价规则实测几何」证据链方法

（sync-changelog.py「版本号+轮后缀」解析丢失已在 v5.88.1 修复：正则容忍「 轮」、未匹配标题打印警告、verify 增加 CHANGELOG 首条版本门禁。）

## 十一、git 提交习惯

- 每轮提交并 `git push`（2026-09-25 起接入 GitHub 远程 `origin`，Pages 随 main 自动部署）
- 提交消息格式：`v{版本号} 类型: 简述`
- git log 即完整修订史，修订历史页由此生成
- **版本号纪律（v5.88.1 教训）**：2026-09-20 凌晨连续多轮迭代时曾出现版本号误标（v5.80.1/v5.89.0 提前使用、v5.85.0/v5.88.0 各重复两次）和三轮 CHANGELOG 漏记（2013 首次盈利 / 2018 工会推文 / 2021 世界首富日）——v5.88.1 已补账（补录 + 勘误加注，git 历史未改写）。提交前先看 `git log --oneline -3` 确认下一个版本号，CHANGELOG 补条目后再提交；verify.py 的「CHANGELOG 首条版本」门禁会拦截漏记。

---

**总结**：这是一个内容密度极高、事实纪律严格、基础设施完善的静态研究站。核心工作模式是「账本扩容（先查账本→WebSearch 核实→四段深读→全链同步→verify 全绿）」。当前 67 条账本已覆盖极广，后续增量价值递减——可考虑转向深化既有条目、增加争议板块内容、或填充长卷阅读版的空白章节。
