# SDTM IG v3.4 Variables - CO Domain

**Domain Code:** `CO`

**Total Variables:** 13

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `RDOMAIN` | Related Domain Abbreviation | Char | Perm | Record Qualifier | Two-character abbreviation for the domain of the parent record(s). Null for comments collected on a general comments or additional information CRF page. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `COSEQ` | Sequence Number | Num | Req | Identifier | Sequence Number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `IDVAR` | Identifying Variable | Char | Perm | Record Qualifier | Identifying variable in the parent dataset that identifies the record(s) to which the comment applies. Examples AESEQ or CMGRPID. Used only when individual comments are related to domain records. Null for comments collected on separate CRFs. |
| `IDVARVAL` | Identifying Variable Value | Char | Perm | Record Qualifier | Value of identifying variable of the parent record(s). Used only when individual comments are related to domain records. Null for comments collected on separate CRFs. |
| `COREF` | Comment Reference | Char | Perm | Record Qualifier | Sponsor-defined reference associated with the comment. May be the CRF page number (e.g., 650), or a module name (e.g., DEMOG), or a combination of information that identifies the reference (e.g. 650-VITALS-VISIT 2). |
| `COVAL` | Comment | Char | Req | Topic | The text of the comment. Text over 200 characters can be added to additional columns COVAL1-COVALn. See Assumption 3. |
| `COEVAL` | Evaluator | Char | Perm | Record Qualifier | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Example: "INVESTIGATOR". |
| `COEVALID` | Evaluator Identifier | Char | Perm | Record Qualifier | Used to distinguish multiple evaluators with the same role recorded in --EVAL. Examples: "RADIOLOGIST", "RADIOLOGIST 1", "RADIOLOGIST 2". |
| `CODTC` | Date/Time of Comment | Char | Perm | Timing | Date/time of comment on dedicated comment form. Should be null if this is a child record of another domain or if comment date was not collected. |
| `CODY` | Study Day of Comment | Num | Perm | Timing | Study day of the comment, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. |
