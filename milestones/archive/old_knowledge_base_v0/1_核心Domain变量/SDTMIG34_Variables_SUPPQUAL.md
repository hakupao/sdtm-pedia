# SDTM IG v3.4 Variables - SUPPQUAL Domain

**Domain Code:** `SUPPQUAL`

**Total Variables:** 10

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Study identifier of the parent record(s). |
| `RDOMAIN` | Related Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain of the parent record(s). |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. This is the value of USUBJID in the parent record(s). |
| `IDVAR` | Identifying Variable | Char | Exp | Identifier | Identifying variable in the dataset that identifies the related record(s). Examples: --SEQ, --GRPID. |
| `IDVARVAL` | Identifying Variable Value | Char | Exp | Identifier | Value of identifying variable of the parent record(s). |
| `QNAM` | Qualifier Variable Name | Char | Req | Topic | The short name of the qualifier variable, which is used as a column name in a domain view with data from the parent domain. The value in QNAM cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). QNAM cannot contain characters other than letters, numbers, or underscores. This will often be the column name in the sponsor's operational dataset. |
| `QLABEL` | Qualifier Variable Label | Char | Req | Synonym Qualifier | This is the long name or label associated with QNAM. The value in QLABEL cannot be longer than 40 characters. This will often be the column label in the sponsor's original dataset. |
| `QVAL` | Data Value | Char | Req | Result Qualifier | Result of, response to, or value associated with QNAM. A value for this column is required; no records can be in SUPP-- with a null value for QVAL. |
| `QORIG` | Origin | Char | Req | Record Qualifier | Because QVAL can represent a mixture of collected (on a CRF), derived, or assigned items, QORIG is used to indicate the origin of this data. Examples: "CRF", "Assigned", "Derived". See Section 4.1.8, Origin Metadata. |
| `QEVAL` | Evaluator | Char | Exp | Record Qualifier | Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain objectively collected or derived data. Examples: "ADJUDICATION COMMITTEE", "STATISTICIAN", "DATABASE ADMINISTRATOR", "CLINICAL COORDINATOR". |
