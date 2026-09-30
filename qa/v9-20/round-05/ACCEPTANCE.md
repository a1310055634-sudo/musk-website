# V9-20 R05 验收记录 · 访谈扩充 II（Lex 候选消化 + 官方转写新批次）

日期：2026-10-01 ｜ 版本：8.4.0 → 8.5.0 ｜ 计划锚：V9-20-PROGRESS.md R05

## 本轮范围（计划书 R05）

- 必做：EXPANSION 留档的 Lex #252（I love humanity / life insurance for life / bang or a whimper）与 #400（free-speech 段）已核实引语立条。
- 候选：Acquired 播客（若有官方稿）、MKBHD 2018、其他大会 keynote。
- 验收：EXPANSION 候选清零或逐条注明保留原因。

## 完成（访谈 37 → 42 条，索引 262 → 267）

| id | 条目 | 场次 | 逐字源 |
|---|---|---|---|
| i2021-12-28-2 | 「给生命本身买保险」 | Lex #252 文明与火星段 | elonmuskarchive.org transcript（lex-fridman-252，119,586 字符，YouTube 字幕源） |
| i2023-11-10-2 | 「言论自由的试金石」 | Lex #400 平台与媒体段 | lexfidman.com 官方稿（01:43:13 / 02:02:38 段，镜像转写 116,518 字符对表） |
| i2013-02-27 | 「一枚完全且快速可复用的火箭」 | TED2013 · Chris Anderson | 镜像 transcript（ted-2013-02-27，19,924 字符） |
| i2014-09-25 | 「火星宪法草案」 | Code Conference 2014 · Kara Swisher | 镜像 transcript（code-conference-2014-09-25，72,966 字符） |
| i2018-08-15 | 「我们不花一分钱广告费」 | MKBHD Talking Tech · Tesla 工厂 | 镜像 transcript（talking-tech-with-marques-brownlee-2018-08-15，17,996 字符） |

- 计划必做三项全部落实：#252「life insurance for life」入引语块、「I love humanity」入引语块、「bang or a whimper」入编者注（含中文对照）；#400 free-speech 句 + 「worst thing that happened on Earth today」媒体段（V8 R06 留档一并落实）。
- 同场多条为站内既有结构（#18/#49/#252/#400 各两条先例），新条 id 用 `-2` 后缀符合索引正则 `i\d[\d-]*`。
- 插入位置：Lex 两条随组插在 #252/#400 既有条目后；TED2013/Code2014/MKBHD2018 三条以「R05 批次」注释区插在 R04 批次后。
- 互链：Code2014→x-posts.html#p2025-07-05（America Party 弧线）；MKBHD→promises.html#promises-s4（2.5 万美元车未兑现）+ 页内 i2017-07-28；TED2013→页内 i2024-10-13（塔接兑现）+ i2018-08-15；#400→platform-x.html + 页内 i2022-11-16。

## 甄别（宁缺毋滥，EXPANSION 详录）

1. TED2013 官方转写无「I would like to die on Mars」句——存量无 id 条目维持「广泛征引」标注，新条独立锚定，两不相扰；该名句出处待考留档。
2. Acquired 播客：镜像 0 条目 + 官网列表抽查无本人出场（公司史叙事播客），不构成第一手信息，不立条；重验条件留档。
3. Lex #438（Neuralink 团体访谈）转写在档本轮不立，入候选池。
4. 字幕平面化口径（Code2014/MKBHD/TED2013）卡内注明；Code2014「60 of people」字幕脱漏百分号已注明编者补回；「king of moss」误听未入引语。

## 候选池收尾（计划验收要求「清零或逐条注明」）

- 已消化：ted-2013 / code-conference-2014 / mkbhd-2018 三场 + Lex #252/#400 留档引语全部落实。
- 保留池（立条资格成立，受单轮 +5 上限约束，留后续轮次，共 6 场）：allthingsd-d11-2013、60-minutes-2012、code-conference-2021、ark-invest-2019、e3-coliseum-2019、lex-fridman-438。161 场全清单存 qa/v9-20/round-04/interviews-all.json。

## 验证证据

- verify.py 9/9 全绿（37 页/索引 267 = 109+14+42+31+5+53+4+9；版本 8.5.0 一致）。
- node --check app.js 通过。
- CDP 探针 tools/v9r05-probe.js（端口 9336，全新 user-data-dir）：**29/29 全过**——文件级 8（五卡入索引/访谈 42/总数 267/五卡逐字句入索引）+ 桌面结构 4 + 五卡逐字 5 + 双语 1 + 互链锚 6 + 检索 3（censorship/insurance 命中 + DMV 回归）+ 390 溢出 2。
- 截图 8 张：before-interviews-head-desktop/390（git worktree @9adff03 独立服务 8767 截取真改前）+ after 五卡桌面定位（CDP scrollIntoView）+ R05 批次 390。

## 管线与提交

- 断言：tools/build-search-index.py 访谈 37→42。
- 生成器：build-search-index（267）/ build-ledger-timeline（109 幂等）/ sync-changelog（194 条）/ build-epub（211,383 B, 24 章）。
- 版本三件套：VERSION + app.js SITE_VERSION + 14 页 site-version-val span（替换计数 14 打印在案）。
- 提交：成果提交 [V9-20 R05]（v8.5.0）；第二提交=账本回填 + build-revisions + EPUB 重刷。纯本地，不推送。
