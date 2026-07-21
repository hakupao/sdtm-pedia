# SDTM IG v3.4 Variables - TR Domain

**Domain Code:** `TR`

**Total Variables:** 32

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `TRSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number. |
| `TRGRPID` | Group ID | Char | Perm | Identifier | Used to link together a block of related records within a subject in a domain. |
| `TRREFID` | Reference ID | Char | Perm | Identifier | Internal or external identifier. |
| `TRSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. |
| `TRLNKID` | Link ID | Char | Exp | Identifier | Identifier used to link the assessment result records to the individual tumor/lesion identification record in TU domain. |
| `TRLNKGRP` | Link Group | Char | Perm | Identifier | Used to group and link all of the measurement/assessment records used in the assessment of the response record in the RS domain. |
| `TRTESTCD` | Tumor/Lesion Assessment Short Name | Char | Req | Topic | Short name of the TEST in TRTEST. TRTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TUMSTATE", "DIAMETER", "LESSCIND", "LESRVIND". See assumption 3. |
| `TRTEST` | Tumor/Lesion Assessment Test Name | Char | Req | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in TRTEST cannot be longer than 40 characters. Examples: "Tumor State", "Diameter", "Volume", "Lesion Success Indicator", "Lesion Revascularization Indicator". See assumption 3. |
| `TRORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the tumor/lesion measurement/assessment as originally received or collected. |
| `TRORRESU` | Original Units | Char | Exp | Variable Qualifier | Original units in which the data were collected. The unit for TRORRES. Example: "mm". |
| `TRSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings copied or derived from TRORRES, in a standard format or standard units. TRSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in TRSTRESN. |
| `TRSTRESN` | Numeric Result/Finding in Standard Units | Num | Exp | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from TRSTRESC. TRSTRESN should store all numeric test results or findings. |
| `TRSTRESU` | Standard Units | Char | Exp | Variable Qualifier | Standardized unit used for TRSTRESN. |
| `TRSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate a scan/image/physical exam was not performed or a tumor/lesion measurement was not taken. Should be null if a result exists in TRORRES. |
| `TRREASND` | Reason Not Done | Char | Perm | Record Qualifier | Describes why a scan/image/physical exam was not performed or a tumor/lesion measurement was not taken. Examples: "SCAN NOT PERFORMED", "NOT ASSESSABLE: IMAGE OBSCURED TUMOR". Used in conjunction with TRSTAT when value is "NOT DONE". |
| `TRNAM` | Laboratory/Vendor Name | Char | Perm | Record Qualifier | The name or identifier of the vendor that performed the tumor/lesion measurement or assessment. This column can be left null when the investigator provides the complete set of data in the domain. |
| `TRMETHOD` | Method Used to Identify the Tumor/Lesion | Char | Exp | Record Qualifier | Method used to measure the tumor/lesion/location of interest. Examples: "MRI", "CT SCAN", "PET SCAN", "Coronary angiography". |
| `TRLOBXFL` | Last Observation Before Exposure Flag | Char | Exp | Record Qualifier | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| `TRBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be "Y" or null. Note that TRBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| `TREVAL` | Evaluator | Char | Exp | Record Qualifier | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR". |
| `TREVALID` | Evaluator Identifier | Char | Perm | Variable Qualifier | Used to distinguish multiple evaluators with the same role recorded in TREVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumption 6. |
| `TRACPTFL` | Accepted Record Flag | Char | Perm | Record Qualifier | In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATION COMMITTEE") provide independent assessments at the same time point, this flag identifies the record that is considered to be the accepted assessment. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Epoch associated with the date/time at which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the element in the planned sequence of elements for the arm to which the subject was assigned. |
| `TRDTC` | Date/Time of Tumor/Lesion Measurement | Char | Exp | Timing | The date of the scan/image/physical exam. TRDTC does not represent the date that the image was read to identify tumors/lesions. TRDTC also does not represent the VISIT date. |
| `TRDY` | Study Day of Tumor/Lesion Measurement | Num | Perm | Timing | Study day of the scan/image/physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
