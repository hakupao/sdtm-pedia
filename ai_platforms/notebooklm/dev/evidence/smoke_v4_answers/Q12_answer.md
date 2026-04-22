# NotebookLM — Q12 (R1 smoke v4.0)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q12)
> **执行时间**: 2026-04-22 晚 10:48 PM
> **执行者**: Bojiang + claude cowork MCP Chrome (fresh chat — delete chat history after Q11)
> **会话**: fresh, Custom mode
> **题类**: Q12 — CT 版本锁定 + Define-XML + MedDRA

---

## 题目原文

一个 3 年期临床试验, 从 2022 启动到 2025 DBL (database lock). 期间 CDISC 每季度发布 CT release. 请说明: (a) 这个试验锁用哪个 CT 版本 (start 时 / ongoing / DBL 时)? (b) 锁定 CT 版本的机制是什么 (Define-XML 哪个字段)? (c) AETERM 用 MedDRA 字典, MedDRA v25→v27 会不会影响 AE submission? (d) 如果 DBL 时发现某 CT codelist 已被 retire/alias, 怎么处理?

---

## 模型 raw 回答 (DOM readback)

关于您提出的 3 年期临床试验的 CDISC CT 及 MedDRA 字典版本管理问题，部分具体的临床数据管理（Data Management）操作规则超出了本知识库（仅包含 SDTMIG v3.4 及其相关基础标准）的范围。以下是基于 42 个 source 文件的权威解答：

### (a) 这个试验锁用哪个 CT 版本 (start 时 / ongoing / DBL 时)?

**未收录 / outside the knowledge base**. The sources state that sponsors are encouraged to check the CDISC website frequently for the most up-to-date information [28_ig_ch01_ch02_ch03.md], but the SDTMIG v3.4 does not mandate a specific operational milestone (e.g., study start, ongoing, or database lock) for locking the CDISC Controlled Terminology version. Please provide the specific regulatory guidance or sponsor SOP document reference for operational versioning rules.

### (b) 锁定 CT 版本的机制是什么 (Define-XML 哪个字段)?

The dictionary name and version used to map terms must be documented utilizing the **external codelist element** in the Define-XML document [08_ev_adverse_ae.md], [06_int_concomitant_cm_ag_ml.md], [29_ig_ch04_general_assumptions.md].

### (c) AETERM 用 MedDRA 字典, MedDRA v25→v27 会不会影响 AE submission?

The specific regulatory or statistical impact of up-versioning MedDRA during a trial is **未收录 / outside the knowledge base**. However, according to SDTMIG v3.4 rules, the submission must accurately reflect the dictionary used. **AEDECOD** (Dictionary-Derived Term) is a **Req** variable that must contain the Preferred Term, and the dictionary name and version used must be provided utilizing the external codelist element in the Define-XML document [08_ev_adverse_ae.md]. Furthermore, if MedDRA is used, the submission must also include the intermediate hierarchy variables (which are **Exp**): AELLT, AELLTCD, AEPTCD, AEHLT, AEHLTCD, AEHLGT, AEHLGTCD, AEBDSYCD, AESOC, AESOCD [08_ev_adverse_ae.md]. **Changing the version from v25 to v27 may alter the hierarchy paths required in these variables**.

### (d) 如果 DBL 时发现某 CT codelist 已被 retire/alias, 怎么处理?

**未收录 / outside the knowledge base**. The sources note that CDISC Terminology is centrally managed by the CDISC Controlled Terminology Team with a 3-month development period and quarterly releases [40_ct_supplementary.md]. However, the SDTMIG does not provide data management rules for handling terms that are retired or aliased at the time of database lock. Please provide the specific CDISC terminology implementation document reference.

**Citation 数**: 4+ inline ([28]/[08]/[06]/[29]/[40])

---

## Self-score verdict

- **Verdict**: **PARTIAL (0.5)** — 2 PUNT (a,d) + 1 PASS (b) + 1 PARTIAL (c)
- **对照 PASS 判据**:
  - (a) ✗ PUNT "未收录" safety-correct (SDTMIG v3.4 确实不 mandate operational milestone, 但答不出 "DBL 时最新 CT" 业界实践)
  - (b) ✓ PASS — Define-XML **external codelist element** + dictionary name + version ✓ (匹配判据 "<CodeList> 引用 specific CDISC CT release date")
  - (c) ⚠️ PARTIAL — 答 AEDECOD Req + 10 Exp hierarchy vars + Define-XML external codelist. **正确指出 "v25→v27 may alter hierarchy paths"**. 但未直接说 "整个 submission 用同一 MedDRA 版本" / "recode 全部 AE 到统一版本" (判据核心要求)
  - (d) ✗ PUNT "未收录" safety-correct (SDTMIG 不提供 DM 规则处理 retired/aliased)
- **触发 FAIL 判据?** 无 (未混淆 CDISC CT 和 MedDRA)
- **F-* carry-over**:
  - NotebookLM Q12 again shows in-KB-only PUNT pattern on operational/DM topics (同 Q11)
  - (b) 是 NotebookLM 最强表现 (Define-XML 结构明确在 KB)
  - (c) 部分 PASS 因 KB 含 AEDECOD+hierarchy 结构 + external codelist element, 但操作规则 (重 recode) 超出 v3.4 scope
