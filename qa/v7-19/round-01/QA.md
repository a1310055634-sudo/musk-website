# 第 1 轮验收记录 · 视觉基础与基线（V7-19 R01）

日期：2026-09-29 · 分支：visual-v7-19rounds · 目标版本：v6.6.0

## 本轮要解决的问题

建立 V7「深色纪实封面 + 暖白长文阅读 + 朱红强调」的统一设计基础（色彩/字体层级/间距/栅格/按钮/边框/焦点），清理影响新设计的硬编码旧色与重复规则，并把基础实际应用到首页与一篇长文；保存改版前后证据。

## 实际完成的改动

1. **改版前基线证据**：`qa/v7-19/round-01/before/`（index/reading/timeline/companies/search × 1440×900 + 390×844，共 10 张）。
2. **色彩令牌归一化**（tools/v7r1-normalize-colors.py，共 839 处 + build-revisions.py 模板 14 处）：
   - 全部 32 页 + style.css + app.js 的硬编码 `#7c2d2d/#faf9f6/#1a1a1a/#5c574e` 统一为 CSS 变量（SVG 属性、内嵌 JS、favicon、theme-color 用新十六进制直换）；
   - 同步更新 build-revisions.py 生成模板，避免重建时旧色回退。
3. **V7 令牌基础层**（style.css `:root` 重写）：
   - 色彩：暖白 `--paper #F3F0E8`、近黑 `--coal #101316`（本轮定义，第 3 轮封面启用）、墨色 `--ink #17191d`、次级 `--muted #5b5850`（对比度≈6.3:1）、朱红 `--accent #C84032`、小号强调文字 `--accent-text #A63628`（对比度≈5.8:1）；
   - 字号层级令牌：`--fs-hero`（88–144px，第 3 轮启用）/ `--fs-h1/h2/lead/body/small/micro`；
   - 间距标尺 `--space-1..8`、阅读宽度 `--read-width 720px`（640–760 区间）、动效 `--t-fast 180ms / --t-med 320ms`；
   - 新增深色面上的焦点样式（outline 用纸色）。
4. **基础可见应用**：
   - 全站：报头 3px 朱红顶条；主按钮 `.btn-ink` 改朱红填充；kicker 前导红短线；12 处小号强调文字改 `--accent-text` 保对比度；
   - 首页：封面标题刻度提升（clamp 48–104px、行高 1.05）、导语用 `--fs-lead`；
   - 长文（reading.html）：正文 15px→16.5px（进入 16–18px 规范区间）、行高 2.0→1.9、导语 15.5px、阅读宽度令牌化、强调色对比度修正。
5. **重复基础规则清理**：删除文件尾与前一 print 块完全重复的规则；`:root` 循环引用风险（归一化副作用）当场发现并随令牌块重写消除。

## 检查了哪些页面和交互

- 截图对比（before/after 各 10 张 + primary 补拍）：index、reading、timeline、companies、search、primary；
- 交互（IAB 实测）：中英切换（标题/按钮/`<html lang>`/导航均正确往返）、手机菜单开合（390px：开 flex/aria-expanded=true、Esc 关闭）、
- 回归：verify.py 9 项（8 绿 + EPUB 新鲜度待终建）、`node --check app.js` 通过。

## 测试结果与发现的问题

- 桌面与手机、中英双语下新基础清晰可辨：朱红顶条/主按钮/kicker 短线、暖白纸底；
- 时间轴泳道公司色（藏蓝/朱红/黑/金）、筛选胶囊、深色资料卡不受影响；
- 发现并处理：
  1. headless 截图偶发图片解码竞态（手机端肖像白框一次）→ 截图协议加 `--virtual-time-budget=6000` 并复拍确认正常；
  2. IAB 物理点击 lang-toggle 超时（elementFromPoint 证明无遮挡，为环境怪癖）→ 改用页面内事件派发验证，逻辑正确；
  3. 归一化一度把 `:root` 定义值替换成自引用 var()（会使全部令牌失效）→ 立即整体重写为 V7 令牌块，终检无残留。

## 是否完成本轮

**完成**。旧链接/锚点未动（verify 断链检查绿）；原有功能（双语、菜单、筛选、检索、时间轴）回归通过。

## 截图协议（后续轮次沿用）

`python tools/qa-shots.py <outdir>`：headless Chrome `--force-prefers-reduced-motion --virtual-time-budget=6000`，5 代表页 × 桌面 1440×900 / 手机 390×844。
