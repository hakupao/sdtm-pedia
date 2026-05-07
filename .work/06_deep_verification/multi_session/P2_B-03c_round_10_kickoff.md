# P2 B-03c Round 10 — Alphabetical RELSPEC/RELSUB/SM/SR/SS 5 Domains × 2 Files Kickoff (alphabetical recovery + v1.9.3 1st production validation)

> 创建: 2026-05-07 (post B-03c round 09 CLOSED commit 0c872e1 + v1.9.3 prompt cut COMPLETED commit 6990c54 同日; **v1.9.3 active baseline 第 1 个 production validation round** — 4 paired-sync prompts writer_md/pdf/matcher/reviewer + 3 NEW F-rules § F-1 §F-2 §F-3 首次 production 验证)
> 父 umbrella: `multi_session/P2_B-03_kickoff.md`
> 父 prompt (active baseline, v1.9.3 cut commit 6990c54): `subagent_prompts/P0_writer_md_v1.9.3.md` (3 NEW F-rules + 30 hooks) + `P0_matcher_v1.9.3.md` (30 hooks) + `P0_reviewer_v1.9.3.md` (35 hooks) + `P0_writer_pdf_v1.9.3.md` (paired-sync)
> Parent round close ref: `multi_session/P2_B-03c_round_09_kickoff.md` + commit 0c872e1 (round 09 close 10 batches 297 atoms 5 domains RELREC/RP/RS/SC/SE ★ v1.9.2 3rd sustained round + §2.11 Plan B 2nd production validation 4 cases including NEW References boundary RS/ex L92 + §2.7 lock 5 cases + §2.5 lock 6 cases + 0 NEW lock 0 halt 0 post-hoc fix; v1.9.3 cut planning trigger MET 2 rounds sustained → cut COMPLETED)
> 路由词: 用户 session 说 **"开始 work 的 06 的 Round 10"** → 主 session 经 grep verify + scope ack 流程 (Bojiang ack 2026-05-07 "RELSPEC/RELSUB 将来一定会做, 顺序由你决定") → 进本 kickoff dispatch
> Convention 继承: round 01-09 §2.1-2.11 全 carry-forward + v1.9.3 §F-1/F-2/F-3 NEW 注入; **round 10 NO NEW first-time lock 预期** (10 文件 grep 实证: 0 H4 / 1 mermaid RELSPEC/ex / 0 numberless H2 with H3 children → 0 §2.11 Plan B trigger; 7 numbered H2 §2.5 + 2 numberless childless H2 SUPPQUAL/ass §2.7 + 1 FIGURE §2.6)

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1 CRITICAL + v1.9.2 §E-1 paired-sync + v1.9.3 §F-2 ratio band)

逐项 grep-verified against source byte-exact (执行日 2026-05-07 post round 09 CLOSE + v1.9.3 cut). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令. 缺 §0.5 = orchestrator preflight FAIL.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | post B-03c round 09 CLOSE 时 md_atoms.jsonl 末原子 = `md_dmSE_ex_a050` (round 09 batch_103 final atom; parent_section `§SE.2 [Example 2]`; file `knowledge_base/domains/SE/examples.md`) | `tail -1 md_atoms.jsonl \| python3 -c "import sys,json; a=json.loads(sys.stdin.read()); print(a['atom_id'], a.get('parent_section'), a.get('file'))"` | ✓ md_dmSE_ex_a050, §SE.2 [Example 2], knowledge_base/domains/SE/examples.md |
| 2 | md_atoms.jsonl 当前总原子 = **9112** (post round 09 CLOSED) | `wc -l md_atoms.jsonl` | ✓ 9112 |
| 3 | round 09 实际产 atoms = **297** (9112 − 8815 round 09 起始基线) | progress.json `cumulative_post_round_09.md_atoms_jsonl_total` 9112 − round 08 close 8815 | ✓ 297 |
| 4 | round 09 atoms/line ratio = 297/460 = **0.646** (band 0.59-0.85 内 mid; v1.9.3 §F-2 INFO 9-round sustained band) | round 09 §0.5 row 4 source 460 + actual 297 atoms | ✓ 0.646 |
| 5 | 累计 distinct domains atomized in md_atoms.jsonl = **44** (canonical post round 09; round 08 close 39 + RELREC/RP/RS/SC/SE = 44) | `python3 -c "import json; d=set(); [d.add(json.loads(l)['atom_id'][5:].split('_')[0]) for l in open('md_atoms.jsonl') if json.loads(l)['atom_id'].startswith('md_dm')]; print(len(d), sorted(d))"` | ✓ 44 (AE/AG/BE/BS/CE/CM/CO/CP/CV/DA/DD/DM/DS/DV/EC/EG/EX/FA/FT/GF/HO/IE/IS/LB/MB/MH/MI/MK/ML/MS/NV/OE/OI/PC/PE/PP/PR/QS/RE/RELREC/RP/RS/SC/SE) |
| 6 | 累计 distinct files atomized in md_atoms.jsonl = **103** (post round 09; round 08 93 + RELREC/RP/RS/SC/SE × 2 = 103) | `python3 -c "import json; f=set(); [f.add(json.loads(l)['file']) for l in open('md_atoms.jsonl')]; print(len(f))"` | ✓ 103 |
| 7 | domains/ 余 = **19 domains** (63 total − 44 done = 19; post round 10 = 19 − 5 = 14) | 63 − 44 = 19 | ✓ 19 (RELSPEC/RELSUB/SM/SR/SS/SU/SUPPQUAL/SV/TA/TD/TE/TI/TM/TR/TS/TU/TV/UR/VS) |
| 8 | Round 10 scope = **RELSPEC/RELSUB/SM/SR/SS 5 domains alphabetical recovery** × 2 files = **10 source files** (alphabetical order RELSPEC<RELSUB<SM<SR<SS; recovery RELSPEC/RELSUB skipped in round 09) | `ls knowledge_base/domains/{RELSPEC,RELSUB,SM,SR,SS}/{assumptions,examples}.md` = 10 文件 | ✓ 10 source files |
| 9 | Round 10 source lines total = **308** (RELSPEC/ass 11 + RELSPEC/ex 47 + RELSUB/ass 21 + RELSUB/ex 38 + SM/ass 13 + SM/ex 40 + SR/ass 9 + SR/ex 116 + SS/ass 10 + SS/ex 3) | `wc -l knowledge_base/domains/{RELSPEC,RELSUB,SM,SR,SS}/{assumptions,examples}.md` | ✓ 308 |
| 10 | Round 10 size buckets: <50L=**9** (SS/ex 3 + SR/ass 9 + SS/ass 10 + RELSPEC/ass 11 + SM/ass 13 + RELSUB/ass 21 + RELSUB/ex 38 + SM/ex 40 + RELSPEC/ex 47), 50-99L=**0**, 100-199L=**1** (SR/ex 116), 200+slice=**0** | 文件大小逐项核 | ✓ 9/0/1/0 总 10 |
| 11 | Round 10 切片 = **0** (10 文件全 <300L threshold; SR/ex 116L 单 batch; round 09 同 0 slice 模式 sustained 第 2 round) | 全文件 <300L threshold | ✓ 0 slice (all single batch) |
| 12 | RELSPEC/ass.md H2 count = **0** (file-root only; H1 + body atoms) | `grep -nE "^## " knowledge_base/domains/RELSPEC/assumptions.md` | ✓ 0 H2 |
| 13 | RELSPEC/ex.md H2 count = **1** (L3 numbered `## Example 1`) → §2.5 self-namespace `§RELSPEC.1 [Example 1]`; **+ 1 mermaid block § §2.6 FIGURE-in-domains lock applies** | `grep -nE "^## " knowledge_base/domains/RELSPEC/examples.md` + `grep -c '\`\`\`mermaid' RELSPEC/examples.md` | ✓ 1 H2 (numbered) + 1 mermaid → 1 FIGURE atom expected |
| 14 | RELSUB/ass.md H2 count = **0** (file-root only) | `grep -nE "^## " knowledge_base/domains/RELSUB/assumptions.md` | ✓ 0 H2 |
| 15 | RELSUB/ex.md H2 count = **1** (L3 numbered `## Example 1`) → §2.5 self-namespace `§RELSUB.1 [Example 1]` | `grep -nE "^## " knowledge_base/domains/RELSUB/examples.md` | ✓ 1 H2 (numbered) |
| 16 | SM/ass.md H2 count = **0** (file-root only) | `grep -nE "^## " knowledge_base/domains/SM/assumptions.md` | ✓ 0 H2 |
| 17 | SM/ex.md H2 count = **1** (L3 numbered `## Example 1`) → §2.5 self-namespace `§SM.1 [Example 1]` | `grep -nE "^## " knowledge_base/domains/SM/examples.md` | ✓ 1 H2 (numbered) |
| 18 | SR/ass.md H2 count = **0** (file-root only; 9 lines minimal) | `grep -nE "^## " knowledge_base/domains/SR/assumptions.md` | ✓ 0 H2 |
| 19 | SR/ex.md H2 count = **3** (L3 + L25 + L85 全 numbered `## Example N`) → §2.5 self-namespace × 3 (`§SR.1 / §SR.2 / §SR.3 [Example N]`) | `grep -nE "^## " knowledge_base/domains/SR/examples.md` | ✓ 3 H2 (全 numbered) |
| 20 | SS/ass.md H2 count = **0** (file-root only; 10 lines minimal) | `grep -nE "^## " knowledge_base/domains/SS/assumptions.md` | ✓ 0 H2 |
| 21 | SS/ex.md H2 count = **0** (file-root only; **3 lines最 minimal — 仅 H1 + 可能 1 body atom**) ★ smallest file in round 10 | `grep -nE "^## " knowledge_base/domains/SS/examples.md` + `wc -l` | ✓ 0 H2, 3L total |
| 22 | Round 10 累计 H2 = **6** (0+1+0+1+0+1+0+3+0+0 = 6; **全 numbered §2.5**, 0 numberless → 0 §2.7 trigger 0 §2.11 Plan B trigger ★) | per-file 上述行 | ✓ 6 H2 全 numbered |
| 23 | Round 10 累计 H3 = **0** (10 文件全 0 H3) + H4 = **0** + mermaid = **1** (RELSPEC/ex 1 block) | 全 10 文件 grep | ✓ 0 H3 / 0 H4 / 1 mermaid |
| 24 | Batch 序号续 = **batch_104..113** (round 09 末 batch_103 = SE/ex; round 10 共 10 batches: 5 domains × 2 files) | round 09 §0.5 row 30 + round 09 close batch_103 final | ✓ batch_104..113 (10 batches) |
| 25 | Round 10 估 atoms = **182-262** (308L × 0.59 lower = 182; 308L × 0.73 mid = 225; 308L × 0.85 upper = 262; v1.9.3 §F-2 9-round sustained band 0.59-0.85) | 308 × {0.59, 0.73, 0.85} | ✓ 182-225-262 (mid ~225) |
| 26 | post Round 10 累计 md_atoms.jsonl ≈ **9,294-9,374 atoms** (mid ~9,337) | 9112 + 182-262 | ✓ ~9,294-9,374 |
| 27 | post Round 10 累计 file coverage = **113/141 = 80.14%** ★ 跨 80% file 里程碑 | 103 + 10 = 113; 113/141 = 0.8014 | ✓ 80.14% (was 73.05% post round 09) |
| 28 | post Round 10 累计 distinct domain coverage = **49/63 = 77.78%** | 44 + 5 = 49; 49/63 = 0.7778 | ✓ 77.78% (was 69.84% post round 09) |
| 29 | post Round 10 B-03c progress = **92/114 = 80.70%** ★ 跨 80% B-03c 里程碑 (round 09 close 82 + round 10 10 = 92) | 82 + 10 = 92; 92/114 = 0.8070 | ✓ 80.70% (was 71.93% post round 09) |
| 30 | v1.9.3 active baseline (commit 6990c54) post round 09 close — round 10 是 v1.9.3 第 1 个 production validation round; gold reference atom = `md_dmRELREC_assn_a001` (round 09 batch_94 first atom 预期 sustained pattern; v1.9.3 §F-1/F-2/F-3 全 1st production validation) | v1.9.3 active files: P0_writer_md_v1.9.3.md / P0_matcher_v1.9.3.md / P0_reviewer_v1.9.3.md / P0_writer_pdf_v1.9.3.md | ✓ v1.9.3 active (1st round) |

**Drift 校正记录**:
- Round 09 close 时 progress.json `cumulative_post_round_09.domains_atomized` = 44 sustained canonical; round 10 entry baseline = 44.
- Round 10 启动时 update progress.json `current_phase` → `P2_B-03c_round_10_in_flight_acked_2026-05-07_alphabetical_RELSPEC_RELSUB_SM_SR_SS_10_batches_batch_104_to_113_v1.9.3_1st_production_validation`.
- Round 09 atoms/line ratio 0.646 (round 04 0.644 → round 05 0.761 → round 06 0.681 → round 07 0.782 → round 08 0.602 → round 09 0.646); v1.9.3 §F-2 INFO 9-round sustained band 0.59-0.85 codified post v1.9.3 cut. Round 10 含 9 small (<50L) + 1 mid (100-199L SR/ex), 全 numbered H2 → 估算用 0.59-0.85 baseline (中性 vs round 09).
- Round 10 体量 vs round 09: round 09 460L 297 atoms 10 batches; round 10 308L ~225 atoms 10 batches. **体量 = round 09 0.67× by lines / 0.76× by atoms / 1.00× by batch count**. 单 session 完成可行性: 10 single batches 类似 round 08/09, 0 slice 干净, **预计 round 10 是 round 09 后期同等或更轻**.
- post round 10 remaining = 19 − 5 = 14 domains × 2 = 28 files (估 2-3 round 完成 P2 B-03c; round 11 候选 SU/SUPPQUAL/SV/TA/TD = 5 domains).

---

## 1. Round 10 Scope (alphabetical RELSPEC/RELSUB/SM/SR/SS × 2 files = 10 single-batch; no slicing)

| # | Batch | Target | Lines | 估 atoms | Bucket | atom_id prefix | parent_section root | NEW lock applies |
|---|---|---|---|---|---|---|---|---|
| 1 | **batch_104** | `domains/RELSPEC/assumptions.md` | 11 | ~6-9 | <50 | `md_dmRELSPEC_assn_a` (起 a001) | `§RELSPEC [RELSPEC — Assumptions]` | NO (0 H2) |
| 2 | **batch_105** | `domains/RELSPEC/examples.md` | 47 | ~22-32 | <50 | `md_dmRELSPEC_ex_a` (起 a001) | `§RELSPEC [RELSPEC — Examples]` | **NO but §2.6 FIGURE 1 trigger** (1 mermaid block → 1 FIGURE atom expected) + §2.5 ×1 numbered H2 |
| 3 | **batch_106** | `domains/RELSUB/assumptions.md` | 21 | ~12-18 | <50 | `md_dmRELSUB_assn_a` (起 a001) | `§RELSUB [RELSUB — Assumptions]` | NO (0 H2) |
| 4 | **batch_107** | `domains/RELSUB/examples.md` | 38 | ~22-32 | <50 | `md_dmRELSUB_ex_a` (起 a001) | `§RELSUB [RELSUB — Examples]` | NO (1 numbered H2 §2.5) |
| 5 | **batch_108** | `domains/SM/assumptions.md` | 13 | ~7-11 | <50 | `md_dmSM_assn_a` (起 a001) | `§SM [SM — Assumptions]` | NO (0 H2) |
| 6 | **batch_109** | `domains/SM/examples.md` | 40 | ~22-34 | <50 | `md_dmSM_ex_a` (起 a001) | `§SM [SM — Examples]` | NO (1 numbered H2 §2.5) |
| 7 | **batch_110** | `domains/SR/assumptions.md` | 9 | ~5-8 | <50 | `md_dmSR_assn_a` (起 a001) | `§SR [SR — Assumptions]` | NO (0 H2) |
| 8 | **batch_111** | `domains/SR/examples.md` | 116 | ~70-100 | 100-199 | `md_dmSR_ex_a` (起 a001) | `§SR [SR — Examples]` | NO (3 numbered H2 §2.5; biggest file in round) |
| 9 | **batch_112** | `domains/SS/assumptions.md` | 10 | ~5-8 | <50 | `md_dmSS_assn_a` (起 a001) | `§SS [SS — Assumptions]` | NO (0 H2) |
| 10 | **batch_113** | `domains/SS/examples.md` | 3 | **~1-2** ★ smallest | <50 | `md_dmSS_ex_a` (起 a001) | `§SS [SS — Examples]` | NO (0 H2, 3-line file 仅 H1 + 可能 1 body atom) |
| **总** | 10 batches | 10 files (0 sliced) | **308** | **~172-254** (mid ~225) | — | — | — | **0 NEW lock; §2.5 ×7 + §2.6 ×1 + §2.7 ×0 + §2.11 ×0** |

post Round 10 累计 file coverage: 103 + 10 = 113/141 = **80.14%** ★ 跨 80% file 里程碑 (was 73.05% post round 09).
post Round 10 累计 md_atoms.jsonl: 9112 + ~182-262 = ~9,294-9,374 atoms (mid ~9,337).
post Round 10 累计 distinct domain coverage: 44 + 5 = **49/63 = 77.78%** (was 69.84% post round 09).
post Round 10 B-03c progress: 82 + 10 = 92/114 = **80.70%** ★ 跨 80% B-03c 里程碑 (was 71.93% post round 09).

**Round 10 vs Round 09 对照**: round 09 = 460L 297 atoms 10 batches 5 domains RELREC/RP/RS/SC/SE 0 NEW lock 4 §2.11 Plan B trigger 9 H3 stress-test; round 10 = 308L ~225 atoms 10 batches 5 domains RELSPEC/RELSUB/SM/SR/SS 0 NEW lock **0 §2.11 trigger** (cooling-off post stress-test) + **§2.6 FIGURE 1 trigger** (RELSPEC/ex 1 mermaid). **体量 = round 09 0.67× by lines / 0.76× by atoms / 1.00× by batch count**. 关键差异: round 10 v1.9.3 active baseline 1st production validation (post v1.9.3 cut commit 6990c54); §F-1 §F-2 §F-3 全 1st production validation; 0 §2.11 Plan B trigger 让 round 10 成 **§F-2 ratio band sustained 验证 + §F-1 backward compat 验证** 而非 stress-test round.

**Round 10 vs Round 08 对照** (closest precedent: 0 §2.11 trigger + 0 NEW lock + small files): round 08 = 399L 240 atoms 10 batches 5 domains PE/PP/PR/QS/RE 0 NEW lock 0 §2.11 trigger 0 H3; round 10 = 308L ~225 atoms 10 batches 5 domains 0 NEW lock 0 §2.11 trigger 0 H3 + §2.6 FIGURE 1 trigger. **体量 = round 08 0.77× by lines / 0.94× by atoms — round 08 接近原型**.

**ctx pressure forecast**: round 10 = 10 + 10 + 1 = **21 dispatch calls** (= round 06/08/09). 0 slice + 0 NEW lock + v1.9.3 §F-2 ratio sustained → halt 触发概率 **类似 round 08 干净 round**. ctx checkpoint 强制 at batch_109 (round 中点 SM/ex). 单批 SR/ex 估 ~85 atoms 上限 — 注意 writer ctx 中段.

---

## 2. Convention inherit (round 01-09 全 carry-forward + v1.9.3 §F-1/F-2/F-3 NEW)

### 2.1-2.11 全 inherit from round 01-09

(全 carry-forward, 不重复列出 — 详见 round 09 kickoff §2.1-2.11:)
- **§2.1** Heading level pattern (H1 file root / H2 examples self-namespace / H3 sub-namespace / H4+ TBD)
- **§2.2** atom_id prefix per file (4-digit 容许)
- **§2.3** atom_id 起始 a001 per file (NOT per batch; 不跨 file 续号)
- **§2.4** multi-batch single-file slice convention — **round 10 NO trigger** (10 文件全 <300L, 全 single batch)
- **§2.5** numbered H2 self-namespace — **round 10 applies 7 cases**: RELSPEC/ex L3 + RELSUB/ex L3 + SM/ex L3 + SR/ex L3+L25+L85 + SS/ex (n/a 0 H2) wait recount: RELSPEC/ex 1 + RELSUB/ex 1 + SM/ex 1 + SR/ex 3 = 6 numbered H2 § §2.5 ×6 cases (NOT 7 — SS/ex 0 H2). **修正**: §2.5 6 cases, NOT 7.
- **§2.6** FIGURE-in-domains lock — **round 10 trigger 1 case**: RELSPEC/ex 1 mermaid block → 1 FIGURE atom expected (round 03 §2.6 lock sustained × N rounds; round 10 1st FIGURE atom in B-03c since round 06 batch_72 ML/MS area 待 grep 确认 — anyway sustained per round 03 lock)
- **§2.7** Numberless H2 with childless = file-root parent (round 04 lock FT/ass) — **round 10 NO trigger** (0 numberless H2 in round 10 grep 实证; 6 numbered H2 全 §2.5)
- **§2.8 R-2.8-1/2/3** (now v1.9.2 §E-2/E-3/E-4 codified): H1 sib_idx=1 + TABLE_HEADER sib_idx=null + extracted_by object schema
- **§2.9** LIST_ITEM sib_idx universal = null (round 03 lock, sustained)
- **§2.10** LIST_ITEM hl+sib field-explicit-null (round 05 MED-01 → v1.9.2 §E-5 codified): explicit JSON `"heading_level": null, "sibling_index": null` NOT omitted
- **§2.11 Plan B sub-namespace by sib_idx for numberless H2 with H3 children** (round 07 NEW lock; round 09 4 cases stress-test PASS; v1.9.3 §F-1 SUSTAINED VALIDATED EXTENDED) — **round 10 NO trigger** (0 numberless H2 with H3 children); §F-1 1st production validation will be **backward compat verification** instead of new trigger

**重要修正 §2.5 count**: §0.5 row 22 "6 H2 全 numbered" 是对的; §2.5 trigger 数 = 6 (RELSPEC/ex 1 + RELSUB/ex 1 + SM/ex 1 + SR/ex 3 = 6).

### 2.12-? **Round 10 0 NEW first-time lock 预期 (v1.9.3 1st production validation round)**

Round 10 grep 实证 (§0.5 row 12-23):
- 0 H3 in 10 文件 → 0 §2.11 Plan B trigger (cooling-off post round 09 stress-test 4 cases)
- 0 H4 in 10 文件 → 无 H4 sub-policy 设计需求
- 1 mermaid in 10 文件 (RELSPEC/ex) → §2.6 FIGURE 1 atom 预期 (round 03 lock sustained)
- 0 numberless H2 → 0 §2.7 trigger (round 10 全 numbered H2 + 4 ass.md 全 0 H2)
- 6 numbered H2 全 §2.5 self-namespace 沿用

**Surprise H4 occurrence handling** (per §4 halt #6): 若 dispatch 后 writer 实测发现 H4 (虽 grep 实证 0) → halt + 请求 lock 扩展.

**v1.9.3 NEW F-rules 1st production validation focus**:
- **§F-1 §2.11 Plan B**: round 10 0 trigger → backward compat verification (round 07/09 production atoms 应 unchanged in re-dispatch); round 10 不会触发新 §2.11 case
- **§F-2 ratio band 0.59-0.85**: round 10 8th sustained validation cycle (round 04-09 6 rounds + v1.9.2 1 round + v1.9.3 cut-内置 = round 10 是 v1.9.3 production 1st)
- **§F-3 INFO kickoff atom estimate calibration**: round 10 用 §F-2 mid 0.73 → 308 × 0.73 = 225 atoms 估算

---

## 3. v1.9.3 prompt 入口条件 (active baseline 1st round post-cut)

### Writer pool (per v1.9.1 §D-8 peer-alternative + v1.9.2 §E-1 explicit JSON template mandate + v1.9.3 §F-1 sustained)
- `oh-my-claudecode:executor` (OMC primary, opus when available; **typically NOT available in default CC session — fallback expected**)
- `general-purpose` (FALLBACK peer-alternative; B-02 + round 01-09 sustained 130 batches 7816 atoms 0 writer defect post-fix cumulative; round 06 batch_72 1 schema regression 已 root-revert + re-dispatch RESOLVED, sustained quality streak intact post v1.9.2 §E-1 explicit JSON template mandate post v1.9.3 §F-1 sub-namespace codification)

### Reviewer pool (per v1.9.1 §D-8 + v1.9.2 §R-E1 schema regression sweep PRIORITY 1)
- `pr-review-toolkit:code-reviewer` (FALLBACK peer-alternative; B-02 + round 01-09 sustained 100% PASS post-fix; round 10 默认 per-batch reviewer × 10)
- **BURNED list (round 10 mini-audit 必避用)**:
  - `feature-dev:code-reviewer` (round 01 mini-audit + round 02 batch_23 burn)
  - `feature-dev:code-architect` (round 02 mini-audit burn)
  - `pr-review-toolkit:type-design-analyzer` (round 03 mini-audit burn)
  - `pr-review-toolkit:silent-failure-hunter` (round 04 mini-audit burn)
  - `pr-review-toolkit:comment-analyzer` (round 05 mini-audit burn)
  - `pr-review-toolkit:pr-test-analyzer` (round 06 mini-audit burn)
  - `pr-review-toolkit:code-simplifier` (round 07 mini-audit burn — 5/5 pr-review-toolkit AUDIT pool 已耗尽)
  - `Plan` AUDIT mode (round 08 mini-audit burn — 1st planner-family AUDIT-pivot)
  - `feature-dev:code-explorer` AUDIT mode (round 09 mini-audit burn — 7th cumulative B-03c reviewer family-pivot, 3rd feature-dev sub-type)
  - `vercel:ai-architect` AUDIT (v1.9.3 cut audit slot #71 burn — 1st vercel-family AUDIT pivot; 8 PASS + 2 OBSERVATION + 0 FAIL with 3 in-place hotfixes)
  - `pr-review-toolkit:code-reviewer` (round 04+05+06+07+08+09 per-batch ~68 burn — round 10 也将作 per-batch reviewer × 10 仍 burn for mini-audit slot)
  - `general-purpose` (writer pool sustained burn)
- **Fresh candidates (round 10 mini-audit, vercel-family Plan + feature-dev:code-explorer AUDIT 已 burn)**:
  - **`vercel:deployment-expert` AUDIT mode** ★ 1st choice — vercel-family 2nd sub-type AUDIT pivot post v1.9.3 cut vercel:ai-architect; cross-family Rule D 距离 sustained vercel-family AUDIT pool extension; **8th cumulative B-03c reviewer family-pivot ★ vercel family AUDIT pool 2nd sub-type post ai-architect**
  - `vercel:performance-optimizer` AUDIT mode (vercel-family 3rd sub-type, fallback if deployment-expert 不可用)
  - `claude-code-guide` AUDIT mode (general-purpose-family pivot, 2nd fallback)
- **首选 (round 10 mini-audit)**: **`vercel:deployment-expert` AUDIT mode** (reviewer-only role; 跨 family Rule D 距离 vs feature-dev/pr-review-toolkit/Plan 历史 pivot 可接受 — vercel family 内 sub-type pivot post v1.9.3 ai-architect)
- **次选**: 若 vercel:deployment-expert 不可用, 备选 `vercel:performance-optimizer` 或 `claude-code-guide` AUDIT (halt + 请求 ack 选择)

### N21 ban list (sustained per v1.7 cut + v1.9.2 §E-1 paired-sync + v1.9.3 §F-1 carry-forward)
`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer` (writer role; reviewer role per round 09 fresh candidates already burn), `oh-my-claudecode:document-specialist`

### Rule D 硬约束
writer ≠ reviewer (不同 subagent_type, NOT 仅不同 instance).

### v1.9.3 active hooks (sustained from v1.9.2 + 3 NEW F-rules first production)
- **§F-1 HIGH Hook** (NEW): §2.11 Plan B sub-namespace by sib_idx for numberless H2 with H3 children (round 07 1st + round 09 4 cases sustained validated extended; round 10 0 trigger → backward compat)
- **§F-2 INFO Hook** (NEW): atoms/line ratio empirical band 0.59-0.85 9-round sustained (round 04-09 6 rounds + v1.9.2 cut 1 round + v1.9.3 cut 1 round + round 10 1st production validation = 9 cumulative validations expected post round 10)
- **§F-3 INFO Hook** (NEW): kickoff atom estimate calibration for multi-level nested-list domains (round 08 INFO-R08-01 codified; round 10 §0.5 row 25 用 §F-2 mid 0.73)
- **§E-1 CRITICAL Hook 22c** (sustained): dispatch prompt MUST include explicit JSON template with all 12 field names + reference working batch_70 a001 as gold reference; orchestrator preflight FAIL if missing (round 07-09 cumulative 990 atoms 0 schema regression validated v1.9.2 §E-1 effective)
- **§E-2 HIGH Hook E-2-1** (sustained): H1 sib_idx=1 universal (R-2.8-1 codified)
- **§E-3 HIGH Hook E-3-2** (sustained): TABLE_HEADER sib_idx=null universal (R-2.8-2 codified)
- **§E-4 HIGH Hook E-4-3** (sustained): extracted_by object schema (R-2.8-3 codified)
- **§E-5 MED Hook E-5** (sustained): non-HEADING atoms field-explicit-null (round 05 MED-01 codified; LIST_ITEM hl+sib explicit JSON form NOT omitted)
- **§E-6 LOW Hook** (sustained): FIGURE-vs-CODE_LITERAL boundary clarification — **round 10 1st post-v1.9.3 FIGURE production validation** (RELSPEC/ex 1 mermaid block)
- **Hook 22b (D-1 CRITICAL sustained)**: kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims ✓ (本 kickoff §0.5 30/30 PASS)
- **Hook D-NOTE-BQ (D-2 HIGH sustained)**: blockquote-prefix `> **Note:**` / `> **Exception:**` = atom_type NOTE
- **Hook D-D8 (D-4 sustained)**: numberless `## Overview` H2 chapter root inherit children — **round 10 NO trigger** (0 numberless H2)
- **Round 03 §2.4 (multi-batch slice)**: round 10 NO trigger (全 <300L)
- **Round 03 §2.6 (FIGURE-in-domains)**: round 10 1 trigger (RELSPEC/ex 1 mermaid → 1 FIGURE atom expected)
- **Round 03 LIST_ITEM sib_idx null**: 全 round 10 enforce
- **Round 04 §2.7 (numberless H2 in ass.md / childless ex.md)**: round 10 NO trigger (0 numberless H2 grep 实证)
- **Round 04 §2.8 R-2.8-1/2/3 (now v1.9.2 §E-2/E-3/E-4)**: 全 round 10 dispatch prompt 显式注入
- **Round 05 §2.10 MED-01 (now v1.9.2 §E-5)**: 全 round 10 dispatch prompt 显式 JSON form
- **Round 07 §2.11 (Plan B sub-namespace by sib_idx)** (now v1.9.3 §F-1): round 10 NO trigger; backward compat verification only

---

## 4. 自治连跑 halt 条件 (per umbrella §10.2 + round 10 specific)

任一触发 → 暂停 + ping 用户, 不强行进下一步:

1. **任一 batch §0.5 grep checksum 任一项 FAIL** (numeric drift detected at kickoff write time — 本 kickoff 已 30/30 PASS)
2. **任一 batch Rule A audit < 90% PASS rate** 或现 HIGH severity finding
3. **Schema violation / atom_id collision / 9 atom_type 任一异常** (含 v1.9.2 §R-E1 PRIORITY 1 schema regression sweep — round 06 batch_72 4-schema-regression precedent + round 07-09 cumulative 0 schema regression validated; round 10 v1.9.3 1st production 关注 §F-1 backward compat regression)
4. **Source markdown anomaly** 需 Rule B preserve + 业务 judgment call
5. **v1.9.3 prompt 路径 drift** — writer pool 任一不可用 OR reviewer pool 任一不可用 + FALLBACK 也不可
6. **Convention lock 首次扩展** — round 10 计划 0 NEW lock; 若遇到 H4 surprise (虽 grep 实证 0) / 额外 mermaid in non-RELSPEC/ex (虽 grep 实证 0 in 其余 9 文件) / 额外 H3 outside grep 实证 0 → 暂停 + 请求 lock 扩展
7. **ctx 紧张 (剩 < 30%)** 或 session 累计已 > 1.5 hr 仍未到 round 闭环 — 主动写 handoff.md + resume prompt 给用户. **Round 10 ctx pressure 警戒线**: 21 dispatch calls — batch_109 (round 6/10 中点 = SM/ex) 后强制 ctx checkpoint
8. **Round-specific**: 任一 batch atom 数实际 outside 估算 [0.5×low, 1.5×high] → 暂停核 source / prompt drift. Round 10 各 batch 估算与下限/上限:

| Batch | est range | halt low (0.5×low) | halt high (1.5×high) |
|---|---|---|---|
| 104 RELSPEC/ass | 6-9 | <3 | >14 |
| 105 RELSPEC/ex | 22-32 | <11 | >48 |
| 106 RELSUB/ass | 12-18 | <6 | >27 |
| 107 RELSUB/ex | 22-32 | <11 | >48 |
| 108 SM/ass | 7-11 | <4 | >17 |
| 109 SM/ex | 22-34 | <11 | >51 |
| 110 SR/ass | 5-8 | <3 | >12 |
| 111 SR/ex | 70-100 | <35 | >150 |
| 112 SS/ass | 5-8 | <3 | >12 |
| 113 SS/ex | 1-2 | <1 | >3 |

---

## 5. Dispatch order (sequential, single-session)

| Step | Action | Subagent | Prompt source |
|---|---|---|---|
| 1 | batch_104 RELSPEC/ass writer | `general-purpose` | `subagent_prompts/P0_writer_md_v1.9.3.md` + per-batch prompt |
| 2 | batch_104 reviewer | `pr-review-toolkit:code-reviewer` | `subagent_prompts/P0_reviewer_v1.9.3.md` |
| 3 | batch_105 RELSPEC/ex writer | `general-purpose` | (同上) |
| 4 | batch_105 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 5 | batch_106 RELSUB/ass writer | `general-purpose` | (同上) |
| 6 | batch_106 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 7 | batch_107 RELSUB/ex writer | `general-purpose` | (同上) |
| 8 | batch_107 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 9 | batch_108 SM/ass writer | `general-purpose` | (同上) |
| 10 | batch_108 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| **CTX CHECKPOINT** | **batch_108 close 后强制 ctx 余量评估** | — | (per §4.7) |
| 11 | batch_109 SM/ex writer | `general-purpose` | (同上) |
| 12 | batch_109 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 13 | batch_110 SR/ass writer | `general-purpose` | (同上) |
| 14 | batch_110 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 15 | batch_111 SR/ex writer (largest 116L) | `general-purpose` | (同上) |
| 16 | batch_111 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 17 | batch_112 SS/ass writer | `general-purpose` | (同上) |
| 18 | batch_112 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 19 | batch_113 SS/ex writer (smallest 3L) | `general-purpose` | (同上) |
| 20 | batch_113 reviewer | `pr-review-toolkit:code-reviewer` | (同上) |
| 21 | **mini-audit Rule A** (random 8 atoms across batch_104-113) | **`vercel:deployment-expert` AUDIT mode** ★ NEW vercel-family 2nd sub-type pivot | `evidence/checkpoints/mini_audit_P2_B-03c_round_10_*` |

---

## 6. Round 10 close criteria (per umbrella §10.3)

- [ ] 10 batches 全部 atomized 写入 `md_atoms.jsonl`
- [ ] 10 per-batch reviewer 全 PASS (Rule A audit ≥ 90% rate, 0 HIGH severity)
- [ ] mini-audit 8/8 PASS (`vercel:deployment-expert` AUDIT mode random sample)
- [ ] 10/10 invariants per round 09 sustained pattern (atom_id uniqueness / 9 atom_type / parent_section format / extracted_by schema / sib_idx rules / etc.)
- [ ] 0 schema regression vs v1.9.3 baseline (§F-1 backward compat verification)
- [ ] §F-2 ratio band 0.59-0.85 9th sustained validation (308L × actual ratio = mid range expected)
- [ ] 0 NEW first-time lock (per grep 实证 forecast)
- [ ] §2.6 FIGURE-in-domains 1 trigger PASS (RELSPEC/ex 1 mermaid → 1 FIGURE atom)
- [ ] progress.json `cumulative_post_round_10` written (md_atoms_jsonl_total / domains_atomized 49 / file_coverage 113 / B-03c progress 92/114)
- [ ] sibling_continuity_sweep_report_round10.md written
- [ ] commit message format: "06 P2 B-03c round 10 自治连跑 CLOSED — 10 batches N atoms 5 domains RELSPEC/RELSUB/SM/SR/SS ★ v1.9.3 1st production validation + §F-1 backward compat + §F-2 ratio band sustained 9 rounds + §2.6 FIGURE 1 trigger + alphabetical recovery RELSPEC/RELSUB"

---

**Bojiang ack 2026-05-07 captured**: "RELSPEC/RELSUB 将来一定会做, 顺序由你决定 — 写完 kickoff dispatch 直接开干"
**Decision**: alphabetical recovery first (RELSPEC + RELSUB) + 接 SM/SR/SS = 5 domains × 2 = 10 files = 308L
**Next**: dispatch batch_104 immediately per §5 sequential order.
