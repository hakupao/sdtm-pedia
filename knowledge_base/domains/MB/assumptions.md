# MB — Assumptions

1. Representation of findings in the Microbiology Specimen domain should be handled as follows:
   a. In cases of tests that target an organism, group of organisms, or antigen for identification, MBTEST equals the name of the organism/antigen targeted by the identification assay, and
      i. MBTSTDTL should be "DETECTION".
      ii. The result should generally be "PRESENT"/"ABSENT", "POSITIVE"/"NEGATIVE", or "INDETERMINATE". However, there may be cases where a test differentiates between 2 or more similar organisms, in which case it would be appropriate for the result to be the name of the organism detected. For example, a test may look for influenza A or influenza B antigen. In this case, MBTEST would be "Influenza A/B Antigen"; the result could be "INFLUENZA A ANTIGEN", "INFLUENZA B ANTIGEN", or "INFLUENZA A/B ANTIGEN".
   b. For non-targeted identification of organisms (i.e., tests that have the ability to identify a range of organisms without specifically targeting any), the value for MBTESTCD/MBTEST should be "MCORGIDN"/"Microbial Organism Identification", and the result should be the name of the organism or group of organisms found to be present (e.g., "INFLUENZA A VIRUS SUBTYPE H1N1"; "CLONORCHIS SINENSIS"). In this scenario MBORRES is populated with values from the Microorganism Codelist (C85491).
   c. Culture characteristics covers concepts such as growth/no growth, colony quantification measures, colony color, colony morphology, and so on. **Note that this does not include drug susceptibility testing, which is represented in the Microbiology Susceptibility (MS) domain.**
      i. MBTESTCD/MBTEST should be the name of the organism or group of organisms being characterized.
      ii. MBTSTDTL should be the name of the characteristic being described (e.g., "COLONY COUNT", "VIRAL LOAD").
      iii. MBGRPID should be used to group characteristic records with the identification record of the organism to which the characteristics apply.
      iv. CDISC Controlled Terminology Rules for Microbiology (MB/MS) domains are available at https://www.cdisc.org/standards/terminology/controlled-terminology.

2. MBDTC represents the date the specimen was collected.

3. If the specimen was cultured, the start and end date of culture are represented in the Biospecimen Events (BE) domain in BESTDTC and BEENDTC respectively. The variable --REFID represents the sample ID as originally assigned in the BE domain. See BE domain assumptions in the SDTMIG v3.4, section 6.2.2, for guidelines on assigning --REFID values to samples and subsamples.
   a. Culture dates can be connected to the MB record via MBREFID and BEREFID.
   b. If the same sample is associated with many biospecimen events and tests, users may need to make use of additional linking variables such as --LNKID.

4. The variable NHOID is not allowed for use in the MB domain. Any additional Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the MB domain, but the following variables would not generally be used: --MODIFY, --BODSYS, --FAST, --TOX, --TOXGR, --SEV.
