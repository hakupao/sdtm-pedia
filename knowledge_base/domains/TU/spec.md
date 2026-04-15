# TU — Tumor/Lesion Identification

> Class: Findings | Structure: One record per identified tumor per subject per assessor

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### TUSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number.

### TUGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records within a subject in a domain. Can be used to group split or merged tumors/lesions which have been identified.

### TUREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier (e.g., medical image ID number).

### TUSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### TULNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Identifier used to link identified tumor/lesion/location of interest to the assessment results (in TR domain) over the course of the study.

### TULNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### TUTESTCD
- **Order:** 10
- **Label:** Tumor/Lesion ID Short Name
- **Type:** Char
- **Controlled Terms:** C96784
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the TEST in TUTEST. TUTESTCD cannot be longer than 8 characters nor can start with a number. TUTESTCD cannot contain characters other than letters, numbers, or underscores. Example: "TUMIDENT". See assumption 3.

### TUTEST
- **Order:** 11
- **Label:** Tumor/Lesion ID Test Name
- **Type:** Char
- **Controlled Terms:** C96783
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test for the tumor/lesion identification. The value in TUTEST cannot be longer than 40 characters. Example: "Tumor identification". See assumption 3.

### TUORRES
- **Order:** 12
- **Label:** Tumor/Lesion ID Result
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the tumor/lesion identification. The result of tumor/lesion identification is a classification of the identified tumor/lesion. Example: When TUTESTCD = "TUMIDENT", values of TUORRES might be "TARGET", "NON-TARGET", "NEW", or "BENIGN ABNORMALITY".

### TUSTRESC
- **Order:** 13
- **Label:** Tumor/Lesion ID Result Std. Format
- **Type:** Char
- **Controlled Terms:** C123650
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from TUORRES in a standard format.

### TUNAM
- **Order:** 14
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The name or identifier of the vendor that performed the tumor/lesion Identification. This column can be left null when the investigator provides the complete set of data in the domain.

### TULOC
- **Order:** 15
- **Label:** Location of the Tumor/Lesion
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to specify the anatomical location of the identified tumor/lesion (e.g., "LIVER").  Note: When anatomical location is broken down and collected as distinct pieces of data that when combined provide the overall location information (e.g., laterality/directionality/distribution), then additional anatomical location qualifiers should be used. See assumption 3.

### TULAT
- **Order:** 16
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality (e.g., "LEFT", "RIGHT", "BILATERAL").

### TUDIR
- **Order:** 17
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality (e.g., "UPPER", "INTERIOR").

### TUPORTOT
- **Order:** 18
- **Label:** Portion or Totality
- **Type:** Char
- **Controlled Terms:** C99075
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing the distribution, which means arrangement of, or apportioning of. Examples: "ENTIRE", "SINGLE", "SEGMENT", "MULTIPLE".

### TUMETHOD
- **Order:** 19
- **Label:** Method of Identification
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Method used to identify the tumor/lesion. Examples: "MRI", "CT SCAN".

### TULOBXFL
- **Order:** 20
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.

### TUBLFL
- **Order:** 21
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that TUBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### TUEVAL
- **Order:** 22
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Role of the person who provided the evaluation. Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR".  This column can be left null when the investigator provides the complete set of data in the domain. However, the column should contain no null values when data from 1 or more independent assessors is included. For example, the rows attributed to the investigator should contain a value of "INVESTIGATOR".

### TUEVALID
- **Order:** 23
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in --EVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumption 9.

### TUACPTFL
- **Order:** 24
- **Label:** Accepted Record Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATION COMMITTEE") provide independent assessments at the same time point, this flag identifies the record that is considered to be the accepted assessment.

### VISITNUM
- **Order:** 25
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 26
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 27
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics. Should be an integer.

### TAETORD
- **Order:** 28
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 29
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### TUDTC
- **Order:** 30
- **Label:** Date/Time of Tumor/Lesion Identification
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** TUDTC variable represents the date of the scan/image/physical exam. TUDTC does not represent the date that the image was read to identify tumors. TUDTC also does not represent the VISIT date.

### TUDY
- **Order:** 31
- **Label:** Study Day of Tumor/Lesion Identification
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the scan/image/physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
