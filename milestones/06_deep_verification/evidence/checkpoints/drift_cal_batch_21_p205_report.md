# Drift Cal — Batch 21 p.205 (round 3)

**Date**: 2026-04-26
**Session**: C (batch 21)
**Cadence trigger**: every-3-batches (last cal batch 18 p.180 → next mandatory batch 21) + cumulative atoms post-p.180 (batch 19 226 + batch 20 ~280-320 + batch 21 185 = ~691-731 ≥300 双触发 mandatory)
**Target page**: p.205 — CP-Assumptions HEADING + 16 numbered/lettered/roman LIST_ITEMs (per kickoff priority p.205, 17 atoms ≥15 threshold satisfied)
**Methodology**: NEW1 dual-threshold (strict count + verbatim hash overlap, both ≥80% PASS)

---

## §1 Pair design

| Role | Subagent | Output |
|---|---|---|
| Baseline | `oh-my-claudecode:executor` (sub-batch 21a, p.201-205 range) | `pdf_atoms_batch_21a.jsonl` (p.205 = 17 atoms) |
| Rerun | `oh-my-claudecode:writer` (drift cal independent re-run, p.205 single page) | `drift_cal_p205_writer_rerun.jsonl` (17 atoms) |

Alternation rule: 21a baseline = executor → drift cal rerun = writer (opposite family). Per round 2 batch 18 precedent.

---

## §2 NEW1 dual-threshold computation

### Strict count match
- Baseline: 17 atoms
- Rerun: 17 atoms
- Strict: 17/17 = **100.0%** → ✅ **PASS** (≥80% threshold)

### Verbatim hash overlap
- Hash signature: SHA256 of `(atom_type | verbatim)` per atom
- Baseline unique hashes: 17
- Rerun unique hashes: 17
- Intersection: 16
- Overlap ratio (intersection / max): **94.1%** → ✅ **PASS** (≥80% threshold)
- Jaccard (intersection / union = 16/18): 88.9%

### Overall verdict
**✅ PASS (both ≥80%)**

---

## §3 Difference analysis (1 atom divergence)

### Atom in baseline only (rerun missing this exact verbatim)
- `ig34_p0205_a005` [LIST_ITEM]: `4. CPCELSTA is used in conjunction with CPCSMRKS. When CPCELSTA is populated, CPCSMRKS must also be populated. Conversel...`

### Atom in rerun only (baseline missing this exact verbatim)
- `ig34_p0205_a005` [LIST_ITEM]: `4. CPCELSTA is used in conjunction with CPSCMRKS. When CPCELSTA is populated, CPSCMRKS must also be populated. Conversel...`

### Diff localized
- Position: variable name within "CPCELSTA is used in conjunction with X" + 2 more occurrences
- Baseline writes: **CPCSMRKS**
- Rerun writes: **CPSCMRKS**
- Diff: **C/S adjacent character swap** in 3 occurrences within the same LIST_ITEM (positions 4, 7+1, 7+1)

---

## §4 Root cause analysis

### Ground truth verification (PDF cross-check)
PDF p.201 spec table row for variable `CPCSMRKS` shows "Cell State Marker String" with Variable Name column literal **`CPCSMRKS`**. p.207 (item 8 "Recommended formatting of marker string variables CPMRKSTR, CPSBMRKS, and CPCSMRKS") also confirms **`CPCSMRKS`**. Decoding: CP + CS + MRKS = Cell-Phenotype + Cell-State + MaRKer-String. The expansion is unambiguous.

### Direction
**Baseline (executor) is correct.**
**Rerun (writer) introduced drift.** Direction REVERSED — same pattern as round 2 batch 18 6th precedent.

### Motif categorization
**Writer-family character-swap motif** (adjacent-letter swap C↔S in trigram CSC vs SCC). New variant of the writer-family character-drop / character-swap pattern family:
- O-P1-23 DSDTC (character-drop)
- O-P1-34 ECNKID (character-drop in DALNKID)
- O-P1-36 STUDIID (character-extra-letter in STUDYID)
- O-P1-46 DALKID (character-drop in DALNKID + paraphrases)
- **O-P1-NEW (this report) CPSCMRKS (character-swap in CPCSMRKS)** — 7th drift cal precedent + 7th DIRECTION REVERSED instance + new sub-motif within character-error family

Notably the same writer-family rerun **self-caught** another character drift in the same page during its own NEW2 self-validation pass (Cyrillic `CPCЕЛSTA` → `CPCELSTA` self-correction). This shows NEW2 character-level self-validation catches **non-Latin-character substitutions** (Cyrillic ↔ Latin glyph collision) but **misses adjacent-letter swaps within Latin alphabet** (C↔S which look correct character-by-character but encode wrong semantic substring).

### Implication for NEW2 v1.3 candidate
NEW2 needs strengthening: post-character validation should also verify **trigram/4-gram substring match against canonical CDISC variable names** (e.g., CPCSMRKS / CPMRKSTR / CPSBMRKS / etc.). Adjacent-character-swap is undetectable by single-character iteration but easily caught by substring n-gram check against a canonical variable list.

---

## §5 Action

### Decision
- ✅ NO root file repair (baseline 21a correct → root will inherit correct CPCSMRKS via reconciler merge)
- ✅ NO Option E full-page rerun (drift confined to 1 atom, isolated character-swap)
- ✅ NO Option H bulk fix (single-atom isolated drift, not systemic)
- ✅ Document for v1.3 candidate (NEW2 strengthening — substring n-gram cross-check)

### Repair cycle counter
**+0** (no repair action triggered; drift cal value-add is detection + categorization, not correction)

---

## §6 Files

| File | Purpose |
|---|---|
| `pdf_atoms_batch_21a.jsonl` (p.205 = 17 atoms) | Baseline executor output |
| `drift_cal_p205_writer_rerun.jsonl` (17 atoms) | Rerun writer output |
| `drift_cal_batch_21_p205_report.md` (this file) | NEW1 dual-threshold verdict + root cause + action |

---

## §7 v1.3 candidate update (drift cal value-add)

**NEW8 candidate (proposed)**: Substring n-gram cross-check for CDISC variable names. Augment NEW2 character-level self-validation with:
- Pre-publish step: extract all candidate variable names from atom verbatim using regex `/[A-Z]{3,}/g`
- For each candidate, compute trigrams + 4-grams
- Cross-check against canonical CDISC variable name list (extracted from PDF spec table column 1 "Variable Name" + cumulative root atoms)
- If candidate has trigram/4-gram match to canonical name within Levenshtein distance 1-2 BUT differs character-by-character → flag for human review

This catches **adjacent character swap** (C↔S, I↔L), **transposition** (CSCB ↔ SCBC), **homoglyph substitution** (Latin O ↔ digit 0, Latin l ↔ digit 1) — patterns that single-character iteration misses.

Validate on 5+ batches before formal v1.3 cut. Cross-validate with reviewer-side Rule A spot-check.

---

*Authored by main session C 2026-04-26 post drift cal p.205 NEW1 dual-threshold + root cause categorization. Per round 3 G-MS-7 finding ID range pre-allocation: O-P1-NEW slot reserved within batch 21 range O-P1-63..66 (per multi-session round 3 protocol). Writer-family character-swap 7th drift cal precedent + 7th DIRECTION REVERSED instance.*
