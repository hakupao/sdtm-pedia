# SDTMIG v3.4 — Chapter 1: Introduction

Source: SDTMIG v3.4, Section 1 (Pages 7-12)

## 1.1 Purpose

The Study Data Tabulation Model Implementation Guide for Human Clinical Trials (SDTMIG) Version 3.4 has been prepared by the Submissions Data Standards (SDS) team of the Clinical Data Interchange Standards Consortium (CDISC). Like its predecessors, v3.4 is intended to guide the organization, structure, and format of standard clinical trial tabulation datasets submitted to a regulatory authority. Version 3.4 supersedes all prior versions of the SDTMIG.

The SDTMIG should be used in close concert with Version 2.0 of the CDISC Study Data Tabulation Model (SDTM), which describes the general conceptual model for representing clinical study data that is submitted to regulatory authorities and should be read prior to reading the SDTMIG. SDTMIG Version 3.4 provides specific domain models, assumptions, business rules, and examples for preparing standard tabulation datasets that are based on the SDTM.

This document is intended for companies and individuals involved in the collection, preparation, and analysis of clinical data that will be submitted to regulatory authorities.

## 1.2 Organization of this Document

| Section | Title | Description |
|---------|-------|-------------|
| 1 | Introduction | Overall introduction to v3.4 models; changes from prior versions |
| 2 | Fundamentals of the SDTM | Basic concepts of the SDTM; how to use SDTMIG with SDTM |
| 3 | Submitting Data in Standard Format | How to describe metadata for regulatory submissions; conformance assessment |
| 4 | Assumptions for Domain Models | Basic concepts, business rules, and assumptions before applying domain models |
| 5 | Models for Special-purpose Domains | Special-purpose domains: Demographics, Comments, Subject Visits, Subject Elements |
| 6 | Domain Models Based on the General Observation Classes | Specific metadata models based on the 3 GOC, with assumptions and examples |
| 7 | Trial Design Model Datasets | Domains for trial-level data, with assumptions and examples |
| 8 | Representing Relationships and Data | How to represent relationships between domains, datasets, and records |
| 9 | Study References | Structures for study-specific terminology used in subject data |
| 10 | Appendices | Additional background material and supplemental material |

## 1.3 Relationship to Prior CDISC Documents

This document, together with the SDTM, represents the most recent version of the CDISC submission data domain models. All updates are intended to be backward-compatible. A detailed list of changes between versions is provided in Appendix E, Revision History.

Version 3.1 was the first fully implementation-ready version of the CDISC submission data standards that was directly referenced by the US FDA for use in human clinical studies involving drug products. However, future improvements and enhancements will continue to be made as sponsors gain more experience submitting data in this format. Therefore, CDISC will be preparing regular updates to the implementation guide to provide corrections, clarifications, additional domain models, examples, business rules, and conventions for using the standard domain models. Because CDISC will produce further documentation for Controlled Terminology as separate publications, sponsors are encouraged to check the CDISC website (https://www.cdisc.org/standards/terminology/controlled-terminology) frequently for additional information. See Section 4.3, Coding and Controlled Terminology Assumptions, for the most up-to-date information on applying Controlled Terminology.

The most significant changes since SDTMIG v3.3 include:

- Expanded the scope of the DA domain to include study products in addition to study drugs
- Grouped specimen-based lab domains (e.g., CP, GF, LB) in Sections 6.3.5.1-6.3.5.9 and added a generic specification
- Expanded the scope of the IS domain for assessments of antigen-induced humoral or cell-mediated immune response; added 3 new variables (Binding Agent, Molecule Secreted by Cells, Test Operational Objective)
- Updated the LB domain specification to include 10 new variables (Test Condition, Binding Agent, Test Operational Objective, Result Scale, Result Type, Collected Summary Result Type, Lower Limit of Detection, Method Sensitivity, Point in Time Flag, and Planned Duration)
- Decommissioned the Morphology (MO) domain
- Added Cell Phenotyping Findings (CP) and Genomics Findings (GF) domains
- Copied in Biospecimen Events (BE), Biospecimen Findings (BS), and Related Specimens (RELSPEC) from the provisional SDTMIG-PGx v1.0
- Updated QRS specifications and assumptions; introduced subsections for RS Disease Response and RS Clinical Classifications use cases
- Updated Tumor/Lesion (TU and TR) domain assumptions to describe use of indicator questions, disease recurrence conventions, and modeling of location of interest
- Expanded the scope of the SC domain to support collection over time
- Updated guidance and examples for the FA domain
- Corrected Core values for: DSDY, DSSTDY, LBSTREFC, MILOBXFL, and MIBLFL
- Updated Controlled Terminology for applicable variables across all domains, if available
- Removed Appendix C1, Trial Summary Codes

### Related Implementation Guides

| Guide | Scope |
|-------|-------|
| SDTMIG-AP | Associated Persons — data about persons who are not study subjects |
| SDTMIG-MD | Medical Devices — data about devices |
| SDTMIG-PGx | Pharmacogenomics/Genetics — largely incorporated into/superseded by SDTMIG v3.4 |

## 1.4 How to Read this Implementation Guide

The SDTMIG is best read online, so the reader can benefit from the many hyperlinks to internal and external references.

Recommended reading order:

1. Read the SDTM to gain a general understanding of SDTM concepts
2. Read Sections 1-3 for key concepts about preparing domains and submitting data. Refer to Appendix B, Glossary and Abbreviations, as necessary
3. Read Section 4, Assumptions for Domain Models
4. Review Section 5 (Special-purpose Domains) and Section 6 (Domain Models Based on GOC), referring back to Section 4 as directed
5. Read Section 7, Trial Design Model Datasets
6. Review Section 8, Representing Relationships and Data
7. Review Section 9, Study References
8. Review the appendices as appropriate. Appendix C, Controlled Terminology, in particular, describes how CDISC Terminology is centrally managed by the CDISC Controlled Terminology Team. Efforts are made at publication time to ensure all SDTMIG domain/dataset specification tables and/or examples reflect the latest CDISC Terminology; users, however, should refer to https://www.cancer.gov/research/resources/terminology/cdisc as the authoritative source of controlled terminology, as CDISC Controlled Terminology is updated on a quarterly basis.

This implementation guide covers most data collected in human clinical trials, but separate implementation guides provide information about certain data. See the SDTMIG for Associated Persons (SDTMIG-AP) and the SDTMIG for Medical Devices (SDTMIG-MD). Historically, the SDTM Implementation Guide for Pharmacogenomics/Genetics (SDTMIG-PGx) has provided structures for pharmacogenetic/genomic data and for data about biospecimens. Much of the content of the SDTMIG-PGx has been incorporated into and/or superseded by the SDTMIG v3.4.

### 1.4.1 How to Read a Domain Specification

A domain specification table includes rows for all required and expected variables and for a set of permissible variables. The permissible variables do not include all the variables that are allowed for the domain; they are a set of variables that the SDS Team considered likely to be included. The columns of the table are:

| Column | Description |
|--------|-------------|
| **Variable Name** | Standard name; variables without domain prefix are taken from SDTM directly; `--` is replaced by 2-character domain code |
| **Variable Label** | Longer name; may be same as SDTM label or customized for the domain. Sponsors should create an appropriate label if they include in a dataset an allowable variable not in the domain specification. |
| **Type** | SAS datatypes: "Num" or "Char" |
| **Controlled Terms, Codelist, or Format** | Controlled terminology references: an asterisk (*) indicates the variable may be subject to controlled terminology. Specifically, the asterisk means one of the following: (1) the controlled terminology might be of a type that would inherently be sponsor-defined; (2) the controlled terminology might be of a type that could be standardized, but for which a codelist has not yet been developed; or (3) the controlled terminology might be terminology specified in value-level metadata. Codelist references follow these conventions: (a) a hyperlinked codelist name in parentheses indicates that the variable is subject to the CDISC Controlled Terminology in that named codelist; (b) multiple hyperlinked codelist names indicate that the variable is subject to 1 or more of those named codelists from CDISC Controlled Terminology (if multiple codelists are in use for a single domain, value-level metadata indicates where each codelist is applicable); (c) a hyperlinked codelist name AND an asterisk (*) together indicate that the variable is subject to either the named CDISC Controlled Terminology codelist or to an external dictionary (the specific dictionary is identified in the metadata). The name of an external code system (e.g., MedDRA) is listed as plain text. "ISO 8601 datetime or interval" or "ISO 8601 duration" in plain text indicates that the variable values should be formatted in conformance with that standard. |
| **Role** | From the SDTM; SDTM includes the qualified variable for Variable/Synonym Qualifiers, but SDTMIG does not |
| **CDISC Notes** | Variable description, relationship to other variables, population rules, and example values. Such examples are only examples, and although they may be CDISC Controlled Terminology values, their presence in a CDISC Note should not be construed as definitive. For authoritative information on CDISC Controlled Terminology, consult the NCI website (https://www.cancer.gov/research/resources/terminology/cdisc). |
| **Core** | "Req" (Required), "Exp" (Expected), or "Perm" (Permissible) |

## 1.5 Known Issues

### Derived Records and the use of --DRVFL

Although it is implicit in the general concept of a derived record that there is no collected result (--ORRES should be null), this is not an explicit requirement currently stated in published CDISC material. This is being evaluated for clarification in a future release.

### Use of --LNKID and --LNKGRP

The definition of --LNKID says it is "used to identify a record," and --LNKGRP says it is "used to identify a group of records." This implies:
- RELTYPE = ONE → IDVAR of --LNKID (not --LNKGRP)
- RELTYPE = MANY → IDVAR of --LNKID (not --LNKGRP)

The examples in SDTMIG v3.4 have not been systematically reviewed to implement this distinction. This will be clarified in a future release.
