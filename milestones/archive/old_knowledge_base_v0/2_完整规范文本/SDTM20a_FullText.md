# SDTM v2.0 — Study Data Tabulation Model — Part 1

> **Source:** SDTM_v2.0.pdf | **Version:** 2.0 Final | **Date:** 2021-11-29
> **Publisher:** CDISC Submission Data Standards Team
> **Purpose:** Complete specification text optimized for search and retrieval
> **Split:** Part 1/2 — Sections 1-3.1: Introduction, Model Concepts, General Observation Classes
> **Original:** `SDTM20_FullText.md`
> **Related:** `SDTM20b_FullText.md`

---

## Revision History

| Date | Version |
|---|---|
| 2021-11-29 | 2.0 Final |
| 2019-09-17 | 1.8 Final |
| 2018-03-31 | 1.7 Final |
| 2017-11-08 | 1.6 Final |
| 2016-06-27 | 1.5 Final |
| 2013-11-26 | 1.4 Final |
| 2012-07-16 | 1.3 Final |
| 2008-11-12 | 1.2 Final |
| 2005-04-28 | 1.1 Final |

**Notes to Readers:**
- This is the final Version 2.0 of the SDTM. Includes additional variables related to SDTMIG Version 3.4.
- Changes from the prior version are described in Section 1.4 and Section 7.

---

## Table of Contents

- 1 Introduction
  - 1.1 Purpose
  - 1.2 Implementation Advice for this Model
  - 1.3 Relationship to Prior CDISC Models
  - 1.4 Significant Changes from Prior Versions
- 2 Model Concepts and Terms — Organization of the SDTM
  - 2.1 Model Concepts and Terms — Variables
  - 2.2 Table Structure
- 3 Study Subject Data
  - 3.1 The General Observation Classes
    - 3.1.1 The Interventions Observation Class
    - 3.1.2 The Events Observation Class
    - 3.1.3 The Findings Observation Class
      - 3.1.3.1 Findings About Events or Interventions
    - 3.1.4 Identifiers for All Classes
    - 3.1.5 Timing Variables for All Classes
  - 3.2 Special-purpose Domains
    - 3.2.1 Demographics
    - 3.2.2 Comments
    - 3.2.3 Subject Summary Domains
- 4 Associated Persons Data
- 5 Study-level Data
  - 5.1 The Trial Design Model
  - 5.2 Study References
- 6 Datasets for Representing Relationships
- 7 Changes from SDTM v1.8 to SDTM v2.0
- 8 Proposed Future Changes to the SDTM
- 9 Appendices

---


# 1 Introduction

## 1.1 Purpose
This document describes the Study Data Tabulation Model (SDTM), which defines a standard structure for study 
data tabulations. This document, which supersedes all prior versions, includes numerous changes from the prior
version (SDTM v1.8). These changes are described in Section 1.4, Significant Changes from Prior Versions, and
Section 7, Changes from SDTM v1.8 to SDTM v2.0.
This document is intended for companies and individuals involved in the collection, preparation, and analysis of
study data that may be used for various purposes, including publication, warehousing, meta-analyses, and regulatory
submission. Guidance and specifications for the application of this model are provided separately in the
implementation guides (IGs). Regulatory authorities provide separate guidance, specification, and regulations.
Readers are advised to refer to these documents before preparing a regulatory submission based on the SDTM.

## 1.2 Implementation Advice for this Model
The SDTM has been designed to accommodate the broadest range of human and animal study data in a standardized
manner. This document describes the basic concepts and general structure of the model. Individual implementation
guides (IGs) have been created to provide specific recommendations for numerous domains of data commonly
collected in human, animal, and medical device studies, identifying which variables from a general observation class
may apply. These IGs also describe basic assumptions and business rules, and provide numerous examples for
mapping data to the standard format. Sponsors wishing to represent data in the standard formats should consult the
IGs before preparing datasets based on the SDTM. The following implementation guides have been published by
CDISC:
- The Study Data Tabulation Model Implementation Guide for Human Clinical Trials (SDTMIG)
https://www.cdisc.org/standards/foundational/sdtmig
- The Study Data Tabulation Model Implementation Guide for Medical Devices (SDTMIG-MD)
https://www.cdisc.org/standards/foundational/sdtm-ig-md
- The Study Data Tabulation Model Implementation Guide: Associated Persons (SDTMIG-AP)
https://www.cdisc.org/standards/foundational/sdtmig/sdtmig-ap
- The Standard for Exchange of Nonclinical Data Implementation Guide (SENDIG)
https://www.cdisc.org/standards/foundational/send
- The Standard for Exchange of Nonclinical Data Implementation Guide: Developmental and Reproductive
Toxicology (SENDIG-DART) https://www.cdisc.org/standards/foundational/send/sendig-dart
- The Standard for Exchange of Nonclinical Data Implementation Guide: Animal Rule (SENDIG-AR)
https://www.cdisc.org/standards/foundational/send/sendig-animal-rule
In addition to the IGs, CDISC implementation advice is contained in:
- Multiple indication-specific therapeutic area user guides (TAUGs;
https://www.cdisc.org/standards/therapeutic-areas), which provide examples and implementation advice for
various therapeutic areas.
- Supplements for individual questionnaires, ratings, and scales (QRS;
https://www.cdisc.org/foundational/qrs), which provide information on how to structure the data in a
standard format for public domain and copyright-approved instruments.
- The CDISC Controlled Terminology website page
(https://www.cdisc.org/standards/terminology/controlled-terminology).


## 1.3 Relationship to Prior CDISC Models
This document is a major release of the SDTM. The content of the model has been rearranged and revised to update
explanatory text. Tables have been revised to separate material previously included in the Description column into
separate metadata, as described in the next section.
The SDTM has evolved to support a broad range of study types and regulated products, and is expected to evolve
further to support an even broader range of study data.

## 1.4 Significant Changes from Prior Versions
The SDTM has been designed for backward compatibility; datasets prepared with prior versions should be
compatible with v2.0. In most cases, this means that later versions may add new variables or correct textual errors,
but do not eliminate variables or structures incorporated in prior versions. There are, however, isolated instances
where some older variables may be deprecated in favor of newer, more functional variables.
Reorganization of Content
The content has been reorganized; the content of some sections has been relocated, some section names have
changed, and some sections have been added, most notably:
- Content from Model Fundamentals has been moved to Section 2, Model Concepts and Terms –
Organization of the SDTM, and Section 3, Study Subject Data.
- Content from Applying Model Fundamentals to Associated Persons is now in Section 4, Associated
Persons Data and Section 6.6, Associated Persons Relationships.
- The table contained in Variables Used in Associated Persons Data is now in Section 4, Associated Persons
Data.
- Content from Domain-specific Variables for General Observation Classes was moved to Section 3.1.1, The
Interventions Observation Class, Section 3.1.2, The Events Observation Class, and Section 3.1.3, The
Findings Observation Class.
- Content from SDTM Version History is now in Section 7, Changes from SDTM v1.8 to SDTM v2.0.
- The headings Representing Relationships among Datasets; Records and Datasets for Study References; and
Variable, Dataset, and Section Changes and Additions were determined to be unnecessary extra section
levels and were deleted.
In this version of the SDTM, tables are not numbered. No section contained more than 1 table, so table numbers
added no information to section numbers.
Changes to Structures of Tables
All tables have been updated to include the following columns:
- Variable Name
- Variable Label
- Type
- Format
- Role
- Variable Qualified (when Role is "Variable Qualifier" or "Synonym Qualifier")
- Usage Restrictions
- Variable C-code
- Definition
- Notes
- Examples

Information previously in the Description column has been moved into or replaced by text in new columns.
- Text indicating that variables are not to be used for human clinical trials now appears in the Usage
Restrictions column.
- Examples formerly in the Description column were moved into the Examples column. Example values are
enclosed in quotation marks.
- Other content in the Description column is now in the Notes column, except that for variables with
definitions, definition-like text has been removed.
- Not all variables currently have approved definitions. Missing variable definitions will be added in future
versions of the SDTM as they are developed and approved.
- Not all variables currently have approved c-codes. Missing c-codes will be added in future versions of the
SDTM as they are developed and approved.
Variables that were previously represented in a separate table of Domain-Specific Variables for General Observation
Classes have been moved to tables of variables for the appropriate general observation class, with a note in the
Usage Restrictions column giving the domain(s) to which use is restricted. The role of the domain-specific variable -
-BEATNO was changed to Identifier, so it was included in Section 3.1.4, Identifiers for All Classes, rather than
Section 3.1.3, The Findings Observation Class.
Usage Restrictions previously mentioned only in the SDTMIG and/or the Standard for Exchange of Nonclinical
Data Implementation Guide (SENDIG) were added:
- --OCCUR may not be used in the AE domain.
- --STDTC, --STDY,  --XSTDY, and --CHSTDY may not be used in Findings domains.
For each general observation class, 1 table of variables was created by combining former tables for the topic variable
and the qualifier variables.
Changes to Datasets and Variables
The Subject Visits domain, which was a special-purpose domain, has been moved to an Events class domain. The
variable "SVUPDES" became a domain-specific Events class variable.
A new relationships domain, Related Specimens (RELSPEC), has been added. This domain, first introduced in the
provisional SDTMIG-PGx (now deprecated), had not previously been a part of the SDTM. RELSPEC was added to
this version of the SDTM because the domain was added to SDTMIG v3.4.
SDTM v2.0 does not identify any proposed deprecated variables, as there are no variables to be deprecated at this
time.
The variable APID was removed from Section 3.1.4, Identifiers for All Classes, because APID is only allowed in
AP domains. It is still listed in Section 3, Associated Persons Data.
New variables have been added to the following sections:
- Section 3.1.1, The Interventions Observation Class
- Section 3.1.2, The Events Observation Class
- Section 3.1.3, The Findings Observation Class
- Section 3.1.5, Timing Variables for All Classes
- Section 3.2.3.1, Subject Elements
The role of the --LOINC variable in Section 3.1.3, The Findings Observation Class, was changed from Synonym
Qualifier of --TESTCD to Record Qualifier, because a single value of --TESTCD may be associated with multiple
values of --LOINC, depending on the values of other variables, such as --SPEC and --METHOD.
The order of --METHOD within Interventions Variables in Section 3.1.1, The Interventions Observation Class, was
changed so that the variable appears after --PORTOT, rather than after --LOC. This change was made so that --METHOD would appear after the variable qualifiers of --LOC rather than immediately after --LOC.

A number of changes are proposed for the next version of the SDTM. See Section 8, Proposed Future Changes to
the SDTM, for the rationale for these proposed changes.


---


# 2 Model Concepts and Terms – Organization of
the SDTM
The SDTM provides a general framework for describing the organization of information collected during human and
animal studies. The model is built around the concept of observations, which consist of discrete pieces of
information collected during a study. Observations normally correspond to rows in a dataset. A domain is
a collection of observations on a particular topic (see Concept Map, below). For example, "Subject 101 had an
adverse event of mild nausea starting on study day 6" is an observation belonging to the Adverse Events domain in a
clinical trial.
The primary purpose of the SDTM is to represent data about study subjects—which may be humans or animals—or
medical devices. The SDTM includes a general model for representing data in 3 "general observation" classes.
Within those classes, data are grouped by topic into domains, represented in separate datasets. The 3 general
observation classes (i.e., Interventions, Events, Findings) are described further in Section 3.1, The General
Observation Classes. Additional special-purpose datasets about individuals are described in Section 3.2, Special-
purpose Domains.
Studies sometimes include data about "associated persons" who are not study subjects; these data are represented in
domains based on the domains used to represent data about study subjects. The structure of these domains is
described in Section 4, Associated Persons Data.
The SDTM also includes a set of tables for representing data at the study level. These datasets are specified in
Section 5, Study-level Data.
The last group of datasets in the SDTM are those that describe relationships among datasets and records. These
datasets are specified in Section 6, Datasets for Representing Relationships.
Concept Map. Relationships Between SDTM Domains


## 2.1 Model Concepts and Terms – Variables
All datasets are structured as flat files with rows representing observations and columns representing variables; each
dataset is described by metadata definitions that provide information about the variables used in the dataset.
Metadata are described in the CDISC Define-XML specification, available at https://www.cdisc.org/standards/data-
exchange/define-xml.
Each observation consists of a series of named variables. Each variable, which normally corresponds to a column in
a dataset, can be classified according to its role. A role describes the type of information conveyed by the variable
about each distinct observation and how it can be used. There are variables which play different roles in different
datasets. This is most common for variables which appear in both trial design datasets and general observation class
datasets. For example, ARMCD is the topic variable in Trial Arms (TA), but a record qualifier in Demographics
(DM) and Trial Visits (TV). Variables which appear in multiple general observation classes have the same role,
although the variable qualified by a variable qualifier or synonym qualifier can be different in different general
observation classes. For example, --MODIFY qualifies --TRT in interventions, --TERM in events, and --ORRES in
findings.
SDTM variables can be classified into 5 major roles:
- Identifier variables, such as those that identify the study, the subject involved in the study, the domain, and
the sequence number of the record;
- Topic variables, which specify the focus of the observation (e.g., the name of a lab test);
- Timing variables, which describe the timing of an observation (e.g., start date, end date);
- Qualifier variables, which include additional illustrative text or numeric values that describe the results or
additional traits of the observation (e.g., units, descriptive adjectives); and
- Rule variables, which describe the conditions for starting, ending, branching, or looping in the Trial Design
model.
The set of Qualifier variables can be further categorized into 5 subclasses:
- Grouping Qualifiers, used to group together a collection of observations within the same domain (e.g.,
categories or subcategories);
- Result Qualifiers, which describe the specific results associated with the topic variable in a Findings dataset
and that answer the question raised by the topic variable;
- Synonym Qualifiers specifying an alternative name for a particular variable in an observation (e.g., coded
version of a verbatim topic variable or the name associated with a test code);
- Record Qualifiers, which define additional attributes of the observation record as a whole, rather than
describing a particular variable within a record (e.g., for a lab test, the specimen type and the name of lab
that performed the test); and
- Variable Qualifiers used to further modify or describe 1 or more of a specific set of variables within an
observation and which are only meaningful in the context of the variable they qualify (e.g., the unit for a
numeric test result or a medication dose, the laterality of an anatomic location).
The SDTM includes variable metadata for the standard variables; variable metadata attributes are described in
Section 2.2, Table Structure.
All datasets for data about individuals and for data about a study include the variable DOMAIN, a code that should
be used in the dataset name. Some relationship datasets include the variable RDOMAIN, to describe a relationship
to a domain for data about individuals. The Comments special-purpose domain includes the variable RDOMAIN,
but other special-purpose domains do not. The Device-subject Relationships dataset includes the variable DOMAIN,
but other study reference datasets do not.
The SDTM is structured so that data can be represented in SAS v5 transport files, the file format accepted by the US
Food and Drug Administration (FDA) and other regulatory authorities. This imposes certain restrictions on
variables. Note that the SDTM type specified in this document is either character or numeric, as these are the only
types supported by SAS v5 transport files. Define-XML provides more descriptive data types (e.g., integer, float,

date, datetime); see the Define-XML specification for information about how to represent SDTM types using
Define-XML data types.

## 2.2 Table Structure
Tables in this document include the following variable metadata:
- Variable Name
- Variable Label
- Type (i.e., SAS data type, as described in Section 2.1, Model Concepts and Terms – Variables)
- Format (an ISO format standard or a description such as "number-number")
- Role (as defined in Section 2.1)
- Variable(s) Qualified (for the variables with a role of Variable Qualifier or Synonym Qualifier)
- Usage Restrictions (rules for when a variable can or cannot be used in a particular kind of trial, a particular
class, or a particular domain)
- Variable C-code (the concept code associated with a variable definition by the National Cancer Institute
Enterprise Vocabulary Services (NCI-EVS))
- Definition (published as part of CDISC Controlled Terminology through the NCI-EVS)
- Notes (descriptive information not covered elsewhere)
- Examples (sample values or descriptions of kinds of information used to populate the variable)
Information on usage restrictions and examples that were in the Description column in SDTM v1.x tables have been
moved to the Usage Restrictions and Examples columns. Other information previously in the Description column
has been moved to the Notes column, except that definition-like information has been removed for variables which
have approved definitions.

---

# 3 Study Subject Data
Observations about study subjects are normally represented in a series of domains. A domain is defined as a
collection of logically related observations with a common topic. The logic of the relationship may pertain to the
scientific subject matter of the data or to its role in the trial. For example, "Subject 101 had an adverse event of mild
nausea starting on study day 6" is an observation belonging to the Adverse Events (AE) domain in a clinical trial.
SDTM datasets that represent data about study subjects are of 2 types: general observation class datasets and
special-purpose datasets. General observation class domains conform to general structures for 1 of 3 classes:
findings, events, and interventions. The data for a study would generally include multiple domains in each general
observation class. In contrast to general observation class models on which individual domains can be based,
special-purpose domains are specified completely.
Domains based on the general observation classes are specified in SDTM implementation guides (see Section 1.2,
Implementation Advice for this Model).
Each study subject domain dataset is distinguished by a unique 2-character code. This code, which is stored in the
SDTM variable named DOMAIN, is used in the dataset name, as the value of the DOMAIN variable in that dataset,
and as a prefix for most variable names in that dataset.
Domain codes are also used in RDOMAIN, a variable that is included in several relationship datasets and in the
Comments special-purpose domain.

## 3.1 The General Observation Classes
The majority of observations collected during a study can be divided among 3 general observation classes:
Interventions, Events, and Findings.
- The Interventions Observation Class represents investigational, therapeutic, and other treatments that are
administered to or used by a subject (with some actual or expected physiological effect). This includes
treatments specified by the study protocol (i.e., "exposure").
- The Events Observation Class represents planned protocol milestones such as randomization and study
completion, and occurrences, conditions, or incidents independent of planned study evaluations occurring
during the study (e.g., adverse events) or prior to the study (e.g., medical history).
- The Findings Observation Class represents observations resulting from planned evaluations to address
specific tests or questions such as laboratory tests, electrocardiogram (ECG) testing, and questions listed on
questionnaires. The Findings class also includes a subtype, Findings About, which is used to record
findings related to observations in the Interventions or Events classes.
Datasets based on any of the general observation classes share a set of common identifier and timing variables (see
Section 3.1.4, Identifiers for All Classes, and Section 3.1.5, Timing Variables for All Classes). As a general rule, any
valid identifier or timing variable is permissible for use in any dataset based on a general observation class.
The SDTM is the foundation for many implementations. SDTM implementation guides specify particular domains
based on the general observation classes. Domain specification tables in the implementation guides describe which
variables must be included in the domain. Not all variables described in the tables in this document (SDTM tables)
are appropriate for all domains in all implementations. The SDTM includes information on variables which are not
to be used in human clinical trials. Refer to the implementation guides for specific information on any identifier or
timing variables that are not allowed in a particular observation class domain.
In the tables in this document, the presence of 2 hyphens before the variable name (e.g., --TRT) is used to indicate
the required use of a prefix based on the 2-character domain code. The domain code is used as a variable prefix to
minimize the risk of difficulty when merging or joining domains for reporting purposes. The variable with 2
hyphens may be referred to as a "root" variable.
Domain-specific variables, a concept introduced in SDTM v1.5, are for use in a limited number of designated
domains based on general observation classes and will be identified in the appropriate implementation guide. The
variable names include the specific domain prefix. Domain-specific variables are included in the table of general


### 3.1.1 The Interventions Observation Class


**Interventions—Topic and Qualifier Variables—One Record per Constant-dosing Interval or Intervention Episode**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | --TRT | Name of Treatment | Char | Topic |  |  | C82542 |
| 2 | --MODIFY | Modified Treatment Name | Char | Synonym Qualifier | --TRT |  | C170998 |
| 3 | --DECOD | Standardized Treatment Name | Char | Synonym Qualifier | --TRT |  | C170991 |
| 4 | --MOOD | Mood | Char | Record Qualifier |  |  | C117051 |
| 5 | --CAT | Category | Char | Grouping Qualifier |  |  | C25372 |
| 6 | --SCAT | Subcategory | Char | Grouping Qualifier |  |  |  |
| 7 | --PRESP | Pre-Specified | Char | Variable Qualifier | --TRT | Not in nonclinical trials | C82510 |
| 8 | --OCCUR | Occurrence Indicator | Char | Record Qualifier |  |  | C171000 |
| 9 | --REASOC | Reason for Occur Value | Char | Record Qualifier |  |  |  |
| 10 | --STAT | Completion Status | Char | Record Qualifier |  |  |  |
| 11 | --REASND | Reason Not Done | Char | Record Qualifier |  |  | C82556 |
| 12 | --CNTMOD | Contact Mode | Char | Record Qualifier |  |  |  |
| 13 | --EPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier |  |  |  |
| 14 | --INDC | Indication | Char | Record Qualifier |  |  | C41184 |
| 15 | --CLAS | Class | Char | Variable Qualifier | --TRT |  | C170987 |
| 16 | --CLASCD | Class Code | Char | Variable Qualifier | --TRT |  | C170988 |
| 17 | --DOSE | Dose | Num | Record Qualifier |  |  | C25488 |
| 18 | --DOSTXT | Dose Description | Char | Record Qualifier |  |  | C70961 |
| 19 | --DOSU | Dose Units | Char | Variable Qualifier | --DOSE; --DOSTXT; --DOSTOT |  | C73558 |
| 20 | --TDOSD | Toxic/Physiologic Dose Descr | Char | Record Qualifier |  |  |  |
| 21 | --FTDOSD | Factor for Toxic/Physiologic Dose Descr | Num | Variable Qualifier | --TDOSD |  |  |
| 22 | --DOSFRM | Dose Form | Char | Variable Qualifier | --TRT |  | C42636 |
| 23 | --DOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier |  |  | C15682 |
| 24 | --DOSTOT | Total Daily Dose | Num | Record Qualifier |  |  | C70888 |
| 25 | --DOSRGM | Intended Dose Regimen | Char | Record Qualifier |  |  | C71137 |
| 26 | --ROUTE | Route of Administration | Char | Record Qualifier |  |  | C38114 |
| 27 | --LOT | Lot Number | Char | Record Qualifier |  |  | C70848 |
| 28 | --LOC | Location of Administration | Char | Record Qualifier |  |  |  |
| 29 | --METHOD | Method of Administration | Char | Record Qualifier |  | Not in human clinical trials; EX domain only |  |
| 30 | --LAT | Laterality | Char | Variable Qualifier | --LOC |  |  |
| 31 | --DIR | Directionality | Char | Variable Qualifier | --LOC |  |  |
| 32 | --PORTOT | Portion or Totality | Char | Variable Qualifier | --LOC |  |  |
| 33 | --FAST | Fasting Status | Char | Record Qualifier |  |  | C93566 |
| 34 | --PSTRG | Pharmaceutical Strength | Num | Record Qualifier |  |  | C53294 |
| 35 | --PSTRGU | Pharmaceutical Strength Units | Char | Variable Qualifier | --PSTRG |  | C117055 |
| 36 | --TRTV | Treatment Vehicle | Char | Record Qualifier |  |  | C927 |
| 37 | --VAMT | Treatment Vehicle Amount | Num | Record Qualifier |  |  | C82553 |
| 38 | --VAMTU | Treatment Vehicle Amount Units | Char | Variable Qualifier | --VAMT |  | C82583 |
| 39 | --ADJ | Reason for Dose Adjustment | Char | Record Qualifier |  |  | C82555 |
| 40 | --RSDISC | Reason for Treatment Discontinuation | Char | Record Qualifier |  |  |  |
| 41 | --USCHFL | Unscheduled Flag | Char | Record Qualifier |  | Not in human clinical trials | C170510 |
| 42 | --RSTIND | Restraint Indicator | Char | Record Qualifier |  | Not in human clinical trials |  |
| 43 | --RSTMOD | Restraint Mode | Char | Record Qualifier |  | Not in human clinical trials |  |

**Variable Definitions:**

- **--TRT**: The reported name of the drug, procedure, or therapy. | *Notes:* The topic for the intervention observation, usually the verbatim name of the treatment, drug, medicine, or therapy given during the dosing interval for the observation.
- **--MODIFY**: A value which represents an alteration to a collected value for coding purposes. | *Notes:* If the value for --TRT is modified for coding purposes, then the modified text is placed here.
- **--DECOD**: Standardized or dictionary- derived text for the description of an event or intervention. | *Notes:* Equivalent to the generic drug name in WHODrug, or a term in SNOMED, ICD-9, or other published or sponsor- defined dictionaries.
- **--MOOD**: The state that may be applied to a record to indicate its phase in a life cycle or business process (e.g., scheduled, performed). | *Examples:* "SCHEDULED", "PERFORMED"
- **--CAT**: A grouping or classification of the topic of the finding, event, or intervention.
- **--SCAT**: A further grouping or classification of the category for the topic of the finding, event, or intervention. | *Notes:* The category is in --CAT.
- **--PRESP**: An indication that the event or intervention was prospectively stated or detailed on the CRF. | *Notes:* Values should be "Y" or null.
- **--OCCUR**: An indication as to whether a prespecified event or intervention has occurred.
- **--REASOC**: *Notes:* --REASOC is the reason the intervention did or did not occur, according to the value in --OCCUR. This does not replace --INDC.
- **--STAT**: *Notes:* Used to indicate when a question about the occurrence of a prespecified intervention was not answered. Should be null or have a value of "NOT DONE".
- **--REASND**: The explanation for why requested information was not available. | *Notes:* Used in conjunction with --STAT when value is "NOT DONE".
- **--CNTMOD**: *Notes:* The way in which the event, visit, or contact was conducted.
- **--EPCHGI**: *Notes:* Indicates whether the intervention was changed due to an epidemic or pandemic.
- **--INDC**: The sign, symptom, or condition that is the basis for initiation of a treatment.
- **--CLAS**: A standardized or dictionary- derived name for a grouping of drugs, procedures, or therapies.
- **--CLASCD**: A standardized or dictionary- derived short sequence of characters used to represent a grouping of drugs, procedures, or therapies. | *Notes:* Used to represent code for --CLAS.
- **--DOSE**: The quantity of an agent (e.g., drug, substance, radiation) taken or absorbed at a single administration. | *Notes:* Not populated when --DOSTXT is populated.
- **--DOSTXT**: A textual description of the quantity of an agent (e.g., drug, substance, radiation) taken or absorbed at a single administration. | *Notes:* Not populated when --DOSE is populated. | *Examples:* "200-400"
- **--DOSU**: The unit of measure for the administered agent (e.g., drug, substance, radiation), using standardized values. | *Notes:* Units for --DOSE, --DOSTOT, or --DOSTXT. | *Examples:* "ng", "mg", "mg/kg"
- **--TDOSD**: *Notes:* A description of a statistically derived estimate of a dose with a certain toxicological or physiological effect in a population, based on data from a dose-response study. | *Examples:* "LD50", "ED90"
- **--FTDOSD**: *Notes:* The quantity given for the multiplier of --TDOSD. | *Examples:* If --TDOSD="LD50" and --FTDOSD="5", then the value represented by --DOSE and --DOSU is 5 times the LD50.
- **--DOSFRM**: Physical characteristics of a drug product, (e.g., tablet, capsule, or solution) that contains a drug substance, generally (but not necessarily) in association with one or more other ingredients. | *Examples:* "TABLET", "CAPSULE"
- **--DOSFRQ**: The number of times that an agent (e.g., drug, substance, radiation) is administered per unit of time. | *Examples:* "Q2H", "QD", "PRN"
- **--DOSTOT**: The quantity of an agent (e.g., drug, substance, radiation) taken or absorbed on a single day. | *Notes:* Uses the units in --DOSU.
- **--DOSRGM**: The planned schedule for the administration of an agent (e.g., drug, substance, radiation). | *Examples:* "TWO WEEKS ON, TWO WEEKS OFF"
- **--ROUTE**: Designation of the part of the body through which or into which, or the way in which, a substance is introduced. | *Examples:* "ORAL", "INTRAVENOUS"
- **--LOT**: An identifier assigned by the manufacturer or distributor to a specific quantity of manufactured material or product. | *Notes:* Although the identifier for a lot is generally called a lot number, it may contain characters other than digits (e.g., letters).
- **--LOC**: *Notes:* Anatomical location of an intervention, such as an injection site. | *Examples:* "ARM" for an injection
- **--METHOD**: Method of administration of the treatment. | *Examples:* "INFUSION" when ROUTE is "INTRAVENOUS"
- **--LAT**: *Notes:* Qualifier for anatomical location further detailing laterality of intervention administration. | *Examples:* "RIGHT", "LEFT", "BILATERAL"
- **--DIR**: *Notes:* Qualifier for anatomical location further detailing directionality of intervention administration. | *Examples:* "ANTERIOR", "LOWER", "PROXIMAL"
- **--PORTOT**: *Notes:* Qualifier for anatomical location further detailing the distribution, which means arrangement of or apportioning of the intervention administration. | *Examples:* "ENTIRE", "SINGLE", "SEGMENT", "MANY"
- **--FAST**: An indication as to whether a subject has abstained from food and liquid for a prescribed amount of time. | *Notes:* Valid values include "Y", "N", "U", or null if not relevant.
- **--PSTRG**: The amount of active ingredient per unit of pharmaceutical dosage form. | *Examples:* "50", "300"
- **--PSTRGU**: The unit of measure for the amount of active ingredient per unit of pharmaceutical dosage form, using standardized values. | *Notes:* Unit for --PSTRG. | *Examples:* "mg/TABLET", "mg/mL"
- **--TRTV**: A carrier or inert medium in which a medicinally active agent is administered. | *Examples:* "SALINE"
- **--VAMT**: Amount of the prepared product (treatment plus vehicle) administered. | *Notes:* Note: Should not be diluent amount alone.
- **--VAMTU**: The unit of measure for the prepared product (treatment plus vehicle) using standardized values. | *Examples:* "mL", "mg"
- **--ADJ**: The explanation given for why a dose was changed as | *Examples:* "ADVERSE EVENT", "INSUFFICIENT
- **--RSDISC**: *Notes:* Reason the treatment was discontinued.
- **--USCHFL**: An indication that the performed test or observation was done at a time that was not planned. | *Notes:* If a test or observation was performed based upon a schedule defined in the protocol, this flag should be null. Expected values are "Y" or null. This variable would not be needed when information on planned assessments is provided, such as when the Trial Visits (TV) and Subject Visits (SV) domains are used.
- **--RSTIND**: *Notes:* An indicator as to whether the animal subject was restrained during the intervention period. Expected values are "Y" or null.
- **--RSTMOD**: *Notes:* A description of whether the restraint was physical and/or chemical.

### 3.1.2 The Events Observation Class


**Events—Topic and Qualifier Variables—One Record per Event**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | --TERM | Reported Term | Char | Topic |  |  | C82571 |
| 2 | --MODIFY | Modified Reported Term | Char | Synonym Qualifier | --TERM |  | C170998 |
| 3 | --LLT | Lowest Level Term | Char | Variable Qualifier | --TERM | Not in nonclinical trials | C71886 |
| 4 | --LLTCD | Lowest Level Term Code | Num | Variable Qualifier | --LLT | Not in nonclinical trials | C117048 |
| 5 | --DECOD | Dictionary-Derived Term | Char | Synonym Qualifier | --TERM |  | C170991 |
| 6 | --EVDTYP | Medical History Event Date Type | Char | Variable Qualifier | --STDTC; --ENDTC | MH domain only |  |
| 7 | --PTCD | Preferred Term Code | Num | Variable Qualifier | --DECOD | Not in nonclinical trials | C117056 |
| 8 | --HLT | High Level Term | Char | Variable Qualifier | --TERM | Not in nonclinical trials | C71880 |
| 9 | --HLTCD | High Level Term Code | Num | Variable Qualifier | --HLT | Not in nonclinical trials | C117047 |
| 10 | --HLGT | High Level Group Term | Char | Variable Qualifier | --TERM | Not in nonclinical trials | C71889 |
| 11 | --HLGTCD | High Level Group Term Code | Num | Variable Qualifier | --HLGT | Not in nonclinical trials | C117046 |
| 12 | --CAT | Category | Char | Grouping Qualifier |  |  | C25372 |
| 13 | --SCAT | Subcategory | Char | Grouping Qualifier |  |  |  |
| 14 | --PRESP | Pre-Specified | Char | Variable Qualifier | --TERM |  | C82510 |
| 15 | --OCCUR | Occurrence Indicator | Char | Record Qualifier |  | Not in AE domain | C171000 |
| 16 | --REASOC | Reason for Occur Value | Char | Record Qualifier |  | Not in AE domain |  |
| 17 | --STAT | Completion Status | Char | Record Qualifier |  | Not in AE domain |  |
| 18 | --REASND | Reason Not Done | Char | Record Qualifier |  | Not in AE domain | C82556 |
| 19 | --BODSYS | Body System or Organ Class | Char | Record Qualifier |  |  | C170986 |
| 20 | --BDSYCD | Body System or Organ Class Code | Num | Variable Qualifier | --BODSYS | Not in nonclinical trials | C170985 |
| 21 | --SOC | Primary System Organ Class | Char | Variable Qualifier | --TERM | Not in nonclinical trials | C71888 |
| 22 | --SOCCD | Primary System Organ Class Code | Num | Variable Qualifier | --SOC | Not in nonclinical trials | C117059 |
| 23 | --CNTMOD | Contact Mode | Char | Record Qualifier |  |  |  |
| 24 | --EPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier |  |  |  |
| 25 | --LOC | Location of Event | Char | Record Qualifier |  |  |  |
| 26 | --LAT | Laterality | Char | Variable Qualifier | --LOC |  |  |
| 27 | --DIR | Directionality | Char | Variable Qualifier | --LOC |  |  |
| 28 | --PORTOT | Portion or Totality | Char | Variable Qualifier | --LOC |  |  |
| 29 | --PARTY | Accountable Party | Char | Record Qualifier |  | Not in nonclinical trials | C117052 |
| 30 | --PRTYID | Identification of Accountable Party | Char | Variable Qualifier | --PARTY | Not in nonclinical trials | C117054 |
| 31 | --SEV | Severity/Intensity | Char | Record Qualifier |  |  | C25676 |
| 32 | --SER | Serious Event | Char | Record Qualifier |  |  | C82578 |
| 33 | --ACN | Action Taken with Study Treatment | Char | Record Qualifier |  |  | C49499 |
| 34 | --ACNOTH | Other Action Taken | Char | Record Qualifier |  |  | C82509 |
| 35 | --ACNDEV | Action Taken with Device | Char | Record Qualifier |  |  | C117037 |
| 36 | --REL | Causality | Char | Record Qualifier |  |  | C103163 |
| 37 | --RLDEV | Relationship of Event to Device | Char | Record Qualifier |  |  |  |
| 38 | --RELNST | Relationship to Non- Study Treatment | Char | Record Qualifier |  |  | C82564 |
| 39 | --PATT | Pattern of Event | Char | Record Qualifier |  |  | C82550 |
| 40 | --OUT | Outcome of Event | Char | Record Qualifier |  |  | C171001 |
| 41 | --SCAN | Involves Cancer | Char | Record Qualifier |  | Not in nonclinical trials | C82561 |
| 42 | --SCONG | Congenital Anomaly or Birth Defect | Char | Record Qualifier |  | Not in nonclinical trials | C2849 |
| 43 | --SDISAB | Persist or Signif Disability/Incapacity | Char | Record Qualifier |  | Not in nonclinical trials | C68606 |
| 44 | --SDTH | Results in Death | Char | Record Qualifier |  | Not in nonclinical trials | C82549 |
| 45 | --SHOSP | Requires or Prolongs Hospitalization | Char | Record Qualifier |  | Not in nonclinical trials | C68605 |
| 46 | --SLIFE | Is Life Threatening | Char | Record Qualifier |  | Not in nonclinical trials | C82508 |
| 47 | --SOD | Occurred with Overdose | Char | Record Qualifier |  | Not in nonclinical trials | C82548 |
| 48 | --SMIE | Other Medically Important Serious Event | Char | Record Qualifier |  | Not in nonclinical trials | C82521 |
| 49 | --SINTV | Needs Intervention to Prevent Impairment | Char | Record Qualifier |  | AE domain only |  |
| 50 | --UNANT | Unanticipated Adverse Device Effect | Char | Record Qualifier |  | AE domain only |  |
| 51 | --RLPRT | Rel of AE to Device- Related Procedure | Char | Record Qualifier |  | AE domain only |  |
| 52 | --RLPRC | Rel of AE to Non- Dev-Rel Study Activity | Char | Record Qualifier |  | AE domain only |  |
| 53 | --CONTRT | Concomitant or Additional Trtmnt Given | Char | Record Qualifier |  |  | C170989 |
| 54 | --TOX | Toxicity | Char | Variable Qualifier | --TOXGR |  | C27990 |
| 55 | --TOXGR | Toxicity Grade | Char | Record Qualifier |  |  | C82528 |
| 56 | --USCHFL | Unscheduled Flag | Char | Record Qualifier |  | Not in human clinical trials | C170510 |

**Variable Definitions:**

- **--TERM**: The collected name for an event observation. | *Notes:* The verbatim or prespecified name of the event.
- **--MODIFY**: A value which represents an alteration to a collected value for coding. | *Notes:* If the value for --TERM is modified for coding purposes, then the modified text is placed here.
- **--LLT**: The lowest-level term assigned to the event from MedDRA.
- **--LLTCD**: The lowest-level term code assigned to the event from MedDRA.
- **--DECOD**: Standardized or dictionary-derived text for the description of an event or intervention. | *Notes:* Equivalent to the Preferred Term ("PT" in MedDRA).
- **--EVDTYP**: *Notes:* Specifies the aspect of the medical condition or event by which MHSTDTC and/or the MHENDTC is defined. | *Examples:* "DIAGNOSIS", "SYMPTOM ONSET", "DISEASE RELAPSE"
- **--PTCD**: The preferred term code assigned to the event from the MedDRA dictionary.
- **--HLT**: The high-level term from the primary hierarchy assigned to the event from MedDRA.
- **--HLTCD**: The high-level term code from the primary hierarchy assigned to the event from MedDRA.
- **--HLGT**: The high-level group term from the primary hierarchy assigned to the event from MedDRA.
- **--HLGTCD**: The high-level group term code from the primary hierarchy assigned to the event from MedDRA.
- **--CAT**: A grouping or classification of the topic of the finding, event, or intervention.
- **--SCAT**: A further grouping or classification of the category for the topic of the finding, event, or intervention. | *Notes:* The category is in --CAT.
- **--PRESP**: An indication that the event or intervention was prospectively stated or detailed on the CRF. | *Notes:* Value is "Y" for prespecified events, null for spontaneously reported events.
- **--OCCUR**: An indication as to whether a prespecified event or intervention has occurred.
- **--REASOC**: *Notes:* --REASOC is the reason the event did or did not occur, according to the value in --OCCUR.
- **--STAT**: *Notes:* Used to indicate when a question about the occurrence of a prespecified event was not answered. Should be null or have a value of "NOT DONE".
- **--REASND**: The explanation for why requested information was not available. | *Notes:* Used in conjunction with --STAT when its value is "NOT DONE".
- **--BODSYS**: A standardized or dictionary-derived name for the body system or organ class. | *Notes:* Body system or system organ class assigned for analysis from a standard hierarchy (e.g., MedDRA) associated with an event. | *Examples:* "GASTROINTESTINAL DISORDERS"
- **--BDSYCD**: A standardized or dictionary-derived short sequence of characters used to represent the body system or organ class. | *Notes:* MedDRA System Organ Class code corresponding to --BODSYS assigned for analysis.
- **--SOC**: The system organ class from the primary hierarchy assigned in the MedDRA dictionary.
- **--SOCCD**: The system organ class code from the primary hierarchy assigned in the MedDRA dictionary.
- **--CNTMOD**: *Notes:* The way in which the event, visit, or contact was conducted. | *Examples:* "IN PERSON", "TELEPHONE", "IVRS"
- **--EPCHGI**: *Notes:* Indicates whether the event was changed due to an epidemic or pandemic. Not the same as whether a medical condition was caused by an epidemic or pandemic.
- **--LOC**: *Notes:* Describes anatomical location relevant for the event. | *Examples:* "ARM" for skin rash
- **--LAT**: *Notes:* Qualifier for anatomical location, further detailing laterality. | *Examples:* "RIGHT", "LEFT", "BILATERAL"
- **--DIR**: *Notes:* Qualifier for anatomical location, further detailing directionality. | *Examples:* "ANTERIOR", "LOWER", "PROXIMAL"
- **--PORTOT**: *Notes:* Qualifier for anatomical location, further detailing the distribution (i.e., arrangement of, apportioning of). | *Examples:* "ENTIRE", "SINGLE", "SEGMENT", "MANY"
- **--PARTY**: The role of the individual or entity responsible for the receipt of the transferred object (e.g., device, specimen). | *Notes:* The party could be an individual (e.g., subject), an organization (e.g., sponsor), or a location that is a proxy for an individual or organization (e.g., site). It is usually a somewhat general term that is further identified in the --PRTYID variable.
- **--PRTYID**: A sequence of characters used to uniquely identify the individual or entity responsible for the receipt of the transferred object (e.g., device, specimen). | *Notes:* Used in conjunction with --PARTY.
- **--SEV**: The quality or degree of harm associated with a finding or event, as collected. | *Examples:* "MILD", "MODERATE", "SEVERE"
- **--SER**: A collected indication as to whether an event meets regulatory criteria for seriousness. | *Notes:* Valid values are "Y" and "N".
- **--ACN**: An action taken with study treatment as the result of the event. | *Examples:* "DOSE INCREASED", "DOSE NOT CHANGED"
- **--ACNOTH**: An action taken unrelated to study treatment, as the result of the event.
- **--ACNDEV**: An action taken with a device as the result of the event. | *Notes:* The device may or may not be the device under study.
- **--REL**: The investigator's assessment of the likelihood that the study | *Examples:* "NOT RELATED", "UNLIKELY RELATED", "POSSIBLY RELATED", "RELATED"
- **--RLDEV**: A judgement as to the likelihood that the device caused the event. | *Notes:* The device may or may not be the device under study. Controlled terminology from EC Directive MEDDEV 2.7/3 March 2015 is required in EU but not US. | *Examples:* "CAUSAL", "UNLIKELY"
- **--RELNST**: The investigator's assessment of the causal relationship of the event to a non-study treatment. | *Examples:* "MORE LIKELY RELATED TO ASPIRIN USE"
- **--PATT**: A characterization of the temporal pattern of occurrences of the event. | *Examples:* "INTERMITTENT", "CONTINUOUS", "SINGLE EVENT"
- **--OUT**: The status associated with the result or conclusion of the event. | *Examples:* "RECOVERED/RESOLVED", "FATAL"
- **--SCAN**: An indication as to whether the reason an event was serious was because the event was associated with cancer. | *Notes:* Valid values are "Y", "N", and null.
- **--SCONG**: An indication as to whether the reason an event is serious is because the event is associated with congenital anomaly or birth defect in an offspring of the subject. | *Notes:* Valid values are "Y", "N", and null.
- **--SDISAB**: An indication as to whether the reason an event is serious is because the event resulted in a significant, persistent, or permanent change, impairment, damage, or disruption in the subject's body function/structure, physical activities, and/or quality of life. | *Notes:* Valid values are "Y", "N", and null.
- **--SDTH**: An indication as to whether the reason an event is serious is because the event resulted in death. | *Notes:* Valid values are "Y", "N", and null.
- **--SHOSP**: An indication as to whether the reason an event is serious is because the event resulted in or prolonged hospitalization. | *Notes:* Valid values are "Y", "N", and null.
- **--SLIFE**: An indication as to whether the reason an event is serious is | *Notes:* Valid values are "Y", "N", and null.
- **--SOD**: An indication as to whether the reason an event is serious is because the event is associated with overdose. | *Notes:* Valid values are "Y", "N", and null.
- **--SMIE**: An indication as to whether the reason an event is serious is because the event may jeopardize the subject and may require intervention to prevent one of the other outcomes associated with serious adverse events. | *Notes:* Valid values are "Y", "N", and null.
- **--SINTV**: *Notes:* Valid values are "Y", "N", and null. Expected use is in medical device- related trials. It is part of the definition of a serious AE as represented in 21 CFR Part 803.3(w)(3). Records whether medical or surgical intervention was necessary to preclude permanent impairment of a body function, or prevent permanent damage to a body structure, with either situation suspected to be due to the use of a medical product.
- **--UNANT**: *Notes:* The assessment is about a device identified in the data (i.e., which has an SPDEVID). The device may be ancillary or under study. Any serious adverse effect on health or safety or any life-threatening problem or death caused by or associated with a device, if that effect, problem, or death was not previously identified in nature, severity, or degree of incidence in the investigational plan or application (including a supplementary plan or application), or any other unanticipated serious problem associated with a device that relates to the rights, safety, or welfare of subjects. (21 CFR 812.3(s)).
- **--RLPRT**: *Notes:* The investigator's opinion as to the likelihood that the device-related study procedure caused the AE (e.g., implant/insertion, revision/adjustment, explant/removal) | *Examples:* "CAUSAL", "UNLIKELY"
- **--RLPRC**: *Notes:* The investigator's opinion as to the causality of the event as related to other protocol-required activities, actions or assessments (e.g., medication changes, tests/assessments, other procedures). The relationship is to a protocol- specified non-device-related activity where the device is identified in the data (i.e., which has an SPDEVID). The device may be ancillary or under study. | *Examples:* "CAUSAL", "UNLIKELY"
- **--CONTRT**: An indication as to whether a non-study treatment was given because of the occurrence of the event. | *Notes:* Valid values are "Y", "N", and null.
- **--TOX**: The standardized or dictionary-derived name for an untoward event or finding. | *Notes:* Sponsor should specify which scale and version is used in the Sponsor Comments column of the Define- XML document. | *Examples:* An NCI CTCAE Short Name, "HYPERCALCEMIA", "HYPOCALCEMIA"
- **--TOXGR**: A categorical classification of the severity of an event or finding, based on a standard scale, used in study data tabulation. | *Notes:* Sponsor should specify which scale and version is used in the Sponsor Comments column of the Define- XML document. | *Examples:* A toxicity grade from the NCI CTCAE.
- **--USCHFL**: An indication that the performed test or observation was done at a time that was not planned. | *Notes:* If a test or observation was performed based upon a schedule defined in the protocol, this flag should be null. Expected values are "Y" or null. This variable would not be needed when information on planned assessments is provided, such as when the Trial Visits (TV) and Subject Visits (SV) domains are used.

### 3.1.3 The Findings Observation Class


**Findings—Topic and Qualifier Variables—One Record per Finding**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | --TESTCD | Short Name of Measurement, Test, or Exam | Char | Topic |  |  | C82503 |
| 2 | --TEST | Name of Measurement, Test, or Exam | Char | Synonym Qualifier | --TESTCD |  | C82541 |
| 3 | --SBMRKS | Sublineage Marker String | Char | Variable Qualifier | --TESTCD | CP domain only |  |
| 4 | --CELSTA | Cell State | Char | Variable Qualifier | --TESTCD | CP domain only |  |
| 5 | --CSMRKS | Cell State Marker String | Char | Variable Qualifier | --TESTCD | CP domain only |  |
| 6 | --CNTMOD | Contact Mode | Char | Record Qualifier |  |  |  |
| 7 | --EPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier |  |  |  |
| 8 | --TSTCND | Test Condition | Char | Variable Qualifier | --TESTCD | CP, IS, and LB domains only |  |
| 9 | --CNDAGT | Test Condition Agent | Char | Record Qualifier |  | CP, IS, and LB domains only |  |
| 10 | --BDAGNT | Binding Agent | Char | Variable Qualifier | --TESTCD | CP, IS, and LB domains only |  |
| 11 | --ABCLID | Antibody Clone Identifier | Char | Record Qualifier |  | CP domain only |  |
| 12 | --MRKSTR | Marker String | Char | Record Qualifier |  | CP domain only |  |
| 13 | --GATE | Gate | Char | Record Qualifier |  | CP domain only |  |
| 14 | --GATDEF | Gate Definition | Char | Record Qualifier |  | CP domain only |  |
| 15 | --TSTOPO | Test Operational Objective | Char | Variable Qualifier | --TESTCD |  |  |
| 16 | --MSCBCE | Molecule Secreted by Cells | Char | Variable Qualifier | --TESTCD | IS domain only |  |
| 17 | --AGENT | Agent Name | Char | Record Qualifier |  | MS Domain only |  |
| 18 | --CONC | Agent Concentration | Num | Variable Qualifier | --AGENT | MS Domain only |  |
| 19 | --CONCU | Agent Concentration Units | Char | Variable Qualifier | --CONC | MS Domain only |  |
| 20 | --MODIFY | Modified Result Term | Char | Synonym Qualifier | --ORRES |  | C170998 |
| 21 | --TSTDTL | Measurement, Test, or Examination Detail | Char | Variable Qualifier | --TESTCD |  |  |
| 22 | --SPTSTD | Sponsor Test Description | Char | Record Qualifier |  | CP domain only |  |
| 23 | --CAT | Category | Char | Grouping Qualifier |  |  | C25372 |
| 24 | --SCAT | Subcategory | Char | Grouping Qualifier |  |  |  |
| 25 | --TSTPNL | Test Panel | Char | Grouping Qualifier |  | CP domain only |  |
| 26 | --POS | Position of Subject During Observation | Char | Record Qualifier |  |  | C171002 |
| 27 | --BODSYS | Body System or Organ Class | Char | Record Qualifier |  |  | C170986 |
| 28 | --ORRES | Result or Finding in Original Units | Char | Result Qualifier |  |  | C117221 |
| 29 | --ORRESU | Original Units | Char | Variable Qualifier | --ORRES; --ORNRLO; --ORNRHI; --ORREF |  | C82586 |
| 30 | --RESSCL | Result Scale | Char | Record Qualifier |  |  |  |
| 31 | --RESTYP | Result Type | Char | Record Qualifier |  |  |  |
| 32 | --COLSRT | Collected Summary Result Type | Char | Variable Qualifier | --TESTCD |  |  |
| 33 | --ORNRLO | Normal Range Lower Limit- Original Units | Char | Variable Qualifier | --ORRES |  | C82580 |
| 34 | --ORNRHI | Normal Range Upper Limit- Original Units | Char | Variable Qualifier | --ORRES |  | C70933 |
| 35 | --ORREF | Reference Result in Original Units | Char | Variable Qualifier | --ORRES |  |  |
| 36 | --LLOD | Lower Limit of Detection | Char | Variable Qualifier | --TESTCD |  |  |
| 37 | --STRESC | Result or Finding in Standard Format | Char | Result Qualifier |  |  | C117222 |
| 38 | --IMPLBL | Implantation Site Label | Char | Record Qualifier |  | Not in human clinical trials; IC Domain only |  |
| 39 | --STRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier |  |  | C171009 |
| 40 | --STRESU | Standard Units | Char | Variable Qualifier | --STRESC; --STRESN; --STNRLO; --STNRHI; --STREFC; --STREFN; --LLOQ; --ULOQ |  | C82587 |
| 41 | --STNRLO | Normal Range Lower Limit- Standard Units | Num | Variable Qualifier | --STRESC; --STRESN |  | C171008 |
| 42 | --STNRHI | Normal Range Upper Limit- Standard Units | Num | Variable Qualifier | --STRESC; --STRESN |  | C171007 |
| 43 | --STNRC | Normal Range for Character Results | Char | Variable Qualifier | --STRESC |  | C171006 |
| 44 | --STREFC | Reference Result in Standard Format | Char | Variable Qualifier | --STRESC |  |  |
| 45 | --STREFN | Numeric Reference Result in Std Units | Num | Variable Qualifier | --STRESN |  |  |
| 46 | --NRIND | Normal/Reference Range Indicator | Char | Variable Qualifier | --ORRES; --STRESC; --STRESN |  | C170999 |
| 47 | --RESCAT | Result Category | Char | Variable Qualifier | --ORRES; --STRESC; --STRESN |  | C82498 |
| 48 | --INHERT | Inheritability | Char | Variable Qualifier | --ORRES; --STRESC; --STRESN | GF domain only |  |
| 49 | --GENREF | Genome Reference | Char | Variable Qualifier | --METHOD | GF domain only |  |
| 50 | --CHROM | Chromosome Identifier | Char | Variable Qualifier | --ORRES; --STRESC; --STRESN | GF domain only |  |
| 51 | --SYM | Genomic Symbol | Char | Variable Qualifier | --ORRES; --STRESC; --STRESN | GF domain only |  |
| 52 | --SYMTYP | Genomic Symbol Type | Char | Variable Qualifier | --SYM | GF domain only |  |
| 53 | --GENLOC | Genetic Location | Char | Variable Qualifier | --ORRES; --STRESC; --STRESN | GF domain only |  |
| 54 | --GENSR | Genetic Sub- Region | Char | Variable Qualifier | --ORRES; --STRESC; --STRESN | GF domain only |  |
| 55 | --SEQID | Sequence Identifier | Char | Variable Qualifier | --ORRES; --STRESC; --STRESN | GF domain only |  |
| 56 | --PVRID | Published Variant Identifier | Char | Variable Qualifier | --ORRES; --STRESC; --STRESN | GF domain only |  |
| 57 | --COPYID | Copy Identifier | Char | Variable Qualifier | --ORRES; --STRESC; --STRESN | GF domain only |  |
| 58 | --CHRON | Chronicity of Finding | Char | Variable Qualifier | --STRESC |  |  |
| 59 | --DISTR | Distribution Pattern of Finding | Char | Variable Qualifier | --STRESC |  |  |
| 60 | --RESLOC | Result Location of Finding | Char | Record Qualifier |  | Not in human clinical trials | C170500 |
| 61 | --STAT | Completion Status | Char | Record Qualifier |  |  |  |
| 62 | --REASND | Reason Not Done | Char | Record Qualifier |  |  | C82556 |
| 63 | --XFN | External File Path | Char | Record Qualifier |  |  | C82536 |
| 64 | --NAM | Laboratory/Vendor Name | Char | Record Qualifier |  |  | C117200 |
| 65 | --LOINC | LOINC Code | Char | Record Qualifier |  |  | C82502 |
| 66 | --SPEC | Specimen Material Type | Char | Record Qualifier |  |  | C70713 |
| 67 | --ANTREG | Anatomical Region | Char | Variable Qualifier | --SPEC |  | C170983 |
| 68 | --SPCCND | Specimen Condition | Char | Record Qualifier |  |  | C70714 |
| 69 | --SPCUFL | Specimen Usability for the Test | Char | Record Qualifier |  |  | C171004 |
| 70 | --LOC | Location Used for the Measurement | Char | Record Qualifier |  |  |  |
| 71 | --LAT | Laterality | Char | Variable Qualifier | --LOC; --SPEC |  |  |
| 72 | --DIR | Directionality | Char | Variable Qualifier | --LOC; --SPEC |  |  |
| 73 | --PORTOT | Portion or Totality | Char | Variable Qualifier | --LOC; --SPEC |  |  |
| 74 | --METHOD | Method of Test or Examination | Char | Record Qualifier |  |  |  |
| 75 | --RUNID | Run ID | Char | Record Qualifier |  |  | C117058 |
| 76 | --ANMETH | Analysis Method | Char | Record Qualifier |  |  |  |
| 77 | --TMTHSN | Test Method Sensitivity | Char | Record Qualifier |  |  |  |
| 78 | --LEAD | Lead Identified to Collect Measurements | Char | Record Qualifier |  |  | C170997 |
| 79 | --CSTATE | Consciousness State | Char | Record Qualifier |  |  | C88429 |
| 80 | --LOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier |  |  |  |
| 81 | --BLFL | Baseline Flag | Char | Record Qualifier |  |  | C82526 |
| 82 | --FAST | Fasting Status | Char | Record Qualifier |  |  | C93566 |
| 83 | --DRVFL | Derived Flag | Char | Record Qualifier |  |  | C81197 |
| 84 | --EVAL | Evaluator | Char | Record Qualifier |  | Not in QS, FT, and clinical classifications use case of RS | C51824 |
| 85 | --EVALID | Evaluator Identifier | Char | Variable Qualifier | --EVAL | Not in QS, FT, and clinical classifications use case of RS | C117043 |
| 86 | --ACPTFL | Accepted Record Flag | Char | Record Qualifier |  |  | C117038 |
| 87 | --TOX | Toxicity | Char | Variable Qualifier | --TOXGR |  | C27990 |
| 88 | --TOXGR | Toxicity Grade | Char | Record Qualifier |  |  | C82528 |
| 89 | --SEV | Severity/Intensity | Char | Record Qualifier |  |  | C25676 |
| 90 | --CLSIG | Clinically Significant, Collected | Char | Record Qualifier |  |  | C93532 |
| 91 | --DTHREL | Relationship to Death | Char | Record Qualifier |  | Not in human clinical trials | C82563 |
| 92 | --LLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | --STRESC; --STRESN |  | C82589 |
| 93 | --ULOQ | Upper Limit of Quantitation | Num | Variable Qualifier | --STRESC; --STRESN |  | C85533 |
| 94 | --REASPF | Reason Test Performed | Char | Record Qualifier |  |  | C171003 |
| 95 | --EXCLFL | Exclude from Statistics | Char | Record Qualifier |  | Not in human clinical trials | C117045 |
| 96 | --REASEX | Reason for Exclusion from Statistics | Char | Record Qualifier |  | Not in human clinical trials | C117057 |
| 97 | --USCHFL | Unscheduled Flag | Char | Record Qualifier |  | Not in human clinical trials | C170510 |
| 98 | --REPNUM | Repetition Number | Num | Record Qualifier |  |  |  |
| 99 | --RSTIND | Restraint Indicator | Char | Record Qualifier |  | Not in human clinical trials |  |
| 100 | --RSTMOD | Restraint Mode | Char | Record Qualifier |  | Not in human clinical trials |  |
| 1 | --OBJ | Object of the Observation | Char | Record Qualifier |  |  |  |

**Variable Definitions:**

- **--TESTCD**: The standardized or dictionary- derived short sequence of characters used to | *Notes:* Used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. | *Examples:* "PLAT", "SYSBP", "RRMIN", "EYEEXAM"
- **--TEST**: The standardized or dictionary- derived name of the measurement, test, or examination. | *Examples:* "Platelets", "Systolic Blood Pressure", "Summary (Min) RR Duration", "Eye Examination"
- **--SBMRKS**: *Notes:* Used to further subset the cell population identified in CPTEST based on the use of additional marker(s) that define a sublineage. The value in CPSBMRKS is used in combination with values in CPTEST and CPCELSTA to fully describe the cell population being measured. As such, it is an essential component of the full test name. | *Examples:* Three unnamed sublineages of monocytes have been identified: CCR2+CD16-; CCR2-CD16+; and CCR2+CD16+. Whereas the entire monocyte cell population can be defined as CD14+ cells, the additional CCR2 and CD16 markers are used to differentiate one sublineage from another, none of which has yet been given a name by the scientific community. By combining the CPTEST value of "Monocyte Subset" with the value of "CCR2+CD16-" in CPSBMRKS, the full test is defined to be the CCR2+CD16- monocyte subpopulation.
- **--CELSTA**: *Notes:* A textual description of a subset of the cell population identified in CPTEST based on a particular functional and/or biological state (e.g., primed, activated, proliferating, senescent, G2-arrested). When populated, the values in CPCELSTA and CPSMRKS, in combination with values in CPTEST and CPSBMRKS, fully describe the cell population being measured.
- **--CSMRKS**: *Notes:* Identifies the marker(s) or indicator(s) used to define the cell state (i.e., the value in CPCELSTA). | *Examples:* When Ki67 expression is used to determine that a cell population is in a proliferating state (i.e., CPCELSTA value = "PROLIFERATING"), the value "Ki67+" in CPCSMRKS indicates that positive expression of Ki67 was used to define the population as proliferating. Similarly, a value of "Ki67-" in CPCSMRKS would indicate that lack of expression of Ki67 defined the "NON- PROLIFERATING" cell state in CPCELSTA. The CPCSMRKS value is useful for quickly determining which marker(s) were used to classify (i.e., operationally
- **--CNTMOD**: *Notes:* The way in which the measurement, test, or examination was conducted.
- **--EPCHGI**: *Notes:* Indicates whether the measurement, test, or examination was changed due to an epidemic or pandemic.
- **--TSTCND**: *Notes:* Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed. | *Examples:* Stimulating or activating agents, assay temperature, incubation time "STIMULATED", "NON- STIMULATED", "25 C", "37 C".
- **--CNDAGT**: *Notes:* The textual description of the agent used to impose a test condition identified in CPTSTCND. For example, records might be produced for the same test run under stimulating (CPTSTCND value = "STIMULATED") conditions produced by different stimulating agents. | *Examples:* "Phorbol myristate acetate", "Concanavalin A, PHA-P", "TNF- alpha, Ionomycin", "Candida antigen"
- **--BDAGNT**: *Notes:* The textual description of the agent that's binding to the entity in the --TEST variable. The --BDAGNT variable is used to indicate that there is a binding relationship between the entities in the --TEST and --BDAGNT variables, regardless of direction. --BDAGNT is not a method qualifier. It should only be used when the actual interest of the measurement is the binding interaction between the two entities in --TEST and --BDAGNT. In other words, the combination of --TEST and --BDAGNT should describe the thing, the entity, or the analyte being measured, without the need for additional variables. The binding agent may be, but is not limited to, a test article, a portion of the test article, a related compound, an endogenous molecule, an allergen, or an infectious agent.
- **--ABCLID**: *Notes:* Identifies the antibody clone (e.g., supplier-provided catalog name) used to confer specificity for the binding agent specified in CPBDAGNT.
- **--MRKSTR**: *Notes:* The text string identifying the full set of markers/indicators used by the laboratory to operationally define the complete test. Because laboratories often use different markers/indicators to identify a cell population, the relationship between a named cell population in CPTEST (as combined with CPSBMRKS and CPCELSTA values) and the set of markers used to
- **--GATE**: *Notes:* The sponsor-defined name assigned to a gate. Gates are electronic (device setting or software-defined) boundaries set by a user to virtually parse a specimen into discrete populations based on a set of defined characteristics (e.g., presence, absence, or intensity of expression of various markers; physical size; internal complexity or granularity). Gates are used to constrain data collection or analysis to a specific cell population or region of interest within the specimen.
- **--GATDEF**: *Notes:* The text string identifying the set of parameters and the order in which they are applied to define the gating strategy. In practice, a series of 2- dimensional subgates based on 2 different cell characteristics (i.e., markers/indicators/physical properties) are most often combined until the cell population of interest is sufficiently resolved (i.e., electronically isolated) from other cell populations contained within the specimen. For complex analyses, differences in gating strategies can produce subtle differences in results obtained for a test. To ensure nuances important for accurately interpreting the data are accounted for and which arise from the use of different gating strategies, it is often necessary to qualify the test in terms of the gating strategy. For some purposes, however, and at the discretion of the sponsor, only the ultimate or penultimate gate is identified. When specifying the gating strategy in CPGATDEF, each subgate should be listed in the order it was applied and separated from the next sub-gate using the vertical line or pipe character ("|").
- **--TSTOPO**: *Notes:* The textual description of the high- level purpose of the test at the operational level. | *Examples:* "SCREEN", "CONFIRM", "QUANTIFY"
- **--MSCBCE**: *Notes:* The textual description of the entity secreted by the cells represented in --TEST. The combination of --TEST and --MSBCE should describe the thing, the entity, or the analyte being measured, without the need for additional variables.
- **--AGENT**: *Notes:* The name of the drug or other material for which resistance is tested. The agent may be used for in vitro testing or may be used in tests for genetic markers or in direct phenotypic drug-sensitivity testing.
- **--CONC**: *Notes:* The amount of drug or other material listed in MSAGENT per unit volume or weight. Used when the agent is part of the prespecified test. Not to be used when the concentration is a result of a test such as minimal inhibitory concentration, IC50, or EC50.
- **--CONCU**: *Notes:* Unit of measure for MSCONC.
- **--MODIFY**: A value which represents an alteration to a collected value for coding purposes.
- **--TSTDTL**: *Notes:* Further description of --TESTCD and --TEST. | *Examples:* "STAINING INTENSITY" when MITEST="Human Epidermal Growth Factor Receptor 2"
- **--SPTSTD**: *Notes:* Sponsor's description of a test. This variable is particularly valuable for identifying the cell population on which certain tests are conducted when it is not identified in the Test Name (CPTEST; e.g., tests for quantitative expression of a particular marker).
- **--CAT**: A grouping or classification of the topic of the finding, event, or intervention. | *Examples:* "HEMATOLOGY", "URINALYSIS", "CHEMISTRY", "HAMD 17", "SF36 V2.0 ACUTE", "EGFR MUTATION ANALYSIS"
- **--SCAT**: A further grouping or classification of the category for the topic of the finding, event, or intervention. | *Notes:* The category is in --CAT. | *Examples:* "WBC DIFFERENTIAL"
- **--TSTPNL**: *Notes:* Sponsor-defined textual description used to group tests run together as
- **--POS**: The particular way that a subject's body is placed or situated during an assessment. | *Examples:* "SUPINE", "STANDING", "SITTING"
- **--BODSYS**: A standardized or dictionary-derived name for the body system or organ class. | *Examples:* MedDRA SOC
- **--ORRES**: The result of the measurement, test, or examination, as originally received or collected. | *Examples:* "120", "<1", "POS"
- **--ORRESU**: The unit of measure for the result (as originally received or collected) of the measurement, test, or examination. | *Notes:* Unit for --ORRES and --ORREF. | *Examples:* "in", "LB", "kg/L"
- **--RESSCL**: *Notes:* Classifies the scale of the original result value with respect to whether the result is, for example, ordinal, nominal, quantitative, or narrative. | *Examples:* "NARRATIVE", "NOMINAL", "ORDINAL", "QUANTITATIVE"
- **--RESTYP**: *Notes:* Classifies the kind of result (i.e., property type) originally reported for the test. | *Examples:* "SUBSTANCE CONCENTRATION", "MASS RATE", "ARBITRARY CONCENTRATION"
- **--COLSRT**: *Notes:* Used to indicate the type of a collected summary result. This is used for summary results collected on a CRF or provided by an external vendor (e.g., central lab). If the summary result is derived by the sponsor using individual source data records, the summary result is represented in ADaM. If a sponsor has both a collected or vendor- provided summary result and a derived summary result, the collected or vendor-provided summary result is represented in SDTM and the derived summary result is represented in ADaM. | *Examples:* "MAXIMUM", "MINIMUM", "MEAN", "MEDIAN", "NADIR"
- **--ORNRLO**: The lowest value in a normal or reference range
- **--ORNRHI**: The highest value in a normal or reference range for the result (as originally received or collected) of the measurement, test, or examination.
- **--ORREF**: *Notes:* Reference value for the result or finding as originally received or collected. --ORREF uses the same units as --ORRES, if applicable. | *Examples:* Value from predicted normal value in spirometry tests.
- **--LLOD**: *Notes:* The lowest threshold (as originally received or collected) for reliably detecting the presence or absence of substance measured by a specific test. The value for the field will be as described in documentation from the instrument or lab vendor.
- **--STRESC**: The standardized result of the measurement, test, or examination, in character format. | *Notes:* --STRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in --STRESN. | *Examples:* If various tests have results "NONE", "NEG", and "NEGATIVE" in --ORRES and these results effectively have the same meaning, they could be represented in standard format in --STRESC as "NEGATIVE".
- **--IMPLBL**: *Notes:* Label or identifier that describes the location or position of a fetal implantation site in the uterus (or uterine horn) when classifying implantations during a uterine examination in a reproductive toxicology study.
- **--STRESN**: The standardized result of the measurement, test, or examination in numeric format. | *Notes:* Copied in numeric format from --STRESC. --STRESN should store all numeric test results or findings.
- **--STRESU**: The unit of measure for the standardized result of the measurement, test, or examination. | *Examples:* "mol/L"
- **--STNRLO**: The lowest value in a normal or reference range for the standardized result of the measurement, test, or examination.
- **--STNRHI**: The highest value in a normal or reference range for the standardized result of the measurement, test, or examination.
- **--STNRC**: A set of normal or reference values for the standardized character result, in an ordinal scale or categorical grouping. | *Examples:* "Negative to Trace"
- **--STREFC**: *Notes:* Reference value for the result or finding copied or derived from --ORREF in a standard format.
- **--STREFN**: *Notes:* Reference value for continuous or numeric results or findings in standard format or in standard units. --STREFN uses the same units as --STRESN, if applicable.
- **--NRIND**: A classification of the original or standardized result as it relates to a normal or reference result range. | *Notes:* May be defined by --ORNRLO and --ORNRHI or other objective criteria. | *Examples:* "Y", "N"; "HIGH", "LOW"; "NORMAL", "ABNORMAL"
- **--RESCAT**: A grouping or classification of the results of an assessment. | *Notes:* The result is in --STRESC. | *Examples:* "MALIGNANT" or "BENIGN" for tumor findings
- **--INHERT**: *Notes:* Identifies whether the variation can be passed to the next generation.
- **--GENREF**: *Notes:* An identifier for the genome reference used to generate the reported result. | *Examples:* For example, Genome Reference Consortium Human Build 38 patch release 13 may be represented as GRCh38.p13.
- **--CHROM**: *Notes:* The designation (name or number) of the chromosome or contig on which the variant or other feature appears. | *Examples:* "17", "X"
- **--SYM**: *Notes:* A published symbol for the portion of the genome serving as a locus for the experiment/test.
- **--SYMTYP**: *Notes:* A description of the type of genomic entity that is represented by the published symbol in --SYM.
- **--GENLOC**: *Notes:* Specifies the location within a sequence for the observed value in --ORRES.
- **--GENSR**: *Notes:* The portion of the locus in which the variation was found. | *Examples:* "Exon 15", "Kinase domain"
- **--SEQID**: *Notes:* A unique identifier for the sequence used as the reference to identify the genetic variation in the result. | *Examples:* "NM 001234", _ "ENSG00000182533", "ENST00000343849.2"
- **--PVRID**: *Notes:* A unique identifier for the variation that has been publicly characterized in an external database. | *Examples:* "rs2231142", "COSM41596"
- **--COPYID**: *Notes:* An arbitrary identifier used to differentiate between copies of a genetic target of interest present on homologous chromosomes.
- **--CHRON**: *Notes:* Characterization of the duration of a biological process resulting in a particular finding. | *Examples:* "ACUTE", "CHRONIC", "SUBACUTE"
- **--DISTR**: *Notes:* Description of the distribution pattern of a finding within the examined area. | *Examples:* "FOCAL", "MULTIFOCAL", "DIFFUSE"
- **--RESLOC**: Anatomical location where the result was observed. | *Notes:* Location where the result was observed (as opposed to the location specified for examination). This location may have a higher degree of specificity than the location specified for examination. | *Examples:* "PINNA" when --LOC is "EAR" "LUNG, LEFT LOWER LOBE" where --LOC is "CHEST" "CORTEX" when --SPEC is "KIDNEY"
- **--STAT**: *Notes:* Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".
- **--REASND**: The explanation for why requested information was not available. | *Notes:* Used in conjunction with --STAT when value is "NOT DONE".
- **--XFN**: The filename and/or path to external data not stored in the same format and possibly not the same location as the other data for a study. | *Examples:* A filename and/or path for an ECG waveform or a medical image.
- **--NAM**: The name of the vendor performing an assessment. | *Examples:* A laboratory name.
- **--LOINC**: A short sequence of characters used to represent laboratory and clinical tests within the Logical Observation Identifiers Names and Codes (LOINC) database.
- **--SPEC**: The type of sample material taken from a biological entity. | *Examples:* "SERUM", "PLASMA", "URINE", "DNA", "RNA"
- **--ANTREG**: The specific anatomical or biological region of a tissue or organ specimen. | *Notes:* As defined in the protocol. | *Examples:* A section or part of what is described in the --SPEC variable "CORTEX", "MEDULLA", "MUCOSA"
- **--SPCCND**: The physical state or quality of a sample for assessment. | *Examples:* "CLOUDY"
- **--SPCUFL**: An indication as to whether a sample is suitable for testing. | *Notes:* The value will be "N" if the specimen is not usable, and null if the specimen is usable.
- **--LOC**: *Notes:* Anatomical location of the subject relevant to the collection of the measurement. | *Examples:* "RECTUM" for temperature, "ARM" for blood pressure
- **--LAT**: *Notes:* Qualifier for anatomical location or specimen further detailing laterality. | *Examples:* "RIGHT", "LEFT", "BILATERAL"
- **--DIR**: *Notes:* Qualifier for anatomical location or specimen further detailing directionality. | *Examples:* "ANTERIOR", "LOWER", "PROXIMAL"
- **--PORTOT**: *Notes:* Qualifier for anatomical location or specimen further detailing the distribution (i.e., arrangement or apportioning of). | *Examples:* "ENTIRE", "SINGLE", "SEGMENT", "MANY"
- **--METHOD**: *Notes:* Method of the test or examination. | *Examples:* "EIA" (enzyme immunoassay), "ELECTROPHORESIS", "DIPSTICK"
- **--RUNID**: A sequence of characters used to uniquely identify a particular run of a test on a particular batch of samples.
- **--ANMETH**: *Notes:* Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result (e.g., an image, a genetic sequence).
- **--TMTHSN**: *Notes:* The sensitivity of the test methodology with respect to observation, detection, or quantification. | *Examples:* "LOW SENSITIVITY", "HIGH SENSITIVITY", "ULTRA-HIGH SENSITIVITY"
- **--LEAD**: An electrical recording from some region of the body that represents the voltage difference between 2 electrodes. | *Examples:* "LEAD I", "LEAD V2", "LEAD CM5"
- **--CSTATE**: The subject's level of consciousness. | *Examples:* "CONSCIOUS", "SEMI- CONSCIOUS", "UNCONSCIOUS"
- **--LOBXFL**: *Notes:* Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Result value is in --STRESC. Should be "Y" or null.
- **--BLFL**: An indication that the record is the sponsor-defined baseline assessment, used in study data tabulation. | *Notes:* Result value is in --STRESC. Should be "Y" or null.
- **--FAST**: An indication as to whether a subject has abstained from food and liquid for a prescribed amount of time. | *Notes:* Valid values include "Y", "N", "U", or null if not relevant.
- **--DRVFL**: An indication that the measurement or finding is not a collected value but is processed or computed by the sponsor from collected data. | *Notes:* Should be "Y" or null. | *Examples:* The average of other records used as a computed baseline.
- **--EVAL**: The role of the person(s) providing an evaluation, appraisal, or interpretation. | *Notes:* Used only for results that are subjective (e.g., assigned by a person or a group). | *Examples:* "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR"
- **--EVALID**: A sequence of characters used to uniquely identify the evaluator(s). | *Notes:* Used to distinguish multiple evaluators with the same role recorded in --EVAL. | *Examples:* "RADIOLOGIST1", "RADIOLOGIST2"
- **--ACPTFL**: An indication that a record is the endorsed assessment. | *Notes:* Expected values can include "Y", "N", or null. This is not intended to be an analysis flag to indicate acceptability for a given analysis.
- **--TOX**: The standardized or dictionary- derived name for an untoward event or finding. | *Notes:* Sponsors should specify which scale and version is used in the Sponsor Comments column of the Define-XML document. | *Examples:* An NCI CTCAE Short Name. "HYPERCALCEMIA", "HYPOCALCEMIA"
- **--TOXGR**: A categorical classification of the severity of an event or finding, based on a standard scale, used in study data tabulation. | *Notes:* Sponsors should specify which scale and version is used in the Sponsor Comments column of the Define-XML document. | *Examples:* A grade from the NCI CTCAE. "2"
- **--SEV**: The quality or degree of harm associated with a finding or event, as collected. | *Examples:* "MILD", "MODERATE", "SEVERE"
- **--CLSIG**: An indication as to whether an observation is clinically significant based on judgment. | *Notes:* For collected assessments of clinical significance of a result. | *Examples:* "Y", "N"
- **--DTHREL**: An indication that a particular finding is related to the cause of death. | *Examples:* "Y", "N", or "U"
- **--LLOQ**: The lowest threshold for reliably quantifying the amount of substance measured by a specific test, in standardized units. | *Notes:* Units will be those used for --STRESU.
- **--ULOQ**: The highest threshold for reliably detecting the result of a specific test in standardized units. | *Notes:* Units will be those used for --STRESU.
- **--REASPF**: The explanation for why a test, measurement, or assessment is executed.
- **--EXCLFL**: An indication that the result is to be excluded from all calculations. | *Notes:* Expected to be "Y" or null. --EXCLFL should be null when --STAT is "NOT DONE".
- **--REASEX**: The explanation for why a result is excluded from all calculations. | *Notes:* Used in conjunction with --EXCLFL when its value is "Y".
- **--USCHFL**: An indication that the performed test or observation was done at a time that was not planned. | *Notes:* If a test or observation was performed based upon a schedule defined in the protocol, this flag should be null. Expected values are "Y" or null. This variable would not be needed when information on planned assessments is provided, such as when the Trial Visits (TV) and Subject Visits (SV) domains are used.
- **--REPNUM**: *Notes:* The instance number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point or within a visit). | *Examples:* Multiple measurements of blood pressure or multiple analyses of a sample.
- **--RSTIND**: *Notes:* An indicator as to whether the animal was restrained during the observation period. Expected values are "Y" or null.
- **--RSTMOD**: *Notes:* A description of whether the restraint was physical and/or chemical.
- **--OBJ**: *Notes:* Used in domains modeled as Findings About Events or Findings About Interventions. Describes the event or intervention whose property is being measured in --TESTCD/--TEST. | *Examples:* An event of vomiting which has findings, where --OBJ="VOMIT" and the volume of VOMIT is being measured where --TESTCD="VOLUME".

#### 3.1.3.1 Findings About Events or Interventions

Findings About is a specialization of the Findings class that utilizes Findings general observation class variables with the addition of the --OBJ variable.


### 3.1.4 Identifiers for All Classes

STUDYID, DOMAIN, and --SEQ are required in all domains based on one of the 3 general observation classes. Each general class domain must also include at least 1 of the following subject identifiers: USUBJID, SPDEVID, or POOLID.


**All Observation Classes—Identifiers**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 4 | POOLID | Pool Identifier | Char | Identifier |  |  | C117053 |
| 5 | SPDEVID | Sponsor Device Identifier | Char | Identifier |  |  | C117060 |
| 6 | NHOID | Non-Host Organism Identifier | Char | Identifier |  |  |  |
| 7 | FETUSID | Fetus Identifier | Char | Identifier |  | Not in human clinical trials | C170497 |
| 8 | FOCID | Focus of Study- Specific Interest | Char | Identifier |  |  |  |
| 9 | --SEQ | Sequence Number | Num | Identifier |  |  | C70710 |
| 10 | --GRPID | Group ID | Char | Identifier |  |  | C170996 |
| 11 | --REFID | Reference ID | Char | Identifier |  |  | C82531 |
| 12 | --RECID | Invariant Record Identifier | Char | Identifier |  |  |  |
| 13 | --SPID | Sponsor- Defined Identifier | Char | Identifier |  |  | C82530 |
| 14 | --LNKID | Link ID | Char | Identifier |  |  | C117050 |
| 15 | --LNKGRP | Link Group ID | Char | Identifier |  |  | C117049 |
| 16 | --BEATNO | ECG Beat Number | Num | Identifier |  | EG Domain only |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation. The domain abbreviation is also used as a prefix for variables to ensure uniqueness when datasets are merged.
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **POOLID**: A sequence of characters used to uniquely identify a group of subjects that have been pooled together. | *Notes:* Used for results that are not assignable to a specific subject.
- **SPDEVID**: A sequence of characters used by the sponsor to uniquely identify a specific device.
- **NHOID**: *Notes:* Sponsor-defined identifier for a non- host organism. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by the lab. | *Examples:* "A/California/7/2009 (H1N1)"
- **FETUSID**: A sequence of characters used to uniquely identify a fetus associated with a maternal subject, for a particular prenatal evaluation.
- **FOCID**: *Notes:* Identification of a focus of study- specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed. The value in this variable should have inherent semantic meaning. | *Examples:* A drug application site (e.g., "Injection site 1", "Biopsy site 1", "Treated site 1"), or a more specific focus (e.g., "OD" (right eye), "Upper left quadrant of the back")
- **--SEQ**: A number used in combination with the identifier of the subject of the observation to uniquely identify a record within a domain. | *Notes:* May be any valid number (including decimals) and does not have to start at 1. Datasets that do not contain subject data, such as the Trial Summary (TS) domain and the Device Tracking (DT) domains, use --SEQ as a sequence
- **--GRPID**: A sequence of characters used to uniquely identify related records for a subject within a domain, or related parameters in the Trial Summary (TS) dataset. | *Notes:* See also Section 5.1.6, Trial Summary Information and Section 5.1.7, Challenge Agent Characterization.
- **--REFID**: A sequence of characters used to uniquely identify a source of information. | *Examples:* A lab specimen ID, the UUID for an ECG waveform or a medical image.
- **--RECID**: *Notes:* Identifier for a record that is unique within a domain for a study and that remains invariant through subsequent versions of the dataset, even if the content of the record is modified. When a record is deleted, this value must not be reused to identify another record in either the current or future versions of the domain.
- **--SPID**: A sponsor-defined sequence of characters used to identify an instance of an observation. | *Examples:* A preprinted line identifier on a Concomitant Medications form.
- **--LNKID**: A sequence of characters used to uniquely identify a record, for a subject, in one domain and link it to 1 or more records for that subject in another domain. | *Notes:* This may be a one-to-one or a one-to- many relationship. | *Examples:* A value that links a single tumor to multiple measurements/assessments performed at different times.
- **--LNKGRP**: A sequence of characters used to uniquely identify a group of records, for a subject, in one domain and link it to 1 or more records for that subject in another domain. | *Notes:* This will usually be a many-to-one relationship. | *Examples:* A value that links multiple tumor measurement/assessments to a single response to therapy.
- **--BEATNO**: *Notes:* A sequence number that identifies the beat within an ECG.

### 3.1.5 Timing Variables for All Classes

The following timing variables are available for use in any domain based on one of the 3 general observation classes.


**All Observation Classes—Timing Variables**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 10 | --GRPID | Group ID | Char | Identifier |  |  | C170996 |
| 11 | --REFID | Reference ID | Char | Identifier |  |  | C82531 |
| 12 | --RECID | Invariant Record Identifier | Char | Identifier |  |  |  |
| 13 | --SPID | Sponsor- Defined Identifier | Char | Identifier |  |  | C82530 |
| 14 | --LNKID | Link ID | Char | Identifier |  |  | C117050 |
| 15 | --LNKGRP | Link Group ID | Char | Identifier |  |  | C117049 |
| 16 | --BEATNO | ECG Beat Number | Num | Identifier |  | EG Domain only |  |
| 1 | VISITNUM | Visit Number | Num | Timing |  |  | C83101 |
| 2 | VISIT | Visit Name | Char | Timing |  |  | C171010 |
| 3 | VISITDY | Planned Study Day of Visit | Num | Timing |  |  | C171011 |
| 4 | TAETORD | Planned Order of Element Within Arm | Num | Timing |  |  | C83438 |
| 5 | EPOCH | Epoch | Char | Timing |  |  | C71738 |
| 6 | RPHASE | Repro Phase | Char | Timing |  | Not in human clinical trials |  |
| 7 | RPPLDY | Planned Repro Phase Day of Observation | Num | Timing |  | Not in human clinical trials | C170506 |
| 8 | RPPLSTDY | Planned Repro Phase Day of Obs Start | Num | Timing |  | Not in human clinical trials | C170508 |
| 9 | RPPLENDY | Planned Repro Phase Day of Obs End | Num | Timing |  | Not in human clinical trials | C170507 |
| 10 | --DTC | Date/Time of Collection | Char | Timing |  |  | C82515 |
| 11 | --STDTC | Start Date/Time of Observation | Char | Timing |  | Not in Findings class domains | C82517 |
| 12 | --ENDTC | End Date/Time of Observation | Char | Timing |  |  | C82516 |
| 13 | --DY | Study Day of Visit/Collection/Exam | Num | Timing |  |  | C170993 |
| 14 | --STDY | Study Day of Start of Observation | Num | Timing |  | Not in Findings class domains | C171005 |
| 15 | --ENDY | Study Day of End of Observation | Num | Timing |  |  | C170995 |
| 16 | --NOMDY | Nominal Study Day for Tabulations | Num | Timing |  | Not in human clinical trials | C170498 |
| 17 | --NOMLBL | Label for Nominal Study Day | Char | Timing |  | Not in human clinical trials | C170499 |
| 18 | --RPDY | Actual Repro Phase Day of Observation | Num | Timing |  | Not in human clinical trials | C170504 |
| 19 | --RPSTDY | Actual Repro Phase Day of Obs Start | Num | Timing |  | Not in human clinical trials | C170509 |
| 20 | --RPENDY | Actual Repro Phase Day of Obs End | Num | Timing |  | Not in human clinical trials | C170505 |
| 21 | --XDY | Day of Obs Relative to Exposure | Num | Timing |  |  |  |
| 22 | --XSTDY | Start Day of Obs Relative to Exposure | Num | Timing |  | Not in Findings class domains |  |
| 23 | --XENDY | End Day of Obs Relative to Exposure | Num | Timing |  |  |  |
| 24 | --CHDY | Day of Obs Rel to Challenge Agent | Num | Timing |  |  |  |
| 25 | --CHSTDY | Start Day of Obs Rel to Challenge Agent | Num | Timing |  | Not in Findings class domains |  |
| 26 | --CHENDY | End Day of Obs Rel to Challenge Agent | Num | Timing |  |  |  |
| 27 | --DUR | Collected Duration | Char | Timing |  |  | C170992 |
| 28 | --TPT | Planned Time Point Name | Char | Timing |  |  | C171029 |
| 29 | --TPTNUM | Planned Time Point Number | Num | Timing |  |  | C82545 |
| 30 | --ELTM | Planned Elapsed Time from Time Point Ref | Char | Timing |  |  | C170994 |
| 31 | --TPTREF | Time Point Reference | Char | Timing |  |  | C171030 |
| 32 | --RFTDTC | Date/Time of Reference Time Point | Char | Timing |  |  | C82518 |
| 33 | --STRF | Start Relative to Reference Period | Char | Timing |  |  | C82559 |
| 34 | --ENRF | End Relative to Reference Period | Char | Timing |  |  | C82557 |
| 35 | --EVLINT | Evaluation Interval | Char | Timing |  |  | C82534 |
| 36 | --EVINTX | Evaluation Interval Text | Char | Timing |  |  | C117044 |
| 37 | --STRTPT | Start Relative to Reference Time Point | Char | Timing |  |  | C82560 |
| 38 | --STTPT | Start Reference Time Point | Char | Timing |  |  | C82575 |
| 39 | --ENRTPT | End Relative to Reference Time Point | Char | Timing |  |  | C82558 |
| 40 | --ENTPT | End Reference Time Point | Char | Timing |  |  | C82574 |
| 41 | MIDS | Disease Milestone Instance Name | Char | Timing |  |  |  |
| 42 | RELMIDS | Temporal Relation to Milestone Instance | Char | Timing |  |  |  |
| 43 | MIDSDTC | Disease Milestone Instance Date/Time | Char | Timing |  |  |  |
| 44 | --STINT | Planned Start of Assessment Interval | Char | Timing |  |  | C117061 |
| 45 | --ENINT | Planned End of Assessment Interval | Char | Timing |  |  | C117042 |
| 46 | --DETECT | Time in Days to Detection | Num | Timing |  | Not in human clinical trials | C117041 |
| 47 | --PTFL | Point in Time Flag | Char | Timing |  | Only in Findings class specimen- based domains: BS, CP, GF, IS, LB, MB, MS, MI, PC, PP |  |
| 48 | --PDUR | Planned Duration | Char | Timing |  | Only in Findings class specimen- based domains: BS, CP, GF, IS, LB, MB, MS, MI, PC, PP |  |
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 4 | SUBJID | Subject Identifier for the Study | Char | Topic |  |  |  |
| 5 | RFSTDTC | Subject Reference Start Date/Time | Char | Record Qualifier |  |  | C83395 |
| 6 | RFENDTC | Subject Reference End Date/Time | Char | Record Qualifier |  |  | C83394 |

**Variable Definitions:**

- **--GRPID**: A sequence of characters used to uniquely identify related records for a subject within a domain, or related parameters in the Trial Summary (TS) dataset. | *Notes:* See also Section 5.1.6, Trial Summary Information and Section 5.1.7, Challenge Agent Characterization.
- **--REFID**: A sequence of characters used to uniquely identify a source of information. | *Examples:* A lab specimen ID, the UUID for an ECG waveform or a medical image.
- **--RECID**: *Notes:* Identifier for a record that is unique within a domain for a study and that remains invariant through subsequent versions of the dataset, even if the content of the record is modified. When a record is deleted, this value must not be reused to identify another record in either the current or future versions of the domain.
- **--SPID**: A sponsor-defined sequence of characters used to identify an instance of an observation. | *Examples:* A preprinted line identifier on a Concomitant Medications form.
- **--LNKID**: A sequence of characters used to uniquely identify a record, for a subject, in one domain and link it to 1 or more records for that subject in another domain. | *Notes:* This may be a one-to-one or a one-to- many relationship. | *Examples:* A value that links a single tumor to multiple measurements/assessments performed at different times.
- **--LNKGRP**: A sequence of characters used to uniquely identify a group of records, for a subject, in one domain and link it to 1 or more records for that subject in another domain. | *Notes:* This will usually be a many-to-one relationship. | *Examples:* A value that links multiple tumor measurement/assessments to a single response to therapy.
- **--BEATNO**: *Notes:* A sequence number that identifies the beat within an ECG.
- **VISITNUM**: An assigned numeric identifier that aligns to the chronological order of a clinical encounter. | *Notes:* Numeric version of VISIT, used for sorting. VISITNUM does not have to be an integer value. | *Examples:* 1, 1.1, 503.75
- **VISIT**: The label for a protocol-defined clinical encounter.
- **VISITDY**: The planned study day of a clinical encounter relative to the sponsor-defined reference start date. | *Notes:* Should be an integer.
- **TAETORD**: An assigned numeric identifier that gives the planned order of the element within the trial arm of the study. | *Notes:* See Section 5.1.1.2, Trial Arms.
- **EPOCH**: A time period defined in the protocol with a study-specific purpose. | *Notes:* The epoch associated with an observation is determined by the start date or start date and time of the observation, or the date/time of collection if start date/time is not collected (see Section 5.1.1.2, Trial Arms).
- **RPHASE**: *Notes:* Reproductive phase with which the reproductive stage of the reproductive path is associated. Defined in Trial Paths domain. The RPHASE variable is Required when any Reproductive Phase Day variable is used.
- **RPPLDY**: The day within the reproductive phase on which the test or observation was scheduled to occur. | *Notes:* Expressed as an integer.
- **RPPLSTDY**: The day within the reproductive phase on which the test or observation was scheduled to begin. | *Notes:* Expressed as an integer.
- **RPPLENDY**: The day within the reproductive phase on which the test or observation was scheduled to end. | *Notes:* Expressed as an integer.
- **--DTC**: The date or date and time of the assessment or the specimen or data collection from the subject, represented in a standardized character format.
- **--STDTC**: The start date or date and time of an intervention or event, represented in a standardized character format. | *Notes:* The start date of a Findings class record is stored in the --DTC variable.
- **--ENDTC**: The end date or date and time of an intervention, event, or finding, represented in a standardized character format.
- **--DY**: The number of days from the sponsor-defined reference start date to the date of collection (--DTC), used in study data tabulation. | *Notes:* The sponsor-defined reference start date is RFSTDTC in Demographics.
- **--STDY**: The number of days from the sponsor-defined reference start date to the start of an intervention or event (--STDTC), used for study data tabulation. | *Notes:* The sponsor-defined reference start date is RFSTDTC in Demographics.
- **--ENDY**: The number of days from the sponsor-defined reference start date to the end of an intervention, event, or finding (--ENDTC), used for study data tabulation. | *Notes:* The sponsor-defined reference start date is RFSTDTC in Demographics.
- **--NOMDY**: The nominal study day, relative to the sponsor-defined reference start date, used by data collection and reporting systems for grouping records for observations that may be scheduled to occur on different days into a single study day (e.g., for output on a tabulation report).
- **--NOMLBL**: The name for a protocol- defined nominal study day. | *Notes:* As presented in the study report.
- **--RPDY**: The day within the reproductive phase on which the test or observation occurred. | *Notes:* Expressed as an integer.
- **--RPSTDY**: The day within the reproductive phase on which the test or observation began. | *Notes:* Expressed as an integer.
- **--RPENDY**: The day within the reproductive phase on which the test or observation ended. | *Notes:* Expressed as an integer.
- **--XDY**: *Notes:* The actual study day of an intervention, event, or finding, derived relative to the first exposure to any protocol- specified treatment. Expressed in integer days relative to RFXSTDTC in Demographics.
- **--XSTDY**: *Notes:* The actual study day of the start of an intervention or event, derived relative to the first exposure to any protocol- specified treatment. Expressed in integer days relative to RFXSTDTC in Demographics.
- **--XENDY**: *Notes:* The actual study day of the end of an intervention, event, or finding, derived relative to the
- **--CHDY**: *Notes:* The actual study day of an intervention, event, or finding, derived relative to the first exposure to the challenge agent that induces the disease or condition that the investigational treatment is intended to cure, mitigate, treat, or prevent. Expressed in integer days relative to RFCSTDTC in Demographics.
- **--CHSTDY**: *Notes:* The actual study day of the start of an intervention or event derived relative to the first exposure to the challenge agent that induces the disease or condition that the investigational treatment is intended to c ure, mitigate, treat, or prevent. Expressed in integer days relative to RFCSTDTC in Demographics.
- **--CHENDY**: *Notes:* The actual study day of the end of an intervention, event, or finding derived relative to the first exposure to the challenge agent that induces the disease or condition that the investigational treatment is intended to cure, mitigate, treat, or prevent. Expressed in integer days relative to RFCSTDTC in Demographics.
- **--DUR**: The collected length of time during which an observation continues, represented in a standardized character format. | *Notes:* Used only if collected on the CRF and not derived.
- **--TPT**: The description of the time when a protocol-defined activity is planned to occur, used for study data tabulation. | *Notes:* This may be represented as an elapsed time relative to a fixed reference point (e.g., time since last dose). See --TPTNUM and --TPTREF. | *Examples:* "PREDOSE", "1 HOUR POST-DOSE"
- **--TPTNUM**: The numeric identifier of when an observation is planned to occur. | *Notes:* Used in sorting.
- **--ELTM**: The interval of time between a planned time point and a fixed reference point, represented in a standardized character format. | *Notes:* The fixed reference point is in --TPTREF. This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval.
- **--TPTREF**: The description of a time point that acts as a fixed reference for a series of planned time points, used for study data tabulation. | *Notes:* Description of the fixed reference point referred to by --ELTM, --TPTNUM, --TPT, --STINT, and --ENINT. | *Examples:* "PREVIOUS DOSE", "PREVIOUS MEAL"
- **--RFTDTC**: The actual date or date and time of a time point that acts as a fixed reference for a series of planned time points, represented in a standardized character format. | *Notes:* The fixed reference point is in --TPTREF.
- **--STRF**: The characterization of the start of an observation relative to the study reference period. | *Notes:* The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point represented by RFSTDTC and RFENDTC in Demographics.
- **--ENRF**: The characterization of the end of an observation relative to the study reference period. | *Notes:* The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point represented by RFSTDTC and RFENDTC in Demographics.
- **--EVLINT**: The planned time interval for which an observation is assessed, represented in a standardized character format. | *Notes:* Usually used with --DTC to describe an interval of this duration that ended at the time represented in --DTC. | *Examples:* "-P2M" to represent a period of the past 2 months as the evaluation interval for a question from a questionnaire.
- **--EVINTX**: A textual description of the planned time interval for which an observation is assessed, where the interval is not able to be represented in a standardized character format. | *Notes:* A value that cannot be represented in ISO 8601 format. | *Examples:* "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS"
- **--STRTPT**: The characterization of the start of an observation relative to a reference time point. | *Notes:* The sponsor-defined reference time point is in --STTPT.
- **--STTPT**: The description or date and/or time of a time point that acts as a fixed reference for characterizing the start of an observation. | *Notes:* This is the sponsor-defined reference point referred to by --STRTPT. | *Examples:* "2003-12-15", "VISIT 1"
- **--ENRTPT**: The characterization of the end of an observation relative to a reference time point. | *Notes:* The sponsor-defined reference time point is in --ENTPT.
- **--ENTPT**: The description or date and/or time of a time point that acts as a fixed reference for characterizing the end of an observation. | *Notes:* This is the sponsor-defined reference point referred to by --ENRTPT. | *Examples:* "2003-12-25", "VISIT 2"
- **MIDS**: *Notes:* The name of a specific instance of a Disease Milestone Type
- **RELMIDS**: *Notes:* The temporal relationship of the observation to the Disease Milestone Instance Name in MIDS. | *Examples:* "IMMEDIATELY BEFORE", "AT TIME OF", "AFTER"
- **MIDSDTC**: *Notes:* The start date/time of the Disease Milestone Instance Name in MIDS.
- **--STINT**: The start of a planned assessment interval relative to a reference time point, represented in a standardized character format. | *Notes:* The reference time point is in --TPTREF. As this variable describes planned timing of an assessment, caution should be exercised when using outside of the Findings class of domains. In an Events or Interventions domain, it may refer to the interval over which --OCCUR is assessed.
- **--ENINT**: The end of a planned assessment interval relative to a reference time point, represented in a standardized character format. | *Notes:* The reference time point is in --TPTREF. As this variable describes planned timing of an assessment, caution should be exercised when using outside of the Findings class of domains. In an Events or Interventions domain, it may refer to the interval over which --OCCUR is assessed.
- **--DETECT**: The number of days from the start of dosing to the earliest detection of a condition or pathogen.
- **--PTFL**: *Notes:* An indication that the specimen was collected at a single point in time. The value is "Y" or null.
- **--PDUR**: *Notes:* Planned duration of a finding. For a sample-based finding, this could apply to the planned duration of specimen collection.
- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "DM".
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **SUBJID**: *Notes:* Subject identifier, which must be unique within the study. Often the ID of the subject as recorded on a CRF.
- **RFSTDTC**: The start date or date and time of the sponsor-defined study reference period, represented in a standardized character format. | *Notes:* Usually equivalent to date/time when subject was first exposed to study treatment. Required for all randomized subjects; will be null for all subjects who did not meet the milestone the date requires, such as screen failures or unassigned subjects.
- **RFENDTC**: The end date or date and time of the sponsor-defined study reference period, represented in a standardized character format. | *Notes:* Usually equivalent to the date/time when a subject was determined to have ended the trial. Often equivalent to either date/time of last exposure to study treatment or date/time of last contact with the subject. Required for all randomized subjects;

