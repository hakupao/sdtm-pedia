# 进度看板

> **唯一进度状态源**. 历史细节看 `.work/meta/worklog/INDEX.md`. 文件结构看 `.work/MANIFEST.md`. 一页纸入门看 `.work/AGENT_GUIDE.md`.
> 最后更新: 2026-05-06 (P2 B-03c round 06 CLOSED — ★ 跨 50% domain coverage milestone)

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
| **06 旁枝** Deep Verification | 🟢 进行中 | P2 B-03c round 06 CLOSED 2026-05-06 (★ 跨 50% domain coverage milestone, 33/63 domains; Option C defer PC); round 07 pending Bojiang ack scope (default PC solo) | 详见 `.work/06_deep_verification/_progress.json` |
| **07 旁枝** Website | ✅ 完成 | Phase 6/7/8/9/10/11 全 closed; prod sdtm-pedia.pages.dev | — |
| **docs/jp** iTMS 納品 | 🟢 进行中 | Phase 1 P0 中間版 v0.5 已提出 2026-04-30 | 残 02/03 + 05/06/99 中文列充填 (Phase 2-3, 2026-05 中下旬) |
| **refactor v1** 项目重构 | 🟢 进行中 (段 2) | 段 1 closed 2026-05-06; 段 2 进行中 | 段 3 (路径迁移) 待 B-03c cycle 收官 |

**图例**: ✅ 完成 · 🟢 进行中 · ⏸ 待启动 · 🔴 阻塞

---

## 关键 milestone (近 30 天)

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
| 06 累计 md_atoms | 8122 | `.work/06_deep_verification/_progress.json` `b_03c_round_06_details.cumulative_post_round_06.md_atoms_jsonl_total` |
| 06 P2 B-03c 进度 | 58/114 = 50.9% | 同上 `b_03c_progress_pct` |
| 06 P2 file coverage | 81/141 = 57.4% | 同上 `file_coverage_pct` |
| 06 P2 domain coverage | 33/63 = 52.4% ★ | 同上 `domain_coverage_pct` (post drift-fix from STALE 23) |
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
