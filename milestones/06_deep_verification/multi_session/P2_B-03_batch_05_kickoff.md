# P2 B-03 batch 05 — Multi-Session Kickoff (ROUTING.md, B-03b #2)

> 创建: 2026-05-05 (post batch_04 INDEX PASS 100%; B-03b 自治连跑 #2)
> 父 kickoff: `multi_session/P2_B-03_kickoff.md` (umbrella post-correction)
> atom_id prefix LOCKED in batch_04 — 本 batch 用 `md_routing_a001`+

---

## §0.5 Kickoff numeric claim grep checksum (含 `\s*` 兼容)

| # | Claim | Match? |
|---|---|---|
| 1 | ROUTING 行数 = 211 | ✓ |
| 2 | H1 = 1 (L1) | ✓ |
| 3 | H2 = 4 (L8 §快速入口 numberless + L19 §路由规则 numberless + L187 §多文件查询策略 numberless + L200 §文件类型速查 numberless) | ✓ |
| 4 | H3 = 7 (L21/41/65/92/119/137/163, 全 numbered `### N. <Title>` under §路由规则) | ✓ |
| 5 | inline NOTE = 0; NOTE-BQ = 0 | ✓ |
| 6 | 标准 bold-caption `^\*\*[A-Z]` = 0 (Chinese chars 不 match `[A-Z]`); 实际 8 bold-prefix SENTENCE patterns: 7 `**问法示例**:` + 1 `**不要一次读取...**` | ✓ |
| 7 | pipe-row = 16 (2 tables: L10-15 快速入口 6-row + L202-211 文件类型速查 10-row) | ✓ |
| 8 | numbered LIST_ITEM `^N\.` = 4 (L191-194 § 多文件查询策略 1-4) | ✓ |
| 9 | code fences `^```` = 14 (7 code blocks under §路由规则 H3 sub-sections; L25-39/45-63/69-90/96-117/123-135/141-161/167-183) | ✓ |
| 10 | horizontal rules = 4 (L6/17/185/198) | ✓ |
| 11 | blockquote SENTENCE = 2 (L3 + L4 metadata; non-NOTE) | ✓ |
| 12 | ROUTING 现有 atoms in md_atoms.jsonl = 0 | ✓ |
| 13 | tables = 2 (TABLE_HEADER count) | ✓ |

---

## 1. 必读

1. `multi_session/P2_B-03_batch_04_kickoff.md` (atom_id LOCK precedent)
2. `multi_session/P2_B-03_kickoff.md` (umbrella)
3. `subagent_prompts/P0_writer_md_v1.9.1.md` (尤其 §D-5 bold-caption SENTENCE; §C 代码块 CODE_LITERAL handling 沿 v1.9 baseline)

---

## 2. Batch 任务

- **文件**: `knowledge_base/ROUTING.md`
- **切片**: 全文 1-211 单 dispatch
- **估 atoms**: ~80-110 (HEADING 12 + SENTENCE blockquote 2 + bold-prefix SENTENCE 8 + narrative SENTENCE ~10 + LIST_ITEM 4 + TABLE_HEADER 2 + TABLE_ROW 12 + CODE_LITERAL 7 = ~57; 加 sub-line splits ~20-50 = ~80-110)
- **atom_id 起始**: `md_routing_a001`
- **batch_id**: `P2_B-03_batch_05`

### 2.1 Source structure

```
L1:    # SDTM Knowledge Base — Query Routing Guide       ← H1 sib=1
L3-4:  > AI 在回答... / > 不要猜测...                     ← 2 SENTENCE blockquote (含 inline-bold L3, NO Note prefix)
L6:    ---                                                 ← skip hr
L8:    ## 快速入口                                         ← H2 sib=1 numberless
L10-15: TABLE (header + 4 rows)
L17:   ---                                                 ← skip hr
L19:   ## 路由规则                                         ← H2 sib=2 numberless
L21:   ### 1. 变量定义类                                  ← H3 sib=1 (numbered "1. "; 沿 model/05 §5.1.1 numbered H3 模式 — 但 numbered prefix 形态)
L23:   **问法示例**: "...?, ...?"                         ← SENTENCE bold-prefix per §D-5
L25-39: code block (CODE_LITERAL atom; verbatim 含 ```...``` fences + body)
L41-63: ### 2. 编码/术语类 + L43 SENTENCE + code block
... (7 H3 同模 1..7)
L185:  ---                                                 ← skip hr
L187:  ## 多文件查询策略                                   ← H2 sib=3 numberless
L189:  narrative SENTENCE
L191-194: LIST_ITEM × 4 numbered (`1. **先定位**:` ... `4. **通用规则兜底**:`)
L196:  **不要一次读取超过 3 个文件**...                    ← SENTENCE bold-prefix per §D-5
L198:  ---                                                 ← skip hr
L200:  ## 文件类型速查                                     ← H2 sib=4 numberless
L202-211: TABLE (header + 8 rows; file 末)
```

### 2.2 Boundary critical (Rule A 6 atoms)

- a001 L1 H1
- L3 OR L4 SENTENCE blockquote (verify `> ` byte-exact, atom_type=SENTENCE NOT NOTE)
- L21 H3 `### 1. 变量定义类` numbered sib=1 (验 numbered H3 + parent `§ 路由规则`)
- L25-39 OR any other CODE_LITERAL (验 atom_type=CODE_LITERAL, line_start=fence-open, line_end=fence-close, verbatim 含 fence + body byte-exact)
- L191 OR L194 LIST_ITEM numbered (验 `^N\. ` prefix + inline-bold + parent=`§ 多文件查询策略`)
- 末原子 L211 TABLE_ROW

---

## 3. parent_section convention (numberless H1 spaced format)

- chapter root: `§ SDTM Knowledge Base — Query Routing Guide`
- L1 H1 atom parent=chapter root
- L3-4 blockquote parent=chapter root
- 4 H2 sib chain: `§ 快速入口` (sib=1) / `§ 路由规则` (sib=2) / `§ 多文件查询策略` (sib=3) / `§ 文件类型速查` (sib=4); H2 atom emit parent=chapter root; children parent=父 H2
- 7 H3 numbered under §路由规则 sib=1..7; H3 atom emit parent=`§ 路由规则`; H3 children (`**问法示例**:` SENTENCE + CODE_LITERAL) parent=`§ 路由规则` (NOT 父 H3, v1.9 baseline)
- D8 不触发 (无 `## Overview`)

---

## 4. atom_type 决策 关键 cases

| Source | atom_type | 注 |
|---|---|---|
| L1 H1 | HEADING h_lvl=1 sib=1 | parent=chapter root |
| L3-4 `> ...` blockquote (no Note prefix) | SENTENCE × 2 | verbatim 含 `> ` byte-exact; L3 含 inline `**先读本文件...**` bold byte-exact |
| L6/17/185/198 `---` 4 hr | **DO NOT emit** | skip |
| L8/19/187/200 numberless H2 | HEADING h_lvl=2 sib=1..4 | parent=chapter root |
| L21/41/65/92/119/137/163 numbered H3 (`### N. <Title>`) | HEADING h_lvl=3 sib=1..7 | parent=`§ 路由规则` |
| L23/43/67/94/121/139/165 `**问法示例**: "..."` | SENTENCE bold-prefix per §D-5 (NOT NOTE; not Note/Exception prefix) | parent=`§ 路由规则` |
| L25-39 / L45-63 / L69-90 / L96-117 / L123-135 / L141-161 / L167-183 — 7 fenced code blocks | CODE_LITERAL × 7 | line_start=fence-open line, line_end=fence-close line; verbatim=full block 含 ` ``` ` fences + body byte-exact; parent=`§ 路由规则` |
| L191-194 numbered list `1. **先定位**:` ... `4. **通用规则兜底**:` | LIST_ITEM × 4 | full `N. ` prefix retained byte-exact; inline-bold retained; parent=`§ 多文件查询策略` |
| L196 `**不要一次读取超过 3 个文件**...` | SENTENCE bold-prefix per §D-5 | parent=`§ 多文件查询策略` |
| L189 narrative SENTENCE | SENTENCE | parent=`§ 多文件查询策略` |
| L10-15 / L202-211 — 2 tables | TABLE_HEADER (2-row span ≤1) + TABLE_ROW × N | parent=父 H2 |
| L189 narrative | SENTENCE | parent=`§ 多文件查询策略` |

---

## 5. Dispatch + Rule A

派 `general-purpose` writer; 输出 `evidence/checkpoints/P2_B-03_batch_05_md_atoms.jsonl`. Rule A 派 `pr-review-toolkit:code-reviewer`; 输出 `rule_a_P2_B-03_batch_05_*`. gate ≥90% PASS. boundary 6 + stratified 4 (TABLE_ROW 1 / SENTENCE bold-prefix 1 / CODE_LITERAL 1 / HEADING H2 1).

---

*Kickoff written 2026-05-05 (B-03b #2 ROUTING). §0.5 grep 13/13 ✓. v1.9.1 §D-1 compliance. CODE_LITERAL × 7 first cumulative B-03 live-fire.*
