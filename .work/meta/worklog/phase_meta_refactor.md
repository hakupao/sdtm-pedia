# Phase Meta — 项目重构 v1 工作日志

> `.work/refactor_v1/` 配下的段 1/2/3 close entries (Chain REFACTOR-v1).
> 段 3 完成后, 本文件可选择性归档到 `historical_*.md` 或保留作为 retro 索引.

> **新 entry** append 到本文件, 标题格式 `## YYYY-MM-DD refactor v1 段 N <verb>`.

---

## 2026-05-06 refactor v1 段 2 CLOSED

- **Scope**: A 余 (.bak 整理 85→1) + B (MANIFEST 360→205 + worklog 2498→6 文件 + PROGRESS 339→74) + B-14 (CLAUDE.md Chain B 更新, 三套索引职责段)
- **Trigger 满足**: 06 round 04 CLOSED (commit `7d8db63`+`bb04c4b` 2026-05-06) + round 05 未 kickoff + git clean
- **Evidence**: `.work/refactor_v1/evidence/checkpoints/段2_完成报告.md`
- **Rule A audit**: worklog split 0% drift (2498 → 2498 lines across 5 phase 文件)
- **Actual hours**: ~45 min (vs estimate 4h, 快是 .bak 机械操作 + worklog 用 python 一次性切)
- **Triggers next**: 段 3 (路径迁移 → branches/) 等 P2 B-03c 整个 cycle 收官 (现 36/114 = 31.6%)

## 2026-05-06 refactor v1 段 1 CLOSED

- **Scope**: D (project_knowledge_base 归档) + E (AGENT_GUIDE) + A 零冲突部分 (顶层清污)
- **Commit**: `25fadac refactor v1 段 1 CLOSED — 顶层清污 + AGENT_GUIDE + project_knowledge_base 归档`
- **Evidence**: `.work/refactor_v1/evidence/checkpoints/段1_完成报告.md`
- **Actual hours**: ~30 min (vs estimate 2h, 因决策走默认 + mv 大量是 ignored 目录)
- **Triggers next**: 段 2 在 06 round 04 close 后启动

## 2026-05-11 refactor v1 段 3 CLOSED ★ 项目重构 v1 収官

- **触发**: B-03c 収官 COMPLETE (2026-05-11) + Bojiang 说 "执行段 3"
- **实际用时**: ~1.5h
- **执行摘要**:
  - C-2 全量备份 (50MB → refactor_v1/evidence/checkpoints/06_pre_C/)
  - C-3/4 `mkdir branches/` + `git mv .work/06_deep_verification branches/06_deep_verification`
  - C-8/9 `git mv docs/jp branches/jp_delivery` + 内部路径更新
  - C-5/6/7 PLAN.md chain F + PROTOCOL.md + 85 multi_session/*.md 批量 sed
  - Table 4 subagent_prompts/ 批量 sed
  - C-10-12 CLAUDE.md 路由词 + Key Paths 全量更新
  - C-13 MANIFEST.md 结构指针更新
  - C-14 AGENT_GUIDE.md 入口路径 + 段3后注记清理
  - C-15 worklog/phase06_deep_verification.md → 1 行指针
  - Table 8/9 PROGRESS.md + .gitignore 路径更新
  - METHODOLOGY.md + README.md/CN + release METHODOLOGY 3语 更新
  - phase_jp_delivery.md 活跃引用更新
  - C-16/17/18 dry-run: 0 kickoff 文件残留旧路径; 主路由文件新路径 ≥4 refs ✅
  - R-1 RETROSPECTIVE.md 三段齐备; R-3 _progress.json overall_status=CLOSED
- **产物**:
  - `branches/06_deep_verification/` (完整迁移)
  - `branches/jp_delivery/` (完整迁移)
  - `.work/refactor_v1/RETROSPECTIVE.md`
  - `evidence/checkpoints/段3_完成报告.md` (规则 A PASS)
- **规则 C**: RETROSPECTIVE.md 三段齐备 ✅

---

## 2026-07-21 repo restructure v3 — branches/ 解散 + sdtm-rag 提顶层 + milestones/ 收成果 DONE ✅

- **触发**: 用户判定 branches/ 语义错误 (实为阶段性成果非 git branch) + 开发垃圾累积, 要求大改结构方便后续开发维护。走完整 brainstorm→spec→plan→executing-plans (13 task 六段时序)。
- **决策 (D1-D5 用户确认)**: 活跃 vs 成果二分 / .work 不动 archive 并入 / release 进 milestones 同步改 web / tracked 冗余四类全删 / jp_delivery 全量收编入 git。
- **新布局**: 顶层 = knowledge_base + **sdtm-rag** (★活跃, 深度 3→1) + web + **milestones/** (06_deep_verification / 07_rag_kg 文档层 / jp_delivery / ai_platforms / release / archive) + source + docs + .work + tools。`branches/` 消失, 顶层可见目录 14→9 (含文件)。
- **清理**: 磁盘 ~300MB (mypy_cache 86M / chroma_backup 93M / .omx 15M / web dist ~74M / 根 node_modules 17M / 缓存杂项) + tracked ~93MB git rm (06 .bak×15 ~40M + 07_release_v1_3/backups 26M + eval ≤6/20 旧 run ~9.6M 逐文件枚举 + sharp package.json) + **git gc 146M→42.6M** (首次 repack)。
- **迁移工程**: bootout api/ui → jp 原位收编 (74 文件入 git) → git mv 全部 → venv 重建 (uv sync) → plist ×2 改写 → bootstrap; parent-chain 深度锚 ×21 修 (**含 plan 遗漏执行期抓住的 tests ×11 + smoke a/c ×2**); web content.config/build-bundles/tools/build_release/git-hooks/jp build_zip 全指 milestones。
- **验证矩阵全 PASS**: 双向 grep 0 残留 (历史白名单外) / 服务四联 (api·ui·neo4j·/api/ask 真答 15 sources) / reconcile_meta 8/8 锚 / **pytest 525 passed** (> 迁移前 521 — 旧布局下 4 测试因锚指空在静默 skip, 本次连带治愈) / web 本地 build 过 + push 触发 CF / 独立 dry-run agent 走查。
- **文档**: 活文档 78 处路径迁移 + README×2 结构树重写 + MANIFEST Chain 07_RAG 改指顶层 sdtm-rag + 布局变更总注记; **PROGRESS.md 重切** (117→64 行, 14.4K 单行巨段→550 字符, 30 天外 milestone 剪除); memory ×2 更新; 历史文档 (worklog/closed checkpoint/superpowers 已执行 spec·plan/release 内部) 旧路径故意保留。
- **销旧账**: 08_repo_refactor_v2 `awaiting_user_ack` (2026-05-11 起挂) → closed (v2 遗留 smoke 被 v3 Task 9/12 实测覆盖)。
- **证据**: `.work/09_repo_refactor_v3/evidence/step_{disk_cleanup,services_smoke,verification_matrix,dryrun_agent}.md` + `RETROSPECTIVE.md` (Rule C 三段)。spec/plan `docs/superpowers/{specs,plans}/2026-07-21-repo-restructure-v3*`。
