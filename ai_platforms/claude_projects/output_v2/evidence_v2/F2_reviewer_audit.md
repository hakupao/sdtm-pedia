# F2 Reviewer Audit — Phase 6.5 v2 Task F2

> Reviewer: `oh-my-claudecode:code-reviewer` (opus), subagent_type disjoint from executor (规则 D).
> Scope: `scripts_v2/extract_terminology_terms.py` + `output_v2/11a_terminology_high_core.md` + `11b_terminology_high_questionnaires.md` + `11c_terminology_high_supp.md`.
> Spec refinements in scope: A (Related Domain codelist-level) + B (11a/b/c subdir split) + D (per-file cap relaxed to 350K).

## Verdict: **PASS**

No HIGH issues. No MEDIUM issues. 2 LOW observations (non-blocking).

## Re-verified counts (independently from disk, not from executor claims)

| File | Codelists | Tokens | Under 350K cap |
|------|-----------|--------|----------------|
| 11a_terminology_high_core.md | 29 | 68,559 | YES |
| 11b_terminology_high_questionnaires.md | 152 | 256,336 | YES (above 200K soft, under 350K hard) |
| 11c_terminology_high_supp.md | 19 | 26,857 | YES |
| **TOTAL** | **200** | **351,752** | — |

Set properties verified via Python:
- 11a ∩ 11b = ∅, 11a ∩ 11c = ∅, 11b ∩ 11c = ∅ (no cross-file duplicates).
- union(11a, 11b, 11c) = F1_codelist_high.txt exactly (0 missing, 0 extra, 200 total).

## Subdir alignment (spec B compliance)

- All 29 `<!-- source: -->` markers in 11a_core point inside `knowledge_base/terminology/core/`.
- All 152 markers in 11b_questionnaires point inside `knowledge_base/terminology/questionnaires/`.
- All 19 markers in 11c_supp point inside `knowledge_base/terminology/supplementary/`.
- 0 mismatches.

## Legacy cleanup

`ai_platforms/claude_projects/output_v2/11_terminology_high.md` is no longer on disk. Script logic at lines 672-676 confirms unlink-on-run.

## Per-file cap policy (spec D compliance)

Script `HARD_CAP = 350_000` (line 95). 11b at 256,336 is below 350K, so hard-cap check passes. Exit 0 from re-run.

## Idempotency verification

Re-ran `python3 scripts_v2/extract_terminology_terms.py --tier high --list evidence_v2/F1_codelist_high.txt` from scratch. MD5s matched byte-for-byte:
- 11a: `af59e38b58bf3926f7d6b69bef08c78e` (unchanged)
- 11b: `7a94fa36debb18110124fb66d7573a3a` (unchanged)
- 11c: `d28622aa98a5f1ed3cb1bd2fb3e0bdf7` (unchanged)

Timestamp derived from max-mtime of touched KB sources, not wall clock — good.

## Definition truncation verification (spec: ≤200 chars)

Independently scanned all 3 files: max `defn` cell length = **200** in every file; **0 violations** across 200 codelists. Truncation offenders per executor log match spec (`C71620(88)`, `C141668(33)`, `C141669(33)` rows truncated).

## N=10 sample audit (规则 A, disjoint from main controller's 10)

Main controller reserved: C66742, C71620, C99079, C71148, C135677, C147541, C130272, C166184, C111111, C150770.

My 10 (all disjoint):

| C-code | File | Source file | Terms src | Terms out | Extensible | Related Domains | Finding |
|--------|------|-------------|-----------|-----------|-----------|------------------|---------|
| C66789 | 11a | terminology/core/general_part4.md | 1 | 1 | No | 36 domains | PASS |
| C78735 | 11a | terminology/core/general_part2.md | 52 | 52 | Yes | 19 domains | PASS |
| C66727 | 11a | terminology/core/disposition.md | 37 | 37 | Yes | DS | PASS |
| C135678 | 11b | terminology/questionnaires/questionnaires_part32.md | 29 | 29 | No | — | PASS |
| C124685 | 11b | terminology/questionnaires/questionnaires_part32.md | 30 | 30 | No | — | PASS |
| C106662 | 11b | terminology/questionnaires/questionnaires_part20.md | 31 | 31 | No | — | PASS |
| C117986 | 11b | terminology/questionnaires/questionnaires_part8.md | 28 | 28 | No | — | PASS |
| C66739 | 11c | terminology/supplementary/supplementary_part5.md | 30 | 30 | Yes | — | PASS |
| C174223 | 11c | terminology/supplementary/supplementary_part2.md | 28 | 28 | Yes | — | PASS |
| C138216 | 11c | terminology/supplementary/supplementary_part4.md | 32 | 32 | No | — | PASS |

**All 10 samples: term counts match source verbatim. "Extensible: Yes/No" preserved. "Related Domains:" line present under Extensible (em-dash when empty, comma-separated when populated). Source-order preserved.**

## Independent Related Domain re-derivation (2 codelists)

Independently grepped `knowledge_base/domains/*/spec.md` for each C-code:

### C66727 (Completion/Reason for Non-Completion)
- Output: `Related Domains: DS`
- My re-derivation: `{DS}`
- Result: **EXACT MATCH**

### C78735 (Evaluator)
- Output: `Related Domains: CO, CV, DD, EG, FA, MI, MK, MS, NV, OE, PE, RE, RS, SR, SS, SUPPQUAL, TR, TU, UR` (19)
- My re-derivation: `CO, CV, DD, EG, FA, MI, MK, MS, NV, OE, PE, RE, RS, SR, SS, SUPPQUAL, TR, TU, UR` (19)
- Result: **EXACT MATCH (set equality)**

### C66789 (Not Done) bonus sanity check
- Output lists 36 domains.
- My re-derivation count: 36.
- Result: **EXACT COUNT MATCH**

## Script quality review

### PASS points
- Module docstring (lines 1-55) clearly describes all 3 output files, 规则 A refinement, hard-cap 350K, idempotency strategy. Matches observed behavior.
- Idempotency (lines 389-397): timestamp via `_iso_from_mtimes(touched_paths)` — no wall-clock drift.
- Missing-C-code handling (lines 431-439, 678-680): graceful, non-fatal, writes `failures/stage_v2.4_attempt_1.md`.
- `--tier mid` stub (lines 585-587): prints `NOT_IMPLEMENTED`, rc=2 — verified.
- `--tier high` without `--list` → rc=2 with friendly message (line 590).
- Read-only on KB: all `read_text` calls under `knowledge_base/`; writes limited to `output_v2/` and `evidence_v2/failures/`.
- Output path contract: exactly `11a_terminology_high_core.md`, `11b_...questionnaires.md`, `11c_..._supp.md`. Legacy unlink on line 674-676.
- Syntax check via `ast.parse`: clean.
- Pipe escaping (`_escape_cell`, line 279-281): prevents table corruption from `|` in definitions.
- Domain index (lines 231-260): single-pass over spec.md, dedupes within file to avoid double-count, sorts at end for deterministic output.
- Multi-file codelist aggregation (lines 284-320): dedup by leftmost Code cell, first-seen order preserved.

### LOW observations (non-blocking, note-only)

**[LOW-1]** `build_subdir_documents` (line 452): the return type hint describes the value as a 3-tuple `(full_text, per_cl_summary, truncations)`, but `full_text` is later rebuilt from `out` as a string joined on newlines. The type annotation is correct but verbose; harmless.

**[LOW-2]** `file_num` extraction on lines 476 and 627 shadows `file_num` naming between local variables. Cosmetic; no functional impact.

## Spec deviations found

**None.** Script and output fully implement A+B+D refinements:
- A: Related Domains is a codelist-level metadata line (`Related Domains: ...`), not a per-row column. Verified on all 10 samples. Table remains 4-column.
- B: Output correctly split into 11a/11b/11c by source subdir with 0 mis-filed codelists.
- D: Per-file hard cap relaxed to 350K; all 3 files under cap.

## Issue Summary

| Severity | Count |
|----------|-------|
| HIGH (blocks commit) | **0** |
| MEDIUM (fix next session) | **0** |
| LOW (note only) | 2 |

## Positive observations

- Executor correctly identified that `fail-over` to core when subdir is unexpected is the right safety net (line 468-470), even though 0 records triggered it in practice.
- Stable sort via Python set→sorted list for domain names ensures diff-friendly output across runs.
- Pipe escaping + newline stripping on cells defends against corrupting markdown tables.
- `_iso_from_mtimes` pattern correctly reuses max-mtime across ALL touched files (terminology sources + domain specs), so a change in either triggers a new timestamp.
- Per-codelist stderr summary (tab-separated `code\tterms\ttokens\trd_count`) is grep-friendly for downstream tooling.

## Recommendation

**PASS — safe to commit and stage into v2.4.** Main controller should verify their own 10 samples remain disjoint from my list, merge audit findings, and proceed with stage v2.4 aggregation.
