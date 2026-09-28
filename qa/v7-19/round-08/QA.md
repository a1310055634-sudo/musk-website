# V7-19 第 8 轮 QA 记录 · 公司档案体系（v6.13.0）

日期：2026-09-29 · 分支 visual-v7-19rounds · 运行标识 v7r8-20260929-a

## 本轮要解决的问题

公司版图只有一句话卡片，没有可核查的公司档案；财务数字散落各页且口径（融资/估值/收入/市值）易混；关系图点选公司后没有通向完整档案的路径。本轮建立「可复用公司档案模板」：4 份完整档案（Tesla / SpaceX / X / xAI）+ 6 份简介，全部站内在册口径、逐条锚点、带截至日期。

## 实际完成的改动

- `tools/company-files-data.py`（新）：档案单一事实来源——4 档案五段结构（业务定位/在册里程碑/财务口径/风险与争议/相关事件与延伸阅读：33 里程碑 · 19 财务行 · 13 风险项）+ 6 简介；结构自检（id 必须在 companies-data.py 节点表 / 里程碑·财务·风险逐条带站内锚点 / 财务 kind 枚举 12 类 / as_of 必填 / 双语完整），不过拒生成。
- `tools/build-company-files.py`（新）：生成 company-files.html（第 34 页，lr-* 模板层复用）+ companies-data.js（自 R8 起由本生成器统一写出：COMPANIES_V7 格式与 R7 逐字节一致 + 新增 FILES_V7 出口）。
- `tools/build-network.py`：移交 companies-data.js 写出职责（避免双生成器写同一文件互相覆盖），其余不变。
- `tools/companies-data.py`：10 个公司节点 href 从泛页升级为档案锚点（#file-* / #brief-*）。
- `tools/site-nav.py`：公司组 7→8 项（公司档案），全站 34 页重注入。
- `companies.html`：六张卡片各加档案深链；`app.js`：关系图详情面板新增「查看公司档案 →」链接（data-en 双语）。
- `style.css`：.cf-* 档案组件层（含 640px/打印）+ .company-file-link + .net-d-file。
- ASSETS.md 三处图片用途同步；CHANGELOG/VERSION/app.js/13 页 span → 6.13.0；EPUB 重建。

## 事实纪律自查

- 零新增外部事实：里程碑/财务/风险全部取自言行账本、编年史、财务资本全景、争议深读、一手文档馆的在册口径，逐条锚点可查（verify.py 断链检查兜底）。
- 财务行 kind 分列（个人投入/融资/IPO/合同/收入/估值/市值/收购对价/减记/薪酬激励等 12 类），估值/减记徽标用虚线边框再强调「报道口径」；私有公司估值全部标注「非公司披露」。
- 每份档案 as_of 截至行（Tesla 2025-11 / SpaceX 2024-12 / X 2025-03 / xAI 2026-01），SpaceX 估值停在 2024-12 $350B 不冒充当前报价；业务定位统一标注「编者归纳」；xAI 无纪实图不放占位图。
- 事件交叉引用沿用 R6/R7 既有口径：e2002-10-03 companies 含四家（PayPal 交割资金分配引语）、e2006 含 Tesla——Tesla 档案 4 条事件深链为既定数据口径，非本轮扩写。

## 检查了哪些页面与交互

- 探针（D:/vibe coding/v7r8-work/r08-probe.js，CDP 真实 headless Chrome，可复跑）：**51/51 断言全过**
  - A 结构 13：4 档案/6 简介/33·19·13 计数/as_of ≥5/3 图带署名与宽高声明/目录 ≥11/aria-current/kind 徽标 ≥8 类
  - B 接入 8：锚点落报头下（≥100px）/六卡深链 href 精确匹配/导航含新页/COMPANIES_V7 完整/FILES_V7 出口/href 指向档案锚点
  - C 双语 9：EN 切换（定位/徽标/简介/截至行/页头标题）+ 切回恢复
  - D 联动 5：Tesla 4 条事件深链含两条关键事件/SpaceX 塔捕/X 交割/xAI 无深链（已知口径）/财务来源链接 19 条
  - E 无 JS 4：禁脚本后正文（里程碑/财务/简介）完整可读
  - F 390 真视口 3：零横向溢出/里程碑单列/目录盒装
  - G network 回归 3：点选详情/档案链接（#file-tesla）/键盘 Enter（#file-xai）
  - H file:// 5：四档案/简介/样式/双数据出口/页头图
  - I 版本 1：span 6.13.0
- verify.py 9/9 绿（34 页，检索索引 169 条不变口径）；node --check app.js 通过；EPUB 重建（126,994 B · 24 章）。

## 测试中发现并修复的问题

1. **详情面板 [object Object]（R7 遗留 bug，本轮截图暴露）**：`net-d-meta` 行 `netEsc(c.era)` 漏 `netT()` 双语解包——R7 修了 evidenceLabel/statusLabel 但 era 漏网。已修 + 重拍截图确认（network-detail-file-link.png）。
2. **详情面板无档案入口**：R7 的 href 字段从未被面板渲染——本轮补「查看公司档案 →」链接（data-en），键盘/点选均可达（G2/G3 断言）。
3. **目录三条链接缺 data-en**（EN 下残留中文）——生成器补齐后重建，EPUB 随后重建保持新鲜度。
4. 探针 D1 首版断言口径错误（预期 2 条深链，实际数据口径为 4 条）——修正断言而非数据，附口径说明见上。

## 已知口径与留待后续

- events.html 六事件未含 xAI 相关事件（e2025-03-28 仅账本），xAI 档案无事件深链区——R6/R7 既定口径，R9 时间轴升级时随事件扩容自然解决。
- 检索未覆盖 company-files.html——留 R15 搜索与发现（计划内）。
- before 证据仅 companies.html 卡片区（档案页为全新页面，git 历史即「不存在」的改前状态，worktree @ 7de17c8 截图佐证）。

## 结论

**本轮完成。** 51/51 探针 + 9/9 verify 全绿，桌面/390/EN/file:// 截图人工复核通过，证据在本目录（after 10 张 + before 1 张）。下一轮：R9 事件时间轴升级（v6.14.0）。
