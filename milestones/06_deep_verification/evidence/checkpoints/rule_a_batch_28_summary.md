---
slot: 37
family: general-purpose
family_burn: 1
audit_pivot_index: 18
seed: 20260610
sample_size: 10
weighted_pct: 87.9
pass_n: 7
partial_n: 1
fail_n: 2
batch: 28
pages: "271-280"
section: "§6.3.5.9 Pharmacokinetics Domains body (PP-Specification + PP-Assumptions + PP-Examples + §6.3.5.9.3 Relating PP Records to PC Records, Methods A/B/C/D for Examples 1-3)"
reviewer: general-purpose
writers: ["oh-my-claudecode:executor (28a)", "oh-my-claudecode:writer→executor recovery (28b)"]
rule_d_isolation: confirmed (no co-touch, NEW family inaugural burn)
---

# Rule A Reviewer — Batch 28 (slot #37, general-purpose, AUDIT pivot #18)

## §1 Per-atom verdict table

| atom_id | page | type | verdict | notes |
|---|---|---|---|---|
| ig34_p0271_a016 | 271 | HEADING | PASS | PP – Specification L6 sib=2 under §6.3.5.9.2; en-dash exact |
| ig34_p0272_a012 | 272 | TABLE_ROW | PASS | PPTPTREF spec row exact 7-column match |
| ig34_p0273_a037 | 273 | LIST_ITEM | **FAIL** | EDITORIAL_CORRECTION: PDF "pre-corrdinating" → atom "pre-coordinating" (typo silently fixed, multi-char drift) |
| ig34_p0274_a003 | 274 | TABLE_HEADER | PASS | 19-column pp.xpt header Example 2 exact |
| ig34_p0275_a012 | 275 | HEADING | PASS | §6.3.5.9.3 L5 sib=3 under §6.3.5.9 group container; NEW7 L4-group precedent applied correctly |
| ig34_p0276_a028 | 276 | TABLE_ROW | PASS | pc.xpt row 22 (29 fields) exact match incl. blank PCBLFL |
| ig34_p0277_a002 | 277 | CODE_LITERAL | PASS | "pp.xpt" filename literal |
| ig34_p0278_a010 | 278 | TABLE_ROW | **PARTIAL** | row 8 verbatim correct but parent_section "Example 1" shortcut (NEW7 L6 codification → should anchor "§6.3.5.9.3 — Example 1") |
| ig34_p0279_a037 | 279 | HEADING | PASS | "Method A (Many to Many, Using PCGRPID and PPGRPID)" L7 sib=1; NEW7 deep-nesting correctly applied (avg 0.875 just-PASS, parent_section PARTIAL but heading-fields PASS lifts to overall PASS) |
| ig34_p0280_a030 | 280 | TABLE_ROW | **FAIL** | DOUBLE-FAIL: row 14 with PPSEQ=4 + parent "Example 2" — PDF p.280 row 14 of Example 1 Method D table = PPSEQ=**2**; PPSEQ=4 corresponds to row 16; Example 2 on p.280 only has Method B rows 1-11 visible (no row 14). Both verbatim row-value mismatch AND example-boundary misattribution |

## §2 Summary stats

- PASS_n: 7
- PARTIAL_n: 1
- FAIL_n: 2
- weighted_sum: 29.0 / total_max: 33.0
- **weighted_pct: 87.9%**

Per cross-validation table threshold (≥80% weighted = batch-PASS), this batch CLEARS the floor (87.9% > 80%) but with material findings warranting reconciler-side residual review.

## §3 Findings (rule violations)

### F1 — atom 3 p.273 a037: EDITORIAL_CORRECTION violation (R12 verbatim strict)
- **PDF source**: "Instead of pre-**corrdinating** ..." (PDF-source typo, missing 'o')
- **Atom verbatim**: "Instead of pre-**coordinating** ..."
- **Drift**: silent 1-char insertion ('o') = multi-char editorial correction without EDITORIAL_CORRECTION verdict tagging per v1.2 prompt H2' reverse forward-aware rule
- **Severity**: HIGH — second EDITORIAL_CORRECTION instance in P1 cumulative (R12 violation pattern); writer should either preserve PDF typo verbatim OR flip to EDITORIAL_CORRECTION verdict explicitly
- **Recommend**: reconciler manual repair — restore "pre-corrdinating" verbatim OR add metadata field `editorial_correction: true` with PDF original noted in extracted_by.notes

### F2 — atom 10 p.280 a030: NEW7 L6 sub-batch context drift RECURRENCE (3rd instance!)
- **PDF source**: p.280 top continuation table = Example 1 Method D, where Row 14 = PP PPSEQ=**2** RELID=1 (PPSEQ=4 corresponds to Row **16**)
- **Atom verbatim**: "14 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 4 | | 1" with parent_section "Example 2"
- **Drift**: dual error — (a) row number / IDVARVAL value mismatch (Row 14 ≠ PPSEQ=4) AND (b) example boundary mis-attribution (Example 1 → Example 2)
- **Severity**: CRITICAL — this is the **3rd recurrence** of the NEW7 L6 sub-batch context drift motif (round 3 batch 23 GF Examples 4-5 = O-P1-68; round 4 batch 25 LB Examples 1-3 = O-P1-79; **round 5 batch 28 PP Examples 1-2 = O-P1-NEW**). Writer cycled across example boundaries during multi-Example PP relrec.xpt batch and lost row-numbering anchor.
- **Recommend**: reconciler-side Option H 1-atom rewrite. **Triple-recurrence** = PROCEDURAL ENFORCEMENT v1.3+ codification mandatory: when sub-batch crosses Example N→Example N+1 boundary in PP/PC/LB-style multi-Example tables, writer MUST inline-re-verify row numbering against PDF table boundary, not carry counter forward.

### F3 — atoms 8 + 9 p.278/p.279: NEW7 L6 parent_section shortcut form (SHORTCUT vs FULL-FORM)
- **Atoms**: ig34_p0278_a010 ("Example 1") + ig34_p0279_a037 ("Example 2")
- **Per NEW7 round 4 codification**: parent_section for sub-Example atoms should be canonical full-form anchor "§6.3.5.9.3 Relating PP Records to PC Records — Example N" not bare "Example N"
- **Severity**: MEDIUM (atom 8 PARTIAL) / LOW (atom 9 weighted just-PASS due to heading_fields lift)
- **Recommend**: reconciler-side bulk patch all "Example N" → "§6.3.5.9.3 Relating PP Records to PC Records — Example N" within p.278-280 PP Examples cluster (also covers any sibling atoms not in Rule A sample)

### Rules NOT triggered in sample
- R10 (HEADING sibling RESTART): atom 9 L7 sib=1 correct (Method A first method in Example 2)
- R11 (HEADING level): all 3 HEADING atoms correct (L6/L5/L7)
- R14 (atom_type 9-enum): all atoms in 9-enum {HEADING, TABLE_ROW, TABLE_HEADER, LIST_ITEM, CODE_LITERAL}
- R15 (verbatim strict): only F1 violated (atom 3); F2 is row-mismatch not paraphrase
- NEW1 dual-threshold: not applicable (this is Rule A audit, not drift cal)
- NEW6/NEW6.b L4 self-parent: atom 5 §6.3.5.9.3 correctly uses §6.3.5.9 (L4 group container) as parent, not self

## §4 NEW8 char-iteration sweep on canonical CDISC variable names

Letter-by-letter audit of all canonical SDTM variable names appearing in sample atoms vs PDF:

| Atom | Variables (PDF expected) | Atom verbatim | Match |
|---|---|---|---|
| 2 (p.272) | PPTPTREF (8 chars: P-P-T-P-T-R-E-F) | PPTPTREF | ✓ exact |
| 4 (p.274) | PPTESTCD (8) / PPRFTDTC (8) / PPSTRESC (8) / PPSTRESN (8) / PPSTRESU (8) / PPANMETH (8) / PPNOMDY (7) / PPRFID (6) | all match exactly | ✓ all 13 vars |
| 6 (p.276) | PCGRPID (7) / PCREFID (7) / PCTESTCD (8) / PCRFTDTC (8) / PCBLFL (6) / PCLLOQ (6) / PCNOMDY (7) / PCPTREF (7) / PCSTRESC (8) | row data only, no header (header on a separate atom) | ✓ N/A (data row) |
| 9 (p.279) | PCGRPID (7) / PPGRPID (7) | "PCGRPID" + "PPGRPID" in heading text | ✓ exact |
| 10 (p.280) | PPSEQ (5) | "PPSEQ" | ✓ exact (variable name itself correct; row-number/value drift is separate F2 issue) |

**Result**: NEW8 char-iteration sweep PASS — 0 character-level drift on CDISC variable names. The atom 3 typo "corrdinating"→"coordinating" is on a non-variable English word (NEW8.b SENTENCE-trigram territory, not NEW8 variable-name territory). The atom 10 drift is on row index value not variable name.

NEW8 status: VARIABLE-NAME drift = 0/n. NEW8.b SENTENCE-trigram caught F1 multi-char drift indirectly (`corrd-coord-` trigram diff), validating round 4 NEW8.b candidate codification.

## §5 NEW6.b L4 self-parent + NEW7 deep-nesting verification

### HEADING atoms in sample: 3 (atoms 1, 5, 9)

#### Atom 1 — ig34_p0271_a016: PP – Specification (L6 sib=2)
- Parent: §6.3.5.9.2 Pharmacokinetics Parameters (PP) (L5)
- L6 children of §6.3.5.9.2: PP – Description/Overview (sib=1) → PP – Specification (sib=2) → PP – Assumptions (sib=3) → PP – Examples (sib=4)
- **Verdict**: L6 + sib=2 CORRECT
- **NEW6.b L4 self-parent**: N/A (this is L6 not L4)

#### Atom 5 — ig34_p0275_a012: §6.3.5.9.3 Relating PP Records to PC Records (L5 sib=3)
- Parent: §6.3.5.9 Pharmacokinetics Domains (L4 group container)
- L5 children of §6.3.5.9: §6.3.5.9.1 PC (sib=1) / §6.3.5.9.2 PP (sib=2) / §6.3.5.9.3 (sib=3)
- **Verdict**: L5 + sib=3 CORRECT
- **NEW7 L4-group-container precedent**: APPLIED CORRECTLY — per round 4 NEW (§6.3.5.7.1 MB under §6.3.5.7 Microbiology Domains group, O-P1-75 INFO), §6.3.5.X individual sub-section sits at L5 under §6.3.5 group at L4. This atom validates the precedent for PK family. **Round 5 batch 28 = 2nd cross-family validation of NEW7 L4-group-container precedent (Microbiology batch 25 → Pharmacokinetics batch 28).**

#### Atom 9 — ig34_p0279_a037: Method A (Many to Many, Using PCGRPID and PPGRPID) (L7 sib=1)
- Parent: Example 2 (L6 — but parent_section bare form, see F3)
- Canonical chain: §6.3.5.9 Pharmacokinetics Domains (L4 group) → §6.3.5.9.3 Relating PP Records to PC Records (L5) → Example 2 (L6) → Method A (L7)
- **Verdict**: L7 + sib=1 CORRECT — Method A is first of 4 methods (A→B→C→D) within Example 2
- **NEW7 deep-nesting L7 precedent**: this validates round 3 batch 21 L7 sub-example precedent (Example 1a/1b L7 sib=1,2 in CDISC GF batch). **Round 5 = 2nd cross-family L7 validation (GF batch 21 → PP batch 28).** Methods A/B/C/D form a sibling chain at L7, with sib_index RESTART per Example parent (Example 1's Method A would be a separate sib=1, not sib=5 cumulative).

### NEW6.b L4 self-parent atoms in sample: 0
No L4 atoms in sample, so NEW6.b proactive extension cannot be validated this batch. (Round 4 had 4× proactive EFFECTIVE — round 5 batch 28 sample missed L4-level HEADING coverage; recommend Rule A future seed include §6.3.5.9 group HEADING explicitly.)

### NEW7 deep-nesting summary
- L4 group container (§6.3.5.X) precedent: validated 2nd cross-family (Microbiology+PK)
- L5 individual sub-section: validated (atom 5)
- L7 deep-nesting (Method A under Example N): validated 2nd cross-family (GF+PK)
- L6 (Example N pseudo-heading): present in parent_section of atoms 8/9 but no L6 HEADING atom in sample (Example N typically not extracted as HEADING since it's a paragraph label)

---

**Final**: Rule A batch 28 weighted=87.9% PASS_n=7 PARTIAL_n=1 FAIL_n=2

**Critical hand-off to reconciler**: F2 NEW7 L6 sub-batch context drift = **3rd recurrence** across 3 rounds (round 3+4+5) — formal v1.3+ procedural enforcement codification ULTRA-CRITICAL escalation; F1 EDITORIAL_CORRECTION verdict policy clarification needed in v1.3 prompt cut.
