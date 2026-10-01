# V9-20 R18 验收记录 · 排版与阅读体验（v9.8.0）

日期：2026-10-02（定时任务 automation-3a82f550 首触发，锁 run=V10PLAN-R18）

## 成果（纯 CSS，style.css +30 行，DOM/HTML 零改动）

- **基线复核锁定**：--fs-body 16.5px（16–18 ✓）/ --read-width 720px（640–760 ✓）＝R15 定值，探针 computed 断言锁定。
- **数字等宽**：文字层 12 选择器 tabular-nums（lr 正文/引语/编者注/来源/meta/数据框 + ps 引语/译文/事实/日期/来源/计数）；数据表 .lr-data .num 改 --font-num（deep-dive-01 实测 Consolas 系生效）。
- **引语/编者注三重区分**：引语=实底+5px 实线+--shadow-1+加宽内衬；编者注=纸底+虚线框。覆盖三族引语容器（.lr-quote / .sv-node blockquote / .pv-case blockquote）。
- **EN**：行高 1.92→1.78（引语 1.75）+ overflow-wrap 换行保护，中文不变。
- **print**：引语影显式关闭，CDP 媒体模拟实测 none。

## 验证

| 项 | 结果 |
|---|---|
| verify.py | ✓ 9/9（38 页 / 索引 318） |
| CDP 探针 tools/v9r18-probe.js（端口 9371） | ✓ **28/28**：文件级 6 / survival 排版 7（含 EN 切换往返 1.78↔1.92）/ deep-dive .num 1 / primary 账本 2 / print 模拟 1 / 三视口九宫格 12 |
| before/after | 九组四页样本：survival 三组差异可辨（md5 不同，本轮唯一含 lr 元素的样本页）；index/timeline/capital 六组逐像素一致＝改动面不含 lr/ps 元素，属预期并如实注明 |
| 版本三件套 | ✓ 9.7.0→9.8.0，15 页 span；build-resources 以 9.8.0 重建（36 条） |
| sync-changelog / EPUB | ✓ 207 条 / 223,159 B · 24 章 |

## 探针修正记录（页面正确，探针/首版 CSS 各一处）

1. **首版 CSS 漏覆盖**：survival-2008 引语实为裸 `blockquote`（.sv-node 内，无 .lr-quote 类）——首版只强化 .lr-quote 被探针捕获（no lr-quote→定位到 .sv-node blockquote 规则 1798 行），修正为三族容器同覆盖。
2. print API：`Emulation.setEmulatedMediaType` 在本机 Chrome 不存在，改旧版 `Emulation.setEmulatedMedia {media:'print'}` 成功。

## 产物

- qa/v9-20/round-18/：before/after 各 9 张（四页样本 8 + survival 引语特写 1 对）。
- 工具脚本：tools/v9r18-probe.js / v9r18-bump.py（截图复用 v9r17-shot.js）。

## 提交

- 成果提交：`[V9-20 R18]`（本地，不推送）。
- 第二提交：账本回填 + build-revisions + EPUB 重刷。
