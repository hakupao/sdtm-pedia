# SDTM IG v3.4 Datasets Reference

**Version:** SDTM IG v3.4

## Overview

This document contains all SDTM datasets organized by class.

## Events

### AE - Adverse Events

| Property | Value |
|---|---|
| **Dataset Code** | `AE` |
| **Label** | Adverse Events |
| **Structure** | One record per adverse event per subject |

### BE - Biospecimen Events

| Property | Value |
|---|---|
| **Dataset Code** | `BE` |
| **Label** | Biospecimen Events |
| **Structure** | One record per instance per biospecimen event per biospecimen identifier per subject |

### CE - Clinical Events

| Property | Value |
|---|---|
| **Dataset Code** | `CE` |
| **Label** | Clinical Events |
| **Structure** | One record per event per subject |

### DS - Disposition

| Property | Value |
|---|---|
| **Dataset Code** | `DS` |
| **Label** | Disposition |
| **Structure** | One record per disposition status or protocol milestone per subject |

### DV - Protocol Deviations

| Property | Value |
|---|---|
| **Dataset Code** | `DV` |
| **Label** | Protocol Deviations |
| **Structure** | One record per protocol deviation per subject |

### HO - Healthcare Encounters

| Property | Value |
|---|---|
| **Dataset Code** | `HO` |
| **Label** | Healthcare Encounters |
| **Structure** | One record per healthcare encounter per subject |

### MH - Medical History

| Property | Value |
|---|---|
| **Dataset Code** | `MH` |
| **Label** | Medical History |
| **Structure** | One record per medical history event per subject |

## Findings

### BS - Biospecimen Findings

| Property | Value |
|---|---|
| **Dataset Code** | `BS` |
| **Label** | Biospecimen Findings |
| **Structure** | One record per measurement per biospecimen identifier per subject |

### CP - Cell Phenotype Findings

| Property | Value |
|---|---|
| **Dataset Code** | `CP` |
| **Label** | Cell Phenotype Findings |
| **Structure** | One record per test per specimen per timepoint per visit per subject |

### CV - Cardiovascular System Findings

| Property | Value |
|---|---|
| **Dataset Code** | `CV` |
| **Label** | Cardiovascular System Findings |
| **Structure** | One record per finding or result per time point per visit per subject |

### DA - Product Accountability

| Property | Value |
|---|---|
| **Dataset Code** | `DA` |
| **Label** | Product Accountability |
| **Structure** | One record per product accountability finding per subject |

### DD - Death Details

| Property | Value |
|---|---|
| **Dataset Code** | `DD` |
| **Label** | Death Details |
| **Structure** | One record per finding per subject |

### EG - ECG Test Results

| Property | Value |
|---|---|
| **Dataset Code** | `EG` |
| **Label** | ECG Test Results |
| **Structure** | One record per ECG observation per replicate per time point or one record per ECG observation per beat per visit per subject |

### FT - Functional Tests

| Property | Value |
|---|---|
| **Dataset Code** | `FT` |
| **Label** | Functional Tests |
| **Structure** | One record per Functional Test finding per time point per visit per subject |

### GF - Genomics Findings

| Property | Value |
|---|---|
| **Dataset Code** | `GF` |
| **Label** | Genomics Findings |
| **Structure** | One record per finding per observation per biospecimen per subject |

### IE - Inclusion/Exclusion Criteria Not Met

| Property | Value |
|---|---|
| **Dataset Code** | `IE` |
| **Label** | Inclusion/Exclusion Criteria Not Met |
| **Structure** | One record per inclusion/exclusion criterion not met per subject |

### IS - Immunogenicity Specimen Assessments

| Property | Value |
|---|---|
| **Dataset Code** | `IS` |
| **Label** | Immunogenicity Specimen Assessments |
| **Structure** | One record per test per visit per subject |

### LB - Laboratory Test Results

| Property | Value |
|---|---|
| **Dataset Code** | `LB` |
| **Label** | Laboratory Test Results |
| **Structure** | One record per lab test per time point per visit per subject |

### MB - Microbiology Specimen

| Property | Value |
|---|---|
| **Dataset Code** | `MB` |
| **Label** | Microbiology Specimen |
| **Structure** | One record per microbiology specimen finding per time point per visit per subject |

### MI - Microscopic Findings

| Property | Value |
|---|---|
| **Dataset Code** | `MI` |
| **Label** | Microscopic Findings |
| **Structure** | One record per finding per specimen per subject |

### MK - Musculoskeletal System Findings

| Property | Value |
|---|---|
| **Dataset Code** | `MK` |
| **Label** | Musculoskeletal System Findings |
| **Structure** | One record per assessment per visit per subject |

### MS - Microbiology Susceptibility

| Property | Value |
|---|---|
| **Dataset Code** | `MS` |
| **Label** | Microbiology Susceptibility |
| **Structure** | One record per microbiology susceptibility test (or other organism-related finding) per organism found in MB |

### NV - Nervous System Findings

| Property | Value |
|---|---|
| **Dataset Code** | `NV` |
| **Label** | Nervous System Findings |
| **Structure** | One record per finding per location per time point per visit per subject |

### OE - Ophthalmic Examinations

| Property | Value |
|---|---|
| **Dataset Code** | `OE` |
| **Label** | Ophthalmic Examinations |
| **Structure** | One record per ophthalmic finding per method per location, per time point per visit per subject |

### PC - Pharmacokinetics Concentrations

| Property | Value |
|---|---|
| **Dataset Code** | `PC` |
| **Label** | Pharmacokinetics Concentrations |
| **Structure** | One record per sample characteristic or time-point concentration per reference time point or per analyte per subject |

### PE - Physical Examination

| Property | Value |
|---|---|
| **Dataset Code** | `PE` |
| **Label** | Physical Examination |
| **Structure** | One record per body system or abnormality per visit per subject |

### PP - Pharmacokinetics Parameters

| Property | Value |
|---|---|
| **Dataset Code** | `PP` |
| **Label** | Pharmacokinetics Parameters |
| **Structure** | One record per PK parameter per time-concentration profile per modeling method per subject |

### QS - Questionnaires

| Property | Value |
|---|---|
| **Dataset Code** | `QS` |
| **Label** | Questionnaires |
| **Structure** | One record per questionnaire per question per time point per visit per subject |

### RE - Respiratory System Findings

| Property | Value |
|---|---|
| **Dataset Code** | `RE` |
| **Label** | Respiratory System Findings |
| **Structure** | One record per finding or result per time point per visit per subject |

### RP - Reproductive System Findings

| Property | Value |
|---|---|
| **Dataset Code** | `RP` |
| **Label** | Reproductive System Findings |
| **Structure** | One record per finding or result per time point per visit per subject |

### RS - Disease Response and Clin Classification

| Property | Value |
|---|---|
| **Dataset Code** | `RS` |
| **Label** | Disease Response and Clin Classification |
| **Structure** | One record per response assessment or clinical classification assessment per time point per visit per subject per assessor per medical evaluator |

### SC - Subject Characteristics

| Property | Value |
|---|---|
| **Dataset Code** | `SC` |
| **Label** | Subject Characteristics |
| **Structure** | One record per characteristic per visit per subject. |

### SS - Subject Status

| Property | Value |
|---|---|
| **Dataset Code** | `SS` |
| **Label** | Subject Status |
| **Structure** | One record per status per visit per subject |

### TR - Tumor/Lesion Results

| Property | Value |
|---|---|
| **Dataset Code** | `TR` |
| **Label** | Tumor/Lesion Results |
| **Structure** | One record per tumor measurement/assessment per visit per subject per assessor |

### TU - Tumor/Lesion Identification

| Property | Value |
|---|---|
| **Dataset Code** | `TU` |
| **Label** | Tumor/Lesion Identification |
| **Structure** | One record per identified tumor per subject per assessor |

### UR - Urinary System Findings

| Property | Value |
|---|---|
| **Dataset Code** | `UR` |
| **Label** | Urinary System Findings |
| **Structure** | One record per finding per location per per visit per subject |

### VS - Vital Signs

| Property | Value |
|---|---|
| **Dataset Code** | `VS` |
| **Label** | Vital Signs |
| **Structure** | One record per vital sign measurement per time point per visit per subject |

## Findings About

### FA - Findings About Events or Interventions

| Property | Value |
|---|---|
| **Dataset Code** | `FA` |
| **Label** | Findings About Events or Interventions |
| **Structure** | One record per finding, per object, per time point, per visit per subject |

### SR - Skin Response

| Property | Value |
|---|---|
| **Dataset Code** | `SR` |
| **Label** | Skin Response |
| **Structure** | One record per finding, per object, per time point, per visit per subject |

## Interventions

### AG - Procedure Agents

| Property | Value |
|---|---|
| **Dataset Code** | `AG` |
| **Label** | Procedure Agents |
| **Structure** | One record per recorded intervention occurrence per subject |

### CM - Concomitant/Prior Medications

| Property | Value |
|---|---|
| **Dataset Code** | `CM` |
| **Label** | Concomitant/Prior Medications |
| **Structure** | One record per recorded intervention occurrence or constant-dosing interval per subject |

### EC - Exposure as Collected

| Property | Value |
|---|---|
| **Dataset Code** | `EC` |
| **Label** | Exposure as Collected |
| **Structure** | One record per protocol-specified study treatment, collected-dosing interval, per subject, per mood |

### EX - Exposure

| Property | Value |
|---|---|
| **Dataset Code** | `EX` |
| **Label** | Exposure |
| **Structure** | One record per protocol-specified study treatment, constant-dosing interval, per subject |

### ML - Meal Data

| Property | Value |
|---|---|
| **Dataset Code** | `ML` |
| **Label** | Meal Data |
| **Structure** | One record per food product occurrence or constant intake interval per subject |

### PR - Procedures

| Property | Value |
|---|---|
| **Dataset Code** | `PR` |
| **Label** | Procedures |
| **Structure** | One record per recorded procedure per occurrence per subject |

### SU - Substance Use

| Property | Value |
|---|---|
| **Dataset Code** | `SU` |
| **Label** | Substance Use |
| **Structure** | One record per substance type per reported occurrence per subject |

## Relationship

### RELREC - Related Records

| Property | Value |
|---|---|
| **Dataset Code** | `RELREC` |
| **Label** | Related Records |
| **Structure** | One record per related record, group of records or dataset |

### RELSPEC - Related Specimens

| Property | Value |
|---|---|
| **Dataset Code** | `RELSPEC` |
| **Label** | Related Specimens |
| **Structure** | One record per specimen identifier per subject |

### RELSUB - Related Subjects

| Property | Value |
|---|---|
| **Dataset Code** | `RELSUB` |
| **Label** | Related Subjects |
| **Structure** | One record per relationship per related subject per subject |

### SUPPQUAL - Supplemental Qualifiers for [domain name]

| Property | Value |
|---|---|
| **Dataset Code** | `SUPPQUAL` |
| **Label** | Supplemental Qualifiers for [domain name] |
| **Structure** | One record per supplemental qualifier per related parent domain record(s) |

## Special-Purpose

### CO - Comments

| Property | Value |
|---|---|
| **Dataset Code** | `CO` |
| **Label** | Comments |
| **Structure** | One record per comment per subject |

### DM - Demographics

| Property | Value |
|---|---|
| **Dataset Code** | `DM` |
| **Label** | Demographics |
| **Structure** | One record per subject |

### SE - Subject Elements

| Property | Value |
|---|---|
| **Dataset Code** | `SE` |
| **Label** | Subject Elements |
| **Structure** | One record per actual Element per subject |

### SM - Subject Disease Milestones

| Property | Value |
|---|---|
| **Dataset Code** | `SM` |
| **Label** | Subject Disease Milestones |
| **Structure** | One record per Disease Milestone per subject |

### SV - Subject Visits

| Property | Value |
|---|---|
| **Dataset Code** | `SV` |
| **Label** | Subject Visits |
| **Structure** | One record per actual or planned visit per subject |

## Study Reference

### OI - Non-host Organism Identifiers

| Property | Value |
|---|---|
| **Dataset Code** | `OI` |
| **Label** | Non-host Organism Identifiers |
| **Structure** | One record per taxon per non-host organism |

## Trial Design

### TA - Trial Arms

| Property | Value |
|---|---|
| **Dataset Code** | `TA` |
| **Label** | Trial Arms |
| **Structure** | One record per planned Element per Arm |

### TD - Trial Disease Assessments

| Property | Value |
|---|---|
| **Dataset Code** | `TD` |
| **Label** | Trial Disease Assessments |
| **Structure** | One record per planned constant assessment period |

### TE - Trial Elements

| Property | Value |
|---|---|
| **Dataset Code** | `TE` |
| **Label** | Trial Elements |
| **Structure** | One record per planned Element |

### TI - Trial Inclusion/Exclusion Criteria

| Property | Value |
|---|---|
| **Dataset Code** | `TI` |
| **Label** | Trial Inclusion/Exclusion Criteria |
| **Structure** | One record per I/E criterion |

### TM - Trial Disease Milestones

| Property | Value |
|---|---|
| **Dataset Code** | `TM` |
| **Label** | Trial Disease Milestones |
| **Structure** | One record per Disease Milestone type |

### TS - Trial Summary

| Property | Value |
|---|---|
| **Dataset Code** | `TS` |
| **Label** | Trial Summary |
| **Structure** | One record per trial summary parameter value |

### TV - Trial Visits

| Property | Value |
|---|---|
| **Dataset Code** | `TV` |
| **Label** | Trial Visits |
| **Structure** | One record per planned Visit per Arm |

