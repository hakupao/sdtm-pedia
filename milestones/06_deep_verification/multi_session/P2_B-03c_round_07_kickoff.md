# P2 B-03c Round 07 — PC Solo Mini-Round Kickoff (Option C continuation, Plan B sub-policy NEW lock)

> 创建: 2026-05-06 (post B-03c round 06 CLOSED + v1.9.2 prompt cut COMPLETED 同日, commits 0ba2bdc + a0ccaf4 + 966e6c4)
> 父 umbrella: `multi_session/P2_B-03_kickoff.md`
> 父 prompt (active baseline): `subagent_prompts/P0_writer_md_v1.9.2.md` (6 NEW E-rules + 28 hooks) + `P0_matcher_v1.9.2.md` (29 hooks) + `P0_reviewer_v1.9.2.md` (32 hooks) + `P0_writer_pdf_v1.9.2.md` (paired-sync)
> Parent round close ref: `multi_session/P2_B-03c_round_06_kickoff.md` + commits 0ba2bdc (round 06 close 10 batches 331 atoms 5 domains ML/MS/NV/OE/OI ★ 跨 50% domain coverage milestone 33/63=52.4%; 1 RESOLVED HALT batch_72 4-schema-regression → re-dispatch PASS; PC defer per Option C) + 966e6c4 (v1.9.2 prompt cut 4 paired-sync prompts + 6 NEW E-rules consolidating 10-candidate stack)
> 路由词: 用户在 session 说 **"开始 work 的 06 的 Round 07"** → 主 session 经 grep verify + sub-policy ack ("按你推荐的来" = Plan B sub-namespace + PC solo Option C continuation) → 进本 kickoff dispatch
> Convention 继承: round 01-06 §2.1-2.10 全 carry-forward; **round 07 NEW first-time lock §2.11 Plan B sub-namespace by sib_idx** for numberless H2 with H3 children in examples.md (PC/ex L58 case; PC defer 到 round 07 设计原因正是此 case 需独立 sub-policy)

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1 CRITICAL + v1.9.2 §E-1 paired-sync)

逐项 grep-verified against source byte-exact (执行日 2026-05-06). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令. 缺 §0.5 = orchestrator preflight FAIL.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | post B-03c round 06 CLOSE 时 md_atoms.jsonl 末原子 = `md_dmOI_ex_a023` (round 06 batch_79 final atom; parent_section `§OI.1 [Example 1]`; file `knowledge_base/domains/OI/examples.md`; atom_type TABLE_ROW) | `tail -1 md_atoms.jsonl \| python3 -c "import sys,json; a=json.loads(sys.stdin.read()); print(a['atom_id'], a.get('parent_section'), a.get('file'))"` | ✓ md_dmOI_ex_a023, §OI.1 [Example 1], knowledge_base/domains/OI/examples.md |
| 2 | md_atoms.jsonl 当前总原子 = **8122** (post round 06 CLOSED) | `wc -l md_atoms.jsonl` | ✓ 8122 |
| 3 | round 06 实际产 atoms = **331** (8122 − 7791 round 06 起始基线) | progress.json `cumulative_post_round_06.md_atoms_jsonl_total` 8122 − round 05 close 7791 | ✓ 331 |
| 4 | round 06 atoms/line ratio = 331/486 = **0.681** (drift -10% vs round 05 0.761; 4 small ass.md <50L 拉低 SENTENCE 密度) | round 06 §0.5 row 9 source 486 + actual 331 atoms | ✓ 0.681 |
| 5 | 累计 distinct domains atomized in md_atoms.jsonl = **33** (canonical post round 06; round 06 close drift 修正 progress.json STALE counter 28→33) | `python3 -c "import json; d=set(); [d.add(json.loads(l)['atom_id'][5:].split('_')[0]) for l in open('md_atoms.jsonl') if json.loads(l)['atom_id'].startswith('md_dm')]; print(len(d), sorted(d))"` | ✓ 33 (AE/AG/BE/BS/CE/CM/CO/CP/CV/DA/DD/DM/DS/DV/EC/EG/EX/FA/FT/GF/HO/IE/IS/LB/MB/MH/MI/MK/ML/MS/NV/OE/OI) |
| 6 | 累计 distinct files atomized in md_atoms.jsonl = **81** (post round 06; round 05 71 + round 06 10 = 81) | `python3 -c "import json; f=set(); [f.add(json.loads(l)['file']) for l in open('md_atoms.jsonl')]; print(len(f))"` | ✓ 81 |
| 7 | domains/ 余 = **30 domains** (63 total − 33 done = 30; post round 07 = 30 − 1 = 29) | 63 − 33 = 30 | ✓ 30 |
| 8 | Round 07 scope = **PC solo (1 domain)** × 2 files = **2 source files** (Option C continuation; round 06 PC defer 因 PC/ex 572L numberless H2 含 7 H3 children 需 Plan B 独立 sub-policy 设计 — 本 round 解决) | `ls knowledge_base/domains/PC/*.md \| grep -v spec.md` = ass + ex | ✓ 2 source files |
| 9 | Round 07 source lines total = **579** (PC/ass 7L + PC/ex 572L) | `wc -l knowledge_base/domains/PC/{assumptions,examples}.md` (7+572) | ✓ 579 |
| 10 | Round 07 size buckets: <50L=**1** (PC/ass 7L), 50-99L=**0**, 100-199L=**0**, 200-299L=**0**, 300+slice=**1** (PC/ex 572L 切 3 slice) | PC/ass(7) <50 ✓ + PC/ex(572) >300 → slice required | ✓ 1/0/0/0/1 总 2 |
| 11 | Round 07 PC/ex 572L 切片 = **3 slices** (L1-249 / L250-447 / L448-572 全部 < 300L threshold; H3 boundary aligned: L249 = end of L120 H3 "Example 1" 内容; L447 = end of L332 H3 "Example 3" 内容; L572 = file end including L556 + L562 trailing numberless H2) | sed -n '249,250p' / sed -n '447,448p' / wc -l confirm 572 | ✓ 3 slices: 249L / 198L / 125L |
| 12 | PC/ass.md H2 count = **0** (file 仅 7L: H1 + 3 numbered list narrative items; 0 H2/H3/H4) → **§2.7 round 04 lock NO trigger** + **§2.11 round 07 NEW lock NO trigger** for PC/ass | `grep -cE "^## " knowledge_base/domains/PC/assumptions.md` = 0 | ✓ 0 H2 |
| 13 | PC/ex.md H2 count = **4** (L7 numbered `## Example 1` + L58 numberless `## Relating PC and PP — Overview` + L556 numberless `## PC-PP Conclusions` + L562 numberless `## PC-PP — Suggestions for Implementing RELREC in the Submission of PK Data`) | `grep -nE "^## " knowledge_base/domains/PC/examples.md` | ✓ 4 H2 (1 numbered + 3 numberless) |
| 14 | PC/ex.md H3 count = **7** (all 7 under L58 numberless H2; L62 PC-PP Relating Datasets / L75 PC-PP Relating Records / L89 Shared PC Dataset for All Examples / L120 Example 1 (All PC records used) / L250 Example 2 (Some PC records excluded) / L332 Example 3 (Inconsistent PC usage) / L448 Example 4 (Complex exclusions)) | `grep -nE "^### " knowledge_base/domains/PC/examples.md` = 7 行 | ✓ 7 H3 (all under L58) |
| 15 | PC/ex.md H4 count = **0** | `grep -cE "^#### " knowledge_base/domains/PC/examples.md` = 0 | ✓ 0 H4 |
| 16 | Mermaid blocks in PC/ass + PC/ex = **0** → round 07 expected **0 FIGURE atoms** (vs round 06 0 + round 05 0 + round 04 0; round 03 4 in DM/ex baseline) | `grep -lE '^\`\`\`mermaid' knowledge_base/domains/PC/{assumptions,examples}.md \|\| echo NONE` → NONE | ✓ 0 mermaid in round 07 scope |
| 17 | **NEW round 07 first-time lock §2.11 Plan B sub-namespace by sib_idx** applies to **L58 only** (唯一 numberless H2 含 H3 children); L556 + L562 numberless H2 无 children 沿用 §2.7 file-root parent (round 04 lock); L7 numbered H2 沿用 §2.5 self-namespace (`§PC.1 [Example 1]`) | grep verify L58 含 7 H3 children + L556/L562 无 H3 children | ✓ Plan B 仅 1 case (L58) |
| 18 | Batch 序号续 = **batch_80..83** (round 06 末 batch_79 = OI/ex final; round 07 共 4 batches: PC/ass 1 single + PC/ex 3 sliced = 4) | round 06 §0.5 row 16 + round 06 close batch_79 final | ✓ batch_80..83 (4 batches) |
| 19 | Round 07 估 atoms = **345-475** (PC/ass 7L × 0.681 ratio = ~5; PC/ex 572L × 0.681 = ~390; total ~395 mid; lower 0.5×579=290 + upper 0.85×579=492; PC/ex SENTENCE+TABLE_ROW 密度高估高端) | 579L × 0.5 = 290; × 0.681 = 394; × 0.85 = 492 | ✓ 290-394-492 (mid ~400) |
| 20 | post Round 07 累计 md_atoms.jsonl ≈ **8,412-8,614 atoms** (mid 8,520) | 8122 + 290-492 | ✓ ~8,412-8,614 |
| 21 | post Round 07 累计 file coverage = **83/141 = 58.9%** | 81 + 2 = 83; 83/141 = 0.5887 | ✓ 58.9% (was 57.4% post round 06) |
| 22 | post Round 07 累计 distinct domain coverage = **34/63 = 54.0%** | 33 + 1 = 34; 34/63 = 0.5397 | ✓ 54.0% (was 52.4% post round 06) |
| 23 | v1.9.2 active baseline cut **2026-05-06 (commit 966e6c4)** post round 06 close — round 07 首个使用 v1.9.2 的 round; gold reference atom = `md_dmML_assn_a001` (batch_70 round 06 first atom; HEADING H1 sib=1 explicit object extracted_by per §E-1 mandate) | active baseline files: P0_writer_md_v1.9.2.md / P0_matcher_v1.9.2.md / P0_reviewer_v1.9.2.md / P0_writer_pdf_v1.9.2.md | ✓ v1.9.2 active |

**Drift 校正记录**:
- Round 06 close 时 progress.json `cumulative_post_round_05.domains_atomized` STALE counter 28 已修正; canonical going forward = `cumulative_post_round_06.domains_atomized` = 33 (+ round 07 close → 34).
- Round 07 启动时 update progress.json `current_phase` → `P2_B-03c_round_07_in_flight_acked_2026-05-06_PC_solo_4_batches_batch_80_to_83_NEW_lock_§2.11_Plan_B_sub_namespace`.
- Round 06 atoms/line ratio 0.681 (round 04 0.644 → round 05 0.761 → round 06 0.681); 多 round 实证 ratio 范围 0.59-0.78 driven by file size mix (small ass.md 拉低 / 大 ex.md 含 dense table 拉高). Round 07 PC/ex 含 1 大 narrative + 4 dense TABLE_ROW Examples + 4 LIST_ITEM trailing → 估算用 0.68-0.85 baseline (中性偏高).
- Round 07 体量 vs round 06: round 06 486L 331 atoms 10 batches; round 07 579L ~400 atoms 4 batches. **体量 = round 06 1.19× by lines / 1.21× by atoms / 0.40× by batch count** (大 file 切片 4 batches vs 10 small batches). 单 session 完成可行性: PC/ex 切片大 batch 估 atom 80-200 单批 — ctx 压力可控但需 monitor.
- post round 07 remaining = 30 − 1 = 29 domains × 2 = 58 files (估 4-5 round 完成 P2 B-03c).

---

## 1. Round 07 Scope (PC solo × 2 files; PC/ex 切 3 slice = 4 batches)

| # | Batch | Target | Lines | 估 atoms | Bucket | atom_id prefix | parent_section root | NEW lock applies |
|---|---|---|---|---|---|---|---|---|
| 1 | **batch_80** | `domains/PC/assumptions.md` | 7 | ~3-5 | <50 | `md_dmPC_assn_a` | `§PC [PC — Assumptions]` | NO (file 仅 H1 + 3 numbered list narrative; 0 H2) |
| 2 | **batch_81** | `domains/PC/examples.md` slice 1 (L1-249) | 249 | ~150-200 | 300+ slice 1/3 | `md_dmPC_ex_a` (起 a001) | `§PC [PC — Examples]` | **YES** (L58 numberless H2 + 4 H3 children L62/75/89/120) |
| 3 | **batch_82** | `domains/PC/examples.md` slice 2 (L250-447) | 198 | ~120-160 | 300+ slice 2/3 | `md_dmPC_ex_a` (续号 §2.4 multi-batch slice) | `§PC [PC — Examples]` | **YES** (L250 + L332 H3 children of L58 numberless H2) |
| 4 | **batch_83** | `domains/PC/examples.md` slice 3 (L448-572) | 125 | ~75-100 | 300+ slice 3/3 | `md_dmPC_ex_a` (续号) | `§PC [PC — Examples]` | **YES** (L448 H3 child of L58 + L556/L562 trailing numberless H2 无 children 走 §2.7 file-root) |
| **总** | 4 batches | 2 files (1 sliced 3-way) | **579** | **~345-475** (mid ~400) | — | — | — | 1 NEW lock case |

post Round 07 累计 file coverage: 81 + 2 = 83/141 = **58.9%** (was 57.4% post round 06).
post Round 07 累计 md_atoms.jsonl: 8122 + ~345-475 = ~8,467-8,597 atoms (mid ~8,520).
post Round 07 累计 distinct domain coverage: 33 + 1 = **34/63 = 54.0%** (was 52.4% post round 06).

**Round 07 vs Round 06 对照**: round 06 = 486L 331 atoms 10 small batches 0 sliced; round 07 = 579L ~400 atoms 4 batches (1 single + 3 sliced from 1 file). **体量 ≈ round 06 1.19× by lines / 1.21× by atoms / 0.40× by batch count**. 单 session 完成可行性: 4 batches dispatch 量更小但单批 atom 数更大 (slice 1 估 150-200 atoms 接近上限).

**Round 07 vs Round 03 对照** (有 sliced batch 类似): round 03 = 12 batches 741 atoms 含 4 sliced batches (ch04 ~1395L 4-way slice); round 07 = 4 batches ~400 atoms 含 3 sliced batches (PC/ex 572L 3-way slice). round 07 体量 = round 03 0.54× by atoms.

**ctx pressure forecast**: round 06 21 dispatch calls (10 writer + 10 reviewer + 1 mini-audit) 0 halt baseline; round 07 = 4 + 4 + 1 = **9 dispatch calls** (轻于 round 06 半量). 无 ctx 警戒线 forecast. 单批 PC/ex slice 1 估 200 atoms 上限 — 注意 writer ctx; 若超 250 atoms → halt + slice 再切.

---

## 2. Convention inherit (round 01-06 全 carry-forward) + §2.11 NEW round 07 first-time lock

### 2.1-2.10 全 inherit from round 01-06

(全 carry-forward, 不重复列出 — 详见 round 06 kickoff §2.1-2.10:)
- **§2.1** Heading level pattern (H1 file root / H2 examples self-namespace / H3 sub-namespace / H4+ TBD)
- **§2.2** atom_id prefix per file (4-digit 容许)
- **§2.3** atom_id 起始 a001 per file (NOT per batch; 不跨 file 续号)
- **§2.4** multi-batch single-file slice convention (round 03 lock + round 04/05/06 sustained) — **round 07 trigger** at PC/ex 572L 切 3 slice (atom_id 跨 batch 续号 a001..aNNN per file; parent_section context 跨 batch 传递 via dispatch prompt)
- **§2.5** 共通规则 (domains/ spaced format, `## Example N` → `§<D>.N [Example N]`, 跨 file 不续号) — **round 07 applies** at PC/ex L7 numbered H2 "Example 1" → children parent `§PC.1 [Example 1]`
- **§2.6** FIGURE-in-domains lock (round 03 lock) — **round 07 expected 0 FIGURE atoms** per §0.5 row 16 grep 实证 0 mermaid in 2 source files
- **§2.7** Numberless H2 in assumptions.md = file-root parent (round 04 lock FT/ass) — **round 07 NO trigger for PC/ass** per §0.5 row 12 grep 实证 0 H2 in PC/ass; **applies for L556 + L562 numberless H2 in PC/ex 无 children case** (childless numberless H2 = file-root parent sustained)
- **§2.8 R-2.8-1/2/3** (round 04 v1.9.2 candidates → v1.9.2 §E-2/E-3/E-4 codified): H1 sib_idx=1 + TABLE_HEADER sib_idx=null + extracted_by object schema
- **§2.9** LIST_ITEM sib_idx universal = null (round 03 lock, sustained)
- **§2.10** LIST_ITEM hl+sib field-explicit-null (round 05 MED-01 → v1.9.2 §E-5 codified): explicit JSON `"heading_level": null, "sibling_index": null` NOT omitted

### 2.11 **NEW round 07 first-time lock — Plan B sub-namespace by sib_idx for numberless H2 with H3 children**

**Trigger**: PC/ex L58 `## Relating PC and PP — Overview` (numberless H2) 含 7 H3 children (L62/75/89/120/250/332/448), 是 round 06 PC defer 的根本原因. 既有 §2.7 (round 04 lock) 仅处理 numberless H2 **无 children** 场景 (file-root parent inherit), 不适用此 case. 既有 §2.5 (numbered H2 self-namespace) 不能用因 H2 无编号. v1.9.1 D8 chapter root inherit (Plan A) 会让 H3 children 全部 parent 指向 file-root, 造成 L120 H3 "Example 1 (All PC records used)" 与 L7 H2 "Example 1" 同 parent 语义混乱 + 与 L7 sib_idx 冲突.

**Plan B sub-namespace by sib_idx 决断 (Bojiang ack 2026-05-06 "按你推荐的来")**:

| 原子 | atom_type | parent_section | hl | sib_idx | 说明 |
|---|---|---|---|---|---|
| L1 `# PC — Examples` | HEADING | `§PC [PC — Examples]` (self-root convention) | 1 | 1 | H1 file root sib=1 universal (R-2.8-1) |
| L7 `## Example 1` (numbered H2) | HEADING | `§PC [PC — Examples]` | 2 | 1 | numbered H2 self-namespace per §2.5; 自身 sib=1 (1st H2 in file) |
| L7 H2 之下 narrative + table atoms | (各 type) | **`§PC.1 [Example 1]`** (per §2.5) | 3+/null | per type | numbered H2 children sub-namespace |
| **L58 `## Relating PC and PP — Overview` (numberless H2 with children) ★ NEW** | HEADING | `§PC [PC — Examples]` | 2 | 2 | 自身 sib=2 (2nd H2 in file); parent = file root |
| **L58 之下 lead-in narrative** (L60) | SENTENCE 等 | **`§PC.2 [Relating PC and PP — Overview]`** ★ NEW | null | null/序 | 直接 children of L58 (无 H3 包裹) → sub-namespace by sib_idx of L58 |
| **L62/75/89/120/250/332/448 H3 children of L58** | HEADING | **`§PC.2 [Relating PC and PP — Overview]`** ★ NEW | 3 | 1..7 | sub-namespace `§PC.<sib_idx_of_parent_H2> [<title_of_parent_H2>]` consistent with §2.5 numbered format |
| **L62 H3 之下 narrative + table atoms** | (各 type) | **`§PC.2.1 [PC-PP Relating Datasets]`** ★ NEW | 4+/null | per type | H3 sub-sub-namespace 沿用 H3a 规则 (round 02 lock §2.1) by H3 sib_idx within parent H2 |
| **L120 H3 "Example 1 (All PC records used)" 之下 atoms** | (各 type) | **`§PC.2.4 [Example 1 (All PC records used)]`** ★ NEW | 4+/null | per type | sib_idx=4 (4th H3 of L58); 与 L7 H2 "Example 1" 子原子 parent `§PC.1 [Example 1]` 清晰区分 — slug 冲突自动消解 |
| L556 `## PC-PP Conclusions` (numberless H2 无 children) | HEADING | `§PC [PC — Examples]` | 2 | 3 | 自身 sib=3; **§2.7 round 04 lock 沿用** — 无 children → file-root parent (Plan A); 无 children → 不创 sub-namespace |
| L556 之下 paragraph atoms | SENTENCE | `§PC [PC — Examples]` | null | null | parent 沿用 file-root per §2.7 |
| L562 `## PC-PP — Suggestions for Implementing RELREC...` (numberless H2 无 H3 children, 含 4 numbered LIST_ITEM) | HEADING | `§PC [PC — Examples]` | 2 | 4 | 自身 sib=4; §2.7 file-root |
| L562 之下 4 LIST_ITEM | LIST_ITEM | `§PC [PC — Examples]` | null | null | LIST_ITEM hl=null sib=null per §2.9+§2.10 (explicit JSON) |

**Plan B 决断核心 = Plan A.1 拒绝原因**:
- Plan A.1 (v1.9.1 D8 chapter-root-inherit 严格): 7 H3 children of L58 全部 parent = `§PC [PC — Examples]` → 与 L7 H2 同 parent → sib_idx 跨 hl 混乱 (H3 sib 与 H2 sib 同表) + L120 H3 "Example 1" 与 L7 H2 "Example 1" slug 语义冲突
- Plan B (本 lock): L58 sub-namespace `§PC.2 [Relating PC and PP — Overview]` → 7 H3 children 自然有自己 sib_idx 1..7 + parent 与 L7 numbered H2 children 区分 + slug 冲突自动消解

**Plan B 一致性 with §2.5**: 既有 §2.5 numbered H2 children parent = `§<D>.<N> [<title>]` (N=numbered Example N); Plan B numberless H2 with children parent = `§<D>.<sib_idx> [<title>]` (sib_idx=该 H2 在 file 中的 sib_idx) — **同一格式族, 仅区分 N (numbered) vs sib_idx (numberless)**, 视觉上 user 看到 `§PC.1 [Example 1]` vs `§PC.2 [Relating PC and PP — Overview]` 自然识别.

**Plan B vs §2.7 (round 04 lock 无 children numberless H2 file-root parent) 边界**:
- 无 H3 children → §2.7 file-root parent (Plan A) — sustained
- 含 H3 children → §2.11 sub-namespace by sib_idx (Plan B) — NEW lock
- 判定逻辑: writer 检测 numberless H2 之后是否含 H3 → 是 sub-namespace, 否 file-root

**Dispatch prompt 强制注入** (新增 round 07 §2.11 lock):
- `"NEW round 07 §2.11 Plan B sub-namespace by sib_idx: numberless H2 with H3 children → children parent_section = §<D>.<sib_idx> [<title>] (consistent with §2.5 format); applies to PC/ex L58 only this round"`
- `"§2.11 boundary: numberless H2 WITHOUT H3 children sustains §2.7 file-root parent (Plan A) — applies to PC/ex L556 + L562 this round"`
- `"§2.11 sub-sub-namespace H3a sustained: H3 children with own atoms parent_section = §<D>.<sib_of_H2>.<sib_of_H3> [<title_of_H3>]"`

---

## 3. v1.9.2 prompt 入口条件 (NEW active baseline post 2026-05-06 cut)

### Writer pool (per v1.9.1 §D-8 peer-alternative + v1.9.2 §E-1 explicit JSON template mandate)
- `oh-my-claudecode:executor` (OMC primary, opus when available; **typically NOT available in default CC session — fallback expected**)
- `general-purpose` (FALLBACK peer-alternative; B-02 + round 01-06 sustained 96 batches 6586 atoms 0 writer defect post-fix cumulative; round 06 batch_72 1 schema regression 已 root-revert + re-dispatch RESOLVED, sustained quality streak intact)

### Reviewer pool (per v1.9.1 §D-8 + v1.9.2 §R-E1 schema regression sweep PRIORITY 1)
- `pr-review-toolkit:code-reviewer` (FALLBACK peer-alternative; B-02 + round 01-06 sustained 100% PASS post-fix; round 07 默认 per-batch reviewer × 4)
- **BURNED list (round 07 mini-audit 必避用)**:
  - `feature-dev:code-reviewer` (round 01 mini-audit + round 02 batch_23 burn)
  - `feature-dev:code-architect` (round 02 mini-audit burn)
  - `pr-review-toolkit:type-design-analyzer` (round 03 mini-audit burn)
  - `pr-review-toolkit:silent-failure-hunter` (round 04 mini-audit burn)
  - `pr-review-toolkit:comment-analyzer` (round 05 mini-audit burn)
  - `pr-review-toolkit:pr-test-analyzer` (round 06 mini-audit burn)
  - `pr-review-toolkit:code-reviewer` (round 04+05+06+07 per-batch ~38 burn — round 07 也将作 per-batch reviewer × 4 仍 burn for mini-audit slot)
  - `general-purpose` (writer pool sustained burn)
- **Fresh candidates (round 07 mini-audit, pr-review-toolkit family AUDIT slots 4/4 已耗尽)**:
  - `pr-review-toolkit:code-simplifier` AUDIT mode (review family, NOT yet burned in mini-audit slot — pivot to atom 字面审 mode; **9th cumulative B-03c reviewer family-pivot + 5th pr-review-toolkit AUDIT-pivot ★ extends pr-review-toolkit AUDIT pool 4→5**)
  - `Plan` AUDIT mode (planner family, NOT yet burned — pivot to "audit dispatch contract compliance" verification role)
  - `feature-dev:code-explorer` (writer family, N21 banned for atomization but **reviewer-only AUDIT role 不违反 N21** since N21 specifically targets writer role in atomization)
- **首选 (round 07 mini-audit)**: `pr-review-toolkit:code-simplifier` AUDIT mode (维持 pr-review-toolkit AUDIT family 累积; review-family 自然契合 atom 审; 5th AUDIT-pivot 延续 round 03/04/05/06 4-pr-review-toolkit-AUDIT sequence)
- **次选**: `Plan` AUDIT mode (若 code-simplifier 不可用; planner 跨 family 提供 Rule D 距离更远)

### N21 ban list (sustained per v1.7 cut + v1.9.2 §E-1 paired-sync)
`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer` (writer role; reviewer role per fresh candidates above 例外允许), `oh-my-claudecode:document-specialist`

### Rule D 硬约束
writer ≠ reviewer (不同 subagent_type, NOT 仅不同 instance).

### v1.9.2 active hooks (post 2026-05-06 cut)
- **§E-1 CRITICAL Hook 22c** (NEW round 06 prevention): dispatch prompt MUST include explicit JSON template with all 12 field names + reference working batch_70 a001 as gold reference; orchestrator preflight FAIL if missing
- **§E-2 HIGH Hook E-2-1**: H1 sib_idx=1 universal (R-2.8-1 codified)
- **§E-3 HIGH Hook E-3-2**: TABLE_HEADER sib_idx=null universal (R-2.8-2 codified)
- **§E-4 HIGH Hook E-4-3**: extracted_by object schema (R-2.8-3 codified)
- **§E-5 MED Hook E-5**: non-HEADING atoms field-explicit-null (round 05 MED-01 codified; LIST_ITEM hl+sib explicit JSON form NOT omitted)
- **§E-6 LOW Hook**: FIGURE-vs-CODE_LITERAL boundary clarification
- **Hook 22b (D-1 CRITICAL sustained)**: kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims ✓ (本 kickoff §0.5 23/23 PASS)
- **Hook D-NOTE-BQ (D-2 HIGH sustained)**: blockquote-prefix `> **Note:**` / `> **Exception:**` = atom_type NOTE
- **Hook D-D8 (D-4 sustained)**: numberless `## Overview` H2 chapter root inherit children (无 children case) — **round 07 PC/ex L556 + L562 沿用** (numberless H2 无 H3 children → file-root parent per §2.7 + Hook D-D8)
- **Round 03 §2.4 (multi-batch slice)**: round 07 trigger PC/ex 3-way slice
- **Round 03 §2.6 (FIGURE-in-domains)**: round 07 expected 0 FIGURE atoms
- **Round 03 LIST_ITEM sib_idx null**: 全 round 07 enforce
- **Round 04 §2.7 (numberless H2 in ass.md)**: round 07 NO trigger (PC/ass 0 H2)
- **Round 04 §2.8 R-2.8-1/2/3 (now v1.9.2 §E-2/E-3/E-4)**: 全 round 07 dispatch prompt 显式注入
- **Round 05 §2.10 MED-01 (now v1.9.2 §E-5)**: 全 round 07 dispatch prompt 显式 JSON form
- **NEW round 07 §2.11 (Plan B sub-namespace by sib_idx)**: 全 round 07 PC/ex dispatch prompt 显式注入

---

## 4. 自治连跑 halt 条件 (per umbrella §10.2 + round 07 specific)

任一触发 → 暂停 + ping 用户, 不强行进下一步:

1. **任一 batch §0.5 grep checksum 任一项 FAIL** (numeric drift detected at kickoff write time — 本 kickoff 已 23/23 PASS)
2. **任一 batch Rule A audit < 90% PASS rate** 或现 HIGH severity finding
3. **Schema violation / atom_id collision / 9 atom_type 任一异常** (含 v1.9.2 §R-E1 PRIORITY 1 schema regression sweep — round 06 batch_72 4-schema-regression precedent)
4. **Source markdown anomaly** 需 Rule B preserve + 业务 judgment call
5. **v1.9.2 prompt 路径 drift** — writer pool 任一不可用 OR reviewer pool 任一不可用 + FALLBACK 也不可
6. **Convention lock 首次扩展** — round 07 计划 1 NEW lock §2.11 (Plan B); 若遇到其他 H4+ 子标题 / FIGURE in PC (虽 grep 实证 0) / numbered H2 in PC/ass (虽 grep 实证 0) / numberless H2 with H3 不在 L58 之外的 surprise occurrence (虽 grep 实证仅 L58) → 暂停 + 请求 lock 扩展
7. **ctx 紧张 (剩 < 30%)** 或 session 累计已 > 1.5 hr 仍未到 round 闭环 — 主动写 handoff.md + resume prompt 给用户. **Round 07 ctx pressure 警戒线**: round 07 仅 4 batches dispatch + 单批 PC/ex slice 1 估 atom 150-200 上限 — batch_82 (PC/ex slice 2 完成 = round 中点) 后强制 ctx checkpoint
8. **Round-specific**: 任一 batch atom 数实际 outside 估算 [0.5×low, 1.5×high] → 暂停核 source / prompt drift. Round 07 各 batch 估算与下限/上限:

| Batch | est range | halt low (0.5×low) | halt high (1.5×high) |
|---|---|---|---|
| 80 PC/ass | 3-5 | <2 | >8 |
| 81 PC/ex slice 1 (L1-249) | 150-200 | <75 | >300 |
| 82 PC/ex slice 2 (L250-447) | 120-160 | <60 | >240 |
| 83 PC/ex slice 3 (L448-572) | 75-100 | <38 | >150 |

9. **Carry from round 04 (now v1.9.2 §E-2)**: H1 sib_idx 非 1 universal violation → 暂停 + 重派
10. **Carry from round 04 (now v1.9.2 §E-3)**: TABLE_HEADER sib_idx 非 null universal violation → 暂停 + 重派
11. **Carry from round 04 (now v1.9.2 §E-4)**: extracted_by 字符串简化 form (非 object schema) violation → 暂停 + 重派
12. **Carry from round 05 MED-01 (now v1.9.2 §E-5)**: LIST_ITEM atoms missing hl+sib fields (omitted instead of explicit null) → 暂停 + 重派 with explicit JSON form `"heading_level": null, "sibling_index": null`
13. **NEW round 07 §2.11 violation**: PC/ex L58 H3 children parent_section ≠ `§PC.2 [Relating PC and PP — Overview]` (i.e., writer falls back to Plan A.1 chapter-root-inherit OR uses inconsistent slug) → 暂停 + 重派 with explicit Plan B example
14. **NEW round 06 prevention (now v1.9.2 §E-1 CRITICAL)**: dispatch prompt 缺 explicit JSON template with all 12 field names + 缺 reference working atom md_dmML_assn_a001 → orchestrator preflight FAIL, 不 dispatch
15. **NEW v1.9.2 §R-E1 schema regression sweep**: writer 产物含 schema regression (verbatim_text vs verbatim, missing line_start/line_end/figure_ref, atom_type non-enum value) → reviewer 必触发 PRIORITY 1 sweep → halt + Rule B revert + re-dispatch with explicit JSON template (per round 06 batch_72 RESOLVED precedent)

**Round 07 intended 退出**:
- batch_80..83 全 PASS Rule A ≥90%
- batch_83 后派 reviewer 8-atom stratified mini-audit (2 files × 4 atoms 含 1 § 2.11 Plan B verify atom + 1 §2.7 file-root verify atom + 1 LIST_ITEM hl+sib explicit-null + 1 boundary; **+ R-2.8-1/2/3 + round 05 MED-01 + NEW §2.11 Plan B sub-namespace verify**)
- mini-audit ≥90% PASS → 单 commit (含全 4 batches + mini-audit + 3 index files 更新 + progress.json round_07 close + domain counter 33→34) + push → 一行 summary 报告 → session 自然结束 / 等用户路由词 round 08

---

## 5. Per-batch 产物 (round 01-06 模式 carry-forward + v1.9.2 §E-1 dispatch prompt 强制)

- `evidence/checkpoints/P2_B-03_batch_<NN>_md_atoms.jsonl` — writer 产物 (atomized JSONL)
- `evidence/checkpoints/rule_a_P2_B-03_batch_<NN>_verdicts.jsonl` + `_summary.md` — Rule A audit (8 boundary + 3 stratified per B-02 R-B02-3; 小文件 <30 atoms 减 stratified 至 2; round 07 极小 PC/ass ~3-5 atoms 可全审 + 0 stratified; PC/ex slice batches 估 atoms ≥75 → 标准 8+3 = 11 atom audit)
- 追加 root `md_atoms.jsonl` (`>> md_atoms.jsonl`)
- `audit_matrix.md` 行追加 (per batch + round close mini-audit)
- `trace.jsonl` phase_report 事件 + dispatch 事件 (每 subagent 调用一行)
- `_progress.json` 字段更新 (last_completed_batch / current_phase / cumulative atom count + round 07 close domain counter 33→34)

注: round 07 不写 per-batch kickoff_NN.md (round 01-06 模式 sustained) — 本 kickoff §1 batch 序列 + §2 convention (含 §2.8 R-2.8-1/2/3 + §2.10 MED-01 + §2.11 NEW Plan B) + §3 prompt + §4 halt 已含 dispatch contract.

**Dispatch prompt 强制注入** (v1.9.2 §E-1 CRITICAL + 既有 R-2.8/MED-01 + NEW §2.11 Plan B):

每 batch dispatch prompt 必 include 以下 explicit instruction (orchestrator preflight FAIL if 任一 missing):
1. **§E-1 CRITICAL: explicit JSON template with all 12 field names + reference working atom**:
   ```jsonc
   {"atom_id": "md_dmPC_<file_short>_a001", "file": "knowledge_base/domains/PC/<file>.md", "line_start": <int>, "line_end": <int>, "parent_section": "§PC [...]", "atom_type": "HEADING|SENTENCE|LIST_ITEM|TABLE_ROW|TABLE_HEADER|FIGURE|CODE_LITERAL|CROSS_REF|NOTE", "verbatim": "<byte-exact source>", "heading_level": <int|null>, "sibling_index": <int|null>, "figure_ref": <obj|null>, "cross_refs": [<obj>], "extracted_by": {"subagent_type": "<actual>", "prompt_version": "P0_writer_md_v1.9.2", "ts": "<ISO8601>"}}
   ```
   Reference working atom: `md_dmML_assn_a001` from batch_70 round 06 (HEADING H1 sib=1 explicit object extracted_by).
2. **§E-2 H1 atoms sibling_index=1 universal (R-2.8-1)**
3. **§E-3 TABLE_HEADER atoms sibling_index=null universal (R-2.8-2)**
4. **§E-4 extracted_by must be object schema (NOT string form, R-2.8-3)** with `prompt_version: "P0_writer_md_v1.9.2"`
5. **§E-5 non-HEADING atoms heading_level=null AND sibling_index=null universal — explicit JSON form, NOT omitted (round 03 lock + round 05 MED-01)**
6. **NEW §2.11 Plan B sub-namespace by sib_idx**:
   - PC/ex L7 numbered H2 children parent_section = `§PC.1 [Example 1]` (per §2.5 numbered)
   - PC/ex **L58 numberless H2 with 7 H3 children → children parent_section = `§PC.2 [Relating PC and PP — Overview]`** (NEW Plan B; sib_idx=2 is L58's own sib_idx in file)
   - PC/ex L62/75/89 H3 children of L58 (无自己 H3 children) → atoms parent_section = sub-sub-namespace `§PC.2.<H3_sib> [<H3_title>]`
   - PC/ex L120/250/332/448 H3 children of L58 (Examples 1-4 内含 dense table) → atoms parent_section = `§PC.2.<H3_sib> [<H3_title>]` where H3_sib ∈ {4, 5, 6, 7} (其 sib_idx within L58)
   - PC/ex L556 numberless H2 无 children → file-root parent `§PC [PC — Examples]` (§2.7 sustained)
   - PC/ex L562 numberless H2 无 H3 children (含 4 LIST_ITEM) → file-root parent `§PC [PC — Examples]` (§2.7 sustained); LIST_ITEM hl=null sib=null per §2.9+§2.10
7. **§2.4 multi-batch slice context (PC/ex 3-way slice)**: dispatch prompt for slice 2/3 必 include "续 atom_id from slice <N-1> last atom_id" + "parent_section context: <previous H2/H3 still in scope>" + "first atom_id of slice <N> = a<NNN> (continued from slice <N-1>)"

**Slice 1 (batch_81) entry condition**:
- atom_id 起 `md_dmPC_ex_a001`
- L1 H1 → H1 atom (sib=1 R-2.8-1)
- L7 H2 numbered Example 1 → H2 atom (sib=1, 1st H2 in file)
- L7-57 内 narrative + table → atoms parent `§PC.1 [Example 1]`
- L58 H2 numberless Overview → H2 atom (sib=2)
- L58 之下 lead-in narrative → atoms parent `§PC.2 [Relating PC and PP — Overview]` (Plan B)
- L62 H3 PC-PP Relating Datasets → H3 atom (parent `§PC.2 [Relating PC and PP — Overview]`, sib=1)
- L62-74 内 narrative + table → atoms parent `§PC.2.1 [PC-PP Relating Datasets]`
- 同样 L75-88 / L89-119 / L120-249

**Slice 2 (batch_82) entry condition**:
- atom_id 续 slice 1 末 (e.g., a150 if slice 1 emitted 150)
- 上下文 carry: L58 numberless H2 仍 in scope (parent `§PC.2 [Relating PC and PP — Overview]`)
- L250 H3 Example 2 → H3 atom (parent `§PC.2 [Relating PC and PP — Overview]`, sib=5)
- L250-331 内 atoms parent `§PC.2.5 [Example 2 (Some PC records excluded)]`
- L332 H3 Example 3 → H3 atom (sib=6)
- L332-447 内 atoms parent `§PC.2.6 [Example 3 (Inconsistent PC usage across parameters)]`

**Slice 3 (batch_83) entry condition**:
- atom_id 续 slice 2 末
- 上下文 carry: L58 numberless H2 仍 in scope 至 L555
- L448 H3 Example 4 → H3 atom (parent `§PC.2 [...]`, sib=7)
- L448-555 内 atoms parent `§PC.2.7 [Example 4 (Complex exclusions)]`
- L556 H2 numberless PC-PP Conclusions → H2 atom (parent `§PC [PC — Examples]` file-root, sib=3) ★ §2.7 sustained
- L556-561 atoms parent `§PC [PC — Examples]` (file-root)
- L562 H2 numberless Suggestions → H2 atom (parent `§PC [PC — Examples]`, sib=4) ★ §2.7 sustained
- L562-572 atoms parent `§PC [PC — Examples]`; 4 LIST_ITEM hl=null sib=null

---

## 6. Round close mini-audit (gate before round 08)

- **Trigger**: batch_83 PASS + 全部入 root md_atoms.jsonl
- **Sample**: 8-atom stratified across 2 files (PC/ass + PC/ex 3 slices = 4 batches; 2 atoms per batch). 实操: 选 boundary atom (首 + 末) + 1 NEW lock §2.11 Plan B verify atom (e.g., L62 H3 children atom checking parent_section = `§PC.2.1 [...]`) + 1 LIST_ITEM hl+sib explicit-null verify (PC/ex L562 LIST_ITEM atoms) + R-2.8-1 verify (PC/ex L1 H1 atom sib_idx=1) + R-2.8-2 verify (任一 PC/ex TABLE_HEADER atom sib_idx=null) + R-2.8-3 verify (任一 batch atom extracted_by object form with prompt_version="P0_writer_md_v1.9.2") + §E-1 verify (任一 batch dispatch prompt log 含 explicit JSON template + reference working atom)
- **Reviewer**: subagent_type **distinct from per-batch reviewer + round 01-06 mini-audit reviewers** (Rule D 跨 batch 隔离). 排除 list 见 §3 BURNED list.
  - **首选**: `pr-review-toolkit:code-simplifier` AUDIT mode (5th pr-review-toolkit AUDIT-pivot; 9th cumulative B-03c reviewer family-pivot)
  - **次选**: `Plan` AUDIT mode (planner family, NOT yet burned; 跨 family Rule D 距离更远)
- **Gate**: ≥90% functional PASS (round 01-06 mini-audit 100% post-fix 持平期待) + 10/10 round invariants:
  1. atom_id collision check (cumulative ~8,520 atoms post round 07; cross-slice 续号 verification needed for PC/ex 3-way slice — atom_id 必跨 slice 1→2→3 单调递增 a001..aNNN)
  2. Hook C-8 file prefix universal (knowledge_base/ prefix)
  3. **§2.5 numbered H2 self-namespace** (PC/ex L7 children parent `§PC.1 [Example 1]`)
  4. TABLE_HEADER Hook A1 span=1 + **R-2.8-2 sib_idx=null universal**
  5. extracted_by consistency (subagent_type + **prompt_version="P0_writer_md_v1.9.2"** post v1.9.2 cut) + **R-2.8-3 object schema (NOT string)**
  6. **§2.4 lock validation**: PC/ex 3-way slice atom_id 跨 slice 单调递增 + parent_section context 跨 slice 一致传递 (无 H2/H3 scope drift)
  7. **§2.6 lock validation (round 03 carry-forward)**: round 07 expected 0 FIGURE — verify 0 atom_type=FIGURE 出现
  8. **LIST_ITEM sib_idx null (round 03 lock) + heading_level null explicit (round 05 MED-01 codification, now v1.9.2 §E-5)**: 全 round 07 LIST_ITEM atoms hl=null AND sib=null verify (PC/ex L562 4 LIST_ITEM 必符)
  9. **§2.7 lock validation**: PC/ex L556 + L562 numberless H2 无 children → file-root parent `§PC [PC — Examples]` verify (NOT sub-namespace)
  10. **NEW §2.11 lock validation**: PC/ex L58 numberless H2 with 7 H3 children → 自身 atom parent=`§PC [PC — Examples]` sib=2 hl=2 + 7 H3 children atoms parent=`§PC.2 [Relating PC and PP — Overview]` sib=1..7 hl=3 + H3 子原子 parent=`§PC.2.<sib> [<H3 title>]` verify (Plan B 全链路 byte-exact)
- **Findings 处理**: HIGH 必修在 round 08 前 / MEDIUM 入 v1.9.3 backlog / LOW carry-forward
- **v1.9.3 cut 触发评估 (post round 07)**: v1.9.2 cut 同日 (2026-05-06) 已 fired post round 06 (10-candidate stack); round 07 NEW candidate 预期 ≤3 (§2.11 Plan B sub-namespace 经验 codification + INFO atoms/line ratio drift + 可能 LOW item); 远低 v1.9.x cut 阈值 10. 决策: round 07 close 时 review, 若 stack ≥10 cumulative (post round 06 v1.9.2 cut backlog 5 items + round 07 ≤3) 启动 cut planning, 否则 carry 到 round 08+.
- **Round 08 trigger**: round 07 mini-audit PASS + Bojiang ack → 进 round 08 (默认 alphabetical PE/PP/PR/QS/RE next 5 domains × 2 = 10 batches; 29 domains × 2 = 58 files remaining post round 07; 估 4-5 round 完成 P2 B-03c)

---

## 7. Recovery hint

若 session 中断:
- 看 `_progress.json` (主) 找 `current_phase` + `last_completed_batch`
- 看 `audit_matrix.md` P2 Bulk 表最后 PASS 行
- 看 `trace.jsonl` 尾 phase_report 事件
- 续 batch: 找 `evidence/checkpoints/P2_B-03_batch_<last_NN>_md_atoms.jsonl` 末原子的 atom_id, 下一 batch 起始 atom_id:
  - **Round 07 默认 (PC/ass, PC/ex slice 1)**: a001 (新 file 起始)
  - **Round 07 multi-batch slice (PC/ex slice 2, 3)**: 续 slice 1/2 末 (e.g., slice 2 起 a151 if slice 1 emitted 150)
- 跨 round 边界: 看 round 07 mini-audit 状态 + 用户 ack round 08 scope (默认 alphabetical PE/PP/PR/QS/RE) 决定后续
- Round 07 含 NEW lock §2.11 Plan B → halt 触发概率高于 round 06 (round 06 1 RESOLVED HALT batch_72 schema regression baseline). 若 halt 触发, 70% 概率是 §2.11 Plan B writer 误用 Plan A.1 chapter-root-inherit (orchestrator dispatch prompt 没注入 explicit Plan B example) — 看 §5 dispatch prompt 强制注入 list 第 6 项
- 25% 概率是 v1.9.2 §E-1 CRITICAL dispatch prompt 缺 explicit JSON template 触发 §R-E1 schema regression sweep (round 06 batch_72 precedent) — 看 §5 dispatch prompt 强制注入 list 第 1 项
- 5% 概率其他 (R-2.8/MED-01 carry-forward 已 v1.9.1+v1.9.2 codified, sustained 0 violation post explicit dispatch prompt)

---

## 8. 用户 ack 状态 (round 07 启动 prerequisite)

**Bojiang ack 已 (本 session, 用户路由词 "开始 work 的 06 的 Round 07" + 主 session grep verify + sub-policy ack 流程 2026-05-06)**:

1. **§1 round 07 scope = PC solo × 2 files = 4 batches** (Option C continuation; round 06 PC defer 因 numberless H2 含 H3 children + slug 冲突独立设计需要 — 本 round 解决) — Bojiang ack "按你推荐的来" → 主 session 选 PC solo (Option C continuation, 1 domain mini-round) 直接开干
2. **§2.11 NEW first-time lock Plan B sub-namespace by sib_idx** (numberless H2 with H3 children → children parent_section = `§<D>.<sib_idx> [<title>]` consistent with §2.5 numbered format; applies to PC/ex L58 only this round; L556 + L562 numberless H2 无 children 沿用 §2.7 file-root) — Bojiang ack "按你推荐的来" → Plan B 决断 lock'd
3. **§2.1-2.10 全 inherit + §2.11 NEW** (per §0.5 row 12-17 grep 实证 PC/ass 0 H2 + PC/ex 4 H2 含 1 numberless H2 with H3 + 0 mermaid)
4. **§2.8 R-2.8-1/2/3 (now v1.9.2 §E-2/E-3/E-4)** + **§2.10 round 05 MED-01 (now v1.9.2 §E-5)** + **§E-1 NEW v1.9.2 CRITICAL** — 全 round 07 dispatch prompt 显式注入 explicit JSON template + reference working atom
5. **§3 v1.9.2 prompt 路径 (NEW active baseline post 2026-05-06 cut)** — writer pool sustained; round 07 mini-audit reviewer 候选 `pr-review-toolkit:code-simplifier` AUDIT mode (5th pr-review-toolkit AUDIT-pivot)
6. **§4 halt 条件 1-15** (含 round-specific #8 atom 估算 outside [0.5×low, 1.5×high] + #9-12 R-2.8-1/2/3+MED-01 carry + #13 NEW §2.11 Plan B violation + #14 §E-1 CRITICAL + #15 NEW §R-E1 schema regression sweep)
7. **Round 07 体量 ≈ round 06 1.21× by atoms / 0.40× by batch count** — 4 batches dispatch 量小但单批 atom 数大 (slice 1 估 150-200); halt 触发概率高于 round 06 (因 NEW lock + slice convention + v1.9.2 首用)

**Scope 备选** (用户已选 Option C continuation = PC solo):
- **Option C continuation (acked 2026-05-06)**: PC solo × 2 files = 4 batches, **NEW §2.11 Plan B lock**, 单 domain 深度处理 ✓
- (Option A/B/D 备选未提出 - PC defer 是 round 06 既定决断, round 07 必处理 PC)

**用户路由词 + scope ack 激活 (acked 2026-05-06)** → **READY for autonomous dispatch** (round 07 含 1 NEW first-time lock §2.11 已 ack via "按你推荐的来", dispatch unblocked).

---

*Kickoff written 2026-05-06 post round 06 CLOSED commit 0ba2bdc + v1.9.2 cut commit 966e6c4 同日. §0.5 grep checksum 23/23 byte-exact verified. v1.9.1 §D-1 + v1.9.2 §E-1 mandatory compliance. Convention inherit per round 01-06 §2.1-2.10 + NEW round 07 §2.11 Plan B sub-namespace by sib_idx (numberless H2 with H3 children case; PC/ex L58 唯一 trigger this round). Round 07 自治连跑 dispatch ready (NEW lock §2.11 acked via "按你推荐的来"; PC solo Option C continuation 1 domain mini-round).*
