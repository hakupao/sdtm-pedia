# SDTM v2.0 — Chapter 6: Datasets for Representing Relationships

Source: SDTM v2.0, Sections 6.1-6.7 (Pages 64-69)

## Overview

The last group of datasets in the SDTM are those that describe relationships among datasets and records. These datasets are specified in this section.

---

## 6.1 Related Records (RELREC)

**Structure:** One record per related record, group of records, or dataset

The Related Records dataset describes relationships between records within a domain, between records across domains, or between entire datasets.

### Variables (10 variables)

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | RDOMAIN | Related Domain Abbreviation | Char | Record Qualifier | Domain of the related record(s) |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Null for dataset-level relationships |
| 4 | IDVAR | Identifying Variable | Char | Record Qualifier | Variable used to identify the related record(s) |
| 5 | IDVARVAL | Identifying Variable Value | Char | Record Qualifier | Value of IDVAR |
| 6 | RELTYPE | Relationship Type | Char | Record Qualifier | "ONE" or "MANY" |
| 7 | RELID | Relationship Identifier | Char | Identifier | Groups related RELREC records together |
| 8 | DOMAIN | Domain Abbreviation | Char | Identifier | |
| 9 | POOLID | Pool Identifier | Char | Identifier | For pooled subject data |
| 10 | RSUBJID | Related Subject ID | Char | Identifier | |

### RELTYPE Combinations

| Source RELTYPE | Target RELTYPE | Meaning |
|---------------|----------------|---------|
| ONE | ONE | One record relates to one record |
| ONE | MANY | One record relates to many records |
| MANY | ONE | Many records relate to one record |
| MANY | MANY | Many records relate to many records |

---

## 6.2 Supplemental Qualifiers (SUPP--)

**Structure:** One record per supplemental qualifier per related parent domain record(s)

The Supplemental Qualifiers datasets provide a mechanism for including non-standard variables that cannot be accommodated in the standard domain datasets.

### Variables (13 variables)

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | RDOMAIN | Related Domain Abbreviation | Char | Identifier | Parent domain code |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 4 | POOLID | Pool Identifier | Char | Identifier | |
| 5 | IDVAR | Identifying Variable | Char | Identifier | Typically --SEQ or --LNKID |
| 6 | IDVARVAL | Identifying Variable Value | Char | Identifier | |
| 7 | QNAM | Qualifier Variable Name | Char | Topic | 8-character name for the supplemental qualifier |
| 8 | QLABEL | Qualifier Variable Label | Char | Synonym Qualifier | Human-readable label |
| 9 | QVAL | Data Value | Char | Result Qualifier | The actual data value |
| 10 | QORIG | Origin | Char | Record Qualifier | Source of the data: "CRF", "ASSIGNED", "DERIVED" |
| 11 | QEVAL | Evaluator | Char | Record Qualifier | Role of the evaluator |
| 12 | QNAM (C-code) | | | | Variable C-code associated with QNAM |
| 13 | QLABEL (C-code) | | | | |

### Naming Convention

Separate Supplemental Qualifier datasets of the form `supp--.xpt` are required (e.g., `suppae.xpt`, `suppcm.xpt`). The RDOMAIN variable identifies which parent domain the supplemental data belongs to.

---

## 6.3 Pool Definition (POOLDEF)

**Structure:** One record per pooled subject per pool

Defines which subjects belong to each pool (for nonclinical studies where subjects are pooled).

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | POOLID | Pool Identifier | Char | Identifier |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |
| 4 | DOMAIN | Domain Abbreviation | Char | Identifier |

---

## 6.4 Related Subjects (RELSUB)

**Structure:** One record per relationship per subject

Describes relationships between subjects in a study (e.g., family relationships in genetic studies).

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | USUBJID | Unique Subject Identifier | Char | Identifier |
| 3 | RSUBJID | Related Subject Identifier | Char | Record Qualifier |
| 4 | SREL | Subject Relationship | Char | Topic |
| 5 | DOMAIN | Domain Abbreviation | Char | Identifier |

---

## 6.5 Device-subject Relationships (DR)

**Structure:** One record per device-subject relationship

Links devices to subjects when the device is associated with a subject.

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | USUBJID | Unique Subject Identifier | Char | Identifier |
| 3 | SPDEVID | Sponsor Device Identifier | Char | Record Qualifier |
| 4 | DOMAIN | Domain Abbreviation | Char | Identifier |

---

## 6.6 Associated Persons Related Subjects (APRELSUB)

**Structure:** One record per associated person relationship

Links associated persons to subjects.

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | APID | Associated Person Identifier | Char | Identifier |
| 3 | RSUBJID | Related Subject Identifier | Char | Record Qualifier |
| 4 | SREL | Subject Relationship | Char | Topic |
| 5 | DOMAIN | Domain Abbreviation | Char | Identifier |

---

## 6.7 Related Specimens (RELSPEC)

**Structure:** One record per specimen identifier per subject

Describes relationships between specimens, enabling representation of specimen lineage (e.g., parent specimen to derived aliquots or processed specimens).

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |
| 4 | REFID | Specimen Identifier | Char | Identifier |
| 5 | SPEC | Specimen Type | Char | Record Qualifier |
| 6 | PARENT | Parent Specimen ID | Char | Record Qualifier |

**Note:** RELSPEC was added new in SDTM v2.0. This domain was first introduced in the provisional SDTMIG-PGx (now deprecated) and had not previously been a part of the SDTM. It was added because the domain was added to SDTMIG v3.4.

---

## Summary of Relationship Datasets

| Dataset | Code | Purpose | Subject-level? |
|---------|------|---------|----------------|
| Related Records | RELREC | Link records/datasets | Both |
| Supplemental Qualifiers | SUPP-- | Non-standard variables | Yes |
| Pool Definition | POOLDEF | Pool membership | Yes (nonclinical) |
| Related Subjects | RELSUB | Subject relationships | Yes |
| Device-subject Relationships | DR | Device-subject links | Yes |
| AP Related Subjects | APRELSUB | AP-subject links | AP |
| Related Specimens | RELSPEC | Specimen lineage | Yes |
