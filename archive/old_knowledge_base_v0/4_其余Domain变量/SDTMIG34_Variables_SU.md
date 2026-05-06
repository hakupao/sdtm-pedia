# SDTM IG v3.4 Variables - SU Domain

**Domain Code:** `SU`

**Total Variables:** 37

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `SUSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `SUGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `SUSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Tobacco & Alcohol Use CRF page. |
| `SUTRT` | Reported Name of Substance | Char | Req | Topic | Substance name. Examples: "CIGARETTES", "COFFEE". |
| `SUMODIFY` | Modified Substance Name | Char | Perm | Synonym Qualifier | If SUTRT is modified, then the modified text is placed here. |
| `SUDECOD` | Standardized Substance Name | Char | Perm | Synonym Qualifier | Standardized or dictionary-derived text description of SUTRT or SUMODIFY if the sponsor chooses to code the substance use. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. |
| `SUCAT` | Category for Substance Use | Char | Perm | Grouping Qualifier | Used to define a category of related records. Examples: "TOBACCO", "ALCOHOL", or "CAFFEINE". |
| `SUSCAT` | Subcategory for Substance Use | Char | Perm | Grouping Qualifier | A further categorization of substance use. Examples: "CIGARS", "CIGARETTES", "BEER", "WINE". |
| `SUPRESP` | SU Pre-Specified | Char | Perm | Variable Qualifier | Used to indicate whether ("Y"/null) information about the use of a specific substance was solicited on the CRF. |
| `SUOCCUR` | SU Occurrence | Char | Perm | Record Qualifier | When the use of specific substances is solicited, SUOCCUR is used to indicate whether ("Y"/"N") a particular prespecified substance was used. Values are null for substances not specifically solicited. |
| `SUSTAT` | Completion Status | Char | Perm | Record Qualifier | When the use of prespecified substances is solicited, the completion status indicates that there was no response to the question about the prespecified substance. When there is no prespecified list on the CRF, then the completion status indicates that substance use was not assessed for the subject. |
| `SUREASND` | Reason Substance Use Not Collected | Char | Perm | Record Qualifier | Describes the reason substance use was not collected. Used in conjunction with SUSTAT when value of SUSTAT is "NOT DONE". |
| `SUCLAS` | Substance Use Class | Char | Perm | Variable Qualifier | Substance use class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, then follow Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit SUCLAS. |
| `SUCLASCD` | Substance Use Class Code | Char | Perm | Variable Qualifier | Code corresponding to SUCLAS. May be obtained from coding. |
| `SUDOSE` | Substance Use Consumption | Num | Perm | Record Qualifier | Amount of SUTRT consumed. Not populated if SUDOSTXT is populated. |
| `SUDOSTXT` | Substance Use Consumption Text | Char | Perm | Record Qualifier | Substance use consumption amounts or a range of consumption information collected in text form. Not populated if SUDOSE is populated. |
| `SUDOSU` | Consumption Units | Char | Perm | Variable Qualifier | Units for SUDOSE, SUDOSTOT, or SUDOSTXT. Examples: "oz", "CIGARETTE", "PACK", "g". |
| `SUDOSFRM` | Dose Form | Char | Perm | Variable Qualifier | Dose form for SUTRT. Examples: "INJECTABLE", "LIQUID", "POWDER". |
| `SUDOSFRQ` | Use Frequency Per Interval | Char | Perm | Variable Qualifier | Usually expressed as the number of repeated administrations of SUDOSE within a specific time period. Example: "Q24H" (every day). |
| `SUDOSTOT` | Total Daily Consumption | Num | Perm | Record Qualifier | Total daily use of SUTRT using the units in SUDOSU. Used when dosing is collected as total daily dose. If a sponsor needs to aggregate the data over a period other than daily, then the aggregated total could be recorded in a supplemental qualifier variable. |
| `SUROUTE` | Route of Administration | Char | Perm | Variable Qualifier | Route of administration for SUTRT. Examples: "ORAL", "INTRAVENOUS". |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the substance use started. Null for substances that started before study participation. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the substance use. Null for substances that started before study participation. |
| `SUSTDTC` | Start Date/Time of Substance Use | Char | Perm | Timing | Start date/time of the substance use represented in ISO 8601 character format. |
| `SUENDTC` | End Date/Time of Substance Use | Char | Perm | Timing | End date/time of the substance use represented in ISO 8601 character format. |
| `SUSTDY` | Study Day of Start of Substance Use | Num | Perm | Timing | Study day of start of substance use relative to the sponsor-defined RFSTDTC. |
| `SUENDY` | Study Day of End of Substance Use | Num | Perm | Timing | Study day of end of substance use relative to the sponsor-defined RFSTDTC. |
| `SUDUR` | Duration of Substance Use | Char | Perm | Timing | Collected duration of substance use in ISO 8601 format. Used only if collected on the CRF and not derived from start and end date/times. |
| `SUSTRF` | Start Relative to Reference Period | Char | Perm | Timing | Describes the start of the substance use relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR" was collected, this information may be translated into SUSTRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `SUENRF` | End Relative to Reference Period | Char | Perm | Timing | Describes the end of the substance use with relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into SUENRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `SUSTRTPT` | Start Relative to Reference Time Point | Char | Perm | Timing | Identifies the start of the substance as being before or after the reference time point defined by variable SUSTTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7 , Use of Relative Timing Variables. |
| `SUSTTPT` | Start Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the reference point referred to by SUSTRTPT. Examples: "2003-12-15", "VISIT 1". |
| `SUENRTPT` | End Relative to Reference Time Point | Char | Perm | Timing | Identifies the end of the substance as being before or after the reference time point defined by variable SUENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7 , Use of Relative Timing Variables. |
| `SUENTPT` | End Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the reference point referred to by SUENRTPT. Examples: "2003-12-25", "VISIT 2". |
