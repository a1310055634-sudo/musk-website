# V12-20 R15 验收 · 美术·报头刊头体系（v11.16.0）

日期：2026-10-07 · 模式：纯本地（无 push/remote 写）

## 成果（四动作）
1. **Vol./No. 期号**：Vol. XI（主版本罗马数字）· No. <span class="site-version-val">11.16.0</span>——VERSION 同源 span，bump 自动覆盖，与页脚版本戳/期号三方一致（探针断言）。
2. **日期线**：构建日北京时间「2026 年 10 月 7 日」+data-en 英文对称（October 7, 2026）——site-nav 生成时写入（幂等重注入自动更新）。
3. **eyebrow 体系**：masthead-eyebrow 容器（em-dash 分隔+letter-spacing 0.22em 小帽字 dateline+0.18em issue+0.14em volno 细双线左缘）。
4. **章节开篇题花（纯 CSS）**：.cy-co/.fn-co/.ct-ch/.lr-sec 四族 h2 统一 3px double 细双线+0.05em 字距。

**纪律**：改刊头只动 site-nav.py 模板+style.css 组件层，41/41 全站重注入，零逐页手改。

## 对比度（任务书双主题 ≥4.5）
mh-volno：浅主题 **7.05** / 深主题 **7.05**（CDP computed-style 实算，含 α 背景上溯）。

## before/after
四页样本（index/survival-2008/timeline/capital-evolution）×双视口（1440/390）=**八组**，取景 masthead 原生入画——qa/v12/round-15/before/（改动前）与 after/（改动后）各 8 张。

## 验证
- **CDP 探针 14/14**（任务书 ≥6 达标）：期号 span 同源/期号文本=Vol. XI · No. 11.16.0/页脚同值/日期线中文渲染/eyebrow letter-spacing 实测>1px/浅深双主题对比度 7.05×2/三视口（1440/768/390）零溢出/reduced-motion。
- verify.py 9/9（版本一致性 11.16.0 含 58 span 全量校验）。

## span 口径演进（如实）
刊头期号 span 上墙后全站 site-version-val=58（41 刊头+17 存量，随页数增长）——bump 改通用版 tools/v12r15-bump.py（argv 传 OLD/NEW+无残留断言），R16–R19 复用。

## 版本
- 11.15.0 → 11.16.0（58 span 无残留）。
