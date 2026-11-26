# SDTM v2.0 — Chapter 6: Datasets for Representing Relationships

Source: SDTM v2.0, Sections 6.1-6.7 (Pages 64-69)

## Overview

There are many occasions when it is necessary or desirable to represent relationships among datasets or records. The SDTM includes the following relationship datasets:

- Related Records Dataset, which represents 2 types of relationships:
  - A relationship between independent records (usually in separate datasets) for a subject (e.g., a concomitant medication taken to treat an adverse event)
  - A relationship between 2 (or more) datasets where records of 1 (or more) dataset(s) are related to record(s) in another dataset (or datasets)
- Supplemental Qualifiers Dataset, which represents dependent relationships where data that cannot be represented by a standard variable within a general-observation class dataset record (or records) can be related back to that record
- Pool Definition Dataset, which represents relationships between a subject and a pool of subjects
- Related Subjects Dataset, which represents relationships between study subjects other than membership in a pool.
- Associated Persons Relationships Dataset, which represents relationships between associated person(s) and study subjects
- Device-subject Relationships Dataset, which represents relationships between devices and study subjects
- Related Specimens Dataset, which represents relationships between collected specimens and specimens derived from them

The implementation guides define specific details and examples for each of these relationships.

---

## 6.1 Related Records (RELREC)

> KB note (not in SDTM v2.0): **Structure:** One record per related record, group of records, or dataset
>
> The Related Records dataset describes relationships between records within a domain, between records across domains, or between entire datasets.

### Variables (10 variables)

**RELREC Dataset**

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | RDOMAIN | Related Domain Abbreviation | Char | Identifier | 2-character abbreviation for the domain of the parent record(s). |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Null for dataset-level relationships |
| 4 | APID | Associated Persons Identifier | Char | Identifier | Identifier for a single associated person, a group, or a pool of associated persons |
| 5 | POOLID | Pool Identifier | Char | Identifier | For pooled subject data |
| 6 | SPDEVID | Sponsor Device Identifier | Char | Identifier | |
| 7 | IDVAR | Identifying Variable | Char | Identifier | Name of the identifying variable in the general-observation-class dataset that identifies the related record(s). |
| 8 | IDVARVAL | Identifying Variable Value | Char | Identifier | Value of identifying variable described in IDVAR. If --SEQ is the variable being used to describe this record, then the value of --SEQ is entered here. |
| 9 | RELTYPE | Relationship Type | Char | Record Qualifier | Identifies the hierarchical level of the records in the relationship. Values should be either ONE or MANY. However, values are only necessary when identifying a relationship between datasets. |
| 10 | RELID | Relationship Identifier | Char | Record Qualifier | RELID value should be unique within the ID variable (e.g., USUBJID, APID, POOLID, SPDEVID) that is the subject of the relationship. All records with this ID variable that have the same RELID are considered related/associated. RELID can be any value the sponsor chooses, and is only meaningful within the RELREC dataset to identify the related/associated Domain records. |

### RELTYPE Combinations

> KB note (not in SDTM v2.0): the RELTYPE combinations table below is KB-authored.

| Source RELTYPE | Target RELTYPE | Meaning |
|---------------|----------------|---------|
| ONE | ONE | One record relates to one record |
| ONE | MANY | One record relates to many records |
| MANY | ONE | Many records relate to one record |
| MANY | MANY | Many records relate to many records |

---

## 6.2 Supplemental Qualifiers (SUPP--)

For information on the naming of supplemental qualifier datasets, see the SDTMIG, SENDIG, and SDTMIG-AP.

> KB note (not in SDTM v2.0): **Structure:** One record per supplemental qualifier per related parent domain record(s)
>
> The Supplemental Qualifiers datasets provide a mechanism for including non-standard variables that cannot be accommodated in the standard domain datasets.

### Variables (13 variables)

**SUPP-- Dataset**

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | RDOMAIN | Related Domain Abbreviation | Char | Identifier | 2-character abbreviation for the domain of the parent record(s). |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 4 | APID | Associated Persons Identifier | Char | Identifier | Identifier for a single associated person, a group of associated persons, or a pool of associated persons. If APID identifies a pool, POOLDEF records must exist for each associated person (see Section 6.3, Pool Definition Dataset, and Section 4, Associated Persons Data). |
| 5 | POOLID | Pool Identifier | Char | Identifier | |
| 6 | SPDEVID | Sponsor Device Identifier | Char | Identifier | |
| 7 | IDVAR | Identifying Variable | Char | Identifier | Identifying variable in the parent dataset that identifies the related record(s). |
| 8 | IDVARVAL | Identifying Variable Value | Char | Identifier | Value of identifying variable of the parent record(s). |
| 9 | QNAM | Qualifier Variable Name | Char | Topic | The short name of the qualifier variable, which is used as a column name in a domain view with data from the parent domain. The value in QNAM cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST"). QNAM cannot contain characters other than letters, numbers, or underscores. This will often be the column name in the sponsor's operational dataset. QNAM should not be the name of any standard ADaM variable. |
| 10 | QLABEL | Qualifier Variable Label | Char | Synonym Qualifier | This is the long name or label associated with QNAM. The value in QLABEL cannot be longer than 40 characters. This will often be the column label in the sponsor's original dataset. |
| 11 | QVAL | Data Value | Char | Result Qualifier | Result of, response to, or value associated with QNAM. A value for this column is required; no records can be in a SUPP-- dataset with a null value for QVAL. |
| 12 | QORIG | Origin | Char | Record Qualifier | Because QVAL can represent a mixture of collected (on a CRF), derived, or assigned items, QORIG is used to indicate the origin of this data. |
| 13 | QEVAL | Evaluator | Char | Record Qualifier | Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain objectively collected or derived data. |

### Naming Convention

> KB note (not in SDTM v2.0): Separate Supplemental Qualifier datasets of the form `supp--.xpt` are required (e.g., `suppae.xpt`, `suppcm.xpt`). The RDOMAIN variable identifies which parent domain the supplemental data belongs to.

---

## 6.3 Pool Definition (POOLDEF)

This dataset identifies individual subjects included in a pool of subjects for which a single observation record (pool level) is captured.

> KB note (not in SDTM v2.0): **Structure:** One record per pooled subject per pool

**POOLDEF Dataset**

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | POOLID | Pool Identifier | Char | Identifier |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |
| 4 | APID | Associated Persons Identifier | Char | Identifier |

---

## 6.4 Related Subjects (RELSUB)

Some studies include subjects who are related to each other, and in some cases it is important to record those relationships. Studies in which pregnant women are treated and both the mother and her child(ren) are study subjects are the most common case in which relationships between subjects are collected. There are also studies of genetically based diseases where subjects who are related to each other are enrolled, and the relationships between subjects are recorded.

> KB note (not in SDTM v2.0): **Structure:** One record per relationship per subject

**RELSUB Dataset**

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | USUBJID | Unique Subject Identifier | Char | Identifier |
| 3 | POOLID | Pool Identifier | Char | Identifier |
| 4 | RSUBJID | Related Subject or Pool Identifier | Char | Identifier |
| 5 | SREL | Subject Relationship | Char | Record Qualifier |

---

## 6.5 Device-subject Relationships (DR)

The Device-subject Relationships (DR) domain is a special-purpose domain that links each subject to the associated devices. Information in this domain may have been collected and submitted in other domains (e.g., Device Exposure, Device Tracking and Disposition, Device Events). This domain, however, provides a single, consistent location to find the relationship between a subject and a device, regardless of the device or the domain in which subject-related data may have been collected or submitted.

> KB note (not in SDTM v2.0): **Structure:** One record per device-subject relationship

**Device-subject Relationships Dataset**

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier |

---

## 6.6 Associated Persons Related Subjects (APRELSUB)

To justify collection of AP data, some sort of a relationship is necessary between the associated person and a study, a subject, or a device. However, a single value in SREL is inadequate to describe relationships to multiple subjects or devices and/or multiple relationships to a single subject or device. In such cases, the value MULTIPLE should appear in SREL. MULTIPLE may also appear in RSUBJID to describe relationships with multiple subjects. When other SDTM variables are populated with MULTIPLE, the multiple values are stored in supplemental qualifiers.

However, this approach has been found to be an indirect and cumbersome way to handle multiple associated person-subject relationships. In addition, when there is AP data in multiple domains, the supplemental qualifier approach would require the same set of supplemental qualifiers to be repeated for each domain. The APRELSUB dataset, which parallels the structure of the RELSUB dataset, was created as a more efficient and simpler way to record these multiple relationships. The APRELSUB dataset is required for studies in which SREL values of MULTIPLE appear, but would not be needed if each associated person has only 1 relationship to a study, a subject, or a device.

> KB note (not in SDTM v2.0): **Structure:** One record per associated person relationship

**APRELSUB Dataset**

| # | Variable | Label | Type | Role |
|---|----------|-------|------|------|
| 1 | STUDYID | Study Identifier | Char | Identifier |
| 2 | APID | Associated Persons Identifier | Char | Identifier |
| 3 | RSUBJID | Related Subject or Pool Identifier | Char | Identifier |
| 4 | RDEVID | Related Device Identifier | Char | Identifier |
| 5 | SREL | Subject, Device, or Study Relationship | Char | Record Qualifier |

---

## 6.7 Related Specimens (RELSPEC)

> KB note (not in SDTM v2.0): **Structure:** One record per specimen identifier per subject
>
> Describes relationships between specimens, enabling representation of specimen lineage (e.g., parent specimen to derived aliquots or processed specimens).

**RELSPEC Dataset**

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | STUDYID | Study Identifier | Char | Identifier | |
| 2 | USUBJID | Unique Subject Identifier | Char | Identifier | |
| 3 | REFID | Reference ID | Char | Identifier | |
| 4 | SPEC | Specimen Type | Char | Variable Qualifier (REFID) | |
| 5 | PARENT | Specimen Parent | Char | Identifier | Identifies the REFID of the parent of a specimen to support tracking its genealogy. |
| 6 | LEVEL | Specimen Level | Num | Variable Qualifier (REFID) | Identifies the generation number of the sample where the collected sample is considered the first generation. |

> See [01_concepts_and_terms.md#changes-to-datasets-and-variables](01_concepts_and_terms.md#changes-to-datasets-and-variables) for the addition of RELSPEC in SDTM v2.0.

---

## Summary of Relationship Datasets

> KB note (not in SDTM v2.0): this summary table is KB-authored.

| Dataset | Code | Purpose | Subject-level? |
|---------|------|---------|----------------|
| Related Records | RELREC | Link records/datasets | Both |
| Supplemental Qualifiers | SUPP-- | Non-standard variables | Yes |
| Pool Definition | POOLDEF | Pool membership | Yes |
| Related Subjects | RELSUB | Subject relationships | Yes |
| Device-subject Relationships | DR | Device-subject links | Yes |
| AP Related Subjects | APRELSUB | AP-subject links | AP |
| Related Specimens | RELSPEC | Specimen lineage | Yes |
