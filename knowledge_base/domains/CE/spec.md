# CE — Clinical Events

> Class: Events | Structure: One record per event per subject

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

### CESEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### CEGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records for a subject within a domain.

### CEREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier (e.g., lab specimen ID, UUID for an ECG waveform or medical image).

### CESPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### CETERM
- **Order:** 8
- **Label:** Reported Term for the Clinical Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Term for the medical condition or event. Most likely preprinted on CRF.

### CEDECOD
- **Order:** 9
- **Label:** Dictionary-Derived Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Controlled terminology for the name of the clinical event. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.

### CECAT
- **Order:** 10
- **Label:** Category for the Clinical Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records.

### CESCAT
- **Order:** 11
- **Label:** Subcategory for the Clinical Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the condition or event.

### CEPRESP
- **Order:** 12
- **Label:** Clinical Event Pre-specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether the event in CETERM was prespecified. Value is "Y" for prespecified events and null for spontaneously reported events.

### CEOCCUR
- **Order:** 13
- **Label:** Clinical Event Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used when the occurrence of specific events is solicited, to indicate whether or not a clinical event occurred. Values are null for spontaneously reported events.

### CESTAT
- **Order:** 14
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The status indicates that a question from a prespecified list was not answered.

### CEREASND
- **Order:** 15
- **Label:** Reason Clinical Event Not Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the reason clinical event data was not collected. Used in conjunction with CESTAT when value is "NOT DONE".

### CEBODSYS
- **Order:** 16
- **Label:** Body System or Organ Class
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Dictionary-derived. Body system or organ class that is involved in an event or measurement from a standard hierarchy (e.g., MedDRA). When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables, which may not necessarily be the primary SOC.

### CESEV
- **Order:** 17
- **Label:** Severity/Intensity
- **Type:** Char
- **Controlled Terms:** C165643
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The severity or intensity of the event. Examples: "MILD", "MODERATE", "SEVERE".

### CETOXGR
- **Order:** 18
- **Label:** Standard Toxicity Grade
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Toxicity grade according to a standard toxicity scale (e.g., Common Terminology Criteria for Adverse Events (CTCAE) v3.0). Sponsor should specify name of the scale and version used in the metadata. If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2").

### TAETORD
- **Order:** 19
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the clinical event started.

### EPOCH
- **Order:** 20
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the clinical event.

### CEDTC
- **Order:** 21
- **Label:** Date/Time of Event Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time for the clinical event observation represented in ISO 8601 character format.

### CESTDTC
- **Order:** 22
- **Label:** Start Date/Time of Clinical Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Start date/time of the clinical event represented in ISO 8601 character format.

### CEENDTC
- **Order:** 23
- **Label:** End Date/Time of Clinical Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the clinical event, represented in ISO 8601 character format.

### CEDY
- **Order:** 24
- **Label:** Study Day of Event Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of clinical event collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.

### CESTDY
- **Order:** 25
- **Label:** Study Day of Start of Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of start of the clinical event expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### CEENDY
- **Order:** 26
- **Label:** Study Day of End of Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of the clinical event expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### CESTRF
- **Order:** 27
- **Label:** Start Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the start of the clinical event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics).  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### CEENRF
- **Order:** 28
- **Label:** End Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics).  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### CESTRTPT
- **Order:** 29
- **Label:** Start Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the start of the observation as being before or after the reference time point defined by variable CESTTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### CESTTPT
- **Order:** 30
- **Label:** Start Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by --STRTPT. Examples: "2003-12-15", "VISIT 1".

### CEENRTPT
- **Order:** 31
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the observation as being before or after the sponsor-defined reference time point defined by variable CEENTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### CEENTPT
- **Order:** 32
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the reference point referred to by CEENRTPT. Examples: "2003-12-25", "VISIT 2".
