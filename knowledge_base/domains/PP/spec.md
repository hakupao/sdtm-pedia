# PP — Pharmacokinetics Parameters

> Class: Findings | Structure: One record per PK parameter per time-concentration profile per modeling method per subject

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

### PPSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### PPGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain to support relationships within the domain and between domains.

### PPTESTCD
- **Order:** 6
- **Label:** Parameter Short Name
- **Type:** Char
- **Controlled Terms:** C85839
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the pharmacokinetic parameter. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PPTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PPTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "AUCALL", "TMAX", "CMAX".

### PPTEST
- **Order:** 7
- **Label:** Parameter Name
- **Type:** Char
- **Controlled Terms:** C85493
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Name of the pharmacokinetic parameter. The value in PPTEST cannot be longer than 40 characters. Examples: "AUC All", "Time of CMAX", "Max Conc".

### PPCAT
- **Order:** 8
- **Label:** Parameter Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to define a category of related records. For PP, this should be the name of the analyte in PCTEST whose profile the parameter is associated with.

### PPSCAT
- **Order:** 9
- **Label:** Parameter Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Categorization of the model type used to calculate the PK parameters. Examples: "COMPARTMENTAL", "NON-COMPARTMENTAL".

### PPORRES
- **Order:** 10
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### PPORRESU
- **Order:** 11
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C85494; C128684; C128683; C128685; C128686
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for PPORRES. Example: "ng/L". See PP Assumption 3.

### PPSTRESC
- **Order:** 12
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from PPORRES in a standard format or standard units. PPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in PPSTRESN.

### PPSTRESN
- **Order:** 13
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from PPSTRESC. PPSTRESN should store all numeric test results or findings.

### PPSTRESU
- **Order:** 14
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C85494; C128684; C128683; C128685; C128686
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for PPSTRESC and PPSTRESN. See PP Assumption 3.

### PPSTAT
- **Order:** 15
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a parameter was not calculated. Should be null if a result exists in PPORRES.

### PPREASND
- **Order:** 16
- **Label:** Reason Parameter Not Calculated
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a parameter was not calculated, such as "INSUFFICIENT DATA". Used in conjunction with PPSTAT when value is "NOT DONE".

### PPSPEC
- **Order:** 17
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Defines the type of specimen used for a measurement. If multiple specimen types are used for a calculation (e.g., serum and urine for renal clearance), then this field should be left blank. Examples: "SERUM", "PLASMA", "URINE".

### PPANMETH
- **Order:** 18
- **Label:** Analysis Method
- **Type:** Char
- **Controlled Terms:** C172330
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result. Example: A named formula used to calculate AUC, such as "LIN-LOG TRAPEZOIDAL METHOD".  Sponsor-defined formulas can also be represented by this variable. Example: Calculating ratio AUCs where the PPANMETH may be "DRUG METABOLITE 1 TO DRUG PARENT" or "DRUG METABOLITE 2 TO METABOLITE 1".

### TAETORD
- **Order:** 19
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 20
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### PPDTC
- **Order:** 21
- **Label:** Date/Time of Parameter Calculations
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Nominal date/time of parameter calculations.

### PPDY
- **Order:** 22
- **Label:** Study Day of Parameter Calculations
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.

### PPTPTREF
- **Order:** 23
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The description of a time point that acts as a fixed reference for a series of planned time points.

### PPRFTDTC
- **Order:** 24
- **Label:** Date/Time of Reference Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of the reference time point from the PC records used to calculate a parameter record. The values in PPRFTDTC should be the same as that in PCRFTDTC for related records.

### PPSTINT
- **Order:** 25
- **Label:** Planned Start of Assessment Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The start of a planned evaluation or assessment interval relative to the time point reference.

### PPENINT
- **Order:** 26
- **Label:** Planned End of Assessment Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The end of a planned evaluation or assessment interval relative to the time point reference.
