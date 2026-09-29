# V7-19 R18 QA 验收记录 — 动效、无障碍与性能（v6.23.0）

日期：2026-09-30 · 分支 visual-v7-19rounds · 探针 qa/v7-19/round-18/r18-probe.js（可复跑）

## 本轮要解决的问题

计划第 18 轮：统一按钮、章节、筛选、关系图和详情的动效；检查键盘顺序、焦点可见性、弹层焦点恢复和对比度；检查减少动态模式；优化图片、脚本、字体加载及布局稳定性；使用当前可用工具实际测量性能。

## 审计与实测结果（如实记录）

**静态审计（修复前基线已达标项）**
- reduced-motion：style.css 13 处 @media 块覆盖全部组件层（lr/cap/gx/sv/cf/pv 等）+ app.js 56 行显式 matchMedia 处理——reduce 时 reveal 全部立即 is-visible；
- 图片布局稳定性：全站 20/20 img 均有 width/height；加载策略正确（首页肖像 fetchpriority="high" 首屏优先，其余 19 张 loading 懒加载）；
- 焦点样式：style.css :focus/:focus-visible 规则 19 处；
- 对比度：--muted #5b5850 对 --paper、--mist 对 --coal（注释既有计算，本轮 CDP 实测复核）。

**动态实测（CDP 真实按键与模拟）——12/12 全过**
1. 性能实测（条件：本机 headless Chrome + 127.0.0.1 静态服务器、无网络延迟，数据为本地条件实测，非真实网络分数）：index/survival-2008/timeline/primary/search 五页 load 全部 <1500ms；首页最大资源 x-hq.jpg 196KB、tesla-factory.jpg 133KB、style.css 108KB（明细 perf-log.txt）；
2. reduced-motion 模拟：reveal 全部立即可见、首屏标题不依赖动画；
3. 键盘焦点：CDP Input.dispatchKeyEvent 真实 Tab 按键 8 次逐个进入可交互元素（合成 KeyboardEvent 不触发真实焦点移动——审计方法修正为真实按键）；:focus 规则在册；
4. 对比度实测：浅底次级文字 ≥4.5、深底文字 ≥4.5（WCAG AA 达标）；
5. Esc 焦点恢复回归：资本流向图 Enter 开详情 → Esc 焦点归还图本体（R10 机制回归正常）。

**本轮实际改动**
- app.js/cite.js 全站 36 页挂载点加 defer（解析不阻塞；执行顺序保持）；changelog.html 无脚本引用为历史合理现状（静态日志页）；
- 审计期间修探针自身问题 3 处（结构顺序/CDP API 更名 clearEmulatedMedia→setEmulatedMedia 空参/合成按键改真实按键）——站点零缺陷，此前 17 轮的无障碍与性能基础良好。

## 验收条件逐项

- 动效关闭后功能与内容完整 ✓（reduced-motion 模拟：reveal 全显、正文完整）
- 正文不依赖动画成功才显示 ✓（html.js 降级 + app.js reduceMotion 分支）
- 图片有尺寸，加载时不出现明显跳动 ✓（20/20 width/height + 加载策略正确）
- 不编造性能分数；记录实测条件和结果 ✓（本地条件如实标注，perf-log.txt 留档）

## 结论

**本轮完成。** 无新增事实；四项验收全部达成；实测数据留档。

## 证据清单（本目录）

perf-log.txt / QA.md / r18-probe.js
