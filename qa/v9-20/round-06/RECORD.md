# V9-20 R06 验收记录 · 文档馆扩充（14 → 18 份）

日期：2026-10-01 ｜ 版本：8.5.0 → 8.6.0 ｜ 分支：main（本地，不推送）

## 本轮范围（计划 R06）

文档馆扩充：Master Plan 系列查缺 + SpaceX 官方更新信 + SEC 文件（S-1/10-K/xAI 披露若有），目标 +3~5。

## 成果（+4，documents.html 14 → 18）

| id | 文档 | 逐字源（双源） | 互链 |
|---|---|---|---|
| d2010-01-29 | Tesla Form S-1（IPO 招股书关键段） | EDGAR 0001193125-10-017054 ds1.htm 直读（唯源即权威原件） | e2010-06-29 / d2006-08 / d2022-02-07 |
| d2010-05-04 | Acronyms Seriously Suck（SpaceX 全员信） | 镜像 /email/spacex-acronyms-seriously-suck-2010 + gist 全文转载逐字一致（Ashlee Vance 传记收录） | i2021-07-30 / d2022-11-16 |
| d2021-11-26 | Raptor「破产警报」全员信 | 镜像 /email/spacex-raptor-bankruptcy-2021 + Newsweek 全文报道关键句逐字一致（逗号异文照录） | e2019-09-28 / p2024-10-13 |
| d2022-02-07 | Tesla Form 10-K FY2021（Technoking） | EDGAR 0000950170-22-000796 tsla-20211231.htm 直读 | d2010-01-29 / d2024-04-29 / d2022-10-27 |

- 员工外流文本口径如实标注（SPACEX 内部全员信 · 员工外流文本）；引语英文原文+中文对照，永不混写。
- 原文摘录与来源全档：sources/（镜像页×2 + gist + EDGAR 摘录 + Newsweek 摘要 + email 库全清单 47 封）。

## 计划候选盘点（写入 EXPANSION.md）

- Master Plan 系列：Part 1/Deux/3/IV 已全在册（d2006-08/d2016-07-20/d2023-04-05/d2025-09-01），无缺。
- SpaceX「官方更新信」：以 email 库两封全员信落位（Raptor 信即 Starship 进展警报）。
- xAI：私营无 SEC 备案；Series E 官方公告已在册（d2026-01）。
- 弃收：镜像 email 库其余 43 封（候选池，重验条件=逐封双源）；Epstein 两信（弱相关，不收）。

## 同步面

- documents.html：og:description + doc-path 导读（中英双语）十八份版；reading.html 计数同步。
- tools/build-search-index.py：一手文档断言 14→18；索引 267→271（109+18+42+31+5+53+4+9）。
- 生成器重跑：build-search-index / build-ledger-timeline（109 节点不变）/ build-epub（24 章）/ sync-changelog（195 条）。
- 版本三件套：VERSION + app.js SITE_VERSION + 14 页 span（8.5.0→8.6.0，替换计数 14 打印在案）。

## 验收门

- verify.py 9/9 全绿（37 页/索引 271）。
- node --check（app.js/cite.js）通过。
- CDP 探针 31/31（tools/v9r06-probe.js，记录 probe.txt）：文件级 7（索引 id/计数/逐字句）+ 桌面 16（18 卡渲染/五件套/Permalink 18 对/四卡逐字/doc-path 口径/双语/互链目标存在性）+ 检索 4（Technoking/acronyms/Raptor 命中 + wild swings 回归）+ 390 两项零溢出。
- 探针迭代说明：首轮 28/31——①10-K 卡单 blockquote 不符「多段摘录」先例，拆两段（内容不变，逐字保留）；②Raptor bankruptcy 双词查询超索引 q 字段（首段摘录无 bankruptcy 词），改单词查询；③回归词 funding secured 不在文档馆索引字段，改 wild swings。三处均为探针口径修正，非站点内容缺陷；修复后 31/31。
- 截图：documents-desktop/mobile + d2010/d2021 锚点视图（本目录）。

## 提交

- 成果提交：[V9-20 R06]（哈希见 git log，本地 main，不推送）
- 账本回填提交：第二提交（build-revisions + EPUB 重刷 + V9-20-PROGRESS.md 回填）
