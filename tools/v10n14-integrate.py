# -*- coding: utf-8 -*-
"""V10-15 N14：events-data.py 追加 2 个新档案（OpenAI 弧线 / xAI 线）——全部由已入册材料聚合。"""
import io

p = 'tools/events-data.py'
s = io.open(p, encoding='utf-8').read()
# 插入点：EVENTS 列表收尾（最后一个档案对象之后）
assert '"id": "e2019-04-22"' in s
i = s.rfind('    },\n]')
assert i > 0

addition = '''    },
    # ------------------------------------------------ 2015-2026 OpenAI 创立与出走弧线
    {
        "id": "e2015-11-22",
        "date": "2015.11.22",
        "precision": "day",
        "etype": "risk",
        "companies": ["xAI"],
        "title": {"zh": "OpenAI：从「10 亿承诺」到「最后一根稻草」",
                  "en": "OpenAI: from the \\"$1B commitment\\" to \\"the final straw\\""},
        "summary": {
            "zh": "创立承诺、控制权之争、停止资助——六年间三封邮件画出马斯克与 OpenAI 从共同创立到对簿公堂的完整弧线。",
            "en": "Founding promise, control fight, funding cutoff — three emails across six years trace the full arc from co-founding OpenAI to suing it.",
        },
        "background": {
            "zh": "2015 年底 OpenAI 创立时，马斯克为对冲谷歌 DeepMind 主导 AI 的前景，推动对外宣布 10 亿美元资助承诺并承诺兜底差额。2017 年营利化谈判中他要求初始控制权未果；9 月 21 日发出「最后一根稻草」邮件宣布停止资助；2018 年 2 月退出董事会。2024 年他以「背叛非营利使命」起诉 OpenAI，OpenAI 则公开这批邮件反证其当年主张营利化与控制权。",
            "en": "At OpenAI's founding in late 2015, Musk pushed a $1B public funding commitment (backstopping the difference) to counter Google DeepMind. In 2017 for-profit talks he demanded initial control; on Sept 21 he sent the \\"final straw\\" email cutting funding, and left the board in Feb 2018. In 2024 he sued OpenAI for betraying the nonprofit mission; OpenAI published the emails as rebuttal.",
        },
        "facts": [
            {"zh": "2015.11.22 邮件：宣布口径应为「以 10 亿美元资助承诺起步」，差额由马斯克补齐；比 1 亿大以免「相对谷歌/FB 听起来毫无希望」。",
             "en": "2015-11-22 email: announce starting with a $1B funding commitment, Musk covering the gap — bigger than $100M to avoid sounding hopeless next to Google/Facebook."},
            {"zh": "2017.09.13 邮件：马斯克要求「毫无保留的初始控制权」与董事会任命权，称这会很快改变。",
             "en": "2017-09-13 email: Musk demands unequivocal initial control and board appointment rights, saying this would change quickly."},
            {"zh": "2017.09.21 邮件（Honest Thoughts 九分钟后）：「这是最后一根稻草」——停止资助直至结构承诺；马斯克 2018 年 2 月退出董事会。",
             "en": "2017-09-21 email (nine minutes after Honest Thoughts): \\"the final straw\\" — funding stops pending a structure commitment; Musk leaves the board Feb 2018."},
            {"zh": "2024 年马斯克起诉；OpenAI 公开邮件反证；2026 年联邦法院判决在案（FindLaw 引 2017 邮件）。",
             "en": "Musk sues in 2024; OpenAI publishes the emails in rebuttal; a 2026 federal ruling cites the 2017 email (on FindLaw)."},
        ],
        "quotes": [
            {"en": "I think we should say that we are starting with a $1B funding commitment. This is real. I will cover whatever anyone else doesn’t provide.",
             "zh": "我认为我们应该对外宣布：我们是以 10 亿美元的资助承诺起步的。这是真的。别人没出的部分我来补齐。",
             "src": "2015.11.22 致 Brockman 邮件（d2015-11-22）"},
            {"en": "I would unequivocally have initial control of the company, but this will change quickly.",
             "zh": "我会毫无保留地拥有公司的初始控制权，但这会很快改变。",
             "src": "2017.09.13 邮件（d2017-09-13）"},
            {"en": "This is the final straw. Either go do something on your own or continue with OpenAI as a nonprofit. I will no longer fund OpenAI.",
             "zh": "这是最后一根稻草。要么你们自己单干，要么继续把 OpenAI 当非营利组织做下去。我不会再资助 OpenAI。",
             "src": "2017.09.21 邮件（d2017-09-21）"},
        ],
        "materials": [
            {"kind": "document", "href": "documents.html#d2015-11-22", "date": "2015.11.22",
             "label": {"zh": "文档 · $1B 承诺邮件（2015.11.22）", "en": "Document · the $1B commitment email"},
             "note": {"zh": "创立承诺的原文（诉讼证物）", "en": "The founding-promise text (litigation evidence)"}},
            {"kind": "document", "href": "documents.html#d2017-09-13", "date": "2017.09.13",
             "label": {"zh": "文档 · 控制权邮件（2017.09.13）", "en": "Document · the control-terms email"},
             "note": {"zh": "营利化谈判中的控制权条款", "en": "Control terms in the for-profit talks"}},
            {"kind": "document", "href": "documents.html#d2017-09-21", "date": "2017.09.21",
             "label": {"zh": "文档 · 最后一根稻草邮件（2017.09.21）", "en": "Document · the final-straw email"},
             "note": {"zh": "停止资助与结构最后通牒", "en": "The funding cutoff and structure ultimatum"}},
            {"kind": "feature", "href": "ai-strategy.html", "date": None,
             "label": {"zh": "专题 · AI 战略（OpenAI 弧线的叙事层）", "en": "Feature · AI strategy (the narrative layer of the OpenAI arc)"},
             "note": {"zh": "弧线的解读与后续", "en": "The reading and the aftermath"}},
        ],
        "related": [
            {"href": "#e2026-02-10", "label": {"zh": "2026.02.10 · xAI All-Hands", "en": "2026-02-10 · xAI All-Hands"}},
        ],
        "no_quote_note": None,
        "outcome": {
            "zh": "弧线的终点尚未封笔：2024 年诉讼互诉、2026 年判决继续上诉程序中。三封邮件作为法庭证物与公开文件，把「谁先背离使命」的问题变成了可逐字对账的文本史。（末句为编者分析，非其原话。）",
            "en": "The arc has no final period yet: dueling 2024 lawsuits, a 2026 ruling under appeal. The three emails — as court exhibits and public files — turned \\"who betrayed the mission first\\" into a text history you can check word by word. (Last sentence is editorial analysis, not his words.)",
        },
    },
    # ------------------------------------------------ 2023-2026 xAI 线：成立到银河百科
    {
        "id": "e2026-02-10",
        "date": "2026.02.10",
        "precision": "day",
        "etype": "milestone",
        "companies": ["xAI"],
        "title": {"zh": "xAI All-Hands：两岁半的「幼儿」开出第一张成绩单",
                  "en": "xAI All-Hands: the two-and-a-half-year-old toddler files its first report card"},
        "summary": {
            "zh": "对标成立五到二十年的对手，他给出 xAI 的第一份全景成绩单：语音/图像/视频生成第一、Grokkipedia 对标维基百科、10 万张 H100 集群——并把「银河百科」设为下一章。",
            "en": "Measuring xAI against rivals five to twenty years older, he files the first full report card: #1 in voice, image and video generation; Grokipedia beyond Wikipedia; a 100,000-H100 cluster — with the \\"Encyclopedia Galactica\\" as the next chapter.",
        },
        "background": {
            "zh": "xAI 于 2023 年 7 月成立、11 月发布 Grok；2026 年 2 月 10 日首届 All-Hands 上，马斯克以「两岁半的幼儿」自况，全面盘点与老牌对手的差距与反超点。",
            "en": "xAI was founded in July 2023 and shipped Grok that November. At the first All-Hands on Feb 10, 2026, Musk — calling xAI \\"a toddler\\" — sized it against legacy rivals on both gaps and leads.",
        },
        "facts": [
            {"zh": "自评：语音、图像与视频生成第一；图像与视频生成量「超过所有对手之和」。",
             "en": "Self-assessment: #1 in voice, image and video generation; generating more images and video than all competitors combined."},
            {"zh": "Grok 420 预测模型在预测基准上击败其他 AI；Grokkipedia 定位为超越维基百科的「银河百科全书」。",
             "en": "Grok 420 forecasting beats other AIs on forecasting; Grokipedia is positioned as Encyclopedia Galactica beyond Wikipedia."},
            {"zh": "首个 10 万张 H100 训练集群；愿景宣言延续到 3 月的 Terafab 芯片厂发布（三公司合力）。",
             "en": "First 100,000-H100 training cluster; the vision carried into March's Terafab fab announcement (a three-company effort)."},
        ],
        "quotes": [
            {"en": "xAI is only two and a half years old, basically a toddler, and we’ve nonetheless achieved number one in many arenas — in voice, in image and video generation. Grokipedia is intended ultimately to be Encyclopedia Galactica, a distillation of all knowledge.",
             "zh": "xAI 才两岁半，基本是个幼儿，但我们已经在很多领域做到了第一——语音、图像与视频生成。Grokkipedia 的终极目标是成为「银河百科全书」——一切知识的蒸馏。",
             "src": "2026.02.10 xAI All-Hands（e2026-02-10）"},
        ],
        "materials": [
            {"kind": "ledger", "href": "primary.html#e2026-02-10", "date": "2026.02.10",
             "label": {"zh": "言行账本 e2026-02-10 · All-Hands 成绩单", "en": "Ledger e2026-02-10 · the All-Hands report card"},
             "note": {"zh": "一手言行记录", "en": "First-hand record"}},
            {"kind": "ledger", "href": "primary.html#e2026-03-21", "date": "2026.03.21",
             "label": {"zh": "言行账本 e2026-03-21 · Terafab 发布", "en": "Ledger e2026-03-21 · the Terafab announcement"},
             "note": {"zh": "同一叙事的下一章", "en": "The next chapter of the same narrative"}},
            {"kind": "post", "href": "x-posts.html#p2023-11-04", "date": "2023.11.04",
             "label": {"zh": "X 帖史收录 · Grok 发布期发言", "en": "X posts archive · Grok launch-era remarks"},
             "note": {"zh": "Grok 起点的第一手记录", "en": "First-hand record of Grok's origin"}},
            {"kind": "feature", "href": "grok.html", "date": None,
             "label": {"zh": "专题 · xAI 与 Grok", "en": "Feature · xAI and Grok"},
             "note": {"zh": "Grok 线的完整梳理", "en": "The full Grok thread"}},
        ],
        "related": [
            {"href": "#e2015-11-22", "label": {"zh": "2015-2026 · OpenAI 创立与出走弧线", "en": "2015-2026 · the OpenAI arc"}},
        ],
        "no_quote_note": None,
        "outcome": {
            "zh": "成绩单的真实性交给市场检验：预测基准、生成量与 Grokipedia 的覆盖度都是可核指标——这正是 xAI 自己选的记账方式。（末句为编者分析，非其原话。）",
            "en": "The report card is left to the market: forecasting benchmarks, generation volume and Grokipedia's coverage are all checkable — exactly the bookkeeping xAI itself chose. (Last sentence is editorial analysis, not his words.)",
        },
    },
]'''
s = s[:i] + addition + s[i + len('    },\n]'):]
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('2 new event files appended')
