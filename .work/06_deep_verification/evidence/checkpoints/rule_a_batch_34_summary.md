# Rule A Batch 34 — AUDIT Summary

**Reviewer**: `pr-review-toolkit:type-design-analyzer` (AUDIT-mode pivot 24th cumulative, pr-review-toolkit family 3rd-agent depth burn)
**Sample**: 10 atoms, seed=20260640, p.331-340 (SDTMIG v3.4 §6.3.9.3 RS tail + §6.3.10 SC head)
**Adaptation**: full-tool (Write tool used directly, no Bash-heredoc fallback)
**Date**: 2026-04-28

---

## §1 Verdict counts

| Verdict | Count |
|---|---|
| PASS | 7 |
| PARTIAL | 3 |
| FAIL | 0 |

**Weighted score** = (7 × 1.0 + 3 × 0.5 + 0 × 0.0) / 10 × 100 = **85.0%**

Threshold reference (kickoff §7): PASS ≥ 90% / WARN 70-90% / FAIL < 70% → **WARN band** (parent_section systematic level-skip motif drives 3 PARTIAL).

---

## §2 Per-atom verdict table

| # | atom_id | page | atom_type | verdict | dimensions failing | brief |
|---|---|---|---|---|---|---|
| 1 | ig34_p0331_a008 | 331 | TABLE_ROW | PASS | — | EPOCH RS Spec row verbatim 7 cols 8 pipes |
| 2 | ig34_p0332_a005 | 332 | HEADING | PASS | — | §6.3.9.3.1 L5 sib=3 chain plausible |
| 3 | ig34_p0333_a010 | 333 | TABLE_ROW | PASS | — | SYMPTDTR inline-table 5 cols 6 pipes |
| 4 | ig34_p0334_a008 | 334 | HEADING | PARTIAL | parent_section | Example 1 L7 sib=1; parent skips L6 Examples canonical |
| 5 | ig34_p0335_a012 | 335 | TABLE_ROW | PASS | — | Example 2 row 8 USUBJID 55555 19 cols 20 pipes |
| 6 | ig34_p0336_a001 | 336 | CODE_LITERAL | PASS | — | rs.xpt caption verbatim |
| 7 | ig34_p0337_a007 | 337 | LIST_ITEM | PARTIAL | parent_section | QRS Naming Rules — parent §6.3 L3 skips L4+L5 |
| 8 | ig34_p0338_a009 | 338 | LIST_ITEM | PARTIAL | parent_section | scoring rules — same 2-level skip as atom 7 |
| 9 | ig34_p0339_a022 | 339 | HEADING | PASS | — | SC – Description/Overview L4 sib=1 |
| 10 | ig34_p0340_a021 | 340 | TABLE_ROW | PASS | — | VISITNUM SC Spec row, empty cell `\| \|` preserved |

---

## §3 Detailed findings

No FAIL verdicts. Three PARTIAL verdicts share a common motif: **systematic parent_section level-skip on §6.3.9.3.2 Clinical Classifications Use Case "common to FT/QS/CC" assumption block (p.337-338) and L7 Example 1 (p.334)**.

### Finding A — atoms 7 + 8: parent_section 2-level skip (PARTIAL × 2)

**Symptom**: Atoms `ig34_p0337_a007` and `ig34_p0338_a009` both list parent_section as `§6.3 [MODELS FOR FINDINGS DOMAINS]` (L3 short-bracket), but the underlying PDF content lives in:
- §6.3.9.3.2 Clinical Classifications Use Case (L5)
  - "RS – Clinical Classifications Use Case Assumptions" (L6)
    - "common to FT and QS as well as Clinical Classifications use case" sub-block on p.337-338

**PDF cross-check**:
- p.337 atom 7 content "The QRS Naming Rules for --CAT, --TEST, and --TESTCD…" matches Assumption 1.a under "common to FT/QS/CC" sub-block
- p.338 atom 8 content "The sponsor is expected to provide information about the scoring rules in the metadata." matches Assumption 6.d under same sub-block

**Expected parent**: `§6.3.9.3.2 Clinical Classifications Use Case` (L5 canonical full-form per NEW6 dual-form spec) OR `§6.3.9.3.2 RS – Clinical Classifications Use Case Assumptions` (L6 canonical)

**Actual parent**: `§6.3 [MODELS FOR FINDINGS DOMAINS]` (L3 short-bracket — 2 levels too high)

**Severity assessment**: PARTIAL not FAIL because:
1. Verbatim text and atom_type and cross_refs are correct
2. The "common to FT/QS/CC" sub-block IS cross-domain by nature (writer may have read it as §6.3-level guidance shared across multiple domain sections)
3. Round 6 chapter-short-bracket extension (NEW6.b) does support `§6.3 [MODELS FOR FINDINGS DOMAINS]` as a real canonical short-form for L3 transitions

**Risk**: Systematic across the 2-page sub-block (p.337-338) — likely affects all atoms in the "common to FT/QS/CC" assumption block, not just sampled atoms 7+8. **Reconciler should sweep §6.3.9.3.2 batch atoms for parent_section L3-vs-L5 ambiguity and decide canonical anchor (matches O-P1-95 / O-P1-103 cross-batch handoff motif family).**

### Finding B — atom 4: L7 Example 1 parent_section skips L6 Examples canonical (PARTIAL × 1)

**Symptom**: Atom `ig34_p0334_a008` is HEADING "Example 1" with heading_level=7 sibling_index=1, parent_section `§6.3.9.3.1 Disease Response Use Case` (L5).

**PDF cross-check**: p.334 shows "RS – Examples - Disease Response" preamble heading PRECEDING "Example 1". Per kickoff dimension 3 ("for L6 atoms parent = L5 canonical full-form (NOT bare 'Example N' shortcut per O-P1-91); for L7 atom should parent to L6 Examples canonical"), an L7 "Example 1" should parent to the L6 "RS – Examples - Disease Response" or similar L6 Examples canonical anchor, not directly to L5 §6.3.9.3.1.

**Alternative interpretation**: Round 3 batch 21 established L7 sub-example precedent (Example 1a/1b L7 sib=1, 2 under L6 Example 1 parent). If writer's chain is **§6.3.9.3.1 [L5] → RS – Examples - Disease Response [L6 implicit] → Example 1 [L7]**, then L7 parent should be the L6 Examples canonical, not L5.

**Severity**: PARTIAL not FAIL because:
1. Verbatim "Example 1" matches PDF
2. heading_level=7 + sibling_index=1 RESTART are consistent with L7 chain
3. Parent-level ambiguity is a known motif (O-P1-91), not a verbatim/data corruption

**Risk**: Cascades to all L7 Example N atoms in §6.3.9.3.1 — reconciler should confirm L6 Examples header atom exists and L7 Example N atoms parent to it.

### Verbatim integrity (R10 strict)

10/10 atoms PASS character-for-character including:
- 2-space numbering gap "6.3.9.3.1  Disease" (atom 2)
- En-dash "SC – Description/Overview" (atom 9) — ASCII en-dash preserved correctly
- Empty cell `| |` preservation in VISITNUM Controlled Terms col (atom 10) per O-P1-26 R8 rule
- 19-column wide table row (atom 5) all 20 pipes correct
- URL preservation in cross_refs (atom 7)

### NEW2/NEW8 oracle (homoglyph + canonical CDISC vars)

10/10 PASS — no Cyrillic homoglyphs detected in any [A-Z]{3,} identifier. Canonical RS vars EPOCH/RSEVAL/RSEVALID/RSACPTFL/VISITNUM (atoms 1, 5, 10) all match canonical list. Atom 5 contains OVRLRESP which is RSTESTCD **value**, not a variable name — correctly does not trigger oracle (oracle scope is variable-name slot, not data-cell content).

### TABLE_ROW pipe count + empty cell (R8 + O-P1-26)

4/4 sampled TABLE_ROW atoms PASS:
- Atom 1: 7 cols → 8 pipes ✓
- Atom 3: 5 cols → 6 pipes ✓
- Atom 5: 19 cols → 20 pipes ✓
- Atom 10: 7 cols + empty Controlled Terms cell preserved as `| |` ✓ (O-P1-26 NEW1 6th-failure-motif protection live-fire effective)

---

## §4 AUDIT-mode pivot reflection

This is the **24th cumulative AUDIT-mode pivot** of the family-agnostic recipe + **3rd-agent depth burn** within pr-review-toolkit family. The agent's normal mode ("type design analyzer") rates encapsulation / invariant expression / invariant usefulness / invariant enforcement on a 1-10 scale. Mapping that mental model to SDTM atomization audit:

| Type-design dimension | SDTM atomization analog | This batch's evidence |
|---|---|---|
| **Encapsulation** (hide internals; minimal complete interface) | **Atom semantic isolation** — each atom carries ONE textual unit + its metadata; parent_section + heading_level + atom_type expose only what consumers need; raw PDF bytes/positioning hidden | 10/10 atoms have well-bounded `verbatim` field; no atom leaks multiple semantic units; atom_type 9-enum acts as discriminated union |
| **Invariant Expression** (clarity; compile-time guarantees; self-documenting) | **Verbatim integrity** — atom must express EXACTLY the PDF source text; whitespace/punctuation/case = part of the contract | 10/10 verbatim PASS character-for-character; en-dash + 2-space numbering + empty pipe-cell all preserved; expression discipline strong |
| **Invariant Usefulness** (prevent real bugs; align with business; ease reasoning) | **parent_section canonical correctness** — gives consumers a stable navigation anchor; downstream KB pages depend on parent for L3/L4/L5/L6 reconstruction | **3 PARTIAL on this dim** — L3 short-bracket vs L5 canonical full-form ambiguity in §6.3.9.3.2 sub-block + L7-skip-L6-Examples for atom 4 = real downstream-cost risk for KB section navigation |
| **Invariant Enforcement** (construction-time validation; impossible illegal states) | **NEW2 Cyrillic + NEW8 canonical CDISC oracle** — automated cross-checks at writer/reviewer boundaries that catch corruption before it persists | 10/10 PASS oracle; no Cyrillic У homoglyph (post-O-P1-102 watch); canonical var lists hold for sampled rows |

**Aggregate verdict mapped to type-design idiom**: this 10-atom slice exhibits **strong encapsulation (10/10)**, **strong invariant expression (10/10 verbatim)**, **WEAK invariant usefulness (7/10) on parent_section dimension** (3 systematic PARTIAL = unenforced informal contract about which level wins when content is cross-cutting), and **strong invariant enforcement (10/10)** on the NEW2/NEW8 oracle layer. The "weak invariant" is exactly where atomization quality risk concentrates — and where v1.3 §F NEW6 dual-form spec already prescribes a remedy (canonical full-form L4-L7, short-bracket L3 only). The atoms' parent_section choices show writer ambiguity in cross-cutting sub-blocks, suggesting v1.4 candidate: **explicit guidance for cross-domain "common to X/Y/Z" assumption blocks — pin parent to the most specific containing L4/L5, never escalate to L3 short-bracket**.

---

## §5 pr-review-toolkit family 3rd-agent depth-burn recipe consistency

Comparison vs prior 2 burns within same family:

| Burn | Round | Batch | Agent | Sample size | Verdict counts | Weighted | Recipe artifacts produced |
|---|---|---|---|---|---|---|---|
| 1st | round 6 | batch 29 | `pr-review-toolkit:code-reviewer` (#38) | 10 atoms p.281-290 | per round 6 retro | per round 6 retro | full-tool verdicts.jsonl + summary.md |
| 2nd | round 6 | batch 31 | `pr-review-toolkit:silent-failure-hunter` (#40) | 10 atoms p.301-310 | per round 6 retro | per round 6 retro | full-tool verdicts.jsonl + summary.md |
| **3rd** | **round 7** | **batch 34** | **`pr-review-toolkit:type-design-analyzer` (#43)** | **10 atoms p.331-340** | **7 PASS / 3 PARTIAL / 0 FAIL** | **85.0%** | **full-tool verdicts.jsonl + summary.md (this file)** |

**Recipe consistency check** (the AUDIT-mode pivot expects: agent ignores its default mode, executes the 6-dimension Rule A audit in the same shape regardless of which family-tool persona it inhabits):

1. **Output schema fidelity** — verdicts.jsonl 10 lines / required keys all present / verdict tri-enum / weighted formula correct → **CONSISTENT** with prior 2 burns
2. **Dimension coverage** — verbatim + atom_type + parent_section + heading_chain + table_pipes + new2_new8 all reasoned about with PDF cross-check evidence → **CONSISTENT**
3. **PARTIAL-vs-FAIL discrimination** — this 3rd burn distinguishes data corruption (FAIL) from level-skip-on-cross-cutting (PARTIAL); same calibration as prior burns (round 6 retro reports comparable FAIL-rate restraint when no actual variable-name corruption is present)
4. **Pivot adherence** — type-design-analyzer's default "encapsulation/invariant-expression rating 1-10" is **NOT** emitted in main verdicts; instead reflected metaphorically in §4 only after primary audit complete → **CONSISTENT** with code-reviewer (1st burn) and silent-failure-hunter (2nd burn) which similarly suppressed default modes
5. **Adaptation correctness** — full-tool path used Write tool directly (no Bash-heredoc fallback needed since Write is available); same as prior 2 burns

**Verdict on recipe consistency across 3 agents within pr-review-toolkit family**: **VALIDATED**. The AUDIT-mode pivot recipe holds across `code-reviewer` → `silent-failure-hunter` → `type-design-analyzer` (3 distinct agent personas, all suppressed defaults to perform identical 6-dimension Rule A audit with consistent verdict shape). This **strengthens the round 5 D-MS-3 conclusion** that AUDIT-mode pivot recipe is **family-agnostic AND intra-family-agent-agnostic** (24 successes spanning 8 NEW family burns + 4 cumulative depth burns within respective families).

**Concern flagged for round 7 retro**: 3 PARTIAL on parent_section in a 10-atom sample is higher concentration than prior burns (round 6 batch 29 + 31 reportedly under 2/10 PARTIAL average). Two interpretations:
- (a) §6.3.9.3.2 cross-cutting "common to FT/QS/CC" sub-block is genuinely a parent-ambiguity hot zone (PDF-content artifact, not writer/reviewer regression)
- (b) round 7 writer-direction may be slipping on parent_section discipline post-v1.3 codification (regression watch)

Recommendation: reconciler-side sweep on §6.3.9.3.2 atoms (p.337-339) cross-validation table check vs L4/L5/L6 canonical anchors before merging batch 34.

---

## Final reviewer message

`Rule A batch 34 weighted=85.0% PASS_n=7 PARTIAL_n=3 FAIL_n=0`
