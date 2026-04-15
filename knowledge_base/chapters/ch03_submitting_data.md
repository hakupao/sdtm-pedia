# SDTMIG v3.4 — Chapter 3: Submitting Data in Standard Format

Source: SDTMIG v3.4, Section 3 (Pages 17-21)

## 3.1 Standard Metadata for Dataset Contents and Attributes

The SDTMIG provides standard descriptions of some of the most commonly used data domains, with metadata attributes. These include descriptive metadata attributes that should be included in a Define-XML document. In addition, the CDISC domain models include 2 shaded columns that are not sent to the FDA, but which assist sponsors:

- **CDISC Notes column** — information regarding the relevant use of each variable
- **Core column** — indicates how a variable is classified (see Section 4.1.5, SDTM Core Designations)

The domain models in Section 6, Domain Models Based on the General Observation Classes, illustrate how to apply the SDTM when creating a specific domain dataset. In particular, these models illustrate the selection of a subset of the variables offered in 1 of the general observation classes, along with applicable timing variables. The models also show how a standard variable from a general observation class should be adjusted to meet the specific content needs of a particular domain, including making the label more meaningful, specifying controlled terminology, and creating domain-specific notes and examples. Thus, the domain models not only demonstrate how to apply the model for the most common domains but also give insight on how to apply general model concepts to other domains not yet defined by CDISC.

## 3.2 Using the CDISC Domain Models in Regulatory Submissions — Dataset Metadata

The Define-XML document that accompanies a submission should also describe each dataset that is included in the submission and describe the natural key structure of each dataset. Most studies will include Demographics (DM) and a set of safety domains based on the 3 general observation classes — typically including Exposure (EX), Concomitant and Prior Medications (CM), Adverse Events (AE), Disposition (DS), Medical History (MH), Laboratory Test Results (LB), and Vital Signs (VS). However, choosing which data to submit will depend on the protocol and the needs of the regulatory review division or agency.

Dataset definition metadata should include:
- Dataset filenames, descriptions, locations, structures, class, purpose, and keys

**Note:** "In the event that no records are present in a dataset (e.g., a small PK study where no subjects took concomitant medications), the empty dataset should not be submitted and should not be described in the Define-XML document."

### 3.2.1 Dataset-level Metadata

**Note:** The key variables shown in this table are examples only. A sponsor's actual key structure may be different. The order of classes and datasets in this table is not intended as a normative order of datasets in a submission.

The Dataset-level Metadata table provides examples of dataset structures:

| Dataset | Description | Class | Structure | Purpose | Keys | Location |
|---------|-------------|-------|-----------|---------|------|----------|
| CO | Comments | Special Purpose | One record per comment per subject | Tabulation | STUDYID, USUBJID, IDVAR, COREF, COOTC | co.xpt |
| DM | Demographics | Special Purpose | One record per subject | Tabulation | STUDYID, USUBJID | dm.xpt |
| SE | Subject Elements | Special Purpose | One record per actual Element per subject | Tabulation | STUDYID, USUBJID, ETCD, SESTDTC | se.xpt |
| SM | Subject Disease Milestones | Special Purpose | One record per Disease Milestone per subject | Tabulation | STUDYID, USUBJID, MIDS | sm.xpt |
| SV | Subject Visits | Special Purpose | One record per actual or planned visit per subject | Tabulation | STUDYID, USUBJID, SVTERM | sv.xpt |
| AG | Procedure Agents | Interventions | One record per recorded intervention occurrence per subject | Tabulation | STUDYID, USUBJID, AGTRT, AGSTDTC | ag.xpt |
| CM | Concomitant/Prior Medications | Interventions | One record per recorded intervention occurrence or constant-dosing interval per subject | Tabulation | STUDYID, USUBJID, CMTRT, CMSTDTC | cm.xpt |
| EC | Exposure as Collected | Interventions | One record per protocol-specified study treatment, collected-dosing interval, per subject, per mood | Tabulation | STUDYID, USUBJID, ECTRT, ECSTDTC, ECMOOD | ec.xpt |
| EX | Exposure | Interventions | One record per protocol-specified study treatment, constant-dosing interval, per subject | Tabulation | STUDYID, USUBJID, EXTRT, EXSTDTC | ex.xpt |
| ML | Meal Data | Interventions | One record per food product occurrence or constant intake interval per subject | Tabulation | STUDYID, USUBJID, MLTRT, MLSTDTC | ml.xpt |
| PR | Procedures | Interventions | One record per recorded procedure per occurrence per subject | Tabulation | STUDYID, USUBJID, PRTRT, PRSTDTC | pr.xpt |
| SU | Substance Use | Interventions | One record per substance type per reported occurrence per subject | Tabulation | STUDYID, USUBJID, SUTRT, SUSTDTC | su.xpt |
| AE | Adverse Events | Events | One record per adverse event per subject | Tabulation | STUDYID, USUBJID, AEDECOD, AESTDTC | ae.xpt |
| BE | Biospecimen Events | Events | One record per instance per biospecimen event per biospecimen identifier per subject | Tabulation | STUDYID, USUBJID, BEREFID, BETERM, BESTDTC | be.xpt |
| CE | Clinical Events | Events | One record per event per subject | Tabulation | STUDYID, USUBJID, CETERM, CESTDTC | ce.xpt |
| DS | Disposition | Events | One record per disposition status or protocol milestone per subject | Tabulation | STUDYID, USUBJID, DSDECOD, DSSTDTC | ds.xpt |
| DV | Protocol Deviations | Events | One record per protocol deviation per subject | Tabulation | STUDYID, USUBJID, DVTERM, DVSTDTC | dv.xpt |
| HO | Healthcare Encounters | Events | One record per healthcare encounter per subject | Tabulation | STUDYID, USUBJID, HOTERM, HOSTDTC | ho.xpt |
| MH | Medical History | Events | One record per medical history event per subject | Tabulation | STUDYID, USUBJID, MHDECOD | mh.xpt |
| BS | Biospecimen Findings | Findings | One record per measurement per biospecimen identifier per subject | Tabulation | STUDYID, USUBJID, BSREFID, BSTESTCD | bs.xpt |
| CP | Cell Phenotype Findings | Findings | One record per test per specimen per timepoint per visit per subject | Tabulation | STUDYID, USUBJID, CPTESTCD, CPSPEC, VISITNUM, CPTPTREF, CPTPTNUM | cp.xpt |
| CV | Cardiovascular System Findings | Findings | One record per finding or result per time point per visit per subject | Tabulation | STUDYID, USUBJID, VISITNUM, CVTESTCD, CVTPTREF, CVTPTNUM | cv.xpt |
| DA | Product Accountability | Findings | One record per product accountability finding per subject | Tabulation | STUDYID, USUBJID, DATESTCD, DADTC | da.xpt |
| DD | Death Details | Findings | One record per finding per subject | Tabulation | STUDYID, USUBJID, DDTESTCD, DDDTC | dd.xpt |
| EG | ECG Test Results | Findings | One record per ECG observation per replicate per time point or one record per ECG observation per beat per visit per subject | Tabulation | STUDYID, USUBJID, EGTESTCD, VISITNUM, EGTPTREF, EGTPTNUM, EGREPNUM | eg.xpt |
| FT | Functional Tests | Findings | One record per Functional Test finding per time point per visit per subject | Tabulation | STUDYID, USUBJID, FTTESTCD, VISITNUM, FTTPTREF, FTTPTNUM | ft.xpt |
| GF | Genomics Findings | Findings | One record per finding per observation per biospecimen per subject | Tabulation | STUDYID, USUBJID, GFTESTCD, GFSPEC, VISITNUM, GFTPTREF, GFTPTNUM | gf.xpt |
| IE | Inclusion/Exclusion Criteria Not Met | Findings | One record per inclusion/exclusion criterion not met per subject | Tabulation | STUDYID, USUBJID, IETESTCD | ie.xpt |
| IS | Immunogenicity Specimen Assessments | Findings | One record per test per visit per subject | Tabulation | STUDYID, USUBJID, ISTESTCD, ISBDAGNT, ISSCMBDL, ISSTOPO, VISITNUM | is.xpt |
| LB | Laboratory Test Results | Findings | One record per lab test per time point per visit per subject | Tabulation | STUDYID, USUBJID, LBTESTCD, LBSPEC, VISITNUM, LBTPTREF, LBTPTNUM | lb.xpt |
| MB | Microbiology Specimen | Findings | One record per microbiology specimen finding per time point per visit per subject | Tabulation | STUDYID, USUBJID, MBTESTCD, VISITNUM, MBTPTREF, MBTPTNUM | mb.xpt |
| MI | Microscopic Findings | Findings | One record per finding per specimen per subject | Tabulation | STUDYID, USUBJID, MISPEC, MITESTCD | mi.xpt |
| MK | Musculoskeletal System Findings | Findings | One record per assessment per visit per subject | Tabulation | STUDYID, USUBJID, VISITNUM, MKTESTCD, MKLOC, MKLAT | mk.xpt |
| MS | Microbiology Susceptibility | Findings | One record per microbiology susceptibility test (or other organism-related finding) per organism found in MB | Tabulation | STUDYID, USUBJID, MSTESTCD, VISITNUM, MSTPTREF, MSTPTNUM | ms.xpt |
| NV | Nervous System Findings | Findings | One record per finding per location per time point per visit per subject | Tabulation | STUDYID, USUBJID, VISITNUM, NVTPTNUM, NVLOC, NVTESTCD | nv.xpt |
| OE | Ophthalmic Examinations | Findings | One record per ophthalmic finding per method per location, per time point per visit per subject | Tabulation | STUDYID, USUBJID, FOCID, OETESTCD, OETSTDTL, OEMETHOD, OELOC, OELAT, OEDIR, VISITNUM, OEDTC, OETPTREF, OETPTNUM, OEREPNUM | oe.xpt |
| PC | Pharmacokinetics Concentrations | Findings | One record per sample characteristic or time-point concentration per reference time point or per analyte per subject | Tabulation | STUDYID, USUBJID, PCTESTCD, VISITNUM, PCTPTREF, PCTPTNUM | pc.xpt |
| PE | Physical Examination | Findings | One record per body system or abnormality per visit per subject | Tabulation | STUDYID, USUBJID, PETESTCD, VISITNUM | pe.xpt |
| PP | Pharmacokinetics Parameters | Findings | One record per PK parameter per time-concentration profile per modeling method per subject | Tabulation | STUDYID, USUBJID, PPTESTCD, PPCAT, VISITNUM, PPRFTDTC | pp.xpt |
| QS | Questionnaires | Findings | One record per questionnaire per question per time point per visit per subject | Tabulation | STUDYID, USUBJID, QSCAT, QSSCAT, VISITNUM, QSTESTCD | qs.xpt |
| RE | Respiratory System Findings | Findings | One record per finding or result per time point per visit per subject | Tabulation | STUDYID, USUBJID, VISITNUM, RETESTCD, RETPTNUM, REREPNUM | re.xpt |
| RP | Reproductive System Findings | Findings | One record per finding or result per time point per visit per subject | Tabulation | STUDYID, DOMAIN, USUBJID, RPTESTCD, VISITNUM | rp.xpt |
| RS | Disease Response and Clin Classification | Findings | One record per response assessment or clinical classification assessment per time point per visit per subject per assessor per medical evaluator | Tabulation | STUDYID, USUBJID, RSTESTCD, VISITNUM, RSTPTREF, RSEVAL, RSPTPNUM, RSEVALID | rs.xpt |
| SC | Subject Characteristics | Findings | One record per characteristic per visit per subject. | Tabulation | STUDYID, USUBJID, SCTESTCD, VISITNUM | sc.xpt |
| SS | Subject Status | Findings | One record per status per visit per subject | Tabulation | STUDYID, USUBJID, SSTESTCD, VISITNUM | ss.xpt |
| TR | Tumor/Lesion Results | Findings | One record per tumor measurement/assessment per visit per subject per assessor | Tabulation | STUDYID, USUBJID, TRTESTCD, TREVALID, VISITNUM | tr.xpt |
| TU | Tumor/Lesion Identification | Findings | One record per identified tumor per subject per assessor | Tabulation | STUDYID, USUBJID, TUEVALID, TULNKID | tu.xpt |
| UR | Urinary System Findings | Findings | One record per finding per location per visit per subject | Tabulation | STUDYID, USUBJID, VISITNUM, URTESTCD, URLOC, URLAT, URDIR | ur.xpt |
| VS | Vital Signs | Findings | One record per vital sign measurement per time point per visit per subject | Tabulation | STUDYID, USUBJID, VSTESTCD, VISITNUM, VSTPTREF, VSTPTNUM | vs.xpt |
| FA | Findings About Events or Interventions | Findings About | One record per finding, per object, per time point, per visit per subject | Tabulation | STUDYID, USUBJID, FATESTCD, FAOBJ, VISITNUM, FATPTREF, FATPTNUM | fa.xpt |
| SR | Skin Response | Findings About | One record per finding, per object, per time point, per visit per subject | Tabulation | STUDYID, USUBJID, SRTESTCD, SROBJ, VISITNUM, SRTPTREF, SRTPTNUM | sr.xpt |
| TA | Trial Arms | Trial Design | One record per planned Element per Arm | Tabulation | STUDYID, ARMCD, TAETORD | ta.xpt |
| TD | Trial Disease Assessments | Trial Design | One record per planned constant assessment period | Tabulation | STUDYID, TDORDER | td.xpt |
| TE | Trial Elements | Trial Design | One record per planned Element | Tabulation | STUDYID, ETCD | te.xpt |
| TI | Trial Inclusion/Exclusion Criteria | Trial Design | One record per I/E criterion | Tabulation | STUDYID, IETESTCD | ti.xpt |
| TM | Trial Disease Milestones | Trial Design | One record per Disease Milestone type | Tabulation | STUDYID, MIDSTYPE | tm.xpt |
| TS | Trial Summary | Trial Design | One record per trial summary parameter value | Tabulation | STUDYID, TSPARMCD, TSSEQ | ts.xpt |
| TV | Trial Visits | Trial Design | One record per planned Visit per Arm | Tabulation | STUDYID, ARM, VISIT | tv.xpt |
| RELREC | Related Records | Relationship | One record per related record, group of records or dataset | Tabulation | STUDYID, RDOMAIN, USUBJID, IDVAR, IDVARVAL, RELID | relrec.xpt |
| RELSPEC | Related Specimens | Relationship | One record per specimen identifier per subject | Tabulation | STUDYID, USUBJID, REFID | relspec.xpt |
| RELSUB | Related Subjects | Relationship | One record per relationship per related subject per subject | Tabulation | STUDYID, USUBJID, RSUBJID, SREL | relsub.xpt |
| SUPP-- | Supplemental Qualifiers for [domain name] | Relationship | One record per supplemental qualifier per related parent domain record(s) | Tabulation | STUDYID, RDOMAIN, USUBJID, IDVAR, IDVARVAL, QNAM | supp--.xpt |
| OI | Non-host Organism Identifiers | Study Reference | One record per taxon per non-host organism | Tabulation | NHOID, OISEQ | oi.xpt |

Separate Supplemental Qualifier datasets of the form supp--.xpt are required. See Section 8.4, Relating Non-standard Variable Values to a Parent Domain.

### 3.2.1.1 Primary Keys

The table in Section 3.2.1, Dataset-level Metadata, shows examples of what a sponsor might submit as variables that comprise the primary key for SDTM datasets. Because the purpose of the Keys column is to aid reviewers in understanding the structure of a dataset, sponsors should list all of the natural keys for the dataset. These keys should define uniqueness for records in a dataset, and may define a record sort order. The identified keys for each dataset should be consistent with the description of the dataset structure as described in the Define-XML document.

For all the general observation-class domains (and for some special-purpose domains), the --SEQ variable was created so that a unique record could be identified consistently across all of these domains via its use, along with STUDYID, USUBJID, and DOMAIN. In most domains, --SEQ will be a surrogate key for a set of variables that comprise the natural key. In certain instances, a supplemental qualifier (SUPP--) variable might also contribute to the natural key of a record for a particular domain. See Section 4.1.9, Assigning Natural Keys in the Metadata, for how this should be represented, and for additional information on keys.

**Definitions:**
- A **natural key** is a set of data (1 or more columns) that uniquely identifies an entity and distinguishes it from any other row in the table. The advantage of natural keys is that they exist already; one does not need to introduce a new, "unnatural" value to the data schema. One of the difficulties in choosing a natural key is that just about any natural key one can think of has the potential to change. Because they have business meaning, natural keys are effectively coupled to the business, and they may need to be reworked when business requirements change. An example of such a change in clinical trials data would be the addition of a position or location that becomes a key in a new study, but which was not collected in previous studies.
- A **surrogate key** is a single-part, artificially established identifier for a record. A surrogate key is immune to changes in business needs. In addition, the key depends on only 1 field, so it is compact. A common way of deriving surrogate key values is to assign integer values sequentially. The --SEQ variable in the SDTM datasets is an example of a surrogate key for most datasets; in some instances, however, --SEQ might be a part of a natural key as a replacement for what might have been a key (e.g., a repeat sequence number) in the sponsor's database.

### 3.2.1.2 CDISC Submission Value-level Metadata

In general, findings data models are closely related to normalized, relational data models in a vertical structure of 1 record per observation. Because general observation class data structures are fixed, sometimes information that might appear as columns in a more horizontal (denormalized) structure in presentations and reports will instead be represented as rows in an SDTM Findings structure. Because many different types of observations are all presented in the same structure, there is a need to provide additional metadata to describe expected properties that differentiate (e.g., hematology lab results from serum chemistry lab results in terms of data type, standard units, and other attributes).

**Example:** The Vital Signs (VS) data domain could contain subject records related to diastolic and systolic blood pressure, height, weight, and body mass index (BMI). These data are all submitted in the normalized SDTM Findings structure of 1 row per vital signs measurement. This means that there could be 5 records per subject (1 for each test or measurement) for a single visit or time point, with the parameter names stored in the Test Code/Name variables, and the parameter values stored in result variables. Because the unique test code/names could have different attributes (e.g., different origins, roles, definitions) there would be a need to provide value-level metadata for this information.

The value-level metadata should be provided as a separate section of the Define-XML document. For details on the CDISC Define-XML standard, see https://www.cdisc.org/standards/data-exchange/define-xml.

---

## 3.2.2 Conformance

Conformance with the SDTMIG domain models is minimally indicated by:

1. Following the complete metadata structure for data domains
2. Following SDTMIG domain models wherever applicable
3. Using SDTM-specified standard domain names and prefixes where applicable
4. Using SDTM-specified standard variable names
5. Using SDTM-specified data types for all variables
6. Following SDTM-specified controlled terminology and format guidelines for variables, when provided
7. Including all collected and relevant derived data in one of the standard domains, special-purpose datasets, or general observation class structures
8. Including all Required and Expected variables as columns in standard domains, and ensuring that all Required variables are populated
9. Ensuring that each record in a dataset includes the appropriate Identifier and Timing variables, as well as a Topic variable
10. Conforming to all business rules described in the CDISC Notes column and general and domain-specific assumptions
