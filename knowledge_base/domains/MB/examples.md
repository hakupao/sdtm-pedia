# MB — Examples

*Note: MB and MS share a combined examples section (6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples). MB-specific data tables are shown here; see also MS examples for susceptibility data from the same studies.*

## Example 1

In this example, both a central and a local lab (MBNAM) independently identified Enterococcus faecalis (MBORRES) in a fluid specimen (MBSPEC) taken from the skin (MBLOC) of a subject at visit 1. The method used by both labs was a solid microbial culture (MBMETHOD). Because the culture was not targeted to encourage the growth of a specific organism, MBTESTCD/MBTEST = "MCORGIDN"/"Microbial Organism Identification" and MBORRES represents the name of the organism identified.

After E. faecalis was identified in the subject sample, drug susceptibility testing was performed at each of the labs using both the sponsor's investigational drug and amoxicillin. Because an identified organism is the subject of the test, the NHOID variable is populated with "ENTEROCOCCUS FAECALIS". Between the 2 labs (MSNAM), a total of 3 susceptibility testing methods were used: epsilometer, disk diffusion, and macro broth dilution (MSMETHOD). Epsilometer and disk diffusion both use agar diffusion methods, in which an agar plate is inoculated with the microorganism of interest and either a strip (epsilometer) or discs (disk diffusion) containing various concentrations of the drug are placed on the agar plate. The epsilometer test method provides both a minimum inhibitory concentration (MSTESTCD = "MIC"), the lowest concentration of a drug that inhibits the growth of a microorganism, and a qualitative interpretation (MSTESTCD = "MICROSUS"). The quantitative and qualitative results are grouped together using MSGRPID. The disk diffusion test method provides the diameter of the zone of inhibition (MSTESTCD = "DIAZOINH") and a qualitative interpretation such as susceptible, intermediate, or resistant (MSTESTCD = "MICROSUS"). The third method, macro broth dilution, was used to test the specimen at a predefined drug concentration of each of the drugs. When the drug and amount are a predefined part of the test, the variable MSAGENT is populated with the name of the drug being used in the susceptibility test. The variables MSCONC and MSCONCU represent the concentration and units of the drug being used.

**mb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MBSEQ | MBREFID | MBLNKID | MBTESTCD | MBTEST | MBTSTDTL | MBORRES | MBSTRESC | MBSPEC | MBLOC | MBMETHOD | MBNAM | VISITNUM | VISIT | MBDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|----------|---------|----------|--------|-------|----------|-------|----------|-------|-------|
| 1 | ABC | MB | ABC-001-002 | 1 | SPEC01 | | MCORGIDN | Microbial Organism Identification | DETECTION | PRESENT | PRESENT | FLUID | SKIN | MICROBIAL CULTURE, SOLID | CENTRAL LAB ABC | 1 | VISIT 1 | 2005-06-19T08:00 |
| 2 | ABC | MB | ABC-001-002 | 2 | SPEC01 | | MCORGIDN | Microbial Organism Identification | DETECTION | PRESENT | PRESENT | FLUID | SKIN | MICROBIAL CULTURE, SOLID | LOCAL LAB XYZ | 1 | VISIT 1 | 2005-06-19T08:00 |

Although not expected, the sponsor decided to connect the identification records in MB to the records in MS using the variables MBLNKID and MSLNKGRP.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | MB | | MBLNKID | | ONE | A |
| 2 | ABC | MS | | MSLNKGRP | | MANY | A |

## Example 2

In this example, a sputum sample, collected from the subject at 3 visits over the course of 15 days, was tested for the presence of infectious organisms. The 2 organisms identified were also tested for susceptibility to both penicillin and the sponsor's study drug (MSAGENT). The example shows that the 2 infecting organisms were cleared over the course of the 3 visits.

Specimen collection was represented in the Biospecimen Events (BE) domain.

**be.xpt**

| Row | STUDYID | DOMAIN | USUBJID | BESEQ | BEREFID | BETERM | BEDTC |
|-----|---------|--------|---------|-------|---------|--------|-------|
| 1 | ABC | BE | ABC-01-001 | 1 | SP01 | Collecting | 2005-06-19T08:00 |
| 2 | ABC | BE | ABC-01-001 | 2 | SP02 | Collecting | 2005-06-26T08:00 |
| 3 | ABC | BE | ABC-01-001 | 3 | SP03 | Collecting | 2005-07-01T08:00 |

The SUPPBE table is used to represent 2 non-standard variables of BE.

**Rows 1-3:** Show that all 3 samples (IDVARVAL where IDVAR="BEREFID") were sputum, as indicated by QVAL where QNAM="BESPEC" and QLABEL="Specimen Type".
**Rows 4-6:** Show that all 3 sputum samples were collected via expectoration, as indicated by QVAL where QNAM="Specimen Collection Method". QVAL is populated using the CDISC Controlled Terminology codelist, "Specimen Collection Method".

**suppbe.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|
| 1 | ABC | BE | ABC-01-101 | BEREFID | SP01 | BESPEC | Specimen Type | SPUTUM | CRF |
| 2 | ABC | BE | ABC-01-101 | BEREFID | SP02 | BESPEC | Specimen Type | SPUTUM | CRF |
| 3 | ABC | BE | ABC-01-101 | BEREFID | SP03 | BESPEC | Specimen Type | SPUTUM | CRF |
| 4 | ABC | BE | ABC-01-101 | BEREFID | SP01 | BECLMETH | Specimen Collection Method | EXPECTORATION | CRF |
| 5 | ABC | BE | ABC-01-101 | BEREFID | SP02 | BECLMETH | Specimen Collection Method | EXPECTORATION | CRF |
| 6 | ABC | BE | ABC-01-101 | BEREFID | SP03 | BECLMETH | Specimen Collection Method | EXPECTORATION | CRF |

**Rows 1-2:** Show that a gram stain was used on a subject sputum sample to identify the presence of gram negative cocci (row 1) and to quantify the bacteria (row 2). MBORRES in row 2 represents an ordinal result (MBRSLSCL = "Ord"), such as from a published quantification scale. This value decodes to "FEW" as shown in MBSTRESC. The quantification scale used is represented as Supplemental Qualifiers of MB.
**Rows 3-4:** Show that the same gram-stained sample was used to identify and quantify the presence of gram negative rods.
**Rows 5-6:** Show that microbial culture of the same sample was used at the same visit to identify the presence of two organisms, "STREPTOCOCCUS PNEUMONIAE" and "KLEBSIELLA PNEUMONIAE" (MBORRES).
**Row 7:** Shows that microbial culture of a subsequent sample at a later visit indicated only the presence of "KLEBSIELLA PNEUMONIAE" (MBORRES).
**Row 8:** Shows that microbial culture of a third subject sample at the third visit indicated "NO GROWTH" (MBORRES) of any organisms.

**mb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MBSEQ | MBREFID | MBTESTCD | MBTEST | MBTSTDTL | MBORRES | MBRSLSCL | MBSTRESC | MBSPEC | MBLOC | MBMETHOD | VISITNUM | VISIT | MBDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|---------|----------|----------|--------|-------|----------|----------|-------|-------|
| 1 | ABC | MB | ABC-001-001 | 1 | SP01 | GMNCOC | Gram Negative Cocci | DETECTION | PRESENT | Ord | PRESENT | LUNG | | GRAM STAIN | 1 | VISIT 1 | 2005-06-19T08:00 |
| 2 | ABC | MB | ABC-001-001 | 2 | SP01 | GMNCOC | Gram Negative Cocci | CELL COUNT | 2+ | Ord | FEW | LUNG | | GRAM STAIN | 1 | VISIT 1 | 2005-06-19T08:00 |
| 3 | ABC | MB | ABC-001-001 | 3 | SP01 | GMNROD | Gram Negative Rods | DETECTION | PRESENT | Ord | PRESENT | LUNG | | GRAM STAIN | 1 | VISIT 1 | 2005-06-19T08:00 |
| 4 | ABC | MB | ABC-001-001 | 4 | SP01 | GMNROD | Gram Negative Rods | CELL COUNT | 2+ | Ord | FEW | LUNG | | GRAM STAIN | 1 | VISIT 1 | 2005-06-19T08:00 |
| 5 | ABC | MB | ABC-001-001 | 5 | SP01 | MCORGIDN | Microbial Organism Identification | | STREPTOCOCCUS PNEUMONIAE | Nom | STREPTOCOCCUS PNEUMONIAE | LUNG | | MICROBIAL CULTURE, SOLID | 1 | VISIT 1 | 2005-06-19T08:00 |
| 6 | ABC | MB | ABC-001-001 | 6 | SP01 | MCORGIDN | Microbial Organism Identification | | KLEBSIELLA PNEUMONIAE | Nom | KLEBSIELLA PNEUMONIAE | LUNG | | MICROBIAL CULTURE, SOLID | 1 | VISIT 1 | 2005-06-19T08:00 |
| 7 | ABC | MB | ABC-001-001 | 7 | SP02 | MCORGIDN | Microbial Organism Identification | | KLEBSIELLA PNEUMONIAE | Nom | KLEBSIELLA PNEUMONIAE | LUNG | | MICROBIAL CULTURE, SOLID | 2 | VISIT 2 | 2005-06-26T08:00 |
| 8 | ABC | MB | ABC-001-001 | 8 | SP03 | MCORGIDN | Microbial Organism Identification | | NO GROWTH | Nom | NO GROWTH | LUNG | | MICROBIAL CULTURE, SOLID | 3 | VISIT 3 | 2005-07-06T08:00 |

**suppmb.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|
| 1 | ABC | MB | ABC-01-101 | MBSEQ | 2 | MBQSCAL | Quantification Scale | CDC semi-quantitative score for gram staining | CRF |

## Example 3

This example shows the microorganisms detected from a gastric aspirate specimen from a child with suspected tuberculosis (TB). In this example, gastric lavage is only performed once. Three records in the MB domain store detection records for 2 levels of detection: acid-fast bacilli, and Mycobacterium tuberculosis (Mtb). Characteristics from a culture on solid media that support the presumptive detection of Mtb are also represented in MB. The susceptibility results from both the nucleic acid amplification test (NAAT) and the solid culture are represented in the MS domain.

Specimen processing events included sample collection, preparation, and culturing; these events are represented in the BE domain. For TB studies, each sample needs a separate identifier to link it to further actions or characteristics of the sample. Therefore, each aliquot is assigned a unique BEREFID value that can be traced to the BEREFID value assigned to the collected "parent" sample. BEREFID is also used to connect the BE and Biospecimen Findings (BS) domains (via BSREFID), as well as any results obtained from the sample that are in the MB or MS domains (via MBREFID and MSREFID). If the same sample is used in many domains, the use of --REFID may result in a potentially undesirable many-to-many merge; users may need to make use of additional linking variables such as --LNKID and --LNKGRP. Information about the BE and BS domains including the specification tables, assumptions, and examples can be found in Sections 6.2.2 and 6.3.5.2 of this document.

In the BE, BS, MB, and MS domains, --DTC represents the date of sample collection. --LNKID and --LNKGRP are used to link culture start and stop dates (BE) with culture results in MB and MS. MBGRPID is used to connect the detection record in MB with the corresponding culture characteristics shown in rows 5-7.

**Row 1:** Shows the event of specimen collection. This is the genesis of the sample identified by BEREFID="100"; therefore, BEDTC and BESTDTC are the same. The specimen collection setting, collection method, and specimen type are represented using supplemental qualifiers. Even though the variable Specimen Type is available for use in Findings domains, it is not available for use in Events domains and thus it is represented as supplemental qualifier.

**Rows 2-6:** Show that the sample was aliquoted (i.e., smaller subsamples were portioned out from the parent sample) and each separate aliquot assigned a unique BEREFID. In such cases, BEREFID is an incremented decimal value with the original sample's BEREFID (when BECAT="COLLECTION") as the base number. (This is not an explicit requirement, but makes tracking the samples easier.) The definitive link between parent-child samples is defined by the PARENT variable shown in the RELSPEC dataset.

**Rows 7-9:** Show that 3 of the aliquots (100.3, 100.4, and 100.5) were cultured for detection (row 7) and tested for drug susceptibility (rows 8 and 9). The inoculation and read dates of a culture should be represented in BESTDTC and BEENDTC, respectively. These dates can be linked to the culture results in MB and MS using BELNKID, MBLNKGRP, and MSLNKID.

**Row 10:** Shows that sample 100.1 was concentrated.

**be.xpt**

| Row | STUDYID | DOMAIN | USUBJID | BESEQ | BEREFID | BELNKID | BETERM | BECAT | BEDTC | BESTDTC | BEENDTC |
|-----|---------|--------|---------|-------|---------|---------|--------|-------|-------|---------|---------|
| 1 | ABC | BE | ABC-01-101 | 1 | 100 | | Collecting | COLLECTION | 2011-01-17T06:00 | 2011-01-17T05:00 | |
| 2 | ABC | BE | ABC-01-101 | 2 | 100.1 | | Aliquoting | PREPARATION | 2011-01-17T06:00 | 2011-01-17T09:00 | |
| 3 | ABC | BE | ABC-01-101 | 3 | 100.2 | | Aliquoting | PREPARATION | 2011-01-17T06:00 | 2011-01-17T09:00 | |
| 4 | ABC | BE | ABC-01-101 | 4 | 100.3 | | Aliquoting | PREPARATION | 2011-01-17T06:00 | 2011-01-17T09:00 | |
| 5 | ABC | BE | ABC-01-101 | 5 | 100.4 | | Aliquoting | PREPARATION | 2011-01-17T06:00 | 2011-01-17T09:00 | |
| 6 | ABC | BE | ABC-01-101 | 6 | 100.5 | | Aliquoting | PREPARATION | 2011-01-17T06:00 | 2011-01-17T09:00 | |
| 7 | ABC | BE | ABC-01-101 | 7 | 100.3 | 1 | Culturing | CULTURE | 2011-01-17T06:00 | 2011-01-17T09:30 | 2011-02-02T09:00 |
| 8 | ABC | BE | ABC-01-101 | 8 | 100.4 | 2 | Culturing | CULTURE | 2011-01-17T06:00 | 2011-02-21T10:00 | 2011-02-21T09:00 |
| 9 | ABC | BE | ABC-01-101 | 9 | 100.5 | 3 | Culturing | CULTURE | 2011-01-17T06:00 | 2011-02-02T10:00 | 2011-02-22T09:00 |
| 10 | ABC | BE | ABC-01-101 | 10 | 100.1 | | Concentrating | PREPARATION | 2011-01-17T06:00 | 2011-01-17T09:15 | |

The RELSPEC table shows the relationship of the parent sample to its aliquots. The LEVEL variable indicates that the sample has been subsampled. The original parent sample is always LEVEL="1". An aliquot of the sample would be LEVEL="2". If the aliquot was further split, that subsample would be LEVEL="3".

**relspec.xpt**

| Row | STUDYID | USUBJID | REFID | SPEC | PARENT | LEVEL |
|-----|---------|---------|-------|------|--------|-------|
| 1 | ABC | ABC-01-101 | 100 | LAVAGE FLUID | | 1 |
| 2 | ABC | ABC-01-101 | 100.1 | LAVAGE FLUID | 100 | 2 |
| 3 | ABC | ABC-01-101 | 100.2 | LAVAGE FLUID | 100 | 2 |
| 4 | ABC | ABC-01-101 | 100.3 | LAVAGE FLUID | 100 | 2 |
| 5 | ABC | ABC-01-101 | 100.4 | LAVAGE FLUID | 100 | 2 |
| 6 | ABC | ABC-01-101 | 100.5 | LAVAGE FLUID | 100 | 2 |

Findings data captured about the specimen during collection, preparation, and handling are represented in the BS domain.

**Row 1:** Shows the total volume of lavage fluid collected during the gastric lavage by using the same values for BSREFID and BEREFID. This is the parent (collected) sample from which further aliquots were generated.
**Rows 2-6:** Show the volume of each aliquot created.

**bs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | BSSEQ | BSREFID | BSTESTCD | BSTEST | BSORRES | BSORRESU | BSSTRESC | BSSTRESN | BSSTRESU | BSSPEC | BSLOC | BSDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|---------|----------|----------|----------|----------|--------|-------|-------|
| 1 | ABC | BS | ABC-01-101 | 1 | 100 | VOLUME | Volume | 20 | mL | 20 | 20 | mL | LAVAGE FLUID | STOMACH | 2011-01-17T06:00 |
| 2 | ABC | BS | ABC-01-101 | 2 | 100.1 | VOLUME | Volume | 4 | mL | 4 | 4 | mL | LAVAGE FLUID | STOMACH | 2011-01-17T06:00 |
| 3 | ABC | BS | ABC-01-101 | 3 | 100.2 | VOLUME | Volume | 4 | mL | 4 | 4 | mL | LAVAGE FLUID | STOMACH | 2011-01-17T06:00 |
| 4 | ABC | BS | ABC-01-101 | 4 | 100.3 | VOLUME | Volume | 4 | mL | 4 | 4 | mL | LAVAGE FLUID | STOMACH | 2011-01-17T06:00 |
| 5 | ABC | BS | ABC-01-101 | 5 | 100.4 | VOLUME | Volume | 4 | mL | 4 | 4 | mL | LAVAGE FLUID | STOMACH | 2011-01-17T06:00 |
| 6 | ABC | BS | ABC-01-101 | 6 | 100.5 | VOLUME | Volume | 4 | mL | 4 | 4 | mL | LAVAGE FLUID | STOMACH | 2011-01-17T06:00 |

Results from detection tests performed on samples are represented in the MB domain. The sputum sample was aliquoted 5 times. Three of these aliquots underwent detection testing using 3 separate tests: 1 for acid-fast bacillus (AFB), 1 for M. tuberculosis complex, and 1 for M. tuberculosis. MBTESTCD/MBTEST represents the organism being investigated, MBMETHOD represents the testing method, and MBREFID represents which aliquot was tested. The variable MBTSTDTL is used to provide further description of the test performed in producing the MB result. In addition to detection, MBTSTDTL can be used to represent specific attributes (e.g., quantifiable and semi-quantifiable results of the culture) as well as qualitative details about the culture (e.g., colony color, morphology).

**Row 1:** Shows a test targeting the presence or absence of AFB using a stain. The MBSPCND shows that the sample used in the test was concentrated. MBGRPID can be used to connect the detection record with the corresponding AFB quantification results shown in row 2.
**Row 2:** Shows a categorical result for an AFB test using a stain. MBORRES contains a result based on a CDC AFB quantification scale. The name of the scale used is represented as a supplemental qualifier. MBREFID indicates which aliquot the procedure was performed upon and MBGRPID is used to connect the AFB quantification record to the detection record in row 1.
**Row 3:** Shows a test targeting the presence or absence of M. tuberculosis complex using a genotyping method. Details about the assay can be found in the Device Identifiers (DI) domain. The value in SPDEVID links the genotype result to the assay information in the DI domain. The microbial detection certainty is represented as a supplemental qualifier. Because genotyping was used, the detection is considered to be definitive.
**Row 4:** Shows a test targeting the presence or absence of M. tuberculosis performed on a solid culture. The medium type and microbial detection certainty are represented as supplemental qualifier. Because genotyping was not used, the detection is considered to be presumptive. The culture start and stop dates are represented in BE and are connected to the culture results via BELNKID and MBLNKGRP. MBGRPID is used to connect the detection record in MB with the corresponding culture characteristics shown in rows 5-7.
**Row 5:** Shows a colony-forming unit (CFU) count from a solid culture. The MBORRES value represents the actual colony count from this plate. However, the sample that was spread on this plate represented a 100-fold dilution from the original subject sample. This information is represented in the Dilution Factor supplemental qualifier (MBDILFCT), whose value = 10^-2 (1/100th). In order to enable more straightforward pooling of CFU data, a simple integer result (14700) is used in MBSTRESC/N, and MBSTRESU="CFU/mL". The medium type for the solid culture is also represented as a supplemental qualifier.
**Row 6:** Shows the standardized colony count category based on a CDC M. tuberculosis colony quantification scale. The quantification scale used and the medium type for the solid culture are represented as supplemental qualifiers.

**mb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | MBSEQ | MBGRPID | MBREFID | MBLNKGRP | MBTESTCD | MBTEST | MBTSTDTL | MBORRES | MBRSLSCL | MBSTRESC | MBSTRESN | MBSTRESU | MBSPCND | MBSPEC | MBLOC | MBMETHOD | VISITNUM | VISIT | MBDTC |
|-----|---------|--------|---------|---------|-------|---------|---------|----------|----------|--------|----------|---------|----------|----------|----------|----------|---------|--------|-------|----------|----------|-------|-------|
| 1 | ABC | MB | ABC-01-101 | | 1 | 1 | 100.1 | | AFB | Acid-Fast Bacilli | DETECTION | PRESENT | Ord | PRESENT | | | CONCENTRATED | LAVAGE FLUID | STOMACH | ZIEHL-NEELSEN ACID FAST STAIN | 1 | WEEK 1 | 2011-01-17T06:00 |
| 2 | ABC | MB | ABC-01-101 | | 2 | 1 | 100.1 | | AFB | Acid-Fast Bacilli | CELL COUNT | 3+ | Ord | 3+ | | | CONCENTRATED | LAVAGE FLUID | STOMACH | ZIEHL-NEELSEN ACID FAST STAIN | 1 | WEEK 1 | 2011-01-17T06:00 |
| 3 | ABC | MB | ABC-01-101 | ABC765 | 3 | | 100.2 | | MTBCMPLX | Mycobacterium Tuberculosis Complex | DETECTION | PRESENT | Ord | PRESENT | | | | LAVAGE FLUID | STOMACH | NUCLEIC ACID AMPLIFICATION TEST | 1 | WEEK 1 | 2011-01-17T06:00 |
| 4 | ABC | MB | ABC-01-101 | | 4 | 2 | 100.3 | 1 | MTB | Mycobacterium Tuberculosis | DETECTION | PRESENT | Ord | PRESENT | | | | LAVAGE FLUID | STOMACH | MICROBIAL CULTURE, SOLID | 1 | WEEK 1 | 2011-01-17T06:00 |
| 5 | ABC | MB | ABC-01-101 | | 5 | 2 | 100.3 | 1 | MTB | Mycobacterium Tuberculosis | COLONY COUNT | 147 | | CFU | 14700 | CFU/mL | | LAVAGE FLUID | STOMACH | MICROBIAL CULTURE, SOLID | 1 | WEEK 1 | 2011-01-17T06:00 |
| 6 | ABC | MB | ABC-01-101 | | 6 | 2 | 100.3 | 1 | MTB | Mycobacterium Tuberculosis | COLONY COUNT | 2+ | Ord | 2+ | | | | LAVAGE FLUID | STOMACH | MICROBIAL CULTURE, SOLID | 1 | WEEK 1 | 2011-01-17T06:00 |

**suppmb.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|
| 1 | ABC | MB | ABC-01-101 | MBSEQ | 2 | MBQSCAL | Quantification Scale | Smear Quantitation: Centers for Disease Control Method for Carbol Fuchsin Staining (1000X) | Collected |
| 2 | ABC | MB | ABC-01-101 | MBSEQ | 3 | MBMICERT | Microbial Identification Certainty | DEFINITIVE | Collected |
| 3 | ABC | MB | ABC-01-101 | MBSEQ | 4 | MBMICERT | Microbial Identification Certainty | PRESUMPTIVE | Collected |
| 4 | ABC | MB | ABC-01-101 | MBREFID | 100.3 | MBMEDTYP | Medium Type | MIDDLEBROOK 7H10 AGAR | Collected |
| 5 | ABC | MB | ABC-01-101 | MBSEQ | 5 | MBDILFCT | Dilution Factor | 10^-2 | Collected |
| 6 | ABC | MB | ABC-01-101 | MBSEQ | 6 | MBQSCAL | Quantification Scale | Solid Media Result: Centers for Disease Control (CDC) Quantification Scale | Collected |
