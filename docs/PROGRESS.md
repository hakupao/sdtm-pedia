# 进度看板

> **唯一进度状态源**. 历史细节看 `.work/meta/worklog/INDEX.md`. 文件结构看 `.work/MANIFEST.md`. 一页纸入门看 `.work/AGENT_GUIDE.md`.
> 最后更新: 2026-11-26 (Tier B T2 60 批完成; 全局核查 + 用户裁定 U1-U4)

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
| **Phase 6.5** AI 平台部署 | ⏸ CLOSED 冻结 | 多平台部署线收口 2026-06-15 (用户决策, 以后不再更新); 终态 = Release v1.4 (tag `v1.4-company-release`) + 4 平台 signed-off + Gemini MAINTAINED_NO_SANITY_TEST | — (v1.5 候选全部放弃; 历史只读 releases/ + archive/ai_platforms/retrospectives/) |
| **Phase 7** RAG + KG | ↗ 已拆仓 | 独立公开仓 `hakupao/sdtm-rag` | — |
| **06 旁枝** Deep Verification | ✅ 完成 | P1-P7 全 PASS ★★ (coverage 99.02%, Issues 5-16 repaired, P7 content error 3.3%, RETROSPECTIVE.md 归档) | `archive/deep_verification/RETROSPECTIVE.md` |
| **07 旁枝** Website | ✅ 完成 | Phase 6/7/8/9/10/11 全 closed; prod sdtm-pedia.pages.dev | — |
| **10 旁枝** Tier B 内容补修 | 🔄 T2 完成 (60/60 批本地 commit, 未 push) | 全局核查 3 份 + 用户裁定 U1-U4 | T2 后扫描批 (S-*) → T3 → T4 → push; `.work/10_tier_b_repair/HANDOFF.md` |
| **refactor v1/v2/v3** 项目重构 | ✅ 完成 | v1 段1-3 (2026-05-11) · v2 release 提顶层 (2026-05-11) · v3 branches→milestones (2026-07-21) · **R2 milestones→releases+archive (2026-11-25)** | `docs/PATH_MAP.md` |

**图例**: ✅ 完成 · 🟢 进行中 · ⏸ 待启动 · 🔴 阻塞

---

## RAG+KG 问答服务

RAG 问答服务已拆到独立的公开仓 [hakupao/sdtm-rag](https://github.com/hakupao/sdtm-rag) (2026-11), 其进度/milestone/证据在该仓维护; 拆仓过程记录在 sdtm-rag 仓。

---

## 数据指标速查

| 指标 | 值 | 来源 |
|------|----|----|
| 知识库 md 文件数 | 293 | `knowledge_base/` |
| 覆盖 domain 数 | 63 | 同上 |
| 06 累计 md_atoms | **10,435** ★★ | `archive/deep_verification/md_atoms.jsonl` (P2 B-03c 収官 COMPLETE) |
| 06 P2 B-03c 进度 | **143/143 = 100%** ★★ | P2 B-03c CLOSED 2026-05-11 |
| 06 P2 file coverage | **141/141 = 100%** ★★ | P2 B-03c CLOSED 2026-05-11 |
| 06 P2 domain coverage | **63/63 = 100%** ★★ | P2 B-03c CLOSED 2026-05-11 |
| 06 累计 pdf_atoms | 12487 | P1 CLOSURE (2026-04-29) |
| Phase 6.5 Claude v2.6 | 24/24 A/B PASS, 0 衰减, capacity 77% | `archive/ai_platforms/claude_projects/dev/test_results.md` |
| Phase 6.5 NotebookLM smoke v4 R1 | 15/17 strict PASS (88.2%) | `archive/ai_platforms/notebooklm/dev/evidence/smoke_v4_results.md` |
| 07 Website prod | sdtm-pedia.pages.dev | Phase 7 closed |
---

## 详细子板

详细历史进度、reviewer reports、commit 链等见对应 phase 子文件:

- 06 旁枝 → `.work/meta/worklog/phase06_deep_verification.md` + `archive/deep_verification/_progress.json`
- 07 旁枝 → `.work/meta/worklog/phase07_website.md` + `.work/07_website/phase{6,7,8,9}/PLAN.md`
- Phase 6.5 多平台部署 (CLOSED 冻结) → `archive/ai_platforms/SYNC_BOARD.md` + `retrospectives/` + `releases/v1.{0-4}/` (只读)
- refactor v1 → `.work/refactor_v1/PLAN.md` + `_progress.json` + `phase_meta_refactor.md`
