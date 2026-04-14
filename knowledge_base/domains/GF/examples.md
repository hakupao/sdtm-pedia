# GF — Examples

## Example 1

This example shows findings from an assessment of single nucleotide and copy number variation generated from biocomputational analysis with wet laboratory methodology targeted genome sequencing. Findings from this assessment show variation from DNA extracted from an individual's tumor tissue. As the DNA specimen was extracted from tumor tissue, the inheritability of the variation is considered to be somatic.

**Row 1:** Shows the predicted amino acid change due to the single nucleotide variant.

**Row 2:** Shows the predicted coding sequence change due to the single nucleotide variant.

**Row 3:** Shows the classification of the variant impact given the predicted amino acid change.

**Row 4:** Shows the number of times the locus specified in variables GFCHROM and GFGENLOC was observed.

**Row 5:** Shows the percent variant read depth to total read depth.

**Row 6:** Shows the number of copies of the gene of interest within the genome of the tumor cell.

**Row 7:** Shows the number of altered exons within the gene of interest in the genome of the tumor cell.

**Row 8:** Shows the ratio of the copy number of the gene of interest in the tumor cell to the reference number of copies.

**Row 9:** Shows the interpretation of the copy number of the gene of interest within the genome of the tumor cell.

**gf.xpt**

| Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFREFID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFSTRESC | GFSTREFN | GFSTRESU | GFINHERTG | GFGENREF | GFCHROM | GFSYM | GFSYMTYP | GFGENLOC | GFGENSR | GFSEQID | GFPVRID | GFCOPYID | GFNAM | GFSPEC | GFMETHOD | GFRUNID | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|---------|----------|----------|----------|-----------|----------|---------|-------|----------|----------|---------|---------|---------|----------|-------|--------|----------|---------|----------|-------|---------|-------|------|
| 1 | ABC-123 | GF | 123101 | 1 | | SNV | Single Nucleotide Variation | PREDICTED AMINO ACID CHANGE | p.Val600Glu | | | | SOMATIC | | 7 | BRAF | Gene with Protein Product | Exon 15 | | ENSG00000157764 | rs121913227 | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 2 | ABC-123 | GF | 123101 | 2 | | SNV | Single Nucleotide Variation | PREDICTED CODING SEQUENCE CHANGE | c.1799T>A | | | | SOMATIC | GRCh38.p13 | 7 | BRAF | Gene with Protein Product | 140753336 | Exon 15 | ENSG00000157764 | rs121913227 | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 3 | ABC-123 | GF | 123101 | 3 | | SNV | Single Nucleotide Variation | VARIANT CLASSIFICATION | Pathogenic | | | | SOMATIC | | 7 | BRAF | Gene with Protein Product | Exon 15 | | ENSG00000157764 | rs121913227 | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 4 | ABC-123 | GF | 123101 | 4 | | SNV | Single Nucleotide Variation | LOCUS COUNT | | | 200 | | SOMATIC | GRCh38.p13 | 7 | BRAF | Gene with Protein Product | 140753336 | Exon 15 | ENSG00000157764 | rs121913227 | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 5 | ABC-123 | GF | 123101 | 5 | | SNV | Single Nucleotide Variation | PERCENT VARIANT READ DEPTH | | | 50 | % | SOMATIC | GRCh38.p13 | 7 | BRAF | Gene with Protein Product | 140753336 | Exon 15 | ENSG00000157764 | rs121913227 | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 6 | ABC-123 | GF | 123101 | 6 | | CNV | Copy Number Variation | COPY NUMBER | | | 5 | | SOMATIC | | 7 | BRAF | Gene with Protein Product | | | ENSG00000157764 | | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 7 | ABC-123 | GF | 123101 | 7 | | CNV | Copy Number Variation | EXON COPY NUMBER ALTERATION | | | 3 | | SOMATIC | | 7 | BRAF | Gene with Protein Product | | | ENSG00000157764 | | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 8 | ABC-123 | GF | 123101 | 8 | | CNV | Copy Number Variation | COPY NUMBER RATIO | | | 2.5 | | SOMATIC | | 7 | BRAF | Gene with Protein Product | | | ENSG00000157764 | | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 9 | ABC-123 | GF | 123101 | 9 | | CNV | Copy Number Variation | INTERPRETATION | AMPLIFICATION | | | | SOMATIC | | 7 | BRAF | Gene with Protein Product | | | ENSG00000157764 | | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |

Identifying information for the gene panel used to generate the result is in the DI domain. The gene panel is represented in SDTM, as the panel used as part of the wet laboratory methodology may change and affects interpretation of the result. The platform in which the gene panel was used is not represented, because it does not provide additional context for the result.

**di.xpt**

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
|-----|---------|--------|---------|-------|----------|--------|-------|
| 1 | ABC-123 | DI | ACME GenePanel 500 | 1 | DEVTYPE | Device Type | Gene Panel |
| 2 | ABC-123 | DI | ACME GenePanel 500 | 2 | MANUF | Manufacturer | ACME |

## Example 2

This example shows findings from an assessment of a known single nucleotide variant in gene ABCG2 using wet laboratory methodology real-time polymerase chain reaction. Findings from this assessment show the genotypes from DNA extracted from the blood of 3 individuals, each with a different genotype at the genetic locus of interest. Because the DNA specimen was extracted from normal blood, the inheritability of the variation is considered to be in the germline.

**Row 1:** Shows a subject genotype which is homozygous for the variant nucleotide in the reference sequence.

**Row 2:** Shows a subject genotype which is heterozygous for the nucleotide in the reference sequence.

**Row 3:** Shows a subject genotype which is homozygous for the nucleotide in the reference sequence.

**gf.xpt**

| Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFREFID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFSTRESC | GFSTREFN | GFINHERTG | GFGENREF | GFCHROM | GFSYM | GFGENLOC | GFGENSR | GFSEQID | GFPVRID | GFNAM | GFSPEC | GFMETHOD | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|---------|----------|----------|-----------|----------|---------|-------|----------|---------|---------|---------|-------|--------|----------|----------|-------|---------|-------|------|
| 1 | C12345 | GF | C12345-001 | 1 | NA01001 | SNV | Single Nucleotide Variation | GENOTYPE | G/G | G/G | | GERMLINE | GRCh38.p13 | 4 | ABCG2 | | 4.88131177 | ENSG00000118777 | rs2231142 | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | 1 | SCREENING | -1 | | -25 |
| 2 | C12345 | GF | C12345-002 | 1 | NA01001 | SNV | Single Nucleotide Variation | GENOTYPE | G/G | G/G | | GERMLINE | | | ABCG2 | | 4.88131177 | ENSG00000118777 | rs2231142 | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | 1 | SCREENING | -1 | | -25 |
| 3 | C12345 | GF | C12345-003 | 1 | NA01001 | SNV | Single Nucleotide Variation | GENOTYPE | G/G | G/G | | GERMLINE | GRCh38.p13 | 4 | ABCG2 | GENE WITH PROTEIN PRODUCT | 4.88131177 | ENSG00000118777 | rs2231142 | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | 1 | SCREENING | -1 | 2020-06-3 | -3 |

## Example 3

This example shows transcription levels of genes ACTB and GAPDH and summarized scores from the transcription levels. Transcription levels and scores were determined using biocomputational analysis with wet laboratory methodology targeted transcriptome sequencing. Specific formulas used in biocomputational analyses to generate normalized and summarized score results are respresented when applicable.

**Rows 1, 7:** Show the number of fragments counted corresponding to the indicated gene.

**Rows 2-4, 8-10:** Show normalized transcription levels based on the normalization methods noted in variable GFANMETH and the raw fragment count reported in rows 1 and 7.

**Rows 5, 11:** Show the percentile rank of the indicated gene among those genes reported in the indicated panel.

**Rows 6, 12:** Show the predicted expression status of the indicated gene based on a threshold established by the assay.

**Rows 13-14:** Show normalized transcription levels based on the normalization methods noted in variable GFANMETH and the raw fragment count reported in rows 1 and 7.

**Rows 15-16:** Show gene signature scores from summarization of genetic data based on the methods noted in variable GFANMETH.

**gf.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | GFSEQ | GFGRPID | GFREFID | GFSPID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFORRESU | GFSTRESC | GFSTRESN | GFSTRESU | GFGENREF | GFCHROM | GFSYM | GFSYMTYP | GFSEQID | GFXFN | GFNAM | GFSPEC | GFMETHOD | GFANMETH | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
|-----|---------|--------|---------|---------|-------|---------|---------|--------|----------|--------|----------|---------|----------|----------|----------|----------|----------|---------|-------|----------|---------|-------|-------|--------|----------|----------|----------|-------|---------|-------|------|
| 1 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 1 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | FRAGMENT COUNT | 36 | | 36 | 36 | | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 2 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 2 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 0.5679 | /MBP | 0.5679 | 0.5679 | /MBP | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | FRAGMENTS PER KILOBASE MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 3 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 3 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 1.0523 | /10^6 | 1.0523 | 1.0523 | /10^6 | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | COUNTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 4 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 4 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 1.9935 | /MBP | 1.9935 | 1.9935 | /MBP | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | TRANSCRIPTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 5 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 5 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | PERCENTILE RANK | 0.37 | % | 0.37 | 0.37 | % | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 6 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 6 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | GENETIC TRANSCRIPTION INDICATOR | no | | no | | | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 7 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 7 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | FRAGMENT COUNT | 23658 | | 23658 | 23658 | | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 8 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 8 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 148.6268 | /MBP | 148.6268 | 148.6268 | /MBP | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | FRAGMENTS PER KILOBASE MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 9 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 9 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 691.5607 | /10^6 | 691.5607 | 691.5607 | /10^6 | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | COUNTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 10 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 10 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 521.716 | /MBP | 521.716 | 521.716 | /MBP | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | TRANSCRIPTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 11 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 11 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | PERCENTILE RANK | 0.99 | % | 0.99 | 0.99 | % | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 12 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 12 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | GENETIC TRANSCRIPTION INDICATOR | yes | | yes | | | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 13 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 13 | 1 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | -0.056299177 | | -0.056299177 | -0.056299177 | | GRCh38.p12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 14 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 14 | 1 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | -0.046787999 | | -0.046787999 | -0.046787999 | | GRCh38.p12 | | GAPDH | GENE WITH PROTEIN PRODUCT | NM_001256799.3 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 15 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 15 | 2 | ABC1234567 | AP483910 | GENESIG | Gene Signature | GENETIC TRANSCRIPTION INTERPRETATION | LOW | | LOW | | | GRCh38.p12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | IFN-1 GENE SIGNATURE | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 16 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 16 | 3 | ABC1234567 | AP483910 | GENESIG | Gene Signature | SCORE | -1.126819661 | | -1.126819661 | -1.126819661 | | GRCh38.p12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | IFN-1 GENE SIGNATURE | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |

Identifying information for the gene panel used to generate the result is in the DI domain. The gene panel is represented in SDTM, as the panel used as part of the wet laboratory methodology may change and affects interpretation of the result. The platform in which the gene panel was used is not represented, because it does not provide additional context for the result.

The DI example shows the device type and manufacturer for the device identified as ACME GenePanel 250.

**di.xpt**

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
|-----|---------|--------|---------|-------|----------|--------|-------|
| 1 | ABC-123 | DI | ACME GenePanel 250 | 1 | DEVTYPE | Device Type | Gene Panel |
| 2 | ABC-123 | DI | ACME GenePanel 250 | 2 | MANUF | Manufacturer | ACME |

## Example 4

This example shows findings from an assessment of microsatellite instability for genetic subregions that are known to be unstable. DNA extracted from tumor tissue is amplified and the resulting amplicons are resolved using wet laboratory methodology capillary electrophoresis.

**Row 1:** Shows the summarized interpretation of overall microsatellite instability.

**Rows 2-6:** Show whether microsatellite instability is detected in the genetic subregions indicated.

**gf.xpt**

| Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFREFID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFSTRESC | GFXFN | GFNAM | GFSPEC | GFMETHOD | GFRUNID | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|---------|----------|-------|-------|--------|----------|---------|----------|-------|---------|-------|------|
| 1 | ABC123 | GF | 123101 | 1 | 4401470-2-6 | MICRISTB | Microsatellite Instability | MSI-Stable | MSI-Stable | | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MS-D10418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 2 | ABC123 | GF | 123101 | 2 | 4401470-2-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | BAT-25 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MS-D10418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 3 | ABC123 | GF | 123101 | 3 | 4401470-2-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | BAT-26 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MS-D10418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 4 | ABC123 | GF | 123101 | 4 | 4401470-2-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | MONO-27 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MS-D10418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 5 | ABC123 | GF | 123101 | 5 | 4401470-2-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | NR-21 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MS-D10418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 6 | ABC123 | GF | 123101 | 6 | 4401470-2-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | NR-24 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MS-D10418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |

## Example 5

This example includes 3 datasets (i.e., MB and MS in addition to GF). The purpose of this 3-part example is to illustrate how these domains are appropriately used in cases where the concepts in each domain are very closely related. Specifically, the example demonstrates the use of these domains by following a subject through a hypothetical scenario of influenza diagnosis, genetic evaluation of the virus, and interpretation of drug susceptibility resulting from genetic testing.

Tests that diagnose or identify the presence of an infectious agent in a subject sample are represented in the MB domain, regardless of the methodology used. In this example, the subject was diagnosed with influenza A H3N2 via a nucleic acid amplification test (NAAT) at the baseline visit. MBTEST = "Microbial Organism Identification" because the assay does not specifically test for the presence of 1 organism or subtype to the exclusion of all others.

**mb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MBSEQ | MBREFID | MBTESTCD | MBTEST | MBORRES | MBSTRESC | MBSPEC | MBLOC | MBMETHOD | VISITNUM | VISIT | MBDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|---------|----------|--------|-------|----------|----------|-------|-------|
| 1 | INFLU122 | MB | INF01-01 | 1 | INFLU0101.1 | MCORGIDN | Microbial Organism Identification | INFLUENZA A VIRUS SUBTYPE | INFLUENZA A VIRUS SUBTYPE H3N2 | MUCUS | NOSTRIL | NUCLEIC ACID AMPLIFICATION TEST | 1 | BASELINE | 2020-06-11 |

Next, a series of virus samples extracted from the subject underwent targeted single nucleotide polymorphism (SNP) testing to determine the feasibility of using the neuraminidase inhibitor oseltamivir to treat the infection (i.e., drug susceptibility testing). Findings from this testing provide both genetic data in the form of the genotype identified and the susceptibility/resistance data as inferred phenotype. Genotypic findings are represented in the GF domain, and inferred susceptibility/resistance in MS.

GFLNKID serves as the link between this dataset and the MS dataset which follows.

**Row 1:** Shows the result of a targeted test to detect a single nucleotide polymorphism in the influenza neuraminidase gene known to confer resistance to the drug oseltamivir. The result (R292R) indicates that the amino acid residue R (arginine) at position 292 remains unchanged at the baseline visit.

**Rows 2-3:** Show the results of the same targeted test at the day 2 and day 5 visits. The results (R292K) show that a mutation has occurred at position 292 from the amino acid R (arginine) to the amino acid K (lysine).

**gf.xpt**

| Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFREFID | NHOID | GFLNKID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFSTRESC | GFSYM | GFGENLOC | GFSEQID | GFSPEC | GFMETHOD | VISITNUM | VISIT | GFDTC |
|-----|---------|--------|---------|-------|---------|-------|---------|----------|--------|----------|---------|----------|-------|----------|---------|--------|----------|----------|-------|-------|
| 1 | INFLU122 | GF | INF01-01 | 1 | INFLU0101.1 | INFLUENZA A H3N2 | GF-MS-01 | SNV | Single Nucleotide Variation | PREDICTED AMINO ACID CHANGE | R292R | R292R | NA | 292 | U43427 | RNA | | 1 | BASELINE | 2020-06-11 |
| 2 | INFLU122 | GF | INF01-01 | 2 | INFLU0102 | INFLUENZA A H3N2 | GF-MS-02 | SNV | Single Nucleotide Variation | PREDICTED AMINO ACID CHANGE | R292K | R292K | NA | 292 | U43427 | RNA | | 2 | DAY 2 | 2020-06-12 |
| 3 | INFLU122 | GF | INF01-01 | 3 | INFLU0103 | INFLUENZA A H3N2 | GF-MS-03 | SNV | Single Nucleotide Variation | PREDICTED AMINO ACID CHANGE | R292K | R292K | NA | 292 | U43427 | RNA | | 3 | DAY 5 | 2020-06-15 |

The susceptibility data stemming from this genetic testing above are represented in MS (see Section 6.3.5.7.2, Microbiology Susceptibility, assumption 1b). GFLINKID matches MSLNKID to connect the records in GF with the corresponding conclusion regarding susceptibility in MS. As above, NHOID is used to indicate that influenza A H3N2 is the focus of these records. MSAGENT represents the drug to which the results of susceptible or resistant pertain.

**Row 1:** Shows the influenza extracted from the subject at the baseline visit is susceptible to oseltamivir.

**Rows 2-3:** Show the influenza extracted from the subject at the day 2 and day 5 visits is resistant to oseltamivir.

**ms.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MSSEQ | MSREFID | NHOID | MSLNKID | MSTESTCD | MSTEST | MSAGENT | MSORRES | MSSTRESC | MSMETHOD | VISITNUM | VISIT | MSDTC |
|-----|---------|--------|---------|-------|---------|-------|---------|----------|--------|---------|---------|----------|----------|----------|-------|-------|
| 1 | INFLU122 | MS | INF01-01 | 1 | INFLU0101.1 | INFLUENZA A H3N2 | GF-MS-01 | MICROSUS | Microbial Susceptibility | OSELTAMIVIR | SUSCEPTIBLE | SUSCEPTIBLE | | 1 | BASELINE | 2020-06-11 |
| 2 | INFLU122 | MS | INF01-01 | 2 | INFLU0102 | INFLUENZA A H3N2 | GF-MS-02 | MICROSUS | Microbial Susceptibility | OSELTAMIVIR | RESISTANT | RESISTANT | | 2 | DAY 2 | 2020-06-12 |
| 3 | INFLU122 | MS | INF01-01 | 3 | INFLU0103 | INFLUENZA A H3N2 | GF-MS-03 | MICROSUS | Microbial Susceptibility | OSELTAMIVIR | RESISTANT | RESISTANT | | 3 | DAY 5 | 2020-06-15 |

The relrec dataset example shows the relationship between the genetic assessment in GF and the resistance/susceptibility data in MS.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | PS001 | GF | | GFLNKID | | ONE | 1 |
| 2 | PS001 | MS | | MSLNKID | | ONE | 1 |
