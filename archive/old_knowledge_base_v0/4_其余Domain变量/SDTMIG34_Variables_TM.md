# SDTM IG v3.4 Variables - TM Domain

**Domain Code:** `TM`

**Total Variables:** 5

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain, which must be TM. |
| `MIDSTYPE` | Disease Milestone Type | Char | Req | Topic | The type of disease milestone. Example: "HYPOGLYCEMIC EVENT". |
| `TMDEF` | Disease Milestone Definition | Char | Req | Variable Qualifier | Definition of the disease milestone. |
| `TMRPT` | Disease Milestone Repetition Indicator | Char | Req | Record Qualifier | Indicates whether this is a disease milestone that can occur only once ("N") or a type of disease milestone that can occur multiple times ("Y"). |
