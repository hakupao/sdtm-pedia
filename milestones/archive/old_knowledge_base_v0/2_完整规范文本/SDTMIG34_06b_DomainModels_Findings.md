# SDTMIG v3.4 --- Domain Models: Findings — Part 2

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 2/8 — 6.3.5.1-6.3.5.3: Specimen-based (Generic, BS, CP)
> **Original:** `SDTMIG34_06_DomainModels_Findings.md`
> **Related:** `SDTMIG34_06a_DomainModels_Findings.md`, `SDTMIG34_06c_DomainModels_Findings.md`, `SDTMIG34_06d_DomainModels_Findings.md`, `SDTMIG34_06e_DomainModels_Findings.md`, `SDTMIG34_06f_DomainModels_Findings.md`, `SDTMIG34_06g_DomainModels_Findings.md`, `SDTMIG34_06h_DomainModels_Findings.md`

---

### 6.3.5 Specimen-based Findings Domains

Individual domains (e.g., IS, LB, MB) for laboratory measurements, tests, or examinations performed on collected biological specimens (e.g., blood, urine, tumor tissue) are grouped together in this section. This grouping is not meant to imply that there is a single laboratory domain for all test methodologies. Additional laboratory domains are expected to be added in future versions.

#### 6.3.5.1 Generic Specimen-based Lab Findings Domain Specification

This section describes variables commonly used in specimen-based laboratory domains (e.g., IS, LB, MB/MS, MI, PC/PP).


- The SDTMIG includes several domains for representing clinical pathology laboratory measurements, tests, and examinations supporting safety and/or efficacy analyses. Each domain is defined to group measures of a common topic (e.g., microbiology susceptibility, microscopic findings, pharmacokinetic concentrations).
- In the generic lab domain specification table that follows, "--" is used as a placeholder. In each individual laboratory findings domain specification, it is replaced by the appropriate domain code.
- The variables in the generic domain specification table include required, expected, and permissible variables typically used across specimen-based laboratory findings domains to uniquely describe a measurement, test, or examination of a biological specimen.
  - Individual domains include additional variables with specific Controlled Terminology codelists and domain-specific Core values.
  - The Findings general observation class includes additional permissible variables that may be added when representing specimen-based laboratory findings.
  - Permissible identifier and timing variables may be added to represent details (e.g., identifiers to describe related records, planned time points, actual timing).

--.xpt, Generic Specimen-Based Laboratory Findings — Findings, Version 1.0. One record per finding per visit per subject, Tabulation.

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | -- |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | --SEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | --GRPID | Group ID | Char | Identifier | Perm |  |
| 6 | --REFID | Reference ID | Char | Identifier | Perm |  |
| 7 | --TESTCD | Short Name of Measurement, Test or Exam | Char | Topic | Req | * |
| 8 | --TEST | Name of Measurement, Test or Exam | Char | Synonym Qualifier | Req | * |
| 9 | --CAT | Category | Char | Grouping Qualifier | Perm | * |
| 10 | --SCAT | Subcategory | Char | Grouping Qualifier | Perm | * |
| 11 | --ORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 12 | --ORRESU | Original Units | Char | Variable Qualifier | Perm | * |
| 13 | --LLOD | Lower Limit of Detection | Char | Variable Qualifier | Perm |  |
| 14 | --STRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |
| 15 | --STRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 16 | --STRESU | Standard Units | Char | Variable Qualifier | Perm | * |
| 17 | --STAT | Completion Status | Char | Record Qualifier | Perm | * |
| 18 | --REASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 19 | --NAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm | * |
| 20 | --SPEC | Specimen Material Type | Char | Record Qualifier | Perm | * |
| 21 | --METHOD | Method of Test or Examination | Char | Record Qualifier | Perm | * |
| 22 | --LOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | * |
| 23 | --LLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Perm |  |
| 24 | --ULOQ | Upper Limit of Quantitation | Num | Variable Qualifier | Perm |  |
| 25 | VISITNUM | Visit Number | Num | Timing | Perm |  |
| 26 | VISIT | Visit Name | Char | Timing | Perm |  |
| 27 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 28 | --DTC | Date/Time of Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| 29 | --DY | Study Day of Collection | Num | Timing | Perm |  |

> **Note:** An asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

#### 6.3.5.2 Biospecimen Findings (BS)

BE, BS, and RELSPEC domain specifications, assumptions, and examples were copied and minimally updated from the provisional SDTMIG-PGx, published 2015-05-26. This was done in preparation for the retirement of the SDTMIG-PGx upon publication of SDTMIG v3.4. These domains are currently under extensive revision for inclusion in a future SDTMIG publication, after v3.4.

##### BS – Description/Overview
A findings domain that contains data related to biospecimen characteristics.

##### BS – Specification
bs.xpt, Biospecimen Findings — Findings. One record per measurement per biospecimen identifier per subject, Tabulation.

**Structure:** One record per measurement per biospecimen identifier per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | BS |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |
| 5 | BSSEQ | Sequence Number | Num | Identifier | Req |  |
| 6 | BSGRPID | Group ID | Char | Identifier | Perm |  |
| 7 | BSREFID | Reference ID | Char | Identifier | Exp |  |
| 8 | BSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 9 | BSTESTCD | Biospecimen Test Short Name | Char | Topic | Req | C124300 |
| 10 | BSTEST | Biospecimen Test Name | Char | Synonym Qualifier | Req | C124299 |
| 11 | BSCAT | Category for Biospecimen Test | Char | Grouping Qualifier | Exp |  |
| 12 | BSSCAT | Subcategory for Biospecimen Test | Char | Grouping Qualifier | Perm |  |
| 13 | BSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 14 | BSORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |
| 15 | BSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 16 | BSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |
| 17 | BSSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |
| 18 | BSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 19 | BSREASND | Reason Test Not Done | Char | Record Qualifier | Perm |  |
| 20 | BSNAM | Vendor Name | Char | Record Qualifier | Perm |  |
| 21 | BSSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734; C111114 |
| 22 | BSANTREG | Anatomical Region of Specimen | Char | Variable Qualifier | Perm |  |
| 23 | BSSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| 24 | BSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 25 | BSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 26 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 27 | VISIT | Visit Name | Char | Timing | Perm |  |
| 28 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 29 | BSDTC | Date/Time of Specimen Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 30 | BSDY | Study Day of Specimen Collection | Num | Timing | Perm |  |
| 31 | BSTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 32 | BSTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 33 | BSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 34 | BSTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 35 | BSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **SPDEVID**: Sponsor-defined identifier for a device.
- **BSSEQ**: Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.
- **BSGRPID**: Optional group identifier, used to link together a block of related records within a subject in a domain.
- **BSREFID**: Internal or external identifier such as lab specimen ID.
- **BSSPID**: Sponsor-defined identifier.
- **BSTESTCD**: Short character value for BSTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Examples: VOLUME, RIN.
- **BSTEST**: Long name for BSTESTCD. Examples: Volume, RNA Integrity Number.
- **BSCAT**: Used to define a category of topic-variable values. Example: MEASUREMENT, QUALITY.
- **BSSCAT**: Used to define a further categorization of BSCAT values.
- **BSORRES**: Result of the measurement or finding as originally received or collected.
- **BSORRESU**: Unit for BSORRES. Examples: mg, mL.
- **BSSTRESC**: Contains the result value for all findings, copied or derived from BSORRES in a standard format or standard units. BSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in BSSTRESN.
- **BSSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from BSSTRESC. BSSTRESN should store all numeric test results or findings.
- **BSSTRESU**: Standardized unit used for BSSTRESC and BSSTRESN.
- **BSSTAT**: Used to indicate that a test was not done, or was attempted but did not generate a result. Should be null or have a value of NOT DONE.
- **BSREASND**: Reason not done. Used in conjunction with BSSTAT when value is NOT DONE.
- **BSNAM**: Name or identifier of the vendor (e.g., laboratory) that provided the test results.
- **BSSPEC**: Defines the type of specimen used for a measurement. Examples: SERUM, PLASMA, URINE, SOFT TISSUE.
- **BSANTREG**: Defines the specific anatomical or biological region of a tissue, organ specimen or the region from which the specimen is obtained, as defined in the protocol, such as a section or part of what is described in the BSSPEC variable. Examples: CORTEX, MEDULLA, MUCOSA.
- **BSSPCCND**: Defines the condition of the specimen. Examples: HEMOLYZED, ICTERIC, LIPEMIC.
- **BSMETHOD**: Method of the test or examination. Examples: SPECTROPHOTOMETRY, ELECTROPHORESIS.
- **BSBLFL**: Indicator used to identify a baseline value.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter.
- **VISITDY**: Planned study day of VISIT. Should be an integer.
- **BSDTC**: Date and time of specimen collection.
- **BSDY**: Study day of specimen collection relative to the sponsor-defined RFSTDTC.
- **BSTPT**: Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See BSTPTNUM and BSTPTREF.
- **BSTPTNUM**: Numerical version of BSTPT used in sorting.
- **BSELTM**: Elapsed time relative to a planned fixed reference (BSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration.
- **BSTPTREF**: Name of the fixed reference point referred to by BSELTM, BSTPTNUM, and BSTPT. Examples: PREVIOUS DOSE, PREVIOUS MEAL.
- **BSRFTDTC**: Date/time for a fixed reference time point defined by BSTPTREF.


##### BS – Assumptions
1. The BS domain is used to store findings related to specimen handling and specimen characteristics such as type, amount, or size. BS is not restricted to PGx-related specimens.
2. For biospecimens of genetic material, BSSPEC values are drawn from the GENSMP (C111114) codelist.
3. Non-genetic BSSPEC values are drawn from the SPEC (C77529) codelist, which is part the SEND terminology listing. BSANTREG is used to further define BSSPEC when it is desirable to identify a specific region within an organ.
4. To adapt BS for use with the SDTMIG, use the SPECTYPE (C78734) codelist in BSSPEC, add --LOC, --LAT, --DIR, and --PORTOT as applicable, and remove BSANTREG. Values that would otherwise have gone in BSANTREG may be placed in a supplemental qualifier that is almost identical to that variable, but which further qualifies BSLOC instead of BSSPEC.
5. The following variables generally would not be used in BS: --POS, --ORNLO, --ORNHI, --STRNLO, --STNRHI, --STNRC, --NRIND, --LEAD, --CSTATE, --ACPTFL, --FAST, --TOX, --TOXGR, --SEV, --DTHREL.

##### BS – Examples

**Example 1**
This example shows data about RNA integrity. The data collected focus on the quality of the RNA sample being collected. It has been shown that improper storage or isolation methods might compromise the usability of a sample.

**Rows 1-2:** The A260/A280 and A260/A230 ratios are used to determine the purity of the RNA sample. Any ratios outside of the accepted values may indicate contamination with protein or reagents used during the extraction process.
**Row 3:** The amounts of both 28S and 18S ribosomal RNA are measured and then a ratio is calculated. Because values in --TESTCD cannot begin with a number, the test code has been prefixed with an "I" for integrity.
**Row 4:** The RNA integrity number is a quality measurement calculated using a special algorithm and used to determine the usability of the RNA sample.

*bs.xpt*

| Row | STUDYID | DOMAIN | USUBJID | BSSEQ | BSREFID | BSTESTCD | BSTEST | BSCAT | BSORRES | BSSTRESC | BSSTRESN | BSXFN | BSNAM | BSSPEC | BSMETHOD | BSRUNID | VISIT | VISITNUM | VISITDY | BSDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A12345 | BS | 43871 | 1 | 1148.26704 | A260A230 | A260/A230 | QUALITY CONTROL | 2.05 | 2.05 | 2.05 | 2.16.090.1.135764.3.4:7280912 | Deluxe Central Labs | rRNA | SPECTROPHOTOMETRY | 1000450001 | Baseline | 1 | 1 | 2005-03-21T11:28:17 |
| 2 | A12345 | BS | 43871 | 2 | 1148.26704 | A260A280 | A260/A280 | QUALITY CONTROL | 2 | 2 | 2 | 2.16.090.1.135764.3.4:7280912 | Deluxe Central Labs | rRNA | SPECTROPHOTOMETRY | 1000450001 | Baseline | 1 | 1 | 2005-03-21T11:28:17 |
| 3 | A12345 | BS | 43871 | 3 | 1148.26704 | I28S18S | 28S/18S | QUALITY CONTROL | 1.2 | 1.2 | 1.2 | 2.16.090.1.135764.3.4:7280912 | Deluxe Central Labs | rRNA | ELECTROPHORESIS | 1000450001 | Baseline | 1 | 1 | 2005-03-21T11:28:17 |
| 4 | A12345 | BS | 43871 | 4 | 1148.26704 | RIN | RNA INTEGRITY NUMBER | QUALITY CONTROL | 9.5 | 9.5 | 9.5 | 2.16.090.1.135764.3.4:7280912 | Deluxe Central Labs | rRNA | ELECTROPHORESIS | 1000450001 | Baseline | 1 | 1 | 2005-03-21T11:28:17 |

#### 6.3.5.3 Cell Phenotype Findings (CP)

##### CP – Description/Overview
A findings domain that contains data related to the characterization of cell phenotype, lineage, and function based on expression of specific markers in single cell or particle suspensions.
The CP domain is modeled for use with disseminated tissue specimens (e.g., blood and other body fluids, bone marrow aspirates) and cell suspensions, and is not currently modeled for evaluations of solid tissue specimens. The domain is intended to support tests associated with a cell phenotyping component based on the use of markers and is not intended for tests that are not associated with marker-based phenotyping, which are more appropriate to include in another domain (e.g., Immunogenicity Specimen Assessments (IS), Laboratory Test Results (LB), Microscopic Findings (MI)). The CP domain is not intended to supplant use of the LB domain for routine lab hematology (e.g., blood cell differentials), nor is it intended for findings originating from microscopic assessment of cells, including those employing immunohistochemical (IHC) techniques.
The modeled use cases include measurement of
- cell populations identified, classified, and/or otherwise characterized based on the differential expression of phenotypic and/or cell state/function markers, as determined for both normal and abnormal cell populations;
- the level of marker expression;
- substances interacting with (e.g., binding to) a marker which is a target of interest (not limited to a pharmacologic target); and
- other cell properties based on characterization of expression marker(s) and/or substances that interact with the marker(s).

To provide the flexibility needed to report cell marker expression data, which can range widely in complexity, several new SDTM variables have been created. Most of the new variables are permissible, and are available as needed to fully define a test and/or to prevent ambiguity that could lead to misunderstanding or difficulty in interpreting the data. New variables include --SBMRKS (Sublineage Marker String), -- CELSTA (Cell State), --CSMRKS (Cell State Marker String), --TSTCND (Test Condition), --CNDAGT (Test Condition Agent), --BNDAGT (Binding Agent), --ABCLID (Antibody Clone Identifier), --MRKSTR (Marker String), --GATE (Gate Name), --GATEDEF (Gate Definition), --SPTSTD (Sponsor Test Description), --TSTPNL (Test Panel), --RESSCL (Result Scale), and --RESTYP (Result Type). Definitions and appropriate use of these variables are provided in the Specification and Assumptions sections of this guidance and are illustrated in the examples for selected use cases.

Data submitters should work closely with laboratory data providers, analysts, and data receivers/users to determine the appropriate set of permissible variables to include in a dataset (i.e., the variables needed to fully document tests and associated findings for a particular use case).

Sponsors that previously chose to submit cell phenotyping data in the LB domain, where LBTEST was often used to populate cell marker information (e.g., "CD4" to indicate helper T lymphocytes), should note that the new variable --MRKSTR should be used to house the full marker string information used to define the test in terms of markers; the --TEST variable is reserved for the name of the cell population. Several of the new variables (i.e., --SBMRKS, --CELSTA, -- CSMRKS) are used to further subdivide the population reported in --TEST into more granular unnamed subpopulations based on 1 or more additional markers.
This approach provides a more easily understood test name in the --TEST variable and enables development of controlled terminology for --TEST and -- TESTCD. The goal is to standardize, where possible, cell phenotype test names across studies so that it will be easier for users to understand and interpret the data (e.g., when different marker sets are used across labs to define the same cell population). This approach also enhances the ability to integrate and compare data across studies in a practicable manner that (in addition to being less error-prone) preserves the often subtle differences between tests, which are essential for determining whether tests are truly comparable.

Used in accordance with this guidance, the complete marker sting information provided in the --MRKSTR variable reflects the operational (i.e., laboratory- specific) definition of the test measurement. Together with the gating information provided in the --GATE and --GATEDEF variables, --MRKSTR values help to ensure that proper groupings and comparisons are made across tests by preserving nuanced details that may affect the interpretation of test results. To facilitate these objectives and to enable accurate cross-study comparisons and data-mining efforts, it is recommended that --MRKSTR values conform as closely as possible to marker string formatting principles presented in the CP Assumptions section.

##### CP – Specification

cp.xpt, Cell Phenotype Findings — Findings. One record per test per specimen per timepoint per visit per subject, Tabulation.

**Structure:** One record per test per specimen per timepoint per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | CP |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | CPSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | CPGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | CPREFID | Reference ID | Char | Identifier | Perm |  |
| 7 | CPSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | CPLNKID | Link ID | Char | Identifier | Perm |  |
| 9 | CPLNKGRP | Link Group ID | Char | Identifier | Perm |  |
| 10 | CPTESTCD | Test or Examination Short Name | Char | Topic | Req | C181173 |
| 11 | CPTEST | Name of Measurement, Test or Examination | Char | Synonym Qualifier | Req | C181174 |
| 12 | CPSBMRKS | Sublineage Marker String | Char | Variable Qualifier | Perm |  |
| 13 | CPCELSTA | Cell State | Char | Variable Qualifier | Perm | C181172 |
| 14 | CPCSMRKS | Cell State Marker String | Char | Variable Qualifier | Perm |  |
| 15 | CPTSTCND | Test Condition | Char | Variable Qualifier | Perm | C181175 |
| 16 | CPCNDAGT | Test Condition Agent | Char | Record Qualifier | Perm |  |
| 17 | CPBDAGNT | Binding Agent | Char | Record Qualifier | Perm |  |
| 18 | CPABCLID | Antibody Clone Identifier | Char | Record Qualifier | Perm |  |
| 19 | CPMRKSTR | Marker String | Char | Record Qualifier | Exp |  |
| 20 | CPGATE | Gate | Char | Record Qualifier | Perm |  |
| 21 | CPGATDEF | Gate Definition | Char | Record Qualifier | Perm |  |
| 22 | CPSPTSTD | Sponsor Test Description | Char | Record Qualifier | Perm |  |
| 23 | CPCAT | Category | Char | Grouping Qualifier | Perm | C181171 |
| 24 | CPSCAT | Subcategory | Char | Grouping Qualifier | Perm |  |
| 25 | CPTSTPNL | Test Panel | Char | Grouping Qualifier | Perm |  |
| 26 | CPORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 27 | CPORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 28 | CPRESSCL | Result Scale | Char | Record Qualifier | Perm | C177910 |
| 29 | CPRESTYP | Result Type | Char | Record Qualifier | Perm | C179588 |
| 30 | CPCOLSRT | Collected Summary Result Type | Char | Record Qualifier | Perm | C177908 |
| 31 | CPORNRLO | Reference Range Lower Limit in Orig Unit | Char | Variable Qualifier | Perm |  |
| 32 | CPORNRHI | Reference Range Upper Limit in Orig Unit | Char | Variable Qualifier | Perm |  |
| 33 | CPSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |
| 34 | CPSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 35 | CPSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 36 | CPSTNRLO | Reference Range Lower Limit-Std Units | Num | Variable Qualifier | Perm |  |
| 37 | CPSTNRHI | Reference Range Upper Limit-Std Units | Num | Variable Qualifier | Perm |  |
| 38 | CPNRIND | Reference Range Indicator | Char | Variable Qualifier | Perm | C78736 |
| 39 | CPSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 40 | CPREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 41 | CPNAM | Vendor Name | Char | Record Qualifier | Perm |  |
| 42 | CPLOINC | LOINC Code | Char | Synonym Qualifier | Perm | LOINC |
| 43 | CPSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734 |
| 44 | CPSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| 45 | CPMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 46 | CPANMETH | Analysis Method | Char | Record Qualifier | Perm |  |
| 47 | CPLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| 48 | CPBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 49 | CPDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 50 | CPCLSIG | Clinically Significant, Collected | Char | Record Qualifier | Perm | C66742 |
| 51 | VISITNUM | Visit Number | Num | Timing | Perm |  |
| 52 | VISIT | Visit Name | Char | Timing | Perm |  |
| 53 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 54 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 55 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 56 | CPDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 57 | CPDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |
| 58 | CPTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 59 | CPTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 60 | CPELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 61 | CPTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 62 | CPRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **CPSEQ**: Sequence number to ensure uniqueness of subject records within a domain. May be any valid number.
- **CPGRPID**: Used to tie together a block of related records in a single domain for a subject.
- **CPREFID**: Internal or external specimen identifier.
- **CPSPID**: Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the lab page.
- **CPLNKID**: Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.
- **CPLNKGRP**: Identifier used to link related records across domains. This will usually be a many-to-one relationship.
- **CPTESTCD**: Short name of the measurement, test, or examination described in CPTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in CPTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). CPTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MONO", "MNS".
- **CPTEST**: Long name for CPTESTCD. For cell phenotyping, the name (often abbreviated) of the cell population, as it is generally accepted by the scientific community, is populated (rather than a colloquial designation based on a primary marker, e.g., TLym Help rather than CD4). When the test is for a sublineage which can only be identified by specifying additional markers (i.e., has not been given a name) or which is further restricted to a subpopulation based on a particular cell state (e.g., activated, proliferating, apoptotic), the Sublineage Marker String (CPSBMRKS), Cell State (CPCELSTA), and Cell State Marker String (CPCSMRKS) variables are additionally populated and the value in CPTEST is suffixed with "Sub" to denote that it is a subset of the population identified in CPTEST (e.g., Monocytes Sub).; The value in CPTEST cannot be longer than 40 characters.
- **CPSBMRKS**: Used to further subset the cell population identified in CPTEST based on the use of additional marker(s) that define a sublineage. The value in CPSBMRKS is used in combination with values in CPTEST and CPCELSTA to fully describe the cell population being measured. As such, it is an essential component of the full test name.; For example, three unnamed sublineages of monocytes have been identified as: CCR2+CD16-, CCR2-CD16+, and CCR2+CD16+. Whereas the entire monocyte cell population can be defined as CD14+ cells, the additional CCR2 and CD16 markers are used to differentiate one sublineage from another. As none of these sublineages have been given names, they are only known by the CCR2 and CD16 marker combinations. By associating the CPTEST value of "Monocytes Sub" with, for example, a value of "CCR2+CD16-" in CPSBMRKS, the full test is defined to be the CCR2+CD16- monocyte subpopulation.
- **CPCELSTA**: A textual description of a subset of the cell population identified in CPTEST based on a particular functional and/or biological state (e.g., "ACTIVATED", "PROLIFERATING", "SENESCENT"). When populated, the values in CPCELSTA and CPSMRKS, in combination with the values in CPTEST and CPSBMRKS, fully describe the cell population being measured.
- **CPCSMRKS**: Identifies the marker(s) or indicator(s) used to define the cell state (i.e., the value in CPCELSTA).; For example, when Ki67 expression is used to determine that a cell population is in a proliferating state (i.e., CPCELSTA value="PROLIFERATING"), the value "Ki67+" in CPCSMRKS indicates that positive expression of Ki67 was used to define the population as proliferating. Similarly, a value of "Ki67-" in CPCSMRKS would indicate that lack of expression of Ki67 defined the "NON-PROLIFERATING" cell state in CPCELSTA. The CPCSMRKS value is useful for quickly determining which marker(s) were used to classify (i.e., operationally define) a cell population based on a functional/biological state.
- **CPTSTCND**: Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed. --TSTCND is generally used to distinguish between two or more records where the same assay is performed under varying (as opposed to fixed) conditions, usually for the purpose of making a comparison. For example, when the same assay (identified in --TEST) is performed under stimulated and non-stimulated conditions, the --TSTCND variable is used distinguish between the records.
- **CPCNDAGT**: The textual description of the agent, if applicable, used to impose the condition identified in CPTSTCND. For example, records might be produced for the same assay run under stimulating (CPTSTCND value = "STIMULATED") conditions produced by different stimulating agents (e.g., phorbol myristate acetate, concanavalin A, PHA-P, TNF-alpha, Ionomycin, candida antigen).
- **CPBDAGNT**: The textual description of the agent that is binding to the entity in the CPTEST variable. The CPBDAGNT variable is used to indicate that there is a binding relationship between the entities in the CPTEST and CPBDAGNT variables, regardless of direction.; The binding agent may be, but is not limited to, a test article; a portion of a test article; a substance related to a test article; an endogenous molecule; an allergen; an infectious agent; or a reagent (e.g., primary antibody) that confers the binding specificity for the measurement defined in CPTEST when it is needed to uniquely identify the test.
- **CPABCLID**: Identifies the antibody clone (e.g., supplier-provided catalog name) used to confer specificity for the binding agent specified in CPBDAGNT.
- **CPMRKSTR**: The text string identifying the full set of markers/indicators used by the laboratory to operationally define the complete test based on the combination of CPTEST, CPSBMRKS, and CPCELSTA. Because laboratories often use different markers/indicators to identify a cell population, the relationship between a named cell population in CPTEST (as combined with CPSBMRKS and CPCELSTA values) and the set of markers used to identify that population is many-to-one. To ensure nuances important for accurately interpreting the data are accounted for and which arise from the use of different sets of markers, it is necessary to operationally define the test in terms of the complete set of markers/indicators used to perform that test.
- **CPGATE**: The sponsor-defined name assigned to a gate. Gates are electronic (i.e., a device setting or software-defined) boundaries set by a user to virtually parse a specimen into discrete populations based on a set of defined characteristics (e.g., presence, absence, or intensity of expression of various markers; physical size; internal complexity or granularity). Gates are used to constrain data collection or analysis to a specific cell population or region of interest within the specimen.
- **CPGATDEF**: The text string identifying the set of parameters and the order in which they are applied to define the gating strategy. In practice, a series of 2-dimensional sub-gates based on different cell characteristics (i.e., markers/indicators/physical properties) are most often combined until the cell population of interest is sufficiently resolved (i.e., electronically isolated) from other cell populations contained within the specimen.; For complex analyses, differences in gating strategies can produce subtle differences in results obtained for a test. To ensure nuances important for accurately interpreting the data are accounted for and which arise from the use of different gating strategies, it is often necessary to qualify the test in terms of the gating strategy. For some purposes, however, and at the discretion of the sponsor, only the ultimate or penultimate gate is identified. When specifying the gating strategy in CPGATDEF, each sub-gate should be listed in the order it was applied and separated from the next sub-gate using the pipe/vertical line ("|") character.
- **CPSPTSTD**: Sponsor's description of a test. The variable is intended to contain highly structured test description metadata used by a sponsor to unambiguously define (label) a test. Such values generally reside in a sponsor/laboratory test metadata repository. CPSPTSTD is not intended for unstructured (spontaneous) free text.; An example of appropriate usage is when it is necessary to include identifying information for a target cell population on which a test is conducted when the target population is not part of the test name, e.g., tests for quantitative expression of a particular marker on a specific cell population.
- **CPCAT**: Used to define a category of topic-variable values across subjects. Examples: "IMMUNOPHENOTYPING", "CELL FUNCTION", "TARGET ENGAGEMENT".
- **CPSCAT**: A further categorization of CPCAT.
- **CPTSTPNL**: Sponsor-defined textual description used to group tests run together as part of a test panel. Can be used with --GRPID to ensure that relationships between associated tests are accurately identified.
- **CPORRES**: Result of the measurement or finding as originally received or collected.
- **CPORRESU**: Original units in which the data were collected. The unit for CPORRES. Examples: "10^6/L", "%", "MESF".
- **CPRESSCL**: Classifies the scale of the original result value with respect to whether the result is quantitative, ordinal, nominal, or narrative.
- **CPRESTYP**: Classifies the kind of result (i.e., property type) originally reported for the test. Examples: "NUMBER CONCENTRATION", "NUMBER FRACTION", "RATIO".
- **CPCOLSRT**: Used to indicate the type of collected summary result. This includes source summary results collected on a CRF or provided by an external vendor (e.g., central lab). If the summary result is derived using individual source data records, this summary result should be represented in ADaM. If a sponsor has both a collected summary result and a derived summary result, the collected summary result should be represented in SDTM and the derived summary result should be represented in ADaM.
- **CPORNRLO**: Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results.
- **CPORNRHI**: Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results.
- **CPSTRESC**: Contains the result value for all findings, copied or derived from CPORRES in a standard format or in standard units. CPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in CPSTRESN.
- **CPSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from CPSTRESC. CPSTRESN should store all numeric test results or findings.
- **CPSTRESU**: Standardized unit used for CPSTRESC or CPSTRESN.
- **CPSTNRLO**: Lower end of reference range for continuous measurements for CPSTRESC/CPSTRESN in standardized units. Should be populated only for continuous results.
- **CPSTNRHI**: Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results.
- **CPNRIND**: Indicates where the value falls with respect to reference range defined by CPORNRLO and CPORNRHI, CPSTNRLO and CPSTNRHI, or by CPSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether CPNRIND refers to the original or standard reference ranges and results. CPNRIND should not be used to indicate clinical significance.
- **CPSTAT**: Used to indicate that the test was not performed or that it was attempted but did not generate a result. Should be null if a result exists in CPORRES.
- **CPREASND**: Describes why a test was not performed, e.g., "BROKEN EQUIPMENT", "SUBJECT REFUSED", "SPECIMEN LOST". Used in conjunction with CPSTAT when value is "NOT DONE".
- **CPNAM**: The name or identifier of the laboratory that performed the test.
- **CPLOINC**: Code for the test from the LOINC code system. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the Define-XML external codelist attributes.
- **CPSPEC**: Defines the type of specimen used for a measurement. Examples: "BLOOD", "BONE MARROW".
- **CPSPCCND**: The physical state or quality of a specimen for an assessment. Example: "CLOTTED".
- **CPMETHOD**: Method of the test or examination. Example: "FLOW CYTOMETRY".
- **CPANMETH**: Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result.
- **CPLOBXFL**: Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **CPBLFL**: Indicator used to identify a baseline value. The value should be "Y" or null.
- **CPDRVFL**: Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or do not come from the CRF, or are not as originally received or collected are examples of records that might be derived for the submission datasets. If CPDRVFL = "Y", then CPORRES may be null, with CPSTRESC and (if numeric) CPSTRESN having the derived value.
- **CPCLSIG**: Used to indicate whether a collected observation is clinically significant based on judgement.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics. Should be an integer.
- **TAETORD**: Number that gives the planned order of the element within the arm.
- **EPOCH**: Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.
- **CPDTC**: Date/time of specimen collection represented in ISO 8601 character format.
- **CPDY**: Study day of specimen collection, measured in integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC value in Demographics.
- **CPTPT**: Text description of time when a specimen is to be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (i.e., to the value in CPTPTREF). Example: "1 hour post".
- **CPTPTNUM**: Numerical version of CPTPT to aid in sorting. When CPTPT is represented as an elapsed time relative to a fixed reference point (i.e., to the value in CPTPTREF), the values in CPTPTNUM should be assigned in ascending order relative to the value in CPTPTREF. For example, records for time points where CPTPT = "5 minutes post", 1 hour post", and "4 hours post" could be represented in CPTPTNUM as "1", "2", and "3", which maintains the order between CPTPT and CPTPTNUM with respect to the fixed time point reference in CPTPTREF.
- **CPELTM**: Planned elapsed time relative to the planned fixed reference value in CPTPTREF, represented in ISO 8601 duration format. Examples: "-PT15M" to represent 15 minutes prior to the reference time point indicated by CPTPTREF, "T8H" to represent 8 hours after the reference time point represented by CPTPTREF.
- **CPTPTREF**: Descriptive name of the fixed reference point referred to by CPTPT, CPTPTNUM, and CPELTM. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **CPRFTDTC**: Date/time for a fixed reference time point defined by CPTPTREF.

##### CP – Assumptions

1. The Cell Phenotype domain captures cell phenotyping and related data based on cell expression markers and other indicators (e.g., stains/dyes) in disseminated tissue specimens and cell suspensions.
2. The CP domain is only used for tests which include a phenotyping component that relies on using cell markers to identify a specific population of cells (e.g., quantitative cell phenotyping), or on which the test is conducted (e.g., quantitative single marker expression, target/receptor occupancy). For example, a test which measures gamma-interferon expression in helper T lymphocytes defined as the CD45+CD3+CD4+CD8- population is an appropriate test for including in CP, whereas a test which measures gamma interferon secretion in an undefined "PBMC" (peripheral blood mononuclear cell) population is not appropriate.
3. A value which is calculated and reported by a lab according to its procedures is considered collected rather than derived; the Derived Flag (CPDRVFL) should be null for these results.
4. CPCELSTA is used in conjunction with CPSCMRKS. When CPCELSTA is populated, CPSCMRKS must also be populated. Conversely, when CPSCMRKS is populated, CPCELSTA must be populated.
5. The combination of values in CPTEST, CPSBMRKS, CPCELSTA, and CPCSMRKS are used to uniquely identify a test. When 1 or more of the variables CPSBMRKS, CPCELSTA, or CPCSMRKS are populated, the Test Name (CPTEST) must be populated with the test name variant containing the "Sub" suffix to indicate that the finding/result pertains to a subpopulation of the cell type named in CPTEST.
6. Populating the CPTEST and CPMRKSTR variables: The general structure of CPTEST depends on the use case (e.g., immunophenotyping, quantitative marker expression, target/receptor occupancy), which is generally conveyed by the CPCAT and/or CPSCAT value(s). Currently, CP supports the following use cases for which guidance on CPTEST and CPMRKSTR values are given:
    a. Immunophenotyping
        i. CPTEST is populated with the name of the cell type being measured, not with the set of markers used to define the cell type.
        ii. It is expected that CPMRKSTR is populated, and that it contains the entire set of markers used to define the test, including those that are also present in CPSBMRKS and/or CPCSMRKS.
        iii. Marker strings follow, as closely as possible, formatting recommendations presented in assumption 8.
    b. Quantitative single-marker expression
        i. CPTEST begins with the identity of the marker (e.g., CD99), followed by the word "Expression" (e.g., "CD99 Expression").
        ii. It is expected that CPMRKSTR is populated, and that it starts by identifying the marker being quantified (e.g. "CD99"). This is followed by a delimiter (described below) and then the entire marker string used to define the cell population on which the marker is measured, including the marker being quantified, since it also defines the cell population.
        iii. The general form of the delimiter used to separate the marker being quantified from the cell population on which it is measured is "<space>xxxx<space>", where "xxxx" represents a character string used as delimiting text. It is recommended that the delimiting text is the abbreviation for the unit of measure used to report the level of expression of the quantified marker (e.g., "MESF", "MdFI"). An example which follows this guidance is: CPTEST = "CD99 Expression" and CPMRKSTR = "CD99 MESF CD45+CD3-CD19+CD99+", where "MESF" is the text delimiter and is followed by the entire marker string defining the cell population on which CD99 was measured, which includes the CD99 marker itself.
        iv. Marker strings follow, as closely as possible, formatting recommendations presented in assumption 8.
    c. Other use cases (e.g., target/receptor occupancy), refer to the examples section and to published Controlled Terminology supporting CP. In the case of target/receptor occupancy a more generalized test value is populated into CPTEST (e.g., "Total Bound") and the identity of the target/receptor is included in another variable, such as CPBNDAGT and/or CPTSTPNL (refer to examples). CDISC will continue to develop examples for other use cases as they are identified and modeled.
7. Specifying viability:
    a. Because the majority of cell phenotyping tests of interest are for viable cells, the word "Viable" is not generally included in the test name (CPTEST) and usually does not need to be explicitly stated in CPCELSTA. Because populating CPCELSTA and CSMRKS with viability information necessitates appending the "Sub" suffix to the value in CPTEST (assumption 5), it is recommended that CPCELSTA and CPCSMRKS generally not be used unless a selective viability stain was included in the test in order to differentiate the record for viable cells from record(s) for cells in a different vital state. For example, when viable cells are being compared to apoptotic and/or non-viable cells, it is necessary to differentiate those records using CPCELSTA and CPCSMRKS. In such cases where CPCELSTA and CPCSMRKS are populated, the "Sub" suffix is appended to the value in CPTEST (assumption 5).
    b. Viability marker(s) used to define a test are included in the full marker string in CPMRKSTR regardless of whether the viability status is stated explicitly in CPCELSTA. Moreover, if viability is explicitly stated in CPGATE, marker(s) used to designate viability are included in CPGATDEF. For example, if the value in CPGATE is "Lymphocytes, Viable" and 7AAD- was used to define the viable state, 7AAD- is included in CPGATDEF, in addition to being included in the complete marker string in CPMRKSTR.
8. Recommended formatting of marker string variables CPMRKSTR, CPSBMRKS, and CPCSMRKS: The marker string variables provide critical information for defining a test. Although there are no current plans to control their values through CDISC Controlled Terminology codelists, adherence to the following formatting guidelines helps to preclude ambiguities that can lead to uncertainty in uniquely understanding a test and its associated result.
    a. Marker strings do not contain delimiting characters (e.g., ",", space, "/", "|") to separate individual markers within the string, nor do they contain punctuation (e.g., hyphens) within individual markers, as these can be confused with symbols used to designate levels of expression and/or make it difficult to distinguish between the individual markers that comprise the string. For example, although the scientific literature often uses "HLA-DR", this is represented in CP marker strings as "HLADR".
    b. Forward slash "/" is only used to separate the portion of the marker string defining a numerator from the portion defining a denominator.
    c. When referring to a marker using the cluster of differentiation (CD) designation, "CD" should be included as part of the marker reference. For example, a marker string for helper T lymphocytes comprising CD45, CD3, CD4, and CD8 markers would be "CD45+CD3+CD4+CD8-" (rather than "45+3+4+8-").
    d. The order of markers within a string is consistent across similar tests, generally proceeding in the order that defines the cell hierarchy from highest to lowest, followed by additional non-lineage-defining markers, and ending with cell state and viability markers. This order maintains alignment with how a test is identified using the ordered combination of CPTEST, CPSMRKS, and CPCELSTA. For example, a test for proliferating viable activated central memory helper T-lymphocytes would be operationally defined in CPMRKSTR as similar to "CD45+CD3+CD19-CD4+CD8-CD197+CD45RA-CD278+Ki67+7AAD-", where the order of markers in the string is "CD45" (leukocyte), "CD3+CD19-" (T lymphocyte), "CD4+CD8-" (helper), "CD197+CD45RA-" (central memory), "CD278+" (activated), "Ki67+" (proliferating), "7AAD-" (viable). Corresponding to this marker-based definition of the test, and using the appropriate Controlled Terminology terms, CPTEST is "TLym Help Cen Mem Sub", CPCELSTA is "ACTIVATED; PROLIFERATING", and CPCSMRKS is "CD278+Ki67+". If the sponsor also chose to include the viability status as a cell state in addition to the activation and proliferative states, CPCELSTA would be similar to "ACTIVATED; PROLIFERATING; VIABLE" and the corresponding CPCSMRKS value would be "CD278+Ki67+7AAD-". In this example, the named cell population in CPTEST has not been further divided into an unnamed sublineage based on additional sublineage markers; therefore, CPSBMRKS is null.
    e. Forward (FSC) and Side (SSC) light scatter: These parameters are generally used to perform initial gating to exclude debris non-singlets and are often reapplied to differentiate cell subpopulations in the "inclusion" gate. However, FSC and SSC are often not included in marker string definitions as it is generally taken for granted that they were used. In contrast, they are usually included in a descriptions of a gating strategy, and would generally be included in CPGATDEF when the full gating strategy is shown. Labs/sponsors may choose whether to include FSC and SSC parameters in CPMRKSTR. It is recommended to include them when they are needed to differentiate one test from another. For example, because there is no universal expression marker specific for lymphocytes, FSC and SSC are used to define the lymphocyte subpopulation within a CD45+ leukocyte population. A test of "Lymphocytes/Leukocytes" defined only in terms of CD45 expression would not make sense as it would be "CD45+/CD45+". In this case, it makes sense to define lymphocytes as "CD45+SSClo" so that the value in CPMRKSTR is "CD45+SSClo/CD45+".
    f. Indicating the expression level of individual markers included in a marker string: A variety of formats are used in the scientific literature for indicating the level of expression of a marker on or within a cell. For example, after identifying a marker such as CD4, its level of expression might be represented as 1 of the following:
        i. neg, min, or - to denote the absence or minimal expression (e.g., CD4neg, CD4min, CD4-)
        ii. pos or + to denote that the marker is expressed (e.g., CD4pos, CD4+)
        iii. high, hi, or ++ to denote that the marker is expressed at a very high level relative to simply being "positive" (e.g., CD4high, CD4hi, CD4++)
        iv. other formats (e.g., -/low, -/lo, low, lo, mid, -/+, +++)
    g. Because categories for expression levels are subjective in the sense that they are relative to one another, various formats often overlap, which can create ambiguities. Some degree of consistency in formats used to represent relative expression levels is warranted to mitigate ambiguity, at least to the extent that relative expression levels used to define cell lineages/sublineages are similar across studies and laboratories in order to enable comparisons. Five designations are recommended for use in SDTM datasets:
        i. "-" (the marker is not expressed; at times, the use of "-lo" may be justified to indicate that the marker is either not expressed or is present in a negligible amount)
        ii. "lo" (the marker is expressed at a low level)
        iii. "mid" (the marker is expressed somewhere between a low and "normal" positive level for that cell type)
        iv. "+" (the marker is expressed at a normal positive level for that cell type)
        v. "hi" (the marker is expressed at a distinctly higher level than in cells that are "+", such that they are distinguishable from the "+" population and define their own subpopulation)
        vi. Although these designations are expected to be useful in the majority of cases, it is recognized that designations not listed here may be more appropriate in some cases. The data provider must determine the best way to designate an expression level suited to the purpose of the test, while striving to mitigate ambiguities resulting from lack of consistency of use.
    h. Explicitly indicating the cellular sublocation for a marker: In most cases, the location of a marker on or within a cell is not necessary; however, there are situations in which a marker can be expressed in more than a single cellular compartment and there is a need for the test to distinguish between marker expression in one compartment versus another. To accommodate this, using a lowercase letter in front of the marker is recommended. The cell sublocations are usually related to the cell surface (plasma membrane), cytoplasm, and nucleus. Use m, c, or n in front of the marker to denote "membrane", "cytoplasm", and "nucleus", respectively. An example of a marker often associated with a need to indicate cell location is CD152 (CTLA4), where cytoplasmic expression may define a test to distinguish it from whole cell expression. In this case, "cCD152" is used to denote that it is the cytoplasmic expression of CD152 that is measured for the test.
9. CPNRIND can be added to indicate where a result falls with respect to a reference range defined by CPORNRLO and CPORNRHI (e.g., "HIGH", "LOW").
10. The variable CPORRESU uses the UNIT codelist. This means that sponsors should be submitting a term from the CDISC Submission Value column in the published Controlled Terminology maintained for CDISC by NCI EVS. When sponsors have units that are not in this column, they should first check to see if their unit is mathematically synonymous with an existing unit and submit their lab values using that unit. If this is not the case, then a request for a new term (see https://ncitermform.nci.nih.gov/) should be submitted.

##### CP – Examples
The CP domain includes use of several new qualifier variables. The primary intent of the following examples is to demonstrate the appropriate use of these new variables based on a selection of use cases for which they would ordinarily be included in a well-structured CP dataset. Secondarily, the examples illustrate standardized formatting concepts for variables that are not associated with a formal Controlled Terminology codelist. Although not controlled, the standardized formatting of content for these variables significantly aids understanding of the test and associated data, making data review and comparisons much easier. To make the examples as easy to understand as possible, many of the other SDTM variables that would normally be included in the dataset and which are already familiar to the reader have not been included.
The following new SDTM variables are included in the examples: CPSBMRKS (Sublineage Marker String), CPCELSTA (Cell State), CPCSMRKS (Cell State Marker String), CPTSTCND (Test Condition), CPCNDAGT (Test Condition Agent), CPBDAGNT (Binding Agent), CPABCLID (Antibody Clone Identifier), CPMRKSTR (Marker String), CPGATE (Gate), CPGATDEF (Gate Definition), CPSPTSTD (Sponsor Test Description), CPTSTPNL (Test Panel), CPRESSCL (Result Scale), CPRESTYP (Result Type), and CPCOLSRT (Collected Summary Result Type). The proper use of each of these variables is illustrated in 1 or more of the examples, based on the identified use case.

**Example 1**
Example 1a illustrates use of the CPMRKSTR variable for an assay panel that enumerates several of the major named cell subpopulations of leukocytes. For most cases involving simple phenotyping, and when used in accordance with CP domain guidance, the CPMRKSTR variable is sufficient for providing the marker information needed to fully describe a test. As such, CPMRKSTR is the only new CP test qualifier variable having a Core designation of "Expected". In such a case, the sponsor may determine whether to include other permissible CP test qualifier variables, based on the needs of the data recipient. This example presents records that might typically be reported for a panel of tests quantifying T-cell, B-cell, monocyte, and natural killer (NK) cell populations, and for subtyping T-cells. In this example, the sponsor determined that none of the permissible CP test qualifier variables were needed to accurately comprehend or distinguish among tests in the dataset, so chose to include only the CPMRKSTR (complete markers string) information.
Example 1b, in addition to including the expected CPMRKSTR variable, introduces 2 additional variables: CPGATE and CPGATDEF. These variables convey gating information used in data collection and/or analyses, and are often needed to fully understand a test. Typically, either the full gating strategy or the penultimate gate is identified. Because different gating strategies for the same test can yield somewhat different test results, the CPGATE and CPGATDEF variables provide the means for transmitting this information at the test (i.e., record) level.

**Example 1a**
**Rows 1-3:** The total leukocyte population is determined using positive expression of the CD45 marker as the operational definition of the test (CD45+ in the CPMRKSTR variable). The total leukocyte count is reported because it contains the value used as the denominator in several subsequent tests for leukocyte subpopulations. Row 2 contains the total lymphocyte count which, in addition to CD45, used Forward (FSC) and Side (SSC) Light Scatter properties to define the lymphocyte subpopulation of leukocytes. By convention, FSC and SSC are often not included as part of the marker string definition of a cell subpopulation since it is well-recognized that these physical properties are used as the first gate in nearly all cell phenotyping applications. However, in the absence of a pan-lymphocyte marker to distinguish them from other leukocytes, FSC and SSC are included in rows 2 and 3 to indicate that these parameters are used in addition to CD45, to differentiate lymphocytes from other CD45+ leukocytes. Once they have been included in the marker string (CPMRKSTR) definition of lymphocytes, they can generally be dropped for any further subsetting of the lymphocytes population.
**Row 3:** Shows the proportion of lymphocytes as a percentage of total leukocytes. Note that the value in CPMRKSTR used a forward slash ("/") to separate the numerator marker string from the denominator marker string.
**Rows 4-5:** The B-lymphocyte lineage of lymphocytes is determined using a set of lineage-specific markers in addition to the CD45 leukocyte marker, to define the subpopulation both in terms of positive (i.e., CD19+) and negative (i.e., CD3-, CD14-, and CD56-) marker expression. Following a common convention and CP domain guidance for ordering markers in CPMRKSTR, the marker(s) used to define the highest level of the lineage hierarchy are placed first (i.e., CD45+ defining the leukocyte population), followed by marker(s) that define each subsequently lower level of the hierarchy. The example also follows a convention whereby the set of positive and negative markers used to identify the major lineages of leukocytes are ordered by T-cell, B-cell, monocyte, and NK cell. In row 4, B lymphocytes are defined as leukocytes (CD45+), non-T-cell (CD3-), B-cell (CD19+), non-monocyte (CD14-), and non-NK cell (CD56-), resulting in a CPMRKSTR value of "CD45+CD3-CD19+CD14-CD56-". Row 5 shows that CPMRKSTR contains the full set of markers used to define both the numerator and the denominator, separated by a forward slash "/".
**Rows 6-7:** The T-lymphocyte lineage of lymphocytes is determined using a set of lineage-specific markers in addition to the CD45 leukocyte marker, to define the subpopulation both in terms of positive (i.e., CD3+) and negative (i.e., CD19-, CD14-, and CD56-) marker expression. The order of markers in CPMRKSTR follows the same convention described for B-lymphocytes in rows 4 and 5.
**Rows 8-11:** The T-lymphocyte lineage is divided further into T helper and T cytotoxic sublineages. In these examples the laboratory does not use the negative lineage markers for B-cells, monocytes, and NK cells, but used the positive T-cell (CD3) marker to identify the T-lymphocyte population, and additional markers to define subpopulations as either the T helper (CD4+CD8-) or T cytotoxic (CD4-CD8+) subpopulation. In rows 9 and 11, results are reported as a percentage of the total T-lymphocyte population. Using CPMRKSTR, the numerator is the marker string used to define the T helper subpopulation (as shown in row 8) or the T cytotoxic subpopulation (as shown in row 10), and the denominator consists of the marker string used to define the total T-lymphocyte population (as shown in row 6). A forward slash "/" is used to separate the numerator and denominator.
**Rows 12-13:** The monocyte lineage of leukocytes is determined using a set of lineage-specific markers in addition to the CD45 leukocyte marker, to define the subpopulation both in terms of positive (i.e., CD14+) and negative (i.e., CD3-, CD19-, and CD56-) marker expression. The order of markers in CPMRKSTR follows the same convention described for B-lymphocytes in rows 4 and 5. In addition, the sponsor chose to include the FSC and SSC properties as markers because they are used, in part, to differentiate the monocyte and lymphocyte populations. Note that when FSC and SSC are used in a marker string, they usually go last, whereas they often come first when showing a gating strategy.
**Rows 14-15:** The NK cell lineage of leukocytes is determined using a set of lineage-specific markers in addition to the CD45 leukocyte marker, to define the subpopulation both in terms of positive (i.e., CD56+) and negative (i.e., CD3-, CD19-, and CD14-) marker expression. The order of markers in CPMRKSTR follows the same convention described for B-lymphocytes in rows 4 and 5. In addition, the sponsor chose to include the FSC and SSC properties as markers because they are used, in part, to differentiate the natural killer cell and lymphocyte populations. Note that when FSC and SSC are used in a marker string, they usually go last, whereas they often come first when showing a gating strategy.
**Row 16:** The ratio of T helper to T cytotoxic lymphocytes is calculated from the T helper (CD4+) cell count in row 8 and the T cytotoxic (CD8+) cell count in row 10 and a unit of measure is not included because it is not reported by the lab for this type of test.


*cp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPTESTCD | CPTEST | CPMRKSTR | CPCAT | CPORRES | CPORRESU | CPSTRESC | CPSTRESU | CPSTRESN | CPRESSCL | CPRESTYP | CPSPEC | CPMETHOD | CPDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABCD | CP | ABCD-001-001 | 1 | WBC | Leukocytes | CD45+ | IMMUNOPHENOTYPING | 6630 | 10^6/L | 6630 | 10^6/L | 6630 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 2 | ABCD | CP | ABCD-001-001 | 2 | LYM | Lymphocytes | CD45+FSC SSC | IMMUNOPHENOTYPING | 1710 | 10^6/L | 1710 | 10^6/L | 1710 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 3 | ABCD | CP | ABCD-001-001 | 3 | LYMLE | Lymphocytes/Leukocytes | CD45+FSC SSC/CD45+ | IMMUNOPHENOTYPING | 25.8 | % | 25.8 | % | 25.8 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 4 | ABCD | CP | ABCD-001-001 | 4 | BLYCE | B-Lymphocytes | CD45+CD3-CD19+CD14-CD56- | IMMUNOPHENOTYPING | 104 | 10^6/L | 104 | 10^6/L | 104 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 5 | ABCD | CP | ABCD-001-001 | 5 | BLYCELY | B-Lymphocytes/Lymphocytes | CD45+CD3-CD19+CD14-CD56- /CD45+FSC SSC | IMMUNOPHENOTYPING | 6.1 | % | 6.1 | % | 6.1 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 6 | ABCD | CP | ABCD-001-001 | 6 | TLYCE | T-Lymphocytes | CD45+CD3+CD19-CD14-CD56- | IMMUNOPHENOTYPING | 1108 | 10^6/L | 1108 | 10^6/L | 1108 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 7 | ABCD | CP | ABCD-001-001 | 7 | TLYLY | TLym/Lym | CD45+CD3+CD19-CD14-CD56- /CD45+FSC SSC | IMMUNOPHENOTYPING | 64.8 | % | 64.8 | % | 64.8 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 8 | ABCD | CP | ABCD-001-001 | 8 | TLYH | TLym Help | CD45+CD3+CD4+CD8- | IMMUNOPHENOTYPING | 425 | 10^6/L | 425 | 10^6/L | 425 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 9 | ABCD | CP | ABCD-001-001 | 9 | TLYHTLY | TLym Help/TLym | CD45+CD3+CD4+CD8- /CD45+CD3+CD19-CD14-CD56- | IMMUNOPHENOTYPING | 38.4 | % | 38.4 | % | 38.4 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 10 | ABCD | CP | ABCD-001-001 | 10 | TLC | TLym Cytx | CD45+CD3+CD4-CD8+ | IMMUNOPHENOTYPING | 682 | 10^6/L | 682 | 10^6/L | 682 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 11 | ABCD | CP | ABCD-001-001 | 11 | TLYCTLY | TLym Cytx/TLym | CD45+CD3+CD4-CD8+/CD45+CD3+CD19-CD14-CD56- | IMMUNOPHENOTYPING | 61.6 | % | 61.6 | % | 61.6 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 12 | ABCD | CP | ABCD-001-001 | 12 | MONO | Monocytes | CD45+CD3-CD19-CD14+CD56- FSC SSC | IMMUNOPHENOTYPING | 613 | 10^6/L | 613 | 10^6/L | 613 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 13 | ABCD | CP | ABCD-001-001 | 13 | MONOLE | Monocytes/Leukocytes | CD45+CD3-CD19-CD14+CD56- FSC SSC/CD45+ | IMMUNOPHENOTYPING | 9.3 | % | 9.3 | % | 9.3 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 14 | ABCD | CP | ABCD-001-001 | 14 | NKCE | Natural Killer Cells | CD45+CD3-CD19-CD14-CD56+FSC SSC | IMMUNOPHENOTYPING | 230 | 10^6/L | 230 | 10^6/L | 230 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 15 | ABCD | CP | ABCD-001-001 | 15 | NKLE | NK Cells/Leuk | CD45+CD3-CD19-CD14-CD56+FSC SSC/CD45+ | IMMUNOPHENOTYPING | 3.5 | % | 3.5 | % | 3.5 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 16 | ABCD | CP | ABCD-001-001 | 16 | TLYHTLYC | TLym Help/TLym Cytx | CD45+CD3+CD4+CD8- /CD45+CD3+CD4-CD8+ | IMMUNOPHENOTYPING | 0.62 |  | 0.62 |  | 0.62 | QUANTITATIVE | RATIO | BLOOD | CALCULATION | 2021-08-16T04:20 |


**Example 1b**

**Row 1:** The total leukocyte count is reported for a whole blood specimen in which the CD45 marker is used to identify the leukocyte population. FSC and SSC are used to exclude debris and non-singlets from data collection events. Because FSC and SSC are nearly always used in this manner in the first data collection gate, they are usually assumed and are often not reported (i.e., the sponsor could have chosen to leave CPGATDEF null).
**Rows 2-3:** The total lymphocyte subpopulation of leukocytes is reported in row 2 as an absolute cell count, and in row 3 as a percentage of leukocytes. In these cases, FSC and SSC were used as subgates to isolate the lymphocyte lineage within the leukocyte (CD45+) population. Because FSC and SSC (in addition to the CD45 leukocyte marker) are used to define the lymphocyte lineage, they are included in CPMRKSTR.

*cp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPTESTCD | CPTEST | CPMRKSTR | CPGATE | CPGATDEF | CPCAT | CPORRES | CPORRESU | CPSTRESC | CPSTRESU | CPSTRESN | CPRESSCL | CPRESTYP | CPSPEC | CPMETHOD | CPDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABCD | CP | ABCD-001-001 | 1 | WBC | Leukocytes | CD45+ |  | FSC SSC | IMMUNOPHENOTYPING | 6630 | 10^6/L | 6630 | 10^6/L | 6630 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 2 | ABCD | CP | ABCD-001-001 | 2 | LYM | Lymphocytes | CD45+FSC SSC | LEUK | CD45+ | IMMUNOPHENOTYPING | 1710 | 10^6/L | 1710 | 10^6/L | 1710 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
| 3 | ABCD | CP | ABCD-001-001 | 3 | LYMLE | Lymphocytes/Leukocytes | CD45+FSC SSC/CD45+ | LEUK | CD45+ | IMMUNOPHENOTYPING | 25.8 | % | 25.8 | % | 25.8 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |

**Example 2**
This example illustrates a lymphocyte apoptosis assay. It demonstrates the use of CPCELSTA and CPCSMRKS for biological cell states (viable, apoptotic, activated, exhausted, senescent, proliferating).

**Rows 1-2:** Forward light scatter (FSC) and side scatter (SSC) are almost always applied as the first gating parameters. In row 1, a lymphocyte count is reported which does not explicitly provide viability information. In contrast, row 2 explicitly calls out cell viability based on the use of viability marker 7AAD to exclude cells that are in the process of dying (7AAD+). This is indicated in CPMRKSTR, CPGATDEF, and CPGATE ("VIABLE").
**Rows 3-4:** Illustrate using CPCELSTA and CPCSMRKS to provide the cell state descriptor and the markers used to define the cell state. These variables further define CPTEST to be a subset, therefore the suffix "Sub" is appended. Row 3 = VIABLE (7AAD-); Row 4 = NON-VIABLE (7AAD+).
**Rows 5-6:** Illustrate CPCELSTA and CPCSMRKS for the APOPTOTIC cell state. Row 5 = apoptotic lymphocyte count (ANXV+); Row 6 = apoptotic lymphocytes as percentage of total lymphocytes.
**Rows 7-8:** Illustrate CPTEST, CPCELSTA, and CPCSMRKS when the cell population has more than a single cell state of interest (both VIABLE and APOPTOTIC). 7AAD combined with ANXV.
**Rows 9-11:** Illustrate pre-coordinated test names when the test incorporates results from multiple records. Rows 9-10 use CPCELSTA for VIABLE and NON-VIABLE. Row 11 is the ratio of viable to nonviable; viability information is pre-coordinated into CPTEST rather than using CPCELSTA. CPGRPID groups the related records.

*cp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPGRPID | CPTESTCD | CPTEST | CPCELSTA | CPCSMRKS | CPMRKSTR | CPGATE | CPGATDEF | CPCAT | CPTSTPNL | CPORRES | CPORRESU | CPSTRESC | CPSTRESU | CPSTRESN | CPRESSCL | CPRESTYP | CPSPEC | CPMETHOD | CPDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | IM001-123 | CP | 000500542 | 1 |  | LYM | Lymphocytes |  |  | CD45+FSC SSC | LEUK | CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 3500 | 10^6/L | 3500 | 10^6/L | 3500 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
| 2 | IM001-123 | CP | 000500542 | 2 | 1 | LYM | Lymphocytes |  |  | CD45+7AAD-FSC SSC | LEUK, VIABLE | CD45+7AAD- | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 3325 | 10^6/L | 3325 | 10^6/L | 3325 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
| 3 | IM001-123 | CP | 000500542 | 3 | 1 | LYS | Lym Sub | VIABLE | 7AAD- | CD45+7AAD- | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 3325 | 10^6/L | 3325 | 10^6/L | 3325 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
| 4 | IM001-123 | CP | 000500542 | 4 | 1 | LYS | Lym Sub | NON-VIABLE | 7AAD+ | CD45+7AAD+ | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 175 | 10^6/L | 175 | 10^6/L | 175 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
| 5 | IM001-123 | CP | 000500542 | 5 | 1 | LYS | Lym Sub | APOPTOTIC | ANXV+ | CD45+ANXV+ | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 700 | 10^6/L | 700 | 10^6/L | 700 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
| 6 | IM001-123 | CP | 000500542 | 6 | 1 | LYSLY | Lym Sub/Lym | APOPTOTIC | ANXV+ | CD45+ANXV+/CD45+FSC SSC | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 21 | % | 21 | % | 21 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T04:20 |
| 7 | IM001-123 | CP | 000500542 | 7 | 1 | LYS | Lym Sub | VIABLE; APOPTOTIC | 7AAD-ANXV+ | CD45+7AAD-ANXV+ | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 665 | 10^6/L | 665 | 10^6/L | 665 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
| 8 | IM001-123 | CP | 000500542 | 8 | 1 | LYSLY | Lym Sub/Lym | VIABLE; APOPTOTIC | 7AAD-ANXV+ | CD45+7AAD-ANXV+/CD45+FSC SSC | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 20 | % | 20 | % | 20 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
| 9 | IM001-123 | CP | 000500542 | 9 | 2 | LYS | Lym Sub | VIABLE | 7AAD- | CD45+7AAD- | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 3325 | 10^6/L | 3325 | 10^6/L | 3325 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
| 10 | IM001-123 | CP | 000500542 | 10 | 2 | LYS | Lym Sub | NON-VIABLE | 7AAD+ | CD45+7AAD+ | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 175 | 10^6/L | 175 | 10^6/L | 175 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
| 11 | IM001-123 | CP | 000500542 | 11 | 3 | LYVLYNV | Lym Viable/Lym NonViable |  |  | CD45+7AAD-/CD45+7AAD+ | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 19 | RATIO | 19 | RATIO | 19 | QUANTITATIVE | RATIO | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |

**Example 3**
This example illustrates a monocyte subset assay. It highlights CPSBMRKS, CPCELSTA, CPCSMRKS, and how CPTEST is qualified by those variables. Demonstrates named populations, "Sub" suffix, and CPSBMRKS for unnamed sublineages.

**Rows 1-3:** Show use of CPCELSTA and CPCSMRKS to further subset the named cell population. Row 1 = total monocytes (CD14+). Rows 2-3 subdivide into proliferating (Ki67+) and non-proliferating (Ki67-) subpopulations as indicated by CPCELSTA. "Sub" is appended to CPTEST. CPCSMRKS indicates Ki67+ for proliferating and Ki67- for non-proliferating.
**Rows 4-5:** Show the proliferating (from row 2) and non-proliferating (from row 3) monocyte subpopulations expressed as a percentage of total monocytes (from row 1). CPGRPID indicates which records belong to the group.
**Row 6:** Shows the ratio of the proliferating to non-proliferating monocyte subpopulation. CPCELSTA and CPCSMRKS are not populated because cell state information is pre-coordinated into the test name (CPTEST). CPORRESU/CPSTRESU left blank; CPRESTYP = RATIO.
**Rows 7-9:** Show use of CPSBMRKS to further subset monocytes into sublineages based on expression of additional markers CDxx and CDyy. Row 7 = total monocytes. Rows 8-9 = CDxx+CDyy- and CDxx-CDyy+ sublineages. "Sub" appended to CPTEST.
**Rows 10-11:** Show monocyte sublineages from rows 8-9 expressed as percentage of total monocytes (row 7). CPSBMRKS differentiates the sublineages. CPGRPID indicates which records belong to the group.
**Row 12:** Demonstrates how CPSBMRKS, CPCELSTA, and CPCSMRKS work in combination with CPTEST to further define cell subpopulations based on any additional sublineage and cell state markers.

*cp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPGRPID | CPTESTCD | CPTEST | CPSBMRKS | CPCELSTA | CPCSMRKS | CPMRKSTR | CPGATE | CPGATDEF | CPCAT | CPTSTPNL | CPORRES | CPORRESU | CPSTRESC | CPSTRESU | CPSTRESN | CPRESSCL | CPRESTYP | CPSPEC | CPMETHOD | CPDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | CP | ABCD-001-001 | 1 | 1 | MONO | Monocytes |  |  |  | CD14+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 394 | 10^6/L | 394 | 10^6/L | 394 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
| 2 | ABC-123 | CP | ABCD-001-001 | 2 | 1 | MNS | Mono Sub |  | PROLIFERATING | Ki67+ | CD14+Ki67+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 50 | 10^6/L | 50 | 10^6/L | 50 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
| 3 | ABC-123 | CP | ABCD-001-001 | 3 | 1 | MNS | Mono Sub |  | NON-PROLIFERATING | Ki67- | CD14+Ki67- | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 344 | 10^6/L | 344 | 10^6/L | 344 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
| 4 | ABC-123 | CP | ABCD-001-001 | 4 | 1 | MNSMN | Mono Sub/Mono |  | PROLIFERATING | Ki67+ | CD14+Ki67+/CD14+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 12.69 | % | 12.69 | % | 12.69 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
| 5 | ABC-123 | CP | ABCD-001-001 | 5 | 1 | MNSMN | Mono Sub/Mono |  | NON-PROLIFERATING | Ki67- | CD14+Ki67-/CD14+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 87.31 | % | 87.31 | % | 87.31 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
| 6 | ABC-123 | CP | ABCD-001-001 | 6 | 1 | MNPMNNP | Mono Prolif/Mono NonProlif |  |  |  | CD14+Ki67+/CD14+Ki67- | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 0.15 |  | 0.15 |  | 0.15 | QUANTITATIVE | RATIO | BLOOD | CALCULATION | 2020-08-16T08:00 |
| 7 | ABC-123 | CP | ABCD-001-001 | 7 | 2 | MONO | Monocytes |  |  |  | CD14+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 394 | 10^6/L | 394 | 10^6/L | 394 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
| 8 | ABC-123 | CP | ABCD-001-001 | 8 | 2 | MNS | Mono Sub | CDxx+CDyy- |  |  | CD14+CDxx+CDyy- | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 366 | 10^6/L | 366 | 10^6/L | 366 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
| 9 | ABC-123 | CP | ABCD-001-001 | 9 | 2 | MNS | Mono Sub | CDxx-CDyy+ |  |  | CD14+CDxx-CDyy+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 20 | 10^6/L | 20 | 10^6/L | 20 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
| 10 | ABC-123 | CP | ABCD-001-001 | 10 | 2 | MNSMN | Mono Sub/Mono | CDxx+CDyy- |  |  | CD14+CDxx+CDyy-/CD14+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 93.00 | % | 93.00 | % | 93.00 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
| 11 | ABC-123 | CP | ABCD-001-001 | 11 | 2 | MNSMN | Mono Sub/Mono | CDxx-CDyy+ |  |  | CD14+CDxx-CDyy+/CD14+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 5.00 | % | 5.00 | % | 5.00 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
| 12 | ABC-123 | CP | ABCD-001-001 | 12 | 3 | MNS | Mono Sub | CDxx+CDyy- | APOPTOTIC | ANXV+ | CD14+CDxx+CDyy-ANXV+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 5 | 10^6/L | 5 | 10^6/L | 5 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |

**Example 4**
This example illustrates a CCR5 cytotoxic T helper assay. It demonstrates CPTSTCND, CPCNDAGT, CPREPNUM, and CPCOLSRT for test conditions, replicates, and summary results.

**Rows 1-3:** Illustrate how the test condition (CPTSTCND), replicates (CPREPNUM) and collected summary result type (CPCOLSRT) are used for a test system involving unstimulated CCR5+ cytotoxic T-lymphocytes. Rows 1-2 are replicates (CPREPNUM = 1 and 2). Row 3 is the MEAN of the unstimulated condition (CPCOLSRT = MEAN, CPREPNUM blank).
**Rows 4-6:** Illustrate the association between CPTSTCND ("WITH STIMULATING AGENT") and CPCNDAGT ("MACROPHAGE INFLAMMATORY PROTEIN 1BETA"). CPREPNUM and CPCOLSRT are used as described for rows 1-3.
**Row 7:** Shows the ratio of the stimulated to unstimulated populations based on mean results. CPANMETH = "STIMULATED/UNSTIMULATED". Calculated values provided in a lab report are considered collected rather than derived.

*cp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPGRPID | CPTESTCD | CPTEST | CPCELSTA | CPCSMRKS | CPTSTCND | CPCNDAGT | CPMRKSTR | CPGATE | CPGATDEF | CPCAT | CPTSTPNL | CPORRES | CPORRESU | CPRESSCL | CPRESTYP | CPCOLSRT | CPSTRESC | CPSTRESN | CPSTRESU | CPSPEC | CPMETHOD | CPANMETH | CPREPNUM | CPDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | CP | ABCD-001-001 | 1 | 1 | TLCSTLC | TLym Cytx Sub/TLym Cytx | ACTIVATED | pCCR5+ | WITHOUT STIMULATING AGENT |  | CD3+CD8+pCCR5+/CD3+CD8+ | TLym Cytx | FSC SSC\|CD3+CD8+ | CELL FUNCTION | pCCR5 T-LYMPHOCYTES | 0.9 | % | QUANTITATIVE | NUMBER FRACTION |  | 0.9 | 0.9 | % | BLOOD | FLOW CYTOMETRY |  | 1 | 2021-03-20T09:52:00 |
| 2 | ABC-123 | CP | ABCD-001-001 | 2 | 1 | TLCSTLC | TLym Cytx Sub/TLym Cytx | ACTIVATED | pCCR5+ | WITHOUT STIMULATING AGENT |  | CD3+CD8+pCCR5+/CD3+CD8+ | TLym Cytx | FSC SSC\|CD3+CD8+ | CELL FUNCTION | pCCR5 T-LYMPHOCYTES | 0.6 | % | QUANTITATIVE | NUMBER FRACTION |  | 0.6 | 0.6 | % | BLOOD | FLOW CYTOMETRY |  | 2 | 2021-03-20T09:52:00 |
| 3 | ABC-123 | CP | ABCD-001-001 | 3 | 1 | TLCSTLC | TLym Cytx Sub/TLym Cytx | ACTIVATED | pCCR5+ | WITHOUT STIMULATING AGENT |  | CD3+CD8+pCCR5+/CD3+CD8+ | TLym Cytx | FSC SSC\|CD3+CD8+ | CELL FUNCTION | pCCR5 T-LYMPHOCYTES | 0.8 | % | QUANTITATIVE | NUMBER FRACTION | MEAN | 0.8 | 0.8 | % | BLOOD | CALCULATION |  |  | 2021-03-20T09:52:00 |
| 4 | ABC-123 | CP | ABCD-001-002 | 1 | 2 | TLCSTLC | TLym Cytx Sub/TLym Cytx | ACTIVATED | pCCR5+ | WITH STIMULATING AGENT | MACROPHAGE INFLAMMATORY PROTEIN 1BETA | CD3+CD8+pCCR5+/CD3+CD8+ | TLym Cytx | FSC SSC\|CD3+CD8+ | CELL FUNCTION | pCCR5 T-LYMPHOCYTES | 2.9 | % | QUANTITATIVE | NUMBER FRACTION |  | 2.9 | 2.9 | % | BLOOD | FLOW CYTOMETRY |  | 1 | 2021-03-20T09:52:00 |
| 5 | ABC-123 | CP | ABCD-001-002 | 2 | 2 | TLCSTLC | TLym Cytx Sub/TLym Cytx | ACTIVATED | pCCR5+ | WITH STIMULATING AGENT | MACROPHAGE INFLAMMATORY PROTEIN 1BETA | CD3+CD8+pCCR5+/CD3+CD8+ | TLym Cytx | FSC SSC\|CD3+CD8+ | CELL FUNCTION | pCCR5 T-LYMPHOCYTES | 2.6 | % | QUANTITATIVE | NUMBER FRACTION |  | 2.6 | 2.6 | % | BLOOD | FLOW CYTOMETRY |  | 2 | 2021-03-20T09:52:00 |
| 6 | ABC-123 | CP | ABCD-001-002 | 3 | 2 | TLCSTLC | TLym Cytx Sub/TLym Cytx | ACTIVATED | pCCR5+ | WITH STIMULATING AGENT | MACROPHAGE INFLAMMATORY PROTEIN 1BETA | CD3+CD8+pCCR5+/CD3+CD8+ | TLym Cytx | FSC SSC\|CD3+CD8+ | CELL FUNCTION | pCCR5 T-LYMPHOCYTES | 2.8 | % | QUANTITATIVE | NUMBER FRACTION | MEAN | 2.8 | 2.8 | % | BLOOD | CALCULATION |  |  | 2021-03-20T09:52:00 |
| 7 | ABC-123 | CP | ABCD-001-002 | 4 |  | STIMDX | Stimulation Index | ACTIVATED | pCCR5+ |  | MACROPHAGE INFLAMMATORY PROTEIN 1BETA |  |  |  | CELL FUNCTION | pCCR5 T-LYMPHOCYTES | 3.5 | RATIO | QUANTITATIVE | RATIO |  | 3.5 | 3.5 | RATIO | BLOOD | CALCULATION | STIMULATED/UNSTIMULATED |  | 2021-03-20T09:52:00 |

**Example 5**
This example illustrates a B-lymphocyte activation assay with single-marker quantitation, CPGATE/CPGATDEF for full gating strategy, and total events counted within a gate.

**Rows 1-3:** Incorporates both standard proportion analysis and single marker expression for a cell state marker in the B lymphocyte assay using CPGRPID to group the related records. Row 3 contains "CD95 Expression" — CPMRKSTR uses the recommended format: marker being measured first, followed by the unit (MdFI), then the complete marker string of the cell population. CPGATE and CPGATDEF show the gating strategy.
**Rows 4-8:** Show a set of tests similar to rows 1-3, except that the marker being quantified is more narrowly restricted to a subpopulation of B lymphocytes (naive B cells), identified using a richer set of markers. The sponsor chose, in row 6, to include the total number of events counted in the final gate to document that the data are reliable based on sufficient sample size. Rows 7-8 = CD95 Expression for naive B cells.

*cp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPGRPID | CPTESTCD | CPTEST | CPCELSTA | CPCSMRKS | CPMRKSTR | CPGATE | CPGATDEF | CPCAT | CPSCAT | CPTSTPNL | CPORRES | CPORRESU | CPRESSCL | CPRESTYP | CPSTRESC | CPSTRESN | CPSTRESU | CPSPEC | CPMETHOD | CPDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | CP | ABCD-001-001 | 1 | 1 | BLYCELE | BLym/Leuk |  |  | CD45+CD19+/CD45+ | BLym | FSC+SSC+|CD45+|CD19+ | IMMUNOPHENOTYPING | B CELL ACTIVATION | CD95 Expr BLym | 5.3 | % | QUANTITATIVE | NUMBER FRACTION | 5.3 | 5.3 | % | BLOOD | FLOW CYTOMETRY | 2021-10-20T09:20:00 |
| 2 | ABC-123 | CP | ABCD-001-001 | 2 | 1 | BLYSBLY | BLym Sub/BLym | APOPTOTIC | CD95+ | CD45+CD19+CD95+/CD45+CD19+ | BLym | FSC+SSC+|CD45+|CD19+CD95+ | IMMUNOPHENOTYPING | B CELL ACTIVATION | CD95 Expr BLym | 55.3 | % | QUANTITATIVE | NUMBER FRACTION | 55.3 | 55.3 | % | BLOOD | FLOW CYTOMETRY | 2021-10-20T09:20:00 |
| 3 | ABC-123 | CP | ABCD-001-001 | 3 | 1 | CD95X | CD95 Expression | APOPTOTIC | CD95+ | CD95 MdFI CD45+CD19+CD95+ | CD95+ BLym | FSC+SSC+|CD45+|CD19+CD95+ | IMMUNOPHENOTYPING | B CELL ACTIVATION | CD95 Expr BLym | 100 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY | 100 | 100 | MdFI | BLOOD | FLOW CYTOMETRY | 2021-10-20T09:20:00 |
| 4 | ABC-123 | CP | ABCD-001-002 | 1 | 2 | BLYCELE | BLym/Leuk |  |  | CD45+CD19+/CD45+ | BLym | FSC+SSC+|CD45+|CD19+ | IMMUNOPHENOTYPING | B CELL ACTIVATION | CD95 Expr BLym | 5.3 | % | QUANTITATIVE | NUMBER FRACTION | 5.3 | 5.3 | % | BLOOD | FLOW CYTOMETRY | 2021-10-20T09:20:00 |
| 5 | ABC-123 | CP | ABCD-001-002 | 2 | 2 | BLYNBLY | BLym Naive/BLym |  |  | CD45+CD19+IgD+CD27-/CD45+CD19+ | BLym | FSC+SSC+|CD45+CD19+ | IMMUNOPHENOTYPING | B CELL ACTIVATION | CD95 Expr BLym | 83.9 | % | QUANTITATIVE | NUMBER FRACTION | 83.9 | 83.9 | % | BLOOD | FLOW CYTOMETRY | 2021-10-20T09:20:00 |
| 6 | ABC-123 | CP | ABCD-001-002 | 3 | 2 | BLYN | BLym Naive Sub | APOPTOTIC | CD95+ | CD45+CD19+IgD+CD27- CD95+/CD45+CD19+IgD+CD27- | CD95+ BLym Naive | FSC+SSC+|CD45+|CD19+|IgD+CD27- |CD95+ | IMMUNOPHENOTYPING | B CELL ACTIVATION | CD95 Expr BLym | 2946 | Events | QUANTITATIVE | NUMBER | 2946 | 2946 | Events | BLOOD | FLOW CYTOMETRY | 2021-10-20T09:20:00 |
| 7 | ABC-123 | CP | ABCD-001-002 | 4 | 2 | BNSBN | BLym Naive Sub/BLym Naive | APOPTOTIC | CD95+ | CD45+CD19+IgD+CD27- CD95+/CD45+CD19+IgD+CD27- | CD95+ BLym Naive | FSC+SSC+|CD45+|CD19+|IgD+CD27- |CD95+ | IMMUNOPHENOTYPING | B CELL ACTIVATION | CD95 Expr BLym | 50.2 | % | QUANTITATIVE | NUMBER FRACTION | 50.2 | 50.2 | % | BLOOD | FLOW CYTOMETRY | 2021-10-20T09:20:00 |
| 8 | ABC-123 | CP | ABCD-001-002 | 5 | 2 | CD95X | CD95 Expression | APOPTOTIC | CD95+ | CD95 MdFI CD45+CD19+IgD+CD27- CD95+ | CD95+ BLym Naive | FSC+SSC+|CD45+|CD19+|IgD+CD27- |CD95+ | IMMUNOPHENOTYPING | B CELL ACTIVATION | CD95 Expr BLym | 89 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY | 89 | 89 | MdFI | BLOOD | FLOW CYTOMETRY | 2021-10-20T09:20:00 |

**Example 6**
This example illustrates a complex dendritic cell (DC) assay panel. It demonstrates CPSPTSTD (Sponsor Test Description) for lab/sponsor internal nomenclature, which aids in understanding the test when formal controlled terminology may not fully capture the lab-specific nuances.

**Rows 1-6:** Illustrate how the sponsor uses CPSPTSTD to combine details of a test into a single variable to align with the lab/sponsor data repository or dictionary and to aid understanding of the test. Rows 1-4 introduce CPSPTSTD using simple tests for dendritic cells to set the stage for the more complex tests shown in rows 5-6. Those rows incorporate an additional marker (CD1c-) to define the plasmacytoid sublineage, and a non-lineage, non-cell state marker (CD303+) that is of interest.
**Rows 7-10:** Illustrate how CPSPTSTD might preface the name of a cell population with cell state marker(s) (e.g., CD83+ in rows 7-8). Rows 9-10 additionally show that the lab/sponsor uses CPSPTSTD to identify the target cell population by name when it is not in CPTEST, such as when the test is for quantitative single marker expression (CD83 Expression in rows 9-10).
**Rows 11-14:** Same as rows 7-10, except here the cell state activation marker for the CD303+ pDC cell subset and the single marker expression measurement is CD80.
**Rows 15-18:** Illustrate how CPSPTSTD might preface the name of a cell population with cell sublineage marker(s) (e.g., CD40+ in rows 15-16). Rows 17-18 additionally show the lab/sponsor uses CPSPTSTD to identify the target cell population by name for quantitative single marker expression (CD40 Expression in rows 17-18).
**Rows 19-32:** No new concepts are introduced in these rows, but they are additional illustrations of using CPSBMRKS, CPCELSTA, CPCSMRKS and CPSPTSTD for a subset of pDC in which CD123+ is a marker of interest which is neither a cell sublineage nor cell state marker. These rows are included to reinforce the principles illustrated in rows 1-18.

*cp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPGRPID | CPTESTCD | CPTEST | CPSBMRKS | CPCELSTA | CPCSMRKS | CPMRKSTR | CPGATE | CPGATDEF | CPSPTSTD | CPCAT | CPTSTPNL | CPORRES | CPORRESU | CPRESSCL | CPRESTYP | CPSTRESC | CPSTRESN | CPSTRESU | CPSPEC | CPMETHOD | CPDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | CP | ABCD-001-001 | 1 | 1 | LYMONOLE | Lym+Mono/Leuk |  |  |  | CD45+SSCmid/CD45+ | LYM+MONO | SSCmid|CD45+ | %Lym+Mono/Leuk | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 6.70 | % | QUANTITATIVE | NUMBER FRACTION | 6.70 | 6.70 | % | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 2 | ABC-123 | CP | ABCD-001-001 | 2 | 1 | LYMONO | Lym+Mono |  |  |  | CD45+SSCmid | LYM+MONO | SSCmid|CD45+ | Lym+Mono Count | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 663 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | 663 | 663 | 10^6/L | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 3 | ABC-123 | CP | ABCD-001-001 | 3 | 1 | DCLYMONO | Dendritic Cells/Lym+Mono |  |  |  | CD45+CD3-CD19-CD20-CD56- HLADR+/CD45+SSCmid | DENDRITIC CELLS | SSCmid|CD45+LIN- |HLADR+ | %Dendritic Cells/Lym+Mono | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 31.20 | % | QUANTITATIVE | NUMBER FRACTION | 31.20 | 31.20 | % | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 4 | ABC-123 | CP | ABCD-001-001 | 4 | 1 | DC | Dendritic Cells |  |  |  | CD45+CD3-CD19-CD20-CD56- HLADR+ | DENDRITIC CELLS | SSCmid|CD45+LIN- |HLADR+ | Dendritic Cells Count | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 156 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | 156 | 156 | 10^6/L | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 5 | ABC-123 | CP | ABCD-001-001 | 5 | 2 | DCPDC | DC Plasmacytoid/DC |  |  |  | CD45+CD3-CD19-CD20-CD56- HLADR+CD303+CD1c- /CD45+CD3-CD19... | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45+LIN- |HLADR+|CD303+CD1c- | %CD303+ Dendritic Cells Plasmacytoid Sub/DC | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 2.76 | % | QUANTITATIVE | NUMBER FRACTION | 2.76 | 2.76 | % | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 6 | ABC-123 | CP | ABCD-001-001 | 6 | 2 | DCP | DC Plasmacytoid |  |  |  | CD45+CD3-CD19-CD20-CD56- HLADR+CD303+CD1c- | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45+LIN- |HLADR+|CD303+CD1c- | CD303+ Dendritic Cells Plasmacytoid Sub Count | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 430 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | 430 | 430 | 10^6/L | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 7 | ABC-123 | CP | ABCD-001-001 | 7 | 2.1 | DCPSDCP | DC Plasmacytoid Sub/DC Plasmacytoid |  | ACTIVATED | CD83+ | CD45+CD3-CD19-CD20-CD56- HLADR+CD303+CD1c- CD83+/CD45+CD3... | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD303+CD1c- | %CD83+CD303+ Dendritic Cells Plasmacytoid Sub/CD303+ DCPS | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 44.50 | % | QUANTITATIVE | NUMBER FRACTION | 44.50 | 44.50 | % | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 8 | ABC-123 | CP | ABCD-001-001 | 8 | 2.1 | DCPS | DC Plasmacytoid Sub |  | ACTIVATED | CD83+ | CD45+CD3-CD19-CD20-CD56- HLADR+CD303+CD1c-CD83+ | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD303+CD1c- | CD83+CD303+ Dendritic Cells Plasmacytoid Sub Count | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 2 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | 2 | 2 | 10^6/L | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 9 | ABC-123 | CP | ABCD-001-001 | 9 | 2.1 | CD83X | CD83 Expression |  |  |  | CD83 MdFI CD45+CD3-CD19- CD20-CD56- HLADR+CD303+CD1c-CD83+ | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD303+CD1c- | CD83 Expr MdFI CD83+CD303+ Dendritic Cells Plasmacytoid Sub | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 500 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY | 500 | 500 | MdFI | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 10 | ABC-123 | CP | ABCD-001-001 | 10 | 2.1 | CD83X | CD83 Expression |  |  |  | CD83 MESF CD45+CD3-CD19- CD20-CD56- HLADR+CD303+CD1c-CD83+ | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD303+CD1c- | CD83 Expr MESF CD83+CD303+ Dendritic Cells Plasmacytoid Sub | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 2000 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 2000 | 2000 | MESF | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 11 | ABC-123 | CP | ABCD-001-001 | 11 | 2.2 | DCPSDCP | DC Plasmacytoid Sub/DC Plasmacytoid |  | ACTIVATED | CD80+ | CD45+CD3-CD19-CD20-CD56- HLADR+CD303+CD1c- CD80+/CD45+CD3... | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD303+CD1c- | %CD80+CD303+ Dendritic Cells Plasmacytoid Sub/CD303+ DCPS | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 23.20 | % | QUANTITATIVE | NUMBER FRACTION | 23.20 | 23.20 | % | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 12 | ABC-123 | CP | ABCD-001-001 | 12 | 2.2 | DCPS | DC Plasmacytoid Sub |  | ACTIVATED | CD80+ | CD45+CD3-CD19-CD20-CD56- HLADR+CD303+CD1c-CD80+ | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD303+CD1c- | CD80+CD303+ Dendritic Cells Plasmacytoid Sub Count | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 100 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | 100 | 100 | 10^6/L | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 13 | ABC-123 | CP | ABCD-001-001 | 13 | 2.2 | CD80X | CD80 Expression |  |  |  | CD80 MdFI CD45+CD3-CD19- CD20-CD56- HLADR+CD303+CD1c-CD80+ | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD303+CD1c- | CD80 Expr MdFI CD80+CD303+ Dendritic Cells Plasmacytoid Sub | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 100 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY | 100 | 100 | MdFI | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 14 | ABC-123 | CP | ABCD-001-001 | 14 | 2.2 | CD80X | CD80 Expression |  |  |  | CD80 MESF CD45+CD3-CD19- CD20-CD56- HLADR+CD303+CD1c-CD80+ | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD303+CD1c- | CD80 Expr MESF CD80+CD303+ Dendritic Cells Plasmacytoid Sub | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 400 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 400 | 400 | MESF | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 15 | ABC-123 | CP | ABCD-001-001 | 15 | 2.3 | DCPSDCP | DC Plasmacytoid Sub/DC Plasmacytoid | CD40+ |  |  | CD45+CD3-CD19-CD20-CD56- HLADR+CD303+CD1c- CD40+/CD45+CD3... | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD303+CD1c- | %CD40+CD303+ Dendritic Cells Plasmacytoid Sub/CD303+ DCPS | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 14.60 | % | QUANTITATIVE | NUMBER FRACTION | 14.60 | 14.60 | % | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 16 | ABC-123 | CP | ABCD-001-001 | 16 | 2.3 | DCPS | DC Plasmacytoid Sub | CD40+ |  |  | CD45+CD3-CD19-CD20-CD56- HLADR+CD303+CD1c-CD40+ | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD303+CD1c- | CD40+CD303+ Dendritic Cells Plasmacytoid Sub Count | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 63 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | 63 | 63 | 10^6/L | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 17 | ABC-123 | CP | ABCD-001-001 | 17 | 2.3 | CD40X | CD40 Expression |  |  |  | CD40 MdFI CD45+CD3-CD19- CD20-CD56- HLADR+CD303+CD1c-CD40+ | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD303+CD1c- | CD40 Expr MdFI CD40+CD303+ Dendritic Cells Plasmacytoid Sub | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 300 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY | 300 | 300 | MdFI | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 18 | ABC-123 | CP | ABCD-001-001 | 18 | 2.3 | CD40X | CD40 Expression |  |  |  | CD40 MESF CD45+CD3-CD19- CD20-CD56- HLADR+CD303+CD1c-CD40+ | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD303+CD1c- | CD40 Expr MESF CD40+CD303+ Dendritic Cells Plasmacytoid Sub | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 1200 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 1200 | 1200 | MESF | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 19 | ABC-123 | CP | ABCD-001-001 | 19 | 3 | DCPDC | DC Plasmacytoid/DC |  |  |  | CD45+CD3-CD19-CD20-CD56- HLADR+CD123+CD1c- /CD45+CD3-CD19... | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD123+CD1c- | %CD123+ Dendritic Cells Plasmacytoid Sub/DC | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 5.25 | % | QUANTITATIVE | NUMBER FRACTION | 5.25 | 5.25 | % | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 20 | ABC-123 | CP | ABCD-001-001 | 20 | 3 | DCP | DC Plasmacytoid |  |  |  | CD45+CD3-CD19-CD20-CD56- HLADR+CD123+CD1c- | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD123+CD1c- | CD123+ Dendritic Cells Plasmacytoid Sub Count | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 26 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | 26 | 26 | 10^6/L | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 21 | ABC-123 | CP | ABCD-001-001 | 21 | 3.1 | DCPSDCP | DC Plasmacytoid Sub/DC Plasmacytoid |  | ACTIVATED | CD83+ | CD45+CD3-CD19-CD20-CD56- HLADR+CD123+CD1c- CD83+/CD45+CD3... | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD123+CD1c- | %CD83+CD123+ Dendritic Cells Plasmacytoid Sub/CD123+ DCPS | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 30.20 | % | QUANTITATIVE | NUMBER FRACTION | 30.20 | 30.20 | % | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 22 | ABC-123 | CP | ABCD-001-001 | 22 | 3.1 | DCPS | DC Plasmacytoid Sub |  | ACTIVATED | CD83+ | CD45+CD3-CD19-CD20-CD56- HLADR+CD123+CD1c-CD83+ | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD123+CD1c- | CD83+CD123+ Dendritic Cells Plasmacytoid Sub Count | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 8 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | 8 | 8 | 10^6/L | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 23 | ABC-123 | CP | ABCD-001-001 | 23 | 3.1 | CD83X | CD83 Expression |  |  |  | CD83 MdFI CD45+CD3-CD19- CD20-CD56- HLADR+CD123+CD1c-CD83+ | DENDRITIC CELLS PLASMACYTOID | SSCmid|CD45LIN- |HLADR+|CD123+CD1c- | CD83 Expr MdFI CD83+CD123+ Dendritic Cells Plasmacytoid Sub | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 200 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY | 200 | 200 | MdFI | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 24 | ABC-123 | CP | ABCD-001-001 | 24 | 3.1 | CD83X | CD83 Expression |  |  |  | CD83 MESF CD45+CD3-CD19-CD20-CD56- HLADR+CD123+CD1c-CD83+ | DENDRITIC CELLS PLASMACYTOID | SSCmid\|CD45LIN-\|HLADR+\|CD123+CD1c- | CD83 Expr MESF CD83+CD123+ Dendritic Cells Plasmacytoid Sub | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 800 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 800 | 800 | MESF | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 25 | ABC-123 | CP | ABCD-001-001 | 25 | 3.2 | DCPSDCP | DC Plasmacytoid Sub/DC Plasmacytoid |  | ACTIVATED | CD80+ | CD45+CD3-CD19-CD20-CD56-HLADR+CD123+CD1c-CD80+/CD45+CD3-CD19-CD20-CD56-HLADR+CD123+CD1c- | DENDRITIC CELLS PLASMACYTOID | SSCmid\|CD45LIN-\|HLADR+\|CD123+CD1c- | %CD80+CD123+ Dendritic Cells Plasmacytoid Sub/CD123+ DCPS | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 15.40 | % | QUANTITATIVE | NUMBER FRACTION | 15.40 | 15.40 | % | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 26 | ABC-123 | CP | ABCD-001-001 | 26 | 3.2 | DCPS | DC Plasmacytoid Sub |  | ACTIVATED | CD80+ | CD45+CD3-CD19-CD20-CD56-HLADR+CD123+CD1c-CD80+ | DENDRITIC CELLS PLASMACYTOID | SSCmid\|CD45LIN-\|HLADR+\|CD123+CD1c- | CD80+CD123+ Dendritic Cells Plasmacytoid Sub Count | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 4 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | 4 | 4 | 10^6/L | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 27 | ABC-123 | CP | ABCD-001-001 | 27 | 3.2 | CD80X | CD80 Expression |  |  |  | CD80 MdFI CD45+CD3-CD19-CD20-CD56-HLADR+CD123+CD1c-CD80+ | DENDRITIC CELLS PLASMACYTOID | SSCmid\|CD45LIN-\|HLADR+\|CD123+CD1c- | CD80 Expr MdFI CD80+CD123+ Dendritic Cells Plasmacytoid Sub | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 50 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY | 50 | 50 | MdFI | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 28 | ABC-123 | CP | ABCD-001-001 | 28 | 3.2 | CD80X | CD80 Expression |  |  |  | CD80 MESF CD45+CD3-CD19-CD20-CD56-HLADR+CD123+CD1c-CD80+ | DENDRITIC CELLS PLASMACYTOID | SSCmid\|CD45LIN-\|HLADR+\|CD123+CD1c- | CD80 Expr MESF CD80+CD123+ Dendritic Cells Plasmacytoid Sub | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 200 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 200 | 200 | MESF | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 29 | ABC-123 | CP | ABCD-001-001 | 29 | 3.3 | DCPSDCP | DC Plasmacytoid Sub/DC Plasmacytoid | CD40+ |  |  | CD45+CD3-CD19-CD20-CD56-HLADR+CD123+CD1c-CD40+/CD45+CD3-CD19-CD20-CD56-HLADR+CD123+CD1c- | DENDRITIC CELLS PLASMACYTOID | SSCmid\|CD45LIN-\|HLADR+\|CD123+CD1c- | %CD40+CD123+ Dendritic Cells Plasmacytoid Sub/CD123+ DCPS | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 12.80 | % | QUANTITATIVE | NUMBER FRACTION | 12.80 | 12.80 | % | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 30 | ABC-123 | CP | ABCD-001-001 | 30 | 3.3 | DCPS | DC Plasmacytoid Sub | CD40+ |  |  | CD45+CD3-CD19-CD20-CD56-HLADR+CD123+CD1c-CD40+ | DENDRITIC CELLS PLASMACYTOID | SSCmid\|CD45LIN-\|HLADR+\|CD123+CD1c- | CD40+CD123+ Dendritic Cells Plasmacytoid Sub Count | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 6 | 10^6/L | QUANTITATIVE | NUMBER CONCENTRATION | 6 | 6 | 10^6/L | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 31 | ABC-123 | CP | ABCD-001-001 | 31 | 3.3 | CD40X | CD40 Expression |  |  |  | CD40 MdFI CD45+CD3-CD19-CD20-CD56-HLADR+CD123+CD1c-CD40+ | DENDRITIC CELLS PLASMACYTOID | SSCmid\|CD45LIN-\|HLADR+\|CD123+CD1c- | CD40 Expr MdFI CD40+CD123+ Dendritic Cells Plasmacytoid Sub | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 240 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY | 240 | 240 | MdFI | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |
| 32 | ABC-123 | CP | ABCD-001-001 | 32 | 3.3 | CD40X | CD40 Expression |  |  |  | CD40 MESF CD45+CD3-CD19-CD20-CD56-HLADR+CD123+CD1c-CD40+ | DENDRITIC CELLS PLASMACYTOID | SSCmid\|CD45LIN-\|HLADR+\|CD123+CD1c- | CD40 Expr MESF CD40+CD123+ Dendritic Cells Plasmacytoid Sub | IMMUNOPHENOTYPING | mDC AND pDC SUBSETS | 535 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 535 | 535 | MESF | BLOOD | FLOW CYTOMETRY | 2021-01-30T07:10:00 |

**Example 7**
This example illustrates a monocyte target occupancy assay. It demonstrates CPBDAGNT (Binding Agent) for cell surface marker binding, with three different ways to populate CPGATE/CPGATDEF.

**Row 1:** The sponsor chose to submit only the final calculated result for target occupancy. CPMRKSTR includes markers identifying the cell population (CD45+CD14+) and the target of interest (CDxx). The sponsor chose to report the penultimate gate, which does not include the target marker (CDxx). Because the target of interest is not part of the test name, it is identified in CPBDAGNT and/or CPTSTPNL.
**Row 2:** Same as row 1 except that the sponsor chose to use CPGATE and CPGATDEF to report the final gate rather than the penultimate gate. The CDxx marker is placed in front of the named portion of the gate (CDxx+ MONOCYTES).
**Row 3:** The target of interest (CD16) is also a marker needed to identify the named cell population (proinflammatory monocytes, defined as CD16+HLADRhi). Because CD16 is included in the marker set identifying the named population, it does not need to be explicitly called out in CPGATE.

*cp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPTESTCD | CPTEST | CPBDAGNT | CPMRKSTR | CPGATE | CPGATDEF | CPCAT | CPSCAT | CPTSTPNL | CPORRES | CPORRESU | CPRESSCL | CPRESTYP | CPSTRESC | CPSTRESN | CPSTRESU | CPSPEC | CPMETHOD | CPDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | CP | ABCD-001-001 | 1 | TGOCC | Target Occupancy | CDxx BINDING MOLECULE | CD45+CD14+CDxx+ | MONOCYTES | FSC SSC|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CDxx RO | 83 | % | QUANTITATIVE | NUMBER FRACTION | 83 | 83 | % | BLOOD | FLOW CYTOMETRY | 2020-07-24T09:00 |
| 2 | ABC-123 | CP | ABCD-001-001 | 1 | TGOCC | Target Occupancy | CDxx BINDING MOLECULE | CD45+CD14+CDxx+ | CDxx+ MONOCYTES | FSC SSC|CD45+CD14+|CDxx+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CDxx RO | 83 | % | QUANTITATIVE | NUMBER FRACTION | 83 | 83 | % | BLOOD | FLOW CYTOMETRY | 2020-07-24T09:00 |
| 3 | ABC-123 | CP | ABCD-001-001 | 1 | TGOCC | Target Occupancy | CD16 BINDING MOLECULE | CD45+CD14+CD16+HLADRhi | MONOCYTES, PROINFLAMMATORY | FSC SSC|CD45+CD14+|CD16+HLADRhi | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD16 RO | 83 | % | QUANTITATIVE | NUMBER FRACTION | 83 | 83 | % | BLOOD | FLOW CYTOMETRY | 2020-07-24T09:00 |

**Example 8**
This example illustrates a receptor occupancy study using a direct cell-binding assay. It demonstrates CPBDAGNT, CPTSTCND, CPREPNUM, CPCOLSRT, CPSPTSTD, and CPANMETH for direct binding assay methodology (therapeutic antibody, detection antibody, isotype controls, specific binding calculations).

**Rows 1-3:** Illustrate how CPTEST, CPMRKSTR, CPBDAGNT, CPREPNUM, and CPCOLSRT are populated for data measuring the occupancy of CDxx target protein on cytotoxic T-lymphocytes (CD45+CD3+CD8+CDxx+). CPBDAGNT identifies the CDxx antibody (therapeutic antibody). Two replicate determinations and the mean extent of CDxx bound in the unaltered specimen are indicated using CPREPNUM and CPCOLSRT.
**Rows 4-6:** Same as rows 1-3, except CPTSTCND indicates the assay was conducted under a saturating condition of CDxx antibody. Under this condition, the labeled detection antibody reflects the maximum (total) amount of CDxx available to be occupied.
**Rows 7-8:** Show values for background (non-specific) binding of the labeled detection antibody using an isotype control (IGG1 ISOTYPE), indicated in CPBDAGNT and CPMRKSTR.
**Rows 9-11:** Rows 9 and 10 show specific binding values (native specimen and saturated condition), determined by subtracting the appropriate background from the mean target bound (Row 3) and mean target total (Row 6). Row 11 shows the final CDxx antibody occupancy as the quotient of specific binding in the native specimen to specific binding measuring total CDxx available. CPANMETH populated with formulas.

*cp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPGRPID | CPTESTCD | CPTEST | CPTSTCND | CPBDAGNT | CPMRKSTR | CPGATE | CPGATDEF | CPSPTSTD | CPCAT | CPSCAT | CPTSTPNL | CPORRES | CPORRESU | CPRESSCL | CPRESTYP | CPCOLSRT | CPSTRESC | CPSTRESN | CPSTRESU | CPSPEC | CPMETHOD | CPANMETH | CPREPNUM | CPDTC | CPTPT | CPTPTNUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | CP | ABCD-001-001 | 1 | 1 | TGB | Target Bound |  | ANTI-CDxx ANTIBODY | CDxx MdFI CD45+CD3+CD8+CDxx+ | TLym Cytx | FSC SSC\|CD45+\|CD3+CD8+ | CDxx Bound Expression MdFI T-Lymphocytes Cytotoxic Rep 1 | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | CD8 T CELL CDxx RO | 24.6 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY |  | 24.6 | 24.6 | MdFI | BLOOD | FLOW CYTOMETRY |  | 1 | 2020-07-24T09:00 | CYCLE 1, DAY 1 | 1 |
| 2 | ABC-123 | CP | ABCD-001-001 | 2 | 1 | TGB | Target Bound |  | ANTI-CDxx ANTIBODY | CDxx MdFI CD45+CD3+CD8+CDxx+ | TLym Cytx | FSC SSC\|CD45+\|CD3+CD8+ | CDxx Bound Expression MdFI T-Lymphocytes Cytotoxic Rep 2 | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | CD8 T CELL CDxx RO | 31.7 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY |  | 31.7 | 31.7 | MdFI | BLOOD | FLOW CYTOMETRY |  | 2 | 2020-07-24T09:00 | CYCLE 1, DAY 1 | 1 |
| 3 | ABC-123 | CP | ABCD-001-001 | 3 | 1 | TGB | Target Bound |  | ANTI-CDxx ANTIBODY | CDxx MdFI CD45+CD3+CD8+CDxx+ | TLym Cytx | FSC SSC\|CD45+\|CD3+CD8+ | CDxx Bound Expression MdFI T-Lymphocytes Cytotoxic Mean | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | CD8 T CELL CDxx RO | 28.15 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY | MEAN | 28.15 | 28.15 | MdFI | BLOOD | CALCULATION |  |  | 2020-07-24T09:00 | CYCLE 1, DAY 1 | 1 |
| 4 | ABC-123 | CP | ABCD-001-001 | 4 | 2 | TGT | Target Total | SATURATED CONDITION WITH BINDING AGENT | ANTI-CDxx ANTIBODY | CDxx MdFI CD45+CD3+CD8+CDxx+ | TLym Cytx | FSC SSC\|CD45+\|CD3+CD8+ | CDxx Total Expression MdFI T-Lymphocytes Cytotoxic Rep 1 | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | CD8 T CELL CDxx RO | 182 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY |  | 182 | 182 | MdFI | BLOOD | FLOW CYTOMETRY |  | 1 | 2020-07-24T09:00 | CYCLE 1, DAY 1 | 1 |
| 5 | ABC-123 | CP | ABCD-001-001 | 5 | 2 | TGT | Target Total | SATURATED CONDITION WITH BINDING AGENT | ANTI-CDxx ANTIBODY | CDxx MdFI CD45+CD3+CD8+CDxx+ | TLym Cytx | FSC SSC\|CD45+\|CD3+CD8+ | CDxx Total Expression MdFI T-Lymphocytes Cytotoxic Rep 2 | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | CD8 T CELL CDxx RO | 160 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY |  | 160 | 160 | MdFI | BLOOD | FLOW CYTOMETRY |  | 2 | 2020-07-24T09:00 | CYCLE 1, DAY 1 | 1 |
| 6 | ABC-123 | CP | ABCD-001-001 | 6 | 2 | TGT | Target Total | SATURATED CONDITION WITH BINDING AGENT | ANTI-CDxx ANTIBODY | CDxx MdFI CD45+CD3+CD8+CDxx+ | TLym Cytx | FSC SSC\|CD45+\|CD3+CD8+ | CDxx Total Expression MdFI T-Lymphocytes Cytotoxic Mean | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | CD8 T CELL CDxx RO | 171 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY | MEAN | 171 | 171 | MdFI | BLOOD | CALCULATION |  |  | 2020-07-24T09:00 | CYCLE 1, DAY 1 | 1 |
| 7 | ABC-123 | CP | ABCD-001-001 | 7 |  | TGBBK | Target Bound, Background |  | IGG1 ISOTYPE | ISOTYPE MdFI CD45+CD3+CD8+CDxx+ | TLym Cytx | FSC SSC\|CD45+\|CD3+CD8+ | CDxx Isotype Control Expression MdFI T-Lymphocytes Cytotoxic | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | CD8 T CELL CDxx RO | 33.9 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY |  | 33.9 | 33.9 | MdFI | BLOOD | FLOW CYTOMETRY |  |  | 2020-07-24T09:00 | CYCLE 1, DAY 1 | 1 |
| 8 | ABC-123 | CP | ABCD-001-001 | 8 |  | TGTBK | Target Total, Background |  | IGG1 ISOTYPE | ISOTYPE MdFI CD45+CD3+CD8+CDxx+ | TLym Cytx | FSC SSC\|CD45+\|CD3+CD8+ | CDxx Isotype Control Expression MdFI T-Lymphocytes Cytotoxic | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | CD8 T CELL CDxx RO | 33.9 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY |  | 33.9 | 33.9 | MdFI | BLOOD | FLOW CYTOMETRY |  |  | 2020-07-24T09:00 | CYCLE 1, DAY 1 | 1 |
| 9 | ABC-123 | CP | ABCD-001-001 | 9 | 3 | TGBDBBK | Target Bound, Delta Bound Background |  | ANTI-CDxx ANTIBODY | CDxx MdFI CD45+CD3+CD8+CDxx+ | TLym Cytx | FSC SSC\|CD45+\|CD3+CD8+ | CDxx Delta Bound Expression MdFI T-Lymphocytes Cytotoxic | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | CD8 T CELL CDxx RO | -5.75 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY |  | -5.75 | -5.75 | MdFI | BLOOD | CALCULATION | (Target Bound mean)-(Target Bound, Background) |  | 2020-07-24T09:00 | CYCLE 1, DAY 1 | 1 |
| 10 | ABC-123 | CP | ABCD-001-001 | 10 | 3 | TGTDTBK | Target Total, Delta Total Background |  | ANTI-CDxx ANTIBODY | CDxx MdFI CD45+CD3+CD8+CDxx+ | TLym Cytx | FSC SSC\|CD45+\|CD3+CD8+ | CDxx Delta Total Expression MdFI T-Lymphocytes Cytotoxic | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | CD8 T CELL CDxx RO | 137.1 | MdFI | QUANTITATIVE | FLUORESCENCE INTENSITY |  | 137.1 | 137.1 | MdFI | BLOOD | CALCULATION | (Target Total mean)-(Target Total, Background) |  | 2020-07-24T09:00 | CYCLE 1, DAY 1 | 1 |
| 11 | ABC-123 | CP | ABCD-001-001 | 11 | 3 | TGOCC | Target Occupancy |  | ANTI-CDxx ANTIBODY | CDxx MdFI CD45+CD3+CD8+CDxx+ | TLym Cytx | FSC SSC\|CD45+\|CD3+CD8+ | % CDxx Receptor Occupancy T-Lymphocytes Cytotoxic Direct Measurement MdFI | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | CD8 T CELL CDxx RO | -4.19 | % | QUANTITATIVE | NUMBER FRACTION |  | -4.19 | -4.19 | MdFI | BLOOD | CALCULATION | (Target Bound, Delta Bound Background)*100/(Target Total, Delta Total Background) |  | 2020-07-24T09:00 | CYCLE 1, DAY 1 | 1 |

**Example 9**
This example illustrates a monocyte receptor occupancy indirect detection assay with CPABCLID (Antibody Clone Identifier), competitive/non-competitive probes (HA5-PE and 2D4-APC), saturating conditions, and background subtraction.

**Row 1:** The sponsor chose to submit only the final calculated result for target occupancy. CPMRKSTR includes markers identifying the cell population (CD45+CD14+) and the target of interest (CD99). The sponsor chose to report the penultimate gate. Because the target of interest is not part of the test name, it is identified using CPBDAGNT and/or CPTSTPNL.
**Rows 2-7:** Baseline (PREDOSE) measurements. Rows 2-4 show results for free target using labeled competitive antibody probe (HA5). Rows 5-7 show results for total CD99 using labeled non-competitive antibody probe (2D4). CPBLFL="Y" marks baseline measurements (rows 2 and 5). CPTSTCND captures saturated condition for background binding (rows 3 and 6). CPGRPID groups individual measured tests to calculated values. CPTPT and CPTPTNUM provide time point information.
**Rows 8-14:** Show the same set of tests collected for baseline (rows 2-7) but measured 24 hours after treatment with the therapeutic drug. Row 14 shows the final calculated receptor occupancy at the 24-hour post-treatment time point relative to pre-dose. CPANMETH populated with formula.

*cp.xpt*

| Row | STUDYID | DOMAIN | USUBJID | CPSEQ | CPGRPID | CPTESTCD | CPTEST | CPTSTCND | CPBDAGNT | CPABCLID | CPMRKSTR | CPGATE | CPGATDEF | CPCAT | CPSCAT | CPTSTPNL | CPORRES | CPORRESU | CPRESSCL | CPRESTYP | CPSTRESC | CPSTRESN | CPSTRESU | CPSPEC | CPMETHOD | CPANMETH | CPBLFL | CPDTC | CPTPT | CPTPTNUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CA123-456 | CP | 000100001 | 1 |  | TGOCC | Target Occupancy |  | CD99 BINDING DRUG |  | CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 85 | % | QUANTITATIVE | NUMBER FRACTION | 83 | 83 | % | BLOOD | FLOW CYTOMETRY |  |  | 2019-07-24T09:00 |  |  |
| 2 | CA123-456 | CP | 000100001 | 1 | 1 | TGF | Target Free |  | ANTI-CD99 ANTIBODY | HA5 | CD99 CLONE HA5 AB MESF CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 5023 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 5023 | 5023 | MESF | BLOOD | FLOW CYTOMETRY |  | Y | 2019-07-23T09:00 | PREDOSE | 1 |
| 3 | CA123-456 | CP | 000100001 | 2 | 1 | TGFBK | Target Free, Background | SATURATED CONDITION WITH BINDING AGENT | UNLABELED ANTI-CD99 ANTIBODY | HA5 | CD99 CLONE HA5 AB MESF CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 225 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 225 | 225 | MESF | BLOOD | FLOW CYTOMETRY |  |  | 2019-07-23T09:00 | PREDOSE | 1 |
| 4 | CA123-456 | CP | 000100001 | 3 | 1 | TGFDFBK | Target Free, Delta Free Background |  | ANTI-CD99 ANTIBODY | HA5 | CD99 CLONE HA5 AB MESF CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 4798 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 4798 | 4798 | MESF | BLOOD | CALCULATION | (Target Free)-(Target Free, Background) |  | 2019-07-23T09:00 | PREDOSE | 1 |
| 5 | CA123-456 | CP | 000100001 | 4 | 2 | TGT | Target Total |  | ANTI-CD99 ANTIBODY | 2D4 | CD99 CLONE 2D4 AB MESF CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 7550 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 7550 | 7550 | MESF | BLOOD | FLOW CYTOMETRY |  | Y | 2019-07-23T09:00 | PREDOSE | 1 |
| 6 | CA123-456 | CP | 000100001 | 5 | 2 | TGTBK | Target Total, Background | SATURATED CONDITION WITH BINDING AGENT | UNLABELED ANTI-CD99 ANTIBODY | 2D4 | CD99 CLONE 2D4 AB MESF CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 297 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 297 | 297 | MESF | BLOOD | FLOW CYTOMETRY |  |  | 2019-07-23T09:00 | PREDOSE | 1 |
| 7 | CA123-456 | CP | 000100001 | 6 | 2 | TGTDTBK | Target Total, Delta Total Background |  | ANTI-CD99 ANTIBODY | 2D4 | CD99 CLONE 2D4 AB MESF CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 7253 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 7253 | 7253 | MESF | BLOOD | CALCULATION | (Target Total)-(Target Total, Background) |  | 2019-07-23T09:00 | PREDOSE | 1 |
| 8 | CA123-456 | CP | 000100001 | 1 | 1 | TGF | Target Free |  | ANTI-CD99 ANTIBODY | HA5 | CD99 CLONE HA5 AB MESF CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 1100 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 1100 | 1100 | MESF | BLOOD | FLOW CYTOMETRY |  |  | 2019-07-24T09:00 | 24h POSTDOSE | 2 |
| 9 | CA123-456 | CP | 000100001 | 2 | 1 | TGFBK | Target Free, Background | SATURATED CONDITION WITH BINDING AGENT | UNLABELED ANTI-CD99 ANTIBODY | HA5 | CD99 CLONE HA5 AB MESF CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 282 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 282 | 282 | MESF | BLOOD | FLOW CYTOMETRY |  |  | 2019-07-24T09:00 | 24h POSTDOSE | 2 |
| 10 | CA123-456 | CP | 000100001 | 3 | 1 | TGFDFBK | Target Free, Delta Free Background |  | ANTI-CD99 ANTIBODY | HA5 | CD99 CLONE HA5 AB MESF CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 818 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 818 | 818 | MESF | BLOOD | CALCULATION | (Target Free)-(Target Free, Background) |  | 2019-07-24T09:00 | 24h POSTDOSE | 2 |
| 11 | CA123-456 | CP | 000100001 | 4 | 2 | TGT | Target Total |  | ANTI-CD99 ANTIBODY | 2D4 | CD99 CLONE 2D4 AB MESF CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 7530 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 7530 | 7530 | MESF | BLOOD | FLOW CYTOMETRY |  |  | 2019-07-24T09:00 | 24h POSTDOSE | 2 |
| 12 | CA123-456 | CP | 000100001 | 5 | 2 | TGTBK | Target Total, Background | SATURATED CONDITION WITH BINDING AGENT | UNLABELED ANTI-CD99 ANTIBODY | 2D4 | CD99 CLONE 2D4 AB MESF CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 295 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 295 | 295 | MESF | BLOOD | FLOW CYTOMETRY |  |  | 2019-07-24T09:00 | 24h POSTDOSE | 2 |
| 13 | CA123-456 | CP | 000100001 | 6 | 2 | TGTDTBK | Target Total, Delta Total Background |  | ANTI-CD99 ANTIBODY | 2D4 | CD99 CLONE 2D4 AB MESF CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 7235 | MESF | QUANTITATIVE | FLUORESCENCE INTENSITY | 7235 | 7235 | MESF | BLOOD | CALCULATION | (Target Total)-(Target Total, Background) |  | 2019-07-24T09:00 | 24h POSTDOSE | 2 |
| 14 | CA123-456 | CP | 000100001 | 7 |  | TGOCC | Target Occupancy |  | CD99 BINDING DRUG |  | CD45+CD14+CD99+ | MONOCYTES | FSC SSC\|CD45+CD14+ | TARGET ENGAGEMENT | RECEPTOR OCCUPANCY | MONOCYTE CD99 RO | 83 | % | QUANTITATIVE | NUMBER FRACTION | 83 | 83 | % | BLOOD | CALCULATION | ((Target Free, Delta Free Background at T1)-(Target Free, Delta Free Background at T2))/(Target Free, Delta Free Background at T1) |  | 2019-07-24T09:00 | 24h POSTDOSE | 2 |

