# NotebookLM 平台部署 PLAN (v1, 2026-04-21)

> **产出时间**: 2026-04-21
> **Writer**: Phase 2 PLAN Writer (`oh-my-claudecode:planner`, opus) — Rule D 第 5 种 subagent_type
> **审查链**: Writer#1 `general-purpose` → R1 `verifier` → Writer#2 `executor` → R2 `critic` → **本 PLAN Writer** `planner` → 待 R3 (第 6 种) 独立审核
> **所属 Phase**: 2 PLAN (Phase 1 Research 已 PASS, 见 `dev/evidence/_progress.json`)
> **项目 Tier**: **Tier 2** (5-15 step, 半天-1 天级体量, 走 workflow-tier2 模板 — PLAN.md / _progress.json / evidence/ / failures/ / RETROSPECTIVE.md 齐全)

---

## 执行摘要 (Executive Summary)

本 PLAN 把 SDTM 293 md 知识库部署到 **NotebookLM Pro tier** (via Google AI Pro 订阅, personal Gmail 账号), 采用 **multi-notebook 架构**: Notebook 1 主训练 (Scope A 个人学习, 一对一上传 293 md, 余 7 source slot) + Notebook 2 Scope B Mode A (invite-only ≤50 users, 合并到 ≤30 精选 source) + Notebook 3 Scope B Mode B (public link 无 user cap 需 Google 账号, 独立上传同 ≤30 精选).

三 notebook 因 NotebookLM source 严格隔离 (见 research.md §11), 必须**分别独立上传** source, 代价 = 最坏 293 + 30 + 30 = 353 次 Web UI 上传操作. 关键风险: (1) Pro tier audio 20/day 限制意味 A/B Audio 题必跨天; (2) Mode B 50-cap 归属 UNVERIFIED (见 C2.9), 可能破坏 Scope B 广泛分享前提; (3) Indexing silent fail 已由 Google 官方确认 (research.md Q5). Phase 3 第一 Task = **Pre-upload audit** (`wc -w` Top 5 outlier md 过筛 500K words 单源 cap, 见 §5 动作 1).

A/B 矩阵共 **45 题次** (3 notebook × 15 题: 10 smoke v2 共享 + 5 独有 per notebook). 每 notebook 独立 PASS (≥13/15 ~87%).

---

## Project Success Criteria

三 notebook 部署的**业务成功定义** (非 technical 交付物清单). 用户 2026-04-21 ack:

1. **Quality**: 3 notebook 各 A/B PASS ≥13/15 (~87%) AND **Req 变量零丢失** (Q1 红线, 见 §3.2.1); 独有 5 题每 notebook 至少 4/5 精确命中.
2. **Completeness**: 3 notebook + 3 instructions_N.md + UPLOAD_TUTORIAL 10 章节 + 3 uploads_N/MANIFEST.md + consistency_review.md + cross_platform_compare.md 全落盘.
3. **Template contribution**: `_template/` 补丁候选 ≥9 条 (原 7 + P11/P12) PR 合并; **SDTM-like 领域红线审计模式**作补丁候选 #10 (见 §9).
4. **Cross-platform data**: 10 smoke v2 和 Claude v2.6 / ChatGPT GPTs / Gemini Gems 三平台对比数据 (`docs/cross_platform_compare.md`) 完整.
5. **Workflow replication**: 任何 SDTM 工作者凭 `current/uploads_N/` + `UPLOAD_TUTORIAL.md` 能 ≤1 天独立在自己 Google AI Pro 账号上重建等效 3 notebook 且通过 smoke v2 Q1-Q3.

**分用户群 use-case success**:
- **Success A (Scope A, 用户本人)**: 30 秒内用 Notebook 1 回答 smoke v2 Q1-Q3, citation 精确到 md 段
- **Success B (Scope B Mode A, ≤50 同事)**: 5 位受邀同事 onboard 后 ≤10 分钟独立查任 core domain spec + 理解 Learning Guide Socratic 引导
- **Success C (Scope B Mode B, 陌生 public)**: 陌生访客打开 Notebook 3 能读懂 smoke v2 Q1-Q3 且回答不含臆造事实 (对比 Notebook 2 差异 ≤20%)

---

## §0 修订记录

| 版本 | 日期 | Writer | 变更 | 触发 |
|------|------|--------|------|------|
| v1 | 2026-04-21 | planner | 初版 PLAN (集成 Phase 1 research 全量事实 + R1/R2 carry-over 10 条 + known_differences_from_template 7 条) | Phase 1 PASS, 进 Phase 2 |
| v1.1 | 2026-04-21 | feature-dev:code-architect (Writer #4) | R3 analyst CONDITIONAL_PASS 82% 6 必改 + 1 连锁: I3 挂 P3.9 + §6 每 Task 工时/操作数/parallel_with + §3.2 Q1=0 零丢失红线 + Project Success Criteria + §2.5 Phase A Setup + §8.4 失败集中表 + extract_req_vars.py 新脚本 | R3 审核 + 用户 Q1/Q2 ack 2026-04-21 |

### 用户二次 ack (2026-04-21, Q1/Q2 决策)

| Q | 问题 | 用户决定 | 连锁影响 |
|---|------|---------|---------|
| **Q1** | SDTM 业务红线 — Notebook 2/3 精选 ≤30 source 合并后允许丢失 Core=Req 变量? | **零丢失 (0 Req 变量允许丢)** — 零容忍 | §3.2.1 合并策略改 concept cluster + §3.4 阈值 "2→0" + §5 动作 4 加 Req 审计 + §6 P3.4 加审计子步骤 + §10 carry-over 一行 |
| **Q2** | 工时节奏 — 是否赶 1 天内完成 Phase 3? | **不限工时, 质量第一** | §6 Task 工时估算取保守上界; §4.4 Audio 分 3 天不强制压 2 天; 失败重试预算可放宽 |
| 方案 | W#4 + R#4 一轮修正方案选择 | **Y (严格方案)** | Writer #4 = feature-dev:code-architect; R#4 = pr-review-toolkit:code-reviewer |

### Phase 1 engrained 事实摘录 (本 PLAN 的立足点)

| # | 事实 | 来源 |
|---|------|------|
| 1 | **套餐 = NotebookLM Pro tier** (via Google AI Pro 订阅), 非 "Plus" — SKU 语义漂移后原 Plus 规格 (300 sources) 上移改名 Pro, 新 Plus 仅 100 sources | research.md Q2 表 + Q3 时间线 2025-05 I/O 行 + 脚注 SKU 警示 (line 35, 46) |
| 2 | **Pro tier 四数字**: 500 notebooks/user × 300 sources/notebook × 500 chat/day × 20 audio/day | research.md Q2 (line 42) |
| 3 | **500K words/source 全 tier 统一**, SDTM 单 md 远 <10K words, 不触发单源 cap | research.md Q2 脚注 + Q8 (line 228-229) |
| 4 | **Chat custom goals 三档** Default / Learning Guide / Custom (**全档开放, 非 Plus+ 独享**), 2025-10-29 blog.google 发布; Custom mode 10,000 char 可自定角色 — 本平台最接近 system prompt 机制 | research.md Q6 Custom Instructions 行 (line 155) + 关键差异段 (line 159) |
| 5 | **Source 严格隔离** — "Each notebook is independent, and NotebookLM can't access information across multiple notebooks at the same time" (官方 philosophy); notebook 2/3 不能引用 notebook 1 source, 必须分别独立上传 | research.md §11 (line 314) |
| 6 | **分享双模式**: Mode A Direct invite (email 邀请, personal Gmail 50 users cap) + Mode B Public link (仅 consumer Gmail 开, 无 user 上限, 需访客持 Google 账号); 两模式可叠加但 Scope B 本质两选一 | research.md Q7 全节 (line 174-218) |
| 7 | **Indexing silent fail** 官方承认, 点击 source tile 预览内容是唯一可靠验证手段; YouTube <72h 不能立即 import | research.md Q5 (line 124-131) |
| 8 | **Capacity 透明** (sources 数 + words/source 硬指标), skip calibration; 对比 Claude Projects 的 capacity% 黑盒, NotebookLM 直接给数字 | research.md Q8 + platform_profile §B (line 29) |
| 9 | **Audio Overview 4 format**: Deep Dive / The Brief / The Critique / The Debate; Custom prompt 10,000 char 上限; **per-day 非 per-month**; Pro = 20/day | research.md §9 (line 242-275) |
| 10 | **Workflow_replication fallback**: 若分享模式受限, 通过 current/UPLOAD_TUTORIAL.md + 打包 uploads/ 让接收者自建复刻 (用户 2026-04-21 ack, platform_profile §E line 80) | platform_profile.md §E + _progress.json rule_E_user_priority |

### 对 Phase 0 初稿的显式修订条 (研究后修订 10 条的本 PLAN 相关子集)

| # | 原 Phase 0 假设 | 本 PLAN 修订 | 对应 research.md 修订表行 |
|---|----------------|-------------|-----|
| M1 | "套餐 Plus (via Google AI Pro)", 300 sources | 修订为 Pro tier, 300 sources 属 Pro (SKU 漂移); PLAN §3 三 notebook 架构均按 Pro 预算 | research.md 修订 #1 #2 |
| M2 | Multi-notebook "Plus 权益下 3 个 notebook" | Pro 权益 500 notebooks/user, 3 个占 0.6%, 远充裕; PLAN §3 明示 source 隔离代价 (最坏 353 次上传) | research.md 修订 #3 |
| M3 | Audio "每月 Plus 5x" (暗示月额) | per-day, Pro=20/day; PLAN §4 A/B Audio 题**必跨天**, §6 Task 分布标明 | research.md 修订 #4 |
| M4 | "NotebookLM 无 system prompt, 退化 3 条" | 补最新 **Chat custom goals 三档** (2025-10-29 发布, 全档开放); PLAN §5 动作 2 + §3 每 notebook 固化 Chat mode 决策 | research.md 修订 #5 |
| M5 | "Indexing 训练知识印象相对可靠" | 官方承认 silent fail, PLAN §6 Task P3.1 加 indexing smoke test 前置 gate, pass 前不进全量上传 | research.md 修订 #6 |
| M6 | 未提 pre-upload audit | PLAN §5 动作 1 + §6 Task P3.0 强制 `wc -w` 排序 Top 5 outlier, 确认无 >500K words single source | research.md 修订 #7 |
| M7 | "公开分享具体权限模型待确认" | 修订为 Mode A (invite 50 cap) + Mode B (public link 无 cap 需 Google 账号) 两独立模式; PLAN §3 Notebook 2/3 分别对应; §6 Task P3.7 验 Mode B cap (挂 I8) | research.md 修订 #9 |

---

## §1 执行规则 P1-P12 + 规则 A/B/C/D/E

继承全局 `~/.claude/CLAUDE.md` 四条规则 A/B/C/D, 范本规则 E (用户优先级早问), 本 PLAN P1-P10 传承 + **P11/P12 本平台新增**:

| # | 规则 | 适用 | 本平台特化 |
|---|------|------|----------|
| **A** (全局) | 语义抽检: 压缩/改写 >50% 强制 N 样本独立抽检 | Phase 3/4 writer 完成后 | 本平台: Notebook 2/3 合并到 ≤30 source (压缩率 ~90%) → 必触发规则 A, N 样本 = 10 |
| **B** (全局) | 失败归档: `failures/step_NN_attempt_X.md` 不删 | 任何失败 attempt | 失败归档路径 `dev/evidence/failures/task_<N>_attempt_<X>.md` |
| **C** (全局) | Retro 强制: Tier 2/3 收尾必写 RETROSPECTIVE.md 三段式 | Phase 5 收束 | docs/RETROSPECTIVE.md, 另经独立 reviewer (第 8+ subagent_type) 复核 |
| **D** (全局) | 写审分离: Writer ≠ Reviewer, 不同 subagent_type | 每次 subagent 派发 | 本 PLAN 为 Writer#3 (planner), 待 R3 (第 6 种) 审; Phase 3/4 会开到第 7/8 种 |
| **E** (范本) | 用户业务优先级必须在 Phase 0/2 即确认 | 本次**已 ack 2026-04-21** | ABC 全向 + Pro tier + Web UI + personal Gmail, 见 _progress.json rule_E_user_priority |
| **P1** | 量化 PASS: 每 step 打印 `[Stage X.Y] <file>: <N> words (target ≤500K)` | 每 step | 本平台用 **words 不用 tokens** (官方 help 原文), 不做 tokens 换算 |
| **P2** | 写/审分离执行态: executor ≠ reviewer subagent_type | 每 subagent 派发 | 同规则 D |
| **P3** | AI 估算值前缀 `~`, 实测值不加 | manifest / 报告 | Indexing 时间 / audio 质量评分等实测数字无前缀, 估算数字 (如"SDTM md 总 words ~3M") 加 `~` |
| **P4** | 人工抽查 checkpoint: 每 Task 显式标 hard/soft/none, 不擅自连推 | 每 Task | 见 §6 Task 分解, 每 Task 末尾有 "Checkpoint 级别" 行 |
| **P5** | 源文件只读: `knowledge_base/` 不允许 Edit/Write | 全程 | `git status knowledge_base/` 非 clean 立即回滚 |
| **P6** | Subagent 上下文隔离: 每个脚本独立 executor, 主控不读脚本源 | 每次派发 | 每次 agent 调用 prompt 归档到 `dev/evidence/subagent_prompts/task_<N>_<role>.md` |
| **P7** | 进度持久化: 每 Task 完成立即更新 `dev/evidence/_progress.json` + `trace.jsonl` | 每 Task | Schema 继承 Phase 1 的 phase_states/sub_steps/carry_over_* 结构 |
| **P8** | 失败归档 (同规则 B) | 任何失败 | — |
| **P9** | 语义抽检 (同规则 A) | Notebook 2/3 合并压缩时 | N=10 (中批规模, 规格见 _spec/06_review.md §规则 A 抽样规格) |
| **P10** | A/B 衰减强制响应 (本平台改写): **A/B 题 PASS <87%/notebook 触发重构** (而非跨批衰减, 本平台单批无跨批) | 每 notebook A/B 完成后 | 若某 notebook <87% (即 <13/15), 走 P10 响应: 归因 (source 缺失 / Chat mode prompt 问题 / 平台能力边界) → reviewer 归因 → 用户决策 continue/rework |
| **P11 (新)** | **Per-day rate limit 约束**: Audio ≤20/day, Chat ≤500/day; 任何 A/B 循环超限**必跨天执行** | Phase 4 执行 Audio 相关题 | 本平台独有; 3 notebook × 2 audio 题 = 6 audio 生成, 单日可完成; 但若加 retry 则必须预留次日窗口. 作为 `_template/` 补丁候选 #8 |
| **P12 (新)** | **Source 隔离约束**: notebook A 的 source 不能被 notebook B/C 引用, 三 notebook 必须分别上传 | Phase 3 所有上传 Task | 本平台独有; Notebook 1 上传 293 md + Notebook 2/3 各上传精选 ≤30 = 最坏 **353 次 Web UI 上传**; 为 `_template/` 补丁候选 #9 (前 7 条已在 platform_profile.md 末段) |

**Rule E 引用**: 用户 2026-04-21 已 ack Scope ABC 全向 + Pro tier + Web UI only + personal Gmail, 见 `dev/evidence/_progress.json` `rule_E_user_priority` 段. 本 PLAN 三 notebook 架构直接由此 ack 锚定, 不再回头问用户.

---

## §2 文件结构 map (Create / Modify / Read-only)

按 `_spec/01_directory_structure.md` 四层 + multi-notebook 专属子目录扩展 (补丁候选 #5 应用).

### 2.1 Create (Phase 2-5 内新建)

```
ai_platforms/notebooklm/
├── docs/
│   ├── PLAN.md                                  ← 本文件 (Phase 2 产物)
│   ├── RETROSPECTIVE.md                         ← Phase 5 (规则 C)
│   ├── handoff.md                               ← Phase 5 (若 Phase 7 RAG/KG 启动)
│   └── cross_platform_compare.md                ← Phase 4 (4 平台 10 smoke v2 对比)
├── current/
│   ├── README.md                                ← Phase 5 (发布版总览)
│   ├── UPLOAD_TUTORIAL.md                       ← Phase 5 (10 章节用户视角)
│   ├── uploads_main/                            ← 🆕 multi-notebook 专属 (Notebook 1)
│   │   ├── MANIFEST.md                          ← 293 md source 清单
│   │   └── README.md                            ← 本 notebook 能力 + 限制
│   ├── uploads_invite/                          ← 🆕 Notebook 2 (Mode A)
│   │   ├── MANIFEST.md                          ← ≤30 精选 source 清单 + 合并策略
│   │   └── README.md
│   ├── uploads_public/                          ← 🆕 Notebook 3 (Mode B)
│   │   ├── MANIFEST.md                          ← 同 Notebook 2 精选清单 (独立上传)
│   │   └── README.md
│   ├── instructions_1.md                        ← 🆕 Notebook 1 Chat custom goals 文本 (≤10K char)
│   ├── instructions_2.md                        ← 🆕 Notebook 2 (Learning Guide / Custom 决策)
│   └── instructions_3.md                        ← 🆕 Notebook 3 (Custom, public-friendly)
├── dev/
│   ├── scripts/
│   │   ├── count_words.py                       ← 改写自 claude count_tokens, 本平台用 words
│   │   ├── source_mapping.py                    ← 293 md → Notebook 1 source 映射 + `--audit-req-coverage` flag (Q1=0)
│   │   ├── select_core_domains.py               ← legacy (Q1=0 前 domain-unit 挑, 被 cluster_req_variables.py 替代, 保留对照)
│   │   ├── cluster_req_variables.py             ← 🆕 Notebook 2/3 concept cluster 重分 bucket (Q1=0 实现)
│   │   ├── extract_req_vars.py                  ← 🆕 从 VARIABLE_INDEX.md + domains/*/spec.md 抽 Core=Req 全集 (Phase A A6)
│   │   └── pre_upload_audit.py                  ← wc -w 排序 + Top 5 outlier 校验
│   ├── evidence/
│   │   ├── pre_upload_audit.md                  ← Phase A A1 产物
│   │   ├── source_mapping.md                    ← Phase A A3 产物
│   │   ├── req_vars_full_set.md                 ← 🆕 Phase A A6 — SDTM Req 变量全集 (~366 记录, 去重 ~100-120 独立)
│   │   ├── req_vars_coverage_audit.md           ← 🆕 Phase A A4 — Notebook 2 ≤30 覆盖 vs 全集 diff (Q1=0 自证)
│   │   ├── webui_batch_capability.md            ← 🆕 Phase A A5 — Web UI batch upload 能力实测
│   │   ├── mind_map_refresh_test.md             ← 🆕 Phase 3 P3.9 — I3 Mind Map 自动/手动刷新观察
│   │   ├── phase3_task_N_audit.md               ← 每 Task 规则 A 抽检 (规则 A 触发时)
│   │   ├── subagent_prompts/                    ← 每次派发 prompt 归档 (P6)
│   │   ├── failures/                            ← task_<N>_attempt_<X>.md (规则 B)
│   │   └── checkpoints/                         ← hard checkpoint handoff (P4)
│   ├── ab_reports/
│   │   ├── notebook_1_ab.md                     ← Notebook 1 15 题 A/B
│   │   ├── notebook_2_ab.md                     ← Notebook 2 15 题 A/B
│   │   ├── notebook_3_ab.md                     ← Notebook 3 15 题 A/B
│   │   └── consistency_review.md                ← 跨 notebook 一致性审查
│   └── test_results.md                          ← 45 题次完整记录
```

### 2.2 Modify (执行中滚动更新)

```
ai_platforms/notebooklm/dev/evidence/_progress.json    (每 Task 完成)
ai_platforms/notebooklm/dev/evidence/trace.jsonl        (append-only)
ai_platforms/notebooklm/README.md                       (Phase 5 reorg 后)
ai_platforms/notebooklm/ROADMAP.md                      (Phase 5 状态改 "已完成")
.work/MANIFEST.md                                       (Phase 5 收束时, Chain 规则)
.work/meta/worklog.md                                   (Phase 5 收束时)
docs/PROGRESS.md                                        (Phase 5 收束时)
CLAUDE.md                                               (Phase 5 收束时, Key Paths 新增 notebooklm 入口)
```

### 2.3 Read-only (强制禁写)

```
knowledge_base/**                                       (P5)
ai_platforms/_template/**                               (范本不可污染, 补丁候选走 Phase 5 PR)
ai_platforms/notebooklm/_spec/**                        (Phase 0-1 已固化, 禁改)
ai_platforms/notebooklm/docs/research.md                (Phase 1 固化, 禁改; 新事实写进 PLAN)
ai_platforms/notebooklm/docs/platform_profile.md        (同上)
ai_platforms/notebooklm/dev/evidence/phase1_reviewer*.md (Phase 1 审查纪录)
ai_platforms/SYNC_BOARD.md                              (本平台**不**参与 2-way 锁步, 只在 Phase 5 加一行状态)
ai_platforms/claude_projects/**                         (已完成, 参照只读)
```

### 2.4 脚本职责边界 (单一职责, P6)

| 脚本 | 单一职责 | 输入 | 输出 |
|------|---------|------|------|
| `count_words.py` | 用 `wc -w` 语义数 words (英文 md 主要) | 目录或文件 | stdout: `<file>: <N> words` |
| `pre_upload_audit.py` | wc -w 排序 + 过筛 Top 5 outlier + 对 500K 单源 cap 校验 | `knowledge_base/**/*.md` | `dev/evidence/pre_upload_audit.md` (Top 5 + PASS/FAIL per source) |
| `source_mapping.py` | 决定 "293 一对一上传" vs "合并到 ≤300" 策略, 产 Notebook 1 source 清单 | 293 md paths + 策略参数 | `dev/evidence/source_mapping.md` + `current/uploads_main/MANIFEST.md` |
| `select_core_domains.py` | (legacy, Q1=0 前 domain-unit 挑; 被 `cluster_req_variables.py` 替代, 保留作对照) 基于 SDTM 业务优先级筛 ≤30 source | 293 md + 优先级权重 | 已废弃 — 实际输出由 cluster_req_variables.py 产 |
| `extract_req_vars.py` 🆕 | 从 `knowledge_base/VARIABLE_INDEX.md` + `domains/*/spec.md` 抽所有 `Core=Req` 变量, 产出全集清单 (通用 Req 分组 + 域特定 Req 分组) | `knowledge_base/**` | `dev/evidence/req_vars_full_set.md` (~366 记录, 去重 ~100-120 独立) |
| `cluster_req_variables.py` 🆕 | 基于 concept cluster (Demographics / Interventions / Events / Findings 3 levels / Trial Design / Relationships) 重分 bucket, 产 Notebook 2/3 的 ≤30 source bucket 方案 (Q1=0 实现) | `req_vars_full_set.md` + 293 md | `current/uploads_invite/MANIFEST.md` + `current/uploads_public/MANIFEST.md` (内容一致) |

---

## §2.5 Phase A Setup (先于 Phase 3, 独立段)

本段显式列 Phase 3 启动**前必须完成**的 Setup Task, 替代 R3 指出的 "Setup 动作混在 §5 前置动作 + §6 Task P3.0 开头" 的隐式设计. Phase A 共 **6 子动作**, 其中 4 条继承原 §5, 新增 2 条 (A5 batch upload 能力调研 + A6 Req 变量全集 extract).

| Task | 子动作 | 输入 | 输出 | Checkpoint | 估算工时 |
|------|-------|------|------|-----------|---------|
| **A1** Pre-upload audit | `find knowledge_base -name '*.md' -exec wc -w {} \;` → 排序 Top 5 outlier → 500K cap 校验 | `knowledge_base/**/*.md` | `dev/evidence/pre_upload_audit.md` | **hard** | 15 分钟 |
| **A2** Chat mode 决策固化 | 3 notebook Chat mode 落盘到 3 instructions_N.md (N=1 Custom SDTM 专家, N=2 Learning Guide, N=3 Custom public) | 空白 → 用户决策文本 | `current/instructions_1.md` + `instructions_2.md` + `instructions_3.md` (均 ≤10K char) | soft | 2-4 小时 |
| **A3** Notebook 1 source 映射 | 决定 "293 一对一 vs 少量合并到 ≤300" (视 A1 outlier 结果) | A1 产物 + 293 md | `dev/evidence/source_mapping.md` + `current/uploads_main/MANIFEST.md` | **hard** | 1-2 小时 |
| **A4** Notebook 2/3 精选清单 (**含 Req 变量全覆盖审计, Q1=0 红线**) | 从 293 md 选 ≤30 source + 审计 Req 零丢失 | 293 md + A6 产物 | `current/uploads_invite/MANIFEST.md` + `uploads_public/MANIFEST.md` (内容一致) + `dev/evidence/req_vars_coverage_audit.md` | **hard** | 4-6 小时 |
| **A5 (新)** NotebookLM Web UI batch upload 能力调研 | 登 Web UI 实测: 单文件拖 / 多选拖 / 文件夹拖 是否支持 + indexing 并发行为 | Web UI (手测 或 MCP) | `dev/evidence/webui_batch_capability.md` (3 场景 PASS/FAIL + 截图 + 操作次数预估修正) | **hard** (R3 主张, 决定 Phase 3 是否走 Playwright) | 1 小时 |
| **A6 (新)** SDTM 293 md Req 变量 extraction | 运行 `extract_req_vars.py` 从 `VARIABLE_INDEX.md` + `domains/*/spec.md` 抽 `Core=Req` | `knowledge_base/VARIABLE_INDEX.md` + `domains/*/spec.md` | `dev/evidence/req_vars_full_set.md` (~366 记录; 去重后 ~100-120 独立; "通用 Req" + "域特定 Req" 两表) | **hard** (Q1=0 红线前置数据; A4 审计无 baseline) | 1-2 小时 |

**Phase A 总工时估算**: **9-16 小时** (不赶可分 2-3 天; Q2 保险 2x 则 18-32 小时). Phase A 完成前**不得启动** §6 Phase 3 Task P3.0.

**Phase A 依赖图 (parallel_with)**:
- A1 独立 — 可第一个跑
- A2 独立 — 可和 A1 并行
- A3 依赖 A1 (A1 outlier 决定是否拆分)
- A4 依赖 A6 (没 Req 全集无法审计)
- A5 独立 — 可和 A1/A2/A6 并行
- A6 独立 — 可和 A1/A2/A5 并行

**推荐调度**: Day 1 并行 A1 + A2 + A5 + A6; Day 2 串行 A3 → A4.

**Phase A 完成判据** (进 §6 Phase 3 的 gate):
- 6 子动作 evidence 全部落盘
- A1/A3/A4/A5/A6 5 个 hard checkpoint 用户 ack
- `req_vars_coverage_audit.md` 显式声明 "Req 变量零缺集" (∅ gap)

---

## §3 Multi-notebook 架构设计 (核心)

Phase 1 已定型 3 notebook 策略 (`known_differences_from_template` `multi_notebook_strategy` 条). 本节详化每 notebook 完整设计.

### 3.1 Notebook 1 — 主训练 (Scope A 个人学习)

| 字段 | 值 |
|------|----|
| 命名 | `SDTM Knowledge Base — Main Training` |
| 目标用户 | 用户本人 (SDTM domain expert) |
| Source 组成 | SDTM **293 md 一对一** 上传 (研究 Q2 确认单源远 <500K words); Pro tier 300 cap, 余 **7 slot** |
| Source 数 | 293 (固定), 占 Pro cap 97.7% |
| Chat mode | **Custom** (Chat custom goals) — 自定 SDTM 专家 system-prompt, ≤10,000 char |
| Chat prompt 重点 | "你是 SDTM 数据标准专家, 回答时必 inline citation 源 md + 章节号, 不在知识库外编造, 遇边界问题坦诚 '未收录'" (实际文本见 `current/instructions_1.md`) |
| Audio Overview 侧重 | Long podcast (Deep Dive format, Longer length), **domain group 粒度**每组 30-45 min, 覆盖 SAFETY / EFFICACY / PK 三组 |
| Mind Map 侧重 | 63 domain 关系全景图, 用于个人快速预览 |
| 分享模式 | 私有 (不分享) |
| A/B 矩阵 | 15 题: 10 smoke v2 + 5 独有 (2 Audio fidelity + 2 Mind Map coverage + 1 Study Guide) |
| PASS 阈值 | ≥13/15 (~87%) AND 每个独有产出 ≥1 精确命中 |

**关键决策点 (Phase 3 前回答)**:
- 一对一 293 source **保留文件名 / 结构**, 有利 citation 精度, 但占满 cap
- 若 Pre-upload audit 发现 ≤2 个 outlier >500K words, 需**拆分**, 拆分后仍应 ≤300 source (有 7 slot 缓冲)
- 若 outlier >7 个, 需**部分合并** (优先合并同 domain 的 part 1/2/3 碎片), 保证 ≤300

### 3.2 Notebook 2 — Scope B Mode A (invite-only 小圈)

| 字段 | 值 |
|------|----|
| 命名 | `SDTM Knowledge Base — Shared Edition (Invite)` |
| 目标用户 | 用户指定 SDTM 小组同事 (≤50 人, personal Gmail 50-cap) |
| Source 数 | ~30 (预留 cap 余量) |
| Chat mode | **Learning Guide** (官方 Socratic, 2025-10-29 blog.google 发布, 全档开放) |
| Audio Overview 侧重 | 短 Audio (The Brief, 10-15 min), 每个核心 concept cluster 一期 |
| Mind Map 侧重 | concept cluster 关系图 + IG 章节, 训练导向 |
| 分享模式 | **Mode A Direct invite** — email 邀请, ≤50 users (personal Gmail, research.md Q7) |
| A/B 矩阵 | 同 15 题 (10 smoke v2 必一致); 独有 5 题侧重 "分享版本可读性" |
| PASS 阈值 | ≥13/15 (~87%) + **Req 变量零丢失** (Q1 红线, 见 §3.2.1) + "一致性校验" (10 smoke v2 业务结论对齐 Notebook 1) |

#### 3.2.1 Source 组成策略 — Req 变量全覆盖 (Q1=0 强制)

**Q1 红线 (用户 2026-04-21 ack)**: Notebook 2 合并到 ≤30 source 必须 **100% 覆盖所有 SDTM `Core=Req` 变量**. 丢 >0 触发 FAIL, 不允许容差.

**SDTM 事实基础** (Phase A A6 extract):
- 63 domain × 3-9 `**Core:** Req` 变量 = **~366 Req 记录**
- 去重通用变量 (STUDYID 63 域, DOMAIN 59 域, USUBJID 55 域, ETCD/IECAT/IETEST/IETESTCD/MIDSTYPE) 后 **独立 Req ~100-120**
- 来源: `knowledge_base/VARIABLE_INDEX.md` (自动生成, 含 Core 列)

**策略转向 — 从 "按 domain 挑" 到 "按 concept cluster 合"**:

| 旧思路 (planner v1) | 新思路 (Q1=0 强制) |
|----|----|
| 9 core domain spec + IG 7 章 + 4 examples ≈ 20 source | 按 **concept cluster** 重分 bucket, 每 source 跨 domain 含相关 Req 变量 |
| 按 domain 粒度挑, 非 core (DD/HO/ML 等) Req 可能全丢 | 按 Req 变量粒度保留, 所有 ~366 Req 至少出现在 1 source |

**Notebook 2 的 ≤30 source 重 bucket 方案** (Phase A A4 产出 concrete 清单):

| # | Source 名 | 内含 domain Req 变量 (示例) | 预计 words |
|---|----------|---------------------------|-----------|
| 1 | `00_navigation.md` | 索引 / 路由提示 / Req 变量速查入口 | ~3K |
| 2 | `01_common_identifiers.md` | STUDYID + DOMAIN + USUBJID + SUBJID + SEQ pattern (所有 63 域共享) | ~5K |
| 3 | `02_patient_demographics.md` | DM + SC 合并 | ~10K |
| 4 | `03_intervention_family.md` | EX + EC + AG + CM + PR + SU 合并 | ~30K |
| 5 | `04_events_family.md` | AE + CE + DS + DV + MH + HO | ~30K |
| 6 | `05_findings_core.md` | LB + VS + EG + PE + QS + IE | ~35K |
| 7 | `06_findings_specialized.md` | MB + MI + MS + MK + PC + PP + OE | ~30K |
| 8 | `07_findings_other.md` | BE/BS/CP/CV/DA/DD/FA/FT/GF/IS/ML/NV/RE/RP/RS/SR/SS/TR/TU/UR 合并 | ~40K |
| 9 | `08_trial_design.md` | TA/TD/TE/TI/TM/TS/TV 7 trial design domains | ~25K |
| 10 | `09_relationships.md` | RELREC + RELSPEC + RELSUB + SUPPQUAL + SE + SV + SM + CO | ~20K |
| 11-16 | `10_ig_chapter_3.md` .. `15_ig_chapter_8.md` | IG ch 3-8 核心段 | 各 ~30K |
| 17 | `16_controlled_terms_core.md` | terminology/core/ 高频 codelist | ~50K |
| 18 | `17_controlled_terms_supplementary.md` | terminology/core/ 低频 + supplementary 摘要 | ~30K |
| 19 | `18_examples_high_freq.md` | AE/CM/DM/LB/VS 5 核心域高频 example | ~40K |
| 20 | `19_assumptions_high_freq.md` | 5 核心域 assumptions | ~25K |
| 21-25 | `20_variable_index.md` .. `24_variable_index_part5.md` | VARIABLE_INDEX.md 拆 5 part | 各 ~25K |
| 26 | `25_cross_domain_variables.md` | 24 通用变量详表 | ~15K |
| 27 | `26_study_design_bridge.md` | DM-TA-TV 跨 domain 桥接 + ARM/ARMCD | ~10K |
| 28 | `27_timing_rules.md` | ISO 8601 + Study Day 计算 | ~10K |
| 29 | `28_rule_decisions.md` | IG ch04 关键判断规则 (CM/AE/MH 拆分 / SAESUB 升级) | ~15K |
| 30 | `29_req_variable_coverage.md` | **审计元 source**: 显式列本 notebook 覆盖的 Req 变量集合 + Q1=0 自证断言 | ~10K |

**总字数估**: ~550K words, 远低于 Pro tier 30 × 500K = 15M cap.

**Req 变量全覆盖审计** (在 A4 产出):
1. `source_mapping.py --audit-req-coverage` flag
2. 每 source 扫 `**Core:** Req` 出现的变量名
3. 30 source 覆盖 `S_covered` vs 全集 `S_full` (~366 记录 / 去重 ~100-120 独立, 来自 A6)
4. `diff = S_full \ S_covered`
5. 判据: `len(diff) == 0` → PASS; `>0` → FAIL, 归档 `failures/A4_req_coverage_attempt_N.md`, 调整 source #29 (`req_variable_coverage.md`) 直到零差集

**Phase 3 信息损失评估**:
- 规则 A N=10 抽检对比 Notebook 1 vs 2 同概念表述 (Exp/Perm 变量 + 业务规则)
- Req 变量零丢失**独立于抽检**走自动化脚本证明 (不靠抽样)

#### 3.2.2 Notebook 2 关键决策点

- **合并策略**: 按 **concept cluster** (非 "domain unit") 分组, 每 source 跨 domain 聚合相关 Req 变量
- **Req 变量全集**: 从 `VARIABLE_INDEX.md` (权威) 抽, 不手工枚举 63 domain
- **审计 source #29**: 元 source, 给 LLM 自我声明 + 给 reviewer 审计依据
- **信息丢失评估**: 规则 A N=10 覆盖 Exp/Perm 变量 + 业务规则; Req 变量零丢失由自动脚本证明

### 3.3 Notebook 3 — Scope B Mode B (public-link 广泛)

| 字段 | 值 |
|------|----|
| 命名 | `SDTM Knowledge Base — Public (Open Link)` |
| 目标用户 | 陌生访客 (持 Google 账号, 无 user cap per research.md — **但见 C2.9 UNVERIFIED**) |
| Source 组成 | **和 Notebook 2 完全相同 ≤30 精选清单** (但因 source 隔离 P12, 必须**独立上传**); **自动继承 Q1=0 Req 变量零丢失红线** (内容一致), 无需独立审计, 但 Phase 3 Task P3.5 末尾加 "Notebook 3 source 一致性快照" 验 Notebook 2/3 内容未漂 |
| Source 数 | ~30 (和 Notebook 2 内容一致但数据完全独立) |
| Chat mode | **Custom** (public 版 system-prompt, ≤10,000 char) — 更 neutral / 免 SDTM jargon, 入门抹平 |
| Chat prompt 重点 | "欢迎, 你正在访问公开 SDTM 知识库. 假设访客是 CDISC 初学者, 回答时先定义术语再展开, 保持客观中立, 不含组织专有观点" (实际文本见 `current/instructions_3.md`) |
| Audio Overview 侧重 | 1-3 期入门导览 Audio (The Brief, 10-15 min), "SDTM 是什么" / "63 domain 概览" / "如何读 IG" |
| Mind Map 侧重 | 和 Notebook 2 相同, 但导出单独 PNG 给公开访客参考 |
| 分享模式 | **Mode B Public link** — 仅 consumer/personal Gmail 能开 (research.md Q7), 需访客持 Google 账号 (无匿名) |
| A/B 矩阵 | 同 15 题; 独有 5 题侧重**"公开陌生访客理解度"** (术语前置定义 / 跨入门完整度) |
| PASS 阈值 | ≥13/15 (~87%) + **Req 变量零丢失** (继承 Notebook 2 审计) + 陌生访客可独立完成 Smoke v2 Q1-Q3 场景应用题 (对比 Notebook 2 同题, 差异 ≤ 20%) |

**关键决策点**:
- **C2.9 UNVERIFIED (Phase 3 实测)**: Mode B owner 是否套用 Mode A 的 50-cap? Writer#2 从 "Anyone with a link" 语义推断无 cap, 但官方 Help 未区分 → Phase 3 Task P3.7 挂实测 I8
- 若 I8 实测发现 Mode B 也有 50-cap, Scope B 广泛分享前提崩塌 → fallback 到 **workflow_replication** (打包 uploads_public/ + UPLOAD_TUTORIAL § Notebook 3 章节让接收者自建)
- Chat prompt 需**禁用** "你可引用 IG v3.4 第 N 章" 这种内部 cite 约定, 改为 "引用 source 文件中具体段落"

### 3.4 跨 notebook 一致性审查 (Phase 4 独立段)

**原则**: 三 notebook 的 A/B 10 smoke v2 **必须一致** (业务答案对齐, 只有详略差异); 独有 5 题才允许每 notebook 各自侧重. **Req 变量零丢失红线 (Q1)** 跨 Notebook 2 和 3 双向生效 (Notebook 3 继承 Notebook 2).

**审查矩阵** (Phase 4 Task 4.3 产出 `dev/ab_reports/consistency_review.md`):

| 对比维度 | 期望 | FAIL 判据 |
|---------|------|----------|
| 10 smoke v2 核心事实 | 三 notebook 答案业务结论一致 | 某 notebook 给出与另两个明显矛盾的事实 (如 AESEV 档位错) |
| **Notebook 1 vs 2 Req 变量覆盖** | Notebook 2 100% 覆盖 Notebook 1 含的 Req 变量全集 (A6 extract + A4 审计保证) | **丢失 >0 Core=Req 变量触发 FAIL** (Q1 红线, 零容忍) |
| Notebook 1 vs 2 Exp/Perm 信息 | Exp/Perm 变量 + 业务规则允许详略差, 不允许**语义错位** | 某 Exp 变量语义被改写致与源 md 矛盾 (N=10 抽检 FAIL ≥2) |
| Notebook 2 vs 3 措辞 | 2 Socratic 引导 / 3 neutral 定义; 同事实不同呈现 | 3 的 public 版引入 Notebook 2 没有的 (臆造) 事实 |
| **Notebook 1 vs 3 综合 (新)** | "1 vs 2" + "2 vs 3" 组合; Notebook 3 覆盖所有 Req (继承) + public 措辞合规 | 两侧任一行 FAIL 判 1 vs 3 FAIL |
| Audio / Mind Map 对齐 | 三 notebook 生成物事实不冲突 | Audio 介绍 "AE 域", Mind Map 缺 AE 节点 |

**术语修正 (R3 维度 4(b))**: Notebook 1 (293 source) → Notebook 2 (~30 source) 是**文件数压缩 ~90%** (293→30); **内容字数压缩 ~82%** (~550K vs ~3M). 规则 A 抽检的是**内容语义保全**, 不是文件数.

**规则 A N 数规格** (按 `_spec/06_review.md` 抽样表): Notebook 2 合并涉源 293 md → 属**大批** (>200) → **reviewer N=15 + 主控 N=10, 不重叠**. 判据: 样本源文本核心业务含义是否在 Notebook 2 合并 source 中可检索, FAIL ≥2 触发 P10 归因.

**Q1=0 零丢失与 Rule A 抽检关系**:
- Q1=0 边界不变 (仍对 Exp/Perm/业务规则抽样)
- Req 变量零丢失**独立于抽检**, 走自动化脚本证明 (A4 产出 `req_vars_coverage_audit.md` diff==0)
- 规则 A 抽检**不必覆盖 Req 变量** (因已自证)

---

## §4 A/B 矩阵设计 (Phase 4 执行预览)

### 4.1 标准 10 题 (共享)

**直接引用** `ai_platforms/SMOKE_QUESTIONS_V2.md` 全文:

| # | 题名 | 维度 |
|---|------|------|
| Q1 | 合并用药同服两种降压药, CM 拆分 | I 场景应用 |
| Q2 | AE 升 SAE, 住院 Serious 子变量 | I 场景应用 |
| Q3 | 实验室 HbA1c 超标, LB 变量填写 | I 场景应用 |
| Q4 | AESEV vs CTCAE Grade 映射 | II 规则判断 |
| Q5 | PK LLOQ 以下值记录 | II 规则判断 |
| Q6 | DM.ARMCD vs ARM + 换组 | II 规则判断 |
| Q7 | 病史"高血压 + 仍服药" MH/CM 拆 | III 映射 |
| Q8 | 时间精度 ISO 8601 + Study Day | III 映射 |
| Q9 | SUPPAE QNAM/QLABEL/QVAL 示例 | IV 域间鉴别 |
| Q10 | RELREC vs SUPP-- 选择 | IV 域间鉴别 |

**原文规则 (SMOKE_QUESTIONS_V2.md)**: 题目**原文复制**, 禁改字 / 禁加文件名提示 / 禁加位置描述 (三 notebook 完全一致以便对比).

### 4.2 独有 5 题 (本平台, 每 notebook 各自一版)

| # | 题型 | 模板题干 | PASS 判据 |
|---|------|---------|----------|
| P1 Audio fidelity | **Audio Overview 事实保真** | 生成本 notebook 任意一个核心 domain (如 AE) 的 Deep Dive Audio Overview, 记长度, 人工听完, 勾事实错误数 | 0-1 事实错误 = PASS; ≥2 = FAIL (hallucination) |
| P2 Audio language | **Audio 英文源 → 中文输出** (I4 carry-over) | 同 P1 domain, Custom prompt 指定 "用中文播讲", 评估术语准确率 + 口音 / glitch | ≥80% 术语准确 (如 "严重不良事件" 对应 SAE, 不误译) |
| P3 Mind Map coverage | **Mind Map 跨 domain 连线** | 提问 "SDTM 跨域关系 RELREC 涉及哪些域", 观察 Mind Map 是否全部列出 + 是否遗漏 | 覆盖 AE/CM/MH/LB 等典型 RELREC 场景 ≥5 个 |
| P4 Mind Map depth | **Mind Map 长源深层衰减** (I4 carry-open 社区观察) | 对 Notebook 1 的长 md (最大一个, wc -w 找), 看 Mind Map 是否覆盖该源末尾概念 | 末尾 20% 内容至少有 1 节点呈现 |
| P5 Study Guide layering | **Study Guide 分层** | 提问 "给我 DM 域的 Study Guide", 检查 Standard → IG → Examples 三层覆盖 | 三层各 ≥1 条目 |

### 4.3 矩阵规格 + PASS 判定

| 项 | 值 |
|----|----|
| 每 notebook 题数 | 15 (10 standard + 5 unique) |
| Notebook 数 | 3 |
| **总题次** | **45** |
| Per-notebook PASS 阈值 | ≥13/15 (≥87%) business correct AND 每个独有产出 ≥1 精确命中 |
| 跨 notebook 一致性阈值 | 10 smoke v2 业务结论对齐, 允许详略差 (见 §3.4) |
| Rule A 抽检触发? | Yes (Notebook 2/3 合并压缩 >50%), 规则 A N=10 独立抽检 |

### 4.4 Audio 题 rate limit 分布 (P11 强制)

Pro tier audio 20/day, 3 notebook × 2 audio 题 (P1 + P2) = 6 audio 生成. **单日可完成**, 但若失败 retry ≥10 次就超 cap. 保守方案:

| 日次 | Notebook | Audio 题 | 预算 audio/day |
|------|---------|---------|--------------|
| Day 1 | Notebook 1 | P1 + P2 | 2 + retry 预算 8 |
| Day 2 | Notebook 2 | P1 + P2 | 2 + retry 预算 8 |
| Day 3 | Notebook 3 | P1 + P2 | 2 + retry 预算 8 |

若 Day 1 顺利 (2/2 PASS), Day 2 可并 Notebook 2 + 3, 缩为 2 天.

---

## §5 Phase 3 落地前置动作 (进 Phase 3 前完成, 4 条)

### 动作 1 — Pre-upload audit (强制, §6 Task P3.0 对应)

- **命令**: `find knowledge_base -name '*.md' -exec wc -w {} \;` → 排序 → Top 5 outlier
- **判据**: 所有 md <500K words (Pro tier 单源 cap). SDTM 单 md 估计 <10K words, 预计 Top 5 也远 <500K, 假阳性低但必做
- **输出**: `dev/evidence/pre_upload_audit.md`, 含:
  - Top 5 outlier md 名 + words 数
  - 总 words 汇总 (所有 293 md 之和, 对 Pro cap 150M 的占比)
  - PASS / FAIL 判定 (若有单 md >500K 必拆分或合并后重测)
- **Checkpoint 级别**: **hard** (用户 ack 后才进 Task P3.1)

### 动作 2 — Chat mode 决策固化

- **目标**: 三 notebook 的 Chat mode 决策在 Phase 3 前写死进 `current/instructions_N.md` (N=1/2/3)
- **产物**:
  - `instructions_1.md`: Custom mode SDTM 专家 prompt (≤10,000 char, 含角色 / 引用规范 / 边界声明 / 零臆造要求)
  - `instructions_2.md`: Learning Guide mode (无需 10K char, 官方模板; 本文件记补充教学偏好)
  - `instructions_3.md`: Custom mode public 版 (≤10,000 char, 入门抹平术语)
- **Checkpoint 级别**: **soft** (Phase 3 初期可微调, 不阻塞)

### 动作 3 — Notebook 1 source 映射清单

- **决策点**: "**293 一对一上传**" vs "**少量合并到 ≤300**"
- **默认策略**: 一对一, 余 7 slot. 若 Pre-upload audit 发现 outlier 需拆分, 转为"部分拆分 + 部分合并到 ≤300"
- **产物**: `dev/evidence/source_mapping.md` 含 293 → source 映射表 + 拆分/合并策略说明
- **Checkpoint 级别**: **hard** (一对一还是合并, 决定 Notebook 1 上传脚本逻辑)

### 动作 4 — Notebook 2/3 精选清单 (**含 Req 变量全覆盖审计, Q1=0 红线**)

**注**: 本动作已在 **§2.5 Phase A A4** 展开详化, 本段保留作 §6 Task 向后兼容索引. 核心变更:

- **筛选策略从 "按 domain 挑" 改为 "按 concept cluster 重 bucket"** (Q1=0 技术必要)
- 具体 bucket 方案见 **§3.2.1 30 source 表格**
- Req 变量全覆盖审计脚本见 §2.1 `cluster_req_variables.py` + `source_mapping.py --audit-req-coverage`
- Phase A A6 (`extract_req_vars.py`) 是 A4 的前置

- **产物**: 同 A4 (`current/uploads_invite/MANIFEST.md` + `uploads_public/MANIFEST.md` 两清单内容一致 + `dev/evidence/req_vars_coverage_audit.md`)
- **Checkpoint 级别**: **hard** (Req 变量零丢失红线, gate 到 §6 Task P3.4)

---

## §6 Phase 3 Task 分解 (8 Tasks)

按 _spec/04_plan.md Task 模板. 每 Task 含: 目标 / 输入 / 输出 / Checkpoint 级别 / 失败归档路径 / 实测证据要求. **注**: 进 Phase 3 前必须完成 §5 全部 4 动作.

---

### Task P3.0 — Pre-upload audit + source 映射 (Phase 3 第一任务)

- **目标**: 执行 §5 动作 1 + 动作 3 + 动作 4, 固化 source 映射
- **输入**: `knowledge_base/**/*.md` (293 md); Pre-upload audit 脚本; 用户 Rule E ack
- **输出**:
  - `dev/evidence/pre_upload_audit.md` (Top 5 outlier + 500K words 校验 PASS/FAIL)
  - `dev/evidence/source_mapping.md` (Notebook 1 源映射决策)
  - `current/uploads_invite/MANIFEST.md` + `current/uploads_public/MANIFEST.md` (Notebook 2/3 清单, 内容一致)
- **Rule D 派发**: executor (writer) + code-reviewer (独立复核 manifest 结构完整)
- **Checkpoint 级别**: **hard** (用户 ack 后才进 P3.1)
- **操作次数估算**: 脚本运行 2 次 (pre_upload_audit.py + source_mapping.py); 无 Web UI 上传
- **工时估算** (Q2 保守上界): **1-2 小时** (实为 Phase A A1+A3 索引入口, 主要工时已在 Phase A)
- **prerequisite_tasks**: Phase A A1 + A3 + A4 + A5 + A6 全部 PASS
- **parallel_with**: — (Phase 3 入口, 串行)
- **失败归档**: `dev/evidence/failures/task_P3.0_attempt_<X>.md`
- **实测证据要求**: wc -w 输出原始日志 + 映射决策 rationale 文本

---

### Task P3.1 — Notebook 1 上传 + indexing smoke test (C2.6/I1 前置 gate)

- **目标**: 在 NotebookLM web UI 创建 Notebook 1, 执行 source 映射决策上传 293 source, 做 I1 indexing 实测
- **输入**: Notebook 1 source 清单 (来自 P3.0); user's Google AI Pro 账号 Web UI
- **输出**:
  - Notebook 1 在线 (Web UI 截图 + source 数确认 = 预期)
  - `dev/evidence/indexing_smoke_test.md` (I1 产物: 单 md / 单 PDF / 批量三场景的 indexing 耗时 + 独有关键词召回测试结果)
  - 若有 silent fail source, 列出并 re-upload
- **Rule D 派发**: executor (用户侧+MCP 自动化, 可用 computer-use / claude-in-chrome; 若阻塞 fallback 手动) + verifier (独立核对召回)
- **Checkpoint 级别**: **hard** (indexing 若未 PASS 不进 P3.2; indexing 验证只有"点 source tile 预览内容"这一条官方可靠路径 per Q5)
- **操作次数估算**: Web UI 上传最坏 **293 次** (单文件点击) / 最好 **3-10 次** (A5 batch PASS 文件夹拖); indexing smoke test 5 次关键词提问; retry 预算 ≤10 次
- **工时估算** (Q2 保守上界): Web UI batch PASS = **2-3 小时**; 不支持 batch = **3-5 小时** (293 × 30s = 2.5h + indexing); Q2 保险 2x = **5-10 小时** (跨 1-2 天)
- **prerequisite_tasks**: P3.0 PASS
- **parallel_with**: Phase A A2 (instructions_1.md 撰写) 可在 indexing 等候时间跑
- **失败归档**: `dev/evidence/failures/task_P3.1_attempt_<X>.md` (特别记 silent fail 的 source 列表)
- **实测证据要求**: 对 5 个独有关键词分别提问召回时间 + citation 是否 inline

---

### Task P3.2 — Notebook 1 Chat custom goals 配置 + Smoke A/B (10 题)

- **目标**: 注入 `instructions_1.md` Custom mode prompt; 跑 10 smoke v2 题 (不含独有 5 题)
- **输入**: Notebook 1 (已 indexed); `current/instructions_1.md`
- **输出**:
  - Chat mode = Custom 已配置 (UI 截图)
  - `dev/ab_reports/notebook_1_smoke.md` (10 题答案 + PASS/PARTIAL/FAIL 评分, 按 SMOKE_QUESTIONS_V2.md PASS 判据)
- **Rule D 派发**: executor (提问 + 记答案) + critic (独立业务判定 PASS/FAIL, **必须对照源 md 核对**, 规则 A N=5 独立抽检)
- **Checkpoint 级别**: **hard** (若 <8/10 PASS, 走 P10 归因, 可能触发 instructions_1.md 重写)
- **操作次数估算**: Chat mode UI 配置 1 次 + 10 题 × (1 提问 + critic 判定 1 次) = ~20 次
- **工时估算**: **2-3 小时** (10 题 × ~10 分钟/题含源 md 核对)
- **prerequisite_tasks**: P3.1 PASS (Notebook 1 已 indexed)
- **parallel_with**: P3.4 的 instructions_2.md 最终校对 (不冲突)
- **失败归档**: `dev/evidence/failures/task_P3.2_attempt_<X>.md`
- **实测证据要求**: 每题原始答案全文 + critic 判定理由

---

### Task P3.3 — Notebook 1 独有 5 题 + Audio rate limit 分布 (P11)

- **目标**: 跑 Notebook 1 独有 5 题 (P1-P5), P1/P2 Audio 题 Day 1 集中
- **输入**: Notebook 1; Audio Custom prompt 模板 (中英文各一)
- **输出**:
  - 2 audio 生成 (P1 英文 Deep Dive + P2 中文版)
  - Mind Map PNG 导出
  - Study Guide 输出
  - `dev/ab_reports/notebook_1_unique.md` (5 题评分)
- **Rule D 派发**: executor + critic (audio 事实保真人工听, mind map 节点对照源, study guide 三层校验)
- **Checkpoint 级别**: **soft** (若 P4 mind map depth 题 FAIL, 记 carry-over, 不阻塞 P3.4)
- **操作次数估算**: Audio 生成 2 + retry 预算 8 + Mind Map 导出 1 + Study Guide 1 + 5 题 × ~3 = ~27 至 ~35 次
- **工时估算** (Q2 保守): Audio 1.5-2h + 5 题 1-2h = **2.5-4 小时** Day 1; Q2 保险 2x: **5-8 小时** (可跨 2 天)
- **prerequisite_tasks**: P3.2 PASS
- **parallel_with**: P3.4 Notebook 2 上传 (两 tab 交替; Audio 后台生成 + 你跑 Notebook 2 smoke)
- **失败归档**: 同上
- **Rate limit 预算**: Day 1 消耗 audio 2 + retry 8 = 10/20 day cap

---

### Task P3.4 — Notebook 2 上传 + Learning Guide 配置 + 15 题 A/B (P12 分别独立上传)

- **目标**: 创建 Notebook 2, 独立上传 ≤30 精选 (P12: source 不能从 Notebook 1 引用, 必须重新上传), 配 Learning Guide mode, 跑 15 题
- **输入**: `current/uploads_invite/MANIFEST.md`; Notebook 2 Chat mode = Learning Guide (官方模板, 无需 10K char prompt)
- **输出**:
  - Notebook 2 在线 (≤30 source)
  - 15 题 A/B (10 smoke + 5 unique) → `dev/ab_reports/notebook_2_ab.md`
  - 规则 A N=10 抽检 (Notebook 2 压缩率 >50%, 强制触发) → `dev/evidence/notebook_2_audit.md`
- **Rule D 派发**: executor + code-reviewer (规则 A 主控抽检不同 subagent_type)
- **Checkpoint 级别**: **hard** (若 <87% PASS 或规则 A FAIL 样本 ≥2, 走 P10 归因)
- **操作次数估算**: Notebook 创建 1 + source 上传 ≤30 (batch PASS ~1-3 / 不支持 ≤30) + Learning Guide mode 1 + 15 题 A/B × ~3 = ~45 chat + 规则 A N=25 抽检 + Audio 2 + retry 5 = ~95 次 (最坏)
- **工时估算** (Q2 保守): Web UI 上传+indexing 1-2h + 15 题 A/B + Audio 4-6h + 规则 A 抽检 3-4h + Req 审计 0.5h = **Day 2: 8-12 小时**; Q2 保险 2x: **16-24 小时** (跨 2-3 天)
- **Req 变量零丢失审计 (新, Q1 红线)**: Task 完成前必跑 `source_mapping.py --audit-req-coverage --notebook 2`, `diff==0` 方 PASS; 若 diff > 0 归档 `failures/task_P3.4_attempt_N.md` + 立即修 source #29 (`req_variable_coverage.md`) 重上传
- **prerequisite_tasks**: P3.3 至少 soft PASS (或跳) + Phase A A4 Req 审计 PASS
- **parallel_with**: P3.5 Notebook 3 上传 (若 A5 不支持 batch 严重耦合, 此时不推荐并行)
- **失败归档**: `dev/evidence/failures/task_P3.4_attempt_<X>.md`
- **Rate limit 预算**: Day 2 消耗 audio 2 (P1 + P2 Notebook 2 版)

---

### Task P3.5 — Notebook 3 上传 + Custom public prompt + 15 题 A/B (P12 再次独立上传)

- **目标**: 创建 Notebook 3, **独立上传同 ≤30 精选** (P12, 不能从 Notebook 2 引用), 配 Custom mode + public prompt, 跑 15 题
- **输入**: `current/uploads_public/MANIFEST.md` (同 Notebook 2 内容); `current/instructions_3.md`
- **输出**:
  - Notebook 3 在线 (≤30 source, 独立索引, **和 Notebook 2 source 完全不共享**)
  - 15 题 A/B → `dev/ab_reports/notebook_3_ab.md`
  - 规则 A N=10 抽检 (内容和 Notebook 2 同但 chat mode 不同, 抽检点是"public prompt 是否改变事实输出")
- **Rule D 派发**: executor + critic (public 版是否引入臆造 / 抹平过头丢失信息两个维度判)
- **Checkpoint 级别**: **hard** (同 P3.4)
- **操作次数估算**: 类 P3.4 但 Chat mode 不同; ~90 次
- **工时估算** (Q2 保守): **Day 3: 8-12 小时** (同 P3.4 结构, Custom prompt 撰写 +0.5h); Q2 保险 2x: 跨 2-3 天
- **Req 变量一致性快照 (新, Q1 连锁)**: Task 完成前跑 `diff current/uploads_invite/MANIFEST.md current/uploads_public/MANIFEST.md` 期望空 diff, 证 Notebook 2/3 source 清单未漂
- **prerequisite_tasks**: P3.4 PASS (继承 Notebook 2 清单) + A4 Req 审计已 PASS (Notebook 3 不必重审)
- **parallel_with**: P3.4 Audio 后台生成阶段 (Audio 异步, 你跑 Notebook 3 上传)
- **失败归档**: 同上
- **Rate limit 预算**: Day 3 消耗 audio 2 (或若 Day 2 提前完成, 合并到 Day 2)

---

### Task P3.6 — Mode A invite 分享功能验证 (Notebook 2)

- **目标**: 在 Notebook 2 上开 Mode A invite, 邀请测试用户 (用户自己的第二 Gmail 或同事), 验证 view + chat 权限工作
- **输入**: Notebook 2 (P3.4 完成); 测试 email
- **输出**:
  - Share 面板截图 (邀请已发送)
  - 测试用户登录访问截图 + chat 问一题验证 (不需完整 A/B, 只验连通)
  - `dev/evidence/mode_a_invite_test.md`
- **Rule D 派发**: executor + verifier
- **Checkpoint 级别**: **soft** (功能验证, 非 A/B 一部分)
- **操作次数估算**: 1 invite 发送 + 1 测试 email 登录 + 3 题 chat 验证 = ~5 次
- **工时估算**: **30 分钟 - 1 小时**
- **prerequisite_tasks**: P3.4 PASS + 测试 email (第二 Gmail 账号)
- **parallel_with**: P3.5 的 Audio 生成阶段 (两边不冲突)
- **失败归档**: 同上

---

### Task P3.7 — Mode B public link 分享 + I8 50-cap 实测 (C2.9)

- **目标**: 在 Notebook 3 上开 Mode B public link, 执行 I8 实测 (C2.9): 尝试 >50 访客 (可模拟或用文档 infer) 判断 Mode B owner 是否套用 50-cap
- **输入**: Notebook 3 (P3.5 完成); 公开链接入口
- **输出**:
  - Public link URL
  - 50-cap 实测结果文档 `dev/evidence/mode_b_cap_test.md`: (a) 实际 cap 数字 (若能触发); (b) 若无法直接触发, 记 NotebookLM UI 有无 "user cap" 字段; (c) 官方文档 re-survey 结论
  - **若 I8 发现 Mode B 也受 50-cap** → Scope B 广泛分享前提崩塌, 立即 carry-over 到 Phase 5 workflow_replication fallback 设计
- **Rule D 派发**: executor + critic
- **Checkpoint 级别**: **hard** (影响 Scope B 定义, 用户 ack 后 Phase 4 推进)
- **操作次数估算**: Share 面板 1 + I8 实测 ~5 (无法 50+ 真访客, 改 Web UI 字段观察 + 官方 Help re-survey + 第二 Gmail 模拟访问测) + I2 re-index 可选 ~3 = ~7-10 次
- **工时估算**: **1-2 小时** (I2 可选加 1 小时)
- **prerequisite_tasks**: P3.5 PASS
- **parallel_with**: P3.8 跨 notebook 汇总的准备阶段 (读 3 份 A/B 报告不冲突)
- **失败归档**: 同上
- **其他 carry-over 实测**: I5 (访客问答是否回写 owner chat history, 用第二账号测试); I2 re-index (可选, 若 Phase 3 内有时间)

---

### Task P3.9 — I3 Mind Map / Study Guide 刷新节奏 + I4 长源衰减实测

- **目标**: 补 R3 遗漏的 I3 (R1 carry-over "添加 source 后 Mind Map 自动/手动刷新") + 强化 I4 (Mind Map 长源深层衰减). planner v1 完全遗漏, Writer #4 新增
- **输入**: Notebook 1 (Mind Map, P3.3 产出); Notebook 2/3 (Mind Map); 1 额外测试 md (来自 knowledge_base/ 但未上传)
- **实测 4 场景**:
  1. **I3a (Notebook 1 增量)**: 加 1 新测试 source, 观察 Mind Map 是否 (i) 自动刷新 / (ii) 显示 "点击重新生成" / (iii) 需手动删除旧图重生
  2. **I3b (Notebook 2 增量 — concept cluster)**: 同 I3a 但对 concept cluster 合并 source 做测
  3. **I3c (Study Guide 刷新)**: 同 I3a/b, 对 Study Guide 做测
  4. **I4 (长源深层衰减)**: 对 Notebook 1 最长 md (A1 Top 5 第一), 用 Mind Map 深层节点 (3+ 级) 提问, 观察该 md 末尾 20% 是否有节点
- **输出**: `dev/evidence/mind_map_refresh_test.md` (4 场景 × PASS/FAIL + UI 截屏 + 衰减程度)
- **Rule D 派发**: executor + verifier (独立观察 UI 行为)
- **Checkpoint 级别**: **soft** (R3 建议; 记录数据供 Phase 7 KG 参考, 不阻塞 P3.8 一致性汇总)
- **操作次数估算**: 4 场景 × (1 操作 + 1 观察) + I4 Mind Map 深挖 ~10 节点 = ~18 次
- **工时估算**: **1-2 小时**
- **prerequisite_tasks**: P3.3 PASS (Notebook 1 Mind Map) + P3.4 PASS (Notebook 2 Mind Map)
- **parallel_with**: P3.6 Mode A invite 验证 (两独立操作); 与 P3.7 I8 实测时序接近
- **失败归档**: `dev/evidence/failures/task_P3.9_attempt_<X>.md`
- **Carry-over 去向**: I3 自动刷新 = FALSE (需手动重生) 则 UPLOAD_TUTORIAL § 6 必加警示 + Phase 7 RAG/KG 考虑替代

---

### Task P3.8 — 跨 notebook 一致性 + 45 题次汇总

- **目标**: 汇总 3 notebook × 15 题 = 45 题次结果, 做跨 notebook 一致性审查 (§3.4 矩阵)
- **输入**: `notebook_1_ab.md` + `notebook_2_ab.md` + `notebook_3_ab.md`
- **输出**:
  - `dev/ab_reports/consistency_review.md` (见 §3.4 审查矩阵)
  - `dev/test_results.md` (45 题次完整记录, per-题 per-notebook 评分表)
- **Rule D 派发**: 主控独立抽检 (不同 subagent_type, 建议 `oh-my-claudecode:critic` 或 `pr-review-toolkit:code-reviewer`)
- **Checkpoint 级别**: **hard** (跨 notebook 一致性 FAIL 可能要求重做某 notebook, 用户 ack 后进 Phase 4)
- **操作次数估算**: 读 3 份 ab_reports + consistency_review 产出 + 按 §3.4 矩阵逐行核 = ~20 次人工核对
- **工时估算**: **3-5 小时** (依 15 × 3 = 45 题次对照密度)
- **I6 chat 输入长度顺带实测**: 50K / 200K / 500K words 三级用 Notebook 1 chat 提问, 记最大输入上限
- **prerequisite_tasks**: P3.4 + P3.5 + P3.7 + P3.9 全 PASS
- **parallel_with**: — (串行, 最后一步)
- **失败归档**: 同上

---

### Task 清单 Checkpoint 级别汇总

| Task | Checkpoint |
|------|-----------|
| P3.0 Pre-upload audit + source 映射 | **hard** |
| P3.1 Notebook 1 上传 + indexing smoke test | **hard** |
| P3.2 Notebook 1 Chat mode + 10 smoke | **hard** |
| P3.3 Notebook 1 独有 5 题 | **soft** |
| P3.4 Notebook 2 上传 + 15 题 | **hard** |
| P3.5 Notebook 3 上传 + 15 题 | **hard** |
| P3.6 Mode A invite 验证 | **soft** |
| P3.7 Mode B public link + I8 实测 | **hard** |
| P3.9 (新) I3 Mind Map / Study Guide 刷新 + I4 长源衰减 | **soft** |
| P3.8 跨 notebook 一致性 + 45 题次汇总 | **hard** |

**Hard checkpoint 总计**: 6 次 (符合 v1 G4 教训, 显式写出不隐式推进).

### Phase 3 Task 工时汇总 (Q2 不赶时间, 取保守上界)

| Task | 估算工时 (下界) | 估算工时 (Q2 保险 2x 上界) | 关键 rate limit / checkpoint |
|------|---------------|---------------------------|---------------------------|
| P3.0 Pre-upload audit + source 映射 | 1 小时 | 2 小时 | 引 Phase A A1+A3+A4 |
| P3.1 Notebook 1 上传 + indexing | 2-5 小时 | 10 小时 | A5 batch 能力决定; hard |
| P3.2 Notebook 1 Chat + 10 smoke | 2-3 小时 | 6 小时 | hard |
| P3.3 Notebook 1 独有 5 题 | 2.5-4 小时 | 8 小时 | Audio 20/day cap 单日 |
| P3.4 Notebook 2 上传 + 15 题 + Req 审计 | 8-12 小时 | 24 小时 | hard + Req 零丢失 gate |
| P3.5 Notebook 3 上传 + 15 题 | 8-12 小时 | 24 小时 | hard |
| P3.6 Mode A invite 验证 | 0.5-1 小时 | 2 小时 | soft |
| P3.7 Mode B public + I8 | 1-2 小时 | 4 小时 | hard (I8 决 Scope B 可行性) |
| P3.9 (新) I3/I4 Mind Map 实测 | 1-2 小时 | 4 小时 | soft |
| P3.8 一致性 + 45 题汇总 | 3-5 小时 | 10 小时 | hard |
| **合计** | **29-47 小时** | **~94 小时** | — |

**换算天数**:
- **急速模式** (理想, A5 batch PASS, 无 rate limit 堆积): ~29h / 6h 日均 = **5 天**
- **标准模式** (中位, A5 部分支持): ~40h / 6h 日均 = **7 天**
- **Q2 保险模式** (保守, 无 batch + 多 retry): ~94h / 6h 日均 = **16 天**

Q2 用户明示 "不限工时, 质量第一" — 本 PLAN 按**标准模式 7 天**规划, 允许 Q2 保险模式 16 天兜底. **不要求 1 天完成**.

---

## §7 Phase 4 审查设计 (Phase 3 后)

### 7.1 三 lane

| Lane | 角色 | subagent_type 候选 | 产物 |
|------|------|-------------------|------|
| Writer | 执行 A/B + 归纳 | executor (P3.2-P3.8 已覆盖) | `dev/ab_reports/*.md` |
| Reviewer #1 (事实核对) | 独立对照源 md 校对 45 题次业务 PASS | **第 7 种 subagent_type** (Phase 4 时选, 建议 `code-reviewer` 或 `oh-my-claudecode:verifier`) | `dev/evidence/phase4_reviewer1.md` |
| Reviewer #2 (多视角) | critic 角度看跨 notebook 一致性 + Scope B fallback | **第 8 种 subagent_type** (建议 `oh-my-claudecode:critic` 或 `pr-review-toolkit:code-reviewer`) | `dev/evidence/phase4_reviewer2.md` |

**Rule D 占位**: 本 PLAN **不定死** subagent_type 选择 — Phase 3 完成后主 session 视 subagent_type 使用情况动态分配, 保证 Phase 4 两个 reviewer 和 Phase 1/2/3 已用的 6 种互斥.

**已用 subagent_type**: `general-purpose` (W1 research), `oh-my-claudecode:verifier` (R1), `oh-my-claudecode:executor` (W2 research / 可能 Phase 3 复用), `oh-my-claudecode:critic` (R2 / 可能 Phase 3 复用), `oh-my-claudecode:planner` (本 PLAN Writer), 待 **R3 Phase 2 审**.

**Phase 3/4 可用候选** (避免前 5 种):
- `code-reviewer`, `oh-my-claudecode:code-reviewer`, `feature-dev:code-reviewer`, `pr-review-toolkit:code-reviewer`
- `feature-dev:code-architect`, `oh-my-claudecode:writer`
- `superpowers:verifier` 等

### 7.2 跨平台对比段 (Phase 4 Task 4.2)

**目标**: NotebookLM A/B 结果 (10 smoke v2) vs Claude Projects / ChatGPT GPTs / Gemini Gems 的 10 smoke v2 对比

**输入**:
- `ai_platforms/notebooklm/dev/ab_reports/notebook_1_ab.md` (Notebook 1 是三 notebook 里最接近 "全量" 的)
- `ai_platforms/claude_projects/dev/ab_reports/STAGE_V2.6_AB_REPORT.md` (Claude 终态)
- `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v2_results.md` (若 Phase 6.5 已完成)
- `ai_platforms/gemini_gems/dev/evidence/smoke_v2_results.md` (同)

**输出**: `docs/cross_platform_compare.md`, 结构:

- 4 平台 10 题并排 (题 × 平台 matrix)
- 每题 PASS/FAIL + 差异分析
- 平台独有优势观察: NotebookLM inline citation / Audio / Mind Map; Claude RAG 曲线; ChatGPT 20 文件硬限下的压缩; Gemini 1M 窗口全量)
- 回灌 `_template/` 的新补丁候选 (见 §9)

### 7.3 Phase 4 退出条件

- 45 题次 ≥ 39 (87%) PASS
- 三 notebook 一致性审查 PASS
- 两个 reviewer subagent 独立验证 PASS
- cross_platform_compare.md 完成
- 用户 ack

---

## §8 Phase 5 收束三件套

### 8.1 `docs/RETROSPECTIVE.md` (规则 C 强制)

**三段式**:

1. **保留下来的做法 (R 段)** — 例: Phase 0 Rule E 早 ack / Phase 1 四轮 subagent 隔离链 / Pre-upload audit 强制 / Chat custom goals Custom mode 作 system prompt 退化
2. **必须补上的缺口 (G 段)** — 例: workflow_replication fallback 设计需专门 retro 段 / 三 notebook 独立上传成本预估偏差
3. **关键决策复盘 (D 段)** — 例: 为何选 Learning Guide 而非 Custom 给 Notebook 2 / 为何一对一上传 293 而非合并

**独立审阅**: 主控写完后用 `oh-my-claudecode:writer-reviewer` 或任一未用 subagent_type 复核 (规则 D + _spec/06_review.md §RETROSPECTIVE 的独立审阅 段要求).

### 8.2 `docs/handoff.md` (若 Phase 7 启动)

- 传递 6 条 Phase 7 actionable insight (参考 `claude_projects/docs/phase7_handoff.md` 格式)
- 标 I1-I9 实测结果 + Unverified 7 条处置 (哪些消除 / 哪些仍 UNVERIFIED)

### 8.3 `current/UPLOAD_TUTORIAL.md` (10 章节用户视角)

按 `_spec/09_closure.md` 10 章节要求, 但因 **multi-notebook 架构**需覆盖 3 notebook, 分章节组织:

| 章节 | 内容 |
|------|------|
| 1 前置准备 | Google AI Pro 订阅状态确认 + Personal Gmail 账号 (因 Mode B 要求) |
| 2 建 Notebook 1 (主训练) | 创建 + 上传 293 md + Custom mode prompt |
| 3 建 Notebook 2 (Invite) | 创建 + 独立上传 ≤30 精选 + Learning Guide + Mode A invite |
| 4 建 Notebook 3 (Public link) | 创建 + 独立上传 ≤30 精选 (提示 P12 source 隔离必重传) + Custom mode + Mode B open |
| 5 Smoke Test (10 题) | 三 notebook 各跑一遍 |
| 6 回归 / 更新 | source 修改 re-index (I2 结果) / 批量更新流程 |
| 7 排错 | Indexing silent fail 处理 / Audio hallucination 记录 / Mind Map 导出 |
| 8 升降级 | Pro → Ultra / Plus / Standard 降级路径 + source cap 调整 |
| 9 团队协作 | Mode A invite 扩容到 50 / 超 50 走 workflow_replication |
| 10 **Scope B Mode B workflow_replication fallback** | **强调**: 若 Mode B 因 I8 实测受 50-cap, 打包 `current/uploads_public/*` + 本 TUTORIAL § 3-5 让接收者自建 |

---

### 8.4 失败应急集中表 (R3 维度 1 指缺失)

散落在 §3.3 / §6 各 Task / §8.3 的失败模式和 fallback 汇总到此表, Phase 3 执行遇失败**先查本表**再查 Task 详情.

| # | Task / 场景 | 失败模式 | 触发信号 | 归档路径 | 响应 / Fallback |
|---|------------|---------|---------|---------|---------------|
| 1 | Phase A A1 Pre-upload audit | Top 5 outlier md >500K words | wc -w > 500,000 | `failures/A1_attempt_N.md` | 拆分大 md (按 section) 或合并小 md |
| 2 | Phase A A4 Req 审计 | Req 变量 diff > 0 (丢失 >0) | `source_mapping.py --audit-req-coverage` 输出 diff | `failures/A4_req_coverage_attempt_N.md` | 扩 source #29 `req_variable_coverage.md` 直至 diff=0; 不允许放行 |
| 3 | Phase A A5 batch capability | Web UI 不支持 batch upload | 拖文件夹只上传 1 文件 / 无反应 | `failures/A5_attempt_N.md` | Fallback 单文件上传 (293 次点击); 或评估 Playwright 自动化 |
| 4 | P3.1 Notebook 1 上传 | Indexing silent fail (source tile 无内容) | 独有关键词召回失败 / tile 显示 metadata only | `failures/task_P3.1_attempt_N.md` (列 silent fail source) | 重试 2x (re-upload); 仍失败改小批; >10% silent fail 换 Chrome profile |
| 5 | P3.2 / P3.4 / P3.5 Chat 10 smoke | <8/10 (或 <13/15) PASS | critic 判定 FAIL 计数超阈值 | `failures/task_P3.X_attempt_N.md` | P10 响应: reviewer 归因 (source 缺失 / prompt 问题 / 平台边界) → 用户决策 continue/rework |
| 6 | P3.3 Notebook 1 独有 5 题 - Audio | Audio hallucination 事实错误 ≥2 | 人工听完标注 ≥2 | `failures/task_P3.3_attempt_N.md` | retry (预算 8); 仍 FAIL 改 Custom prompt "基于 source 绝不脑补" |
| 7 | P3.3 / P3.4 Audio - per-day cap | 单日 Audio 生成 ≥20 次 | 20/day 触顶 UI 拒绝 | — (rate limit 不算失败) | 跨天重跑 (P11 强制); Q2 不赶无压力 |
| 8 | P3.4 / P3.5 规则 A 抽检 | FAIL 样本 ≥2 (15 reviewer / 10 主控) | 抽检报告 FAIL count | `failures/task_P3.X_audit_attempt_N.md` | P10 归因 → 压缩丢 Exp/Perm 调 source cluster; Req 丢 (不应发生) 立即 rollback 到 A4 |
| 9 | P3.4 Notebook 2 Req 审计 (Task 末尾) | diff > 0 (A4 后 drift) | `source_mapping.py --audit-req-coverage --notebook 2` diff | `failures/task_P3.4_req_drift_attempt_N.md` | 回溯 source #29 是否被编辑 / indexing 某 source 丢; 重审+重上传 |
| 10 | P3.6 Mode A invite | 邀请发出 email 测试账号收不到 | 15 分钟未收 | `failures/task_P3.6_attempt_N.md` | 检查 spam; 换测试 email; Gmail invite best-effort |
| 11 | P3.7 Mode B public link I8 | **Mode B 也受 50-cap** (I8 FAIL) | Web UI / 实测 / re-survey 显示 50 | `failures/task_P3.7_cap_attempt_N.md` | **关键 fallback**: workflow_replication (§8.3 UPLOAD_TUTORIAL § 10); 打包 uploads_public/ 让接收者自建 |
| 12 | P3.9 I3 Mind Map 手动刷新 | 加 source 后 Mind Map 不自动刷新 | UI 观察 | `failures/task_P3.9_attempt_N.md` | 不阻塞; UPLOAD_TUTORIAL § 6 加警示 + Phase 7 RAG/KG 替代 |
| 13 | P3.8 跨 notebook 一致性 | 10 smoke 业务结论某 notebook 矛盾 | §3.4 矩阵 FAIL 行 | `failures/task_P3.8_attempt_N.md` | 识别矛盾源 → 该 notebook 重做 P3.2/P3.4/P3.5 对应部分 → 回归 |
| 14 | 全局 | Hard checkpoint >24h 无 ack | `_progress.json.status = paused` | `failures/checkpoint_pause_N.md` | 用户 ack 后恢复; Q2 不赶无时效压力 |
| 15 | 全局 | 源文件污染 | `git status knowledge_base/` 非 clean | `failures/p5_violation_N.md` | **立即回滚** (`git checkout knowledge_base/`); 调查来源 |
| 16 | 全局 | 同 subagent_type 自审 (违规 D) | Rule D 合规自检 FAIL | `failures/rule_d_violation_N.md` | 立即停, 换第 N+1 种 subagent_type 重跑 reviewer 轮 |

**判据: 什么算 "归档不删" (规则 B)**: 本表任一行触发 → `failures/<path>.md` 必写 5 段: 输入 + 产物 + 技术判定 + 业务判定 + 下一 attempt 输入 plan. 失败数据永不 rm.

---

## §9 对 `_template/` 的补丁候选 (Phase 5 PR)

Phase 1 platform_profile.md 末段已累积 **7 条** (line 126-136). 本 PLAN 起草过程新增 **2 条**:

| # | 补丁主题 | 对应 _template 文件 |
|---|---------|-------------------|
| 1 | Custom Instructions 无 system prompt 平台退化路径 | `00_platform_profile.md §D` |
| 2 | A/B 矩阵 "生成物类平台" 子节 (Audio / Mind Map / Study Guide / Briefing) | `00_platform_profile.md §G` |
| 3 | 无 system prompt 平台 "Notebook 首源设计" if/else 分支 | `05_solution.md` |
| 4 | Q8 "官方公开精确限额 Yes → 跳 calibration" 前置判定 | `03_research.md Q8` |
| 5 | 多实例平台 (multi-notebook 架构) 目录子节 `uploads_N/`/`instructions_N.md` | `01_directory_structure.md` + `05_solution.md` |
| 6 | `share_mode` 两档 `direct_link` / `workflow_replication` | `00_platform_profile.md §E` + `09_closure.md` |
| 7 | Tier 重命名漂移警示 (SKU 词 12 月内语义翻转) | `03_research.md Q2` |
| **8 (新)** | **Per-day rate limit P11 作新范本规则** (Claude/ChatGPT/Gemini 无此概念, NotebookLM 独有) | `04_plan.md §1` (补 P11 模板) |
| **9 (新)** | **Source 隔离约束 P12 + multi-notebook 独立上传成本预估** (最坏 N × sources 次操作) | `05_solution.md` + `04_plan.md §1` (补 P12 模板) |

---

## §10 Carry-over 集成清单 (明示消化位置)

| Carry-over 编号 | 来源 | 内容 | 本 PLAN 位置 |
|----------------|------|------|-------------|
| **C2.9** | R2 (phase1_reviewer2.md) | Mode B cap UNVERIFIED — 可能 owner 套用 Mode A 50-cap | §3.3 Notebook 3 设计 UNVERIFIED 标 + §6 Task P3.7 I8 实测 + §8.3 UPLOAD_TUTORIAL § 10 fallback |
| **C2.10** | R2 | Chat mode rollout 日期分野 (Learning Guide 2025-09-23 XDA vs Chat custom goals 2025-10-29 blog.google) | §0 修订记录 engrained #4 (不区分两日期, Phase 3 UI 截屏防第三方误读) + §5 动作 2 Chat mode 决策 |
| **C2.1 (R1 继承)** | R1 + R2 | PLAN §0 套餐行用 "NotebookLM Pro (via Google AI Pro 订阅)", SKU 漂移注脚 | §0 修订记录 engrained #1 + §1 Rule E 段 |
| **C2.2 (R1 继承)** | R1 + R2 | Scope B 分设计 invite-mode + public-link-mode 两 notebook | §3.2 Notebook 2 Mode A + §3.3 Notebook 3 Mode B |
| **C2.3 (R1 继承)** | R1 + R2 | 容量表四档必列, Pro 高亮; tier 名 Standard/Plus/Pro/Ultra | §0 engrained #2 (Pro tier 500/300/500/20) + §1 P1 (用 words 不用 tokens) |
| **C2.4 (R1 继承)** | R1 + R2 | Chat mode 三档决策格: 默认 Custom + SDTM 专家 prompt | §3.1 Notebook 1 (Custom) + §3.2 Notebook 2 (Learning Guide) + §3.3 Notebook 3 (Custom public) + §5 动作 2 |
| **C2.5 (R1 继承)** | R1 + R2 | Pre-upload source audit `wc -w` Top 5 outlier | §5 动作 1 + §6 Task P3.0 |
| **C2.6 (R1 继承)** | R1 + R2 | Phase 3 节点挂 I1-I7 (+ I8 + I9) 清单, 每 item 明示 pass 判据 | §6 Task P3.1 (I1) + P3.5 可选 (I2) + P3.7 (I5 + I8) + P3.3 (I4 Audio 双语) + P3.3 (I7 audio hallucination) + P3.8 前置 (I6 chat 输入长度 可 soft 顺便) + I9 chat mode UI 截屏 贯穿 P3.2/P3.4/P3.5 |
| **C2.7 (R1 继承)** | R1 + R2 | Source 严格隔离 (每 notebook 独立 source 预算) | §1 P12 (新规则) + §3.3 Notebook 3 说明 P12 重传 + §6 Task P3.4 / P3.5 标"P12 再次独立上传" |
| **C2.8 (R1 继承)** | R1 + R2 | A/B 15 题矩阵 (10 smoke v2 + 5 独有), 阈值 13/15 (87%) | §4 A/B 矩阵设计全节 + §6 Task P3.2-P3.5 |
| **known_differences_from_template `D_system_prompt`** | _progress.json | 跳 system_prompt.md 累积, 改用 Chat custom goals | §3 三 notebook 均用 instructions_N.md (非 system_prompt.md) |
| **known_differences `G_ab_matrix`** | _progress.json | A/B +5 题独有生成物 | §4.2 独有 5 题 |
| **known_differences `H_capacity_calibration`** | _progress.json | 跳 calibration | §0 engrained #8 + §1 (无 P1 tokens 换算) |
| **known_differences `batch_design`** | _progress.json | 单批上传, 无 RAG 衰减 | §6 P3.1 一次全上 293; P10 改写为 per-notebook 87% 阈值 (而非跨批衰减) |
| **known_differences `multi_notebook_strategy`** | _progress.json | 3 notebook 架构 | §3 全节 + §2 uploads_N/ 目录 |
| **known_differences `workflow_replication_sharing`** | _progress.json | Scope B fallback | §3.3 Notebook 3 fallback + §8.3 UPLOAD_TUTORIAL § 10 |
| **known_differences `tier_naming_drift`** | _progress.json | SKU 漂移 | §0 engrained #1 + §0 修订记录表 M1 |
| **I3 (Writer #4 新挂载)** | R1 carry-over (planner v1 遗漏) | 添加 source 后 Mind Map / Study Guide 自动/手动刷新 | §6 新 Task **P3.9** I3a/b/c 场景 + §8.3 UPLOAD_TUTORIAL § 6 警示 + §8.4 失败应急 #12 |
| **Q1=0 红线连锁** (用户 2026-04-21 ack) | 用户 ack | Notebook 2/3 Req 变量零丢失, 无容差 | §3.2.1 concept cluster 30 source 方案 + §3.4 矩阵 "2→0" + §5 动作 4 / §2.5 Phase A A4 (审计脚本) + §6 Task P3.4 审计子步骤 + §2.1 新脚本 (5 处连锁) |

---

## §11 开放问题 (写回 `.omc/plans/open-questions.md` 候选)

Phase 2 PLAN 层面未定死的问题 (Phase 3 执行或用户 ack 时解决):

| # | 问题 | 为何重要 | 解决时点 |
|---|------|---------|---------|
| OQ1 | Notebook 1 "一对一 293 上传" vs "部分合并到 ≤300" 默认选一对一, 但若 Pre-upload audit 发现 >7 outlier 须拆, 拆到多少? | 影响 Notebook 1 source 数 + citation 精度 | Phase 3 Task P3.0 ack |
| OQ2 | Notebook 2/3 精选 ≤30 的具体域选择 (9 core + IG 7 章 + 4 example = 20 实际, 留 10 slot 给 terminology 摘要还是 assumptions?) | 影响 Scope B 知识覆盖广度 | **RESOLVED 2026-04-21 (Writer #4)** — Q1=0 策略下改 concept cluster 30 source 方案, 全域覆盖 + 审计; 见 §3.2.1 具体表. |
| OQ3 | Chat custom goals Custom mode 的 10K char prompt 具体文本 | 影响三 notebook 回答质量 | §5 动作 2 产出 instructions_N.md 时 |
| OQ4 | I8 Mode B 50-cap 实测方法 (找 50+ 真人访客不现实, 是否可模拟或接受 UI 字段观察) | 决定 Scope B 广泛分享的实际可行性 | Phase 3 Task P3.7, 可能最终仍 UNVERIFIED 进 Phase 5 |
| OQ5 | 跨 notebook 一致性 FAIL 时的 rework 范围 (某 notebook 重做 vs 全 3 重做) | 影响 Phase 3/4 时间预算 | Phase 3 Task P3.8 FAIL 时 |
| OQ6 | Phase 4 cross_platform_compare 的对齐维度 (若 ChatGPT/Gemini Phase 6.5 未完成, 能否用 Claude 终态 baseline 单向对比) | 影响 Phase 4 交付形态 | Phase 3 完成时看其他平台状态 |
| **OQ7 (新)** | Phase A A5 Web UI batch upload 能力未知 | 影响 Phase 3 总操作数 (3-10 次 vs 293 次) + 工时 (5h vs 16h) | Phase A A5 实测 |
| **OQ8 (新)** | extract_req_vars.py 从 VARIABLE_INDEX.md 抽 vs 从 63 spec.md 逐个抽 | 决定 A6 脚本实现复杂度 | Phase A A6 实现时 |

---

## 执行规则一览 (Cheatsheet)

| 规则 | 触发条件 | 动作 |
|------|---------|------|
| A | Notebook 2/3 合并压缩 >50% | N=10 独立抽检, `notebook_N_audit.md` |
| B | 任何 Task attempt FAIL | `dev/evidence/failures/task_<N>_attempt_<X>.md`, 不删 |
| C | Phase 5 收束 | `docs/RETROSPECTIVE.md` 三段式 + 独立 reviewer 复核 |
| D | 每次 subagent 派发 | Writer ≠ Reviewer, 不同 subagent_type |
| E | 本次已 ack | ABC 全向 + Pro + Web UI + personal Gmail |
| P4 | 每 Task | 标 hard/soft/none, 不隐式推进 |
| P10 | Per-notebook A/B PASS <87% | 立即停, reviewer 归因, 用户决策 continue/rework |
| P11 (新) | Audio 题执行 | 单日 ≤20, 跨 notebook 建议跨天 |
| P12 (新) | 创建 Notebook 2/3 上传 source | 不能从其他 notebook 引用, 必独立重传 |

---

*本 PLAN 产出 = Writer #3 (oh-my-claudecode:planner, opus), Rule D 第 5 种 subagent_type. 待 Reviewer #3 (第 6 种) 独立审核.*

---

### Writer #4 修正日志 (2026-04-21, subagent_type=feature-dev:code-architect, 主 session apply blueprint)

**背景**: Writer #3 (planner) 产出 PLAN v1 657 行, Reviewer #3 (analyst) 判 CONDITIONAL_PASS 82%, 指 6 必改 + 4 Open Questions. 用户 2026-04-21 二次 ack: Q1=Req 变量零丢失 (红线), Q2=不赶工时质量第一, 方案=Y. Writer #4 = Rule D 第 7 种 subagent_type (前 6: general-purpose / verifier / executor / critic / planner / analyst); W#4 subagent 工具集限 Read/Glob/Grep, 故产出完整 blueprint, 主 session 据此 apply 落盘. 待 Reviewer #4 (`pr-review-toolkit:code-reviewer`, 第 8 种) 独立复核.

| # | 修正项 | 严重度 (R3) | 位置 | 改前 → 改后 |
|---|-------|-----------|------|-----------|
| 1 | I3 Mind Map / Study Guide 刷新节奏挂 Task | MAJOR (遗漏) | §6 新增 P3.9 + §10 carry-over + §8.4 失败 #12 | 从 "完全未挂" → 独立 Task P3.9 (soft checkpoint, 4 场景 I3a/b/c + I4) |
| 2 | §6 每 Task 加 operations_count + wallclock_hours + prerequisite_tasks + parallel_with | MEDIUM | §6 P3.0-P3.8 + P3.9 | 从 "无量化" → 逐 Task 4 字段 + 工时汇总表 (29-94h / 5-16 天) |
| 3 | §3.4 "丢 >2 Req 变量 FAIL" 改 "丢 >0" + 全 chain 连锁 | HIGH (业务红线) | §3.2.1 (concept cluster 30 source) + §3.4 (阈值) + §5 动作 4 / §2.5 Phase A A4 + §6 P3.4 审计子步骤 + §10 carry-over + §2.1 新脚本 | "按 domain 挑" → "按 concept cluster 重 bucket"; 2→0; 新 extract_req_vars.py + cluster_req_variables.py + `--audit-req-coverage` + source #29 |
| 4 | 新增 Project Success Criteria 段 | MEDIUM | 执行摘要后, §0 前 | 从 "无业务成功定义" → 5 条 + 3 use-case A/B/C |
| 5a | 新增独立 §2.5 Phase A Setup (6 子动作 A1-A6) | MEDIUM | §2 后, §3 前 | 从 "混在 §5" → 独立段, 6 Task (A1 audit + A2 chat mode + A3 N1 映射 + A4 N2/3 清单含 Req 审计 + A5 Web UI batch + A6 Req extract), 含依赖图 + parallel_with + 工时 9-32h |
| 5b | §8.4 失败应急集中表 | MEDIUM | §8.3 后, §9 前 | 从 "失败散落 4 处" → 集中表 16 行 |
| 6 | §6 Task 加 parallel_with (合并到修正 2) | MEDIUM | 同修正 2 | 识别 P3.3∥P3.4, P3.4 audio∥P3.5 上传, P3.6∥P3.9 等 |
| 连锁 | §2.1/§2.4 新脚本 + evidence 文件 | 来自修正 3 | §2.1 scripts + §2.4 职责 + §2.1 evidence | 新 2 脚本 + 4 evidence 文件 |
| 连锁 | §11 OQ2 RESOLVED + OQ7/OQ8 新增 | 来自修正 3 + A5/A6 | §11 | Q1 ack 清 OQ2; 新 OQ7 (A5 batch) + OQ8 (extract 脚本路径) |

**SDTM 领域事实核查** (Q1=0 技术前提):
- 63 domain spec.md × 平均 5-9 `**Core:** Req` = **~366 Req 记录**
- `knowledge_base/VARIABLE_INDEX.md` 通用变量段 ~24 条 + 域特定段 ~90-100 独立 Req
- 合并到 30 source 的 concept cluster 方案**可覆盖 100%** (见 §3.2.1)

**`_template/` 补丁候选新增 (第 10 条)**:
- **#10** **领域红线变量零丢失审计模式** (SDTM-like 独有): 源材料含域标记"必填/关键/红线"变量时, 平台部署合并压缩必过"该标记变量零丢失"自动化审计 (脚本 + source_N_coverage_audit 元 source); 对齐 `_template/05_solution.md` Deferred stub 段后加子段 "domain red-line audit"

**Rule D 合规声明**:
- W#1 `general-purpose` → R#1 `oh-my-claudecode:verifier`
- W#2 `oh-my-claudecode:executor` → R#2 `oh-my-claudecode:critic`
- W#3 `oh-my-claudecode:planner` → R#3 `oh-my-claudecode:analyst`
- **W#4 (本次) `feature-dev:code-architect`** ← 第 7 种 (blueprint 模式, 主 session 代 apply)
- R#4 (后续) `pr-review-toolkit:code-reviewer` ← 第 8 种

**未修正范围自律**:
- 未动 research.md / phase1_reviewer*.md / phase2_reviewer.md / platform_profile.md / _progress.json / _spec/ / 其他平台
- §4 A/B 矩阵 (10 smoke + 5 unique) 无实质改
- §9 补丁候选 7 条保留, 附加 #10 (SDTM 红线审计)
- 规则 A N=10 边界数字不动

---

*Writer #4 (feature-dev:code-architect 设计 + 主 session 按 blueprint apply) 完成 2026-04-21. 等 Reviewer #4 (第 8 种 `pr-review-toolkit:code-reviewer`) 独立复核.*
