# C2R P1 — 预登记判据 (草稿 v0, 2026-09-09)

> 状态: **草稿** — 题面与判分点先于实现写死; S0 闸出结果后微调题面, 实现开始 (I2) 后**不得再改判分点**。
> 目的: 防止事后对症下药 (按 example 修而不是按 pattern 修)。判分由**非本 session 的 Reviewer subagent** 执行 (规则 D)。
> 素材来源: `data/study/st01/catalog.json` 实测 — 77 活动中 15 个带活动级 `visibility_condition=X` (卡片层不可见); 334 个项目的显示条件是「式は別ソース」(卡片只有标志位, 公式不在 ConfigReport 里); 复现命令:
> `python3 -c "import json;d=json.load(open('data/study/st01/catalog.json'));print(sum(1 for a in d['activities'] if a['visibility_condition']), sum(1 for i in d['items'] if i['raw'].get('Visibility::Show on advanced condition') or i['raw'].get('Visibility::Hide on advanced condition')))"`

## 1. 应触发 PDF 旁路的题 (T 组)

| # | 题面 (用户原语) | 卡片层为何答不全 | 判分点 (每点 1 分) |
|---|---|---|---|
| T1 | 帮我看一下st01这个研究的LB这个文件（Form），放的是什么数据，我看更像是采血数据。我看有身高体重这个数据收集，这个两个数据的收集逻辑是不是只登录一次，然后在后续的每个visit都显示，而不是每次采血都测量。 (dogfood 2026-09-09) | 体重/身长的实际采集时点取决于活动级显示 + 画面布局, 卡片只有 非表示アクティビティ 名单 | ① 区分 LBG4 体格测量组 vs LBG6 采血组; ② 每个提到的活动 OID 附日语名; ③ 给出体重实际显示的活动清单并注明来源是画面 p.NN 还是卡片; ④ 对「只录一次」给出有证据的判定 (不是仅推测); ⑤ 三分来源标注 (卡片/标准/画面) |
| T2 | AE フォームの「その他」補足の自由記述項目はどんな条件で表示されますか (題面の実項目名は gitignored 側に保存) | AE 120 项 advanced 条件, 卡片只有「条件あり (式は別ソース)」 | ① 明说卡片无公式; ② 若 PDF 页给出条件, 引用 p.NN 并复述条件; ③ 不编造条件; ④ 附 OID 日语名 |
| T3 | NAC フォームのカペシタビン投与量（某给药量项）はいつ入力画面に出ますか | 同上 (NAC 17 项 advanced) | 同 T2 四点 |
| T4 | 術前化学療法 A 群で、Day1 と Day8 のLB表单は採取項目がどう違いますか | 跨 ≥2 活动 (A群C1-Day1-LB活动 vs A群C1-Day8-LB活动), 需合并多张卡片的隐藏名单 + 画面核对 | ① 列出两活动各自显示的项目集; ② 指出差异项 (体重等); ③ 活动 OID 附日语名; ④ 画面来源标 p.NN |
| T5 | 手術イベントの「术前LB活动名」は常に表示されますか、条件付きですか | 活动级 `visibility_condition=X`, 卡片完全不可见 | ① 明说活动级条件卡片不含; ② PDF 若有条件则引用, 否则诚实说未找到; ③ 不把「常時表示」(项目级) 误读为活动级 |
| T6 | TME フォームの画面で、項目はどう並んでいますか、グループ分けは | 纯画面布局问题, Annotated PDF 才有 | ① 引用 Annotated p.NN; ② 布局描述与项目组 (group) 一致; ③ 不用卡片顺序冒充画面顺序 |

## 2. 不应触发的反例 (N 组, 误触 = FAIL)

| # | 题面 | 为何不触发 |
|---|---|---|
| N1 | VS ドメインの Required 変数を教えて | 纯 cdisc, 无 study 卡片命中 |
| N2 | DM フォームに生年月日の項目はありますか | 单卡片、单活动, 卡片层可完整回答 |
| N3 | 体重 STAT 項 (選択子 `__LB__W`) のコードリストは何ですか | 单卡片字段属性, 卡片完整 |
| N4 | study golden v2 全 48 题 (`eval/` gold) | 现有基线, 逐题 IDENTICAL 为 G2 硬闸 |
| N5 | 偏 CDISC 但含「画面」词的题, 且 `corpus=both` 下只蹭到一张低相似度非直查卡片 (例: SDTM の VS ドメインは画面のどの項目から作りますか) | R3 须有相关性下限 (复审 M10): 至少一张 via_lookup 卡片或 strong_hit, 否则不触发 |

## 3. 触发规则初版 (纯函数, 实现前登记)

命中 study 卡片集合 S 满足任一 → 触发:
- R1: S 中「非表示アクティビティ」并集涉及 ≥2 个不同活动, **且**问题含时点/显示类词 (visit / 時点 / いつ / 表示 / 出る / 每次 / 只录一次 / 显示)
- R2: S 中任一卡片含「条件あり (式は別ソース)」或「非表示条件あり」, 且问题含 条件 / いつ / どんな時 / 显示 / 表示
- R3: 问题含 画面 / レイアウト / 並び / 布局 / 排列, 且 S 非空
反例 N1-N3 在上述规则下必须为 False (实现后用测试钉死)。

**R1 最终词表 (r1 定稿, 与 `server/pdf_trigger.py` 一致)**: visit, 時点, いつ, 表示, 出る, 每次, 只录一次, 显示 (P1 原 8 词) + 違い, 違う, 比較, タイミング, 毎回, 出ます (实现期新增语义类)。代码测试中 N5 对应用例名为 N4。

**修订 r3 (2026-09-09, V3 attempt 1 T6 未触发, 见 `evidence/failures/c2r_v3_attempt_1_T6.md`)**: R3 下限扩为三选一 — via_lookup 卡片 / strong_hit / 问题点名了 study 表单。**r3b 实现口径修正**: 「点名表单」用 `resolve().form_scopes` 判在生产上不成立 (该通道只来自手写别名表, 仅 1 条), 改为对照页索引 `names.forms`: 表单 OID 按 token 边界、表单名按子串 (≥4 字符) 命中问题文本。不碰检索层, 无需 G2 重跑。N5 仍须不触发。判分点不改。

**修订 r2 (2026-09-09, I2 复审 M10)**: R3 增加相关性下限 — 命中集合 S 中至少一张卡片经 study 直查注入 (via_lookup) 或问题 strong_hit; 新增反例 N5。

**修订 r1 (2026-09-09, I2 实现期)**: R1 词表增加一个「差异/比较」语义类 (違い / 違う / 比較 / タイミング / 毎回 / 出ます)。动因: T4 题面无任何时点/显示词, 初版 R1 不触发。**按 pattern 加类, 不按 example 加词** — 刻意不加 T4 自身词汇 (Day8 / 採取項目), 否则 N 组失去判别力。N1-N3 修订后仍不触发 (测试钉死)。判分点 (§1) 未改。

## 4. 规则 A 抽检 N
- T 组 6 题 × 每题至少 2 个模型 = 12 份答案, 全部由 Reviewer 独立判分, 结果落 `evidence/step_c2r_v3_audit.md`。

## 5. 红线说明
本文按 `scripts/oidscan_evidence.py` 红线不写真实 OID/label; 题面真值与卡片选择子存 gitignored `data/study/st01/eval/c2r_pre_registration_realvalues.md` (V3 判分时从该文件取)。
