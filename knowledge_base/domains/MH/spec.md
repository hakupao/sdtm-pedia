# MH — Medical History

> Class: Events | Structure: One record per medical history event per subject

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

### MHSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### MHGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### MHREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external medical history identifier.

### MHSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Medical History CRF page.

### MHTERM
- **Order:** 8
- **Label:** Reported Term for the Medical History
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim or preprinted CRF term for the medical condition or event.

### MHMODIFY
- **Order:** 9
- **Label:** Modified Reported Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** If MHTERM is modified to facilitate coding, then MHMODIFY will contain the modified text.

### MHDECOD
- **Order:** 10
- **Label:** Dictionary-Derived Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Dictionary-derived text description of MHTERM or MHMODIFY. Equivalent to the Preferred Term (PT in MedDRA). The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.

### MHEVDTYP
- **Order:** 11
- **Label:** Medical History Event Date Type
- **Type:** Char
- **Controlled Terms:** C124301
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Specifies the aspect of the medical condition or event by which MHSTDTC and/or the MHENDTC is defined. Examples: "DIAGNOSIS", "SYMPTOMS", "RELAPSE", "INFECTION".

### MHCAT
- **Order:** 12
- **Label:** Category for Medical History
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records. Examples: "CARDIAC", "GENERAL".

### MHSCAT
- **Order:** 13
- **Label:** Subcategory for Medical History
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the condition or event.

### MHPRESP
- **Order:** 14
- **Label:** Medical History Event Pre-Specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A value of "Y" indicates that this medical history event was prespecified on the CRF. Values are null for spontaneously reported events (i.e., those collected as free-text verbatim terms).

### MHOCCUR
- **Order:** 15
- **Label:** Medical History Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used when the occurrence of specific medical history conditions is solicited, to indicate whether ("Y"/"N") a medical condition (MHTERM) had ever occurred. Values are null for spontaneously reported events.

### MHSTAT
- **Order:** 16
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The status indicates that the prespecified question was not asked/answered.

### MHREASND
- **Order:** 17
- **Label:** Reason Medical History Not Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the reason why data for a prespecified condition was not collected. Used in conjunction with MHSTAT when value is "NOT DONE".

### MHBODSYS
- **Order:** 18
- **Label:** Body System or Organ Class
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Dictionary-derived. Body system or organ class that is involved in an event or measurement from a standard hierarchy (e.g., MedDRA). When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables which may not necessarily be the primary SOC.

### TAETORD
- **Order:** 19
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 20
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the medical history event.

### MHDTC
- **Order:** 21
- **Label:** Date/Time of History Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time of the medical history observation represented in ISO 8601 character format.

### MHSTDTC
- **Order:** 22
- **Label:** Start Date/Time of Medical History Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Start date/time of the medical history event represented in ISO 8601 character format.

### MHENDTC
- **Order:** 23
- **Label:** End Date/Time of Medical History Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the medical history event.

### MHDY
- **Order:** 24
- **Label:** Study Day of History Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of medical history collection, measured as integer day. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.

### MHENRF
- **Order:** 25
- **Label:** End Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### MHENRTPT
- **Order:** 26
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the event as being before or after the reference time point defined by variable MHENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### MHENTPT
- **Order:** 27
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the reference point referred to by MHENRTPT. Examples: "2003-12-25", "VISIT 2".
