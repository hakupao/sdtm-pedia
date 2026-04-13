# AG — Procedure Agents

> Class: Interventions | Structure: One record per recorded intervention occurrence per subject

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

### AGSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### AGGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### AGSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the procedure or test page.

### AGLNKID
- **Order:** 7
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains.This may be a one-to-one or a one-to-many relationship.

### AGLNKGRP
- **Order:** 8
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains.This will usually be a many-to-one relationship.

### AGTRT
- **Order:** 9
- **Label:** Reported Agent Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim medication name that is either preprinted or collected on a CRF.

### AGMODIFY
- **Order:** 10
- **Label:** Modified Reported Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** If AGTRT is modified to facilitate coding, then AGMODIFY will contain the modified text.

### AGDECOD
- **Order:** 11
- **Label:** Standardized Agent Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized or dictionary-derived text description of AGTRT or AGMODIFY. Equivalent to the generic medication name in WHO Drug. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. If an intervention term does not have a decode value in the dictionary, then AGDECOD will be left blank.

### AGCAT
- **Order:** 12
- **Label:** Category for Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of agent. Examples: "CHALLENGE AGENT", "PET TRACER".

### AGSCAT
- **Order:** 13
- **Label:** Subcategory for Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Further categorization of agent.

### AGPRESP
- **Order:** 14
- **Label:** AG Pre-Specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether ("Y"/null) information about the use of a specific agent was solicited on the CRF.

### AGOCCUR
- **Order:** 15
- **Label:** AG Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** When the use of specific agent is solicited, AGOCCUR is used to indicate whether ("Y"/"N") use of the agent occurred. Values are null for agents not specifically solicited.

### AGSTAT
- **Order:** 16
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question about a prespecified agent was not answered. Should be null or have a value of "NOT DONE".

### AGREASND
- **Order:** 17
- **Label:** Reason Procedure Agent Not Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the reason a response to a question about the occurrence of a procedure agent was not collected. Used in conjunction with AGSTAT when value is "NOT DONE".

### AGCLAS
- **Order:** 18
- **Label:** Agent Class
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Drug class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, follow guidance in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit AGCLAS.

### AGCLASCD
- **Order:** 19
- **Label:** Agent Class Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Class code corresponding to AGCLAS. Drug class. May be obtained from coding. When coding to a single class, populate with class code. If using a dictionary and coding to multiple classes, follow guidance in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit AGCLASCD.

### AGDOSE
- **Order:** 20
- **Label:** Dose per Administration
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount of AGTRT taken.

### AGDOSTXT
- **Order:** 21
- **Label:** Dose Description
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Dosing amounts or a range of dosing information collected in text form. Units may be stored in AGDOSU. Examples: "200-400", "15-20".

### AGDOSU
- **Order:** 22
- **Label:** Dose Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Units for AGDOSE and AGDOSTXT. Examples: "ng", "mg", "mg/kg".

### AGDOSFRM
- **Order:** 23
- **Label:** Dose Form
- **Type:** Char
- **Controlled Terms:** C66726
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Dose form for AGTRT. Examples: "TABLET", "AEROSOL".

### AGDOSFRQ
- **Order:** 24
- **Label:** Dosing Frequency per Interval
- **Type:** Char
- **Controlled Terms:** C71113
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Usually expressed as the number of repeated administrations of AGDOSE within a specific time period. Example: "ONCE".

### AGROUTE
- **Order:** 25
- **Label:** Route of Administration
- **Type:** Char
- **Controlled Terms:** C66729
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Route of administration for AGTRT. Example: "ORAL".

### VISITNUM
- **Order:** 26
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** 1. Clinical encounter number. \n 2. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 27
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** 1. Protocol-defined description of clinical encounter. \n 2. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 28
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 29
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the agent administration started.

### EPOCH
- **Order:** 30
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the agent administration started.

### AGSTDTC
- **Order:** 31
- **Label:** Start Date/Time of Agent
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The date/time when administration of the treatment indicated by AGTRT and the dosing variables began.

### AGENDTC
- **Order:** 32
- **Label:** End Date/Time of Agent
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The date/time when administration of the treatment indicated by AGTRT and the dosing variables ended.

### AGSTDY
- **Order:** 33
- **Label:** Study Day of Start of Agent
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of start of agent relative to the sponsor-defined RFSTDTC.

### AGENDY
- **Order:** 34
- **Label:** Study Day of End of Agent
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of end of agent relative to the sponsor-defined RFSTDTC.

### AGDUR
- **Order:** 35
- **Label:** Duration of Agent
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration for an agent episode. Used only if collected on the CRF and not derived from start and end date/times.

### AGSTRF
- **Order:** 36
- **Label:** Start Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the start of the agent relative to sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into AGSTRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### AGENRF
- **Order:** 37
- **Label:** End Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the end of the agent relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into AGENRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### AGSTRTPT
- **Order:** 38
- **Label:** Start Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the start of the agent as being before or after the sponsor-defined reference time point defined by variable AGSTTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### AGSTTPT
- **Order:** 39
- **Label:** Start Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the reference point referred to by AGSTRTPT. Examples: "2003-12-15", "VISIT 1".

### AGENRTPT
- **Order:** 40
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the agent as being before or after the reference time point defined by variable AGENTPT. Identifies the end of the agent as being before or after the sponsor-defined reference time point defined by variable AGENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### AGENTPT
- **Order:** 41
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the reference point referred to by AGENRTPT. Examples: "2003-12-25", "VISIT 2".
