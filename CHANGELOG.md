# 更新日志 · CHANGELOG

> 每个定时周期追加一条。格式：版本 — 日期 · 主题（主题包成果 + 自主优化）。

## v11.18.0 — 2026-10-07 · V12-20 R17 · 美术·图表复古化（美术四轮 III · 纯 CSS）

**主题包成果（V12 R17 · 美术轮）**
- **①hatch 纹理**：gx-board/cap-graphwrap/net-graphwrap 三图图底 repeating-linear-gradient 45° 斜纹——浅主题纸棕单色阶 rgba(139,109,31,.055)/深主题朱红低透明 rgba(200,64,50,.07)（双主题双配色）；print 关闭。
- **②双色纪律**：单色阶底+朱红强调只在非数据装饰层——公司色标（#C84032 等）与 etype 色零触碰。
- **③形状语言/图例深化**：etype 节点形状（V9-R17 圆方菱三角）原规则零触碰（探针类名断言）；图例刻度等宽字深化（cap-lg/.gx-tchip/.net-elabel tabular-nums+0.02em 字距）。
- **④口径注保留**：「线宽按金额对数标度（示意）」「金额未入册（不编造）」原文在页（探针断言）。
- **数据编码不动（探针实证）**：cap-ribbon 线宽 attribute=生成器值（≥5 条 ≥3 档互异→对数标定在）；**390 清单形态逐像素一致**——capital-evolution/companies 两页 390 截图 md5 与 before 完全相等（cap/net 移动端图表隐藏零接触）。
- **before/after 六组**：三页×双视口入 qa/v12/round-17/{before,after}/。
- **CDP 探针 13/13**（≥6 达标）。
- **版本三件套**：11.17.0 → 11.18.0（58 span 无残留）。

## v11.17.0 — 2026-10-07 · V12-20 R16 · 美术·正文杂志版式（美术四轮 II · 纯 CSS 零 HTML）

**主题包成果（V12 R16 · 美术轮）**
- **①drop cap 首字下沉**：lr-* 长文首段 ::first-letter（衬线 3.1em float 下沉+small-caps+主题色）——::first-letter 对中英双文种皆效（中文网格对齐 line-height 0.86）；**390 降级**为加粗首字（float:none 防溢出）。
- **②引语块题花三族统一**：.lr-sec blockquote/.sv-node blockquote/.pv-case blockquote——大引号 ::before 装饰（“ 2.6em serif 45% 透明）+正文左移 30px+实线竖 border-left 3px；与③边注（.lr-note 虚线框+纸底）视觉分野强化。
- **④基线锁定**：--fs-body 16.5px 不动（探针 computed 断言），段距 10px→12px 呼吸。
- **print 媒体模拟**：题花 content:none+首字降级（关影/关题花截图入册）；reduced-motion 显式压平。
- **CDP 探针 18/18**（首字 float/字号/衬线/题花三族/边注分野/基线锁定/390 降级+零溢出/print 关题花/reduced-motion）。
- **工程记录**：题花正文左移被既有 .lr-quote .lr-quote-zh 高优先级 margin 压制——特异性补写（.lr-quote .lr-quote-zh 并入选择器组）后过。
- **版本三件套**：11.16.0 → 11.17.0（58 span，通用 bump 无残留校验）。

## v11.16.0 — 2026-10-07 · V12-20 R15 · 美术·报头刊头体系（美术四轮 I）

**主题包成果（V12 R15 · 美术轮）**
- **刊头三件套（site-nav.py 模板一次改动全站重注入 41/41，零逐页手改）**：①**Vol./No. 期号**——Vol. XI（主版本罗马数字）· No. <span class="site-version-val">（VERSION 同源 span，bump 自动覆盖）；②**日期线**——构建日北京时间「YYYY 年 M 月 D 日」+data-en 英文对称（October…）；③**eyebrow 体系**——masthead-eyebrow 容器（细 em-dash 分隔+小帽字大字距）。
- **章节开篇题花（纯 CSS）**：.cy-co/.fn-co/.ct-ch/.lr-sec 四族 h2 统一 3px double 细双线+letter-spacing 0.05em。
- **对比度实测**：mh-volno 浅主题 7.05 / 深主题 7.05（≥4.5 达标，CDP computed-style 实算）。
- **span 口径演进**：刊头期号 span 上墙后全站 site-version-val=58（41 刊头+17 存量，随页数增长）——bump 改通用版（argv 传版本+无残留断言），不再定死总数。
- **before/after**：四页样本（index/survival-2008/timeline/capital-evolution）×双视口=八组入 qa/v12/round-15/。
- **CDP 探针 14/14**（≥6 达标：期号同源/日期线双语/题花 CSS/eyebrow letter-spacing/双主题对比度/三视口零溢出/reduced-motion）。
- **版本三件套**：11.15.0 → 11.16.0（58 span 无残留校验）。

## v11.15.0 — 2026-10-07 · V12-20 R14 · 质量节点②：互链扩展 + 检索审计

**主题包成果（V12 R14 · 质量轮）**
- **互链路①资源↔档案**：companies 字段驱动自动增长核对——R13 新资源自动入对应公司档案资源行（Tesla 档含 tesla-support、SpaceX 档含 sec-edgar-spacex、xAI 档含 docs-xai/xai-org-github），事件联动 24≥20+（任务书 16→20+ 达标）。
- **互链路②三方共现扫描（tools/v12r14-xlinks.py）**：Neuralink 簇 7 候选+人工裁决 **6 对新增**——e2024-01-29 materials +3（e2019-07-16 弧线起点/i2024-01-29 同日访谈/i2019-11-12 五年前口径）+e2026-02-10 +1（i2026-07-23 Economist）+e2023-11 +1（i2026-02-05 Dwarkesh）+e2024-07 +1（e2025-11-06 股东会交汇点）；插入前锚点跨页 fetch 全验证。事件材料 89→95。
- **顺手修 bug**：e2025-03-28 档 external 条 href=None（历史遗留）→补镜像检索锚（先例同款）；其余 8 处 None 为历史档媒体占位体例如实保留（探针断言按档定位）。
- **检索审计**：抽 30 条验证——命中/高亮 <mark>/日期升序/类型过滤 aria-pressed/清除筛选恢复 413/aria-live=polite/URL ?q= 回填/**Ctrl+K 键盘流补齐**（search 页聚焦+全局跳转，输入态不劫持）/**noscript 降级提示补齐**；双语切换验证；390 双页零溢出。
- **CDP 探针 21/21**（任务书 ≥15 达标）。
- **版本三件套**：11.14.0 → 11.15.0（17 span）。

## v11.14.0 — 2026-10-07 · V12-20 R13 · 资源扩容：SpaceX EDGAR/官方与开源补（49→54）

**主题包成果（V12 R13 · 资源轮）**
- **RESOURCES +5 条（49→54，validate() 全过零绕过）**：①sec-edgar-spacex（official，200——SpaceX CIK 0001181412 上市后披露通道：10-Q/8-K/13G，同期链 S-1→424B4→notes→10-Q）；②docs-xai（official，200——Grok API 官方文档）；③tesla-support（official，**三路法第三路**：curl/WebFetch 403 拦、服务端读取器 200 实锤，同 xai-official 先例注记）；④xai-org-github（opensource，200——org 入口；grok-1 仓库 api.github.com 实测 52,236 stars/最近 push 2024-08）；⑤spacex-ir（tools，200——上市后投资者关系页）。
- **核活纪律**：每条 curl 实测记 http；403/000 按纪律不硬收（x.ai/models 超时弃、ownersmanual 403 弃）；候选 7 实收 5——宁缺毋滥（任务书 58± 以核活结果为准）。
- **采集方向完成度**：Grok API 官方文档 ✓/x.ai 官方页 ✓（xai-official 已在册）/开源权重 ✓（grok-1+org 页）/官方补强（tesla.com 支持 ✓、车主手册 403 弃）/Starlink 社区已足（starlink-grpc-tools/starlink-sx 已在册）。
- **检索索引 403→408→含资源 54：合计 408 不变**（资源断言动态 len(RD.RESOURCES)），verify n_res 动态同步。
- **版本三件套**：11.13.0 → 11.14.0（17 span）。

## v11.13.0 — 2026-10-07 · V12-20 R12 · 深读新篇 II：deep-dive-07《Robotaxi 落地考》（40 页）

**主题包成果（V12 R12 · 深读轮）**
- **择题**：Robotaxi 落地考开工（素材较政治主题更扎实：账本逐字×2+R02 四卡+事件档 7 材料）；**Musk 政治参与 2024–2026 连同已探明素材写 EXPANSION 候选池**（R10 事件档 e2024-07 正反并陈+三镜像帖 200 实测+178+ 帖池检索锚——素材已在册，待专属轮次展开）。
- **deep-dive-07.html《Robotaxi 落地考》**（18.3KB，逐字克隆 dd05 骨架）：五章——欠账的形状（2016–2024 承诺簇+promises 五案为何不设 robotaxi 案的核查发现）/We,Robot（Cybercab 逐字）/奥斯汀弧线（四帖逐字含 p2026-01-22 无监督员句）/一周年口径（e2026-07-22）/**指控·回应·本站核查三段体**（controversy 体例：两半都真、分别可核）。
- **promises 互链**：任务书条件句「若有 robotaxi 承诺条目则互链」——实测 promises.html 五案无 robotaxi 专属卡（0 命中），如实不造互链；以 s3 全览段互链+「制度性排除」作为核查发现写入正文。
- **七件接入**：site-nav 注册 41/41（五组 40 页）/索引深读长文 5→10（dd06+dd07 十章）/verify n_dd 正则扩展/新页含 span（17 处）/sitemap 未动/build-longread 幂等/互链 6 处 fetch 验证。
- **检索索引 403→408**；页数 39→40。
- **版本三件套**：11.12.0 → 11.13.0（17 span）。

## v11.12.0 — 2026-10-07 · V12-20 R11 · 编年史补齐 + 新页 deep-dive-06《xAI 三年志》（39 页）

**主题包成果（V12 R11 · 编年史+新页轮）**
- **chronicle.html 近年补齐 +11 条（53→64）**：tesla 段 7（Investor Day MP3/SolarCity 终审/Q3+Cybertruck 倒计时/We,Robot/Robotaxi 首发/万亿薪酬包 proxy/Optimus 产线）+spacex 段 2（Starbase 员工会/**SpaceX IPO 定价**）+x 段 2（DealBook 抵制回应/政治参与升级）——全部克隆页内 cy-year/cy-ev 结构、逐条带账本/文档/事件档深链；Neuralink 无对应公司段如实弃收录 EXPANSION。
- **新页 deep-dive-06.html《xAI 三年志》（39 页）**：逐字克隆 deep-dive-05 全部结构（head/lr-hero/五 lr-sec/lr-foot/TOC/进度条），内容为公司志读法——一句话章程/四个月出 Grok/收购 X/第一份成绩单/资本线与披露缺位，引语全部带一手锚。
- **七件接入**：①site-nav.py NAV_GROUPS 专题组注册+全站重注入（40/40）；②build-search-index.py 新类型「深读长文」五章入索引+编年史断言 53→64；③verify.py 锚点计数加 n_dd（同事件档案先例，页数 38→39 自动）；④新页含 site-version-val span——**站点 span 15→16**；⑤sitemap.xml 未动（R20 统一）；⑥build-longread 幂等跳过确认；⑦新页互链 7 处（账本×4/帖史×2/文档/事件档/grok 财务）全 fetch 验证。
- **检索索引 387→403**（编年史 +11、深读长文 +5）；三口径审计口径同步（页 DOM 64+索引 64+生成器 64）。
- **CDP 探针见 ACCEPTANCE**（新页渲染/双语/导航高亮 aria-current/390 零溢出/互链跨页存在）。
- **版本三件套**：11.11.0 → 11.12.0（16 span，bump 断言随新页更新）。

## v11.11.0 — 2026-10-07 · V12-20 R10 · 事件档案补档：2023–2026 四档（16→20）

**主题包成果（V12 R10 · 事件档案轮）**
- **EVENTS 追加四档（tools/events-data.py，etype 五类枚举内）**：①e2023-11 **Grok：从聊天玩具到操作系统层**（milestone/month——6 材料：xAI 成立账本/Grok-1 发布卡/Grok 4.8 卡/Moonshots 访谈/Series E 文档/grok 专题）；②e2025-06-22 **Robotaxi 落地**（milestone/day——7 材料：We,Robot 前史+一周年电话会+R02 四卡弧线+promises 欠账口径）；③e2026-07 **Optimus 量产线**（milestone/month——5 材料：Fremont 实拍/AI5 访谈/产线前史/财报互证/欠账卡）；④e2024-07 **政治参与与 America Party**（risk/month——**正反并陈**：他的立场原文口径+批评方立场并列，4 条 external 镜像帖材料含 single-party state 逐字引语与 178+ 帖池检索锚；R02 移交条款落地）。
- **口径红线等式闭环（探针断言）**：时间轴独立记录 309 + 吸收 58 + events.html 档案记录 20 = **索引 387**（事件档自身记录入索引后等式两侧同步 +4+1）。
- **材料深链全部预验证**：external 三镜像帖 HTTP 200 实测；站内锚（e2024-10-10/e2026-07-22/e2024-04-23/e2023-07-12/p2023-11-04/p2025-08-16/p2025-10-29/p2026-10-03/i2026-01-06/i2026-02-05/d2026-01/grok/promises-s3）跨页 fetch 断言存在。
- **CDP 探针 19/19**（端口 9356：等式/四档渲染/etype 徽标/正反并陈/深链抽查/external 渲染/390）。
- **工程记录**：①新档英文文案裸双引号连炸三处（"firsts"/"crossing…"/"whether…how fast" 等）——第一次批量修复脚本误伤历史档合法转义引号 18 行，git 单文件还原后弯引号重写一次通过；②no_quote_note 必须为 dict {zh,en}（render_event t() 取键），字符串形态直接 TypeError；③sed 链式自噬再现（v12r09 bump 为底本生成 v12r10 bump 双规则互吃）——bump 必须 Write 全新（红线第 N 次）。
- **版本三件套**：11.10.0 → 11.11.0（15 span 替换计数打印）。

## v11.10.0 — 2026-10-06 · V12-20 R09 · 质量节点①：第一手盘点总表 v3（三口径零漂移）

**主题包成果（V12 R09 · 质量盘点轮）**
- **三口径零漂移（脚本核对打印在案 tools/v12r09-audit.py）**：九类型「页面 DOM / 检索索引 / 生成器断言」三并列全 OK——账本 124/文档 37/访谈 51/X 帖 44/深读 5/编年史 53/财务 4/事件 16/资源 49，合计 383=383=383。
- **盘点总表 v3 入册（qa/v12/round-09/AUDIT-v3.md）**：R02–R08 增量对账（X 帖 34→44/账本 119→124/访谈 47→51/文档 27→37/引语三态 ✅15⚠️86❌0）+ 逐类型年份分布表——**X 帖 2018–2026 连续覆盖无断年（R02/R03 填补生效）**；访谈 2009–2012 四年空白=已知硬约束；文档 2011–2014/2019 空白；账本 **2003/2005/2007 三整年空白**=最大剩余缺口。
- **缺口清单 v4 写回 EXPANSION 卷首**（接替 v2/v3，九项全带重验条件）：访谈早期空白/文档 2019 可挖 SEC 批准令/账本 SpaceX 早期三空白年候选（F1 立项 2003/首静火 2005/Flight 2-3 2007）/⚠️85 续核+e2013-05-08 换锚/email 余 10 封/xAI 首披露/SpaceX 10-Q 富矿/documents 页脚/X 帖 2020 与账本 2011-2012 加密。
- **主路径探针 15/15 全过**（首页→账本→语录→检索→资源五页：版本戳 11.10.0×2/ps-row 124/qs-card 107/✓15◎83/检索索引 383/rs-item 49/页间链接连通/390 零溢出）。
- **版本三件套**：11.9.0 → 11.10.0（15 span 替换计数打印）。

## v11.9.0 — 2026-10-06 · V12-20 R08 · 引语核验质量轮：101 块三态结论 + 15 原文锚上卡

**主题包成果（V12 R08 · 质量轮）**
- **101 块非镜像来源引语逐条机核完成**（quotes-worklog.tsv 全 101 行 verdict+anchor_url 非空）：**✅ 原文核验 15**（镜像 /agents/search 精确短语命中 10——含 2 场 earnings call 镜像转录 e2018-08-01/e2023-10-18 与 Fork in the Road 邮件底本；EDGAR FTS 命中 3——e2016-07-20/e2018-08-07/e2018-09-29 备案原文；stockanalysis WebFetch 逐字吻合 2——e2016-02-10 Q4-2015/e2016-05-04 Q1-2016）；**⚠️ 转引在册 85**（原文逐字档本轮流管线未获，收录底源=卡注来源+账本条目双重一致，逐组注明原因：earnings-call 组 stockanalysis 转录底本+抽样吻合记录/EDGAR 组实为 SEC 起诉状与判词措辞/ted transcript JSON 无逐字吻合等）；**❌ 撤下 0**（无反证不撤）。
- **quotes.html 上屏**：✓ 15 卡附原文核验标（title 悬停显锚链接，a 嵌 a 规避=并入 qs-src 行尾+title 属性，零新 CSS 零新类）；◎ 83 卡转引标；页脚新增核验口径段（三态分布+底册路径）。107 卡总数不变——**语录卡 107=账本引文块 109−白名单豁免 2 恒等式保持**（e2021-07/e2025 两条账本块无语录卡，TSV 如实标注）。
- **抽样人工复核 10 条**：2 条 stockanalysis 逐字吻合+1 条口径不符如实记（e2013-05-08 该季逐字稿无此句，引语实为股东信口径——留待后续换锚）+镜像/EDGAR/专路各取样，记录入 qa/v12/round-08/SAMPLE-REVIEW.md。
- **核验底册**：qa/v12/round-08/（quotes-payload.json 101 条短语提取/mirror-edgar-results.json 机核原始结果/quotes-worklog-r08.tsv 定稿副本回填 R01 正册）。
- **版本三件套**：11.8.0 → 11.9.0（15 span 替换计数打印）。

## v11.8.0 — 2026-10-06 · V12-20 R07 · email 续 + 文档馆近年化：SpaceX IPO 锚 + 万亿薪酬包 proxy

**主题包成果（V12 R07 · 一手信息增量）**
- **重大发现：SpaceX 已上市（Nasdaq: SPCX）——站内此前零覆盖**。EDGAR 备案全链在档：S-1（2026-05-20）→ 8-A12B（06-10）→ **424B4 定价书（06-12，555,555,555 股 × $135.00，募资约 750 亿美元，A/B 双层 10:1 投票+受控公司豁免，募资用途首位=AI 算力基础设施）**→ senior notes 8-K 三连（06-22/23/26，五档 2031–2056 合计 250 亿美元）→ 10-Q（08-04）。立 **d2026-06-12**（424B4）与 **d2026-06-22**（notes 定价 8-K）两条。
- **Tesla 近年化两条**：d2025-09-17 **万亿薪酬包 proxy**（12 档市值里程碑 2 万亿→8.5 万亿+4000 亿 EBITDA 门槛，备案号 0001104659-25-090866，互链 e2025-11-06）；d2026-01-29 **10-K FY2025**（AI 写进公司定义句首段+Technoking 关键人风险句，备案号 0001628280-26-003952）。
- **email 续两条（双源）**：d2018-08-12 **PIF 鲁梅延短信**（"You are throwing me under the bus"——funding secured 证券集团诉讼披露展品+Fortune 2022-04-25 双源，互链 e2018-08-07）；d2022-03-26 **Dorsey 协议短信**（"A new platform is needed. It can't be a company."——Twitter v. Musk 法庭披露展品+danluu.com 披露件汇编双源，互链 e2022-03-26）。
- **xAI 披露**：EDGAR full-text search "xAI Holdings" 56 命中实为 SpaceX 相关文件（333-296740 注册号）；x.ai 关联实体多个 CIK 存在但无可立条披露文书——如实记 EXPANSION。
- **断言与生成器**：doc-article 31→37/索引 377→383/build-search-index 守护断言同步 37；集成断言两次拦截（口径戳全页计数=R06 4+R07 6=10，非 6）后一次通过。
- **版本三件套**：11.7.0 → 11.8.0（15 span 替换计数打印）。

## v11.7.0 — 2026-10-06 · V12-20 R06 · email 库双源核验 I：四封立条 + 镜像 SSR 直取管线打通

**主题包成果（V12 R06 · 一手信息增量）**
- **立条 4 封（文档馆 27→31）**：①d2022-04-20 **埃里森十亿美元承诺**（"A billion … or whatever you recommend"——Twitter v. Musk 法庭披露件+SEC 2022-05-05 备案双源，与账本 e2022-04-20 互证）；②d2022-11-09 **Twitter 首封全员信**（远程工作终结令——镜像+CNBC 全文双源）；③d2023-01 **"This is a bait and switch"**（马斯克致奥特曼——口径如实标注=2026 庭审宣誓作证当场追述，非原始短信档）；④d2023-02 **"You're my hero … it really fucking hurts"**（奥特曼致马斯克——2026-01 解封展品+Business Insider 逐字引用双源）。
- **管线突破：镜像 email 详情页 SSR 直取**——带浏览器 UA 的 curl 可拿完整 SSR HTML（26KB 级，此前裸 curl 只得 404 壳），正文在 RSC payload 内，tools/v12r06-extract.py 采料脚本入册；四封镜像存档 qa/v12/round-06/sources/。镜像页脚自带第二源链接（法庭展品/CNBC/hardresetmedia），双源核验链路完整。
- **归账**：Bret Taylor "take private offer" 私信=在册复用（e2022-04-09 现场段已覆盖对话），不新立；N09 留档清单 30 封中本次消化 5 封。
- **断言与生成器**：doc-article 27→31/索引断言一手文档 27→31=377 条/build-search-index 守护断言同步更新；CDP 探针 24/24（首跑 1 挂=documents.html 历史上无站点页脚版本戳，系断言写错非站点回归——该页页尾结构是定制 doc-foot，15 span 口径从未含它）；2022-04/2022-11/2023 三段时序邻居断言全过。
- **版本三件套**：11.6.0 → 11.7.0（15 span 替换计数打印）。

## v11.6.0 — 2026-10-06 · V12-20 R05 · 访谈消化轮：2026 访谈断代补齐 + 双降级重验

**主题包成果（V12 R05 · 一手信息增量）**
- **重大发现：访谈断代与 X 帖同源**——镜像 161 场与站内 47 场对照，2013+ 未收的 11 场**全部是 2026 年**（站内最新 2025-11-06）。本轮立 4 场（47→51）：i2026-01-06 Moonshots #220（「Grok 一直在更新」电路访谈）；i2026-01-22 **达沃斯与 Larry Fink**（「有史以来最大的飞行器」/Falcon 9 复用 500+ 次→星舰今年证明完全复用）；i2026-02-05 Dwarkesh（AI5 进 Optimus/边缘算力+电网错峰论）；i2026-07-23 **The Economist**（「数字智能与物理智能」两半论——SpaceX 招股书收入大头是 AI 之问的正面回答）。
- **双降级重验维持**：lex-438（Neuralink 专场）官方稿两 URL 404 维持「待外部逐字源」（并勘误：缺口清单 v2① 的 lex-438 指该专场，与站内已收的 #400 稿是两回事）；60-minutes-2012 CBS 页面 404 维持留档。
- **锚与查重**：四场逐字锚=镜像详情页 elonmuskarchive.org/video/{id}（161 场 hasTranscript 全量库，详情页 2.75MB 级全文剥标签抽词）；existing.json 查重清单存 qa/v12/round-05/；All-In 场详情页为列表壳、Bloomberg 场空壳——如实弃收留档。
- **断言与生成器**：iv-item 52（51 带 id+1 legacy）/blockquote 与 iv-zh 52 成对；索引断言 47→51=373 条；CDP 探针 18/18（首跑 1 挂=legacy 条目计数，修正后过）。
- **版本三件套**：11.5.0 → 11.6.0（15 span 替换计数打印）。

## v11.5.0 — 2026-10-06 · V12-20 R04 · 账本早期加密（2002–2010）

**主题包成果（V12 R04 · 一手信息增量）**
- **五条入账（119→124，全无引语节——语录卡计数不变）**：e2002-05 SpaceX 成立（424B4 官方陈述「since May 2002」）；e2004 Musk 任 Tesla 董事长（424B4「since April 2004」+Series A 领投）；e2008-12-23 **NASA CRS-1 合同 $1.6B/12 飞行**（SpaceX 翻生文书，圣诞夜融资前一日）；e2009-05-19 Daimler 战略投资（424B4 Blackstar Investco >5% 陈述+EDGAR Form D 2009-05-20 佐证）；e2010-05-20 Toyota/Fremont 合作（424B4 May 2010 原文段）。
- **锚全一手**：Tesla 424B4（2010-06-29 IPO 定价书，EDGAR Archives 直读）单文书覆盖五条中的四条；EDGAR submissions API 实证 **2004 Form D 不在 EDGAR**（归档自 2005-02 起——制度性缺失如实留档）；CRS-1 走 NASA 公告转存两源（Spaceflight Now/NASA Watch+OIG 2013 审计），NASA 原稿链接 404 已注记。
- **查重纠偏（任务书快照勘误）**：候选表里 Falcon 1 F4（e2008-09-28）/Tesla IPO（e2010-06-29）/Master Plan（e2006-08）**均已在册**；e2008-12-24 是圣诞夜融资而非 CRS-1（合同 12-23 披露）——实际增量按实测五条执行。
- **断言与生成器**：ps-row 124/ps-quote 115（不变）/时序局部邻居检查；索引断言 119→124=369 条；CDP 探针 20/20（data-en 属性断言——textContent 中文模式坑第三次实证）。
- **版本三件套**：11.4.0 → 11.5.0（15 span 替换计数打印）。

## v11.4.0 — 2026-10-06 · V12-20 R03 · X 帖早期加密 I（2018–2019）

**主题包成果（V12 R03 · 一手信息增量）**
- **四卡上墙（40→44，五帖两连发一卡×2）**：p2018-09-18 BFR 首段实体箭体（碳纤维时代——卡注如实写「两个月后 180° 转身不锈钢」伏笔，**逐字甄别纠错：该帖原文是 carbon fiber，网传"不锈钢首曝"不实**）；p2018-10-04 SEC「做空者致富委员会」typo 两连发（"Just want to that" 漏 say 原样保留+顺势补刀帖）；p2019-07-26 Starhopper 150 米成功「水塔*能*飞」（星号原样）；p2019-11-23 Cybertruck 146k 订单+零广告两连发（与大锤翻车卡成 48 小时翻盘弧线）。
- **查重与口径**：既有 2018×3/2019×3 卡逐张对照（funding secured 本尊 2018-08-07 已在，候选避让）；Bitcoin 购车三连发实为 2021-03-24 出局（留档 EXPANSION）；六帖 snowflake 解码与镜像 date 全吻合。
- **断言与生成器**：cards/permalink/text/zh=44×4、年份条 9；索引断言 40→44=364 条；CDP 探针 20/20（文件级 6/桌面 13/390 溢出 1，含 SEC 卡 typo 原样断言与 2019 组七卡卡序）。
- **版本三件套**：11.3.0 → 11.4.0（15 span 替换计数打印）。

## v11.3.0 — 2026-10-06 · V12-20 R02 · X 帖断代回捞 III（2025-08→2026-10 十五个月空白补齐）

**主题包成果（V12 R02 · 一手信息增量）**
- **六卡上墙（34→40）**：robotaxi 弧线四卡——p2025-08-16 服务面积超对手（断代窗首卡）/p2025-10-29 大奥斯汀全区开放/p2026-01-22 **车内无安全监督员**+Optimus「100X 于汽车」/p2026-10-03 运营延时 23 点+「灰色小猫」长尾场景（**本墙最新卡，回捞日前三天**）；Optimus p2026-07-01 弗里蒙特产线实拍（t.co 图链不入正文，站内先例）；Grok p2026-09-14 Grok 4.8 技术规格首曝（2.5T 参数/C++ 自研栈）+同日 Grok 5 次序确认。
- **口径全链**：每卡镜像 transcript 逐字原文+snowflake 解码 UTC 对表（六卡全吻合，精确到分写进卡注）；2026 年份条新建（xp-year 结构克隆，扁平混排不新增容器层）。
- **留档**（EXPANSION 卷首）：Grok 4 发布帖（2025-07-09，断代窗界外真空四天）/America Party 2026 政治帖组 178 条池（移交 R10 双写语境）/robotaxi 同日候选 2 条。
- **断言与生成器**：卡数/Permalink/双语对=40×3、年份条 9 全过；检索索引断言 34→40，索引 360 条（119+27+47+40+5+53+4+16+49）；CDP 探针 23/23 全过（文件级 8/桌面 14/390 溢出 1：渲染/时序/逐字/双语/年份组 2026 归位/互链/跨页锚）。
- **版本三件套**：11.2.0 → 11.3.0（15 span 替换计数打印）。

## v11.2.0 — 2026-10-06 · V12-20 R01 · 基建：账本+缺口清单 v3+两份工作册

**主题包成果（V12 R01 · 计划起步）**
- **计划启动**：V12-20 二十轮计划立项（任务书 V12-TASKBOOK.md @097c10d，含四A速查节=站内四模板真实结构/etype 五类/kind 八类/资源 13 字段/verify 九项/全家桶 14 脚本/CDP 惯例）；轮次账本 V12-PROGRESS.md 建立（基线快照+20 轮状态表+恢复指引）；锁 .v12run.lock 确认已在 .gitignore。
- **缺口清单 v3 入账本**：①X 帖断代 2025-08→2026-10 镜像五短语探明（Grok 4=1105/Grok 5=898/America Party=178/robotaxi Austin=37/Optimus production=19 条，最新 2026-10-04——断代期覆盖充足，R02 弹药确认）；②引语 101 块工作册 qa/v12/round-01/quotes-worklog.tsv（101 行，重验路径按来源分类预填，verdict 留 R08）；③email 库 47 封工作册 qa/v12/round-01/emails-worklog.tsv（日精度日期初判在册 14 封，33 封待 R06/R07 双源）。
- **勘误**：全站 site-version-val span 实为 15 处（15 文件各 1）；此前"16 处"系 grep -l 被 changelog.html 正文「site-version-val」字样提及污染（该页无 span 元素）——任务书 §9 与 bump 脚本注释已修正；计数规范=必须用 `site-version-val">` 精确模式。
- **版本三件套**：VERSION / app.js SITE_VERSION / 15 页 span 同步 11.1.0 → 11.2.0（替换计数 15 打印在案）。

## v11.1.0 — 2026-10-02 · 美术增量：复古杂志方向正式落地（用户选定）

**主题包成果（用户选定方向 B · 全站换装）**
- **令牌层替换（style.css :root 15 项）**：纸面五档暖白→奶油（#F3F0E8→#F6EBD7 系）；文字刻度冷黑→暖黑（#17191D→#2B2118 系）；强调色朱红→深棕（#C84032→#8B4513 系，deep/bright/soft/glow 四档同步）；色相刻度 --hue-red 同步转棕（语义不变）。
- **对比度实测全达标**（WCAG 2.1）：浅底正文 13.34 / 次级 7.05 / 三级 5.54；深棕对浅底 6.01（旧朱红 4.35——反而提升）；白字按钮 7.10；深底 accent-bright 5.69——无一项不达标。
- **硬编码清扫**：style.css 内 rgba(200,64,50) 14 处+favicon data-URI 38 页+app.js 彩蛋飞机与关系图 fallback 2 处——全站旧朱红清零（仅 changelog.html 历史文本存 1 处不动）。
- **工具页排除**：preview-v12.html（开发工具）从 verify 页面计数与 sitemap 排除（同 revisions 先例）；build-sitemap.py 同步。
- **排版基线不动**：正文 16.5px / 阅读宽 720px / R17–R19 全部排版与动效成果原样保留——本轮只换色，不碰排版。
- before/after 四页桌面截图入 qa/art-v11.1.0/（全 DIFFERENT ✓）。

**质量门**
- 对比度复测 tools/v12-contrast.py 全达标；v12 验证探针 9/9（色值令牌/favicon/排版基线/390 三页零溢出）；verify.py 9 项全绿（38 页 / 索引 354）；版本三件套 10.14.0→11.0.0→11.1.0；EPUB 重跑（236,024 B）。本轮仅本地提交，不推送。

## v11.0.0 — 2026-10-02 · V10-15 N15/15：终检＋盘点总表 v2＋待发布清单 v2（十五轮收官）

**主题包成果（V10-15 N15 · 收官轮）**
- **盘点总表 v2（入账本独立节）**：账本 119 / 一手文档 27 / 访谈 47 / X 帖 34 / 语录卡 107（引文块 109=107+豁免 2）/ 事件档案 16（材料 67）/ 资源 49（official 11·opensource 9·community 21·tools 8）/ 索引 354；对照 R09 总表的清偿率与新增缺口 v2 见账本盘点节与 EXPANSION。
- **生成器全家桶 11 项幂等重跑**（十项+build-sitemap，sitemap 37 URL=38 页−noindex revisions）。
- **DEVLOG 追加「V10-15 交接要点」**（〇-ter 节）；V10-15-PROGRESS.md 收官标 complete。
- **终验**：verify.py 9/9；CDP 全站终检（主路径六步+双语+390+file://+资源页+38 页×3 视口 114 组合复扫+print 抽查）——探针 tools/v15n15-final-probe.js 断言数见 qa/v10-15/round-15/ACCEPTANCE.md。
- **版本三件套 → 11.0.0**；输出「待发布清单 v2」（RELEASE-CHECKLIST-v11.md，不推送）。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 354）；版本三件套 10.14.0→11.0.0（15 span）；EPUB 重跑。本轮仅本地提交，不推送。

## v11.0.0 — 2026-10-02 · V10-15 N15/15：终检＋盘点总表 v2＋待发布清单 v2（十五轮收官）

**主题包成果（V10-15 N15 · 收官轮）**
- **盘点总表 v2（入账本独立节）**：账本 119 / 一手文档 27 / 访谈 47 / X 帖 34 / 语录卡 107（引文块 109=107+豁免 2）/ 事件档案 16（材料 67）/ 资源 49（official 11·opensource 9·community 21·tools 8）/ 索引 354；对照 R09 总表的清偿率与新增缺口 v2 见账本盘点节与 EXPANSION。
- **生成器全家桶 11 项幂等重跑**（十项+build-sitemap，sitemap 37 URL=38 页−noindex revisions）。
- **DEVLOG 追加「V10-15 交接要点」**（〇-ter 节）；V10-15-PROGRESS.md 收官标 complete。
- **终验**：verify.py 9/9；CDP 全站终检（主路径六步+双语+390+file://+资源页+38 页×3 视口 114 组合复扫+print 抽查）——探针 tools/v15n15-final-probe.js 断言数见 qa/v10-15/round-15/ACCEPTANCE.md。
- **版本三件套 → 11.0.0**；输出「待发布清单 v2」（RELEASE-CHECKLIST-v11.md，不推送）。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 354）；版本三件套 10.14.0→11.0.0（15 span）；EPUB 重跑。本轮仅本地提交，不推送。


## v11.1.0 — 2026-10-02 · 美术增量：复古杂志方向正式落地（用户选定）

**主题包成果（用户选定方向 B · 全站换装）**
- **令牌层替换（style.css :root 15 项）**：纸面五档暖白→奶油（#F3F0E8→#F6EBD7 系）；文字刻度冷黑→暖黑（#17191D→#2B2118 系）；强调色朱红→深棕（#C84032→#8B4513 系，deep/bright/soft/glow 四档同步）；色相刻度 --hue-red 同步转棕（语义不变）。
- **对比度实测全达标**（WCAG 2.1）：浅底正文 13.34 / 次级 7.05 / 三级 5.54；深棕对浅底 6.01（旧朱红 4.35——反而提升）；白字按钮 7.10；深底 accent-bright 5.69——无一项不达标。
- **硬编码清扫**：style.css 内 rgba(200,64,50) 14 处+favicon data-URI 38 页+app.js 彩蛋飞机与关系图 fallback 2 处——全站旧朱红清零（仅 changelog.html 历史文本存 1 处不动）。
- **工具页排除**：preview-v12.html（开发工具）从 verify 页面计数与 sitemap 排除（同 revisions 先例）；build-sitemap.py 同步。
- **排版基线不动**：正文 16.5px / 阅读宽 720px / R17–R19 全部排版与动效成果原样保留——本轮只换色，不碰排版。
- before/after 四页桌面截图入 qa/art-v11.1.0/（全 DIFFERENT ✓）。

**质量门**
- 对比度复测 tools/v12-contrast.py 全达标；v12 验证探针 9/9（色值令牌/favicon/排版基线/390 三页零溢出）；verify.py 9 项全绿（38 页 / 索引 354）；版本三件套 10.14.0→11.0.0→11.1.0；EPUB 重跑（236,024 B）。本轮仅本地提交，不推送。

## v10.14.0 — 2026-10-02 · V10-15 N14/15：事件档案 v2 聚合（事件 14→16）

**主题包成果（V10-15 N14 · 聚合线）**
- **+2 个新档案（事件 14→16，材料 59→67，索引 352→354）**：
  ①**e2015-11-22**「OpenAI：从 10 亿承诺到最后一根稻草」（etype=risk）——2015 创立承诺→2017 控制权→2017 停止资助→2018 退出→2024 诉讼→2026 判决的完整弧线；三封邮件（d2015-11-22/d2017-09-13/d2017-09-21）作为法庭证物材料入档，ai-strategy.html 为叙事层；
  ②**e2026-02-10**「xAI All-Hands：两岁半的幼儿成绩单」（etype=milestone）——2023-07 成立→2023-11 Grok→2026-02 成绩单→2026-03 Terafab；材料含账本 e2026-02-10/e2026-03-21、X 帖 p2023-11-04 与 grok.html 专题。
- **红线自查**：全部材料均为已入册条目（零新增未核实事实）；口径红线闭环探针 **354 = 16 档案 + 45 吸收 + 293 独立**（timeline-events.js records 实测解析）——防漂移机制连续两轮生效。
- Twitter 私有化弧线不立：e2018-08-07 档案已吸收同期材料（2022 后续材料量不足独立成档）。
- **工程**：events-data.py 追加脚本+validate-lite（etype 枚举/必需键全查）；口径复算改用 timeline-events.js 的 TIMELINE_V7 JSON 实测解析（比正则抓 meta 更稳）。

**质量门**
- validate() 过（16 档案/67 材料/28 引语）；全家桶 9 项幂等重跑；verify.py 9 项全绿（38 页 / 索引 354）；CDP 探针 tools/v10n14-probe.js 8/8（口径闭环/16 卡/两新档案渲染/三链深链/390）；版本三件套 10.13.0→10.14.0；EPUB 重跑（236,024 B）。本轮仅本地提交，不推送。

## v10.13.0 — 2026-10-02 · V10-15 N13/15：社区资源扩容 II——档案与书目（资源 44→49）

**主题包成果（V10-15 N13 · 社区资源线）**
- **+5 条入册（资源 44→49，索引 347→352）**：Wikidata 马斯克条目（Q317521，CC0 结构化事实层）/ Internet Archive 马斯克资料搜索页（历史广播与早期访谈的存档层）/ **Isaacson《Elon Musk》官方书页**（Simon & Schuster 2023）/ **Vance《Elon Musk》官方书页**（HarperCollins/Ecco 2015——两书版本判定锚点）/ **Reuters Tesla 专题页**（通讯社滚动档案，本站多条后续注记的背景源）。
- **三路法核活（2026-10-02）**：wikidata 直连 200；**本机 DNS 全域污染**（archive.org/harpercollins/reuters/wikipedia 解析到 Meta 段或 000）——五条经服务端读取器核活 200（archive 搜索页/两书页/Reuters 专题/wikipedia 主条目 DNS 波动），note 逐条注明。
- **查重**：wikipedia-elon-musk 主条目 R13 已在册（本轮初稿误判「漏主条目」，validate id 重复拦截后删除重复项）——validate() 的 id 重复守卫再次生效。
- **Internet Archive collection 页**：搜索页为入口口径收录（具体 collection 页待用户环境定位），note 降表述。

**质量门**
- validate() 过（49 条：official 11/opensource 9/community 21/tools 8）；verify.py 9 项全绿（38 页 / 索引 352）；CDP 探针 tools/v10n13-probe.js 7/7（49 卡/五新卡/DNS 注记/CC0/主条目唯一/检索 Q317521/390）；版本三件套 10.12.0→10.13.0；EPUB 重跑。本轮仅本地提交，不推送。

## v10.12.0 — 2026-10-02 · V10-15 N12/15：社区资源扩容 I——SpaceX 观测生态（资源 36→44）

**主题包成果（V10-15 N12 · 社区资源线）**
- **+8 条入册（资源 36→44，索引 335→347）**：LabPadre（24h 星舰直播）/ NASASpaceflight（报道站）/ NSF Forum（社区情报层）/ r/teslamotors wiki / Everyday Astronaut（与本站 i2021-07-30 专访双向互认）/ Ringwatchers（星舰建造追踪）/ Starship Wiki（S/N 数据库）/ SpaceX 官网发射列表（official）。分布：community 11→16、tools 5→8、official 10→11。
- **三路法核活（2026-10-02）**：直连 200 三条（everydayastronaut/ringwatchers/wikibase）；服务端读取器五条（labpadre 000/nasaspaceflight 403/forum 403/r-teslamotors wiki 000/spacex-launches 403——与既有受限域模式一致，卡内 note 逐条注明）。
- 弃收甄别：spacex.com/launches 虽为官方但与既有 spacex-starship/falcon-9 卡同域不同页——独立收录（任务档案官方入口）。

**质量门**
- validate() 过（44 条四类计数在册）；verify.py 9 项全绿（38 页 / 索引 347）；CDP 探针 tools/v10n12-probe.js 7/7（44 卡/八新卡/核活日期/服务端注记/分类分布/检索 Ringwatchers/390）；版本三件套 10.11.0→10.12.0；EPUB 重跑。本轮仅本地提交，不推送。

## v10.11.0 — 2026-10-02 · V10-15 N11/15：访谈保留池清账（+4 条，43→47）

**主题包成果（V10-15 N11 · 第一手信息线）**
- **保留池逐场处置（5 场：4 立条 + 1 留档）**：
  ①**i2013-05-29** AllThingsD D11——「那份自由感」："Even if you only drive your car…you always want that sense of freedom that if I had to, I could get in this car and go from Boston to DC."（里程焦虑的「自由感」答案）；
  ②**i2019-02-19** ARK Invest 播客——「今年 Feature Complete 级 FSD，我确定」（每周直接管 Autopilot 工程的个人背书）——**承诺对账素材**：当年未按年兑现（FSD beta 2020-10 推送），卡内如实注记；
  ③**i2019-06-13** E3 Coliseum——「未涉之地必然有失败——否则就是你还不够拼」（与 i2008-08-05「失败即数据」弧线互链）；
  ④**i2021-09-28** Code Conference 2021——「就是觉得很酷，来吧——人类，我们在月球上建个基地吧」（+Branson/Bezos 亚轨道点评）。
  ⑤**lex-fridman-438**：镜像 transcript 端点 404（无档），留档待外部逐字源（lexfridman.com 官网）。
- **ASR 平面化口径**：code/ark 两场转写为平文本/全大写形态——引语句大小写与标点为编者所加，卡内注明（R05 MKBHD 先例）。
- 保留池状态：**5 场全部有归宿（4 立条+1 留档），池清零**；60-minutes-2012 已在 N05 降级留档（口径不变）。访谈 43→47，索引 335→339，修订史 227 锚点（访谈 47 入轨）。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 339）；CDP 探针 tools/v10n11-probe.js 9/9（48 卡/六件套/逐字/ASR 注记/对账注记/互链/邻居关系断言[批次式排列口径校准]/检索 freaking/390）；版本三件套 10.10.0→10.11.0；EPUB 重跑（233,848 B）。本轮仅本地提交，不推送。

## v10.10.0 — 2026-10-02 · V10-15 N10/15：keynote 池消化＋AI Day 2021 引语升级（账本 115→119）

**主题包成果（V10-15 N10 · 第一手信息线）**
- **+4 条入册（账本 115→119，语录卡 103→107，索引 327→335）**：
  ①**e2024-06-13-2** 股东大会（特拉华投票同日，`-2` 后缀惯例）——"The goal is to give people hope that there is a path to a fully sustainable global economy…Regarding FSD version 12, it's profound."；
  ②**e2025-05-29** Starship Update at Starbase（正式建制的 Starbase, Texas）——"Progress is measured by the timeline to establishing a self sustaining civilization on Mars…We need about a million tons to the surface of Mars so that Mars can continue to grow even if the supply ships from Earth stop coming"（百万吨判据）；
  ③**e2026-02-10** xAI All-Hands——"xAI is only two and a half years old, basically a toddler…achieved number one in many arenas—in voice, in image and video generation."（10 万张 H100 集群+Grokipedia「银河百科」框架）；
  ④**e2026-03-21** Terafab 发布会——"the most epic chip building exercise in history by far"（Kardashev 尺度开场+SpaceX/xAI/Tesla 三家合力）。
- **必做项完成：AI Day 2021 引语升级（e2021-08）**——原引语「worth more than the car business」实为 2022.09.30 AI Day 的媒体口径（与条目日期 2021.08 错位）。本轮以 2021-08-19 首届官方逐字（555 词在档）替换引文块："Tesla is arguably the world's biggest robotics company, because our cars are semi-sentient robots on wheels…We think we'll probably have a prototype sometime next year…At a mechanical level, you can run away from it and most likely overpower it."（含原型明年见承诺与「能跑赢能制住」安全表述）；「worth more than」句照录保留于现场段并明确标注 2022 媒体口径；ps-src 注明官方转写与 2026-10 复核升级；quotes 卡同轮同批升级。**注意**：555 词逐字中并无「worth more than」句——升级同时修正了「2021 年说过此话」的隐含错配。
- 政治类（wisconsin-town-hall-2025）维持不立；4 场 transcript 存 qa/v10-15/round-10/sources/。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 335）；CDP 探针 tools/v10n10-probe.js 10/10（119 行/升级三重断言/四条逐字/时序/双语/quotes 107/检索 toddler/390）；版本三件套 10.9.0→10.10.0（硬编码三步法）；EPUB 重跑（232,296 B）。本轮仅本地提交，不推送。

## v10.9.0 — 2026-10-02 · V10-15 N09/15：email 库消化 II——四封冲刺信＋47 封归宿清账（文档 23→27）

**主题包成果（V10-15 N09 · 第一手信息线）**
- **+4 份入册（文档 23→27，索引 327→331，全部「媒体获得」口径注明）**：
  ①**d2018-06-17**「破坏者」全员信（"quite extensive and damaging sabotage" + 虚假用户名改 TMOS 代码——Model 3 爬坡黑暗周内患信，CNBC 2018-06-18 全文报道）；
  ②**d2020-09-20** 冲刺创纪录季度信（"record quarter for deliveries…absolute top priority"——Q3 2020 最终 13.93 万辆创当时纪录）；
  ③**d2020-12-01**「舒芙蕾与大锤」盈利警告（"profitability is very low at around 1%" + "crushed like a soufflé under a sledgehammer"——入标普当周的清醒剂，年度名句）；
  ④**d2022-05-31**「回到办公室」终结令（"minimum of 40 hours in the office per week…If you don't show up, we will assume you have resigned."——2022 大回归办公室争论标志文件）。
- **双源**：每封=镜像底本（web_reader 渲染）+ 媒体全文报道（CNBC 2018-06-18 / Electrek·CNBC 2020-09 / CNBC 2020-12-01 / CNBC 2022-05-31），2026-10-02 核验。**Fork in the Road（2022-11-16）查重发现已在册（d2022-11-16，V8 收录）不重立。**
- **email 库 47 封归宿清账（EXPANSION 注记）**：立条 10（R06 两封+N08 四封+本轮四封）+ 在册复用 1（Fork in the Road）+ 留档候选 30（Twitter 收购私信其余件/OpenAI 诉讼余量/逐封双源待续）+ 不立 2（Epstein 两封——与商业主线弱相关且敏感）+ 归类说明 4 = 47。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 331）；CDP 探针 tools/v10n09-probe.js 6/6（27 卡/四信逐字/媒体获得口径/时序/检索命中/390；首跑检索断言踩「索引 q 只存第一 blockquote」既有架构口径——R06 已知限制，断言校准非放宽）；版本三件套 10.8.0→10.9.0；EPUB 重跑（229,371 B）。本轮仅本地提交，不推送。

## v10.8.0 — 2026-10-02 · V10-15 N08/15：email 库消化 I——四封诉讼证物信（文档 19→23）

**主题包成果（V10-15 N08 · 第一手信息线）**
- **+4 份入册（文档 19→23，索引 323→327，全部「诉讼证物」口径注明）**：
  ①**d2015-11-22** OpenAI 创立期邮件「$1B 承诺」（"I think we should say that we are starting with a $1B funding commitment. This is real. I will cover whatever anyone else doesn't provide." + 比 $100M 大以免「听起来毫无希望」）——Musk v. Altman 反驳证据；
  ②**d2017-09-13** 控制权邮件（"I would unequivocally have initial control of the company, but this will change quickly."）——OpenAI 2024-12 官方博客公开文件（WaPo 同步报道）；
  ③**d2017-09-21**「最后一根稻草」（"This is the final straw. Either go do something on your own or continue with OpenAI as a nonprofit. I will no longer fund OpenAI…"）——**2026 联邦法院判决书原文引用**（FindLaw 在档）+ techemails.com 存档，三源；
  ④**d2022-04-09** 马斯克致 Agrawal 三连短信（"What did you get done this week? … I'm not joining the board. This is a waste of time. Will make an offer to take Twitter private."）——Delaware 衡平法院 2022-09 解封证物（BBC/Business Insider 逐字引用）。
- **双源核验**：每封=镜像底本（elonmuskarchive.org/email，web_reader 渲染——curl 拿不到 SSR 正文，正文在客户端流；镜像自带法庭 Exhibit 标注）+ 独立第二逐字源（muskvsaltman.com 法庭文件存档 / OpenAI 官方公开 / FindLaw 判决 / BBC-BI 报道），2026-10-02 核验逐字吻合。
- 其余 39 封（Twitter 收购私信其余件/Tesla 冲刺信等）留 N09。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 327）；CDP 探针 tools/v10n08-probe.js 7/7（23 卡/四信逐字/诉讼证物口径/双语成对/时序/检索 final straw/390）；版本三件套 10.7.0→10.8.0（自动派生版 bump）；EPUB 重跑（228,004 B）。本轮仅本地提交，不推送。

## v10.7.0 — 2026-10-02 · V10-15 N07/15：X 帖 2018–2019 回捞（+3 卡，镜像下限实测）

**主题包成果（V10-15 N07 · 第一手信息线）**
- **镜像下限实测（重要）**：按月切片 24 月全量回捞 3,997 帖（月均不过千、切片可行）——**2018-01 至 2018-06 覆盖近乎零**（01–06 月合计 2 帖），实测下限=**2018-07**。Falcon Heavy 首飞日（2018-02-06）帖镜像无档，候选落空如实留档 EXPANSION（站内存量 p2018-01-28 为特例收录）。
- **+3 卡入册（X 帖 31→34，索引 320→323）**：①**p2018-08-14**「私有化提案顾问阵容官宣帖」（Silver Lake+Goldman 财务顾问、Wachtell+Munger 法律顾问——funding secured 八天后的进程实锤，互链 p2018-08-07）；②**p2019-03-14**「S3XY」（Model Y 发布日命名梗，S/3/X/Y 四车型字母拼合）；③**p2019-05-25**「Starlink 首批致团队帖」（推进/测试/材料三线致谢+披露高温超合金与自建铸造厂工艺决策）。三卡 snowflake 解码与镜像日期一致，transcript 存档 qa/v10-15/round-07/sources/。
- 查重：站内 2018/2019 存量 3 卡（01-28/08-07/11-21）不动；「420」回复帖弱不立。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 323）；CDP 探针 tools/v10n07-probe.js 8/8（34 卡/五件套/逐字/时序分组/互链/双语/检索 S3XY/390）；版本三件套 10.6.0→10.7.0（bump 改自动派生：读上轮 NEW 为 OLD）；EPUB 重跑（226,356 B）。本轮仅本地提交，不推送。

## v10.6.0 — 2026-10-02 · V10-15 N06/15：早期年代 II——文档馆补空（+1 份 DEFM14A 回避记录）

**主题包成果（V10-15 N06 · 第一手信息线）**
- **+1 份入册（文档 18→19，索引 319→320）**：**d2016-10-12**「SolarCity Form DEFM14A（合并委托书 · 马斯克回避表决记录）」——EDGAR 备案 0001193125-16-736379（SolarCity Corp CIK 1408356，被收购方备案），「Background of the Merger」章三段逐字摘录：①董事会回避决定（evaluation/negotiation/approval 全回避+二人不在场审议权）②执行（recused themselves and left the meeting→0.122-0.131 换股比初步提案）③终局（缺席已回避下批准合并协议「fair to, advisable and in the best interests」）——马斯克关联交易治理争议的第一手程序证据。doc-article 模板三段 EN+zh 对照。
- **其余候选处置（如实留档）**：2016-04-21 年度委托书经全文检索无 recusal 措辞（常规关联披露）不立；2009–2010 Tesla 博客存档（tesla.com Akamai/web.archive TLS 双受限）与 2013 爬坡信（需媒体双源）留档 EXPANSION，重验条件不变。
- **检索细节**：2016 合并委托书在**被收购方 SolarCity（CIK 1408356）**而非 Tesla 名下——首次 CIK 检索误中匹兹堡同名公司，经公司名搜索修正（坑：按公司简称猜 CIK 不可靠）。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 320）；CDP 探针 tools/v10n06-probe.js 8/8（19 卡/三段逐字/双语对照/meta 三徽标/时间序/检索 recuse 命中/390 两处零溢出）；版本三件套 10.5.0→10.6.0（**bump 脚本重构为自动前滚版**——三步法代码化，彻底告别手动档位坑）；EPUB 重跑（225,293 B）。本轮仅本地提交，不推送。

## v10.5.0 — 2026-10-02 · V10-15 N05/15：早期年代 I——访谈库 2003–2012 深挖（+1 条）

**主题包成果（V10-15 N05 · 第一手信息线开跑）**
- **候选池实测（预告修正）**：镜像 161 场中 2013 前场次 9 场，逐场试拉 transcript——**仅 wired-musk-2008 有逐字稿**（4,008 字符），其余 8 场 404。R04/R05「60-minutes-2012 官方转写在档」判断经实测不成立（端点 404），该保留池成员降级「待外部逐字源」，EXPANSION 已注记。
- **+1 条入册（访谈 42→43，索引 318→319）**：**i2008-08-05**「乐观悲观，滚他妈的；我们会让它发生」——Wired.com 电话专访（Falcon 1 三连败后、四飞前 5 周、金融危机最坏周）：主句 "Optimism, pessimism, fuck that; we're going to make it happen…"（站外广为征引名句的**原始出处补全**，站内四页查重零命中）+ "That was the dumbest thing I've ever said."（「钱只够烧三次」论当场自嘲修正）+ "Patience is a virtue…It's a tough lesson."；互链 i2008-09-28（四飞成功）与 survival-2008（144 天专题）；transcript 存档 qa/v10-15/round-05/sources/。
- 2003–2012 断档改善有限（+1 条 2008），8 场无档留档如实入账（重验条件=镜像补档或外部逐字源）。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 319）；CDP 探针 tools/v10n05-probe.js 8/8（渲染/六件套/逐字主句/双语/互链双通/时间序/检索 hell-bent 命中/真 390 零溢出）；版本三件套 10.4.0→10.5.0（三步法）；EPUB 重跑（224,144 B）。本轮仅本地提交，不推送。

## v10.4.0 — 2026-10-02 · V10-15 N04/15：资源核活复测＋元数据升级（36 条刷新）

**主题包成果（V10-15 N04 · 核实主线收口）**
- **36 条全量复测**：复用 N01 同日直连/api 结果（零死链）+ GitHub api 串行刷新 8 条——stars 漂移 4 条同步（vehicle-command 705→706 / teslamate 9061→9065 且 pushed 进入 2026-10 / grok-1 52239→52233 / SpaceX-API 10912→10913）；**36 条 checked 全刷 2026-10-02**；resources.html 重建（核活 2026-10-02）。
- **弃收件重验**：tesla.com 专利博文服务端读取器重试仍 Akamai 拦截、SAE J3400 仍 JS 壳——双双维持留档（EXPANSION N04 注记，重验条件不变）；Swisher/JMIR 维持留档。
- **工程**：tools/v10n04-recheck.py（N01 结果复用+api 刷新）/ v10n04-apply.py（checked 批量+gh 逐条精确替换带断言）；recheck.json/tsv 落盘 qa/v10-15/round-04/。

**质量门**
- validate() 过（36 条四类计数不变）；verify.py 9 项全绿；版本三件套 10.3.0→10.4.0（bump 正则前滚直接命中——N03 机制生效）；EPUB 重跑。本轮仅本地提交，不推送。

## v10.3.0 — 2026-10-02 · V10-15 N03/15：口径审计＋引语复核声明上站

**主题包成果（V10-15 N03 · 核实主线收口）**
- **snowflake 全量对表**：X 帖 22 条有 id 者 `(id>>22)+1288834974657` 解码 UTC 与卡内日期 **22/22 全 match**、UTC 口径注零缺失（9 条无 id 卡注明立条口径）。
- **人工抽样**：财报会来源抽 2 条（Q3 2017「地狱刻度 level 9→8」/ Q4 2015「Model 3 下月发布」）对 stockanalysis 逐字稿（23967/23975）——**2/2 逐字吻合**。
- **未覆盖逐条清单**：N02 待人工 101 块逐条归因落盘 unmatched-itemized.tsv（other-official 73 / earnings-call 20 / edgar 6 / jre 1 / ted 1——原因=非镜像源无本地 transcript+Cloudflare 拦批量机核；立条时均经逐字源核实）。
- **双语对齐探针**：quotes 103 卡中 100 卡 EN/ZH 双语齐备（enOnly=0）；primary 抽样 20 行含引文块者 100% 配译文，2 行无引语为 SolarCity 两案（无本人逐字引语，如实设计）——探针首跑误报 2 行经结构甄别后校准口径。
- **「引语复核声明」上站**：primary.html + quotes.html 双语声明（id=quote-review-statement）——措辞如实三层：镜像来源已逐字机核 / 财报会人工抽样 2/2 吻合 / 未覆盖条目逐条注明原因（立条时均经逐字源核实）。满足纪律 D「未覆盖项逐条注明原因」门槛。
- numbers 交叉抽核：「1 万亿」市值口径 numbers 与 primary 双页同现一致。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 318）；CDP 探针 tools/v10n03-probe.js 6/6（双语对齐+声明双语切换+在册）；版本三件套 10.2.0→10.3.0（15 span；bump 正则前滚机制落地）；EPUB 重跑（223,463 B）。本轮仅本地提交，不推送。

## v10.2.0 — 2026-10-02 · V10-15 N02/15：引语逐字核验 I（机核，零实质差异）

**主题包成果（V10-15 N02 · 核实主线）**
- **机核管线三件**：v10n02-extract.py（X 帖 31 卡/访谈 42 块/账本 106 引文块提取，归一化去实体引号空白）+ v10n02-corpus.py（镜像 interview 日期匹配场次 transcript 拉取，19 场匹配新拉 9）+ v10n02-verify.py（本地 45 文件 2.66M 字符语料 indexOf + 镜像 API 分段 diff）。
- **结果：零实质差异，无引语修正**——X 帖 31：18 verified + 3 合并卡口径（两连发合一卡 vs 镜像单帖存档；p2023-07-23 人工深查镜像原文与站内第一段逐字吻合）+ 1 镜像疑无档（2018 flamethrower）+ 9 无锚注记；访谈 42：16 verified + 26 待人工；账本 106 块：5 verified + 101 待人工。**待人工归因=机核语料未覆盖非镜像源**（V8 时代条目来自 stockanalysis/TED/Rev/JRE/EDGAR，本地无 transcript），非发现差异——N03 人工抽样续核。
- **途中甄别**：首跑 3 条 "mismatch" 逐条深查后全部定性为合并卡结构口径，判定逻辑修正为分段 indexOf（避免假红）；X 帖卡提取正则被嵌套 div 截断（改卡起点切片法）。

**质量门**
- verify.py 9 项全绿；版本三件套 10.1.0→10.2.0（15 页 span）；报告全量落盘 qa/v10-15/round-02/。纯核实轮，页面内容零改动。本轮仅本地提交，不推送。


## v10.1.0 — 2026-10-02 · V10-15 N01/15：全站源存活复测（37 条外链，零死链）

**主题包成果（V10-15 N01 · 核实主线开篇）**
- **口径修正（重要发现）**：scan 干跑实测六页来源标注均为 `.ps-src` 文字徽章形态、无明文超链接（引语锚存于账本文字与 qa 溯源，逐字核验归 N02）——复测对象据实调整为全站 38 页真实外链 37 条（resources 36 卡为主体；本站设计=资源页外链层+一手页文字锚层）。
- **复测结果：零死链**——直连存活 12 / GitHub 8 条 api.github.com 复核全 200 / wikipedia+tesla-api.io 服务端读取器复核存活 / wikipedia 余条同域代表推定（口径注明）/ openai.com·x.ai 前档佐证 / 本机受限 5（Akamai/TLS 历史实测）/ SVG 命名空间 n/a。GitHub stars 微漂移 4 条记录在案（字段刷新归 N04）。
- **工程**：tools/v10n01-sources.py（scan/check 两模式，RESTRICTED 预分类清单补录 openai.com）；报告四栏全量落盘 qa/v10-15/round-01/（inventory/check 原始/report 终版）。纯核实轮，无页面内容改动。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 318）；报告覆盖全部外链 37/37；版本三件套 10.0.0→10.1.0（15 页 span）。本轮仅本地提交，不推送。

## v10.0.0 — 2026-10-02 · V9-20 R20/20：全站验收＋待发布清单（二十轮收官，本地待推送）

**主题包成果（V9-20 R20 · 收官轮）**
- **口径总核对（入账本）**：38 页（含 resources，revisions.html 为 noindex 机器页）/ 账本 115 / 文档 18 / 访谈 42 / X 帖 31 / 语录卡 103（账本引文块 105=103+豁免 2）/ 事件档案 14（59 材料）/ 资源 36（官方 10·开源 9·社区 11·工具 6）/ 检索索引 318（115+18+42+31+5+53+4+14+36）。
- **生成器全家桶幂等重跑**：build-events/timeline-events/network/company-files/capital/ledger-links/search-index/resources/ledger-timeline 九项 + 新增 build-sitemap.py 纳入全家桶——sitemap.xml 37 URL（38 页 − noindex revisions.html，口径修正注记）。
- **DEVLOG 追加「V9-20 交接要点」**（〇-bis 节）：三十轮成果地图/单一事实来源增量/已知限制/续作指南。
- **终验**：verify.py 9/9；CDP 全站终检（主路径五步+双语+390+file://+资源页）；38 页×3 视口（320/390/768）全站复扫零溢出；打印抽查（EmulatedMedia print）。
- **版本三件套 → 10.0.0**；.gitignore 补 .v10run.lock；输出「待发布清单」（不推送，另存 RELEASE-CHECKLIST-v10.md）。
- **衔接**：V10-15-PROGRESS.md 已建（N01–N15 内容精修计划，终点 v11.0.0）。

**质量门**
- verify.py 9 项全绿；全站终检探针断言数见 qa/v9-20/round-20/ACCEPTANCE.md；版本三件套 9.9.0→10.0.0（15 页 span）；EPUB 重跑。本轮仅本地提交，不推送。

## v9.9.0 — 2026-10-02 · V9-20 R19/20：动效与微交互＋质量节点③（美术四轮收官）

**主题包成果（V9-20 R19 · transition 审计清单化 + 三态闭环）**
- **全站 transition 审计清单化**：58 处声明全分类落盘 `qa/v9-20/round-19/transition-audit.tsv`（行号/分类/处置/声明）——令牌消费 27、slow 白名单保留 12（0.3s 卡片浮起 / 0.4s 展开动画 / 0.6–1s 进场 / stagger 延迟，语义档保留不改值）、none/reduce 豁免 9、关键帧动画 5、按压反馈 1、other 4。
- **微交互时长归一**：0.18s/.18s/0.25s 硬编码 8 处 → var(--t-fast)（180ms，hover 类无损/更跟手）；归一后硬编码清零（探针断言）。
- **三态闭环**：.btn 补 :active 按压回落（translateY(0)+80ms 快速回弹）——hover 浮起 ↔ active 按压 ↔ focus（R15 全局 :focus-visible 统一出口）三态齐备；aria-pressed 切换型组件（fchip/chip）语义不同不强加。
- **reduced-motion 复核**：14 个 reduce 块在册（reveal 直出/bars 关闭/图形组件/汉堡/语录滚动全覆盖），CDP 模拟 reduce 实测 reveal opacity=1 直出。
- **性能复测（本机条件如实记录）**：五页 load 中位 ≤5ms（127.0.0.1 + urllib 全文取回口径）；体积 style.css 131.6 kB / app.js 31.9 kB / search-index.js 210.8 kB / 38 页 HTML 合计 2071.5 kB——perf.json 落盘。
- **质量节点③（美术四轮收官）**：R15 32 张（before/after 各 16，中英双视口）+ R16 12 + R17 12 + R18 18 + R19 12 张截图齐备入 qa/v9-20/round-15…19/；R19 桌面四页 before/after 中 timeline/capital 逐像素一致（零静态回归），index/survival 微小字节差为运行中动画帧差（语录轮播），如实注明。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 318）；CDP 探针 23/23（文件级 8/btn 三态 2/reduce 模拟 1/三视口九宫格 12）；node --check 通过；版本三件套 9.8.0→9.9.0（15 页 span）；EPUB 重跑。本轮仅本地提交，不推送。

## v9.8.0 — 2026-10-02 · V9-20 R18/20：排版与阅读体验（lr-*/ps-*，数字等宽+引语注区分）

**主题包成果（V9-20 R18 · 纯 CSS 精修，style.css +30 行）**
- **基线复核并锁定**：正文 --fs-body 16.5px（16–18 ✓）/ 长文阅读宽 --read-width 720px（640–760 ✓），均为 R15 定值，本轮探针断言锁定（computed fontSize/maxWidth）。
- **数字/日期/金额等宽**：文字层 12 类选择器 tabular-nums（lr 正文/引语/编者注/来源行/meta 值/数据框 + ps 引语/译文/事实/日期/来源徽章/计数）；数据表 .lr-data .num 数字列改 --font-num（工业数字，消费 R17 令牌）。
- **引语块与编者注三重区分**：引语=实底+5px 实线+块影（--shadow-1）+加宽内衬；编者注=纸底（--paper）+虚线框。**覆盖三族引语容器**——.lr-quote（长文/events 档案 24 处）与 .sv-node/.pv-case blockquote（特稿节点，survival-2008 引语实为裸 blockquote 无类，首版 CSS 漏覆盖被探针捕获后修正）。
- **EN 长文**：正文行高 1.92→1.78、引语 1.75（仅 EN 模式）+ 长词换行保护（overflow-wrap）；中文模式不变。
- **print**：引语块影显式关闭（CDP print 媒体模拟实测 boxShadow none）。
- 零新增 transition/animation（reduced-motion 免复核）；「示意非等比」等口径注无触碰。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 318）；CDP 探针 28/28（文件级 6/survival 排版 7 含 EN 切换往返/deep-dive .num 1/primary 账本 2/print 模拟 1/三视口九宫格 12）；before/after 九组（survival 三组差异可辨，index/timeline/capital 六组逐像素一致=改动面不含 lr 元素属预期，如实注明）；node --check 通过；版本三件套 9.7.0→9.8.0（15 页 span）。本轮仅本地提交，不推送。

## v9.7.0 — 2026-10-02 · V9-20 R17/20：数据图形工业风（三图精修，数据编码不动）

**主题包成果（V9-20 R17 · gx-*/cap-*/net-* 三图工业风精修，纯 CSS）**
- **etype 节点形状语言（色标不变加形）**：创业起步=圆（既定）/ 资本运作=方 / 豪赌翻身=菱（45° 旋转）/ 产品里程碑=满圆 / 争议时刻=三角（clip-path 警示形）——形状四分补足色盲可达性；**类型筛选芯片补 ::before 形状图例**（原为纯文本无色点），图例即形状表。
- **gx 年轴刻度细化**：年份改等宽数字（新令牌 --font-num，入 R15 字体层）+ 每个年份刻度线（::after 6px）；清单视图日期同步等宽。
- **标注层数字等宽**：cap-elabel 改技术字体（sans + tabular-nums，标注层与节点名 serif 形成分层）；cap-meta/cap-status/net-elabel/两图例 tabular-nums。
- **图例语法统一**：cap-legend 与 net-legend 同字号（--fs-small-2）、同间距（22px 列距）、虚线同构造（repeating-linear-gradient 统一）。
- **图底点阵网格**：cap-graph 与 net-graph 加示意纸面点阵（radial-gradient 26px 网距，不模拟坐标刻度、不伪装精确）；print 显式关闭。
- **数据编码不动（红线自查）**：流向线宽仍按金额对数标定（探针断言首条 ribbon 计算线宽=生成器属性值）、公司色标与 etype 色不动（gamble 仍朱红 rgb(200,64,50)）、「示意非等比」口径注原文保留；R17 段零新增 transition/animation（reduced-motion 免复核），打印形态复查通过。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 318）；CDP 探针 34/34（文件级 5/桌面三图 17/三视口九宫格零溢出 9/390 清单形态 3）；node --check 通过；版本三件套 9.6.0→9.7.0（15 页 span）；EPUB 重跑。本轮仅本地提交，不推送。

## v9.6.0 — 2026-10-01 · V9-20 R16/20：首页视觉迭代（封面构图 + 模块节奏 + 三入口强化）

**主题包成果（V9-20 R16 · 美术升级第 1 轮，消费 R15 令牌体系）**
- **三入口视觉强化（封面 hero）**：`开始阅读 / 探索公司版图 / 查找资料` 由普通按钮行升级为**编号入口条**（`.act`：斜体衬线编号 01/02/03 + 右细分隔线 + 文字 + 箭头，hover 箭头右移、反白填充；主入口 `.act-primary` 朱红实底）。`data-en` 全部下沉到 `.act-txt` 叶子节点，编号与箭头语言无关，中英切换不破坏结构。移动端 640px 断点下三入口各自占满一行，主次分明。
- **封面照「报头」处理**：肖像加左上角朱红封面标 `COVER · 2018`（`.cover-tag`，aria-hidden 装饰）+ 内衬细线双框（`.hero-figure::before`，inset 10px hairline）——经典报刊封面照语言。
- **业务画面横带（hero-strip）图版化**：四图的公司标（TESLA/SPACEX/X）从图下说明移至**图片左上角深底浅红角标**（图版编号式叠加）；图片 hover 微抬升 + 朱红描边（`--t-fast`，reduced-motion 全覆盖）。
- **封面关键数字行强化**：`.hero-stats` 顶部分隔线 1px/40% → **2px/55%**，数字色 `--paper` → `--paper-0` 提亮一档，刊头感更强。
- **模块节奏：公司版图打破等尺寸卡片感**：6 等大瓦片 → **2 特大（Tesla / SpaceX，各跨 2 列，自动排布为「上行两大、下行四小」）+ 4 标准**。特大瓦片标题 26px、编号标 10.5px、行距与内边距放大（`.firm-grid .firm-tile--xl` 提高特异性防基础规则覆盖）。公司色标顶条 `--co-*` 语义未动。
- **旗舰专题分层**：`.feature-rows` 前三条 FEATURE 级行（2008 生死役 / 平台变局 / 承诺与结果）加 **3px 朱红左标线**，与后四条 DEEP DIVE 级行拉开层级；全部行 hover 加 `--paper-50` 微底色。路径区 `.path-row` hover 标题转朱红，与全站 hover 语言一致。

**质量门**
- CDP 探针 **43/43**（tools/v9r16-probe.js，端口 9364）：结构断言（2 特大瓦片 / 3 入口 / 角标定位）/ 几何断言（特大瓦片宽 501px = 2× 标准 244px，同行并排）/ 计算样式（主入口朱红 `rgb(200,64,50)` 白字、stats 2px、前三行 3px 左标线）/ EN 切换结构不破 / hero 标题不破版 / 三视口（320/390/768）× 中英零横向溢出 / 60 次 Tab 内键盘命中三入口且焦点环 3px 统一。
- before/after 全页截图各 6 张（index × 桌面/平板/手机 × 中英）+ 首屏并排对比图 3 张（compare/）；像素差异 **11.0%–28.1%**（中位 22.3%，首屏显著变化达成）。
- verify.py 9/9（38 页 / 索引 318 / 版本 9.6.0）；node --check 通过；版本三件套 9.5.0→9.6.0（VERSION + app.js + 15 页 span，替换计数在案）；EPUB 重刷。本轮仅本地提交，不推送。
- 过程修复：探针首跑 38/43——① `.firm-tile--xl h3` 与 `.firm-tile h3` 同特异性被源码顺序覆盖（真缺陷，改 `.firm-grid .firm-tile--xl h3` 提特异性）；② 探针期望值误写（`--on-hue` 本为 `#fff` 非 paper-0）；③ reduce 模拟下断言 transition（自然为 none，改文件级断言）；④ Tab 循环上限 14 次不足（导航下拉经 `:focus-within` 展开后可聚焦，键盘需穿越约 43 个导航项，上限放宽至 60）。

## v9.5.0 — 2026-10-01 · V9-20 R15/20：设计系统升级（令牌层 + 焦点统一 + 对比度复核）

**主题包成果（V9-20 R15 · 美术地基轮）**
- **`:root` 令牌层重建为三层结构**（style.css）：① 刻度令牌（`--hue-*` 五色相 / `--paper-0…200` 暖白 5 档 / `--coal-soft,0,100,200` 近黑 4 档 / `--tx-1…4` 浅底文字 4 阶 / `--txd-1…6` 深底文字 6 阶 / `--accent-deep…glow` 朱红 5 档 / `--rule-*` 描边 6 阶 / `--r-1…circle` 圆角 6 档 / `--shadow-1…shadow-accent-lg` 块影 6 档 / `--fs-*` 字号 18 阶 / `--space-*` 4-8 基间距 18 阶）→ ② 语义令牌（`--ty-*` 事件类型 6 色、`--paper/--ink/--muted/--mist/--card/--navy/--accent-text`）→ ③ 焦点令牌（`--focus-w / --focus-w-tight / --focus-offset* / --focus-color[-dark|-invert]`）。令牌 **37 → 113 项**。
- **正文硬编码收敛为令牌（值等价、零视觉回归）**：事件类型色 12 处 → `--ty-*`；资源徽标色 6 处 → `--hue-*`（与事件类型同源，色相刻度统一）；纯白表面 `#fff` 26 处（chip/card/图节点）→ 暖白 `--paper-0`，统一暖纸体系；描边 7 处、圆角 46 处、块影 8 处、字号 269 处、焦点环 8 处全部令牌化。`@media print` 18 个块显式保护（`#fff/#000/#999` 印刷形态不动）。公司色标 `--co-*` 语义与值一律未改。
- **`:focus-visible` 全站统一出口**：所有焦点环改用 `--focus-*` 令牌（文字控件 3px/3px、密集 SVG 节点 2px/2px、暗底用 `--focus-color-dark`、反色用 `--focus-color-invert`），原先散落的 8 处 `2px/3px` 硬编码全部消除；`--focus-offset-wide` 用于锚点 `:target` 高亮。
- **对比度复核（WCAG 2.1，tools/v9r15-contrast.py 实测）**：`--mist` 9.27:1、`--muted` 6.24:1、`--accent-text` 5.80:1、`--accent-bright` 6.26:1 全部 ≥4.5 达标。**查出并修复 2 处不达标的小字色阶**：`#8a857c`（3.22:1）与 `#9a948b`（2.64:1）原用于时间轴年份轴标、事件引语行、空态提示等浅底小字——新增 `--tx-3`（#6A665D，浅底 5.02:1 / 卡片 4.63:1）承接，5 处换用；`--tx-4`（#8a857c）保留给装饰线与暗底小字（coal 5.08 / ink 4.80，达标）。
- **四页样板落地**：index（封面/路径卡/资料入口）、survival-2008（`sv-*` 图形与阶段徽标）、timeline（`gx-*`/`pt-*` 图与账本时间轴）、capital-evolution（`cap-*` 流向图与图例）四页消费全部新令牌；before/after 各 16 张全页截图（4 页 × 桌面 1440×900 / 手机 390×844 × 中英）。

## v9.4.0 — 2026-10-01 · V9-20 R14/20：资源交互与联动（质量节点②）

**主题包成果（V9-20 R14 · 资源板块从「有」到「通」）**
- **资源↔公司档案互链（单一事实来源驱动）**：resources-data.py 新增 `resources_for_company()` 查询接口；build-company-files.py 按公司实体交叉引用，为 4 份公司档案（Tesla/SpaceX/X/xAI）各加「相关社区资源」节（`.cf-resl`，共 16 条资源深链，按 category 顺序稳定排序、每公司上限 6 条，「综合」类不参与匹配避免泛条污染）；companies-data.js 增 `resources` 字段，app.js 公司关系图详情面板同步增「相关社区资源」行（中文「相关社区资源（N）」/ 英文 COMMUNITY RESOURCES (N)）。
- **资源页可访问性**：筛选状态行 `#rs-status` 加 `role="status" aria-live="polite"`（切分类时读屏即时播报「显示 N 条资源 · 分类」；无脚本环境该行静态完整可读）。
- **首页资料入口**：index.html「查找资料」路径行第三入口由「文档馆」改为「社区资源」（resources.html，双语 data-en="Community resources"），资源板块从深链导航升级为首页主路径可见。
- **检索联动复核**：search.html 类型按钮「社区资源」+「按公司过滤」对资源条目直接可用（R10 已接通，本轮验证命中与类型筛选组合）。

**质量节点②验收（计划要求 ≥15 断言全流程）**
- **资源页全流程 CDP 探针 37/37**（tools/v9r14-probe.js，端口 9358）：筛选（切分类→状态行 aria-live 更新→清除恢复）/ 跳转（资源→公司档案→回资源互链闭环）/ 双语（中英切换资源名与状态行）/ 无 JS（禁脚本 36 条全量可读）/ 390 零横向溢出 / file:// 协议离线可读。
- **外链抽样 10 条核活**（2026-10-01 复测，qa/v9-20/round-14/sources/liveness-sample.md）：官方 2 / 开源 2 / 社区 3 / 工具 3，10/10 可达（Wikipedia 群与 GitHub 项目当日 200）。
- verify.py 9/9（38 页 / 索引 318 / 版本 9.4.0）；node --check 通过；EPUB 重刷（223,127 B）。

## v9.3.0 — 2026-10-01 · V9-20 R13/20：社区与档案资源（community 3→11，wikipedia「DNS 污染」判定证伪）

**主题包成果（V9-20 R13 · 资源板块 +12 条，R11–R13 合计 +26 条）**
- **+12 条入库（community 3→11 · opensource 6→9 · tools 5→6，全站资源 24→36，索引 306→318）**：维基百科条目群 8 条（Elon Musk / SpaceX / Tesla, Inc. / Starship / Acquisition of Twitter by Elon Musk / List of SpaceX launches / Grok (chatbot) / Neuralink）/ Tesla JSON API 非官方文档（tesla-api.timdorr.com）/ TeslaPy（417★ MIT 2026-07 活跃）/ Powerwall 2 本地网关 API 文档（290★ Apache-2.0 2024-10 停更）/ Jonathan McDowell 太空档案（planet4589.org）。Wikipedia 群以「公共参照系」口径收录并逐条注明为二手（非一手）。
- **重要重验：R10「en.wikipedia.org DNS 污染不可达」判定证伪**——R10 留档记解析被污染至 31.13.88.26 故弃收；本轮实测直连 **200 且内容为真**（Elon_Musk 页 2.68 MB、title 正确、正文 525 处命中；SpaceX 1.53 MB；Twitter 页正常重定向至 X (social network)）。curl `%{remote_ip}` 显示 127.0.0.1（本机代理/hosts 接管路径），故 R10 的污染判断已被推翻，8 条 Wikipedia 条目全部入册，卡内 note 注明判定全过程与所载 http 口径。
- **Reddit 社区档案「假活」甄别（宁缺毋滥）**：www/old.reddit.com 的 r/teslamotors 与 r/SpaceXLounge wiki**直连返回 200 但内容为 8.4 KB JS 空壳**（title 仅「Reddit」，正文 0），WebFetch 服务端复验同为空壳，`…/wiki/index.json` API 403——不满足「内容到手」门槛，**本轮不收**（R12 收 r/SpaceX wiki 的前提是服务端读取器取得正文）。留档 EXPANSION，重验条件=服务端读取器能取正文或 API 放开。
- **软页甄别**：teslaownersonline.com 返回 **202 + JS proof-of-work 挑战**（bot 拦截软页），非真内容，弃收；web.archive.org 直连 000 且 WebFetch 失败，留档待重验；spaceflightnow.com / apnews.com / reuters.com / nytimes.com / science.org / sec.gov 搜索页均 403，弃收留档。
- **媒体档案类择要**：teslarati.com / electrek.co / arstechnica.com（含 /space/）/ nasaspaceflight.com / everydayastronaut.com / space.com / theverge.com/elon-musk / techcrunch.com 与 cnbc.com 的马斯特 tag 页 / BBC 专题页 全部直连 200 且内容为真——按「媒体档案库」性质作为后续候选（本轮以 Wikipedia 群 + 开源补位为主，媒体 hub 页入候选池留 R14 后按检索联动需要择要）。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 318）；CDP 探针（断言数见账本）；node --check 通过；版本三件套 9.2.0→9.3.0（VERSION + app.js + 15 页 span，替换计数在案）；EPUB 重跑。本轮仅本地提交，不推送。

## v9.2.0 — 2026-10-01 · V9-20 R12/20：开源项目资源（opensource 2→6，tesla-api.io 死链判定证伪）

**主题包成果（V9-20 R12 · 资源板块 +6 条）**
- **+6 条入库（opensource 2→6 · community 2→3 · tools 4→5，全站资源 18→24，索引 300→306）**：timdorr/tesla-api（2,065★ MIT，2026-03 活跃，近十年非官方 API 文档+Ruby gem）/ r-spacex/SpaceX-API（10,912★ Apache-2.0，维护者已存档 2024-08）/ sparky8512/starlink-grpc-tools（710★ Unlicense，2026-09 活跃，星链终端 gRPC 遥测）/ tesla-api.io 社区文档站（2024-01 起停更）/ r/SpaceX 社区维基（发射编年史与 FAQ，非官方）/ Tessie（商业托管路线代表，与 Teslamate 自托管互为两端）。
- **R10 死链判断证伪（重要重验）**：tesla-api.io 此前本机 DNS ENOTFOUND（R10 留档疑似死链）——本轮独立解析发现本机 UDP DNS（8.8.8.8/1.1.1.1）全部被墙不可用，改经服务端读取器核活 **200 且站点在线**（自注 2024-01 起弃用、由官方文档接管，deprecated ≠ 下线）→ 结论为**本地运营商 DNS 污染而非死链**，按「停更」收录并卡内注明判定过程。
- **核活路径如实注记**：GitHub 三仓库 api.github.com 直读（stars/最近提交/许可/存档态）；tesla-api.io 与 Reddit wiki 经服务端读取器 200（本机 curl 000/被墙），Tessie 直连 200。
- **治本修复 revisions.html 导航回归（R10/R11 连续两轮同处回归）**：build-revisions.py 内联模板从不包含 site-nav 报头，每次重跑都会冲掉导航注入——本轮在模板内直接嵌入 `build_masthead('revisions.html')` + app.js（导航单一来源原则），此后重跑不再回归；本轮探针新增「revisions.html 导航在册」断言防复发。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 306）；CDP 探针（断言数见账本）；node --check 通过；版本三件套 9.1.0→9.2.0（span 替换计数在案）；EPUB 重跑。本轮仅本地提交，不推送。

## v9.1.0 — 2026-10-01 · V9-20 R11/20：官方与标准类资源（official 2→10，核活三路法）

**主题包成果（V9-20 R11 · 资源板块 +8 条全落官方与标准类）**
- **+8 条入库（official 2→10，全站资源 10→18，索引 292→300）**：SpaceX 官网三页（vehicles/starship · vehicles/falcon-9 · updates）/ Tesla 官方开发者门户 Fleet API（developer.tesla.com）/ Neuralink 患者登记（patient-registry）/ OpenAI 2015 官宣文 Introducing OpenAI（联合主席含马斯克，AI 弧线官方起点）/ xAI 官网 / The Boring Company 官网。COMPANIES_VOCAB 增 OpenAI 实体（仅资源条目使用，检索「按公司过滤」自动出现，不扰动存量 282 条实体推断）。
- **核活三路法（本轮方法论沉淀）**：浏览器 UA curl → WebFetch → 服务端读取器逐级复核——curl 直连对 tesla.com / spacex.com / openai.com 全 403（Akamai 反爬）、neuralink.com 连接重置、x.ai 超时；服务端读取器对其中 7 条核活成功并取得官方 meta/正文，**逐条在卡内 note 注明真实核活路径，不冒充直连**（Boring Company 为直连 200）。R10 留档反爬项除 tesla.com 外全部重验成功入册。
- **弃收留档（宁缺毋滥）**：SAE J3400（NACS 标准化文本）——检索确认标准存在（J3400/2 连接器尺寸 2025-04 / J3400/1 适配器安全），但 sae.org 全站 JS 壳、构造 URL 与 connect.sae.org 落地页均无法内容级验证，弃收待用户环境重验；**tesla.com 全站（含 All Our Patent Are Belong To You 博文与 NACS 页）三路均被 Akamai 拦截**，维持留档。详见 EXPANSION.md R11 块。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 300）；CDP 探针 ≥10 断言（结构/双语/检索联动/无 JS/390）；node --check 通过；版本三件套 8.10.0→9.1.0（span 替换计数在案）；EPUB 重跑。本轮仅本地提交，不推送。

## v8.10.0 — 2026-10-01 · V9-20 R10/20：资源页基建（开源社区资源板块开工）

**主题包成果（V9-20 R10 · 新板块第 38 页 resources.html 打通管线）**
- **数据单一事实来源 tools/resources-data.py**：字段 url / name(zh,en) / desc(zh,en) / category / 语言 / 活跃度（维护中|停更|存档）/ 许可 / 收录理由 / 关联公司 / 核活日期，内置 validate()（url 须 http(s)、双语完整、category∈枚举、核活日期必填，不过拒生成）；首批种子 10 条（官方与标准 2 · 开源项目 2 · 社区与档案 2 · 工具与数据 4——工具类 4 条为当批核活清单全量入库，超「每类 1~2」软指引、在 8~12 硬区间内）：SEC EDGAR Tesla 文件 / Tesla 官方开源 vehicle-command / Teslamate（★9,061）/ xAI Grok-1 权重（★52,239）/ Elon Musk Archive 镜像 / Wait But Why Neuralink 长文 / Flight Club / Next Spaceflight / Launch Library 2 / starlink.sx。
- **核活口径**：每条 URL 于 2026-10-01 实测（curl http_code 或 WebFetch），GitHub 记 stars 与最近提交月（api.github.com 无认证串行）；grok 仓库已改名 grok-1（52 跳转跟随后建档）。本机不可核活 7 条留档 EXPANSION.md 待重验（tesla.com 与 spacex.com 反爬 403、neuralink.com/tesla-api.io 连接失败、en.wikipedia.org DNS 不可达等），未编造任何一条。
- **生成器 tools/build-resources.py**：幂等生成 resources.html——lr-hero 页头 + 分类筛选芯片（仿 gx-fchip，min-height 28px 由既有移动层继承）+ 四分类清单 + 逐条详情字段行（网址/分类/语言/活跃度/许可/关联公司/GitHub 实测/核活码/口径备注/收录理由）；无 JS 完整可读（芯片惰性、全量可见，筛选仅做分类节显隐）；≤640 字段行纵向堆叠；print 隐藏筛选保留清单；rs-* 组件层入 style.css（无新过渡，reduced-motion 免复核）。
- **管线**：site-nav.py「资料」组注册 resources.html（37 页重注入）；build-search-index 增「社区资源」类型，索引 282 → 292；search.html 类型按钮 +1。**verify.py 第 4 项断言扩展**（索引=页面锚点约束原样保留，新增 rs-item 锚点计数）——理由：社区资源为生成器产出的合法新增类型，同 V7-19 R15 事件档案先例，CHANGELOG 特此说明。
- **资源纪律声明**：外链不构成运行时依赖，页面本体静态、file:// 离线可读；资源条目一律不作为引语出处（页内明示，查证原话走账本/文档/访谈/X 帖）。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 292）；CDP 探针 ≥10 断言（结构/筛选/双语/无 JS/390）；node --check 通过；EPUB 重跑。本轮仅本地提交，不推送。

## v8.9.0 — 2026-10-01 · V9-20 R09/20：语录卡补齐 + 质量节点①（盘点总表与缺口清单）

**主题包成果（V9-20 R09 · 语录核实组全覆盖收口 + 第一手信息盘点）**
- **e2013 立卡（die on Mars 名句入核实组）**：quotes.html qs-grid 按时间序补入 2013（约）卡（e2012-06-22 与 e2013-05-08 之间），语录卡 102 → 103 张；卡文与账本 e2013 逐字一致（"I would like to die on Mars. Just not on impact."），日期与来源如实双标「约 2013 · 广泛征引」（R05 甄别留档：真实出处待考，TED2013 官方转写无此句——本卡锚账本口径，不杜撰出处）。顶部格言轮播五句维持「广泛征引待考」注记不动。
- **verify.py 第 6 项白名单收窄（3 → 2）**：e2013 移出 QS_EXEMPT（已立卡）；e2021-07（The Next Web 第三人称转述，非本人逐字）与 e2025（Boring Company 官网项目页统计口径，非本人引语）保留豁免——注释更新说明保留理由，原约束精神（有引文必上卡/卡必有引文）不变。此为口径收严而非放宽：白名单越小，覆盖要求越高。
- **第一手信息盘点总表入账本**（V9-20-PROGRESS.md 独立节）：八类型计数表（282 = 115+18+42+31+5+53+4+14）、账本逐年分布条形表（重心 2016–2022 占 59%）、X 帖/访谈/文档分类型年份覆盖、语录卡覆盖状态。
- **缺口清单写回 EXPANSION.md**（顶部 R09 节）：账本早期年代稀薄（2003–2005/2007 零、2009–2011 各 1）、访谈 2007–2012 断档（保留池 6 场可随时立）、X 帖 ≤2019 未探（镜像下限 2018）、文档馆五个年代空白，各附候选与重验条件——作为后续轮候选池。
- **质量节点① · 三口径零漂移核对**：页面锚点（verify 第 4 项）= 检索索引（search-index.js 282 条）= 生成器断言（build-search-index.py 8 项计数）三者一致；语录卡口径（第 6 项）103 卡 + 2 豁免 = 105 引文块闭环；生成器全家桶幂等重跑无漂移。

**质量门**
- verify.py 9 项全绿（37 页/索引 282/语录卡 103+2）；CDP 探针全过（新卡渲染与位置/跳转锚实存/双语/格言区与核实区并存/检索回归/390 无溢出）；node --check 不涉及（无 JS 改动）；EPUB 重刷。纯本地提交，不推送。

## v8.8.0 — 2026-10-01 · V9-20 R08/20：事件档案聚合扩容（V8/V9 新材料归档，9→14）

**主题包成果（V9-20 R08 · events-data.py 9 → 14 个事件档案，材料关联 37 → 59 份）**
- **五个新档案入册（全部由已核实账本/文档/帖子聚合，不新增未核实事实）**：**e2010-06-29** Tesla IPO——S-1 商业模式总纲与首份关键人风险因子、2013 Q1 首盈利收尾、与 d2022-02-07 十年后「Technoking」同名风险因子跨十二年对照；账本当日无本人逐字原话，档案如实引 SEC 文件并注明口径。**e2021-10-25** 万亿市值日——Hertz 十万辆订单、same margin 对冲帖（p2021-11-02，snowflake 解码 UTC 2021.11.02 01:48 即美国 11.01 晚）、编年史 c2021-10-25 三方同框；V8 弃收件回捞闭环在 outcome 注明。**e2021-11-26** Raptor 危机与星舰翻身——环月承诺（2018）→不锈钢转向（2019）→SN15 着陆（2021-05）→破产警报全员信（2021-11）→Starbase 员工演讲（2024-03）五材料时间线，「每两周一飞未兑现/破产未发生/dearMoon 取消」如实对照。**e2024-01-29** Neuralink 首例人体植入——三只小猪（2020）→MindPong（2021）→「大概六个月」预言（2022-11-30）→Telepathy 官宣（2024-01-29）五材料「预言→兑现」线，实际约十四个月的口径差异在案。**e2019-04-22** 从 Autonomy Day 到 Optimus——HW3/LIDAR doomed/「2020 功能完整」承诺滑票（promises.html 对账）→AI Day 2021 幻灯片→Q4 2021 电话会排位→AI Day 2022 真机，四条已核实引语串联。
- **材料类型枚举扩充**：KIND_LABELS 新增 chronicle（编年史条目，站内第二叙事口径）——validate() 与 build-events.py 渲染同步通过，无 CSS 变更（非 ledger 类型共用默认样式）。
- **口径红线闭环（防 160 漂移重演）**：检索索引 277 → 282 条（事件档案 9→14 自动跟随断言 len(ED.EVENTS)）；时间轴吸收 18 → 39 条，独立记录 250 → 229 条，**282 = 14 档案记录 + 39 吸收 + 229 独立**，TIMELINE_V7.meta 探针断言在案；建档卡关联 18 → 23 处（新覆盖 5 个账本条目）；timeline.html 静态清单同步注入（14 已建档事件行 + 229 独立记录行）。
- **深链全在册**：events.html 14/14 锚点 fetch 验证通过；五张新卡结构抽查（引语/材料徽标/相关事件渲染）全过；档案间互链 6 处（#e2008-12-24/#e2018-08-07/#e2024-10-13/#e2008-09-28/#e2010-06-29↔#e2021-10-25 双向）+ 争议深读 controversy.html#autopilot。
- **版本三件套**：8.7.0→8.8.0（VERSION/app.js/14 页 span，替换计数打印在案）。

**质量门**
- verify.py 9 项全绿（37 页/索引 282）；node --check 通过；CDP 探针全过（TIMELINE_V7.meta 口径断言/五新卡渲染/材料徽标 chronicle/深链 fetch 14/14/390 无溢出/检索命中）；生成器全家桶幂等重跑（events/timeline-events/network/company-files/capital/ledger-links/search-index/epub）。纯本地提交，不推送。

## v8.7.0 — 2026-10-01 · V9-20 R07/20：官方演讲扩充（镜像 keynote/speech 全档转写批次）

**主题包成果（V9-20 R07 · 账本 109 → 115 条，全部为官方发布会/演讲全场逐字）**
- **六条入册（elonmuskarchive.org keynote/speech 库 /video/{id} 详情页全场逐字转写，官方直播录像源在册）**：**e2015-12-02** COP21 索邦演讲——「史上最愚蠢的实验」+ 纽约 ±5 度气候敏感性对照 + 税收中性碳税药方，互链 e2015-04-30；**e2018-09-17** BFR 环月旅客发布会——前田裕二 2023 环月承诺与「这很危险，可不是公园散步」风险声明同框，dearMoon 2024 年中取消入后续，互链 e2017-09-29/e2019-09-28；**e2019-04-22** Autonomy Day——「LIDAR is a fool's errand…doomed」传感器路线宣言 + 芯片冗余论证，承诺滑票注 promises.html；**e2022-09-30** AI Day 2022——「去年那就是个穿机器人服装的人」自首式开场 + Bumble C 真机行走 + 丰裕未来压轴，互链 e2021-08（AI Day 2021 媒体口径条目）；**e2022-11-30** Neuralink Show and Tell——「六个月内首例人体植入」预言 + 意念打字 + AI 对冲动机，兑现注脚 2024-01 底（e2024-01-29），互链 e2020-08-28/e2021-04-09；**e2024-03-18** Starbase 星舰更新会——「总有一天我们会真正在火星上安家」+ 一年 96 发猎鹰成绩单 + 八年载人上火星新钟，八个月后塔架捕获（e2024-10-13/p2024-10-13）。
- **采料管线（本轮新建）**：镜像 keynote 库 60 场 + speech 库 21 场全部 hasTranscript（100%）；/video/{id} 详情页正文为「说话人标签 + 可点击段落块」结构，tools/v9r07-fetch-keynotes3.py 按 button 块整体剥标签保词序抽取（v1/v2 逐词 span 截断导致乱序的教训在案）；六场 transcript 全文存 qa/v9-20/round-07/sources/。
- **甄别与留档（EXPANSION.md 详录）**：AI Day 2021-08-19 官方逐字已在档（Musk 独白 555 词）但账本 e2021-08 已有媒体口径条目，不重复立条留档待引语升级；Starship Update 2025-05-29（Musk 4,836 词）入候选池；Wisconsin town hall 2025（12,095 词）政治集会类与「官方演讲」主题不合不立；AI Day 2021 时长仅 401 秒（开场片段）单独成条价值有限；COP21（1,632 词）与 SpaceX IPO 敲钟（9 词）经评估取前者。
- **口径与互链**：六卡页内互链 13 处（站内锚全部实存）；ASR 转写口径卡内注明（Yusaku 误听 Usage/Falcon 误听 Belkin/neural link 分词等，引语避开或照录注明）；e2024-03-18 镜像归档日期与内容指向 IFT-3（03-14）前夜的差异如实双注。
- **检索断言同步**：tools/build-search-index.py 言行实录断言 109→115，索引 271→277 条（115+18+42+31+5+53+4+9）。
- **版本三件套**：8.6.0→8.7.0（VERSION/app.js/14 页 span，替换计数打印在案）。

**质量门**
- verify.py 9 项全绿（37 页/索引 277）；node --check 通过；CDP 探针全过（六新卡渲染/结构四段五件套/Permalink 115 对/双语 data-en/互链目标存在性/390 无溢出/检索命中）；EPUB 重跑（24 章）。纯本地提交，不推送。

## v8.6.0 — 2026-10-01 · V9-20 R06/20：文档馆扩充（SpaceX 全员信 + SEC 文件）

**主题包成果（V9-20 R06 · documents.html 14 → 18 份）**
- **两封 SpaceX 全员信入册（elonmuskarchive.org email 库，全部「员工外流文本」口径如实标注）**：**d2010-05-04**「Acronyms Seriously Suck」——自造缩写禁令三段逐字（"a significant impediment to communication" / "Unless an acronym is approved by me, it should not enter the SpaceX glossary" / VTS-3 四音节 vs Tripod 两音节），与 i2021-07-30 五步算法互链为「减法哲学」档案对；公开 gist 全文转载与镜像底本逐字一致（Ashlee Vance 传记亦收录）。**d2021-11-26** Raptor「破产警报」信——"the Raptor production crisis is much worse than it had seemed a few weeks ago… There is no way to sugarcoat this" + "a genuine risk of bankruptcy if we can't achieve a Starship flight rate of at least once every two weeks next year"；兑现注脚：每两周一飞未兑现（IFT-1 迟至 2023-04-20，见 e2019-09-28），破产未发生（两年半后塔架捕获 p2024-10-13）；Newsweek 版引句一处逗号异文照录。
- **两份 SEC EDGAR 文书入册（引文全部逐字取自 EDGAR 原文，备案号在册）**：**d2010-01-29** Tesla Form S-1（IPO 招股书，备案号 0001193125-10-017054）——商业模式总纲 + 首份「关键人风险」因子（Musk/Straubel 无固定期限雇佣协议）+ 资产负债实况（累亏 2.364 亿美元），与 e2010-06-29 IPO 条目互链；**d2022-02-07** Tesla Form 10-K FY2021（备案号 0000950170-22-000796）——"highly dependent on the services of Elon Musk, Technoking of Tesla and our Chief Executive Officer"，与 S-1 同名风险因子跨十二年对照（头衔玩梗进入监管文本），与 d2024-04-29 薪酬再批互链。
- **计划候选盘点**：Master Plan 系列查缺——Part 1（d2006-08）/ Part Deux（d2016-07-20）/ Part 3（d2023-04-05）/ Part IV（d2025-09-01）四份已全在册，无缺；SpaceX「官方更新信」以 email 库两封全员信落位；xAI 无 SEC 备案（私营公司），Series E 官方公告已在册（d2026-01）。
- **口径与互链同步**：documents.html og:description 与 doc-path 导读（中英双语）改写为十八份版；reading.html「十四份一手文档」升「十八份」；四份新词条互链 10 处（e2010-06-29/e2019-09-28/i2021-07-30/p2024-10-13 与 d2006-08/d2010-01-29/d2022-02-07/d2022-10-27/d2022-11-16/d2024-04-29 等站内锚）。
- **检索断言同步**：tools/build-search-index.py 一手文档断言 14→18，索引 267→271 条（109+18+42+31+5+53+4+9）。
- **版本三件套**：8.5.0→8.6.0（VERSION/app.js/14 页 span，替换计数打印在案）。

**质量门**
- verify.py 9 项全绿（37 页/索引 271）；node --check 通过；CDP 探针全过（四新卡渲染/结构五件套/Permalink 18 对/双语 data-en/页内互链目标存在性/390 无溢出/检索命中）；EPUB 重跑（24 章）。纯本地提交，不推送。

## v8.5.0 — 2026-10-01 · V9-20 R05/20：访谈扩充 II（Lex 候选消化 + 官方转写新批次）

**主题包成果（V9-20 R05 · 访谈 37 → 42 条）**
- **计划必做项完成——Lex 候选全部消化入册（V8 R06 已核实引语，本轮补立条目）**：**i2021-12-28-2**「给生命本身买保险」（Lex #252 文明与火星段）——霍金每世纪 1% 文明终结概率 + "life insurance for life" 名句 + "foundationally, I love humanity" 收束信条，文明灭绝「bang or a whimper」两种方式（人口崩溃是呜咽/三战是巨响）入编者注；**i2023-11-10-2**「言论自由的试金石」（Lex #400）——"Free speech only matters if people you don't like are allowed to say things you don't like"（官方逐字稿 01:43:13 段）+ "what is the worst thing that happened on Earth today" 媒体批评（02:02:38 段，V8 R06 留档段一并落实）。
- **三条新场次入册（elonmuskarchive.org interview 库官方转写，全部 transcript 直读）**：**i2013-02-27** TED2013「一枚完全且快速可复用的火箭」——SpaceX 目标宣言 + 航天飞机十亿美元/次对比；"rapidly and fully reusable" 十一年后由塔架接住兑现（页内互链 i2024-10-13）；**i2014-09-25** Code Conference 2014「火星宪法草案」——直接民主/废法比立法易/日落条款（60% 立法、40% 可废），与 2025 America Party 纲领互链 x-posts.html#p2025-07-05；**i2018-08-15** MKBHD Talking Tech「我们不花一分钱广告费」——口碑哲学 + "I actually even pay full retail price for my own cars"，2.5 万美元车「三年之约」未兑现入承诺档案注（promises.html#promises-s4）。
- **甄别与留档（EXPANSION.md 详录）**：TED2013 官方转写中**无**「I would like to die on Mars」句——存量无 id 条目「die on Mars」（约 2013 广泛征引）维持原标注不动，新 i2013-02-27 条目独立锚定官方转写，两不相扰；Acquired 播客镜像库 0 条目、官网 11 页单集列表抽查无 Musk 本人出场（公司史叙事播客，主角非其本人），不构成第一手信息，留档不立条；Lex #438（2024-08 Neuralink 团体访谈）转写在档本轮不立，入候选池。
- **检索断言同步**：tools/build-search-index.py 访谈断言 37→42，索引 262→267 条（109+14+42+31+5+53+4+9）。
- **版本三件套**：8.4.0→8.5.0（VERSION/app.js/14 页 span，替换计数打印在案）。

**质量门**
- verify.py 9 项全绿（37 页/索引 267）；node --check 通过；CDP 探针全过（五新卡渲染/六件套/Permalink 42 对/双语/页内互链目标存在性/390 无溢出/检索命中）；EPUB 重跑。纯本地提交，不推送。

## v8.4.0 — 2026-10-01 · V9-20 R04/20：访谈扩充 I（镜像官方转写批次）

**主题包成果（V9-20 R04 · 访谈 33 → 37 条）**
- **四条访谈入册（全部以 elonmuskarchive.org interview 库官方转写为逐字锚，transcript 全文存档 qa/v9-20/round-04/sources/）**：**i2016-06-01** Code Conference（与 Kara Swisher/Walt Mossberg）「仿真论证」段——"There's a one in billions chance that this is base reality" + 两个选项句，本人转发推文 x-738470842695176192（snowflake 2016-06-02 20:42 UTC）佐证；**i2020-03-09** SATELLITE 2020 开幕 Keynote——天文界之问的 "Zero impact whatsoever… Zero" 双零承诺 + "fully and rapidly reusable rocket"，Business Insider 报道印证；**i2021-07-30** Everyday Astronaut 星舰基地巡礼三部曲（拍摄日锚）——"a factory is underrated and design is overrated" + 五步算法完整版逐字（EA 官网文章 2021-08-11 变体 "manufacturing is underrated" 已注明，以镜像转写为准）；**i2024-09-08** All-In Summit——"The government is the DMV at scale"（**V8 R07 弃收件重验入册**：原单源 podcastnotes 笔记之外新增镜像官方转写 53,865 字符逐字，双源成立；日期口径以镜像库锚 2024-09-08 为准，EXPANSION 旧记 09-09 已注明）。
- **采料管线升级**：发现镜像站 interview 类型库（161 条，2003 起全收录，含 transcript 端点 /agents/transcript/{id}），四场候选三场直接命中；「Kara Swisher Recode Decode 2018-11-02」镜像所存为主播事后复盘（全程间接转述，无本人逐字），Vox 原文与本机均不可达（vox.com 超时、recode.net 500、web.archive.org 超时）——**弃收留档 EXPANSION**，重验条件注明。
- **检索断言同步**：tools/build-search-index.py 访谈断言 33→37，索引 258→262 条（109+14+37+31+5+53+4+9）。顺带增强：访谈 ctx 正则放宽为 `<p class="ctx[^>]*>` 以兼容带 data-en 属性的版式，17 张卡（13 存量 + 4 新）此前恒空的 bg（背景句）字段全部补全——纯增强，非校验放宽，q/s/bg 三字段口径不变。
- **甄别与留档（EXPANSION.md 详录）**：Decode 2018 弃收（转写非本人逐字）；Code 2016 转写为字幕平面化（口吃从略、标点编者所加，卡内注明）；镜像库另存 2014/2021 Code Conference、MKBHD 2018 等 161 场官方转写，作为 R05 访谈扩充 II 的候选池。

**质量门**
- verify.py 9 项全绿（37 页/索引 262）；node --check 通过；CDP 探针全过（新卡渲染/六件套/Permalink 37 对/双语 data-en/页内互链/390 无溢出/检索命中）；EPUB 重跑。纯本地提交，不推送。

## v8.3.0 — 2026-10-01 · V9-20 R03/20：X 帖回捞 II（2022–2025 深水区）

**主题包成果（V9-20 R03 · X 帖 27 → 31 张）**
- **四张帖卡入册（全部经 elonmuskarchive.org Agent API 精确短语检索逐字直读 + snowflake 解码对表，镜像日期与解码 UTC 全部同日）**：**p2023-11-30**「First Cybertruck deliveries in 2 hours!」——跳票四年兑现时刻，同日致谢帖（Massive congrats…I love you）一并存证，互链账本 e2023-11-30；**p2024-01-30**「Never incorporate your company in the state of Delaware」——特拉华衡平法院撤销 2018 薪酬包当日怒斥，01.31 投票帖与 02.01「The public vote is unequivocally in favor of Texas!」两帖逐字在档，弧线闭合于账本 e2024-06-13（股东大会重批+迁册德州）；**p2024-07-13**「I fully endorse President Trump and hope for his rapid recovery」——**V8 弃收件重验入册**（计划指定项），snowflake 解码显示距巴特勒枪响约 34 分钟，America PAC/出资/集会弧线注齐，卡内直通 p2025-07-05；**p2025-07-05** America Party 建党宣言三段全文（2:1 投票、one-party system、give you back your freedom），前情 06.30 预告帖与 07.04 独立日投票帖镜像逐字在档，07.07 Tesla 股价计价（Reuters）。
- **采料管线适配深水区**：清单管线（/agents/index 按年按月）在 2023–2025 大量触及单次 1000 上限（2024 全年 12 个月全满，12 月仅覆盖至 12-12），本轮确立深水区以 /agents/search 精确短语检索为主路径（六组短语全命中，total 精确），清单数据保留用于 2022 年全量（5,063 帖完整）。检索证据与 10 帖 transcript 存档 qa/v9-20/round-03/sources/（清单工作副本 _tmp_r03/ 不入库）。
- **帖墙小结增补**：章末编者提炼补政治维度（「并在 2024 年中之后变成政治武器——背书、决裂、建党」，EN/中文同步）。
- **检索断言同步**：tools/build-search-index.py X 帖断言 27→31，索引 254→258 条（109+14+33+31+5+53+4+9）。
- **甄别与留档（EXPANSION.md 详录）**：Grok 3 发布帖不立卡（账本 e2025-02-18 已覆盖同日两帖，页卡不重复）；Grok 3 免费/OpenAI 关系帖入候选池；2024-01-30 建议注册地帖（Nevada 变体）未单独检索到逐字、以 01.31 投票帖替代；2025 帖量巨大（年 12,000+ 触上限），2025-12 段未完整覆盖已注明。

**质量门**
- verify.py 9 项全绿（37 页/索引 258）；node --check 通过；CDP 探针全过（新卡渲染/时序/五件套唯一/Permalink 31 对/双语/年份分组/互链/390 无溢出/检索命中）；EPUB 重跑。纯本地提交，不推送。

## v8.2.0 — 2026-10-01 · V9-20 R02/20：X 帖回捞 I（2020–2021）

**主题包成果（V9-20 R02 · X 帖 23 → 27 张）**
- **四张帖卡入册（全部经 elonmuskarchive.org 新 Agent API 逐字直读 + snowflake 解码对表）**：**p2020-04-29**「FREE AMERICA NOW」（禁足令怒吼→5.11 违令复工→得州南迁序章，卡内互链 p2020-03-06 疫情弧线）；**p2021-01-26**「Gamestonk!!」（散户逼空助燃帖，「账号即市场变量」实证）；**p2021-05-05**「Starship landing nominal!」（SN15 首次完好着陆，四连炸迭代路线正名）；**p2021-11-02** Hertz 对冲四段全文——**V8 弃收件重验入册**（万亿市值日泼水帖，第三句「same margin as to consumers」首次入册，卡内互链账本 e2021-10-25）。
- **采料管线升级**：镜像站 Agent API（免钥无限流）全量回捞 2020 年 3,359 帖 / 2021 年 3,111 帖，精确短语检索取代旧 span 分页直读；V8 R08「镜像早期覆盖率有限」的判断随之作废。来源证据（四帖 transcript JSON + snowflake 解码字段）存档 qa/v9-20/round-02/sources/。
- **存量错位修正（两处）**：①「2020」年份条此前错标为「2021」（p2020-03-06/p2020-05-01 两卡被归入 2021 组），本轮改正并补齐 2021 年份条；②「2023」年份条此前压在 p2022-12-18（2022.12.18 帖）之前——本轮归位。全站年份分组现与卡序逐卡一致（探针断言在案）。
- **检索断言同步**：tools/build-search-index.py X 帖断言 23→27，索引 250→254 条（109+14+33+27+5+53+4+9）。
- **甄别与弃收（EXPANSION.md 详录）**：Bitcoin 暂停购车帖（2021-05-12）镜像库三短语检索 0 命中——弃收待补；Trump 背书帖留 R03；「卖房系列后续」以 p2020-05-01 既有卡注弧线为准未另立卡。

**质量门**
- verify.py 9 项全绿（37 页/索引 254）；node --check 通过；CDP 探针 24 断言全过（新卡渲染/时序/年份分组/互链/双语/390 无溢出/检索命中）；EPUB 重跑。纯本地提交，不推送。

## v8.1.0 — 2026-10-01 · V9-20 计划启动（R01/20）：基建与前账收官

**主题包成果（V9-20 R01 · 新计划第一轮）**
- **V8 R10 收尾入账**：v8.0.0 口径总核对（索引 250）与生成器全家桶幂等重跑已在上一提交完成；V8-PROGRESS.md R10 行回填 complete 并注明「本地完成，待用户推送」。
- **V9-20 计划基建**：新建 `V9-20-PROGRESS.md`（基线快照 + 20 轮状态表 + 恢复指引），本计划 20 轮三大目标：①第一手信息继续扩充（X 帖回捞/访谈/文档/演讲/事件聚合/语录卡补齐，R02–R09）；②新建「开源社区马斯克相关网站与资源」板块（resources-data.py 单一事实来源 + 静态资源页，外链不构成运行时依赖、file:// 离线可读，R10–R14）；③美术升级（设计系统 tokens/首页/数据图形/排版/动效，R15–R19）。
- **运行纪律**：本计划纯本地模式——每轮本地提交，绝不 push；`.v9run.lock` 锁机制就绪并已入 .gitignore；每轮版本步进 R01=v8.1.0 → R20=v10.0.0。

**质量门**
- verify.py 9 项全绿（37 页/索引 250/版本 8.1.0 一致）；EPUB 重跑。

## v8.0.0 — 2026-10-01 · V8 扩充（10/10）收官：全站验收（本地版）

**主题包成果（V8 R10 · 发布节点，本地完成待用户推送）**
- **口径总核对**：检索索引 250 条 = 言行实录 109 + 一手文档 14 + 访谈与表态 33 + X 帖 23 + 争议深读 5 + 编年史 53 + 财务全景 4 + 事件档案 9；37 个 HTML 页面；账本时间轴 109 节点；语录卡 96；事件档案 9 档 37 材料。
- **生成器全家桶幂等重跑**：build-events / build-timeline-events / build-network / build-company-files / build-capital / build-ledger-links / build-search-index / sync-changelog / build-revisions / build-epub 全部通过；修订史 179 锚点；EPUB 24 章 201,489 字节。
- **版本节点**：VERSION / app.js SITE_VERSION / 14 页 site-version-val 三件套同步 7.9.0 → 8.0.0（替换计数 14 打印在案）。
- **本版为 V8 计划（10 轮）收官**：账本 67 → 109 条、文档 14、访谈 33、X 帖 23、语录卡 54 → 96、索引 178 → 250。下一计划 V9-20（20 轮：第一手信息回捞 + 开源社区资源板块 + 美术升级）自 v8.1.0 起步，详见 V9-20-PROGRESS.md。

**质量门**
- verify.py 9 项全绿；node --check（app.js + cite.js）通过；EPUB 重跑。本轮按用户指令仅本地提交，不推送。

## v7.9.0 — 2026-10-01 · V8 扩充（9/10）：SpaceX / Neuralink / xAI 官方演讲与 demo

**主题包成果（V8 R09 · 账本 103 → 109 条）**
- **六条账本条目入册（官方发布会/demo/演讲逐字，镜像与媒体双源核验）**：
  **e2017-09-29** IAC 2017 阿德莱德 BFR（「space-faring civilization」句，Business Insider 逐字 + SpaceX 官方视频；互链 e2016-09-27/e2022-02-10）；
  **e2019-07-16** Neuralink 2019 发布会（「A monkey has been able to control a computer with his brain.」CT Insider/Mashable 双源；互链 e2021-04-09/e2024-01-29）；
  **e2020-08-28** Gertrude 猪演示（「a Fitbit in your skull with tiny wires」TechCrunch/Globe and Mail 双源）；
  **e2021-04-09** Pager MindPong（镜像回帖逐字「Sure.」「Hopefully, later this year.」status/1380314267077894148+1380314485324308482，snowflake 00:19 UTC；媒体记录转发语「literally playing a video game telepathically」CNBC/CNET）；
  **e2022-02-10** Starbase 星舰更新（「I feel, at this point, highly confident that we'll get to orbit this year.」Space.com 逐字——IFT-1 实际晚十四个月，「lose a few vehicles」字面兑现；互链 p2024-10-13）；
  **e2025-02-18** Grok 3 发布（镜像逐字两帖：「Grok 3 presentation starting shortly.」03:59 UTC +「the world's smartest AI」19:29 UTC；互链 p2023-11-04/grok.html）。
- **检索索引 244 → 250 条**（言行实录 103→109）；页顶时间轴重建 109 节点；index.html 计数文案 103→109 ×3 处（含 data-en）。
- **查重勘定**：IAC 2016（e2016-09-27/i2016-09-27）、Starship Mk1（e2019-09-28）、xAI 官宣（e2023-07-12）、xAI 收购 X（e2025-03-28）已在册，本轮不重复立条。
- **甄别记录（宁缺毋滥）**：①Starship 2022 发布会 Spaceflight Now/Everyday Astronaut 无直引，靠 Space.com（Mike Wall）逐字立条；②Neuralink 2020 TechCrunch 原文 URL 已 404，Fitbit 句以检索摘要多源核对收录；③Grok 3 直播内容逐字不可得，条目只收帖文第一手，「smartest AI on Earth」的现场口号版未采；④Neuralink JMIR 论文（d 条目候选）jmir.org 本机不可达，文档馆本轮不动。
- **工程备注**：primary.html 行尾已转 LF（与既往 CRLF 惯例不同），集成脚本改为自适应行尾；逐卡结构断言（4 ps-sec/1 quote/1 zh/1 permalink/1 src）全过。

**质量门**
- verify.py 9 项全绿；node --check（app.js + cite.js）通过；EPUB 重跑。
## v7.8.0 — 2026-09-30 · V8 扩充（8/10）：X 帖史扩容 · 十帖入册

**主题包成果（V8 R08 · x-posts.html 13 → 23 张）**
- **十张帖卡入册（逐字全部经 elonmuskarchive.org 镜像详情页直读核验，status ID 经 snowflake 解码对表日期）**：
  **p2020-03-06**「The coronavirus panic is dumb」（CNBC/Reuters 双源）；
  **p2020-05-01**「卖掉几乎所有有形财产」+「Tesla stock price is too high imo」相隔一分钟两连发（互链 i2020-05）；
  **p2022-03-26**「de facto public town square」——收购案公开起点（引用嵌套完整存档，含 3.25 投票原帖）；
  **p2022-04-14**「I made an offer」三个字要约帖（互链 i2022-04-14/d2022-04-25/px-0414）；
  **p2022-05-13**「temporarily on hold」spam 之争引线（互链 d2022-10-27）；
  **p2022-11-01**「lords & peasants…Blue for $8/month」定价宣言；
  **p2022-12-18**「Should I step down…」辞职投票（57.5%/1750 万票，Reuters/BBC/CNBC）；
  **p2023-07-23**「bid adieu to the twitter brand」更名宣言两连发（互链 px-0723）；
  **p2024-04-05**「Tesla Robotaxi unveil on 8/8」一句话预告（互链 e2024-04-23/promises）；
  **p2025-03-28**「@xAI has acquired @X」全股票收购官宣（互链 e2025-03-28）。
- **交叉引用**：platform-x px-0414/px-0723 sv-links 各补帖史直链；多卡互链账本/文档/访谈锚点。
- **检索索引 234 → 244 条**（X 帖 13→23）。
- **甄别记录（宁缺毋滥）**：Hertz 对冲推文（2021-10-26）镜像站无存档且站内记忆措辞存疑，弃收；「I endorse President Trump」（2024-07-13/14）镜像分页未命中原帖，弃收待后续补；web.archive.org 本机 TLS 中断不可用，已删帖核验全部改走 elonmuskarchive.org 镜像（status ID=归档路径，详情页直读=逐字锚）。

**自主优化**
- 工具脚本 tools/r08-snippet.html + tools/r08-integrate.py（10 卡结构断言+时间序分组插入）+ tools/r08-xlinks.py（交叉引用断言）。

**质量门**
- verify.py 9 项全绿；node --check（app.js + cite.js）通过。
## v7.7.0 — 2026-09-30 · V8 扩充（7/10）：长访谈 II · Rogan / TED / DealBook

**主题包成果（V8 R07 · interviews.html 26 → 33 条）**
- **七条长访谈条目入册（引语逐字取自逐字稿或官方转录，关键处两源印证）**：
  **i2017-04-28** TED 2017 温哥华「最摧残灵魂的东西，是堵车」+「It's maybe two or three percent」的爱好自陈（ted.com 官方逐字稿）；
  **i2018-09-07** JRE #1169 大麻卷烟时刻——次日 Guardian/CNBC 报道股价跌约 6%、两位高管辞职，六周后 SEC 起诉（互链 e2018-08-07 / e2018-09-27）；
  **i2018-09** JRE #1169「AI 一定会被用作武器」+「超出人类控制」（全文逐字稿在档，互链 AI 战略布局）；
  **i2020-05-07** JRE #1470「文明现在看起来很脆弱」+「What's that? I never heard of it.」疫情冷面段（Rev.com 官方逐字稿，互链 e2020-05-11）；
  **i2020-05** JRE #1470「Mars or a house? I'm like Mars.」——卖房宣言的时间经济学（Rev.com 官方逐字稿）；
  **i2022-04-06** TED Giga Texas 开幕前夜「人口崩溃是文明最大的威胁之一」+ curiosity/consciousness 动机自述（ted.com 官方逐字稿，互链 i2022-04-14）；
  **i2024-11-04** JRE #2223 大选前夜「If Trump doesn't win, this is the last election.」——多家转写出入如实注明（Musixmatch 逐字稿 + Mediaite/The Spectator 记录）。
- **检索索引 227 → 234 条**（访谈 26→33）；期数/日期勘定：JRE #1169=2018-09-07、#1470=2020-05-07、#2223=2024-11-04（jrelibrary 官方口径）；TED 2017 场次=2017-04-28（TED Blog）。
- **甄别记录（宁缺毋滥）**：All-In Summit 2024（2024-09-09 LA）无第二媒体直引源，弃收；JRE #2054（2023-10-31）逐字稿不可达且媒体仅转述，弃收；DealBook 2023「滚蛋」名句已在册 i2023-11-29；「I'm fucked / 监狱刑期」名句出自 Tucker Carlson 访谈（2024-10-07）而非 Rogan，已记录防止误引。

**自主优化**
- 工具脚本 tools/r07-snippet.html + tools/r07-integrate.py（唯一性断言 + CRLF 统一）+ tools/r07-spans.py（版本步进断言 14）。

**质量门**
- verify.py 9 项全绿（37 页，索引 234）；node --check（app.js + cite.js）通过；EPUB 重跑含最新条目。
## v7.6.0 — 2026-09-30 · V8 扩充（6/10）：长访谈 I · Lex Fridman 四期

**主题包成果（V8 R06 · interviews.html 18 → 26 条）**
- **八条 Lex Fridman 访谈条目入册（引语逐字取自逐字稿，关键句两源印证）**：
  **i2019-04-12** #18「两吨重的死亡机器」+「像马一样有用」（ZDNet/CleanTechnica 印证）；
  **i2019-04** #18「What's outside the simulation?」——#400 官方逐字稿回溯印证；
  **i2019-11-12** #49「打不过，就加入」+ Dumb and Dumber 现场 + AI 监管机构呼吁（Rev.com 官方逐字稿 PDF）；
  **i2019-11** #49 淡蓝点时刻：读萨根读到一半当场反驳「This is false, Mars」；
  **i2021-12-28** #252「物理是法律，其余都是建议」+ 公理基础方法论（PodScript 全文逐字稿，转写出入如实注）；
  **i2021-12** #252「金钱是信息」+ 荒岛归谬 + 货币数据库（PodcastNotes 印证）；
  **i2023-11-10** #400「病态乐观」+「我对 Autopilot 实在太乐观了」（lexfridman.com 官方逐字稿）；
  **i2023-11** #400 speciesist/Team Robot + OpenAI 起源内幕（Business Insider/Observer 印证）。
- **交叉引用**：promises.html s4 模式注 + s5 第一手记录清单补 i2023-11-10（「病态乐观」当事人自认）；ai-strategy.html 捐资者岁月补 i2023-11（OpenAI 起源）。
- **检索索引 219 → 227 条**（访谈 18→26）；四期正确期数勘定：#18（2019-04-12）/ #49（2019-11-12）/ #252（2021-12-28）/ #400（2023-11-10），同日第二条沿用月份级 ID 先例（i2006-08/i2018-04 同款）。

**自主优化**
- 工具脚本 tools/r06-snippet.html + tools/r06-integrate.py（唯一性断言 + CRLF 统一，r04 修好版模式）。

## v7.5.0 — 2026-09-30 · V8 扩充（5/10）：财报电话会 II（2019–2026）

**主题包成果（V8 R05 · primary.html 93 → 103 条）**
- **十条财报电话会条目入册（引语逐字取自逐字稿，关键句两源印证）**：
  **e2019-04-24** Q1 2019「斯巴达饮食」与「强制函数」——八天后 23→27 亿美元增发（Reuters「ends Spartan diet」印证）；
  **e2020-01-29** Q4 2019 Cybertruck 需求「难以置信」+ FSD「几个月 feature complete」（Fortune 当日印证）；
  **e2020-07-22** Q2 2020 FSD「年底前完成」+「一场『九』的长征」；
  **e2022-01-26** Q4 2021 Optimus 首获财报会排位：「有潜力比汽车业务更重要」（CNN Business 印证）；
  **e2022-10-19** Q3 2022「比 Apple 与沙特阿美加起来还值钱」（Business Insider 印证，合计约 4.4 万亿美元语境）；
  **e2023-10-18** Q3 2023 Cybertruck「我们给自己挖了坟」+「原型到量产难 10,000%」（TechRadar 印证）；
  **e2024-04-23** Q1 2024 Robotaxi 8/8 之约 + Optimus「年内工厂做有用任务」（Seeking Alpha 印证；8/8 后顺延至 10.10）；
  **e2024-10-23** Q3 2024「全球最有价值公司，遥遥领先」+ Cybercab 2026 量产（Investopedia/Fortune 印证，次日 +22%）；
  **e2025-04-22** Q1 2025「五月起 DOGE 时间大幅减少」（The Hill 印证）；
  **e2026-07-22** Q2 2026「Optimus 会是有史以来最大的产品」+ 里程周增 10%——账本 2026 年首条。
- **quotes.html +10 卡（80→90）**；index.html 计数文案 93→103 ×5；EXPANSION.md 补 R05 入包块（含十场逐字稿链接与甄别注）。
- **管线**：build-ledger-timeline（103 节点）/ build-search-index（断言 93→103，索引 209→219）/ build-epub 重跑。

**质量门**
- verify.py 9 项全绿；来源留档见 V8-PROGRESS.md「核实来源留档（R05）」节。

## v7.4.0 — 2026-09-30 · V8 扩充（4/10）：财报电话会 I（2013–2018）

**主题包成果（V8 R04 · 账本 primary.html 83 → 93 条）**
- **账本 +10 条（9 条财报电话会 + 1 条推文前史，逐字均直读逐字稿/多源印证）**：
  e2016-02-10 Q4 2015 call（Model 3 发布预告：「really well-received, getting into production and delivery at the end of next year」）；
  e2016-05-04 Q1 2016 call（供应商契约式承诺：「volume production capability … July 1st next year」+ 下半年 10–20 万辆目标，2017 实产 2,685 辆落差约 50 倍）；
  e2016-08-03 Q2 2016 call（Joshua Brown 事故后首个 call：「full autonomy is gonna come a hell of a lot faster than anyone thinks」+「hardware exists」口径 +「35,000 automotive deaths」反问）；
  e2016-10-26 Q3 2016 call（solar roof 周五发布预告 +「SolarCity to be approximately cash neutral, next year」）；
  e2017-02-22 Q4 2016 call（500,000 vehicles next year + 1 million by 2020 预测 +「We anti-sell the Model 3」，2018 实交 245,240）；
  e2017-08-02 Q2 2017 call（「when I said manufacturing hell and supply chain hell on Friday, I meant it」+ 2018 年底周产 10,000 预测 + S-curve 金句）；
  e2017-11-01 Q3 2017 call（Jonas「How hot is it in hell?」→「We were in level 9. We're now in level 8」+ 电池模组线瓶颈点破）；
  e2018-04-13 自动化认错推文（「excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated.」· Gadgets360/The Guardian 印证，作为 Q1 call flufferbot 展开段的前史入册）；
  e2018-05-02 Q1 2018 call（「Boring, bonehead questions are not cool. Next」+ 转 YouTube + flufferbot 故事 · BBC/Slate/The Verge 三源）；
  e2018-08-01 Q2 2018 call（「I'd like to apologize for being impolite on the prior call … There's no excuse for bad manners」· Business Insider/Bloomberg，funding secured 六天前）。
- **quotes.html 核实卡 +10（70→80）**：每条新账本引文块逐一对卡；
- **管线**：build-ledger-timeline（时间轴 93 节点）/ build-search-index（断言 83→93，索引 194→209）/ build-revisions / sync-changelog / build-epub 全部重跑；index.html 计数文案 83→93 ×5；
- **甄别记录（宁缺毋滥）**：①Q4 2013 call（2014-02-19）Gigafactory 表述全为「下周官宣再谈」的推迟口径，无出彩逐字，弃；②Q2 2016 call Autopilot 辩护各家转述不一（「more deaths」「50%」均无稳定逐字），改以逐字稿直读的 full autonomy/hardware 句立条；③Q3 2017「level 9→level 8」采用 stockanalysis.com（Quartr）转写并以 MediaPost「one to nine」与 CNBC「deep in production hell」双源印证；④「manufacturing hell and supply chain hell on Friday」按转写照录，并在条目内注明台上原话为「production hell」（两场合措辞差异如实呈现）。
- 来源留档：V8-PROGRESS.md「核实来源留档（R04）」节。

**质量门**
- verify.py 9 项全绿；node --check app.js/cite.js 通过。

## v7.3.0 — 2026-09-30 · V8 扩充（3/10）：SEC EDGAR 公文扩容

**主题包成果（V8 R03 · documents.html 9 → 14 份）**
- **五份 SEC EDGAR 一手文书入册（引文全部逐字取自 EDGAR 原文，备案号在册）**：
  **d2018-08-14** Tesla 8-K 私有化特别委员会公告（Item 7.01 + Ex-99.1，0001564590-18-021585）——「尚未收到任何正式提案」，funding secured 一周后的监管口径急刹车；
  **d2022-04-11** Twitter 8-K/A 董事会提名五日始末（0001193125-22-101041）——4.04 邀请、4.09 辞谢、4.11 备案，收购案第一份正式法律文书；
  **d2022-07-26** Twitter DEFM14A（0001193125-22-202163）——4.13 要约信全文（含「My offer is my best and final offer」）+ Background of the Merger 逐日大事记（9.2% 曝光→毒丸→融资承诺→4.24-25 董事会放行）；
  **d2022-10-27** Twitter 最后一份 8-K（0001193125-22-272772）——交割完成、九董事列名离任、「马斯克成为唯一董事」、NYSE 摘牌（Form 25→15 档案定格）；
  **d2024-04-29** Tesla DEF 14A（0001104659-24-053333）——Tornetta 判决后 2018 奖励再批 + 迁州德州双议案（含 2.04/2.10 董事会程序内幕、proxy 引用的马斯克 X 帖与董事长署名信）。
- **交叉引用**：platform-x.html px-0414 补 d2022-04-11/d2022-07-26 两链、px-1028 补 d2022-10-27；promises.html 2018 私有化案 sv-links 与来源列表各补 d2018-08-14；documents.html d2022-04-25 词条补 d2022-07-26 站内链；reading.html「九份一手文档」升「十四份」；doc-path 导读链改写为十四份版（中英双语）。
- **管线**：build-search-index（断言 9→14，索引 194→199）/ build-epub 重跑；账本未动（时间轴/语录卡/EPUB 新鲜度不受影响）。

**质量门**
- verify.py 9 项全绿；来源留档见 V8-PROGRESS.md「核实来源留档（R03）」节（六份 EDGAR 索引页+正文直读，表决结果多源印证）。

## v7.2.0 — 2026-09-30 · V8 扩充（2/10）：Twitter 收购案私信原件

**主题包成果（V8 R02 · 特拉华衡平法院披露件）**
- **账本 +9 条（74→83）**：Twitter, Inc. v. Musk（Del. Ch. C.A. No. 2022-0613-KSJM）2022 年披露的私信逐字件——e2022-03-26 Dorsey 劝进（「could def help in immeasurable ways」）、e2022-04-05 Dorsey 祝贺入董事会（「Parag is an incredible engineer. The board is terrible.」）、e2022-04-09 Musk↔Agrawal 决裂（「What did you get done this week?」/「I'm not joining the board. This is a waste of time.」+ 同日 Kimbal「no throat to choke」Plan B）、e2022-04-16 Lonsdale 转达 DeSantis（政治入场）、e2022-04-20 Ellison 一小时承诺 10 亿美元（「Roughly what dollar size?」）、e2022-04-22 Gates 空头对峙（Musk 自晒件 · CNBC/BI 印证）、e2022-04-25 签署日拒 SBF（「Blockchain Twitter isn't possible」）、e2022-04-26 Dorsey 斡旋收尾（「too critical to humanity」/「At least it became clear that you can't work together」）、e2022-06-28 「Your lawyers are using these conversations to cause trouble」（BI/Economic Times 披露）；
- **quotes.html 核实卡 +9（61→70）**：每条新账本引文块逐一对卡；
- **交叉引用**：platform-x.html 阶段一补两处账本链接（px-0414 要约 → e2022-04-09 私信；px-0425 协议 → e2022-04-25 SBF 拒绝信）；index.html 三处「74 条」计数文案升 83；
- **管线**：build-ledger-timeline（时间轴 83 节点）/ build-search-index（断言 74→83，索引 185→194）/ sync-changelog / build-epub 全部重跑；
- 来源留档：V8-PROGRESS.md「核实来源留档（R02）」节（TIME/BBC/Guardian/WaPo/Gizmodo/CNBC 全文转载 + 案号 C.A. No. 2022-0613-KSJM；Gates 短信为 Musk 2022-04-22 自晒件）。

## v7.1.0 — 2026-09-30 · V8 扩充（1/10）：funding secured 案（SEC v. Musk）

**主题包成果（V8 R01 · 第一手信息扩充计划启动轮）**
- **账本 +7 条（67→74）**：SEC v. Musk（S.D.N.Y. No. 1:18-cv-08865）完整法庭弧线，逐条 SEC/CourtListener 第一手锚点——e2018-09-27 起诉（诉状第 3 段逐字 + 新闻稿 2018-219）、e2018-09-29 和解（新闻稿 2018-226 条款全文 + 10/16 Final Judgment）、e2018-12-09 60 Minutes「I do not respect the SEC」（四源印证）、e2019-02-19 产量推文（SEC 函件 Dkt.18-2 引述两条推文全文 + 藐视动议/show cause 令）、e2019-04-30 修正终审判决（Dkt.47/48 逐字，藐视战终结）、e2022-03-08 终结动议（Dkt.70-72 + SEC「a deal is a deal」反对简报 + Liman 2022-04-27 驳回）、e2023-05-15 第二巡回维持（Summary Order 22-1291 逐字 + Fair Fund 分发收尾）；
- **quotes.html 核实卡 +7（54→61）**：每条新账本引文块逐一对卡；
- **交叉引用**：controversy.html#sec-sec「结果」段补法庭弧线入口并把「暂作参考记录」的 60 Minutes 引语转正链接账本 e2018-12-09；promises.html 第 03 案来源列表补 e2018-09-27–e2023-05-15 一行；index.html 三处「67 条」计数文案升 74；
- **管线**：build-ledger-timeline（时间轴 74 节点）/ build-search-index（断言 67→74，索引 178→185）/ build-revisions / build-epub 全部重跑；
- 来源留档：V8-PROGRESS.md「核实来源留档（R01）」节（SEC 官网 / CourtListener / RECAP 公开件 / 四源媒体印证）。

## v7.0.0 — 2026-09-30 · V7 改版（19/19）：全站验收、交接与发布 🎉

**收官条目（V7-19 第 19 轮 · 最终轮）——「马斯克商业志 MUSK, INC.」v7.0 正式发布**

- **全站终检（新探针 r19-final.js，11/11 全过）**：数量口径（37 页 / 账本 67 / 事件档案 9 / 检索索引 178 / 导航五组）· 390px 主路径「首页→2008 专题→事件档案→账本来源→检索」五步全通且锚点在视口 · EN 争议页正文英文 · file:// 离线首页渲染+导航+JS 标记；
- **口径漂移修正（本轮实测发现）**：时间轴独立记录 151→160 的漂移由 R15 检索扩容引入——events.html 的事件档案索引记录混入一手材料记录池，致同一事件被「档案+材料」双重表达；build-timeline-events.py 补 pg 过滤并注明理由，151 独立 / 18 吸收口径恢复，探针复验通过；
- **生成器幂等重建**：build-events / build-timeline-events / build-network / build-company-files / build-capital / build-ledger-links 全部重跑，产物一致；
- **站点地图**：新建 sitemap.xml（37 URL，GitHub Pages 基准地址，v7.0.0 lastmod）；
- **交接文档**：DEVLOG.md 追加「V7-19 十九轮改版」交接段（19 轮成果地图 / 数据单一事实来源清单 / 已知限制 / 续作指南）；
- **数量口径终值（v7.0.0）**：37 个 HTML 页面 · 账本 67 条 · 事件档案 9 个（材料关联 37 · 逐字引语 9）· 检索索引 178 条（169 一手材料 + 9 事件档案）· 时间轴 151 独立记录 + 18 吸收 · 公司档案 4 份+6 简介 · 资本流向 18 笔 · 承诺对账 5 案 · EPUB 24 章；
- verify.py 9 项全绿；CDP 终检 11/11；视觉升级自 R1 深色纪实封面起 19 轮截图留档（qa/v7-19/round-01…18 + 本轮）。

**发布**：升级分支 visual-v7-19rounds 全站验收通过后合入 main 并推送，GitHub Pages 部署验证以线上实际呈现为准（见 V7-19-PROGRESS.md 收官记录）。

## v6.23.0 — 2026-09-30 · V7 改版（18/19）：动效、无障碍与性能

**主题包成果（V7-19 第 18 轮 · 动效、无障碍与性能）**
- **全站审计（新探针 r18-probe.js，12/12 断言全过）**：①性能实测——条件为本机 headless Chrome + 127.0.0.1 静态服务器（无网络延迟，如实标注非真实网络分数），index/survival-2008/timeline/primary/search 五页 load 全部 <1500ms，首页最大资源 x-hq.jpg 196KB（明细 qa/v7-19/round-18/perf-log.txt）；②reduced-motion 模拟（CDP features 注入）——reveal 全部立即可见、首屏标题不依赖动画（app.js matchMedia 分支 + CSS 13 处 @media 块既有机制回归验证）；③键盘焦点——CDP Input.dispatchKeyEvent **真实 Tab 按键** 8 次逐个进入可交互元素（修正审计方法：合成 KeyboardEvent 不触发真实焦点移动）、:focus 规则 19 处在册；④对比度实测（WCAG 公式计算）——浅底次级文字与深底文字均 ≥4.5（AA）；⑤Esc 焦点恢复回归——资本流向图 Enter 开详情 → Esc 焦点归还（R10 机制正常）；
- **静态基线复核**：全站 20/20 img 均有 width/height（布局稳定）；加载策略正确（首页肖像 fetchpriority="high" 首屏优先、其余 19 张 loading 懒加载）；
- **本轮改动**：app.js/cite.js 全站 36 页挂载点加 defer（解析不阻塞、执行顺序保持）；changelog.html 无脚本引用为历史合理现状（静态日志页）不动；
- **站点零缺陷**：审计发现的 3 处问题均为探针自身方法问题（结构顺序/CDP API 更名/合成按键无效），逐一定位修正——此前 17 轮的无障碍与性能基础良好，本轮以实测留档为主；
- VERSION/app.js/14 页 span → 6.23.0；EPUB 重建。

**质量门**
- verify.py 9 项全绿（37 页，索引 178 条）；node --check（app.js + cite.js）通过；审计探针 12/12；实测数据留档 qa/v7-19/round-18/perf-log.txt。

## v6.22.0 — 2026-09-30 · V7 改版（17/19）：双语与全站统一

**主题包成果（V7-19 第 17 轮 · 双语与全站统一）**
- **全站双语审计（新工具 r17-scan.js）**：37 页 EN 模式逐元素扫描漏翻（区分设计意图豁免：译文并置块/语言按钮目标语言名/图注署名），首轮 385 类型→去重 130 模式→逐类修复；
- **系统性公共项清零**：skip-link「跳到主要内容」data-en（12 页）· 资料子导航 ps-nav 八项 data-en（12 页）· footer-brand 文本 span 包裹 data-en（14 页）· lr-toc-h 目录头（8 页）· 各页「← 返回网站主页 / Back to site」双语并列改纯 data-en；
- **页面级补漏翻**：controversy.html **五篇 22 段正文全量 data-en 英文**（pedo guy 诽谤案/SEC funding secured/Autopilot-FSD DMV 与 NHTSA 双线/工会 NLRB 六年战/Twitter 审核与 DSA 首罚，含第三至五篇 h2 与 ct-lead）· interviews.html 10 标题+10 语境段+12 徽标 · reading.html 长卷 **8 章 28 段全量 data-en** + 8 章节标 + 延伸阅读行 · platform-x/survival-2008/promises 深链与 SVG 轴标签 · 主要内容页 h1 data-en（12 页）· 各页页副题（sr/doc/iv/xp/my/ce/cy/fn/pr/sc sub）纯英文 data-en；
- **动态产物双语**：search.html 计数行/空结果/清除按钮/芯片计数 EN 感知（修复 srLang 作用域错误——原定义在子 IIFE 内致 EN 模式 render 抛 ReferenceError 检索完全失效，**探针抓出的真缺陷**）· timeline.html 年份选项双语（全部年份/按月，生成时读语言偏好）· timeline data-en 混排中文词修正 · grok h3 data-en 含 CJK 修正 · company-files-data.py 19 笔财务金额补 amount_en（data-en 美元记法）与 X 档案 name_en · build-events.py 材料标签双语渲染（ev-mat-plain 与链接均带 data-en）· capital-evolution 口径/来源与 companies 来源标签 data-en · changelog.html 页顶英文说明（开发日志以中文维护）；
- **已知限制（如实入册）**：capital-evolution 四时代正文、money/ai-strategy/grok 等深色页叙事正文与 changelog 条目正文仍以中文为主（正文层长尾；高频路径与全部结构性元素已双语）；changelog 页顶已加英文说明；
- VERSION/app.js/14 页 span → 6.22.0；EPUB 重建。

**质量门**
- verify.py 9 项全绿（37 页，索引 178 条）；node --check 通过；CDP 验收探针 **10/10**（EN 交互回归 4：检索命中行英文格式/空结果英文/时间轴年份选项/事件档案标题与材料标签 · 跨页语言保持 2：EN 状态跨 5 页跳转含返回首页 · EN 不破版 3：controversy/reading/promises 390px 英文长段无溢出 · 缓存往返 1：切回中文原文完整恢复）；截图 1 张（EN 争议页）人工复核；证据在 qa/v7-19/round-17/。

## v6.21.0 — 2026-09-30 · V7 改版（16/19）：手机全流程打磨

**主题包成果（V7-19 第 16 轮 · 手机全流程打磨）**
- **全站三视口扫描（体检工具 r16-scan.js）**：37 页 × 320/390/768 = **111 页视口组合**系统扫描横向溢出（逐元素定位溢出源）+ 390px 触摸目标抽查（按钮/芯片/引用等交互控件 ≥30×22px 基线）——首轮发现 5 处问题，修复后**复扫全绿（NO ISSUES）**；
- **修复 5 处**：① chronicle.html 320px 溢出 15px——编年史日期列 108px 网格在窄屏挤压，≤420px 断点改单列左对齐 + .cy-ev 断行；② companies.html 320px 微溢出 3px——关系行不可断内容，.net-li-main 等加 overflow-wrap: anywhere；③ supplychain.html 320px 溢出 21px——190px 标签列挤压，≤560px 断点单列 + .sc-v 断行 + 出处徽标收窄；④ timeline.html gx-fchip 触摸目标 20px 高——min-height: 28px（桌面同受益）；⑤ primary.html cite-btn 21px——min-height: 26px；
- **验收探针（r16-probe.js，17/17）**：三视口（320/390/768）**首页→专题→事件→来源完整链路走通**（每步无溢出 + 锚点定位 + 菜单开关）；锚点到达采用轮询断言（320px 布局稳定需 ~1.6s，浏览器自动重定位 hash）；hover-only 抽查（账本时间轴悬浮点为原生链接可点击定位、公司关系视图点击驱动）；菜单弹层可开可关不残留遮挡；320px 长标题（平台变局/承诺对账）不破版；
- VERSION → 6.21.0（无其他构建产物变化：无新事件/索引/EPUB 内容改动，EPUB 保持 141,940 bytes——verify 通过）。

**质量门**
- verify.py 9 项全绿（37 页，索引 178 条）；扫描复扫 111 组合零问题；CDP 验收探针 17/17（三视口链路 12 + hover-only 与弹层 3 + 320 长标题 2）；截图 2 张人工复核（390 账本锚点到达未被遮挡 / 320 平台专题长标题换行）；证据与扫描器在 qa/v7-19/round-16/。

## v6.20.0 — 2026-09-30 · V7 改版（15/19）：搜索与发现（质量节点：11–15 打通）

**主题包成果（V7-19 第 15 轮 · 搜索与发现）**
- **索引扩容与事件聚合字段**：`tools/build-search-index.py` 扩展——原 169 条一手材料记录全部保留（一条未丢），新增「事件档案」类型 9 条（events-data.py 单一事实来源：标题/摘要/关键事实入索引，公司名映射到索引实体口径），索引 **169→178 条**；每条被事件档案吸收的材料记录获得 `ev` 字段（与 build-timeline-events.py 吸收逻辑同源），供检索端事件聚合；
- **search.html 检索升级**：① **事件聚合条**——命中项若属于某事件，显示「◈ 事件聚合 · 属于事件档案 eXXX · 同事件另外 N 份材料 ▾」，展开列出该事件全部来源（账本/文档/原帖/专题，逐条深链）——**同一事件可展开多份来源**；② **命中解释**——每项显示「命中于：原话/摘要 · 出处 · 日期 · 背景 · 公司」标签，说明为什么搜到它；③ **URL 参数**——?q=&type=&co= 读写（replaceState），支持分享、返回与深链预填；④ **筛选状态行**——关键词/类型/年份区间/公司的完整组合描述 +「清除全部筛选」一键重置；⑤ 空结果提示升级（给替代关键词建议+指向清除按钮）；类型筛选组新增「事件档案」；
- **校验器如实扩展（保留原约束）**：verify.py 索引一致性检查由「七类锚点求和」扩展为「七类 + 事件档案锚点数」（events.html ev-item 动态取），178 = 67+9+18+13+5+53+4+9；原七类约束一行未动，事件档案为生成器产出的合法新增类型（理由：R6 起事件档案成为独立结构化内容类型，R15 将其纳入可检索范围）；
- **质量节点（第 11–15 轮连通）**：探针验证完整链路——专题（survival-2008）→ 事件档案 → 账本材料 → 建档卡回事件 → 检索命中事件档案与原话（案例 01「最后一枚火箭」）；中英文代表性查询各测（「圣诞夜」5 命中含聚合展开、「funding secured」命中 e2018-08-07）；
- **实测修复**：探针抓出 1 个真 HTML 缺陷——事件聚合条原渲染在 `<a class="sr-item">` 内部（button 嵌套 a 非法，浏览器拆开外层链接致结果计数错乱 36=9×4），已移出至链接外层兄弟节点；
- **样式**：style.css 增 .sr-hit / .sr-evline / .sr-evtag / .sr-evbtn / .sr-evmat / .sr-clear；
- VERSION/app.js/14 页 span → 6.20.0；EPUB 重建。

**质量门**
- verify.py 9 项全绿（37 页，索引 **178 条** 口径）；node --check 通过；CDP 真视口探针 **22/22**（基础 2 / 中文查询 5 含聚合展开 / 英文查询 2 / 事件档案入检索 2 / URL 参数与清除 4 / 质量节点链路 4 / 无 JS 1 / 390 1 / file:// 1）；截图 6 张人工复核；证据与 QA 记录在 qa/v7-19/round-15/。

## v6.19.0 — 2026-09-30 · V7 改版（14/19）：原始资料阅读体验

**主题包成果（V7-19 第 14 轮 · 原始资料阅读体验）**
- **复制引用组件 cite.js（新增，四资料页挂载）**：primary（账本 67 条）/ documents（9 篇文档）/ interviews（18 条有稳定 id 的访谈）/ x-posts（13 条帖卡）共 **107 个可引用单元**，每单元头部注入「复制引用 / Cite」按钮——引用文本含 标题 · 单元 id · 日期 · 出处行 · 所属页 · **稳定链接**（http(s) 下为完整 permalink，file:// 离线时如实标注「离线文件 文件名#锚点」）；引用语言跟随站内中英切换；无 id 的单元不注入（引用必须有稳定锚点，不造链接）；
- **复制三级退路**：clipboard API → execCommand 隐藏 textarea → 内嵌只读文本框全选手抄；按钮反馈「已复制 ✓ / 请手动复制」，失败时文本框就地展开为可用替代；
- **账本关联建档卡**：新增 `tools/build-ledger-links.py` 生成器——从 events-data.py 材料组反向映射，9 个已建档账本条目（e2002-10-03 / e2006 / e2008-08-02 / e2008-09-28 / e2008-12-24 / e2018-08-07 / e2022-10-28 / e2024-10-13 / e2025-03-28）条目尾部注入「关联建档」卡（PS-LINKCARD 标记幂等）：事件档案直链 + 同事件的站内专题/文档深链（如 e2008-08-02 卡含 survival-2008 与 promises 两专题、e2018-08-07 卡含私有化方案信与争议页）；无 JS 完整可见；
- **四层结构图例**：账本页编者导读补「每条四层互不混装」说明——背景=事实摘要 / 原话=逐字原文+紧随其下的本站译文（原文与译文永不混写）/ 现场=同记录场景 / 后续=结果且编者解读句内标明；
- **样式**：style.css 增 .cite-btn（成功/失败态）与 .ps-linkcard 层（含打印隐藏按钮）；
- VERSION/app.js/14 页 span → 6.19.0；EPUB 重建。

**质量门**
- verify.py 9 项全绿（37 页，索引 169 口径不变）；node --check（app.js + cite.js）通过；CDP 真视口探针与双端双语截图见 qa/v7-19/round-14/（结论以 QA 记录为准）。

## v6.18.0 — 2026-09-29 · V7 改版（13/19）：承诺与结果专题

**主题包成果（V7-19 第 13 轮 · 承诺与结果专题）**
- **新专题页 promises.html（第 37 页）**：「承诺与结果：五案对账」——承诺-结果配对进入标准：逐字原话、带日期精度的原定目标、有自身记录的可核实结果，三件套缺一不入选。深色页头（装饰大字「5」+ SVG 五案分类轴：按四类结果着色，形状与文字与颜色同义不单靠色区分）+ 正文五节：选案与分类方法（**四类归类**：兑现 / 放弃 / 尚无足够证据 / 不是判决——事实分拣非评分）· 五组对照总览表（原话/目标/结果/归类五列）· 五案全文卡片（**01 六周复飞→57 天入轨标「超期 15 天」如实记录 · 02 生产地狱至少六个月→约 11 个月不过不满说成六个月 · 03 funding secured→放弃+SEC 和解+2023 无责判决并置 · 04 专利开放→承诺仍挂官网十余年+对手未蜂拥+善意门槛未经检验的动机保留 · 05 万亿薪酬里程碑→尚无足够证据拒绝吹喇叭与唱衰两种省事立场**；每案金句块引+「金句之外还有上下文」段+记录深链行）· 归类不说的话（不打分/不写反事实/双向不摘樱桃三道护栏+唯一概括显式标注）· **排除项点名**（Cybertruck 时间表无逐字日期原话、Starship 六个月入轨无在册结果条目——缺失件入册前挂起）；
- **事实纪律**：零新增外部事实——五案全部锚定账本在册条目（e2008-08-02/09-28、e2017-07-28、e2018-08-07、e2014-06-12、e2025-11-06）+ 文档 d2018-08-07 + 争议页 2023 Ortega 判决口径；专利博文原文不在文档馆→链接修正为账本 SEC 备案口径（d2014-06-12 锚点不存在，如实不造）；超期、玩笑价、善意门槛等不利与有利细节同页并置；
- **事件材料联动**：e2008-08-02 与 e2018-08-07 材料组各补 promises feature 深链（35→37 份材料关联）；build-events / build-timeline-events 重跑（口径不变：9 事件 / 151 独立 / 18 吸收）；
- **联动三入口**：survival-2008.html 阶段一节点补「比六个星期晚 15 天」对账互链、controversy.html SEC 段收「第 03 案」链接、首页 feature-rows 第三行「FEATURE · LEDGER 承诺与结果」；专题组导航第三位（37 页重注入）；
- **样式**：style.css 扩展 .pv-* 组件层（案例卡 / 编号 / 时段行 / 四类徽标色辅文字，含 ≤760 / 打印）；
- VERSION/app.js/14 页 span → 6.18.0；EPUB 重建。

**质量门**
- verify.py 9 项全绿（37 页，索引 169 口径不变）；node --check 通过；CDP 真视口探针与双端双语截图见 qa/v7-19/round-13/（结论以 QA 记录为准）。

## v6.17.0 — 2026-09-29 · V7 改版（12/19）：平台与 AI 旗舰专题

**主题包成果（V7-19 第 12 轮 · 平台与 AI 旗舰专题）**
- **新专题页 platform-x.html（第 36 页）**：「平台变局：Twitter、X 与并入 xAI」，lr-* 模板 + .sv-* 扩展层。深色页头（装饰大字「X」+ **SVG 三阶段总览图**：买下 2022 / 重塑 2022–24 / 并入 2023–26，方块可点击、宽度声明示意）+ 正文九节：为什么平台单独立档（**内容归属四分工表**：本页=平台交易线 / ai-strategy=AI 全景 / 深读五=AI 战略视角 / grok=模型产品）· 三阶段总览表 · 阶段一买下四节点（04.14 要约 → 04.25 协议第 9.9 条 → 07–10 反悔与强制履约 → 10.27–28 交割「the bird is freed」引语在册）· 阶段二重塑三节点（extremely hardcore 通牒 / 品牌更替 X / 广告主撤离与 DealBook 回应）· 阶段三并入四节点（xAI 成立宣言 → Grok 首发+开源 → 全股票合并引语在册 → Grok 4 + Series E 200 亿 @2300 亿）· **所有权三时代 SVG 图**（公众公司→他私有→并入 xAI，控制线画法声明非持股比例）· **状态口径三分列表**（历史已完结 / 截至日期现状 / 编者框架，逐格分列防混读）· 记录四组 21 条 · 方法与边界六条；
- **口径纪律**：440 亿现金对价与 330 亿全股票估值不混用、不相减算「亏损」，差额连同口径呈现留给读者；800/330 亿标「本人宣布数字·多方报道转述·均未上市无市场报价」；Fidelity 80% 减记标「持仓方记账非成交价」；交割 10.27（资本档案）与 10.28（账本/发帖）双口径并列不静默取舍；编者框架（万能应用底盘/广告动摇背景/开放问题）出现处逐条标注；
- **事件材料联动**：events-data.py e2022-10-28 与 e2025-03-28 材料组各补 feature 深链（33→35 份材料关联）；build-events / build-timeline-events / build-company-files / build-network 全部重跑（events.html 9 事件 35 材料、timeline 151 独立/18 吸收、company-files 12 事件联动不变口径）；
- **联动四入口**：ai-strategy.html「AI 公司买平台」节与 deep-dive-05 第三节各加平台线链接（内容归属互指）、grok.html 关键节点后加「平台交易完整叙事 →」、首页 feature-rows 第二行「FEATURE · X 平台变局」；专题组导航第二位（36 页重注入）；
- **样式**：style.css 扩展 .sv-* 层（三阶段方块三态/阶段徽标三色 sv-tag-s1–s3/所有权图组件/分工清单/grok 链接行，含 ≤760 隐藏所有权图/打印/悬停焦点态）；
- VERSION/app.js/14 页 span → 6.17.0；EPUB 重建。

**质量门**
- verify.py 9 项全绿（36 页，索引 169 口径不变）；node --check 通过；CDP 真视口探针与双端双语截图见 qa/v7-19/round-12/（结论以 QA 记录为准）。

## v6.16.0 — 2026-09-29 · V7 改版（11/19）：2008 生死役旗舰专题

**主题包成果（V7-19 第 11 轮 · 2008 旗舰专题）**
- **新专题页 survival-2008.html（第 35 页）**：「2008 生死役——同时走向断粮的两家公司」，lr-* 长文模板 + .sv-* 专题组件层。深色纪实页头（近黑底 + 装饰大年份「2008」+ 144 天生死线 SVG 轴：三飞失败 / 第四发入轨 / 接任 CEO / NASA 合同 / 圣诞夜关账五节点可点击、图注声明「节点等距示意，非时间等比」；≤760px 隐轴由正文节点列表完整替代）；正文六节——为什么单独讲 2008（四个数字）· 盘面（PayPal 1.8 亿分配原话 + 借钱付房租口径说明）· **144 天逐节点推进（五节点：背景 / 在册原话 / 结果 / 记录深链行）** · 结果弧线（SpaceX 与 Tesla 双弧线数据表：Falcon 1 退役全押 Falcon 9、龙船对接 ISS、Model S 原型、DOE ATVM 4.65 亿批准→放款→2013 提前九年还清、IPO 2.26 亿、2012 交付）· 本专题背后的记录（第一手 / 事件档案与数据视图 / 站内编者线索 / 外部口径四组分列）· 方法与边界（144 天计算口径、CRS 系合同总额非当日现金、圣诞夜轮金额未入册不编造、2008.10 月份精度、传记细节保持传记口径、引语与分析分界）；sticky 目录 + 打印保留 + 无 JS 完整可读；
- **事件档案扩容（7→9）**：`tools/events-data.py` 新增 **e2008-08-02（Falcon 1 三飞失败，豪赌类）** 与 **e2008-09-28（第四发入轨，里程碑类）** 两档案——内容全部取自言行账本在册四段（「I will never give up」Universe Today 标题口径、「最后一枚火箭/六个星期」Vance 传记口径、「the fourth time's the charm」Space.com/Spaceflight Now 现场口径），材料组含新专题页 feature 深链；e2008-12-24 related 补 09-28 双向互链；validate() 通过（9 事件 · 9 引语 · 33 材料）；
- **生成产物刷新**：build-events.py 重建 events.html（9 事件）+ events-data.js；build-timeline-events.py 重聚合——吸收 16→**18** 条（两条 2008 账本记录归入新档案）、独立记录 153→**151**、timeline.html 静态清单同步；build-company-files.py 重跑——SpaceX 档案事件联动 +2（10→**12**），companies-data.js 数据出口同步（companies.html 静态块无需变动）；
- **联动三入口**：deep-dive-01 第五节（2008 案例深读）与 stories.html 特稿 Ⅰ 结尾各加「完整专题 →」；首页 #features 的 feature-rows 首行新增「FEATURE · 2008 生死役」；专题组导航置顶（site-nav.py 注册，35 页重注入，新页 aria-current 正确）；
- **样式**：style.css 增 .sv-* 组件层（页头年份 / SVG 轴 / 四数字栅格 / 节点时间线 / 类型徽标五变体 / 深链行 / 证据清单 / 方法清单 / 引语来源行，含 ≤760 / 打印 / prefers-reduced-motion）；
- **事实纪律**：零新增外部事实——全部内容锚定账本三条、编年史 c2008-12-23、资本流两笔、账本 e2009-03-26 结果弧线与站内特稿口径；站内未载的圣诞夜轮金额不出现数字；「借钱付房租」按本人自述口径标注、不当作审计数字；无 2008 现场合法图片，页头用 SVG 编辑图形不放假照片。

**质量门**
- verify.py 9 项全绿（35 页）；node --check（app.js + events-data.js + timeline-events.js + companies-data.js）通过；CDP 真视口探针与双端双语截图见 qa/v7-19/round-11/（探针断言数与结论以 QA 记录为准）。

## v6.15.0 — 2026-09-29 · V7 改版（10/19）：资本流向可视化

**主题包成果（V7-19 第 10 轮 · 资本流向可视化）**
- **资本流向数据单一事实来源**：新建 `tools/capital-data.py`——5 个资金来源节点（个人资本 / 风险与产业资本 / 公开市场 / 政府 / 收购方）× 7 家公司 × **18 笔真实发生的资金移动**（1999–2026），每笔带日期精度、金额与币种（USD）、统计口径说明与站内来源锚点；八类资金性质（个人投入 / 融资 / IPO 募资 / 政府合同 / 政府贷款 / 收购对价 / 并购对价 / 退出套现）归入五个筛选分组；自带结构自检（端点存在 / kind∈分组枚举 / 双语完整 / 来源·事件·档案锚点逐一在册核对 / 收购必须标实际出资方 / 方向语义校验），不过拒生成；
- **capital-evolution.html#flow 流向区（生成器注入）**：新建 `tools/build-capital.py` 幂等生成——SVG 静态流向图（左来源右公司、18 条带箭头丝带、线宽按金额对数标度且图例显式声明「示意——精确数字以标注为准」；金额未入册的 2008 圣诞夜融资轮画最细虚线并标注「金额未入册」，不编造数字；标签双列错位避让；退出流向个人资本，「退出即入场」闭环可见）+ 图例 + 分组筛选芯片（含 aria-live 状态行与清除）+ 交互详情面板（点选/键盘 Tab+Enter/Esc 焦点归还，口径·来源·事件档案·公司档案深链，面板内可跳转单笔流向）+ 五组文字清单（每行：方向 · 金额 · 日期 · 类型与精度徽标 · 口径 · 来源深链；无 JS 即完整信息）；≤760px 隐图以清单为主形态；打印保留图与清单；产出 `capital-data.js`（window.CAPITAL_V7，供 R15 检索复用）并自动补挂；
- **旧装饰图退役**：capital-evolution.html 原 #ce-flow 静态示意图（宽度口径含混、无出处）由新区块整体替换，死样式清理；「资本模式演化四时代」正文原样保留；
- **不入图声明（口径纪律）**：估值、市值与机构减记不是资金流动，一律不画线（SpaceX 股转估值 2021 约 $100.3B / 2024.12 约 $350B、X 的 Fidelity 减记、Tesla 万亿市值、xAI 约 800 亿并购口径与 E 轮投后约 2300 亿量级，只在各笔口径说明里作背景引用并标「报道口径」）；融资额、收入、合同额分别建卡不混写（NASA CRS 16 亿标「收入性质，非股权融资」、DOE 4.65 亿标「债务，非股权」且载明 2009 批准/2010 放款/2013 提前九年还清全弧线）；
- **联动（第 7–10 轮连贯探索）**：companies.html 关系图详情面板每家公司新增「查看它的资本流向 →」；money.html 资本解剖页新增可交互流向图入口；首页 #map 新增「看钱怎么流——18 笔逐笔带出处 →」；流向清单每行深链事件档案 / 公司档案 / 账本 / 一手文档；
- **样式**：style.css 增 .cap-* 组件层（芯片 / 图 / 图例 / 详情面板 / 清单 / 640px 手机 / 打印 / prefers-reduced-motion）；
- **事实纪律**：零新增外部事实——18 笔全部取自言行账本、一手文档馆、财务资本全景、公司档案、资本解剖与速览的在册口径；站内未载金额的流向诚实标注（1 笔），不编造数字凑图形。

**质量门**
- verify.py 9 项全绿（34 页）；node --check（app.js + capital-data.js）通过；CDP 真视口探针 **56/56 断言全过**（结构 20 / 交互 12 / 双语 4 / 无 JS 3 / 打印 1 / 390 真视口 3 / 三页联动 4 / 版本与回归 6 / file:// 1；探针抓出并修复 1 个真缺陷：面板内跳转后 Esc 焦点丢失 → 焦点归还到流向线本体）；桌面 / EN / 390 截图人工复核；证据与 QA 记录在 qa/v7-19/round-10/。

## v6.14.0 — 2026-09-29 · V7 改版（9/19）：事件时间轴升级

**主题包成果（V7-19 第 9 轮 · 事件时间轴升级）**
- **事件数据扩容与类型维度**：`tools/events-data.py` 新增事件类型五类（创业起步 / 资本运作 / 豪赌翻身 / 产品里程碑 / 争议时刻，与页内静态清单同源口径）+ 第 7 个事件档案 **e2025-03-28（xAI 收购 X）**——内容全部取自言行账本在册四段（本人推文逐字引语在册），估值注明「本人宣布数字 · CNBC/Forbes/AP 报道转述 · 两家公司均未上市无市场报价」；validate() 增 etype 枚举校验（7 事件 · 6 引语 · 27 材料关联）；
- **聚合数据出口**：新建 `tools/build-timeline-events.py`——search-index 条目 pg#id 与事件材料 href 完全匹配即归入事件（16 条被吸收，不再单独成点：**同一事件不会因多份材料伪装成多个事件**）；产出 `timeline-events.js`（TIMELINE_V7：153 条独立记录 + 吸收口径 meta，供时间轴与 R15 检索复用）；
- **timeline.html 泳道重构**：「事件档案」泳道（7 个类型色环节点，点选/键盘 Enter 开详情面板：类型+日期精度徽标、公司 chips、摘要、逐字引语、材料清单、档案深链；Esc 关闭焦点归还）+ 9 条公司泳道（Tesla / SpaceX / X / xAI / SolarCity / PayPal / Neuralink / Boring / 其他——修复旧五泳道整丢 PayPal/SolarCity/Neuralink/Boring 16 条的缺陷；未筛选时一份记录只画主泳道一个点，筛选时所选泳道承载全部含该公司记录）；公司/年份（全部 · 单年按月）/类型三维筛选 + 清除按钮 + aria-live 状态行；同年同月重叠贪心子行分配（≤5 子行）；泳道图/清单视图切换（≤760px 默认清单）；
- **静态清单**：生成器向 timeline.html TL-V7 标记间注入按年分组清单（7 事件行带精度/类型/材料数徽标 + 153 记录行带类型与引语摘录，共 160 行）——无 JS 可读、打印可见（打印规则由整节隐藏改为清单形态输出）；页头 description 同步新口径；移除本页 search-index.js 依赖（改挂 events-data.js + timeline-events.js）；
- **联动扩容**：`tools/build-events.py` ev-head 渲染类型徽标、计数与年份跨度改数据动态取值；重跑 build-network / build-company-files——xAI 档案自动获得事件深链、X 档案 +1（事件档案联动 8→10，events_for_company 单一事实来源交叉引用）；companies-data.py 过期口径注释更新；index.html 事件区措辞 六个→七个；
- **样式**：style.css 增 .gx-* v2 组件层（筛选芯片 / 事件节点 / 详情面板 / 清单 / 视图互斥 / 640px / 打印 / prefers-reduced-motion）与 .ev-etype 五色徽标（events.html 与时间轴同源配色）；
- **事实纪律**：零新增外部事实——第 7 事件全部内容取自账本 e2025-03-28 在册口径；事件 7 / 独立记录 153 / 吸收归位 16 / 材料关联 27 分别统计，不混口径。

**质量门**
- verify.py 9 项全绿（34 页）；node --check（app.js + 内联时间轴脚本）通过；CDP 真视口探针 **64/64 断言全过**（结构与聚合 13 / 筛选 11 / 详情面板与焦点 9 / 键盘 3 / 双语 6 / 390 真视口 5 / 无 JS 3 / file:// 3 / 联动回归 10；探针抓出并修复 1 个真缺陷：跨公司记录重复画点 → 主泳道去重）；before/after 截图 11 张与 QA 记录在 qa/v7-19/round-09/。

## v6.13.0 — 2026-09-29 · V7 改版（8/19）：公司档案体系

**主题包成果（V7-19 第 8 轮 · 公司档案体系）**
- **档案数据单一事实来源**：新建 `tools/company-files-data.py`——4 份完整公司档案（Tesla / SpaceX / X / xAI，五段结构：业务定位 · 在册里程碑 · 财务口径 · 风险与争议 · 相关事件与延伸阅读：33 里程碑 · 19 财务行 · 13 风险项）+ 6 份公司简介（Neuralink / Boring / SolarCity / Zip2 / PayPal / OpenAI）；自带结构自检（档案 id 必须在 companies-data.py 节点表 / 里程碑与财务与风险逐条带站内锚点 / 财务 kind 枚举 / as_of 截至口径必填 / 双语完整），不过拒生成；
- **company-files.html（第 34 页，生成器整页重建）**：新建 `tools/build-company-files.py`——复用 R5 lr-* 模板层（深色页头 + 正文列 + sticky 目录），页头大图三张（Tesla 弗里蒙特产线 / SpaceX 星舰塔捕 / X 总部，全部 R2 已溯源带署名；xAI 无纪实图，不放占位图）；里程碑行「日期列 + 正文 + 来源短标签深链」、财务行「kind 徽标 + 日期 + 金额 + 说明」分列建档、风险项全部链向争议深读/账本/财务全景在册位置；相关事件与 events-data.py 交叉引用（4 档案共 8 条事件深链）；目录含 4 档案 + 6 简介；
- **体系闭环**：companies.html 六张卡片各加档案深链（四家 → #file-*，Neuralink/Boring → #brief-*）；companies-data.py 全部 10 个公司节点 href 从泛页升级为档案锚点 → 重跑 build-network.py 后关系图点选详情面板的「查看档案」直达对应档案段；companies-data.js 自 R8 起由 build-company-files.py 统一写出（新增 window.FILES_V7 数据出口，供 R9 时间轴 / R10 资本流向 / R15 检索复用；COMPANIES_V7 格式与 R7 逐字节一致，build-network.py 移交写出职责避免双写覆盖）；
- **事实纪律**：零新增外部事实——里程碑/财务/风险全部取自言行账本、编年史、财务资本全景、争议深读、一手文档馆的在册口径，逐条锚点可查；财务行按 kind 分列（个人投入/融资/IPO/合同/收入/估值/市值/收购对价/减记/薪酬），融资额、估值、收入、市值不混写，私有公司估值一律标注「报道口径，非公司披露」；每份档案带 as_of 截至行（Tesla 2025-11 / SpaceX 2024-12 / X 2025-03 / xAI 2026-01），站内未再更新的数字不冒充当前事实；业务定位统一标注「编者归纳」；
- **同步**：site-nav.py 公司组 7→8 项（新增「公司档案」）全站 34 页重注入；style.css 增 .cf-* 档案组件层（含 640px 手机与打印规则）与 .company-file-link 卡片深链样式；ASSETS.md 三处图片用途同步；VERSION / app.js / 13 页 span 步进 6.13.0；EPUB 重建。

**质量门**
- verify.py 9 项全绿（34 页）；node --check app.js 通过；CDP 真视口探针全过（档案页结构/锚点落报头下/双语全量切换/财务分列与来源链接可达/无 JS 正文完整/390 真视口零溢出/file:// 冒烟/companies.html 卡片深链与关系图档案链接回归）；证据与 QA 记录在 qa/v7-19/round-08/。

## v6.12.0 — 2026-09-29 · V7 改版（7/19）：公司关系总览

**主题包成果（V7-19 第 7 轮 · 公司关系总览）**
- **关系数据单一事实来源**：新建 `tools/companies-data.py`——11 节点（运营者 + 10 公司）× 13 条关系边；每条边带类型（创立 / 入主执掌 / 收购 / 创意发起 / 编者关联）、日期与精度、双语标签、图上短标签、证据分级（12 条 verified 站内在册证实 + 1 条 editorial 编者关联）与站内来源锚点；自带结构自检（重复 ID / 端点存在 / 双语完整 / 枚举合法 / editorial 也必须有在册出处 / verified 必须带日期），不过拒生成；与 events-data.py 交叉引用（公司 ← 相关事件）；
- **companies.html#network 关系视图（生成器注入）**：新建 `tools/build-network.py` 幂等生成——SVG 静态关系图（中心墨色圆 + 10 公司色标顶条节点卡 + 13 条着色关系线：创立/入主/发起=实线、收购=实线+方向箭头、编者关联=虚线；13 个图上短标签手工避让；无 JS 完整可读）+ 图例四项 + 交互详情面板（点选/Tab+Enter/Esc，业务定位、状态、相关事件深链、关系清单含来源与证据标注）+ 三组文字清单（创立·入主·发起 9 / 收购与合并 3 / 编者关联 1，每行带证据徽标与来源锚链接）；≤760px 隐图以清单为主形态，打印隐藏交互面板；
- **本地 JS 数据出口**：`companies-data.js`（`window.COMPANIES_V7`，file:// 下以 script 标签加载），供 R8 公司档案 / R9 时间轴 / R10 资本流向复用；生成器自动补挂 script 标签；
- **全站公司色标体系定稿（:root --co-*）**：musk 墨 / tesla 红 / spacex 藏蓝 / x 石墨 / xai 紫 / neuralink 玫紫 / boring 暗金 / solarcity 绿 / paypal 蓝 / history 灰褐；本轮接入三处——关系图节点与边线、首页六瓦顶条（hover 保持公司色）、events.html 公司 chip 顶条；色标只作辅助，公司一律以名称文字为准；
- **首页接入**：#map 区头新增「查看关系总览——谁创立了什么、谁买了谁，逐条带来源 →」入口行（companies.html#network）；
- **事实纪律**：13 条关系全部取自站内在册口径，零新增外部事实；SolarCity 沿用账本「表兄弟按他的创意创立，他出任董事长」（创意发起，不写「共同创立」）；2002 SpaceX 创立只用通识年份口径并标注「创立故事细节未入册」；xAI 收购 X 引账本 e2025-03-28（本人推文 permalink 在册）；OpenAI—xAI「对手」标编者关联并注明非当事方表述；金额不混用估值与收入；
- **同步**：VERSION / app.js / 13 页版本 span 步进 6.12.0；EPUB 重建。

**质量门**
- verify.py 9 项全绿；node --check app.js 通过；CDP 真视口探针 43 断言全过（结构 14 / 交互 5 / 键盘 2 / 双语 6 / 首页 2 / events 回归 2 / 无 JS 3 / 390 真视口 4 / file:// 4 / 版本 1）；探针抓出并修复 2 个真 bug（详情面板双语对象被字符串化为 [object Object]）；桌面/390/EN/file:// 截图人工复核通过；证据与 QA 记录在 qa/v7-19/round-07/。

## v6.11.0 — 2026-09-29 · V7 改版（6/19）：事件与来源结构

**主题包成果（V7-19 第 6 轮 · 事件与来源结构）**
- **事件数据单一事实来源**：新建 `tools/events-data.py`——六个代表性事件（2002 PayPal 交割 / 2006 SolarCity 创立 / 2008 圣诞夜融资 / 2018 funding secured / 2022 Twitter 交割 / 2024 星舰塔捕）的结构化档案：稳定事件 ID（沿用账本 e* 锚点体系）、公司清单、显式日期精度（精确到日 / 精确到月 / 仅年份）、背景 / 关键事实 / 逐字引语 / 后续结果四段本体 + 材料关联；自带结构自检（重复 ID / 字段双语完整 / 精度枚举 / 无引语条目必须有诚实说明），不通过则拒绝生成；
- **事件与材料分离建档**：一个事件关联多份材料——账本条目（基准口径）、一手文档、X 帖、访谈、站内专题、纪实图片、外部来源七类分开列示（共 24 份材料关联），「同一事件的不同记录分开列示；事实表述以账本条目为基准口径」写入页面口径说明；关键事实区统一标注「编者归纳，非当事人原话」；
- **events.html 事件档案页（第 33 页）**：导航事件组 4→5，复用 R5 长文模板层（.lr-hero 深色页头 + .lr-layout 正文列 + sticky 目录，目录滚动定位自动生效）；每事件五段结构 + 日期精度徽标 + 公司 chip + 材料清单（类型标签 + 日期 + 说明）+ 相关事件互链；e2024-10-13 配 R2 已溯源塔捕纪实图（Steve Jurvetson · CC BY 2.0 署名 + 尺寸声明 + 懒加载）；e2006 无逐字原话条目以 no_quote_note 诚实建档、不凑引语；新增 .ev-* 组件层入 style.css（含手机 640px 与打印规则）；
- **本地 JS 数据出口**：`events-data.js`（`window.EVENTS_V7` 全量结构化数据）——file:// 下以 script 标签加载（规避 fetch CORS），供 R7 公司关系视图、R9 事件时间轴、R15 检索聚合复用同一份数据；
- **首页接入**：#events 区头新增「事件档案」入口行（.section-more）；五个事件行各追加「事件详情」深链（events.html#e*，tools/r06-index-links.py 注入）；
- **事实纪律**：全部事实与引语取自已核实的言行账本条目，本轮未新增外部事实；日期精度只作档案分层不作杜撰（e2006 仅年份；2018 SEC 起诉沿用账本「八天后」相对表述，不断言具体日期）；
- **同步**：VERSION / app.js / 12 页版本 span 步进 6.11.0；site-nav.py 事件组注册后全站 33 页导航重注入；changelog.html 同步；EPUB 重建。

**质量门**
- verify.py 9 项全绿；node --check app.js 通过；CDP 真视口实测（桌面 1440×900 / 手机 390×844）：events.html 六事件渲染与锚点定位、EN 全量切换、材料链接可达、无 JS 正文完整、390px 零横向溢出、file:// 冒烟、旧锚点回归（primary#e*）；证据与 QA 记录在 qa/v7-19/round-06/。

## v6.10.0 — 2026-09-29 · V7 改版（5/19）：长文阅读模板

**主题包成果（V7-19 第 5 轮 · 长文阅读模板）**
- **共享长文模板层**：style.css 新增 `.lr-*` 组件——深色纪实页头 `.lr-hero`（近黑底 + 编者大标题 + 斜体导语 + 元信息行 + 通栏大图带署名）、`.lr-layout`（正文列 = --read-width 720px + 右侧目录栏）、`.lr-toc`（桌面 sticky 目录 / ≤960px 盒装链接）、正文 16.5px · 行高 1.92；统一引语 `.lr-quote`（原文 + 中译分层）、数据框 `.lr-data`/`.lr-data-box`、编者注 `.lr-note`、来源脚注 `.lr-foot` 四类内容组件；
- **深读五篇全部迁移**：新建 tools/build-longread.py 生成器（幂等，含 V7-R5-LONGREAD 标记跳过）——五篇深读从「页内样式 + 14.5px 正文 + h1→h3 跳级 + 无目录无页头」迁移到共享模板：页内旧样式块删除（并入 style.css）、正文升 16.5px、章节 h3→h2 并建 `{stem}-s{n}` 锚点、类名 dd-*→lr-* 逐一映射（内容段落逐字保留，diff 复核）；每篇页头配已溯源纪实大图（资→弗里蒙特产线 / 用人→肖像 / 失败→星舰塔捕 / 监管→猎鹰重型着陆 / AI→Twitter 总部）并带作者·许可署名，og:image 同步指向本篇大图；
- **元信息行**：阅读时长按实际内容计算（中文 300 字/分 + 英文 200 词/分）静态写入（无 JS 依赖），并标注小节数、字数与版本更新日期；深读五篇为 4–5 分钟、长卷为 11 分钟（约 2,900 字）；
- **长卷页同模板**：reading.html 加深色大图页头（portrait-hero 3:2 取景）与元信息行，删除与新页头重复的旧 rd-head；十章目录与既有锚点（含 controversy.html → #ch5 外链）原样保留；
- **交互**：app.js 新增长文目录滚动定位（.lr-toc 链接 ↔ 章节锚点，IntersectionObserver，无 IO 时优雅降级）；深读页补挂顶部阅读进度条（复用既有 .progress 驱动）；入场动画与正文可见性不受影响（模板无 .reveal 依赖）；
- **同步**：VERSION / app.js / 12 页版本 span 步进 6.10.0；ASSETS.md 五处图片用途补记；EPUB 重建。

**质量门**
- verify.py 9 项全绿；node --check app.js 通过；CDP 真视口实测（桌面 1440×900 / 手机 390×844）：页头大图与元信息渲染、目录锚点跳转落视野、滚动定位高亮、进度条、EN 切换（标题/导语/图注/元信息/目录全量换英）、无 JS 正文完整可见、390px 零横向溢出、表格手机横滑提示；改前改后截图与 QA 记录在 qa/v7-19/round-05/。

## v6.9.0 — 2026-09-29 · V7 改版（4/19）：首页编排与全局导航

**主题包成果（V7-19 第 4 轮 · 首页编排与全局导航）**
- **全站统一导航（五组）**：顶层导航由 11 项平铺重组为 开始 / 公司 / 事件 / 专题 / 资料 五组（覆盖全部 32 页，每页唯一归属）；新建 `tools/site-nav.py` 生成器作为导航单一事实来源——分组注册表 + 单一模板，逐页注入并自动标注 aria-current，幂等可重跑；此前 20 个页头页（深读五篇、账本系、检索、长卷、修订史等）完全没有全局导航，本轮全部补齐，其中 17 页同步挂载 app.js（语言切换/版本号首次覆盖全站）；
- **搜索随时可达**：报头新增常驻「检索」胶囊（全站 32 页、桌面手机均在），资料组内保留第一手检索入口；
- **桌面下拉 + 手机手风琴**：桌面分组支持 hover / 键盘 focus-within / 点击（触屏）三种展开，aria-expanded 语义完整，外点与 Esc 关闭（Esc 焦点归位分组标签）；手机 ≤760px 汉堡面板改五组手风琴，打开菜单时自动展开当前页所在组；当前页在面板与下拉中均有朱红左边线高亮，分组标签以 :has([aria-current]) 同步高亮（无 :has 支持时优雅降级）；
- **首页编排**：16 卡平铺章节目录重组为五个主次分明的分区——三条阅读路径（快速了解 30 分钟 / 深度阅读 / 查找资料，编号大字 + 串联链接 + 各自 CTA）、公司版图总览（六家在营公司瓦片，文案照抄 companies.html 不新造事实，色标体系留给 R7）、旗舰专题（资本运作主推特写 + 四行次级专题 + 更多线索行）、关键事件与证据（账本 67 条中选五个节点：2002 PayPal 交割 / 2008 圣诞夜融资 / 2018 funding secured / 2022 440 亿交割 / 2024 星舰塔捕，全部深链 primary.html#e* 已验证锚点）、最近实质更新（v6.5.0–v6.8.0 四条链修订记录）；
- **结构修复**：消除旧「第一手」卡内 <a> 嵌套 <a> 的非法结构（子链接成为资料组导航与版图注释行）；删除 chapter-grid/chapter-card 死样式（chapter-pager 各篇章页沿用保留）；
- **健壮性**：.reveal 入场动画改为 html.js 前缀守卫（app.js 首行添加 js 类）——脚本失败时全站正文不再隐形（此前 .reveal 元素依赖 JS 显现）；
- **同步**：VERSION / app.js / 12 页版本 span 步进 6.9.0；EPUB 重建；QA 证据在 qa/v7-19/round-04/。

**质量门**
- verify.py 9 项全绿；node --check app.js 通过；32 页断链校验含新导航与新锚点零断裂；CDP 真视口实测（桌面 1440×900 / 手机 390×844）：五组下拉三态展开、手机手风琴、EN 切换、当前页高亮、深读页导航注入后排版正常；改前改后截图各 10 张 + QA 记录在 qa/v7-19/round-04/。

## v6.8.0 — 2026-09-29 · V7 改版（3/19）：首页首屏重构

**主题包成果（V7-19 第 3 轮 · 首页首屏重构）**
- **深色纪实封面**：首页首屏整体换为近黑 #101316（--coal）满幅封面，海报式构图——编者大标题「把未来做成生意」通栏一行（88–138px 刻度，≥720px 隐藏手动换行），kicker「编者视角 · 商业档案」明确编者文案属性（非当事人引语）；副标题「从公司、资本与关键决策，读懂马斯克的商业世界。」；
- **三入口**：开始阅读（reading.html 长卷版）/ 探索公司版图（companies.html）/ 查找资料（search.html），朱红主按钮 + 暗底描边新 .btn-ghost；
- **人物与业务画面主次**：肖像启用 R2 备好的 portrait-hero.jpg 3:2 裁切（<picture> ≤640px 自动换 4:5 竖版），去白框衬纸、改暗底细边框 + 朱红错位色块（18px slab）+ 30% 去灰纪实调色；新增四格业务横带（弗里蒙特总装线 / 猎鹰重型双助推着陆 / 星舰第五飞塔捕 / 2022-11 Twitter 总部），全部为 R2 已溯源素材，图块带公司标签 + 图注 + 作者·许可署名；ASSETS.md 用途记录同步；
- **手机首屏修复**：删除 ≤960px「肖像 order:-1 插队首屏」旧规则——手机次序改为 标题→定位→三按钮（通栏）→肖像（4:5）→数字行→横带（scroll-snap 横滑，保留原生滚动）；真 390px CDP 探针零横向溢出，CTA 底缘 546px < 844px 完整落在首屏内；
- **英文不破版**：html[lang="en"] 独立标题刻度（桌面 clamp 40–96px 两行、手机 36–44px）+ 行高 1.08；390px EN 实测右缘 372px 零溢出；
- **首屏零动画依赖**：封面全部元素不挂 .reveal（CSS 默认可见），脚本或动画失败首屏照常完整；.cnt 计数保留静态数字兜底；
- **工程修复（本轮实测发现）**：① auto 网格轨道内 min(480px,100%) 百分比循环解析致文字列被压成 0 宽（计算值 0px 944px）——轨道改 min(480px,44vw) 确定尺寸；② .deal-lines 亮色规则源码顺序靠后压过暗底覆盖（dd 墨字不可读）——覆盖规则提高特异性为 .deal-lines.hero-stats；③ 猎鹰横带图 4:3 裁切 object-position 74% 对准双助推着陆瞬间；
- **同步**：index title/description/og:image/og:description/twitter:description/theme-color(#101316) 换新定位；print 模式封面转白底、隐藏横带与按钮；令牌新增 --accent-bright/--mist；12 页版本 span 步进。

**质量门**
- verify.py 9 项全绿；node --check app.js 通过；CDP 真视口探针：桌面标题 138px 单行、EN 96px 两行、390px 中英零溢出；EN 切换/file:// 冒烟正常；改前改后证据 + QA 记录在 qa/v7-19/round-03/。

## v6.7.0 — 2026-09-29 · V7 改版（2/19）：图片与纪实素材体系

**主题包成果（V7-19 第 2 轮 · 图片与纪实素材体系）**
- **全站图片溯源建档**：新建 ASSETS.md 作为素材唯一权威清单（来源页/作者/许可/核实日期/加工方式/用途）；portrait.jpg 经感知哈希比对**逐像素命中** Commons「Elon Musk Royal Society (crop2)」（Debbie Rowe · CC BY-SA 3.0）、tesla-factory.jpg 命中「Tesla Factory, Fremont」（Maurizio Pesce · CC BY 2.0）；falcon-heavy.jpg 两轮检索无法定位原文件——整体替换为 SpaceX 官方 CC0 的「Falcon Heavy 演示飞行双助推器同步着陆（2018）」，画面更有冲击力且来源可查；
- **新增纪实素材 4 张**：Starship 助推器塔捕（Jurvetson · CC BY 2.0，2024-10-13 第五飞，与账本 e2024-10-13 锚点互证）、Twitter/X 总部（osunpokeh · CC BY-SA 4.0，2022-11 收购交割时点）、Cybertruck 量产展车（N2e · CC0）、及上述 Falcon 替换图；全部经目检、裁切（3:2 上部/偏移构图保主体）、压缩与尺寸声明，检索与下载脚本入 tools/（trace-assets/find-assets/get-files/prep-assets）；
- **公司版图卡配图**：companies.html 六卡中 Tesla/SpaceX/X 三家接入纪实配图（带作者·许可署名行），xAI/Neuralink/Boring 暂无可查纪实素材、诚实保持文字卡；新增 `.card-photo` 样式（3:2 object-fit、边框衬纸、署名行、打印灰度）；
- **首页与深读页素材治理**：首页封面肖像补 figcaption 署名行（中英双语）+ fetchpriority=high；indepth.html 图注升级为完整署名并修正 alt 与实拍内容不符处（「工厂外景」实为总装线内景）；全站 `img` 补 `height:auto` 防拉伸；
- **封面备用裁切入库**：portrait-hero.jpg（3:2 横版）与 portrait-hero-mobile.jpg（4:5 竖版）供第 3 轮首页首屏重构取用；
- **加载策略**：三张公司卡图 loading=lazy + decoding=async；首屏肖像 eager+高优先级；真实 390px 视口（CDP 仿真）验证零横向溢出——此前截图「裁字」系 headless Chrome 最小窗宽 500px 伪影，已用 CDP 探针（tools/r02-probe.js）实证排除。

**质量门**
- verify.py 9 项全绿；`node --check app.js` 通过；EN 切换署名行/懒加载滚动加载/21:9 底部取景（object-position）实测正常；断链与锚点零变化。

## v6.6.0 — 2026-09-29 · V7 改版启动（1/19）：设计基础与全站令牌归一

**主题包成果（V7-19 第 1 轮 · 视觉基础与基线）**
- **V7 设计令牌基础层**：`:root` 重写——暖白阅读底 `#F3F0E8`、近黑封面底 `#101316`（第 3 轮启用）、墨色 `#17191d`、朱红主强调 `#C84032` + 小号强调文字深阶 `#A63628`（对比度 5.8:1）；新增字号层级（含第 3 轮启用的 88–144px 封面主标题刻度）、4px 间距标尺、阅读宽度 720px 令牌、动效时长令牌；
- **全站色彩令牌归一**：32 页 + style.css + app.js 共 853 处硬编码旧色（酒红 `#7c2d2d`/纸白 `#faf9f6`/`#1a1a1a`/`#5c574e`）统一为 CSS 变量（SVG 属性/内嵌 JS/favicon/theme-color 按语境直换新值）；`build-revisions.py` 生成模板同步归一，避免重建回退；
- **基础可见应用**：报头 3px 朱红顶条、主按钮朱红填充、kicker 前导红短线、12 处小号强调文字对比度达标；首页封面标题刻度提升（48–104px）；长卷阅读版正文 15→16.5px 进入 16–18px 规范区间、阅读宽度令牌化；
- **重复基础规则清理**：删除文件尾重复 print 块；归一化过程中发现的 `:root` 自引用风险随令牌块重写消除；
- **改版证据**：`qa/v7-19/round-01/` 存 before/after 各 10 张（5 代表页 × 1440×900 + 390×844）+ QA 验收记录；新增 `tools/qa-shots.py` 截图协议（headless Chrome + 冻结动画）。

**质量门**
- verify.py 9 项全绿；`node --check app.js` 通过；双语切换/手机菜单/时间轴筛选交互实测正常；断链与锚点零变化（旧链接全兼容）。

## v6.5.0 — 2026-09-26 · 17 轮精进计划收官：全量对账与交接同步（自由精进第七十二轮）

**收官对账**
- **CHANGELOG 总条数 160**（143 基线 + 17 轮，逐轮有账）；git 172 次提交；32 页；索引 169 条七类型；账本 67 条（无净增——Fremont 候选 v6.0.0 裁定放弃）；
- **build-revisions 幂等重跑**：修订历史 100 → **107 锚点**（15 轮迭代的锚点轨迹演进，e* 锚点生命周期补全）；EPUB 重建 121,762 bytes / 24 章（防旧）；
- **DEVLOG.md 全量同步**：版本 v6.5.0 / git 172 次 / 索引 169 七类型 / 修订历史 107 / CHANGELOG 160；待做清单重写（账本候选序列关闭、排版与 QA 完成项归档）；
- **README** 站点结构表 30 → 32 页口径。

**17 轮净成果一览**：检索索引 107→169（+58%，三新页入索引）；争议三篇深化（+100% 篇幅，DMV/NLRB/DSA 多源新节点）；ai-strategy + deep-dive×5 全量重写（平均增幅 109%）；og 五件套 32 页全覆盖；窄屏与打印适配全站就位；技术债#1 核销；引语纪律修正四处；Fremont 候选裁定关闭。每轮恰好一个 commit、verify 全绿、push 部署。

**质量门**
- verify.py 11 项全绿（含修订历史 107 锚点新口径）；EPUB 新鲜度通过。

## v6.4.0 — 2026-09-26 · 全面 QA：打印五页 + 双语覆盖 + 窄屏自检（自由精进第七十一轮）

**QA-1 五页打印抽检（headless Edge + pypdf）**
- chronicle 8 页 / finance 4 页 / revisions 5 页 / controversy 5 页 / reading 10 页——**全部零近空白页**；
- 关键术语全命中（初测 finance 缺「2,300」为探针笔误——页面用「2300 亿」口径，复认非缺陷）。

**QA-2 双语 data-en 覆盖抽查（本轮新写六页）**
- ai-strategy + deep-dive-01~05：data-en 标题 38 个、段落 61 个、引语中译行 17 个、页脚双语 6/6——覆盖完整；
- 检查器曾报 29 处 data-en 值含裸 `<a>`——**核实为误报**：app.js 切换用 innerHTML（第 34 行），属性值内 HTML 标签合法且正常渲染为链接，属设计允许。

**QA-3 窄屏 CSS 自检**
- style.css（450 对）与八页页内 style 括号全部配对；480px 块存在性盘点发现 **ai-strategy.html 缺块**（v5.94 重写遗漏）——**就地修复**：补 480px 块（页边距/正文/引语/数据框/分析块缩排适配），与深读页模式对齐。

**质量门**
- 修复后 verify.py 11 项全绿；EPUB 重建满足新鲜度门禁；本轮净变更 = ai-strategy.html 一处补块 + QA 报告。

## v6.3.0 — 2026-09-26 · 技术债#1 核销：bg 检索匹配诊断与实证（自由精进第七十轮）

**主题包成果**
- **诊断结论：技术债#1 已不存在**。原记录称「bg 仅限 primary 类型、其他类型匹配未纳入」——实测：169 条索引条目的 bg 字段全部非空（primary=背景段 67、一手文档=note 9、访谈=ctx 18、帖史=note 13、编年史=节主线 53、争议=篇摘要 5、财务=节摘要 4），且 search.html 的 match() 早已含 `(it.bg||'')`——缺口在 v5.89-5.90 检索扩容两轮中被自然消化。
- **实证验证**：抽取 6 条「仅存在于 bg 字段、其他字段不含」的独特词（文档/访谈类各半）模拟 match() 全部命中（6/6），含 d2006-08、i2015-04-30 等。
- **DEVLOG 技术债清单 #1 核销标注**（划线+核销说明），清单从四项降至有效三项。

**质量门**
- 验证脚本纯只读（未改任何站点文件）；verify.py 11 项全绿；EPUB 重建满足新鲜度门禁。

## v6.2.0 — 2026-09-26 · 排版精进：长卷/争议窄屏 + 时间轴横滑（自由精进第六十九轮）

**主题包成果**
- **reading.html**：新增 ≤480px 块（布局内边距/正文 14px/引语与目录缩排——此前仅有 960px 侧栏折叠）；print 块补 `.rd-ch h2 { break-after: avoid; }` 与段落孤行控制；
- **controversy.html**：新增 ≤480px 块（此前零窄屏规则）；print 块补标题防孤行与段落孤行控制；
- **style.css**：页顶时间轴（.ps-timeline，67 节点）≤640px 横滑（此前窄屏挤压）、打印 break-inside 防拆；
- 深读五页的同类规则已在 v6.0.0 完成，本轮为其余主力内容页补齐。

**质量门**
- 打印复验（headless Edge + pypdf）：reading 10 页 / controversy 5 页，均零近空白页，关键词全命中（含 v5.91-93 新扩写的 DSA/工会节点）；verify.py 11 项全绿；EPUB 重建满足新鲜度门禁。

## v6.1.0 — 2026-09-26 · Open Graph 社交标签全站覆盖（自由精进第六十八轮）

**主题包成果**
- **32 页 og 五件套齐备**（og:title / og:description / og:type / og:url / og:image）：
  - 新注入 20 页（head 内 </head> 前整块插入，python 批量）；og:title 取页 title，og:description 优先复用既有 meta description（19 页有），其余 13 页自各页页首文字改写一句话（不造新事实）；
  - 老版 12 页（index/primary 等，v5.5x 时代注入）升级：og:image 由相对路径改绝对 URL（https://a1310055634-sudo.github.io/musk-website/assets/portrait.jpg）、补齐缺失的 og:url。
- 分享到社交平台将获得标题+摘要+配图的预览卡片。

**质量门**
- 抽查 index/controversy/deep-dive-05 三页五件套完整、og:image 与 og:url 均为绝对路径；verify.py 11 项全绿（断链不受 og: content 属性影响）；EPUB 重建满足新鲜度门禁。

## v6.0.0 — 2026-09-26 · 账本收官候选放弃 + 深读五页排版精进（自由精进第六十七轮）

**账本候选裁定（放弃，Gruber 先例）**
- **2010.05 Toyota-Tesla NUMMI/Fremont 收购不录入**。核查：账本 2010 年仅 e2010-06-29（IPO），"Toyota" 零提及，确属未录；框架事实多源可证（2010.05.20 官宣合作、$42M 收购 NUMMI、Toyota $50M IPO 前入股、$17M 设备——NYT/Autoblog/Green Car Reports/SFGate）。但三轮定向 WebSearch + 新闻稿原文抓取均**未获得 Musk 逐字引语**（各源均为转述，Toyoda "extreme innovator" 亦非逐字）——按「无逐字不录」纪律放弃，Fremont 作为账本候选序列就此关闭（DEVLOG 待做清单相应清空）。存量 Fremont 内容（e2012-06-22 首批交付、e2020-05-11 违令复工）不受影响。

**主题包成果（改做排版精进）**
- 深读五页（deep-dive-01~05）批量注入统一的 ≤480px 窄屏块：页边距/引语块/数据框/中译行缩排与字号适配（此前除 dd-01 表格横滑外四页无任何窄屏规则）；
- 打印规则补充：`.dd-sec h3 { break-after: avoid; }`（标题不孤行）、`.dd-data { break-inside: avoid; }`、`.dd-lead/.dd-sec p { orphans:3; widows:3 }`（参照 v5.87.0 revisions 防拆先例）；
- **打印抽检**：headless Edge 渲染 deep-dive-05 → PDF 3 页、无近空白页、六个关键术语全命中（含新扩写的「三位一体」「无限金钱外挂」）。

**质量门**
- verify.py 11 项全绿；EPUB 重建满足新鲜度门禁；临时 PDF 用后即删。

## v5.99.0 — 2026-09-26 · 薄页充实：AI 战略逻辑深读全量重写（自由精进第六十六轮，deep-dive 系列收官）

**主题包成果**
- deep-dive-05.html 6317 → 13609 字节（目标 10KB+ 达成），四节扩为五节：
  - **定位差异化**：与 v5.94 重写的 ai-strategy.html（时间线叙事）互补——本篇读「逻辑」（动机链/三位一体/治理变量），页头声明互为表里并交叉链接；
  - **补双语**：全页叶子节点补齐 data-en；
  - **引语纪律修正**：原两条「已核实」标注的引语（"I'm the reason OpenAI exists" / "Grok will actually answer…"）经与账本/语录卡/帖史对账均无核实记录——第一条降级为「广泛流传口径、逐字待补不入账本」（与 SEC 引语同一纪律）并在编者注说明；第二条弃用，替换为账本已核实的 e2023-07-12 章程引语与 x-posts#p2023-11-04 Grok 上线帖；
  - **新增第四节**「新变量：有人管这台机器了」——DSA 首罚对 AI 分发面的治理含义（编者框架标注：三位一体三条腿分属不同法域）；
  - **补锚点**：e2023-07-12、e2025-03-28、e2024-10-10、e2024-06-13、e2025-11-06、p2023-11-04、finance#xai、controversy#twitter。
- 五轮融资数据框（240 亿→2300 亿轨迹）取自 finance xAI 节；零新造事实。
- **deep-dive 五篇充实系列全部收官**（01 资本/02 用人/03 失败/04 监管/05 AI，平均增幅 109%）。

**质量门**
- 引语对账三条（账本/语录卡/帖史）；verify.py 11 项全绿；EPUB 重建满足新鲜度门禁。

## v5.98.0 — 2026-09-26 · 薄页充实：监管博弈深读全量重写（自由精进第六十五轮）

**主题包成果**
- deep-dive-04.html 6476 → 14931 字节（目标 10KB+ 达成），四节扩为五节：
  - **补双语**：全页叶子节点补齐 data-en；
  - **补引语块**：接塔推文补全账本逐字版（"The tower has caught the rocket!!" + "Science fiction without the fiction part."，e2024-10-13）；迁册引语替换为账本已核实的股东大会发言（"hot d***! I love you guys." + $25T 愿景，e2024-06-13——原 "Texas reincorporation was approved by shareholders." 不在账本，弃用）；SEC 引语统一为「60 Minutes 广泛报道口径、逐字待考不入账本」（与争议页口径对齐，修正原「已核实」的不一致表述）；
  - **新增第四节**「新战线（2024-2026）：NLRB、DMV、DSA」——缝入 v5.92-5.93 三篇争议深读的成果（删帖令撤销/一词换暂停/€120M 首罚），并纳入逻辑链小结与适用边界；
  - **补锚点**：e2018-08-07、d2018-08-07、e2024-10-13、e2024-06-13、controversy 五篇互链。
- 零新造事实；引语取舍全部以账本为唯一标准。

**质量门**
- 引语账本逐字核对（两条替换一条降级口径）；verify.py 11 项全绿；EPUB 重建满足新鲜度门禁。

## v5.97.0 — 2026-09-26 · 薄页充实：失败模式深读全量重写（自由精进第六十四轮）

**主题包成果**
- deep-dive-03.html 7001 → 15212 字节（目标 10KB+ 达成），四节扩为五节：
  - **补双语**：全页叶子节点补齐 data-en（含第四节适用边界原三处英文残留的中文化）；
  - **补引语块**：新增 Amos-6「14 年来最困难、最复杂的失败」（e2016-09-01 逐字，中英对照）；原「important enough」引语补中译；
  - **补锚点**：e2008-08-02/e2008-09-28/e2008-12-24/c2008-12-23（2008 链条）/ e2017-07-28（生产地狱）/ e2022-10-28（bird is freed）/ e2022-11-16（Extremely Hardcore 深夜邮件）/ e2010-06-29（IPO）/ e2018-08-07（私有化未遂）/ e2016-09-01（Amos-6）；
  - **新增第三节**「失败的另一种处理：Amos-6 公开调查」——根因公开、修复随复飞发布，并串联 2019 Crew Dragon 与 Starship 迭代爆炸的公开呈现（编者观察标注）；
  - **就地修复事实性错误**：原第四节「2018 之后他私有化了 Twitter」时间线错乱（2018 为私有化未遂 fuding secured 被罚，Twitter 私有化为 2022）——改写为对照案例并注明 SEC 罚金与董事长职务代价。
- 零新造事实（Amos-6 根因表述取自账本 e2016-09-01 既有核实内容）。

**质量门**
- 引语与归属经账本逐字核对；verify.py 11 项全绿；EPUB 重建满足新鲜度门禁。

## v5.96.0 — 2026-09-26 · 薄页充实：用人逻辑深读全量重写（自由精进第六十三轮）

**主题包成果**
- deep-dive-02.html 7868 → 15183 字节（目标 10KB+ 达成），五节扩为六节：
  - **补双语**：全页叶子节点补齐 data-en（此前整页无英文）；
  - **补引语块**：新增 Starbase 建市引语 "STARBASE IS AWESOME AND ANYONE CAN VISIT."（e2025-05-03，中英对照）；既有两条 blockquote（面试法待考引语、Humans are underrated）保留并补中译；
  - **补锚点**：e2025-05-03（Starbase 建市）/ e2016（自动化纠错，经块级定位确认归属）/ e2017-07-28（生产地狱）/ e2020-05-11（Fremont 复工）+ supplychain/persona 交叉链接；
  - **新增第五节**「压力测试：2020 年的 Fremont」——违令复工推文作为用人体系的极端案例（「只逮捕我一个」中英对照）；
  - **就地修复**：原第三节「2025.14.03」日期笔误 → 2025.05.03（以账本 e2025-05-03 为准）；"physically" 英文残留改中文。
- 零新造事实（全部重组账本与扩展包既有材料）。

**质量门**
- 引语归属经块级正则定位确认（Humans are underrated 在 e2016 年份级条目内）；verify.py 11 项全绿；EPUB 重建满足新鲜度门禁。

## v5.95.0 — 2026-09-26 · 薄页充实：资本运作深读全量重写（自由精进第六十二轮）

**主题包成果**
- deep-dive-01.html 7554 → 15499 字节（目标 10KB+ 达成），五节扩为六节：
  - **补双语**：全页叶子节点补齐 data-en（此前整页无英文）；
  - **补引语块**：三条账本逐字引语入 blockquote（e2002-10-03 借钱付房租 / e2008-09-28 第四次的好运 / e2008-12-24 最后一天最后一小时），均中英对照；
  - **补锚点**：正文与表格贯穿 primary/documents/chronicle/finance 交叉链接（e2002-10-03、e2010-06-29、e2015-01-20、e2021-10-25、e2022-07-13、e2025-03-28、e2025-11-06、c2008-12-23、d2022-04-25）；
  - **新增第五节案例深读**「2008：链条差点断掉的一年」——九十天窗口内 Flight 3 失败→第四发入轨→圣诞夜融资→NASA CRS 背靠背，四锚点串联；
  - **就地修复**：原第四节「2025.14.06」日期笔误 → 2025.11.06；融资表补 Google+Fidelity 2015 行。
- 结构对齐分析页；零新造事实（全部重组账本与扩展包既有材料）。

**质量门**
- verify.py 断链检查捕获一处错误锚点（e2008-12-23 不存在）→ 已改为编年史锚点 c2008-12-23 后复检全绿（11 项）；EPUB 重建满足新鲜度门禁。

## v5.94.0 — 2026-09-26 · 薄页充实：AI 战略布局页全量重写（自由精进第六十一轮）

**主题包成果**
- ai-strategy.html 4787 → 11812 字节（目标 8KB+ 达成），五个节点扩为六节完整叙事：
  - **补双语**：全页叶子节点补齐 data-en（此前整页无英文，违反双语约定）；
  - **补引语块**：两条账本已核实逐字引语入 blockquote（e2023-07-12 xAI 章程 + AI 安全论证中英对照；e2025-03-28 xAI 收购 X 推文）；
  - **补数据点**：finance xAI 节五轮融资轨迹表（B 轮 240 亿 → C 轮 400 亿 → 股权+债 → E 轮 2300 亿，2025 秋股权+债 100 亿+120 亿债务）；
  - **补锚点链接**：primary/finance/grok/capital-evolution 交叉链接贯穿；
  - **新增编者分析块**（显式标注）：捐资人→大股东的身份转换、估值跳升先于产品验证的赌注结构。
- 结构对齐其他分析页（小节标题+段落+数据框+引语+交叉链接）；不新造事实（全部重组站内已核实材料）。

**质量门**
- verify.py 11 项全绿（断链检查覆盖全部新锚点）；EPUB 重建满足新鲜度门禁。

## v5.93.0 — 2026-09-26 · 争议深化3：Twitter 内容审核篇扩写（自由精进第六十轮）

**主题包成果**
- controversy.html 第五篇 Twitter 内容审核三段 → 五段（增幅 100%+）：
  - **新增「欧盟 DSA 首案」段**：2023.10 Breton 警告信 → 2023.12 正式立案 → 2025.12.05 欧盟委员会开出 DSA 生效以来首张罚单 €1.2 亿（付费蓝勾「欺骗性」+ 广告商/研究者数据透明义务；The Register/AP/PCMag/Pinsent Masons 多源）；
  - **新增「两侧声音」段**（正反两面）：监管方「罚设计不罚观点」与 X 方公开批评罚款、美欧监管主权摩擦并列，罚款远低于上限的两种解读标注为编者观察；
  - **编者分析更新**：三案连读——美国第一修正案挡住删帖之手（工会案）vs 欧盟 DSA 对商业设计开罚，外部制衡的新变量。
- EXPANSION.md 记录 DSA 时间线（无新增 Musk 逐字引语，不新增语录卡）；CV_META twitter 摘要同步；索引重建（169 条不变）。
- 至此争议板块三篇深化全部完成（Autopilot v5.91.0 / 工会 v5.92.0 / Twitter 本轮）。

**质量门**
- 新事实多源互证（The Register/AP/PCMag/Pinsent Masons）；编者观察与转述立场严格标注；verify.py 11 项全绿；EPUB 重建满足新鲜度门禁。

## v5.92.0 — 2026-09-26 · 争议深化2：工会与劳动争议篇扩写（自由精进第五十九轮）

**主题包成果**
- controversy.html 第四篇工会篇三段 → 五段（增幅 100%+）：
  - **法律后果段精确化**：补 2024.01 第五巡回口头辩论时法官质疑 NLRB 救济权边界（Reuters）；
  - **新增「2024 年反转」段**：2024.10.25 第五巡回在 NLRB v. Tesla（No. 21-60285）以第一修正案为由撤销强制删帖令（NYT/HR Dive/案号互证）——删帖救济被撤销但违法底层认定未被推翻、公告栏张贴令保留；
  - **新增「更广的战线」段**：SpaceX 以 NLRB 结构违宪获禁制令暂停程序（Balls & Strikes 2025.11 评论框架，显式标注为编者引述）；
  - **编者分析更新**：终局从「推文边界」升维到「国家能否命令平台时代 CEO 删除自己的言论」（显式标注）。
- EXPANSION.md 记录新节点（与站内既有 2023.03 节点区分，保留不动）；无新增逐字引语，不新增语录卡。
- CV_META union 摘要同步新时间线；索引重建（条数不变 169）。

**质量门**
- 新节点 NYT/HR Dive/法院案号三源互证；评论性内容标注来源与性质；verify.py 11 项全绿；EPUB 重建满足新鲜度门禁。

## v5.91.0 — 2026-09-26 · 争议深化1：Autopilot/FSD 篇扩写（自由精进第五十八轮）

**主题包成果**
- controversy.html 第三篇 Autopilot/FSD 三段 → 五段（约 400 字 → 约 850 字，增幅 100%+）：
  - **监管线精确化**：2025.12.16 DMV 认定违法并暂缓 30 天销售/制造牌照吊销（条件：纠正营销）；2026.02.13 Tesla 起诉 DMV；
  - **新增「纠正与暂缓」段**：2026.02.17-18 Tesla 遵令在加州营销中停用「Autopilot」一词并修改材料，免于销售暂停——DMV 官方新闻稿（一手）+ Electrek + Guardian 三源互证；
  - **新增「Tesla 一侧」段**（正反两面）：FSD 需驾驶员全程监督、裁决误述能力（CNBC 转述起诉立场）；
  - **编者分析更新**：Tesla 保留「能力」表述权、只让出「Autopilot」一词本身的象征性结局（显式标注）。
- EXPANSION.md 记录三条新核实事实（含 DMV 官方新闻稿一手源）；无新增 Musk 逐字引语，不新增语录卡。
- build-search-index.py CV_META autopilot 条目 zh/bg 摘要同步新时间线；索引重建（条数不变 169）。

**质量门**
- 新事实均两源以上核实（DMV 官门口径优先）；verify.py 11 项全绿；EPUB 重建满足新鲜度门禁。

## v5.90.0 — 2026-09-26 · 检索扩容B：编年史与财务全景入索引（自由精进第五十七轮）

**主题包成果**
- **chronicle.html 编年史 53 行纳入检索**（新类型「编年史」）：每行注入稳定锚点 id——精确日期 c{Y-M-D}、年月 c{Y-M}、纯年份 c{Y-序号}（2022.07–10 区间日期按起始月定形；2025.03 重月自动后缀 -2）；d 字段沿用行内真实日期文本不虚构；bg 取所属公司节主线摘要。
- **finance.html 财务全景四节纳入检索**（新类型「财务全景」，id 沿用 tesla/spacex/x/xai）：d 取节内最新年份（Tesla 2025 / SpaceX 2024 / X 2025 / xAI 2026），q 与 bg 取节 intro 摘要。
- 同步三处：build-search-index.py 断言字典（169 条七类型）；verify.py 检查4 总数公式加 cy-ev 与 fn-co 计数；search.html 按钮组加「编年史」「财务全景」、页头板块描述同步。
- 公司过滤自动生效（实体推断复用）：编年史行按内容归 Tesla/SpaceX/X/xAI/PayPal 等，财务四节各归其主。

**质量门**
- build-search-index.py 断言通过（169 条）；chronicle 53 个新 id 无重复（verify 重复 id 检查覆盖）；verify.py 11 项全绿；EPUB 重建满足新鲜度门禁。

## v5.89.0 — 2026-09-26 · 检索扩容A：争议深读入索引（自由精进第五十六轮）

**主题包成果**
- **controversy.html 五篇深读纳入站内检索**（索引 107 → 112 条，新类型「争议深读」）：
  - tools/build-search-index.py 新增 controversy 解析段（CV_META 五条：sec-pedo/sec-sec/autopilot/union/twitter，q/zh/bg 均重组自页内已核实文字，d 取篇内首个关键年份）；
  - 断言字典同步 '争议深读': 5；
  - verify.py 检查4 总数公式加入 controversy 计数（ct-ch section 数）；
  - search.html 类型按钮组加「争议深读」。
- **就地修复**：search.html 页头 sr-sub 原写死「67 条/9 份/18 条/13 张」违反 v5.50 无写死计数原则——改为板块描述不带数字；controversy.html 页脚一处残破未闭合 `<p class="ct-foot"` 标签（渲染冗余行）修复。
- 公司过滤自动生效（实体推断复用）：sec-sec/union/autopilot→Tesla，twitter→Tesla+X/Twitter，sec-pedo→综合。

**质量门**
- build-search-index.py 断言通过（112 条五类型）；verify.py 11 项全绿；EPUB 重建满足新鲜度门禁；node --check 不适用（app.js 未改）。

## v5.88.1 — 2026-09-20 · 补账：CHANGELOG 漏记补录 + 版本误标澄清 + 门禁加固（自由精进第五十五轮）

**主题包成果**
- **三轮 CHANGELOG 漏记补录**（内容均已入库，仅缺账面；材料取自 git log 与 EXPANSION.md）：
  - **v5.84.0（补录）**：2013.05.08 Tesla 首次季度盈利（e2013-05-08，Q1 股东信逐字，CNET/IBD），账本 61 → 62，索引 102 条；
  - **v5.85.1（补录）**：2018.05.20 工会推文（e2018-05-20，The Indiana Lawyer/Reuters/CBS 逐字），账本 63 → 64，索引 104 条；
  - **v5.88.0（补录）**：2021.01.07 世界首富日（e2021-01-07，「How strange.」Economic Times/Bloomberg），账本 66 → 67，chronicle+语录卡+EXPANSION 同步，索引 107 条。
- **四处版本误标加注**（git 历史不改写，条目内加「勘误」小节）：v5.89.0（时序早于 v5.86-5.88 三轮，版本从未到达）、「v5.85.0 轮」（与 Google/Fidelity 轮重号）、「v5.80.0 轮」（与 Phase1-1 轮重号）、工会轮 git 误标 v5.88.0。
- **sync-changelog.py 解析修复**：标题含「 轮」后缀（如「v5.85.0 轮 —」）此前不匹配正则、条目被静默丢弃，changelog.html 实缺 2 条——正则已容忍该后缀。
- **verify.py 新增两道门禁**：① CHANGELOG 首条版本 = VERSION（防本轮这类漏记）；② EPUB 含最新账本锚点（防电子书过期）。
- reading.html 页首英文残留修复（"Chapters 4-10 are being rebuilt in place" → 十章齐备口径）；DEVLOG 待做清单与技术债同步。
- **musk-inc.epub 重建**：旧版构建于 v5.83.0 轮，此后账本 60 → 67 共 7 条新增、争议第五篇、打印 CSS 修复全部缺位，本轮一并补入。

**质量门**
- sync-changelog.py 重生成（143 条，v0.1.0 → v5.88.1）；build-epub.py 重建；verify.py 体检通过（含新增两检查）；node --check 通过。

## v5.88.0 — 2026-09-19 · 自由精进：账本扩容（+2021 世界首富日，67 条）（补录）

**勘误（v5.88.1 补注）**
- 本轮完成时漏记 CHANGELOG（git 241cbcc 已提交），由 v5.88.1 轮依 git log 与 EXPANSION.md 补录；commit 信息「账本 65→67」为笔误，实为 66 → 67。

**主题包成果**
- 言行实录 66 → 67 条：新增 **2021.01.07 世界首富日**（id e2021-01-07）——双推文逐字（“How strange.” / “Well, back to work …”，Economic Times/Bloomberg），Tesla 当日 +5% 收 $816、净资产 ≈$185-190B、终结 Bezos 全球首富地位。
- chronicle 补行 + quotes.html 语录卡 + EXPANSION.md 同步；索引 106 → 107 条。

**质量门**
- 67 条时序校验递增；verify.py 体检通过；node --check 通过。

## v5.87.0 — 2026-09-19 · 自由精进：全面打印 QA + revisions 表格防拆（自由精进第五十四轮）

**主题包成果**
- **打印 PDF 抽检五页**（controversy/chronicle/finance/reading/revisions），headless Edge + pypdf：
  - 全部无空白页、无返回链接泄漏；
  - controversy 5 页含 pedo guy/Autopilot/union dues/NLRB 全部关键术语；
  - chronicle 8 页含全部年份行；finance 4 页含收入/估值数据；
  - reading 10 页含十章标题；revisions 5 页含 100 锚点表。
- **就地修复**：revisions.html 缺表格行防拆规则——100 行表格会被跨页拆断，
  已补 `.rv-table tr { break-inside: avoid; }` + `.rv-table th { break-after: avoid; }`。

**质量门**
- 打印复验：controversy/chronicle/finance/reading/revisions 五页全部 ✓；
  verify.py 体检通过（32 页）；node --check 通过。

## v5.86.0 — 2026-09-19 · 自由精进：编年史全量同步尝试——回滚与策略调整（自由精进第五十三轮）

**过程记录**
- 尝试用脚本自动将账本 66 条全量同步到编年史——但自动生成的行缺少编年史的手写深度（背景/原话/现场/后续
  四段结构），且跨段插入导致 36 个年份重复。已回滚。
- **策略调整**：编年史定位为「精选节点 + 深读」而非「全量镜像 + 简行」。账本（primary.html）本身就是
  全量记录，编年史的价值在于筛选与叙述深度。当前 20 行（Tesla 12 + SpaceX 10 - 重叠）已覆盖所有
  关键商业转折点；后续账本扩容新增的条目将继续以「逐条精选」方式按需补入。

**结论**
- 无净变更（编年史回滚至 HEAD）。本轮产出：策略文档 + 工具教训（自动同步编年史不可取，需手动精选）。

## v5.89.0 — 2026-09-19 · 自由精进：账本扩容（+2025 xAI 收购 X，66 条）

**勘误（v5.88.1 补注）**
- 版本号误标：该轮 git（1be1eef）时序位于 v5.86/v5.87/v5.88 三轮之前，站点版本从未到达 v5.89——条目位置与内容保持原样，仅此说明。

**主题包成果**
- 言行实录 65 → 66 条：新增 **2025.03.28 xAI 收购 X**（id e2025-03-28）——
  本人推文逐字（CNBC/Forbes/AP 多源互证）：“@xAI has acquired @X in an all-stock transaction.
  The combination values xAI at $80 billion and X at $33 billion ($45B less $12B debt).”
- 后续线：2022 年 $44B 买入 → 2025 年 $33B 独立估值 → 并入后成为 $80B 公司一部分
  （「重新定价」为编者分析已标注）。与 chronicle X 部、finance.html X 部完整互链。
- 全链一次到位：语录卡 52 张、索引 106 条、时间轴 66 节点。

**质量门**
- 66 条时序校验递增；verify.py 体检通过；node --check 通过。

## v5.85.0 轮 — 2026-09-19 · 自由精进：账本扩容（+2019 Crew Dragon Demo-1 对接 ISS，65 条）

**勘误（v5.88.1 补注）**
- 版本号误标：git（2043e21）标 v5.85.0 与 Google/Fidelity 轮重号（时序在其后）；标题「 轮」后缀曾致 changelog.html 渲染丢失，v5.88.1 已修复解析。条目保持原样。

**主题包成果**
- 言行实录 64 → 65 条：新增 **2019.03.03 Crew Dragon Demo-1 自主对接 ISS**（id e2019-03-03）——
  首次商业航天器自主对接 ISS；行为条目（无逐字引语段，事实包无新增核实需求）。
  与 e2019-04-20（一个月后事故）和 e2020-05-30（载人首飞）构成 SpaceX 载人弧三联画。

**质量门**
- 65 条时序校验递增；索引 104 条；时间轴 65 节点；verify.py 体检通过；node --check 通过。

## v5.84.1 — 2026-09-19 · 自由精进：争议板块收尾（+Twitter 内容审核篇，5 篇齐备）

**主题包成果**
- controversy.html 新增第五篇（最后一篇）——**Twitter 内容审核与言论边界**：
  Tax the rich 投票（2021.11 逐字 BBC/Reuters/CNBC）+ 记者封禁（2022.12.15，Washington Post/NPR）
  + 编者分析（规则双标模式）。
- **争议板块五篇齐备**：SEC/pedo guy/Autopilot/工会/Twitter 内容审核。

**质量门**
- 5 篇深读渲染正常；verify.py 体检通过（32 页）。

## v5.85.1 — 2026-09-19 · 自由精进：账本扩容（+2018 工会推文，64 条）（补录）

**勘误（v5.88.1 补注）**
- 本轮 git 提交时误标 v5.88.0（dd13293，时序实际位于 v5.85.0 Google/Fidelity 轮之后、v5.84.1 内容审核轮之前），且当时漏记 CHANGELOG——由 v5.88.1 轮按时序补录并编为 v5.85.1。

**主题包成果**
- 言行实录 63 → 64 条：新增 **2018.05.20 工会推文**（id e2018-05-20）——「Nothing stopping… But why pay union dues & give up stock options for nothing」逐字核实（The Indiana Lawyer/Reuters/CBS）；与 controversy.html 工会篇完整互链。
- 索引 103 → 104 条；语录卡同步。

**质量门**
- 64 条时序校验递增；verify.py 体检通过；node --check 通过。

## v5.85.0 — 2026-09-19 · 自由精进：账本扩容（+2015 Google/Fidelity 入股 SpaceX，63 条）

**主题包成果**
- 言行实录 62 → 63 条：新增 **2015.01.20 Google+Fidelity 投资 SpaceX 10 亿美元**（id e2015-01-20）——
  行为条目（无逐字引语段，公告为 SpaceX 声明而非个人引语）；WSJ/Reuters/NYT 多源。
- 编年史 SpaceX 段 13 → 14 行（时序校验 2012.05.25 → 2015.01.20 → 2015.12.21）。
- 编者分析：卫星互联网星座→Starlink 收入引擎 / 估值 7 年→$350B（已标注）。

**质量门**
- 63 条时序校验递增；chronicle SpaceX 14 行断言；索引 103 条；时间轴 63 节点；verify.py 通过；node --check 通过。

## v5.84.0 — 2026-09-19 · 自由精进：账本扩容（+2013 Tesla 首次季度盈利，62 条）（补录）

**勘误（v5.88.1 补注）**
- 本轮完成时漏记 CHANGELOG（git 2e7c621 已提交），由 v5.88.1 轮依 git log 与 EXPANSION.md 补录；版本号沿用其 git 标签 v5.84.0（时序位于 pedo guy 轮之后，见其勘误注）。

**主题包成果**
- 言行实录 61 → 62 条：新增 **2013.05.08 Tesla 首次季度盈利**（id e2013-05-08）——Q1 2013 股东信逐字（Musk 执笔）：“Tesla reached profitability in the first quarter of 2013 for the first time in our ten year history.”（CNET/IBD，股东信全文可查）；非 GAAP 盈利 $15M、营收 ~$562M、股价当日 +24%。
- chronicle 补行 + EXPANSION.md 五行同步；索引 101 → 102 条。

**质量门**
- 62 条时序校验递增；verify.py 体检通过；node --check 通过。

## v5.80.0 轮 — 2026-09-19 · 自由精进：账本扩容（+2018 pedo guy 推文，61 条）

**勘误（v5.88.1 补注）**
- 版本号误标：git（0f4cc6d）实标 v5.80.1，时序位于 v5.83.0 电子书轮之后；CHANGELOG 标题误写 v5.80.0 与 Phase1-1 轮重号，且「 轮」后缀曾致渲染丢失（v5.88.1 已修复解析）。条目保持原样。

**主题包成果**
- 言行实录 60 → 61 条：新增 **2018.07.15 pedo guy 推文**（id e2018-07-15）——
  双推文逐字（“Sorry pedo guy, you really did ask for it.” + “Bet ya a signed dollar it's true.”），
  7.18 道歉句（“the fault is mine and mine alone”，BBC），
  12.06 陪审团裁决不构成诽谤（BBC/Guardian/NPR）。
- 与 controversy.html#sec-pedo 争议板块互链。
- 全链一次到位：语录卡 50 张、索引 101 条、时间轴 61 节点。

**质量门**
- 61 条时序校验递增；verify.py 体检通过；node --check 通过。

## v5.83.0 — 2026-09-19 · 新三阶段 Phase3：电子书打包上线（三阶段全部收官）

**主题包成果**
- 新工具 **tools/build-epub.py**：纯 Python zipfile 手写 EPUB 结构（零外部依赖），
  按章节顺序将 24 页编译为 25 章 XHTML → musk-inc.epub（112KB）。
  EPUB 结构含 mimetype/container.xml/content.opf/nav.xhtml 目录页，可在 Apple Books/Calibre/Kobo/手机打开。
- **三阶段全部收官**：Phase 1 修订历史 ✓ / Phase 2 争议板块 ✓ / Phase 3 电子书打包 ✓。

**质量门**
- EPUB 结构验证：mimetype 首位、OPF 存在、25 个 XHTML 章节文件、ch0 卷首有实质内容、
  ch12 (primary) 7818 字完整。verify.py 体检通过（32 页）。node --check 通过。

## v5.82.0 — 2026-09-19 · 新三阶段 Phase2-2：争议板块扩至四篇（Autopilot + 工会）

**主题包成果**
- controversy.html 新增两篇完整深读（四篇总计）：
  - **第三篇 Autopilot/FSD 安全争议**：加州 DMV 虚假广告指控（2022）→ 行政法官拒驳（2024.06）→
    DMV 认定违法（2025.12）→ Tesla 起诉 DMV（2026.02）；NHTSA 2024.10 对 240 万辆 FSD 展开调查；
    参议员 Markey 质疑「误导性和不完整的安全统计数据」（CNBC/PBS 口径）。
  - **第四篇 工会与劳动争议**：2018.05.20 推文逐字（「Nothing stopping… But why pay union dues & give up
    stock options for nothing」）+ NLRB(2019)/上诉法院(2023)/后续(2024) 六年法律战完整时间线
    （The Indiana Lawyer/Reuters/CBS 多源）。
- 「重组中」卡收缩为仅剩 Twitter 内容审核一篇。

**质量门**
- 4 篇深读渲染正常；verify.py 体检通过（32 页）；node --check 通过。

## v5.80.0 — 2026-09-19 · 新三阶段 Phase1-1：修订历史系统上线

**主题包成果**
- 新工具 **tools/build-revisions.py**：解析 git log（99 次相关提交逐条比对锚点集合增减），
  为每个第一手锚点生成完整生命周期（创建版本/续存提交数/是否移除），只保留当前在册锚点。
- 新页 **revisions.html「修订历史」**：100 个在册锚点的修订轨迹表（板块/锚点 ID/状态/修订轨迹/原文链接），
  研究者可验证任何一条内容是否被悄悄修改过。
- **index.html 章节卡**新增「修订史」入口；verify.py 新增「修订历史一致性」检查（100 锚点 ≥50 阈值）。

**质量门**
- verify.py 八项全绿（新增修订历史检查）；30 页面 + revisions.html；断链零；node --check 通过。

## v5.79.0 — 2026-09-19 · 自由精进：账本扩容（+2017 首辆 Model 3 下线，60 条里程碑）

**主题包成果**
- 言行实录 59 → 60 条：新增 **2017.07.09 首辆生产版 Model 3 下线**（id e2017-07-09）——
  双推文逐字（“First Production Model 3” + “Production unit 1 … final checkout”，Forbes/AP/CNBC 多源），
  落位 e2017-03-30 与 e2017-07-28 之间（时序校验递增）。
- **检索索引破百：100 条第一手锚点。**

**质量门**
- 60 条时序校验递增；chronicle Tesla 行序断言（20 行）；verify.py 体检通过；node --check 通过。

## v5.78.0 — 2026-09-19 · 自由精进：账本扩容（+2013 DOE 贷款还清，59 条）

**主题包成果**
- 言行实录 58 → 59 条：新增 **2013.05.22 DOE 贷款提前九年还清**（id e2013-05-22）——行为条目，
  **零新增核实**（来源为事实包既有 Tesla IR/NYT DealBook/CSMonitor 记录）。
- 贷款弧闭环：e2009-03-26（批准/放款）→ e2013-05-22（还清），「唯一全额还清 ATVM 的企业」入册。

**质量门**
- 59 条时序校验递增（e2013 → e2013-05-22 → e2013-08-12）；chronicle Tesla 行序断言；
  索引 99 条；时间轴 59 节点；verify.py 体检通过；node --check 通过。

## v5.77.0 — 2026-09-19 · 自由精进：账本扩容（+2019 Crew Dragon 事故，58 条）

**主题包成果**
- 言行实录 57 → 58 条：新增 **2019.04.20 Crew Dragon 静态点火爆燃**（id e2019-04-20）——行为条目
  （两轮检索无马斯克本人逐字引语，按纪律不做引语段；公司表态归 Koenigsmann 并显式署名）。
- 调查线核实：故障单向阀 NTO+钛点燃（SpaceNews 7-15）→ SuperDraco 弃着陆 → 2020-01 逃逸测试完美
  → 2020-05 载人（与 e2020-05-30 呼应）。
- 甄别记录：网络流传的两句「Musk 推文」无法核实，未入册（EXPANSION.md）。

**质量门**
- 58 条时序校验递增；chronicle SpaceX 段行序断言（14 行）；索引 98 条；时间轴 58 节点；
  verify.py 体检通过；node --check 通过。

## v5.76.0 — 2026-09-19 · 自由精进：账本扩容（+2012 Dragon 对接 ISS，57 条）

**主题包成果**
- 言行实录 56 → 57 条：新增 **2012.05.25 龙飞船首次对接国际空间站**（id e2012-05-25）——
  首个商业航天器与 ISS 对接；三句核实引语（新时代黎明发布会句 / Dragon captured 推文 /
  溅落日 overwhelmed with joy）；与 22 天后的 Model S 交付构成「双子月」对照（编者分析已标注）。
- 流程：先查账本确认无 C2+/ISS 覆盖才启动核实；全链一次到位（48 卡 / chronicle SpaceX 13 行 /
  索引 97 条 / 时间轴 57 节点）；版本步进 import 三件套（glob 教训固化）。

**质量门**
- 57 条时序校验递增；chronicle SpaceX 段行序断言；verify.py 体检通过；node --check 通过。

## v5.75.0 — 2026-09-19 · 自由精进：账本扩容（+2008 Flight 3 失败夜，56 条）

**主题包成果**
- 言行实录 55 → 56 条：新增 **2008.08.02 Falcon 1 第三次发射失败**（id e2008-08-02）——
  与 e2008-09-28 构成「最黑一夜 → 五十七天后黎明」的完整弧；失败原因（残余推力致两级再撞）
  经 Space.com/维基口径核实；双引语（Universe Today 标题句 + 传记「最后一枚火箭」句）入册。
- 同轮纪律执行：放弃「2013.11 Gruber/NYPSC」候选（两轮检索无逐字来源，疑为记忆混淆），
  甄别记录入 EXPANSION.md。

**质量门**
- 56 条时序校验递增；chronicle SpaceX 段行序断言（11 行）；语录卡 47 张；
  verify.py 体检通过；node --check 通过。
- 工程注记：版本步进脚本两次漏 import glob（v5.72/v5.75），均为 verify 一致性检查当场抓到——
  该检查已把这类半成品提交完全挡在门外；后续版本步进将统一 import io, re, glob 三件套。

## v5.74.0 — 2026-09-19 · 自由精进：README 同步站点现状（自由精进第四十二轮）

**主题包成果**
- README.md 结构表 27 → 30 页：补入 v5.42 之后新增的三页——**长卷阅读版 reading.html**（十章书籍形态）、
  **chronicle.html 四公司编年史**、**finance.html 财务资本全景**；
- 主题深读行补「资本解剖（含流向图）」；研究功能补体验注：落点高亮（1.8 秒）与时间轴悬停引文预览；
- 账本行改为「第一手言行账本（2002→2026，随迭代增长）」——延续无计数原则。

**质量门**
- verify.py 体检通过（30 页）；README 与实际页面清单一致（30 个 HTML）。

## v5.73.0 — 2026-09-19 · 自由精进：计数声明最终清扫（自由精进第四十一轮）

**主题包成果**
- 活跃 UI 计数漂移清零（延续 v5.50 原则）：
  - reading.html 第十章链接「核实组 42 条全录」→「已核实引语全录」（该数字已漂移 4 轮）；
  - primary.html 时间轴 aria-label「44 个节点」→ **生成器动态写入实际节点数**（现显示 55）——
    从根上消除未来漂移。
- grep 全站复验：活跃 UI 已无任何写死的条目/卡片/节点计数。

**过程注记**
- 生成器行内 `
` 转义在本轮 shell 链中三次变为真实换行（SyntaxError × 3），最终用 chr(92) 显式构造
  反斜杠绕开转义歧义——嵌套引号+转义的场景，字符码构造是唯一可靠解。

**质量门**
- 新 aria-label 显示 55 节点；verify.py 体检通过；node --check 通过。

## v5.72.0 — 2026-09-19 · 自由精进：账本扩容（+2023 X 品牌更替，55 条）

**主题包成果**
- 言行实录 54 → 55 条：新增 **2023.07.23 X 品牌更替推文**（id e2023-07-23）——
  “And soon we shall bid adieu to the twitter brand and, gradually, all the birds.”
  （Reuters/NYT/PBS 多源逐字）。X 公司叙事线的品牌里程碑补全。
- 后续线：24 小时内鸟标退役/X.com 上线 → 8 个月后并入 xAI（与 e2025-03 语境呼应）。
- 全链同步一次到位：语录卡 46 张、chronicle X 部 +1 行、索引 95 条、时间轴 55 节点。

**质量门**
- 55 条时序校验递增；chronicle X 段行序断言；verify.py 体检通过；node --check 通过。

## v5.71.0 — 2026-09-19 · 自由精进：账本扩容（+2020 Fremont 复工抗命，54 条）

**主题包成果**
- 言行实录 53 → 54 条：新增 **2020.05.11 Fremont 违令复工推文**（id e2020-05-11）——
  「Tesla is restarting production today against Alameda County rules… If anyone is arrested, I ask that it only be me.」
  （NPR/NBC/LA Times 多源逐字）。2020 年叙事线补全：停摆 → 违令复工 → 载人龙 → Battery Day。
- 流程改进：**先查账本再核实**（上上轮 Cybertruck 重复核实教训的直接应用）——本轮开工前 grep 确认
  无 e2020-05-11 才启动 WebSearch。
- 全链同步一次到位：语录卡 45 张（proactive，未等一致性检查抓）、chronicle Tesla +1 行（写盘后断言行序）、
  索引 94 条、时间轴 54 节点。

**质量门**
- 54 条时序校验递增；verify.py 体检通过；node --check 通过。

## v5.70.0 — 2026-09-19 · 自由精进：时间轴 hover 摘要升级（自由精进第三十八轮）

**主题包成果**
- 两处时间轴的悬停摘要加入**引文片段**（截断 64 字、次级灰白斜体）：
  - timeline.html 泳道大时间轴（gx-tip）：105 个 hover 点全部带引文（数据源 search-index 的 q 字段）；
  - primary.html 账本时间轴（pt-tip）：53 个节点中 47 个带引文（有引语段的条目全部覆盖）。
  时间轴从「导航工具」升级为「预览工具」——hover 即读原话开头，点击才进现场。
- 顺手修复存量瑕疵：pt-tip 日期重复显示（「2019.09.28 2019.09.28 · 出处」→ 只留一处）。
- 工程修复：build-ledger-timeline.py 的尾部可选组被懒惰匹配吞掉（引文提取恒空），
  改为整块捕获 + 逐字段提取（与 verify.py 白名单检查同法）。

**质量门**
- 两处 tip 实测含引文片段（含 Starship「I'm in love with steel」样例）；53 节点重建一致；
  1280/375 双宽零溢出；verify.py 体检通过；node --check 通过。

## v5.69.0 — 2026-09-19 · 自由精进：锚点落点高亮（自由精进第三十七轮）

**主题包成果**
- 全站七类锚点目标（ps-row / doc-article / iv-item / tweet-card / cy-year / fn-row / rd-ch）
  新增 `:target` 落点高亮：1.8 秒淡黄闪光渐隐——引用跳转后视觉立刻定位目标条目。
- `prefers-reduced-motion` 用户改为静态酒红轮廓（无闪烁）。
- 覆盖全部引用入口：账本日期徽章、语录卡、编年史行、财务行、长卷章节、检索结果。

**质量门**
- 页内注入等价规则实测 :target 动画正确触发（tgt-flash/1.8s）；curl 确认服务器端新规则在位；
  IAB 缓存问题沿用既定证据链方法（file:// 真实使用无影响）；1280/375 双宽零溢出；node --check 通过。

## v5.68.0 — 2026-09-19 · 自由精进：Cybertruck 条目补第二引语块（自由精进第三十六轮）

**主题包成果**
- e2023-11-30（Cybertruck 首批交付）追加第二引语块：USA Today 记录完整句
  “The apocalypse could come along at any moment, and here at Tesla we have the finest in Apocalypse technology.”
  + Forbes 逐字确认的「apocalypse-proof」（两源互证，上轮核实成果转化入册）。
- EXPANSION.md 补记甄别记录（「final masterpiece」未证实未入册；2019/2023 玻璃对照）。

**复盘注记**
- 上轮「补原话段」的前提是错的——该条目本就有原话段与语录卡（引语为 future/experts 两句）。
  本轮改为追加第二引语块，核实工作未浪费；教训：先 grep 再 WebSearch。

**质量门**
- 双引语块渲染复验；白名单校验不变（同条目加块不改卡片映射）；1280/375 零溢出；
  verify.py 七项全绿；node --check 通过。

## v5.67.0 — 2026-09-19 · 自由精进：账本扩容（+2017 Semi 发布会，53 条）

**主题包成果**
- 言行实录 52 → 53 条：新增 **2017.11.16 Tesla Semi 发布会**（id e2017-11-16），与 e2017-07-28 生产地狱、
  e2018-01-28 火焰喷射器构成 2017-2018 的时间弧。
- 引文核实（WebSearch）：「fastest production car ever made, period.」（WAMU/NPR 逐字；Reuters/Bloomberg/CNBC
  多源印证）；数据：Roadster 0-60 1.9 秒/约 $20 万，Semi 空载 5 秒/满载 20 秒。
- 后续线：Semi 2022.12 实际运营、Roadster 跳票多年——「头条对冲坏消息」为编者分析（已标注）。

**质量门**
- 53 条时序校验递增；verify.py 体检通过；node --check 通过。
- 一致性检查再次当场抓到漏卡（e2017-11-16）——已补卡 43 → 44 并重排时序，校验恢复全绿（5.67.1）。
- **编年史同步（5.67.2/5.67.3）**：chronicle.html Tesla 段同步账本新增节点——+6 行
  （2009.03.26 原型 / 2010.06.29 IPO 日 / 2016.07.20 Part Deux 与 SolarCity / 2017.11.16 Semi+Roadster /
    2021.10.25 Hertz 万亿日 / 2022.07.13 诉讼判决），行序 12 → 17 行且全局递增；
  SpaceX 段补 2019.09.28 Starship Mk1 一行（10 行齐备，diff 核对其余 7 节点已在位）。

## v5.66.0 — 2026-09-19 · 自由精进：账本扩容（+2011 猎鹰重型公布，52 条）

**主题包成果**
- 言行实录 51 → 52 条：新增 **2011.04.05 猎鹰重型公布**（id e2011-04-05），填补 2011 年空缺，
  落位 e2010-06-29 与 e2012-06-22 之间（时序校验递增）。
- 引文核实（WebSearch）：官方新闻稿逐字「载荷两倍多、成本不到三分之一」；数据口径
  （53 吨 vs 117 吨 LEO、$80-125M vs $350M+）NPR 报道印证。
- 后续线：首飞目标 2013 → 实际 2018-02-06（七年滑期），与 e2018-02-06 首飞条目前后呼应；
  「日期会滑，规格不缩水」为编者分析（已标注）。

**质量门**
- 52 条时序校验递增；verify.py 体检通过；node --check 通过。
- 新增的一致性检查当场抓到漏卡（e2011-04-05 有引文未上卡）——已补卡 42 → 43 并重排时序，校验恢复全绿。

## v5.65.0 — 2026-09-19 · 自由精进：账本扩容（+SolarCity 诉讼判决，51 条）

**主题包成果**
- 言行实录 50 → 51 条：新增 **2022.07.13 特拉华衡平法院 SolarCity 诉讼判决**（id e2022-07-13），
  与 e2016-11 收购条目首尾呼应：2016 创立→收购、2022 判决、2023 州最高法院维持「entirely fair」。
- 三源核实（Morris James / Justia / Dechert）；判决理由两条结构性保障（独立委员会 + 少数股东投票）入册。
- 过程注记：首插落在 4 月条目之前（时序审计抓出），已移正至 4.14 与 10.26 之间的正确时序位。

**质量门**
- 51 条时序校验递增；verify.py 体检通过（含语录卡白名单 42/45/3 平衡）；node --check 通过。

## v5.64.0 — 2026-09-19 · 自由精进：账本扩容（50 条里程碑：Model S 原型发布）

**主题包成果**
- 言行实录 49 → **50 条里程碑**：新增 **2009.03.26 Model S 原型发布**（id e2009-03-26），
  行为条目（无逐字引语段，媒体转述为主——原话无逐字公开，按纪律不做引语段）。
- 落位 e2008-12-24 与 e2010-06-29 之间（时序校验全局递增）；2009 年账本空缺补上。
- 后续线多项来源核实：DOE ATVM 4.65 亿（2009.06 有条件批准 Tesla IR / 2010.01 放款 DOE 页 /
  2013.05 提前九年还清 NYT DealBook）。

**联动更新**
- search-index.js 重生成 90 条；search.html 计数文案「言行实录 50 条」；时间轴重建 50 节点；索引断言同步。

**质量门**
- 50 条时序校验递增；verify.py 体检通过；node --check 通过。

## v5.63.0 — 2026-09-19 · 自由精进：一致性校验扩展 + 全类型 bg 字段（自由精进第二十九轮）

**主题包成果**
- **检索匹配扩展**：search-index.js 为全部类型补 bg 字段（documents=本站注释段、interviews=ctx 背景、
  x-posts=tweet-note），关键词召回面进一步加宽（与检索页 bg 匹配早已就位形成闭环）。
- **verify.py 一致性校验升级**：
  - 新增「时间轴节点数 = 账本条目数」检查（漏跑 build-ledger-timeline 会被当场抓住）；
  - 新增「语录核实组卡覆盖」白名单精确核对：每张卡必须有对应引文块、每个有引文块必须上卡或命中
    豁免白名单（e2013 在格言组 / e2021-07 转述 / e2025 统计行）——当前 42 卡 / 45 引文块 / 豁免 3，精确平衡。

**过程修复**
- 白名单检查首版引用了 findall 单捕获组的返回值（id 字符串而非整块文本），containment 恒假；
  逐字复刻调试定位后改为双捕获组。

**质量门**
- verify.py 六项检查全绿（新增两项）；build-search-index 重建后 89 条不变（bg 只加字段不改条数）。

## v5.62.0 — 2026-09-19 · 自由精进：语录核实组补卡（40 → 42）+ Hertz 条目补「原话」段

**主题包成果**
- quotes.html 核实组 40 → 42：补入 **2019 Starship「Honestly, I'm in love with steel.」** 与
  **2021 Hertz 对冲推文**（“No contract has been signed yet … zero effect on our economics.”）两张卡，
  时序重排后全局 2002→2025。
- **账本质量补课**：e2021-10-25 条目原缺「原话」段（两条推文引文嵌在叙述里）——按账本四段规范补上
  逐字「原话」段（NPR/CNBC 口径），现与四段结构一致。
- reading.html 第十章计数引用同步（核实组 42 条）。

**工程修复**
- 发现并修复「改内存未写盘」丢改：多文件连环修改脚本在中途读写其他文件时，前一个文件的修改必须
  当场写回——本轮 primary.html 的原话段一度丢失，复验探针抓到后单独补写。

**质量门**
- 核实组 42 卡时序递增、新卡内容正确；账本四段结构复验（背景/原话/现场/后续）；
  1280/375 双宽零溢出；verify.py 体检通过；四工具流水线全绿。

## v5.61.0 — 2026-09-19 · Phase3 账本扩容（+2 条：Hertz 万亿日 / SolarCity 创立）

**主题包成果**
- 言行实录 47 → 49 条：
  - **2021.10.25 Hertz 订单与万亿市值日**（e2021-10-25）：10 万辆订单当日市值首破万亿；一周后对冲推文
    「no contract has been signed yet」「zero effect on our economics」致约 400 亿美元蒸发——
    一句话双向撬动市值的经典样本（引文 WebSearch 多源核实）。
  - **2006 SolarCity 创立**（e2006，年份级日期）：账本最早段补齐能源第三家公司的起源，
    与 2016.11 收购条目首尾呼应。
- 两条落位时序正确（SolarCity 插于 2002 与 2006.08 之间；Hertz 插于 2021.08 与 2022.04.14 之间）。

**联动更新**
- search-index.js 重生成 89 条；search.html 计数文案「言行实录 49 条」；时间轴重建 49 节点；索引断言同步。

**质量门**
- verify.py 体检通过；node --check 通过；全局时序校验递增。

## v5.60.0 — 2026-09-19 · 新三阶段 Phase3-2 第二批：X 与 xAI 财务部补齐（财务全景四部齐备）

**主题包成果**
- finance.html 补齐第三、四部（22 行、4 条编者分析全部标注）：
  - **第三部 X**：440 亿收购（含约 130 亿银行债务）→ 收入 5.2B→3.4B→2.5B → Fidelity 减记 -72%→-80%
    （隐含 19B→9.4B）→ 2025.03 并入 xAI 时作价 33B 重估反转。
  - **第四部 xAI**：B 轮 60 亿@240 亿（2024.05）→ C 轮 60 亿@约 400 亿（2024.12.23，x.ai 官方）→
    2025 秋 100 亿股权+120 亿债 → E 轮 200 亿@2300 亿（2026.01）。
- 数据核实：Reuters/CNBC/Forbes（xAI B 轮）、x.ai 官方（C 轮公告）、Fortune/Axios/USA Today（X 收入与减记）。
- 「X 越买越便宜」「xAI 与 2002 SpaceX 同构」为编者分析（已标注）。

**质量门**
- 四部 id 齐全（tesla/spacex/x/xai）、22 行 4 注、跨页锚点抽测到位（d2022-04-25）；
  1280/375 双宽零溢出；verify.py 体检通过（30 页）；node --check 通过。

## v5.59.0 — 2026-09-19 · 新三阶段 Phase3-2：财务资本全景第一批（Tesla + SpaceX）

**主题包成果**
- 新页 **finance.html「财务资本全景」**：融资-估值-收入三轴，Tesla / SpaceX 两部上线（X / xAI 下批）。
  - **Tesla**：A 轮 750 万 → 圣诞夜融资 → IPO 2.26 亿 → 万亿市值 → 万亿激励；2023 收入 96.8B/交付 181 万、
    2024 收入 97.7B（+0.95%）/经营现金流 14.9B（Macrotrends/Tesla 10-K 口径）。
  - **SpaceX**（未上市，报道口径）：自投 1 亿 → NASA 16 亿 → 估值 46B（2020.08）→ 74B → 100.3B（2021.10）→
    127B（2022.06）→ ≈150B（2023）→ ≈350B（2024.12 tender）。
- 编者分析两处已标注：Tesla 2024 增长贴地=定价页「使用边界」的年度验证；SpaceX 无 IPO 资本结构的前提。
- 「$1.75T IPO」等未证实说法未收录；X/xAI 部以过渡卡示明下批补齐。

**质量门**
- 锚点抽测跳转到位（e2008-12-24）；10 节点导航 aria-current 正确；1280/375 双宽零溢出；
  verify.py 体检通过（30 页）；node --check 通过。

## v5.58.0 — 2026-09-19 · 新三阶段 Phase3 账本扩容（自由精进并入：+2 条）

**主题包成果**
- 言行实录 45 → 47 条：
  - **2019.09.28 Starship Mk1 发布**（e2019-09-28）：「Honestly, I'm in love with steel.」（Ars Technica/
    Popular Mechanics 双源）；日期恰为猎鹰一号入轨十一周年；材料换钢的供应链哲学注脚（编者分析已标注）。
  - **2010.06.29 Tesla IPO**（e2010-06-29）：行为条目（无引语段，索引降级提取背景段），四类资金序列第三类。
- 「liquid silver / insane」等未证实措辞按纪律甄别未入册（EXPANSION.md 记录甄别过程）。

**联动更新**
- search-index.js 重生成 87 条；search.html 计数文案「言行实录 47 条」；时间轴重建 47 节点；索引断言同步。

**质量门**
- 两条目时序落位正确（全局递增）；verify.py 体检通过；node --check 通过。

## v5.57.0 — 2026-09-19 · 新三阶段 Phase3-1 第二批：X 与 xAI 编年史补齐（编年史四部齐备）

**主题包成果**
- chronicle.html 补齐第三、四部：
  - **第三部 X（原 Twitter）10 节点**：54.20 要约 → 协议签署（8.3/9.9 条）→ 反悔被诉 → let that sink in →
    交割 → the bird is freed → Extremely Hardcore → Twitter Files → 更名 X 与广告主风波 → 并入 xAI；
  - **第四部 xAI 5 节点**：成立宣言 → Grok 首发 → Grok-1 开源 → 全股票收购 X → Series E。
- **编年史四部齐备**（36 个年份行、29 个跨页锚点），页头副题更新「四部全部上线」。
- 全部节点来自事实扩展包（含 grok/x-posts/ai-strategy 既有核实锚点），零新增核实需求。

**质量门**
- 四部 id 齐全（tesla/spacex/x/xai）；跨页锚点抽测跳转到位（d2026-01）；1280/375 双宽零溢出；
  verify.py 体检通过（29 页）。

## v5.56.0 — 2026-09-19 · 新三阶段 Phase3-1：四公司编年史第一批（Tesla + SpaceX）

**主题包成果**
- 新页 **chronicle.html「四家公司编年史」**：只收本站已核实节点的逐年编年，空缺年份显式声明「不代表无事发生」。
  本批上线两部：
  - **Tesla 12 个节点**（2004 A 轮 → 2025 万亿薪酬），全部锚点互链账本/定价/资本页；
  - **SpaceX 9 个节点**（2002 创立 → 2024 接塔），含 NASA 16 亿与复飞线。
  零新增核实需求（全部为事实包既有锚点）。X 与 xAI 两部以「重组中」卡过渡，下批补齐。
- 布线：index 章节卡 10 子链接新增「编年史」。

**质量门**
- 21 个年份行、24 个锚点互链；账本锚点抽测跳转到位；9 节点导航 aria-current 正确；
  1280/375 双宽零溢出；verify.py 体检通过（29 页）；node --check 通过。

## v5.55.0 — 2026-09-19 · 新三阶段 Phase2-2：资本流向图并入（第二阶段收官）

**主题包成果**
- capital-evolution.html 顶部新增**资本流向图**（简化 Sankey，纯 SVG 手写）：
  左带 PayPal 套现 ≈$180M（2002.10，宽度等比 1px≈$1M）→ 三条流带拆入 SpaceX ≈$100M /
  Tesla ≈$70M / SolarCity ≈$10M；右列标注六项关键后续资本事件（NASA $1.6B / Tesla IPO $226M /
  万亿市值与激励 / SolarCity $2.6B 并回 / xAI $20B Series E），非等比并显式注明。
- 原生 SVG title 实现 hover 数值；窄屏容器内横滑（min-width 680）；打印防拆且解除横滑；
  全部数字来自事实扩展包，零新增核实。

**质量门**
- SVG 渲染 3 条流带 + 10 处金额标注；1280/375 双宽零溢出；容器横滑不破审计；verify.py 通过。

## v5.54.0 — 2026-09-19 · 新三阶段 Phase2-1：全局泳道大时间轴（timeline.html 升级）

**主题包成果**
- timeline.html 顶部新增**全局泳道大时间轴**：85 条一手材料按 Tesla（30）/ SpaceX（18）/ X·Twitter（23）/
  xAI（5）/ 其他（16）五条泳道并列——同年跨公司的并行推进一目了然（多项多公司条目在多条泳道各出现一次）。
- 交互：年份下拉缩放（全部年份 ↔ 单年按月定位，1/3/5/7/9/11 月刻度）、圆点 hover 摘要（日期+出处）、
  点击直达对应锚点（实测 e2020-05-30 跳转到位）。
- 数据源 search-index.js 与检索页同源（含公司实体字段），账本/文档/访谈/帖史变动后重跑
  build-search-index 即自动同步。纯 CSS/JS，零图表库；窄屏容器内横滑；打印隐藏。

**质量门**
- 五泳道渲染与计数正确；缩放 2020 仅显示当年条目；月份刻度浮点漂移已修（Math.round）；
  点击跳转到位；1280/375 双宽零溢出；verify.py 通过。

## v5.53.0 — 2026-09-19 · 新三阶段 Phase1-3：长卷后段五章填充——十章齐备（第一阶段收官）

**主题包成果**
- 长卷阅读版后段五章一次填充，**十章齐备**：
  - 陆 · 监管与失败（SEC 罚单/Amos-6/SolarCity 诉讼两条学费线，互链深读 03/04 与账本）
  - 柒 · 方法论（六卡浓缩+边界条件，互链 playbook/persona）
  - 捌 · 资本与定价（资本四模式+定价三角，汇合至万亿美元薪酬与 Series E）
  - 玖 · 供应链（工厂即产品/自动化之错/零件合并/整合判据，互链供应链页）
  - 拾 · 收束（五句跨 23 年核实引语，互链账本五条目与语录页）
- 「重组中」跳转区块全部移除；目录 10 锚全内联；页头副题更新「十章齐备」。

**过程注记**
- 插入锚点注释与实际标记不一致导致首次替换失败（原子性保住，片段误删一次后重写并在同一脚本内完成插入）。

**质量门**
- 10 章 id 齐全（ch1-ch10）、目录内锚一一对应、跳转实测、双宽零溢出、verify.py 体检通过；node --check 通过。

## v5.52.0 — 2026-09-19 · 新三阶段 Phase1-2：长卷中段两章（肆 公司史 / 伍 商战）

**主题包成果**
- 长卷阅读版新增两章（重组自站内已核实材料，零新造）：
  - **肆 · 公司史四部曲**：Tesla（成本曲线护城河）/ SpaceX（一次性→可复用）/ X（买下的广场）/
    xAI（资本速度追使命），每段互链定价/供应链/协议/公告锚点。
  - **伍 · 经典商战四篇**：2008 双至暗 / 生产地狱 / funding secured / 440 亿收购攻防，
    互链账本双条目、协议条款、stories 与深读页。
- 目录肆/伍改为内部锚点（内锚 5 = 章节 5 对应）；「重组中」区块更新为第六至十章。

**质量门**
- 5 章齐全、目录内锚一一对应、跳转落位 70px、重组区文案更新；1280/375 双宽零溢出；
  verify.py 体检通过（28 页）；node --check 通过。

## v5.51.0 — 2026-09-19 · 新三阶段 Phase1-1：长卷阅读版上线（框架 + 前三章）

**主题包成果**
- 新页 **reading.html「长卷阅读版」**：书籍形态的连续叙事，与既有引用式页面互补。
  本轮交付框架 + 前三章：
  - 壹 · 卷首「一亿八千万，拆成三份」（2002 分配 → 2008 双至暗 → 二十年展开，全部锚点互链）
  - 贰 · 速览与人格（六种行为模式浓缩 + persona/playbook 互链）
  - 叁 · 时间线（2002→2026 六时代叙事，年份词逐一链到账本条目）
- 阅读体验：桌面 sticky 侧目录（IntersectionObserver 高亮当前章）、app.js 阅读进度条复用、
  章节锚点 scroll-margin、打印分章换页；窄屏目录转顶部面板（≤960px）。
- 四至十章以「重组中」跳转卡过渡（指向对应既有板块），后两轮填充。
- 已知取舍：长卷中文为主，标题/导语带 data-en，正文暂不做全量英译；页面暂未放语言切换按钮。

**布线**
- index.html 章节卡 10 子链接新增「长卷版」。

**质量门**
- 目录跳转与滚动高亮实测（#ch3 落位 70px + rd-on 切换）；16 个外链/锚点有效；
  1280/375 双宽零溢出；tools/verify.py 体检通过（28 页）；node --check 通过。

## v5.50.0 — 2026-09-19 · 自由精进：全站数字一致性走查（自由精进第二十七轮）

**主题包成果**
- 普活全站计数声明，抓到主漂移：**页脚「17 个版本，从 v0.1 到 v1.0」**散布在 12 个页面
  （v1.0.0 时代写的快照文本，实际已迭代至 v5.x、近 100 个版本）。
- 修复策略：改为**版本无关表述**「由定时自主迭代持续构建 · 完整修订史见『修订记录』」
  （中英双语 data-en 同步）——从根上杜绝 future 漂移。
- README.md 快照数字同步（账本 45 条标注「随迭代增长」、CHANGELOG 计数改为非快照表述）。
- changelog.html 中残留的同类字样为 v1.0.0 历史修订原文，按「历史记录不改写」原则保留。

**质量门**
- tools/verify.py 四项全绿；活跃页脚零残留（grep 复验）。

## v5.49.0 — 2026-09-18 · 自由精进：深读页表格窄屏打磨（自由精进第二十六轮）

**主题包成果**
- deep-dive-01 融资节点表格窄屏改造：表格包进滚动容器（min-width 560px，窄屏左右滑动查看），
  ≤640px 显示「← 左右滑动查看完整表格 →」提示；此前 4 列被压进 320px（数字列 nowrap 挤压其余列，可读性差）。
- 打印还原：@media print 下容器 overflow 恢复 visible、min-width 归零、提示隐藏——PDF 中表格完整呈现。

**质量门**
- 375px 实测：容器可滑（表 560px）、提示显示、页面零溢出；1280px 表格自然全宽无滚动；
- 打印 PDF 验证：五笔金额（$7.5M/$100M/$226M/$1.6B/$20B）全部在文、滑动提示未打印；node --check 通过。

## v5.48.0 — 2026-09-18 · 自由精进：语录核实组收尾批（23 → 40 条，核实组封顶）

**主题包成果**
- quotes.html 核实组一次性补齐全部剩余 17 条有引文条目：机器造机器（2016）/ NASA 载人首飞（2020）/
  Battery Day（2020）/ Investor Day（2023）/ xAI 宣言（2023）/ Telepathy（2024）/ Robotaxi（2024）/
  Starbase 建市（2025）/ Part IV（2025）等。核实组 40 条封顶——账本全部有逐字引文的条目均已上卡。
- 按纪律跳过 5 项：e2016-11 与 e2018-12-18（无引文段）、e2013（已在上方格言组）、e2021-07（转述非
  第一人称）、e2025（统计行非引语）。
- 出处标签直接取账本 ps-src（自动截断 40 字），来源与账本严格一致。

**工程修复**
- 年份无月份的日期（如"2016"）使排序函数崩溃——date_of 改为月份可选；上轮「同一位置重复插入」
  切坏多字节的教训延续：本轮全程使用片段文件 + 整网格单次重建，文件原子性未破坏。

**质量门**
- 40 卡全局时序复验通过（2002.10.03 → 2025.11.06）；跳转实测到位；出处无乱码；
  1280/375 双宽零溢出；tools/verify.py 体检通过。

## v5.47.0 — 2026-09-18 · 自由精进：语录核实组第四批（18 → 23 条）

**主题包成果**
- quotes.html 核实组再扩容：新增 5 张引语卡——2015 Powerwall 发布会（“existing batteries… suck”）/
  2017「Welcome to production hell!」/ 2019 Cybertruck 发布会装甲玻璃现场 / 2022 收购要约
  （“I don't care about the economics at all”）/ 2024 Starship 第五飞「The tower has caught the rocket!!」。
- 核实组现 23 条、覆盖 2002–2024，全部从账本程序化提取（逐字一致）+ 专属出处标签 + 全局时序。

**过程修复**
- 首次插入用「同一位置重复插入」导致多字节字符切坏（乱码+结构损坏+375px 溢出 179px）；
  git 还原后改用「片段文件 + 整网格单次重建」（与前几轮重排同法），乱码清零、结构完整。

**质量门**
- 23 卡锚点有效、全局时序复验通过、跳转实测到位、双宽零溢出、tools/verify.py 体检通过。

## v5.46.0 — 2026-09-18 · 自由精进：语录核实组第三批（12 → 18 条）

**主题包成果**
- quotes.html 核实组再扩容：新增 6 张引语卡——2006 秘密蓝图开篇 / 2008 圣诞夜融资 / 2016 Model 3 预订夜 /
  2016 IAC 火星宣言 / 2022「the bird is freed」/ 2022「Extremely Hardcore」。
- 引文继续从账本程序化提取（逐字一致），六卡均配专属出处标签；网格全局时序重排（2002.10.03 → 2022.11.16）。

**质量门**
- 18 卡锚点全部有效、无遗留通用标签、跳转实测到位；轮播不受影响（5 卡 5 圆点原样）；
  1280/375 双宽零溢出；tools/verify.py 体检通过。

## v5.45.0 — 2026-09-18 · 自由精进：语录核实组扩容第二批（6 → 12 条）

**主题包成果**
- quotes.html 核实组翻倍：新增 6 张引语卡——2013 Hyperloop 白皮书之问 / 2014 Dragon V2「直升机精度」 /
  2016 猎鹰火球推文 / 2017 SES-10「15 年集大成」/ 2018 猎鹰重型「looks so fake」/ 2025 Optimus「无限金钱外挂」。
- **引文从账本程序化提取**（逐字与言行实录保证一致），每卡专属出处标签（白皮书/发布会/推文/股东大会）。
- 网格重排为全局时间序（2002.10.03 → 2025.11.06），核实区现完整覆盖 23 年间六大节点。

**质量门**
- 12 卡锚点全部有效、跳转实测到位；全局时序复验通过；1280/375 双宽零溢出；链接零断链。

## v5.44.0 — 2026-09-18 · 自由精进：语录页扩容「有出处的语录」（自由精进第二十一轮）

**主题包成果**
- quotes.html 新增「有出处的语录 · 已核实」专区：6 条经本站核实并锚定账本的引语卡
  （2002 PayPal 分配 / 2008 第四次好运 / 2012 打破魔咒 / 2014 开放专利 / 2015 台阶变化 / 2018 funding secured），
  每卡含日期、逐字引文、中译与「言行实录 →」锚点链接，点击即达原文现场。
- 引语全部来自事实包既有核实记录（EXPANSION.md 各轮），本轮零新增核实需求。
- 版式区分：上方广为征引格言组保持「无出处诚实注脚」原样；下方核实组以日期+出处+锚点呈现，两级互不混淆。

**工程与质量门**
- qs-* 样式入 style.css（双列网格/打印防拆/窄屏单列）；轮播不受影响（新区域在轮播容器之外）；
  卡片点击跳转实测到位；1280/375 双宽零溢出；链接零断链。

## v5.43.0 — 2026-09-18 · 自由精进：补录 2014 Dragon V2 发布条目（自由精进第二十轮）

**主题包成果**
- 言行实录 44 → 45 条：新增 **2014.05.29 Dragon V2 载人飞船发布**（id e2014-05-29），四段深读版，
  插入 e2013-08-12 与 e2014-06-12 之间的正确时序位（脚本校验全局递增）。
- 引文核实（WebSearch）：「直升机精度」句 + 「飞船就应该能做到」对句（Universe Today 完整记录，
  NBC/New Scientist/SCMP 多源同引）。
- 后续线：推进着陆让位海上溅落、SuperDraco 转为逃逸系统——激进目标与适航现实的折中（编者分析已标注）。

**联动更新**
- search-index.js 重生成 85 条；search.html 计数文案「言行实录 45 条」；时间轴重建 45 节点；索引断言同步。

**质量门**
- tools/verify.py 一键体检全绿；node --check 通过。

## v5.42.0 — 2026-09-18 · 自由精进：部署就绪包（README + 一键体检脚本）

**主题包成果**
- 新增 **README.md**：站点简介、打开方式（双击即可/本地服务）、27 页结构表、研究功能说明
  （锚点引用格式/跨页检索/打印存档）、tools/ 工具表、内容三纪律、部署要点（含 noindex 现状说明）。
- 新增 **tools/verify.py 一键体检脚本**：断链（文件+跨页锚点，自动跳过 JS 模板串）/重复 id/
  版本一致性/检索索引与页面锚点数一致性，四项检查汇总输出，✗ 退出码 1（部署前必跑）。
- 本轮为部署准备材料，**未执行任何部署**（遵守禁令）。

**质量门**
- verify.py 实跑全绿：27 页零断链、无重复 id、版本一致 5.41.0、索引 84 条 = 44+9+18+13。

## v5.41.0 — 2026-09-18 · 新四阶段 Phase4：全站 QA 收官（四阶段计划完成）

**全维度审计结果**
- 静态：25+ HTML 递归链接/资源引用零断链（唯一标记为检索页 JS 模板字符串已知误报）；全站无重复 id；
  页内与跨页锚点（e/d/i/p 系列）全部有效；VERSION/app.js/12 个页面版本 span 三处一致。
- 浏览器：27 页 × 375/1280 双宽零溢出；首页双语切换中→英→中回归通过；检索三重组合
  （SpaceX 过滤 + "rocket" 关键词 + 倒序）→ 7 条且排序正确。
- 打印抽检（headless Edge + pypdf）：pricing/supplychain/primary 三页无空白页、无返回链接与交互
  提示泄漏、关键内容齐全。

**就地修复**
- primary.html 时间轴标题「悬停看摘要，点击跳到该条」在打印稿中泄漏——它生成在 ps-timeline-wrap
  外部，打印隐藏规则只盖住了 wrap。修复：标题加 pt-heading 类（页面/生成器/样式三处同步），
  打印隐藏；重建幂等性验证通过，重新出 PDF 复核无泄漏。

**定版**
- v5.41.0 为四阶段计划收官版本：文档馆 9 份、主题页 2 个、检索（关键词+类型+年份+公司+排序）、
  时间轴可视化、账本 44 条，全站锚点 84 个。

## v5.40.0 — 2026-09-18 · 新四阶段 Phase3-2：账本时间轴可视化 + 公司过滤（第三阶段收官）

**主题包成果**
- **账本时间轴**：primary.html 账本前新增可交互时间轴——44 个节点按日期线性定位、7 个年份刻度，
  hover/键盘聚焦显示「日期 + 出处」摘要，点击直达对应条目锚点（实测精确落位 132px）。
  纯 CSS 定位实现，零图表库；生成器 tools/build-ledger-timeline.py 幂等重建（账本变动后重跑即可）。
  窄屏容器内横滑（不破 375px 零溢出审计），打印自动隐藏。
- **检索页公司过滤**：索引构建器新增实体推断（Zip2/PayPal/SolarCity/Tesla/SpaceX/X·Twitter/xAI/
  Boring/Neuralink 九类，匹配文本含背景段 bg 字段）；检索页动态生成公司药丸（按命中数排序）+
  显式「全部」重置。实测 xAI → 精确 5 条、全部重置 → 84/84。
- 检索匹配文本扩展背景段（bg），关键词召回面随之变宽（如 "spacex" 命中从 2 → 4 条）。

**质量门**
- 时间轴 44 节点跳转几何验证；公司过滤组合实测；1280/375 双宽零溢出；node --check 通过。

**修复**
- 公司过滤组初版缺显式「全部」重置药丸（仅靠二次点击同一药丸取消），已补齐。

## v5.39.0 — 2026-09-18 · 新四阶段 Phase3-1：检索页升级（年份区间 + 排序）

**主题包成果**
- search.html 新增过滤控件行：**年份区间双下拉**（2002–2026，自动从索引收集）+ **排序切换**（时间正序/倒序），
  与既有类型筛选、关键词检索全部可组合。
- 实测：区间 2002–2008 → 命中 7 条（PayPal 创世至圣诞夜融资，日期全部带内）；倒序 → 首条 2026.01；
  "spacex" + 倒序组合 → 4 条首条 2020.05.30；复位 → 正序 84/84。
- 公司主体过滤（需索引 schema 增加 entity 字段）本轮缩小范围暂缓，留待下轮与时间轴可视化一并处理。

**质量门**
- 功能组合实测全通过；1280/375 双宽零溢出；打印隐藏 filters 行；node --check 通过。

## v5.38.0 — 2026-09-18 · 新四阶段 Phase2-2：新页「供应链与工厂哲学」（第二阶段收官）

**主题包成果**
- 新页 **supplychain.html**：四节结构——①机器造机器（Giga Shanghai 当年动工当年交付）②过度自动化之错
  （2018-04-13 推文逐字 + permalink，三短句「认错-揽责-立原则」）③零件合并哲学（70 件→1 件一体压铸省 300 机器人、
  4680 5x/6x/56% 路线图）④垂直整合的深度与边界（IDRA/外购电芯与「整合判据」）。
- 数据核实：Guardian/CNBC/TechCrunch（推文）、Electrek/Forbes（4680）、Electrek/Teslarati（压铸）。
- 工程规范：与 pricing.html 同款 sc-* 样式、10 节点 pill 导航（含自身 aria-current）、编者分析显式标注、
  @media print 打印保护、index.html 章节卡加「供应链」入口。

**质量门**
- CSSOM 验证打印规则就位；1280/375 双宽零溢出；检索 "excessive automation" 命中访谈页同源条目（覆盖一致）；node --check 通过。

## v5.37.0 — 2026-09-18 · 新四阶段 Phase2-1：新页「定价与需求管理」（自由主题页第一页）

**主题包成果**
- 新页 **pricing.html**：以 2023 年 1 月降价潮为样本拆「订单-交付-价格」三角。四节结构：
  ①01.13 降价数据行（Model Y -20% / Model 3 -6% / 抵免资格套利）②01.25 电话会议逐字自述
  （"strongest orders… almost twice the rate of production"，含 1.8 倍修正细节）③三角循环机制 ④使用边界。
- 数据核实：InsideEVs/Reuters/Fortune（降价数字）+ Motley Fool transcript/CNBC/Fox Business（引语多源）。
- 工程规范：复用 style.css + 自页样式（pr-*）、9 节点 pill 导航（含检索与自身，aria-current）、
  编者分析显式标注、@media print 打印保护、index.html 章节卡加「定价」入口。

**质量门**
- CSSOM 验证打印规则就位；1280/375 双宽零溢出；9 节点导航 aria-current 正确；链接零断链；node --check 通过。

## v5.36.0 — 2026-09-18 · 新四阶段 Phase1-3：文档馆入册 xAI Series E 公告（第一阶段收官）

**主题包成果**
- 一手文档 8 → 9 份（**第一阶段 9 份目标达成**）：新增 **2026.01 xAI「Series E」官方公告**（id d2026-01），
  官方原文三段逐字引文入册（$20B/$230B post-money/Valor 领投/NVIDIA·思科参投/秋季 $10B 股权+$12B 债务）。
- 引文核实：x.ai/news/series-e 官方原文（web_reader 两次读取一致）+ CNBC、WSJ 交叉印证；估值口径以官方
  post-money $230B 为准（与既有「约 2300 亿量级」报道一致）。
- **顺手修复存量乱序**：d2023-07-12（xAI 章程）原排在 d2023-04-05（Part 3）之前——4 月应先于 7 月；
  两块交换，导语路线中英文同步修正，9 份时序校验全递增。

**联动更新**
- search-index.js 重生成 84 条；search.html 计数文案「一手文档 9 份」；索引断言同步。

**质量门**
- 双宽零溢出；链接零断链；node --check 通过。

## v5.35.0 — 2026-09-18 · 新四阶段 Phase1-2：文档馆入册收购协议条款摘录

**主题包成果**
- 一手文档 7 → 8 份：新增 **2022.04.25《Agreement and Plan of Merger》关键条款摘录**（id d2022-04-25），
  落位 d2018-08-07 与 d2022-11-16 之间的正确时序位。
- 来源：SEC EDGAR Exhibit 2.1（Twitter, Inc. 8-K，accession 0001193125-22-120461），web_reader 两次独立读取一致；
  四条款逐字摘录：2.1(a) 54.20 美元现金转换 / 7.1(c) 终止日 2022-10-24 / 8.3 十亿美元终止费 / 9.9 特定履约。
- 本站注释串起完整法律链：价格写入推文→写进协议→9.9 条成为强制交割武器→交割与更名 X。

**联动更新**
- search-index.js 重生成 83 条；search.html 计数文案「一手文档 8 份」；导语「七→八份」中英同步；索引断言同步。

**质量门**
- 检索 "54.20" 精确命中新档；8 id 唯一；双宽零溢出；链接零断链；node --check 通过。

## v5.34.0 — 2026-09-18 · 新四阶段 Phase1-1：文档馆入册「Taking Tesla Private」全文

**主题包成果**
- 一手文档 6 → 7 份：新增 **2018.08.07「Taking Tesla Private」致员工私有化方案信**（id d2018-08-07），
  落位 d2016-07-20 与 d2022-11-16 之间的正确时序位。
- 全文核实：Wayback Machine 2018-09-18 存档（web_reader 成功绕过 webfetch 的 archive.org 超时），
  页面导语证实 8/7 博客文与员工信为同一文本；8/8"Hi All"公开信为另一文本，注脚说明未收录。
- 入册三段逐字引文：财报周期之苦 / $420 与 20% 溢价 / 持股 20% 非为控制权；注脚含与 e2018-08-07 条目互链。
- documents.html 导语同步「六→七份」，演化路线加入 2018 私有化尝试（中英双语文案同步）。

**联动更新**
- search-index.js 重生成 82 条；search.html 计数文案「一手文档 7 份」；索引断言同步。

**质量门**
- 检索 "quarterly earnings cycle" 精确命中新档；7 id 唯一；双宽零溢出；链接零断链；node --check 通过。

## v5.33.0 — 2026-09-18 · 自由精进：语录轮播键盘无障碍（自由精进第十八轮）

**主题包成果**
- quotes.html 语录轮播（5 张卡）补齐键盘操作：容器改为可聚焦区域（tabindex=0 + role=region +
  aria-roledescription=轮播 + aria-label 提示「左右方向键切换」），全局 ：focus-visible 焦点环自动生效。
- app.js：ArrowLeft/ArrowRight 循环切换、Home/End 跳首尾；聚焦即暂停自动播放、失焦恢复
  （与既有悬停暂停同路径）；reduced-motion 用户切换为瞬时定位（复用既有 reduceMotion 逻辑）。

**质量门**
- 状态机同步验证全通过：0→(→)1→(→)2→(←)1→(Home)0→(End)4，含回绕语义；
  滚动走与已验证的点按/自动播放同一路径（auto 行为实测精确落位 868px snap 点）。
- 方法注：平滑滚动动画会让「按键后立即测量 scrollLeft」拿到中途值——状态类切换是同步可靠的验证面。
- node --check 通过；双宽零溢出。

## v5.32.0 — 2026-09-18 · 自由精进：补录 2017 SES-10 首次复飞条目（自由精进第十七轮）

**主题包成果**
- 言行实录 43 → 44 条：新增 **2017.03.30 SES-10 首次整级复飞**（id e2017-03-30），四段深读版，
  插入 e2016-11 与 e2017-07-28 之间的正确时序位（脚本校验全局递增）。
- 引文核实（WebSearch）：「15 年工作的集大成」发布会句（Universe Today 逐字记录 + SpaceNews 任务报道）。
- 叙事闭环：与 e2015-12-21 组成「工程证明 → 商业证明」两联画；客户 SES 同席发布会的信任结构入册
  （编者分析已标注）。

**联动更新**
- search-index.js 重生成 81 条；search.html 计数文案同步「言行实录 44 条」；索引断言同步。

**质量门**
- 双宽零溢出；链接零断链；node --check 通过。

## v5.31.0 — 2026-09-17 · 自由精进：补录 2002 PayPal 交割条目——账本创世（自由精进第十六轮）

**主题包成果**
- 言行实录 42 → 43 条：新增 **2002.10.03 PayPal 交割与资金分配**（id e2002-10-03），账本现最早条目，
  「1 亿 SpaceX / 7000 万 Tesla / 1000 万 SolarCity / 借钱付房租」自述入册。
- 引文核实（WebSearch）：2012 访谈原句（The Transcript 存档）+ USA Today 2013 访谈 + Jorgenson《Book of Elon》
  变体印证；措辞差异已按纪律记录 EXPANSION.md。
- 商业逻辑闭环：money.html「退出即入场 / 个人资本买信用」两大模式自此有了第一手锚点。

**联动更新**
- search-index.js 重生成 80 条；search.html 计数文案同步「言行实录 43 条」；索引断言同步。

**质量门**
- 双宽零溢出；链接零断链；node --check 通过。

## v5.30.0 — 2026-09-17 · 自由精进：补录 2016 Amos-6 爆燃条目（自由精进第十五轮）

**主题包成果**
- 言行实录 41 → 42 条：新增 **2016.09.01 Amos-6 爆燃**（id e2016-09-01），四段深读版，
  插入 e2016-07-20 与 e2016-09-27 之间的正确时序位（脚本校验全局递增）。
- 引文核实（WebSearch）：2016.09.09 本人推文「Falcon fireball / 14 年来最困难最复杂的失败」
  （Spaceflight Now、CBS、Phys.org、SpacePolicyOnline 四源逐字印证）；调查结论（COPV 固氧）引 SpaceNews。
- 商业逻辑：事故透明度本身成为信用资产——公开失败、承认最难、当众修好（编者分析已标注）。

**联动更新**
- search-index.js 重生成 79 条；search.html 计数文案同步「言行实录 42 条」；索引断言同步。

**质量门**
- 双宽零溢出；链接零断链；node --check 通过。

## v5.29.0 — 2026-09-17 · 自由精进：补录 2018 猎鹰重型首飞条目（自由精进第十四轮）

**主题包成果**
- 言行实录 40 → 41 条：新增 **2018.02.06 猎鹰重型首飞**（id e2018-02-06），四段深读版，
  插入 e2018-01-28 与 e2018-08-07 之间的正确时序位（脚本校验全局递增）。
- 引文核实（WebSearch）：「looks so fake」句以 Space.com 完整版入册，AP 通稿多 outlet 印证；
  「普通车。在太空里。」同发布会补充原话一并核实。2022 创立故事（俄罗斯买火箭/吐鞋）因原话仅存于
  传记转述、无本人逐字权威出处，按「查不到不写」纪律暂不入册。
- 商业逻辑：载荷决策式营销——花掉一辆车让重型运载显得势在必行（编者分析已标注）。

**联动更新**
- search-index.js 重生成 78 条；search.html 计数文案同步「言行实录 41 条」；索引断言同步。

**质量门**
- 双宽零溢出；链接零断链；node --check 通过。

## v5.28.0 — 2026-09-17 · 自由精进：补录 2012 Model S 首批交付条目（自由精进第十三轮）

**主题包成果**
- 言行实录 39 → 40 条：新增 **2012.06.22 Model S 首批交付**（id e2012-06-22），四段深读版，
  落位 e2008-12-24 与 e2013 之间（首次插入位置错误在 e2013 之后，已移动修正并复验全局递增）。
- 引文核实（WebSearch）：「breaking a spell / 打破魔咒」句（Forbes 现场报道 + AP + CleanTechnica + BBC 多源，
  措辞差异已在 EXPANSION 说明）；Tesla IR 新闻稿锁定日期与 Jurvetson 细节。
- 商业逻辑：拒绝在对手维度上被比较、改变维度本身（编者分析已标注）。

**联动更新**
- search-index.js 重生成 77 条；search.html 计数文案同步「言行实录 40 条」；索引断言同步。

**质量门**
- 双宽零溢出；链接零断链；node --check 通过。

## v5.27.0 — 2026-09-17 · 自由精进：补录 2015 猎鹰一级首陆条目（自由精进第十二轮）

**主题包成果**
- 言行实录 38 → 39 条：新增 **2015.12.21 猎鹰九号一级首次陆上回收**（id e2015-12-21），四段深读版，
  插入 e2015-04-30 与 e2016 之间的正确时序位（脚本校验全局递增）。
- 引文核实（WebSearch）：电信会议「fundamental step change」句（transcript 存档 + NPR + ABC 三方）；
  现场段含「Welcome back, baby!」推文与贝索斯「Welcome to the club!」互怼（原帖链接在案）。
- 商业逻辑：复用经济学改写发射成本曲线，为星链奠基（编者分析已标注）。

**联动更新**
- search-index.js 重生成 76 条；search.html 计数文案同步「言行实录 39 条」；索引断言同步。

**质量门**
- 双宽零溢出；链接零断链；node --check 通过。

## v5.26.0 — 2026-09-17 · 自由精进：补录 2008 圣诞夜 Tesla 融资条目（自由精进第十一轮）

**主题包成果**
- 言行实录 37 → 38 条：新增 **2008.12.24 圣诞夜融资关闭**（id e2008-12-24），四段深读版，
  插入 e2008-09-28 与 e2013 之间的正确时序位（脚本校验全局递增）。
- 引文核实（WebSearch）：“We actually closed the financing round on Christmas Eve 2008.
  It was the last hour of the last day that it was possible.”（Business Insider 2015-12 巴黎演讲报道；
  本人 X 自述复述经 Hindustan Times 报道）。与 12.23 NASA 合同构成「背靠背的两天」叙事。
- 编者分析（已标注）：投进最后的钱这个行为本身成为融资定价的抵押品。

**联动更新**
- search-index.js 重生成 75 条；search.html 计数文案同步「言行实录 38 条」；索引断言同步。

**质量门**
- 双宽零溢出；链接零断链；node --check 通过。

## v5.25.0 — 2026-09-17 · 自由精进：补录 2013 Hyperloop 白皮书条目（自由精进第十轮）

**主题包成果**
- 言行实录 36 → 37 条：新增 **2013.08.12《Hyperloop Alpha》白皮书**（id e2013-08-12），四段深读版，
  插入 e2013 与 e2014-06-12 之间的正确时序位（脚本校验全局递增）。
- 引文核实（WebSearch，LA Times/WaPo/American Interest 三方印证）：「硅谷和 JPL 的老家怎么会修一条每英里最贵、
  速度又最慢的高铁之一？」原句入册。
- 商业逻辑对照：与上轮 2014 开放专利同构——都是「把护城河换成平台位」；本轮是反向操作的开端
  （没时间做就开源规格书），编者分析已显式标注。

**联动更新**
- search-index.js 重生成 74 条；search.html 计数文案同步「言行实录 37 条」；索引断言同步。

**质量门**
- 双宽零溢出；链接零断链；node --check 通过。

## v5.24.0 — 2026-09-17 · 自由精进：补录 2014 开放专利条目（自由精进第九轮 · 回到内容主线）

**主题包成果**
- 言行实录 35 → 36 条：新增 **2014.06.12「All Our Patent Are Belong To You」开放专利**（id e2014-06-12），
  四段深读版（背景/原话/现场/后续），插入 e2013 与 e2015-04-30 之间的正确时序位（脚本校验全局递增）。
- 引文核实（WebSearch）：“Tesla will not initiate patent lawsuits against anyone who, in good faith,
  wants to use our technology.” + 开场「帕洛阿尔托总部大厅的专利墙」句。
  来源：Tesla 官方博客原文存档（teslamagazine.org/2014/06/）、NBC News、Hacker News 当日帖。
- 「后续」段的 NACS 开放对照为编者分析并已显式标注，与原话严格区分。

**联动更新**
- search-index.js 重生成：73 条；search.html 计数文案同步「言行实录 36 条」；检索 "patent" 精确命中新条目。
- tools/build-search-index.py 数量断言同步 36。

**质量门**
- 双宽零溢出；data-en 双语叶子齐备；链接零断链；node --check 通过。

## v5.23.0 — 2026-09-17 · 自由精进：跨页第一手检索上线 + 账本时间序修复（自由精进第八轮）

**主题包成果**
- 新页 search.html「第一手检索」：一个搜索框覆盖全部 72 条第一手条目（实时过滤 + 类型筛选 + 命中高亮），
  每条结果直链来源页可引用锚点（实测 "funding secured" 首条即 $420 推文锚点）。
- 新工具 tools/build-search-index.py：从四个第一手页自动提取 72 条生成 search-index.js
  （JS 全局变量而非 JSON fetch——file:// 下 fetch 被 CORS 拦截；实测无服务器直开文件可用，离线约束达成）。
- 入口布线：index.html 章节卡「第一手」子链接与 primary.html 阅读路径各加「检索」。

**内容修复（建索引时暴露，准确性优先）**
- primary.html 账本 35 条时间序 6 处乱序（此前插补条目落位错误）→ 全量重排，脚本校验全局递增 + 条目集合 MD5 守恒。
- 三条日期错误修正（详见 EXPANSION.md）：Investor Day 2023.7.05→2023.03.01；股东大会 2025.12.06→2025.11.06；
  Starbase 投票 2025.12.03→2025.05.03。id 同步更新并保持全站唯一。

**质量门**
- 搜索实测：72 条全量 / "spacex" 2 条 / "funding secured" 2 条 / "火箭" 3 条 / 类型过滤正确；结果点击跳转到位。
- file:// 离线验证通过（headless Edge dump-dom 渲染出「命中 72 / 72 条」）；375/1280 双宽零溢出；链接零断链。

## v5.22.0 — 2026-09-17 · 自由精进：帖墙可引用化 + 事实修正，引用体系全量收官（自由精进第七轮）

**主题包成果**
- x-posts.html 13 张帖卡全部挂稳定 id（p2018-01-28 … p2025-05-03），深底卡上的日期成为自锚链接
  （颜色保持 #d9a7a7，悬停下划线；flex 布局 margin-left:auto 右对齐不受影响）。
- **事实修正**（WebSearch 核实后）：Grok 首发公告推文日期「2023.4.04」→「2023.11.04」。
  原日期时 Grok 尚不存在；修正后与卡片年代序位置吻合（TechCrunch 2023-11-03 报道佐证）。修正记录入 EXPANSION.md。
- **引用体系全量收官**：账本 35（e…）+ 文档 6（d…）+ 访谈 18（i…）+ 帖卡 13（p…）= 72 个第一手锚点。

**质量门**
- 13 id 唯一；跳转实测落点 20px（the bird is freed 帖卡精确落位）；日期链接计算样式与改动前一致；
  1280/375 双宽零溢出。

## v5.21.0 — 2026-09-17 · 自由精进：访谈页可引用化，第一手引用体系收官（自由精进第六轮）

**主题包成果**
- interviews.html 18 条带日期的访谈/表态条目全部挂稳定 id（i2006-08 … i2025-11-06，含 i2016-09-27 瓜达拉哈拉），
  日期徽章成为自锚链接（观感保持，悬停酒红边框）；第 19 个 iv-item 为编者块，不参与引用，未加 id。
- 至此三大第一手页全部可逐条引用：言行实录 35 条（primary.html#e…）+ 一手文档 6 份（documents.html#d…）
  + 访谈表态 18 条（interviews.html#i…），共 59 个第一手锚点。

**质量门**
- 18 id 全唯一；跳转实测落点可见（targetTop 56px 稳定，标题区完整，本页无吸顶头不影响可用性）；
  徽章计算样式与改动前一致；1280/375 双宽零溢出。
- 方法注：本轮再次踩到平滑滚动时序坑——hash 跳转后立刻测量会拿到滚动中途值（328px 假通过）；
  须在 scroll-behavior:auto 确认生效且滚动稳定后复测（56px 稳定值）。

## v5.20.0 — 2026-09-17 · 自由精进：一手文档馆可引用化 + 事实修正（自由精进第五轮）

**主题包成果**
- documents.html 六份一手文档全部挂稳定 id（d2006-08 / d2016-07-20 / d2022-11-16 / d2023-07-12 / d2023-04-05 / d2025-09-01），
  日期徽章成为自锚链接（观感保持：11px 胶囊、悬停酒红边框呼应全站 hover 语言），支持逐份引用。
- **事实修正**（WebSearch 核实后）：Part 3 日期徽章「2023.7.01 Investor Day 预告 · 2023.7.05 全文」为错误，
  修正为「2023.03.01 Investor Day 发布 · 2023.04.05 全文」（Investor Day 2023-03-01 Austin；
  全文 41 页 PDF 于 2023-04-05 发布于 tesla.com）。修正事实已记录 EXPANSION.md。

**质量门**
- 6 id 唯一；锚点跳转实测落点 20px 在视口内；徽章计算样式与改动前一致；1280/375 双宽零溢出。

## v5.19.0 — 2026-09-17 · 自由精进：账本条目稳定锚点（自由精进第四轮）

**主题包成果**
- primary.html 言行实录 35 条全部挂上稳定 id（日期派生：e2006-08 / e2008-09-28 / e2023-07-12 …，
  本轮 35 条日期天然无重复）——研究引用场景：任何一条可直接以 primary.html#e2016-03-31 形式引用。
- 每条日期徽章本身成为自锚链接（span → a，观感零变化：同字体同色同字号，悬停下划线），
  点击即定位本条；title 属性提示「定位到本条 · Permalink」。
- style.css：.ps-row scroll-margin-top 132px（桌面，吸顶报头实测 125px + 间隙）/ 170px（窄屏沿用既有约定）。

**质量门**
- 35 id 全部唯一；跳转几何实测：目标条目顶部落点 132px，恰在报头下方 6px 间隙，无遮挡。
- 搜索回归通过（spacex → 4/35，清空恢复）；1280/375 双宽零溢出；徽章计算样式与改动前一致。
- 方法注：QA 环境内嵌浏览器缓存顽固，用「服务器端 curl 确认 + 页内注入等价规则实测几何」构成证据链；
  file:// 真实使用无 HTTP 缓存，不受此影响。

## v5.18.0 — 2026-09-17 · 自由精进：真实打印管线验证 + 导航统一（自由精进第三轮）

**主题包成果**
- 建立真实打印验证管线：无头 Edge --print-to-pdf 产出 6 页代表页 PDF + pypdf 逐页文本分析
  （此前 v5.16.0 只做过 CSSOM 级验证，本轮首次在真实渲染路径上确认打印规则生效）。
- 抽检发现并修复 2 处真泄漏：
  - changelog.html 的「返回主页」链接（.cl-back 不在 v5.16.0 隐藏名单）→ 已隐藏；
  - index.html 页脚「彩蛋」操作提示（.footer-hint 不在名单）→ 全局打印隐藏名单补入。
- 顺带发现并统一：documents/interviews/x-posts/money 四页 pill 导航仍是旧 5 节点
  （v5.15.0 只更新了两个新页）→ 四页补齐为 7 节点，与 primary/两个新页一致，7 页全部 aria-current 正确。

**验证方法说明**
- 泄漏检测用「导航专属串」代理（如「资本演化」仅存在于导航），正文 legitimate 提及不算泄漏；
  英文引文检查需大小写+空白归一（The bird is freed 跨行提取）。

**质量门**
- 6+4 个 PDF 复检全绿：无空白页、返回链接/导航/彩蛋提示全部隐藏、正文关键内容齐全；
- 24 页链接终扫零断链；打印稿页数合理（money 4页 / changelog 24页 / primary 33页）。

## v5.17.0 — 2026-09-17 · 自由精进：375px 窄屏全站走查（自由精进第二轮）

**主题包成果**
- 24 页 × 375px 视口横向溢出探针：23 页零溢出，changelog.html 溢出 327px。
- 元凶定位：v3.1.0 修订条目中 `profile/timeline/companies/...` 斜杠路径长串——CSS 默认不在 `/` 处断行，
  340px 不可断 ASCII 串把 li 撑到 667px（边界框探针抓不到，scrollWidth 链路定位）。
- 修复（双层）：style.css body 全局 `overflow-wrap: break-word`（防御长 URL/路径，不影响 min-content 尺寸）；
  changelog.html `.cl-page` 加 `overflow-wrap: anywhere`（修订条目含大量文件名串，允许更积极断行）。

**质量门**
- 复测：changelog 375px 溢出归零（最宽 li 320px，容器内）；全站 24/24 页 375px 零溢出。
- 1280px 桌面端回归：24/24 零溢出，money.html 双列网格结构完好（break-word 不改 min-content，无副作用）。

## v5.16.0 — 2026-09-17 · 自由精进：打印/存档保护补全（Phase 1-3 完成后首轮）

**主题包成果**
- money.html 打印保护从零补全：my-row/my-note 防拆页、⓪ 资本时间线 SVG 图表整节不拆页、返回链接隐藏。
- deep-dive-01~05：dd-table 表格行与 dd-note 编者注防拆页、表头不与行分离、返回链接打印隐藏。
- capital-evolution / ai-strategy / x-posts / documents / interviews：返回链接统一打印隐藏（存档版无 UI 链接）。
- style.css 全局打印块新增隐藏：ps-nav 药丸导航、阅读进度条、语录轮播圆点。
- 新增 tools/sync-changelog.py：changelog.html 由 CHANGELOG.md 全量重生成的可复用工具（本轮起纳入固定流程）。

**工程修复（本轮 QA 中发现并修复）**
- 前述打印补丁的正则替换在嵌套规则处截断，money/x-posts/deep-dive 系列产生错位嵌套的坏规则
  （如 .dd-back 被嵌进 .dd-table tr 内层导致选择器永不匹配）。已用括号感知整块替换全部重写为平铺规则，
  并经 CSSOM 缓存穿透验证：选择器层级全部正确、零嵌套污染。

**质量门**
- 括号配平审计 11 页全过；CSSOM 解析验证 9 页全绿；node --check 通过；tools/sync-changelog.py 回归零差异。

## v5.15.0 — 2026-09-17 · 第二/三阶段收官：新页导航补全 + 全站 QA（Phase 2-3）

**主题包成果（Phase 2 完成 + Phase 3 QA）**
- capital-evolution.html「资本模式演化时间轴」与 ai-strategy.html「AI 战略布局全景」两新子页补全导航：
  - index.html 章节卡 10「第一手」子链接新增「资本演化」「AI 战略」两入口。
  - 两新页各加 7 节点 pill 导航（与四子页同款，aria-current 标识当前页）。
  - 两新页互链 + 底部返回主页链接。
- 修复 7 处断链：pill 导航残留的 index.html#primary 锚点（多页迁移前遗留）统一改为 primary.html。
- changelog.html 长期脱同步修复：从 CHANGELOG.md 全量重生成（v0.1.0 → v5.15.0 共 65 条）。

**质量门（Phase 3 QA 记录）**
- 静态扫描：24 个 HTML、332 个链接，页面/锚点/CSS/JS/图片引用零断链。
- 浏览器探针：首页版本显示、双语切换（中→英→中往返）、16 张章节卡、2 个新页入口全通过。
- 两新页 pill 导航渲染与 aria-current 正确；primary.html 实时检索正常（"spacex" 过滤 4/35，清空恢复 35）。
- 全部页面无损坏图片。

## v5.14.0 — 2026-09-15 · 第一阶段：补录 3 条言行条目（今夜第 24 轮）

**主题包成果（Phase 1 完成）**
- 言行实录 32 → 35 条：
  - 2016.03.31 Model 3 预订夜（约 40 万预订压顶，周产 5000 生死线开启）
  - 2016.11 SolarCity 收购（26 亿关联交易，股东诉讼持续多年）
  - 2018.12.18 Boring Company 首条隧道通车（"traffic is soul-destroying" 的解决方案初落地）
- 三条全部为此前已核实锚点，插在时间序正确位置。

**工程修复**
- primary.html 版本字符串散落在 5.05-5.12 多个版本号上，本轮全站归一。
- 修复了前几轮 `;` 链导致的片段文件误删问题（改用独立调用）。

**质量门**
- node --check 通过；无重复 id；锚点完整；全部引文为此前已核实锚点；浏览器验证渲染。


## v5.13.0 — 2026-09-15 · 全站版本归一 + 四子页导航重建（今夜第 23 轮）

**主题包成果**
- 全站版本字符串归一至 5.13.0（此前散落在 5.05-5.12 多个版本号上）。
- 四子页统一 pill 导航重建（documents/interviews/x-posts/money 各 1 个，aria-current 标识当前页）。

**质量门**
- node --check 通过；13 卡全在位；全页 HTTP 200。


## v5.3.0 — 2026-09-15 · 补齐 index 缺失卡片 + documents 阅读路径确认（今夜第 22 轮）

**主题包成果**
- index.html 补入 deep-dive-04（监管博弈）与 deep-dive-05（AI 战略布局）两张章节卡片。
- documents.html 阅读路径确认在位。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证渲染。


## v5.2.0 — 2026-09-15 · 深读长文第 4 篇：与监管的博弈（今夜第 20 轮）

**主题包成果**
- deep-dive-04.html「马斯克与监管的博弈」——四节：SEC 和解 / FAA 塔捕许可 / 德州迁册 / 逻辑链小结与适用边界。
- 全部事实为此前已核实锚点，零新增未核实内容。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证渲染。


## v5.2.0 — 2026-09-15 · 深读长文第 2 篇：用人逻辑与团队建设（今夜第 19 轮）

**主题包成果**
- deep-dive-02.html「马斯克的用人逻辑与团队建设」——五节：第一性原理招聘 / 直系团队 / 公司城模式 / 过度自动化纠错 / 逻辑链小结。
- index.html 章节目录新增深读第 2 篇卡片。
- 全站版本号同步 5.2.0。

**质量门**
- node --check 通过；无重复 id；锚点完整；全部事实可溯源事实扩展包；浏览器验证渲染。


## v5.1.0 — 2026-09-15 · 深读长文第 1 篇：资本运作全解（今夜第 18 轮）

**主题包成果**
- 新页面 deep-dive-01.html：「马斯克的资本运作全解」——退出、融资、收购、估值四节，含融资节点数据表格（五类资金来源顺序）、编者注虚线框、适用边界。
- index.html 章节目录新增深读卡，primary.html 交叉引用链接。

**质量门**
- node --check 通过；无重复 id；锚点完整；全部数字可溯源事实扩展包；浏览器验证渲染。


## v4.2.0 — 2026-09-15 · money.html 资本时间线 SVG 图表（今夜第 17 轮 · 自由精进）

**主题包成果**
- money.html 新增「⓪ 资本时间线」SVG 图表：七笔关键交易（Zip2 $307M → PayPal $1.5B → Tesla A 轮 → NASA $1.6B → SolarCity → Twitter $44B → xAI E 轮）沿时间轴可视化，含虚线弧线暗示连续性。

**质量门**
- node --check 通过；SVG 图表数字全部可溯源事实扩展包；浏览器验证渲染。


## v4.9.0 — 2026-09-15 · 访谈页补 IAC 2016 演讲条目（今夜第 17 轮）

**主题包成果**
- interviews.html 17 → 18 条：补入 2016.09.27 IAC 瓜达拉哈拉演讲条目（「Making Humans a Multi-Planetary Species」——ITS 架构首发与后续演化），与主页账本的 IAC 深读条目同步，引文全部为此前已核实锚点。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证渲染。


## v4.8.0 — 2026-09-15 · 实录扩容：IAC 2016 火星演讲（今夜第 16 轮）

**主题包成果**
- 言行实录 31 → 32 条：新增 2016.09.27 IAC 瓜达拉哈拉演讲深读条目——《Making Humans a Multi-Planetary Species》标题逐字核实（Ingenium/EarthSky/New Space 期刊），ITS 架构首发、现场反应与后续演化（2017 论文 → 2024 塔捕的直系谱系）入注。
- 插入位置按时间序校准（蓝图二之后、造机器的机器之前），全站版本同步 4.8.0。

**质量门**
- node --check 通过；无重复 id；锚点完整（Ingenium/EarthSky/New Space 期刊）；浏览器验证渲染。


## v4.7.0 — 2026-09-15 · 子页统一导航（今夜第 15 轮 · 自由精进）

**主题包成果**
- documents / interviews / x-posts / money 四个子页补统一 pill 导航（言行实录/文档馆/访谈/帖史/资本解剖），aria-current 标识当前页——五页板块间跳转不再绕行主页。

**质量门**
- node --check 通过；无重复 id；四页渲染验证。


## v4.6.0 — 2026-09-15 · 帖墙小结：编者提炼（今夜第 14 轮 · 自由精进）

**主题包成果**
- x-posts.html 帖尾新增「帖墙小结 · 编者提炼」：把发帖节奏作为研究对象——2018 承诺之年、2022 平台之年、2024-2025 基础设施公告期，与主页「言行实录」的三卷读法互为对照。

**质量门**
- node --check 通过；全部页面版本同步 4.6.0；浏览器验证渲染。


## v4.5.0 — 2026-09-15 · 帖墙按年份分组重排（今夜第 13 轮 · 自由精进）

**主题包成果**
- x-posts.html 帖墙按年份分组：7 个年份分隔条（2018/2019/2021/2022/2023/2024/2025），卡片按时间升序重排，读起来像一部编年史。
- 修复历史遗留的网格未闭合问题（xp-grid 缺失闭合 div），页面结构恢复合法。

**自主优化**
- 新增 .xp-year 年份分隔条样式（酒红衬线 + 底边线），与全站设计令牌一致。
- 打印支持补齐：帖卡与年份条防跨页。

**质量门**
- node --check 通过；13 张卡全部在位且时间升序；无横向溢出；pill 导航在位；浏览器验证渲染。


## v4.4.0 — 2026-09-15 · 帖墙补 Twitter Files 预告帖（今夜第 12 轮）

**主题包成果**
- x-posts.html 补 2022.11.28 预告帖卡（广泛征引措辞 + 诚实标注：逐字未经原帖复核）——与主页「言行实录」深读版互为对照。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证渲染。


## v4.3.0 — 2026-09-15 · 帖墙与访谈页同步扩容（今夜第 11 轮）

**主题包成果**
- x-posts.html 13 → 14 张：补 2018.01.28 火焰喷射器丧尸推文（原帖编号核实，The Guardian 报道）。
- interviews.html 16 → 17 条：补 2019.11.22「大锤砸门」技术解释表态条（BBC 引 X 帖原文），工程师式不找借口的话术样本。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证渲染。


## v4.2.0 — 2026-09-15 · 帖墙扩容：+2 张已核实名帖（今夜第 10 轮）

**主题包成果**
- x-posts.html 11 → 13 张：
  - 2021.03.02 Starbase 并入预言帖（与 2025 建市帖构成四年呼应）；
  - 2024.01.29 Neuralink 首例植入官宣帖（原帖编号核实）。
- 页脚互链补「资本解剖」入口。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证渲染。


## v4.1.0 — 2026-09-15 · 新资本事件同步三页（今夜第 9 轮）

**主题包成果**
- money.html 资本解剖补两行：薪酬二次表决（2024.06.13，重新批准 2018 方案 + 迁册德州）与 Starbase 建市（2025.05.03，约 283 选民压倒性通过、5.20 认证）。
- interviews.html 补「STARBASE IS AWESOME AND ANYONE CAN VISIT」表态条（Texas Tribune/13News 来源徽章）。
- x-posts.html 补同款帖卡。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证渲染。


## v4.0.0 — 2026-09-15 · 实录破 30 条里程碑：新增一手深读条目×2（今夜第 8 轮）

**主题包成果**
- 言行实录 29 → 31 条：
  - 2024.06.13 股东年会——「hot d***! I love you guys」开场 + 25 万亿美元 Optimus 表态（CNBC/Teslarati 全文转录核实）；
  - 2025.05.03 Starbase 建市投票——约 283 选民/压倒性通过/5.20 认证（Texas Tribune/TPR/PBS 核实），「STARBASE IS AWESOME AND ANYONE CAN VISIT」。
- 版本跳 **v4.0.0**：言行实录突破 30 条，里程碑达成。

**质量门**
- node --check 通过；无重复 id；锚点完整（CNBC/Teslarati/Texas Tribune/TPR/PBS 逐条核实）；浏览器验证渲染。


## v3.9.0 — 2026-09-15 · 实录扩容：Cybertruck 交付日（今夜第 7 轮）

**主题包成果**
- 新增 2023.11.30 Cybertruck 首批交付深读条目：跳票四年 → 交付日登台（乘车斗）→ 逐字引语「Finally, the future will look like the future」「experts said was impossible」→ 逻辑链收尾：2019 破玻璃与 2023 慢交付是同一模式（最大音量宣布、付出信用代价、照样交付）。
- 引语锚点：CNBC/Fortune/Business Insider 记录，逐字核实。

**质量门**
- node --check 通过；无重复 id；锚点完整；全站版本同步 3.9.0。


## v3.7.1 — 2026-09-15 · 热修：章节页 app.js 双重执行（严重）+ 导航残留切除补记

**问题**：v3.1.0 章节化转换时，页脚正则把 `<script src="app.js">` 一并捕获、模板又追加了一次——全部 12 个转换页面 app.js 执行两遍。后果：双语切换双监听互相抵消（切换失效）、轮播双计时器互相打架（圆点翻倍 10 个、引语快速闪跳）。

**修复**
- 12 个页面逐一去重（保留 DOM 末尾那一个）。
- 双语切换、轮播、圆点全部复测通过。

**经验入册**
- 探针发现「圆点 10 个」这一异常数字是破案关键；今后凡计数异常即视为双重初始化信号。
- 后续巡检又发现四个子页残留一枚格式损坏的旧导航（同一失败轮次的半成品写入），已全部切除并以干净导航重建。

## v3.8.0 — 2026-09-15 · 交叉污染修复 + primary 阅读路径（今夜第 6 轮）

**主题包成果**
- 修复 quotes.html 交叉污染：v3.1.0 章节拆分时语录板块闭合锚定失误，导致整个「第一手」板块（362 行）被吞并进语录页——外科切除后语录页回到 103 行纯语录（五条引语 + 轮播 + 注脚完好）。
- primary.html 补「使用路径 · 编者导读」（账本 → 文档馆 → 访谈 → 方法 → 检索的研究顺序）。

**工程复盘**
- 连续多轮「点击无效」的假象，实为两条因素叠加：①Playwright fill("") 在该后端不派发 input 事件；②7 秒自动轮播与探针读取的时序竞争。改用原生事件派发 + window.onerror 挂钩后确认处理器完全正常。

**质量门**
- node --check 通过；quotes.html 103 行 / 0 条 ps-row 残留 / 5 圆点 5 引语；primary 阅读路径在位；双档渲染正常。


## v3.7.0 — 2026-09-15 · 自由精进：语录补第 5 条 + 子页直达（今夜第 7 轮）

**主题包成果**
- 语录区补第 5 条：「I would like to die on Mars. Just not on impact.」（已核实原句）——自动轮播与圆点同步。
- index 第一手章节卡加五个子页直达链接（账本/文档馆/访谈/帖史/资本解剖），提升多页板块可发现性。

**质量门**
- node --check 通过；无重复 id；浏览器验证渲染。


## v3.6.0 — 2026-09-15 · money.html 续建 + 三子页阅读路径（今夜第 6 轮）

**主题包成果**
- money.html 新增「⑥ 小结：马斯克资本运作的四个模式」（退出即入场 / 个人资本买信用 / 收购买时间 / 激励即契约），每条注明对应的第一手材料位置；页脚互链访谈与文档馆。
- documents.html 与 interviews.html 各加「阅读路径 · 编者导读」：前者按时间读成二十年战略演化史，后者按时间听语气演化。

**质量门**
- node --check 通过；无重复 id；锚点完整；money.html 渲染验证（HTTP 200）。


## v3.5.0 — 2026-09-15 · money.html 资本解剖页（今夜第 5 轮）

**主题包成果**
- 新独立页 money.html「资本解剖」五节：①两次退出换门票（Zip2 3.07 亿 / PayPal 15 亿）②外部资本四节点（A 轮 750 万 / IPO 2.26 亿 / NASA 16 亿 / Series E 200 亿）③收购买关键环节（SolarCity 26 亿 / Twitter 440 亿）④市值与薪酬互锁（第一车企 / 1 万亿 / 8.5 万亿目标 / 75% 支持）⑤财富里程碑（5000 亿 / 8920 亿）。
- 每节「编者注」明确标注为本站分析：资本来源四类的顺序观察、收购逻辑、激励契约观察、里程碑优于快照的方法论提示。
- 「第一手」升级为五页板块，primary pill 导航与三个子页页脚互链接入。

**质量门**
- node --check 通过；无重复 id；全部数字可溯源事实扩展包；money.html 渲染验证（HTTP 200）。


## v3.3.0 — 2026-09-15 · 实录扩容：Battery Day 与 We, Robot（今夜第 3 轮）

**主题包成果**
- 言行实录 26 → 28 条（primary.html）：
  - 2020.09.22 Battery Day——4680 无极耳电池与 2.5 万美元车型承诺；次日股价下跌的「不公平但真实」反应；
  - 2024.10.10「We, Robot」Cybercab——「专为无监督全自动驾驶而造」的原话；与 2020 年电池承诺构成「同一赌注换载具」逻辑链（2024.02 搁置 → Robotaxi 优先，The Information 报道）。

**工程修复**
- 发现并修复 primary.html 版本号在 v3.2.0 轮被漏改的问题（3.1.0 → 3.3.0），版本三处同步机制复查通过。

**质量门**
- node --check 通过；无重复 id；锚点完整（Rev.com 转录/What's Up Tesla/The Information）；浏览器验证渲染。


## v3.2.0 — 2026-09-15 · 书卷化编排第一批（今夜第 2 轮）

**主题包成果（中心线三落地）**
- timeline.html：「阅读路径 · 编者导读」（三卷读法：起步与豪赌 2006-2008 / 规模化 2010-2018 / 平台与 AI 2022-2026）+「本章小结 · 编者提炼」（三个行为模式研究要点）。
- stories.html / persona.html：各加「本章小结」（四场危机一个模式；六项特质互相咬合）+ 交叉引用指向「言行实录」与「经典商战」。
- 编者提炼与原话在排版上严格区分（虚线框 + 「编者提炼」标注）。子页无版本显示，无需同步。

**质量门**
- node --check 通过；三页无重复 id；浏览器验证渲染。


## v3.1.0 — 2026-09-15 · 章节化改版：单页站 → 多页篇章架构（今夜第 1 轮）

**主题包成果（用户指定方向）**
- index.html 重构为「封面 + 章节目录」：封面保留卷首特稿/肖像/关键数字，新增 11 张章节卡片（编号 + 双语标题 + 一句话导读 + 阅读入口）。
- 11 个板块独立成页（profile/timeline/companies/indepth/stories/persona/playbook/numbers/grok/quotes/primary.html），共享报头/页脚/双语切换/设计令牌；每章底部「上一章 · 下一章」翻页。
- 四个子页（文档馆/访谈/帖史/修订记录）保持独立并接入互链网络。
- 工程修复：scrollspy 适配文件型导航链接（非 # 锚点不再参与页内高亮，避免 querySelector 异常）。

**质量门**
- node --check 通过；各页无重复 id；锚点与本地资源完整；浏览器验证 index 与章节页在 1440px 与 375px 的渲染。
- 验证方式说明：本轮浏览器截图组件间歇故障，视觉确认以 DOM 探针为主（11 张章节卡/卡片跳转/翻页导航/双语切换/版本号/21 条时间线全部探针通过），下轮补截图走查。


## v3.0.0 — 2026-09-13 · 自由精进：检索清空按钮 + 子页打印（今夜第 18 次唤醒）

**主题包成果**
- 检索框新增「清空」按钮：一键清空并回焦输入框（补足部分浏览器 type=search 无原生 ✕ 的场景）。
- 子页打印支持：文档卡/访谈条/帖卡 break-inside 防跨页；帖卡打印转白底黑框。

**质量门**
- node --check 通过；无重复 id；浏览器验证 1440px 渲染与清空交互。


## v2.9.0 — 2026-09-13 · 自由精进：实录实时检索（今夜第 17 次唤醒）

**主题包成果**
- 言行实录新增实时检索框：输入关键字（如「火星」「420」「塔」「SolarCity」）即时筛选 24 条深读条目，中英文本均可命中；显示「可见条数 / 总数」计数。
- 原生 JS、键盘可用（type=search + focus 焦点环）、reduced-motion 无影响。

**质量门**
- node --check 通过；无重复 id；浏览器验证 1440px 与 375px 的筛选交互。


## v2.8.0 — 2026-09-13 · 全站终版 QA · 收官轮（自动化今夜第 16 轮）

**终版走查（全部通过）**
- 五个页面（index/documents/interviews/x-posts/changelog）重复 id 全检：零重复。
- 本地资源：三张照片 + 两文件引用完整；五页 HTTP 200。
- 双语完整性：data-en 达 551 处；node --check 通过。
- 今夜扩张收官统计：言行实录 13 → 24 条（全部四段深读版）、一手文档馆 6 份、访谈表态 16 条、帖墙 11 张、四页统一导航与互链闭环。

**致谢**
- 全部引文锚点经 WebSearch 逐条核实并记录于 EXPANSION.md 事实扩展包；两轮因核实服务不可用而按纪律转为结构精进，未杜撰任何内容。


## v2.7.0 — 2026-09-13 · 访谈页与帖墙同步扩容（自动化今夜第 15 轮）

**主题包成果**
- interviews.html 14 → 16 条：补入 2013「死在火星」之答与 2015 Powerwall 发布会「they suck」逐字引语（TechCrunch/ABC 已核实）。
- x-posts.html 9 → 10 张：Twitter Files 预告帖卡，广泛征引措辞带诚实徽章。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证 interviews.html 与 x-posts.html 在 1440px 与 375px 的渲染。


## v2.6.0 — 2026-09-13 · 访谈页补入两条已核实表态（自动化今夜第 14 轮）

**主题包成果**
- interviews.html 12 → 14 条：2016「造机器的机器」（含 Grohmann 收购与 2018「人类被低估」纠错互链）、2021 SolarCity 庭审证词（「hates/die」）。
- 访谈页与主页账本的覆盖率就此对齐；引文全部复用既有已核实锚点，零新增未核实内容。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证 interviews.html 在 1440px 与 375px 的渲染。


## v2.5.0 — 2026-09-13 · 三页子站与账本同步（自动化今夜第 13 轮）

**主题包成果**
- interviews.html：9 → 12 条表态，补入新年份三条（Telepathy / 塔接火箭 / 无限金钱外挂），引文全部复用已核实锚点。
- x-posts.html：8 → 9 张帖卡，新增 Telepathy 官宣帖（含原帖编号）。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证 interviews.html 与 x-posts.html 在 1440px 与 375px 的渲染。


## v2.4.0 — 2026-09-13 · 新增一手深读条目×2（自动化今夜第 12 轮）

**主题包成果**
- 言行实录 24 → 26 条：
  - 2025 Boring Company 商业化——官网项目页口径（68 英里/104 站/90k pax）+ Encore 车站/机场段/旅游局协议 + 230 亿估值融资（报道口径，已标注）+ ProPublica 监督批评入注；
  - 2025.11.06 股东年会「infinite money glitch」——全文转录核实 + 与 Optimus 共舞（Sky News）+ 「8.5 万亿市值与数百万机器人由他本人控制兑现进度」的收尾观察。

**质量门**
- node --check 通过；无重复 id；锚点完整（官方页面口径与报道口径分别标注）；浏览器验证 1440px 与 375px。


## v2.3.0 — 2026-09-13 · 新增一手深读条目×2（自动化今夜第 11 轮）

**主题包成果**
- 言行实录 22 → 24 条：
  - 2015.04.30 Powerwall 发布会——「they suck」+「改变世界能源基础设施」逐字引语（TechCrunch/ABC），7kWh 起价 3000 美元；
  - 2022.11.28 Twitter Files 预告——可核实部分（系列时间线、free speech suppression 框架）为正文，预告措辞以「广泛征引、未复核逐字」诚实标注入引文块。

**工程修复**
- 发现并修复上一轮的版本同步遗漏：app.js 的 SITE_VERSION 在 v2.2.0 轮被漏改（停在 2.1.0），本轮直接归位 2.3.0 并复查三处一致。

**质量门**
- node --check 通过；无重复 id；锚点完整；诚实标注机制再次用于未复核逐字的广泛征引措辞；浏览器验证 1440px 与 375px。


## v2.2.0 — 2026-09-13 · 自由精进：第一手四页统一导航（自动化今夜第 10 轮）

**主题包成果**
- 「第一手」四页板块（账本/文档馆/访谈/帖史）顶部统一 pill 式导航，aria-current 标识当前页。
- 主页「经典商战」板块新增指向「第一手」的互链，叙事与原始材料形成对照环。

**事实纪律说明**
- 本轮 WebSearch 连续超时，按纪律不写任何未经核实的新引文，转为纯结构精进——宁缺毋滥。

**质量门**
- node --check 通过；四页导航 aria-current 正确；浏览器验证 1440px 与 375px 渲染。


## v2.1.0 — 2026-09-13 · 新增一手深读条目×2（自动化今夜第 9 轮）

**主题包成果**
- 言行实录 20 → 22 条：
  - 2021.07 SolarCity 庭审作证——「讨厌当 CEO、没有我公司会死」的证词张力（治理模型的第一手注脚）；
  - 2021.08 AI Day Optimus 表态——「worth more than the car business, worth more than FSD」+ 2022 真机复述 + 2024 的 25 万亿美元量级升级。
- 事实纪律实战：SolarCity 庭审「banality / boring stuff」类说法经四组搜索查无出处，按纪律弃用；只采用 The Next Web 可核实的证词表述。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证 1440px 与 375px。


## v2.0.0 — 2026-09-13 · 言行实录破 20 条里程碑（自动化今夜第 8 轮）

**主题包成果**
- 新增 2 条一手深读条目：2018.01.28 Boring Company「Not-a-Flamethrower」营销战役（丧尸推文原帖核实，两万台售罄筹资约 1000 万）与 2024.01.29 Neuralink「Telepathy」官宣（临床帖+命名帖双帖结构核实）。
- 言行实录 18 → 20 条，版本跳至 2.0.0 致敬里程碑。

**质量门**
- node --check 通过；无重复 id；锚点完整（X 原帖编号 + The Guardian 报道）；浏览器验证 1440px 与 375px。


## v1.9.0 — 2026-09-13 · x-posts.html X 帖史选辑（自动化今夜第 7 轮）

**主题包成果**
- 新独立页 x-posts.html：8 张商业名帖暗色卡片墙（原帖式设计：头像/日期/正文/中译/背景后续），含 2018 funding secured、2019 破玻璃解释、2022 两连发、2023 Grok 首发、2024 Grok-1 开源、2024 塔捕三连发。
- 新核实锚点：Grok 首发公告（2023-11-04）与 Grok-1 开源宣布（2024-03-11，原帖 status/1767108624038449405；xAI 官网 3.17 Apache 2.0 发布）。
- index/documents/interviews 三处互链打通，「第一手」升级为四页板块。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证 x-posts.html 在 1440px 与 375px 的渲染。


## v1.8.0 — 2026-09-13 · interviews.html 访谈与表态专页（自动化今夜第 6 轮）

**主题包成果**
- 新独立页 interviews.html：9 条一手表态按时间排列（2006–2023），每条 = 场合背景 + 逐字原话 + 中译 + 「后续」注脚 + 来源徽章（TechCrunch/WaPo/Space.com/NASA/Fortune/Reuters 等）。
- index「第一手」板块新增「访谈与表态专页 →」与「文档馆全文 →」双入口；documents.html 页脚互链访谈页。
- 「第一手」至此升级为三页板块：index 账本 + documents 文档馆 + interviews 访谈表态。

**自主优化**
- 互链设计形成阅读环：账本 → 文档 → 访谈 → 回主页。

**质量门**
- node --check 通过；无重复 id；锚点完整；引文全部为此前已核实条目；浏览器验证 interviews.html 与 index 在 1440px 与 375px 的渲染。


## v1.7.0 — 2026-09-13 · documents.html 一手文档馆（自动化今夜第 5 轮）

**主题包成果**
- 新独立页 documents.html「一手文档馆」：6 份第一手文档深读（2006 秘密蓝图全文五步、2016 Part Deux 四支柱、2022 Extremely Hardcore 邮件、2023 xAI 宣言、2023 Part 3、2025 Part IV）。
- 每份：原文逐段摘录（blockquote）+ 逐段中译 + 「本站注释」（含背景解读与二进制决策/资本循环等方法论观察）+ 「兑现情况」注脚 + 来源徽章。
- 页面复用主站设计令牌（style.css），杂志风一致；整页中英并列（原句恒显 + 中译跟随），noindex。

**自主优化**
- index「第一手」板块的「原话文档」小节新增「文档馆全文 →」入口，首页与文档馆形成导流闭环。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证 documents.html 与 index 在 1440px 与 375px 的渲染。


## v1.6.0 — 2026-09-13 · 新增一手深读条目×3（自动化今夜第 4 轮）

**主题包成果**
- 言行实录 15 → 18 条（全部深读版）：
  - 2019.11.21 Cybertruck「装甲玻璃」碎裂现场——含 BBC 引他的推文解释原文与「免费广告」后续；
  - 2020.05.30 Demo-2 载人首飞——NASA 通稿引语 + 「我不太信教，但这一次我祈祷了」；
  - 2023.11.29 DealBook 广告主风波——CNBC 记录原话（脏话按 CNBC 口径消音处理）与完整语境（点名 Iger、威胁反杀逻辑）。
- 三条新锚点均经 WebSearch 核实（NASA/BBC/CNBC/Wired）。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证 1440px 与 375px。


## v1.5.0 — 2026-09-13 · 言行实录深读·第三批（自动化今夜第 3 轮）

**主题包成果**
- 4 条升级深读版（背景→原话→现场→后续）：2013 死在火星、2023 蓝图三、2023 xAI 使命（并入 07.14 Spaces 的 AI 安全动机原句）、2025 蓝图四。
- 新增条目「the machine that builds the machine」（2016）：投资者语境 + alien dreadnought 代号 + Grohmann 收购 + 2018「Humans are underrated」自我修正。
- 至此 15 条实录全部完成深读改造，无遗留浅条目。

**质量门**
- node --check 通过；无重复 id；锚点完整；新引文（Reuters/Teslarati/Ars Technica/tesla.com）逐条核实；浏览器验证 1440px 与 375px。


## v1.4.0 — 2026-09-13 · 言行实录深读·第二批（自动化今夜第 2 轮）

**主题包成果**
- 5 条实录升级深读版（背景→原话→现场→后续）：2016 蓝图 2.0（SolarCity 整合争议与 SEC 备案细节）、2017 生产地狱（「承诺苦难」的发布会）、2022 TED（台上承认「不确定买不买得下来」）、2022 Extremely Hardcore 邮件（二选一通牒现场）、2024 塔捕（七分钟穿焰降落与 Starship 经济学）。
- 引文全部为此前已核实条目（TechCrunch/WaPo/Fortune/The Verge/Reuters/AP），本轮未新增未核实引文。

**质量门**
- node --check 通过；无重复 id；锚点完整；浏览器验证 1440px 与 375px。


## v1.3.0 — 2026-09-13 · 言行实录深读·第一批（自动化今夜第 1 轮）

**主题包成果**
- 5 条实录升级为深读版（背景→原话→现场→后续 四段结构）：2006 秘密蓝图、2008 Falcon 1 第四发、2018 funding secured、2022 let that sink in（新增条目）、2022 the bird is freed。
- 新条目「let that sink in」（2022.10.26）经 X 原帖核实（status/1585341984679469056）；「Spoiler alert: Let the good times roll」经 Washington Post 核实。
- 深读版式：白色引文块 + 酒红小节标签（背景/原话/现场/后续 双语），条目高度约为原 3-4 倍。

**自主优化**
- 深读版式可复用（.ps-deep 类），后续批次沿用。

**质量门**
- node --check 通过；无重复 id；锚点完整；新引文逐条核实；浏览器验证 1440px 与 375px。


## v1.2.0 — 2026-09-13 · P2-P4 第一手资料续包（一口气交付）

**主题包成果**
- 言行实录 10 → 13 条：新增 2017「Welcome to production hell」、2023「Sustainable Energy for All of Earth」、2025「Sustainable abundance」。
- 原话文档 3 → 5 份：新增 Master Plan Part 3（2023.04.05）与 Part IV（2025.09.01），核实自 Tesla 官网与报道。
- 语录区补诚实注脚：四句广泛征引的表述因精确出处年份不可考，明确标注「不杜撰出处」。

**质量门**
- node --check 通过；无重复 id；新引文均经 WebSearch 核实（tesla.com/master-plan-part-4 等）；浏览器验证 1440px 与 375px。

## v1.1.0 — 2026-09-13 · P1 第一手资料板块（用户定向：只收一手材料）

**主题包成果**
- 新板块「11 / 第一手」，导航新增「第一手」入口。
- 言行实录 10 条（2006 秘密蓝图 → 2024 塔接住了火箭）：每条 = 日期 + 英文逐字原话 + 本站中译 + 对应之「行」+ 出处徽章。
- 原话文档 3 份（深色公文卡）：Master Plan 2006 / Part Deux 2016 / Extremely Hardcore 2022，各带「兑现情况」注脚。
- 全部引文经 WebSearch 逐条核实措辞与日期（Tesla 博客、SEC 备案、Space.com、Reuters/AP、TechCrunch/WaPo、Fortune/The Verge、X 原帖）。

**自主优化**
- 双语排版约定：原句恒显（本身即英文），中译行在英文模式隐藏避免重复（html[lang=en] .ps-zh）。
- 打印样式：文档卡转白底黑框，账本行不跨页。

**质量门**
- node --check 通过；无重复 id；锚点完整；引文措辞与日期均溯源公开报道；浏览器验证 1440px 与 375px。

## v1.0.0 — 2026-09-13 · 🎉 正式版（M17 终版 QA · 自动化第 16 轮）

**终版走查（全部通过）**
- 全站错别字、死链、重复 id、锚点完整性：通过；控制台无报错；双语完整性 data-en 354 处。
- 三档宽度（375 / 768 / 1440）+ 中英双语视觉走查：无重叠、无破版。
- 清理临时文件 style-preview.html（风格选型对比页，历史已存 git）。
- 版本定格 **1.0.0 正式版**。全站共 10 大板块（封面/速览/时间线 21 条/公司版图/四份公司档案/商战四篇/商业人格/方法论/数据图表/xAI·语录）。

**自主优化**
- 页脚署名更新为「17 个版本，从 v0.1 到 v1.0」。


## v0.17.0 — 2026-09-13 · M16 代码重构 + 英文文案审校（自动化第 15 轮）

**主题包成果**
- 清理死代码：废弃 .quotes-wrap 规则移除；计数器观察器 cio2→counterObs 语义化命名；外观零变化（本轮浏览器截图组件瞬时故障，以 DOM 探针验证页面完整可交互 + 本轮改动均为命名/文案级，风险可控；下轮 M17 终版 QA 将补全量视觉走查）。
- 英文母语级复审：时间线与商战叙事 2 处润色；全站 data-en 逐条复核无翻译腔。

**自主优化**
- 「07 语录」分区注释指向更新。


## v0.16.0 — 2026-09-13 · M15 彩蛋与个性（自动化第 14 轮）

**主题包成果**
- Konami 彩蛋（↑↑↓↓←→←→BA）：线稿纸飞机携酒红虚线航迹掠过纸面，2.6 秒自清理；页脚灰色小提示。
- 编者按彩蛋：每次加载随机抽取语录区一条金句（中英对照）入页脚。
- 两者均尊重 prefers-reduced-motion。

**自主优化**
- 编者按文案采用「编者按 / Editor's note」双语格式，与全站双语气质统一。


## v0.15.0 — 2026-09-13 · M14 SEO / 元信息 / 更新日志页（自动化第 13 轮）

**主题包成果**
- 补全 keywords / Open Graph / Twitter Card 元信息；新增酒红 M 字 SVG favicon（data URI，离线可用）；theme-color 此前已就位。
- 新建 changelog.html「修订记录」页：由 CHANGELOG.md 自动渲染（脚本解析），杂志风排版，页脚版本号点击可达；页带 noindex。

**自主优化**
- changelog.html 复用主站 style.css 设计令牌，视觉与主站完全一致；返回主页链接常驻左上。


## v0.14.0 — 2026-09-13 · M13 可访问性 + 性能（自动化第 12 轮）

**主题包成果**
- scrollspy 高亮同步 aria-current；Escape 键关闭汉堡菜单并回焦按钮。
- 页脚注脚颜色 #8a857c→#98938a（对比度 ≥4.5:1）；肖像图补 decoding="async"。
- 盘点确认已在位：skip-link、:focus-visible 焦点环、prefers-reduced-motion 全覆盖（轮播/计数器/图表/汉堡动画均适配）、照片 lazy+async+定比、进度条 rAF 节流。

**自主优化**
- 语言切换按钮 aria-pressed 状态与 aria-current 导航语义形成完整可访问性闭环。


## v0.13.0 — 2026-09-13 · M12 移动端深度适配（自动化第 11 轮）

**主题包成果**
- 汉堡菜单（≤760px）：原生 JS 开合、三条线→×动画、aria-expanded/aria-controls 完整、reduced-motion 兼容。
- 触控目标：导航项 12px 行高 + 底边线（整行 ≥44px）、轮播圆点 11→16px。
- 375px 逐板块走查：hero 竖排、卡片/图表/时间线单列（前几轮已落实），本轮补窄屏导航与圆点触控。

**自主优化**
- 菜单项虚线分隔 + 激活项酒红，视觉与杂志风统一。

## v0.12.0 — 2026-09-13 · M11 动效与阅读体验（自动化第 10 轮，M11 重试成功）

**主题包成果**
- 顶部阅读进度条（酒红 3px，rAF 节流）；封面统计数字滚动（9/44/4，reduced-motion 直接显示终值）。
- 语录自动轮播：原生 scroll-snap 横向滚动 + 动态圆点（可点、酒红激活态），7s 播放、悬停暂停、缩放重对齐、reduced-motion 停用。

**工程教训**
- 上轮重写语录 DOM 后被浏览器解析器整体丢弃且静态检查无法发现；本轮改用「外壳包裹」策略（引言卡零改动，仅换容器+追加圆点），DOM 探针验证通过后提交。

## v0.11.0 — 2026-09-13 · M10 真实素材扩充（自动化第 9 轮）

**主题包成果**
- 经 Commons API 检索下载 2 张真实照片并 `file` 校验：
  - 「Falcon Heavy liftoff KSC20180260」（2018 首飞，LC-39A）→ SpaceX 公司特稿配图
  - 「Tesla Factory, Fremont」→ Tesla 公司特稿配图
- 均为 width=800 拉取（实际 960px），中文 alt、`loading="lazy"` + `decoding="async"`、来源标注进图注。
- 21:9 杂志式裁切 + 细黑框白边，与封面肖像框风格一致。

**自主优化**
- 打印时照片自动加 20% 灰度（更接近纸媒质感），且不跨页截断（BACKLOG「图片单色调」的打印先行版）。

**质量门**
- node --check 通过；无重复 id；data-en 354 处；两张图片经服务器 200 验证；浏览器视觉验证 1440px + 375px，裁切与图注无破版。

## v0.10.0 — 2026-09-13 · M09 数据可视化（自动化第 8 轮）

**主题包成果**
- 新板块「08 / 数据一览」，导航新增「数据」入口；后续章节顺延（xAI·Grok→09、语录→10）。
- 三张纯 SVG 图表：①主要交易金额通栏条形图（Zip2 3.07 亿 → PayPal 15 亿 → SolarCity 26 亿 → Twitter 440 亿，线性坐标如实呈现量级差）②Tesla 市值里程碑（2021 $1T 实线达成 vs 2025 $8.5T 薪酬方案目标虚线，达成与目标严格区分）③身家里程碑（$500B 首破 → ≈$892B）。
- 全部图表带标题、单位、数据来源标注；诚实性注释（如「Twitter 与其余三笔不在一个量级——坐标如实保留」）。

**自主优化**
- 生长动画：scaleX + 逐条延迟，进入视口触发；reduced-motion 与打印场景直接呈现最终状态（打印不丢图表）。

**质量门**
- node --check 通过；无重复 id；data-en 达 352 处；图内数字全部可溯源 FACTS；浏览器视觉验证 1440px（动画后状态）与 375px（等比缩放）中文，无重叠破版。

## v0.9.0 — 2026-09-13 · M08 商业方法论板块（自动化第 7 轮）

**主题包成果**
- 新板块「07 / 可复用的方法」，导航新增「方法」入口；后续章节顺延（xAI·Grok→08、语录→09）。
- 六张方法卡（原则 + 案例 + 适用边界）：① 先定物理上限再谈成本 ② 最好的零件是不存在的零件 ③ 把「不可能」拆成日程表 ④ 垂直整合卡脖子环节 ⑤ 现场优于汇报 ⑥ 用表达换杠杆。
- 诚实性设计：板块导语显性声明「编辑提炼、并非原话」；每卡边界句含合规/治理提醒（SEC 红线、SolarCity 关联交易争议等），案例全部引用站内已核实事实。

**自主优化**
- 打印保护扩展至方法卡。
- 方法卡案例左边线采用藏蓝、边界用斜体灰，与「行为证据」卡形成视觉区分。

**质量门**
- node --check 通过；无重复 id；data-en 达 342 处；数字全部可溯源 FACTS；浏览器视觉验证 1440px 中英 + 375px 中文（即时定位），无重叠破版。

## v0.8.0 — 2026-09-13 · M07 商业人格板块（自动化第 6 轮）

**主题包成果**
- 新板块「06 / 商业人格」，导航新增「人格」入口；后续章节顺延（xAI·Grok→07、语录→08）。
- 六张「行为证据卡」：Ⅰ 第一性原理 / Ⅱ 极端风险偏好 / Ⅲ Hardcore 文化 / Ⅳ 垂直整合 / Ⅴ 用人逻辑 / Ⅵ 表达即战略。
- 每卡结构：定义 → 「行为证据」两条（仅 FACTS 与广为公开报道的行为，数字全部在案）→ 酒红斜体提炼句。明确「不猜动机，只看行为」的方法论。
- 卡片设计：罗马数字水印、悬停微动效、3/2/1 列响应式。

**自主优化**
- 打印保护扩展至人格卡片。
- 排查发现验证脚本此前受全局平滑滚动影响存在「截图截在滚动中途」的假阳性，本轮起验证改用即时定位（站点本身的平滑滚动保留，面向用户体验不变）。

**质量门**
- node --check 通过；无重复 id；data-en 达 320 处；例证全部可溯源 FACTS 或公开报道；浏览器视觉验证 1440px 中英 + 375px 中文（即时定位复拍），无重叠破版。

## v0.7.0 — 2026-09-13 · M06 商战故事 ③④：生产地狱与 SEC 事件（自动化第 5 轮）

**主题包成果**
- 「快读」双联短篇上线：《Model 3 生产地狱》（订单如山→GA4 帐篷产线→睡车间→6 月最后一周压过周产 5000）与《一条推文，4000 万美元》（funding secured→SEC 证券欺诈起诉→各罚 2000 万合计 4000 万→卸任董事长保留 CEO→重大推文先过律师）。
- 共用版式：卡片式快读（约 3 分钟徽章）、酒红左边线粗体金句抽出、双列（窄屏单列）。
- 第四篇收尾互相勾连：SEC 事件解释了 𝕏 时代的平台执念，叙事线闭环。

**自主优化**
- .flash 悬停微动效，与公司卡片动效语言保持一致。
- 打印保护扩展至快读卡片。

**质量门**
- node --check 通过；无重复 id；data-en 达 280 处；数字全部可溯源（周产 5000、$420、各 $2000 万、2020 全球第一车企）；浏览器视觉验证 1440px 中英 + 375px 中文，无破版。

## v0.6.0 — 2026-09-13 · M05 商战故事 ②：440 亿收购 Twitter 全程（自动化第 4 轮）

**主题包成果**
- 《买下全球的广场》：六节点交互式竖向时间轴（低调建仓 → 54.20 要约 → 冻结 → 退出未遂被诉 → 强制交割 → 更名 X），点击展开/收起细节，纯 CSS grid-rows 动画。
- 无障碍：节点为原生 button，aria-expanded + aria-controls 完整，键盘可操作。
- 数据侧栏「交易解剖」五行卡（10 个月建仓到交割 / $54.20 / $440 亿 / 1 起强制履行诉讼 / 9 个月到更名）+ 黑底「一句话复盘」结论盒。

**自主优化**
- 打印修复：手风琴内容在打印时自动全部展开（否则 PDF 会丢失未展开细节）。
- 首节点默认展开，让交互可供性一目了然。

**质量门**
- node --check 通过；无重复 id（acq-d1~d6 全部匹配 aria-controls）；data-en 达 264 处；日期与数字全部可溯源 FACTS 或由其推导（4.14→4.25 的 11 天、9 个月更名等）；浏览器视觉验证：1440px 中英双语交互点击、375px 窄屏，无重叠破版。

## v0.5.0 — 2026-09-13 · M04 商战故事 ①：2008 至暗时刻（自动化第 3 轮）

**主题包成果**
- 新板块「05 / 经典商战」，导航新增「商战」入口；后续章节顺延（xAI·Grok→06、语录→07）。
- 长文《2008：同时押注两个不可能》：商学院案例式开头、SpaceX 三连败→第四发入轨→NASA 16 亿合同、Tesla 接任 CEO 与借钱付房租的公开讲述、结尾复盘「同一个判断的两次应用」。
- 杂志特稿组件首发：中文首字下沉（酒红衬线）、双细线引言拉页（FACTS 语录 ① + 中译 + 署名）、四列数据条、右侧栏「手绘线稿 SVG」（发射塔 + 火箭 + 虚线尾焰）与「那一年，按顺序」时间小轴（2008→2010.06 五节点）。

**自主优化**
- 全站新增 ::selection 酒红选中效果（配合设计系统强调色）。
- 打印保护扩展：拉页引用、时间小轴、插画不跨页截断。
- CSS 分区注释编号与章节重编号同步（05→07 语录修正）。

**质量门**
- node --check 通过；无重复 id；data-en 达 239 处；9 个页内锚点逐一校验存在；数字全部可溯源 FACTS（三连败/09.28/$16 亿/2008.10/2.26 亿）；浏览器视觉验证 1440px 中英 + 375px 中文，无重叠破版。

## v0.4.0 — 2026-09-13 · M03 公司商业史（下）：X、xAI 与其余（自动化第 2 轮）

**主题包成果**
- 「公司深度」扩至四份档案：新增「公司特稿 Ⅲ · 𝕏」（《440 亿美元买下的全球广场》：建仓→要约→反悔被诉→强制交割→更名）与「公司特稿 Ⅳ · XAI」（《亮相仅二十个月，它吞下了一个社交平台》：Grok 节奏→反向收购→Series E 200 亿）。
- 两份新档案各含 5 个硬数据点（$54.20/$440 亿/≈$330 亿；2023.07/≈$800 亿/$200 亿）+ 5 条关键决策。
- Neuralink / Boring 简卡文案加厚（业务切入点与商业逻辑）。
- 「早期交易记录」从列表升级为正式三列表格（交易 / 年份 / 退出与要点），含 Zip2、PayPal、SolarCity、OpenAI 四笔。

**自主优化**
- 导航新增「深度」入口，scrollspy 自动识别公司深度板块。
- 修正板块标题与数量不一致（两份→四份）。
- 窄屏导航间距与表格换行优化（375px 实测）。

**质量门**
- node --check 通过；无重复 id；data-en 达 216 处；新数字全部可溯源 FACTS（含 Series E、估值口径）；浏览器视觉验证 1440px 中英 + 375px 中文，表格与特稿无破版。

## v0.3.0 — 2026-09-13 · M02 公司商业史（上）：Tesla 与 SpaceX（自动化第 1 轮）

**主题包成果**
- 新板块「04 / 公司深度」：Tesla 与 SpaceX 两份杂志式公司特稿。
- 每份档案：衬线大标题 + 斜体导语 + 五列硬数据行（A 轮 $650 万 / IPO $2.26 亿 / 万亿市值 / 薪酬上限；自投 $1 亿 / NASA $16 亿 / 猎鹰重型 / 载人入轨 / 筷子回收）+ 双栏正文（窄屏单栏）+ 编号「关键决策」侧栏（各 5 条）。
- 章节编号顺延：xAI·Grok → 05，语录 → 06。

**自主优化**
- 「公司版图」「公司深度」「语录」三个章节补充斜体导语，统一杂志「编者按」腔调（BACKLOG 项）。
- 打印样式增强：特稿、数据行、卡片、语录 break-inside: avoid，PDF 存档不跨页截断。
- 质量门中发现并修复：①英文模式下数据行残留中文货币单位（≈$1亿→≈$100M 等 4 处补 data-en）；②特稿与窄屏锚点被吸顶报头遮挡（补 scroll-margin）。

**质量门**
- node --check 通过；无重复 id；新增文案全部双语（全站 data-en 达 180+）；全部数字可溯源 FACTS；浏览器视觉验证 1440px（中/英）与 375px（中文），排版无重叠破版。

## v0.2.0 — 2026-09-13 · M01 商业时间线深度扩容（人工完成，自动化接力前）

**主题包成果**
- 时间线 16 → 21 条，补齐 FACTS 全部年份节点：新增 2000（X.com×Confinity 合并、PayPal 诞生）、2006（参与创办 SolarCity）、2015（联合创立 OpenAI）。
- 2018 拆为两条：Falcon Heavy 首飞（产品里程碑）与 SEC 罚单事件（争议时刻，「一条推文，4000 万美元」）。
- 2025 拆为两条：xAI 反向收购 X + Grok 4；身家首破 5000 亿 + 万亿美元级薪酬方案获批。
- 时间线顶部新增分类筛选按钮（全部/创业起步/资本运作/豪赌翻身/产品里程碑/争议时刻），原生 JS，筛选带淡入动画，按钮激活态与分类配色一致。

**自主优化**
- 筛选按钮栏兼任「分类图例」（激活色 = 标签色），不需要额外图例行。
- 页脚新增「返回顶部 ↑」链接（BACKLOG 项）。
- 新增 @media print 打印样式：隐藏导航/按钮/动效残留，白底黑字，方便存档为 PDF（BACKLOG 项）。

**质量门**
- node --check 通过；无重复 id；21 条时间线全部带 data-en 双语（全站 135 处）；新数字均可溯源 FACTS；浏览器视觉验证：1440px 中文（筛选交互）+ 英文、375px 窄屏，均无破版。

## v0.1.0 — 2026-09-13 · 创刊号地基（人工完成）

**定位重构**
- 站点从「粉丝向介绍站」重构为「商业人物志」：只讲商业人格、商业经历、商业故事、商界传奇；不含任何感情/家庭内容。
- 读者定位：想了解马斯克商业方法的中文读者，默认中文、一键切英文。

**视觉**
- 落定浅色商业杂志风：纸面底、衬线大标题、酒红 kicker、发丝分隔线、成交行（dotted deal-lines）、细黑框肖像。

**双语**
- 中/EN 一键切换：`data-en` 属性约定 + localStorage 记忆 + `<html lang>` 同步，全站 113 处文案双语覆盖。

**内容板块**
- 封面（卷首特稿 + 肖像 + 关键数字成交行）
- 01 速览（三段商业叙事 + 快速档案）
- 02 商业时间线（16 条，全部带硬数据与分类标签）
- 03 公司版图（6 张公司卡 + 早期交易记录表）
- 04 xAI·Grok（反向收购逻辑 + 关键节点表）
- 05 语录（4 条，英文原句 + 中译）

**数据核实（本轮新增事实）**
- 2025-11-06 Tesla 股东以约 75% 支持批准马斯克绩效薪酬方案（达标约 1 万亿美元级）
- 2026-01 xAI 完成 200 亿美元 Series E（超 150 亿目标，英伟达/思科参投，估值约 2300 亿量级）
- 2025-10-01 Forbes 史上首位身家破 5000 亿美元

**交互**
- 入场动画（IntersectionObserver）、导航 scrollspy、`prefers-reduced-motion` 全适配、skip-link。

**质量门**
- node --check 通过；无重复 id；本地资源引用完整；双语叶子节点约定无嵌套违规。
