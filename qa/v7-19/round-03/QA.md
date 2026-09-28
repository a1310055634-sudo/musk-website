# V7-19 第 3 轮 QA 验收记录 — 首页首屏重构（v6.8.0）

日期：2026-09-29 · 运行标识 v7r3-20260929-c · 分支 visual-v7-19rounds

## 本轮要解决的问题

旧首页首屏是浅色杂志封面（标题「埃隆·马斯克」+ 白框肖像 + 两按钮），无一句话定位、无查找资料入口；手机端 ≤960px 肖像 `order:-1` 插队抢占首屏。按计划第 3 轮改为深色纪实封面：编者大标题、明确定位、开始阅读/探索版图/查找资料三入口，手机首屏优先表达标题与入口。

## 实际完成的改动

- index.html：`section#cover` 整体重构为 `.hero`（近黑 #101316 满幅）——海报式构图：kicker「编者视角 · 商业档案」+ 通栏一行大标题「把未来做成生意」（≥720px 隐藏手动换行）+ 副标题定位句 + 三入口按钮（reading/companies/search）+ `hero-body`（左定位与入口、右 portrait-hero 肖像）+ `.deal-lines.hero-stats` 关键数字行 + `.hero-strip` 四格业务横带（tesla-factory / falcon-heavy / starship-catch / x-hq，带公司标签·图注·署名）；`<picture>` 手机档自动换 portrait-hero-mobile.jpg（4:5）；title/description/og:image/og:description/twitter:description/theme-color 换新定位。
- style.css：旧 `.cover*` 块替换为 `.hero` 体系（head/body/kicker/title/sub/actions/figure/stats/strip + 960/640 媒体查询 + 独立 print 块）；`html[lang="en"]` 英文标题独立刻度与行高；删除 ≤960px `.cover-portrait{order:-1}`（手机照片抢占首屏的根源）；令牌新增 `--accent-bright`/`--mist`；960 块与 print 块清理旧封面引用。
- app.js：仅 SITE_VERSION → 6.8.0（无逻辑改动）。
- ASSETS.md：六处素材「用途」同步（portrait-hero 启用、四图新增横带用途、portrait.jpg 收窄为其余 29 页）。
- 12 页版本 span + VERSION 步进 6.8.0；CHANGELOG 记账；sync-changelog（163 条）；EPUB 重建（122,058 B / 24 章）。

## 检查了哪些页面和交互

- 检查页面：index.html（中/英 × 桌面 1440 / 真 390 CDP / file://）。
- 交互：EN 语言切换（标题/署名/按钮全文替换、html[lang] 切换生效、切回中文无损）；导航高亮/汉堡菜单未受影响（报头未改动）；`.cnt` 计数器在数字行正常；`.reveal` 章节卡入场正常（封面本身零 .reveal）。

## 测试结果

- verify.py 9 项全绿（断链/重复id/版本一致 6.8.0/索引 169/时间轴/语录卡 54+3 豁免/修订史 107/CHANGELOG 首条/EPUB 新鲜度）；`node --check app.js` 通过。
- CDP 真视口探针（tools 于 v7r3-work/r03-probe.js，仓库外 scratch）：桌面标题 138px 单行不溢出；EN 96px 两行不溢出；390px 中/英 `scrollWidth=390` 零页面级横向溢出（横带 flex 滚动容器内图块 right=484 属滚动内容，非页面溢出）；CTA 底缘 546px < 844px 完整落在首屏；封面元素 opacity=1、零 .reveal（无动画依赖）。
- file:// 冒烟：双击场景封面完整呈现（截图 file-smoke-1440.png）。
- 本轮实测发现并修复的三个缺陷：
  1. 桌面中文标题在 1.08fr 栅格列内 144px×4 字放不下折成三行 → 重构为标题通栏海报式构图；
  2. `auto` 网格轨道内 `min(480px,100%)` 百分比循环解析，文字列计算宽度被压成 0px（竖排逐字）→ 轨道改 `min(480px,44vw)` 确定尺寸；
  3. `.deal-lines` 亮色规则源码顺序靠后、同特异性压过暗底覆盖（数字行墨字不可读）→ 覆盖规则升为 `.deal-lines.hero-stats`。
- 已知伪影说明：qa-shots.py 手机档 500px 最小窗宽与 --virtual-time-budget 下图片未及绘制（首版截图肖像空白框）均为工具伪影，已用 CDP 真渲染核实排除；qa/v7-19/round-03/after/ 以 CDP 截图为准。

## 是否完成本轮

完成。桌面与手机第一屏均可理解主题并三键开始操作；英文标题不破版；首屏关键内容无入场动画依赖；与改版前（qa/v7-19/round-03/before/）对比视觉变化显著。下一轮：第 4 轮「首页编排与全局导航」（v6.9.0）。

## 证据清单

- before/：index-desktop.png、index-mobile.png（改前浅色杂志封面）
- after/：index-desktop.png、index-mobile.png（qa-shots 标准档）；desk-en.png、mob-390-zh.png、mob-390-en.png（CDP 真视口）；full-page-desktop.png（1440×2600 全页）；file-smoke-1440.png（file:// 冒烟）
- 本记录 QA.md
