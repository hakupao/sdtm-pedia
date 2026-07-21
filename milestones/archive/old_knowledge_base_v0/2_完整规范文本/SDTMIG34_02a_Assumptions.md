# SDTMIG v3.4 --- Assumptions for Domain Models — Part 1

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 1/2 — 4.1-4.4: General Domain, Variable, Coding/Terminology, Time Assumptions
> **Original:** `SDTMIG34_02_Assumptions.md`
> **Related:** `SDTMIG34_02b_Assumptions.md`

---

## 4 Assumptions for Domain Models

### 4.1 General Domain Assumptions

#### 4.1.1 Review Study Data Tabulation Model and Implementation Guide

Review the SDTM as well as this complete implementation guide before attempting to use any of the individual domain models.

#### 4.1.2 Relationship to Analysis Datasets

Specific guidance on preparing analysis datasets can be found in the CDISC Analysis Data Model (ADaM)
Implementation Guide and other ADaM documents, available at https://www.cdisc.org/standards/foundational/adam.

#### 4.1.3 Additional Timing Variables

Additional Timing variables can be added as needed to a standard domain model based on the 3 general observation classes, except for the cases specified in Assumption 4.4.8, Date and Time Reported in a Domain Based on
Findings. Timing variables can be added to special-purpose domains only where specified in the SDTMIG domain model assumptions. Timing variables cannot be added to SUPPQUAL datasets or to RELREC (described in Section
8, Representing Relationships and Data).

##### 4.1.3.1 EPOCH Variable Guidance

When EPOCH is included in a Findings class domain, it should be based on the --DTC variable, since this is the date/time of the test or, for tests performed on specimens, the date/time of specimen collection. For observations in
Interventions or Events class domains, EPOCH should be based on the --STDTC variable, since this is the start of the intervention or event. A possible, though unlikely, exception would be a finding based on an interval specimen collection that started in one epoch but ended in another.  --ENDTC might be a more appropriate basis for EPOCH in such a case.
Sponsors should not impute EPOCH values, but should, where possible, assign EPOCH values on the basis of CRF instructions and structure, even if EPOCH was not directly collected and date/time data was not collected with sufficient precision to permit assignment of an observation to an EPOCH on the basis of date/time data alone. If it is not possible to determine the epoch of an observation, then EPOCH should be null. Methods for assigning EPOCH values can be described in the Define-XML document.
Because EPOCH is a study-design construct, it is not applicable to interventions or events that started before the subject's participation in a study, nor to findings performed before participation in a study. For such records,
EPOCH should be null. Note that a subject's participation in a study includes screening, which generally occurs before the reference start date (RFSTDTC) in the Demographics (DM) domain.

#### 4.1.4 Order of the Variables

The order of variables in the Define-XML document must reflect the order of variables in the dataset. The order of variables in CDISC domain models has been chosen to facilitate the review of the models and application of the models. Variables for the 3 general observation classes must be ordered with Identifiers variables first, followed by
Topic, Qualifier, and Timing variables. Within each role, variables must be ordered as shown in SDTM Sections
3.1.1, The Interventions Observation Class; 3.1.2, The Events Observation Class; 3.1.3, The Findings Observation
Class; 3.1.3.1, Findings About Events or Interventions; 3.1.4, Identifiers for All Classes; and 3.1.5, Timing
Variables for All Classes.

#### 4.1.5 SDTM Core Designations

Three categories are specified in the Core column in the domain models:

- A Required variable is any variable that is basic to the identification of a data record (i.e., essential key variables and a topic variable) or is necessary to make the record meaningful. Required variables must always be included in the dataset and cannot be null for any record.
- An Expected variable is any variable necessary to make a record useful in the context of a specific domain.
Expected variables may contain some null values, but in most cases will not contain null values for every record. When the study does not include the data item for an expected variable, however, a null column must still be included in the dataset, and a comment must be included in the Define-XML document to state that the study does not include the data item.
- A Permissible variable should be used in an SDTM dataset wherever appropriate. Although domain specification tables list only some of the identifier, timing, and general observation class variables listed in the SDTM, all are permissible unless specifically restricted in this implementation guide (see Section 2.7,
SDTM Variables Not Allowed in the SDTMIG) or by specific domain assumptions.
  - Domain assumptions that say a Permissible variable is "generally not used" do not prohibit use of the variable.
  - If a study includes a data item that would be represented in a Permissible variable, then that variable must be included in the SDTM dataset, even if null. Indicate no data were available for that variable in the Define-XML document.
  - If a study did not include a data item that would be represented in a Permissible variable, then that variable should not be included in the SDTM dataset and should not be declared in the Define-XML document.

#### 4.1.6 Additional Guidance on Dataset Naming

SDTM datasets are normally named to be consistent with the domain code; for example, the Demographics dataset (DM) is named dm.xpt. (See the SDTM Domain Abbreviation codelist, C66734, in CDISC Controlled Terminology (https://www.cancer.gov/research/resources/terminology/cdisc) for standard domain codes). Exceptions to this rule are described in Section 4.1.7, Splitting Domains, for general observation class datasets and in Section 8,
Representing Relationships and Data, for RELREC and SUPP-- datasets.
In some cases, sponsors may need to define new custom domains and may be concerned that CDISC domain codes defined in the future will conflict with those they choose to use. To eliminate any risk of a sponsor using a name that
CDISC later determines to have a different meaning, domain codes beginning with the letters X, Y, and Z have been reserved for the creation of custom domains. Any letter or number may be used in the second position. Note the use of codes beginning with X, Y, or Z is optional, and not required for custom domains.

#### 4.1.7 Splitting Domains

Sponsors may choose to split a domain of topically related information into physically separate datasets.
- A domain based on a general observation class may be split according to values in --CAT. When a domain is split on --CAT, --CAT must not be null.
- The Findings About (FA) domain (see Section 6.4.4, Findings About Events or Interventions) may alternatively be split based on the domain of the value in --OBJ. For example, FACM would store findings about Concomitant/Prior Medications (CM) records. See Section 6.4.2, Naming Findings About Domains, for more details.

The following rules must be adhered to when splitting a domain into separate datasets to ensure they can be appended back into 1 domain dataset:
1. The value of DOMAIN must be consistent across the separate datasets as it would have been if they had not
been split (e.g., QS, FA).
1. All variables that require a domain prefix (e.g., --TESTCD, --LOC) must use the value of DOMAIN as the
prefix value (e.g., QS, FA).
1. --SEQ must be unique within USUBJID for all records across all the split datasets. If there are 1000 records
for a USUBJID across the separate datasets, all 1000 records need unique values for --SEQ.

1. When relationship datasets (e.g., SUPPxx, FAxx, CO, RELREC) relate back to split parent domains,
IDVAR would generally be --SEQ. When IDVAR is a value other than --SEQ (e.g., --GRPID, --REFID, -- SPID), care should be used to ensure that the parent records across the split datasets have unique values for the variable specified in IDVAR, so that related children records do not accidentally join back to incorrect parent records.
1. Permissible variables included in one split dataset need not be included in all split datasets.
2. For domains with 2-letter domain codes (i.e., other than SUPPxx and RELREC), split dataset names can be
up to 4 characters in length. For example, if splitting by --CAT, dataset names would be the domain name plus up to 2 additional characters (e.g., QS36 for SF-36). If splitting Findings About by parent domain, then the dataset name would be the domain code, "FA", plus the 2-character domain code for parent domain code (e.g., "FACM"). The 4-character dataset-name limitation allows the use of a Supplemental Qualifier dataset associated with the split dataset.
1. Supplemental Qualifier datasets for split domains would also be split. The nomenclature would include the
additional 1 to 2 characters used to identify the split dataset (e.g., SUPPQS36, SUPPFACM). The value of
RDOMAIN in the SUPP-- datasets would be the 2-character domain code (e.g., QS, FA).
1. In RELREC, if a dataset-level relationship is defined for a split Findings About domain, then RDOMAIN
may contain the 4-character dataset name, rather than the domain name "FA", as shown in the following example. relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | CM |  | CMSPID |  | ONE | 1 |
| 2 | ABC | FACM |  | FASPID |  | MANY | 1 |

##### 4.1.7.1 Example of Splitting Questionnaires

QRS datasets are routinely created and reviewed for the individual QRS instrument. This example shows the QS domain data split into 3 datasets: Clinical Global Impression (QSCG), Pain Intensity (QSPI), and Satisfaction of
Life Scale (QSSW). Each dataset represents a subset of the QS domain data and has only 1 value of QSCAT.

QS Domains Dataset for Clinical Global Impressions 
qscg.xpt

| Row | STUDYID | DOMAIN | USUBJID | QSSEQ | QSTESTCD | QSTEST | QSCAT | QSORRES | QSSTRESC | QSSTRESN | QSLOBXFL | VISITNUM | VISIT | VISITDY | QSDTC | QSDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CDISC01 | QS | CDISC01.100008 | 1 | CGI0201 | CGI02-Severity | CGI | Moderate | 4 | 4 | Y | 1 | WEEK 1 | 1 | 2003-04-15 | 1 |
| 2 | CDISC01 | QS | CDISC01.100008 | 2 | CGI0201 | CGI02-Severity | CGI | Mild | 3 | 3 |  | 2 | WEEK 2 | 7 | 2003-04-21 | 7 |
| 3 | CDISC01 | QS | CDISC01.100008 | 3 | CGI0202 | CGI02-Change | CGI | Minimally Improved | 3 | 3 |  | 2 | WEEK 2 | 7 | 2003-04-21 | 7 |
| 4 | CDISC01 | QS | CDISC01.100008 | 4 | CGI0203 | CGI02-Improvement | CGI | A little better | 3 | 3 |  | 2 | WEEK 2 | 7 | 2003-04-21 | 7 |
| 5 | CDISC01 | QS | CDISC01.100014 | 1 | CGI0201 | CGI02-Severity | CGI | Moderate | 4 | 4 | Y | 1 | WEEK 1 | 1 | 2003-04-15 | 1 |
| 6 | CDISC01 | QS | CDISC01.100014 | 2 | CGI0201 | CGI02-Severity | CGI | Mild | 3 | 3 |  | 2 | WEEK 2 | 7 | 2003-04-21 | 7 |
| 7 | CDISC01 | QS | CDISC01.100014 | 3 | CGI0202 | CGI02-Change | CGI | Minimally Improved | 3 | 3 |  | 2 | WEEK 2 | 7 | 2003-04-21 | 7 |
| 8 | CDISC01 | QS | CDISC01.100014 | 4 | CGI0203 | CGI02-Improvement | CGI | A little better | 3 | 3 |  | 2 | WEEK 2 | 7 | 2003-04-21 | 7 |
#### 4.1.8 Origin Metadata

##### 4.1.8.1 Origin Metadata for Variables

The origin element in the Define-XML document file is used to indicate where the data originated. Its purpose is to unambiguously communicate to the reviewer the origin of the data source. For example, data could be collected (on the CRF, from a vendor, or from a device), derived, or assigned; CRF data should be traceable to an annotated CRF and derived data should be traceable to some derivation algorithm. The Define-XML specification is the definitive source of allowable origin values. Additional guidance and supporting examples can be referenced using the
Metadata Submission Guidelines (MSG) for SDTMIG.

##### 4.1.8.2 Origin Metadata for Records

Sponsors are cautioned to recognize that a derived origin means that all values for that variable were derived, and that collected on the CRF applies to all values as well. In some cases, both collected and derived values may be reported in the same field. For example, some records in a Findings dataset such as Questionnaires (QS) contain values collected from the CRF; other records may contain derived values, such as a total score. When both derived and collected values are reported in a variable, the origin is to be described using value-level metadata in the Define-
XML document.

#### 4.1.9 Assigning Natural Keys in the Metadata

Section 3.2, Using the CDISC Domain Models in Regulatory Submissions – Dataset Metadata, indicates that a sponsor should include in the metadata the variables that contribute to the natural key for a domain. In a case where a dataset includes a mix of records with different natural keys, the natural key that provides the most granularity is the one that should be provided. The following example illustrates how to do this, and include a case where a Supplemental Qualifier variable is referenced because it forms part of the natural key.

##### Musculoskeletal System Findings (MK) Domain Example

Sponsor A chooses the following natural key for the MK domain:

> `STUDYID, USUBJID, VISITNUM, MKTESTCD`

Sponsor B collects data in such a way that the location (MKLOC and MKLAT) and method (MKMETHOD) variables need to be included in the natural key to identify a unique row. Sponsor B then defines the following natural key for the MK domain.

> `STUDYID, USUBJID, VISITNUM, MKTESTCD, MKLOC, MKLAT, MKMETHOD`

In certain instances a Supplemental Qualifier variable (i.e., a QNAM value; see Section 8.4, Relating Non-standard Variable Values to a Parent Domain) might also contribute to the natural key of a record, and therefore needs to be referenced as part of the natural key for a domain. The important concept here is that a domain is not limited by physical structure. A domain may comprise more than 1 physical dataset (e.g., the main domain dataset and its associated Supplemental Qualifiers dataset). Supplemental Qualifier variables should be referenced in the natural key by using a 2-part name. The word QNAM must be used as the first part of the name to indicate that the contributing variable exists in a domain-specific SUPP--; the second part is the value of QNAM that ultimately becomes a column reference when the SUPPQUAL records are joined on to the main domain dataset (e.g., QNAM.XVAR when the SUPP-- record has a QNAM of "XVAR").

In this example, sponsor B might have collected data that used different imaging methods, using imaging devices with different makes and models, and using different hand positions. The sponsor considers the make and model information and hand position to be essential data that contributes to the uniqueness of the test result, and so includes a device identifier (SPDEVID) in the data and creates a Supplemental Qualifier variable for hand position (QNAM = "MKHNDPOS"). The natural key is then defined as follows:

> `STUDYID, USUBJID, SPDEVID, VISITNUM, MKTESTCD, MKLOC, MKLAT, MKMETHOD, QNAM.MKHNDPOS`

where the notation "QNAM.MKHNDPOS" means the Supplemental Qualifier whose QNAM is "MKHNDPOS".

This approach becomes very useful in a Findings domain when --TESTCD values are "generic" and rely on other variables to completely describe the test. The use of generic test codes helps to create distinct lists of manageable controlled terminology for --TESTCD. In studies where multiple repetitive tests or measurements are being made, for example in a rheumatoid arthritis study where repetitive measurements of bone erosion in the hands and wrists might be made using both X-ray and MRI equipment, the generic MKTEST "Sharp/Genant Bone Erosion Score" would be used in combination with other variables to fully identify the result.
Taking just the phalanges, a sponsor might want to express the following in a test in order to make it unique:
- Left or right hand
- Phalangeal joint position (which finger, which joint)
- Rotation of the hand
- Method of measurement (x-ray or MRI)
- Machine make and model
When CDISC Controlled Terminology for a test is not available, and a sponsor creates --TEST and --TESTCD values, trying to encapsulate all information about a test within a unique value of a --TESTCD is not a recommended approach for the following reasons:
- It results in the creation of a potentially large number of test codes.
- The 8-character values of --TESTCD become less intuitively meaningful.
- Multiple test codes are essentially representing the same test or measurement simply to accommodate attributes of a test within the --TESTCD value itself (e.g., to represent a body location at which a measurement was taken).
  
As a result, the preferred approach would be to use a generic (or simple) test code that requires associated qualifier variables to fully express the test detail. This approach was used in creating the CDISC Controlled Terminology used in this example:

The MKTESTCD value "SGBESCR" is a generic test code, and additional information about the test is provided by separate qualifier variables. The variables that completely specify a test may include domain variables and supplemental qualifier variables. Expressing the natural key becomes very important in this situation in order to communicate the variables that contribute to the uniqueness of a test.

The following variables would be used to fully describe the test. The natural key for this domain includes both parent dataset variables and a supplemental qualifier variable that contribute to the natural key of each row and to describe the uniqueness of the test.

| SPDEVID | MKTESTCD | MKTEST | MKLOC | MKLAT | MKMETHOD | QNAM.MKHNDPOS |
| --- | --- | --- | --- | --- | --- | --- |
| ACME3000 | SGBESCR | Sharp/Genant Bone Erosion Score | METACARPOPHALANGEAL JOINT 1 | LEFT | X-RAY | PALM UP |

### 4.2 General Variable Assumptions

#### 4.2.1 Variable-naming Conventions

SDTM variables are named according to a set of conventions, using fragment names (see Appendix D, CDISC Variable-naming Fragments). Variables with names ending in "CD" are "short" versions of associated variables that do not include the "CD" suffix (e.g., --TESTCD is the short version of --TEST).

Values of --TESTCD must be limited to 8 characters and cannot start with a number, nor can they contain characters other than letters, numbers, or underscores. This is to avoid possible incompatibility with SAS v5 transport files. This limitation will be in effect until the use of other formats (e.g., Dataset-XML) becomes acceptable to regulatory authorities.

Because QNAM serves the same purpose as --TESTCD within supplemental qualifier datasets, values of QNAM are subject to the same restrictions as values of --TESTCD.

Values of other "CD" variables are not subject to the same restrictions as --TESTCD:

- ETCD (the companion to ELEMENT) and TSPARMCD (the companion to TSPARM) are limited to 8 characters and do not have the character restrictions that apply to --TESTCD. These values should be short for ease of use in programming, but it is not expected that they will need to serve as variable names.
- ARMCD is limited to 20 characters and does not have the character restrictions that apply to --TESTCD. The maximum length of ARMCD is longer than for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20. This same rule applies to the ACTARMCD variable.

Variable descriptive names (labels), up to 40 characters, should be provided as data variable labels for all variables, including Supplemental Qualifier variables.

Use of variable names (other than domain prefixes), formats, decodes, terminology, and data types for the same type of data (even for custom domains and Supplemental Qualifiers) should be consistent within and across studies within a submission.

#### 4.2.2 Two-character Domain Identifier

In order to minimize the risk of difficulty when merging/joining domains for reporting purposes, the 2-character domain identifier is used as a prefix in most variable names.

Variables in domain specification tables (see Section 5, Models for Special-purpose Domains; Section 6, Domain Models Based on the General Observation Classes; Section 7, Trial Design Model Datasets; Section 8, Representing Relationships and Data; and Section 9, Study References) already specify the complete variable names. When adding variables from the SDTM to standard domains or creating custom domains based on the general observation classes, sponsors must replace the "--" prefix in the SDTM tables of General Observation Class, Timing, and Identifier variables with the 2-character domain identifier (DOMAIN) value for that domain/dataset. The 2-character domain code is limited to A-Z for the first character, and A-Z, 0-9 for the second character. No other characters are allowed. This is for compatibility with SAS v5 transport files and with file naming requirements as part of the Electronic Common Technical Document (eCTD).

The following variables are exceptions to the philosophy that all variable names are prefixed with the domain identifier:

- Required Identifiers (STUDYID, DOMAIN, USUBJID)
- Commonly used grouping and merge keys (e.g., VISIT, VISITNUM, VISITDY)
- All Demographics (DM) domain variables other than DMDTC and DMDY
- All variables in RELREC and SUPPQUAL, and some variables in the Comments and Trial Design datasets

Required identifiers are not prefixed because they are usually used as keys when merging/joining observations. The --SEQ and the optional Identifiers --GRPID and --REFID are prefixed because they may be used as keys when relating observations across domains.

#### 4.2.3 Use of "Subject" and USUBJID

"Subject" is used to generically refer to both patients and healthy volunteers in order to be consistent with the recommendation in FDA guidance. The term "subject" should be used consistently in all labels and Define-XML document comments. To identify a subject uniquely across all studies for all applications or submissions involving the product, a unique identifier (USUBJID) should be assigned and included in all datasets.

The unique subject identifier (USUBJID) is required in all datasets containing subject-level data. USUBJID values must be unique for each trial participant (subject) across all trials in the submission. This means that no 2 or more subjects, across all trials in the submission, may have the same USUBJID. In addition, the same person who participates in multiple clinical trials (when this is known) must be assigned the same USUBJID value in all trials.

CDISC does not recommend any specific format for the values of USUBJID, only that the values need to be unique for all subjects in the submission, and across multiple submissions for the same compound. Many sponsors concatenate values for the study, site, and subject into USUBJID, but this is not a requirement. It is acceptable to use any format for USUBJID, as long as the values are unique across all subjects.

The following dm.xpt sample rows illustrate a single subject who participates in 2 studies, first in ACME01 and later in ACME14. Note that this is only one example of the possible values for USUBJID.

dm.xpt

| Row | STUDYID | DOMAIN | USUBJID | SUBJID | SITEID | INVNAM |
|---|---|---|---|---|---|---|
| 1 | ACME01 | DM | ACME01-05-001 | 001 | 05 | John Doe |

dm.xpt

| Row | STUDYID | DOMAIN | USUBJID | SUBJID | SITEID | INVNAM |
|---|---|---|---|---|---|---|
| 1 | ACME14 | DM | ACME01-05-001 | 017 | 14 | Mary Smith |

#### 4.2.4 Text Case in Submitted Data

It is recommended that text data be submitted in text that is all upper case (e.g., NEGATIVE). Exceptions may include long text data (e.g., comment text) and values of --TEST in Findings datasets (which may be more readable in title case if used as labels in transposed views). Values from CDISC Controlled Terminology or external code systems (e.g., MedDRA, SNOMED) or response values for QRS instruments specified by the instrument documentation should be in the case specified by those sources, which may be mixed case. The case used in the text data must match the case used in the controlled terminology provided in the Define-XML document.

#### 4.2.5 Convention for Missing Values

Missing values for individual data items should be represented by nulls. Conventions for representing observations not done, using the SDTM --STAT and --REASND variables, are addressed in Section 4.5.1.2, Tests Not Done, and the individual domain models.

#### 4.2.6 Grouping Variables and Categorization

Grouping variables are Identifiers and Qualifiers variables—such as the --CAT (Category) and --SCAT (Subcategory)—that group records in the SDTM domains/datasets and can be assigned by sponsors to categorize topic-variable values. For example, a lab record with LBTEST = "SODIUM" might have LBCAT = "CHEMISTRY" and LBSCAT = "ELECTROLYTES". Values for --CAT and --SCAT should not be redundant with the domain name or dictionary classification provided by --DECOD and --BODSYS.
##### Hierarchy of Grouping Variables

```
STUDYID
DOMAIN
  --CAT
  --SCAT

   USUBJID
     --GRPID
     --LNKID
     --LNKGRP
```

##### How Grouping Variables Group Data 

###### For the subject

1. All records with the same USUBJID value are a group of records that describe that subject.

###### Across subjects (records with different USUBJID values)

1. All records with the same STUDYID value are a group of records that describe that study.
2. All records with the same DOMAIN value are a group of records that describe that domain.

3. --CAT (Category) and --SCAT (Sub-category) values further subset groups within the domain. Generally, --CAT/--SCAT values have meaning within a particular domain. However, it is possible to use the same values for --CAT/--SCAT in related domains (e.g., MH and AE). When values are used across domains, the meanings should be the same. Examples of where --CAT/--SCAT may have meaning across domains/datasets include:

   a. Cases where different domains in the same general observation class contain similar conceptual information. Adverse Events (AE), Medical History (MH), and Clinical Events (CE), for example, are conceptually the same data, the only differences being when the event started relative to the study start and whether the event is considered a regulatory-reportable adverse event in the study. Neurotoxicities collected in oncology trials both as separate Medical History CRFs (MH domain) and Adverse Event CRFs (AE domain) could both identify/collect "Paresthesia of the left arm". In both domains, the --CAT variable could have the value of "NEUROTOXICITY".

   b. Cases where multiple datasets are necessary to capture data about the same topic. Following the oncology example, the existence and start and stop date of paresthesia of the left arm may be reported as an adverse event (AE domain), whereas the severity of the event is captured at multiple visits and recorded as Findings About (FA dataset). In both cases the --CAT variable could have a value of "NEUROTOXICITY".

   c. Cases where multiple domains are necessary to capture data that were collected together and have an implicit relationship, perhaps identified in the Related Records (RELREC) special-purpose dataset. Stress-test data collection may capture the following:
      - i. Information about the occurrence, start, stop, and duration of the test (in the Procedures (PR) domain)
      - ii. Vital Signs recorded during the stress test (VS domain)
      - iii. Treatments (e.g., oxygen) administered during the stress test (in an Interventions domain)

   In such cases, the data collected during the stress tests recorded in 3 separate domains may all have --CAT/--SCAT values (STRESS TEST) that identify that data were collected during the stress test.

###### Within subjects (records with the same USUBJID values)

1. --GRPID values further group (subset) records within USUBJID. All records in the same domain with the same --GRPID value are a group of records within USUBJID. Unlike --CAT and --SCAT, --GRPID values are not intended to have any meaning across subjects and are usually assigned during or after data collection.

Although --SPID and --REFID are Identifier variables, they may sometimes be used as grouping variables and may also have meaning across domains.

--LNKID and --LNKGRP express values that are used to link records in separate domains. As such, these variables are often used in IDVAR in a RELREC relationship when there is a dataset-to-dataset relationship.

1. --LNKID is a grouping identifier used to identify a record in one domain that is related to records in another domain, often forming a one-to-many relationship.
2. --LNKGRP is a grouping identifier used to identify a group of records in one domain that is related to a record in another domain, often forming a many-to-one relationship.

##### Differences Between Grouping Variables

The primary distinctions between --CAT/--SCAT and --GRPID are:
1. --CAT/--SCAT are known (identified) about the data before it is collected.
2. --CAT/--SCAT values group data across subjects.
3. --CAT/--SCAT may have some controlled terminology.
4. --GRPID is usually assigned during or after data collection at the discretion of the sponsor.
5. --GRPID groups data only within a subject.
6. --GRPID values are sponsor-defined, and will not be subject to controlled terminology.

Therefore, data that would be the same across subjects is usually more appropriate in --CAT/--SCAT, and data that would vary across subjects is usually more appropriate in --GRPID. For example, a concomitant medication administered as part of a known combination therapy for all subjects (e.g., "Mayo Clinic Regimen") would more appropriately use --CAT/--SCAT to identify the medication as part of that regimen. Groups of medications recorded on a Serious Adverse Event (SAE) form as treatments for the SAE would more appropriately use --GRPID because groupings are likely to differ across subjects.
In domains based on the Findings general observation class, the --RESCAT variable can be used to categorize results after the fact. --CAT and --SCAT by contrast, are generally defined by the sponsor or used by the investigator at the point of collection, not after assessing the value of Findings results.

#### 4.2.7 Submitting Free Text from the CRF

Sponsors often collect free-text data on a CRF to supplement a standard field. This often occurs as part of a list of choices accompanied by "Other, specify." The manner in which these data are submitted will vary based on their role.
##### 4.2.7.1 "Specify" Values for Non-result Qualifier Variables

When free-text information is collected to supplement a standard non-result qualifier field, the free-text value should be placed in the SUPP-- dataset described in Section 8.4, Relating Non-standard Variable Values to a Parent Domain. When applicable, controlled terminology should be used for SUPP-- field names (QNAM) and their associated labels (QLABEL; see Section 8.4, Relating Non-standard Variable Values to a Parent Domain, and Appendix C1, Supplemental Qualifiers Name Codes).

For example, when a description of "Other Medically Important Serious Adverse Event" category is collected on a CRF, the free-text description should be stored in the SUPPAE dataset.

- AESMIE = "Y"
- SUPPAE QNAM = "AESOSP", QLABEL = "Other Medically Important SAE", QVAL = "HIGH RISK FOR ADDITIONAL THROMBOSIS"

Another example is a CRF that collects reason for dose adjustment with additional free-text description:
> Reason for Dose Adjustment (EXADJ): Describe ________________
> - Adverse Event
> - Insufficient Response
> - Non-medical Reason

The free-text description should be stored in the SUPPEX dataset.
- EXADJ = "NONMEDICAL REASON"
- SUPPEX QNAM = "EXADJDSC", QLABEL = "Reason For Dose Adjustment Description", QVAL = "PATIENT MISUNDERSTOOD INSTRUCTIONS"

Note that QNAM references the "parent" variable name with the addition of "DSC". Likewise, the label is a modification of the parent variable label.

When the CRF includes a list of values for a qualifier field that includes "Other" and the "Other" is supplemented with a "Specify" free-text field, then the manner in which the free-text "Specify" value is submitted will vary based on the sponsor's coding practice and analysis requirements.

For example, consider a CRF that collects the indication for an analgesic concomitant medication (CMINDC) using a list of prespecified values and an "Other, specify" field:
> Indication for analgesic: &#9675; Post-operative pain &#9675; Headache &#9675; Menstrual pain &#9675; Myalgia &#9675; Toothache &#9675; Other, specify: ________________

An investigator has selected "OTHER" and specified "Broken arm". Several options are available for submission of this data:
1. If the sponsor wishes to maintain controlled terminology for the CMINDC field and limit the terminology to the 5 prespecified choices, then the free text is placed in SUPPCM.

   | CMINDC |
   |---|
   | OTHER |

   suppcm.xpt

   | QNAM | QLABEL | QVAL |
   |---|---|---|
   | CMINDOTH | Other Indication | BROKEN ARM |

2. If the sponsor wishes to maintain controlled terminology for CMINDC but will expand the terminology based on values seen in the "Other, specify" field, then the value of CMINDC will reflect the sponsor's coding decision and SUPPCM could be used to store the verbatim text.

   | CMINDC |
   |---|
   | FRACTURE |

   suppcm.xpt

   | QNAM | QLABEL | QVAL |
   |---|---|---|
   | CMINDOTH | Other Indication | BROKEN ARM |

   Note that the sponsor might choose a different value for CMINDC (e.g., "BONE FRACTURE") depending on the sponsor's coding practice and analysis requirements.

3. If the sponsor does not require that controlled terminology be maintained and wishes for all responses to be stored in a single variable, then CMINDC will be used and SUPPCM is not required.

   | CMINDC |
   |---|
   | BROKEN ARM |

##### 4.2.7.2 "Specify" Values for Result Qualifier Variables

When the CRF includes a list of values for a result field that includes "Other" and the "Other" is supplemented with a "Specify" free-text field, then the manner in which the free-text "Specify" value is submitted will vary based on the sponsor's coding practice and analysis requirements.

For example, consider a CRF where the sponsor requests the subject's eye color:
> Eye Color: &#9675; Brown &#9675; Black &#9675; Blue &#9675; Green &#9675; Other, specify: ________________

An investigator has selected "OTHER" and specified "BLUEISH GRAY". As in the preceding discussion for non-result qualifier values, the sponsor has several options for submission:

1. If the sponsor wishes to maintain controlled terminology in the standard result field and limit the terminology to the 5 prespecified choices, then the free text is placed in --ORRES and the controlled terminology in --STRESC.

   | SCTEST | SCORRES | SCSTRESC |
   |---|---|---|
   | Eye Color | BLUEISH GRAY | OTHER |

2. If the sponsor wishes to maintain controlled terminology in the standard result field, but will expand the terminology based on values seen in the "Other, specify" field, then the free text is placed in --ORRES and the value of --STRESC will reflect the sponsor’s coding decision.

   | SCTEST | SCORRES | SCSTRESC |
   |---|---|---|
   | Eye Color | BLUEISH GRAY | GRAY |

3. If the sponsor does not require that controlled terminology be maintained, the verbatim value will be copied to --STRESC.

   | SCTEST | SCORRES | SCSTRESC |
   |---|---|---|
   | Eye Color | BLUEISH GRAY | BLUEISH GRAY |

##### 4.2.7.3 "Specify" Values for Topic Variables

**Interventions**

If a list of specific treatments is provided along with "Other, Specify", --TRT should be populated with the name of the treatment found in the specified text. If the sponsor wishes to distinguish between the prespecified list of treatments and those recorded in "Other, Specify," the --PRESP variable could be used. For example:

> Indicate which of the following concomitant medications was used to treat the subject’s headaches: &#9675; Acetaminophen &#9675; Aspirin &#9675; Ibuprofen &#9675; Naproxen &#9675; Other, specify: ________________

If ibuprofen and diclofenac were reported, the CM dataset would include the following:

| CMTRT | CMPRESP |
|---|---|
| IBUPROFEN | Y |
| DICLOFENAC | |

**Events**

"Other, Specify" for events may be handled similarly to Interventions. --TERM should be populated with the description of the event found in the specified text and --PRESP could be used to distinguish between prespecified and free-text responses.

**Findings**

"Other, Specify" for tests may be handled similarly to Interventions. --TESTCD and --TEST should be populated with the code and description of the test found in the specified text. If specific tests are not listed on the CRF and the investigator has the option of writing in tests, then the name of the test would have to be coded to ensure that all --TESTCD and --TEST values are consistent with the test controlled terminology. For example, a lab CRF collected values for hemoglobin, hematocrit, and "Other, specify". The value the investigator wrote for "Other, specify" was "Prothrombin time" with an associated result and units. The sponsor would submit the controlled terminology for this test: LBTESTCD would be "PT" and LBTEST would be "Prothrombin Time", rather than the verbatim term, "Prothrombin time" supplied by the investigator.

##### 4.2.7.4 "Specify" Values for --OBJ

As illustrated in the following figure, when findings are collected about an event or intervention, and the name of the event or intervention is collected in an "Other, specify" CRF field, the value in --OBJ variable depends on whether the Findings record has a parent record and whether the "Other, specify" value was coded. See also Section 6.4.3,
Variables Unique to Findings About.
*Figure 4.2.7.4-1: Decision Tree for Populating --OBJ*

#### 4.2.8 Multiple Values for a Variable

##### 4.2.8.1 Multiple Values for an Intervention or Event Topic Variable

If multiple values are reported for an intervention or event topic variable (e.g., --TRT in an Interventions general observation-class dataset or --TERM in an Events general observation-class dataset), it is expected that the sponsor will split the values into multiple records or otherwise resolve the multiplicity per the sponsor's data management standard operating procedures. For example, if an adverse event term of "Headache and nausea" or a concomitant medication of "Tylenol and Benadryl" is reported, sponsors will often split the original report into separate records and/or query the site for clarification. By the time of submission, datasets should be in conformance with the record structures described in the SDTMIG.

Note: The Disposition (DS) dataset is an exception to the general rule of splitting multiple topic values into separate records. For DS, 1 record for each disposition or protocol milestone is permitted according to the domain structure.
For cases of multiple reasons for discontinuation see Section 6.2.4, Disposition, assumption 5 for additional information.

##### 4.2.8.2 Multiple Values for a Findings Result Variable

If multiple result values (--ORRES) are reported for a test in a Findings class dataset, multiple records should be submitted for that --TESTCD.

For example,
- EGTESTCD = "SPRTARRY", EGTEST = "Supraventricular Tachyarrhythmias", EGORRES = "ATRIAL
FIBRILLATION"
- EGTESTCD = "SPRTARRY", EGTEST = "Supraventricular Tachyarrhythmias", EGORRES = "ATRIAL
FLUTTER"

When a finding can have multiple results, the key structure for the findings dataset must be adequate to distinguish between the multiple results. See Section 4.1.9, Assigning Natural Keys in the Metadata.

##### 4.2.8.3 Multiple Values for a Non-result Qualifier Variable

The SDTM permits 1 value for each qualifier variable per record. If multiple values exist (e.g., due to a "Check all that apply" instruction on a CRF), then the value for the qualifier variable should be "MULTIPLE" and SUPP-- should be used to store the individual responses. It is recommended that the SUPP-- QNAM value reference the corresponding standard domain variable with an appended number or letter. In some cases, the standard variable name will be shortened to meet the 8-character variable name requirement, or it may be clearer to append a meaningful character string as shown in the second Adverse Events (AE) example below, where the first 3 characters of the drug name are appended. Likewise, the QLABEL value should be similar to the standard label. The values stored in QVAL should be consistent with the controlled terminology associated with the standard variable.

See Section 8.4, Relating Non-standard Variable Values to a Parent Domain, for additional guidance on maintaining appropriately unique QNAM values.

The following example includes selected variables from the ae.xpt and suppae.xpt datasets for a rash with locations on the face, neck, and chest.

ae.xpt

| AETERM | AELOC |
|---|---|
| RASH | MULTIPLE |

suppae.xpt

| QNAM | QLABEL | QVAL |
|---|---|---|
| AELOC1 | Location of the Reaction 1 | FACE |
| AELOC2 | Location of the Reaction 2 | NECK |
| AELOC3 | Location of the Reaction 3 | CHEST |

In some cases, values for QNAM and QLABEL more specific than these may be needed.

For example, a sponsor might conduct a study with 2 study drugs (e.g., open-label study of Abcicin + Xyzamin), and may require the investigator assess causality and describe action taken for each drug for the rash:

ae.xpt

| AETERM | AEREL | AEACN |
|---|---|---|
| RASH | MULTIPLE | MULTIPLE |

suppae.xpt

| QNAM | QLABEL | QVAL |
|---|---|---|
| AERELABC | Causality of Abcicin | POSSIBLY RELATED |
| AERELXYZ | Causality of Xyzamin | UNLIKELY RELATED |
| AEACNABC | Action Taken with Abcicin | DOSE REDUCED |
| AEACNXYZ | Action Taken with Xyzamin | DOSE NOT CHANGED |

In each of these examples, the use of SUPPAE should be documented in the Define-XML document and the annotated CRF. The controlled terminology used should be documented as part of value-level metadata.

If the sponsor has clearly documented that one response is of primary interest (e.g., in the CRF, protocol, or analysis plan), the standard domain variable may be populated with the primary response and SUPP-- may be used to store the secondary response(s).

For example, if Abcicin is designated as the primary study drug in the example above:

ae.xpt

| AETERM | AEREL | AEACN |
|---|---|---|
| RASH | POSSIBLY RELATED | DOSE REDUCED |

suppae.xpt

| QNAM | QLABEL | QVAL |
|---|---|---|
| AERELX | Causality of Xyzamin | UNLIKELY RELATED |
| AEACNX | Action Taken with Xyzamin | DOSE NOT CHANGED |

Note that in the latter case, the label for standard variables AEREL and AEACN will have no indication that they pertain to Abcicin. This association must be clearly documented in the metadata and annotated CRF.

##### 4.2.8.4 Multiple Values for a Parameter

If multiple values (--VAL) are reported for a parameter in a Trial Design or Study Reference dataset (e.g., TS, OI), multiple records should be submitted for that --PARMCD.

For example,
- TSPARMCD = "TTYPE", TSPARM = "Trial Type", TSVAL = "EFFICACY"
- TSPARMCD = "TTYPE", TSPARM = "Trial Type", TSVAL = "SAFETY"

When a parameter can have multiple values, the key structure for the dataset must be adequate to distinguish between the multiple records. See Section 4.1.9, Assigning Natural Keys in the Metadata.

#### 4.2.9 Variable Lengths

When variable length is referenced in the SDTMIG, this refers to the length in bytes of ASCII character strings.
Very large transport files have become an issue for certain regulatory authorities (e.g., US FDA) to process. One of the main contributors to large file sizes has been sponsors using the maximum length of 200 for character variables.
To help rectify this situation:
- The maximum SAS v5 transport file character variable length of 200 characters should not be used unless necessary.
- Sponsors should consider the nature of the data and apply reasonable, appropriate lengths to variables. For example:
  - The length of flags will always be 1.
  - --TESTCD and IDVAR will never be more than 8, so the length can always be set to 8.
  - The length for variables that use controlled terminology can be set to the length of the longest term.

### 4.3 Coding and Controlled Terminology Assumptions

Examples provided in the CDISC Notes column and domain examples are only examples and not intended to imply controlled terminology. For current CDISC Controlled Terminology, visit https://datascience.cancer.gov/resources/cancer-vocabulary/cdisc-terminology.

#### 4.3.1 Controlled Terms, Codelist or Format Column

As of SDTMIG v3.3, controlled terminology is represented in the following ways:
- A single asterisk (*) when CDISC Controlled Terminology is not currently available but the SDS Team expects that sponsors may have their own controlled terminology and/or the CDISC Controlled
Terminology Team may develop controlled terminology in the future
- The single applicable value for the variable DOMAIN (e.g., "PR")
- The name of a CDISC codelist, represented as a hyperlink in parentheses (e.g., "(NY)")
- A short reference to an external terminology (e.g., "MedDRA", "ISO 3166-1 alpha-3")
In addition, the Controlled Terms, Codelist or Format column has been used to indicate variables that use an ISO
8601 format.

#### 4.3.2 Controlled Terminology Text Case

Terms from controlled terminology should be in the case that appears the source codelist or code system (e.g.,
CDISC codelist or external code system such as MedDRA). See Section 4.2.4, Text Case in Submitted Data.

#### 4.3.3 Controlled Terminology Values

The controlled terminology or a reference to the controlled terminology should be included in the Define-XML document file wherever applicable. All values in the permissible value set for the study should be included, whether or not they are represented in the submitted data. Note that a null value should not be included in the permissible value set. A null value is implied for any list of controlled terms unless the variable is "Required" (see Section 4.1.5,
SDTM Core Designations).
When a domain or dataset specification includes a codelist for a variable, not every value in that codelist may have been part of planned data collection; only values that were part of planned data collection should be included in the
Define-XML document. For example, --PRESP variables are associated with the NY codelist, but only the value
"Y" is allowed in --PRESP variables. Future versions of the Define-XML specification are expected to include information on representing subsets of controlled terminology.

#### 4.3.4 Use of Controlled Terminology and Arbitrary Number Codes

Controlled terminology or human-readable text should be used instead of arbitrary number codes in order to reduce ambiguity for submission reviewers. For example, CMDECOD would contain human-readable dictionary text rather than a numeric code. Numeric code values may be submitted as Supplemental Qualifiers if necessary.

#### 4.3.5 Storing Controlled Terminology for Synonym Qualifier Variables

- For events such as adverse events and medical history, populate --DECOD with the dictionary's preferred term and populate --BODSYS with the preferred body system name. If a dictionary is multi-axial, the value in --BODSYS should represent the system organ class (SOC) used for the sponsor's analysis and summary tables, which may not necessarily be the primary SOC. Populate --SOC with the dictionary-derived primary
SOC. In cases where the primary SOC was used for analysis, --BODSYS and --SOC are the same.
- If MedDRA is used to code events, the intermediate levels in the MedDRA hierarchy should also be represented in the dataset. A pair of variables has been defined for each of the levels of the hierarchy other than SOC and Preferred Term (PT): one to represent the text description and the other to represent the code value associated with it. For example, --LLT should be used to represent the Lowest Level Term text description and --LLTCD should be used to represent the Lowest Level Term code value.
- For concomitant medications, populate CMDECOD with the drug's generic name and populate CMCLAS with the drug class used for the sponsor's analysis and summary tables. If coding to multiple classes, follow
Section 4.2.8.1, Multiple Values for an Intervention or Event Topic Variable, or omit CMCLAS.
- For concomitant medications, supplemental qualifiers may be used to represent additional coding dictionary information (e.g., a drug's ATC codes from the WHO Drug Dictionary; see Section 8.4, Relating
Non-standard Variable Values to a Parent Domain).
The sponsor is expected to provide the dictionary name and version used to map the terms by utilizing the Define-
XML external codelist attributes.

#### 4.3.6 Storing Topic Variables for General Domain Models

The topic variable for the Interventions and Events general observation-class models is often stored as verbatim text.
For an Events domain, the topic variable is --TERM. For an Interventions domain, the topic variable is --TRT. For a
Findings domain, the topic variable --TESTCD should use controlled terminology (e.g., "SYSBP" for systolic blood pressure). If CDISC Controlled Terminology exists, it should be used; otherwise, sponsors should define their own controlled list of terms. If the verbatim topic variable in an Interventions or Event domain is modified to facilitate coding, the modified text is stored in --MODIFY. In most cases—other than Physical Examination (PE)—the

dictionary-coded text is derived into --DECOD. Because the PEORRES variable is modified instead of the topic variable for PE, the dictionary-derived text would be placed in PESTRESC. The variables used in each of the defined domains are:
| Domain | Original Verbatim | Modified Verbatim | Standardized Value |
|---|---|---|---|
| AE | AETERM | AEMODIFY | AEDECOD |
| DS | DSTERM | | DSDECOD |
| CM | CMTRT | CMMODIFY | CMDECOD |
| MH | MHTERM | MHMODIFY | MHDECOD |
| PE | PEORRES | PEMODIFY | PESTRESC |

#### 4.3.7 Use of "Yes" and "No" Values

Variables where the response is "Yes" or "No" ("Y" or "N") should normally be populated for both "Y" and "N" responses. This eliminates confusion regarding whether a blank response indicates "N" or is a missing value.
However, some variables are collected or derived in a manner that allows only 1 response, such as when a single checkbox indicates "Yes". In situations such as these, where it is unambiguous to populate only the response of interest, it is permissible to populate only 1 value ("Y" or "N") and leave the alternate value blank. An example of when it would be acceptable to use only a value of "Y" would be for Last Observation Before Exposure Flag (--
LOBXFL) variables, where "N" is not necessary to indicate that a value is not the last observation before exposure.
Note: Permissible values for variables with controlled terms of "Y" or "N" may be extended to include "U" or
"NA" if it is the sponsor's practice to explicitly collect or derive values indicating "Unknown" or "Not Applicable" for that variable.

### 4.4 Actual and Relative Time Assumptions

Timing variables (SDTM Section 3.1.5, Timing Variables for All Classes) are an essential component of all SDTM subject-level domain datasets. In general, all domains based on the 3 general observation classes should have at least
1 timing variable. In the Events or Interventions general observation class, this could be the start date of the event or intervention. In the Findings observation class, where data are usually collected at multiple visits, at least 1 timing variable must be used.
The SDTMIG requires dates and times of day to be stored according to the international standard ISO 8601 (http://www.iso.org). ISO 8601 provides a text-based representation of dates and/or times, intervals of time, and durations of time.

#### 4.4.1 Formats for Date/Time Variables

An SDTM DTC variable may include data that is represented in ISO 8601 format as a complete date/time, a partial date/time, or an incomplete date/time.
The SDTMIG template uses ISO 8601 for calendar dates and times of day, which are expressed as follows:
`YYYY-MM-DDThh:mm:ss(.n+)?(((+|-)hh:mm)|Z)?`

where:
- `[YYYY]` = four-digit year
- `[MM]` = two-digit representation of the month (01-12, 01=January, etc.)
- `[DD]` = two-digit day of the month (01 through 31)
- `[T]` = (time designator) indicates time information follows
- `[hh]` = two digits of hour (00 through 23) (am/pm is NOT allowed)
- `[mm]` = two digits of minute (00 through 59)
- `[ss]` = two digits of second (00 through 59)
The last two components, indicated in the format pattern with a question mark, are optional:

- [(.n+)?] = optional fractions of seconds
- [(((+|-)hh:mm)|Z)?] = optional time zone
Other characters defined for use within the ISO 8601 standard are:
- [-] (hyphen): to separate the time elements "year" from "month" and "month" from "day" and to represent missing date components.
- [:] (colon): to separate the time elements "hour" from "minute" and "minute" from "second"
- [/] (solidus): to separate components in the representation of date/time intervals
- [P] (duration designator): precedes the components that represent the duration
Spaces are not allowed in any ISO 8601 representations.
Key aspects of the ISO 8601 standard are as follows:
- ISO 8601 represents dates as a text string using the notation YYYY-MM-DD.
- ISO 8601 represents times as a text string using the notation hh:mm:ss(.n+)?(((+|-)hh:mm)|Z)?.
- The SDTM and the SDTMIG require use of the ISO 8601 extended format, which requires hyphen delimiters for date components and colon delimiters for time components. The ISO 8601 basic format, which does not require delimiters, should not be used in SDTM datasets.
- When a date is stored with a time in the same variable (as a date/time), the date is written in front of the time and the time is preceded with "T" using the notation YYYY-MM-DDThh:mm:ss (e.g. 2001-12-
26T00:00:01).
Implementation of the ISO 8601 standard means that date/time variables are character/text data types. The SDTM fragment employed for date/time character variables is DTC.

#### 4.4.2 Date/Time Precision

The concept of representing date/time precision is handled through use of the ISO 8601 standard. According to ISO
8601, precision (also referred to by ISO 8601 as "completeness" or "representations with reduced accuracy") can be inferred from the presence or absence of components in the date and/or time values. Missing components are represented by right truncation or a hyphen (for intermediate components that are missing). If the date and time values are completely missing, the SDTM date field should be null. Every component except year is represented as 2 digits. Years are represented as 4 digits; for all other components, 1-digit numbers are always padded with a leading zero.
The following table provides examples of ISO 8601 representations of complete and truncated date/time values using ISO 8601 "appropriate right truncations" of incomplete date/time representations. Note that if no time component is represented, the [T] time designator (in addition to the missing time) must be omitted in ISO 8601 representation.

| # | Date and Time as Originally Recorded | Precision | ISO 8601 Date/Time |
|---|---|---|---|
| 1 | December 15, 2003 13:14:17.123 | Date/time, including fractional seconds | 2003-12-15T13:14:17.123 |
| 2 | December 15, 2003 13:14:17 | Date/time to the nearest second | 2003-12-15T13:14:17 |
| 3 | December 15, 2003 13:14 | Unknown seconds | 2003-12-15T13:14 |
| 4 | December 15, 2003 13 | Unknown minutes and seconds | 2003-12-15T13 |
| 5 | December 15, 2003 | Unknown time | 2003-12-15 |
| 6 | December, 2003 | Unknown day and time | 2003-12 |
| 7 | 2003 | Unknown month, day, and time | 2003 |

This date and date/time model also provides for imprecise or estimated dates, such as those commonly seen in Medical History. To represent these intervals while applying the ISO 8601 standard, it is recommended that the sponsor concatenate the date/time values (using the most complete representation of the date/time known) that describe the beginning and the end of the interval of uncertainty and separate them with a solidus, as shown in the following table.

| # | Interval of Uncertainty | ISO 8601 Date/Time |
|---|---|---|
| 1 | Between 10:00 and 10:30 on the morning of December 15, 2003 | 2003-12-15T10:00/2003-12-15T10:30 |
| 2 | Between the first of this year (2003) until "now" (February 15, 2003) | 2003-01-01/2003-02-15 |
| 3 | Between the first and the tenth of December, 2003 | 2003-12-01/2003-12-10 |
| 4 | Sometime in the first half of 2003 | 2003-01-01/2003-06-30 |

Other uncertainty intervals may be represented by the omission of components of the date when these components are unknown or missing. As previously mentioned, ISO 8601 represents missing intermediate components through the use of a hyphen where the missing component would normally be represented. This may be used in addition to "appropriate right truncations" for incomplete date/time representations. When components are omitted, the expected delimiters must still be kept in place and only a single hyphen is to be used to indicate an omitted component. Examples of this method of omitted component representation are shown in the following table.

| # | Date and Time as Originally Recorded | Level of Uncertainty | ISO 8601 Date/Time |
|---|---|---|---|
| 1 | December 15, 2003 13:15:17 | Date/time to the nearest second | 2003-12-15T13:15:17 |
| 2 | December 15, 2003 ??:15 | Unknown hour with known minutes | 2003-12-15T-:15 |
| 3 | December 15, 2003 13:??:17 | Unknown minutes with known date, hours, and seconds | 2003-12-15T13:-:17 |
| 4 | The 15th of some month in 2003, time not collected | Unknown month and time with known year and day | 2003---15 |
| 5 | December 15, but can't remember the year, time not collected | Unknown year with known month and day | --12-15 |
| 6 | 7:15 of some unknown date | Unknown date with known hour and minute | -----T07:15 |

Note that row 6, where a time is reported with no date information, represents a very unusual situation. Because most data are collected as part of a visit, when only a time appears on a CRF, it is expected that the date of the visit would usually be used as the date of collection.
Using a character-based data type to implement the ISO 8601 date/time standard will ensure that the date/time information will be machine- and human-readable without the need for further manipulation, and will be platform- and software-independent.

#### 4.4.3 Intervals of Time and Use of Duration for --DUR Variables

##### 4.4.3.1 Intervals of Time and Use of Duration

As defined by ISO 8601, an interval of time is the part of a time axis, limited by 2 time "instants" such as the times represented in SDTM by the variables --STDTC and --ENDTC. These variables represent the 2 instants that bound an interval of time; the duration is the quantity of time that is equal to the difference between these time points.

ISO 8601 allows an interval to be represented in multiple ways. One representation, shown below, uses 2 dates in the format:

`YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss`

Although this example represents the interval (by providing the start date/time and end date/time to bound the interval of time), it does not provide the value of the duration (the quantity of time).
Duration is frequently used during a review; however, the duration timing variable (--DUR) should generally be used in a domain if it was collected in lieu of a start date/time (--STDTC) and end date/time (--ENDTC). If both --STDTC and --ENDTC are collected, durations can be calculated by the difference in these 2 values, and need not be in the submission dataset.

Both duration and duration units can be provided in the single --DUR variable, in accordance with the ISO 8601 standard. The values provided in --DUR should follow 1 of the following ISO 8601 duration formats:

```
PnYnMnDTnHnMnS
- or -
PnW
```

where the letter designation is defined as:
- `[P]` (duration designator): precedes the alphanumeric text string that represents the duration. Note that the use of the character "P" is based on the historical use of the term "period" for duration.
- `[n]` represents a positive number or zero.
- `[W]` is used as week designator, preceding a data element that represents the number of calendar weeks within the calendar year (e.g., P6W represents 6 weeks of calendar time).

The letter "P" must precede other values in the ISO 8601 representation of duration. The "n" preceding each letter represents the number of years, months, days, hours, minutes, seconds, or the number of weeks. As with the date/time format, "T" is used to separate the date components from time components.

Note that weeks cannot be mixed with any other date/time components such as days or months in duration expressions.

As is the case with the date/time representation in --DTC, --STDTC, or --ENDTC, only the components of duration that are known or collected need to be represented. As is the case with the date/time representation, if no time component is represented, the [T] time designator (in addition to the missing time) must be omitted in ISO 8601 representation.

ISO 8601 also allows that the "lowest-order components" of duration being represented may be represented in decimal format. This may be useful if data are collected in formats such as "one and one-half years", "two and a half weeks", "half a week" or "quarter of an hour" and the sponsor wishes to represent this "precision" (or lack of precision) in ISO 8601 representation. This is ONLY allowed in the lowest-order (right-most) component in any duration representation.

The following table provides some examples of ISO 8601-compliant representations of durations.
| Duration as Originally Recorded | ISO 8601 Duration |
|---|---|
| 2 years | P2Y |
| 10 weeks | P10W |
| 3 months 14 days | P3M14D |
| 3 days | P3D |
| 6 months 17 days 3 hours | P6M17DT3H |
| 14 days 7 hours 57 minutes | P14DT7H57M |
| 42 minutes 18 seconds | PT42M18S |
| One-half hour | PT0.5H |
| 5 days 12¼ hours | P5DT12.25H |
| 4 ½ weeks | P4.5W |

Note that a leading zero is required with decimal values less than 1.

##### 4.4.3.2 Interval with Uncertainty

When an interval of time is an amount of time (duration) following an event whose start date/time is recorded (with some level of precision, e.g., when one knows the start date/time and the duration following the start date/time), the correct ISO 8601 usage to represent this interval is:
`YYYY-MM-DDThh:mm:ss/PnYnMnDTnHnMnS`

where the start date/time is represented before the solidus or foreword slash [/], the "Pn…" following the solidus represents a "duration," and the entire representation is known as an "interval." Note that this is the recommended representation of elapsed time, given a start date/time and the duration elapsed.
When an interval of time is an amount of time (duration) measured prior to an event whose start date/time is recorded (with some level of precision, e.g., where one knows the end date/time and the duration preceding that end date/time), the syntax is:
`PnYnMnDTnHnMnS/YYYY-MM-DDThh:mm:ss`

where the duration, "Pn…", is represented before the solidus [/], the end date/time is represented following the solidus, and the entire representation is known as an "interval."

#### 4.4.4 Use of the Study Day Variables

The permissible study day variables (i.e., --DY, --STDY, --ENDY) describe the relative day of the observation starting with the reference date as day 1. They are determined by comparing the date portion of the respective date/time variables (--DTC, --STDTC, and --ENDTC) to the date portion of the subject reference start date (RFSTDTC from the Demographics domain).

The subject reference start date (RFSTDTC) is designated as study day 1. The study day value is incremented by 1 for each date following RFSTDTC. Dates prior to RFSTDTC are decreased by 1, with the date preceding RFSTDTC designated as study day -1 (there is no study day 0). This algorithm for determining Study Day is consistent with how people typically describe sequential days relative to a fixed reference point, but creates problems if used for mathematical calculations because it does not allow for a day 0. As such, Study Day is not suited for use in subsequent numerical computations, such as calculating duration. The raw date values should be used rather than Study Day in those calculations.
All study day values are integers. Thus, to calculate Study Day:

- `--DY = (date portion of --DTC) - (date portion of RFSTDTC) + 1` if --DTC is on or after RFSTDTC
- `--DY = (date portion of --DTC) - (date portion of RFSTDTC)` if --DTC precedes RFSTDTC

This method should be used across all domains.

#### 4.4.5 Clinical Encounters and Visits

All domains based on the 3 general observation classes should have at least 1 timing variable. For domains in the Events or Interventions observation classes, and for domains in the Findings observation class, for which data are collected only once during the study, the most appropriate timing variable may be a date (e.g., --DTC, --STDTC) or some other timing variable. For studies that are designed with a prospectively defined schedule of visit-based activities, domains for data that are to be collected more than once per subject (e.g., labs, ECG, vital signs) are expected to include VISITNUM as a timing variable.

Clinical encounters are described by the CDISC visit variables. For planned visits, values of VISIT, VISITNUM, and VISITDY must be those defined in the Trial Visits (TV) dataset (see Section 7.3.1, Trial Visits). For planned visits:

- Values of VISITNUM are used for sorting and should, wherever possible, match the planned chronological order of visits. Occasionally, a protocol will define a planned visit whose timing is unpredictable (e.g., planned in response to an adverse event, a threshold test value, or a disease event), and completely chronological values of VISITNUM may not be possible in such cases.
- There should be a one-to-one relationship between values of VISIT and VISITNUM.
- For visits that may last more than 1 calendar day, VISITDY should be the planned day of the start of the visit.

Sponsor practices for populating visit variables for unplanned visits may vary.

- VISITNUM should generally be populated, even for unplanned visits, as it is expected in many Findings domains, as described above. The easiest method of populating VISITNUM for unplanned visits is to assign the same value (e.g., 99) to all unplanned visits, although this method provides no differentiation between the unplanned visits and does not provide chronological sorting. Methods that provide a one-to-one relationship between visits and values of VISITNUM, that are consistent across domains, and that assign VISITNUM values that sort chronologically require more work and must be applied after all of a subject's unplanned visits are known.
- VISIT may be left null or may be populated with a generic value (e.g., "Unscheduled") for all unplanned visits, or individual values may be assigned to different unplanned visits.
- VISITDY must not be populated for unplanned visits; VISITDY is, by definition, the planned study day of visit. The actual study day of an unplanned visit belongs in a --DY variable.

The following lb.xpt sample rows show how visit identifiers might be used for lab data.

lb.xpt

| USUBJID | VISIT | VISITNUM | VISITDY | LBDY |
|---|---|---|---|---|
| 001 | Week 1 | 2 | 7 | 7 |
| 001 | Week 2 | 3 | 14 | 13 |
| 001 | Week 2 Unscheduled | 3.1 | | 17 |

#### 4.4.6 Representing Additional Study Days

The SDTM allows for the representation of study days relative to the RFSTDTC reference start date variable in the DM dataset, using variables --DY, as described in Section 4.4.4, Use of the "Study Day" Variables. The calculation of additional study days within subdivisions of time in a clinical trial may be based on 1 or more sponsor-defined reference dates not represented by RFSTDTC. In such cases, the sponsor may define supplemental qualifier variables and the Define-XML document should reflect the reference dates used to calculate such study days. If the sponsor wishes to define "day within element" or "day within epoch", the reference date/time will be an element start date/time in the Subject Elements (SE) dataset (see Section 5.3, Subject Elements).

#### 4.4.7 Use of Relative Timing Variables

**--STRF and --ENRF**

The variables --STRF and --ENRF represent the timing of an observation relative to the sponsor-defined study reference period, when information such as "BEFORE", "PRIOR", "ONGOING"', or "CONTINUING" is collected in lieu of a date and this collected information is in relation to the sponsor-defined study reference period. The sponsor-defined study reference period is the continuous period of time defined by the discrete starting point, RFSTDTC, and the discrete ending point, RFENDTC, for each subject in the Demographics (DM) dataset.

--STRF is used to identify the start of an observation relative to the sponsor-defined study reference period.

--ENRF is used to identify the end of an observation relative to the sponsor-defined study reference period.

Allowable values for --STRF are "BEFORE", "DURING", "DURING/AFTER", "AFTER", and "UNKNOWN". Although "COINCIDENT" and "ONGOING" are in the STENRF codelist, they describe timing relative to a point in time rather than an interval of time, so are not appropriate for use with --STRF variables. It would be unusual for an event or intervention to be recorded as starting "AFTER" the study reference period, but could be possible, depending on how the study reference period is defined in a particular study.

Allowable values for --ENRF are "BEFORE", "DURING", "DURING/AFTER", "AFTER" and "UNKNOWN". If --ENRF is used, then --ENRF = "AFTER" means that the event did not end before or during the study reference period. Although "COINCIDENT" and "ONGOING" are in the STENRF codelist, they describe timing relative to a point in time rather than an interval of time, so are not appropriate for use with --ENRF variables.

As an example, a CRF checkbox that identifies concomitant medication use that began prior to the study reference period would translate into CMSTRF = "BEFORE", if selected. Note that in this example, the information collected is with respect to the start of the concomitant medication use only, and therefore the collected data corresponds to variable CMSTRF, not CMENRF. Note also that the information collected is relative to the study reference period, which meets the definition of CMSTRF.

Some sponsors may wish to derive --STRF and --ENRF for analysis or reporting purposes even when dates are collected. Sponsors are cautioned that doing so in conjunction with directly collecting or mapping data such as "BEFORE", "PRIOR", and "ONGOING" to --STRF and --ENRF will blur the distinction between collected and derived values within the domain. Sponsors wishing to do such derivations are instead encouraged to use analysis datasets for this derived data.

In general, sponsors are cautioned that representing information using variables --STRF and --ENRF may not be as precise as other methods, particularly because information is often collected relative to a point in time or to a period of time other than the one defined as the study reference period. SDTMIG v3.1.2 attempted to address these limitations by the addition of 4 new relative timing variables, which are described in the following section. Sponsors should use the set of variables that allows for accurate representation of collected data. In many cases, this will mean using these new relative timing variables in place of --STRF and --ENRF.
**--STRTPT, --STTPT, --ENRTPT, and --ENTPT**

Although the variables --STRF and --ENRF are useful in the case when relative timing assessments are made coincident with the start and end of the study reference period, they may not be suitable for expressing relative timing assessments (e.g., "Prior", "Ongoing") that are collected at other times of the study. As a result, 4 new timing variables were added in SDTMIG v3.1.2 to express a similar concept at any point in time. The variables --STRTPT and --ENRTPT contain values similar to --STRF and --ENRF, but may be anchored with any timing description or date/time value expressed in the respective --STTPT and --ENTPT variables, and are not limited to the study reference period. Unlike the variables --STRF and --ENRF, which for all domains are defined relative to one study reference period, the timing variables --STRTPT, --STTPT, --ENRTPT, and --ENTPT are defined by each sponsor for each study. Allowable values for --STRTPT and --ENRTPT are as follows.

If the reference time point corresponds to the date of collection or assessment:
- Start values: An observation can start BEFORE that time point, can start COINCIDENT with that time point, or it can be UNKNOWN when it started.
- End values: An observation can end BEFORE that time point, can end COINCIDENT with that time point, can be known that it did not end but was ONGOING, or it can be UNKNOWN when it ended or if it was ongoing.
- AFTER is not a valid value in this case because it would represent an event after the date of collection.
If the reference time point is prior to the date of collection or assessment:
- Start values: An observation can start BEFORE the reference point, can start COINCIDENT with the reference point, can start AFTER the reference point, or it can be UNKNOWN when it started.
- End values: An observation can end BEFORE the reference point, can end COINCIDENT with the reference point, can end AFTER the reference point, can be known that it did not end but was ONGOING, or it can be UNKNOWN when it ended or if it was ongoing.
Although "DURING" and "DURING/AFTER" are in the STENRF codelist, they describe timing relative to an interval of time rather than a point in time, so are not allowable for use with --STRTPT and --ENRTPT variables.

**Examples of --STRTPT, --STTPT, --ENRTPT, and --ENTPT**

**Example 1: Medical History**

Assumptions:
- CRF contains "Year Started" and checkbox for "Active"
- "Date of Assessment" is collected

Example when "Active" is checked:
- MHDTC = date of assessment value (e.g., "2006-11-02")
- MHSTDTC = year of condition start (e.g., "2002")
- MHENRTPT = "ONGOING"
- MHENTPT = date of assessment value (e.g., "2006-11-02")

*Figure 4.4.7-1: Example of --ENRTPT and --ENTPT for Medical History*

**Example 2: Prior and Concomitant Medications**

Assumptions:
- CRF includes collection of "Start Date" and "Stop Date", and checkboxes for
  - "Prior" if start date was before the screening visit and was unknown or uncollected
  - "Continuing" if medication had not stopped as of the final study visit, so no end date was collected

Example when both "Prior" and "Continuing" are checked:
- CMSTDTC is null
- CMENDTC is null
- CMSTRTPT = "BEFORE"
- CMSTTPT is screening date (e.g., "2006-10-21")
- CMENRTPT = "ONGOING"
- CMENTPT is final study visit date (e.g., "2006-11-02")

**Example 3: Adverse Events**

Assumptions:
- CRF contains "Start Date", "Stop Date"
- Collection of "Outcome" includes checkboxes for "Continuing" and "Unknown", to be used, if necessary, at the end of the subject's participation in the trial
- No assessment date or visit information was collected

Example when "Unknown" is checked:
- AESTDTC is start date (e.g., "2006-10-01")
- AEENDTC is null
- AEENRTPT = "UNKNOWN"
- AEENTPT is final subject contact date (e.g., "2006-11-02")

#### 4.4.8 Date and Time Reported in a Domain Based on Findings

When the date/time of collection is reported in any domain, the date/time should go into the --DTC field (e.g., EGDTC for Date/Time of ECG). For any domain based on the Findings general observation class (e.g., lab tests based on a specimen), the collection date is likely to be tied to when the source of the finding was captured, not necessarily when the data were recorded. In order to ensure that the critical timing information is always represented in the same variable, the --DTC variable is used to represent the time of specimen collection. For example, in the Laboratory Test Results (LB) domain, the LBDTC variable would be used for all single-point blood collections or spot urine collections. For timed lab collections (e.g., 24-hour urine collections) the LBDTC variable would be used for the start date/time of the collection and LBENDTC for the end date/time of the collection. This approach allows the single-point and interval collections to use the same date/time variables consistently across all datasets for the Findings general observation class. The following table illustrates the proper use of these variables. Note that --STDTC should not be used in the Findings general observation class and is therefore blank in this table.
| Collection Type | --DTC | --STDTC | --ENDTC |
|---|---|---|---|
| Single-point Collection | X | | |
| Interval Collection | X | | X |

#### 4.4.9 Use of Dates as Result Variables

Dates are generally used only as timing variables to describe the timing of an event, intervention, or collection activity, but there may be occasions when it may be preferable to model a date as a result (--ORRES) in a Findings dataset. Note that using a date as a result to a Findings question is unusual and atypical, and should be approached with caution. This situation, however, may occasionally occur when (1) a group of questions (each of which has a date response) is asked and analyzed together; or (2) the event(s) and intervention(s) in question are not medically significant (e.g., when included in questionnaires). Consider the following cases:

- Calculated due date
- Date of last day on the job
- Date of high school graduation

One approach to modeling these data would be to place the text of the question in --TEST and the response to the question (a date represented in ISO 8601 format) in --ORRES and --STRESC, as long as these date results do not contain the dates of medically significant events or interventions.

Again, use extreme caution when storing dates as the results of findings. Remember, in most cases, these dates should be timing variables associated with a record in an Intervention or Events dataset.
#### 4.4.10 Representing Time Points

Time points can be represented using the time point variables --TPT, --TPTNUM, --ELTM, and the time-point anchors --TPTREF (text description) and --RFTDTC (the date/time). Note that time-point data will usually have an associated --DTC value. The interrelationship of these variables is shown in the following figure.

*Figure 4.4.10-1: Representing Time Points*

Values for these variables for vital signs measurements taken at 30, 60, and 90 minutes after dosing would look like the following.

| VSTPTNUM | VSTPT | VSELTM | VSTPTREF | VSRFTDTC | VSDTC |
| --- | --- | --- | --- | --- | --- |
| 1 | 30 MIN | PT30M | DOSE ADMINISTRATION | 2006-08-01T08:00 | 2006-08-01T08:30 |
| 2 | 60 MIN | PT1H | DOSE ADMINISTRATION | 2006-08-01T08:00 | 2006-08-01T09:01 |
| 3 | 90 MIN | PT1H30M | DOSE ADMINISTRATION | 2006-08-01T08:00 | 2006-08-01T09:32 |

Note that VSELTM is the planned elapsed time, not the actual elapsed time. The actual elapsed time could be derived in an analysis dataset, if desired, as VSDTC-VSRFTDTC.

Values for these variables for urine collections taken pre-dose, and from 0-12 hours and 12-24 hours after dosing would look like the following.

| LBTPTNUM | LBTPT | LBELTM | LBTPTREF | LBRFTDTC | LBDTC |
|---|---|---|---|---|---|
| 1 | 15 MIN PRE-DOSE | -PT15M | DOSE ADMINISTRATION | 2006-08-01T08:00 | 2006-08-01T07:45 |
| 2 | 0-12 HOURS | PT12H | DOSE ADMINISTRATION | 2006-08-01T08:00 | 2006-08-01T20:35 |
| 3 | 12-24 HOURS | PT24H | DOSE ADMINISTRATION | 2006-08-01T08:00 | 2006-08-02T08:40 |

Note that the value in LBELTM represents the end of the specimen collection interval.

When time points are represented in SDTMIG domains, both --TPT and --TPTNUM must be used. Time points may or may not have an associated --TPTREF. Sometimes, --TPTNUM may be used as a key for multiple values collected for the same test within a visit; as such, there is no dependence upon an anchor such as --TPTREF, but there will be a dependency upon VISITNUM. In such cases, VISITNUM will be required to confer uniqueness to values of --TPTNUM.

If the protocol describes the scheduling of a dose using a reference intervention or assessment, then --TPTREF should be populated, even if it does not contribute to uniqueness. The fact that time points are related to a reference time point, and what that reference time point is, are important for interpreting the data collected at the time point.

Not all time points will require all 3 variables to provide uniqueness. In fact, in some cases a time point may be uniquely identified without the use of VISIT, or without the use of --TPTREF, or without the use of either. For instance:
- A trial might have time points only within 1 visit, so that the contribution of VISITNUM to uniqueness is trivial. (VISITNUM would be populated, but would not contribute to uniqueness.)
- A trial might have time points that do not relate to any visit, such as time points relative to a dose of drug self-administered by the subject at home. (Visit variables would not be included, but --TPTREF and other time point variables would be populated.)
- A trial may have only 1 reference time point per visit, and all reference time points may be similar, so that only 1 value of --TPTREF (e.g., "DOSE") is needed. (--TPTREF would be populated, but would not contribute to uniqueness.)
- A trial may have time points not related to a reference time point. For instance, --TPTNUM values could be used to distinguish first, second, and third repeats of a measurement scheduled without any relationship to dosing (–TPTREF and --ELTM would not be included.) In this case, where the protocol calls for repeated measurements but does not specify timing of the measurements, the --REPNUM variable could be used instead of time-point variables.
For trials with many time points, the requirement to provide uniqueness using only VISITNUM, --TPTREF, and --TPTNUM may lead to a scheme where multiple natural keys are combined into the values of one of these variables. For instance, in a crossover trial with multiple doses on multiple days within each period, either of the following options could be used.

1. VISITNUM might be used to designate period, --TPTREF might be used to designate the day and the dose, and --TPTNUM might be used to designate the timing relative to the reference time point.
2. VISITNUM might be used to designate period and day within period, --TPTREF might be used to designate the dose within the day, and --TPTNUM might be used to designate the timing relative to the reference time point.
**Option 1**

| VISIT | VISITNUM | --TPT | --TPTNUM | --TPTREF |
|---|---|---|---|---|
| PERIOD 1 | 3 | PRE-DOSE | 1 | DAY 1, AM DOSE |
| | | 1H | 2 | |
| | | 4H | 3 | |
| | | PRE-DOSE | 1 | DAY 1, PM DOSE |
| | | 1H | 2 | |
| | | 4H | 3 | |
| | | PRE-DOSE | 1 | DAY 5, AM DOSE |
| | | 1H | 2 | |
| | | 4H | 3 | |
| | | PRE-DOSE | 1 | DAY 5, PM DOSE |
| | | 1H | 2 | |
| | | 4H | 3 | |
| PERIOD 2 | 4 | PRE-DOSE | 1 | DAY 1, AM DOSE |
| | | 1H | 2 | |
| | | 4H | 3 | |
| | | PRE-DOSE | 1 | DAY 1, PM DOSE |
| | | 1H | 2 | |
| | | 4H | 3 | |

**Option 2**

| VISIT | VISITNUM | --TPT | --TPTNUM | --TPTREF |
|---|---|---|---|---|
| PERIOD 1, DAY 1 | 3 | PRE-DOSE | 1 | AM DOSE |
| | | 1H | 2 | |
| | | 4H | 3 | |
| | | PRE-DOSE | 1 | PM DOSE |
| | | 1H | 2 | |
| | | 4H | 3 | |
| PERIOD 1, DAY 5 | 4 | PRE-DOSE | 1 | AM DOSE |
| | | 1H | 2 | |
| | | 4H | 3 | |
| | | PRE-DOSE | 1 | PM DOSE |
| | | 1H | 2 | |
| | | 4H | 3 | |
| PERIOD 2, DAY 1 | 5 | PRE-DOSE | 1 | AM DOSE |
| | | 1H | 2 | |
| | | 4H | 3 | |
| | | PRE-DOSE | 1 | PM DOSE |
| | | 1H | 2 | |
| | | 4H | 3 | |

Within the context that defines uniqueness for a time point (which may include domain, visit, and reference time point), there must be a one-to-one relationship between values of --TPT and --TPTNUM. In other words, if domain, visit, and reference time point uniquely identify subject data, then if 2 subjects have records with the same values of DOMAIN, VISITNUM, --TPTREF, and --TPTNUM, these records may not have different time point descriptions in --TPT.

Within the context that defines uniqueness for a time point, there is likely to be a one-to-one relationship between most values of --TPT and --ELTM. However, because --ELTM can only be populated with ISO 8601 periods of time (as described in Section 4.4.3, Intervals of Time and Use of Duration for --DUR Variables), --ELTM may not be populated for all time points. For example, --ELTM is likely to be null for time points described by text such as "pre-dose" or "before breakfast." When --ELTM is populated, if 2 subjects have records with the same values of DOMAIN, VISITNUM, --TPTREF, and --TPTNUM, then these records may not have different values in --ELTM.

When the protocol describes a time point with text (e.g., "4-6 hours after dose," "12 hours +/- 2 hours after dose"), the sponsor may choose whether and how to populate --ELTM. For example, a time point described as "4-6 hours after dose" might be associated with an --ELTM value of PT4H. A time point described as "12 hours +/- 2 hours after dose" might be associated with an --ELTM value of PT12H. Conventions for populating --ELTM should be consistent (the examples just given would probably not both be used in the same trial). It would be good practice to indicate the range of intended timings by some convention in the values used to populate --TPT.

Sponsors may, of course, use more stringent requirements for populating --TPTNUM, --TPT, and --ELTM. For instance, a sponsor could decide that all time points with a particular --ELTM value would have the same values of --TPTNUM, and --TPT, across all visits, reference time points, and domains.

#### 4.4.11 Disease Milestones and Disease Milestone Timing Variables

A disease milestone is an event or activity that can be anticipated in the course of a disease, but whose timing is not controlled by the study schedule. A disease milestone may be something that occurred pre-study, but which represents a time at which data would have been collected (e.g., diagnosis of the disease under study). A disease milestone may also be something which is anticipated to occur during a study and which, if it occurs, triggers the collection of related data outside the regular schedule of visits (e.g., adverse event of interest). The types of disease milestones for a study are defined in the study-level Trial Disease Milestones (TM) dataset (see Section 7.3.3, Trial Disease Milestones). The times at which disease milestones occurred for a particular subject are summarized in the special-purpose Subject Disease Milestones (SM) domain (see Section 5.4, Subject Disease Milestones), a domain similar in structure to the Subject Visits (SV) and Subject Elements (SE) domains.

Not all studies will have disease milestones. If a study does not have disease milestones, the TM and SM domains will not be present and the disease milestones timing variables may not be included in other domains.

**Disease Milestone Naming**

Instances of disease milestones are given names at a subject level. The name of a disease milestone is composed of a character string that depends on the disease milestone type (MIDSTYPE in TM and SM) and, if the type of disease milestone is one that may occur multiple times, a chronological sequence number for this disease milestone among other instances of the same type for the subject. The character string used in the name of a disease milestone is usually a short form of the disease milestone type. For example, if the type of disease milestone is "EPISODE OF DISEASE UNDER STUDY", the values of MIDS for instances of this type of event could include "EPISODE1", "EPISODE2"; or "EPISODE01", "EPISODE02", and so on. The association between the longer text in MIDSTYPE and the shorter text in MIDS can be seen in SM, which includes both variables.

**Disease Milestone Name (MIDS)**

If something that has been defined as a disease milestone for a particular study occurs for a particular subject, it is represented as usual: in the appropriate findings, intervention, or events class record. In addition, this record will include the MIDS timing variable, populated with the name of the disease milestone. The timing of a disease milestone is also represented in the special-purpose SM domain.
The record that represents a disease milestone does not include values for the timing variables RELMIDS and
MIDSDTC, which are used to represent the timing of other observations relative to a disease milestone. The usual timing variables in the record for a disease milestone (e.g., --DTC, --STDTC, --ENDTC) provide the needed timing for this observation and for the timing information represented in the SM domain.
**Timing Relative to a Disease Milestone (MIDS, RELMIDS, MIDSDTC)**

For an observation triggered by the occurrence of a disease milestone, the relationship of the observation to the disease milestone can be represented using the disease milestones timing variables MIDS, RELMIDS, and MIDSDTC to describe the timing of the observation.
- MIDS is populated with the name of a disease milestone for this subject. MIDS is the “anchor” for describing the timing of the observation relative to the disease milestone. In this sense, its function is similar to --TPTREF for time points.
- RELMIDS is usually populated with a textual description of the temporal relationship between the observation and the disease milestone named in MIDS. Controlled Terminology has not yet been developed for RELMIDS, but is likely to include terms such as "IMMEDIATELY BEFORE", "AT START OF",
"DURING", "AT END OF", and "SHORTLY AFTER". It is similar to --ELTM, except that --ELTM is represented ISO 8601 duration.
- MIDSDTC is populated with the date/time of the disease milestone. This is the --DTC for a finding, or the --STDTC for an event or intervention, and is the date recorded in SMSTDTC in the SM domain. Its function is similar to --RFTDTC for time points.

In some cases, data collected in conjunction with a disease milestone do not include the collection of a separate date for the related observation. This is particularly common for pre-study disease milestones, but may occur with on- study disease milestones as well. In such cases, MIDSDTC provides a related date/time in records that would not otherwise contain any date. In records that do contain date/time(s) of the observation, MIDSDTC allows easy comparison of the date(s) of the observation to the (start) date of the disease milestone. In such cases, it functions much like the reference time point date/time (--RFTDTC) in observations at time points.
When a disease milestone is an event or intervention, some data triggered by the disease milestone may be modeled as findings about the disease milestone (i.e., FAOBJ is the disease milestone). In such cases, RELMIDS should be used to describe the temporal relationship between the disease milestone and the subject of the question being asked in the finding, rather than as describing when the question was asked.
- When the subject of the question is the disease milestone itself, RELMIDS may be populated with a value such as “ENTIRE EVENT” or “ENTIRE TREATMENT”.
- When the subject of the question is a question about the occurrence of some activity or event related to the disease milestone, RELMIDS acts like an evaluation interval, describing the period of time on which the question is focused.

  - For questions about a possible cause of an event or about the indication for a treatment, RELMIDS would have a value such as “WEEK PRIOR” or “IMMEDIATELY BEFORE”, or even just
“BEFORE”.
  - RELMIDS would be “DURING” for questions about things that may have occurred while an event or intervention disease milestone was in progress.
  - For sequelae of a disease milestone, RELMIDS would have a value such as “AT DISCHARGE” or “WEEK AFTER”, or simply “AFTER”.

**Use of Disease Milestone Timing Variables with Other Timing Variables**

The disease milestone timing variables provide timing relative to an activity or event that has been identified, for the particular study, as a disease milestone. Their use does not preclude the use of variables that collect actual date/times or timing relative to the study schedule.
- The use of actual date/times is unaffected. The disease milestone timing variables may provide timing information in cases where actual date/times are unavailable, particularly for pre-study disease milestones.
When the question text for an observation references a disease milestone but a separate date for the observation is not collected, the disease milestone timing variables should be populated but the actual date/s should not be imputed by populating them with the date of the disease milestone. Examples of such questions include disease stage at initial diagnosis of disease under study, or treatment for most recent disease episode.
- Study-day variables should be populated wherever complete actual date/times are populated. This includes negative study days for pre-study observations.
- The timing variables EPOCH and TAETORD (Planned Order of Element within Arm) may be populated for on-study observations associated with disease milestones. However, pre-study disease milestones— those which occur before the start of study participation when informed consent is obtained—by definition do not have an associated EPOCH or TAETORD.
- Visit variables are expected in many Findings domains, but findings triggered by the occurrence of a study milestone might not occur at a scheduled visit.
  - Findings associated with pre-study disease milestones are often collected at a screening visit, although the test was not performed at that visit.
  - For findings associated with on-study disease milestones but not conducted at a scheduled visit, practices for populating VISITNUM as for an unscheduled visit should be followed.
- The use of time-point variables with disease milestone variables may occur in cases where a disease milestone triggers treatment, and time points relative to treatment are part of the study schedule. For instance, a migraine trial may call for assessments of symptom severity at prescribed times after treatment of the migraine. If the migraine episodes were treated as disease milestones, then the disease milestone timing variables might be populated in the exposure and symptom-severity records. If the study planned to treat multiple migraine episodes, the MIDS variable would provide a convenient way to determine the episode with which data were associated.
  - An evaluation interval variable (--EVLINT or --EVINTX) can be used in conjunction with disease milestone variables. For instance, patient-reported outcome (PRO) instruments might be administered at the time of a disease milestone, and the questions in the instrument might include an evaluation interval.
- The timing variables for start and end of an event or intervention relative to the study reference period (--
STRF and --ENRF) or relative to a reference time point (--STRTPT and --STTPT, --ENRTPT and -- ENTPT) can be used in conjunction with disease milestone variables. For example, a concomitant medication could be collected in association with a disease milestone, so that the disease milestone timing variables were populated but relative timing variables used for the start or end of the concomitant medication.

- The timing variables for start and end of a planned assessment interval might be populated for an assessment triggered by a disease milestone, if applicable. For example, the occurrence of a particular event might trigger both a treatment and Holter monitoring for 24 hours after the treatment.
**Linking and Disease Milestones**

When disease milestones have been defined for a study, the MIDS variable serves to link observations associated with a disease milestone in a way similar to the way that VISITNUM links observations collected at a visit. If disease milestones were not defined for the study, it would be possible to link records associated with a disease milestone using RELREC, but the use of disease milestones has certain advantages:
- RELREC indicates that there is a relationship between records or datasets, but not the nature of the relationship. Records with the same MIDS value are related to the same disease milestone.
- When disease milestones are defined, it is not necessary to create RELREC records to establish relationships between observations associated with a disease milestone.

