# T4.1 第三轮补检包 4 — R3_IG34_EQUIV (25 条; 编号 T76-T100)

> 由 `scripts/t4/t4_round3_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 T).

### T76. `ig34_p0401_a004` — r3:R3_IG34_EQUIV

- PDF 页 401 · 原子类型 SENTENCE · 所在节 `§7.2.1 Trial Arms (TA) – Example 7`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The following table shows the trial design matrix for this 2-arm example trial.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0401.txt` 第 14-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13| 
 14| The following table shows the trial design matrix for this 2-arm example trial.
 15| Trial Design Matrix
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:972` (来源: live valid_hits):

~~~~
 972| The following table shows the trial design matrix for this 2-arm example trial.
~~~~

### T77. `ig34_p0406_a011` — r3:R3_IG34_EQUIV

- PDF 页 406 · 原子类型 SENTENCE · 所在节 `§7.2.2.1 Trial Elements Issues – Distinguishing Elements, Study Cells, and Epochs`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
It also is natural to use the same name (e.g., screen, follow-up) for both such an epoch and the single element that appears within it.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0406.txt` 第 12-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11| this is because many trials have epochs for which the same element appears in all arms. In other words, in the trial
 12| design matrix for many trials, there are columns (Epochs) in which all the study cells have the same contents. It also
 13| is natural to use the same name (e.g., screen, follow-up) for both such an epoch and the single element that appears
 14| within it.
 15| Confusion can also arise from the fact that in the blinded treatment portions of blinded trials, blinded participants do
~~~~

KB 现文: `knowledge_base/domains/TE/examples.md:67` (来源: live valid_hits):

~~~~
  67| It is easy to confuse elements, which are reusable trial building blocks, with study cells (which contain the elements for a particular epoch and Arm) and with epochs (which are time periods for the trial as a whole). In part, this is because many trials have epochs for which the same element appears in all arms. In other words, in the trial design matrix for many trials, there are columns (Epochs) in which all the study cells have the same contents. It also is natural to use the same name (e.g., screen, follow-up) for both such an epoch and the single element that appears within it.
~~~~

### T78. `ig34_p0417_a018` — r3:R3_IG34_EQUIV

- PDF 页 417 · 原子类型 SENTENCE · 所在节 `§7.4.2 Trial Summary (TS)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
A trial design domain that contains one record for each trial summary characteristic.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0417.txt` 第 24-24 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 23| TS – Description/Overview
 24| A trial design domain that contains one record for each trial summary characteristic. This domain is not subject
 25| oriented.
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:5` (来源: live valid_hits):

~~~~
   5| A trial design domain that contains one record for each trial summary characteristic. This domain is not subject oriented.
~~~~

### T79. `ig34_p0424_a006` — r3:R3_IG34_EQUIV

- PDF 页 424 · 原子类型 SENTENCE · 所在节 `§7.4.2.1 Use of Null Flavor`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
When the trial summary parameter is AGEMAX, then TSVAL should have a value expressed as an ISO 8601 time duration (e.g., P43Y for 43 years old, P6M for 6 months old).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0424.txt` 第 9-10 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  8| (TS) dataset arose when it was realized that the TS model did not have a good way to represent the fact that a
  9| protocol placed no upper limit on the age of study subjects. When the trial summary parameter is AGEMAX, then
 10| TSVAL should have a value expressed as an ISO 8601 time duration (e.g., P43Y for 43 years old, P6M for 6 months
 11| old). Although it would be possible to allow a value such as "NONE" or "UNBOUNDED" to be entered in TSVAL,
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:67` (来源: live valid_hits):

~~~~
  67| The proposal to include a null flavor variable to supplement the TSVAL variable in the Trial Summary Information (TS) dataset arose when it was realized that the TS model did not have a good way to represent the fact that a protocol placed no upper limit on the age of study subjects. When the trial summary parameter is AGEMAX, then TSVAL should have a value expressed as an ISO 8601 time duration (e.g., P43Y for 43 years old, P6M for 6 months old). Although it would be possible to allow a value such as "NONE" or "UNBOUNDED" to be entered in TSVAL, validation programs would then have to recognize this special term as an exception to the expected data format. Therefore, the SDS team decided that a separate null flavor variable that uses the ISO 21090 null-flavor terminology would be a better solution.
~~~~

### T80. `ig34_p0424_a009` — r3:R3_IG34_EQUIV

- PDF 页 424 · 原子类型 SENTENCE · 所在节 `§7.4.2.1 Use of Null Flavor`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The SDS Team also decided to specify the use of a null-flavor variable in the TS domain with SDTMIG v3.4 as a way of testing the use of such a variable in a limited setting.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0424.txt` 第 15-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14| would be a better solution.
 15| The SDS Team also decided to specify the use of a null-flavor variable in the TS domain with SDTMIG v3.4 as a
 16| way of testing the use of such a variable in a limited setting. As the title of ISO 21090 suggests, that standard was
 17| developed for use with healthcare data; it is expected that it will eventually see wide use in the clinical data from
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:69` (来源: live valid_hits):

~~~~
  69| The SDS Team also decided to specify the use of a null-flavor variable in the TS domain with SDTMIG v3.4 as a way of testing the use of such a variable in a limited setting. As the title of ISO 21090 suggests, that standard was developed for use with healthcare data; it is expected that it will eventually see wide use in the clinical data from which clinical trial data are derived. CDISC already uses this data-type standard (see BRIDG; https://www.cdisc.org/standards/). The null flavor, in particular, is a solution to the widespread problem of needing or wanting to convey information that will help in the interpretation of a missing value. Although null flavors could certainly be eventually used for this purpose in other cases (e.g., with subject data), doing so at this time would be extremely disruptive and premature. The use of null flavors for the variable TSVAL provides an opportunity for sponsors and reviewers to learn about the null flavors and to evaluate their usefulness in a concrete setting.
~~~~

### T81. `ig34_p0424_a010` — r3:R3_IG34_EQUIV

- PDF 页 424 · 原子类型 SENTENCE · 所在节 `§7.4.2.1 Use of Null Flavor`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
As the title of ISO 21090 suggests, that standard was developed for use with healthcare data; it is expected that it will eventually see wide use in the clinical data from which clinical trial data are derived.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0424.txt` 第 16-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15| The SDS Team also decided to specify the use of a null-flavor variable in the TS domain with SDTMIG v3.4 as a
 16| way of testing the use of such a variable in a limited setting. As the title of ISO 21090 suggests, that standard was
 17| developed for use with healthcare data; it is expected that it will eventually see wide use in the clinical data from
 18| which clinical trial data are derived. CDISC already uses this data-type standard (see BRIDG;
 19| https://www.cdisc.org/standards/). The null flavor, in particular, is a solution to the widespread problem of needing
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:69` (来源: live valid_hits):

~~~~
  69| The SDS Team also decided to specify the use of a null-flavor variable in the TS domain with SDTMIG v3.4 as a way of testing the use of such a variable in a limited setting. As the title of ISO 21090 suggests, that standard was developed for use with healthcare data; it is expected that it will eventually see wide use in the clinical data from which clinical trial data are derived. CDISC already uses this data-type standard (see BRIDG; https://www.cdisc.org/standards/). The null flavor, in particular, is a solution to the widespread problem of needing or wanting to convey information that will help in the interpretation of a missing value. Although null flavors could certainly be eventually used for this purpose in other cases (e.g., with subject data), doing so at this time would be extremely disruptive and premature. The use of null flavors for the variable TSVAL provides an opportunity for sponsors and reviewers to learn about the null flavors and to evaluate their usefulness in a concrete setting.
~~~~

### T82. `ig34_p0441_a002` — r3:R3_IG34_EQUIV

- PDF 页 441 · 原子类型 SENTENCE · 所在节 `§9 [STUDY REFERENCES]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
There are occasions when it is necessary to establish study-specific terminology that will be used in tabulated data.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0441.txt` 第 2-2 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| 9 Study References
  2| There are occasions when it is necessary to establish study-specific terminology that will be used in tabulated data.
  3| The following situations have been identified thus far:
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:256-256` (来源: fuzzy locate (score 0.895)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 256| There are occasions when it is necessary to establish study-specific identifiers that will be used in subject data. Two such situations have been identified thus far:
~~~~

### T83. `ig34_p0448_a013` — r3:R3_IG34_EQUIV

- PDF 页 448 · 原子类型 SENTENCE · 所在节 `Appendix D: CDISC Variable-naming Fragments`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In other cases the same fragment may be used for more than one meaning, but these would not normally overlap for the same variable.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0449.txt` 第 11-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 10| possible) to fit within the 8-character limit.
 11| In other cases the same fragment may be used for more than one meaning, but these would not normally overlap for
 12| the same variable.
 13| 
~~~~

KB 现文: `knowledge_base/chapters/ch10_appendices.md:173` (来源: live valid_hits):

~~~~
 173| In other cases the same fragment may be used for more than one meaning, but these would not normally overlap for the same variable.
~~~~

### T84. `ig34_p0032_a022` — r3:R3_IG34_EQUIV

- PDF 页 32 · 原子类型 TABLE_HEADER · 所在节 `§4.2.7.1 "Specify" Values for Non-result Qualifier Variables`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
CMINDC | FRACTURE
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0032.txt` 第 47-47 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 46| 
 47|          Note that the sponsor might choose a different value for CMINDC (e.g., "BONE FRACTURE") depending
 48|          on the sponsor's coding practice and analysis requirements.
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:456-456` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 456|    Note that the sponsor might choose a different value for CMINDC (e.g., "BONE FRACTURE") depending on the sponsor's coding practice and analysis requirements.
~~~~

### T85. `ig34_p0071_a013` — r3:R3_IG34_EQUIV

- PDF 页 71 · 原子类型 TABLE_HEADER · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Select each value that applies if the subject answered "BLACK OR AFRICAN AMERICAN". Check all that apply. | Which of the following racial designations best describes you? | [checkboxes]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0072.txt` 第 55-64 行 (自动定位, 词覆盖 0.8; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 54|                                                    after ethnicity.
 55| If study participant answered: AMERICAN INDIAN OR ALASKA NATIVE
 56| CRACE01- 10            Which of the following Race Select each       Text   SUPPDM.QVAL   For each value that   (RACEC)       ALASKA NATIVE; AMERICAN                           checkbox
 57| CRACE04                racial designations         value that                             applies,                            INDIAN; CARIBBEAN INDIAN;
 58|                        best describes you?         applies if the                         SUPPDM.QVAL where                   CENTRAL AMERICAN
 59|                                                    subject                                SUPPDM.QNAM                         INDIAN;
 60|                                                    answered                               ="CRACEn" and
 61| 
 62| 
 63| 
 64| © 2021 Clinical Data Interchange Standards Consortium, Inc. All rights reserved                                                                                                             Page 72
 65| 2021-11-29
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:192-192` (来源: fuzzy locate (score 0.96)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 192| | CRACE11-CRACE17 | 12 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "BLACK OR AFRICAN AMERICAN". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | AFRICAN; AFRICAN AMERICAN; AFRICAN CARIBBEAN; BAHAMIAN; BARBADIAN; BLACK; BLACK CENTRAL AMERICAN; | | | checkbox | |
~~~~

### T86. `ig34_p0118_a002` — r3:R3_IG34_EQUIV

- PDF 页 118 · 原子类型 TABLE_HEADER · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Intended Dose | 10 mg/kg | 7.5 mg/kg | 10 mg/kg | 7.5 mg/kg |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0118.txt` 第 2-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| Visit                                     1                                                         2                                                        3
  2| Intended Dose                                 • 10 mg/kg                                               • 10 mg/kg                                               • 10 mg/kg
  3|                                               • 7.5 mg/kg                                              • 7.5 mg/kg                                              • 7.5 mg/kg
  4| Reason for Dose Adjustment                    • Dose-limiting toxicity                                 • Dose-limiting toxicity                                 • Dose-limiting toxicity
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:329-329` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 329| The study in this example involved weekly infusions of drug Z 10 mg/kg. If a subject experienced a dose-limiting toxicity (DLT), the intended dose could be reduced to 7.5 mg/kg.
~~~~

### T87. `ig34_p0141_a019` — r3:R3_IG34_EQUIV

- PDF 页 141 · 原子类型 TABLE_HEADER · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AEDECOD | AEPRESP | AEBODSYS | AESER | AEACN | AEREL | AEDTC | AESTDTC | AEENDTC | AEDY |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0141.txt` 第 35-35 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 34| ae.xpt
 35| Row      STUDYID     DOMAIN       USUBJID     AESEQ     AETERM       AEDECOD         AEPRESP        AEBODSYS                          AESER     AEACN    AEREL     AEDTC         AESTDTC         AEENDTC        AEDY
 36| 1        ABC123      AE           123101      1         NAUSEA       Nausea          Y              Gastrointestinal disorders                                     2005-10-29                                   19
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:43` (来源: live valid_hits):

~~~~
  43| | Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AEDECOD | AEPRESP | AEBODSYS | AESER | AEACN | AEREL | AEDTC | AESTDTC | AEENDTC | AEDY |
~~~~

### T88. `ig34_p0202_a001` — r3:R3_IG34_EQUIV

- PDF 页 202 · 原子类型 TABLE_HEADER · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format1 | Role | CDISC Notes | Core |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0202.txt` 第 1-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| Variable      Variable Label           Type Controlled           Role        CDISC Notes                                                                                                      Core
  2| Name                                        Terms, Codelist
  3|                                             or Format1
  4|                                                                              of defined characteristics (e.g., presence, absence, or intensity of expression of various markers;
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### T89. `ig34_p0311_a011` — r3:R3_IG34_EQUIV

- PDF 页 311 · 原子类型 TABLE_HEADER · 所在节 `§6.3.7.7 Respiratory System Findings (RE)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0311.txt` 第 12-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11| di.xpt
 12| Row      STUDYID    DOMAIN     SPDEVID     DISEQ     DIPARMCD    DIPARM          DIVAL
 13| 1        XYZ        DI         ABC001      1         DEVTYPE     Device Type     SPIROMETER
~~~~

KB 现文: `knowledge_base/domains/RE/examples.md:27,74` (来源: live valid_hits):

~~~~
  27| | Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
  74| | Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
~~~~

### T90. `ig34_p0311_a028` — r3:R3_IG34_EQUIV

- PDF 页 311 · 原子类型 TABLE_HEADER · 所在节 `§6.3.7.7 Respiratory System Findings (RE)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | RESEQ | RETESTCD | RETEST | REORRES | REORRESU | RESTRESN | RESTRESU | REREPNUM | VISITNUM | VISIT | REDTC |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0311.txt` 第 30-30 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 29| re.xpt
 30| Row STUDYID DOMAIN USUBJID               SPDEVID RESEQ RETESTCD RETEST                          REORRES REORRESU RESTRESN RESTRESU REREPNUM VISITNUM VISIT                       REDTC
 31| 1   XYZ     RE     XYZ-001-              ABC001  1     FEV1     Forced Expiratory               1.94    L        1.94     L        1        2        VISIT                       2013-04-
~~~~

KB 现文: `knowledge_base/domains/RE/examples.md:49` (来源: live valid_hits):

~~~~
  49| | Row | STUDYID | DOMAIN | USUBJID | SPDEVID | RESEQ | RETESTCD | RETEST | REORRES | REORRESU | RESTRESN | RESTRESU | REREPNUM | VISITNUM | VISIT | REDTC |
~~~~

### T91. `ig34_p0018_a014` — r3:R3_IG34_EQUIV

- PDF 页 18 · 原子类型 TABLE_ROW · 所在节 `§3.2.1 Dataset-level Metadata`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
CE | Clinical Events | Events | One record per event per subject | Tabulation | STUDYID, USUBJID, CETERM, CESTDTC | ce.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0018.txt` 第 17-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 16|                                               identifier per subject                         BESDTC
 17| CE        Clinical Events       Events        One record per event per subject    Tabulation STUDYID, USUBJID,     ce.xpt
 18|                                                                                              CETERM, CESTDTC
 19| DS        Disposition           Events       One record per disposition status or Tabulation STUDYID, USUBJID,     ds.xpt
~~~~

KB 现文: `knowledge_base/chapters/ch03_submitting_data.md:38` (来源: live valid_hits):

~~~~
  38| | CE | Clinical Events | Events | One record per event per subject | Tabulation | STUDYID, USUBJID, CETERM, CESTDTC | ce.xpt |
~~~~

### T92. `ig34_p0018_a022` — r3:R3_IG34_EQUIV

- PDF 页 18 · 原子类型 TABLE_ROW · 所在节 `§3.2.1 Dataset-level Metadata`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
MH | Medical History | Events | One record per medical history event per subject | Tabulation | STUDYID, USUBJID, MHDECOD | mh.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0018.txt` 第 25-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24|           Encounters                         encounter per subject                           HOTERM, HOSTDTC
 25| MH        Medical History       Events       One record per medical history       Tabulation STUDYID, USUBJID,     mh.xpt
 26|                                              event per subject                               MHDECOD
 27| BS        Biospecimen           Findings     One record per measurement per       Tabulation STUDYID, USUBJID,     bs.xpt
~~~~

KB 现文: `knowledge_base/chapters/ch03_submitting_data.md:42` (来源: live valid_hits):

~~~~
  42| | MH | Medical History | Events | One record per medical history event per subject | Tabulation | STUDYID, USUBJID, MHDECOD | mh.xpt |
~~~~

### T93. `ig34_p0018_a024` — r3:R3_IG34_EQUIV

- PDF 页 18 · 原子类型 TABLE_ROW · 所在节 `§3.2.1 Dataset-level Metadata`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
BS | Biospecimen Findings | Findings | One record per measurement per biospecimen identifier per subject | Tabulation | STUDYID, USUBJID, BSREFID, BSTESTCD | bs.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0018.txt` 第 27-28 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26|                                              event per subject                               MHDECOD
 27| BS        Biospecimen           Findings     One record per measurement per       Tabulation STUDYID, USUBJID,     bs.xpt
 28|           Findings                           biospecimen identifier per subject              BSREFID, BSTESTCD
 29| CP        Cell Phenotype        Findings     One record per test per specimen     Tabulation STUDYID, USUBJID,     cp.xpt
~~~~

KB 现文: `knowledge_base/chapters/ch03_submitting_data.md:43` (来源: live valid_hits):

~~~~
  43| | BS | Biospecimen Findings | Findings | One record per measurement per biospecimen identifier per subject | Tabulation | STUDYID, USUBJID, BSREFID, BSTESTCD | bs.xpt |
~~~~

### T94. `ig34_p0018_a032` — r3:R3_IG34_EQUIV

- PDF 页 18 · 原子类型 TABLE_ROW · 所在节 `§3.2.1 Dataset-level Metadata`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
DD | Death Details | Findings | One record per finding per subject | Tabulation | STUDYID, USUBJID, DDTESTCD, DDDTC | dd.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0018.txt` 第 38-39 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 37|           Accountability                     accountability finding per subject              DATESTCD, DADTC
 38| DD        Death Details         Findings     One record per finding per subject   Tabulation STUDYID, USUBJID,     dd.xpt
 39|                                                                                              DDTESTCD, DDDTC
 40| EG        ECG Test Results      Findings     One record per ECG observation       Tabulation STUDYID, USUBJID,     eg.xpt
~~~~

KB 现文: `knowledge_base/chapters/ch03_submitting_data.md:47` (来源: live valid_hits):

~~~~
  47| | DD | Death Details | Findings | One record per finding per subject | Tabulation | STUDYID, USUBJID, DDTESTCD, DDDTC | dd.xpt |
~~~~

### T95. `ig34_p0018_a042` — r3:R3_IG34_EQUIV

- PDF 页 18 · 原子类型 TABLE_ROW · 所在节 `§3.2.1 Dataset-level Metadata`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
IS | Immunogenicity Specimen Assessments | Findings | One record per test per visit per subject | Tabulation | STUDYID, USUBJID, ISTESTCD, ISBDAGNT, ISSCMBCL, ISTSTOPO, VISITNUM | is.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0018.txt` 第 53-56 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 52|           Criteria Not Met                   criterion not met per subject                   IETESTCD
 53| IS        Immunogenicity        Findings     One record per test per visit per    Tabulation STUDYID, USUBJID,     is.xpt
 54|           Specimen                           subject                                         ISTESTCD, ISBDAGNT,
 55|           Assessments                                                                        ISSCMBCL, ISTSTOPO,
 56|                                                                                              VISITNUM
 57| LB        Laboratory Test       Findings     One record per lab test per time     Tabulation STUDYID, USUBJID,     lb.xpt
~~~~

KB 现文: `knowledge_base/chapters/ch03_submitting_data.md:52` (来源: live valid_hits):

~~~~
  52| | IS | Immunogenicity Specimen Assessments | Findings | One record per test per visit per subject | Tabulation | STUDYID, USUBJID, ISTESTCD, ISBDAGNT, ISSCMBCL, ISTSTOPO, VISITNUM | is.xpt |
~~~~

### T96. `ig34_p0061_a021` — r3:R3_IG34_EQUIV

- PDF 页 61 · 原子类型 TABLE_ROW · 所在节 `§5.1 [Comments (CO)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 5: | Shows a comment related to multiple VS records with VSGRPID = "VS2".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0061.txt` 第 31-31 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 30| Row 4:         Shows a comment related to multiple EX records with EXGRPID = "COMBO1".
 31| Row 5:         Shows a comment related to multiple VS records with VSGRPID = "VS2".
 32| 
~~~~

KB 现文: `knowledge_base/domains/CO/examples.md:13` (来源: live valid_hits):

~~~~
  13| **Row 5:** Shows a comment related to multiple VS records with VSGRPID = "VS2".
~~~~

### T97. `ig34_p0062_a002` — r3:R3_IG34_EQUIV

- PDF 页 62 · 原子类型 TABLE_ROW · 所在节 `§5.1 [Comments (CO)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 7: | Shows a second option for representing a comment associated only with a visit. In this case, COREF is used to show that the comment is related to the particular visit.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0062.txt` 第 3-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2|                comment is linked to the Subject Visit record in SV (RDOMAIN = "SV") and IDVAR and IDVARVAL are populated link the comment to the
  3|                particular visit.
  4| Row 7:         Shows a second option for representing a comment associated only with a visit. In this case, COREF is used to show that the comment is related to
  5|                the particular visit.
~~~~

KB 现文: `knowledge_base/domains/CO/examples.md:17` (来源: live valid_hits):

~~~~
  17| **Row 7:** Shows a second option for representing a comment associated only with a visit. In this case, COREF is used to show that the comment is related to the particular visit.
~~~~

### T98. `ig34_p0068_a006` — r3:R3_IG34_EQUIV

- PDF 页 68 · 原子类型 TABLE_ROW · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
2 | ABC123 | DM | ABC1230102 | 0102 | 2006-01-28 | 2006-02-28 | 2006-01-15 | 2006-03-26 | 01 | JOHNSON, JANE | 1953-03-22 | 50 | YEARS | M | WHITE | NOT HISPANIC OR LATINO | Placebo | P | Placebo | | USA
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0068.txt` 第 6-8 行 (自动定位, 词覆盖 0.852; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  5| 1   ABC123  DM     ABC12301001 01001  2006-01-        2006-03-   2006-01-12 2006-03-10 2006-01-       2006-04-01 01   JOHNSON,      1948-12- 57 YEARS M  WHITE              HISPANIC    A     Drug A    A        Drug A                       USA
  6|                                       12              10                               03                             M             13                                      OR LATINO
  7| 2   ABC123  DM     ABC12301002 01002  2006-01-        2006-02-   2006-01-15 2006-02-28 2006-01-       2006-03-26 01   JOHNSON,      1955-03- 50 YEARS M  WHITE              NOT         P      Placebo P         Placebo                      USA
  8|                                       15              28                               04                             M             22                                      HISPANIC
  9|                                                                                                                                                                             OR LATINO
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:10-10` (来源: fuzzy locate (score 0.852)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  10| | 2 | ABC123 | DM | ABC12301002 | 01002 | 2006-01-15 | 2006-02-28 | 2006-01-15 | 2006-02-28 | 2006-01-04 | 2006-03-26 | 01 | JOHNSON, M | 1955-03-22 | 50 | YEARS | M | WHITE | NOT HISPANIC OR LATINO | P | Placebo | P | Placebo | | | USA |
~~~~

### T99. `ig34_p0075_a006` — r3:R3_IG34_EQUIV

- PDF 页 75 · 原子类型 TABLE_ROW · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
RACE01 | RACE | Which of the following racial designations best describes you? (More than one choice is acceptable.) | AMERICAN INDIAN OR ALASKA NATIVE / <Race codelist>
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0076.txt` 第 6-12 行 (自动定位, 词覆盖 0.957; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  5|                                                                                                Name
  6| RACE01      3      Which of the        Race    Study          Text   RACE                      (RACE)        AMERICAN INDIAN OR                         checkbox
  7|                    following racial            participants                                                  ALASKA NATIVE
  8|                    designations best           should self-
  9|                    describes you?              report race,
 10|                    (More than one              with race
 11|                    choice is                   being asked
 12|                    acceptable.)                about after
 13|                                                ethnicity.
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:180-180` (来源: fuzzy locate (score 0.957)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 180| | RACE01 | 1 | Which of the following racial designations best describes you? (More than one choice is acceptable.) | Race | Study participants should self-report race, with race being asked about after ethnicity. | Text | RACE | | (RACE) | AMERICAN INDIAN OR ALASKA NATIVE | | | checkbox | |
~~~~

### T100. `ig34_p0112_a023` — r3:R3_IG34_EQUIV

- PDF 页 112 · 原子类型 TABLE_ROW · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Side | RIGHT
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0112.txt` 第 24-24 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 23| Location             ABDOMEN
 24| Side                 RIGHT
 25| 
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:82` (来源: live valid_hits):

~~~~
  82| | Side | RIGHT |
~~~~

