# SDTM IG v3.4 Variables - TS Domain

**Domain Code:** `TS`

**Total Variables:** 11

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `TSSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness within a parameter. Allows inclusion of multiple records for the same TSPARMCD. |
| `TSGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a group of related records. |
| `TSPARMCD` | Trial Summary Parameter Short Name | Char | Req | Topic | TSPARMCD (the companion to TSPARM) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that TSPARMCD will need to serve as variable names. Examples: "AGEMIN", "AGEMAX". |
| `TSPARM` | Trial Summary Parameter | Char | Req | Synonym Qualifier | Term for the trial summary parameter. The value in TSPARM cannot be longer than 40 characters. Examples: "Planned Minimum Age of Subjects", "Planned Maximum Age of Subjects". |
| `TSVAL` | Parameter Value | Char | Exp | Result Qualifier | Value of TSPARM. Example: "ASTHMA" when TSPARM value is "Trial Indication". TSVAL can only be null when TSVALNF is populated. Text over 200 characters can be added to additional columns TSVAL1-TSVALn. See Assumption 8. |
| `TSVALNF` | Parameter Value Null Flavor | Char | Perm | Result Qualifier | Null flavor for the value of TSPARM, to be populated only if TSVAL is null. |
| `TSVALCD` | Parameter Value Code | Char | Exp | Result Qualifier | This is the code of the term in TSVAL. For example, "6CW7F3G59X" is the code for gabapentin; "C49488" is the code for Y. The length of this variable can be longer than 8 to accommodate the length of the external terminology. |
| `TSVCDREF` | Name of the Reference Terminology | Char | Exp | Result Qualifier | The name of the reference terminology from which TSVALCD is taken. For example; CDISC CT, SNOMED, ISO 8601. |
| `TSVCDVER` | Version of the Reference Terminology | Char | Exp | Result Qualifier | The version number of the reference terminology, if applicable. |
