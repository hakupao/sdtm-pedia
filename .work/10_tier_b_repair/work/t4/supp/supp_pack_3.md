# T4.1 补检包 3/8 — TRIAGE_ATOM_ERR (25 条, 全检, 不抽样)

> 由 `scripts/t4/t4_supp_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续.

### 59. `ig34_p0056_a001` — supp:TRIAGE_ATOM_ERR

- PDF 页 56 · 原子类型 SENTENCE · 所在节 `§4.5.3.2 [Text Strings Greater than 200 Characters in Other Variables]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:16375 (lane D pack_028; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The first 200 characters of text should be stored in the variable and separate additional 200 characters of text in supplemental qualifiers.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0056.txt` 第 31-34 行 (自动定位, 词覆盖 0.875; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 30| General Observation Class and          CO.COVAL                            TS.TSVAL                            TI.IETEST and IE.IETEST
 31| Supplemental Qualifier Variables
 32| The first 200 characters of text       The first 200 characters of text    The first 200 characters of text    If the inclusion/exclusion criteria text
 33| should be stored in the variable and   should be stored in COVAL and       should be stored in TSVAL and       is >200 characters, put meaningful
 34| each additional 200 characters of      each additional 200 characters of   each additional 200 characters of   text in IETEST and describe the full
 35| text should be stored as a record in   text should be stored in COVAL1     text should be stored in TSVAL1     text in the study metadata.
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1361` (来源: triage kb_loc knowledge_base/chapters/ch04_general_assumptions.md:1361 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
1359| | 5 | INTP | Interpretation | ABNORMAL | | ABNORMAL | | | | 1 | 2015-03-07 |
1360| | 6 | PRAG | PR Interval, Aggregate | | | | | | NOT DONE | 2 | 2015-03-14 |
1361| | 7 | EGALL | ECG Test Results | | | | | | NOT DONE | 3 | 2015-03-21 |
1362| 
1363| **Example 3**
~~~~

### 60. `ig34_p0057_a002` — supp:TRIAGE_ATOM_ERR

- PDF 页 57 · 原子类型 SENTENCE · 所在节 `§4.5.4 [Evaluators in the Interventions and Events Observation Classes]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:16428 (lane D pack_028; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
See Section 8.4.1, Supplemental Qualifiers—SUPP-- Datasets for additional detail.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0056.txt` 第 50-56 行 (自动定位, 词覆盖 0.917; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 49| which do not include the --EVAL variable, all data are assumed to be attributed to the principal investigator. The
 50| QEVAL variable can be used to describe the evaluator for any data item in a SUPP-- dataset (see Section 8.4.1,
 51| Supplemental Qualifiers – SUPP-- Datasets), but is not required when the data are objective. For observations that
 52| have primary and secondary evaluations of specific qualifier variables, sponsors should put data from the primary
 53| evaluation into the standard domain dataset and data from the secondary evaluation into the Supplemental Qualifier
 54| datasets (SUPP--). Within each SUPP-- record, the value for QNAM should be formed by appending a "1" to the
 55| corresponding standard domain variable name. In cases where the standard domain variable name is already 8
 56| characters in length, sponsors should replace the last character with a "1" (incremented for each additional
 57| attribution).
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1369` (来源: triage kb_loc knowledge_base/chapters/ch04_general_assumptions.md:1369 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
1367| - **Rows 4-5:** Two measurements for VSTESTCD = "SYSBP" were done at visit 1.
1368| - **Row 6:** A third measurement for VSTESTCD = "SYSBP" at visit 1 was a derived record, as indicated by VSDRVFL = "Y".
1369| - **Row 7:** At visit 2, there were no Vital Signs results, as indicated by VSTESTCD = "VSALL" and VSSTAT = "NOT DONE".
1370| 
1371| vs.xpt
~~~~

### 61. `ig34_p0063_a017` — supp:TRIAGE_ATOM_ERR

- PDF 页 63 · 原子类型 TABLE_ROW · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1368 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
AGEU | Age Units | Num | (AGEU) | Variable Qualifier | Units associated with AGE. | Exp
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0063.txt` 第 38-40 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 37|                                       or interval           Qualifier
 38| AGE           Age                Num                        Record      Age expressed in AGEU. May be derived from RFSTDTC and BRTHDTC, but BRTHDTC may not be                            Exp
 39|                                                             Qualifier   available in all cases (due to subject privacy concerns).
 40| AGEU          Age Units            Char (AGEU)              Variable    Units associated with AGE.                                                                                        Exp
 41|                                                             Qualifier
~~~~

KB 现文: `knowledge_base/domains/DM/spec.md:180-183` (来源: near triage kb_loc knowledge_base/domains/DM/spec.md:176 (score 0.889)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 180| - **Controlled Terms:** (AGEU) C66781
 181| - **Role:** Variable Qualifier
 182| - **Core:** Exp
 183| - **CDISC Notes:** Units associated with AGE.
~~~~

### 62. `ig34_p0067_a014` — supp:TRIAGE_ATOM_ERR

- PDF 页 67 · 原子类型 LIST_ITEM · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1746 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
d. RFICIDITC and RFPENDTC: The definitions of this pair of variables are consistent in every study in which they are used.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0067.txt` 第 21-22 行 (自动定位, 词覆盖 0.944; 版式以原 PDF 为准):

~~~~
 20|      last exposure to the challenge agent.
 21| d.   RFICDTC and RFPENDTC: The definitions of this pair of variables are consistent in every study in
 22|      which they are used: They represent the entire period of a subject’s involvement in a study, from
 23|      providing informed consent through the last participation event or activity. There may be times when
~~~~

KB 现文: `knowledge_base/domains/DM/assumptions.md:50-50` (来源: near triage kb_loc knowledge_base/domains/DM/assumptions.md:48 (score 0.944)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  50|     d. RFICDTC and RFPENDTC: The definitions of this pair of variables are consistent in every study in which they are used: They represent the entire period of a subject’s involvement in a study, from providing informed consent through the last participation event or activity. There may be times when this period coincides with other reference periods but that is unusual. An example of when these periods might coincide with the study reference period, RFSTDTC to RFENDTC, might be an observational trial where no study intervention is administered. RFICDTC should correspond to the date of the informed consent protocol milestone in Disposition (DS), if that protocol milestone is documented in DS. In the event that there are multiple informed consents, this will be the date of the first. RFPENDTC will be the last date of participation for a subject for data included in a submission. This should be the last date of any record for the subject in the database at the time it is locked for submission. As such, it may not be the last date of participation in the study if the submission includes interim data.
~~~~

### 63. `ig34_p0068_a017` — supp:TRIAGE_ATOM_ERR

- PDF 页 68 · 原子类型 TABLE_HEADER · 所在节 `§5.2 [DM – Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1759 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
ARMCD Example table with columns: Row, STUDYID, DOMAIN, USUBJID, ARMCD, ARM, ACTARMCD, ACTARM, ARMNRS, ACTARMNRS
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0068.txt` 第 28-36 行 (自动定位, 词覆盖 0.786; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 27| This example Demographics dataset does not include all the DM required and expected variables, only those that illustrate the variables that represent arm information. The following example illustrates values of
 28| ARMCD for subjects in Example Trial 1, described in Section 7.2.1, Trial Arms. This study included 2 elements, screen and run-in, before subjects were randomized to treatment. For this study,
 29| the sponsor submitted data on all subjects, including screen-failure subjects.
 30| Row 1:         Subject 001 was randomized to arm "Drug A". As shown in the SE dataset, this subject completed the "Drug A" element, so their actual arm was also "Drug A".
 31| Row 2:         Subject 002 was randomized to arm "Drug B". As shown in the SE dataset, their actual arm was consistent with their randomization.
 32| Row 3:         Subject 003 was a screen failure, so they were not assigned to an arm or treated. The arm actual arm variables are null, and ARMNRS="SCREEN FAILURE".
 33| Row 4:         Subject 004 withdrew during the run-in element. Like subject 003, they were not assigned to an arm or treated. However, they were not considered a screen failure, and ARMNRS="NOT ASSIGNED".
 34| Row 5:         Subject 005 was randomized but dropped out before being treated. Thus, the actual arm variables are not populated and ARMNRS="ASSIGNED, NOT TREATED".
 35| dm.xpt
 36| Row   STUDYID   DOMAIN    USUBJID   ARMCD ARM    ACTARMCD ACTARM ARMNRS                ACTARMUD
 37| 1     ABC       DM        001       A     Drug A A        Drug A
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:32-32` (来源: near triage kb_loc knowledge_base/domains/DM/examples.md:32 (score 0.643)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  32| | Row | STUDYID | DOMAIN | USUBJID | ARMCD | ARM | ACTARMCD | ACTARM | ARMNRS | ACTARMUD |
~~~~

### 64. `ig34_p0069_a013` — supp:TRIAGE_ATOM_ERR

- PDF 页 69 · 原子类型 TABLE_HEADER · 所在节 `§5.2 [DM – Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1798 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
DM table with columns: Row, STUDYID, DOMAIN, USUBJID, ARMCD, ARM, ACTARMCD, ACTARM, ARMNRS, ACTARMNRS
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 27-32 行 (自动定位, 词覆盖 0.786; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 26|                drug A or the rescue element. Their ARMCD is "A". This case illustrates the exception to the rule that
 27|                ARMCD, ARM, ACTARMCD, and ACTARM must be populated with values from the TA dataset.
 28| Row 3:         Subject "003" was randomized to drug A, but received drug B. At the end of the double-blind
 29|                treatment epoch, they were assigned to rescue treatment. ARMCD shows the result of their
 30|                assignments, "AR"; ACTARMCD shows their actual treatment, "BR".
 31| dm.xpt
 32| Row      STUDYID   DOMAIN   USUBJID     ARMCD    ARM        ACTARMCD   ACTARM   ARMNRS ACTARMUD
 33| 1        DEF       DM       001         AA       A-OPEN A   AA         A-OPEN A
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:74-76` (来源: near triage kb_loc knowledge_base/domains/DM/examples.md:76 (score 0.714)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  74| **dm.xpt**
  75| 
  76| | Row | STUDYID | DOMAIN | USUBJID | ARMCD | ARM | ACTARMCD | ACTARM | ARMNRS | ACTARMUD |
~~~~

### 65. `ig34_p0069_a023` — supp:TRIAGE_ATOM_ERR

- PDF 页 69 · 原子类型 TABLE_ROW · 所在节 `§5.2 [DM – Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1811 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
1 | ABC | SE | 001 | 1 | SCRN | Screen | 2006-01-07 | 2006-01-12
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 8-8 行 (自动定位, 词覆盖 0.9; 版式以原 PDF 为准):

~~~~
  7| Row      STUDYID   DOMAIN     USUBJID    SESEQ    ETCD   ELEMENT    SESTDTC        SEENDTC
  8| 1        ABC       SE         001        1        SCRN   Screen     2006-06-01     2006-06-07
  9| 2        ABC       SE         001        2        RI     Run-In     2006-06-07     2006-06-21
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:94-94` (来源: near triage kb_loc knowledge_base/domains/DM/examples.md:94 (score 0.9)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  94| | 1 | DEF | SE | 001 | 1 | SCRN | Screen | 2006-01-07 | 2006-01-12 |
~~~~

### 66. `ig34_p0069_a024` — supp:TRIAGE_ATOM_ERR

- PDF 页 69 · 原子类型 TABLE_ROW · 所在节 `§5.2 [DM – Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1824 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
2 | ABC | SE | 001 | 2 | DBA | Treatment A | 2006-01-12 | 2006-06-21
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 5-10 行 (自动定位, 词覆盖 0.833; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  4| Rows 8-9:      Subject 004 withdrew during the "Run-in" element, before they could be randomized.
  5| Rows 10-11: Subject 005 withdrew after they were randomized, but did not start treatment.
  6| se.xpt
  7| Row      STUDYID   DOMAIN     USUBJID    SESEQ    ETCD   ELEMENT    SESTDTC        SEENDTC
  8| 1        ABC       SE         001        1        SCRN   Screen     2006-06-01     2006-06-07
  9| 2        ABC       SE         001        2        RI     Run-In     2006-06-07     2006-06-21
 10| 3        ABC       SE         001        3        A      Drug A     2006-06-21     2006-07-05
 11| 4        ABC       SE         002        1        SCRN   Screen     2006-05-03     2006-05-10
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:95-100` (来源: near triage kb_loc knowledge_base/domains/DM/examples.md:95 (score 0.833)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  95| | 2 | DEF | SE | 001 | 2 | DBA | Treatment A | 2006-01-12 | 2006-04-10 |
  96| | 3 | DEF | SE | 001 | 3 | OA | Open Drug A | 2006-04-10 | 2006-07-05 |
  97| | 4 | DEF | SE | 002 | 1 | SCRN | Screen | 2006-02-03 | 2006-02-10 |
  98| | 5 | DEF | SE | 002 | 2 | DBA | Treatment A | 2006-02-10 | 2006-03-24 |
  99| | 6 | DEF | SE | 003 | 1 | SCRN | Screen | 2006-02-22 | 2006-03-01 |
 100| | 7 | DEF | SE | 003 | 2 | DBB | Treatment B | 2006-03-01 | 2006-06-27 |
~~~~

### 67. `ig34_p0069_a025` — supp:TRIAGE_ATOM_ERR

- PDF 页 69 · 原子类型 TABLE_ROW · 所在节 `§5.2 [DM – Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1837 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
3 | ABC | SE | 001 | 3 | OA | Drug A | 2006-06-21 | 2006-07-05
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 10-10 行 (自动定位, 词覆盖 0.917; 版式以原 PDF 为准):

~~~~
  9| 2        ABC       SE         001        2        RI     Run-In     2006-06-07     2006-06-21
 10| 3        ABC       SE         001        3        A      Drug A     2006-06-21     2006-07-05
 11| 4        ABC       SE         002        1        SCRN   Screen     2006-05-03     2006-05-10
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:96-100` (来源: near triage kb_loc knowledge_base/domains/DM/examples.md:96 (score 0.833)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  96| | 3 | DEF | SE | 001 | 3 | OA | Open Drug A | 2006-04-10 | 2006-07-05 |
  97| | 4 | DEF | SE | 002 | 1 | SCRN | Screen | 2006-02-03 | 2006-02-10 |
  98| | 5 | DEF | SE | 002 | 2 | DBA | Treatment A | 2006-02-10 | 2006-03-24 |
  99| | 6 | DEF | SE | 003 | 1 | SCRN | Screen | 2006-02-22 | 2006-03-01 |
 100| | 7 | DEF | SE | 003 | 2 | DBB | Treatment B | 2006-03-01 | 2006-06-27 |
~~~~

### 68. `ig34_p0069_a027` — supp:TRIAGE_ATOM_ERR

- PDF 页 69 · 原子类型 TABLE_ROW · 所在节 `§5.2 [DM – Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1850 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
5 | ABC | SE | 002 | 2 | DBA | Treatment A | 2006-05-10 | 2006-05-24
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 46-48 行 (自动定位, 词覆盖 0.917; 版式以原 PDF 为准):

~~~~
 45| 2        DEF         SE         001         2         DBA      Treatment A       2006-01-12     2006-04-10
 46| 3        DEF         SE         001         3         OA       Open Drug A       2006-04-10     2006-07-05
 47| 4        DEF         SE         002         1         SCRN     Screen            2006-02-03     2006-02-10
 48| 5        DEF         SE         002         2         DBA      Treatment A       2006-02-10     2006-03-24
 49| 6        DEF         SE         003         1         SCRN     Screen            2006-02-22     2006-03-01
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:96-98` (来源: near triage kb_loc knowledge_base/domains/DM/examples.md:98 (score 0.917)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  96| | 3 | DEF | SE | 001 | 3 | OA | Open Drug A | 2006-04-10 | 2006-07-05 |
  97| | 4 | DEF | SE | 002 | 1 | SCRN | Screen | 2006-02-03 | 2006-02-10 |
  98| | 5 | DEF | SE | 002 | 2 | DBA | Treatment A | 2006-02-10 | 2006-03-24 |
~~~~

### 69. `ig34_p0069_a029` — supp:TRIAGE_ATOM_ERR

- PDF 页 69 · 原子类型 TABLE_ROW · 所在节 `§5.2 [DM – Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1863 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
7 | ABC | SE | 003 | 1 | SCRN | Screen | 2006-05-27 | 2006-06-30
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 13-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12| 5        ABC       SE         002        2        RI     Run-In     2006-05-10     2006-05-24
 13| 6        ABC       SE         002        3        B      Drug B     2006-05-24     2006-06-07
 14| 7        ABC       SE         003        1        SCRN   Screen     2006-06-27     2006-06-30
 15| 8        ABC       SE         004        1        SCRN   Screen     2006-05-14     2006-05-21
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:59-60` (来源: near triage kb_loc knowledge_base/domains/DM/examples.md:60 (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  59| | 6 | ABC | SE | 002 | 3 | B | Drug B | 2006-05-24 | 2006-06-07 |
  60| | 7 | ABC | SE | 003 | 1 | SCRN | Screen | 2006-06-27 | 2006-06-30 |
~~~~

### 70. `ig34_p0069_a030` — supp:TRIAGE_ATOM_ERR

- PDF 页 69 · 原子类型 TABLE_ROW · 所在节 `§5.2 [DM – Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1876 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
8 | ABC | SE | 004 | 2 | RI | Run-in | 2006-05-21 | 2006-05-26
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 15-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14| 7        ABC       SE         003        1        SCRN   Screen     2006-06-27     2006-06-30
 15| 8        ABC       SE         004        1        SCRN   Screen     2006-05-14     2006-05-21
 16| 9        ABC       SE         004        2        RI     Run-In     2006-05-21     2006-05-26
 17| 10       ABC       SE         005        1        SCRN   Screen     2006-05-14     2006-05-21
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:61-62` (来源: near triage kb_loc knowledge_base/domains/DM/examples.md:62 (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  61| | 8 | ABC | SE | 004 | 1 | SCRN | Screen | 2006-05-14 | 2006-05-21 |
  62| | 9 | ABC | SE | 004 | 2 | RI | Run-In | 2006-05-21 | 2006-05-26 |
~~~~

### 71. `ig34_p0069_a031` — supp:TRIAGE_ATOM_ERR

- PDF 页 69 · 原子类型 TABLE_ROW · 所在节 `§5.2 [DM – Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1889 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
9 | ABC | SE | 004 | 2 | RI | Run-in | 2006-05-14 | 2006-05-26
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 15-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14| 7        ABC       SE         003        1        SCRN   Screen     2006-06-27     2006-06-30
 15| 8        ABC       SE         004        1        SCRN   Screen     2006-05-14     2006-05-21
 16| 9        ABC       SE         004        2        RI     Run-In     2006-05-21     2006-05-26
 17| 10       ABC       SE         005        1        SCRN   Screen     2006-05-14     2006-05-21
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:61-62` (来源: near triage kb_loc knowledge_base/domains/DM/examples.md:62 (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  61| | 8 | ABC | SE | 004 | 1 | SCRN | Screen | 2006-05-14 | 2006-05-21 |
  62| | 9 | ABC | SE | 004 | 2 | RI | Run-In | 2006-05-21 | 2006-05-26 |
~~~~

### 72. `ig34_p0069_a032` — supp:TRIAGE_ATOM_ERR

- PDF 页 69 · 原子类型 TABLE_ROW · 所在节 `§5.2 [DM – Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1902 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
10 | ABC | SE | 004 | 1 | RI | Run-in | 2006-05-14 | 2006-05-26
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 16-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15| 8        ABC       SE         004        1        SCRN   Screen     2006-05-14     2006-05-21
 16| 9        ABC       SE         004        2        RI     Run-In     2006-05-21     2006-05-26
 17| 10       ABC       SE         005        1        SCRN   Screen     2006-05-14     2006-05-21
 18| 11       ABC       SE         005        2        RI     Run-In     2006-05-21     2006-05-26
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:62-63` (来源: near triage kb_loc knowledge_base/domains/DM/examples.md:63 (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  62| | 9 | ABC | SE | 004 | 2 | RI | Run-In | 2006-05-21 | 2006-05-26 |
  63| | 10 | ABC | SE | 005 | 1 | SCRN | Screen | 2006-05-14 | 2006-05-21 |
~~~~

### 73. `ig34_p0070_a022` — supp:TRIAGE_ATOM_ERR

- PDF 页 70 · 原子类型 NOTE · 所在节 `§5.2 [DM – Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:1967 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
For each value that applies, SUPPQUAL where SUPPQUAL.QNAM = "<RACEC" and SUPPQUAL.QLABEL is the choice value.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0070.txt` 第 3-5 行 (自动定位, 词覆盖 0.357; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  2| The CRF in this example is annotated to show the CDASH variable name and the target SDTMIG variable. Data
  3| that are collected using the same variable name as defined in the SDTMIG are in RED . If the CDASHIG variable
  4| differs from the one defined in the SDTMIG, the CDASHIG variable is in GREY .
  5| See the CDASH Model and Implementation Guide for additional
  6| information: https://www.cdisc.org/standards/foundational/cdash.
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:188-188` (来源: near triage kb_loc knowledge_base/domains/DM/examples.md:179 (score 0.929)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 188| | CRACE01-CRACE04 | 10 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "AMERICAN INDIAN OR ALASKA NATIVE". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ALASKA NATIVE; AMERICAN INDIAN; CARIBBEAN INDIAN; CENTRAL AMERICAN INDIAN; | | | checkbox | |
~~~~

### 74. `ig34_p0077_a015` — supp:TRIAGE_ATOM_ERR

- PDF 页 77 · 原子类型 TABLE_HEADER · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:2071 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
suppdm.xpt | Row | STUDYID | DOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QORIG | QEVAL
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0078.txt` 第 4-5 行 (自动定位, 词覆盖 0.917; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  3| Row 3:         Shows USUBJID ABC789-010-003 selected "BLACK" as the specific BLACK OR AFRICAN AMERICAN race collected.
  4| suppdm.xpt
  5| Row   STUDYID      RDOMAIN   USUBJID          IDVAR IDVARVAL     QNAM       QLABEL             QVAL               QORIG   QEVAL
  6| 1     ABC789       DM        ABC789-010-001                      CRACE3     Collected Race 3   JAPANESE           CRF
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:350` (来源: triage kb_loc knowledge_base/domains/DM/examples.md:350 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 348| **Row 1:** Shows that USUBJID ABC789-010-001 designated 1 race, "ASIAN", as the value that best describes their race.
 349| 
 350| **Row 2:** Shows that USUBJID ABC789-010-002 designated 1 race, "BLACK OR AFRICAN AMERICAN", as the value that best describes their race.
 351| 
 352| **Row 3:** Shows that USUBJID ABC789-010-003 designated 1 race, "BLACK OR AFRICAN AMERICAN", as the value that best describes their race.
~~~~

### 75. `ig34_p0078_a007` — supp:TRIAGE_ATOM_ERR

- PDF 页 78 · 原子类型 TABLE_HEADER · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:2084 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
suppdm.xpt | Row | STUDYID | DOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QORIG | QEVAL
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0078.txt` 第 4-5 行 (自动定位, 词覆盖 0.917; 版式以原 PDF 为准):

~~~~
  3| Row 3:         Shows USUBJID ABC789-010-003 selected "BLACK" as the specific BLACK OR AFRICAN AMERICAN race collected.
  4| suppdm.xpt
  5| Row   STUDYID      RDOMAIN   USUBJID          IDVAR IDVARVAL     QNAM       QLABEL             QVAL               QORIG   QEVAL
  6| 1     ABC789       DM        ABC789-010-001                      CRACE3     Collected Race 3   JAPANESE           CRF
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:426` (来源: triage kb_loc knowledge_base/domains/DM/examples.md:426 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 424| 
 425| **Rows 1-2:** Subjects self-identify to 1 of the first 5 race options on the CRF form.
 426| 
 427| **Row 3:** Subject did not self-identify to 1 of the existing race options and selected "Other". RACE was populated with "OTHER" in this case.
 428| 
~~~~

### 76. `ig34_p0078_a021` — supp:TRIAGE_ATOM_ERR

- PDF 页 78 · 原子类型 TABLE_ROW · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 ERROR) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:2097 (lane A pack_004; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
3 | ABC789 | DM | ABC789-010-047 | 010-047 | 24 | YEARS | M | OTHER | HISPANIC OR LATINO
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0078.txt` 第 25-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24| 2        ABC789     DM         ABC789-010-046      010-046   21     YEARS      F      ASIAN         NOT HISPANIC OR LATINO
 25| 3        ABC789     DM         ABC789-010-047      010-047   24     YEARS      F      OTHER         HISPANIC OR LATINO
 26| 3        ABC789     DM         ABC789-010-048      010-048   33     YEARS      M      UNKNOWN       HISPANIC OR LATINO
 27| 
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:415` (来源: triage kb_loc knowledge_base/domains/DM/examples.md:415 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 413| 
 414| > KB note (not in SDTMIG): The CRF presents 5 racial designations plus "Unknown" and "Other" options:
 415| > - American Indian or Alaska Native
 416| > - Asian
 417| > - Black or African American
~~~~

### 77. `ig34_p0080_a002` — supp:TRIAGE_ATOM_ERR

- PDF 页 80 · 原子类型 TABLE_ROW · 所在节 `§5.3 [Subject Elements]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:19045 (lane D pack_033; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
ELEMENT | Description of Element | Char | * | Synonym Qualifier | The name of the element. If ETCD has a value of "UNPLAN", the value for ELEMENT would be as specified in the Comment Concepts) section after a comment in the CRF.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0080.txt` 第 4-9 行 (自动定位, 词覆盖 0.72; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  3| ETCD           Element Code           Char *                        Topic               1. ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special               Req
  4|                                                                                            character restrictions. These values should be short for ease of use in programming, but it is
  5|                                                                                            not expected that ETCD will need to serve as a variable name.
  6|                                                                                        2.  If an encountered element differs from the planned element to the point that it is considered a
  7|                                                                                            new element, then use "UNPLAN" as the value for ETCD to represent this element.
  8| ELEMENT        Description of         Char *                        Synonym       The name of the element. If ETCD has a value of "UNPLAN", then ELEMENT should be null.                      Perm
  9|                Element                                              Qualifier
 10| TAETORD        Planned Order of       Num                           Timing        Number that gives the planned order of the element within the subject's assigned trial arm.                 Perm
~~~~

KB 现文: `knowledge_base/domains/SE/spec.md:48-53` (来源: near triage kb_loc knowledge_base/domains/SE/spec.md:50 (score 0.6)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  48| - **CDISC Notes:** 1. ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name.  2. If an encountered element differs from the planned element to the point that it is considered a new element, then use "UNPLAN" as the value for ETCD to represent this element.
  49| 
  50| ### ELEMENT
  51| - **Order:** 6
  52| - **Label:** Description of Element
  53| - **Type:** Char
~~~~

### 78. `ig34_p0101_a011` — supp:TRIAGE_ATOM_ERR

- PDF 页 101 · 原子类型 SENTENCE · 所在节 `§6.1.2 [Concomitant/Prior Medications (CM)]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 MISPLACED) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:9352 (lane B pack_017; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
CMENDC could be used to indicate that the use is unknown/has not yet happened.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0101.txt` 第 2-11 行 (自动定位, 词覆盖 0.867; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  1|                 b.    CMOCCUR is used to indicate whether a prespecified medication was used. A value of "Y" indicates that the medication was used and "N"
  2|                       indicates that it was not.
  3|                 c.    If a medication was not prespecified, the value of CMOCCUR should be null. CMPRESP and CMOCCUR are permissible fields and may be
  4|                       omitted from the dataset if all medications were collected as free text. Values of CMOCCUR may also be null for prespecified medications if
  5|                       no Y/N response was collected; in such cases, CMSTAT = "NOT DONE", and CMREASND could be used to describe the reason the answer
  6|                       was missing.
  7|       4.   Variables for timing relative to a time point
  8|            a.   CMSTRTPT, CMSTTPT, CMENRTPT, and CMENTPT may be populated as necessary to indicate when a medication was used relative to
  9|                 specified time points. For example, assume a subject uses birth control medication. The subject has used the same medication for many years and
 10|                 continues to do so. The date the subject began using the medication (or at least a partial date) would be stored in CMSTDTC. CMENDTC is null
 11|                 because the end date is unknown/has not yet happened. This fact can be recorded by setting CMENTPT = "2007-04-30" (the date the assessment
 12|                 was made) and CMENRTPT = "ONGOING".
~~~~

KB 现文: `knowledge_base/domains/CM/assumptions.md:23-27` (来源: near triage kb_loc knowledge_base/domains/CM/assumptions.md:27 (score 0.867)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  23|    b. CMOCCUR is used to indicate whether a prespecified medication was used. A value of "Y" indicates that the medication was used and "N" indicates that it was not.
  24|    c. If a medication was not prespecified, the value of CMOCCUR should be null. CMPRESP and CMOCCUR are permissible fields and may be omitted from the dataset if all medications were collected as free text. Values of CMOCCUR may also be null for prespecified medications if no Y/N response was collected; in such cases, CMSTAT = "NOT DONE", and CMREASND could be used to describe the reason the answer was missing.
  25| 
  26| 4. Variables for timing relative to a time point
  27|    a. CMSTRTPT, CMSTTPT, CMENRTPT, and CMENTPT may be populated as necessary to indicate when a medication was used relative to specified time points. For example, assume a subject uses birth control medication. The subject has used the same medication for many years and continues to do so. The date the subject began using the medication (or at least a partial date) would be stored in CMSTDTC. CMENDTC is null because the end date is unknown/has not yet happened. This fact can be recorded by setting CMENTPT = "2007-04-30" (the date the assessment was made) and CMENRTPT = "ONGOING".
~~~~

### 79. `ig34_p0112_a009` — supp:TRIAGE_ATOM_ERR

- PDF 页 112 · 原子类型 TABLE_HEADER · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 MISPLACED) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:6978 (lane B pack_013; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[Field] | [Value]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0112.txt` 第 ? 行 (自动定位, 词覆盖 0; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
(未定位, 请直接看该页)
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:65` (来源: triage kb_loc knowledge_base/domains/EX/examples.md:65 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  63| This example shows data from an open-label study. A subject received drug X as a 20 mg/mL solution administered across 3 injection sites to deliver a total dose of 3 mg/kg. The subject's weight was 100 kg.
  64| 
  65| **Exposure CRF**
  66| 
  67| | | |
~~~~

### 80. `ig34_p0116_a009` — supp:TRIAGE_ATOM_ERR

- PDF 页 116 · 原子类型 TABLE_HEADER · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:7004 (lane B pack_013; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECTRT | ECPREP | ECOCCUR | ECDOSE | ECDOSEU | ECDOSFRM | ECDOSFRQ | ECROUTE | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY | ECTPT | ECELTM | ECTRREF |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0116.txt` 第 11-11 行 (自动定位, 词覆盖 0.857; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 10| ec.xpt
 11| Row STUDYID DOMAIN USUBJID ECSEQ ECTRT                 ECPRESP ECOCCUR ECDOSE ECDOSU                  ECDOSFRM          ECDOSFRQ ECROUTE EPOCH       ECSTDTC    ECENDTC    ECSTDY ECENDY ECTPT        ECELTM ECTPTREF
 12| 1   56789   EC     56789001 1    BOTTLE                Y       Y       1      CAPSULE                 CAPSULE           QD       ORAL    TREATMENT   2002-07-   2002-07-   1      1      30 MINUTES   -PT30M STD
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:265-265` (来源: near triage kb_loc knowledge_base/domains/EX/examples.md:265 (score 0.857)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 265| | Row | STUDYID | DOMAIN | USUBJID | ECSEQ | ECTRT | ECPRESP | ECOCCUR | ECDOSE | ECDOSU | ECDOSFRM | ECDOSFRQ | ECROUTE | EPOCH | ECSTDTC | ECENDTC | ECSTDY | ECENDY | ECTPT | ECELTM | ECTPTREF |
~~~~

### 81. `ig34_p0116_a010` — supp:TRIAGE_ATOM_ERR

- PDF 页 116 · 原子类型 TABLE_ROW · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:7017 (lane B pack_013; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | 56789 | EC | 56789001 | 1 | BOTTLE | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT | 2002-07-01T07:30 | 2002-07-01T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0116.txt` 第 14-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13|                                  1                                                                                                       1           01T07:30   01T07:30                 PRIOR               BREAKFAST
 14| 2   56789   EC     56789001 2    BOTTLE                Y         Y         1       TABLET,            TABLET,           QD       ORAL    TREATMENT   2002-07-   2002-07-   1      1      30 MINUTES   -PT30M STD
 15|                                  2                                                 COATED             COATED                             1           01T07:30   01T07:30                 PRIOR               BREAKFAST
 16| 3   56789   EC     56789001 3    BOTTLE                Y         Y         1       CAPSULE            CAPSULE           QD       ORAL    TREATMENT   2002-07-   2002-07-   2      2      30 MINUTES   -PT30M STD
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:268-268` (来源: near triage kb_loc knowledge_base/domains/EX/examples.md:267 (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 268| | 2 | 56789 | EC | 56789001 | 2 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-01T07:30 | 2002-07-01T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
~~~~

### 82. `ig34_p0116_a012` — supp:TRIAGE_ATOM_ERR

- PDF 页 116 · 原子类型 TABLE_ROW · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:7043 (lane B pack_013; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | 56789 | EC | 56789001 | 3 | BOTTLE | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT | 2002-07-01T07:30 | 2002-07-01T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0116.txt` 第 14-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13|                                  1                                                                                                       1           01T07:30   01T07:30                 PRIOR               BREAKFAST
 14| 2   56789   EC     56789001 2    BOTTLE                Y         Y         1       TABLET,            TABLET,           QD       ORAL    TREATMENT   2002-07-   2002-07-   1      1      30 MINUTES   -PT30M STD
 15|                                  2                                                 COATED             COATED                             1           01T07:30   01T07:30                 PRIOR               BREAKFAST
 16| 3   56789   EC     56789001 3    BOTTLE                Y         Y         1       CAPSULE            CAPSULE           QD       ORAL    TREATMENT   2002-07-   2002-07-   2      2      30 MINUTES   -PT30M STD
 17|                                  1                                                                                                       1           02T07:30   02T07:30                 PRIOR               BREAKFAST
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:268-269` (来源: near triage kb_loc knowledge_base/domains/EX/examples.md:269 (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 268| | 2 | 56789 | EC | 56789001 | 2 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-01T07:30 | 2002-07-01T07:30 | 1 | 1 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
 269| | 3 | 56789 | EC | 56789001 | 3 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-02T07:30 | 2002-07-02T07:30 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
~~~~

### 83. `ig34_p0116_a014` — supp:TRIAGE_ATOM_ERR

- PDF 页 116 · 原子类型 TABLE_ROW · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:7069 (lane B pack_013; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 5 | 56789 | EC | 56789001 | 5 | BOTTLE | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT | 2002-07-02T07:30 | 2002-07-02T07:30 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0116.txt` 第 18-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17|                                  1                                                                                                       1           02T07:30   02T07:30                 PRIOR               BREAKFAST
 18| 4   56789   EC     56789001 4    BOTTLE                Y         Y         1       TABLET,            TABLET,           QD       ORAL    TREATMENT   2002-07-   2002-07-   2      2      30 MINUTES   -PT30M STD
 19|                                  2                                                 COATED             COATED                             1           02T07:30   02T07:30                 PRIOR               BREAKFAST
 20| 5   56789   EC     56789001 5    BOTTLE                Y         Y         1       CAPSULE            CAPSULE           QD       ORAL    TREATMENT   2002-07-   2002-07-   3      3      30 MINUTES   -PT30M STD
 21|                                  1                                                                                                       1           03T07:32   03T07:32                 PRIOR               BREAKFAST
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:270-271` (来源: near triage kb_loc knowledge_base/domains/EX/examples.md:271 (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 270| | 4 | 56789 | EC | 56789001 | 4 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-02T07:30 | 2002-07-02T07:30 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
 271| | 5 | 56789 | EC | 56789001 | 5 | BOTTLE 1 | Y | Y | 1 | CAPSULE | CAPSULE | QD | ORAL | TREATMENT 1 | 2002-07-03T07:32 | 2002-07-03T07:32 | 3 | 3 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
~~~~

