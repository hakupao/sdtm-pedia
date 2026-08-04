# 进度看板

> **唯一进度状态源**. 历史细节看 `.work/meta/worklog/INDEX.md`. 文件结构看 `.work/MANIFEST.md`. 一页纸入门看 `.work/AGENT_GUIDE.md`.
> 最后更新: 2026-07-25 (**SP7.1 查看器间距重排 DONE ✅** — 布局从"固定角宽塞节点"翻成"最小间距反推环容量" (`ringPack`), 总览扇区制/域钻取自动分列/explore 环半径随节点数放大; fit 上限 1.35 + 标签阈值 0.8; 18/18 layout 测试含 3 条新间距断言, pytest 零回归) · 此前 (2026-07-24): **SP7 KG 查看器 UX 重构 DONE ✅** — 力导向物理 → 确定性布局+补间, 用户抱怨"点一下到处飞"根治 (no-explode 实测 0px); 精密仪器视觉 (暗色优先/发丝网格/信号色/等宽码值/标线环); fit-to-content; overview 域码按需显隐; 源码拆 `sdtm-rag/viewer/{template,style,layout.mjs,app.js}` → build 内联 (勿手改 `kg_viewer.html`); 全分支 review READY; spec/plan `docs/superpowers/*2026-07-24-kg-viewer-ux*`) · 此前 (2026-07-21): **repo restructure v3 DONE ✅** — `branches/` 解散: 活跃代码仓提升为顶层 `sdtm-rag/` (深度 3→1: launchd plist/venv 重建/parent-chain 锚点 ×21 全迁, pytest 525 passed 零回归); 收官成果统一进 `milestones/` (06_deep_verification / 07_rag_kg 文档层 / jp_delivery [全量收编入 git] / ai_platforms / release / archive); 垃圾清理: 磁盘 ~300MB (缓存/备份/废弃状态) + tracked ~93MB git rm (06 .bak×15 + release_v1_3 backups + eval 旧 run + sharp 工具链) + git gc 146M→43M; web 构建改指 `milestones/release/v1.4` (本地 build 过); spec/plan `docs/superpowers/{specs,plans}/2026-07-21-repo-restructure-v3*`)
> 此前各阶段收口细节 (SP1-SP6 / AGG / 部署 / Chat UI 等): 见 `.work/meta/worklog/phase_07_rag_kg.md` 对应收口记录 (本行原 84K 单行巨段已于 restructure v3 剪除, 全文在 git 历史 `816c4a5^` 前的版本可查)

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
| **Phase 6.5** AI 平台部署 | ⏸ CLOSED 冻结 | 多平台部署线收口 2026-06-15 (用户决策, 以后不再更新); 终态 = Release v1.4 (tag `v1.4-company-release`) + 4 平台 signed-off + Gemini MAINTAINED_NO_SANITY_TEST | — (v1.5 候选全部放弃; 历史只读 milestones/release/ + milestones/ai_platforms/retrospectives/) |
| **Phase 7** RAG + KG | 🟢 唯一活跃线 | KG SP1-6/AGG 全 DONE + 部署 launchd (api 8000/ui 8501/neo4j) + Chat UI; 主力 DeepSeek-v4-pro。**study 确定性轨 (st01) 已收官**: golden v1.1 真实基线 **88.5%**; CDISC **81.1%** (2026-08-04 重测, 旧记录 99%/100% 因题集与索引缺陷作废) | **下一步 Plan B 联邦路由** — 交接见 `.work/meta/study_rag_handoff_2026-08-04.md`; 服务认证已关 (局域网免密); 细节 `.work/meta/worklog/phase_07_rag_kg.md` |
| **06 旁枝** Deep Verification | ✅ 完成 | P1-P7 全 PASS ★★ (coverage 99.02%, Issues 5-16 repaired, P7 content error 3.3%, RETROSPECTIVE.md 归档) | `milestones/06_deep_verification/RETROSPECTIVE.md` |
| **07 旁枝** Website | ✅ 完成 | Phase 6/7/8/9/10/11 全 closed; prod sdtm-pedia.pages.dev | — |
| **refactor v1/v2/v3** 项目重构 | ✅ 完成 | v1 段1-3 (2026-05-11) · v2 release 提顶层 (2026-05-11) · **v3 branches→milestones (2026-07-21)** | `.work/09_repo_refactor_v3/RETROSPECTIVE.md` |

**图例**: ✅ 完成 · 🟢 进行中 · ⏸ 待启动 · 🔴 阻塞

---

## 关键 milestone (近 30 天)

- 2026-07-25 (SP7.1) — **查看器间距重排 DONE ★** (固定角宽 → 最小间距反推环容量; 总览扇区制/域钻取自动分列/fit 上限 1.35/标签阈值 0.8; 新增 3 条间距断言当场抓到"比例留白在极坐标里是错的"缺陷) — 细节: `.work/meta/worklog/phase_07_rag_kg.md`
- 2026-07-24 (SP7) — **KG 查看器 UX 重构 DONE ★★** (力导向物理 → 确定性布局+补间; "到处飞"根治 no-explode 实测 0px; 精密仪器视觉; 源码 `sdtm-rag/viewer/*` build 内联; 全分支 review READY) — evidence: `sdtm-rag/evidence/checkpoints/kg_viewer_ux_redesign.md` · retro: `docs/superpowers/2026-07-24-sp7-kg-viewer-ux-RETROSPECTIVE.md`
- 2026-07-21 — **repo restructure v3 DONE ★★** (branches/ 解散 → sdtm-rag 顶层 + milestones/; ~550MB 清理; 525 passed; spec/plan `docs/superpowers/*2026-07-21-repo-restructure-v3*`)
- 2026-07-10 (SP6) — **隐性关系挖掘 + 网状富节点查看器 DONE ★★** (30 advisory 边 + 网状查看器; 确定性反捏造闸 > 软化 LLM 裁判) — 细节: `.work/meta/worklog/phase_07_rag_kg.md`
- 2026-07-09 (SP4+SP5) — **Neo4j 探索层 + 图增强校验器 DONE ★★ — KG 重启全线收官** (SP1-5+AGG 全 DONE; 路由词无剩余单元) — 细节: worklog 同上
- 2026-07-07 (AGG) — **aggregate 独立通道 DONE ★ 默认 ON** (ds e2e Δ+41.7pp; 诚实 fire-rate 口径) — 细节: worklog 同上

→ **完整时间线**: `.work/meta/worklog/INDEX.md` → 各 phase 文件

---

## 数据指标速查

| 指标 | 值 | 来源 |
|------|----|----|
| 知识库 md 文件数 | 293 | `knowledge_base/` |
| 覆盖 domain 数 | 63 | 同上 |
| 06 累计 md_atoms | **10,435** ★★ | `milestones/06_deep_verification/md_atoms.jsonl` (P2 B-03c 収官 COMPLETE) |
| 06 P2 B-03c 进度 | **143/143 = 100%** ★★ | P2 B-03c CLOSED 2026-05-11 |
| 06 P2 file coverage | **141/141 = 100%** ★★ | P2 B-03c CLOSED 2026-05-11 |
| 06 P2 domain coverage | **63/63 = 100%** ★★ | P2 B-03c CLOSED 2026-05-11 |
| 06 累计 pdf_atoms | 12487 | P1 CLOSURE (2026-04-29) |
| Phase 6.5 Claude v2.6 | 24/24 A/B PASS, 0 衰减, capacity 77% | `milestones/ai_platforms/claude_projects/dev/test_results.md` |
| Phase 6.5 NotebookLM smoke v4 R1 | 15/17 strict PASS (88.2%) | `milestones/ai_platforms/notebooklm/dev/evidence/smoke_v4_results.md` |
| 07 Website prod | sdtm-pedia.pages.dev | Phase 7 closed |
---

## 详细子板

详细历史进度、reviewer reports、commit 链等见对应 phase 子文件:

- 06 旁枝 → `.work/meta/worklog/phase06_deep_verification.md` + `milestones/06_deep_verification/_progress.json`
- 07 旁枝 → `.work/meta/worklog/phase07_website.md` + `.work/07_website/phase{6,7,8,9}/PLAN.md`
- Phase 6.5 多平台部署 (CLOSED 冻结) → `milestones/ai_platforms/SYNC_BOARD.md` + `retrospectives/` + `milestones/release/v1.{0-4}/` (只读)
- refactor v1 → `.work/refactor_v1/PLAN.md` + `_progress.json` + `phase_meta_refactor.md`
