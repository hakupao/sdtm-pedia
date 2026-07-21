# SDTMIG v3.4 — Introduction (Sections 1–3)

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials

---

## 1 Introduction

### 1.1 Purpose

The Study Data Tabulation Model Implementation Guide for Human Clinical Trials (SDTMIG) Version 3.4 has been prepared by the Submissions Data Standards (SDS) team of the Clinical Data Interchange Standards Consortium (CDISC). Like its predecessors, v3.4 is intended to guide the organization, structure, and format of standard clinical trial tabulation datasets submitted to a regulatory authority. Version 3.4 supersedes all prior versions of the SDTMIG.

The SDTMIG should be used in close concert with Version 2.0 of the CDISC Study Data Tabulation Model (SDTM, available at https://www.cdisc.org/standards/foundational/sdtm), which describes the general conceptual model for representing clinical study data that is submitted to regulatory authorities and should be read prior to reading the SDTMIG. SDTMIG Version 3.4 provides specific domain models, assumptions, business rules, and examples for preparing standard tabulation datasets that are based on the SDTM.

This document is intended for companies and individuals involved in the collection, preparation, and analysis of clinical data that will be submitted to regulatory authorities.

### 1.2 Organization of this Document

This document is organized into the following sections:

- Section 1, Introduction, provides an overall introduction to the v3.4 models and describes changes from prior versions.
- Section 2, Fundamentals of the SDTM, recaps the basic concepts of the SDTM, and describes how this implementation guide should be used in concert with the SDTM.
- Section 3, Submitting Data in Standard Format, explains how to describe metadata for regulatory submissions, and how to assess conformance with the standards.
- Section 4, Assumptions for Domain Models, describes basic concepts, business rules, and assumptions that should be taken into consideration before applying the domain models.
- Section 5, Models for Special-purpose Domains, describes special-purpose domains, including Demographics, Comments, Subject Visits, and Subject Elements.
- Section 6, Domain Models Based on the General Observation Classes, provides specific metadata models based on the 3 general observation classes, along with assumptions and example data.
- Section 7, Trial Design Model Datasets, describes domains for trial-level data, with assumptions and examples.
- Section 8, Representing Relationships and Data, describes how to represent relationships between separate domains, datasets, and/or records, and provides information to help sponsors determine where data belong in the SDTM.
- Section 9, Study References, provides structures for representing study-specific terminology used in subject data.
- Appendices provide additional background material and describe other supplemental material relevant to implementation.

### 1.3 Relationship to Prior CDISC Documents

This document, together with the SDTM, represents the most recent version of the CDISC submission data domain models. All updates are intended to be backward-compatible. The most significant changes since SDTMIG v3.3 include:

- Expanded the scope of the DA domain to include study products in addition to study drugs. See Section 6.3.1, Product Accountability.
- Grouped specimen-based lab domains (e.g., CP, GF, LB) in Sections 6.3.5.1–6.3.5.9 and added a generic specification for these domains. See Section 6.3.5, Specimen-based Findings Domains.
- Expanded the scope of the IS domain for assessments of antigen-induced humoral or cell-mediated immune response. Added 3 new variables (i.e., Binding Agent, Molecule Secreted by Cells, Test Operational Objective). See Section 6.3.5.5, Immunogenicity Specimen Assessments.
- Updated the LB domain specification to include the following 10 new variables: Test Condition, Binding Agent, Test Operational Objective, Result Scale, Result Type, Collected Summary Result Type, Lower Limit of Detection, Method Sensitivity, Point in Time Flag, and Planned Duration. See Section 6.3.5.6, Laboratory Test Results.
- Decommissioned the Morphology (MO) domain.
- Added Cell Phenotyping Findings (CP) and Genomics Findings (GF) domains. See Section 6.3.5.3, Cell Phenotype Findings (CP), and Section 6.3.5.4, Genomics Findings (GF).
- Copied in Biospecimen Events (BE), Biospecimen Findings (BS), and Related Specimens (RELSPEC) from the provisional SDTMIG-PGx v1.0 in preparation for its eventual retirement. See Section 6.2.2, Biospecimen Events (BE); Section 6.3.5.2, Biospecimen Findings (BS); and Section 8.8, Related Specimens (RELSPEC).
- Updated QRS specifications and assumptions. Also introduced subsections to separate assumptions and examples describing the RS Disease Response use case and the RS Clinical Classifications use case. See Section 6.3.9, Questionnaires, Ratings, and Scales (QRS) Domains (FT, QS, RS).
- Updated the Tumor/Lesion (TU and TR) domain assumptions to describe use of indicator questions, disease recurrence conventions, and modeling of location of interest. See Section 6.3.12, Tumor/Lesion Domains.
- Expanded the scope of the SC domain to support collection over time. See Section 6.3.10, Subject Characteristics.
- Updated guidance and examples for the FA domain. See Section 6.4, Findings About Events or Interventions.
- Corrected Core values for the following variables: DSDY, DSSTDY, LBSTREFC, MILOBXFL, and MIBLFL.
- Updated Controlled Terminology for applicable variables across all domains, if available.
- Removed Appendix C1, Trial Summary Codes.

A detailed list of changes between versions is provided in Appendix E, Revision History.

Version 3.1 was the first fully implementation-ready version of the CDISC submission data standards that was directly referenced by the US FDA for use in human clinical studies involving drug products. However, future improvements and enhancements will continue to be made as sponsors gain more experience submitting data in this format. Therefore, CDISC will be preparing regular updates to the implementation guide to provide corrections, clarifications, additional domain models, examples, business rules, and conventions for using the standard domain models. Because CDISC will produce further documentation for Controlled Terminology as separate publications, sponsors are encouraged to check the CDISC website (https://www.cdisc.org/standards/terminology/controlled-terminology) frequently for additional information. See Section 4.3, Coding and Controlled Terminology Assumptions, for the most up-to-date information on applying Controlled Terminology.

### 1.4 How to Read this Implementation Guide

The SDTMIG is best read online, so the reader can benefit from the many hyperlinks to internal and external references. The following guidelines may be helpful in reading this document:

1. First, read the SDTM to gain a general understanding of SDTM concepts.
2. Next, read Sections 1–3 of this document to review the key concepts for preparing domains and submitting data to regulatory authorities. Refer to Appendix B, Glossary and Abbreviations, as necessary.
3. Read Section 4, Assumptions for Domain Models.
4. Review Section 5, Models for Special-purpose Domains, and Section 6, Domain Models Based on the General Observation Classes, in detail, referring back to Section 4, Assumptions for Domain Models, as directed. See the implementation examples for each domain to gain an understanding of how to apply the domain models for specific types of data.
5. Read Section 7, Trial Design Model Datasets, to understand the fundamentals of the Trial Design Model and consider how to apply the concepts for typical protocols.
6. Review Section 8, Representing Relationships and Data, to learn advanced concepts of how to express relationships between datasets, records, and additional variables not specifically defined in the models.
7. Review Section 9, Study References, to learn about occasions when it is necessary to establish study-specific references that will be used in accordance with subject data.
8. Finally, review the appendices as appropriate. Appendix C, Controlled Terminology, in particular, describes how CDISC Terminology is centrally managed by the CDISC Controlled Terminology Team. Efforts are made at publication time to ensure all SDTMIG domain/dataset specification tables and/or examples reflect the latest CDISC Terminology; users, however, should refer to https://www.cancer.gov/research/resources/terminology/cdisc as the authoritative source of controlled terminology, as CDISC Controlled Terminology is updated on a quarterly basis.

This implementation guide covers most data collected in human clinical trials, but separate implementation guides provide information about certain data, and should be consulted when needed. The following guides are available at https://www.cdisc.org/standards/foundational/sdtmig:

- The SDTM Implementation Guide: Associated Persons (SDTMIG-AP) provides structures for representing data collected about persons who are not study subjects.
- The SDTM Implementation Guide for Medical Devices (SDTMIG-MD) provides structures for data about devices.
- Historically, the SDTM Implementation Guide for Pharmacogenomics/Genetics (SDTMIG-PGx) has provided structures for pharmacogenetic/genomic data and for data about biospecimens. Much of the content of the SDTMIG-PGx has been incorporated into and/or superseded by the SDTMIG v3.4.

#### 1.4.1 How to Read a Domain Specification

A domain specification table includes rows for all required and expected variables for a domain and for a set of permissible variables. The permissible variables do not include all the variables that are allowed for the domain; they are a set of variables that the SDS Team considered likely to be included. The columns of the table are:

- **Variable Name**
  - For variables that do not include a domain prefix, this name is taken directly from the SDTM.
  - For variables with a "--" placeholder in the SDTM, the "--" is replaced by the 2-character domain code.
- **Variable Label**: A longer name for the variable.
  - This may be the same as the label in the SDTM, or it may be customized for the domain.
  - Sponsors should create an appropriate label if they include in a dataset an allowable variable not in the domain specification.
- **Type**: One of the 2 SAS datatypes, "Num" or "Char". These values are taken directly from the SDTM.
- **Controlled Terms, Codelist, or Format**
  - *Controlled Terms*
    - As noted in the table note, an asterisk (\*) indicates that the variable may be subject to controlled terminology.
    - The controlled terminology might be of a type that would inherently be sponsor-defined.
    - The controlled terminology might be of a type that could be standardized, but for which a codelist not yet been developed.
    - The controlled terminology might be terminology specified in value-level metadata.
    - The name of an external code system (e.g., MedDRA) will be listed in plain text.
  - *Codelist*
    - A hyperlinked codelist name in parentheses indicates that the variable is subject to the CDISC Controlled Terminology in the named codelist.
    - Multiple hyperlinked codelist names indicate that the variable is subject to 1 or more of the named codelists from CDISC Controlled Terminology. If multiple codelists are in use for a single domain, value-level metadata would indicate where each codelist is applicable.
    - A hyperlinked codelist name and an asterisk (\*) indicate that the variable is subject to either the named codelist from the CDISC Controlled Terminology or to an external dictionary. The specific dictionary is identified in the metadata.
  - *Format*: "ISO 8601 datetime or interval" or "ISO 8601 duration" in plain text indicates that the variable values should be formatted in conformance with that standard.
- **Role**: This is taken directly from the SDTM. Note that if a variable is either a Variable Qualifier or a Synonym Qualifier, the SDTM includes the qualified variable, but SDTMIG domain specifications do not.
- **CDISC Notes** may include any of the following:
  - A description of what the variable means
  - Information about how this variable relates to another variable
  - Rules for when or how the variable should be populated, or how the contents should be formatted
  - Examples of values that might appear in the variable. Such examples are only examples, and although they may be CDISC Controlled Terminology values, their presence in a CDISC Note should not be construed as definitive. For authoritative information on CDISC Controlled Terminology, consult https://www.cancer.gov/research/resources/terminology/cdisc.
- **Core**: Contains 1 of the 3 values — "Req", "Exp", or "Perm" — explained further in Section 4.1.5, SDTM Core Designations.

### 1.5 Known Issues

**Derived Records and the use of --DRVFL**

Although it is implicit in the general concept of a derived record that there is no collected result (--ORRES should be null), this is not an explicit requirement currently stated in published CDISC material. This is being evaluated for clarification in a future release of the SDTMIG and/or Model document.

**Use of --LNKID and --LNKGRP**

The definition of --LNKID says that it is "used to identify a record," and the definition of --LNKGRP says that it is "used to identify a group of records." This implies that when setting up a relationship in RELREC, a row where RELTYPE = ONE will have an IDVAR of --LNKID (and not --LNKGRP); a row where RELTYPE = MANY will have an IDVAR of --LNKID (and not --LNKGRP). The examples in this version of the SDTMIG have not been systematically reviewed to implement this distinction between --LNKID and --LNKGRP. This distinction between --LNKID and --LNKGRP, and the appropriateness of using other identification variables for linking, will be clarified in a future release of the SDTMIG and/or Model document, and at that time examples in the SDTMIG will be systematically reviewed and updated to reflect that clarification.

---

## 2 Fundamentals of the SDTM

### 2.1 Observations and Variables

The SDTMIG for Human Clinical Trials is based on the SDTM's general framework for organizing clinical trial information that is to be submitted to regulatory authorities. The SDTM is built around the concept of observations collected about subjects who participated in a clinical study. Each observation can be described by a series of variables, corresponding to a row in a dataset. Each variable can be classified according to its role. A role determines the type of information conveyed by the variable about each distinct observation and how it can be used.

Variables can be classified into 5 major roles:

- **Identifier variables**, such as those that identify the study, subject, domain, and sequence number of the record
- **Topic variables**, which specify the focus of the observation (e.g., the name of a lab test)
- **Timing variables**, which describe the timing of the observation (e.g., start date and end date)
- **Qualifier variables**, which include additional illustrative text or numeric values that describe the results or additional traits of the observation (e.g., units, descriptive adjectives)
- **Rule variables**, which describe the condition to start, end, branch, or loop in the Trial Design Model

The set of Qualifier variables can be further categorized into 5 subclasses:

- **Grouping Qualifiers** are used to group together a collection of observations within the same domain. Examples include --CAT and --SCAT.
- **Result Qualifiers** describe the specific results associated with the topic variable in a Findings dataset. They answer the question raised by the topic variable. Result Qualifiers are --ORRES, --STRESC, and --STRESN.
- **Synonym Qualifiers** specify an alternative name for a particular variable in an observation. Examples include --MODIFY and --DECOD, which are equivalent terms for a --TRT or --TERM topic variable, and --TEST and --LOINC, which are equivalent terms for a --TESTCD.
- **Record Qualifiers** define additional attributes of the observation record as a whole (rather than describing a particular variable within a record). Examples include --REASND, AESLIFE, and all other serious adverse event (SAE) flag variables in the AE domain; AGE, SEX, and RACE in the DM domain; and --BLFL, --POS, --LOC, --SPEC and --NAM in a Findings domain.
- **Variable Qualifiers** are used to further modify or describe a specific variable within an observation and are only meaningful in the context of the variable they qualify. Examples include --ORRESU, --ORNRHI, and --ORNRLO, all of which are Variable Qualifiers of --ORRES; and --DOSU, which is a Variable Qualifier of --DOSE.

For example, in the observation, "Subject 101 had mild nausea starting on study day 6," the Topic variable value is the term for the adverse event, "NAUSEA". The Identifier variable is the subject identifier, "101". The Timing variable is the study day of the start of the event, which captures the information, "starting on study day 6," whereas an example of a Record Qualifier is the severity, the value for which is "MILD". Additional Timing and Qualifier variables could be included to provide the necessary detail to adequately describe an observation.

### 2.2 Datasets and Domains

Observations about study subjects are normally collected for all subjects in a series of domains. A domain is defined as a collection of logically related observations with a common topic. The logic of the relationship may pertain to the scientific subject matter of the data or to its role in the trial. Each domain is represented by a single dataset.

Each domain dataset is distinguished by a unique, 2-character code that should be used consistently throughout the submission. This code, which is stored in the SDTM variable named DOMAIN, is used in 4 ways: as the dataset name, as the value of the DOMAIN variable in that dataset, as a prefix for most variable names in that dataset, and as a value in the RDOMAIN variable in relationship tables (see Section 8, Representing Relationships and Data).

All datasets are structured as flat files with rows representing observations and columns representing variables. Each dataset is described by metadata definitions that provide information about the variables used in the dataset. The metadata are described in a data definition document (i.e., a Define-XML document) that is submitted with the data to regulatory authorities. The Define-XML standard (available at https://www.cdisc.org/standards/data-exchange/define-xml) specifies metadata attributes to describe SDTM data.

Data represented in SDTM datasets include data as originally collected or received, data from the protocol, assigned data, and derived data. The SDTM lists only the name, label, and type, with a set of brief CDISC guidelines that provide a general description for each variable.

The domain dataset models in Section 5, Models for Special-purpose Domains, and Section 6, Domain Models Based on the General Observation Classes, provide additional information about controlled terms or format, notes on proper usage, and examples. See also Section 1.4.1, How to Read a Domain Specification.

### 2.3 The General Observation Classes

Most subject-level observations collected during the study should be represented according to 1 of the 3 SDTM general observation classes: Interventions, Events, or Findings. The lists of variables allowed to be used in each of these can be found in the SDTM.

- The **Interventions** class captures investigational, therapeutic, and other treatments that are administered to the subject (with some actual or expected physiological effect) either as specified by the study protocol (e.g., exposure to study drug), coincident with the study assessment period (e.g., concomitant medications), or self-administered by the subject (e.g., use of alcohol, tobacco, or caffeine).
- The **Events** class captures planned protocol milestones such as randomization and study completion, and occurrences, conditions, or incidents independent of planned study evaluations occurring during the trial (e.g., adverse events) or prior to the trial (e.g., medical history).
- The **Findings** class captures the observations resulting from planned evaluations to address specific tests or questions (e.g., laboratory tests, ECG testing, questions listed on questionnaires).

In most cases, the choice of observation class appropriate to a specific collection of data can be easily determined according to these descriptions. The majority of data, which typically consists of measurements or responses to questions, usually at specific visits or time points, will fit the Findings general observation class. Additional guidance on choosing the appropriate general observation class is provided in Section 8.6.1, Guidelines for Determining the General Observation Class.

General assumptions for use with all domain models and custom domains based on the general observation classes are described in Section 4, Assumptions for Domain Models; specific assumptions for individual domains are included with the domain models.

### 2.4 Datasets Other than General Observation Class Domains

The SDTM includes 4 types of datasets other than those based on the general observation classes:

- Domain datasets with subject-level data that do not conform to 1 of the 3 general observation classes. These include Demographics (DM), Comments (CO), Subject Elements (SE), and Subject Visits (SV), and are described in Section 5, Models for Special-purpose Domains.
- Trial Design Model (TDM) datasets, which represent information about the study design but do not contain subject data. These include datasets such as Trial Arms (TA) and Trial Elements (TE) and are described in Section 7, Trial Design Model Datasets.
- Relationship datasets, such as the RELREC and SUPP-- datasets. These are described in Section 8, Representing Relationships and Data.
- Study Reference datasets include Device Identifiers (DI) and Non-host Organism Identifiers (OI). These provide structures for representing study-specific terminology used in subject data. These are described in Section 9, Study References.

### 2.5 The SDTM Standard Domain Models

A sponsor should only submit domain datasets that were actually collected (or directly derived from the collected data) for a given study. Decisions on what data to collect should be based on the scientific objectives of the study, rather than the SDTM. Note that any data collected that will be submitted in an analysis (ADaM) dataset must be traceable to a source in a tabulation (SDTM) dataset.

The collected data for a given study may use standard domains from this and other SDTM implementation guides as well as additional custom domains based on the 3 general observation classes. A list of standard domains is provided in Section 3.2.1, Dataset-level Metadata. Final domains will be published only in an SDTM implementation guide (this guide or another implementation guide, e.g., SDTMIG for Medical Devices). Therapeutic-area standards projects and other projects may develop proposals for additional domains. Draft versions of these domains may be made available in the CDISC wiki in the SDTM Draft Domains space (https://wiki.cdisc.org/display/SDD/SDTM+Draft+Domains+Home).

These general rules apply when determining which variables to include in a domain:

- The Identifier variables, STUDYID, USUBJID, DOMAIN, and --SEQ are required in all domains based on the general observation classes. Other Identifiers may be added as needed.
- Any Timing variables are permissible for use in any submission dataset based on a general observation class except where restricted by specific domain assumptions.
- Any additional Qualifier variables from the same general observation class may be added to a domain model except where restricted by specific domain assumptions.
- Sponsors may not add any variables other than those described in the preceding 3 bullets. The SDTM allows for the inclusion of a sponsor's non-SDTM variables using the Supplemental Qualifiers special-purpose dataset structure, described in Section 8.4, Relating Non-standard Variable Values to a Parent Domain. As the SDTM continues to evolve, certain additional standard variables may be added to the general observation classes.
- Standard variables must not be renamed or modified for novel usage. Their metadata should not be changed.
- A Permissible variable should be used in an SDTM dataset wherever appropriate.
  - If a study includes a data item that would be represented in a Permissible variable, then that variable must be included in the SDTM dataset, even if null. Refer to the Define-XML standard (available at https://www.cdisc.org/standards/data-exchange/define-xml) for additional details on how to manage no data availability.
  - If a study did not include a data item that would be represented in a Permissible variable, then that variable should not be included in the SDTM dataset and should not be declared in the Define-XML document.

### 2.6 Creating a New Domain

This section describes the overall process for creating a custom domain, which must be based on 1 of the 3 SDTM general observation classes. The number of domains submitted should be based on the specific requirements of the study. To create a custom domain:

1. Confirm that none of the existing published domains will fit the need. A custom domain may only be created if the data are different in nature and do not fit into an existing published domain.
   - Establish a domain of a common topic; that is, where the nature of the data is the same rather than by a specific method of collection (e.g., electrocardiogram). Group and separate data within the domain using --CAT, --SCAT, --METHOD, --SPEC, --LOC, and so on, as appropriate. Examples of different topics are: microbiology, tumor measurements, pathology/histology, vital signs, and physical exam results.
   - Do not create separate domains based on time; rather, represent both prior and current observations in a domain (e.g., CM for all non-study medications). Note that Adverse Events (AE) and Medical History (MH) are an exception to this best practice because of regulatory reporting needs.
   - How collected data are used (e.g., to support analyses and/or efficacy endpoints) must not result in the creation of a custom domain. For example, if blood pressure measurements are endpoints in a hypertension study, they must still be represented in the Vital Signs (VS) domain, as opposed to a custom "efficacy" domain. Similarly, if liver function test results are of special interest, they must still be represented in the Laboratory Tests (LB) domain.
   - Data that were collected on separate CRF modules or pages may fit into an existing domain (e.g., as separate questionnaires into the QS domain, prior and concomitant medications in the CM domain).
   - If it is necessary to represent relationships between data that are hierarchical in nature (e.g., a parent record must be observed before child records), then establish a domain pair (e.g., MB/MS, PC/PP). Note: Domain pairs have been modeled for microbiology data (MB/MS domains) and pharmacokinetics (PK) data (PC/PP domains) to enable dataset-level relationships to be described using RELREC. The domain pair uses DOMAIN as an identifier to group parent records (e.g., MB) from child records (e.g., MS) and enables a dataset-level relationship to be described in RELREC. Without using DOMAIN to facilitate description of the data relationships, RELREC, as currently defined, could not be used without introducing a variable that would group data like DOMAIN.
2. Check the SDTM Draft Domains area of the CDISC wiki (https://wiki.cdisc.org/display/SDD/SDTM+Draft+Domains+Home) for proposed domains developed since the last published version of the SDTMIG. These proposed domains may be used as custom domains in a submission.
3. Look for an existing, relevant domain model to serve as a prototype. If no existing model seems appropriate, choose the general observation class (Interventions, Events, or Findings) that best fits the data by considering the topic of the observation. As illustrated in the following figure, the general approach for selecting variables for a custom domain is:
   1. Select and include the required identifier variables (e.g., STUDYID, DOMAIN, USUBJID, --SEQ) and any permissible Identifier variables from the SDTM.
   2. Include the topic variable from the identified general observation class (e.g., --TESTCD for Findings) in the SDTM.
   3. Select and include the relevant qualifier variables from the identified general observation class in the SDTM. Variables belonging to other general observation classes must not be added.
   4. Select and include the applicable timing variables in the SDTM.
   5. Determine the domain code, one that is not a domain code in the CDISC Controlled Terminology SDTM Domain Abbreviations codelist (see https://datascience.cancer.gov/resources/cancer-vocabulary/cdisc-terminology). If it is desired to have this domain code be part of CDISC Controlled Terminology, submit a request at https://ncitermform.nci.nih.gov/ncitermform/?version=cdisc. The sponsor-selected, 2-character domain code should be used consistently throughout the submission. AD, AX, AP, SQ, and SA may not be used as custom domain codes.
   6. Apply the 2-character domain code to the appropriate variables in the domain. Replace all variable prefixes (shown in the models as "--") with the domain code.
   7. Set the order of variables consistent with the order defined in the SDTM for the general observation class.
   8. Adjust the labels of the variables only as appropriate to properly convey the meaning in the context of the data being submitted in the newly created domain. Use title case for all labels (title case means to capitalize the first letter of every word except for articles, prepositions, and conjunctions).
   9. Ensure that appropriate standard variables are being properly applied by comparing their use in the custom domain to their use in standard domains.
   10. Describe the dataset within the Define-XML document. See Section 3.2, Using the CDISC Domain Models in Regulatory Submissions — Dataset Metadata.
   11. Place any non-standard (SDTM) variables in a Supplemental Qualifier dataset. Mechanisms for representing additional non-standard qualifier variables not described in the general observation classes and for defining relationships between separate datasets or records are described in Section 8.4, Relating Non-standard Variable Values to a Parent Domain.

> *Figure. Creating a New Domain*

### 2.7 SDTM Variables Not Allowed in the SDTMIG

This section identifies those SDTM variables that either (1) should not be used in SDTM-compliant data tabulations of clinical trials data or (2) have not yet been evaluated for use in human clinical trials.

The following SDTM variables, defined for use in nonclinical studies (SEND), must **NEVER** be used in the submission of SDTM-based data for human clinical trials:

- --USCHFL (Interventions, Events, Findings)
- --METHOD (Interventions)
- --RSTIND (Interventions, Findings)
- --RSTMOD (Interventions, Findings)
- --IMPLBL (Findings)
- --RESLOC (Findings)
- --DTHREL (Findings)
- --EXCLFL (Findings)
- --REASEX (Findings)
- FETUSID (Identifiers)
- RPHASE (Timing Variables)
- RPPLDY (Timing Variables)
- RPPLSTDY (Timing Variables)
- RPPLENDY (Timing Variables)
- --NOMDY (Timing Variables)
- --NOMLBL (Timing Variables)
- --RPDY (Timing Variables)
- --RPSTDY (Timing Variables)
- --RPENDY (Timing Variables)
- --DETECT (Timing Variables)

The following variables can be used for nonclinical studies (SEND) but must **NEVER** be used in the Demographics (DM) domain for human clinical trials, where all subjects are human. See Section 9.2, Non-host Organism Identifiers, for information about representing taxonomic information for non-host organisms such as bacteria and viruses.

- SPECIES (Demographics)
- STRAIN (Demographics)
- SBSTRAIN (Demographics)
- RPATHCD (Demographics)

The following variables have not been evaluated for use in human clinical trials and must therefore be used with extreme caution:

- --ANTREG (Findings)
- --CHRON (Findings)
- --DISTR (Findings)
- SETCD (Demographics)

The use of SETCD additionally requires the use of the Trials Sets domain.

The following identifier variable can be used for nonclinical studies (SEND), and may be used in human clinical trials when appropriate:

- POOLID

The use of POOLID additionally requires the use of the Pool Definition dataset.

Other variables defined in the SDTM are allowed for use as defined in this SDTMIG except when explicitly stated. Custom domains, created following the guidance in Section 2.6, Creating a New Domain, may utilize any appropriate qualifier variables from the selected general observation class.

---

## 3 Submitting Data in Standard Format

### 3.1 Standard Metadata for Dataset Contents and Attributes

The SDTMIG provides standard descriptions of some of the most commonly used data domains, with metadata attributes. These include descriptive metadata attributes that should be included in a Define-XML document. In addition, the CDISC domain models include 2 shaded columns that are not sent to the FDA, but which assist sponsors in preparing their datasets:

- The **CDISC Notes** column provides information regarding the relevant use of each variable.
- The **Core** column indicates how a variable is classified (see Section 4.1.5, SDTM Core Designations).

The domain models in Section 6, Domain Models Based on the General Observation Classes, illustrate how to apply the SDTM when creating a specific domain dataset. In particular, these models illustrate the selection of a subset of the variables offered in 1 of the general observation classes, along with applicable timing variables. The models also show how a standard variable from a general observation class should be adjusted to meet the specific content needs of a particular domain, including making the label more meaningful, specifying controlled terminology, and creating domain-specific notes and examples. Thus, the domain models not only demonstrate how to apply the model for the most common domains but also give insight on how to apply general model concepts to other domains not yet defined by CDISC.

### 3.2 Using the CDISC Domain Models in Regulatory Submissions — Dataset Metadata

The Define-XML document that accompanies a submission should also describe each dataset that is included in the submission and describe the natural key structure of each dataset. Most studies will include Demographics (DM) and a set of safety domains based on the 3 general observation classes — typically including Exposure (EX), Concomitant and Prior Medications (CM), Adverse Events (AE), Disposition (DS), Medical History (MH), Laboratory Test Results (LB), and Vital Signs (VS). However, choosing which data to submit will depend on the protocol and the needs of the regulatory review division or agency. Dataset definition metadata should include the dataset filenames, descriptions, locations, structures, class, purpose, and keys, as shown in Section 3.2.1, Dataset-level Metadata. In addition, comments can also be provided where needed.

#### 3.2.1 Dataset-level Metadata

Note that the key variables shown in this table are examples only. A sponsor's actual key structure may be different. The order of classes and datasets in this table is not intended as a normative order of datasets in a submission.

| Dataset | Description | Class | Structure | Purpose | Keys | Location |
|---------|-------------|-------|-----------|---------|------|----------|
| CO | Comments | Special Purpose | One record per comment per subject | Tabulation | STUDYID, USUBJID, IDVAR, COREF, CODTC | co.xpt |
| DM | Demographics | Special Purpose | One record per subject | Tabulation | STUDYID, USUBJID | dm.xpt |
| SE | Subject Elements | Special Purpose | One record per actual Element per subject | Tabulation | STUDYID, USUBJID, ETCD, SESTDTC | se.xpt |
| SM | Subject Disease Milestones | Special Purpose | One record per Disease Milestone per subject | Tabulation | STUDYID, USUBJID, MIDS | sm.xpt |
| SV | Subject Visits | Special Purpose | One record per actual or planned visit per subject | Tabulation | STUDYID, USUBJID, SVTERM | sv.xpt |
| AG | Procedure Agents | Interventions | One record per recorded intervention occurrence per subject | Tabulation | STUDYID, USUBJID, AGTRT, AGSTDTC | ag.xpt |
| CM | Concomitant/Prior Medications | Interventions | One record per recorded intervention occurrence or constant-dosing interval per subject | Tabulation | STUDYID, USUBJID, CMTRT, CMSTDTC | cm.xpt |
| EC | Exposure as Collected | Interventions | One record per protocol-specified study treatment, collected-dosing interval, per subject, per mood | Tabulation | STUDYID, USUBJID, ECTRT, ECSTDTC, ECMOOD | ec.xpt |
| EX | Exposure | Interventions | One record per protocol-specified study treatment, constant-dosing interval, per subject | Tabulation | STUDYID, USUBJID, EXTRT, EXSTDTC | ex.xpt |
| ML | Meal Data | Interventions | One record per food product occurrence or constant intake interval per subject | Tabulation | STUDYID, USUBJID, MLTRT, MLSTDTC | ml.xpt |
| PR | Procedures | Interventions | One record per recorded procedure per occurrence per subject | Tabulation | STUDYID, USUBJID, PRTRT, PRSTDTC | pr.xpt |
| SU | Substance Use | Interventions | One record per substance type per reported occurrence per subject | Tabulation | STUDYID, USUBJID, SUTRT, SUSTDTC | su.xpt |
| AE | Adverse Events | Events | One record per adverse event per subject | Tabulation | STUDYID, USUBJID, AEDECOD, AESTDTC | ae.xpt |
| BE | Biospecimen Events | Events | One record per instance per biospecimen event per biospecimen identifier per subject | Tabulation | STUDYID, USUBJID, BEREFID, BETERM, BESDTC | be.xpt |
| CE | Clinical Events | Events | One record per event per subject | Tabulation | STUDYID, USUBJID, CETERM, CESTDTC | ce.xpt |
| DS | Disposition | Events | One record per disposition status or protocol milestone per subject | Tabulation | STUDYID, USUBJID, DSDECOD, DSSTDTC | ds.xpt |
| DV | Protocol Deviations | Events | One record per protocol deviation per subject | Tabulation | STUDYID, USUBJID, DVTERM, DVSTDTC | dv.xpt |
| HO | Healthcare Encounters | Events | One record per healthcare encounter per subject | Tabulation | STUDYID, USUBJID, HOTERM, HOSTDTC | ho.xpt |
| MH | Medical History | Events | One record per medical history event per subject | Tabulation | STUDYID, USUBJID, MHDECOD | mh.xpt |
| BS | Biospecimen Findings | Findings | One record per measurement per biospecimen identifier per subject | Tabulation | STUDYID, USUBJID, BSREFID, BSTESTCD | bs.xpt |
| CP | Cell Phenotype Findings | Findings | One record per test per specimen per timepoint per visit per subject | Tabulation | STUDYID, USUBJID, CPTESTCD, CPSPEC, VISITNUM, CPTPTREF, CPTPTNUM | cp.xpt |
| CV | Cardiovascular System Findings | Findings | One record per finding or result per time point per visit per subject | Tabulation | STUDYID, USUBJID, VISITNUM, CVTESTCD, CVTPTREF, CVTPTNUM | cv.xpt |
| DA | Product Accountability | Findings | One record per product accountability finding per subject | Tabulation | STUDYID, USUBJID, DATESTCD, DADTC | da.xpt |
| DD | Death Details | Findings | One record per finding per subject | Tabulation | STUDYID, USUBJID, DDTESTCD, DDDTC | dd.xpt |
| EG | ECG Test Results | Findings | One record per ECG observation per replicate per time point or one record per ECG observation per beat per visit per subject | Tabulation | STUDYID, USUBJID, EGTESTCD, VISITNUM, EGTPTREF, EGTPTNUM | eg.xpt |
| FT | Functional Tests | Findings | One record per Functional Test finding per time point per visit per subject | Tabulation | STUDYID, USUBJID, TESTCD, VISITNUM, FTTPTREF, FTTPTNUM | ft.xpt |
| GF | Genomics Findings | Findings | One record per finding per observation per biospecimen per subject | Tabulation | STUDYID, USUBJID, GFTESTCD, GFSPEC, VISITNUM, GFTPTREF, GFTPTNUM | gf.xpt |
| IE | Inclusion/Exclusion Criteria Not Met | Findings | One record per inclusion/exclusion criterion not met per subject | Tabulation | STUDYID, USUBJID, IETESTCD | ie.xpt |
| IS | Immunogenicity Specimen Assessments | Findings | One record per test per visit per subject | Tabulation | STUDYID, USUBJID, ISTESTCD, ISBDAGNT, ISSCMBCL, ISTSTOPO, VISITNUM | is.xpt |
| LB | Laboratory Test Results | Findings | One record per lab test per time point per visit per subject | Tabulation | STUDYID, USUBJID, LBTESTCD, LBSPEC, VISITNUM, LBTPTREF, LBTPTNUM | lb.xpt |
| MB | Microbiology Specimen | Findings | One record per microbiology specimen finding per time point per visit per subject | Tabulation | STUDYID, USUBJID, MBTESTCD, VISITNUM, MBTPTREF, MBTPTNUM | mb.xpt |
| MI | Microscopic Findings | Findings | One record per finding per specimen per subject | Tabulation | STUDYID, USUBJID, MISPEC, MITESTCD | mi.xpt |
| MK | Musculoskeletal System Findings | Findings | One record per assessment per visit per subject | Tabulation | STUDYID, USUBJID, VISITNUM, MKTESTCD, MKLOC, MKLAT | mk.xpt |
| MS | Microbiology Susceptibility | Findings | One record per microbiology susceptibility test (or other organism-related finding) per organism found in MB | Tabulation | STUDYID, USUBJID, MSTESTCD, VISITNUM, MSTPTREF, MSTPTNUM | ms.xpt |
| NV | Nervous System Findings | Findings | One record per finding per location per time point per visit per subject | Tabulation | STUDYID, USUBJID, VISITNUM, NVTPTNUM, NVLOC, NVTESTCD | nv.xpt |
| OE | Ophthalmic Examinations | Findings | One record per ophthalmic finding per method per location, per time point per visit per subject | Tabulation | STUDYID, USUBJID, FOCID, OETESTCD, OETSTDTL, OEMETHOD, OELOC, OELAT, OEDIR, VISITNUM, OEDTC, OETPTREF, OETPTNUM, OEREPNUM | oe.xpt |
| PC | Pharmacokinetics Concentrations | Findings | One record per sample characteristic or time-point concentration per reference time point or per analyte per subject | Tabulation | STUDYID, USUBJID, PCTESTCD, VISITNUM, PCTPTREF, PCTPTNUM | pc.xpt |
| PE | Physical Examination | Findings | One record per body system or abnormality per visit per subject | Tabulation | STUDYID, USUBJID, PETESTCD, VISITNUM | pe.xpt |
| PP | Pharmacokinetics Parameters | Findings | One record per PK parameter per time-concentration profile per modeling method per subject | Tabulation | STUDYID, USUBJID, PPTESTCD, PPCAT, VISITNUM, PPRFTDTC | pp.xpt |
| QS | Questionnaires | Findings | One record per questionnaire per question per time point per visit per subject | Tabulation | STUDYID, USUBJID, QSCAT, QSSCAT, VISITNUM, QSTESTCD | qs.xpt |
| RE | Respiratory System Findings | Findings | One record per finding or result per time point per visit per subject | Tabulation | STUDYID, USUBJID, VISITNUM, RETESTCD, RETPTNUM, REREPNUM | re.xpt |
| RP | Reproductive System Findings | Findings | One record per finding or result per time point per visit per subject | Tabulation | STUDYID, DOMAIN, USUBJID, RPTESTCD, VISITNUM | rp.xpt |
| RS | Disease Response and Clin Classification | Findings | One record per response assessment or clinical classification assessment per time point per visit per subject per assessor per medical evaluator | Tabulation | STUDYID, USUBJID, RSTESTCD, VISITNUM, RSTPTREF, RSTPTNUM, RSEVAL, RSEVALID | rs.xpt |
| SC | Subject Characteristics | Findings | One record per characteristic per visit per subject | Tabulation | STUDYID, USUBJID, SCTESTCD, VISITNUM | sc.xpt |
| SS | Subject Status | Findings | One record per status per visit per subject | Tabulation | STUDYID, USUBJID, SSTESTCD, VISITNUM | ss.xpt |
| TR | Tumor/Lesion Results | Findings | One record per tumor measurement/assessment per visit per subject per assessor | Tabulation | STUDYID, USUBJID, TRTESTCD, TREVALID, VISITNUM | tr.xpt |
| TU | Tumor/Lesion Identification | Findings | One record per identified tumor per subject per assessor | Tabulation | STUDYID, USUBJID, TUEVALID, TULNKID | tu.xpt |
| UR | Urinary System Findings | Findings | One record per finding per location per per visit per subject | Tabulation | STUDYID, USUBJID, VISITNUM, URTESTCD, URLOC, URLAT, URDIR | ur.xpt |
| VS | Vital Signs | Findings | One record per vital sign measurement per time point per visit per subject | Tabulation | STUDYID, USUBJID, VSTESTCD, VISITNUM, VSTPTREF, VSTPTNUM | vs.xpt |
| FA | Findings About Events or Interventions | Findings About | One record per finding, per object, per time point, per visit per subject | Tabulation | STUDYID, USUBJID, FATESTCD, FAOBJ, VISITNUM, FATPTREF, FATPTNUM | fa.xpt |
| SR | Skin Response | Findings About | One record per finding, per object, per time point, per visit per subject | Tabulation | STUDYID, USUBJID, SRTESTCD, SROBJ, VISITNUM, SRTPTREF, SRTPTNUM | sr.xpt |
| TA | Trial Arms | Trial Design | One record per planned Element per Arm | Tabulation | STUDYID, ARMCD, TAETORD | ta.xpt |
| TD | Trial Disease Assessments | Trial Design | One record per planned constant assessment period | Tabulation | STUDYID, TDORDER | td.xpt |
| TE | Trial Elements | Trial Design | One record per planned Element | Tabulation | STUDYID, ETCD | te.xpt |
| TI | Trial Inclusion/Exclusion Criteria | Trial Design | One record per I/E criterion | Tabulation | STUDYID, IETESTCD | ti.xpt |
| TM | Trial Disease Milestones | Trial Design | One record per Disease Milestone type | Tabulation | STUDYID, MIDSTYPE | tm.xpt |
| TS | Trial Summary | Trial Design | One record per trial summary parameter value | Tabulation | STUDYID, TSPARMCD, TSSEQ | ts.xpt |
| TV | Trial Visits | Trial Design | One record per planned Visit per Arm | Tabulation | STUDYID, ARM, VISIT | tv.xpt |
| RELREC | Related Records | Relationship | One record per related record, group of records or dataset | Tabulation | STUDYID, RDOMAIN, USUBJID, IDVAR, IDVARVAL, RELID | relrec.xpt |
| RELSPEC | Related Specimens | Relationship | One record per specimen identifier per subject | Tabulation | STUDYID, USUBJID, REFID | relspec.xpt |
| RELSUB | Related Subjects | Relationship | One record per relationship per related subject per subject | Tabulation | STUDYID, USUBJID, RSUBJID, SREL | relsub.xpt |
| SUPP-- | Supplemental Qualifiers for [domain name] | Relationship | One record per supplemental qualifier per related parent domain record(s) | Tabulation | STUDYID, RDOMAIN, USUBJID, IDVAR, IDVARVAL, QNAM | supp--.xpt |
| OI | Non-host Organism Identifiers | Study Reference | One record per taxon per non-host organism | Tabulation | NHOID, OISEQ | oi.xpt |

Separate Supplemental Qualifier datasets of the form supp--.xpt are required. See Section 8.4, Relating Non-standard Variable Values to a Parent Domain.

##### 3.2.1.1 Primary Keys

The table in Section 3.2.1, Dataset-level Metadata, shows examples of what a sponsor might submit as variables that comprise the primary key for SDTM datasets. Because the purpose of the Keys column is to aid reviewers in understanding the structure of a dataset, sponsors should list all of the natural keys for the dataset. These keys should define uniqueness for records within a dataset, and may define a record sort order. The identified keys for each dataset should be consistent with the description of the dataset structure as described in the Define-XML document.

For all the general observation-class domains (and for some special-purpose domains), the --SEQ variable was created so that a unique record could be identified consistently across all of these domains via its use, along with STUDYID, USUBJID, and DOMAIN. In most domains, --SEQ will be a surrogate key for a set of variables that comprise the natural key. In certain instances, a supplemental qualifier (SUPP--) variable might also contribute to the natural key of a record for a particular domain. See Section 4.1.9, Assigning Natural Keys in the Metadata, for how this should be represented, and for additional information on keys.

> **Definitions**
>
> A **natural key** is a set of data (1 or more columns of an entity) that uniquely identifies that entity and distinguishes it from any other row in the table. The advantage of natural keys is that they exist already; one does not need to introduce a new, "unnatural" value to the data schema. One of the difficulties in choosing a natural key is that just about any natural key one can think of has the potential to change. Because they have business meaning, natural keys are effectively coupled to the business, and they may need to be reworked when business requirements change.
>
> An example of such a change in clinical trials data would be the addition of a position or location that becomes a key in a new study, but which was not collected in previous studies.
>
> A **surrogate key** is a single-part, artificially established identifier for a record. Surrogate key assignment is a special case of derived data, one where a portion of the primary key is derived. A surrogate key is immune to changes in business needs. In addition, the key depends on only 1 field, so it is compact. A common way of deriving surrogate key values is to assign integer values sequentially. The --SEQ variable in the SDTM datasets is an example of a surrogate key for most datasets; in some instances, however, --SEQ might be a part of a natural key as a replacement for what might have been a key (e.g., a repeat sequence number) in the sponsor's database.

##### 3.2.1.2 CDISC Submission Value-level Metadata

In general, findings data models are closely related to normalized, relational data models in a vertical structure of 1 record per observation. Because general observation class data structures are fixed, sometimes information that might appear as columns in a more horizontal (denormalized) structure in presentations and reports will instead be represented as rows in an SDTM Findings structure. Because many different types of observations are all presented in the same structure, there is a need to provide additional metadata to describe expected properties that differentiate (e.g., hematology lab results from serum chemistry lab results in terms of data type, standard units, and other attributes).

For example, the Vital Signs (VS) data domain could contain subject records related to diastolic and systolic blood pressure, height, weight, and body mass index (BMI). These data are all submitted in the normalized SDTM Findings structure of 1 row per vital signs measurement. This means that there could be 5 records per subject (1 for each test or measurement) for a single visit or time point, with the parameter names stored in the Test Code/Name variables, and the parameter values stored in result variables. Because the unique test code/names could have different attributes (e.g., different origins, roles, definitions) there would be a need to provide value-level metadata for this information.

The value-level metadata should be provided as a separate section of the Define-XML document. For details on the CDISC Define-XML standard, see https://www.cdisc.org/standards/data-exchange/define-xml.

#### 3.2.2 Conformance

Conformance with the SDTMIG domain models is minimally indicated by:

- Following the complete metadata structure for data domains
- Following SDTMIG domain models wherever applicable
- Using SDTM-specified standard domain names and prefixes where applicable
- Using SDTM-specified standard variable names
- Using SDTM-specified data types for all variables
- Following SDTM-specified controlled terminology and format guidelines for variables, when provided
- Including all collected and relevant derived data in one of the standard domains, special-purpose datasets, or general observation class structures
- Including all Required and Expected variables as columns in standard domains, and ensuring that all Required variables are populated
- Ensuring that each record in a dataset includes the appropriate Identifier and Timing variables, as well as a Topic variable
- Conforming to all business rules described in the CDISC Notes column and general and domain-specific assumptions
