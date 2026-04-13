# TS — Examples

## Example 1

This example shows a subset of published controlled terminology parameters and the relationship of values across response variables TSVAL, TSVALNF, TSVALCD, TSVCDREF, and TSVCDVER.

**ts.xpt**

| Row | STUDYID | DOMAIN | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL | TSVALNF | TSVALCD | TSVCDREF | TSVCDVER |
|-----|---------|--------|-------|---------|----------|--------|-------|---------|---------|----------|----------|
| 1 | XYZ | TS | 1 | | ADDON | Added on to Existing Treatments | Y | | C49488 | CDISC CT | 2011-06-10 |
| 2 | XYZ | TS | 1 | | AGEMAX | Planned Maximum Age of Subjects | P70Y | | | ISO 8601 | |
| 3 | XYZ | TS | 1 | | AGEMIN | Planned Minimum Age of Subjects | P18M | | | ISO 8601 | |
| 4 | XYZ | TS | 1 | | LENGTH | Trial Length | P3M | | | ISO 8601 | |
| 5 | XYZ | TS | 1 | | PLANSUB | Planned Number of Subjects | 300 | | | | |
| 6 | XYZ | TS | 1 | | RANDOM | Trial is Randomized | Y | | C49488 | CDISC CT | 2011-06-10 |
| 7 | XYZ | TS | 1 | | SEXPOP | Sex of Participants | BOTH | | C49636 | CDISC CT | 2011-06-10 |
| 8 | XYZ | TS | 1 | | STOPRULE | Study Stop Rules | INTERIM ANALYSIS FOR FUTILITY | | | | |
| 9 | XYZ | TS | 1 | | TBLIND | Trial Blinding Schema | DOUBLE BLIND | | C15228 | CDISC CT | 2011-06-10 |
| 10 | XYZ | TS | 1 | | TCNTRL | Control Type | PLACEBO | | C49648 | CDISC CT | 2011-06-10 |
| 11 | XYZ | TS | 1 | | TDIGRP | Diagnosis Group | Neurofibromatosis Syndrome (Disorder) | | 19133005 | SNOMED | 2011-03 |
| 12 | XYZ | TS | 1 | | INDIC | Trial Disease/Condition Indication | Tonic-Clonic Epilepsy (Disorder) | | 352818000 | SNOMED | 2011-03 |
| 13 | XYZ | TS | 1 | | TINDTP | Trial Intent Type | TREATMENT | | C49656 | CDISC CT | 2011-06-10 |
| 14 | XYZ | TS | 1 | | TITLE | Trial Title | A 24 Week Study of Oral Gabapentin vs. Placebo as add-on Treatment to Phenytoin in Subjects with Neurofibromatosis Epilepsy due to Neurofibromatosis | | | | |
| 15 | XYZ | TS | 1 | | TPHASE | Trial Phase Classification | Phase II Trial | | C15601 | CDISC CT | 2011-06-10 |
| 16 | XYZ | TS | 1 | | TTYPE | Trial Type | EFFICACY | | C49666 | CDISC CT | 2011-06-10 |
| 17 | XYZ | TS | 2 | | TTYPE | Trial Type | SAFETY | | C49667 | CDISC CT | 2011-06-10 |
| 18 | XYZ | TS | 1 | | CURTRT | Current Therapy or Treatment | Phenytoin | | 6158TKW0C5 | UNII | |
| 19 | XYZ | TS | 1 | | OBJPRIM | Trial Primary Objective | Reduction in the 3-month seizure frequency from baseline | | | | |
| 20 | XYZ | TS | 1 | | OBJSEC | Trial Secondary Objective | Percent reduction in the 3-month seizure frequency from baseline | | | | |
| 21 | XYZ | TS | 2 | | OBJSEC | Trial Secondary Objective | Reduction in the 3-month tonic-clonic seizure frequency from baseline | | | | |
| 22 | XYZ | TS | 1 | | SPONSOR | Clinical Study Sponsor | Pharmaco | | 123456789 | D-U-N-S NUMBER | |
| 23 | XYZ | TS | 1 | | TRT | Investigational Therapy or Treatment | Gabapentin | | 6CW7F3G59X | UNII | |
| 24 | XYZ | TS | 1 | | RANDQT | Randomization Quotient | 0.67 | | | | |
| 25 | XYZ | TS | 1 | | STRATFCT | Stratification Factor | SEX | | | | |
| 26 | XYZ | TS | 1 | | REGID | Registry Identifier | NCT123456789 | | NCT123456789 | ClinicalTrials.gov | |
| 27 | XYZ | TS | 2 | | REGID | Registry Identifier | XXYYZZ456 | | XXYYZZ456 | EudraCT | |
| 28 | XYZ | TS | 1 | | OUTMSPRI | Primary Outcome Measure | SEIZURE FREQUENCY | | | | |
| 29 | XYZ | TS | 1 | | OUTMSSEC | Secondary Outcome Measure | SEIZURE FREQUENCY | | | | |
| 30 | XYZ | TS | 2 | | OUTMSSEC | Secondary Outcome Measure | SEIZURE DURATION | | | | |
| 31 | XYZ | TS | 1 | | OUTMSEXP | Exploratory Outcome Measure | SEIZURE INTENSITY | | | | |
| 32 | XYZ | TS | 1 | | PCLAS | Pharmacological Class | Anti-epileptic Agent | | N0000175753 | MED-RT | |
| 33 | XYZ | TS | 1 | | FCNTRY | Planned Country of Investigational Sites | USA | | | ISO 3166-1 Alpha-3 | |
| 34 | XYZ | TS | 2 | | FCNTRY | Planned Country of Investigational Sites | CAN | | | ISO 3166-1 Alpha-3 | |
| 35 | XYZ | TS | 3 | | FCNTRY | Planned Country of Investigational Sites | MEX | | | ISO 3166-1 Alpha-3 | |
| 36 | XYZ | TS | 1 | | ADAPT | Adaptive Design | N | | C49487 | CDISC CT | 2011-06-10 |
| 37 | XYZ | TS | 1 | PA | DCUTDTC | Data Cutoff Date | 2010-04-10 | | | | |
| 38 | XYZ | TS | 1 | PA | DCUTDESC | Data Cutoff Description | PRIMARY ANALYSIS | | | | |
| 39 | XYZ | TS | 1 | | INTMODEL | Intervention Model | PARALLEL | | C82639 | CDISC CT | 2011-06-10 |
| 40 | XYZ | TS | 1 | | NARMS | Planned Number of Arms | 3 | | | | |
| 41 | XYZ | TS | 1 | | STYPE | Study Type | INTERVENTIONAL | | C98388 | CDISC CT | 2011-06-10 |
| 42 | XYZ | TS | 1 | | INTTYPE | Intervention Type | DRUG | | C1909 | CDISC CT | 2011-06-10 |
| 43 | XYZ | TS | 1 | | SSTDTC | Study Start Date | 2009-03-11 | | | ISO 8601 | |
| 44 | XYZ | TS | 1 | | SENDTC | Study End Date | 2011-04-01 | | | ISO 8601 | |
| 45 | XYZ | TS | 1 | | ACTSUB | Actual Number of Subjects | 304 | | | | |
| 46 | XYZ | TS | 1 | | HLTSUBJI | Healthy Subject Indicator | N | | C49487 | CDISC CT | 2011-06-10 |
| 47 | XYZ | TS | 1 | | SDMDUR | Stable Disease Minimum Duration | P3W | | | ISO 8601 | |
| 48 | XYZ | TS | 1 | | CRMDUR | Confirmed Response Minimum Duration | P28D | | | ISO 8601 | |

## Example 2

This example shows the relationship between parameters involving diagnosis and indication. Only selected trial summary parameters are included.

**Row 1:** Shows the trial title.

**Row 2:** Shows that subjects in this trial have a diagnosis of diabetes.

**Rows 3-4:** Show the conditions with the intervention in the trial are intended to address. The 2 rows for the same parameter are differentiated by their TSSEQ values.

**Row 5:** Shows that the intent of this trial is prevention of the conditions represented using the parameter "Trial Indication".

**ts.xpt**

| Row | STUDYID | DOMAIN | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL | TSVALNF | TSVALCD | TSVCDREF | TSVCDVER |
|-----|---------|--------|-------|---------|----------|--------|-------|---------|---------|----------|----------|
| 1 | XYZ | TS | 1 | | TITLE | Trial Type | A Study Comparing Cardiovascular Effects of Ticagrelor Versus Placebo in Patients With Type 2 Diabetes Mellitus (THEMIS) | | | | |
| 2 | XYZ | TS | 1 | | TDIGRP | Diagnosis Group | Diabetes mellitus type 2 | | 44054006 | SNOMED | 2017-03 |
| 3 | XYZ | TS | 1 | | INDIC | Trial Indication | Cardiac infarction | | 22298006 | SNOMED | 2017-03 |
| 4 | XYZ | TS | 2 | | INDIC | Trial Indication | Cerebrovascular accident | | 230690007 | SNOMED | 2017-01 |
| 5 | XYZ | TS | 1 | | TINDTP | Trial Intent Type | PREVENTION | | C49657 | CDISC CT | 2017-03-01 |

## Example 3

This example shows how to implement the null flavor in TSVALNF when the value in TSVAL is missing. Note that when TSVAL is null, TSVALCD is also null, and no code system is specified in TSVCDREF and TSVCDVER.

**Row 1:** Shows that there was no upper limit on planned age of subjects, as indicated by TSVALNF="PINF" (the null flavor that means "positive infinity").

**Row 2:** Shows that trial phase classification is not applicable, as indicated by TSVALNF="NA".

**ts.xpt**

| Row | STUDYID | DOMAIN | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL | TSVALNF | TSVALCD | TSVCDREF | TSVCDVER |
|-----|---------|--------|-------|---------|----------|--------|-------|---------|---------|----------|----------|
| 1 | XYZ | TS | 1 | | AGEMAX | Planned Maximum Age of Subjects | | PINF | | | |
| 2 | XYZ | TS | 1 | | TPHASE | Trial Phase Classification | | NA | | | |

## Example 4

This example uses TSGRPID to group parameter values describing specific study parts (e.g., PHASE 1B, PHASE 3) and specific study treatments (e.g., DRUG X, DRUG Z).

**Rows 1-6:** Show parameters and values that apply to the whole trial (i.e., both Phase 1B and Phase 3 parts of the trial). TSGRPID is null for this set of parameters.

**Rows 7-17:** Show parameters and values that describe the Phase 1B part of the trial. TSGRPID is populated with a value of "PHASE 1B" for this set of parameters.

**Rows 18-29:** Show parameters and values that describe the Phase 3 part of the trial. TSGRPID is populated with a value of "PHASE 3" for this set of parameters.

**Rows 30-33:** Show parameters and values that describe details about 1 of the treatments planned in the trial. TSGRPID="DRUG X" for this set of parameters.

**Rows 34-37:** Show parameters and values that describe details about 1 of the treatments planned in the trial. TSGRPID="DRUG Z" for this set of parameters.

**ts.xpt**

| Row | STUDYID | DOMAIN | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL | TSVALNF | TSVALCD | TSVCDREF | TSVCDVER |
|-----|---------|--------|-------|---------|----------|--------|-------|---------|---------|----------|----------|
| 1 | ABC123 | TS | 1 | | TITLE | Trial Title | A Phase 1b/3, Multicenter Trial of Drug Z in Combination with Drug X for Treatment of Melanoma | | | | |
| 2 | ABC123 | TS | 1 | | INDIC | Trial Indication | Malignant melanoma | | 372244006 | SNOMED | 2018-09-01 |
| 3 | ABC123 | TS | 1 | | SEXPOP | Sex of Participants | BOTH | | C49636 | CDISC CT | 2018-12-21 |
| 4 | ABC123 | TS | 1 | | AGEMIN | Planned Minimum Age of Subjects | P18Y | | | ISO 8601 | |
| 5 | ABC123 | TS | 1 | | AGEMAX | Planned Maximum Age of Subjects | | PINF | | | |
| 6 | ABC123 | TS | 1 | | HLTSUBJI | Healthy Subject Indicator | N | | C49487 | CDISC CT | 2018-12-21 |
| 7 | ABC123 | TS | 1 | PHASE 1B | TPHASE | Trial Phase Classification | | | | | |
| 8 | ABC123 | TS | 1 | PHASE 1B | TBLIND | Trial Blinding Schema | OPEN LABEL | | C49659 | CDISC CT | 2018-12-21 |
| 9 | ABC123 | TS | 1 | PHASE 1B | TCNTRL | Control Type | NONE | | C41132 | CDISC CT | 2018-12-21 |
| 10 | ABC123 | TS | 1 | PHASE 1B | TTYPE | Trial Type | SAFETY | | C49667 | CDISC CT | 2018-12-21 |
| 11 | ABC123 | TS | 1 | PHASE 1B | INTMODEL | Intervention Model | SINGLE GROUP | | C82640 | CDISC CT | 2018-12-21 |
| 12 | ABC123 | TS | 1 | PHASE 1B | NARMS | Planned Number of Arms | 1 | | | | |
| 13 | ABC123 | TS | 1 | PHASE 1B | PLANSUB | Planned Number of Subjects | 30 | | | | |
| 14 | ABC123 | TS | 1 | PHASE 1B | RANDOM | Trial is Randomized | N | | C49487 | CDISC CT | 2018-12-21 |
| 15 | ABC123 | TS | 1 | PHASE 1B | OBJPRIM | Trial Primary Objective | To evaluate the safety, as assessed by incidence of dose limiting toxicity, of combination therapy (Drug X + Drug Z) | | | | |
| 16 | ABC123 | TS | 1 | PHASE 1B | OUTMEAS | Primary Outcome Measure | Incidence of dose limiting toxicities | | | | |
| 17 | ABC123 | TS | 1 | PHASE 1B | COMPTRT | Comparative Treatment | | NA | | | |
| 18 | ABC123 | TS | 1 | PHASE 3 | TPHASE | Trial Phase Classification | PHASE III TRIAL | | C15602 | CDISC CT | 2018-12-21 |
| 19 | ABC123 | TS | 1 | PHASE 3 | TBLIND | Trial Blinding Schema | DOUBLE BLIND | | C15228 | CDISC CT | 2018-12-21 |
| 20 | ABC123 | TS | 1 | PHASE 3 | TCNTRL | Control Type | PLACEBO | | C49648 | CDISC CT | 2018-12-21 |
| 21 | ABC123 | TS | 1 | PHASE 3 | TTYPE | Trial Type | EFFICACY | | C49666 | CDISC CT | 2018-12-21 |
| 22 | ABC123 | TS | 1 | PHASE 3 | INTMODEL | Intervention Model | PARALLEL | | C82639 | CDISC CT | 2018-12-21 |
| 23 | ABC123 | TS | 1 | PHASE 3 | NARMS | Planned Number of Arms | 2 | | | | |
| 24 | ABC123 | TS | 1 | PHASE 3 | PLANSUB | Planned Number of Subjects | 500 | | | | |
| 25 | ABC123 | TS | 1 | PHASE 3 | RANDOM | Trial is Randomized | Y | | C49488 | CDISC CT | 2018-12-21 |
| 26 | ABC123 | TS | 1 | PHASE 3 | RANDQT | Randomization Quotient | 0.5 | | | | |
| 27 | ABC123 | TS | 1 | PHASE 3 | OBJPRIM | Trial Primary Objective | To evaluate the efficacy of combination therapy (Drug X + Drug Z) versus monotherapy (Drug X + Placebo), as assessed by progression-free survival using RECIST 1.1 | | | | |
| 28 | ABC123 | TS | 1 | PHASE 3 | OUTMEAS | Primary Outcome Measure | Progression Free Survival (response evaluation by blinded central review using RECIST 1.1) | | | | |
| 29 | ABC123 | TS | 1 | PHASE 3 | COMPTRT | Comparative Treatment | DRUG X | | | | |
| 30 | ABC123 | TS | 1 | DRUG X | DOSE | Dose per Administration | 200 | | | | |
| 31 | ABC123 | TS | 1 | DRUG X | DOSU | Dose Units | mg | | C28253 | CDISC CT | 2018-12-21 |
| 32 | ABC123 | TS | 1 | DRUG X | DOSFRQ | Dosing Frequency | EVERY WEEK | | C67069 | CDISC CT | 2018-12-21 |
| 33 | ABC123 | TS | 1 | DRUG X | ROUTE | Route of Administration | ORAL | | C38288 | CDISC CT | 2018-12-21 |
| 34 | ABC123 | TS | 1 | DRUG Z | DOSE | Dose per Administration | 10000 | | | | |
| 35 | ABC123 | TS | 1 | DRUG Z | DOSU | Dose Units | PFU | | C67264 | CDISC CT | 2018-12-21 |
| 36 | ABC123 | TS | 1 | DRUG Z | DOSFRQ | Dosing Frequency | EVERY 2 WEEKS | | C71127 | CDISC CT | 2018-12-21 |
| 37 | ABC123 | TS | 1 | DRUG Z | ROUTE | Route of Administration | INTRATUMOR | | C38269 | CDISC CT | 2018-12-21 |
