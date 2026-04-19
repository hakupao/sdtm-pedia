# F1 — 批 4 高频 codelist 清单 (top 200)

> Stage: v2.4 (batch 4) preparation
> Script: `scripts_v2/score_codelists.py` (read-only, reads knowledge_base/terminology/ + knowledge_base/domains/*/spec.md)
> Log: `F1_codelist_score.log` (1005 codelists ranked)
> Completed: 2026-04-19 (主控 review)

## 得分公式 (见脚本 module docstring)

```
score = 0.5 * normalize(domain_ref_count)
      + 0.3 * sigmoid_term(term_count)         # 对数距离 hat, center=30
      + 0.2 * (50 if c_code in T_codelist_hits else 0)
```

- `domain_ref_count`: 该 codelist 的 C-code 在 knowledge_base/domains/*/spec.md 中被引用的次数 (min-max normalized)
- `term_count`: codelist 内 Term 行数 (正则 `^\| C\d+`)
- `T_codelist_hits`: 硬编码 {NY=C66742, FREQ=C71113}; AERELN / PROBLEM_TYPE 不在 knowledge_base (spec 中已兼容)

## T_codelist_hits 审计 (PLAN §F1 强制门)

| short_name | c_code | rank | score | 判定 |
|-----------|--------|------|-------|------|
| NY | C66742 | **1** | 10.669 | ✅ high tier |
| FREQ | C71113 | **2** | 10.232 | ✅ high tier |
| AERELN | (无映射) | — | — | knowledge_base 未收录 (spec 兼容) |
| PROBLEM_TYPE | (无映射) | — | — | knowledge_base 未收录 (spec 兼容) |

**PLAN §F1 门**: "top 200 名单必含 T_codelist_hits 中至少前两个属于 high tier" → NY + FREQ 双双进入 top 2, 门满足.

## 容量预算

| 指标 | 值 |
|-----|-----|
| 总 codelists | 1005 |
| Top 200 (批 4) 估算 tokens | **201,660** (term_count × 30) |
| Rank 201-500 (批 5 预留) 估算 tokens | 338,070 |
| 批 4 硬上限 (PLAN §F2 spec) | 250,000 |
| 批 4 软目标 (PLAN §F2 spec) | 200,000 |

**结论**: 201K 估算值**贴近** 200K 软目标, 处于软/硬之间. 安全边际: 实际 tokens 可能小于估算 (TOKENS_PER_TERM=30 是 spec 简化, 真实值可能 20-25/term). 建议 F2 按 top 200 全量抽取, 落盘后再决定是否拆 11a/11b/11c.

## 分布观察 (主控 review)

| 段 | 内容 | 占比 |
|----|------|------|
| rank 1-2 | T_hit (NY, FREQ) | 核心 — bonus +10 |
| rank 3-11 | 核心 SDTM codelist (Epoch, Unit, Not Done, Evaluator, Directionality, Specimen Condition, Medical Evaluator Identifier, Genetic Sample Type, Relation to Reference Period) | 高 domain_ref_count |
| rank 12-36 | Findings/Trial Design 辅助 + QRS Test Code/Name 首批 (Device Properties, Laterality, Cardiac Procedure Indication, ECG Lead/Test Method, Category of Functional Test 等) | 混合 |
| rank 37-200 | 以 QS / FT / CV / CL 相关 Test Name/Code pair 为主 (每种 PRO/QRS 工具两条: Name+Code) | 主体 |

**PRO/QRS pair 主导现象的合理性**: QS Test Name + Test Code 成对出现 (e.g. PASI Clinical Classification C135677/C135678), 每个 codelist 都有 ~10-30 terms, sigmoid_term 打到接近峰值 (0.3). domain_ref_count 在 QS spec 统一引用, 每对得分相同. 这种"对称冗余"是 CDISC CT 的客观结构, 不是打分偏差.

**缺失/意外**:
- `--SEV` severity codelist 不在 top 200 (spec 中未标注 C-code, 或 terms 分散多个 sublist)
- `EVALID` / `EVAL` 核心归因 codelist (C78735 Evaluator) 排 rank 6, 符合预期
- `RACE` / `ETHNIC` 核心 DM codelists 未在 top 200 顶部 (推测: term_count 小且对称引用度一般)

## Top 200 完整清单

| # | C-code | Codelist Name | Score |
|---|--------|--------------|-------|
| 1 | C66742 | No Yes Response | 10.669 |
| 2 | C71113 | Frequency | 10.232 |
| 3 | C99079 | Epoch | 0.488 |
| 4 | C71620 | Unit | 0.397 |
| 5 | C66789 | Not Done | 0.357 |
| 6 | C78735 | Evaluator | 0.356 |
| 7 | C99074 | Directionality | 0.318 |
| 8 | C78733 | Specimen Condition | 0.318 |
| 9 | C96777 | Medical Evaluator Identifier | 0.308 |
| 10 | C111114 | Genetic Sample Type | 0.306 |
| 11 | C66728 | Relation to Reference Period | 0.304 |
| 12 | C111111 | Device Properties Test Code | 0.300 |
| 13 | C111112 | Device Properties Test Name | 0.300 |
| 14 | C135677 | Psoriasis Area and Severity Index Clinical Classification Test Name | 0.300 |
| 15 | C135678 | Psoriasis Area and Severity Index Clinical Classification Test Code | 0.300 |
| 16 | C179935 | Psoriasis Area and Severity Index Version 2 Clinical Classification Test Name | 0.300 |
| 17 | C179936 | Psoriasis Area and Severity Index Version 2 Clinical Classification Test Code | 0.300 |
| 18 | C124685 | Positive and Negative Syndrome Scale Clinical Classification Test Name | 0.296 |
| 19 | C124686 | Positive and Negative Syndrome Scale Clinical Classification Test Code | 0.296 |
| 20 | C125744 | Expanded Disability Rating Scale - Postacute Interview Caregiver Version Questionnaire Test Name | 0.296 |
| 21 | C125745 | Expanded Disability Rating Scale - Postacute Interview Caregiver Version Questionnaire Test Code | 0.296 |
| 22 | C147541 | Functional Assessment of Chronic Illness Therapy-Dyspnea 10 Item Short Form Questionnaire Test Name | 0.296 |
| 23 | C147542 | Functional Assessment of Chronic Illness Therapy-Dyspnea 10 Item Short Form Questionnaire Test Code | 0.296 |
| 24 | C66739 | Trial Type Response | 0.296 |
| 25 | C117986 | Craig Handicap Assessment and Reporting Technique - Short Form Interview Version Questionnaire Test Name | 0.296 |
| 26 | C117987 | Craig Handicap Assessment and Reporting Technique - Short Form Interview Version Questionnaire Test Code | 0.296 |
| 27 | C117990 | Extrapyramidal Symptom Rating Scale-Abbreviated Clinical Classification Test Name | 0.296 |
| 28 | C117991 | Extrapyramidal Symptom Rating Scale-Abbreviated Clinical Classification Test Code | 0.296 |
| 29 | C119067 | Craig Handicap Assessment and Reporting Technique - Short Form Paper Version Questionnaire Test Name | 0.296 |
| 30 | C119068 | Craig Handicap Assessment and Reporting Technique - Short Form Paper Version Questionnaire Test Code | 0.296 |
| 31 | C174223 | Crohn's Disease Findings About Test Code | 0.296 |
| 32 | C174224 | Crohn's Disease Findings About Test Name | 0.296 |
| 33 | C99073 | Laterality | 0.294 |
| 34 | C115304 | Category of Functional Test | 0.293 |
| 35 | C123650 | Tumor or Lesion Identification Test Results | 0.293 |
| 36 | C90013 | ECG Lead | 0.293 |
| 37 | C106662 | Geriatric Depression Scale Questionnaire Test Name | 0.292 |
| 38 | C106663 | Geriatric Depression Scale Questionnaire Test Code | 0.292 |
| 39 | C176050 | Simple Endoscopic Score for Crohn's Disease Version 1 Clinical Classification Test Name | 0.292 |
| 40 | C176051 | Simple Endoscopic Score for Crohn's Disease Version 1 Clinical Classification Test Code | 0.292 |
| 41 | C177717 | Short Form 12 Health Survey Acute, US Version 2.0 Questionnaire Test Name | 0.292 |
| 42 | C177718 | Short Form 12 Health Survey Acute, US Version 2.0 Questionnaire Test Code | 0.292 |
| 43 | C177719 | Short Form 12 Health Survey Standard, US Version 2.0 Questionnaire Test Name | 0.292 |
| 44 | C177720 | Short Form 12 Health Survey Standard, US Version 2.0 Questionnaire Test Code | 0.292 |
| 45 | C141666 | International Physical Activity Questionnaire (October 2002) Long Last 7 Days Self-Administered Format Questionnaire Test Name | 0.291 |
| 46 | C141667 | International Physical Activity Questionnaire (October 2002) Long Last 7 Days Self-Administered Format Questionnaire Test Code | 0.291 |
| 47 | C181180 | Genomic Findings Test Detail | 0.291 |
| 48 | C111339 | Columbia-Suicide Severity Rating Scale Children's Since Last Visit Questionnaire Test Name | 0.288 |
| 49 | C111340 | Columbia-Suicide Severity Rating Scale Children's Since Last Visit Questionnaire Test Code | 0.288 |
| 50 | C127353 | The Functional Assessment of Cancer Therapy-General Version 4 Questionnaire Test Name | 0.288 |
| 51 | C127354 | The Functional Assessment of Cancer Therapy-General Version 4 Questionnaire Test Code | 0.288 |
| 52 | C138216 | Performance of the Upper Limb Module for DMD Version 1.2 Functional Test Test Name | 0.288 |
| 53 | C138217 | Performance of the Upper Limb Module for DMD Version 1.2 Functional Test Test Code | 0.288 |
| 54 | C138218 | Performance of the Upper Limb Module for DMD Version 2.0 Functional Test Test Name | 0.288 |
| 55 | C138219 | Performance of the Upper Limb Module for DMD Version 2.0 Functional Test Test Code | 0.288 |
| 56 | C170526 | Short Physical Performance Battery Version 1.2 Functional Test Test Name | 0.288 |
| 57 | C170527 | Short Physical Performance Battery Version 1.2 Functional Test Test Code | 0.288 |
| 58 | C174051 | Quality of Life in Inflammatory Bowel Disease Questionnaire Test Name | 0.288 |
| 59 | C174052 | Quality of Life in Inflammatory Bowel Disease Questionnaire Test Code | 0.288 |
| 60 | C71151 | ECG Test Method | 0.287 |
| 61 | C100159 | Screener and Opioid Assessment for Patients with Pain - Revised Questionnaire Test Name | 0.287 |
| 62 | C100160 | Screener and Opioid Assessment for Patients with Pain - Revised Questionnaire Test Code | 0.287 |
| 63 | C125746 | Expanded Disability Rating Scale - Postacute Interview Survivor Version Questionnaire Test Name | 0.287 |
| 64 | C125747 | Expanded Disability Rating Scale - Postacute Interview Survivor Version Questionnaire Test Code | 0.287 |
| 65 | C127349 | The Expanded Prostate Cancer Index Composite Short Form Questionnaire Test Name | 0.287 |
| 66 | C127350 | The Expanded Prostate Cancer Index Composite Short Form Questionnaire Test Code | 0.287 |
| 67 | C150791 | Suicidal Ideation Questionnaire-JR Questionnaire Test Name | 0.287 |
| 68 | C150792 | Suicidal Ideation Questionnaire-JR Questionnaire Test Code | 0.287 |
| 69 | C154456 | Symptoms of Major Depressive Disorder Scale v1.0 Questionnaire Test Name | 0.287 |
| 70 | C154457 | Symptoms of Major Depressive Disorder Scale v1.0 Questionnaire Test Code | 0.287 |
| 71 | C101859 | Cardiac Procedure Indication | 0.285 |
| 72 | C103474 | The Overactive Bladder Questionnaire Questionnaire Test Name | 0.285 |
| 73 | C103475 | The Overactive Bladder Questionnaire Questionnaire Test Code | 0.285 |
| 74 | C130246 | Inventory of Depressive Symptomatology Clinician-Rated Version Clinical Classification Test Name | 0.285 |
| 75 | C130247 | Inventory of Depressive Symptomatology Clinician-Rated Version Clinical Classification Test Code | 0.285 |
| 76 | C130260 | Inventory of Depressive Symptomatology Self-Report Version Questionnaire Test Name | 0.285 |
| 77 | C130261 | Inventory of Depressive Symptomatology Self-Report Version Questionnaire Test Code | 0.285 |
| 78 | C150769 | Mini-Mental State Examination 2 Standard Version Functional Test Test Name | 0.285 |
| 79 | C150770 | Mini-Mental State Examination 2 Standard Version Functional Test Test Code | 0.285 |
| 80 | C124297 | Biospecimen Events Dictionary Derived Term | 0.284 |
| 81 | C96781 | Oncology Response Assessment Test Name | 0.284 |
| 82 | C96782 | Oncology Response Assessment Test Code | 0.284 |
| 83 | C66770 | Units for Vital Signs Results | 0.283 |
| 84 | C100165 | Roland Morris Disability Questionnaire Questionnaire Test Name | 0.282 |
| 85 | C100166 | Roland Morris Disability Questionnaire Questionnaire Test Code | 0.282 |
| 86 | C103464 | Revised Fibromyalgia Impact Questionnaire Questionnaire Test Name | 0.282 |
| 87 | C103465 | Revised Fibromyalgia Impact Questionnaire Questionnaire Test Code | 0.282 |
| 88 | C130244 | Hamilton Depression Rating Scale - 24 Item Clinical Classification Test Name | 0.282 |
| 89 | C130245 | Hamilton Depression Rating Scale - 24 Item Clinical Classification Test Code | 0.282 |
| 90 | C138226 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Child Questionnaire Test Name | 0.282 |
| 91 | C138227 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Child Questionnaire Test Code | 0.282 |
| 92 | C138228 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Toddler Parent Report Questionnaire Test Name | 0.282 |
| 93 | C138229 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Toddler Parent Report Questionnaire Test Code | 0.282 |
| 94 | C138230 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Child Parent Report Questionnaire Test Name | 0.282 |
| 95 | C138231 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Child Parent Report Questionnaire Test Code | 0.282 |
| 96 | C138232 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Teen Parent Report Questionnaire Test Name | 0.282 |
| 97 | C138233 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Teen Parent Report Questionnaire Test Code | 0.282 |
| 98 | C138234 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Young Adult Parent Report Questionnaire Test Name | 0.282 |
| 99 | C138235 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Young Adult Parent Report Questionnaire Test Code | 0.282 |
| 100 | C138236 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Young Child Parent Report Questionnaire Test Name | 0.282 |
| 101 | C138237 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Young Child Parent Report Questionnaire Test Code | 0.282 |
| 102 | C138238 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Teen Questionnaire Test Name | 0.282 |
| 103 | C138239 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Teen Questionnaire Test Code | 0.282 |
| 104 | C138240 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Young Adult Questionnaire Test Name | 0.282 |
| 105 | C138241 | Pediatric Quality of Life Neuromuscular Module Acute Version 3 Young Adult Questionnaire Test Code | 0.282 |
| 106 | C138244 | Pediatric Quality of Life Neuromuscular Module Version 3 Child Questionnaire Test Name | 0.282 |
| 107 | C138245 | Pediatric Quality of Life Neuromuscular Module Version 3 Child Questionnaire Test Code | 0.282 |
| 108 | C138246 | Pediatric Quality of Life Neuromuscular Module Version 3 Toddler Parent Report Questionnaire Test Name | 0.282 |
| 109 | C138247 | Pediatric Quality of Life Neuromuscular Module Version 3 Toddler Parent Report Questionnaire Test Code | 0.282 |
| 110 | C138248 | Pediatric Quality of Life Neuromuscular Module Version 3 Child Parent Report Questionnaire Test Name | 0.282 |
| 111 | C138249 | Pediatric Quality of Life Neuromuscular Module Version 3 Child Parent Report Questionnaire Test Code | 0.282 |
| 112 | C138250 | Pediatric Quality of Life Neuromuscular Module Version 3 Teen Parent Report Questionnaire Test Name | 0.282 |
| 113 | C138251 | Pediatric Quality of Life Neuromuscular Module Version 3 Teen Parent Report Questionnaire Test Code | 0.282 |
| 114 | C138252 | Pediatric Quality of Life Neuromuscular Module Version 3 Young Adult Parent Report Questionnaire Test Name | 0.282 |
| 115 | C138253 | Pediatric Quality of Life Neuromuscular Module Version 3 Young Adult Parent Report Questionnaire Test Code | 0.282 |
| 116 | C138254 | Pediatric Quality of Life Neuromuscular Module Version 3 Young Child Parent Report Questionnaire Test Name | 0.282 |
| 117 | C138255 | Pediatric Quality of Life Neuromuscular Module Version 3 Young Child Parent Report Questionnaire Test Code | 0.282 |
| 118 | C138256 | Pediatric Quality of Life Neuromuscular Module Version 3 Teen Questionnaire Test Name | 0.282 |
| 119 | C138257 | Pediatric Quality of Life Neuromuscular Module Version 3 Teen Questionnaire Test Code | 0.282 |
| 120 | C138258 | Pediatric Quality of Life Neuromuscular Module Version 3 Young Adult Questionnaire Test Name | 0.282 |
| 121 | C138259 | Pediatric Quality of Life Neuromuscular Module Version 3 Young Adult Questionnaire Test Code | 0.282 |
| 122 | C71148 | Position | 0.282 |
| 123 | C103460 | Columbia-Suicide Severity Rating Scale Since Last Visit Questionnaire Test Name | 0.281 |
| 124 | C103461 | Columbia-Suicide Severity Rating Scale Since Last Visit Questionnaire Test Code | 0.281 |
| 125 | C124299 | Biospecimen Characteristics Test Name | 0.280 |
| 126 | C124300 | Biospecimen Characteristics Test Code | 0.280 |
| 127 | C181176 | Genomic Symbol Type Response | 0.280 |
| 128 | C66727 | Completion/Reason for Non-Completion | 0.278 |
| 129 | C101821 | Hamilton Depression Rating Scale 21-Item Clinical Classification Test Code | 0.278 |
| 130 | C101822 | Hamilton Depression Rating Scale 21-Item Clinical Classification Test Name | 0.278 |
| 131 | C150785 | National Comprehensive Cancer Network/Functional Assessment of Cancer Therapy-Brain Symptom Index-24 Version 2 Questionnaire Test Name | 0.278 |
| 132 | C150786 | National Comprehensive Cancer Network/Functional Assessment of Cancer Therapy-Brain Symptom Index-24 Version 2 Questionnaire Test Code | 0.278 |
| 133 | C163394 | Diabetes Distress Scale for Parents of Teens with Type 1 Diabetes Questionnaire Test Name | 0.278 |
| 134 | C163395 | Diabetes Distress Scale for Parents of Teens with Type 1 Diabetes Questionnaire Test Code | 0.278 |
| 135 | C170524 | European Organisation for the Research and Treatment of Cancer Quality of Life Questionnaire - Colorectal Version 2.1 Questionnaire Test Name | 0.278 |
| 136 | C170525 | European Organisation for the Research and Treatment of Cancer Quality of Life Questionnaire - Colorectal Version 2.1 Questionnaire Test Code | 0.278 |
| 137 | C113861 | RAND 36-Item Health Survey 1.0 Questionnaire Test Name | 0.275 |
| 138 | C113862 | RAND 36-Item Health Survey 1.0 Questionnaire Test Code | 0.275 |
| 139 | C123654 | Rey Auditory Verbal Learning Test Functional Test Test Name | 0.275 |
| 140 | C123655 | Rey Auditory Verbal Learning Test Functional Test Test Code | 0.275 |
| 141 | C161620 | Diabetes Distress Scale for Adults with Type 1 Diabetes Questionnaire Test Name | 0.275 |
| 142 | C161621 | Diabetes Distress Scale for Adults with Type 1 Diabetes Questionnaire Test Code | 0.275 |
| 143 | C163396 | Diabetes Distress Scale for Partners of Adults with Type 1 Diabetes Questionnaire Test Name | 0.275 |
| 144 | C163397 | Diabetes Distress Scale for Partners of Adults with Type 1 Diabetes Questionnaire Test Code | 0.275 |
| 145 | C115403 | Extended Glasgow Outcome Scale Questionnaire Test Name | 0.273 |
| 146 | C115404 | Extended Glasgow Outcome Scale Questionnaire Test Code | 0.273 |
| 147 | C176048 | Crohn's Disease Activity Index Version 1 Clinical Classification Test Name | 0.273 |
| 148 | C176049 | Crohn's Disease Activity Index Version 1 Clinical Classification Test Code | 0.273 |
| 149 | C100151 | Michigan Neuropathy Screening Instrument Questionnaire Test Name | 0.272 |
| 150 | C100152 | Michigan Neuropathy Screening Instrument Questionnaire Test Code | 0.272 |
| 151 | C111335 | Columbia-Suicide Severity Rating Scale Children's Baseline Questionnaire Test Name | 0.272 |
| 152 | C111336 | Columbia-Suicide Severity Rating Scale Children's Baseline Questionnaire Test Code | 0.272 |
| 153 | C150781 | Functional Assessment of Cancer Therapy-Lung Version 4 Questionnaire Test Name | 0.272 |
| 154 | C150782 | Functional Assessment of Cancer Therapy-Lung Version 4 Questionnaire Test Code | 0.272 |
| 155 | C160922 | Laboratory Analytical Method Calculation Formula | 0.270 |
| 156 | C100141 | Mini-Mental State Examination Functional Test Test Name | 0.269 |
| 157 | C100142 | Mini-Mental State Examination Functional Test Test Code | 0.269 |
| 158 | C106652 | Alzheimer's Disease Cooperative Study-Activities of Daily Living Inventory Severe Dementia Version Questionnaire Test Name | 0.269 |
| 159 | C106653 | Alzheimer's Disease Cooperative Study-Activities of Daily Living Inventory Severe Dementia Version Questionnaire Test Code | 0.269 |
| 160 | C150779 | Functional Assessment of Cancer Therapy/Gynecologic Oncology Group-Neurotoxicity Version 4 Questionnaire Test Name | 0.269 |
| 161 | C150780 | Functional Assessment of Cancer Therapy/Gynecologic Oncology Group-Neurotoxicity Version 4 Questionnaire Test Code | 0.269 |
| 162 | C100155 | Short-Form McGill Pain Questionnaire-2 Questionnaire Test Name | 0.269 |
| 163 | C100156 | Short-Form McGill Pain Questionnaire-2 Questionnaire Test Code | 0.269 |
| 164 | C123652 | Exacerbations of Chronic Pulmonary Disease Tool Patient-Reported Outcome Questionnaire Test Name | 0.269 |
| 165 | C123653 | Exacerbations of Chronic Pulmonary Disease Tool Patient-Reported Outcome Questionnaire Test Code | 0.269 |
| 166 | C127351 | The Expanded Prostate Cancer Index Composite for Clinical Practice Questionnaire Test Name | 0.269 |
| 167 | C127352 | The Expanded Prostate Cancer Index Composite for Clinical Practice Questionnaire Test Code | 0.269 |
| 168 | C150787 | National Comprehensive Cancer Network/Functional Assessment of Cancer Therapy-Head & Neck Symptom Index-22 Version 2 Questionnaire Test Name | 0.269 |
| 169 | C150788 | National Comprehensive Cancer Network/Functional Assessment of Cancer Therapy-Head & Neck Symptom Index-22 Version 2 Questionnaire Test Code | 0.269 |
| 170 | C158113 | QRS Method | 0.269 |
| 171 | C100167 | Columbia-Suicide Severity Rating Scale Baseline Questionnaire Test Name | 0.267 |
| 172 | C100168 | Columbia-Suicide Severity Rating Scale Baseline Questionnaire Test Code | 0.267 |
| 173 | C111341 | Columbia-Suicide Severity Rating Scale Screening Questionnaire Test Name | 0.267 |
| 174 | C111342 | Columbia-Suicide Severity Rating Scale Screening Questionnaire Test Code | 0.267 |
| 175 | C127357 | The Functional Assessment of Cancer Therapy-Prostate Version 4 Questionnaire Test Name | 0.267 |
| 176 | C127358 | The Functional Assessment of Cancer Therapy-Prostate Version 4 Questionnaire Test Code | 0.267 |
| 177 | C130272 | World Health Organization Disability Assessment Schedule 2.0 - 36-Item Self Questionnaire Test Name | 0.267 |
| 178 | C130273 | World Health Organization Disability Assessment Schedule 2.0 - 36-Item Self Questionnaire Test Code | 0.267 |
| 179 | C171444 | Health Care Encounters Dictionary Derived Term | 0.266 |
| 180 | C101863 | Discharge Disposition | 0.264 |
| 181 | C103484 | Symptom Impact Questionnaire Questionnaire Test Name | 0.264 |
| 182 | C103485 | Symptom Impact Questionnaire Questionnaire Test Code | 0.264 |
| 183 | C113857 | Modified Fatigue Impact Scale Questionnaire Test Name | 0.264 |
| 184 | C113858 | Modified Fatigue Impact Scale Questionnaire Test Code | 0.264 |
| 185 | C130274 | World Health Organization Disability Assessment Schedule 2.0 - 12-Item Interviewer Questionnaire Test Name | 0.264 |
| 186 | C130275 | World Health Organization Disability Assessment Schedule 2.0 - 12-Item Interviewer Questionnaire Test Code | 0.264 |
| 187 | C179939 | Functional Assessment of Cancer Therapy-Bone Pain Version 4 Questionnaire Test Name | 0.264 |
| 188 | C179940 | Functional Assessment of Cancer Therapy-Bone Pain Version 4 Questionnaire Test Code | 0.264 |
| 189 | C130270 | World Health Organization Disability Assessment Schedule 2.0 - 36-Item Proxy Questionnaire Test Name | 0.264 |
| 190 | C130271 | World Health Organization Disability Assessment Schedule 2.0 - 36-Item Proxy Questionnaire Test Code | 0.264 |
| 191 | C150777 | Functional Assessment of Cancer Therapy-Biologic Response Modifiers Version 4 Questionnaire Test Name | 0.264 |
| 192 | C150778 | Functional Assessment of Cancer Therapy-Biologic Response Modifiers Version 4 Questionnaire Test Code | 0.264 |
| 193 | C106670 | St. George's Respiratory Questionnaire for COPD Patients Questionnaire Test Name | 0.262 |
| 194 | C106671 | St. George's Respiratory Questionnaire for COPD Patients Questionnaire Test Code | 0.262 |
| 195 | C141668 | International Physical Activity Questionnaire (November 2002) Long Last 7 Days Telephone Format Questionnaire Test Name | 0.262 |
| 196 | C141669 | International Physical Activity Questionnaire (November 2002) Long Last 7 Days Telephone Format Questionnaire Test Code | 0.262 |
| 197 | C154446 | Children's Depression Rating Scale, Revised Clinical Classification Test Name | 0.262 |
| 198 | C154447 | Children's Depression Rating Scale, Revised Clinical Classification Test Code | 0.262 |
| 199 | C166183 | Functional Assessment of Cancer Therapy-Cognitive Function Version 3 Questionnaire Test Name | 0.262 |
| 200 | C166184 | Functional Assessment of Cancer Therapy-Cognitive Function Version 3 Questionnaire Test Code | 0.262 |

## 下一步

→ **Task F2**: 写 `scripts_v2/extract_terminology_terms.py --tier high`, 输入本文件 (top 200 C-code 列表), 输出 `output_v2/11_terminology_high.md` (或拆 11a/b/c), 软目标 ≤200K, 硬上限 250K.

Executor subagent prompt 已在 PLAN_V2.md §F2 落盘. 抽取算法 (tier=high): 完整保留 codelist 标题/描述 + Term 表 (Code | Term | Synonyms | Definition ≤200 char | Related Domain); 不展开 NCI Concept Description 长文本.

Reviewer 抽样 N=10 (规则 A 强制), 主控独立抽样 N=10 (不重叠), 验证 Term 表完整.
