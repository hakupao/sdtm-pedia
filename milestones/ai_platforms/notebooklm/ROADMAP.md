# NotebookLM Deployment Roadmap (v2, 2026-04-21 架构 pivot 后)

## 状态 (首屏)

- **当前状态**: ✅ **Phase 5 SIGN-OFF 闭环 (2026-04-24 Daisy 认可)** — retro v1.0 FINAL + UPLOAD_TUTORIAL v1.0 同批交付 (async lane NotebookLM 全 lifecycle 完成)
- **smoke v4 R1**: **15/17 (88.2%) strict PASS** — AHP × 3 全 PASS+ 最强 (in-KB-only 天然反虚构优势)
- **跨 4 平台合流**: `ai_platforms/retrospectives/PHASE5_RETROSPECTIVE.md` 已 **v1.0 FINAL 2026-04-24 Daisy 认可** (4 平台 sign-off 闭环 ✅)
- **目标 Tier**: **Tier 2** (5-15 步, 半天-1 天) — 实际 lifecycle 3 天 (2026-04-21 起跑 pivot → 2026-04-23 Phase 4 闭合)
- **模式**: 异步 (不参与 `SYNC_BOARD.md` 2-way 锁步)
- **参考基线**: Claude v2.6 方法论 + ChatGPT/Gemini 范本补丁
- **架构**: **1 notebook × 42 sources** (v1 3 notebook × 各 30-293 源已归档)

## v2 架构 (首屏)

### 1. 状态 + 日期
- **Phase 0-1 PASS 2026-04-21** — 事实依据已核实 (Pro tier / 500 notebooks / Chat custom goals / 50-cap 仅 Restricted invite)
- **Phase 2 v1 (3 notebook) 已废 + 归档** (2026-04-21, 见 `archive/v1_3notebook_SUPERSEDED_2026-04-21/`)
- **Phase 2 v2 (1 notebook × ≤50) 进行中** — PLAN 重写中

### 2. 着重方向 (本平台独有优势)
- **Audio Overview 培训产物**: SDTM 初学者 30 分钟可听完一期"SDTM Domain 速览"播客
- **Mind Map 关系可视化**: 跨 domain 的 RELREC / --STAT / Supplemental Qualifier 依赖关系图形化
- **Grounded citation 默认强**: 每句都能点回源 chunk, "SDTM 标准依据"类问题最稳
- **Study Guide / Briefing Doc 自动化**: 问卷式学习产出

### 3. 平台特性 (已 Phase 1 确认)

| 维度 | 值 | 来源 |
|------|-----|------|
| 订阅 | **Pro** (via Google AI Pro) — 500 notebooks × 300 sources × 500 chat × 20 audio/day | support.google.com/notebooklm/answer/16213268 |
| RAG | 内置 grounded retrieval, chunk-level inline citation | 官方 |
| Source 数上限 (硬) | Pro 300 / notebook; 500K words / source 全档统一 | 同上 |
| **本次实际使用** | **≤50 sources** (主动压缩 Free tier 兼容水位) | v2 架构 |
| 文件类型 | PDF, .txt, .md, Google Docs/Slides, 网页 URL, YouTube URL, 音频文件 | 官方 |
| 分享 | **同一 notebook 3 档** (Restricted / Anyone with link / Public) 可切 | answer/16322204 |
| Chat custom goals | 三档 (Default / Learning Guide / **Custom**), Custom 10K char 写 SDTM 专家 | blog.google 2025-10-29 |
| API | 无 GA consumer API (本次 Web UI only) | research §12 |

### 4. 内容策略 (已 Phase 2 v2 定)

- **单 notebook**: 293 md → concept cluster 重 bucket → **≤50 source**
- **ABC 三场景在同一 notebook 内按分享档位切换** (默认 Restricted, 按需切 Anyone with link / Public)
- **Req 零丢失红线** (用户 2026-04-21 ack Q1=0): concept cluster 保证 ~100-120 独立 Req 变量全覆盖
- **Chat mode**: Custom (10K char, SDTM 专家 prompt)

### 5. 执行步骤 (Phase 0-5)
- Phase 0 脚手架 ✓
- Phase 1 八问八答调研 ✓ (含 Chat custom goals / Indexing silent fail 三 WebFetch 核实)
- Phase 2 PLAN ✓ (v1 ×3 notebook 归档, v2 ×1 notebook 重写)
- Phase 3 单批上传 (≤50) + A/B 15 题 + 独有生成物评估 + 分享档位演练
- Phase 4 回归 + 跨平台 (Claude/ChatGPT/Gemini/NotebookLM 四平台) 同题对比
- Phase 5 RETROSPECTIVE (含本次 pivot 作关键案例) + `_template/` 缺陷补丁合并 + handoff

### 6. 验收标准 (A/B 矩阵 PASS 条件)
- **15 题** (10 SMOKE v2 + 5 独有生成物评估: Audio Overview 2 + Mind Map 2 + Study Guide 1)
- PASS 阈值: **≥13/15 (~87%) 业务正确 + 每个独有产出至少 1 题精确命中**
- **Req 变量零丢失** (用户 Q1 红线, 基于 `extract_req_vars.py` 产出对照审计)

## 实际产出 (Phase 4 闭合 2026-04-23 填)

- 文件数: **42 sources** (目标 ≤50, 8 slot headroom)
- 总 words: **1,582,085** (最大 bucket 302K < 500K/source cap, 0 over-cap / 0 missing)
- Source 占用: **42/300** Pro slot (14%, 远低 Pro cap)
- Req 变量覆盖: **176/176 独立 Req ∅ gap** (A4 结构级 + P3.4.5 语义级双锚)
- Domain 覆盖: **63/63** 全覆盖
- A/B PASS: **smoke v4 R1 15/17 (88.2%) strict PASS** (6 PASS + 8 PASS+ + 2 PARTIAL + 1 safety-correct PUNT); AHP × 3 全 PASS+ 最强
- P3.9 三档切换演练: **PASS** (5 PASS + 1 PARTIAL Public≠gallery 新发现 + 1 SKIP Free-tier cap 接受残余风险)
- 跨平台对比: 4 平台矩阵 `ai_platforms/SMOKE_V4.md §3` 17×4 filled; NotebookLM 15/17 vs Claude 17/17 / ChatGPT 16.5/17 / Gemini R2 16/17
- `_template/` 补丁: **10a/10b.1/10b.2/15** 已吸收到跨 4 retro §4; **16-19** 候选登记本 retro §4 待 Daisy ack

---

## CHANGELOG

| 日期 | 版本 | 变更 |
|------|------|------|
| 2026-04-21 (am) | v1 draft | 初版, Phase 0 脚手架, 3 notebook × 30-293 源假设 |
| 2026-04-21 (pm) | **v2** | **架构 pivot** (3 notebook → 1 × ≤50) — 用户 UI 实测 + 三 WebFetch 核实, 见 `archive/v1_.../ARCHITECTURE_PIVOT_RECORD.md` |
| 2026-04-22 | v2.1 / v2.2 | PLAN v2.1 ICEBOX Studio 三件套 (P3.5/P3.6/P3.7 post-project optional) + v2.2 P3.8 题库 smoke v2.1 → v3 Q1-Q10 升级对齐 ChatGPT+Gemini N5.3; P3.8 9/10 strict PASS; smoke v3→v4 升级决策 (加 AHP × 3) |
| 2026-04-23 | **Phase 4 COMPLETE** | smoke v4 R1 15/17 (88.2%) + AHP × 3 全 PASS+ 最强; P3.8 reviewer 12th slot (feature-dev:code-reviewer) PASS; P3.9 三档切换演练 PASS (5 PASS + 1 PARTIAL + 1 SKIP) |
| 2026-04-24 (上午) | Phase 5 DRAFT v0.1 | 跨 4 平台 `PHASE5_RETROSPECTIVE.md` v1.0 FINAL Daisy 认可; NotebookLM 平台独立 `docs/RETROSPECTIVE.md` v0.1 DRAFT (主 session writer lane) |
| 2026-04-24 (下午) | Phase 5 v0.2 post-reviewer-fix | 独立 reviewer `oh-my-claudecode:critic` CONDITIONAL_PASS 8.0/10 → 1 HIGH + 4 MEDIUM + 3 遗漏 + 2 Open Q 全修 → v0.2 ack-ready; `dev/evidence/phase5_retrospective_reviewer.md` 落档 |
| 2026-04-24 (晚) | ✅ **Phase 5 SIGN-OFF** | retro **v1.0 FINAL** Daisy 认可 + `current/UPLOAD_TUTORIAL.md` **v1.0** 同批产出 (10 章节 276 行) + 4 索引文件同步 (CLAUDE.md + MANIFEST + PROGRESS + ROADMAP) — NotebookLM async lane 全 lifecycle 完成 ✅ |
| 2026-04-24 (晚, post-sign-off) | **Post-project ICEBOX TRIGGERED** | Daisy 主动触发 Studio 三件套 ICEBOX lane (P3.5 Audio × 3 / P3.6 Mind Map / P3.7 Study Guide × 3) — **证伪** D-NBL-2 "ICEBOX 触发条件 weak → 永不做" 负外部性担忧; lane 位置 `post_project_icebox/STUDIO_TRIO_HANDOFF.md` (258 行自足); Daisy 在其他终端 NotebookLM Web UI 实操; 主 session 侧: `_template/` 补丁 16-19 inline 合入 4 原文件 (00/02/05/06 +110 行) 完成升 ✅ APPLIED; PATCHES.md + README.md 状态表同步 |

---

*更新规则: 每 Phase 收束时刷新本文件首屏 + append 一条 CHANGELOG.*
