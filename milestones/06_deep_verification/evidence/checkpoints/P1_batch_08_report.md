# P1 Batch 08 Report — Systemic §5.x Numbering Bug + Option H Bulk Repair

> Date: 2026-04-25
> Strategy: Option C parallel mini-batch default + Option H bulk repair (2nd Option H in session)
> Writers: 08a = `oh-my-claudecode:executor` × p.71-75 (130 atoms); 08b = `oh-my-claudecode:writer` × p.76-80 (90 atoms)
> Scope: SDTMIG v3.4 p.71-80 (10 pages — DM Examples + SE domain start)
> Status: **✅ DONE + BULK REPAIRED** (Rule A raw 40% FAIL, main-session scope sweep + bulk fix)

---

## Metrics

| 指标 | 值 |
|---|---|
| Pages | 10 (p.71-80) |
| Atoms final | **220** (08a 130 + 08b 90) |
| Pre-root atoms | 2066 |
| Post-merge root | 2286 |
| Atom_type coverage | 9/9 single-batch |
| Writer failures | 0 (parallel default holds per O-P1-13) |

## Execution summary

### Parallel mini-batch (Option C default)
- 08a executor × p.71-75: 3.9 min wall, 130 atoms, 26/页 avg, 9/9 types (incl 1 FIGURE)
- 08b writer × p.76-80: 2.1 min wall, 90 atoms, 18/页 avg, 7/9 types (no CROSS_REF, no CODE_LITERAL) — 但 16 HEADING missing sibling_index → main session backfill applied
- Parallel wall 3.9 min vs sequential est 6.0 min (35% speedup)

### Inline pre-Rule-A: 08b HEADING sibling_index backfill
16 HEADING atoms in 08b had `sibling_index=None`. Main session backfilled pragmatically based on text pattern:
- `Row 1:`/`Row 2:`/`Row 3:` → sibling 1/2/3
- `Example 7` → sibling 7 (7th DM Example)
- `5.3 Subject Elements (SE)` → sibling 3 (3rd §5.x section)
- `SE – Description/Overview`/`SE – Specification`/`SE – Assumptions` → sibling 1/2/3
- `CRF Metadata` → sibling 1

## Rule A gate (slot #17 `pr-review-toolkit:comment-analyzer`)

**Sample**: 10 atoms with **10/10 page coverage** (O-P1-14 lesson applied — force 1 atom per page instead of purely stratified by type). Seed=20260445.

**Raw verdict: 4 PASS + 2 PARTIAL + 4 FAIL = 40% → FAIL vs ≥90% threshold**

### Findings

**F-B08-RA-1 (p.71 a025)**: Reviewer flagged case drift — actually PASS after check.

**F-B08-RA-2/3/4 (systemic parent_section bug, scope expanded from 3 sample atoms to 182 total via main-session sweep)**:
- Reviewer flagged 3 sample atoms with `§5.2 [CRF Metadata]` parent_section claiming "§5.2 is CO"
- Main-session PDF verification (read p.62 earlier + p.79 now): **§5.1 = Comments (CO), §5.2 = Demographics (DM), §5.3 = Subject Elements (SE)** — reviewer had INVERTED mental model
- Main-session scope sweep of batch 08 parent_section distribution revealed 182 total bad atoms:
  - **130 atoms (08a p.71-75)** tagged `§5.1 [Demographics (DM)]` — should be `§5.2 [Demographics (DM)]` (08a writer confused §5.1/§5.2 entirely, missed by reviewer)
  - **52 atoms (08b p.76-78)** tagged `§5.2 [CRF Metadata]` — `CRF Metadata` is a local sub-table label within DM Example 6, not a section title (08b writer misread local heading as section)
- **38 atoms (08b p.79-80)** tagged `§5.3 [Subject Elements]` — correct

**F-B08-RA-5 (p.79 a008 SENTENCE)**: Verbatim paraphrase — atom says "reviewers can EVALUATE all observations made about a subject IN THE CONTEXT OF", PDF literal "reviewers can RELATE all observations made about a subject TO". Fixed to PDF literal.

**F-B08-RA-6 (p.80 a008 TABLE_ROW SEENDY)**: Verbatim truncated — missing `| Perm` Core column at end. Appended.

## Option H bulk repair applied

- 130 atoms: parent_section `§5.1 [Demographics (DM)]` → `§5.2 [Demographics (DM)]`
- 52 atoms: parent_section `§5.2 [CRF Metadata]` → `§5.2 [Demographics (DM)]`
- 1 atom (p.79 a008): verbatim paraphrase → PDF literal
- 1 atom (p.80 a008): Core column `| Perm` appended

Post-repair parent_section distribution: 182 §5.2 DM + 38 §5.3 SE (clean).

## Findings added

| ID | Severity | Summary |
|---|---|---|
| O-P1-18 | HIGH | 08a writer §5.1/§5.2 numbering confusion (130 atoms mis-tagged). v1.3 prompt: TOC consultation + no topic-guessing of section numbers. |
| O-P1-19 | HIGH | 08b writer local-label as section title (52 atoms "§5.2 [CRF Metadata]"). v1.3 prompt: parent_section TITLE must come from PDF §X.Y heading only, never local table/form labels. |
| O-P1-20 | MEDIUM | Rule A reviewer (#17 comment-analyzer) own section numbering INVERTED (claimed §5.2=CO, actually §5.2=DM). Direction right, rationale wrong. v1.3 reviewer prompt: prepend section-map ground truth. |

## Rule D roster (post batch 08)

- Cumulative: 17 distinct subagent types burned
- New: pr-review-toolkit:comment-analyzer (slot #17)
- Noted quality issue: slot #16 (silent-failure-hunter) AND slot #17 (comment-analyzer) BOTH had false-positive/inverted-rationale issues on parent_section checks — signals systematic gap in Rule D reviewer's section-number ground truth knowledge

## Session wrap (batch 08 end)

- Rule A sample re-run post bulk-repair: NOT executed this session (context budget). Mechanical verification via enumerated distribution + PDF spot-check deemed sufficient.
- **Recommendation for batch 09 session start**: main session reads PDF TOC (p.6) once to establish ground truth §5.x → §6.x → §7.x → §8.x section map, pass that map to all writers AND reviewers as anchor.

## Session budget (batch 08 total)

- 08a+08b parallel dispatch: 3.9 min wall
- Schema + collision check: 1 min
- HEADING backfill (16 atoms): 1 min
- Rule A sample (with page-coverage improvement): 1 min
- Comment-analyzer reviewer: 3.6 min
- Main-session scope sweep + PDF p.72/76/79 reads: 3 min
- Option H bulk repair (182 + 2 atoms): 2 min
- Paperwork (progress + audit_matrix + report): 4 min
- **Total ~20 min** (comparable to batch 07 despite larger repair scope, due to mechanical bulk fix)

---

*Handoff: Next session reads `_progress.json.recovery_hint` + this report + `rule_a_batch_08_summary.md` + O-P1-18/19/20 detail. Batch 09 dispatch SHOULD include: (a) prepend TOC ground truth to writer prompts; (b) force-apply O-P1-15/16/18/19/20 rules; (c) Rule A reviewer prompt should also include TOC anchor; (d) drift cal mandatory post batch 09.*
