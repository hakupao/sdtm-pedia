# P2 B-03c Round 05 — Multi-Domain Autonomous Cycle Kickoff (IS..MK scope)

> 创建: 2026-05-06 (post B-03c round 04 CLOSED 同日, commit 7d8db63 + 0ba2bdc refactor v1 段 2)
> 父 umbrella: `multi_session/P2_B-03_kickoff.md`
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.1.md` (8 D-rules) + `P0_matcher_v1.9.1.md` + `P0_reviewer_v1.9.1.md`
> Parent round close ref: `multi_session/P2_B-03c_round_04_kickoff.md` + commit 7d8db63 (13 batches 731 atoms 6 domains EX/FA/FT/GF/HO/IE per-batch Rule A 100% × 13 + mini-audit 10/10 + 10/10 invariants PASS post-fix reviewer pr-review-toolkit:silent-failure-hunter; §2.7 first-time numberless H2 in assumptions.md FT/ass fully validated; 3 in-place post-hoc fix Rule B backups preserved)
> 路由词: 用户在 session 说 **"P2 bulk B-03c round 05 自治连跑"** → 进本 kickoff dispatch (post §0.5 + §1 scope acked Bojiang 2026-05-06 "可以, 你建议的不错, 开始 round 05" = Option default 6 domains IS/LB/MB/MH/MI/MK)
> Convention 继承: round 01-04 §2.1-2.7 全 carry-forward (atom_id + parent_section + H3a sub-namespace + §2.4 multi-batch slice + §2.6 FIGURE-in-domains lock + LIST_ITEM sib_idx null + §2.7 numberless H2 in assumptions.md = file-root parent); **round 05 无新 first-time lock** (grep 实证 0 numberless H2 in 6 ass.md / 0 mermaid in 12 source files / 最大 IS/ex 273L < 300L slice threshold)

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1 CRITICAL)

逐项 grep-verified against source byte-exact (执行日 2026-05-06). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令. 缺 §0.5 = orchestrator preflight FAIL.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | post B-03c round 04 CLOSE 时 md_atoms.jsonl 末原子 = `md_dmIE_ex_a011` (round 04 batch_57 final atom; parent_section `§IE.1 [Example 1]`; file `knowledge_base/domains/IE/examples.md`) | `tail -1 md_atoms.jsonl \| python3 -c "import sys,json; a=json.loads(sys.stdin.read()); print(a['atom_id'], a.get('parent_section'), a.get('file'))"` | ✓ md_dmIE_ex_a011, §IE.1 [Example 1], knowledge_base/domains/IE/examples.md |
| 2 | md_atoms.jsonl 当前总原子 = **7114** (post round 04 CLOSED) | `wc -l md_atoms.jsonl` | ✓ 7114 |
| 3 | round 04 实际产 atoms = **731** (7114 − 6383 round 04 起始基线) | progress.json `cumulative_post_round_04.md_atoms_jsonl_total` 7114 − round 03 close 6383 | ✓ 731 |
| 4 | round 04 atoms/line ratio = 731/1135 = **0.644** (实证 ratio drift: round 01 0.782 → round 02 0.614 → round 03 0.589 → round 04 0.644 +9.3% slight uptick; signal 用 round 04 baseline 估算 round 05) | round 04 §0.5 row 8 source 1135 + actual 731 atoms | ✓ 0.644 |
| 5 | 累计 unique files atomized = **59** (post round 04; B-02 17 + round 01 10 + round 02 10 + round 03 10 + round 04 12) | post-round 04 59 files; `_progress.json` cumulative_post_round_04.files_atomized = 59 | ✓ 59 |
| 6 | domains/ 余 = **41 domains** (63 total − 1 CM B-02 done − 5 round 01 done − 5 round 02 done − 5 round 03 done − 6 round 04 done = 22 done) | 63 − 22 = 41 | ✓ 41 |
| 7 | Round 05 scope = 6 domains alphabetical (IS / LB / MB / MH / MI / MK) × 2 files = **12 source files** | 字母序 first 6 post round 04: post done 序 IE → next IS LB MB MH MI MK | ✓ 12 source files |
| 8 | Round 05 source lines total = **890** | `wc -l knowledge_base/domains/{IS,LB,MB,MH,MI,MK}/{assumptions,examples}.md` (27+273+18+85+20+171+43+109+7+64+7+66) | ✓ 890 |
| 9 | Round 05 size buckets: <50L=**6**, 50-99L=**3**, 100-199L=**2**, 200-299L=**1**, 300+slice=**0** | <50 = IS/ass(27) + LB/ass(18) + MB/ass(20) + MH/ass(43) + MI/ass(7) + MK/ass(7) = **6**; 50-99 = LB/ex(85) + MI/ex(64) + MK/ex(66) = **3**; 100-199 = MB/ex(171) + MH/ex(109) = **2**; 200-299 = IS/ex(273) = **1**; 300+ slice = **0** — 总 12 ✓ | ✓ 6/3/2/1/0 总 12 |
| 10 | Round 05 **NO file 切片** (largest IS/ex = 273L < 300L slice threshold) → **0 sliced batch** (vs round 03 2 sliced + round 04 1 sliced) | `wc -l knowledge_base/domains/IS/examples.md` = 273 | ✓ 273 < 300 (no slice) |
| 11 | IS/examples.md = **273L** 含 11 H2 examples (Ex1..Ex11 at lines 3, 23, 51, 69, 97, 125, 147, 167, 187, 207, 232) — 单 batch 内一次性 atomize, 不 cross-batch slice | `grep -nE "^## " knowledge_base/domains/IS/examples.md` | ✓ 11 H2 examples single batch |
| 12 | All 6 round 05 assumptions.md = **0 numberless H2** (grep 实证 IS/ass + LB/ass + MB/ass + MH/ass + MI/ass + MK/ass 全 0 H2) → **§2.7 round 04 lock 在 round 05 NO trigger** | `grep -cE "^## " knowledge_base/domains/{IS,LB,MB,MH,MI,MK}/assumptions.md` 全 0 | ✓ 0 numberless H2 in 6 ass.md |
| 13 | All 6 round 05 examples.md H2 全 numbered `## Example N` 格式 (29 examples 总: IS=11+LB=5+MB=3+MH=5+MI=3+MK=2) → 全 §2.5 共通规则 standard self-namespace `§<D>.N [Example N]`, 不触 §2.7 numberless | `grep -cE "^## Example" knowledge_base/domains/{IS,LB,MB,MH,MI,MK}/examples.md` 全 numbered | ✓ 29 numbered Example H2, 0 numberless |
| 14 | Mermaid blocks across 12 round 05 source files = **0** (所有 12 文件 grep 实证 0 fenced mermaid block) → round 05 expected **0 FIGURE atoms** (vs round 04 0 + round 03 4 in DM/ex) | `grep -l '^\`\`\`mermaid$' knowledge_base/domains/{IS,LB,MB,MH,MI,MK}/{assumptions,examples}.md \|\| echo NONE` → NONE | ✓ 0 mermaid in round 05 scope |
| 15 | Round 05 估 atoms = **445-757** (round 04 实证 ratio 0.644 × 890 = 573 mid; lower 0.5 × 890 = 445; upper 0.85 × 890 = 757) | 890L × 0.5 = 445; × 0.644 = 573; × 0.85 = 756.5 | ✓ 445-573-757 |
| 16 | Batch 序号续 = **batch_58..69** (round 04 末 batch = 57 = IE/examples.md final; round 05 共 12 batch: 6 ass single + 6 ex single = 12, 无 sliced batch) | round 04 §0.5 row 16 + round 04 close batch_57 final | ✓ batch_58..69 (12 batches) |
| 17 | post Round 05 累计 md_atoms.jsonl ≈ **7,559-7,871 atoms** (mid 7,687) | 7114 + 445-757 | ✓ ~7,559-7,871 |
| 18 | post Round 05 累计 file coverage = **71/141 = 50.4%** ★ **跨 50% milestone** | 59 + 12 = 71; 71/141 = 0.5035 | ✓ 50.4% (was 41.8% post round 04; **跨过半线**) |
| 19 | post Round 05 累计 domain coverage = **23/63 = 36.5%** | 17 + 6 = 23; 23/63 = 0.365 | ✓ 36.5% (was 27.0% post round 04) |
| 20 | Convention inherit (round 01-04 lock all carry-forward, **round 05 无新增**): atom_id `md_dm<D>_assn\|ex_aNNN` + parent_section root `§<D> [<D> — <File-type>]` + H2 self-namespace `§<D>.N [Example N]` + H3a sub-namespace + §2.4 multi-batch slice (round 05 NO trigger 因 0 切片) + §2.6 FIGURE-in-domains lock + LIST_ITEM sib_idx null + §2.7 numberless H2 in ass.md (round 05 NO trigger 因 0 numberless H2 in 6 ass.md) + H1 sib_idx=1 universal (round 04 v1.9.2 candidate, empirical baseline) + TABLE_HEADER sib_idx=null universal (round 04 v1.9.2 candidate) + extracted_by object schema (round 04 v1.9.2 candidate, dispatch prompt 注意 explicit object form) | round 04 final atom md_dmIE_ex_a011, parent_section `§IE.1 [Example 1]` per md_atoms.jsonl tail = format alive | ✓ inherit (no new locks) |

**Drift 校正记录**:
- progress.json `current_phase` post round 04 close = `P2_B-03c_round_04_CLOSED_pending_round_05_ack` → 启动 round 05 dispatch 时 update → `P2_B-03c_round_05_in_flight_acked_2026-05-06_6_domains_IS_LB_MB_MH_MI_MK_12_batches_batch_58_to_69_no_first_time_locks`.
- Round 04 atoms/line ratio 0.644 vs round 03 0.589 = +9.3% drift (slight uptick, 在波动范围内 — 解释: round 04 多 small <50L files with high SENTENCE/HEADING density). Round 05 size mix 类似 round 04 (6 <50L vs round 04 7 <50L), 估算继续用 0.644 baseline.
- Round 05 体量小 vs round 03/04: 890L (round 04 1135L = 0.78×; round 03 1257L = 0.71×). 单 session 完成可行性 **进一步回升**.
- post round 05 remaining = 41 − 6 = 35 domains × 2 = 70 files (估 5-6 round 完成 P2 B-03c).

---

## 1. Round 05 Scope (6 domains × 2 files = 12 source files = 12 batches, no slice)

| # | Batch | Target | Lines | 估 atoms | Bucket | atom_id prefix | parent_section root |
|---|---|---|---|---|---|---|---|
| 1 | **batch_58** | `domains/IS/assumptions.md` | 27 | ~14-23 | <50 | `md_dmIS_assn_a` | `§IS [IS — Assumptions]` |
| 2 | **batch_59** | `domains/IS/examples.md` | 273 | ~137-232 | 200-299 (largest) | `md_dmIS_ex_a` | `§IS [IS — Examples]` |
| 3 | **batch_60** | `domains/LB/assumptions.md` | 18 | ~9-15 | <50 | `md_dmLB_assn_a` | `§LB [LB — Assumptions]` |
| 4 | **batch_61** | `domains/LB/examples.md` | 85 | ~43-72 | 50-99 | `md_dmLB_ex_a` | `§LB [LB — Examples]` |
| 5 | **batch_62** | `domains/MB/assumptions.md` | 20 | ~10-17 | <50 | `md_dmMB_assn_a` | `§MB [MB — Assumptions]` |
| 6 | **batch_63** | `domains/MB/examples.md` | 171 | ~86-145 | 100-199 | `md_dmMB_ex_a` | `§MB [MB — Examples]` |
| 7 | **batch_64** | `domains/MH/assumptions.md` | 43 | ~22-37 | <50 | `md_dmMH_assn_a` | `§MH [MH — Assumptions]` |
| 8 | **batch_65** | `domains/MH/examples.md` | 109 | ~55-93 | 100-199 | `md_dmMH_ex_a` | `§MH [MH — Examples]` |
| 9 | **batch_66** | `domains/MI/assumptions.md` | 7 | ~4-6 | <50 (smallest tied) | `md_dmMI_assn_a` | `§MI [MI — Assumptions]` |
| 10 | **batch_67** | `domains/MI/examples.md` | 64 | ~32-54 | 50-99 | `md_dmMI_ex_a` | `§MI [MI — Examples]` |
| 11 | **batch_68** | `domains/MK/assumptions.md` | 7 | ~4-6 | <50 (smallest tied) | `md_dmMK_assn_a` | `§MK [MK — Assumptions]` |
| 12 | **batch_69** | `domains/MK/examples.md` | 66 | ~33-56 | 50-99 | `md_dmMK_ex_a` | `§MK [MK — Examples]` |
| **总** | 12 batches | 12 files (0 sliced) | **890** | **~445-757** (mid 573) | — | — | — |

post Round 05 累计 file coverage: 59 + 12 = 71/141 = **50.4%** (★ 跨 50% milestone, was 41.8% post round 04).
post Round 05 累计 md_atoms.jsonl: 7114 + ~445-757 = ~7,559-7,871 atoms (mid ~7,687).

**Round 05 vs Round 04 对照**: round 04 = 1135L 731 atoms 13 batches (1 sliced); round 05 = 890L ~573 atoms 12 batches (0 sliced). **体量 ≈ round 04 0.78× by lines / 0.78× by atoms / 0.92× by batch count**. 单 session 完成可行性 **进一步回升** (vs round 04 已无 halt).

**Round 05 vs Round 03 对照**: round 03 = 1257L 741 atoms 12 batches; round 05 = 890L ~573 atoms 12 batches. 体量 ≈ round 03 0.71×.

**ctx pressure forecast**: round 04 13 batches + 13 reviewer + 1 mini-audit dispatch 共 27 subagent calls (0 halt). Round 05 12 + 12 + 1 = **25 dispatch calls** (轻于 round 04). 无 ctx 警戒线 forecast (round 05 体量 = 0.78× round 04 已成功 vary).

---

## 2. Convention inherit (round 05 全 carry-forward, 无新增)

### 2.1-2.7 全 inherit from round 01-04

(全 carry-forward, 不重复列出 — 详见 round 04 kickoff §2.1-2.7:)
- **§2.1** Heading level pattern (H1 file root / H2 examples self-namespace / H3 sub-namespace / H4+ TBD)
- **§2.2** atom_id prefix per file (4-digit 容许)
- **§2.3** atom_id 起始 a001 per file (NOT per batch; 不跨 file 续号)
- **§2.4** multi-batch single-file slice convention (round 03 lock + round 04 second application) — **round 05 NO trigger** (largest IS/ex 273L < 300L)
- **§2.5** 共通规则 (domains/ spaced format, `## Example N` → `§<D>.N [Example N]`, 跨 file 不续号)
- **§2.6** FIGURE-in-domains lock (round 03 lock) — **round 05 expected 0 FIGURE atoms** per §0.5 row 14 grep 实证 0 mermaid in 12 source files
- **§2.7** Numberless H2 in assumptions.md = file-root parent (round 04 lock FT/ass) — **round 05 NO trigger** per §0.5 row 12 grep 实证 0 numberless H2 in 6 ass.md

### 2.8 Round 04 v1.9.2 candidate empirical rules (全 carry-forward, 等 v1.9.2 cut 才 prompt 显式化)

Round 04 实证 3 条 empirical rule (全 round 04 in-place fix 后 mini-audit invariants 验证), 在 v1.9.2 prompt 显式 codify 之前 round 05 dispatch 注意:

- **R-2.8-1 H1 sib_idx universal = 1** (NOT null): 全 file root H1 atom (`# <Domain> — <File-type>`) 必带 sibling_index=**1** (round 04 batch_45 EX/ass H1 起始 sib=null 误, post-hoc fixed; precedent 47/47 prior H1 atoms = sib=1 universal). Round 05 dispatch prompt 显式: "H1 sib_idx=1 universal".
- **R-2.8-2 TABLE_HEADER sib_idx universal = null** (NOT 1, 2, 3...): 全 TABLE_HEADER atom 必带 sibling_index=**null** (round 04 batch_49+51 TABLE_HEADER sib=1,2 误, post-hoc fixed; precedent 338/353 corpus null universal). Round 05 dispatch prompt 显式: "TABLE_HEADER sib_idx=null universal".
- **R-2.8-3 extracted_by object schema (NOT 字符串简化)**: extracted_by 必带 object form `{"subagent_type": "...", "prompt_version": "...", "ts": "..."}`, NOT 字符串 `"name+version"` 简化形式 (round 04 batch_48+52+56 mini-audit Inv #5 FAIL caught, post-hoc fixed). Round 05 orchestrator dispatch prompt template **强制** explicit object form 一次注入, 单 source-of-truth.

### 2.9 LIST_ITEM sib_idx universal = null (round 03 lock, sustained)

全 round 05 LIST_ITEM atoms sib_idx **必 null**. Cross-H2 LIST_ITEM 不续号 (round 04 batch_50 FT/ass 已先例, sib=null universal).

---

## 3. v1.9.1 prompt 入口条件 (round 01-04 carry-forward)

### Writer pool (per v1.9.1 §D-8 peer-alternative)
- `oh-my-claudecode:executor` (OMC primary, opus when available)
- `general-purpose` (FALLBACK peer-alternative; B-02 + round 01-04 sustained 73 batches 5578 atoms 0 writer defect cumulative)

### Reviewer pool (per v1.9.1 §D-8)
- `pr-review-toolkit:code-reviewer` (FALLBACK peer-alternative; B-02 + round 01-04 sustained 100% PASS; round 05 默认 per-batch reviewer × 12)
- `oh-my-claudecode:scientist` / `oh-my-claudecode:critic` (OMC primary, fresh for round 05 mini-audit)
- **BURNED list (round 05 mini-audit 必避用)**:
  - `feature-dev:code-reviewer` (round 01 mini-audit + round 02 batch_23 burn)
  - `feature-dev:code-architect` (round 02 mini-audit burn)
  - `pr-review-toolkit:type-design-analyzer` (round 03 mini-audit burn)
  - `pr-review-toolkit:silent-failure-hunter` (round 04 mini-audit burn)
  - `pr-review-toolkit:code-reviewer` (round 04 per-batch × 13 burn — round 05 也将作 per-batch reviewer × 12 仍 burn for mini-audit slot)
- **Fresh candidates (round 05 mini-audit)**: `pr-review-toolkit:comment-analyzer` AUDIT mode / `pr-review-toolkit:pr-test-analyzer` AUDIT mode / `oh-my-claudecode:critic` / `oh-my-claudecode:scientist`
- **首选 (round 05 mini-audit)**: `pr-review-toolkit:comment-analyzer` AUDIT mode (NOT comment-rot detection — pivot to atom 字面审 mode; 7th cumulative B-03c reviewer family-pivot)

### N21 ban list (sustained)
`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer`, `oh-my-claudecode:document-specialist`

### Rule D 硬约束
writer ≠ reviewer (不同 subagent_type, NOT 仅不同 instance).

### v1.9.1 active hooks
- **Hook 22b** (D-1 CRITICAL): kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims ✓
- **Hook D-NOTE-BQ** (D-2 HIGH): blockquote-prefix `> **Note:**` / `> **Exception:**` = atom_type NOTE (round 05 inline non-blockquote Note → SENTENCE per Hook negative case)
- **Hook D-D8** (D-4): numberless `## Overview` H2 不创 sub-namespace → **round 05 NO trigger** (0 numberless H2 in 6 ass.md per grep)
- **Hook A4** (sustained): FIGURE atom 必带 figure_ref non-null (round 05 expected 0 occurrence)
- **Hook C-8** (sustained): file 字段必含 `knowledge_base/` 前缀
- **Round 03 §2.4** (multi-batch slice): round 05 NO trigger (0 sliced batch)
- **Round 03 §2.6** (FIGURE-in-domains): round 05 expected 0 FIGURE atoms
- **Round 03 LIST_ITEM sib_idx null**: 全 round 05 enforce
- **Round 04 §2.7** (numberless H2 in ass.md): round 05 NO trigger (0 numberless H2 in 6 ass.md)
- **Round 04 §2.8 R-2.8-1/2/3** (H1 sib=1 / TABLE_HEADER sib=null / extracted_by object): 全 round 05 dispatch prompt 显式注入

---

## 4. 自治连跑 halt 条件 (per umbrella §10.2 + round 05 specific)

任一触发 → 暂停 + ping 用户, 不强行进下一步:

1. **任一 batch §0.5 grep checksum 任一项 FAIL** (numeric drift detected at kickoff write time — 本 kickoff 已 20/20 PASS)
2. **任一 batch Rule A audit < 90% PASS rate** 或现 HIGH severity finding
3. **Schema violation / atom_id collision / 9 atom_type 任一异常**
4. **Source markdown anomaly** 需 Rule B preserve + 业务 judgment call
5. **v1.9.1 prompt 路径 drift** — writer pool 任一不可用 OR reviewer pool 任一不可用 + FALLBACK 也不可
6. **Convention lock 首次扩展** — round 05 无 first-time lock 计划; 若遇到 H4+ 子标题 / FIGURE in domains/ 突发 (虽 grep 实证 0) / numbered H2 in assumptions.md / numberless H2 in assumptions.md (虽 grep 实证 0) / 切片需求 (虽 grep 实证 IS/ex 273L < 300L) → 暂停 + 请求 lock 扩展
7. **ctx 紧张 (剩 < 30%)** 或 session 累计已 > 1.5 hr 仍未到 round 闭环 — 主动写 handoff.md + resume prompt 给用户. **Round 05 ctx pressure 警戒线**: round 05 体量 = 0.78× round 04 (round 04 0 halt), 预期更轻; batch_63 (MB/ex 完成 = round 中点) 后强制 ctx checkpoint
8. **Round-specific**: 任一 batch atom 数实际 outside 估算 [0.5×low, 1.5×high] → 暂停核 source / prompt drift. Round 05 各 batch 估算与下限/上限:

| Batch | est range | halt low (0.5×low) | halt high (1.5×high) |
|---|---|---|---|
| 58 IS/ass | 14-23 | <7 | >34 |
| 59 IS/ex | 137-232 | <68 | >348 |
| 60 LB/ass | 9-15 | <4 | >22 |
| 61 LB/ex | 43-72 | <21 | >108 |
| 62 MB/ass | 10-17 | <5 | >25 |
| 63 MB/ex | 86-145 | <43 | >217 |
| 64 MH/ass | 22-37 | <11 | >55 |
| 65 MH/ex | 55-93 | <27 | >139 |
| 66 MI/ass | 4-6 | <2 | >9 |
| 67 MI/ex | 32-54 | <16 | >81 |
| 68 MK/ass | 4-6 | <2 | >9 |
| 69 MK/ex | 33-56 | <16 | >84 |

9. **NEW round 05 (carry from round 04)**: H1 sib_idx 非 1 universal (R-2.8-1 violation) → 暂停 + 重派 with explicit prompt
10. **NEW round 05 (carry from round 04)**: TABLE_HEADER sib_idx 非 null universal (R-2.8-2 violation) → 暂停 + 重派
11. **NEW round 05 (carry from round 04)**: extracted_by 字符串简化 form (非 object schema, R-2.8-3 violation) → 暂停 + 重派 with explicit object form

**Round 05 intended 退出**:
- batch_58..69 全 PASS Rule A ≥90%
- batch_69 后派 reviewer 10-atom stratified mini-audit (6 domains × ~1.7 atoms each, 选 boundary + sentence + list_item; **+ R-2.8-1/2/3 round 04 v1.9.2 candidate 经验规则 verify (1 H1 atom sib=1 + 1 TABLE_HEADER atom sib=null + 1 atom extracted_by object form)**)
- mini-audit ≥90% PASS → 单 commit (含全 12 batches + mini-audit + 3 index files 更新) + push → 一行 summary 报告 → session 自然结束 / 等用户路由词 round 06

---

## 5. Per-batch 产物 (round 01-04 模式 carry-forward)

- `evidence/checkpoints/P2_B-03_batch_<NN>_md_atoms.jsonl` — writer 产物 (atomized JSONL)
- `evidence/checkpoints/rule_a_P2_B-03_batch_<NN>_verdicts.jsonl` + `_summary.md` — Rule A audit (8 boundary + 3 stratified per B-02 R-B02-3; 小文件 <30 atoms 减 stratified 至 2; round 05 极小文件 MI/ass + MK/ass 7L ~4-6 atoms 可全审 + 0 stratified)
- 追加 root `md_atoms.jsonl` (`>> md_atoms.jsonl`)
- `audit_matrix.md` 行追加 (per batch + round close mini-audit)
- `trace.jsonl` phase_report 事件 + dispatch 事件 (每 subagent 调用一行)
- `_progress.json` 字段更新 (last_completed_batch / current_phase / cumulative atom count + round 04 close stale `current_phase` 校正 → round_05_in_flight)

注: round 05 不写 per-batch kickoff_NN.md (round 01-04 模式 sustained) — 本 kickoff §1 batch 序列 + §2 convention (含 §2.8 v1.9.2 candidate 经验规则) + §3 prompt + §4 halt 已含 dispatch contract, batch dispatch 直接复用本文 + B-02 dispatch template (umbrella §6).

**Dispatch prompt 强制注入** (round 04 §2.8 R-2.8-3 教训, prevent Inv #5 FAIL):
每 batch dispatch prompt 必 include 以下 explicit instruction:
- `"H1 atoms sibling_index=1 universal (R-2.8-1)"`
- `"TABLE_HEADER atoms sibling_index=null universal (R-2.8-2)"`
- `"LIST_ITEM atoms sibling_index=null universal (round 03 lock)"`
- `"extracted_by must be object schema: {\"subagent_type\": \"...\", \"prompt_version\": \"P0_writer_md_v1.9.1\", \"ts\": \"...\"} — NOT string form (R-2.8-3)"`

---

## 6. Round close mini-audit (gate before round 06)

- **Trigger**: batch_69 PASS + 全部入 root md_atoms.jsonl
- **Sample**: 10-atom 跨累积 6 domains × 2 files = 12 文件 中分层 (10 atoms 跨 12 files 不能 1-per-file 全覆盖 → 选 6 domains 中 stratified pick 1 ass + 1 ex 部分 per domain coverage). 实操: 选 boundary atom (首 atom + 末 atom 交替 OR 中段 SENTENCE/LIST_ITEM), **+ R-2.8-1 verify (任一 batch 首 H1 atom sib_idx=1) + R-2.8-2 verify (任一 batch TABLE_HEADER atom sib_idx=null) + R-2.8-3 verify (任一 batch atom extracted_by object form)**
- **Reviewer**: subagent_type **distinct from per-batch reviewers AND round 01-04 mini-audit reviewers** (Rule D 跨 batch 隔离). 排除 list:
  - `feature-dev:code-reviewer` (round 01 mini-audit + round 02 batch_23 burn)
  - `feature-dev:code-architect` (round 02 mini-audit burn)
  - `pr-review-toolkit:type-design-analyzer` (round 03 mini-audit burn)
  - `pr-review-toolkit:silent-failure-hunter` (round 04 mini-audit burn)
  - `pr-review-toolkit:code-reviewer` (round 04 per-batch × 13 + round 05 per-batch × 12 burn)
  - 候选: `pr-review-toolkit:comment-analyzer` / `pr-review-toolkit:pr-test-analyzer` / `oh-my-claudecode:critic` / `oh-my-claudecode:scientist` 中 round 05 未 burn 的
  - **首选 (round 05 mini-audit)**: `pr-review-toolkit:comment-analyzer` AUDIT mode (NOT comment-rot detection — pivot to atom 字面审 mode; 7th cumulative B-03c reviewer family-pivot)
- **Gate**: ≥90% functional PASS (round 01-04 mini-audit 100% post-fix 持平 期待) + 9/9 round invariants:
  1. atom_id collision check (cumulative ~7,687 atoms post round 05; 0 sliced batch → 无 cross-batch 续号 verification needed)
  2. Hook C-8 file prefix universal (knowledge_base/ prefix)
  3. H3a sub-namespace convention (round 02 lock; round 05 expected 0 occurrence per 6 ass.md grep + 29 numbered Example H2 — verify expectation)
  4. TABLE_HEADER Hook A1 span=1 (continued v1.9 standard) + **R-2.8-2 sib_idx=null universal**
  5. extracted_by consistency (subagent_type + prompt_version P0_writer_md_v1.9.1) + **R-2.8-3 object schema (NOT string)**
  6. **§2.4 lock validation**: round 05 NO trigger (0 sliced batch) — verify 0 cross-batch 续号 anomaly
  7. **§2.6 lock validation (round 03 carry-forward)**: round 05 expected 0 FIGURE — verify 0 atom_type=FIGURE 出现
  8. **LIST_ITEM sib_idx null (round 03 lock)**: round 05 全 LIST_ITEM atoms sib_idx=null verify
  9. **§2.7 lock validation**: round 05 NO trigger (0 numberless H2 in 6 ass.md) — verify 0 H2 atom in any ass.md batch + **R-2.8-1 H1 sib_idx=1 universal verify**
- **Findings 处理**: HIGH 必修在 round 06 前 / MEDIUM 入 v1.9.2 backlog / LOW carry-forward
- **v1.9.2 cut 触发评估 (post round 05)**: 累 candidate stack ≤ 7-10 (round 03 carry 4 + round 04 NEW 3 + round 05 NEW 0-3 expected); 远低 v1.9.1 cut 阈值 19. 决策: round 05 close 时 review, 若 stack ≥10 启动 cut planning, 否则 carry 到 round 06.
- **Round 06 trigger**: round 05 mini-audit PASS + Bojiang ack → 进 round 06 (alphabetical NV..onwards 或 用户决定 scope; **MK 已 round 05 done — round 06 起步 ML/MO/MS 等**)

---

## 7. Recovery hint

若 session 中断:
- 看 `_progress.json` (主) 找 `current_phase` + `last_completed_batch`
- 看 `audit_matrix.md` P2 Bulk 表最后 PASS 行
- 看 `trace.jsonl` 尾 phase_report 事件
- 续 batch: 找 `evidence/checkpoints/P2_B-03_batch_<last_NN>_md_atoms.jsonl` 末原子的 atom_id, 下一 batch 起始 atom_id:
  - **Round 05 默认**: a001 (0 sliced batch — 全 round 05 batches 都是新 file 起始)
- 跨 round 边界: 看 round 05 mini-audit 状态 + 用户 ack round 06 scope 决定后续
- Round 05 无 first-time lock → halt 触发概率应低于 round 04 (round 04 0 halt). 若 halt 触发, 90% 概率是 R-2.8-1/2/3 v1.9.2 candidate 经验规则被 writer 忽略 (orchestrator dispatch prompt 没注入) — 看 §5 dispatch prompt 强制注入 list

---

## 8. 用户 ack 状态 (round 05 启动 prerequisite)

**Bojiang ack 已 (本 session 起始, 用户路由词 "看看 work 里面 06 的进度" + 主 session 报告 round 04 CLOSED 状态 + 提供 next-step recommend (IS/LB/MB/MH/MI/MK 6 domains alphabetical) + Bojiang ack "可以, 你建议的不错, 开始 round 05" 2026-05-06)**:

1. **§1 round 05 scope = 6 domains (IS/LB/MB/MH/MI/MK) × 2 files = 12 batches** (vs round 04 13 batches; -1 batch due to 0 切片 — round 04 had 1 sliced EX/ex; round 05 0 sliced because IS/ex 273L < 300L)
2. **§2 全 inherit + 无新增 first-time lock** (per §0.5 row 12/14 grep 实证 0 numberless H2 + 0 mermaid; row 10 grep 实证 IS/ex 273L < 300L slice threshold)
3. **§2.8 round 04 v1.9.2 candidate 经验规则 (R-2.8-1 H1 sib=1 + R-2.8-2 TABLE_HEADER sib=null + R-2.8-3 extracted_by object schema)** — 全 round 05 dispatch prompt 显式注入, 防 round 04 同等 post-hoc fix
4. **§3 v1.9.1 prompt 路径 (active baseline)** — writer pool + reviewer pool sustained; round 05 mini-audit reviewer 候选 `pr-review-toolkit:comment-analyzer` AUDIT mode (7th cumulative B-03c reviewer family-pivot)
5. **§4 halt 条件 1-11 (含 round-specific #8 atom 估算 outside [0.5×low, 1.5×high] + #9 R-2.8-1 H1 sib violation + #10 R-2.8-2 TABLE_HEADER sib violation + #11 R-2.8-3 extracted_by string violation)**
6. **Round 05 体量 ≈ round 04 0.78×** — 单 session 完成可行性进一步回升; halt 触发概率应 ≤ round 04 (round 04 0 halt baseline)

**Scope 备选** (用户已选 §1 default 6 domains alphabetical):
- **Option A (5 domains)**: IS/LB/MB/MH/MI = 10 batches (略小, 不含 MK)
- **Option default (acked 2026-05-06)**: 6 domains IS/LB/MB/MH/MI/MK = 12 batches ✓
- **Option C (扩展)**: 7-8 domains IS..ML 或 IS..MS = 14-16 batches (ctx 风险更高, 用户已不选)

**用户路由词 + scope ack 激活 (acked 2026-05-06)** → **READY for autonomous dispatch** (round 05 无 first-time lock 需额外 ack, dispatch unblocked).

---

*Kickoff written 2026-05-06 post round 04 CLOSED commits 7d8db63 + 0ba2bdc. §0.5 grep checksum 20/20 byte-exact verified. v1.9.1 §D-1 mandatory compliance. Convention inherit per round 01-04 §2.1-2.7 + round 04 §2.8 R-2.8-1/2/3 经验规则 dispatch prompt 显式注入. Round 05 自治连跑 dispatch ready (无 first-time lock 需 ack).*
