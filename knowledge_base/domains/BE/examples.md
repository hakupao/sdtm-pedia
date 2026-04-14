# BE — Examples

## Example 1

In this example, a specimen is collected, flash frozen, thawed, and shipped to another location.

Some tests are very sensitive to specimen handling processes such as flash freezing or time spent in transit. Therefore, it is important to record when the processes were started and completed. Such information is recorded in the BE domain.

**Row 1:** Shows specimen collection. The value in SPDEVID for this row identifies the vessel into which the specimen is collected.

**Rows 2-4:** Show the start and end date/times of flash freezing, storing while frozen, and thawing. The value in SPDEVID for row 3 identifies the freezer in which the specimen is stored.

**Row 5:** Records the transportation of a biospecimen. Because there is only one ABC Lab, BEPRTYID is null. The value in SPDEVID for this row identifies the shipping container.

**be.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | BESEQ | BEREFID | BETERM | BEDECOD | BEPARTY | BEPRTYID | BECAT | BELOC | VISITNUM | VISIT | BEDTC | BESTDTC | BEENDTC |
|-----|---------|--------|---------|---------|-------|---------|--------|---------|---------|----------|-------|-------|----------|-------|-------|---------|---------|
| 1 | ABC134 | BE | 43871 | TS409871 | 1 | 1148.267 | Collecting | COLLECTING | SITE | 01 | COLLECTION | BRAIN | 1 | BASELINE | 2005-03-20 | 2005-03-20T15:07 | |
| 2 | ABC134 | BE | 43871 | | 2 | 1148.267 | Flash Freezing | FLASH FREEZING | SITE | 01 | PREPARATION | | 1 | BASELINE | 2005-03-20 | 2005-03-20T15:07 | 2005-03-20T15:09 |
| 3 | ABC134 | BE | 43871 | 309827 | 3 | 1148.267 | Storing | STORING | SITE | 01 | STORING | | 1 | BASELINE | 2005-03-20 | 2005-03-20T15:09 | 2005-03-21T10:29 |
| 4 | ABC134 | BE | 43871 | | 4 | 1148.267 | Thawing | THAWING | SITE | 01 | PREPARATION | | 1 | BASELINE | 2005-03-20 | 2005-03-21T10:29 | 2005-03-21T10:36 |
| 5 | ABC134 | BE | 43871 | LN43871 | 5 | 1148.267 | Shipping | SHIPPING | ABC LAB | | TRANSPORT | | 1 | BASELINE | 2005-03-20 | 2005-03-21T11:00 | 2005-03-21T15:00 |

**suppbe.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC134 | BE | 43871 | BEREFID | 1148.267 | BESPEC | Specimen Type | TISSUE | CRF | |

Findings related to specimen handling processes are stored in the Biospecimen (BS) domain. These processes can be important to maintain the integrity of the specimens used in genetic variation and gene expression testing. Depending on how a study is designed, there might be very specific specimen handling specifications contained in the protocol for all labs to follow. Other protocols may let the labs determine the processes to follow. This example illustrates the latter approach.

**Row 1:** Shows the volume of the biospecimen.

**Rows 2-3:** Show the flash freeze temperature and material, associated via RELREC with BE row 2.

**bs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | BSSEQ | BSGRPID | BSREFID | BSTESTCD | BSTEST | BSCAT | BSORRES | BSORRESU | BSSTRESC | BSSTRESN | BSSTRESU | BSSPEC | BSANTREG | VISITNUM | BSDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|----------|-------|
| 1 | ABC134 | BS | 43871 | 1 | | 1148.267 | VOLUME | Volume | SPECIMEN MEASUREMENT | 2 | cm3 | 2 | | cm3 | BRAIN | CEREBRAL AQUEDUCT | 1 | 2005-03-20 |
| 2 | ABC134 | BS | 43871 | 2 | 267FF | 1148.267 | TEMP | Temperature | SPECIMEN HANDLING | -80 | C | -80 | -80 | C | BRAIN | CEREBRAL AQUEDUCT | 1 | 2005-03-20 |
| 3 | ABC134 | BS | 43871 | 3 | 267FF | 1148.267 | FFRZMAT | Flash Freeze Material | SPECIMEN HANDLING | DRY ICE/ISOPROPANOL | | DRY ICE/ISOPROPANOL | | | BRAIN | CEREBRAL AQUEDUCT | 1 | 2005-03-20 |

The Device Identifiers (DI) dataset (required with the use of SPDEVID) is not shown in this example. RELREC relates the records in BE and BS to each other.

**Rows 1-2:** Tie the specimen's volume to its collection, when the measurement was made.

**Rows 3-4:** Tie the temperature to which the specimen was flash frozen to the event of its occurrence.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC134 | BE | 43871 | BESEQ | 1 | | 1 |
| 2 | ABC134 | BS | 43871 | BSSEQ | 1 | | 1 |
| 3 | ABC134 | BE | 43871 | BESEQ | 2 | | 2 |
| 4 | ABC134 | BS | 43871 | BSGRPID | 267FF | | 2 |

## Example 2

Cell-free RNA, which can be obtained from plasma, may be useful for some tumor-specific cancer detection, but has poor integrity. In this example, a blood sample was drawn, centrifuged to get plasma, and stored in a pretreated container before being shipped to the lab. The lab then extracted and purified RNA from the plasma, divided the RNA into 3 aliquots, and sequenced 1 aliquot immediately while freezing and storing the other 2 for later use.

**Row 1:** Shows the collection of the blood sample.

**Row 2:** Shows the extraction of the plasma via centrifuge. BESPDEVID holds the identifier for the container into which the plasma is placed. (Not shown: any preservatives with which the container comes pretreated, which would be stored in the Device Properties (DO) domain.)

**Row 3:** Shows the transportation of the plasma from the site to the lab.

**Row 4:** Shows the extraction of the RNA, which includes purification and quality control testing to make sure the sample is of a high enough quality to be viable. BESPDEVID holds the identifier for the purification kit.

**Rows 5-7:** Show the aliquoting of the RNA.

**Row 8:** Shows the sequencing of the first RNA aliquot. (Not shown: results from sequencing, which would be stored in the Pharmacogenomics Findings (PF) domain.)

**Rows 9-10:** Show the freezing of the second and third RNA aliquots.

**be.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | BESEQ | BEREFID | BETERM | BEDECOD | BEPARTY | BEPRTYID | BECAT | VISITNUM | BEDTC | BESTDTC | BEENDTC |
|-----|---------|--------|---------|---------|-------|---------|--------|---------|---------|----------|-------|----------|-------|---------|---------|
| 1 | 3441271 | BE | MU-298 | | 1 | 298B1 | Collecting | COLLECTING | SITE | 05 | COLLECTION | 2 | 2010-04-01T11:50 | 2010-04-01T11:50 | |
| 2 | 3441271 | BE | MU-298 | 293USHE8 | 2 | 298B1-1 | Extracting | EXTRACTING | SITE | 05 | EXTRACTION | 2 | 2010-04-01T11:50 | 2010-04-01T12:10 | |
| 3 | 3441271 | BE | MU-298 | | 3 | 298B1-1 | Shipping | SHIPPING | ABC LAB | | TRANSPORT | 2 | 2010-04-01T11:50 | 2010-04-01T15:00 | 2010-04-02T8:00 |
| 4 | 3441271 | BE | MU-298 | PURKIT | 4 | 298R1-1R0 | Extracting | EXTRACTING | ABC LAB | | EXTRACTION | 2 | 2010-04-01T11:50 | 2010-04-02T9:00 | 2010-04-05T13:50 |
| 5 | 3441271 | BE | MU-298 | | 5 | 298R1-1R1 | Aliquoting | ALIQUOTING | ABC LAB | | PREPARATION | 2 | 2010-04-01T11:50 | 2010-04-05T13:50 | |
| 6 | 3441271 | BE | MU-298 | | 6 | 298R1-1R2 | Aliquoting | ALIQUOTING | ABC LAB | | PREPARATION | 2 | 2010-04-01T11:50 | 2010-04-05T13:50 | |
| 7 | 3441271 | BE | MU-298 | | 7 | 298R1-1R3 | Aliquoted | ALIQUOTING | ABC LAB | | PREPARATION | 2 | 2010-04-01T11:50 | 2010-04-05T13:50 | |
| 8 | 3441271 | BE | MU-298 | | 8 | 298R1-1R1 | Sequenced | SEQUENCING | ABC LAB | | PREPARATION | 2 | 2010-04-01T11:50 | 2010-04-05T13:50 | 2010-04-06T10:30 |
| 9 | 3441271 | BE | MU-298 | | 9 | 298R1-1R2 | Frozen | FREEZING | ABC LAB | | PREPARATION | 2 | 2010-04-01T11:50 | 2010-04-05T13:50 | |
| 10 | 3441271 | BE | MU-298 | | 10 | 298R1-1R3 | Frozen | FREEZING | ABC LAB | | PREPARATION | 2 | 2010-04-01T11:50 | 2010-04-05T13:50 | |

The specimen type is given in a supplemental qualifier that mimics the standard findings variable --SPEC, and draws from the 2 codelists (GENSMP and SPECTYPE) for its values, depending on whether or not the biospecimen is a sample of the subject's genetic material.

**Rows 1-2:** Give the specimen types for the first 2 specimens as blood and plasma, respectively. These values come from the SPECTYPE codelist.

**Rows 3-6:** Give the specimen type for all subsequent specimens as RNA. "RNA" is one of the terms in the GENSMP codelist.

**suppbe.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | 3441271 | BE | MU-298 | BEREFID | 298B1 | BESPEC | Specimen Type | BLOOD | CRF | |
| 2 | 3441271 | BE | MU-298 | BEREFID | 298B1-1 | BESPEC | Specimen Type | PLASMA | CRF | |
| 3 | 3441271 | BE | MU-298 | BEREFID | 298R1-1R0 | BESPEC | Specimen Type | RNA | Collected | |
| 4 | 3441271 | BE | MU-298 | BEREFID | 298R1-1R1 | BESPEC | Specimen Type | RNA | Collected | |
| 5 | 3441271 | BE | MU-298 | BEREFID | 298R1-1R2 | BESPEC | Specimen Type | RNA | Collected | |
| 6 | 3441271 | BE | MU-298 | BEREFID | 298R1-1R3 | BESPEC | Specimen Type | RNA | Collected | |

**Row 1:** Shows the volume of the blood sample.

**Row 2:** Shows the volume of the plasma sample.

**Rows 3-4:** Show the volume and purity (integrity) of the RNA sample.

**Rows 5-7:** Show the volumes of the RNA aliquots.

**bs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | BSSEQ | BSREFID | BSTESTCD | BSTEST | BSCAT | BSORRES | BSORRESU | BSSTRESC | BSSTRESN | BSSTRESU | BSSPEC | VISITNUM | BSDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|-------|
| 1 | 3441271 | BS | MU-298 | 1 | 298B1 | VOLUME | Volume | SPECIMEN MEASUREMENT | 12 | mL | 6 | 6 | mL | BLOOD | 2 | 2010-04-01T11:50 |
| 2 | 3441271 | BS | MU-298 | 2 | 298B1-1 | VOLUME | Volume | SPECIMEN MEASUREMENT | 7 | mL | 6 | 6 | mL | PLASMA | 2 | 2010-04-01T11:50 |
| 3 | 3441271 | BS | MU-298 | 3 | 298R1-1R0 | VOLUME | Volume | SPECIMEN MEASUREMENT | 6 | mL | 6 | 6 | mL | RNA | 2 | 2010-04-01T11:50 |
| 4 | 3441271 | BS | MU-298 | 4 | 298R1-1R0 | RIN | RNA Integrity Number | QUALITY CONTROL | 9.3 | | 9.3 | 9.3 | | RNA | 2 | 2010-04-01T11:50 |
| 5 | 3441271 | BS | MU-298 | 5 | 298R1-1R1 | VOLUME | Volume | SPECIMEN MEASUREMENT | 2 | mL | 2 | 2 | mL | RNA | 2 | 2010-04-01T11:50 |
| 6 | 3441271 | BS | MU-298 | 6 | 298R1-1R2 | VOLUME | Volume | SPECIMEN MEASUREMENT | 2 | mL | 2 | 2 | mL | RNA | 2 | 2010-04-01T11:50 |
| 7 | 3441271 | BS | MU-298 | 7 | 298R1-1R3 | VOLUME | Volume | SPECIMEN MEASUREMENT | 2 | mL | 2 | 2 | mL | RNA | 2 | 2010-04-01T11:50 |

The results from the sequencing procedure are stored in the PF domain, which is not shown in this example. See GF datasets for examples of GF datasets.

The RELSPEC dataset preserves the specimen hierarchy.

**relspec.xpt**

| Row | STUDYID | USUBJID | REFID | SPEC | PARENT | LEVEL |
|-----|---------|---------|-------|------|--------|-------|
| 1 | 3441271 | MU-298 | 298B1 | BLOOD | 298B1 | 1 |
| 2 | 3441271 | MU-298 | 298B1-1 | PLASMA | 298B1 | 2 |
| 3 | 3441271 | MU-298 | 298R1-1R0 | RNA | 298B1-1 | 3 |
| 4 | 3441271 | MU-298 | 298R1-1R1 | RNA | 298R1-1R0 | 4 |
| 5 | 3441271 | MU-298 | 298R1-1R2 | RNA | 298R1-1R0 | 4 |
| 6 | 3441271 | MU-298 | 298R1-1R3 | RNA | 298R1-1R0 | 4 |

The relationship between BE and BS is often many-to-many because any given biospecimen may have multiple findings about it and may undergo multiple events.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | 3441271 | BE | | BEREFID | | MANY | 1 |
| 2 | 3441271 | BS | | BSREFID | | MANY | 1 |
| 3 | 3441271 | BE | MU-298 | BESEQ | 8 | | 2 |
| 4 | 3441271 | GF | MU-298 | GFSEQ | 1 | | 2 |
| 5 | 3441271 | GF | MU-298 | GFSEQ | 2 | | 2 |
| 6 | 3441271 | GF | MU-298 | GFSEQ | 3 | | 2 |

**References**

1. Tsui NB, Ng EK, Lo YM. Molecular analysis of circulating RNA in plasma. Methods Mol Biol. 2006;336:123-134. doi:10.1385/1-59745-074-X:123
2. Cerkovnik P, Perhavec A, Zgajnar J, Novakovic S. Optimization of an RNA isolation procedure from plasma samples. Int J Mol Med. 2007;20(3):293-300. doi:10.3892/ijmm.20.3.293
