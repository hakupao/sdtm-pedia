# P2 B-03c Round 02 — Multi-Domain Autonomous Cycle Kickoff (CO..DD scope)

> 创建: 2026-05-05 (post B-03c round 01 CLOSED 同日, commit 40ccc43)
> 父 umbrella: `multi_session/P2_B-03_kickoff.md`
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.1.md` (8 D-rules) + `P0_matcher_v1.9.1.md` + `P0_reviewer_v1.9.1.md`
> Parent round close ref: `multi_session/P2_B-03c_round_01_kickoff.md` + commit 40ccc43 (10 batches 510 atoms 5 domains AE/AG/BE/BS/CE per-batch Rule A 100% × 10 + mini-audit 10/10 + 5/5 invariants PASS 100% reviewer feature-dev:code-reviewer)
> 路由词: 用户在 session 说 **"P2 bulk B-03c round 02 自治连跑"** → 进本 kickoff dispatch (post §0.5 + scope ack 用户 ack 2026-05-05 "Option A 全 ack 开始")
> Convention 继承: 本 kickoff §2 = round 01 §2 carry-forward (atom_id + parent_section lock; CM pilot precedent inherited; round 02 全部 ≤181L < 切片阈值 300L = 不预期 first-time extension)

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1 CRITICAL)

逐项 grep-verified against source byte-exact (执行日 2026-05-05). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令. 缺 §0.5 = orchestrator preflight FAIL.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | post B-03c round 01 CLOSE 时 md_atoms.jsonl 末原子 = `md_dmCE_ex_a126` (round 01 batch_22 final atom; parent_section `§CE.3 [Example 3]`) | `tail -1 md_atoms.jsonl \| python3 -c "import sys,json; a=json.loads(sys.stdin.read()); print(a['atom_id'], a.get('parent_section'))"` | ✓ md_dmCE_ex_a126, §CE.3 [Example 3] |
| 2 | md_atoms.jsonl 当前总原子 = **5364** (post round 01 CLOSED) | `wc -l md_atoms.jsonl` | ✓ 5364 |
| 3 | round 01 实际产 atoms = **510** (5364 − 4854 round 01 起始基线) | progress.json status string `10_batches_510_atoms_5_domains` + commit 40ccc43 message | ✓ 510 |
| 4 | round 01 atoms/line ratio = 510/652 = **0.782** (实证 within 0.7-0.9 范围 per umbrella §3) | round 01 kickoff §0.5 row 7 source 652 + row 3 实证 510 | ✓ 0.782 |
| 5 | 累计 unique files atomized = **27** (post round 01) | post-B-03b 17 files + round 01 added 10 files (5 domains × 2) = 27 | ✓ 27 |
| 6 | domains/ 余 = **57 domains** (63 total − 1 CM B-02 done − 5 round 01 done) | `ls knowledge_base/domains/ \| grep -vE "^(CM\|AE\|AG\|BE\|BS\|CE)$" \| wc -l` | ✓ 57 |
| 7 | Round 02 scope = 5 domains alphabetical (CO / CP / CV / DA / DD) × 2 files = **10 batches** | 字母序 first 5 post round 01: `ls knowledge_base/domains \| grep -vE "^(CM\|AE\|AG\|BE\|BS\|CE)$" \| sort \| head -5` → CO CP CV DA DD | ✓ 10 |
| 8 | Round 02 source lines total = **453** | `wc -l knowledge_base/domains/{CO,CP,CV,DA,DD}/{assumptions,examples}.md \| tail -1` | ✓ 453 (16+32+51+181+5+32+12+48+11+65) |
| 9 | Round 02 size buckets: <50L=**7**, 50-99L=**2**, 100-199L=**1** (per umbrella §3 桶) | CO/ass(16)+CO/ex(32)+CV/ass(5)+CV/ex(32)+DA/ass(12)+DA/ex(48)+DD/ass(11) = 7 ∈ <50; CP/ass(51)+DD/ex(65) = 2 ∈ 50-99; CP/ex(181) = 1 ∈ 100-199 | ✓ 7+2+1=10 |
| 10 | Round 02 估 atoms = **318-409** (0.7-0.9 atoms/line × 453 + round 01 实证 0.782 → 中点 ~354) | 453L × 0.7 = 317.1; × 0.9 = 407.7 | ✓ 318-409 |
| 11 | Batch 序号续 = **batch_23..32** (round 01 末 batch = 22 = CE/examples.md final) | round 01 §1 final row batch_22 = CE/examples.md | ✓ batch_23..32 |
| 12 | post Round 02 累计 md_atoms.jsonl ≈ **5,682-5,773 atoms** | 5364 + 318-409 | ✓ ~5,682-5,773 |
| 13 | post Round 02 累计 file coverage = **37/141 = 26.2%** | 27 + 10 = 37; 37/141 = 0.2624 | ✓ 26.2% |
| 14 | Convention inherit (no first-time lock): atom_id `md_dm<D>_assn\|ex_aNNN` + parent_section root `§<D> [<D> — Assumptions\|Examples]` per round 01 §2 (CM pilot precedent) | round 01 final atom md_dmCE_ex_a126, parent_section `§CE.3 [Example 3]` per md_atoms.jsonl tail = format alive | ✓ inherit |
| 15 | progress.json status string drift detected: text `"52_domains_x_2_files_114_files_remaining"` — 实测 57 domains × 2 files = 114 files (only "52" 数字错, 114 文件总数对) | `ls knowledge_base/domains/ \| grep -vE "^(CM\|AE\|AG\|BE\|BS\|CE)$" \| wc -l` = 57 | ✓ 57 (status string `_progress.json` next write 修正 52→57) |

**Drift 校正记录**:
- progress.json status string contains "52_domains" — drift detected at round 02 kickoff write time. 文件总数 114 是对的 (57×2=114, 巧合), 仅 domain count digit "52" 错. Round 02 close 时 _progress.json status update 一并修正 52→57.
- round 01 kickoff §0.5 row 4 "62 domains" (post-CM-skip) 是对的 — 是 B-03c full scope baseline, 不是 round 02 余量. Round 02 余量 = 62 − 5 = 57 ✓ 自洽.

---

## 1. Round 02 Scope (5 domains × 2 files = 10 batches)

| # | Batch | Target | Lines | 估 atoms | Bucket | atom_id prefix | parent_section root |
|---|---|---|---|---|---|---|---|
| 1 | **batch_23** | `domains/CO/assumptions.md` | 16 | ~11-14 | <50 | `md_dmCO_assn_a` | `§CO [CO — Assumptions]` |
| 2 | **batch_24** | `domains/CO/examples.md` | 32 | ~22-29 | <50 | `md_dmCO_ex_a` | `§CO [CO — Examples]` |
| 3 | **batch_25** | `domains/CP/assumptions.md` | 51 | ~36-46 | 50-99 | `md_dmCP_assn_a` | `§CP [CP — Assumptions]` |
| 4 | **batch_26** | `domains/CP/examples.md` | 181 | ~127-163 | 100-199 | `md_dmCP_ex_a` | `§CP [CP — Examples]` |
| 5 | **batch_27** | `domains/CV/assumptions.md` | 5 | ~4-5 | <50 | `md_dmCV_assn_a` | `§CV [CV — Assumptions]` |
| 6 | **batch_28** | `domains/CV/examples.md` | 32 | ~22-29 | <50 | `md_dmCV_ex_a` | `§CV [CV — Examples]` |
| 7 | **batch_29** | `domains/DA/assumptions.md` | 12 | ~8-11 | <50 | `md_dmDA_assn_a` | `§DA [DA — Assumptions]` |
| 8 | **batch_30** | `domains/DA/examples.md` | 48 | ~34-43 | <50 | `md_dmDA_ex_a` | `§DA [DA — Examples]` |
| 9 | **batch_31** | `domains/DD/assumptions.md` | 11 | ~8-10 | <50 | `md_dmDD_assn_a` | `§DD [DD — Assumptions]` |
| 10 | **batch_32** | `domains/DD/examples.md` | 65 | ~46-59 | 50-99 | `md_dmDD_ex_a` | `§DD [DD — Examples]` |
| **总** | 10 batches | 10 files | **453** | **~318-409** | — | — | — |

post Round 02 累计 file coverage: 27 + 10 = 37/141 = **26.2%** (was 19.1% post round 01).
post Round 02 累计 md_atoms.jsonl: 5364 + ~318-409 = ~5,682-5,773 atoms.

**Round 02 vs Round 01 对照**: round 01 = 652L 510 atoms; round 02 = 453L ~354 atoms (中点). Round 02 体量 ≈ round 01 70% — 单 session 完成可行性更高. CP/ex 181L 是 round 02 唯一 100-199 bucket, 仍 < round 01 BE/ex 161L 与 CE/ex 165L 的 envelope (181 仅 +10%, 在合理外推范围).

---

## 2. Convention inherit (round 01 §2 carry-forward, no first-time lock)

完整 carry-forward, 无 first-time extension since round 02 不引入新 schema 情景.

### 2.1 atom_id prefix

| File | Prefix | 4-digit 容许 (per v1.9.1 §D-7.13) |
|---|---|---|
| `domains/<D>/assumptions.md` | `md_dm<D>_assn_aNNN` | YES (round 02 max ~163 atoms in CP/ex < 999, no 4-digit needed) |
| `domains/<D>/examples.md` | `md_dm<D>_ex_aNNN` | YES |

aNNN 起始 `a001` per file, 不跨 file 续号.

### 2.2 parent_section format

| Heading level | Pattern | Example |
|---|---|---|
| H1 (file root) | `§<D> [<D> — <File-type>]` | `§CO [CO — Assumptions]` / `§CO [CO — Examples]` |
| H2 (only in examples) | `§<D>.<index> [<H2 title>]` | `§CO.1 [Example 1]` |
| H3 (LOCKED 2026-05-05 batch_26 first-time, Daisy/Bojiang ack "H3a 开始") | sub-namespace `§<D>.<index>.<sub-index> [...]` from md suffix (e.g., `### Example 1a` → `§CP.1.a [Example 1a]`); H3 atom emits parent_section = its H2 parent (`§CP.1 [Example 1]`); children of H3 inherit H3 sub-namespace | `### Example 1a` (h_lvl=3, sib=1, parent=§CP.1, sub-ns=§CP.1.a); `### Example 1b` (h_lvl=3, sib=2, sub-ns=§CP.1.b); ch08 H3 precedent inherited |
| H4+ (deeper, rare) | TBD per future encounter | not in round 02 (none in 10 source files per grep) |

**File-type 大写枚举**: `Assumptions` / `Examples` (CM pilot 实测 precedent).
**`<D>` value**: domain code (CO, CP, CV, DA, DD all 2-char, no edge case).

### 2.3 共通规则
- domains/ spaced format `§<D>` (无 numbered) — 区别于 chapters/ numbered
- examples 内 H2 `## Example N` → `§<D>.N [Example N]` 格式
- 跨 batch (单 file 内 round 02 全 ≤181L < 300L 切片阈值) parent_section 续接非问题; round 02 全部 1-file-1-batch 全 dispatch

---

## 3. v1.9.1 prompt 入口条件 (round 01 carry-forward)

### Writer pool (per v1.9.1 §D-8 peer-alternative)
- `oh-my-claudecode:executor` (OMC primary, opus when available)
- `general-purpose` (FALLBACK peer-alternative; B-02 sustained 7 batches 1331 atoms 0 writer defect; round 01 sustained 10 batches 510 atoms 0 writer defect)

### Reviewer pool (per v1.9.1 §D-8)
- `pr-review-toolkit:code-reviewer` (FALLBACK peer-alternative; B-02 + round 01 sustained 100% PASS)
- `oh-my-claudecode:scientist` / `oh-my-claudecode:critic` (OMC primary)
- `feature-dev:code-reviewer` (cumulative inter-cycle audit; round 01 mini-audit 已 burn — round 02 mini-audit 必避用此 type, see §6)

### N21 ban list (sustained)
`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer`, `oh-my-claudecode:document-specialist`

### Rule D 硬约束
writer ≠ reviewer (不同 subagent_type, NOT 仅不同 instance).

### v1.9.1 active hooks
- **Hook 22b** (D-1 CRITICAL): kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims ✓
- **Hook D-NOTE-BQ** (D-2 HIGH): blockquote-prefix `> **Note:**` / `> **Exception:**` = atom_type NOTE
- **Hook D-D8** (D-4 NEW): numberless `## Overview` H2 不创 sub-namespace (domains/ 一般无)
- **Hook A4** (sustained): FIGURE atom 必带 figure_ref non-null
- **Hook C-8** (sustained): file 字段必含 `knowledge_base/` 前缀

---

## 4. 自治连跑 halt 条件 (per umbrella §10.2 + round 02 specific)

任一触发 → 暂停 + ping 用户, 不强行进下一步:

1. **任一 batch §0.5 grep checksum 任一项 FAIL** (numeric drift detected at kickoff write time — 本 kickoff 已 13/13 PASS)
2. **任一 batch Rule A audit < 90% PASS rate** 或现 HIGH severity finding
3. **Schema violation / atom_id collision / 9 atom_type 任一异常**
4. **Source markdown anomaly** 需 Rule B preserve + 业务 judgment call (e.g. 首次遇到 H3+ 子标题 / 首次遇到 NOTE blockquote / 首次遇到 FIGURE in domains/)
5. **v1.9.1 prompt 路径 drift** — writer pool 任一不可用 OR reviewer pool 任一不可用 + FALLBACK 也不可
6. **Convention lock 首次扩展** (e.g. 遇 H3 sub-section 或 FIGURE in domains/, round 02 lock 表 §2.2 未覆盖 — 暂停 + 请求 lock 扩展)
7. **ctx 紧张 (剩 < 30%)** 或 session 累计已 > 1 hr 仍未到 round 闭环 — 主动写 handoff.md + resume prompt 给用户
8. **Round-specific**: 任一 batch atom 数实际 outside 估算 [0.5×low, 1.5×high] → 暂停核 source / prompt drift. Round 02 各 batch 估算与下限/上限:

| Batch | est range | halt low (0.5×low) | halt high (1.5×high) |
|---|---|---|---|
| 23 CO/ass | 11-14 | <6 | >21 |
| 24 CO/ex | 22-29 | <11 | >44 |
| 25 CP/ass | 36-46 | <18 | >69 |
| 26 CP/ex | 127-163 | <64 | >245 |
| 27 CV/ass | 4-5 | <2 | >8 |
| 28 CV/ex | 22-29 | <11 | >44 |
| 29 DA/ass | 8-11 | <4 | >17 |
| 30 DA/ex | 34-43 | <17 | >65 |
| 31 DD/ass | 8-10 | <4 | >15 |
| 32 DD/ex | 46-59 | <23 | >89 |

**Round 02 intended 退出**:
- batch_23..32 全 PASS Rule A ≥90%
- batch_32 后派 reviewer 10-atom stratified mini-audit (5 domains × 2 atoms each, 选 boundary + sentence + list_item)
- mini-audit ≥90% PASS → 单 commit (含全 10 batches + mini-audit + 3 index files 更新) + push → 一行 summary 报告 → session 自然结束 / 等用户路由词 round 03

---

## 5. Per-batch 产物 (round 01 模式 carry-forward)

- `evidence/checkpoints/P2_B-03_batch_<NN>_md_atoms.jsonl` — writer 产物 (atomized JSONL)
- `evidence/checkpoints/rule_a_P2_B-03_batch_<NN>_verdicts.jsonl` + `_summary.md` — Rule A audit (8 boundary + 3 stratified per B-02 R-B02-3; 小文件 <30 atoms 减 stratified 至 2; round 02 极小文件 CV/ass 5L ~4 atoms 可全审 + 0 stratified)
- 追加 root `md_atoms.jsonl` (`>> md_atoms.jsonl`)
- `audit_matrix.md` 行追加 (per batch + round close mini-audit)
- `trace.jsonl` phase_report 事件 + dispatch 事件 (每 subagent 调用一行)
- `_progress.json` 字段更新 (last_completed_batch / current_phase / cumulative atom count)

注: round 02 不写 per-batch kickoff_NN.md (round 01 模式区别 B-03b) — 本 kickoff §1 batch 序列 + §2 convention + §3 prompt + §4 halt 已含 dispatch contract, batch dispatch 直接复用本文 + B-02 dispatch template (umbrella §6).

---

## 6. Round close mini-audit (gate before round 03)

- **Trigger**: batch_32 PASS + 全部入 root md_atoms.jsonl
- **Sample**: 10-atom 跨累积 5 domains × 2 files = 10 文件 分层 (1 atom/file; 选 boundary atom: 首 atom + 末 atom 交替 OR 中段 SENTENCE/LIST_ITEM)
- **Reviewer**: subagent_type **distinct from per-batch reviewers AND round 01 mini-audit reviewer** (Rule D 跨 batch 隔离). 排除 list:
  - `feature-dev:code-reviewer` (round 01 mini-audit burn 2026-05-05)
  - 任一 round 02 per-batch reviewer (TBD per batch dispatch)
  - 候选: `oh-my-claudecode:scientist` / `oh-my-claudecode:critic` / `superpowers:requesting-code-review` 中 round 02 未 burn 的
- **Gate**: ≥90% functional PASS (与 round 01 mini-audit 100% 持平 期待)
- **Findings 处理**: HIGH 必修在 round 03 前 / MEDIUM 入 v1.9.2 backlog / LOW carry-forward
- **Round 03 trigger**: round 02 mini-audit PASS + Daisy/Bojiang ack → 进 round 03 (alphabetical DM..onwards 或 用户决定 scope; **DM/ex 429L + DS/ex 413L** 切片首次 = round 03 halt #6 first-time conv extension expected)

---

## 7. Recovery hint

若 session 中断:
- 看 `_progress.json` (主) 找 `current_phase` + `last_completed_batch`
- 看 `audit_matrix.md` P2 Bulk 表最后 PASS 行
- 看 `trace.jsonl` 尾 phase_report 事件
- 续 batch: 找 `evidence/checkpoints/P2_B-03_batch_<last_NN>_md_atoms.jsonl` 末原子的 atom_id, 下一 batch 起始 atom_id = a001 (新 file, round 02 全 1-file-1-batch 模式不跨 file 续号)
- 跨 round 边界: 看 round 02 mini-audit 状态 + 用户 ack round 03 scope 决定后续

---

## 8. 用户 ack 状态 (round 02 启动 prerequisite)

**Daisy/Bojiang ack 2026-05-05** (本 session 起始, 用户消息 "Option A 全 ack 开始"):

1. **§1 round 02 scope = 5 domains (CO/CP/CV/DA/DD) × 2 files = 10 batches** ✓
2. **§2 convention inherit (round 01 §2 carry-forward, no first-time lock)** ✓
3. **§3 v1.9.1 prompt 路径 (active baseline)** ✓
4. **§4 halt 条件 1-8 (含 round-specific #8 atom 估算 outside [0.5×low, 1.5×high])** ✓

**用户路由词激活**: **"全 ack 开始"** → session 进 batch_23 dispatch (writer for CO/assumptions.md), round 02 全自治执行直到 mini-audit.

---

*Kickoff written 2026-05-05 post round 01 CLOSED commit 40ccc43. §0.5 grep checksum 15/15 byte-exact verified. v1.9.1 §D-1 mandatory compliance. Convention inherit per round 01 §2 (CM pilot precedent) — no first-time lock expected. User ack received via "Option A 全 ack 开始" — dispatch unblocked.*
