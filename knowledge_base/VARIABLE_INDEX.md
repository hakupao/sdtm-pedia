# SDTM Variable Index

> 自动生成，勿手动编辑 | 生成日期: 2026-04-16
> 唯一变量数: 1523 | 条目总数: 1917 | 覆盖域: 63

## 使用说明

查询变量时，在本文件搜索变量名即可找到它出现在哪些 domain、属于什么角色/类型/核心程度。

- **通用变量**（出现在 2+ 个域）：表头标注出现域数，域列表用逗号分隔
- **领域专属变量**（仅 1 个域）：按域分组，直接标注所属域
- **CT 交叉引用**：按 CDISC Controlled Terminology Code 分组，列出所有引用该 CT 的变量

---

## 一、通用变量（出现在 2+ 个域，共 24 个）

| 变量名 | 域数 | 出现的域 | Label | Type | Role | Core |
|--------|------|---------|-------|------|------|------|
| STUDYID | 63 | 所有域 | Study Identifier | Char | Identifier | Req |
| DOMAIN | 59 | 除 RELREC, RELSPEC, RELSUB, SUPPQUAL 外所有域 | Domain Abbreviation | Char | Identifier | Req |
| USUBJID | 55 | 除 OI, TA, TD, TE, TI, TM, TS, TV 外所有域 | Unique Subject Identifier | Char | Identifier | Req* |
| EPOCH | 44 | AE, AG, CE, CM, CP, CV, DA, DS, DV, EC, EG, EX, FA, FT, HO, IE, IS, LB, MB, MH, MI, MK, ML, MS, NV, OE, PC, PE, PP, PR, QS, RE, RP, RS, SC, SE, SR, SS, SU, TA, TR, TU, UR, VS | Epoch | Char | Timing | Perm* |
| TAETORD | 43 | AE, AG, CE, CM, CP, CV, DA, DV, EC, EG, EX, FA, FT, HO, IE, IS, LB, MB, MH, MI, MK, ML, MS, NV, OE, PC, PE, PP, PR, QS, RE, RP, RS, SC, SE, SR, SS, SU, TA, TR, TU, UR, VS | Planned Order of Element within Arm | Num | Timing | Perm* |
| VISIT | 36 | AG, BE, BS, CP, CV, DA, EG, FA, FT, GF, IE, IS, LB, MB, MI, MK, ML, MS, NV, OE, PC, PE, PR, QS, RE, RP, RS, SC, SR, SS, SV, TR, TU, TV, UR, VS | Visit Name | Char | Timing | Perm* |
| VISITDY | 36 | AG, BE, BS, CP, CV, DA, EG, FA, FT, GF, IE, IS, LB, MB, MI, MK, ML, MS, NV, OE, PC, PE, PR, QS, RE, RP, RS, SC, SR, SS, SV, TR, TU, TV, UR, VS | Planned Study Day of Visit | Num | Timing | Perm |
| VISITNUM | 36 | AG, BE, BS, CP, CV, DA, EG, FA, FT, GF, IE, IS, LB, MB, MI, MK, ML, MS, NV, OE, PC, PE, PR, QS, RE, RP, RS, SC, SR, SS, SV, TR, TU, TV, UR, VS | Visit Number | Num | Timing | Exp* |
| SPDEVID | 6 | AE, BE, BS, EG, GF, RE | Sponsor Device Identifier | Char | Identifier | Perm |
| NHOID | 4 | GF, IS, MS, OI | Non-Host Organism Identifier | Char | Identifier | Perm* |
| ARM | 3 | DM, TA, TV | Description of Planned Arm | Char | Synonym Qualifier | Exp* |
| ARMCD | 3 | DM, TA, TV | Planned Arm Code | Char | Record Qualifier | Exp* |
| ELEMENT | 3 | SE, TA, TE | Description of Element | Char | Synonym Qualifier | Perm* |
| ETCD | 3 | SE, TA, TE | Element Code | Char | Topic | Req |
| FOCID | 3 | MB, NV, OE | Focus of Study-Specific Interest | Char | Identifier | Perm |
| IDVAR | 3 | CO, RELREC, SUPPQUAL | Identifying Variable | Char | Record Qualifier | Perm* |
| IDVARVAL | 3 | CO, RELREC, SUPPQUAL | Identifying Variable Value | Char | Record Qualifier | Exp* |
| RDOMAIN | 3 | CO, RELREC, SUPPQUAL | Related Domain Abbreviation | Char | Record Qualifier | Req* |
| IECAT | 2 | IE, TI | Inclusion/Exclusion Category | Char | Grouping Qualifier | Req |
| IESCAT | 2 | IE, TI | Inclusion/Exclusion Subcategory | Char | Grouping Qualifier | Perm |
| IETEST | 2 | IE, TI | Inclusion/Exclusion Criterion | Char | Synonym Qualifier | Req |
| IETESTCD | 2 | IE, TI | Inclusion/Exclusion Criterion Short Name | Char | Topic | Req |
| MIDS | 2 | ML, SM | Disease Milestone Instance Name | Char | Timing | Perm* |
| MIDSTYPE | 2 | SM, TM | Disease Milestone Type | Char | Record Qualifier | Req |

> \* Core 值后带星号表示该变量在不同域中 Core 不完全一致，以最常见值显示。

---

## 二、领域专属变量（仅 1 个域，共 1499 个），按域分组

### AE — Adverse Events (Events)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| AESEQ | Sequence Number | Num | Identifier | Req | — |
| AEGRPID | Group ID | Char | Identifier | Perm | — |
| AEREFID | Reference ID | Char | Identifier | Perm | — |
| AESPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| AETERM | Reported Term for the Adverse Event | Char | Topic | Req | — |
| AEMODIFY | Modified Reported Term | Char | Synonym Qualifier | Perm | — |
| AELLT | Lowest Level Term | Char | Variable Qualifier | Exp | MedDRA |
| AELLTCD | Lowest Level Term Code | Num | Variable Qualifier | Exp | MedDRA |
| AEDECOD | Dictionary-Derived Term | Char | Synonym Qualifier | Req | MedDRA |
| AEPTCD | Preferred Term Code | Num | Variable Qualifier | Exp | MedDRA |
| AEHLT | High Level Term | Char | Variable Qualifier | Exp | MedDRA |
| AEHLTCD | High Level Term Code | Num | Variable Qualifier | Exp | MedDRA |
| AEHLGT | High Level Group Term | Char | Variable Qualifier | Exp | MedDRA |
| AEHLGTCD | High Level Group Term Code | Num | Variable Qualifier | Exp | MedDRA |
| AECAT | Category for Adverse Event | Char | Grouping Qualifier | Perm | — |
| AESCAT | Subcategory for Adverse Event | Char | Grouping Qualifier | Perm | — |
| AEPRESP | Pre-Specified Adverse Event | Char | Variable Qualifier | Perm | C66742 |
| AEBODSYS | Body System or Organ Class | Char | Record Qualifier | Exp | — |
| AEBDSYCD | Body System or Organ Class Code | Num | Variable Qualifier | Exp | MedDRA |
| AESOC | Primary System Organ Class | Char | Variable Qualifier | Exp | MedDRA |
| AESOCCD | Primary System Organ Class Code | Num | Variable Qualifier | Exp | MedDRA |
| AELOC | Location of Event | Char | Record Qualifier | Perm | C74456 |
| AESEV | Severity/Intensity | Char | Record Qualifier | Perm | C66769 |
| AESER | Serious Event | Char | Record Qualifier | Exp | C66742 |
| AEACN | Action Taken with Study Treatment | Char | Record Qualifier | Exp | C66767 |
| AEACNOTH | Other Action Taken | Char | Record Qualifier | Perm | — |
| AEACNDEV | Action Taken with Device | Char | Record Qualifier | Perm | C111110 |
| AEREL | Causality | Char | Record Qualifier | Exp | — |
| AERLDEV | Relationship of Event to Device | Char | Record Qualifier | Perm | — |
| AERELNST | Relationship to Non-Study Treatment | Char | Record Qualifier | Perm | — |
| AEPATT | Pattern of Adverse Event | Char | Record Qualifier | Perm | — |
| AEOUT | Outcome of Adverse Event | Char | Record Qualifier | Perm | C66768 |
| AESCAN | Involves Cancer | Char | Record Qualifier | Perm | C66742 |
| AESCONG | Congenital Anomaly or Birth Defect | Char | Record Qualifier | Perm | C66742 |
| AESDISAB | Persist or Signif Disability/Incapacity | Char | Record Qualifier | Perm | C66742 |
| AESDTH | Results in Death | Char | Record Qualifier | Perm | C66742 |
| AESHOSP | Requires or Prolongs Hospitalization | Char | Record Qualifier | Perm | C66742 |
| AESLIFE | Is Life Threatening | Char | Record Qualifier | Perm | C66742 |
| AESOD | Occurred with Overdose | Char | Record Qualifier | Perm | C66742 |
| AESMIE | Other Medically Important Serious Event | Char | Record Qualifier | Perm | C66742 |
| AESINTV | Needs Intervention to Prevent Impairment | Char | Record Qualifier | Perm | C66742 |
| AEUNANT | Unanticipated Adverse Device Effect | Char | Record Qualifier | Perm | C66742 |
| AERLPRT | Rel of AE to Non-Dev-Rel Study Activity | Char | Record Qualifier | Perm | — |
| AERLPRC | Rel of AE to Device-Related Procedure | Char | Record Qualifier | Perm | — |
| AECONTRT | Concomitant or Additional Trtmnt Given | Char | Record Qualifier | Perm | C66742 |
| AETOXGR | Standard Toxicity Grade | Char | Record Qualifier | Perm | — |
| AESTDTC | Start Date/Time of Adverse Event | Char | Timing | Exp | ISO 8601 datetime or interval |
| AEENDTC | End Date/Time of Adverse Event | Char | Timing | Exp | ISO 8601 datetime or interval |
| AESTDY | Study Day of Start of Adverse Event | Num | Timing | Perm | — |
| AEENDY | Study Day of End of Adverse Event | Num | Timing | Perm | — |
| AEDUR | Duration of Adverse Event | Char | Timing | Perm | ISO 8601 duration |
| AEENRF | End Relative to Reference Period | Char | Timing | Perm | C66728 |
| AEENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| AEENTPT | End Reference Time Point | Char | Timing | Perm | — |

### AG — Procedure Agents (Interventions)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| AGSEQ | Sequence Number | Num | Identifier | Req | — |
| AGGRPID | Group ID | Char | Identifier | Perm | — |
| AGSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| AGLNKID | Link ID | Char | Identifier | Perm | — |
| AGLNKGRP | Link Group ID | Char | Identifier | Perm | — |
| AGTRT | Reported Agent Name | Char | Topic | Req | — |
| AGMODIFY | Modified Reported Name | Char | Synonym Qualifier | Perm | — |
| AGDECOD | Standardized Agent Name | Char | Synonym Qualifier | Perm | — |
| AGCAT | Category for Agent | Char | Grouping Qualifier | Perm | — |
| AGSCAT | Subcategory for Agent | Char | Grouping Qualifier | Perm | — |
| AGPRESP | AG Pre-Specified | Char | Variable Qualifier | Perm | C66742 |
| AGOCCUR | AG Occurrence | Char | Record Qualifier | Perm | C66742 |
| AGSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| AGREASND | Reason Procedure Agent Not Collected | Char | Record Qualifier | Perm | — |
| AGCLAS | Agent Class | Char | Variable Qualifier | Perm | — |
| AGCLASCD | Agent Class Code | Char | Variable Qualifier | Perm | — |
| AGDOSE | Dose per Administration | Num | Record Qualifier | Perm | — |
| AGDOSTXT | Dose Description | Char | Record Qualifier | Perm | — |
| AGDOSU | Dose Units | Char | Variable Qualifier | Perm | C71620 |
| AGDOSFRM | Dose Form | Char | Variable Qualifier | Perm | C66726 |
| AGDOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier | Perm | C71113 |
| AGROUTE | Route of Administration | Char | Variable Qualifier | Perm | C66729 |
| AGSTDTC | Start Date/Time of Agent | Char | Timing | Perm | ISO 8601 datetime or interval |
| AGENDTC | End Date/Time of Agent | Char | Timing | Perm | ISO 8601 datetime or interval |
| AGSTDY | Study Day of Start of Agent | Num | Timing | Perm | — |
| AGENDY | Study Day of End of Agent | Num | Timing | Perm | — |
| AGDUR | Duration of Agent | Char | Timing | Perm | ISO 8601 duration |
| AGSTRF | Start Relative to Reference Period | Char | Timing | Perm | C66728 |
| AGENRF | End Relative to Reference Period | Char | Timing | Perm | C66728 |
| AGSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| AGSTTPT | Start Reference Time Point | Char | Timing | Perm | — |
| AGENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| AGENTPT | End Reference Time Point | Char | Timing | Perm | — |

### BE — Biospecimen Events (Events)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| BESEQ | Sequence Number | Num | Identifier | Req | — |
| BEGRPID | Group ID | Char | Identifier | Perm | — |
| BEREFID | Reference ID | Char | Identifier | Exp | — |
| BESPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| BETERM | Reported Term for the Biospecimen Event | Char | Topic | Req | — |
| BEMODIFY | Modified Reported Term | Char | Synonym Qualifier | Perm | — |
| BEDECOD | Dictionary-Derived Term | Char | Synonym Qualifier | Perm | C124297 |
| BECAT | Category for Biospecimen Event | Char | Grouping Qualifier | Perm | — |
| BESCAT | Subcategory for Biospecimen Event | Char | Grouping Qualifier | Perm | — |
| BELOC | Anatomical Location of Event | Char | Record Qualifier | Perm | C74456 |
| BEPARTY | Accountable Party | Char | Record Qualifier | Perm | — |
| BEPRTYID | Identification of Accountable Party | Char | Record Qualifier | Perm | — |
| BEDTC | Date/Time of Specimen Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| BESTDTC | Start Date/Time of Biospecimen Event | Char | Timing | Exp | ISO 8601 datetime or interval |
| BEENDTC | End Date/Time of Biospecimen Event | Char | Timing | Exp | ISO 8601 datetime or interval |
| BESTDY | Study Day of Start of Biospecimen Event | Num | Timing | Perm | — |
| BEENDY | Study Day of End of Biospecimen Event | Num | Timing | Perm | — |
| BEDUR | Duration of Biospecimen Event | Char | Timing | Perm | ISO 8601 duration |

### BS — Biospecimen Findings (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| BSSEQ | Sequence Number | Num | Identifier | Req | — |
| BSGRPID | Group ID | Char | Identifier | Perm | — |
| BSREFID | Reference ID | Char | Identifier | Exp | — |
| BSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| BSTESTCD | Biospecimen Test Short Name | Char | Topic | Req | C124300 |
| BSTEST | Biospecimen Test Name | Char | Synonym Qualifier | Req | C124299 |
| BSCAT | Category for Biospecimen Test | Char | Grouping Qualifier | Exp | — |
| BSSCAT | Subcategory for Biospecimen Test | Char | Grouping Qualifier | Perm | — |
| BSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| BSORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |
| BSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| BSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp | — |
| BSSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |
| BSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| BSREASND | Reason Test Not Done | Char | Record Qualifier | Perm | — |
| BSNAM | Vendor Name | Char | Record Qualifier | Perm | — |
| BSSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734; C111114 |
| BSANTREG | Anatomical Region of Specimen | Char | Variable Qualifier | Perm | — |
| BSSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| BSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| BSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| BSDTC | Date/Time of Specimen Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| BSDY | Study Day of Specimen Collection | Num | Timing | Perm | — |
| BSTPT | Planned Time Point Name | Char | Timing | Perm | — |
| BSTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| BSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| BSTPTREF | Time Point Reference | Char | Timing | Perm | — |
| BSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### CE — Clinical Events (Events)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| CESEQ | Sequence Number | Num | Identifier | Req | — |
| CEGRPID | Group ID | Char | Identifier | Perm | — |
| CEREFID | Reference ID | Char | Identifier | Perm | — |
| CESPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| CETERM | Reported Term for the Clinical Event | Char | Topic | Req | — |
| CEDECOD | Dictionary-Derived Term | Char | Synonym Qualifier | Perm | — |
| CECAT | Category for the Clinical Event | Char | Grouping Qualifier | Perm | — |
| CESCAT | Subcategory for the Clinical Event | Char | Grouping Qualifier | Perm | — |
| CEPRESP | Clinical Event Pre-specified | Char | Variable Qualifier | Perm | C66742 |
| CEOCCUR | Clinical Event Occurrence | Char | Record Qualifier | Perm | C66742 |
| CESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| CEREASND | Reason Clinical Event Not Collected | Char | Record Qualifier | Perm | — |
| CEBODSYS | Body System or Organ Class | Char | Record Qualifier | Perm | — |
| CESEV | Severity/Intensity | Char | Record Qualifier | Perm | C165643 |
| CETOXGR | Standard Toxicity Grade | Char | Record Qualifier | Perm | — |
| CEDTC | Date/Time of Event Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| CESTDTC | Start Date/Time of Clinical Event | Char | Timing | Perm | ISO 8601 datetime or interval |
| CEENDTC | End Date/Time of Clinical Event | Char | Timing | Perm | ISO 8601 datetime or interval |
| CEDY | Study Day of Event Collection | Num | Timing | Perm | — |
| CESTDY | Study Day of Start of Event | Num | Timing | Perm | — |
| CEENDY | Study Day of End of Event | Num | Timing | Perm | — |
| CESTRF | Start Relative to Reference Period | Char | Timing | Perm | C66728 |
| CEENRF | End Relative to Reference Period | Char | Timing | Perm | C66728 |
| CESTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| CESTTPT | Start Reference Time Point | Char | Timing | Perm | — |
| CEENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| CEENTPT | End Reference Time Point | Char | Timing | Perm | — |

### CM — Concomitant/Prior Medications (Interventions)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| CMSEQ | Sequence Number | Num | Identifier | Req | — |
| CMGRPID | Group ID | Char | Identifier | Perm | — |
| CMSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| CMTRT | Reported Name of Drug, Med, or Therapy | Char | Topic | Req | — |
| CMMODIFY | Modified Reported Name | Char | Synonym Qualifier | Perm | — |
| CMDECOD | Standardized Medication Name | Char | Synonym Qualifier | Perm | — |
| CMCAT | Category for Medication | Char | Grouping Qualifier | Perm | — |
| CMSCAT | Subcategory for Medication | Char | Grouping Qualifier | Perm | — |
| CMPRESP | CM Pre-specified | Char | Variable Qualifier | Perm | C66742 |
| CMOCCUR | CM Occurrence | Char | Record Qualifier | Perm | C66742 |
| CMSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| CMREASND | Reason Medication Not Collected | Char | Record Qualifier | Perm | — |
| CMINDC | Indication | Char | Record Qualifier | Perm | — |
| CMCLAS | Medication Class | Char | Variable Qualifier | Perm | — |
| CMCLASCD | Medication Class Code | Char | Variable Qualifier | Perm | — |
| CMDOSE | Dose per Administration | Num | Record Qualifier | Perm | — |
| CMDOSTXT | Dose Description | Char | Record Qualifier | Perm | — |
| CMDOSU | Dose Units | Char | Variable Qualifier | Perm | C71620 |
| CMDOSFRM | Dose Form | Char | Variable Qualifier | Perm | C66726 |
| CMDOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier | Perm | C71113 |
| CMDOSTOT | Total Daily Dose | Num | Record Qualifier | Perm | — |
| CMDOSRGM | Intended Dose Regimen | Char | Record Qualifier | Perm | — |
| CMROUTE | Route of Administration | Char | Variable Qualifier | Perm | C66729 |
| CMADJ | Reason for Dose Adjustment | Char | Record Qualifier | Perm | — |
| CMRSDISC | Reason the Intervention Was Discontinued | Char | Record Qualifier | Perm | — |
| CMSTDTC | Start Date/Time of Medication | Char | Timing | Perm | ISO 8601 datetime or interval |
| CMENDTC | End Date/Time of Medication | Char | Timing | Perm | ISO 8601 datetime or interval |
| CMSTDY | Study Day of Start of Medication | Num | Timing | Perm | — |
| CMENDY | Study Day of End of Medication | Num | Timing | Perm | — |
| CMDUR | Duration | Char | Timing | Perm | ISO 8601 duration |
| CMSTRF | Start Relative to Reference Period | Char | Timing | Perm | C66728 |
| CMENRF | End Relative to Reference Period | Char | Timing | Perm | C66728 |
| CMSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| CMSTTPT | Start Reference Time Point | Char | Timing | Perm | — |
| CMENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| CMENTPT | End Reference Time Point | Char | Timing | Perm | — |

### CO — Comments (Special-Purpose)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| COSEQ | Sequence Number | Num | Identifier | Req | — |
| COREF | Comment Reference | Char | Record Qualifier | Perm | — |
| COVAL | Comment | Char | Topic | Req | — |
| COEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| COEVALID | Evaluator Identifier | Char | Record Qualifier | Perm | C96777 |
| CODTC | Date/Time of Comment | Char | Timing | Perm | ISO 8601 datetime or interval |
| CODY | Study Day of Comment | Num | Timing | Perm | — |

### CP — Cell Phenotype Findings (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| CPSEQ | Sequence Number | Num | Identifier | Req | — |
| CPGRPID | Group ID | Char | Identifier | Perm | — |
| CPREFID | Reference ID | Char | Identifier | Perm | — |
| CPSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| CPLNKID | Link ID | Char | Identifier | Perm | — |
| CPLNKGRP | Link Group ID | Char | Identifier | Perm | — |
| CPTESTCD | Test or Examination Short Name | Char | Topic | Req | C181173 |
| CPTEST | Name of Measurement, Test or Examination | Char | Synonym Qualifier | Req | C181174 |
| CPSBMRKS | Sublineage Marker String | Char | Variable Qualifier | Perm | — |
| CPCELSTA | Cell State | Char | Variable Qualifier | Perm | C181172 |
| CPCSMRKS | Cell State Marker String | Char | Variable Qualifier | Perm | — |
| CPTSTCND | Test Condition | Char | Variable Qualifier | Perm | C181175 |
| CPCNDAGT | Test Condition Agent | Char | Record Qualifier | Perm | — |
| CPBDAGNT | Binding Agent | Char | Record Qualifier | Perm | — |
| CPABCLID | Antibody Clone Identifier | Char | Record Qualifier | Perm | — |
| CPMRKSTR | Marker String | Char | Record Qualifier | Exp | — |
| CPGATE | Gate | Char | Record Qualifier | Perm | — |
| CPGATDEF | Gate Definition | Char | Record Qualifier | Perm | — |
| CPSPTSTD | Sponsor Test Description | Char | Record Qualifier | Perm | — |
| CPCAT | Category | Char | Grouping Qualifier | Perm | C181171 |
| CPSCAT | Subcategory | Char | Grouping Qualifier | Perm | — |
| CPTSTPNL | Test Panel | Char | Grouping Qualifier | Perm | — |
| CPORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| CPORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| CPRESSCL | Result Scale | Char | Record Qualifier | Perm | C177910 |
| CPRESTYP | Result Type | Char | Record Qualifier | Perm | C179588 |
| CPCOLSRT | Collected Summary Result Type | Char | Record Qualifier | Perm | C177908 |
| CPORNRLO | Reference Range Lower Limit in Orig Unit | Char | Variable Qualifier | Perm | — |
| CPORNRHI | Reference Range Upper Limit in Orig Unit | Char | Variable Qualifier | Perm | — |
| CPSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp | — |
| CPSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| CPSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| CPSTNRLO | Reference Range Lower Limit-Std Units | Num | Variable Qualifier | Perm | — |
| CPSTNRHI | Reference Range Upper Limit-Std Units | Num | Variable Qualifier | Perm | — |
| CPNRIND | Reference Range Indicator | Char | Variable Qualifier | Perm | C78736 |
| CPSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| CPREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| CPNAM | Vendor Name | Char | Record Qualifier | Perm | — |
| CPLOINC | LOINC Code | Char | Synonym Qualifier | Perm | LOINC |
| CPSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734 |
| CPSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| CPMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| CPANMETH | Analysis Method | Char | Record Qualifier | Perm | — |
| CPLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| CPBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| CPDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| CPCLSIG | Clinically Significant, Collected | Char | Record Qualifier | Perm | C66742 |
| CPDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| CPDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |
| CPTPT | Planned Time Point Name | Char | Timing | Perm | — |
| CPTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| CPELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| CPTPTREF | Time Point Reference | Char | Timing | Perm | — |
| CPRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### CV — Cardiovascular System Findings (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| CVSEQ | Sequence Number | Num | Identifier | Req | — |
| CVGRPID | Group ID | Char | Identifier | Perm | — |
| CVREFID | Reference ID | Char | Identifier | Perm | — |
| CVSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| CVLNKID | Link ID | Char | Identifier | Perm | — |
| CVLNKGRP | Link Group | Char | Identifier | Perm | — |
| CVTESTCD | Short Name of Cardiovascular Test | Char | Topic | Req | C101847 |
| CVTEST | Name of Cardiovascular Test | Char | Synonym Qualifier | Req | C101846 |
| CVCAT | Category for Cardiovascular Test | Char | Grouping Qualifier | Perm | — |
| CVSCAT | Subcategory for Cardiovascular Test | Char | Grouping Qualifier | Perm | — |
| CVPOS | Position of Subject During Observation | Char | Record Qualifier | Perm | C71148 |
| CVORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| CVORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| CVSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| CVSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| CVSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| CVSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| CVREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| CVLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |
| CVLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| CVDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| CVMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| CVLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| CVBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| CVDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| CVEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| CVEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| CVDTC | Date/Time of Test | Char | Timing | Exp | ISO 8601 datetime or interval |
| CVDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |
| CVTPT | Planned Time Point Name | Char | Timing | Perm | — |
| CVTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| CVELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| CVTPTREF | Time Point Reference | Char | Timing | Perm | — |
| CVRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### DA — Product Accountability (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| DASEQ | Sequence Number | Num | Identifier | Req | — |
| DAGRPID | Group ID | Char | Identifier | Perm | — |
| DAREFID | Reference ID | Char | Identifier | Perm | — |
| DASPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| DALNKID | Link ID | Char | Identifier | Perm | — |
| DALNKGRP | Link Group ID | Char | Identifier | Perm | — |
| DATESTCD | Short Name of Accountability Assessment | Char | Topic | Req | C78732 |
| DATEST | Name of Accountability Assessment | Char | Synonym Qualifier | Req | C78731 |
| DACAT | Category | Char | Grouping Qualifier | Perm | — |
| DASCAT | Subcategory | Char | Grouping Qualifier | Perm | — |
| DAORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| DAORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| DASTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp | — |
| DASTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| DASTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| DASTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| DAREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| DADTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| DADY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |

### DD — Death Details (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| DDSEQ | Sequence Number | Num | Identifier | Req | — |
| DDTESTCD | Death Detail Assessment Short Name | Char | Topic | Req | C116108 |
| DDTEST | Death Detail Assessment Name | Char | Synonym Qualifier | Req | C116107 |
| DDORRES | Result or Finding as Collected | Char | Result Qualifier | Exp | — |
| DDSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| DDRESCAT | Result Category | Char | Variable Qualifier | Perm | — |
| DDEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| DDDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| DDDY | Study Day of Collection | Num | Timing | Perm | — |

### DM — Demographics (Special-Purpose)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| SUBJID | Subject Identifier for the Study | Char | Topic | Req | — |
| RFSTDTC | Subject Reference Start Date/Time | DateTime | Record Qualifier | Exp | ISO 8601 datetime or interval |
| RFENDTC | Subject Reference End Date/Time | DateTime | Record Qualifier | Exp | ISO 8601 datetime or interval |
| RFXSTDTC | Date/Time of First Study Treatment | Char | Record Qualifier | Exp | ISO 8601 datetime or interval |
| RFXENDTC | Date/Time of Last Study Treatment | Char | Record Qualifier | Exp | ISO 8601 datetime or interval |
| RFCSTDTC | Date/Time of First Challenge Agent Admin | Char | Record Qualifier | Perm | ISO 8601 datetime or interval |
| RFCENDTC | Date/Time of Last Challenge Agent Admin | Char | Record Qualifier | Perm | ISO 8601 datetime or interval |
| RFICDTC | Date/Time of Informed Consent | Char | Record Qualifier | Exp | ISO 8601 datetime or interval |
| RFPENDTC | Date/Time of End of Participation | Char | Record Qualifier | Exp | ISO 8601 datetime or interval |
| DTHDTC | Date/Time of Death | Char | Record Qualifier | Exp | ISO 8601 datetime or interval |
| DTHFL | Subject Death Flag | Char | Record Qualifier | Exp | C66742 |
| SITEID | Study Site Identifier | Char | Record Qualifier | Req | — |
| INVID | Investigator Identifier | Char | Record Qualifier | Perm | — |
| INVNAM | Investigator Name | Char | Synonym Qualifier | Perm | — |
| BRTHDTC | Date/Time of Birth | Char | Record Qualifier | Perm | ISO 8601 datetime or interval |
| AGE | Age | Num | Record Qualifier | Exp | — |
| AGEU | Age Units | Char | Variable Qualifier | Exp | C66781 |
| SEX | Sex | Char | Record Qualifier | Req | C66731 |
| RACE | Race | Char | Record Qualifier | Exp | C74457 |
| ETHNIC | Ethnicity | Char | Record Qualifier | Perm | C66790 |
| ACTARMCD | Actual Arm Code | Char | Record Qualifier | Exp | — |
| ACTARM | Description of Actual Arm | Char | Synonym Qualifier | Exp | — |
| ARMNRS | Reason Arm and/or Actual Arm is Null | Char | Record Qualifier | Exp | C142179 |
| ACTARMUD | Description of Unplanned Actual Arm | Char | Record Qualifier | Exp | — |
| COUNTRY | Country | Char | Record Qualifier | Req | — |
| DMDTC | Date/Time of Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| DMDY | Study Day of Collection | Num | Timing | Perm | — |

### DS — Disposition (Events)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| DSSEQ | Sequence Number | Num | Identifier | Req | — |
| DSGRPID | Group ID | Char | Identifier | Perm | — |
| DSREFID | Reference ID | Char | Identifier | Perm | — |
| DSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| DSTERM | Reported Term for the Disposition Event | Char | Topic | Req | — |
| DSDECOD | Standardized Disposition Term | Char | Synonym Qualifier | Req | C66727; C114118; C150811 |
| DSCAT | Category for Disposition Event | Char | Grouping Qualifier | Exp | C74558 |
| DSSCAT | Subcategory for Disposition Event | Char | Grouping Qualifier | Perm | C170443 |
| DSDTC | Date/Time of Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| DSSTDTC | Start Date/Time of Disposition Event | Char | Timing | Exp | ISO 8601 datetime or interval |
| DSDY | Study Day of Collection | Num | Timing | Perm | — |
| DSSTDY | Study Day of Start of Disposition Event | Num | Timing | Exp | — |

### DV — Protocol Deviations (Events)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| DVSEQ | Sequence Number | Num | Identifier | Req | — |
| DVREFID | Reference ID | Char | Identifier | Perm | — |
| DVSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| DVTERM | Protocol Deviation Term | Char | Topic | Req | — |
| DVDECOD | Protocol Deviation Coded Term | Char | Synonym Qualifier | Perm | — |
| DVCAT | Category for Protocol Deviation | Char | Grouping Qualifier | Perm | — |
| DVSCAT | Subcategory for Protocol Deviation | Char | Grouping Qualifier | Perm | — |
| DVSTDTC | Start Date/Time of Deviation | Char | Timing | Perm | ISO 8601 datetime or interval |
| DVENDTC | End Date/Time of Deviation | Char | Timing | Perm | ISO 8601 datetime or interval |
| DVSTDY | Study Day of Start of Deviation Event | Num | Timing | Perm | — |
| DVENDY | Study Day of End of Deviation Event | Num | Timing | Perm | — |

### EC — Exposure as Collected (Interventions)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| ECSEQ | Sequence Number | Num | Identifier | Req | — |
| ECGRPID | Group ID | Char | Identifier | Perm | — |
| ECREFID | Reference ID | Char | Identifier | Perm | — |
| ECSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| ECLNKID | Link ID | Char | Identifier | Perm | — |
| ECLNKGRP | Link Group ID | Char | Identifier | Perm | — |
| ECTRT | Name of Treatment | Char | Topic | Req | — |
| ECMOOD | Mood | Char | Record Qualifier | Perm | C125923 |
| ECCAT | Category of Treatment | Char | Grouping Qualifier | Perm | — |
| ECSCAT | Subcategory of Treatment | Char | Grouping Qualifier | Perm | — |
| ECPRESP | Pre-Specified | Char | Variable Qualifier | Perm | C66742 |
| ECOCCUR | Occurrence | Char | Record Qualifier | Perm | C66742 |
| ECREASOC | Reason for Occur Value | Char | Record Qualifier | Perm | — |
| ECDOSE | Dose | Num | Record Qualifier | Exp | — |
| ECDOSTXT | Dose Description | Char | Record Qualifier | Perm | — |
| ECDOSU | Dose Units | Char | Variable Qualifier | Exp | C71620 |
| ECDOSFRM | Dose Form | Char | Variable Qualifier | Exp | C66726 |
| ECDOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier | Perm | C71113 |
| ECDOSTOT | Total Daily Dose | Num | Record Qualifier | Perm | — |
| ECDOSRGM | Intended Dose Regimen | Char | Record Qualifier | Perm | — |
| ECROUTE | Route of Administration | Char | Variable Qualifier | Perm | C66729 |
| ECLOT | Lot Number | Char | Record Qualifier | Perm | — |
| ECLOC | Location of Dose Administration | Char | Record Qualifier | Perm | C74456 |
| ECLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| ECDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| ECPORTOT | Portion or Totality | Char | Variable Qualifier | Perm | C99075 |
| ECFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |
| ECPSTRG | Pharmaceutical Strength | Num | Record Qualifier | Perm | — |
| ECPSTRGU | Pharmaceutical Strength Units | Char | Variable Qualifier | Perm | C71620 |
| ECADJ | Reason for Dose Adjustment | Char | Record Qualifier | Perm | — |
| ECSTDTC | Start Date/Time of Treatment | Char | Timing | Exp | ISO 8601 datetime or interval |
| ECENDTC | End Date/Time of Treatment | Char | Timing | Exp | ISO 8601 datetime or interval |
| ECSTDY | Study Day of Start of Treatment | Num | Timing | Perm | — |
| ECENDY | Study Day of End of Treatment | Num | Timing | Perm | — |
| ECDUR | Duration of Treatment | Char | Timing | Perm | ISO 8601 duration |
| ECTPT | Planned Time Point Name | Char | Timing | Perm | — |
| ECTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| ECELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| ECTPTREF | Time Point Reference | Char | Timing | Perm | — |
| ECRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### EG — ECG Test Results (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| EGSEQ | Sequence Number | Num | Identifier | Req | — |
| EGGRPID | Group ID | Char | Identifier | Perm | — |
| EGREFID | ECG Reference ID | Char | Identifier | Perm | — |
| EGSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| EGBEATNO | ECG Beat Number | Num | Identifier | Perm | — |
| EGTESTCD | ECG Test or Examination Short Name | Char | Topic | Req | C71153; C120523 |
| EGTEST | ECG Test or Examination Name | Char | Synonym Qualifier | Req | C71152; C120524 |
| EGCAT | Category for ECG | Char | Grouping Qualifier | Perm | — |
| EGSCAT | Subcategory for ECG | Char | Grouping Qualifier | Perm | — |
| EGPOS | ECG Position of Subject | Char | Record Qualifier | Perm | C71148 |
| EGORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| EGORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| EGSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C71150; C120522; C101834 |
| EGSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| EGSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| EGSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| EGREASND | Reason ECG Not Done | Char | Record Qualifier | Perm | — |
| EGXFN | ECG External File Path | Char | Record Qualifier | Perm | — |
| EGNAM | Vendor Name | Char | Record Qualifier | Perm | — |
| EGMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C71151 |
| EGLEAD | Lead Location Used for Measurement | Char | Record Qualifier | Perm | C90013 |
| EGLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| EGBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| EGDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| EGEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| EGEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| EGCLSIG | Clinically Significant, Collected | Char | Record Qualifier | Perm | C66742 |
| EGREPNUM | Repetition Number | Num | Record Qualifier | Perm | — |
| EGDTC | Date/Time of ECG | Char | Timing | Exp | ISO 8601 datetime or interval |
| EGDY | Study Day of ECG | Num | Timing | Perm | — |
| EGTPT | Planned Time Point Name | Char | Timing | Perm | — |
| EGTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| EGELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| EGTPTREF | Time Point Reference | Char | Timing | Perm | — |
| EGRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### EX — Exposure (Interventions)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| EXSEQ | Sequence Number | Num | Identifier | Req | — |
| EXGRPID | Group ID | Char | Identifier | Perm | — |
| EXREFID | Reference ID | Char | Identifier | Perm | — |
| EXSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| EXLNKID | Link ID | Char | Identifier | Perm | — |
| EXLNKGRP | Link Group ID | Char | Identifier | Perm | — |
| EXTRT | Name of Treatment | Char | Topic | Req | — |
| EXCAT | Category of Treatment | Char | Grouping Qualifier | Perm | — |
| EXSCAT | Subcategory of Treatment | Char | Grouping Qualifier | Perm | — |
| EXDOSE | Dose | Num | Record Qualifier | Exp | — |
| EXDOSTXT | Dose Description | Char | Record Qualifier | Perm | — |
| EXDOSU | Dose Units | Char | Variable Qualifier | Exp | C71620 |
| EXDOSFRM | Dose Form | Char | Variable Qualifier | Exp | C66726 |
| EXDOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier | Perm | C71113 |
| EXDOSRGM | Intended Dose Regimen | Char | Record Qualifier | Perm | — |
| EXROUTE | Route of Administration | Char | Variable Qualifier | Perm | C66729 |
| EXLOT | Lot Number | Char | Record Qualifier | Perm | — |
| EXLOC | Location of Dose Administration | Char | Record Qualifier | Perm | C74456 |
| EXLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| EXDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| EXFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |
| EXADJ | Reason for Dose Adjustment | Char | Record Qualifier | Perm | — |
| EXSTDTC | Start Date/Time of Treatment | Char | Timing | Exp | ISO 8601 datetime or interval |
| EXENDTC | End Date/Time of Treatment | Char | Timing | Exp | ISO 8601 datetime or interval |
| EXSTDY | Study Day of Start of Treatment | Num | Timing | Perm | — |
| EXENDY | Study Day of End of Treatment | Num | Timing | Perm | — |
| EXDUR | Duration of Treatment | Char | Timing | Perm | ISO 8601 duration |
| EXTPT | Planned Time Point Name | Char | Timing | Perm | — |
| EXTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| EXELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| EXTPTREF | Time Point Reference | Char | Timing | Perm | — |
| EXRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### FA — Findings About Events or Interventions (Findings About)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| FASEQ | Sequence Number | Num | Identifier | Req | — |
| FAGRPID | Group ID | Char | Identifier | Perm | — |
| FASPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| FATESTCD | Findings About Test Short Name | Char | Topic | Req | C101832 |
| FATEST | Findings About Test Name | Char | Synonym Qualifier | Req | C101833 |
| FAOBJ | Object of the Observation | Char | Record Qualifier | Req | — |
| FACAT | Category for Findings About | Char | Grouping Qualifier | Perm | — |
| FASCAT | Subcategory for Findings About | Char | Grouping Qualifier | Perm | — |
| FAORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| FAORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| FASTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| FASTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| FASTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| FASTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| FAREASND | Reason Not Performed | Char | Record Qualifier | Perm | — |
| FALOC | Location of the Finding About | Char | Record Qualifier | Perm | C74456 |
| FALAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| FALOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| FABLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| FAEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| FADTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| FADY | Study Day of Collection | Num | Timing | Perm | — |

### FT — Functional Tests (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| FTSEQ | Sequence Number | Num | Identifier | Req | — |
| FTGRPID | Group ID | Char | Identifier | Perm | — |
| FTREFID | Reference ID | Char | Identifier | Perm | — |
| FTSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| FTTESTCD | Short Name of Test | Char | Topic | Req | — |
| FTTEST | Name of Test | Char | Synonym Qualifier | Req | — |
| FTCAT | Category | Char | Grouping Qualifier | Req | C115304 |
| FTSCAT | Subcategory | Char | Grouping Qualifier | Perm | — |
| FTPOS | Position of Subject During Observation | Char | Record Qualifier | Perm | C71148 |
| FTORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| FTORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| FTSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp | — |
| FTSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| FTSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| FTSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| FTREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| FTXFN | External File Path | Char | Record Qualifier | Perm | — |
| FTNAM | Vendor Name | Char | Record Qualifier | Perm | — |
| FTMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C158113 |
| FTLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| FTBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| FTDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| FTREPNUM | Repetition Number | Num | Record Qualifier | Perm | — |
| FTDTC | Date/Time of Test | Char | Timing | Exp | ISO 8601 datetime or interval |
| FTDY | Study Day of Test | Num | Timing | Perm | — |
| FTTPT | Planned Time Point Name | Char | Timing | Perm | — |
| FTTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| FTELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| FTTPTREF | Time Point Reference | Char | Timing | Perm | — |
| FTRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### GF — Genomics Findings (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| GFSEQ | Sequence Number | Num | Identifier | Req | — |
| GFGRPID | Group ID | Char | Identifier | Perm | — |
| GFREFID | Reference ID | Char | Identifier | Exp | — |
| GFSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| GFLNKID | Link ID | Char | Identifier | Perm | — |
| GFLNKGRP | Link Group ID | Char | Identifier | Perm | — |
| GFTESTCD | Short Name of Genomic Measurement | Char | Topic | Req | C181178 |
| GFTEST | Name of Genomic Measurement | Char | Synonym Qualifier | Req | C181179 |
| GFTSTDTL | Measurement, Test, or Examination Detail | Char | Variable Qualifier | Perm | C181180 |
| GFCAT | Category for Genomic Finding | Char | Grouping Qualifier | Perm | — |
| GFSCAT | Subcategory for Genomic Finding | Char | Grouping Qualifier | Perm | — |
| GFORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| GFORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| GFORREF | Reference Result in Original Units | Char | Variable Qualifier | Perm | — |
| GFSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp | — |
| GFSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| GFSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| GFSTREFC | Reference Result in Standard Format | Char | Variable Qualifier | Perm | — |
| GFSTREFN | Numeric Reference Result in Std Units | Num | Variable Qualifier | Perm | — |
| GFRESCAT | Result Category | Char | Variable Qualifier | Perm | — |
| GFINHERT | Inheritability | Char | Variable Qualifier | Perm | C181177 |
| GFGENREF | Genome Reference | Char | Variable Qualifier | Perm | — |
| GFCHROM | Chromosome Identifier | Char | Variable Qualifier | Perm | — |
| GFSYM | Genomic Symbol | Char | Variable Qualifier | Perm | — |
| GFSYMTYP | Genomic Symbol Type | Char | Variable Qualifier | Perm | C181176 |
| GFGENLOC | Genetic Location | Char | Variable Qualifier | Perm | — |
| GFGENSR | Genetic Sub-Region | Char | Variable Qualifier | Perm | — |
| GFSEQID | Sequence Identifier | Char | Variable Qualifier | Perm | — |
| GFPVRID | Published Variant Identifier | Char | Variable Qualifier | Perm | — |
| GFCOPYID | Copy Identifier | Char | Variable Qualifier | Perm | — |
| GFSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| GFREASND | Reason Test Not Done | Char | Record Qualifier | Perm | — |
| GFXFN | External File Path | Char | Record Qualifier | Perm | — |
| GFNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm | — |
| GFSPEC | Specimen Material Type | Char | Record Qualifier | Perm | C111114 |
| GFMETHOD | Method of Test or Examination | Char | Record Qualifier | Exp | C85492 |
| GFRUNID | Run ID | Char | Record Qualifier | Perm | — |
| GFANMETH | Analysis Method | Char | Record Qualifier | Perm | C181181 |
| GFBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| GFDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| GFLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Perm | — |
| GFREPNUM | Repetition Number | Num | Record Qualifier | Perm | — |
| GFDTC | Date/Time of Specimen Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| GFDY | Study Day of Specimen Collection | Num | Timing | Perm | — |
| GFTPT | Planned Time Point Name | Char | Timing | Perm | — |
| GFTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| GFELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| GFTPTREF | Time Point Reference | Char | Timing | Perm | — |
| GFRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### HO — Healthcare Encounters (Events)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| HOSEQ | Sequence Number | Num | Identifier | Req | — |
| HOGRPID | Group ID | Char | Identifier | Perm | — |
| HOREFID | Reference ID | Char | Identifier | Perm | — |
| HOSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| HOTERM | Healthcare Encounter Term | Char | Topic | Req | — |
| HODECOD | Dictionary-Derived Term | Char | Synonym Qualifier | Perm | C171444 |
| HOCAT | Category for Healthcare Encounter | Char | Grouping Qualifier | Perm | — |
| HOSCAT | Subcategory for Healthcare Encounter | Char | Grouping Qualifier | Perm | — |
| HOPRESP | Pre-Specified Healthcare Encounter | Char | Variable Qualifier | Perm | C66742 |
| HOOCCUR | Healthcare Encounter Occurrence | Char | Record Qualifier | Perm | C66742 |
| HOSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| HOREASND | Reason Healthcare Encounter Not Done | Char | Record Qualifier | Perm | — |
| HODTC | Date/Time of Event Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| HOSTDTC | Start Date/Time of Healthcare Encounter | Char | Timing | Exp | ISO 8601 datetime or interval |
| HOENDTC | End Date/Time of Healthcare Encounter | Char | Timing | Perm | ISO 8601 datetime or interval |
| HODY | Study Day of Event Collection | Num | Timing | Perm | — |
| HOSTDY | Study Day of Start of Encounter | Num | Timing | Perm | — |
| HOENDY | Study Day of End of Healthcare Encounter | Num | Timing | Perm | — |
| HODUR | Duration of Healthcare Encounter | Char | Timing | Perm | ISO 8601 duration |
| HOSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| HOSTTPT | Start Reference Time Point | Char | Timing | Perm | — |
| HOENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| HOENTPT | End Reference Time Point | Char | Timing | Perm | — |

### IE — Inclusion/Exclusion Criteria Not Met (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| IESEQ | Sequence Number | Num | Identifier | Req | — |
| IESPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| IEORRES | I/E Criterion Original Result | Char | Result Qualifier | Req | C66742 |
| IESTRESC | I/E Criterion Result in Std Format | Char | Result Qualifier | Req | C66742 |
| IEDTC | Date/Time of Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| IEDY | Study Day of Collection | Num | Timing | Perm | — |

### IS — Immunogenicity Specimen Assessments (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| ISSEQ | Sequence Number | Num | Identifier | Req | — |
| ISGRPID | Group ID | Char | Identifier | Perm | — |
| ISREFID | Reference ID | Char | Identifier | Perm | — |
| ISSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| ISTESTCD | Immunogenicity Test/Exam Short Name | Char | Topic | Req | C120525 |
| ISTEST | Immunogenicity Test or Examination Name | Char | Synonym Qualifier | Req | C120526 |
| ISTSTCND | Test Condition | Char | Variable Qualifier | Perm | C181175 |
| ISCNDAGT | Test Condition Agent | Char | Record Qualifier | Perm | — |
| ISBDAGNT | Binding Agent | Char | Variable Qualifier | Perm | C85491; C181169 |
| ISTSTOPO | Test Operational Objective | Char | Variable Qualifier | Perm | C181170 |
| ISMSCBCE | Molecule Secreted by Cells | Char | Variable Qualifier | Perm | — |
| ISTSTDTL | Test Detail | Char | Variable Qualifier | Perm | — |
| ISCAT | Category for Immunogenicity Test | Char | Grouping Qualifier | Perm | — |
| ISSCAT | Subcategory for Immunogenicity Test | Char | Grouping Qualifier | Perm | — |
| ISORRES | Results or Findings in Original Units | Char | Result Qualifier | Exp | — |
| ISORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |
| ISORNRLO | Reference Range Lower Limit in Orig Unit | Char | Variable Qualifier | Exp | — |
| ISORNRHI | Reference Range Upper Limit in Orig Unit | Char | Variable Qualifier | Exp | — |
| ISSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| ISSTRESN | Numeric Results/Findings in Std. Units | Num | Result Qualifier | Exp | — |
| ISSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |
| ISSTNRLO | Reference Range Lower Limit-Std Units | Num | Variable Qualifier | Exp | — |
| ISSTNRHI | Reference Range Upper Limit-Std Units | Num | Variable Qualifier | Exp | — |
| ISSTNRC | Reference Range for Char Rslt-Std Units | Char | Variable Qualifier | Perm | — |
| ISNRIND | Reference Range Indicator | Char | Variable Qualifier | Exp | C78736 |
| ISSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| ISREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| ISNAM | Vendor Name | Char | Record Qualifier | Perm | — |
| ISSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734 |
| ISSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| ISSPCUFL | Specimen Usability for the Test | Char | Record Qualifier | Perm | C66742 |
| ISMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| ISLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| ISBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| ISDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| ISLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Exp | — |
| ISDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| ISENDTC | End Date/Time of Specimen Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| ISDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |
| ISENDY | Study Day of End of Specimen Collection | Num | Timing | Perm | — |
| ISTPT | Planned Time Point Name | Char | Timing | Perm | — |
| ISTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| ISELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| ISTPTREF | Time Point Reference | Char | Timing | Perm | — |
| ISRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### LB — Laboratory Test Results (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| LBSEQ | Sequence Number | Num | Identifier | Req | — |
| LBGRPID | Group ID | Char | Identifier | Perm | — |
| LBREFID | Specimen ID | Char | Identifier | Perm | — |
| LBSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| LBTESTCD | Lab Test or Examination Short Name | Char | Topic | Req | C65047 |
| LBTEST | Lab Test or Examination Name | Char | Synonym Qualifier | Req | C67154 |
| LBTSTCND | Test Condition | Char | Variable Qualifier | Perm | C181175 |
| LBBDAGNT | Binding Agent | Char | Variable Qualifier | Perm | — |
| LBTSTOPO | Test Operational Objective | Char | Variable Qualifier | Perm | C181170 |
| LBCAT | Category for Lab Test | Char | Grouping Qualifier | Exp | — |
| LBSCAT | Subcategory for Lab Test | Char | Grouping Qualifier | Perm | — |
| LBORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| LBORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |
| LBRESSCL | Result Scale | Char | Record Qualifier | Perm | C177910 |
| LBRESTYP | Result Type | Char | Record Qualifier | Perm | C179588 |
| LBCOLSRT | Collected Summary Result Type | Char | Record Qualifier | Perm | C177908 |
| LBORNRLO | Reference Range Lower Limit in Orig Unit | Char | Variable Qualifier | Exp | — |
| LBORNRHI | Reference Range Upper Limit in Orig Unit | Char | Variable Qualifier | Exp | — |
| LBLLOD | Lower Limit of Detection | Char | Variable Qualifier | Perm | — |
| LBSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C102580 |
| LBSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp | — |
| LBSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |
| LBSTNRLO | Reference Range Lower Limit-Std Units | Num | Variable Qualifier | Exp | — |
| LBSTNRHI | Reference Range Upper Limit-Std Units | Num | Variable Qualifier | Exp | — |
| LBSTNRC | Reference Range for Char Rslt-Std Units | Char | Variable Qualifier | Perm | — |
| LBNRIND | Reference Range Indicator | Char | Variable Qualifier | Exp | C78736 |
| LBSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| LBREASND | Reason Test Not Done | Char | Record Qualifier | Perm | — |
| LBNAM | Vendor Name | Char | Record Qualifier | Perm | — |
| LBLOINC | LOINC Code | Char | Synonym Qualifier | Perm | LOINC |
| LBSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734 |
| LBSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| LBSPCUFL | Specimen Usability for the Test | Char | Record Qualifier | Perm | C66742 |
| LBMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| LBANMETH | Analysis Method | Char | Record Qualifier | Perm | C160922 |
| LBTMTHSN | Test Method Sensitivity | Char | Record Qualifier | Perm | C179589 |
| LBLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| LBBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| LBFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |
| LBDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| LBTOX | Toxicity | Char | Variable Qualifier | Perm | — |
| LBTOXGR | Standard Toxicity Grade | Char | Record Qualifier | Perm | — |
| LBCLSIG | Clinically Significant, Collected | Char | Record Qualifier | Perm | C66742 |
| LBDTC | Date/Time of Specimen Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| LBENDTC | End Date/Time of Specimen Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| LBDY | Study Day of Specimen Collection | Num | Timing | Perm | — |
| LBENDY | Study Day of End of Observation | Num | Timing | Perm | — |
| LBTPT | Planned Time Point Name | Char | Timing | Perm | — |
| LBTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| LBELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| LBTPTREF | Time Point Reference | Char | Timing | Perm | — |
| LBRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |
| LBPTFL | Point in Time Flag | Char | Timing | Perm | C66742 |
| LBPDUR | Planned Duration | Char | Timing | Perm | ISO 8601 duration |

### MB — Microbiology Specimen (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| MBSEQ | Sequence Number | Num | Identifier | Req | — |
| MBGRPID | Group ID | Char | Identifier | Perm | — |
| MBREFID | Reference ID | Char | Identifier | Perm | — |
| MBSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| MBLNKID | Link ID | Char | Identifier | Perm | — |
| MBLNKGRP | Link Group ID | Char | Identifier | Perm | — |
| MBTESTCD | Microbiology Test or Finding Short Name | Char | Topic | Req | C120527 |
| MBTEST | Microbiology Test or Finding Name | Char | Synonym Qualifier | Req | C120528 |
| MBTSTDTL | Measurement, Test or Examination Detail | Char | Variable Qualifier | Perm | C174225 |
| MBCAT | Category | Char | Grouping Qualifier | Perm | — |
| MBSCAT | Subcategory | Char | Grouping Qualifier | Perm | — |
| MBORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| MBORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| MBSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp | — |
| MBSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| MBSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| MBRESCAT | Result Category | Char | Variable Qualifier | Perm | — |
| MBSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| MBREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| MBNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm | — |
| MBLOINC | LOINC Code | Char | Synonym Qualifier | Perm | — |
| MBSPEC | Specimen Material Type | Char | Record Qualifier | Perm | C78734 |
| MBSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| MBLOC | Specimen Collection Location | Char | Record Qualifier | Perm | C74456 |
| MBLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| MBDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| MBMETHOD | Method of Test or Examination | Char | Record Qualifier | Exp | C85492 |
| MBLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| MBBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| MBFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |
| MBDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| MBDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| MBDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |
| MBTPT | Planned Time Point Name | Char | Timing | Perm | — |
| MBTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| MBELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| MBTPTREF | Time Point Reference | Char | Timing | Perm | — |
| MBRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### MH — Medical History (Events)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| MHSEQ | Sequence Number | Num | Identifier | Req | — |
| MHGRPID | Group ID | Char | Identifier | Perm | — |
| MHREFID | Reference ID | Char | Identifier | Perm | — |
| MHSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| MHTERM | Reported Term for the Medical History | Char | Topic | Req | — |
| MHMODIFY | Modified Reported Term | Char | Synonym Qualifier | Perm | — |
| MHDECOD | Dictionary-Derived Term | Char | Synonym Qualifier | Perm | — |
| MHEVDTYP | Medical History Event Date Type | Char | Variable Qualifier | Perm | C124301 |
| MHCAT | Category for Medical History | Char | Grouping Qualifier | Perm | — |
| MHSCAT | Subcategory for Medical History | Char | Grouping Qualifier | Perm | — |
| MHPRESP | Medical History Event Pre-Specified | Char | Variable Qualifier | Perm | C66742 |
| MHOCCUR | Medical History Occurrence | Char | Record Qualifier | Perm | C66742 |
| MHSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| MHREASND | Reason Medical History Not Collected | Char | Record Qualifier | Perm | — |
| MHBODSYS | Body System or Organ Class | Char | Record Qualifier | Perm | — |
| MHDTC | Date/Time of History Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| MHSTDTC | Start Date/Time of Medical History Event | Char | Timing | Perm | ISO 8601 datetime or interval |
| MHENDTC | End Date/Time of Medical History Event | Char | Timing | Perm | ISO 8601 datetime or interval |
| MHDY | Study Day of History Collection | Num | Timing | Perm | — |
| MHENRF | End Relative to Reference Period | Char | Timing | Perm | C66728 |
| MHENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| MHENTPT | End Reference Time Point | Char | Timing | Perm | — |

### MI — Microscopic Findings (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| MISEQ | Sequence Number | Num | Identifier | Req | — |
| MIGRPID | Group ID | Char | Identifier | Perm | — |
| MIREFID | Reference ID | Char | Identifier | Perm | — |
| MISPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| MITESTCD | Microscopic Examination Short Name | Char | Topic | Req | C132263 |
| MITEST | Microscopic Examination Name | Char | Synonym Qualifier | Req | C132262 |
| MITSTDTL | Microscopic Examination Detail | Char | Record Qualifier | Perm | C125922 |
| MICAT | Category for Microscopic Finding | Char | Grouping Qualifier | Perm | — |
| MISCAT | Subcategory for Microscopic Finding | Char | Grouping Qualifier | Perm | — |
| MIORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| MIORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| MISTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| MISTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| MISTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| MIRESCAT | Result Category | Char | Variable Qualifier | Perm | — |
| MISTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| MIREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| MINAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm | — |
| MISPEC | Specimen Material Type | Char | Record Qualifier | Req | C78734 |
| MISPCCND | Specimen Condition | Char | Record Qualifier | Exp | C78733 |
| MILOC | Specimen Collection Location | Char | Record Qualifier | Perm | C74456 |
| MILAT | Specimen Laterality within Subject | Char | Variable Qualifier | Perm | C99073 |
| MIDIR | Specimen Directionality within Subject | Char | Variable Qualifier | Perm | C99074 |
| MIMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| MILOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| MIBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| MIEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| MIDTC | Date/Time of Specimen Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| MIDY | Study Day of Specimen Collection | Num | Timing | Perm | — |

### MK — Musculoskeletal System Findings (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| MKSEQ | Sequence Number | Num | Identifier | Req | — |
| MKGRPID | Group ID | Char | Identifier | Perm | — |
| MKREFID | Reference ID | Char | Identifier | Perm | — |
| MKSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| MKLNKID | Link ID | Char | Identifier | Perm | — |
| MKLNKGRP | Link Group ID | Char | Identifier | Perm | — |
| MKTESTCD | Short Name of Musculoskeletal Test | Char | Topic | Req | C127269 |
| MKTEST | Name of Musculoskeletal Test | Char | Synonym Qualifier | Req | C127270 |
| MKCAT | Category for Musculoskeletal Test | Char | Grouping Qualifier | Perm | — |
| MKSCAT | Subcategory for Musculoskeletal Test | Char | Grouping Qualifier | Perm | — |
| MKPOS | Position of Subject | Char | Record Qualifier | Perm | C71148 |
| MKORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| MKORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| MKSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| MKSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| MKSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| MKSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| MKREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| MKLOC | Location Used for the Measurement | Char | Record Qualifier | Exp | C74456 |
| MKLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| MKDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| MKMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| MKLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| MKBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| MKDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| MKEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| MKEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| MKDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| MKDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |
| MKTPT | Planned Time Point Name | Char | Timing | Perm | — |
| MKTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| MKELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| MKTPTREF | Time Point Reference | Char | Timing | Perm | — |
| MKRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### ML — Meal Data (Interventions)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| MLSEQ | Sequence Number | Num | Identifier | Req | — |
| MLGRPID | Group ID | Char | Identifier | Perm | — |
| MLSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| MLTRT | Name of Meal | Char | Topic | Req | — |
| MLCAT | Category for Meal | Char | Grouping Qualifier | Perm | — |
| MLSCAT | Subcategory for Meal | Char | Grouping Qualifier | Perm | — |
| MLPRESP | ML Pre-specified | Char | Variable Qualifier | Perm | C66742 |
| MLOCCUR | ML Occurrence | Char | Record Qualifier | Perm | C66742 |
| MLSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| MLREASND | Reason Meal Not Collected | Char | Record Qualifier | Perm | — |
| MLDOSE | Dose | Num | Record Qualifier | Perm | — |
| MLDOSTXT | Dose Description | Char | Record Qualifier | Perm | — |
| MLDOSU | Dose Units | Char | Variable Qualifier | Perm | C71620 |
| MLDOSFRM | Dose Form | Char | Variable Qualifier | Perm | C66726 |
| MLDTC | Date/Time of Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| MLSTDTC | Start Date/Time of Meal | Char | Timing | Perm | ISO 8601 datetime or interval |
| MLENDTC | End Date/Time of Meal | Char | Timing | Perm | ISO 8601 datetime or interval |
| MLDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |
| MLSTDY | Study Day of Start of Meal | Num | Timing | Perm | — |
| MLENDY | Study Day of End of Meal | Num | Timing | Perm | — |
| MLDUR | Duration of Meal | Char | Timing | Perm | ISO 8601 duration |
| MLTPT | Planned Time Point Name | Char | Timing | Perm | — |
| MLTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| MLELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| MLTPTREF | Time Point Reference | Char | Timing | Perm | — |
| MLRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |
| RELMIDS | Temporal Relation to Milestone Instance | Char | Timing | Perm | — |
| MIDSDTC | Disease Milestone Instance Date/Time | Char | Timing | Perm | ISO 8601 datetime or interval |

### MS — Microbiology Susceptibility (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| MSSEQ | Sequence Number | Num | Identifier | Req | — |
| MSGRPID | Group ID | Char | Identifier | Perm | — |
| MSREFID | Reference ID | Char | Identifier | Perm | — |
| MSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| MSLNKID | Link ID | Char | Identifier | Perm | — |
| MSTESTCD | Short Name of Assessment | Char | Topic | Req | C128688 |
| MSTEST | Name of Assessment | Char | Synonym Qualifier | Req | C128687 |
| MSAGENT | Agent Name | Char | Variable Qualifier | Exp | — |
| MSCONC | Agent Concentration | Num | Variable Qualifier | Perm | — |
| MSCONCU | Agent Concentration Units | Char | Variable Qualifier | Perm | C71620 |
| MSTSTDTL | Measurement, Test or Examination Detail | Char | Variable Qualifier | Perm | — |
| MSCAT | Category | Char | Grouping Qualifier | Perm | — |
| MSSCAT | Subcategory | Char | Grouping Qualifier | Perm | — |
| MSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| MSORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| MSSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp | — |
| MSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| MSSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| MSNRIND | Normal/Reference Range Indicator | Char | Variable Qualifier | Perm | C78736 |
| MSRESCAT | Result Category | Char | Variable Qualifier | Perm | C85495 |
| MSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| MSREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| MSXFN | External File Path | Char | Record Qualifier | Perm | — |
| MSNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm | — |
| MSLOINC | LOINC Code | Char | Synonym Qualifier | Perm | — |
| MSSPEC | Specimen Material Type | Char | Record Qualifier | Perm | C78734 |
| MSSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| MSLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |
| MSLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| MSDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| MSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| MSANMETH | Analysis Method | Char | Record Qualifier | Perm | — |
| MSLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| MSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| MSFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |
| MSDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| MSEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| MSEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| MSACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |
| MSLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Perm | — |
| MSULOQ | Upper Limit of Quantitation | Num | Variable Qualifier | Perm | — |
| MSREPNUM | Repetition Number | Num | Record Qualifier | Perm | — |
| MSDTC | Date/Time of Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| MSDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |
| MSDUR | Duration | Char | Timing | Perm | ISO 8601 duration |
| MSTPT | Planned Time Point Name | Char | Timing | Perm | — |
| MSTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| MSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| MSTPTREF | Time Point Reference | Char | Timing | Perm | — |
| MSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |
| MSEVLINT | Evaluation Interval | Char | Timing | Perm | ISO 8601 duration or interval |
| MSEVINTX | Evaluation Interval Text | Char | Timing | Perm | — |

### NV — Nervous System Findings (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| NVSEQ | Sequence Number | Num | Identifier | Req | — |
| NVGRPID | Group ID | Char | Identifier | Perm | — |
| NVREFID | Reference ID | Char | Identifier | Perm | — |
| NVSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| NVLNKID | Link ID | Char | Identifier | Perm | — |
| NVLNKGRP | Link Group | Char | Identifier | Perm | — |
| NVTESTCD | Short Name of Nervous System Test | Char | Topic | Req | C116104 |
| NVTEST | Name of Nervous System Test | Char | Synonym Qualifier | Req | C116103 |
| NVCAT | Category for Nervous System Test | Char | Grouping Qualifier | Perm | — |
| NVSCAT | Subcategory for Nervous System Test | Char | Grouping Qualifier | Perm | — |
| NVORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| NVORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| NVSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| NVSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| NVSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| NVSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| NVREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| NVLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |
| NVLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| NVDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| NVMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| NVLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| NVBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| NVDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| NVEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| NVEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| NVDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| NVDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |
| NVTPT | Planned Time Point Name | Char | Timing | Perm | — |
| NVTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| NVELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| NVTPTREF | Time Point Reference | Char | Timing | Perm | — |
| NVRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### OE — Ophthalmic Examinations (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| OESEQ | Sequence Number | Num | Identifier | Req | — |
| OEGRPID | Group ID | Char | Identifier | Perm | — |
| OELNKID | Link ID | Char | Identifier | Perm | — |
| OELNKGRP | Link Group | Char | Identifier | Perm | — |
| OETESTCD | Short Name of Ophthalmic Test or Exam | Char | Topic | Req | C117743 |
| OETEST | Name of Ophthalmic Test or Exam | Char | Synonym Qualifier | Req | C117742 |
| OETSTDTL | Ophthalmic Test or Exam Detail | Char | Variable Qualifier | Perm | — |
| OECAT | Category for Ophthalmic Test or Exam | Char | Grouping Qualifier | Perm | — |
| OESCAT | Subcategory for Ophthalmic Test or Exam | Char | Grouping Qualifier | Perm | — |
| OEORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| OEORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |
| OEORNRLO | Normal Range Lower Limit-Original Units | Char | Variable Qualifier | Perm | — |
| OEORNRHI | Normal Range Upper Limit-Original Units | Char | Variable Qualifier | Perm | — |
| OESTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| OESTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp | — |
| OESTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |
| OESTNRLO | Normal Range Lower Limit-Standard Units | Num | Variable Qualifier | Perm | — |
| OESTNRHI | Normal Range Upper Limit-Standard Units | Num | Variable Qualifier | Perm | — |
| OESTNRC | Normal Range for Character Results | Char | Variable Qualifier | Perm | — |
| OENRIND | Normal/Reference Range Indicator | Char | Variable Qualifier | Perm | C78736 |
| OERESCAT | Result Category | Char | Variable Qualifier | Perm | — |
| OESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| OEREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| OEXFN | External File Path | Char | Record Qualifier | Perm | — |
| OELOC | Location Used for the Measurement | Char | Record Qualifier | Exp | C74456 |
| OELAT | Laterality | Char | Variable Qualifier | Exp | C99073 |
| OEDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| OEPORTOT | Portion or Totality | Char | Variable Qualifier | Perm | C99075 |
| OEMETHOD | Method of Test or Examination | Char | Record Qualifier | Exp | C85492 |
| OELOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| OEBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| OEDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| OEEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| OEEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| OEACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |
| OEREPNUM | Repetition Number | Num | Record Qualifier | Perm | — |
| OEDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| OEDY | Study Day of Visit/Collection/Exam | Num | Timing | Exp | — |
| OETPT | Planned Time Point Name | Char | Timing | Perm | — |
| OETPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| OEELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| OETPTREF | Time Point Reference | Char | Timing | Perm | — |
| OERFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### OI — Non-host Organism Identifiers (Study Reference)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| OISEQ | Sequence Number | Num | Identifier | Req | — |
| OIPARMCD | Non-host Organism ID Element Short Name | Char | Topic | Req | C179591 |
| OIPARM | Non-host Organism ID Element Name | Char | Synonym Qualifier | Req | C179590 |
| OIVAL | Non-host Organism ID Element Value | Char | Result Qualifier | Req | — |

### PC — Pharmacokinetics Concentrations (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| PCSEQ | Sequence Number | Num | Identifier | Req | — |
| PCGRPID | Group ID | Char | Identifier | Perm | — |
| PCREFID | Reference ID | Char | Identifier | Perm | — |
| PCSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| PCTESTCD | Pharmacokinetic Test Short Name | Char | Topic | Req | — |
| PCTEST | Pharmacokinetic Test Name | Char | Synonym Qualifier | Req | — |
| PCCAT | Test Category | Char | Grouping Qualifier | Perm | — |
| PCSCAT | Test Subcategory | Char | Grouping Qualifier | Perm | — |
| PCORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| PCORRESU | Original Units | Char | Variable Qualifier | Exp | C85494 |
| PCSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| PCSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp | — |
| PCSTRESU | Standard Units | Char | Variable Qualifier | Exp | C85494 |
| PCSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| PCREASND | Reason Test Not Done | Char | Record Qualifier | Perm | — |
| PCNAM | Vendor Name | Char | Record Qualifier | Exp | — |
| PCSPEC | Specimen Material Type | Char | Record Qualifier | Exp | C78734 |
| PCSPCCND | Specimen Condition | Char | Record Qualifier | Perm | C78733 |
| PCMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| PCFAST | Fasting Status | Char | Record Qualifier | Perm | C66742 |
| PCDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| PCLLOQ | Lower Limit of Quantitation | Num | Variable Qualifier | Exp | — |
| PCULOQ | Upper Limit of Quantitation | Num | Variable Qualifier | Perm | — |
| PCDTC | Date/Time of Specimen Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| PCENDTC | End Date/Time of Specimen Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| PCDY | Actual Study Day of Specimen Collection | Num | Timing | Perm | — |
| PCENDY | Study Day of End of Observation | Num | Timing | Perm | — |
| PCTPT | Planned Time Point Name | Char | Timing | Perm | — |
| PCTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| PCELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| PCTPTREF | Time Point Reference | Char | Timing | Perm | — |
| PCRFTDTC | Date/Time of Reference Point | Char | Timing | Perm | ISO 8601 datetime or interval |
| PCEVLINT | Evaluation Interval | Char | Timing | Perm | ISO 8601 duration or interval |

### PE — Physical Examination (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| PESEQ | Sequence Number | Num | Identifier | Req | — |
| PEGRPID | Group ID | Char | Identifier | Perm | — |
| PESPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| PETESTCD | Body System Examined Short Name | Char | Topic | Req | — |
| PETEST | Body System Examined | Char | Synonym Qualifier | Req | — |
| PEMODIFY | Modified Reported Term | Char | Synonym Qualifier | Perm | — |
| PECAT | Category for Examination | Char | Grouping Qualifier | Perm | — |
| PESCAT | Subcategory for Examination | Char | Grouping Qualifier | Perm | — |
| PEBODSYS | Body System or Organ Class | Char | Record Qualifier | Perm | — |
| PEORRES | Verbatim Examination Finding | Char | Result Qualifier | Exp | — |
| PEORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| PESTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| PESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| PEREASND | Reason Not Examined | Char | Record Qualifier | Perm | — |
| PELOC | Location of Physical Exam Finding | Char | Record Qualifier | Perm | C74456 |
| PELAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| PEMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| PELOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| PEBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| PEEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| PEDTC | Date/Time of Examination | Char | Timing | Exp | ISO 8601 datetime or interval |
| PEDY | Study Day of Examination | Num | Timing | Perm | — |

### PP — Pharmacokinetics Parameters (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| PPSEQ | Sequence Number | Num | Identifier | Req | — |
| PPGRPID | Group ID | Char | Identifier | Perm | — |
| PPTESTCD | Parameter Short Name | Char | Topic | Req | C85839 |
| PPTEST | Parameter Name | Char | Synonym Qualifier | Req | C85493 |
| PPCAT | Parameter Category | Char | Grouping Qualifier | Exp | — |
| PPSCAT | Parameter Subcategory | Char | Grouping Qualifier | Perm | — |
| PPORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| PPORRESU | Original Units | Char | Variable Qualifier | Exp | C85494; C128684; C128683; C128685; C128686 |
| PPSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| PPSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp | — |
| PPSTRESU | Standard Units | Char | Variable Qualifier | Exp | C85494; C128684; C128683; C128685; C128686 |
| PPSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| PPREASND | Reason Parameter Not Calculated | Char | Record Qualifier | Perm | — |
| PPSPEC | Specimen Material Type | Char | Record Qualifier | Exp | C78734 |
| PPANMETH | Analysis Method | Char | Record Qualifier | Perm | C172330 |
| PPDTC | Date/Time of Parameter Calculations | Char | Timing | Perm | ISO 8601 datetime or interval |
| PPDY | Study Day of Parameter Calculations | Num | Timing | Perm | — |
| PPTPTREF | Time Point Reference | Char | Timing | Perm | — |
| PPRFTDTC | Date/Time of Reference Point | Char | Timing | Exp | ISO 8601 datetime or interval |
| PPSTINT | Planned Start of Assessment Interval | Char | Timing | Perm | ISO 8601 duration |
| PPENINT | Planned End of Assessment Interval | Char | Timing | Perm | ISO 8601 duration |

### PR — Procedures (Interventions)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| PRSEQ | Sequence Number | Num | Identifier | Req | — |
| PRGRPID | Group ID | Char | Identifier | Perm | — |
| PRSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| PRLNKID | Link ID | Char | Identifier | Perm | — |
| PRLNKGRP | Link Group ID | Char | Identifier | Perm | — |
| PRTRT | Reported Name of Procedure | Char | Topic | Req | — |
| PRDECOD | Standardized Procedure Name | Char | Synonym Qualifier | Perm | C101858 |
| PRCAT | Category | Char | Grouping Qualifier | Perm | — |
| PRSCAT | Subcategory | Char | Grouping Qualifier | Perm | — |
| PRPRESP | Pre-specified | Char | Variable Qualifier | Perm | C66742 |
| PROCCUR | Occurrence | Char | Record Qualifier | Perm | C66742 |
| PRINDC | Indication | Char | Record Qualifier | Perm | — |
| PRDOSE | Dose | Num | Record Qualifier | Perm | — |
| PRDOSTXT | Dose Description | Char | Record Qualifier | Perm | — |
| PRDOSU | Dose Units | Char | Variable Qualifier | Perm | C71620 |
| PRDOSFRM | Dose Form | Char | Variable Qualifier | Perm | C66726 |
| PRDOSFRQ | Dosing Frequency per Interval | Char | Record Qualifier | Perm | C71113 |
| PRDOSRGM | Intended Dose Regimen | Char | Record Qualifier | Perm | — |
| PRROUTE | Route of Administration | Char | Variable Qualifier | Perm | C66729 |
| PRLOC | Location of Procedure | Char | Record Qualifier | Perm | C74456 |
| PRLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| PRDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| PRPORTOT | Portion or Totality | Char | Variable Qualifier | Perm | C99075 |
| PRSTDTC | Start Date/Time of Procedure | Char | Timing | Exp | ISO 8601 datetime or interval |
| PRENDTC | End Date/Time of Procedure | Char | Timing | Perm | ISO 8601 datetime or interval |
| PRSTDY | Study Day of Start of Procedure | Num | Timing | Perm | — |
| PRENDY | Study Day of End of Procedure | Num | Timing | Perm | — |
| PRDUR | Duration of Procedure | Char | Timing | Perm | ISO 8601 duration |
| PRTPT | Planned Time Point Name | Char | Timing | Perm | — |
| PRTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| PRELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| PRTPTREF | Time Point Reference | Char | Timing | Perm | — |
| PRRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |
| PRSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| PRSTTPT | Start Reference Time Point | Char | Timing | Perm | — |
| PRENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| PRENTPT | End Reference Time Point | Char | Timing | Perm | — |

### QS — Questionnaires (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| QSSEQ | Sequence Number | Num | Identifier | Req | — |
| QSGRPID | Group ID | Char | Identifier | Perm | — |
| QSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| QSTESTCD | Question Short Name | Char | Topic | Req | — |
| QSTEST | Question Name | Char | Synonym Qualifier | Req | — |
| QSCAT | Category of Question | Char | Grouping Qualifier | Req | C100129 |
| QSSCAT | Subcategory for Question | Char | Grouping Qualifier | Perm | — |
| QSORRES | Finding in Original Units | Char | Result Qualifier | Exp | — |
| QSORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| QSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| QSSTRESN | Numeric Finding in Standard Units | Num | Result Qualifier | Perm | — |
| QSSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| QSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| QSREASND | Reason Not Performed | Char | Record Qualifier | Perm | — |
| QSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C158113 |
| QSLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| QSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| QSDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| QSDTC | Date/Time of Finding | Char | Timing | Exp | ISO 8601 datetime or interval |
| QSDY | Study Day of Finding | Num | Timing | Perm | — |
| QSTPT | Planned Time Point Name | Char | Timing | Perm | — |
| QSTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| QSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| QSTPTREF | Time Point Reference | Char | Timing | Perm | — |
| QSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |
| QSEVLINT | Evaluation Interval | Char | Timing | Perm | ISO 8601 duration or interval |
| QSEVINTX | Evaluation Interval Text | Char | Timing | Perm | — |

### RE — Respiratory System Findings (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| RESEQ | Sequence Number | Num | Identifier | Req | — |
| REGRPID | Group ID | Char | Identifier | Perm | — |
| REREFID | Reference ID | Char | Identifier | Perm | — |
| RESPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| RELNKID | Link ID | Char | Identifier | Perm | — |
| RELNKGRP | Link Group | Char | Identifier | Perm | — |
| RETESTCD | Short Name of Respiratory Test | Char | Topic | Req | C111106 |
| RETEST | Name of Respiratory Test | Char | Synonym Qualifier | Req | C111107 |
| RECAT | Category for Respiratory Test | Char | Grouping Qualifier | Perm | — |
| RESCAT | Subcategory for Respiratory Test | Char | Grouping Qualifier | Perm | — |
| REPOS | Position of Subject During Observation | Char | Record Qualifier | Perm | C71148 |
| REORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| REORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| REORREF | Reference Result in Original Units | Char | Variable Qualifier | Perm | — |
| RESTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| RESTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| RESTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| RESTREFC | Character Reference Result | Char | Variable Qualifier | Perm | — |
| RESTREFN | Numeric Reference Result in Std Units | Num | Variable Qualifier | Perm | — |
| RESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| REREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| RELOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |
| RELAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| REDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| REMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| RELOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| REBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| REDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| REEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| REEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| REREPNUM | Repetition Number | Num | Record Qualifier | Perm | — |
| REDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| REDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |
| RETPT | Planned Time Point Name | Char | Timing | Perm | — |
| RETPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| REELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| RETPTREF | Time Point Reference | Char | Timing | Perm | — |
| RERFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### RELREC — Related Records (Relationship)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| RELTYPE | Relationship Type | Char | Record Qualifier | Exp | C78737 |
| RELID | Relationship Identifier | Char | Record Qualifier | Req | — |

### RELSPEC — Related Specimens (Relationship)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| REFID | Specimen ID | Char | Identifier | Req | — |
| SPEC | Specimen Type | Char | Variable Qualifier | Perm | C78734; C111114 |
| PARENT | Specimen Parent | Char | Identifier | Exp | — |
| LEVEL | Specimen Level | Num | Variable Qualifier | Req | — |

### RELSUB — Related Subjects (Relationship)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| POOLID | Pool Identifier | Char | Identifier | Perm | — |
| RSUBJID | Related Subject or Pool Identifier | Char | Identifier | Req | — |
| SREL | Subject Relationship | Char | Record Qualifier | Req | C100130 |

### RP — Reproductive System Findings (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| RPSEQ | Sequence Number | Num | Identifier | Req | — |
| RPGRPID | Group ID | Char | Identifier | Perm | — |
| RPREFID | Reference ID | Char | Identifier | Perm | — |
| RPSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| RPLNKID | Link ID | Char | Identifier | Perm | — |
| RPLNKGRP | Link Group ID | Char | Identifier | Perm | — |
| RPTESTCD | Short Name of Reproductive Test | Char | Topic | Req | C106479 |
| RPTEST | Name of Reproductive Test | Char | Synonym Qualifier | Req | C106478 |
| RPCAT | Category for Reproductive Test | Char | Grouping Qualifier | Perm | — |
| RPSCAT | Subcategory for Reproductive Test | Char | Grouping Qualifier | Perm | — |
| RPORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| RPORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| RPSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| RPSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| RPSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| RPSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| RPREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| RPLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| RPBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| RPDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| RPDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| RPDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |
| RPDUR | Duration | Char | Timing | Perm | ISO 8601 duration |
| RPTPT | Planned Time Point Name | Char | Timing | Perm | — |
| RPTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| RPELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| RPTPTREF | Time Point Reference | Char | Timing | Perm | — |
| RPRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### RS — Disease Response and Clin Classification (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| RSSEQ | Sequence Number | Num | Identifier | Req | — |
| RSGRPID | Group ID | Char | Identifier | Perm | — |
| RSREFID | Reference ID | Char | Identifier | Perm | — |
| RSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| RSLNKID | Link ID | Char | Identifier | Perm | — |
| RSLNKGRP | Link Group ID | Char | Identifier | Perm | — |
| RSTESTCD | Assessment Short Name | Char | Topic | Req | C96782 |
| RSTEST | Assessment Name | Char | Synonym Qualifier | Req | C96781 |
| RSCAT | Category for Assessment | Char | Grouping Qualifier | Exp | C124298; C118971 |
| RSSCAT | Subcategory | Char | Grouping Qualifier | Perm | — |
| RSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| RSORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| RSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C96785 |
| RSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| RSSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| RSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| RSREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| RSNAM | Vendor Name | Char | Record Qualifier | Perm | — |
| RSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C158113 |
| RSLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| RSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| RSDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| RSEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| RSEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| RSACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |
| RSDTC | Date/Time of Assessment | Char | Timing | Exp | ISO 8601 datetime or interval |
| RSDY | Study Day of Assessment | Num | Timing | Perm | — |
| RSTPT | Planned Time Point Name | Char | Timing | Perm | — |
| RSTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| RSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| RSTPTREF | Time Point Reference | Char | Timing | Perm | — |
| RSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |
| RSEVLINT | Evaluation Interval | Char | Timing | Perm | ISO 8601 duration or interval |
| RSEVINTX | Evaluation Interval Text | Char | Timing | Perm | — |
| RSSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| RSSTTPT | Start Reference Time Point | Char | Timing | Perm | — |
| RSENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| RSENTPT | End Reference Time Point | Char | Timing | Perm | — |

### SC — Subject Characteristics (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| SCSEQ | Sequence Number | Num | Identifier | Req | — |
| SCGRPID | Group ID | Char | Identifier | Perm | — |
| SCSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| SCTESTCD | Subject Characteristic Short Name | Char | Topic | Req | C74559 |
| SCTEST | Subject Characteristic | Char | Synonym Qualifier | Req | C103330 |
| SCCAT | Category for Subject Characteristic | Char | Grouping Qualifier | Perm | — |
| SCSCAT | Subcategory for Subject Characteristic | Char | Grouping Qualifier | Perm | — |
| SCORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| SCORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| SCSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| SCSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| SCSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| SCSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| SCREASND | Reason Not Performed | Char | Record Qualifier | Perm | — |
| SCDTC | Date/Time of Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| SCDY | Study Day of Examination | Num | Timing | Perm | — |

### SE — Subject Elements (Special-Purpose)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| SESEQ | Sequence Number | Num | Identifier | Req | — |
| SESTDTC | Start Date/Time of Element | Char | Timing | Req | ISO 8601 datetime or interval |
| SEENDTC | End Date/Time of Element | Char | Timing | Exp | ISO 8601 datetime or interval |
| SESTDY | Study Day of Start of Element | Num | Timing | Perm | — |
| SEENDY | Study Day of End of Element | Num | Timing | Perm | — |
| SEUPDES | Description of Unplanned Element | Char | Synonym Qualifier | Perm | — |

### SM — Subject Disease Milestones (Special-Purpose)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| SMSEQ | Sequence Number | Num | Identifier | Req | — |
| SMSTDTC | Start Date/Time of Milestone | Char | Timing | Exp | ISO 8601 datetime or interval |
| SMENDTC | End Date/Time of Milestone | Char | Timing | Exp | ISO 8601 datetime or interval |
| SMSTDY | Study Day of Start of Milestone | Num | Timing | Exp | — |
| SMENDY | Study Day of End of Milestone | Num | Timing | Exp | — |

### SR — Skin Response (Findings About)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| SRSEQ | Sequence Number | Num | Identifier | Req | — |
| SRGRPID | Group ID | Char | Identifier | Perm | — |
| SRREFID | Reference ID | Char | Identifier | Perm | — |
| SRSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| SRTESTCD | Skin Response Test or Exam Short Name | Char | Topic | Req | C112024 |
| SRTEST | Skin Response Test or Examination Name | Char | Synonym Qualifier | Req | C112023 |
| SROBJ | Object of the Observation | Char | Record Qualifier | Req | — |
| SRCAT | Category for Test | Char | Grouping Qualifier | Perm | — |
| SRSCAT | Subcategory for Test | Char | Grouping Qualifier | Perm | — |
| SRORRES | Results or Findings in Original Units | Char | Result Qualifier | Exp | — |
| SRORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |
| SRSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| SRSTRESN | Numeric Results/Findings in Std. Units | Num | Result Qualifier | Exp | — |
| SRSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |
| SRSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| SRREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| SRNAM | Vendor Name | Char | Record Qualifier | Perm | — |
| SRSPEC | Specimen Type | Char | Record Qualifier | Perm | C78734 |
| SRLOC | Location Used for Measurement | Char | Record Qualifier | Perm | C74456 |
| SRLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| SRMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| SRLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| SRBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| SREVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| SRDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| SRDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |
| SRTPT | Planned Time Point Name | Char | Timing | Perm | — |
| SRTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| SRELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| SRTPTREF | Time Point Reference | Char | Timing | Perm | — |
| SRRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### SS — Subject Status (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| SSSEQ | Sequence Number | Num | Identifier | Req | — |
| SSGRPID | Group ID | Char | Identifier | Perm | — |
| SSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| SSTESTCD | Status Short Name | Char | Topic | Req | C124305 |
| SSTEST | Status Name | Char | Synonym Qualifier | Req | C124306 |
| SSCAT | Category for Assessment | Char | Grouping Qualifier | Perm | — |
| SSSCAT | Subcategory for Assessment | Char | Grouping Qualifier | Perm | — |
| SSORRES | Result or Finding Original Result | Char | Result Qualifier | Exp | — |
| SSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C124304 |
| SSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| SSREASND | Reason Assessment Not Performed | Char | Record Qualifier | Perm | — |
| SSEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| SSDTC | Date/Time of Assessment | Char | Timing | Exp | ISO 8601 datetime or interval |
| SSDY | Study Day of Assessment | Num | Timing | Perm | — |

### SU — Substance Use (Interventions)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| SUSEQ | Sequence Number | Num | Identifier | Req | — |
| SUGRPID | Group ID | Char | Identifier | Perm | — |
| SUSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| SUTRT | Reported Name of Substance | Char | Topic | Req | — |
| SUMODIFY | Modified Substance Name | Char | Synonym Qualifier | Perm | — |
| SUDECOD | Standardized Substance Name | Char | Synonym Qualifier | Perm | — |
| SUCAT | Category for Substance Use | Char | Grouping Qualifier | Perm | — |
| SUSCAT | Subcategory for Substance Use | Char | Grouping Qualifier | Perm | — |
| SUPRESP | SU Pre-Specified | Char | Variable Qualifier | Perm | C66742 |
| SUOCCUR | SU Occurrence | Char | Record Qualifier | Perm | C66742 |
| SUSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| SUREASND | Reason Substance Use Not Collected | Char | Record Qualifier | Perm | — |
| SUCLAS | Substance Use Class | Char | Variable Qualifier | Perm | — |
| SUCLASCD | Substance Use Class Code | Char | Variable Qualifier | Perm | — |
| SUDOSE | Substance Use Consumption | Num | Record Qualifier | Perm | — |
| SUDOSTXT | Substance Use Consumption Text | Char | Record Qualifier | Perm | — |
| SUDOSU | Consumption Units | Char | Variable Qualifier | Perm | C71620 |
| SUDOSFRM | Dose Form | Char | Variable Qualifier | Perm | C66726 |
| SUDOSFRQ | Use Frequency Per Interval | Char | Variable Qualifier | Perm | C71113 |
| SUDOSTOT | Total Daily Consumption | Num | Record Qualifier | Perm | — |
| SUROUTE | Route of Administration | Char | Variable Qualifier | Perm | C66729 |
| SUSTDTC | Start Date/Time of Substance Use | Char | Timing | Perm | ISO 8601 datetime or interval |
| SUENDTC | End Date/Time of Substance Use | Char | Timing | Perm | ISO 8601 datetime or interval |
| SUSTDY | Study Day of Start of Substance Use | Num | Timing | Perm | — |
| SUENDY | Study Day of End of Substance Use | Num | Timing | Perm | — |
| SUDUR | Duration of Substance Use | Char | Timing | Perm | ISO 8601 duration |
| SUSTRF | Start Relative to Reference Period | Char | Timing | Perm | C66728 |
| SUENRF | End Relative to Reference Period | Char | Timing | Perm | C66728 |
| SUSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| SUSTTPT | Start Reference Time Point | Char | Timing | Perm | — |
| SUENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| SUENTPT | End Reference Time Point | Char | Timing | Perm | — |

### SUPPQUAL — Supplemental Qualifiers for [domain name] (Relationship)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| QNAM | Qualifier Variable Name | Char | Topic | Req | — |
| QLABEL | Qualifier Variable Label | Char | Synonym Qualifier | Req | — |
| QVAL | Data Value | Char | Result Qualifier | Req | — |
| QORIG | Origin | Char | Record Qualifier | Req | — |
| QEVAL | Evaluator | Char | Record Qualifier | Exp | C78735 |

### SV — Subject Visits (Special-Purpose)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| SVPRESP | Pre-specified | Char | Variable Qualifier | Exp | C66742 |
| SVOCCUR | Occurrence | Char | Record Qualifier | Exp | C66742 |
| SVREASOC | Reason for Occur Value | Char | Record Qualifier | Perm | — |
| SVCNTMOD | Contact Mode | Char | Record Qualifier | Perm | C171445 |
| SVEPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier | Perm | C66742 |
| SVSTDTC | Start Date/Time of Observation | Char | Timing | Exp | ISO 8601 datetime or interval |
| SVENDTC | End Date/Time of Observation | Char | Timing | Exp | ISO 8601 datetime or interval |
| SVSTDY | Study Day of Start of Observation | Num | Timing | Perm | — |
| SVENDY | Study Day of End of Observation | Num | Timing | Perm | — |
| SVUPDES | Description of Unplanned Visit | Char | Record Qualifier | Perm | — |

### TA — Trial Arms (Trial Design)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| TABRANCH | Branch | Char | Rule | Exp | — |
| TATRANS | Transition Rule | Char | Rule | Exp | — |

### TD — Trial Disease Assessments (Trial Design)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| TDORDER | Sequence of Planned Assessment Schedule | Num | Timing | Req | — |
| TDANCVAR | Anchor Variable Name | Char | Timing | Req | — |
| TDSTOFF | Offset from the Anchor | Char | Timing | Req | ISO 8601 duration |
| TDTGTPAI | Planned Assessment Interval | Char | Timing | Req | ISO 8601 duration |
| TDMINPAI | Planned Assessment Interval Minimum | Char | Timing | Req | ISO 8601 duration |
| TDMAXPAI | Planned Assessment Interval Maximum | Char | Timing | Req | ISO 8601 duration |
| TDNUMRPT | Maximum Number of Actual Assessments | Num | Record Qualifier | Req | — |

### TE — Trial Elements (Trial Design)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| TESTRL | Rule for Start of Element | Char | Rule | Req | — |
| TEENRL | Rule for End of Element | Char | Rule | Perm | — |
| TEDUR | Planned Duration of Element | Char | Timing | Perm | ISO 8601 duration |

### TI — Trial Inclusion/Exclusion Criteria (Trial Design)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| TIRL | Inclusion/Exclusion Criterion Rule | Char | Rule | Perm | — |
| TIVERS | Protocol Criteria Versions | Char | Record Qualifier | Perm | — |

### TM — Trial Disease Milestones (Trial Design)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| TMDEF | Disease Milestone Definition | Char | Variable Qualifier | Req | — |
| TMRPT | Disease Milestone Repetition Indicator | Char | Record Qualifier | Req | C66742 |

### TR — Tumor/Lesion Results (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| TRSEQ | Sequence Number | Num | Identifier | Req | — |
| TRGRPID | Group ID | Char | Identifier | Perm | — |
| TRREFID | Reference ID | Char | Identifier | Perm | — |
| TRSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| TRLNKID | Link ID | Char | Identifier | Exp | — |
| TRLNKGRP | Link Group | Char | Identifier | Perm | — |
| TRTESTCD | Tumor/Lesion Assessment Short Name | Char | Topic | Req | C96779 |
| TRTEST | Tumor/Lesion Assessment Test Name | Char | Synonym Qualifier | Req | C96778 |
| TRORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| TRORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |
| TRSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C124309 |
| TRSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp | — |
| TRSTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |
| TRSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| TRREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| TRNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm | — |
| TRMETHOD | Method Used to Identify the Tumor/Lesion | Char | Record Qualifier | Exp | C85492 |
| TRLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| TRBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| TREVAL | Evaluator | Char | Record Qualifier | Exp | C78735 |
| TREVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| TRACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |
| TRDTC | Date/Time of Tumor/Lesion Measurement | Char | Timing | Exp | ISO 8601 datetime or interval |
| TRDY | Study Day of Tumor/Lesion Measurement | Num | Timing | Perm | — |

### TS — Trial Summary (Trial Design)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| TSSEQ | Sequence Number | Num | Identifier | Req | — |
| TSGRPID | Group ID | Char | Identifier | Perm | — |
| TSPARMCD | Trial Summary Parameter Short Name | Char | Topic | Req | C66738 |
| TSPARM | Trial Summary Parameter | Char | Synonym Qualifier | Req | C67152 |
| TSVAL | Parameter Value | Char | Result Qualifier | Exp | — |
| TSVALNF | Parameter Value Null Flavor | Char | Result Qualifier | Perm | ISO 21090 NullFlavor |
| TSVALCD | Parameter Value Code | Char | Result Qualifier | Exp | — |
| TSVCDREF | Name of the Reference Terminology | Char | Result Qualifier | Exp | C66788 |
| TSVCDVER | Version of the Reference Terminology | Char | Result Qualifier | Exp | — |

### TU — Tumor/Lesion Identification (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| TUSEQ | Sequence Number | Num | Identifier | Req | — |
| TUGRPID | Group ID | Char | Identifier | Perm | — |
| TUREFID | Reference ID | Char | Identifier | Perm | — |
| TUSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| TULNKID | Link ID | Char | Identifier | Exp | — |
| TULNKGRP | Link Group ID | Char | Identifier | Perm | — |
| TUTESTCD | Tumor/Lesion ID Short Name | Char | Topic | Req | C96784 |
| TUTEST | Tumor/Lesion ID Test Name | Char | Synonym Qualifier | Req | C96783 |
| TUORRES | Tumor/Lesion ID Result | Char | Result Qualifier | Exp | — |
| TUSTRESC | Tumor/Lesion ID Result Std. Format | Char | Result Qualifier | Exp | C123650 |
| TUNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm | — |
| TULOC | Location of the Tumor/Lesion | Char | Record Qualifier | Exp | C74456 |
| TULAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| TUDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| TUPORTOT | Portion or Totality | Char | Variable Qualifier | Perm | C99075 |
| TUMETHOD | Method of Identification | Char | Record Qualifier | Exp | C85492 |
| TULOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| TUBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| TUEVAL | Evaluator | Char | Record Qualifier | Exp | C78735 |
| TUEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| TUACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |
| TUDTC | Date/Time of Tumor/Lesion Identification | Char | Timing | Exp | ISO 8601 datetime or interval |
| TUDY | Study Day of Tumor/Lesion Identification | Num | Timing | Perm | — |

### TV — Trial Visits (Trial Design)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| TVSTRL | Visit Start Rule | Char | Rule | Req | — |
| TVENRL | Visit End Rule | Char | Rule | Perm | — |

### UR — Urinary System Findings (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| URSEQ | Sequence Number | Num | Identifier | Req | — |
| URGRPID | Group ID | Char | Identifier | Perm | — |
| URREFID | Reference ID | Char | Identifier | Perm | — |
| URSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| URLNKID | Link ID | Char | Identifier | Perm | — |
| URLNKGRP | Link Group ID | Char | Identifier | Perm | — |
| URTESTCD | Short Name of Urinary Test | Char | Topic | Req | C129942 |
| URTEST | Name of Urinary Test | Char | Synonym Qualifier | Req | C129941 |
| URTSTDTL | Urinary Test Detail | Char | Variable Qualifier | Perm | — |
| URCAT | Category for Urinary Test | Char | Grouping Qualifier | Perm | — |
| URSCAT | Subcategory for Urinary Test | Char | Grouping Qualifier | Perm | — |
| URORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| URORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| URSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| URSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm | — |
| URSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| URRESCAT | Result Category | Char | Variable Qualifier | Perm | — |
| URSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| URREASND | Reason Not Done | Char | Record Qualifier | Perm | — |
| URLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |
| URLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| URDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| URMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| URLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| URBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| URDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| UREVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| UREVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| URDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| URDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm | — |
| URTPT | Planned Time Point Name | Char | Timing | Perm | — |
| URTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| URELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| URTPTREF | Time Point Reference | Char | Timing | Perm | — |
| URRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

### VS — Vital Signs (Findings)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| VSSEQ | Sequence Number | Num | Identifier | Req | — |
| VSGRPID | Group ID | Char | Identifier | Perm | — |
| VSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm | — |
| VSTESTCD | Vital Signs Test Short Name | Char | Topic | Req | C66741 |
| VSTEST | Vital Signs Test Name | Char | Synonym Qualifier | Req | C67153 |
| VSCAT | Category for Vital Signs | Char | Grouping Qualifier | Perm | — |
| VSSCAT | Subcategory for Vital Signs | Char | Grouping Qualifier | Perm | — |
| VSPOS | Vital Signs Position of Subject | Char | Record Qualifier | Perm | C71148 |
| VSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp | — |
| VSORRESU | Original Units | Char | Variable Qualifier | Exp | C66770 |
| VSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | — |
| VSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp | — |
| VSSTRESU | Standard Units | Char | Variable Qualifier | Exp | C66770 |
| VSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| VSREASND | Reason Not Performed | Char | Record Qualifier | Perm | — |
| VSLOC | Location of Vital Signs Measurement | Char | Record Qualifier | Perm | C74456 |
| VSLAT | Laterality | Char | Result Qualifier | Perm | C99073 |
| VSLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| VSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| VSDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| VSTOX | Toxicity | Char | Variable Qualifier | Perm | — |
| VSTOXGR | Standard Toxicity Grade | Char | Record Qualifier | Perm | — |
| VSCLSIG | Clinically Significant, Collected | Char | Record Qualifier | Perm | C66742 |
| VSDTC | Date/Time of Measurements | Char | Timing | Exp | ISO 8601 datetime or interval |
| VSDY | Study Day of Vital Signs | Num | Timing | Perm | — |
| VSTPT | Planned Time Point Name | Char | Timing | Perm | — |
| VSTPTNUM | Planned Time Point Number | Num | Timing | Perm | — |
| VSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| VSTPTREF | Time Point Reference | Char | Timing | Perm | — |
| VSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

---

## 三、CDISC Controlled Terminology 交叉引用（共 135 个 CT Code）

| CT Code | 引用数 | 引用此 CT 的变量 (域.变量名) |
|---------|--------|---------------------------|
| C100129 | 1 | QS.QSCAT |
| C100130 | 1 | RELSUB.SREL |
| C101832 | 1 | FA.FATESTCD |
| C101833 | 1 | FA.FATEST |
| C101846 | 1 | CV.CVTEST |
| C101847 | 1 | CV.CVTESTCD |
| C101858 | 1 | PR.PRDECOD |
| C102580 | 1 | LB.LBSTRESC |
| C103330 | 1 | SC.SCTEST |
| C106478 | 1 | RP.RPTEST |
| C106479 | 1 | RP.RPTESTCD |
| C111106 | 1 | RE.RETESTCD |
| C111107 | 1 | RE.RETEST |
| C111110 | 1 | AE.AEACNDEV |
| C111114 | 1 | GF.GFSPEC |
| C112023 | 1 | SR.SRTEST |
| C112024 | 1 | SR.SRTESTCD |
| C115304 | 1 | FT.FTCAT |
| C116103 | 1 | NV.NVTEST |
| C116104 | 1 | NV.NVTESTCD |
| C116107 | 1 | DD.DDTEST |
| C116108 | 1 | DD.DDTESTCD |
| C117742 | 1 | OE.OETEST |
| C117743 | 1 | OE.OETESTCD |
| C119013 | 1 | OE.FOCID |
| C120525 | 1 | IS.ISTESTCD |
| C120526 | 1 | IS.ISTEST |
| C120527 | 1 | MB.MBTESTCD |
| C120528 | 1 | MB.MBTEST |
| C123650 | 1 | TU.TUSTRESC |
| C124297 | 1 | BE.BEDECOD |
| C124298 | 1 | RS.RSCAT |
| C124299 | 1 | BS.BSTEST |
| C124300 | 1 | BS.BSTESTCD |
| C124301 | 1 | MH.MHEVDTYP |
| C124304 | 1 | SS.SSSTRESC |
| C124305 | 1 | SS.SSTESTCD |
| C124306 | 1 | SS.SSTEST |
| C124309 | 1 | TR.TRSTRESC |
| C125922 | 1 | MI.MITSTDTL |
| C125923 | 1 | EC.ECMOOD |
| C127269 | 1 | MK.MKTESTCD |
| C127270 | 1 | MK.MKTEST |
| C128687 | 1 | MS.MSTEST |
| C128688 | 1 | MS.MSTESTCD |
| C129941 | 1 | UR.URTEST |
| C129942 | 1 | UR.URTESTCD |
| C132262 | 1 | MI.MITEST |
| C132263 | 1 | MI.MITESTCD |
| C142179 | 1 | DM.ARMNRS |
| C158113 | 3 | FT.FTMETHOD, QS.QSMETHOD, RS.RSMETHOD |
| C160922 | 1 | LB.LBANMETH |
| C165643 | 1 | CE.CESEV |
| C170443 | 1 | DS.DSSCAT |
| C171444 | 1 | HO.HODECOD |
| C171445 | 1 | SV.SVCNTMOD |
| C172330 | 1 | PP.PPANMETH |
| C174225 | 1 | MB.MBTSTDTL |
| C177908 | 2 | CP.CPCOLSRT, LB.LBCOLSRT |
| C177910 | 2 | CP.CPRESSCL, LB.LBRESSCL |
| C179588 | 2 | CP.CPRESTYP, LB.LBRESTYP |
| C179589 | 1 | LB.LBTMTHSN |
| C179590 | 1 | OI.OIPARM |
| C179591 | 1 | OI.OIPARMCD |
| C181170 | 2 | IS.ISTSTOPO, LB.LBTSTOPO |
| C181171 | 1 | CP.CPCAT |
| C181172 | 1 | CP.CPCELSTA |
| C181173 | 1 | CP.CPTESTCD |
| C181174 | 1 | CP.CPTEST |
| C181175 | 3 | CP.CPTSTCND, IS.ISTSTCND, LB.LBTSTCND |
| C181176 | 1 | GF.GFSYMTYP |
| C181177 | 1 | GF.GFINHERT |
| C181178 | 1 | GF.GFTESTCD |
| C181179 | 1 | GF.GFTEST |
| C181180 | 1 | GF.GFTSTDTL |
| C181181 | 1 | GF.GFANMETH |
| C65047 | 1 | LB.LBTESTCD |
| C66726 | 7 | AG.AGDOSFRM, CM.CMDOSFRM, EC.ECDOSFRM, EX.EXDOSFRM, ML.MLDOSFRM, PR.PRDOSFRM, SU.SUDOSFRM |
| C66727 | 1 | DS.DSDECOD |
| C66728 | 26 | AE.AEENRF, AE.AEENRTPT, AG.AGENRF, AG.AGENRTPT, AG.AGSTRF, AG.AGSTRTPT, CE.CEENRF, CE.CEENRTPT, CE.CESTRF, CE.CESTRTPT, CM.CMENRF, CM.CMENRTPT, CM.CMSTRF, CM.CMSTRTPT, HO.HOENRTPT ... (共 26 个) |
| C66729 | 6 | AG.AGROUTE, CM.CMROUTE, EC.ECROUTE, EX.EXROUTE, PR.PRROUTE, SU.SUROUTE |
| C66731 | 1 | DM.SEX |
| C66734 | 3 | CO.RDOMAIN, RELREC.RDOMAIN, SUPPQUAL.RDOMAIN |
| C66738 | 1 | TS.TSPARMCD |
| C66741 | 1 | VS.VSTESTCD |
| C66742 | 123 | AE.AECONTRT, AE.AEPRESP, AE.AESCAN, AE.AESCONG, AE.AESDISAB, AE.AESDTH, AE.AESER, AE.AESHOSP, AE.AESINTV, AE.AESLIFE, AE.AESMIE, AE.AESOD, AE.AEUNANT, AG.AGOCCUR, AG.AGPRESP ... (共 123 个) |
| C66767 | 1 | AE.AEACN |
| C66768 | 1 | AE.AEOUT |
| C66769 | 1 | AE.AESEV |
| C66770 | 2 | VS.VSORRESU, VS.VSSTRESU |
| C66781 | 1 | DM.AGEU |
| C66788 | 1 | TS.TSVCDREF |
| C66789 | 36 | AG.AGSTAT, BS.BSSTAT, CE.CESTAT, CM.CMSTAT, CP.CPSTAT, CV.CVSTAT, DA.DASTAT, EG.EGSTAT, FA.FASTAT, FT.FTSTAT, GF.GFSTAT, HO.HOSTAT, IS.ISSTAT, LB.LBSTAT, MB.MBSTAT ... (共 36 个) |
| C66790 | 1 | DM.ETHNIC |
| C66797 | 2 | IE.IECAT, TI.IECAT |
| C67152 | 1 | TS.TSPARM |
| C67153 | 1 | VS.VSTEST |
| C67154 | 1 | LB.LBTEST |
| C71113 | 6 | AG.AGDOSFRQ, CM.CMDOSFRQ, EC.ECDOSFRQ, EX.EXDOSFRQ, PR.PRDOSFRQ, SU.SUDOSFRQ |
| C71148 | 6 | CV.CVPOS, EG.EGPOS, FT.FTPOS, MK.MKPOS, RE.REPOS, VS.VSPOS |
| C71150 | 1 | EG.EGSTRESC |
| C71151 | 1 | EG.EGMETHOD |
| C71152 | 1 | EG.EGTEST |
| C71153 | 1 | EG.EGTESTCD |
| C71620 | 58 | AG.AGDOSU, BS.BSORRESU, BS.BSSTRESU, CM.CMDOSU, CP.CPORRESU, CP.CPSTRESU, CV.CVORRESU, CV.CVSTRESU, DA.DAORRESU, DA.DASTRESU, EC.ECDOSU, EC.ECPSTRGU, EG.EGORRESU, EG.EGSTRESU, EX.EXDOSU ... (共 58 个) |
| C74456 | 19 | AE.AELOC, BE.BELOC, CV.CVLOC, EC.ECLOC, EX.EXLOC, FA.FALOC, MB.MBLOC, MI.MILOC, MK.MKLOC, MS.MSLOC, NV.NVLOC, OE.OELOC, PE.PELOC, PR.PRLOC, RE.RELOC ... (共 19 个) |
| C74457 | 1 | DM.RACE |
| C74558 | 1 | DS.DSCAT |
| C74559 | 1 | SC.SCTESTCD |
| C78731 | 1 | DA.DATEST |
| C78732 | 1 | DA.DATESTCD |
| C78733 | 8 | BS.BSSPCCND, CP.CPSPCCND, IS.ISSPCCND, LB.LBSPCCND, MB.MBSPCCND, MI.MISPCCND, MS.MSSPCCND, PC.PCSPCCND |
| C78734 | 11 | BS.BSSPEC, CP.CPSPEC, IS.ISSPEC, LB.LBSPEC, MB.MBSPEC, MI.MISPEC, MS.MSSPEC, PC.PCSPEC, PP.PPSPEC, RELSPEC.SPEC, SR.SRSPEC |
| C78735 | 19 | CO.COEVAL, CV.CVEVAL, DD.DDEVAL, EG.EGEVAL, FA.FAEVAL, MI.MIEVAL, MK.MKEVAL, MS.MSEVAL, NV.NVEVAL, OE.OEEVAL, PE.PEEVAL, RE.REEVAL, RS.RSEVAL, SR.SREVAL, SS.SSEVAL ... (共 19 个) |
| C78736 | 5 | CP.CPNRIND, IS.ISNRIND, LB.LBNRIND, MS.MSNRIND, OE.OENRIND |
| C78737 | 1 | RELREC.RELTYPE |
| C85491 | 1 | IS.ISBDAGNT |
| C85492 | 19 | BS.BSMETHOD, CP.CPMETHOD, CV.CVMETHOD, GF.GFMETHOD, IS.ISMETHOD, LB.LBMETHOD, MB.MBMETHOD, MI.MIMETHOD, MK.MKMETHOD, MS.MSMETHOD, NV.NVMETHOD, OE.OEMETHOD, PC.PCMETHOD, PE.PEMETHOD, RE.REMETHOD ... (共 19 个) |
| C85493 | 1 | PP.PPTEST |
| C85494 | 4 | PC.PCORRESU, PC.PCSTRESU, PP.PPORRESU, PP.PPSTRESU |
| C85495 | 1 | MS.MSRESCAT |
| C85839 | 1 | PP.PPTESTCD |
| C90013 | 1 | EG.EGLEAD |
| C96777 | 12 | CO.COEVALID, CV.CVEVALID, EG.EGEVALID, MK.MKEVALID, MS.MSEVALID, NV.NVEVALID, OE.OEEVALID, RE.REEVALID, RS.RSEVALID, TR.TREVALID, TU.TUEVALID, UR.UREVALID |
| C96778 | 1 | TR.TRTEST |
| C96779 | 1 | TR.TRTESTCD |
| C96781 | 1 | RS.RSTEST |
| C96782 | 1 | RS.RSTESTCD |
| C96783 | 1 | TU.TUTEST |
| C96784 | 1 | TU.TUTESTCD |
| C96785 | 1 | RS.RSSTRESC |
| C99073 | 17 | CV.CVLAT, EC.ECLAT, EX.EXLAT, FA.FALAT, MB.MBLAT, MI.MILAT, MK.MKLAT, MS.MSLAT, NV.NVLAT, OE.OELAT, PE.PELAT, PR.PRLAT, RE.RELAT, SR.SRLAT, TU.TULAT ... (共 17 个) |
| C99074 | 13 | CV.CVDIR, EC.ECDIR, EX.EXDIR, MB.MBDIR, MI.MIDIR, MK.MKDIR, MS.MSDIR, NV.NVDIR, OE.OEDIR, PR.PRDIR, RE.REDIR, TU.TUDIR, UR.URDIR |
| C99075 | 4 | EC.ECPORTOT, OE.OEPORTOT, PR.PRPORTOT, TU.TUPORTOT |
| C99079 | 44 | AE.EPOCH, AG.EPOCH, CE.EPOCH, CM.EPOCH, CP.EPOCH, CV.EPOCH, DA.EPOCH, DS.EPOCH, DV.EPOCH, EC.EPOCH, EG.EPOCH, EX.EPOCH, FA.EPOCH, FT.EPOCH, HO.EPOCH ... (共 44 个) |
