# GF — Genomics Findings

> Class: Findings | Structure: One record per finding per observation per biospecimen per subject

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

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### SPDEVID
- **Order:** 4
- **Label:** Sponsor Device Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier for a device.

### NHOID
- **Order:** 5
- **Label:** Non-Host Organism Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears.

### GFSEQ
- **Order:** 6
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### GFGRPID
- **Order:** 7
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records within a subject in a domain.

### GFREFID
- **Order:** 8
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** A unique identifier for the assayed genetic specimen.

### GFSPID
- **Order:** 9
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### GFLNKID
- **Order:** 10
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### GFLNKGRP
- **Order:** 11
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### GFTESTCD
- **Order:** 12
- **Label:** Short Name of Genomic Measurement
- **Type:** Char
- **Controlled Terms:** C181178
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in GFTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in GFTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). GFTESTCD cannot contain characters other than letters, numbers, or underscores.

### GFTEST
- **Order:** 13
- **Label:** Name of Genomic Measurement
- **Type:** Char
- **Controlled Terms:** C181179
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for GFTESTCD. The value in GFTEST cannot be longer than 40 characters.

### GFTSTDTL
- **Order:** 14
- **Label:** Measurement, Test, or Examination Detail
- **Type:** Char
- **Controlled Terms:** C181180
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of a reportable qualifying the assessment in GFTESTCD and GFTEST.

### GFCAT
- **Order:** 15
- **Label:** Category for Genomic Finding
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values.

### GFSCAT
- **Order:** 16
- **Label:** Subcategory for Genomic Finding
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of GFCAT values.

### GFORRES
- **Order:** 17
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### GFORRESU
- **Order:** 18
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for GFORRES.

### GFORREF
- **Order:** 19
- **Label:** Reference Result in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Reference value for the result or finding as originally received or collected. GFORREF uses the same units as GFORRES, if applicable.

### GFSTRESC
- **Order:** 20
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from GFORRES, in a standard format or in standard units. GFSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in GFSTRESN.

### GFSTRESN
- **Order:** 21
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from GFSTRESC. GFSTRESN should store all numeric test results or findings.

### GFSTRESU
- **Order:** 22
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for GFSTRESC, GFSTRESN, GFSTREFC, and GFSTREFN.

### GFSTREFC
- **Order:** 23
- **Label:** Reference Result in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Reference value for the result or finding copied or derived from GFORREF in a standard format.

### GFSTREFN
- **Order:** 24
- **Label:** Numeric Reference Result in Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Reference value for continuous or numeric results or findings in standard format or in standard units. GFSTREFN uses the same units as GFSTRESN, if applicable.

### GFRESCAT
- **Order:** 25
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding.

### GFINHERT
- **Order:** 26
- **Label:** Inheritability
- **Type:** Char
- **Controlled Terms:** C181177
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies whether the variation can be passed to the next generation.

### GFGENREF
- **Order:** 27
- **Label:** Genome Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** An identifier for the genome reference used to generate the reported result. For example, Genome Reference Consortium Human Build 38 patch release 13 may be represented as "GRCh38.p13".

### GFCHROM
- **Order:** 28
- **Label:** Chromosome Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** The designation (name or number) of the chromosome or contig on which the variant or other feature appears (e.g., "17"; "X").

### GFSYM
- **Order:** 29
- **Label:** Genomic Symbol
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A published symbol for the portion of the genome serving as a locus for the experiment/test.

### GFSYMTYP
- **Order:** 30
- **Label:** Genomic Symbol Type
- **Type:** Char
- **Controlled Terms:** C181176
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A description of the type of genomic entity that is represented by the published symbol in GFSYM.

### GFGENLOC
- **Order:** 31
- **Label:** Genetic Location
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Specifies the location within a sequence for the observed value in GFORRES.

### GFGENSR
- **Order:** 32
- **Label:** Genetic Sub-Region
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** The portion of the locus in which the variation was found. Examples: "Exon 15", "Kinase domain".

### GFSEQID
- **Order:** 33
- **Label:** Sequence Identifier \n
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A unique identifier for the sequence used as the reference to identify the genetic variation in the result. Examples: "NM_001234", "ENSG00000182533", "ENST00000343849.2".

### GFPVRID
- **Order:** 34
- **Label:** Published Variant Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A unique identifier for the variation that has been publicly characterized in an external database. Examples: "rs2231142", "COSM41596".

### GFCOPYID
- **Order:** 35
- **Label:** Copy Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** An arbitrary identifier used to differentiate between copies of a genetic target of interest present on homologous chromosomes.

### GFSTAT
- **Order:** 36
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### GFREASND
- **Order:** 37
- **Label:** Reason Test Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with GFSTAT when value is "NOT DONE".

### GFXFN
- **Order:** 38
- **Label:** External File Path
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The filename and/or path to external data not stored in the same format and possibly not the same location as the other data for a study.

### GFNAM
- **Order:** 39
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor that provided the test result. When more than 1 vendor is involved in the generation of the result, additional vendors should be represented as supplemental qualifiers.

### GFSPEC
- **Order:** 40
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C111114
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies the type of genetic material used for the measurement.

### GFMETHOD
- **Order:** 41
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** The test method by which the examination is performed by the wet lab in order to yield the result reported in the dataset.

### GFRUNID
- **Order:** 42
- **Label:** Run ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** A unique identifier for a particular run of a test performed by the wet lab on a particular batch of samples. This identifier can be used to distinguish between records for the same test performed at different times.

### GFANMETH
- **Order:** 43
- **Label:** Analysis Method
- **Type:** Char
- **Controlled Terms:** C181181
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The method of secondary processing performed by the dry lab to yield the result reported in the dataset.

### GFBLFL
- **Order:** 44
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null.

### GFDRVFL
- **Order:** 45
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### GFLLOQ
- **Order:** 46
- **Label:** Lower Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates the lower limit of quantitation for an assay. Units will be those used for GFSTRESU.

### GFREPNUM
- **Order:** 47
- **Label:** Repetition Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The instance number of a test that is repeated within a given timeframe for the same test performed by the wet lab.

### VISITNUM
- **Order:** 48
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 49
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter.

### VISITDY
- **Order:** 50
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### GFDTC
- **Order:** 51
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of specimen collection.

### GFDY
- **Order:** 52
- **Label:** Study Day of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### GFTPT
- **Order:** 53
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See GFTPTNUM and GFTPTREF.

### GFTPTNUM
- **Order:** 54
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of GFTPT used in sorting.

### GFELTM
- **Order:** 55
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Elapsed time relative to a planned fixed reference (GFTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration.

### GFTPTREF
- **Order:** 56
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by GFELTM, GFTPTNUM, and GFTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### GFRFTDTC
- **Order:** 57
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by GFTPTREF.
