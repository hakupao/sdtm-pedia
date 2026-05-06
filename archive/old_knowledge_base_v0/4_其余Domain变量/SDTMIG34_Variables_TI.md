# SDTM IG v3.4 Variables - TI Domain

**Domain Code:** `TI`

**Total Variables:** 8

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `IETESTCD` | Incl/Excl Criterion Short Name | Char | Req | Topic | Short name IETEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). IETESTCD cannot contain characters other than letters, numbers, or underscores. The prefix "IE" is used to ensure consistency with the IE domain. |
| `IETEST` | Inclusion/Exclusion Criterion | Char | Req | Synonym Qualifier | Full text of the inclusion or exclusion criterion. The prefix "IE" is used to ensure consistency with the IE domain. |
| `IECAT` | Inclusion/Exclusion Category | Char | Req | Grouping Qualifier | Used for categorization of the inclusion or exclusion criteria. |
| `IESCAT` | Inclusion/Exclusion Subcategory | Char | Perm | Grouping Qualifier | A further categorization of the exception criterion. Can be used to distinguish criteria for a sub-study or to categorize as major or minor exceptions. Examples: "MAJOR", "MINOR". |
| `TIRL` | Inclusion/Exclusion Criterion Rule | Char | Perm | Rule | Rule that expresses the criterion in computer-executable form. See Assumption 4. |
| `TIVERS` | Protocol Criteria Versions | Char | Perm | Record Qualifier | The number of this version of the Inclusion/Exclusion criteria. May be omitted if there is only 1 version. |
