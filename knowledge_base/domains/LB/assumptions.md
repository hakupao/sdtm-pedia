# LB — Assumptions

## §6.3.5 Specimen-based Findings Domains

Individual domains (e.g., IS, LB, MB) for laboratory measurements, tests, or examinations performed on collected biological specimens (e.g., blood, urine, tumor tissue) are grouped together in this section. This grouping is not meant to imply that there is a single laboratory domain for all test methodologies. Additional laboratory domains are expected to be added in future versions.

## §6.3.5.1 Generic Specimen-based Lab Findings Domain Specification

This section describes variables commonly used in specimen-based laboratory domains (e.g., IS, LB, MB/MS, MI, PC/PP).

- The SDTMIG includes several domains for representing clinical pathology laboratory measurements, tests, and examinations supporting safety and/or efficacy analyses. Each domain is defined to group measures of a common topic (e.g., microbiology susceptibility, microscopic findings, pharmacokinetic concentrations).
- In the generic lab domain specification table that follows, "--" is used as a placeholder. In each individual laboratory findings domain specification, it is replaced by the appropriate domain code.
- The variables in the generic domain specification table include required, expected, and permissible variables typically used across specimen-based laboratory findings domains to uniquely describe a measurement, test, or examination of a biological specimen.
  - Individual domains include additional variables with specific Controlled Terminology codelists and domain-specific Core values.
  - The Findings general observation class includes additional permissible variables that may be added when representing specimen-based laboratory findings.
  - Permissible identifier and timing variables may be added to represent details (e.g., identifiers to describe related records, planned time points, actual timing).

**--.xpt, Generic Specimen-Based Laboratory Findings — Findings, Version 1.0. One record per finding per visit per subject, Tabulation.**

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format¹ | Role | CDISC Notes | Core |
|--------------|----------------|------|---------------------------------------|------|-------------|------|
| STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | -- | Identifier | Two-character abbreviation for the domain. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. | Req |
| --SEQ | Sequence Number | Num | | Identifier | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. | Req |
| --GRPID | Group ID | Char | | Identifier | Optional group identifier, used to link together a block of related records within a subject in a domain. | Perm |
| --REFID | Reference ID | Char | | Identifier | Optional internal or external identifier (e.g., lab specimen ID). | Perm |
| --TESTCD | Short Name of Measurement, Test or Exam | Char | * | Topic | Short character value for --TEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Subject to domain-specific test code controlled terminology. | Req |
| --TEST | Name of Measurement, Test or Exam | Char | * | Synonym Qualifier | Long name for --TESTCD. Subject to domain-specific test code controlled terminology. | Req |
| --CAT | Category | Char | * | Grouping Qualifier | Used to define a category of topic-variable values. | Perm |
| --SCAT | Subcategory | Char | * | Grouping Qualifier | Used to define a further categorization of --CAT values. | Perm |
| --ORRES | Result or Finding in Original Units | Char | | Result Qualifier | Result of the measurement or finding as originally received or collected. | Exp |
| --ORRESU | Original Units | Char | * | Variable Qualifier | Unit for --ORRES and --ORREF. Subject to domain-specific test code controlled terminology. | Perm |
| --LLOD | Lower Limit of Detection | Char | | Variable Qualifier | The lowest threshold (as originally received or collected) for reliably detecting the presence or absence of substance measured by a specific test. The value for the field will be as described in documentation from the instrument or lab vendor. | Perm |
| --STRESC | Result or Finding in Standard Format | Char | | Result Qualifier | Contains the result value for all findings copied or derived from --ORRES, in a standard format or in standard units. --STRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in --STRESN. | Exp |
| --STRESN | Numeric Result/Finding in Standard Units | Num | | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from --STRESC. --STRESN should store all numeric test results or findings. | Perm |
| --STRESU | Standard Units | Char | * | Variable Qualifier | Standardized units used for --STRESC, --STRESN, --STREFC, and --STREFN. Subject to domain-specific test code controlled terminology. | Perm |
| --STAT | Completion Status | Char | * | Record Qualifier | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". | Perm |
| --REASND | Reason Not Done | Char | | Record Qualifier | Reason not done. Used in conjunction with --STAT when value is "NOT DONE". | Perm |
| --NAM | Laboratory/Vendor Name | Char | * | Record Qualifier | Name or identifier of the vendor (e.g., laboratory) that provided the test results. | Perm |
| --SPEC | Specimen Material Type | Char | * | Record Qualifier | Defines the type of specimen used for a measurement. Subject to domain-specific test code controlled terminology. | Perm |
| --METHOD | Method of Test or Examination | Char | * | Record Qualifier | Method of the test or examination. Subject to domain-specific test code controlled terminology. | Perm |
| --LOBXFL | Last Observation Before Exposure Flag | Char | * | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. | Perm |
| --LLOQ | Lower Limit of Quantitation | Num | | Variable Qualifier | Indicates the lower limit of quantitation for an assay. Units will be those used for --STRESU. | Perm |
| --ULOQ | Upper Limit of Quantitation | Num | | Variable Qualifier | Indicates the upper limit of quantitation for an assay. Units will be those used for --STRESU. | Perm |
| VISITNUM | Visit Number | Num | | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. | Perm |
| VISIT | Visit Name | Char | | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. | Perm |
| VISITDY | Planned Study Day of Visit | Num | | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. | Perm |
| --DTC | Date/Time of Collection | Char | ISO 8601 datetime or interval | Timing | Collection date and time of an observation. | Perm |
| --DY | Study Day of Collection | Num | | Timing | Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. | Perm |

> ¹In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

## LB – Description/Overview

A findings domain that contains laboratory test data such as hematology, clinical chemistry and urinalysis. This domain does not include microbiology or pharmacokinetic data, which are stored in separate domains.

## LB – Specification

lb.xpt, Laboratory Test Results — Findings. One record per lab test per time point per visit per subject, Tabulation.

## LB – Assumptions

1. This domain captures laboratory data collected on the CRF or received from a central provider or vendor.

2. For lab tests that do not have continuous numeric results (e.g., urine protein as measured by dipstick, descriptive tests such as urine color), LBSTNRC could be populated either with normal range values that are a range of character values for an ordinal scale (e.g., “NEGATIVE to TRACE") or a delimited set of values that are considered to be normal (e.g., “YELLOW”, “AMBER”). LBORNRLO, LBORNRHI, LBSTNRLO, and LBSTNRHI should be null for these types of tests.

3. LBNRIND can be added to indicate where a result falls with respect to reference range defined by LBORNRLO and LBORNRHI. Examples: "HIGH", "LOW". If toxicity grading is available, values would be represented in the variables LBTOX and LBTOXGR. Clinical significance would be represented as described in Section 4.5.5, Clinical Significance for Findings Observation Class Data, in LBCLSIG (see also LB Example 1).

4. For lab tests where the specimen is collected over time (e.g., 24-hour urine collection), the start date/time of the collection goes into LBDTC and the end date/time of collection goes into LBENDTC. See Section 4.4.8, Date and Time Reported in a Domain Based on Findings.

5. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the LB domain, but the following qualifiers would not generally be used: --BODSYS, --SEV.

6. A value derived by a central lab according to its procedures is considered collected rather than derived. See Section 4.1.8.1, Origin Metadata for Variables.

7. The variable LBORRESU uses the UNIT codelist. This means that sponsors should be submitting a term from the CDISC Submission Value column in the published Controlled Terminology List that is maintained for CDISC by NCI EVS. When sponsors have units that are not in this column, they should first check to see if their unit is mathematically synonymous with an existing/published unit from the UNIT codelist and submit their lab values using the published CDISC submission value. Example: "g/L" and "mg/mL" are mathematically synonymous, but only "g/L" is the submission value in the CDISC Unit codelist. If this is not the case, the unit must be added as a codelist extensible value in the Define.xml, and a new-term request must be submitted.
   a. CDISC Controlled Terminology Rules for Lab and Unit are available at https://www.cdisc.org/standards/terminology/controlled-terminology.

8. The LBLOINC variable contains a code from the Logical Observation Identifiers Names and Codes (LOINC) database that identifies a specific laboratory test. The LOINC to LB Mapping Codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology, may be used to identify appropriate CDISC CT values for a test with a particular LOINC code. In addition to LBTEST, LBSPEC, LBMETHOD, and LBORRESU, the aspects of a test that are associated with a LOINC code may be represented in the variables LBTPT, LBANMETH, LBPOS, LBLOC, LBFAST, LBTSTCND, LBBDAGNT, LBTSTOPO, LBRESSCL, LBRESTYP, LBCOLSRT, LBLLOD, LBPTFL, and LBPDUR. These additional variables are only required to be populated when necessary to provide a semantically meaningful distinction between records with different LBLOINC values.
