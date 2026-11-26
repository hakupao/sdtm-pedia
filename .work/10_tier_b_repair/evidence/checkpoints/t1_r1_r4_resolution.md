# T1.4 裁定落地: R1 / R4 逐条

<!-- chain: E (plans) -->
> 生成: `scripts/helpers/t2_pkg.py` (2026-11-26) 读 `work/triage_merged.json` (含 `work/t1_rulings.json`); 只列 ID / 位置 / 计数, 不含 PDF 原文.

## 1. R1 — VERSION_MISMATCH 70 条

规则: sv20 变量表行且 model/ 有 5 列精简版 (#/name/label/type/role 与 PDF 一致, 脚本逐行断言) → IE; sv20 §1 Introduction 句 → REAL_GAP (补进 model/01, 在 §2 前新增 §1);
TD 句 (sv20 §5.1.4.2) → REAL_GAP (按归属补进 model/05 TD 节). 70 = 表行 45 + §1 22 + TD 3; 零散条目 (TOC / 列头) 不在这 70 条内, 按 §3 的先例归类.
ack 里写的 '§1 17 条 / TD 2 句' 是 T1.3b 追加复核子集的数, 全集为 §1 22 / TD 3 (同一规则).

| atom_id | 节 | 原 kb_loc | 裁定 | 修复目标 |
|---|---|---|---|---|
| sv20_p0004_a003 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a005 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a007 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a008 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a009 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a011 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a012 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a013 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a015 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a018 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a019 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a020 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a021 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a022 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a023 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a024 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a025 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0005_a002 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0005_a003 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0005_a005 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0005_a008 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0005_a009 | §1 [INTRODUCTION] |  | REAL_GAP (R1-intro) | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0046_a003 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:107 | IE (R1-row) |  |
| sv20_p0046_a004 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:108 | IE (R1-row) |  |
| sv20_p0046_a005 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:109 | IE (R1-row) |  |
| sv20_p0046_a006 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:110 | IE (R1-row) |  |
| sv20_p0046_a007 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:111 | IE (R1-row) |  |
| sv20_p0046_a008 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:112 | IE (R1-row) |  |
| sv20_p0046_a009 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:113 | IE (R1-row) |  |
| sv20_p0046_a010 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:114 | IE (R1-row) |  |
| sv20_p0046_a011 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:115 | IE (R1-row) |  |
| sv20_p0046_a012 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:116 | IE (R1-row) |  |
| sv20_p0046_a013 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:117 | IE (R1-row) |  |
| sv20_p0046_a014 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:118 | IE (R1-row) |  |
| sv20_p0046_a015 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:119 | IE (R1-row) |  |
| sv20_p0047_a003 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:133 | IE (R1-row) |  |
| sv20_p0047_a004 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:134 | IE (R1-row) |  |
| sv20_p0047_a005 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:135 | IE (R1-row) |  |
| sv20_p0047_a006 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:136 | IE (R1-row) |  |
| sv20_p0047_a007 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:137 | IE (R1-row) |  |
| sv20_p0047_a008 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:138 | IE (R1-row) |  |
| sv20_p0047_a009 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:139 | IE (R1-row) |  |
| sv20_p0047_a010 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:140 | IE (R1-row) |  |
| sv20_p0047_a011 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:141 | IE (R1-row) |  |
| sv20_p0047_a012 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:142 | IE (R1-row) |  |
| sv20_p0055_a003 | §5.1.3.2 Trial Repro Paths | knowledge_base/model/05_study_level_data.md:105 | IE (R1-row) |  |
| sv20_p0055_a004 | §5.1.3.2 Trial Repro Paths | knowledge_base/model/05_study_level_data.md:106 | IE (R1-row) |  |
| sv20_p0056_a008 | §5.1.4.1 Trial Visits | knowledge_base/model/05_study_level_data.md:124 | IE (R1-row) |  |
| sv20_p0056_a009 | §5.1.4.1 Trial Visits | knowledge_base/model/05_study_level_data.md:125 | IE (R1-row) |  |
| sv20_p0056_a010 | §5.1.4.1 Trial Visits | knowledge_base/model/05_study_level_data.md:126 | IE (R1-row) |  |
| sv20_p0056_a019 | §5.1.4.2 Trial Disease Assessments | knowledge_base/domains/TD/assumptions.md:3 | REAL_GAP (R1-TD) | knowledge_base/model/05_study_level_data.md |
| sv20_p0056_a020 | §5.1.4.2 Trial Disease Assessments | knowledge_base/domains/TD/assumptions.md:3 | REAL_GAP (R1-TD) | knowledge_base/model/05_study_level_data.md |
| sv20_p0056_a022 | §5.1.4.2 Trial Disease Assessments | knowledge_base/domains/TD/assumptions.md:3 | REAL_GAP (R1-TD) | knowledge_base/model/05_study_level_data.md |
| sv20_p0057_a003 | §5.1.4.2 Trial Disease Assessments | knowledge_base/model/05_study_level_data.md:142 | IE (R1-row) |  |
| sv20_p0057_a004 | §5.1.4.2 Trial Disease Assessments | knowledge_base/model/05_study_level_data.md:143 | IE (R1-row) |  |
| sv20_p0057_a006 | §5.1.4.2 Trial Disease Assessments | knowledge_base/model/05_study_level_data.md:145 | IE (R1-row) |  |
| sv20_p0057_a007 | §5.1.4.2 Trial Disease Assessments | knowledge_base/model/05_study_level_data.md:146 | IE (R1-row) |  |
| sv20_p0057_a011 | §5.1.4.2 Trial Disease Assessments | knowledge_base/model/05_study_level_data.md:150 | IE (R1-row) |  |
| sv20_p0058_a003 | §5.1.4.3 Trial Disease Milestones | knowledge_base/model/05_study_level_data.md:160 | IE (R1-row) |  |
| sv20_p0058_a004 | §5.1.4.3 Trial Disease Milestones | knowledge_base/model/05_study_level_data.md:161 | IE (R1-row) |  |
| sv20_p0058_a013 | §5.1.5 Trial Inclusion/Exclusion Criteria | knowledge_base/model/05_study_level_data.md:174 | IE (R1-row) |  |
| sv20_p0058_a014 | §5.1.5 Trial Inclusion/Exclusion Criteria | knowledge_base/model/05_study_level_data.md:175 | IE (R1-row) |  |
| sv20_p0059_a008 | §5.1.6 Trial Summary Information | knowledge_base/model/05_study_level_data.md:191 | IE (R1-row) |  |
| sv20_p0059_a009 | §5.1.6 Trial Summary Information | knowledge_base/model/05_study_level_data.md:192 | IE (R1-row) |  |
| sv20_p0064_a017 | §6.1 [Related Records Dataset] | knowledge_base/model/06_relationship_datasets.md:31 | IE (R1-row) |  |
| sv20_p0064_a019 | §6.1 [Related Records Dataset] | knowledge_base/model/06_relationship_datasets.md:33 | IE (R1-row) |  |
| sv20_p0064_a020 | §6.1 [Related Records Dataset] | knowledge_base/model/06_relationship_datasets.md:34 | IE (R1-row) |  |
| sv20_p0065_a001 | §6.1 [Related Records Dataset] | knowledge_base/model/06_relationship_datasets.md:35 | IE (R1-row) |  |
| sv20_p0065_a002 | §6.1 [Related Records Dataset] | knowledge_base/model/06_relationship_datasets.md:36 | IE (R1-row) |  |
| sv20_p0068_a023 | §6.6 [Associated Persons Relationships] | knowledge_base/model/06_relationship_datasets.md:137 | IE (R1-row) |  |

### 1b. 反向口径兄弟 (lane notes: pack_027 sv20 §2 / sv20 §6.6) — 45 条, **0 条改类**

判据: 是变量表行且 5 列版在 model/ → IE; 是 prose → 保持分诊类. 这些全是 prose (脚本断言: 非 IE 的 sv20 原子无 TABLE_ROW/TABLE_HEADER);
§6.6 的表行 sv20_p0068_a023 已在上表 (IE). 只给 null kb_loc 的补了修复目标 (TARGET).

| atom_id | 节 | atom_type | 类 | 目标 |
|---|---|---|---|---|
| sv20_p0004_a003 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a005 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a007 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a008 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a009 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a011 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a012 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a013 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a015 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a018 | §1 [INTRODUCTION] | LIST_ITEM | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a019 | §1 [INTRODUCTION] | LIST_ITEM | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a020 | §1 [INTRODUCTION] | LIST_ITEM | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a021 | §1 [INTRODUCTION] | LIST_ITEM | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a022 | §1 [INTRODUCTION] | LIST_ITEM | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a023 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a024 | §1 [INTRODUCTION] | LIST_ITEM | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0004_a025 | §1 [INTRODUCTION] | LIST_ITEM | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0005_a002 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0005_a003 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0005_a004 | §1 [INTRODUCTION] | SENTENCE | REWRITE_OK | knowledge_base/model/01_concepts_and_terms.md:102 |
| sv20_p0005_a005 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0005_a008 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0005_a009 | §1 [INTRODUCTION] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0008_a002 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | SENTENCE | PRESENT | knowledge_base/model/01_concepts_and_terms.md:7 |
| sv20_p0008_a004 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md:7 |
| sv20_p0008_a005 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | SENTENCE | PRESENT | knowledge_base/model/01_concepts_and_terms.md:9 |
| sv20_p0008_a007 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0008_a009 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | SENTENCE | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md |
| sv20_p0009_a005 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | SENTENCE | PRESENT | knowledge_base/model/01_concepts_and_terms.md:47 |
| sv20_p0009_a006 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | SENTENCE | PRESENT | knowledge_base/model/01_concepts_and_terms.md:47 |
| sv20_p0009_a013 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | SENTENCE | PRESENT | knowledge_base/model/01_concepts_and_terms.md:59 |
| sv20_p0009_a016 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | LIST_ITEM | REWRITE_OK | knowledge_base/model/01_concepts_and_terms.md:65 |
| sv20_p0009_a018 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | LIST_ITEM | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md:67 |
| sv20_p0009_a019 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | SENTENCE | REWRITE_OK | knowledge_base/model/01_concepts_and_terms.md:86 |
| sv20_p0009_a020 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | SENTENCE | PRESENT | knowledge_base/model/01_concepts_and_terms.md:80 |
| sv20_p0009_a021 | §2 [MODEL CONCEPTS AND TERMS – ORGANIZATION OF THE SDTM] | SENTENCE | PRESENT | knowledge_base/model/01_concepts_and_terms.md:82 |
| sv20_p0051_a008 | §5.1 [The Trial Design Model] | LIST_ITEM | REAL_GAP | knowledge_base/model/05_study_level_data.md:17 |
| sv20_p0051_a013 | §5.1 [The Trial Design Model] | SENTENCE | REAL_GAP | knowledge_base/model/05_study_level_data.md:23 |
| sv20_p0052_a008 | §5.1.1.2 Trial Arms | SENTENCE | PRESENT | knowledge_base/model/05_study_level_data.md:45 |
| sv20_p0056_a019 | §5.1.4.2 Trial Disease Assessments | SENTENCE | REAL_GAP | knowledge_base/model/05_study_level_data.md |
| sv20_p0056_a020 | §5.1.4.2 Trial Disease Assessments | SENTENCE | REAL_GAP | knowledge_base/model/05_study_level_data.md |
| sv20_p0056_a022 | §5.1.4.2 Trial Disease Assessments | SENTENCE | REAL_GAP | knowledge_base/model/05_study_level_data.md |
| sv20_p0068_a012 | §6.6 [Associated Persons Relationships] | SENTENCE | REAL_GAP | knowledge_base/model/06_relationship_datasets.md:129 |
| sv20_p0068_a019 | §6.6 [Associated Persons Relationships] | SENTENCE | REAL_GAP | knowledge_base/model/06_relationship_datasets.md:129 |
| sv20_p0068_a020 | §6.6 [Associated Persons Relationships] | SENTENCE | REAL_GAP | knowledge_base/model/06_relationship_datasets.md:129 |

另: 06 whitelist 里 sv20 §1 的 `sv20_p0004_a016` 已是 IE (VERSION_MISMATCH, 不在本项目范围), 按 R1 它也属 §1 引言 → **待用户**: 是否一并补进 model/01.

## 2. R4 — IE 整体 ack; 逐字在 KB 的转 PRESENT

判据: `fp_match.norm(verbatim)` 是 kb_loc **整个文件** `norm()` 的子串 (同 T3.2 指纹复验口径).
- R4-present 40: §3.2.1 xpt 文件名 (ch03 Location 格), T1.3b 追加复核所列;
- R4-present-sibling 9: 同表同型的 xpt 文件名, T1.3 已复核故不在 44 内; 同口径一并转 (统一标签);
- **R4-blocked 5**: 4 条数据集标题行 (T1.3b 说逐字一致) + 同型 AE 1 条. 实际 KB spec.md 顶部为 `> Class: … | Structure: …`, 缺 'xx.xpt,' 与 ', Tabulation' →
  非逐字, PRESENT 过不了 T3.2 指纹复验; **暂留 IE (REDUNDANT_WITH_SPEC), 待用户** (同型 ML 标题行 ig34_p0121_a005 现为 REWRITE_OK, 已标 t2_recheck).

| atom_id | kb_loc | 裁定 |
|---|---|---|
| ig34_p0017_a029 | knowledge_base/chapters/ch03_submitting_data.md:34 | PRESENT (R4-present) |
| ig34_p0017_a031 | knowledge_base/chapters/ch03_submitting_data.md:35 | PRESENT (R4-present) |
| ig34_p0017_a033 | knowledge_base/chapters/ch03_submitting_data.md:36 | PRESENT (R4-present) |
| ig34_p0017_a035 | knowledge_base/chapters/ch03_submitting_data.md:37 | PRESENT (R4-present) |
| ig34_p0017_a037 | knowledge_base/chapters/ch03_submitting_data.md:38 | PRESENT (R4-present-sibling) |
| ig34_p0018_a003 | knowledge_base/chapters/ch03_submitting_data.md:39 | PRESENT (R4-present) |
| ig34_p0018_a005 | knowledge_base/chapters/ch03_submitting_data.md:40 | PRESENT (R4-present-sibling) |
| ig34_p0018_a007 | knowledge_base/chapters/ch03_submitting_data.md:41 | PRESENT (R4-present) |
| ig34_p0018_a009 | knowledge_base/chapters/ch03_submitting_data.md:42 | PRESENT (R4-present) |
| ig34_p0018_a011 | knowledge_base/chapters/ch03_submitting_data.md:43 | PRESENT (R4-present) |
| ig34_p0018_a013 | knowledge_base/chapters/ch03_submitting_data.md:44 | PRESENT (R4-present) |
| ig34_p0018_a015 | knowledge_base/chapters/ch03_submitting_data.md:45 | PRESENT (R4-present) |
| ig34_p0018_a017 | knowledge_base/chapters/ch03_submitting_data.md:46 | PRESENT (R4-present-sibling) |
| ig34_p0018_a019 | knowledge_base/chapters/ch03_submitting_data.md:47 | PRESENT (R4-present) |
| ig34_p0018_a021 | knowledge_base/chapters/ch03_submitting_data.md:48 | PRESENT (R4-present) |
| ig34_p0018_a023 | knowledge_base/chapters/ch03_submitting_data.md:49 | PRESENT (R4-present) |
| ig34_p0018_a025 | knowledge_base/chapters/ch03_submitting_data.md:50 | PRESENT (R4-present) |
| ig34_p0018_a027 | knowledge_base/chapters/ch03_submitting_data.md:51 | PRESENT (R4-present) |
| ig34_p0018_a029 | knowledge_base/chapters/ch03_submitting_data.md:52 | PRESENT (R4-present) |
| ig34_p0018_a031 | knowledge_base/chapters/ch03_submitting_data.md:53 | PRESENT (R4-present) |
| ig34_p0018_a033 | knowledge_base/chapters/ch03_submitting_data.md:54 | PRESENT (R4-present) |
| ig34_p0018_a035 | knowledge_base/chapters/ch03_submitting_data.md:55 | PRESENT (R4-present-sibling) |
| ig34_p0018_a037 | knowledge_base/chapters/ch03_submitting_data.md:56 | PRESENT (R4-present-sibling) |
| ig34_p0018_a039 | knowledge_base/chapters/ch03_submitting_data.md:57 | PRESENT (R4-present) |
| ig34_p0018_a041 | knowledge_base/chapters/ch03_submitting_data.md:58 | PRESENT (R4-present) |
| ig34_p0018_a043 | knowledge_base/chapters/ch03_submitting_data.md:59 | PRESENT (R4-present) |
| ig34_p0018_a045 | knowledge_base/chapters/ch03_submitting_data.md:60 | PRESENT (R4-present) |
| ig34_p0018_a047 | knowledge_base/chapters/ch03_submitting_data.md:61 | PRESENT (R4-present-sibling) |
| ig34_p0018_a049 | knowledge_base/chapters/ch03_submitting_data.md:62 | PRESENT (R4-present) |
| ig34_p0018_a051 | knowledge_base/chapters/ch03_submitting_data.md:63 | PRESENT (R4-present) |
| ig34_p0019_a003 | knowledge_base/chapters/ch03_submitting_data.md:65 | PRESENT (R4-present-sibling) |
| ig34_p0019_a005 | knowledge_base/chapters/ch03_submitting_data.md:66 | PRESENT (R4-present) |
| ig34_p0019_a007 | knowledge_base/chapters/ch03_submitting_data.md:67 | PRESENT (R4-present) |
| ig34_p0019_a009 | knowledge_base/chapters/ch03_submitting_data.md:68 | PRESENT (R4-present) |
| ig34_p0019_a011 | knowledge_base/chapters/ch03_submitting_data.md:69 | PRESENT (R4-present) |
| ig34_p0019_a013 | knowledge_base/chapters/ch03_submitting_data.md:70 | PRESENT (R4-present) |
| ig34_p0019_a015 | knowledge_base/chapters/ch03_submitting_data.md:71 | PRESENT (R4-present) |
| ig34_p0019_a017 | knowledge_base/chapters/ch03_submitting_data.md:72 | PRESENT (R4-present) |
| ig34_p0019_a019 | knowledge_base/chapters/ch03_submitting_data.md:73 | PRESENT (R4-present-sibling) |
| ig34_p0019_a021 | knowledge_base/chapters/ch03_submitting_data.md:74 | PRESENT (R4-present) |
| ig34_p0019_a023 | knowledge_base/chapters/ch03_submitting_data.md:75 | PRESENT (R4-present) |
| ig34_p0019_a025 | knowledge_base/chapters/ch03_submitting_data.md:76 | PRESENT (R4-present) |
| ig34_p0019_a027 | knowledge_base/chapters/ch03_submitting_data.md:77 | PRESENT (R4-present) |
| ig34_p0019_a029 | knowledge_base/chapters/ch03_submitting_data.md:78 | PRESENT (R4-present) |
| ig34_p0019_a031 | knowledge_base/chapters/ch03_submitting_data.md:79 | PRESENT (R4-present) |
| ig34_p0019_a033 | knowledge_base/chapters/ch03_submitting_data.md:80 | PRESENT (R4-present-sibling) |
| ig34_p0019_a035 | knowledge_base/chapters/ch03_submitting_data.md:81 | PRESENT (R4-present) |
| ig34_p0019_a037 | knowledge_base/chapters/ch03_submitting_data.md:82 | PRESENT (R4-present) |
| ig34_p0019_a039 | knowledge_base/chapters/ch03_submitting_data.md:83 | PRESENT (R4-present) |
| ig34_p0129_a005 | knowledge_base/domains/SU/spec.md:3 | IE (R4-blocked) |
| ig34_p0134_a002 | knowledge_base/domains/AE/spec.md:3 | IE (R4-blocked) |
| ig34_p0148_a017 | knowledge_base/domains/CE/spec.md:2 | IE (R4-blocked) |
| ig34_p0183_a006 | knowledge_base/domains/DD/spec.md:3 | IE (R4-blocked) |
| ig34_p0185_a022 | knowledge_base/domains/EG/spec.md:3 | IE (R4-blocked) |

## 3. IE 标签统一 (whitelist 先例)

- CT 星号脚注 → REDUNDANT_WITH_SPEC (whitelist 同文 REDUNDANT_WITH_SPEC 13 : EDITORIAL_META 5, 取多数);
- sv20 目录条目 → VERSION_MISMATCH (同页 sv20_p0002_a001/a004/a006/a010/a021 先例);
- sv20 变量表列头 → VERSION_MISMATCH (whitelist sv20 TABLE_HEADER: VERSION_MISMATCH 13 + sdtm_v2_superseded 4; 'structural' 6 为结构标题非列头);
- ig34_p0195_a008 无 ie_cat → SPEC_TABLE_HEADER (reviewer 说明).

| atom_id | 原 → 新 |
|---|---|
| ig34_p0064_a011 | EDITORIAL_META → REDUNDANT_WITH_SPEC |
| ig34_p0172_a0013 | EDITORIAL_META → REDUNDANT_WITH_SPEC |
| ig34_p0193_a025 | EDITORIAL_META → REDUNDANT_WITH_SPEC |
| ig34_p0195_a008 | None → SPEC_TABLE_HEADER |
| ig34_p0288_a018 | EDITORIAL_META → REDUNDANT_WITH_SPEC |
| ig34_p0320_a023 | EDITORIAL_META → REDUNDANT_WITH_SPEC |
| sv20_p0002_a002 | EDITORIAL_META → VERSION_MISMATCH |
| sv20_p0002_a003 | EDITORIAL_META → VERSION_MISMATCH |
| sv20_p0002_a007 | EDITORIAL_META → VERSION_MISMATCH |
| sv20_p0002_a011 | EDITORIAL_META → VERSION_MISMATCH |
| sv20_p0002_a015 | EDITORIAL_META → VERSION_MISMATCH |
| sv20_p0002_a029 | EDITORIAL_META → VERSION_MISMATCH |
| sv20_p0002_a033 | EDITORIAL_META → VERSION_MISMATCH |
| sv20_p0002_a036 | EDITORIAL_META → VERSION_MISMATCH |
| sv20_p0002_a041 | EDITORIAL_META → VERSION_MISMATCH |
| sv20_p0055_a002 | SPEC_TABLE_HEADER → VERSION_MISMATCH |
| sv20_p0056_a007 | SPEC_TABLE_HEADER → VERSION_MISMATCH |
| sv20_p0057_a002 | SPEC_TABLE_HEADER → VERSION_MISMATCH |
| sv20_p0058_a002 | SPEC_TABLE_HEADER → VERSION_MISMATCH |
| sv20_p0058_a012 | SPEC_TABLE_HEADER → VERSION_MISMATCH |
| sv20_p0059_a007 | SPEC_TABLE_HEADER → VERSION_MISMATCH |

## 4. 修复目标补全 (kb_loc 为空 / ledger 目标错; 依据 lane notes, T1.3 已核)

| atom_id | 类 | 目标 | 依据 |
|---|---|---|---|
| ig34_p0285_a009 | REAL_GAP | knowledge_base/domains/NV/assumptions.md:5 | §6.3.7 概述宿主 NV/assumptions.md (lane D/C) |
| ig34_p0285_a010 | REAL_GAP | knowledge_base/domains/NV/assumptions.md:5 | §6.3.7 概述宿主 NV/assumptions.md (lane D/C) |
| ig34_p0363_a014 | RELOCATE | knowledge_base/domains/FA/assumptions.md:62 | source knowledge_base/chapters/ch02_fundamentals.md:219 (仅这些行允许删除) |
| ig34_p0364_a003 | RELOCATE | knowledge_base/domains/FA/assumptions.md:62 | source knowledge_base/chapters/ch02_fundamentals.md:227 (仅这些行允许删除) |
| ig34_p0364_a011 | RELOCATE | knowledge_base/domains/FA/assumptions.md:64 | source knowledge_base/model/02_observation_classes.md:188-190 (仅这些行允许删除) |
| sv20_p0008_a007 | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md | sv20 §2; 归属 model/01 (lane D, C10) |
| sv20_p0008_a009 | REAL_GAP | knowledge_base/model/01_concepts_and_terms.md | sv20 §2; 归属 model/01 (lane D, C10) |
| sv20_p0068_a012 | REAL_GAP | knowledge_base/model/06_relationship_datasets.md:129 | §6.6 APRELSUB; ledger 目标 model/04 错 (lane B) |
| sv20_p0068_a019 | REAL_GAP | knowledge_base/model/06_relationship_datasets.md:129 | §6.6 APRELSUB; ledger 目标 model/04 错 (lane B) |
| sv20_p0068_a020 | REAL_GAP | knowledge_base/model/06_relationship_datasets.md:129 | §6.6 APRELSUB; ledger 目标 model/04 错 (lane B) |
| ig34_p0194_a022 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a001 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a002 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a003 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a004 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a005 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a006 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a009 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a010 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a011 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a012 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a013 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a014 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a015 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a016 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a017 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a018 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a019 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a021 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0195_a023 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0196_a003 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0196_a004 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0196_a005 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0196_a006 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0196_a007 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0196_a008 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0196_a011 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
| ig34_p0196_a013 | REAL_GAP | knowledge_base/domains/LB/assumptions.md:1 | §6.3.5.1 → LB/assumptions.md 顶部新增 §6.3.5.1 节 (先例 NV 承载 §6.3.7.1); 表行连同整张通用规格表 p195-196 一并补 |
