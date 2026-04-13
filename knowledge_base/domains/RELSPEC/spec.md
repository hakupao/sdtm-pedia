# RELSPEC — Related Specimens

> Class: Relationship | Structure: One record per specimen identifier per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### USUBJID
- **Order:** 2
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### REFID
- **Order:** 3
- **Label:** Specimen ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Specimen identifier, unique within USUBJID.

### SPEC
- **Order:** 4
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734; C111114
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE", "SOFT TISSUE".

### PARENT
- **Order:** 5
- **Label:** Specimen Parent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Identifies the REFID of the parent of a specimen to support tracking its genealogy.

### LEVEL
- **Order:** 6
- **Label:** Specimen Level
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Req
- **CDISC Notes:** Identifies the generation number of the sample where the collected sample is considered the first generation.
