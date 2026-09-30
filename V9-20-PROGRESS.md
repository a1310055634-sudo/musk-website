# V9-20 计划进度记录（第一手信息扩充 + 开源社区资源板块 + 美术升级）

> 「马斯克商业志 MUSK, INC.」V9-20 升级计划（共 20 轮，2026-10-01 启动）。
> 本文件是本计划的唯一轮次账本；与 git 提交记录相互核验，不以提交总数推算轮次。
> 历史计划：V7 十九轮改版（v6.6.0→v7.0.0）见 `V7-19-PROGRESS.md`；V8 十轮扩充（v7.1.0→v8.0.0）见 `V8-PROGRESS.md`。不继承其计数。

## 运行模式（重要）

- **纯本地模式**：每轮仅做本地 git 提交，**绝不 push、不 fetch 后合并远程、不改写已有历史、不做云端发布与 Pages 验证**。第 20 轮输出「待发布清单」，由用户验收后自行推送。
- 每次触发完成一个未完成轮次；上轮中断先恢复。成功轮次共 20；失败/空触发/重复检查不增加轮次；一轮未验收不进下一轮。
- 20 轮全部本地验收通过后，后续触发**静默退出**（不改文件不加版本不提交）。
- 每轮锁：`.v9run.lock`（不入 git，已在 .gitignore）。有效锁直接退出；确认旧实例已死（进程+仓库静默>15min）才可恢复遗留锁。

## 基线快照（2026-10-01 核对）

- 分支 main @ `24020fe`（V8 R10 本地版收官提交），VERSION `8.0.0`；origin/main 停在 `355fc0d`（v7.9.0 时代）——**待用户推送**。
- 工作区干净：37 个 HTML 页面；账本 109 条；一手文档 14；访谈 33；X 帖 23；语录卡 96（引文块 99，豁免 3）；检索索引 250（109+14+33+23+5+53+4+9）；事件档案 9 档 37 材料；时间轴 109 节点 + 223 独立记录（吸收 18）；资本流向 18 笔；修订史 179 锚点；EPUB 24 章；verify.py 9 项。
- 每轮版本步进：R01=v8.1.0 → R19=v9.9.0 → R20=v10.0.0（每轮必 bump，以 VERSION 实测为准不降级）。版本三件套 = VERSION + app.js SITE_VERSION + 14 页 site-version-val span（替换计数须打印）。

## 轮次状态

| 轮 | 主题 | 状态 | 版本 | 成果提交（本地） | 备注 |
|---|---|---|---|---|---|
| 01 | V8 R10 收尾 + V9-20 基建（账本/锁/gitignore） | complete | v8.1.0 | （见工作记录） | 含 V8 R10 本地版 |
| 02 | X 帖回捞 I（2020–2021），目标 23→27± | pending | — | — | — |
| 03 | X 帖回捞 II（2022–2025 深水区），目标 31± | pending | — | — | — |
| 04 | 访谈扩充 I（Code Conf 2016 / EA 星舰 / Swisher / Satellite 2020） | pending | — | — | — |
| 05 | 访谈扩充 II + Lex 候选消化（#252/#400 立条） | pending | — | — | — |
| 06 | 文档馆扩充（Master Plan 缺 / SpaceX 更新信 / SEC 文件） | pending | — | — | — |
| 07 | 官方演讲扩充（Starship 更新会 / Neuralink demo / AI Day） | pending | — | — | — |
| 08 | 事件档案聚合扩容（9→14±，口径红线探针） | pending | — | — | — |
| 09 | 语录卡补齐 + 质量节点①（盘点总表入账本） | pending | — | — | — |
| 10 | 资源页基建（resources-data.py + build-resources.py + 导航注册） | pending | — | — | — |
| 11 | 官方与标准类资源 | pending | — | — | — |
| 12 | 开源项目资源（Tesla API 生态 / Starlink 追踪 / 发射工具） | pending | — | — | — |
| 13 | 社区与档案资源 + 元数据补全（R11–13 合计 +30~50 条） | pending | — | — | — |
| 14 | 资源交互与联动 + 质量节点②（≥15 断言） | pending | — | — | — |
| 15 | 设计系统升级（style.css :root tokens，四页样板） | pending | — | — | — |
| 16 | 首页视觉迭代 | pending | — | — | — |
| 17 | 数据图形工业风（gx-*/cap-*/net-* 三图精修） | pending | — | — | — |
| 18 | 排版与阅读体验（lr-*/ps-*） | pending | — | — | — |
| 19 | 动效与微交互 + 质量节点③ | pending | — | — | — |
| 20 | 全站验收 + 待发布清单（v10.0.0，不推送） | pending | — | — | — |

状态取值：pending / in_progress / complete / blocked。失败不推进轮次。备注列记本地提交哈希与要点。

## 恢复指引

- 每轮唯一成果提交信息带 `[V9-20 Rxx]` 前缀；工作记录追 加在本文件末尾。每轮原则上一个成果提交+一个账本回填提交。
- 提交了但中断 → 账本行回填后直接进下一轮，不重做工作。
- 账本/一手页变动后必跑：`build-ledger-timeline.py` / `build-search-index.py`（断言同步）/ `build-epub.py`；CHANGELOG 更新后跑 `sync-changelog.py`；提交后 `build-revisions.py` + EPUB 重刷为第二提交内容；最后 `verify.py` 9 项全绿。
- 采料纪律：查不到原文不写；媒体转述两源印证；引语保留英文原文+中文对照；X 帖 snowflake 解码对表；弃收件写入 EXPANSION.md。
- 复杂 Python 改动写成 .py 文件执行（heredoc 中文/引号必失真）；工作区 CRLF/LF 混合，行级比较 rstrip('\r')。

## 三大目标

1. **第一手信息**：R02–R07 回捞 X 帖/访谈/文档/演讲（锚：elonmuskarchive.org 镜像、官方 transcript、SEC EDGAR 等）；R08 事件聚合；R09 语录卡补齐。
2. **开源社区资源板块**：R10–R14 新建 resources.html（单一事实来源 tools/resources-data.py；只收链接+简介+元数据；外链不构成运行时依赖，file:// 离线可读；每条 URL 实访核活）。
3. **美术升级**：R15–R19 设计系统 tokens → 首页 → 数据图形 → 排版 → 动效（深色 #101316 / 暖白 #F3F0E8 / 朱红 #C84032 主基调不变；每轮 before/after 截图入 qa/v9-20/）。

## 第 1 轮工作记录（V8 R10 收尾 + V9-20 基建）— complete（2026-10-01）

- **V8 R10 本地版**：R09 状态核对（已 complete+回填+推送确认 355fc0d，无需补）；口径总核对 250 = 109+14+33+23+5+53+4+9；生成器全家桶十件幂等重跑全过（events/timeline-events/network/company-files/capital/ledger-links/search-index/sync-changelog/revisions/epub）；verify.py 9/9（37 页/索引 250/8.0.0 一致）；版本三件套 → 8.0.0（14 span 替换计数打印）；CHANGELOG 补 v8.0.0 条目；changelog.html 189 条；修订史 179 锚点；EPUB 24 章 201,489 B。V8 账本 R10 行改 complete「本地提交/不推送（用户验收后自行推送）」并附工作记录。成果提交 `24020fe`（含 .gitignore 补 .v9run.lock——首次建锁曾被 `git add -A` 带入提交，已 amend 移除，锁文件从此不入 git）。
- **V9-20 基建**：本账本建立（基线快照 + 20 轮状态表 + 恢复指引）；`.v9run.lock` 锁机制就绪。
- **下一轮预告**：R02 X 帖回捞 I（2020–2021）——镜像 elonmuskarchive.org 列表页 ?year=2020/2021&page=N&sort=old 全量回捞，候选 COVID 早期表态补充/卖房系列后续/2021 关键节点帖；重验 V8 弃收件 Hertz 对冲（2021-10-26 前后 8 页找 "no contract has been signed yet"）。
