# T4.1 第三轮补检包 7 — R3_PDF_TYPO (25 条; 编号 T151-T175)

> 由 `scripts/t4/t4_round3_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 T).

### T151. `ig34_p0010_a023` — r3:R3_PDF_TYPO

- PDF 页 10 · 原子类型 SENTENCE · 所在节 `§1.5 [Known Issues]`
- triage 类 **REAL_GAP** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `S1-R2` · 批 `B-ch01`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-ch01 T-2: --LNKID/--LNKGRP 对调; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-ch01.md:26`
- 登记 `B-ch01 T-2`: PDF 写 "MANY → --LNKID (and not --LNKGRP)" → KB 写 "--LNKGRP (and not --LNKID)" (处理: KB 写正确值; 依据: 同段前句 + p31 §4 定义, 两名对调; KB `knowledge_base/chapters/ch01_introduction.md:109`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This implies that when setting up a relationship in RELREC, a row where RELTYPE = ONE will have an IDVAR of --LNKID (and not --LNKGRP); a row where RELTYPE = MANY will have an IDVAR of --LNKID (and not --LNKGRP).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0010.txt` 第 37-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36| The definition of --LNKID says that it is "used to identify a record," and the definition of --LNKGRP says that it is
 37| "used to identify a group of records." This implies that when setting up a relationship in RELREC, a row where
 38| RELTYPE = ONE will have an IDVAR of --LNKID (and not --LNKGRP); a row where RELTYPE = MANY will
 39| have an IDVAR of --LNKID (and not --LNKGRP). The examples in this version of the SDTMIG have not been
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:109` (来源: registry B-ch01 T-2 kb_line_now):

~~~~
 109| The definition of --LNKID says that it is "used to identify a record," and the definition of --LNKGRP says that it is "used to identify a group of records." This implies that when setting up a relationship in RELREC, a row where RELTYPE = ONE will have an IDVAR of --LNKID (and not --LNKGRP); a row where RELTYPE = MANY will have an IDVAR of --LNKGRP (and not --LNKID). The examples in this version of the SDTMIG have not been systematically reviewed to implement this distinction between --LNKID and --LNKGRP. This distinction between --LNKID and --LNKGRP, and the appropriateness of using other identification variables for linking, will be clarified in a future release of the SDTMIG and/or Model document, and at that time examples in the SDTMIG will be systematically reviewed and updated to reflect that clarification.
~~~~

### T152. `ig34_p0018_a012` — r3:R3_PDF_TYPO

- PDF 页 18 · 原子类型 TABLE_ROW · 所在节 `§3.2.1 Dataset-level Metadata`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-ch03`
- 登记 `B-ch03 T-1`: PDF 写 "BE Keys BESDTC" → KB 写 "BESTDTC" (处理: KB 写正确值; 依据: 全书仅 p18; BE 节均 BESTDTC; KB `knowledge_base/chapters/ch03_submitting_data.md:37`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
BE | Biospecimen Events | Events | One record per instance per biospecimen event per biospecimen identifier per subject | Tabulation | STUDYID, USUBJID, BEREFID, BETERM, BESDTC | be.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0018.txt` 第 14-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13|                                               subject                                        AEDECOD, AESTDTC
 14| BE        Biospecimen Events    Events        One record per instance per         Tabulation STUDYID, USUBJID,     be.xpt
 15|                                               biospecimen event per biospecimen              BEREFID, BETERM,
 16|                                               identifier per subject                         BESDTC
 17| CE        Clinical Events       Events        One record per event per subject    Tabulation STUDYID, USUBJID,     ce.xpt
~~~~

KB 现文: `knowledge_base/chapters/ch03_submitting_data.md:37` (来源: registry B-ch03 T-1 kb_line_now):

~~~~
  37| | BE | Biospecimen Events | Events | One record per instance per biospecimen event per biospecimen identifier per subject | Tabulation | STUDYID, USUBJID, BEREFID, BETERM, BESTDTC | be.xpt |
~~~~

### T153. `ig34_p0041_a038` — r3:R3_PDF_TYPO

- PDF 页 41 · 原子类型 SENTENCE · 所在节 `§4.4.3.2 [Interval with Uncertainty]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-ch04`
- 登记 `B-ch04 N-1`: PDF 写 "solidus or foreword slash [/]" → KB 写 "forward slash" (处理: KB 写正确值; 依据: PDF 拼写 foreword (应 forward), 照录; KB `knowledge_base/chapters/ch04_general_assumptions.md:863`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
where the start date/time is represented before the solidus or foreword slash [/], the "Pn..." following the solidus represents a "duration," and the entire representation is known as an "interval."
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0041.txt` 第 37-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36|                                   YYYY-MM-DDThh:mm:ss/PnYnMnDTnHnMnS
 37| where the start date/time is represented before the solidus or foreword slash [/], the "Pn…" following the solidus
 38| represents a "duration," and the entire representation is known as an "interval." Note that this is the recommended
 39| representation of elapsed time, given a start date/time and the duration elapsed.
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:863` (来源: registry B-ch04 N-1 kb_line_now):

~~~~
 863| where the start date/time is represented before the solidus or forward slash [/], the "Pn…" following the solidus represents a "duration," and the entire representation is known as an "interval." Note that this is the recommended representation of elapsed time, given a start date/time and the duration elapsed.
~~~~

### T154. `ig34_p0063_a023` — r3:R3_PDF_TYPO

- PDF 页 63 · 原子类型 TABLE_ROW · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **IE** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `K3b-registry` · 批 `S-SPEC1`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: -
- 登记 `S-SPEC1 T-1`: PDF 写 "ETHNIC Notes FDA guidance¹" → KB 写 "guidance²" (处理: KB 写正确值; 依据: 脚注² 才是 FDA guidance; RACE 用 ²; KB `knowledge_base/domains/DM/spec.md:210`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
ETHNIC | Ethnicity | Char | (ETHNIC) | Record Qualifier | The ethnicity of the subject. Sponsors should refer to the FDA guidance1 regarding the collection of ethnicity. | Perm
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0063.txt` 第 45-46 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 44| RACE          Race                 Char (RACE)              Record      Race of the subject. Sponsors should refer to the FDA guidance2 regarding the collection of race. See             Exp
 45|                                                             Qualifier   assumption below regarding RACE.
 46| ETHNIC        Ethnicity            Char (ETHNIC)            Record      The ethnicity of the subject. Sponsors should refer to the FDA guidance1 regarding the collection of ethnicity.   Perm
 47|                                                             Qualifier
~~~~

KB 现文: `knowledge_base/domains/DM/spec.md:210` (来源: registry S-SPEC1 T-1 kb_line_now):

~~~~
 210| - **CDISC Notes:** The ethnicity of the subject. Sponsors should refer to the FDA guidance² regarding the collection of ethnicity.
~~~~

### T155. `ig34_p0068_a010` — r3:R3_PDF_TYPO

- PDF 页 68 · 原子类型 TABLE_ROW · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-DM`
- 登记 `B-DM T-2`: PDF 写 "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDERS" → KB 写 "…PACIFIC ISLANDER" (处理: KB 写正确值; 依据: PDF Ex4/Ex6 RACE CT 值 …ISLANDER; KB `knowledge_base/domains/DM/examples.md:14`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
6 | ABC123 | DM | ABC1230002 | 0202 | 2006-02-02 | 2006-04-05 | 2006-02-02 | 2006-04-25 | 02 | GONZALEZ, MARIA | 1966-04-05 | 49 | YEARS | F | NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER | NOT HISPANIC OR LATINO | Drug A | A | Drug A | | USA
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0068.txt` 第 20-23 行 (自动定位, 词覆盖 0.821; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 19|                                                                                                                                                               NATIVE
 20| 6     ABC123   DM      ABC12302002 02002   2006-02-   2006-04-   2006-02-03   2006-04-05   2006-01-   2006-04-25   02   GONZALEZ,   1956-05-   49   YEARS F   NATIVE        NOT         A      Drug A   A        Drug A                       USA
 21|                                            03         05                                   10                           E           05                        HAWAIIAN OR   HISPANIC
 22|                                                                                                                                                               OTHER         OR LATINO
 23|                                                                                                                                                               PACIFIC
 24|                                                                                                                                                               ISLANDERS
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:14` (来源: registry B-DM T-2 kb_line_now):

~~~~
  14| | 6 | ABC123 | DM | ABC12302002 | 02002 | 2006-02-03 | 2006-04-05 | 2006-02-03 | 2006-04-05 | 2006-01-10 | 2006-04-25 | 02 | GONZALEZ, E | 1956-05-05 | 49 | YEARS | F | NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER | NOT HISPANIC OR LATINO | A | Drug A | A | Drug A | | | USA |
~~~~

### T156. `ig34_p0089_a026` — r3:R3_PDF_TYPO

- PDF 页 89 · 原子类型 LIST_ITEM · 所在节 `§5.5 [Subject Visits (SV)]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-SV`
- 登记 `B-SV T-1`: PDF 写 "Row 5 句末无句点" → KB 写 "补句点" (处理: KB 写正确值; 依据: 同组 Row 说明均句点; KB `knowledge_base/domains/SV/examples.md:40`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 5: Shows informed consent for subject 101
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0089.txt` 第 29-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28| Row 4:            Shows that subject 85 completed the study.
 29| Row 5:            Shows informed consent for subject 101
 30| Row 6:            Shows that subject 101 chose to withdraw early.
~~~~

KB 现文: `knowledge_base/domains/SV/examples.md:40` (来源: decision.evidence.hit):

~~~~
  40| **Row 5:** Shows informed consent for subject 101.
~~~~

### T157. `ig34_p0107_a002` — r3:R3_PDF_TYPO

- PDF 页 107 · 原子类型 LIST_ITEM · 所在节 `§6.1.3.1 [Exposure (EX)]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `S-INT`
- 登记 `S-INT EX T-7`: PDF 写 "…document.Additional interventions qualifiers (并入下条标题)" → KB 写 "…Define-XML document." (处理: KB 写正确值; 依据: 下一行即 6. 标题, 重复排版错; KB `knowledge_base/domains/EX/assumptions.md:41`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Collected exposure data points are to be represented in the Exposure as Collected (EC) domain. When the relationship between EC and EX records can be described in RELREC, then it should be defined. EX derivations must be described in the Define-XML document.Additional interventions qualifiers
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0107.txt` 第 3-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2|                collected, EXSTDTC should be copied to EXENDTC as the standard representation.
  3|      5.   Collected exposure data points are to be represented in the Exposure as Collected (EC) domain. When the relationship between EC and EX records can
  4|           be described in RELREC, then it should be defined. EX derivations must be described in the Define-XML document.Additional interventions qualifiers
  5|      6.   Additional interventions qualifiers
~~~~

KB 现文: `knowledge_base/domains/EX/assumptions.md:41-43` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  41| 5. Collected exposure data points are to be represented in the Exposure as Collected (EC) domain. When the relationship between EC and EX records can be described in RELREC, then it should be defined. EX derivations must be described in the Define-XML document.
  42| 
  43| 6. Additional interventions qualifiers
~~~~

### T158. `ig34_p0113_a011` — r3:R3_PDF_TYPO

- PDF 页 113 · 原子类型 LIST_ITEM · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-EX`
- 登记 `B-EX T-3`: PDF 写 "from ottles A, B and C" → KB 写 "bottles" (处理: KB 写正确值; 依据: 同列表其他项 bottles; KB `knowledge_base/domains/EX/examples.md:118`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
1 tablet from ottles A, B and C from 2011-01-23 to 2011-01-28
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0113.txt` 第 13-13 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12|       •     1 tablet from bottles A and C on 2011-01-21 and 2011-01-22
 13|       •     1 tablet from ottles A, B and C from 2011-01-23 to 2011-01-28
 14| The EC dataset shows administrations as collected, in tablets.
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:118` (来源: registry B-EX T-3 kb_line_now):

~~~~
 118| - 1 tablet from bottles A, B and C from 2011-01-23 to 2011-01-28
~~~~

### T159. `ig34_p0115_a009` — r3:R3_PDF_TYPO

- PDF 页 115 · 原子类型 SENTENCE · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `B-EX`
- 登记 `B-EX T-4`: PDF 写 "protocol specified unit" → KB 写 "protocol-specified unit" (处理: KB 写正确值; 依据: 本节 p111/113/114/118 均 protocol-specified; KB `knowledge_base/domains/EX/examples.md:207`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The EX dataset shows the unmasked administrations in the protocol specified unit, mg. Amount of placebo was represented as 0 mg. The sponsor chose to represent the administrations at the time-point level.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0115.txt` 第 10-10 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  9| 
 10| The EX dataset shows the unmasked administrations in the protocol specified unit, mg. Amount of placebo was represented as 0 mg. The sponsor chose to represent the administrations at the time-point level.
 11| Rows 1-2:      Show administrations for a subject who was randomized to the 20 mg drug X arm.
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:207` (来源: registry B-EX T-4 kb_line_now):

~~~~
 207| The EX dataset shows the unmasked administrations in the protocol-specified unit, mg. Amount of placebo was represented as 0 mg. The sponsor chose to represent the administrations at the time-point level.
~~~~

### T160. `ig34_p0118_a017` — r3:R3_PDF_TYPO

- PDF 页 118 · 原子类型 SENTENCE · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **PRESENT** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `S1-R2` · 批 `B-EX`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-EX T-6: verbatim mg/mL 为 PDF 笔误, KB 改 mg/kg; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-EX.md:133`
- 登记 `B-EX T-6`: PDF 写 "Scheduled dose is represented in mg/mL" → KB 写 "mg/kg" (处理: KB 写正确值; 依据: 同句 (mg/kg) + Ex7 ec ECDOSU=mg/kg; KB `knowledge_base/domains/EX/examples.md:362`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Scheduled dose is represented in mg/mL.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0118.txt` 第 20-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19| The EC dataset shows both intended and actual doses of Drug Z, as collected.
 20| Rows 1, 3, 5: Show the collected intended dose levels (mg/kg) and ECMOOD is "SCHEDULED". Scheduled dose is represented in mg/mL.
 21| Rows 2, 4:       Show the collected actual administration amounts (mL) and ECMOOD is "PERFORMED". Actual doses are represented using dose in mL and concentration (pharmaceutical strength) in mg/mL.
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:362` (来源: registry B-EX T-6 kb_line_now):

~~~~
 362| **Rows 1, 3, 5:** Show the collected intended dose levels (mg/kg) and ECMOOD is "SCHEDULED". Scheduled dose is represented in mg/kg.
~~~~

### T161. `ig34_p0119_a011` — r3:R3_PDF_TYPO

- PDF 页 119 · 原子类型 SENTENCE · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `writer-Tn-registry` · 批 `B-EX`
- 登记 `B-EX T-2`: PDF 写 "using --LNKID, ." → KB 写 "using --LNKID." (处理: KB 写正确值; 依据: 多余逗号空格; KB `knowledge_base/domains/EX/examples.md:403`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-3:    Represent the one-to-one-to-one relationship between "PERFORMED" records in EC, records in EX, and records in VS using --LNKID, .
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0119.txt` 第 15-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14| The RELREC dataset represents relationships between EC, EX, and VS.
 15| Rows 1-3:      Represent the one-to-one-to-one relationship between "PERFORMED" records in EC, records in EX, and records in VS using --LNKID, .
 16| Rows 4-6:      Represent the many-to-one-to-one relationship between many records in EC (both "SCHEDULED" and "PERFORMED"), one record in EX, and one record in VS (for each visit), using --LNKGRP.
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:403` (来源: registry B-EX T-2 kb_line_now):

~~~~
 403| **Rows 1-3:** Represent the one-to-one-to-one relationship between "PERFORMED" records in EC, records in EX, and records in VS using --LNKID.
~~~~

### T162. `ig34_p0123_a005` — r3:R3_PDF_TYPO

- PDF 页 123 · 原子类型 LIST_ITEM · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `writer-Tn-registry` · 批 `B-ML`
- 登记 `B-ML T-2`: PDF 写 "occurrence of of prespecified" → KB 写 "occurrence of prespecified" (处理: KB 写正确值; 依据: 重复词; KB `knowledge_base/domains/ML/examples.md:8`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Data was collected about the occurrence of of prespecified foods prior to a suspected event of drug-induced liver injury (DILI).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0123.txt` 第 11-11 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 10|      •    Data was collected about the last meal before each hypoglycemic event
 11|      •    Data was collected about the occurrence of of prespecified foods prior to a suspected event of drug-induced liver injury (DILI).
 12| 
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:8` (来源: registry B-ML T-2 kb_line_now):

~~~~
   8| - Data was collected about the occurrence of prespecified foods prior to a suspected event of drug-induced liver injury (DILI).
~~~~

### T163. `ig34_p0132_a014` — r3:R3_PDF_TYPO

- PDF 页 132 · 原子类型 SENTENCE · 所在节 `§6.1.6 [Substance Use (SU)]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `B-SU`
- 登记 `B-SU T-1`: PDF 写 "SUENTTP = "2006-01-01"" → KB 写 "SUENTPT" (处理: KB 写正确值; 依据: spec/Row 3/表头 SUENTPT; KB `knowledge_base/domains/SU/examples.md:19`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 1: Subject 1234005 is a 2-pack/day current smoker. "Current" implies that smoking started sometime before the time the question was asked (SUSTTPT = "2006-01-01", SUSTRTPT = "BEFORE") and had not ended as of that date (SUENTTP = "2006-01-01", SUENRTPT = "ONGOING"). See Section 4.4.7, Use of Relative Timing Variables for the use of these variables. Both the beginning and ending reference time points for this question are the date of the assessment.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0132.txt` 第 18-21 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| have any caffeine records. A subject who never smoked and did not drink caffeinated drinks on the day of the assessment does not appear in the dataset.
 18| Row 1:         Subject 1234005 is a 2-pack/day current smoker. “Current” implies that smoking started sometime before the time the question was asked
 19|                (SUSTTPT = "2006-01-01", SUSTRTPT = "BEFORE") and had not ended as of that date (SUENTTP = "2006-01-01", SUENRTPT =
 20|                "ONGOING"). See Section 4.4.7, Use of Relative Timing Variables for the use of these variables. Both the beginning and ending reference time
 21|                points for this question are the date of the assessment.
 22| Row 2:         Subject 1234005 drank 3 cups of coffee on the day of the assessment.
~~~~

KB 现文: `knowledge_base/domains/SU/examples.md:19` (来源: registry B-SU T-1 kb_line_now):

~~~~
  19| **Row 1:** Subject 1234005 is a 2-pack/day current smoker. “Current” implies that smoking started sometime before the time the question was asked (SUSTTPT = "2006-01-01", SUSTRTPT = "BEFORE") and had not ended as of that date (SUENTPT = "2006-01-01", SUENRTPT = "ONGOING"). See Section 4.4.7, Use of Relative Timing Variables for the use of these variables. Both the beginning and ending reference time points for this question are the date of the assessment.
~~~~

### T164. `ig34_p0142_a012` — r3:R3_PDF_TYPO

- PDF 页 142 · 原子类型 LIST_ITEM · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-AE`
- 登记 `B-AE T-3`: PDF 写 "probably related to the event" → KB 写 "probably related to the device" (处理: KB 写正确值; 依据: 同表 r2 AERLDEV=PROBABLE, AEACNDEV=REMOVED; 主题为器械关系; KB `knowledge_base/domains/AE/examples.md:75`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 2: Shows an AE of "Osteomyelitis right hip". The location and laterality are specified and it is considered a serious adverse event. The device was removed as the AE was probably related to the event.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0142.txt` 第 18-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| Row 1:             Shows an AE of "Twisted left ankle". The location and laterality are specified as it may be important to know if it occurred on the same or opposite side of the body.
 18| Row 2:             Shows an AE of "Osteomyelitis right hip". The location and laterality are specified and it is considered a serious adverse event. The device was removed as the AE was probably related to the event.
 19| ae.xpt
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:75` (来源: registry B-AE T-3 kb_line_now):

~~~~
  75| **Row 2:** Shows an AE of "Osteomyelitis right hip". The location and laterality are specified and it is considered a serious adverse event. The device was removed as the AE was probably related to the device.
~~~~

### T165. `ig34_p0142_a014` — r3:R3_PDF_TYPO

- PDF 页 142 · 原子类型 TABLE_HEADER · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-AE`
- 登记 `B-AE T-4`: PDF 写 "Ex5 表头首格空白" → KB 写 "Row" (处理: KB 写正确值; 依据: 同文件其他表首格均为 Row; 列下为行号; KB `knowledge_base/domains/AE/examples.md:79`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| STUDYID | DOMAIN | USUBJID | SPDEVID | AESEQ | AESPID | AETERM | AEDECOD | AELOC | AELAT | AESER | AESEV | AEACNDEV | AERLDEV | AEOUT | AESCONG | AESHOSP | AESDISAB | AESDTH | AESLIFE | AESMIE | AESINTV | AEUNANT | AERLPRC | AERLPRT | AESTDTC | AEENDTC | AESTDY | AEENDY |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0142.txt` 第 20-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19| ae.xpt
 20|     STUDYID   DOMAIN    USUBJID   SPDEVID    AESEQ   AESPID   AETERM          AEDECOD           AELOC   AELAT   AESER     AESEV      AEACNDEV   AERLDEV    AEOUT        AESCONG   AESHOSP   AESDISAB   AESDTH   AESLIFE   AESMIE   AESINTV   AEUNANT   AERLPRC   AERLPRT   AESTDTC    AEENDTC     AESTDY    AEENDY
 21| 1   T002      AE        002       HipX22     1       AE0099   Twisted left    SPRAIN            ANKLE   LEFT    N         MILD       NONE       NOT        RECOVERED/   N         N         N          N        N         N        N         Y         N         Y         2018-04-   2014-04-    5         10
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:79` (来源: decision.evidence.hit):

~~~~
  79| | Row | STUDYID | DOMAIN | USUBJID | SPDEVID | AESEQ | AESPID | AETERM | AEDECOD | AELOC | AELAT | AESER | AESEV | AEACNDEV | AERLDEV | AEOUT | AESCONG | AESHOSP | AESDISAB | AESDTH | AESLIFE | AESMIE | AESINTV | AEUNANT | AERLPRC | AERLPRT | AESTDTC | AEENDTC | AESTDY | AEENDY |
~~~~

### T166. `ig34_p0142_a015` — r3:R3_PDF_TYPO

- PDF 页 142 · 原子类型 TABLE_ROW · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-AE`
- 登记 `B-AE T-1`: PDF 写 "AEENDTC 2014-04-26" → KB 写 "2018-04-26" (处理: KB 写正确值; 依据: 同行 AESTDTC 2018-04-21=AESTDY 5, AEENDY 10 → +5 天单值; KB `knowledge_base/domains/AE/examples.md:81`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| T002 | AE | 002 | HipX22 | 1 | AE0099 | Twisted left ankle | SPRAIN | ANKLE JOINT | LEFT | Y | MILD | NONE | NOT RELATED | RECOVERED/ RESOLVED | N | N | N | N | N | N | Y | Y | N | N | 2018-04-26 | 2014-04-28 | 15 | 10 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0142.txt` 第 21-23 行 (自动定位, 词覆盖 0.962; 版式以原 PDF 为准):

~~~~
 20|     STUDYID   DOMAIN    USUBJID   SPDEVID    AESEQ   AESPID   AETERM          AEDECOD           AELOC   AELAT   AESER     AESEV      AEACNDEV   AERLDEV    AEOUT        AESCONG   AESHOSP   AESDISAB   AESDTH   AESLIFE   AESMIE   AESINTV   AEUNANT   AERLPRC   AERLPRT   AESTDTC    AEENDTC     AESTDY    AEENDY
 21| 1   T002      AE        002       HipX22     1       AE0099   Twisted left    SPRAIN            ANKLE   LEFT    N         MILD       NONE       NOT        RECOVERED/   N         N         N          N        N         N        N         Y         N         Y         2018-04-   2014-04-    5         10
 22|                                                               ankle                             JOINT                                           RELATED    RESOLVED                                                                                                        21         26
 23| 2   T002      AE        002       HipX22     2       AE0033   Osteomyelitis   OSTEOMYELITIS     HIP     RIGHT   Y         MODERATE   REMOVED    PROBABLE   RECOVERED/   N         Y         Y          N        N         N        Y         Y         N         N         2018-05-   2018-05-    15        25
 24|                                                               right hip                                                                                    RESOLVED                                                                                                        01         10
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:81` (来源: registry B-AE T-1 kb_line_now):

~~~~
  81| | 1 | T002 | AE | 002 | HipX22 | 1 | AE0099 | Twisted left ankle | SPRAIN | ANKLE JOINT | LEFT | N | MILD | NONE | NOT RELATED | RECOVERED/RESOLVED | N | N | N | N | N | N | N | Y | N | Y | 2018-04-21 | 2018-04-26 | 5 | 10 |
~~~~

### T167. `ig34_p0142_a016` — r3:R3_PDF_TYPO

- PDF 页 142 · 原子类型 TABLE_ROW · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-AE`
- 登记 `B-AE T-2`: PDF 写 "RECOVERED/RESOLVED WITH SEQUELLAE" → KB 写 "RECOVERED/RESOLVED WITH SEQUELAE" (处理: KB 写正确值; 依据: CT C49495 拼写 (terminology/core/ae.md); KB `knowledge_base/domains/AE/examples.md:82`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| T002 | AE | 002 | HipX22 | 2 | AE0033 | Osteomyelitis right hip | OSTEOMYELITIS | HIP | RIGHT | Y | MODERATE | REMOVED | PROBABLE | RECOVERED/ RESOLVED WITH SEQUELLAE | N | Y | Y | N | N | N | Y | Y | N | N | 2018-05-01 | 2018-05-10 | 15 | 25 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0142.txt` 第 23-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 22|                                                               ankle                             JOINT                                           RELATED    RESOLVED                                                                                                        21         26
 23| 2   T002      AE        002       HipX22     2       AE0033   Osteomyelitis   OSTEOMYELITIS     HIP     RIGHT   Y         MODERATE   REMOVED    PROBABLE   RECOVERED/   N         Y         Y          N        N         N        Y         Y         N         N         2018-05-   2018-05-    15        25
 24|                                                               right hip                                                                                    RESOLVED                                                                                                        01         10
 25|                                                                                                                                                            WITH
 26|                                                                                                                                                            SEQUELLAE
 27| 
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:82` (来源: registry B-AE T-2 kb_line_now):

~~~~
  82| | 2 | T002 | AE | 002 | HipX22 | 2 | AE0033 | Osteomyelitis right hip | OSTEOMYELITIS | HIP | RIGHT | Y | MODERATE | REMOVED | PROBABLE | RECOVERED/RESOLVED WITH SEQUELAE | N | Y | Y | N | N | N | Y | Y | N | N | 2018-05-01 | 2018-05-10 | 15 | 25 |
~~~~

### T168. `ig34_p0146_a005` — r3:R3_PDF_TYPO

- PDF 页 146 · 原子类型 TABLE_ROW · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `B-BE`
- 登记 `B-BE T-1`: PDF 写 "DRY ICE/ISOPOPANOL" → KB 写 "DRY ICE/ISOPROPANOL" (处理: KB 写正确值; 依据: 拼写错; BSORRES/BSSTRESC 两格; KB `knowledge_base/domains/BE/examples.md:43`)
- 登记 `B-BE T-2`: PDF 写 "Ex1 bs r3 BSDTC 残缺 "5-0"" → KB 写 "2005-03-20" (处理: KB 写正确值; 依据: 同组 r1/r2 BSDTC 及 Ex1 全部 BEDTC=2005-03-20; KB `knowledge_base/domains/BE/examples.md:43`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | ABC134 | BS | 43871 | 3 | 267FF | 1148.267 | FFRZMAT | Flash Freeze Material | SPECIMEN HANDLING | DRY ICE/ISOPOPANOL | | DRY ICE/ISOPOPANOL | | | BRAIN | CEREBRAL AQUEDUCT | 1 | 5-0 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0146.txt` 第 7-8 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  6|                                                                                                                                                                                               AQUEDUCT                   20
  7| 3     ABC134       BS       43871   3       267FF    1148.267    FFRZMAT    Flash Freeze       SPECIMEN HANDLING    DRY                         DRY                                    BRAIN  CEREBRAL          1        5-0
  8|                                                                             Material                                ICE/ISOPOPANOL              ICE/ISOPOPANOL                                AQUEDUCT
  9| 
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:43` (来源: registry B-BE T-1 kb_line_now):

~~~~
  43| | 3 | ABC134 | BS | 43871 | 3 | 267FF | 1148.267 | FFRZMAT | Flash Freeze Material | SPECIMEN HANDLING | DRY ICE/ISOPROPANOL | | DRY ICE/ISOPROPANOL | | | BRAIN | CEREBRAL AQUEDUCT | 1 | 2005-03-20 |
~~~~

### T169. `ig34_p0152_a0019` — r3:R3_PDF_TYPO

- PDF 页 152 · 原子类型 SENTENCE · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **PRESENT** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-CE`
- 登记 `B-CE T-1`: PDF 写 "Topic Variables,for" → KB 写 "Topic Variables, for" (处理: KB 写正确值; 依据: 逗号后缺空格, 排版错; KB `knowledge_base/domains/CE/examples.md:54`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 5:	Shows a record for a write-in clinical event recorded in the "Other, Specify" space. Because this event was not prespecified, CEPRESP and CEOCCUR are null. See Section 4.2.7.3, "Specify" Values for Topic Variables,for further information on populating the topic variable when "Other, Specify" is used on the CRF.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0152.txt` 第 27-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26|                DONE indicates that the probing question was not asked or that there was no answer.
 27| Row 5:         Shows a record for a write-in clinical event recorded in the "Other, Specify" space. Because this event was not prespecified, CEPRESP and
 28|                CEOCCUR are null. See Section 4.2.7.3, "Specify" Values for Topic Variables,for further information on populating the topic variable when
 29|                "Other, Specify" is used on the CRF.
 30| ce.xpt
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:54` (来源: registry B-CE T-1 kb_line_now):

~~~~
  54| **Row 5:** Shows a record for a write-in clinical event recorded in the "Other, Specify" space. Because this event was not prespecified, CEPRESP and CEOCCUR are null. See Section 4.2.7.3, "Specify" Values for Topic Variables, for further information on populating the topic variable when "Other, Specify" is used on the CRF.
~~~~

### T170. `ig34_p0160_a0026` — r3:R3_PDF_TYPO

- PDF 页 160 · 原子类型 SENTENCE · 所在节 `§6.2.4 Disposition (DS)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `B-DS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A3-2 B-DS U-4 删 in | errata: t3_atom_err | new_target: domains/DS/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:17`
- 登记 `B-DS U-4`: PDF 写 "and in the AE record was represented" → KB 写 "between the DS record and the AE record (删 in)" (处理: KB 写正确值; 依据: PDF 原句语法瑕疵; KB `knowledge_base/domains/DS/examples.md:87`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The relationship between the DS record and in the AE record was represented in a RELREC dataset.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0160.txt` 第 26-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25| Example 4
 26| In this example, the CRF included collection of an AE number when study participation was incomplete due to an adverse event. The relationship between the
 27| DS record and in the AE record was represented in a RELREC dataset.
 28| The DS domain represents the end of the subject's participation in the study, due to their death from heart failure. In this case, the disposition was collected
~~~~

KB 现文: `knowledge_base/domains/DS/examples.md:87` (来源: registry B-DS U-4 kb_line_now):

~~~~
  87| In this example, the CRF included collection of an AE number when study participation was incomplete due to an adverse event. The relationship between the DS record and the AE record was represented in a RELREC dataset.
~~~~

### T171. `ig34_p0160_a0028` — r3:R3_PDF_TYPO

- PDF 页 160 · 原子类型 SENTENCE · 所在节 `§6.2.4 Disposition (DS)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-DS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-DS T-3 PDF_TYPO (DSDTDTC)→(DSSTDTC) (t2_B-DS.md:35) | errata: t3_atom_err | new_target: domains/DS/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:18`
- 登记 `B-DS T-3`: PDF 写 "(DSDTDTC)" → KB 写 "(DSSTDTC)" (处理: KB 写正确值; 依据: 无 DSDTDTC 变量; 句指 DSSTDTC; KB `knowledge_base/domains/DS/examples.md:89`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In this case, the disposition was collected (DSDTC) on the same day that death occurred and the subject's study participation ended. (DSDTDTC).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0160.txt` 第 28-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27| DS record and in the AE record was represented in a RELREC dataset.
 28| The DS domain represents the end of the subject's participation in the study, due to their death from heart failure. In this case, the disposition was collected
 29| (DSDTC) on the same day that death occurred and the subject's study participation ended. (DSDTDTC).
 30| ds.xpt
~~~~

KB 现文: `knowledge_base/domains/DS/examples.md:89` (来源: registry B-DS T-3 kb_line_now):

~~~~
  89| The DS domain represents the end of the subject's participation in the study, due to their death from heart failure. In this case, the disposition was collected (DSDTC) on the same day that death occurred and the subject's study participation ended. (DSSTDTC).
~~~~

### T172. `ig34_p0165_a0007` — r3:R3_PDF_TYPO

- PDF 页 165 · 原子类型 TABLE_ROW · 所在节 `§6.2.4 Disposition (DS)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `B-DS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A1-9 B-DS U-1 se ETCD SCREEN→SCRN | errata: t3_atom_err | new_target: domains/DS/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:19`
- 登记 `B-DS U-1`: PDF 写 "Ex10 se ETCD SCREEN" → KB 写 "ETCD SCRN (2 格, SE.ETCD 须为 TE 定义的 ETCD)" (处理: KB 写正确值; 依据: 同例 TE/TA 为 SCRN; 跨表不可定 (reviewer: 可用 SE.ETCD∈TE spec); KB `knowledge_base/domains/DS/examples.md:294`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 5 | XYZ | SE | XYZ-767-002 | 1 | SCREEN | Screen | 2016-02-04 | 2016-02-21 | 1 | SCREENING |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0165.txt` 第 7-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  6| 4        XYZ       SE          XYZ-767-001     4         FU          Follow-up                       2016-04-24    2016-04-24    4         FOLLOW-UP
  7| 5        XYZ       SE          XYZ-767-002     1         SCREEN      Screen                          2016-02-04    2016-02-21    1         SCREENING
  8| 6        XYZ       SE          XYZ-767-002     2         DRUG2       Drug-2                          2016-02-21    2016-03-24    2         TREATMENT 1
~~~~

KB 现文: `knowledge_base/domains/DS/examples.md:294` (来源: registry B-DS U-1 kb_line_now):

~~~~
 294| | 1 | XYZ | SE | XYZ-767-001 | 1 | SCRN | Screen | 2016-02-02 | 2016-02-14 | 1 | SCREENING |
~~~~

### T173. `ig34_p0166_a0035` — r3:R3_PDF_TYPO

- PDF 页 166 · 原子类型 LIST_ITEM · 所在节 `§6.2.4 Disposition (DS)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-DS`
- 登记 `B-DS T-5`: PDF 写 "recieved" → KB 写 "received" (处理: KB 写正确值; 依据: 拼写; KB `knowledge_base/domains/DS/examples.md:377`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 5: The subject's fifth element was not "ABC" or "AB", as would have been expected if they recieved all 4 cycles of therapy, but "FU".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0166.txt` 第 38-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 37| Rows 1-4:       The subject participated in the screening epoch and 3 elements of the treatment epoch.
 38| Row 5:          The subject's fifth element was not "ABC" or "AB", as would have been expected if they recieved all 4 cycles of therapy, but "FU".
 39| se.xpt
~~~~

KB 现文: `knowledge_base/domains/DS/examples.md:377` (来源: registry B-DS T-5 kb_line_now):

~~~~
 377| **Row 5:** The subject's fifth element was not "ABC" or "AB", as would have been expected if they received all 4 cycles of therapy, but "FU".
~~~~

### T174. `ig34_p0169_a0024` — r3:R3_PDF_TYPO

- PDF 页 169 · 原子类型 TABLE_ROW · 所在节 `§6.2.5 Healthcare Encounters (HO)`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-HO`
- 登记 `B-HO T-1`: PDF 写 "REHABILIATION FACILITY" → KB 写 "REHABILITATION FACILITY" (处理: KB 写正确值; 依据: Ex2 r3 / 叙述 / Assumption 1; KB `knowledge_base/domains/HO/examples.md:25`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 5 | ABC | HO | ABC123105 | 1 | GENERAL WARD | | TREATMENT | 2011-09-09 | 2011-09-11 | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0170.txt` 第 6-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  5| 2        ABC        HO         ABC123101     2          NURSING HOME                                      TREATMENT                                   P6D
  6| 3        ABC        HO         ABC123102     1          GENERAL WARD                                      TREATMENT      2011-08-06    2011-08-08
  7| 4        ABC        HO         ABC123102     2          INTENSIVE CARE                                    TREATMENT      2011-08-08    2011-08-15
  8| 5        ABC        HO         ABC123102     3          REHABILIATION FACILITY                            TREATMENT      2011-08-15    2011-08-20
  9| 6        ABC        HO         ABC123103     1          HOSPITAL                                          TREATMENT      2011-09-09    2011-09-11
 10| 7        ABC        HO         ABC123103     2          HOSPITAL                                          TREATMENT      2011-09-11    2011-09-15
 11| 8        ABC        HO         ABC123104     1          CARDIAC CATHETERIZATION LABORATORY                TREATMENT      2011-10-10    2011-10-10
 12| 9        ABC        HO         ABC123105     1          CARDIAC CATHETERIZATION LABORATORY                TREATMENT      2011-10-11    2011-10-11
 13| 10       ABC        HO         ABC123105     2          HOSPITAL                                          TREATMENT      2011-10-11    2011-10-15
~~~~

KB 现文: `knowledge_base/domains/HO/examples.md:25` (来源: registry B-HO T-1 kb_line_now):

~~~~
  25| | 5 | ABC | HO | ABC123102 | 3 | REHABILITATION FACILITY | TREATMENT | 2011-08-15 | 2011-08-20 | |
~~~~

### T175. `ig34_p0173_a0007` — r3:R3_PDF_TYPO

- PDF 页 173 · 原子类型 LIST_ITEM · 所在节 `§6.2.6 Medical History (MH)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `writer-Tn-registry` · 批 `B-MH`
- 登记 `B-MH T-3`: PDF 写 "“Allergy Medical History, “" → KB 写 ""Allergy Medical History,"" (处理: KB 写正确值; 依据: 标点印刷错; KB `knowledge_base/domains/MH/assumptions.md:27`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
ii. Examples of MHCAT could include "General Medical History" (see above assumption; if "General Medical History" is an MHCAT value, then there should be other MHCAT values), "Allergy Medical History, " and "Reproductive Medical History".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0173.txt` 第 17-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 16|                    necessary to include or populate this variable.
 17|                ii. Examples of MHCAT could include “General Medical History“ (see above assumption; if “General Medical History” is an MHCAT value,
 18|                    then there should be other MHCAT values), “Allergy Medical History, “ and “Reproductive Medical History”.
 19|           b.   MHGRPID may be used to link (or associate) different records together to form a block of related records at the subject level within the MH
~~~~

KB 现文: `knowledge_base/domains/MH/assumptions.md:27` (来源: registry B-MH T-3 kb_line_now):

~~~~
  27|       ii. Examples of MHCAT could include “General Medical History“ (see above assumption; if “General Medical History” is an MHCAT value, then there should be other MHCAT values), “Allergy Medical History,“ and “Reproductive Medical History”.
~~~~

