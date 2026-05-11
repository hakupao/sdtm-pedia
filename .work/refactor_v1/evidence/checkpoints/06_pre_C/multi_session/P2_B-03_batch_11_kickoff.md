# P2 B-03 batch 11 — VARIABLE_INDEX slice #6 (L1412-1670)

> 创建: 2026-05-05 (post batch_10 PASS 100%; B-03b 自治连跑 #8, slice 6/7)
> 续 batch_10 last `md_varindex_a1280` → batch_11 起 **`md_varindex_a1281`**
> H3 sib chain 续: slice 5 sib=31..39 → slice 6 sib=40..52 (RELREC..SV; 13 H3)

---

## §0.5 grep checksum (slice #6)

| # | Claim | Match? |
|---|---|---|
| 1 | slice line range = L1412-1670 (259L) | ✓ |
| 2 | slice 内 H3 = 13 (L1412 RELREC sib=40 / L1419 RELSPEC sib=41 / L1428 RELSUB sib=42 / L1436 RP sib=43 / L1469 RS sib=44 / L1512 SC sib=45 / L1533 SE sib=46 / L1544 SM sib=47 / L1554 SR sib=48 / L1590 SS sib=49 / L1609 SU sib=50 / L1646 SUPPQUAL sib=51 / L1656 SV sib=52) | ✓ |
| 3 | slice 内 H1 = 0; H2 = 0; SENTENCE/LIST_ITEM/NOTE/fences/hr/blockquote = 0 | ✓ |
| 4 | slice 内 tables = 13 (含小 tables: RELREC/RELSPEC/RELSUB 各 ~5-6 行, SE/SM 各 ~8-10 行, SUPPQUAL 8 行) | ✓ |
| 5 | L1669 = last SV TABLE_ROW `\| SVUPDES \| ... \|`; L1670 = blank; L1671 = `### TA` (slice 7 起始) | ✓ post writer Rule B |
| 6 | atom_id 起 = `md_varindex_a1281` | ✓ |

---

## 1. Batch 任务

- file: `knowledge_base/VARIABLE_INDEX.md` slice L1412-1670
- 估 atoms ~210-260 (13 tables; 多小 table — relationship + special-purpose domains)
- atom_id 起 `md_varindex_a1281`
- batch_id: `P2_B-03_batch_11`

### Boundary critical (Rule A 6 atoms)

- a1281 L1412 H3 RELREC sib=40 (slice first; 4-digit atom_id 续)
- L1428 H3 RELSUB sib=42 OR L1469 H3 RS sib=44
- L1554 H3 SR sib=48
- L1656 H3 SV sib=52 (slice last H3)
- 1 TABLE_HEADER (e.g., 任一 13 表)
- 末原子 L1669 TABLE_ROW SV 表末 (`| SVUPDES | ... |`)

### parent_section + atom_type

同 batch_07-10 模式: 全 atoms parent=`§ 二、领域专属变量（仅 1 个域，共 1499 个），按域分组`. 仅 HEADING h_lvl=3 sib=40..52 / TABLE_HEADER / TABLE_ROW. 0 SENTENCE/LIST_ITEM/NOTE/FIGURE/CODE_LITERAL.

---

## 2. Dispatch

派 `general-purpose` writer; output `evidence/checkpoints/P2_B-03_batch_11_md_atoms.jsonl`. Rule A 派 `pr-review-toolkit:code-reviewer`.

---

*Kickoff written 2026-05-05 (B-03b #8, slice 6/7). §0.5 grep 6/6 ✓. 13 H3 (densest slice).*
