# P2 B-03 batch 02 — Multi-Session Kickoff (model/05 single-dispatch full-file)

> 创建: 2026-05-05 (post P2_B-03 batch_01 PASS 100% 10/10, B-03a 自治连跑 第 2 batch)
> 父 kickoff: `multi_session/P2_B-03_kickoff.md` (umbrella §3 B-03a #2)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.1.md` + `P0_reviewer_v1.9.1.md`
> 路由词: 自治模式 (沿 batch_01 PASS 续派)
> **本 batch = 新 file (model/05_study_level_data.md), 不跨 batch continuity, atom_id 重起 a001**; B-03a #2; single-dispatch full-file. **2 FIGURE atoms 预期** (mermaid Concept Maps L238 + L272).

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1)

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | file 行数 = 296 | `wc -l knowledge_base/model/05_study_level_data.md` | ✓ 296 |
| 2 | H1 count = 1 (L1) | `grep -cE "^# " ...` | ✓ 1 |
| 3 | H2 count = 3 (L5 `## Overview` numberless + L11 `## 5.1` + L226 `## 5.2`) | `grep -nE "^## " ...` | ✓ 3 |
| 4 | H3 count = 13 (11 under §5.1 + 2 under §5.2) | `grep -cE "^### " ...` | ✓ 13 |
| 5 | inline NOTE 行数 = 2 (L81, L99) | `grep -nE "^\*\*Note:\*\*" ...` | ✓ 2 |
| 6 | blockquote NOTE = 0 | `grep -nE "^>\s+\*\*Note:\*\*" ...` | ✓ 0 |
| 7 | bold-caption 行数 = 17 (13 `**Structure:**` + 2 `**Note:**` + 2 `**Concept Map: ...**`) | `grep -nE "^\*\*[A-Z]" ...` | ✓ 17 |
| 8 | pipe-row 行数 = 136 | `grep -cE "^\|" ...` | ✓ 136 |
| 9 | mermaid blocks = 2 (L238, L272) | `grep -n "mermaid" ...` | ✓ 2 |
| 10 | LIST_ITEM `^- ` 行数 = 7 (L15-21 §5.1 intro 7-bullet list) | `grep -cE "^- " ...` | ✓ 7 |
| 11 | tables 数 = 13 (1 表 per H3 — TE/TA/TX/TT/TP/TV/TD/TM/TI/TS/AC under §5.1 + DI/OI under §5.2) | source 视察 | ✓ 13 |
| 12 | H1 含 "Chapter 5:" numbered (vs model/03 "Chapter 3.2:" sub) | source 视察 | ✓ |

---

## 1. 必读 (按序)

1. `multi_session/P2_B-03_kickoff.md` (umbrella §6 + §7.1)
2. `subagent_prompts/P0_writer_md_v1.9.1.md` (尤其 §D-4 D8 numberless `## Overview` + §D-2 inline NOTE + Hook A4 FIGURE figure_ref)
3. `subagent_prompts/P0_reviewer_v1.9.1.md`
4. `schema/atom_schema.json` v1.2.1
5. 本 kickoff (本身) + `P2_B-03_batch_01_kickoff.md` (precedent for D8 chapter root inherit applied)

---

## 2. Batch 任务

### 2.1 Target

- **文件**: `knowledge_base/model/05_study_level_data.md`
- **切片**: **全文 1-296 (单 dispatch, 不切片)**
- **估 atoms**: ~190-240 (基于 batch_01 model/03 0.84 atoms/line × 296 = 249; 但 model/05 表格密度更高 136/296=46% + 2 FIGURE block 占 30 行 reduces SENTENCE density; 估 ~190-240)
- **atom_id 起始**: `md_model05_a001`
- **batch_id**: `P2_B-03_batch_02`

### 2.2 Source structure prefix

```
L1:    # SDTM v2.0 — Chapter 5: Study-level Data         ← H1 sib=1
L3:    Source: SDTM v2.0, Sections 5.1-5.2 (Pages 51-63) ← SENTENCE metadata
L5:    ## Overview                                        ← H2 sib=1 NUMBERLESS (D8)
L7:    narrative (chapter root inherit per D8)
L9:    ---                                                ← horizontal rule (NOT atomized — verify with reviewer; 推荐 skip rule line)
L11:   ## 5.1 Trial Design Model                          ← H2 sib=2 (numbered)
L13:   narrative
L15-21: 7 LIST_ITEM (`- Planned ...`) parent §5.1
L23:   narrative
L25:   ### Trial Elements (TE)                            ← H3 sib=1 under §5.1
L27:   **Structure:** ... SENTENCE bold-caption
L29:   narrative
L31-39: TABLE (header + alignment + rows for TE) parent §5.1
L41:   ### Trial Arms (TA)                                ← H3 sib=2
L43:   **Structure:** ...
... (重复 §5.1 下 11 H3: TE/TA/TX/TT/TP/TV/TD/TM/TI/TS/AC, 各 H3 下 narrative + table)
L77:   ### Trial Reproductive Stages (TT)                ← H3 sib=4
L79:   **Structure:** One record per Planned Repro Stage
L81:   **Note:** Not for use with human clinical trials. ← NOTE inline §D-2
L95:   ### Trial Reproductive Paths (TP)                 ← H3 sib=5
L97:   **Structure:** ...
L99:   **Note:** Not for use with human clinical trials. ← NOTE inline §D-2 (2nd instance)
L116:  ### Trial Visits (TV)                             ← H3 sib=6
L134:  ### Trial Disease Assessments (TD)                ← H3 sib=7
L152:  ### Trial Disease Milestones (TM)                 ← H3 sib=8
L166:  ### Trial Inclusion/Exclusion Criteria (TI)       ← H3 sib=9
L183:  ### Trial Summary (TS)                            ← H3 sib=10
L203:  ### Challenge Agent Characterization (AC)         ← H3 sib=11
L226:  ## 5.2 Study References                           ← H2 sib=3 (numbered)
L230:  ### Device Identifiers (DI)                       ← H3 sib=1 RESTART under §5.2
L232:  **Structure:** ...
L234:  narrative
L236:  **Concept Map: Relationships Between Device Identifier Variables**  ← SENTENCE bold-caption (caption for FIGURE)
L238-252: ```mermaid graph```                            ← FIGURE atom; figure_ref="md_model05_device_identifier_concept_map"
L254-262: TABLE (DI 7-row)                               ← parent §5.2 (NOT 父 H3 per v1.9 baseline)
L264:  ### Non-host Organism Identifiers (OI)            ← H3 sib=2 under §5.2
L266:  **Structure:** ...
L270:  **Concept Map: Relationships Between Non-host Organism Identifier Variables**
L272-286: ```mermaid graph```                            ← FIGURE; figure_ref="md_model05_nonhost_organism_identifier_concept_map"
L288-296: TABLE (OI 7-row)                               ← parent §5.2
```

### 2.3 Boundary critical (Rule A 必入 sample, 6 atoms)

- **a001** L1 HEADING h_lvl=1 sib=1 (新 file H1)
- **L5 H2 `## Overview` numberless** sib=1 (D8 trigger)
- **L7 SENTENCE under Overview** — D8 chapter root inherit (parent=`§5 [SDTM v2.0 — Chapter 5: Study-level Data]`)
- **L81 OR L99 NOTE inline** `**Note:**` (v1.9 §D-2; 选 1 of 2)
- **L238 OR L272 FIGURE** mermaid block (Hook A4 figure_ref non-null + canonical pattern)
- **末原子 L296 TABLE_ROW** OI 表末行 (file 末 boundary)

---

## 3. parent_section canonical format (本 batch lock — 模 B-01 model/01 numbered + chapter format)

H1 含 numbered "Chapter 5:" → 沿用 numbered bracketed format (B-01 model/01 precedent: `§2 [SDTM v2.0 — Chapter 2: Model Concepts and Terms]`):

- **chapter root**: `§5 [SDTM v2.0 — Chapter 5: Study-level Data]`
- **H1 atom (L1)**: parent_section = chapter root (自指)
- **H2 sib chain**:
  - `## Overview` (L5, numberless) sib=1, parent=chapter root, **D8 children inherit chapter root**
  - `## 5.1 Trial Design Model` sib=2, parent=chapter root, atom 自身 emit parent=chapter root, children parent=`§5.1 [Trial Design Model]`
  - `## 5.2 Study References` sib=3, parent=chapter root, children parent=`§5.2 [Study References]`
- **H3 sib chain**:
  - 11 H3 under §5.1 (TE/TA/TX/TT/TP/TV/TD/TM/TI/TS/AC) sib=1..11; parent=`§5.1 [Trial Design Model]`; H3 自身 emit parent=`§5.1 [...]`; children parent=`§5.1 [Trial Design Model]` (NOT 父 H3, 模 v1.9 baseline)
  - 2 H3 under §5.2 (DI/OI) sib=1..2 RESTART; children parent=`§5.2 [Study References]`
- **FIGURE atoms** (L238, L272): parent_section=父 H2 (`§5.2 [Study References]`)
- **L7 narrative under Overview**: per D8 → parent=chapter root

---

## 4. Hook A4 inline (FIGURE figure_ref) — 关键 (model/05 1st FIGURE in B-03)

**2 FIGURE atoms expected**:

| atom_id 起 | line range | figure_ref |
|---|---|---|
| (writer 自定 sequential) | L238-252 | `md_model05_device_identifier_concept_map` |
| (writer 自定 sequential) | L272-286 | `md_model05_nonhost_organism_identifier_concept_map` |

verbatim 含完整 ` ```mermaid` 起始 + graph TD body + ` ``` ` 结束行. line_start=mermaid 起始行, line_end=mermaid 结束行.

注: bold-caption 前置行 (L236, L270) `**Concept Map: ...**` 仍 emit 为 SENTENCE bold-caption per §D-5 (与 FIGURE atom 是分开 2 atoms — caption + figure 各自).

---

## 5. atom_type 决策 (本 batch 关键 cases)

| Source | atom_type | 注 |
|---|---|---|
| L1 H1 | HEADING h_lvl=1 sib=1 | parent=chapter root |
| L3 `Source: ...` | SENTENCE | metadata, parent=chapter root |
| L5 `## Overview` | HEADING h_lvl=2 sib=1 | parent=chapter root; D8 |
| L7 narrative | SENTENCE × 1 (无 sub-line split, 单句) | parent=**chapter root** per D8 |
| L9 `---` 水平线 | **不 emit atom** (skip horizontal rule per v1.9 baseline) | (验证: B-01 model 是否 emit `---`? batch 01 model/03 无 `---`, 此为新 case; 推荐 skip) |
| L11 `## 5.1 Trial Design Model` | HEADING h_lvl=2 sib=2 | parent=chapter root |
| L13 narrative | SENTENCE | parent=`§5.1 [Trial Design Model]` |
| L15-21 7 bullets `- Planned ...` | LIST_ITEM × 7 | parent=`§5.1 [Trial Design Model]`; full prefix `- ` retained |
| L23 narrative | SENTENCE | parent=`§5.1 [Trial Design Model]` |
| L25-203 §5.1 下 11 H3 sections | repeat pattern: H3 sib=1..11 + Structure SENTENCE + narrative + table | parent attached per §3 lock |
| L81/L99 `**Note:** Not for use...` | NOTE inline §D-2 | parent=父 H3 (TT/TP); verbatim 含 `**Note:**` byte-exact |
| L226 `## 5.2 Study References` | HEADING h_lvl=2 sib=3 | parent=chapter root |
| L230/L264 `### Device Identifiers (DI)` / `### Non-host Organism Identifiers (OI)` | HEADING h_lvl=3 sib=1/2 RESTART | parent=`§5.2 [Study References]` |
| L236/L270 `**Concept Map: ...**` | SENTENCE bold-caption §D-5 | parent=`§5.2 [Study References]` |
| L238-252 / L272-286 mermaid blocks | FIGURE × 2 (Hook A4) | parent=`§5.2 [Study References]`; figure_ref=表 above |
| TABLE_HEADER (13 表) | 2-row span ≤1 per §C-5 | parent=父 H2 (NOT 父 H3) |
| TABLE_ROW × ~120 | parent=父 H2 | |
| 13 `**Structure:**` lines | SENTENCE bold-caption §D-5 | parent=父 H3 |

---

## 6. Dispatch 模板

派 `general-purpose` 单 dispatch (FALLBACK peer-alternative). 同 batch_01 模板, 替换:
- file=`knowledge_base/model/05_study_level_data.md`, 1-296 全文
- atom_id `md_model05_a001`+
- batch_id=`P2_B-03_batch_02`
- 输出: `evidence/checkpoints/P2_B-03_batch_02_md_atoms.jsonl`
- **2 FIGURE 预期**: figure_ref 表见 §4
- **关键 D-rules**: D8 (`## Overview` + L7 chapter root inherit) + D2 (L81/L99 inline NOTE) + D5 (17 bold-caption — 13 Structure + 2 Note + 2 Concept Map) + Hook A4 (2 FIGURE)
- **`---` horizontal rule (L9) skip 不 emit** (新 case for B-03; 写 batch report flag if writer 决定 atomize)

---

## 7. Rule A 跟进

派 `pr-review-toolkit:code-reviewer` (Rule D 隔离 sustained):

- 加载 `subagent_prompts/P0_reviewer_v1.9.1.md`
- 输入: `evidence/checkpoints/P2_B-03_batch_02_md_atoms.jsonl`
- 输出: `evidence/checkpoints/rule_a_P2_B-03_batch_02_verdicts.jsonl` + `_summary.md`
- gate ≥90% PASS
- **boundary 必入 sample (6 atoms)** per §2.3
- **stratified 4 atoms 余样**: TABLE_HEADER 1 / TABLE_ROW 1 / LIST_ITEM 1 (L15-21) / SENTENCE bold-caption 1 (`**Structure:**` 或 `**Concept Map**`)

---

## 8. PASS 后 append + checkpoint

- cat 输出 >> `md_atoms.jsonl` (post batch_01 = 3027; post batch_02 应 ~3217-3267)
- `_progress.json` 暂不更新 (B-03a 收尾时一并写)
- `trace.jsonl` 写 batch 02 phase_report

---

*Kickoff written 2026-05-05 (B-03a #2, model/05). §0.5 grep checksum 12/12 verified byte-exact. v1.9.1 §D-1 mandatory compliance. 2 FIGURE 1st in B-03 cycle = Hook A4 live-fire.*
