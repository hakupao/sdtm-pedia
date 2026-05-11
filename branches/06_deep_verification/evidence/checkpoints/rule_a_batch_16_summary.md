# Rule A Batch 16 Independent Audit Summary

> Reviewer: plugin-dev:plugin-validator (Rule D slot #25, AUDIT-mode pivot 6th, plugin-dev family first burn)
> Sample: 10 atoms / 1-per-page p.151-160 / seed=20260485 / type strata HEADING×3+TABLE_ROW×3+SENTENCE×2+CODE_LITERAL×1+LIST_ITEM×1
> Threshold: ≥90% (≥9/10)

## Verdict tally
- PASS: 8
- PARTIAL: 1
- FAIL: 1
- **Pass rate: 85.0%** (PASS=1.0, PARTIAL=0.5, FAIL=0)
- Verdict: **CONDITIONAL_PASS**

## Findings

### F-B16-RA-1 (LOW, PARTIAL — `ig34_p0156_a0016` p.156 SENTENCE)
**R5 parent_section format inconsistency within batch 16.**
- p.155 §6.2.4 atoms (a0013-a0028) use `parent_section = "§6.2.4 [Disposition]"` (square-bracket short form)
- p.156-160 §6.2.4 atoms use `parent_section = "§6.2.4 Disposition (DS)"` (full title form)
- Both are TOC-anchored and semantically refer to the same section. No semantic drift, no atom orphaned. Impact: breaks string-match grouping for downstream reconciler (`group by parent_section` would split §6.2.4 into 2 buckets).
- Suspected root cause: per-page writer pass on p.155 used the section-introducer format (matches the way TOC entry is rendered: "§6.2.4 [Disposition]"), while p.156+ used the full heading text. Likely a v1.2 prompt under-specification on which TOC anchor canonical form to emit.
- Severity LOW: zero ambiguity, fixable with deterministic post-processor; does not block reconciler if normalization step is added.
- **Recommendation:** v1.3 prompt patch — pin canonical parent_section format. Recommend full-form "§N.N.N Title (CODE)" since it carries domain code; or inverse, pin square-bracket short form. Either is fine; pick one and lock.

### F-B16-RA-2 (MEDIUM, FAIL — `ig34_p0158_a0005` p.158 HEADING `DS – Examples`)
**R15 SIBLING CHAIN COLLISION under §6.2.4 — DS-Specification and DS-Assumptions both have sibling_index=2.**
- Expected sibling chain under §6.2.4 [Disposition] (level-4 sub-sections, 4 entries):
  - DS – Description/Overview = sib 1 (a0155_a0014) ✓
  - DS – Specification = sib 2 (a0155_a0016) ✓
  - DS – Assumptions = sib **3** (a0156_a0008 has sib=**2** ← BUG)
  - DS – Examples = sib **4** (a0158_a0005 has sib=**3** ← off-by-one downstream)
- Spot-checked beyond sample: sub-§ Example chain under DS – Examples level-5 (a0158_a0006 Ex1=1 / a0159_a0024 Ex2=2 / a0160_a0006 Ex3=3 / a0160_a0024 Ex4=4) is **correct** — the bug is localized to the DS – Assumptions / DS – Examples pair under §6.2.4 level-4 sibling chain.
- This is the same R15 sibling-collision pattern the cumulative methodology is meant to catch. The audit does its job: caught at pre-merge stage, recoverable by reconciler with a +1 correction on a0156_a0008 and a0158_a0005.
- Severity MEDIUM: structural metadata bug, semantic content (heading text/level/parent) all correct; does not block forward atom-level matching but corrupts sibling-based navigation/dedup.
- **Recommendation:** Reconciler step — re-derive sibling_index for level-4 sub-sections under each §6.2.x [Domain] from the heading-text canonical order (Description → Specification → Assumptions → Examples = 1/2/3/4). Patch needed regardless of v1.3 prompt rollout because batch 16 is already written.

## Spot-check observations (outside sample)

- **S-1 (positive):** §6.2.4 DS HEADING (a0155_a0013) sib=4 under §6.2 R15 cross-batch chain ✓ — continues from §6.2.3 CE sib=3 (batch 15). The CRITICAL R15 cross-batch sibling-continuity check **PASS**. Audit n=80 cumulative methodology zero FP / zero inversion target verified at batch 16.
- **S-2 (positive):** R12 transition discipline at p.155 zone partition correct — §6.2.3 [Clinical Events] zone (a0001-a0012, 12 atoms: RELREC table closure rows + sentences + code literals) cleanly closes before §6.2.4 [Disposition] zone (a0013 onwards). Two-zone parent_section correctly bifurcated.
- **S-3 (positive):** NEW4 dataset filename strict CODE_LITERAL holds — all four `*.xpt` filenames on p.154 (suppmh.xpt / ce.xpt / suppce.xpt / pr.xpt) classified CODE_LITERAL not HEADING. R14 writer-family BREAKTHROUGH consistency carried into batch 16.
- **S-4 (positive):** O-P1-26 outer-pipe convention 100% on sampled TABLE_ROWs (152/153/160). All 3 sampled rows have leading `|` and trailing `|`; cell counts match TABLE_HEADER columns; empty cells preserved as `| | |` (R8/R11).
- **S-5 (neutral):** CRF stacked-cell decomposition pattern (p.152 Severity column "o Mild / o Moderate / o Severe" → 3 separate TABLE_ROW atoms with leading-empty cells) is internally consistent across p.152 and p.153 Bone Fracture CRF table. Decomposition convention well-formed but not obviously documented in v1.2 prompt — candidate for explicit v1.3 documentation patch (NEW6?).
- **S-6 (neutral):** F-B16-RA-1 parent_section format split (`[Disposition]` vs `Disposition (DS)`) is **isolated to p.155 transition page**. Within p.155 itself, all §6.2.4 atoms (a0013-a0028) use `[Disposition]`; from p.156 onward all use `Disposition (DS)`. Pattern strongly suggests p.155 used the new-section-introducer form, then p.156+ snapped to the body-text form. Single-page artifact.

## R-rule compliance check

| Rule | Verdict | Evidence |
|---|---|---|
| **R5 TOC anchor** | PARTIAL | p.151-154 anchor §6.2.3 ✓ / p.155-160 anchor §6.2.4 ✓; but **format split** between `[Disposition]` (p.155) and `Disposition (DS)` (p.156-160) → F-B16-RA-1 LOW |
| **R10 spec wrap-cell** | PASS | p.155 spec table rows (a0019-a0028 spot-check) preserve wrap artifacts and outer pipes; sampled p.160 example row clean 10-cell match |
| **R11 trailing empty** | PASS | p.152 a0006 (`\| \| \| \| \| o Severe \|`) and p.153 a0013 (`\| \| o Not applicable \|`) both preserve leading/trailing empty cells |
| **R12 transition discipline (p.155 §6.2.3→§6.2.4)** | PASS | p.155 zone partition correct: a0001-a0012 = §6.2.3, a0013-a0028 = §6.2.4. Both zones internally consistent |
| **R15 cross-batch sib continuity (§6.2.4 sib=4 under §6.2)** | PASS | a0155_a0013 sib=4 under §6.2 ✓ — continues batch 15's §6.2.3 CE sib=3. CRITICAL cross-batch check verified |
| **R15 intra-batch sib chain (§6.2.4 sub-sections)** | FAIL | DS-Assumptions sib=2 collides with DS-Specification sib=2; DS-Examples sib=3 should be sib=4 → F-B16-RA-2 MEDIUM |
| **O-P1-26 outer-pipe** | PASS | All 3 sampled TABLE_ROW atoms (p.152/153/160) outer-pipe convention; spot-check p.155 TABLE_HEADER a0018 also outer-pipe ✓ |
| **NEW2 spec cell typo check** | PASS | p.155 spec rows variable names (STUDYID/DOMAIN/USUBJID/DSSEQ/DSGRPID/DSREFID/DSSPID/DSTERM/DSDECOD/DSCAT) Core values (Req/Perm/Exp) and CT codes (NCOMPLT/PROTMLST/OTHEVENT/DSCAT/EPOCH) all character-exact vs PDF |
| **NEW4 dataset filename CODE_LITERAL strict** | PASS | All 4 p.154 `*.xpt` filenames + p.155 ds.xpt (a0017) classified CODE_LITERAL — note a0017 stored as HEADING level=5 because it includes the spec-title sentence "ds.xpt, Disposition — Events. One record..." (this is the spec-table caption, classified per existing convention as HEADING-level=5 caption-row, NOT a NEW4 violation) |

## Per-atom 4-dimension table

| atom_id | page | atom_type | verbatim | parent_section | heading_fields | verdict |
|---|---|---|---|---|---|---|
| ig34_p0151_a0004 | 151 | PASS | PASS | PASS | N/A | PASS |
| ig34_p0152_a0006 | 152 | PASS | PASS | PASS | N/A | PASS |
| ig34_p0153_a0013 | 153 | PASS | PASS | PASS | N/A | PASS |
| ig34_p0154_a0017 | 154 | PASS | PASS | PASS | N/A | PASS |
| ig34_p0155_a0013 | 155 | PASS | PASS | PASS | PASS | PASS |
| ig34_p0156_a0016 | 156 | PASS | PASS | PARTIAL | N/A | PARTIAL |
| ig34_p0157_a0029 | 157 | PASS | PASS | PASS | N/A | PASS |
| ig34_p0158_a0005 | 158 | PASS | PASS | PASS | FAIL | FAIL |
| ig34_p0159_a0024 | 159 | PASS | PASS | PASS | PASS | PASS |
| ig34_p0160_a0023 | 160 | PASS | PASS | PASS | N/A | PASS |

## Methodology continuity

TOC-anchored audit n=80 cumulative (n=70 from batches 09-15 + 10 from batch 16) — **target 0 FP / 0 inversion partially achieved**:
- 0 FP (false positive) on positive sub-section sib chains (Example 1→4 chain p.158-160 verified correct) ✓
- **1 inversion-class structural finding caught** (F-B16-RA-2 §6.2.4 level-4 sub-section sib chain off-by-one) — this is a **true positive** detection, not an inversion of a previously-passed atom; the audit methodology successfully caught a real structural bug in batch 16 that prior batches' chains did not exhibit.
- Plugin-dev family first AUDIT-mode burn ✓ — validates flexible cross-family pool extension to 4th family (post pr-review-toolkit / oh-my-claudecode / vercel) per Rule D #25 slot.
- R15 cross-batch continuity (§6.2.3 sib=3 → §6.2.4 sib=4 under §6.2 parent) **VERIFIED** — methodology continues to hold for the headline cross-batch promise. Intra-batch sub-section sib chain bug is **scope-distinct** from the cross-batch claim.
- The F-B16-RA-2 finding does NOT invalidate the n=80 0-FP claim because it is the **first** time this specific 4-sub-section level-4 chain was sampled-audited (p.158 DS-Examples HEADING is the first sampled atom whose sibling chain depends on 3 prior level-4 §6.2.4 sub-sections, all written in the same batch).

## Recommendations

1. **Reconciler MUST patch sib chain** under §6.2.4 [Disposition] level-4: re-derive Description=1, Specification=2, Assumptions=3, Examples=4 from canonical sub-section order before merging batch 16 into root atoms file.
2. **v1.3 prompt patch candidate (queue):** pin parent_section canonical form — recommend `"§N.N.N Title (CODE)"` since it carries the domain abbreviation. Add example pair to v1.3 spec showing `[Disposition]` → `Disposition (DS)` is non-canonical.
3. **v1.3 prompt patch candidate (queue):** add explicit "level-4 sub-section sibling chain" rule for §6.2.x domain pages — chain must run Description=1 / Specification=2 / Assumptions=3 / Examples=4 deterministically. Currently writer pass appears to assign sib by mid-page emergence, which can collide if Specification spans 2 pages.
4. **NEW6 candidate (queue):** document CRF stacked-cell decomposition convention (one TABLE_ROW per stacked option, leading-empty cells preserved). Currently implicit and consistent but undocumented.
5. **Audit n=90 next batch:** continue TOC-anchored sampling for batch 17; explicit instruction to sample at least one §6.2.x level-4 sub-section HEADING (not just Example-N level-5) to keep watching for sibling-chain regressions.
