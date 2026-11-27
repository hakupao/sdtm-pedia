# T4.1 第三轮补检包 2 — R3_IG34_EQUIV (25 条; 编号 T26-T50)

> 由 `scripts/t4/t4_round3_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 T).

### T26. `ig34_p0211_a005` — r3:R3_IG34_EQUIV

- PDF 页 211 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 3-4: Illustrate using CPCELSTA and CPCSMRKS to provide (1) the cell state descriptor in CPCELSTA, and (2) the markers used to define the cell state in CPCSMRKS. These variables further define CPTEST to be a subset of cells named in CPTEST, therefore the suffix "Sub" is appended to the value in CPTEST. In this example, the sponsor is interested in contrasting viable cells with those in the process of dying (non-viable), so each population is reported and the records differentiated using CPCELSTA and CPCSMRKS.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0211.txt` 第 15-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14|                  "VIABLE" is included in the gate name (CPGATE).
 15| Rows 3-4:        Illustrate using CPCELSTA and CPCSMRKS to provide (1) the cell state descriptor in CPCELSTA, and (2) the markers used to define the cell state in CPCSMRKS. These variables further define
 16|                  CPTEST to be a subset of cells named in CPTEST, therefore the suffix "Sub" is appended to the value in CPTEST. In this example, the sponsor is interested in contrasting viable cells with those in the
 17|                  process of dying (non-viable), so each population is reported and the records differentiated using CPCELSTA and CPCSMRKS.
 18| Rows 5-6:        Illustrate using CPCELSTA and CPCSMRKS for the apoptotic cell state. The sponsor is reporting the apoptotic lymphocyte subpopulation, both as a cell count (row 5) and as a percentage of total
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:73` (来源: live valid_hits):

~~~~
  73| **Rows 3-4:** Illustrate using CPCELSTA and CPCSMRKS to provide (1) the cell state descriptor in CPCELSTA, and (2) the markers used to define the cell state in CPCSMRKS. These variables further define CPTEST to be a subset of cells named in CPTEST, therefore the suffix "Sub" is appended to the value in CPTEST. In this example, the sponsor is interested in contrasting viable cells with those in the process of dying (non-viable), so each population is reported and the records differentiated using CPCELSTA and CPCSMRKS.
~~~~

### T27. `ig34_p0211_a008` — r3:R3_IG34_EQUIV

- PDF 页 211 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 9-11: Illustrate a need to pre-coordinate information into the test name when the test incorporates results from two or more records (e.g., a ratio) in which key component(s) of the test are split across multiple variables. In the example, rows 9 and 10 use the CPCELSTA variable to indicate that the measured lymphocyte subpopulation includes only viable cells (row 9) or dying (non-viable cells, row 10). The ratio of viable to nonviable lymphocytes in row 11 is calculated using data from rows 9 and 10.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0211.txt` 第 23-25 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 22|                  viability marker 7AAD is used in combination with apoptosis marker ANXV.
 23| Rows 9-11: Illustrate a need to pre-coordinate information into the test name when the test incorporates results from two or more records (e.g., a ratio) in which key component(s) of the test are split across multiple
 24|            variables. In the example, rows 9 and 10 use the CPCELSTA variable to indicate that the measured lymphocyte subpopulation includes only viable cells (row 9) or dying (non-viable cells, row 10). The
 25|            ratio of viable to nonviable lymphocytes in row 11 is calculated using data from rows 9 and 10.
 26|                  Because the ratio in row 11 is based on counts of both the viable (row 9) and the non-viable (row 10) lymphocyte subpopulations, it is not appropriate to use the CPCELSTA variable. Instead, the
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:79` (来源: live valid_hits):

~~~~
  79| **Rows 9-11:** Illustrate a need to pre-coordinate information into the test name when the test incorporates results from two or more records (e.g., a ratio) in which key component(s) of the test are split across multiple variables. In the example, rows 9 and 10 use the CPCELSTA variable to indicate that the measured lymphocyte subpopulation includes only viable cells (row 9) or dying (non-viable cells, row 10). The ratio of viable to nonviable lymphocytes in row 11 is calculated using data from rows 9 and 10.
~~~~

### T28. `ig34_p0214_a017` — r3:R3_IG34_EQUIV

- PDF 页 214 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-3: Incorporates both standard proportion analysis and single marker expression for a cell state marker in the B lymphocyte assay using CPGRPID to group the related record. In accordance with CP guidance for quantitative single marker expression, row 3 contains the marker being measured followed by "Expression". CPMRKSTR uses the recommended format of listing the marker being measured first, followed by the unit in which expression was quantified (median fluorescence intensity, MdFI in the example), and lastly by the complete marker string of the cell population on which expression was measured. The analyte is repeated as part of the target cell population string (CD95+ in the example). GATE and GATEDEF show the gating strategy so it is clear which gate was used to make the quantitative measurement of expression.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0214.txt` 第 41-45 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 40| CPGATE and CPGATDEF for reporting a full gating strategy and for reporting the total number of events counted within a gate.
 41| Rows 1-3:                Incorporates both standard proportion analysis and single marker expression for a cell state marker in the B lymphocyte assay using CPGRPID to group the related record. In accordance with CP
 42|                          guidance for quantitative single marker expression, row 3 contains the marker being measured followed by "Expression". CPMRKSTR uses the recommended format of listing the marker being
 43|                          measured first, followed by the unit in which expression was quantified (median fluorescence intensity, MdFI in the example), and lastly by the complete marker string of the cell population on which
 44|                          expression was measured. The analyte is repeated as part of the target cell population string (CD95+ in the example). GATE and GATEDEF show the gating strategy so it is clear which gate was used to
 45|                          make the quantitative measurement of expression.
 46| Rows 4-8:                Show a set of tests similar to those in rows 1-3, except that the marker being quantified is more narrowly restricted to a subpopulation of B lymphocytes (i.e., naive B cells), which are identified using a
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:171` (来源: live valid_hits):

~~~~
 171| **Rows 1-3:** Incorporates both standard proportion analysis and single marker expression for a cell state marker in the B lymphocyte assay using CPGRPID to group the related record. In accordance with CP guidance for quantitative single marker expression, row 3 contains the marker being measured followed by "Expression". CPMRKSTR uses the recommended format of listing the marker being measured first, followed by the unit in which expression was quantified (median fluorescence intensity, MdFI in the example), and lastly by the complete marker string of the cell population on which expression was measured. The analyte is repeated as part of the target cell population string (CD95+ in the example). GATE and GATEDEF show the gating strategy so it is clear which gate was used to make the quantitative measurement of expression.
~~~~

### T29. `ig34_p0220_a003` — r3:R3_IG34_EQUIV

- PDF 页 220 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 2-7:	The CD99 marker is identified as the target of interest for measuring occupancy. Because the target of interest for which occupancy was measured is not part of the test name (CPTEST), it is identified using CPBDAGNT and/or CPTSTPNL. The CPTSTCND variable defines the condition imposed on the assay at runtime to for measuring background binding. CPGRPID groups individual measured tests to the calculated test value derived from them. Because final results involve comparing specific binding of free or total receptor for the baseline occupancy to a 24-hour post-treatment set of results (rows 8-14), time point information for specimen collection is included in CPTPT and CPTPTNUM. Rows 2-4 show results for measurement of free target using a labeled competitive antibody probe (HA5). Rows 5-7 show results for measurement of total CD99 on the monocyte cell target population using a labeled non-competitive antibody probe (2D4). The total CD99 measurement is a control to monitor for any difference in CD99 expression that might exist between the pre-dose and post-dose specimens that could bias the relative occupancy. They are not used to calculate occupancy of the CD99 target, as the relative expression of CD99 at the post-dose time point is comparable to the pre-dose expression (7253 vs 7530 MESF).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0220.txt` 第 5-11 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  4|                      CPSCAT variables are used to indicate that the assay is intended for target engagement and that the assay is measuring receptor occupancy.
  5| Rows 2-7:            The CD99 marker is identified as the target of interest for measuring occupancy. Because the target of interest for which occupancy was measured is not part of the test name (CPTEST), it is identified
  6|                      using CPBDAGNT and/or CPTSTPNL. The CPTSTCND variable defines the condition imposed on the assay at runtime to for measuring background binding. CPGRPID groups individual measured
  7|                      tests to the calculated test value derived from them. Because final results involve comparing specific binding of free or total receptor for the baseline occupancy to a 24-hour post-treatment set of results
  8|                      (rows 8-14), time point information for specimen collection is included in CPTPT and CPTPTNUM. Rows 2-4 show results for measurement of free target using a labeled competitive antibody probe
  9|                      (HA5) and rows 5-7 show results for measurement of total CD99 on the monocyte cell target population using a labeled non-competitive antibody probe (2D4). The total CD99 measurement is a control
 10|                      to monitor for any difference in CD99 expression that might exist between the pre-dose and post-dose specimens that could bias the relative occupancy. They are not used to calculate occupancy of the
 11|                      CD99 target, as the relative expression of CD99 at the post-dose time point is comparable to the pre-dose expression (7253 vs 7530 MESF).
 12| Rows 8-14: Show the same set of tests collected for baseline (rows 2-7) but measured 24 hours after treatment with the therapeutic drug, which binds in situ to CD99. The reported receptor occupancy is for the 24-
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:305-305` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 305| **Rows 2-7:** The CD99 marker is identified as the target of interest for measuring occupancy. Because the target of interest for which occupancy was measured is not part of the test name (CPTEST), it is identified using CPBDAGNT and/or CPTSTPNL. The CPTSTCND variable defines the condition imposed on the assay at runtime to for measuring background binding. CPGRPID groups individual measured tests to the calculated test value derived from them. Because final results involve comparing specific binding of free or total receptor for the baseline occupancy to a 24-hour post-treatment set of results (rows 8-14), time point information for specimen collection is included in CPTPT and CPTPTNUM. Rows 2-4 show results for measurement of free target using a labeled competitive antibody probe (HA5) and rows 5-7 show results for measurement of total CD99 on the monocyte cell target population using a labeled non-competitive antibody probe (2D4). The total CD99 measurement is a control to monitor for any difference in CD99 expression that might exist between the pre-dose and post-dose specimens that could bias the relative occupancy. They are not used to calculate occupancy of the CD99 target, as the relative expression of CD99 at the post-dose time point is comparable to the pre-dose expression (7253 vs 7530 MESF).
~~~~

### T30. `ig34_p0237_a008` — r3:R3_IG34_EQUIV

- PDF 页 237 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 2:	Shows the number of H1-specific IgG ASCs from the same subject's blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is in ISMSCBCE (i.e. IgG antibody specific to H1 antigen).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0237.txt` 第 14-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13| Row 1:         Shows the total number of IgG ASCs from a subject’s blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is represented by the variable
 14|                ISMSCBCE (i.e. IGG antibody non-specific to any antigen).
 15| Row 2:         Shows the number of H1-specific IgG ASCs from the same subject’s blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is in ISMSCBCE (i.e.
 16|                IgG antibody specific to H1 antigen).
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:136` (来源: live valid_hits):

~~~~
 136| **Row 2:** Shows the number of H1-specific IgG ASCs from the same subject’s blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is in ISMSCBCE (i.e. IgG antibody specific to H1 antigen).
~~~~

### T31. `ig34_p0246_a010` — r3:R3_IG34_EQUIV

- PDF 页 246 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.6 Laboratory Test Results (LB)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 6:   Shows use of LBTMTHSN to represent "HIGH SENSITIVITY" for the high-sensitivity C-reactive protein (hs-CRP) test.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0246.txt` 第 26-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25|                  derived record represented a single point in time. The sponsor chose to populate LBDTC with the first of the 2 specimen collection dates.
 26| Row 6:           Shows use of LBTMTHSN to represent "HIGH SENSITIVITY" for the high-sensitivity C-reactive protein (hs-CRP) test.
 27| Rows 7, 10:      Show use of LBTSTCND. For the cryoglobulin test, 1-day cold incubation is noted; for the platelet aggregation test, collagen induced is noted.
~~~~

KB 现文: `knowledge_base/domains/LB/examples.md:10` (来源: live valid_hits):

~~~~
  10| **Row 6:** Shows use of LBTMTHSN to represent "HIGH SENSITIVITY" for the high-sensitivity C-reactive protein (hs-CRP) test.
~~~~

### T32. `ig34_p0258_a002` — r3:R3_IG34_EQUIV

- PDF 页 258 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-3: Show that all 3 samples (IDVARVAL where IDVAR="BEREFID") were sputum, as indicated by QVAL where QNAM="BESPEC" and QLABEL="Specimen Type".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0258.txt` 第 2-2 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| The SUPPBE dataset is used to represent 2 non-standard variables of BE.
  2| Rows 1-3:       Show that all 3 samples (IDVARVAL where IDVAR="BEREFID") were sputum, as indicated by QVAL where QNAM="BESPEC" and QLABEL="Specimen Type".
  3| Rows 4-6:       Show that all 3 sputum samples were collected via expectoration, as indicated by QVAL where QNAM="Specimen Collection Method". QVAL is populated using the CDISC Controlled Terminology
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:47` (来源: live valid_hits):

~~~~
  47| - Rows 1-3: Show that all 3 samples (IDVARVAL where IDVAR="BEREFID") were sputum, as indicated by QVAL where QNAM="BESPEC" and QLABEL="Specimen Type".
~~~~

### T33. `ig34_p0260_a002` — r3:R3_IG34_EQUIV

- PDF 页 260 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 7-9: Show that 3 of the aliquots (100.3, 100.4, and 100.5) were cultured for detection (row 7) and tested for drug susceptibility (rows 8 and 9). The inoculation and read dates of a culture should be represented in BESTDTC and BEENDTC, respectively. These dates can be linked to the culture results in MB and MS using BELNKID, MBLNKGRP, and MSLNKID.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0260.txt` 第 5-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  4|                 between parent-child samples is defined by the PARENT variable shown in the RELSPEC dataset.
  5| Rows 7-9:       Show that 3 of the aliquots (100.3, 100.4, and 100.5) were cultured for detection (row 7) and tested for drug susceptibility (rows 8 and 9). The
  6|                 inoculation and read dates of a culture should be represented in BESTDTC and BEENDTC, respectively. These dates can be linked to the culture
  7|                 results in MB and MS using BELNKID, MBLNKGRP, and MSLNKID.
  8| Row 10:         Shows that sample 100.1 was concentrated.
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:105` (来源: live valid_hits):

~~~~
 105| - Rows 7-9: Show that 3 of the aliquots (100.3, 100.4, and 100.5) were cultured for detection (row 7) and tested for drug susceptibility (rows 8 and 9). The inoculation and read dates of a culture should be represented in BESTDTC and BEENDTC, respectively. These dates can be linked to the culture results in MB and MS using BELNKID, MBLNKGRP, and MSLNKID.
~~~~

### T34. `ig34_p0261_a015` — r3:R3_IG34_EQUIV

- PDF 页 261 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 2: Shows a categorical result for an AFB test using a stain. MBORRES contains a result based on a CDC AFB quantification scale. The name of the scale used is represented as a supplemental qualifier. MBREFID indicates which aliquot the procedure was performed upon and MBGRPID is used to connect the AFB quantification record to the detection record in row 1.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0261.txt` 第 24-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 23|                MBGRPID can be used to connect the detection record with the corresponding AFB quantification results shown in row 2.
 24| Row 2:         Shows a categorical result for an AFB test using a stain. MBORRES contains a result based on a CDC AFB quantification scale. The name of the
 25|                scale used is represented as a supplemental qualifier. MBREFID indicates which aliquot the procedure was performed upon and MBGRPID is used
 26|                to connect the AFB quantification record to the detection record in row 1.
 27| Row 3:         Shows a test targeting the presence or absence of M. tuberculosis complex using a genotyping method. Details about the assay can be found in the
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:175` (来源: live valid_hits):

~~~~
 175| - Row 2: Shows a categorical result for an AFB test using a stain. MBORRES contains a result based on a CDC AFB quantification scale. The name of the scale used is represented as a supplemental qualifier. MBREFID indicates which aliquot the procedure was performed upon and MBGRPID is used to connect the AFB quantification record to the detection record in row 1.
~~~~

### T35. `ig34_p0261_a016` — r3:R3_IG34_EQUIV

- PDF 页 261 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 3: Shows a test targeting the presence or absence of M. tuberculosis complex using a genotyping method. Details about the assay can be found in the Device Identifiers (DI) domain. The value in SPDEVID links the genotype result to the assay information in the DI domain. The microbial detection certainty is represented as a supplemental qualifier. Because genotyping was used, the detection is considered to be definitive.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0261.txt` 第 27-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26|                to connect the AFB quantification record to the detection record in row 1.
 27| Row 3:         Shows a test targeting the presence or absence of M. tuberculosis complex using a genotyping method. Details about the assay can be found in the
 28|                Device Identifiers (DI) domain. The value in SPDEVID links the genotype result to the assay information in the DI domain. The microbial
 29|                detection certainty is represented as a supplemental qualifier. Because genotyping was used, the detection is considered to be definitive.
 30| Row 4:         Shows a test targeting the presence or absence of M. tuberculosis performed on a solid culture. The medium type and microbial detection certainty
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:177` (来源: live valid_hits):

~~~~
 177| - Row 3: Shows a test targeting the presence or absence of M. tuberculosis complex using a genotyping method. Details about the assay can be found in the Device Identifiers (DI) domain. The value in SPDEVID links the genotype result to the assay information in the DI domain. The microbial detection certainty is represented as a supplemental qualifier. Because genotyping was used, the detection is considered to be definitive.
~~~~

### T36. `ig34_p0270_a006` — r3:R3_IG34_EQUIV

- PDF 页 270 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.1 Pharmacokinetics Concentrations (PC)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 5-6:	Show specimen properties (VOLUME and PH) for the day 1 pre-dose urine specimens. These have a PCCAT value of "SPECIMEN PROPERTY".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0270.txt` 第 9-9 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  8|                      that these specimens were collected at a point in time rather than over an interval.
  9| Rows 5-6:            Show specimen properties (VOLUME and PH) for the day 1 pre-dose urine specimens. These have a PCCAT value of "SPECIMEN PROPERTY".
 10| Rows 7-12:           Show day 1 post-dose drug and metabolite concentrations in plasma.
~~~~

KB 现文: `knowledge_base/domains/PC/examples.md:17` (来源: live valid_hits):

~~~~
  17| **Rows 5-6:** Show specimen properties (VOLUME and PH) for the day 1 pre-dose urine specimens. These have a PCCAT value of "SPECIMEN PROPERTY".
~~~~

### T37. `ig34_p0282_a031` — r3:R3_IG34_EQUIV

- PDF 页 282 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 4`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 5-8:	The relationship with RELID "2" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", and "DY1DRGX_D" and the one PP record with PPGRPID = "CMAX".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0282.txt` 第 37-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36|                  "DY1DRGX_C", and "DY1DRGX_D" and the one PP record with PPGRPID = "TMAX".
 37| Rows 5-8:        The relationship with RELID "2" includes PC records with PCGRPID values "DY1DRGX_A",
 38|                  "DY1DRGX_B", and "DY1DRGX_D" and the one PP record with PPGRPID = "CMAX".
 39| Rows 9-12:       The relationship with RELID "3" includes PC records with PCGRPID values "DY1DRGX_A",
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### T38. `ig34_p0284_a015` — r3:R3_IG34_EQUIV

- PDF 页 284 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
If none of the above applies, or the data become difficult to group, then start with Example 4, and decide which RELREC method would be easiest to implement and represent.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0284.txt` 第 46-47 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 45|             methods B, C, and D as applicable.
 46|       4.    If none of the above applies, or the data become difficult to group, then start with Example 4, and decide
 47|             which RELREC method would be easiest to implement and represent.
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### T39. `ig34_p0345_a002` — r3:R3_IG34_EQUIV

- PDF 页 345 · 原子类型 LIST_ITEM · 所在节 `TU – Description/Overview`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
method used to identify the tumor
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0345.txt` 第 2-2 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1|      •     anatomical location of the tumor
  2|      •     method used to identify the tumor
  3|      •     role of the individual identifying the tumor
~~~~

KB 现文: `knowledge_base/domains/TU/assumptions.md:17` (来源: live valid_hits):

~~~~
  17| - method used to identify the tumor
~~~~

### T40. `ig34_p0356_a025` — r3:R3_IG34_EQUIV

- PDF 页 356 · 原子类型 LIST_ITEM · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 8-19:    Show the measurements of the target tumors and other assessments of the target and non-target tumors at the week 6 visit by the independent assessor, Radiologist 1.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0356.txt` 第 40-40 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39| Rows 1-7:        Show the measurements of the target tumors and other assessments of the target and non-target tumors at the screening visit by the independent assessor, Radiologist 1.
 40| Rows 8-19:       Show the measurements of the target tumors and other assessments of the target and non-target tumors at the week 6 visit by the independent assessor, Radiologist 1.
 41| Rows 20-32: Show the measurements of the target tumors and other assessments of the target and non-target tumors at the week 12 visit by the independent assessor, Radiologist 1.
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:62` (来源: live valid_hits):

~~~~
  62| **Rows 8-19:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the week 6 visit by the independent assessor, Radiologist 1.
~~~~

### T41. `ig34_p0406_a002` — r3:R3_IG34_EQUIV

- PDF 页 406 · 原子类型 LIST_ITEM · 所在节 `§7.2.2.1 Trial Elements Issues – Granularity of Trial Elements`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
c. One element with dosing determined by titration.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0406.txt` 第 2-2 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1|           b.   As a titration element of variable length followed by a constant dosing element of variable length
  2|           c.   One element with dosing determined by titration.
  3|                The choice of elements used to represent this dose titration will depend on the objectives of the trial
~~~~

KB 现文: `knowledge_base/domains/TE/examples.md:61` (来源: live valid_hits):

~~~~
  61|     c. One element with dosing determined by titration.
~~~~

### T42. `ig34_p0406_a032` — r3:R3_IG34_EQUIV

- PDF 页 406 · 原子类型 LIST_ITEM · 所在节 `§7.2.2.1 Trial Elements Issues – Transitions Between Elements`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
for all records that contain a particular element, all the TE variable values are exactly the same; and
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0406.txt` 第 46-46 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 45| Note that
 46|     •     for all records that contain a particular element, all the TE variable values are exactly the same; and
 47|     •     when both TABRANCH and TATRANS are blank, the implicit decision in step 2 is that the subject moves
~~~~

KB 现文: `knowledge_base/domains/TE/examples.md:94` (来源: live valid_hits):

~~~~
  94| - for all records that contain a particular element, all the TE variable values are exactly the same; and
~~~~

### T43. `ig34_p0425_a016` — r3:R3_IG34_EQUIV

- PDF 页 425 · 原子类型 LIST_ITEM · 所在节 `§7.4.2.1 Use of Null Flavor`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Quantity sufficient
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0425.txt` 第 20-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19|              ▪    Not asked
 20|              ▪    Quantity sufficient
 21|              ▪    Trace
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:106` (来源: live valid_hits):

~~~~
 106|         - Quantity sufficient
~~~~

### T44. `ig34_p0426_a001` — r3:R3_IG34_EQUIV

- PDF 页 426 · 原子类型 LIST_ITEM · 所在节 `§7.5 How to Model the Design of a Clinical Trial`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
4. For each arm, identify the major time periods of treatment and non-treatment a subject assigned to that arm will go through. These are the elements, or building blocks, of which the arm is composed.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0426.txt` 第 3-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2|      belong to a single arm.
  3| 4.   For each arm, identify the major time periods of treatment and non-treatment a subject assigned to that
  4|      arm will go through. These are the elements, or building blocks, of which the arm is composed.
  5| 5.   Define the starting point of each element. Define the rule for how long the element should last. Determine
~~~~

KB 现文: `knowledge_base/domains/TI/assumptions.md:45` (来源: live valid_hits):

~~~~
  45| 4. For each arm, identify the major time periods of treatment and non-treatment a subject assigned to that arm will go through. These are the elements, or building blocks, of which the arm is composed.
~~~~

### T45. `ig34_p0425_a002` — r3:R3_IG34_EQUIV

- PDF 页 425 · 原子类型 NOTE · 所在节 `§7.4.2.1 Use of Null Flavor`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
WARNING — Use of this null flavor does provide information that may be a breach of confidentiality, even though no detailed data are provided. Its primary purpose is for those circumstances where it is necessary to inform the receiver that the information does exist without providing any detail.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0425.txt` 第 2-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| NullFlavor Enumeration. OID: 2.16.840.1.113883.5.1008
  2|                               WARNING — Use of this null flavor does provide information that may be a breach of
  3|                            confidentiality, even though no detailed data are provided. Its primary purpose is for those
  4|                            circumstances where it is necessary to inform the receiver that the information does exist
  5|                                                           without providing any detail.
  6| 2 NA      Not applicable   No proper value is applicable in this context (e.g., last menstrual period for a male).
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:90` (来源: live valid_hits):

~~~~
  90| | 2 | MSK | Masked | There is information on this item available, but it has not been provided by the sender due to security, privacy or other reasons. There may be an alternate mechanism for gaining access to this information.<br>**WARNING — Use of this null flavor does provide information that may be a breach of confidentiality, even though no detailed data are provided. Its primary purpose is for those circumstances where it is necessary to inform the receiver that the information does exist without providing any detail.** |
~~~~

### T46. `ig34_p0015_a009` — r3:R3_IG34_EQUIV

- PDF 页 15 · 原子类型 SENTENCE · 所在节 `§2.7 SDTM Variables Not Allowed in the SDTMIG`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The following SDTM variables, defined for use in nonclinical studies (SEND), must NEVER be used in the submission of SDTM-based data for human clinical trials:
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0015.txt` 第 18-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| of clinical trials data or (2) have not yet been evaluated for use in human clinical trials.
 18| The following SDTM variables, defined for use in nonclinical studies (SEND), must NEVER be used in the
 19| submission of SDTM-based data for human clinical trials:
 20|     •   --USCHFL (Interventions, Events, Findings)
~~~~

KB 现文: `knowledge_base/chapters/ch02_fundamentals.md:135` (来源: live valid_hits):

~~~~
 135| The following SDTM variables, defined for use in nonclinical studies (SEND), must NEVER be used in the submission of SDTM-based data for human clinical trials:
~~~~

### T47. `ig34_p0020_a031` — r3:R3_IG34_EQUIV

- PDF 页 20 · 原子类型 SENTENCE · 所在节 `§3.2.1.1 Primary Keys`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Surrogate key assignment is a special case of derived data, one where a portion of the primary key is derived.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0020.txt` 第 41-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 40| key in a new study, but which was not collected in previous studies.
 41| A surrogate key is a single-part, artificially established identifier for a record. Surrogate key assignment is a special
 42| case of derived data, one where a portion of the primary key is derived. A surrogate key is immune to changes in
 43| business needs. In addition, the key depends on only 1 field, so it is compact. A common way of deriving surrogate
~~~~

KB 现文: `knowledge_base/chapters/ch03_submitting_data.md:100` (来源: live valid_hits):

~~~~
 100| A surrogate key is a single-part, artificially established identifier for a record. Surrogate key assignment is a special case of derived data, one where a portion of the primary key is derived. A surrogate key is immune to changes in business needs. In addition, the key depends on only 1 field, so it is compact. A common way of deriving surrogate key values is to assign integer values sequentially. The --SEQ variable in the SDTM datasets is an example of a surrogate key for most datasets; in some instances, however, --SEQ might be a part of a natural key as a replacement for what might have been a key (e.g., a repeat sequence number) in the sponsor's database.
~~~~

### T48. `ig34_p0037_a022` — r3:R3_IG34_EQUIV

- PDF 页 37 · 原子类型 SENTENCE · 所在节 `§4.3.5 Storing Controlled Terminology for Synonym Qualifier Variables`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
A pair of variables has been defined for each of the levels of the hierarchy other than SOC and Preferred Term (PT): one to represent the text description and the other to represent the code value associated with it.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0037.txt` 第 29-31 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28|     •    If MedDRA is used to code events, the intermediate levels in the MedDRA hierarchy should also be
 29|          represented in the dataset. A pair of variables has been defined for each of the levels of the hierarchy other
 30|          than SOC and Preferred Term (PT): one to represent the text description and the other to represent the code
 31|          value associated with it. For example, --LLT should be used to represent the Lowest Level Term text
 32|          description and --LLTCD should be used to represent the Lowest Level Term code value.
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:683` (来源: live valid_hits):

~~~~
 683| - If MedDRA is used to code events, the intermediate levels in the MedDRA hierarchy should also be represented in the dataset. A pair of variables has been defined for each of the levels of the hierarchy other than SOC and Preferred Term (PT): one to represent the text description and the other to represent the code value associated with it. For example, --LLT should be used to represent the Lowest Level Term text description and --LLTCD should be used to represent the Lowest Level Term code value.
~~~~

### T49. `ig34_p0039_a019` — r3:R3_IG34_EQUIV

- PDF 页 39 · 原子类型 SENTENCE · 所在节 `§4.4.1 Formats for Date/Time Variables`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The SDTM fragment employed for date/time character variables is DTC.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0039.txt` 第 21-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 20|          26T00:00:01).
 21| Implementation of the ISO 8601 standard means that date/time variables are character/text data types. The SDTM
 22| fragment employed for date/time character variables is DTC.
 23| 
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:758-758` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 758| Implementation of the ISO 8601 standard means that date/time variables are character/text data types. The SDTM fragment employed for date/time character variables is **DTC**.
~~~~

### T50. `ig34_p0046_a009` — r3:R3_IG34_EQUIV

- PDF 页 46 · 原子类型 SENTENCE · 所在节 `§4.4.10 [Representing Time Points]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Time points can be represented using the time point variables --TPT, --TPTNUM, --ELTM, and the time-point anchors --TPTREF (text description) and --RFTDTC (the date/time).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0046.txt` 第 14-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13| 4.4.10       Representing Time Points
 14| Time points can be represented using the time point variables --TPT, --TPTNUM, --ELTM, and the time-point
 15| anchors --TPTREF (text description) and --RFTDTC (the date/time). Note that time-point data will usually have an
 16| associated --DTC value. The interrelationship of these variables is shown in the following figure.
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1072` (来源: live valid_hits):

~~~~
1072| Time points can be represented using the time point variables --TPT, --TPTNUM, --ELTM, and the time-point anchors --TPTREF (text description) and --RFTDTC (the date/time). Note that time-point data will usually have an associated --DTC value. The interrelationship of these variables is shown in the following figure.
~~~~

