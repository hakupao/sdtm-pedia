# P2 B-03 batch 06 — VARIABLE_INDEX slice #1 (L1-288)

> 创建: 2026-05-05 (post batch_05 ROUTING PASS 100%; B-03b 自治连跑 #3, VARIABLE_INDEX slice 1/7)
> 父 kickoff: `multi_session/P2_B-03_kickoff.md` (umbrella)
> atom_id prefix LOCKED in batch_04: `md_varindex_a001`+ for batch_06; **续号 across batches 07-12** (NOT restart per slice)

---

## §0 跨 batch atom_id 连续性约定 (B-03b VARIABLE_INDEX 7-slice rule)

- batch_06 → `md_varindex_a001` 起
- batch_07 起始 atom_id = batch_06 last atom_id + 1
- batch_08 起始 = batch_07 last + 1
- ...
- batch_12 末原子 atom_id 即 VARIABLE_INDEX 全文 atom 总数 (估 ~1500-2000)

每 batch 完成后 main session 必读 writer DONE report 取 last atom_id, 下 batch dispatch 时 hardcode 起始号.

---

## §0.5 Kickoff numeric claim grep checksum (slice #1 specific)

| # | Claim | Match? |
|---|---|---|
| 1 | VARIABLE_INDEX 全文 = 2005 lines | ✓ |
| 2 | 本 slice line range = L1-288 (含 §使用说明 + §一 通用变量 + §二 AE→CO 7 H3) | ✓ |
| 3 | slice 内 H1 = 1 (L1) | ✓ |
| 4 | slice 内 H2 = 2 (L6 §使用说明 numberless + L16 §一 numbered "一、") | ✓ |
| 5 | slice 内 H3 = 7 (L51 AE / L110 AG / L148 BE / L171 BS / L204 CE / L236 CM / L277 CO) | ✓ |
| 6 | slice 内 inline NOTE = 0 | ✓ |
| 7 | slice 内 NOTE-BQ = 0 | ✓ |
| 8 | slice 内 blockquote SENTENCE = 3 (L3, L4 metadata + L45 footnote `> \* Core...`) | ✓ |
| 9 | slice 内 LIST_ITEM `^- ` = 3 (L10/11/12 §使用说明) | ✓ |
| 10 | slice 内 horizontal rules `---` = 2 (L14 + L47) | ✓ |
| 11 | slice 内 tables = 8 (1 §一通用变量 24-row + 7 §二 domain tables AE/AG/BE/BS/CE/CM/CO) | ✓ |
| 12 | slice 内 fences = 0 | ✓ |
| 13 | slice 内 已 atomized atoms = 0 (pre-batch) | ✓ |
| 14 | ~~line 288 = `| CODY | ... | — |` (CO 表末行)~~ → **CORRECTION 2026-05-05**: line 287 = CODY 表末 / line 288 = 空白 / line 289 = `### CP` (kickoff §0.5 row #14 had off-by-1; writer Rule B emit source-truth: last atom line_end=287; reviewer §R-D1 confirmed) | ✓ post-correction |
| 15 | line 289 = `### CP — Cell Phenotype Findings (Findings)` (slice 2 起始) | ✓ |

---

## 1. Batch 任务

- **文件**: `knowledge_base/VARIABLE_INDEX.md`
- **切片**: **L1-288** (slice #1 of 7)
- **估 atoms**: ~250-310 (table-heavy: ~270 pipe-rows in slice / 1788 total × 288/2005 ≈ 257 pipe rows; 加 17 HEADING + 3 SENTENCE blockquote + 3 LIST_ITEM + 1-2 narrative SENTENCE + 8 TABLE_HEADER × 2-row = atoms ~280)
- **atom_id 起始**: `md_varindex_a001`
- **batch_id**: `P2_B-03_batch_06`

### 1.1 Source structure

```
L1:    # SDTM Variable Index                                          ← H1 sib=1
L3-4:  > 自动生成... / > 唯一变量数: 1523...                           ← 2 SENTENCE blockquote
L6:    ## 使用说明                                                     ← H2 sib=1 numberless
L8:    narrative SENTENCE
L10-12: LIST_ITEM × 3 (- **通用变量** / - **领域专属变量** / - **CT 交叉引用**)
L14:   ---                                                              ← skip hr
L16:   ## 一、通用变量（出现在 2+ 个域，共 24 个）                       ← H2 sib=2 numbered "一、"
L18-19: TABLE_HEADER (header + alignment)
L20-43: TABLE_ROW × 24 (24 通用变量)
L45:   > \* Core 值后带星号表示...                                       ← SENTENCE blockquote (footnote, NOT NOTE)
L47:   ---                                                              ← skip hr
L49:   ## 二、领域专属变量（仅 1 个域，共 1499 个），按域分组            ← H2 sib=3 numbered "二、"
L51:   ### AE — Adverse Events (Events)                                ← H3 sib=1 under §二
L53-54: TABLE_HEADER
L55-108: TABLE_ROW × 54 (AE 域专属变量)
L110:  ### AG — Procedure Agents (Interventions)                       ← H3 sib=2
... (重复 BE/BS/CE/CM/CO H3 sib=3..7 with their tables)
L288:  | CODY | ... | (CO 表末行, slice 末)
```

### 1.2 Boundary critical (Rule A 6 atoms)

- a001 L1 H1 (新 file H1, atom_id LOCK起 `md_varindex_a001`)
- L3 OR L4 SENTENCE blockquote
- L16 H2 numbered "一、通用变量..." sib=2 (验 numbered H2 + 中文-numbered prefix `一、` retained byte-exact)
- L45 SENTENCE blockquote footnote `> \* Core...` (验 atom_type=SENTENCE NOT NOTE; verbatim含 `> \*` byte-exact 含 backslash-escape)
- L51 H3 `### AE — Adverse Events (Events)` sib=1 under §二 (验 numbered H2 → H3 chain)
- 末原子 L288 TABLE_ROW (CO 表末)

---

## 2. parent_section convention (B-03b VARIABLE_INDEX lock)

- chapter root: `§ SDTM Variable Index`
- L1 H1 atom parent=chapter root
- L3-4 blockquote parent=chapter root
- 4 H2 sib chain (slice 1 含前 3, slice 7 含 §三):
  - `## 使用说明` (L6 numberless) sib=1, atom parent=chapter root, children parent=`§ 使用说明`
  - `## 一、通用变量（出现在 2+ 个域，共 24 个）` (L16 numbered "一、") sib=2, atom parent=chapter root, children parent=`§ 一、通用变量（出现在 2+ 个域，共 24 个）`
  - `## 二、领域专属变量（仅 1 个域，共 1499 个），按域分组` (L49 numbered "二、") sib=3, atom parent=chapter root, children parent=`§ 二、领域专属变量（仅 1 个域，共 1499 个），按域分组`
  - `## 三、CDISC Controlled Terminology 交叉引用（共 135 个 CT Code）` (L1867 numbered "三、") sib=4 — 在 slice 7 处理
- 63 H3 全 under §二 (slice 1 含 7 H3 sib=1..7); H3 atom emit parent=`§ 二、领域专属变量...`; H3 children (table) parent=`§ 二、领域专属变量...` (NOT 父 H3, v1.9 baseline)
- D8 不触发 (无 `## Overview`)

**slice 跨 batch H3 sib_index 连续性**: H3 sib chain 在 §二 内 1..63 全 cycle (跨 slices 1-7 连续编号; AE=1, AG=2, ..., VS=63). 每 slice writer dispatch 时 hardcode 起始 sib (slice 1 起=1; slice 2 起=8 后续 etc).

---

## 3. atom_type 决策 关键

| Source | atom_type | 注 |
|---|---|---|
| L1 H1 | HEADING h_lvl=1 sib=1 | parent=chapter root |
| L3 `> 自动生成，勿手动编辑 \| 生成日期: 2026-04-16` | SENTENCE | `> ` prefix byte-exact; NOT NOTE |
| L4 `> 唯一变量数: 1523 \| 条目总数: 1917 \| 覆盖域: 63` | SENTENCE | `> ` prefix |
| L6/16/49 H2 (1 numberless `## 使用说明` + 2 numbered `## 一、` + `## 二、`) | HEADING h_lvl=2 sib=1..3 | parent=chapter root |
| L8 `查询变量时...` | SENTENCE | parent=`§ 使用说明` |
| L10-12 `- **通用变量** ...` | LIST_ITEM × 3 | full `- ` prefix; inline-bold; parent=`§ 使用说明` |
| L14/47 `---` 2 hr | **DO NOT emit** | skip |
| L18-19 TABLE_HEADER (§一 通用变量) | TABLE_HEADER 2-row span ≤1 | parent=`§ 一、通用变量（出现在 2+ 个域，共 24 个）` |
| L20-43 TABLE_ROW × 24 | TABLE_ROW | parent=`§ 一、通用变量（出现在 2+ 个域，共 24 个）` |
| L45 `> \* Core 值后带星号表示...` | SENTENCE | parent=`§ 一、通用变量（出现在 2+ 个域，共 24 个）`; verbatim 含 `> ` prefix + `\*` backslash byte-exact |
| L51/110/148/171/204/236/277 H3 (AE/AG/BE/BS/CE/CM/CO) | HEADING h_lvl=3 sib=1..7 (slice 内连续 1..7; 全 cycle 1..63) | parent=`§ 二、领域专属变量（仅 1 个域，共 1499 个），按域分组` |
| 7 domain TABLE_HEADER + TABLE_ROW × N | TABLE_HEADER + TABLE_ROW | parent=`§ 二、领域专属变量（仅 1 个域，共 1499 个），按域分组` |

---

## 4. Dispatch + Rule A

派 `general-purpose` writer; 输出 `evidence/checkpoints/P2_B-03_batch_06_md_atoms.jsonl`. Rule A 派 `pr-review-toolkit:code-reviewer`. boundary 6 + stratified 4 (TABLE_ROW 1 / SENTENCE blockquote 1 / HEADING H3 1 / TABLE_HEADER 1).

---

*Kickoff written 2026-05-05 (B-03b #3, VARIABLE_INDEX slice 1/7). §0.5 grep 15/15 ✓. v1.9.1 §D-1 compliance. atom_id sequential continuous across 7 slices.*
