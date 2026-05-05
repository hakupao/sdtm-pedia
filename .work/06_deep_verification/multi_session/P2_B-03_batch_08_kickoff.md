# P2 B-03 batch 08 — VARIABLE_INDEX slice #3 (L535-816)

> 创建: 2026-05-05 (post batch_07 PASS 100%; B-03b 自治连跑 #5, slice 3/7)
> 续 batch_07 last `md_varindex_a475` → batch_08 起 **`md_varindex_a476`**
> H3 sib chain 续: slice 2 sib=8..15 → slice 3 sib=16..23 (EG..IS)

---

## §0.5 grep checksum (slice #3)

| # | Claim | Match? |
|---|---|---|
| 1 | slice line range = L535-816 (282L) | ✓ |
| 2 | slice 内 H3 = 8 (L535 EG sib=16 / L575 EX sib=17 / L612 FA sib=18 / L639 FT sib=19 / L674 GF sib=20 / L728 HO sib=21 / L756 IE sib=22 / L767 IS sib=23) | ✓ |
| 3 | slice 内 H1 = 0; H2 = 0 | ✓ |
| 4 | slice 内 inline NOTE = 0; NOTE-BQ = 0; fences = 0; hr = 0; blockquote = 0; LIST_ITEM = 0 | ✓ |
| 5 | slice 内 tables = 8 (EG/EX/FA/FT/GF/HO/IE/IS) | ✓ |
| 6 | L815 = last IS TABLE_ROW `\| ISRFTDTC \| ... \|`; L816 = blank; L817 = `### LB` (slice 4 start) | ✓ post writer Rule B verify |
| 7 | atom_id 起 = `md_varindex_a476` | ✓ |

---

## 1. Batch 任务

- file: `knowledge_base/VARIABLE_INDEX.md` slice L535-816
- 估 atoms ~220-260 (8 tables, 同 slice 2 模式)
- atom_id 起 `md_varindex_a476`
- batch_id: `P2_B-03_batch_08`

### Boundary critical (Rule A 6 atoms)

- a476 L535 H3 EG sib=16 (slice 3 first atom)
- L612 OR L674 H3 (FA sib=18 OR GF sib=20)
- L728 H3 HO sib=21
- L767 H3 IS sib=23 (slice last H3)
- 1 TABLE_HEADER (任一 8 表)
- 末原子 L815 TABLE_ROW IS 表末

### parent_section convention

同 batch_07: 全 atoms parent=`§ 二、领域专属变量（仅 1 个域，共 1499 个），按域分组` (含 8 H3 atom 自身 + table children, NOT parent H3)

### atom_type 决策

仅 3 种: HEADING h_lvl=3 sib=16..23 / TABLE_HEADER / TABLE_ROW. 无 SENTENCE/LIST_ITEM/NOTE/FIGURE/CODE_LITERAL/blockquote/hr.

---

## 2. Dispatch + Rule A

派 `general-purpose` writer; output `evidence/checkpoints/P2_B-03_batch_08_md_atoms.jsonl`. Rule A 派 `pr-review-toolkit:code-reviewer`. boundary 6 + stratified 4.

---

*Kickoff written 2026-05-05 (B-03b #5, VARIABLE_INDEX slice 3/7). §0.5 grep 7/7 ✓.*
