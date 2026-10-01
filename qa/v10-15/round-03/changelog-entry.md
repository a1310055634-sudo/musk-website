## v10.3.0 — 2026-10-02 · V10-15 N03/15：口径审计＋引语复核声明上站

**主题包成果（V10-15 N03 · 核实主线收口）**
- **snowflake 全量对表**：X 帖 22 条有 id 者 `(id>>22)+1288834974657` 解码 UTC 与卡内日期 **22/22 全 match**、UTC 口径注零缺失（9 条无 id 卡注明立条口径）。
- **人工抽样**：财报会来源抽 2 条（Q3 2017「地狱刻度 level 9→8」/ Q4 2015「Model 3 下月发布」）对 stockanalysis 逐字稿（23967/23975）——**2/2 逐字吻合**。
- **未覆盖逐条清单**：N02 待人工 101 块逐条归因落盘 unmatched-itemized.tsv（other-official 73 / earnings-call 20 / edgar 6 / jre 1 / ted 1——原因=非镜像源无本地 transcript+Cloudflare 拦批量机核；立条时均经逐字源核实）。
- **双语对齐探针**：quotes 103 卡中 100 卡 EN/ZH 双语齐备（enOnly=0）；primary 抽样 20 行含引文块者 100% 配译文，2 行无引语为 SolarCity 两案（无本人逐字引语，如实设计）——探针首跑误报 2 行经结构甄别后校准口径。
- **「引语复核声明」上站**：primary.html + quotes.html 双语声明（id=quote-review-statement）——措辞如实三层：镜像来源已逐字机核 / 财报会人工抽样 2/2 吻合 / 未覆盖条目逐条注明原因（立条时均经逐字源核实）。满足纪律 D「未覆盖项逐条注明原因」门槛。
- numbers 交叉抽核：「1 万亿」市值口径 numbers 与 primary 双页同现一致。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 318）；CDP 探针 tools/v10n03-probe.js 6/6（双语对齐+声明双语切换+在册）；版本三件套 10.2.0→10.3.0（15 span；bump 正则前滚机制落地）；EPUB 重跑（223,463 B）。本轮仅本地提交，不推送。

