# T1.4 T2 批次表草案 (draft, 待用户定)

<!-- chain: E (plans) -->
> 状态: 草案 (2026-11-26), T1.4 hard checkpoint 时与用户定稿; 生成: `scripts/helpers/t14_pkg.py`.
> 输入: `work/triage_merged.json` (REAL_GAP/VALUE_DIFF/RELOCATE/LOCATE) + `work/census_full.json` (v2 全量 census) + `work/out_of_scope_findings.md` O1-O12.
> 只列位置与计数, 不含 PDF 原文.

## 1. 按 KB 单元汇总 (单元 = 域目录或单个 chapter/model 文件; 一批 = 一个单元, 同单元串行)

列: 分诊 = REAL_GAP/VALUE_DIFF/RELOCATE/LOCATE 原子数 (无 kb_loc 者按 prefilter `primary_unit`, 再退 pack `kb_owned_files`, 计入 `无loc`);
census = v2 DIFF/NO_PDF 表数 / 有 diff 的 KB 行数 (与落在同表的 VALUE_DIFF 原子去重 = `重叠`); PDF_ONLY = KB 缺整表;
不可机检 = 该单元 UNPARSEABLE 表数 (行数) — 本批触碰到才须 reviewer 人工逐格 (G-TB4);
工作量 = 分诊 + census 行 − 重叠 (VALUE_DIFF 落在 census DIFF 表内) − 分诊已含 (无 kb_loc 的表行/表头原子落在 PDF_ONLY 表页) + PDF_ONLY 行.

| # | 单元 | 分诊 (RG/VD/RL/LC) | 无loc | census 表/行/格 | 重叠 | PDF_ONLY (其中分诊已含) | 不可机检 | O# | 工作量 |
|--:|---|---|--:|---|--:|---|---|---|--:|
| 1 | domains/CP | 52 (38/14/0/0) | 38 | 2/20/62 | 13 | p211 Ex2 cp.xpt (11行); p213 Ex3 cp.xpt (12行); p214 Ex4 cp.xpt (7行); p215 Ex5 cp.xpt (8行); p216 Ex6 cp.xpt (32行); p218 Ex7 cp.xpt (3行); p219 Ex8 cp.xpt (11行) (−13) | 0 (0) | O10 | 130 |
| 2 | domains/PC | 21 (8/13/0/0) | 8 | 5/29/40 | 12 | p270 Ex1 pc.xpt (32行) (−8) | 0 (0) | O1 | 62 |
| 3 | domains/TR | 19 (0/19/0/0) | 0 | 2/48/139 | 19 | p358 Ex3 relrec.xpt (2行) | 1 (1) |  | 50 |
| 4 | domains/MB | 12 (8/4/0/0) | 8 | 11/36/85 | 3 | p263 Ex3 di.xpt (2行); p263 Ex3 relrec.xpt (6行) (−6) | 0 (0) | O9 | 47 |
| 5 | domains/PP | 2 (0/2/0/0) | 0 | 5/40/268 | 2 | p274 Ex2 None (7行) | 1 (4) | O1 | 47 |
| 6 | chapters/ch04_general_assumptions.md | 28 (26/2/0/0) | 12 | 6/17/31 | 1 |  | 33 (142) | O3,O12 | 44 |
| 7 | domains/DS | 0 (0/0/0/0) | 0 | 11/37/51 | 0 |  | 0 (0) |  | 37 |
| 8 | domains/EX | 10 (2/8/0/0) | 2 | 5/32/74 | 7 |  | 11 (44) | O10 | 35 |
| 9 | chapters/ch02_fundamentals.md | 34 (32/0/2/0) | 12 | 0/0/0 | 0 |  | 4 (32) |  | 34 |
| 10 | domains/IS | 14 (1/13/0/0) | 0 | 8/28/87 | 13 |  | 0 (0) | O7 | 29 |
| 11 | model/02_observation_classes.md | 29 (0/0/1/28) | 28 | 0/0/0 | 0 |  | 16 (183) |  | 29 |
| 12 | domains/LB | 5 (1/4/0/0) | 0 | 3/6/114 | 4 | p247 Ex1 lb.xpt (18行) | 0 (0) |  | 25 |
| 13 | domains/GF | 3 (1/2/0/0) | 1 | 4/19/330 | 2 |  | 0 (0) |  | 20 |
| 14 | domains/MS | 0 (0/0/0/0) | 0 | 2/18/67 | 0 |  | 0 (0) |  | 18 |
| 15 | domains/AE | 5 (2/3/0/0) | 1 | 6/12/72 | 0 |  | 1 (1) | O8,O11 | 17 |
| 16 | domains/EG | 2 (1/1/0/0) | 1 | 3/16/65 | 1 |  | 0 (0) | O6 | 17 |
| 17 | domains/TA | 17 (16/1/0/0) | 15 | 0/0/0 | 0 |  | 8 (27) | O4,O10 | 17 |
| 18 | domains/OE | 0 (0/0/0/0) | 0 | 7/12/13 | 0 | p305 Ex4 ae.xpt (3行) | 0 (0) |  | 15 |
| 19 | domains/MH | 0 (0/0/0/0) | 0 | 5/14/22 | 0 |  | 1 (4) |  | 14 |
| 20 | chapters/ch08_relationships.md | 3 (3/0/0/0) | 0 | 1/11/11 | 0 |  | 5 (34) |  | 14 |
| 21 | domains/FA | 5 (1/4/0/0) | 1 | 3/12/13 | 4 |  | 9 (43) | O10 | 13 |
| 22 | domains/SR | 0 (0/0/0/0) | 0 | 4/13/19 | 0 |  | 0 (0) |  | 13 |
| 23 | domains/TU | 4 (0/4/0/0) | 0 | 3/11/12 | 4 |  | 6 (27) |  | 11 |
| 24 | domains/EC | 0 (0/0/0/0) | 0 | 2/9/15 | 0 |  | 1 (5) |  | 9 |
| 25 | chapters/ch01_introduction.md | 9 (9/0/0/0) | 0 | 0/0/0 | 0 |  | 3 (20) |  | 9 |
| 26 | domains/RP | 1 (1/0/0/0) | 1 | 1/7/7 | 0 |  | 0 (0) |  | 8 |
| 27 | domains/VS | 0 (0/0/0/0) | 0 | 1/7/10 | 0 |  | 0 (0) |  | 7 |
| 28 | domains/BE | 0 (0/0/0/0) | 0 | 4/6/8 | 0 |  | 0 (0) |  | 6 |
| 29 | domains/MK | 0 (0/0/0/0) | 0 | 1/6/6 | 0 |  | 0 (0) |  | 6 |
| 30 | domains/TE | 6 (6/0/0/0) | 5 | 0/0/0 | 0 | p407 ExNone special.xpt (4行) (−4) | 1 (3) |  | 6 |
| 31 | domains/BS | 1 (0/1/0/0) | 0 | 1/4/7 | 0 |  | 0 (0) |  | 5 |
| 32 | domains/RE | 0 (0/0/0/0) | 0 | 1/5/5 | 0 |  | 0 (0) |  | 5 |
| 33 | domains/SM | 1 (1/0/0/0) | 1 | 3/4/5 | 0 |  | 0 (0) |  | 5 |
| 34 | domains/CV | 1 (1/0/0/0) | 1 | 1/3/3 | 0 |  | 0 (0) |  | 4 |
| 35 | domains/DM | 1 (1/0/0/0) | 1 | 2/3/10 | 0 |  | 2 (20) |  | 4 |
| 36 | domains/RS | 0 (0/0/0/0) | 0 | 1/4/6 | 0 |  | 0 (0) |  | 4 |
| 37 | domains/TS | 1 (1/0/0/0) | 0 | 2/3/3 | 0 |  | 2 (19) |  | 4 |
| 38 | domains/NV | 1 (1/0/0/0) | 1 | 1/2/4 | 0 |  | 0 (0) |  | 3 |
| 39 | model/04_associated_persons.md | 3 (3/0/0/0) | 3 | 0/0/0 | 0 |  | 1 (4) |  | 3 |
| 40 | domains/CE | 1 (1/0/0/0) | 1 | 1/1/1 | 0 |  | 4 (22) | O4,O10 | 2 |
| 41 | domains/DA | 0 (0/0/0/0) | 0 | 1/2/8 | 0 |  | 0 (0) |  | 2 |
| 42 | domains/HO | 2 (0/2/0/0) | 0 | 2/2/2 | 2 |  | 0 (0) |  | 2 |
| 43 | domains/MI | 2 (2/0/0/0) | 2 | 1/0/0 | 0 |  | 0 (0) |  | 2 |
| 44 | domains/QS | 0 (0/0/0/0) | 0 | 1/2/2 | 0 |  | 0 (0) |  | 2 |
| 45 | domains/SUPPQUAL | 0 (0/0/0/0) | 0 | 2/2/3 | 0 |  | 0 (0) | O2 | 2 |
| 46 | model/05_study_level_data.md | 2 (2/0/0/0) | 0 | 0/0/0 | 0 |  | 13 (110) |  | 2 |
| 47 | domains/DD | 2 (2/0/0/0) | 2 | 0/0/0 | 0 |  | 0 (0) |  | 2 |
| 48 | domains/FT | 2 (2/0/0/0) | 2 | 0/0/0 | 0 |  | 0 (0) |  | 2 |
| 49 | domains/CM | 0 (0/0/0/0) | 0 | 1/1/2 | 0 |  | 0 (0) |  | 1 |
| 50 | domains/CO | 0 (0/0/0/0) | 0 | 1/1/2 | 0 |  | 0 (0) |  | 1 |
| 51 | domains/DV | 0 (0/0/0/0) | 0 | 1/1/1 | 0 |  | 0 (0) |  | 1 |
| 52 | domains/ML | 0 (0/0/0/0) | 0 | 1/1/1 | 0 |  | 3 (9) | O4 | 1 |
| 53 | domains/SV | 0 (0/0/0/0) | 0 | 1/1/1 | 0 |  | 0 (0) |  | 1 |
| 54 | chapters/ch03_submitting_data.md | 1 (0/1/0/0) | 0 | 0/0/0 | 0 |  | 1 (63) | O5 | 1 |
| 55 | model/01_concepts_and_terms.md | 1 (1/0/0/0) | 0 | 0/0/0 | 0 |  | 2 (16) |  | 1 |
| 56 | domains/IE | 1 (1/0/0/0) | 1 | 0/0/0 | 0 |  | 0 (0) |  | 1 |
| 57 | domains/TI | 1 (1/0/0/0) | 1 | 0/0/0 | 0 |  | 0 (0) |  | 1 |
| 58 | domains/TV | 1 (1/0/0/0) | 1 | 0/0/0 | 0 |  | 0 (0) |  | 1 |
| 59 | domains/DI | 1 (1/0/0/0) | 0 | 0/0/0 | 0 |  | 0 (0) |  | 1 |
| 60 | domains/SU | 1 (1/0/0/0) | 1 | 0/0/0 | 0 |  | 0 (0) |  | 1 |

合计: 单元 60; 分诊原子 308; census 有 diff 行 508 (格 1687); 重叠 87; PDF_ONLY 行 158 (其中 31 行已作分诊原子计入, 已扣); 工作量 856.

## 2. 单元内文件分布 (有 kb_loc 的分诊原子 / census DIFF 表所在文件)

- **domains/CP**: domains/CP/examples.md (14)
- **domains/PC**: domains/PC/assumptions.md (12), domains/PC/examples.md (1)
- **domains/TR**: domains/TR/examples.md (19)
- **domains/MB**: domains/MB/examples.md (4)
- **domains/PP**: domains/PP/examples.md (2)
- **chapters/ch04_general_assumptions.md**: chapters/ch04_general_assumptions.md (16)
- **domains/DS**: domains/DS/examples.md (0)
- **domains/EX**: domains/EX/examples.md (8)
- **chapters/ch02_fundamentals.md**: chapters/ch02_fundamentals.md (22)
- **domains/IS**: domains/IS/examples.md (14)
- **model/02_observation_classes.md**: model/02_observation_classes.md (1)
- **domains/LB**: domains/LB/examples.md (5)
- **domains/GF**: domains/GF/examples.md (2)
- **domains/MS**: domains/MS/examples.md (0)
- **domains/AE**: domains/AE/examples.md (4)
- **domains/EG**: domains/EG/examples.md (1)
- **domains/TA**: domains/TA/examples.md (2)
- **domains/OE**: domains/OE/examples.md (0)
- **domains/MH**: domains/MH/examples.md (0)
- **chapters/ch08_relationships.md**: chapters/ch08_relationships.md (3)
- **domains/FA**: domains/FA/examples.md (4)
- **domains/SR**: domains/SR/examples.md (0)
- **domains/TU**: domains/TU/examples.md (4)
- **domains/EC**: domains/EC/examples.md (0)
- **chapters/ch01_introduction.md**: chapters/ch01_introduction.md (9)
- **domains/RP**: domains/RP/examples.md (0)
- **domains/VS**: domains/VS/examples.md (0)
- **domains/BE**: domains/BE/examples.md (0)
- **domains/MK**: domains/MK/examples.md (0)
- **domains/TE**: domains/TE/assumptions.md (1)
- **domains/BS**: domains/BS/examples.md (1)
- **domains/RE**: domains/RE/examples.md (0)
- **domains/SM**: domains/SM/examples.md (0)
- **domains/CV**: domains/CV/examples.md (0)
- **domains/DM**: domains/DM/examples.md (0)
- **domains/RS**: domains/RS/examples.md (0)
- **domains/TS**: domains/TS/assumptions.md (1), domains/TS/examples.md (0)
- **domains/NV**: domains/NV/examples.md (0)
- **domains/CE**: domains/CE/examples.md (0)
- **domains/DA**: domains/DA/examples.md (0)
- **domains/HO**: domains/HO/examples.md (2)
- **domains/MI**: domains/MI/examples.md (0)
- **domains/QS**: domains/QS/examples.md (0)
- **domains/SUPPQUAL**: domains/SUPPQUAL/examples.md (0)
- **model/05_study_level_data.md**: model/05_study_level_data.md (2)
- **domains/CM**: domains/CM/examples.md (0)
- **domains/CO**: domains/CO/examples.md (0)
- **domains/DV**: domains/DV/examples.md (0)
- **domains/ML**: domains/ML/examples.md (0)
- **domains/SV**: domains/SV/examples.md (0)
- **chapters/ch03_submitting_data.md**: chapters/ch03_submitting_data.md (1)
- **model/01_concepts_and_terms.md**: model/01_concepts_and_terms.md (1)
- **domains/DI**: domains/DI/assumptions.md (1)

## 3. 批次草案 (PLAN §6 规则: 一批 = 一个文件或 ≤8 个域目录; 同文件串行; 并行 ≤4) — §3-§5 为手写, 数字对应 2026-11-26 的 §1

| 批 | 单元 | 工作量 | 备注 |
|---|---|--:|---|
| B-PCPP (首批 hard) | domains/PC + domains/PP | 109 | Issue 5 + O1; PC Ex1 整表缺 (p270-271); PP Ex1 用了 Ex3 数据 (MANUAL_01); p274 两表垂直居中须人工逐格 |
| B-CP | domains/CP | 130 | Ex2-8 七张表 KB 只占位 (PDF_ONLY 84 行); Ex1a/1b 列错位 (O10) |
| B-MBMS | domains/MB + domains/MS | 65 | O9 两份 Ex1-3 去重; Ex3 di.xpt / relrec 缺 (DI 无 examples) |
| B-TUTR | domains/TR + domains/TU | 61 | TR Ex2 PDF 跳 Row 12 (行号 diff = PDF_TYPO 候选); Ex3 TRMETHOD/TRNAM 列互换 |
| B-ch04a / B-ch04b | chapters/ch04 | 44 | 串行; O3 / O12; 33 张不可机检表 (触碰才人工) |
| B-ch02 | chapters/ch02 | 34 | 含 RELOCATE 2 (§6.4.2 → FA/assumptions.md:62) |
| B-model | model/02,04,05,01 | 35 | 含 LOCATE 28 (§6.3.5.1), 目标待裁 (候选 LB/assumptions.md, 若改则移入 B-dom) |
| B-ch01/08/03 | 3 文件 | 24 | 一批, 文件间串行 |
| B-dom1..dom6 | 其余 44 个域目录 | 354 | 按工作量装箱 ≤8 目录/批; DS 37 / EX 35 / IS 29 / LB 25 / GF 20 / AE 17 / EG 17 / TA 17 / OE 15 / MH 14 ... |

合计约 **16-17 批** (B-PCPP 1 + CP 1 + MBMS 1 + TUTR 1 + ch04 2 + ch02 1 + model 1 + 杂章 1 + dom 6-7).

## 4. T2 成本重估 vs PLAN §7

分开看两部分: **分诊负载** (T1 分诊出的 REAL_GAP/VALUE_DIFF/RELOCATE/LOCATE) 与 **census 新增负载** (Q9 扩展的全量 census, 分诊阶段看不到).

| 项 | PLAN §7 假设 | 现估 | 偏差 |
|---|---|---|---|
| 分诊负载 | 300-700 原子 | **308** (VERSION_MISMATCH 70 若不认 → 378) | 在区间内 |
| census 新增负载 (净) | 未计 | **548** = census 有 diff 行 508 − 与 VALUE_DIFF 重叠 87 + PDF_ONLY 行 158 − 已作分诊原子计入的整表缺行 31 | 新增 |
| 合计真修量 | 300-700 | **856** (+70 → 926) | 超上限 **+22% ~ +32%** (报警线 700×1.2 = 840) |
| 批数 | 10-14 | 16-17 | +14% ~ +21% |
| subagent 调用 (3/批) | 30-42 | 48-51 (未计失败重跑) | +14% ~ +21% |
| sessions | 3-6 | ~7.3-7.9 (按工作量线性外推 6 × 856/700 ≈ 7.3; +70 时 ≈ 7.9) | +22% ~ +32% |
| 人工逐格 (不可机检表) | 未计 | 全 KB 150 张 / 1,184 行; 只有"本批触碰的表"进 G-TB4 | 新增 |

**报警 (PLAN §7: 超上限 20% → 停下问用户)**: 合计真修量 856 已略过报警线 840, VERSION_MISMATCH 不认时 926; 超出全部来自 census 新增负载.
可选收缩 (T1.4 由用户定):
(a) 全量做 (本表 16-17 批);
(b) T2 只修 Tier B 范围 + 被触碰的表; census 新增且该单元无分诊原子的差异 (19 个单元 145 项: DS 37 / MS 18 / OE 15 / MH 14 / SR 13 ...) 另立后续项目
    (SUPPQUAL 含 O2, 建议保留) → 合计约 711, 回到报警线内;
(c) 先把整表缺 (CP Ex2-8 / PC Ex1 / LB Ex1) 单独一批, 验证 writer 抄整表的质量后再铺开.

## 5. 未决 (T1.4 由用户裁, 本文件不裁)

- VERSION_MISMATCH 口径 (70 条; lane A/C/D 口径不一, 见 `t1_ie_candidates.md`); 不认 → 转 REAL_GAP / LOCATE, 工作量 +70.
- `pending_user` 4 条 (ig34_p0010_a023 / p0011_a020 / p0012_a005 / p0056_a006): REWRITE_OK vs REAL_GAP, 现按 REAL_GAP 计.
- 规则 OPEN: "丢失短语在同节上下文 / 同表行已有 → REWRITE_OK" (`subagent_prompts/t1_calibration_v1.1.md` R-OPEN-1).
- §6.3.5.1 的 28 条 LOCATE 目标文件 (model/02 vs LB/assumptions.md).
- p277 PP 表两份副本 (PP/examples.md:112 与 PC/assumptions.md:86) 去留; MB 两份 Ex1-3 去留 (O9).
- 单独 `xx.xpt` 标题原子口径 (IE_CAND vs PRESENT, lane C).
- 274 条追加复核 (`t1_extra_review_set.json`) 结果未出, 可能改变 IE_CAND / PRESENT 计数.
- census 的 PDF_TYPO 候选 (TR Ex2 行号, OE OCCULAR 等) 须登记 + 用户 ack 才算终态.
