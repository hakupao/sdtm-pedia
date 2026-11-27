# T4.1 第三轮补检包 10 — R3_PDF_TYPO (24 条; 编号 T226-T249)

> 由 `scripts/t4/t4_round3_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 T).

### T226. `ig34_p0355_a017` — r3:R3_PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 16 | ABC | TR | 44444 | 16 | TARGET | A2 | | SUMNLNLD | Sum Diameters of Non Lymph Node Tumors | 18 | mm | 18 | 18 | mm | | | | INVESTIGATOR | 40 | WEEK 6 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 33-36 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 32|                                                                               Diameter
 33| 16       ABC   TR      44444    16     TARGET    A2                  SUMNLNLD Sum               18             mm       18             18       mm                                          INVESTIGATOR 40      WEEK 6
 34|                                                                               Diameters of
 35|                                                                               Non Lymph
 36|                                                                               Node Tumors
 37| 17       ABC   TR      44444    17     TARGET    A2                  LNSTATE  Lymph Node        PATHOLOGICAL            PATHOLOGICAL                                                        INVESTIGATOR 40      WEEK 6
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### T227. `ig34_p0355_a019` — r3:R3_PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 18 | ABC | TR | 44444 | 18 | TARGET | A2 | | ACNSD | Absolute Change Nadir in Sum of Diam | -32 | mm | -32 | -32 | mm | | | | INVESTIGATOR | 40 | WEEK 6 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 39-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 38|                                                                               State
 39| 18       ABC   TR      44444    18     TARGET    A2                  ACNSD    Absolute          -32            mm       -32            -32      mm                                          INVESTIGATOR 40      WEEK 6
 40|                                                                               Change Nadir
 41|                                                                               in Sum of
 42|                                                                               Diam
 43| 19       ABC   TR      44444    19     TARGET    A2                  PCBSD    Percent           -52            %        -52            -52      %                                           INVESTIGATOR 40      WEEK 6
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### T228. `ig34_p0355_a020` — r3:R3_PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 19 | ABC | TR | 44444 | 19 | TARGET | A2 | | PCBSD | Percent Change From Baseline in Sum of Diameter | -52 | % | -52 | -52 | % | | | | INVESTIGATOR | 40 | WEEK 6 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 43-47 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 42|                                                                               Diam
 43| 19       ABC   TR      44444    19     TARGET    A2                  PCBSD    Percent           -52            %        -52            -52      %                                           INVESTIGATOR 40      WEEK 6
 44|                                                                               Change From
 45|                                                                               Baseline in
 46|                                                                               Sum of
 47|                                                                               Diameter
 48| 20       ABC   TR      44444    20     TARGET    A2                  PCNSD    Percent           -52            %        -52            -52      %                                           INVESTIGATOR 40      WEEK 6
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### T229. `ig34_p0355_a023` — r3:R3_PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 22 | ABC | TR | 44444 | 22 | NON-TARGET | A2 | NT02 | TUMSTATE | Tumor State | PRESENT | | PRESENT | | | | | MRI | INVESTIGATOR | 40 | WEEK 6 | 2010-02-19 | 47 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 54-55 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 53|                                        TARGET                                                                                                                                                                              02-18
 54| 22       ABC   TR      44444    22     NON-      A2         NT02     TUMSTATE     Tumor State   PRESENT                 PRESENT                                                 MRI         INVESTIGATOR 40      WEEK 6    2010-   47
 55|                                        TARGET                                                                                                                                                                              02-19
 56| 23       ABC   TR      44444    23     TARGET    A3         T01      DIAMETER     Diameter      0              mm       0              0        mm                              CT SCAN     INVESTIGATOR 60      WEEK      2010-   88
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### T230. `ig34_p0355_a024` — r3:R3_PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 23 | ABC | TR | 44444 | 23 | TARGET | A3 | T01 | DIAMETER | Diameter | 0 | mm | 0 | 0 | mm | | | CT SCAN | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 56-57 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 55|                                        TARGET                                                                                                                                                                              02-19
 56| 23       ABC   TR      44444    23     TARGET    A3         T01      DIAMETER     Diameter      0              mm       0              0        mm                              CT SCAN     INVESTIGATOR 60      WEEK      2010-   88
 57|                                                                                                                                                                                                                  12        04-02
 58| 24       ABC   TR      44444    24     TARGET    A3         T02      DIAMETER     Diameter      6              mm       6              6        mm                              CT SCAN     INVESTIGATOR 60      WEEK      2010-   88
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### T231. `ig34_p0355_a025` — r3:R3_PDF_TYPO

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 24 | ABC | TR | 44444 | 24 | TARGET | A3 | T02 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | CT SCAN | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 57-58 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 56| 23       ABC   TR      44444    23     TARGET    A3         T01      DIAMETER     Diameter      0              mm       0              0        mm                              CT SCAN     INVESTIGATOR 60      WEEK      2010-   88
 57|                                                                                                                                                                                                                  12        04-02
 58| 24       ABC   TR      44444    24     TARGET    A3         T02      DIAMETER     Diameter      6              mm       6              6        mm                              CT SCAN     INVESTIGATOR 60      WEEK      2010-   88
 59|                                                                                                                                                                                                                  12        04-02
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### T232. `ig34_p0356_a001` — r3:R3_PDF_TYPO

- PDF 页 356 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `K3b-registry` · 批 `B-TR`
- 登记 `B-TR T-3`: PDF 写 "POOR IMAGEQUALITY" → KB 写 "POOR IMAGE QUALITY" (处理: KB 写正确值; 依据: 缺空格; KB `knowledge_base/domains/TR/examples.md:43`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 27 | ABC | TR | 44444 | 27 | NON-TARGET | A3 | NT01 | TUMSTATE | Tumor State | | | | | | | POOR IMAGEQUALITY | CT SCAN | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0356.txt` 第 2-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| Row STUDYID DOMAIN USUBJID TRSEQ TRGRPID            TRLNKGRP TRLNKID TRTESTCD      TRTEST        TRORRES        TRORRESU TRSTRESC     TRSTRESN TRSTRESU TRSTAT   TRREASND       TRMETHOD      TREVAL        VISITNUM VISIT    TRDTC   TRDY
  2|                                                                                                                                                                  POOR
  3|                                                                                                                                                                  IMAGEQUALITY
  4| 27       ABC   TR      44444      27       NON-     A3       NT01      TUMSTATE    Tumor State                                                                                  CT SCAN       INVESTIGATOR 60        WEEK     2010-   88
  5|                                            TARGET                                                                                                                                                                    12       04-02
  6| 28       ABC   TR      44444      28       NON-     A3       NT02      TUMSTATE    Tumor State                                                          NOT      SCAN NOT       MRI           INVESTIGATOR 60        WEEK
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:43` (来源: registry B-TR T-3 kb_line_now):

~~~~
  43| | 25 | ABC | TR | 44444 | 25 | TARGET | A3 | T04 | DIAMETER | Diameter | | | | | | NOT DONE | NOT ASSESSABLE: POOR IMAGE QUALITY | PHOTOGRAPHY | INVESTIGATOR | 60 | WEEK 12 | | |
~~~~

### T233. `ig34_p0356_a002` — r3:R3_PDF_TYPO

- PDF 页 356 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- 登记 `B-TR T-1`: PDF 写 "Ex2 Row/TRSEQ 跳 12 (16 行×2 格)" → KB 写 "连续 1-27" (处理: KB 写正确值; 依据: 叙述 Rows 9-21/22-27 与连续编号一致; KB `knowledge_base/domains/TR/examples.md:30`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 28 | ABC | TR | 44444 | 28 | NON-TARGET | A3 | NT02 | TUMSTATE | Tumor State | | | | | | | NOT DONE | SCAN NOT PERFORMED | MRI | INVESTIGATOR | 60 | WEEK 12 | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0356.txt` 第 6-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5|                                            TARGET                                                                                                                                                                    12       04-02
  6| 28       ABC   TR      44444      28       NON-     A3       NT02      TUMSTATE    Tumor State                                                          NOT      SCAN NOT       MRI           INVESTIGATOR 60        WEEK
  7|                                            TARGET                                                                                                       DONE     PERFORMED                                           12
  8| 
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### T234. `ig34_p0362_a010` — r3:R3_PDF_TYPO

- PDF 页 362 · 原子类型 SENTENCE · 所在节 `§6.4.1 When to Use Findings About Events or Interventions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-FA`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 后依据变更: KB 按 U-7 A3-7 写正确值 'thought to be related' (= 原子), PDF p362 'thought be related' → R2 PDF_TYPO (主控决定 2026-11-27). 原 basis: B-FA audit: 原子抽错; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-FA_audit.md:36`
- 登记 `B-FA T-4`: PDF 写 "thought be related" → KB 写 "thought to be related" (处理: KB 写正确值; 依据: 漏词 (语法); KB `knowledge_base/domains/FA/assumptions.md:39`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Previous versions of the SDTMIG included the criterion, "Data or information about an Event or Intervention that indicate the occurrence of related symptoms or therapies." This criterion has been removed because information about related symptoms or therapies is more appropriately represented as information about those symptoms or therapies rather than as information about the event or intervention to which they are thought to be related. Data about related symptoms or interventions should be evaluated against the above Criterion 1 - 3 to determine whether they should be represented in an FA dataset. If data do not meet one of the criteria above, they should be represented in
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0362.txt` 第 47-52 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 46| recorded in medical history or adverse events CRFs.
 47| Previous versions of the SDTMIG included the criterion, "Data or information about an Event or Intervention that
 48| indicate the occurrence of related symptoms or therapies." This criterion has been removed because information
 49| about related symptoms or therapies is more appropriately represented as information about those symptoms or
 50| therapies rather than as information about the event or intervention to which they are thought be related. Data about
 51| related symptoms or interventions should be evaluated against the above Criterion 1 - 3 to determine whether they
 52| should be represented in an FA dataset. If data do not meet one of the criteria above, they should be represented in
~~~~

KB 现文: `knowledge_base/domains/FA/assumptions.md:39` (来源: decision.evidence.hit):

~~~~
  39| Previous versions of the SDTMIG included the criterion, "Data or information about an Event or Intervention that indicate the occurrence of related symptoms or therapies." This criterion has been removed because information about related symptoms or therapies is more appropriately represented as information about those symptoms or therapies rather than as information about the event or intervention to which they are thought to be related. Data about related symptoms or interventions should be evaluated against the above Criterion 1 - 3 to determine whether they should be represented in an FA dataset. If data do not meet one of the criteria above, they should be represented in an event or interventions record. If data do meet criteria to be represented in the findings about structure, FAOBJ will be the name of the symptom. The relationship to the disease under study may be represented in FACAT or FASCAT, as in FA Example 5.
~~~~

### T235. `ig34_p0363_a009` — r3:R3_PDF_TYPO

- PDF 页 363 · 原子类型 LIST_ITEM · 所在节 `§6.4.1 When to Use Findings About Events or Interventions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-FA`
- 登记 `B-FA T-6`: PDF 写 "FA may provided" → KB 写 "FA may provide" (处理: KB 写正确值; 依据: 语法类; KB `knowledge_base/domains/FA/assumptions.md:51`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Are there multiple evaluators for a data item that could otherwise be represented as a supplemental qualifier? If so, FA may provided a clearer representation of the multiple opinions, and would also allow the use of FAEVALID.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0363.txt` 第 24-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 23|          What was the result?) were collected, then the FA structure would be needed.
 24|     •    Are there multiple evaluators for a data item that could otherwise be represented as a supplemental
 25|          qualifier? If so, FA may provided a clearer representation of the multiple opinions, and would also allow
 26|          the use of FAEVALID.
 27| 
~~~~

KB 现文: `knowledge_base/domains/FA/assumptions.md:51` (来源: registry B-FA T-6 kb_line_now):

~~~~
  51| - Are there multiple evaluators for a data item that could otherwise be represented as a supplemental qualifier? If so, FA may provide a clearer representation of the multiple opinions, and would also allow the use of FAEVALID.
~~~~

### T236. `ig34_p0377_a015` — r3:R3_PDF_TYPO

- PDF 页 377 · 原子类型 TABLE_ROW · 所在节 `SR – Specification`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `S1-R2` · 批 `B-SR`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-SR T-4: verbatim EGTPTREF 为 PDF 笔误, KB 改 SRTPTREF; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-SR.md:116`
- 登记 `B-SR T-4`: PDF 写 "indicated by EGTPTREF" → KB 写 "SRTPTREF" (处理: KB 写正确值; 依据: 同表 SR 前缀; 同注释第二例; KB `knowledge_base/domains/SR/spec.md:336`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| SRELTM | Planned Elapsed Time from Time Point Ref | Char | ISO 8601 duration | Timing | Planned elapsed time (in ISO 8601) relative to a fixed time point reference (SRTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by SRTPTREF. | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0377.txt` 第 34-37 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 33|                 Number
 34| SRELTM          Planned Elapsed Time        Char ISO 8601 duration      Timing        Planned elapsed time (in ISO 8601) relative to a fixed time point reference (SRTPTREF). Not a clock Perm
 35|                 from Time Point Ref                                                   time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent
 36|                                                                                       the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the
 37|                                                                                       period of 8 hours after the reference point indicated by SRTPTREF.
 38| SRTPTREF        Time Point Reference        Char                        Timing        Name of the fixed reference point referred to by SRELTM, SRTPTNUM, and SRTPT. Example:               Perm
~~~~

KB 现文: `knowledge_base/domains/SR/spec.md:336` (来源: registry B-SR T-4 kb_line_now):

~~~~
 336| - **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a fixed time point reference (SRTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by SRTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by SRTPTREF.
~~~~

### T237. `ig34_p0412_a006` — r3:R3_PDF_TYPO

- PDF 页 412 · 原子类型 SENTENCE · 所在节 `§7.3.2 Trial Disease Assessments (TD) – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `S-TDM`
- 登记 `S-TDM TD T-1`: PDF 写 "assessments.." → KB 写 "单句点" (处理: KB 写正确值; 依据: 双句点排印错; KB `knowledge_base/domains/TD/examples.md:40`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example shows a study where the disease assessment schedule changes over the course of the study.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0412.txt` 第 14-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13| 
 14| This example shows a study where the disease assessment schedule changes over the course of the study. In this
 15| example, there are 3 distinct disease-assessment schedule patterns. A single anchor date variable (TDANCVAR)
~~~~

KB 现文: `knowledge_base/domains/TD/examples.md:40` (来源: decision.evidence.hit):

~~~~
  40| This example shows a study where the disease assessment schedule changes over the course of the study. In this example, there are 3 distinct disease-assessment schedule patterns. A single anchor date variable (TDANCVAR) provides the anchor date for each pattern. The offset variable (TDSTOFF), used in conjunction with the anchor date variable, provides the start point of each pattern of assessments.
~~~~

### T238. `ig34_p0412_a007` — r3:R3_PDF_TYPO

- PDF 页 412 · 原子类型 SENTENCE · 所在节 `§7.3.2 Trial Disease Assessments (TD) – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `S-TDM`
- 登记 `S-TDM TD T-1`: PDF 写 "assessments.." → KB 写 "单句点" (处理: KB 写正确值; 依据: 双句点排印错; KB `knowledge_base/domains/TD/examples.md:40`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In this example, there are 3 distinct disease-assessment schedule patterns.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0412.txt` 第 14-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13| 
 14| This example shows a study where the disease assessment schedule changes over the course of the study. In this
 15| example, there are 3 distinct disease-assessment schedule patterns. A single anchor date variable (TDANCVAR)
 16| provides the anchor date for each pattern. The offset variable (TDSTOFF), used in conjunction with the anchor date
~~~~

KB 现文: `knowledge_base/domains/TD/examples.md:40` (来源: decision.evidence.hit):

~~~~
  40| This example shows a study where the disease assessment schedule changes over the course of the study. In this example, there are 3 distinct disease-assessment schedule patterns. A single anchor date variable (TDANCVAR) provides the anchor date for each pattern. The offset variable (TDSTOFF), used in conjunction with the anchor date variable, provides the start point of each pattern of assessments.
~~~~

### T239. `ig34_p0412_a008` — r3:R3_PDF_TYPO

- PDF 页 412 · 原子类型 SENTENCE · 所在节 `§7.3.2 Trial Disease Assessments (TD) – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `S-TDM`
- 登记 `S-TDM TD T-1`: PDF 写 "assessments.." → KB 写 "单句点" (处理: KB 写正确值; 依据: 双句点排印错; KB `knowledge_base/domains/TD/examples.md:40`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
A single anchor date variable (TDANCVAR) provides the anchor date for each pattern.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0412.txt` 第 15-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14| This example shows a study where the disease assessment schedule changes over the course of the study. In this
 15| example, there are 3 distinct disease-assessment schedule patterns. A single anchor date variable (TDANCVAR)
 16| provides the anchor date for each pattern. The offset variable (TDSTOFF), used in conjunction with the anchor date
 17| variable, provides the start point of each pattern of assessments..
~~~~

KB 现文: `knowledge_base/domains/TD/examples.md:40` (来源: decision.evidence.hit):

~~~~
  40| This example shows a study where the disease assessment schedule changes over the course of the study. In this example, there are 3 distinct disease-assessment schedule patterns. A single anchor date variable (TDANCVAR) provides the anchor date for each pattern. The offset variable (TDSTOFF), used in conjunction with the anchor date variable, provides the start point of each pattern of assessments.
~~~~

### T240. `ig34_p0413_a010` — r3:R3_PDF_TYPO

- PDF 页 413 · 原子类型 TABLE_HEADER · 所在节 `§7.3.2 Trial Disease Assessments (TD) – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `S-TDM`
- 登记 `S-TDM TD T-4`: PDF 写 "Ex3 表头 TDTGPAI" → KB 写 "TDTGTPAI" (处理: KB 写正确值; 依据: spec + Ex1/Ex2 表头; KB `knowledge_base/domains/TD/examples.md:167`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0413.txt` 第 21-21 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 20| td.xpt
 21| Row STUDYID DOMAIN TDORDER TDANCVAR TDSTOFF TDTGTPAI TDMINPAI TDMAXPAI TDNUMRPT
 22| 1   ABC123  TD     1       ANCH1DT  P0D     P8W      P53D     P9W      6
~~~~

KB 现文: `knowledge_base/domains/TD/examples.md:50,102,167` (来源: decision.evidence.hit):

> 同一文件共 3 处逐字命中 (行 50, 102, 167); 请按 PDF 所在例/表判断对应的是哪一处

~~~~
  50| | Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT |
 102| | Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT |
 167| | Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT |
~~~~

### T241. `ig34_p0414_a008` — r3:R3_PDF_TYPO

- PDF 页 414 · 原子类型 LIST_ITEM · 所在节 `§7.3.2 Trial Disease Assessments (TD) – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `writer-Tn-registry` · 批 `S-TDM`
- 登记 `S-TDM TD T-3`: PDF 写 "( i.e., week 8" → KB 写 "(i.e., week 8" (处理: KB 写正确值; 依据: 同节 (i.e., 无空格; KB `knowledge_base/domains/TD/examples.md:157`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The first disease-assessment schedule pattern starts at the reference start date (identified in the ADSL ANCH1DT variable) and repeats every 8 weeks for a total of 6 repeats ( i.e., week 8, week 16, week 24, week 32, week 40, week 48), with respective upper and lower limits of - 3 days and + 1 week.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0414.txt` 第 13-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12| In this example, there are 3 distinct disease-assessment schedule patterns:
 13|       •     The first disease-assessment schedule pattern starts at the reference start date (identified in the ADSL
 14|             ANCH1DT variable) and repeats every 8 weeks for a total of 6 repeats ( i.e., week 8, week 16, week 24,
 15|             week 32, week 40, week 48), with respective upper and lower limits of - 3 days and + 1 week.
 16|       •     The second disease assessment schedule starts from week 48 and repeats every 12 weeks (week 60,
~~~~

KB 现文: `knowledge_base/domains/TD/examples.md:157-157` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 157| - The first disease-assessment schedule pattern starts at the reference start date (identified in the ADSL ANCH1DT variable) and repeats every 8 weeks for a total of 6 repeats (i.e., week 8, week 16, week 24, week 32, week 40, week 48), with respective upper and lower limits of - 3 days and + 1 week.
~~~~

### T242. `ig34_p0419_a013` — r3:R3_PDF_TYPO

- PDF 页 419 · 原子类型 TABLE_ROW · 所在节 `§7.4.2 Trial Summary (TS) – Assumptions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `B-TS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-5 B-TS T-3 DOSFREQ→DOSFRQ | errata: t3_atom_err | new_target: domains/TS/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:119`
- 登记 `B-TS T-3`: PDF 写 "DOSFREQ" → KB 写 "DOSFRQ (TSPARMCD CT C89081; 叙述 + 表 2 格共 3 处)" (处理: KB 写正确值; 依据: 两处互异; KB `knowledge_base/domains/TS/assumptions.md:43`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
2 | B | DOSFREQ | Dosing Frequency | Q24H
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0419.txt` 第 24-24 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 23|      2                     B                     DOSE                   Dose per Administration   100
 24|      2                     B                     DOSFREQ                Dosing Frequency          Q24H
 25|      1                                           DOSU                   Dose Units                mg
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:43` (来源: registry B-TS T-3 kb_line_now):

~~~~
  43|     For example, if a trial compared administration of a total daily dose given once a day to that dose split over 2 administrations, the TS dataset might include the following records. There are 2 records each for TSPARMCD = "DOSE" and TSPARMCD = "DOSFRQ". Records with the same TSGRPID are associated with each other. In this example, dose units are the same for both administration schedules, so only 1 record for DOSU is needed.
~~~~

### T243. `ig34_p0425_a024` — r3:R3_PDF_TYPO

- PDF 页 425 · 原子类型 SENTENCE · 所在节 `§7.4.2.1 Use of Null Flavor`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-TS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-7 B-TS T-6 MAXAGE→AGEMAX | errata: t3_atom_err | new_target: domains/TS/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:121`
- 登记 `B-TS T-6`: PDF 写 "MAXAGE case" → KB 写 "AGEMAX (TSPARMCD CT C49694)" (处理: KB 写正确值; 依据: PDF 内不一致; KB `knowledge_base/domains/TS/assumptions.md:115`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
For example, for the MAXAGE case that provided the impetus for the creation of the TSVALNF variable, the value PINF means that there is information about the maximum age, but it is not something that can be expressed, as in the ISO8601 quantity of time format required for populating TSVAL.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0425.txt` 第 29-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28| to be represented in the primary piece of data).
 29| The values at levels 3 and 4 provide successively more information about the situation. For example, for the
 30| MAXAGE case that provided the impetus for the creation of the TSVALNF variable, the value PINF means that
 31| there is information about the maximum age, but it is not something that can be expressed, as in the ISO8601
 32| quantity of time format required for populating TSVAL. The null flavor PINF provides the most complete
 33| information possible in this case (i.e., that the maximum age for the study is unbounded).
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:115` (来源: registry B-TS T-6 kb_line_now):

~~~~
 115| The values at levels 3 and 4 provide successively more information about the situation. For example, for the AGEMAX case that provided the impetus for the creation of the TSVALNF variable, the value PINF means that there is information about the maximum age, but it is not something that can be expressed, as in the ISO8601 quantity of time format required for populating TSVAL. The null flavor PINF provides the most complete information possible in this case (i.e., that the maximum age for the study is unbounded).
~~~~

### T244. `ig34_p0428_a006` — r3:R3_PDF_TYPO

- PDF 页 428 · 原子类型 LIST_ITEM · 所在节 `§8.1.1 --GRPID Example`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-ch08`
- 登记 `B-ch08 T-2`: PDF 写 "GMGRPID ×2" → KB 写 "CMGRPID" (处理: KB 写正确值; 依据: 同段/表头; KB `knowledge_base/chapters/ch08_relationships.md:36`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-3: Show 3 medications taken by subject 1234. GMGRPID="COMBO THPY 1" has been used to group these medications.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0428.txt` 第 20-21 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19| This example illustrates how CMGRPID groups information only within a subject within a domain.
 20| Rows 1-3:      Show 3 medications taken by subject 1234. GMGRPID="COMBO THPY 1" has been used to group
 21|                these medications.
 22| Rows 4-6:      Show 3 different medications taken by subject 1234, with CMGRPID="COMBO THPY 2".
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:36` (来源: registry B-ch08 T-2 kb_line_now):

~~~~
  36| **Rows 1-3:** Show 3 medications taken by subject 1234. CMGRPID="COMBO THPY 1" has been used to group these medications.
~~~~

### T245. `ig34_p0428_a008` — r3:R3_PDF_TYPO

- PDF 页 428 · 原子类型 LIST_ITEM · 所在节 `§8.1.1 --GRPID Example`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-ch08`
- 登记 `B-ch08 T-2`: PDF 写 "GMGRPID ×2" → KB 写 "CMGRPID" (处理: KB 写正确值; 依据: 同段/表头; KB `knowledge_base/chapters/ch08_relationships.md:36`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 7-9: Show 3 medications taken by subject 5678. CMGRPID="COMBO THPY 1" has been used to group these medications. Note that the medications with GMGRPID "COMBO THPY 1" are completely different for subjects 1234 and 5678.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0428.txt` 第 23-25 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 22| Rows 4-6:      Show 3 different medications taken by subject 1234, with CMGRPID="COMBO THPY 2".
 23| Rows 7-9:      Show 3 medications taken by subject 5678. CMGRPID="COMBO THPY 1" has been used to group
 24|                these medications. Note that the medications with GMGRPID "COMBO THPY 1" are completely
 25|                different for subjects 1234 and 5678.
 26| Rows 10-12: Show 3 different medications taken by subject 5678, with CMGRPID=“COMBO THPY 2”. Again,
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:36` (来源: registry B-ch08 T-2 kb_line_now):

~~~~
  36| **Rows 1-3:** Show 3 medications taken by subject 1234. CMGRPID="COMBO THPY 1" has been used to group these medications.
~~~~

### T246. `ig34_p0433_a017` — r3:R3_PDF_TYPO

- PDF 页 433 · 原子类型 SENTENCE · 所在节 `§8.4.2 Submitting Supplemental Qualifiers in Separate Datasets`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `writer-Tn-registry` · 批 `B-ch08`
- 登记 `B-ch08 T-3`: PDF 写 "SQAPFAMH. (括号未闭合)" → KB 写 "SQAPFAMH)." (处理: KB 写正确值; 依据: 同句开括号; KB `knowledge_base/chapters/ch08_relationships.md:224`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In this case only, the “SUPP” portion should be shortened to “SQ” (e.g., resulting in the dataset name SQAPFAMH.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0433.txt` 第 24-25 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 23| be represented (see the SDTMIG for Associated Persons, https://www.cdisc.org/standards/foundational/sdtmig/). A
 24| dataset name with the SUPP fragment (e.g., SUPPAPFAMH) would be too long. In this case only, the “SUPP”
 25| portion should be shortened to “SQ” (e.g., resulting in the dataset name SQAPFAMH.
 26| 
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:224` (来源: registry B-ch08 T-3 kb_line_now):

~~~~
 224| There is a one-to-one correspondence between a domain dataset and its Supplemental Qualifier dataset. The single SUPPQUAL dataset option that was introduced in SDTMIG v3.1 was deprecated. The set of supplemental qualifiers for each domain is included in a separate dataset with the name SUPP-- (where "--" denotes the source domain which the supplemental qualifiers relate back to). For example, Demographics (DM) qualifiers would be submitted in suppdm.xpt. When data have been split into multiple datasets (see Section 4.1.7, Splitting Domains), longer names such as SUPPFAMH may be needed. In cases where data about associated persons have been collected, supplemental qualifiers for Findings About events or interventions for an associated person may need to be represented (see the SDTMIG for Associated Persons, https://www.cdisc.org/standards/foundational/sdtmig/). A dataset name with the SUPP fragment (e.g., SUPPAPFAMH) would be too long. In this case only, the “SUPP” portion should be shortened to “SQ” (e.g., resulting in the dataset name SQAPFAMH).
~~~~

### T247. `ig34_p0433_a019` — r3:R3_PDF_TYPO

- PDF 页 433 · 原子类型 SENTENCE · 所在节 `§8.4.3 SUPP-- Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-ch08`
- 登记 `B-ch08 T-4`: PDF 写 "llustrate" → KB 写 "illustrate" (处理: KB 写正确值; 依据: 拼写; KB `knowledge_base/chapters/ch08_relationships.md:228`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
These examples llustrate how a set of SUPP-- datasets could be used to relate non-standard information to a parent domain.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0433.txt` 第 28-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27| 8.4.3 SUPP-- Examples
 28| These examples llustrate how a set of SUPP-- datasets could be used to relate non-standard information to a parent
 29| domain.
 30| Example 1
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:228` (来源: registry B-ch08 T-4 kb_line_now):

~~~~
 228| These examples illustrate how a set of SUPP-- datasets could be used to relate non-standard information to a parent domain.
~~~~

### T248. `ig34_p0438_a019` — r3:R3_PDF_TYPO

- PDF 页 438 · 原子类型 LIST_ITEM · 所在节 `RELSUB – Assumptions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `B-REL`
- 登记 `B-REL T-9 (RELSUB 副本)`: PDF 写 "asm 7 句末无句号" → KB 写 "补句号" (处理: KB 写正确值; 依据: 同列表其余项均句号; KB `knowledge_base/domains/RELSUB/assumptions.md:29`)
- 登记 `B-ch08 T-9 (ch08 副本)`: PDF 写 "RELSUB asm 7 句末无句号" → KB 写 "补句号" (处理: KB 写正确值; 依据: 同列表其余项; KB `knowledge_base/chapters/ch08_relationships.md:373`)
- 登记 `B-REL T-9 (RELSUB 副本)`: PDF 写 "asm 7 句末无句号" → KB 写 "补句号" (处理: KB 写正确值; 依据: 同列表其余项均句号; KB `knowledge_base/domains/RELSUB/assumptions.md:29`)
- 登记 `B-ch08 T-9 (ch08 副本)`: PDF 写 "RELSUB asm 7 句末无句号" → KB 写 "补句号" (处理: KB 写正确值; 依据: 同列表其余项; KB `knowledge_base/chapters/ch08_relationships.md:373`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
7.    Every relationship between 2 study subjects is represented in RELSUB as 2 directional relationships: (1) with the first subject's identifier in USUBJID and the second subject's identifier in RSUBJID, and (2) with the second subject's identifier in USUBJID and the first subject's identifier in RSUBJID. The SREL values in the 2 records will describe the same relationship, but from the viewpoint of each subject (e.g., "MOTHER, BIOLOGICAL"; "CHILD, BIOLOGICAL")
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0438.txt` 第 45-49 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 44|            relationship was "brother".
 45|      7.    Every relationship between 2 study subjects is represented in RELSUB as 2 directional relationships: (1)
 46|            with the first subject's identifier in USUBJID and the second subject's identifier in RSUBJID, and (2) with
 47|            the second subject's identifier in USUBJID and the first subject's identifier in RSUBJID. The SREL values
 48|            in the 2 records will describe the same relationship, but from the viewpoint of each subject (e.g.,
 49|            "MOTHER, BIOLOGICAL"; "CHILD, BIOLOGICAL")
 50|      8.    All collected relationships between subjects should be recorded in RELSUB. In some cases, 2 subjects may
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:373` (来源: decision.evidence.hit):

~~~~
 373| 7. Every relationship between 2 study subjects is represented in RELSUB as 2 directional relationships: (1) with the first subject's identifier in USUBJID and the second subject's identifier in RSUBJID, and (2) with the second subject's identifier in USUBJID and the first subject's identifier in RSUBJID. The SREL values in the 2 records will describe the same relationship, but from the viewpoint of each subject (e.g., "MOTHER, BIOLOGICAL"; "CHILD, BIOLOGICAL").
~~~~

### T249. `ig34_p0457_a004` — r3:R3_PDF_TYPO

- PDF 页 457 · 原子类型 TABLE_ROW · 所在节 `§10.E Appendix E: Revision History`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `S-CH10`
- 登记 `S-CH10 T-2`: PDF 写 "--TETM" → KB 写 "--TERM" (处理: KB 写正确值; 依据: 同句 --TRT/--DECOD Topic 变量; KB `knowledge_base/chapters/ch10_appendices.md:387`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
6.4.3 | Variables Unique to Findings About Events or Interventions | Added a sentence to state that an FA record will not necessarily have a parent record, to make it clear that the information about FAOBJ matching --TETM, --TRT, or --DECOD is not meant to imply that an FA record must have a parent record.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0457.txt` 第 27-31 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26|                                                      guidance on how these situations should be approached were added.
 27| 6.4.3     Variables Unique to Findings About       • Added a sentence to state that an FA record will not necessarily have
 28|                                                      a parent record, to make it clear that the information about FAOBJ
 29|                                                      matching --TETM, --TRT, or --DECOD is not meant to imply that an
 30|                                                      FA record must have a parent record.
 31| 6.4.4     Findings About Events or Interventions   • The core value for FADTC was changed from "Perm" to "Exp" for
 32|           (FA)                                       consistency with other Findings domains.
~~~~

KB 现文: `knowledge_base/chapters/ch10_appendices.md:387` (来源: registry S-CH10 T-2 kb_line_now):

~~~~
 387| | 6.4.3 | Variables Unique to Findings About | • Added a sentence to state that an FA record will not necessarily have a parent record, to make it clear that the information about FAOBJ matching --TERM, --TRT, or --DECOD is not meant to imply that an FA record must have a parent record. |
~~~~

