# SDTMIG v3.4 --- Domain Models: Findings — Part 5

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 5/8 — 6.3.5.8-6.3.5.9: Specimen-based (MI, PK)
> **Original:** `SDTMIG34_06_DomainModels_Findings.md`
> **Related:** `SDTMIG34_06a_DomainModels_Findings.md`, `SDTMIG34_06b_DomainModels_Findings.md`, `SDTMIG34_06c_DomainModels_Findings.md`, `SDTMIG34_06d_DomainModels_Findings.md`, `SDTMIG34_06f_DomainModels_Findings.md`, `SDTMIG34_06g_DomainModels_Findings.md`, `SDTMIG34_06h_DomainModels_Findings.md`

---

#### 6.3.5.8 Microscopic Findings (MI)

##### MI – Description/Overview
A findings domain that contains histopathology findings and microscopic evaluations.
The MI dataset provides a record for each microscopic finding observed. There may be multiple microscopic tests on a subject or specimen.


##### MI – Specification
mi.xpt, Microscopic Findings — Findings. One record per finding per specimen per subject, Tabulation.

**Structure:** One record per finding per specimen per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | MI |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | MISEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | MIGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | MIREFID | Reference ID | Char | Identifier | Perm |  |
| 7 | MISPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | MITESTCD | Microscopic Examination Short Name | Char | Topic | Req | C132263 |
| 9 | MITEST | Microscopic Examination Name | Char | Synonym Qualifier | Req | C132262 |
| 10 | MITSTDTL | Microscopic Examination Detail | Char | Record Qualifier | Perm | C125922 |
| 11 | MICAT | Category for Microscopic Finding | Char | Grouping Qualifier | Perm |  |
| 12 | MISCAT | Subcategory for Microscopic Finding | Char | Grouping Qualifier | Perm |  |
| 13 | MIORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 14 | MIORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 15 | MISTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 16 | MISTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 17 | MISTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 18 | MIRESCAT | Result Category | Char | Variable Qualifier | Perm |  |
| 19 | MISTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 20 | MIREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 21 | MINAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |
| 22 | MISPEC | Specimen Material Type | Char | Record Qualifier | Req | C78734 |
| 23 | MISPCCND | Specimen Condition | Char | Record Qualifier | Exp | C78733 |
| 24 | MILOC | Specimen Collection Location | Char | Record Qualifier | Perm | C74456 |
| 25 | MILAT | Specimen Laterality within Subject | Char | Variable Qualifier | Perm | C99073 |
| 26 | MIDIR | Specimen Directionality within Subject | Char | Variable Qualifier | Perm | C99074 |
| 27 | MIMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 28 | MILOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| 29 | MIBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 30 | MIEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| 31 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 32 | VISIT | Visit Name | Char | Timing | Perm |  |
| 33 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 36 | MIDTC | Date/Time of Specimen Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 37 | MIDY | Study Day of Specimen Collection | Num | Timing | Perm |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **MISEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **MIGRPID**: Used to tie together a block of related records in a single domain for a subject. This is not the treatment group number.
- **MIREFID**: Internal or external specimen identifier. Example: specimen barcode number.
- **MISPID**: Sponsor-defined reference number. May be printed on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: line number from the MI Findings page.
- **MITESTCD**: Short name of the measurement, test, or examination described in MITEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MITESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MITESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "HER2", "BRCA1", "TTF1".
- **MITEST**: Verbatim name of the test or examination used to obtain the measurement or finding. The value in MITEST cannot be longer than 40 characters. Examples: "Human Epidermal Growth Factor Receptor 2", "Breast Cancer Susceptibility Gene 1", "Thyroid Transcription Factor 1".
- **MITSTDTL**: Further description of the test performed in producing the MI result. This would be used to represent specific attributes, such as intensity score or percentage of cells displaying presence of the biomarker or compound.
- **MICAT**: Used to define a category of related records.
- **MISCAT**: Used to define a further categorization of MICAT.
- **MIORRES**: Result of the histopathology measurement or finding as originally received or collected.
- **MIORRESU**: Original unit for MIORRES.
- **MISTRESC**: Contains the result value for all findings, copied or derived from MIORRES in a standard format or standard units. MISTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MISTRESN.
- **MISTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from MISTRESC. MISTRESN should store all numeric test results or findings.
- **MISTRESU**: Standardized unit used for MISTRESC and MISTRESN.
- **MIRESCAT**: Used to categorize the result of a finding. Examples: "MALIGNANT" or "BENIGN" for tumor findings.
- **MISTAT**: Used to indicate examination not done or result is missing. Should be null if a result exists in MIORRES or have a value of "NOT DONE" when MIORRES = "NULL".
- **MIREASND**: Reason not done. Used in conjunction with MISTAT when value is NOT DONE. Examples: "SAMPLE AUTOLYZED", "SPECIMEN LOST".
- **MINAM**: Name or identifier of the vendor (e.g., laboratory) that provided the test results.
- **MISPEC**: Subject of the observation. Defines the type of specimen used for a measurement. Examples: "TISSUE", "BLOOD", "BONE MARROW".
- **MISPCCND**: Free or standardized text describing the condition of the specimen. Example: "AUTOLYZED".
- **MILOC**: Location relevant to the collection of the specimen. Examples: "LUNG", "KNEE JOINT", "ARM", "THIGH".
- **MILAT**: Qualifier for laterality of the location of the specimen in MILOC. Examples: "LEFT", "RIGHT", "BILATERAL".
- **MIDIR**: Qualifier for directionality of the location of the specimen in MILOC. Examples: "DORSAL", "PROXIMAL".
- **MIMETHOD**: Method of the test or examination. This could include the technique or type of staining used for the slides. Examples: "IHC", "Crystal violet", "Safranin", "Trypan blue", or "Propidium iodide".
- **MILOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **MIBLFL**: Indicator used to identify a baseline value. The value should be "Y" or null. Note that MIBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.
- **MIEVAL**: Role of the person who provided the evaluation. Example: "PATHOLOGIST", "PEER REVIEW", "SPONSOR PATHOLOGIST".
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the date/time at which the specimen was collected.
- **MIDTC**: Date/time of specimen collection, in ISO 8601 format.
- **MIDY**: Study day of specimen collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.


##### MI – Assumptions
1. This domain holds findings resulting from the microscopic examination of tissue samples. These examinations are performed on a specimen, usually one that has been prepared with some type of stain. Some examinations of cells in fluid specimens (e.g., blood, urine) are classified as lab tests and should be stored in the Laboratory Test Results (LB) domain. Biomarkers assessed by histologic or histopathological examination (by employing cytochemical/immunocytochemical stains) are stored in the MI domain.
2. When biomarker results are represented in MI, MITESTCD reflects the biomarker of interest (e.g., "BRCA1", "HER2", "TTF1"), and MITSTDTL further qualifies the record. MITSTDTL is used to represent details descriptive of staining results (e.g., "H SCORE TOTAL SCORE", "STAINING INTENSITY", "PERCENT POSITIVE CELL").
3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the MI domain, but the following qualifiers would generally not be used: --POS, --MODIFY, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --LEAD, --CSTATE, --BLFL, -- FAST, --DRVFL, --LLOQ, --ULOQ.


##### MI – Examples

**Example 1**
Immunohistochemistry (IHC) is a method that involves treating tissue with a stain that adheres to very specific substances. IHC is the method most commonly used to assess the amount of HER2 receptor protein on the surface of the cancer cells. A cell with too many receptors receives too many growth signals. In this study, IHC assessment of HER2 in samples of breast cancer tissue yielded staining intensity on a scale of 0 to 3+. Staining intensity values of 0 to 1+ were categorized as negative; values of 2+ and 3+ were categorized as positive.
**Row 1:** Shows a subject with a receptor protein stain intensity value of "0", categorized in MIRESCAT as "NEGATIVE".
**Row 2:** Shows a subject with a receptor protein stain intensity value of "2+", categorized in MIRESCAT as "POSITIVE".
*mi.xpt*

| Row | STUDYID | DOMAIN | USUBJID | MISEQ | MITESTCD | MITEST | MITSTDTL | MIORRES | MISTRESC | MIRESCAT | MISPEC | MILOC | MIMETHOD | VISIT | MIDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MI | ABC-1001 | 1 | HER2 | Human Epidermal Growth Factor Receptor 2 | STAINING INTENSITY | 0 | 0 | NEGATIVE | TISSUE | BREAST | IHC | SCREENING | 2001-06-15 |
| 2 | ABC | MI | ABC-2002 | 1 | HER2 | Human Epidermal Growth Factor Receptor 2 | STAINING INTENSITY | 2+ | 2+ | POSITIVE | TISSUE | BREAST | IHC | SCREENING | 2001-06-15 |

**Example 2**
In this study, IHC for estrogen receptor protein expression in a tissue was reported using the Allred scoring system. The proportion positive score was assessed as the percentage of tumor cells that stained positive on a scale from 0 to 5. Staining intensity was assessed as none, weak, intermediate, or strong, and scored from 0 to 3, respectively. The total score is the sum of the proportion positive and stain intensity scores.
**Row 1:** Shows the Allred proportion positive score.
**Row 2:** Shows the staining intensity, which was assessed as "Strong". The score associated with an intensity of "STRONG" is in MISTRESC and MISTRESN.
**Row 3:** The total score is a represented in a derived record, so MIORRES is null.
*mi.xpt*

| Row | STUDYID | DOMAIN | USUBJID | MISEQ | MIGRPID | MITESTCD | MITEST | MITSTDTL | MIORRES | MISTRESC | MISTRESN | MISPEC | MILOC | MIMETHOD | MIDRVFL | VISIT | MIDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MI | ABC-1001 | 1 | 1 | ESTRCPT | Estrogen Receptor | ALLRED PROPORTION POSITIVE SCORE | 3 | 3 | 3 | TISSUE | BREAST | IHC |  | SCREENING | 2001-06-15 |
| 2 | ABC | MI | ABC-1001 | 2 | 1 | ESTRCPT | Estrogen Receptor | ALLRED STAINING INTENSITY SCORE | STRONG | 3 | 3 | TISSUE | BREAST | IHC |  | SCREENING | 2001-06-15 |
| 3 | ABC | MI | ABC-1001 | 3 | 1 | ESTRCPT | Estrogen Receptor | ALLRED TOTAL SCORE |  | 6 | 6 | TISSUE | BREAST | IHC | Y | SCREENING | 2001-06-15 |

These IHC staining results were all for the cell nucleus, represented using a supplemental qualifier for subcellular location.
*suppmi.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MI | ABC-1001 | MIGRPID | 1 | MISCELOC | Subcellular Location | NUCLEUS | CRF |  |

**Example 3**
In this study, IHC staining for NK2 homeobox 1 (NKX2-1; also known as thyroid transcription factor 1) was reported at a detailed level. Staining intensity of individual cells was assessed on a semi-quantitative scale ranging from 0 to 3+, and the percentage of tumor cells at each staining intensity level was reported. These results were used to calculate the H-score, which ranges from 0 to 300.
**Rows 1-4:** Show the percentage of cells at each H-Score staining intensity.
**Row 5:** Shows the H-score derived from the percentages. This is a derived record, so MIORRES is blank.
*mi.xpt*

| Row | STUDYID | DOMAIN | USUBJID | MISEQ | MIGRPID | MITESTCD | MITEST | MITSTDTL | MIORRES | MIORRESU | MISTRESC | MISTRESN | MISTRESU | MISPEC | MILOC | MIMETHOD | MIDRVFL | VISIT | MIDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MI | ABC-1001 | 1 | 1 | NKX2_1 | NK2 Homeobox 1 | H SCORE STAINING INTENSITY 0 | 25 | % | 25 | 25 | % | TISSUE | LUNG | IHC |  | SCREENING | 2001-06-15 |
| 2 | ABC | MI | ABC-1001 | 2 | 1 | NKX2_1 | NK2 Homeobox 1 | H SCORE STAINING INTENSITY 1+ | 40 | % | 40 | 40 | % | TISSUE | LUNG | IHC |  | SCREENING | 2001-06-15 |
| 3 | ABC | MI | ABC-1001 | 3 | 1 | NKX2_1 | NK2 Homeobox 1 | H SCORE STAINING INTENSITY 2+ | 35 | % | 35 | 35 | % | TISSUE | LUNG | IHC |  | SCREENING | 2001-06-15 |
| 4 | ABC | MI | ABC-1001 | 4 | 1 | NKX2_1 | NK2 Homeobox 1 | H SCORE STAINING INTENSITY 3+ | 0 | % | 0 | 0 | % | TISSUE | LUNG | IHC |  | SCREENING | 2001-06-15 |
| 5 | ABC | MI | ABC-1001 | 5 | 1 | NKX2_1 | NK2 Homeobox 1 | H SCORE TOTAL SCORE |  |  | 110 | 110 |  | TISSUE | LUNG | IHC | Y | SCREENING | 2001-06-15 |

These IHC staining results were all for the cell cytoplasm, represented using a supplemental qualifier for subcellular location.
*suppmi.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MI | ABC-1001 | MIGRPID | 1 | MISCELOC | Subcellular Location | CYTOPLASM | CRF |  |

#### 6.3.5.9 Pharmacokinetics Domains

The pharmacokinetics domains include Pharmacokinetics Concentrations (PC) and Pharmacokinetics Parameters (PP). The PC domain is used for concentrations of drugs or metabolites in fluids or tissues as a function of time. PP is used for pharmacokinetic parameters derived from concentration-time data.

##### 6.3.5.9.1 Pharmacokinetics Concentrations (PC)

###### PC – Description/Overview
A findings domain that contains concentrations of drugs or metabolites in fluids or tissues as a function of time.

###### PC – Specification
pc.xpt, Pharmacokinetics Concentrations — Findings. One record per sample characteristic or time-point concentration per reference time point or per analyte per subject, Tabulation.

**Structure:** One record per sample characteristic or time-point concentration per reference time point or per analyte per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | PC |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | PCSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | PCGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | PCREFID | Reference ID | Char | Identifier | Perm |  |
| 7 | PCSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | PCTESTCD | Pharmacokinetic Test Short Name | Char | Topic | Req |  |
| 9 | PCTEST | Pharmacokinetic Test Name | Char | Synonym Qualifier | Req |  |
| 10 | PCCAT | Test Category | Char | Grouping Qualifier | Perm |  |
| 11 | PCSCAT | Test Subcategory | Char | Grouping Qualifier | Perm |  |
| 12 | PCORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 13 | PCORRESU | Original Units | Char | Variable Qualifier | Exp | C85494 |
| 14 | PCSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 15 | PCSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |
| 16 | PCSTRESU | Standard Units | Char | Variable Qualifier | Exp | C85494 |
| 17 | PCSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 18 | PCREASND | Reason Test Not Done | Char | Record Qualifier | Perm |  |
| 19 | PCNAM | Vendor Name | Char | Record Qualifier | Exp |  |
| 20 | PCSPEC | Specimen Material Type | Char | Record Qualifier | Exp | C78734 |
| 21 | PCSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| 22 | PCMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 23 | PCFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |
| 24 | PCDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 25 | PCLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Exp |  |
| 26 | PCULOQ | Upper Limit of Quantitation | Num | Variable Qualifier | Perm |  |
| 27 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 28 | VISIT | Visit Name | Char | Timing | Perm |  |
| 29 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 30 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 31 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 32 | PCDTC | Date/Time of Specimen Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 33 | PCENDTC | End Date/Time of Specimen Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| 34 | PCDY | Actual Study Day of Specimen Collection | Num | Timing | Perm |  |
| 35 | PCENDY | Study Day of End of Observation | Num | Timing | Perm |  |
| 36 | PCTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 37 | PCTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 38 | PCELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 39 | PCTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 40 | PCRFTDTC | Date/Time of Reference Point | Char | Timing | Perm | ISO 8601 datetime or interval |
| 41 | PCEVLINT | Evaluation Interval | Char | Timing | Perm | ISO 8601 duration or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **PCSEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **PCGRPID**: Used to tie together a block of related records in a single domain to support relationships within the domain and between domains.
- **PCREFID**: Internal or external specimen identifier.
- **PCSPID**: Sponsor-defined reference number.
- **PCTESTCD**: Short name of the analyte or specimen characteristic. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PCTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PCTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "ASA", "VOL", "SPG".
- **PCTEST**: Name of the analyte or specimen characteristic. Note any test normally performed by a clinical laboratory is considered a lab test. The value in PCTEST cannot be longer than 40 characters. Examples: "Acetylsalicylic Acid", "Volume", "Specific Gravity".
- **PCCAT**: Used to define a category of related records. Examples: "ANALYTE", "SPECIMEN PROPERTY".
- **PCSCAT**: A further categorization of a test category.
- **PCORRES**: Result of the measurement or finding as originally received or collected.
- **PCORRESU**: Original units in which the data were collected. The unit for PCORRES. Example: "mg/L".
- **PCSTRESC**: Contains the result value for all findings, copied or derived from PCORRES in a standard format or standard units. PCSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in PCSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in PCORRES, and these results effectively have the same meaning, they could be represented in standard format in PCSTRESC as "NEGATIVE". For other examples, see general assumptions.
- **PCSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from PCSTRESC. PCSTRESN should store all numeric test results or findings.
- **PCSTRESU**: Standardized unit used for PCSTRESC and PCSTRESN.
- **PCSTAT**: Used to indicate a result was not obtained. Should be null if a result exists in PCORRES.
- **PCREASND**: Describes why a result was not obtained, such as "SPECIMEN LOST". Used in conjunction with PCSTAT when value is "NOT DONE".
- **PCNAM**: Name or identifier of the laboratory or vendor who provides the test results.
- **PCSPEC**: Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE".
- **PCSPCCND**: Free or standardized text describing the condition of the specimen. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC".
- **PCMETHOD**: Method of the test or examination. Examples: "HPLC/MS", "ELISA". This should contain sufficient information and granularity to allow differentiation of various methods that might have been used within a study.
- **PCFAST**: Indicator used to identify fasting status.
- **PCDRVFL**: Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, which do not come from the CRF, are examples of records that would be derived for the submission datasets. If PCDRVFL = "Y", then PCORRES may be null with PCSTRESC, and PCSTRESN (if the result is numeric) having the derived value.
- **PCLLOQ**: Indicates the lower limit of quantitation for an assay. Units should be those used in PCSTRESU.
- **PCULOQ**: Indicates the upper limit of quantitation for an assay. Units should be those used in PCSTRESU.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm.
- **EPOCH**: Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.
- **PCDTC**: Date/time of specimen collection represented in ISO 8601 character format. If there is no end time, then this will be the collection time.
- **PCENDTC**: End date/time of specimen collection represented in ISO 8601 character format. If there is no end time, the collection time should be stored in PCDTC, and PCENDTC should be null.
- **PCDY**: Study day of specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
- **PCENDY**: Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.
- **PCTPT**: Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See PCTPTNUM and PCTPTREF. Examples: "Start", "5 min post".
- **PCTPTNUM**: Numerical version of PCTPT to aid in sorting.
- **PCELTM**: Planned elapsed time (in ISO 8601) relative to a planned fixed reference (PCTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date time variable.
- **PCTPTREF**: Name of the fixed reference point used as a basis for PCTPT, PCTPTNUM, and PCELTM. Example: "MOST RECENT DOSE".
- **PCRFTDTC**: Date/time of the reference time point described by PCTPTREF.
- **PCEVLINT**: Evaluation Interval associated with a PCTEST record represented in ISO 8601 character format. Example: "-PT2H" to represent an evaluation interval of 2 hours prior to a PCTPT.


###### PC – Assumptions
1. This domain can be used to represent specimen properties (e.g., volume, pH) in addition to drug and metabolite concentration measurements.
2. CDISC Controlled Terminology Rules for Pharmacokinetics are available at https://www.cdisc.org/standards/terminology/controlled-terminology.
3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the PC domain, but the following Qualifiers would not generally be used: --BODSYS, --SEV.

###### PC – Examples
Due to space limitations, not all expected or permissible findings variables are included in the example for this domain.


**Example 1**
This example shows concentration data for drug A and a metabolite of drug A from plasma and from urine samples collected pre-dose and after dosing on study days 1 and 11.
PCTPTREF is a text value of the description of a “zero” time (e.g., time of dosing). It should be meaningful. If there are multiple PK profiles being generated, the zero time for each will be different (e.g., a different dose such as first dose, second dose) and, as a result, values for PCTPTREF must be different. In this example, such values for PCTPTREF are required to make values of PCTPTNUM and PCTPT unique (see Section 4.4.10, Representing Time Points).
**Rows 1-2:** Show day 1 pre-dose drug and metabolite concentrations in plasma and urine.
**Rows 3-4:** Show day 1 pre-dose drug and metabolite concentrations in urine. Urine specimens may be collected over an interval; both PCDTC and PCENDTC have been populated with the same value to indicate that these specimens were collected at a point in time rather than over an interval.
**Rows 5-6:** Show specimen properties (VOLUME and PH) for the day 1 pre-dose urine specimens. These have a PCCAT value of "SPECIMEN PROPERTY".
**Rows 7-12:** Show day 1 post-dose drug and metabolite concentrations in plasma.
**Rows 13-16:** Show day 11 drug and metabolite concentrations in plasma.
**Rows 17-20:** Show day 11 drug and metabolite concentrations in urine specimens collected over an interval. The elapsed times for urine samples are calculated as the elapsed time (from the reference time point,
PCTPTREF) to the end of the specimen collection interval. Elapsed time values that are the same for urine and plasma samples have been assigned the same value for PCTPT. For the urine samples, the value in PCEVLINT describes the planned evaluation (or collection) interval relative to the time point. The actual evaluation interval can be determined by subtracting PCDTC from PCENDTC.
**Rows 21-30:** Show additional drug and metabolite concentrations and specimen properties related to the day 11 dose.
**Rows 31-32:** Show day 12 (24H post day 11 dose) drug and metabolite concentrations in plasma.
*pc.xpt*

| Row | STUDYID | DOMAIN | USUBJID | PCSEQ | PCGRPID | PCREFID | PCTESTCD | PCTEST | PCCAT | PCSPEC | PCORRES | PCORRESU | PCSTRESC | PCSTRESN | PCSTRESU | PCSTAT | PCLLOQ | PCULOQ | VISITNUM | VISIT | VISITDY | PCDTC | PCENDTC | PCDY | PCTPT | PCTPTNUM | PCTPTREF | PCRFTDTC | PCELTM | PCEVLINT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | 123-0001 | 1 | Day 1 | A554134-10 | DRGA_MET | Drug A Metabolite | ANALYTE | PLASMA | <0.1 | ng/mL | <0.1 |  | ng/mL |  | 0.10 | 20 | 1 | DAY 1 | 1 | 2001-02-01T07:45 |  | 1 | PREDOSE | 0 | Day 1 Dose | 2001-02-01T08:00 | -PT15M |  |
| 2 | ABC-123 | PC | 123-0001 | 2 | Day 1 | A554134-10 | DRGA_PAR | Drug A Parent | ANALYTE | PLASMA | <0.1 | ng/mL | <0.1 |  | ng/mL |  | 0.10 | 20 | 1 | DAY 1 | 1 | 2001-02-01T07:45 |  | 1 | PREDOSE | 0 | Day 1 Dose | 2001-02-01T08:00 | -PT15M |  |
| 3 | ABC-123 | PC | 123-0001 | 3 | Day 1 | A554134-11 | DRGA_MET | Drug A Metabolite | ANALYTE | URINE | <2 | ng/mL | <2 |  | ng/mL |  | 2.00 | 500 | 1 | DAY 1 | 1 | 2001-02-01T07:45 | 2001-02-01T07:45 | 1 | PREDOSE | 0 | Day 1 Dose | 2001-02-01T08:00 | -PT15M |  |
| 4 | ABC-123 | PC | 123-0001 | 4 | Day 1 | A554134-11 | DRGA_PAR | Drug A Parent | ANALYTE | URINE | <2 | ng/mL | <2 |  | ng/mL |  | 2.00 | 500 | 1 | DAY 1 | 1 | 2001-02-01T07:45 | 2001-02-01T07:45 | 1 | PREDOSE | 0 | Day 1 Dose | 2001-02-01T08:00 | -PT15M |  |
| 5 | ABC-123 | PC | 123-0001 | 5 | Day 1 | A554134-11 | VOLUME | Volume | SPECIMEN PROPERTY | URINE | 3500 | mL | 100 | 100 | mL |  |  |  | 1 | DAY 1 | 1 | 2001-02-01T07:45 | 2001-02-01T07:45 | 1 | PREDOSE | 0 | Day 1 Dose | 2001-02-01T08:00 | -PT15M |  |
| 6 | ABC-123 | PC | 123-0001 | 6 | Day 1 | A554134-11 | PH | PH | SPECIMEN PROPERTY | URINE | 5.5 |  | 5.5 | 5.5 |  |  |  |  | 1 | DAY 1 | 1 | 2001-02-01T07:45 | 2001-02-01T07:45 | 1 | PREDOSE | 0 | Day 1 Dose | 2001-02-01T08:00 | -PT15M |  |
| 7 | ABC-123 | PC | 123-0001 | 7 | Day 1 | A554134-12 | DRGA_MET | Drug A Metabolite | ANALYTE | PLASMA | 5.4 | ng/mL | 5.4 | 5.4 | ng/mL |  | 0.10 | 20 | 1 | DAY 1 | 1 | 2001-02-01T09:30 |  | 1 | 1H30MIN | 1.5 | Day 1 Dose | 2001-02-01T08:00 | PT1H30M |  |
| 8 | ABC-123 | PC | 123-0001 | 8 | Day 1 | A554134-12 | DRGA_PAR | Drug A Parent | ANALYTE | PLASMA | 4.74 | ng/mL | 4.74 | 4.74 | ng/mL |  | 0.10 | 20 | 1 | DAY 1 | 1 | 2001-02-01T09:30 |  | 1 | 1H30MIN | 1.5 | Day 1 Dose | 2001-02-01T08:00 | PT1H30M |  |
| 9 | ABC-123 | PC | 123-0001 | 9 | Day 1 | A554134-13 | DRGA_MET | Drug A Metabolite | ANALYTE | PLASMA | 5.44 | ng/mL | 5.44 | 5.44 | ng/mL |  | 0.10 | 20 | 1 | DAY 1 | 1 | 2001-02-01T14:00 |  | 1 | 6H | 6 | Day 1 Dose | 2001-02-01T08:00 | PT6H00M |  |
| 10 | ABC-123 | PC | 123-0001 | 10 | Day 1 | A554134-13 | DRGA_PAR | Drug A Parent | ANALYTE | PLASMA | 1.09 | ng/mL | 1.09 | 1.09 | ng/mL |  | 0.10 | 20 | 1 | DAY 1 | 1 | 2001-02-01T14:00 |  | 1 | 6H | 6 | Day 1 Dose | 2001-02-01T08:00 | PT6H |  |
| 11 | ABC-123 | PC | 123-0001 | 11 | Day 1 | A554134-14 | DRGA_MET | Drug A Metabolite | ANALYTE | PLASMA |  |  |  |  |  | NOT DONE |  | 20 | 2 | DAY 2 | 2 | 2001-02-02T08:00 |  | 2 | 24H | 24 | Day 1 Dose | 2001-02-01T08:00 | PT24H |  |
| 12 | ABC-123 | PC | 123-0001 | 12 | Day 1 | A554134-14 | DRGA_PAR | Drug A Parent | ANALYTE | PLASMA | <0.1 | ng/mL | <0.1 |  | ng/mL |  | 0.10 | 20 | 2 | DAY 2 | 2 | 2001-02-02T08:00 |  | 2 | 24H | 24 | Day 1 Dose | 2001-02-01T08:00 | PT24H |  |
| 13 | ABC-123 | PC | 123-0001 | 13 | Day 11 | A554134-15 | DRGA_MET | Drug A Metabolite | ANALYTE | PLASMA | 3.41 | ng/mL | 3.41 | 3.41 | ng/mL |  | 0.10 | 20 | 3 | DAY 11 | 11 | 2001-02-11T07:45 |  | 11 | PREDOSE | 0 | Day 11 Dose | 2001-02-11T08:00 | -PT15M |  |
| 14 | ABC-123 | PC | 123-0001 | 14 | Day 11 | A554134-15 | DRGA_PAR | Drug A Parent | ANALYTE | PLASMA | <0.1 | ng/mL | <0.1 |  | ng/mL |  | 0.10 | 20 | 3 | DAY 11 | 11 | 2001-02-11T07:45 |  | 11 | PREDOSE | 0 | Day 11 Dose | 2001-02-11T08:00 | -PT15M |  |
| 15 | ABC-123 | PC | 123-0001 | 15 | Day 11 | A554134-16 | DRGA_MET | Drug A Metabolite | ANALYTE | PLASMA | 8.74 | ng/mL | 8.74 | 8.74 | ng/mL |  | 0.10 | 20 | 3 | DAY 11 | 11 | 2001-02-11T09:30 |  | 11 | 1H30MIN | 1.5 | Day 11 Dose | 2001-02-11T08:00 | PT1H30M |  |
| 16 | ABC-123 | PC | 123-0001 | 16 | Day 11 | A554134-16 | DRGA_PAR | Drug A Parent | ANALYTE | PLASMA | 4.2 | ng/mL | 4.2 | 4.2 | ng/mL |  | 0.10 | 20 | 3 | DAY 11 | 11 | 2001-02-11T09:30 |  | 11 | 1H30MIN | 1.5 | Day 11 Dose | 2001-02-11T08:00 | PT1H30M |  |
| 17 | ABC-123 | PC | 123-0001 | 17 | Day 11 | A554134-17 | DRGA_MET | Drug A Metabolite | ANALYTE | URINE | 245 | ng/mL | 245 | 245 | ng/mL |  | 2.00 | 500 | 3 | DAY 11 | 11 | 2001-02-11T08:00 | 2001-02-11T14:03 | 11 | 6H | 6 | Day 11 Dose | 2001-02-11T08:00 | PT6H | -PT6H |
| 18 | ABC-123 | PC | 123-0001 | 18 | Day 11 | A554134-17 | DRGA_PAR | Drug A Parent | ANALYTE | URINE | 13.1 | ng/mL | 13.1 | 13.1 | ng/mL |  | 2.00 | 500 | 3 | DAY 11 | 11 | 2001-02-11T08:00 | 2001-02-11T14:03 | 11 | 6H | 6 | Day 11 Dose | 2001-02-11T08:00 | PT6H | -PT6H |
| 19 | ABC-123 | PC | 123-0001 | 19 | Day 11 | A554134-17 | VOLUME | Volume | SPECIMEN PROPERTY | URINE | 574 | mL | 574 | 574 | mL |  |  |  | 3 | DAY 11 | 11 | 2001-02-11T08:00 | 2001-02-11T14:03 | 11 | 6H | 6 | Day 11 Dose | 2001-02-11T08:00 | PT6H | -PT6H |
| 20 | ABC-123 | PC | 123-0001 | 20 | Day 11 | A554134-17 | PH | PH | SPECIMEN PROPERTY | URINE | 5.5 |  | 5.5 | 5.5 |  |  |  |  | 3 | DAY 11 | 11 | 2001-02-11T08:00 | 2001-02-11T14:03 | 11 | 6H | 6 | Day 11 Dose | 2001-02-11T08:00 | PT6H | -PT6H |
| 21 | ABC-123 | PC | 123-0001 | 21 | Day 11 | A554134-18 | DRGA_MET | Drug A Metabolite | ANALYTE | PLASMA | 9.02 | ng/mL | 9.02 | 9.02 | ng/mL |  | 0.10 | 20 | 3 | DAY 11 | 11 | 2001-02-11T14:00 |  | 11 | 6H | 6 | Day 11 Dose | 2001-02-11T08:00 | PT6H |  |
| 22 | ABC-123 | PC | 123-0001 | 22 | Day 11 | A554134-18 | DRGA_PAR | Drug A Parent | ANALYTE | PLASMA | 1.18 | ng/mL | 1.18 | 1.18 | ng/mL |  | 0.10 | 20 | 3 | DAY 11 | 11 | 2001-02-11T14:00 |  | 11 | 6H | 6 | Day 11 Dose | 2001-02-11T08:00 | PT6H |  |
| 23 | ABC-123 | PC | 123-0001 | 23 | Day 11 | A554134-19 | DRGA_MET | Drug A Metabolite | ANALYTE | URINE | 293 | ng/mL | 293 | 293 | ng/mL |  | 2.00 |  | 3 | DAY 11 | 11 | 2001-02-11T14:03 | 2001-02-11T20:10 | 11 | 12H | 12 | Day 11 Dose | 2001-02-11T08:00 | PT12H | -PT6H |
| 24 | ABC-123 | PC | 123-0001 | 24 | Day 11 | A554134-19 | DRGA_PAR | Drug A Parent | ANALYTE | URINE | 7.1 | ng/mL | 7.1 | 7.1 | ng/mL |  | 2.00 |  | 3 | DAY 11 | 11 | 2001-02-11T14:03 | 2001-02-11T20:10 | 11 | 12H | 12 | Day 11 Dose | 2001-02-11T08:00 | PT12H | -PT6H |
| 25 | ABC-123 | PC | 123-0001 | 25 | Day 11 | A554134-19 | VOLUME | Volume | SPECIMEN PROPERTY | URINE | 363 | mL | 363 | 363 | mL |  |  |  | 3 | DAY 11 | 11 | 2001-02-11T14:03 | 2001-02-11T20:10 | 11 | 12H | 12 | Day 11 Dose | 2001-02-11T08:00 | PT12H | -PT6H |
| 26 | ABC-123 | PC | 123-0001 | 26 | Day 11 | A554134-19 | PH | PH | SPECIMEN PROPERTY | URINE | 5.5 |  | 5.5 | 5.5 |  |  |  |  | 3 | DAY 11 | 11 | 2001-02-11T14:03 | 2001-02-11T20:10 | 11 | 12H | 12 | Day 11 Dose | 2001-02-11T08:00 | PT12H | -PT6H |
| 27 | ABC-123 | PC | 123-0001 | 27 | Day 11 | A554134-20 | DRGA_MET | Drug A Metabolite | ANALYTE | URINE | 280 | ng/mL | 280 | 280 | ng/mL |  | 2.00 |  | 4 | DAY 12 | 12 | 2001-02-11T20:03 | 2001-02-12T08:10 | 12 | 24H | 24 | Day 11 Dose | 2001-02-11T08:00 | PT24H | -PT12H |
| 28 | ABC-123 | PC | 123-0001 | 28 | Day 11 | A554134-20 | DRGA_PAR | Drug A Parent | ANALYTE | URINE | 2.4 | ng/mL | 2.4 | 2.4 | ng/mL |  | 2.00 |  | 4 | DAY 12 | 12 | 2001-02-11T20:03 | 2001-02-12T08:10 | 12 | 24H | 24 | Day 11 Dose | 2001-02-11T08:00 | PT24H | -PT12H |
| 29 | ABC-123 | PC | 123-0001 | 29 | Day 11 | A554134-20 | VOLUME | Volume | SPECIMEN PROPERTY | URINE | 606 | mL | 606 | 606 | mL |  |  |  | 4 | DAY 12 | 12 | 2001-02-11T20:03 | 2001-02-12T08:10 | 12 | 24H | 24 | Day 11 Dose | 2001-02-11T08:00 | PT24H | -PT12H |
| 30 | ABC-123 | PC | 123-0001 | 30 | Day 11 | A554134-20 | PH | PH | SPECIMEN PROPERTY | URINE | 5.5 |  | 5.5 | 5.5 |  |  |  |  | 4 | DAY 12 | 12 | 2001-02-11T20:03 | 2001-02-12T08:10 | 12 | 24H | 24 | Day 11 Dose | 2001-02-11T08:00 | PT24H | -PT12H |
| 31 | ABC-123 | PC | 123-0001 | 31 | Day 11 | A554134-21 | DRGA_MET | Drug A Metabolite | ANALYTE | PLASMA | 3.73 | ng/mL | 3.73 | 3.73 | ng/mL |  | 0.10 | 20 | 4 | DAY 12 | 12 | 2001-02-12T08:00 |  | 12 | 24H | 24 | Day 11 Dose | 2001-02-11T08:00 | PT24H |  |
| 32 | ABC-123 | PC | 123-0001 | 32 | Day 11 | A554134-21 | DRGA_PAR | Drug A Parent | ANALYTE | PLASMA | <0.1 | ng/mL | <0.1 |  | ng/mL |  | 0.10 | 20 | 4 | DAY 12 | 12 | 2001-02-12T08:00 |  | 12 | 24H | 24 | Day 11 Dose | 2001-02-11T08:00 | PT24H |  |

##### 6.3.5.9.2 Pharmacokinetics Parameters (PP)

###### PP – Description/Overview
A findings domain that contains pharmacokinetic parameters derived from pharmacokinetic concentration-time (PC) data.

###### PP – Specification
pp.xpt, Pharmacokinetics Parameters — Findings. One record per PK parameter per time-concentration profile per modeling method per subject, Tabulation.

**Structure:** One record per PK parameter per time-concentration profile per modeling method per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | PP |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | PPSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | PPGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | PPTESTCD | Parameter Short Name | Char | Topic | Req | C85839 |
| 7 | PPTEST | Parameter Name | Char | Synonym Qualifier | Req | C85493 |
| 8 | PPCAT | Parameter Category | Char | Grouping Qualifier | Exp |  |
| 9 | PPSCAT | Parameter Subcategory | Char | Grouping Qualifier | Perm |  |
| 10 | PPORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 11 | PPORRESU | Original Units | Char | Variable Qualifier | Exp | C85494; C128684; C128683; C128685; C128686 |
| 12 | PPSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 13 | PPSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |
| 14 | PPSTRESU | Standard Units | Char | Variable Qualifier | Exp | C85494; C128684; C128683; C128685; C128686 |
| 15 | PPSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 16 | PPREASND | Reason Parameter Not Calculated | Char | Record Qualifier | Perm |  |
| 17 | PPSPEC | Specimen Material Type | Char | Record Qualifier | Exp | C78734 |
| 18 | PPANMETH | Analysis Method | Char | Record Qualifier | Perm | C172330 |
| 19 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 20 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 21 | PPDTC | Date/Time of Parameter Calculations | Char | Timing | Perm | ISO 8601 datetime or interval |
| 22 | PPDY | Study Day of Parameter Calculations | Num | Timing | Perm |  |
| 23 | PPTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 24 | PPRFTDTC | Date/Time of Reference Point | Char | Timing | Exp | ISO 8601 datetime or interval |
| 25 | PPSTINT | Planned Start of Assessment Interval | Char | Timing | Perm | ISO 8601 duration |
| 26 | PPENINT | Planned End of Assessment Interval | Char | Timing | Perm | ISO 8601 duration |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **PPSEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **PPGRPID**: Used to tie together a block of related records in a single domain to support relationships within the domain and between domains.
- **PPTESTCD**: Short name of the pharmacokinetic parameter. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PPTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PPTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "AUCALL", "TMAX", "CMAX".
- **PPTEST**: Name of the pharmacokinetic parameter. The value in PPTEST cannot be longer than 40 characters. Examples: "AUC All", "Time of CMAX", "Max Conc".
- **PPCAT**: Used to define a category of related records. For PP, this should be the name of the analyte in PCTEST whose profile the parameter is associated with.
- **PPSCAT**: Categorization of the model type used to calculate the PK parameters. Examples: "COMPARTMENTAL", "NON-COMPARTMENTAL".
- **PPORRES**: Result of the measurement or finding as originally received or collected.
- **PPORRESU**: Original units in which the data were collected. The unit for PPORRES. Example: "ng/L". See PP Assumption 3.
- **PPSTRESC**: Contains the result value for all findings, copied or derived from PPORRES in a standard format or standard units. PPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in PPSTRESN.
- **PPSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from PPSTRESC. PPSTRESN should store all numeric test results or findings.
- **PPSTRESU**: Standardized unit used for PPSTRESC and PPSTRESN. See PP Assumption 3.
- **PPSTAT**: Used to indicate that a parameter was not calculated. Should be null if a result exists in PPORRES.
- **PPREASND**: Describes why a parameter was not calculated, such as "INSUFFICIENT DATA". Used in conjunction with PPSTAT when value is "NOT DONE".
- **PPSPEC**: Defines the type of specimen used for a measurement. If multiple specimen types are used for a calculation (e.g., serum and urine for renal clearance), then this field should be left blank. Examples: "SERUM", "PLASMA", "URINE".
- **PPANMETH**: Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result. Example: A named formula used to calculate AUC, such as "LIN-LOG TRAPEZOIDAL METHOD".; Sponsor-defined formulas can also be represented by this variable. Example: Calculating ratio AUCs where the PPANMETH may be "DRUG METABOLITE 1 TO DRUG PARENT" or "DRUG METABOLITE 2 TO METABOLITE 1".
- **TAETORD**: Number that gives the planned order of the element within the arm.
- **EPOCH**: Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.
- **PPDTC**: Nominal date/time of parameter calculations.
- **PPDY**: Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.
- **PPTPTREF**: The description of a time point that acts as a fixed reference for a series of planned time points.
- **PPRFTDTC**: Date/time of the reference time point from the PC records used to calculate a parameter record. The values in PPRFTDTC should be the same as that in PCRFTDTC for related records.
- **PPSTINT**: The start of a planned evaluation or assessment interval relative to the time point reference.
- **PPENINT**: The end of a planned evaluation or assessment interval relative to the time point reference.


###### PP – Assumptions
1. Pharmacokinetics Parameters is a derived dataset, and may be produced from an analysis dataset with a different structure. As a result, some sponsors may need to normalize their analysis dataset in order for it to fit into the SDTM-based PP domain.
2. Information pertaining to all parameters (e.g., number of exponents, model weighting) should be submitted in the SUPPPP dataset.
3. There are separate codelists used for PPORRESU/PPSTRESU where the choice depends on whether the value of the pharmacokinetic parameter is normalized.
    a. Codelist “PKUNIT” is used for non-normalized parameters.
    b. Codelists “PKUDMG” and “PKUDUG” are used when parameters are normalized by dose amount in milligrams or micrograms, respectively.
    c. Codelists “PKUWG” and “PKUWKG” are used when parameters are normalized by weight in grams or kilograms, respectively.
4. Multiple subset codelists were created for the unique unit expressions of the same concept across codelists. This approach allows study-context appropriate use of unit values for pharmacokinetics (PK) analysis subtypes. Controlled Terminology Rules for PK are available at https://www.cdisc.org/standards/terminology/controlled-terminology.
5. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the PP domain, but the following qualifiers would not generally be used: --BODSYS, --SEV.

###### PP – Examples

**Example 1**
This example shows PK parameters calculated from time-concentration profiles for the parent drug and 1 metabolite in plasma and urine for one subject. Note that PPRFTDTC is populated in order to link the PP records to the respective PC records. In this example, PPSPEC is null for observed total clearance (PPTESTCD = "CLO") records because it is calculated from multiple specimen sources (i.e., plasma and urine).
**Rows 1-12:** Show parameters for day 1.
**Rows 13-24:** Show parameters for day 11.
*pp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPGRPID | PPTESTCD | PPTEST | PPCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | VISITNUM | VISIT | PPDTC | PPRFTDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PP | ABC-123-0001 | 1 | DAY1_PAR | TMAX | Time of CMAX | DRUG A PARENT | 1.87 | h | 1.87 | 1.87 | h | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 2 | ABC-123 | PP | ABC-123-0001 | 2 | DAY1_PAR | CMAX | Max Conc | DRUG A PARENT | 44.5 | ug/L | 44.5 | 44.5 | ug/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 3 | ABC-123 | PP | ABC-123-0001 | 3 | DAY1_PAR | AUCALL | AUC All | DRUG A PARENT | 294.7 | h*mg/L | 294.7 | 294.7 | h*mg/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 4 | ABC-123 | PP | ABC-123-0001 | 4 | DAY1_PAR | LAMZHL | Half-Life Lambda z | DRUG A PARENT | 0.75 | h | 0.75 | 0.75 | h | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 5 | ABC-123 | PP | ABC-123-0001 | 5 | DAY1_PAR | VZO | Vz Obs | DRUG A PARENT | 10.9 | L | 10.9 | 10.9 | L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 6 | ABC-123 | PP | ABC-123-0001 | 6 | DAY1_PAR | CLO | Total CL Obs | DRUG A PARENT | 1.68 | L/h | 1.68 | 1.68 | L/h |  | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 7 | ABC-123 | PP | ABC-123-0001 | 7 | DAY1_MET | TMAX | Time of CMAX | DRUG A METABOLITE | 0.94 | h | 0.94 | 0.94 | h | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 8 | ABC-123 | PP | ABC-123-0001 | 8 | DAY1_MET | CMAX | Max Conc | DRUG A METABOLITE | 22.27 | ug/L | 22.27 | 22.27 | ug/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 9 | ABC-123 | PP | ABC-123-0001 | 9 | DAY1_MET | AUCALL | AUC All | DRUG A METABOLITE | 147.35 | h*mg/L | 147.35 | 147.35 | h*mg/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 10 | ABC-123 | PP | ABC-123-0001 | 10 | DAY1_MET | LAMZHL | Half-Life Lambda z | DRUG A METABOLITE | 0.38 | h | 0.38 | 0.38 | h | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 11 | ABC-123 | PP | ABC-123-0001 | 11 | DAY1_MET | VZO | Vz Obs | DRUG A METABOLITE | 5.45 | L | 5.45 | 5.45 | L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 12 | ABC-123 | PP | ABC-123-0001 | 12 | DAY1_MET | CLO | Total CL Obs | DRUG A METABOLITE | 0.84 | L/h | 0.84 | 0.84 | L/h |  | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
| 13 | ABC-123 | PP | ABC-123-0001 | 13 | DAY11_PAR | TMAX | Time of CMAX | DRUG A PARENT | 1.91 | h | 1.91 | 1.91 | h | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 14 | ABC-123 | PP | ABC-123-0001 | 14 | DAY11_PAR | CMAX | Max Conc | DRUG A PARENT | 46.0 | ug/L | 46.0 | 46.0 | ug/L | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 15 | ABC-123 | PP | ABC-123-0001 | 15 | DAY11_PAR | AUCALL | AUC All | DRUG A PARENT | 289.0 | h*mg/L | 289.0 | 289.0 | h*mg/L | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 16 | ABC-123 | PP | ABC-123-0001 | 16 | DAY11_PAR | LAMZHL | Half-Life Lambda z | DRUG A PARENT | 0.77 | h | 0.77 | 0.77 | h | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 17 | ABC-123 | PP | ABC-123-0001 | 17 | DAY11_PAR | VZO | Vz Obs | DRUG A PARENT | 10.7 | L | 10.7 | 10.7 | L | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 18 | ABC-123 | PP | ABC-123-0001 | 18 | DAY11_PAR | CLO | Total CL Obs | DRUG A PARENT | 1.75 | L/h | 1.75 | 1.75 | L/h |  | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 19 | ABC-123 | PP | ABC-123-0001 | 19 | DAY11_MET | TMAX | Time of CMAX | DRUG A METABOLITE | 0.96 | h | 0.96 | 0.96 | h | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 20 | ABC-123 | PP | ABC-123-0001 | 20 | DAY11_MET | CMAX | Max Conc | DRUG A METABOLITE | 23.00 | ug/L | 23.00 | 23.00 | ug/L | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 21 | ABC-123 | PP | ABC-123-0001 | 21 | DAY11_MET | AUCALL | AUC All | DRUG A METABOLITE | 144.50 | h*mg/L | 144.50 | 144.50 | h*mg/L | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 22 | ABC-123 | PP | ABC-123-0001 | 22 | DAY11_MET | LAMZHL | Half-Life Lambda z | DRUG A METABOLITE | 0.39 | h | 0.39 | 0.39 | h | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 23 | ABC-123 | PP | ABC-123-0001 | 23 | DAY11_MET | VZO | Vz Obs | DRUG A METABOLITE | 5.35 | L | 5.35 | 5.35 | L | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
| 24 | ABC-123 | PP | ABC-123-0001 | 24 | DAY11_MET | CLO | Total CL Obs | DRUG A METABOLITE | 0.88 | L/h | 0.88 | 0.88 | L/h |  | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |

**Example 2**
This example shows various AUCs calculated using sponsor-defined formulas or the linear-log trapezoidal method.
**Rows 1-3:** Show the "AUC from T1 to T2" measurements for Drug Parent (row 1), Drug Metabolite 1 (row 2) and Drug Metabolite 2 (row 3). These parameters are calculated using the LIN-LOG TRAPEZOIDAL METHOD which is in PPANMETH.
**Row 4:** Shows the "Ratio AUC" measurement of Drug Metabolite 1 to Drug Parent. Instead of pre-coordinating "Ratio AUC of Drug Metabolite 1 to Drug Parent" all into the PPTEST, PPANMETH is used to describe the numerator (Drug Metabolite 1) and the denominator (Drug Parent) values that contribute to the Ratio AUC calculation in PPTEST. This post-coordination approach liberates the PPTEST variable from having to house hyper-specific, pre-coordinated PK parameter values.
**Row 5:** Shows the "Ratio AUC" measurement of Drug Metabolite 2 to Drug Metabolite 1. Note the PPTEST is Ratio AUC, whereas DRUG METABOLITE 2 TO METABOLITE 1 is in PPANMETH.
**Rows 6-7:** Show AUC Infinity Obs and AUC Infinity Pred for the DRUG PARENT. Both are calculated using the LIN-LOG TRAPEZOIDAL METHOD which is in PPANMETH.
*pp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPREFID | PPTESTCD | PPTEST | PPCAT | PPSCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | PPANMETH | PPFAST | PPNOMDY | PPRFTDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PP | 123-1001 | 1 | B2222 | AUCINT | AUC from T1 to T2 | DRUG PARENT | NCA | 154.1 | h*ng/L | 154.1 | 154.1 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
| 2 | ABC-123 | PP | 123-1001 | 2 | B2222 | AUCINT | AUC from T1 to T2 | DRUG METABOLITE 1 | NCA | 144.5 | h*ng/L | 144.5 | 144.5 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
| 3 | ABC-123 | PP | 123-1001 | 3 | B2222 | AUCINT | AUC from T1 to T2 | DRUG METABOLITE 2 | NCA | 294.7 | h*ng/L | 294.7 | 294.7 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
| 4 | ABC-123 | PP | 123-1001 | 4 | B2222 | RAAUC | Ratio AUC | DRUG METABOLITE 1 | NCA | 1.07 |  | 1.07 | 1.07 |  | PLASMA | DRUG METABOLITE 1 TO DRUG PARENT | Y | 1 | 2001-02-01T12:00 |
| 5 | ABC-123 | PP | 123-1001 | 5 | B2222 | RAAUC | Ratio AUC | DRUG METABOLITE 2 | NCA | 0.52 |  | 0.52 | 0.52 |  | PLASMA | DRUG METABOLITE 2 TO METABOLITE 1 | Y | 1 | 2001-02-01T12:00 |
| 6 | ABC-123 | PP | 123-1001 | 1 | B2222 | AUCIFO | AUC Infinity Obs | DRUG PARENT | NCA | 520 | h*ng/L | 520 | 520 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
| 7 | ABC-123 | PP | 123-1001 | 2 | B2222 | AUCIFP | AUC Infinity Pred | DRUG PARENT | NCA | 510 | h*ng/L | 510 | 510 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |

The SUPPPP dataset example shows the specific condition under which the PK analysis was performed.
*supppp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PP | 123-1001 | PPSEQ | 1 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected |  |
| 2 | ABC-123 | PP | 123-1001 | PPSEQ | 2 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected |  |
| 3 | ABC-123 | PP | 123-1001 | PPSEQ | 3 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected |  |
| 4 | ABC-123 | PP | 123-1001 | PPSEQ | 4 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected |  |
| 5 | ABC-123 | PP | 123-1001 | PPSEQ | 5 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected |  |
| 6 | ABC-123 | PP | 123-1001 | PPSEQ | 6 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected |  |
| 7 | ABC-123 | PP | 123-1001 | PPSEQ | 7 | PKCOND | Condition of PK Analysis | SINGLE DOSE |  |  |

**Example 3**
This example shows the use of PPSTINT and PPENINT to describe the AUC segments for the test code "AUCINT", the area under the curve from time T1 to time T2. Time T1 is represented in PPSTINT as the elapsed time since PPRFTDTC and time T2 is represented in PPENINT as the elapsed time since PPRFTDTC.
**Rows 1-7:** Show parameters for day 1.
**Rows 8-14:** Show parameters for day 14.
*pp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPGRPID | PPTESTCD | PPTEST | PPCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | VISITNUM | VISIT | PPDTC | PPRFTDTC | PPSTINT | PPENINT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PP | ABC-123-001 | 1 | DRUGA_DAY1 | TMAX | Time of CMAX | DRUG A PARENT | 0.65 | h | 0.65 | 0.65 | h | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 |  |  |
| 2 | ABC-123 | PP | ABC-123-001 | 2 | DRUGA_DAY1 | CMAX | Max Conc | DRUG A PARENT | 6.92 | ng/mL | 6.92 | 6.92 | ng/mL | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 |  |  |
| 3 | ABC-123 | PP | ABC-123-001 | 3 | DRUGA_DAY1 | AUCALL | AUC All | DRUG A PARENT | 45.5 | h*ng/mL | 45.5 | 45.5 | h*ng/mL | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 |  |  |
| 4 | ABC-123 | PP | ABC-123-001 | 4 | DRUGA_DAY1 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 43.6 | h*ng/mL | 43.6 | 43.6 | h*ng/mL | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 | PT0M | PT24H |
| 5 | ABC-123 | PP | ABC-123-001 | 5 | DRUGA_DAY1 | LAMZHL | Half-Life Lambda z | DRUG A PARENT | 7.74 | h | 7.74 | 7.74 | h | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 |  |  |
| 6 | ABC-123 | PP | ABC-123-001 | 6 | DRUGA_DAY1 | VZFO | Vz Obs by F | DRUG A PARENT | 256 | L | 256000 | 256 | L | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 |  |  |
| 7 | ABC-123 | PP | ABC-123-001 | 7 | DRUGA_DAY1 | CLFO | Total CL Obs by F | DRUG A PARENT | 20.2 | L/hr | 20200 | 20.2 | L/h | PLASMA | 1 | DAY 1 | 2001-02-25 | 2001-02-01T08:00 |  |  |
| 8 | ABC-123 | PP | ABC-123-001 | 15 | DRUGA_DAY14 | TMAX | Time of CMAX | DRUG A PARENT | 0.65 | h | 0.65 | 0.65 | h | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 |  |  |
| 9 | ABC-123 | PP | ABC-123-001 | 16 | DRUGA_DAY14 | CMAX | Max Conc | DRUG A PARENT | 6.51 | ng/mL | 6.51 | 6.51 | ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 |  |  |
| 10 | ABC-123 | PP | ABC-123-001 | 17 | DRUGA_DAY14 | AUCALL | AUC All | DRUG A PARENT | 34.2 | h*ng/mL | 34.2 | 34.2 | h*ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 |  |  |
| 11 | ABC-123 | PP | ABC-123-001 | 18 | DRUGA_DAY14 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 35.6 | h*ng/mL | 35.6 | 35.6 | h*ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 | PT0M | PT24H |
| 12 | ABC-123 | PP | ABC-123-001 | 19 | DRUGA_DAY14 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 38.4 | h*ng/mL | 38.4 | 38.4 | h*ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 | PT0M | PT48H |
| 13 | ABC-123 | PP | ABC-123-001 | 20 | DRUGA_DAY14 | AUCINT | AUC from T1 to T2 | DRUG A PARENT | 2.78 | h*ng/mL | 2.78 | 2.78 | h*ng/mL | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 | PT24H | PT48H |
| 14 | ABC-123 | PP | ABC-123-001 | 21 | DRUGA_DAY14 | LAMZHL | Half-Life Lambda z | DRUG A PARENT | 7.6 | h | 7.6 | 7.6 | h | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 |  |  |
| 15 | ABC-123 | PP | ABC-123-001 | 22 | DRUGA_DAY14 | VZFO | Vz Obs by F | DRUG A PARENT | 283 | L | 283 | 283 | L | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 |  |  |
| 16 | ABC-123 | PP | ABC-123-001 | 23 | DRUGA_DAY14 | CLFO | Total CL Obs by F | DRUG A PARENT | 28.1 | L/h | 28.1 | 28.1 | L/h | PLASMA | 2 | DAY 14 | 2001-02-25 | 2001-02-15T08:00 |  |  |

##### 6.3.5.9.3 Relating PP Records to PC Records

Sponsors must document the concentrations used to calculate each parameter. This may be done in analysis dataset metadata or by documenting relationships between records in the Pharmacokinetics Parameters (PP) and Pharmacokinetics Concentrations (PC) datasets in a RELREC dataset (see Section 8.2, Relating Peer Records, and Section 8.3, Relating Datasets).

**PC-PP – Relating Datasets**
If all time-point concentrations in PC are used to calculate all parameters for all subjects, then the relationship between the 2 datasets can be documented as shown in this table:
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC |  | PCGRPID |  | MANY | A |
| 2 | ABC-123 | PP |  | PPGRPID |  | MANY | A |

Note that the reference time point and the analyte are part of the natural key (see Section 3.2.1.1, Primary Keys) for both datasets. In this relationship, --GRPID is a surrogate key, and must be populated so that each combination of analyte and reference time point has a separate value of --GRPID.

**PC-PP – Relating Records**
This section illustrates 4 methods for representing relationships between PC and PP records under 4 different circumstances. All these examples are based on the same PC and PP data for 1 drug (i.e., drug X). The different methods for representing relationships are based on which linking variables are used in RELREC.
- Method A (many to many, using PCGRPID and PPGRPID)
- Method B (one to many, using PCSEQ and PPGRPID)
- Method C (many to one, using PCGRPID and PPSEQ)
- Method D (one to one, using PCSEQ and PPSEQ)

The different examples illustrate situations in which different subsets of the pharmacokinetic concentration data were used in calculating the pharmacokinetic parameters. As in the example above, --GRPID values must take into account all the combinations of analytes and reference time points; both are part of the natural key for both datasets. For each example, PCGRPID and PPGRPID were used to group related records within each respective dataset. The exclusion of some concentration values from the calculation of some parameters affects the values of PCGRPID and PPGRPID for the different situations. To conserve space, the PC and PP domains appear only once, but with 4 --GRPID columns, 1 for each of the example situations.
Note that a submission dataset would contain only 1 --GRPID column with a set of values such as those shown in 1 of the 4 columns in the PC and PP datasets.

**Pharmacokinetic Concentrations (PC) Dataset for All Examples**
*pc.xpt*

| Row | STUDYID | DOMAIN | USUBJID | PCSEQ | PCGRPID (Ex 1) | PCGRPID (Ex 2) | PCGRPID (Ex 3) | PCGRPID (Ex 4) | PCREFID | PCTESTCD | PCTEST | PCCAT | PCORRES | PCORRESU | PCSTRESC | PCSTRESN | PCSTRESU | PCSPEC | PCBLFL | PCLLOQ | PCDTC | PCDY | PCNOMDY | PCTPT | PCTPTNUM | PCELTM | PCTPTREF | PCRFTDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | 1 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX_A | 123-0001-01 | DRUG X | STUDYDRUG | ANALYTE | 9 | ug/mL | 9 | 9 | ug/mL | PLASMA |  | 1.00 | 2001-02-01T08:35 | 1 | 1 | 5 min | 1 | PT5M | Day 1 Dose | 2001-02-01T08:30 |
| 2 | ABC-123 | PC | ABC-123-0001 | 2 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX_A | 123-0001-02 | DRUG X | STUDYDRUG | ANALYTE | 20 | ug/mL | 20 | 20 | ug/mL | PLASMA |  | 1.00 | 2001-02-01T08:55 | 1 | 1 | 25 min | 2 | PT25M | Day 1 Dose | 2001-02-01T08:30 |
| 3 | ABC-123 | PC | ABC-123-0001 | 3 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX_A | 123-0001-03 | DRUG X | STUDYDRUG | ANALYTE | 31 | ug/mL | 31 | 31 | ug/mL | PLASMA |  | 1.00 | 2001-02-01T09:20 | 1 | 1 | 50 min | 3 | PT50M | Day 1 Dose | 2001-02-01T08:30 |
| 4 | ABC-123 | PC | ABC-123-0001 | 4 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX_A | 123-0001-04 | DRUG X | STUDYDRUG | ANALYTE | 38 | ug/mL | 38 | 38 | ug/mL | PLASMA |  | 1.00 | 2001-02-01T09:45 | 1 | 1 | 75 min | 4 | PT1H15M | Day 1 Dose | 2001-02-01T08:30 |
| 5 | ABC-123 | PC | ABC-123-0001 | 5 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX_B | 123-0001-05 | DRUG X | STUDYDRUG | ANALYTE | 45 | ug/mL | 45 | 45 | ug/mL | PLASMA |  | 1.00 | 2001-02-01T10:10 | 1 | 1 | 100 min | 5 | PT1H40M | Day 1 Dose | 2001-02-01T08:30 |
| 6 | ABC-123 | PC | ABC-123-0001 | 6 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX_C | 123-0001-06 | DRUG X | STUDYDRUG | ANALYTE | 48 | ug/mL | 48 | 48 | ug/mL | PLASMA |  | 1.00 | 2001-02-01T10:35 | 1 | 1 | 125 min | 6 | PT2H5M | Day 1 Dose | 2001-02-01T08:30 |
| 7 | ABC-123 | PC | ABC-123-0001 | 7 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX_A | 123-0001-07 | DRUG X | STUDYDRUG | ANALYTE | 41 | ug/mL | 41 | 41 | ug/mL | PLASMA |  | 1.00 | 2001-02-01T11:00 | 1 | 1 | 150 min | 7 | PT2H30M | Day 1 Dose | 2001-02-01T08:30 |
| 8 | ABC-123 | PC | ABC-123-0001 | 8 | DY1_DRGX | EXCLUDE | DY1_DRGX_B | DY1_DRGX_A | 123-0001-08 | DRUG X | STUDYDRUG | ANALYTE | 35 | ug/mL | 35 | 35 | ug/mL | PLASMA |  | 1.00 | 2001-02-01T11:50 | 1 | 1 | 200 min | 8 | PT3H20M | Day 1 Dose | 2001-02-01T08:30 |
| 9 | ABC-123 | PC | ABC-123-0001 | 9 | DY1_DRGX | EXCLUDE | DY1_DRGX_B | DY1_DRGX_A | 123-0001-09 | DRUG X | STUDYDRUG | ANALYTE | 31 | ug/mL | 31 | 31 | ug/mL | PLASMA |  | 1.00 | 2001-02-01T12:40 | 1 | 1 | 250 min | 9 | PT4H10M | Day 1 Dose | 2001-02-01T08:30 |
| 10 | ABC-123 | PC | ABC-123-0001 | 10 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX_A | 123-0001-10 | DRUG X | STUDYDRUG | ANALYTE | 25 | ug/mL | 25 | 25 | ug/mL | PLASMA |  | 1.00 | 2001-02-01T14:45 | 1 | 1 | 375 min | 10 | PT6H15M | Day 1 Dose | 2001-02-01T08:30 |
| 11 | ABC-123 | PC | ABC-123-0001 | 11 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX_D | 123-0001-11 | DRUG X | STUDYDRUG | ANALYTE | 18 | ug/mL | 18 | 18 | ug/mL | PLASMA |  | 1.00 | 2001-02-01T16:50 | 1 | 1 | 500 min | 11 | PT8H20M | Day 1 Dose | 2001-02-01T08:30 |
| 12 | ABC-123 | PC | ABC-123-0001 | 12 | DY1_DRGX | DY1_DRGX | DY1_DRGX_A | DY1_DRGX_D | 123-0001-12 | DRUG X | STUDYDRUG | ANALYTE | 12 | ug/mL | 12 | 12 | ug/mL | PLASMA |  | 1.00 | 2001-02-01T18:30 | 1 | 1 | 600 min | 12 | PT10H | Day 1 Dose | 2001-02-01T08:30 |
| 13 | ABC-123 | PC | ABC-123-0001 | 13 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-13 | DRUG X | STUDYDRUG | ANALYTE | 10 | ug/mL | 10 | 10 | ug/mL | PLASMA |  | 1.00 | 2001-02-08T08:35 | 8 | 8 | 5 min | 1 | PT5M | Day 8 Dose | 2001-02-08T08:30 |
| 14 | ABC-123 | PC | ABC-123-0001 | 14 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-14 | DRUG X | STUDYDRUG | ANALYTE | 21 | ug/mL | 21 | 21 | ug/mL | PLASMA |  | 1.00 | 2001-02-08T08:55 | 8 | 8 | 25 min | 2 | PT25M | Day 8 Dose | 2001-02-08T08:30 |
| 15 | ABC-123 | PC | ABC-123-0001 | 15 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-15 | DRUG X | STUDYDRUG | ANALYTE | 32 | ug/mL | 32 | 32 | ug/mL | PLASMA |  | 1.00 | 2001-02-08T09:20 | 8 | 8 | 50 min | 3 | PT50M | Day 8 Dose | 2001-02-08T08:30 |
| 16 | ABC-123 | PC | ABC-123-0001 | 16 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-16 | DRUG X | STUDYDRUG | ANALYTE | 39 | ug/mL | 39 | 39 | ug/mL | PLASMA |  | 1.00 | 2001-02-08T09:45 | 8 | 8 | 75 min | 4 | PT1H15M | Day 8 Dose | 2001-02-08T08:30 |
| 17 | ABC-123 | PC | ABC-123-0001 | 17 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-17 | DRUG X | STUDYDRUG | ANALYTE | 46 | ug/mL | 46 | 46 | ug/mL | PLASMA |  | 1.00 | 2001-02-08T10:10 | 8 | 8 | 100 min | 5 | PT1H40M | Day 8 Dose | 2001-02-08T08:30 |
| 18 | ABC-123 | PC | ABC-123-0001 | 18 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-18 | DRUG X | STUDYDRUG | ANALYTE | 48 | ug/mL | 48 | 48 | ug/mL | PLASMA |  | 1.00 | 2001-02-08T10:35 | 8 | 8 | 125 min | 6 | PT2H5M | Day 8 Dose | 2001-02-08T08:30 |
| 19 | ABC-123 | PC | ABC-123-0001 | 19 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-19 | DRUG X | STUDYDRUG | ANALYTE | 40 | ug/mL | 40 | 40 | ug/mL | PLASMA |  | 1.00 | 2001-02-08T11:00 | 8 | 8 | 150 min | 7 | PT2H30M | Day 8 Dose | 2001-02-08T08:30 |
| 20 | ABC-123 | PC | ABC-123-0001 | 20 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-20 | DRUG X | STUDYDRUG | ANALYTE | 35 | ug/mL | 35 | 35 | ug/mL | PLASMA |  | 1.00 | 2001-02-08T11:50 | 8 | 8 | 200 min | 8 | PT3H20M | Day 8 Dose | 2001-02-08T08:30 |
| 21 | ABC-123 | PC | ABC-123-0001 | 21 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-21 | DRUG X | STUDYDRUG | ANALYTE | 30 | ug/mL | 30 | 30 | ug/mL | PLASMA |  | 1.00 | 2001-02-08T12:40 | 8 | 8 | 250 min | 9 | PT4H10M | Day 8 Dose | 2001-02-08T08:30 |
| 22 | ABC-123 | PC | ABC-123-0001 | 22 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-22 | DRUG X | STUDYDRUG | ANALYTE | 24 | ug/mL | 24 | 24 | ug/mL | PLASMA |  | 1.00 | 2001-02-08T14:45 | 8 | 8 | 375 min | 10 | PT6H15M | Day 8 Dose | 2001-02-08T08:30 |
| 23 | ABC-123 | PC | ABC-123-0001 | 23 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-23 | DRUG X | STUDYDRUG | ANALYTE | 17 | ug/mL | 17 | 17 | ug/mL | PLASMA |  | 1.00 | 2001-02-08T16:50 | 8 | 8 | 500 min | 11 | PT8H20M | Day 8 Dose | 2001-02-08T08:30 |
| 24 | ABC-123 | PC | ABC-123-0001 | 24 | DY8_DRGX | DY8_DRGX | DY8_DRGX | DY8_DRGX | 123-0002-24 | DRUG X | STUDYDRUG | ANALYTE | 11 | ug/mL | 11 | 11 | ug/mL | PLASMA |  | 1.00 | 2001-02-08T18:30 | 8 | 8 | 600 min | 12 | PT10H | Day 8 Dose | 2001-02-08T08:30 |

**Pharmacokinetic Parameters (PP) Dataset for All Examples**
*pp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPGRPID (Ex 1) | PPGRPID (Ex 2) | PPGRPID (Ex 3) | PPGRPID (Ex 4) | PPTESTCD | PPTEST | PPCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | PPNOMDY | PPRFTDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PP | ABC-123-0001 | 1 | DY1DRGX | DY1DRGX | DY1DRGX_A | TMAX | TMAX | Time of CMAX | DRUG X | 1.87 | h | 1.87 | 1.87 | h | PLASMA | 1 | 2001-02-01T08:35 |
| 2 | ABC-123 | PP | ABC-123-0001 | 2 | DY1DRGX | DY1DRGX | DY1DRGX_A | CMAX | CMAX | Max Conc | DRUG X | 44.5 | ng/mL | 44.5 | 44.5 | ng/mL | PLASMA | 1 | 2001-02-01T08:35 |
| 3 | ABC-123 | PP | ABC-123-0001 | 3 | DY1DRGX | DY1DRGX | DY1DRGX_A | AUC | AUCALL | AUC All | DRUG X | 294.7 | h*ug/mL | 294.7 | 294.7 | h*ug/mL | PLASMA | 1 | 2001-02-01T08:35 |
| 4 | ABC-123 | PP | ABC-123-0001 | 5 | DY1DRGX | DY1DRGX | DY1DRGX_HALF | OTHER | LAMZHL | Half-Life Lambda z | DRUG X | 4.69 | h | 4.69 | 4.69 | h | PLASMA | 1 | 2001-02-01T08:35 |
| 5 | ABC-123 | PP | ABC-123-0001 | 6 | DY1DRGX | DY1DRGX | DY1DRGX_A | OTHER | VZO | Vz Obs | DRUG X | 10.9 | L | 10.9 | 10.9 | L | PLASMA | 1 | 2001-02-01T08:35 |
| 6 | ABC-123 | PP | ABC-123-0001 | 7 | DY1DRGX | DY1DRGX | DY1DRGX_A | OTHER | CLO | Total CL Obs | DRUG X | 1.68 | L/h | 1.68 | 1.68 | L/h | PLASMA | 1 | 2001-02-01T08:35 |
| 7 | ABC-123 | PP | ABC-123-0001 | 8 | DY8DRGX | DY8DRGX | DY8DRGX | DY8DRGX | TMAX | Time of CMAX | DRUG X | 1.91 | h | 1.91 | 1.91 | h | PLASMA | 8 | 2001-02-08T08:35 |
| 8 | ABC-123 | PP | ABC-123-0001 | 9 | DY8DRGX | DY8DRGX | DY8DRGX | DY8DRGX | CMAX | Max Conc | DRUG X | 46.0 | ng/mL | 46.0 | 46.0 | ng/mL | PLASMA | 8 | 2001-02-08T08:35 |
| 9 | ABC-123 | PP | ABC-123-0001 | 10 | DY8DRGX | DY8DRGX | DY8DRGX | DY8DRGX | AUCALL | AUC All | DRUG X | 289.0 | h*ug/mL | 289.0 | 289.0 | h*ug/mL | PLASMA | 8 | 2001-02-08T08:35 |
| 10 | ABC-123 | PP | ABC-123-0001 | 12 | DY8DRGX | DY8DRGX | DY8DRGX | DY8DRGX | LAMZHL | Half-Life Lambda z | DRUG X | 4.50 | h | 4.50 | 4.50 | h | PLASMA | 8 | 2001-02-08T08:35 |
| 11 | ABC-123 | PP | ABC-123-0001 | 13 | DY8DRGX | DY8DRGX | DY8DRGX | DY8DRGX | VZO | Vz Obs | DRUG X | 10.7 | L | 10.7 | 10.7 | L | PLASMA | 8 | 2001-02-08T08:35 |
| 12 | ABC-123 | PP | ABC-123-0001 | 14 | DY8DRGX | DY8DRGX | DY8DRGX | DY8DRGX | CLO | Total CL Obs | DRUG X | 1.75 | L/h | 1.75 | 1.75 | L/h | PLASMA | 8 | 2001-02-08T08:35 |

**Example 1**
All PC records used to calculate all pharmacokinetic parameters.
This example uses --GRPID values in the PCGRPID (Example 1) and PPGRPID (Example 1) columns.

***Method A (Many to Many, Using PCGRPID and PPGRPID)***
**Rows 1-2:** The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX" and all PP records with PPGRPID = "DY1DRGX".
**Rows 3-4:** The relationship with RELID "2" includes all PC records with GRPID = "DY8_DRGX" and all PP records with GRPID = "DY8DRGX".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX |  | 1 |
| 2 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX |  | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY8_DRGX |  | 2 |
| 4 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY8DRGX |  | 2 |

***Method B (One to Many, Using PCSEQ and PPGRPID)***
**Rows 1-13:** The relationship with RELID "1" includes the individual PC records with PCSEQ values "1" to "12" and all PP records with PPGRPID = "DY1DRGX".
**Rows 14-26:** The relationship with RELID "2" includes the individual PC records with PCSEQ values "13" to "24" and all PP records with PPGRPID = "DY8DRGX".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 |  | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 |  | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 |  | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 |  | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 |  | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 |  | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 |  | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 |  | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 |  | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 |  | 1 |
| 11 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 |  | 1 |
| 12 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 |  | 1 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX |  | 1 |
| 14 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 13 |  | 2 |
| 15 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 14 |  | 2 |
| 16 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 15 |  | 2 |
| 17 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 16 |  | 2 |
| 18 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 17 |  | 2 |
| 19 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 18 |  | 2 |
| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 19 |  | 2 |
| 21 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 20 |  | 2 |
| 22 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 21 |  | 2 |
| 23 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 22 |  | 2 |
| 24 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 23 |  | 2 |
| 25 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 24 |  | 2 |
| 26 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY8DRGX |  | 2 |

***Method C (Many to One, Using PCGRPID and PPSEQ)***
**Rows 1-8:** The relationship with RELID = "1" includes all PC records with a PCGRPID = "DY1_DRGX" and PP records with PPSEQ values "1" through "7".
**Rows 9-16:** The relationship with RELID = "2" includes all PC records with a PCGRPID = "DY8_DRGX" and PP records with PPSEQ values of "8" through "14".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX |  | 1 |
| 2 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 |  | 1 |
| 3 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 |  | 1 |
| 4 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 |  | 1 |
| 5 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 |  | 1 |
| 6 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 |  | 1 |
| 7 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 |  | 1 |
| 8 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 |  | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY8_DRGX |  | 2 |
| 10 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 8 |  | 2 |
| 11 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 9 |  | 2 |
| 12 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 10 |  | 2 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 11 |  | 2 |
| 14 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 12 |  | 2 |
| 15 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 13 |  | 2 |
| 16 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 14 |  | 2 |

***Method D (One to One, Using PCSEQ and PPSEQ)***
**Rows 1-19:** The relationship with RELID "1" includes individual PC records with PCSEQ values "1" through "12" and PP records with PPSEQ values "1" through "7".
**Rows 20-38:** The relationship with RELID "2" includes individual PC records with PCSEQ values "13" through "24" and PP records with PPSEQ values "8" through "14".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 |  | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 |  | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 |  | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 |  | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 |  | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 |  | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 |  | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 |  | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 |  | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 |  | 1 |
| 11 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 |  | 1 |
| 12 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 |  | 1 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 |  | 1 |
| 14 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 |  | 1 |
| 15 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 |  | 1 |
| 16 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 |  | 1 |
| 17 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 |  | 1 |
| 18 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 |  | 1 |
| 19 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 |  | 1 |
| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 13 |  | 2 |
| 21 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 14 |  | 2 |
| 22 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 15 |  | 2 |
| 23 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 16 |  | 2 |
| 24 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 17 |  | 2 |
| 25 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 18 |  | 2 |
| 26 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 19 |  | 2 |
| 27 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 20 |  | 2 |
| 28 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 21 |  | 2 |
| 29 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 22 |  | 2 |
| 30 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 23 |  | 2 |
| 31 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 24 |  | 2 |
| 32 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 8 |  | 2 |
| 33 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 9 |  | 2 |
| 34 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 10 |  | 2 |
| 35 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 11 |  | 2 |
| 36 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 12 |  | 2 |
| 37 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 13 |  | 2 |
| 38 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 14 |  | 2 |

**Example 2**
Only some records in PC were used to calculate all pharmacokinetic parameters; time points 8 and 9 on day 1 were not used for any pharmacokinetic parameters.
This example uses --GRPID values in the PCGRPID (Example 2) and PPGRPID (Example 2) columns. Note that for the 2 excluded PC records, PCGRPID = "EXCLUDE"; for other PC records, PCGRPID = "DY1_DRGX".
All pharmacokinetic concentrations for day 8 were used to calculate all pharmacokinetic parameters. Because day 8 relationships are the same as in Example 1, they are not included here.

***Method A (Many to Many, Using PCGRPID and PPGRPID)***
The relationship with RELID "1" includes PC records with PCGRPID = "DY1_DRGX" and all PP records with PPGRPID = "DY1DRGX". PC records with PCGRPID = "EXCLUDE" are not included in this relationship.
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX |  | 1 |
| 2 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX |  | 1 |

***Method B (One to Many, Using PCSEQ and PPGRPID)***
The relationship with RELID "1" includes individual PC records with PCSEQ values "1" through "7" and "10" through "12", and all the PP records with PPGRPID = "DY1DRGX".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 |  | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 |  | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 |  | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 |  | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 |  | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 |  | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 |  | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 |  | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 |  | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 |  | 1 |
| 11 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX |  | 1 |

***Method C (Many to One, Using PCGRPID and PPSEQ)***
The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX" and individual PP records with PPSEQ values "1" through "7".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX |  | 1 |
| 2 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 |  | 1 |
| 3 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 |  | 1 |
| 4 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 |  | 1 |
| 5 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 |  | 1 |
| 6 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 |  | 1 |
| 7 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 |  | 1 |
| 8 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 |  | 1 |

***Method D (One to One, Using PCSEQ and PPSEQ)***
The relationship with RELID "1" includes individual PC records with PCSEQ values "1" through "7" and "10" through "12" and individual PP records with PPSEQ values "1" through "7".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 |  | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 |  | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 |  | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 |  | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 |  | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 |  | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 |  | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 |  | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 |  | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 |  | 1 |
| 11 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 |  | 1 |
| 12 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 |  | 1 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 |  | 1 |
| 14 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 |  | 1 |
| 15 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 |  | 1 |
| 16 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 |  | 1 |
| 17 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 |  | 1 |

**Example 3**
Only some records in PC were used to calculate some parameters; time points 8 and 9 on day 1 were not used for half-life calculations, but were used for other parameters.
This example uses --GRPID values in the PCGRPID (Example 3) and PPGRPID (Example 3) columns. Note that the 2 excluded PC records have PCGRPID = "DY1_DRGX_B"; the other PC records have PCGRPID = "DY1_DRGX_A". Note also that the PP records for half-life calculations have PPGRPID = "DY1DRGX_HALF", whereas the other PP records have PPGRPID = "DY1DRGX_A".
All pharmacokinetic concentrations for day 8 were used to calculate all pharmacokinetic parameters. Because day 8 relationships are the same as in Example 1, they are not included here.

***Method A (Many to Many, Using PCGRPID and PPGRPID)***
**Rows 1-3:** The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX_A", all PC records with PCGRPID = "DY1_DRGX_B" (which in this case is all the PP records for Day 1) and all PP records with PPGRPID = "DY1DRGX_A".
**Rows 4-5:** The relationship with RELID "2" includes only PC records with PCGRPID = "DY1_DRGX_A" and all PP records with PPGRPID = "DY1DRGX_HALF".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_A |  | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_B |  | 1 |
| 3 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX_A |  | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_A |  | 2 |
| 5 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX_HALF |  | 2 |

***Method B (One to Many, Using PCSEQ and PPGRPID)***
**Rows 1-13:** The relationship with RELID "1" includes PC records with PCSEQ values "1" through "12" and PP records with PPGRPID = "DY1DRGX_A".
**Rows 14-24:** The relationship with RELID "2" includes PC records with PCSEQ values "1" through "7" and "10" through "12" and PP records with PPGRPID = "DY1DRGX_HALF".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 |  | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 |  | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 |  | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 |  | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 |  | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 |  | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 |  | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 |  | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 |  | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 |  | 1 |
| 11 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 |  | 1 |
| 12 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 |  | 1 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX_A |  | 1 |
| 14 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 |  | 2 |
| 15 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 |  | 2 |
| 16 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 |  | 2 |
| 17 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 |  | 2 |
| 18 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 |  | 2 |
| 19 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 |  | 2 |
| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 |  | 2 |
| 21 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 |  | 2 |
| 22 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 |  | 2 |
| 23 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 |  | 2 |
| 24 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX_HALF |  | 2 |

***Method C (Many to One, Using PCGRPID and PPSEQ)***
**Rows 1-7:** The relationship with RELID "1" includes all PC records with PCGRPID values "DY1_DRGX_A" and "DY1_DRGX_B" and PP records with PPSEQ values "1" through "3", "6", and "7".
**Rows 8-14:** The relationship with RELID "2" includes only PC records with PCGRPID = "DY1_DRGX_A" and PP records with PPSEQ values "4" and "5".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_A |  | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_B |  | 1 |
| 3 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 |  | 1 |
| 4 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 |  | 1 |
| 5 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 |  | 1 |
| 6 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 |  | 1 |
| 7 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 |  | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1_DRGX_A |  | 2 |
| 9 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 |  | 2 |
| 10 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 |  | 2 |

***Method D (One to One, Using PCSEQ and PPSEQ)***
**Rows 1-17:** The relationship with RELID "1" includes individual PC records with PCSEQ values "1" through "12" and PP records with PPSEQ values "1" through "3", "6", and "7".
**Rows 18-29:** The relationship with RELID "2" includes PC records with PCSEQ values "1" through "7" and "10" through "12" and PP records with PPSEQ values "4" and "5".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 |  | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 |  | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 |  | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 |  | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 |  | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 |  | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 |  | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 |  | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 |  | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 |  | 1 |
| 11 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 |  | 1 |
| 12 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 |  | 1 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 |  | 1 |
| 14 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 |  | 1 |
| 15 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 |  | 1 |
| 16 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 |  | 1 |
| 17 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 |  | 1 |
| 18 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 |  | 2 |
| 19 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 |  | 2 |
| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 |  | 2 |
| 21 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 |  | 2 |
| 22 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 |  | 2 |
| 23 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 |  | 2 |
| 24 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 |  | 2 |
| 25 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 |  | 2 |
| 26 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 |  | 2 |
| 27 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 |  | 2 |
| 28 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 |  | 2 |
| 29 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 |  | 2 |

**Example 4**
Only some records in PC were used to calculate parameters; time point 5 was excluded from Tmax, time point 6 from Cmax, and time points 11 and 12 from AUC.
This example uses --GRPID values in the PCGRPID (Example 4) and PPGRPID (Example 4) columns. Note that 4 values of PCGRPID and 4 values of PPGRPID were used.
Because of the complexity of this example, only methods A and D are illustrated.

***Method A (Many to Many, Using PCGRPID and PPGRPID)***
**Rows 1-4:** The relationship with RELID "1" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_C", and "DY1DRGX_D" and the one PP record with PPGRPID = "TMAX".
**Rows 5-8:** The relationship with RELID "2" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", and "DY1DRGX_D" and the one PP record with PPGRPID = "CMAX".
**Rows 9-12:** The relationship with RELID "3" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", and "DY1DRGX_C" and the one PP record with PPGRPID = "AUC".
**Rows 13-17:** The relationship with RELID "4" includes PC records with PCGRPID values "DY1DRGX_A", "DY1DRGX_B", "DY1DRGX_C", and "DY1DRGX_D" (in this case, all PC records) and all PP records with PPGRPID = "OTHER".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PP | ABC-123-0001 | PPGRPID | TMAX |  | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_A |  | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_C |  | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_D |  | 1 |
| 5 | ABC-123 | PP | ABC-123-0001 | PPGRPID | CMAX |  | 2 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_A |  | 2 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_B |  | 2 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_D |  | 2 |
| 9 | ABC-123 | PP | ABC-123-0001 | PPGRPID | AUC |  | 3 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_A |  | 3 |
| 11 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_B |  | 3 |
| 12 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_C |  | 3 |
| 13 | ABC-123 | PP | ABC-123-0001 | PPGRPID | OTHER |  | 4 |
| 14 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_A |  | 4 |
| 15 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_B |  | 4 |
| 16 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_C |  | 4 |
| 17 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY1DRGX_D |  | 4 |

Note that in the RELREC table for method A, the single records in rows 1, 5, 9, and 13, represented by their PPGRPID values, could have been referenced by their PPSEQ values; both identify the records sufficiently.
At least 2 other hybrid approaches would also be acceptable:
- Using PPSEQ values; use PCGRPID values wherever possible
- Using PPGRPID values wherever possible; use PCSEQ values

Method D uses only PCSEQ and PPSEQ values.

***Method D (One to One, Using PCSEQ and PPSEQ)***
**Rows 1-12:** The relationship with RELID "1" includes PC records with PCSEQ values "1" through "4" and "6" through "12" and PP records with PPSEQ = "1".
**Rows 13-24:** The relationship with RELID "2" includes PC records with PCSEQ values "1" through "5" and "7" through "12" and PP records with PPSEQ = "2".
**Rows 25-35:** The relationship with RELID "3" includes PC records with PCSEQ values "1" through "10" and PP records with PPSEQ = "3".
**Rows 36-51:** The relationship with RELID "4" includes PC records with PCSEQ values "1" through "12" and PP records with PPSEQ values "4" through "7".
*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 |  | 1 |
| 2 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 |  | 1 |
| 3 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 |  | 1 |
| 4 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 |  | 1 |
| 5 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 |  | 1 |
| 6 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 |  | 1 |
| 7 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 |  | 1 |
| 8 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 |  | 1 |
| 9 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 |  | 1 |
| 10 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 |  | 1 |
| 11 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 |  | 1 |
| 12 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 |  | 1 |
| 13 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 |  | 2 |
| 14 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 |  | 2 |
| 15 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 |  | 2 |
| 16 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 |  | 2 |
| 17 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 |  | 2 |
| 18 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 |  | 2 |
| 19 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 |  | 2 |
| 20 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 |  | 2 |
| 21 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 |  | 2 |
| 22 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 |  | 2 |
| 23 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 |  | 2 |
| 24 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 2 |  | 2 |
| 25 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 |  | 3 |
| 26 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 |  | 3 |
| 27 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 |  | 3 |
| 28 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 |  | 3 |
| 29 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 |  | 3 |
| 30 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 |  | 3 |
| 31 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 |  | 3 |
| 32 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 |  | 3 |
| 33 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 |  | 3 |
| 34 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 |  | 3 |
| 35 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 3 |  | 3 |
| 36 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 1 |  | 4 |
| 37 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 2 |  | 4 |
| 38 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 3 |  | 4 |
| 39 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 4 |  | 4 |
| 40 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 5 |  | 4 |
| 41 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 6 |  | 4 |
| 42 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 7 |  | 4 |
| 43 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 8 |  | 4 |
| 44 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 9 |  | 4 |
| 45 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 10 |  | 4 |
| 46 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 11 |  | 4 |
| 47 | ABC-123 | PC | ABC-123-0001 | PCSEQ | 12 |  | 4 |
| 48 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 |  | 4 |
| 49 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 5 |  | 4 |
| 50 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 |  | 4 |
| 51 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 7 |  | 4 |

**PC-PP Conclusions**
Relating the datasets (as described in Section 8, Representing Relationships and Data) is the simplest method; however, all time-point concentrations in PC must be used to calculate all parameters for all subjects. If datasets cannot be related, then individual subject records must be related. In either case, the values of PCGRPID and PPGRPID must take into account multiple analytes and multiple reference time points, if they exist.

Method A is clearly the most efficient in terms of having the least number of RELREC records, but it does require the assignment of --GRPID values (which are optional) in both the PC and PP datasets. Method D, in contrast, does not require the assignment of --GRPID values, relying instead on the required --SEQ values in both datasets to relate the records. Although Method D results in the largest number of RELREC records compared to the other methods, it may be the easiest to implement consistently across the range of complexities shown in the examples. Two additional methods, methods B and C, are also shown for Examples 1-3. They represent hybrid approaches, using --GRPID values in only 1 dataset (PP and PC, respectively) and --SEQ values for the other. These methods are best suited for sponsors who want to minimize the number of RELREC records while not having to assign --GRPID values in both domains. Methods B and C would not be ideal, however, if one expected complex scenarios as shown in Example 4.

Note that an attempt has been made to approximate real pharmacokinetic data; however, the example values are not intended to reflect data used for actual analysis. When certain time-point concentrations have been omitted from PP calculations in Examples 2-4, the actual parameter values in the PP dataset have not been recalculated from those in Example 1 to reflect those omissions.

**PC-PP – Suggestions for Implementing RELREC in the Submission of PK Data**
Determine which of the scenarios best reflects how PP data are related to PC data. Questions that should be considered include:
1. Do all parameters for each PK profile use all concentrations for all subjects? If so, create a PPGRPID value for all PP records and a PCGRPID value for all PC records for each profile for each subject, analyte, and reference time point. Decide whether to relate datasets or records. If choosing the latter, create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.
2. Do all parameters use the same concentrations, although maybe not all of them (Example 2)? If so, create a single PPGRPID value for all PP records, and 2 PCGRPID values for the PC records: a PCGRPID value for ones that were used and a PCGRPID value for those that were not used. Create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.
3. Do any parameters use the same concentrations, but not as consistently as shown in Examples 1 and 2? If so, refer to Example 3. Assign a GRPID value to the PP records that use the same concentrations. More than 1 PPGRPID value may be necessary. Assign as many PCGRPID values in the PC domain as needed to group these records. Create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.
4. If none of the above applies, or the data become difficult to group, then start with Example 4, and decide which RELREC method would be easiest to implement and represent.

---

