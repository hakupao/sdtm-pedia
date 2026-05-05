# P2 B-03 batch 04 — Multi-Session Kickoff (INDEX.md, B-03b 1st batch + atom_id prefix lock)

> 创建: 2026-05-05 (post B-03 umbrella §0.5 correction + B-03a SKIP; B-03b 自治连跑 1st batch)
> 父 kickoff: `multi_session/P2_B-03_kickoff.md` (umbrella post-correction §3 B-03b #1)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.1.md` + `P0_reviewer_v1.9.1.md`
> 路由词: `P2 bulk B-03b 自治连跑 直到 mini-audit PASS`
> **本 batch = top-level 3 文件 1st atomization** → atom_id prefix convention LOCK (per kickoff §10.2 halt condition #6 解除)

---

## §0 atom_id prefix convention LOCK (per kickoff §10.2 halt #6)

| File | atom_id prefix | 起始 | sequential rule |
|---|---|---|---|
| `knowledge_base/INDEX.md` | `md_index_a` | `md_index_a001` | restart a001 |
| `knowledge_base/ROUTING.md` | `md_routing_a` | `md_routing_a001` | restart a001 |
| `knowledge_base/VARIABLE_INDEX.md` | `md_varindex_a` | `md_varindex_a001` | **跨 batch_06..12 切片 sequential 续号** (NOT restart per slice) |

LOCKED 2026-05-05 by main orchestrator. v1.9.1 §C-3 atom_id pattern `^md_<file_stem>_a\d{3,}$` 兼容. 一旦此 batch dispatch, prefix 即 freeze for subsequent B-03b batches.

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1)

注: grep regex 含 `\s*` 兼容 JSON formatting variants (post B-03a drift learning).

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | INDEX 行数 = 195 | `wc -l knowledge_base/INDEX.md` | ✓ 195 |
| 2 | H1 = 1 (L1) | `grep -cE "^# " ...` | ✓ 1 |
| 3 | H2 = 6 (L6/13/24/37/144/188 — 全 numberless) | `grep -nE "^## " ...` | ✓ 6 |
| 4 | H3 = 10 (7 under §Domains + 3 under §Terminology) | `grep -cE "^### " ...` | ✓ 10 |
| 5 | inline NOTE = 0 | `grep -nE "^\*\*Note:\*\*" ...` | ✓ 0 |
| 6 | NOTE-BQ = 0 | `grep -nE "^>\s+\*\*Note:\*\*" ...` | ✓ 0 |
| 7 | bold-caption `^\*\*[A-Z]` = 0 | `grep -cE "^\*\*[A-Z]" ...` | ✓ 0 |
| 8 | pipe-row = 122 | `grep -cE "^\|" ...` | ✓ 122 |
| 9 | LIST_ITEM `^- ` = 5 | `grep -cE "^- " ...` | ✓ 5 |
| 10 | numbered-list `^N\. ` = 0 | `grep -cE "^[0-9]+\. " ...` | ✓ 0 |
| 11 | fences = 0 (no mermaid; no FIGURE expected) | `grep -cE '^```' ...` | ✓ 0 |
| 12 | horizontal rules `---` = 4 (L11/35/142/186) | `grep -cE "^---$" ...` | ✓ 4 |
| 13 | blockquote SENTENCE (non-NOTE) lines = 2 (L3/4 metadata blockquote) | `grep -cE "^> " ...` | ✓ 2 |
| 14 | INDEX 现有 atoms in md_atoms.jsonl = 0 (pre-batch) | `grep -cE '"file":\s*"knowledge_base/INDEX.md"' md_atoms.jsonl` | ✓ 0 |
| 15 | tables (TABLE_HEADER count) = 11 (1 Model + 1 Chapters + 7 Domains class tables + 1 Core Term + 1 Source Documents — Questionnaires + Supplementary 各 1 narrative paragraph + 0 table per L174-184) | source 视察 | ✓ 11 |

---

## 1. 必读 (按序)

1. `multi_session/P2_B-03_kickoff.md` (umbrella post-correction; §3 B-03b 起点 + §4 batch table batch_04 row + §10.2 halt 条件)
2. `subagent_prompts/P0_writer_md_v1.9.1.md` 全文 (尤其 §D-2/§D-4/§D-5 + Hook A4)
3. `subagent_prompts/P0_reviewer_v1.9.1.md`
4. `evidence/failures/B-03a_drift_attempt/FAILURE_REPORT.md` (B-03a drift cautionary tale; §0.5 grep regex `\s*` 兼容 lesson)

---

## 2. Batch 任务

### 2.1 Target

- **文件**: `knowledge_base/INDEX.md`
- **切片**: **全文 1-195 (单 dispatch, 不切片)**
- **估 atoms**: ~120-160 (table-heavy 122 pipe-rows = ~110 TABLE_ROW + 11 TABLE_HEADER ~= 121; 加 17 HEADING + 5 LIST_ITEM + 2 blockquote + ~10 narrative SENTENCE = ~155; 估 ~120-160 后 sub-line split / table cell density 调整)
- **atom_id 起始**: `md_index_a001`
- **batch_id**: `P2_B-03_batch_04`

### 2.2 Source structure prefix

```
L1:    # SDTM Knowledge Base — Index                    ← H1 sib=1
L3-4:  > Generated... / > Total: **293 files** (...)    ← SENTENCE blockquote (NOT NOTE; no Note/Exception prefix); verbatim 含 `> ` byte-exact
L6:    ## Quick Lookup                                  ← H2 sib=1 numberless
L8-9:  - **问题路由** → ... / - **按变量名查询** → ...   ← LIST_ITEM × 2; bold inline retained
L11:   ---                                              ← horizontal rule (skip)
L13:   ## Model (SDTM v2.0 Conceptual Model)            ← H2 sib=2 numberless
L15-22: TABLE_HEADER + TABLE_ROW × 6
L24:   ## Chapters (SDTMIG v3.4 Implementation Guide)   ← H2 sib=3
L26-33: TABLE_HEADER + TABLE_ROW × 6
L35:   ---                                              ← horizontal rule (skip)
L37:   ## Domains (63 domains)                          ← H2 sib=4
L39:   narrative SENTENCE
L40-42: LIST_ITEM × 3 (- **spec.md** / - **assumptions.md** / - **examples.md**)
L44:   ### Special-purpose Domains                      ← H3 sib=1 under §Domains
L46-... TABLE_HEADER + TABLE_ROW × N (Special-purpose 表)
L54:   ### Interventions Domains                        ← H3 sib=2
... (7 H3 under §Domains: Special-purpose / Interventions / Events / Findings / Trial Design / Relationship / Study Reference)
L142:  ---                                              ← horizontal rule (skip)
L144:  ## Terminology (91 files)                        ← H2 sib=5
L146:  narrative SENTENCE
L148:  ### Core Terminology (42 files)                  ← H3 sib=1 under §Terminology RESTART
L150-172: TABLE_HEADER + TABLE_ROW × ~21 (Core Term 表)
L174:  ### Questionnaires Terminology (43 files)        ← H3 sib=2
L176:  narrative SENTENCE w/ link
L178:  narrative SENTENCE
L180:  ### Supplementary Terminology (6 files)          ← H3 sib=3
L182:  narrative SENTENCE
L184:  narrative SENTENCE
L186:  ---                                              ← horizontal rule (skip)
L188:  ## Source Documents                              ← H2 sib=6 numberless
L190-195: TABLE_HEADER + TABLE_ROW × 4 (Source Doc 表; file 末)
```

### 2.3 Boundary critical (Rule A 必入 sample, 6 atoms)

- **a001** L1 H1 `# SDTM Knowledge Base — Index` (新 file H1)
- **L3 SENTENCE blockquote** `> Generated from SDTM v2.0 ...` (verify atom_type=SENTENCE NOT NOTE; verbatim 含 `> ` prefix byte-exact)
- **L6 H2 `## Quick Lookup` numberless** sib=1 (验 H2 sib chain start under chapter root)
- **L40 OR L41 OR L42 LIST_ITEM** `- **spec.md** — ...` (验 inline-bold + full `- ` prefix retain)
- **L148 H3 `### Core Terminology (42 files)` under §Terminology** sib=1 RESTART (验 H3 sib RESTART under new H2)
- **末原子 L195 TABLE_ROW** Source Documents 表末 (file 末)

---

## 3. parent_section canonical format (本 batch lock)

INDEX H1 = `# SDTM Knowledge Base — Index` (numberless, no chapter number). 沿用 spaced format (B-01 model/06 + 本 batch 01 model/03 precedent):

- **chapter root**: `§ SDTM Knowledge Base — Index`
- **L1 H1 atom**: parent_section = chapter root (自指)
- **L3-4 blockquote SENTENCE**: parent = chapter root
- **6 H2 sib chain** (全 numberless):
  - `## Quick Lookup` (L6) sib=1, atom emit parent=chapter root, children parent=`§ Quick Lookup`
  - `## Model (SDTM v2.0 Conceptual Model)` (L13) sib=2, children parent=`§ Model (SDTM v2.0 Conceptual Model)`
  - `## Chapters (SDTMIG v3.4 Implementation Guide)` (L24) sib=3, children parent=`§ Chapters (SDTMIG v3.4 Implementation Guide)`
  - `## Domains (63 domains)` (L37) sib=4, children parent=`§ Domains (63 domains)`
  - `## Terminology (91 files)` (L144) sib=5, children parent=`§ Terminology (91 files)`
  - `## Source Documents` (L188) sib=6, children parent=`§ Source Documents`
- **H3 sib chain**:
  - 7 H3 under §Domains (Special-purpose / Interventions / Events / Findings / Trial Design / Relationship / Study Reference) sib=1..7
  - 3 H3 under §Terminology (Core / Questionnaires / Supplementary) sib=1..3 RESTART under §Terminology
  - H3 自身 emit parent=父 H2
  - H3 children (table rows etc) parent=父 H2 (NOT 父 H3, v1.9 baseline)
- **D8 不触发** (无 `## Overview` numberless H2; INDEX 6 H2 全 numberless 但都是 normal sections, 各自有 own parent_section, 不 inherit chapter root)

---

## 4. Hook A4 inline (FIGURE)

INDEX 0 mermaid → 0 FIGURE 预期. Hook A4 trivially satisfied.

---

## 5. atom_type 决策 (本 batch 关键 cases)

| Source | atom_type | 注 |
|---|---|---|
| L1 H1 | HEADING h_lvl=1 sib=1 | parent=chapter root |
| L3-4 `> Generated... / > Total: **293 files** ...` | SENTENCE × 2 (各 line 1 atom; 含 inline-bold) | parent=chapter root; verbatim 含 `> ` byte-exact prefix; NOT NOTE (无 Note/Exception 前缀) |
| L6/13/24/37/144/188 `## ...` numberless H2 | HEADING h_lvl=2 sib=1..6 | parent=chapter root |
| L8-9 `- **问题路由** → ...` / `- **按变量名查询** → ...` | LIST_ITEM × 2 | parent=`§ Quick Lookup`; full `- ` prefix retained; inline `**...**` byte-exact |
| L11/35/142/186 `---` | **不 emit** (skip horizontal rule, 模 batch_02 model/05 L9/L224 决策) | n/a |
| L40-42 `- **spec.md** — ...` etc | LIST_ITEM × 3 | parent=`§ Domains (63 domains)`; full `- ` prefix |
| 7 H3 under §Domains (L44/54/66/78/115/127/136) | HEADING h_lvl=3 sib=1..7 | parent=`§ Domains (63 domains)` |
| 3 H3 under §Terminology (L148/174/180) | HEADING h_lvl=3 sib=1..3 RESTART | parent=`§ Terminology (91 files)` |
| 11 tables: Model L15-22 + Chapters L26-33 + 7 Domains H3 tables + Core Terminology L150-172 + Source Documents L190-195 | TABLE_HEADER (2-row span ≤1 per §C-5) + TABLE_ROW × N | parent=父 H2 |
| narrative SENTENCE (L39, L146, L176, L178, L182, L184) | SENTENCE | parent=父 H2 |

---

## 6. Dispatch 模板

派 `general-purpose` 单 dispatch (FALLBACK peer-alternative). Dispatch 含:
- file=`knowledge_base/INDEX.md`, 1-195 全文
- atom_id `md_index_a001`+ (LOCKED §0)
- batch_id=`P2_B-03_batch_04`
- 输出: `evidence/checkpoints/P2_B-03_batch_04_md_atoms.jsonl`
- 23 hooks self-validate
- §5 atom_type 决策 reminders 全粘
- horizontal rules `---` skip (4 instances L11/35/142/186)
- 0 FIGURE / 0 NOTE / 0 NOTE-BQ / 0 bold-caption 预期

---

## 7. Rule A 跟进

派 `pr-review-toolkit:code-reviewer`:
- 输入: `evidence/checkpoints/P2_B-03_batch_04_md_atoms.jsonl`
- 输出: `rule_a_P2_B-03_batch_04_verdicts.jsonl` + `_summary.md`
- gate ≥90% PASS
- **boundary 必入 sample (6 atoms)** per §2.3
- **stratified 4 atoms 余样**: TABLE_HEADER 1 / TABLE_ROW 1 (任一 11 表) / SENTENCE 1 (narrative L39 OR L146) / HEADING H2 1 (L13 OR L37 — 验 sib chain numberless)

---

## 8. PASS 后 append

- cat 输出 >> `md_atoms.jsonl` (post 2867; post batch_04 应 ~2987-3027)
- `_progress.json` + `audit_matrix.md` + `trace.jsonl` 暂不更新 (B-03b 收尾时一并写)

---

## 9. 失败处理

若 dispatch 或 Rule A FAIL 走 §10.2 halt 条件. 写 `evidence/failures/P2_B-03_batch_04_attempt_<M>.md`.

---

*Kickoff written 2026-05-05 (B-03b 1st batch, INDEX.md, atom_id prefix LOCK). §0.5 grep checksum 15/15 verified byte-exact (含 `\s*` 兼容). v1.9.1 §D-1 mandatory compliance. Post B-03a drift learning.*
