# 进度看板

> **唯一进度状态源**. 历史细节看 `.work/meta/worklog/INDEX.md`. 文件结构看 `.work/MANIFEST.md`. 一页纸入门看 `.work/AGENT_GUIDE.md`.
> 最后更新: 2026-08-06 (**study golden v2 扩容 DONE ✅** — 25→**48 计分题**, form 覆盖 18/21→**21/21**; 新增确定性 gold 唯一性 lint + 端到端"只有 gold 能得分"双向验证 48/48; **v1.1 题集已饱和判别力耗尽 (S2 下 100%), v2 新口径 80.49% → 87.50%**; 增益拆开看: 继承题 +11.94pt 但**新写题只有 +2.08pt**; 证据 `sdtm-rag/evidence/checkpoints/study_golden_v2.md` 含 5 条已知限制) · 此前同日 (**Plan B Phase 2 study 结构化直查 DONE ✅ 默认启用** — 三通道(+段交集)确定性直查, 零 LLM; study golden v1.1 25 计分题 **88.53% → 100.00%** 逐题零回归, 联邦复核同值 Δ0; 720→799 passed; 证据 `sdtm-rag/evidence/checkpoints/planb_phase2_study_lookup.md` 含 6 条已知限制) · 此前 (2026-08-04): **Plan B Phase 0+1 双库联邦路由 DONE ✅ 默认启用** — CDISC + study(st01) 联邦引擎 + LLM 判库; 三闸全绿 (路由三遍 178/181=98.3% fatal=0 稳定 181/181; 检索控制组 vs 联邦组三组逐题 Δ0); 答题供给切 AWS Bedrock; 证据 `sdtm-rag/evidence/checkpoints/planb_phase1_federation.md` · 此前 (2026-07-25): **SP7.1 查看器间距重排 DONE ✅** — 布局从"固定角宽塞节点"翻成"最小间距反推环容量" (`ringPack`), 总览扇区制/域钻取自动分列/explore 环半径随节点数放大; fit 上限 1.35 + 标签阈值 0.8; 18/18 layout 测试含 3 条新间距断言, pytest 零回归) · 此前 (2026-07-24): **SP7 KG 查看器 UX 重构 DONE ✅** — 力导向物理 → 确定性布局+补间, 用户抱怨"点一下到处飞"根治 (no-explode 实测 0px); 精密仪器视觉 (暗色优先/发丝网格/信号色/等宽码值/标线环); fit-to-content; overview 域码按需显隐; 源码拆 `sdtm-rag/viewer/{template,style,layout.mjs,app.js}` → build 内联 (勿手改 `kg_viewer.html`); 全分支 review READY; spec/plan `docs/superpowers/*2026-07-24-kg-viewer-ux*`) · 此前 (2026-07-21): **repo restructure v3 DONE ✅** — `branches/` 解散: 活跃代码仓提升为顶层 `sdtm-rag/` (深度 3→1: launchd plist/venv 重建/parent-chain 锚点 ×21 全迁, pytest 525 passed 零回归); 收官成果统一进 `milestones/` (06_deep_verification / 07_rag_kg 文档层 / jp_delivery [全量收编入 git] / ai_platforms / release / archive); 垃圾清理: 磁盘 ~300MB (缓存/备份/废弃状态) + tracked ~93MB git rm (06 .bak×15 + release_v1_3 backups + eval 旧 run + sharp 工具链) + git gc 146M→43M; web 构建改指 `milestones/release/v1.4` (本地 build 过); spec/plan `docs/superpowers/{specs,plans}/2026-07-21-repo-restructure-v3*`)
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
| **Phase 7** RAG + KG | 🟢 唯一活跃线 | KG SP1-6/AGG 全 DONE + 部署 launchd (api 8000/ui 8501/neo4j) + Chat UI; 答题主力已切 **AWS Bedrock** (`jp.anthropic.*` haiku/sonnet/opus, Anthropic 直连额度耗尽)。**Plan B Phase 0+1 双库联邦路由 DONE, 默认启用** (2026-08-04): CDISC + study(st01) 合成联邦引擎, LLM 判库, `/api/info` `federation: true`。**Plan B Phase 2 study 结构化直查 (S2) DONE, 默认启用** (2026-08-06): label/段/别名三通道 + 段交集, 确定性零 LLM。**CDISC 判据 section 粒度化 DONE** (2026-08-06): 18 题 gold 由路径级改 `路径#节$`, 基线 98.93% → **95.71%** — **判据变准非检索回归** (同一份检索结果换判据, 未改写的 122 题逐位 Δ0)。**study golden v2 扩容 DONE** (2026-08-06): 48 计分题 + 判据闸 (lint + 端到端双向验证), 尺子恢复判别力。检索基线: CDISC **81.07% (hybrid-only)** / **95.71% (加 S1, section 级判据; 旧路径级口径 98.93% 含约 3pt 水分, 两者不可直接比较)**; study **golden v2 (当前口径) 80.49% → 87.50% (加 S2)** — 旧 golden v1.1 的 **88.53% → 100.00%** ⚠ **该题集已饱和、判别力耗尽, 不再作为 study 侧改动的验收尺** (联邦前后逐题 Δ0)。**三版分数互不可比, 一版一把尺子** | **Plan B Phase 3 已裁定放弃** (勘察实证 Δrecall=0, 见 `planb_phase3_probe_not_worth_doing.md`)。**下一步**: v2 `--judge` 语义基线 (近义双卡判别题的答案正确性尚无任何测量) / v2 联邦复核 / q38 chapters 整文件单块 / 联邦答题 eval (需先修 `_FederatedAdapter.build_messages` 硬编码 corpus) / S1 对 VARIABLE_INDEX 改按 CT 码字面选块 (section 化暴露的 4 题真缺陷)。收口证据 `sdtm-rag/evidence/checkpoints/{study_golden_v2,planb_phase1_federation,planb_phase2_study_lookup}.md` + `cdisc_gold_section_granularity.md`; 服务局域网免密**含 study 库** (决策 D2) |
| **06 旁枝** Deep Verification | ✅ 完成 | P1-P7 全 PASS ★★ (coverage 99.02%, Issues 5-16 repaired, P7 content error 3.3%, RETROSPECTIVE.md 归档) | `milestones/06_deep_verification/RETROSPECTIVE.md` |
| **07 旁枝** Website | ✅ 完成 | Phase 6/7/8/9/10/11 全 closed; prod sdtm-pedia.pages.dev | — |
| **refactor v1/v2/v3** 项目重构 | ✅ 完成 | v1 段1-3 (2026-05-11) · v2 release 提顶层 (2026-05-11) · **v3 branches→milestones (2026-07-21)** | `.work/09_repo_refactor_v3/RETROSPECTIVE.md` |

**图例**: ✅ 完成 · 🟢 进行中 · ⏸ 待启动 · 🔴 阻塞

---

## 关键 milestone (近 30 天)

- 2026-08-06 (golden v2) — **study 题集 v2 扩容 DONE ★★ 尺子恢复判别力** (25→48 计分题, form 覆盖 21/21; 判据从人工约定变可执行闸: gold 唯一性 lint (AND+OR 双侧) + 端到端"只有 gold 能得分"48/48; **v2 口径 80.49%→87.50% (+7.01pt)**, 但拆开看继承题 +11.94pt 而**新写题只有 +2.08pt** — S2 增益几乎全部局限在旧题集恰好包含的题型上; 继承题逐题对历史 run Δ0 保证口径可对接; 823 passed) — evidence: `sdtm-rag/evidence/checkpoints/study_golden_v2.md` (含 5 条已知限制: 继承题 fact 存量债 1 题恒满分/7 题回声 · 子串判据看不出"两项互换"须走 `--judge` · 抽样总体应对齐变更集 · form_overview 仅 n=4 · lint 语义事故)
- 2026-08-06 (Plan B P2) — **study 结构化直查 S2 DONE ★★ 默认启用** (三通道 label/段/别名 + 段交集, 确定性零 LLM; golden v1.1 25 计分题 88.53%→**100.00%** (+11.47pt), 四题转命中且逐题零回归; 联邦复核 100% 逐题 Δ0; 720→799 tests; 生产冒烟 gold 命中) — evidence: `sdtm-rag/evidence/checkpoints/planb_phase2_study_lookup.md` (含 6 条已知限制: 1 题 gold 判别力≈0 / ②a fire 正确性 n=1 / cap 平台性与代价 / 别名表 n=1 / 终审模型降档 / 4 条 open follow-up)
- 2026-08-04 (Plan B P0+1) — **双库联邦路由 DONE ★★ 默认启用** (三闸全绿: 路由 181 题三遍 178/181=98.3% fatal=0 稳定性 181/181; 检索控制组 vs 联邦组三组逐题 Δ0; 前端下拉/徽章/判定行冒烟全过; 669→720 tests) — evidence: `sdtm-rag/evidence/checkpoints/planb_phase1_federation.md`
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
