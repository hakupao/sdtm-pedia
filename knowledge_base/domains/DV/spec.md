# DV — Protocol Deviations

> Class: Events | Structure: One record per protocol deviation per subject

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

### DVSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### DVREFID
- **Order:** 5
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier.

### DVSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page.

### DVTERM
- **Order:** 7
- **Label:** Protocol Deviation Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim name of the protocol deviation criterion. Example: "IVRS PROCESS DEVIATION - NO DOSE CALL PERFORMED". DVTERM values will map to the controlled terminology in DVDECOD (e.g., "TREATMENT DEVIATION").

### DVDECOD
- **Order:** 8
- **Label:** Protocol Deviation Coded Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Controlled terminology for the name of the protocol deviation. Examples: "SUBJECT NOT WITHDRAWN AS PER PROTOCOL", "SELECTION CRITERIA NOT MET", "EXCLUDED CONCOMITANT MEDICATION", "TREATMENT DEVIATION".

### DVCAT
- **Order:** 9
- **Label:** Category for Protocol Deviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Category of the protocol deviation criterion.

### DVSCAT
- **Order:** 10
- **Label:** Subcategory for Protocol Deviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the protocol deviation.

### TAETORD
- **Order:** 11
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 12
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the deviation. Examples: "TREATMENT", "SCREENING", "FOLLOW-UP".

### DVSTDTC
- **Order:** 13
- **Label:** Start Date/Time of Deviation
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Start date/time of deviation represented in ISO 8601 character format.

### DVENDTC
- **Order:** 14
- **Label:** End Date/Time of Deviation
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of deviation represented in ISO 8601 character format.

### DVSTDY
- **Order:** 15
- **Label:** Study Day of Start of Deviation Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of start of event relative to the sponsor-defined RFSTDTC.

### DVENDY
- **Order:** 16
- **Label:** Study Day of End of Deviation Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of end of event relative to the sponsor-defined RFSTDTC.
