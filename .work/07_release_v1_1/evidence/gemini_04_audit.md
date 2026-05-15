# Gemini 04 Business Scenarios Audit — v1.1 Interaction with 06 Fixes

> Audit date: 2026-05-16
> Auditor: executor subagent (read-only; 04 file not modified)
> Source: `ai_platforms/gemini_gems/current/uploads/04_business_scenarios_and_cross_domain.md`
> KB baseline after 06: `knowledge_base/domains/PC/assumptions.md`, `knowledge_base/domains/PP/examples.md`, `knowledge_base/domains/TA/assumptions.md`

---

## §1. High-Level Structure of 04 and Sections with 06 Interaction

The 04 file is a 2,764-line writer-authored SDTM business ammunition pack generated 2026-04-21. It contains:

- §0 Usage rules (3 hard constraints: CO-1 Core防污染, CO-2 零臆造CT Code, CO-3 citation强制)
- §1 26 clinical scenario→SDTM mappings (§1.1–§1.26 + lettered sub-items)
- §2 21 pitfall警示 (negative examples)
- §3 CT Code index (codelist CT Code → name mapping only, no Terms)
- §4 Cross-domain rules (RELREC/SUPP--/Timing/Visit/Dataset/Baseline)
- §5 Smoke v2 10-question mapping
- §6 Answer templates
- §7–§8 Quick indexes (variable→section, 63-domain class table)
- §9 High-frequency FAQ
- §10 Version mapping (SDTMIG v3.4/SDTM v2.0)
- §12–§24 Deep-dives: Trial Design (TA/TE/TV/TI/TS/TM), IE, Oncology (TU/TR/RS), AG, PR, imaging, Events class, SUPP-- deep-dive, naming rules, EDC patches, specialty domains, Q&A supplements

**Sections with potential 06-fix interaction:**

| Section | Topic | 06 Fix Involved |
|---------|-------|-----------------|
| §1.5 | PC LLOQ handling | PC/assumptions content; 06 added §6.3.5.9 RELREC section |
| §1.6 + §12.3 | DM/TA ARMCD, Trial Arms design | TA/assumptions +175 lines (06 added TA-specific assumptions §7.2 deep content) |
| §1.10 + §4.1 + §4.9 | RELREC general rules | PC §6.3.5.9.3 Methods A/B/C/D added by 06 |
| §1.24 | PP domain (NCA parameters) | PP/examples.md RELREC method descriptions added by 06 |
| §12.3 | TA deep-dive | KB TA/assumptions extended significantly by 06 |

---

## §2. Section-by-Section Verdict

### §1.5 PK LLOQ (PC Domain)

**04 content**: Correctly describes PCORRES="<LLOQ", PCSTRESN=NULL (not 0), PCLLOQ=0.5. Source cited: `PC/spec.md` and `PC/assumptions.md §3`.

**06 KB addition**: PC/assumptions.md now includes §6.3.5.9.3 "Relating PP Records to PC Records" with Methods A/B/C/D for RELREC linking between PC and PP datasets.

**Gap**: 04 §1.5 covers the LLOQ recording rule correctly. It does **not** mention that PC records should be linked to PP via RELREC. §1.24 covers PP separately but only lists PPRFTDTC as a link mechanism — it does not describe the RELREC Methods A/B/C/D.

**Verdict**: **GAP** — 04 has no scenario covering "how to relate PC concentration records to PP parameter records via RELREC". The KB now has a detailed §6.3.5.9.3 with 4 methods; 04 is silent on this.

---

### §1.6 + §1.15e + §12.3 — DM ARMCD / TA Trial Arms

**04 content**:
- §1.6 is extremely detailed on DM.ARMCD/ARM/ACTARMCD/ACTARM. Correct. References `DM/spec.md` and `DM/assumptions.md §4`.
- §1.15e covers TA/TE/TV brief overview. TA.ARMCD=Req, TAETORD, ETCD, ELEMENT, TABRANCH, TATRANS, EPOCH — all correct.
- §12.3 deep-dives TA: ARMCD Req (≤20), ARM Req, TAETORD Req, ETCD Req, TABRANCH Exp, TATRANS Exp, EPOCH Req. States DM.ARMCD/ACTARMCD must come from TA.ARMCD.

**06 KB addition**: TA/assumptions.md received +175 lines covering §7.2.1 Trial Arms description/overview, Example 2 (crossover), §7.2.1.1 (Branch vs Transition distinction), §7.2.2.1 (Elements/Study Cells/Epochs), and 11 TA-specific assumptions (TAETORD rules, TABRANCH/TATRANS semantics, EPOCH assignment rules, numbered-epoch convention).

**04 vs KB comparison**:
- 04 §12.3 already captures ARMCD/ARM Req, TAETORD Req, ETCD Req, EPOCH Req — matching the KB spec.
- 04 §1.6 pitfall (8) correctly states "ACTARMCD must be a value of ARMCD in Trial Arms dataset" — consistent with KB.
- 04 §12.3 does not cover the TABRANCH vs TATRANS distinction (§7.2.1.1), the numbered-epoch convention (assumption 10a/b), or the "elements are reusable" rule (assumption 2). These are in the new KB TA content.

**Verdict**: **ALIGNED** on the core variables and DM↔TA key constraint. **GAP** on TABRANCH/TATRANS semantics, numbered-epoch convention, and reusable-elements concept — these are now in KB but not reflected in 04. The gap is informational depth, not a factual error.

---

### §1.10 + §4.1 + §4.9 — RELREC General Rules

**04 content**: §1.10 covers AE↔CM causal RELREC with correct RELID binding. §4.1 covers 3 RELREC use cases (cross-domain, same-domain, dataset-level). §4.9 priority ladder: VISIT → MIDS → --LNKID → RELREC → SUPP--. All internally consistent.

**06 KB addition**: PC/assumptions.md §6.3.5.9.3 adds PC-PP specific RELREC: Methods A (many-to-many, PCGRPID+PPGRPID), B (one-to-many, PCSEQ+PPGRPID), C (many-to-one, PCGRPID+PPSEQ), D (one-to-one, PCSEQ+PPSEQ). Decision tree for implementation.

**04 vs KB**: 04's general RELREC coverage is correct. The PC-PP specific methods are not in 04. This is a specialization gap, not an error in the existing content.

**Verdict**: **ALIGNED** on general rules. **GAP** on PC-PP RELREC specialization (Methods A/B/C/D).

---

### §1.24 — PP Domain (Non-Compartmental PK)

**04 content**: Brief. Lists PPTESTCD/PPTEST (AUC, CMAX), PPORRES/PPSTRESC/PPSTRESN, PPRFTDTC. States "PC=blood concentration (raw sampling), PP=PK parameters (NCA/compartmental results)". PPRFTDTC described as "reference time point date" without explaining it is used to link PP to PC.

**06 KB addition**: PP/examples.md now contains: (a) full PPGRPID-based shared PP data table (12 rows, 4 PPGRPID columns for Examples 1–4), (b) RELREC Method B, C, A descriptions referencing PPSEQ and PPGRPID values, (c) cross-reference "see PC examples for RELREC Methods A–D and relrec.xpt tables".

**04 vs KB**: 04 §1.24 is minimal — it does not explain that PPRFTDTC links to PC, does not mention PPGRPID, and says nothing about the RELREC linking obligation ("Sponsors must document the concentrations used to calculate each parameter" — KB PC/assumptions §6.3.5.9.3 intro). This is a substantive omission for PK programmers.

**Verdict**: **STALE** / **GAP** — §1.24 is incomplete relative to current KB. PPRFTDTC's linking purpose, PPGRPID, and RELREC obligation are all absent.

---

### §1.6 Pitfall (8) — ACTARMCD must come from TA

**04 content**: Explicitly states: "DM/spec.md §ACTARMCD 原文: 'With the exception of studies which use multistage arm assignments, must be a value of ARMCD in the Trial Arms dataset.'" Correct and sourced.

**06 KB addition**: TA/assumptions.md added TA-specific assumption 11: "study cells are not explicitly defined in TA; set of records with common ARMCD and EPOCH values constitutes a study cell." No conflict with 04.

**Verdict**: **ALIGNED**.

---

### §9 FAQ / §23 Q&A — PC/PP/TA Business Scenarios

**04 content**: §9.4 DM/Trial Design FAQ covers ARMCD must be in TA (correct). §23.1 oncology and §23.2 trial design Q&As do not touch PC-PP RELREC. §21.5 "PK vs PD data" briefly notes PC=PK concentrations, PP=PK parameters — no RELREC guidance.

**Verdict**: **GAP** — No FAQ or Q&A covers the PC-PP RELREC linking question, which is a real CDM/programmer pain point.

---

### DI Domain — 06 added new domain

**06 KB addition**: DI domain was added (noted in KNOWN_LIMITATIONS §0: "DI domain added").

**04 coverage**: §8 63-domain class table covers all domains by class. A grep for "DI" in §8 shows DI is not listed in the domain speed-reference table. The table was generated 2026-04-21 before the DI domain was added to KB.

**Verdict**: **GAP** — DI domain absent from §8 domain table.

---

## §3. Total Verdict Summary

| Section | Verdict | Severity |
|---------|---------|----------|
| §1.5 PC LLOQ recording | ALIGNED | — |
| §1.5 / §1.24 PC-PP RELREC Methods A/B/C/D | GAP | HIGH — PK programmers need this |
| §1.24 PP: PPRFTDTC purpose + PPGRPID + RELREC obligation | STALE/GAP | HIGH |
| §1.6 / §12.3 TA ARMCD/ACTARMCD key constraint | ALIGNED | — |
| §12.3 TA TABRANCH/TATRANS semantics depth | GAP | LOW (informational depth) |
| §12.3 TA numbered-epoch convention | GAP | LOW |
| §4.1 / §4.9 RELREC general rules | ALIGNED | — |
| §8 domain table: DI domain absent | GAP | MEDIUM |
| §9 / §23 FAQ: PC-PP RELREC question missing | GAP | MEDIUM |

**Overall**: 04 has **no factual errors** relative to the 06 KB fixes. All existing content that overlaps with 06-modified KB areas is correct (ARMCD key constraint, LLOQ handling, general RELREC rules). The issue is **omission**: PC-PP RELREC Methods A/B/C/D, PPGRPID, PPRFTDTC linking purpose, DI domain, and enhanced TA depth are all absent.

---

## §4. Main Session Intervention Decision

**Requires main session update to 04: YES (HIGH priority gaps exist)**

Specific diff recommendations (not written to 04 — read-only):

### Diff 1: Add §1.24b PC-PP RELREC linking (new subsection after §1.24)

Insert after §1.24 "Non-Compartmental PK (PP) 域":

```
### §1.24b PC 浓度与 PP 参数的 RELREC 关联 (§6.3.5.9.3)

**业务场景**: PK 研究提交时, 须记录每个 PP 参数由哪些 PC 浓度记录计算得出.

**SDTM 规则** (KB PC/assumptions.md §6.3.5.9.3):
Sponsors must document the concentrations used to calculate each parameter, either via analysis
dataset metadata or via RELREC relationships between PC and PP.

**4 种 RELREC 方法** (按 --GRPID 使用情况):
| 方法 | 使用变量 | 适用场景 |
|------|----------|---------|
| A (many-to-many) | PCGRPID + PPGRPID | 所有参数用所有浓度; 最高效 |
| B (one-to-many)  | PCSEQ + PPGRPID   | 浓度按记录引用, 参数按组 |
| C (many-to-one)  | PCGRPID + PPSEQ   | 浓度按组, 参数按记录引用 |
| D (one-to-one)   | PCSEQ + PPSEQ     | 无需 GRPID; 记录数最多但实现最简单 |

**关键变量**:
- PCGRPID / PPGRPID (Perm): 分别在 PC 和 PP 内分组相关记录
- PPRFTDTC (Exp): PP 参数关联的 PC 参考时间点 — 同时作为 PC↔PP 软链接

**源路径**: `knowledge_base/domains/PC/assumptions.md` §6.3.5.9.3, `knowledge_base/domains/PP/examples.md`
```

### Diff 2: Update §8 domain table to add DI

In §8 (63-domain class table), add DI (Device Identifiers) under the appropriate class (Findings or Special Purpose — confirm from KB DI/spec.md).

### Diff 3: Add §9.x FAQ entry for PC-PP RELREC

In §9 (High-frequency FAQ), add:

```
### §9.x PC 和 PP 域必须用 RELREC 关联吗?

**必须文档化** (KB PC/assumptions.md §6.3.5.9.3): sponsors 须说明每个 PP 参数
由哪些 PC 浓度计算得出. 可通过 analysis dataset metadata 或 RELREC 实现.
推荐 RELREC 方法 A (PCGRPID+PPGRPID) 作为首选 (最少记录数).
PPRFTDTC 可作软链接但不是正式 RELREC 替代.
```

### Diff 4: Deepen §12.3 TA with TABRANCH/TATRANS distinction

In §12.3, add a "TABRANCH vs TATRANS 区分" paragraph sourcing `TA/assumptions.md §7.2.1.1`: branch = fork in flowchart giving rise to separate arms (no "if" within a record); transition = choice within an arm (contains "if" clause).
