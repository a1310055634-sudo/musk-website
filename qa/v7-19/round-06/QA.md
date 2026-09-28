# V7-19 第 6 轮 QA 记录 — 事件与来源结构（v6.11.0）

日期：2026-09-29 · 分支 visual-v7-19rounds · 执行实例 run-a（接管 run-b 遗留锁，run-b 已自证 R5 完成并推送 b3cf2d2）

## 本轮要解决的问题

计划第 6 轮（事件与来源结构）：建立稳定事件 ID、公司、日期精度、材料与来源关系；明确区分一个事件和描述它的多份材料；从代表性事件迁移；制作事件详情页；让新数据能生成静态 HTML 或本地 JS 数据。验收线：一个事件可关联多份资料；事件含背景/事实/原话/后续/证据；不虚构具体日期；file:// 可用，旧链接有效。

## 实际完成的改动

- **tools/events-data.py（新）**：事件数据单一事实来源。6 个代表性事件（2002 PayPal 交割 / 2006 SolarCity 创立 / 2008 圣诞夜融资 / 2018 funding secured / 2022 Twitter 交割 / 2024 星舰塔捕，前五者即首页 #events 深链节点，e2006 为仅年份精度示范）：稳定 ID（沿用账本 e* 锚点）、公司、显式日期精度（day/month/year）、背景/关键事实/逐字引语/后续四段本体、材料关联（七类 24 份）、相关事件互链；自带结构自检（重复 ID/双语字段/精度枚举/无引语必须有 no_quote_note），不通过拒绝生成。
- **tools/build-events.py（新）**：生成 events.html（静态、双语 data-en、复用 R5 lr-* 模板层）+ events-data.js（window.EVENTS_V7 全量数据，file:// 以 script 标签加载，供 R7/R9/R15 复用）。
- **events.html（新，第 33 页）**：lr-hero 深色页头（kicker/大标题/斜体导语/元信息行）+ 口径说明框（读法与口径）+ 六事件五段结构 + 日期精度徽标 + 公司 chip + 材料清单（类型标签/日期/说明）+ 相关事件 + 塔捕纪实图（署名+尺寸声明+懒加载）+ sticky 目录（滚动定位自动生效）。
- **style.css**：.ev-* 组件层（≈50 行）+ .section-more 首页入口行样式；640px 手机与打印规则。
- **tools/site-nav.py**：事件组注册 events.html（4→5）；全站 33 页导航重注入。
- **index.html**：#events 区头加「事件档案」入口行；五个事件行各加「事件详情」深链（tools/r06-index-links.py，ASCII 锚点+脚本内中文，规避 bash GBK 坑）。
- **同步**：VERSION/app.js/12 页 span → 6.11.0；CHANGELOG + changelog.html；ASSETS.md starship-catch 用途补记；EPUB 重建。

## 事实纪律

- 全部事实与引语逐字取自已核实的言行账本条目（本轮零新增外部事实），引语 5 条均为账本在册逐字引文。
- 日期精度只作档案分层：e2006 仅年份；2018 SEC 起诉沿用账本「八天后」相对表述，不断言具体日期；2008.12.23 NASA 合同日期出自账本原文。
- e2006 无逐字原话 → no_quote_note 诚实建档，不凑引语；关键事实区统一标注「编者归纳，非当事人原话」。

## 检查与结果

**静态检查**：verify.py 9/9 全绿（33 页面，断链含 events.html 全部跨页锚点；检索索引 169 = 67+9+18+13+5+53+4 不变；EPUB 新鲜度过）；node --check app.js 过；python tools/events-data.py 结构自检过（6 事件 · 5 引语 · 24 材料）。

**CDP 真视口探针（v7r6-work/r06-probe.js，33 断言全过）**：
- A 结构：六 section/ID 集合/精度徽标 5日+1年/事实 22 条/引语 5/材料 24/chip 11/目录 8 链接/塔捕图加载+尺寸声明/版本 span/aria-current/桌面零溢出/EVENTS_V7=6；
- B 外部深链（about:blank → events.html#e2008-12-24）锚点落在报头之下（132px scroll-margin）；
- C 双语：EN 切换 h1/材料类型标签/目录全量换英，切回中文无损；
- D 材料跳转：events.html#e2018-08-07 → documents.html#d2018-08-07 点击可达落视野；
- E 首页接入：入口行存在 + 5 深链 + 点击落到 e2024-10-13；
- F 账本回归：67 条 + 67 时间轴节点 + 导航含事件档案 + 旧锚点 primary#e2008-12-24 有效；
- G 检索回归：SEARCH_INDEX=169；
- H 无 JS：script 禁用下六事件/材料/标题完整可见（正文静态存在）；
- I 手机 390×844（真视口 Emulation）：events/index 零横向溢出 + 目录盒装退路可见；
- J file://：events.html 六事件 + EVENTS_V7 加载 + 深色页头样式生效 + index 导航含事件档案。

**截图证据**：before/（v6.10.0 git worktree：index-desktop.png、primary-desktop.png、index-desktop-full.png）+ after/（events-desktop.png 干净整页、events-desktop-en.png、events-anchor-e2008.png、events-mobile.png 390、index-desktop.png、index-desktop-full.png、index-mobile.png、primary-desktop.png）。已人工复核：深色页头/五段结构/材料清单/手机换行/首页三链接行均正常。

**本轮修掉的探针缺陷（非站点缺陷）**：① A9 懒加载图在视口外 naturalWidth=0 属预期 → 滚动到图再断言；② B1 同文档 hash 导航不重载 → 改模拟外部深链（about:blank 进入）；③ profile 复用致 localStorage 残留 → 每次运行全新 chrome-profile + 目标源清键重载；④ captureBeyondViewport 整页图 sticky 元素冻结在中途位置（报头横带伪影，R2/R5 已知工具伪影同类）→ 截图前临时 static 化报头/目录 + 强制 .reveal is-visible。

## 是否完成本轮

完成。6 个代表性事件结构化建档 + 事件详情页上线 + 本地 JS 数据出口 + 首页接入 + 旧锚点零破坏，验收线全部满足。下一轮：第 7 轮公司关系总览（v6.12.0），可直接消费 events-data.js。

## 遗留与交接

- 探针与补拍脚本在仓库外 D:/vibe coding/v7r6-work/（r06-probe.js 33 断言、r06-reshot.js、r06-reshot-idx.js 可复跑）。
- 公司色标仍留 R7/R8（本轮 chip 为中性样式，符合 R4 备注）。
- 检索未覆盖 events.html（build-search-index 七类型口径未动）——按计划留 R15 事件聚合时一并处理。
