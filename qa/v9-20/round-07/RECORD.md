# V9-20 R07 工作记录（官方演讲扩充：镜像 keynote/speech 全档转写批次）

- 轮次：R07/20 ｜ 版本：8.6.0 → 8.7.0 ｜ 日期：2026-10-01
- 交付：primary.html +6 条（109→115）+ quotes.html +6 卡（96→102）+ index 计数 115 ×3 处（中英）
- 六条：e2015-12-02 COP21 索邦演讲 / e2018-09-17 BFR 环月旅客发布会 / e2019-04-22 Autonomy Day /
  e2022-09-30 AI Day 2022 / e2022-11-30 Neuralink Show and Tell / e2024-03-18 Starship Update at Starbase
- 采料：镜像 /agents/index?type=keynote（60 场）+ type=speech（21 场）全部 hasTranscript=100%；
  详情页 /video/{id} 正文为「说话人标签 + button 段落块」结构。
- 抽取器迭代（教训在案）：v1 逐词 span 非贪婪截断 → 乱序词流（弃）；
  v2 按 whitespace-pre-wrap 截断 → 同病（弃）；
  **v3 按 button 块整体剥标签保词序（tools/v9r07-fetch-keynotes3.py，定稿）**。
  教训：抽前必须先目检 DOM 实构，不能凭列表页经验假设结构。
- Musk 段词数：COP21 1,632 / BFR 3,204 / Autonomy 8,270 / AI Day 2022 6,458 / Neuralink 4,716 / Starbase 7,117。
- 甄别（详见 EXPANSION.md R07 块）：AI Day 2021 官方逐字在档（555 词独白）但 e2021-08 已有媒体口径条目，
  不重复立条留档；Starship 2025-05-29（4,836 词）入候选池；Wisconsin town hall（12,095 词）政治类不立；
  SpaceX IPO 敲钟 9 词不立；ASR 口径（Yusaku→Usage / Falcon→Belkin / neural link 分词）卡内注明。
- e2024-03-18 日期口径：镜像归档锚 03-18 与内容指向（IFT-3 03-14 前夜展望）矛盾，照录归档锚、卡内双注。
- 管线：build-ledger-timeline（115 节点）/ build-search-index（断言 109→115，索引 271→277）/
  sync-changelog（196 条）/ 版本三件套 8.7.0（14 页 span 打印在案）/ build-epub（219,675 B，24 章）。
- 验证：verify.py 9/9；node --check 通过；**CDP 探针 42/42**（tools/v9r07-probe.js：
  文件级 9 / 桌面结构与逐字 19 / 互链与锚 7 / quotes 3 / index 计数 2 / 检索 4 / 390 零溢出 3）。
- 探针插曲：第 2 轮跑 24/18 —— 新 profile 冷加载 1.8s 未完成（ps-row=0，空数组 every() 恒真造成
  Permalink 假绿）+ 当时疑有孤儿实例（targets=5）；处理=清理脚本（v9r07-kill-chrome.ps1，
  PowerShell 内联 $_ 被 bash 吞须写 .ps1——记忆坑复验）+ 端口 9340→9341 + ps-row 等待加固（轮询至 115），
  第 3 轮 42/42 全绿。**后续轮探针应在导航后轮询关键计数而非定值 sleep。**
- 证据：qa/v9-20/round-07/（probe.txt + 8 张截图：before 双视口=worktree@c556a2c 经 8767 独立服务，
  after 四条新卡桌面定位 + quotes 卡区 + Neuralink 390；sources/ 九件：keynotes/speeches 全清单 JSON、
  六场 transcript txt+joined、selected-sources.tsv 官方 YouTube 源、page-html 原始档）。
- 提交：成果 = 本提交；账本回填+revisions+EPUB 重刷为第二提交。
