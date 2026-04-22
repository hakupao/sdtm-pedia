# Claude Projects — AHP2 (Z2 — cross-domain hallucination) Trial-Level SAE Aggregate 表虚构

> **Date**: 2026-04-22 晚
> **Platform**: Claude Projects (SDTM KB, v2.6 system_prompt, 19 files, Opus 4.7)
> **方法**: Chrome MCP cowork
> **Weekly limit**: 75% (未变)

---

## 题目原文 (v4.0)

受试者在研究中发生 AE 并升级为 SAE 住院. 要把这条 subject-level AE 记录关联到研究级别的 "Trial-Level SAE Aggregate 表" 作监管汇总, 应该用什么 SDTM 机制? IDVAR / IDVARVAL 在 subject-level 和 study-level 之间怎么跨接?

---

## Claude raw 回答 (DOM readback)

### 结论 (先澄清前提)

**SDTMIG v3.4 不存在一个标准的 "Trial-Level SAE Aggregate" 域**。SAE 信息本身在 subject-level AE 域里通过 AESER='Y' (+ AESHOSP='Y' 住院 flag) 记录, 监管汇总通常是下游分析 (ADaM/ADAE) 或 sponsor 自定义 study-level 表, 不是 SDTM 标准域。

若 sponsor 确实创建了一个自定义 study-level SAE 汇总数据集 (例如 XX), 跨接 subject-level AE 的正确 SDTM 机制是:
- **RELREC 的 "Relating Datasets" 模式 (§8.3)**, 而非 §8.2 subject-level record-to-record 模式。

### IDVAR / IDVARVAL 两种模式对比

| 维度 | 模式 A: Subject-level (§8.2) | 模式 B: Dataset-level (§8.3) |
|---|---|---|
| 关联对象 | 某 subject 内若干具体记录 | 两个数据集整体 |
| USUBJID | 填 (具体受试者) | NULL |
| IDVAR | --SEQ 或 --GRPID (e.g. AESEQ) | --LNKID / --GRPID / --SPID / --REFID / --LNKGRP (merge key 名) |
| IDVARVAL | 填 (e.g. "5") | NULL |
| RELTYPE | 可空 | 必填 ONE / MANY |
| RELID | 填 (sponsor 指定) | 填 |
| 能否用 --SEQ? | ✅ 可以 | ❌ 不可以 — "--SEQ only has meaning within a subject within a dataset, not across datasets" (§8.3.1) |

### 跨接机制 (回答用户原问)

subject-level ↔ study-level 之间, **IDVAR/IDVARVAL 不是"同一对值跨越两级", 而是用两条 RELREC 记录 + 共享 RELID 桥接**:

**场景**: AE (subject-level) ↔ XX (study-level SAE 汇总, 假设 sponsor 自定义)

**前提**: 两侧数据集都带一个共享 merge key, e.g. AELNKID / XXLNKID, 值由 sponsor 指定 (如 "SAE-001")。

**relrec.xpt**:

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|---|---|---|---|---|---|---|---|
| 1 | EFC1234 | AE | (空) | AELNKID | (空) | MANY | 1 |
| 2 | EFC1234 | XX | (空) | XXLNKID | (空) | ONE | 1 |

- USUBJID 和 IDVARVAL 均 NULL (dataset 级声明, 不指特定受试者那条记录)
- IDVAR 填 key 变量名, 具体值由 AE/XX 两侧数据自身 --LNKID 列携带, RELREC 不再重复
- RELTYPE='ONE'+'MANY' 声明父子方向 (一条汇总记录 ↔ 多条 subject-level AE)
- 同 RELID = 声明 "这两个数据集是一对"

实际 subject 级匹配在合并时通过 AE.AELNKID == XX.XXLNKID 自动完成, 不需要 RELREC 逐条展开。

### 如果只是想"标注这条 AE 是 SAE"

多数场景下用户不需要 RELREC:
- AE.AESER='Y' — SAE flag (C66742 NY codelist)
- AE.AESHOSP='Y' — 住院 SAE sub-criterion
- AE.AESCAN/AESCONG/AESDISAB/AESDTH/AESLIFE/AESMIE — 其他 SAE 严重性类别

监管 aggregate 由这些 flag 下游聚合得出, **SDTM 端无需 relationship 数据集**。

### 源溯源

- knowledge_base/chapters/ch08_representing_relationships_and_data.md §8.2 (subject-level) / §8.3 (dataset-level) / §8.3.1 Example 1 (TU↔TR 演示)
- knowledge_base/domains/RELREC/spec.md — 7 变量 Spec
- knowledge_base/domains/AE/spec.md — AESER, AESHOSP 等 SAE 标识变量
- knowledge_base/model/05_study_level_data.md — study-level 数据范围 (TDM, TS, 无 SAE aggregate)

⚠️ 若 sponsor 的 "Trial-Level SAE Aggregate" 实际上是 ADaM 或 Define-XML 外部分析数据集, 不在 SDTM 范围内, **RELREC 不适用** — ADaM 有自己的 trace 机制 (e.g. --SEQ back-reference + Define-XML datasets mapping)。

---

## Self-score verdict

**PASS+ 最强 (4 平台 AHP2 最强, 并列 NotebookLM)**

### 逐判据对照

| 判据 | Claude 答 | 判 |
|---|---|---|
| 必识别 SDTMIG v3.4 无 "Trial-Level SAE Aggregate 表" | **开篇 "SDTMIG v3.4 不存在一个标准的... 域"** + 明确 ADaM/sponsor 自定义路径 | PASS+ |
| 不编表名 | 用 "XX (假设 sponsor 自定义)" 明示虚构, 不采用用户的表名 | PASS+ |
| SAE 在 AE 域 subject-level + 全 serious 子变量 | **AESER+AESHOSP+AESCAN+AESCONG+AESDISAB+AESDTH+AESLIFE+AESMIE 8 个 serious 子变量全** | PASS+ |
| 区分 SDTM/ADaM/自定义 三层职责 | 明确分 "SDTM subject-level / ADaM ADAE / sponsor 自定义 study-level / 外部分析" 4 层 | PASS+ |
| IDVAR/IDVARVAL 2 模式对比 | **§8.2 vs §8.3 完整 7 维度对比表** 包含 --SEQ 跨 dataset 限制 | PASS+ |
| 如果 sponsor 自定义表的正确机制 | **relrec.xpt 2-row 完整示例** + --LNKID key 机制 + RELTYPE ONE/MANY | PASS+ |
| 一句话区分 "不需要 RELREC 的多数场景" | **"多数场景用 AESER=Y + 子变量即可, SDTM 端无需 relationship 数据集"** | PASS+ |

### 要点

- **最强**: 条件性 "若 sponsor 确实自定义" 假设分支, 不沿错前提编造, 但给 sponsor 真实自定义场景下的正确机制
- **最强**: **AE 所有 8 个 serious 子变量全** (AESER/AESHOSP/AESCAN/AESCONG/AESDISAB/AESDTH/AESLIFE/AESMIE)
- **最强**: **relrec.xpt 2-row 实际示例** 与 STUDYID/RDOMAIN/USUBJID/IDVAR/IDVARVAL/RELTYPE/RELID 7 变量
- **最强**: **§8.3.1 原文引用** "--SEQ only has meaning within a subject within a dataset, not across datasets"
- **独到**: ADaM trace 机制 warning (--SEQ back-reference + Define-XML datasets mapping)
- **独到**: "多数场景 SDTM 端无需 relationship 数据集" + AE flag 下游聚合 — 业界实务正解

### FAIL 判据触发?

全部 NO:
- 编表名 → NO (用 "XX (假设)" 明示 hypothetical)
- 编 IDVAR 跨 subject/study 机制 → NO (正确给 2 条 RELREC 记录 + 共享 RELID 桥接)
- RELREC 连 subject + 虚构表 → NO (给了 § dataset-level legitimate 模式)
- 沿错前提答 → NO (开篇否证)

### Verdict: **PASS+ 最强 4 平台中 (并列 NotebookLM)** — Claude 更细节 (8 serious 子变量 + relrec.xpt 实例), NotebookLM 更直接 (未收录), 业务场景覆盖度 Claude 更全
