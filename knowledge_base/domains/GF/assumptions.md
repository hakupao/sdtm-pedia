# GF — Assumptions

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
