# Rule A audit — P2 B-03 batch_50 (FT/assumptions.md, round 04 §2.7 first-time numberless H2 in ass.md)

> Reviewer: independent subagent (writer subagent_type=`general-purpose`, reviewer ≠ writer per Rule D)
> Prompt version: P0_reviewer_v1.9.1
> Mode: AUDIT — JSONL atoms vs source byte-exact + §2.7 lock independent verification
> Date: 2026-05-06
> Source: `knowledge_base/domains/FT/assumptions.md` (53L)
> Writer output: `evidence/checkpoints/P2_B-03_batch_50_md_atoms.jsonl` (38 atoms)

---

## 1. Sample plan

13 verdicts = 8 boundary + 5 stratified (slightly more than per-batch standard 11 given §2.7 first-time critical scrutiny).

- Boundary atoms (8): a001 (H1) / a002 (L3 SENTENCE pre-H2) / a003 (L5 LIST 1 pre-H2) / a004 (L7 LIST 2 pre-H2) / **a005 (L9 H2 §2.7 critical)** / a006 (L11 SENTENCE post-H2) / a007 (L13 first LIST post-H2) / a038 (L53 last)
- Stratified (5): a019 (L28 Roman i sub) / a022 (L31 deepest 4-level sub) / a024 (L33 cross_refs) / a031 (L43 long LIST + 2 cross_refs) / a035 (L49 a. sub post-H2)

---

## 2. Verdicts

13/13 PASS, 0 FAIL.

| # | atom_id | category | verdict |
|---|---|---|---|
| v01 | md_dmFT_assn_a001 | boundary H1 | PASS |
| v02 | md_dmFT_assn_a002 | boundary SENTENCE pre-H2 | PASS |
| v03 | md_dmFT_assn_a003 | boundary LIST_ITEM 1 pre-H2 | PASS |
| v04 | md_dmFT_assn_a004 | boundary LIST_ITEM 2 pre-H2 | PASS |
| **v05** | **md_dmFT_assn_a005** | **boundary §2.7 H2 critical** | **PASS** |
| v06 | md_dmFT_assn_a006 | boundary SENTENCE post-H2 | PASS |
| v07 | md_dmFT_assn_a007 | boundary LIST_ITEM 1 post-H2 | PASS |
| v08 | md_dmFT_assn_a038 | boundary last | PASS |
| v09 | md_dmFT_assn_a019 | stratified Roman sub | PASS |
| v10 | md_dmFT_assn_a022 | stratified deepest 4-level sub | PASS |
| v11 | md_dmFT_assn_a024 | stratified cross_refs | PASS |
| v12 | md_dmFT_assn_a031 | stratified long + 2 cross_refs | PASS |
| v13 | md_dmFT_assn_a035 | stratified a. sub post-H2 | PASS |

PASS rate = **13/13 = 100%**.

---

## 3. §2.7 LOCK independent verification (CRITICAL — round 04 first-time)

Independent grep verified all four §2.7 invariants:

### 3.1 a005 numberless H2 atom (verdict v05)

| Field | Required | Actual | Match |
|---|---|---|---|
| atom_type | HEADING | HEADING | ✓ |
| heading_level | 2 | 2 | ✓ |
| sibling_index | 1 (1st numberless H2 in file) | 1 | ✓ |
| parent_section | `§FT [FT — Assumptions]` (file root, NOT sub-namespace) | `§FT [FT — Assumptions]` | ✓ |
| verbatim | `## QRS Shared Assumptions` byte-exact L9 | `## QRS Shared Assumptions` | ✓ |

5/5 §2.7 critical fields PASS for a005.

### 3.2 All 38 atoms parent_section uniformity

```
$ python3 ... Counter(a['parent_section'] for a in atoms)
Counter({'§FT [FT — Assumptions]': 38})
```

**38/38 atoms have parent_section=`§FT [FT — Assumptions]`. Zero atoms with sub-namespace `§FT.QRS [...]` or any other variant.**

§2.7 LOCK invariant **fully enforced**. D-D8 numberless H2 chapter-root inherit canonical.

### 3.3 a001 H1 atom

| Field | Required | Actual | Match |
|---|---|---|---|
| atom_type | HEADING | HEADING | ✓ |
| heading_level | 1 | 1 | ✓ |
| sibling_index | 1 (universal H1 sib=1 precedent) | 1 | ✓ |
| parent_section | `§FT [FT — Assumptions]` | `§FT [FT — Assumptions]` | ✓ |
| verbatim | `# FT — Assumptions` byte-exact L1 | `# FT — Assumptions` | ✓ |

5/5 PASS.

### 3.4 All 34 LIST_ITEM atoms sib_idx null (round 03 lock)

```
LIST_ITEM with non-null sib_idx: 0
```

**34/34 LIST_ITEM atoms have sibling_index=null** regardless of source numbering (1-10 or sub-letters a/b/c/d or Roman i/ii/iii or deep numeric `1.`). Round 03 lock honored.

### 3.5 SENTENCE sib chain across H2 boundary (interpretation note)

a002 (L3 pre-H2) sib=1; a006 (L11 post-H2) sib=2. SENTENCE atoms continue sib chain across H2 boundary at the file-root parent level — semantically correct under D-D8 chapter-root inherit (since both SENTENCE atoms share the same parent_section `§FT [FT — Assumptions]`, sib indexing is per-parent monotonic). **Not flagged as defect** per §R-D4 (D8 numberless H2 chapter-root inherit acceptance).

**§2.7 = PASS**

---

## 4. Round invariants (5/5 PASS)

| # | Invariant | Status |
|---|---|---|
| 1 | atom_id collision = 0 | ✓ unique 38/38 |
| 2 | Hook C-8: 38/38 `knowledge_base/` prefix | ✓ 38/38 |
| 3 | H3a sub-namespace N/A (verify 0 H3 atoms) | ✓ 0 atoms heading_level=3 |
| 4 | TABLE_HEADER Hook A1 N/A (verify 0 TABLE_HEADER atoms) | ✓ 0 TABLE_HEADER + 0 FIGURE |
| 5 | extracted_by consistency | ✓ all 38 = `(general-purpose, P0_writer_md_v1.9.1)` |

All 5/5 round invariants PASS.

---

## 5. Atom_type breakdown

```
LIST_ITEM: 34
HEADING:    2  (a001 H1 + a005 H2)
SENTENCE:   2  (a002 pre-H2 + a006 post-H2)
TOTAL:     38
```

Matches kickoff §2.2 expectation (1 H1 + 1 numberless H2 + 2 SENTENCE + 34 LIST_ITEM = 38). Atom count 38 in within halt range [27×0.5=13, 45×1.5=67] for batch_50.

---

## 6. Kickoff drift verification (per §R-D1 mandatory section)

Kickoff §0.5 row 12 claims FT/ass = 53L with 1 numberless H2 at L9 `## QRS Shared Assumptions`. Independent verify:
- `wc -l knowledge_base/domains/FT/assumptions.md` → 53 ✓
- `grep -nE "^## " knowledge_base/domains/FT/assumptions.md` → `9:## QRS Shared Assumptions` (only 1 match) ✓

Kickoff numeric claim row 12 byte-exact verified. **No kickoff drift detected.** Hook R24 not triggered.

---

## 7. Findings

**Zero findings of any severity.** No HIGH / MEDIUM / LOW defects. No interpretation-vs-defect ambiguity (Hook R23 not triggered).

§2.7 first-time application of D-D8 numberless H2 chapter-root inherit in `assumptions.md` (vs prior round 02-03 examples.md only) is **canonically enforced** by writer. The convention extends cleanly: H2 atom itself sib=1 + parent=file-root; under-H2 children atoms inherit file-root parent without creating any sub-namespace.

---

## 8. Final verdict

```
BATCH_50_RULE_A PASS rate=100% invariants=5/5 §2.7=PASS findings=[]
```
