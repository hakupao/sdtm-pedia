# SDTM Knowledge Base Project

## Project Overview

SDTM (Study Data Tabulation Model) knowledge base built from CDISC standard source files (PDF + xlsx).
293 Markdown files covering 63 domains, terminology, model concepts, and implementation guide chapters.

## CLAUDE.md 写作规则 (写入前必过闸)

CLAUDE.md 是**长效约束清单**, 不是工作日志, 不是状态看板. 写入前先过三道闸:

**可以写 (durable, 6+ 月稳定)**:
- 启动 / 收尾 / 约定 / 锁步 gate / 章节链 (Chain) 等流程规则
- 跨 session 必守的硬约束 (规则 A/B/C/D, PASS 四条)
- Key Paths 一行指针: `名字 → 路径 — 一句话用途` (单元格 ≤ 80 字符)

**不要写 (属 worklog / progress.json / handoff)**:
- 任何 round / batch / version 进度数字 (atoms / pages / batches / cut #N)
- 当前 in-flight 状态 ("round N closing in flight", "batch M 即将派发")
- 历史归档清单 (v1.1-v1.7 archive 路径) — 归档目录自身即来源
- 多子句长段落 / 表格单元格 > 100 字符 — 拆专门 doc, 这里只留指针
- 已在 MANIFEST.md / worklog.md 写过的内容 (避免重复维护)

**写完后必须及时清理 (TTL 触发条件)**:
- 带日期 / round N / version vX 的句子, 该阶段关闭立即删除或迁移到 `.work/meta/worklog.md`
- 收尾流程必须扫一遍 CLAUDE.md, 把过期状态描述剪掉 (新增到下方 Session Wrap-up checklist)
- Key Paths 条目 ≥ 2 个月没动过, 重审一次: 在用就压短描述, 不在用就删

**红线**:
- CLAUDE.md 总行数硬上限 **150 行** (含空行); 超出 = 该剪了
- 单章节 ≥ 30 行 = 该拆 doc, CLAUDE.md 只留入口指针
- 表格单行 > 200 字符 = 该拆出去

## Session Startup

Every new session, **before doing any work**, read these files in order:

1. `.work/MANIFEST.md` — file layout, change chains, quick reference table
2. `.work/meta/worklog.md` — work log with recovery guide
3. `.work/03_verification/issues_found.md` — open issues
4. `.work/meta/retrospective.md` § 4 — four prevention rules (must follow when doing any AI-assisted content work)

Then summarize to the user: current status, open issues, and suggested next step.

## 06 Deep Verification (旁枝)

状态 / round 进度 / drift cal 历史 / Rule D roster / 累计 metric / archive 路径 → `.work/06_deep_verification/_progress.json`.
Multi-session 派发: 当前 round kickoff 文件在 `.work/06_deep_verification/multi_session/batch_NN_kickoff.md` + `reconciler_kickoff_roundN.md`. 路由词 `batch NN 开始任务` / `reconciler 开始任务` 对应当前 round 的 kickoff 文件 (路由名遵 round 内对应 batch 号; 找不到对应 batch_NN_kickoff.md 时停下问).
Master 协议 `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md`. 入口 PLAN `.work/06_deep_verification/PLAN.md`.

## Change Chains

This project uses a change-chain system to prevent forgotten updates.
When modifying any `.work/` file, check its `<!-- chain: X -->` header for related files that must also be updated.
Full chain definitions are in `.work/MANIFEST.md`.

## Key Paths

| What | Where |
|------|-------|
| Knowledge base output | `knowledge_base/` |
| Source files (PDF/xlsx) | `source/` |
| Work artifacts | `.work/` (phase-numbered dirs) |
| Project docs | `docs/` |
| Page index (authoritative) | `.work/02_indexing/page_index.json` |
| Verification plan | `.work/03_verification/plan.md` |
| Retrospective & rules | `.work/meta/retrospective.md` |
| Follow-up risk plan | `.work/03_verification/followup_plan.md` |
| TODO (Phase 6) | `.work/04_optimization/retrieval_optimization.md` |
| Phase 7 设计文档 | `docs/DESIGN_RAG_KG.md` |
| Phase 7 session 记录 | `.work/05_rag_kg/session_2026-04-16_design.md` |
| 06 Deep Verification 入口 | `.work/06_deep_verification/PLAN.md` (字面级 PDF→KB 深审; 详细见 §06 Deep Verification 段) |
| 06 Deep Verification schema | `.work/06_deep_verification/schema/{atom,ledger}_schema.json` (frozen JSON Schema 2020-12) |
| Phase 6.5 AI 平台部署 | `ai_platforms/` (总览 + 三平台子目录) |
| Phase 6.5 范本 + 锁步看板 | `ai_platforms/_template/README.md` + `ai_platforms/SYNC_BOARD.md` (双平台锁步 gate) |
| Phase 6.5 smoke 题库 + retro | `ai_platforms/SMOKE_V4.md` + `ai_platforms/retrospectives/` |
| Phase 6.5 ChatGPT + Gemini | `ai_platforms/{chatgpt_gpt,gemini_gems}/` (current/ + dev/ + docs/) |
| Phase 6.5 NotebookLM | `ai_platforms/notebooklm/` (current/ + docs/RETROSPECTIVE.md) |
| Phase 6.5 Claude Projects | `ai_platforms/claude_projects/` (current/UPLOAD_TUTORIAL.md + docs/) |
| Phase 6.5 Release v1.0 | `ai_platforms/release/v1.0/` + `.work/07_release/{PLAN,RETROSPECTIVE}.md` (tag `v1.0-company-release`) |
| METHODOLOGY 公开声明 | `METHODOLOGY.md` + `ai_platforms/release/v1.0/METHODOLOGY.{en,zh,ja}.md` |
| 07 Website Phases 6-8 (closed) | `.work/07_website/phase{6,7,8}/` + handoffs `.work/meta/website_phase*_handoff_*.md`; prod https://sdtm-pedia.pages.dev/ |

## AI 平台双平台并行部署 (锁步规则)

涉及 **ChatGPT GPTs** (`ai_platforms/chatgpt_gpt/`) 或 **Gemini Gems** (`ai_platforms/gemini_gems/`) 任一方时, 遵守锁步规则:

1. **Session 启动自动动作**: 若用户首次提到两平台任一方, 主 session 必须先读 `ai_platforms/SYNC_BOARD.md` + 两份 `dev/evidence/_progress.json`, 报告当前锁步 Phase + 允许的下一动作, **再开工**.
2. **Gate 机制**: Phase 0-5 (启动/调研/PLAN/落地/审查/收束), 任一 Phase N 两边未都 PASS, **两边都不能进 Phase N+1**. 主 session 派发 Phase N+1 subagent 前强制校验.
3. **PASS 四条** (规则 D 强制): evidence 存在 / writer 产物合规 / 独立 reviewer subagent PASS (不同 subagent_type) / 用户口头 ack.
4. **偏离处理**: 若两平台 Phase 偏离 >1 格, 先同步慢的那边, 再推快的. **严禁跑通一边再补另一边** (会丢失 cross-pollination).
5. **并行派发模式**: 每 Phase 内用 2 个 subagent 并行 (各平台一个), 主 session 做 cross-review + 更新 `_template/` 缺陷.
6. **状态写回**: 每步操作完, 双写更新两处: 对应平台 `_progress.json` + `SYNC_BOARD.md` Phase 矩阵格.

Claude Projects 已完成, **不**参与本锁步 — 仅作为方法论参考 (`ai_platforms/claude_projects/docs/RETROSPECTIVE_V2.md`).

## Session Wrap-up (收尾)

When the user says **"收尾"**, **"wrap up"**, or **"提交收尾"**, execute the following checklist automatically:

1. **Review** what was done this session (read git diff + new files)
2. **Update index files** — always update these 3 (+ CLAUDE.md if new key paths):
   - `.work/MANIFEST.md` — plan map, directory structure, phase mapping, quick reference
   - `.work/meta/worklog.md` — execution phase table + append work record entry
   - `docs/PROGRESS.md` — progress board status
   - `CLAUDE.md` Key Paths table (only if new key paths were created; 单元格 ≤ 80 字符)
3. **Prune CLAUDE.md** — 按"CLAUDE.md 写作规则"扫一遍: 该阶段已关闭的 round/batch/version 进度状态, 删除或迁移到 worklog; 总行数应稳定在 150 行以内
4. **Check Change Chains** — if knowledge_base/ changed → Chain D; if plans changed → Chain E
5. **Commit + push** — single commit with descriptive message, push to main
6. **Report** — one-line summary of what was committed

Do NOT ask for confirmation on each step — just execute the full checklist and report at the end.

## Conventions

- Knowledge base content is in English (extracted from English PDF sources)
- Work logs, plans, and meta docs are in Chinese
- File status fields use format: `> 状态: **已完成** (date)` or `> 状态: 描述`
- When completing a task, follow Chain B (work log → progress.json → docs/PROGRESS.md)
