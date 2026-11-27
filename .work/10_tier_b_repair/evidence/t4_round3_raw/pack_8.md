# T4.1 第三轮补检 — 包 8 (R3_PDF_TYPO, T176-T200) 审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间 (date -u): 2026-11-27T06:38:38Z
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round3_v1.0.md` (R3_PDF_TYPO = round2 `PDF_TYPO` 层同口径: ① PDF 确有登记的问题; ② KB 与 `handling` 一致; ③ 其余内容 KB = PDF)
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`): p198、p206、p257、p263 (Read 整页); p215 (pdftoppm -r 200 局部裁剪, Rows 15-18 行右半)
- 其余页 (174/190/200/211/213/217/218/220/224/225/227/228/236/262) 用文本层 `work/pdf_pages/ig34_pNNNN.txt`; 这些都是拼写 / 变量名 / 表格单格值类问题, 文本层字符明确
- 用过的命令:
  - 登记查询: `grep -F '"id": "<id>"' work/t2_pdf_typo_registry.jsonl`; 同页其它登记: `grep -n -E 'ORNLO|GPRID|CD278|CD19-|"pdf_page": (174|...|263),' work/t2_pdf_typo_registry.jsonl`; `grep -n 'CD278|T-16a|未闭合' evidence/checkpoints/*.md`; `grep -n '^| T-3 ' evidence/checkpoints/t2_B-CP*.md`
  - KB 定位: `grep -n "<句首片段>" knowledge_base/domains/{CP,IS,MS,GF}/*.md`; `sed -n` 看表头
  - 叙述类逐词比对: 临时脚本 `scratchpad/r3_8/wd.py` (PDF 文本层行段拼接 → 与 KB 行做 difflib 词级 diff, 归一 `**` 与弯引号), 20 条叙述原子全部跑过, 差异逐条人工复核
  - 渲染裁剪: `pdftoppm -r 200 -f 215 -l 215 -x 1900 -y 1150 -W 1100 -H 120 -png ...`

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| T176 | `ig34_p0174_a0012` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0174.txt:25-29`; `domains/MH/assumptions.md:51` | B-MH T-1: PDF 第二处 `MHENDTYP = "DIAGNOSIS"`, KB `MHEVDTYP`; 词级 diff 仅此一处 |
| T177 | `ig34_p0190_a017` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0190.txt:32`; `domains/EG/examples.md:42` | B-EG T-3: PDF "principal investigation" → KB "investigator"; 其余逐词一致 ("SCREEN 2" 照录, 属 B-EG T-2 照录+T4, KB = PDF) |
| T178 | `ig34_p0198_a014` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p198 Assumption 5; `ig34_p0198.txt:31-32`; `domains/BS/assumptions.md:23` | B-BS T-3 (`--STRNLO`→`--STNRLO`) 成立。同句另有 `--ORNLO, --ORNHI` → KB `--ORNRLO, --ORNRHI`, 样本包没列, 但已另登记 **REG BS N-1** (KB 写正确值, U-7 B 定), 故不算未登记差异。其余项逐个一致 |
| T179 | `ig34_p0200_a006` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0200.txt:10-11`; `domains/CP/assumptions.md:40` | S-SPC1 CP T-17: "marker sting" → "marker string"; 其余一致 |
| T180 | `ig34_p0200_a007` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0200.txt:11-12`; `domains/CP/assumptions.md:42` (包给的 :24 不是对应行) | S-SPC1 CP T-21 ("--GATEDEF ×2", note 含 :42): PDF `--GATEDEF` → KB `--GATDEF`; 其余逐词一致 |
| T181 | `ig34_p0206_a001` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p206 首行; `ig34_p0206.txt:1-2`; `domains/CP/assumptions.md:72` (包给的 :24 不是对应行) | S-SPC1 CP T-21 (note 含 :72): PDF `CPBNDAGT` → KB `CPBDAGNT`; 原子部分其余一致 (KB :72 前半为 p205 上的 6c 前文) |
| T182 | `ig34_p0206_a003` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p206 7a; `ig34_p0206.txt:4-13`; `domains/CP/assumptions.md:75` | S-SPC1 CP T-18: 7a 第一处 `CSMRKS` → `CPCSMRKS`; 其余一致 |
| T183 | `ig34_p0206_a009` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p206 8d; `ig34_p0206.txt:36-51`; `domains/CP/assumptions.md:82` | S-SPC1 CP T-19: `CPSMRKS` → `CPSBMRKS`。另 2 处差异: 渲染页确为 `"CD3+CD19- (T lymphocyte)`、`"CD278+ (activated)` 引号未闭合, KB 闭合 → 属 **S-SPC1 CP T-16a** (KB 写正确值)。注: 登记表 T-16a 的 `pdf_value` 只写了 CD3+CD19- 一处, CD278+ 那处只在 `evidence/checkpoints/t2_S-SPC1.md:127` / `t2_S-SPC1_review.md:100` 写明; 判 HOLDS, 登记文字不全见 "样本外发现" |
| T184 | `ig34_p0211_a004` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0211.txt:10-14`; `domains/CP/examples.md:71` | B-CP T-15: `(CPGATEDEF)` → `(CPGATDEF)`; 其余一致 |
| T185 | `ig34_p0213_a002` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0213.txt:6-11`; `domains/CP/examples.md:117` (包给的 :71 不是对应行) | B-CP T-15: 两处 `CPGATEDEF` → `CPGATDEF`; 其余逐词一致 (diff 里 "CDxx+CDyy-monocyte" 是脚本跨行拼接伪差, PDF 实为 "CDxx+CDyy- monocyte") |
| T186 | `ig34_p0215_a017` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p215 (裁剪) Rows 15-18; `ig34_p0215.txt:39-41`; `domains/CP/examples.md:200` | B-CP T-3: 渲染页为 "(e.g., CD40+ in rows 15-16 in addition to non-cell state, non-sublineage marker(s). Rows 17-18" — "(e.g.," 括号没有闭合; KB 在 "15-16" 后补 ")" = 登记的 kb_value。问题成立、处理一致、其余一致。注: 登记 `pdf_value` 写的是 "…marker(s))."(双右括号), 渲染页实为 "marker(s)." 单括号 (只有 "(s)" 自带的那个), 登记对 PDF 原文的誊写不准, 见 "样本外发现" |
| T187 | `ig34_p0217_a015` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0217.txt:47-51`; `domains/CP/examples.md:247` (包给的 :71 不是对应行) | B-CP T-15: `CPGATEDEF` → `CPGATDEF`; 其余一致 |
| T188 | `ig34_p0218_a014` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0218.txt:20`; `domains/CP/examples.md:267` (包给的 :71 不是对应行) | B-CP T-15: `CPGATEDEF` → `CPGATDEF`; 其余一致 |
| T189 | `ig34_p0220_a001` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0220.txt:1-2`; `domains/CP/examples.md:303` (Ex9 Row 1 段, 包给的 :71 不是对应行) | B-CP T-15: 句首 `CPGATEDEF` → `CPGATDEF`; 原子这段 (到 "…on which the test was performed.") 其余逐词一致 |
| T190 | `ig34_p0224_a013` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0224.txt:22-24`; `domains/GF/examples.md:5` | B-GF T-1: inheritabilty → inheritability; 其余一致 |
| T191 | `ig34_p0225_a019` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0225.txt:65-66`; `domains/GF/examples.md:70` | B-GF T-3: PDF "respresented" → KB "represented"; 其余一致。原子写成 "rerspresented", 是原子抽错 (PDF 文本层为 "respresented") |
| T192 | `ig34_p0227_a018` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0227.txt:29-31`; `domains/GF/examples.md:142-145` | B-GF T-2: MBTEST "Idenitifcation" → "Identification"。16 格逐格: 1 / INFLU122 / MB / INF01-01 / 1 / INFLU0101 (B-GF U-2 照录, KB = PDF) / MCORGIDN / MBTEST / MBORRES、MBSTRESC "INFLUENZA A VIRUS SUBTYPE H3N2" / MUCUS / NOSTRIL / NUCLEIC ACID AMPLIFICATION TEST / 1 / BASELINE / 2020-06-11, 都一致; 表头 16 列一致 |
| T193 | `ig34_p0228_a002` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0228.txt:2-3`; `domains/GF/examples.md:157` | B-GF T-5: PDF 句末没有句号, KB 补了; 其余一致 |
| T194 | `ig34_p0228_a009` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0228.txt:15-17`; `domains/GF/examples.md:169` | B-GF T-4: PDF `GFLINKID` → KB `GFLNKID`; 其余一致 (原子已被抽成改正值) |
| T195 | `ig34_p0236_a005` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0236.txt:16-17`; `domains/IS/examples.md:108` | B-IS T-3: "NON-STUDY RELATED" → "NON-STUDY-RELATED"; 其余一致 |
| T196 | `ig34_p0236_a015` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0236.txt:40-42`; `domains/IS/examples.md:121` (r7; 包给的 :120 是 r6) | B-IS T-2: r7 STUDYID RSC1230 → RSV1230。22 格逐格: 7 / STUDYID / IS / RSV1230-011 / 3 / 13671 / ISGRPID 空 / MBIGGAB / Microbial-induced IgG Antibody / HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B / QUANTIFY / STUDY VACCINE-RELATED IMMUNOGENICITY / HUMORAL IMMUNITY / 1:500 / 500 / 500 / titer / SERUM / ELISA / 4 / VISIT 3 / 2017-09-27, 都一致。ISSEQ=3 与 B-IS U-1 (照录) 一致 |
| T197 | `ig34_p0257_a016` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p257 ms.xpt r9; `domains/MS/examples.md:20,31` | B-MS T-1: 渲染页 r9 的 MSSTRESC 格为空 (MSORRES 25 / MSORRESU mm / MSSTRESN 25 / MSSTRESU mm), KB 的 MSSTRESC 是 25。其余 21 格逐格一致 (NHOID ENTEROCOCCUS FAECALIS, MSGRPID 4, MSSEQ 9, SPEC01, MSLNKGRP 2, DIAZOINH, Amoxicillin, MSCONC/MSCONCU 空, LOCAL LAB XYZ, DISK DIFFUSION, 2005-06-26T08:00) |
| T198 | `ig34_p0262_a020` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0262.txt:35-37`; `domains/MS/examples.md:65` | B-MS T-2: `MSCONU` → `MSCONCU`; 其余一致 |
| T199 | `ig34_p0262_a030` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0262.txt:55`; `domains/MS/examples.md:78,81` (r2; 包给的 :80 是 r1) | B-MS T-3: IDVAR `MBREFID` → `MSREFID`。10 格逐格: 2 / ABC / MS / ABC-01-101 / IDVAR / 100.5 / MSMEDTYPE (B-MS T-4 照录, KB = PDF) / Medium Type / LOWENSTEIN-JENSEN / Collected, 都一致 |
| T200 | `ig34_p0263_a020` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p263 Example 4 mb.xpt 表头; `domains/MB/examples.md:241` | B-MB T-3: `MBTRESN` → `MBSTRESN`。同一表头还有 `MBGPRID` → KB `MBGRPID` (渲染页确认), 样本包没列, 但已登记 **B-MB T-2** (KB 写正确值)。其余 21 列名逐个一致 |

## 计数

| 判定 | 数量 |
|---|---|
| HOLDS | 25 |
| NOT_HOLD | 0 |
| UNVERIFIABLE | 0 |

全部 25 条属 R3_PDF_TYPO 层。层通过 (NOT_HOLD 0、UNVERIFIABLE 0)。

补充 (不影响判定): 有 3 条原子含**不止一处**已登记笔误, 样本包只写了其中一个登记 id: T178 (另含 REG BS N-1)、T183 (另含 S-SPC1 CP T-16a)、T200 (另含 B-MB T-2)。另有 8 条的 KB 指针不是对应行 (T180、T181、T185、T187、T188、T189、T196、T199), 已按上表自己定位到的行核对。

## 样本外发现 (不算样本判定, 不修)

1. **登记文字不准 — B-CP T-3** (`work/t2_pdf_typo_registry.jsonl` 第 23 行; `evidence/checkpoints/t2_B-CP.md:140,200` 同样写法): `pdf_value` 写成 "(e.g., CD40+ in rows 15-16 in addition to … marker(s)).", 但 p215 渲染页实为 "…non-sublineage marker(s). Rows 17-18" — 没有第二个右括号, 问题实质是 "(e.g.," 括号没有闭合, 不是括号位置错。KB 处理 (在 "15-16" 后补 ")") 不受影响。建议只修登记文字。
2. **登记文字不全 — S-SPC1 CP T-16a** (`work/t2_pdf_typo_registry.jsonl` 第 37 行): `pdf_value` 只记了 `"CD3+CD19- (T lymphocyte)` 一处, p206 8d 的 `"CD278+ (activated)` 同样引号未闭合、KB 也已闭合 (`knowledge_base/domains/CP/assumptions.md:82`); 第二处只记在 `evidence/checkpoints/t2_S-SPC1.md:127`。建议登记补全。
3. KB 内容问题: 无。
