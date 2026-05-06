# SDTM IG v3.4 Variables - TU Domain

**Domain Code:** `TU`

**Total Variables:** 31

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `TUSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number. |
| `TUGRPID` | Group ID | Char | Perm | Identifier | Used to link together a block of related records within a subject in a domain. Can be used to group split or merged tumors/lesions which have been identified. |
| `TUREFID` | Reference ID | Char | Perm | Identifier | Internal or external identifier (e.g., medical image ID number). |
| `TUSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. |
| `TULNKID` | Link ID | Char | Exp | Identifier | Identifier used to link identified tumor/lesion/location of interest to the assessment results (in TR domain) over the course of the study. |
| `TULNKGRP` | Link Group ID | Char | Perm | Identifier | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| `TUTESTCD` | Tumor/Lesion ID Short Name | Char | Req | Topic | Short name of the TEST in TUTEST. TUTESTCD cannot be longer than 8 characters nor can start with a number. TUTESTCD cannot contain characters other than letters, numbers, or underscores. Example: "TUMIDENT". See assumption 3. |
| `TUTEST` | Tumor/Lesion ID Test Name | Char | Req | Synonym Qualifier | Verbatim name of the test for the tumor/lesion identification. The value in TUTEST cannot be longer than 40 characters. Example: "Tumor identification". See assumption 3. |
| `TUORRES` | Tumor/Lesion ID Result | Char | Exp | Result Qualifier | Result of the tumor/lesion identification. The result of tumor/lesion identification is a classification of the identified tumor/lesion. Example: When TUTESTCD = "TUMIDENT", values of TUORRES might be "TARGET", "NON-TARGET", "NEW", or "BENIGN ABNORMALITY". |
| `TUSTRESC` | Tumor/Lesion ID Result Std. Format | Char | Exp | Result Qualifier | Contains the result value for all findings copied or derived from TUORRES in a standard format. |
| `TUNAM` | Laboratory/Vendor Name | Char | Perm | Record Qualifier | The name or identifier of the vendor that performed the tumor/lesion Identification. This column can be left null when the investigator provides the complete set of data in the domain. |
| `TULOC` | Location of the Tumor/Lesion | Char | Exp | Record Qualifier | Used to specify the anatomical location of the identified tumor/lesion (e.g., "LIVER"). \n Note: When anatomical location is broken down and collected as distinct pieces of data that when combined provide the overall location information (e.g., laterality/directionality/distribution), then additional anatomical location qualifiers should be used. See assumption 3. |
| `TULAT` | Laterality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing laterality (e.g., "LEFT", "RIGHT", "BILATERAL"). |
| `TUDIR` | Directionality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing directionality (e.g., "UPPER", "INTERIOR"). |
| `TUPORTOT` | Portion or Totality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing the distribution, which means arrangement of, or apportioning of. Examples: "ENTIRE", "SINGLE", "SEGMENT", "MULTIPLE". |
| `TUMETHOD` | Method of Identification | Char | Exp | Record Qualifier | Method used to identify the tumor/lesion. Examples: "MRI", "CT SCAN". |
| `TULOBXFL` | Last Observation Before Exposure Flag | Char | Exp | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| `TUBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be "Y" or null. Note that TUBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| `TUEVAL` | Evaluator | Char | Exp | Record Qualifier | Role of the person who provided the evaluation. Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR". \n This column can be left null when the investigator provides the complete set of data in the domain. However, the column should contain no null values when data from 1 or more independent assessors is included. For example, the rows attributed to the investigator should contain a value of "INVESTIGATOR". |
| `TUEVALID` | Evaluator Identifier | Char | Perm | Variable Qualifier | Used to distinguish multiple evaluators with the same role recorded in --EVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumption 9. |
| `TUACPTFL` | Accepted Record Flag | Char | Perm | Record Qualifier | In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATION COMMITTEE") provide independent assessments at the same time point, this flag identifies the record that is considered to be the accepted assessment. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. Should be an integer. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the date/time at which the assessment was made. |
| `TUDTC` | Date/Time of Tumor/Lesion Identification | Char | Exp | Timing | TUDTC variable represents the date of the scan/image/physical exam. TUDTC does not represent the date that the image was read to identify tumors. TUDTC also does not represent the VISIT date. |
| `TUDY` | Study Day of Tumor/Lesion Identification | Num | Perm | Timing | Study day of the scan/image/physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
