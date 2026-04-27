---
batch: 28
session: D (round 5)
scope: ig34 p.271-280 (10 pages)
section: §6.3.5.9 Pharmacokinetics Domains body (PP-Specification + PP-Assumptions + PP-Examples + §6.3.5.9.3 Relating PP Records to PC Records with Method A/B/C/D for Examples 1-3)
atoms: 372 (148 28a + 224 28b)
failures: 0
repair_cycles: 3
rule_a_raw: 87.9% (7P/1PA/2F)
rule_a_post_adjudication: 93.9% PASS (8P/1PA/1F)
rule_d_slot: 37 (general-purpose family INAUGURAL burn)
audit_pivot_index: 18
findings: O-P1-88/89/90/91 (4)
drift_cal: skipped (cadence; next mandatory batch 30)
date: 2026-04-27
---

# P1 Batch 28 Report — SDTM Deep Verification multi-session round 5 session D

## §1 Scope + structure

10 pages SDTMIG v3.4 p.271-280, fully within §6.3.5.9 Pharmacokinetics Domains group container (introduced by sister session C batch 27 at p.267). Batch 28 covers:
- PC Example 1 pc.xpt rows 21-32 tail (continuation from batch 27 p.270)
- §6.3.5.9.2 Pharmacokinetics Parameters (PP) full body: Description/Overview + Specification + Assumptions + Examples 1/2/3
- §6.3.5.9.3 Relating PP Records to PC Records full body: PC-PP Relating Datasets + PC-PP Relating Records + Examples 1/2/3 each with Method A/B/C/D + relrec.xpt tables

## §2 Sub-batch breakdown

| sub-batch | writer subagent | pages | atoms | repair |
|---|---|---|---|---|
| 28a | oh-my-claudecode:executor | 271-275 | 148 | Option H atom_id padding (cycle 2) + atom 3 verbatim restore (cycle 3) |
| 28b initial | oh-my-claudecode:writer | 276-280 | 50 (only p.280, 4 pages lost) | — (Option E rerun cycle 1) |
| 28b recovery | oh-my-claudecode:executor | 276-280 | 224 | post-cycle-1 |

Total: 372 atoms post-recovery.

## §3 Rule A audit (slot #37 general-purpose, AUDIT pivot 18th, NEW family inaugural burn)

### Sample (n=10, seed=20260610, 1/page stratified)
- 4 TABLE_ROW + 3 HEADING + 1 LIST_ITEM + 1 TABLE_HEADER + 1 CODE_LITERAL

### Raw verdict
- **7 PASS / 1 PARTIAL / 2 FAIL = 87.9%**

### Main-session PDF cross-check adjudication
- **F1 (atom 3 p.273)**: ✅ reviewer correct — atom verbatim 'pre-coordinating' silently corrected from PDF 'pre-corrdinating' typo. R10 strict no-paraphrase violation. Repaired via Option H cycle 3.
- **F2 (atom 10 p.280)**: ❌ reviewer FALSE POSITIVE — reviewer claimed Row 14 = PPSEQ=2 in Example 1 Method D, atom incorrectly says PPSEQ=4 in Example 2. Main-session PDF cross-check confirms atom is CORRECT: PDF p.280 Method D Example 2 Row 14 = PP PPSEQ=4 RELID=1 exactly. Reviewer confused this with Example 1 Method D table on p.278-279. **Adjudicated PASS** (overrides reviewer FAIL on dim_verbatim + dim_parent_section).
  - **Precedent**: Joins G-MS-12 density alarm 3 FALSE POSITIVE round 2-4 pattern (main-session PDF cross-check adjudicates reviewer-side errors). Reviewer-side FALSE POSITIVE first observation in Rule A audit (vs density alarm domain prior).
- **F3 (atoms 8/9 parent_section)**: stylistic — 'Example N' bare form vs canonical full-form. LOW severity, deferred to reconciler bulk-patch (O-P1-91).

### Post-adjudication verdict
- **8 PASS / 1 PARTIAL / 1 FAIL = 93.9% PASS** (above ≥90% threshold)

## §4 STEP 4 schema + format sweeps

| Sweep | Result |
|---|---|
| JSON parse all 372 atoms | 0 errors |
| atom_type ∈ 9-enum | 0 violations |
| atom_id `ig34_p\d{4}_a\d{3}` | 0 violations (post Option H cycle 2) |
| Within-batch dup atom_id | 0 |
| Root collision (vs 6146 root atoms) | 0 |
| Per-page density (≥15 floor) | 0 violations (lowest p.272=23) |
| Per-sub-batch density (≥100 floor) | 0 violations (28a=148, 28b=224) |
| NEW6.b L4 self-parent | N/A (no L4 in scope) |
| NEW7 L5 chain under §6.3.5.9 | PASS — sib=2 PP + sib=3 Relating PP-PC RESTART correct |
| NEW7 L6 chain under §6.3.5.9.2 PP | PASS — Description/Spec/Assump/Examples sib=1/2/3/4 |
| NEW7 L6 chain under §6.3.5.9.3 | PASS — Relating Datasets/Records + Example 1/2/3 sib=1/2/3/4/5 |
| NEW7 L7 chain (Examples + Methods) | PASS — Example 1/2/3 L7 sib=1/2/3 under PP; Method A/B/C/D L7 sib=1/2/3/4 RESTART per Example |
| NEW7 L4 group container precedent 2nd cross-family validation | PASS — §6.3.5.9 PK validates round-4 §6.3.5.7 Microbiology pattern |
| R12 transition page sweep | PASS — p.271 (30 atoms) + p.275 (29 atoms) both ≥8 with 3-zone partition |
| R15 cross-batch sibling continuity (intra-batch) | PASS — 28a→28b L5/L6 chain continuous |
| R15 cross-session sibling continuity (vs sister batch 27) | DEFERRED to reconciler |
| NEW8 substring n-gram | PASS — 0 char-drift on canonical CDISC variable names; PPRFID/PPFAST verified verbatim per PDF p.274 ground truth (real CDISC strings, not corruptions) |

## §5 Findings (4 total, range O-P1-88..91 reserved + all used)

### O-P1-88 — HIGH writer-family R10 strict EDITORIAL_CORRECTION violation
- **Atom**: ig34_p0273_a037 (LIST_ITEM Row 4 of PP-Examples Example 2)
- **Drift**: PDF 'pre-corrdinating' → atom 'pre-coordinating' (silent multi-char correction; PDF original is CDISC-source typo, missing 'o')
- **Rule violation**: R10 strict no-paraphrase
- **Repair**: Option H cycle 3 — verbatim restored to PDF original
- **v1.3 cut codification candidate**: explicit EDITORIAL_CORRECTION verdict path (writer choice = preserve typo OR flag with `editorial_correction: true` + extracted_by.notes; silent correction = R10 FAIL)

### O-P1-89 — HIGH writer-family NEW motif: Write-tool-overwrite silent data loss
- **Scope**: 28b initial dispatch reported atoms=342 but only saved 50 (p.280 only); p.276-279 ~290 atoms LOST
- **Rule violation**: v1.2 prompt wording '追加 JSONL' (append) but Write tool semantically overwrites; writer family followed instruction literally; per-page Write replaced prior content
- **Repair**: Option E cycle 1 — re-dispatched via oh-my-claudecode:executor with explicit Bash-heredoc append protocol (`cat << 'EOF' >> output_file`) per atom batch + `wc -l` verification. Rule B backup `pdf_atoms_batch_28b.jsonl.pre-recovery-OptionE-p276-280.bak` preserves the 50-atom partial as evidence.
- **NEW motif**: distinct from wide-TABLE_HEADER family (R10 paraphrase) and EDITORIAL_CORRECTION family (O-P1-88); first observation in P1 cumulative
- **v1.3 cut codification candidate**: procedural enforcement — writer/executor agents MUST use Bash-heredoc append for multi-page batches, NOT Write tool (overwrite default). v1.2 §'工作模式' wording must be tool-faithful.
- **Family-specific behavior**: oh-my-claudecode:writer affected; oh-my-claudecode:executor in 28a + 28b recovery completed correctly. Recommend round-5+ writer family carry explicit append protocol.

### O-P1-90 — LOW v1.2 prompt spec ambiguity: atom_id page-padding self-contradiction
- **Issue**: v1.2 §'atom_id 命名规范' text says '3 位 0-pad 页码' but example shows 4-digit `ig34_p0425_a012`; root convention is 4-digit `ig34_p0001_a001`
- **Impact**: ALL 148 28a atoms initially used 3-digit padding (p271 vs root p0001 standard); 28b initial 50-atom write used same; 28b recovery via explicit prompt clarification used 4-digit correctly
- **Repair**: Option H cycle 2 — Python regex bulk fix all 28a atoms; backup `pdf_atoms_batch_28a.jsonl.pre-OptionH-atomid-padding.bak`. Post-fix: 372/372 atom_ids match `ig34_p\d{4}_a\d{3}`. 0 root collision.
- **Root cause**: v1.2 prompt text-vs-example self-contradiction (NOT writer-family error)
- **v1.3 cut codification candidate**: clarify atom_id format = `<source_short>_p<NNNN>_a<NNN>` 4-digit page zero-padded; add explicit regex validator `^[a-z]+_p\d{4}_a\d{3}$`

### O-P1-91 — LOW NEW7 L6/L7 parent_section shortcut form ('Example N' bare vs canonical full-form)
- **Atoms affected**: ~30+ in p.278-280 PP-relrec cluster within §6.3.5.9.3 Examples 1/2/3 — Method A/B/C/D HEADINGs and their relrec.xpt TABLE_ROW children
- **Rule A flag**: ig34_p0278_a010 (PARTIAL) + ig34_p0279_a037 (just-PASS)
- **Issue**: parent_section uses bare 'Example N' instead of canonical full-form '§6.3.5.9.3 Relating PP Records to PC Records — Example N'
- **Severity**: LOW (stylistic, not corruption; both writers used same convention)
- **Repair**: DEFERRED to reconciler bulk-patch — mechanical replace `"parent_section":"Example N"` → `"parent_section":"§6.3.5.9.3 Relating PP Records to PC Records — Example N"` post-merge to root
- **v1.4 codification candidate**: NEW7 chain spec parent_section canonicalization rule — any atom with sub-Example/sub-Method L6/L7 immediate parent MUST use canonical full-form `§N.N.N — Sub-Heading-Title`

## §6 Round 5 / Multi-session protocol observations

### NEW7 L6 sub-batch handoff procedural enforcement EFFECTIVE first-time round 5
- 28a→28b sub-batch handoff prepend (mandatory per round 5 spec) inline-prepended 28a terminal state into 28b recovery dispatch
- 28b output validated correct sib continuation: §6.3.5.9.3 L6 chain Example 1 sib=3 / Example 2 sib=4 / Example 3 sib=5 (continuing from 28a's PC-PP Relating Datasets sib=1 + PC-PP Relating Records sib=2)
- **ZERO recurrence** of NEW7 L6 cross-sub-batch context drift in batch 28 (vs round 3 batch 23 O-P1-68 + round 4 batch 25 O-P1-79 prior recurrences)
- Validates round-4 retro D-MS-4 codification mandatory decision

### General-purpose family INAUGURAL AUDIT-mode pivot burn (slot #37)
- NEW family pivot post round 4 EXHAUSTED 3 family pools (vercel + plugin-dev + feature-dev)
- Tools: full-tool variant (Write tool authorized — vs round 3-4 write-tool-less + Bash heredoc family adaptation)
- Validates AUDIT-mode pivot recipe family-agnostic at 18th cumulative pivot
- Recipe accuracy: 90% (7 valid PASS + 1 valid PARTIAL + 1 valid FAIL + 1 reviewer-side FALSE POSITIVE on cross-Example boundary)
- Adaptation: full-tool variant proven viable; recipe extends to new families without write-tool-less workaround

### Reviewer-side FALSE POSITIVE (atom 10 p.280) — main-session adjudication precedent extension
- Joins G-MS-12 density 3 FALSE POSITIVE round 2-4 pattern
- First Rule A reviewer-side FP (vs density alarm domain prior)
- Adjudication recipe: main-session PDF cross-check + override reviewer dim verdicts when ground truth contradicts
- Reviewer error pattern: cross-Example boundary confusion (Example 1 vs Example 2 Method D table attribution); recipe needs additional cross-Example anchor reinforcement for AUDIT-mode pivots in PP/PC/relrec multi-Example contexts

### v1.3 cut DEFERRED 5th time = ULTRA-CRITICAL ESCALATION
- Round 1/2/3/4/5 all deferred per Rule D writer/reviewer isolation (reconciler session cannot writer-create v1.3 + reviewer-validate without self-overlap)
- Evidence quintuple-saturated (R10-R15 + O-P1-26 + NEW1-NEW8 + NEW6/NEW6.b + NEW7 L4-group-container + NEW7 L6 procedural enforcement first-time-EFFECTIVE round 5 + NEW7 L7 sub-method NEW round-5 + 3 NEW writer-family motifs O-P1-88/89/91 + atom_id spec ambiguity O-P1-90)
- v1.3 cut session BEFORE batch 30 next mandatory drift cal is now ULTRA-CRITICAL 5th-time

## §7 Final state

| Metric | Value |
|---|---|
| Atoms contributed | 372 |
| Pages | 10 (271-280) |
| Failures | 0 |
| Repair cycles | 3 (Option E + 2× Option H) |
| Rule A raw | 87.9% (7P/1PA/2F) |
| Rule A post-adjudication | 93.9% PASS (8P/1PA/1F) |
| Findings added | O-P1-88/89/90/91 (4) |
| Rule D slot | 37 (general-purpose, NEW family inaugural) |
| AUDIT pivot index | 18 |
| Drift cal | SKIP (next batch 30) |
| Halt state | none |

## §8 Handoff to reconciler

See `_progress_batch_28.json` §handoff_to_reconciler — full instructions for cross-batch sibling sweep, audit_matrix update, _progress.json update, v1.3 cut decision (5th-time DEFERRED), v1.4 patch agenda accumulation, multi-session round 5 retro write, and cleanup.

---

> Round 5 batch 28 verdict ✅ — 93.9% post-adjudication PASS; NEW7 L6 procedural handoff first-time-EFFECTIVE zero recurrence; general-purpose family INAUGURAL AUDIT-mode pivot burn validates recipe family-agnostic; 4 NEW findings (3 v1.3 codification + 1 v1.4 codification); v1.3 cut DEFERRED 5th-time ULTRA-CRITICAL ESCALATION.
> The boulder never stops.
