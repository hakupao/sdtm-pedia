# 25_td_meta_ti_ts_oi

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `25`
> - **Concept**: Trial Design: TI + TS + OI (inclusion + summary + organism)
> - **Merged files**: 9
> - **Words**: 7,498
> - **Chars**: 41,399
> - **Sources**:
>   - `domains/TI/spec.md`
>   - `domains/TI/assumptions.md`
>   - `domains/TI/examples.md`
>   - `domains/TS/spec.md`
>   - `domains/TS/assumptions.md`
>   - `domains/TS/examples.md`
>   - `domains/OI/spec.md`
>   - `domains/OI/assumptions.md`
>   - `domains/OI/examples.md`

---
## Source: `domains/TI/spec.md`

# TI — Trial Inclusion/Exclusion Criteria

> Class: Trial Design | Structure: One record per I/E criterion

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### IETESTCD
- **Order:** 3
- **Label:** Incl/Excl Criterion Short Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name IETEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). IETESTCD cannot contain characters other than letters, numbers, or underscores. The prefix "IE" is used to ensure consistency with the IE domain.

### IETEST
- **Order:** 4
- **Label:** Inclusion/Exclusion Criterion
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Full text of the inclusion or exclusion criterion. The prefix "IE" is used to ensure consistency with the IE domain.

### IECAT
- **Order:** 5
- **Label:** Inclusion/Exclusion Category
- **Type:** Char
- **Controlled Terms:** C66797
- **Role:** Grouping Qualifier
- **Core:** Req
- **CDISC Notes:** Used for categorization of the inclusion or exclusion criteria.

### IESCAT
- **Order:** 6
- **Label:** Inclusion/Exclusion Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the exception criterion. Can be used to distinguish criteria for a sub-study or to categorize as major or minor exceptions. Examples: "MAJOR", "MINOR".

### TIRL
- **Order:** 7
- **Label:** Inclusion/Exclusion Criterion Rule
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Perm
- **CDISC Notes:** Rule that expresses the criterion in computer-executable form. See Assumption 4.

### TIVERS
- **Order:** 8
- **Label:** Protocol Criteria Versions
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The number of this version of the Inclusion/Exclusion criteria. May be omitted if there is only 1 version.
---

## Cross References

### Controlled Terminology
- [Category of Inclusion/Exclusion (C66797)](../../terminology/core/general_part2.md) — IECAT

### Related Domains
- **Same class (Trial Design):** TA, TD, TE, TM, TS, TV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)

## Source: `domains/TI/assumptions.md`

# TI — Assumptions

The variable TIRL was included in the Trial Inclusion/Exclusion Criteria (TI) domain in anticipation of developing a way to represent eligibility criteria in a computer-executable manner. However, such a method has not been developed, and it is not clear that an SDTM dataset would be the best place to represent such a computer-executable representation.

TI contains all the inclusion and exclusion criteria for the trial, and thus provides information that may not be present in the subject-level data on inclusion and exclusion criteria. The IE domain (described in Section 6.3.4, Inclusion/Exclusion Criteria Not Met) contains records only for inclusion and exclusion criteria that subjects did not meet.

1. If inclusion/exclusion criteria were amended during the trial, then each complete set of criteria must be included in the TI domain. TIVERS is used to distinguish between the versions.

2. Protocol version numbers should be used to identify criteria versions, although there may be more versions of the protocol than versions of the inclusion/exclusion criteria. For example, a protocol might have versions 1, 2, 3, and 4, but if the inclusion/exclusion criteria in version 1 were unchanged through versions 2 and 3, and changed only in version 4, then there would be 2 sets of inclusion/exclusion criteria in TI: one for version 1 and one for version 4.

3. Individual criteria do not have versions. If a criterion changes, it should be treated as a new criterion, with a new value for IETESTCD. If criteria have been numbered and values of IETESTCD are generally of the form INCL00n or EXCL00n, and new versions of a criterion have not been given new numbers, separate values of IETESTCD might be created by appending letters (e.g., INCL003A, INCL003B).

4. IETEST contains the text of the inclusion/exclusion criterion. However, because entry criteria are rules, the variable TIRL has been included in anticipation of the development of computer-executable rules.

5. If a criterion text is <200 characters, it goes in IETEST; if the text is >200 characters, put meaningful text in IETEST and describe the full text in the study metadata. See Section 4.5.3.1, Test Name (--TEST) Greater than 40 Characters, for further information.

## Source: `domains/TI/examples.md`

# TI — Examples

## Example 1

This example shows records for a trial with 2 versions of inclusion/exclusion criteria.

**Rows 1-3:** Show the 2 inclusion criteria and 1 exclusion criterion for version 1 of the protocol.

**Rows 4-6:** Show the inclusion/exclusion criteria for version 2.2 of the protocol, which changed the minimum age for entry from 21 to 18.

**ti.xpt**

| Row | STUDYID | DOMAIN | IETESTCD | IETEST | IECAT | TIVERS |
|-----|---------|--------|----------|--------|-------|--------|
| 1 | XYZ | TI | INCL01 | Has disease under study | INCLUSION | 1 |
| 2 | XYZ | TI | INCL02 | Age 21 or greater | INCLUSION | 1 |
| 3 | XYZ | TI | EXCL01 | Pregnant or lactating | EXCLUSION | 1 |
| 4 | XYZ | TI | INCL01 | Has disease under study | INCLUSION | 2.2 |
| 5 | XYZ | TI | INCL02A | Age 18 or greater | INCLUSION | 2.2 |
| 6 | XYZ | TI | EXCL01 | Pregnant or lactating | EXCLUSION | 2.2 |

## Source: `domains/TS/spec.md`

# TS — Trial Summary

> Class: Trial Design | Structure: One record per trial summary parameter value

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### TSSEQ
- **Order:** 3
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness within a parameter. Allows inclusion of multiple records for the same TSPARMCD.

### TSGRPID
- **Order:** 4
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a group of related records.

### TSPARMCD
- **Order:** 5
- **Label:** Trial Summary Parameter Short Name
- **Type:** Char
- **Controlled Terms:** C66738
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** TSPARMCD (the companion to TSPARM) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that TSPARMCD will need to serve as variable names. Examples: "AGEMIN", "AGEMAX".

### TSPARM
- **Order:** 6
- **Label:** Trial Summary Parameter
- **Type:** Char
- **Controlled Terms:** C67152
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Term for the trial summary parameter. The value in TSPARM cannot be longer than 40 characters. Examples: "Planned Minimum Age of Subjects", "Planned Maximum Age of Subjects".

### TSVAL
- **Order:** 7
- **Label:** Parameter Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Value of TSPARM. Example: "ASTHMA" when TSPARM value is "Trial Indication". TSVAL can only be null when TSVALNF is populated. Text over 200 characters can be added to additional columns TSVAL1-TSVALn. See Assumption 8.

### TSVALNF
- **Order:** 8
- **Label:** Parameter Value Null Flavor
- **Type:** Char
- **Controlled Terms:** ISO 21090 NullFlavor
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Null flavor for the value of TSPARM, to be populated only if TSVAL is null.

### TSVALCD
- **Order:** 9
- **Label:** Parameter Value Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** This is the code of the term in TSVAL. For example, "6CW7F3G59X" is the code for gabapentin; "C49488" is the code for Y. The length of this variable can be longer than 8 to accommodate the length of the external terminology.

### TSVCDREF
- **Order:** 10
- **Label:** Name of the Reference Terminology
- **Type:** Char
- **Controlled Terms:** C66788
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** The name of the reference terminology from which TSVALCD is taken. For example; CDISC CT, SNOMED, ISO 8601.

### TSVCDVER
- **Order:** 11
- **Label:** Version of the Reference Terminology
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** The version number of the reference terminology, if applicable.
---

## Cross References

### Controlled Terminology
- [Trial Summary Parameter Test Code (C66738)](../../terminology/core/trial_design.md) — TSPARMCD
- [Dictionary Name (C66788)](../../terminology/core/trial_design.md) — TSVCDREF
- [Trial Summary Parameter Test Name (C67152)](../../terminology/core/trial_design.md) — TSPARM

### Related Domains
- **Same class (Trial Design):** TA, TD, TE, TI, TM, TV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)

## Source: `domains/TS/assumptions.md`

# TS — Assumptions

The Trial Summary (TS) dataset allows the sponsor to submit a summary of the trial in a structured format. Each record in the TS dataset contains the value of a parameter, a characteristic of the trial. For example, TS is used to record basic information about the study such as trial phase, protocol title, and trial objectives. The TS dataset contains information about the planned and actual trial characteristics.

1. The intent of this dataset is to provide a summary of trial information. This is not subject-level data.

2. Recipients may specify their requirements for which trial summary parameters should be included under which conditions. For example, the US FDA includes such information in their Study Data Technical Conformance Guide.

3. The order of parameters in the examples of TS datasets should not be taken as a requirement. There are no requirements or expectations about the order of parameters within the TS dataset.

4. The method for treating text >200 characters in TS is similar to that used for the Comments (CO) special-purpose domain (Section 5.1, Comments). If TSVAL is >200 characters, then it should be split into multiple variables, TSVAL-TSVALn. See Section 4.5.3.2, Text Strings Greater than 200 Characters in Other Variables.

5. A list of values for TSPARM and TSPARMCD can be found in CDISC Controlled Terminology, available at https://www.cancer.gov/research/resources/terminology/cdisc.

6. Controlled terminology for TSPARM is extensible. The meaning of any added parameters should be explained in the metadata for the TS dataset.

7. For a particular trial summary parameter, responses (values in TSVAL) may be numeric, datetimes or amounts of time represented in ISO8601 format, or text. For some parameters, textual responses may be taken from controlled terminology; for others, responses may be free text.

8. For some trial summary parameters, CDISC Controlled Terminology includes codelists for use with TSVAL. The associations between trial summary parameters and response codelists are in the TS codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology. Recipients may also specify controlled terminology for TSVAL. These specifications may be for trial summary parameters for which there is no CDISC Controlled Terminology or they may replace CDISC Controlled Terminology for a trial summary parameter. For example, the US FDA Data Standards Catalog includes terminologies to be used for certain trial summary parameters.

9. There is a code value for TSVALCD only when there is controlled terminology for TSVAL. For example, when TSPARMCD = "PLANSUB" (Planned Number of Subjects) or TSPARMCD = "TITLE" (Trial Title), then TSVALCD will be null.

10. TSVALNF contains a "null flavor," a value that provides additional coded information when TSVAL is null. For example, for TSPARM = "AGEMAX" (Planned Maximum Age of Subjects), there is no value if a study does not specify a maximum age. In this case, the appropriate null flavor is "PINF", which stands for "positive infinity." In a clinical pharmacology study conducted in healthy volunteers for a drug where indications are not yet established, the appropriate null flavor for TSPARM = "INDIC" (Trial Disease/Condition Indication) would be "NA" (i.e., not applicable). TSVALNF can also be used in a case where the value of a particular parameter is unknown.

11. Some codelists used for TSVAL include terms which are also null flavors. For example, the Pharmaceutical Dosage Form codelist includes the values "UNKNOWN" and "NOT APPLICABLE". In such cases, TSVAL should have the term from the codelist and TSVALNF should be null.

12. For some trials, there will be multiple records in the TS dataset for a single parameter. For example, a trial that addresses both safety and efficacy could have 2 records with TSPARMCD = "TTYPE" (Trial Type), one with the TSVAL = "SAFETY" and the other with TSVAL = "EFFICACY". TSSEQ has a different value for each record for the same parameter.

    Note that this is different from datasets that contain subject data, where the --SEQ variable has a different value for each record for the same subject.

13. TS does not contain subject-level data, so there is no restriction analogous to the requirement in subject-level datasets that the blocks bound by TSGRPID are within a subject. TSGRPID can be used to tie together any block of records in the TS dataset. TSGRPID is most likely to be used when the TS dataset includes multiple records for the same parameter.

    For example, if a trial compared administration of a total daily dose given once a day to that dose split over 2 administrations, the TS dataset might include the following records. There are 2 records each for TSPARMCD = "Dose" and TSPARMCD = "DOSFREQ". Records with the same TSGRPID are associated with each other. In this example, dose units are the same for both administration schedules, so only 1 record for DOSU is needed.

    | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL |
    |-------|---------|----------|--------|-------|
    | 1 | A | DOSE | Dose per Administration | 50 |
    | 1 | A | DOSFREQ | Dosing Frequency | BID |
    | 2 | B | DOSE | Dose per Administration | 100 |
    | 2 | B | DOSFREQ | Dosing Frequency | Q24H |
    | 1 | | DOSU | Dose Units | mg |

14. Protocols vary in how they describe objectives. If the protocol does not provide information about which objectives meet the definition of TSPARM = "OBJPRIM" (Trial Primary Objective; i.e., the principal purpose of the trial), then the objectives should be provided as values of TSPARM = "OBJPRIM". Consult the controlled terminology for trial summary parameters for appropriate parameter values for representing other objective designations (e.g., secondary, exploratory).

15. As per the definitions, the primary outcome measure is associated with the primary objective, the secondary outcome measure is associated with the secondary objective, and the exploratory outcome measure is associated with the exploratory objective. It is possible for the same outcome measure to be associated with more than 1 objective. For example, 2 objectives could use the same outcome measure at different time points, or using different analysis methods.

16. If a primary objective is assessed by means of multiple outcome measures, then all of these outcome measures should be provided as values of TSPARM = "OUTMSPR" (Primary Outcome Measure). Similarly, all outcome measures used to assess secondary objectives should be provided as values of TSPARM = "OUTMSSEC" (Secondary Outcome Measure), and all outcome measures used to assess exploratory objectives should be provided as values of TSPARM = "OUTMSEXP" (Exploratory Outcome Measure). Additional key measures of a study that are not designated as primary, secondary, or exploratory should be provided as values of TSPARM = "OUTMSADD" (Additional Outcome Measure).

17. Trial indication: Values for TSVAL when TSPARMCD = "INDIC" would indicate the condition, disease, or disorder the trial is intended to investigate or address. A vaccine study of healthy subjects, with the intended purpose of preventing influenza infection, would have TSVAL = "Influenza". A clinical pharmacology study of healthy volunteers, with the purpose of collecting pharmacokinetic data, would have TSVAL be null and TSVALNF = "NA" if TS contains a row where TSPARMCD = "INDIC".

18. Values for TSVAL when TSPARMCD = "REGID" (Registry Identifier) will be identifiers assigned by the registry (e.g., ClinicalTrials.gov, EudraCT).

### Use of Null Flavor

The variable TSVALNF is based on the idea of a "null flavor" as embodied in the ISO 21090 standard. A null flavor is an ancillary piece of data that provides additional information when its primary piece of data is null (has a missing value). There is controlled terminology for the null flavor data item which includes such familiar values as "Unknown", "Other", and "Not Applicable" among its 14 terms.

The controlled terminology for null flavor, which supersedes Appendix C1, Supplemental Qualifiers Name Codes, is included below.

**NullFlavor Enumeration (OID: 2.16.840.1.113883.5.1008)**

| Rank | Code | Display Name | Definition |
|------|------|---|---|
| 1 | NI | No information | The value is exceptional (i.e., missing, omitted, incomplete, improper). No information as to the reason for being an exceptional value is provided. This is the most general exceptional value. It is also the default exceptional value. |
| 2 | INV | Invalid | The value as represented in the instance is not a member of the set of permitted data values in the constrained value domain of a variable. |
| 3 | OTH | Other | The actual value is not a member of the set of permitted data values in the constrained value domain of a variable (e.g., concept not provided by required code system). |
| 4 | PINF | Positive infinity | Positive infinity of numbers |
| 4 | NINF | Negative infinity | Negative infinity of numbers |
| 3 | UNC | Unencoded | No attempt has been made to encode the information correctly, but the raw source information is represented (usually in original Text). |
| 3 | DER | Derived | An actual value may exist, but it must be derived from the information provided (usually an expression is provided directly). |
| 2 | UNK | Unknown | A proper value is applicable, but not known. |
| 3 | ASKU | Asked but unknown | Information was sought but not found (e.g., patient was asked but didn't know). |
| 4 | NAV | Temporarily unavailable | Information is not available at this time, but is expected to be available later. |
| 3 | NASK | Not asked | This information has not been sought (e.g., patient was not asked). |
| 3 | QS | Sufficient quantity | The specific quantity is not known, but is known to be non-zero and is not specified because it makes up the bulk of the material. For example, if directions said, "Add 10 mg of ingredient X, 50 mg of ingredient Y, and sufficient quantity of water to 100 ml", the null flavor "QS" would be used to express the quantity of water. |
| 3 | TRC | Trace | The content is greater than zero, but too small to be quantified. |
| 2 | MSK | Masked | There is information on this item available, but it has not been provided by the sender due to security, privacy or other reasons. There may be an alternate mechanism for gaining access to this information. |

## Source: `domains/TS/examples.md`

# TS — Examples

## Example 1

This example shows a subset of published controlled terminology parameters and the relationship of values across response variables TSVAL, TSVALNF, TSVALCD, TSVCDREF, and TSVCDVER.

**ts.xpt**

| Row | STUDYID | DOMAIN | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL | TSVALNF | TSVALCD | TSVCDREF | TSVCDVER |
|-----|---------|--------|-------|---------|----------|--------|-------|---------|---------|----------|----------|
| 1 | XYZ | TS | 1 | | ADDON | Added on to Existing Treatments | Y | | C49488 | CDISC CT | 2011-06-10 |
| 2 | XYZ | TS | 1 | | AGEMAX | Planned Maximum Age of Subjects | P70Y | | | ISO 8601 | |
| 3 | XYZ | TS | 1 | | AGEMIN | Planned Minimum Age of Subjects | P18M | | | ISO 8601 | |
| 4 | XYZ | TS | 1 | | LENGTH | Trial Length | P3M | | | ISO 8601 | |
| 5 | XYZ | TS | 1 | | PLANSUB | Planned Number of Subjects | 300 | | | | |
| 6 | XYZ | TS | 1 | | RANDOM | Trial is Randomized | Y | | C49488 | CDISC CT | 2011-06-10 |
| 7 | XYZ | TS | 1 | | SEXPOP | Sex of Participants | BOTH | | C49636 | CDISC CT | 2011-06-10 |
| 8 | XYZ | TS | 1 | | STOPRULE | Study Stop Rules | INTERIM ANALYSIS FOR FUTILITY | | | | |
| 9 | XYZ | TS | 1 | | TBLIND | Trial Blinding Schema | DOUBLE BLIND | | C15228 | CDISC CT | 2011-06-10 |
| 10 | XYZ | TS | 1 | | TCNTRL | Control Type | PLACEBO | | C49648 | CDISC CT | 2011-06-10 |
| 11 | XYZ | TS | 1 | | TDIGRP | Diagnosis Group | Neurofibromatosis Syndrome (Disorder) | | 19133005 | SNOMED | 2011-03 |
| 12 | XYZ | TS | 1 | | INDIC | Trial Disease/Condition Indication | Tonic-Clonic Epilepsy (Disorder) | | 352818000 | SNOMED | 2011-03 |
| 13 | XYZ | TS | 1 | | TINDTP | Trial Intent Type | TREATMENT | | C49656 | CDISC CT | 2011-06-10 |
| 14 | XYZ | TS | 1 | | TITLE | Trial Title | A 24 Week Study of Oral Gabapentin vs. Placebo as add-on Treatment to Phenytoin in Subjects with Neurofibromatosis Epilepsy due to Neurofibromatosis | | | | |
| 15 | XYZ | TS | 1 | | TPHASE | Trial Phase Classification | Phase II Trial | | C15601 | CDISC CT | 2011-06-10 |
| 16 | XYZ | TS | 1 | | TTYPE | Trial Type | EFFICACY | | C49666 | CDISC CT | 2011-06-10 |
| 17 | XYZ | TS | 2 | | TTYPE | Trial Type | SAFETY | | C49667 | CDISC CT | 2011-06-10 |
| 18 | XYZ | TS | 1 | | CURTRT | Current Therapy or Treatment | Phenytoin | | 6158TKW0C5 | UNII | |
| 19 | XYZ | TS | 1 | | OBJPRIM | Trial Primary Objective | Reduction in the 3-month seizure frequency from baseline | | | | |
| 20 | XYZ | TS | 1 | | OBJSEC | Trial Secondary Objective | Percent reduction in the 3-month seizure frequency from baseline | | | | |
| 21 | XYZ | TS | 2 | | OBJSEC | Trial Secondary Objective | Reduction in the 3-month tonic-clonic seizure frequency from baseline | | | | |
| 22 | XYZ | TS | 1 | | SPONSOR | Clinical Study Sponsor | Pharmaco | | 123456789 | D-U-N-S NUMBER | |
| 23 | XYZ | TS | 1 | | TRT | Investigational Therapy or Treatment | Gabapentin | | 6CW7F3G59X | UNII | |
| 24 | XYZ | TS | 1 | | RANDQT | Randomization Quotient | 0.67 | | | | |
| 25 | XYZ | TS | 1 | | STRATFCT | Stratification Factor | SEX | | | | |
| 26 | XYZ | TS | 1 | | REGID | Registry Identifier | NCT123456789 | | NCT123456789 | ClinicalTrials.gov | |
| 27 | XYZ | TS | 2 | | REGID | Registry Identifier | XXYYZZ456 | | XXYYZZ456 | EudraCT | |
| 28 | XYZ | TS | 1 | | OUTMSPRI | Primary Outcome Measure | SEIZURE FREQUENCY | | | | |
| 29 | XYZ | TS | 1 | | OUTMSSEC | Secondary Outcome Measure | SEIZURE FREQUENCY | | | | |
| 30 | XYZ | TS | 2 | | OUTMSSEC | Secondary Outcome Measure | SEIZURE DURATION | | | | |
| 31 | XYZ | TS | 1 | | OUTMSEXP | Exploratory Outcome Measure | SEIZURE INTENSITY | | | | |
| 32 | XYZ | TS | 1 | | PCLAS | Pharmacological Class | Anti-epileptic Agent | | N0000175753 | MED-RT | |
| 33 | XYZ | TS | 1 | | FCNTRY | Planned Country of Investigational Sites | USA | | | ISO 3166-1 Alpha-3 | |
| 34 | XYZ | TS | 2 | | FCNTRY | Planned Country of Investigational Sites | CAN | | | ISO 3166-1 Alpha-3 | |
| 35 | XYZ | TS | 3 | | FCNTRY | Planned Country of Investigational Sites | MEX | | | ISO 3166-1 Alpha-3 | |
| 36 | XYZ | TS | 1 | | ADAPT | Adaptive Design | N | | C49487 | CDISC CT | 2011-06-10 |
| 37 | XYZ | TS | 1 | PA | DCUTDTC | Data Cutoff Date | 2010-04-10 | | | | |
| 38 | XYZ | TS | 1 | PA | DCUTDESC | Data Cutoff Description | PRIMARY ANALYSIS | | | | |
| 39 | XYZ | TS | 1 | | INTMODEL | Intervention Model | PARALLEL | | C82639 | CDISC CT | 2011-06-10 |
| 40 | XYZ | TS | 1 | | NARMS | Planned Number of Arms | 3 | | | | |
| 41 | XYZ | TS | 1 | | STYPE | Study Type | INTERVENTIONAL | | C98388 | CDISC CT | 2011-06-10 |
| 42 | XYZ | TS | 1 | | INTTYPE | Intervention Type | DRUG | | C1909 | CDISC CT | 2011-06-10 |
| 43 | XYZ | TS | 1 | | SSTDTC | Study Start Date | 2009-03-11 | | | ISO 8601 | |
| 44 | XYZ | TS | 1 | | SENDTC | Study End Date | 2011-04-01 | | | ISO 8601 | |
| 45 | XYZ | TS | 1 | | ACTSUB | Actual Number of Subjects | 304 | | | | |
| 46 | XYZ | TS | 1 | | HLTSUBJI | Healthy Subject Indicator | N | | C49487 | CDISC CT | 2011-06-10 |
| 47 | XYZ | TS | 1 | | SDMDUR | Stable Disease Minimum Duration | P3W | | | ISO 8601 | |
| 48 | XYZ | TS | 1 | | CRMDUR | Confirmed Response Minimum Duration | P28D | | | ISO 8601 | |

## Example 2

This example shows the relationship between parameters involving diagnosis and indication. Only selected trial summary parameters are included.

**Row 1:** Shows the trial title.

**Row 2:** Shows that subjects in this trial have a diagnosis of diabetes.

**Rows 3-4:** Show the conditions with the intervention in the trial are intended to address. The 2 rows for the same parameter are differentiated by their TSSEQ values.

**Row 5:** Shows that the intent of this trial is prevention of the conditions represented using the parameter "Trial Indication".

**ts.xpt**

| Row | STUDYID | DOMAIN | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL | TSVALNF | TSVALCD | TSVCDREF | TSVCDVER |
|-----|---------|--------|-------|---------|----------|--------|-------|---------|---------|----------|----------|
| 1 | XYZ | TS | 1 | | TITLE | Trial Type | A Study Comparing Cardiovascular Effects of Ticagrelor Versus Placebo in Patients With Type 2 Diabetes Mellitus (THEMIS) | | | | |
| 2 | XYZ | TS | 1 | | TDIGRP | Diagnosis Group | Diabetes mellitus type 2 | | 44054006 | SNOMED | 2017-03 |
| 3 | XYZ | TS | 1 | | INDIC | Trial Indication | Cardiac infarction | | 22298006 | SNOMED | 2017-03 |
| 4 | XYZ | TS | 2 | | INDIC | Trial Indication | Cerebrovascular accident | | 230690007 | SNOMED | 2017-01 |
| 5 | XYZ | TS | 1 | | TINDTP | Trial Intent Type | PREVENTION | | C49657 | CDISC CT | 2017-03-01 |

## Example 3

This example shows how to implement the null flavor in TSVALNF when the value in TSVAL is missing. Note that when TSVAL is null, TSVALCD is also null, and no code system is specified in TSVCDREF and TSVCDVER.

**Row 1:** Shows that there was no upper limit on planned age of subjects, as indicated by TSVALNF="PINF" (the null flavor that means "positive infinity").

**Row 2:** Shows that trial phase classification is not applicable, as indicated by TSVALNF="NA".

**ts.xpt**

| Row | STUDYID | DOMAIN | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL | TSVALNF | TSVALCD | TSVCDREF | TSVCDVER |
|-----|---------|--------|-------|---------|----------|--------|-------|---------|---------|----------|----------|
| 1 | XYZ | TS | 1 | | AGEMAX | Planned Maximum Age of Subjects | | PINF | | | |
| 2 | XYZ | TS | 1 | | TPHASE | Trial Phase Classification | | NA | | | |

## Example 4

This example uses TSGRPID to group parameter values describing specific study parts (e.g., PHASE 1B, PHASE 3) and specific study treatments (e.g., DRUG X, DRUG Z).

**Rows 1-6:** Show parameters and values that apply to the whole trial (i.e., both Phase 1B and Phase 3 parts of the trial). TSGRPID is null for this set of parameters.

**Rows 7-17:** Show parameters and values that describe the Phase 1B part of the trial. TSGRPID is populated with a value of "PHASE 1B" for this set of parameters.

**Rows 18-29:** Show parameters and values that describe the Phase 3 part of the trial. TSGRPID is populated with a value of "PHASE 3" for this set of parameters.

**Rows 30-33:** Show parameters and values that describe details about 1 of the treatments planned in the trial. TSGRPID="DRUG X" for this set of parameters.

**Rows 34-37:** Show parameters and values that describe details about 1 of the treatments planned in the trial. TSGRPID="DRUG Z" for this set of parameters.

**ts.xpt**

| Row | STUDYID | DOMAIN | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL | TSVALNF | TSVALCD | TSVCDREF | TSVCDVER |
|-----|---------|--------|-------|---------|----------|--------|-------|---------|---------|----------|----------|
| 1 | ABC123 | TS | 1 | | TITLE | Trial Title | A Phase 1b/3, Multicenter Trial of Drug Z in Combination with Drug X for Treatment of Melanoma | | | | |
| 2 | ABC123 | TS | 1 | | INDIC | Trial Indication | Malignant melanoma | | 372244006 | SNOMED | 2018-09-01 |
| 3 | ABC123 | TS | 1 | | SEXPOP | Sex of Participants | BOTH | | C49636 | CDISC CT | 2018-12-21 |
| 4 | ABC123 | TS | 1 | | AGEMIN | Planned Minimum Age of Subjects | P18Y | | | ISO 8601 | |
| 5 | ABC123 | TS | 1 | | AGEMAX | Planned Maximum Age of Subjects | | PINF | | | |
| 6 | ABC123 | TS | 1 | | HLTSUBJI | Healthy Subject Indicator | N | | C49487 | CDISC CT | 2018-12-21 |
| 7 | ABC123 | TS | 1 | PHASE 1B | TPHASE | Trial Phase Classification | | | | | |
| 8 | ABC123 | TS | 1 | PHASE 1B | TBLIND | Trial Blinding Schema | OPEN LABEL | | C49659 | CDISC CT | 2018-12-21 |
| 9 | ABC123 | TS | 1 | PHASE 1B | TCNTRL | Control Type | NONE | | C41132 | CDISC CT | 2018-12-21 |
| 10 | ABC123 | TS | 1 | PHASE 1B | TTYPE | Trial Type | SAFETY | | C49667 | CDISC CT | 2018-12-21 |
| 11 | ABC123 | TS | 1 | PHASE 1B | INTMODEL | Intervention Model | SINGLE GROUP | | C82640 | CDISC CT | 2018-12-21 |
| 12 | ABC123 | TS | 1 | PHASE 1B | NARMS | Planned Number of Arms | 1 | | | | |
| 13 | ABC123 | TS | 1 | PHASE 1B | PLANSUB | Planned Number of Subjects | 30 | | | | |
| 14 | ABC123 | TS | 1 | PHASE 1B | RANDOM | Trial is Randomized | N | | C49487 | CDISC CT | 2018-12-21 |
| 15 | ABC123 | TS | 1 | PHASE 1B | OBJPRIM | Trial Primary Objective | To evaluate the safety, as assessed by incidence of dose limiting toxicity, of combination therapy (Drug X + Drug Z) | | | | |
| 16 | ABC123 | TS | 1 | PHASE 1B | OUTMEAS | Primary Outcome Measure | Incidence of dose limiting toxicities | | | | |
| 17 | ABC123 | TS | 1 | PHASE 1B | COMPTRT | Comparative Treatment | | NA | | | |
| 18 | ABC123 | TS | 1 | PHASE 3 | TPHASE | Trial Phase Classification | PHASE III TRIAL | | C15602 | CDISC CT | 2018-12-21 |
| 19 | ABC123 | TS | 1 | PHASE 3 | TBLIND | Trial Blinding Schema | DOUBLE BLIND | | C15228 | CDISC CT | 2018-12-21 |
| 20 | ABC123 | TS | 1 | PHASE 3 | TCNTRL | Control Type | PLACEBO | | C49648 | CDISC CT | 2018-12-21 |
| 21 | ABC123 | TS | 1 | PHASE 3 | TTYPE | Trial Type | EFFICACY | | C49666 | CDISC CT | 2018-12-21 |
| 22 | ABC123 | TS | 1 | PHASE 3 | INTMODEL | Intervention Model | PARALLEL | | C82639 | CDISC CT | 2018-12-21 |
| 23 | ABC123 | TS | 1 | PHASE 3 | NARMS | Planned Number of Arms | 2 | | | | |
| 24 | ABC123 | TS | 1 | PHASE 3 | PLANSUB | Planned Number of Subjects | 500 | | | | |
| 25 | ABC123 | TS | 1 | PHASE 3 | RANDOM | Trial is Randomized | Y | | C49488 | CDISC CT | 2018-12-21 |
| 26 | ABC123 | TS | 1 | PHASE 3 | RANDQT | Randomization Quotient | 0.5 | | | | |
| 27 | ABC123 | TS | 1 | PHASE 3 | OBJPRIM | Trial Primary Objective | To evaluate the efficacy of combination therapy (Drug X + Drug Z) versus monotherapy (Drug X + Placebo), as assessed by progression-free survival using RECIST 1.1 | | | | |
| 28 | ABC123 | TS | 1 | PHASE 3 | OUTMEAS | Primary Outcome Measure | Progression Free Survival (response evaluation by blinded central review using RECIST 1.1) | | | | |
| 29 | ABC123 | TS | 1 | PHASE 3 | COMPTRT | Comparative Treatment | DRUG X | | | | |
| 30 | ABC123 | TS | 1 | DRUG X | DOSE | Dose per Administration | 200 | | | | |
| 31 | ABC123 | TS | 1 | DRUG X | DOSU | Dose Units | mg | | C28253 | CDISC CT | 2018-12-21 |
| 32 | ABC123 | TS | 1 | DRUG X | DOSFRQ | Dosing Frequency | EVERY WEEK | | C67069 | CDISC CT | 2018-12-21 |
| 33 | ABC123 | TS | 1 | DRUG X | ROUTE | Route of Administration | ORAL | | C38288 | CDISC CT | 2018-12-21 |
| 34 | ABC123 | TS | 1 | DRUG Z | DOSE | Dose per Administration | 10000 | | | | |
| 35 | ABC123 | TS | 1 | DRUG Z | DOSU | Dose Units | PFU | | C67264 | CDISC CT | 2018-12-21 |
| 36 | ABC123 | TS | 1 | DRUG Z | DOSFRQ | Dosing Frequency | EVERY 2 WEEKS | | C71127 | CDISC CT | 2018-12-21 |
| 37 | ABC123 | TS | 1 | DRUG Z | ROUTE | Route of Administration | INTRATUMOR | | C38269 | CDISC CT | 2018-12-21 |

## Source: `domains/OI/spec.md`

# OI — Non-host Organism Identifiers

> Class: Study Reference | Structure: One record per taxon per non-host organism

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### NHOID
- **Order:** 3
- **Label:** Non-host Organism Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sponsor-defined identifier for a non-host organism. NHOID should be populated with an intuitive name based on the identity of the organism as reported by the lab. It must be unique for each unique organism as defined by the specific values of the organism's entire known taxonomy described by pairs of OIPARMCD and OIVAL .

### OISEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to given to ensure uniqueness within a parameter within an organism (NHOID) within dataset.

### OIPARMCD
- **Order:** 5
- **Label:** Non-host Organism ID Element Short Name
- **Type:** Char
- **Controlled Terms:** C179591
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the taxon being described. Examples: "GROUP", "GENTYP", "SUBTYP".

### OIPARM
- **Order:** 6
- **Label:** Non-host Organism ID Element Name
- **Type:** Char
- **Controlled Terms:** C179590
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Name of the taxon being described. Examples: "Group", "Genotype", "Subtype".

### OIVAL
- **Order:** 7
- **Label:** Non-host Organism ID Element Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Req
- **CDISC Notes:** Value for the taxon in OIPARMCD/OIPARM for the organism identified by NHOID.
---

## Cross References

### Controlled Terminology
- [Non-host Organism Identifier Parameters (C179590)](../../terminology/core/oi.md) — OIPARM
- [Non-host Organism Identifier Parameters Code (C179591)](../../terminology/core/oi.md) — OIPARMCD

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Study Reference class definition](../../model/05_study_level_data.md)

## Source: `domains/OI/assumptions.md`

# OI — Assumptions

A special-purpose domain containing information that identifies levels of taxonomic nomenclature of microbes or parasites that have been either experimentally determined in the course of a study or are previously known, as in the case of lab strains used as reference in the study.

The biological classification of a non-host organism typically stops at the taxonomic rank of "species." Scientific taxonomic nomenclature below the rank of species is not clearly defined, lacks a globally accepted standard terminology, and is frequently organism-dependent. Therefore, the OI domain addresses organism taxonomy with a series of parameters that name the taxa appropriate to the organism and the granularity with which the organism has been identified in the particular study.

1. Non-host organisms include viruses and organisms such as pathogens or parasites, but also non-pathogenic organisms such as normal intestinal flora. Non-host organism identifiers are not to be used for host species identification (e.g., for animals used in preclinical studies), nor should they be used to represent other, non-taxonomy characteristics of non-host species (e.g., drug susceptibility, growth rates).

2. NHOID is sponsor-defined, with the following constraints:
    a. A unique NHOID must represent a unique identity as represented in its combination of OIPARMCD/OIVAL pairs. If 2 organisms share the same first 2 levels of taxonomy with regard to OIPARMCD/OIVAL, but 1 is identified to a third level and the other is not, they should be assigned 2 unique NHOIDs.
    b. Study sponsors should populate NHOID with intuitive name values based on either
        i. the name of the organism as reported by a lab or specified by the investigator, or
        ii. published references/databases where applicable and appropriate (e.g., when reference strain H77 is used in a HCV study, NHOID for this strain should be populated with "H77" or "HCV1a-H77").

3. NHOID can be used in any domain where observations about these organisms are being represented, allowing end users to determine what is known about the organism's identity by merging on NHOID, or by otherwise referring to the OI domain.

4. OIPARMCD and OIPARM must represent parameters for the identification of non-host organisms with regard to nomenclature only.
    a. Mostly, this will represent taxonomic ranks (i.e., species) as well as commonly used grouping terms (taxa that are not officially ranked, e.g., subtype, group, strain).
    b. They may also include other nomenclature terms that are less widely known but are used frequently for organism identification in a specific field of study (e.g., spoligotype in tuberculosis).
    c. They should be listed in the OI dataset in hierarchical order of least to most specific with increasing OISEQ values.

5. Variables not listed in the OI domain specification table should not be used in OI data sets.

## Source: `domains/OI/examples.md`

# OI — Examples

## Example 1

This example shows taxonomic identifiers for human immunodeficiency virus (HIV) and hepatitis C virus (HCV). NHOID is a unique non-host organism ID used to link findings on that organism in other datasets with details about its identification in OI. OIPARM shows the name of the individual taxa identified and OIVAL shows the experimentally determined values of those taxa.

**Rows 1-4:** Show the taxonomy for the HIV organism given the NHOID of HIV1MC. This virus has been identified as HIV-1, Group M, Subtype C.

**Rows 5-8:** Show the taxonomy for the HIV organism given the NHOID of HIV1MB, which was used as a reference. This virus has been identified as HIV-1, Group M, Subtype B.

**Rows 9-11:** Show the taxonomy for the HCV organism given the NHOID of HCV2C. This virus has been identified as HCV 2c.

**Rows 12-14:** Show the taxonomy for the HCV organism given the NHOID of H77. This virus is a known reference strain of HCV 1a.

**oi.xpt**

| Row | STUDYID | DOMAIN | NHOID | OISEQ | OIPARMCD | OIPARM | OIVAL |
|-----|---------|--------|-------|-------|----------|--------|-------|
| 1 | STUDY123 | OI | HIV1MC | 1 | SPCIES | Species | HIV |
| 2 | STUDY123 | OI | HIV1MC | 2 | TYPE | Type | 1 |
| 3 | STUDY123 | OI | HIV1MC | 3 | GROUP | Group | M |
| 4 | STUDY123 | OI | HIV1MC | 4 | SUBTYP | Subtype | C |
| 5 | STUDY123 | OI | HIV1MB | 1 | SPCIES | Species | HIV |
| 6 | STUDY123 | OI | HIV1MB | 2 | TYPE | Type | 1 |
| 7 | STUDY123 | OI | HIV1MB | 3 | GROUP | Group | M |
| 8 | STUDY123 | OI | HIV1MB | 4 | SUBTYP | Subtype | B |
| 9 | STUDY123 | OI | HCV2C | 1 | SPCIES | Species | HCV |
| 10 | STUDY123 | OI | HCV2C | 2 | GENTYP | Genotype | 2 |
| 11 | STUDY123 | OI | HCV2C | 3 | SUBTYP | Subtype | C |
| 12 | STUDY123 | OI | H77 | 1 | SPCIES | Species | HCV |
| 13 | STUDY123 | OI | H77 | 2 | GENTYP | Genotype | 1 |
| 14 | STUDY123 | OI | H77 | 3 | SUBTYP | Subtype | A |
