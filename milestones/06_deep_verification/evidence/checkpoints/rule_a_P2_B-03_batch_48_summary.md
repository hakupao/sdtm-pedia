# Rule A Audit — P2 B-03 batch_48 (FA/assumptions.md)

> Reviewer subagent_type: pr-review-toolkit:code-reviewer (per round 04 default per-batch reviewer pool)
> Writer subagent_type: general-purpose+P0_writer_md_v1.9.1 (per atom `extracted_by` field)
> Rule D 隔离: PASS (writer ≠ reviewer subagent_type)
> Prompt version: P0_reviewer_v1.9.1
> Audit date: 2026-05-06
> Source: knowledge_base/domains/FA/assumptions.md (15L)
> Writer output: P2_B-03_batch_48_md_atoms.jsonl (9 atoms)

## §1. Sample plan

**Full coverage** — file is small (15L / 9 atoms / homogeneous), so all 9 atoms sampled (boundary 3 + stratified 6). Standard B-02 8-boundary + 3-stratified rule for ≥30 atoms relaxed per umbrella convention for ≤15-atom files.

| # | atom_id | role |
|---|---|---|
| s01 | a001 | boundary — H1 file root (sib_idx=1 universal precedent check) |
| s02 | a002 | boundary — first LIST_ITEM after H1 (sib_idx null lock check) |
| s03 | a003 | stratified — multi cross_refs |
| s04 | a004 | stratified — single cross_ref |
| s05 | a005 | stratified — long LIST_ITEM with `e.g.` inline |
| s06 | a006 | stratified — sub-bullet 4.a (3-space indent + URL) |
| s07 | a007 | stratified — parent LIST_ITEM #5 |
| s08 | a008 | stratified — sub-bullet 5.a (3-space indent) |
| s09 | a009 | boundary — final LIST_ITEM #6 (file tail) |

## §2. Verdict matrix

| atom_id | verbatim | line_range | atom_type | sib_idx | parent_section | C-8 | A-4 | cross_refs | overall |
|---|---|---|---|---|---|---|---|---|---|
| a001 | PASS | PASS | HEADING h1 | =1 ✓ | §FA root ✓ | ✓ | ✓ | empty ✓ | **PASS** |
| a002 | PASS | PASS | LIST_ITEM | null ✓ | §FA root ✓ | ✓ | ✓ | empty ✓ | **PASS** |
| a003 | PASS | PASS | LIST_ITEM | null ✓ | §FA root ✓ | ✓ | ✓ | 6.4.1+8.6.3 ✓ | **PASS** |
| a004 | PASS | PASS | LIST_ITEM | null ✓ | §FA root ✓ | ✓ | ✓ | 6.4.2 ✓ | **PASS** |
| a005 | PASS | PASS | LIST_ITEM | null ✓ | §FA root ✓ | ✓ | ✓ | 6.4.3 ✓ | **PASS** |
| a006 | PASS | PASS | LIST_ITEM (4.a) | null ✓ | §FA root ✓ | ✓ | ✓ | empty ✓ | **PASS** |
| a007 | PASS | PASS | LIST_ITEM | null ✓ | §FA root ✓ | ✓ | ✓ | empty ✓ | **PASS** |
| a008 | PASS | PASS | LIST_ITEM (5.a) | null ✓ | §FA root ✓ | ✓ | ✓ | empty ✓ | **PASS** |
| a009 | PASS | PASS | LIST_ITEM | null ✓ | §FA root ✓ | ✓ | ✓ | empty ✓ | **PASS** |

**PASS rate**: 9/9 = **100.0%**

## §3. Invariants

| # | Invariant | Result |
|---|---|---|
| 1 | atom_id sequence a001..a009 strict monotonic, no collision | PASS (9 unique IDs in order) |
| 2 | Hook C-8 universal: file = `knowledge_base/domains/FA/assumptions.md` for all 9 | PASS |
| 3 | Hook A-4 universal: figure_ref=null for all (no FIGURE atoms — kickoff §0.5 row 14 grep 0 mermaid) | PASS |
| 4 | H1 sib_idx=1 (universal precedent — NOT null per round 03 H1 lock) | PASS (a001 sib=1) |
| 5 | LIST_ITEM sib_idx null universal (round 03 lock) | PASS (8/8 LIST_ITEMs sib_idx=null) |

**Invariants**: 5/5 PASS

## §4. Kickoff drift verification (Hook R24 / R-D1)

Kickoff §0.5 claims for batch_48 source: `knowledge_base/domains/FA/assumptions.md = 15L`. Reviewer independent `wc -l` = 15. **No drift.**

Kickoff §1 estimate: 8-13 atoms. Writer produced 9 atoms. **Within range** (no halt #8 trigger).

Kickoff §2.7 explicit claim: round 04 first-time numberless H2 in assumptions.md applies to **FT/ass batch_50** only. FA/assumptions.md (this batch) has **0 H2** (independent grep verified — only `# FA — Assumptions` H1). §2.7 numberless H2 lock therefore **N/A** for batch_48; file-root parent_section for all atoms is the natural canonical state, not D-D8 codified anomaly.

## §5. D-rule applicability scan (v1.9.1 §R-D1..D-8)

| D-rule | Trigger pattern | Present in batch_48? | Reviewer action |
|---|---|---|---|
| §R-D2 NOTE-BQ | `> **Note:**` / `> **Exception:**` blockquote | No | N/A |
| §R-D3 D5 dual-constraint h_lvl | numbered H2/H3 with semantic-divergent parent | No | N/A |
| §R-D4 D8 numberless `## Overview` chapter root | numberless H2 with children inheriting chapter root | No (0 H2 in file) | N/A |
| §R-D5 bold-caption SENTENCE | `**Caption:** ...` non-Note | No | N/A |
| §R-D6 TABLE_HEADER pilot legacy | TABLE_HEADER atom in ch04 a<a219 | No (no TABLE atoms; file is domains/ not ch04) | N/A |
| §R-D7.2 Axis 5 LIST_ITEM ordered `N.` | `^N\.\s+` ordered list as LIST_ITEM | Yes (a002-a005, a007, a009) | accept canonical ✓ |
| §R-D7.3 inline cross_refs | `(see §...)` or `Section X.Y.Z` mentions in cross_refs field | Yes (a003, a004, a005) | accept canonical ✓ |
| §R-D7.6 trailing-narrative parent | inherit closest H2/H3 parent (here: H1 file root since 0 H2) | Yes (all 9 atoms inherit file root) | accept canonical ✓ |

**Anomaly stratified sample**: §R-D7.2 ordered LIST_ITEM verified across a002-a005/a007/a009 (6 instances) — verbatim preserves leading `N. ` byte-exact. §R-D7.3 cross_refs declared 1:1 with in-text Section-mentions (a003 2 refs, a004/a005 1 ref each — verified by regex extraction).

## §6. Hex-dump style preservation spot-checks

- a006 leading 3-space indent + `a. ` prefix preserved byte-exact (`   a. Associations...`)
- a008 same 3-space + `a. ` pattern preserved byte-exact (`   a. The FAOBJ...`)
- a001 H1 single-`# ` prefix + em-dash `—` (U+2014, 3-byte UTF-8) preserved
- All 6 numbered LIST_ITEMs (a002-a005, a007, a009) leading `N. ` (digit + period + space) preserved without normalization

No NOTE-BQ instances in batch_48 → Hook R-D2 hex-dump verify N/A.

## §7. Findings

**0 HIGH / 0 MEDIUM / 0 LOW findings.**

Writer atoms = byte-exact source preservation; sib_idx invariants honored (H1=1, LIST_ITEM=null); cross_refs faithfully extracted; parent_section uniformly file root since FA/ass has no H2 (kickoff §2.7 numberless-H2 lock is N/A for this file — that lock targets FT/ass batch_50). All Rule A v1.9.1 hooks pass.

## §8. Comparison to round 03 baseline

| Metric | Round 03 (12 batches) | Batch_48 |
|---|---|---|
| Per-batch PASS rate | 100% × 12 batches | 100% (9/9) |
| Invariants | 8/8 per round-close | 5/5 per-batch (subset applicable) |
| HIGH/MEDIUM/LOW findings | 0/0/0 | 0/0/0 |

Sustains the round 03 100% strict PASS trend.

---

BATCH_48_RULE_A PASS rate=100.0% invariants=5/5 findings=[]
