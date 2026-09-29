# V8 计划进度记录（第一手信息扩充）

> 「马斯克商业志 MUSK, INC.」v8.0 扩充计划（共 10 轮，2026-09-30 启动）。
> 本文件是本计划的唯一轮次账本；与 git 提交记录相互核验，不以提交总数推算轮次。
> 历史计划（V7 十九轮改版，v6.6.0→v7.0.0）已完结，见 `V7-19-PROGRESS.md`，不继承其计数。

## 基线快照（2026-09-30 核对）

- 分支 main @ `d0b8b4b`（V7-19 R19 收官提交），VERSION `7.0.0`
- 工作区干净；37 个 HTML 页面；账本 67 条；检索索引 178 条；verify.py 9 项检查
- 每轮版本步进：R01=v7.1.0 → R09=v7.9.0 → R10=v8.0.0（每轮 bump，防版本重复，吸取 v5.88.1 教训）

## 轮次状态

| 轮 | 主题 | 状态 | 版本 | 成果提交 | 推送 |
|---|---|---|---|---|---|
| 01 | 建 V8-PROGRESS.md + funding secured 案（SEC v. Musk） | complete | v7.1.0 | 398b249 | done |
| 02 | Twitter 收购案私信原件（特拉华衡平法院披露件） | pending | — | — | — |
| 03 | SEC EDGAR 公文扩容（8-K/proxy/合并协议条款） | pending | — | — | — |
| 04 | 财报电话会 I（2013–2018） | pending | — | — | — |
| 05 | 财报电话会 II（2019–2026） | pending | — | — | — |
| 06 | 长访谈 I：Lex Fridman 四期 | pending | — | — | — |
| 07 | 长访谈 II：Rogan / TED / All-In / DealBook | pending | — | — | — |
| 08 | X 帖史扩容（含 Wayback 核对已删帖） | pending | — | — | — |
| 09 | SpaceX / Neuralink / xAI 官方演讲 | pending | — | — | — |
| 10 | 全站验收与发布 v8.0.0 | pending | — | — | — |

状态取值：pending / in_progress / complete / blocked。失败不推进轮次；推送失败时仅恢复推送。

## 恢复指引

- 每轮唯一成果提交信息带 `[V8 Rxx]` 前缀；工作记录追加在本文件末尾。
- 提交了但没推送 → 直接 `git push`，不重做工作。
- 账本/一手页变动后必跑：`build-ledger-timeline.py` / `build-search-index.py`（改断言）/ `build-epub.py`；CHANGELOG 更新后跑 `sync-changelog.py`；最后 `verify.py` 9 项全绿。
- 采料纪律：查不到原文不写；媒体转载两源印证；引语保留英文原文+中文对照。
- 本计划不再新建分支，直接在 main 上逐轮提交（V7 时代分支流程已完成使命）。

## 核实来源留档（R01）

SEC v. Musk（S.D.N.Y. No. 1:18-cv-08865；CourtListener docket 7946295）：
- 起诉新闻稿（2018-09-27）：https://www.sec.gov/news/press-release/2018-219
- 起诉书 PDF：https://www.sec.gov/litigation/complaints/2018/comp-pr2018-219.pdf
- 和解新闻稿（2018-09-29，含 Tesla 单独指控）：https://www.sec.gov/news/press-release/2018-226
- 案卷（Final Judgment Dkt.14 / show cause Dkt.19 / 修正判决 Dkt.47 / Liman 裁决 Dkt.81 / mandate Dkt.97）：https://www.courtlistener.com/docket/7946295/united-states-securities-and-exchange-commission-v-musk/
- SEC 函件 2019-02-20（引述 2/19 两条推文全文）：RECAP Dkt. 18-2（storage.courtlistener.com 公开件）
- SEC 藐视动议附件（预审政策 Dkt. 18-1）：RECAP 公开件
- 第二巡回 Summary Order（2023-05-15，No. 22-1291）：Courthouse News 公开件 https://www.courthousenews.com/wp-content/uploads/2023/05/22-1291-SEC-musk-ruling.pdf
- 60 Minutes（2018-12-09）：CBS 片段「I have no respect for the SEC」+ LA Times / Ars Technica / NZ Herald / WaPo 四源印证引语
- 2022 简报引语：Reuters「a deal is a deal」（2022-03-22）+ Boing Boing / Fox Business 转载（两源印证）

## 第 1 轮工作记录（funding secured 案）— complete（2026-09-30）

- **交付**：V8-PROGRESS.md 建立（本文件，含 10 轮状态表/恢复指引/来源留档）；账本 primary.html +7 条（67→74，严格克隆既有 `<li class="ps-row ps-deep reveal">` 结构，四段深读双语）：e2018-09-27 SEC 起诉、e2018-09-29 两天和解（含 10/16 Final Judgment）、e2018-12-09 60 Minutes「I do not respect the SEC」、e2019-02-19 产量推文与藐视动议、e2019-04-30 修正终审判决终结藐视战、e2022-03-08 终结动议与 Liman 驳回、e2023-05-15 第二巡回维持 + Fair Fund 分发；quotes.html 核实卡 +7（54→61）；controversy.html#sec-sec 补法庭弧线入口并把 60 Minutes 引语由「暂作参考记录」转正链接账本；promises.html 第 03 案来源列表补弧线行；index.html 三处计数文案 67→74。
- **采料与核实**：全部条目第一手锚点——SEC 官网新闻稿 2018-219/2018-226 + 起诉书 PDF（comp-pr2018-219.pdf，逐字提取）+ CourtListener 案卷 7946295（Final Judgment/show cause/修正判决/Liman 裁决/mandate 等 12 个节点，docket 文本直接引用）+ RECAP 公开件（SEC 2019-02-20 函件引述两条推文全文、第二巡回 Summary Order 22-1291 全文）+ 60 Minutes 四源印证 + 2022 简报引语 Reuters/Boing Boing/Fox Business 多源印证。案号勘误：正确案号 1:18-cv-08865（任务书里的 08695 有误）。完整 URL 清单见本文件「核实来源留档（R01）」节。
- **管线修复（遗留漂移）**：build-search-index.py 的访谈页 h2 正则在 V7-R17 双语化（h2 加 data-en 属性）后失配——生成器自那之后未再重跑，本轮重跑暴露；已最小修复（`<h2>` → `<h2[^>]*>`），未动页面。断言 言行实录 67→74。
- **验证**：verify.py 9/9 全绿（索引 185 = 74+9+18+13+5+53+4+9；时间轴 74 节点；语录卡 61 vs 引文块 64 豁免 3；EPUB 含最新条目）；node --check app.js cite.js 通过；版本 v7.0.0→v7.1.0（VERSION/app.js/14 页 span），CHANGELOG 首条 v7.1.0，changelog.html/revisions.html/EPUB 重跑。
- **提交**：主成果 `398b249`（25 文件，+449/−231），已推送 main；本回填为第二个提交。
- **范围说明**：本轮按计划只动账本一手体系；编年史行未加（2018.08.07 行已覆盖 SEC 案入口，chronicle 53 断言不动）；新条目暂未挂 ps-linkcard（事件档案归 events-data.py 体系，如需建档卡建议在后续轮统一评估）。
- **下一轮预告**：R02 Twitter 收购案私信原件（特拉华衡平法院 2022 披露件），账本目标 +8~10 条。
