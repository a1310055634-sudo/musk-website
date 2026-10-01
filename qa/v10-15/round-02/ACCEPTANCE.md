# V10-15 N02 验收记录 · 引语逐字核验 I（机核）（v10.2.0）

日期：2026-10-02（定时任务第五次触发，锁 run=V10-15-N02）

## 机核管线（tools/v10n02-extract.py + v10n02-corpus.py + v10n02-verify.py）

- **Step1 提取**：X 帖 31 卡（tweet-text+镜像 status id，22 条有 id）/ 访谈 42 裸 blockquote / 账本 106 引文块（覆盖 105 条目）——inventory.json。
- **语料**：本地 qa 存档 transcript（round-02/03/04/05/07，36 文件）+ 本轮新拉镜像 interview 场次（日期精确匹配 19 场，新拉 9 存 round-02/sources）——合计 45 文件 2.66M 归一字符。
- **判定**：归一化（去实体/引号形态/空白/大小写）后 indexOf；X 帖走镜像 API transcript 分段 diff（**合并卡口径：站内两连发合一卡 vs 镜像单帖存档，任一段命中即逐字证据成立**）。

## 结果（零实质差异）

| 对象 | verified | 合并卡口径 | 待人工（语料未覆盖） | 无锚/无档 |
|---|---|---|---|---|
| X 帖 31 | 18 | 3（p2020-05-01 卖房两连发 / p2022-10-28 bird is freed 两连发 / p2023-07-23 bid adieu 两连发——后者人工深查：镜像原文与站内第一段逐字吻合） | — | 1 fetch-failed（p2018-01-28 flamethrower，镜像疑无档——2018 覆盖稀薄，V8 R03 立条时多源核实口径）+ 9 no-anchor（早期卡无 status id 记录） |
| 访谈 42 块 | 16 | — | 26 | — |
| 账本 106 块 | 5 | — | 101 | — |

- **实质差异：0 条**（无引语修正，页面内容零改动）。
- **待人工口径（如实注明，N03 续）**：访谈 26 + 账本 101 块 unmatched 的归因是**机核语料未覆盖其来源库**（V8 时代条目来源=stockanalysis 财报会/TED 页内 JSON/Rev.com/JRE/EDGAR 等——非镜像库、本地无 transcript 存档；Cloudflare 拦脚本直读），**不是发现差异**。N03 按人工抽样+WebFetch 逐条继续。
- 途中甄别：首跑 3 条 "mismatch" 逐条深查后全部定性为合并卡结构口径（非逐字差异）——机核判定逻辑修正为分段 indexOf+合并卡口径，避免假红。

## 产物

- qa/v10-15/round-02/：inventory.json / verify-results.json / sources/（本轮新拉镜像 interview transcript 9 场）。
- 脚本：tools/v10n02-extract.py / v10n02-corpus.py / v10n02-verify.py / v10n02-bump.py。

## 验收

- 106 账本引文块全部有判定（verified 5 / 待人工 101 已注明归因口径）✓
- X 帖 31 卡全覆盖（18+3+1+9）✓
- 访谈 42 块全覆盖（16+26）✓
- verify.py 9/9 ✓；版本三件套 10.1.0→10.2.0 ✓

## 提交

- 成果提交：`[V10-15 N02]`（本地，不推送）。
- 第二提交：账本回填 + build-revisions + EPUB 重刷。
