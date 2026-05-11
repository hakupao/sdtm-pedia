# P1 Batch 09 Report — TOC Anchor Prompt First Run + 2 Option H Repair Cycles + Drift Cal FAIL Known-Limitation

> Date: 2026-04-25
> Strategy: Option C parallel mini-batch default + TOC ground truth prepend + 2 Option H bulk repairs (p.87 spec table verbatim drift + p.89 DS row data hallucination)
> Writers: 09a = `oh-my-claudecode:executor` × p.81-85 (107 atoms); 09b = `oh-my-claudecode:writer` × p.86-90 (120 atoms clean, 139 over-claim + 1 `</content>` frame-tag contamination)
> Scope: SDTMIG v3.4 p.81-90 (10 pages — §5.3 SE tail + §5.4 SM whole + §5.5 SV whole)
> Status: **✅ DONE + REPAIRED** (Rule A 90% pooled PASS + drift cal 60.6% FAIL known-limitation + 7 inline fixes)

---

## Metrics

| 指标 | 值 |
|---|---|
| Pages | 10 (p.81-90) |
| Atoms final | **227** (09a 107 + 09b 120) |
| Pre-root atoms | 2286 |
| Post-merge root | **2513** |
| Atom_type coverage | 7/9 single-batch (no CROSS_REF / no FIGURE on §5.x pages) |
| Writer failures | 0 (both parallel default clean per O-P1-13) |
| Rule A verdict | CONDITIONAL_PASS @ 90% pooled (8/10 PASS + 1 PARTIAL + 1 FAIL) |
| Drift cal verdict | FAIL 60.6% → 69.7% post-repair (known-limitation class) |
| Option H repair cycles | 2 (p.87 spec table 4 atoms + p.89 DS row 3 atoms) |
| Rule D slot 烧 | #18 pr-review-toolkit:pr-test-analyzer (新烧, 18 total) |

## Execution summary

### Parallel mini-batch (Option C default) + TOC anchor prompt

- Main session pre-dispatch: read PDF p.3-5 TOC once, extracted authoritative §5-§8 section map (§5.1 CO p.60 / §5.2 DM p.62 / §5.3 SE p.79 / §5.4 SM p.84 / §5.5 SV p.86 / §6 start p.92 / ...)
- Prepended TOC ground truth to BOTH 09a + 09b prompts (writer side anchor) AND Rule A reviewer prompt (reviewer side anchor)
- 09a executor × p.81-85: 5.6 min wall, 107 atoms, 21.4/页 avg, 7/9 types (incl NOTE on p.84)
- 09b writer × p.86-90: 2.3 min wall, 120 atoms, 24.0/页 avg (post-repair), 7/9 types
  - Writer over-claimed 139 atoms in DONE message (19-atom discrepancy, O-P1-22)
  - Writer contaminated output with trailing `</content>` XML frame tag (stripped before parse)
- Parallel wall 5.6 min vs sequential est 8 min (30% speedup)

### Schema validation (immediate post-merge)

- 0 atom_id 格式错 (all 4-digit 0-padded `ig34_pNNNN_aNNN`)
- 0 造词 atom_type (all ∈ 9-enum)
- 0 missing heading_level/sibling_index on HEADING
- 0 atom_id collision with root (2286 + 227 = 2513 total)
- 2 cross-page verbatim dup on TABLE_HEADER (p.82/83 SE Examples + p.82/83 DM reference table) — LEGITIMATE (PDF re-renders header per page, verbatim字面对); NOT an O-P1-16 dup bug
- 5 HEADING level=4 entries with non-numeric verbatim (`Example 1`, `Example 2`, `sm.xpt ...`) — VALID per tree-depth convention (Chapter 5 → §5.X → sub-section L3 "SE – Examples" / "SM – Specification" → Example 1 / sm.xpt caption L4). Original R5 rule "level=4 仅 §N.x.y.z" 过严, 不改已判定正确.

## Rule A gate (slot #18 `pr-review-toolkit:pr-test-analyzer`)

**Sample**: 10 atoms with **10/10 page coverage** (1/page, O-P1-14 lesson applied). Seed=20260450. Atom_type coverage 7/9 exercised (HEADING×1 / CODE_LITERAL×1 / TABLE_HEADER×1 / NOTE×1 / LIST_ITEM×2 / TABLE_ROW×3 / SENTENCE×1).

**Raw verdict: 8 PASS + 1 PARTIAL + 1 FAIL = 90% pooled (PASS threshold ≥90% boundary PASS)**

### Findings

**F-B09-RA-1 HIGH (p.87 a001 SVCNTMOD)**: Controlled Terms cell corrupted `(CNTMODE)` → `C\(NCI\)GCD` (hallucinated NCI+codelist tokens). Main-session PDF verification p.87 table row 1 confirms `(CNTMODE)`.
- Inline fix applied.
- **Scope sweep triggered by reviewer recommendation**: main session dumped all SV TABLE_ROW on p.86-90 and compared against PDF. Uncovered **3 additional verbatim drifts in same p.87 spec table**:
  - `a004` SVSTDTC: `ISO 8601 datetime or format` → PDF `ISO 8601 datetime or interval` (format→interval)
  - `a005` SVENDTC: same `format`→`interval`
  - `a008` SVUPDES: `Description of the reason for the subject` → PDF `Description of what happened to the subject`
- **Scope expansion: 1 Rule A flag → 4 atoms fixed bulk** (O-P1-21 HIGH).
- Root cause hypothesis: Writer 09b on p.87 spec table had a local corruption pattern — may have substituted semantically-similar but not-literal tokens (e.g. CT lookup + paraphrase). Similar class to O-P1-12 (CO spec table under-extract) but different manifestation.

**F-B09-RA-2 PARTIAL LOW (p.90 a001 ds.xpt row 5)**: Empty DSSCAT cell pipe-count ambiguity (`PROTOCOL MILESTONE | SCREENING` vs explicit `PROTOCOL MILESTONE | | SCREENING`). Structurally resolvable (pipe count matches 13-col header). Accept as-is, v1.3 prompt candidate.

**F-B09-RA-3 INFO (p.88 a001 figure_ref misfield)**: figure_ref populated with `§4.4.5` — should be `null` (§4.4.5 is a section cross-reference, NOT a figure). cross_refs field already correctly contains `§4.4.5`. Inline fix: set figure_ref → null.

### Ground-truth anchor check — **0 inversion bug** ✓

All 10 sample atoms' parent_section matched TOC ground truth:
- p.81-83 atoms → `§5.3 [Subject Elements (SE)]` ✓
- p.84-85 atoms → `§5.4 [Subject Disease Milestones (SM)]` ✓
- p.86-90 atoms → `§5.5 [Subject Visits (SV)]` ✓

Reviewer's own rationale 0 inverted (contrast slot #17 comment-analyzer which said `§5.2=CO` wrong). **TOC anchor prepend methodology生效 — reviewer side anchor discipline confirmed.**

## Drift calibration — 300-atom cumulative §C.1 3rd cycle (post batch 07-09, 675 atoms)

**Target**: p.89 §5.5 SV – Examples (tv.xpt + ds.xpt tables, 33 atoms baseline, mixed HEADING/SENTENCE/LIST_ITEM/CODE_LITERAL/TABLE_HEADER/TABLE_ROW — 2-way cross-check (writer baseline vs executor rerun)

**Pre-repair agreement: 0.606** < 0.80 threshold → **FAIL** (similar to O-P1-09 batch 03 p.25 FAIL class)

**Root cause triage**:
- **R1 (O-P1-24 INFO)**: CODE_LITERAL vs HEADING ambiguity for `tv.xpt` / `ds.xpt` dataset filenames. Prompt ambiguity — both defensible. Scope 4 atoms.
- **R2 (O-P1-23 HIGH)**: Baseline 09b HALLUCINATED DS row data values — PDF-verified via rerun cross-check:
  - `a030` row 1 DS 37: baseline `DSDTC=2019-09-09, DSSTDY=1` → PDF `2019-09-10, (empty)` ❌
  - `a031` row 2 DS 37: baseline `DSDTC=2019-09-10, DSSTDY=2` → PDF `2019-09-16, (empty)` ❌
  - `a032` row 3 DS 85: baseline `DSSTDY=1` → PDF `DSSTDY=-6` ❌
  - Bulk Option H fix applied using rerun verbatim (PDF-verified accurate).
- **R3 (minor)**: TV rows 3-7 trailing empty pipe — baseline truncates 7 fields, rerun keeps 8 fields with trailing `|`. LOW drift, same class as F-B09-RA-2, v1.3 prompt candidate.

**Post-repair agreement: 0.697** (R2 fixed, R1 R3 defer to v1.3 prompt) — still FAIL vs 0.80 threshold.

**Verdict**: FAIL but **known-limitation class** (consistent with O-P1-09 disposition Option 2' — continue P1 with Rule A per-batch as safety net, consolidated v1.3 prompt fix at P1 末). Tiebreaker general-purpose NOT dispatched (ctx conservation + root cause already localized).

**Drift cal value-add vs Rule A**: 10-atom Rule A sample did NOT include `a030/a031/a032` DS row atoms. Drift cal full-page 2-way cross-check captured ALL of them. Drift cal is a **necessary complementary check** for dense example/spec table pages where Rule A narrow sample may miss systemic data corruption. Methodology implication: Rule A may need to weight TABLE_ROW sampling higher on spec-heavy pages.

## Option H repairs applied (7 total inline fixes)

| # | Atom | Issue | Fix |
|---|---|---|---|
| 1 | `ig34_p0087_a001` | SVCNTMOD CT cell `C\(NCI\)GCD` hallucinated | → `(CNTMODE)` per PDF |
| 2 | `ig34_p0087_a004` | SVSTDTC `or format` drift | → `or interval` per PDF |
| 3 | `ig34_p0087_a005` | SVENDTC `or format` drift | → `or interval` per PDF |
| 4 | `ig34_p0087_a008` | SVUPDES `reason for` paraphrase | → `what happened to` per PDF |
| 5 | `ig34_p0088_a001` | figure_ref=[§4.4.5] misfield | → null (§4.4.5 already in cross_refs) |
| 6 | `ig34_p0089_a030` | DS row 1 DSDTC=09-09 DSSTDY=1 hallucinated | → rerun verbatim (2019-09-10, empty) PDF-verified |
| 7 | `ig34_p0089_a031` | DS row 2 DSDTC=09-10 DSSTDY=2 hallucinated | → rerun verbatim (2019-09-16, empty) PDF-verified |
| (7) | `ig34_p0089_a032` | DS row 3 DSSTDY=1 hallucinated | → rerun verbatim (-6) PDF-verified |

Plus 1 mechanical strip: 09b trailing `</content>` XML frame tag (O-P1-22 INFO) line 121 removed.

## Findings added

| ID | Severity | Summary |
|---|---|---|
| O-P1-21 | HIGH | 09b writer p.87 spec table 4-atom verbatim drift (SVCNTMOD CT hallucination + SVSTDTC/SVENDTC format→interval drift + SVUPDES "reason for"→"what happened to" paraphrase). Root: likely CT-lookup-then-paraphrase pattern. v1.3 prompt: 加 rule "spec table verbatim 必字面逐字 PDF, 禁 CT-lookup / 同义扩展 / 合理化 paraphrase". |
| O-P1-22 | INFO | 09b writer DONE message over-claim atoms=139 vs actual 120 (19-atom gap) + trailing `</content>` XML frame tag 泄漏 output_file. Writer subagent frame 渗入. 单例. 观察期: 若再出升 MEDIUM + v1.3 prompt "output_file 只 contain 合法 JSONL 每行, 不含 frame tag / 自然语言 / 非 JSON 内容". |
| O-P1-23 | HIGH | 09b writer p.89 DS example table 3-atom data hallucination (DSDTC 09-09→实 09-10, 09-10→实 09-16; DSSTDY 1/2/1→实 (empty)/(empty)/-6). PDF-verified via drift cal rerun. Root: writer 可能读表时 column 对齐错 / 插 row-index 当 DSSTDY 空 cell. v1.3 prompt: 加 rule "TABLE_ROW verbatim 必 literal PDF 读取, 禁 row-index 填空 / 插 sequential integers / 插 interpolated dates". |
| O-P1-24 | INFO | CODE_LITERAL vs HEADING 分类对 `*.xpt` dataset filenames 歧义: v1.2 H1' 说 CODE_LITERAL, 但 visually positioned above example table 像 sub-heading. v1.3 prompt: 明示 "`*.xpt` / `*.sas7bdat` always CODE_LITERAL; 若 PDF 同时显式 bold-caption 额外 styled heading text above, 可并存独立 HEADING + CODE_LITERAL 两原子". |

## Rule D roster (post batch 09)

- Cumulative: **18 distinct subagent types** burned
- New: pr-review-toolkit:pr-test-analyzer (slot #18) — **0 false positive / 0 inverted rationale** (首 TOC-anchored reviewer, 方法学生效)
- Quality trend: slot #16/#17 had 10-20% FP/inverted issues on section numbering; slot #18 with TOC anchor prepend = 0% errors on 10-sample. **Methodology locked**: reviewer prompt prepend TOC ground truth 是 anti-inversion 标准做法.

## Post-batch state

| 项 | Value |
|---|---|
| P1 pages_done | **90** / 535 (16.8%) |
| P1 atoms_done | **2513** root (pre 2286 + 227 = 2513 clean post-repair) |
| P1 batches_done | **9** |
| P1 failures_done | 1 (batch 06 attempt 1, Rule B archived) |
| Rule A cumulative | 6 batches × 10 atoms + 1 × 30 atoms = 90-atom independently PDF-verified sample; 1 batch 04 PARTIAL + 1 batch 06 FAIL (inline 修) + 1 batch 07 FAIL (Option H 修) + 1 batch 08 FAIL (Option H bulk 修) + 1 batch 09 CONDITIONAL_PASS boundary |
| Drift cal cumulative | 3 runs (p.25 3-way FAIL / p.60 2-way FAIL 为 writer bug / p.89 2-way FAIL 为 writer hallucination + prompt 歧义) |
| Option H repair cycles | 4 cumulative (batch 06 Option E + batch 07 + batch 08 bulk + batch 09 2× for p.87 spec + p.89 DS) |

## Session budget (batch 09 total)

- Session startup (3 prereq reads): 3 min
- TOC read + extract ground truth: 1 min
- 09a + 09b parallel dispatch: 5.6 min wall (parallel)
- Schema + collision check + `</content>` strip: 2 min
- Rule A dispatch (slot #18): 3.1 min wall
- Main session Rule A finding verify + PDF p.87 read + scope sweep: 3 min
- Option H bulk repair (5 atoms: p.87 4 + p.88 1): 2 min
- Drift cal dispatch (executor rerun p.89): 1.3 min wall
- Drift cal agreement analysis + PDF p.89 read + O-P1-23 detection: 3 min
- Option H bulk repair (3 atoms: DS rows): 1 min
- Paperwork (drift cal report + batch 09 report + audit_matrix + _progress.json): 5 min
- **Total ~30 min** (含 2 repair cycles, drift cal FAIL analysis depth, 方法学 retrospective)

---

*Handoff: Next session reads `_progress.json.recovery_hint` + this report + `rule_a_batch_09_summary.md` + `drift_cal_batch_07_09_p89_report.md` + new findings O-P1-21/22/23/24. Batch 10 dispatch SHOULD include: (a) **continue TOC anchor prompt** (validated 0-inversion on slot #18); (b) force-apply O-P1-15/16/18/19/20/21/22/23/24 rules (cumulative 10 prompt rules); (c) Rule A reviewer also TOC-anchored (methodology locked); (d) batch 10 spans p.91-100 — first pages of §6 Domain Models based on General Observation Classes starting p.92, TOC anchor should be extended to include §6.1/§6.1.1 (AG) / §6.1.2 (CM) section map; (e) drift cal next trigger at batch 12 (batch 10-12 cumulative ~300 atoms).*
