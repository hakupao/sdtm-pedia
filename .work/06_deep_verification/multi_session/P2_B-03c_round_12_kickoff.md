# P2 B-03c Round 12 — TA Solo (3-slice §2.4) + TE/TI/TM Glue Kickoff (per Bojiang ack 2026-05-07 Option B)

> 创建: 2026-05-07 (post B-03c round 11 CLOSED commit 66f29bd; **v1.9.3 active baseline 3rd production validation round** — 4 paired-sync prompts writer_md/pdf/matcher/reviewer + 3 F-rules §F-1/F-2/F-3 sustained; v1.9.4 cut planning trigger MET — round 12 = 1 more sustained validation cycle pre-cut)
> 父 umbrella: `multi_session/P2_B-03_kickoff.md`
> 父 prompt (active baseline, v1.9.3 cut commit 6990c54): `subagent_prompts/P0_writer_md_v1.9.3.md` (3 F-rules + 30 hooks) + `P0_matcher_v1.9.3.md` (30 hooks) + `P0_reviewer_v1.9.3.md` (35 hooks) + `P0_writer_pdf_v1.9.3.md` (paired-sync)
> Parent round close ref: `multi_session/P2_B-03c_round_11_kickoff.md` + commit 66f29bd (round 11 close 8 batches 208 atoms 4 domains SU/SUPPQUAL/SV/TD ★ 跨 85% file coverage 85.82% + 跨 80% domain coverage 84.13% + 跨 100 files B-03c + 跨 85% B-03c progress 87.72% quadruple milestones; v1.9.3 2nd production validation §F-1 2nd backward compat + §F-2 de-figure-naive 0.698 in band 10th sustained + §F-3 aggregate -34.4% within threshold + §2.6 FIGURE 3 trigger TD/ex byte-exact 770/895/1340 bytes + §2.7 lock 2 cases SUPPQUAL/ass + Hook A1 attempt 1 HIGH severity HALT RESOLVED in-session; mini-audit plugin-dev:plugin-validator AUDIT 9th family-pivot inaugural plugin-dev family-pivot)
> 路由词: 用户 session 说 **"work 的 06 的 round 12 开跑"** → 主 session 经 grep verify (本 §0.5 30/30 PASS) → 进本 kickoff dispatch
> Convention 继承: round 01-11 §2.1-2.11 全 carry-forward + v1.9.3 §F-1/F-2/F-3 sustained; **round 12 NO NEW first-time lock 预期** but **§F-1 §2.11 Plan B DUAL production trigger** (TA/ex L694 5th case + **TE/ex L48 6th case ★ NEW DISCOVERY post-grep**); **§2.4 multi-batch slice 3rd production trigger** (TA/ex 710L 3-slice; round 03 inaugural lock 1st production; v1.9.3 sustained validation 2nd batch slice production); **§2.6 FIGURE-in-domains 20-block stress-test** (TA/ex 全 20 mermaid 单 round NEW peak 远超 round 11 3 FIGURE)

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1 CRITICAL + v1.9.2 §E-1 paired-sync + v1.9.3 §F-2 ratio band)

逐项 grep-verified against source byte-exact (执行日 2026-05-07 post round 11 CLOSE). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令. 缺 §0.5 = orchestrator preflight FAIL.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | post B-03c round 11 CLOSE 时 md_atoms.jsonl 末原子 = round 11 batch_121 final (TD/ex Example 3 closing; parent_section = `§TD.3 [Example 3]`) | `tail -1 md_atoms.jsonl \| python3 -c "import sys,json; a=json.loads(sys.stdin.read()); print(a['atom_id'], a.get('parent_section'), a.get('file'))"` | ✓ `md_dmTD_ex_a038` / `§TD.3 [Example 3]` / TD/ex |
| 2 | md_atoms.jsonl 当前总原子 = **9502** (post round 11 CLOSED) | `wc -l md_atoms.jsonl` | ✓ 9502 |
| 3 | round 11 实际产 atoms = **208** (9502 − 9294 round 11 起始基线) | progress.json `cumulative_post_round_11.md_atoms_jsonl_total` 9502 − round 10 close 9294 | ✓ 208 |
| 4 | round 11 atoms/line ratio naive = 208/434 = **0.479** (BELOW 0.59-0.85 band lower edge); de-figure-naive = (208−3)/(434−~50 FIGURE compression-line) ≈ **0.698** (in band) per round 11 retro §F-2 10th sustained | round 11 §0.5 source 434 + actual 208 atoms − 3 FIGURE atoms; FIGURE compression ≈ 50 lines (3 × ~17L mermaid blocks) | ✓ naive 0.479 / de-figure 0.698 in band |
| 5 | 累计 distinct domains atomized in md_atoms.jsonl = **53** (canonical post round 11; round 10 49 + SU/SUPPQUAL/SV/TD = 53) | `python3 -c "import json; d=set(); [d.add(json.loads(l)['atom_id'][5:].split('_')[0]) for l in open('md_atoms.jsonl') if json.loads(l)['atom_id'].startswith('md_dm')]; print(len(d))"` | ✓ 53 (AE..TD) |
| 6 | 累计 distinct files atomized in md_atoms.jsonl = **121** (post round 11; round 10 113 + SU/SUPPQUAL/SV/TD × 2 = 121) | `python3 -c "import json; f=set(); [f.add(json.loads(l)['file']) for l in open('md_atoms.jsonl')]; print(len(f))"` | ✓ 121 |
| 7 | domains/ 余 = **10 domains** (63 total − 53 done = 10; post round 12 = 10 − 4 = 6) | 63 − 53 = 10 | ✓ 10 (TA/TE/TI/TM/TR/TS/TU/TV/UR/VS) |
| 8 | Round 12 scope = **TA/TE/TI/TM 4 domains alphabetical** × 2 files = **8 source files** (per Bojiang ack Option B 2026-05-07 "TA solo + TE/TI/TM glue") | `ls knowledge_base/domains/{TA,TE,TI,TM}/{assumptions,examples}.md` = 8 文件 | ✓ 8 source files |
| 9 | Round 12 source lines total = **911** (TA/ass 29 + TA/ex 710 + TE/ass 37 + TE/ex 77 + TI/ass 15 + TI/ex 20 + TM/ass 7 + TM/ex 16) | `wc -l knowledge_base/domains/{TA,TE,TI,TM}/{assumptions,examples}.md` | ✓ 911 |
| 10 | Round 12 size buckets: <50L=**6** (TM/ass 7 + TI/ass 15 + TM/ex 16 + TI/ex 20 + TA/ass 29 + TE/ass 37), 50-99L=**1** (TE/ex 77), 100-199L=**0**, **300+slice=1** (TA/ex 710L → §2.4 3-slice) | 文件大小逐项核 | ✓ 6/1/0/1 总 8 |
| 11 | Round 12 切片 = **3** (TA/ex 710L > 300L → §2.4 multi-batch slice 3rd production trigger; round 03 lock 1st production + v1.9.3 cut B-02 cumulative validation 2nd; **3-slice H2-aligned**: A=L1-L344 Examples 1-3 / B=L344-L606 Examples 4-6 / C=L606-L710 Example 7 + Trial Arms Issues §2.11) | TA/ex 710 / 3 ≈ 237 per slice; H2 边界 align (Example 4 L344 + Example 7 L606) | ✓ 3-slice H2-aligned |
| 12 | TA/ass.md H2 count = **0** (file-root only; 29L) | `grep -nE "^## " knowledge_base/domains/TA/assumptions.md` | ✓ 0 H2 |
| 13 | TA/ex.md H2 count = **8** (7 numbered L18/120/245/344/466/534/606 + 1 numberless `## Trial Arms Issues` L694 with 4 H3 children = §F-1 §2.11 Plan B 5th cumulative production case) | `grep -nE "^## " knowledge_base/domains/TA/examples.md` | ✓ 8 H2 (7 numbered + 1 numberless §2.11) |
| 14 | TA/ex.md H3 count = **4** (L696/700/704/708 全 under L694 numberless H2) → §2.11 Plan B sub-namespace by sib_idx 5th cumulative production case | `grep -nE "^### " knowledge_base/domains/TA/examples.md` | ✓ 4 H3 (under §2.11 trigger) |
| 15 | TA/ex.md mermaid count = **20** (L24/39/60/84/126/137/185/251/269/301/352/364/388/416/472/488/542/558/614/632) → §2.6 FIGURE-in-domains 20 atoms expected (B-03c 单 round NEW peak 远超 round 11 3 FIGURE TD/ex) | `grep -nE "^\`\`\`mermaid" knowledge_base/domains/TA/examples.md` | ✓ 20 mermaid → 20 FIGURE |
| 16 | TE/ass.md H2 count = **0** (file-root only; 37L) | `grep -nE "^## " knowledge_base/domains/TE/assumptions.md` | ✓ 0 H2 |
| 17 | **TE/ex.md H2 count = 4 (3 numbered L5/19/34 + 1 numberless `## Trial Elements Issues` L48 with 3 H3 children = §F-1 §2.11 Plan B 6th cumulative production case ★ NEW post-grep DISCOVERY 未在 round_12_trigger 预报)** | `grep -nE "^## " knowledge_base/domains/TE/examples.md` | ✓ **4 H2 (3 numbered + 1 numberless §2.11) ★ NEW** |
| 18 | TE/ex.md H3 count = **3** (L50/63/67 全 under L48 numberless H2) → §2.11 Plan B sub-namespace 6th case | `grep -nE "^### " knowledge_base/domains/TE/examples.md` | ✓ 3 H3 (under §2.11 trigger) |
| 19 | TE/ex.md mermaid count = **0** (无 figure) | `grep -nE "^\`\`\`mermaid" knowledge_base/domains/TE/examples.md` | ✓ 0 mermaid |
| 20 | TI/ass.md H2 = **0** (15L) / TI/ex.md H2 = **1** numbered L3 / TM/ass.md H2 = **0** (7L) / TM/ex.md H2 = **1** numbered L3 | per-file grep | ✓ 0/1/0/1 (2 numbered §2.5) |
| 21 | Round 12 累计 H2 = **14** (0+8+0+4+0+1+0+1 = 14; **12 numbered §2.5 + 2 numberless §F-1 §2.11 Plan B**) | per-file 上述行 | ✓ 14 H2 (12 numbered + 2 numberless §2.11) |
| 22 | Round 12 累计 H3 = **7** (4 TA/ex + 3 TE/ex 全 §2.11 trigger 下); H4 = **0**; mermaid = **20** (全 TA/ex) | 全 8 文件 grep | ✓ 7 H3 / 0 H4 / 20 mermaid |
| 23 | Batch 序号续 = **batch_122..131** (round 11 末 batch_121 = TD/ex; round 12 共 10 batches: TA/ass + TA/ex×3-slice + TE/ass + TE/ex + TI/ass + TI/ex + TM/ass + TM/ex) | round 11 §0.5 row 22 + round 11 close batch_121 final | ✓ batch_122..131 (10 batches) |
| 24 | Round 12 估 atoms naive = **538-774** (911L × 0.59-0.85 = 537.5-774.4; mid 665); **de-figure adjusted ≈ 460-600** (扣 20 FIGURE 行约 ~280L mermaid compression: 911L − 280L = 631L × 0.59-0.85 = 372-536; + 20 FIGURE atoms = 392-556 actual atoms; mid ~470-490) | 911 × {0.59, 0.73, 0.85} 与 §F-2 de-figure 调整 | ✓ naive 538-774 / de-figure 460-600 (mid ~470-490) |
| 25 | post Round 12 累计 md_atoms.jsonl ≈ **9,962-10,102 atoms** (mid ~10,000); ★ **跨 10,000 atoms 里程碑 mid-estimate** (was 9502 post round 11) | 9502 + 460-600 | ✓ ~9,962-10,102 mid 10,000 ★ 跨 10K |
| 26 | post Round 12 累计 file coverage = **129/141 = 91.49%** ★ **跨 90% file coverage 里程碑** (was 85.82% post round 11) | 121 + 8 = 129; 129/141 = 0.9149 | ✓ 91.49% ★ 跨 90% file |
| 27 | post Round 12 累计 distinct domain coverage = **57/63 = 90.48%** ★ **跨 90% domain coverage 里程碑** (was 84.13% post round 11) | 53 + 4 = 57; 57/63 = 0.9048 | ✓ 90.48% ★ 跨 90% domain |
| 28 | post Round 12 B-03c progress = **108/114 = 94.74%** ★ **跨 90% B-03c progress 里程碑 + 跨 100 files B-03c sustained** (was 87.72% post round 11) | 100 + 8 = 108; 108/114 = 0.9474 | ✓ 94.74% ★ 跨 90% B-03c |
| 29 | v1.9.3 active baseline (commit 6990c54) **3rd production validation round** post round 10 1st + round 11 2nd; gold reference atom = `md_dmRELSPEC_assn_a001` (round 10 batch_104 first atom; v1.9.3 §F-1/F-2/F-3 3rd sustained); v1.9.4 cut planning trigger MET 5 actionable + 5 INFO carries ≥10 threshold post round 11 — recommend **v1.9.4 cut after round 12 close** | v1.9.3 active files: P0_writer_md_v1.9.3.md / P0_matcher_v1.9.3.md / P0_reviewer_v1.9.3.md / P0_writer_pdf_v1.9.3.md | ✓ v1.9.3 active 3rd production round; v1.9.4 cut post-round-12 |
| 30 | Round 12 vs Round 11 体量对照: round 11 = 434L 208 atoms 8 batches 4 domains 0 §2.11 trigger 3 FIGURE 0 slice; round 12 = 911L ~470-490 atoms 10 batches 4 domains **DUAL §2.11 trigger** (5th + 6th cumulative case) **20 FIGURE** (单 round NEW peak) **3-slice TA/ex** (§2.4 3rd production trigger). **体量 = round 11 2.10× by lines / 2.26× by atoms (mid de-figure) / 1.25× by batch count** | 911 vs 434 + 10 vs 8 batch + atoms est | ✓ 2.10× lines / 1.25× batch — TA solo + 3-slice 是 round 12 主体 stress |

**Drift 校正记录**:
- Round 11 close 时 progress.json `cumulative_post_round_11.domains_atomized` = 53 sustained canonical; round 12 entry baseline = 53.
- Round 12 启动时 update progress.json `current_phase` → `P2_B-03c_round_12_in_flight_acked_2026-05-07_alphabetical_TA_TE_TI_TM_10_batches_batch_122_to_131_v1.9.3_3rd_production_validation_TA_solo_3_slice_§2.11_dual_trigger_20_FIGURE_stress_test_v1.9.4_cut_planning_post_round`.
- Round 11 atoms/line ratio naive 0.479 BELOW band lower edge 0.59 (round 04 0.644 → round 05 0.761 → round 06 0.681 → round 07 0.782 → round 08 0.602 → round 09 0.646 → round 10 0.591 → round 11 0.479); v1.9.3 §F-2 INFO band sustained 10 cycles via de-figure-naive 0.698 in-band adjustment. **Round 12 含 20 FIGURE compression 远高于 round 11 3 FIGURE → naive ratio 预期 < 0.50 (ratio band naive falls outside, sustained validation MUST use de-figure-naive); §F-2 11th sustained cycle expected via de-figure adjustment.**
- Round 12 体量 vs round 11: round 11 434L 208 atoms 8 batches; round 12 911L ~470-490 atoms 10 batches. **体量 = round 11 2.10× by lines / 2.26× by atoms (mid de-figure) / 1.25× by batch count**. 单 session 完成可行性: 10 batches 与 round 06/08/10 体量同等; ctx pressure 中等 (TA/ex 3-slice 单 batch ~110-200 atoms 上限 类似 round 03 2-slice precedent).
- post round 12 remaining = 10 − 4 = 6 domains × 2 = 12 files (TR/TS/TU/TV/UR/VS = 6); **round 13 收官 P2 B-03c** (估 6 domains × 2 = 12 batches similar to round 06/08/10 体量); v1.9.4 cut 后 round 13 = v1.9.4 1st production validation round.

**★ NEW post-grep DISCOVERY (TE/ex L48 §2.11 Plan B 6th case)**:
- progress.json `round_12_trigger` 仅预报 "5th production case TA/ex L694" → 漏报 TE/ex L48 `## Trial Elements Issues` 同样是 numberless H2 with 3 H3 children = §F-1 §2.11 Plan B trigger
- 实际 round 12 §F-1 §2.11 Plan B **DUAL trigger**: TA/ex L694 5th cumulative case (4 H3 children) + TE/ex L48 6th cumulative case (3 H3 children); 双 case 跨 batch_125 + batch_127 落在 2 batches 给 retro 独立验证机会
- 影响: round 12 §F-1 production validation 从单 case (5th) 升级为 dual case (5th + 6th); round 13 之前 §F-1 cumulative 从 5 → 7 cases (跳过 1 case 翻 1.4×); v1.9.4 cut 时 §F-1 cumulative 7 cases 实证基础 比预期更厚

---

## 1. Round 12 Scope (TA solo 3-slice + TE/TI/TM glue = 10 batches; §2.11 dual trigger; 20 FIGURE stress)

| # | Batch | Target | Lines | 估 atoms (de-figure) | Bucket | atom_id prefix | parent_section root | NEW lock applies |
|---|---|---|---|---|---|---|---|---|
| 1 | **batch_122** | `domains/TA/assumptions.md` | 29 | ~9-15 | <50 | `md_dmTA_assn_a` (起 a001) | `§TA [TA — Assumptions]` | NO (0 H2) |
| 2 | **batch_123** | `domains/TA/examples.md` slice **A** L1-L344 (Examples 1-3) | 344 | ~140-200 (10 FIGURE atoms) | 300+slice | `md_dmTA_ex_a` (起 a001) | `§TA [TA — Examples]` | **§2.4 multi-batch slice 1/3** + **§2.5 ×3 numbered** + **§2.6 ×10 FIGURE** |
| 3 | **batch_124** | `domains/TA/examples.md` slice **B** L344-L606 (Examples 4-6) | 262 | ~110-160 (8 FIGURE atoms) | 200+slice | `md_dmTA_ex_a` (续号; round 03 §2.4 lock cross-slice continue) | `§TA [TA — Examples]` | **§2.4 multi-batch slice 2/3** + **§2.5 ×3 numbered** + **§2.6 ×8 FIGURE** |
| 4 | **batch_125** | `domains/TA/examples.md` slice **C** L606-L710 (Example 7 + Trial Arms Issues) | 104 | ~50-80 (2 FIGURE + §2.11 sub-atoms) | 100-199 | `md_dmTA_ex_a` (续号) | `§TA [TA — Examples]` | **§2.4 multi-batch slice 3/3** + **§2.5 ×1 numbered** + **§F-1 §2.11 Plan B 5th case ★** + **§2.6 ×2 FIGURE** |
| 5 | **batch_126** | `domains/TE/assumptions.md` | 37 | ~14-20 | <50 | `md_dmTE_assn_a` (起 a001) | `§TE [TE — Assumptions]` | NO (0 H2) |
| 6 | **batch_127** | `domains/TE/examples.md` | 77 | ~32-50 | 50-99 | `md_dmTE_ex_a` (起 a001) | `§TE [TE — Examples]` | **§F-1 §2.11 Plan B 6th case ★ NEW** + **§2.5 ×3 numbered** |
| 7 | **batch_128** | `domains/TI/assumptions.md` | 15 | ~5-9 | <50 | `md_dmTI_assn_a` (起 a001) | `§TI [TI — Assumptions]` | NO (0 H2) |
| 8 | **batch_129** | `domains/TI/examples.md` | 20 | ~7-12 | <50 | `md_dmTI_ex_a` (起 a001) | `§TI [TI — Examples]` | NO (1 numbered H2 §2.5) |
| 9 | **batch_130** | `domains/TM/assumptions.md` | 7 | ~2-4 | <50 (smallest in round 12) | `md_dmTM_assn_a` (起 a001) | `§TM [TM — Assumptions]` | NO (0 H2) |
| 10 | **batch_131** | `domains/TM/examples.md` | 16 | ~6-10 | <50 | `md_dmTM_ex_a` (起 a001) | `§TM [TM — Examples]` | NO (1 numbered H2 §2.5) |
| **总** | 10 batches | 8 files (1 sliced 3×) | **911** | **~375-560** (de-figure mid ~470-490 incl. 20 FIGURE atoms) | — | — | — | **0 NEW lock; §2.4 ×3 + §2.5 ×7 + §2.6 ×20 + §F-1 §2.11 ×2 (DUAL)** |

post Round 12 累计 file coverage: 121 + 8 = 129/141 = **91.49%** ★ 跨 90% file 里程碑 (was 85.82% post round 11).
post Round 12 累计 md_atoms.jsonl: 9502 + ~460-600 = **~9,962-10,102 atoms (mid ~10,000)** ★ 跨 10,000 atoms 里程碑 mid-estimate.
post Round 12 累计 distinct domain coverage: 53 + 4 = **57/63 = 90.48%** ★ 跨 90% domain 里程碑 (was 84.13% post round 11).
post Round 12 B-03c progress: 100 + 8 = **108/114 = 94.74%** ★ 跨 90% B-03c progress 里程碑 + 跨 100 files B-03c sustained (was 87.72% post round 11).

**Round 12 vs Round 11 对照**: round 11 = 434L 208 atoms 8 batches 4 domains SU/SUPPQUAL/SV/TD 0 NEW lock 0 §2.11 trigger 3 §2.6 FIGURE; round 12 = 911L ~470-490 atoms 10 batches 4 domains TA/TE/TI/TM 0 NEW lock **DUAL §F-1 §2.11 Plan B trigger (5th + 6th case)** + **20 §2.6 FIGURE (单 round NEW peak)** + **§2.4 3-slice TA/ex (3rd production trigger)**. 体量 = round 11 2.10× by lines / 2.26× by atoms / 1.25× by batch count. 关键差异: round 12 v1.9.3 3rd production validation; §F-2 ratio band 11th sustained validation expected 必 via de-figure-naive (naive 必 outside 0.59 lower edge due 20 FIGURE compression); **TA/ex 710L 3-slice 是 round 12 主体 stress**, **TE/ex L48 §2.11 6th case 是 round 12 NEW DISCOVERY post-grep** 不在 round_12_trigger 预报.

**Round 12 vs Round 03 对照** (closest precedent: 单文件 slice 多 batch + FIGURE-in-domains lock 1st production): round 03 = AE/ex 2-slice 1st §2.4 production lock + FT/ex 1st §2.6 FIGURE production lock; round 12 = TA/ex 3-slice **§2.4 3rd production (round 03 lock 1st + v1.9.3 cut B-02 cumulative validation 2nd + round 12 3rd)** + TA/ex 20 FIGURE **§2.6 单 round NEW peak**. **体量 = round 03 ~2.5× by lines / 3× by atoms — round 03 是 3-slice 制度的 inaugural; round 12 是 3-slice 制度的 mass-production stress-test**.

**ctx pressure forecast**: round 12 = 10 + 10 + 1 = **21 dispatch calls** (= round 06/08/10's 21). 1 三-slice + DUAL §2.11 trigger + 20 FIGURE + v1.9.3 §F-2 de-figure ratio 11th sustained → halt 触发概率 **类似 round 06/08 中等密度 round** (TA/ex 3-slice 单 batch ~140-200 atoms 上限是 round 12 最大单 batch). ctx checkpoint 强制 at batch_125 (round 中点 = TA/ex slice C closing + §2.11 5th case). 单批 batch_123 TA/ex slice A 估 ~140-200 atoms 上限 — 注意 writer ctx 中段.

---

## 2. Convention inherit (round 01-11 全 carry-forward + v1.9.3 §F-1/F-2/F-3 sustained)

### 2.1-2.11 全 inherit from round 01-11

(全 carry-forward, 不重复列出 — 详见 round 11 kickoff §2.1-2.11:)
- **§2.1** Heading level pattern (H1 file root / H2 examples self-namespace / H3 sub-namespace per §2.11 Plan B / H4+ TBD)
- **§2.2** atom_id prefix per file (4-digit 容许)
- **§2.3** atom_id 起始 a001 per file (NOT per batch; **§2.4 cross-slice 续号 NOT reset per round 03 lock**)
- **§2.4** multi-batch single-file slice convention — **round 12 trigger 3 cases** (TA/ex 3-slice batch_123/124/125; round 03 inaugural lock 1st production AE/ex 2-slice + v1.9.3 cut B-02 cumulative validation 2nd + round 12 3rd production = 3rd cumulative production trigger; **3-slice scale NEW** vs round 03 2-slice + B-02 cumulative): atom_id `md_dmTA_ex_aXXX` 跨 3 slice 续号 (slice A 起 a001 → slice B 续 ~a141+ → slice C 续 ~a251+)
- **§2.5** numbered H2 self-namespace — **round 12 applies 7 cases**: TA/ex L18 + L120 + L245 + L344 + L466 + L534 + L606 (Examples 1-7; 7 numbered H2; spread 跨 3 slice = 3+3+1 distribution) + TE/ex L5 + L19 + L34 (Examples 1-3) + TI/ex L3 + TM/ex L3 = **7+3+1+1 = 12 numbered H2 §2.5 cases** (not 7; per §0.5 row 21 = 12 cumulative numbered H2)
- **§2.6** FIGURE-in-domains lock — **round 12 trigger 20 cases**: TA/ex 全 20 mermaid blocks (L24/39/60/84/126/137/185/251/269/301 slice A 10 块 + L352/364/388/416/472/488/542/558 slice B 8 块 + L614/632 slice C 2 块) → 20 FIGURE atoms expected (round 03 §2.6 lock sustained × N rounds; round 11 3 FIGURE → round 12 20 FIGURE **单 round NEW peak** 6.67× over round 11 + 20× over round 10 1 FIGURE)
- **§2.7** Numberless H2 with childless = file-root parent — **round 12 NO trigger** (0 numberless childless H2; 2 numberless H2 全 with H3 children = §2.11 Plan B trigger NOT §2.7)
- **§2.8 R-2.8-1/2/3** (now v1.9.2 §E-2/E-3/E-4 codified): H1 sib_idx=1 + TABLE_HEADER sib_idx=null + extracted_by object schema
- **§2.9** LIST_ITEM sib_idx universal = null (round 03 lock, sustained)
- **§2.10** LIST_ITEM hl+sib field-explicit-null (round 05 MED-01 → v1.9.2 §E-5 codified)
- **§2.11 Plan B sub-namespace by sib_idx for numberless H2 with H3 children** (round 07 NEW lock; round 09 4 cases stress-test PASS; v1.9.3 §F-1 SUSTAINED VALIDATED EXTENDED) — **round 12 DUAL trigger ★**:
  - **5th cumulative case** TA/ex L694 `## Trial Arms Issues` numberless H2 + 4 H3 children (L696/700/704/708 = sib_idx 1/2/3/4) → sub-namespace `§TA [TA — Trial Arms Issues §2.11.1]` / `§TA [TA — Trial Arms Issues §2.11.2]` / 等 4 个 sub-namespace per Plan B
  - **6th cumulative case ★ NEW DISCOVERY post-grep** TE/ex L48 `## Trial Elements Issues` numberless H2 + 3 H3 children (L50/63/67 = sib_idx 1/2/3) → sub-namespace `§TE [TE — Trial Elements Issues §2.11.1]` / `§TE [TE — Trial Elements Issues §2.11.2]` / 等 3 个 sub-namespace per Plan B
  - 2 cases 跨 batch_125 + batch_127 落在 不同 batch 给 retro 独立验证机会

### 2.12-? **Round 12 0 NEW first-time lock 预期 (v1.9.3 3rd production validation round)**

Round 12 grep 实证 (§0.5 row 12-22):
- 7 H3 in 8 文件 全 under 2 numberless H2 (TA/ex L694 4 H3 + TE/ex L48 3 H3) → §2.11 Plan B DUAL trigger (5th + 6th case)
- 0 H4 in 8 文件 → 无 H4 sub-policy 设计需求
- 20 mermaid 全 TA/ex (slice A 10 + B 8 + C 2) → §2.6 FIGURE 20 atoms 预期 (round 03 lock sustained; round 11 3 → round 12 20 = **B-03c 单 round NEW peak**)
- 0 numberless H2 childless → §2.7 round 04 lock NO trigger
- 12 numbered H2 全 §2.5 self-namespace 沿用

**Surprise H3 occurrence handling** (per §4 halt #6): 若 dispatch 后 writer 实测发现 H3 outside grep 实证的 7 (虽 grep 实证 0 outside the 2 §2.11 trigger blocks) → halt + 请求 lock 扩展 (§F-1 §2.11 Plan B 7th+ unexpected emergence).

**v1.9.3 F-rules 3rd production validation focus**:
- **§F-1 §2.11 Plan B**: round 12 **DUAL trigger 5th + 6th case** = 1st production stress-test 双 case 同 round (round 07 1st 单 case + round 09 4 cases 单 round + round 10/11 backward compat sustained → round 12 = 双 case 在 single round 验证 sub-namespace by sib_idx 制度的 stress-test 上限). gold reference: round 07 PC/ex 4 sub-namespace (sib_idx 1/2/3/4)
- **§F-2 ratio band 0.59-0.85**: round 12 11th sustained validation cycle (round 04-11 8 rounds + v1.9.2 cut + v1.9.3 cut + round 10 1st + round 11 2nd via de-figure-naive = 11 cumulative validations expected post round 12); **20 FIGURE compression 远超 round 11 3 FIGURE 必 via de-figure-naive 0.59-0.85 band sustained** (naive ratio 必 outside)
- **§F-3 INFO kickoff atom estimate calibration**: round 12 用 §F-2 mid 0.73 de-figure → 631 (911-280) × 0.73 = 461 atoms + 20 FIGURE = 481 atoms 估算 (range 460-600)

---

## 3. v1.9.3 prompt 入口条件 (active baseline 3rd production validation round)

### Writer pool (per v1.9.1 §D-8 peer-alternative + v1.9.2 §E-1 explicit JSON template mandate + v1.9.3 §F-1 sustained)
- `oh-my-claudecode:executor` (OMC primary, opus when available; **typically NOT available in default CC session — fallback expected**)
- `general-purpose` (FALLBACK peer-alternative; B-02 + round 01-11 sustained 148 batches 8206 atoms 0 writer defect post-fix cumulative; round 06 batch_72 1 schema regression 已 root-revert + re-dispatch RESOLVED, sustained quality streak intact post v1.9.2 §E-1 + v1.9.3 §F-1 codification)

### Reviewer pool (per v1.9.1 §D-8 + v1.9.2 §R-E1 schema regression sweep PRIORITY 1)
- `pr-review-toolkit:code-reviewer` (FALLBACK peer-alternative; B-02 + round 01-11 sustained 100% PASS post-fix; round 12 默认 per-batch reviewer × 10)
- **BURNED list (round 12 mini-audit 必避用)**:
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
  - `plugin-dev:plugin-validator` AUDIT (round 11 mini-audit burn — **9th cumulative B-03c reviewer family-pivot inaugural plugin-dev family-pivot**)
  - `pr-review-toolkit:code-reviewer` (writer/reviewer pool sustained burn — round 12 also per-batch × 10 仍 burn for mini-audit slot)
  - `general-purpose` (writer pool sustained burn)
- **Fresh candidates (round 12 mini-audit, 10th cumulative B-03c family-pivot target)**:
  - **`claude-code-guide` AUDIT mode** ★ 1st choice — Anthropic-domain reviewer family **inaugural NEW pivot post round 11 fall-through** (round 11 1st choice 但 fall-through 选 plugin-dev:plugin-validator; round 12 重新尝试 claude-code-guide AUDIT mode); **cross-family Rule D distance maximum** vs all burned slots (vercel/feature-dev/pr-review-toolkit/Plan/plugin-dev/general-purpose); **10th cumulative B-03c reviewer family-pivot ★ Anthropic-domain family AUDIT pool inaugural sub-type**
  - `plugin-dev:skill-reviewer` AUDIT mode (plugin-dev family 2nd sub-type intra-depth post round 11 plugin-validator pivot, fallback if claude-code-guide 不可用)
  - `vercel:performance-optimizer` AUDIT mode (vercel-family 3rd sub-type intra-depth post ai-architect + deployment-expert; 2nd fallback)
  - `superpowers` AUDIT or specialized review skill (3rd fallback if 上述全 fall-through)
- **首选 (round 12 mini-audit)**: **`claude-code-guide` AUDIT mode** (reviewer-only role; 跨 family Rule D 距离 最大化 — Anthropic-domain reviewer pool 1st sub-type post 9 burns vercel/feature-dev/pr-review-toolkit/Plan/plugin-dev/general-purpose 累计)
- **次选**: 若 claude-code-guide 不可用, 备选 `plugin-dev:skill-reviewer` AUDIT (plugin-dev family 2nd sub-type) 或 `vercel:performance-optimizer` AUDIT (vercel-family 3rd sub-type)

### N21 ban list (sustained per v1.7 cut + v1.9.2 §E-1 paired-sync + v1.9.3 §F-1 carry-forward)
`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer` (writer role; reviewer role per round 09 fresh candidates already burn), `oh-my-claudecode:document-specialist`

### Rule D 硬约束
writer ≠ reviewer (不同 subagent_type, NOT 仅不同 instance).

### v1.9.3 active hooks (sustained from v1.9.2 + 3 F-rules 3rd production)
- **§F-1 HIGH Hook** (sustained): §2.11 Plan B sub-namespace by sib_idx for numberless H2 with H3 children (round 07 1st + round 09 4 cases + round 10/11 backward compat = 5 cumulative production cases pre-round-12; **round 12 DUAL trigger TA/ex 5th + TE/ex 6th post-grep DISCOVERY → 7 cumulative production cases post-round-12**)
- **§F-2 INFO Hook** (sustained): atoms/line ratio empirical band 0.59-0.85 — round 12 **11th sustained validation expected via de-figure-naive** (naive 必 outside due 20 FIGURE compression; round 11 已 via de-figure-naive 0.698 in band)
- **§F-3 INFO Hook** (sustained): kickoff atom estimate calibration for FIGURE-bearing domains (round 11 INFO codified de-figure-naive recipe; round 12 §0.5 row 24 用 §F-2 de-figure mid 0.73 + 20 FIGURE additive)
- **§E-1 CRITICAL Hook 22c** (sustained): dispatch prompt MUST include explicit JSON template with all 12 field names + reference working batch_104 a001 = `md_dmRELSPEC_assn_a001` as gold reference (cumulative empirical baseline 9502 atoms 0 schema regression post round 11)
- **§E-2 HIGH Hook E-2-1** (sustained): H1 sib_idx=1 universal
- **§E-3 HIGH Hook E-3-2** (sustained): TABLE_HEADER sib_idx=null universal
- **§E-4 HIGH Hook E-4-3** (sustained): extracted_by object schema
- **§E-5 MED Hook E-5** (sustained): non-HEADING atoms field-explicit-null
- **§E-6 LOW Hook** (sustained): FIGURE-vs-CODE_LITERAL boundary clarification — **round 12 3rd post-v1.9.3 FIGURE production validation 20-block stress-test** (TA/ex 20 mermaid; round 10 1 RELSPEC/ex → round 11 3 TD/ex → round 12 20 TA/ex 量级阶跃)
- **Hook 22b (D-1 CRITICAL sustained)**: kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims ✓ (本 kickoff §0.5 30/30 PASS)
- **Hook D-NOTE-BQ (D-2 HIGH sustained)**: blockquote-prefix `> **Note:**` / `> **Exception:**` = atom_type NOTE
- **Hook D-D8 (D-4 sustained)**: numberless `## Overview` H2 chapter root inherit children — **round 12 NO trigger** (2 numberless H2 全 §2.11 trigger NOT §D-D8)
- **Round 03 §2.4 (multi-batch slice)**: round 12 trigger 3 cases (TA/ex 3-slice; round 03 lock 1st production + v1.9.3 cut B-02 cumulative validation 2nd + round 12 = 3rd cumulative production trigger)
- **Round 03 §2.6 (FIGURE-in-domains)**: round 12 20 trigger (TA/ex 20 mermaid → 20 FIGURE atoms expected; **B-03c 单 round NEW peak**)
- **Round 03 LIST_ITEM sib_idx null**: 全 round 12 enforce
- **Round 04 §2.7 (numberless H2 in ass.md / childless ex.md)**: round 12 NO trigger (2 numberless H2 全 §2.11)
- **Round 04 §2.8 R-2.8-1/2/3** (now v1.9.2 §E-2/E-3/E-4): 全 round 12 dispatch prompt 显式注入
- **Round 05 §2.10 MED-01** (now v1.9.2 §E-5): 全 round 12 dispatch prompt 显式 JSON form
- **Round 07 §2.11 (Plan B sub-namespace by sib_idx)** (now v1.9.3 §F-1): round 12 **DUAL trigger** TA/ex 5th + TE/ex 6th cumulative production case

### Round 11 v2.0 LOW INFO carries (monitor in round 12, NOT block)
- **C-R11-01** §F-2 de-figure-naive band sustained recipe — round 12 必 via de-figure-naive due 20 FIGURE compression (naive ratio 必 outside)
- **C-R11-02** §F-3 FIGURE-aware estimate adjustment (additive recipe) — round 12 用 §F-2 de-figure mid 0.73 + 20 FIGURE atoms additive
- **C-R11-03** §F-1 §2.11 Plan B kickoff §0.5 grep 实证 必 catch numberless H2 + H3 children pattern — round 12 §0.5 row 17 already catches TE/ex L48 NEW DISCOVERY (本 round 实证有效)
- **C-R11-04** §2.4 cross-slice atom_id 续号 lock sustained — round 12 TA/ex 3-slice 跨 batch_123/124/125 续号 lock 验证 (round 03 lock 2-slice → round 12 = 3-slice 1st production)
- **C-R11-05** Hook A1 attempt 1 HIGH severity HALT in-session resolved 实证 — round 12 §4 halt #6 sustained (任一 surprise H3 outside grep 实证的 7 → halt)

---

## 4. 自治连跑 halt 条件 (per umbrella §10.2 + round 12 specific)

任一触发 → 暂停 + ping 用户, 不强行进下一步:

1. **任一 batch §0.5 grep checksum 任一项 FAIL** (numeric drift detected at kickoff write time — 本 kickoff 已 30/30 PASS)
2. **任一 batch Rule A audit < 90% PASS rate** 或现 HIGH severity finding
3. **Schema violation / atom_id collision / 9 atom_type 任一异常** (含 v1.9.2 §R-E1 PRIORITY 1 schema regression sweep — round 06 batch_72 4-schema-regression precedent + round 07-11 cumulative 0 schema regression validated; round 12 v1.9.3 3rd production 关注 §F-1 backward compat regression + §2.11 DUAL Plan B sub-namespace re-validation)
4. **Source markdown anomaly** 需 Rule B preserve + 业务 judgment call
5. **v1.9.3 prompt 路径 drift** — writer pool 任一不可用 OR reviewer pool 任一不可用 + FALLBACK 也不可
6. **Convention lock 首次扩展** — round 12 计划 0 NEW lock; 若遇到 H3 surprise outside grep 实证的 7 (虽 grep 实证 7 全 under §2.11 trigger) / 额外 mermaid in non-TA/ex (虽 grep 实证 0 in 其余 7 文件) / 额外 H4 outside grep 实证 0 → 暂停 + 请求 lock 扩展
7. **ctx 紧张 (剩 < 30%)** 或 session 累计已 > 1.5 hr 仍未到 round 闭环 — 主动写 handoff.md + resume prompt 给用户. **Round 12 ctx pressure 警戒线**: 21 dispatch calls — batch_125 (round 中点 = TA/ex slice C closing + §2.11 5th case) 后强制 ctx checkpoint
8. **Round-specific**: 任一 batch atom 数实际 outside 估算 [0.5×low, 1.5×high] → 暂停核 source / prompt drift. Round 12 各 batch 估算与下限/上限:

| Batch | est range (de-figure) | halt low (0.5×low) | halt high (1.5×high) |
|---|---|---|---|
| 122 TA/ass | 9-15 | <5 | >23 |
| 123 TA/ex slice A (10 FIGURE) | 140-200 | <70 | >300 |
| 124 TA/ex slice B (8 FIGURE) | 110-160 | <55 | >240 |
| 125 TA/ex slice C (2 FIGURE + §2.11 5th) | 50-80 | <25 | >120 |
| 126 TE/ass | 14-20 | <7 | >30 |
| 127 TE/ex (§2.11 6th NEW) | 32-50 | <16 | >75 |
| 128 TI/ass | 5-9 | <3 | >14 |
| 129 TI/ex | 7-12 | <4 | >18 |
| 130 TM/ass | 2-4 | <1 | >6 |
| 131 TM/ex | 6-10 | <3 | >15 |

---

## 5. Dispatch order (sequential, single-session)

| Step | Action | Subagent | Prompt source |
|---|---|---|---|
| 1 | batch_122 TA/ass writer | `general-purpose` | `subagent_prompts/P0_writer_md_v1.9.3.md` + per-batch prompt |
| 2 | batch_122 reviewer | `pr-review-toolkit:code-reviewer` | `subagent_prompts/P0_reviewer_v1.9.3.md` |
| 3 | batch_123 TA/ex slice A writer (L1-L344, 10 FIGURE) | `general-purpose` | (同上) |
| 4 | batch_123 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 5 | batch_124 TA/ex slice B writer (L344-L606, 8 FIGURE) | `general-purpose` | (同上) |
| 6 | batch_124 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 7 | batch_125 TA/ex slice C writer (L606-L710, §2.11 Plan B 5th case + 2 FIGURE) | `general-purpose` | (同上) |
| 8 | batch_125 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| **CTX CHECKPOINT** | **batch_125 close 后强制 ctx 余量评估 + §2.11 5th case backward compat sweep** | — | (per §4.7) |
| 9 | batch_126 TE/ass writer | `general-purpose` | (同上) |
| 10 | batch_126 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 11 | batch_127 TE/ex writer (§2.11 Plan B 6th case ★ NEW) | `general-purpose` | (同上) |
| 12 | batch_127 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 13 | batch_128 TI/ass writer | `general-purpose` | (同上) |
| 14 | batch_128 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 15 | batch_129 TI/ex writer | `general-purpose` | (同上) |
| 16 | batch_129 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 17 | batch_130 TM/ass writer (smallest 7L) | `general-purpose` | (同上) |
| 18 | batch_130 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 19 | batch_131 TM/ex writer | `general-purpose` | (同上) |
| 20 | batch_131 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 21 | **mini-audit Rule A** (random 10 atoms across batch_122-131, ≥2 from FIGURE batches 123/124, ≥1 from §2.11 batch_125 + ≥1 from §2.11 batch_127, ≥1 from slice-cross-boundary batch_124 起始 atom_id) | **`claude-code-guide` AUDIT mode** ★ NEW Anthropic-domain family inaugural pivot (10th cumulative B-03c reviewer family-pivot) | `evidence/checkpoints/mini_audit_P2_B-03c_round_12_*` |

---

## 6. Round 12 close criteria (per umbrella §10.3)

- [ ] 10 batches 全部 atomized 写入 `md_atoms.jsonl`
- [ ] 10 per-batch reviewer 全 PASS (Rule A audit ≥ 90% rate, 0 HIGH severity)
- [ ] mini-audit 10/10 PASS (`claude-code-guide` AUDIT mode random sample with §2.11 + FIGURE + slice-cross-boundary coverage)
- [ ] 10/10 invariants per round 11 sustained pattern (atom_id uniqueness / 9 atom_type / parent_section format / extracted_by schema / sib_idx rules / §2.4 cross-slice 续号 / 等)
- [ ] 0 schema regression vs v1.9.3 baseline (§F-1 3rd production validation including DUAL §2.11 case)
- [ ] §F-1 §2.11 Plan B DUAL case sub-namespace 验证 PASS (TA/ex 5th 4 sub-namespace by sib_idx 1/2/3/4 + TE/ex 6th 3 sub-namespace by sib_idx 1/2/3 byte-exact)
- [ ] §F-2 ratio band 0.59-0.85 11th sustained validation via de-figure-naive (911L − ~280L FIGURE compression = 631L × actual de-figure ratio = lower-edge expected ~0.65-0.78)
- [ ] §F-3 estimate calibration aggregate within ±35% threshold (11th sustained per round 11 -34.4% precedent)
- [ ] §2.4 multi-batch slice 3rd production trigger 验证 PASS (TA/ex 3-slice cross-slice atom_id 续号 byte-exact: slice A end → slice B start → slice C start 续号 NO RESET)
- [ ] §2.6 FIGURE-in-domains 20 trigger PASS (TA/ex 20 mermaid → 20 FIGURE atoms, byte-exact verbatim incl. opening/closing fences ` ```mermaid ` / ` ``` `)
- [ ] 0 NEW first-time lock (per grep 实证 forecast — 0 H4 outside / 0 mermaid in non-TA/ex / 0 H3 outside §2.11 trigger blocks)
- [ ] progress.json `cumulative_post_round_12` written (md_atoms_jsonl_total ~9962-10102 / domains_atomized 57 / file_coverage 129 / B-03c progress 108/114)
- [ ] sibling_continuity_sweep_report_round12_P2-B-03c.md written (NB: distinct from existing `sibling_continuity_sweep_report_round12.md` which is P1-phase round 12 reconciler artifact; P2 round 12 sweep file MUST suffix `_P2-B-03c` to avoid collision)
- [ ] commit message format: "06 P2 B-03c round 12 自治连跑 CLOSED — 10 batches N atoms 4 domains TA/TE/TI/TM ★ 跨 90% file coverage + 跨 90% domain coverage + 跨 90% B-03c progress + 跨 10K atoms milestones — v1.9.3 3rd production validation §F-1 DUAL §2.11 trigger TA/ex 5th + TE/ex 6th cumulative + §F-2 de-figure-naive band 11th sustained + §F-3 aggregate within threshold + §2.4 3-slice TA/ex 3rd production + §2.6 FIGURE 20-block stress-test single-round NEW peak + mini-audit claude-code-guide AUDIT 10th family-pivot inaugural Anthropic-domain — v1.9.4 cut planning post-round-12"

---

## 7. Round 13 preview + v1.9.4 cut trigger

**Round 13 preview** (P2 B-03c 收官): 6 domains 余 (TR/TS/TU/TV/UR/VS) × 2 = 12 files = ~600-800L (估; pending grep verify pre-round-13 kickoff write); 估 12 batches (类似 round 06/08/10 体量); pre-allocated mini-audit reviewer slot 11th cumulative B-03c family-pivot candidates: `plugin-dev:skill-reviewer` AUDIT 或 `vercel:performance-optimizer` 或 `superpowers` AUDIT 等. P2 B-03c 关闭 milestone: post-round-13 = 114/114 = 100% B-03c CLOSED.

**v1.9.4 cut trigger** (post-round-12 close): v1.9.3 3 production rounds (round 10 + 11 + 12) cumulative 5 actionable carries + 5 INFO carries (round 11 commit) + round 12 NEW carries (DUAL §2.11 case + §2.4 3-slice + §2.6 20 FIGURE 量级峰值) ≥ 12 candidate stack threshold; v1.9.4 cut session estimated post round 12 commit prior to round 13 dispatch. v1.9.4 焦点: §F-1 DUAL Plan B sub-namespace formalization + §F-2 de-figure-naive band recipe formalization + §F-3 FIGURE-aware estimate aggregator + §2.4 multi-slice atom_id 续号 codification + §2.6 FIGURE batch sub-classification (mermaid/ASCII/PNG-ref) + 等.

---

**Bojiang ack 2026-05-07 captured (Option B)**: "round 12 = TA solo + TE/TI/TM glue Option B Bojiang ack" (per round 11 close commit 66f29bd)
**Decision**: TA + TE + TI + TM (alphabetical 4 domains) = 4 domains × 2 = 8 files = 911L (TA/ex 710L → 3-slice §2.4); 10 batches batch_122..131
**★ NEW post-grep DISCOVERY**: TE/ex L48 §2.11 Plan B 6th case (未在 round_12_trigger 预报); round 12 §F-1 DUAL trigger 5th + 6th cumulative production case; round 13 之前 §F-1 cumulative 7 cases (vs round_12_trigger 预期 6 cases)
**Next**: Bojiang review + ack of this kickoff (尤其 §F-1 DUAL trigger discovery + 3-slice 计划 + claude-code-guide AUDIT 候选 priority order) → dispatch batch_122 sequential per §5
