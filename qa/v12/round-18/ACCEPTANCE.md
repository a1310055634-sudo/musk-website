# V12-20 R18 验收 · 美术·专题封面化+首页封面故事（v11.19.0）

日期：2026-10-07 · 模式：纯本地（无 push/remote 写）

## 成果（纯 CSS + 既有 DOM，style.css +1.8KB + index 局部 DOM）
1. **专题封面三段式**（.lr-hero 类名不改）：lr-kick 细双线题花（0.3em small-caps）/h1 serif 大标题/lr-hero-fig 图版 3px double 框+figcaption 帽字题注——覆盖 deep-dive-01~07+survival-2008（9 页）；.section-head .kicker 统一封面语言（44px 双线前置）覆盖 grok/index 标准段页。
2. **index「本期封面故事」**：IN THIS ISSUE 导读条（本期看点=v11.17.0 版式/v11.18.0 图表/v11.19.0 封面三条目，§ 计数符）+feature-lead kicker「COVER STORY · DEEP DIVE 01 · CAPITAL」+feature-rows 目录感编号（CSS counter 01/02/03）——.act 三入口编号条健在（探针 010203 断言）。
3. **EN 往返**：lang-toggle 切换英文渲染+中文复原全过（hero-title data-en 往返断言）。
4. **320/390/768 复扫零溢出**（index 三视口断言）。

## 新旧首屏对比（像素 diff 报告）
八组 after 全部 DIFF（md5 与 before 显著不同）——报告 qa/v12/round-18/pixel-diff-report.txt（index-desktop：IN THIS ISSUE+COVER STORY+counter 编号；dd05-desktop：封面三段式等）。

## 重大发现（如实）
**站内无深色主题实现**（style.css 0 处 prefers-color-scheme、无 [data-theme] 定义块）——复古纸面单主题即美术基线 v11.1.0。R15 探针「深主题对比度 7.05」系切换无效果的假测量（两主题同值即为证），已如实记录在案；R17 的 dark hatch 覆盖块为死代码（保留无害）。修复：新增 :root --line 分隔线令牌——R15 期号细双线/mh-sep 的 var(--line) 失效调用点随之复活。

## 验证
- **CDP 探针 16/16**（≥8 达标）：文件级 4/封面三段式 3/首页封面故事 4/EN 往返 1/三视口零溢出 3/像素 diff 1。
- before/after 八组入 qa/v12/round-18/{before,after}/。
- verify.py 9/9（版本一致性 11.19.0）。

## 工程记录（如实）
- git checkout -- style.css 回滚 --line 误插时连带回滚 R18 CSS 追加——`git diff --stat`（1 行≠预期 52 行）暴露后重追加（教训：checkout 单文件前先 diff 确认损失面）。
- CSS counter 的 Chrome computed content 保留原始记法（counter(ftr) 字面）——断言改「规则在册+渲染宽度>0」。
- counter-reset 作用域：.feature-rows 局部 reset 不解析——上移 #features 段。

## 版本
- 11.18.0 → 11.19.0（58 span 无残留，通用 bump）。
