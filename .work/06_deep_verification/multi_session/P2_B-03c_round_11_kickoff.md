# P2 B-03c Round 11 — Alphabetical SU/SUPPQUAL/SV/TD 4 Domains × 2 Files Kickoff (TA solo deferred to round 12 per Bojiang ack 2026-05-07 Option B)

> 创建: 2026-05-07 (post B-03c round 10 CLOSED commit 8deb94c; **v1.9.3 active baseline 2nd production validation round** — 4 paired-sync prompts writer_md/pdf/matcher/reviewer + 3 F-rules §F-1/F-2/F-3 sustained validation)
> 父 umbrella: `multi_session/P2_B-03_kickoff.md`
> 父 prompt (active baseline, v1.9.3 cut commit 6990c54): `subagent_prompts/P0_writer_md_v1.9.3.md` (3 F-rules + 30 hooks) + `P0_matcher_v1.9.3.md` (30 hooks) + `P0_reviewer_v1.9.3.md` (35 hooks) + `P0_writer_pdf_v1.9.3.md` (paired-sync)
> Parent round close ref: `multi_session/P2_B-03c_round_10_kickoff.md` + commit 8deb94c (round 10 close 10 batches 182 atoms 5 domains RELSPEC/RELSUB/SM/SR/SS ★ v1.9.3 1st production validation §F-1 backward compat + §F-2 ratio 0.591 in band lower edge + §F-3 estimate delta 14.6% within threshold + §2.6 FIGURE 1 trigger RELSPEC/ex byte-exact 788 bytes + 0 NEW lock 0 halt 0 post-hoc fix; mini-audit vercel:deployment-expert AUDIT 8th family-pivot 8/8 PASS; 3 v2.0 LOW INFO carries surfaced)
> 路由词: 用户 session 说 **"开始 work 的 06 的 Round 11"** → 主 session 经 grep verify + scope ack 流程 (Bojiang ack 2026-05-07 Option B "拆分: round 11 = SU/SUPPQUAL/SV/TD 4 domain 轻 round + round 12 TA solo") → 进本 kickoff dispatch
> Convention 继承: round 01-10 §2.1-2.11 全 carry-forward + v1.9.3 §F-1/F-2/F-3 sustained; **round 11 NO NEW first-time lock 预期** (8 文件 grep 实证: 0 H4 / 3 mermaid TD/ex / 0 numberless H2 with H3 children → 0 §2.11 Plan B trigger; 7 numbered H2 §2.5 + 2 numberless childless H2 SUPPQUAL/ass §2.7 + 3 FIGURE §2.6); **TA solo deferred to round 12** (TA/ex 710L 8 H2 4 H3 20 mermaid §F-1 5th case — 隔离 stress-test 给独立 retro)

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1 CRITICAL + v1.9.2 §E-1 paired-sync + v1.9.3 §F-2 ratio band)

逐项 grep-verified against source byte-exact (执行日 2026-05-07 post round 10 CLOSE). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令. 缺 §0.5 = orchestrator preflight FAIL.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | post B-03c round 10 CLOSE 时 md_atoms.jsonl 末原子 = round 10 batch_113 final (SS/ex; parent_section root = `§SS [SS — Examples]`) | `tail -1 md_atoms.jsonl \| python3 -c "import sys,json; a=json.loads(sys.stdin.read()); print(a['atom_id'], a.get('parent_section'), a.get('file'))"` | ✓ md_atoms.jsonl 末原子 in SS/ex |
| 2 | md_atoms.jsonl 当前总原子 = **9294** (post round 10 CLOSED) | `wc -l md_atoms.jsonl` | ✓ 9294 |
| 3 | round 10 实际产 atoms = **182** (9294 − 9112 round 10 起始基线) | progress.json `cumulative_post_round_10.md_atoms_jsonl_total` 9294 − round 09 close 9112 | ✓ 182 |
| 4 | round 10 atoms/line ratio = 182/308 = **0.591** (band 0.59-0.85 内 lower edge; v1.9.3 §F-2 INFO 9-round sustained band) | round 10 §0.5 source 308 + actual 182 atoms | ✓ 0.591 |
| 5 | 累计 distinct domains atomized in md_atoms.jsonl = **49** (canonical post round 10; round 09 close 44 + RELSPEC/RELSUB/SM/SR/SS = 49) | `python3 -c "import json; d=set(); [d.add(json.loads(l)['atom_id'][5:].split('_')[0]) for l in open('md_atoms.jsonl') if json.loads(l)['atom_id'].startswith('md_dm')]; print(len(d), sorted(d))"` | ✓ 49 (AE..SS) |
| 6 | 累计 distinct files atomized in md_atoms.jsonl = **113** (post round 10; round 09 103 + RELSPEC/RELSUB/SM/SR/SS × 2 = 113) | `python3 -c "import json; f=set(); [f.add(json.loads(l)['file']) for l in open('md_atoms.jsonl')]; print(len(f))"` | ✓ 113 |
| 7 | domains/ 余 = **14 domains** (63 total − 49 done = 14; post round 11 = 14 − 4 = 10) | 63 − 49 = 14 | ✓ 14 (SU/SUPPQUAL/SV/TA/TD/TE/TI/TM/TR/TS/TU/TV/UR/VS) |
| 8 | Round 11 scope = **SU/SUPPQUAL/SV/TD 4 domains alphabetical** × 2 files = **8 source files** (TA solo deferred to round 12 per Bojiang ack Option B 2026-05-07; alphabetical SU<SUPPQUAL<SV<TA(deferred)<TD) | `ls knowledge_base/domains/{SU,SUPPQUAL,SV,TD}/{assumptions,examples}.md` = 8 文件 | ✓ 8 source files |
| 9 | Round 11 source lines total = **434** (SU/ass 20 + SU/ex 43 + SUPPQUAL/ass 26 + SUPPQUAL/ex 29 + SV/ass 43 + SV/ex 95 + TD/ass 13 + TD/ex 165) | `wc -l knowledge_base/domains/{SU,SUPPQUAL,SV,TD}/{assumptions,examples}.md` | ✓ 434 |
| 10 | Round 11 size buckets: <50L=**6** (TD/ass 13 + SU/ass 20 + SUPPQUAL/ass 26 + SUPPQUAL/ex 29 + SU/ex 43 + SV/ass 43), 50-99L=**1** (SV/ex 95), 100-199L=**1** (TD/ex 165), 200+slice=**0** | 文件大小逐项核 | ✓ 6/1/1/0 总 8 |
| 11 | Round 11 切片 = **0** (8 文件全 <300L threshold; TD/ex 165L 单 batch; round 09+10 同 0 slice 模式 sustained 第 3 round) | 全文件 <300L threshold | ✓ 0 slice (all single batch) |
| 12 | SU/ass.md H2 count = **0** (file-root only; H1 + body atoms) | `grep -nE "^## " knowledge_base/domains/SU/assumptions.md` | ✓ 0 H2 |
| 13 | SU/ex.md H2 count = **1** (L3 numbered `## Example 1`) → §2.5 self-namespace `§SU.1 [Example 1]` | `grep -nE "^## " knowledge_base/domains/SU/examples.md` | ✓ 1 H2 (numbered) |
| 14 | SUPPQUAL/ass.md H2 count = **2** (L15 numberless `## Submitting Supplemental Qualifiers in Separate Datasets` + L19 numberless `## When Not to Use Supplemental Qualifiers`) → §2.7 round 04 lock 2 cases (childless verified: 0 H3 children both H2) | `grep -nE "^## \|^### " knowledge_base/domains/SUPPQUAL/assumptions.md` | ✓ 2 H2 numberless childless (§2.7 ×2) |
| 15 | SUPPQUAL/ex.md H2 count = **2** (L5 numbered `## Example 1` + L16 numbered `## Example 2`) → §2.5 self-namespace × 2 (`§SUPPQUAL.1 / §SUPPQUAL.2 [Example N]`) | `grep -nE "^## " knowledge_base/domains/SUPPQUAL/examples.md` | ✓ 2 H2 (全 numbered) |
| 16 | SV/ass.md H2 count = **0** (file-root only) | `grep -nE "^## " knowledge_base/domains/SV/assumptions.md` | ✓ 0 H2 |
| 17 | SV/ex.md H2 count = **1** (L3 numbered `## Example 1`) → §2.5 self-namespace `§SV.1 [Example 1]` | `grep -nE "^## " knowledge_base/domains/SV/examples.md` | ✓ 1 H2 (numbered) |
| 18 | TD/ass.md H2 count = **0** (file-root only; 13 lines minimal) | `grep -nE "^## " knowledge_base/domains/TD/assumptions.md` | ✓ 0 H2 |
| 19 | TD/ex.md H2 count = **3** (L3 + L54 + L103 全 numbered `## Example N`) → §2.5 self-namespace × 3; **+ 3 mermaid blocks § §2.6 FIGURE-in-domains lock applies × 3** (L7 + L58 + L107) | `grep -nE "^## " knowledge_base/domains/TD/examples.md` + `grep -c '\`\`\`mermaid' TD/examples.md` | ✓ 3 H2 (全 numbered) + 3 mermaid → 3 FIGURE atoms expected |
| 20 | Round 11 累计 H2 = **9** (0+1+2+2+0+1+0+3 = 9; **7 numbered §2.5 + 2 numberless childless §2.7**) | per-file 上述行 | ✓ 9 H2 (7 numbered + 2 numberless childless) |
| 21 | Round 11 累计 H3 = **0** (8 文件全 0 H3) + H4 = **0** + mermaid = **3** (TD/ex 3 blocks at L7+L58+L107) | 全 8 文件 grep | ✓ 0 H3 / 0 H4 / 3 mermaid |
| 22 | Batch 序号续 = **batch_114..121** (round 10 末 batch_113 = SS/ex; round 11 共 8 batches: 4 domains × 2 files) | round 10 §0.5 row 24 + round 10 close batch_113 final | ✓ batch_114..121 (8 batches) |
| 23 | Round 11 估 atoms = **256-369** (434L × 0.59 lower = 256; 434L × 0.73 mid = 317; 434L × 0.85 upper = 369; v1.9.3 §F-2 9-round sustained band 0.59-0.85; **caveat**: round 11 含 4 ass.md = 102L 低密度 + 3 FIGURE 压缩, 实际 likely 偏 lower-edge similar to round 10 0.591) | 434 × {0.59, 0.73, 0.85} | ✓ 256-317-369 (mid ~317; expected lower-edge ~256-280) |
| 24 | post Round 11 累计 md_atoms.jsonl ≈ **9,550-9,663 atoms** (mid ~9,611) | 9294 + 256-369 | ✓ ~9,550-9,663 |
| 25 | post Round 11 累计 file coverage = **121/141 = 85.82%** ★ 跨 85% file 里程碑 | 113 + 8 = 121; 121/141 = 0.8582 | ✓ 85.82% (was 80.14% post round 10) |
| 26 | post Round 11 累计 distinct domain coverage = **53/63 = 84.13%** ★ 跨 80% domain 里程碑 | 49 + 4 = 53; 53/63 = 0.8413 | ✓ 84.13% (was 77.78% post round 10) |
| 27 | post Round 11 B-03c progress = **100/114 = 87.72%** ★ B-03c 跨 100 文件 + 跨 85% 双重里程碑 | 92 + 8 = 100; 100/114 = 0.8772 | ✓ 87.72% (was 80.70% post round 10) |
| 28 | v1.9.3 active baseline (commit 6990c54) **2nd production validation round** post round 10 1st production; gold reference atom = `md_dmRELSPEC_assn_a001` (round 10 batch_104 first atom; v1.9.3 §F-2/F-3 2nd sustained) | v1.9.3 active files: P0_writer_md_v1.9.3.md / P0_matcher_v1.9.3.md / P0_reviewer_v1.9.3.md / P0_writer_pdf_v1.9.3.md | ✓ v1.9.3 active (2nd production round) |
| 29 | TA solo deferred reason = TA/ex 710L 8 H2 (7 numbered + 1 numberless `## Trial Arms Issues` L694 with 4 H3 children) + 4 H3 + 20 mermaid blocks → §F-1 §2.11 Plan B 5th production case + §2.6 mass FIGURE stress-test → **隔离到 round 12 给独立 retro 价值** (Bojiang ack Option B 2026-05-07) | `wc -l + grep -nE "^#{1,4} \|^\`\`\`mermaid" knowledge_base/domains/TA/examples.md` | ✓ TA/ex 710L 8 H2 4 H3 20 mermaid → round 12 deferred |
| 30 | Round 11 vs Round 10 体量对照: round 10 = 308L 182 atoms 10 batches 5 domains; round 11 = 434L ~317 atoms 8 batches 4 domains. **体量 = round 10 1.41× by lines / 1.74× by atoms (mid) / 0.80× by batch count**. Round 11 单 batch 平均 atoms 偏高 (54 vs round 10 18.2) due to TD/ex 165L 单 batch (~80-120 atoms) | 434 vs 308 + 8 vs 10 batch + atoms est | ✓ 1.41× lines / 0.80× batch — TD/ex 单 batch 体量类似 SR/ex 116L round 10 batch_111 (70-100 atoms est) |

**Drift 校正记录**:
- Round 10 close 时 progress.json `cumulative_post_round_10.domains_atomized` = 49 sustained canonical; round 11 entry baseline = 49.
- Round 11 启动时 update progress.json `current_phase` → `P2_B-03c_round_11_in_flight_acked_2026-05-07_alphabetical_SU_SUPPQUAL_SV_TD_8_batches_batch_114_to_121_v1.9.3_2nd_production_validation_TA_solo_deferred_to_round_12_option_B`.
- Round 10 atoms/line ratio 0.591 lower edge (round 04 0.644 → round 05 0.761 → round 06 0.681 → round 07 0.782 → round 08 0.602 → round 09 0.646 → round 10 0.591); v1.9.3 §F-2 INFO 9-round sustained band 0.59-0.85. **Round 11 含 4 ass.md (102L) + 3 FIGURE 压缩 → 预期 ratio 落在 lower edge 0.59-0.65** similar to round 10.
- Round 11 体量 vs round 10: round 10 308L 182 atoms 10 batches; round 11 434L ~317 atoms 8 batches. **体量 = round 10 1.41× by lines / 1.74× by atoms (mid) / 0.80× by batch count**. 单 session 完成可行性: 8 single batches ≤ round 10 dispatch 数, 0 slice 干净, **TD/ex 165L 单 batch 估 ~80-120 atoms 是 round 11 最大 batch** — 类似 round 10 batch_111 SR/ex 116L 70-100 atoms 模型.
- post round 11 remaining = 14 − 4 = 10 domains × 2 = 20 files (TA + TE/TI/TM/TR/TS/TU/TV/UR/VS = 10; **round 12 = TA solo + 1-2 small domain glue**, **round 13 = 剩余 8-9 domains 收官**; 估 round 12 + 13 关闭 P2 B-03c).

---

## 1. Round 11 Scope (alphabetical SU/SUPPQUAL/SV/TD × 2 files = 8 single-batch; no slicing; TA solo to round 12)

| # | Batch | Target | Lines | 估 atoms | Bucket | atom_id prefix | parent_section root | NEW lock applies |
|---|---|---|---|---|---|---|---|---|
| 1 | **batch_114** | `domains/SU/assumptions.md` | 20 | ~7-12 | <50 | `md_dmSU_assn_a` (起 a001) | `§SU [SU — Assumptions]` | NO (0 H2) |
| 2 | **batch_115** | `domains/SU/examples.md` | 43 | ~22-30 | <50 | `md_dmSU_ex_a` (起 a001) | `§SU [SU — Examples]` | NO (1 numbered H2 §2.5) |
| 3 | **batch_116** | `domains/SUPPQUAL/assumptions.md` | 26 | ~10-14 | <50 | `md_dmSUPPQUAL_assn_a` (起 a001) | `§SUPPQUAL [SUPPQUAL — Assumptions]` | **§2.7 round 04 lock 2 cases** (L15 + L19 numberless H2 childless → file-root parent inherit) |
| 4 | **batch_117** | `domains/SUPPQUAL/examples.md` | 29 | ~10-15 | <50 | `md_dmSUPPQUAL_ex_a` (起 a001) | `§SUPPQUAL [SUPPQUAL — Examples]` | NO (2 numbered H2 §2.5) |
| 5 | **batch_118** | `domains/SV/assumptions.md` | 43 | ~17-22 | <50 | `md_dmSV_assn_a` (起 a001) | `§SV [SV — Assumptions]` | NO (0 H2) |
| 6 | **batch_119** | `domains/SV/examples.md` | 95 | ~30-50 | 50-99 | `md_dmSV_ex_a` (起 a001) | `§SV [SV — Examples]` | NO (1 numbered H2 §2.5; 35 table_rows) |
| 7 | **batch_120** | `domains/TD/assumptions.md` | 13 | ~3-6 | <50 | `md_dmTD_assn_a` (起 a001) | `§TD [TD — Assumptions]` | NO (0 H2; smallest ass.md in round 11) |
| 8 | **batch_121** | `domains/TD/examples.md` | 165 | ~80-120 | 100-199 | `md_dmTD_ex_a` (起 a001) | `§TD [TD — Examples]` | **§2.6 FIGURE-in-domains lock × 3** (L7+L58+L107 mermaid blocks → 3 FIGURE atoms expected) + §2.5 ×3 numbered H2 (largest single batch in round 11) |
| **总** | 8 batches | 8 files (0 sliced) | **434** | **~256-369** (mid ~317) | — | — | — | **0 NEW lock; §2.5 ×7 + §2.6 ×3 + §2.7 ×2 + §2.11 ×0** |

post Round 11 累计 file coverage: 113 + 8 = 121/141 = **85.82%** ★ 跨 85% file 里程碑 (was 80.14% post round 10).
post Round 11 累计 md_atoms.jsonl: 9294 + ~256-369 = ~9,550-9,663 atoms (mid ~9,611).
post Round 11 累计 distinct domain coverage: 49 + 4 = **53/63 = 84.13%** ★ 跨 80% domain 里程碑 (was 77.78% post round 10).
post Round 11 B-03c progress: 92 + 8 = 100/114 = **87.72%** ★ B-03c 跨 100 文件 + 跨 85% 双重里程碑 (was 80.70% post round 10).

**Round 11 vs Round 10 对照**: round 10 = 308L 182 atoms 10 batches 5 domains RELSPEC/RELSUB/SM/SR/SS 0 NEW lock 0 §2.11 trigger 1 §2.6 FIGURE; round 11 = 434L ~317 atoms 8 batches 4 domains SU/SUPPQUAL/SV/TD 0 NEW lock **0 §2.11 trigger** + **§2.7 lock 2 cases (SUPPQUAL/ass)** + **§2.6 FIGURE 3 trigger (TD/ex 3 mermaid)**. 体量 = round 10 1.41× by lines / 1.74× by atoms / 0.80× by batch count. 关键差异: round 11 v1.9.3 2nd production validation; §F-2 ratio band 10th sustained validation expected (round 10 0.591 lower edge → round 11 likely similar lower-edge); **TA/ex 710L 7+1 H2 4 H3 20 mermaid §F-1 5th production case 隔离到 round 12** 给 stress-test 独立 retro.

**Round 11 vs Round 08 对照** (closest precedent: 0 §2.11 trigger + 0 NEW lock + small files mix): round 08 = 399L 240 atoms 10 batches 5 domains PE/PP/PR/QS/RE 0 NEW lock §2.7 lock 2 cases (PP/ex L106 + QS/ass L5); round 11 = 434L ~317 atoms 8 batches 4 domains 0 NEW lock §2.7 lock 2 cases (SUPPQUAL/ass L15 + L19) + §2.6 FIGURE 3 trigger. **体量 = round 08 1.09× by lines / 1.32× by atoms — round 08 接近原型 + §2.7 lock 2 cases 同等密度**.

**ctx pressure forecast**: round 11 = 8 + 8 + 1 = **17 dispatch calls** (< round 06/08/09/10's 21). 0 slice + 0 NEW lock + v1.9.3 §F-2 ratio sustained → halt 触发概率 **类似 round 10 干净 round**. ctx checkpoint 强制 at batch_119 (round 中点 SV/ex). 单批 TD/ex 估 ~80-120 atoms 上限 — 注意 writer ctx 中段.

---

## 2. Convention inherit (round 01-10 全 carry-forward + v1.9.3 §F-1/F-2/F-3 sustained)

### 2.1-2.11 全 inherit from round 01-10

(全 carry-forward, 不重复列出 — 详见 round 10 kickoff §2.1-2.11:)
- **§2.1** Heading level pattern (H1 file root / H2 examples self-namespace / H3 sub-namespace / H4+ TBD)
- **§2.2** atom_id prefix per file (4-digit 容许)
- **§2.3** atom_id 起始 a001 per file (NOT per batch; 不跨 file 续号)
- **§2.4** multi-batch single-file slice convention — **round 11 NO trigger** (8 文件全 <300L, 全 single batch)
- **§2.5** numbered H2 self-namespace — **round 11 applies 7 cases**: SU/ex L3 + SUPPQUAL/ex L5 + SUPPQUAL/ex L16 + SV/ex L3 + TD/ex L3 + TD/ex L54 + TD/ex L103 = **7 numbered H2 §2.5 cases**
- **§2.6** FIGURE-in-domains lock — **round 11 trigger 3 cases**: TD/ex L7 + L58 + L107 mermaid blocks → 3 FIGURE atoms expected (round 03 §2.6 lock sustained × N rounds; round 11 = round 10 1 FIGURE → round 11 3 FIGURE 渐增)
- **§2.7** Numberless H2 with childless = file-root parent (round 04 lock FT/ass) — **round 11 trigger 2 cases**: SUPPQUAL/ass L15 `## Submitting Supplemental Qualifiers in Separate Datasets` + L19 `## When Not to Use Supplemental Qualifiers` 全 numberless childless → file-root `§SUPPQUAL [SUPPQUAL — Assumptions]` parent inherit
- **§2.8 R-2.8-1/2/3** (now v1.9.2 §E-2/E-3/E-4 codified): H1 sib_idx=1 + TABLE_HEADER sib_idx=null + extracted_by object schema
- **§2.9** LIST_ITEM sib_idx universal = null (round 03 lock, sustained)
- **§2.10** LIST_ITEM hl+sib field-explicit-null (round 05 MED-01 → v1.9.2 §E-5 codified): explicit JSON `"heading_level": null, "sibling_index": null` NOT omitted
- **§2.11 Plan B sub-namespace by sib_idx for numberless H2 with H3 children** (round 07 NEW lock; round 09 4 cases stress-test PASS; v1.9.3 §F-1 SUSTAINED VALIDATED EXTENDED) — **round 11 NO trigger** (0 numberless H2 with H3 children; **TA/ex L694 numberless H2 + 4 H3 children 5th case deferred to round 12**); §F-1 2nd production validation will be **backward compat verification** (round 07 PC/ex + round 09 RELREC/RS sub-namespace atoms preserved byte-exact)

### 2.12-? **Round 11 0 NEW first-time lock 预期 (v1.9.3 2nd production validation round)**

Round 11 grep 实证 (§0.5 row 12-21):
- 0 H3 in 8 文件 → 0 §2.11 Plan B trigger (TA solo deferred to round 12 = 5th case stress-test 隔离)
- 0 H4 in 8 文件 → 无 H4 sub-policy 设计需求
- 3 mermaid in 8 文件 (TD/ex 全 3 块 L7+L58+L107) → §2.6 FIGURE 3 atoms 预期 (round 03 lock sustained; round 10 1 FIGURE → round 11 3 FIGURE 量级提升; B-03c 单 round FIGURE 数 NEW peak)
- 2 numberless H2 (SUPPQUAL/ass L15 + L19) 全 childless → §2.7 round 04 lock 2 cases sustained (round 04 FT/ass 1 + round 08 PP/ex L106 + QS/ass L5 = 3 cumulative + round 11 2 = 5 cumulative)
- 7 numbered H2 全 §2.5 self-namespace 沿用

**Surprise H3 occurrence handling** (per §4 halt #6): 若 dispatch 后 writer 实测发现 H3 (虽 grep 实证 0) → halt + 请求 lock 扩展 (§F-1 §2.11 Plan B 6th case unexpected emergence).

**v1.9.3 F-rules 2nd production validation focus**:
- **§F-1 §2.11 Plan B**: round 11 0 trigger → 2nd backward compat verification (round 07 PC/ex + round 09 RELREC/RS sub-namespace atoms 应 unchanged; round 11 不会触发新 §2.11 case; TA round 12 才是 5th 新 case)
- **§F-2 ratio band 0.59-0.85**: round 11 10th sustained validation cycle (round 04-10 7 rounds + v1.9.2 cut + v1.9.3 cut + round 10 1st = 10 cumulative validations expected post round 11)
- **§F-3 INFO kickoff atom estimate calibration**: round 11 用 §F-2 mid 0.73 → 434 × 0.73 = 317 atoms 估算 (range 256-369; lower edge bias expected due 4 ass.md 102L compression + 3 FIGURE compression)

---

## 3. v1.9.3 prompt 入口条件 (active baseline 2nd production validation round)

### Writer pool (per v1.9.1 §D-8 peer-alternative + v1.9.2 §E-1 explicit JSON template mandate + v1.9.3 §F-1 sustained)
- `oh-my-claudecode:executor` (OMC primary, opus when available; **typically NOT available in default CC session — fallback expected**)
- `general-purpose` (FALLBACK peer-alternative; B-02 + round 01-10 sustained 140 batches 7998 atoms 0 writer defect post-fix cumulative; round 06 batch_72 1 schema regression 已 root-revert + re-dispatch RESOLVED, sustained quality streak intact post v1.9.2 §E-1 + v1.9.3 §F-1 codification)

### Reviewer pool (per v1.9.1 §D-8 + v1.9.2 §R-E1 schema regression sweep PRIORITY 1)
- `pr-review-toolkit:code-reviewer` (FALLBACK peer-alternative; B-02 + round 01-10 sustained 100% PASS post-fix; round 11 默认 per-batch reviewer × 8)
- **BURNED list (round 11 mini-audit 必避用)**:
  - `feature-dev:code-reviewer` (round 01 mini-audit + round 02 batch_23 burn)
  - `feature-dev:code-architect` (round 02 mini-audit burn)
  - `pr-review-toolkit:type-design-analyzer` (round 03 mini-audit burn)
  - `pr-review-toolkit:silent-failure-hunter` (round 04 mini-audit burn)
  - `pr-review-toolkit:comment-analyzer` (round 05 mini-audit burn)
  - `pr-review-toolkit:pr-test-analyzer` (round 06 mini-audit burn)
  - `pr-review-toolkit:code-simplifier` (round 07 mini-audit burn — 5/5 pr-review-toolkit AUDIT pool 已耗尽)
  - `Plan` AUDIT mode (round 08 mini-audit burn — 1st planner-family AUDIT-pivot)
  - `feature-dev:code-explorer` AUDIT mode (round 09 mini-audit burn — 7th cumulative B-03c reviewer family-pivot, 3rd feature-dev sub-type)
  - `vercel:ai-architect` AUDIT (v1.9.3 cut audit slot #71 burn — 1st vercel-family AUDIT pivot)
  - `vercel:deployment-expert` AUDIT (round 10 mini-audit burn — 2nd vercel-family AUDIT pivot, 8th cumulative B-03c reviewer family-pivot)
  - `pr-review-toolkit:code-reviewer` (round 04+05+06+07+08+09+10 per-batch ~78 burn — round 11 也将作 per-batch reviewer × 8 仍 burn for mini-audit slot)
  - `general-purpose` (writer pool sustained burn)
- **Fresh candidates (round 11 mini-audit, 9th cumulative B-03c family-pivot target)**:
  - **`claude-code-guide` AUDIT mode** ★ 1st choice — Anthropic-domain reviewer family NEW pivot; **cross-family Rule D distance maximum** vs all burned slots (vercel/feature-dev/pr-review-toolkit/Plan/general-purpose); **9th cumulative B-03c reviewer family-pivot ★ Anthropic-domain family AUDIT pool inaugural sub-type**
  - `vercel:performance-optimizer` AUDIT mode (vercel-family 3rd sub-type intra-family depth 3, fallback if claude-code-guide 不可用 — 但 cross-family distance 较 weak vs 已用 vercel:ai-architect + vercel:deployment-expert)
  - `plugin-dev:plugin-validator` AUDIT mode (plugin-dev family inaugural reviewer pivot, 2nd fallback)
  - `plugin-dev:skill-reviewer` AUDIT mode (plugin-dev family inaugural reviewer pivot, 3rd fallback)
- **首选 (round 11 mini-audit)**: **`claude-code-guide` AUDIT mode** (reviewer-only role; 跨 family Rule D 距离 最大化 — Anthropic-domain reviewer pool 1st sub-type post 8 burns vercel/feature-dev/pr-review-toolkit/Plan/general-purpose 累计)
- **次选**: 若 claude-code-guide 不可用 (无 AUDIT mode), 备选 `vercel:performance-optimizer` AUDIT (vercel-family 3rd sub-type) 或 `plugin-dev:plugin-validator` AUDIT (plugin-dev family inaugural)

### N21 ban list (sustained per v1.7 cut + v1.9.2 §E-1 paired-sync + v1.9.3 §F-1 carry-forward)
`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer` (writer role; reviewer role per round 09 fresh candidates already burn), `oh-my-claudecode:document-specialist`

### Rule D 硬约束
writer ≠ reviewer (不同 subagent_type, NOT 仅不同 instance).

### v1.9.3 active hooks (sustained from v1.9.2 + 3 F-rules 2nd production)
- **§F-1 HIGH Hook** (sustained): §2.11 Plan B sub-namespace by sib_idx for numberless H2 with H3 children (round 07 1st + round 09 4 cases + round 10 backward compat = 5 production cases; round 11 0 trigger → 2nd backward compat; TA round 12 = 5th case primary trigger)
- **§F-2 INFO Hook** (sustained): atoms/line ratio empirical band 0.59-0.85 — round 11 10th sustained validation expected (round 04-10 7 rounds + v1.9.2 cut + v1.9.3 cut + round 10 1st production + round 11 2nd production = 10 cumulative)
- **§F-3 INFO Hook** (sustained): kickoff atom estimate calibration for multi-level nested-list domains (round 08 INFO-R08-01 codified; round 11 §0.5 row 23 用 §F-2 mid 0.73)
- **§E-1 CRITICAL Hook 22c** (sustained): dispatch prompt MUST include explicit JSON template with all 12 field names + reference working batch_104 a001 = `md_dmRELSPEC_assn_a001` as gold reference (cumulative empirical baseline 9294 atoms 0 schema regression post round 10)
- **§E-2 HIGH Hook E-2-1** (sustained): H1 sib_idx=1 universal (R-2.8-1 codified)
- **§E-3 HIGH Hook E-3-2** (sustained): TABLE_HEADER sib_idx=null universal (R-2.8-2 codified)
- **§E-4 HIGH Hook E-4-3** (sustained): extracted_by object schema (R-2.8-3 codified)
- **§E-5 MED Hook E-5** (sustained): non-HEADING atoms field-explicit-null (round 05 MED-01 codified; LIST_ITEM hl+sib explicit JSON form NOT omitted)
- **§E-6 LOW Hook** (sustained): FIGURE-vs-CODE_LITERAL boundary clarification — **round 11 2nd post-v1.9.3 FIGURE production validation** (TD/ex 3 mermaid blocks; round 10 1 FIGURE RELSPEC/ex → round 11 3 FIGURE TD/ex 量级提升)
- **Hook 22b (D-1 CRITICAL sustained)**: kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims ✓ (本 kickoff §0.5 30/30 PASS)
- **Hook D-NOTE-BQ (D-2 HIGH sustained)**: blockquote-prefix `> **Note:**` / `> **Exception:**` = atom_type NOTE
- **Hook D-D8 (D-4 sustained)**: numberless `## Overview` H2 chapter root inherit children — **round 11 NO trigger** (2 numberless H2 全 childless §2.7)
- **Round 03 §2.4 (multi-batch slice)**: round 11 NO trigger (全 <300L)
- **Round 03 §2.6 (FIGURE-in-domains)**: round 11 3 trigger (TD/ex 3 mermaid → 3 FIGURE atoms expected)
- **Round 03 LIST_ITEM sib_idx null**: 全 round 11 enforce
- **Round 04 §2.7 (numberless H2 in ass.md / childless ex.md)**: round 11 2 trigger (SUPPQUAL/ass L15 + L19 numberless childless)
- **Round 04 §2.8 R-2.8-1/2/3 (now v1.9.2 §E-2/E-3/E-4)**: 全 round 11 dispatch prompt 显式注入
- **Round 05 §2.10 MED-01 (now v1.9.2 §E-5)**: 全 round 11 dispatch prompt 显式 JSON form
- **Round 07 §2.11 (Plan B sub-namespace by sib_idx)** (now v1.9.3 §F-1): round 11 NO trigger; backward compat verification only

### Round 10 v2.0 LOW INFO carries (monitor in round 11, NOT block)
- **C-R10-01** §F-2 FIGURE-bearing band supplement — round 11 TD/ex 3 FIGURE 是相关 batch, 监测 batch_121 ratio 是否 lower-edge driven by FIGURE compression (round 10 batch_105 RELSPEC/ex 单 FIGURE batch ratio 48% near halt threshold)
- **C-R10-02** §F-3 FIGURE-aware estimate adjustment — round 11 batch_121 TD/ex est 80-120 atoms 用 §F-2 mid 0.73 + §2.6 3 FIGURE compression (估算 ~85-120 范围)
- **C-R10-03** §2.6 FIGURE sub-classification (mermaid/ASCII/PNG-ref) — round 11 TD/ex 全 mermaid 3 blocks (无 sub-classification 触发, monitoring only)

---

## 4. 自治连跑 halt 条件 (per umbrella §10.2 + round 11 specific)

任一触发 → 暂停 + ping 用户, 不强行进下一步:

1. **任一 batch §0.5 grep checksum 任一项 FAIL** (numeric drift detected at kickoff write time — 本 kickoff 已 30/30 PASS)
2. **任一 batch Rule A audit < 90% PASS rate** 或现 HIGH severity finding
3. **Schema violation / atom_id collision / 9 atom_type 任一异常** (含 v1.9.2 §R-E1 PRIORITY 1 schema regression sweep — round 06 batch_72 4-schema-regression precedent + round 07-10 cumulative 0 schema regression validated; round 11 v1.9.3 2nd production 关注 §F-1 backward compat regression + §2.7 lock 2 cases re-validation)
4. **Source markdown anomaly** 需 Rule B preserve + 业务 judgment call
5. **v1.9.3 prompt 路径 drift** — writer pool 任一不可用 OR reviewer pool 任一不可用 + FALLBACK 也不可
6. **Convention lock 首次扩展** — round 11 计划 0 NEW lock; 若遇到 H3 surprise (虽 grep 实证 0) / 额外 mermaid in non-TD/ex (虽 grep 实证 0 in 其余 7 文件) / 额外 H4 outside grep 实证 0 → 暂停 + 请求 lock 扩展
7. **ctx 紧张 (剩 < 30%)** 或 session 累计已 > 1.5 hr 仍未到 round 闭环 — 主动写 handoff.md + resume prompt 给用户. **Round 11 ctx pressure 警戒线**: 17 dispatch calls — batch_119 (round 6/8 中点 = SV/ex) 后强制 ctx checkpoint
8. **Round-specific**: 任一 batch atom 数实际 outside 估算 [0.5×low, 1.5×high] → 暂停核 source / prompt drift. Round 11 各 batch 估算与下限/上限:

| Batch | est range | halt low (0.5×low) | halt high (1.5×high) |
|---|---|---|---|
| 114 SU/ass | 7-12 | <4 | >18 |
| 115 SU/ex | 22-30 | <11 | >45 |
| 116 SUPPQUAL/ass | 10-14 | <5 | >21 |
| 117 SUPPQUAL/ex | 10-15 | <5 | >23 |
| 118 SV/ass | 17-22 | <9 | >33 |
| 119 SV/ex | 30-50 | <15 | >75 |
| 120 TD/ass | 3-6 | <2 | >9 |
| 121 TD/ex | 80-120 | <40 | >180 |

---

## 5. Dispatch order (sequential, single-session)

| Step | Action | Subagent | Prompt source |
|---|---|---|---|
| 1 | batch_114 SU/ass writer | `general-purpose` | `subagent_prompts/P0_writer_md_v1.9.3.md` + per-batch prompt |
| 2 | batch_114 reviewer | `pr-review-toolkit:code-reviewer` | `subagent_prompts/P0_reviewer_v1.9.3.md` |
| 3 | batch_115 SU/ex writer | `general-purpose` | (同上) |
| 4 | batch_115 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 5 | batch_116 SUPPQUAL/ass writer (§2.7 ×2) | `general-purpose` | (同上) |
| 6 | batch_116 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 7 | batch_117 SUPPQUAL/ex writer | `general-purpose` | (同上) |
| 8 | batch_117 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 9 | batch_118 SV/ass writer | `general-purpose` | (同上) |
| 10 | batch_118 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| **CTX CHECKPOINT** | **batch_118 close 后强制 ctx 余量评估** | — | (per §4.7) |
| 11 | batch_119 SV/ex writer | `general-purpose` | (同上) |
| 12 | batch_119 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 13 | batch_120 TD/ass writer (smallest 13L) | `general-purpose` | (同上) |
| 14 | batch_120 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 15 | batch_121 TD/ex writer (largest 165L; §2.6 ×3 FIGURE) | `general-purpose` | (同上) |
| 16 | batch_121 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 17 | **mini-audit Rule A** (random 8 atoms across batch_114-121, ≥1 from FIGURE batch_121 + ≥1 from §2.7 batch_116) | **`claude-code-guide` AUDIT mode** ★ NEW Anthropic-domain family inaugural pivot (9th cumulative B-03c reviewer family-pivot) | `evidence/checkpoints/mini_audit_P2_B-03c_round_11_*` |

---

## 6. Round 11 close criteria (per umbrella §10.3)

- [ ] 8 batches 全部 atomized 写入 `md_atoms.jsonl`
- [ ] 8 per-batch reviewer 全 PASS (Rule A audit ≥ 90% rate, 0 HIGH severity)
- [ ] mini-audit 8/8 PASS (`claude-code-guide` AUDIT mode random sample)
- [ ] 10/10 invariants per round 10 sustained pattern (atom_id uniqueness / 9 atom_type / parent_section format / extracted_by schema / sib_idx rules / etc.)
- [ ] 0 schema regression vs v1.9.3 baseline (§F-1 2nd backward compat verification)
- [ ] §F-2 ratio band 0.59-0.85 10th sustained validation (434L × actual ratio = lower-edge expected ~256-280)
- [ ] 0 NEW first-time lock (per grep 实证 forecast)
- [ ] §2.7 lock 2 cases sustained (SUPPQUAL/ass L15 + L19 numberless childless H2 → file-root parent verified)
- [ ] §2.6 FIGURE-in-domains 3 trigger PASS (TD/ex 3 mermaid → 3 FIGURE atoms, byte-exact verbatim incl. opening/closing fences)
- [ ] progress.json `cumulative_post_round_11` written (md_atoms_jsonl_total / domains_atomized 53 / file_coverage 121 / B-03c progress 100/114)
- [ ] sibling_continuity_sweep_report_round11.md written
- [ ] commit message format: "06 P2 B-03c round 11 自治连跑 CLOSED — 8 batches N atoms 4 domains SU/SUPPQUAL/SV/TD ★ 跨 85% file coverage + 跨 80% domain coverage milestones — v1.9.3 2nd production validation §F-1 2nd backward compat + §F-2 ratio band 10th sustained + §2.6 FIGURE 3 trigger TD/ex + §2.7 lock 2 cases SUPPQUAL/ass + TA solo deferred to round 12 option B"

---

**Bojiang ack 2026-05-07 captured (Option B)**: "拆分: round 11 = SU/SUPPQUAL/SV/TD 4 domain 408L 轻 round, round 12 = TA solo (TA/ex 710L 切片 + 衔接) + TE/TI 等 — 干净分层"
**Decision**: SU + SUPPQUAL + SV + TD (alphabetical 4 domains, TA deferred) = 4 domains × 2 = 8 files = 434L (实测, 408L 是 ack 时口语估算)
**Round 12 preview**: TA solo + 1-2 small TE/TI/TM glue (TA/ass 29L + TA/ex 710L 3-slice + TE/ass 37L + TE/ex 77L + TI/ass 15L + TI/ex 20L = ~888L 4 domains 11-12 batches). §F-1 §2.11 Plan B 5th production case + §2.6 mass FIGURE 20-block stress-test 集中在 round 12 给独立 retro 价值.
**Next**: dispatch batch_114 immediately per §5 sequential order.
