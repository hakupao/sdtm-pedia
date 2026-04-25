# Rule A Batch 14 — Audit Summary
**Reviewer:** oh-my-claudecode:designer (slot #23, AUDIT-mode pivot 4th)
**Date:** 2026-04-25
**Scope:** 10 sampled atoms from batch 14 (SDTMIG v3.4 p.131–140)
**Source PDF:** `source/SDTMIG v3.4 (no header footer).pdf`

---

## Top-Line Verdict

```
Rule A batch 14 raw verdict: 95.0% (P/PA/F = 9/1/0)
Weighted: 9×1.0 + 1×0.5 + 0×0 = 9.5 / 10 = 95.0%
Threshold: ≥90% = PASS  |  80–89% = CONDITIONAL_PASS  |  <80% = FAIL
→ BATCH 14 RULE A: PASS (95.0%)
```

---

## Per-Atom Verdict Table

| atom_id | page | atom_type | overall | severity | finding (1-line) |
|---|---|---|---|---|---|
| ig34_p0131_a002 | 131 | TABLE_ROW | PASS | N/A | SUENTPT row verbatim exact; §6.1.6 parent correct |
| ig34_p0132_a003 | 132 | HEADING | PASS | N/A | "Example 1" L5/sib=1 correct; §6.1.6 parent correct |
| ig34_p0133_a019 | 133 | HEADING | PASS | N/A | §6.2.1 self-heading parent correctly set to §6.2 per R12/TOC |
| ig34_p0134_a009 | 134 | TABLE_ROW | PASS | N/A | AEGRPID row verbatim exact; §6.2.1 parent correct |
| ig34_p0135_a017 | 135 | TABLE_ROW | PASS | N/A | AESCONG row with (NY) codelist literal exact; §6.2.1 parent correct |
| ig34_p0136_a008 | 136 | TABLE_ROW | PARTIAL | MEDIUM | AERLPRT missing leading and trailing pipe delimiters; heading_level/sibling_index keys absent rather than null |
| ig34_p0137_a011 | 137 | HEADING | PASS | N/A | "AE – Assumptions" L4/sib=3 correct; §6.2.1 parent correct |
| ig34_p0138_a004 | 138 | LIST_ITEM | PASS | N/A | Item b AEGRPID list verbatim exact; cross_refs populated |
| ig34_p0139_a003 | 139 | LIST_ITEM | PASS | N/A | "AEACN, only for actions taken with study treatment" exact match |
| ig34_p0140_a012 | 140 | HEADING | PASS | N/A | "Rows 1-2:" L5/sib=2 correct under AE Example 1 |

---

## Findings — FAIL and PARTIAL (HIGH/MEDIUM severity)

### F-1 [MEDIUM] ig34_p0136_a008 — TABLE_ROW pipe-delimiter inconsistency (verbatim PARTIAL)

**Atom:** `ig34_p0136_a008`, page 136, AERLPRT row (Option E rerun atom)

**Issue:** The verbatim field is missing the leading pipe and trailing pipe that are standard for TABLE_ROW atoms throughout this batch and the broader batch 14 dataset:

- **Expected format** (consistent with all other TABLE_ROW atoms in batch 14):
  `| AERLPRT | Rel of AE to Non-Dev-Rel Study Activity | Char | * | Record Qualifier | ... | Perm |`
- **Actual format in atom:**
  `AERLPRT | Rel of AE to Non-Dev-Rel Study Activity | Char | * | Record Qualifier | ... | Perm`
  (no leading `|`, no trailing `|` after `Perm`)

**Additional schema deviation:** The JSON object for this atom is missing the `heading_level` and `sibling_index` keys entirely (rather than setting them to `null` as other non-HEADING atoms do). While the values would be null for a TABLE_ROW, the key absence is a schema inconsistency. This atom was produced by the Option E executor rerun (`prompt_version: P0_writer_pdf_v1.2+R10..R15+OptionE`), distinct from the standard executor used for other atoms.

**Substantive content:** The CDISC Notes text, variable label, type, role, controlled terms (`*`), and core designation (`Perm`) all match the PDF p.136 exactly. This is a formatting/structural issue, not a content accuracy failure.

**R-rule reference:** R8 (TABLE_ROW empty cell preservation / pipe formatting), R10 (spec table verbatim wrap-cell artifact preservation).

**Recommendation:** Repair leading and trailing pipe delimiters; ensure `heading_level: null` and `sibling_index: null` keys are present.

---

## Spot-Check Observations (outside the 10-sample, noticed while reading PDF)

### OBS-1: p.133 transition zone discipline — CLEAN
The three-zone structure of p.133 is correctly handled in the 10-sample atoms:
- SU table rows are assigned to §6.1.6 (verified via ig34_p0133_a019 zone context)
- §6.2.1 HEADING-self atom (a019) correctly has `parent_section = §6.2` (not §6.2.1)
- §6.2 heading itself and the 7 events-domain LIST_ITEMs are properly in the §6.2 zone per TOC

### OBS-2: p.136 Option E rerun atoms — pipe format regression signal
Only Option E rerun atoms (`+OptionE` suffix in prompt_version) in the sample show the pipe-delimiter inconsistency (F-1 above). The standard executor atoms (p.131–135) all use consistent outer-pipe format. This suggests the Option E rerun prompt may have a subtle TABLE_ROW formatting difference from the standard executor prompt. Recommend spot-checking 2–3 additional Option E rerun TABLE_ROW atoms from p.136–140 in a future pass.

### OBS-3: p.136 AERLPRT — multi-line CDISC Notes with bullet points
The AERLPRT row on p.136 contains multi-line CDISC Notes with embedded bullet points (Terminology section). The atom correctly captures the `\n` line breaks and `•` bullet characters. Content accuracy is high despite the outer-pipe format issue.

### OBS-4: p.133 heading "6.2 Models for Events Domains" — font rendering
PDF renders the §6.2 chapter heading as "6.2 Models for Events Domains" (sentence-case body text), while the TOC ground truth uses all-caps "MODELS FOR EVENTS DOMAINS". The atom for the §6.2 HEADING-self (not in sample) should use the verbatim PDF text "6.2 Models for Events Domains", not the TOC all-caps form. This was not part of the 10-sample, but is worth confirming in a future audit.

### OBS-5: p.134 AE Specification heading — not in sample but visible
"AE – Specification" heading on p.134 is L4 sib=2 under §6.2.1. The "ae.xpt, Adverse Events — Events. One record per adverse event per subject, Tabulation." line is a sub-heading or note beneath it. If extracted as a separate HEADING atom, it should be distinct from the main AE – Specification L4 heading.

### OBS-6: p.135 AESCONG codelist (NY) — R6 preserved correctly
The `(NY)` codelist literal in the Controlled Terms column is preserved verbatim in atom ig34_p0135_a017. This confirms R6 compliance for NY-type codelists in the Option E rerun output.

---

## Summary Metrics

| Metric | Value |
|---|---|
| Total atoms sampled | 10 |
| PASS | 9 |
| PARTIAL | 1 |
| FAIL | 0 |
| Weighted score | 9.5 / 10.0 = **95.0%** |
| Threshold gate | ≥90% = PASS |
| **Batch 14 Rule A verdict** | **PASS** |
| Findings total | 1 |
| HIGH severity | 0 |
| MEDIUM severity | 1 (F-1: pipe delimiter formatting) |
| LOW severity | 0 |

---

## 4-Dimension Aggregate

| Dimension | PASS | PARTIAL | FAIL |
|---|---|---|---|
| atom_type | 10 | 0 | 0 |
| verbatim | 9 | 1 | 0 |
| parent_section | 10 | 0 | 0 |
| heading_fields (HEADING atoms only, n=4) | 4 | 0 | 0 |

---

*Audit conducted in AUDIT-mode only. No source files, pdf_atoms.jsonl, audit_matrix.md, or _progress.json modified.*
