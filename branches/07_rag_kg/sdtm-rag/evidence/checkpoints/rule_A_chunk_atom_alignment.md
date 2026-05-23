# Rule A — Chunk-Atom Alignment Verification

**Date:** 2026-05-23
**Reviewer:** Independent scientist agent (Rule D isolation from Phase 1A writer)
**Chroma collection:** `sdtm_kb_v1` (4 146 chunks, PersistentClient)
**KB root:** `/Users/bojiangzhang/MyProject/sdtm-pedia/knowledge_base`
**Sample seed:** 20260522 (N=10 SOURCED atoms from 06 Deep Verification reverse_ledger)

---

## Summary Table

| # | atom_id | file | atom_section | chunk_id found | chunk `section` meta | text found | verdict |
|---|---------|------|-------------|----------------|----------------------|-----------|---------|
| 1 | md_ch08_a046 | chapters/ch08_relationships.md | §8.1.1 [--GRPID Example] | `chapters/ch08_relationships.md#0` | 8.1.1 | YES | **PASS** |
| 2 | md_ch01_a041 | chapters/ch01_introduction.md | §1.3 | `chapters/ch01_introduction.md#0` | whole_file | YES | **PASS** |
| 3 | md_dmIS_ex_a127 | domains/IS/examples.md | §IS.9 [Example 9] | `domains/IS/examples.md#8` | IS.9 | YES | **PASS** |
| 4 | md_dmRELSPEC_ex_a010 | domains/RELSPEC/examples.md | §RELSPEC.1 [Example 1] | `domains/RELSPEC/examples.md#0` | RELSPEC.1 | YES | **PASS** |
| 5 | md_dmTV_assn_a005 | domains/TV/assumptions.md | §TV | `domains/TV/assumptions.md#4` | item_4 | YES | **PASS** |
| 6 | md_dmIS_ex_a042 | domains/IS/examples.md | §IS.3 [Example 3] | `domains/IS/examples.md#2` | IS.3 | YES | **PASS** |
| 7 | md_dmRELSUB_ex_a019 | domains/RELSUB/examples.md | §RELSUB.1 | `domains/RELSUB/examples.md#0` | Example 1 | YES | **PASS** |
| 8 | md_dmRE_ex_a025 | domains/RE/examples.md | §RE.2 [Example 2] | `domains/RE/examples.md#1` | RE.2 | YES | **PASS** |
| 9 | md_ch04_a971 | chapters/ch04_general_assumptions.md | §4.5.5 | `chapters/ch04_general_assumptions.md#40` | 4.5.5 | YES | **PASS** |
| 10 | md_ch04_a196 | chapters/ch04_general_assumptions.md | §4.2.2 | `chapters/ch04_general_assumptions.md#10` | 4.2.2 | YES | **PASS** |

---

## Overall Score

**10 / 10 PASS** — exceeds the ≥9/10 threshold.

[FINDING] All 10 sampled atoms were found verbatim inside their expected Chroma chunks.
[STAT:n] n = 10 (seed=20260522, SOURCED atoms only)
[STAT:p_value] Exact binomial: observed 10/10; one-sided p < 0.001 vs null hypothesis p_pass = 0.50
[STAT:effect_size] Pass rate = 1.00 (95% Clopper-Pearson CI: [0.69, 1.00])

---

## Section Metadata Alignment

7 / 10 atoms showed full section label MATCH between the atom's `parent_section` and the chunk's `section` metadata field. The 3 apparent MISMATCHes are explained below — all are benign naming conventions, not content errors.

### MISMATCH Detail

| atom_id | atom parent_section | chunk `section` meta | Explanation |
|---------|--------------------|-----------------------|-------------|
| md_ch01_a041 | §1.3 | `whole_file` | `ch01_introduction.md` is a single-chunk file (1 chunk total). The chunker correctly labels it `whole_file` since no sub-section split occurred. The atom text is present. |
| md_dmTV_assn_a005 | §TV | `item_4` | The atom's ledger records a coarse parent section `§TV` (domain-level). The chunker refined it to `item_4` (the 4th list item). More specific, not wrong. |
| md_dmRELSUB_ex_a019 | §RELSUB.1 | `Example 1` | Ledger uses the heading token `RELSUB.1`; chunker metadata stores the rendered heading text `Example 1`. Semantically equivalent — same section. |

---

## Observations

1. **Chunk boundary integrity is sound.** Long files like `ch04_general_assumptions.md` (47 chunks) and `domains/IS/examples.md` (11 chunks) correctly distribute atoms across chunk indices with no cross-contamination detected.

2. **Single-file chunk case.** Three files — `ch01_introduction.md`, `domains/RELSPEC/examples.md`, `domains/RELSUB/examples.md` — each produced exactly 1 chunk (whole file). Their atoms were found in chunk `#0`. This is expected for short source files; no issue.

3. **Section metadata naming convention gap.** The 3 MISMATCH cases reveal a minor terminology divergence between the reverse_ledger's `parent_section` labels (using the markdown heading notation from the atom extraction pass) and the chunker's `section` metadata field (which may use `whole_file`, `item_N`, or rendered heading text). This does not affect retrieval correctness — text lookup succeeds — but could affect metadata-filtered queries. Worth noting for Phase 1B query evaluation.

4. **No atom found in a wrong file.** Every found chunk ID has a prefix matching the atom's declared source file — no cross-file contamination.

---

## Verdict

**PASS** — Rule A chunk-atom alignment is verified at 10/10 (100%). The ingestion pipeline correctly places all sampled atom content inside the Chroma chunks corresponding to their source files. The 3 section metadata naming variations are minor convention differences and do not constitute failures.

[LIMITATION] Sample size is N=10 from a corpus of >10 000 atoms; tail-case errors (very short atoms, atoms near chunk boundaries, non-ASCII content) are not covered by this sample. A larger random audit (N≥50) would provide tighter confidence bounds.

---

*Verification executed: 2026-05-23 by independent scientist agent. No chunker, ingest, or Chroma data was modified.*
