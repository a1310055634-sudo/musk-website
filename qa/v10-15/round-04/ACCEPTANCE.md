# V10-15 N04 验收记录 · 资源核活复测＋元数据升级（v10.4.0）

日期：2026-10-02（定时任务第七次触发，锁 run=V10-15-N04）

## 成果

- **36 条全量复测**：复用 N01 同日结果（零死链）+ GitHub api 串行刷新 8 条全 200——**零死链**；stars 漂移 4 条同步写回（vehicle-command 705→706 / teslamate 9061→9065+pushed 2026-09→2026-10 / grok-1 52239→52233 / SpaceX-API 10912→10913）；**36 条 checked 全刷 2026-10-02**；resources.html 重建（页脚核活日期 2026-10-02）。
- **弃收件重验**：tesla.com 专利博文（服务端读取器重试仍 Akamai 拦）与 SAE J3400（仍 JS 壳）双双维持留档；Swisher 2018/JMIR 维持留档——EXPANSION N04 注记，重验条件不变。
- **validate() 过**：36 条 {official 10, opensource 9, community 11, tools 6} 计数不变。

## 验证

| 项 | 结果 |
|---|---|
| resources-data.py validate() | ✓ 36 条 |
| build-resources.py | ✓ 36 条 · 8 条 GitHub 实测 · 核活 2026-10-02 |
| verify.py | ✓ 9/9（38 页 / 索引 318） |
| 版本三件套 | ✓ 10.3.0→10.4.0（15 span；正则「运行匹配当前值→跑→前滚到 NEW」三步法首次完整执行） |

## 产物

- qa/v10-15/round-04/：recheck.json/tsv（36 条复测+gh 刷新表）/ ACCEPTANCE.md。
- 脚本：tools/v10n04-recheck.py / v10n04-apply.py / v10n04-bump.py。

## 提交

- 成果提交：`[V10-15 N04]`（本地，不推送）。
- 第二提交：账本回填 + build-revisions + EPUB 重刷。
