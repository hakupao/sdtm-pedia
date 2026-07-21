# SDTM IG v3.4 Variables - PE Domain

**Domain Code:** `PE`

**Total Variables:** 30

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `PESEQ` | Sequence Number | Num | Req | Identifier | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number. |
| `PEGRPID` | Group ID | Char | Perm | Identifier | Used to link together a block of related records in a single domain for a subject. |
| `PESPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. Perhaps preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF. |
| `PETESTCD` | Body System Examined Short Name | Char | Req | Topic | Short name of a part of the body examined in a physical examination. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "HEAD", "ENT". If the results of the entire physical examination are represented in one record, value should be "PHYSEXAM". |
| `PETEST` | Body System Examined | Char | Req | Synonym Qualifier | Long name of a part of the body examined in a physical examination. The value in PETEST cannot be longer than 40 characters. Examples: "Head", "Ear/Nose/Throat". If the results of the entire physical examination are represented in one record, value should be "Physical Examination". |
| `PEMODIFY` | Modified Reported Term | Char | Perm | Synonym Qualifier | If the value of PEORRES is modified for coding purposes, then the modified text is placed here. |
| `PECAT` | Category for Examination | Char | Perm | Grouping Qualifier | Used to define a category of topic-variable values. Example: "GENERAL". |
| `PESCAT` | Subcategory for Examination | Char | Perm | Grouping Qualifier | Used to define a further categorization of --CAT values. |
| `PEBODSYS` | Body System or Organ Class | Char | Perm | Record Qualifier | Body system or organ class (e.g., MedDRA SOC) that is involved for a finding from the standard hierarchy for dictionary-coded results. |
| `PEORRES` | Verbatim Examination Finding | Char | Exp | Result Qualifier | Text description of any abnormal findings. If the examination was completed and there were no abnormal findings, the value should be "NORMAL". If the examination was not performed on a particular body system, or at the subject level, then the value should be null, and "NOT DONE" should appear in PESTAT. |
| `PEORRESU` | Original Units | Char | Perm | Variable Qualifier | Original units in which the data were collected. The unit for PEORRES. |
| `PESTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | If there are findings for a body system, then either the dictionary preferred term (if findings are coded using a dictionary) or PEORRES (if findings are not encoded) should appear here. If PEORRES is null, PESTRESC must be null. |
| `PESTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate exam not done. Must be null if a result exists in PEORRES/PESTRESC. |
| `PEREASND` | Reason Not Examined | Char | Perm | Record Qualifier | Describes why an examination was not performed or why a body system was not examined. Example: "SUBJECT REFUSED". Used in conjunction with PESTAT when value is "NOT DONE". |
| `PELOC` | Location of Physical Exam Finding | Char | Perm | Record Qualifier | Anatomical location of the subject relevant to the collection of the measurement. Example: "ARM" for skin rash. |
| `PELAT` | Laterality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing laterallity. Examples: "RIGHT", "LEFT", "BILATERAL". |
| `PEMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method of the test or examination. Examples: "PALPATION", "PERCUSSION". |
| `PELOBXFL` | Last Observation Before Exposure Flag | Char | Perm | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| `PEBLFL` | Baseline Flag | Char | Perm | Record Qualifier | A baseline defined by the sponsor (could be derived in the same manner as PELOBXFL or ABLFL, but is not required to be). The value should be "Y" or null. Note that PEBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| `PEEVAL` | Evaluator | Char | Perm | Record Qualifier | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Example: "INVESTIGATOR". |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT. Should be an integer. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the observation date/time of the physical exam finding. |
| `PEDTC` | Date/Time of Examination | Char | Exp | Timing | Date and time of the physical examination represented in ISO 8601 character format. |
| `PEDY` | Study Day of Examination | Num | Perm | Timing | Study day of physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
