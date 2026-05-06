# P2 B-03c Round 06 — Multi-Domain Autonomous Cycle Kickoff (ML/MS/NV/OE/OI scope, Option C)

> 创建: 2026-05-06 (post B-03c round 05 CLOSED 同日, commit 0ee951a)
> 父 umbrella: `multi_session/P2_B-03_kickoff.md`
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.1.md` (8 D-rules) + `P0_matcher_v1.9.1.md` + `P0_reviewer_v1.9.1.md`
> Parent round close ref: `multi_session/P2_B-03c_round_05_kickoff.md` + commit 0ee951a (12 batches 677 atoms 6 domains IS/LB/MB/MH/MI/MK per-batch Rule A 100% × 12 + mini-audit 10/10 + 9/9 invariants PASS post-fix reviewer pr-review-toolkit:comment-analyzer; 1 MED-01 batch_60 LB/assn 9 LIST_ITEM hl+sib explicit-null in-place fix Rule B backups preserved; ★ 跨 50% file coverage milestone 71/141)
> 路由词: 用户在 session 说 **"开始 work 的 06 的 Round 06"** → 主 session 经 grep verify + sub-policy ack ("a" + "你推荐选哪个，直接开干") 路由 Option C scope (5 domains ML/MS/NV/OE/OI; PC defer 到 round 07 因 numberless H2 含 H3 children + L7 H2 numbered Ex1 slug 冲突需独立设计) → 进本 kickoff dispatch
> Convention 继承: round 01-05 §2.1-2.7 全 carry-forward (atom_id + parent_section + H3a sub-namespace + §2.4 multi-batch slice + §2.6 FIGURE-in-domains lock + LIST_ITEM sib_idx null + §2.7 numberless H2 in assumptions.md + R-2.8-1/2/3 round 04 v1.9.2 candidate empirical rules + round 05 MED-01 v1.9.2 candidate LIST_ITEM hl+sib field-explicit-null); **round 06 无新 first-time lock** (grep 实证 0 numberless H2 in 5 ass.md + 0 numberless H2 in 5 ex.md / 0 mermaid in 10 source files / 最大 OE/ex 153L < 300L slice threshold)

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1 CRITICAL)

逐项 grep-verified against source byte-exact (执行日 2026-05-06). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令. 缺 §0.5 = orchestrator preflight FAIL.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | post B-03c round 05 CLOSE 时 md_atoms.jsonl 末原子 = `md_dmMK_ex_a064` (round 05 batch_69 final atom; parent_section `§MK.2 [Example 2]`; file `knowledge_base/domains/MK/examples.md`) | `tail -1 md_atoms.jsonl \| python3 -c "import sys,json; a=json.loads(sys.stdin.read()); print(a['atom_id'], a.get('parent_section'), a.get('file'))"` | ✓ md_dmMK_ex_a064, §MK.2 [Example 2], knowledge_base/domains/MK/examples.md |
| 2 | md_atoms.jsonl 当前总原子 = **7791** (post round 05 CLOSED) | `wc -l md_atoms.jsonl` | ✓ 7791 |
| 3 | round 05 实际产 atoms = **677** (7791 − 7114 round 05 起始基线) | progress.json `cumulative_post_round_05.md_atoms_jsonl_total` 7791 − round 04 close 7114 | ✓ 677 |
| 4 | round 05 atoms/line ratio = 677/890 = **0.761** (实证 ratio drift: round 01 0.782 → round 02 0.614 → round 03 0.589 → round 04 0.644 → round 05 0.761 +18% uptick; signal 用 round 05 baseline 估算 round 06 因 size mix 类似 round 05) | round 05 §0.5 row 8 source 890 + actual 677 atoms | ✓ 0.761 |
| 5 | 累计 distinct domains atomized in md_atoms.jsonl = **28** (DRIFT: progress.json `cumulative_post_round_05.domains_atomized` 写 23 = STALE counter; 实证 grep 28: AE/AG/BE/BS/CE/CM/CO/CP/CV/DA/DD/DM/DS/DV/EC/EG/EX/FA/FT/GF/HO/IE/IS/LB/MB/MH/MI/MK) | `python3 -c "import json; d=set(); [d.add(json.loads(l)['atom_id'][5:].split('_')[0]) for l in open('md_atoms.jsonl')]; print(len(d), sorted(d))"` | ✓ 28 (round 06 close 时 fix progress.json counter) |
| 6 | 累计 distinct files atomized in md_atoms.jsonl = **71** (post round 05; B-02 17 + round 01 10 + round 02 10 + round 03 10 + round 04 12 + round 05 12 = 71) | `python3 -c "import json; f=set(); [f.add(json.loads(l)['file']) for l in open('md_atoms.jsonl')]; print(len(f))"` | ✓ 71 |
| 7 | domains/ 余 = **35 domains** (63 total − 28 done = 35; **NOT 41 per round 05 kickoff §0.5 row 6 stale claim** 因 progress.json 计数 buggy 早期) | 63 − 28 = 35 | ✓ 35 |
| 8 | Round 06 scope = 5 domains alphabetical (ML / MS / NV / OE / OI) × 2 files = **10 source files** (Option C; PC defer 到 round 07 因 numberless H2 含 H3 children + slug 冲突独立设计) | 字母序 first 5 post round 05: post done 序 MK → next ML MS NV OE OI (PC defer); 注: 字母序中 MO 不存在 SDTM 域 (确认源目录 listing) | ✓ 10 source files |
| 9 | Round 06 source lines total = **486** | `wc -l knowledge_base/domains/{ML,MS,NV,OE,OI}/{assumptions,examples}.md` (15+73+19+73+5+87+7+153+22+32) | ✓ 486 |
| 10 | Round 06 size buckets: <50L=**6**, 50-99L=**3**, 100-199L=**1**, 200-299L=**0**, 300+slice=**0** | <50 = ML/ass(15) + MS/ass(19) + NV/ass(5) + OE/ass(7) + OI/ass(22) + OI/ex(32) = **6**; 50-99 = ML/ex(73) + MS/ex(73) + NV/ex(87) = **3**; 100-199 = OE/ex(153) = **1**; 200-299 = **0**; 300+ slice = **0** — 总 10 ✓ | ✓ 6/3/1/0/0 总 10 |
| 11 | Round 06 **NO file 切片** (largest OE/ex = 153L < 300L slice threshold) → **0 sliced batch** (vs round 03 4 sliced + round 04 2 sliced + round 05 0 sliced sustained) | `wc -l knowledge_base/domains/OE/examples.md` = 153 | ✓ 153 < 300 (no slice) |
| 12 | All 5 round 06 assumptions.md = **0 numberless H2** (grep 实证 ML/ass + MS/ass + NV/ass + OE/ass + OI/ass 全 0 H2) → **§2.7 round 04 lock 在 round 06 NO trigger** | `grep -cE "^## " knowledge_base/domains/{ML,MS,NV,OE,OI}/assumptions.md` 全 0 | ✓ 0 numberless H2 in 5 ass.md |
| 13 | All 5 round 06 examples.md H2 全 numbered `## Example N` 格式 (12 numbered Examples 总: ML=2 + MS=3 + NV=2 + OE=4 + OI=1) → 全 §2.5 共通规则 standard self-namespace `§<D>.N [Example N]`, 不触 §2.7 numberless 也不触 NEW lock for ex.md numberless H2 | `grep -cE "^## Example" knowledge_base/domains/{ML,MS,NV,OE,OI}/examples.md` 全 numbered | ✓ 12 numbered Example H2, 0 numberless H2 in 5 ex.md |
| 14 | Mermaid blocks across 10 round 06 source files = **0** (所有 10 文件 grep 实证 0 fenced mermaid block) → round 06 expected **0 FIGURE atoms** (vs round 05 0 + round 04 0 + round 03 4 in DM/ex) | `grep -l '^\`\`\`mermaid$' knowledge_base/domains/{ML,MS,NV,OE,OI}/{assumptions,examples}.md \|\| echo NONE` → NONE | ✓ 0 mermaid in round 06 scope |
| 15 | Round 06 估 atoms = **243-413** (round 05 实证 ratio 0.761 × 486 = 370 mid; lower 0.5 × 486 = 243; upper 0.85 × 486 = 413) | 486L × 0.5 = 243; × 0.761 = 370; × 0.85 = 413 | ✓ 243-370-413 |
| 16 | Batch 序号续 = **batch_70..79** (round 05 末 batch = 69 = MK/ex final; round 06 共 10 batch: 5 ass single + 5 ex single = 10, 无 sliced batch) | round 05 §0.5 row 16 + round 05 close batch_69 final | ✓ batch_70..79 (10 batches) |
| 17 | post Round 06 累计 md_atoms.jsonl ≈ **8,034-8,204 atoms** (mid 8,161) | 7791 + 243-413 | ✓ ~8,034-8,204 |
| 18 | post Round 06 累计 file coverage = **81/141 = 57.4%** | 71 + 10 = 81; 81/141 = 0.5745 | ✓ 57.4% (was 50.4% post round 05) |
| 19 | post Round 06 累计 distinct domain coverage = **33/63 = 52.4%** ★ **跨 50% domain coverage milestone** | 28 + 5 = 33; 33/63 = 0.5238 | ✓ 52.4% (was 44.4% post round 05 实证 28/63; **跨过 domain 半线**) |
| 20 | Convention inherit (round 01-05 lock all carry-forward, **round 06 无新增**): atom_id `md_dm<D>_assn\|ex_aNNN` + parent_section root `§<D> [<D> — <File-type>]` + H2 self-namespace `§<D>.N [Example N]` + H3a sub-namespace + §2.4 multi-batch slice (round 06 NO trigger 因 0 切片) + §2.6 FIGURE-in-domains lock + LIST_ITEM sib_idx null + §2.7 numberless H2 in ass.md (round 06 NO trigger 因 0 numberless H2 in 5 ass.md + 0 numberless H2 in 5 ex.md) + H1 sib_idx=1 universal (R-2.8-1) + TABLE_HEADER sib_idx=null universal (R-2.8-2) + extracted_by object schema (R-2.8-3) + LIST_ITEM hl+sib field-explicit-null (round 05 MED-01 v1.9.2 candidate, dispatch prompt 注意 explicit JSON form `"sibling_index": null` NOT 仅 narrative `sib_idx=null`) | round 05 final atom md_dmMK_ex_a064, parent_section `§MK.2 [Example 2]` per md_atoms.jsonl tail = format alive | ✓ inherit (no new locks) |

**Drift 校正记录**:
- progress.json `cumulative_post_round_05.domains_atomized` = 23 = STALE counter (实证 grep 28). Round 06 close 时一并 fix counter to actual.
- progress.json `current_phase` post round 05 close = `P2_B-03c_round_05_CLOSED_pending_round_06_ack` → 启动 round 06 dispatch 时 update → `P2_B-03c_round_06_in_flight_acked_2026-05-06_5_domains_ML_MS_NV_OE_OI_10_batches_batch_70_to_79_no_first_time_locks_PC_defer_round_07`.
- Round 05 atoms/line ratio 0.761 vs round 04 0.644 = +18% drift uptick (likely cause: round 05 多 dense sub-line SENTENCE 大 ex 文件 IS/MB/MH; v1.9.2 candidate stack #9 INFO). Round 06 size mix 类似 round 05 (6 <50L + 3 中 ex + 1 大 ex), 估算用 0.761 baseline.
- Round 06 体量 vs round 05/04: round 04 1135L (731 atoms 13 batches), round 05 890L (677 atoms 12 batches), round 06 486L (~370 atoms 10 batches). 体量 = round 05 0.55× / round 04 0.43×. **单 session 完成可行性极高**.
- post round 06 remaining = 35 − 5 = 30 domains × 2 = 60 files (估 4-5 round 完成 P2 B-03c, 含 PC 单独 round 07).

---

## 1. Round 06 Scope (5 domains × 2 files = 10 source files = 10 batches, no slice; PC defer 到 round 07)

| # | Batch | Target | Lines | 估 atoms | Bucket | atom_id prefix | parent_section root |
|---|---|---|---|---|---|---|---|
| 1 | **batch_70** | `domains/ML/assumptions.md` | 15 | ~8-13 | <50 | `md_dmML_assn_a` | `§ML [ML — Assumptions]` |
| 2 | **batch_71** | `domains/ML/examples.md` | 73 | ~37-62 | 50-99 | `md_dmML_ex_a` | `§ML [ML — Examples]` |
| 3 | **batch_72** | `domains/MS/assumptions.md` | 19 | ~10-16 | <50 | `md_dmMS_assn_a` | `§MS [MS — Assumptions]` |
| 4 | **batch_73** | `domains/MS/examples.md` | 73 | ~37-62 | 50-99 | `md_dmMS_ex_a` | `§MS [MS — Examples]` |
| 5 | **batch_74** | `domains/NV/assumptions.md` | 5 | ~3-4 | <50 (smallest) | `md_dmNV_assn_a` | `§NV [NV — Assumptions]` |
| 6 | **batch_75** | `domains/NV/examples.md` | 87 | ~44-74 | 50-99 | `md_dmNV_ex_a` | `§NV [NV — Examples]` |
| 7 | **batch_76** | `domains/OE/assumptions.md` | 7 | ~4-6 | <50 | `md_dmOE_assn_a` | `§OE [OE — Assumptions]` |
| 8 | **batch_77** | `domains/OE/examples.md` | 153 | ~77-130 | 100-199 (largest) | `md_dmOE_ex_a` | `§OE [OE — Examples]` |
| 9 | **batch_78** | `domains/OI/assumptions.md` | 22 | ~11-19 | <50 | `md_dmOI_assn_a` | `§OI [OI — Assumptions]` |
| 10 | **batch_79** | `domains/OI/examples.md` | 32 | ~16-27 | <50 | `md_dmOI_ex_a` | `§OI [OI — Examples]` |
| **总** | 10 batches | 10 files (0 sliced) | **486** | **~243-413** (mid 370) | — | — | — |

post Round 06 累计 file coverage: 71 + 10 = 81/141 = **57.4%** (was 50.4% post round 05).
post Round 06 累计 md_atoms.jsonl: 7791 + ~243-413 = ~8,034-8,204 atoms (mid ~8,161).
post Round 06 累计 distinct domain coverage: 28 + 5 = **33/63 = 52.4%** ★ **跨 50% domain milestone**.

**Round 06 vs Round 05 对照**: round 05 = 890L 677 atoms 12 batches; round 06 = 486L ~370 atoms 10 batches. **体量 ≈ round 05 0.55× by lines / 0.55× by atoms / 0.83× by batch count**. 单 session 完成可行性 **进一步回升** (round 05 0 halt baseline; round 06 体量更轻 + 0 NEW lock + 0 sliced batch).

**Round 06 vs Round 02 对照** (体量类似):  round 02 = 10 batches 278 atoms 0 切片; round 06 = 10 batches ~370 atoms 0 切片. 体量略大 1.33× by atoms.

**ctx pressure forecast**: round 05 12 batches + 12 reviewer + 1 mini-audit dispatch 共 25 subagent calls (0 halt). Round 06 10 + 10 + 1 = **21 dispatch calls** (轻于 round 05). 无 ctx 警戒线 forecast.

---

## 2. Convention inherit (round 06 全 carry-forward, 无新增)

### 2.1-2.7 全 inherit from round 01-05

(全 carry-forward, 不重复列出 — 详见 round 05 kickoff §2.1-2.7:)
- **§2.1** Heading level pattern (H1 file root / H2 examples self-namespace / H3 sub-namespace / H4+ TBD)
- **§2.2** atom_id prefix per file (4-digit 容许)
- **§2.3** atom_id 起始 a001 per file (NOT per batch; 不跨 file 续号)
- **§2.4** multi-batch single-file slice convention (round 03 lock + round 04/05 sustained) — **round 06 NO trigger** (largest OE/ex 153L < 300L)
- **§2.5** 共通规则 (domains/ spaced format, `## Example N` → `§<D>.N [Example N]`, 跨 file 不续号)
- **§2.6** FIGURE-in-domains lock (round 03 lock) — **round 06 expected 0 FIGURE atoms** per §0.5 row 14 grep 实证 0 mermaid in 10 source files
- **§2.7** Numberless H2 in assumptions.md = file-root parent (round 04 lock FT/ass) — **round 06 NO trigger** per §0.5 row 12 grep 实证 0 numberless H2 in 5 ass.md (Plan A 沿用 ack Bojiang 2026-05-06; PC defer 到 round 07 因 numberless H2 in ex.md 含 H3 children 需独立设计)

### 2.8 Round 04 v1.9.2 candidate empirical rules (全 carry-forward)

- **R-2.8-1 H1 sib_idx universal = 1**: H1 root atom 必 sib=1 (round 05 sustained 0 violation post explicit dispatch prompt). Round 06 dispatch prompt 显式: "H1 sib_idx=1 universal".
- **R-2.8-2 TABLE_HEADER sib_idx universal = null**: TABLE_HEADER atom 必 sib=null (round 05 sustained 0 violation post explicit dispatch prompt). Round 06 dispatch prompt 显式: "TABLE_HEADER sib_idx=null universal".
- **R-2.8-3 extracted_by object schema (NOT 字符串简化)**: extracted_by 必带 object form `{"subagent_type": "...", "prompt_version": "...", "ts": "..."}` (round 05 sustained 0 violation post explicit dispatch prompt template). Round 06 orchestrator dispatch prompt template **强制** explicit object form.

### 2.9 LIST_ITEM sib_idx universal = null (round 03 lock, sustained)

全 round 06 LIST_ITEM atoms sib_idx **必 null**. Cross-H2 LIST_ITEM 不续号.

### 2.10 NEW round 05 MED-01 v1.9.2 candidate: LIST_ITEM hl+sib field-explicit-null

Round 05 batch_60 LB/assn 9 LIST_ITEM atoms missing explicit hl+sib fields (writer omitted instead of explicit null per terse dispatch prompt). v1.9.2 candidate #8 codify field-explicit-null requirement. **Round 06 dispatch prompt** 强制 explicit JSON form `"heading_level": null, "sibling_index": null` NOT narrative `sib_idx=null universal` (round 05 batch_58 succeeded 因 explicit JSON, batch_60 失败 因 narrative 形式 → writer omit fields).

---

## 3. v1.9.1 prompt 入口条件 (round 01-05 carry-forward)

### Writer pool (per v1.9.1 §D-8 peer-alternative)
- `oh-my-claudecode:executor` (OMC primary, opus when available)
- `general-purpose` (FALLBACK peer-alternative; B-02 + round 01-05 sustained 85 batches 6255 atoms 0 writer defect cumulative)

### Reviewer pool (per v1.9.1 §D-8)
- `pr-review-toolkit:code-reviewer` (FALLBACK peer-alternative; B-02 + round 01-05 sustained 100% PASS; round 06 默认 per-batch reviewer × 10)
- `oh-my-claudecode:scientist` / `oh-my-claudecode:critic` (OMC primary, fresh for round 06 mini-audit)
- **BURNED list (round 06 mini-audit 必避用)**:
  - `feature-dev:code-reviewer` (round 01 mini-audit + round 02 batch_23 burn)
  - `feature-dev:code-architect` (round 02 mini-audit burn)
  - `pr-review-toolkit:type-design-analyzer` (round 03 mini-audit burn)
  - `pr-review-toolkit:silent-failure-hunter` (round 04 mini-audit burn)
  - `pr-review-toolkit:comment-analyzer` (round 05 mini-audit burn)
  - `pr-review-toolkit:code-reviewer` (round 04+05 per-batch × 25 burn — round 06 也将作 per-batch reviewer × 10 仍 burn for mini-audit slot)
- **Fresh candidates (round 06 mini-audit)**: `pr-review-toolkit:pr-test-analyzer` AUDIT mode / `oh-my-claudecode:critic` / `oh-my-claudecode:scientist`
- **首选 (round 06 mini-audit)**: `pr-review-toolkit:pr-test-analyzer` AUDIT mode (NOT pr-test detection — pivot to atom 字面审 mode; **8th cumulative B-03c reviewer family-pivot + 4th pr-review-toolkit AUDIT-pivot**)

### N21 ban list (sustained)
`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer`, `oh-my-claudecode:document-specialist`

### Rule D 硬约束
writer ≠ reviewer (不同 subagent_type, NOT 仅不同 instance).

### v1.9.1 active hooks
- **Hook 22b** (D-1 CRITICAL): kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims ✓
- **Hook D-NOTE-BQ** (D-2 HIGH): blockquote-prefix `> **Note:**` / `> **Exception:**` = atom_type NOTE
- **Hook D-D8** (D-4): numberless `## Overview` H2 不创 sub-namespace → **round 06 NO trigger** (0 numberless H2 in 5 ass.md + 0 in 5 ex.md per grep)
- **Hook A4** (sustained): FIGURE atom 必带 figure_ref non-null (round 06 expected 0 occurrence)
- **Hook C-8** (sustained): file 字段必含 `knowledge_base/` 前缀
- **Round 03 §2.4** (multi-batch slice): round 06 NO trigger (0 sliced batch)
- **Round 03 §2.6** (FIGURE-in-domains): round 06 expected 0 FIGURE atoms
- **Round 03 LIST_ITEM sib_idx null**: 全 round 06 enforce
- **Round 04 §2.7** (numberless H2 in ass.md): round 06 NO trigger (0 numberless H2 in 5 ass.md)
- **Round 04 §2.8 R-2.8-1/2/3** (H1 sib=1 / TABLE_HEADER sib=null / extracted_by object): 全 round 06 dispatch prompt 显式注入
- **Round 05 §2.10 MED-01 carry-forward** (LIST_ITEM hl+sib field-explicit-null): 全 round 06 dispatch prompt 显式 JSON form

---

## 4. 自治连跑 halt 条件 (per umbrella §10.2 + round 06 specific)

任一触发 → 暂停 + ping 用户, 不强行进下一步:

1. **任一 batch §0.5 grep checksum 任一项 FAIL** (numeric drift detected at kickoff write time — 本 kickoff 已 20/20 PASS)
2. **任一 batch Rule A audit < 90% PASS rate** 或现 HIGH severity finding
3. **Schema violation / atom_id collision / 9 atom_type 任一异常**
4. **Source markdown anomaly** 需 Rule B preserve + 业务 judgment call
5. **v1.9.1 prompt 路径 drift** — writer pool 任一不可用 OR reviewer pool 任一不可用 + FALLBACK 也不可
6. **Convention lock 首次扩展** — round 06 无 first-time lock 计划; 若遇到 H4+ 子标题 / FIGURE in domains/ 突发 (虽 grep 实证 0) / numbered H2 in assumptions.md / numberless H2 in assumptions.md (虽 grep 实证 0) / numberless H2 in examples.md (虽 grep 实证 0) / 切片需求 (虽 grep 实证 OE/ex 153L < 300L) → 暂停 + 请求 lock 扩展
7. **ctx 紧张 (剩 < 30%)** 或 session 累计已 > 1.5 hr 仍未到 round 闭环 — 主动写 handoff.md + resume prompt 给用户. **Round 06 ctx pressure 警戒线**: round 06 体量 = 0.55× round 05 (round 05 0 halt), 预期更轻; batch_75 (NV/ex 完成 = round 中点) 后强制 ctx checkpoint
8. **Round-specific**: 任一 batch atom 数实际 outside 估算 [0.5×low, 1.5×high] → 暂停核 source / prompt drift. Round 06 各 batch 估算与下限/上限:

| Batch | est range | halt low (0.5×low) | halt high (1.5×high) |
|---|---|---|---|
| 70 ML/ass | 8-13 | <4 | >20 |
| 71 ML/ex | 37-62 | <19 | >93 |
| 72 MS/ass | 10-16 | <5 | >24 |
| 73 MS/ex | 37-62 | <19 | >93 |
| 74 NV/ass | 3-4 | <2 | >6 |
| 75 NV/ex | 44-74 | <22 | >111 |
| 76 OE/ass | 4-6 | <2 | >9 |
| 77 OE/ex | 77-130 | <39 | >195 |
| 78 OI/ass | 11-19 | <6 | >29 |
| 79 OI/ex | 16-27 | <8 | >41 |

9. **Carry from round 04**: H1 sib_idx 非 1 universal (R-2.8-1 violation) → 暂停 + 重派
10. **Carry from round 04**: TABLE_HEADER sib_idx 非 null universal (R-2.8-2 violation) → 暂停 + 重派
11. **Carry from round 04**: extracted_by 字符串简化 form (非 object schema, R-2.8-3 violation) → 暂停 + 重派
12. **NEW round 06 (carry from round 05 MED-01)**: LIST_ITEM atoms missing hl+sib fields (omitted instead of explicit null) → 暂停 + 重派 with explicit JSON form `"heading_level": null, "sibling_index": null`

**Round 06 intended 退出**:
- batch_70..79 全 PASS Rule A ≥90%
- batch_79 后派 reviewer 10-atom stratified mini-audit (5 domains × 2 atoms each, 选 boundary + sentence + list_item; **+ R-2.8-1/2/3 + round 05 MED-01 LIST_ITEM hl+sib explicit JSON verify**)
- mini-audit ≥90% PASS → 单 commit (含全 10 batches + mini-audit + 3 index files 更新 + progress.json domain counter drift fix 23→33) + push → 一行 summary 报告 → session 自然结束 / 等用户路由词 round 07

---

## 5. Per-batch 产物 (round 01-05 模式 carry-forward)

- `evidence/checkpoints/P2_B-03_batch_<NN>_md_atoms.jsonl` — writer 产物 (atomized JSONL)
- `evidence/checkpoints/rule_a_P2_B-03_batch_<NN>_verdicts.jsonl` + `_summary.md` — Rule A audit (8 boundary + 3 stratified per B-02 R-B02-3; 小文件 <30 atoms 减 stratified 至 2; round 06 极小文件 NV/ass 5L ~3-4 atoms 可全审 + 0 stratified)
- 追加 root `md_atoms.jsonl` (`>> md_atoms.jsonl`)
- `audit_matrix.md` 行追加 (per batch + round close mini-audit)
- `trace.jsonl` phase_report 事件 + dispatch 事件 (每 subagent 调用一行)
- `_progress.json` 字段更新 (last_completed_batch / current_phase / cumulative atom count + round 06 close domain counter drift fix 23→33 + round_05 close stale `current_phase` 校正 → round_06_in_flight)

注: round 06 不写 per-batch kickoff_NN.md (round 01-05 模式 sustained) — 本 kickoff §1 batch 序列 + §2 convention (含 §2.8 + §2.10 v1.9.2 candidate 经验规则) + §3 prompt + §4 halt 已含 dispatch contract.

**Dispatch prompt 强制注入** (round 04 §2.8 R-2.8-3 + round 05 §2.10 MED-01 教训):
每 batch dispatch prompt 必 include 以下 explicit instruction:
- `"H1 atoms sibling_index=1 universal (R-2.8-1)"`
- `"TABLE_HEADER atoms sibling_index=null universal (R-2.8-2)"`
- `"LIST_ITEM atoms heading_level=null AND sibling_index=null universal — explicit JSON form, NOT omitted (round 03 lock + round 05 MED-01)"`
- `"extracted_by must be object schema: {\"subagent_type\": \"...\", \"prompt_version\": \"P0_writer_md_v1.9.1\", \"ts\": \"...\"} — NOT string form (R-2.8-3)"`

---

## 6. Round close mini-audit (gate before round 07)

- **Trigger**: batch_79 PASS + 全部入 root md_atoms.jsonl
- **Sample**: 10-atom 跨累积 5 domains × 2 files = 10 文件 中分层 (10 atoms 跨 10 files 完美 1-per-file 全覆盖). 实操: 选 boundary atom (首 atom + 末 atom 交替 OR 中段 SENTENCE/LIST_ITEM), **+ R-2.8-1 verify (任一 batch 首 H1 atom sib_idx=1) + R-2.8-2 verify (任一 batch TABLE_HEADER atom sib_idx=null) + R-2.8-3 verify (任一 batch atom extracted_by object form) + round 05 MED-01 verify (任一 batch LIST_ITEM atom heading_level + sibling_index 都 explicit null fields)**
- **Reviewer**: subagent_type **distinct from per-batch reviewers AND round 01-05 mini-audit reviewers** (Rule D 跨 batch 隔离). 排除 list:
  - `feature-dev:code-reviewer` (round 01 mini-audit + round 02 batch_23 burn)
  - `feature-dev:code-architect` (round 02 mini-audit burn)
  - `pr-review-toolkit:type-design-analyzer` (round 03 mini-audit burn)
  - `pr-review-toolkit:silent-failure-hunter` (round 04 mini-audit burn)
  - `pr-review-toolkit:comment-analyzer` (round 05 mini-audit burn)
  - `pr-review-toolkit:code-reviewer` (round 04 per-batch × 13 + round 05 per-batch × 12 + round 06 per-batch × 10 burn)
  - 候选: `pr-review-toolkit:pr-test-analyzer` / `oh-my-claudecode:critic` / `oh-my-claudecode:scientist` 中 round 06 未 burn 的
  - **首选 (round 06 mini-audit)**: `pr-review-toolkit:pr-test-analyzer` AUDIT mode (NOT pr-test detection — pivot to atom 字面审 mode; 8th cumulative B-03c reviewer family-pivot + 4th pr-review-toolkit AUDIT-pivot)
- **Gate**: ≥90% functional PASS (round 01-05 mini-audit 100% post-fix 持平 期待) + 9/9 round invariants:
  1. atom_id collision check (cumulative ~8,161 atoms post round 06; 0 sliced batch → 无 cross-batch 续号 verification needed)
  2. Hook C-8 file prefix universal (knowledge_base/ prefix)
  3. H3a sub-namespace convention (round 02 lock; round 06 expected 0 occurrence per 5 ass.md grep + 12 numbered Example H2 — verify expectation; numbered Examples in 5 ex.md 可能含 H3 sub-section 待 actual writer 产物 verify)
  4. TABLE_HEADER Hook A1 span=1 (continued v1.9 standard) + **R-2.8-2 sib_idx=null universal**
  5. extracted_by consistency (subagent_type + prompt_version P0_writer_md_v1.9.1) + **R-2.8-3 object schema (NOT string)**
  6. **§2.4 lock validation**: round 06 NO trigger (0 sliced batch) — verify 0 cross-batch 续号 anomaly
  7. **§2.6 lock validation (round 03 carry-forward)**: round 06 expected 0 FIGURE — verify 0 atom_type=FIGURE 出现
  8. **LIST_ITEM sib_idx null (round 03 lock) + heading_level null explicit (round 05 MED-01 codification)**: round 06 全 LIST_ITEM atoms hl=null AND sib=null verify
  9. **§2.7 lock validation**: round 06 NO trigger (0 numberless H2 in 5 ass.md + 0 in 5 ex.md) — verify 0 H2 atom in any ass.md batch + verify all H2 in ex.md batch numbered Example format + **R-2.8-1 H1 sib_idx=1 universal verify**
- **Findings 处理**: HIGH 必修在 round 07 前 / MEDIUM 入 v1.9.2 backlog / LOW carry-forward
- **v1.9.2 cut 触发评估 (post round 06)**: 累 candidate stack ≤ 9-12 (round 03 carry 4 + round 04 NEW 3 + round 05 NEW 2 + round 06 NEW 0-3 expected); 远低 v1.9.1 cut 阈值 19. 决策: round 06 close 时 review, 若 stack ≥10 启动 cut planning, 否则 carry 到 round 07.
- **Round 07 trigger**: round 06 mini-audit PASS + Bojiang ack → 进 round 07 (默认 PC 单独 mini-round per Option C 决断 / 或扩展 PC + 后续 alphabetical PE/PP/PR/QS/RE; 30 domains × 2 = 60 files remaining post round 06; 估 4-5 round 完成 P2 B-03c)

---

## 7. Recovery hint

若 session 中断:
- 看 `_progress.json` (主) 找 `current_phase` + `last_completed_batch`
- 看 `audit_matrix.md` P2 Bulk 表最后 PASS 行
- 看 `trace.jsonl` 尾 phase_report 事件
- 续 batch: 找 `evidence/checkpoints/P2_B-03_batch_<last_NN>_md_atoms.jsonl` 末原子的 atom_id, 下一 batch 起始 atom_id:
  - **Round 06 默认**: a001 (0 sliced batch — 全 round 06 batches 都是新 file 起始)
- 跨 round 边界: 看 round 06 mini-audit 状态 + 用户 ack round 07 scope 决定后续
- Round 06 无 first-time lock → halt 触发概率应低于 round 05 (round 05 0 halt 但 1 MED-01 in-place fix). 若 halt 触发, 90% 概率是 R-2.8-1/2/3 + round 05 MED-01 v1.9.2 candidate 经验规则被 writer 忽略 (orchestrator dispatch prompt 没注入 explicit JSON form) — 看 §5 dispatch prompt 强制注入 list

---

## 8. 用户 ack 状态 (round 06 启动 prerequisite)

**Bojiang ack 已 (本 session, 用户路由词 "开始 work 的 06 的 Round 06" + 主 session grep verify + sub-policy ack 流程 2026-05-06)**:

1. **§1 round 06 scope = 5 domains (ML/MS/NV/OE/OI) × 2 files = 10 batches** (Option C; PC defer 到 round 07 因 numberless H2 含 H3 children + L7 H2 numbered Ex1 slug 冲突需独立设计) — Bojiang ack "a" (Option A scope 6 domains) → 主 session grep 发现 PC/ex 4 H2 中 3 numberless + 7 H3 含 4 "Example N" 与 §2.7 Plan A sub-policy 决断需要 → re-ping 用户 → Bojiang ack "你推荐选哪个，直接开干" → 主 session 选 Option C (PC defer) 直接开干
2. **§2 全 inherit + 无新增 first-time lock** (per §0.5 row 12/13/14 grep 实证 0 numberless H2 in 5 ass.md + 0 numberless H2 in 5 ex.md + 0 mermaid)
3. **§2.8 round 04 v1.9.2 candidate + §2.10 round 05 MED-01 v1.9.2 candidate** — 全 round 06 dispatch prompt 显式注入 explicit JSON form
4. **§3 v1.9.1 prompt 路径 (active baseline)** — writer pool + reviewer pool sustained; round 06 mini-audit reviewer 候选 `pr-review-toolkit:pr-test-analyzer` AUDIT mode (8th cumulative B-03c reviewer family-pivot)
5. **§4 halt 条件 1-12** (含 round-specific #8 atom 估算 outside [0.5×low, 1.5×high] + #9-11 R-2.8-1/2/3 + #12 round 05 MED-01 LIST_ITEM hl+sib explicit JSON)
6. **Round 06 体量 ≈ round 05 0.55×** — 单 session 完成可行性进一步回升; halt 触发概率应 ≤ round 05 (round 05 0 halt + 1 MED-01 baseline)

**Scope 备选** (用户已选 Option C = 5 domains ML/MS/NV/OE/OI; PC defer round 07):
- **Option A (rejected)**: 6 domains ML/MS/NV/OE/OI/PC = 14-16 batches with PC/ex slicing + numberless H2 sub-policy decision
- **Option B (rejected)**: 6 domains with NEW lock for ex.md numberless H2 sub-namespace by title
- **Option C (acked 2026-05-06)**: 5 domains ML/MS/NV/OE/OI = 10 batches, 0 NEW lock, PC defer to round 07 单独深度处理 ✓

**用户路由词 + scope ack 激活 (acked 2026-05-06)** → **READY for autonomous dispatch** (round 06 无 first-time lock 需额外 ack, dispatch unblocked).

---

*Kickoff written 2026-05-06 post round 05 CLOSED commit 0ee951a. §0.5 grep checksum 20/20 byte-exact verified (含 row 5 progress.json domains_atomized stale counter drift correction record). v1.9.1 §D-1 mandatory compliance. Convention inherit per round 01-05 §2.1-2.7 + round 04 §2.8 R-2.8-1/2/3 + round 05 §2.10 MED-01 v1.9.2 candidate dispatch prompt 显式注入. Round 06 自治连跑 dispatch ready (无 first-time lock 需 ack; PC defer 到 round 07 per Option C 决断).*
