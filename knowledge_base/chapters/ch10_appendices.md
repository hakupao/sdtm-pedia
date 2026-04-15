# SDTMIG v3.4 — Chapter 10: Appendices

Source: SDTMIG v3.4, Appendices A-F (Pages 444-461)

---

## Appendix A: CDISC SDS Team

The Submissions Data Standards (SDS) Team is responsible for the development of the SDTMIG. The team includes approximately 70 contributors from pharmaceutical companies, CROs, regulatory agencies, and technology vendors.

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
- Visit the CDISC Controlled Terminology page for the most recently published terminology packages (final or under review)
- The NCI Enterprise Vocabulary Services CDISC Terminology website provides access to the full list
- SDTM terminology was previously provided separately for questionnaires and other domains; as of the 2015-12-18 release, these were merged into a single publication
- Appendix C1 (Trial Summary Codes) was removed from SDTMIG v3.4; TS assumptions now reference CDISC controlled terminology directly

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

This appendix provides an overview of revisions since the last production version, SDTMIG v3.3.

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

### New Domains for SDTMIG v3.4

| Domain | Description |
|--------|-------------|
| BE | Biospecimen Events |
| BS | Biospecimen Findings |
| CP | Cell Phenotyping Findings |
| GF | Genomics Findings |
| RELSPEC | Related Specimens |

### Decommissioning of MO (Morphology)

The Morphology domain was removed in SDTMIG v3.4. When MO was introduced in v3.2, the intent was to represent morphology and physiology findings in separate domains. The team found this separation more difficult than anticipated and provided little added value. Body system-based domains now cover both morphology and physiology findings.

### Key Section-by-Section Changes

| Section | Change Summary |
|---------|---------------|
| 2.5 | Domain-specific versioning removed |
| 2.6 | SA added as reserved domain code |
| 2.7 | Updated based on SDTM v2.0 Usage Restrictions |
| 3.2 | Updated per MSG v2.0 and Define-XML v2.1 standards |
| 4.2 | USUBJID format clarification; new "Specify" values for --OBJ |
| 4.4 | Updated unknown values; --DRVFL clarified; --STDTC clarification for Findings |
| 4.5 | --DRVFL, --CLSIG, --REASPF, --REAS, --REASOC clarifications |
| 5.1 (CO) | Assumption 2 added; VISIT/VISITNUM/VISITDY removed from unused list |
| 5.2 (DM) | COUNTRY format clarification; updated DM Examples 4-7 |
| 5.5 (SV) | New variables added; now contains visits that did not occur |
| 6.1 | --DOSFRQ and --DOSRGM roles changed |
| 6.2.1 (AE) | New device-related variables added |
| 6.3.1 (DA) | Renamed from "Drug Accountability" to "Product Accountability" |
| 6.3.5 | Specimen-based Findings domains grouped with generic specification |
| 6.4 (FA) | "Events or Interventions" added to domain name |
| 7.3.2 (TD) | Assumption 4 inserted for schedule interval clarification |
| 8.8 (RELSPEC) | New section added from SDTMIG-PGx |
| App C | Appendix C1 Trial Summary Codes removed |
| App D | "V3.x dataset" replaced with "Findings dataset" |

---

## Appendix F: Representations and Warranties, Limitations of Liability, and Disclaimers

### CDISC Patent Disclaimers

Implementation of and compliance with this standard may require use of subject matter covered by patent rights. By publication of this standard, no position is taken with respect to the existence or validity of any claim or patent rights in connection therewith.

### Key Legal Terms

- CDISC grants open public use of this User Guide (or Final Standards) under CDISC's copyright
- All draft standards and final standards are provided "AS IS" with no warranties
- In no event will CDISC or any of its constituent parts be liable for any loss of profits, loss of use, or any damages
