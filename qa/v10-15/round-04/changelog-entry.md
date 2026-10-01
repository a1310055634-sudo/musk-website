## v10.4.0 — 2026-10-02 · V10-15 N04/15：资源核活复测＋元数据升级（36 条刷新）

**主题包成果（V10-15 N04 · 核实主线收口）**
- **36 条全量复测**：复用 N01 同日直连/api 结果（零死链）+ GitHub api 串行刷新 8 条——stars 漂移 4 条同步（vehicle-command 705→706 / teslamate 9061→9065 且 pushed 进入 2026-10 / grok-1 52239→52233 / SpaceX-API 10912→10913）；**36 条 checked 全刷 2026-10-02**；resources.html 重建（核活 2026-10-02）。
- **弃收件重验**：tesla.com 专利博文服务端读取器重试仍 Akamai 拦截、SAE J3400 仍 JS 壳——双双维持留档（EXPANSION N04 注记，重验条件不变）；Swisher/JMIR 维持留档。
- **工程**：tools/v10n04-recheck.py（N01 结果复用+api 刷新）/ v10n04-apply.py（checked 批量+gh 逐条精确替换带断言）；recheck.json/tsv 落盘 qa/v10-15/round-04/。

**质量门**
- validate() 过（36 条四类计数不变）；verify.py 9 项全绿；版本三件套 10.3.0→10.4.0（bump 正则前滚直接命中——N03 机制生效）；EPUB 重跑。本轮仅本地提交，不推送。

