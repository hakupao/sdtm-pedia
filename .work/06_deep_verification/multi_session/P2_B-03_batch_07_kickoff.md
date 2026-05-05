# P2 B-03 batch 07 — VARIABLE_INDEX slice #2 (L289-534)

> 创建: 2026-05-05 (post batch_06 PASS 100%; B-03b 自治连跑 #4, slice 2/7)
> 续 batch_06 last atom_id `md_varindex_a253` → batch_07 起 **`md_varindex_a254`**
> H3 sib chain 续: slice 1 sib=1..7 (AE..CO) → slice 2 sib=8..15 (CP..EC)

---

## §0.5 grep checksum (slice #2)

| # | Claim | Match? |
|---|---|---|
| 1 | slice line range = L289-534 | ✓ |
| 2 | slice 内 H3 = 8 (L289 CP sib=8 / L348 CV sib=9 / L387 DA sib=10 / L411 DD sib=11 / L425 DM sib=12 / L457 DS sib=13 / L474 DV sib=14 / L490 EC sib=15) | ✓ |
| 3 | slice 内 H1 = 0; H2 = 0 (no chapter/section headers in slice) | ✓ |
| 4 | slice 内 inline NOTE = 0; NOTE-BQ = 0 | ✓ |
| 5 | slice 内 fences = 0; mermaid = 0 | ✓ |
| 6 | slice 内 horizontal rules = 0 | ✓ |
| 7 | slice 内 blockquote = 0 | ✓ |
| 8 | slice 内 LIST_ITEM = 0 | ✓ |
| 9 | slice end: L533 = last EC TABLE_ROW `| ECRFTDTC | ... |`; L534 = blank; L535 = `### EG` (slice 3 起始) | ✓ post writer Rule B verify |
| 10 | slice 内 tables = 8 (CP/CV/DA/DD/DM/DS/DV/EC each 1 table) | ✓ |
| 11 | atom_id 起始 = `md_varindex_a254` (cross-slice continuity) | ✓ |

---

## 1. Batch 任务

- **文件**: `knowledge_base/VARIABLE_INDEX.md`
- **切片**: L289-534 (slice #2 of 7)
- **估 atoms**: ~210-260 (8 tables, ~200 pipe-rows in slice = ~200 TABLE_ROW + 8 TABLE_HEADER + 8 H3 = ~216)
- **atom_id 起**: `md_varindex_a254` (续 batch_06)
- **batch_id**: `P2_B-03_batch_07`

### 1.1 Source structure

```
L289:  ### CP — Cell Phenotype Findings (Findings)        ← H3 sib=8 (cumulative across slices)
L291-292: TABLE_HEADER
L293-347: TABLE_ROW × N
L348:  ### CV — Cardiovascular System Findings (Findings) ← H3 sib=9
... (similar pattern for DA/DD/DM/DS/DV/EC)
L490:  ### EC — Exposure as Collected (Interventions)     ← H3 sib=15
L492-493: TABLE_HEADER
L494-533: TABLE_ROW × N (last EC row L533)
L534:  blank line (skip, no atom)
```

### 1.2 Boundary critical (Rule A 6 atoms)

- a254 L289 H3 `### CP — Cell Phenotype Findings (Findings)` sib=8 (slice 2 first atom; verify cross-slice atom_id continuity + cross-slice sib_index continuity)
- L348 OR L425 H3 (CV sib=9 OR DM sib=12 — stratified pick)
- 1 TABLE_HEADER (e.g., L291-292 CP)
- 1 TABLE_ROW (any non-CP)
- L490 H3 EC sib=15 (slice last H3)
- 末原子 L533 TABLE_ROW EC last row (slice 末)

---

## 2. parent_section convention

同 batch_06 §2:
- 8 H3 atom emit parent=`§ 二、领域专属变量（仅 1 个域，共 1499 个），按域分组` sib=8..15
- All H3 children (table rows) parent=`§ 二、领域专属变量（仅 1 个域，共 1499 个），按域分组`

---

## 3. atom_type 决策

| Source | atom_type | 注 |
|---|---|---|
| L289/348/387/411/425/457/474/490 8 H3 | HEADING h_lvl=3 sib=8..15 | parent=`§ 二、领域专属变量（仅 1 个域，共 1499 个），按域分组` |
| 8 domain TABLE_HEADER (2-row each) | TABLE_HEADER span ≤1 | parent=`§ 二、领域专属变量（仅 1 个域，共 1499 个），按域分组` |
| TABLE_ROW × ~200 | TABLE_ROW | parent=`§ 二、领域专属变量（仅 1 个域，共 1499 个），按域分组` |

无 SENTENCE / LIST_ITEM / NOTE / FIGURE / CODE_LITERAL / blockquote in slice.

---

## 4. Dispatch + Rule A

派 `general-purpose` writer; output `evidence/checkpoints/P2_B-03_batch_07_md_atoms.jsonl`. Rule A 派 `pr-review-toolkit:code-reviewer`. boundary 6 + stratified 4 (TABLE_HEADER 1 / TABLE_ROW 1 / HEADING H3 1 stratified domain / TABLE_ROW 1 from another non-CP domain).

---

*Kickoff written 2026-05-05 (B-03b #4, VARIABLE_INDEX slice 2/7). §0.5 grep 11/11 ✓ (含 cross-slice continuity claims). atom_id continuity 254..~510 估.*
