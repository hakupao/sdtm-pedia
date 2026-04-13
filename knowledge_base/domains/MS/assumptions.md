# MS — Assumptions

1. Microbiology Susceptibility testing includes testing of the following types:
   a. Phenotypic drug susceptibility testing (qualitative), which may involve determining susceptibility/resistance (qualitative) at a predefined concentration of drug, or determining a specific dose (quantitative) at which a drug inhibits organism growth or some other process associated with virulence.
      i. For studies using qualitative testing methods, MSAGENT, MSCONC, and MSCONCU are used to represent the predefined drug, concentration, and units, respectively. Results are represented with values such as "SUSCEPTIBLE" or "RESISTANT".
      ii. For studies using quantitative testing methods, MSAGENT is used to represent the drug being tested; MSCONC and MSCONCU are not used. The concentration at which growth is inhibited is the result in these cases (MSORRES, MSSTRESC/MSSTRESN), with units being represented in MSORRESU/MSSTRESU.
      iii. As in 1.a.ii, MSAGENT should be populated with the drug whose action would be affected by the genetic marker being assessed via the genotypic test. MSCONC and MSCONCU are null in these records.
   b. Genetic tests that provide results in terms of susceptible/resistant only (e.g., nucleic acid amplification tests (NAAT)). Genotypic tests that provide results in terms of specific changes to nucleotides, codons, or amino acids of genes/gene products associated with resistance should be represented in the Genomic Findings (GF) domain, as that domain structure contains the variables necessary to accommodate data of this type. If a test provides both mutation data and susceptibility data, the mutation results should be represented in GF and the susceptibility information should be represented in MS. In these cases, the GF records should be linked via RELREC to susceptibility records in MS.
   c. CDISC Controlled Terminology Rules for Microbiology (MB/MS) domains are available at https://www.cdisc.org/standards/terminology/controlled-terminology.

2. MSDTC represents the date the specimen was collected.

3. If the specimen was cultured, the start and end date of culture are represented in the Biospecimen Events (BE) domain in BESTDTC and BEENDTC respectively. --REFID represents the sample ID as originally assigned in the BE domain. See BE domain assumptions in the SDTMIG v3.4, Section 6.2.2, for guidelines on assigning --REFID values to samples and subsamples.
   a. Culture dates can be connected to the MS record via MSREFID and BEREFID.
   b. If the same sample is associated with many biospecimen events and tests, users may need to make use of additional linking variables such as --LNKID.

4. NHOID is a sponsor-defined, intuitive name of the non-host organism being tested. It should only be populated with values representing what is known about the identity of the organism before the results of the test are determined. It should therefore never be used as a qualifier of result.

5. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the MS domain, but the following variables would not generally be used: --MODIFY, --BODSYS, --TOX, --TOXGR --SEV.
