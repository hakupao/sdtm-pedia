# Rule A Verdict Summary — P2 B-03c round 10 batch_105

> Reviewer: pr-review-toolkit:code-reviewer (Rule D 隔离: writer general-purpose ≠ reviewer pr-review-toolkit:code-reviewer)
> Prompt version: P0_reviewer_v1.9.3
> Source: knowledge_base/domains/RELSPEC/examples.md (47 lines)
> Atoms file: P2_B-03_batch_105_md_atoms.jsonl (14 atoms)
> Date: 2026-05-07

## Overall verdict: **PASS** (14/14 = 100%)

## Summary table

| atom_id | type | lines | verbatim | schema | parent | verdict |
|---|---|---|---|---|---|---|
| a001 | HEADING H1 sib=1 | 1 | PASS | PASS | §RELSPEC [RELSPEC — Examples] | PASS |
| a002 | HEADING H2 sib=1 | 3 | PASS | PASS | §RELSPEC [RELSPEC — Examples] | PASS |
| a003 | SENTENCE | 5 | PASS | PASS | §RELSPEC.1 [Example 1] | PASS |
| a004 | SENTENCE (bold-label) | 7 | PASS | PASS | §RELSPEC.1 [Example 1] | PASS |
| a005 | FIGURE (mermaid) | 9-34 | PASS | PASS | §RELSPEC.1 [Example 1] | PASS |
| a006 | SENTENCE | 36 | PASS | PASS | §RELSPEC.1 [Example 1] | PASS |
| a007 | SENTENCE (bold-label) | 38 | PASS | PASS | §RELSPEC.1 [Example 1] | PASS |
| a008 | TABLE_HEADER | 40 | PASS | PASS | §RELSPEC.1 [Example 1] | PASS |
| a009-a014 | TABLE_ROW × 6 | 42-47 | PASS | PASS | §RELSPEC.1 [Example 1] | PASS |

## Rule A check results (20 checks)

1. **atom_id sequential a001..a014, 0 collision**: PASS
2. **file path correct** (`knowledge_base/domains/RELSPEC/examples.md`): PASS
3. **parent_section namespace**:
   - a001 H1 → file-root `§RELSPEC [RELSPEC — Examples]` PASS
   - a002 H2 (numbered) → file-root `§RELSPEC [RELSPEC — Examples]` PASS
   - a003-a014 → §2.5 self-namespace `§RELSPEC.1 [Example 1]` PASS
4. **line ranges within [1,47]**: PASS (all valid; FIGURE 9-34, last atom L47)
5. **atom_type ∈ 9 valid types** (HEADING/SENTENCE/FIGURE/TABLE_HEADER/TABLE_ROW used): PASS
6. **verbatim byte-exact** (programmatic check vs source): PASS 14/14
7. **§E-2 H1 sib=1 hl=1**: PASS
8. **H2 atom L3** hl=2 sib=1, verbatim `## Example 1`, file-root parent: PASS
9. **§2.5 numbered H2 self-namespace** all a003+ children → `§RELSPEC.1 [Example 1]`: **PASS** (12/12 children)
10. **§2.6 FIGURE-in-domains lock**: PASS — a005 atom_type=FIGURE, line_start=9 line_end=34, byte-exact 788 chars including opening ` ```mermaid ` and closing ` ``` ` fences
11. **§E-3 TABLE_HEADER**: a008 atom_type=TABLE_HEADER, sib=null, hl=null PASS
12. **TABLE_ROW** atoms (a009-a014) all hl=null sib=null verbatim correct: PASS
13. **§E-5 non-HEADING field-explicit-null**: PASS (all 12 non-HEADING atoms have hl=null AND sib=null)
14. **§E-4 extracted_by object form** `{subagent_type, prompt_version, ts}`: PASS 14/14
15. **prompt_version = "P0_writer_md_v1.9.3"**: PASS 14/14
16. **12 fields present per atom**: PASS (no missing/extra fields)
17. **§E-6 FIGURE/CODE_LITERAL boundary**: mermaid → FIGURE: PASS
18. **Bold-label lines L7+L38** as SENTENCE: PASS (a004, a007)
19. **Table separator L41 NOT atomized**: PASS — verified no atom for L41 (atoms jump from a008@L40 → a009@L42)
20. **cross_refs**: empty `[]` for all atoms (no cross-references in examples file): PASS

## Schema regression sweep (§R-E1 PRIORITY 1)

**Result: CLEAN** — no schema regression detected vs v1.9.2 baseline. All atoms 12 fields, extracted_by object form intact, hl/sib explicit-null where required, §F-1 backward compat preserved.

## §F-1 §2.11 Plan B namespace verify

**Not triggered** — file has 1 numbered H2 (`## Example 1`) and 0 H3. §2.5 numbered H2 self-namespace path applies, NOT §2.11 Plan B (which requires numberless H2 with H3 children). §F-1 audit gate not exercised this batch.

## §F-2 atoms/line ratio retrospective (INFO non-blocking)

- Raw ratio: 14 / 47 = **0.298** — below empirical band 0.59-0.85
- Driver: §2.6 FIGURE compression — 26 mermaid source lines (L9-L34) collapsed to 1 FIGURE atom
- Mermaid-excluded ratio: (14-1) / (47-26) = 13 / 21 = **0.619** — within band 0.59-0.85
- Verdict: **INFO** — driver identified as expected §2.6 behavior, NOT halt

## §F-3 kickoff atom estimate calibration retrospective (INFO non-blocking)

- Kickoff estimate: 22-32 atoms (mid 27, ratio mid 0.73)
- Actual: 14 atoms
- Delta: |14 - 27| / 27 = **48.1%** — just below 50% flag threshold
- Driver: §2.6 FIGURE compression for 26-line mermaid block (-25 effective atoms vs naive line-by-line)
- **Carry-forward observation**: §F-3 multi-level nested-list calibration may benefit from extension covering FIGURE-bearing files (mermaid blocks ≥ 10 lines compress to 1 atom). Candidate stack item for v2.0 consideration.

## HIGH findings: **none**

## Conclusion

**PASS rate: 14/14 (100%)**, schema CLEAN, byte-exact 100%, §2.5 namespace 12/12 correct, FIGURE byte-exact verified. No HIGH severity findings. Two INFO carry-forward observations (§F-2 ratio + §F-3 kickoff calibration) both attributable to §2.6 FIGURE compression — expected behavior, non-blocking.

Halt conditions: none triggered (PASS rate ≥ 90%, 0 HIGH, 0 schema regression, 0 atom_id collision).
