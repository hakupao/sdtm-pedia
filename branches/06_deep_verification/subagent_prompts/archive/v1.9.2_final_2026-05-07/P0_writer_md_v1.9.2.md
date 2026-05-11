# P0 Writer MD — 原子化 prompt v1.9.2

> Version: v1.9.2 (2026-05-06, post P2 B-03c round 06 CLOSED + cumulative audit ★ 跨 50% domain coverage milestone 33/63)
> Cut trigger: 10 cumulative v1.9.2 candidates post round 06 = ≥10 cut planning trigger threshold MET (1 NEW HIGH round 06 explicit JSON template + 1 MED round 05 LIST_ITEM hl+sib field-explicit-null + 3 HIGH round 04 R-2.8-1/2/3 + 1 LOW round 03 FIGURE-vs-CODE_LITERAL boundary + 4 INFO/process candidates)
> 基于 v1.9.1 (2026-05-05) + B-03c rounds 01-06 evidence (`evidence/checkpoints/` + `multi_session/P2_B-03c_round_*_kickoff.md` + `_progress.json` `b_03c_round_*_details`)
> 角色: Writer MD (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.9.2 变更 over v1.9.1: 6 NEW E-rules (E-1..E-6) consolidating 10 candidate stack — 1 CRITICAL §E-1 dispatch JSON template + 3 HIGH §E-2/E-3/E-4 R-2.8-1/2/3 explicit codify + 1 MED §E-5 non-HEADING field-explicit-null + 1 LOW §E-6 FIGURE-vs-CODE_LITERAL boundary. **Backward compatible** with v1.9.1 atoms (B-02 + B-03c rounds 01-06 production atoms md_atoms.jsonl 8122 cumulative). v1.9.1 archived `archive/v1.9.1_final_2026-05-06/`.

## 角色硬约束 (v1.7/v1.8/v1.9/v1.9.1 carry-forward unchanged)

参 `archive/v1.7_final_2026-04-30/P0_writer_md_v1.7.md` §角色硬约束 全文.
参 `archive/v1.9_final_2026-05-05/P0_writer_md_v1.9.md` §C-1..C-8 全文.
参 `archive/v1.9.1_final_2026-05-06/P0_writer_md_v1.9.1.md` §D-1..D-8 全文.

═══════════════════════════════════════════════════════════════════
## v1.9.2 NEW PATCHES (E-1..E-6, B-03c rounds 01-06 + round 06 batch_72 HIGH-severity 实证驱动)
═══════════════════════════════════════════════════════════════════

### §E-1 Dispatch contract: explicit JSON template + reference working atom (CRITICAL — HIGH severity prevention)

**Background**: B-03c round 06 batch_72 MS/assumptions.md writer general-purpose initial dispatch emitted 4 schema violations 100% atoms — (1) `verbatim_text` field name instead of frozen schema `verbatim`, (2) missing required `line_start`/`line_end` int fields, (3) missing `figure_ref` field, (4) `atom_type: "H1"` instead of canonical enum `"HEADING"`. Reviewer caught HALT at audit stage. Cause traced: dispatch prompt narratively described schema ("atom_type=HEADING") but lacked explicit JSON template; writer subagent interpreted loosely (used "H1") + dropped optional-looking fields + renamed intuitive variants.

This is the **same root cause class** as round 04 R-2.8-3 (extracted_by string→object regression) — writer dispatch prompt narrative description without concrete example invites subagent reinterpretation. Round 04 fix was post-hoc in-place patch. Round 06 fix was full re-dispatch. v1.9.2 codifies prevention.

**Orchestrator rule (kickoff doc + dispatch prompt writer = main session)**: Every batch dispatch prompt MUST include:

1. **Explicit JSON template** showing all 12 frozen schema fields with EXACT names:

```json
{
  "atom_id": "<prefix>_aNNN",
  "file": "<full path with knowledge_base/ prefix>",
  "line_start": <int>,
  "line_end": <int>,
  "parent_section": "§<scope>",
  "atom_type": "HEADING" | "LIST_ITEM" | "SENTENCE" | "TABLE_HEADER" | "TABLE_ROW" | "FIGURE" | "NOTE" | "CODE_LITERAL" | "CROSS_REF",
  "verbatim": "<source byte-exact, NOT verbatim_text>",
  "heading_level": <int> for HEADING, null for non-HEADING,
  "sibling_index": <int> for HEADING, null for non-HEADING (EXPLICIT JSON null, NOT omitted),
  "figure_ref": null,
  "cross_refs": [<refs>] or [],
  "extracted_by": {
    "subagent_type": "<writer agent>",
    "prompt_version": "P0_writer_md_v1.9.2",
    "ts": "<ISO timestamp>"
  }
}
```

2. **Reference to working production atom** as concrete schema example (e.g., point to `evidence/checkpoints/P2_B-03_batch_70_md_atoms.jsonl` first atom as gold reference).

3. **Explicit "NEVER" anti-patterns list**:
- ❌ `verbatim_text` → use `verbatim`
- ❌ `atom_type: "H1"` or `"H2"` → use `atom_type: "HEADING"` (level via `heading_level`)
- ❌ Missing `line_start`/`line_end` → both REQUIRED integer fields
- ❌ Missing `figure_ref` → REQUIRED (null for non-FIGURE atoms)
- ❌ `extracted_by` string form `"name+version"` → use object schema

**Hook 22c for writer (NEW, pre-DONE schema self-validate)**: Before writing JSONL, writer MUST verify EACH atom has all 12 keys with EXACT names. If any key missing or named differently, FIX before writing. Writer DONE report MUST include `schema_self_validate: PASS (12/12 keys per atom, 0 verbatim_text, 0 H1/H2 enums)` confirmation.

**Reviewer rule (paired-sync §R-E1)**: When auditing, perform schema regression sweep as PRIORITY check 1 (before per-atom byte-exact verify). Detect any of: `verbatim_text` field, missing line_start/line_end/figure_ref, atom_type `H1`/`H2`/non-enum strings — emit FAIL_SCHEMA_REGRESSION at HIGH severity → HALT.

**B-03c round 07+ entry**: 所有 round 07+ kickoff dispatch prompt template 强制 §E-1 explicit JSON template + reference working atom; 缺 = orchestrator preflight FAIL.

### §E-2 H1 sibling_index=1 universal explicit codification (HIGH)

**Background**: B-03c round 04 batch_45 EX/assumptions.md a001 H1 atom emitted with `sibling_index=null` (orchestrator dispatch prompt 误指 sib=null). Post-batch_46 sanity-check verified 47/47 prior H1 atoms cumulative B-02+B-03b+B-03c-r01-03 = sib=1 universal precedent. 1 atom in-place fixed with Rule B backup.

**Rule (codify implicit empirical convention)**: ALL HEADING atoms with `heading_level=1` (file root H1) MUST have `sibling_index=1`. NEVER null. This is the **default and only** valid value for H1 atoms in the SDTM knowledge base.

**Rationale**: H1 in this corpus is universally the file-root single chapter title (e.g., `# AE — Assumptions`, `# Chapter 4 — Models`). There is exactly 1 H1 per file by construction. sibling_index=1 represents "1st of 1 sibling" canonically.

**Pre-DONE Hook 22c check**: Writer self-validate H1 atom sib=1 explicit (NOT null) before writing JSONL. Writer DONE report MUST include `r_2_8_1_h1_sib_idx_1: PASS` confirmation.

**Reviewer rule (paired-sync §R-E2)**: Audit verifies a001 (or whichever atom is H1 of file) has `heading_level=1, sibling_index=1`. Emit FAIL_H1_SIB_IDX if sib≠1 → HIGH severity HALT.

**Cumulative empirical baseline post round 06**: 81 H1 atoms across 81 files atomized = 81/81 sib=1 universal post round 04 fix.

### §E-3 TABLE_HEADER sibling_index=null universal explicit codification (HIGH)

**Background**: B-03c round 04 batch_49 + batch_51 FA/examples.md + FT/examples.md TABLE_HEADER atoms emitted with `sibling_index=1` or `2` (writer prompt v1.9.1 silent on TABLE_HEADER sib_idx specific rule; writer applied positional sib chain). Post-fix 17 atoms patched (15 batch_49 + 2 batch_51) with Rule B backups. Cumulative precedent verified 338/353 prior TABLE_HEADER atoms = sib=null universal.

**Rule (codify implicit empirical convention)**: ALL `atom_type="TABLE_HEADER"` atoms MUST have `sibling_index=null`. NEVER 1, 2, 3, ..., N. Also NEVER omitted — explicit JSON `"sibling_index": null`.

**Rationale**: TABLE_HEADER atoms represent the 2-row header span (header row + alignment row) of a markdown table. They are not part of the H2/H3/etc heading sibling chain. They have a `heading_level=null` (since not HEADING type, despite naming). `sibling_index=null` aligns with all non-HEADING atoms.

**Hook A1 carry-forward (v1.9 baseline unchanged)**: TABLE_HEADER `line_end - line_start = 1` (2-row span: header + alignment row).

**Pre-DONE Hook 22c check**: Writer self-validate ALL TABLE_HEADER atoms have `sibling_index=null` explicit. Writer DONE report MUST include `r_2_8_2_table_header_sib_null: PASS (N/N TABLE_HEADER atoms)` confirmation.

**Reviewer rule (paired-sync §R-E3)**: Audit verifies TABLE_HEADER atoms `sibling_index=null` universal. Emit FAIL_TABLE_HEADER_SIB if any TABLE_HEADER has sib≠null → HIGH severity HALT.

**Cumulative empirical baseline post round 06**: 401 TABLE_HEADER atoms across rounds 01-06 = 401/401 sib=null universal post round 04 fix (138 round 04 + 41 round 05 + 25 round 06 + ~197 rounds 01-03).

### §E-4 extracted_by object schema explicit codification (HIGH)

**Background**: B-03c round 04 batches 48 + 52 + 56 FA/assumptions.md + GF/assumptions.md + IE/assumptions.md emitted `extracted_by` as string form `"general-purpose+P0_writer_md_v1.9.1"` instead of object schema. 30 atoms cumulative fixed with Rule B backups. Cause: orchestrator dispatch prompt 简化 form `"extracted_by": "name+version"` 而非 explicit object — writer literally interpreted simplified narrative.

**Rule (codify implicit empirical convention)**: ALL atoms MUST have `extracted_by` as object schema with EXACTLY these 3 fields:

```json
"extracted_by": {
  "subagent_type": "<writer subagent name>",
  "prompt_version": "P0_writer_md_v1.9.2",
  "ts": "<ISO 8601 timestamp>"
}
```

NEVER string form (e.g., `"name+version"` / `"general-purpose v1.9.2"` / etc).

**Pre-DONE Hook 22c check**: Writer self-validate ALL atoms have `extracted_by` object form (NOT string). Writer DONE report MUST include `r_2_8_3_extracted_by_object: PASS (N/N atoms)` confirmation.

**Reviewer rule (paired-sync §R-E4)**: Audit verifies `extracted_by` is object form universal. Emit FAIL_EXTRACTED_BY if any atom has string form → HIGH severity HALT.

**Cumulative empirical baseline post round 06**: 8122 atoms cumulative B-02+B-03b+B-03c-rounds-01-06 = 8122/8122 object form universal post round 04 fix.

### §E-5 non-HEADING heading_level + sibling_index field-explicit-null requirement (MEDIUM, MED-01 codification)

**Background**: B-03c round 05 batch_60 LB/assumptions.md 9 LIST_ITEM atoms (a002-a010) emitted with `heading_level` and `sibling_index` fields ENTIRELY OMITTED instead of explicit JSON null. Cause: dispatch prompt for batch_60 used terse "sib_idx=null universal" wording vs batch_58 explicit JSON form `"sibling_index": null` → writer interpretation drift (omitted fields instead of writing explicit null). 18 fields added in-place (9 hl + 9 sib) with Rule B backups. Subsequent batches 61-69 dispatched with explicit JSON form prompt instruction = 0 recurrence.

**Rule (codify post-MED-01 prevention)**: ALL non-HEADING atoms (atom_type ∈ {LIST_ITEM, SENTENCE, TABLE_HEADER, TABLE_ROW, FIGURE, NOTE, CODE_LITERAL, CROSS_REF}) MUST emit `heading_level=null` AND `sibling_index=null` as **EXPLICIT JSON null fields**. NEVER omit either field — even though both values are null, both keys MUST be present in the JSON object.

**Rationale**: JSON Schema 2020-12 frozen `atom_schema.json` v1.2 requires both fields. Field omission breaks schema validation + downstream tooling expecting consistent atom shape. Schema explicit null preserves "field present, value null" semantics distinct from "field missing" ambiguity.

**Pre-DONE Hook 22c check**: Writer self-validate ALL non-HEADING atoms have `"heading_level":null, "sibling_index":null` literal byte present in JSONL output. Writer DONE report MUST include `med_01_non_heading_fields_explicit: PASS (N/N atoms)` confirmation.

**Reviewer rule (paired-sync §R-E5)**: Audit verifies via raw JSONL byte-grep `grep -c '"heading_level":null'` and `grep -c '"sibling_index":null'` matching count of non-HEADING atoms. Emit FAIL_FIELD_OMISSION if either field omitted on any atom → MEDIUM severity HALT.

**Cumulative empirical baseline post round 06**: 7720 non-HEADING atoms cumulative round 06 alone (309/331 = 22 HEADING + 309 non-HEADING) all explicit null fields post-fix sustained.

### §E-6 FIGURE-vs-CODE_LITERAL boundary clarification (LOW carry-forward from round 03)

**Background**: B-03c round 03 batch_34 DM/examples.md a072 atom mistakenly classified as CODE_LITERAL (mermaid fenced block at L115-149) — should have been FIGURE per round 03 §2.6 lock. Cause: v1.9.1 §C-8 archive 引用 没显式 covered fenced code block in domains/. Resolved post-hoc + 3 more FIGURE atoms emitted cleanly in batch_35.

**Rule (clarify boundary)**:
- **atom_type=FIGURE**: fenced code blocks with language identifier `mermaid` (or other diagram format) representing visual content. verbatim 含 full mermaid block byte-exact (incl. ` ```mermaid` opening + content + ` ``` ` closing fences). `figure_ref` MUST be non-null with format `<file path> L<start>-<end> mermaid <type>: <description>`.
- **atom_type=CODE_LITERAL**: fenced code blocks with language identifier other than diagram-language (e.g., `xml`, `json`, `python`, `bash`, no-language) representing literal data values OR single literal codelist values (e.g., literal `"AE"` value in narrative). NOT for diagrams.

**Hook A4 carry-forward (v1.9 baseline)**: FIGURE atom MUST have `figure_ref` non-null. CODE_LITERAL atom may have `figure_ref=null`.

**Reviewer rule (paired-sync §R-E6)**: When encountering fenced code block, verify language identifier — if `mermaid` → atom_type=FIGURE, if other → atom_type=CODE_LITERAL or context-dependent. Emit INFO_FIGURE_BOUNDARY if classification ambiguous.

### §D-1..D-8 carry-forward (v1.9.1 unchanged)

ALL v1.9.1 §D-1..D-8 rules carry-forward to v1.9.2 unchanged:
- §D-1 Hook 22b kickoff numeric claim grep checksum (CRITICAL)
- §D-2 NOTE blockquote-prefix bold-Note carve-out (HIGH)
- §D-3 D5 markdown-uniform numbered Heading dual-constraint (HIGH)
- §D-4 D8 numberless `## Overview` H2 chapter root inherit (NEW)
- §D-5 bold-caption SENTENCE retention rule (MEDIUM)
- §D-6 TABLE_HEADER style 兼容 (writer 2-row sustained, matcher 1-row legacy accept) (MEDIUM)
- §D-7.1..D-7.13 LOW codifications group consolidated
- §D-8 FALLBACK pool peer-alternative status promotion (INFO codification)

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.7/v1.8/v1.9/v1.9.1 carry-forward, FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.9.1_final_2026-05-06/P0_writer_md_v1.9.1.md` for §D-1..D-8 + carry-forward chain to v1.9 §C-1..C-8 + v1.7/v1.8 archives for §A-N28 full text.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (v1.9.2 = 28 hooks for MD-side)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- v1.8 Hook 21 (PDF-only, N/A MD-side) carry-forward unchanged
- v1.9 Hook 22 carry-forward (pre-DONE last_atom.line_end ≥ slice_end - 5, hard slice mode only)
- v1.9 Hook A1/A2/A3 carry-forward (TABLE_HEADER `line_end - line_start ≤ 1` / HEADING `^#{1,6}\s+` / LIST_ITEM full prefix + multi-sentence)
- v1.9 Hook A4 carry-forward (FIGURE atom 必带 figure_ref non-null)
- v1.9.1 Hook 22b carry-forward (kickoff §0.5 grep checksum integrity 信任)
- v1.9.1 Hook D-NOTE-BQ carry-forward (blockquote-prefix bold-Note → atom_type=NOTE)
- v1.9.1 Hook D-D8 carry-forward (numberless `## Overview` H2 → chapter root)
- **v1.9.2 NEW Hook 22c**: pre-DONE schema self-validate — writer MUST verify each atom 12 keys with EXACT names + r_2_8_1/2/3 + med_01 + extracted_by object before writing JSONL. DONE report MUST include `schema_self_validate: PASS` + sub-confirms.
- **v1.9.2 NEW Hook E-2-1**: H1 atom sibling_index=1 universal (NOT null)
- **v1.9.2 NEW Hook E-3-2**: TABLE_HEADER atom sibling_index=null universal (NOT 1/2/3)
- **v1.9.2 NEW Hook E-4-3**: extracted_by object schema universal (NOT string form)
- **v1.9.2 NEW Hook E-5**: non-HEADING heading_level + sibling_index field-explicit-null (NOT omitted)

**MD-side hook 总数**: 25 (v1.9.1) + 5 NEW (v1.9.2 Hook 22c + E-2-1 + E-3-2 + E-4-3 + E-5) − overlap counting = **28 hooks effective** (Hook 22c 涵盖 E-2-1/E-3-2/E-4-3/E-5 sub-checks; counted independently per layer).

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.2 sync with B-03c rounds 01-06 cycle evidence)
═══════════════════════════════════════════════════════════════════

- **N21 PDF + MD all-side blanket ban**: STRONGLY VALIDATED EXTENDED (v1.9.1 baseline + B-03c rounds 01-06 21 batches × 6 = 126 batches cumulative writer-family contamination = 0 across chapters/ + domains/ + sustained executor + general-purpose pool)
- **FALLBACK pool peer-alternative status**: STRONGLY VALIDATED EXTENDED (general-purpose + pr-review-toolkit:code-reviewer 等同 OMC priority; sustained 96-batch B-02+B-03b+B-03c rounds 01-06 100% PASS post-fix empirical quality; 8122 atoms 0 writer defect post-fix)
- **Axis 5 ordered LIST_ITEM**: STRONGLY VALIDATED EXTENDED (P1 round 14 codify + B-02 9 batches + B-03c rounds 01-06 60+ batches sustained 0 violation; §D-7.2)
- **D5 markdown-uniform numbered Heading dual-constraint**: SUSTAINED (B-02 batch 06 ch03 L117 实证; round 06 0 instances in 5 ass.md + 5 ex.md)
- **D7 NOTE blockquote carve-out**: SUSTAINED (B-02 batch 09 ch08 L389 实证; round 03 batch_35 DM/ex 3 NOTE atoms multi-instance; round 06 0 instances)
- **D8 numberless `## Overview` chapter root inherit**: SUSTAINED (post pilot F-P2P-002 N27 fix + B-02 batch 09 D8 INAUGURAL + round 04 §2.7 numberless H2 in ass.md FT/ass first-time lock + round 06 0 trigger)
- **bold-caption SENTENCE retention rule (§D-5)**: STRONGLY VALIDATED EXTENDED (B-02 batch 06 codify + B-03c rounds 01-06 ~250+ instances cumulative; 100% canonical SENTENCE classification, 0 misclassification across 6 rounds)
- **§2.4 multi-batch single-file slice (round 03 lock)**: SUSTAINED (DM/ex + DS/ex + EX/ex sliced batches + round 06 0 trigger 因 max 153L < 300L)
- **§2.6 FIGURE-in-domains lock (round 03 lock)**: SUSTAINED (DM/ex 4 FIGURE atoms validated + round 04/05/06 0 occurrence)
- **§2.7 numberless H2 in assumptions.md = file-root parent (round 04 lock)**: SUSTAINED (FT/ass first-time + round 05/06 0 trigger)
- **R-2.8-1 H1 sib_idx=1 universal**: NEW STATUS CODIFIED §E-2 (round 04 in-place fix 1 atom + post-fix 81/81 universal sustained rounds 04-06)
- **R-2.8-2 TABLE_HEADER sib_idx=null universal**: NEW STATUS CODIFIED §E-3 (round 04 in-place fix 17 atoms + post-fix 401/401 universal sustained rounds 04-06)
- **R-2.8-3 extracted_by object schema**: NEW STATUS CODIFIED §E-4 (round 04 in-place fix 30 atoms + post-fix 8122/8122 universal sustained rounds 04-06)
- **MED-01 non-HEADING field-explicit-null**: NEW STATUS CODIFIED §E-5 (round 05 in-place fix 18 fields + post-fix sustained rounds 05-06 0 recurrence)
- **CRITICAL §E-1 dispatch JSON template + reference working atom**: NEW STATUS CODIFIED (round 06 batch_72 4-schema-regression HALT-RESOLVED + re-dispatch with explicit JSON template → batches 73-79 ALL clean schema 0 recurrence)
- **§E-6 FIGURE-vs-CODE_LITERAL boundary clarification**: NEW STATUS CODIFIED (round 03 carry-forward)
- **CRITICAL kickoff self-consistency rule (Hook 22b)**: SUSTAINED (B-03+ kickoff template §0.5 mandatory; round 06 batch_71 INFO drift "4→5 tables" caught + writer Rule-B'd byte-exact)
- **Schema v1.2.1**: SUSTAINED status (8122 atoms 0 schema issue post round 06; v1.3 promote 暂搁置 — frozen v1.2 working well)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.7 | 2026-04-29 | post P1 round 10 cut EMERGENCY-CRITICAL: N21 SCOPED PDF-side blanket ban writer-family |
| v1.8 | 2026-04-30 | post P1 round 12 cut: 5 NEW patches N24-N28 paired-sync; N21 PDF-side carry-forward |
| v1.9 | 2026-04-29 | post P2 Pilot 2-attempt cycle: 8 NEW patches C-1..C-8. N21 全 ban writer-family 扩到 MD-side. |
| v1.9.1 | 2026-05-05 | post P2 B-02 cycle CLOSED + cumulative audit GREEN-LIGHT 30/30=100%: 8 NEW D-rules consolidating 19 candidate stack (1 CRITICAL Hook 22b kickoff checksum + 2 HIGH D7 NOTE-BQ + D5 dual-constraint + 1 NEW D8 chapter-root-inherit + 2 MEDIUM bold-caption + TABLE_HEADER style兼容 + 13 LOW group consolidated). FALLBACK pool peer-alternative status PROMOTED. 3 NEW hooks (22b + D-NOTE-BQ + D-D8). MD-side hooks 22 → 25. v1.9 archived `archive/v1.9_final_2026-05-05/`. **Backward compatible** — ch04 pilot a001-a218 v1.8 style + B-01/B-02 v1.9 style 都 accepted by matcher/reviewer 之 §M-D6/§R-D6. |
| **v1.9.2** | **2026-05-06** | **post P2 B-03c rounds 01-06 cycle CLOSED + ★ 跨 50% domain coverage milestone 33/63 + 8122 atoms cumulative**: 6 NEW E-rules consolidating 10 candidate stack (1 CRITICAL §E-1 dispatch JSON template + reference working atom HIGH-severity prevention from round 06 batch_72 4-schema-regression + 3 HIGH §E-2/E-3/E-4 R-2.8-1/2/3 explicit codify from round 04 post-hoc fixes + 1 MED §E-5 non-HEADING field-explicit-null from round 05 MED-01 + 1 LOW §E-6 FIGURE-vs-CODE_LITERAL boundary from round 03 carry). 5 NEW hooks (22c + E-2-1 + E-3-2 + E-4-3 + E-5). MD-side hooks 25 → 28. v1.9.1 archived `archive/v1.9.1_final_2026-05-06/`. **Backward compatible** — B-02 + B-03c rounds 01-06 production atoms 8122 cumulative byte-exact preserved. |
