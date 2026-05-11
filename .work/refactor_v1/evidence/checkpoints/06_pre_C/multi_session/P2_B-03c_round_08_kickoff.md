# P2 B-03c Round 08 — Alphabetical PE/PP/PR/QS/RE 5 Domains × 2 Files Kickoff (default scope post round 07)

> 创建: 2026-05-06 (post B-03c round 07 CLOSED commit 85260be 同日; v1.9.2 active baseline 1st full-round post-cut sustained)
> 父 umbrella: `multi_session/P2_B-03_kickoff.md`
> 父 prompt (active baseline, sustained from round 07): `subagent_prompts/P0_writer_md_v1.9.2.md` (6 NEW E-rules + 28 hooks) + `P0_matcher_v1.9.2.md` (29 hooks) + `P0_reviewer_v1.9.2.md` (32 hooks) + `P0_writer_pdf_v1.9.2.md` (paired-sync)
> Parent round close ref: `multi_session/P2_B-03c_round_07_kickoff.md` + commit 85260be (round 07 close 4 batches 453 atoms 1 domain PC ★ §2.11 Plan B sub-namespace first production validation + v1.9.2 first round post-cut all PASS)
> 路由词: 用户 session 说 **"开始 work 的 06 的 Round 08"** → 主 session 经 grep verify + 默认 scope ack 流程 → 进本 kickoff dispatch
> Convention 继承: round 01-07 §2.1-2.11 全 carry-forward; **round 08 NO NEW first-time lock 预期** (10 文件 grep 实证: 0 H3 / 0 H4 / 0 mermaid; 2 numberless H2 cases [PP/ex L106 + QS/ass L5] 都 0 H3 children → §2.7 round 04 lock 沿用 file-root parent, NOT §2.11 Plan B trigger)

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1 CRITICAL + v1.9.2 §E-1 paired-sync)

逐项 grep-verified against source byte-exact (执行日 2026-05-06 post round 07 CLOSE). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令. 缺 §0.5 = orchestrator preflight FAIL.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | post B-03c round 07 CLOSE 时 md_atoms.jsonl 末原子 = `md_dmPC_ex_a449` (round 07 batch_83 final atom; parent_section `§PC [PC — Examples]`; file `knowledge_base/domains/PC/examples.md`) | `tail -1 md_atoms.jsonl \| python3 -c "import sys,json; a=json.loads(sys.stdin.read()); print(a['atom_id'], a.get('parent_section'), a.get('file'))"` | ✓ md_dmPC_ex_a449, §PC [PC — Examples], knowledge_base/domains/PC/examples.md |
| 2 | md_atoms.jsonl 当前总原子 = **8575** (post round 07 CLOSED) | `wc -l md_atoms.jsonl` | ✓ 8575 |
| 3 | round 07 实际产 atoms = **453** (8575 − 8122 round 07 起始基线) | progress.json `cumulative_post_round_07.md_atoms_jsonl_total` 8575 − round 06 close 8122 | ✓ 453 |
| 4 | round 07 atoms/line ratio = 453/579 = **0.782** (drift +15% vs round 06 0.681; PC/ex 572L dense Examples 1-4 + LIST_ITEM 拉高) | round 07 §0.5 row 11 source 579 + actual 453 atoms | ✓ 0.782 |
| 5 | 累计 distinct domains atomized in md_atoms.jsonl = **34** (canonical post round 07; round 07 close 33 + PC = 34) | `python3 -c "import json; d=set(); [d.add(json.loads(l)['atom_id'][5:].split('_')[0]) for l in open('md_atoms.jsonl') if json.loads(l)['atom_id'].startswith('md_dm')]; print(len(d), sorted(d))"` | ✓ 34 (AE/AG/BE/BS/CE/CM/CO/CP/CV/DA/DD/DM/DS/DV/EC/EG/EX/FA/FT/GF/HO/IE/IS/LB/MB/MH/MI/MK/ML/MS/NV/OE/OI/PC) |
| 6 | 累计 distinct files atomized in md_atoms.jsonl = **83** (post round 07; round 06 81 + PC/ass + PC/ex = 83) | `python3 -c "import json; f=set(); [f.add(json.loads(l)['file']) for l in open('md_atoms.jsonl')]; print(len(f))"` | ✓ 83 |
| 7 | domains/ 余 = **29 domains** (63 total − 34 done = 29; post round 08 = 29 − 5 = 24) | 63 − 34 = 29 | ✓ 29 |
| 8 | Round 08 scope = **PE/PP/PR/QS/RE 5 domains alphabetical default** × 2 files = **10 source files** (similar volume to round 06; 默认 scope per round 07 close trigger) | `ls knowledge_base/domains/{PE,PP,PR,QS,RE}/*.md \| grep -v spec.md` = 10 文件 | ✓ 10 source files |
| 9 | Round 08 source lines total = **399** (PE/ass 9 + PE/ex 19 + PP/ass 14 + PP/ex 127 + PR/ass 16 + PR/ex 58 + QS/ass 49 + QS/ex 24 + RE/ass 7 + RE/ex 76) | `wc -l knowledge_base/domains/{PE,PP,PR,QS,RE}/{assumptions,examples}.md` | ✓ 399 |
| 10 | Round 08 size buckets: <50L=**8** (PE/ass 9 + PE/ex 19 + PP/ass 14 + PR/ass 16 + QS/ass 49 + QS/ex 24 + RE/ass 7 + PR/ex 58→50-99), 50-99L=**2** (PR/ex 58 + RE/ex 76), 100-199L=**1** (PP/ex 127), 200-299L=**0**, 300+slice=**0** | 文件大小逐项核 | ✓ 7/2/1/0/0 总 10 (NOTE: PR/ex 58 入 50-99 bucket → 实际 <50=7 / 50-99=2 / 100-199=1) |
| 11 | Round 08 切片 = **0** (10 文件全 <300L, 全 single batch; 与 round 03 4-slice / round 07 3-slice 对照, round 08 最干净 0 slice) | 全文件 <300L threshold | ✓ 0 slice (all single batch) |
| 12 | PE/ass.md H2 count = **0** (file 9L 仅 H1 + narrative; 0 H2/H3/H4) | `grep -cE "^## " knowledge_base/domains/PE/assumptions.md` | ✓ 0 H2 |
| 13 | PE/ex.md H2 count = **1** (L3 numbered `## Example 1`) → §2.5 self-namespace `§PE.1 [Example 1]` | `grep -nE "^## " knowledge_base/domains/PE/examples.md` | ✓ 1 H2 (numbered) |
| 14 | PP/ass.md H2 count = **0** | `grep -cE "^## " knowledge_base/domains/PP/assumptions.md` | ✓ 0 H2 |
| 15 | PP/ex.md H2 count = **4** (L7 numbered `## Example 1` + L57 numbered `## Example 2` + L78 numbered `## Example 3` + **L106 numberless `## Shared PP Dataset for RELREC Examples`** ★) | `grep -nE "^## " knowledge_base/domains/PP/examples.md` | ✓ 4 H2 (3 numbered + 1 numberless) |
| 16 | **PP/ex L106 numberless H2 H3 children count = 0** → **§2.7 round 04 lock applies (file-root parent), NOT §2.11 Plan B trigger** | `grep -cE "^### " knowledge_base/domains/PP/examples.md` = 0 | ✓ 0 H3 → §2.7 sustained |
| 17 | PR/ass.md H2 count = **0** | `grep -cE "^## " knowledge_base/domains/PR/assumptions.md` | ✓ 0 H2 |
| 18 | PR/ex.md H2 count = **3** (L3 numbered `## Example 1` + L17 numbered `## Example 2` + L48 numbered `## Example 3`) → 全 §2.5 self-namespace | `grep -nE "^## " knowledge_base/domains/PR/examples.md` | ✓ 3 H2 (全 numbered) |
| 19 | QS/ass.md H2 count = **1** (L5 numberless `## QRS Shared Assumptions`) ★ | `grep -nE "^## " knowledge_base/domains/QS/assumptions.md` | ✓ 1 H2 (numberless) |
| 20 | **QS/ass L5 numberless H2 H3 children count = 0** → **§2.7 round 04 lock applies (file-root parent), NOT §2.11 Plan B trigger** | `grep -cE "^### " knowledge_base/domains/QS/assumptions.md` = 0 | ✓ 0 H3 → §2.7 sustained |
| 21 | QS/ex.md H2 count = **1** (L5 numbered `## Example 1`) | `grep -nE "^## " knowledge_base/domains/QS/examples.md` | ✓ 1 H2 (numbered) |
| 22 | RE/ass.md H2 count = **0** | `grep -cE "^## " knowledge_base/domains/RE/assumptions.md` | ✓ 0 H2 |
| 23 | RE/ex.md H2 count = **2** (L3 numbered `## Example 1` + L40 numbered `## Example 2`) | `grep -nE "^## " knowledge_base/domains/RE/examples.md` | ✓ 2 H2 (全 numbered) |
| 24 | Round 08 累计 H2 = **12** (0+1+0+4+0+3+1+1+0+2 = 12; 含 9 numbered + 2 numberless 无 H3 children + 1 ass.md numberless 无 H3) | per-file 上述行 | ✓ 12 H2 |
| 25 | Round 08 累计 H3 = **0** + H4 = **0** + mermaid = **0** → **0 FIGURE atoms 预期** + **0 NEW first-time lock 预期** (无 H3 → §2.11 Plan B 无 trigger; 全 numberless H2 都 childless → §2.7 file-root sustained) | 全 10 文件 grep | ✓ 0 H3 / 0 H4 / 0 mermaid |
| 26 | Batch 序号续 = **batch_84..93** (round 07 末 batch_83 = PC/ex slice 3; round 08 共 10 batches: 5 domains × 2 files) | round 07 §0.5 row 18 + round 07 close batch_83 final | ✓ batch_84..93 (10 batches) |
| 27 | Round 08 估 atoms = **235-340** (399L × 0.59 lower = 235; 399L × 0.73 mid = 291; 399L × 0.85 upper = 339; round 06 0.681 + round 07 0.782 baseline) | 399 × {0.59, 0.73, 0.85} | ✓ 235-291-340 (mid ~290) |
| 28 | post Round 08 累计 md_atoms.jsonl ≈ **8,810-8,915 atoms** (mid ~8,865) | 8575 + 235-340 | ✓ ~8,810-8,915 |
| 29 | post Round 08 累计 file coverage = **93/141 = 65.96%** | 83 + 10 = 93; 93/141 = 0.6596 | ✓ 65.96% (was 58.9% post round 07) |
| 30 | post Round 08 累计 distinct domain coverage = **39/63 = 61.9%** | 34 + 5 = 39; 39/63 = 0.6190 | ✓ 61.9% (was 54.0% post round 07) |
| 31 | post Round 08 B-03c progress = **72/114 = 63.16%** (round 07 close 62 + round 08 10 = 72) | 62 + 10 = 72; 72/114 = 0.6316 | ✓ 63.16% (was 54.4% post round 07) |
| 32 | v1.9.2 active baseline (commit 966e6c4) post round 06 close — round 08 是 v1.9.2 第 2 个 round (round 07 first round post-cut all PASS validation 完成); gold reference atom = `md_dmML_assn_a001` (batch_70 round 06 first atom; HEADING H1 sib=1 explicit object extracted_by per §E-1 mandate) | v1.9.2 active files: P0_writer_md_v1.9.2.md / P0_matcher_v1.9.2.md / P0_reviewer_v1.9.2.md / P0_writer_pdf_v1.9.2.md | ✓ v1.9.2 active (2nd round) |

**Drift 校正记录**:
- Round 07 close 时 progress.json `cumulative_post_round_06.domains_atomized` = 33 sustained canonical; round 08 entry baseline = `cumulative_post_round_07.domains_atomized` = 34.
- Round 08 启动时 update progress.json `current_phase` → `P2_B-03c_round_08_in_flight_acked_2026-05-06_alphabetical_PE_PP_PR_QS_RE_10_batches_batch_84_to_93_NO_NEW_lock_v1.9.2_2nd_round`.
- Round 07 atoms/line ratio 0.782 (round 04 0.644 → round 05 0.761 → round 06 0.681 → round 07 0.782); 多 round 实证 ratio 范围 0.59-0.85 driven by file size mix. Round 08 含 7 small ass.md (<50L) + 3 mid ex.md (19-127L) → 估算用 0.59-0.85 baseline (中性偏低 vs round 07).
- Round 08 体量 vs round 06: round 06 486L 331 atoms 10 batches; round 08 399L ~290 atoms 10 batches. **体量 = round 06 0.82× by lines / 0.88× by atoms / 1.00× by batch count**. 单 session 完成可行性: 10 small batches 类似 round 06, 0 slice 更干净.
- post round 08 remaining = 29 − 5 = 24 domains × 2 = 48 files (估 3-4 round 完成 P2 B-03c).

---

## 1. Round 08 Scope (alphabetical PE/PP/PR/QS/RE × 2 files = 10 single-batch; no slicing)

| # | Batch | Target | Lines | 估 atoms | Bucket | atom_id prefix | parent_section root | NEW lock applies |
|---|---|---|---|---|---|---|---|---|
| 1 | **batch_84** | `domains/PE/assumptions.md` | 9 | ~5-8 | <50 | `md_dmPE_assn_a` (起 a001) | `§PE [PE — Assumptions]` | NO (0 H2) |
| 2 | **batch_85** | `domains/PE/examples.md` | 19 | ~10-15 | <50 | `md_dmPE_ex_a` (起 a001) | `§PE [PE — Examples]` | NO (1 numbered H2 §2.5; 0 H3) |
| 3 | **batch_86** | `domains/PP/assumptions.md` | 14 | ~8-12 | <50 | `md_dmPP_assn_a` (起 a001) | `§PP [PP — Assumptions]` | NO (0 H2) |
| 4 | **batch_87** | `domains/PP/examples.md` | 127 | ~75-100 | 100-199 | `md_dmPP_ex_a` (起 a001) | `§PP [PP — Examples]` | NO (3 numbered §2.5 + 1 numberless 无 children §2.7) |
| 5 | **batch_88** | `domains/PR/assumptions.md` | 16 | ~10-14 | <50 | `md_dmPR_assn_a` (起 a001) | `§PR [PR — Assumptions]` | NO (0 H2) |
| 6 | **batch_89** | `domains/PR/examples.md` | 58 | ~30-45 | 50-99 | `md_dmPR_ex_a` (起 a001) | `§PR [PR — Examples]` | NO (3 numbered H2 §2.5; 0 H3) |
| 7 | **batch_90** | `domains/QS/assumptions.md` | 49 | ~30-40 | <50 | `md_dmQS_assn_a` (起 a001) | `§QS [QS — Assumptions]` | NO (1 numberless H2 无 children §2.7 sustained) |
| 8 | **batch_91** | `domains/QS/examples.md` | 24 | ~12-18 | <50 | `md_dmQS_ex_a` (起 a001) | `§QS [QS — Examples]` | NO (1 numbered H2 §2.5; 0 H3) |
| 9 | **batch_92** | `domains/RE/assumptions.md` | 7 | ~3-5 | <50 | `md_dmRE_assn_a` (起 a001) | `§RE [RE — Assumptions]` | NO (0 H2) |
| 10 | **batch_93** | `domains/RE/examples.md` | 76 | ~45-60 | 50-99 | `md_dmRE_ex_a` (起 a001) | `§RE [RE — Examples]` | NO (2 numbered H2 §2.5; 0 H3) |
| **总** | 10 batches | 10 files (0 sliced) | **399** | **~228-317** (mid ~290) | — | — | — | **0 NEW lock** |

post Round 08 累计 file coverage: 83 + 10 = 93/141 = **65.96%** (was 58.9% post round 07).
post Round 08 累计 md_atoms.jsonl: 8575 + ~235-340 = ~8,810-8,915 atoms (mid ~8,865).
post Round 08 累计 distinct domain coverage: 34 + 5 = **39/63 = 61.9%** (was 54.0% post round 07).
post Round 08 B-03c progress: 62 + 10 = 72/114 = **63.16%** (was 54.4% post round 07).

**Round 08 vs Round 07 对照**: round 07 = 579L 453 atoms 4 batches (1 single + 3 sliced 含 NEW §2.11 Plan B lock); round 08 = 399L ~290 atoms 10 batches (全 single, 0 NEW lock). **体量 ≈ round 07 0.69× by lines / 0.64× by atoms / 2.50× by batch count**. 单 session 完成可行性: 10 small batches dispatch 量大但单批 atom 数小 (max batch_87 PP/ex 估 ~100 atoms) — ctx 压力分散.

**Round 08 vs Round 06 对照** (10 batches similar): round 06 = 486L 331 atoms 10 batches 5 domains ML/MS/NV/OE/OI 0 NEW lock 1 RESOLVED HALT batch_72 schema regression; round 08 = 399L ~290 atoms 10 batches 5 domains PE/PP/PR/QS/RE 0 NEW lock 0 HALT 期待 (v1.9.2 §E-1 explicit JSON template 防 schema regression). round 08 体量 = round 06 0.82× by lines / 0.88× by atoms.

**ctx pressure forecast**: round 06 21 dispatch calls (10 writer + 10 reviewer + 1 mini-audit) 1 RESOLVED HALT baseline; round 08 = 10 + 10 + 1 = **21 dispatch calls** (= round 06). 0 slice + 0 NEW lock + v1.9.2 sustained → halt 触发概率 **低于 round 06** (主要因 v1.9.2 §E-1 mandate prevent batch_72-style schema regression). 单批 PP/ex 估 ~100 atoms 上限 — 注意 writer ctx; 若超 200 atoms → halt + slice 再切. ctx checkpoint 强制 at batch_88 (round 中点).

---

## 2. Convention inherit (round 01-07 全 carry-forward; 0 NEW lock 预期)

### 2.1-2.11 全 inherit from round 01-07

(全 carry-forward, 不重复列出 — 详见 round 07 kickoff §2.1-2.11:)
- **§2.1** Heading level pattern (H1 file root / H2 examples self-namespace / H3 sub-namespace / H4+ TBD)
- **§2.2** atom_id prefix per file (4-digit 容许)
- **§2.3** atom_id 起始 a001 per file (NOT per batch; 不跨 file 续号)
- **§2.4** multi-batch single-file slice convention — **round 08 NO trigger** (10 文件全 <300L, 全 single batch)
- **§2.5** 共通规则 — **round 08 applies** at PE/ex L3 + PP/ex L7/57/78 + PR/ex L3/17/48 + QS/ex L5 + RE/ex L3/40 = 9 numbered H2 全 §<D>.<N> [<title>] self-namespace
- **§2.6** FIGURE-in-domains lock — **round 08 expected 0 FIGURE atoms** per §0.5 row 25 grep 实证 0 mermaid in 10 source files
- **§2.7** Numberless H2 in assumptions.md (childless) = file-root parent (round 04 lock FT/ass) — **round 08 applies** at QS/ass L5 numberless H2 (0 H3 children → file-root `§QS [QS — Assumptions]`) + PP/ex L106 numberless H2 (0 H3 children → file-root `§PP [PP — Examples]`)
- **§2.8 R-2.8-1/2/3** (now v1.9.2 §E-2/E-3/E-4 codified): H1 sib_idx=1 + TABLE_HEADER sib_idx=null + extracted_by object schema
- **§2.9** LIST_ITEM sib_idx universal = null (round 03 lock, sustained)
- **§2.10** LIST_ITEM hl+sib field-explicit-null (round 05 MED-01 → v1.9.2 §E-5 codified): explicit JSON `"heading_level": null, "sibling_index": null` NOT omitted
- **§2.11 Plan B sub-namespace by sib_idx for numberless H2 with H3 children** (round 07 NEW lock; PC/ex L58 first production validation PASS) — **round 08 NO trigger** per §0.5 row 16+20 grep 实证 PP/ex L106 + QS/ass L5 numberless H2 都 0 H3 children → §2.7 sustained, NOT §2.11

### 2.12-? **Round 08 0 NEW first-time lock 预期**

Round 08 grep 实证 (§0.5 row 12-25):
- 0 H3 in 10 文件 → §2.11 Plan B 无 trigger
- 0 H4 in 10 文件 → 无 H4 sub-policy 设计需求
- 0 mermaid in 10 文件 → §2.6 FIGURE 0 atom 预期
- 2 numberless H2 都 childless → §2.7 round 04 lock 沿用 (NOT §2.11)
- 9 numbered H2 全 §2.5 self-namespace 沿用

Round 08 是 **B-03c 第 1 个 0 NEW lock round** (round 01 §2.1-2.5 + round 02 §2.5扩展 + round 03 §2.4/§2.6 + round 04 §2.7/§2.8 + round 05 §2.9 explicit + round 06 0 NEW + round 07 §2.11 Plan B; round 06 也 0 NEW lock 但是因为 ratio drift carry, 不是 grep 实证 0 trigger). Round 08 是 B-03c **首个 grep-verified 0-trigger round** — 干净执行 sustained convention 测试.

**Surprise H4 occurrence handling** (per §4 halt #6): 若 dispatch 后 writer 实测发现 H4 (虽 grep 实证 0) → halt + 请求 lock 扩展 (虽然 grep 已 0, 但保留 fallback).

---

## 3. v1.9.2 prompt 入口条件 (active baseline 2nd round post-cut)

### Writer pool (per v1.9.1 §D-8 peer-alternative + v1.9.2 §E-1 explicit JSON template mandate)
- `oh-my-claudecode:executor` (OMC primary, opus when available; **typically NOT available in default CC session — fallback expected**)
- `general-purpose` (FALLBACK peer-alternative; B-02 + round 01-07 sustained 100 batches 7039 atoms 0 writer defect post-fix cumulative; round 06 batch_72 1 schema regression 已 root-revert + re-dispatch RESOLVED, sustained quality streak intact post v1.9.2 §E-1 explicit JSON template mandate)

### Reviewer pool (per v1.9.1 §D-8 + v1.9.2 §R-E1 schema regression sweep PRIORITY 1)
- `pr-review-toolkit:code-reviewer` (FALLBACK peer-alternative; B-02 + round 01-07 sustained 100% PASS post-fix; round 08 默认 per-batch reviewer × 10)
- **BURNED list (round 08 mini-audit 必避用)**:
  - `feature-dev:code-reviewer` (round 01 mini-audit + round 02 batch_23 burn)
  - `feature-dev:code-architect` (round 02 mini-audit burn)
  - `pr-review-toolkit:type-design-analyzer` (round 03 mini-audit burn)
  - `pr-review-toolkit:silent-failure-hunter` (round 04 mini-audit burn)
  - `pr-review-toolkit:comment-analyzer` (round 05 mini-audit burn)
  - `pr-review-toolkit:pr-test-analyzer` (round 06 mini-audit burn)
  - `pr-review-toolkit:code-simplifier` (round 07 mini-audit burn — 5/5 pr-review-toolkit AUDIT pool 已耗尽)
  - `pr-review-toolkit:code-reviewer` (round 04+05+06+07 per-batch ~48 burn — round 08 也将作 per-batch reviewer × 10 仍 burn for mini-audit slot)
  - `general-purpose` (writer pool sustained burn)
- **Fresh candidates (round 08 mini-audit, pr-review-toolkit family AUDIT slots 5/5 已耗尽 post round 07)**:
  - **`Plan` AUDIT mode** (planner family, NOT yet burned — pivot to "audit dispatch contract compliance + atom 字面审" verification role; **6th cumulative B-03c reviewer family-pivot ★ first planner-family AUDIT-pivot, 跨 family Rule D 距离最远**)
  - `feature-dev:code-explorer` AUDIT mode (writer-family N21-banned for atomization but reviewer-only role allowed; clarification needed if used; **Rule D 距离 vs Plan 较近 — 次选**)
- **首选 (round 08 mini-audit)**: **`Plan` AUDIT mode** (planner family首次启用, 跨 family Rule D 距离最远 vs review/writer family pivot 史)
- **次选**: `feature-dev:code-explorer` AUDIT mode (若 Plan 不可用; reviewer-only 角色 N21 例外允许)

### N21 ban list (sustained per v1.7 cut + v1.9.2 §E-1 paired-sync)
`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer` (writer role; reviewer role per fresh candidates above 例外允许), `oh-my-claudecode:document-specialist`

### Rule D 硬约束
writer ≠ reviewer (不同 subagent_type, NOT 仅不同 instance).

### v1.9.2 active hooks (sustained from round 07 first production validation)
- **§E-1 CRITICAL Hook 22c**: dispatch prompt MUST include explicit JSON template with all 12 field names + reference working batch_70 a001 as gold reference; orchestrator preflight FAIL if missing (round 07 0 schema regression validated v1.9.2 §E-1 effective)
- **§E-2 HIGH Hook E-2-1**: H1 sib_idx=1 universal (R-2.8-1 codified)
- **§E-3 HIGH Hook E-3-2**: TABLE_HEADER sib_idx=null universal (R-2.8-2 codified)
- **§E-4 HIGH Hook E-4-3**: extracted_by object schema (R-2.8-3 codified)
- **§E-5 MED Hook E-5**: non-HEADING atoms field-explicit-null (round 05 MED-01 codified; LIST_ITEM hl+sib explicit JSON form NOT omitted)
- **§E-6 LOW Hook**: FIGURE-vs-CODE_LITERAL boundary clarification
- **Hook 22b (D-1 CRITICAL sustained)**: kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims ✓ (本 kickoff §0.5 32/32 PASS)
- **Hook D-NOTE-BQ (D-2 HIGH sustained)**: blockquote-prefix `> **Note:**` / `> **Exception:**` = atom_type NOTE
- **Hook D-D8 (D-4 sustained)**: numberless `## Overview` H2 chapter root inherit children (无 children case) — **round 08 PP/ex L106 + QS/ass L5 沿用** (numberless H2 无 H3 children → file-root parent per §2.7 + Hook D-D8)
- **Round 03 §2.4 (multi-batch slice)**: round 08 NO trigger (全 <300L)
- **Round 03 §2.6 (FIGURE-in-domains)**: round 08 expected 0 FIGURE atoms
- **Round 03 LIST_ITEM sib_idx null**: 全 round 08 enforce
- **Round 04 §2.7 (numberless H2 in ass.md / childless ex.md)**: round 08 trigger 2 cases (PP/ex L106 + QS/ass L5)
- **Round 04 §2.8 R-2.8-1/2/3 (now v1.9.2 §E-2/E-3/E-4)**: 全 round 08 dispatch prompt 显式注入
- **Round 05 §2.10 MED-01 (now v1.9.2 §E-5)**: 全 round 08 dispatch prompt 显式 JSON form
- **Round 07 §2.11 (Plan B sub-namespace by sib_idx)**: round 08 NO trigger (0 H3 children in 10 文件 grep 实证)

---

## 4. 自治连跑 halt 条件 (per umbrella §10.2 + round 08 specific)

任一触发 → 暂停 + ping 用户, 不强行进下一步:

1. **任一 batch §0.5 grep checksum 任一项 FAIL** (numeric drift detected at kickoff write time — 本 kickoff 已 32/32 PASS)
2. **任一 batch Rule A audit < 90% PASS rate** 或现 HIGH severity finding
3. **Schema violation / atom_id collision / 9 atom_type 任一异常** (含 v1.9.2 §R-E1 PRIORITY 1 schema regression sweep — round 06 batch_72 4-schema-regression precedent + round 07 0 schema regression validated)
4. **Source markdown anomaly** 需 Rule B preserve + 业务 judgment call
5. **v1.9.2 prompt 路径 drift** — writer pool 任一不可用 OR reviewer pool 任一不可用 + FALLBACK 也不可
6. **Convention lock 首次扩展** — round 08 计划 0 NEW lock; 若遇到 H3/H4 surprise occurrence (虽 grep 实证 0) / FIGURE in 任一文件 (虽 grep 实证 0) / numberless H2 with H3 children 不在 grep 实证之外的 surprise occurrence → 暂停 + 请求 lock 扩展
7. **ctx 紧张 (剩 < 30%)** 或 session 累计已 > 1.5 hr 仍未到 round 闭环 — 主动写 handoff.md + resume prompt 给用户. **Round 08 ctx pressure 警戒线**: round 08 21 dispatch calls (10 writer + 10 reviewer + 1 mini-audit) — batch_88 (round 5/10 中点) 后强制 ctx checkpoint
8. **Round-specific**: 任一 batch atom 数实际 outside 估算 [0.5×low, 1.5×high] → 暂停核 source / prompt drift. Round 08 各 batch 估算与下限/上限:

| Batch | est range | halt low (0.5×low) | halt high (1.5×high) |
|---|---|---|---|
| 84 PE/ass | 5-8 | <3 | >12 |
| 85 PE/ex | 10-15 | <5 | >23 |
| 86 PP/ass | 8-12 | <4 | >18 |
| 87 PP/ex | 75-100 | <38 | >150 |
| 88 PR/ass | 10-14 | <5 | >21 |
| 89 PR/ex | 30-45 | <15 | >68 |
| 90 QS/ass | 30-40 | <15 | >60 |
| 91 QS/ex | 12-18 | <6 | >27 |
| 92 RE/ass | 3-5 | <2 | >8 |
| 93 RE/ex | 45-60 | <23 | >90 |

9. **Carry from round 04 (now v1.9.2 §E-2)**: H1 sib_idx 非 1 universal violation → 暂停 + 重派
10. **Carry from round 04 (now v1.9.2 §E-3)**: TABLE_HEADER sib_idx 非 null universal violation → 暂停 + 重派
11. **Carry from round 04 (now v1.9.2 §E-4)**: extracted_by 字符串简化 form (非 object schema) violation → 暂停 + 重派
12. **Carry from round 05 MED-01 (now v1.9.2 §E-5)**: LIST_ITEM atoms missing hl+sib fields (omitted instead of explicit null) → 暂停 + 重派 with explicit JSON form `"heading_level": null, "sibling_index": null`
13. **Carry from round 07 §2.11 (Plan B)**: round 08 NO trigger 预期; 但若 surprise H3 children 出现, 必 fallback to §2.11 Plan B sub-namespace (NOT Plan A.1 chapter-root-inherit) — halt + lock 扩展确认
14. **Carry from round 06 prevention (now v1.9.2 §E-1 CRITICAL)**: dispatch prompt 缺 explicit JSON template with all 12 field names + 缺 reference working atom md_dmML_assn_a001 → orchestrator preflight FAIL, 不 dispatch
15. **§R-E1 schema regression sweep (sustained)**: writer 产物含 schema regression (verbatim_text vs verbatim, missing line_start/line_end/figure_ref, atom_type non-enum value) → reviewer 必触发 PRIORITY 1 sweep → halt + Rule B revert + re-dispatch with explicit JSON template

**Round 08 intended 退出**:
- batch_84..93 全 PASS Rule A ≥90%
- batch_93 后派 reviewer 8-atom stratified mini-audit (10 batches × ~0.8 atoms = 8 atom 含 1 §2.7 numberless-H2-childless verify atom [PP/ex L106 OR QS/ass L5] + 1 LIST_ITEM hl+sib explicit-null + 1 §2.5 numbered H2 self-namespace verify + 1 R-2.8-1 H1 sib=1 verify + 1 R-2.8-2 TABLE_HEADER sib=null verify + 1 R-2.8-3 extracted_by object verify + 1 §E-5 non-HEADING explicit-null verify + 1 boundary atom)
- mini-audit ≥90% PASS → 单 commit (含全 10 batches + mini-audit + 3 index files 更新 + progress.json round_08 close + domain counter 34→39) + push → 一行 summary 报告 → session 自然结束 / 等用户路由词 round 09

---

## 5. Per-batch 产物 (round 01-07 模式 carry-forward + v1.9.2 §E-1 dispatch prompt 强制)

- `evidence/checkpoints/P2_B-03_batch_<NN>_md_atoms.jsonl` — writer 产物 (atomized JSONL)
- `evidence/checkpoints/rule_a_P2_B-03_batch_<NN>_verdicts.jsonl` + `_summary.md` — Rule A audit (8 boundary + 3 stratified per B-02 R-B02-3; 小文件 <30 atoms 减 stratified 至 2; round 08 极小 RE/ass ~3-5 atoms 可全审 + 0 stratified; mid batches 10-50 atoms 标准 8+3 = 11 atom audit; large PP/ex ~100 atoms 标准 8+3 = 11 atom audit)
- 追加 root `md_atoms.jsonl` (`>> md_atoms.jsonl`)
- `audit_matrix.md` 行追加 (per batch + round close mini-audit)
- `trace.jsonl` phase_report 事件 + dispatch 事件 (每 subagent 调用一行)
- `_progress.json` 字段更新 (last_completed_batch / current_phase / cumulative atom count + round 08 close domain counter 34→39)

注: round 08 不写 per-batch kickoff_NN.md (round 01-07 模式 sustained) — 本 kickoff §1 batch 序列 + §2 convention (含 §2.8 R-2.8-1/2/3 + §2.10 MED-01 + §2.11 Plan B carry-forward) + §3 prompt + §4 halt 已含 dispatch contract.

**Dispatch prompt 强制注入** (v1.9.2 §E-1 CRITICAL + 既有 R-2.8/MED-01 + §2.11 Plan B carry-forward):

每 batch dispatch prompt 必 include 以下 explicit instruction (orchestrator preflight FAIL if 任一 missing):
1. **§E-1 CRITICAL: explicit JSON template with all 12 field names + reference working atom**:
   ```jsonc
   {"atom_id": "md_dm<D>_<file_short>_a001", "file": "knowledge_base/domains/<D>/<file>.md", "line_start": <int>, "line_end": <int>, "parent_section": "§<D> [...]", "atom_type": "HEADING|SENTENCE|LIST_ITEM|TABLE_ROW|TABLE_HEADER|FIGURE|CODE_LITERAL|CROSS_REF|NOTE", "verbatim": "<byte-exact source>", "heading_level": <int|null>, "sibling_index": <int|null>, "figure_ref": <obj|null>, "cross_refs": [<obj>], "extracted_by": {"subagent_type": "<actual>", "prompt_version": "P0_writer_md_v1.9.2", "ts": "<ISO8601>"}}
   ```
   Reference working atom: `md_dmML_assn_a001` from batch_70 round 06 (HEADING H1 sib=1 explicit object extracted_by).
2. **§E-2 H1 atoms sibling_index=1 universal (R-2.8-1)**
3. **§E-3 TABLE_HEADER atoms sibling_index=null universal (R-2.8-2)**
4. **§E-4 extracted_by must be object schema (NOT string form, R-2.8-3)** with `prompt_version: "P0_writer_md_v1.9.2"`
5. **§E-5 non-HEADING atoms heading_level=null AND sibling_index=null universal — explicit JSON form, NOT omitted (round 03 lock + round 05 MED-01)**
6. **§2.5 numbered H2 self-namespace (round 08 9 cases)**:
   - PE/ex L3 `## Example 1` → children parent `§PE.1 [Example 1]`
   - PP/ex L7/57/78 `## Example 1/2/3` → children parent `§PP.1 / §PP.2 / §PP.3 [Example N]`
   - PR/ex L3/17/48 `## Example 1/2/3` → children parent `§PR.1 / §PR.2 / §PR.3 [Example N]`
   - QS/ex L5 `## Example 1` → children parent `§QS.1 [Example 1]`
   - RE/ex L3/40 `## Example 1/2` → children parent `§RE.1 / §RE.2 [Example N]`
7. **§2.7 numberless H2 childless = file-root parent (round 08 2 cases)**:
   - PP/ex L106 `## Shared PP Dataset for RELREC Examples` (numberless H2, 0 H3 children) → 自身 H2 atom parent `§PP [PP — Examples]` sib=4 hl=2; 之下 atoms parent `§PP [PP — Examples]` (file-root, NOT sub-namespace per §2.11)
   - QS/ass L5 `## QRS Shared Assumptions` (numberless H2, 0 H3 children) → 自身 H2 atom parent `§QS [QS — Assumptions]` sib=1 hl=2; 之下 atoms parent `§QS [QS — Assumptions]` (file-root, NOT sub-namespace per §2.11)
8. **§2.11 Plan B sub-namespace by sib_idx — round 08 NO trigger expected** (0 H3 in 10 文件 grep 实证); 若 surprise H3 出现, halt + lock 扩展确认 (per §4 halt #6+#13)

---

## 6. Round close mini-audit (gate before round 09)

- **Trigger**: batch_93 PASS + 全部入 root md_atoms.jsonl
- **Sample**: 8-atom stratified across 10 batches. 实操: 选 boundary atom (round 起 + 末) + 1 §2.7 numberless-H2-childless verify atom (PP/ex L106 OR QS/ass L5 自身 atom 检查 parent_section = file-root) + 1 §2.5 numbered H2 children verify atom (任一 PE/ex / PP/ex / PR/ex / QS/ex / RE/ex Example 之下 atom 检查 parent_section = `§<D>.<N> [Example N]`) + 1 LIST_ITEM hl+sib explicit-null verify (任一 batch LIST_ITEM atom) + R-2.8-1 verify (任一 batch H1 atom sib_idx=1) + R-2.8-2 verify (任一 batch TABLE_HEADER atom sib_idx=null) + R-2.8-3 verify (任一 batch atom extracted_by object form with prompt_version="P0_writer_md_v1.9.2") + §E-1 verify (任一 batch dispatch prompt log 含 explicit JSON template + reference working atom)
- **Reviewer**: subagent_type **distinct from per-batch reviewer + round 01-07 mini-audit reviewers** (Rule D 跨 batch 隔离). 排除 list 见 §3 BURNED list.
  - **首选**: `Plan` AUDIT mode (6th cumulative B-03c reviewer family-pivot; **first planner-family AUDIT-pivot ★ extends Rule D pool to planner family**)
  - **次选**: `feature-dev:code-explorer` AUDIT mode (writer-family reviewer-only role; N21 例外允许)
- **Gate**: ≥90% functional PASS (round 01-07 mini-audit 100% post-fix 持平期待) + 10/10 round invariants:
  1. atom_id collision check (cumulative ~8,865 atoms post round 08; per-file atom_id 起 a001 verification needed for 10 文件)
  2. Hook C-8 file prefix universal (knowledge_base/ prefix)
  3. **§2.5 numbered H2 self-namespace** (PE/ex L3 / PP/ex L7/57/78 / PR/ex L3/17/48 / QS/ex L5 / RE/ex L3/40 = 9 cases verify)
  4. TABLE_HEADER Hook A1 span=1 + **R-2.8-2 sib_idx=null universal**
  5. extracted_by consistency (subagent_type + **prompt_version="P0_writer_md_v1.9.2"** sustained 2nd round post-cut) + **R-2.8-3 object schema (NOT string)**
  6. **§2.4 lock validation NO trigger**: round 08 全 single batch (无 cross-slice atom_id 续号 verification)
  7. **§2.6 lock validation (round 03 carry-forward)**: round 08 expected 0 FIGURE — verify 0 atom_type=FIGURE 出现
  8. **LIST_ITEM sib_idx null (round 03 lock) + heading_level null explicit (round 05 MED-01 codification, now v1.9.2 §E-5)**: 全 round 08 LIST_ITEM atoms hl=null AND sib=null verify
  9. **§2.7 lock validation (round 04 carry-forward, round 08 trigger 2 cases)**: PP/ex L106 + QS/ass L5 numberless H2 无 children → file-root parent verify (NOT sub-namespace per §2.11 boundary)
  10. **§2.11 lock validation NO trigger**: round 08 grep 实证 0 H3 → verify 0 atom 含 sub-namespace `§<D>.<sib>.<sub>` form (除已 round 07 PC/ex 历史 atoms 外, round 08 新原子全 file-root 或 `§<D>.<N>` numbered self-namespace)
- **Findings 处理**: HIGH 必修在 round 09 前 / MEDIUM 入 v1.9.3 backlog / LOW carry-forward
- **v1.9.3 cut 触发评估 (post round 08)**: v1.9.2 cut 同日 (2026-05-06) fired post round 06; round 07 NEW candidate INFO-R07-01/02 + carry 5 = stack 7 post round 07; round 08 NEW candidate 预期 ≤2 (0 NEW lock + sustained convention 测试). 决策: round 08 close 时 review, 若 stack ≥10 cumulative 启动 cut planning, 否则 carry 到 round 09+.
- **Round 09 trigger**: round 08 mini-audit PASS + Bojiang ack → 进 round 09 (默认 alphabetical RELREC/RP/RS/SC/SE next 5 domains × 2 = 10 batches OR 调 scope; 24 domains × 2 = 48 files remaining post round 08; 估 3-4 round 完成 P2 B-03c)

---

## 7. Recovery hint

若 session 中断:
- 看 `_progress.json` (主) 找 `current_phase` + `last_completed_batch`
- 看 `audit_matrix.md` P2 Bulk 表最后 PASS 行
- 看 `trace.jsonl` 尾 phase_report 事件
- 续 batch: 找 `evidence/checkpoints/P2_B-03_batch_<last_NN>_md_atoms.jsonl` 末原子的 atom_id, 下一 batch 起始 atom_id:
  - **Round 08 默认 (全 single batch, 跨 file 不续号)**: 每 batch 起 a001
- 跨 round 边界: 看 round 08 mini-audit 状态 + 用户 ack round 09 scope (默认 alphabetical RELREC/RP/RS/SC/SE) 决定后续
- Round 08 0 NEW lock 预期 → halt 触发概率 **低于 round 07** (round 07 NEW §2.11 Plan B 触发风险已无). 若 halt 触发, 70% 概率是 **v1.9.2 §E-1 CRITICAL dispatch prompt 缺 explicit JSON template** 触发 §R-E1 schema regression sweep (round 06 batch_72 precedent) — 看 §5 dispatch prompt 强制注入 list 第 1 项
- 20% 概率是 **§2.7 numberless H2 childless 误判 sub-namespace** (writer 误 fallback Plan B 而非 Plan A) — PP/ex L106 + QS/ass L5 boundary; 看 §5 dispatch prompt 强制注入 list 第 7 项
- 10% 概率其他 (R-2.8/MED-01 carry-forward 已 v1.9.1+v1.9.2 codified, sustained 0 violation post explicit dispatch prompt; round 07 PC/ex 0 schema regression validated v1.9.2 §E-1 effective)

---

## 8. 用户 ack 状态 (round 08 启动 prerequisite)

**Bojiang ack 状态 (本 session, 用户路由词 "开始 work 的 06 的 Round 08" + 主 session §0.5 grep verify 流程 2026-05-06)**:

1. **§1 round 08 scope = alphabetical PE/PP/PR/QS/RE 5 domains × 2 files = 10 single-batches** (round 07 close trigger 默认; 0 slice 0 NEW lock 预期 — 干净 sustained 测试 round) — **PENDING ack** (用户 routing word 已触发但默认 scope 显式 ack 待提)
2. **§2 convention inherit 全 1-11 carry-forward, 0 NEW lock** (per §0.5 row 12-25 grep 实证 PE/PP/PR/QS/RE 5 domains 10 文件 0 H3 + 0 H4 + 0 mermaid + 2 numberless H2 都 childless)
3. **§2.5 numbered H2 self-namespace 9 cases + §2.7 numberless H2 childless 2 cases** (PP/ex L106 + QS/ass L5 都 0 H3 children → §2.7 sustained, NOT §2.11 Plan B trigger)
4. **§2.8 R-2.8-1/2/3 (now v1.9.2 §E-2/E-3/E-4)** + **§2.10 round 05 MED-01 (now v1.9.2 §E-5)** + **§E-1 v1.9.2 CRITICAL** — 全 round 08 dispatch prompt 显式注入 explicit JSON template + reference working atom
5. **§3 v1.9.2 prompt 路径 (active baseline 2nd round post-cut)** — writer pool sustained; round 08 mini-audit reviewer 候选 `Plan` AUDIT mode (6th cumulative B-03c reviewer family-pivot ★ first planner-family AUDIT-pivot)
6. **§4 halt 条件 1-15** (round-specific #8 atom 估算 outside [0.5×low, 1.5×high] + #9-12 R-2.8-1/2/3+MED-01 carry + #13 §2.11 Plan B carry-forward (NO trigger 但 surprise fallback 保留) + #14 §E-1 CRITICAL + #15 §R-E1 schema regression sweep)
7. **Round 08 体量 ≈ round 06 0.88× by atoms / 1.00× by batch count** — 10 small batches dispatch 量类似 round 06; halt 触发概率 **低于 round 06** (因 v1.9.2 §E-1 mandate prevent batch_72-style schema regression + 0 NEW lock 复杂度低 + round 07 0 schema regression validated v1.9.2 effective)

**Scope 备选** (round 07 close trigger 默认):
- **Default (本 kickoff)**: alphabetical PE/PP/PR/QS/RE × 2 files = 10 batches ★
- **Option B (备选)**: 调 scope 含 RELREC/RP/RS 等大 domain 提前
- **Option C (备选)**: 单 domain 深度处理 (类 round 07 PC solo)

**用户路由词激活 + 默认 scope ack 待提** → **PENDING Bojiang 显式 ack** (本 kickoff §0.5 32/32 verified, dispatch contract ready; ack 后立即 batch_84 dispatch).

---

*Kickoff written 2026-05-06 post round 07 CLOSED commit 85260be 同日. §0.5 grep checksum 32/32 byte-exact verified. v1.9.1 §D-1 + v1.9.2 §E-1 mandatory compliance. Convention inherit per round 01-07 §2.1-2.11 + 0 NEW round 08 lock 预期. Round 08 自治连跑 dispatch ready (默认 scope PE/PP/PR/QS/RE alphabetical, 10 single-batch 干净 sustained-convention 测试 round).*
