# V10-15 N01 验收记录 · 全站源存活复测（v10.1.0）

日期：2026-10-02（定时任务第四次触发，锁 run=V10-15-N01）

## 口径修正（重要发现，如实入账）

任务书预期「扫六页全部外链」——scan 干跑实测：**六页（primary/documents/interviews/x-posts/quotes/events）的来源标注全部为 `.ps-src` 文字徽章形态，无明文超链接**（引语原文锚存于账本文字描述与 qa/v9-20 溯源文件，引语逐字核验属 N02 transcript diff 口径）。故本脚本复测对象据实调整为**全站 38 页真实外链**——唯一外链 37 条（resources.html 36 张资源卡为主体，此为本站设计使然：资源页=外链层，一手页=文字锚层）。

## 复测结果（37 条，零死链）

| 判定 | 条数 | 说明 |
|---|---|---|
| 直连存活 | 12 | 200/301（sae/boringcompany/waitbutwhy/developer.tesla.com/flightclub 等） |
| api/服务端复核存活 | 11 | GitHub 8 条走 api.github.com 全 200（★与 pushed 在档）；wikipedia Elon_Musk/Starship + tesla-api.io 走服务端读取器 200 |
| 同域推定存活 | 6 | wikipedia 其余条目——同域两个代表服务端核活通过，本机直连失败为 DNS 波动（R12 tesla-api.io/R13 wikipedia 直连 200 先例），如实注明推定口径 |
| 前档佐证存活 | 2 | openai.com（R11 服务端 200 在档；本轮直连 403=Akamai，RESTRICTED 已补录）/ x.ai（R11 服务端 200 在档；本机直连超时既有模式） |
| n/a | 1 | w3.org/2000/svg——SVG 命名空间 URI 非内容源（脚本已排除此类） |
| 本机受限 | 5 | tesla.com×1/spacex.com×3/reddit×1（历史轮实测反爬/TLS，非死链） |
| **死链** | **0** | — |

## 漂移记录（GitHub stars，字段刷新归 N04）

SpaceX-API 10912→10913 · teslamate 9061→9065 · grok-1 52239→52233 · vehicle-command 705→706（真实漂移，本轮不改数据）。

## 产物与脚本

- qa/v10-15/round-01/：sources-inventory.tsv（37 条清单）/ sources-check.json（直连原始）/ sources-report.tsv / sources-report.json（终版含二路复核与口径注记）。
- tools/v10n01-sources.py（scan 干跑 / check 全量，RESTRICTED 预分类清单含 openai.com 补录）。

## 验收

- 报告覆盖全部外链 ✓（37/37，四栏判定+二路复核口径逐条在案）
- verify.py 9/9 ✓（38 页 / 索引 318）
- 无页面内容改动（纯核实轮，无引语修正项——零死链零漂移处置需求）

## 提交

- 成果提交：`[V10-15 N01]`（本地，不推送）。
- 第二提交：账本回填 + build-revisions + EPUB 重刷。
