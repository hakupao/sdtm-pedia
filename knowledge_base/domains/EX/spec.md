# EX — Exposure

> Class: Interventions | Structure: One record per protocol-specified study treatment, constant-dosing interval, per subject

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

### EXSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### EXGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### EXREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier (e.g., kit number, bottle label, vial identifier).

### EXSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page.

### EXLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains.

### EXLNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related, grouped records across domains.

### EXTRT
- **Order:** 10
- **Label:** Name of Treatment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Name of the protocol-specified study treatment given during the dosing period for the observation.

### EXCAT
- **Order:** 11
- **Label:** Category of Treatment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of EXTRT values.

### EXSCAT
- **Order:** 12
- **Label:** Subcategory of Treatment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of EXCAT values.

### EXDOSE
- **Order:** 13
- **Label:** Dose
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Amount of EXTRT when numeric. Not populated when EXDOSTXT is populated.

### EXDOSTXT
- **Order:** 14
- **Label:** Dose Description
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount of EXTRT when non-numeric. Dosing amounts or a range of dosing information collected in text form. Example: "200-400". Not populated when EXDOSE is populated.

### EXDOSU
- **Order:** 15
- **Label:** Dose Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Units for EXDOSE, EXDOSTOT, or EXDOSTXT representing protocol-specified values. Examples: "ng", "mg", "mg/kg", "mg/m2".

### EXDOSFRM
- **Order:** 16
- **Label:** Dose Form
- **Type:** Char
- **Controlled Terms:** C66726
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dose form for EXTRT. Examples: "TABLET", "LOTION".

### EXDOSFRQ
- **Order:** 17
- **Label:** Dosing Frequency per Interval
- **Type:** Char
- **Controlled Terms:** C71113
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Usually expressed as the number of repeated administrations of EXDOSE within a specific time period. Examples: "Q2H", "QD", "BID".

### EXDOSRGM
- **Order:** 18
- **Label:** Intended Dose Regimen
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the intended schedule or regimen for the Intervention. Example: "TWO WEEKS ON, TWO WEEKS OFF".

### EXROUTE
- **Order:** 19
- **Label:** Route of Administration
- **Type:** Char
- **Controlled Terms:** C66729
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Route of administration for the intervention. Examples: "ORAL", "INTRAVENOUS".

### EXLOT
- **Order:** 20
- **Label:** Lot Number
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Lot number of the intervention product.

### EXLOC
- **Order:** 21
- **Label:** Location of Dose Administration
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Specifies location of administration. Examples: "ARM", "LIP".

### EXLAT
- **Order:** 22
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location further detailing laterality of the intervention administration. Examples: "LEFT", "RIGHT".

### EXDIR
- **Order:** 23
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL", "UPPER".

### EXFAST
- **Order:** 24
- **Label:** Fasting Status
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify fasting status. Examples: "Y", "N".

### EXADJ
- **Order:** 25
- **Label:** Reason for Dose Adjustment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes reason or explanation of why a dose is adjusted.

### TAETORD
- **Order:** 26
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 27
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Trial epoch of the exposure record. Examples: "RUN-IN", "TREATMENT".

### EXSTDTC
- **Order:** 28
- **Label:** Start Date/Time of Treatment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** The date/time when administration of the treatment indicated by EXTRT and EXDOSE began.

### EXENDTC
- **Order:** 29
- **Label:** End Date/Time of Treatment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** The date/time when administration of the treatment indicated by EXTRT and EXDOSE ended. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, EXSTDTC should be copied to EXENDTC as the standard representation.

### EXSTDY
- **Order:** 30
- **Label:** Study Day of Start of Treatment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of EXSTDTC relative to DM.RFSTDTC.

### EXENDY
- **Order:** 31
- **Label:** Study Day of End of Treatment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of EXENDTC relative to DM.RFSTDTC.

### EXDUR
- **Order:** 32
- **Label:** Duration of Treatment
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration of administration. Used only if collected on the CRF and not derived from start and end date/times.

### EXTPT
- **Order:** 33
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when administration should occur. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See EXTPTNUM and EXTPTREF.

### EXTPTNUM
- **Order:** 34
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of EXTPT to aid in sorting.

### EXELTM
- **Order:** 35
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to the planned fixed reference (EXTPTREF). This variable is useful where there are repetitive measures. Not a clock time.

### EXTPTREF
- **Order:** 36
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by EXELTM, EXTPTNUM, and EXTPT. Examples: PREVIOUS DOSE, PREVIOUS MEAL.

### EXRFTDTC
- **Order:** 37
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by EXTPTREF.
