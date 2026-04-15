# HO — Healthcare Encounters

> Class: Events | Structure: One record per healthcare encounter per subject

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

### HOSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### HOGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### HOREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external healthcare encounter identifier.

### HOSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Healthcare Encounters CRF page.

### HOTERM
- **Order:** 8
- **Label:** Healthcare Encounter Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim or preprinted CRF term for the healthcare encounter.

### HODECOD
- **Order:** 9
- **Label:** Dictionary-Derived Term
- **Type:** Char
- **Controlled Terms:** C171444
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Dictionary or sponsor-defined derived text description of HOTERM or the modified topic variable (HOMODIFY).

### HOCAT
- **Order:** 10
- **Label:** Category for Healthcare Encounter
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-related values.

### HOSCAT
- **Order:** 11
- **Label:** Subcategory for Healthcare Encounter
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of HOCAT values.

### HOPRESP
- **Order:** 12
- **Label:** Pre-Specified Healthcare Encounter
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A value of "Y" indicates that this healthcare encounter event was prespecified on the CRF. Values are null for spontaneously reported events (i.e., those collected as free-text verbatim terms).

### HOOCCUR
- **Order:** 13
- **Label:** Healthcare Encounter Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used when the occurrence of specific healthcare encounters is solicited, to indicate whether an encounter occurred. Values are null for spontaneously reported events.

### HOSTAT
- **Order:** 14
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The status indicates that the prespecified question was not answered.

### HOREASND
- **Order:** 15
- **Label:** Reason Healthcare Encounter Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the reason data for a prespecified event were not collected. Used in conjunction with HOSTAT when value is "NOT DONE".

### TAETORD
- **Order:** 16
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 17
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the healthcare encounter. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP".

### HODTC
- **Order:** 18
- **Label:** Date/Time of Event Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time of the healthcare encounter.

### HOSTDTC
- **Order:** 19
- **Label:** Start Date/Time of Healthcare Encounter
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of the healthcare encounter (e.g., date of admission).

### HOENDTC
- **Order:** 20
- **Label:** End Date/Time of Healthcare Encounter
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the healthcare encounter (e.g., date of discharge).

### HODY
- **Order:** 21
- **Label:** Study Day of Event Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of event collection relative to the sponsor-defined RFSTDTC.

### HOSTDY
- **Order:** 22
- **Label:** Study Day of Start of Encounter
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the start of the healthcare encounter relative to the sponsor-defined RFSTDTC.

### HOENDY
- **Order:** 23
- **Label:** Study Day of End of Healthcare Encounter
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the end of the healthcare encounter relative to the sponsor-defined RFSTDTC.

### HODUR
- **Order:** 24
- **Label:** Duration of Healthcare Encounter
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration of the healthcare encounter. Used only if collected on the CRF and not derived from the start and end date/times. Example: "P1DT2H" (for 1 day, 2 hours).

### HOSTRTPT
- **Order:** 25
- **Label:** Start Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the start of the observation as being before or after the sponsor-defined reference time point defined by variable --STTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### HOSTTPT
- **Order:** 26
- **Label:** Start Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by STRTPT. Examples: "2003-12-15", "VISIT 1".

### HOENRTPT
- **Order:** 27
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the event as being before or after the reference time point defined by variable HOENTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### HOENTPT
- **Order:** 28
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the reference point referred to by HOENRTPT. Examples: "2003-12-25", "VISIT 2".
