# R10 验收记录（资源页基建 · v8.10.0）

日期：2026-10-01 · 轮次：V9-20 R10/20 · 模式：纯本地（不 push）

## 交付物

| 项 | 内容 |
|---|---|
| 数据单一事实来源 | tools/resources-data.py（10 条种子：official 2 / opensource 2 / community 2 / tools 4；validate() 内置，不过拒生成） |
| 生成器 | tools/build-resources.py（幂等生成 resources.html，第 38 页） |
| 导航注册 | tools/site-nav.py「资料」组 +resources.html；37 页重注入（38/38 页含入站链接，探针实测） |
| 检索 | build-search-index.py 增「社区资源」类型（断言同步）；索引 282 → 292；search.html 类型按钮 +1（共 10 枚） |
| verify.py 第 4 项 | 断言扩展 +rs-item 锚点计数（原约束原样保留，V7-19 R15 事件档案先例同款，CHANGELOG 已说明理由） |
| 样式 | style.css 末尾 rs-* 组件层（~55 行）：无新过渡（reduced-motion 免复核）、≤640 字段行纵排、print 隐藏筛选保留清单 |
| 版本三件套 | VERSION / app.js SITE_VERSION / 14 页 span → 8.10.0（bump 打印 14 处；resources.html 以 8.10.0 直接建档） |

## 种子清单（核活 2026-10-01，逐条实测）

sec-edgar-tesla（SEC 合规 UA 200）/ tesla-vehicle-command（705★, 2026-09）/ teslamate（9,061★, 2026-09, AGPL-3.0）/ grok-1（52,239★, 2024-08, 原仓库名 grok 已 301 迁移）/ elonmuskarchive（200）/ wbw-neuralink（200）/ flight-club（200）/ next-spaceflight（200）/ launch-library-2（200）/ starlink-sx（200）。
GitHub 数据来源 api.github.com（无认证、串行）；本机不可核活 7 条留档 EXPANSION.md R10 块（tesla.com/spacex.com/developer.tesla.com 403 反爬、neuralink.com 000、wikipedia DNS 污染、tesla-api.io DNS 失效疑似、openai.com 未测）。

## 验证结果

- **verify.py 9/9 全绿**：38 页 / 索引 292（115+18+42+31+5+53+4+14+10）/ 版本 8.10.0 / 语录卡 103+2 豁免 / 修订史 206 锚点 / CHANGELOG 首条 v8.10.0 / EPUB 含 e2026-07-22 且新鲜。
- **node --check app.js 通过**。
- **CDP 探针 27/27（tools/v9r10-probe.js，端口 9354，全新 user-data-dir）**：
  - 文件级 6：rs-item 锚 10 / 四分类节 / 生成器署名 / 索引 292 / pg=resources.html 10 条 / 入站导航 38/38 页。
  - 结构 8：hero+版本 / aria-current 资料·社区资源 / 2-2-2-4 分布 / rs-item=10 / 芯片五枚默认全选 / Teslamate 字段行（★9,061·AGPL·HTTP 200·2026-10-01）/ Grok-1 停更徽标+口径备注 / 外链 href 逐字双抽。
  - 筛选 2：开源项目芯片 aria-pressed 迁移+三节隐藏+状态行 2 条；全部恢复+状态行 10 条。
  - 双语 4：EN h1=Community Resources / 卡名卡描切换 / EN 状态行 Showing 4 / 切回中文复原。
  - 无 JS 2（Emulation.setScriptExecutionDisabled 实测）：10 条全量可见+无 rs-cat-off / SEC 字段行静态在册。
  - 检索联动 3：q=Teslamate 命中类型社区资源 / 类型按钮 10 枚 / type=社区资源 URL 参数+starlink-sx 深链命中。
  - 390 两项：零横向溢出（scrollWidth 390 ≤ clientWidth 390）/ 芯片行不溢出。
  - 首跑 26/27：唯一失败为探针自身计数断言写错（误写 11 枚，实际原 9+1=10）——页面对，断言修正后全绿（修正记录在案）。
- **截图**：qa/v9-20/round-10/resources-desktop.png（1440×900，芯片区）+ resources-390.png（390×844，Teslamate 卡）。

## 纪律自查

- 只收链接+简介+元数据，未复制任何外部正文 ✓（desc 均为本站自写一句话）
- 外链不构成运行时依赖：页面静态、无任何外域资源加载、file:// 结构可读 ✓（无 JS 实测+脚本仅做显隐）
- 死链不删如实标：本批无死链入库；疑似死链 tesla-api.io 留档未收 ✓
- 资源条目不作引语出处：页内「读法与口径」+ lr-foot 双处明示 ✓
- 工具类 4 条超「每类 1~2」软指引（当批核活全量入库），硬区间 8~12 内，CHANGELOG/账本/EXPANSION 三处注明 ✓
- sitemap.xml 按 R20 计划暂不动 ✓

## 本轮提交

- 成果提交：见 V9-20-PROGRESS.md 状态表（[V9-20 R10] 前缀）
- 第二提交：账本回填 + build-revisions + EPUB 重刷
