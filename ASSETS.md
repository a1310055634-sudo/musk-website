# ASSETS · 图片来源与许可清单

> 本站全部图片来自 Wikimedia Commons，均带可查证的作者与许可。
> 本清单是唯一权威记录：每张图保留「来源页 · 作者 · 许可 · 核实日期 · 加工方式 · 用途」。
> 溯源方法：Commons API 检索 + 缩略图感知哈希比对（tools/trace-assets.py），diff=0 为逐像素一致。
> 新增素材流程：tools/find-assets.py（候选筛选）→ tools/get-files.py（元数据落盘 assets-meta/）→ tools/prep-assets.py（裁切压缩）。

## 现用图片（assets/）

### portrait.jpg — 封面肖像（首页）
- 尺寸/体积：960×1272 · 192KB（灰度背景竖幅）
- 来源：<https://commons.wikimedia.org/wiki/File:Elon_Musk_Royal_Society_(crop2).jpg>
- 作者：Debbie Rowe（2018-07-13 Royal Society 活动）
- 许可：CC BY-SA 3.0（裁切属演绎件，同许可延续）
- 核实：2026-09-29 感知哈希 diff=0（逐像素一致）
- 加工：原站既有裁切（自 1337×1771 原件）
- 用途：其余 29 页 og:image 与页内配图（2026-09-29 起首页封面改用 portrait-hero.jpg）

### tesla-factory.jpg — Tesla 工厂总装线
- 尺寸/体积：960×638 · 133KB
- 来源：<https://commons.wikimedia.org/wiki/File:Tesla_Factory,_Fremont_(CA,_USA)_(8763130149).jpg>
- 作者：Maurizio Pesce（2011-10-01，Fremont 工厂总装线上的 Model S 车身）
- 许可：CC BY 2.0
- 核实：2026-09-29 感知哈希 diff=0（逐像素一致）
- 加工：原站既有缩放（自 3008×2000 原件）
- 用途：indepth.html Tesla 档案配图；index.html 首页业务横带（TESLA · 弗里蒙特总装线）

### falcon-heavy.jpg — Falcon Heavy 双助推器同步着陆（2026-09-29 替换）
- 尺寸/体积：960×1440 · 113KB
- 来源：<https://commons.wikimedia.org/wiki/File:Falcon_Heavy_Demo_Mission_(39337245575).jpg>
- 作者：SpaceX（2018-02-06 演示飞行）
- 许可：CC0（公有领域贡献）
- 核实：Commons 元数据直接采信（SpaceX 官方账号上传，Flickr 源 39337245575）
- 加工：原图 2000×3000 → 960×1440 缩放；页面 21:9 框内 object-position 底部取景
- 替换说明：旧图（远景升空）经两轮检索无法在 Commons 定位到确切文件（最佳候选 diff≥211，非同一图），来源不可追查——按本轮「来源可追查」标准整体替换为同题材（Falcon Heavy 演示飞行 2018）可溯源官方图；页面标题/alt 同步改为「两侧助推器同步着陆」以匹配新画面内容
- 用途：indepth.html SpaceX 档案配图；index.html 首页业务横带（SPACEX · 双助推同步着陆，object-position 74% 取着陆瞬间）

### starship-catch.jpg — Starship 助推器塔捕（新增）
- 尺寸/体积：1200×1345 · 127KB
- 来源：<https://commons.wikimedia.org/wiki/File:Starship_Booster_Landing_on_Mechzilla_(54064036815).jpg>
- 作者：Steve Jurvetson（2024-10-13，Starship 第五飞助推器被发射塔「Mechzilla」机械臂接住）
- 许可：CC BY 2.0
- 核实：Commons 元数据；描述原文「The booster being caught during Starship flight test 5」与本站账本 e2024-10-13 锚点互证
- 加工：缩放至 1200px 宽，质量 80
- 用途：companies.html SpaceX 卡片；index.html 首页业务横带（SPACEX · 星舰塔捕）

### x-hq.jpg — Twitter/X 总部（新增）
- 尺寸/体积：1200×800 · 196KB
- 来源：<https://commons.wikimedia.org/wiki/File:TwitterHeadquarters2022.jpg>
- 作者：osunpokeh（2022-11-04，旧金山 Market 街视角，@twitter 标牌）
- 许可：CC BY-SA 4.0（裁切属演绎件，同许可延续）
- 核实：Commons 元数据；拍摄时点即收购交割后一周（收购 2022-10-27 完成），画面仍为 Twitter 标牌
- 加工：正方形原件上部 3:2 裁切（保住 @twitter 标牌与楼体），缩放至 1200px 宽
- 用途：companies.html X 卡片；index.html 首页业务横带（X · Twitter 总部）

### cybertruck.jpg — Cybertruck 展车（新增）
- 尺寸/体积：1080×720 · 102KB
- 来源：<https://commons.wikimedia.org/wiki/File:2023_production-level_Tesla_Cybertruck_on_display_in_Denver,_Colorado.jpg>
- 作者：N2e（2023-11-29，Denver 展厅量产版 Cybertruck 右前视）
- 许可：CC0（公有领域贡献）
- 核实：Commons 元数据
- 加工：16:9 原件 3:2 裁切（对准车头），缩放至 1080px 宽
- 用途：companies.html Tesla 卡片

### portrait-hero.jpg / portrait-hero-mobile.jpg — 封面备用裁切（第 3 轮启用）
- 尺寸/体积：960×640 · 79KB ／ 960×1200 · 166KB
- 来源：自 portrait.jpg（见上，CC BY-SA 3.0）派生
- 加工：3:2 横版（面部居中）与 4:5 竖版两档
- 用途：2026-09-29（R3）起为首页封面主图——桌面 3:2 / ≤640px 经 <picture> 自动换 4:5；含 figcaption 署名行；首页 og:image 亦指向 3:2 版

## 署名落点（许可合规）

- 图片所在页面均带 figcaption 署名（作者 · 许可 · via Wikimedia Commons）；首页封面肖像的署名在其 figcaption，页脚免责声明另有「图片来自 Wikimedia Commons」总说明。
- CC BY / CC BY-SA 要求的署名与许可声明以上述 figcaption + 本清单满足；CC0 无强制署名要求，仍统一标注。
- 本站为非官方学习型站点，与马斯克先生及其公司无隶属关系。

## 备选未采用（assets-meta/ 留档，未入库）

- `2024 Tesla Cybertruck, Moab`（A1C6 · CC0）——车尾视角，弱于展厅正脸
- `Quo vadis, Twitter?-L1001307`（Frank Schulenburg · CC BY-SA 4.0）——前景交通标志抢夺主体
