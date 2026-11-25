# P2 B-03c Round 01 — Multi-Domain Autonomous Cycle Kickoff (entry + convention lock)

> 创建: 2026-05-05 (post B-03b cycle CLOSED + v1.9.1 cut COMPLETED 同日, commit 8182700)
> 父 umbrella: `multi_session/P2_B-03_kickoff.md`
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.1.md` (8 NEW D-rules D-1..D-8) + `P0_matcher_v1.9.1.md` + `P0_reviewer_v1.9.1.md`
> Parent retro 入口: `multi_session/P2_B-02_RETROSPECTIVE.md` §5 trigger #4 (B-03 entry conditions)
> 路由词: 用户在 session 说 **"P2 bulk B-03c round 01 自治连跑"** → 进本 kickoff dispatch (post §0.5 + §2 convention 用户 ack)
> Halt #6 lock 文件: 本 kickoff 即 **atom_id + parent_section convention 首次 lock 文件** per umbrella §10.2 halt 条件 6 + §7.3 convention TBD per first batch_13 dispatch

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1 CRITICAL)

本 kickoff 内 **每条 numeric claim 已 grep-verified against source byte-exact**. 逐项 verify 命令 + 实测值如下表 (执行日 2026-05-05). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令. 缺 §0.5 = orchestrator preflight FAIL.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | B-03b 收官时 md_atoms.jsonl 末原子 = `md_varindex_a1798` (B-03b batch_12 final atom) | `tail -1 md_atoms.jsonl \| python -c "import sys,json; print(json.loads(sys.stdin.read())['atom_id'])"` | ✓ md_varindex_a1798 |
| 2 | md_atoms.jsonl 当前总原子 = 4854 (post B-03b cycle CLOSED) | `wc -l md_atoms.jsonl` | ✓ 4854 |
| 3 | 累计 unique files atomized = 17 (post B-03b) | spaced/no-space JSON 双格式去重后: 6 chapters + 6 model + 2 CM + 3 top-level = 17 | ✓ 17 (raw `sort -u` 数 19 因 ch04 + VARIABLE_INDEX 各 2 格式条目) |
| 4 | domains/ 余 = **62 domains** (CM 已 done) | `ls kb/domains/ \| grep -v "^CM$" \| wc -l` | ✓ 62 |
| 5 | B-03c 全 scope = 62 domains × 2 files = 124 files (per umbrella §3 + §0.5 行 6) | `find kb/domains -name "(assumptions\|examples).md" \| grep -v "/CM/" \| wc -l` | ✓ 62 ass + 62 ex = 124 |
| 6 | Round 01 scope = 5 domains alphabetical (AE / AG / BE / BS / CE) × 2 files = **10 files = 10 batches** | 字母序 first 5 post-CM-skip: `ls kb/domains \| grep -v "^CM$" \| sort \| head -5` → AE AG BE BS CE | ✓ 10 |
| 7 | Round 01 source lines total = 652 | `wc -l kb/domains/{AE,AG,BE,BS,CE}/{assumptions,examples}.md \| tail -1` | ✓ 652 (58+97+25+72+18+161+11+20+25+165) |
| 8 | Round 01 size buckets: <50L=6, 50-99L=2, 100-199L=2 (per umbrella §3 桶) | AE-ass(58)+AG-ex(72) ∈ 50-99 = 2; BE-ex(161)+CE-ex(165) ∈ 100-199 = 2; 余 6 文件 <50L | ✓ 6+2+2=10 |
| 9 | Round 01 估 atoms = 460-590 (0.7-0.9 atoms/line range per umbrella §3 + B-02 batch 09 实证) | 652L × 0.7 = 456; 652L × 0.9 = 587 | ✓ ~460-590 |
| 10 | Batch 序号续 = batch_13..22 (B-03b 末 batch = 12 = VARIABLE_INDEX final slice) | umbrella §4 batch_13 = AE/assumptions.md 已声明 | ✓ batch_13..22 |
| 11 | atom_id prefix convention = `md_dm<D>_assn_aNNN` / `md_dm<D>_ex_aNNN` (CM pilot precedent, **NOT** umbrella §4 注 2 建议 `md_<D>_<assumptions\|examples>_aNNN`) | `grep '"file":"kb/domains/CM/' md_atoms.jsonl \| head -1` 实测 atom_id = `md_dmCM_assn_a001` + `md_dmCM_ex_a001` | ✓ CM pilot 已用此格式, B-03c sustain 一致性 |
| 12 | parent_section convention root = `§<D> [<D> — <File-type>]`; H2 sub = `§<D>.<index> [<H2 title>]` (CM pilot 实测) | `grep '"file":"kb/domains/CM/' md_atoms.jsonl` 实测 root `§CM [CM — Assumptions]` + H2 `§CM.1 [Example 1]` | ✓ CM pilot 一致 |
| 13 | CM pilot 已 atomized atoms count: ass 6 + ex 77 = 83 (B-02 R-B02-1 验证基线) | `grep '"file":"kb/domains/CM/' md_atoms.jsonl \| awk -F'"' '{print $4}' \| uniq -c` | ✓ 6 + 77 = 83 |

**Drift 校正记录 (umbrella §4 注 2 建议 vs 实测 CM pilot)**:
- umbrella `P2_B-03_kickoff.md` §4 注 2 建议: atom_id prefix `md_<DOMAIN>_<assumptions|examples>_aNNN` (e.g. `md_AE_assumptions_a001`)
- CM pilot 实测 (B-02 batch 路径): `md_dmCM_assn_aNNN` + `md_dmCM_ex_aNNN` ("dm" 前缀 + 2-letter file 缩写 `assn`/`ex`)
- **决定**: 沿用 CM pilot 实测格式 (本 kickoff §2.1) — 一致性优先 (避免 Issue 4 §8.4 式 atom_id 跨格式 collision); umbrella §4 注 2 建议作为 alternate 不采用. 若用户 ack alternate 需重 atomize CM pilot, 不推荐.
- B-03c entry 此为 first-time lock — 后续 round 02+ 必沿用本 kickoff §2 lock format

---

## 1. Round 01 Scope (5 domains × 2 files = 10 batches)

| # | Batch | Target | Lines | 估 atoms | Bucket | atom_id prefix | parent_section root |
|---|---|---|---|---|---|---|---|
| 1 | **batch_13** | `domains/AE/assumptions.md` | 58 | ~45-55 | 50-99 | `md_dmAE_assn_a` | `§AE [AE — Assumptions]` |
| 2 | **batch_14** | `domains/AE/examples.md` | 97 | ~70-90 | 50-99 | `md_dmAE_ex_a` | `§AE [AE — Examples]` |
| 3 | **batch_15** | `domains/AG/assumptions.md` | 25 | ~20-25 | <50 | `md_dmAG_assn_a` | `§AG [AG — Assumptions]` |
| 4 | **batch_16** | `domains/AG/examples.md` | 72 | ~55-70 | 50-99 | `md_dmAG_ex_a` | `§AG [AG — Examples]` |
| 5 | **batch_17** | `domains/BE/assumptions.md` | 18 | ~15-20 | <50 | `md_dmBE_assn_a` | `§BE [BE — Assumptions]` |
| 6 | **batch_18** | `domains/BE/examples.md` | 161 | ~120-160 | 100-199 | `md_dmBE_ex_a` | `§BE [BE — Examples]` |
| 7 | **batch_19** | `domains/BS/assumptions.md` | 11 | ~8-12 | <50 | `md_dmBS_assn_a` | `§BS [BS — Assumptions]` |
| 8 | **batch_20** | `domains/BS/examples.md` | 20 | ~16-20 | <50 | `md_dmBS_ex_a` | `§BS [BS — Examples]` |
| 9 | **batch_21** | `domains/CE/assumptions.md` | 25 | ~20-25 | <50 | `md_dmCE_assn_a` | `§CE [CE — Assumptions]` |
| 10 | **batch_22** | `domains/CE/examples.md` | 165 | ~120-160 | 100-199 | `md_dmCE_ex_a` | `§CE [CE — Examples]` |
| **总** | 10 batches | 10 files | **652** | **~460-590** | — | — | — |

post Round 01 累计 file coverage: 17 + 10 = 27/141 = **19.1%** (was 12.1% post B-03b).
post Round 01 累计 md_atoms.jsonl: 4854 + ~460-590 = ~5,314-5,444 atoms.

**为什么 5 domains 不是 10 (umbrella §10.2 中位)**: B-03c first round, atom_id + parent_section convention 首次 lock + alphabetical AE-CE 含 1 大文件 (BE/ex 161L) + 1 大文件 (CE/ex 165L) → 慎拐弯; round 02+ 视 round 01 实测 ctx 余量 + Rule A PASS rate 决定是否扩到 10 domains. B-03b 9 batches 单 session sustained = 10 batches B-03c 同量级.

---

## 2. Convention lock (CM pilot precedent inherited)

### 2.1 atom_id prefix

| File | Prefix | 4-digit 容许 (per v1.9.1 §D-7.13) |
|---|---|---|
| `domains/<D>/assumptions.md` | `md_dm<D>_assn_aNNN` | YES (≥a999 → a1000+ for 大文件; round 01 无此情况, 估 max ~160 atoms) |
| `domains/<D>/examples.md` | `md_dm<D>_ex_aNNN` | YES |

**Schema v1.2.1 inline pattern**: `^md_[A-Za-z0-9_]+_a\d{3,}$` — `dmAE_assn` 11 chars ≤ 限制, `dmAE_ex` 7 chars 同.

**Rule (per CM pilot)**:
- "dm" 前缀 = "domain" 简写 (区别于 chapters `ch<NN>`, model `model<NN>`, top-level `index`/`routing`/`varindex`)
- 文件类型 abbreviation: `assn` (assumptions, 4 chars) + `ex` (examples, 2 chars) — 不写 `assumptions`/`examples` 全词 (CM 实测精简 verbatim)
- aNNN 起始 `a001` per file, 不跨 file 续号 (B-02 R-B02-1 验证模式)

### 2.2 parent_section format

| Heading level | Pattern | Example | Source data |
|---|---|---|---|
| H1 (file root) | `§<D> [<D> — <File-type>]` | `§AE [AE — Assumptions]` / `§AE [AE — Examples]` | CM pilot `§CM [CM — Assumptions]` |
| H2 (only in examples) | `§<D>.<index> [<H2 title>]` | `§AE.1 [Example 1]` / `§AE.5 [Example 5]` | CM pilot `§CM.1 [Example 1]` |
| H3+ (rare in domains/) | inherit parent (per v1.9.1 §D-D8 logic) 或 `§<D>.<index>.<sub-index> [...]` | TBD if encountered | not in CM pilot, 首次遇时再 lock (halt #6 子条款) |

**File-type 大写枚举**: `Assumptions` / `Examples` (首字母大写, 不全大写 `ASSUMPTIONS` per CM pilot 实测).

**`<D>` value**: domain code 2-3 char uppercase (AE, AG, BE, BS, CE; 后段 RELREC, RELSPEC, RELSUB, SUPPQUAL 是 6-7 char — 仍 treat as `<D>`).

### 2.3 共通规则 (per umbrella §7.3)

- domains/ 用 spaced format `§<D>` (不是 `§<num>` numbered) — 区别于 chapters/ 的 `§<num>.<num>...` numbered
- examples 内 H2 `## Example N` → `§<D>.N [Example N]` 格式 (CM pilot 已用)
- 跨 batch (单 file 内不切片 round 01 — 全 ≤165L < ch04 切片阈值 300L) parent_section 续接非问题; round 01 全部 1 file = 1 batch 全 dispatch

---

## 3. v1.9.1 prompt 入口条件

### Writer pool (per v1.9.1 §D-8 peer-alternative)
- `oh-my-claudecode:executor` (OMC primary, opus when available)
- `general-purpose` (FALLBACK peer-alternative; B-02 sustained 7 batches 1331 atoms 0 writer defect)

### Reviewer pool (per v1.9.1 §D-8)
- `pr-review-toolkit:code-reviewer` (FALLBACK peer-alternative; B-02 sustained 7 batches 100% PASS)
- `oh-my-claudecode:scientist` / `oh-my-claudecode:critic` (OMC primary)
- `feature-dev:code-reviewer` (cumulative inter-cycle audit; Rule D distinct)

### N21 ban list (sustained, unchanged)
`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer`, `oh-my-claudecode:document-specialist`

### Rule D 硬约束
writer ≠ reviewer (不同 subagent_type, NOT 仅不同 instance).

### v1.9.1 active hooks (Round 01 重点)
- **Hook 22b** (D-1 CRITICAL): kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims
- **Hook D-NOTE-BQ** (D-2 HIGH): blockquote-prefix `> **Note:**` / `> **Exception:**` = atom_type NOTE (12-byte hex prefix `3e 20 2a 2a 4e 6f 74 65 3a 2a 2a 20`)
- **Hook D-D8** (D-4 NEW): numberless `## Overview` H2 不创 sub-namespace — domains/ 一般无 `## Overview`, 此 hook round 01 不太会触发, 但 carry-forward 备用
- **Hook A4** (sustained): FIGURE atom 必带 figure_ref non-null
- **Hook C-8** (sustained): file 字段必含 `knowledge_base/` 前缀

---

## 4. 自治连跑 halt 条件 (per umbrella §10.2 + 本 kickoff round 01 specific)

任一触发 → 暂停 + ping 用户, 不强行进下一步:

1. **任一 batch §0.5 grep checksum 任一项 FAIL** (numeric drift detected at kickoff write time)
2. **任一 batch Rule A audit < 90% PASS rate** 或现 HIGH severity finding
3. **Schema violation / atom_id collision / 9 atom_type 任一异常**
4. **Source markdown anomaly** 需 Rule B preserve + 业务 judgment call (e.g. 首次遇到 H3+ 子标题 / 首次遇到 NOTE blockquote / 首次遇到 FIGURE in domains/)
5. **v1.9.1 prompt 路径 drift** — writer pool 任一不可用 OR reviewer pool 任一不可用 + FALLBACK 也不可
6. **Convention lock 首次扩展** (e.g. 遇 H3 sub-section, round 01 lock 表 §2.2 未覆盖 — 暂停 + 请求 lock 扩展)
7. **ctx 紧张 (剩 < 30%)** 或 session 累计已 > 1 hr 仍未到 round 闭环 — 主动写 handoff.md + resume prompt 给用户
8. **Round-specific**: 任一 batch atom 数实际 outside 估算范围 [0.5×low, 1.5×high] (e.g. AE/ass 估 45-55, 实际 <22 or >82) → 暂停核 source / prompt drift

**Round 01 intended 退出**: 
- batch_13..22 全 PASS Rule A ≥90%
- batch_22 后派 reviewer 10-atom stratified mini-audit (5 domains × 2 atoms each, 选 boundary + sentence + list_item)
- mini-audit ≥90% PASS → 单 commit (含全 10 batches + mini-audit + 3 index files 更新) + push → 一行 summary 报告 → session 自然结束 / 等用户路由词 round 02

---

## 5. Per-batch 产物 (每 batch 共用, B-02 模式)

- `evidence/checkpoints/P2_B-03_batch_<NN>_md_atoms.jsonl` — writer 产物 (atomized JSONL)
- `evidence/checkpoints/rule_a_P2_B-03_batch_<NN>_verdicts.jsonl` + `_summary.md` — Rule A audit (8 boundary + 3 stratified per B-02 R-B02-3; 小文件 <30 atoms 可减 stratified 至 2)
- 追加 root `md_atoms.jsonl` (`>> md_atoms.jsonl`)
- `audit_matrix.md` 行追加
- `trace.jsonl` phase_report 事件 + dispatch 事件
- `_progress.json` 字段更新 (last_completed_batch / current_phase / cumulative atom count)

注: round 01 不写 per-batch kickoff_NN.md (B-02 模式区别 B-03b) — 本 round 01 kickoff 已含 §1 batch 序列 + §2 convention lock + §3 prompt + §4 halt 条件, batch dispatch 直接复用本文 + B-02 dispatch template (umbrella §6).

---

## 6. Round close mini-audit (gate before round 02)

固化 inter-round gate (B-03b mini-audit 模式 + B-02 R-B02-4):

- **Trigger**: batch_22 PASS + 全部入 root md_atoms.jsonl
- **Sample**: 10-atom 跨累积 5 domains × 2 files = 10 文件 分层 (1 atom/file; 选 boundary atom: 首 atom + 末 atom 交替 OR 中段 SENTENCE/LIST_ITEM)
- **Reviewer**: subagent_type **distinct from per-batch reviewers** (Rule D 跨 batch 隔离; 候选: `feature-dev:code-reviewer` 已在 B-03b CLOSED audit 烧 → round 01 用 `oh-my-claudecode:scientist` 或 `superpowers:requesting-code-review` 中未 burn 的)
- **Gate**: ≥90% functional PASS (与 B-02 30/30=100% 一致)
- **Findings 处理**: HIGH 必修在 round 02 前 / MEDIUM 入 v1.9.2 backlog / LOW carry-forward
- **Round 02 trigger**: round 01 mini-audit PASS + Daisy/Bojiang ack → 进 round 02 (alphabetical CO..DD or 用户决定 scope)

---

## 7. Recovery hint

若 session 中断:
- 看 `_progress.json` (主) 找 `current_phase` + `last_completed_batch`
- 看 `audit_matrix.md` P2 Bulk 表最后 PASS 行
- 看 `trace.jsonl` 尾 phase_report 事件
- 续 batch: 找 `evidence/checkpoints/P2_B-03_batch_<last_NN>_md_atoms.jsonl` 末原子的 atom_id, 下一 batch 起始 atom_id = a001 (新 file, round 01 全 1-file-1-batch 模式不跨 file 续号)
- 跨 round 边界: 看 round 01 mini-audit 状态 + 用户 ack round 02 scope 决定后续

---

## 8. 用户 ack 条款 (round 01 启动 prerequisite)

**自治连跑前 pending 4 条用户 ack** (per halt #6 first-time lock):

1. **§2.1 atom_id prefix convention lock**: `md_dm<D>_assn_aNNN` + `md_dm<D>_ex_aNNN` (CM pilot precedent inherit) — 接受?
2. **§2.2 parent_section convention lock**: root `§<D> [<D> — <File-type>]` + H2 `§<D>.<index> [<H2 title>]` (CM pilot precedent inherit) — 接受?
3. **§1 round 01 scope = 5 domains (AE/AG/BE/BS/CE) × 2 files = 10 batches**: 接受? 或扩到 10 domains (umbrella §10.2 中位 = 20 batches batch_13..32)?
4. **§4 halt 条件 1-8** (含 round-specific #8): 接受?

**用户路由词** (post ack):
- **"全 ack 开始"** / **"自治连跑开始"** → session 进 batch_13 dispatch (writer for AE/assumptions.md), round 01 全自治执行直到 mini-audit
- **"扩到 10 domains"** → 调整 §1 表为 batch_13..32 (再次 grep-verify §0.5 行 6-9 + 表格行 11-20), 然后开始
- **"缩到 N domains"** → N ∈ [3, 4] 调整 §1 表后开始
- **"调整 convention"** → 暂停, 用户给定新 atom_id 或 parent_section format, 重写 §2 + 重 atomize CM pilot

---

*Kickoff written 2026-05-05. §0.5 grep checksum 13/13 byte-exact verified. v1.9.1 §D-1 mandatory compliance. Halt #6 first-time atom_id + parent_section lock per umbrella §10.2 + §7.3 — pending Daisy/Bojiang ack to unblock dispatch.*
