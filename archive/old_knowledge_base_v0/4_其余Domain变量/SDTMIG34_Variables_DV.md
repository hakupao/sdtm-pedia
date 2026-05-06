# SDTM IG v3.4 Variables - DV Domain

**Domain Code:** `DV`

**Total Variables:** 16

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `DVSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `DVREFID` | Reference ID | Char | Perm | Identifier | Internal or external identifier. |
| `DVSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page. |
| `DVTERM` | Protocol Deviation Term | Char | Req | Topic | Verbatim name of the protocol deviation criterion. Example: "IVRS PROCESS DEVIATION - NO DOSE CALL PERFORMED". DVTERM values will map to the controlled terminology in DVDECOD (e.g., "TREATMENT DEVIATION"). |
| `DVDECOD` | Protocol Deviation Coded Term | Char | Perm | Synonym Qualifier | Controlled terminology for the name of the protocol deviation. Examples: "SUBJECT NOT WITHDRAWN AS PER PROTOCOL", "SELECTION CRITERIA NOT MET", "EXCLUDED CONCOMITANT MEDICATION", "TREATMENT DEVIATION". |
| `DVCAT` | Category for Protocol Deviation | Char | Perm | Grouping Qualifier | Category of the protocol deviation criterion. |
| `DVSCAT` | Subcategory for Protocol Deviation | Char | Perm | Grouping Qualifier | A further categorization of the protocol deviation. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the deviation. Examples: "TREATMENT", "SCREENING", "FOLLOW-UP". |
| `DVSTDTC` | Start Date/Time of Deviation | Char | Perm | Timing | Start date/time of deviation represented in ISO 8601 character format. |
| `DVENDTC` | End Date/Time of Deviation | Char | Perm | Timing | End date/time of deviation represented in ISO 8601 character format. |
| `DVSTDY` | Study Day of Start of Deviation Event | Num | Perm | Timing | Study day of start of event relative to the sponsor-defined RFSTDTC. |
| `DVENDY` | Study Day of End of Deviation Event | Num | Perm | Timing | Study day of end of event relative to the sponsor-defined RFSTDTC. |
