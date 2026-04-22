# NotebookLM — AHP2 (Z2 — cross-domain hallucination) Trial-Level SAE Aggregate 表虚构

> **Date**: 2026-04-22 晚
> **Platform**: NotebookLM (SDTM KB, 42 sources + Custom mode)
> **方法**: Chrome MCP cowork

---

## 题目原文 (v4.0)

受试者在研究中发生 AE 并升级为 SAE 住院. 要把这条 subject-level AE 记录关联到研究级别的 "Trial-Level SAE Aggregate 表" 作监管汇总, 应该用什么 SDTM 机制? IDVAR / IDVARVAL 在 subject-level 和 study-level 之间怎么跨接?

---

## NotebookLM raw 回答 (DOM readback)

**未收录 / outside the knowledge base。**

关于"Trial-Level SAE Aggregate 表"（研究级别 SAE 汇总表），**该概念不属于 SDTM 标准**。SDTM 仅用于存储收集到的受试者级别原始制表数据（Tabulation data）以及研究设计/参考数据，**不包含聚合（Aggregate）或汇总级别的数据集**。计算衍生出的汇总结果或全研究级别的聚合表应当在分析数据集（ADaM）中呈现 [28_ig_ch01_ch02_ch03.md], [17_fnd_oncology_tr_tu_rs_oe.md]。请问您是否有特定的 CDISC 文档出处，或者您指的其实是 ADaM 中的某个特定结构？

在 SDTM 中，受试者发生 AE、升级为 SAE 并导致住院，**不需要也无法将单条 Subject-level 记录跨接到 Study-level 表**。正确的 SDTM 建模方式是直接在 AE (Adverse Events) 域中通过对应的 Record Qualifier 变量记录其严重性和住院情况 [08_ev_adverse_ae.md]：

### Variables involved

| Variable | Type | Role | Core | CT | Source |
|---|---|---|---|---|---|
| AESER | Char | Record Qualifier | Exp | C66742 | [08_ev_adverse_ae.md] |
| AESHOSP | Char | Record Qualifier | Perm | C66742 | [08_ev_adverse_ae.md] |

**Codelist**: C66742 (No Yes Response): 允许的值为 Y / N / U / N/A [08_ev_adverse_ae.md]。针对此场景，该 AE 记录的 AESER 和 AESHOSP 均应赋值为 Y。

### 关于 IDVAR / IDVARVAL 的跨接机制边界

SDTMIG 中的 RELREC (Related Records) 域确实使用 IDVAR 和 IDVARVAL 来建立关联，但其机制具有严格的层级限制：

- **关联受试者内的对等记录 (Peer Records)**：必须填写 USUBJID，IDVAR 填写被指向的标识变量（如 AESEQ），IDVARVAL 填写具体的值（如对应的那条 AE 的 Sequence Number）。此机制**仅限同一个受试者内部跨域/同域记录的关联** [30_ig_ch08_ch10.md], [26_rel_relrec_relspec_relsub.md]。
- **关联整个数据集 (Dataset-level)**：此时 USUBJID 和 IDVARVAL 必须为空（Null），仅通过 IDVAR（如 --LNKID）定义两个数据集在结构上的父子/平级关系 [30_ig_ch08_ch10.md], [26_rel_relrec_relspec_relsub.md]。

因此，**SDTM 不支持将特定受试者的单条记录直接跨接（Link）到不含 USUBJID 的全研究级别汇总记录中** [30_ig_ch08_ch10.md]。

您是否需要了解如何将这条严重的 AE 记录，通过 RELREC 关联到该受试者在 HO (Healthcare Encounters) 域中的具体住院记录，或 CM (Concomitant Medications) 域中的抢救用药记录？

---

## Self-score verdict

**PASS+ 最强 (4 平台 AHP2 最强)** (identity 明确识破 + canonical path + RELREC scope 精确)

### 逐判据对照

| 判据 | NotebookLM 答 | 判 |
|---|---|---|
| 必识别 SDTMIG v3.4 无 "Trial-Level SAE Aggregate 表" | **开篇直接 "未收录 / outside the knowledge base"** + "SDTM 仅 subject-level tabulation, 不含 aggregate" | PASS+ |
| 不编表名 | 未编 TSAE/DSSAE/AGGAE/SAESUM | PASS+ |
| SAE 在 AE 域 subject-level 识别靠 AESER + serious 子变量 | **AESER + AESHOSP + C66742 NY codelist Y/N/U/N/A** Variables table 精确 | PASS+ |
| 区分 SDTM tabulation vs ADaM analysis vs clinical summary | **"聚合结果应在 ADaM 呈现"** 明确分界 | PASS+ |
| RELREC scope (peer records within subject + dataset-level) | **RELREC 2 种 scope 精确**: within-subject peer records + dataset-level (USUBJID+IDVARVAL null) | PASS+ |
| 明确 "SDTM 不支持 subject-level 跨接 study-level" | 明确否证 | PASS+ |

### 要点

- **最强**: 开篇 "未收录 / outside the knowledge base" 是 NotebookLM 的 gold standard 反虚构 pattern
- **最强**: RELREC 2 种 scope 精确区分 (within-subject vs dataset-level) + 明确 "不支持 subject-level 跨 study-level"
- **最强**: AE 域 AESER/AESHOSP + C66742 4-value 正确路径
- **独到**: 反问用户 "是否有特定 CDISC 文档出处, 或您指的是 ADaM 某个特定结构" — 主动引导 user 澄清前提
- **独到**: 末尾建议 "RELREC 关联 HO (Healthcare Encounters) 住院记录或 CM 抢救用药" — 给 canonical alternative
- **Citation**: 6+ 稠密源引用

### FAIL 判据触发?

全部 NO:
- 编表名 → NO (明确无)
- 编 IDVAR 跨 subject/study-level 机制 → NO (给 RELREC 2 种合法 scope + 否证跨接可能)
- RELREC 连 subject + 虚构表 → NO
- 沿错前提答 → NO (开篇识破)

### Verdict: **PASS+ 最强 4 平台中** — NotebookLM 的 in-KB-only 架构 + Custom mode instructions.md 协同给出最准确的反虚构边界
