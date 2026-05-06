# SDTM IG v3.4 Variables - GF Domain

**Domain Code:** `GF`

**Total Variables:** 57

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `SPDEVID` | Sponsor Device Identifier | Char | Perm | Identifier | Sponsor-defined identifier for a device. |
| `NHOID` | Non-Host Organism Identifier | Char | Perm | Identifier | Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears. |
| `GFSEQ` | Sequence Number | Num | Req | Identifier | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| `GFGRPID` | Group ID | Char | Perm | Identifier | Used to link together a block of related records within a subject in a domain. |
| `GFREFID` | Reference ID | Char | Exp | Identifier | A unique identifier for the assayed genetic specimen. |
| `GFSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. |
| `GFLNKID` | Link ID | Char | Perm | Identifier | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| `GFLNKGRP` | Link Group ID | Char | Perm | Identifier | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| `GFTESTCD` | Short Name of Genomic Measurement | Char | Req | Topic | Short name of the measurement, test, or examination described in GFTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in GFTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). GFTESTCD cannot contain characters other than letters, numbers, or underscores. |
| `GFTEST` | Name of Genomic Measurement | Char | Req | Synonym Qualifier | Long name for GFTESTCD. The value in GFTEST cannot be longer than 40 characters. |
| `GFTSTDTL` | Measurement, Test, or Examination Detail | Char | Perm | Variable Qualifier | Description of a reportable qualifying the assessment in GFTESTCD and GFTEST. |
| `GFCAT` | Category for Genomic Finding | Char | Perm | Grouping Qualifier | Used to define a category of topic-variable values. |
| `GFSCAT` | Subcategory for Genomic Finding | Char | Perm | Grouping Qualifier | Used to define a further categorization of GFCAT values. |
| `GFORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the measurement or finding as originally received or collected. |
| `GFORRESU` | Original Units | Char | Perm | Variable Qualifier | Unit for GFORRES. |
| `GFORREF` | Reference Result in Original Units | Char | Perm | Variable Qualifier | Reference value for the result or finding as originally received or collected. GFORREF uses the same units as GFORRES, if applicable. |
| `GFSTRESC` | Result or Finding in Standard Format | Char | Exp | Result Qualifier | Contains the result value for all findings, copied or derived from GFORRES, in a standard format or in standard units. GFSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in GFSTRESN. |
| `GFSTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from GFSTRESC. GFSTRESN should store all numeric test results or findings. |
| `GFSTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized units used for GFSTRESC, GFSTRESN, GFSTREFC, and GFSTREFN. |
| `GFSTREFC` | Reference Result in Standard Format | Char | Perm | Variable Qualifier | Reference value for the result or finding copied or derived from GFORREF in a standard format. |
| `GFSTREFN` | Numeric Reference Result in Std Units | Num | Perm | Variable Qualifier | Reference value for continuous or numeric results or findings in standard format or in standard units. GFSTREFN uses the same units as GFSTRESN, if applicable. |
| `GFRESCAT` | Result Category | Char | Perm | Variable Qualifier | Used to categorize the result of a finding. |
| `GFINHERT` | Inheritability | Char | Perm | Variable Qualifier | Identifies whether the variation can be passed to the next generation. |
| `GFGENREF` | Genome Reference | Char | Perm | Variable Qualifier | An identifier for the genome reference used to generate the reported result. For example, Genome Reference Consortium Human Build 38 patch release 13 may be represented as "GRCh38.p13". |
| `GFCHROM` | Chromosome Identifier | Char | Perm | Variable Qualifier | The designation (name or number) of the chromosome or contig on which the variant or other feature appears (e.g., "17"; "X"). |
| `GFSYM` | Genomic Symbol | Char | Perm | Variable Qualifier | A published symbol for the portion of the genome serving as a locus for the experiment/test. |
| `GFSYMTYP` | Genomic Symbol Type | Char | Perm | Variable Qualifier | A description of the type of genomic entity that is represented by the published symbol in GFSYM. |
| `GFGENLOC` | Genetic Location | Char | Perm | Variable Qualifier | Specifies the location within a sequence for the observed value in GFORRES. |
| `GFGENSR` | Genetic Sub-Region | Char | Perm | Variable Qualifier | The portion of the locus in which the variation was found. Examples: "Exon 15", "Kinase domain". |
| `GFSEQID` | Sequence Identifier \n | Char | Perm | Variable Qualifier | A unique identifier for the sequence used as the reference to identify the genetic variation in the result. Examples: "NM_001234", "ENSG00000182533", "ENST00000343849.2". |
| `GFPVRID` | Published Variant Identifier | Char | Perm | Variable Qualifier | A unique identifier for the variation that has been publicly characterized in an external database. Examples: "rs2231142", "COSM41596". |
| `GFCOPYID` | Copy Identifier | Char | Perm | Variable Qualifier | An arbitrary identifier used to differentiate between copies of a genetic target of interest present on homologous chromosomes. |
| `GFSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| `GFREASND` | Reason Test Not Done | Char | Perm | Record Qualifier | Reason not done. Used in conjunction with GFSTAT when value is "NOT DONE". |
| `GFXFN` | External File Path | Char | Perm | Record Qualifier | The filename and/or path to external data not stored in the same format and possibly not the same location as the other data for a study. |
| `GFNAM` | Laboratory/Vendor Name | Char | Perm | Record Qualifier | Name or identifier of the vendor that provided the test result. When more than 1 vendor is involved in the generation of the result, additional vendors should be represented as supplemental qualifiers. |
| `GFSPEC` | Specimen Material Type | Char | Perm | Record Qualifier | Identifies the type of genetic material used for the measurement. |
| `GFMETHOD` | Method of Test or Examination | Char | Exp | Record Qualifier | The test method by which the examination is performed by the wet lab in order to yield the result reported in the dataset. |
| `GFRUNID` | Run ID | Char | Perm | Record Qualifier | A unique identifier for a particular run of a test performed by the wet lab on a particular batch of samples. This identifier can be used to distinguish between records for the same test performed at different times. |
| `GFANMETH` | Analysis Method | Char | Perm | Record Qualifier | The method of secondary processing performed by the dry lab to yield the result reported in the dataset. |
| `GFBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be "Y" or null. |
| `GFDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| `GFLLOQ` | Lower Limit of Quantitation | Num | Perm | Variable Qualifier | Indicates the lower limit of quantitation for an assay. Units will be those used for GFSTRESU. |
| `GFREPNUM` | Repetition Number | Num | Perm | Record Qualifier | The instance number of a test that is repeated within a given timeframe for the same test performed by the wet lab. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT. Should be an integer. |
| `GFDTC` | Date/Time of Specimen Collection | Char | Exp | Timing | Date and time of specimen collection. |
| `GFDY` | Study Day of Specimen Collection | Num | Perm | Timing | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `GFTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See GFTPTNUM and GFTPTREF. |
| `GFTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numerical version of GFTPT used in sorting. |
| `GFELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Elapsed time relative to a planned fixed reference (GFTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration. |
| `GFTPTREF` | Time Point Reference | Char | Perm | Timing | Name of the fixed reference point referred to by GFELTM, GFTPTNUM, and GFTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| `GFRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by GFTPTREF. |
