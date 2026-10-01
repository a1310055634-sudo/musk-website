# V9-20 R20 验收记录 · 全站验收＋待发布清单（v10.0.0 收官）

日期：2026-10-02（定时任务第三次触发，锁 run=V10PLAN-R20）

## 口径总核对（收官口径，入账本）

| 项 | 值 |
|---|---|
| 页面 | 38（含 resources；revisions.html 为 noindex 机器页，不入 sitemap → sitemap 37 URL） |
| 账本/文档/访谈/X 帖 | 115 / 18 / 42 / 31 |
| 语录卡 | 103（账本引文块 105 = 103 + 豁免 2） |
| 事件档案 | 14 档 59 材料（口径闭环探针在册） |
| 资源 | 36（官方 10 / 开源 9 / 社区 11 / 工具 6，以 resources-data.py 为准） |
| 检索索引 | 318 = 115+18+42+31+5+53+4+14+36 |
| 版本 | 10.0.0（三件套 15 span 一致） |

## 终验结果

| 项 | 结果 |
|---|---|
| 生成器全家桶 | ✓ 10 项幂等（九项原有 + 新增 build-sitemap.py 纳入全家桶） |
| verify.py | ✓ 9/9（38 页 / 索引 318） |
| CDP 全站终检 tools/v9r20-probe.js（端口 9381） | ✓ **15/15**：口径 3 / 主路径六步（index 封面+版本/quotes 103/primary 115/timeline 泳道/events 14/search 命中）/双语切换/资源页 36 卡+筛选/file:// 离线（渲染+导航）/38 页×3 视口 114 组合零横向溢出/print 抽查 |
| sitemap | ✓ 37 URL 新建（lastmod 2026-10-02，含 resources） |
| DEVLOG | ✓ 「〇-bis V9-20 交接要点」追加（三十轮成果地图/已知限制/续作指南） |
| 版本三件套 | ✓ 9.9.0→10.0.0（15 span）；bump 派生三处核对红线再次生效（OLD 误换被拦截） |
| sync-changelog / EPUB | ✓ 209 条 / 223,159 B |

## 交付物

- **RELEASE-CHECKLIST-v10.md**（待发布清单，不推送）：范围 `24020fe..HEAD`（41 个提交）、一条推送命令、Pages 五步验证、已知事项。
- **V10-15-PROGRESS.md**：后半段计划账本（N01–N15，v10.1.0→v11.0.0），本计划不停轮衔接。
- .gitignore 补 .v10run.lock。
- 工具脚本：tools/v9r20-probe.js / v9r20-bump.py / build-sitemap.py。

## 提交

- 成果提交：`[V9-20 R20]`（本地，不推送）。
- 第二提交：账本收官回填 + build-revisions + EPUB 重刷。
