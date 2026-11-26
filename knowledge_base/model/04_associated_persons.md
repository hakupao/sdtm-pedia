# SDTM v2.0 — Chapter 4: Associated Persons Data

Source: SDTM v2.0, Section 4 (Page 50)

## Overview

### 4 Associated Persons Data

Associated persons are individuals other than study subjects who can be associated with a study, a particular study subject, or a device used in the study. The structures of SDTM datasets that represent data about associated persons are based on the structures for data about study subjects, either general observation class structures or special-purpose domain structures. AP domains are created using SDTM variables, with the application of specific AP rules, including:

- Implementers creating AP domains will follow the AP assumptions for the Identifier variables.
- AP will be the prefix for the domain and dataset name, and will identify the dataset as AP data.
- The Associated Persons Identifier (APID) will be required in all AP datasets, and will identify records as AP data.

### AP Domain Rules

> KB note (not in SDTM v2.0):
> 1. **Prefix convention:** AP domains use the domain code prefix `AP` followed by the relevant domain code. For example, associated persons demographics would use `APDM`.
> 2. **APID:** The variable APID is used as an identifier in AP domains (instead of USUBJID for subjects).

> See [01_concepts_and_terms.md#changes-to-datasets-and-variables](01_concepts_and_terms.md#changes-to-datasets-and-variables) for the removal of APID from Section 3.1.4; RSUBJID, RDEVID, and SREL are described in the table below.

### Key Principles

The SDTM Implementation Guide: Associated Persons (SDTMIG-AP; available at https://www.cdisc.org/standards/foundational/sdtmig/sdtmig-ap) provides implementation rules, advice, and examples. Unless an exception is described in the SDTMIG-AP, all other general assumptions about SDTM and SDTMIG variables and domains apply to AP data.

> KB note (not in SDTM v2.0):
> - The same variables, roles, and controlled terminology apply
> - AP domains are not part of the core SDTMIG for human clinical trials

### Variables Used in Associated Persons Data

The variables in the following table are used in AP domains. APID is always included in each record in an AP domain. If the associated person is related to a study subject, RSUBJID identifies that subject; if the individual is related to a study device, RDEVID identifies the device. SREL describes the relationship of the associated person to a study subject, a study device, or the study.

**Associated Persons—Additional Identifier Variables**

| # | Variable | Label | Type | Role | Notes |
|---|----------|-------|------|------|-------|
| 1 | APID | Associated Persons Identifier | Char | Identifier | Identifier for a single associated person, a group of associated persons, or a pool of associated persons. If APID identifies a pool, POOLDEF records must exist for each associated person (see Section 6.3, Pool Definition Dataset, and Section 4, Associated Persons Data). |
| 2 | RSUBJID | Related Subject or Pool Identifier | Char | Identifier | Identifier for a related subject or pool of subjects. RSUBJID may be populated with the USUBJID of the related subject or the POOLID of the related pool. RSUBJID will be null for data about associated persons who are related to the study but not to any study subjects. |
| 3 | RDEVID | Related Device Identifier | Char | Identifier | Identifier for a related device. RDEVID will be populated with the SPDEVID of the related device. |
| 4 | SREL | Subject, Device, or Study Relationship | Char | Identifier | If RSUBJID is populated, describes the relationship of the associated person(s) identified in APID to the subject or pool identified in RSUBJID. If RDEVID is populated, describes the relationship of the associated person(s) identified in APID to the device identified in RDEVID. If RSUBJID and RDEVID are null, SREL describes the relationship of the associated person(s) identified in APID to the study identified in STUDYID. |

Relationships of an associated person to study subjects may be represented in the Associated Persons Relationships dataset. When an individual has multiple collected relationships to a study subject or study subjects, those multiple relationships must be represented in that relationships dataset.
