# TE — Trial Elements

> Class: Trial Design | Structure: One record per planned Element

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

### ETCD
- **Order:** 3
- **Label:** Element Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name.

### ELEMENT
- **Order:** 4
- **Label:** Description of Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** The name of the element.

### TESTRL
- **Order:** 5
- **Label:** Rule for Start of Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Req
- **CDISC Notes:** Describes condition for beginning element.

### TEENRL
- **Order:** 6
- **Label:** Rule for End of Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Perm
- **CDISC Notes:** Describes condition for ending element. Either TEENRL or TEDUR must be present for each element.

### TEDUR
- **Order:** 7
- **Label:** Planned Duration of Element
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned duration of element in ISO 8601 format. Used when the rule for ending the element is applied after a fixed duration.
