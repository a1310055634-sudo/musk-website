# V7-19 R12 QA 验收记录 — 平台与 AI 旗舰专题（v6.17.0）

日期：2026-09-29 · 分支 visual-v7-19rounds · 探针脚本 qa/v7-19/round-12/r12-probe.js（可复跑，副本同 v7r12-work）

## 本轮要解决的问题

计划第 12 轮：重组 X、xAI 及相关平台与 AI 内容；用阶段变化和关系图解释交易与战略；清楚区分历史状态、当前已核实状态和编者推断；同步关联公司、事件与资料。

## 实际完成的改动

1. **新专题页 `platform-x.html`（第 36 页）**：「平台变局：Twitter、X 与并入 xAI」——平台交易线独立立档（与 ai-strategy=AI 全景、deep-dive-05=AI 战略视角、grok=模型产品的**内容归属四分工表**在第一节明示）。深色页头（装饰"X" + SVG 三阶段总览：买下/重塑/并入，方块可点击、宽度声明示意）+ 正文九节：为什么单独立档 / 三阶段总览表 / 阶段一买下四节点（04.14 要约 · 04.25 协议第 9.9 条 · 07–10 强制履约 · 10.27–28 交割）· 阶段二重塑三节点（extremely hardcore · 品牌 X · 广告主撤离）· 阶段三并入四节点（xAI 成立 · Grok · 全股票合并 · Grok 4+Series E）· **所有权三时代 SVG**（公众公司→他私有→并入 xAI；控制线画法声明非持股比例）· **状态口径三分列表**（历史/截至/编者逐格分列）· 记录四组 19 条 · 方法边界六条。
2. **事件材料联动**：e2022-10-28 与 e2025-03-28 材料组各补 platform-x.html feature 深链（33→35 份材料）；build-events/build-timeline-events/build-company-files/build-network 全部重跑（口径不变：9 事件/151 独立/18 吸收/12 事件联动）。
3. **联动四入口**：ai-strategy「AI 公司买平台」节、deep-dive-05 第三节、grok 关键节点后、首页 feature-rows 第二行；专题组导航第二位（36 页重注入）。
4. style.css 扩展 .sv-* 层（三阶段方块/徽标三色/所有权图/分工清单）；VERSION/app.js/14 页 span → 6.17.0；EPUB 重建。

## 检查了哪些页面和交互

platform-x.html（结构/阶段方块跳转/深链全量/双语/无 JS/390/file://）、index、ai-strategy、deep-dive-05、grok、events（材料深链）、timeline（TIMELINE_V7 meta）。

## 测试结果

- verify.py **9/9 全绿**（36 页，索引 169 口径不变）；node --check 通过。
- CDP 真视口探针 **35/35 断言全过**：结构 13（三阶段图 3 方块/所有权图 3 时代/11 节点/2 引语+来源行/深链 11 行 23 链接/分工 4/九节九目录/证据 4 组 19 条/方法 6/口径表 3 列/版本/aria-current）· 深链有效性 1（含 sv-ev 与 sv-scope 全量去重核对）· 交互 1 · 双语 4 + 无漏翻 1 · 无 JS 1 · 390 真视口 4（无溢出/两图隐藏由表格与列表替代/节点满宽/口径表容器滚动）· 联动回归 8（首页前两行/导航/ai-strategy/深读五/grok/两事件材料深链/span/TIMELINE_V7 meta）· file:// 2 · 打印与减动效 2。
- 探针首轮 4 FAIL 全为探针自身问题（服务器掉线致结构 0 + 条目数错算 + 图注选择器 + TIMELINE_V7 查询页错误），修正后全过，站点零缺陷。
- 截图人工复核：桌面首屏（三阶段图）/阶段一节点区（徽标+深链行）/所有权三时代图（控制线+X 虚线并入盒）/状态口径三分表/EN/390（X 装饰字+标题换行正常+无溢出）/file:///首页专题行/events 合并档案。
- 本轮实测修复：meta 行「小节 8 个」与实际 9 节不符 → 改「9 个」；owned 图 figcaption 英文拼写 holdinngs→holdings。

## 事实纪律（全部在册口径，零新增外部事实）

- 440 亿（现金对价 2022）与约 330 亿（全股票估值 2025）不混用不相减；800/330 亿标「本人宣布数字·CNBC/Forbes/AP 报道转述·均未上市无市场报价」；Fidelity 80% 减记标「持仓方记账非成交价非公司披露」。
- 交割日期双口径并列（10.27 资本档案 / 10.28 账本与发帖），不作静默取舍。
- 编者框架（万能应用底盘/广告动摇背景/价值毁灭还是价格发现开放问题）出现处逐条标注，均不归于本人。
- 「Extremely hardcore」邮件、并购协议关键条款、xAI 宣言、Series E 公告均链向 documents.html 在册一手文档。

## 结论

**本轮完成。** 验收条件逐项达成：完整专题交付 ✓ 阶段变化+所有权关系图 ✓ 历史/现状/编者三分 ✓ 与已有深读内容归属清楚（四分工表+互指链接）✓。

## 证据清单（本目录）

r12-desktop-hero.png / r12-desktop-stage1.png / r12-desktop-merger.png / r12-desktop-ownership.png / r12-desktop-calibers.png / r12-desktop-en.png / r12-mobile-hero.png / r12-file-hero.png / r12-index-feature-row.png / r12-events-merger.png / QA.md / r12-probe.js
