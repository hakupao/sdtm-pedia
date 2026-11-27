# T4.1 第二轮补检包 7 — PDF_TYPO (20 条; 编号 R116-R135)

> 由 `scripts/t4/t4_round2_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 R).

### R116. `ig34_p0372_a013` — r2:PDF_TYPO

- PDF 页 372 · 原子类型 SENTENCE · 所在节 `FA – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-FA`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A3-9 B-FA T-8 populated→populate | errata: t3_atom_err | new_target: domains/FA/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:113`
- 登记 `B-FA T-8`: PDF 写 "used to populated FADTC" → KB 写 "used to populate FADTC" (处理: KB 写正确值; 依据: 语法类; KB `knowledge_base/domains/FA/examples.md:183`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example shows data for 1 subject at 2 visits. Each response (e.g., No, Yes) to the prespecified terms is represented in the FA domain. The visit date was used to populated FADTC.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0372.txt` 第 16-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15| 
 16| This example shows data for 1 subject at 2 visits. Each response (e.g., No, Yes) to the prespecified terms is represented in the FA domain. The visit date was used
 17| to populated FADTC.
 18| Rows 1, 4: "Headache" was reported at both visits.
~~~~

KB 现文: `knowledge_base/domains/FA/examples.md:183` (来源: registry B-FA T-8 kb_line_now):

~~~~
 183| This example shows data for 1 subject at 2 visits. Each response (e.g., No, Yes) to the prespecified terms is represented in the FA domain. The visit date was used to populate FADTC.
~~~~

### R117. `ig34_p0373_a013` — r2:PDF_TYPO

- PDF 页 373 · 原子类型 SENTENCE · 所在节 `FA – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `B-FA`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-FA T-9: FAEVINTX → FAEVLINT; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-FA.md:129`
- 登记 `B-FA T-9`: PDF 写 "叙述 FAEVINTX" → KB 写 "FAEVLINT" (处理: KB 写正确值; 依据: 同例 face 列 FAEVLINT, 值 -PT24H; KB `knowledge_base/domains/FA/examples.md:228`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This SDTM example represents data from 2 visits for 1 subject. FAEVINTX indicates that assessments were for the previous 24 hours.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0373.txt` 第 18-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| criterion 2 data (“about” an event or intervention), having qualifiers that can be represented in Findings variables (e.g., units, method).
 18| This SDTM example represents data from 2 visits for 1 subject. FAEVINTX indicates that assessments were for the previous 24 hours.
 19| Rows 1-4:        Show the results for the vomiting tests at visit 1. Because the number of episodes was recorded as ">10", this is represented in FASTRESC but
~~~~

KB 现文: `knowledge_base/domains/FA/examples.md:228` (来源: registry B-FA T-9 kb_line_now):

~~~~
 228| This SDTM example represents data from 2 visits for 1 subject. FAEVLINT indicates that assessments were for the previous 24 hours.
~~~~

### R118. `ig34_p0419_a006` — r2:PDF_TYPO

- PDF 页 419 · 原子类型 SENTENCE · 所在节 `§7.4.2 Trial Summary (TS) – Assumptions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-TS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-5 B-TS T-3 DOSFREQ→DOSFRQ (+A2-4 B-TS T-2 Dose→DOSE) | errata: t3_atom_err | new_target: domains/TS/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:117`
- 登记 `B-TS T-3`: PDF 写 "DOSFREQ" → KB 写 "DOSFRQ (TSPARMCD CT C89081; 叙述 + 表 2 格共 3 处)" (处理: KB 写正确值; 依据: 两处互异; KB `knowledge_base/domains/TS/assumptions.md:43`)
- 登记 `B-TS T-2`: PDF 写 "TSPARMCD = "Dose"" → KB 写 "DOSE (TSPARMCD CT C25488)" (处理: KB 写正确值; 依据: 大小写不一致; KB `knowledge_base/domains/TS/assumptions.md:43`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
There are 2 records each for TSPARMCD = "Dose" and TSPARMCD = "DOSFREQ".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0419.txt` 第 16-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15|     For example, if a trial compared administration of a total daily dose given once a day to that dose split over
 16|     2 administrations, the TS dataset might include the following records. There are 2 records each for
 17|     TSPARMCD = "Dose" and TSPARMCD = "DOSFREQ". Records with the same TSGRPID are associated
 18|     with each other. In this example, dose units are the same for both administration schedules, so only 1 record
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:43` (来源: registry B-TS T-3 kb_line_now):

~~~~
  43|     For example, if a trial compared administration of a total daily dose given once a day to that dose split over 2 administrations, the TS dataset might include the following records. There are 2 records each for TSPARMCD = "DOSE" and TSPARMCD = "DOSFRQ". Records with the same TSGRPID are associated with each other. In this example, dose units are the same for both administration schedules, so only 1 record for DOSU is needed.
~~~~

### R119. `ig34_p0419_a011` — r2:PDF_TYPO

- PDF 页 419 · 原子类型 TABLE_ROW · 所在节 `§7.4.2 Trial Summary (TS) – Assumptions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `B-TS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-5 B-TS T-3 DOSFREQ→DOSFRQ | errata: t3_atom_err | new_target: domains/TS/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:118`
- 登记 `B-TS T-3`: PDF 写 "DOSFREQ" → KB 写 "DOSFRQ (TSPARMCD CT C89081; 叙述 + 表 2 格共 3 处)" (处理: KB 写正确值; 依据: 两处互异; KB `knowledge_base/domains/TS/assumptions.md:43`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
1 | A | DOSFREQ | Dosing Frequency | BID
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0419.txt` 第 22-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 21|      1                     A                     DOSE                   Dose per Administration   50
 22|      1                     A                     DOSFREQ                Dosing Frequency          BID
 23|      2                     B                     DOSE                   Dose per Administration   100
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:43` (来源: registry B-TS T-3 kb_line_now):

~~~~
  43|     For example, if a trial compared administration of a total daily dose given once a day to that dose split over 2 administrations, the TS dataset might include the following records. There are 2 records each for TSPARMCD = "DOSE" and TSPARMCD = "DOSFRQ". Records with the same TSGRPID are associated with each other. In this example, dose units are the same for both administration schedules, so only 1 record for DOSU is needed.
~~~~

### R120. `ig34_p0419_a017` — r2:PDF_TYPO

- PDF 页 419 · 原子类型 LIST_ITEM · 所在节 `§7.4.2 Trial Summary (TS) – Assumptions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `B-TS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-6 B-TS T-4 OUTMSPR→OUTMSPRI | errata: t3_atom_err | new_target: domains/TS/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:120`
- 登记 `B-TS T-4`: PDF 写 "TSPARM = "OUTMSPR"" → KB 写 "OUTMSPRI (TSPARMCD CT C98772)" (处理: KB 写正确值; 依据: 两处互异; KB `knowledge_base/domains/TS/assumptions.md:57`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
16. If a primary objective is assessed by means of multiple outcome measures, then all of these outcome measures should be provided as values of TSPARM = "OUTMSPR" (Primary Outcome Measure). Similarly, all outcome measures used to assess secondary objectives should be provided as values of TSPARM = "OUTMSSEC" (Secondary Outcome Measure), and all outcome measures used to assess exploratory objectives should be provided as values of TSPARM = "OUTMSEXP" (Exploratory Outcome Measure). Additional key measures of a study that are not designated as primary, secondary, or exploratory should be provided as values of TSPARM = "OUTMSADD" (Additional Outcome Measure).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0419.txt` 第 37-43 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36|     points, or using different analysis methods.
 37| 16. If a primary objective is assessed by means of multiple outcome measures, then all of these outcome
 38|     measures should be provided as values of TSPARM = "OUTMSPR" (Primary Outcome Measure).
 39|     Similarly, all outcome measures used to assess secondary objectives should be provided as values of
 40|     TSPARM = "OUTMSSEC" (Secondary Outcome Measure), and all outcome measures used to assess
 41|     exploratory objectives should be provided as values of TSPARM = "OUTMSEXP" (Exploratory Outcome
 42|     Measure). Additional key measures of a study that are not designated as primary, secondary, or exploratory
 43|     should be provided as values of TSPARM = "OUTMSADD" (Additional Outcome Measure).
 44| 17. Trial indication: Values for TSVAL when TSPARMCD = "INDIC" would indicate the condition, disease,
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:57` (来源: registry B-TS T-4 kb_line_now):

~~~~
  57| 16. If a primary objective is assessed by means of multiple outcome measures, then all of these outcome measures should be provided as values of TSPARM = "OUTMSPRI" (Primary Outcome Measure). Similarly, all outcome measures used to assess secondary objectives should be provided as values of TSPARM = "OUTMSSEC" (Secondary Outcome Measure), and all outcome measures used to assess exploratory objectives should be provided as values of TSPARM = "OUTMSEXP" (Exploratory Outcome Measure). Additional key measures of a study that are not designated as primary, secondary, or exploratory should be provided as values of TSPARM = "OUTMSADD" (Additional Outcome Measure).
~~~~

### R121. `ig34_p0016_a019` — r2:PDF_TYPO

- PDF 页 16 · 原子类型 NOTE · 所在节 `§2.7 SDTM Variables Not Allowed in the SDTMIG`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `writer-Tn-registry` · 批 `B-ch02`
- 登记 `B-ch02 T-1`: PDF 写 "Trials Sets domain" → KB 写 "Trial Sets (sv20 p53 §5.1.2)" (处理: KB 写正确值; 依据: SDTMIG 自身无 Trial Sets; sv20 p53 §5.1.2 标题; KB `knowledge_base/chapters/ch02_fundamentals.md:176`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The use of SETCD additionally requires the use of the Trials Sets domain.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0016.txt` 第 22-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 21| 
 22|         The use of SETCD additionally requires the use of the Trials Sets domain.
 23| 
~~~~

KB 现文: `knowledge_base/chapters/ch02_fundamentals.md:176` (来源: registry B-ch02 T-1 kb_line_now):

~~~~
 176| The use of SETCD additionally requires the use of the Trial Sets domain.
~~~~

### R122. `ig34_p0218_a017` — r2:PDF_TYPO

- PDF 页 218 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `writer-Tn-registry` · 批 `B-CP`
- 登记 `B-CP T-4`: PDF 写 "段末逗号 therapeutic antibody," → KB 写 "therapeutic antibody." (处理: KB 写正确值; 依据: 段落结束; KB `knowledge_base/domains/CP/examples.md:271`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 4-6:	CPTEST, CPBDAGNT, REPNUM, and CPCOLSRT are used the same manner as they are in rows 1-3, except that CPTSTCND is now also used to indicate that the assay was conducted under a saturating condition of CDxx antibody by adding an excess of this therapeutic antibody to the assay system. Under this condition, the labeled detection antibody reflects the maximum (total) amount of CDxx available to be occupied by the therapeutic antibody,
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0218.txt` 第 26-28 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25|                      unaltered specimen are indicated using CPREPNUM and CPCOLSRT.
 26| Rows 4-6:            CPTEST, CPBDAGNT, REPNUM, and CPCOLSRT are used the same manner as they are in rows 1-3, except that CPTSTCND is now also used to indicate that the assay was conducted under a
 27|                      saturating condition of CDxx antibody by adding an excess of this therapeutic antibody to the assay system. Under this condition, the labeled detection antibody reflects the maximum (total) amount of
 28|                      CDxx available to be occupied by the therapeutic antibody,
 29| Rows 7-8:            Show values for background (i.e. non-specific) binding of the labeled detection antibody to the CDxx-expressing cells of interest by using an isotype control belonging to the same immunoglobulin
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:271` (来源: registry B-CP T-4 kb_line_now):

~~~~
 271| **Rows 4-6:** CPTEST, CPBDAGNT, REPNUM, and CPCOLSRT are used the same manner as they are in rows 1-3, except that CPTSTCND is now also used to indicate that the assay was conducted under a saturating condition of CDxx antibody by adding an excess of this therapeutic antibody to the assay system. Under this condition, the labeled detection antibody reflects the maximum (total) amount of CDxx available to be occupied by the therapeutic antibody.
~~~~

### R123. `ig34_p0237_a018` — r2:PDF_TYPO

- PDF 页 237 · 原子类型 SENTENCE · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `writer-Tn-registry` · 批 `B-IS`
- 登记 `B-IS T-5`: PDF 写 "participating a vaccine study" → KB 写 "participating in" (处理: KB 写正确值; 依据: 漏介词, 单值语法补全; KB `knowledge_base/domains/IS/examples.md:153`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In this example, PBMCs were isolated from a subject participating a vaccine study for RSV and restimulated in vitro with either a RSV-antigen or without a stimulating agent. At baseline (i.e., before vaccination), the RSV antigen-stimulated PBMCs produced minimal number of interferon gamma, as expressed in interferon gamma-secreting cells quantified in the number of SFC/10^6 PBMC (row 2), as compared to no stimulation (row 1). Three weeks after vaccination, RSV-antigen stimulated PBMCs (row 4) showed significant increase in the number of interferon-gamma secreting cells compared to no stimulation (row 3) or baseline values (rows 1 and 2). This suggests immunological memory of the immune cells after encountering the same microorganism or its antigens, and the switch of cell state from resting to active.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0237.txt` 第 36-39 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 35| course of the trial and restimulating them with the virus or its viral antigens in vitro.
 36| In this example, PBMCs were isolated from a subject participating a vaccine study for RSV and restimulated in vitro with either a RSV-antigen or without a stimulating agent. At baseline (i.e., before vaccination),
 37| the RSV antigen-stimulated PBMCs produced minimal number of interferon gamma, as expressed in interferon gamma-secreting cells quantified in the number of SFC/10^6 PBMC (row 2), as compared to no
 38| stimulation (row 1). Three weeks after vaccination, RSV-antigen stimulated PBMCs (row 4) showed significant increase in the number of interferon-gamma secreting cells compared to no stimulation (row 3) or
 39| baseline values (rows 1 and 2). This suggests immunological memory of the immune cells after encountering the same microorganism or its antigens, and the switch of cell state from resting to active.
 40| 
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:153` (来源: registry B-IS T-5 kb_line_now):

~~~~
 153| In this example, PBMCs were isolated from a subject participating in a vaccine study for RSV and restimulated in vitro with either a RSV-antigen or without a stimulating agent. At baseline (i.e., before vaccination), the RSV antigen-stimulated PBMCs produced minimal number of interferon gamma, as expressed in interferon gamma-secreting cells quantified in the number of SFC/10^6 PBMC (row 2), as compared to no stimulation (row 1). Three weeks after vaccination, RSV-antigen stimulated PBMCs (row 4) showed significant increase in the number of interferon-gamma secreting cells compared to no stimulation (row 3) or baseline values (rows 1 and 2). This suggests immunological memory of the immune cells after encountering the same microorganism or its antigens, and the switch of cell state from resting to active.
~~~~

### R124. `ig34_p0355_a015` — r2:PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 14 | ABC | TR | 44444 | 14 | TARGET | A2 | T04.2 | DIAMETER | Diameter | 7 | mm | 7 | 7 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 28-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27| 13       ABC   TR      44444    13     TARGET    A2         T04.1    DIAMETER     Diameter      6              mm       6              6        mm                              PHOTOGRAPHY INVESTIGATOR 40      WEEK 6    2010-   48
 28|                                                                                                                                                                                                                            02-20
 29| 14       ABC   TR      44444    14     TARGET    A2         T04.2    DIAMETER     Diameter      7              mm       7              7        mm                              PHOTOGRAPHY INVESTIGATOR 40      WEEK 6    2010-   48
 30|                                                                                                                                                                                                                            02-20
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### R125. `ig34_p0355_a016` — r2:PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 15 | ABC | TR | 44444 | 15 | TARGET | A2 | | SUMDIAM | Sum of Diameter | 30 | mm | 30 | 30 | mm | | | | INVESTIGATOR | 40 | WEEK 6 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 31-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 30|                                                                                                                                                                                                                            02-20
 31| 15       ABC   TR      44444    15     TARGET    A2                  SUMDIAM  Sum of            30             mm       30             30       mm                                          INVESTIGATOR 40      WEEK 6
 32|                                                                               Diameter
 33| 16       ABC   TR      44444    16     TARGET    A2                  SUMNLNLD Sum               18             mm       18             18       mm                                          INVESTIGATOR 40      WEEK 6
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### R126. `ig34_p0355_a018` — r2:PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 17 | ABC | TR | 44444 | 17 | TARGET | A2 | | LNSTATE | Lymph Node State | PATHOLOGICAL | | PATHOLOGICAL | | | | | | INVESTIGATOR | 40 | WEEK 6 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 37-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36|                                                                               Node Tumors
 37| 17       ABC   TR      44444    17     TARGET    A2                  LNSTATE  Lymph Node        PATHOLOGICAL            PATHOLOGICAL                                                        INVESTIGATOR 40      WEEK 6
 38|                                                                               State
 39| 18       ABC   TR      44444    18     TARGET    A2                  ACNSD    Absolute          -32            mm       -32            -32      mm                                          INVESTIGATOR 40      WEEK 6
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### R127. `ig34_p0355_a021` — r2:PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 20 | ABC | TR | 44444 | 20 | TARGET | A2 | | PCNSD | Percent Change Nadir in Sum of Diam | -52 | % | -52 | -52 | % | | | | INVESTIGATOR | 40 | WEEK 6 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 48-51 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 47|                                                                               Diameter
 48| 20       ABC   TR      44444    20     TARGET    A2                  PCNSD    Percent           -52            %        -52            -52      %                                           INVESTIGATOR 40      WEEK 6
 49|                                                                               Change Nadir
 50|                                                                               in Sum of
 51|                                                                               Diam
 52| 21       ABC   TR      44444    21     NON-      A2         NT01     TUMSTATE Tumor State       PRESENT                 PRESENT                                                 CT SCAN     INVESTIGATOR 40      WEEK 6    2010-   46
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### R128. `ig34_p0355_a022` — r2:PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 21 | ABC | TR | 44444 | 21 | NON-TARGET | A2 | NT01 | TUMSTATE | Tumor State | PRESENT | | PRESENT | | | | | CT SCAN | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 52-53 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 51|                                                                               Diam
 52| 21       ABC   TR      44444    21     NON-      A2         NT01     TUMSTATE Tumor State       PRESENT                 PRESENT                                                 CT SCAN     INVESTIGATOR 40      WEEK 6    2010-   46
 53|                                        TARGET                                                                                                                                                                              02-18
 54| 22       ABC   TR      44444    22     NON-      A2         NT02     TUMSTATE     Tumor State   PRESENT                 PRESENT                                                 MRI         INVESTIGATOR 40      WEEK 6    2010-   47
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### R129. `ig34_p0355_a026` — r2:PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 25 | ABC | TR | 44444 | 25 | TARGET | A3 | T03 | DIAMETER | Diameter | | | | | | NOT DONE | SCAN NOT PERFORMED | MRI | INVESTIGATOR | 60 | WEEK 12 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 60-61 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 59|                                                                                                                                                                                                                  12        04-02
 60| 25       ABC   TR      44444    25     TARGET    A3         T03      DIAMETER     Diameter                                                               NOT      SCAN NOT      MRI         INVESTIGATOR 60      WEEK
 61|                                                                                                                                                          DONE     PERFORMED                                      12
 62| 26       ABC   TR      44444    26     TARGET    A3         T04      DIAMETER     Diameter                                                               NOT      NOT           PHOTOGRAPHY INVESTIGATOR 60      WEEK
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### R130. `ig34_p0355_a027` — r2:PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-3`: PDF 写 "POOR IMAGEQUALITY" → KB 写 "POOR IMAGE QUALITY" (处理: KB 写正确值; 依据: 缺空格; KB `knowledge_base/domains/TR/examples.md:43`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 26 | ABC | TR | 44444 | 26 | TARGET | A3 | T04 | DIAMETER | Diameter | | | | | | NOT DONE | NOT ASSESSABLE: | PHOTOGRAPHY | INVESTIGATOR | 60 | WEEK 12 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 62-63 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 61|                                                                                                                                                          DONE     PERFORMED                                      12
 62| 26       ABC   TR      44444    26     TARGET    A3         T04      DIAMETER     Diameter                                                               NOT      NOT           PHOTOGRAPHY INVESTIGATOR 60      WEEK
 63|                                                                                                                                                          DONE     ASSESSABLE:                                    12
 64| 
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:43` (来源: registry B-TR T-3 kb_line_now):

~~~~
  43| | 25 | ABC | TR | 44444 | 25 | TARGET | A3 | T04 | DIAMETER | Diameter | | | | | | NOT DONE | NOT ASSESSABLE: POOR IMAGE QUALITY | PHOTOGRAPHY | INVESTIGATOR | 60 | WEEK 12 | | |
~~~~

### R131. `ig34_p0363_a008` — r2:PDF_TYPO

- PDF 页 363 · 原子类型 LIST_ITEM · 所在节 `§6.4.1 When to Use Findings About Events or Interventions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `writer-Tn-registry` · 批 `B-FA`
- 登记 `B-FA T-5`: PDF 写 "(e.g, When?" → KB 写 "(e.g., When?" (处理: KB 写正确值; 依据: PDF 他处均 e.g.,; KB `knowledge_base/domains/FA/assumptions.md:50`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Is the data item alone in a particular study, but related to other data items likely to be collected in other studies? If so, it may be preferable to represent the item in FA, where other FA variables might be needed for related items in the future. For example, the response to "Was a rechallenge conducted?" might be represented as a supplemental qualifier, but if additional information about the rechallenge (e.g, When?, What was the result?) were collected, then the FA structure would be needed.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0363.txt` 第 19-23 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18|          allows the use of FAGRPID, FACAT, or FASCAT to group the items.
 19|     •    Is the data item alone in a particular study, but related to other data items likely to be collected in other
 20|          studies? If so, it may be preferable to represent the item in FA, where other FA variables might be needed
 21|          for related items in the future. For example, the response to "Was a rechallenge conducted?" might be
 22|          represented as a supplemental qualifier, but if additional information about the rechallenge (e.g, When?,
 23|          What was the result?) were collected, then the FA structure would be needed.
 24|     •    Are there multiple evaluators for a data item that could otherwise be represented as a supplemental
~~~~

KB 现文: `knowledge_base/domains/FA/assumptions.md:50` (来源: registry B-FA T-5 kb_line_now):

~~~~
  50| - Is the data item alone in a particular study, but related to other data items likely to be collected in other studies? If so, it may be preferable to represent the item in FA, where other FA variables might be needed for related items in the future. For example, the response to "Was a rechallenge conducted?" might be represented as a supplemental qualifier, but if additional information about the rechallenge (e.g., When?, What was the result?) were collected, then the FA structure would be needed.
~~~~

### R132. `ig34_p0412_a009` — r2:PDF_TYPO

- PDF 页 412 · 原子类型 SENTENCE · 所在节 `§7.3.2 Trial Disease Assessments (TD) – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `writer-Tn-registry` · 批 `S-TDM`
- 登记 `S-TDM TD T-1`: PDF 写 "assessments.." → KB 写 "单句点" (处理: KB 写正确值; 依据: 双句点排印错; KB `knowledge_base/domains/TD/examples.md:40`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The offset variable (TDSTOFF), used in conjunction with the anchor date variable, provides the start point of each pattern of assessments..
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0412.txt` 第 16-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15| example, there are 3 distinct disease-assessment schedule patterns. A single anchor date variable (TDANCVAR)
 16| provides the anchor date for each pattern. The offset variable (TDSTOFF), used in conjunction with the anchor date
 17| variable, provides the start point of each pattern of assessments..
 18|       •     The first disease-assessment schedule pattern starts at the reference start date (identified in the ADSL
~~~~

KB 现文: `knowledge_base/domains/TD/examples.md:40-40` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  40| This example shows a study where the disease assessment schedule changes over the course of the study. In this example, there are 3 distinct disease-assessment schedule patterns. A single anchor date variable (TDANCVAR) provides the anchor date for each pattern. The offset variable (TDSTOFF), used in conjunction with the anchor date variable, provides the start point of each pattern of assessments.
~~~~

### R133. `ig34_p0414_a006` — r2:PDF_TYPO

- PDF 页 414 · 原子类型 SENTENCE · 所在节 `§7.3.2 Trial Disease Assessments (TD) – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `writer-Tn-registry` · 批 `S-TDM`
- 登记 `S-TDM TD T-2`: PDF 写 "is restarted)." → KB 写 "restarted." (处理: KB 写正确值; 依据: 同句无左括号; KB `knowledge_base/domains/TD/examples.md:153`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
At the start of the extension treatment epoch, subjects are re-baselined, i.e., an extension baseline disease assessment is performed and the disease assessment schedule is restarted).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0414.txt` 第 9-11 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  8| end the standard treatment (e.g., due to disease progression on standard treatment). In the randomized treatment
  9| epoch, the disease assessment schedule changes over the course of the study. At the start of the extension treatment
 10| epoch, subjects are re-baselined, i.e., an extension baseline disease assessment is performed and the disease
 11| assessment schedule is restarted).
 12| In this example, there are 3 distinct disease-assessment schedule patterns:
~~~~

KB 现文: `knowledge_base/domains/TD/examples.md:153-153` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 153| This example shows a study where subjects are randomized to standard treatment or an experimental treatment. The subjects who are randomized to standard treatment are given the option to receive experimental treatment after they end the standard treatment (e.g., due to disease progression on standard treatment). In the randomized treatment epoch, the disease assessment schedule changes over the course of the study. At the start of the extension treatment epoch, subjects are re-baselined, i.e., an extension baseline disease assessment is performed and the disease assessment schedule is restarted.
~~~~

### R134. `ig34_p0436_a022` — r2:PDF_TYPO

- PDF 页 436 · 原子类型 TABLE_ROW · 所在节 `§8.6.3 Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `writer-Tn-registry` · 批 `B-ch08`
- 登记 `B-ch08 T-6`: PDF 写 "may also be coded). (多余右括号)" → KB 写 "may also be coded." (处理: KB 写正确值; 依据: 无对应开括号; KB `knowledge_base/chapters/ch08_relationships.md:328`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Is verbatim text collected and then coded? | • A "Yes" answer suggests that this is Events or Interventions general observation class data. However, Findings general observation class data from an examination (e.g., physical examination) that identifies abnormalities may also be coded). Note that for Events and Interventions general observation class data, the topic variable is coded, whereas for Findings general observation class data, the result is coded.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0436.txt` 第 46-50 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 45|                                  data collection.
 46| Is verbatim text collected and • A “Yes” answer suggests that this is Events or Interventions general observation class data.
 47| then coded?                      However, Findings general observation class data from an examination (e.g., physical
 48|                                  examination) that identifies abnormalities may also be coded). Note that for Events and
 49|                                  Interventions general observation class data, the topic variable is coded, whereas for Findings
 50|                                  general observation class data, the result is coded.
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:328` (来源: registry B-ch08 T-6 kb_line_now):

~~~~
 328| | Is verbatim text collected and then coded? | • A “Yes” answer suggests that this is Events or Interventions general observation class data. However, Findings general observation class data from an examination (e.g., physical examination) that identifies abnormalities may also be coded. Note that for Events and Interventions general observation class data, the topic variable is coded, whereas for Findings general observation class data, the result is coded.<br>• A “No” answer is inconclusive. This does not rule out Events or Interventions general observation class data, because events or interventions are not always collected as verbatim text, but may be prespecified or chosen from a list; it also does not rule out Findings general observation class data. |
~~~~

### R135. `sv20_p0006_a020` — r2:PDF_TYPO

- PDF 页 6 · 原子类型 SENTENCE · 所在节 `§1.4 Significant Changes from Prior Versions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 None) · 判定规则 `writer-Tn-registry` · 批 `B-model01`
- 登记 `B-model01 T-1`: PDF 写 "Section 3, Associated Persons Data" → KB 写 "Section 4" (处理: KB 写正确值; 依据: p5 两处 + p8 均 Section 4; KB `knowledge_base/model/01_concepts_and_terms.md:94`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
It is still listed in Section 3, Associated Persons Data.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0006.txt` 第 36-36 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 35| The variable APID was removed from Section 3.1.4, Identifiers for All Classes, because APID is only allowed in
 36| AP domains. It is still listed in Section 3, Associated Persons Data.
 37| New variables have been added to the following sections:
~~~~

KB 现文: `knowledge_base/model/01_concepts_and_terms.md:94` (来源: registry B-model01 T-1 kb_line_now):

~~~~
  94| The variable APID was removed from Section 3.1.4, Identifiers for All Classes, because APID is only allowed in AP domains. It is still listed in Section 4, Associated Persons Data.
~~~~

