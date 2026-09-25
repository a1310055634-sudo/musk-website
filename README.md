# 马斯克商业志 MUSK, INC.

一部关于埃隆·马斯克商业逻辑与行为的**离线、双语（中文为主）、可检索**的静态人物志。
非官方、学习型项目；信息整理自公开资料，所有第一手引语均经核实并标注日期与出处；不含任何感情/家庭内容。

## 打开方式

- **在线版**：<https://a1310055634-sudo.github.io/musk-website/>（GitHub Pages，随 main 分支自动部署）；
- **直接双击 `index.html`**（全部功能在 file:// 协议下可用，无任何联网依赖）；
- 或本地起服务：`python -m http.server 8765` 后访问 `http://127.0.0.1:8765/index.html`。

## 站点结构（32 页）

| 板块 | 页面 | 说明 |
|---|---|---|
| 封面与导航 | `index.html` | 卷首特稿、章节卡片（全站入口）、双语切换 |
| 言行实录 | `primary.html` | 第一手言行账本（2002→2026，随迭代增长），每条含稳定锚点 `#e…`、页顶可交互时间轴（hover 预览引文）、实时检索 |
| 一手文档馆 | `documents.html` | 9 份关键文本摘录（秘密蓝图系列/私有化方案信/收购协议 SEC 条款/Series E 公告），锚点 `#d…` |
| 访谈与表态 | `interviews.html` | 18 条公开表态，锚点 `#i…` |
| X 帖史选辑 | `x-posts.html` | 13 张名帖深读卡，锚点 `#p…` |
| 主题深读 | `money.html` `capital-evolution.html` `ai-strategy.html` `pricing.html` `supplychain.html` | 资本解剖（含流向图）/ 资本模式演化 / AI 战略 / 定价与需求 / 供应链与工厂 |
| 长卷阅读 | `reading.html` | 十章连续叙事（书籍形态，重组自站内已核实材料），侧目录 + 进度条 |
| 公司专著 | `chronicle.html` `finance.html` | 四公司编年史（Tesla/SpaceX/X/xAI）/ 财务资本全景（融资-估值-收入） |
| 商战故事 | `stories.html` `deep-dive-01~05.html` | 经典商战长文与五篇深读（资本/用人/失败/监管/AI） |
| 速览类 | `profile.html` `timeline.html` `companies.html` `numbers.html` `grok.html` `persona.html` `playbook.html` `quotes.html` `indepth.html` | 速览、时间线、公司版图、数据、xAI·Grok、人格、方法、语录、深度总览 |
| 工具与记录 | `search.html` `changelog.html` | 全站第一手检索（关键词/类型/公司/年份区间/排序）；修订记录（由 CHANGELOG.md 同步生成） |

> 时间轴点击/引用跳转后目标条目有 1.8 秒落点高亮；泳道时间轴与账本时间轴的悬停摘要均含引文片段。

## 研究功能

- **逐条引用**：每个第一手条目都有稳定锚点，如 `primary.html#e2018-08-07`、`documents.html#d2022-04-25`、`interviews.html#i2016-09-27`、`x-posts.html#p2022-10-28`。
- **跨页检索**：`search.html` 支持关键词、类型、公司、年份区间过滤与正/倒序排序；索引在 `search-index.js`。
- **打印存档**：全部页面带打印样式（隐藏界面铬件、防拆页），可直接浏览器「打印为 PDF」。

## 目录结构

```
index.html …（27 个页面）
style.css          全站设计系统（纸面底/衬线标题/酒红强调）
app.js             交互（双语切换/检索/轮播/时间轴/动效）
search-index.js    检索索引（由 tools/build-search-index.py 生成）
assets/            图片
tools/             自动化工具（见下）
CHANGELOG.md       修订记录（随迭代持续追加）
EXPANSION.md       事实扩展包（每条新事实的核实来源）
ROADMAP.md         历史规则与方向记录
VERSION            当前版本号
```

## tools/ 自动化工具（站点根目录执行）

| 脚本 | 作用 |
|---|---|
| `verify.py` | **一键体检**：断链/重复 id/版本一致性/索引一致性（部署前必跑） |
| `build-search-index.py` | 从四个第一手页重建检索索引 |
| `build-ledger-timeline.py` | 从账本重建页顶时间轴 |
| `sync-changelog.py` | 从 CHANGELOG.md 全量重生成 changelog.html |

## 内容纪律（本站约定）

1. **第一手锚点**：所有内容必须有日期+出处+逐字原句；档案文本（Wayback/SEC EDGAR/x.ai 官网）优先于二手转述，媒体转载需至少两源印证；查不到不写。
2. **深度纪律**：条目为深读版（背景→逐字原话→现场→后续），反对过度概括。
3. **准确性高于一切**：编者分析与原话严格区分，所有编者推断显式标注。

## 部署要点（供站长参考）

- 纯静态：任意静态文件服务器/对象存储可直接托管；无构建步骤、无运行时联网、无外部 CDN。
- 部署前跑 `python tools/verify.py`，全部 ✓ 再上线。
- 子页（检索/修订记录等）当前带 `<meta name="robots" content="noindex">`，主页面未做限制；如需调整收录策略请自行修改各页 meta。
- 版本号见 `VERSION`；每轮自动化更新后请同步提交 git（本仓库历史即完整修订史）。
