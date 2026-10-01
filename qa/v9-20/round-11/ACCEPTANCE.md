# V9-20 R11 验收记录 · 官方与标准类资源（v9.1.0）

日期：2026-10-01（单轮单触发，锁 run=V9-20-R11-takeover3）

## 成果

- resources-data.py +8 条全落官方与标准类（official 2→10，全站资源 10→18）：spacex-starship / spacex-falcon9 / spacex-updates / tesla-fleet-api / neuralink-registry / openai-2015 / xai-official / boringcompany-official。
- COMPANIES_VOCAB 增 OpenAI 实体（仅资源条目；build-search-index 经 CO_MAP 透传，检索「按公司过滤」自动出现，存量 282 条实体推断零扰动）。
- 索引 292→300；resources.html 幂等重建（v9.1.0 署名）；changelog.html 200 条；EPUB 24 章。
- **附带修复**：R10 第二提交引入的导航回归——build-revisions.py 重建 revisions.html 时丢失「资料」组链接（R10 探针在提交前跑，回归未暴露）。本轮 site-nav.py 全站重注入后 38/38 页恢复，探针新增「38/38 入站导航」断言防复发。

## 核活（三路法：curl → WebFetch → 服务端读取器）

8 条入库全部 2026-10-01 实测，路径与证据见 sources/liveness.md：
- 直连 200：boringcompany.com（1 条）
- 服务端读取器 200（直连 403/重置/超时，卡内 note 如实注明）：spacex 三页、developer.tesla.com、neuralink patient-registry、openai 2015、x.ai（7 条）
- 弃收留档：SAE J3400（JS 壳内容不可验）、tesla.com 全站（三路均被 Akamai 拦）——EXPANSION.md R11 块。

## 验证

| 项 | 结果 |
|---|---|
| resources-data.py validate() | ✓ 18 条 {official 10, opensource 2, community 2, tools 4} |
| build-resources.py | ✓ 幂等重建，18 条 · 4 类 |
| build-search-index.py | ✓ 300 条，社区资源 18，OpenAI 实体 1 处 |
| sync-changelog.py | ✓ changelog.html 200 条（v0.1.0 → v9.1.0） |
| 版本三件套 | ✓ VERSION / app.js SITE_VERSION / 15 页 span（含 resources.html），复核全一致 |
| build-epub.py | ✓ 220,597 B · 24 章 |
| node --check | ✓ app.js 与探针均过 |
| verify.py | ✓ 9/9（38 页 / 索引 300；EPUB 修复后复跑两轮均绿） |
| CDP 探针 tools/v9r11-probe.js（端口 9355） | ✓ **30/30**：文件级 9（含 38/38 导航、OpenAI 实体唯一、反爬注记 7 处）/ 结构 9 / 筛选 2 / 双语 3 / 无 JS 2 / 检索联动 4（OpenAI 命中+公司过滤按钮+过滤后保留+Starship 命中）/ 390 零溢出 2 |

## 探针修正记录

- 首跑 28/30：①「official 节 10 条」文件级断言用 data-cat 切分被筛选芯片同名属性干扰（页面 DOM 断言同口径已过，页面正确）——改用 section id 定界后过；②「入站导航 38/38」实为真回归（revisions.html），修复后过。两处均非页面缺陷掩盖。

## 产物

- 截图：resources-openai-desktop.png（1440×900，OpenAI 卡定位）/ resources-openai-390.png（390×844）。
- sources/liveness.md：三路法全记录（14 候选 URL 结果表）；sources/liveness-r11.json：curl 层原始结果。
- 工具脚本：tools/v9r11-liveness.py / v9r11-bump.py / v9r11-probe.js / v9r11-checkproc.ps1（进程归属检查）。

## 提交

- 成果提交：见 git log `[V9-20 R11]`（本地，不推送）。
- 第二提交：账本回填 + build-revisions + EPUB 重刷。
