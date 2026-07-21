# Rule A Audit Summary — P2 B-03c Round 06 batch_75 (NV/examples.md)

> Date: 2026-05-06
> Batch: batch_75
> Source: `knowledge_base/domains/NV/examples.md` (87 lines)
> Writer JSONL: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_75_md_atoms.jsonl` (61 atoms)
> Writer subagent_type: `general-purpose`
> Reviewer subagent_type: `pr-review-toolkit:code-reviewer` (Rule D distinct from writer ✓)
> Reviewer prompt: `subagent_prompts/P0_reviewer_v1.9.1.md`
> Sample size: 11 verdicts (8 boundary + 3 stratified per B-02 R-B02-3 standard for batches ≥30 atoms)

## Verdict

**PASS — 11/11 = 100% strict PASS · 0 HIGH · 0 MEDIUM · 0 LOW · 0 schema regression**

## Stats

- atom count: 61 (writer) — within kickoff §0.5 row 9 / §4 halt range [22, 111] for batch_75 NV/ex (87L × 0.701 ratio = 61 atoms; aligns round 05 trend 0.761 and round 06 OE/ass+OI/ex baseline)
- atoms/line ratio: 61/87 = **0.701** (round 06 trend tracking: post round 05 0.761; +0.06 down vs round 05 mid)
- atom_type breakdown: HEADING=3 (1 H1 + 2 H2) · SENTENCE=24 (incl. 15 bold-caption per §R-D5) · TABLE_HEADER=4 · TABLE_ROW=30
- LIST_ITEM=0 / NOTE=0 / FIGURE=0 / CODE_BLOCK=0 / CROSS_REF=0 (all consistent with kickoff §0.5 row 14 grep 0 mermaid + §2.7 NO trigger 0 numberless H2)

## Schema regression check (R-2.8-1/2/3 + v1.9.1 §D-* + Hook C-8)

| Invariant | Status | Evidence |
|---|---|---|
| 12-key schema v1.2.1 (verbatim NOT verbatim_text; figure_ref present) | PASS | All 61 atoms 12-key schema ✓ |
| atom_type valid 9-enum | PASS | HEADING/SENTENCE/TABLE_HEADER/TABLE_ROW only — no H1/H2 strings |
| atom_id sequential `md_dmNV_ex_a001..a061` | PASS | 61 atoms continuous |
| Hook C-8 file prefix `knowledge_base/` | PASS | All 61 atoms ✓ |
| R-2.8-1 H1 sib=1 universal | PASS | a001 sib=1 ✓ |
| R-2.8-2 TABLE_HEADER sib=null + span=1 | PASS | 4/4 TABLE_HEADER (a009/a018/a032/a050) line_end-line_start=1 sib=null ✓ |
| R-2.8-3 extracted_by object schema | PASS | All 61 atoms `{subagent_type, prompt_version, ts}` object ✓ |
| SENTENCE/TABLE_ROW hl+sib explicit null (round 03 lock + round 05 MED-01) | PASS | 24/24 SENTENCE + 30/30 TABLE_ROW explicit null ✓ |
| §R-D5 bold-caption SENTENCE accept (15 instances: L9-11/13/26/41-44/46/67-70/72) | PASS | All 15 bold-caption SENTENCE NOT mis-typed as HEADING/NOTE ✓ |
| §2.5 H2 self-namespace `§<D>.N [Example N]` | PASS | a002 H2 Ex1 → root §NV; a041 H2 Ex2 → root §NV (H2 stay at root per §2.5); a003-a040 children → §NV.1; a042-a061 children → §NV.2 ✓ |

## Per-atom audit (11 verdicts)

| # | atom_id | role | line | type | verdict |
|---|---|---|---|---|---|
| 1 | a001 | boundary_H1 | L1 | HEADING h_lvl=1 sib=1 | PASS |
| 2 | a002 | boundary_H2_Ex1 | L3 | HEADING h_lvl=2 sib=1 | PASS |
| 3 | a005 | boundary_bold_caption_SENTENCE | L9 | SENTENCE | PASS |
| 4 | a009 | boundary_first_TABLE_HEADER | L15-16 | TABLE_HEADER span=1 sib=null | PASS |
| 5 | a010 | boundary_first_TABLE_ROW_post_H2 | L17 | TABLE_ROW | PASS |
| 6 | a025 | boundary_L37_cross_ref_rich_SENTENCE | L37 | SENTENCE cross_refs=PR/AG/DU | PASS |
| 7 | a041 | boundary_H2_Ex2 | L59 | HEADING h_lvl=2 sib=2 | PASS |
| 8 | a061 | boundary_final_SENTENCE | L87 | SENTENCE cross_refs=DI/DO/DU | PASS |
| 9 | a042 | stratified_plain_SENTENCE_Ex2 | L61 | SENTENCE | PASS |
| 10 | a055 | stratified_TABLE_ROW_Ex2_INTP | L80 | TABLE_ROW (multi-empty cells) | PASS |
| 11 | a026 | stratified_cross_ref_bearing | L39 | SENTENCE cross_refs=DU | PASS |

## Byte-exact verbatim sweep (full 61, beyond required 11)

Independent Python reconstruction `'\n'.join(src_lines[ls-1:le])` vs `verbatim` field for all 61 atoms = **0 mismatches**. Confirms:
- Em-dash U+2014 preserved (a001 H1 / a025 L37 / a042 L61 x2)
- Bold markers `**...**` preserved (15 bold-caption SENTENCE)
- Pipe-separated table cells preserved including multi-empty cells (a055 INTP row 6 empty cells)
- Double-quotes `"EEG"` / `"VISUAL EVOKED POTENTIAL"` / `"INTP"` preserved (a042 L61, a043 L63)
- Double-hyphen `--LNKID` / `--REFID` / `--REFID` preserved (a025 L37, a026 L39)
- Parenthetical references `(see SDTMIG-MD, Device-in-Use (DU) domain assumptions)` preserved (a026)

## Kickoff drift verification (§R-D1)

Writer report flag: no `kickoff_doc_drift_detected` flag in batch report. Independent grep confirms:
- Source 87L matches kickoff §0.5 row 9 row 75-NV/ex line count claim
- 0 numberless H2 in NV/ex (kickoff §0.5 row 13 grep 实证 ✓)
- 0 mermaid in NV/ex (kickoff §0.5 row 14 grep 实证 ✓)
- atom estimate range [44, 74] kickoff §1; halt range [22, 111] §4 row #8; actual 61 within both ✓

No kickoff drift, no writer fabrication. Writer Rule-B preserved source byte-exact.

## Findings

None.

## Hooks invoked

R-2.8-1 / R-2.8-2 / R-2.8-3 / Hook A1 / Hook C-8 / §R-D1 / §R-D5 / §R-D7.3 / §R-D7.6 / §2.5 / §2.9 / schema v1.2.1

## audit_matrix row (pre-formatted, append to `.work/06_deep_verification/audit_matrix.md`)

```
| batch_75 | 2026-05-06 | NV/examples.md | 87 | 61 | 0.701 | 3H/24S/4TH/30TR (15 bold-caption S per §R-D5) | general-purpose | pr-review-toolkit:code-reviewer | 11/11=100% | R-2.8-1/2/3 + Hook C-8 + §R-D5 + 12-key schema all PASS | 0 findings | PASS |
```

## Halt-gate evaluation

- < 90% PASS? No (100%)
- HIGH severity? No
- R-2.8 violation? No (R-2.8-1/2/3 all PASS)
- MED-01 (LIST_ITEM hl+sib explicit null)? No (0 LIST_ITEM in batch — N/A)
- Schema regression (verbatim_text / missing figure_ref / H1-H2 strings)? No

**Decision: GREEN — proceed to next batch (batch_76 OE/assumptions.md).**

---

*Reviewer: pr-review-toolkit:code-reviewer (Rule D distinct from writer general-purpose ✓). Hooks: 26 v1.9.1 hooks evaluated, 12 invoked, 0 violations. Audit reproducible via `.work/06_deep_verification/evidence/checkpoints/rule_a_P2_B-03_batch_75_verdicts.jsonl`.*
