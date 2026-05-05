# P2 B-03 batch 09 — VARIABLE_INDEX slice #4 (L817-1108)

> 创建: 2026-05-05 (post batch_08 PASS 100%; B-03b 自治连跑 #6, slice 4/7)
> 续 batch_08 last `md_varindex_a733` → batch_09 起 **`md_varindex_a734`**
> H3 sib chain 续: slice 3 sib=16..23 → slice 4 sib=24..30 (LB..MS)

---

## §0.5 grep checksum (slice #4)

| # | Claim | Match? |
|---|---|---|
| 1 | slice line range = L817-1108 (292L) | ✓ |
| 2 | slice 内 H3 = 7 (L817 LB sib=24 / L876 MB sib=25 / L919 MH sib=26 / L946 MI sib=27 / L980 MK sib=28 / L1019 ML sib=29 / L1052 MS sib=30) | ✓ |
| 3 | slice 内 H1 = 0; H2 = 0; SENTENCE/LIST_ITEM/NOTE/fences/hr/blockquote = 0 | ✓ |
| 4 | slice 内 tables = 7 | ✓ |
| 5 | L1107 = last MS TABLE_ROW; L1108 = blank; L1109 = `### NV` (slice 5 起始) | ✓ post writer Rule B |
| 6 | atom_id 起 = `md_varindex_a734` | ✓ |

---

## 1. Batch 任务

- file: `knowledge_base/VARIABLE_INDEX.md` slice L817-1108
- 估 atoms ~230-280 (7 tables, similar density)
- atom_id 起 `md_varindex_a734`
- batch_id: `P2_B-03_batch_09`

### Boundary critical (Rule A 6 atoms)

- a734 L817 H3 LB sib=24 (slice first)
- L876 H3 MB sib=25 OR L919 H3 MH sib=26
- L946 H3 MI sib=27 OR L980 H3 MK sib=28
- L1052 H3 MS sib=30 (slice last H3)
- 1 TABLE_HEADER
- 末原子 L1107 TABLE_ROW MS 表末 (`| MSEVINTX | ... |`)

### parent_section + atom_type

同 batch_07/08: 全 atoms parent=`§ 二、领域专属变量（仅 1 个域，共 1499 个），按域分组`. 仅 HEADING h_lvl=3 sib=24..30 / TABLE_HEADER / TABLE_ROW.

---

## 2. Dispatch

派 `general-purpose` writer; output `evidence/checkpoints/P2_B-03_batch_09_md_atoms.jsonl`. Rule A 派 `pr-review-toolkit:code-reviewer`. boundary 6 + stratified 4.

---

*Kickoff written 2026-05-05 (B-03b #6, slice 4/7). §0.5 grep 6/6 ✓.*
