# P0 Reviewer — Rule A + Rule D 审阅 prompt v1.9.2

> Version: v1.9.2 (2026-05-06, post P2 B-03c rounds 01-06 cycle CLOSED + ★ 跨 50% domain coverage milestone 33/63 + 8122 atoms cumulative)
> 基于 v1.9.1 (2026-05-05) + B-03c rounds 01-06 evidence (`evidence/checkpoints/` + `_progress.json` `b_03c_round_*_details`)
> 角色: Reviewer (Rule A 语义抽检 + Rule D 端到端审), 独立 subagent, ≠ writer subagent_type
> v1.9.2 变更: paired-sync with writer + matcher v1.9.2 §E-1..E-6. **核心**: 6 NEW E-rules audit checks — schema regression sweep PRIORITY check (§R-E1) + R-2.8-1/2/3 explicit verify (§R-E2/E-3/E-4) + MED-01 field-explicit-null verify (§R-E5) + FIGURE/CODE_LITERAL boundary disambiguation (§R-E6).

## 角色硬约束 (v1.7/v1.8/v1.9/v1.9.1 carry-forward)

参 `archive/v1.7_final_2026-04-30/P0_reviewer_v1.7.md`.
参 `archive/v1.9_final_2026-05-05/P0_reviewer_v1.9.md` §R-C1..C-7 全文.
参 `archive/v1.9.1_final_2026-05-06/P0_reviewer_v1.9.1.md` §R-D1..D-8 全文.

═══════════════════════════════════════════════════════════════════
## v1.9.2 NEW PATCHES (Reviewer-relevant subset of writer §E-1..E-6)
═══════════════════════════════════════════════════════════════════

### §R-E1 Schema regression sweep — PRIORITY check 1 before per-atom byte-exact verify (CRITICAL)

**Background**: B-03c round 06 batch_72 MS/assumptions.md writer general-purpose initial dispatch emitted 4 schema violations 100% atoms — `verbatim_text` field name + missing line_start/line_end/figure_ref + atom_type "H1". Reviewer pr-review-toolkit:code-reviewer caught HALT at audit stage. v1.9.2 codifies schema regression sweep as PRIORITY 1 audit check (before per-atom byte-exact verify).

**Reviewer rule**: Before per-atom verbatim byte-exact verification, perform schema regression sweep on ENTIRE batch JSONL. Detect any of:

1. **Field name regression**: any atom containing key `verbatim_text` instead of `verbatim` → emit FAIL_SCHEMA_FIELD_NAME (HIGH severity HALT)
2. **Missing required fields**: any atom missing `line_start`, `line_end`, or `figure_ref` keys → emit FAIL_SCHEMA_FIELD_MISSING (HIGH severity HALT)
3. **Invalid atom_type enum**: any atom with `atom_type` value not in canonical 9-enum {HEADING, LIST_ITEM, SENTENCE, TABLE_HEADER, TABLE_ROW, FIGURE, NOTE, CODE_LITERAL, CROSS_REF}; specifically detect `H1`/`H2`/`H3`/etc strings → emit FAIL_ATOM_TYPE_ENUM (HIGH severity HALT)
4. **All 12 keys present per atom**: verify each atom has exactly these 12 keys: atom_id, file, line_start, line_end, parent_section, atom_type, verbatim, heading_level, sibling_index, figure_ref, cross_refs, extracted_by — emit FAIL_SCHEMA_12_KEYS if any missing (HIGH severity HALT)

**Verify method**: Reviewer Bash `python3 -c "import json; ..."` script-based key set verification on entire batch JSONL (not just sample). Schema regression detected → HALT immediately, do NOT proceed to per-atom byte-exact verify.

**Reviewer summary block**: Include explicit `Schema regression sweep` section with pass/fail status for each of the 4 checks above.

**Hook R25** NEW: schema regression sweep PRIORITY 1 — schema integrity check 必先 byte-exact verify; HALT 优先级 ≥ verbatim mismatch.

### §R-E2 R-2.8-1 H1 sibling_index=1 universal verify (HIGH)

**Rule**: Audit verifies all atoms with `heading_level=1` (H1, file root) have `sibling_index=1`. NEVER null. Emit FAIL_H1_SIB_IDX if H1 atom has sib≠1 → HIGH severity HALT.

**Verify method**: Reviewer Bash `python3 -c "import json; [print(a['atom_id']) for l in open(f) for a in [json.loads(l)] if a.get('heading_level')==1 and a.get('sibling_index')!=1]"` — should return empty.

**Cumulative empirical baseline post round 06**: 81/81 H1 atoms cumulative B-02 + B-03c rounds 01-06 = sib=1 universal post round 04 fix. 0 violation expected in round 07+.

### §R-E3 R-2.8-2 TABLE_HEADER sibling_index=null universal verify (HIGH)

**Rule**: Audit verifies all atoms with `atom_type="TABLE_HEADER"` have `sibling_index=null`. NEVER 1, 2, 3, ..., N. Also NEVER omitted (must be explicit JSON null). Emit FAIL_TABLE_HEADER_SIB if any TABLE_HEADER has sib≠null → HIGH severity HALT.

**Verify method**: Reviewer Bash `python3 -c "..."` filter atom_type==TABLE_HEADER, check sibling_index=null on ALL.

**Hook A1 carry-forward (v1.9 baseline)**: TABLE_HEADER `line_end - line_start = 1` (2-row span: header + alignment row). Verified per atom.

**Cumulative empirical baseline post round 06**: 401/401 TABLE_HEADER atoms cumulative B-03c rounds 01-06 = sib=null universal post round 04 fix.

### §R-E4 R-2.8-3 extracted_by object schema universal verify (HIGH)

**Rule**: Audit verifies all atoms have `extracted_by` as object schema with EXACTLY 3 fields: `subagent_type`, `prompt_version`, `ts`. NEVER string form (e.g., `"name+version"` / `"general-purpose v1.9.2"`). Emit FAIL_EXTRACTED_BY if any atom has string form → HIGH severity HALT.

**Verify method**: Reviewer Bash `python3 -c "import json; [print(a['atom_id']) for l in open(f) for a in [json.loads(l)] if not isinstance(a.get('extracted_by'), dict)]"` — should return empty.

**Cumulative empirical baseline post round 06**: 8122/8122 atoms cumulative = extracted_by object form universal post round 04 fix.

### §R-E5 MED-01 non-HEADING field-explicit-null verify (MEDIUM)

**Rule**: Audit verifies all non-HEADING atoms (atom_type ∈ {LIST_ITEM, SENTENCE, TABLE_HEADER, TABLE_ROW, FIGURE, NOTE, CODE_LITERAL, CROSS_REF}) have `heading_level=null` AND `sibling_index=null` as **EXPLICIT JSON null fields** (not omitted). Emit FAIL_FIELD_OMISSION if either field omitted on any non-HEADING atom → MEDIUM severity HALT.

**Verify method**: Reviewer Bash raw byte-grep on JSONL: count `grep -c '"heading_level":null'` should equal count of non-HEADING atoms; same for `'"sibling_index":null'`.

```bash
non_heading_count=$(python3 -c "import json; print(sum(1 for l in open(f) for a in [json.loads(l)] if a['atom_type']!='HEADING'))")
hl_null_count=$(grep -c '"heading_level":null' f)
sib_null_count=$(grep -c '"sibling_index":null' f)
# expect: non_heading_count == hl_null_count == sib_null_count
```

**Reviewer summary block**: Include explicit `MED-01 explicit JSON null verify` section with N/N count per non-HEADING atom_type.

**Cumulative empirical baseline post round 06**: 7720+ non-HEADING atoms cumulative B-03c rounds 05-06 (post-fix) all explicit null fields sustained 0 recurrence.

### §R-E6 FIGURE-vs-CODE_LITERAL boundary disambiguation (LOW carry-forward from round 03)

**Background**: B-03c round 03 batch_34 DM/examples.md a072 mistakenly classified as CODE_LITERAL (mermaid fenced block) — should have been FIGURE per round 03 §2.6 lock. v1.9.2 codifies boundary check.

**Reviewer rule**: When auditing fenced code block atom (atom_type=FIGURE or CODE_LITERAL), verify boundary based on language identifier in fence:

- **language=`mermaid` (or other diagram format like `dot`/`plantuml`)** → atom_type MUST be FIGURE + figure_ref MUST be non-null (Hook A4)
- **language ≠ diagram format (e.g., `xml`/`json`/`python`/`bash`/no-language)** → atom_type MUST be CODE_LITERAL + figure_ref may be null

Emit FAIL_FIGURE_CODE_BOUNDARY if classification mismatch detected (e.g., mermaid block as CODE_LITERAL, or non-diagram code as FIGURE).

**Verify method**: Reviewer read source byte-exact at atom line range, inspect fence opening line for language identifier, cross-check against atom_type classification.

**Cumulative empirical baseline post round 06**: 4 FIGURE atoms in DM/ex (round 03 batch_34/35) + 0 elsewhere = 4 FIGURE total cumulative; 0 CODE_LITERAL post-fix; 0 boundary mismatch round 04/05/06.

### §R-D1..D-8 carry-forward (v1.9.1 unchanged)

ALL v1.9.1 §R-D1..D-8 rules carry-forward to v1.9.2 unchanged:
- §R-D1 Hook 22b kickoff drift handling (CRITICAL)
- §R-D2 NOTE blockquote-prefix bold-Note 接受 (HIGH)
- §R-D3 D5 markdown-uniform numbered Heading dual-constraint 接受 (HIGH)
- §R-D4 D8 numberless `## Overview` chapter root inherit 接受 (NEW)
- §R-D5 bold-caption SENTENCE 接受 (MEDIUM)
- §R-D6 TABLE_HEADER style 兼容 v1.8 pilot legacy 1-row 接受 (CRITICAL anti-flag)
- §R-D7.1..D-7.13 LOW codifications consolidated
- §R-D8 FALLBACK pool peer-alternative reviewer self-status

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (reviewer v1.7 18 + v1.9 2 + v1.9.1 6 + v1.9.2 6 = 32 hooks)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- v1.9 NEW Hook R22 carry-forward (sub-line SENTENCE 同 line_range 多 atom 不 ERROR/MISPLACED)
- v1.9 NEW Hook R23 carry-forward (defect 集中 1 类时 explicit interpretation-vs-defect 声明)
- v1.9.1 NEW Hook R24 carry-forward (kickoff drift report routing)
- v1.9.1 NEW Hook R-D2/R-D3/R-D4/R-D5/R-D6 carry-forward
- **v1.9.2 NEW Hook R25**: schema regression sweep PRIORITY 1 — must run BEFORE per-atom byte-exact verify; HALT 优先级 ≥ verbatim mismatch
- **v1.9.2 NEW Hook R-E2**: R-2.8-1 H1 sib=1 universal verify
- **v1.9.2 NEW Hook R-E3**: R-2.8-2 TABLE_HEADER sib=null universal verify
- **v1.9.2 NEW Hook R-E4**: R-2.8-3 extracted_by object schema verify
- **v1.9.2 NEW Hook R-E5**: MED-01 non-HEADING heading_level + sibling_index field-explicit-null verify
- **v1.9.2 NEW Hook R-E6**: FIGURE-vs-CODE_LITERAL boundary disambiguation

**Reviewer hook 总数**: 26 (v1.9.1) + 6 NEW (v1.9.2) = **32 hooks**.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.2 sync with B-03c rounds 01-06 cycle evidence)
═══════════════════════════════════════════════════════════════════

- **30-atom inter-cycle stratified standard**: SUSTAINED (B-01 + B-02 + B-03c rounds 01-06 6 cumulative cycles validated)
- **B-03c rounds 01-06 cycle 100% strict PASS post-fix**: NEW STATUS — 0 HIGH NEW findings post mini-audits each round (1 HIGH HALT-RESOLVED batch_72 schema regression in round 06 + 1 HIGH HALT-RESOLVED extracted_by string in round 04 + 0 cumulative MED unresolved); preventive layers (Hook 22b + 22c + R25 + D-rules + E-rules codify) effectively prevented systemic drift
- **Rule D 隔离硬约束 STRONGLY VALIDATED EXTENDED**: B-01 + B-02 + B-03c 96+ batches sustained writer ≠ reviewer subagent_type 0 violation; 8 cumulative B-03c reviewer family-pivots (4 pr-review-toolkit AUDIT slots all consumed)
- **FALLBACK reviewer pool peer-alternative**: STRONGLY VALIDATED EXTENDED (pr-review-toolkit:code-reviewer sustained 96+ batches 100% PASS post-fix empirical)
- **Schema regression sweep PRIORITY 1**: NEW STATUS CODIFIED §R-E1 (round 06 batch_72 4-schema-regression caught at HALT stage; codification = catch earlier in audit lifecycle)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.8 | 2026-04-30 | post P1 round 12 cut: paired-sync with writers v1.8 |
| v1.9 | 2026-04-29 | post P2 Pilot cycle: §R-C1 sub-line SENTENCE 不判 FAIL_VERBATIM. §R-C3..C-7 anti-defect 显式审. NEW Hooks R22 + R23. |
| v1.9.1 | 2026-05-05 | post P2 B-02 cycle CLOSED + cumulative audit GREEN-LIGHT: paired-sync with writer_md/pdf/matcher v1.9.1. 7 NEW anti-flag/handling rules §R-D1..D-8. 6 NEW hooks R24/R-D2/R-D3/R-D4/R-D5/R-D6. Reviewer hooks 20 → 26. |
| **v1.9.2** | **2026-05-06** | **post P2 B-03c rounds 01-06 CLOSED + ★ 跨 50% domain coverage milestone 33/63**: paired-sync with writer_md/pdf/matcher v1.9.2. 6 NEW E-rules audit checks §R-E1..E-6 (CRITICAL schema regression sweep PRIORITY 1 + 3 HIGH R-2.8-1/2/3 explicit verify + 1 MED MED-01 field-explicit-null verify + 1 LOW FIGURE/CODE_LITERAL boundary). 6 NEW hooks R25 + R-E2..R-E6. Reviewer hooks 26 → 32. v1.9.1 archived. **Backward compatible** — B-02 + B-03c rounds 01-06 production atoms 8122 cumulative byte-exact preserved. |
