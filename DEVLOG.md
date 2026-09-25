# 马斯克商业志 MUSK, INC. — 开发日志与交接文档

> 本文档供新会话接手时快速了解项目全貌。最后更新：v5.88.1（2026-09-20）。

---

## 一、项目概况

**定位**：埃隆·马斯克的商业逻辑与行为研究——离线、双语（中文为主）、纯静态、零外部依赖。

**当前版本**：v5.88.1（git 154 次提交，从 v0.1 到 v5.88.1）

**核心数字**（截至 v5.88.0）：
- 32 个 HTML 页面
- 账本 67 条第一手言行（2002→2026，全部有逐字引语或行为描述）
- 一手文档 9 份（秘密蓝图系列/私有化方案信/收购协议 SEC 条款/Series E 公告等）
- 访谈 18 条 / X 帖 13 张
- 检索索引 107 条锚点（关键词+类型+公司+年份+排序）
- 语录核实组 54 张卡（vs 账本引文块 57 个，白名单豁免 3 项）
- 修订历史 100 锚点（覆盖全部在册锚点的 git 生命周期）
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
CHANGELOG.md            修订记录（143 条）
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

1. **账本继续扩容**：候选逐年减少，已有 67 条覆盖极广。可考虑：
   - 2019.03.02 Crew Dragon Demo-1 对接 ISS（已录 e2019-03-03 ✓）
   - 2016.07.20 Part Deux（已录 ✓）
   - 2010.10 Tesla Fremont 工厂 Model S 早期产线
   - 2013.11 Gruber 争议（已放弃——无逐字来源）
2. **争议板块第五篇 Twitter 内容审核**已有——但 Autopilot/工会/Twitter 三篇可继续深化
3. **search.html 公司过滤纳入新页**——controversy/chronicle/finance 目前不在索引中
4. **排版精进**——深读页表格窄屏横滑已做，可继续优化

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
