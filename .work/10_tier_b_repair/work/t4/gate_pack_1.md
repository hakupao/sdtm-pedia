# T4.1 总闸样本包 1/4 (行 1-21 / 84)

> 由 `scripts/t4/t4_sample.py` (seed 20261127) 生成, `scripts/t4/t4_render.py` 渲染. 只读材料.

### 1. `ig34_p0016_a018` — gate:PRESENT

- PDF 页 16 · 原子类型 LIST_ITEM · 所在节 `§2.7 SDTM Variables Not Allowed in the SDTMIG`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_027`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
SETCD (Demographics)
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0016.txt` 第 20-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19|     •      --DISTR (Findings)
 20|     •      SETCD (Demographics)
 21| 
~~~~

KB 现文: `knowledge_base/chapters/ch02_fundamentals.md:174` (来源: decision.evidence.hit):

~~~~
 174| - SETCD (Demographics)
~~~~

### 2. `ig34_p0031_a028` — gate:PRESENT

- PDF 页 31 · 原子类型 CODE_LITERAL · 所在节 `§4.2.7.1 "Specify" Values for Non-result Qualifier Variables`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_027`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
AESMIE = "Y"
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0031.txt` 第 39-39 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 38| CRF, the free-text description should be stored in the SUPPAE dataset.
 39|     •    AESMIE = "Y"
 40|     •    SUPPAE QNAM = "AESOSP", QLABEL = "Other Medically Important SAE", QVAL = "HIGH RISK
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:403` (来源: decision.evidence.hit):

~~~~
 403| - AESMIE = "Y"
~~~~

### 3. `ig34_p0055_a003` — gate:PRESENT

- PDF 页 55 · 原子类型 SENTENCE · 所在节 `§4.5.3.1 [Test Name (--TEST) Greater than 40 Characters]`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_028`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Values of IETEST that exceed 200 characters should be described in study metadata as per the convention above.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0055.txt` 第 4-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3| domains are exceptions to the 40-character rule and are limited to 200 characters, because these are not expected to
  4| be transformed to column labels. Values of IETEST that exceed 200 characters should be described in study
  5| metadata as per the convention above. See Section 6.3.4, Inclusion/Exclusion Criteria Not Met, assumption 3; and
  6| Section 7.4.1, Trial Inclusion/Exclusion Criteria, assumption 5.
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1399` (来源: decision.evidence.hit):

~~~~
1399| IETEST values in the Inclusion/Exclusion Criteria Not Met (IE) and Trial Inclusion/Exclusion Criteria (TI) domains are exceptions to the 40-character rule and are limited to 200 characters, because these are not expected to be transformed to column labels. Values of IETEST that exceed 200 characters should be described in study metadata as per the convention above. See Section 6.3.4, Inclusion/Exclusion Criteria Not Met, assumption 3; and Section 7.4.1, Trial Inclusion/Exclusion Criteria, assumption 5.
~~~~

### 4. `ig34_p0103_a006` — gate:PRESENT

- PDF 页 103 · 原子类型 SENTENCE · 所在节 `§6.1.2 [Concomitant/Prior Medications (CM)]`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_017`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In this rheumatoid arthritis (RA) study, the sponsor collected medications using the category "Prior RA Medications", then collected information on whether the subject had received certain medication classes, represented as subcategories. If a subject did receive medications in a subcategory, information about those medications was collected. This example shows data for 2 subjects who received prior RA medications. It includes data only about their prior disease-modifying antirheumatic drugs (DMARDs); information about other kinds of prior RA medications is not included.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0103.txt` 第 7-10 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  6| Example 5
  7| In this rheumatoid arthritis (RA) study, the sponsor collected medications using the category "Prior RA Medications", then collected information on whether the
  8| subject had received certain medication classes, represented as subcategories. If a subject did receive medications in a subcategory, information about those
  9| medications was collected. This example shows data for 2 subjects who received prior RA medications. It includes data only about their prior disease-modifying
 10| antirheumatic drugs (DMARDs); information about other kinds of prior RA medications is not included.
 11| Row 1:         Shows that subject 101 received prior RA medications. The values of CMTRT and CMCAT are the same, indicating that this record represents the
~~~~

KB 现文: `knowledge_base/domains/CM/examples.md:82` (来源: decision.evidence.hit):

~~~~
  82| In this rheumatoid arthritis (RA) study, the sponsor collected medications using the category "Prior RA Medications", then collected information on whether the subject had received certain medication classes, represented as subcategories. If a subject did receive medications in a subcategory, information about those medications was collected. This example shows data for 2 subjects who received prior RA medications. It includes data only about their prior disease-modifying antirheumatic drugs (DMARDs); information about other kinds of prior RA medications is not included.
~~~~

### 5. `ig34_p0117_a007` — gate:PRESENT

- PDF 页 117 · 原子类型 SENTENCE · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_013`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The example CRF below was for subject ABC123-0201, who weighed 55 kg.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0117.txt` 第 39-39 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 38| The study in this example involved weekly infusions of drug Z 10 mg/kg. If a subject experienced a dose-limiting toxicity (DLT), the intended dose could be reduced to 7.5 mg/kg.
 39| The example CRF below was for subject ABC123-0201, who weighed 55 kg. The CRF shows that:
 40|       •     The subject's first administration of drug Z was on 2009-02-13; the intended dose was 10 mg/kg, but the actual amount given was 99 mL at 5.5 mg/mL, so the actual dose was 9.9 mg/kg.
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:331` (来源: decision.evidence.hit):

~~~~
 331| The example CRF below was for subject ABC123-0201, who weighed 55 kg. The CRF shows that:
~~~~

### 6. `ig34_p0119_a006` — gate:PRESENT

- PDF 页 119 · 原子类型 CODE_LITERAL · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_013`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
vs.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0119.txt` 第 9-9 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  8| To complete this example the relevant records from the Vital Signs domain are represented below, to show the collected weight of the subject which was used for the dosing calculations.
  9| vs.xpt
 10| Row      STUDYID    DOMAIN   USUBJID         VSSEQ    VSLNKID           VSLNKGRP         VSTESTCD     VSTEST   VSORRES   VSORRESU    VSSTRESC     VSSTRESN     VSSTRESU       VSLOBXFL   VISITNUM   VISIT     VSDTC        EPOCH
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:394` (来源: decision.evidence.hit):

~~~~
 394| **vs.xpt**
~~~~

### 7. `ig34_p0123_a019` — gate:PRESENT

- PDF 页 123 · 原子类型 NOTE · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_030`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Note that in this example MLENDTC is null. Because no end date was collected, the meal was represented as a point-in-time event, as described in Assumption 2b.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0123.txt` 第 29-30 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28| 
 29| Note that in this example MLENDTC is null. Because no end date was collected, the meal was represented as a point-in-time event, as described in Assumption
 30| 2b.
 31| Rows 1-3:       Show the last meal data for 3 hypoglycemic events.
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:31` (来源: decision.evidence.hit):

~~~~
  31| Note that in this example MLENDTC is null. Because no end date was collected, the meal was represented as a point-in-time event, as described in Assumption 2b.
~~~~

### 8. `ig34_p0184_a022` — gate:PRESENT

- PDF 页 184 · 原子类型 SENTENCE · 所在节 `§6.3.2 Death Details (DD)`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_023`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Example 2
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0184.txt` 第 30-30 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 29| 
 30| Example 2
 31| This example illustrates how the DD, Disposition (DS), and AE data for a subject were linked using RELREC. Note that each of these domains serves a different
~~~~

KB 现文: `knowledge_base/domains/DD/examples.md:25` (来源: decision.evidence.hit):

~~~~
  25| ## Example 2
~~~~

### 9. `ig34_p0281_a023` — gate:PRESENT

- PDF 页 281 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 3`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_002`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 18 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0281.txt` 第 25-25 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24| 17    ABC-123     PC          ABC-123-0001     PCSEQ      4                         2
 25| 18    ABC-123     PC          ABC-123-0001     PCSEQ      5                         2
 26| 19    ABC-123     PC          ABC-123-0001     PCSEQ      6                         2
~~~~

KB 现文: `knowledge_base/domains/PC/examples.md:323` (来源: decision.evidence.hit):

~~~~
 323| | 18 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 | | 2 |
~~~~

### 10. `ig34_p0282_a003` — gate:PRESENT

- PDF 页 282 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 3`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_002`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 | | 1 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0282.txt` 第 4-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3| 7      ABC-123      PC         ABC-123-0001    PCSEQ    7                          1
  4| 8      ABC-123      PC         ABC-123-0001    PCSEQ    8                          1
  5| 9      ABC-123      PC         ABC-123-0001    PCSEQ    9                          1
~~~~

KB 现文: `knowledge_base/domains/PC/examples.md:313,367,160,98` (来源: decision.evidence.hit):

~~~~
 160| | 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 | | 1 |
 313| | 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 | | 1 |
 367| | 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 | | 1 |
~~~~

### 11. `ig34_p0440_a012` — gate:PRESENT

- PDF 页 440 · 原子类型 SENTENCE · 所在节 `RELSPEC – Examples`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_033`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
SPEC reflects the specimen type for the sample regardless of whether it is collected or derived.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0440.txt` 第 18-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| A specimen with a LEVEL value of "1" and a blank value for PARENT indicates a collected sample. All other
 18| values represent a derived sample. SPEC reflects the specimen type for the sample regardless of whether it is
 19| collected or derived.
 20| relspec.xpt
~~~~

KB 现文: `knowledge_base/domains/RELSPEC/examples.md:40` (来源: decision.evidence.hit):

~~~~
  40| A specimen with a LEVEL value of "1" and a blank value for PARENT indicates a collected sample. All other values represent a derived sample. SPEC reflects the specimen type for the sample regardless of whether it is collected or derived.
~~~~

### 12. `sv20_p0009_a006` — gate:PRESENT

- PDF 页 9 · 原子类型 SENTENCE · 所在节 `§2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM]`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_027`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
There are variables which play different roles in different datasets. This is most common for variables which appear in both trial design datasets and general observation class datasets. For example, ARMCD is the topic variable in Trial Arms (TA), but a record qualifier in Demographics (DM) and Trial Visits (TV). Variables which appear in multiple general observation classes have the same role, although the variable qualified by a variable qualifier or synonym qualifier can be different in different general observation classes. For example, --MODIFY qualifies --TRT in interventions, --TERM in events, and --ORRES in findings.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0009.txt` 第 12-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11| a dataset, can be classified according to its role. A role describes the type of information conveyed by the variable
 12| about each distinct observation and how it can be used. There are variables which play different roles in different
 13| datasets. This is most common for variables which appear in both trial design datasets and general observation class
 14| datasets. For example, ARMCD is the topic variable in Trial Arms (TA), but a record qualifier in Demographics
 15| (DM) and Trial Visits (TV). Variables which appear in multiple general observation classes have the same role,
 16| although the variable qualified by a variable qualifier or synonym qualifier can be different in different general
 17| observation classes. For example, --MODIFY qualifies --TRT in interventions, --TERM in events, and --ORRES in
 18| findings.
 19| SDTM variables can be classified into 5 major roles:
~~~~

KB 现文: `knowledge_base/model/01_concepts_and_terms.md:160` (来源: decision.evidence.hit):

~~~~
 160| Each observation consists of a series of named variables. Each variable, which normally corresponds to a column in a dataset, can be classified according to its **role**. A role describes the type of information conveyed by the variable about each distinct observation and how it can be used. There are variables which play different roles in different datasets. This is most common for variables which appear in both trial design datasets and general observation class datasets. For example, ARMCD is the topic variable in Trial Arms (TA), but a record qualifier in Demographics (DM) and Trial Visits (TV). Variables which appear in multiple general observation classes have the same role, although the variable qualified by a variable qualifier or synonym qualifier can be different in different general observation classes. For example, --MODIFY qualifies --TRT in interventions, --TERM in events, and --ORRES in findings.
~~~~

### 13. `ig34_p0010_a008` — gate:REWRITE_OK

- PDF 页 10 · 原子类型 LIST_ITEM · 所在节 `§1.4.1 [How to Read a Domain Specification]`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_005`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
A hyperlinked codelist name and an asterisk (*) indicate that the variable is subject to either the named codelist from the CDISC Controlled Terminology or to an external dictionary. The specific dictionary is identified in the metadata.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0010.txt` 第 12-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11|                   domain, value-level metadata would indicate where each codelist is applicable.
 12|              ▪    A hyperlinked codelist name and an asterisk (*) indicate that the variable is subject to either the
 13|                   named codelist from the CDISC Controlled Terminology or to an external dictionary. The specific
 14|                   dictionary is identified in the metadata.
 15|          o   Format: "ISO 8601 datetime or interval" or "ISO 8601 duration" in plain text indicates that the variable
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:91` (来源: decision.evidence.hit):

~~~~
  91|     - A hyperlinked codelist name and an asterisk (*) indicate that the variable is subject to either the named codelist from the CDISC Controlled Terminology or to an external dictionary. The specific dictionary is identified in the metadata.
~~~~

### 14. `ig34_p0011_a008` — gate:REWRITE_OK

- PDF 页 11 · 原子类型 SENTENCE · 所在节 `§2.1 Observations and Variables`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_026`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Variables can be classified into 5 major roles:
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0011.txt` 第 8-8 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7| determines the type of information conveyed by the variable about each distinct observation and how it can be used.
  8| Variables can be classified into 5 major roles:
  9|     •    Identifier variables, such as those that identify the study, subject, domain, and sequence number of the
~~~~

KB 现文: `knowledge_base/chapters/ch02_fundamentals.md:15` (来源: decision.evidence.hit):

~~~~
  15| Variables can be classified into 5 major roles:
~~~~

### 15. `ig34_p0012_a017` — gate:REWRITE_OK

- PDF 页 12 · 原子类型 LIST_ITEM · 所在节 `§2.3 The General Observation Classes`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_026`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The Findings class captures the observations resulting from planned evaluations to address specific tests or questions (e.g., laboratory tests, ECG testing, questions listed on questionnaires).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0012.txt` 第 26-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25|          (e.g., adverse events) or prior to the trial (e.g., medical history).
 26|     •    The Findings class captures the observations resulting from planned evaluations to address specific tests or
 27|          questions (e.g., laboratory tests, ECG testing, questions listed on questionnaires).
 28| In most cases, the choice of observation class appropriate to a specific collection of data can be easily determined
~~~~

KB 现文: `knowledge_base/chapters/ch02_fundamentals.md:53` (来源: decision.evidence.hit):

~~~~
  53| - The **Findings** class captures the observations resulting from planned evaluations to address specific tests or questions (e.g., laboratory tests, ECG testing, questions listed on questionnaires).
~~~~

### 16. `ig34_p0012_a028` — gate:REWRITE_OK

- PDF 页 12 · 原子类型 LIST_ITEM · 所在节 `§2.4 Datasets Other than General Observation Class Domains`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_026`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Relationship datasets, such as the RELREC and SUPP-- datasets. These are described in Section 8, Representing Relationships and Data.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0012.txt` 第 45-46 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 44|          Section 7, Trial Design Model Datasets.
 45|     •    Relationship datasets, such as the RELREC and SUPP-- datasets. These are described in Section
 46|          8, Representing Relationships and Data.
~~~~

KB 现文: `knowledge_base/chapters/ch02_fundamentals.md:67` (来源: decision.evidence.hit):

~~~~
  67| - Relationship datasets, such as the RELREC and SUPP-- datasets. These are described in Section 8, Representing Relationships and Data.
~~~~

### 17. `ig34_p0043_a013` — gate:REWRITE_OK

- PDF 页 43 · 原子类型 SENTENCE · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch04`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
--ENRF is used to identify the end of an observation relative to the sponsor-defined study reference period.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0043.txt` 第 18-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| --STRF is used to identify the start of an observation relative to the sponsor-defined study reference period.
 18| --ENRF is used to identify the end of an observation relative to the sponsor-defined study reference period.
 19| Allowable values for --STRF are "BEFORE", "DURING", "DURING/AFTER", "AFTER", and "UNKNOWN".
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:934` (来源: decision.evidence.hit):

~~~~
 934| --STRF is used to identify the start of an observation relative to the sponsor-defined study reference period. --ENRF is used to identify the end of an observation relative to the sponsor-defined study reference period.
~~~~

### 18. `ig34_p0043_a023` — gate:REWRITE_OK

- PDF 页 43 · 原子类型 SENTENCE · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch04`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Some sponsors may wish to derive --STRF and --ENRF for analysis or reporting purposes even when dates are collected.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0043.txt` 第 32-33 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31| CMSTRF, not CMENRF. Note also that the information collected is relative to the study reference period, which
 32| meets the definition of CMSTRF.Some sponsors may wish to derive --STRF and --ENRF for analysis or reporting
 33| purposes even when dates are collected. Sponsors are cautioned that doing so in conjunction with directly collecting
 34| or mapping data such as "BEFORE", "PRIOR", and "ONGOING" to --STRF and --ENRF will blur the distinction
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:949` (来源: decision.evidence.hit):

~~~~
 949| Some sponsors may wish to derive --STRF and --ENRF for analysis or reporting purposes even when dates are collected. Sponsors are cautioned that doing so in conjunction with directly collecting or mapping data such as "BEFORE", "PRIOR", and "ONGOING" to --STRF and --ENRF will blur the distinction between collected and derived values within the domain. Sponsors wishing to do such derivations are instead encouraged to use analysis datasets for this derived data.
~~~~

### 19. `ig34_p0044_a002` — gate:REWRITE_OK

- PDF 页 44 · 原子类型 SENTENCE · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch04`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Allowable values for --STRTPT and --ENRTPT are as follows.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0044.txt` 第 2-2 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| reference period, the timing variables --STRTPT, --STTPT, --ENRTPT, and --ENTPT are defined by each sponsor
  2| for each study. Allowable values for --STRTPT and --ENRTPT are as follows.
  3| If the reference time point corresponds to the date of collection or assessment:
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:966` (来源: decision.evidence.hit):

~~~~
 966| Allowable values for --STRTPT and --ENRTPT are as follows.
~~~~

### 20. `ig34_p0044_a004` — gate:REWRITE_OK

- PDF 页 44 · 原子类型 LIST_ITEM · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch04`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Start values: An observation can start BEFORE that time point, can start COINCIDENT with that time point, or it can be UNKNOWN when it started.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0044.txt` 第 4-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3| If the reference time point corresponds to the date of collection or assessment:
  4|     •    Start values: An observation can start BEFORE that time point, can start COINCIDENT with that time
  5|          point, or it can be UNKNOWN when it started.
  6|     •    End values: An observation can end BEFORE that time point, can end COINCIDENT with that time point,
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:970` (来源: decision.evidence.hit):

~~~~
 970| - Start values: An observation can start BEFORE that time point, can start COINCIDENT with that time point, or it can be UNKNOWN when it started.
~~~~

### 21. `ig34_p0044_a013` — gate:REWRITE_OK

- PDF 页 44 · 原子类型 SENTENCE · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_028`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Assumptions:
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0044.txt` 第 20-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19| Example 1: Medical History
 20| Assumptions:
 21|     •    CRF contains "Year Started" and checkbox for "Active"
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:990,1019,1035` (来源: decision.evidence.hit):

~~~~
 990| Assumptions:
1019| Assumptions:
1035| Assumptions:
~~~~

