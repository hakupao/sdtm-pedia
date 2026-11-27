# T4.1 补检包 7/8 — RULE_T1-two-agent+T2-rework (25 条, 全检, 不抽样)

> 由 `scripts/t4/t4_supp_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续.

### 160. `ig34_p0032_a014` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 32 · 原子类型 TABLE_HEADER · 所在节 `§4.2.7.1 "Specify" Values for Non-result Qualifier Variables`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `S-CH4`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Indication for analgesic | Post-operative pain / Headache / Menstrual pain / Myalgia / Toothache / Other, specify: ___________
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0032.txt` 第 19-24 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18| For example, consider a CRF that collects the indication for an analgesic concomitant medication (CMINDC) using
 19| a list of prespecified values and an "Other, specify" field :
 20| Indication for analgesic     o    Post-operative pain
 21|                              o    Headache
 22|                              o    Menstrual pain
 23|                              o    Myalgia
 24|                              o    Toothache
 25|                              o    Other,
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:400` (来源: triage kb_loc knowledge_base/chapters/ch04_general_assumptions.md:400 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 398| 
 399| When free-text information is collected to supplement a standard non-result qualifier field, the free-text value should be placed in the SUPP-- dataset described in Section 8.4, Relating Non-standard Variable Values to a Parent Domain. When applicable, controlled terminology should be used for SUPP-- field names (QNAM) and their associated labels (QLABEL; see Section 8.4, Relating Non-standard Variable Values to a Parent Domain, and Appendix C1, Supplemental Qualifiers Name Codes).
 400| 
 401| For example, when a description of "Other Medically Important Serious Adverse Event" category is collected on a CRF, the free-text description should be stored in the SUPPAE dataset.
 402| 
~~~~

### 161. `ig34_p0071_a002` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 71 · 原子类型 TABLE_HEADER · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-DM`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Select each value that applies if the subject answered "ASIAN". Check all that apply. | Which of the following racial designations best describes you? | [checkboxes]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0072.txt` 第 56-64 行 (自动定位, 词覆盖 0.818; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 55| If study participant answered: AMERICAN INDIAN OR ALASKA NATIVE
 56| CRACE01- 10            Which of the following Race Select each       Text   SUPPDM.QVAL   For each value that   (RACEC)       ALASKA NATIVE; AMERICAN                           checkbox
 57| CRACE04                racial designations         value that                             applies,                            INDIAN; CARIBBEAN INDIAN;
 58|                        best describes you?         applies if the                         SUPPDM.QVAL where                   CENTRAL AMERICAN
 59|                                                    subject                                SUPPDM.QNAM                         INDIAN;
 60|                                                    answered                               ="CRACEn" and
 61| 
 62| 
 63| 
 64| © 2021 Clinical Data Interchange Standards Consortium, Inc. All rights reserved                                                                                                             Page 72
 65| 2021-11-29
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:190-190` (来源: near triage kb_loc knowledge_base/domains/DM/examples.md:180 (score 0.955)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 190| | CRACE05-CRACE10 | 11 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "ASIAN". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ASIAN AMERICAN; ASIAN INDIAN; BANGLADESHI; CHINESE; JAPANESE; KOREAN; | | | checkbox | CRACE05-CRACE10 |
~~~~

### 162. `ig34_p0152_a0004` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 152 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Nausea | o Yes | _ _/_ _ _/_ _ _ _ | _ _/_ _ _/_ _ _ _ | o Mild |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0152.txt` 第 6-6 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5| Event                         Date Started          Date Ended            Severity
  6| Nausea             o Yes      _ _ / _ _ _ / _ _ _ _ _ _ / _ _ _ / _ _ _ _ o Mild
  7|                    o No         (dd/mmm/yyyy)         (dd/mmm/yyyy)        o Moderate
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:43-43` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:43 (score 0.75)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  43| | Nausea | ○ Yes  ○ No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ○ Mild  ○ Moderate  ○ Severe |
~~~~

### 163. `ig34_p0152_a0005` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 152 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o No | (dd/mmm/yyyy) | (dd/mmm/yyyy) | o Moderate |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0152.txt` 第 7-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  6| Nausea             o Yes      _ _ / _ _ _ / _ _ _ _ _ _ / _ _ _ / _ _ _ _ o Mild
  7|                    o No         (dd/mmm/yyyy)         (dd/mmm/yyyy)        o Moderate
  8|                                                                            o Severe
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:43-43` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:43 (score 0.833)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  43| | Nausea | ○ Yes  ○ No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ○ Mild  ○ Moderate  ○ Severe |
~~~~

### 164. `ig34_p0152_a0006` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 152 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 ERROR) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | | | | o Severe |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0152.txt` 第 8-8 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7|                    o No         (dd/mmm/yyyy)         (dd/mmm/yyyy)        o Moderate
  8|                                                                            o Severe
  9| Vomit            o Yes        _ _ / _ _ _ / _ _ _ _ _ _ / _ _ _ / _ _ _ _ o Mild
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:43-43` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:43 (score 0.5)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  43| | Nausea | ○ Yes  ○ No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ○ Mild  ○ Moderate  ○ Severe |
~~~~

### 165. `ig34_p0152_a0007` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 152 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Vomit | o Yes | _ _/_ _ _/_ _ _ _ | _ _/_ _ _/_ _ _ _ | o Mild |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0152.txt` 第 9-9 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  8|                                                                            o Severe
  9| Vomit            o Yes        _ _ / _ _ _ / _ _ _ _ _ _ / _ _ _ / _ _ _ _ o Mild
 10|                  o No           (dd/mmm/yyyy)         (dd/mmm/yyyy)        o Moderate
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:44-44` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:44 (score 0.75)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  44| | Vomit | ○ Yes  ○ No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ○ Mild  ○ Moderate  ○ Severe |
~~~~

### 166. `ig34_p0152_a0008` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 152 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o No | (dd/mmm/yyyy) | (dd/mmm/yyyy) | o Moderate |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0152.txt` 第 7-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  6| Nausea             o Yes      _ _ / _ _ _ / _ _ _ _ _ _ / _ _ _ / _ _ _ _ o Mild
  7|                    o No         (dd/mmm/yyyy)         (dd/mmm/yyyy)        o Moderate
  8|                                                                            o Severe
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:43-43` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:44 (score 0.833)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  43| | Nausea | ○ Yes  ○ No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ○ Mild  ○ Moderate  ○ Severe |
~~~~

### 167. `ig34_p0152_a0009` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 152 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 ERROR) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | | | | o Severe |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0152.txt` 第 8-8 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7|                    o No         (dd/mmm/yyyy)         (dd/mmm/yyyy)        o Moderate
  8|                                                                            o Severe
  9| Vomit            o Yes        _ _ / _ _ _ / _ _ _ _ _ _ / _ _ _ / _ _ _ _ o Mild
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:43-43` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:44 (score 0.5)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  43| | Nausea | ○ Yes  ○ No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ○ Mild  ○ Moderate  ○ Severe |
~~~~

### 168. `ig34_p0152_a0010` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 152 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Diarrhea | o Yes | _ _/_ _ _/_ _ _ _ | _ _/_ _ _/_ _ _ _ | o Mild |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0152.txt` 第 12-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11|                                                                            o Severe
 12| Diarrhea         o Yes        _ _ / _ _ _ / _ _ _ _ _ _ / _ _ _ / _ _ _ _ o Mild
 13|                  o No           (dd/mmm/yyyy)         (dd/mmm/yyyy)        o Moderate
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:45-45` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:45 (score 0.75)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  45| | Diarrhea | ○ Yes  ○ No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ○ Mild  ○ Moderate  ○ Severe |
~~~~

### 169. `ig34_p0152_a0011` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 152 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o No | (dd/mmm/yyyy) | (dd/mmm/yyyy) | o Moderate |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0152.txt` 第 7-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  6| Nausea             o Yes      _ _ / _ _ _ / _ _ _ _ _ _ / _ _ _ / _ _ _ _ o Mild
  7|                    o No         (dd/mmm/yyyy)         (dd/mmm/yyyy)        o Moderate
  8|                                                                            o Severe
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:43-43` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:45 (score 0.833)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  43| | Nausea | ○ Yes  ○ No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ○ Mild  ○ Moderate  ○ Severe |
~~~~

### 170. `ig34_p0152_a0012` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 152 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 ERROR) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | | | | o Severe |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0152.txt` 第 8-8 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7|                    o No         (dd/mmm/yyyy)         (dd/mmm/yyyy)        o Moderate
  8|                                                                            o Severe
  9| Vomit            o Yes        _ _ / _ _ _ / _ _ _ _ _ _ / _ _ _ / _ _ _ _ o Mild
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:43-43` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:45 (score 0.5)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  43| | Nausea | ○ Yes  ○ No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ○ Mild  ○ Moderate  ○ Severe |
~~~~

### 171. `ig34_p0152_a0014` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 152 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | | (dd/mmm/yyyy) | (dd/mmm/yyyy) | o Moderate |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0152.txt` 第 7-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  6| Nausea             o Yes      _ _ / _ _ _ / _ _ _ _ _ _ / _ _ _ / _ _ _ _ o Mild
  7|                    o No         (dd/mmm/yyyy)         (dd/mmm/yyyy)        o Moderate
  8|                                                                            o Severe
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:43-43` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:46 (score 0.8)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  43| | Nausea | ○ Yes  ○ No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ○ Mild  ○ Moderate  ○ Severe |
~~~~

### 172. `ig34_p0152_a0015` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 152 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 ERROR) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | | | | o Severe |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0152.txt` 第 8-8 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7|                    o No         (dd/mmm/yyyy)         (dd/mmm/yyyy)        o Moderate
  8|                                                                            o Severe
  9| Vomit            o Yes        _ _ / _ _ _ / _ _ _ _ _ _ / _ _ _ / _ _ _ _ o Mild
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:43-43` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:46 (score 0.5)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  43| | Nausea | ○ Yes  ○ No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ○ Mild  ○ Moderate  ○ Severe |
~~~~

### 173. `ig34_p0153_a0006` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| How did fracture occur? | o Pathologic |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 6-6 行 (自动定位, 词覆盖 0.833; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  5| Date of fracture                                              --/---/--
  6| How did fracture occur?                                       ○ Pathologic
  7|                                                               ○ Fall
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:77-77` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:77 (score 0.833)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  77| | How did fracture occur? | ○ Pathologic  ○ Fall  ○ Other trauma  ○ Unknown |
~~~~

### 174. `ig34_p0153_a0007` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 ERROR) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o Fall |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 7-7 行 (自动定位, 词覆盖 0.5; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  6| How did fracture occur?                                       ○ Pathologic
  7|                                                               ○ Fall
  8|                                                               ○ Other trauma
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:77-77` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:77 (score 0.5)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  77| | How did fracture occur? | ○ Pathologic  ○ Fall  ○ Other trauma  ○ Unknown |
~~~~

### 175. `ig34_p0153_a0008` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o Other trauma |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 8-8 行 (自动定位, 词覆盖 0.667; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  7|                                                               ○ Fall
  8|                                                               ○ Other trauma
  9|                                                               ○ Unknown
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:77-77` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:77 (score 0.667)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  77| | How did fracture occur? | ○ Pathologic  ○ Fall  ○ Other trauma  ○ Unknown |
~~~~

### 176. `ig34_p0153_a0011` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| What was the laterality? | o Left |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 11-11 行 (自动定位, 词覆盖 0.833; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 10| What was the location of the fracture?                        _____
 11| What was the laterality?                                      ○ Left
 12|                                                               ○ Right
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:79-79` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:79 (score 0.833)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  79| | What was the laterality? | ○ Left  ○ Right  ○ Not applicable |
~~~~

### 177. `ig34_p0153_a0012` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o Right |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 12-12 行 (自动定位, 词覆盖 0.5; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 11| What was the laterality?                                      ○ Left
 12|                                                               ○ Right
 13|                                                               ○ Not applicable
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:79-79` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:79 (score 0.5)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  79| | What was the laterality? | ○ Left  ○ Right  ○ Not applicable |
~~~~

### 178. `ig34_p0153_a0013` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o Not applicable |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 13-13 行 (自动定位, 词覆盖 0.667; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 12|                                                               ○ Right
 13|                                                               ○ Not applicable
 14| Were therapeutic measures required?                           ○ Yes
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:79-79` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:79 (score 0.667)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  79| | What was the laterality? | ○ Left  ○ Right  ○ Not applicable |
~~~~

### 179. `ig34_p0153_a0016` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o Unknown |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 9-9 行 (自动定位, 词覆盖 0.5; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  8|                                                               ○ Other trauma
  9|                                                               ○ Unknown
 10| What was the location of the fracture?                        _____
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:77-77` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:80 (score 0.5)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  77| | How did fracture occur? | ○ Pathologic  ○ Fall  ○ Other trauma  ○ Unknown |
~~~~

### 180. `ig34_p0153_a0018` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 ERROR) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o Traction |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 18-18 行 (自动定位, 词覆盖 0.5; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 17| If therapeutic measures were required, select all that apply. □ Casting/immobilization
 18|                                                               □ Traction
 19|                                                               □ Surgery
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:81-81` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:81 (score 0.5)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  81| | If therapeutic measures were required, select all that apply. | □ Casting/immobilization  □ Traction  □ Surgery |
~~~~

### 181. `ig34_p0153_a0022` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o Unknown |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 9-9 行 (自动定位, 词覆盖 0.5; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  8|                                                               ○ Other trauma
  9|                                                               ○ Unknown
 10| What was the location of the fracture?                        _____
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:77-77` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:82 (score 0.5)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  77| | How did fracture occur? | ○ Pathologic  ○ Fall  ○ Other trauma  ○ Unknown |
~~~~

### 182. `ig34_p0153_a0023` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| If there were complications, select all that apply. | o Infection of fracture site |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 23-23 行 (自动定位, 词覆盖 0.923; 版式以原 PDF 为准):

~~~~
 22|                                                               ○ Unknown
 23| If there were complications, select all that apply.           □ Infection of fracture site
 24|                                                               □ Improper healing requiring bone reset
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:83-83` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:83 (score 0.923)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  83| | If there were complications, select all that apply. | □ Infection of fracture site  □ Improper healing requiring bone reset  □ Soft tissue damage, specify location ___ |
~~~~

### 183. `ig34_p0153_a0024` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 ERROR) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o Improper healing requiring bone reset |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 24-24 行 (自动定位, 词覆盖 0.833; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 23| If there were complications, select all that apply.           □ Infection of fracture site
 24|                                                               □ Improper healing requiring bone reset
 25|                                                               □ Soft tissue damage, specify location ______
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:83-83` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:83 (score 0.833)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  83| | If there were complications, select all that apply. | □ Infection of fracture site  □ Improper healing requiring bone reset  □ Soft tissue damage, specify location ___ |
~~~~

### 184. `ig34_p0153_a0025` — supp:RULE_T1-two-agent+T2-rework

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 ERROR) · 判定规则 `T1-two-agent+T2-rework` · 批 `B-CE`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| | o Soft tissue damage, specify location ____ |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 25-25 行 (自动定位, 词覆盖 0.833; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 24|                                                               □ Improper healing requiring bone reset
 25|                                                               □ Soft tissue damage, specify location ______
 26| 
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:83-83` (来源: near triage kb_loc knowledge_base/domains/CE/examples.md:83 (score 0.833)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  83| | If there were complications, select all that apply. | □ Infection of fracture site  □ Improper healing requiring bone reset  □ Soft tissue damage, specify location ___ |
~~~~

