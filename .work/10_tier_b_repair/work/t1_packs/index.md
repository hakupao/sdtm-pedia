# T1.2 分诊包索引

> 生成: `python3 -I .work/10_tier_b_repair/scripts/t1_pack.py` (输入 `work/triage_prefilter.jsonl`)
> 包 33 个 / 原子 1461 (含 manual 2). 每包整节 (节 > 80 才拆, 标 part). lane 间 owned KB 文件不相交 (脚本断言); `kb_context_readonly` 只读参考, 可跨 lane.
> 跨 lane 的只读参考文件引用: 34 个 (T1 只读无冲突; T2 批次表在 T1.4 定).

| lane | 包数 | 原子 | units |
|---|--:|--:|---|
| lane_A | 9 | 366 | chapters/ch01_introduction.md, domains/DM, domains/HO, domains/IE, domains/LB, domains/MH, domains/MI, domains/PC, domains/PP, domains/RELSUB, domains/RP, domains/RS, domains/TI, domains/TS, model/02_observation_classes.md |
| lane_B | 8 | 365 | domains/CE, domains/CM, domains/CP, domains/EX, domains/FA, domains/GF, domains/MS, domains/RE, domains/SM, domains/TA, domains/TU, domains/TV, model/04_associated_persons.md |
| lane_C | 8 | 365 | chapters/ch03_submitting_data.md, chapters/ch08_relationships.md, domains/AE, domains/BS, domains/DD, domains/EG, domains/IS, domains/NV, domains/OI, domains/SU, domains/TD, domains/TE, model/05_study_level_data.md |
| lane_D | 8 | 365 | VARIABLE_INDEX.md, chapters/ch02_fundamentals.md, chapters/ch04_general_assumptions.md, domains/BE, domains/CO, domains/CV, domains/DA, domains/FT, domains/MB, domains/ML, domains/RELSPEC, domains/TM, domains/TR, model/03_special_purpose_domains.md |

| pack | lane | 原子 | 节 (part) | PDF 页 | 预筛 suggest |
|---|---|--:|---|---|---|
| pack_001 | lane_A | 21 | §6.3.5.9.1 Pharmacokinetics Concentrations (PC); §6.3.5.9.3 Relating PP Records to PC Records | 270-278 | PRESENT:12, -:9 |
| pack_002 | lane_A | 62 | §6.3.5.9.3 Relating PP Records to PC Records — E | 281-283 | PRESENT:60, -:2 |
| pack_003 | lane_A | 22 | §6.3.5.9.3 Relating PP Records to PC Records — E; §6.3.5.9.2 [PP Examples] Example 1; §6.3.5.9.3 Relating PP Records to PC Records — E | 273-284 | PRESENT:17, -:3, VALUE_DIFF:2 |
| pack_004 | lane_A | 57 | §5.2 [Demographics (DM)]; §5.2 [DM – Examples] | 63-79 | -:21, PRESENT:20, IE_CAND:12, ATOM_ERR:3, RELOCATE:1 |
| pack_005 | lane_A | 45 | §1.4 [How to Read this Implementation Guide]; §1.4.1 [How to Read a Domain Specification]; §1.5 [Known Issues]; §1 [INTRODUCTION] | 4-11 | -:44, PRESENT:1 |
| pack_006 | lane_A | 41 | §6.3.5.8 Microscopic Findings (MI) | 263-267 | IE_CAND:38, -:2, PRESENT:1 |
| pack_007 | lane_A | 54 | §6.3.5.1 Generic Specimen-based Lab Findings Dom; §6.4.3 Variables Unique to Findings About; §6.2.5 Healthcare Encounters (HO) | 167-365 | -:42, IE_CAND:8, PRESENT:4 |
| pack_008 | lane_A | 59 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE); §6.3.9.3 Disease Response and Clin Classificatio; §6.3.9.3 Disease Response and Clin Classificatio; §6.3.5.6 Laboratory Test Results (LB); §6.2.6 Medical History (MH); §7.4.2.1 Use of Null Flavor | 172-426 | IE_CAND:42, -:10, PRESENT:4, RELOCATE:3 |
| pack_009 | lane_A | 5 | RELSUB – Description/Overview; §6.3.7.6 Reproductive System Findings (RP); §7.4.1 Trial Inclusion/Exclusion Criteria (TI) | 305-438 | PRESENT:3, -:2 |
| pack_010 | lane_B | 36 | §6.2.3 [Clinical Events (CE)] | 148-151 | IE_CAND:25, -:9, VALUE_DIFF:1, RELOCATE:1 |
| pack_011 | lane_B | 50 | §6.2.3 [Clinical Events] | 151-156 | -:39, PRESENT:11 |
| pack_012 | lane_B | 62 | §6.3.5.3 Cell Phenotype Findings (CP) | 199-221 | -:44, VALUE_DIFF:12, IE_CAND:4, PRESENT:2 |
| pack_013 | lane_B | 54 | §6.1.3.3 [Exposure/Exposure as Collected Example; §7.2 Experimental Design (TA and TE); §7.2.1 Trial Arms (TA) – Examples | 111-387 | -:36, PRESENT:17, VALUE_DIFF:1 |
| pack_014 | lane_B | 40 | §7.2.1 Trial Arms (TA) – Example 1; §7.2.1 Trial Arms (TA) – Example 4; §7.2.1 Trial Arms (TA) – Example 5; §7.2.1 Trial Arms (TA) – Example 6; §7.2.1 Trial Arms (TA) – Example 7; §7.2.1.1 Trial Arms Issues – Distinguishing Betw; §7.2.1.1 Trial Arms Issues – Subjects Not Assign | 387-403 | -:20, PRESENT:12, FIGURE:8 |
| pack_015 | lane_B | 35 | FA – Examples | 367-375 | PRESENT:20, -:11, VALUE_DIFF:4 |
| pack_016 | lane_B | 50 | §6.3.7.7 Respiratory System Findings (RE); §6.3.5.4 Genomics Findings (GF) | 220-311 | IE_CAND:27, -:18, PRESENT:2, FIGURE:2, RELOCATE:1 |
| pack_017 | lane_B | 38 | §5.4 [Subject Disease Milestones (SM)]; §6.1.2 [Concomitant/Prior Medications (CM)]; §6.3.5.7.2 Microbiology Susceptibility (MS); §7.3.1 Trial Visits (TV) – Description/Overview; §7.3.1 Trial Visits (TV) – Example 1; §7.3.1.1 Trial Visits Issues – Contingent Visits; §6.6 [Associated Persons Relationships]; TU – Description/Overview | 68-411 | IE_CAND:16, -:10, PRESENT:9, RELOCATE:1, ATOM_ERR:1, FIGURE:1 |
| pack_018 | lane_C | 41 | §6.2.1 [Adverse Events (AE)] (1/2) | 133-136 | IE_CAND:39, -:2 |
| pack_019 | lane_C | 41 | §6.2.1 [Adverse Events (AE)] (2/2) | 135-143 | IE_CAND:25, PRESENT:10, -:5, RELOCATE:1 |
| pack_020 | lane_C | 62 | §6.3.3 ECG Test Results (EG) | 185-193 | IE_CAND:48, PRESENT:8, -:5, VALUE_DIFF:1 |
| pack_021 | lane_C | 52 | §3.2.1 Dataset-level Metadata; §3.2.1.1 Primary Keys; §3.2.1 [Findings] | 17-22 | -:50, PRESENT:1, RELOCATE:1 |
| pack_022 | lane_C | 60 | §6.3.7.4 Nervous System Findings (NV); §9 [STUDY REFERENCES]; §9.1 Device Identifiers; §0 [TOC]; §5.1 [The Trial Design Model]; §5.1.1.2 Trial Arms; §5.1.3.2 Trial Repro Paths | 2-442 | IE_CAND:42, -:15, RELOCATE:2, PRESENT:1 |
| pack_023 | lane_C | 46 | §5.1.4.1 Trial Visits; §5.1.4.2 Trial Disease Assessments; §5.1.4.3 Trial Disease Milestones; §5.1.5 Trial Inclusion/Exclusion Criteria; §5.1.6 Trial Summary Information; §6.3.2 Death Details (DD) | 56-186 | -:27, IE_CAND:18, RELOCATE:1 |
| pack_024 | lane_C | 58 | §6.3.5.5 Immunogenicity Specimen Assessments (IS; §8 [REPRESENTING RELATIONSHIPS AND DATA]; §8.4.3 SUPP-- Examples; §6.1 [Related Records Dataset]; §7.2.2 Trial Elements (TE) – Description/Overvie; §7.2.2 Trial Elements (TE) – Assumptions; §7.2.2.1 Trial Elements Issues – Transitions Bet; §7.5 How to Model the Design of a Clinical Trial; §9.2 OI – Description/Overview; §9.2 OI – Assumptions | 64-444 | PRESENT:29, -:25, VALUE_DIFF:3, RELOCATE:1 |
| pack_025 | lane_C | 5 | §6.1.6 [Substance Use (SU)]; §6.3.5.2 Biospecimen Findings (BS) | 129-199 | -:3, RELOCATE:1, PRESENT:1 |
| pack_026 | lane_D | 49 | §2.1 Observations and Variables; §2.2 Datasets and Domains; §2.3 The General Observation Classes; §2.4 Datasets Other than General Observation Cla; §2.5 The SDTM Standard Domain Models; §2.6 Creating a New Domain | 11-16 | -:41, PRESENT:5, RELOCATE:3 |
| pack_027 | lane_D | 54 | §2.7 SDTM Variables Not Allowed in the SDTMIG; §6.3.7 Morphology/Physiology Domains; §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF T; §4.1.5 [SDTM Core Designations]; §4.2.3 [Use of "Subject" and USUBJID]; §4.2.5 [Convention for Missing Values]; §4.2.7.1 "Specify" Values for Non-result Qualifi; §4.4.1 Formats for Date/Time Variables; §4.4.3.2 [Interval with Uncertainty]; §4.4.4 [Use of the Study Day Variables]; §4.4.5 [Clinical Encounters and Visits] | 8-286 | -:42, PRESENT:7, RELOCATE:5 |
| pack_028 | lane_D | 48 | §4.4.7 [Use of Relative Timing Variables]; §4.4.10 [Representing Time Points]; §4.5.3.1 [Test Name (--TEST) Greater than 40 Cha; §4.5.3.2 [Text Strings Greater than 200 Characte; §4.5.4 [Evaluators in the Interventions and Even; §6.4.2 Naming Findings About Domains | 43-365 | -:39, ATOM_ERR:4, PRESENT:4, FIGURE:1 |
| pack_029 | lane_D | 47 | §6.3.7.2 Cardiovascular System Findings (CV) | 286-290 | IE_CAND:43, PRESENT:2, -:1, RELOCATE:1 |
| pack_030 | lane_D | 42 | §6.1.4 [Meal Data (ML)] | 121-125 | IE_CAND:34, -:4, PRESENT:4 |
| pack_031 | lane_D | 37 | §6.3.5.7.3 Microbiology Specimen/Microbiology Su; §6.3.5.7 Microbiology Domains | 258-264 | PRESENT:20, -:11, VALUE_DIFF:6 |
| pack_032 | lane_D | 50 | §6.3.12.3 Tumor Identification/Tumor Results Exa; §3.2.3.1 [Subject Elements]; §3.2.3.2 [Subject Repro Stages] | 46-357 | -:31, VALUE_DIFF:18, PRESENT:1 |
| pack_033 | lane_D | 38 | §6.2.2 [Biospecimen Events (BE)]; §6.3.9 Questionnaires, Ratings, and Scales (QRS); §6.3.9.1 Functional Tests (FT); §5.3 [Subject Elements]; §6.3.1 Product Accountability (DA); RELSPEC – Examples; §5.1 [Comments (CO)]; §7.3.3 Trial Disease Milestones (TM) | 61-441 | IE_CAND:19, -:9, PRESENT:8, RELOCATE:1, ATOM_ERR:1 |
