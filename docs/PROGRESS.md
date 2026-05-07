# 进度看板

> **唯一进度状态源**. 历史细节看 `.work/meta/worklog/INDEX.md`. 文件结构看 `.work/MANIFEST.md`. 一页纸入门看 `.work/AGENT_GUIDE.md`.
> 最后更新: 2026-05-07 (P2 B-03c round 09 CLOSED — ★ v1.9.2 3rd sustained round + §2.11 Plan B 2nd production validation 4 cases PASS including NEW `### References` boundary + §2.7 lock 5 cases PASS + §2.5 lock 6 cases PASS + 0 NEW lock 0 halt 0 post-hoc fix; v1.9.3 cut planning trigger MET 2 rounds sustained — cut recommended next session)

---

## 状态总览

| Phase | 状态 | 当前活动 | 下一步 / 阻塞 |
|-------|------|----------|---------------|
| **Phase 0** 方案设计 | ✅ 完成 | — | — |
| **Phase 1** xlsx 自动生成 | ✅ 完成 | — | — |
| **Phase 2** PDF 页码索引 | ✅ 完成 | — | — |
| **Phase 3-4** PDF 提取 | ✅ 完成 | 293 md / 63 域 | — |
| **Phase 5** 全量验证 | ✅ 完成 | Step 0-4 全过 | — |
| **Phase 6** 检索优化 | ✅ 完成 (P0-P2) | — | P3 → 已合并到 Phase 7 |
| **Phase 6.5** AI 平台部署 | 🟢 进行中 | Claude/NotebookLM 完成; ChatGPT/Gemini 双平台锁步 (范本就绪 Phase 0 待启) | 看 `ai_platforms/SYNC_BOARD.md` |
| **Phase 7** RAG + KG | ⏸ 待启动 | 设计完成 (`docs/DESIGN_RAG_KG.md`) | 实施前 5 步待办 (见 `phase7_handoff.md`) |
| **06 旁枝** Deep Verification | 🟢 进行中 | P2 B-03c round 09 CLOSED 2026-05-07 (★ v1.9.2 3rd sustained round PASS + §2.11 Plan B 2nd production validation 4 cases PASS including NEW `### References` boundary + §2.7 lock 5 cases + §2.5 lock 6 cases; 10 batches 297 atoms 5 domains RELREC/RP/RS/SC/SE 0 halt 0 post-hoc fix 0 NEW lock; 44/63 domains 69.84% / 103/141 files 73.05% / B-03c 82/114 = 71.93%; v1.9.3 cut planning trigger MET 2 rounds sustained — cut recommended next session); round 10 pending Bojiang ack scope (default SM/SR/SS/SU/SUPPQUAL) OR v1.9.3 cut 优先 | 详见 `.work/06_deep_verification/_progress.json` |
| **07 旁枝** Website | ✅ 完成 | Phase 6/7/8/9/10/11 全 closed; prod sdtm-pedia.pages.dev | — |
| **docs/jp** iTMS 納品 | 🟢 进行中 | Phase 1 P0 中間版 v0.5 已提出 2026-04-30 | 残 02/03 + 05/06/99 中文列充填 (Phase 2-3, 2026-05 中下旬) |
| **refactor v1** 项目重构 | 🟢 进行中 (段 2) | 段 1 closed 2026-05-06; 段 2 进行中 | 段 3 (路径迁移) 待 B-03c cycle 收官 |

**图例**: ✅ 完成 · 🟢 进行中 · ⏸ 待启动 · 🔴 阻塞

---

## 关键 milestone (近 30 天)

- 2026-05-07 — 06 P2 B-03c **round 09 CLOSED ★ v1.9.2 3rd sustained round + §2.11 Plan B 2nd production validation 4 cases including NEW `### References` boundary + §2.7 lock 5 cases + §2.5 lock 6 cases** (10 batches / 297 atoms / 5 domains RELREC/RP/RS/SC/SE alphabetical default; cumulative md_atoms 9112, file coverage 103/141 = 73.05%, domain coverage 44/63 = 69.84%, B-03c progress 82/114 = 71.93%; **0 NEW first-time lock 0 halt 0 post-hoc fix sustained**; §2.11 Plan B 4 trigger cases (RELREC/ex L3+L53 + RS/ex L3+L65) all PASS sub-namespace by sib_idx including 1 NEW boundary RS/ex L92 `### References` → `§RS.2.2 [References]` sib_idx-based namespace; §2.11 status promoted SUSTAINED VALIDATED EXTENDED post 2nd validation; per-batch Rule A 98/98 + mini-audit 8/8 + 10/10 invariants = 116/116 = 100%; **feature-dev:code-explorer AUDIT mode slot #9 7th cumulative B-03c reviewer family-pivot ★ feature-dev family AUDIT pool 3rd sub-type extension** N21 reviewer-only role exception; v1.9.2 §E-1..E-6 3rd sustained round 0 schema regression cumulative 990 atoms post-cut; v1.9.3 cut planning trigger MET 2 rounds sustained — cut recommended next session)
- 2026-05-06 — 06 P2 B-03c **round 08 CLOSED ★ v1.9.2 2nd sustained round + §2.7 lock 2 cases PASS + §2.5 lock 10 cases PASS** (10 batches / 240 atoms / 5 domains PE/PP/PR/QS/RE alphabetical default; cumulative md_atoms 8815, file coverage 93/141 = 65.96%, domain coverage 39/63 = 61.9%, B-03c progress 72/114 = 63.16%; **0 NEW first-time lock — B-03c 1st grep-verified 0-trigger round** (round 06 was 0 NEW but ratio-drift carry, round 08 is grep-verified 0 H3 + 0 H4 + 0 mermaid); §2.7 round 04 lock 2 trigger cases (PP/ex L106 + QS/ass L5) both file-root anchored 16+12 = 28 atoms PASS — rule stable post 2 productions; §2.5 numbered H2 self-namespace 10 case validation PASS (PE/PP×3/PR×3/QS/RE×2); v1.9.2 §E-1..E-6 2nd sustained validation 0 schema regression (cumulative 693 atoms post v1.9.2 cut clean); per-batch Rule A 86/86 + mini-audit 8/8 + 10/10 invariants = 104/104 = 100%; 0 halt 0 post-hoc fix; **Plan AUDIT mode slot #8 1st planner-family AUDIT-pivot 6th cumulative B-03c reviewer family-pivot**; v1.9.3 cut planning trigger MET stack 10 — decision deferred post round 09)
- 2026-05-06 — 06 P2 B-03c **round 07 CLOSED ★ §2.11 Plan B sub-namespace first production validation + v1.9.2 first round post-cut all PASS** (4 batches / 453 atoms / 1 domain PC solo PC/ass + PC/ex 3-way sliced; cumulative md_atoms 8575, file coverage 83/141 = 58.9%, domain coverage 34/63 = 54.0%; **NEW first-time lock §2.11 Plan B sub-namespace by sib_idx for numberless H2 with H3 children** PC/ex L58 case 7 H3 children + slug-conflict resolved L7 §PC.1 vs L120 §PC.2.4; §2.7 round 04 lock sustained for L556+L562 childless numberless H2; boundary L555/L556 clean; v1.9.2 §E-1..E-6 all PASS first production validation; per-batch Rule A 37/37 + mini-audit 8/8 + 10/10 invariants = 45/45 = 100%; 0 halt 0 post-hoc fix **cleanest B-03c round**; pr-review-toolkit:code-simplifier slot #7 5th AUDIT-pivot 9th cumulative B-03c reviewer family-pivot)
- 2026-05-06 — 06 P2 B-03c **round 06 CLOSED ★ 跨 50% domain coverage milestone** (10 batches / 331 atoms / 5 domains ML/MS/NV/OE/OI; cumulative md_atoms 8122, file coverage 57.4%, domain coverage 33/63 = 52.4% ★, 0 first-time lock, 1 RESOLVED HALT batch_72 schema regression → re-dispatch PASS, NEW v1.9.2 candidate #10 explicit JSON template; v1.9.2 stack 10 = ≥10 cut planning trigger met; PC defer to round 07 per Option C)
- 2026-05-06 — 06 P2 B-03c **round 05 CLOSED ★ 跨 50% file coverage milestone** (12 batches / 677 atoms / 6 domains IS-MK; cumulative md_atoms 7791, file coverage 50.4%, 0 first-time lock 最干净 round, 1 MED-01 fixed)
- 2026-05-06 — 06 P2 B-03c round 04 CLOSED (13 batches / 731 atoms / 6 domains EX-IE; cumulative md_atoms 7114, file coverage 41.8%)
- 2026-05-06 — refactor v1 段 1 CLOSED (顶层清污 + AGENT_GUIDE + project_knowledge_base 归档)
- 2026-05-06 — 06 P2 B-03c round 03 CLOSED (12 batches / 741 atoms / 5 domains DM-EG)
- 2026-05-06 — 06 P2 B-03c round 02 CLOSED (10 batches / 278 atoms)
- 2026-05-05 — 06 P2 B-03c round 01 CLOSED (10 batches / 510 atoms)
- 2026-05-05 — 06 P2 B-03b cycle CLOSED + B-03a SKIPPED post §0.5 drift correction
- 2026-05-05 — 06 v1.9.1 prompt cut COMPLETED (Rule D AUDIT slot #70 PASS)
- 2026-04-30 — docs/jp 中間版 v0.5 提出 (4.6MB / 6 件 xlsx)
- 2026-04-29 — 06 P1 CLOSURE 全闭环 (12487 atoms / 535 pages / 55 batches)
- 2026-04-29 — 07 Website Phase 7 closed (4 commits, prod URL canonical 31/31 PASS)
- 2026-04-28 — 07 Website Phase 6 (Multi-dim Comparison Page) closed
- 2026-04-27 — 07 Release v1.0 (公司发布版) closed (24 文件三语 release 包)
- 2026-04-24 — Phase 6.5 NotebookLM Phase 5 sign-off (smoke v4 R1 15/17 strict PASS)

→ **完整时间线**: `.work/meta/worklog/INDEX.md` → 各 phase 文件

---

## 数据指标速查

| 指标 | 值 | 来源 |
|------|----|----|
| 知识库 md 文件数 | 293 | `knowledge_base/` |
| 覆盖 domain 数 | 63 | 同上 |
| 06 累计 md_atoms | 9112 | `.work/06_deep_verification/_progress.json` `b_03c_round_09_details.cumulative_post_round_09.md_atoms_jsonl_total` |
| 06 P2 B-03c 进度 | 82/114 = 71.93% | 同上 `b_03c_progress_pct` |
| 06 P2 file coverage | 103/141 = 73.05% | 同上 `file_coverage_pct` |
| 06 P2 domain coverage | 44/63 = 69.84% | 同上 `domain_coverage_pct` |
| 06 累计 pdf_atoms | 12487 | P1 CLOSURE (2026-04-29) |
| Phase 6.5 Claude v2.6 | 24/24 A/B PASS, 0 衰减, capacity 77% | `ai_platforms/claude_projects/dev/test_results.md` |
| Phase 6.5 NotebookLM smoke v4 R1 | 15/17 strict PASS (88.2%) | `ai_platforms/notebooklm/dev/evidence/smoke_v4_results.md` |
| 07 Website prod | sdtm-pedia.pages.dev | Phase 7 closed |
| docs/jp 中間版 v0.5 | 6 件 xlsx / 4.6MB | `docs/jp/deliverable/20260430_iTMS_SDTM_進捗版_v0.5.zip` |

---

## 详细子板

详细历史进度、reviewer reports、commit 链等见对应 phase 子文件:

- 06 旁枝 → `.work/meta/worklog/phase06_deep_verification.md` + `.work/06_deep_verification/_progress.json`
- 07 旁枝 → `.work/meta/worklog/phase07_website.md` + `.work/07_website/phase{6,7,8,9}/PLAN.md`
- docs/jp → `.work/meta/worklog/phase_jp_delivery.md` + `docs/jp/_progress.json`
- Phase 6.5 双平台锁步 → `ai_platforms/SYNC_BOARD.md` + 各平台 `dev/evidence/_progress.json`
- refactor v1 → `.work/refactor_v1/PLAN.md` + `_progress.json` + `phase_meta_refactor.md`
