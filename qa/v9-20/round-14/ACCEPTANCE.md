# R14 验收记录 · 资源交互与联动（质量节点②）— complete（v9.4.0）

日期：2026-10-01 · 轮次：V9-20 R14/20

## 本轮范围（计划 R14 原文对照）
| 计划要求 | 落实 |
|---|---|
| 分类筛选 + aria-live 状态行 | `#rs-status` 加 `role="status" aria-live="polite"`（build-resources.py 模板源改） |
| 资源↔公司档案/事件互链（companies 面板与 company-files 加「相关社区资源」行） | 两处均落地：company-files 4 档案各加 `.cf-resl` 节（16 深链）；companies 面板 `netRender` 增「相关社区资源（N）」行 |
| 首页资料入口 | index.html「查找资料」路径行第三入口改指 resources.html |
| 检索命中（含类型筛选） | search.html 类型按钮「社区资源」+ 公司过滤对资源条目可用（R10 接通，本轮验证） |
| 质量节点②：资源页全流程探针（筛选/清除/跳转/双语/无 JS/390/file://）≥15 断言 | **CDP 探针 30/30**（8 大流程全覆盖，见下） |
| 外链抽样 10 条核活 | qa/v9-20/round-14/sources/liveness-sample.md，**10/10 可达** |
| verify 9/9 | 通过 |

## 验证结果
| 项 | 结果 |
|---|---|
| verify.py | **9/9 全绿**（38 页 / 索引 318 / 版本 9.4.0 / 语录卡 103+2 豁免 / 修订史 206 / EPUB 新鲜） |
| node --check | app.js / search-index.js / companies-data.js / events-data.js / timeline-events.js / capital-data.js / v9r14-probe.js 全通过 |
| CDP 探针（质量节点②） | **30/30 全绿**（tools/v9r14-probe.js，端口 9358） |
| 外链抽样核活 | **10/10 可达**（官方 2 / 开源 2 / 社区 3 / 工具 3） |
| 版本三件套 | 9.3.0→9.4.0（VERSION + app.js + 15 页 span） |
| EPUB | 223,127 bytes / 24 章 |
| 截图 | qa/v9-20/round-14/ 4 张（resources-filter-community-desktop / companyfile-tesla-resources-desktop / companyfile-resources-390 / companies-panel-resources-desktop） |

## 探针断言分布（30 项）
- 文件级 8：aria-live 契约 / 4 档案 cf-resl 节 / 深链格式 / companies-data.js resources 字段×4 / 首页入口 / 索引 318·资源 36 / 版本 9.4.0。
- 流程 1 筛选 4：aria-live 生效 / 状态行即时变化含「11」/ 三节隐藏 / 芯片 aria-pressed 同步。
- 流程 2 清除 1：点全部恢复 36。
- 流程 3 跳转闭环 5：档案链接存在 / #file-tesla cf-resl / 深链可达 / 4 档案全渲染 / 点击深链回资源页锚定成功。
- 流程 4 双语 3：EN 状态行 / EN 节名 / 切回中文。
- 流程 5 无 JS 2：36 条全量 / 静态文本「筛选需脚本支持」。
- 流程 6 390 2：资源页零溢出 / 公司档案零溢出。
- 流程 7 file:// 2：资源页 36 条 / 公司档案 cf-resl 渲染。
- 流程 8 关系图面板 3：数据契约 / 面板「相关社区资源」段 / 6 深链计数。

## 探针记录（0 修正，1 处先目检后写断言）
- **先目检 DOM 再写断言（教训第四次生效）**：写公司关系图面板交互断言前先 grep 实构，确认为 `<g class="net-node" data-net-node="tesla">`（非猜测的 `.net-node[data-net=…]`），一次通过，未浪费复跑。
- 首跑即 30/30，无断言修正。

## 数据单一事实来源与联动架构
- `resources-data.py` 新增 `resources_for_company(company_name, limit)` 查询接口（按 companies 实体匹配、category 序稳定排序、「综合」不参与）。
- `build-company-files.py`：新增 `COMPANY_TO_VOCAB`（档案 id→实体词表名）+ 引入 RD；渲染 `.cf-resl` 节；向 `companies-data.js` 的 companies 注入 `resources: [{id,name}]` 字段。
- `app.js`：`netRender` 增「相关社区资源」段（读 `c.resources`，中英双语）。
- **架构原则保持**：资源数据只存于 resources-data.py，公司档案与关系图均经「查询接口」引用，未复制内容、未引入运行时依赖（外链仍为静态 href）。
