# T4 加查复看包 — ATOM_ERR (S1-R1) (5 条; 编号沿用原包)

> 由 `scripts/t4/t4_atomerr_report.py` 从 `work/t4/atomerr/atomerr_pack_N.md` 原样摘出. 只读材料.

### E10. `ig34_p0122_a017` — ae:S1R1_ATOM_ERR

- PDF 页 122 · 原子类型 LIST_ITEM · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-ML review: 原子 verbatim 多 'not'; KB 与 PDF 一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-ML_review.md:70`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The ML domain is used to represent consumption of any food or nutritional item that would not be represented in the exposure domains (EC/EX), Concomitant/Prior Medications (CM), Procedure Agents (AG), or Substance Use (SU). Examples of nutritional items that would not be represented in other domains include:
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0122.txt` 第 36-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 35| ML – Assumptions
 36|      1.   The ML domain is used to represent consumption of any food or nutritional item that would not be represented in the exposure domains (EC/EX),
 37|           Concomitant/Prior Medications (CM), Procedure Agents (AG), or Substance Use (SU). Examples of nutritional items that would be represented in other
 38|           domains include:
 39|           a.    Investigational nutritional products (represented in EC/EX)
~~~~

KB 现文: `knowledge_base/domains/ML/assumptions.md:13-13` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  13| 1. The ML domain is used to represent consumption of any food or nutritional item that would not be represented in the exposure domains (EC/EX), Concomitant/Prior Medications (CM), Procedure Agents (AG), or Substance Use (SU). Examples of nutritional items that would be represented in other domains include:
~~~~


### E11. `ig34_p0123_a012` — ae:S1R1_ATOM_ERR

- PDF 页 123 · 原子类型 NOTE · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-ML review: 原子 verbatim 写成 'row.'; KB 与 PDF 一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-ML_review.md:70`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Click here to add a row. ADD ROW
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0123.txt` 第 19-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18|    Snack        Nutritional drink X Meal                                       2015 Dec 31   19:00        CE003
 19| Click here to add a row: ADD ROW
 20| 
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:19-19` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  19| | Click here to add a row: **ADD ROW** | | | | | | |
~~~~


### E12. `ig34_p0124_a001` — ae:S1R1_ATOM_ERR

- PDF 页 124 · 原子类型 TABLE_ROW · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-ML review: 原子 verbatim MIDSDTC 截断; KB 与 PDF 一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-ML_review.md:70`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
2 | XYZ | ML | XYZ-001-001 | 2 | NUTRITIONAL DRINK | HYPOGLYCEMIA EVALUATION | Y | Y | 8 | oz | | 2015-09-03T08:30 | | | LAST MEAL PRIOR TO | HYPO2 | 2015-09-03T17:00
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0124.txt` 第 2-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| Row STUDYID DOMAIN USUBJID MLSEQ MLTRT                         MLCAT             MLPRESP MLOCCUR MLDOSE MLDOSU MLDTC MLSTDTC                      MLENDTC MLEVLINT RELMIDS   MIDS  MIDSDTC
  2| 2   XYZ     ML     XYZ-001- 2    NUTRITIONAL                   HYPOGLYCEMIA      Y       Y       8      oz           2015-09-                                      LAST      HYPO2 2015-09-
  3|                    001           DRINK                         EVALUATION                                            03T08:30                                      MEAL            03T17:00
  4|                                                                                                                                                                    PRIOR
  5|                                                                                                                                                                    TO
  6| 3     XYZ          ML       XYZ-001-   3       MEAL            HYPOGLYCEMIA      Y          Y                                         2015-12-                     LAST      HYPO3 2016-01-
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:42` (来源: decision.evidence.hit):

~~~~
  42| | 2 | XYZ | ML | XYZ-001-001 | 2 | NUTRITIONAL DRINK | HYPOGLYCEMIA EVALUATION | Y | Y | 8 | oz | | 2015-09-03T08:30 | | | LAST MEAL PRIOR TO | HYPO2 | 2015-09-03T17:00 |
~~~~


### E13. `ig34_p0133_a003` — ae:S1R1_ATOM_ERR

- PDF 页 133 · 原子类型 TABLE_ROW · 所在节 `§6.1.6 [Substance Use (SU)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-SU review: 原子 verbatim 串列 (多 '2006-01-01'); KB 按渲染图正确; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-SU_review.md:28`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | 1234 | SU | 1234005 | 1 | CIGARETTES | TOBACCO | | | | 2 | PACK | QD | | | 2006-01-01 | | 2006-01-01 | BEFORE | 2006-01-01 | ONGOING |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0133.txt` 第 3-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2| Row STUDYID DOMAIN USUBJID SUSEQ SUTRT      SUCAT   SUSTAT SUREASND                        SUDOSE SUDOSU SUDOSFRQ SUSTDTC SUENDTC SUSTTPT SUSTRTPT SUENTPT SUENRTPT
  3| 1   1234    SU     1234005 1     CIGARETTES TOBACCO                                        2      PACK   QD                         2006-01- BEFORE 2006-01- ONGOING
  4|                                                                                                                                     01              01
~~~~

KB 现文: `knowledge_base/domains/SU/examples.md:37-37` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  37| | 1 | 1234 | SU | 1234005 | 1 | CIGARETTES | TOBACCO | | | 2 | PACK | QD | | | 2006-01-01 | BEFORE | 2006-01-01 | ONGOING |
~~~~


### E14. `ig34_p0150_a007` — ae:S1R1_ATOM_ERR

- PDF 页 150 · 原子类型 LIST_ITEM · 所在节 `§6.2.3 [Clinical Events (CE)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-CE writer: 原子抽错, KB 按渲染图正确; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-CE.md:63`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
(a) Events considered to be clinical events may include episodes of symptoms of the disease under study (often known as "signs and symptoms"), or events that do not constitute adverse events in themselves, though they might lead to the identification of an adverse event. For example, in a study of an investigational treatment for migraine headaches, migraine headaches may not be considered as adverse events per protocol. The occurrence of migraines or associated signs and symptoms might be reported in CE.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0150.txt` 第 19-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18|            CEs.
 19|            a.   Events considered to be clinical events may include episodes of symptoms of the disease under study (often known as "signs and symptoms"), or
 20|                 events that do not constitute adverse events in themselves, though they might lead to the identification of an adverse event. For example, in a study
 21|                 of an investigational treatment for migraine headaches, migraine headaches may not be considered to be adverse events per protocol. The
 22|                 occurrence of migraines or associated signs and symptoms might be reported in CE.
 23|            b.   In vaccine trials, certain adverse events may be considered to be signs or symptoms and accordingly determined to be clinical events. If any event is
~~~~

KB 现文: `knowledge_base/domains/CE/assumptions.md:14-14` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  14|    a. Events considered to be clinical events may include episodes of symptoms of the disease under study (often known as "signs and symptoms"), or events that do not constitute adverse events in themselves, though they might lead to the identification of an adverse event. For example, in a study of an investigational treatment for migraine headaches, migraine headaches may not be considered to be adverse events per protocol. The occurrence of migraines or associated signs and symptoms might be reported in CE.
~~~~

