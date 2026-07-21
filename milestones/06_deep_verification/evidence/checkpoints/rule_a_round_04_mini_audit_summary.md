# Round 04 Mini-Audit Summary — pr-review-toolkit:silent-failure-hunter (AUDIT mode)

> Reviewer: `pr-review-toolkit:silent-failure-hunter` (AUDIT-mode pivot, first burn this family in B-03c rounds)
> Round 04 final state: 13 batches (45..57) / 731 atoms / 6 domains EX/FA/FT/GF/HO/IE / 12 source files (1 sliced)
> Cumulative root jsonl post round 04: **7114 atoms** (= 6383 + 731, arithmetic verified)
> Date: 2026-05-06
> Distinct from: per-batch reviewers × 13 (pr-review-toolkit:code-reviewer); round 01 mini-audit (feature-dev:code-reviewer); round 02 mini-audit (feature-dev:code-architect); round 03 mini-audit (pr-review-toolkit:type-design-analyzer)

---

## 1. Sample composition + rationale

10 atoms stratified per kickoff §6 sample plan:

| # | atom_id | atom_type | h_lvl | sib_idx | L-range | Batch | File | Rationale |
|---|---|---|---|---|---|---|---|---|
| 1 | `md_dmEX_ex_a144` | TABLE_ROW | null | null | L231 | 46 | EX/examples.md | §2.4 cross-batch boundary LAST atom of batch_46 |
| 2 | `md_dmEX_ex_a145` | HEADING | 2 | 6 | L233 | 47 | EX/examples.md | §2.4 cross-batch boundary FIRST atom of batch_47 (verify atom_id 续号 a144→a145, parent §EX.5 → §EX file root H2 transition) |
| 3 | `md_dmFT_assn_a005` | HEADING | 2 | 1 | L9 | 50 | FT/assumptions.md | §2.7 numberless H2 atom itself (HEADING h_lvl=2 sib=1 parent=file root) |
| 4 | `md_dmFT_assn_a007` | LIST_ITEM | null | null | L13 | 50 | FT/assumptions.md | §2.7 under-H2 LIST_ITEM (parent=file root, NOT new sub-namespace) — first under-H2 LIST_ITEM in numberless H2 case |
| 5 | `md_dmEX_assn_a001` | HEADING | 1 | 1 | L1 | 45 | EX/assumptions.md | EX/ass H1 (Invariant 10 verify) |
| 6 | `md_dmFA_ex_a001` | HEADING | 1 | 1 | L1 | 49 | FA/examples.md | FA/ex H1 (stratified domain coverage + H1 sib=1 verify) |
| 7 | `md_dmHO_ex_a015` | TABLE_ROW | null | null | L25 | 55 | HO/examples.md | HO/ex stratified TABLE_ROW |
| 8 | `md_dmGF_ex_a014` | TABLE_HEADER | null | null | L27-28 | 53 | GF/examples.md | GF/ex stratified TABLE_HEADER (verify span=1 + sib=null Invariant #4) |
| 9 | `md_dmIE_ex_a005` | SENTENCE | null | null | L9 | 57 | IE/examples.md | IE/ex bold-caption SENTENCE (`**Rows 3-4:**` pattern per §R-D5 — verify SENTENCE classification not HEADING/NOTE) |
| 10 | `md_dmFA_assn_a001` | HEADING | 1 | 1 | L1 | 48 | FA/assumptions.md | FA/ass H1 — **also covers `extracted_by` schema-deviation case** (batch 48/52/56 string form) |

**Composition stats**: 5 HEADING (3 H1 + 2 H2 incl §2.7 numberless) / 2 TABLE_ROW / 1 LIST_ITEM / 1 TABLE_HEADER / 1 SENTENCE.
**Domain coverage**: EX (3 atoms 1 ass + 2 ex) + FA (2 atoms 1 ass + 1 ex) + FT (2 atoms 2 ass) + GF (1 atom ex) + HO (1 atom ex) + IE (1 atom ex) = 6/6 domains covered.
**Required type coverage**: ✓ H1, ✓ H2, ✓ TABLE_HEADER (sib=null verify), ✓ LIST_ITEM (sib=null verify), ✓ SENTENCE, ✓ TABLE_ROW.
**Boundary special-cases covered**: §2.4 cross-batch boundary (a144+a145), §2.7 numberless H2 in ass.md (a005+a007), §R-D5 bold-caption SENTENCE (IE/ex a005).

---

## 2. 10/10 verdict table + final pass rate

Per reviewer §B-3, each atom checked against (a)-(h):
(a) atom_id format & sequence — regex `^md_dm[A-Z]{2}_(assn|ex)_a\d{3,}$`
(b) atom_type ∈ 9-enum
(c) verbatim byte-exact match to source line(s)
(d) line_start/line_end correct (per atom_type — HEADING/LIST_ITEM/SENTENCE/TABLE_ROW = 1 line, TABLE_HEADER = 2 lines)
(e) parent_section correct (file root vs sub-namespace per round 04 conventions)
(f) sibling_index correct (H1=1, H2=N positional, LIST_ITEM=null, TABLE_*=null, SENTENCE=null)
(g) heading_level correct (HEADING has level, others null)
(h) file prefix `knowledge_base/`

| atom_id | type | (a) | (b) | (c) | (d) | (e) | (f) | (g) | (h) | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| md_dmEX_ex_a144 | TABLE_ROW | ✓ | ✓ | ✓ | ✓ | ✓ §EX.5 | ✓ null | ✓ null | ✓ | **PASS** |
| md_dmEX_ex_a145 | HEADING H2 | ✓ | ✓ | ✓ | ✓ | ✓ §EX root | ✓ sib=6 | ✓ h_lvl=2 | ✓ | **PASS** |
| md_dmFT_assn_a005 | HEADING H2 | ✓ | ✓ | ✓ | ✓ | ✓ §FT root | ✓ sib=1 | ✓ h_lvl=2 | ✓ | **PASS** |
| md_dmFT_assn_a007 | LIST_ITEM | ✓ | ✓ | ✓ | ✓ | ✓ §FT root | ✓ null | ✓ null | ✓ | **PASS** |
| md_dmEX_assn_a001 | HEADING H1 | ✓ | ✓ | ✓ | ✓ | ✓ §EX root | ✓ sib=1 | ✓ h_lvl=1 | ✓ | **PASS** |
| md_dmFA_ex_a001 | HEADING H1 | ✓ | ✓ | ✓ | ✓ | ✓ §FA root | ✓ sib=1 | ✓ h_lvl=1 | ✓ | **PASS** |
| md_dmHO_ex_a015 | TABLE_ROW | ✓ | ✓ | ✓ | ✓ | ✓ §HO.1 | ✓ null | ✓ null | ✓ | **PASS** |
| md_dmGF_ex_a014 | TABLE_HEADER | ✓ | ✓ | ✓ | ✓ span=1 | ✓ §GF.1 | ✓ null | ✓ null | ✓ | **PASS** |
| md_dmIE_ex_a005 | SENTENCE | ✓ | ✓ | ✓ | ✓ | ✓ §IE.1 | ✓ null | ✓ null | ✓ | **PASS** |
| md_dmFA_assn_a001 | HEADING H1 | ✓ | ✓ | ✓ | ✓ | ✓ §FA root | ✓ sib=1 | ✓ h_lvl=1 | ✓ | **PASS** |

**Final pass rate: 10/10 = 100.0%**

> NOTE: `md_dmFA_assn_a001` PASSed all (a)-(h) because the (a)-(h) criteria do NOT include schema-shape of `extracted_by`. The schema deviation surfaces in Invariant #5 below — see §3 invariants section + findings.

---

## 3. 10 round invariants — gate ≥ 8/10 PASS

### Invariant #1 — atom_id collision (cumulative ~7114 atoms post round 04)

**PASS** — `(atom_id, file)` duplicates in root jsonl: **0**. Special focus EX/ex contiguous a001..a277 (277 atoms across batch_46+47): 0 gaps, 0 dups, fully contiguous.

Evidence: `python3` scan of 7114 root atoms; explicit check of EX/ex chain confirms range `a001..a277` with `len=277` and no duplicates.

### Invariant #2 — Hook C-8 file prefix universal

**PASS** — All 731 round 04 atoms + cumulative 7114 root atoms have `file` starting with `knowledge_base/`. 0 violations.

Evidence: scan over root jsonl: `Atoms with non knowledge_base/ prefix: 0`. All 12 round 04 source files atomized: `knowledge_base/domains/{EX,FA,FT,GF,HO,IE}/{assumptions,examples}.md`.

### Invariant #3 — H3a sub-namespace convention (expect 0 H3 in round 04)

**PASS** — H3 atoms (heading_level=3) in round 04: **0** as expected. Source kickoff §0.5 grep verified 0 H3 across 12 files.

Evidence: HEADING heading_level distribution in round 04: `{1: 12, 2: 24}` — no H3, H4, etc. (12 H1 = 12 source files, 24 H2 = examples.md sub-headers + FT/ass numberless H2).

### Invariant #4 — TABLE_HEADER Hook A1 span=1 + sib_idx=null universal

**PASS** — 63/63 TABLE_HEADER atoms in round 04 have `line_end - line_start == 1` AND `sibling_index = null`.

By-batch distribution: batch_45=0, batch_46=18, batch_47=13, batch_48=0, batch_49=15, batch_50=0, batch_51=2, batch_52=0, batch_53=10, batch_54=0, batch_55=4, batch_56=0, batch_57=1 = **63 TABLE_HEADER total** (exactly matches kickoff §6 expected).

Evidence: 0 atoms with span > 1; 0 atoms with non-null sib_idx. v1.9 standard 2-row TABLE_HEADER convention sustained universally; post batch_49+51 in-place fix held.

### Invariant #5 — extracted_by consistency (subagent_type=general-purpose + prompt_version=P0_writer_md_v1.9.1)

**FAIL — partial deviation HIGH severity**

- 701/731 atoms have `extracted_by` as object: `{subagent_type: "general-purpose", prompt_version: "P0_writer_md_v1.9.1", ts: "..."}` ✓
- **30/731 atoms have `extracted_by` as flat STRING: `"general-purpose+P0_writer_md_v1.9.1"`** ✗

Affected atoms (all 30): `md_dmFA_assn_a001..a009` (batch_48, 9 atoms) + `md_dmGF_assn_a001..a016` (batch_52, 16 atoms) + `md_dmIE_assn_a001..a005` (batch_56, 5 atoms).

Schema reference: `.work/06_deep_verification/schema/atom_schema.json` `$defs.extracted_by` requires:
```json
{"type": "object", "required": ["subagent_type", "prompt_version", "ts"], "properties": {...}}
```

The 30 deviated atoms violate JSON Schema 2020-12 `extracted_by` shape contract. The semantic content (subagent_type + prompt_version) is preserved in the concatenated string but `ts` is missing entirely and the object structure is collapsed.

**Severity**: HIGH (schema contract violation + missing `ts` field) — but **NOT a content/Rule-A defect**; the writer/extracted_by metadata is auxiliary to atom content. atoms remain content-correct (verbatim/parent/sib/lvl all PASS).

**See §6 Findings for repair recommendation.**

### Invariant #6 — §2.4 lock validation (round 03 carry-forward)

**PASS** — EX/ex sliced batch_46+47:
- batch_46 末 atom = `md_dmEX_ex_a144` (TABLE_ROW L231, parent `§EX.5 [Example 5]`, verbatim `| 2 | ABC | EX | | EXLNKID | | ONE | 1 |`)
- batch_47 首 atom = `md_dmEX_ex_a145` (HEADING h_lvl=2 sib=6 L233, parent `§EX [EX — Examples]` file root, verbatim `## Example 6`)
- atom_id 续号 a144 → a145 = +1 ✓
- parent_section H2 boundary clean: §EX.5 → §EX file root (the H2 atom itself owns file-root parent, then descendants get §EX.6) ✓
- L231 → L233 source gap = 1 blank line (L232) handled correctly ✓

EX/ex full atom_id chain `a001..a277` contiguous (277 atoms) verified.

### Invariant #7 — §2.6 lock validation (round 03 carry-forward, FIGURE-in-domains)

**PASS** — 0 atoms with `atom_type=FIGURE` in round 04 (731 atoms scanned). Matches kickoff §0.5 row 14 grep result (0 mermaid blocks across 12 source files).

### Invariant #8 — LIST_ITEM sib_idx null (round 03 lock)

**PASS** — 106/106 LIST_ITEM atoms in round 04 have `sibling_index = null`. 0 violations.

Evidence: scan round 04 atoms by type LIST_ITEM count=106; non-null sib_idx count=0.

### Invariant #9 — §2.7 NEW round 04 lock (numberless H2 in assumptions.md)

**PASS** — FT/ass batch_50 38 atoms:
- `md_dmFT_assn_a005` (the numberless H2 itself): atom_type=HEADING ✓ heading_level=2 ✓ sibling_index=1 ✓ parent_section=`§FT [FT — Assumptions]` (file root) ✓ verbatim=`## QRS Shared Assumptions` ✓ source byte-exact L9 ✓
- ALL 38 batch_50 atoms have `parent_section = "§FT [FT — Assumptions]"` (file root, NOT new sub-namespace `§FT.QRS [...]`) ✓

parent_section distribution batch_50: `{'§FT [FT — Assumptions]': 38}` — 100% file-root inheritance, §2.7 lock perfectly enforced.

Sample LIST_ITEM under-H2 spot check: `md_dmFT_assn_a007` (L13 first under-H2 list item) parent = `§FT [FT — Assumptions]` ✓ sib=null ✓.

### Bonus Invariant #10 — H1 sib_idx=1 universal precedent

**PASS** — All 59 H1 atoms in cumulative root jsonl have `sibling_index = 1`. Distribution: `{1: 59}` (single value, no exceptions). Post-batch_45 INFO H1 sib correction sustained.

### Invariants gate summary

| # | Invariant | Status |
|---|---|---|
| 1 | atom_id collision | PASS |
| 2 | Hook C-8 file prefix | PASS |
| 3 | H3a sub-namespace (0 expected) | PASS |
| 4 | TABLE_HEADER span=1 + sib=null | PASS |
| 5 | extracted_by consistency | **FAIL** (30/731 string-form deviation) |
| 6 | §2.4 cross-batch slice lock | PASS |
| 7 | §2.6 FIGURE lock (0 expected) | PASS |
| 8 | LIST_ITEM sib_idx null lock | PASS |
| 9 | §2.7 numberless H2 in ass.md lock | PASS |
| 10 | H1 sib=1 universal | PASS |

**Gate result: 9/10 invariants PASS** (≥8/10 threshold satisfied per kickoff §6).

---

## 4. §2.4 / §2.6 / §2.7 lock independent verification

### §2.4 cross-batch slice (EX/ex 434L sliced batch_46+47 at L232|233 H2 boundary)

**Independent re-verification**:
- Source L228-234 read independently:
  ```
  L228: | Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
  L229: |-----|---------|---------|---------|-------|----------|---------|-------|
  L230: | 1 | ABC | EC | | ECLNKID | | ONE | 1 |
  L231: | 2 | ABC | EX | | EXLNKID | | ONE | 1 |
  L232: (blank line)
  L233: ## Example 6
  L234: (blank line)
  ```
- batch_46 末 (a144) verbatim L231 ✓ byte-exact
- batch_47 首 (a145) verbatim L233 ✓ byte-exact
- L232 (blank line) correctly skipped in atomization (no atom for blank lines) ✓
- atom_id 续号 a144 → a145 = +1 ✓
- parent_section transition: a144 = §EX.5 (under Example 5 sub-namespace), a145 = §EX [EX — Examples] (file root, since H2 atom itself owns root parent). Subsequent atom a146 (SENTENCE L235) inherits §EX.6 [Example 6] sub-namespace (verified post-H2).

**§2.4 lock: PASS independently**

### §2.6 FIGURE-in-domains (round 03 lock, expect 0)

**Independent grep verification**:
- `grep -l '^```mermaid$' knowledge_base/domains/{EX,FA,FT,GF,HO,IE}/{assumptions,examples}.md` → no matches (kickoff §0.5 row 14 confirmed 0)
- Round 04 FIGURE atoms: 0 (verified via atom_type scan)

**§2.6 lock: PASS independently**

### §2.7 first-time numberless H2 in assumptions.md (FT/ass L9)

**Independent re-verification**:
- Source FT/ass L9 read independently: `## QRS Shared Assumptions` (numberless, 25 chars) — confirmed numberless `## ` H2 pattern (matches Hook D-D8 negative-case for sub-namespace creation)
- batch_50 atom shape:
  - md_dmFT_assn_a005: `{atom_type: "HEADING", heading_level: 2, sibling_index: 1, parent_section: "§FT [FT — Assumptions]", verbatim: "## QRS Shared Assumptions", line_start: 9, line_end: 9}`
  - All checks match §2.7 lock spec from kickoff §2.7
- batch_50 全 38 atoms parent_section distribution: `{"§FT [FT — Assumptions]": 38}` (single value) — no atom escaped to a `§FT.QRS [...]` sub-namespace ✓
- under-H2 LIST_ITEM spot check (a007 L13): parent=`§FT [FT — Assumptions]` ✓ sib=null ✓
- Pre-H2 atoms (a001..a004 L1-7): all parent=`§FT [FT — Assumptions]` ✓
- Post-H2 atoms (a005..a038 L9-53): all parent=`§FT [FT — Assumptions]` ✓ (NO sub-namespace creation)

**§2.7 lock: PASS independently** — first-time application of v1.9.1 D-4 Hook D-D8 in assumptions.md correctly enforced; no writer drift to sub-namespace creation.

---

## 5. Kickoff drift verification (Hook 22b / R24 — §R-D1)

Per reviewer prompt §R-D1, verify writer atoms vs source byte-exact regardless of any kickoff numeric claims.

- All 10 sample atoms PASS byte-exact verbatim verification ✓
- No discrepancies between atom verbatim and source line content
- Kickoff §0.5 numeric claims (20 entries) all verified ✓ in kickoff itself per Hook 22b
- No `kickoff_doc_drift_detected` flags in batch reports requiring orchestrator-level routing

**Kickoff drift verification: PASS** — no writer fabrication-to-match-kickoff detected; writers correctly Rule-B'd source byte-exact.

---

## 6. Findings

### Finding #1 — extracted_by string-form schema deviation (HIGH)

**Severity**: HIGH (Rule A — schema contract violation)
**Location**: 30 atoms in batches 48 (FA/ass 9), 52 (GF/ass 16), 56 (IE/ass 5) — all 30 in domains/.../assumptions.md files
**Affected atom_ids**: `md_dmFA_assn_a001..a009`, `md_dmGF_assn_a001..a016`, `md_dmIE_assn_a001..a005`

**Issue Description**: `extracted_by` field serialized as flat STRING `"general-purpose+P0_writer_md_v1.9.1"` instead of the schema-required object `{"subagent_type": "general-purpose", "prompt_version": "P0_writer_md_v1.9.1", "ts": "<ISO-8601>"}`.

**Schema violation specifics**:
- `.work/06_deep_verification/schema/atom_schema.json` `$defs.extracted_by` declares `type: "object"` with required keys `subagent_type`, `prompt_version`, `ts`
- Deviated atoms have `type: "string"` — violates JSONSchema 2020-12 `type` constraint
- Missing `ts` field entirely — violates `required: [..., "ts"]` constraint
- Information loss: no per-atom timestamp captured for these 30 atoms

**Hidden errors / silent failure risk** (silent-failure-hunter perspective):
1. Future schema-validation pipelines (`jsonschema.validate(atom, schema)`) will mass-fail these 30 atoms — debugging will require re-reading kickoff + all 13 batch reports to discover the small-file-batch grouping
2. Downstream code that does `atom["extracted_by"]["subagent_type"]` will throw `TypeError: string indices must be integers` — this kind of silent-shape-drift creates obscure crash sites
3. Lineage/audit queries grouping by extractor identity will under-count or mis-bucket these atoms
4. Re-extraction provenance broken: no `ts` means we cannot order by extraction time across batches

**User Impact**: Auditors / downstream tooling expecting object-shape `extracted_by` will encounter type errors. Provenance audits (per writer prompt v1.9.1 §D-7.13) cannot trace extraction times for 30 atoms.

**Recommendation**:
1. Patch script: load each affected batch jsonl + parse `extracted_by` string `"general-purpose+P0_writer_md_v1.9.1"` → reshape to object `{subagent_type:"general-purpose", prompt_version:"P0_writer_md_v1.9.1", ts:"<infer-from-file-mtime-or-batch-report>"}`
2. Re-write the 3 batch jsonl files (48/52/56) + re-fold into root `md_atoms.jsonl` (replace lines, not append)
3. Add v1.9.2 writer prompt rule: "MUST emit extracted_by as object literal with all 3 required keys; reject string serialization"
4. Add CI/check: `jq '[.[] | select(.extracted_by | type == "object" | not)] | length'` should be 0 across all batch jsonls

**Example correction**:
```json
// BEFORE (deviated)
"extracted_by": "general-purpose+P0_writer_md_v1.9.1"

// AFTER (schema-conformant)
"extracted_by": {
  "subagent_type": "general-purpose",
  "prompt_version": "P0_writer_md_v1.9.1",
  "ts": "2026-05-06T11:20:00Z"
}
```

**Routing**: HIGH severity — should be fixed in round 05 prep OR carried as v1.9.2 backlog with explicit pre-round-05 patch task. Does not block round 04 close (content invariants 1-4, 6-10 all PASS; mini-audit per-atom 10/10 PASS).

---

## 7. Final gate verdict

| Gate criterion | Threshold | Result | Status |
|---|---|---|---|
| Per-sample (a)-(h) PASS rate | ≥90% | 10/10 = 100% | ✓ |
| Round invariants | ≥8/10 | 9/10 PASS | ✓ |
| §2.4 lock independent | PASS | PASS | ✓ |
| §2.6 lock independent | PASS | PASS | ✓ |
| §2.7 lock independent | PASS | PASS | ✓ |
| Kickoff drift verification | no writer fabrication | no defects | ✓ |
| HIGH severity findings | 0 expected | 1 (extracted_by schema) | ⚠ |

**Final verdict: CONDITIONAL_PASS**

Rationale: All content-level Rule A criteria are perfectly met (10/10 sample byte-exact + 9/10 invariants + all 3 §2.X locks independently re-verified). However, the 30-atom `extracted_by` schema deviation in batches 48/52/56 is a HIGH severity schema-contract violation that must be addressed before round 05 (or carried with explicit backlog pre-round-05 patch task). Round 04 close can proceed as content correctness is fully validated, but the schema fix should be tracked as a CONDITIONAL_PASS condition.

**Round 05 trigger**: gate satisfied with conditional — recommend Bojiang ack to proceed with explicit acknowledgement of HIGH finding + commit to v1.9.2 prompt rule + 30-atom retro-patch in round 05 prep.

---

*Mini-audit conducted by `pr-review-toolkit:silent-failure-hunter` AUDIT-mode pivot 2026-05-06.*
*Reviewer not previously burned in B-03c rounds (round 01 feature-dev:code-reviewer / round 02 feature-dev:code-architect / round 03 pr-review-toolkit:type-design-analyzer / round 04 per-batch × 13 pr-review-toolkit:code-reviewer all distinct from this reviewer). Rule D 隔离 sustained.*
