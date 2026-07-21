---
lang: en
slug: glossary
order: 40
title: "Glossary"
---

# Glossary

This page explains the clinical data standards terms most likely to appear when using SDTM Pedia. Platform setup, file upload, and internal validation terms are intentionally excluded from this public glossary.

| Term | Meaning | Usage Note |
| --- | --- | --- |
| CDISC | Clinical Data Interchange Standards Consortium, publisher of SDTM, ADaM, CDASH, and related standards. | Formal interpretation should use official CDISC publications. |
| SDTM | Study Data Tabulation Model. | Defines how clinical research tabulation data are organized. |
| SDTMIG | SDTM Implementation Guide. | Explains domains, variables, and implementation rules. |
| Domain | A topic-based SDTM data structure, such as AE, DM, LB, or CM. | Often understood as a standardized dataset. |
| Variable | A standard field within a domain, such as AESER, LBTESTCD, or CMTRT. | Keep variable names in English codes when asking. |
| Core | Variable usage classification, commonly Required, Expected, or Permissible. | Helps determine how a variable should appear in a dataset. |
| Controlled Terminology | A standard set of values maintained through CDISC/NCI terminology. | Often constrains submission values. |
| Codelist | A named terminology list, such as NY, AESEV, or LBNRIND. | Ask for both C-code and submission values when needed. |
| C-code | NCI EVS code for a term or codelist. | Useful for checking against the official terminology source. |
| Submission Value | The value used in submitted data. | Example: Y, N, U, and NA in the NY codelist. |
| MedDRA | Medical Dictionary for Regulatory Activities, commonly used for adverse event coding. | AEDECOD, AELLT, AEHLT, and related AE variables are MedDRA-related. |
| SUPPQUAL / SUPP-- | Supplemental qualifier mechanism for additional information not represented by standard variables. | Not every domain or scenario uses this mechanism; check SDTMIG rules. |
| RELREC | Related Records table used to represent relationships between records. | Commonly appears in cross-domain relationship questions. |
| Trial Design | Study design domains such as TA, TE, TV, TI, and TS. | Different from subject-level event or findings data. |
| ISO 8601 | Date and time representation standard. | SDTM --DTC variables commonly use this format. |
| Define-XML | Metadata exchange format for clinical study submissions. | Describes datasets, variables, terminology, origins, and related metadata. |

## Reading Tip

If an answer includes an unfamiliar variable, domain, or C-code, ask SDTM Pedia to explain that term first, then return to the original question. For formal deliverables, check the explanation against official CDISC materials.
