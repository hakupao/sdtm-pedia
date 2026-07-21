# P2 B-03 batch 01 — Multi-Session Kickoff (model/03 single-dispatch full-file)

> 创建: 2026-05-05 (post P2_B-03 umbrella kickoff §10 expand commit f2f80fa, B-03a 自治连跑 启动 1st batch)
> 父 kickoff: `multi_session/P2_B-03_kickoff.md` (umbrella §3 B-03a #1)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.1.md` + `P0_reviewer_v1.9.1.md`
> 路由词: 用户说 **"P2 bulk B-03a 自治连跑 直到 mini-audit PASS"** OR **"P2 bulk B-03 batch 01 开始任务"** 触发本 kickoff dispatch
> **本 batch = 新 file (model/03_special_purpose_domains.md), 不跨 batch continuity, atom_id 重起 a001**; B-03a sub-cycle 第 1 个 batch (model/ 余 3 文件起点); single-dispatch full-file (B-01 model batch 模式)

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1)

本 kickoff 内每条 numeric claim 已 grep-verified against `knowledge_base/model/03_special_purpose_domains.md` byte-exact (执行日 2026-05-05). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | file 行数 = 190 | `wc -l knowledge_base/model/03_special_purpose_domains.md` | ✓ 190 |
| 2 | H1 count = 1 (L1) | `grep -cE "^# " ...` | ✓ 1 |
| 3 | H2 count = 7 (L5/9/71/97/121/144/171) | `grep -nE "^## " ...` | ✓ 7 |
| 4 | H3 count = 7 (L15/58/77/103/129/150/177) | `grep -nE "^### " ...` | ✓ 7 |
| 5 | bold-caption 行数 = 7 | `grep -nE "^\*\*[A-Z]" ...` (6 `**Structure:**` L11/73/99/123/146/173 + 1 `**Note:**` L125) | ✓ 7 |
| 6 | inline NOTE 行数 = 1 (L125) | `grep -nE "^\*\*Note:\*\*" ...` | ✓ 1 |
| 7 | blockquote NOTE 行数 = 0 | `grep -nE "^>\s+\*\*Note:\*\*" ...` | ✓ 0 |
| 8 | pipe-row 行数 (TABLE_HEADER + TABLE_ROW + alignment 合计) = 124 | `grep -cE "^\|" ...` | ✓ 124 |
| 9 | tables 数 = 7 (DM 38-row + DM Key Refs 8-row + CO 15-row + SE 13-row + SJ 10-row + SV 16-row + SM 10-row) | source 视察 H3 + bold-caption 后表格 | ✓ 7 |
| 10 | numberless `## Overview` H2 = 1 (L5) | `grep -E "^## Overview$" ...` | ✓ 1 |

---

## 1. 必读 (按序)

1. `multi_session/P2_B-03_kickoff.md` (umbrella §6 dispatch template + §7.1 model/ parent_section spaced format + §10.2 自治连跑 halt 条件)
2. `subagent_prompts/P0_writer_md_v1.9.1.md` 全文 (尤其 §D-1..§D-8 NEW 8 D-rules; §D-4 D8 numberless `## Overview` chapter root inherit; §D-2 NOTE inline carve-out)
3. `subagent_prompts/P0_reviewer_v1.9.1.md` (Rule A 用)
4. `schema/atom_schema.json` v1.2.1 (atom_id `\d{3,}`)
5. 本 kickoff (本身)

---

## 2. Batch 任务

### 2.1 Target

- **文件**: `knowledge_base/model/03_special_purpose_domains.md`
- **切片**: **全文 1-190 (单 dispatch, 不切片)**
- **估 atoms**: ~150-180 (基于 model/01 244 atoms / 298L = 0.82 atoms/line; 但 model/03 表格密度更高 124 pipe-rows / 190L = 65% table-heavy → density 略低; 估 0.78-0.95 atoms/line × 190 = ~148-180)
- **atom_id 起始**: `md_model03_a001` (新 file 重起)
- **batch_id**: `P2_B-03_batch_01`

### 2.2 Source structure prefix (writer 必读)

```
L1:  # SDTM v2.0 — Chapter 3.2: Special-purpose Domains    ← H1 sib=1
L3:  Source: SDTM v2.0, Section 3.2 (Pages 40-49)          ← SENTENCE (metadata)
L5:  ## Overview                                            ← H2 sib=1 NUMBERLESS (D8 触发)
L7:  narrative paragraph (3 sentences) — D8 chapter-root inherit
L9:  ## Demographics (DM)                                   ← H2 sib=2
L11: **Structure:** One record per subject                  ← SENTENCE bold-caption (D5)
L13: narrative paragraph (multi-sentence)
L15: ### Variables (38 variables)                           ← H3 sib=1 under §Demographics
L17-18: TABLE_HEADER (header + alignment row)
L19-56: TABLE_ROW × 38
L58: ### Key Reference Date Variables                       ← H3 sib=2 under §Demographics
L60-61: TABLE_HEADER
L62-69: TABLE_ROW × 8
L71: ## Comments (CO)                                       ← H2 sib=3
L73: **Structure:** ... (SENTENCE)
L75: narrative paragraph
L77: ### Variables (15 variables)                           ← H3 sib=1 under §Comments
L79-80: TABLE_HEADER
L81-95: TABLE_ROW × 15
L97: ## Subject Elements (SE)                               ← H2 sib=4
L99: **Structure:** ... (SENTENCE)
L101: narrative paragraph
L103: ### Variables (13 variables)                          ← H3 sib=1 under §SE
L105-106: TABLE_HEADER
L107-119: TABLE_ROW × 13
L121: ## Subject Repro Stages                               ← H2 sib=5
L123: **Structure:** ... (SENTENCE)
L125: **Note:** Not for use with human clinical trials.    ← NOTE inline (v1.9 §D-2 carve-out)
L127: narrative paragraph
L129: ### Variables (10 variables)                          ← H3 sib=1 under §SubjectReproStages
L131-132: TABLE_HEADER
L133-142: TABLE_ROW × 10
L144: ## Subject Visits (SV)                                ← H2 sib=6
L146: **Structure:** ... (SENTENCE)
L148: narrative paragraph
L150: ### Variables (16 variables)                          ← H3 sib=1 under §SV
L152-153: TABLE_HEADER
L154-169: TABLE_ROW × 16
L171: ## Subject Disease Milestones (SM)                    ← H2 sib=7
L173: **Structure:** ... (SENTENCE)
L175: narrative paragraph
L177: ### Variables (10 variables)                          ← H3 sib=1 under §SM
L179-180: TABLE_HEADER
L181-190: TABLE_ROW × 10
```

### 2.3 Boundary critical (Rule A 必入 sample, 6 atoms)

- **a001** L1 HEADING h_lvl=1 sib=1 (新 file H1)
- **L5 H2 `## Overview` numberless** sib=1 (D8 trigger)
- **L7 SENTENCE under Overview** — 关键: D8 "chapter root inherit" (parent=H1 chapter root, NOT `§ Overview`)
- **L125 NOTE** inline `**Note:**` (v1.9 §D-2 inline carve-out, atom_type=NOTE NOT SENTENCE)
- **L9 H2 `## Demographics (DM)` numbered-style title** sib=2 (sib chain 续 numberless Overview)
- **末原子 L190 TABLE_ROW** SM 表末行 (file 末 boundary)

---

## 3. parent_section canonical format (本 batch lock)

参 umbrella kickoff §7.1 model/ spaced format. 本 batch lock convention:

- **H1 chapter root**: `§ SDTM v2.0 — Chapter 3.2: Special-purpose Domains` (full title spaced format, B-01 model/06 v1.9 model)
- **H2 sib chain** (`## Overview` + 6 numbered domain titles): parent_section = chapter root above; 自身 emit 时 parent_section = chapter root
- **H2 children (paragraphs/tables/lists under H2)**: 
  - `## Overview` children (L7) → **chapter root inherit** per D8 (NOT `§ Overview`)
  - 6 numbered domain H2 children (e.g., `## Demographics (DM)` L11-69) → parent_section = `§ Demographics (DM)` (本身 H2 title)
- **H3 (Variables tables, Key Reference Date Variables)**: parent_section = 父 H2 (e.g., `§ Demographics (DM)`); H3 自身 emit parent_section = 父 H2; H3 children (TABLE_HEADER + TABLE_ROW) parent = 父 H2 (NOT 自身 H3 — 模 v1.9 baseline 行为)

注: model/03 H1 含 "Chapter 3.2:" 不规范 chapter number (sub-chapter), 不强行 normalize to `§3.2 [...]` numbered bracketed format; 沿用 spaced `§ <full title>` format consistent with B-01 model/06.

---

## 4. Hook A4 inline (FIGURE figure_ref)

每 atom_type=FIGURE 必满足 figure_ref 非 null + canonical pattern. **预期: model/03 全文 0 FIGURE** (无 mermaid block, 全 narrative + table).

---

## 5. atom_type 决策表 (本 batch 关键 cases)

| Source 形态 | atom_type | 注 |
|---|---|---|
| L1 `# SDTM v2.0 — Chapter 3.2: Special-purpose Domains` | HEADING h_lvl=1 sib=1 | parent=`§ SDTM v2.0 — Chapter 3.2: Special-purpose Domains` (自指) |
| L3 `Source: SDTM v2.0, Section 3.2 (Pages 40-49)` | SENTENCE | parent=chapter root; metadata 非 NOTE (无 `**Note:**` prefix) |
| L5 `## Overview` numberless | HEADING h_lvl=2 sib=1 | parent=chapter root; D8 trigger |
| L7 narrative under Overview (3 sentences) | SENTENCE × 多 (sub-line split) | parent=**chapter root** per D8 |
| L9 `## Demographics (DM)` | HEADING h_lvl=2 sib=2 | parent=chapter root; sib chain 续 Overview |
| L11/73/99/123/146/173 `**Structure:** ...` | SENTENCE bold-caption per §D-5 | parent=父 H2 (e.g., `§ Demographics (DM)`); bold markers byte-exact |
| L125 `**Note:** Not for use with human clinical trials.` | NOTE (inline v1.9 §D-2) | parent=`§ Subject Repro Stages`; verbatim 含 `**Note:**` 12-byte prefix |
| L15/58/77/103/129/150/177 `### Variables (...)` / `### Key Reference Date Variables` | HEADING h_lvl=3 sib=1/2 | parent=父 H2; sib RESTART 各 H2 内 |
| pipe-row tables (7 表) | TABLE_HEADER (2-row per §C-5) + TABLE_ROW × N | parent=父 H2 (NOT H3); span ≤1 |
| L7/L13/L75/L101/L127/L148/L175 narrative paragraphs | SENTENCE (sub-line split合法 per §R-C1) | parent=H2 per location (Overview = chapter root via D8; 其余 = 父 H2 自身) |

---

## 6. Dispatch 模板

派 `general-purpose` 单 dispatch (FALLBACK peer-alternative per v1.9.1 §D-8). Dispatch prompt 含:

1. Schema 12-key 表 + atom_type 9-enum + Hook A4 + Hook C-8 + Hook 22b (kickoff §0.5 verified 100% byte-exact = trust)
2. parent_section §3 lock convention (上)
3. file=`knowledge_base/model/03_special_purpose_domains.md`, line range 1-190 全文, atom_id `md_model03_a001`+, batch_id=`P2_B-03_batch_01`
4. extracted_by.subagent_type=`"general-purpose"`, prompt_version=`"P0_writer_md_v1.9.1"`, ts=ISO8601 RFC3339
5. 输出: `evidence/checkpoints/P2_B-03_batch_01_md_atoms.jsonl` (newline-delimited JSON)
6. 23 hooks self-validate + Hook A4 + Hook C-8 (0 FIGURE 预期; 0 prefix-violation)
7. §5 atom_type 决策 reminders 全粘
8. §D-1 Hook 22b: 信任 §0.5 100% verified, 不需独立 grep-verify

---

## 7. Rule A 跟进

派 `pr-review-toolkit:code-reviewer` (Rule D 隔离: writer ≠ reviewer):

- 加载 `subagent_prompts/P0_reviewer_v1.9.1.md`
- 输入: `evidence/checkpoints/P2_B-03_batch_01_md_atoms.jsonl`
- 输出: `evidence/checkpoints/rule_a_P2_B-03_batch_01_verdicts.jsonl` + `_summary.md`
- gate ≥90% PASS
- **boundary 必入 sample (6 atoms)** per §2.3
- **stratified 4 atoms 余样**: TABLE_HEADER 1 / TABLE_ROW 1 / SENTENCE 1 (narrative) / HEADING H3 1
- 总 sample = 10

---

## 8. PASS 后 append + checkpoint

- cat `P2_B-03_batch_01_md_atoms.jsonl` >> `md_atoms.jsonl` 追加
- `wc -l md_atoms.jsonl` 验证累计 (post B-02 close = 2867; post batch_01 应 ~3015-3047)
- `_progress.json` 暂不更新 (B-03a 收尾时一并写)
- `audit_matrix.md` 暂不更新 (同上)
- `trace.jsonl` 写 batch 01 phase_report 事件

---

## 9. 失败处理 + Recovery hint

若 dispatch 或 Rule A FAIL 走 §10.2 halt 条件 (umbrella kickoff). 写 `evidence/failures/P2_B-03_batch_01_attempt_<M>.md`. attempt 2 调整后再派.

Recovery: writer 已派但未完看 trace.jsonl 末; writer 完 reviewer 未派直接派; reviewer FAIL 走 Rule B preserve.

---

*Kickoff written 2026-05-05 (B-03a kickoff #1, model/03 1st batch). §0.5 grep checksum 10/10 verified byte-exact. v1.9.1 §D-1 mandatory compliance. FALLBACK pool peer-alternative path sustained.*
