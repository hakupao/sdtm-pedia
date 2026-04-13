# TI — Trial Inclusion/Exclusion Criteria

> Class: Trial Design | Structure: One record per I/E criterion

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### IETESTCD
- **Order:** 3
- **Label:** Incl/Excl Criterion Short Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name IETEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). IETESTCD cannot contain characters other than letters, numbers, or underscores. The prefix "IE" is used to ensure consistency with the IE domain.

### IETEST
- **Order:** 4
- **Label:** Inclusion/Exclusion Criterion
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Full text of the inclusion or exclusion criterion. The prefix "IE" is used to ensure consistency with the IE domain.

### IECAT
- **Order:** 5
- **Label:** Inclusion/Exclusion Category
- **Type:** Char
- **Controlled Terms:** C66797
- **Role:** Grouping Qualifier
- **Core:** Req
- **CDISC Notes:** Used for categorization of the inclusion or exclusion criteria.

### IESCAT
- **Order:** 6
- **Label:** Inclusion/Exclusion Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the exception criterion. Can be used to distinguish criteria for a sub-study or to categorize as major or minor exceptions. Examples: "MAJOR", "MINOR".

### TIRL
- **Order:** 7
- **Label:** Inclusion/Exclusion Criterion Rule
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Perm
- **CDISC Notes:** Rule that expresses the criterion in computer-executable form. See Assumption 4.

### TIVERS
- **Order:** 8
- **Label:** Protocol Criteria Versions
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The number of this version of the Inclusion/Exclusion criteria. May be omitted if there is only 1 version.
