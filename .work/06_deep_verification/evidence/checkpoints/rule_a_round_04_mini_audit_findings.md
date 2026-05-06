# Round 04 Mini-Audit Findings — pr-review-toolkit:silent-failure-hunter (AUDIT mode)

> Total findings: **1 HIGH / 0 MEDIUM / 0 LOW**
> Per-sample (a)-(h) defects: 0
> See `rule_a_round_04_mini_audit_summary.md` §6 for full discussion.

---

## HIGH-1: extracted_by string-form schema deviation in 30 atoms (batches 48/52/56)

**Location**:
- `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_48_md_atoms.jsonl` (9 atoms, all of FA/assumptions.md)
- `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_52_md_atoms.jsonl` (16 atoms, all of GF/assumptions.md)
- `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_56_md_atoms.jsonl` (5 atoms, all of IE/assumptions.md)
- `.work/06_deep_verification/md_atoms.jsonl` (cumulative — same 30 atoms appended)

**Severity**: HIGH (Rule A schema contract violation; auxiliary metadata, but the schema is the contract)

**Issue Description**:
The atom_schema.json `$defs.extracted_by` declares this as a required-object with three required string properties (`subagent_type`, `prompt_version`, `ts`):

```json
{
  "type": "object",
  "required": ["subagent_type", "prompt_version", "ts"],
  "properties": {
    "subagent_type": {"type": "string", "description": "..."},
    "prompt_version": {"type": "string", "pattern": "^P0_writer_(pdf|md)_v\\d+(\\.\\d+)?$"},
    "ts": {"type": "string", "format": "date-time"}
  }
}
```

The 30 affected atoms instead emit:
```json
"extracted_by": "general-purpose+P0_writer_md_v1.9.1"
```

This is a flat STRING — violates `type: "object"`, drops the `ts` field entirely, and merges `subagent_type` and `prompt_version` into a delimited blob.

**Affected atom_ids (full list)**:
- `md_dmFA_assn_a001..a009` (9 atoms, batch 48)
- `md_dmGF_assn_a001..a016` (16 atoms, batch 52)
- `md_dmIE_assn_a001..a005` (5 atoms, batch 56)

Pattern observation: ALL three batches are small `assumptions.md` files (FA 15L / GF 25L / IE 9L). EX/ass (batch 45, 33L) does NOT have this defect. HO/ass (batch 54, 13L) does NOT have this defect. FT/ass (batch 50, 53L) does NOT have this defect. The defect is NOT correlated with file size alone — likely correlated with a specific writer dispatch instance for these 3 batches (possibly same dispatcher / template variation / ctx pressure / prompt drift in mid-round).

**Hidden errors a silent-failure-hunter would flag**:
1. **Type-error crash sites downstream**: `atom["extracted_by"]["subagent_type"]` will silently work for 701 atoms then throw `TypeError: string indices must be integers` for 30 atoms — exactly the kind of obscure mid-pipeline failure that takes hours to diagnose without good logging
2. **JSONSchema validation will fire**: any `jsonschema.validate(atom, schema)` will mass-FAIL with `ValidationError: 'general-purpose+P0_writer_md_v1.9.1' is not of type 'object'`. If schema validation is currently disabled/optional, this is itself a silent-failure smell
3. **Provenance lineage broken**: no `ts` field for these 30 atoms means audit/lineage queries cannot order by extraction time, cannot attribute to specific dispatch window
4. **Group-by extractor identity miscounts**: queries doing `GROUP BY extracted_by.subagent_type` will see 30 NULL/error rows
5. **Round 05+ writer dispatch trust**: if writer prompt drifted to flat-string form for 3/13 batches in round 04 without detection, future rounds may have similar drift; this is a process-quality smell

**User Impact**:
- Auditors expecting object-shape `extracted_by` (per kickoff §6 invariant #5) will fail validation
- Future re-runs of cumulative audit (B-04 / Phase 7 RAG ingestion) will hit type errors
- Provenance forensics (e.g., "who wrote this atom and when?") cannot answer for these 30 atoms

**Recommendation**:
1. **Pre-round-05 patch script** (recommended path):
   ```python
   import json
   for batch_num in (48, 52, 56):
       path = f'.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_{batch_num}_md_atoms.jsonl'
       atoms = []
       with open(path) as f:
           for line in f:
               a = json.loads(line)
               eb = a.get('extracted_by')
               if isinstance(eb, str) and eb == 'general-purpose+P0_writer_md_v1.9.1':
                   a['extracted_by'] = {
                       'subagent_type': 'general-purpose',
                       'prompt_version': 'P0_writer_md_v1.9.1',
                       'ts': '2026-05-06T00:00:00Z'  # or recover from file mtime per batch
                   }
               atoms.append(a)
       with open(path, 'w') as f:
           for a in atoms:
               f.write(json.dumps(a, ensure_ascii=False) + '\n')
   # Then rebuild root md_atoms.jsonl from per-batch files (or in-place patch)
   ```
2. **v1.9.2 writer prompt rule** (codify): "MUST emit `extracted_by` as JSON object with all 3 required keys (`subagent_type`, `prompt_version`, `ts`). String/concatenated form is forbidden — schema validation will reject."
3. **Add per-batch reviewer Hook**: schema-validate `extracted_by` shape as part of Rule A boundary checks (currently only verbatim/parent/sib are checked). Adding `jsonschema.validate(atom["extracted_by"], EB_SCHEMA)` to the per-batch reviewer would have caught this at batch 48 instead of 9 batches later.
4. **CI lane**: pre-commit hook or CI step that runs `jq 'select(.extracted_by | type != "object")' md_atoms.jsonl | wc -l` and fails if > 0.

**Status routing**:
- Round 04 close: do NOT block (content correctness 100%, schema-shape is auxiliary). Document the conditional pass.
- Round 05 prep: schedule patch + v1.9.2 prompt rule + per-batch reviewer hook upgrade as explicit pre-round-05 task.
- Backlog tracking: enter into `_progress.json` `b_03c_round_04_findings` field as HIGH-1 with status `OPEN_PENDING_PATCH`.

---

## Per-sample (a)-(h) defects: 0

All 10 sampled atoms passed all (a)-(h) checks. Specifically:
- (a) atom_id format: 10/10 PASS regex `^md_dm[A-Z]{2}_(assn|ex)_a\d{3,}$`
- (b) atom_type: 10/10 ∈ valid 9-enum
- (c) verbatim byte-exact: 10/10 PASS source line read independently
- (d) line_start/line_end: 10/10 PASS (4 H1 single-line, 2 H2 single-line, 2 TABLE_ROW single-line, 1 LIST_ITEM single-line, 1 SENTENCE single-line, 1 TABLE_HEADER 2-line span)
- (e) parent_section: 10/10 PASS (file root for H1 + numberless H2; sub-namespace `§<D>.N [Example N]` for under-numbered-H2 atoms; §2.7 lock perfectly enforced)
- (f) sibling_index: 10/10 PASS (3 H1 sib=1, 1 H2 sib=6 EX/ex Example 6 positional, 1 H2 sib=1 numberless, 1 LIST_ITEM null, 2 TABLE_ROW null, 1 TABLE_HEADER null, 1 SENTENCE null)
- (g) heading_level: 10/10 PASS (3 H1 lvl=1, 2 H2 lvl=2, 5 non-HEADING null)
- (h) file prefix: 10/10 PASS `knowledge_base/`

---

*Findings filed by `pr-review-toolkit:silent-failure-hunter` AUDIT-mode pivot 2026-05-06.*
