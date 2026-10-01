# V9-20 R12 验收记录 · 开源项目资源（v9.2.0）

日期：2026-10-01（单轮单触发，锁 run=V9-20-R12）

## 成果

- resources-data.py +6 条（opensource 2→6 / community 2→3 / tools 4→5，全站资源 18→24）：timdorr-tesla-api（2,065★ MIT）/ r-spacex-api（10,912★ Apache-2.0，存档）/ starlink-grpc-tools（710★ Unlicense）/ tesla-api-io（停更）/ r-spacex-wiki / tessie（tools）。
- 索引 300→306；resources.html 幂等重建（v9.2.0）；changelog.html 201 条。
- **重要重验：R10「tesla-api.io 疑似死链」证伪**——本机 UDP DNS（8.8.8.8/1.1.1.1）全部被墙超时，独立解析改走服务端读取器：HTTP 200 且站点在线（自注 2024-01 起弃用，deprecated ≠ 下线）。判定为本地运营商 DNS 污染（同 wikipedia 污染机制），非死链。按「停更」收录，判定全过程卡内注明。
- **治本修复 revisions.html 导航回归**（R10/R11 连续两轮同处回归）：build-revisions.py 内联模板从不包含 site-nav 报头——本轮模板内嵌 `build_masthead()` + app.js（导航单一来源），重跑不再冲掉导航；探针新增「revisions.html 导航在册」断言防复发。

## 核活记录（详见 sources/liveness.md）

| 条目 | 路径 | 结果 |
|---|---|---|
| timdorr/tesla-api | api.github.com | 200，2,065★，pushed 2026-03，MIT |
| r-spacex/SpaceX-API | api.github.com | 200，10,912★，pushed 2024-08，**archived=true** |
| sparky8512/starlink-grpc-tools | api.github.com | 200，710★，pushed 2026-09，Unlicense |
| tesla-api.io | 本机 curl/DNS 全败（污染）→ 服务端读取器 | **200（死链证伪）** |
| r/SpaceX wiki | 本机 curl 000 → 服务端读取器 | 200 |
| tessie.com | 本机 curl 直连 | 200 |

甄别排除：Look4Sat（卫星追踪通用工具，与马斯克系弱相关）、sgayou/subaru-starlink-research（**斯巴鲁**车载 StarLink 同名不同司）、SmoothWAN（通用组网）。

## 验证

| 项 | 结果 |
|---|---|
| resources-data.py validate() | ✓ 24 条 {official 10, opensource 6, community 3, tools 5} |
| build-resources.py / build-search-index.py | ✓ 24 条 / 索引 306 |
| sync-changelog.py | ✓ 201 条（v0.1.0 → v9.2.0） |
| 版本三件套 | ✓ 9.1.0→9.2.0，15 页 span，复核全一致 |
| build-revisions.py | ✓ 206 锚点幂等，**导航在册（治本后首次重跑验证）** |
| build-epub.py | ✓ 220,597 B · 24 章 |
| node --check | ✓ app.js 与探针均过 |
| verify.py | ✓ 9/9（38 页 / 索引 306） |
| CDP 探针 tools/v9r12-probe.js（端口 9356） | ✓ **28/28**：文件级 9（含 revisions 治本断言）/结构 9/筛选 2/双语 3/无 JS 1/检索联动 3/390 零溢出 2 |

## 探针插曲

首跑 17 项过即中断——qa/v9-20/round-12/ 目录不存在致截图写失败（mkdir 后重跑全绿）。非页面缺陷。

## 产物

- 截图：resources-opensource-desktop.png（1440×900，tesla-api.io 卡定位）/ resources-spacexapi-390.png（390×844，SpaceX-API 存档卡）。
- sources/liveness.md + liveness-r12.json：核活与甄别全记录。
- 工具脚本：tools/v9r12-bump.py / v9r12-probe.js。

## 提交

- 成果提交：`[V9-20 R12]`（本地，不推送）。
- 第二提交：账本回填 + build-revisions + EPUB 重刷。
