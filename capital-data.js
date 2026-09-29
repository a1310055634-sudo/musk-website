window.CAPITAL_V7 = {
 "plan": "V7-19 R10",
 "meta": {
  "nodes": 12,
  "flows": 18,
  "amounted": 17,
  "span": "1999–2026",
  "currency": "USD"
 },
 "srcNodes": [
  {
   "id": "musk",
   "side": "src",
   "label": {
    "zh": "个人资本",
    "en": "Personal capital"
   },
   "sub": {
    "zh": "Elon Musk",
    "en": "Elon Musk"
   },
   "desc": {
    "zh": "两次退出的套现（Zip2 约 2,200 万、PayPal 税后约 1.8 亿）是他此后再投入的全部本金。",
    "en": "Proceeds from two exits (≈$22M from Zip2, ≈$180M after tax from PayPal) funded everything that followed."
   }
  },
  {
   "id": "vc",
   "side": "src",
   "label": {
    "zh": "风险与产业资本",
    "en": "Venture & strategic capital"
   },
   "sub": {
    "zh": "投资方 · 各轮",
    "en": "Investors · by round"
   },
   "desc": {
    "zh": "2008 圣诞夜联合投资方、2015 Google + Fidelity、2024–2026 xAI 各轮投资方（Valor 领投，英伟达与思科参投）。",
    "en": "The 2008 Christmas Eve syndicate, Google + Fidelity in 2015, and xAI's 2024–26 round investors (Valor-led, with Nvidia and Cisco)."
   }
  },
  {
   "id": "public",
   "side": "src",
   "label": {
    "zh": "公开市场",
    "en": "Public markets"
   },
   "sub": {
    "zh": "IPO",
    "en": "IPO"
   },
   "desc": {
    "zh": "2010.06 Tesla 纳斯达克 IPO——1956 年福特之后首家上市的美国车企。",
    "en": "Tesla's June 2010 Nasdaq IPO — the first US carmaker listing since Ford in 1956."
   }
  },
  {
   "id": "gov",
   "side": "src",
   "label": {
    "zh": "政府",
    "en": "Government"
   },
   "sub": {
    "zh": "合同与贷款",
    "en": "Contracts & loans"
   },
   "desc": {
    "zh": "NASA 是客户（CRS 合同是收入），DOE 是债主（ATVM 贷款已还清）——两种关系都不让渡股权。",
    "en": "NASA is a customer (CRS is revenue) and DOE was a lender (the ATVM loan was repaid) — neither is equity."
   }
  },
  {
   "id": "acq",
   "side": "src",
   "label": {
    "zh": "收购方",
    "en": "Acquirers"
   },
   "sub": {
    "zh": "逐笔标注",
    "en": "labeled per deal"
   },
   "desc": {
    "zh": "康柏、eBay、Tesla、他牵头的财团、xAI——每笔收购的实际出资方在线上逐笔标注。",
    "en": "Compaq, eBay, Tesla, his consortium, xAI — each deal's actual payer is labeled on its line."
   }
  }
 ],
 "coNodes": [
  {
   "id": "zip2",
   "side": "co",
   "label": {
    "zh": "Zip2",
    "en": "Zip2"
   },
   "colorVar": "--co-history",
   "href": "company-files.html#brief-zip2"
  },
  {
   "id": "paypal",
   "side": "co",
   "label": {
    "zh": "X.com / PayPal",
    "en": "X.com / PayPal"
   },
   "colorVar": "--co-paypal",
   "href": "company-files.html#brief-paypal"
  },
  {
   "id": "spacex",
   "side": "co",
   "label": {
    "zh": "SpaceX",
    "en": "SpaceX"
   },
   "colorVar": "--co-spacex",
   "href": "company-files.html#file-spacex"
  },
  {
   "id": "tesla",
   "side": "co",
   "label": {
    "zh": "Tesla",
    "en": "Tesla"
   },
   "colorVar": "--co-tesla",
   "href": "company-files.html#file-tesla"
  },
  {
   "id": "solarcity",
   "side": "co",
   "label": {
    "zh": "SolarCity",
    "en": "SolarCity"
   },
   "colorVar": "--co-solarcity",
   "href": "company-files.html#brief-solarcity"
  },
  {
   "id": "x",
   "side": "co",
   "label": {
    "zh": "X（原 Twitter）",
    "en": "X (ex-Twitter)"
   },
   "colorVar": "--co-x",
   "href": "company-files.html#file-x"
  },
  {
   "id": "xai",
   "side": "co",
   "label": {
    "zh": "xAI",
    "en": "xAI"
   },
   "colorVar": "--co-xai",
   "href": "company-files.html#file-xai"
  }
 ],
 "flows": [
  {
   "id": "zip2-acq",
   "kind": "acquisition",
   "kindLabel": {
    "zh": "收购对价",
    "en": "Acquisition price"
   },
   "group": "mna",
   "from": "acq",
   "fromNote": {
    "zh": "康柏",
    "en": "Compaq"
   },
   "to": "zip2",
   "date": "1999",
   "precision": "year",
   "precisionLabel": {
    "zh": "仅年份",
    "en": "Year only"
   },
   "amount": {
    "zh": "约 3.07 亿美元",
    "en": "≈$307M"
   },
   "currency": "USD",
   "amountUsd": 307000000.0,
   "caliber": {
    "zh": "康柏收购 Zip2 的全部交易对价（非个人套现额）。",
    "en": "Compaq's full purchase price for Zip2 (not his personal take)."
   },
   "sources": [
    {
     "href": "money.html",
     "label": {
      "zh": "资本解剖 · 第一桶金",
      "en": "Capital: the first fortune"
     }
    },
    {
     "href": "profile.html",
     "label": {
      "zh": "速览 · 早期两役",
      "en": "Profile: the early campaigns"
     }
    }
   ],
   "event": null,
   "file": "brief-zip2"
  },
  {
   "id": "zip2-exit",
   "kind": "exit",
   "kindLabel": {
    "zh": "退出套现",
    "en": "Exit proceeds"
   },
   "group": "exit",
   "from": "zip2",
   "fromNote": null,
   "to": "musk",
   "date": "1999",
   "precision": "year",
   "precisionLabel": {
    "zh": "仅年份",
    "en": "Year only"
   },
   "amount": {
    "zh": "约 2,200 万美元",
    "en": "≈$22M"
   },
   "currency": "USD",
   "amountUsd": 22000000.0,
   "caliber": {
    "zh": "个人所得份额（口径：速览/资本解剖在册），非交易总额。",
    "en": "His personal share (per on-file accounts), not the deal total."
   },
   "sources": [
    {
     "href": "profile.html",
     "label": {
      "zh": "速览 · 早期两役",
      "en": "Profile: the early campaigns"
     }
    }
   ],
   "event": null,
   "file": "brief-zip2"
  },
  {
   "id": "pp-acq",
   "kind": "acquisition",
   "kindLabel": {
    "zh": "收购对价",
    "en": "Acquisition price"
   },
   "group": "mna",
   "from": "acq",
   "fromNote": {
    "zh": "eBay",
    "en": "eBay"
   },
   "to": "paypal",
   "date": "2002.10.03",
   "precision": "day",
   "precisionLabel": {
    "zh": "精确到日",
    "en": "Day precision"
   },
   "amount": {
    "zh": "15 亿美元",
    "en": "$1.5B"
   },
   "currency": "USD",
   "amountUsd": 1500000000.0,
   "caliber": {
    "zh": "eBay 收购 PayPal 全部交易对价，2002.10.03 交割。",
    "en": "eBay's full acquisition price for PayPal, closed 2002-10-03."
   },
   "sources": [
    {
     "href": "primary.html#e2002-10-03",
     "label": {
      "zh": "言行账本 e2002-10-03",
      "en": "Ledger e2002-10-03"
     }
    }
   ],
   "event": "e2002-10-03",
   "file": "brief-paypal"
  },
  {
   "id": "pp-exit",
   "kind": "exit",
   "kindLabel": {
    "zh": "退出套现",
    "en": "Exit proceeds"
   },
   "group": "exit",
   "from": "paypal",
   "fromNote": null,
   "to": "musk",
   "date": "2002.10.03",
   "precision": "day",
   "precisionLabel": {
    "zh": "精确到日",
    "en": "Day precision"
   },
   "amount": {
    "zh": "约 1.8 亿美元（税后）",
    "en": "≈$180M after tax"
   },
   "currency": "USD",
   "amountUsd": 180000000.0,
   "caliber": {
    "zh": "本人访谈自述口径（2012–2013，USA Today 等）——税后所得。",
    "en": "His own interview account (2012–13, USA Today etc.) — after-tax proceeds."
   },
   "sources": [
    {
     "href": "primary.html#e2002-10-03",
     "label": {
      "zh": "言行账本 e2002-10-03 · 引语原文",
      "en": "Ledger e2002-10-03 · the quote"
     }
    }
   ],
   "event": "e2002-10-03",
   "file": "brief-paypal"
  },
  {
   "id": "spacex-found",
   "kind": "personal",
   "kindLabel": {
    "zh": "个人投入",
    "en": "Founder capital"
   },
   "group": "personal",
   "from": "musk",
   "fromNote": null,
   "to": "spacex",
   "date": "2002",
   "precision": "year",
   "precisionLabel": {
    "zh": "仅年份",
    "en": "Year only"
   },
   "amount": {
    "zh": "约 1 亿美元",
    "en": "≈$100M"
   },
   "currency": "USD",
   "amountUsd": 100000000.0,
   "caliber": {
    "zh": "本人自述分配口径（与 PayPal 税后所得同一引语）；创立故事细节未入册。",
    "en": "His own account of the split (same quote as the PayPal proceeds); founding-story details not on file."
   },
   "sources": [
    {
     "href": "primary.html#e2002-10-03",
     "label": {
      "zh": "言行账本 e2002-10-03",
      "en": "Ledger e2002-10-03"
     }
    }
   ],
   "event": "e2002-10-03",
   "file": "file-spacex"
  },
  {
   "id": "tesla-found",
   "kind": "personal",
   "kindLabel": {
    "zh": "个人投入",
    "en": "Founder capital"
   },
   "group": "personal",
   "from": "musk",
   "fromNote": null,
   "to": "tesla",
   "date": "2004",
   "precision": "year",
   "precisionLabel": {
    "zh": "仅年份",
    "en": "Year only"
   },
   "amount": {
    "zh": "650 万美元",
    "en": "$6.5M"
   },
   "currency": "USD",
   "amountUsd": 6500000.0,
   "caliber": {
    "zh": "A 轮 750 万中的个人份额，并出任董事长；轮次其余部分不在本图重复画线。",
    "en": "His share of the $7.5M Series A, taking the chair; the rest of the round is not double-drawn here."
   },
   "sources": [
    {
     "href": "company-files.html#file-tesla",
     "label": {
      "zh": "公司档案 · Tesla 里程碑",
      "en": "Company file: Tesla"
     }
    },
    {
     "href": "deep-dive-01.html",
     "label": {
      "zh": "深读 · 资本运作",
      "en": "Deep dive: capital"
     }
    }
   ],
   "event": null,
   "file": "file-tesla"
  },
  {
   "id": "sc-found",
   "kind": "personal",
   "kindLabel": {
    "zh": "个人投入",
    "en": "Founder capital"
   },
   "group": "personal",
   "from": "musk",
   "fromNote": null,
   "to": "solarcity",
   "date": "2006",
   "precision": "year",
   "precisionLabel": {
    "zh": "仅年份",
    "en": "Year only"
   },
   "amount": {
    "zh": "约 1,000 万美元",
    "en": "≈$10M"
   },
   "currency": "USD",
   "amountUsd": 10000000.0,
   "caliber": {
    "zh": "本人自述分配口径；公司由表兄弟按其创意创立、他出任董事长。",
    "en": "His own account of the split; founded by his cousins on his idea, with him as chairman."
   },
   "sources": [
    {
     "href": "primary.html#e2002-10-03",
     "label": {
      "zh": "言行账本 e2002-10-03 · 引语原文",
      "en": "Ledger e2002-10-03 · the quote"
     }
    },
    {
     "href": "events.html#e2006",
     "label": {
      "zh": "事件档案 · SolarCity 创立",
      "en": "Event file: SolarCity founded"
     }
    }
   ],
   "event": "e2006",
   "file": "brief-solarcity"
  },
  {
   "id": "spacex-nasa",
   "kind": "contract",
   "kindLabel": {
    "zh": "政府合同",
    "en": "Gov. contract"
   },
   "group": "gov",
   "from": "gov",
   "fromNote": {
    "zh": "NASA（客户）",
    "en": "NASA (customer)"
   },
   "to": "spacex",
   "date": "2008.12",
   "precision": "month",
   "precisionLabel": {
    "zh": "精确到月",
    "en": "Month precision"
   },
   "amount": {
    "zh": "16 亿美元",
    "en": "$1.6B"
   },
   "currency": "USD",
   "amountUsd": 1600000000.0,
   "caliber": {
    "zh": "CRS 货运服务合同（2008.12.23 授予）——收入性质，非股权融资；与 Tesla 圣诞夜融资背靠背。",
    "en": "The CRS cargo-services contract (awarded 2008-12-23) — revenue, not equity; back-to-back with Tesla's Christmas Eve round."
   },
   "sources": [
    {
     "href": "money.html",
     "label": {
      "zh": "资本解剖 · 外部资本节点",
      "en": "Capital: external money"
     }
    },
    {
     "href": "company-files.html#file-spacex",
     "label": {
      "zh": "公司档案 · SpaceX 里程碑",
      "en": "Company file: SpaceX"
     }
    }
   ],
   "event": null,
   "file": "file-spacex"
  },
  {
   "id": "tesla-xmas",
   "kind": "funding",
   "kindLabel": {
    "zh": "融资",
    "en": "Funding round"
   },
   "group": "funding",
   "from": "vc",
   "fromNote": null,
   "to": "tesla",
   "date": "2008.12.24",
   "precision": "day",
   "precisionLabel": {
    "zh": "精确到日",
    "en": "Day precision"
   },
   "amount": {
    "zh": "金额未入册",
    "en": "Amount not on file"
   },
   "currency": "USD",
   "amountUsd": null,
   "caliber": {
    "zh": "圣诞夜关闭的救命轮次（「可能的最后一天的最后一个小时」）；轮次总额站内未载，线宽不适用——不编造数字。",
    "en": "The Christmas Eve round (“the last hour of the last day”); its size is not on file, so no line width is claimed — no invented number."
   },
   "sources": [
    {
     "href": "primary.html#e2008-12-24",
     "label": {
      "zh": "言行账本 e2008-12-24",
      "en": "Ledger e2008-12-24"
     }
    }
   ],
   "event": "e2008-12-24",
   "file": "file-tesla"
  },
  {
   "id": "tesla-doe",
   "kind": "loan",
   "kindLabel": {
    "zh": "政府贷款",
    "en": "Gov. loan"
   },
   "group": "gov",
   "from": "gov",
   "fromNote": {
    "zh": "DOE（债主）",
    "en": "DOE (lender)"
   },
   "to": "tesla",
   "date": "2010.01",
   "precision": "month",
   "precisionLabel": {
    "zh": "精确到月",
    "en": "Month precision"
   },
   "amount": {
    "zh": "4.65 亿美元",
    "en": "$465M"
   },
   "currency": "USD",
   "amountUsd": 465000000.0,
   "caliber": {
    "zh": "ATVM 贷款：2009.06 有条件批准、2010.01 放款、2013.05.22 提前九年全额还清——债务，非股权。",
    "en": "The ATVM loan: conditionally approved Jun 2009, disbursed Jan 2010, repaid in full nine years early on 2013-05-22 — debt, not equity."
   },
   "sources": [
    {
     "href": "primary.html#e2013-05-22",
     "label": {
      "zh": "言行账本 e2013-05-22 · 还清",
      "en": "Ledger e2013-05-22 · repaid"
     }
    },
    {
     "href": "primary.html#e2009-03-26",
     "label": {
      "zh": "言行账本 e2009-03-26 · 批准",
      "en": "Ledger e2009-03-26 · approval"
     }
    }
   ],
   "event": null,
   "file": "file-tesla"
  },
  {
   "id": "tesla-ipo",
   "kind": "ipo",
   "kindLabel": {
    "zh": "IPO 募资",
    "en": "IPO proceeds"
   },
   "group": "funding",
   "from": "public",
   "fromNote": null,
   "to": "tesla",
   "date": "2010.06",
   "precision": "month",
   "precisionLabel": {
    "zh": "精确到月",
    "en": "Month precision"
   },
   "amount": {
    "zh": "约 2.26 亿美元",
    "en": "≈$226M"
   },
   "currency": "USD",
   "amountUsd": 226000000.0,
   "caliber": {
    "zh": "IPO 募资额（文件口径）；2010.06.29 登陆纳斯达克。",
    "en": "IPO proceeds (filing-based); listed on Nasdaq 2010-06-29."
   },
   "sources": [
    {
     "href": "primary.html#e2010-06-29",
     "label": {
      "zh": "言行账本 e2010-06-29",
      "en": "Ledger e2010-06-29"
     }
    }
   ],
   "event": null,
   "file": "file-tesla"
  },
  {
   "id": "spacex-gf",
   "kind": "funding",
   "kindLabel": {
    "zh": "融资",
    "en": "Funding round"
   },
   "group": "funding",
   "from": "vc",
   "fromNote": {
    "zh": "Google + Fidelity",
    "en": "Google + Fidelity"
   },
   "to": "spacex",
   "date": "2015.01.20",
   "precision": "day",
   "precisionLabel": {
    "zh": "精确到日",
    "en": "Day precision"
   },
   "amount": {
    "zh": "10 亿美元",
    "en": "$1B"
   },
   "currency": "USD",
   "amountUsd": 1000000000.0,
   "caliber": {
    "zh": "联合投资换取不到 10% 股份；对应估值约 100 亿为报道口径——估值不画线。",
    "en": "Joint investment for <10%; the ≈$10B implied valuation is reported — valuations are never drawn."
   },
   "sources": [
    {
     "href": "primary.html#e2015-01-20",
     "label": {
      "zh": "言行账本 e2015-01-20",
      "en": "Ledger e2015-01-20"
     }
    }
   ],
   "event": null,
   "file": "file-spacex"
  },
  {
   "id": "sc-acq",
   "kind": "acquisition",
   "kindLabel": {
    "zh": "收购对价",
    "en": "Acquisition price"
   },
   "group": "mna",
   "from": "acq",
   "fromNote": {
    "zh": "Tesla",
    "en": "Tesla"
   },
   "to": "solarcity",
   "date": "2016.11",
   "precision": "month",
   "precisionLabel": {
    "zh": "精确到月",
    "en": "Month precision"
   },
   "amount": {
    "zh": "约 26 亿美元",
    "en": "≈$2.6B"
   },
   "currency": "USD",
   "amountUsd": 2600000000.0,
   "caliber": {
    "zh": "全股票收购对价；关联交易当年受质疑，2022 年特拉华法院认定「entirely fair」。",
    "en": "All-stock consideration; challenged as related-party then, ruled “entirely fair” by Delaware in 2022."
   },
   "sources": [
    {
     "href": "primary.html#e2016-11",
     "label": {
      "zh": "言行账本 e2016-11",
      "en": "Ledger e2016-11"
     }
    }
   ],
   "event": null,
   "file": "brief-solarcity"
  },
  {
   "id": "tw-acq",
   "kind": "acquisition",
   "kindLabel": {
    "zh": "收购对价",
    "en": "Acquisition price"
   },
   "group": "mna",
   "from": "acq",
   "fromNote": {
    "zh": "他牵头的财团",
    "en": "His consortium"
   },
   "to": "x",
   "date": "2022.10.27",
   "precision": "day",
   "precisionLabel": {
    "zh": "精确到日",
    "en": "Day precision"
   },
   "amount": {
    "zh": "440 亿美元（54.20 美元/股）",
    "en": "$44B ($54.20/share)"
   },
   "currency": "USD",
   "amountUsd": 44000000000.0,
   "caliber": {
    "zh": "要约收购交割对价（2022.10.27）；同期公司另背上约 130 亿美元银行债务（协议条款在册）。",
    "en": "Tender-offer consideration (closed 2022-10-27); the company also took on ≈$13B of bank debt (clauses on file)."
   },
   "sources": [
    {
     "href": "primary.html#e2022-10-28",
     "label": {
      "zh": "言行账本 e2022-10-28 · 交割",
      "en": "Ledger e2022-10-28 · closing"
     }
    },
    {
     "href": "documents.html#d2022-04-25",
     "label": {
      "zh": "一手文档 · 合并协议条款",
      "en": "Document: merger agreement clauses"
     }
    }
   ],
   "event": "e2022-10-28",
   "file": "file-x"
  },
  {
   "id": "xai-b",
   "kind": "funding",
   "kindLabel": {
    "zh": "融资",
    "en": "Funding round"
   },
   "group": "funding",
   "from": "vc",
   "fromNote": null,
   "to": "xai",
   "date": "2024.05",
   "precision": "month",
   "precisionLabel": {
    "zh": "精确到月",
    "en": "Month precision"
   },
   "amount": {
    "zh": "60 亿美元（B 轮）",
    "en": "$6B (Series B)"
   },
   "currency": "USD",
   "amountUsd": 6000000000.0,
   "caliber": {
    "zh": "投后约 240 亿为报道口径（Reuters/CNBC/Forbes）——估值不画线。",
    "en": "≈$24B post-money is reported (Reuters/CNBC/Forbes) — valuations are never drawn."
   },
   "sources": [
    {
     "href": "finance.html#xai",
     "label": {
      "zh": "财务资本全景 · xAI",
      "en": "Finance: xAI"
     }
    }
   ],
   "event": null,
   "file": "file-xai"
  },
  {
   "id": "xai-c",
   "kind": "funding",
   "kindLabel": {
    "zh": "融资",
    "en": "Funding round"
   },
   "group": "funding",
   "from": "vc",
   "fromNote": null,
   "to": "xai",
   "date": "2024.12",
   "precision": "month",
   "precisionLabel": {
    "zh": "精确到月",
    "en": "Month precision"
   },
   "amount": {
    "zh": "60 亿美元（C 轮）",
    "en": "$6B (Series C)"
   },
   "currency": "USD",
   "amountUsd": 6000000000.0,
   "caliber": {
    "zh": "估值约 400 亿为 x.ai 官方公告口径——估值不画线。",
    "en": "≈$40B valuation per x.ai's own announcement — valuations are never drawn."
   },
   "sources": [
    {
     "href": "finance.html#xai",
     "label": {
      "zh": "财务资本全景 · xAI",
      "en": "Finance: xAI"
     }
    }
   ],
   "event": null,
   "file": "file-xai"
  },
  {
   "id": "xai-x",
   "kind": "merger",
   "kindLabel": {
    "zh": "并购对价",
    "en": "Merger price"
   },
   "group": "mna",
   "from": "acq",
   "fromNote": {
    "zh": "xAI",
    "en": "xAI"
   },
   "to": "x",
   "date": "2025.03.28",
   "precision": "day",
   "precisionLabel": {
    "zh": "精确到日",
    "en": "Day precision"
   },
   "amount": {
    "zh": "约 330 亿美元（全股票）",
    "en": "≈$33B (all-stock)"
   },
   "currency": "USD",
   "amountUsd": 33000000000.0,
   "caliber": {
    "zh": "并购对价口径（本人宣布·多方报道转述）：xAI 约 800 亿 / X 约 330 亿（含债约 450 亿）；两家均未上市无市场报价，估值部分不画线。",
    "en": "Deal accounting (his announcement, as reported): xAI ≈$80B / X ≈$33B (≈$45B with debt); neither is listed — valuations are never drawn."
   },
   "sources": [
    {
     "href": "primary.html#e2025-03-28",
     "label": {
      "zh": "言行账本 e2025-03-28 · 推文逐字",
      "en": "Ledger e2025-03-28 · the post verbatim"
     }
    }
   ],
   "event": "e2025-03-28",
   "file": "file-x"
  },
  {
   "id": "xai-e",
   "kind": "funding",
   "kindLabel": {
    "zh": "融资",
    "en": "Funding round"
   },
   "group": "funding",
   "from": "vc",
   "fromNote": null,
   "to": "xai",
   "date": "2026.01",
   "precision": "month",
   "precisionLabel": {
    "zh": "精确到月",
    "en": "Month precision"
   },
   "amount": {
    "zh": "200 亿美元（E 轮）",
    "en": "$20B (Series E)"
   },
   "currency": "USD",
   "amountUsd": 20000000000.0,
   "caliber": {
    "zh": "超募 33%（目标 150 亿）；投后约 2300 亿量级为公告与报道口径——估值不画线。Valor 领投、英伟达与思科参投。",
    "en": "33% oversubscribed ($15B target); ≈$230B post-money is announcement/reporting — valuations are never drawn. Valor-led, Nvidia and Cisco aboard."
   },
   "sources": [
    {
     "href": "documents.html#d2026-01",
     "label": {
      "zh": "一手文档 · Series E 公告全文",
      "en": "Document: the Series E announcement"
     }
    }
   ],
   "event": null,
   "file": "file-xai"
  }
 ],
 "groups": [
  {
   "id": "personal",
   "label": {
    "zh": "个人投入",
    "en": "Founder capital"
   },
   "color": "#C84032",
   "kinds": [
    "personal"
   ],
   "count": 3
  },
  {
   "id": "funding",
   "label": {
    "zh": "融资与 IPO",
    "en": "Funding & IPO"
   },
   "color": "#1f3a5f",
   "kinds": [
    "funding",
    "ipo"
   ],
   "count": 6
  },
  {
   "id": "mna",
   "label": {
    "zh": "收购与并购",
    "en": "Acquisitions & mergers"
   },
   "color": "#55524c",
   "kinds": [
    "acquisition",
    "merger"
   ],
   "count": 5
  },
  {
   "id": "gov",
   "label": {
    "zh": "政府资金",
    "en": "Government money"
   },
   "color": "#8a6d1f",
   "kinds": [
    "contract",
    "loan"
   ],
   "count": 2
  },
  {
   "id": "exit",
   "label": {
    "zh": "退出套现",
    "en": "Exit proceeds"
   },
   "color": "#2E7D4F",
   "kinds": [
    "exit"
   ],
   "count": 2
  }
 ]
};
