# SDTM IG v3.4 Variables - AG Domain

**Domain Code:** `AG`

**Total Variables:** 41

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `AGSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `AGGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `AGSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the procedure or test page. |
| `AGLNKID` | Link ID | Char | Perm | Identifier | Identifier used to link related records across domains.This may be a one-to-one or a one-to-many relationship. |
| `AGLNKGRP` | Link Group ID | Char | Perm | Identifier | Identifier used to link related records across domains.This will usually be a many-to-one relationship. |
| `AGTRT` | Reported Agent Name | Char | Req | Topic | Verbatim medication name that is either preprinted or collected on a CRF. |
| `AGMODIFY` | Modified Reported Name | Char | Perm | Synonym Qualifier | If AGTRT is modified to facilitate coding, then AGMODIFY will contain the modified text. |
| `AGDECOD` | Standardized Agent Name | Char | Perm | Synonym Qualifier | Standardized or dictionary-derived text description of AGTRT or AGMODIFY. Equivalent to the generic medication name in WHO Drug. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. If an intervention term does not have a decode value in the dictionary, then AGDECOD will be left blank. |
| `AGCAT` | Category for Agent | Char | Perm | Grouping Qualifier | Used to define a category of agent. Examples: "CHALLENGE AGENT", "PET TRACER". |
| `AGSCAT` | Subcategory for Agent | Char | Perm | Grouping Qualifier | Further categorization of agent. |
| `AGPRESP` | AG Pre-Specified | Char | Perm | Variable Qualifier | Used to indicate whether ("Y"/null) information about the use of a specific agent was solicited on the CRF. |
| `AGOCCUR` | AG Occurrence | Char | Perm | Record Qualifier | When the use of specific agent is solicited, AGOCCUR is used to indicate whether ("Y"/"N") use of the agent occurred. Values are null for agents not specifically solicited. |
| `AGSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a question about a prespecified agent was not answered. Should be null or have a value of "NOT DONE". |
| `AGREASND` | Reason Procedure Agent Not Collected | Char | Perm | Record Qualifier | Describes the reason a response to a question about the occurrence of a procedure agent was not collected. Used in conjunction with AGSTAT when value is "NOT DONE". |
| `AGCLAS` | Agent Class | Char | Perm | Variable Qualifier | Drug class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, follow guidance in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit AGCLAS. |
| `AGCLASCD` | Agent Class Code | Char | Perm | Variable Qualifier | Class code corresponding to AGCLAS. Drug class. May be obtained from coding. When coding to a single class, populate with class code. If using a dictionary and coding to multiple classes, follow guidance in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit AGCLASCD. |
| `AGDOSE` | Dose per Administration | Num | Perm | Record Qualifier | Amount of AGTRT taken. |
| `AGDOSTXT` | Dose Description | Char | Perm | Record Qualifier | Dosing amounts or a range of dosing information collected in text form. Units may be stored in AGDOSU. Examples: "200-400", "15-20". |
| `AGDOSU` | Dose Units | Char | Perm | Variable Qualifier | Units for AGDOSE and AGDOSTXT. Examples: "ng", "mg", "mg/kg". |
| `AGDOSFRM` | Dose Form | Char | Perm | Variable Qualifier | Dose form for AGTRT. Examples: "TABLET", "AEROSOL". |
| `AGDOSFRQ` | Dosing Frequency per Interval | Char | Perm | Record Qualifier | Usually expressed as the number of repeated administrations of AGDOSE within a specific time period. Example: "ONCE". |
| `AGROUTE` | Route of Administration | Char | Perm | Variable Qualifier | Route of administration for AGTRT. Example: "ORAL". |
| `VISITNUM` | Visit Number | Num | Exp | Timing | 1. Clinical encounter number. \n 2. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | 1. Protocol-defined description of clinical encounter. \n 2. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the agent administration started. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the agent administration started. |
| `AGSTDTC` | Start Date/Time of Agent | Char | Perm | Timing | The date/time when administration of the treatment indicated by AGTRT and the dosing variables began. |
| `AGENDTC` | End Date/Time of Agent | Char | Perm | Timing | The date/time when administration of the treatment indicated by AGTRT and the dosing variables ended. |
| `AGSTDY` | Study Day of Start of Agent | Num | Perm | Timing | Study day of start of agent relative to the sponsor-defined RFSTDTC. |
| `AGENDY` | Study Day of End of Agent | Num | Perm | Timing | Study day of end of agent relative to the sponsor-defined RFSTDTC. |
| `AGDUR` | Duration of Agent | Char | Perm | Timing | Collected duration for an agent episode. Used only if collected on the CRF and not derived from start and end date/times. |
| `AGSTRF` | Start Relative to Reference Period | Char | Perm | Timing | Describes the start of the agent relative to sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into AGSTRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `AGENRF` | End Relative to Reference Period | Char | Perm | Timing | Describes the end of the agent relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into AGENRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `AGSTRTPT` | Start Relative to Reference Time Point | Char | Perm | Timing | Identifies the start of the agent as being before or after the sponsor-defined reference time point defined by variable AGSTTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `AGSTTPT` | Start Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the reference point referred to by AGSTRTPT. Examples: "2003-12-15", "VISIT 1". |
| `AGENRTPT` | End Relative to Reference Time Point | Char | Perm | Timing | Identifies the end of the agent as being before or after the reference time point defined by variable AGENTPT. Identifies the end of the agent as being before or after the sponsor-defined reference time point defined by variable AGENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `AGENTPT` | End Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the reference point referred to by AGENRTPT. Examples: "2003-12-25", "VISIT 2". |
