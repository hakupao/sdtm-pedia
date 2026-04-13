# OI — Non-host Organism Identifiers

> Class: Study Reference | Structure: One record per taxon per non-host organism

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

### NHOID
- **Order:** 3
- **Label:** Non-host Organism Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sponsor-defined identifier for a non-host organism. NHOID should be populated with an intuitive name based on the identity of the organism as reported by the lab. It must be unique for each unique organism as defined by the specific values of the organism's entire known taxonomy described by pairs of OIPARMCD and OIVAL .

### OISEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to given to ensure uniqueness within a parameter within an organism (NHOID) within dataset.

### OIPARMCD
- **Order:** 5
- **Label:** Non-host Organism ID Element Short Name
- **Type:** Char
- **Controlled Terms:** C179591
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the taxon being described. Examples: "GROUP", "GENTYP", "SUBTYP".

### OIPARM
- **Order:** 6
- **Label:** Non-host Organism ID Element Name
- **Type:** Char
- **Controlled Terms:** C179590
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Name of the taxon being described. Examples: "Group", "Genotype", "Subtype".

### OIVAL
- **Order:** 7
- **Label:** Non-host Organism ID Element Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Req
- **CDISC Notes:** Value for the taxon in OIPARMCD/OIPARM for the organism identified by NHOID.
