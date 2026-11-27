# T4.2 人工抽样包 (交用户判定)

<!-- chain: E (plans) -->
> 状态: **待用户判定** (样本备于 2026-11-27, 主控只备样本, 不替用户判).
> 生成: `python3 -I .work/10_tier_b_repair/scripts/t4/t4_sample.py` → `python3 -I .work/10_tier_b_repair/scripts/t4/t4_render.py` (确定性, 可复跑; 本文件由脚本整体重写, 判定请在复跑前誊出或复跑后回填).
> 种子: 正式层 20261128, 风险层 20261129. 与 T4.1 总闸 72 条 (seed 20261127) 互不重叠.

## 怎么判

- **判据** (PLAN T4.2, hard 闸): 每条看 "KB 现文" 是否忠实承载 "PDF 原文" 的信息. 内容错误 = 漏信息 / 改了意思 / 值不对 / 放错位置. 闸要求 **内容错误 0**.
- "PDF 原文" 取自 PDF 文本层 (`work/pdf_pages/*.txt`, pdftotext 版式), 自动定位, 表格列对齐可能乱; 有疑问以原 PDF (`source/cdisc/SDTMIG v3.4 (no header footer).pdf` / `SDTM_v2.0.pdf`, 同页号) 为准.
- "原子 verbatim" 是早期抽取物, 已知有抽错 (终态 ATOM_ERR 的就是这类), 只作对照, 不作判据.
- 终态 ATOM_ERR: 判 "原子确实与 PDF 不符, 且 KB 按 PDF 写对了" 即正确. 终态 PDF_TYPO: 判 "PDF 确有笔误, KB 处理与登记一致" 即正确 (改不改由 `t4_user_decisions.md` 另行裁定). 终态 INTENTIONAL_EXCLUDE: 判 "这条不进 KB 合理" (KB 现文一栏为空属正常).
- KB 行号是本仓 HEAD (KB 内容 = 00a2e93) 的当前行号.

## 分层

| 层 | N | 总体 | 说明 |
|---|--:|--:|---|
| REWRITE_OK | 10 | 91 | T1 判 "KB 改写但信息等价" 的原子 |
| REAL_GAP | 10 | 237 | T1 判 "KB 真缺" 并在 T2 补的原子 |
| VALUE_DIFF | 5 | 96 | T1 判 "KB 值与 PDF 不符" 的原子 |
| IE | 5 | 513 | T1 判 "有意不收" 的原子 |
| RISK_ANCHORLESS (加层) | 12 | 508 | T3 判 EXACT 但 KB 命中处没有可核的节号锚 (`work/t3_t4_risk_anchorless.txt`); 按原因分层: "no governing numbered heading" 442 抽 8, "atom section has no number" 66 抽 4 (N 与分层为主控取值) |

- 总体排除: `MANUAL_01`/`MANUAL_02` (无 ledger 行)、残留 `ig34_p0056_a006` (另列 `t4_user_decisions.md` 待裁).
- PLAN 写 "VALUE_DIFF+IE 10", 主控按 5+5 拆. 风险层 8:4 而总体 442:66, 有意加重 "atom section has no number" 一类 (更易错位).
- 本包共 42 条 (PLAN 正式 30 + 风险加层 12). 风险层是加层: 正式闸 = 前 30 条; 风险层若判出错, 主控按 PLAN Q9 同口径扩为该类全量复核.

## 判定汇总 (用户填)

| 层 | 内容正确 | 内容错误 | 看不出 |
|---|--:|--:|--:|
| REWRITE_OK (10) | | | |
| REAL_GAP (10) | | | |
| VALUE_DIFF+IE (10) | | | |
| RISK_ANCHORLESS (12) | | | |

## human:REWRITE_OK

### 1. `ig34_p0010_a002` — human:REWRITE_OK

- PDF 页 10 · 原子类型 LIST_ITEM · 所在节 `§1.4.1 [How to Read a Domain Specification]`
- triage 类 **REWRITE_OK** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `S1-R2` · 批 `B-ch01`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-ch01 T-1: PDF 缺 has, KB 补; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-ch01.md:98`
- 登记 `B-ch01 T-1`: PDF 写 "a codelist not yet been developed" → KB 写 "has not yet been" (处理: KB 写正确值; 依据: p49 同短语旁证; KB `knowledge_base/chapters/ch01_introduction.md:85`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The controlled terminology might be of a type that could be standardized, but for which a codelist not yet been developed.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0010.txt` 第 2-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1|                   •     The controlled terminology might be of a type that would inherently be sponsor-defined.
  2|                   •     The controlled terminology might be of a type that could be standardized, but for which a
  3|                         codelist not yet been developed.
  4|                   •     The controlled terminology might be terminology specified in value-level metadata.
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:85` (来源: registry B-ch01 T-1 kb_line_now):

~~~~
  85|       - The controlled terminology might be of a type that could be standardized, but for which a codelist has not yet been developed.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 2. `ig34_p0010_a012` — human:REWRITE_OK

- PDF 页 10 · 原子类型 LIST_ITEM · 所在节 `§1.4.1 [How to Read a Domain Specification]`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_005`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
A description of what the variable means
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0010.txt` 第 20-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19|     •    CDISC Notes may include any of the following:
 20|          o   A description of what the variable means
 21|          o   Information about how this variable relates to another variable
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:95` (来源: decision.evidence.hit):

~~~~
  95|   - A description of what the variable means
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 3. `ig34_p0011_a018` — human:REWRITE_OK

- PDF 页 11 · 原子类型 LIST_ITEM · 所在节 `§2.1 Observations and Variables`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_026`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Record Qualifiers define additional attributes of the observation record as a whole (rather than describing a particular variable within a record). Examples include --REASND, AESLIFE, and all other serious adverse event (SAE) flag variables in the AE domain; AGE, SEX, and RACE in the DM domain; and --BLFL, --POS, --LOC, --SPEC and --NAM in a Findings domain
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0011.txt` 第 25-28 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24|          -TEST and ‑‑LOINC, which are equivalent terms for a --TESTCD.
 25|     •    Record Qualifiers define additional attributes of the observation record as a whole (rather than describing a
 26|          particular variable within a record). Examples include --REASND, AESLIFE, and all other serious adverse
 27|          event (SAE) flag variables in the AE domain; AGE, SEX, and RACE in the DM domain; and --BLFL, --
 28|          POS, --LOC, --SPEC and --NAM in a Findings domain
 29|     •    Variable Qualifiers are used to further modify or describe a specific variable within an observation and are
~~~~

KB 现文: `knowledge_base/chapters/ch02_fundamentals.md:30` (来源: decision.evidence.hit):

~~~~
  30| - **Record Qualifiers** define additional attributes of the observation record as a whole (rather than describing a particular variable within a record). Examples include --REASND, AESLIFE, and all other serious adverse event (SAE) flag variables in the AE domain; AGE, SEX, and RACE in the DM domain; and --BLFL, --POS, --LOC, --SPEC and --NAM in a Findings domain
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 4. `ig34_p0011_a030` — human:REWRITE_OK

- PDF 页 11 · 原子类型 SENTENCE · 所在节 `§2.2 Datasets and Domains`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_026`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This code, which is stored in the SDTM variable named DOMAIN, is used in 4 ways: as the dataset
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0011.txt` 第 44-44 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 43| Each domain dataset is distinguished by a unique, 2-character code that should be used consistently throughout the
 44| submission. This code, which is stored in the SDTM variable named DOMAIN, is used in 4 ways: as the dataset
~~~~

KB 现文: `knowledge_base/chapters/ch02_fundamentals.md:39` (来源: decision.evidence.hit):

~~~~
  39| Each domain dataset is distinguished by a unique, 2-character code that should be used consistently throughout the submission. This code, which is stored in the SDTM variable named DOMAIN, is used in 4 ways: as the dataset name, as the value of the DOMAIN variable in that dataset, as a prefix for most variable names in that dataset, and as a value in the RDOMAIN variable in relationship tables (see Section 8, Representing Relationships and Data).
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 5. `ig34_p0044_a008` — human:REWRITE_OK

- PDF 页 44 · 原子类型 LIST_ITEM · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch04`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Start values: An observation can start BEFORE the reference point, can start COINCIDENT with the reference point, can start AFTER the reference point, or it can be UNKNOWN when it started.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0044.txt` 第 11-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 10| If the reference time point is prior to the date of collection or assessment:
 11|     •    Start values: An observation can start BEFORE the reference point, can start COINCIDENT with the
 12|          reference point, can start AFTER the reference point, or it can be UNKNOWN when it started.
 13|     •    End values: An observation can end BEFORE the reference point, can end COINCIDENT with the
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:976` (来源: decision.evidence.hit):

~~~~
 976| - Start values: An observation can start BEFORE the reference point, can start COINCIDENT with the reference point, can start AFTER the reference point, or it can be UNKNOWN when it started.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 6. `ig34_p0152_a0006` — human:REWRITE_OK

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
  43| | Nausea | ( ) Yes  ( ) No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ( ) Mild  ( ) Moderate  ( ) Severe |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 7. `ig34_p0152_a0009` — human:REWRITE_OK

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
  43| | Nausea | ( ) Yes  ( ) No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ( ) Mild  ( ) Moderate  ( ) Severe |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 8. `ig34_p0152_a0010` — human:REWRITE_OK

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
  45| | Diarrhea | ( ) Yes  ( ) No | __/___/____ (dd/mmm/yyyy) | __/___/____ (dd/mmm/yyyy) | ( ) Mild  ( ) Moderate  ( ) Severe |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 9. `ig34_p0153_a0008` — human:REWRITE_OK

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent` · 批 `T1:pack_011`

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
  77| | How did fracture occur? | ( ) Pathologic  ( ) Fall  ( ) Other trauma  ( ) Unknown |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 10. `ig34_p0367_a019` — human:REWRITE_OK

- PDF 页 367 · 原子类型 TABLE_ROW · 所在节 `FA – Examples`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_015`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Associated symptoms: Sensitivity to light Sensitivity to sound Nausea Aura | ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0367.txt` 第 18-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| Severity of migraine             ○ Mild ○ Moderate ○ Severe
 18| Associated symptoms:
 19| Sensitivity to light                ○ No   ○ Yes
 20| Sensitivity to sound                ○ No   ○ Yes
 21| Nausea                              ○ No   ○ Yes
 22| Aura
 23|                                     ○ No   ○ Yes
~~~~

KB 现文: `knowledge_base/domains/FA/examples.md:20,17,14` (来源: decision.evidence.hit):

> 同一文件共 3 处逐字命中 (行 20, 17, 14); 请按 PDF 所在例/表判断对应的是哪一处

~~~~
  14| | Associated symptoms: Sensitivity to light Sensitivity to sound Nausea Aura | ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes |
  17| | Associated symptoms: Sensitivity to light Sensitivity to sound Nausea Aura | ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes |
  20| | Associated symptoms: Sensitivity to light Sensitivity to sound Nausea Aura | ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

## human:REAL_GAP

### 11. `ig34_p0009_a006` — human:REAL_GAP

- PDF 页 9 · 原子类型 LIST_ITEM · 所在节 `§1.4 [How to Read this Implementation Guide]`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch01`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Review Section 9, Study References, to learn about occasions when it is necessary to establish study-specific references that will be used in accordance with subject data.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0009.txt` 第 12-13 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11|          relationships between datasets, records, and additional variables not specifically defined in the models.
 12|     7.   Review Section 9, Study References, to learn about occasions when it is necessary to establish study-
 13|          specific references that will be used in accordance with subject data.
 14|     8.   Finally, review the appendices as appropriate. Appendix C, Controlled Terminology, in particular,
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:61` (来源: decision.evidence.hit):

~~~~
  61| 7. Review Section 9, Study References, to learn about occasions when it is necessary to establish study-specific references that will be used in accordance with subject data.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 12. `ig34_p0012_a015` — human:REAL_GAP

- PDF 页 12 · 原子类型 LIST_ITEM · 所在节 `§2.3 The General Observation Classes`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch02`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The Interventions class captures investigational, therapeutic, and other treatments that are administered to the subject (with some actual or expected physiological effect) either as specified by the study protocol (e.g., exposure to study drug), coincident with the study assessment period (e.g., concomitant medications), or self-administered by the subject (e.g., use of alcohol, tobacco, or caffeine).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0012.txt` 第 19-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18| these can be found in the SDTM.
 19|     •    The Interventions class captures investigational, therapeutic, and other treatments that are administered to
 20|          the subject (with some actual or expected physiological effect) either as specified by the study protocol
 21|          (e.g., exposure to study drug), coincident with the study assessment period (e.g., concomitant medications),
 22|          or self‑administered by the subject (e.g., use of alcohol, tobacco, or caffeine).
 23|     •    The Events class captures planned protocol milestones such as randomization and study completion, and
~~~~

KB 现文: `knowledge_base/chapters/ch02_fundamentals.md:51` (来源: decision.evidence.hit):

~~~~
  51| - The **Interventions** class captures investigational, therapeutic, and other treatments that are administered to the subject (with some actual or expected physiological effect) either as specified by the study protocol (e.g., exposure to study drug), coincident with the study assessment period (e.g., concomitant medications), or self-administered by the subject (e.g., use of alcohol, tobacco, or caffeine).
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 13. `ig34_p0013_a008` — human:REAL_GAP

- PDF 页 13 · 原子类型 SENTENCE · 所在节 `§2.5 The SDTM Standard Domain Models`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch02`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Final domains will be published only in an SDTM implementation guide (this guide or another implementation guide, e.g., SDTMIG for Medical Devices).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0013.txt` 第 12-13 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11| well as additional custom domains based on the 3 general observation classes. A list of standard domains is provided
 12| in Section 3.2.1, Dataset-level Metadata. Final domains will be published only in an SDTM implementation guide
 13| (this guide or another implementation guide, e.g., SDTMIG for Medical Devices). Therapeutic-area standards
 14| projects and other projects may develop proposals for additional domains. Draft versions of these domains may be
~~~~

KB 现文: `knowledge_base/chapters/ch02_fundamentals.md:74` (来源: decision.evidence.hit):

~~~~
  74| The collected data for a given study may use standard domains from this and other SDTM implementation guides as well as additional custom domains based on the 3 general observation classes. A list of standard domains is provided in Section 3.2.1, Dataset-level Metadata. Final domains will be published only in an SDTM implementation guide (this guide or another implementation guide, e.g., SDTMIG for Medical Devices). Therapeutic-area standards projects and other projects may develop proposals for additional domains. Draft versions of these domains may be made available in the CDISC wiki in the SDTM Draft Domains space (https://wiki.cdisc.org/display/SDD/SDTM+Draft+Domains+Home).
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 14. `ig34_p0196_a003` — human:REAL_GAP

- PDF 页 196 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-LB`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| --NAM | Laboratory/Vendor Name | Char | * | Record Qualifier | Name or identifier of the vendor (e.g., laboratory) that provided the test results. | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0196.txt` 第 6-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5| --REASND      Reason Not Done                Char                          Record           Reason not done. Used in conjunction with --STAT when value is "NOT DONE".                                         Perm
  6|                                                                            Qualifier
  7| --NAM         Laboratory/Vendor Name         Char   *                      Record           Name or identifier of the vendor (e.g., laboratory) that provided the test results.                                Perm
  8|                                                                            Qualifier
~~~~

KB 现文: `knowledge_base/domains/LB/assumptions.md:40` (来源: decision.evidence.hit):

~~~~
  40| | --NAM | Laboratory/Vendor Name | Char | * | Record Qualifier | Name or identifier of the vendor (e.g., laboratory) that provided the test results. | Perm |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 15. `ig34_p0208_a023` — human:REAL_GAP

- PDF 页 208 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-CP`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-3: The total leukocyte population is determined using positive expression of the CD45 marker as the operational definition of the test (CD45+ in the CPMRKSTR variable). The total leukocyte count is reported because it contains the value used as the denominator in several subsequent tests for leukocyte subpopulations. Row 2 contains the total lymphocyte count which, in addition to CD45, used Forward (FSC) and Side (SSC) Light Scatter properties to define the lymphocyte subpopulation of leukocytes. By convention, FSC and SSC are often not included as part of the marker string definition of a cell subpopulation since it is well-recognized that these physical properties are used as the first gate in nearly all cell phenotyping applications. However, in the absence of a pan-lymphocyte marker to distinguish them from other leukocytes, FSC and SSC are included in rows 2 and 3 to indicate that these parameters are used in addition to CD45, to differentiate lymphocytes from other
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0208.txt` 第 43-52 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 42| Example 1a
 43| Rows 1-3:     The total leukocyte population is determined using positive expression of the CD45 marker as the
 44|               operational definition of the test (CD45+ in the CPMRKSTR variable). The total leukocyte count is
 45|               reported because it contains the value used as the denominator in several subsequent tests for
 46|               leukocyte subpopulations. Row 2 contains the total lymphocyte count which, in addition to CD45,
 47|               used Forward (FSC) and Side (SSC) Light Scatter properties to define the lymphocyte subpopulation
 48|               of leukocytes. By convention, FSC and SSC are often not included as part of the marker string
 49|               definition of a cell subpopulation since it is well-recognized that these physical properties are used as
 50|               the first gate in nearly all cell phenotyping applications. However, in the absence of a pan-lymphocyte
 51|               marker to distinguish them from other leukocytes, FSC and SSC are included in rows 2 and 3 to
 52|               indicate that these parameters are used in addition to CD45, to differentiate lymphocytes from other
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:15` (来源: decision.evidence.hit):

~~~~
  15| **Rows 1-3:** The total leukocyte population is determined using positive expression of the CD45 marker as the operational definition of the test (CD45+ in the CPMRKSTR variable). The total leukocyte count is reported because it contains the value used as the denominator in several subsequent tests for leukocyte subpopulations. Row 2 contains the total lymphocyte count which, in addition to CD45, used Forward (FSC) and Side (SSC) Light Scatter properties to define the lymphocyte subpopulation of leukocytes. By convention, FSC and SSC are often not included as part of the marker string definition of a cell subpopulation since it is well-recognized that these physical properties are used as the first gate in nearly all cell phenotyping applications. However, in the absence of a pan-lymphocyte marker to distinguish them from other leukocytes, FSC and SSC are included in rows 2 and 3 to indicate that these parameters are used in addition to CD45, to differentiate lymphocytes from other CD45+ leukocytes. Once they have been included in the marker string (CPMRKSTR) definition of lymphocytes, they can generally be dropped for any further subsetting of the lymphocytes population. Row 3 shows the proportion of lymphocytes as a percentage of total leukocytes. Note that the value in CPMRKSTR used a forward slash ("/") to separate the numerator marker string from the denominator marker string.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 16. `ig34_p0209_a001` — human:REAL_GAP

- PDF 页 209 · 原子类型 SENTENCE · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-CP`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
CD45+ leukocytes. Once they have been included in the marker string (CPMRKSTR) definition of lymphocytes, they can generally be dropped for any further subsetting of the lymphocytes population. Row 3 shows the proportion of lymphocytes as a percentage of total leukocytes. Note that the value in CPMRKSTR used a forward slash ("/") to separate the numerator marker string from the denominator marker string.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0209.txt` 第 1-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1|               CD45+ leukocytes. Once they have been included in the marker string (CPMRKSTR) definition of
  2|               lymphocytes, they can generally be dropped for any further subsetting of the lymphocytes population.
  3|               Row 3 shows the proportion of lymphocytes as a percentage of total leukocytes. Note that the value in
  4|               CPMRKSTR used a forward slash ("/") to separate the numerator marker string from the denominator
  5|               marker string.
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:15` (来源: decision.evidence.hit):

~~~~
  15| **Rows 1-3:** The total leukocyte population is determined using positive expression of the CD45 marker as the operational definition of the test (CD45+ in the CPMRKSTR variable). The total leukocyte count is reported because it contains the value used as the denominator in several subsequent tests for leukocyte subpopulations. Row 2 contains the total lymphocyte count which, in addition to CD45, used Forward (FSC) and Side (SSC) Light Scatter properties to define the lymphocyte subpopulation of leukocytes. By convention, FSC and SSC are often not included as part of the marker string definition of a cell subpopulation since it is well-recognized that these physical properties are used as the first gate in nearly all cell phenotyping applications. However, in the absence of a pan-lymphocyte marker to distinguish them from other leukocytes, FSC and SSC are included in rows 2 and 3 to indicate that these parameters are used in addition to CD45, to differentiate lymphocytes from other CD45+ leukocytes. Once they have been included in the marker string (CPMRKSTR) definition of lymphocytes, they can generally be dropped for any further subsetting of the lymphocytes population. Row 3 shows the proportion of lymphocytes as a percentage of total leukocytes. Note that the value in CPMRKSTR used a forward slash ("/") to separate the numerator marker string from the denominator marker string.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 17. `ig34_p0214_a001` — human:REAL_GAP

- PDF 页 214 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-CP`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Because not all cellular markers are expressed constitutively at detectable levels, an externally applied condition may need to be added to the test system to enable measurement or to test the functionality of the cell population being investigated. CPTSTCND was developed to capture any variable condition (i.e., a condition which can vary as opposed to is fixed) imposed on the assay system at the time the assay is conducted. Its primary use is when it is needed to differentiate results for the same test and specimen run under different assay conditions (e.g., stimulated vs unstimulated).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0214.txt` 第 1-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1|       1.        Because not all cellular markers are expressed constitutively at detectable levels, an externally applied condition may need to be added to the test system to enable measurement or to test the functionality of
  2|                 the cell population being investigated. CPTSTCND was developed to capture any variable condition (i.e., a condition which can vary as opposed to is fixed) imposed on the assay system at the time the assay
  3|                 is conducted. Its primary use is when it is needed to differentiate results for the same test and specimen run under different assay conditions (e.g., stimulated vs unstimulated).
  4|       2.        Repeated measures (replicates) are typically incorporated into an assay to monitor reproducibility and may be reported in addition to a summarized result value. CPREPNUM and CPCOLSRT have been
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:146` (来源: decision.evidence.hit):

~~~~
 146| 1. Because not all cellular markers are expressed constitutively at detectable levels, an externally applied condition may need to be added to the test system to enable measurement or to test the functionality of the cell population being investigated. CPTSTCND was developed to capture any variable condition (i.e., a condition which can vary as opposed to is fixed) imposed on the assay system at the time the assay is conducted. Its primary use is when it is needed to differentiate results for the same test and specimen run under different assay conditions (e.g., stimulated vs unstimulated).
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 18. `ig34_p0373_a012` — human:REAL_GAP

- PDF 页 373 · 原子类型 SENTENCE · 所在节 `FA – Examples`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-FA`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The collected data were represented in FA because they meet criterion 1 in Section 6.4.1, When to Use Findings About Events or Interventions, that is, data that do not describe an event or intervention as a whole. In this study, GERD symptoms were considered clinical events. In addition, the volume of vomit data met criterion 2 data ("about" an event or intervention), having qualifiers that can be represented in Findings variables (e.g., units, method).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0373.txt` 第 15-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14| 
 15| The collected data were represented in FA because they meet criterion 1 in Section 6.4.1, When to Use Findings About Events or Interventions, that is, data that
 16| do not describe an event or intervention as a whole. In this study, GERD symptoms were considered clinical events. In addition, the volume of vomit data met
 17| criterion 2 data (“about” an event or intervention), having qualifiers that can be represented in Findings variables (e.g., units, method).
 18| This SDTM example represents data from 2 visits for 1 subject. FAEVINTX indicates that assessments were for the previous 24 hours.
~~~~

KB 现文: `knowledge_base/domains/FA/examples.md:226` (来源: decision.evidence.hit):

~~~~
 226| The collected data were represented in FA because they meet criterion 1 in Section 6.4.1, When to Use Findings About Events or Interventions, that is, data that do not describe an event or intervention as a whole. In this study, GERD symptoms were considered clinical events. In addition, the volume of vomit data met criterion 2 data (“about” an event or intervention), having qualifiers that can be represented in Findings variables (e.g., units, method).
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 19. `ig34_p0416_a006` — human:REAL_GAP

- PDF 页 416 · 原子类型 SENTENCE · 所在节 `§7.4.1 Trial Inclusion/Exclusion Criteria (TI)`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-TI`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
A trial design domain that contains one record for each of the inclusion and exclusion criteria for the trial.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0416.txt` 第 8-8 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7| TI – Description/Overview
  8| A trial design domain that contains one record for each of the inclusion and exclusion criteria for the trial. This
  9| domain is not subject oriented.
~~~~

KB 现文: `knowledge_base/domains/TI/assumptions.md:18` (来源: decision.evidence.hit):

~~~~
  18| A trial design domain that contains one record for each of the inclusion and exclusion criteria for the trial. This domain is not subject oriented.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 20. `sv20_p0004_a013` — human:REAL_GAP

- PDF 页 4 · 原子类型 SENTENCE · 所在节 `§1 [INTRODUCTION]`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-model01`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Individual implementation guides (IGs) have been created to provide specific recommendations for numerous domains of data commonly collected in human, animal, and medical device studies, identifying which variables from a general observation class may apply.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0004.txt` 第 20-23 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19| The SDTM has been designed to accommodate the broadest range of human and animal study data in a standardized
 20| manner. This document describes the basic concepts and general structure of the model. Individual implementation
 21| guides (IGs) have been created to provide specific recommendations for numerous domains of data commonly
 22| collected in human, animal, and medical device studies, identifying which variables from a general observation class
 23| may apply. These IGs also describe basic assumptions and business rules, and provide numerous examples for
 24| mapping data to the standard format. Sponsors wishing to represent data in the standard formats should consult the
~~~~

KB 现文: `knowledge_base/model/01_concepts_and_terms.md:15` (来源: decision.evidence.hit):

~~~~
  15| The SDTM has been designed to accommodate the broadest range of human and animal study data in a standardized manner. This document describes the basic concepts and general structure of the model. Individual implementation guides (IGs) have been created to provide specific recommendations for numerous domains of data commonly collected in human, animal, and medical device studies, identifying which variables from a general observation class may apply. These IGs also describe basic assumptions and business rules, and provide numerous examples for mapping data to the standard format. Sponsors wishing to represent data in the standard formats should consult the IGs before preparing datasets based on the SDTM. The following implementation guides have been published by CDISC:
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

## human:VALUE_DIFF

### 21. `ig34_p0055_a026` — human:VALUE_DIFF

- PDF 页 55 · 原子类型 TABLE_HEADER · 所在节 `§4.5.3.2 [Text Strings Greater than 200 Characters in Other Variables]`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 MISPLACED) · 判定规则 `live-hit` · 批 `B-ch04`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0055.txt` 第 43-43 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 42| suppmh.xpt
 43| Row STUDYID RDOMAIN USUBJID IDVAR IDVARVAL QNAM    QLABEL                            QVAL                        QORIG QEVAL
 44| 1   12345   MH      99-123  MHSEQ 6        MHTERM1 Reported Term for the             2nd ~200 chars of text,     CRF
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1428,1445` (来源: decision.evidence.hit):

> 同一文件共 2 处逐字命中 (行 1428, 1445); 请按 PDF 所在例/表判断对应的是哪一处

~~~~
1428| | Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
1445| | Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 22. `ig34_p0169_a0024` — human:VALUE_DIFF

- PDF 页 169 · 原子类型 TABLE_ROW · 所在节 `§6.2.5 Healthcare Encounters (HO)`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-HO`
- 登记 `B-HO T-1`: PDF 写 "REHABILIATION FACILITY" → KB 写 "REHABILITATION FACILITY" (处理: KB 写正确值; 依据: Ex2 r3 / 叙述 / Assumption 1; KB `knowledge_base/domains/HO/examples.md:25`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 5 | ABC | HO | ABC123105 | 1 | GENERAL WARD | | TREATMENT | 2011-09-09 | 2011-09-11 | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0170.txt` 第 6-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  5| 2        ABC        HO         ABC123101     2          NURSING HOME                                      TREATMENT                                   P6D
  6| 3        ABC        HO         ABC123102     1          GENERAL WARD                                      TREATMENT      2011-08-06    2011-08-08
  7| 4        ABC        HO         ABC123102     2          INTENSIVE CARE                                    TREATMENT      2011-08-08    2011-08-15
  8| 5        ABC        HO         ABC123102     3          REHABILIATION FACILITY                            TREATMENT      2011-08-15    2011-08-20
  9| 6        ABC        HO         ABC123103     1          HOSPITAL                                          TREATMENT      2011-09-09    2011-09-11
 10| 7        ABC        HO         ABC123103     2          HOSPITAL                                          TREATMENT      2011-09-11    2011-09-15
 11| 8        ABC        HO         ABC123104     1          CARDIAC CATHETERIZATION LABORATORY                TREATMENT      2011-10-10    2011-10-10
 12| 9        ABC        HO         ABC123105     1          CARDIAC CATHETERIZATION LABORATORY                TREATMENT      2011-10-11    2011-10-11
 13| 10       ABC        HO         ABC123105     2          HOSPITAL                                          TREATMENT      2011-10-11    2011-10-15
~~~~

KB 现文: `knowledge_base/domains/HO/examples.md:25` (来源: registry B-HO T-1 kb_line_now):

~~~~
  25| | 5 | ABC | HO | ABC123102 | 3 | REHABILITATION FACILITY | TREATMENT | 2011-08-15 | 2011-08-20 | |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 23. `ig34_p0190_a011` — human:VALUE_DIFF

- PDF 页 190 · 原子类型 TABLE_ROW · 所在节 `§6.3.3 ECG Test Results (EG)`
- triage 类 **VALUE_DIFF** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-EG review: verbatim P0W 应为 PQW, VISIT 漏折行 1; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-EG_review.md:33`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 9 | XYZ | EG | XYZ-US-701-002 | 9 | 334PT89 | STSTWUW | ST Segment, T wave, and U wave | FINDING | SUPINE | PROLONGED QT | | PROLONGED QT | | | P0W436789-07.xml | Test Lab | | | | 1 | Screening | 2003-04-15T11:58 | -36 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0190.txt` 第 19-20 行 (自动定位, 词覆盖 0.967; 版式以原 PDF 为准):

~~~~
 18|                          701-002                                 Tachyarrhythmias                                                                                                              07.xml       Lab                                                 1           15T11:58
 19| 9     XYZ       EG       XYZ-US-   9       334PT89   STSTWUW     ST Segment, T wave,   FINDING         SUPINE   PROLONGED QT                      PROLONGED QT                                 PQW436789-   Test                                     1          Screening   2003-04-    -36
 20|                          701-002                                 and U wave                                                                                                                    07.xml       Lab                                                 1           15T11:58
 21| 10    XYZ       EG       XYZ-US-   10      334PT89   CHYPTENL    Chamber Hypertrophy   FINDING         SUPINE   LEFT VENTRICULAR                  LEFT VENTRICULAR                             PQW436789-   Test                                     1          Screening   2003-04-    -36
~~~~

KB 现文: `knowledge_base/domains/EG/examples.md:33-33` (来源: near triage kb_loc knowledge_base/domains/EG/examples.md:33 (score 0.967)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  33| | 9 | XYZ | EG | XYZ-US-701-002 | 9 | 334PT89 | STSTWUW | ST Segment, T wave, and U wave | FINDING | SUPINE | PROLONGED QT | | PROLONGED QT | | | PQW436789-07.xml | Test Lab | | | | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 24. `ig34_p0353_a015` — human:VALUE_DIFF

- PDF 页 353 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-TU`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | STUDY01 | TU | 40913 | 2 | L01-1 | VSLIDENT | Vessel Lesion Identification | TARGET | TARGET | AORTO-ILIAC PERIPHERAL ARTERY | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0353.txt` 第 28-30 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27|                                                   Identification                                 AORTA                                                        02-01
 28| 2   STUDY01 TU     40913   2     L01-1   VSLIDENT Vessel Lesion                 TARGET  TARGET   AORTO-ILIAC   LEFT  ANGIOGRAPHY INVESTIGATOR 1        SCREEN 2007-
 29|                                                   Identification                                 PERIPHERAL                                                   02-01
 30|                                                                                                  ARTERY
 31| 3        STUDY01 TU      40913    3       L01-2     LMLIDENT   Limb Lesion      TARGET  TARGET   LEG           LEFT   ANGIOGRAPHY INVESTIGATOR 1      SCREEN 2007-
~~~~

KB 现文: `knowledge_base/domains/TU/examples.md:24` (来源: decision.evidence.hit):

~~~~
  24| | 2 | STUDY01 | TU | 40913 | 2 | L01-1 | VSLIDENT | Vessel Lesion Identification | TARGET | TARGET | AORTO-ILIAC PERIPHERAL ARTERY | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 25. `ig34_p0371_a018` — human:VALUE_DIFF

- PDF 页 371 · 原子类型 TABLE_ROW · 所在节 `FA – Examples`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-FA`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | ABC | MH | 001-001 | 1 | RHEUMATOID ARTHRITIS | Rheumatoid arthritis | DIAGNOSIS | RHEUMATOID ARTHRITIS HISTORY |  | Y | Y |  |  | 2003 |  |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0371.txt` 第 25-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24| Row STUDYID DOMAIN USUBJID MHSEQ MHTERM     MHDECOD MHEVDTYP MHCAT                                   MHSCAT       MHPRESP MHOCCUR MHSEV     MHDTC MHSTDTC MHEVLINT
 25| 1   ABC     MH     001-001 1     RHEUMATOID Rheumatoid DIAGNOSIS RHEUMATOID                                       Y       Y                       2003
 26|                                  ARTHRITIS  arthritis            ARTHRITIS
 27|                                                                  HISTORY
 28| 2   ABC     MH     001-001 2     JOINT      Joint                RHEUMATOID                          RHEUMATOID   Y      Y        SEVERE    2006-            -P6M
~~~~

KB 现文: `knowledge_base/domains/FA/examples.md:155` (来源: decision.evidence.hit):

~~~~
 155| | 1 | ABC | MH | 001-001 | 1 | RHEUMATOID ARTHRITIS | Rheumatoid arthritis | DIAGNOSIS | RHEUMATOID ARTHRITIS HISTORY | | Y | Y | | | 2003 | |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

## human:IE

### 26. `ig34_p0122_a009` — human:IE

- PDF 页 122 · 原子类型 TABLE_ROW · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_030`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
MLELTM | Planned Elapsed Time from Time Point Ref | Char | ISO 8601 duration | Timing | Planned elapsed time (in ISO 8601 values) relative to the planned fixed reference (MLTPREF). This variable is useful when there are repetitive measures. Not a clock time or a date/time variable. Represented as an ISO 8601 duration. | Perm
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0122.txt` 第 19-21 行 (自动定位, 词覆盖 0.947; 版式以原 PDF 为准):

~~~~
 18| MLTPTNUM        Planned Time Point Number       Num                            Timing         Numeric version of planned time point used in sorting.                                             Perm
 19| MLELTM          Planned Elapsed Time from       Char ISO 8601 duration         Timing         Planned elapsed time (in ISO 8601) relative to the planned fixed reference (MLTPTREF). This        Perm
 20|                 Time Point Ref                                                                variable is useful when there are repetitive measures. Not a clock time or a date/time variable.
 21|                                                                                               Represented as an ISO 8601 duration.
 22| MLTPTREF        Time Point Reference            Char                           Timing         Description of the fixed reference point referred to by MLELTM, MLTPTNUM, and MLTPT.               Perm
~~~~

KB 现文: `knowledge_base/domains/ML/spec.md:284-292` (来源: 按变量名 MLELTM 定位 (IE 行: KB 以 spec/model 表另一格式承载)):

~~~~
 284| ### MLELTM
 285| - **Order:** 32
 286| - **Label:** Planned Elapsed Time from Time Point Ref
 287| - **Type:** Char
 288| - **Controlled Terms:** ISO 8601 duration
 289| - **Role:** Timing
 290| - **Core:** Perm
 291| - **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to the planned fixed reference (MLTPTREF). This variable is useful when there are repetitive measures. Not a clock time or a date/time variable. Represented as an ISO 8601 duration.
 292| 
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 27. `ig34_p0188_a003` — human:IE

- PDF 页 188 · 原子类型 TABLE_ROW · 所在节 `§6.3.3 ECG Test Results (EG)`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_020`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| EGTPTREF | Time Point Reference | Char | | Timing | Name of the fixed reference point referred to by EGELTM, EGTPTNUM, and EGTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0188.txt` 第 8-9 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7|                                                                                                      after the reference point indicated by EGTPTREF.
  8| EGTPTREF         Time Point            Char                                                  Timing  Name of the fixed reference point referred to by EGELTM, EGTPTNUM, and EGTPT.      Perm
  9|                  Reference                                                                           Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
 10|  EGRFTDTC Date/Time of                 Char ISO 8601 datetime or interval                    Timing  Date/time for a fixed reference time point defined by EGTPTREF.                    Perm
~~~~

KB 现文: `knowledge_base/domains/EG/spec.md:383-391` (来源: 按变量名 EGTPTREF 定位 (IE 行: KB 以 spec/model 表另一格式承载)):

~~~~
 383| ### EGTPTREF
 384| - **Order:** 43
 385| - **Label:** Time Point Reference
 386| - **Type:** Char
 387| - **Controlled Terms:** 
 388| - **Role:** Timing
 389| - **Core:** Perm
 390| - **CDISC Notes:** Name of the fixed reference point referred to by EGELTM, EGTPTNUM, and EGTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
 391| 
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 28. `ig34_p0295_a021` — human:IE

- PDF 页 295 · 原子类型 TABLE_ROW · 所在节 `§6.3.7.4 Nervous System Findings (NV)`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_022`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| VISIT | Visit Name | Char | | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0295.txt` 第 42-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 41| VISITNUM       Visit Number                    Num                         Timing      Clinical encounter number. Numeric version of VISIT, used for sorting.                                                                                                Exp
 42| VISIT          Visit Name                      Char                        Timing      Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.                                                               Perm
 43| VISITDY        Planned Study Day of Visit      Num                         Timing      Planned study day of the visit based upon RFSTDTC in Demographics.                                                                                                    Perm
~~~~

KB 现文: `knowledge_base/domains/NV/spec.md:284-292` (来源: 按变量名 VISIT 定位 (IE 行: KB 以 spec/model 表另一格式承载)):

~~~~
 284| ### VISIT
 285| - **Order:** 32
 286| - **Label:** Visit Name
 287| - **Type:** Char
 288| - **Controlled Terms:** 
 289| - **Role:** Timing
 290| - **Core:** Perm
 291| - **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
 292| 
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 29. `ig34_p0309_a014` — human:IE

- PDF 页 309 · 原子类型 TABLE_ROW · 所在节 `§6.3.7.7 Respiratory System Findings (RE)`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_016`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| REEVALID | Evaluator Identifier | Char | (MEDEVAL) | Variable Qualifier | Used to distinguish multiple evaluators with the same role recorded in REEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0309.txt` 第 33-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 32|                                                                                   ASSESSOR", "RADIOLOGIST".
 33| REEVALID       Evaluator Identifier      Char (MEDEVAL)            Variable       Used to distinguish multiple evaluators with the same role recorded in REEVAL. Examples:                  Perm
 34|                                                                    Qualifier      "RADIOLOGIST1", "RADIOLOGIST2".
 35| REREPNUM       Repetition Number         Num                       Record         The instance number of a test that is repeated within a given time frame for the same test. The level     Perm
~~~~

KB 现文: `knowledge_base/domains/RE/spec.md:302-310` (来源: 按变量名 REEVALID 定位 (IE 行: KB 以 spec/model 表另一格式承载)):

~~~~
 302| ### REEVALID
 303| - **Order:** 34
 304| - **Label:** Evaluator Identifier
 305| - **Type:** Char
 306| - **Controlled Terms:** (MEDEVAL) C96777
 307| - **Role:** Variable Qualifier
 308| - **Core:** Perm
 309| - **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in REEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2".
 310| 
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 30. `sv20_p0046_a005` — human:IE

- PDF 页 46 · 原子类型 TABLE_ROW · 所在节 `§3.2.3.1 [Subject Elements]`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_032`
- IE 类别 `VERSION_MISMATCH` · 排除理由: Tier B T1 IE (VERSION_MISMATCH; ruling:R1-row)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
3 | USUBJID | Unique Subject Identifier | Char | | Identifier | | | C69256 | A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product. | | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0046.txt` 第 14-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13|                                                                                                            specific commonality.
 14| 3   USUBJID     Unique Subject     Char               Identifier                                C69256     A sequence of characters used
 15|                 Identifier                                                                                 to uniquely identify a subject
 16|                                                                                                            across all studies for all
 17|                                                                                                            applications or submissions
 18|                                                                                                            involving the product.
 19| 4   SESEQ       Sequence           Num                Identifier                                                                              Sequence number to ensure uniqueness within
~~~~

KB 现文: `knowledge_base/model/03_special_purpose_domains.md:131-131` (来源: 按变量名 USUBJID 定位 (IE 行: KB 以 spec/model 表另一格式承载)):

~~~~
 131| | 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

## human:RISK_ANCHORLESS

### 31. `ig34_p0065_a022` — human:RISK_ANCHORLESS

- PDF 页 65 · 原子类型 CROSS_REF · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_004`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
See Section 7.2.1, Trial Arms, Example Trial 3
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0065.txt` 第 34-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 33|         b.   Multistage assignment to treatment: Some trials use a multistage process for assigning a subject to an
 34|              arm (see Section 7.2.1, Trial Arms, Example Trial 3). In such a case, best practice is to create ARMCD
 35|              values composed of codes representing the results of the multiple stages of the treatment assignment
~~~~

KB 现文: `knowledge_base/domains/DM/assumptions.md:25` (来源: decision.evidence.hit):

~~~~
  25|    b. Multistage assignment to treatment: Some trials use a multistage process for assigning a subject to an arm (see Section 7.2.1, Trial Arms, Example Trial 3). In such a case, best practice is to create ARMCD values composed of codes representing the results of the multiple stages of the treatment assignment process. If a subject is partially assigned, then truncated codes representing the stages completed can be used in ARMCD, and similar truncated codes can be used in ACTARMCD. The descriptions used to populate ARM and ACTARM should be similarly truncated, and the one-to-one relationship between these truncated codes should be maintained for all affected subjects in the trial. Example 3 below provides an example of this situation; see also Section 5.3, Subject Elements, Example 2. Note that this use of values not in the TA dataset is allowable only for trials with multistage assignment to arms and to subjects in those trials who do not complete all stages of the assignment.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 32. `ig34_p0071_a015` — human:RISK_ANCHORLESS

- PDF 页 71 · 原子类型 NOTE · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_004`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0072.txt` 第 52-60 行 (自动定位, 词覆盖 0.833; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 51|                        (More than one              report race, with
 52|                        choice is acceptable.)      race being
 53|                                                    asked about
 54|                                                    after ethnicity.
 55| If study participant answered: AMERICAN INDIAN OR ALASKA NATIVE
 56| CRACE01- 10            Which of the following Race Select each       Text   SUPPDM.QVAL   For each value that   (RACEC)       ALASKA NATIVE; AMERICAN                           checkbox
 57| CRACE04                racial designations         value that                             applies,                            INDIAN; CARIBBEAN INDIAN;
 58|                        best describes you?         applies if the                         SUPPDM.QVAL where                   CENTRAL AMERICAN
 59|                                                    subject                                SUPPDM.QNAM                         INDIAN;
 60|                                                    answered                               ="CRACEn" and
 61| 
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:188,190,192,194,340,342` (来源: decision.evidence.hit):

> 同一文件共 6 处逐字命中 (行 188, 190, 192, 194, 340, 342); 请按 PDF 所在例/表判断对应的是哪一处

~~~~
 188| | CRACE01-CRACE04 | 10 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "AMERICAN INDIAN OR ALASKA NATIVE". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ALASKA NATIVE; AMERICAN INDIAN; CARIBBEAN INDIAN; CENTRAL AMERICAN INDIAN; | | | checkbox | |
 190| | CRACE05-CRACE10 | 11 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "ASIAN". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ASIAN AMERICAN; ASIAN INDIAN; BANGLADESHI; CHINESE; JAPANESE; KOREAN; | | | checkbox | CRACE05-CRACE10 |
 192| | CRACE11-CRACE17 | 12 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "BLACK OR AFRICAN AMERICAN". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | AFRICAN; AFRICAN AMERICAN; AFRICAN CARIBBEAN; BAHAMIAN; BARBADIAN; BLACK; BLACK CENTRAL AMERICAN; | | | checkbox | |
 194| | CRACE18-CRACE21 | 13 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "WHITE". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ARAB; EUROPEAN; MIDDLE EASTERN; RUSSIAN; | | | checkbox | |
 340| | CRACE05-CRACE10 | 11 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "ASIAN". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ASIAN AMERICAN; ASIAN INDIAN; BANGLADESHI; CHINESE; JAPANESE; KOREAN; | | | checkbox | |
 342| | CRACE11-CRACE17 | 12 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "BLACK OR AFRICAN AMERICAN". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | AFRICAN; AFRICAN AMERICAN; AFRICAN CARIBBEAN; BAHAMIAN; BARBADIAN; BLACK; BLACK CENTRAL AMERICAN; | | | checkbox | |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 33. `ig34_p0120_a004` — human:RISK_ANCHORLESS

- PDF 页 120 · 原子类型 TABLE_ROW · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_013`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC | EC | ABC7001 | 2 | BOTTLE A | EXCEPTION DOSE | Y | N | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0120.txt` 第 4-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3| 1        ABC       EC       ABC7001   1       BOTTLE A   FIRST TO LAST DOSE INTERVAL   Y         Y       1      TABLET       QD            TREATMENT      2012-01-13   2012-01-20   1        8
  4| 2        ABC       EC       ABC7001   2       BOTTLE A   EXCEPTION DOSE                Y         N              TABLET       QD            TREATMENT      2012-01-15   2012-01-15   3        3
  5| 3        ABC       EC       ABC7001   3       BOTTLE A   EXCEPTION DOSE                Y         Y       2      TABLET       QD            TREATMENT      2012-01-16   2012-01-16   4        4
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:446` (来源: decision.evidence.hit):

~~~~
 446| | 2 | ABC | EC | ABC7001 | 2 | BOTTLE A | EXCEPTION DOSE | Y | N | | TABLET | QD | TREATMENT | 2012-01-15 | 2012-01-15 | 3 | 3 |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 34. `ig34_p0157_a0026` — human:RISK_ANCHORLESS

- PDF 页 157 · 原子类型 LIST_ITEM · 所在节 `§6.2.4 Disposition (DS)`
- triage 类 **-** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `S-EVT`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Reasons for termination: ICH E3 Section 10.1 indicates that "the specific reason for discontinuation" should be presented, and that summaries should be "grouped by treatment and by major reason."
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0157.txt` 第 30-31 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 29|                EPOCH are drawn from the Trial Arms (TA) dataset (see Section 7.2.1, Trial Arms).
 30|      5.   Reasons for termination: ICH E3 Section 10.1 indicates that “the specific reason for discontinuation” should be presented, and that summaries should be
 31|           “grouped by treatment and by major reason.” The CDISC SDS Team interprets this guidance as requiring 1 standardized disposition term (DSDECOD)
 32|           per disposition event. If multiple reasons are reported, the sponsor should identify a primary reason and use that to populate DSTERM and DSDECOD.
~~~~

KB 现文: `knowledge_base/domains/DS/assumptions.md:43` (来源: decision.evidence.hit):

~~~~
  43| 5. Reasons for termination: ICH E3 Section 10.1 indicates that “the specific reason for discontinuation” should be presented, and that summaries should be “grouped by treatment and by major reason.” The CDISC SDS Team interprets this guidance as requiring 1 standardized disposition term (DSDECOD) per disposition event. If multiple reasons are reported, the sponsor should identify a primary reason and use that to populate DSTERM and DSDECOD. Additional reasons should be submitted in SUPPDS.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 35. `ig34_p0171_a0002` — human:RISK_ANCHORLESS

- PDF 页 171 · 原子类型 TABLE_ROW · 所在节 `§6.2.5 Healthcare Encounters (HO)`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-HO`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 10 | ABC | HO | ABC123102 | 3 | ICU | | INITIAL HOSPITALIZATION | 2011-06-25T10:00 | 2011-06-29T19:30 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0171.txt` 第 3-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2| 9     ABC        HO         ABC123102      2       ICU                                   INITIAL HOSPITALIZATION          2011-06-19T22:00   2011-06-23T09:30
  3| 10    ABC        HO         ABC123102      3       ICU                                   INITIAL HOSPITALIZATION          2011-06-25T10:00   2011-06-29T19:30
  4| 11    ABC        HO         ABC123102      4       SKILLED NURSING FACILITY              FOLLOW-UP CARE                   2011-07-02                              ONGOING       END OF STUDY
~~~~

KB 现文: `knowledge_base/domains/HO/examples.md:72` (来源: decision.evidence.hit):

~~~~
  72| | 10 | ABC | HO | ABC123102 | 3 | ICU | INITIAL HOSPITALIZATION | 2011-06-25T10:00 | 2011-06-29T19:30 | | |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 36. `ig34_p0209_a006` — human:RISK_ANCHORLESS

- PDF 页 209 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-CP`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 14-15: The NK cell lineage of leukocytes is determined using a set of lineage-specific markers in addition to the CD45 leukocyte marker, to define the subpopulation both in terms of positive (i.e., CD56+) and negative (i.e., CD3-, CD19-, and CD14-) marker expression. The order of markers in CPMRKSTR follows the same convention described for B-lymphocytes in rows 4 and 5. In addition, the sponsor chose to include the FSC and SSC properties as markers because they are used, in part, to differentiate the natural killer cell and lymphocyte populations. Note that when FSC and SSC are used in a marker string, they usually go last, whereas they often come first when showing a gating strategy.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0209.txt` 第 38-44 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 37|             they usually go last, whereas they often come first when showing a gating strategy.
 38| Rows 14-15: The NK cell lineage of leukocytes is determined using a set of lineage-specific markers in addition to
 39|             the CD45 leukocyte marker, to define the subpopulation both in terms of positive (i.e., CD56+) and
 40|             negative (i.e., CD3-, CD19-, and CD14-) marker expression. The order of markers in CPMRKSTR
 41|             follows the same convention described for B-lymphocytes in rows 4 and 5. In addition, the sponsor
 42|             chose to include the FSC and SSC properties as markers because they are used, in part, to differentiate
 43|             the natural killer cell and lymphocyte populations. Note that when FSC and SSC are used in a marker
 44|             string, they usually go last, whereas they often come first when showing a gating strategy.
 45| Row 16:       The ratio of T helper to T cytotoxic lymphocytes is calculated from the T helper (CD4+) cell count in
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:25` (来源: decision.evidence.hit):

~~~~
  25| **Rows 14-15:** The NK cell lineage of leukocytes is determined using a set of lineage-specific markers in addition to the CD45 leukocyte marker, to define the subpopulation both in terms of positive (i.e., CD56+) and negative (i.e., CD3-, CD19-, and CD14-) marker expression. The order of markers in CPMRKSTR follows the same convention described for B-lymphocytes in rows 4 and 5. In addition, the sponsor chose to include the FSC and SSC properties as markers because they are used, in part, to differentiate the natural killer cell and lymphocyte populations. Note that when FSC and SSC are used in a marker string, they usually go last, whereas they often come first when showing a gating strategy.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 37. `ig34_p0210_a022` — human:RISK_ANCHORLESS

- PDF 页 210 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-CP`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 4: Illustrates an alternative way a sponsor chose to construct the value of CPMRKSTR using the gate name in CPGATE (operationally defined in CPGATDEF) as the denominator. Although the preferred method for constructing CPMRKSTR is to use markers to define both the numerator and denominator, the method shown in this example for designating the denominator can be useful, particularly when the denominator string is merely a very long repeat of the majority of markers in the numerator.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0210.txt` 第 44-46 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 43|                CPMRKSTR, where they are used to distinguish between the lymphocyte and other leukocyte lineages.
 44| Row 4:         Illustrates an alternative way a sponsor chose to construct the value of CPMRKSTR using the gate name in CPGATE (operationally defined in CPGATDEF) as the denominator. Although the preferred
 45|                method for constructing CPMRKSTR is to use markers to define both the numerator and denominator, the method shown in this example for designating the denominator can be useful, particularly
 46|                when the denominator string is merely a very long repeat of the majority of markers in the numerator.
 47| cp.xpt
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:56` (来源: decision.evidence.hit):

~~~~
  56| **Row 4:** Illustrates an alternative way a sponsor chose to construct the value of CPMRKSTR using the gate name in CPGATE (operationally defined in CPGATDEF) as the denominator. Although the preferred method for constructing CPMRKSTR is to use markers to define both the numerator and denominator, the method shown in this example for designating the denominator can be useful, particularly when the denominator string is merely a very long repeat of the majority of markers in the numerator.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 38. `ig34_p0389_a008` — human:RISK_ANCHORLESS

- PDF 页 389 · 原子类型 SENTENCE · 所在节 `§7.2.1 Trial Arms (TA) – Example 1`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-TA`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
For Example Trial 1, the conversion of the trial design matrix into the TA dataset is straightforward. For each cell of the matrix, there is a record in the TA dataset. ARM, EPOCH, and ELEMENT can be populated directly from the matrix. TAETORD acts as a sequence number for the elements within an arm, so it can be populated by counting across the cells in the matrix. The randomization information, which is not represented in the trial design matrix, is held in TABRANCH in the TA dataset. TABRANCH is populated only if there is a branch at the end of an element for the arm. When TABRANCH is populated, it describes how the decision at the branch point would result in a subject being in this arm.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0389.txt` 第 17-23 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 16| 
 17| For Example Trial 1, the conversion of the trial design matrix into the TA dataset is straightforward. For each cell of
 18| the matrix, there is a record in the TA dataset. ARM, EPOCH, and ELEMENT can be populated directly from the
 19| matrix. TAETORD acts as a sequence number for the elements within an arm, so it can be populated by counting
 20| across the cells in the matrix. The randomization information, which is not represented in the trial design matrix, is
 21| held in TABRANCH in the TA dataset. TABRANCH is populated only if there is a branch at the end of an element
 22| for the arm. When TABRANCH is populated, it describes how the decision at the branch point would result in a
 23| subject being in this arm.
 24| ta.xpt
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:147` (来源: decision.evidence.hit):

~~~~
 147| For Example Trial 1, the conversion of the trial design matrix into the TA dataset is straightforward. For each cell of the matrix, there is a record in the TA dataset. ARM, EPOCH, and ELEMENT can be populated directly from the matrix. TAETORD acts as a sequence number for the elements within an arm, so it can be populated by counting across the cells in the matrix. The randomization information, which is not represented in the trial design matrix, is held in TABRANCH in the TA dataset. TABRANCH is populated only if there is a branch at the end of an element for the arm. When TABRANCH is populated, it describes how the decision at the branch point would result in a subject being in this arm.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 39. `ig34_p0342_a022` — human:RISK_ANCHORLESS

- PDF 页 342 · 原子类型 SENTENCE · 所在节 `SS – Specification`
- triage 类 **-** · 终态 **EXACT** (T3 前 INTENTIONAL_EXCLUDE) · 判定规则 `live-hit` · 批 `S-FND`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
ss.xpt, Subject Status — Findings. One record per status per visit per subject, Tabulation.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0342.txt` 第 42-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 41| SS – Specification
 42| ss.xpt, Subject Status — Findings. One record per status per visit per subject, Tabulation.
 43| Variable           Variable Label      Type Controlled Terms,     Role             CDISC Notes                                                                                       Core
~~~~

KB 现文: `knowledge_base/domains/SS/assumptions.md:9` (来源: decision.evidence.hit):

~~~~
   9| ss.xpt, Subject Status — Findings. One record per status per visit per subject, Tabulation.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 40. `ig34_p0367_a001` — human:RISK_ANCHORLESS

- PDF 页 367 · 原子类型 LIST_ITEM · 所在节 `FA – Assumptions`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `live-hit` · 批 `S-TUFA`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
5. When data collection establishes a relationship between FA records and an events or interventions record, the relationship should be represented in RELREC.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0367.txt` 第 1-2 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1|      5.   When data collection establishes a relationship between FA records and an events or interventions record, the relationship should be represented in
  2|           RELREC.
  3|           a.   The FAOBJ variable alone is not sufficient to establish a relationship, because an events or interventions dataset may have multiple records for the
~~~~

KB 现文: `knowledge_base/domains/FA/assumptions.md:114` (来源: decision.evidence.hit):

~~~~
 114| 5. When data collection establishes a relationship between FA records and an events or interventions record, the relationship should be represented in RELREC.
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 41. `ig34_p0367_a013` — human:RISK_ANCHORLESS

- PDF 页 367 · 原子类型 TABLE_ROW · 所在节 `FA – Examples`
- triage 类 **REWRITE_OK** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_015`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Associated symptoms: Sensitivity to light Sensitivity to sound Nausea Aura | ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0367.txt` 第 18-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| Severity of migraine             ○ Mild ○ Moderate ○ Severe
 18| Associated symptoms:
 19| Sensitivity to light                ○ No   ○ Yes
 20| Sensitivity to sound                ○ No   ○ Yes
 21| Nausea                              ○ No   ○ Yes
 22| Aura
 23|                                     ○ No   ○ Yes
~~~~

KB 现文: `knowledge_base/domains/FA/examples.md:14,17,20` (来源: decision.evidence.hit):

> 同一文件共 3 处逐字命中 (行 14, 17, 20); 请按 PDF 所在例/表判断对应的是哪一处

~~~~
  14| | Associated symptoms: Sensitivity to light Sensitivity to sound Nausea Aura | ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes |
  17| | Associated symptoms: Sensitivity to light Sensitivity to sound Nausea Aura | ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes |
  20| | Associated symptoms: Sensitivity to light Sensitivity to sound Nausea Aura | ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes ○ No   ○ Yes |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

### 42. `ig34_p0369_a024` — human:RISK_ANCHORLESS

- PDF 页 369 · 原子类型 TABLE_ROW · 所在节 `FA – Examples`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `T1:pack_015`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Scars | ○ 0   ○ 1 to 25   ○ 26 to 100   ○ 101 to 200   ○ 201 to 300   ○ >300 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0369.txt` 第 40-40 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39| Scabs                              ○0    ○ 1 to 25       ○ 26 to 100     ○ 101 to 200         ○ 201 to 300    ○ >300
 40| Scars                              ○0    ○ 1 to 25       ○ 26 to 100     ○ 101 to 200         ○ 201 to 300    ○ >300
 41| 
~~~~

KB 现文: `knowledge_base/domains/FA/examples.md:87` (来源: decision.evidence.hit):

~~~~
  87| | Scars | ○ 0   ○ 1 to 25   ○ 26 to 100   ○ 101 to 200   ○ 201 to 300   ○ >300 |
~~~~

**用户判定**: ☐ 内容正确　☐ 内容错误　☐ 看不出 / 需查原 PDF

备注: 

