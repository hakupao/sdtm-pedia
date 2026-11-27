# T4.1 第二轮补检 — PDF_TYPO 层 结果 (包 6, R91-R115)

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:39:37Z (`date -u`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` (背景 / 判定口径) + `subagent_prompts/t4/t4_supp_round2_v1.0.md` § PDF_TYPO (冲突以后者为准)
- 样本包: `.work/10_tier_b_repair/work/t4/round2/round2_pack_6.md`; 登记: `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` (28 个 id 全部按 `id` 查到)
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`): p18 (整页, FT Keys 格), p213 (整页, CP Ex3 表), p236 (整页, IS Ex5 表), p280 (400dpi 裁切, `DYIDRGX` 的 I / 1 字形 + 同页 relrec 表), p205 / p199 / p26 / p85 (300dpi 裁切, `CPSCMRKS` / `--BNDAGT` `--GATEDEF` / `VISTNUM` / `SMDY` 字形)
- 用过的命令 (临时文件在 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/r2_p1/`):
  - 登记查询: `python3` 逐 id 读 `t2_pdf_typo_registry.jsonl`
  - 渲染: `pdftoppm -r 110|300|400 -f N -l N [-x -y -W -H] -png "<PDF>" ...`; 定位: `pdftotext -bbox -f N -l N`
  - 散文类 (R92/93/96/97/101-103/105-111/113-115): `scratchpad/r2_p1/cmp.py` — 取 PDF 文本层对应行, 仅套用登记的改正替换, 归一 (粗体 / 列表符 / 空白 / 弯直引号 / 换行连字符) 后判断是否为 KB 行的子串; 17 条全部命中 (R105/R106 差异仅为 PDF 项目符号 "•")
  - 表格类 (R91/94/95/98/99/100/104/112): 渲染页或文本层表头 + 行逐格对 KB 表头 + 行
  - 残留扫描: `grep -rnwE "VISTNUM|occurrs|BIRTHDTC|WHTE|rations|CPSCMRKS|MonoSub|RSC1230|LBSTRNHI|--STRNC|aorta-iliac|reactogencity|TDTGPAI|DIZOGOTIC|SMDY|BNDAGT|GATEDEF|CPGATEDEF|nucleoar|MBREFID|RSPLNKGRP|DYIDRGX_A|DYIDRGX_HALF" knowledge_base/` (MBREFID 命中均为 MB 域合法变量; `GATEDEF` 仅 CP/examples.md:171, 对应 PDF p214 原文同写 "GATE and GATEDEF", 非样本)

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| R91 | `ig34_p0018_a036` | PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p18 FT 行 Keys 格 "STUDYID, USUBJID, TESTCD, VISITNUM, FTTPTREF, FTTPTNUM"; `knowledge_base/chapters/ch03_submitting_data.md:49` | 登记 B-ch03 T-2. ① PDF 确为 TESTCD (同表其余行均 <XX>TESTCD); ② KB=FTTESTCD; ③ 其余 6 格 (FT / Functional Tests / Findings / Structure / Tabulation / ft.xpt) 逐格一致 |
| R92 | `ig34_p0026_a037` | PDF_TYPO | PDF_TYPO | HOLDS | p26 文本层:55 + 300dpi 裁切; `chapters/ch04_general_assumptions.md:200` | 登记 B-ch04 T-7. 渲染确为 "VISTNUM"; KB=VISITNUM; 其余逐字一致 |
| R93 | `ig34_p0049_a008` | PDF_TYPO | PDF_TYPO | HOLDS | p49:11-12; `chapters/ch04_general_assumptions.md:1195` | 登记 B-ch04 T-4. PDF "occurrs"; KB "occurs"; 原子句其余逐字一致 |
| R94 | `ig34_p0082_a025` | PDF_TYPO | PDF_TYPO | HOLDS | p82:36 (Ex1 dm.xpt 表头); `domains/SE/examples.md:44` (Example 1 下, 非 :79) | 登记 S-SPREL SE T-1. PDF 表头 BIRTHDTC; KB BRTHDTC; 其余 19 个列名顺序逐个一致 |
| R95 | `ig34_p0124_a017` | PDF_TYPO | PDF_TYPO | HOLDS | p124:34-35 (表头 9 列); `domains/ML/examples.md:66` | 登记 B-ML T-1. PDF "WHTE MILK"; KB "WHITE MILK"; 其余 8 格 (2/ABC123/ML/ABC123-001/2/1/WEEK 1/2015-09-09) 一致 |
| R96 | `ig34_p0198_a020` | PDF_TYPO | PDF_TYPO | HOLDS | p198:37-38; `domains/BS/examples.md:7` | 登记 B-BS T-1a + T-1b. PDF "rations" / "may indicated"; KB "ratios" / "may indicate"; 其余逐字一致 |
| R97 | `ig34_p0205_a005` | PDF_TYPO | PDF_TYPO | HOLDS | p205:13-14 + 300dpi 裁切; `domains/CP/assumptions.md:58` | 登记 S-SPC1 CP T-16b. 渲染确为 CPSCMRKS ×3; KB 3 处均 CPCSMRKS; 其余一致 |
| R98 | `ig34_p0213_a009` | PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p213 cp.xpt Ex3 r2; `domains/CP/examples.md:127` (表头) / `:130` | 登记 B-CP T-6. PDF CPTEST "MonoSub"; KB "Mono Sub". 26 格逐格对表头: CPSBMRKS 空、CPCELSTA PROLIFERATING、CPCSMRKS Ki67+、CPMRKSTR CD14+Ki67+、CPGATE MONO、CPGATDEF FSC+SSC+\|CD14+、IMMUNOPHENOTYPING / MONOCYTES / 50 / 10^6/L / 50 / 10^6/L / 50 / QUANTITATIVE / NUMBER CONCENTRATION / BLOOD / FLOW CYTOMETRY / 2020-08-16T08:00 全一致 (原子 verbatim 的空格位置抽错, KB 按渲染页正确) |
| R99 | `ig34_p0236_a014` | PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p236 is.xpt Ex5 r6; `domains/IS/examples.md:113` (表头) / `:120` | 登记 B-IS T-1 (T-2 属 r7, 本原子不涉及). 渲染确为 STUDYID "RSC1230"; KB RSV1230. 表头 22 列 (无 ISORRESU) 与 PDF 一致; 其余 21 格 (含 ISGRPID 空、1:220/220/220/titer、VISITNUM 3、VISIT 2、2017-08-27) 一致 |
| R100 | `ig34_p0247_a020` | PDF_TYPO | PDF_TYPO | HOLDS | p247:70 (Example 3 lb.xpt 表头; 包内自动定位的 :6 是 Ex1 宽表, 定位偏); `domains/LB/examples.md:67` | 登记 B-LB T-1. Ex3 表头 PDF 写 LBSTRNHI; KB LBSTNRHI; 其余 28 个列名顺序逐个一致 |
| R101 | `ig34_p0323_a006` | PDF_TYPO | PDF_TYPO | HOLDS | p323:11-13; `domains/FT/assumptions.md:78` | 登记 B-RS T-6 (FT 副本). PDF "--STRNC"; KB "--STNRC"; 其余 16 个变量及句子一致 |
| R102 | `ig34_p0353_a009` | PDF_TYPO | PDF_TYPO | HOLDS | p353:21; `domains/TU/examples.md:13` | 登记 B-TU T-1. PDF "aorta-iliac"; KB "aorto-iliac"; 其余一致 |
| R103 | `ig34_p0377_a021` | PDF_TYPO | PDF_TYPO | HOLDS | p377:49-50; `domains/SR/assumptions.md:15` | 登记 B-SR T-3. PDF "reactogencity"; KB "reactogenicity"; 其余一致 |
| R104 | `ig34_p0414_a013` | PDF_TYPO | PDF_TYPO | HOLDS | p414:29 (Example 3 td.xpt 表头); `domains/TD/examples.md:167` (## Example 3 下; :50/:102 为 Ex1/Ex2) | 登记 S-TDM TD T-4. PDF TDTGPAI; KB TDTGTPAI; 其余 9 列名一致 |
| R105 | `ig34_p0427_a011` | PDF_TYPO | PDF_TYPO | HOLDS | p427:24-26; `chapters/ch08_relationships.md:15` | 登记 B-ch08 T-1. PDF "DIZOGOTIC"; KB "DIZYGOTIC"; 其余一致 (仅列表符 • → -) |
| R106 | `ig34_p0010_a002` | PDF_TYPO | PDF_TYPO | HOLDS | p10:2-3; `chapters/ch01_introduction.md:85` | 登记 B-ch01 T-1. PDF "a codelist not yet been developed" (缺 has); KB 补 "has"; 其余一致 |
| R107 | `ig34_p0085_a010` | PDF_TYPO | PDF_TYPO | HOLDS | p85:14-15 + 300dpi 裁切; `domains/SM/examples.md:7` | 登记 B-SM O32. 渲染确为 "SMDY" (非 SM 变量); KB SMSTDY, 与登记 handling 一致; 其余一致. (登记自注 "不能唯一确定", 改值是否妥当属主人裁定范围, 不在本判定内) |
| R108 | `ig34_p0198_a012` | PDF_TYPO | PDF_TYPO | HOLDS | p198:26-27; `domains/BS/assumptions.md:19` | 登记 B-BS T-2. PDF "part the SEND"; KB "part of the SEND"; 其余一致 |
| R109 | `ig34_p0199_a020` | PDF_TYPO | PDF_TYPO | HOLDS | p199:32-34 + 300dpi 裁切; `domains/CP/assumptions.md:24` | 登记 S-SPC1 CP T-21. 渲染确为 "--BNDAGT" / "--GATEDEF"; KB "--BDAGNT" / "--GATDEF"; 句内其余 12 个变量与括注一致 |
| R110 | `ig34_p0212_a012` | PDF_TYPO | PDF_TYPO | HOLDS | p212:37-43; `domains/CP/examples.md:109` (包内指针 :71 是 Ex1 "Rows 1-2", 指错) | 登记 B-CP T-15 (登记 pdf_page 记 211, 但 checkpoint `evidence/checkpoints/t2_B-CP.md:306` 明列 ":109 (2)", 本处在登记覆盖内). PDF CPGATEDEF ×2; KB CPGATDEF ×2; 其余整段逐字一致 |
| R111 | `ig34_p0240_a004` | PDF_TYPO | PDF_TYPO | HOLDS | p240:5-9; `domains/IS/examples.md:215` | 登记 B-IS T-4. PDF "(i.e., nucleoar)"; KB "nucleolar"; 其余整段一致 |
| R112 | `ig34_p0262_a029` | PDF_TYPO | PDF_TYPO | HOLDS | p262:53-54 (suppms 表头 + r1); `domains/MS/examples.md:78,80` | 登记 B-MS T-3. PDF IDVAR "MBREFID"; KB MSREFID; 其余 9 格 (1/ABC/MS/ABC-01-101/100.4/MSMEDTYPE/Medium Type/LOWENSTEIN-JENSEN/Collected) 一致 |
| R113 | `ig34_p0280_a040` | PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p280 400dpi 裁切 (散文 "DYIDRGX_HALF" 为衬线大写 I, 与同页 "DY1DRGX_A" 的数字 1 字形明显不同; 同页 relrec IDVARVAL 为 DY1DRGX_HALF); `domains/PC/examples.md:285` (包内指针 :284 是 Rows 1-3) | 登记 B-PCPP T-8. PDF 确为 I 而非文本层伪影; KB DY1DRGX_HALF; 其余逐字一致 |
| R114 | `ig34_p0335_a015` | PDF_TYPO | PDF_TYPO | HOLDS | p335:26-28; `domains/RS/examples.md:50` | 登记 B-RS T-7. PDF "RSPLNKGRP"; KB "RSLNKGRP"; 其余一致 |
| R115 | `ig34_p0370_a021` | PDF_TYPO | PDF_TYPO | HOLDS | p370:26; `domains/FA/examples.md:118` | 登记 B-FA T-7. PDF "parent CE record"; KB "parent AE record"; 其余一致 |

## 计数

- PDF_TYPO 层 (本包 25 条): HOLDS 25 / NOT_HOLD 0 / UNVERIFIABLE 0
- 按判定规则: `K3b-registry` (R91-R105) 15 条全 HOLDS; `S1-R2` (R106-R115) 10 条全 HOLDS

## 备注 (不影响判定)

- 包内 "KB 现文" 指针偏的 4 条: R100 (PDF 定位到 Ex1 宽表 :6, 实为 :70 Ex3 表头)、R104 (3 处命中, 实为 :167)、R110 (KB 指针 :71 应为 :109)、R113 (KB 指针 :284 应为 :285). 均已自行定位核对.
- R107 / R113 登记带 `t4_decision: U-7 B (委托代裁)`; R109 登记 note 写 "主控定 #1 可回退照录". 本审查只核 "KB 现状与登记 handling (KB 写正确值) 一致", 是否改值由主人另裁.

## 样本外发现的 KB 内容问题

无.
