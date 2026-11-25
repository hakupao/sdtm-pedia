# SDTMIG v3.4 --- Domain Models: Findings — Part 3

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 3/8 — 6.3.5.4-6.3.5.5: Specimen-based (GF, IS)
> **Original:** `SDTMIG34_06_DomainModels_Findings.md`
> **Related:** `SDTMIG34_06a_DomainModels_Findings.md`, `SDTMIG34_06b_DomainModels_Findings.md`, `SDTMIG34_06d_DomainModels_Findings.md`, `SDTMIG34_06e_DomainModels_Findings.md`, `SDTMIG34_06f_DomainModels_Findings.md`, `SDTMIG34_06g_DomainModels_Findings.md`, `SDTMIG34_06h_DomainModels_Findings.md`

---

#### 6.3.5.4 Genomics Findings (GF)

##### GF – Description/Overview
A findings domain that contains data related to the structure, function, evolution, mapping, and editing of subject and non-host organism genomic material of interest. This domain includes but is not limited to assessments and results for genetic variation and transcription, and summary measures derived from these assessments. The GF domain is used for findings from characteristics assessed from nucleic acids and may include subsequent inferences and/or predictions about related proteins/amino acids.


##### GF – Specification
gf.xpt, Genomics Findings — Findings. One record per finding per observation per biospecimen per subject, Tabulation.

**Structure:** One record per finding per observation per biospecimen per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | GF |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |
| 5 | NHOID | Non-Host Organism Identifier | Char | Identifier | Perm |  |
| 6 | GFSEQ | Sequence Number | Num | Identifier | Req |  |
| 7 | GFGRPID | Group ID | Char | Identifier | Perm |  |
| 8 | GFREFID | Reference ID | Char | Identifier | Exp |  |
| 9 | GFSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 10 | GFLNKID | Link ID | Char | Identifier | Perm |  |
| 11 | GFLNKGRP | Link Group ID | Char | Identifier | Perm |  |
| 12 | GFTESTCD | Short Name of Genomic Measurement | Char | Topic | Req | C181178 |
| 13 | GFTEST | Name of Genomic Measurement | Char | Synonym Qualifier | Req | C181179 |
| 14 | GFTSTDTL | Measurement, Test, or Examination Detail | Char | Variable Qualifier | Perm | C181180 |
| 15 | GFCAT | Category for Genomic Finding | Char | Grouping Qualifier | Perm |  |
| 16 | GFSCAT | Subcategory for Genomic Finding | Char | Grouping Qualifier | Perm |  |
| 17 | GFORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 18 | GFORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 19 | GFORREF | Reference Result in Original Units | Char | Variable Qualifier | Perm |  |
| 20 | GFSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |
| 21 | GFSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 22 | GFSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 23 | GFSTREFC | Reference Result in Standard Format | Char | Variable Qualifier | Perm |  |
| 24 | GFSTREFN | Numeric Reference Result in Std Units | Num | Variable Qualifier | Perm |  |
| 25 | GFRESCAT | Result Category | Char | Variable Qualifier | Perm |  |
| 26 | GFINHERT | Inheritability | Char | Variable Qualifier | Perm | C181177 |
| 27 | GFGENREF | Genome Reference | Char | Variable Qualifier | Perm |  |
| 28 | GFCHROM | Chromosome Identifier | Char | Variable Qualifier | Perm |  |
| 29 | GFSYM | Genomic Symbol | Char | Variable Qualifier | Perm |  |
| 30 | GFSYMTYP | Genomic Symbol Type | Char | Variable Qualifier | Perm | C181176 |
| 31 | GFGENLOC | Genetic Location | Char | Variable Qualifier | Perm |  |
| 32 | GFGENSR | Genetic Sub-Region | Char | Variable Qualifier | Perm |  |
| 33 | GFSEQID | Sequence Identifier; | Char | Variable Qualifier | Perm |  |
| 34 | GFPVRID | Published Variant Identifier | Char | Variable Qualifier | Perm |  |
| 35 | GFCOPYID | Copy Identifier | Char | Variable Qualifier | Perm |  |
| 36 | GFSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 37 | GFREASND | Reason Test Not Done | Char | Record Qualifier | Perm |  |
| 38 | GFXFN | External File Path | Char | Record Qualifier | Perm |  |
| 39 | GFNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |
| 40 | GFSPEC | Specimen Material Type | Char | Record Qualifier | Perm | C111114 |
| 41 | GFMETHOD | Method of Test or Examination | Char | Record Qualifier | Exp | C85492 |
| 42 | GFRUNID | Run ID | Char | Record Qualifier | Perm |  |
| 43 | GFANMETH | Analysis Method | Char | Record Qualifier | Perm | C181181 |
| 44 | GFBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 45 | GFDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 46 | GFLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Perm |  |
| 47 | GFREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |
| 48 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 49 | VISIT | Visit Name | Char | Timing | Perm |  |
| 50 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 51 | GFDTC | Date/Time of Specimen Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 52 | GFDY | Study Day of Specimen Collection | Num | Timing | Perm |  |
| 53 | GFTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 54 | GFTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 55 | GFELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 56 | GFTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 57 | GFRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **SPDEVID**: Sponsor-defined identifier for a device.
- **NHOID**: Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears.
- **GFSEQ**: Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.
- **GFGRPID**: Used to link together a block of related records within a subject in a domain.
- **GFREFID**: A unique identifier for the assayed genetic specimen.
- **GFSPID**: Sponsor-defined identifier.
- **GFLNKID**: Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.
- **GFLNKGRP**: Identifier used to link related records across domains. This will usually be a many-to-one relationship.
- **GFTESTCD**: Short name of the measurement, test, or examination described in GFTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in GFTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). GFTESTCD cannot contain characters other than letters, numbers, or underscores.
- **GFTEST**: Long name for GFTESTCD. The value in GFTEST cannot be longer than 40 characters.
- **GFTSTDTL**: Description of a reportable qualifying the assessment in GFTESTCD and GFTEST.
- **GFCAT**: Used to define a category of topic-variable values.
- **GFSCAT**: Used to define a further categorization of GFCAT values.
- **GFORRES**: Result of the measurement or finding as originally received or collected.
- **GFORRESU**: Unit for GFORRES.
- **GFORREF**: Reference value for the result or finding as originally received or collected. GFORREF uses the same units as GFORRES, if applicable.
- **GFSTRESC**: Contains the result value for all findings, copied or derived from GFORRES, in a standard format or in standard units. GFSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in GFSTRESN.
- **GFSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from GFSTRESC. GFSTRESN should store all numeric test results or findings.
- **GFSTRESU**: Standardized units used for GFSTRESC, GFSTRESN, GFSTREFC, and GFSTREFN.
- **GFSTREFC**: Reference value for the result or finding copied or derived from GFORREF in a standard format.
- **GFSTREFN**: Reference value for continuous or numeric results or findings in standard format or in standard units. GFSTREFN uses the same units as GFSTRESN, if applicable.
- **GFRESCAT**: Used to categorize the result of a finding.
- **GFINHERT**: Identifies whether the variation can be passed to the next generation.
- **GFGENREF**: An identifier for the genome reference used to generate the reported result. For example, Genome Reference Consortium Human Build 38 patch release 13 may be represented as "GRCh38.p13".
- **GFCHROM**: The designation (name or number) of the chromosome or contig on which the variant or other feature appears (e.g., "17"; "X").
- **GFSYM**: A published symbol for the portion of the genome serving as a locus for the experiment/test.
- **GFSYMTYP**: A description of the type of genomic entity that is represented by the published symbol in GFSYM.
- **GFGENLOC**: Specifies the location within a sequence for the observed value in GFORRES.
- **GFGENSR**: The portion of the locus in which the variation was found. Examples: "Exon 15", "Kinase domain".
- **GFSEQID**: A unique identifier for the sequence used as the reference to identify the genetic variation in the result. Examples: "NM_001234", "ENSG00000182533", "ENST00000343849.2".
- **GFPVRID**: A unique identifier for the variation that has been publicly characterized in an external database. Examples: "rs2231142", "COSM41596".
- **GFCOPYID**: An arbitrary identifier used to differentiate between copies of a genetic target of interest present on homologous chromosomes.
- **GFSTAT**: Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".
- **GFREASND**: Reason not done. Used in conjunction with GFSTAT when value is "NOT DONE".
- **GFXFN**: The filename and/or path to external data not stored in the same format and possibly not the same location as the other data for a study.
- **GFNAM**: Name or identifier of the vendor that provided the test result. When more than 1 vendor is involved in the generation of the result, additional vendors should be represented as supplemental qualifiers.
- **GFSPEC**: Identifies the type of genetic material used for the measurement.
- **GFMETHOD**: The test method by which the examination is performed by the wet lab in order to yield the result reported in the dataset.
- **GFRUNID**: A unique identifier for a particular run of a test performed by the wet lab on a particular batch of samples. This identifier can be used to distinguish between records for the same test performed at different times.
- **GFANMETH**: The method of secondary processing performed by the dry lab to yield the result reported in the dataset.
- **GFBLFL**: Indicator used to identify a baseline value. Should be "Y" or null.
- **GFDRVFL**: Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.
- **GFLLOQ**: Indicates the lower limit of quantitation for an assay. Units will be those used for GFSTRESU.
- **GFREPNUM**: The instance number of a test that is repeated within a given timeframe for the same test performed by the wet lab.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter.
- **VISITDY**: Planned study day of VISIT. Should be an integer.
- **GFDTC**: Date and time of specimen collection.
- **GFDY**: Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.
- **GFTPT**: Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See GFTPTNUM and GFTPTREF.
- **GFTPTNUM**: Numerical version of GFTPT used in sorting.
- **GFELTM**: Elapsed time relative to a planned fixed reference (GFTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration.
- **GFTPTREF**: Name of the fixed reference point referred to by GFELTM, GFTPTNUM, and GFTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **GFRFTDTC**: Date/time for a fixed reference time point defined by GFTPTREF.


##### GF – Assumptions
1. The Genomics Findings domain is used to represent findings related to the structure, function, evolution, mapping, and editing of subject and non-host organism genomic material of interest. This domain includes but is not limited to assessments and results for genetic variation and transcription, and summary measures derived from these assessments. The GF domain is used for findings from characteristics assessed from nucleic acids and may include subsequent inferences and/or predictions about related proteins/amino acids. However, direct assessments of proteins (e.g., assessments of amino acids) are out of scope for this domain.
2. Regarding genetic testing on non-host organisms (including but not limited to bacteria, viruses, and parasites), the following additional assumptions apply:
    a. Tests that give genetic results (e.g., expressed in terms of genetic variation, specific sequence information) on non-host organisms that have been identified in subject samples should be represented in GF. To distinguish these findings from subject genetic data, the variable NHOID must be populated to identify the non-host organism as the focus of the record (see Section 9.2, Non-host Organism Identifiers, assumption 2 for more information).
    b. If the purpose of the test is to detect or determine the identity of a viable, non-host organism or infectious agent in a subject sample, data should be represented in the Microbiology Specimen (MB) domain.
    c. Tests that are used to determine the resistance/susceptibility of a non-host organism to a drug on a genetic basis should be represented in the Microbiology Susceptibility (MS) domain.
    d. If the test provides both genetic data and susceptibility/resistance data, genetic data should be represented in GF and the susceptibility/resistance data should be represented in the MS domain (See Section 6.3.5.7.2, Microbiology Susceptibility, assumption 1b for more information).
3. The platform used to detect the finding may be represented in SPDEVID. Attributes used in conjunction with a platform (e.g., assay panel, reagents) may be represented in the Device Identifiers (DI) domain and other associated device domains. See the SDTM Implementation Guide for Medical Devices (SDTMIG-MD) for further information about SPDEVID and the device domains.
4. Values populated in GFCAT and GFSCAT are sponsor-defined and there is no CDISC Controlled Terminology for these variables.
5. Genomic symbols are represented in GFSYM.
    a. GFTESTCD and GFTEST should not include genomic names or symbols, including but not limited to official gene symbols.
    b. For human genetic data, standard nomenclature populated in variable GFSYM must be obtained from the genomic symbol list maintained in the HUGO Gene Nomenclature Committee (HGNC) database (www.genenames.org).
6. When populating GFGENSR, caution should be exercised for annotations of loci where more than 1 annotation applies. In such cases, the source of the annotation should be captured and documented in Define-XML. In addition, the value populated in GFGENSR may be dependent on the precision of the value populated in GFSEQID.
7. Values populated in GFGENREF, GFSEQID, and GFPVRID should reflect the level of granularity collected (e.g., version, build, patch, release) to support interpretation of the reported result.
8. GFMETHOD lists wet lab techniques for the execution of genomics or genetic testing. Methods related to specimen processing or reagents are not represented in GFMETHOD.
9. The following variables generally would not be used in GF: --POS, --BODSYS, --ORNRLO, ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --CHRON, --DISTR, --ANTREG, --LOC, --LAT, --DIR, --PORTOT, --LEAD, --CSTATE, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

##### GF – Examples

**Example 1**
This example shows findings from an assessment of single nucleotide and copy number variation generated from biocomputational analysis with wet laboratory methodology targeted genome sequencing. Findings from this assessment show variation from DNA extracted from an individual's tumor tissue. As the DNA specimen was extracted from tumor tissue, the inheritabilty of the variation is considered to be somatic.
**Row 1:** Shows the predicted amino acid change due to the single nucleotide variant.
**Row 2:** Shows the predicted coding sequence change due to the single nucleotide variant.
**Row 3:** Shows the classification of the variant impact given the predicted amino acid change.
**Row 4:** Shows the number of times the locus specified in variables GFCHROM and GFGENLOC was observed.
**Row 5:** Shows the percent variant read depth to total read depth.
**Row 6:** Shows the number of copies of the gene of interest within the genome of the tumor cell.
**Row 7:** Shows the number of altered exons within the gene of interest in the genome of the tumor cell.
**Row 8:** Shows the ratio of the copy number of the gene of interest in the tumor cell to the reference number of copies.
**Row 9:** Shows the interpretation of the copy number of the gene of interest within the genome of the tumor cell.
*gf.xpt*

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | GFSEQ | GFGRPID | GFREFID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFORRESU | GFSTRESC | GFSTRESN | GFSTRESU | GFINHERT | GFGENREF | GFCHROM | GFSYM | GFSYMTYP | GFGENLOC | GFSEQID | GFPVRID | GFXFN | GFNAM | GFSPEC | GFMETHOD | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | GF | 123101 | ACME GenePanel 500 | 1 | 1 | TRF001338 | SNV | Single Nucleotide Variation | PREDICTED AMINO ACID CHANGE | D1853N |  | D1853N |  |  | SOMATIC VARIATION | GRCh37.75 | 11 | ATM | GENE WITH PROTEIN PRODUCT | 108175462 | ENST00000278616.4 | COSM41596 | /compbio/analysis/120718_SN855_0084_AD13D5ACXX_LCNL361/sampleAnalysis/sample18.TRF001338.01/TRF001338.01.vars.final.xml | ACME SEQUENCING LLC | DNA | TARGETED GENOME SEQUENCING | 1 | Day 1 | 1 | 2018-05-22 | 2 |
| 2 | ABC-123 | GF | 123101 | ACME GenePanel 500 | 2 | 1 | TRF001338 | SNV | Single Nucleotide Variation | PREDICTED CODING SEQUENCE CHANGE | 5557G>A |  | 5557G>A |  |  | SOMATIC VARIATION | GRCh37.75 | 11 | ATM | GENE WITH PROTEIN PRODUCT | 108175462 | ENST00000278616.4 | COSM41596 | /compbio/analysis/120718_SN855_0084_AD13D5ACXX_LCNL361/sampleAnalysis/sample18.TRF001338.01/TRF001338.01.vars.final.xml | ACME SEQUENCING LLC | DNA | TARGETED GENOME SEQUENCING | 1 | Day 1 | 1 | 2018-05-22 | 2 |
| 3 | ABC-123 | GF | 123101 | ACME GenePanel 500 | 3 | 1 | TRF001338 | SNV | Single Nucleotide Variation | VARIANT IMPACT CLASSIFICATION | ambiguous |  | ambiguous |  |  | SOMATIC VARIATION | GRCh37.75 | 11 | ATM | GENE WITH PROTEIN PRODUCT | 108175462 | ENST00000278616.4 | COSM41596 | /compbio/analysis/120718_SN855_0084_AD13D5ACXX_LCNL361/sampleAnalysis/sample18.TRF001338.01/TRF001338.01.vars.final.xml | ACME SEQUENCING LLC | DNA | TARGETED GENOME SEQUENCING | 1 | Day 1 | 1 | 2018-05-22 | 2 |
| 4 | ABC-123 | GF | 123101 | ACME GenePanel 500 | 4 | 1 | TRF001338 | SNV | Single Nucleotide Variation | READ DEPTH | 501 |  | 501 | 501 |  | SOMATIC VARIATION | GRCh37.75 | 11 | ATM | GENE WITH PROTEIN PRODUCT | 108175462 | ENST00000278616.4 | COSM41596 | /compbio/analysis/120718_SN855_0084_AD13D5ACXX_LCNL361/sampleAnalysis/sample18.TRF001338.01/TRF001338.01.vars.final.xml | ACME SEQUENCING LLC | DNA | TARGETED GENOME SEQUENCING | 1 | Day 1 | 1 | 2018-05-22 | 2 |
| 5 | ABC-123 | GF | 123101 | ACME GenePanel 500 | 5 | 1 | TRF001338 | SNV | Single Nucleotide Variation | VARIANT READ DEPTH/READ DEPTH | 51 | % | 51 | 51 | % | SOMATIC VARIATION | GRCh37.75 | 11 | ATM | GENE WITH PROTEIN PRODUCT | 108175462 | ENST00000278616.4 | COSM41596 | /compbio/analysis/120718_SN855_0084_AD13D5ACXX_LCNL361/sampleAnalysis/sample18.TRF001338.01/TRF001338.01.vars.final.xml | ACME SEQUENCING LLC | DNA | TARGETED GENOME SEQUENCING | 1 | Day 1 | 1 | 2018-05-22 | 2 |
| 6 | ABC-123 | GF | 123101 | ACME GenePanel 500 | 6 | 2 | TRF001338 | CPNUMVAR | Copy Number Variation | NUMBER OF GENE COPIES | 0 |  | 0 | 0 |  | SOMATIC VARIATION | GRCh37.75 | 9 | CDKN2A | GENE WITH PROTEIN PRODUCT | 21967751 | ENST00000579755.1 | COSM12473 | /compbio/analysis/120718_SN855_0084_AD13D5ACXX_LCNL361/sampleAnalysis/sample18.TRF001338.01/TRF001338.01.vars.final.xml | ACME SEQUENCING LLC | DNA | TARGETED GENOME SEQUENCING | 1 | Day 1 | 1 | 2018-05-22 | 2 |
| 7 | ABC-123 | GF | 123101 | ACME GenePanel 500 | 7 | 2 | TRF001338 | CPNUMVAR | Copy Number Variation | NUMBER OF ALTERED EXONS | 6 of 6 |  | 6 of 6 |  |  | SOMATIC VARIATION | GRCh37.75 | 9 | CDKN2A | GENE WITH PROTEIN PRODUCT | 21967751 | ENST00000579755.1 | COSM12473 | /compbio/analysis/120718_SN855_0084_AD13D5ACXX_LCNL361/sampleAnalysis/sample18.TRF001338.01/TRF001338.01.vars.final.xml | ACME SEQUENCING LLC | DNA | TARGETED GENOME SEQUENCING | 1 | Day 1 | 1 | 2018-05-22 | 2 |
| 8 | ABC-123 | GF | 123101 | ACME GenePanel 500 | 8 | 2 | TRF001338 | CPNUMVAR | Copy Number Variation | COPY NUMBER RATIO | 0.63 |  | 0.63 | 0.63 |  | SOMATIC VARIATION | GRCh37.75 | 9 | CDKN2A | GENE WITH PROTEIN PRODUCT | 21967751 | ENST00000579755.1 | COSM12473 | /compbio/analysis/120718_SN855_0084_AD13D5ACXX_LCNL361/sampleAnalysis/sample18.TRF001338.01/TRF001338.01.vars.final.xml | ACME SEQUENCING LLC | DNA | TARGETED GENOME SEQUENCING | 1 | Day 1 | 1 | 2018-05-22 | 2 |
| 9 | ABC-123 | GF | 123101 | ACME GenePanel 500 | 9 | 2 | TRF001338 | CPNUMVAR | Copy Number Variation | COPY NUMBER ALTERATION INTERPRETATION | loss |  | loss |  |  | SOMATIC VARIATION | GRCh37.75 | 9 | CDKN2A | GENE WITH PROTEIN PRODUCT | 21967751 | ENST00000579755.1 | COSM12473 | /compbio/analysis/120718_SN855_0084_AD13D5ACXX_LCNL361/sampleAnalysis/sample18.TRF001338.01/TRF001338.01.vars.final.xml | ACME SEQUENCING LLC | DNA | TARGETED GENOME SEQUENCING | 1 | Day 1 | 1 | 2018-05-22 | 2 |

Identifying information for the gene panel used to generate the result is in the DI domain. The gene panel is represented in SDTM, as the panel used as part of the wet laboratory methodology may change and affects interpretation of the result. The platform in which the gene panel was used is not represented, because it does not provide additional context for the result.

The DI example shows the device type and manufacturer for the device identified as ACME GenePanel 500.

*di.xpt*

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | DI | ACME GenePanel 500 | 1 | DEVTYPE | Device Type | Gene Panel |
| 2 | ABC-123 | DI | ACME GenePanel 500 | 2 | MANUF | Manufacturer | ACME |

**Example 2**
This example shows findings from an assessment of a known single nucleotide variant in gene ABCG2 using wet laboratory methodology real-time polymerase chain reaction. Findings from this assessment show the genotypes from DNA extracted from the blood of 3 individuals, each with a different genotype at the genetic locus of interest. Because the DNA specimen was extracted from normal blood, the inheritability of the variation is considered to be in the germline.
**Row 1:** Shows a subject genotype which is homozygous for the variant nucleotide in the reference sequence.
**Row 2:** Shows a subject genotype which is heterozygous for the nucleotide in the reference sequence.
**Row 3:** Shows a subject genotype which is homozygous for the nucleotide in the reference sequence.
*gf.xpt*

| Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFREFID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFORREF | GFSTRESC | GFSTREFC | GFINHERT | GFGENREF | GFCHROM | GFSYM | GFSYMTYP | GFGENLOC | GFSEQID | GFPVRID | GFNAM | GFSPEC | GFMETHOD | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | C12345 | GF | C12345-001 | 1 | NA18537 | SNV | Single Nucleotide Variation | GENOTYPE | T/T | G/G | T/T | G/G | GERMLINE VARIATION | GRCh38.p13 | 4 | ABCG2 | GENE WITH PROTEIN PRODUCT | 4:88131171 | ENSG00000118777 | rs2231142 | ACME LABS | DNA | REAL-TIME POLYMERASE CHAIN REACTION | 1 | SCREENING | -1 | 2020-06-25 | -3 |
| 2 | C12345 | GF | C12345-002 | 2 | NA07000 | SNV | Single Nucleotide Variation | GENOTYPE | G/T | G/G | G/T | G/G | GERMLINE VARIATION | GRCh38.p13 | 4 | ABCG2 | GENE WITH PROTEIN PRODUCT | 4:88131171 | ENSG00000118777 | rs2231142 | ACME LABS | DNA | REAL-TIME POLYMERASE CHAIN REACTION | 1 | SCREENING | -1 | 2020-06-25 | -3 |
| 3 | C12345 | GF | C12345-003 | 3 | NA00131 | SNV | Single Nucleotide Variation | GENOTYPE | G/G | G/G | G/G | G/G | GERMLINE VARIATION | GRCh38.p13 | 4 | ABCG2 | GENE WITH PROTEIN PRODUCT | 4:88131171 | ENSG00000118777 | rs2231142 | ACME LABS | DNA | REAL-TIME POLYMERASE CHAIN REACTION | 1 | SCREENING | -1 | 2020-06-25 | -3 |

**Example 3**
This example shows transcription levels of genes ACTB and GAPDH and summarized scores from the transcription levels. Transcription levels and scores were determined using biocomputational analysis with wet laboratory methodology targeted transcriptome sequencing. Specific formulas used in biocomputational analyses to generate normalized and summarized score results are respresented when applicable.
**Rows 1, 7:** Show the number of fragments counted corresponding to the indicated gene.
**Rows 2-4, 8-10:** Show normalized transcription levels based on the normalization methods noted in variable GFANMETH and the raw fragment count reported in rows 1 and 7.
**Rows 5, 11:** Show the percentile rank of the indicated gene among those genes reported in the indicated panel.
**Rows 6, 12:** Show the predicted expression status of the indicated gene based on a threshold established by the assay.
**Rows 13-14:** Show normalized transcription levels based on the normalization methods noted in variable GFANMETH and the raw fragment count reported in rows 1 and 7.
**Rows 15-16:** Show gene signature scores from summarization of genetic data based on the methods noted in variable GFANMETH.
*gf.xpt*

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | GFSEQ | GFGRPID | GFREFID | GFSPID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFORRESU | GFSTRESC | GFSTRESN | GFSTRESU | GFGENREF | GFCHROM | GFSYM | GFSYMTYP | GFSEQID | GFXFN | GFNAM | GFSPEC | GFMETHOD | GFANMETH | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 1 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | FRAGMENT COUNT | 36 |  | 36 | 36 |  | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING |  | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 2 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 2 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 0.5679 | /MBP | 0.5679 | 0.5679 | /MBP | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | FRAGMENTS PER KILOBASE MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 3 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 3 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 1.0523 | /10^6 | 1.0523 | 1.0523 | /10^6 | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | COUNTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 4 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 4 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 1.9935 | /MBP | 1.9935 | 1.9935 | /MBP | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | TRANSCRIPTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 5 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 5 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | PERCENTILE RANK | 0.37 | % | 0.37 | 0.37 | % | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING |  | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 6 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 6 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | GENETIC TRANSCRIPTION INDICATOR | no |  | no |  |  | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING |  | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 7 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 7 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | FRAGMENT COUNT | 23658 |  | 23658 | 23658 |  | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING |  | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 8 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 8 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 148.6268 | /MBP | 148.6268 | 148.6268 | /MBP | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | FRAGMENTS PER KILOBASE MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 9 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 9 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 691.5607 | /10^6 | 691.5607 | 691.5607 | /10^6 | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | COUNTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 10 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 10 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 521.716 | /MBP | 521.716 | 521.716 | /MBP | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | TRANSCRIPTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 11 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 11 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | PERCENTILE RANK | 0.99 | % | 0.99 | 0.99 | % | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING |  | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 12 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 12 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | GENETIC TRANSCRIPTION INDICATOR | yes |  | yes |  |  | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING |  | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 13 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 13 | 1 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 0.056299177 |  | 0.056299177 | 0.056299177 |  | GRCh38.p12 |  | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 |  | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 14 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 14 | 1 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 0.046787999 |  | 0.046787999 | 0.046787999 |  | GRCh38.p12 |  | GAPDH | GENE WITH PROTEIN PRODUCT | NM_001256799.3 |  | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 15 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 15 | 2 | ABC1234567 | AP483910 | GENESIG | Gene Signature | GENETIC TRANSCRIPTION INTERPRETATION | LOW |  | LOW |  |  | GRCh38.p12 |  | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 |  | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | IFN-1 GENE SIGNATURE | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 16 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 16 | 3 | ABC1234567 | AP483910 | GENESIG | Gene Signature | SCORE | 1.126819661 |  | 1.126819661 | 1.126819661 |  | GRCh38.p12 |  | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 |  | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | IFN-1 GENE SIGNATURE | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |

Identifying information for the gene panel used to generate the result is in the DI domain. The gene panel is represented in SDTM, as the panel used as part of the wet laboratory methodology may change and affects interpretation of the result. The platform in which the gene panel was used is not represented, because it does not provide additional context for the result.

The DI example shows the device type and manufacturer for the device identified as ACME GenePanel 250.

*di.xpt*

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | DI | ACME GenePanel 250 | 1 | DEVTYPE | Device Type | Gene Panel |
| 2 | ABC-123 | DI | ACME GenePanel 250 | 2 | MANUF | Manufacturer | ACME |

**Example 4**
This example shows findings from an assessment of microsatellite instability for genetic subregions that are known to be unstable. DNA extracted from tumor tissue is amplified and the resulting amplicons are resolved using wet laboratory methodology capillary electrophoresis.
**Row 1:** Shows the summarized interpretation of overall microsatellite instability.
**Rows 2-6:** Show whether microsatellite instability is detected in the genetic subregions indicated.
*gf.xpt*

| Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFREFID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFSTRESC | GFGENSR | GFXFN | GFNAM | GFSPEC | GFMETHOD | GFRUNID | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | GF | 123101 | 1 | 44014702-6 | MICRISTB | Microsatellite Instability | MICROSATELLITE INSTABILITY OVERALL STATUS | MSI-Stable | MSI-Stable |  | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MSI010418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 2 | ABC123 | GF | 123101 | 2 | 44014702-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | BAT-25 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MSI010418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 3 | ABC123 | GF | 123101 | 3 | 44014702-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | BAT-26 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MSI010418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 4 | ABC123 | GF | 123101 | 4 | 44014702-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | MONO-27 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MSI010418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 5 | ABC123 | GF | 123101 | 5 | 44014702-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | NR-21 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MSI010418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 6 | ABC123 | GF | 123101 | 6 | 44014702-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | NR-24 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MSI010418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |

**Example 5**
This example includes 3 datasets (i.e., MB and MS in addition to GF). The purpose of this 3-part example is to illustrate how these domains are appropriately used in cases where the concepts in each domain are very closely related. Specifically, the example demonstrates the use of these domains by following a subject through a hypothetical scenario of influenza diagnosis, genetic evaluation of the virus, and interpretation of drug susceptibility resulting from genetic testing.

Tests that diagnose or identify the presence of an infectious agent in a subject sample are represented in the MB domain, regardless of the methodology used. In this example, the subject was diagnosed with influenza A H3N2 via a nucleic acid amplification test (NAAT) at the baseline visit. MBTEST = "Microbial Organism Identification" because the assay does not specifically test for the presence of 1 organism or subtype to the exclusion of all others.

*mb.xpt*

| Row | STUDYID | DOMAIN | USUBJID | MBSEQ | MBREFID | MBTESTCD | MBTEST | MBORRES | MBSTRESC | MBSPEC | MBLOC | MBMETHOD | VISITNUM | VISIT | MBDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | INFLU122 | MB | INF01-01 | 1 | INFLU0101 | MCORGIDN | Microbial Organism Identification | INFLUENZA A VIRUS SUBTYPE H3N2 | INFLUENZA A VIRUS SUBTYPE H3N2 | MUCUS | NOSTRIL | NUCLEIC ACID AMPLIFICATION TEST | 1 | BASELINE | 2020-06-11 |

Next, a series of virus samples extracted from the subject underwent targeted single nucleotide polymorphism (SNP) testing to determine the feasibility of using the neuraminidase inhibitor oseltamivir to treat the infection (i.e., drug susceptibility testing).

Findings from this testing provide both genetic data in the form of the genotype identified and the susceptibility/resistance data as inferred phenotype. Genotypic findings are represented in the GF domain, and inferred susceptibility/resistance in MS.

The GFTEST "Single Nucleotide Variation" is used for SNP tests. GFTSTDTL indicates that the results are expressed as predicted amino acid change instead of nucleotide change. GFSYM = "NA", the published gene symbol for the influenza neuraminidase gene. GFGENLOC represents the position in the protein sequence where the targeted variation which confers resistance to oseltamivir occurs. GFSEQID is the reference sequence/segment to which the results are compared.

Note the use of NHOID, which is populated with the name of the organism to which the testing applies. Note: It is important to use this identifier to distinguish between tests that apply to a non-host organism and tests that apply to the study subject/host.

GFLNKID serves as the link between this dataset and the MS dataset which follows.
**Row 1:** Shows the result of a targeted test to detect a single nucleotide polymorphism in the influenza neuraminidase gene known to confer resistance to the drug oseltamivir. The result (R292R) indicates that the amino acid residue R (arginine) at position 292 remains unchanged at the baseline visit.
**Rows 2-3:** Show the results of the same targeted test at the day 2 and day 5 visits. The results (R292K) show that a mutation has occurred at position 292 from the amino acid R (arginine) to the amino acid K (lysine).
*gf.xpt*

| Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFREFID | NHOID | GFLNKID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFSTRESC | GFSYM | GFGENLOC | GFSEQID | GFSPEC | GFMETHOD | VISITNUM | VISIT | GFDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | INFLU122 | GF | INF01-01 | 1 | INFLU0101.1 | INFLUENZA A H3N2 | GF-MS01 | SNV | Single Nucleotide Variation | PREDICTED AMINO ACID CHANGE | R292R | R292R | NA | 292 | U43427 | RNA |  | 1 | BASELINE | 2020-06-11 |
| 2 | INFLU122 | GF | INF01-01 | 2 | INFLU0102 | INFLUENZA A H3N2 | GF-MS02 | SNV | Single Nucleotide Variation | PREDICTED AMINO ACID CHANGE | R292K | R292K | NA | 292 | U43427 | RNA |  | 2 | DAY 2 | 2020-06-12 |
| 3 | INFLU122 | GF | INF01-01 | 3 | INFLU0103 | INFLUENZA A H3N2 | GF-MS03 | SNV | Single Nucleotide Variation | PREDICTED AMINO ACID CHANGE | R292K | R292K | NA | 292 | U43427 | RNA |  | 3 | DAY 5 | 2020-06-15 |

The susceptibility data stemming from this genetic testing above are represented in MS (see Section 6.3.5.7.2, Microbiology Susceptibility, assumption 1b). GFLINKID matches MSLNKID to connect the records in GF with the corresponding conclusion regarding susceptibility in MS. As above, NHOID is used to indicate that influenza A H3N2 is the focus of these records. MSAGENT represents the drug to which the results of susceptible or resistant pertain.
**Row 1:** Shows the influenza extracted from the subject at the baseline visit is susceptible to oseltamivir.
**Rows 2-3:** Show the influenza extracted from the subject at the day 2 and day 5 visits is resistant to oseltamivir.
*ms.xpt*

| Row | STUDYID | DOMAIN | USUBJID | MSSEQ | MSREFID | NHOID | MSLNKID | MSTESTCD | MSTEST | MSAGENT | MSORRES | MSSTRESC | MSMETHOD | VISITNUM | VISIT | MSDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | INFLU122 | MS | INF01-01 | 1 | INFLU0101.1 | INFLUENZA A H3N2 | GF-MS-01 | MICROSUS | Microbial Susceptibility | OSELTAMIVIR | SUSCEPTIBLE | SUSCEPTIBLE |  | 1 | BASELINE | 2020-06-11 |
| 2 | INFLU122 | MS | INF01-01 | 2 | INFLU0102 | INFLUENZA A H3N2 | GF-MS-02 | MICROSUS | Microbial Susceptibility | OSELTAMIVIR | RESISTANT | RESISTANT |  | 2 | DAY 2 | 2020-06-12 |
| 3 | INFLU122 | MS | INF01-01 | 3 | INFLU0103 | INFLUENZA A H3N2 | GF-MS-03 | MICROSUS | Microbial Susceptibility | OSELTAMIVIR | RESISTANT | RESISTANT |  | 3 | DAY 5 | 2020-06-15 |

The relrec dataset example shows the relationship between the genetic assessment in GF and the resistance/susceptibility data in MS.

*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PS001 | GF |  | GFLNKID |  | ONE | 1 |
| 2 | PS001 | MS |  | MSLNKID |  | ONE | 1 |

#### 6.3.5.5 Immunogenicity Specimen Assessments (IS)

##### IS – Description/Overview
A findings domain for assessments of antigen induced humoral or cell-mediated immune response in the subject.


##### IS – Specification
is.xpt, Immunogenicity Specimen Assessments — Findings. One record per test per visit per subject, Tabulation.

**Structure:** One record per test per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | IS |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | NHOID | Non-host Organism ID | Char | Identifier | Perm |  |
| 5 | ISSEQ | Sequence Number | Num | Identifier | Req |  |
| 6 | ISGRPID | Group ID | Char | Identifier | Perm |  |
| 7 | ISREFID | Reference ID | Char | Identifier | Perm |  |
| 8 | ISSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 9 | ISTESTCD | Immunogenicity Test/Exam Short Name | Char | Topic | Req | C120525 |
| 10 | ISTEST | Immunogenicity Test or Examination Name | Char | Synonym Qualifier | Req | C120526 |
| 11 | ISTSTCND | Test Condition | Char | Variable Qualifier | Perm | C181175 |
| 12 | ISCNDAGT | Test Condition Agent | Char | Record Qualifier | Perm |  |
| 13 | ISBDAGNT | Binding Agent | Char | Variable Qualifier | Perm | C85491; C181169 |
| 14 | ISTSTOPO | Test Operational Objective | Char | Variable Qualifier | Perm | C181170 |
| 15 | ISMSCBCE | Molecule Secreted by Cells | Char | Variable Qualifier | Perm |  |
| 16 | ISTSTDTL | Test Detail | Char | Variable Qualifier | Perm |  |
| 17 | ISCAT | Category for Immunogenicity Test | Char | Grouping Qualifier | Perm |  |
| 18 | ISSCAT | Subcategory for Immunogenicity Test | Char | Grouping Qualifier | Perm |  |
| 19 | ISORRES | Results or Findings in Original Units | Char | Result Qualifier | Exp |  |
| 20 | ISORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |
| 21 | ISORNRLO | Reference Range Lower Limit in Orig Unit | Char | Variable Qualifier | Exp |  |
| 22 | ISORNRHI | Reference Range Upper Limit in Orig Unit | Char | Variable Qualifier | Exp |  |
| 23 | ISSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 24 | ISSTRESN | Numeric Results/Findings in Std. Units | Num | Result Qualifier | Exp |  |
| 25 | ISSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |
| 26 | ISSTNRLO | Reference Range Lower Limit-Std Units | Num | Variable Qualifier | Exp |  |
| 27 | ISSTNRHI | Reference Range Upper Limit-Std Units | Num | Variable Qualifier | Exp |  |
| 28 | ISSTNRC | Reference Range for Char Rslt-Std Units | Char | Variable Qualifier | Perm |  |
| 29 | ISNRIND | Reference Range Indicator | Char | Variable Qualifier | Exp | C78736 |
| 30 | ISSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 31 | ISREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 32 | ISNAM | Vendor Name | Char | Record Qualifier | Perm |  |
| 33 | ISSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734 |
| 34 | ISSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| 35 | ISSPCUFL | Specimen Usability for the Test | Char | Record Qualifier | Perm | C66742 |
| 36 | ISMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 37 | ISLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| 38 | ISBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 39 | ISDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 40 | ISLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Exp |  |
| 41 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 42 | VISIT | Visit Name | Char | Timing | Perm |  |
| 43 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 44 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 45 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 46 | ISDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 47 | ISENDTC | End Date/Time of Specimen Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| 48 | ISDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |
| 49 | ISENDY | Study Day of End of Specimen Collection | Num | Timing | Perm |  |
| 50 | ISTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 51 | ISTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 52 | ISELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 53 | ISTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 54 | ISRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **NHOID**: Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears.
- **ISSEQ**: Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.
- **ISGRPID**: Used to tie together a block of related records in a single domain for a subject.
- **ISREFID**: Internal or external specimen identifier. Example: "458975-01".
- **ISSPID**: Sponsor-defined identifier.
- **ISTESTCD**: Short name of the measurement, test, or examination described in ISTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in ISTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). ISTESTCD cannot contain characters other than letters, numbers, or underscores.
- **ISTEST**: Verbatim name of the test or examination used to obtain the measurement or finding. The value in ISTEST cannot be longer than 40 characters. Example: "Immunoglobulin E".
- **ISTSTCND**: Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed.
- **ISCNDAGT**: The textual description of the agent used to impose a test condition. Examples are different stimulating agents used in immunoassays such as those in the Interferon Gamma Response assay (e.g., Mycobacterium tuberculosis ESAT-6, CFP-10, TB 7.7, Mitogen).
- **ISBDAGNT**: Text description of the agent that is binding to the entity in the ISTEST variable. ISBDAGNT is used to indicate that there is a binding relationship between the entities in the ISTEST and ISBDAGNT variables, regardless of direction.; ISBDAGNT is not a method qualifier. It should only be used when the actual interest of the measurement is the binding interaction between the 2 entities in ISTEST and ISBDAGNT. In other words, the combination of ISTEST and ISBDAGNT should describe the entity or the analyte being measured, without the need for additional variables.; The binding agent may be (but is not limited to) a test article, a portion of the test article, a related compound, an endogenous molecule, an allergen, or an infectious agent.
- **ISTSTOPO**: Text description of the high-level purpose of the test at the operational level. If populated, valid values are "SCREEN", "CONFIRM", and "QUANTIFY".
- **ISMSCBCE**: Text description of the entity secreted by the cells represented in ISTEST. The combination of ISTEST and ISMSCBCE should describe the entity or the analyte being measured, without the need for additional variables.
- **ISTSTDTL**: Further description of ISTESTCD and ISTEST.
- **ISCAT**: Used to define a category of topic-variable values across subjects. Example: "SEROLOGY".
- **ISSCAT**: A further categorization of ISCAT.
- **ISORRES**: Result of the measurement or finding as originally received or collected.
- **ISORRESU**: Original units in which the data were collected. The unit for ISORRES. Examples: "Index Value", "gpELISA", "unit/mL".
- **ISORNRLO**: Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results.
- **ISORNRHI**: Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results.
- **ISSTRESC**: Contains the result value for all findings copied or derived from ISORRES, in a standard format or in standard units. ISSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in ISSTRESN.
- **ISSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from ISSTRESC. ISSTRESN should store all numeric test results or findings.
- **ISSTRESU**: Standardized units used for ISSTRESC and ISSTRESN. Examples: "Index Value", "gpELISA", "unit/mL".
- **ISSTNRLO**: Lower end of reference range for continuous measurements for ISSTRESC/ISSTRESN in standardized units. Should be populated only for continuous results.
- **ISSTNRHI**: Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results.
- **ISSTNRC**: For normal range values that are character in ordinal scale or if categorical ranges were supplied. Examples: "-1 to +1", "NEGATIVE TO TRACE".
- **ISNRIND**: Indicates where the value falls with respect to reference range defined by ISORNRLO and ISORNRHI, ISSTNRLO and ISSTNRHI, or by ISSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW".; Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether ISNRIND refers to the original or standard reference ranges and results.; Should not be used to indicate clinical significance.
- **ISSTAT**: Used to indicate a test was not done. Should be null if a result exists in ISORRES.
- **ISREASND**: Describes why a measurement or test was not performed. Used in conjunction with ISSTAT when value is "NOT DONE".
- **ISNAM**: Name or identifier of the laboratory or vendor who provided the test results.
- **ISSPEC**: Defines the types of specimen used for a measurement. Example: "SERUM".
- **ISSPCCND**: Free or standardized text describing the condition of the specimen. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC".
- **ISSPCUFL**: Describes the usability of the specimen for the test. The value will be "N" if the specimen is not usable, and null if the specimen is usable.
- **ISMETHOD**: Method of the test or examination. Examples: "ELISA", "ELISPOT".
- **ISLOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **ISBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that ISBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.
- **ISDRVFL**: Used to indicate a derived record. The value should be "Y" or null. Examples of records that might be derived for the submission datasets include those that represent the average of other records, do not come from the CRF, or are not as originally received or collected. If ISDRVFL="Y", then ISORRES may be null, with ISSTRESC and (if numeric) ISSTRESN having the derived value.
- **ISLLOQ**: Indicates the lower limit of quantitation for an assay. Units will be those used for ISSTRESU.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm.
- **EPOCH**: Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.
- **ISDTC**: Collection date and time of an observation.
- **ISENDTC**: End date/time of the observation.
- **ISDY**: Actual study day of visit/collection/exam expressed in integer days relative to sponsor-defined RFSTDTC in Demographics.
- **ISENDY**: Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.
- **ISTPT**: Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See ISTPTNUM and ISTPTREF. Examples: "Start", "5 min post".
- **ISTPTNUM**: Numerical version of ISTPT to aid in sorting.
- **ISELTM**: Planned elapsed time (in ISO 8601) relative to a planned fixed reference (ISTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable. Represented as ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by ISTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by ISTPTREF.
- **ISTPTREF**: Name of the fixed reference point referred to by ISELTM, ISTPTNUM, and ISTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **ISRFTDTC**: Date/time of the reference time point, ISTPTREF.


##### IS – Assumptions
1. The Immunogenicity Specimen Assessments (IS) domain holds assessments that describe whether a therapy (e.g., biologic, drug, vaccine) provoked/caused/induced an immune response in a subject. The response can be either positive or negative. For example, a vaccine is expected to induce a beneficial immune response, whereas a cellular therapy (e.g., erythropoiesis-stimulating agents) may cause an adverse immune response.
2. The IS domain also holds assessments that describe whether an allergen, microorganism, or endogenous molecule provoked/caused/induced an immune response in a subject, such as a subject’s antibody reaction (autoantibodies) against auto/self-antigens for autoimmune studies or antibody production in response to allergens in allergy trials. Expected outputs can be positive or negative, present or absent for the antibody of interest, as well as quantification of the antibody. Assessments pertaining to antibodies produced in response to microbial infection will also be represented in the IS domain.
3. Assessments about all other types of “induced” humoral (antibody) immune response in a subject (e.g., antibodies against human leukocyte antigen (HLA) proteins) will also be represented in the IS domain.
4. Certain types of cellular immune responses will also be modeled in IS using non-flow cytometry techniques (see example 6). Flow cytometry data should be modeled in the Cell Phenotype Findings (CP) domain, section 6.3.5.3.
5. An exception is made to the class of antigen/antibody (Ag/Ab) combination assays. Microbial antigen/antibody (Ag/Ab) combination tests should be represented in the Microbiology Specimen (MB) domain. An example is fourth-generation HIV Ag/Ab combination tests, which are commonly seen as HIV identification or detection assays rather than tests that provide additional details on and characterization of a subject’s immunological responses. The outputs of these assays can be expected as reactive, non-reactive, or indeterminate. Whereas some tests generate separate outputs for antigen and antibody, others just indicate “reactive” when either or both are detected. Output is generally based on relative light units, where a result of “reactive” typically requires the signal to cutoff ratio to be greater than 1.
6. Measurements of cytokines, chemokines, and complement proteins should be represented in the Laboratory Test Results (LB) domain.
7. The IS domain variable ISBDAGNT (Binding Agent) is currently supported by 2 Controlled Terminology codelists: Microorganism (MICROORG) and Binding Agent for Immunogenicity Tests (ISBDAGT). Controlled Terminology Rules for Immunogenicity Tests describes how and when to use each codelist (see https://www.cdisc.org/standards/terminology/controlled-terminology).
    a. For antidrug antibody (ADA) tests, the ISBDAGNT variable is used to represent the free-text description of the name/identity of the therapy the antidrug antibody targets. CDISC does not control study therapy names (e.g., drugs, biologics). For ADA tests as a part of regulatory agency submissions, the proprietary binding study therapy name(s) should be considered as extended values of the ISBDAGT codelist when represented in Define-XML.
    b. For mixed-allergens panel tests, submission values represented in the ISBDAGNT variable should follow this format: “XXX, Multiple” (e.g., Dairy Mix Antigens, Multiple; Animal Mix Antigens, Multiple; use the plural form for the word “antigen” if needed). Should the sponsor wish to specify the individual antigens in a mixed antigens panel (e.g., ISBDAGNT = “Animal Mix Antigens, Multiple”), put the names of the specific antigens in Suppqual (e.g., Cat, Dog, Cow, Horse; see example 11).
8. The IS domain variable ISTSTOPO (Test Operational Objective) is supported by a nonextensible Controlled Terminology codelist containing the values SCREEN, CONFIRM, and QUANTIFY.
9. For vaccine studies, in order to distinguish collected data between study vaccine-induced immunogenicity and immunogenicity findings unrelated to the study vaccine (i.e., immunity as a result of natural infection or previous vaccination), the following ISCAT and ISSCAT values are recommended (see example 5):
    a. For immunological data pertaining to the study vaccine, ISCAT = STUDY VACCINE-RELATED IMMUNOGENICITY.
    b. For immunological data collected during the vaccine trial but which are not assessments about the study vaccine, ISCAT = NON-STUDY-RELATED IMMUNOGENICITY.
    c. For assessments measuring the induced-antibody response, ISSCAT = HUMORAL IMMUNITY.
    d. For assessments measuring the induced-cellular response, ISSCAT = CELLULAR IMMUNITY.
10. Any Identifier variables, Timing variables, or Findings general observation class qualifiers may be added to the IS domain.


##### IS – Examples

**Example 1**
This example shows data from tiered testing of antidrug antibody (ADA).
Tiered testing scheme for ADA evaluation generally includes the following steps: screening, confirmatory, and "characterization" of the antidrug antibody. In tier 1, all evaluable samples are run in a screening assay. Samples that are positive for ADA in the screen assay are then analyzed in a confirmatory assay (tier 2). The samples that are positive for ADA in both the screen and confirmatory tiers of testing are further tested in tier 3; this frequently includes analysis of antibody titer and neutralizing activity. In order to illustrate the distinctive differences between the 3 tiers of ADA testing, the standard variable ISTSTOPO is used to represent the controlled values SCREEN, CONFIRM, and QUANTIFY. These values help to describe the operational objective or the reason behind each testing step/tier, and also to provide uniqueness to each row of record. The study drug AZ-007, which induces the subject's production of, and is the target of the antidrug antibody, is represented by the variable ISBDAGNT. ISGRPID is used in this example to show that the records are related to each other; in this particular case, tests are done in a tiered, sequential manner from screen to confirm to quantification of the detected antidrug antibody.
Lastly, antibody titer is often defined as the reciprocal of the lowest dilution of a sample generating a signal that is above the assay cut-point. Alternatively, the titer is defined as the reciprocal of the dilution of a sample generating a signal that is equivalent to the assay cut-point, calculated by an interpolation formula provided in an assay specific bioanalytical method.
**Row 1:** Shows the screening of the presence of ADA to drug AZ-007.
**Row 2:** Shows the confirmation of the previously detected ADA to drug AZ-007.
**Row 3:** Shows the measurement of titer of the ADA from the screen and confirmatory steps.
*is.xpt*

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | IS | ABC-002 | 1 | V555 | 1 | ADA_BAB | Binding Antidrug Antibody | DRUG AZ-007 | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 2 | ABC | IS | ABC-002 | 2 | V555 | 1 | ADA_BAB | Binding Antidrug Antibody | DRUG AZ-007 | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 3 | ABC | IS | ABC-002 | 3 | V555 | 1 | ADA_BAB | Binding Antidrug Antibody | DRUG AZ-007 | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 50 | titer | 50 | 50 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |

**Example 2**
This example shows data from various subtypes of ADA tests.
Although most ADAs do not inhibit the pharmacodynamic activity of a drug, neutralizing antidrug antibodies (NAbs) can inhibit drug activity soon after a drug is administered. Most ADAs (those that are not classified as NAbs) can lower the drug's systemic exposure by increasing the rate of drug clearance, resulting in a clinically similar outcome to that of NAbs (i.e., reduced clinical efficacy).
In this example, the administered drug is an analogue of an endogenous protein. The example data include ADA reactions against both the administered drug and the endogenous protein. Both the study drug and the endogenous protein are represented by the standard variable ISBDAGNT, which qualifies ISTEST. The variable ISTSTOPO, is also used in this dataset to describe the purpose of each testing step, and provides uniqueness among similar records. ISGRPID is used to show which records are related in this dataset.
Note that, in this example, even though only confirmatory records are reported and shown, it is assumed that the screening step has also been performed.
**Rows 1-2:** Show the confirmation and quantification of binding ADA to coagulation factor VIII analogue drug. A binding antidrug antibody is an antibody that binds to a drug.
**Rows 3-4:** Show the confirmation and quantification of the neutralizing binding ADA to coagulation factor VIII analogue drug. A neutralizing binding antidrug antibody is a type of ADA that binds to the functional portion of a drug, leading to diminished or negated pharmacological activity. The neutralizing ADAs are a subset of the total ADAs.
**Rows 5-6:** Show the confirmation and quantification of the cross-reactive binding ADA to the endogenous coagulation factor VIII. A cross-reactive binding antidrug antibody is a type of ADA that binds to endogenous molecules, also a subset of the total ADAs.
**Rows 7-8:** Show the confirmation and quantification of the neutralizing cross-reactive binding ADA to the endogenous coagulation factor VIII. Neutralizing cross-reactive binding antidrug antibodies are a type of ADA that bind to endogenous molecules, leading to diminished or negated function; in some cases, they may also bind and negate the function of the study drug. They are a subset of the total ADAs.
*is.xpt*

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | IS | ABC-001 | 1 | A42839 | 1 | ADA_BAB | Binding Antidrug Antibody | COAGULATION FACTOR VIII ANALOGUE DRUG | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 2 | ABC | IS | ABC-001 | 2 | A42839 | 1 | ADA_BAB | Binding Antidrug Antibody | COAGULATION FACTOR VIII ANALOGUE DRUG | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 30 | titer | 30 | 30 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 3 | ABC | IS | ABC-001 | 3 | A42839 | 2 | ADA_NAB | Neutralizing Binding Antidrug Antibody | COAGULATION FACTOR VIII ANALOGUE DRUG | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | HEMAGGLUTINATION INHIBITION ASSAY | 1 | VISIT 1 | 2017-07-27 |
| 4 | ABC | IS | ABC-001 | 4 | A42839 | 2 | ADA_NAB | Neutralizing Binding Antidrug Antibody | COAGULATION FACTOR VIII ANALOGUE DRUG | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 60 | titer | 60 | 60 | titer | SERUM | HEMAGGLUTINATION INHIBITION ASSAY | 1 | VISIT 1 | 2017-07-27 |
| 5 | ABC | IS | ABC-001 | 5 | A42839 | 3 | ADA_X | Cross-Reactive Binding Antidrug Antibody | ENDOGENOUS COAGULATION FACTOR VIII | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 6 | ABC | IS | ABC-001 | 6 | A42839 | 3 | ADA_X | Cross-Reactive Binding Antidrug Antibody | ENDOGENOUS COAGULATION FACTOR VIII | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 90 | titer | 90 | 90 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 7 | ABC | IS | ABC-001 | 7 | A42839 | 4 | ADA_NX | Neutraliz Cross-React Bind Antidrug AB | ENDOGENOUS COAGULATION FACTOR VIII | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | HEMAGGLUTINATION INHIBITION ASSAY | 1 | VISIT 1 | 2017-07-27 |
| 8 | ABC | IS | ABC-001 | 8 | A42839 | 4 | ADA_NX | Neutraliz Cross-React Bind Antidrug AB | ENDOGENOUS COAGULATION FACTOR VIII | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 150 | titer | 150 | 150 | titer | SERUM | HEMAGGLUTINATION INHIBITION ASSAY | 1 | VISIT 1 | 2017-07-27 |

**Example 3**
This example shows data about ADA reaction against drug components.
This example shows the production of ADA in response to both the prodrug and its active metabolite. A prodrug is a compound that, after administration, is metabolized into a pharmacologically active drug. Note that, in this example, even though only confirmatory records are reported and shown, it is assumed that the screening step has also been performed.
**Rows 1-2:** Show the confirmation and quantification of the ADA against prodrug A.
**Rows 3-4:** Show the confirmation and quantification of the ADA against the active metabolite of prodrug A.
*is.xpt*

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | IS | ABC-004 | 1 | J123 | 1 | ADA_BAB | Binding Antidrug Antibody | PRODRUG A | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 2 | ABC | IS | ABC-004 | 2 | J123 | 1 | ADA_BAB | Binding Antidrug Antibody | PRODRUG A | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 30 | titer | 30 | 30 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 3 | ABC | IS | ABC-004 | 3 | J123 | 2 | ADA_BAB | Binding Antidrug Antibody | PRODRUG A ACTIVE METABOLITE | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 4 | ABC | IS | ABC-004 | 4 | J123 | 2 | ADA_BAB | Binding Antidrug Antibody | PRODRUG A ACTIVE METABOLITE | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 60 | titer | 60 | 60 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |

**Example 4**
This example shows data about ADA reaction against multiple epitopes of a drug molecule.
This example shows the production of ADA in response to the study biologic drug, peginterferon beta-1a; its active metabolite, active interferon beta 1a; and its immunogenic epitope, PEG epitope of peginterferon beta-1a. An immunogenic epitope of a biologic drug is a particular segment within the drug that is recognized by the immune system, specifically by antibodies, B cells, or T cells. This immunogenic epitope portion of the biologic drug is capable of inducing the production of and therefore the binding of ADAs.
This example also shows when tiered testing stops at the screening step (interferon beta-1a assay) and goes straight to neutralizing antidrug antibody testing. Although this is unusual, it illustrates the flexibility of the fields ISTEST, ISBDAGNT, and ISTSTOPO to incorporate multiple options.
**Row 1:** Shows the presence of ADA against the active metabolite of peginterferon beta-1a, active interferon beta 1a, in subject ABC-007.
**Rows 2-3:** Show the screening and confirmation of ADA against the PEG epitope of peginterferon beta-1a in subject ABC-007.
**Rows 4-5:** Show the screen and quantification of neutralizing ADA against the whole molecule peginterferon beta-1a in subject ABC-007.
**Row 6:** Shows the absence of ADA against the active metabolite of peginterferon beta-1a, active interferon beta 1a portion, in subject ABC-008.
**Rows 7-9:** Show the screening, confirmation, and quantification of ADA against the PEG epitope of peginterferon beta-1a, in subject ABC-008.
*is.xpt*

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | IS | ABC-007 | 1 | A1 | ADA_BAB | Binding Antidrug Antibody | ACTIVE INTERFERON BETA 1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 2 | ABC | IS | ABC-007 | 2 | A1 | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA-1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | ELISA | 1 | VISIT 1 | 2017-07-27 |
| 3 | ABC | IS | ABC-007 | 3 | A1 | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA-1A | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | NEGATIVE |  | NEGATIVE |  |  | SERUM | ELISA | 1 | VISIT 1 | 2017-07-27 |
| 4 | ABC | IS | ABC-007 | 4 | A1 | ADA_NAB | Neutralizing Binding Antidrug Antibody | PEGINTERFERON BETA-1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | REPORTER GENE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 5 | ABC | IS | ABC-007 | 5 | A1 | ADA_NAB | Neutralizing Binding Antidrug Antibody | PEGINTERFERON BETA-1A | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 4.7 | titer | 4.7 | 4.7 | titer | SERUM | REPORTER GENE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 6 | ABC | IS | ABC-008 | 6 | V4 | ADA_BAB | Binding Antidrug Antibody | ACTIVE INTERFERON BETA 1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | NEGATIVE |  | NEGATIVE |  |  | SERUM | IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 7 | ABC | IS | ABC-008 | 7 | V4 | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA-1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | ELISA | 1 | VISIT 1 | 2017-07-27 |
| 8 | ABC | IS | ABC-008 | 8 | V4 | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA-1A | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE |  | POSITIVE |  |  | SERUM | ELISA | 1 | VISIT 1 | 2017-07-27 |
| 9 | ABC | IS | ABC-008 | 9 | V4 | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA-1A | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 75 | titer | 75 | 75 | titer | SERUM | ELISA | 1 | VISIT 1 | 2017-07-27 |

**Example 5**
This example illustrates how to represent both study vaccine-induced humoral (antibody) immunity, and immunogenicity responses not related to the study vaccine but which are also important for collection, specifically in vaccine trials.
In this case, the subject was administered with a human respiratory syncytial virus (RSV) vaccine and his protective antibody production against the major component of the study vaccine, RSV-protein B, was assessed. Detection and quantification of the anti-RSV-protein B antibody data from baseline to post-vaccination were collected and are represented below. At baseline, antibody against RSV-protein Z was detected in the same subject, which suggests either natural infection by or previous vaccination with RSV-protein B at the time of assessment. Even though immunity against RSV-protein B was not the interest of the RSV vaccine study, immunological data pertaining to RSV-protein B was collected for the subject.
This example illustrates the use of the CDISC-recommended ISCAT values "STUDY VACCINE-RELATED IMMUNOGENICITY" and "NON-STUDY-RELATED IMMUNOGENICITY" to distinguish between study vaccine-induced immunogenicity and immunogenicity findings unrelated to the study vaccine data collected during a vaccine study. ISCAT = "NON-STUDY-RELATED IMMUNOGENICITY" was developed to explicitly and purposefully indicate whether an observed immunity toward an antigen was not related to the study vaccine but rather was a result of natural infection or previous vaccination. Oftentimes, it is simply impossible to tell whether the antibody found in a subject is due to a natural infection or previous vaccination (or both)--yet this immunogenicity, unrelated to the study vaccine, is important for collection and assessment at the screening phase of the trial.
In this example, immune responses against RSV-protein Z were measured during the study. Because protein Z is not inserted into the vaccine vector, any immune response detected toward protein Z was not related to the study vaccine, although important for assessment and collected per the study protocol. In order to show that RSV-protein Z-induced antibody production was unrelated to the immunity solicited by the study vaccine RSV-protein B (ISCAT = "STUDY VACCINE-RELATED IMMUNOGENICITY"), the ISCAT for rows 3 and 4 is "NON-STUDY-RELATED IMMUNOGENICITY" (note: protein Z and protein B are examples, refer to controlled terminology for standard terms associated with ISBDAGNT).
**Rows 1-2:** Show the screening and quantification of microbial-induced immunoglobulin G (IgG) antibody against the RSV-protein B at baseline, prior to the administration of the study vaccine. ISBDAGNT="HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B" is the immunogenic target in the study vaccine that could potentially stimulate the production of antibodies. Note: ISCAT="STUDY VACCINE-RELATED IMMUNOGENICITY", even though at this point the study vaccine has not been administered to the subject; this is done purposefully to enable the grouping of baseline and treatment measurements.
**Rows 3-4:** Show the screening and quantification of microbial-induced IgG antibody against the RSV-protein Z at baseline. Note: Because RSV-protein Z is not the immunogenic target of interest in this vaccine study, ISCAT is populated with the value "NON-STUDY RELATED IMMUNOGENICITY".
**Rows 5-7:** Show the titer of microbial-induced IgG antibody against the RSV-protein B, post-vaccination at visits 1, 2, and 3. These 3 records show the antibody titers had increased post-vaccination, presumably due to the stimulation from the RSV study vaccine. ISCAT is populated with the value "STUDY VACCINE-RELATED IMMUNOGENICITY".
*is.xpt*

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RSV1230 | IS | RSV1230-011 | 1 | 13668 | 1 | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | SCREEN | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | POSITIVE | POSITIVE |  |  | SERUM | ELISA | 1 | BASELINE | 2017-05-27 |
| 2 | RSV1230 | IS | RSV1230-011 | 2 | 13668 | 1 | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:25 | 25 | 25 | titer | SERUM | ELISA | 1 | BASELINE | 2017-05-27 |
| 3 | RSV1230 | IS | RSV1230-011 | 1 | 13668 | 2 | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN Z | SCREEN | NON-STUDY-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | POSITIVE | POSITIVE |  |  | SERUM | ELISA | 1 | BASELINE | 2017-05-27 |
| 4 | RSV1230 | IS | RSV1230-011 | 2 | 13668 | 2 | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN Z | QUANTIFY | NON-STUDY-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:120 | 120 | 120 | titer | SERUM | ELISA | 1 | BASELINE | 2017-05-27 |
| 5 | RSV1230 | IS | RSV1230-011 | 1 | 13669 |  | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:90 | 90 | 90 | titer | SERUM | ELISA | 2 | VISIT 1 | 2017-07-27 |
| 6 | RSV1230 | IS | RSV1230-011 | 2 | 13670 |  | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:220 | 220 | 220 | titer | SERUM | ELISA | 3 | VISIT 2 | 2017-08-27 |
| 7 | RSV1230 | IS | RSV1230-011 | 3 | 13671 |  | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:500 | 500 | 500 | titer | SERUM | ELISA | 4 | VISIT 3 | 2017-09-27 |

Thus far, all the IS tests illustrated are measurements of concentrations of a substance (e.g., antibody titer). However, some immunogenicity tests are actual counts of immune cells that secrete a particular substance. These tests are described by the combination of ISTEST (Immunogenicity Test or Examination Name) and ISMSCBCE (Molecule Secreted by Cells), where ISTEST identifies the type of cells that secrete a specific substance (e.g., antibody-secreting cells, cytokine-secreting cells) and ISMSCBCE names the substance (e.g., IgG antibody, interferon-gamma). The following 2 examples introduce the IS domain-specific variable, ISMSCBCE, and illustrate its use with ISTEST to represent a complete immunological analyte of interest.

**Example 6**
This example shows data about the assessment of antibody-secreting cells (ASCs).
Traditional methods such as enzyme-linked immunosorbent assay (ELISA) that monitor humoral immune responses after immunization or infection typically only quantify specific antibody titers in serum. These methods do not provide any information about the actual number and location of the immune cells that secrete antibodies or cytokines.
The enzyme-linked immunospot (ELISpot) assay is a method to detect and quantify analyte-secreting T or B cells. During ELISpot testing, a colored precipitate forms and appears as spots at the sites of analyte localization (analytes typically are cytokines or antibodies), with each individual spot representing an individual analyte-secreting cell. The spots can be counted with an automated ELISpot reader system or manually, using a stereomicroscope. This example shows how to represent the quantification of ASCs as the number of spots per million peripheral blood mononuclear cells (PBMC) as determined by B-cell ELISpot from a vaccine trial.
The IS domain-specific variable ISMSCBCE introduced in this example allows flexibility in data representation and post-coordination of the various secreted antibody types and their respective ASCs. This approach liberates the ISTEST variable from having to house precoordinated and thus hyperspecific values crafted based on secretion and cell types.
**Row 1:** Shows the total number of IgG ASCs from a subject's blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is represented by the variable ISMSCBCE (i.e. IGG antibody non-specific to any antigen).
**Row 2:** Shows the number of H1-specific IgG ASCs from the same subject's blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is in ISMSCBCE (i.e. IgG antibody specific to H1 antigen).
**Row 3:** Shows the number of H3-specific IgG ASCs from the same subject's blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is in ISMSCBCE (i.e. IgG antibody specific to H3 antigen).
*is.xpt*

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISMSCBCE | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | ISDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | INFL456 | IS | INF02-01 | 1 | SAMPBL0201 | ABSCCL | Antibody-secreting Cells | IGG ANTIBODY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 2019 | SFC/10^6 PBMC | 2019 | 2019 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2011-08-08 |
| 2 | INFL456 | IS | INF02-01 | 2 | SAMPBL0201 | ABSCCL | Antibody-secreting Cells | INFLUENZA H1-SPECIFIC IGG ANTIBODY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 626 | SFC/10^6 PBMC | 626 | 626 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2011-08-08 |
| 3 | INFL456 | IS | INF02-01 | 3 | SAMPBL0201 | ABSCCL | Antibody-secreting Cells | INFLUENZA H3-SPECIFIC IGG ANTIBODY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 592 | SFC/10^6 PBMC | 592 | 592 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2011-08-08 |

**Example 7**
This example shows data from the in vitro assessment and quantification of cytokine-secreting immune cells, expressed in number of spot-forming cells (SFC) per million peripheral blood mononuclear cells (PBMC) as determined by T-cell ELISpot from a vaccine trial.
Through vaccination, it is expected that cytokine secretion in immune cells is boosted whenever immune cells encounter the same virus and/or the previously exposed viral antigens. By increasing this cytokine secretion, immune cells aid in the host defense and protection against (re-)infections. In vaccine trials, this can be measured by isolating immune cells (e.g., PBMCs) from subjects at multiple time points during the course of the trial and restimulating them with the virus or its viral antigens in vitro.
In this example, PBMCs were isolated from a subject participating a vaccine study for RSV and restimulated in vitro with either a RSV-antigen or without a stimulating agent. At baseline (i.e., before vaccination), the RSV antigen-stimulated PBMCs produced minimal number of interferon gamma, as expressed in interferon gamma-secreting cells quantified in the number of SFC/10^6 PBMC (row 2), as compared to no stimulation (row 1). Three weeks after vaccination, RSV-antigen stimulated PBMCs (row 4) showed significant increase in the number of interferon-gamma secreting cells compared to no stimulation (row 3) or baseline values (rows 1 and 2). This suggests immunological memory of the immune cells after encountering the same microorganism or its antigens, and the switch of cell state from resting to active.
**Rows 1-2:** Show the measurement of interferon gamma (ISMSCBCE) cytokine-secreting cells (ISTEST) at baseline either with no stimulation (row 1) or stimulated with the RSV-antigen (row 2) in ISCNDAGT, respectively, prior to vaccination.
**Rows 3-4:** Show the measurement of interferon gamma (ISMSCBCE) cytokine-secreting cells (ISTEST) 3 weeks after vaccination and restimulation in vitro with the RSV-antigen (row 4) in ISCNDAGT and no stimulation (row 3), respectively.
*is.xpt*

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISMSCBCE | ISTSTCND | ISCNDAGT | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RSV1230 | IS | RSV1230-011 | 1 | 13668 | CYKSCCL | Cytokine-secreting Cells | INTERFERON GAMMA | WITHOUT STIMULATING AGENT |  | STUDY VACCINE-RELATED IMMUNOGENICITY | CELLULAR IMMUNITY | 5.1 | SFC/10^6 PBMC | 5.1 | 5.1 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 1 | BASELINE | 2017-05-27 |
| 2 | RSV1230 | IS | RSV1230-011 | 2 | 13668 | CYKSCCL | Cytokine-secreting Cells | INTERFERON GAMMA | WITH STIMULATING AGENT | RSV-EPITOPE B | STUDY VACCINE-RELATED IMMUNOGENICITY | CELLULAR IMMUNITY | 10.5 | SFC/10^6 PBMC | 10.5 | 10.5 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 1 | BASELINE | 2017-05-27 |
| 3 | RSV1230 | IS | RSV1230-011 | 3 | 13668 | CYKSCCL | Cytokine-secreting Cells | INTERFERON GAMMA | WITHOUT STIMULATING AGENT |  | STUDY VACCINE-RELATED IMMUNOGENICITY | CELLULAR IMMUNITY | 60.8 | SFC/10^6 PBMC | 60.8 | 60.8 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2 | VISIT 1 | 2017-08-27 |
| 4 | RSV1230 | IS | RSV1230-011 | 4 | 13668 | CYKSCCL | Cytokine-secreting Cells | INTERFERON GAMMA | WITH STIMULATING AGENT | RSV-EPITOPE B | STUDY VACCINE-RELATED IMMUNOGENICITY | CELLULAR IMMUNITY | 260.5 | SFC/10^6 PBMC | 260.5 | 260.5 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2 | VISIT 1 | 2017-08-27 |

The next 2 examples show data from microneutralization and opsonophagocytic killing (OPK) assays, which are used to measure vaccine efficacy and immunoprotectivity.

**Example 8**
In vaccine studies, microneutralization assays are commonly used in assays to quantify viral-specific neutralizing antibodies in a subject's specimen that can block viral infection in vitro, and therefore provide a measure of vaccine efficacy. A neutralizing antibody is an antibody that binds to, blocks, and prevents non-self agents from infecting cells.
When immunizing a subject with a vaccine, the hope is that the vaccine will induce antiviral and humoral-protective antibody responses in the subject; with an effective vaccine, the quantity of virus-specific antibodies that are able to block viral infection are increased. To test the efficacy of a vaccine, a microneutralization test is performed by adding a vaccinated subject's serum and the virus of study interest to cell cultures in vitro. If neutralizing antibodies are present in the subject's serum post-vaccination, those antibodies will bind to, block, and prevent the virus from infecting cells in the culture plates. The neutralization titer is the specific dilution of the antibody that blocks viral infection of the cells. The 50% neutralization titer (also known as NT50), in the context of microneutralization assays, is defined as the antiviral antibody titer that blocks 50% of viral infection of the cells. Note: Some users may represent the 50% neutralization titer as "IC50 titer" or other test descriptors. CDISC recommends mapping all such values in the ISTSTDTL variable.
NHOID is populated with respiratory syncytial virus because this microorganism is the subject of the vaccine efficacy test.
*is.xpt*

| Row | STUDYID | DOMAIN | USUBJID | NHOID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTDTL | ISCAT | ISSCAT | ISORRES | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RSV1230 | IS | RSV1230-011 | RESPIRATORY SYNCYTIAL VIRUS | 1 | 13668 | MBNAB | Neutralizing Microbial-induced Antibody | RESPIRATORY SYNCYTIAL VIRUS | NEUTRALIZING TITER 50% | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:40 | 40 | 40 | titer | SERUM | MICRONEUTRALIZATION ASSAY | 1 | BASELINE | 2017-05-27 |
| 2 | RSV1230 | IS | RSV1230-011 | RESPIRATORY SYNCYTIAL VIRUS | 2 | 13668 | MBNAB | Neutralizing Microbial-induced Antibody | RESPIRATORY SYNCYTIAL VIRUS | NEUTRALIZING TITER 50% | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:80 | 80 | 80 | titer | SERUM | MICRONEUTRALIZATION ASSAY | 2 | VISIT 1 | 2017-07-27 |
| 3 | RSV1230 | IS | RSV1230-011 | RESPIRATORY SYNCYTIAL VIRUS | 3 | 13668 | MBNAB | Neutralizing Microbial-induced Antibody | RESPIRATORY SYNCYTIAL VIRUS | NEUTRALIZING TITER 50% | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:200 | 200 | 200 | titer | SERUM | MICRONEUTRALIZATION ASSAY | 3 | VISIT 2 | 2017-08-27 |

**Example 9**
In vaccine trials, the OPK assay is used as a correlate for immunoprotectivity against antigens, by measuring the functional capacities of vaccine-induced antibodies.
Typically, this test is performed by incubating a subject's post-immunization sera with the bacterial strain of interest, phagocytes, and complement proteins. If antibacterial, functional antibodies are present in the subject's serum, those antibodies will bind to the bacteria together with complement proteins. This subsequently targets the bacteria for opsonization, the ingestion and destruction of invading non-self agents by phagocytes. With vaccination, the quantity of bacterial-specific, functional antibodies are increased, leading to a decreased number of viable bacterial cells in the presence of phagocytes, functional antibodies, and complement. The assay read-out is expressed in by the opsonization index, which is calculated using linear interpolation of the serum dilution containing functional antibody killing the desired percentage (usually 50%) of the bacteria, using a specified algorithm.
NHOID is populated with Staphylococcus aureus 04-02981 because this strain of S. aureus is the subject of the vaccine efficacy test.
*is.xpt*

| Row | STUDYID | DOMAIN | USUBJID | NHOID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTDTL | ISCAT | ISSCAT | ISORRES | ISSTRESC | ISSTRESN | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SAU1230 | IS | SAU1230-011 | STAPHYLOCOCCUS AUREUS 04-02981 | 1 | 13668 | MBFAB | Functional Microbial-induced Antibody | STAPHYLOCOCCUS AUREUS–EPITOPE X | OPSONIZATION INDEX | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 100 | 100 | 100 | SERUM | OPSONOPHAGOCYTIC KILLING ASSAY | 1 | BASELINE | 2017-05-27 |
| 2 | SAU1230 | IS | SAU1230-011 | STAPHYLOCOCCUS AUREUS 04-02981 | 2 | 13668 | MBFAB | Functional Microbial-induced Antibody | STAPHYLOCOCCUS AUREUS–EPITOPE X | OPSONIZATION INDEX | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1000 | 1000 | 1000 | SERUM | OPSONOPHAGOCYTIC KILLING ASSAY | 2 | VISIT 1 | 2017-07-27 |
| 3 | SAU1230 | IS | SAU1230-011 | STAPHYLOCOCCUS AUREUS 04-02981 | 3 | 13668 | MBFAB | Functional Microbial-induced Antibody | STAPHYLOCOCCUS AUREUS–EPITOPE X | OPSONIZATION INDEX | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 5000 | 5000 | 5000 | SERUM | OPSONOPHAGOCYTIC KILLING ASSAY | 3 | VISIT 2 | 2017-09-27 |

**Example 10**
This example shows how to present data from an autoimmune disease study, specifically how to represent information from disease-specific autoantibody tests.
Sjogren's syndrome (SS) is a systemic autoimmune disease characterized by dry eyes and dry mouth. Diagnosis of SS is generally based on the detection of antinuclear antibodies (ANAs), that is, anti-Ro (SS-A) and anti-La (SS-B) antibodies.
**Rows 1-5:** Show the screening (row 1) and quantification (rows 2, 4) of ANAs. Rows 2 and 3 are grouped together using ISGRPID="1a"; this means the titer result in row 2 is specifically related to the particular nuclear staining pattern (i.e., speckled) finding in row 3. The speckled pattern of ANA is typically indicative of SS, systemic lupus, and mixed connective tissue disease. Rows 4 and 5 are grouped together using ISGRPID="1b"; this means the titer result in row 4 is specifically related to the nuclear staining pattern (i.e., nucleolar) finding in row 5. Rows 1 to 5 are grouped together using ISGRPID with values starting with the number "1", indicating that these records are related. The antinuclear antibodies test is post-coordinated and represented by both ISTEST="Autoantibody" and ISBDAGNT="NUCLEAR AUTOANTIGENS".
**Rows 6-11:** Show the screening and quantification of the various SS-specific autoantibodies. SS autoantigens are represented by the ISBDAGNT variable, whereas the ISTEST="Autoantibody".
*is.xpt*

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTDTL | ISTSTOPO | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | IS | XYZ1234 | 1 | 19283746 | 1 | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS |  | SCREEN | POSITIVE |  | POSITIVE |  |  | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 2 | XYZ | IS | XYZ1234 | 2 | 19283746 | 1a | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS |  | QUANTIFY | 1:340 |  | 340 | 340 | titer | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 3 | XYZ | IS | XYZ1234 | 3 | 19283746 | 1a | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS | STAINING PATTERN |  | SPECKLED PATTERN |  | SPECKLED PATTERN |  |  | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 4 | XYZ | IS | XYZ1234 | 4 | 19283746 | 1b | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS |  | QUANTIFY | 1:170 |  | 170 | 170 | titer | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 5 | XYZ | IS | XYZ1234 | 5 | 19283746 | 1b | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS | STAINING PATTERN |  | NUCLEOLAR PATTERN |  | NUCLEOLAR PATTERN |  |  | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 6 | XYZ | IS | XYZ1234 | 1 | 19283746 | 2 | ATAB | Autoantibody | SJOGRENS SS-A60 ANTIGEN |  | SCREEN | POSITIVE |  | POSITIVE |  |  | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 7 | XYZ | IS | XYZ1234 | 2 | 19283746 | 2 | ATAB | Autoantibody | SJOGRENS SS-A60 ANTIGEN |  | QUANTIFY | 181 | U/mL | 181 | 181 | U/mL | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 8 | XYZ | IS | XYZ1234 | 3 | 19283746 | 3 | ATAB | Autoantibody | SJOGRENS SS-A52 ANTIGEN |  | SCREEN | POSITIVE |  | POSITIVE |  |  | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 9 | XYZ | IS | XYZ1234 | 4 | 19283746 | 3 | ATAB | Autoantibody | SJOGRENS SS-A52 ANTIGEN |  | QUANTIFY | 51 | U/mL | 51 | 51 | U/mL | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 10 | XYZ | IS | XYZ1234 | 5 | 19283746 | 4 | ATAB | Autoantibody | SJOGRENS SS-B ANTIGEN |  | SCREEN | POSITIVE |  | POSITIVE |  |  | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 11 | XYZ | IS | XYZ1234 | 6 | 19283746 | 4 | ATAB | Autoantibody | SJOGRENS SS-B ANTIGEN |  | QUANTIFY | 169 | U/mL | 169 | 169 | U/mL | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |

**Example 11**
This example shows how to represent data from various allergy tests, specifically data from a mixed animal allergens test.
**Row 1:** Shows the detection of immunoglobulin E (IgE) antibody against multiple animal allergens. ISBDAGNT is used to house the generic but controlled value "ANIMAL MIX ANTIGENS, MULTIPLE".
**Rows 2-3:** Show the amount of IgE antibody against dog dander and its RAST classification score.
**Rows 4-5:** Show the amount of IgE antibody against cat dander and its RAST classification score.
**Rows 6-7:** Show the amount of IgE antibody against horse dander and its RAST classification score.
**Rows 8-9:** Show the amount of IgE antibody against cow dander and its RAST classification score.
*is.xpt*

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTDTL | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | IS | XYZ1234 | 1 | 12453333 | ARIGEAB | Allergen-induced IgE Antibody | ANIMAL MIX ANTIGENS, MULTIPLE |  | POSITIVE |  | POSITIVE |  |  | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 2 | XYZ | IS | XYZ1234 | 2 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | DOG DANDER ANTIGEN |  | 0.12 | U/mL | 0.12 | 0.12 | U/mL | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 3 | XYZ | IS | XYZ1234 | 2 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | DOG DANDER ANTIGEN | RAST SCORE | 0 |  | 0 | 0 |  | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 4 | XYZ | IS | XYZ1234 | 3 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | CAT DANDER ANTIGEN |  | 0.19 | U/mL | 0.19 | 0.19 | U/mL | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 5 | XYZ | IS | XYZ1234 | 3 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | CAT DANDER ANTIGEN | RAST SCORE | 0 |  | 0 | 0 |  | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 6 | XYZ | IS | XYZ1234 | 4 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | HORSE DANDER ANTIGEN |  | 44 | U/mL | 44 | 44 | U/mL | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 7 | XYZ | IS | XYZ1234 | 4 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | HORSE DANDER ANTIGEN | RAST SCORE | 4 |  | 4 | 4 |  | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 8 | XYZ | IS | XYZ1234 | 5 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | COW DANDER ANTIGEN |  | 120 | U/mL | 120 | 120 | U/mL | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 9 | XYZ | IS | XYZ1234 | 5 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | COW DANDER ANTIGEN | RAST SCORE | 6 |  | 6 | 6 |  | SERUM | RIA | 1 | SCREENING | 2018-06-20 |

The SUPPIS dataset shows the specific and individual animal allergens within the animal mixed antigens panel test.

*suppis.xpt*

| Row | STUDYID | DOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISMIXCOP | Mixture Component | DOG | CRF |  |
| 2 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISMIXCOP | Mixture Component | CAT | CRF |  |
| 3 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISMIXCOP | Mixture Component | HORSE | CRF |  |
| 4 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISMIXCOP | Mixture Component | COW | CRF |  |

Alternatively, instead of reporting the specific components of a mixed allergen panel, regional allergen mixes may also be reported by the specific regions/areas where they are predominant, as shown in the SUPPIS dataset below.

*suppis.xpt*

| Row | STUDYID | DOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISALGREG | Allergen Mixture Region | CENTRAL CA, AREA 14 | CRF |  |

