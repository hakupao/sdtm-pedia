# NV — Assumptions

## §6.3.7 Morphology/Physiology Domains — Overview

Individual domains for morphology and physiology findings about specific body systems are grouped together in this section. This grouping is not meant to imply that there is a single morphology/physiology domain. Additional domains for other body systems are expected to be added in future versions of the SDTMIG. The CDISC Controlled Terminology of SDTM domain abbreviations and the therapeutic area user guides may have examples of other body system domains that are not yet in the SDTMIG.

## §6.3.7.1 Generic Morphology/Physiology Specification

This section describes properties common to all the body system-based morphology/physiology domains.

- The SDTMIG includes several domains for physiology and morphology findings for different body systems. These differ only in body system, in domain code, and in informative content such as examples.
- In the partial generic domain specification table, "--" is used as a placeholder. In each individual body system-based morphology/physiology domain specification, this placeholder is replaced by the appropriate domain code.
- The variables included in the generic morphology/physiology domain specification table are those required or expected in the individual body system-based morphology/physiology domains. Individual morphology/physiology domains may included additional expected variables. All other variables allowed in findings domains are allowed in the body system-based morphology/physiology domains
- All body system-based physiology/morphology domains share the same structure, provided here. Although time point is not in the structure, it can be included in the structure of a particular domain if time point variables were included in the data represented.
- CDISC Controlled Terminology includes codelists for TEST and TESTCD values for each body-system based domain.

**--.xpt, Body System-Based Morphology/Physiology — Findings, Version 3.3. One record per finding per visit per subject, Tabulation.**

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format¹ | Role | CDISC Notes | Core |
|--------------|----------------|------|---------------------------------------|------|-------------|------|
| STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | -- | Identifier | Two-character abbreviation for the domain. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. | Req |
| --SEQ | Sequence Number | Num | | Identifier | Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1. | Req |
| --TESTCD | Short Name of Measurement, Test or Exam | Char | * | Topic | Short character value for --TEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Subject to Domain-specific test code controlled terminology. | Req |
| --TEST | Name of Measurement, Test or Examination | Char | * | Synonym Qualifier | Long name for --TESTCD. Subject to Domain-specific test code controlled terminology. | Req |
| --ORRES | Result or Finding in Original Units | Char | | Result Qualifier | Result of the measurement or finding as originally received or collected. | Exp |
| --STRESC | Result or Finding in Standard Format | Char | | Result Qualifier | Contains the result value for all findings, copied or derived from --ORRES in a standard format or in standard units. --STRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in --STRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in --ORRES, and these results effectively have the same meaning, they could be represented in standard format in --STRESC as "NEGATIVE". | Exp |
| --LOBXFL | Last Observation Before Exposure Flag | Char | | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. | Exp |
| VISITNUM | Visit Number | Num | | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. | Exp |
| --DTC | Date/Time of Collection | Char | ISO 8601 datetime or interval | Timing | Collection date and time of an observation. | Exp |
| --DY | Study Day of Collection | Num | | Timing | Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. | Exp |

> ¹In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

## NV – Description/Overview

A findings domain that contains physiological and morphological findings related to the nervous system, including the brain, spinal cord, the cranial and spinal nerves, autonomic ganglia and plexuses.

## NV – Specification

nv.xpt, Nervous System Findings — Findings. One record per finding per location per time point per visit per subject, Tabulation.

## NV – Assumptions

1. Methods of assessment for nervous system findings may include nerve conduction studies, electroencephalogram (EEG), electromyography (EMG), and imaging.

2. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the NV domain, but the following qualifiers would not generally be used: --MODIFY, --BODSYS, --LOINC, --TOX, --TOXGR.
