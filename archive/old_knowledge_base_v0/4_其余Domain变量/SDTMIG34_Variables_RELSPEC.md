# SDTM IG v3.4 Variables - RELSPEC Domain

**Domain Code:** `RELSPEC`

**Total Variables:** 6

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `REFID` | Specimen ID | Char | Req | Identifier | Specimen identifier, unique within USUBJID. |
| `SPEC` | Specimen Type | Char | Perm | Variable Qualifier | Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE", "SOFT TISSUE". |
| `PARENT` | Specimen Parent | Char | Exp | Identifier | Identifies the REFID of the parent of a specimen to support tracking its genealogy. |
| `LEVEL` | Specimen Level | Num | Req | Variable Qualifier | Identifies the generation number of the sample where the collected sample is considered the first generation. |
