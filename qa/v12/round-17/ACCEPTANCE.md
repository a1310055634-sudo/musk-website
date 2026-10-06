# V12-20 R17 验收 · 美术·图表复古化（v11.18.0）

日期：2026-10-07 · 模式：纯本地（无 push/remote 写）

## 成果（纯 CSS，style.css +0.9KB）
1. **hatch 纹理**：gx-board/cap-graphwrap/net-graphwrap 图底 45° 斜纹——浅主题纸棕单色阶 rgba(139,109,31,.055)、深主题朱红低透明 rgba(200,64,50,.07)；print 关闭。
2. **双色纪律**：单色阶底+朱红强调只在装饰层——公司色标与 etype 色零触碰。
3. **形状语言不动**：V9-R17 etype 圆方菱三角规则零触碰（探针类名断言）；图例刻度等宽深化（cap-lg/gx-tchip/net-elabel tabular-nums）。
4. **口径注保留**：cap-legend「线宽按金额对数标度（示意）」「金额未入册（不编造）」原文在页。

## 数据编码不动（探针实证）
- **cap-ribbon 线宽 attribute=生成器值**：≥5 条、≥3 档互异（对数标定在）——探针断言。
- **390 清单形态逐像素一致**：capital-evolution/companies 两页 390 截图 **md5 与 before 完全相等**（cap/net 移动端图表隐藏，清单形态零接触）——回归证据。

## before/after 六组
三页（timeline/capital-evolution/companies）×双视口（1440/390）——qa/v12/round-17/{before,after}/ 各 6 张。

## 验证
- **CDP 探针 13/13**（≥6 达标）：文件级 3/hatch computed×3/ribbon 线宽/口径注/形状类名/图例等宽/390 md5×2/reduced-motion。
- verify.py 9/9（版本一致性 11.18.0）。

## 工程记录（如实）
- 探针首查 .cap-flow 为交互 g 层（computed 1px 恒定）——可见 ribbon=.cap-ribbon（stroke-width attribute=生成器值）；cap-lg 等宽断言曾跑错页（timeline 无该元素）——时序修正后 13/13。

## 版本
- 11.17.0 → 11.18.0（58 span 无残留，通用 bump）。
