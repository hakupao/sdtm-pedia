# SDTMIG v3.4 — Chapter 10: Appendices

Source: SDTMIG v3.4, Appendices A-F (Pages 444-461)

---

## Appendix A: CDISC SDS Team

The CDISC SDS Team would like to thank the many volunteers who contributed to the development, review, and publication of SDTMIG v3.4. Additionally, this publication would not have been possible without the support of the Foundational Team Leads, Global Governance Group, Regulatory Liaisons, and CDISC.

The contributor table lists approximately 70 individuals from pharmaceutical companies (e.g., Merck, GSK, Pfizer, Bayer, Boehringer Ingelheim, AstraZeneca, Biogen, Allergan, Eli Lilly), CROs (e.g., Charles River Laboratories, IQVIA, PRA Health Sciences, Emmes), regulatory and standards bodies (NCI-EVS), technology and data vendors (Quality Data Services, Clinical Solutions Group/IQVIA, Data Standards Consulting, Transendix LLC), and independent contractors. CDISC staff coordinated the project (Dana Booth, Project Manager). A full list of names and affiliations is available in the source PDF (SDTMIG v3.4, page 444).

---

## Appendix B: Glossary and Abbreviations

The following table lists some of the abbreviations and terms are used in this document. Additional definitions can be found in the individual sections of this document (see esp. Section 7.1.2, Definitions of Trial Design Concepts) and in the CDISC Glossary (available at https://www.cdisc.org/standards/glossary).

| Abbreviation | Full Term |
|-------------|-----------|
| ADaM | CDISC Analysis Dataset Model |
| ADSL | (ADaM) Subject-level Analysis Dataset |
| ATC | Anatomic Therapeutic Chemical (code; WHO) |
| CDASH | Clinical Data Acquisition Standards Harmonization |
| CDISC | Clinical Data Interchange Standards Consortium |
| CRF | Case report form (sometimes case record form) |
| CRO | Contract research organization |
| CTCAE | Common Terminology Criteria for Adverse Events |
| Dataset | A collection of structured data in a single file |
| Define-XML | CDISC standard for transmitting metadata that describes any tabular dataset structure |
| Domain | A collection of observations with a topic-specific commonality |
| eDT | Electronic data transfer |
| FDA | (US) Food and Drug Administration |
| HL7 | Health Level 7 |
| ICH | International Conference on Harmonisation of Technical Requirements for Registration of Pharmaceuticals for Human Use |
| ICH E2A | ICH guidelines on Clinical Safety Data Management: Definitions and Standards for Expedited Reporting |
| ICH E2B | ICH guidelines on Clinical Safety Data Management: Data Elements for Transmission of Individual Cases Safety Reports |
| ICH E3 | ICH guidelines on Structure and Content of Clinical Study Reports |
| ICH E9 | ICH guidelines on Statistical Principles for Clinical Trials |
| ISO | International Organization for Standardization |
| ISO 8601 | ISO character representation of dates, date/times, intervals, and durations of time. The SDTM uses the extended format |
| ISO 3166 | ISO codelist for representing countries; the Alpha-3 codelist uses 3-character codes |
| LOINC | Logical Observation, Identifiers, Names, and Codes |
| MedDRA | Medical Dictionary for Regulatory Activities |
| NCI | National Cancer Institute (NIH) |
| NSV | Non-standard variable |
| PRO | Patient-reported outcome |
| SAP | Statistical analysis plan |
| SDS | Submission Data Standards. Also the name of the team that created the SDTM and SDTMIG |
| SDTM | Study Data Tabulation Model |
| SDTMIG | Study Data Tabulation Model Implementation Guide: Human Clinical Trials |
| SDTMIG-AP | Study Data Tabulation Model Implementation Guide: Associated Persons |
| SDTMIG-MD | Study Data Tabulation Model Implementation Guide for Medical Devices |
| SDTMIG-PGx | Study Data Tabulation Model Implementation Guide: Pharmacogenomics/Genetics |
| SEND | Standard for Exchange of Non-Clinical Data |
| SNOMED | Systematized Nomenclature of Medicine (a dictionary) |
| SOC | System organ class |
| TDM | Trial Design Model |
| WHODRUG | World Health Organization Drug Dictionary |
| XML | eXtensible Markup Language |

---

## Appendix C: Controlled Terminology

CDISC Terminology is centrally managed by the CDISC Controlled Terminology Team, supporting the terminology needs of all CDISC foundational standards (SDTM, CDASH, ADaM, SEND) and all disease/therapeutic area standards.

### Key Points

- New/modified terms have a 3-month development period with quarterly public-review comment period followed by publication release
- Visit the CDISC Controlled Terminology page (https://www.cdisc.org/standards/terminology/controlled-terminology) for the most recently published terminology packages (final or under review)
- The NCI Enterprise Vocabulary Services CDISC Terminology website (https://www.cancer.gov/research/resources/terminology/cdisc) provides access to the full list of CDISC terminology
- SDTM terminology was previously provided separately for questionnaires and other domains; as of the 2015-12-18 release, these were merged into a single publication
- Earlier versions of the SDTMIG included several appendices regarding controlled terminology. Starting with SDTMIG 3.2, Appendix C was simplified. Appendix C1 will be considered for expansion in the next version, to contain a complete list of supplemental qualifiers used in the SDTMIG

### Appendix C1: Supplemental Qualifiers Name Codes

An initial set of standard name codes for use in supplemental qualifiers (SUPP--) datasets:

| QNAM | QLABEL | Applicable Domains |
|------|--------|--------------------|
| AESOSP | Other Medically Important SAE | AE |
| AETRTEM | Treatment Emergent Flag | AE |
| --REAS | Reason | Intervention domains where the reason is other than a medical indication. May be used in select Event domains (e.g., Healthcare Encounters) where the topic is not a medical condition |

---

## Appendix D: CDISC Variable-naming Fragments

The CDISC SDS group has defined a standard list of fragments to use as a guide when naming variables in SUPP-- datasets (as QNAM) or assigning --TESTCD values.

### Rules for Using Fragments

- The general rule is to use the fragment(s) that best conveys the meaning within the 8-character limit
- The longer fragment should be used when space allows
- If the combination still exceeds 8 characters, drop characters where most appropriate (avoiding naming conflicts)

### Fragment Reference Table

| Keyword(s) | Fragment | | Keyword(s) | Fragment |
|-----------|----------|-|-----------|----------|
| ACTION | ACN | | INDICATOR | IND |
| ADJUSTMENT | ADJ | | INTERPRETATION | INTP |
| ANALYSIS DATASET | AD | | INTERVAL | INT |
| ASSAY | AS | | INVESTIGATOR | INV |
| BASELINE | BL | | LIFE-THREATENING | LIFE |
| BIRTH | BRTH | | LOCATION | LOC |
| BODY | BOD | | LOINC CODE | LOINC |
| CANCER | CAN | | LOWER LIMIT | LO |
| CATEGORY | CAT | | NAME | NAM |
| CHARACTER | C | | NOT DONE | ND |
| CLASS | CLAS | | NUMBER | NUM |
| CLINICAL | CL | | NUMERIC | N |
| CODE | CD | | OBJECT | OBJ |
| COMMENT | COM | | ONGOING | ONGO |
| CONCOMITANT | CON | | ORDER | ORD |
| CONDITION | CND | | ORIGIN | ORIG |
| CONGENITAL | CONG | | ORIGINAL | OR |
| DATE TIME - CHARACTER | DTC | | OTHER | OTH, O |
| DAY | DY | | OUTCOME | OUT |
| DEATH | DTH | | OVERDOSE | OD |
| DECODE | DECOD | | PARAMETER | PARM |
| DERIVED | DRV | | PATTERN | PATT |
| DESCRIPTION | DESC | | POPULATION | POP |
| DISABILITY | DISAB | | POSITION | POS |
| DOSE, DOSAGE | DOS, DOSE | | QUALIFIER | QUAL |
| DURATION | DUR | | REASON | REAS |
| ELAPSED | EL | | REFERENCE | REF, RF |
| ELEMENT | ET | | REGIMEN | RGM |
| EMERGENT | EM | | RELATED | REL, R |
| END | END, EN | | RELATIONSHIP | REL |
| ETHNICITY | ETHNIC | | RESULT | RES |
| EVALUATION | EVL | | RULE | RL |
| EVALUATOR | EVAL | | SEQUENCE | SEQ |
| EXTERNAL | X | | SERIOUS | S, SER |
| FASTING | FAST | | SEVERITY | SEV |
| FILENAME | FN | | SIGNIFICANT | SIG |
| FLAG | FL | | SPECIMEN | SPEC, SPC |
| FORMULATION, FORM | FRM | | SPONSOR | SP |
| FREQUENCY | FRQ | | STANDARD | ST, STD |
| GRADE | GR | | START | ST |
| GROUP | GRP | | STATUS | STAT |
| HOSPITALIZATION | HOSP | | NORMAL RANGE | NR |
| IDENTIFIER | ID | | SUBJECT | SUBJ |
| INDICATION | INDC | | SUBCATEGORY | SCAT |
| MEDICALLY-IMPORTANT EVENT | MIE | | SUPPLEMENTAL | SUPP |
| NON-STUDY THERAPY | NST | | |
| | | | SYSTEM | SYS |
| | | | TEXT | TXT |
| | | | TIME | TM |
| | | | TIME POINT | TPT |
| | | | TOTAL | TOT |
| | | | TOXICITY | TOX |
| | | | TRANSITION | TRANS |
| | | | TREATMENT | TRT |
| | | | UNIQUE | U |
| | | | UNIT | U |
| | | | UNPLANNED | UP |
| | | | UPPER LIMIT | HI |
| | | | VALUE | VAL |
| | | | VARIABLE | VAR |
| | | | VEHICLE | V |

---

## Appendix E: Revision History

This appendix provides an overview only of revisions since the last production version, SDTMIG v3.3; not all revisions are included.

- A Diff file with details of changes to domain specification tables is available as a member benefit on the CDISC Library Archives page in the Members Only Area of the CDISC website (https://www.cdisc.org/members-only/cdisc-library-archives), and those changes are not repeated here.
- Public review comments and their dispositions will be available upon publication of the SDTMIG.

### General Changes Throughout

- Text and examples clarified as needed
- Text updated to reflect new table names in SDTM v2.0
- Values updated to current CDISC Controlled Terminology
- ISO formats made more granular
- New variables from SDTM v2.0 added
- Domain tables replaced with sectional table of contents
- Supplemental qualifier variable names updated to include 2-character domain abbreviations
- Assumptions providing domain definitions removed (now in Description/Overview)
- Numbered lists in CDISC Notes converted to text for consistency
- Links were updated as needed
- Typographical errors were corrected

### New Domains for SDTMIG v3.4

| Domain | Description |
|--------|-------------|
| BE | Biospecimen Events |
| BS | Biospecimen Findings |
| CP | Cell Phenotyping Findings |
| GF | Genomics Findings |
| RELSPEC | Related Specimens |

### Decommissioning of MO (Morphology)

The following domain was removed:

- Morphology (MO)

When the Morphology domain was introduced in SDTMIG v3.2, the SDS Team planned to represent morphology and physiology findings in separate domains: morphology findings in the MO domain and physiology findings in separate domains by body systems. Since then, the team found that separating morphology and physiology findings was more difficult than anticipated and provided little added value. This led to the decision to expand the body system-based domains to cover both morphology and physiology findings and to deprecate MO in SDTMIG v3.4. Submissions using that later SDTMIG version would represent morphology results in the appropriate body system-based physiology/morphology domain.

For data prepared using a version of the SDTMIG that includes both the MO domain and body system-based physiology/morphology domains, morphology findings may be represented in either the MO domain or in a body-system based physiology/morphology domain. Custom body system-based domains may be used if the appropriate body system-based domain is not included in the SDTMIG version being used.

### Key Section-by-Section Changes

In addition to the general changes described above, the following table provides an overview of changes by section.

| Section Number | Section Name | Change(s) |
|---------------|--------------|-----------|
| **Section 1. Introduction** | | |
| 1.3 | Relationship to Prior CDISC Documents | Rather than referring to all sections with significant changes, some of the more significant changes since SDTMIG v3.3 are highlighted in a bulleted list |
| **Section 2. Fundamentals of the SDTM** | | |
| 2.1 | Observations and Variables | Revised definition for Rule Variables |
| 2.5 | The SDTM Standard Domain Models | Domain-specific versioning (introduced in SDTMIG v3.3) removed; domain version numbers removed for each domain; removed sentence referring to FDA repository; added reference to Define-XML standard for details on no data availability |
| 2.6 | Creating a New Domain | SA added to bullet 3e to reserve the domain code for CDASH; SQ also added as it occurs in the SDTMIG-AP |
| 2.7 | SDTM Variables Not Allowed in the SDTMIG | Updated based on Usage Restrictions column of Study Data Tabulation Model 2.0; Moved --METHOD (Interventions) from not-evaluated list to list of variables not to be used; updated order of list to match order within the model |
| **Section 3. Submitting Data in a Standard Format** | | |
| 3.2 | Using the CDISC Domain Models in Regulatory Submissions — Dataset Metadata | Removed paragraph about empty datasets for small PK studies per MSG v2.0 and Define-XML v2.1 standard |
| 3.2.1 | Dataset-level Metadata | Changes to SDTMIG Content Control appear in this table; new domains added and MO removed |
| 3.2.1.2 | CDISC Submission Value-level Metadata | The phrase "the SDTMIG V3.x" removed from the first sentence |
| **Section 4. Assumptions for Domain Models** | | |
| 4.1 | General Domain Assumptions | QRS Examples for splitting questionnaires updated; Origin Metadata traceability clarified |
| 4.2 | General Variable Assumptions | Added CDISC note on acceptable USUBJID formats; 4.2.6 numbering reworked; new subsection 4.2.7.4 "Specify" Values for --OBJ added; added information about ASCII characters to Section 4.2.9 |
| 4.4 | Actual and Relative Time Assumptions | Updated unknown values from U to UNKNOWN; clarified reference time point; added note that --STDTC is not used in Findings class domains; clarified use of --DRVFL |
| 4.5 | Original and Standardized Results | Clarified description of --DRVFL; two QRS exceptions added to 4.5.1.2; corrected IDVARVAL in supppr.xpt Example 3; promoted --CLSIG to SDTM variable; clarified --REASPF, --REAS, and --REASOC usage; added text for pre-specified groups of interventions or events in --TRT or --TERM |
| **Section 5. Models for Special-purpose Domains** | | |
| 5 | Models for Special-purpose Domains | All SDTMIG v3.4 metadata specifications updated to reflect ISO 8601 granularity |
| 5.1 | Comments (CO) | Assumption 2 added; VISIT, VISITNUM, and VISITDY removed from list of generally not used variables; clarity added to Assumption 1 regarding adverse events and clinical events |
| 5.2 | Demographics (DM) | Revised DM.COUNTRY CDISC Notes; Assumption 6 updated for race self-identification; updated assumption 6a to reference Racec-Ethnicc Codetable; extensive DM example updates |
| 5.3 | Subject Elements (SE) | Added SESTDY and SEENDY |
| 5.4 | Subject Disease Milestones (SM) | Updated CDISC notes for USUBJID for consistency |
| 5.5 | Subject Visits (SV) | Domain considered for moving to Events but kept as Subject Visits; now contains visits that did not occur; new variables added: SVPRESP, SVOCCUR, SVREASOC, SVCNTMOD, SVEPCHGI |
| **Section 6. Domain Models Based on the General Observation Classes** | | |
| 6.1 | Models for Interventions Domains | Roles of --DOSFRQ and --DOSRGM changed where used in the Interventions Domains to Record Qualifier for consistency with the change for the role of --DOSFRQ and --DOSRGM in the SDTM |
| 6.1.2 | Concomitant/Prior Medications (CM) | Example 5 is new |
| 6.1.3 | Exposure Domains | EX assumptions updated to note that since EX includes only treatments received, --MOOD would generally not be used in EX; ECREASOC added (promoted from supplemental qualifier to standard variable); examples updated |
| 6.1.5 | Procedures (PR) | PRSEQ's CDISC Notes updated to reflect that Sequence Number is given to ensure uniqueness of subject records within a domain; added CT reference for PRDECOD variable; more explanations provided in examples for why values in PRTRT are in mixed case |
| 6.2 | Models for Events Domains | BE Domain specification and examples copied from SDTMIG-PGx (originally published 2015-05-26), to be deprecated with publication of SDTMIG v3.4 |
| 6.2.1 | Adverse Events (AE) | New AE variables for Medical Devices added: SPDEVID, AEACNDEV, AEUNANT, AERLPRC, AERLPRT, AERLDEV, AESINTV; new Examples 5 and 6; deleted AE Assumption 2e as superseded; Assumption 6 (Actions taken) added |
| 6.2.2 | Biospecimen Events (BE) | Specification, assumptions, and examples copied from SDTMIG-PGx (published 2015-05-26); BETERM and BEDECOD updated; PF updated to GF; to be deprecated with publication of SDTMIG v3.4 |
| 6.2.3 | Clinical Events (CE) | Added permissible variable CETOXGR; added fracture events example; Examples 1 and 2 revised for clarity |
| 6.2.4 | Disposition (DS) | DSDY's Core value updated to Perm (from Exp); DSSTDY's Core value updated to Exp (from Perm); added reference to DS Codetable; updated Example 9 |
| 6.2.5 | Healthcare Encounters (HO) | Example 5 and Assumption 5 corrected to refer to Events qualifiers |
| 6.2.6 | Medical History (MH) | Example 5 added to illustrate presence of prespecified events |
| 6.2.7 | Protocol Deviations (DV) | Revised label for DVENDY to 'Study Day of End of Deviation Event'; Assumption 3 corrected to refer to Events qualifiers |
| 6.3 | Models for Findings Domains | BS Domain specification and examples copied from SDTMIG-PGx (originally published 2015-05-26), to be deprecated; assumptions and examples updated where --CLSIG is promoted to standard variable |
| 6.3.1 | Product Accountability (DA) | Renamed from "Drug Accountability" to "Product Accountability"; added permissible variables DALNKID and DALNKGRP; revised assumptions to describe broadened product accountability scope; excluded devices |
| 6.3.2 | Death Details (DD) | Added assumption 4 referencing the domain codetable |
| 6.3.3 | ECG Test Results (EG) | Added EGCLSIG as permissible variable; updated EGBEATNO role from "Variable Qualifier" to "Identifier" to align with SDTM v2.0; added Assumption 2a referencing the ECG codetable |
| 6.3.5 | Specimen-based Findings Domains | Added Section 6.3.5 to group domains (e.g., IS, LB, MB/MS, MI, PC/PP) that represent laboratory measurements, tests, or examinations performed on collected biological specimens |
| 6.3.5.1 | Generic Specimen-based Lab Findings Domain Specification | Added generic metadata specification for commonly used variables in specimen-based laboratory domains |
| 6.3.5.2 | Biospecimen Findings (BS) | Newly copied from SDTMIG-PGx with only minor corrections; Row 5 removed as well as reference to the Maycox paper |
| 6.3.5.3 | Cell Phenotype Findings (CP) | This is a new domain |
| 6.3.5.4 | Genomics Findings (GF) | New domain replacing the PF domain from the provisional SDTMIG-PGx; to be deprecated with publication of SDTMIG v3.4 |
| 6.3.5.5 | Immunogenicity Specimen Assessments (IS) | Domain definition updated; 6 new variables added: ISBDAGNT, ISMSCBCE, ISTSTOPO, ISTSTCND, ISNCNDAGT, and NHOID; replaced assumptions from SDTMIG v3.3; Examples 1 and 2 replaced; Examples 3-11 added |
| 6.3.5.6 | Laboratory Test Results (LB) | Revised LBTESTCD variable label to Lab Test or Examination Short Name; revised Core value for LBSTREFC to Perm (from Exp); added new variables: LBTSTCND, LBDAGNT, LBTSTOPO, LBRSLSCL, LBRESTYP, LBCOLSRT, LBLLOD, LBTMTHSN, LBCLSIG, LBPTFL, and LBPDUR; added permissible variables: LBSPCUFL, LBANMETH, LBORREF, LBSTREFN; LBORREF, LBSTREFC, and LBSTREFN removed because there is no clear use case; updated several assumptions; added Assumption 8; revised Examples 1-3; added Examples 4 and 5 |
| 6.4 | Findings About Events or Interventions | Added "Events or Interventions" to the FA domain name; added assumption 4a referencing the CV codetable |
| 6.4.1 | When to Use Findings About Events or Interventions | Additional explanation and examples added for each criterion; new criterion added in version that underwent first public review was removed; new "Points to Consider" section added; third and fourth bullets dropped as criterion for representing data in FA |
| 6.4.3 | Variables Unique to Findings About | Added sentence clarifying that an FA record will not necessarily have a parent record |
| 6.4.4 | Findings About Events or Interventions (FA) | Core value for FADTC changed from "Perm" to "Exp"; updated FATEST and FATESTCD CDISC Notes to reference general codelists; added assumption 4a referencing CV Code table; extensive updates to examples for clarity |
| 6.4.5 | Skin Response (SR) | Updated CDISC Notes for USUBJID; revised representation of quadrants in Example 1; Example 3 updated per CDISC CT |
| **Section 7. Trial Design Model Datasets** | | |
| 7.2 | Experimental Design (TA and TE) | Text about executable code in Section 7.2.1.1 replaced to note that a mechanism to provide machine-readable rules will become available in the future; aligned wording for Rule variables on CDISC Notes between TA and TE; dataset name in Section 7.2.2.1 example changed from "ta.xpt" to "special.xpt" |
| 7.3.1 | Trial Visits (TV) | Made VISIT required and revised VISIT CDISC Notes |
| 7.3.2 | Trial Disease Assessments (TD) | Assumption 4 inserted to clarify that start of a schedule is the start of the interval preceding the first assessment; Examples 1 and 3 diagrams updated; values of TDSTOFF corrected |
| 7.3.3 | Trial Disease Milestones (TM) | Role of TMDEF changed from "Rule" to "Variable Qualifier" for consistency with clarification of the Rule role in SDTM |
| 7.4 | Trial Eligibility and Summary (TI and TS) | Order had been flipped here for TI and TS; has now been corrected and the section numbers updated |
| 7.4.1 | Trial Inclusion/Exclusion Criteria (TI) | The section describing the proposed removal of TIRL was added |
| 7.4.2 | Trial Summary (TS) | Changed the CDISC Notes for TSSEQ to reflect that the sequence number is to ensure uniqueness within a parameter; revisions to most TS assumptions to remove references to Appendix C1 Trial Summary Codes (as this appendix was removed); TS assumptions replaced with ones that note recipients may specify requirements and terminology; reference added for the TS Codetable on the CDISC website; revised TS Assumption 17 to clarify value expectations for TSPARMCD = "INDIC"; additional assumptions revised for clarity; information added about exploratory outcome measures; Examples 1-3 revised; new Example 4 added to show use of TSGRPID for study parts and treatments |
| **Section 8. Representing Relationships and Data** | | |
| 8 | Representing Relationships and Data | Section 8.8 (Related Specimens) added due to BE, BS, and RELSPEC being copied in from SDTMIG-PGx, originally published 2015-05-26, to be deprecated with the publication of SDTMIG v3.4 |
| 8.2.2 | RELREC Dataset Examples | Introductory text updated to more clearly describe how relationships are represented in RELREC |
| 8.4.1 | Supplemental Qualifiers (SUPP--) | Updated CDISC Notes for USUBJID to include description of the variable used in other domains; updated Appendix C2 reference to Appendix C1 |
| 8.6.2 | Guidelines for Forming New Domains | Updated section references and links |
| 8.6.3 | Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions | "Interventions" added to section title; some changes to text to correct typos and clarify wording; second column of second row of table revised to explain what a log form is and to clarify how the data collection format may help understand the general observation class of data collected; added a row to the table to help in deciding between QS and FA for data about symptoms; reordered sentences in paragraph after the table and reiterated reference to AE structure assumption |
| 8.8 | Related Specimens (RELSPEC) | This section was added to SDTMIG v3.4 in preparation for the eventual retirement of the SDTMIG-PGx, originally published 2015-05-26, to be deprecated with the publication of SDTMIG v3.4 |
| **Section 9. Study References** | | |
| 9 | Study References | Removed "Identifiers for pharmacogenomic/genetic biomarkers" from the list; deleted Section 9.3 PB as it was part of SDTMIG-PGx (originally published 2015-05-26, to be deprecated with the publication of SDTMIG v3.4) |
| **Appendices** | | |
| Appendix A | CDISC SDS Team | The team list has been updated |
| Appendix C | Controlled Terminology | Appendix C1 Trial Summary Codes has been removed from SDTMIG v3.4; TS Assumptions were updated to reference CDISC controlled terminology, CDISC TS codetable, and recipient (regulatory agency) implementation expectations; removed --CLSIG due to promotion as a Findings variable; added --REASOC; all references to Appendix C2 in the SDTMIG were changed to Appendix C1 |
| Appendix D | CDISC Variable-naming Fragments | "V3.x dataset" was replaced with "Findings dataset" because the V3.x terminology was somewhat confusing and is being phased out |
| Appendix E | This appendix | This appendix was updated to reflect an overview of changes from SDTMIG v3.3 to SDTMIG v3.4 |

---

## Appendix F: Representations and Warranties, Limitations of Liability, and Disclaimers

### CDISC Patent Disclaimers

It is possible that implementation of and compliance with this standard may require use of subject matter covered by patent rights. By publication of this standard, no position is taken with respect to the existence or validity of any claim or of any patent rights in connection therewith. CDISC, including the CDISC Board of Directors, shall not be responsible for identifying patents for which a license may be required in order to implement this standard or for conducting inquiries into the legal validity or scope of those patents or patent claims that are brought to its attention.

### Representations and Warranties

"CDISC grants open public use of this User Guide (or Final Standards) under CDISC's copyright."

Each Participant in the development of this standard shall be deemed to represent, warrant, and covenant, at the time of a Contribution by such Participant (or by its Representative), that to the best of its knowledge and ability: (a) it holds or has the right to grant all relevant licenses to any of its Contributions in all jurisdictions or territories in which it holds relevant intellectual property rights; (b) there are no limits to the Participant's ability to make the grants, acknowledgments, and agreements herein; and (c) the Contribution does not subject any Contribution, Draft Standard, Final Standard, or implementations thereof, in whole or in part, to licensing obligations with additional restrictions or requirements inconsistent with those set forth in the CDISC Intellectual Property Policy ("the Policy"), or that would require any such Contribution, Final Standard, or implementation, in whole or in part, to be either: (i) disclosed or distributed in source code form; (ii) licensed for the purpose of making derivative works (other than as set forth in Section 4.2 of the CDISC Intellectual Property Policy); or (iii) distributed at no charge, except as set forth in Sections 3, 5.1, and 4.2 of the Policy. If a Participant has knowledge that a Contribution made by any Participant or any other party may subject any Contribution, Draft Standard, Final Standard, or implementation, in whole or in part, to one or more of the licensing obligations listed in Section 9.3, such Participant shall give prompt notice of the same to the CDISC President who shall promptly notify all Participants.

### No Other Warranties/Disclaimers

ALL PARTICIPANTS ACKNOWLEDGE THAT, EXCEPT AS PROVIDED UNDER SECTION 9.3 OF THE CDISC INTELLECTUAL PROPERTY POLICY, ALL DRAFT STANDARDS AND FINAL STANDARDS, AND ALL CONTRIBUTIONS TO FINAL STANDARDS AND DRAFT STANDARDS, ARE PROVIDED "AS IS" WITH NO WARRANTIES WHATSOEVER, WHETHER EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE, AND THE PARTICIPANTS, REPRESENTATIVES, THE CDISC PRESIDENT, THE CDISC BOARD OF DIRECTORS, AND CDISC EXPRESSLY DISCLAIM ANY WARRANTY OF MERCHANTABILITY, NONINFRINGEMENT, FITNESS FOR ANY PARTICULAR OR INTENDED PURPOSE, OR ANY OTHER WARRANTY OTHERWISE ARISING OUT OF ANY PROPOSAL, FINAL STANDARDS OR DRAFT STANDARDS, OR CONTRIBUTION.

### Limitation of Liability

IN NO EVENT WILL CDISC OR ANY OF ITS CONSTITUENT PARTS (INCLUDING, BUT NOT LIMITED TO, THE CDISC BOARD OF DIRECTORS, THE CDISC PRESIDENT, CDISC STAFF, AND CDISC MEMBERS) BE LIABLE TO ANY OTHER PERSON OR ENTITY FOR ANY LOSS OF PROFITS, LOSS OF USE, DIRECT, INDIRECT, INCIDENTAL, CONSEQUENTIAL, OR SPECIAL DAMAGES, WHETHER ARISING UNDER CONTRACT, TORT, WARRANTY, OR OTHERWISE, ARISING IN ANY WAY OUT OF THIS POLICY OR ANY RELATED AGREEMENT, WHETHER OR NOT SUCH PARTY HAD ADVANCE NOTICE OF THE POSSIBILITY OF SUCH DAMAGES.

Note: The CDISC Intellectual Property Policy can be found at http://www.cdisc.org/system/files/all/article/application/pdf/cdisc_20ip_20policy_final.pdf
