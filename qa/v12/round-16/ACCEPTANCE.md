# V12-20 R16 验收 · 美术·正文杂志版式（v11.17.0）

日期：2026-10-07 · 模式：纯本地（无 push/remote 写）

## 成果（纯 CSS 零 HTML，style.css +1.8KB）
1. **drop cap 首字下沉**：.lr-main > section.lr-sec:first-of-type > p:first-of-type::first-letter——衬线 3.1em float 下沉+line-height 0.86 网格对齐+small-caps+主题色；**390 降级**为加粗首字（float:none，防溢出）。::first-letter 对中英双文种皆效（en 衬线形态由 var(--serif) 承载；zh 网格对齐由 line-height/padding 微调承载——单形双用的实现口径如实记录）。
2. **引语块题花三族统一**：.lr-sec blockquote / .sv-node blockquote / .pv-case blockquote——大引号 ::before（U+201C，2.6em serif，45% 透明）+正文左移 30px+实线竖 border-left 3px。
3. **边注分野强化**：.lr-note 保持虚线框+纸底（与引语实线竖+大引号形成体例分野）；基线 **--fs-body 16.5px 锁定**（探针 computed 断言）、段距 10px→12px。
4. **print 媒体模拟**：题花 content:none+首字降级（关影/关题花截图 desktop-dd05-print.png）；**reduced-motion** 显式压平。

## 验证
- **CDP 探针 18/18**：文件级 5/drop cap 3（float/字号>45px/衬线）/题花 2/边注分野 1/基线锁定 1/sv-node+pv-case 覆盖 2/390 降级+零溢出 2/print 关题花 1/reduced-motion 1。
- QA 截图 3 张：desktop-dd05-dropcap.png / desktop-dd05-print.png（print 模拟）/ mobile-390-dd05.png。
- verify.py 9/9（版本一致性 11.17.0，58 span 无残留）。

## 工程记录（如实）
- 题花正文左移（margin-left 30px）被既有 `.lr-quote .lr-quote-zh { margin: 8px 0 0 }` 高特异性规则压制——将其并入选择器组提优先级后过（探针首跑 17/1 修正）。
- en/zh 双语两形态的实现口径：页面 lang=zh-CN 且段落无 per-paragraph lang 属性，CSS 无法按内容文种分支——单形双用（::first-letter 对双文种天然生效），双形态以「衬线承载 en/网格对齐承载 zh」如实注记。

## 版本
- 11.16.0 → 11.17.0（58 span，通用 bump 无残留）。
