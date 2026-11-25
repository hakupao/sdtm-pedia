# .work/AGENT_GUIDE.md — Agent 进入指引 (一页纸)

> 创建: 2026-05-06 (refactor v1 段 1 产物)
> 维护节奏: 段 2 (worklog 拆分) + 段 3 (06 旁枝迁移) 完成后回头更新对应行
> 优先级: **新 session 第 1 个读** — 比 MANIFEST.md 还早
> 2026-11-25 布局重组: `milestones/` 解散 → `releases/` + `archive/{deep_verification,ai_platforms,jp_delivery,legacy}/`; 新旧对照见 `docs/PATH_MAP.md`

## 项目一句话

SDTM 知识库, 从 CDISC PDF + xlsx 抽取. 旁枝均已收口 (字面级深审 ✅ / 双 AI 平台部署 ✅CLOSED 2026-06-15 / 静态站发布 ✅ / 日文 iTMS 納品 ✅CLOSED 2026-06-15); KB 仍会持续修订. **RAG 问答服务已拆到独立的公开仓 `hakupao/sdtm-rag`** (以 submodule 引用本仓 KB).

## 找东西去哪

| 想找 | 看这里 |
|------|--------|
| **当前进度状态** (各 phase 哪个 in-flight 哪个 done) | `docs/PROGRESS.md` (唯一状态板) |
| **某 phase 程序化进度** (round/batch/atom 数字) | `.work/0N_xxx/_progress.json` 或 `archive/<track>/_progress.json` |
| **各文件做啥用 + 变更链** | `.work/MANIFEST.md` |
| **历史工作日志** (谁啥时候做了啥) | `.work/meta/worklog/INDEX.md` → `phase*.md` |
| **跨 session 硬规则** (规则 A/B/C/D + PASS 四条 + CLAUDE.md 写作规则) | 项目根 `CLAUDE.md` + `.work/meta/retrospective.md` § 4 |
| **公开 issue 清单** | `.work/03_verification/issues_found.md` |
| **PDF 原始源** | `source/SDTMIG v3.4 (no header footer).pdf` + xlsx |
| **英文 KB 主成果** | `knowledge_base/` (chapters/ + domains/ + model/ + terminology/ + INDEX/ROUTING/VARIABLE_INDEX) |
| **静态站源码 + 部署产物** | `web/` (Astro; prod https://sdtm-pedia.pages.dev; 内容读 `releases/v1.4/`) |
| **发布包 v1.0-v1.4** (冻结) | `releases/v1.{0-4}/` |
| **双 AI 平台部署** (CLOSED 冻结) | `archive/ai_platforms/SYNC_BOARD.md` + `retrospectives/` (历史只读, 不再更新) |
| **历史归档** (不再维护) | `archive/legacy/` |

## 各 phase 入口表

| Phase | 入口 PLAN | 状态 |
|-------|-----------|------|
| 00 Planning | `.work/00_planning/` | closed |
| 01 Generation | `.work/01_generation/` | closed |
| 02 Indexing | `.work/02_indexing/page_index.json` | closed |
| 03 Verification | `.work/03_verification/plan.md` | closed (Issue 1-16 全修复; 深层缺口经 06 回流补齐) |
| 04 Optimization | `.work/04_optimization/retrieval_optimization.md` | closed (P0-P2; P3 并入 Phase 7) |
| 05 RAG/KG 设计 | (随 RAG 迁出) | 见 RAG 仓 |
| 06 Deep Verification | `archive/deep_verification/PLAN.md` | ✅ COMPLETE (P1-P7, coverage 99.02%, 2026-05-12) |
| 6.5 AI Platforms | `archive/ai_platforms/SYNC_BOARD.md` | ✅ **CLOSED 冻结** 2026-06-15 (终态 v1.4; 以后不再更新) |
| 7 RAG+KG 实现 | 独立公开仓 `hakupao/sdtm-rag` | ↗ 已拆仓 (2026-11); 拆仓过程记录在 sdtm-rag 仓 |
| 7 Release | `.work/07_release_v1_4/PLAN.md` (latest) + `.work/07_release{,_v1_1,_v1_2,_v1_3,_v1_4}/` | latest v1.4 cut 2026-05-22 (tag `v1.4-company-release`); v1.0-v1.3 closed |
| 7 Website | `.work/07_website/phase{6,7,8}/` | closed (prod 已发布) |
| iTMS 日本納品旁枝 | `archive/jp_delivery/PLAN.md` | ✅ **CLOSED 冻结** 2026-06-15 (停于 P0 2/4 + 01 v1.1-draft; 以后不再更新) |
| **本次重构 v1** | `.work/refactor_v1/PLAN.md` | ✅ 全 closed 2026-05-11 (branches/ 迁移完成) |

## 路由词速查

用户在 session 说这些词, 主 session 应该路由:

- **"KB 更新"** / **"网站更新"** → 见 CLAUDE.md「跨会话路由词」段
- (06 深审已收官; 旧路由词 batch / reconciler / P2 kickoff 文件在 `archive/deep_verification/multi_session/`, 仅历史)
- **"收尾"/"wrap up"/"提交收尾"** → 见 CLAUDE.md "Session Wrap-up" 段
- **"refactor v1 执行段 N"** → `.work/refactor_v1/PLAN.md` § 段 N 详细步骤

## 不要做的

- 不要再推进 **archive/ai_platforms (多平台部署)** 或 **archive/jp_delivery (日语納品)** — 两线已 CLOSED 冻结 2026-06-15, 以后不再更新, 仅历史只读
- 不要直接读 `archive/legacy/` 内容做主任务 — 那是历史
- 不要 in-flight 写 06 跨 session 共享文件 (pdf_atoms.jsonl / audit_matrix / _progress.json) — 见 `multi_session/MULTI_SESSION_PROTOCOL.md` 锁规则
- 不要在 CLAUDE.md 写 round/batch/version 状态 — 见 CLAUDE.md "写作规则"
