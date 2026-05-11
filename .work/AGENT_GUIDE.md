# .work/AGENT_GUIDE.md — Agent 进入指引 (一页纸)

> 创建: 2026-05-06 (refactor v1 段 1 产物)
> 维护节奏: 段 2 (worklog 拆分) + 段 3 (06 旁枝迁移) 完成后回头更新对应行
> 优先级: **新 session 第 1 个读** — 比 MANIFEST.md 还早

## 项目一句话

SDTM 知识库, 从 CDISC PDF + xlsx 抽取, 多旁枝 (字面级深审 / 双 AI 平台部署 / 静态站发布 / 日文 iTMS 納品)。

## 找东西去哪

| 想找 | 看这里 |
|------|--------|
| **当前进度状态** (各 phase 哪个 in-flight 哪个 done) | `docs/PROGRESS.md` (段 2 后会变成唯一状态板) |
| **某 phase 程序化进度** (round/batch/atom 数字) | `.work/0N_xxx/_progress.json` 或 `branches/0N_xxx/_progress.json` (段 3 后) |
| **各文件做啥用 + 变更链** | `.work/MANIFEST.md` |
| **历史工作日志** (谁啥时候做了啥) | `.work/meta/worklog.md` (段 2 后拆为 `.work/meta/worklog/phase*.md`) |
| **跨 session 硬规则** (规则 A/B/C/D + PASS 四条 + CLAUDE.md 写作规则) | 项目根 `CLAUDE.md` + `.work/meta/retrospective.md` § 4 |
| **公开 issue 清单** | `.work/03_verification/issues_found.md` |
| **PDF 原始源** | `source/SDTMIG v3.4 (no header footer).pdf` + xlsx |
| **英文 KB 主成果** | `knowledge_base/` (chapters/ + domains/ + model/ + terminology/ + INDEX/ROUTING/VARIABLE_INDEX) |
| **静态站源码 + 部署产物** | `web/` (Astro; prod https://sdtm-pedia.pages.dev) |
| **双 AI 平台部署** | `ai_platforms/SYNC_BOARD.md` (锁步看板) + 各平台 `dev/_progress.json` |
| **历史归档** (不再维护) | `archive/` |

## 各 phase 入口表

| Phase | 入口 PLAN | 状态 |
|-------|-----------|------|
| 00 Planning | `.work/00_planning/` | closed |
| 01 Generation | `.work/01_generation/` | closed |
| 02 Indexing | `.work/02_indexing/page_index.json` | closed |
| 03 Verification | `.work/03_verification/plan.md` | closed (issues_found.md 有 open issues, 走 06 字面级深审回流) |
| 04 Optimization | `.work/04_optimization/retrieval_optimization.md` | TODO |
| 05 RAG/KG | `.work/05_rag_kg/session_2026-04-16_design.md` | **搁置** (仅设计 session, 未启动) |
| 06 Deep Verification | `branches/06_deep_verification/PLAN.md` | 🟢 P3 ✅ COMPLETE 2026-05-11; P4a 待启动 |
| 6.5 AI Platforms | `ai_platforms/SYNC_BOARD.md` | active (双平台锁步) |
| 7 Release | `.work/07_release/PLAN.md` | closed (v1.0 cut) |
| 7 Website | `.work/07_website/phase{6,7,8}/` | closed (prod 已发布) |
| iTMS 日本納品旁枝 | `branches/jp_delivery/PLAN.md` | active |
| **本次重构 v1** | `.work/refactor_v1/PLAN.md` | ✅ 全 closed 2026-05-11 (branches/ 迁移完成) |

## 路由词速查 (06 multi-session)

用户在 session 说这些词, 主 session 应该路由:

- **"batch NN 开始任务"** → `branches/06_deep_verification/multi_session/batch_NN_kickoff.md` 
- **"reconciler 开始任务"** → `branches/06_deep_verification/multi_session/reconciler_kickoff_round_NN.md`
- **"P2 bulk B-03c round NN 自治连跑"** → `branches/06_deep_verification/multi_session/P2_B-03c_round_NN_kickoff.md`
- **"收尾"/"wrap up"/"提交收尾"** → 见 CLAUDE.md "Session Wrap-up" 段
- **"refactor v1 执行段 N"** → `.work/refactor_v1/PLAN.md` § 段 N 详细步骤

## 不要做的

- 不要直接读 `archive/` 内容做主任务 — 那是历史
- 不要在 `.work/05_rag_kg/` 下新建文件 — 该 phase 搁置中
- 不要 in-flight 写 06 跨 session 共享文件 (pdf_atoms.jsonl / audit_matrix / _progress.json) — 见 `multi_session/MULTI_SESSION_PROTOCOL.md` 锁规则
- 不要在 CLAUDE.md 写 round/batch/version 状态 — 见 CLAUDE.md "写作规则"
