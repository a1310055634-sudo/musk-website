# V8 计划进度记录（第一手信息扩充）

> 「马斯克商业志 MUSK, INC.」v8.0 扩充计划（共 10 轮，2026-09-30 启动）。
> 本文件是本计划的唯一轮次账本；与 git 提交记录相互核验，不以提交总数推算轮次。
> 历史计划（V7 十九轮改版，v6.6.0→v7.0.0）已完结，见 `V7-19-PROGRESS.md`，不继承其计数。

## 基线快照（2026-09-30 核对）

- 分支 main @ `d0b8b4b`（V7-19 R19 收官提交），VERSION `7.0.0`
- 工作区干净；37 个 HTML 页面；账本 67 条；检索索引 178 条；verify.py 9 项检查
- 每轮版本步进：R01=v7.1.0 → R09=v7.9.0 → R10=v8.0.0（每轮 bump，防版本重复，吸取 v5.88.1 教训）

## 轮次状态

| 轮 | 主题 | 状态 | 版本 | 成果提交 | 推送 |
|---|---|---|---|---|---|
| 01 | 建 V8-PROGRESS.md + funding secured 案（SEC v. Musk） | complete | v7.1.0 | 398b249 | done |
| 02 | Twitter 收购案私信原件（特拉华衡平法院披露件） | complete | v7.2.0 | a48c1df | done |
| 03 | SEC EDGAR 公文扩容（8-K/proxy/合并协议条款） | complete | v7.3.0 | eceb6ee | done |
| 04 | 财报电话会 I（2013–2018） | complete | v7.4.0 | 7440bd7 | done |
| 05 | 财报电话会 II（2019–2026） | complete | v7.5.0 | 10b41bd | done |
| 06 | 长访谈 I：Lex Fridman 四期 | in_progress | — | — | — |
| 07 | 长访谈 II：Rogan / TED / All-In / DealBook | pending | — | — | — |
| 08 | X 帖史扩容（含 Wayback 核对已删帖） | pending | — | — | — |
| 09 | SpaceX / Neuralink / xAI 官方演讲 | pending | — | — | — |
| 10 | 全站验收与发布 v8.0.0 | pending | — | — | — |

状态取值：pending / in_progress / complete / blocked。失败不推进轮次；推送失败时仅恢复推送。

## 恢复指引

- 每轮唯一成果提交信息带 `[V8 Rxx]` 前缀；工作记录追加在本文件末尾。
- 提交了但没推送 → 直接 `git push`，不重做工作。
- 账本/一手页变动后必跑：`build-ledger-timeline.py` / `build-search-index.py`（改断言）/ `build-epub.py`；CHANGELOG 更新后跑 `sync-changelog.py`；最后 `verify.py` 9 项全绿。
- 采料纪律：查不到原文不写；媒体转载两源印证；引语保留英文原文+中文对照。
- 本计划不再新建分支，直接在 main 上逐轮提交（V7 时代分支流程已完成使命）。

## 核实来源留档（R05）

十场 Tesla 财报电话会逐字稿（stockanalysis.com/stocks/tsla/transcripts/ 全文直读，Quartr 转写；索引页含 2011–2026 全部季度 ID）：
- Q1 2019（2019-04-24）= /23954-q1-2019/；Q4 2019（2020-01-29）= /459-q4-2019/；Q2 2020（2020-07-22）= /7605-q2-2020/；Q4 2021（2022-01-26）= /12798-q4-2021/；Q3 2022（2022-10-19）= /27338-q3-2022/；Q3 2023（2023-10-18）= /83764-q3-2023/；Q1 2024（2024-04-23）= /161624-q1-2024/；Q3 2024（2024-10-23）= /215125-q3-2024/；Q1 2025（2025-04-22）= /310668-q1-2025/；Q2 2026（2026-07-22）= /653184-q2-2026/
- 两源印证：**Q1 2019 增发** Reuters 2019-05-02「Tesla ends 'Spartan diet'…$2.3B」+ Reuters 2019-05-03「Tesla boosts capital raise to $2.7 billion, Musk buys more」（本人认购约 $25M）；**Q4 2019 FSD** Fortune 2020-01-29（「We got pretty close, it's looking like we might be feature complete in a few months」）+ Seeking Alpha 逐字稿（article/4320044）；**Q2 2020 同款表态前哨** CNBC TV18 2020-07-09（WAIC「very close to Level 5」）；**Q4 2021 Optimus** CNN Business（「more significant than the vehicle business」）；**Q3 2022** Business Insider markets（Apple+Aramco 合计约 $4.4T）+ Fortune India/Benzinga/Observer；**Q3 2023** TechRadar 2023-10-19（dug our own grave）+ Wccftech（Bernstein note）；**Q1 2024** Seeking Alpha（「We'll talk about this more on August 8」）+ Shacknews/Teslarati（8/8 最早出自 Musk X 帖 2024-04-05，Reuters 等报道）；**Q3 2024** Investopedia takeaways + Fortune 2024-10-24（次日 +22%、单日 +$30B）+ Last Bastion（含「if we execute on our objectives」条件从句全句）；**Q1 2025** The Hill 2025-04-22（DOGE 原句逐字）+ Yahoo Finance（股价反应）+ USA Today（净利 -71%、「a day or two per week」）；**Q2 2026** elonmuskarchive.org 转写存档（「Optimus will be the biggest product ever」）+ investing.com 预告（call 日期 2026-07-22）
- 甄别记录（宁缺毋滥）：①「Tesla 工厂是 money printing machines」传闻经 Q2 2022 逐字稿直读证伪——原话「license to print money」「minting money」实指锂精炼业务而非工厂，弃收；②Q1 2020「Give people back their goddamn freedom」「this is fascist」逐字确凿（逐字稿在档），但与在册 e2020-05-11 复工弧线重叠（其背景段已引该 call），本轮不单独立条；③Q1 2019「有理由融资」句两家转写有出入（stockanalysis vs Motley Fool），以两句一致立条、该句转述并注明；④估值名句定位在 Q3 2022 call（10-19）而非 Q4 2022（2023-01-25 该场原话为「Long-term, I am convinced that Tesla will be the most valuable company on Earth」，未立条）；⑤Q2 2026 第三方交付数字（如 480,126）仅粉丝站来源，未采信入条。

## 第 5 轮工作记录（财报电话会 II，2019–2026）— complete（2026-09-30）

- **交付**：账本 primary.html +10 条（93→103，严格克隆 `<li class="ps-row ps-deep reveal">` 模板，四段深读双语）：e2019-04-24（Q1 2019 call：斯巴达饮食/强制函数 → 八天后 23→27 亿美元增发，含转写出入如实注）、e2020-01-29（Q4 2019 call：Cybertruck 需求「难以置信」+ FSD「几个月 feature complete」新期限）、e2020-07-22（Q2 2020 call：FSD「年底前完成」+「一场『九』的长征」）、e2022-01-26（Q4 2021 call：Optimus 首获财报会排位「比汽车业务更重要」）、e2022-10-19（Q3 2022 call：「比 Apple 与沙特阿美加起来还值钱」，罕见对冲句一并收录）、e2023-10-18（Q3 2023 call：Cybertruck「我们给自己挖了坟」+「原型到量产难 10,000%」）、e2024-04-23（Q1 2024 call：Robotaxi 8/8 之约 + Optimus「年内工厂做有用任务」，两条期限双双失守）、e2024-10-23（Q3 2024 call：「全球最有价值公司，遥遥领先」+ Cybercab 2026 量产 +「至少每年 200 万台」）、e2025-04-22（Q1 2025 call：DOGE 减时 + 抗议者「拿了钱的」）、e2026-07-22（Q2 2026 call：「Optimus 会是有史以来最大的产品」+ 里程周增 10%——账本 2026 年首条，账上最新一场电话会）。
- **quotes.html** +10 卡（80→90）。**index.html** 计数文案 93→103 ×5。**EXPANSION.md** 顶部补 R05 入包块（含十场逐字稿链接与甄别注）。无新专题页交叉引用需求（估值/FSD 承诺与 promises.html 的挂接，连同 R04 遗留项一并留给 R10 收官轮统一评估）。
- **管线**：build-ledger-timeline（103 节点）/ build-search-index（断言 93→103，索引 219 = 103+14+18+13+5+53+4+9）/ build-revisions（138 锚点）/ sync-changelog / build-epub（179,708 B，24 章）全重跑；版本 v7.4.0→v7.5.0（VERSION/app.js/14 页 span，node --check 通过）；CHANGELOG 首条 v7.5.0。
- **验证**：verify.py 9/9 全绿（语录卡 90 vs 引文块 93 + 3 豁免；EPUB 含 e2026-07-22）；提交后抽查 10 条新条目结构完整（4 段+引语块+中文对照）。
- **提交**：主成果 `10b41bd`（24 文件，+822/−27）；本回填+revisions/EPUB 刷新为第二个提交。
- **实现备注**：①quotes 段首跑被自建断言拦截（81≠90）——根因是 r04-integrate.py 里残留的 quotes 段本就是被 r04-quotes-fix.py 推翻前的错误版本（sub1 吞掉现有卡片开头标签），本轮复制时踩中；回滚 primary.html 后按 r04-quotes-fix.py 修好版（**new = 新卡 + anchor 拼回**）重跑一次通过。**教训固化：复制历史脚本模板前先核对它是否是该坑的修好版，r04-integrate.py 的 quotes 段不可直接复用**。②CRLF 坑：工作区文件经 git checkout 带 CRLF 行尾，split('\n') 后行尾残留 \r，行级插入的精确比较必须 rstrip('\r') 且新行补 \r。③span 步进复制 r02-spans.py 修好版正则（断言 14）一次成功。
- **下一轮预告**：R06 长访谈 I：Lex Fridman 四期（interviews.html +6~8 条，沿用现有访谈页前缀与结构）。

## 核实来源留档（R02）


Twitter, Inc. v. Musk（Del. Ch. **C.A. No. 2022-0613-KSJM**，McCormick 大法官；案卷索引 chancerydocket.com——注意本案无 CourtListener 公开 docket，勿再误引）：
- TIME 全文转载（2022-09-30 发布；披露件 9-29 周四由 Musk 律师提交、@chancery_daily 首发）：https://time.com/6218578/elon-musk-texts-twitter/ （Dorsey/Agrawal/Kimbal/SBF/Lonsdale 逐字 + Ellison 时间线）
- BBC 决裂往来逐字（2022-09-30）：https://www.bbc.co.uk/news/technology-63098117
- Guardian（2022-10-01）：https://www.theguardian.com/technology/2022/oct/01/elon-musk-and-twitter-boss-parag-agrawal-messages-show-blossoming-relationship
- Fortune/AP 披露语境（2022-09-30，Musk 回复 Agrawal「40 秒后」）：https://fortune.com/2022/09/30/elon-musk-friendly-text-messages-twitter-ceo-parag-agrawal-court-trial/
- WaPo Ellison「Roughly what dollar size?」（2022-10-01）：https://www.washingtonpost.com/technology/2022/10/01/elon-musk-texts-twitter-lawsuit/
- Gates 空头短信（Musk 2022-04-22 自晒截图+发推确认，CNBC 2022-04-23 转载，注明无法独立核实）：https://www.cnbc.com/2022/04/23/elon-musk-tweets-that-he-confronted-bill-gates-about-shorting-tesla.html
- SBF $5B 参投与作罢（Axios 2022-10-03）：https://www.axios.com/2022/10/03/sam-bankman-fried-elon-musk-twitter-deal
- 「Your lawyers are using these conversations to cause trouble. That needs to stop」（2022-06-28，Musk→Agrawal/Segal；BI 报道 · Economic Times 转载）：https://economictimes.indiatimes.com/magazines/panache/elon-musks-warning-text-to-twitter-ceo-parag-agrawal-your-lawyers-are-causing-trouble/articleshow/92899468.cms

## 核实来源留档（R04）

九期 Tesla 财报电话会逐字稿（stockanalysis.com/stocks/tsla/transcripts/ 全文直读，Quartr 转写；索引页含 2013–2026 全部季度 ID）：
- Q4 2015（2016-02-10）= /23975-q4-2015/；Q1 2016（05-04）= /23974-q1-2016/；Q2 2016（08-03）= /23973-q2-2016/；Q3 2016（10-26）= /23972-q3-2016/；Q4 2016（2017-02-22）= /23971-q4-2016/；Q2 2017（08-02）= /23968-q2-2017/；Q3 2017（11-01）= /23967-q3-2017/；Q1 2018（05-02）= /23958-q1-2018/；Q2 2018（08-01）= /23957-q2-2018/
- 采料方法备忘：本机 curl 到 stockanalysis.com 被 Cloudflare 拦（Just a moment），**WebFetch 服务端可过**（全文可读，但单次引用限 125 字符，长引语需多轮问询）；web.archive.org 本机 curl 与 WebFetch 均 TLS 中断，不可用；Seeking Alpha/fool.com 直链 404/403。
- 三源印证（Q1 2018 call）：BBC https://www.bbc.com/news/business-43987141 （bonehead/killing me 逐字 + 股价 -5% + Sacconaghi/Levy 反应）、Slate https://slate.com/technology/2018/05/elon-musk-says-a-flufferbot-caused-the-model-3-delays.html （flufferbot 段逐字，Will Oremus 2018-05-02）、The Verge 2018-08-31 回顾 https://www.theverge.com/2018/8/31/17802234/this-week-in-elon-musk-tesla-twitter-investor-shorts （bonehead + YouTube + 「apologized in a subsequent earnings call」）
- Q2 2018 call 道歉：Business Insider https://www.businessinsider.com/elon-musk-apologizes-to-analyst-on-tesla-q2-earnings-call-2018-8 （Mark Matousek 2018-08-01：「I'd like to apologize for being impolite on the prior call」「no excuse for bad manners」+ 110–120 小时工作周 + Jonas「20 年最怪 call」）；Bloomberg 同日报道；Chief Executive 2018-08-02 https://chiefexecutive.net 「the power of a good apology」
- 4·13 自动化推文：Gadgets360/NDTV（2018-04-14）逐字引推文；The Guardian 2018 年表 https://www.theguardian.com/technology/2018/aug/19/elon-musk-tesla-timeline-difficult-painful-year （4 月条目引两句 + 5/3 call bonehead 条目）；注意 Guardian 年表排 4/16，美媒主流口径 4/13（周五晚），锚点从 4/13
- Q3 2017 call 印证：MediaPost（2017-11-02）「one to nine scale」；CNBC 2018-01-03 https://www.cnbc.com/2018/01/03/tesla-q4-2017-production-and-delivery-numbers.html 「deep in production hell」
- 交付数据（条目后续段用）：2017 全年 Model 3 产量 2,685（Q3 260 + Q4 2,425，Tesla 季度报告）；2018 全年交付 245,240 / 2020 交付 499,550 / 2022 交付 1,313,851（Tesla 年度交付报告口径，条目内已注明）

## 第 4 轮工作记录（财报电话会 I，2013–2018）— complete（2026-09-30）

- **交付**：账本 primary.html +10 条（83→93，严格克隆 `<li class="ps-row ps-deep reveal">` 模板，四段深读双语）：e2016-02-10（Q4 2015 call：Model 3 发布预告与「明年底」量产承诺）、e2016-05-04（Q1 2016 call：7/1/2017 供应商契约 + 下半年 10–20 万辆目标，实际落差约 50 倍）、e2016-08-03（Q2 2016 call：Brown 事故后「hardware exists」口径与「35,000 deaths」反问——FSD 时间线膨胀的基准点）、e2016-10-26（Q3 2016 call：solar roof 周五发布预告 + SolarCity「cash neutral」预测）、e2017-02-22（Q4 2016 call：500K/2018 + 1M/2020 预测 +「We anti-sell the Model 3」）、e2017-08-02（Q2 2017 call：「manufacturing hell and supply chain hell on Friday…I meant it」+ 周产 10K 预测 + S-curve 金句）、e2017-11-01（Q3 2017 call：Jonas「How hot is it in hell?」→「level 9→level 8」+ 电池模组线瓶颈）、e2018-04-13（自动化认错推文，作为 flufferbot 前史入册并如实标注非 call 场合）、e2018-05-02（Q1 2018 call：bonehead/killing me/YouTube/flufferbot）、e2018-08-01（Q2 2018 call：道歉开场，funding secured 六天前）。
- **quotes.html** +10 卡（70→80）。**index.html** 计数文案 83→93 ×5。无新专题页交叉引用需求（Model 3 弧线与 2018 私有化弧线已有对应账本行；500K/1M 预测与 promises.html 承诺案的挂接留给 R10 收官轮统一评估）。
- **管线**：build-ledger-timeline（93 节点）/ build-search-index（断言 83→93，索引 209 = 93+14+18+13+5+53+4+9）/ build-revisions（128 锚点）/ sync-changelog（183 条）/ build-epub（172,325 B，24 章）全重跑；版本 v7.3.0→v7.4.0（VERSION/app.js/14 页 span，node --check 通过）；CHANGELOG 首条 v7.4.0。
- **验证**：verify.py 9/9 全绿（语录卡 80 vs 引文块 83 + 3 豁免；EPUB 含最新条目）。
- **提交**：主成果 `7440bd7`（24 文件，+813/−28）；本回填+revisions/EPUB 刷新为第二个提交。
- **实现备注**：①r04-integrate.py 首跑被自建断言拦截（6 处 sub1 的 new 参数漏拼回 anchor，会吞掉下一现有条目的 `<li>` 开头——计数 87≠93 暴露），修复后成功；quotes.html 同款问题由断言拦截（73≠80），改用 r04-quotes-fix.py 独立补齐。**教训已固化：凡「在现有条目前插入新条目」的 replace，new 必须以新条目开头、以 anchor 字符串结尾**。②span 步进本次一次成功（正则复制 r02-spans.py 修好版：`site-version-val">7.3.0<`，断言 14）。③stockanalysis.com 逐字稿是本轮采料主力（Cloudflare 拦 curl 不拦 WebFetch），已记入来源留档。
- **采料甄别（宁缺毋滥）**：①Q4 2013 call（2014-02-19）Gigafactory 表述全为「下周官宣再谈」推迟口径，无出彩逐字，弃收；②Q2 2016 call Autopilot 辩护（Brown 后）各家媒体转述不一（「more deaths」「50%」），无稳定逐字，改以逐字稿直读的 full autonomy/hardware 句立条；③「manufacturing hell and supply chain hell」按转写照录，条目现场段如实注明台上原话为「production hell」（7/28 交付活动已有 e2017-07-28 在册，未重复立条）；④「I'm very confident…10,000 vehicles per week」与「bought the ticket」句中后者疑为转写噪音，未采用。
- **下一轮预告**：R05 财报电话会 II（2019–2026：cybertruck、FSD 时间线、Robotaxi、Optimus 历次表态），账本目标 +8~10 条，同一逐字稿管线（stockanalysis.com ID 已在留档）。

五份 EDGAR 文书（全部 curl 直读原文逐字核验，Acc-no 在册；清单页 https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=… 按 type+dateb 检索）：
- **d2018-08-14** Tesla 8-K（Item 7.01 + Ex-99.1 新闻稿，Acc-no 0001564590-18-021585）：https://www.sec.gov/Archives/edgar/data/1318605/000156459018021585/tsla-ex991_6.htm ——「not yet received a formal proposal」；委员会 Buss/Denholm/Johnson Rice；「no Going Private Transaction will be consummated without the approval of the special committee」
- **d2022-04-11** Twitter 8-K/A（Acc-no 0001193125-22-101041）：https://www.sec.gov/Archives/edgar/data/1418091/000119312522101041/0001193125-22-101041.txt ——4.04 letter agreement / 4.09 辞谢；原始 4.05 8-K 不在 EDGAR 8-K 列表（甄别后不引用）
- **d2022-07-26** Twitter DEFM14A（Acc-no 0001193125-22-202163）：https://www.sec.gov/Archives/edgar/data/1418091/000119312522202163/d283119ddefm14a.htm ——4.13 要约信全文 + Background of the Merger 全节（9.2% 曝光 / 15% 持股上限谈判 / 毒丸 4.15 / 融资承诺 4.21 / Taylor 4.23「压价不太可能成功」/ 4.24–25 放行）
- **d2022-10-27** Twitter 最后一份 8-K（10.27 交割 / 10.31 备案，Acc-no 0001193125-22-272772）：https://www.sec.gov/Archives/edgar/data/1418091/000119312522272772/d411753d8k.htm ——「Mr. Musk became the sole director of Twitter」/ 九董事列名 / NYSE 10.28 摘牌（Form 25→15）/ 债券 101% 控制权要约 / 终止 2018-08-07 循环信贷
- **d2024-04-29** Tesla DEF 14A（Acc-no 0001104659-24-053333）：https://www.sec.gov/Archives/edgar/data/1318605/000110465924053333/tm2326076d15_def14a.htm ——议案三迁州德州 / 议案四追认 2018 奖励 / 2024-02-04 与 02-10 董事会及特别委员会 / 引马斯克 X 帖 / Tornetta No. 2018-0408-KSJM / Denholm 信「reinstate your vote」
- 表决与迁州补充（多源）：2024-06-13 两案皆过、薪酬项约 77%（CNBC/Reuters/AP/Tesla IR）；2024-12 特拉华重申撤销（Bloomberg Law）；Tesla 2024-07-02 8-K 封面注册地 Texas（Acc-no 0001628280-24-030714）

## 第 3 轮工作记录（SEC EDGAR 公文扩容）— complete（2026-09-30）

- **交付**：documents.html +5 份（9→14，编号/结构严格克隆既有 `<article class="doc-article" id="d…">` 模板，四段式「原文摘录+本站注释+兑现情况」双语）：d2018-08-14（funding secured 一周后的特别委员会 8-K，监管口径急刹车）、d2022-04-11（董事会提名五日始末 8-K/A，收购案第一份法律文书）、d2022-07-26（DEFM14A：4.13 要约信全文 + Background 逐日大事记）、d2022-10-27（最后一份 8-K：交割、唯一董事、退市，与 d2022-04-25 协议首尾呼应）、d2024-04-29（Tornetta 后 2018 奖励再批 + 迁州德州双议案 proxy）。
- **交叉引用**：platform-x px-0414 补 d2022-04-11/d2022-07-26 两链、px-1028 补 d2022-10-27；promises.html 2018 私有化案 sv-links 与来源列表各补 d2018-08-14；documents.html d2022-04-25 词条补 d2022-07-26 站内链；reading.html「九份」→「十四份」；doc-path 导读链改写十四份版（中英双语）；og:description 同步。
- **管线**：build-search-index（断言 9→14，索引 194→199）/ build-revisions（128 锚点，文档馆 14）/ sync-changelog / build-epub 全重跑；版本 v7.2.0→v7.3.0（VERSION/app.js/14 页 span，node --check 通过）；CHANGELOG 首条 v7.3.0。
- **验证**：verify.py 9/9 全绿（断链含全部新锚点与跨页链）。
- **提交**：主成果 `eceb6ee`（30 文件，+433/−27）已推送 main；本回填+revisions/EPUB 刷新为第二个提交。
- **采料甄别（宁缺毋滥）**：①Tesla 2018-09-29 SEC 和解无对应 8-K，未强收；②Twitter 2022-04-05 董事会任命原始 8-K 在 EDGAR 8-K 列表缺失，standstill 细节改引 DEFM14A Background（proxy 原文），不杜撰；③候选「Tesla 2022 年会 proxy」经直读议程证伪（无 SolarCity 追认——Chancery 2022-04-27 判 Tornetta 败诉后无需追认），弃用；④2018 CEO Performance Award 授予当年 proxy 未定位到文件，改由 2024 DEF 14A 承载（含「no salary, no cash bonuses」原始条款逐字）；⑤Sharktank 式候选「Tesla 8-K 2018-08-07（推文当日）」经清单核验不存在——推文当日无任何备案，这本身已成为 d2018-08-14 词条注脚的一部分。
- **实现备注**：片段文件 tools/r03-snippet.html + 单次重建 tools/r03-integrate.py（八处 replace 全部唯一性断言）；r03-release.py 的 span 正则有未闭合括号笔误（与 R02 同款），span 步进由临时脚本补跑完成——下次直接复制已修好的版本。
- **下一轮预告**：R04 财报电话会 I（2013–2018：Model 3 量产地狱、solar roof、自动驾驶承诺），账本目标 +8~10 条，逐字稿源 Motley Fool / ir.tesla.com。

## 第 2 轮工作记录（Twitter 收购案私信原件）— complete（2026-09-30）

- **交付**：账本 primary.html +9 条（74→83，严格克隆既有结构、四段深读双语）：e2022-03-26 Dorsey 劝进（「could def help in immeasurable ways」+ 逼宫旧事）、e2022-04-05 Dorsey 祝贺入董事会（「Parag is an incredible engineer. The board is terrible.」「Got very emotional」）、e2022-04-09 Musk↔Agrawal 决裂（「What did you get done this week?」「I'm not joining the board. This is a waste of time. Will make an offer to take Twitter private.」+ 同日 Kimbal blockchain Plan B「no throat to choke」揉入现场段）、e2022-04-16 Lonsdale 转达 DeSantis（政治入场，「Haha cool」）、e2022-04-20 Ellison 一小时承诺 $1B（「Roughly what dollar size?」）、e2022-04-22 Gates 空头对峙（三行往来逐字，Musk 自晒件，ps-src 如实注明非法院披露）、e2022-04-25 签署日拒 SBF（「Blockchain Twitter isn't possible」，Grimes 转达 $5B 参投）、e2022-04-26 Dorsey 斡旋收尾（「too critical to humanity」「At least it became clear that you can't work together」）、e2022-06-28 「Your lawyers are using these conversations to cause trouble. That needs to stop」。
- **quotes.html** +9 卡（61→70）。**交叉引用**：platform-x.html px-0414（要约）补 → e2022-04-09、px-0425（协议）补 → e2022-04-25；index.html 三处「74」计数升 83。
- **管线**：build-ledger-timeline（83 节点）/ build-search-index（断言 74→83，索引 185→194 = 83+9+18+13+5+53+4+9）/ sync-changelog / build-epub 全重跑；版本 v7.1.0→v7.2.0（VERSION/app.js/16 文件 span，node --check 通过）；CHANGELOG 首条 v7.2.0；EXPANSION.md 顶部补 R02 入包块（含可点击来源与甄别注）。
- **验证**：verify.py 9/9 全绿（语录卡 70 vs 引文块 73 + 3 豁免；EPUB 新鲜）。
- **提交**：主成果 `a48c1df`（24 文件，+338/−25），已推送 main。
- **甄别记录（宁缺毋滥）**：①案号勘误——Del. Ch. 正确案号 2022-0613-KSJM（此前记忆中的 2027-01-JTL 有误，CourtListener 63108355 是无关案件，已核实纠正）；②Ellison 回复原句只找到 Musk 问句两源逐字，其回复以 TIME「within an hour committed $1B」转述呈现，网传「I love the idea of buying Twitter」名句两源检索无印证，未采用；③Kim Kardashian / Tim Cook 短信两源检索无果，未收录（留 R08 X 帖史轮再评估，那条实为 Musk 自曝推文而非法庭件）；④Rogan「liberate Twitter from the censorship happy mob」逐字确凿（BBC）但日期仅「late March/early April」模糊，按纪律未单独立条，揉入 e2022-04-05 现场段；⑤Gates 短信为收购案窗口期（4-22，要约与签署之间）的私信原件，主题相容，如实标注来源性质收录。
- **下一轮预告**：R03 SEC EDGAR 公文扩容（documents.html +4~6 份：关键 8-K/proxy/2022-04-25 合并协议条款已有 d2022-04-25 在册，注意查重补新）。

## 核实来源留档（R01）

SEC v. Musk（S.D.N.Y. No. 1:18-cv-08865；CourtListener docket 7946295）：
- 起诉新闻稿（2018-09-27）：https://www.sec.gov/news/press-release/2018-219
- 起诉书 PDF：https://www.sec.gov/litigation/complaints/2018/comp-pr2018-219.pdf
- 和解新闻稿（2018-09-29，含 Tesla 单独指控）：https://www.sec.gov/news/press-release/2018-226
- 案卷（Final Judgment Dkt.14 / show cause Dkt.19 / 修正判决 Dkt.47 / Liman 裁决 Dkt.81 / mandate Dkt.97）：https://www.courtlistener.com/docket/7946295/united-states-securities-and-exchange-commission-v-musk/
- SEC 函件 2019-02-20（引述 2/19 两条推文全文）：RECAP Dkt. 18-2（storage.courtlistener.com 公开件）
- SEC 藐视动议附件（预审政策 Dkt. 18-1）：RECAP 公开件
- 第二巡回 Summary Order（2023-05-15，No. 22-1291）：Courthouse News 公开件 https://www.courthousenews.com/wp-content/uploads/2023/05/22-1291-SEC-musk-ruling.pdf
- 60 Minutes（2018-12-09）：CBS 片段「I have no respect for the SEC」+ LA Times / Ars Technica / NZ Herald / WaPo 四源印证引语
- 2022 简报引语：Reuters「a deal is a deal」（2022-03-22）+ Boing Boing / Fox Business 转载（两源印证）

## 第 1 轮工作记录（funding secured 案）— complete（2026-09-30）

- **交付**：V8-PROGRESS.md 建立（本文件，含 10 轮状态表/恢复指引/来源留档）；账本 primary.html +7 条（67→74，严格克隆既有 `<li class="ps-row ps-deep reveal">` 结构，四段深读双语）：e2018-09-27 SEC 起诉、e2018-09-29 两天和解（含 10/16 Final Judgment）、e2018-12-09 60 Minutes「I do not respect the SEC」、e2019-02-19 产量推文与藐视动议、e2019-04-30 修正终审判决终结藐视战、e2022-03-08 终结动议与 Liman 驳回、e2023-05-15 第二巡回维持 + Fair Fund 分发；quotes.html 核实卡 +7（54→61）；controversy.html#sec-sec 补法庭弧线入口并把 60 Minutes 引语由「暂作参考记录」转正链接账本；promises.html 第 03 案来源列表补弧线行；index.html 三处计数文案 67→74。
- **采料与核实**：全部条目第一手锚点——SEC 官网新闻稿 2018-219/2018-226 + 起诉书 PDF（comp-pr2018-219.pdf，逐字提取）+ CourtListener 案卷 7946295（Final Judgment/show cause/修正判决/Liman 裁决/mandate 等 12 个节点，docket 文本直接引用）+ RECAP 公开件（SEC 2019-02-20 函件引述两条推文全文、第二巡回 Summary Order 22-1291 全文）+ 60 Minutes 四源印证 + 2022 简报引语 Reuters/Boing Boing/Fox Business 多源印证。案号勘误：正确案号 1:18-cv-08865（任务书里的 08695 有误）。完整 URL 清单见本文件「核实来源留档（R01）」节。
- **管线修复（遗留漂移）**：build-search-index.py 的访谈页 h2 正则在 V7-R17 双语化（h2 加 data-en 属性）后失配——生成器自那之后未再重跑，本轮重跑暴露；已最小修复（`<h2>` → `<h2[^>]*>`），未动页面。断言 言行实录 67→74。
- **验证**：verify.py 9/9 全绿（索引 185 = 74+9+18+13+5+53+4+9；时间轴 74 节点；语录卡 61 vs 引文块 64 豁免 3；EPUB 含最新条目）；node --check app.js cite.js 通过；版本 v7.0.0→v7.1.0（VERSION/app.js/14 页 span），CHANGELOG 首条 v7.1.0，changelog.html/revisions.html/EPUB 重跑。
- **提交**：主成果 `398b249`（25 文件，+449/−231），已推送 main；本回填为第二个提交。
- **范围说明**：本轮按计划只动账本一手体系；编年史行未加（2018.08.07 行已覆盖 SEC 案入口，chronicle 53 断言不动）；新条目暂未挂 ps-linkcard（事件档案归 events-data.py 体系，如需建档卡建议在后续轮统一评估）。
- **下一轮预告**：R02 Twitter 收购案私信原件（特拉华衡平法院 2022 披露件），账本目标 +8~10 条。
