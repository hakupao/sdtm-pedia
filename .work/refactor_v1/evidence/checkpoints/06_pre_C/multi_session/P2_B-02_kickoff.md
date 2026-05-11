# P2 B-02 — Multi-Session Cycle Kickoff (umbrella)

> 创建: 2026-04-29 (post B-01 全闭环 same day, post cumulative audit + 1 HIGH hotfix)
> 父 sub-plan: `plans/P2_md_atomization.md` v1.0 §B.1 / §B.4
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.md` (no v1.9.1 cut; carry §2.2 alt = inline self-check in dispatch)
> 路由词: 用户在新 session 说 **"P2 bulk B-02 开始任务"** → 读本 kickoff + 看 §3 决定第一 batch
> 路由词: 用户说 **"P2 bulk B-02 batch 01 开始任务"** → 进 `P2_B-02_batch_01_kickoff.md` 派 dispatch

---

## 1. Session 启动前必读 (按序)

1. `evidence/checkpoints/B01_retrospective.md` — 4 节 retro, 重点 §2 (5 缺口) + §5 (B-02 入口 conditions checklist) + §6 (cumulative audit gate 制度)
2. `evidence/checkpoints/cumulative_audit_post_B01.md` §7 (3 个 v1.9.1 候选) + §9 (B-02 entry 4 项 dispatch 改动)
3. `plans/P2_md_atomization.md` §B.1 (chunk 表) + §B.4 (ch04 切片 5 段; 但 pilot 已做 1-300, 剩 4 段)
4. 本 kickoff (umbrella)
5. 第一 batch kickoff: `P2_B-02_batch_01_kickoff.md`

---

## 2. B-02 Scope

`chapters/` 6 文件 — pilot 已做 ch04 lines 1-300 (218 atoms), B-02 收剩余:

| File | Lines | Pilot 已做 | B-02 待做 | 估 atoms |
|---|---|---|---|---|
| `chapters/ch04_general_assumptions.md` | 1395 | 1-300 (218 atoms) | **lines 301-1395** = 4 段切片 | ~770 (4×~190) |
| `chapters/ch01_introduction.md` | 102 | — | 全文 | ~70 |
| `chapters/ch02_fundamentals.md` | 174 | — | 全文 | ~120 |
| `chapters/ch03_submitting_data.md` | 130 | — | 全文 | ~90 |
| `chapters/ch08_relationships.md` | 439 | — | 全文 | ~310 |
| `chapters/ch10_appendices.md` | 310 | — | 全文 | ~210 |
| **合计** | | | **9 batch** | **~1570 atoms** |

post B-02: md_atoms.jsonl 累计 ~2670 atoms / 14 files (out of 141 in-scope = 9.9%).

---

## 3. Batch 序列 (9 batch)

ch04 续 4 段先打 (锁连续性), 然后剩 5 chapters 文件按 line count 升序 (短的先, 风险最低先消化).

| Batch | Target | Lines | 估 atoms | 切片? | atom_id 起始 |
|---|---|---|---|---|---|
| **P2_B-02_batch_01** | `chapters/ch04_general_assumptions.md` | 301-600 | ~190 | 单段 | `md_ch04_a219` (续 pilot a218) |
| **P2_B-02_batch_02** | `chapters/ch04_general_assumptions.md` | 601-900 | ~190 | 单段 | `md_ch04_a{NNN+1}` (续 batch_01 末) |
| **P2_B-02_batch_03** | `chapters/ch04_general_assumptions.md` | 901-1200 | ~190 | 单段 | (续) |
| **P2_B-02_batch_04** | `chapters/ch04_general_assumptions.md` | 1201-1395 | ~140 | 单段 | (续) |
| **P2_B-02_batch_05** | `chapters/ch01_introduction.md` | 全 102 | ~70 | 单 dispatch | `md_ch01_a001` |
| **P2_B-02_batch_06** | `chapters/ch03_submitting_data.md` | 全 130 | ~90 | 单 dispatch | `md_ch03_a001` |
| **P2_B-02_batch_07** | `chapters/ch02_fundamentals.md` | 全 174 | ~120 | 单 dispatch | `md_ch02_a001` |
| **P2_B-02_batch_08** | `chapters/ch10_appendices.md` | 全 310 | ~210 | 单 dispatch (mirror B-01 model05 296 行 192 atoms) | `md_ch10_a001` |
| **P2_B-02_batch_09** | `chapters/ch08_relationships.md` | 全 439 | ~310 | 单 dispatch (B-01 model02 298 行 244 atoms 已验, 439 行 ~17K tokens 估算 < 32K cap; fallback 切 1-220 + 221-439) | `md_ch08_a001` |

注: **不打包合 batch**. B-01 retro §1.1 验证单 file/单段 1 dispatch 模式稳定, 不混 file 减 atom_id 前缀逻辑复杂度.

---

## 4. B-01 retro 入口 conditions 落地

回应 B01_retrospective.md §5 checklist (B-02 入口前必满足):

- [x] **§2.1 hotfix**: md_model01_a013 figure_ref 已修 (2026-04-29 commit ea0f9bb)
- [x] **§2.2 FIGURE 校验 hook (alt 实现)**: B-02 每 batch dispatch template 顶部加 inline self-check, **不 cut v1.9.1 baseline**. 模板见 §5
- [x] **§2.3 parent_section format 声明**: chapters/ 用 **v1.8 bracketed** `§<num>.<num> [<title>]` (与 pilot ch04 lines 1-300 已写的 218 atoms 同 format, 跨段连续性靠 format 一致). 见 §6
- [x] **§2.4 dispatch template schema-first**: §5 模板顶部 inline 引用 12-key schema 表 + atom_type 9-enum
- [x] **§2.5 LOW deferred**: md_model06_a029 不修, backlog 保留
- [x] **B-02 multi-session kickoff**: 本文件 + `P2_B-02_batch_01_kickoff.md`
- [ ] **本 kickoff 用户 ack** (pending)

---

## 5. Dispatch template (每 batch 共用顶部)

每 batch dispatch 复用以下 schema-first 头部, 不再凭印象写字段:

```
[Schema 字段表 — 12 keys 必填 (除 nullable 标的)]
- atom_id (string, pattern ^md_[A-Za-z0-9_]+_a\d{3}$, unique within file)
- atom_type (string enum: HEADING / SENTENCE / LIST_ITEM / TABLE_HEADER / TABLE_ROW / CODE_LITERAL / NOTE / FIGURE / CROSS_REF)
- file (string, full repo-relative, must start with "knowledge_base/")
- line_start, line_end (int, 1-based)
- verbatim (string, byte-exact substring of source line(s))
- parent_section (string, canonical format §6 below)
- heading_level (int 1-6, REQUIRED for HEADING, null otherwise)
- sibling_index (int 0-based, REQUIRED for HEADING within parent_section, null otherwise)
- figure_ref (string, REQUIRED for FIGURE — pattern md_<file_stem>_<descriptor>_concept_map; null otherwise)
- cross_refs (array of atom_id strings, default [])
- extracted_by (object: { subagent_type: "oh-my-claudecode:executor", prompt_version: "P0_writer_md_v1.9", ts: ISO8601 })

[Hook A4 INLINE pre-DONE FIGURE check]
For every emitted atom_type=FIGURE: verify figure_ref non-null AND matches
md_<file_stem>_<topic_slug>_concept_map (canonical) OR
md_<file_stem>_<descriptor> (alt). If null/empty: DO NOT emit, fix and re-emit.

[Hook C-8 file 全路径]
file 字段必含 "knowledge_base/" 前缀 — 1102/1102 B-01 atoms 合规, 不许漏.
```

---

## 6. parent_section canonical format (chapters/)

chapters 章节有正式编号 (4.1, 4.2.6, 8.3 等), 用 **v1.8 bracketed format** 与 pilot ch04 lines 1-300 已有 218 atoms 对齐:

```
canonical: §<num>.<num>...<num> [<title>]
examples:
  §4.1 [General Assumptions for SDTM Datasets]
  §4.2.6 [Grouping Variables and Categorization]
  §8.3 [Reltype Combinations]
  §10.A.1 [Appendix A.1 — Trial Summary]
```

**禁用** v1.9 spaced format (`§ <title>`) — 仅 model/* 用, 因为 model/* 章节多无正式编号 (B-01 retro §2.3).

跨段 (ch04 切片) 时 parent_section 必持续: 进入 batch 01 时 active L1 = `§4 [General Assumptions]` (来自 pilot a001 H1), active L2 须从段首第一 H2/H3 推断 (line 302 `#### Hierarchy of Grouping Variables` 是 L4 sub-heading under L3 §4.2.6, 见 batch 01 kickoff §3).

---

## 7. Per-batch 产物 (每 batch 共用)

- `evidence/checkpoints/P2_B-02_batch_<NN>_md_atoms.jsonl` — writer 产物
- `evidence/checkpoints/rule_a_P2_B-02_batch_<NN>_verdicts.jsonl` + `_summary.md` — 10-atom scientist
- 追加 root `md_atoms.jsonl` (`>> md_atoms.jsonl`)
- `audit_matrix.md` 行追加
- `trace.jsonl` phase_report 事件 + dispatch 事件
- `_progress.json` 字段更新 (last_completed_batch / current_phase)

---

## 8. B-02 闭环 cumulative audit (gate before B-03)

固化 inter-cycle gate 制度 (B-01 retro §6):
- **Trigger**: B-02 batch 09 PASS + 全部入 root md_atoms.jsonl
- **Sample**: 30-atom 跨累积 14 file 分层 (B-01 close 9 + B-02 close 5 chapters + ch04 全 9 段累计算 1)
- **Reviewer**: 用 ai-slop-cleaner 或 critic (与 B-01 用过的 code-reviewer/scientist 不同 type, Rule D 跨 cycle 隔离更严)
- **Gate**: ≥90% functional PASS
- **Findings 处理**: HIGH 必修在 B-03 入口前 / MEDIUM 入 v1.9.1 backlog / LOW carry-forward

---

## 9. 路由词 quick reference

| 用户说 | session 动作 |
|---|---|
| `P2 bulk B-02 开始任务` | 读本 kickoff (umbrella), 报告下一 batch (默认 batch 01), 等 ack |
| `P2 bulk B-02 batch 01 开始任务` | 进 `P2_B-02_batch_01_kickoff.md` dispatch executor for ch04 lines 301-600 |
| `P2 bulk B-02 batch NN 开始任务` (NN=02..09) | 进对应 batch_NN_kickoff.md (按 §3 表逐个写, 当前仅 batch 01 已写) |
| `B-02 cumulative audit 开始任务` | post batch_09 PASS, 派 ai-slop-cleaner 或 critic 30-atom audit |

---

## 10. Recovery hint

若 session 中断:
- 看 `_progress.json` (主) 找 `current_phase` + `last_completed_batch`
- 看 `audit_matrix.md` P2 Bulk 表最后 PASS 行
- 看 `trace.jsonl` 尾 phase_report 事件
- 续 batch: 找 `evidence/checkpoints/P2_B-02_batch_<last_NN>_md_atoms.jsonl` 末原子的 atom_id, 下一 batch 起始 atom_id = ++NNN

---

*Kickoff written 2026-04-29 (B-01 cycle 闭环 + cumulative audit + hotfix 同日). 等用户 ack 后写 batch 01 kickoff 或直接进 dispatch.*
