V9-20 R06 逐字源留档（EDGAR 直读 + Newsweek 报道摘要）
================================================================

【一】Tesla Motors Form S-1（2010-01-29，d2010-01-29）
EDGAR 备案号 0001193125-10-017054，primary doc ds1.htm
直读 URL: https://www.sec.gov/Archives/edgar/data/1318605/000119312510017054/ds1.htm
（curl -H "User-Agent: ..." 直读，2026-10-01）

-- 摘录 1（Overview 开篇，逐字）：
"We design, manufacture and sell high-performance fully electric vehicles and advanced electric vehicle powertrain components. We have intentionally departed from the traditional automotive industry model by both exclusively focusing on electric powertrain technology and owning our vehicle sales and service network."

-- 摘录 2（Risk Factors · key employees，逐字）：
"In particular, we are highly dependent on the services of Elon Musk, our Chief Executive Officer, Product Architect and Chairman of our Board of Directors, and JB Straubel, our Chief Technical Officer. None of our key employees is bound by an employment agreement for any specific term."

-- 摘录 3（Overview 数字段，逐字）：
"Since inception through September 30, 2009, we have generated $108.2 million in revenue. As of September 30, 2009, we had an accumulated deficit of $236.4 million and had experienced net losses of $30.0 million for the year ended December 31, 2006, $78.2 million for the year ended December 31, 2007, $82.8 million for the year ended December 31, 2008, and $31.5 million for the nine months ended September 30, 2009."

【二】Tesla Form 10-K FY2021（2022-02-07 备案，d2022-02-07）
EDGAR 备案号 0000950170-22-000796，primary doc tsla-20211231.htm
直读 URL: https://www.sec.gov/Archives/edgar/data/1318605/000095017022000796/tsla-20211231.htm
（curl 直读，2026-10-01）

-- 摘录（Human Capital 风险段，逐字）：
"In particular, we are highly dependent on the services of Elon Musk, Technoking of Tesla and our Chief Executive Officer. None of our key employees is bound by an employment agreement for any specific term and we may not be able to successfully attract and retain senior leadership necessary to grow our business."

核注：Technoking 在全文出现 3 处（风险段 + 签名页等）；FY2021 10-K 中已无
"key person life insurance" 句（检索 NF），旧版句式不可引。

【三】Raptor「破产警报」全员信（2021-11-26，d2021-11-26）
底本（镜像，注明 "reported by Space Explored / Newsweek"）:
https://elonmuskarchive.org/email/spacex-raptor-bankruptcy-2021 （页面存 raptor-page.html）
镜像逐字（含 […] 节略标记）：
"Unfortunately, the Raptor production crisis is much worse than it had seemed a few weeks ago. As we have dug into the issues following the exiting of prior senior management, they have unfortunately turned out to be far more severe than was reported. There is no way to sugarcoat this. […] What it comes down to is that we face a genuine risk of bankruptcy if we can't achieve a Starship flight rate of at least once every two weeks next year."

二源（Newsweek 报道，2021-11-30 前后，经 web reader 通道取回）:
URL: https://www.newsweek.com/elon-musk-responds-leaked-email-warns-spacex-faces-bankruptcy-starship-raptor-1654767
报道含句（逐字，与镜像一致）：
"What it comes down to, is that we face a genuine risk of bankruptcy if we can't achieve a Starship flight rate of at least once every two weeks next year."
"Unfortunately, the Raptor production crisis is much worse than it had seemed a few weeks ago. As we have dug into the issues following the exiting of prior senior management, they have unfortunately turned out to be far more severe than was reported. There is no way to sugarcoat this."
异文口径：Newsweek 版 "What it comes down to, is that"（多一逗号）；镜像版无逗号。站内以镜像为底本，异文已在词条注明。
另：Newsweek 标题即 "Elon Musk Responds to Leaked..."——马斯克本人其后公开回应承认存在破产风险（报道转述口径："If a severe global recession were to dry up capital availability..." 等，未达站内逐字锚标准，词条中以转述口径注明）。

【四】Acronyms Seriously Suck 全员信（2010-05-04，d2010-05-04）
底本（镜像）: https://elonmuskarchive.org/email/spacex-acronyms-seriously-suck-2010 （页面存 acronyms-page.html）
二源（gist 全文转载，逐字一致）:
https://gist.github.com/klaaspieter/12cd68f54bb71a3940eae5cdd4ea1764 （原文存 acronyms-gist.txt）
镜像源标注："Internal SpaceX email (reproduced; also in Ashlee Vance's biography)"
异文口径：gist 版 "I will take drastic action - I have given..."（连字符）；镜像版为 em-dash "—"。站内以镜像为底本。
镜像节略（[…]）段为 "This is particularly tough on new employees."（gist 全文在档）。

【五】镜像 email 库全清单
API: https://elonmuskarchive.org/agents/index?type=email&limit=60&sort=old （存 emails.json，47 封）
采料备注：email 条目 hasTranscript=false，正文在 /email/{id} 详情页；
/agents/transcript/{id} 端点对 email 类型返回 {"error":"Unknown id"}。

（留档时间：2026-10-01，V9-20 R06）
