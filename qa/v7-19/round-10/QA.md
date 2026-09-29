# V7-19 R10 验收记录 · 资本流向可视化（v6.15.0）

日期：2026-09-29 · 分支 visual-v7-19rounds

## 本轮要解决的问题
资本相关内容散在三页（money.html 装饰性时间线、capital-evolution.html 静态示意图、finance.html 全景表），
流向图形宽度口径含混、无出处、不可交互；融资额 / 估值 / 收入混排风险。

## 实际完成的改动
1. `tools/capital-data.py`：资本流向单一事实来源（5 来源节点 × 7 公司 × 18 笔真实资金移动，
   八类资金性质 / 五个筛选分组；每笔带日期精度、金额与币种、统计口径、站内来源锚点；
   结构自检含锚点逐一在册核对，不过拒生成）。
2. `tools/build-capital.py` → `capital-evolution.html#flow`（第 34 页外的既有页注入新区块）+
   `capital-data.js`（window.CAPITAL_V7）：SVG 静态流向图（线宽=金额对数标度、图例声明示意；
   箭头=资金方向；金额未入册画最细虚线标注，不编造）+ 图例 + 分组筛选 + 详情面板 + 五组清单；
   旧 #ce-flow 装饰图与死样式移除，四时代正文保留。
3. 不入图声明：估值 / 市值 / 减记一律不画线（NON_FLOW_NOTE），只在口径说明作背景引用。
4. 联动：companies.html 关系图面板「查看它的资本流向 →」；money.html 入口行；首页 #map 入口行；
   清单行深链事件档案 / 公司档案 / 账本 / 一手文档。
5. style.css .cap-* 组件层；app.js 交互块（约 200 行）+ 关系图面板补资本链接；版本 6.15.0（VERSION + app.js + 14 页 span）；EPUB 重建（140,517 bytes · 24 章）。

## 检查了哪些页面和交互
capital-evolution.html（图/清单/筛选/面板/键盘/Esc/双语/打印/无 JS/390/file://）、
companies.html（关系图面板资本链接）、money.html 与 index.html（入口行）、
timeline.html / events.html / company-files.html / search.html（回归）、（探针 56 断言全过）。

## 测试结果及发现的问题
- verify.py 9/9 绿（34 页）；node --check app.js + capital-data.js 过；CDP 探针 **56/56**。
- 探针抓出并修复 1 个真缺陷：详情面板内 jump 跳转后按 Esc，焦点丢失到 body
  → 焦点归还逻辑改为「触发元素失连时退回选中的流向线本体」，jump 的触发元素即该流向线。
- 探针自身三处 bug（线宽断言顺序写反、EN 断言被截断、对象字面量多一次调用、档案计数含简介容器）已修正，非站点缺陷。
- 截图伪影：captureBeyondViewport 会把 sticky 报头冻结在画面中 → 截图前 staticize（R6 已知手法）。
- EN 模式下清单行 dir 与金额间距实测 3.7px 正常（低分辨率截图误读排除）。
- SVG 布局迭代两轮：xAI B/C 轮标签去括号后同名（阈值放宽保留「（B 轮）」）、
  收购方与公司端密集插槽标签双列错位（截图人工复核通过）。

## 是否完成本轮
完成。第 7–10 轮质量门：公司（关系图/档案）→ 事件（时间轴/事件档案）→ 资本（流向图）可连贯探索，
探针联动 4 断言（三页互达 + #flow 深链落地）全过。

## 证据
- flow-section-desktop.png 流向区整段（桌面 1440）
- graph-zoom.png 图形区 2×（标签排布复核）
- flow-detail-open.png 选中「他牵头的财团 → X」详情面板
- flow-filter-gov.png 政府资金筛选态（2 笔）
- flow-en.png EN 全区
- flow-mobile-390.png 390 真视口（清单形态、零溢出）
- r10-probe.js 可复跑探针（56 断言）

## 事实与来源记录
18 笔全部取自在册口径，零新增外部事实：账本 e2002-10-03（PayPal 交割与三分配引语）/ e2008-12-24（圣诞夜融资，金额未载→诚实标注）/
e2009-03-26 + e2013-05-22（DOE 贷款批准与还清）/ e2010-06-29（IPO）/ e2015-01-20（Google+Fidelity）/ e2016-11（SolarCity）/
e2022-10-28 + documents#d2022-04-25（Twitter 收购与合并协议）/ e2025-03-28（xAI 并购 X）/ documents#d2026-01（Series E）；
finance.html#xai（B/C 轮）；money.html、profile.html（Zip2 两笔）；company-files.html 档案锚点。
