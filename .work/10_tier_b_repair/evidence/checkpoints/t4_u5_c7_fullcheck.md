# T4 U-5: C7 规则 38 条 ATOM_ERR 全检
<!-- chain: E (plans) -->
> 状态: 审查完成 (2026-11-27), 审查者 oh-my-claudecode:tracer (opus), 只读

## 方法
- 数据: `.work/10_tier_b_repair/work/t4/u5_c7_38.jsonl` (38 行); 行号对应关系用 `archive/deep_verification/pdf_atoms.jsonl` 核对 (atom verbatim 首格 = PDF Row 号).
- 渲染页: 用 Read(pages) 逐页看了 `source/cdisc/SDTMIG v3.4 (no header footer).pdf` p210, 212, 213, 214, 215, 218, 219, 220, 247, 270, 271, 277 (12 页覆盖全部 38 条); 表格小字另用 `pdftoppm -r 250` 裁切放大 (p214/215/218/219/220/247/270/271/277 表体 + 表头) 后逐格比对.
- 文本层 `work/pdf_pages/ig34_pNNNN.txt` 只作辅助; 列错位/断行处以渲染页为准.
- 半 2: 逐行比对 KB 表格行 (文件:行 见表). 表头 6 处 (p210/218/219/220/247×2) 另用脚本逐列比对文本层 = KB (p220 差异只有登记笔误 T-14); p277 PP 12 行逐 token 比对文本层 = KB 全部 True.
- 笔误登记查 `work/t2_pdf_typo_registry.jsonl`.

## 逐条结果
| # | atom_id | 页 | 半1 原子≠PDF (依据) | 半2 KB=PDF (KB 文件:行) | 判定 | 备注 |
|---|---|---|---|---|---|---|
| 1 | ig34_p0210_a002 | 210 | 原子表头顺序 CPSTRESC/CPSTRESN/CPSTRESU; 渲染页 Ex1a 表头为 CPSTRESC, CPSTRESU, CPSTRESN | CP/examples.md:31 列序同 PDF (19 列脚本比对一致) | 成立 | jsonl discrepancy 文字 ("MD 有 CPRESU") 已过时 |
| 2 | ig34_p0210_a007 | 210 | 原子 CPTESTCD "BLYCE"; 渲染页 row 5 为 BLYCELY, 列序同 #1 | CP/examples.md:37 row 5 BLYCELY, 6.1 %, NUMBER FRACTION 一致 | 成立 | |
| 3 | ig34_p0212_a006 | 212 | 原子 CPGRPID 2、CPGATDEF "FSC SSC/CD45+"; 渲染页 row 11 CPGRPID 3、"FSC SSC\|CD45+" | CP/examples.md:97 GRPID 3, `FSC SSC\|CD45+`, 19 RATIO 一致 | 成立 | |
| 4 | ig34_p0213_a013 | 213 | 原子 MNPMNPNP / "Mono ProlifMono NonProlif" / CPORRESU %; 渲染页 row 6 MNPMNNP / "Mono Prolif/Mono NonProlif" / 单位空 | CP/examples.md:134 一致 (CALCULATION, RATIO, 单位空) | 成立 | |
| 5 | ig34_p0214_a008 | 214 | 原子 TLCRCC、"T-Lym Cyt Cyk…"、2017-01-20、0.6; 渲染页 row 1 TLCSTLC、"TLym Cytx Sub/TLym Cytx"、2021-03-20T09:52:00、0.9 | CP/examples.md:159 逐格一致 | 成立 | 放大图核 |
| 6 | ig34_p0214_a009 | 214 | 同 #5 体系错; 渲染页 row 2 = 0.6, CPREPNUM 2 | CP/examples.md:160 一致 | 成立 | |
| 7 | ig34_p0214_a010 | 214 | 同上; 渲染页 row 3 = 0.8 MEAN CALCULATION | CP/examples.md:161 一致 | 成立 | |
| 8 | ig34_p0214_a011 | 214 | 原子 USUBJID 后 CPSEQ 1 正确但 TESTCD/日期/CPCNDAGT 位置错; 渲染页 row 4 = 2.9, REP 1 | CP/examples.md:162 一致 | 成立 | |
| 9 | ig34_p0214_a012 | 214 | 同上; 渲染页 row 5 = 2.6, REP 2 | CP/examples.md:163 一致 | 成立 | |
| 10 | ig34_p0214_a013 | 214 | 同上; 渲染页 row 6 = 2.8 MEAN | CP/examples.md:164 一致 | 成立 | |
| 11 | ig34_p0214_a014 | 214 | 原子 USUBJID "STBNDX"、CPANMETH "STIMULATED(CONC)/…"; 渲染页 row 7 STIMDX, "STIMULATED/UNSTIMULATED", CPTSTCND 空 | CP/examples.md:165 一致 | 成立 | |
| 12 | ig34_p0215_a005 | 215 | 原子 row 3 = BLYCELE/"Blym/Leuk"/ABCD-001-002; 渲染页 row 3 = CD95X / "CD95 Expression" / ABCD-001-001 / 100 MdFI | CP/examples.md:181 一致 | 成立 | |
| 13 | ig34_p0215_a010 | 215 | 原子 row 8 = BLYBN, 50.2; 渲染页 row 8 = CD95X, 89 MdFI, CPSEQ 5 | CP/examples.md:186 一致 (CPMRKSTR 跨行续接 "CD95+" 无空格合并) | 成立 | |
| 14 | ig34_p0218_a002 | 218 | 原子表头含重复 CPGATE/CPGATDEF、"OPCAT"、"CPTRESU"; 渲染页 Ex7 表头 24 列无此 | CP/examples.md:255 与 PDF 24 列逐列一致 | 成立 | discrepancy 写 "Ex1b" 有误, 实为 Ex7 |
| 15 | ig34_p0219_a002 | 219 | 原子含 CPTESTCND/CPTSCAT/CPPORRES/CPSTRSSC/CPTP; 渲染页 Ex8 表头为 CPTEST/CPTSTCND/CPSCAT/CPORRES…CPTPT | CP/examples.md:279 32 列逐列一致 | 成立 | |
| 16 | ig34_p0220_a006 | 220 | 原子含重复 CPGATE/CPGATDEF、OPCAT、CPANNMTH、CPRELFL, 缺 CPABCLID/CPBLFL; 渲染页 Ex9 表头无此 | CP/examples.md:311 等价 (PDF "ROW"/"CPTST PNL" → KB Row/CPTSTPNL, 登记 B-CP T-14 "KB 写正确值") | 成立 | |
| 17 | ig34_p0247_a005 | 247 | 原子表头含 LBENDTC/LBSTDTC/LBBDAGNT/LBTPT 等 51 列; 渲染页 Ex1 表头 41 列 (…LBDTC, LBPTFL, LBPDUR) | LB/examples.md:22 41 列逐列一致 | 成立 | |
| 18 | ig34_p0247_a011 | 247 | 原子缺 LBLOINC; 渲染页 Ex2 表头 LBNRIND 后有 LBLOINC | LB/examples.md:52 34 列逐列一致 | 成立 | |
| 19 | ig34_p0247_a022 | 247 | 原子 LBRESTYP "PtFtv"; 渲染页 Ex3 row 2 为 "PrThr" | LB/examples.md:70 一致 (NOT DONE / NOT APPLICABLE (SUBJECT MALE) / 1999-06-24T08:00) | 成立 | 表头 PDF "LBSTRNHI" 已登记 B-LB T-1 |
| 20 | ig34_p0270_a013 | 270 | 原子 PCREFID "A854134-10"、PCELTM 空; 渲染页 row 1 A554134-10、PCELTM -PT15M | PC/examples.md:27 一致 | 成立 | |
| 21 | ig34_p0270_a014 | 270 | 同 #20 (A854134、PCELTM 空); 渲染页 row 2 A554134-10, -PT15M | PC/examples.md:28 一致 | 成立 | |
| 22 | ig34_p0270_a023 | 270 | 原子 A854134-14、PCLLOQ 0.10; 渲染页 row 11 A554134-14、PCLLOQ 空、PCULOQ 20 | PC/examples.md:37 一致 (NOT DONE, LLOQ 空) | 成立 | |
| 23 | ig34_p0271_a007 | 271 | 原子 PCREFID -19、PCDTC "12T11:20:03"; 渲染页 row 27 A554134-20、PCDTC 2001-02-11T20:03 | PC/examples.md:53 一致 | 成立 | |
| 24 | ig34_p0271_a009 | 271 | 原子 PCDTC "2001-02- 12T11:20:03"; 渲染页 row 29 PCDTC 2001-02-11T20:03 | PC/examples.md:55 一致 | 成立 | |
| 25 | ig34_p0271_a010 | 271 | 原子 PCSTRESN 空且少 1 列 (VISITNUM 前空格数不足); 渲染页 row 30 PCSTRESN 5.5 | PC/examples.md:56 一致 | 成立 | |
| 26 | ig34_p0271_a011 | 271 | 原子 PCREFID -19、PCDTC 11T20:03、PCENDTC 12T08:10; 渲染页 row 31 A554134-21、PCDTC 2001-02-12T08:00、PCENDTC 空 | PC/examples.md:57 一致 | 成立 | |
| 27 | ig34_p0277_a004 | 277 | 原子 PPGRPID(Ex4) "DY1DRGX"; 渲染页 row 1 为 TMAX | PC/assumptions.md:92 一致 (脚本逐 token True) | 成立 | kb_loc 写 :88, 实际 :92 (偏 4 行, 下同) |
| 28 | ig34_p0277_a005 | 277 | 原子 Ex4 列 DY1DRGX; PDF CMAX | PC/assumptions.md:93 一致 | 成立 | |
| 29 | ig34_p0277_a006 | 277 | 原子 Ex4 列 DY1DRGX; PDF AUC | PC/assumptions.md:94 一致 | 成立 | |
| 30 | ig34_p0277_a007 | 277 | 原子 PPSEQ 4、Ex4 DY1DRGX; PDF PPSEQ 5、OTHER | PC/assumptions.md:95 一致 | 成立 | |
| 31 | ig34_p0277_a008 | 277 | 原子 PPSEQ 5、Ex4 DY1DRGX; PDF 6、OTHER | PC/assumptions.md:96 一致 | 成立 | |
| 32 | ig34_p0277_a009 | 277 | 原子 PPSEQ 6、Ex4 DY1DRGX; PDF 7、OTHER | PC/assumptions.md:97 一致 | 成立 | |
| 33 | ig34_p0277_a010 | 277 | 原子 PPSEQ 7; PDF 8 | PC/assumptions.md:98 一致 | 成立 | |
| 34 | ig34_p0277_a011 | 277 | 原子 PPSEQ 8; PDF 9 | PC/assumptions.md:99 一致 | 成立 | |
| 35 | ig34_p0277_a012 | 277 | 原子 PPSEQ 9; PDF 10 | PC/assumptions.md:100 一致 | 成立 | |
| 36 | ig34_p0277_a013 | 277 | 原子 PPSEQ 10; PDF 12 | PC/assumptions.md:101 一致 | 成立 | |
| 37 | ig34_p0277_a014 | 277 | 原子 PPSEQ 11; PDF 13 | PC/assumptions.md:102 一致 | 成立 | |
| 38 | ig34_p0277_a015 | 277 | 原子 PPSEQ 12; PDF 14 | PC/assumptions.md:103 一致 | 成立 | |

(KB 路径前缀均为 `knowledge_base/domains/`.)

## 计数
- 成立: 38
- 不成立: 0
- 看不出: 0

## 位置说明
- #20-26 在 PC/examples.md Example 1 (§6.3.5.9.1), 与 PDF 章节一致.
- #27-38 PP 数据集在 PC/assumptions.md "Pharmacokinetic Parameters (PP) Dataset for All Examples" (:86-103); PDF 该表属 §6.3.5.9.3 共享数据集, KB 在 PC/examples.md:3 注明 §6.3.5.9.3 共享数据集放在 PC/assumptions.md, 属该章节承载位置. C7 "MISPLACED §R vs §E" 是脚本对章节标签的误判, 不影响 KB 内容.

## 样本外顺手发现 (不修)
1. **KB 正文**: 未发现新的 KB 与 PDF 不一致. 看到的 PDF 笔误均已登记: B-CP T-6 (p213 "MonoSub"), T-11 (p220 r1 CPORRES 85), T-12/T-13 (p220 CPANMETH), T-14 (p220 表头), B-LB T-1 (p247 "LBSTRNHI").
2. **元数据 (非 KB)**: `u5_c7_38.jsonl` 中 #27-38 的 kb_loc 写 PC/assumptions.md:88-99, 实际行是 :92-103 (偏 4 行); #1/#2/#14-16 的 discrepancy 文字已过时 (提到 "CPRESU"、"Example 1b"), 与 KB 当前内容不符. 如果 ledger 引用这些字段, 建议重算.
