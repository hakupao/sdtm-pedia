# T4.1 总闸样本包 2/4 (行 22-42 / 84)

> 由 `scripts/t4/t4_sample.py` (seed 20261127) 生成, `scripts/t4/t4_render.py` 渲染. 只读材料.

### 22. `ig34_p0151_a0013` — gate:REWRITE_OK

- PDF 页 151 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_011`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | Yes | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0151.txt` 第 17-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 16| Rash                No
 17|                     Yes
 18| Wheezing            No
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:13,14,15,16,43,44,45,48,80,82` (来源: decision.evidence.hit):

~~~~
  13| | Rash | No  Yes | |
  14| | Wheezing | No  Yes | |
  15| | Edema | No  Yes | |
~~~~

### 23. `ig34_p0153_a0009` — gate:REWRITE_OK

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent` · 批 `T1:pack_011`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o Unknown |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 9-9 行 (自动定位, 词覆盖 0.5; 版式以原 PDF 为准):

~~~~
  8|                                                               ○ Other trauma
  9|                                                               ○ Unknown
 10| What was the location of the fracture?                        _____
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:77-77` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:77 (score 0.5)):

~~~~
  77| | How did fracture occur? | ( ) Pathologic  ( ) Fall  ( ) Other trauma  ( ) Unknown |
~~~~

### 24. `ig34_p0153_a0019` — gate:REWRITE_OK

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 ERROR) · 判定规则 `T1-two-agent` · 批 `T1:pack_011`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o Surgery |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 19-19 行 (自动定位, 词覆盖 0.5; 版式以原 PDF 为准):

~~~~
 18|                                                               □ Traction
 19|                                                               □ Surgery
 20| Were there any complications of the fracture?                 ○ Yes
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:81-81` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:81 (score 0.5)):

~~~~
  81| | If therapeutic measures were required, select all that apply. | [ ] Casting/immobilization  [ ] Traction  [ ] Surgery |
~~~~

### 25. `ig34_p0010_a025` — gate:REAL_GAP

- PDF 页 10 · 原子类型 SENTENCE · 所在节 `§1.5 [Known Issues]`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch01`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This distinction between --LNKID and --LNKGRP, and the appropriateness of using other identification variables for linking, will be clarified in a future release of the SDTMIG and/or Model document, and at that time examples in the SDTMIG will be systematically reviewed and updated to reflect that clarification.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0010.txt` 第 40-43 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39| have an IDVAR of --LNKID (and not --LNKGRP). The examples in this version of the SDTMIG have not been
 40| systematically reviewed to implement this distinction between --LNKID and --LNKGRP. This distinction between -
 41| -LNKID and --LNKGRP, and the appropriateness of using other identification variables for linking, will be clarified
 42| in a future release of the SDTMIG and/or Model document, and at that time examples in the SDTMIG will be
 43| systematically reviewed and updated to reflect that clarification.
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:109` (来源: decision.evidence.hit):

~~~~
 109| The definition of --LNKID says that it is "used to identify a record," and the definition of --LNKGRP says that it is "used to identify a group of records." This implies that when setting up a relationship in RELREC, a row where RELTYPE = ONE will have an IDVAR of --LNKID (and not --LNKGRP); a row where RELTYPE = MANY will have an IDVAR of --LNKGRP (and not --LNKID). The examples in this version of the SDTMIG have not been systematically reviewed to implement this distinction between --LNKID and --LNKGRP. This distinction between --LNKID and --LNKGRP, and the appropriateness of using other identification variables for linking, will be clarified in a future release of the SDTMIG and/or Model document, and at that time examples in the SDTMIG will be systematically reviewed and updated to reflect that clarification.
~~~~

### 26. `ig34_p0014_a005` — gate:REAL_GAP

- PDF 页 14 · 原子类型 LIST_ITEM · 所在节 `§2.6 Creating a New Domain`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch02`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
If it is necessary to represent relationships between data that are hierarchical in nature (e.g., a parent record must be observed before child records), then establish a domain pair (e.g., MB/MS, PC/PP). Note: Domain pairs have been modeled for microbiology data (MB/MS domains) and pharmacokinetics (PK) data (PC/PP domains) to enable dataset-level relationships to be described using RELREC. The domain pair uses DOMAIN as an identifier to group parent records (e.g., MB) from child records (e.g., MS) and enables a dataset-level relationship to be described in RELREC. Without using DOMAIN to facilitate description of the data relationships, RELREC, as currently defined, could not be used without introducing a variable that would group data like DOMAIN.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0014.txt` 第 13-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12|           separate questionnaires into the QS domain, prior and concomitant medications in the CM domain).
 13|      o    If it is necessary to represent relationships between data that are hierarchical in nature (e.g., a parent
 14|           record must be observed before child records), then establish a domain pair (e.g., MB/MS, PC/PP).
 15|           Note: Domain pairs have been modeled for microbiology data (MB/MS domains) and
 16|           pharmacokinetics (PK) data (PC/PP domains) to enable dataset-level relationships to be described
 17|           using RELREC. The domain pair uses DOMAIN as an identifier to group parent records (e.g., MB)
 18|           from child records (e.g., MS) and enables a dataset-level relationship to be described in RELREC.
 19|           Without using DOMAIN to facilitate description of the data relationships, RELREC, as currently
 20|           defined, could not be used without introducing a variable that would group data like DOMAIN.
 21| 2.   Check the SDTM Draft Domains area of the CDISC wiki
~~~~

KB 现文: `knowledge_base/chapters/ch02_fundamentals.md:98` (来源: decision.evidence.hit):

~~~~
  98|    - If it is necessary to represent relationships between data that are hierarchical in nature (e.g., a parent record must be observed before child records), then establish a domain pair (e.g., MB/MS, PC/PP). Note: Domain pairs have been modeled for microbiology data (MB/MS domains) and pharmacokinetics (PK) data (PC/PP domains) to enable dataset-level relationships to be described using RELREC. The domain pair uses DOMAIN as an identifier to group parent records (e.g., MB) from child records (e.g., MS) and enables a dataset-level relationship to be described in RELREC. Without using DOMAIN to facilitate description of the data relationships, RELREC, as currently defined, could not be used without introducing a variable that would group data like DOMAIN.
~~~~

### 27. `ig34_p0029_a028` — gate:REAL_GAP

- PDF 页 29 · 原子类型 SENTENCE · 所在节 `§4.2.5 [Convention for Missing Values]`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch04`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Conventions for representing observations not done, using the SDTM --STAT and --REASND variables, are addressed in Section 4.5.1.2, Tests Not Done, and the individual domain models.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0029.txt` 第 42-44 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 41| 4.2.5 Convention for Missing Values
 42| Missing values for individual data items should be represented by nulls. Conventions for representing observations
 43| not done, using the SDTM --STAT and --REASND variables, are addressed in Section 4.5.1.2, Tests Not Done, and
 44| the individual domain models.
 45| 
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:320` (来源: decision.evidence.hit):

~~~~
 320| Missing values for individual data items should be represented by nulls. Conventions for representing observations not done, using the SDTM --STAT and --REASND variables, are addressed in Section 4.5.1.2, Tests Not Done, and the individual domain models.
~~~~

### 28. `ig34_p0043_a034` — gate:REAL_GAP

- PDF 页 43 · 原子类型 SENTENCE · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **REAL_GAP** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T2-fix+PASS` · 批 `B-ch04`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Unlike the variables --STRF and --ENRF, which for all domains are defined relative to one study [TRUNCATED_AT_PAGE_BOUNDARY]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0043.txt` 第 47-50 行 (自动定位, 词覆盖 0.85; 版式以原 PDF 为准):

~~~~
 46| timing assessments (e.g., "Prior", "Ongoing") that are collected at other times of the study. As a result, 4 new timing
 47| variables were added in SDTMIG v3.1.2 to express a similar concept at any point in time. The variables --STRTPT
 48| and --ENRTPT contain values similar to --STRF and --ENRF, but may be anchored with any timing description or
 49| date/time value expressed in the respective --STTPT and --ENTPT variables, and are not limited to the study
 50| reference period. Unlike the variables --STRF and --ENRF, which for all domains are defined relative to one study
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:955-955` (来源: fuzzy locate (score 0.85)):

~~~~
 955| Although the variables --STRF and --ENRF are useful in the case when relative timing assessments are made coincident with the start and end of the study reference period, they may not be suitable for expressing relative timing assessments (e.g., "Prior", "Ongoing") that are collected at other times of the study. As a result, 4 new timing variables were added in SDTMIG v3.1.2 to express a similar concept at any point in time. The variables --STRTPT and --ENRTPT contain values similar to --STRF and --ENRF, but may be anchored with any timing description or date/time value expressed in the respective --STTPT and --ENTPT variables, and are not limited to the study reference period. Unlike the variables --STRF and --ENRF, which for all domains are defined relative to one study reference period, the timing variables --STRTPT, --STTPT, --ENRTPT, and --ENTPT are defined by each sponsor for each study.
~~~~

### 29. `ig34_p0045_a018` — gate:REAL_GAP

- PDF 页 45 · 原子类型 LIST_ITEM · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch04`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Collection of "Outcome" includes checkboxes for "Continuing" and "Unknown", to be used, if necessary, at the end of the subject's participation in the trial
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0045.txt` 第 16-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15|     •    CRF contains "Start Date", "Stop Date"
 16|     •    Collection of "Outcome" includes checkboxes for "Continuing" and "Unknown", to be used, if necessary, at
 17|          the end of the subject's participation in the trial
 18|     •    No assessment date or visit information was collected
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1038` (来源: decision.evidence.hit):

~~~~
1038| - Collection of "Outcome" includes checkboxes for "Continuing" and "Unknown", to be used, if necessary, at the end of the subject's participation in the trial
~~~~

### 30. `ig34_p0133_a021` — gate:REAL_GAP

- PDF 页 133 · 原子类型 SENTENCE · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-AE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
An events domain that contains data describing untoward medical occurrences in a patient or subjects that are administered a pharmaceutical product and which may not necessarily have a causal relationship with the treatment.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0133.txt` 第 37-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36| AE – Description/Overview
 37| An events domain that contains data describing untoward medical occurrences in a patient or subjects that are administered a pharmaceutical product and which
 38| may not necessarily have a causal relationship with the treatment.
 39| 
~~~~

KB 现文: `knowledge_base/domains/AE/assumptions.md:17` (来源: decision.evidence.hit):

~~~~
  17| An events domain that contains data describing untoward medical occurrences in a patient or subjects that are administered a pharmaceutical product and which may not necessarily have a causal relationship with the treatment.
~~~~

### 31. `ig34_p0185_a020` — gate:REAL_GAP

- PDF 页 185 · 原子类型 SENTENCE · 所在节 `§6.3.3 ECG Test Results (EG)`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-EG`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
A findings domain that contains ECG data, including position of the subject, method of evaluation, all cycle measurements and all findings from the ECG including an overall interpretation if collected or derived.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0185.txt` 第 24-25 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 23| EG – Description/Overview
 24| A findings domain that contains ECG data, including position of the subject, method of evaluation, all cycle measurements and all findings from the ECG
 25| including an overall interpretation if collected or derived.
 26| EG – Specification
~~~~

KB 现文: `knowledge_base/domains/EG/assumptions.md:5` (来源: decision.evidence.hit):

~~~~
   5| A findings domain that contains ECG data, including position of the subject, method of evaluation, all cycle measurements and all findings from the ECG including an overall interpretation if collected or derived.
~~~~

### 32. `ig34_p0196_a004` — gate:REAL_GAP

- PDF 页 196 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-LB`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| --SPEC | Specimen Material Type | Char | * | Record Qualifier | Defines the type of specimen used for a measurement. Subject to domain-specific test code controlled terminology. | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0196.txt` 第 9-10 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  8|                                                                            Qualifier
  9| --SPEC        Specimen Material Type         Char   *                      Record           Defines the type of specimen used for a measurement. Subject to domain-specific test code controlled               Perm
 10|                                                                            Qualifier        terminology.
 11| --METHOD      Method of Test or              Char   *                      Record           Method of the test or examination. Subject to domain-specific test code controlled terminology.                    Perm
~~~~

KB 现文: `knowledge_base/domains/LB/assumptions.md:41` (来源: decision.evidence.hit):

~~~~
  41| | --SPEC | Specimen Material Type | Char | * | Record Qualifier | Defines the type of specimen used for a measurement. Subject to domain-specific test code controlled terminology. | Perm |
~~~~

### 33. `ig34_p0215_a014` — gate:REAL_GAP

- PDF 页 215 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-CP`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-6: Illustrate how the sponsor uses CPSPTSTD to combine details of a test into a single variable to align with the lab/sponsor data repository or dictionary and to aid understanding of the test. Rows 1-4 introduce CPSPTSTD using simple tests for dendritic cells to set the stage for the more complex tests shown in rows 5-6. Those rows incorporate an additional marker (CD1c-) to define the plasmacytoid sublineage, and a non-lineage, non-cell state marker (CD303+) that is of interest. Although the entire marker string is in CPMRKSTR, it is easy to miss that CD303+ was also used to subdivide the population, even though it is not considered to define a sublineage. The lab/sponsor test nomenclature reinforces the use of CD303 by calling them a "CD303+ Dendritic Cell Plasmacytoid Sub" (subset) in the CPSPTSTD for rows 5-6. The information presented by the lab/sponsor helps the data recipient to quickly understand such nuances of a test at a glance, which is especially useful as the complexity of a test increases.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0215.txt` 第 29-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28| lab/sponsor dictionaries using a single variable which is not managed by CDISC Controlled Terminology.
 29| Rows 1-6:                Illustrate how the sponsor uses CPSPTSTD to combine details of a test into a single variable to align with the lab/sponsor data repository or dictionary and to aid understanding of the test. Rows 1-4
 30|                          introduce CPSPTSTD using simple tests for dendritic cells to set the stage for the more complex tests shown in rows 5-6. Those rows incorporate an additional marker (CD1c-) to define the
 31|                          plasmacytoid sublineage, and a non-lineage, non-cell state marker (CD303+) that is of interest. Although the entire marker string is in CPMRKSTR, it is easy to miss that CD303+ was also used to
 32|                          subdivide the population, even though it is not considered to define a sublineage. The lab/sponsor test nomenclature reinforces the use of CD303 by calling them a "CD303+ Dendritic Cell
 33|                          Plasmacytoid Sub" (subset) in the CPSPTSTD for rows 5-6. The information presented by the lab/sponsor helps the data recipient to quickly understand such nuances of a test at a glance, which is
 34|                          especially useful as the complexity of a test increases.
 35| Rows 7-10:               Illustrate how CPSPTSTD might preface the name of a cell population with cell state marker(s) (e.g., CD83+ in rows 7-8) in addition to non-cell state, non-sublineage marker(s). Rows 9-10
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:194` (来源: decision.evidence.hit):

~~~~
 194| **Rows 1-6:** Illustrate how the sponsor uses CPSPTSTD to combine details of a test into a single variable to align with the lab/sponsor data repository or dictionary and to aid understanding of the test. Rows 1-4 introduce CPSPTSTD using simple tests for dendritic cells to set the stage for the more complex tests shown in rows 5-6. Those rows incorporate an additional marker (CD1c-) to define the plasmacytoid sublineage, and a non-lineage, non-cell state marker (CD303+) that is of interest. Although the entire marker string is in CPMRKSTR, it is easy to miss that CD303+ was also used to subdivide the population, even though it is not considered to define a sublineage. The lab/sponsor test nomenclature reinforces the use of CD303 by calling them a "CD303+ Dendritic Cell Plasmacytoid Sub" (subset) in the CPSPTSTD for rows 5-6. The information presented by the lab/sponsor helps the data recipient to quickly understand such nuances of a test at a glance, which is especially useful as the complexity of a test increases.
~~~~

### 34. `ig34_p0263_a006` — gate:REAL_GAP

- PDF 页 263 · 原子类型 SENTENCE · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-MB`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The RELREC table shows how culture start and end dates from BE were linked to the culture results in MB and MS using --LNKID and --LNKGRP. It also shows how the detection record (MB) was linked to the susceptibility results (MS) from the NAAT, using --REFID.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0263.txt` 第 7-8 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  6| 
  7| The RELREC table shows how culture start and end dates from BE were linked to the culture results in MB and MS using --LNKID and --LNKGRP. It also shows how the detection record (MB) was linked to the
  8| susceptibility results (MS) from the NAAT, using --REFID.
  9| relrec.xpt
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:218` (来源: decision.evidence.hit):

~~~~
 218| The RELREC table shows how culture start and end dates from BE were linked to the culture results in MB and MS using --LNKID and --LNKGRP. It also shows how the detection record (MB) was linked to the susceptibility results (MS) from the NAAT, using --REFID.
~~~~

### 35. `sv20_p0004_a012` — gate:REAL_GAP

- PDF 页 4 · 原子类型 SENTENCE · 所在节 `§1 [INTRODUCTION]`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-model01`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This document describes the basic concepts and general structure of the model.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0004.txt` 第 20-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19| The SDTM has been designed to accommodate the broadest range of human and animal study data in a standardized
 20| manner. This document describes the basic concepts and general structure of the model. Individual implementation
 21| guides (IGs) have been created to provide specific recommendations for numerous domains of data commonly
~~~~

KB 现文: `knowledge_base/model/01_concepts_and_terms.md:15` (来源: decision.evidence.hit):

~~~~
  15| The SDTM has been designed to accommodate the broadest range of human and animal study data in a standardized manner. This document describes the basic concepts and general structure of the model. Individual implementation guides (IGs) have been created to provide specific recommendations for numerous domains of data commonly collected in human, animal, and medical device studies, identifying which variables from a general observation class may apply. These IGs also describe basic assumptions and business rules, and provide numerous examples for mapping data to the standard format. Sponsors wishing to represent data in the standard formats should consult the IGs before preparing datasets based on the SDTM. The following implementation guides have been published by CDISC:
~~~~

### 36. `sv20_p0004_a020` — gate:REAL_GAP

- PDF 页 4 · 原子类型 LIST_ITEM · 所在节 `§1 [INTRODUCTION]`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-model01`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The Standard for Exchange of Nonclinical Data Implementation Guide (SENDIG) https://www.cdisc.org/standards/foundational/send
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0004.txt` 第 33-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 32|           https://www.cdisc.org/standards/foundational/sdtmig/sdtmig-ap
 33|      •    The Standard for Exchange of Nonclinical Data Implementation Guide (SENDIG)
 34|           https://www.cdisc.org/standards/foundational/send
 35|      •    The Standard for Exchange of Nonclinical Data Implementation Guide: Developmental and Reproductive
~~~~

KB 现文: `knowledge_base/model/01_concepts_and_terms.md:20` (来源: decision.evidence.hit):

~~~~
  20| - The Standard for Exchange of Nonclinical Data Implementation Guide (SENDIG) https://www.cdisc.org/standards/foundational/send
~~~~

### 37. `ig34_p0116_a013` — gate:VALUE_DIFF

- PDF 页 116 · 原子类型 TABLE_ROW · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **VALUE_DIFF** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T2-fix+PASS` · 批 `B-EX`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | 56789 | EC | 56789001 | 4 | BOTTLE | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT | 2002-07-02T07:30 | 2002-07-02T07:30 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0116.txt` 第 18-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17|                                  1                                                                                                       1           02T07:30   02T07:30                 PRIOR               BREAKFAST
 18| 4   56789   EC     56789001 4    BOTTLE                Y         Y         1       TABLET,            TABLET,           QD       ORAL    TREATMENT   2002-07-   2002-07-   2      2      30 MINUTES   -PT30M STD
 19|                                  2                                                 COATED             COATED                             1           02T07:30   02T07:30                 PRIOR               BREAKFAST
 20| 5   56789   EC     56789001 5    BOTTLE                Y         Y         1       CAPSULE            CAPSULE           QD       ORAL    TREATMENT   2002-07-   2002-07-   3      3      30 MINUTES   -PT30M STD
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:270-270` (来源: near triage kb_loc knowledge_base/domains/EX/examples.md:270 (score 1.0)):

~~~~
 270| | 4 | 56789 | EC | 56789001 | 4 | BOTTLE 2 | Y | Y | 1 | TABLET, COATED | TABLET, COATED | QD | ORAL | TREATMENT 1 | 2002-07-02T07:30 | 2002-07-02T07:30 | 2 | 2 | 30 MINUTES PRIOR | -PT30M | STD BREAKFAST |
~~~~

### 38. `ig34_p0141_a007` — gate:VALUE_DIFF

- PDF 页 141 · 原子类型 SENTENCE · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-AE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In this example, a CRF module included at several visits asked whether nausea, vomiting, or diarrhea occurred. The responses to the probing questions "Yes", "No", or "Not Done" were represented in the Findings About (FA) domain (see Section 6.4, Findings About Events or Interventions). If "Yes", the investigator was instructed to complete the AE CRF. In the AE dataset, data on AEs solicited via prespecification on the CRF have an AEPRESP value of "Y". For AEs solicited by a general question, AEPRESP is null. RELREC may be used to relate AE records and FA records.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0141.txt` 第 14-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13| Example 2
 14| In this example, a CRF module included at several visits asked whether nausea, vomiting, or diarrhea occurred. The responses to the probing questions "Yes", "No", or "Not Done" were represented in the Findings
 15| About (FA) domain (see Section 6.4, Findings About Events or Interventions). If “Yes”, the investigator was instructed to complete the AE CRF. In the AE dataset, data on AEs solicited via prespecification on the
 16| CRF have an AEPRESP value of "Y". For AEs solicited by a general question, AEPRESP is null. RELREC may be used to relate AE records and FA records.
 17| Rows 1-2:       Show that nausea and vomiting were prespecified on a CRF, as indicated by AEPRESP = "Y". The subject did not experience diarrhea, so no record for that term exists in the AE dataset.
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:21` (来源: decision.evidence.hit):

~~~~
  21| In this example, a CRF module included at several visits asked whether nausea, vomiting, or diarrhea occurred. The responses to the probing questions "Yes", "No", or "Not Done" were represented in the Findings About (FA) domain (see Section 6.4, Findings About Events or Interventions). If “Yes”, the investigator was instructed to complete the AE CRF. In the AE dataset, data on AEs solicited via prespecification on the CRF have an AEPRESP value of "Y". For AEs solicited by a general question, AEPRESP is null. RELREC may be used to relate AE records and FA records.
~~~~

### 39. `ig34_p0210_a002` — gate:VALUE_DIFF

- PDF 页 210 · 原子类型 TABLE_HEADER · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **VALUE_DIFF** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `C7-atom-not-in-PDF` · 批 `B-CP`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPTESTCD | CPTEST | CPMRKSTR | CPCAT | CPORRES | CPORRESU | CPSTRESC | CPSTRESN | CPSTRESU | CPRESSCL | CPRESTYP | CPSPEC | CPMETHOD | CPDTC |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0210.txt` 第 2-2 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| cp.xpt
  2| Row STUDYID DOMAIN USUBJID       CPSEQ   CPTESTCD CPTEST                      CPMRKSTR                     CPCAT             CPORRES CPORRESU CPSTRESC CPSTRESU CPSTRESN CPRESSCL     CPRESTYP                           CPSPEC CPMETHOD       CPDTC
  3| 1   ABCD    CP     ABCD-         1       WBC      Leukocytes                  CD45+                        IMMUNOPHENOTYPING 6630    10^6/L   6630     10^6/L   6630     QUANTITATIVE NUMBER                             BLOOD  FLOW           2021-08-
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:31-31` (来源: near triage kb_loc knowledge_base/domains/CP/examples.md:31 (score 1.0)):

~~~~
  31| | Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPTESTCD | CPTEST | CPMRKSTR | CPCAT | CPORRES | CPORRESU | CPSTRESC | CPSTRESU | CPSTRESN | CPRESSCL | CPRESTYP | CPSPEC | CPMETHOD | CPDTC |
~~~~

### 40. `ig34_p0210_a009` — gate:VALUE_DIFF

- PDF 页 210 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-CP`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 7 | ABCD | CP | ABCD-001-001 | 7 | TLYLY | TLym/Lym | CD45+CD3+CD19-CD14-CD56-/CD45+FSC SSC | IMMUNOPHENOTYPING | 64.8 | % | 64.8 | % | 64.8 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0210.txt` 第 15-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14|                    001-001                                                                                                                                                                             CONCENTRATION            CYTOMETRY      16T04:20
 15| 7   ABCD    CP     ABCD-         7       TLYLY      TLym/Lym                  CD45+CD3+CD19-CD14-CD56-     IMMUNOPHENOTYPING 64.8     %            64.8         %            64.8         QUANTITATIVE NUMBER FRACTION   BLOOD  FLOW           2021-08-
 16|                    001-001                                                    /CD45+FSC SSC                                                                                                                                     CYTOMETRY      16T04:20
 17| 8   ABCD    CP     ABCD-         8       TLYH       TLym Help                 CD45+CD3+CD4+CD8-            IMMUNOPHENOTYPING 425      10^6/L       425          10^6/L       425          QUANTITATIVE NUMBER            BLOOD  FLOW           2021-08-
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:39` (来源: decision.evidence.hit):

~~~~
  39| | 7 | ABCD | CP | ABCD-001-001 | 7 | TLYLY | TLym/Lym | CD45+CD3+CD19-CD14-CD56-/CD45+FSC SSC | IMMUNOPHENOTYPING | 64.8 | % | 64.8 | % | 64.8 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
~~~~

### 41. `ig34_p0210_a018` — gate:VALUE_DIFF

- PDF 页 210 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-CP`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 16 | ABCD | CP | ABCD-001-001 | 16 | TLYHTLYC | TLym Help/TLym Cytx | CD45+CD3+CD4+CD8-/CD45+CD3+CD4-CD8+ | IMMUNOPHENOTYPING | 0.62 | | | 0.62 | | 0.62 | QUANTITATIVE | RATIO | BLOOD | CALCULATION | 2021-08-16T04:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0210.txt` 第 33-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 32| 15    ABCD     CP      ABCD-     15      NKLE       NK Cells/Leuk             CD45+CD3-CD19-CD14-          IMMUNOPHENOTYPING 3.5      %            3.5          %            3.5          QUANTITATIVE NUMBER FRACTION   BLOOD   FLOW          2021-08-
 33|                        001-001                                                CD56+FSC SSC/CD45+                                                                                                                                 CYTOMETRY     16T04:20
 34| 16    ABCD     CP      ABCD-     16      TLYHTLYC   TLym Help/TLym Cytx       CD45+CD3+CD4+CD8-            IMMUNOPHENOTYPING 0.62                  0.62                      0.62         QUANTITATIVE RATIO             BLOOD   CALCULATION   2021-08-
 35|                        001-001                                                /CD45+CD3+CD4-CD8+                                                                                                                                               16T04:20
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:48` (来源: decision.evidence.hit):

~~~~
  48| | 16 | ABCD | CP | ABCD-001-001 | 16 | TLYHTLYC | TLym Help/TLym Cytx | CD45+CD3+CD4+CD8-/CD45+CD3+CD4-CD8+ | IMMUNOPHENOTYPING | 0.62 | | 0.62 | | 0.62 | QUANTITATIVE | RATIO | BLOOD | CALCULATION | 2021-08-16T04:20 |
~~~~

### 42. `ig34_p0225_a017` — gate:VALUE_DIFF

- PDF 页 225 · 原子类型 FIGURE · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **VALUE_DIFF** · 终态 **EQUIVALENT** (T3 前 MISSING) · 判定规则 `T2-fix+PASS` · 批 `B-GF`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
gf.xpt Example 2 dataset table: 3 rows showing STUDYID, DOMAIN, USUBJID, GFSEQ, GFREFID, GFTESTCD, GFTEST, GFTSDTL, GFORRES, GFORREF, GFSTRESC, GFSTRESN, GFINHERT, GFGENREF, GFCHROM, GFSYM, GFSYMTYP, GFGENLOC, GFSEQID, GFPVRID, GFNAM, GFSPEC, GFMETHOD, VISITNUM, VISIT, VISITDY, GFDTC, GFDY columns; C12345 subjects, NA07000/NA00131 NHOID, SNV GFTESTCD, GENOTYPE GFTEST, GRCh38.p13 GFGENREF, ABCG2 GFSYM, rs2231142 GFPVRID, ACME LABS, DNA, REAL TIME POLYMERASE CHAIN REACTION, SCREENING visit, 2020-06-25 GFDTC
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0225.txt` 第 51-64 行 (自动定位, 词覆盖 0.852; 版式以原 PDF 为准):

~~~~
 50| Row 3:                     Shows a subject genotype which is homozygous for the nucleotide in the reference sequence.
 51| gf.xpt
 52| Row    STUDYID       DOMAIN         USUBJID      GFSEQ       GFREFID    GFTESTCD          GFTEST             GFTSTDTL            GFORRES           GFORREF        GFSTRESC       GFSTREFC         GFINHERT          GFGENREF         GFCHROM          GFSYM   GFSYMTYP                GFGENLOC            GFSEQID                     GFPVRID            GFNAM            GFSPEC   GFMETHOD                 VISITNUM      VISIT              VISITDY      GFDTC          GFDY
 53| 1      C12345        GF             C12345-      1           NA18537    SNV               Single             GENOTYPE            T/T               G/G            T/T            G/G              GERMLINE          GRCh38.p13       4                ABCG2   GENE WITH               4:88131171          ENSG00000118777             rs2231142          ACME             DNA      REAL_TIME                1             SCREENING          -1           2020-06-       -3
 54|                                     001                                                   Nucleotide                                                                                              VARIATION                                                   PROTEIN                                                                                    LABS                      POLYMERASE CHAIN                                                       25
 55|                                                                                           Variation                                                                                                                                                           PRODUCT                                                                                                              REACTION
 56| 2      C12345        GF             C12345-      2           NA07000    SNV               Single             GENOTYPE            G/T               G/G            G/T            G/G              GERMLINE          GRCh38.p13       4                ABCG2   GENE WITH               4:88131171          ENSG00000118777             rs2231142          ACME             DNA      REAL_TIME                1             SCREENING          -1           2020-06-       -3
 57|                                     002                                                   Nucleotide                                                                                              VARIATION                                                   PROTEIN                                                                                    LABS                      POLYMERASE CHAIN                                                       25
 58|                                                                                           Variation                                                                                                                                                           PRODUCT                                                                                                              REACTION
 59| 3      C12345        GF             C12345-      3           NA00131    SNV               Single             GENOTYPE            G/G               G/G            G/G            G/G              GERMLINE          GRCh38.p13       4                ABCG2   GENE WITH               4:88131171          ENSG00000118777             rs2231142          ACME             DNA      REAL_TIME                1             SCREENING          -1           2020-06-       -3
 60|                                     003                                                   Nucleotide                                                                                              VARIATION                                                   PROTEIN                                                                                    LABS                      POLYMERASE CHAIN                                                       25
 61|                                                                                           Variation                                                                                                                                                           PRODUCT                                                                                                              REACTION
 62| 
 63| 
 64| Example 3
 65| This example shows transcription levels of genes ACTB and GAPDH and summarized scores from the transcription levels. Transcription levels and scores were determined using biocomputational analysis with wet
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:62-66` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:62 (score 0.82)):

~~~~
  62| | Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFREFID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFORREF | GFSTRESC | GFSTREFC | GFINHERT | GFGENREF | GFCHROM | GFSYM | GFSYMTYP | GFGENLOC | GFSEQID | GFPVRID | GFNAM | GFSPEC | GFMETHOD | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
  63| |-----|---------|--------|---------|-------|---------|----------|--------|----------|---------|---------|----------|----------|----------|----------|---------|-------|----------|----------|---------|---------|-------|--------|----------|----------|-------|---------|-------|------|
  64| | 1 | C12345 | GF | C12345-001 | 1 | NA18537 | SNV | Single Nucleotide Variation | GENOTYPE | T/T | G/G | T/T | G/G | GERMLINE VARIATION | GRCh38.p13 | 4 | ABCG2 | GENE WITH PROTEIN PRODUCT | 4:88131171 | ENSG00000118777 | rs2231142 | ACME LABS | DNA | REAL_TIME POLYMERASE CHAIN REACTION | 1 | SCREENING | -1 | 2020-06-25 | -3 |
  65| | 2 | C12345 | GF | C12345-002 | 2 | NA07000 | SNV | Single Nucleotide Variation | GENOTYPE | G/T | G/G | G/T | G/G | GERMLINE VARIATION | GRCh38.p13 | 4 | ABCG2 | GENE WITH PROTEIN PRODUCT | 4:88131171 | ENSG00000118777 | rs2231142 | ACME LABS | DNA | REAL_TIME POLYMERASE CHAIN REACTION | 1 | SCREENING | -1 | 2020-06-25 | -3 |
  66| | 3 | C12345 | GF | C12345-003 | 3 | NA00131 | SNV | Single Nucleotide Variation | GENOTYPE | G/G | G/G | G/G | G/G | GERMLINE VARIATION | GRCh38.p13 | 4 | ABCG2 | GENE WITH PROTEIN PRODUCT | 4:88131171 | ENSG00000118777 | rs2231142 | ACME LABS | DNA | REAL_TIME POLYMERASE CHAIN REACTION | 1 | SCREENING | -1 | 2020-06-25 | -3 |
~~~~

