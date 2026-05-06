# SDTM IG v3.4 Variables - BE Domain

**Domain Code:** `BE`

**Total Variables:** 25

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `SPDEVID` | Sponsor Device Identifier | Char | Perm | Identifier | Sponsor-defined identifier for a device. |
| `BESEQ` | Sequence Number | Num | Req | Identifier | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| `BEGRPID` | Group ID | Char | Perm | Identifier | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| `BEREFID` | Reference ID | Char | Exp | Identifier | Internal or external identifier for the specimen affected or created by the event. |
| `BESPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Optional sponsor-defined reference number. Example: Line number on a CRF page. |
| `BETERM` | Reported Term for the Biospecimen Event | Char | Req | Topic | Topic variable for an event observation, which is the verbatim or pre-specified name of the event. |
| `BEMODIFY` | Modified Reported Term | Char | Perm | Synonym Qualifier | If the value for BETERM is modified for coding purposes, then the modified text is placed here. |
| `BEDECOD` | Dictionary-Derived Term | Char | Perm | Synonym Qualifier | Dictionary-derived text description of BETERM or BEMODIFY, if applicable. |
| `BECAT` | Category for Biospecimen Event | Char | Perm | Grouping Qualifier | Used to define a category of topic-variable values. Example: COLLECTION, PREPARATION, TRANSPORT. |
| `BESCAT` | Subcategory for Biospecimen Event | Char | Perm | Grouping Qualifier | A further categorization of BECAT values. |
| `BELOC` | Anatomical Location of Event | Char | Perm | Record Qualifier | Describes the anatomical location relevant for the event (e.g. BRAIN, LUNG). |
| `BEPARTY` | Accountable Party | Char | Perm | Record Qualifier | Party accountable for the transferable object (e.g. specimen) as a result of the activity performed in the associated BETERM variable. The party could be an individual (e.g., subject), an organization (e.g., sponsor), or a location that is a proxy for an individual or organization (e.g., site). It is usually a somewhat general term that is further identified in the BEPRTYID variable. |
| `BEPRTYID` | Identification of Accountable Party | Char | Perm | Record Qualifier | Identification of the specific party accountable for the transferable object (e.g. Specimen) after the action in BETERM is taken. Used in conjunction with BEPARTY. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT. Should be an integer. |
| `BEDTC` | Date/Time of Specimen Collection | Char | Exp | Timing | Date and time of specimen collection. |
| `BESTDTC` | Start Date/Time of Biospecimen Event | Char | Exp | Timing | Start date/time of the event. |
| `BEENDTC` | End Date/Time of Biospecimen Event | Char | Exp | Timing | End date/time of the event. |
| `BESTDY` | Study Day of Start of Biospecimen Event | Num | Perm | Timing | Actual study day of start of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `BEENDY` | Study Day of End of Biospecimen Event | Num | Perm | Timing | Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `BEDUR` | Duration of Biospecimen Event | Char | Perm | Timing | Collected duration and unit of a biospecimen event. Used only if collected on the CRF and not derived from start and end date/times. Example: P1DT2H (for 1 day, 2 hours). |
