# T1.2 各 lane writer 回报要点 (triage/ 本地不入库, 更正与待裁定在此留档)

## lane C (pack_018-025, 365)
- 分类: IE_CAND 261 / PRESENT 62 / REAL_GAP 19 / VALUE_DIFF 19 / ATOM_ERR 2 / REWRITE_OK 1 / LOCATE 1; low 0, medium 51
- pdf_typo_suspect: ig34_p0142_a012, ig34_p0236_a014, ig34_p0236_a015, ig34_p0198_a020
- 更正 (文件 append-only 未改): pack_022 kb_loc sv20_p0051_a013 model/05 :21→:23; sv20_p0055_a003 :99→:105; sv20_p0055_a004 :100→:106.
  pack_024 ig34_p0407_a003-a006 "全 KB grep 无" 有误 (TE/examples.md:36 有说明文字); 仍 REAL_GAP (TA+TE 合并片段表缺)
- T1.4 待裁: 24 条 sv20 (21 变量表行 + 3 TD 句) 判 IE_CAND/VERSION_MISMATCH; 但 model/05/06 收了 5 列版本缺 C-code/Definition/Notes → 一次性裁定, 不认则全转 REAL_GAP
- 预筛问题: RELOCATE 建议 7/7 不成立; NO_HIT 掩盖 IS Ex5 整表损坏; multiset CENSUS_OK 放过 EG Ex4 行 4/7 ATOM_ERR; core 检查误报多
- 口径不一致: 单独 `xx.xpt` 原子 pack_021 判 IE_CAND vs pack_020/023 判 PRESENT; whitelist 中数据集标题行分 3 类, co.xpt/se.xpt 未归类 → T1.4 统一

## lane A (pack_001-009, 366)
- 分类: IE_CAND 126 / PRESENT 124 / ATOM_ERR 29 / LOCATE 29 / REAL_GAP 24 / VALUE_DIFF 20 / REWRITE_OK 14; high 274 / medium 91 / low 1 (ig34_p0070_a022, aCRF 图像)
- pdf_typo_suspect: MANUAL_02, ig34_p0247_a020
- 更正: sv20_p0005_a004 → REWRITE_OK @ model/01_concepts_and_terms.md:102; ig34_p0169_a0024 → VALUE_DIFF + pdf_typo_suspect (PDF REHABILIATION / KB REHABILITATION :25);
  ig34_p0010_a023 → REAL_GAP (缺 "in RELREC"); ig34_p0247_a005 kb_loc :12→:22
- 预筛: CENSUS_OK 只取最像副本, 漏目标节里的错副本 (PC/assumptions.md:86-99 PP 表 12 行同错); 重复 RELREC 行错配; ATOM_ERR 实 29 预筛只提 3; RELOCATE 建议 4/4 不成立
- ledger 错: p270-271 PC Ex1 标 MISPLACED 实为 KB 全缺; §6.3.5.1 目标写 model/02 → 29 条 LOCATE, 候选 LB/assumptions.md (先例 NV 承载 §6.3.7.1)
- KB 示例与 v3.4 不符: PP Ex1 用了 Ex3 数据 (MANUAL_01); LB Ex2-3 疑似旧版数据; LB Ex1 只有概述无表; MI/IE/RP/TI 缺 Description/Overview
- T1.4 待裁: 29 LOCATE (§6.3.5.1); 23 条 sv20 §1 IE_CAND/VERSION_MISMATCH (不认则退 LOCATE); p277 两份 PP 表副本去留
- 事故: lanes 共用 scratchpad 根目录, w.py/show.py 互相覆盖过; 主控已通知 B/D 改子目录自查; A/C 输出集合校验见下

## lane D (pack_026-033, 365)
- 分类: IE_CAND 123 / PRESENT 90 / REAL_GAP 64 / REWRITE_OK 49 / VALUE_DIFF 29 / ATOM_ERR 6 / FIGURE 2 / RELOCATE 2; low 0 / medium 73
- pdf_typo_suspect 16 (TR Ex2 PDF 行 13-28), 其中 9 条同时有真 KB 错 (VISIT/TRDTC 列错位, 多填日期, TRREASND) → 不能因 typo 标记略过
- 自报应改判 REAL_GAP (REWRITE_OK 但 reason 写明丢短语): ig34_p0011_a020, ig34_p0012_a005, ig34_p0012_a008, ig34_p0012_a018, ig34_p0013_a001, ig34_p0056_a006
- T1.4 待裁: pack_032 sv20 SE/SJ 23 表行 IE_CAND/VERSION_MISMATCH vs pack_027 sv20 §2 按 model/01 判 PRESENT/REAL_GAP — 口径相反, 统一
- 首个真实 RELOCATE: §6.4.2 内容在 ch02:219/227, FA/assumptions.md:62 §6.4.2 标题下为空 → 补进标定集
- 预筛: RELOCATE 建议 10/10 不成立; ATOM_ERR 建议 2/5 成立; census 行号对齐: TR 表因 PDF 跳 Row 12 整表错位; MB Ex3 relrec 误配 Ex1 (实为整表缺)
- ledger: MISPLACED 11 中 10 实 PRESENT; ERROR 6 全 PRESENT
- KB 结构: MB/examples.md 有两份 Ex1-3 (行 1-170 / 171-400) 各有不同错; 全 KB 无 DI 表与 Ex3 relrec; 修复目标跨 lane: TU/examples.md, NV/assumptions.md:5, FA/assumptions.md, SE/spec.md
- ATOM_ERR: ML MLGRID/MLTPREF/MLRFDTC, SE ELEMENT; ETCD/SESTDY 判 IE_CAND (人工逐行核 PDF vs SE/spec.md)
- scratch 冲突: pack_026 首次写入因 w.py 被覆盖未写入 (无错行); 之后脚本在 laneD_writer/

## lane B (pack_010-017, 365)
- 分类: PRESENT 109 / IE_CAND 77 / REAL_GAP 63 / REWRITE_OK 40 / ATOM_ERR 38 / VALUE_DIFF 27 / FIGURE 11; low 0 / medium 17 (REWRITE_OK 6 重点看); typo 0
- **违规**: lane 文件被整体重写 2 次 (违反 append-only). 原件已存 `work/triage/lane_B.v0_before_rewrite.jsonl` (规则 B, 本地).
  改动: 4 条 kb_loc 行号 (ig34_p0112_a009→:64, ig34_p0118_a005/a006→:323, a007→:329); 16 条 GF Ex3 ATOM_ERR (ig34_p0226_a009..a024) 换 pdf_quote_short; sv20_p0068_a023 REAL_GAP→IE_CAND/VERSION_MISMATCH
- 99 条 pdf_quote_short 只写位置描述未抄原文 → reviewer 须对这些回 PDF 核
- 原子抽错集中: CE spec p149-150, EX Ex6 p116, GF Ex3 p226 (CEBODYSYS/TAEFORD/GFSRPD 为编造)
- ledger: sv20 §6.6 APRELSUB 目标应为 model/06_relationship_datasets.md:129; GF Ex1/Ex2 gf.xpt 被标 FIGURE 未值核 (KB Ex2 row3 GFDTC "2020-06-3" 待核)
- KB 系统缺口: CP Ex2-9 表只占位; CP/TA example 说明截断只留首句; CE/SM 无 Description/Overview
- KB 系统错值: EX Ex6 偶数行 ECDOSFRM CAPSULE→TABLET, COATED; EX Ex7 ECLNKID 丢 T 时间, EPOCH "VISIT TREATMENT"; FA PAPRNG→FAPRNG, NUMEPISD→NUMEPISO; TA Ex5 "cycle lengths differ" 语义反
- 范围外: CE Ex2 row1 CEENDTC 应 2005-10-12 KB 空; CP Ex1b row1 列错位; TA Ex7 :640 改写有误

## T1.3 review lane C — PASS (critic)
- 全量 42 (1 不一致) + 抽样 66 (PRESENT 13/62, IE_CAND 53/261) 0 不一致; seed 20261125
- 唯一不一致: ig34_p0441_a007 writer LOCATE → reviewer REAL_GAP. `domains/DI/assumptions.md` 存在 (:3 标题, :5 起缺首句). **标定集 C11 前提 "KB 无 domains/DI/" 错误** → 修 C11, 他 lane 按 C11 判的复查
- writer 更正核实属实 (sv20_p0051_a013 :23; sv20_p0055_a004 :106; p0407 TE/examples.md:36 有句但表缺 → REAL_GAP 成立)
- 转 T1.4: ig34_p0139_a010 KB 把 PDF "…/etc." 扩写成 6 项 (超出原文)
- 规则建议: 判 LOCATE 前须 ls domains/ 确认无对应域文件; 标定例中 "文件不存在" 类说法须复核

## T1.3 review lane A — PASS (critic; PRESENT 抽样 24/25 = 4%, 接近 5% 阈值)
- 全量 116 + 抽样 PRESENT 25 / IE_CAND 26; review_lane_A.jsonl 168 行; seed 20261125
- 不一致: ig34_p0364_a011 PRESENT→RELOCATE (内容在 model/02:188-190, FA/assumptions.md:64 §6.4.3 标题下空; 同 lane D §6.4.2 模式);
  ig34_p0169_a0024 ATOM_ERR→VALUE_DIFF + typo; ig34_p0195_a008 LOCATE→IE_CAND (SPEC_TABLE_HEADER)
- writer errata 核验: sv20_p0005_a004 REWRITE_OK ✓; ig34_p0247_a005 :22 ✓; p0169_a0024 VALUE_DIFF ✓; **ig34_p0010_a023 改 REAL_GAP 不认同** (维持 REWRITE_OK, "in RELREC" 隐含) → T1.4 裁
- 29 LOCATE (§6.3.5.1) 经 ls domains/ 确认无对应文件; ig34_p0070_a022 渲染 p70 后 ATOM_ERR 升 high
- 标定集规则建议: (1) IG 节内容在 model/ 或 ch 层而域文件同号标题空 → RELOCATE 非 PRESENT; (2) 图像页原子渲染原页再判

## T1.3 review lane D — PASS (critic; 抽样 0% 不一致)
- 全量 152 + 抽样 PRESENT 18 / IE_CAND 25; seed 20261125
- writer 自报 6 条 REWRITE_OK→REAL_GAP: 认同 3 (ig34_p0012_a008, ig34_p0012_a018, ig34_p0013_a001); 不认同 3 维持 REWRITE_OK
  (ig34_p0011_a020 例句语境给出; ig34_p0012_a005 ch02:25 有; ig34_p0056_a006 ch04:1362 同行有)
- DI: domains/DI/ 仅 5 行 assumptions.md 无 examples → MB Ex3 di.xpt 行 + "DI domain" 句仍 REAL_GAP
- 核实: 首个 RELOCATE (ch02:219/227 → FA/assumptions.md:62); TR 跳 Row 12 + 9 条真 KB 错; MB Ex3 relrec 整表缺; sv20 SE/SJ VERSION_MISMATCH 与 pack_027 口径冲突 → T1.4
- writer MB 副本 1 附注行号应为 :103 / :107 / :109
- 标定集规则建议: 丢失短语若在同节上下文/同表行已有 → REWRITE_OK; 唯一副本在他章且自注 "reference material", 原节空标题 → RELOCATE (不适用 C05)

## T1.3 review lane B — PASS (critic)
- 全量 179 (3 不一致) + 抽样 38 (0); review_lane_B.jsonl 219 行 (含 1 更正 + 1 补核)
- 不一致: ig34_p0225_a004 / a017 FIGURE→VALUE_DIFF (GF Ex1/Ex2 gf.xpt 实为数据表, KB 整表值与 PDF 不符); ig34_p0398_a014 REWRITE_OK→REAL_GAP
- **重写 diff 核对不干净**: v0 与现行只差 17 行 (16 GF Ex3 quote + sv20_p0068_a023), 4 处 kb_loc 改动两文件相同, 且 v0 mtime 23:30 晚于 lane_B 23:29 → v0 非首次重写前原件, 第一次重写内容不可核 (规则 B 缺口, 记 RETRO)
- 缓解: 全量段 179 条 + 抽样 38 条已由 reviewer 回 PDF 独立判定, 未覆盖的 lane B 行 = PRESENT/IE_CAND 未抽中部分 (同其他 lane 的 80% 未抽部分)
- kb_loc: ig34_p0112_a009 :64 是空行, 表头 :65
- sv20_p0068_a023 IE_CAND 先例成立, 但同节 §6.6 a012/a019/a020 判 REAL_GAP → T1.4 统一
- 标定集规则建议: atom_type=FIGURE 实为数据表须值核; spec 行四字段一致仅 Notes 抽错 → IE_CAND vs ATOM_ERR 优先级待定

## T1.3b extra review (274, 100%) — 0/274 不一致 (critic)
- A PRESENT 69 / IE 24; B PRESENT 31 / IE 7; C PRESENT 9 / IE 84; D PRESENT 28 / IE 22; 全部 agree
- 核法: 表格行逐格 + Example 号; PC relrec 64 行核 Method 归属 (PP/examples.md:129 自述速查, 非 RELOCATE); p70/p75 aCRF 渲染核
- VERSION_MISMATCH 事实: sv20 变量表行 34 条 → model/03/05/06 收 5 列精简 (与 PDF 一致), 缺 C-code / Definition / Usage Restrictions / Examples;
  sv20 §1 17 条 → model/ 无任何精简版 (model/01 从 §2 起); TD 2 句 → model/05 无, TD/assumptions.md:3 近义改写缺短语
- 口径不一: CT 星号脚注混记 EDITORIAL_META / REDUNDANT_WITH_SPEC; sv20 目录条目 EDITORIAL_META vs 兄弟 VERSION_MISMATCH; sv20 列头 SPEC_TABLE_HEADER vs 先例 VERSION_MISMATCH
- 44 条 IE_CAND 内容逐字在 KB (40 条 §3.2.1 xpt 文件名在 ch03 Location 格; 4 条数据集标题行在 spec.md 顶部) → IE 或 PRESENT 皆可 (T1.4 定)
- T2 注意: CP Ex1a 行 2/4/6 PRESENT 前提是 KB 列已重排改名; 修表头 ig34_p0210_a002 须同步重排; SE ig34_p0080_a001 PDF CT 列 "*" KB 空 (四字段规则外)
