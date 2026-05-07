# Rule A + Rule D Reviewer Summary — P2 B-03c Round 11 batch_114

> 创建: 2026-05-07
> Reviewer subagent: `pr-review-toolkit:code-reviewer` (Rule D 隔离 — writer = `general-purpose`, 不同 subagent_type ✓)
> Prompt baseline: `subagent_prompts/P0_reviewer_v1.9.3.md` (35 hooks v1.9.3 active)
> Source: `knowledge_base/domains/SU/assumptions.md` (20 lines)
> Checkpoint: `evidence/checkpoints/P2_B-03_batch_114_md_atoms.jsonl` (15 atoms)
> Audit verdict: **FAIL** — HIGH severity systematic verbatim regression (9/14 LIST_ITEMs)

---

## 1. Audit verdict — FAIL (HALT recommended)

| Metric | Result |
|---|---|
| Rule A sample size | **15/15 atoms full-coverage audited** (small batch — exhaustive) |
| Rule A pass rate | **6/15 = 40.0%** ❌ (≥90% required for PASS) |
| HIGH severity findings | **9** (systematic verbatim byte-exact mutation) |
| MED severity findings | 0 |
| LOW / INFO findings | 1 (§F-3 estimate calibration carry-forward) |
| Schema regression sweep (R-E1) | PASS (0 schema violations) |
| Halt recommendation | **YES — HALT per kickoff §4 halt #2 + #3** |

---

## 2. CRITICAL FINDING — Systematic indented sub-bullet whitespace strip (Rule A)

**Class**: VERBATIM_BYTE_EXACT_MISMATCH on indented sub-bullet LIST_ITEMs (a./b./c. nested under numbered top-level items).

**Affected atoms** (9 of 14 LIST_ITEMs):

| atom_id | line | source (3-space indent) | atom verbatim (stripped) |
|---|---|---|---|
| a003 | L4 | `   a. In many clinical trials...` | `a. In many clinical trials...` |
| a004 | L5 | `   b. SU may contain responses...` | `b. SU may contain responses...` |
| a006 | L8 | `   a. SUTRT captures the verbatim...` | `a. SUTRT captures the verbatim...` |
| a007 | L9 | `   b. SUMODIFY is a permissible...` | `b. SUMODIFY is a permissible...` |
| a008 | L10 | `   c. SUDECOD is the preferred...` | `c. SUDECOD is the preferred...` |
| a010 | L13 | `   a. SUCAT and SUSCAT...` | `a. SUCAT and SUSCAT...` |
| a011 | L14 | `   b. SUGRPID may be used...` | `b. SUGRPID may be used...` |
| a013 | L17 | `   a. SUSTDTC and SUENDTC...` | `a. SUSTDTC and SUENDTC...` |
| a014 | L18 | `   b. If substance use information...` | `b. If substance use information...` |

All 9 atoms drop the **3 leading spaces** present in the source. Each atom's stated `line_start = line_end` for that line, so verbatim must equal the line byte-for-byte.

**Counter-evidence — established convention preserved indent across 9112 prior atoms**:

A statistical sweep across `md_atoms.jsonl` for indented sub-bullet LIST_ITEMs (source line starts with leading whitespace + `[a-z0-9]+\. ` pattern, single-line atoms):

- **279 atoms PASS** (verbatim preserves 3-space leading indent — examples: `md_ch04_a228..a230` in `chapters/ch04_general_assumptions.md` L327/329/331; identical structural pattern as SU/ass).
- **9 atoms FAIL** — **all 9 are in batch_114** (this batch). 0 pre-existing whitespace-strip atoms in 9112 prior production atoms.

Conclusion: this is a **NEW regression** introduced by writer `general-purpose` for batch_114, contradicting the established byte-exact convention validated across 9 cumulative B-03c rounds + B-01/B-02. The writer's DONE report self-validation `§E-1..E-6: PASS` and `30/30 hooks PASS` did not catch the verbatim mismatch — Hook A1 / Hook 22 verbatim byte-exact verification was bypassed.

**Severity**: HIGH per v1.9.3 §R-E1 escalation (verbatim mismatch class — round 04 v1.6 INFO-1 lessons referenced in audit prompt; reviewer hook priority "HALT priority ≥ verbatim mismatch").

**Halt trigger**: kickoff §4 halt #2 (Rule A audit < 90% PASS rate AND HIGH severity finding) AND #3 (schema-adjacent regression on verbatim convention).

---

## 3. Other hook results — all PASS

| Hook | Status | Note |
|---|---|---|
| **R-E1** Schema regression sweep PRIORITY 1 | **PASS** | 15/15 atoms have all 12 fields in correct order; atom_type ∈ 9-enum (1 HEADING + 14 LIST_ITEM); extracted_by is object with subagent_type+prompt_version+ts |
| **R-E2** R-2.8-1 H1 sib=1 | **PASS** | a001 atom_type=HEADING heading_level=1 sibling_index=1 |
| **R-E3** R-2.8-2 TABLE_HEADER sib=null | **N/A** | 0 TABLE_HEADER (per kickoff §0.5 row 12: 0 H2, table-free file) |
| **R-E4** R-2.8-3 extracted_by object schema | **PASS** | 15/15 — `{"subagent_type":"general-purpose","prompt_version":"P0_writer_md_v1.9.3","ts":"2026-05-07T13:00:00Z"}` uniform |
| **R-E5** MED-01 non-HEADING explicit null | **PASS** | 14/14 LIST_ITEMs have explicit `"heading_level":null,"sibling_index":null` (NOT missing) |
| **R-E6** FIGURE-vs-CODE_LITERAL boundary | **N/A** | 0 FIGURE / 0 CODE_LITERAL in batch |
| **R-F-1 HIGH** §2.11 Plan B sub-namespace | **N/A trigger PASS** | 0 numberless H2 with H3 children in source (per kickoff §0.5 row 12 grep-verified 0 H2). All 15 atoms use file-root `§SU [SU — Assumptions]` parent_section uniformly ✓; 0 sub-namespace mis-application. Backward compat preserved. |
| **R-F-2 INFO** atoms/line ratio retrospective | **INFO IN BAND** | 15/20 = **0.750** within empirical band 0.59-0.85 (10th sustained validation cycle). Independent of verbatim issue. |
| **R-F-3 INFO** kickoff estimate calibration | **INFO ABOVE THRESHOLD** | kickoff est range 7-12 (mid 9.5); actual 15; delta_pct **+57.9%** (above ±50% threshold). Carry-forward as INFO finding for round-close mini-audit. Driver: writer treated each indented sub-bullet (a/b/c) as separate LIST_ITEM atom (same atomic-distinct pattern as RS/ass batch_98 round 09 §F-3 counter-example). NOT a §F-3 compression case; estimate was too low because kickoff §1 used 0.4-0.6× ratio while actual content was atomic-distinct sub-bullets at ~0.75 ratio. |
| atom_id uniqueness + sequential | **PASS** | a001..a015 all distinct, sequential, no gaps |
| parent_section consistency | **PASS** | 15/15 = `§SU [SU — Assumptions]` (file-root, 0 H2 source) |
| **LIST_ITEM Hook A3 full-prefix** | **CONDITIONAL** | List prefix (`1. `, `a. `) preserved in all 14 LIST_ITEMs ✓, BUT **leading whitespace before prefix stripped in 9 indented atoms** (a003/a004/a006/a007/a008/a010/a011/a013/a014) — see §2 above. Hook A3 prefix-only check passed, but byte-exact verbatim (Hook A1 / Hook 22) failed. |
| Rule D writer ≠ reviewer subagent_type | **PASS** | writer=`general-purpose`, reviewer=`pr-review-toolkit:code-reviewer` ✓ |
| 35/35 hooks | **34 PASS / 1 FAIL** (Hook A1 verbatim byte-exact via 9 atoms) |

---

## 4. Recommendation

**HALT** dispatch order at step 2 (post batch_114 reviewer). Per kickoff §4 halt #2 + #3, do NOT proceed to batch_115 writer until:

1. **Root-cause investigation**: writer's `general-purpose` instance applied unprompted whitespace normalization to indented sub-bullets only. This pattern is novel — 279 prior production atoms preserved indent. Hypotheses:
   - Writer mis-interpreted "verbatim" as "trimmed text content" for nested list items (vs prior batches where writer kept indent intact)
   - Writer prompt v1.9.3 may benefit from explicit reinforcement of "preserve ALL leading whitespace including indented sub-bullet 3-space prefix" in §A1 / Hook A1 section
2. **Decision**: orchestrator chooses between:
   - **Option (a) Re-dispatch batch_114 writer** with explicit reinforcement prompt (preferred per round 06 batch_72 4-schema-regression precedent — root-revert + re-dispatch RESOLVED)
   - **Option (b) Post-hoc fix the 9 atoms** to add back `   ` (3-space) leading indent (deviates from "no post-hoc fix" round 09/10 invariant; not recommended)
3. **Backward audit**: did rounds 09-10 produce any whitespace-stripped atoms that escaped reviewer detection? Sweep shows 0 such cases pre-batch_114; regression is isolated to this batch.
4. **Cross-batch implication**: rounds 11 batches 116/118 (SUPPQUAL/ass + SV/ass) have similar nested sub-bullet structure (per kickoff §0.5 verify rows 14, 16). Re-dispatched writer prompt should be applied to ALL remaining round 11 batches, not just batch_114.

**Per audit prompt explicit instruction**: "If you find any HIGH severity issue, halt and emit HALT report instead with details. Do not attempt to fix yourself — write findings only and let orchestrator decide."

---

## 5. Cross-references

- v1.9.3 §R-E1 CRITICAL Schema regression sweep PRIORITY 1 — invoked, found 0 schema regression but caught downstream verbatim regression
- Round 04 v1.6 INFO-1 whitespace mutation lesson (referenced in audit prompt §10) — directly applicable; this batch is a recurrence
- Round 06 batch_72 4-schema-regression precedent — root-revert + re-dispatch resolution model
- Round 09 RS/ass batch_98 §F-3 counter-example (atomic-distinct sub-bullets, 0.655 ratio) — confirms ratio 0.75 here is normal for atomic-distinct content; ratio NOT the issue
- 279 prior production atoms (e.g., `md_ch04_a228..a230`) — counter-evidence proving convention preserves indent

---

**End of summary.**
