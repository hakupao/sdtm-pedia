# T2 批次表 v1.0

<!-- chain: E (plans) -->
> 生成: `scripts/helpers/t2_pkg.py` (2026-11-26) 读 `work/triage_merged.json` (含 `work/t1_rulings.json`); 只列 ID / 位置 / 计数, 不含 PDF 原文.

> 状态: **v1.0** (2026-11-26, T1.4 裁定落地后). 机器可读: `work/t2_batches/<batch>.json` (含原子清单 / census 引用 / 页码 / 串行约束).
> 规则: 一批 = 一个 KB 单元 (域目录或单个 chapter/model 文件); 例外 B-PCPP = domains/PC + domains/PP (Issue 5, PLAN §6 首批 hard).
> 排序: B-PCPP 第一, 其余按工作量降序. 同文件绝不并行; `串行` 列 = 因 RELOCATE 跨单元必须与之串行的批.

列: 分诊 = REAL_GAP/VALUE_DIFF/RELOCATE 原子 (RG/VD/RL); recheck = R2 待 T2 reviewer 回 PDF 定的 REWRITE_OK; census = DIFF/NO_PDF 表数 / 有 diff 的 KB 行数;
PDF_ONLY = KB 缺整表; PDF_UNPARSED = PDF 侧不可机检 (人工逐格); 不可机检 = KB 侧 UNPARSEABLE 表数 (触碰才人工, G-TB4);
工作量 = 分诊 + census 行 − 重叠 (VALUE_DIFF 落在 census DIFF 表) − 分诊已含 (无 loc 表行落在 PDF_ONLY 页) + PDF_ONLY 行.

## LOCATE §6.3.5.1 (28) 的决定

判据: (1) `ls knowledge_base/domains/` 无 §6.3.5.1 的通用文件 (C11); (2) IG 通用规格节的先例宿主 = 该组代表域的 assumptions.md 顶部 (NV/assumptions.md 承载 §6.3.7 概述 + §6.3.7.1);
(3) §6.3.5.1 名为 'Generic Specimen-based **Lab** Findings', LB 是该组通用实验室域, T1.3 reviewer 已把同节列头 ig34_p0195_a008 定位到 LB/assumptions.md:1 →
**目标 = `domains/LB/assumptions.md` 顶部新增 §6.3.5.1 节**; 28 条 LOCATE 转 REAL_GAP (rule LOCATE-LB), 归 B-LB. NV 先例只有 prose, 本节 21 条是通用规格表行 → 整张通用表一并补.

## 批次

| # | 批 | 单元 | 分诊 (RG/VD/RL) | recheck | census 表/行 | PDF_ONLY | PDF_UNPARSED | 不可机检 | O# | 串行 | 工作量 |
|--:|---|---|---|--:|---|---|---|--:|---|---|--:|
| 1 | B-PCPP | domains/PC, domains/PP | 23 (8/15/0) | 0 | 10/69 | p270 Ex1 pc.xpt (32行); p274 Ex2 None (7行) | p274 pp.xpt | 1 | O1 |  | 109 |
| 2 | B-CP | domains/CP | 52 (38/14/0) | 0 | 2/20 | p211 Ex2 cp.xpt (11行); p213 Ex3 cp.xpt (12行); p214 Ex4 cp.xpt (7行); p215 Ex5 cp.xpt (8行); p216 Ex6 cp.xpt (32行); p218 Ex7 cp.xpt (3行); p219 Ex8 cp.xpt (11行) |  | 0 | O10 |  | 130 |
| 3 | B-LB | domains/LB | 33 (29/4/0) | 0 | 3/6 | p247 Ex1 lb.xpt (18行) |  | 0 |  |  | 53 |
| 4 | B-TR | domains/TR | 19 (0/19/0) | 0 | 2/48 | p358 Ex3 relrec.xpt (2行) |  | 1 |  |  | 50 |
| 5 | B-MB | domains/MB | 12 (8/4/0) | 0 | 11/36 | p263 Ex3 di.xpt (2行); p263 Ex3 relrec.xpt (6行) |  | 0 | O9 |  | 47 |
| 6 | B-ch04 | chapters/ch04_general_assumptions.md | 28 (26/2/0) | 5 | 6/17 |  |  | 33 | O3,O12 |  | 44 |
| 7 | B-DS | domains/DS | 0 (0/0/0) | 0 | 11/37 |  |  | 0 |  |  | 37 |
| 8 | B-EX | domains/EX | 10 (2/8/0) | 0 | 5/32 |  |  | 11 | O10 |  | 35 |
| 9 | B-ch02 | chapters/ch02_fundamentals.md | 31 (31/0/0) | 1 | 0/0 |  |  | 4 |  | B-FA | 31 |
| 10 | B-IS | domains/IS | 14 (1/13/0) | 0 | 8/28 |  |  | 0 | O7 |  | 29 |
| 11 | B-model01 | model/01_concepts_and_terms.md | 26 (26/0/0) | 2 | 0/0 |  |  | 2 |  |  | 26 |
| 12 | B-GF | domains/GF | 3 (1/2/0) | 0 | 4/19 |  |  | 0 |  |  | 20 |
| 13 | B-MS | domains/MS | 0 (0/0/0) | 0 | 2/18 |  |  | 0 |  |  | 18 |
| 14 | B-AE | domains/AE | 5 (2/3/0) | 1 | 6/12 |  |  | 1 | O8,O11 |  | 17 |
| 15 | B-EG | domains/EG | 2 (1/1/0) | 0 | 3/16 |  |  | 0 | O6 |  | 17 |
| 16 | B-TA | domains/TA | 17 (16/1/0) | 0 | 0/0 |  |  | 8 | O4,O10 |  | 17 |
| 17 | B-FA | domains/FA | 8 (1/4/3) | 4 | 3/12 |  |  | 9 | O10 | B-ch02 | 16 |
| 18 | B-OE | domains/OE | 0 (0/0/0) | 0 | 7/12 | p305 Ex4 ae.xpt (3行) |  | 0 |  |  | 15 |
| 19 | B-MH | domains/MH | 0 (0/0/0) | 0 | 5/14 |  |  | 1 |  |  | 14 |
| 20 | B-ch08 | chapters/ch08_relationships.md | 3 (3/0/0) | 0 | 1/11 |  |  | 5 |  |  | 14 |
| 21 | B-SR | domains/SR | 0 (0/0/0) | 0 | 4/13 |  |  | 0 |  |  | 13 |
| 22 | B-TU | domains/TU | 4 (0/4/0) | 0 | 3/11 |  |  | 6 |  |  | 11 |
| 23 | B-ch01 | chapters/ch01_introduction.md | 10 (10/0/0) | 1 | 0/0 |  |  | 3 |  |  | 10 |
| 24 | B-EC | domains/EC | 0 (0/0/0) | 0 | 2/9 |  |  | 1 |  |  | 9 |
| 25 | B-RP | domains/RP | 1 (1/0/0) | 0 | 1/7 |  |  | 0 |  |  | 8 |
| 26 | B-VS | domains/VS | 0 (0/0/0) | 0 | 1/7 |  |  | 0 |  |  | 7 |
| 27 | B-BE | domains/BE | 0 (0/0/0) | 0 | 4/6 |  |  | 0 |  |  | 6 |
| 28 | B-MK | domains/MK | 0 (0/0/0) | 0 | 1/6 |  |  | 0 |  |  | 6 |
| 29 | B-TE | domains/TE | 6 (6/0/0) | 0 | 0/0 | p407 ExNone special.xpt (4行) |  | 1 |  |  | 6 |
| 30 | B-BS | domains/BS | 1 (0/1/0) | 0 | 1/4 |  |  | 0 |  |  | 5 |
| 31 | B-NV | domains/NV | 3 (3/0/0) | 0 | 1/2 |  |  | 0 |  |  | 5 |
| 32 | B-RE | domains/RE | 0 (0/0/0) | 0 | 1/5 |  |  | 0 |  |  | 5 |
| 33 | B-SM | domains/SM | 1 (1/0/0) | 0 | 3/4 |  |  | 0 |  |  | 5 |
| 34 | B-model05 | model/05_study_level_data.md | 5 (5/0/0) | 0 | 0/0 |  |  | 13 |  |  | 5 |
| 35 | B-CV | domains/CV | 1 (1/0/0) | 0 | 1/3 |  |  | 0 |  |  | 4 |
| 36 | B-DM | domains/DM | 1 (1/0/0) | 0 | 2/3 |  |  | 2 |  |  | 4 |
| 37 | B-RS | domains/RS | 0 (0/0/0) | 0 | 1/4 |  |  | 0 |  |  | 4 |
| 38 | B-TS | domains/TS | 1 (1/0/0) | 0 | 2/3 |  |  | 2 |  |  | 4 |
| 39 | B-model06 | model/06_relationship_datasets.md | 3 (3/0/0) | 0 | 0/0 |  |  | 9 |  |  | 3 |
| 40 | B-CE | domains/CE | 1 (1/0/0) | 0 | 1/1 |  |  | 4 | O4,O10 |  | 2 |
| 41 | B-DA | domains/DA | 0 (0/0/0) | 0 | 1/2 |  |  | 0 |  |  | 2 |
| 42 | B-DD | domains/DD | 2 (2/0/0) | 0 | 0/0 |  |  | 0 |  |  | 2 |
| 43 | B-FT | domains/FT | 2 (2/0/0) | 0 | 0/0 |  |  | 0 |  |  | 2 |
| 44 | B-HO | domains/HO | 2 (0/2/0) | 0 | 2/2 |  |  | 0 |  |  | 2 |
| 45 | B-MI | domains/MI | 2 (2/0/0) | 0 | 1/0 |  |  | 0 |  |  | 2 |
| 46 | B-QS | domains/QS | 0 (0/0/0) | 0 | 1/2 |  |  | 0 |  |  | 2 |
| 47 | B-SUPPQUAL | domains/SUPPQUAL | 0 (0/0/0) | 0 | 2/2 |  |  | 0 | O2 |  | 2 |
| 48 | B-CM | domains/CM | 0 (0/0/0) | 0 | 1/1 |  |  | 0 |  |  | 1 |
| 49 | B-CO | domains/CO | 0 (0/0/0) | 0 | 1/1 |  |  | 0 |  |  | 1 |
| 50 | B-DV | domains/DV | 0 (0/0/0) | 0 | 1/1 |  |  | 0 |  |  | 1 |
| 51 | B-IE | domains/IE | 1 (1/0/0) | 0 | 0/0 |  |  | 0 |  |  | 1 |
| 52 | B-ML | domains/ML | 0 (0/0/0) | 1 | 1/1 |  |  | 3 | O4 |  | 1 |
| 53 | B-SU | domains/SU | 1 (1/0/0) | 0 | 0/0 |  |  | 0 |  |  | 1 |
| 54 | B-SV | domains/SV | 0 (0/0/0) | 0 | 1/1 |  |  | 0 |  |  | 1 |
| 55 | B-TI | domains/TI | 1 (1/0/0) | 0 | 0/0 |  |  | 0 |  |  | 1 |
| 56 | B-TV | domains/TV | 1 (1/0/0) | 0 | 0/0 |  |  | 0 |  |  | 1 |
| 57 | B-ch03 | chapters/ch03_submitting_data.md | 1 (0/1/0) | 0 | 0/0 |  |  | 1 | O5 |  | 1 |
| 58 | B-DI | domains/DI | 1 (1/0/0) | 0 | 0/0 |  |  | 0 |  |  | 1 |
| 59 | B-SC | domains/SC | 0 (0/0/0) | 0 | 1/0 |  | p342 sc.xpt | 0 |  |  | 0 |

合计: **59 批**; 分诊原子 338 (= 全部 REAL_GAP+VALUE_DIFF+RELOCATE); recheck 15; census 有 diff 行 508; PDF_ONLY 行 158; 工作量 886.

## 每批明细 (ID / 位置; 完整字段见 JSON)

### 1. B-PCPP
- 原子: ig34_p0270_a012(RE), ig34_p0270_a013(RE), ig34_p0270_a014(RE), ig34_p0270_a023(RE), ig34_p0271_a007(RE), ig34_p0271_a009(RE), ig34_p0271_a010(RE), ig34_p0271_a011(RE), ig34_p0277_a004(VA), ig34_p0277_a005(VA), ig34_p0277_a006(VA), ig34_p0277_a007(VA), ig34_p0277_a008(VA), ig34_p0277_a009(VA), ig34_p0277_a010(VA), ig34_p0277_a011(VA), ig34_p0277_a012(VA), ig34_p0277_a013(VA), ig34_p0277_a014(VA), ig34_p0277_a015(VA), MANUAL_02(VA), ig34_p0277_a003(VA), MANUAL_01(VA)
- census DIFF/NO_PDF 表: domains/PC/assumptions.md:55, domains/PC/assumptions.md:86, domains/PC/examples.md:22, domains/PC/examples.md:36, domains/PC/examples.md:236, domains/PP/examples.md:16, domains/PP/examples.md:47, domains/PP/examples.md:68, domains/PP/examples.md:87, domains/PP/examples.md:112
- 不可机检 (触碰才人工): domains/PP/examples.md:135
- PDF 页: 270, 271, 273, 274, 275, 276, 277, 278, 280
### 2. B-CP
- 原子: ig34_p0208_a023(RE), ig34_p0209_a001(RE), ig34_p0209_a004(RE), ig34_p0209_a005(RE), ig34_p0209_a006(RE), ig34_p0210_a020(RE), ig34_p0210_a022(RE), ig34_p0211_a009(RE), ig34_p0212_a006(RE), ig34_p0212_a010(RE), ig34_p0212_a011(RE), ig34_p0212_a013(RE), ig34_p0212_a014(RE), ig34_p0213_a001(RE), ig34_p0213_a002(RE), ig34_p0213_a003(RE), ig34_p0213_a004(RE), ig34_p0213_a013(RE), ig34_p0214_a001(RE), ig34_p0214_a002(RE), ig34_p0214_a005(RE), ig34_p0214_a008(RE), ig34_p0214_a009(RE), ig34_p0214_a010(RE), ig34_p0214_a011(RE), ig34_p0214_a012(RE), ig34_p0214_a013(RE), ig34_p0214_a014(RE), ig34_p0215_a005(RE), ig34_p0215_a010(RE), ig34_p0215_a013(RE), ig34_p0215_a014(RE), ig34_p0215_a015(RE), ig34_p0215_a017(RE), ig34_p0218_a002(RE), ig34_p0218_a011(RE), ig34_p0219_a002(RE), ig34_p0220_a006(RE), ig34_p0217_a010(VA), ig34_p0210_a002(VA), ig34_p0210_a005(VA), ig34_p0210_a007(VA), ig34_p0210_a009(VA), ig34_p0210_a010(VA), ig34_p0210_a011(VA), ig34_p0210_a012(VA), ig34_p0210_a013(VA), ig34_p0210_a014(VA), ig34_p0210_a015(VA), ig34_p0210_a016(VA), ig34_p0210_a017(VA), ig34_p0210_a018(VA)
- census DIFF/NO_PDF 表: domains/CP/examples.md:31, domains/CP/examples.md:60
- 不可机检 (触碰才人工): —
- PDF 页: 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220
### 3. B-LB
- 原子: ig34_p0194_a022(RE), ig34_p0195_a001(RE), ig34_p0195_a002(RE), ig34_p0195_a003(RE), ig34_p0195_a004(RE), ig34_p0195_a005(RE), ig34_p0195_a006(RE), ig34_p0195_a009(RE), ig34_p0195_a010(RE), ig34_p0195_a011(RE), ig34_p0195_a012(RE), ig34_p0195_a013(RE), ig34_p0195_a014(RE), ig34_p0195_a015(RE), ig34_p0195_a016(RE), ig34_p0195_a017(RE), ig34_p0195_a018(RE), ig34_p0195_a019(RE), ig34_p0195_a021(RE), ig34_p0195_a023(RE), ig34_p0196_a003(RE), ig34_p0196_a004(RE), ig34_p0196_a005(RE), ig34_p0196_a006(RE), ig34_p0196_a007(RE), ig34_p0196_a008(RE), ig34_p0196_a011(RE), ig34_p0196_a013(RE), ig34_p0247_a005(RE), ig34_p0247_a011(VA), ig34_p0247_a020(VA), ig34_p0247_a021(VA), ig34_p0247_a022(VA)
- census DIFF/NO_PDF 表: domains/LB/examples.md:33, domains/LB/examples.md:48, domains/LB/examples.md:63
- 不可机检 (触碰才人工): —
- PDF 页: 194, 195, 196, 247, 248
### 4. B-TR
- 原子: ig34_p0355_a002(VA), ig34_p0355_a009(VA), ig34_p0355_a010(VA), ig34_p0355_a014(VA), ig34_p0355_a015(VA), ig34_p0355_a016(VA), ig34_p0355_a017(VA), ig34_p0355_a018(VA), ig34_p0355_a019(VA), ig34_p0355_a020(VA), ig34_p0355_a021(VA), ig34_p0355_a022(VA), ig34_p0355_a023(VA), ig34_p0355_a024(VA), ig34_p0355_a025(VA), ig34_p0355_a026(VA), ig34_p0355_a027(VA), ig34_p0356_a001(VA), ig34_p0356_a002(VA)
- census DIFF/NO_PDF 表: domains/TR/examples.md:17, domains/TR/examples.md:68
- 不可机检 (触碰才人工): domains/TR/assumptions.md:15
- PDF 页: 355, 356, 357, 358
### 5. B-MB
- 原子: ig34_p0263_a001(RE), ig34_p0263_a004(RE), ig34_p0263_a005(RE), ig34_p0263_a006(RE), ig34_p0263_a009(RE), ig34_p0263_a011(RE), ig34_p0263_a013(RE), ig34_p0263_a014(RE), ig34_p0261_a014(VA), ig34_p0262_a003(VA), ig34_p0260_a009(VA), ig34_p0260_a015(VA)
- census DIFF/NO_PDF 表: domains/MB/examples.md:11, domains/MB/examples.md:33, domains/MB/examples.md:63, domains/MB/examples.md:76, domains/MB/examples.md:98, domains/MB/examples.md:151, domains/MB/examples.md:162, domains/MB/examples.md:212, domains/MB/examples.md:277, domains/MB/examples.md:335, domains/MB/examples.md:388
- 不可机检 (触碰才人工): —
- PDF 页: 256, 257, 258, 260, 261, 262, 263
### 6. B-ch04
- 原子: ig34_p0042_a007(RE), ig34_p0042_a009(RE), ig34_p0042_a013(RE), ig34_p0042_a014(RE), ig34_p0043_a016(RE), ig34_p0043_a018(RE), ig34_p0043_a026(RE), ig34_p0043_a027(RE), ig34_p0043_a028(RE), ig34_p0043_a029(RE), ig34_p0043_a034(RE), ig34_p0044_a001(RE), ig34_p0055_a026(VA), ig34_p0056_a005(VA), ig34_p0056_a006(RE), ig34_p0029_a028(RE), ig34_p0023_a003(RE), ig34_p0041_a036(RE), ig34_p0041_a040(RE), ig34_p0042_a012(RE), ig34_p0043_a022(RE), ig34_p0043_a024(RE), ig34_p0043_a032(RE), ig34_p0044_a005(RE), ig34_p0044_a009(RE), ig34_p0044_a006(RE), ig34_p0045_a005(RE), ig34_p0045_a018(RE)
- t2_recheck: ig34_p0043_a012, ig34_p0043_a013, ig34_p0044_a003, ig34_p0044_a004, ig34_p0044_a008
- census DIFF/NO_PDF 表: chapters/ch04_general_assumptions.md:97, chapters/ch04_general_assumptions.md:121, chapters/ch04_general_assumptions.md:1226, chapters/ch04_general_assumptions.md:1250, chapters/ch04_general_assumptions.md:1321, chapters/ch04_general_assumptions.md:1336
- 不可机检 (触碰才人工): chapters/ch04_general_assumptions.md:43, chapters/ch04_general_assumptions.md:383, chapters/ch04_general_assumptions.md:400, chapters/ch04_general_assumptions.md:433, chapters/ch04_general_assumptions.md:445, chapters/ch04_general_assumptions.md:451, chapters/ch04_general_assumptions.md:457, chapters/ch04_general_assumptions.md:467, chapters/ch04_general_assumptions.md:477, chapters/ch04_general_assumptions.md:536, chapters/ch04_general_assumptions.md:542, chapters/ch04_general_assumptions.md:554, chapters/ch04_general_assumptions.md:560, chapters/ch04_general_assumptions.md:575, chapters/ch04_general_assumptions.md:581, chapters/ch04_general_assumptions.md:662, chapters/ch04_general_assumptions.md:733, chapters/ch04_general_assumptions.md:745, chapters/ch04_general_assumptions.md:754, chapters/ch04_general_assumptions.md:807, chapters/ch04_general_assumptions.md:877, chapters/ch04_general_assumptions.md:896, chapters/ch04_general_assumptions.md:909, chapters/ch04_general_assumptions.md:975, chapters/ch04_general_assumptions.md:998, chapters/ch04_general_assumptions.md:1015, chapters/ch04_general_assumptions.md:1025, chapters/ch04_general_assumptions.md:1052, chapters/ch04_general_assumptions.md:1075, chapters/ch04_general_assumptions.md:1110, chapters/ch04_general_assumptions.md:1359, chapters/ch04_general_assumptions.md:1420, chapters/ch04_general_assumptions.md:1452
- PDF 页: 23, 25, 29, 41, 42, 43, 44, 45, 53, 54, 55, 56
### 7. B-DS
- 原子: —
- census DIFF/NO_PDF 表: domains/DS/examples.md:23, domains/DS/examples.md:101, domains/DS/examples.md:128, domains/DS/examples.md:148, domains/DS/examples.md:202, domains/DS/examples.md:226, domains/DS/examples.md:292, domains/DS/examples.md:317, domains/DS/examples.md:342, domains/DS/examples.md:355, domains/DS/examples.md:381
- 不可机检 (触碰才人工): —
- PDF 页: 159, 161, 162, 163, 165, 166
### 8. B-EX
- 原子: ig34_p0118_a005(RE), ig34_p0118_a006(RE), ig34_p0116_a011(VA), ig34_p0116_a013(VA), ig34_p0116_a015(VA), ig34_p0116_a017(VA), ig34_p0116_a019(VA), ig34_p0116_a021(VA), ig34_p0118_a007(VA), ig34_p0118_a027(VA)
- census DIFF/NO_PDF 表: domains/EX/examples.md:86, domains/EX/examples.md:265, domains/EX/examples.md:296, domains/EX/examples.md:341, domains/EX/examples.md:380
- 不可机检 (触碰才人工): domains/EX/examples.md:13, domains/EX/examples.md:19, domains/EX/examples.md:65, domains/EX/examples.md:173, domains/EX/examples.md:180, domains/EX/examples.md:187, domains/EX/examples.md:241, domains/EX/examples.md:250, domains/EX/examples.md:319, domains/EX/examples.md:395, domains/EX/examples.md:399
- PDF 页: 112, 116, 117, 118, 119
### 9. B-ch02
- 原子: ig34_p0011_a007(RE), ig34_p0011_a023(RE), ig34_p0011_a025(RE), ig34_p0011_a027(RE), ig34_p0012_a004(RE), ig34_p0012_a006(RE), ig34_p0012_a014(RE), ig34_p0013_a008(RE), ig34_p0013_a014(RE), ig34_p0013_a015(RE), ig34_p0013_a016(RE), ig34_p0013_a018(RE), ig34_p0013_a025(RE), ig34_p0014_a006(RE), ig34_p0014_a007(RE), ig34_p0014_a012(RE), ig34_p0014_a003(RE), ig34_p0014_a005(RE), ig34_p0011_a014(RE), ig34_p0011_a016(RE), ig34_p0011_a020(RE), ig34_p0011_a022(RE), ig34_p0011_a029(RE), ig34_p0012_a001(RE), ig34_p0012_a005(RE), ig34_p0012_a008(RE), ig34_p0012_a015(RE), ig34_p0012_a016(RE), ig34_p0012_a018(RE), ig34_p0012_a019(RE), ig34_p0013_a001(RE)
- t2_recheck: ig34_p0011_a017
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): chapters/ch02_fundamentals.md:37, chapters/ch02_fundamentals.md:75, chapters/ch02_fundamentals.md:91, chapters/ch02_fundamentals.md:165
- PDF 页: 11, 12, 13, 14
### 10. B-IS
- 原子: ig34_p0236_a008(VA), ig34_p0236_a009(VA), ig34_p0236_a010(VA), ig34_p0236_a011(VA), ig34_p0236_a012(VA), ig34_p0236_a013(VA), ig34_p0236_a014(VA), ig34_p0236_a015(VA), ig34_p0237_a012(VA), ig34_p0237_a013(VA), ig34_p0237_a014(VA), ig34_p0238_a001(RE), ig34_p0238_a004(VA), ig34_p0239_a002(VA)
- census DIFF/NO_PDF 表: domains/IS/examples.md:40, domains/IS/examples.md:85, domains/IS/examples.md:113, domains/IS/examples.md:141, domains/IS/examples.md:160, domains/IS/examples.md:181, domains/IS/examples.md:218, domains/IS/examples.md:244
- 不可机检 (触碰才人工): —
- PDF 页: 234, 235, 236, 237, 238, 239, 240, 241
### 11. B-model01
- 原子: sv20_p0004_a003(RE), sv20_p0004_a005(RE), sv20_p0004_a007(RE), sv20_p0004_a008(RE), sv20_p0004_a009(RE), sv20_p0004_a011(RE), sv20_p0004_a012(RE), sv20_p0004_a013(RE), sv20_p0004_a015(RE), sv20_p0004_a018(RE), sv20_p0004_a019(RE), sv20_p0004_a020(RE), sv20_p0004_a021(RE), sv20_p0004_a022(RE), sv20_p0004_a023(RE), sv20_p0004_a024(RE), sv20_p0004_a025(RE), sv20_p0005_a002(RE), sv20_p0005_a003(RE), sv20_p0005_a005(RE), sv20_p0005_a008(RE), sv20_p0005_a009(RE), sv20_p0008_a007(RE), sv20_p0008_a009(RE), sv20_p0009_a018(RE), sv20_p0008_a004(RE)
- t2_recheck: sv20_p0009_a016, sv20_p0009_a019
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): model/01_concepts_and_terms.md:61, model/01_concepts_and_terms.md:88
- PDF 页: 4, 5, 8, 9
### 12. B-GF
- 原子: ig34_p0227_a021(RE), ig34_p0225_a004(VA), ig34_p0225_a017(VA)
- census DIFF/NO_PDF 表: domains/GF/examples.md:27, domains/GF/examples.md:60, domains/GF/examples.md:124, domains/GF/examples.md:141
- 不可机检 (触碰才人工): —
- PDF 页: 225, 227
### 13. B-MS
- 原子: —
- census DIFF/NO_PDF 表: domains/MS/examples.md:15, domains/MS/examples.md:39
- 不可机检 (触碰才人工): —
- PDF 页: 257, 259
### 14. B-AE
- 原子: ig34_p0133_a021(RE), ig34_p0141_a007(VA), ig34_p0141_a016(VA), ig34_p0142_a010(RE), ig34_p0142_a012(VA)
- t2_recheck: ig34_p0139_a010
- census DIFF/NO_PDF 表: domains/AE/examples.md:13, domains/AE/examples.md:29, domains/AE/examples.md:43, domains/AE/examples.md:60, domains/AE/examples.md:79, domains/AE/examples.md:94
- 不可机检 (触碰才人工): domains/AE/assumptions.md:37
- PDF 页: 133, 139, 141, 142
### 15. B-EG
- 原子: ig34_p0185_a020(RE), ig34_p0190_a011(VA)
- census DIFF/NO_PDF 表: domains/EG/examples.md:23, domains/EG/examples.md:48, domains/EG/examples.md:101
- 不可机检 (触碰才人工): —
- PDF 页: 185, 190, 192
### 16. B-TA
- 原子: ig34_p0384_a016(RE), ig34_p0387_a012(RE), ig34_p0388_a002(RE), ig34_p0388_a004(RE), ig34_p0389_a002(RE), ig34_p0389_a008(RE), ig34_p0396_a004(RE), ig34_p0397_a006(RE), ig34_p0397_a007(RE), ig34_p0397_a010(RE), ig34_p0397_a015(RE), ig34_p0398_a013(RE), ig34_p0398_a023(RE), ig34_p0398_a024(RE), ig34_p0399_a030(RE), ig34_p0397_a002(VA), ig34_p0398_a014(RE)
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): domains/TA/assumptions.md:31, domains/TA/examples.md:112, domains/TA/examples.md:225, domains/TA/examples.md:336, domains/TA/examples.md:466, domains/TA/examples.md:538, domains/TA/examples.md:608, domains/TA/examples.md:709
- PDF 页: 384, 387, 388, 389, 396, 397, 398, 399
### 17. B-FA
- 原子: ig34_p0373_a012(RE), ig34_p0363_a014(RE), ig34_p0364_a003(RE), ig34_p0370_a009(VA), ig34_p0370_a016(VA), ig34_p0371_a018(VA), ig34_p0373_a024(VA), ig34_p0364_a011(RE)
- t2_recheck: ig34_p0367_a013, ig34_p0367_a016, ig34_p0367_a019, ig34_p0374_a011
- census DIFF/NO_PDF 表: domains/FA/examples.md:101, domains/FA/examples.md:153, domains/FA/examples.md:240
- 不可机检 (触碰才人工): domains/FA/examples.md:7, domains/FA/examples.md:76, domains/FA/examples.md:133, domains/FA/examples.md:138, domains/FA/examples.md:176, domains/FA/examples.md:220, domains/FA/examples.md:264, domains/FA/examples.md:274, domains/FA/examples.md:280
- PDF 页: 363, 364, 367, 370, 371, 373, 374
### 18. B-OE
- 原子: —
- census DIFF/NO_PDF 表: domains/OE/examples.md:12, domains/OE/examples.md:22, domains/OE/examples.md:75, domains/OE/examples.md:98, domains/OE/examples.md:121, domains/OE/examples.md:140, domains/OE/examples.md:151
- 不可机检 (触碰才人工): —
- PDF 页: 302, 303, 304, 305
### 19. B-MH
- 原子: —
- census DIFF/NO_PDF 表: domains/MH/examples.md:13, domains/MH/examples.md:39, domains/MH/examples.md:60, domains/MH/examples.md:83, domains/MH/examples.md:104
- 不可机检 (触碰才人工): domains/MH/assumptions.md:30
- PDF 页: 175, 176, 177, 178
### 20. B-ch08
- 原子: ig34_p0427_a010(RE), ig34_p0427_a018(RE), ig34_p0427_a019(RE)
- census DIFF/NO_PDF 表: chapters/ch08_relationships.md:48
- 不可机检 (触碰才人工): chapters/ch08_relationships.md:88, chapters/ch08_relationships.md:193, chapters/ch08_relationships.md:330, chapters/ch08_relationships.md:354, chapters/ch08_relationships.md:421
- PDF 页: 427, 428
### 21. B-SR
- 原子: —
- census DIFF/NO_PDF 表: domains/SR/examples.md:14, domains/SR/examples.md:64, domains/SR/examples.md:95, domains/SR/examples.md:105
- 不可机检 (触碰才人工): —
- PDF 页: 378, 380
### 22. B-TU
- 原子: ig34_p0353_a015(VA), ig34_p0353_a016(VA), ig34_p0353_a018(VA), ig34_p0354_a005(VA)
- census DIFF/NO_PDF 表: domains/TU/examples.md:19, domains/TU/examples.md:31, domains/TU/examples.md:88
- 不可机检 (触碰才人工): domains/TU/assumptions.md:30, domains/TU/assumptions.md:46, domains/TU/assumptions.md:70, domains/TU/assumptions.md:78, domains/TU/assumptions.md:88, domains/TU/assumptions.md:99
- PDF 页: 353, 354, 356
### 23. B-ch01
- 原子: ig34_p0010_a025(RE), ig34_p0009_a003(RE), ig34_p0009_a004(RE), ig34_p0009_a005(RE), ig34_p0009_a006(RE), ig34_p0009_a023(RE), ig34_p0009_a026(RE), ig34_p0010_a014(RE), ig34_p0010_a016(RE), ig34_p0010_a023(RE)
- t2_recheck: ig34_p0010_a009
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): chapters/ch01_introduction.md:15, chapters/ch01_introduction.md:53, chapters/ch01_introduction.md:80
- PDF 页: 9, 10
### 24. B-EC
- 原子: —
- census DIFF/NO_PDF 表: domains/EC/examples.md:32, domains/EC/examples.md:108
- 不可机检 (触碰才人工): domains/EC/examples.md:84
- PDF 页: 112, 118
### 25. B-RP
- 原子: ig34_p0305_a013(RE)
- census DIFF/NO_PDF 表: domains/RP/examples.md:9
- 不可机检 (触碰才人工): —
- PDF 页: 305, 307
### 26. B-VS
- 原子: —
- census DIFF/NO_PDF 表: domains/VS/examples.md:15
- 不可机检 (触碰才人工): —
- PDF 页: 360, 361
### 27. B-BE
- 原子: —
- census DIFF/NO_PDF 表: domains/BE/examples.md:27, domains/BE/examples.md:39, domains/BE/examples.md:120, domains/BE/examples.md:136
- 不可机检 (触碰才人工): —
- PDF 页: 145, 146, 147
### 28. B-MK
- 原子: —
- census DIFF/NO_PDF 表: domains/MK/examples.md:49
- 不可机检 (触碰才人工): —
- PDF 页: 293, 294
### 29. B-TE
- 原子: ig34_p0403_a011(RE), ig34_p0407_a003(RE), ig34_p0407_a004(RE), ig34_p0407_a005(RE), ig34_p0407_a006(RE), ig34_p0404_a012(RE)
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): domains/TE/examples.md:79
- PDF 页: 403, 404, 407
### 30. B-BS
- 原子: ig34_p0198_a020(VA)
- census DIFF/NO_PDF 表: domains/BS/examples.md:15
- 不可机检 (触碰才人工): —
- PDF 页: 198, 199
### 31. B-NV
- 原子: ig34_p0294_a013(RE), ig34_p0285_a009(RE), ig34_p0285_a010(RE)
- census DIFF/NO_PDF 表: domains/NV/examples.md:15
- 不可机检 (触碰才人工): —
- PDF 页: 285, 294, 296
### 32. B-RE
- 原子: —
- census DIFF/NO_PDF 表: domains/RE/examples.md:15
- 不可机检 (触碰才人工): —
- PDF 页: 311
### 33. B-SM
- 原子: ig34_p0084_a004(RE)
- census DIFF/NO_PDF 表: domains/SM/examples.md:15, domains/SM/examples.md:28, domains/SM/examples.md:37
- 不可机检 (触碰才人工): —
- PDF 页: 84, 85, 86
### 34. B-model05
- 原子: sv20_p0056_a019(RE), sv20_p0056_a020(RE), sv20_p0056_a022(RE), sv20_p0051_a008(RE), sv20_p0051_a013(RE)
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): model/05_study_level_data.md:31, model/05_study_level_data.md:47, model/05_study_level_data.md:66, model/05_study_level_data.md:85, model/05_study_level_data.md:103, model/05_study_level_data.md:122, model/05_study_level_data.md:140, model/05_study_level_data.md:158, model/05_study_level_data.md:172, model/05_study_level_data.md:189, model/05_study_level_data.md:209, model/05_study_level_data.md:254, model/05_study_level_data.md:288
- PDF 页: 51, 56
### 35. B-CV
- 原子: ig34_p0286_a017(RE)
- census DIFF/NO_PDF 表: domains/CV/examples.md:23
- 不可机检 (触碰才人工): —
- PDF 页: 286, 289
### 36. B-DM
- 原子: ig34_p0064_a012(RE)
- census DIFF/NO_PDF 表: domains/DM/examples.md:7, domains/DM/examples.md:411
- 不可机检 (触碰才人工): domains/DM/examples.md:170, domains/DM/examples.md:310
- PDF 页: 64, 68, 78
### 37. B-RS
- 原子: —
- census DIFF/NO_PDF 表: domains/RS/examples.md:57
- 不可机检 (触碰才人工): —
- PDF 页: 336
### 38. B-TS
- 原子: ig34_p0424_a002(RE)
- census DIFF/NO_PDF 表: domains/TS/examples.md:9, domains/TS/examples.md:113
- 不可机检 (触碰才人工): domains/TS/assumptions.md:35, domains/TS/assumptions.md:67
- PDF 页: 420, 421, 422, 423, 424
### 39. B-model06
- 原子: sv20_p0068_a012(RE), sv20_p0068_a019(RE), sv20_p0068_a020(RE)
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): model/06_relationship_datasets.md:29, model/06_relationship_datasets.md:44, model/06_relationship_datasets.md:61, model/06_relationship_datasets.md:89, model/06_relationship_datasets.md:104, model/06_relationship_datasets.md:120, model/06_relationship_datasets.md:135, model/06_relationship_datasets.md:151, model/06_relationship_datasets.md:166
- PDF 页: 68
### 40. B-CE
- 原子: ig34_p0148_a015(RE)
- census DIFF/NO_PDF 表: domains/CE/examples.md:58
- 不可机检 (触碰才人工): domains/CE/assumptions.md:10, domains/CE/examples.md:11, domains/CE/examples.md:41, domains/CE/examples.md:72
- PDF 页: 148, 152
### 41. B-DA
- 原子: —
- census DIFF/NO_PDF 表: domains/DA/examples.md:9
- 不可机检 (触碰才人工): —
- PDF 页: 182
### 42. B-DD
- 原子: ig34_p0183_a003(RE), ig34_p0183_a004(RE)
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): —
- PDF 页: 183
### 43. B-FT
- 原子: ig34_p0318_a017(RE), ig34_p0318_a018(RE)
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): —
- PDF 页: 318
### 44. B-HO
- 原子: ig34_p0169_a0024(VA), ig34_p0171_a0002(VA)
- census DIFF/NO_PDF 表: domains/HO/examples.md:19, domains/HO/examples.md:61
- 不可机检 (触碰才人工): —
- PDF 页: 169, 170, 171
### 45. B-MI
- 原子: ig34_p0263_a030(RE), ig34_p0263_a031(RE)
- census DIFF/NO_PDF 表: domains/MI/examples.md:50
- 不可机检 (触碰才人工): —
- PDF 页: 263, 267
### 46. B-QS
- 原子: —
- census DIFF/NO_PDF 表: domains/QS/examples.md:13
- 不可机检 (触碰才人工): —
- PDF 页: 328, 329
### 47. B-SUPPQUAL
- 原子: —
- census DIFF/NO_PDF 表: domains/SUPPQUAL/examples.md:11, domains/SUPPQUAL/examples.md:22
- 不可机检 (触碰才人工): —
- PDF 页: 433
### 48. B-CM
- 原子: —
- census DIFF/NO_PDF 表: domains/CM/examples.md:36
- 不可机检 (触碰才人工): —
- PDF 页: 102
### 49. B-CO
- 原子: —
- census DIFF/NO_PDF 表: domains/CO/examples.md:23
- 不可机检 (触碰才人工): —
- PDF 页: 62
### 50. B-DV
- 原子: —
- census DIFF/NO_PDF 表: domains/DV/examples.md:15
- 不可机检 (触碰才人工): —
- PDF 页: 179
### 51. B-IE
- 原子: ig34_p0193_a003(RE)
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): —
- PDF 页: 193
### 52. B-ML
- 原子: —
- t2_recheck: ig34_p0121_a005
- census DIFF/NO_PDF 表: domains/ML/examples.md:63
- 不可机检 (触碰才人工): domains/ML/examples.md:14, domains/ML/examples.md:25, domains/ML/examples.md:52
- PDF 页: 121, 124
### 53. B-SU
- 原子: ig34_p0129_a003(RE)
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): —
- PDF 页: 129
### 54. B-SV
- 原子: —
- census DIFF/NO_PDF 表: domains/SV/examples.md:46
- 不可机检 (触碰才人工): —
- PDF 页: 89, 90
### 55. B-TI
- 原子: ig34_p0416_a006(RE)
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): —
- PDF 页: 416
### 56. B-TV
- 原子: ig34_p0407_a020(RE)
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): —
- PDF 页: 407
### 57. B-ch03
- 原子: ig34_p0017_a022(VA)
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): chapters/ch03_submitting_data.md:29
- PDF 页: 17
### 58. B-DI
- 原子: ig34_p0441_a007(RE)
- census DIFF/NO_PDF 表: —
- 不可机检 (触碰才人工): —
- PDF 页: 441
### 59. B-SC
- 原子: —
- census DIFF/NO_PDF 表: domains/SC/examples.md:34
- 不可机检 (触碰才人工): —
- PDF 页: 342

## 待用户
- 批数 59 (一单元一批) 远多于 PLAN §6/§7 的 16-17 批: 每批 3 次 subagent 调用 → ~177 次 (PLAN v1.1 估 48-51). 建议: 工作量 < 10 的小域按 ≤8 目录装箱合批 (PLAN §6 原规则), 需用户定.
- 重复副本 (MB 两份 Ex1-3; p277 PP 表两份): 本表默认两份都修、都不删; 是否去重需用户裁.
- R4-blocked 5 条标题行 + ML 标题行 recheck: 见 `t1_r1_r4_resolution.md` §2.
