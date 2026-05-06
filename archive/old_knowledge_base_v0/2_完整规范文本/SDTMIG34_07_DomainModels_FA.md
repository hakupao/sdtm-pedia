# SDTMIG v3.4 --- Domain Models: Findings About Events or Interventions (Section 6.4)

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials

---

## 6.4 Findings About Events or Interventions

Findings About Events or Interventions is a specialization of the Findings general observation class. As such, it shares all qualities and conventions of Findings observations but is specialized by the addition of the --OBJ variable.

### 6.4.1 When to Use Findings About Events or Interventions

The Findings About Events or Interventions structure (or "FA structure") is intended, as its name implies, to be used when collected data represent "findings about" an event or intervention that cannot be represented within an event or intervention record or as a supplemental qualifier to such a record. Not all findings associated with an event or intervention should be represented in the FA structure. The following are criteria for using the FA structure.

**Criterion 1:** Data or observations that have different timing from an associated event or intervention as a whole

Per Section 6.2.1, Adverse Events, assumption 7.e, "It is the sponsor's responsibility to define an event." One common practice is to define an event as the period of time during which an adverse event has a constant severity (or, sometimes, other properties). In this approach, a single medical condition may be represented by multiple AE records (see AE Example 4), each with a start and end date, and FA records are not needed for severity because each AE record covers a period of constant severity.

A finding which is a summary of multiple occurrences of a particular kind of event meets this criterion. For example, the number of episodes of vomiting during a particular time period is a finding about vomiting.

For events that have not ended at the time of an assessment, "event as a whole" means the event up to the time of the assessment. An event need not have ended for information about the event to be considered information about the event as a whole. Data about medical conditions collected before start of study treatment are usually about the event as a whole and are usually represented in Medical History (MH). See Section 6.4.4., Findings About Events or Interventions, Example 3.

Assessments of parts of events (snapshots or slices) are represented in FA and may or may not have parent records (e.g., FA Example 5). If the FA dataset is split by parent domain, the sponsor must decide which Events domain would have held a parent record for a parent-less FA record. A sponsor may consider that symptoms of the disease under study would be considered clinical events represented in the CE domain, so that FA records for symptoms of the disease under study would be in the FACE split of the FA domain.

This criterion is less likely to apply to interventions records than to events records. Interventions records often represent a series of individual substance administrations. When there is a change in dosing or other characteristics during the series, the most appropriate solution may be to represent the series of individual administrations in 2 records, one for the administrations before the change and a second for administrations after the change, rather than to create findings about records.

**Criterion 2:** An observation about an event or intervention which requires more than 1 variable for its representation, particularly when the observation may be represented with Findings class variables (e.g., units, method)

The need to represent data which require more than 1 variable in a findings about structure, rather than by adding 2 or more supplemental qualifiers to an Events or Interventions domain, is driven by the fact that each supplemental qualifier is in a separate record that links only to the parent record. For example, if the size of a rash is measured, then the result and measurement unit (e.g., centimeters, inches) can be represented in an FA domain in a single record; other information regarding the rash (e.g., start and end times) would, if collected, appear in an Event record. See, for example, the longest diameter measurements in Section 6.4.4., Findings About Events or Interventions, Example 2.

**Criterion 3:** Data or information that indicate the occurrence of pre-specified AEs

Every record in the AE domain must represent an actual adverse event. When subjects are asked if a pre-specified AE has occurred and the answer is "No", the "No" response cannot be stored in AE. These "No" responses are represented in an FA domain. In addition, the "Yes" responses are also represented in FA, so that responses to all prespecified questions are represented the same way (see FA Example 4).

**Criterion 4:** Signs or symptoms observed at a point in time that do not constitute events or describe an event as a whole

Data about signs or symptoms of a disease do not necessarily represent events or even describe an event. "Occurred in the last 24 hours" is a finding about a symptom. Whether these findings also constitute events depends on the sponsor's definition of "event". For a disease without recorded events, findings about the symptoms of the disease can be represented without an events or interventions record. If data do meet criteria to be represented in the findings about structure, FAOBJ will be the name of the symptom. The relationship to the disease under study may be represented in FACAT or FASCAT, as in FA Example 5.

The term "symptom" is often used loosely to refer to both symptoms (reported by the subject) and signs (observable by others). When data about signs is collected via questions about the subject's past experience, signs are appropriately represented as SDTM events. However, when a sign is identified or assessed during an examination at a point in time, it may be more appropriate to represent it as an SDTM finding.

**Points to Consider**

The choice between representing a data item as a supplemental qualifier or as a finding about an event or intervention may not be clear-cut. The following questions may help in making a decision.

- Does the data item have its own timing, separate from the timing of the event or intervention? If the data item represents some action during or after the event or intervention, it may be considered to have its own timing, and meet Criterion 1.
  - If the event or intervention is a disease milestone, then RELMIDS is not included in this event or intervention record. Is the relationship of a data item to the disease milestone (RELMIDS) needed? If so, it can be represented in FA, but not as a supplemental qualifier to the parent record.
- Are there several items which would be clearer if they could be grouped together? If so, the FA structure allows the use of FAGRPID, FACAT, or FASCAT to group the items.
- Is the data item alone in a particular study, but related to other data items likely to be collected in other studies? If so, it may be preferable to represent the item in FA, where other FA variables might be needed for related items in the future. For example, the response to "Was a rechallenge conducted?" might be represented as a supplemental qualifier, but if additional information about the rechallenge (e.g, When?, What was the result?) were collected, then the FA structure would be needed.
- Are there multiple evaluators for a data item that could otherwise be represented as a supplemental qualifier? If so, FA may provided a clearer representation of the multiple opinions, and would also allow the use of FAEVALID.

### 6.4.2 Naming Findings About Domains

Findings About domains are defined to store findings about events or interventions. Sponsors may choose to represent FA data collected in the study in a single FA dataset (potentially splitting the FA domain into physically separate datasets following the guidance described in Section 4.1.6, Additional Guidance on Dataset Naming), or separate datasets, assigning unique custom 2-character domain codes. There are 3 options:

1. A single FA domain.
2. A split FA domain, following the guidance described in Section 4.1.6, where:
   - The DOMAIN value is FA.
   - The dataset is named with FA as the first 2 characters and a suffix based on the parent domain, e.g., FAAE, FACE.
   - If a dataset-level RELREC is defined (e.g., between the CE and FACE datasets), then RDOMAIN may contain up to 4 characters to effectively describe the relationship between the CE parent records and the FACE child records.
3. Separate domains where:
   - The DOMAIN value is sponsor-defined and does not begin with FA, following examples in Section 6.4.5, Skin Response, which has a domain code of SR.
   - All published FA guidance applies, specifically:
     - The --OBJ variable cannot be added to a standard Findings domain. A domain is either a Findings domain or a Findings About domain, not one or the other depending on the situation.
     - When the --OBJ variable is included in a domain, this identifies it as an FA domain, and the --OBJ variable must be populated for all records.
   - All published domain guidance applies, specifically:
     - Variables that require a prefix would use the 2-character domain code chosen.

For the naming of datasets with findings about events or interventions for associated persons, refer to the SDTMIG: Associated Persons (available at https://www.cdisc.org/standards/foundational/sdtm).

### 6.4.3 Variables Unique to Findings About

The variable --OBJ is unique to Findings About. In conjunction with FATESTCD, it describes what the topic of the observation is; therefore, both are required to be populated for every record. FATESTCD describes the measurement/evaluation and FAOBJ describes the event or intervention that the measurement/evaluation is about.

When collected data fit a qualifier variable (see SDTM Sections 3.1.1, 3.1.2, and 3.1.3) and are represented in the FA domain, the name of the variable should be used as the value of FATESTCD. For example:

| FATESTCD | FATEST |
| --- | --- |
| OCCUR | Occurrence Indicator |
| SEV | Severity/Intensity |
| TOXGR | Toxicity Grade |

The use of the same names (e.g., SEV, OCCUR) for both qualifier variables in the observation classes and FATESTCD is deliberate, but should not lead users to conclude that the collection of such data (e.g., severity/intensity, occurrence) must be stored in the FA domain. In fact, data should only be stored in the FA domain if they do not fit in the general observation-class domain. If the data describe the underlying event or intervention as a whole and share its timing, then the data should be stored as a qualifier of the general observation-class record.

A record in FA may or may not have a parent record in an events or interventions domain. If an FA record does have a parent record, the value in FAOBJ should match the value in --TERM or --TRT, unless the parent domain is dictionary coded or subject to controlled terminology, in which case FAOBJ should match the value in --DECOD.

Examples for the FA and Skin Response (SR) domains include the use of RELREC to represent the relationship between an FA domain and a parent domain.

---

### 6.4.4 Findings About Events or Interventions (FA)

#### FA -- Description/Overview

A findings domain that contains the findings about an event or intervention that cannot be represented within an events or interventions domain record or as a supplemental qualifier.

#### FA -- Specification

fa.xpt, Findings About Events or Interventions -- Findings About. One record per finding, per object, per time point, per visit per subject, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format | Role | CDISC Notes | Core |
| --- | --- | --- | --- | --- | --- | --- |
| STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | FA | Identifier | Two-character abbreviation for the domain. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. | Req |
| FASEQ | Sequence Number | Num | | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. | Req |
| FAGRPID | Group ID | Char | | Identifier | Used to tie together a block of related records in a single domain for a subject. | Perm |
| FASPID | Sponsor-Defined Identifier | Char | | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF. | Perm |
| FATESTCD | Findings About Test Short Name | Char | (FATESTCD) | Topic | Short name of the measurement, test, or examination described in FATEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in FATESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). FATESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SEV", "OCCUR". | Req |
| FATEST | Findings About Test Name | Char | (FATEST) | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in FATEST cannot be longer than 40 characters. Examples: "Severity/Intensity", "Occurrence". | Req |
| FAOBJ | Object of the Observation | Char | | Record Qualifier | Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the term (e.g., "Acne") describing a clinical sign or symptom that is being measured by a severity test; an event (e.g., "VOMIT"), where the volume of vomit is being measured by a VOLUME test. | Req |
| FACAT | Category for Findings About | Char | * | Grouping Qualifier | Used to define a category of related records. Examples: "GERD", "PRE-SPECIFIED AE". | Perm |
| FASCAT | Subcategory for Findings About | Char | * | Grouping Qualifier | A further categorization of FACAT. | Perm |
| FAORRES | Result or Finding in Original Units | Char | | Result Qualifier | Result of the findings about measurement or test as originally received or collected. | Exp |
| FAORRESU | Original Units | Char | (UNIT) | Variable Qualifier | Original units in which the data were collected. The unit for FAORRES. | Exp |
| FASTRESC | Character Result/Finding in Std Format | Char | | Result Qualifier | Contains the result value for all findings, copied or derived from FAORRES in a standard format or standard units. FASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in FASTRESN. | Exp |
| FASTRESN | Numeric Result/Finding in Standard Units | Num | | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from FASTRESC. FASTRESN should store all numeric test results or findings. | Perm |
| FASTRESU | Standard Units | Char | (UNIT) | Variable Qualifier | Standardized units used for FASTRESC and FASTRESN. | Perm |
| FASTAT | Completion Status | Char | (ND) | Record Qualifier | Used to indicate that a finding was not done. Should be null if a result exists in FAORRES. | Perm |
| FAREASND | Reason Not Done | Char | | Record Qualifier | Describes why a measurement or test was not performed. Used in conjunction with FASTAT when value is "NOT DONE". | Perm |
| FALOC | Location of the Finding About | Char | (LOC) | Record Qualifier | Used to specify the location of the clinical evaluation. Example: "ARM". | Perm |
| FALAT | Laterality | Char | (LAT) | Variable Qualifier | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". | Perm |
| FALOBXFL | Last Observation Before Exposure Flag | Char | (NY) | Record Qualifier | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. | Perm |
| FABLFL | Baseline Flag | Char | (NY) | Record Qualifier | Indicator used to identify a baseline value. The value should be "Y" or null. Note that FABLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. | Perm |
| FAEVAL | Evaluator | Char | (EVAL) | Record Qualifier | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR". | Perm |
| VISITNUM | Visit Number | Num | | Timing | 1. Clinical encounter number. 2. Numeric version of VISIT, used for sorting. | Exp |
| VISIT | Visit Name | Char | | Timing | 1. Protocol-defined description of clinical encounter. 2. May be used in addition to VISITNUM and/or VISITDY. | Perm |
| VISITDY | Planned Study Day of Visit | Num | | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. | Perm |
| TAETORD | Planned Order of Element within Arm | Num | | Timing | Number that gives the planned order of the element within the arm. | Perm |
| EPOCH | Epoch | Char | (EPOCH) | Timing | Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP". | Perm |
| FADTC | Date/Time of Collection | Char | ISO 8601 datetime or interval | Timing | Collection date and time of findings assessment represented in ISO 8601 character format. | Exp |
| FADY | Study Day of Collection | Num | | Timing | 1. Study day of collection, measured as integer days. 2. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. | Perm |

> <sup>1</sup> In this column, an asterisk (\*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

#### FA -- Assumptions

1. The Findings About domain shares all qualities and conventions of findings observations.
2. See Section 6.4.1, When to Use Findings About Events or Interventions; and Section 8.6.3, Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions; for guidance on deciding between the use of the FA domain and other SDTM structures.
3. See Section 6.4.2, Naming Findings About Domains, for advice on splitting the FA domain.
4. Some variables in the events and interventions domains (e.g., OCCUR, SEV, TOXGR) represent findings about the whole of the event or intervention. When FA is used to represent findings about a part of the event or intervention (i.e., the assessment has different timing from the event as a whole), the FATEST and FATESTCD values should be the same as the variable name and variable label in the corresponding event or intervention domain. See Section 6.4.3, Variables Unique to Findings About.
   - a. Associations between some findings about cardiovascular interventions or events and their response codelists are described in the CV codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.
5. When data collection establishes a relationship between FA records and an events or interventions record, the relationship should be represented in RELREC.
   - a. The FAOBJ variable alone is not sufficient to establish a relationship, because an events or interventions dataset may have multiple records for the same topic (e.g., --TERM or --DECOD, --TRT or --DECOD).
6. Any Identifier variables, Timing variables, or Findings general observation-class qualifiers may be added to the FA domain, but the following qualifiers should generally not be used: --BODSYS, --MODIFY, --SEV, --TOXGR.

#### FA -- Examples

**Example 1:** The following example CRF collects severity and symptoms data at multiple time points about a migraine event, relative to dosing.

> **Migraine Symptoms Diary**
>
> Migraine Reference Number: xx
> When did the migraine start? DD-MMM-YYYY HH:MM
> When was study treatment taken? DD-MMM-YYYY HH:MM
>
> Answer the following **5 minutes BEFORE dosing**
> - Severity of migraine: Mild / Moderate / Severe
> - Associated symptoms: Sensitivity to light (No/Yes), Sensitivity to sound (No/Yes), Nausea (No/Yes), Aura (No/Yes)
>
> Answer the following **30 minutes AFTER dosing**
> - Severity of migraine: Mild / Moderate / Severe
> - Associated symptoms: Sensitivity to light (No/Yes), Sensitivity to sound (No/Yes), Nausea (No/Yes), Aura (No/Yes)
>
> Answer the following **90 minutes AFTER dosing**
> - Severity of migraine: Mild / Moderate / Severe
> - Associated symptoms: Sensitivity to light (No/Yes), Sensitivity to sound (No/Yes), Nausea (No/Yes), Aura (No/Yes)

In this example trial, migraines and symptoms associated with migraines were considered clinical events rather than reportable adverse events. The migraine, its sponsor identifier (i.e., the "Migraine Reference Number" on the CRF), and its start date were represented in a CE record.

ce.xpt

| Row | STUDYID | DOMAIN | USUBJID | CESEQ | CESPID | CETERM | CEDECOD | CESTDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | CE | ABC-123 | 1 | 90567 | Migraine | Migraine | 2007-05-16T10:30 |

The time migraine medication was taken was recorded in the Exposure (EX) domain. This date also serves as the reference time point for the symptom assessments.

ex.xpt

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXSPID | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | EX | ABC-123 | 1 | 4 | CURALL | 50 | mg | TABLET | ONCE | ORAL | TREATMENT | 2007-05-16T11:05 | 2007-05-16T11:05 |

The remaining data on the CRF were "snapshots" taken at 3 time points; in accordance with Section 6.4.1, When to Use Findings About Events or Interventions, criterion 1, these were represented as findings about events. The FACAT value "MIGRAINE SYMPTOMS" was used to represent the fact that these data were collected in a CRF module called "Migraine Symptoms Diary."

- Rows 1, 6, 11: Severity of the migraine was represented with FATESTCD="SEV". This FATESTCD value is derived from the events class variable name --SEV, and represents the same assessment as CESEV, except that this assessment is at a point in time rather than for the event as a whole.
- Rows 2-5, 7-10, 12-15: The presence of symptoms associated with migraine was represented with the name of the symptom in FAOBJ, as the data collected is about the occurrence of a particular symptom. The test code value "OCCUR" is derived from the events class variable name --OCCUR, but is an assessment at a point in time, rather than about the event as a whole. The relationship of these symptoms to migraine is represented in FACAT, which indicates that these data were collected in the Migraine Symptoms Diary.

face.xpt

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FASPID | FATESTCD | FATEST | FAOBJ | FACAT | FAORRES | FASTRESC | FADTC | FATPT | FATPTNUM | FAELTM | FATPTREF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | FA | ABC-123 | 1 | 90567 | SEV | Severity/Intensity | Migraine | MIGRAINE SYMPTOMS | SEVERE | SEVERE | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 2 | ABC | FA | ABC-123 | 2 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Light | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 3 | ABC | FA | ABC-123 | 3 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Sound | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 4 | ABC | FA | ABC-123 | 4 | 90567 | OCCUR | Occurrence Indicator | Nausea | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 5 | ABC | FA | ABC-123 | 5 | 90567 | OCCUR | Occurrence Indicator | Aura | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 6 | ABC | FA | ABC-123 | 6 | 90567 | SEV | Severity/Intensity | Migraine | MIGRAINE SYMPTOMS | MODERATE | MODERATE | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 7 | ABC | FA | ABC-123 | 7 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Light | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 8 | ABC | FA | ABC-123 | 8 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Sound | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 9 | ABC | FA | ABC-123 | 9 | 90567 | OCCUR | Occurrence Indicator | Nausea | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 10 | ABC | FA | ABC-123 | 10 | 90567 | OCCUR | Occurrence Indicator | Aura | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 11 | ABC | FA | ABC-123 | 11 | 90567 | SEV | Severity/Intensity | Migraine | MIGRAINE SYMPTOMS | MILD | MILD | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |
| 12 | ABC | FA | ABC-123 | 12 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Light | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |
| 13 | ABC | FA | ABC-123 | 13 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Sound | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |
| 14 | ABC | FA | ABC-123 | 14 | 90567 | OCCUR | Occurrence Indicator | Nausea | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |
| 15 | ABC | FA | ABC-123 | 15 | 90567 | OCCUR | Occurrence Indicator | Aura | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |

A dataset-level relationship in RELREC is based on the sponsor ID (--SPID) value, which was populated with a system-generated identifier unique to each iteration of this form.

relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | CE | | CESPID | | ONE | 1 |
| 2 | ABC | FA | | FASPID | | MANY | 1 |

---

**Example 2:** This CRF collects details about injection site rash events at each visit, until resolved.

> **Rash Assessment**
>
> Date of assessment: DD-MMM-YYYY
> Associated AE reference number: xx
> Rash longest diameter: ________ cm / in
>
> Lesion type and count:
> - Macules: 0 / 1 to 25 / 26 to 100 / 101 to 200 / 201 to 300 / >300
> - Papules: 0 / 1 to 25 / 26 to 100 / 101 to 200 / 201 to 300 / >300
> - Vesicles: 0 / 1 to 25 / 26 to 100 / 101 to 200 / 201 to 300 / >300
> - Pustules: 0 / 1 to 25 / 26 to 100 / 101 to 200 / 201 to 300 / >300
> - Scabs: 0 / 1 to 25 / 26 to 100 / 101 to 200 / 201 to 300 / >300
> - Scars: 0 / 1 to 25 / 26 to 100 / 101 to 200 / 201 to 300 / >300

In this scenario, the injection site rash event was considered a reportable adverse event; therefore, the rash itself was represented in the AE domain. The rash assessment form collects a reference number for the AE, represented in AESPID.

ae.xpt

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AESPID | AETERM | AEBODSYS | AELOC | AELAT | AESEV | AESER | AEACN | AESTDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | AE | XYZ-789 | 47869 | 5 | Injection site rash | General disorders and administration site conditions | ARM | LEFT | MILD | N | NOT APPLICABLE | 2007-05-10 |

Additional data about the rash were collected at visits 3 and 4, which occurred 2 days and 9 days after the start of the rash. These data were represented in an FA dataset because they were not about the event as a whole (see Section 6.4.1, criterion 1). In addition, the measurement of the rash requires multiple variables (value and unit) for its representation and the numbers of various kinds of lesions within the rash are a set of similar assessments of the event (see Section 6.4.1, criterion 2).

faae.xpt

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FASPID | FATESTCD | FATEST | FAOBJ | FAORRES | FAORRESU | FASTRESC | FASTRESU | VISITNUM | FADTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | FA | XYZ-789 | 123451 | 5 | LDIAM | Longest Diameter | Injection Site Rash | 2.5 | IN | 2.5 | IN | 3 | 2007-05-12 |
| 2 | XYZ | FA | XYZ-789 | 123452 | 5 | MACRNG | Number of Macules Range | Injection Site Rash | 26 to 100 | | 26 to 100 | | 3 | 2007-05-12 |
| 3 | XYZ | FA | XYZ-789 | 123453 | 5 | PAPRNG | Number of Papules Range | Injection Site Rash | 1 to 25 | | 1 to 25 | | 3 | 2007-05-12 |
| 4 | XYZ | FA | XYZ-789 | 123454 | 5 | VESRNG | Number of Vesicles Range | Injection Site Rash | 0 | | 0 | | 3 | 2007-05-12 |
| 5 | XYZ | FA | XYZ-789 | 123455 | 5 | PUSRNG | Number of Pustules Range | Injection Site Rash | 0 | | 0 | | 3 | 2007-05-12 |
| 6 | XYZ | FA | XYZ-789 | 123456 | 5 | SCBRNG | Number of Scabs Range | Injection Site Rash | 0 | | 0 | | 3 | 2007-05-12 |
| 7 | XYZ | FA | XYZ-789 | 123457 | 5 | SCRRNG | Number of Scars Range | Injection Site Rash | 0 | | 0 | | 3 | 2007-05-12 |
| 8 | XYZ | FA | XYZ-789 | 123459 | 5 | LDIAM | Longest Diameter | Injection Site Rash | 1 | IN | 1 | IN | 4 | 2007-05-19 |
| 9 | XYZ | FA | XYZ-789 | 123460 | 5 | MACRNG | Number of Macules Range | Injection Site Rash | 1 to 25 | | 1 to 25 | | 4 | 2007-05-19 |
| 10 | XYZ | FA | XYZ-789 | 123461 | 5 | PAPRNG | Number of Papules Range | Injection Site Rash | 1 to 25 | | 1 to 25 | | 4 | 2007-05-19 |
| 11 | XYZ | FA | XYZ-789 | 123462 | 5 | VESRNG | Number of Vesicles Range | Injection Site Rash | 0 | | 0 | | 4 | 2007-05-19 |
| 12 | XYZ | FA | XYZ-789 | 123463 | 5 | PUSRNG | Number of Pustules Range | Injection Site Rash | 0 | | 0 | | 4 | 2007-05-19 |
| 13 | XYZ | FA | XYZ-789 | 123464 | 5 | SCBRNG | Number of Scabs Range | Injection Site Rash | 0 | | 0 | | 4 | 2007-05-19 |
| 14 | XYZ | FA | XYZ-789 | 123465 | 5 | SCRRNG | Number of Scars Range | Injection Site Rash | 0 | | 0 | | 4 | 2007-05-19 |

The FA records were linked to the parent AE record via the AE reference number, which was used to populate both AESPID and FASPID.

relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | AE | | AESPID | | ONE | 23 |
| 2 | XYZ | FA | | FASPID | | MANY | 23 |

---

**Example 3:** This CRF collects information about rheumatoid arthritis. In this scenario, rheumatoid arthritis is a prerequisite for participation in an osteoporosis trial and was not collected as a Medical History (MH) event.

> **Rheumatoid Arthritis History**
>
> Date of assessment: DD-MMM-YYYY
> Date of diagnosis: DD-MMM-YYYY
>
> During the past 6 months, how would you rate the following:
>
> | Symptom | Was the symptom present? | If yes, what was the severity? |
> | --- | --- | --- |
> | Joint stiffness | Yes / No | Mild / Moderate / Severe |
> | Joint swelling | Yes / No | Mild / Moderate / Severe |
> | Joint pain (arthralgia) | Yes / No | Mild / Moderate / Severe |
> | Malaise | Yes / No | Mild / Moderate / Severe |
> | Early morning stiffness | Yes / No | If yes, average daily duration? ___Hours ___Minutes |

In this study, data were collected only at baseline. Because the occurrence and severity apply to the symptoms as a whole, they are represented in the MH domain. Note that the average duration of early morning stiffness cannot be represented in MHDUR because MHDUR would be the duration of the entire event, rather than the average of daily durations.

- Row 1: Because the CRF specifically collected date of diagnosis for rheumatoid arthritis, MHEVDTYP is populated with DIAGNOSIS to indicate that the date in MHSTDTC is the date of diagnosis.
- Rows 2-6: No start or end dates were collected for the symptoms, so the variable MHEVDTYP is not relevant for those records. MHEVDTYP is used only to specify the aspect of the event used to determine start and/or end dates.

mh.xpt

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHTERM | MHDECOD | MHEVDTYP | MHCAT | MHSCAT | MHPRESP | MHOCCUR | MHSEV | MHDTC | MHSTDTC | MHEVLINT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MH | 001-001 | 1 | RHEUMATOID ARTHRITIS | Rheumatoid arthritis | DIAGNOSIS | RHEUMATOID ARTHRITIS HISTORY | | Y | Y | | | 2003 | |
| 2 | ABC | MH | 001-001 | 2 | JOINT STIFFNESS | Joint stiffness | | RHEUMATOID ARTHRITIS HISTORY | RHEUMATOID ARTHRITIS SYMPTOMS | Y | Y | SEVERE | 2006-08-13 | | -P6M |
| 3 | ABC | MH | 001-001 | 3 | JOINT SWELLING | Joint swelling | | RHEUMATOID ARTHRITIS HISTORY | RHEUMATOID ARTHRITIS SYMPTOMS | Y | Y | MODERATE | 2006-08-13 | | -P6M |
| 4 | ABC | MH | 001-001 | 4 | JOINT PAIN | Arthralgia | | RHEUMATOID ARTHRITIS HISTORY | RHEUMATOID ARTHRITIS SYMPTOMS | Y | Y | MODERATE | 2006-08-13 | | -P6M |
| 5 | ABC | MH | 001-001 | 5 | MALAISE | Malaise | | RHEUMATOID ARTHRITIS HISTORY | RHEUMATOID ARTHRITIS SYMPTOMS | Y | Y | MILD | 2006-08-13 | | -P6M |
| 6 | ABC | MH | 001-001 | 6 | EARLY MORNING STIFFNESS | Stiffness | | RHEUMATOID ARTHRITIS HISTORY | RHEUMATOID ARTHRITIS SYMPTOMS | Y | Y | | 2006-08-13 | | -P6M |

The average duration of early morning stiffness would be represented in ISO 8601 duration format as a supplemental qualifier.

suppmh.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | MH | 001-001 | MHSEQ | 6 | MHAVDDUR | Average Daily Duration | PT1H30M | CRF | |

---

**Example 4:** In this example, the occurrence of prespecified adverse events was solicited at every visit and the visit date was used as the date of collection. The data collected meet criterion 3 in Section 6.4.1, When to Use Findings About Events or Interventions; that is, data that indicate the occurrence of prespecified AEs.

> **Prespecified Adverse Events of Clinical Interest**
>
> Date of assessment: DD-MMM-YYYY
> Did the following occur? If Yes, enter a complete record in the AE CRF
> - Headache: No / Yes / Not Done
> - Respiratory infection: No / Yes / Not Done
> - Nausea: No / Yes / Not Done

This example shows data for 1 subject at 2 visits. Each response (e.g., No, Yes) to the prespecified terms is represented in the FA domain. The visit date was used to populate FADTC.

- Rows 1, 4: "Headache" was reported at both visits.
- Rows 2, 5: "Respiratory infection" was not present at either visit.
- Row 3: The investigator did not ask the subject about the occurrence of nausea. This was represented by FASTAT="NOT DONE".
- Row 6: "Nausea" was reported at visit 3.

faae.xpt

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FATESTCD | FATEST | FAOBJ | FAORRES | FASTRESC | FASTAT | VISITNUM | VISIT | FADTC | FAEVINTX |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC101 | FA | 1234 | 1 | OCCUR | Occurrence Indicator | Headache | Y | Y | | 2 | VISIT 2 | 2005-10-01 | SINCE LAST VISIT |
| 2 | ABC101 | FA | 1234 | 2 | OCCUR | Occurrence Indicator | Respiratory Infection | N | N | | 2 | VISIT 2 | 2005-10-01 | SINCE LAST VISIT |
| 3 | ABC101 | FA | 1234 | 3 | OCCUR | Occurrence Indicator | Nausea | | | NOT DONE | 2 | VISIT 2 | 2005-10-01 | SINCE LAST VISIT |
| 4 | ABC101 | FA | 1234 | 4 | OCCUR | Occurrence Indicator | Headache | Y | Y | | 3 | VISIT 3 | 2005-10-10 | SINCE LAST VISIT |
| 5 | ABC101 | FA | 1234 | 5 | OCCUR | Occurrence Indicator | Respiratory Infection | N | N | | 3 | VISIT 3 | 2005-10-10 | SINCE LAST VISIT |
| 6 | ABC101 | FA | 1234 | 6 | OCCUR | Occurrence Indicator | Nausea | Y | Y | | 3 | VISIT 3 | 2005-10-10 | SINCE LAST VISIT |

For each prespecified adverse event for which FAORRES = "Y", the adverse event has a record in the AE domain with AEPRESP = "Y". No relationship was collected to link the FAAE record for the occurrence indicator test with the AE entries, so no RELREC was created.

- Row 1: Comparison of this AE record with the FA dataset records for "Headache" shows that there are 2 records with FAOBJ="Headache". FAORRES="Y" indicates that this AE record is associated with both FA records, because this headache started before visit 2 and ended between visits 2 and 3.
- Row 2: Comparison of this AE record with the FA dataset shows that this AE started and ended in the time between visits 2 and 3, and is consistent with the FA response for FAOBJ="Nausea" for visit 3.

ae.xpt

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AEDECOD | AEPRESP | AEBODSYS | AESEV | AEACN | AESTDTC | AEENDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC101 | AE | 1234 | 1 | Headache | Headache | Y | Nervous system disorders | MILD | NONE | 2005-09-30 | 2005-10-03 |
| 2 | ABC101 | AE | 1234 | 2 | Nausea | Nausea | Y | Gastrointestinal disorders | MODERATE | NONE | 2005-10-08 | 2005-10-09 |

---

**Example 5:** In this example, data about prespecified symptoms of the disease under study were collected on a daily basis. Although the date of the assessment was captured in the CRF header (not shown), start and end timing of the prespecified symptoms was not.

> **Symptoms**
>
> | | Occurred in last 24 hours? | Investigator GERD Symptom Measurement (if symptom occurred) | | |
> | --- | --- | --- | --- | --- |
> | | | Volume (mL) | Number of episodes | Maximum severity |
> | Vomiting | Yes / No | ___ | ___ | Mild / Moderate / Severe |
> | Diarrhea | Yes / No | ___ | ___ | Mild / Moderate / Severe |
> | Nausea | Yes / No | ___ | ___ | Mild / Moderate / Severe |

The collected data were represented in FA because they meet criterion 1 in Section 6.4.1, When to Use Findings About Events or Interventions, that is, data that do not describe an event or intervention as a whole. In this study, GERD symptoms were considered clinical events. In addition, the volume of vomit data met criterion 2 data ("about" an event or intervention), having qualifiers that can be represented in Findings variables (e.g., units, method).

This SDTM example represents data from 2 visits for 1 subject. FAEVINTX indicates that assessments were for the previous 24 hours.

- Rows 1-4: Show the results for the vomiting tests at visit 1. Because the number of episodes was recorded as ">10", this is represented in FASTRESC but not in FASTRESN.
- Rows 5-7: Show the results for the diarrhea tests at visit 1.
- Rows 8-10: Show the results for the nausea tests at visit 1.
- Row 11: Shows that vomiting did not occur in the 24 hours before visit 2; thus, volume, number of episodes, and severity were not applicable.
- Rows 12-14: Show the results for the diarrhea tests at visit 2.
- Row 15: Indicates that the occurrence of nausea was not assessed at visit 2.

face.xpt

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FATESTCD | FATEST | FAOBJ | FACAT | FAORRES | FAORRESU | FASTRESC | FASTRESN | FASTRESU | FASTAT | VISITNUM | VISIT | FADTC | FAEVLINT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | FA | XYZ-701-002 | 1 | OCCUR | Occurrence Indicator | Vomiting | GERD SYMPTOMS | Y | | Y | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 2 | XYZ | FA | XYZ-701-002 | 2 | VOL | Volume | Vomiting | GERD SYMPTOMS | 250 | mL | 250 | 250 | mL | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 3 | XYZ | FA | XYZ-701-002 | 3 | NUMEPISD | Number of Episodes | Vomiting | GERD SYMPTOMS | >10 | | >10 | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 4 | XYZ | FA | XYZ-701-002 | 4 | SEV | Severity/Intensity | Vomiting | GERD SYMPTOMS | SEVERE | | SEVERE | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 5 | XYZ | FA | XYZ-701-002 | 5 | OCCUR | Occurrence Indicator | Diarrhea | GERD SYMPTOMS | Y | | Y | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 6 | XYZ | FA | XYZ-701-002 | 6 | NUMEPISD | Number of Episodes | Diarrhea | GERD SYMPTOMS | 2 | | 2 | 2 | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 7 | XYZ | FA | XYZ-701-002 | 7 | SEV | Severity/Intensity | Diarrhea | GERD SYMPTOMS | SEVERE | | SEVERE | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 8 | XYZ | FA | XYZ-701-002 | 8 | OCCUR | Occurrence Indicator | Nausea | GERD SYMPTOMS | Y | | Y | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 9 | XYZ | FA | XYZ-701-002 | 9 | NUMEPISD | Number of Episodes | Nausea | GERD SYMPTOMS | 1 | | 1 | 1 | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 10 | XYZ | FA | XYZ-701-002 | 10 | SEV | Severity/Intensity | Nausea | GERD SYMPTOMS | MODERATE | | MODERATE | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 11 | XYZ | FA | XYZ-701-002 | 11 | OCCUR | Occurrence Indicator | Vomiting | GERD SYMPTOMS | N | | N | | | | 2 | VISIT 2 | 2006-02-03 | -PT24H |
| 12 | XYZ | FA | XYZ-701-002 | 12 | OCCUR | Occurrence Indicator | Diarrhea | GERD SYMPTOMS | Y | | Y | | | | 2 | VISIT 2 | 2006-02-03 | -PT24H |
| 13 | XYZ | FA | XYZ-701-002 | 13 | NUMEPISD | Number of Episodes | Diarrhea | GERD SYMPTOMS | 1 | | 1 | 1 | | | 2 | VISIT 2 | 2006-02-03 | -PT24H |
| 14 | XYZ | FA | XYZ-701-002 | 14 | SEV | Severity/Intensity | Diarrhea | GERD SYMPTOMS | SEVERE | | SEVERE | | | | 2 | VISIT 2 | 2006-02-03 | -PT24H |
| 15 | XYZ | FA | XYZ-701-002 | 15 | OCCUR | Occurrence Indicator | Nausea | GERD SYMPTOMS | | | | | | NOT DONE | 2 | VISIT 2 | 2006-02-03 | -PT24H |

---

**Example 6:** In this example, the sponsor's definition of "event" meant that 1 record would be created for each adverse event, covering it from start to finish (see Section 6.2.1, Adverse Events, assumption 6.4). The AE module also collected information about severity at each visit.

A paper CRF to be updated at each visit might look like this:

_At each visit, record the maximum severity of the adverse event since the last visit._

| AE ID | Adverse Event | Start Date | End Date | Visit 2 | Visit 3 | Visit 4 | Visit 5 | Visit 6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
||||| Mild / Moderate / Severe | Mild / Moderate / Severe | Mild / Moderate / Severe | Mild / Moderate / Severe | Mild / Moderate / Severe |
||||| Mild / Moderate / Severe | Mild / Moderate / Severe | Mild / Moderate / Severe | Mild / Moderate / Severe | Mild / Moderate / Severe |
||||| Mild / Moderate / Severe | Mild / Moderate / Severe | Mild / Moderate / Severe | Mild / Moderate / Severe | Mild / Moderate / Severe |

An electronic data collection instrument would probably be constructed as 2 related modules:

A module for the adverse event, where a record would be entered for each event:

| AE ID | Adverse Event | Start Date | End Date |
| --- | --- | --- | --- |
|||||

A module for the severity assessment, where a record would be entered for each assessment:

| Visit | AE ID | Maximum severity since last visit |
| --- | --- | --- |
||| Mild / Moderate / Severe |

AE collection started after visit 1, so the first severity data was collected at visit 2.

The collected data met criterion 1 in Section 6.4.1, When to Use Findings About Events or Interventions, for data that do not describe an event or intervention as a whole.

In this example, the sponsor populated AESEV with the maximum severity over the course of the event. This was not directly collected, but rather determined from the weekly maximum severity assessments collected on the CRF. For clarity, only selected variables in the AE dataset are shown here.

ae.xpt

| Row | DOMAIN | USUBJID | AESEQ | AESPID | AETERM | AEDECOD | AESEV | AESTDTC | AEENDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AE | 123 | 1 | 1 | Morning queasiness | Nausea | MODERATE | 2006-02-01 | 2006-02-23 |
| 2 | AE | 123 | 2 | 2 | Watery stools | Diarrhea | MILD | 2006-02-01 | 2006-02-15 |

The values in FAOBJ are the values from AEDECOD, which were assigned during coding, rather than directly collected. The values in FASPID are the AE identifiers from AESPID. FAEVINTX indicates that the evaluation was for the period since the last visit.

- Rows 1-4: Show severity data collected at the 4 visits that occurred between the start and end of the AE "Morning queasiness". FAOBJ=NAUSEA, which is the value of AEDECOD in the associated AE record.
- Rows 5-6: Show severity data collected at the 2 visits that occurred between the start and end of the AE "Watery stools." FAOBJ=DIARRHEA, which is the value of AEDECOD in the associated AE record.

faae.xpt

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FASPID | FATESTCD | FATEST | FAOBJ | FAORRES | FACOLSRT | VISITNUM | VISIT | FADTC | FAEVINTX |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | FA | XYZ-US-701-002 | 1 | 1 | SEV | Severity/Intensity | Nausea | MILD | MAXIMUM | 2 | VISIT 2 | 2006-02-02 | SINCE LAST VISIT |
| 2 | XYZ | FA | XYZ-US-701-002 | 2 | 1 | SEV | Severity/Intensity | Nausea | MODERATE | MAXIMUM | 3 | VISIT 3 | 2006-02-09 | SINCE LAST VISIT |
| 3 | XYZ | FA | XYZ-US-701-002 | 3 | 1 | SEV | Severity/Intensity | Nausea | MODERATE | MAXIMUM | 4 | VISIT 4 | 2006-02-16 | SINCE LAST VISIT |
| 4 | XYZ | FA | XYZ-US-701-002 | 4 | 1 | SEV | Severity/Intensity | Nausea | MILD | MAXIMUM | 5 | VISIT 5 | 2006-02-23 | SINCE LAST VISIT |
| 5 | XYZ | FA | XYZ-US-701-002 | 5 | 2 | SEV | Severity/Intensity | Diarrhea | MILD | MAXIMUM | 2 | VISIT 2 | 2006-02-02 | SINCE LAST VISIT |
| 6 | XYZ | FA | XYZ-US-701-002 | 6 | 2 | SEV | Severity/Intensity | Diarrhea | MILD | MAXIMUM | 3 | VISIT 3 | 2006-02-09 | SINCE LAST VISIT |

Because the AE identifier (AESPID) was included in the FA dataset, AE and FA data can be related with a dataset-to-dataset relationship.

relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | AE | | AESPID | | ONE | 1 |
| 2 | ABC | FA | | FASPID | | MANY | 1 |

---

### 6.4.5 Skin Response (SR)

#### SR -- Description/Overview

A findings about domain for submitting dermal responses to antigens.

#### SR -- Specification

sr.xpt, Skin Response -- Findings About. One record per finding, per object, per time point, per visit per subject, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format | Role | CDISC Notes | Core |
| --- | --- | --- | --- | --- | --- | --- |
| STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | SR | Identifier | Two-character abbreviation for the domain. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. | Req |
| SRSEQ | Sequence Number | Num | | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. | Req |
| SRGRPID | Group ID | Char | | Identifier | Used to tie together a block of related records in a single domain for a subject. | Perm |
| SRREFID | Reference ID | Char | | Identifier | Internal or external specimen identifier. Example: "Specimen ID". | Perm |
| SRSPID | Sponsor-Defined Identifier | Char | | Identifier | Sponsor-defined identifier. | Perm |
| SRTESTCD | Skin Response Test or Exam Short Name | Char | (SRTESTCD) | Topic | Short name of the measurement, test, or examination described in SRTEST. The value in SRTESTCD cannot be longer than 8 characters, nor can it start with a number. SRTESTCD cannot contain characters other than letters, numbers, or underscores. | Req |
| SRTEST | Skin Response Test or Examination Name | Char | (SRTEST) | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in SRTEST cannot be longer than 40 characters. Example: "Wheal Diameter". | Req |
| SROBJ | Object of the Observation | Char | | Record Qualifier | Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the dose of the immunogenic material or the allergen associated with the response (e.g., "Johnson Grass IgE 0.15 BAU mL"). | Req |
| SRCAT | Category for Test | Char | | Grouping Qualifier | Used to define a category of topic-variable values across subjects. | Perm |
| SRSCAT | Subcategory for Test | Char | | Grouping Qualifier | A further categorization of SRCAT values. | Perm |
| SRORRES | Results or Findings in Original Units | Char | | Result Qualifier | Results of measurement or finding as originally received or collected. | Exp |
| SRORRESU | Original Units | Char | (UNIT) | Variable Qualifier | Original units in which the data were collected. The unit for SRORRES. Example: "mm". | Exp |
| SRSTRESC | Character Result/Finding in Std Format | Char | | Result Qualifier | Contains the result value for all findings copied or derived from SRORRES, in a standard format or in standard units. SRSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in SRSTRESN. | Exp |
| SRSTRESN | Numeric Results/Findings in Std. Units | Num | | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from SRSTRESC. SRSTRESN should store all numeric test results or findings. | Exp |
| SRSTRESU | Standard Units | Char | (UNIT) | Variable Qualifier | Standardized units used for SRSTRESC and SRSTRESN. Example: "mm". | Exp |
| SRSTAT | Completion Status | Char | (ND) | Record Qualifier | Used to indicate exam not done. Should be null if a result exists in SRORRES. | Perm |
| SRREASND | Reason Not Done | Char | | Record Qualifier | Describes why a measurement or test was not performed. Used in conjunction with SRSTAT when value is "NOT DONE". | Perm |
| SRNAM | Vendor Name | Char | | Record Qualifier | Name or identifier of the laboratory or vendor who provided the test results. | Perm |
| SRSPEC | Specimen Type | Char | (SPECTYPE) | Record Qualifier | Defines the types of specimen used for a measurement. Example: "SKIN". | Perm |
| SRLOC | Location Used for Measurement | Char | (LOC) | Record Qualifier | Location relevant to the collection of the measurement. | Perm |
| SRLAT | Laterality | Char | (LAT) | Variable Qualifier | Qualifier for anatomical location further detailing laterality of intervention administration. Examples: "RIGHT", "LEFT", "BILATERAL". | Perm |
| SRMETHOD | Method of Test or Examination | Char | (METHOD) | Record Qualifier | Method of test or examination. Examples: "ELISA", "EIA", "MICRONEUTRALIZATION ASSAY", "PLAQUE REDUCTION NEUTRALIZATION ASSAY". | Perm |
| SRLOBXFL | Last Observation Before Exposure Flag | Char | (NY) | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. | Perm |
| SRBLFL | Baseline Flag | Char | (NY) | Record Qualifier | Indicator used to identify a baseline value. The value should be "Y" or null. Note that SRBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. | Perm |
| SREVAL | Evaluator | Char | (EVAL) | Record Qualifier | Role of person who provided evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR". | Perm |
| VISITNUM | Visit Number | Num | | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. | Exp |
| VISIT | Visit Name | Char | | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. | Perm |
| VISITDY | Planned Study Day of Visit | Num | | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. | Perm |
| TAETORD | Planned Order of Element within Arm | Num | | Timing | Number that gives the planned order of the element within the arm. | Perm |
| EPOCH | Epoch | Char | (EPOCH) | Timing | Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", and "FOLLOW-UP". | Perm |
| SRDTC | Date/Time of Collection | Char | ISO 8601 datetime or interval | Timing | Collection date and time of an observation represented in ISO 8601. | Exp |
| SRDY | Study Day of Visit/Collection/Exam | Num | | Timing | Actual study day of visit/collection/exam expressed in integer days relative to sponsor-defined RFSTDTC in Demographics. | Perm |
| SRTPT | Planned Time Point Name | Char | | Timing | Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See SRTPTNUM and SRTPTREF. Examples: "START", "5 MIN POST". | Perm |
| SRTPTNUM | Planned Time Point Number | Num | | Timing | Numerical version of SRTPT to aid in sorting. | Perm |
| SRELTM | Planned Elapsed Time from Time Point Ref | Char | ISO 8601 duration | Timing | Planned elapsed time (in ISO 8601) relative to a fixed time point reference (SRTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent 15 minutes prior to the reference point, "PT8H" to represent 8 hours after the reference point. | Perm |
| SRTPTREF | Time Point Reference | Char | | Timing | Name of the fixed reference point referred to by SRELTM, SRTPTNUM, and SRTPT. Example: "INTRADERMAL INJECTION". | Perm |
| SRRFTDTC | Date/Time of Reference Time Point | Char | ISO 8601 datetime or interval | Timing | Date/time of the reference time point, SRTPTREF. | Perm |

> <sup>1</sup> In this column, an asterisk (\*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

#### SR -- Assumptions

1. The Skin Response (SR) domain is used to represent findings about an intervention, but it has its own domain code, SR, rather than the domain code FA.
2. This domain is intended specifically for tests of the immune response to substances that are intended to provoke such a response (e.g., allergens used in allergy testing). SR is not intended for other injection-site reactions, including reactogenicity events that may follow a vaccine administration.
3. Because a subject is typically exposed to many test materials at the same time, SROBJ is needed to represent the test material for each response record. The method of assessment could be a skin-prick test, a skin-scratch test, or other method of introducing the challenge substance into the skin.
4. Any Identifier variables, Timing variables, or Findings general observation class qualifiers may be added to the SR domain, but the following qualifiers would not generally be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --RESCAT, --XFN, --LOINC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

#### SR -- Examples

**Example 1:** In this example, the subject is dosed with increasing concentrations of Johnson grass IgE.

- Rows 1-4: Show responses associated with the administration of a histamine control.
- Rows 5-8: Show responses associated with the administration of Johnson grass IgE. These records describe the dose response to different concentrations of Johnson grass IgE antigen, as reflected in SROBJ.
- All rows show a specific location on the back (e.g., SITE1), represented in FOCID.

sr.xpt

| Row | STUDYID | DOMAIN | USUBJID | FOCID | SRSEQ | SRTESTCD | SRTEST | SROBJ | SRORRES | SRORRESU | SRSTRESC | SRSTRESN | SRSTRESU | SRLOC | VISITNUM | VISIT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SPI-001 | SR | SPI-001-11035 | SITE1 | 1 | FLRMDIAM | Flare Mean Diameter | Histamine Control 10 mg/mL | 5 | mm | 5 | 5 | mm | BACK | 1 | VISIT 1 |
| 2 | SPI-001 | SR | SPI-001-11035 | SITE2 | 2 | FLRMDIAM | Flare Mean Diameter | Histamine Control 10 mg/mL | 4 | mm | 4 | 4 | mm | BACK | 1 | VISIT 1 |
| 3 | SPI-001 | SR | SPI-001-11035 | SITE3 | 3 | FLRMDIAM | Flare Mean Diameter | Histamine Control 10 mg/mL | 5 | mm | 5 | 5 | mm | BACK | 1 | VISIT 1 |
| 4 | SPI-001 | SR | SPI-001-11035 | SITE4 | 4 | FLRMDIAM | Flare Mean Diameter | Histamine Control 10 mg/mL | 5 | mm | 5 | 5 | mm | BACK | 1 | VISIT 1 |
| 5 | SPI-001 | SR | SPI-001-11035 | SITE5 | 5 | FLRMDIAM | Flare Mean Diameter | Johnson Grass 0.05 BAU/mL | 10 | mm | 10 | 10 | mm | BACK | 1 | VISIT 1 |
| 6 | SPI-001 | SR | SPI-001-11035 | SITE6 | 6 | FLRMDIAM | Flare Mean Diameter | Johnson Grass 0.10 BAU/mL | 11 | mm | 11 | 11 | mm | BACK | 1 | VISIT 1 |
| 7 | SPI-001 | SR | SPI-001-11035 | SITE7 | 7 | FLRMDIAM | Flare Mean Diameter | Johnson Grass 0.15 BAU/mL | 20 | mm | 20 | 20 | mm | BACK | 1 | VISIT 1 |
| 8 | SPI-001 | SR | SPI-001-11035 | SITE8 | 8 | FLRMDIAM | Flare Mean Diameter | Johnson Grass 0.20 BAU/mL | 30 | mm | 30 | 30 | mm | BACK | 1 | VISIT 1 |

---

**Example 2:** In this example, the study product dose, Dog Epi IgG, was administered at increasing concentrations. The size of the wheal is being measured (reaction to Dog Epi IgG) to evaluate the efficacy of the Dog Epi IgG extract versus a negative control (NC) and a positive control (PC) in the testing of allergenic extracts.

While SROBJ is populated with information about the substance administered, full details regarding the study product would be submitted in the Exposure (EX) dataset. The relationship between SR records and EX records would be represented using RELREC.

- Rows 1-6: Show the response (description and reaction grade) to the study product at a series of different dose levels, the latter reflected in SROBJ. The descriptions of SRORRES values are correlated to a grade, and the grade values are stored in SRSTRESC.
- Rows 7-12: Show the results of wheal diameter measurements in response to the study product at a series of different dose levels.

sr.xpt

| Row | STUDYID | DOMAIN | USUBJID | SRSEQ | SRSPID | SRTESTCD | SRTEST | SROBJ | SRORRES | SRORRESU | SRSTRESC | SRSTRESN | SRSTRESU | SRLOC | VISITNUM | VISIT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CC-001 | SR | CC-001-101 | 1 | 1 | REACTGR | Reaction Grade | Dog Epi 0 mg | NEGATIVE | | NEGATIVE | | | FOREARM | 1 | WEEK 1 |
| 2 | CC-001 | SR | CC-001-101 | 2 | 2 | REACTGR | Reaction Grade | Dog Epi 0.1 mg | NEGATIVE | | NEGATIVE | | | FOREARM | 1 | WEEK 1 |
| 3 | CC-001 | SR | CC-001-101 | 3 | 3 | REACTGR | Reaction Grade | Dog Epi 0.5 mg | ERYTHEMA, INFILTRATION, POSSIBLY DISCRETE PAPULES | | 1+ | | | FOREARM | 1 | WEEK 1 |
| 4 | CC-001 | SR | CC-001-101 | 4 | 4 | REACTGR | Reaction Grade | Dog Epi 1 mg | ERYTHEMA, INFILTRATION, PAPULES, VESICLES | | 2+ | | | FOREARM | 1 | WEEK 1 |
| 5 | CC-001 | SR | CC-001-101 | 5 | 5 | REACTGR | Reaction Grade | Dog Epi 1.5 mg | ERYTHEMA, INFILTRATION, PAPULES, VESICLES | | 2+ | | | FOREARM | 1 | WEEK 1 |
| 6 | CC-001 | SR | CC-001-101 | 6 | 6 | REACTGR | Reaction Grade | Dog Epi 2 mg | ERYTHEMA, INFILTRATION, PAPULES, COALESCING VESICLES | | 3+ | | | FOREARM | 1 | WEEK 1 |
| 7 | CC-001 | SR | CC-001-101 | 7 | 7 | FLRMDIAM | Flare Mean Diameter | Dog Epi 0 mg | 5 | mm | 5 | 5 | mm | FOREARM | 1 | WEEK 1 |
| 8 | CC-001 | SR | CC-001-101 | 8 | 8 | FLRMDIAM | Flare Mean Diameter | Dog Epi 0.1 mg | 10 | mm | 10 | 10 | mm | FOREARM | 1 | WEEK 1 |
| 9 | CC-001 | SR | CC-001-101 | 9 | 9 | FLRMDIAM | Flare Mean Diameter | Dog Epi 0.5 mg | 22 | mm | 22 | 22 | mm | FOREARM | 1 | WEEK 1 |
| 10 | CC-001 | SR | CC-001-101 | 10 | 10 | FLRMDIAM | Flare Mean Diameter | Dog Epi 1 mg | 100 | mm | 100 | 100 | mm | FOREARM | 1 | WEEK 1 |
| 11 | CC-001 | SR | CC-001-101 | 11 | 11 | FLRMDIAM | Flare Mean Diameter | Dog Epi 1.5 mg | 1 | mm | 1 | 1 | mm | FOREARM | 1 | WEEK 1 |
| 12 | CC-001 | SR | CC-001-101 | 12 | 12 | FLRMDIAM | Flare Mean Diameter | Dog Epi 2 mg | 8 | mm | 8 | 8 | mm | FOREARM | 1 | WEEK 1 |

ex.xpt

| Row | STUDYID | DOMAIN | USUBJID | EXSPID | EXTRT | EXDOSE | EXDOSEU | EXROUTE | EXLOC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CC-001 | EX | 101 | 1 | Dog Epi IgG | 0 | mg | CUTANEOUS | FOREARM |
| 2 | CC-001 | EX | 101 | 2 | Dog Epi IgG | 0.1 | mg | CUTANEOUS | FOREARM |
| 3 | CC-001 | EX | 101 | 3 | Dog Epi IgG | 0.5 | mg | CUTANEOUS | FOREARM |
| 4 | CC-001 | EX | 101 | 4 | Dog Epi IgG | 1 | mg | CUTANEOUS | FOREARM |
| 5 | CC-001 | EX | 101 | 5 | Dog Epi IgG | 1.5 | mg | CUTANEOUS | FOREARM |
| 6 | CC-001 | EX | 101 | 6 | Dog Epi IgG | 2 | mg | CUTANEOUS | FOREARM |

The relationships between SR and EX records are represented at the record level in RELREC.

relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CC-001 | SR | CC-001-101 | SRSPID | 1 | | R1 |
| 2 | CC-001 | SR | CC-001-101 | SRSPID | 7 | | R1 |
| 3 | CC-001 | EX | CC-001-101 | EXSPID | 1 | | R1 |
| 4 | CC-001 | SR | CC-001-101 | SRSPID | 2 | | R2 |
| 5 | CC-001 | SR | CC-001-101 | SRSPID | 8 | | R2 |
| 6 | CC-001 | EX | CC-001-101 | EXSPID | 2 | | R2 |
| 7 | CC-001 | SR | CC-001-101 | SRSPID | 3 | | R3 |
| 8 | CC-001 | SR | CC-001-101 | SRSPID | 9 | | R3 |
| 9 | CC-001 | EX | CC-001-101 | EXSPID | 3 | | R3 |
| 10 | CC-001 | SR | CC-001-101 | SRSPID | 4 | | R4 |
| 11 | CC-001 | SR | CC-001-101 | SRSPID | 10 | | R4 |
| 12 | CC-001 | EX | CC-001-101 | EXSPID | 4 | | R4 |
| 13 | CC-001 | SR | CC-001-101 | SRSPID | 5 | | R5 |
| 14 | CC-001 | SR | CC-001-101 | SRSPID | 11 | | R5 |
| 15 | CC-001 | EX | CC-001-101 | EXSPID | 5 | | R5 |
| 16 | CC-001 | SR | CC-001-101 | SRSPID | 6 | | R6 |
| 17 | CC-001 | SR | CC-001-101 | SRSPID | 12 | | R6 |
| 18 | CC-001 | EX | CC-001-101 | EXSPID | 6 | | R6 |

---

**Example 3:** This example shows the results from a tuberculin purified protein derivative (PPD) skin test administered using the Mantoux technique. The subject was given an intradermal injection of standard tuberculin PPD (i.e., PPD-S) in the left forearm at visit 1; see the Procedure Agents (AG) record below. At visit 2, the induration diameter and presence of blistering were recorded. Because the tuberculin PPD skin test cannot be interpreted using the induration diameter and blistering alone (e.g., risk for being infected with TB must also be considered), the interpretation of the skin test resides in its own row. The time point variables show that the planned time for reading the test was 48 hours after Mantoux administration. However, a comparison of datetime values in SRDTC and SRRFTDTC shows that in this case the test was read at 53 hours and 56 minutes after Mantoux administration.

- Row 1: Shows the longest diameter in millimeters of the induration after receiving an intradermal injection of 0.1 mL containing 5TU of PPD-S in the left forearm.
- Row 2: Shows the presence of blistering at the tuberculin PPD skin test site.
- Row 3: Shows the interpretation of the tuberculin PPD skin test. SRGRPID is used to tie together the results to the interpretation.

sr.xpt

| Row | STUDYID | DOMAIN | USUBJID | SRSEQ | SRGRPID | SRTESTCD | SRTEST | SROBJ | SRORRES | SRORRESU | SRSTRESC | SRSTRESN | SRSTRESU | SRLOC | SRLAT | SRMETHOD | VISITNUM | VISIT | EPOCH | SRDTC | SRTPT | SRELTM | SRTPTREF | SRRFTDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | SR | ABC-001 | 1 | 1 | IDRLDIAM | Induration Longest Diameter | Tuberculin PPD-S | 16 | mm | 16 | 16 | mm | FOREARM | LEFT | RULER | 2 | VISIT 2 | OPEN LABEL TREATMENT | 2011-01-19T14:08:24 | 48 H | PT48H | MANTOUX ADMINISTRATION | 2011-01-17T08:30:00 |
| 2 | ABC | SR | ABC-001 | 2 | 1 | BLISTIND | Blistering Indicator | Tuberculin PPD-S | Y | | Y | | | FOREARM | LEFT | | 2 | VISIT 2 | OPEN LABEL TREATMENT | 2011-01-19T14:08:24 | 48 H | PT48H | MANTOUX ADMINISTRATION | 2011-01-17T08:30:00 |
| 3 | ABC | SR | ABC-001 | 3 | 1 | INTP | Interpretation | Tuberculin PPD-S | POSITIVE | | POSITIVE | | | | | | 2 | VISIT 2 | OPEN LABEL TREATMENT | 2011-01-19T14:08:24 | 48 H | PT48H | MANTOUX ADMINISTRATION | 2011-01-17T08:30:00 |

The tuberculin PPD skin test administration was represented in the AG domain.

ag.xpt

| Row | STUDYID | DOMAIN | USUBJID | AGSEQ | AGTRT | AGDOSE | AGDOSU | AGVAMT | AGVAMTU | VISITNUM | VISIT | EPOCH | AGSTDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | AG | ABC-001 | 1 | Tuberculin PPD-S | 5 | tuberculin unit | 0.1 | mL | 1 | VISIT 1 | OPEN LABEL TREATMENT | 2011-01-17T08:30:00 |

Relationships between SR and AG records were shown in RELREC.

relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | SR | ABC-001 | SRGRPID | 1 | | R1 |
| 2 | ABC | AG | ABC-001 | AGSEQ | 1 | | R1 |
