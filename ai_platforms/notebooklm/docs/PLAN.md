# NotebookLM 平台部署 PLAN v2 (2026-04-21 架构 pivot 后重写)

> **产出时间**: 2026-04-21
> **Writer**: 主 session (pivot 后重写, 非 subagent) — 作为 v1 → v2 架构修正过渡产物
> **审查链扩展**: v1 Phase 2 已烧 8 种 subagent_type (general-purpose / verifier / executor / critic / planner / analyst / code-architect / pr-review-toolkit:code-reviewer); v2 本 PLAN 计划派第 9 种独立 subagent_type 架构级审
> **所属 Phase**: 2 PLAN v2 (Phase 1 Research 已 PASS, Q7+§11 已 v2 重写)
> **项目 Tier**: **Tier 2** (5-15 step, 半天-1 天级)
> **v2 架构背景**: `archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md` 强制前读

---

## 执行摘要 (Executive Summary)

把 SDTM 293 md 知识库部署到 **NotebookLM Pro tier 单 notebook**, 采用 **concept cluster 合并到 ≤50 sources** 策略 (Pro 300 slot 的 16.7%). ≤50 的**主归因**是 "**indexing silent fail 风险降低 + citation 信噪比提升**" (证据 HIGH), 次归因 "Free tier viewer 兼容水位" (证据 MEDIUM, 待 Phase 3 P3.9 子步骤 (f) 闭合). 在**本次 Rule E ack 场景下** (personal Gmail + ABC + 无 collaborator 圈职责隔离需求), Scope ABC 三场景 (个人学习 / 小圈分享 / 公开分享) 通过**同一 notebook 的 3 档 Access Level 切换** (Restricted / Anyone with link / Public) 实现, 不使用多 notebook. 未来若 collaborator 圈需要完全职责隔离 (同 org 内不同 team), 再评估升级多 notebook.

关键风险已降低: 最坏上传 ~50 次 (v1 最坏 353 次的 14%), A/B 题次 15 (v1 的 33%), indexing silent fail 风险面降低 ~85%, Req 零丢失在 50 slot 下比 v1 的 30 slot 更易守.

Q1 红线 (0 Req 变量丢失, 用户 2026-04-21 ack) 在 v2 下**向内收紧**: 50 slot 给 concept cluster 留更多 outlier 容错余地, 实现路径 `extract_req_vars.py` → 全集清单 → `cluster_req_variables.py` → ≤50 bucket → `req_vars_coverage_audit.md` ∅ gap 断言.

A/B 矩阵 10 题 SMOKE **v3 Q1-Q10** (跨 4 平台对比基线, v2.2 2026-04-22 升级对齐 ChatGPT+Gemini N5.3 Full A/B Generalization Probe; 题源 `ai_platforms/smoke_v3_questions_draft.md` v3.1), PASS 阈值 ≥9/10 (~90%). **原 5 独有生成物评估 (Audio/Mind Map/Study Guide) 与 P3.5/P3.6/P3.7 一起挪 ICEBOX post-project optional** (2026-04-22 用户决策 A+保留: Studio 独有产出无跨 4 平台对比价值, 问答才是核心; 全项目收束后小概率回头精雕, 原任务定义 §6 / §7 保留). 分享档位在 Phase 3 末做一次 3 档切换演练 (不需要多 notebook 测试).

---

## Project Success Criteria (v2)

SDTM 1 notebook 部署的**业务成功定义**. 用户 2026-04-21 ack:

1. **Quality**: 单 notebook 10 SMOKE **v3 Q1-Q10** A/B ≥9/10 (~90%) AND **Req 变量零丢失** (Q1 红线) [v2.1 2026-04-22: 原 "+ 独有 5 题 ≥4/5 精确命中" 挪 ICEBOX post-project optional, 不计入本次 Quality gate] [v2.2 2026-04-22: 题库 v2.1 → v3 Q1-Q10 升级, 阈值 ≥9/10 保不变]
2. **Completeness**: notebook + `instructions.md` + `UPLOAD_TUTORIAL` 10 章节 + `uploads/MANIFEST.md` + `cross_platform_compare.md` 全落盘
3. **Sharing**: 3 档切换演练 (Restricted → Anyone with link → Public → 回 Restricted) 四态全流畅, UI 状态符合预期
4. **Template contribution**: `_template/` 补丁候选 ≥10 条 (原 7 + pivot 后新增 3) 收束合并
5. **Cross-platform data**: 10 SMOKE **v3 Q1-Q10** vs Claude v2.6 / ChatGPT GPTs / Gemini Gems 四平台对比 (Claude v2.6 原测 v2.1, Phase 4 需补 v3 Q1-Q10 回归或接受 Claude 侧 v2 基线异步; 优先确保 ChatGPT/Gemini/NotebookLM 三者 v3 同期可比)
6. **Workflow replication**: 任何 SDTM 工作者凭 `current/uploads/` + `UPLOAD_TUTORIAL.md` 能 ≤1 天在自己账号上 (Pro / Free 皆可, ≤50 source 兼容) 独立重建等效 notebook

**分用户群 use-case success**:
- **Success A (Scope A, 用户本人)**: 30 秒内回答 SMOKE **v3 Q1-Q3** (GF / CP / BE+BS+RELSPEC v3.4 新域场景), citation 精确到 md 段
- **Success B (Scope B, ≤50 同事 Restricted 邀请)**: 5 位同事 onboard ≤10 分钟独立查 core domain spec
- **Success C (Scope B/C, Anyone with link 公开档)**: 陌生访客打开 notebook 能读懂 SMOKE **v3 Q1-Q3**, 不臆造

---

## §0 修订记录

| 版本 | 日期 | Writer | 变更 | 触发 |
|------|------|--------|------|------|
| v1 | 2026-04-21 AM | planner | 初版 (3 notebook × 30-293, 951 行) | Phase 1 PASS |
| v1.1 | 2026-04-21 AM | feature-dev:code-architect (W#4) | R3 analyst 6 必改 + Project Success Criteria + Phase A §2.5 + Q1=0 红线 + extract_req_vars.py 新脚本 | R3 审核 + 用户 Q1/Q2 ack |
| **v1.x SUPERSEDED** | 2026-04-21 PM | — | **整个 v1 架构归档** (`archive/v1_3notebook_SUPERSEDED_2026-04-21/PLAN_v1_3notebook.md`), 触发: 用户 review 质疑 3 notebook 架构 + 三 WebFetch 核实推翻 v1 三假设 | 用户 2026-04-21 PM 决策 |
| **v2** | 2026-04-21 PM | 主 session (pivot 后重写) | 架构改 **1 notebook × ≤50 sources + 分享档位 3 档切换**; 删除 §3 multi-notebook 段 / uploads_main/invite/public 三目录 / 45 题次 A/B / 353 次上传; Req 零丢失红线 slot 从 30 → ≤50 宽松化; Phase A A5 (webui batch capability) 降级为 soft; P12 降级为信息段; I8/C2.9 close; 继承资产 A-F (详 pivot record) | 用户 ack pivot + 三 WebFetch 证据闭合 |
| **v2.1** | 2026-04-22 PM | 主 session (用户决策执行) | **P3.5/P3.6/P3.7 (Audio / Mind Map / Study Guide) 挪 ICEBOX** (post-project optional, non-gating); P3.8 A/B 15→10 题 (仅 10 SMOKE v2 跨平台对比基线), 阈值 ≥13/15 → ≥9/10 (~90%); 5 独有生成物评估 (U1-U5) 同步 ICEBOX; 原任务定义全保留于 §6 / §7 供全项目收束后用户选择性精雕; Phase 3 总工时下调 ~3h; Phase 3 收束 gate 不再依赖 Studio 三件套 | 用户 2026-04-22 PM ack 方案 A+保留: Studio 独有产出无跨 4 平台对比价值 (Claude/ChatGPT/Gemini 均无等价功能); 问答才是跨平台核心比较维度; 全项目收束后小概率回头精雕 |
| **v2.2** | 2026-04-22 PM | 主 session (用户决策执行) | **P3.8 题库升级 smoke v2.1 → smoke v3 Q1-Q10** (跨平台对比基线同步到 ChatGPT+Gemini 当前 N5.3 Full A/B 版本); 题源 `ai_platforms/SMOKE_QUESTIONS_V2.md` → `ai_platforms/smoke_v3_questions_draft.md` v3.1 Q1-Q10 (双平台共用 10 题, Q11-Q14 ChatGPT 专属不适用 NotebookLM); **PASS 阈值保 ≥9/10 (~90%)** 不降 (ChatGPT/Gemini 合格阈 71%/70% 是因为 ChatGPT 多 4 题专属难度; NotebookLM 分母仍 10, 阈值不动); 维度不同: v2 = 04 预设场景 baseline, v3 = generalization probe (v3.4 新域 GF/CP/BE+BS + 域边界 LB/MB/IS + Timing 深化 + Extensible CT + Pinnacle 21 + SUPP 深化) | 用户 2026-04-22 ack 选项 A: NotebookLM 对齐 ChatGPT+Gemini 当前 N5.3 smoke v3 以便 Phase 4 跨平台 A/B 矩阵同批次对比; v2.1 已被证明 04 open-book 偏简单, v3 才是真实 SDTM 泛化能力测试; 阈值保 ≥9/10 按用户决策 |

### 用户 ack 关键决策 (沿袭 v1, v2 不变)

| Q | 用户决定 | v2 含义 |
|---|---------|--------|
| **Q1** (Req 变量零丢失?) | **0 (零容忍)** | §3.2 合并策略 concept cluster, §6 A4 Req 审计子步骤, 50 slot 比 v1 的 30 更宽松 |
| **Q2** (工时节奏?) | **不限工时, 质量第一** | §6 Task 保守上界; 失败重试预算放宽 |
| **v2 pivot 决策** (2026-04-21 PM) | **Y (推倒重做, 干干净净)** | v1 产物全归档, v2 文档清爽不混 |
| **v2 Reviewer 规格** (2026-04-21 PM) | **Y (派第 9 种 subagent_type 架构级审)** | 本 PLAN 写完派第 9 种 subagent_type (前 8 之外) 做架构级独立审, 锚定 Q1 红线在 pivot 过程未被破坏 |

### Phase 1 engrained 事实摘录 (v2 立足点)

| # | 事实 | 来源 |
|---|------|------|
| 1 | Pro tier (via Google AI Pro): 500 notebooks × 300 sources × 500 chat × 20 audio/day | research.md Q2 |
| 2 | 500K words/source 全 tier 统一 | research.md Q2 脚注 |
| 3 | Chat custom goals 三档 (Default / Learning Guide / **Custom**), 全档开放, Custom 10K char | research.md Q6 |
| 4 | **同一 notebook 3 档 Access Level 切换** (Restricted / Anyone with link / Public), **非两独立模式**, 档位可随时切 | **research.md Q7 v2** + 2026-04-21 三 WebFetch |
| 5 | **50-cap 仅套 Restricted invite 档**, 不覆盖 Anyone with link / Public | research.md Q7 v2 |
| 6 | **分享不改 viewer 自己 tier source cap** — 官方原文 "Sharing a notebook does not change the source limit for any collaborator"; WebFetch AI summary 解读 A (Free viewer 最多看 50 sources) **证据强度 MEDIUM** (M5 fix: 非 A 级官方原文, 是二次解读). ≤50 结论保留, 但 "Free tier viewer 兼容" 作 ≤50 首要归因降级为次要; 主 drive 改 "**indexing silent fail 风险随 source 数线性降 + citation 信噪比提升**" (Q5 + 社区观察, 证据 HIGH). P3.9 子步骤 (f) Phase 3 顺手用 Free tier 小号闭合实测 | research.md Q7 v2 + Q8 |
| 7 | Indexing silent fail 官方承认, 预览 + smoke 问答是验证手段 | research.md Q5 |
| 8 | Audio Overview 4 format (Deep Dive / Brief / Critique / Debate), 20/day Pro | research.md §9 |
| 9 | Source 严格隔离 (事实仍成立, 但单 notebook 无跨 notebook 引用需求, 降级为信息约束) | research.md §11 v2 |

---

## §1 执行规则 P1-P12 + A/B/C/D/E (P12 降级)

继承全局 `~/.claude/CLAUDE.md` 四规则 A/B/C/D, 范本规则 E, 本 PLAN P1-P12 (v2):

| # | 规则 | 适用 | v2 特化 |
|---|------|------|---------|
| **A** (全局) | 语义抽检: 压缩/改写 >50% 强制 N 样本独立抽检 | Phase 3/4 writer 完成后 | 本平台: 293 md → ≤50 source (压缩率 ~83%) 触发规则 A, N=10 |
| **B** (全局) | 失败归档不删 | 任何失败 attempt | 路径 `dev/evidence/failures/task_<N>_attempt_<X>.md` |
| **C** (全局) | Retro 强制 Tier 2/3 | Phase 5 收束 | `docs/RETROSPECTIVE.md` 含本次 pivot 作关键案例 |
| **D** (全局) | 写审分离, 不同 subagent_type | 每次 subagent 派发 | v1 已烧 8 种, v2 PLAN 审派第 9 种; Phase 3/4/5 继续延伸 |
| **E** (范本) | 用户业务优先级 Phase 0/2 确认 | 本次**已 ack 2026-04-21** | ABC 全向 + Pro + Web UI + personal Gmail, 三场景在单 notebook 分享档位切换 |
| **P1** | 量化 PASS: 每 step 打印 `[Stage X.Y] <file>: <N> words (target ≤500K)` | 每 step | 本平台用 **words 不用 tokens** |
| **P2** | 写/审分离 executor ≠ reviewer | 每 subagent | 同 D |
| **P3** | AI 估算值前缀 `~`, 实测值不加 | manifest/报告 | indexing 时间 / audio 评分等实测数字无前缀, 估算加 `~` |
| **P4** | 人工抽查 checkpoint: 每 Task 标 hard/soft/none | 每 Task | 见 §6 |
| **P5** | 源文件只读: `knowledge_base/` 禁写 | 全程 | `git status knowledge_base/` 非 clean 立即回滚 |
| **P6** | Subagent 上下文隔离 + prompt 归档 | 每次派发 | `dev/evidence/subagent_prompts/task_<N>_<role>.md` |
| **P7** | 进度持久化 `_progress.json` + `trace.jsonl` | 每 Task | Schema 继承 |
| **P8** | 失败归档 (同 B) | — | — |
| **P9** | 语义抽检 (同 A) | 压缩合并时 | N=10 (规格见 `_spec/06_review.md`) |
| **P10** | A/B 衰减强制响应: PASS <87% 触发重构 | A/B 完成后 | 归因 (source 缺失 / Chat prompt / 平台边界) → 用户决策 |
| **P11** | **Per-day rate limit 约束**: Audio ≤20/day, Chat ≤500/day | Phase 4 Audio 题 | 本平台独有; 2 audio 题单日足够, retry 预算跨天 |
| **P12** (降级) | **Source 隔离信息约束** (非 hard rule v2 下) | 单 notebook 无跨 notebook 引用需求 | 保留作知识: 若未来升级多 notebook 需重启此 rule |

**Rule E 引用**: ABC 全向 + Pro + Web UI + personal Gmail ack 2026-04-21 (`_progress.json rule_E_user_priority`). v2 单 notebook 架构下, ABC 三场景在同 notebook 按分享档位切换实现, 不再映射多 notebook.

---

## §2 文件结构 map (Create / Modify / Read-only) — v2 单层 uploads/

### 2.1 Create

```
ai_platforms/notebooklm/
├── docs/
│   ├── PLAN.md                                  ← 本文件 (v2)
│   ├── RETROSPECTIVE.md                         ← Phase 5 (规则 C, 含 pivot 复盘)
│   ├── handoff.md                               ← Phase 5 (可选, 若 Phase 7 启动)
│   └── cross_platform_compare.md                ← Phase 4 (4 平台 10 SMOKE v3 Q1-Q10 对比, v2.2 2026-04-22 升级)
├── current/
│   ├── README.md                                ← Phase 5 发布版总览
│   ├── UPLOAD_TUTORIAL.md                       ← Phase 5 10 章节 (v2: 单 notebook 路径)
│   ├── uploads/                                 ← 单 notebook source 目录
│   │   ├── MANIFEST.md                          ← ≤50 source 清单 + concept cluster 策略
│   │   └── README.md                            ← notebook 能力 + 3 档分享使用说明
│   └── instructions.md                          ← Chat custom goals Custom mode 文本 (≤10K char)
├── dev/
│   ├── scripts/
│   │   ├── count_words.py                       ← 用 `wc -w`
│   │   ├── pre_upload_audit.py                  ← wc -w 排序 + Top 5 outlier + 500K cap 校验
│   │   ├── extract_req_vars.py                  ← 从 VARIABLE_INDEX.md + domains/*/spec.md 抽 Core=Req 全集
│   │   ├── cluster_req_variables.py             ← concept cluster 重 bucket 到 ≤50 source (Q1=0 实现)
│   │   └── merge_sources.py                     ← (可选) 自动化 md → source 合并文本生成
│   ├── evidence/
│   │   ├── pre_upload_audit.md                  ← Phase A A1 产物
│   │   ├── req_vars_full_set.md                 ← Phase A A2 产物
│   │   ├── source_mapping.md                    ← Phase A A3 产物 (concept cluster → ≤50 bucket)
│   │   ├── req_vars_coverage_audit.md           ← Phase A A4 产物 (Q1=0 ∅ gap 自证)
│   │   ├── mind_map_refresh_test.md             ← Phase 3 P3.x 实测
│   │   ├── share_level_toggle_drill.md          ← Phase 3 末: 3 档切换演练
│   │   ├── phase2_v2_reviewer.md                ← 第 9 种 subagent_type 独立审 (本 PLAN 写完后)
│   │   ├── phase3_task_N_audit.md               ← 每 Task 规则 A 抽检 (触发时)
│   │   ├── subagent_prompts/                    ← 每次派发 prompt 归档 (P6)
│   │   ├── failures/                            ← task_<N>_attempt_<X>.md (规则 B)
│   │   └── checkpoints/                         ← hard checkpoint handoff (P4)
│   ├── ab_reports/
│   │   ├── notebook_ab.md                       ← notebook 15 题 A/B
│   │   └── consistency_review.md                ← (可选) 同 notebook 不同档位答案一致性
│   └── test_results.md                          ← 15 题次完整记录
```

### 2.2 Modify

```
ai_platforms/notebooklm/dev/evidence/_progress.json    (每 Task 完成)
ai_platforms/notebooklm/dev/evidence/trace.jsonl        (append-only)
ai_platforms/notebooklm/README.md                       (Phase 5 reorg 后)
ai_platforms/notebooklm/ROADMAP.md                      (Phase 5 状态改 "已完成")
.work/MANIFEST.md                                       (Phase 5 收束, Chain 规则)
.work/meta/worklog.md                                   (Phase 5 收束)
docs/PROGRESS.md                                        (Phase 5 收束)
CLAUDE.md                                               (Phase 5 收束, Key Paths 新增)
```

### 2.3 Read-only

```
knowledge_base/**                                                     (P5)
ai_platforms/_template/**                                             (范本禁污染, 补丁走 Phase 5 PR)
ai_platforms/notebooklm/_spec/**                                      (Phase 0-1 固化, 禁改)
ai_platforms/notebooklm/docs/research.md                              (Q7/§11 已 v2 重写, 禁再改)
ai_platforms/notebooklm/docs/platform_profile.md                      (v2 已重写, 禁改)
ai_platforms/notebooklm/archive/**                                    (v1 冻结归档, 禁任何改)
ai_platforms/SYNC_BOARD.md                                            (本平台不参与锁步)
ai_platforms/claude_projects/**                                       (参照只读)
```

### 2.4 脚本职责边界 (单一职责, P6)

| 脚本 | 单一职责 | 输入 | 输出 |
|------|---------|------|------|
| `count_words.py` | `wc -w` 数 words | 目录或文件 | stdout: `<file>: <N> words` |
| `pre_upload_audit.py` | wc -w 排序 + Top 5 outlier + 500K cap 校验 | `knowledge_base/**/*.md` | `dev/evidence/pre_upload_audit.md` |
| `extract_req_vars.py` | 从 `VARIABLE_INDEX.md` + `domains/*/spec.md` 抽 `Core=Req` 全集 | `knowledge_base/**` | `dev/evidence/req_vars_full_set.md` (~366 记录; 去重 ~100-120 独立) |
| `cluster_req_variables.py` | 按 concept cluster 重分 bucket 到 ≤50 source (Q1=0) | `req_vars_full_set.md` + 293 md | `current/uploads/MANIFEST.md` + `dev/evidence/source_mapping.md` |
| `merge_sources.py` (可选) | 按 source_mapping 合并 md 片段到单 source 文件 | `source_mapping.md` + 293 md | `current/uploads/<source_N>.md` (≤50 个) |

---

## §2.5 Phase A Setup (简化 v2)

v1 Phase A 6 子动作 + A5 "webui batch upload 能力调研" (hard checkpoint) 在 v2 下降级: 单 notebook × ≤50 次上传 Web UI 手工拖拽, 不强制 Playwright 前置. **但 Web UI 单批拖拽 ≤50 的可行性未做 Phase 1 实测 (M2 fix), 加 A5' 小样闭合**. Phase A 共 **5 子动作**:

| Task | 子动作 | 输入 | 输出 | Checkpoint | 估算工时 |
|------|-------|------|------|-----------|---------|
| **A1** Pre-upload audit | `wc -w` 293 md + Top 5 outlier 排序 + 500K cap 校验 | `knowledge_base/**/*.md` | `dev/evidence/pre_upload_audit.md` | **hard** | 15 分钟 |
| **A2** SDTM Req 变量 extraction | 跑 `extract_req_vars.py`, 从 `VARIABLE_INDEX.md` + `domains/*/spec.md` 抽 `Core=Req` 全集 | `knowledge_base/**` | `dev/evidence/req_vars_full_set.md` (~366 记录; 去重 ~100-120 独立) | **hard** (Q1=0 红线前置) | 1-2 小时 |
| **A3** Source bucket 设计 | 跑 `cluster_req_variables.py`, 按 concept cluster 重分到 ≤50 bucket | A2 产物 + 293 md | `dev/evidence/source_mapping.md` + `current/uploads/MANIFEST.md` (草) | **hard** | 2-3 小时 |
| **A4** Req 变量全覆盖审计 (**结构级**, 见 §3.2 step 3-6) | 对照 A2 全集 vs A3 bucket 蕴含式断言 | A2 + A3 产物 | `dev/evidence/req_vars_coverage_audit.md` ("Req 变量零漏集" 结构级断言 + diff 表) | **hard** (Q1=0 结构自证) | 1-2 小时 |
| **A5' (M2 fix) Web UI 上传能力小样实测** | 主 session (或用户) 登 notebooklm.google.com 建废弃 notebook, 拖 5 个 knowledge_base/ 任选 md 实测 (单批拖入 / indexing 时间 / silent fail 计数 / 预览正确性) | Web UI + 5 md 小样 | `dev/evidence/phase_a_webui_small_sample.md` (5 条记录 + PASS/FAIL + P3.2 策略决策: 单批 50 vs 分批 N×批) | **hard** (决定 P3.2 是否分批) | 30 分钟 |

**Phase A 总工时**: **4.5-7.5 小时** (Q2 保险 2x = 9-15 小时, 1 天内可收完). A5' 小样实测仅 30 分钟, 不影响总工时大头.

**Phase A 依赖图**:
- A1 独立
- A2 独立 (可与 A1 并行)
- A3 依赖 A2
- A4 依赖 A2 + A3
- **A5' 独立** (可与 A1/A2 并行, 不依赖其他产物)

**推荐调度**: Day 1 并行 A1 + A2 + A5'; Day 1-2 串行 A3 → A4.

**Phase A 完成判据** (进 §6 Phase 3 的 gate):
- 5 子动作 evidence 全部落盘
- A1/A2/A3/A4/A5' 全 hard checkpoint 用户 ack
- `req_vars_coverage_audit.md` 显式声明 "Req 变量零漏集" (结构级 ∅ gap)
- ≤50 bucket 清单可用于 Web UI 上传
- **A5' 小样实测 PASS**, P3.2 策略 (单批 / 分批) 明确落盘; 若小样 FAIL 必立即调整 §6 P3.2 设计

---

## §3 单 notebook 架构设计 (核心 v2)

### 3.1 Notebook — SDTM Knowledge Base (统一)

| 字段 | 值 |
|------|----|
| 命名 | `SDTM Knowledge Base` |
| 目标用户 | 用户本人 (Scope A) + SDTM 小组同事 (Scope B Restricted 邀请) + 公开访客 (Scope B/C Anyone with link / Public 档) — 三场景**同一 notebook** |
| Source 数 | **≤50** (Pro 300 slot 的 16.7%) |
| Source 组成 | 按 concept cluster 重分 bucket (见 §3.2), 293 md → ≤50 source |
| Chat mode | **Custom** (Chat custom goals, ≤10,000 char) — SDTM 专家 system prompt |
| Audio Overview 侧重 | Long Deep Dive (≥3 期, 覆盖 SAFETY / EFFICACY / PK 三组) + 短 Brief (5-10 分钟精选 domain) |
| Mind Map 侧重 | 63 domain 跨域关系图 (RELREC / --STAT / SUPP) |
| Study Guide 侧重 | IG ch04/08/10 关键规则 |
| 分享模式 | **3 档按需切** (见 §3.3) |
| A/B 矩阵 | **v2.2 2026-04-22**: 10 题 SMOKE **v3 Q1-Q10** (跨 4 平台对比基线, 升级对齐 ChatGPT+Gemini N5.3 Full A/B Generalization Probe); v2.1 10 题 SMOKE v2.1 作基线已 SUPERSEDED; 原 "5 独有 (Audio 2 + Mind Map 2 + Study Guide 1)" 挪 ICEBOX post-project optional |
| PASS 阈值 | **v2.1 2026-04-22**: ≥9/10 (~90%) AND **Req 变量零丢失** (原 "每个独有产出 ≥1 精确命中" 随 ICEBOX 删除) |

### 3.2 Source 组成策略 — Req 变量全覆盖 (Q1=0 强制)

**Q1 红线 (用户 2026-04-21 ack)**: 合并到 ≤50 source 必须 **100% 覆盖所有 SDTM `Core=Req` 变量**. 丢 >0 触发 FAIL.

**SDTM 事实基础** (Phase A A2 extract):
- 63 domain × 3-9 `**Core:** Req` 变量 ≈ **~366 Req 记录**
- 去重通用变量 (STUDYID 63 域 / DOMAIN 59 域 / USUBJID 55 域 / --SEQ / ETCD/IECAT/IETEST/IETESTCD/MIDSTYPE) 后 **独立 Req ~100-120**
- 来源: `knowledge_base/VARIABLE_INDEX.md` (自动生成, 含 Core 列)

**策略: 按 concept cluster 合并, 非按 domain 挑**

| 旧思路 (v1 domain-unit) | v2 思路 (concept cluster × ≤50 slot 宽松) |
|----|----|
| 9 core domain spec + IG 7 章 + 4 examples ≈ 20 source (v1 ≤30 slot 紧) | 按 concept cluster 重分, 每 source 跨 domain 含相关 Req; ≤50 slot 给 outlier 容错余地 |
| 非 core domain (DD/HO/ML 等) Req 可能全丢 | 所有 ~366 Req 至少出现在 1 source, 后台脚本自动 audit |

**≤50 source 建议 bucket 方案** (Phase A A3 产出 concrete 清单, 以下为示意):

> **Source of truth 契约 (H1 fix)**: **本表仅示意**, Phase A3 `cluster_req_variables.py` 脚本产物 (`dev/evidence/source_mapping.md` + `current/uploads/MANIFEST.md`) **为准**. 若脚本产物与本示意 slot 分配差异 >20% (slot 数 / domain 聚类粒度), **触发本 PLAN §3.2 同步刷新**, 避免 PLAN 自身过时. 示意仅用于评估策略可行性与审查, 不作为上传清单 source.

| # | Source 名 (示意) | 内含 domain Req 变量范围 | 预计 words |
|---|-----------------|------------------------|-----------|
| 1 | `00_navigation.md` | 索引 / 路由提示 / Req 变量速查入口 | ~3K |
| 2 | `01_common_identifiers.md` | STUDYID + DOMAIN + USUBJID + SUBJID + --SEQ (所有 63 域共享) | ~5K |
| 3-4 | `02-03_patient_demographics_family.md` | DM + SC (拆 2 slot 精细化) | ~15K |
| 5-7 | `04-06_intervention_family.md` | EX + EC + AG + CM + PR + SU (拆 3 slot) | ~45K |
| 8-10 | `07-09_events_family.md` | AE + CE + DS + DV + MH + HO (拆 3 slot) | ~45K |
| 11-14 | `10-13_findings_core.md` | LB + VS + EG + PE + QS + IE (拆 4 slot) | ~55K |
| 15-18 | `14-17_findings_specialized.md` | MB + MI + MS + MK + PC + PP + OE (拆 4 slot) | ~45K |
| 19-22 | `18-21_findings_other.md` | BE/BS/CP/CV/DA/DD/FA/FT/GF/IS/ML/NV/RE/RP/RS/SR/SS/TR/TU/UR (拆 4 slot) | ~60K |
| 23-25 | `22-24_trial_design.md` | TA/TD/TE/TI/TM/TS/TV (拆 3 slot) | ~30K |
| 26-27 | `25-26_relationships_and_supp.md` | RELREC + RELSPEC + RELSUB + SUPPQUAL + SE + SV + SM + CO (拆 2 slot) | ~25K |
| 28-33 | `27-32_ig_chapter_3-8.md` | IG ch 3-8 核心段 (每章 1 slot) | 各 ~25K |
| 34-35 | `33-34_controlled_terms_core.md` | terminology/core/ 高频 codelist (拆 2 slot) | ~60K |
| 36 | `35_controlled_terms_supplementary.md` | terminology/core/ 低频 + supplementary 摘要 | ~30K |
| 37-39 | `36-38_examples_core.md` | AE/CM/DM/LB/VS 5 核心域高频 example (拆 3 slot) | ~45K |
| 40-41 | `39-40_assumptions_core.md` | 5 核心域 assumptions (拆 2 slot) | ~30K |
| 42-46 | `41-45_variable_index_part_1-5.md` | VARIABLE_INDEX.md 拆 5 part | 各 ~20K |
| 47 | `46_cross_domain_variables.md` | 24 通用变量详表 | ~15K |
| 48 | `47_timing_rules_and_study_design_bridge.md` | ISO 8601 + Study Day + DM-TA-TV + ARM/ARMCD | ~20K |
| 49 | `48_rule_decisions_ig_core.md` | IG ch04 关键判断规则 (CM/AE/MH 拆分 / SAESUB 升级) | ~15K |
| 50 | `49_req_variable_coverage_audit.md` | **审计元 source**: 显式列本 notebook 覆盖的 Req 变量集合 + Q1=0 自证断言 | ~10K |

**总字数估**: ~720K words, 远低于 Pro tier 50 × 500K = 25M cap (占 cap ~2.9%).

**Req 变量全覆盖审计** (Phase A A4, **结构级** Q1 红线自证):
1. `extract_req_vars.py` 产 `req_vars_full_set.md` (~366 记录去重 ~100-120)
2. `cluster_req_variables.py` 产 `source_mapping.md`, 每 slot 附 `covered_req_set` 子集
3. **覆盖断言** (H2 fix — 蕴含式, 非集合等式):
   - **PASS 条件**: `∀ req ∈ req_vars_full_set, ∃ source ∈ uploads, 使 req.variable ∈ source.covered_req_set`
   - **FAIL 条件**: `∃ req ∈ full_set, ∀ source, req.variable ∉ source.covered_req_set` (即漏集)
4. 断言写进 `req_vars_coverage_audit.md` 结尾段 "Q1=0 红线**结构级**自证: 零漏集"
5. **注意**: 本 A4 是**结构级**审计 (变量名 ∈ source 文本), **不是语义级**验证 (NotebookLM RAG 能否召回). 语义级 Q1 红线自证在 Phase 3 P3.4.5 "Req 变量业务问答抽检 N=10" 完成 (M1 fix, 见 §6), 双锚闭合.
6. 规则 A 触发说明: 压缩 >50% 强制 N=10 独立抽检, 本平台 293→50 (压缩率 ~83%) 触发. N=10 抽检的**语义验证**挪到 P3.4.5 (见 §6), 本步仅作结构抽样 ≤5 (快速自检, 非 Rule A 正本)

### 3.3 分享档位策略 (3 档按需切换)

在**本次 Rule E ack 场景下** (ABC 三 scope + personal Gmail + 无 collaborator 圈职责隔离), Scope ABC 通过**同一 notebook 分享档位切换**实现 (L2 fix: 未来若 collaborator 圈需职责隔离, 再评估升级多 notebook):

| 日常态 / 场景 | Access Level | 允许访客 | 使用方式 |
|-------------|------|---------|---------|
| **Scope A / B 小圈组合 (默认)** | **Restricted** (L1 fix: 无邀请 = Scope A 私有; + invite 邀请 SDTM 小组 = Scope B 小圈, ≤50 specific emails personal Gmail 50-cap) | 仅 owner (Scope A 态) / ≤50 specific emails (Scope B 态) | 默认态 Scope A 私有, 按需邀请 ≤50 同事切 Scope B, 默认 Viewer, 极少数 Editor |
| Scope B/C 广覆盖分享 | **Anyone with link** | 任何 Google 账号拿到链接 | 发社区群 / 培训帖 / 会议群共享, 无 users 上限 |
| Scope C 公开发现 | **Public** | 任何 Google 账号, 可从 NotebookLM 画廊发现 | 极少用, 作 SDTM 社区示范 |

**切换流程** (UI 实测, Phase 3 末演练):
1. Owner (用户) 打开 notebook → 点 Share 按钮
2. 选 "Notebook access" 下拉: Restricted / Anyone with link / Public
3. 切到目标档位 → 生成/更新链接 (非 Restricted 时)
4. 若需 revoke: 回切 Restricted 档, 所有旧链接立即失效

**默认策略**: 日常 Restricted, 需分享时临时切, 分享任务完成后**回切 Restricted** 作为卫生规范.

**Enterprise/EDU 账号限制**: 本次用户 ack personal Gmail, 三档均可用. 若未来账号变动:
- Workspace Enterprise/EDU: 禁 Anyone with link / Public (Restricted 档则无 50-cap, 可邀请 Groups)
- 退化 fallback: workflow_replication (打包 uploads/ + UPLOAD_TUTORIAL 让接收者自建复刻)

### 3.4 Chat mode: Custom 默认 + 单 session 切换假设 (H3 fix: 待 Phase 3 P3.3 验证)

| 字段 | 值 |
|------|----|
| **notebook 级默认 mode** | **Custom** (Chat custom goals, ≤10,000 char) |
| **单 chat session 切换能力** | ✅ **VERIFIED PASS (2026-04-21 UI 实测, evidence `dev/evidence/chat_mode_toggle_test.md`)** — 同 chat session 可动态切换三档 (Default / Learning Guide / Custom), 无需 new chat; 切换后 source set 不变 (同 42 bucket RAG), response 风格与是否应用 Custom instructions 变化. Q-REV-1 CLOSED. 附带发现 F-1 (UI 支持表格但模型偶发 single-line malformed 输出, P3.4 前定锤) + F-2 (同题 retry 幂等性不强制, P3.8 评分规则补) |
| 文本文件 | `current/instructions.md` (≤10,000 char) |
| 角色定位 | "你是 SDTM 数据标准专家, 熟悉 CDISC SDTMIG 3.4, 精通 63 域 + terminology + IG 章节" |
| 行为约束 | "回答时必 inline citation 源 md, 不在知识库外编造, 遇边界问题坦诚 '未收录', 优先引权威 IG + domain spec, 术语以 terminology/core 为准" |
| 回答规范 | "高频 Q 给精确变量 + Core (Req/Exp/Perm) + codelist ID (C-code), 边界 Q 给 assumptions + IG 章节引, 混淆 Q 显式对比" |
| SDTM-specific 锚点 | STUDYID 7 字段 / AESER Core=Exp (区别 AE Req) / LBNRIND HIGH/LOW/NORMAL 全写非短码 / --ACN vs --ACT / NCI EVS 引用时字面 URL |

**替代的范本组件**: 范本 `05_solution.md` 的 "System Prompt 累积段设计" **不适用**, 用本段 instructions.md 单一文本替代 + 精选 source `00_navigation.md` 作首源导航 (双入口: Chat custom mode + notebook 首源).

**P3.3 验证产物** (事实回写): Phase 3 实测后, 将 "是否每 chat session 可切换三档" 的结论回写到 `platform_profile §D` + `research.md Q6` + 本 §3.4 "单 chat session 切换能力" 行.

### 3.5 Audio / Mind Map / Study Guide 侧重

> **[ICEBOX v2.1 2026-04-22 用户决策 A+保留]**: 本节定义的 Studio 三件套 (Audio Overview / Mind Map / Study Guide / Briefing Doc) 与 §6 P3.5/P3.6/P3.7 任务一起挪 post-project optional, **不计入 Phase 3 收束 gate, 不计入 Phase 4 跨平台对比**. 归因: Claude/ChatGPT/Gemini 均无等价独有产出, 无跨平台对比价值; 问答维度 (P3.4 / P3.4.5 / P3.8) 才是核心比较基线. 原设计保留供全项目 (Phase 5) 收束后用户选择性精雕, 触发条件 §10 "Post-project ICEBOX" 小节.

- **Audio Overview**: Deep Dive 长 podcast 3 期 (SAFETY group / EFFICACY group / PK group), 每期 30-45 min, 复用 source `02-03` / `11-14` / `14-17`
- **Mind Map**: 63 domain 跨域关系全景图, 优先回答 "X domain 依赖哪些? Y domain 被哪些引用?"
- **Study Guide**: IG 关键规则章节 (CM 拆分 / AE 升 SAE / QS-C 关联) 作 Socratic 引导
- **Briefing Doc**: SDTMIG 历史版本演进 (3.2 → 3.3 → 3.4 diff 概览, 外围资料)

---

## §4 执行步骤概览 (Phase A / 3 / 4 / 5)

| Phase | 主要 Task | 产出 | 估算工时 | Checkpoint |
|-------|----------|-----|---------|-----------|
| **Phase 2 v2 审** | 第 9 种 subagent_type 独立审本 PLAN | `dev/evidence/phase2_v2_reviewer.md` | 1-2 小时 | hard (主 session 接过再进 Phase 3) |
| **Phase A Setup** | A1 audit + A2 Req extract + A3 bucket + A4 coverage audit (结构级) + **A5' Web UI 小样实测 (M2 fix)** | 5 份 evidence + `uploads/MANIFEST.md` 草 + 小样实测 | 4.5-7.5 小时 (Q2 保险 9-15) | 全 hard |
| **Phase 3 P3.0** | Pre-flight check (re-run A1/A4 确保最新) | audit log | 0.5 小时 | soft |
| **Phase 3 P3.1** | (可选) 跑 `merge_sources.py` 合成 ≤50 个 source 文件 | `current/uploads/<source_N>.md` × ≤50 | 1-2 小时 | soft |
| **Phase 3 P3.2** | Web UI 建 notebook + 上传 ≤50 source (策略按 A5' 小样结果: 单批 or 分批) | notebook 创建 + sources 上传完 | 1-2 小时 (拖拽 + indexing) | hard (indexing smoke 前置) |
| **Phase 3 P3.3** | 贴 `instructions.md` 到 Chat custom goals Custom mode + **H3 切换能力验证 (新增子步骤 b/c)** | Custom mode 激活 + `chat_mode_toggle_test.md` | 30 分钟 | soft |
| **Phase 3 P3.4** | Indexing smoke test (每 source tile 点开预览 + **10 题分布式问答, M3 fix**) | `dev/evidence/indexing_smoke.md` | 1.5 小时 | hard (silent fail 防线 + RAG 检索双验证) |
| **Phase 3 P3.4.5** (M1 fix) | **Req 变量业务问答抽检 N=10** (Q1 红线语义级自证, 规则 A 正本) | `dev/evidence/phase3_task_P3.4.5_req_semantic_audit.md` | 2 小时 | **hard** (Q1 红线 10/10 必过) |
| ~~Phase 3 P3.5~~ **[ICEBOX]** | Audio Overview × 3 (SAFETY/EFFICACY/PK) — **挪 post-project optional (v2.1 2026-04-22)**, 原任务定义保留 §6 P3.5 | — | — | **ICEBOX** (non-gating) |
| ~~Phase 3 P3.6~~ **[ICEBOX]** | Mind Map + 跨域关系验证 — **挪 post-project optional (v2.1)**, 原任务定义保留 §6 P3.6 | — | — | **ICEBOX** (non-gating) |
| ~~Phase 3 P3.7~~ **[ICEBOX]** | Study Guide × 3 + 人工读 — **挪 post-project optional (v2.1)**, 原任务定义保留 §6 P3.7 | — | — | **ICEBOX** (non-gating) |
| **Phase 3 P3.8** | **10 SMOKE v3 Q1-Q10 A/B** (跨 4 平台对比基线, v2.2 2026-04-22 升级对齐 ChatGPT+Gemini N5.3; 原 5 独有题随 P3.5-3.7 一起 ICEBOX) | `dev/ab_reports/notebook_ab.md` | 1.5-2 小时 | hard (**≥9/10 PASS**) |
| **Phase 3 P3.9** | 3 档切换演练 (Restricted → Anyone with link → Public → 回 Restricted) | `dev/evidence/share_level_toggle_drill.md` | 30 分钟 | hard |
| **Phase 4** | 跨 4 平台对比 + 回归 + 规则 A N=10 独立抽检 + 第 10 种 subagent_type 审 | `cross_platform_compare.md` + `phase4_reviewer.md` | 2-3 小时 | hard |
| **Phase 5** | RETROSPECTIVE (含 pivot 复盘) + UPLOAD_TUTORIAL + CLAUDE.md / MANIFEST / worklog / PROGRESS 更新 + `_template/` 10 补丁 PR + commit + push | 3 份终 doc + 多点更新 | 3-5 小时 | hard (规则 D 独立审) |

**Phase 3 总估工时** (v2.1 2026-04-22 ICEBOX 决策后): ~**7-10 小时** (Q2 保险 2x = 14-20 小时, 跨 1-2 天) — 含 P3.0 + P3.1 + P3.2 + P3.3 + P3.4 + P3.4.5 + P3.8 (10 SMOKE) + P3.9; **P3.5/P3.6/P3.7 ICEBOX 节省 ~2.5h + P3.8 缩 5 独有节省 ~1h** = 合计 -3.5h. (原 v2 估值 10-14h / 保险 20-28h 保留作 post-project 精雕参考.)

---

## §5 动作清单

1. **Phase 2 v2 审**: 派第 9 种 subagent_type (前 8 种外) 独立审本 PLAN, 锚定 Q1 红线在 pivot 过程未被破坏, 审架构决策自洽性
2. **Phase A1 pre-audit**: `wc -w` 排序 293 md, 确认无 >500K words outlier
3. **Phase A2 Req extract**: 跑 `extract_req_vars.py`, 产 `req_vars_full_set.md`
4. **Phase A3 bucket**: 跑 `cluster_req_variables.py` → `source_mapping.md` + `uploads/MANIFEST.md`
5. **Phase A4 audit**: diff 全集 vs bucket, 断言 ∅ gap, 规则 A N=10 抽检
6. **Phase A 完收 commit + 用户 hard checkpoint ack**
7. **Phase 3 上传 + indexing smoke + Custom mode + ~~独有产出生成~~ (ICEBOX v2.1 2026-04-22) + 10 SMOKE v3 Q1-Q10 A/B (v2.2 2026-04-22 升级) + 3 档切换演练** (Studio 三件套 P3.5/P3.6/P3.7 挪 post-project optional, 本次 Phase 3 直接从 P3.4.5 跳到 P3.8)
8. **Phase 4 跨平台对比 + 规则 A + 第 10 种 subagent_type 审**
9. **Phase 5 RETROSPECTIVE (含 pivot 复盘作关键案例) + UPLOAD_TUTORIAL + 收束 commit + push**

---

## §6 Task 分解 (简化 v2)

### P3.0 Pre-flight check (0.5 小时)

- 子步骤: re-run A1 + A4, 确认 evidence 最新 (无 knowledge_base/ 非预期变化)
- Checkpoint: soft
- 失败处理: 回 Phase A 重跑对应 task

### P3.1 (可选) merge_sources.py (1-2 小时)

- 子步骤: 按 `source_mapping.md` 自动合成 ≤50 个 source md 文件到 `current/uploads/`
- Checkpoint: soft
- 失败处理: 手工合并 (P4 checkpoint 作备)

### P3.2 notebook 建 + 上传 (1-2 小时)

- 子步骤: (a) 登 notebooklm.google.com → New notebook → 命名 "SDTM Knowledge Base" (b) 拖拽 `current/uploads/*.md` 全选上传 (≤50 个, Web UI 单批批量支持) (c) 等 indexing 完成
- Checkpoint: **hard** (上传完成 + indexing smoke 跟)
- 失败处理: 单文件 retry (NotebookLM 官方承认 silent fail); 规则 B 归档 failure record

### P3.3 Custom mode 激活 + 切换能力验证 (H3 fix, 30 分钟)

- 子步骤 (a): Chat → Configure → Custom mode → 贴 `instructions.md` 全文 (≤10K char) → Save
- 子步骤 (b) **H3 验证 (新增)**: 开一次 chat, 尝试切换三档 (Default → Learning Guide → Custom), 观察:
  - UI 是否允许每 chat session 切换 (PASS = Yes / FAIL = notebook 级锁定单一)
  - 切换 Learning Guide 后是否仍引用同一 source set (PASS = 是) 但 response 风格改变 (PASS = 是)
  - 切回 Custom 是否 instructions.md 仍生效 (PASS = 是)
- 子步骤 (c) **事实回写** (基于 b 结果): 把 "单 chat session 切换能力" 结论回写到 `docs/research.md` Q6 + `docs/platform_profile.md` §D + `docs/PLAN.md` §3.4 对应行 + `dev/evidence/chat_mode_toggle_test.md` (本次验证 evidence 留档)
- Checkpoint: **soft** (验证是增值信息, 不阻塞 P3.4 smoke)

### P3.4 Indexing smoke test (M3 fix: 题数 3 → 10, 1.5 小时)

- 子步骤 (a): 点**每** source tile 预览确认内容存在且格式未乱 (≤50 source 全扫)
- 子步骤 (b) **smoke 题扩 N=10** (M3 + S2 fix): 选 10 个 source (首 source_01 + 末 source_50 + 中间 8 个随机), 每题:
  - 题本身针对该 source 独有内容 (建议至少 1 题选 **non-core domain** 如 DD/HO/ML 的独有 Req 变量, 测 "findings_other" bucket 18-22 的 RAG 信号强度, S2 fix)
  - 看 citation 是否**精确回指**该 source (主 session 对照 `source_mapping.md` 确认)
  - 记录 PASS/FAIL 比例
- PASS 阈值: 10/10 citation 精确回指 (≥9/10 可接受, 但 10/10 是目标)
- Checkpoint: **hard** (silent fail 防线 + RAG 检索验证双防, 不过 gate 不进 Audio/Mind Map)
- 失败处理: 删重上传对应 source + 规则 B 归档; 若 <8/10 PASS 触发 cluster bucket 重分 (Phase A A3 回炉)

### P3.4.5 Req 变量业务问答抽检 N=10 (M1 fix, 2 小时, Q1 红线**语义级**自证)

**规则 A 正本** (用户规则 A: "压缩 >50% 必 N 样本独立抽检", 本平台 293→50 压缩率 83% 触发):

- 子步骤 (a): 主 session 从 `req_vars_full_set.md` 独立随机抽 10 个 Req 变量 (优先选 non-core domain 的, 覆盖 "findings_other" bucket 信号弱区)
- 子步骤 (b): 每个变量构造**业务问答题** (不是字典式变量名查询), 例如:
  - "某 SDTM 域记录 X 事件, 按 SDTMIG 要求哪些变量必填?" (测 Req 变量召回 + Core 属性)
  - "Y 变量的 controlled terminology 是哪个 codelist? C-code?" (测跨 source 召回)
  - "Z 变量在哪些 domain 出现? 语义一致吗?" (测跨 domain 召回)
- 子步骤 (c): Chat 中问每题, 看 NotebookLM:
  - 是否命中正确 Req 变量 (10/10 必 PASS, Q1 红线)
  - citation 是否精确回指 ≥1 个预期 source (9/10 PASS 接受)
- PASS 阈值: **10/10 Req 变量业务问答命中** (结构级 A4 + 语义级本步 P3.4.5 双锚闭合 Q1 红线)
- 产物: `dev/evidence/phase3_task_P3.4.5_req_semantic_audit.md` (10 题 + 答案摘录 + citation 精度 + PASS/FAIL 表)
- Checkpoint: **hard** (Q1 红线语义级自证必过, 不过 gate 不进 P3.8) [v2.1 2026-04-22: 原 "不进 P3.5/3.6/3.7 独有产出" 因 Studio 三件套 ICEBOX 改指 P3.8]
- 失败处理: (a) 漏变量 → cluster bucket 回炉 (Phase A A3) (b) citation 不精确 → instructions.md 加强 citation 约束 (c) RAG 召回跨 source 噪声 → source 合并粒度调整

### P3.5 Audio Overview × 3 (生成 30 分钟 + 听 1-2 天) — **[ICEBOX v2.1 2026-04-22]**

> **ICEBOX 决策 (2026-04-22 用户方案 A+保留)**: 本任务挪 post-project optional, **不计入 Phase 3 收束 gate, 不计入 Phase 4 跨平台对比**. 归因: Audio Overview 为 NotebookLM 独有, Claude/ChatGPT/Gemini 均无等价功能, 无跨平台对比价值. 原任务定义保留如下供全项目 (Phase 5) 收束后用户选择性精雕 (触发条件 §10 "Post-project ICEBOX" 小节):

- 子步骤: (a) Audio Overview → Deep Dive × 3 (SAFETY / EFFICACY / PK 主题各 prompt) (b) 每期 30-45 分钟, 用户抽听 (c) 录事实错误数 + 对照 source 核
- Checkpoint: ~~soft (∃ <10% hallucination 算 PASS)~~ → **ICEBOX (non-gating)**
- 失败处理: instructions.md 微调 (加 "基于 source 绝不脑补") 再跑 1 期; per-day 20 cap 内可 retry

### P3.6 Mind Map + 3.7 Study Guide (各 30-60 分钟) — **[ICEBOX v2.1 2026-04-22]**

> **ICEBOX 决策 (2026-04-22 用户方案 A+保留)**: P3.6/P3.7 同 P3.5 一起挪 post-project optional. 归因同上 (独有无跨平台对比价值). 原任务定义保留如下:

- Mind Map: 生成 → 导出 PNG → 对照 63 domain 清单 checklist
- Study Guide: 3 个 domain (AE / LB / CM) 各生成一份, 人工读

### P3.8 10 SMOKE v3 Q1-Q10 A/B (1.5-2 小时) — v2.2 升级

- **10 SMOKE v3 Q1-Q10** (共享 ChatGPT / Gemini 跨平台对比基线, 见 `ai_platforms/smoke_v3_questions_draft.md` v3.1; Q11-Q14 ChatGPT 专属不适用 NotebookLM)
- **v2.2 升级背景** (2026-04-22): ChatGPT+Gemini 已在 Phase 4 N5.3 跑 smoke v3 Full A/B Generalization Probe; smoke v2.1 10 题全落入 ChatGPT 04 业务弹药 §1.1-§1.10 预设 scenario = open-book 考试, 对 NotebookLM 42 bucket 全域 RAG 也没鉴别力; v3 故意避开 04 预设, 测真 SDTM 泛化能力 (v3.4 新域 GF/CP/BE+BS / 域边界 LB-MB-IS / FA-QS-CE / Timing 四件套 / Partial date / Extensible CT / Pinnacle 21 FAIL 分类 / SUPP 深化)
- **题型分布 (Q1-Q10)**:
  - Q1 A1 v3.4 新域 GF (Genomics Findings) 基因变异场景
  - Q2 A2 v3.4 新域 CP (Cell Phenotype) 流式细胞场景
  - Q3 A3 v3.4 新域 BE + BS + RELSPEC 生物样本全流程
  - Q4 B1 域边界 LB vs MB vs IS 三场景归属
  - Q5 B2 域边界 FA vs QS vs CE 三场景归属
  - Q6 C1 Timing 深化 `--TPTREF/--TPT/--STTPT/--ENTPT/--DUR` 组合
  - Q7 C2 Timing 深化 Partial date 精度 + imputation 规则
  - Q8 D1 CT 深化 Extensible vs Non-Extensible codelist
  - Q9 E1 实战验证 Pinnacle 21 常见 FAIL 分类
  - Q10 H1 SUPP 深化 QORIG/QEVAL/QLABEL + SUPPTS vs SUPP--
- ~~5 独有 (Audio 2 + Mind Map 2 + Study Guide 1)~~ **ICEBOX v2.1 2026-04-22** (随 P3.5/P3.6/P3.7 一起挪 post-project optional)
- 产 `dev/ab_reports/notebook_ab.md`
- Checkpoint: **hard** (**≥9/10 PASS** ~90%, <9 走 P10 归因重构)
- **阈值说明**: ChatGPT smoke v3 合格阈 ≥10/14 (71%) 因 4 题专属; Gemini ≥7/10 (70%); NotebookLM 保 **≥9/10 (90%)** 按用户决策不降 — Gemini 70% 是首次跑生疏平台预留 buffer, NotebookLM 此前 P3.4.5 已 CONDITIONAL_PASS 8.5/10, 有底座, 不给额外 buffer
- **题源单点变更**: 执行时从 `ai_platforms/smoke_v3_questions_draft.md` 取 Q1-Q10 题干 (遇 v3.1→v3.x 继续修订以最新为准); 判据按该文件每题 PASS/FAIL + PARTIAL 规则
- **Sanity 前置** (对齐 ChatGPT N5.3 Step 2, 避免底座问题吃成业务 FAIL): 3 题 sanity (AESER Core / LBNRIND 全写 / CMINDC 场景), 全 PASS 才进 Q1-Q10
- **吸收 Phase 3 carry-over** (P3.4.5 转过来的):
  - F-1-recurring 持续跟踪 (小表渲染漂移, 小表单行漂移不扣语义分; 原放 P3.5/3.6/3.7 监测, ICEBOX 后挪 P3.8)
  - F-2 同题 retry 幂等性不强制 (语义等价即 PASS)
  - F-3 citation dropout T2 题型偏向 (业务场景/举例类 T2 题易丢 inline cite, 记为系统性弱点, 不扣 A/B 题分但 Retro 关键教训)
  - HC-3 bucket 38 尾段补题 (候选 PHQ-9/PDQ-39/PGI, 避 FT 域归属题) — **v2.2 note**: v3 Q1-Q10 无 bucket 38 专属题, HC-3 补题若要跑需作第 11 题单独计, 不混入 ≥9/10 分母 (分母固定 10)

### P3.9 3 档切换演练 (L3 fix + S1 SUGGESTION, 40 分钟)

- 子步骤 (a): Restricted (默认) → 截屏 share panel
- 子步骤 (b): 切 Anyone with link → 生成链接, 匿名窗口 (非 Google 账号) 试打开 (应被要求登录) → 换另一 Google 账号打开 (应能看到 notebook)
- 子步骤 (c): 切 Public → 在 NotebookLM 公开画廊搜
- 子步骤 (d): 回切 Restricted → 测旧链接是否失效
- 子步骤 (e) **L3 fix 快速多次切换**: 连续 Restricted ↔ Public 2 次, 第二次 Public 再生成链接, 用原第一次 Public 链接测是否仍可访问 (预期 revoke). 验证档位切换无 caching 残留
- 子步骤 (f) **S1 SUGGESTION**: 若有 Free tier Gmail 小号, 切 Restricted + invite 档邀请小号, 小号登录查看 notebook 能看到多少 source (≤50 都能看 = 证据 3 解读 A + B 都 OK / 仅能看前 50 sources = 解读 A 成立 / 其他情况 → evidence 3 需深查)
- 产出: `dev/evidence/share_level_toggle_drill.md` (4+ 态截屏 + PASS/FAIL 表 + 证据 3 解读闭合结论)
- Checkpoint: **hard**

---

## §7 A/B 矩阵 (v2.2 2026-04-22 后: 10 题 SMOKE v3 Q1-Q10; 5 独有 ICEBOX)

### 10 SMOKE v3 Q1-Q10 (从 `ai_platforms/smoke_v3_questions_draft.md` v3.1 继承, 对齐 ChatGPT+Gemini N5.3 Full A/B Generalization Probe)

题型分布 (v3 generalization 取向):
- A1/A2/A3 v3.4 新域 (GF / CP / BE+BS+RELSPEC) × 3
- B1/B2 域边界 (LB-MB-IS / FA-QS-CE) × 2
- C1/C2 Timing 深化 (--TPTREF 组合 / Partial date imputation) × 2
- D1 CT 深化 (Extensible vs Non-Extensible) × 1
- E1 实战验证 (Pinnacle 21 FAIL 分类) × 1
- H1 SUPP 深化 (QORIG/QEVAL + SUPPTS vs SUPP--) × 1

判据按 `smoke_v3_questions_draft.md` v3.1 每题末尾 PASS/FAIL + PARTIAL (含 v3.0→v3.1 双 reviewer 修复: Q3 采血 BE+BS 并存 / Q4 MB 免疫应答 PARTIAL / Q5 FA→MH + CE 边界 / Q10 QVAL 归因 ch04 §4.5.3.2 / Q14 DSDECOD C66727 — Q14 ChatGPT 专属对 NotebookLM 不适用).

**v2.1 SMOKE v2 基线废弃备注**: `ai_platforms/SMOKE_QUESTIONS_V2.md` v2.1 10 题 2026-04-22 决策废弃作 P3.8 基线 (见 §0 v2.2 修订记录); v2 题本身不错, 只是 ChatGPT+Gemini 已在 N5.3 切 v3, NotebookLM 若跑 v2 对比基线是两平台 N5.2 阶段历史快照 (ChatGPT 10/10 strict / Gemini 9/10 strict), 不是 N5.3 当前阶段, 无跨平台同期可比性.

### ~~5 独有生成物评估~~ — **[ICEBOX v2.1 2026-04-22]**

> **ICEBOX 决策 (2026-04-22 用户方案 A+保留)**: U1-U5 随 §6 P3.5/P3.6/P3.7 一起挪 post-project optional, **不计入 Phase 3 ≥9/10 PASS 阈值分母**. 归因: Audio/Mind Map/Study Guide 独有产出无跨 4 平台对比价值 (其他 3 平台均无等价功能). 原评估定义保留如下供全项目收束后精雕:

| # | 类型 | 题 | 评估方式 |
|---|------|---|---------|
| U1 | Audio Overview fidelity (高覆盖期) | 抽 SAFETY 组 Deep Dive 听 15 分钟, 勾事实错误 | ≤3 错误 PASS |
| U2 | Audio Overview fidelity (边界期) | 抽 PK 组 Deep Dive 听 10 分钟 (PK 偏少数 domain, 测边界) | ≤2 错误 PASS |
| U3 | Mind Map coverage (RELREC) | 生成 Mind Map, 查 "RELREC 关系" 是否覆盖所有会出现 RELREC 的 domain (AE/CM/MH/DS 等 10+) | ≥9/10 核心 domain 命中 PASS |
| U4 | Mind Map coverage (SUPP--) | 查 "SUPPQUAL 扩展" 是否覆盖所有 63 domain 的 SUPP-- pattern | ≥80% 有 SUPP 例的 domain 有标注 PASS |
| U5 | Study Guide 分层 | 生成 "AE 域 Socratic" Study Guide, 检查覆盖 Standard → IG → Examples 三层 | 三层齐全 PASS |

### PASS 阈值 (v2.2 更新)

- **总分 ≥9/10 (~90%)** (v2.1 ≥9/10 保留, v2.2 题库换 v3 Q1-Q10 但难度升 baseline → generalization probe, 阈值**不降**按用户 2026-04-22 决策)
- **阈值不对齐 ChatGPT/Gemini 的解释**: ChatGPT ≥10/14 (71%) 含 4 题专属且 generalization 难; Gemini ≥7/10 (70%) 因 Gemini 本轮首过 v3 预留 buffer; NotebookLM 保 ≥9/10 (90%) 因 P3.4.5 已 CONDITIONAL_PASS 8.5/10 验底座稳, 不给额外 buffer
- ~~AND 每个独有产出至少 1 题 PASS~~ (ICEBOX 后此子条删除)
- **Req 变量零丢失** 独立自证 (A4 结构级 + P3.4.5 语义级双锚, 非 A/B 题里; 已于 2026-04-22 P3.4.5 CONDITIONAL_PASS 闭合)
- <9 触发 P10 归因: (a) source 缺失重 bucket / (b) instructions.md 微调 / (c) Chat mode 切回 Learning Guide 再测 / (d) **v3 新增**: 若 FAIL 集中在 v3.4 新域 (Q1-Q3 GF/CP/BE+BS), 触发 knowledge_base/ v3.4 新域覆盖审 (部分 v3.4 新域 KB 本身可能不全)

---

## §8 风险与回退

| # | 风险 | 概率 | 影响 | 缓解 | 回退 |
|---|------|-----|------|------|------|
| R1 | Indexing silent fail 漏几个 source | 中 | 中 (A/B 部分题 FAIL) | P3.4 smoke 前置 gate, 每 source tile 预览确认 | 删重上传对应 source + 规则 B 归档 |
| R2 | ≤50 slot 不够覆盖 Req (cluster 合并不到位) | 低 (slot 比 v1 的 30 宽松) | 高 (Q1 红线破) | A4 coverage audit 强制 ∅ gap, 规则 A N=10 抽检 | slot 从 50 扩到 55-60 (Pro 300 cap 内) + cluster 重分 |
| R3 | Audio Overview hallucination >10% | 中 | 低-中 (U1/U2 可能 FAIL) | instructions.md 加 "绝不脑补" 约束, per-day 20 retry | 换 Brief format; 若持续 FAIL 作 U1/U2 单题弃 (总分有容错) |
| R4 | 3 档切换中 Anyone with link 链接访问失败 (Google 账号限制) | 低 | 中 (P3.9 gate) | 用至少 2 个独立 Google 账号实测 | workflow_replication fallback; 或仅 Restricted + invite 档 + workflow_replication 组合 |
| R5 | 用户发现 v2 PLAN 仍有盲区 | 低 (第 9 种 subagent_type 架构级审) | 高 (可能再 pivot) | 第 9 种独立 reviewer 架构级审 + 用户 ack 才进 Phase 3 | 再次 pivot, 复用本次 pivot 流程 (archive + 重写) |

---

## §9 收束 (Phase 5)

按全局 CLAUDE.md "收尾" 规则 + 本 PLAN 补充:

1. **RETROSPECTIVE.md (规则 C 强制)** — 三段式:
   - 保留下来的做法 (v2 方法论 + Rule D 9-chain)
   - 必须补上的缺口 (pivot 前 Rule D 为何未捕获 3 notebook 伪约束?)
   - **关键决策复盘 (含本次 pivot)** — 作典型案例 "Writer 叙事合成伪约束, 用户反问是关键救援路径"
2. **UPLOAD_TUTORIAL.md** (10 章节, 单 notebook 路径, 含 3 档切换使用说明)
3. **ROADMAP.md** 状态 → "已完成", 实际 source 数 / A/B 数据 / 3 档切换结果填入
4. **`_template/` 10 补丁候选 PR**
5. **父目录更新**: `.work/MANIFEST.md` / `.work/meta/worklog.md` / `docs/PROGRESS.md` / `CLAUDE.md` Key Paths (加 notebooklm 入口)
6. **Commit + push**

**规则 C 要求独立 Reviewer 过 RETROSPECTIVE.md**: 第 11-13 种 subagent_type (Phase 3-5 每阶段 1-2 种新 subagent_type, 5 Phase 总共至少 12 种新 subagent_type 跨 Phase 0-5 + pivot)

---

## §10 Carry-over 跟踪

### 从 Phase 1 继承 (v1 → v2 保留)

- **Inherit R1**: SDTM pre-upload audit (A1) / Chat mode Custom selector (P3.3) / personal Gmail + share-level toggle (§3.3)
- **Inherit Q1**: 0 Req variable loss (v2 slot 更宽松下仍强制)
- **Inherit Q2**: quality first, no rush

### v1 carry-over 被 pivot close

| v1 carry-over | v2 处置 |
|--------------|---------|
| **I8** (Mode B 50-cap 实测) | **CLOSED** 2026-04-21 (WebFetch: 仅 Restricted 套 50-cap) |
| **C2.9** (Mode B cap UNVERIFIED) | **CLOSED** 2026-04-21 (同 I8) |
| **I9** (Chat mode UI 截屏) | 保留, Phase 3 P3.3 产出 |
| **I11-I14** (v1 Phase 2 R4 建议: 文件名统一 / tier 核实 / §5 双源 ack / 编号倒置) | **v2 inapplicable** (v1 §5/§6 被重写) |

### v2 新增 Phase 3 carry-over

- **CO-V2-1** (P3.4 indexing smoke 前置 gate 产出) — Phase 3 hard checkpoint, 不 PASS 不进 Audio/Mind Map
- **CO-V2-2** (P3.9 3 档切换演练 + 截屏 evidence) — 本平台独有 UI 演练
- **CO-V2-3** (A4 Req ∅ gap audit) — Q1 红线自证

### Phase 4 预留

- Rule A 独立抽样 N=10 (规则 A, 压缩 >50% 必 N)
- 跨 4 平台 10 SMOKE **v3 Q1-Q10** 对比 (Claude / ChatGPT / Gemini / NotebookLM) — v2.2 2026-04-22 升级; Claude v2.6 原测 v2.1 需补 v3 回归或接受 Claude 异步基线 (Phase 4 决策点)

### Phase 5 预留

- RETROSPECTIVE 过规则 D 独立审 (第 11-13 种 subagent_type)
- `_template/` 10 补丁 PR (ai_platforms/_template/ 只在 Phase 5 写入)

### Post-project ICEBOX (v2.1 2026-04-22 用户决策 A+保留)

> 全项目 (Phase 5 收束 + commit/push + CLAUDE.md Key Paths / MANIFEST / worklog / PROGRESS 全刷新) 完成后, 若用户有精力 + 无新优先级, 可选回头做. **触发条件**: 用户主动提出 "回头精雕 NotebookLM Studio 三件套" 或 "把 P3.5/P3.6/P3.7 补做". **不触发时永久 ICEBOX, 不影响本次 Phase 5 收束完整性**.

- **P3.5 Audio Overview × 3** (SAFETY / EFFICACY / PK Deep Dive, 每期 30-45 min) — 原定义 §6 P3.5 保留
- **P3.6 Mind Map + 跨域关系验证** (63 domain 全景 + RELREC/SUPPQUAL 覆盖 checklist) — 原定义 §6 P3.6 保留
- **P3.7 Study Guide × 3** (AE / LB / CM 各一份, Socratic 引导) — 原定义 §6 P3.7 保留
- **A/B 5 独有题 U1-U5** (Audio fidelity ×2 + Mind Map coverage ×2 + Study Guide layering ×1) — 原定义 §7 保留, 随 Studio 三件套一起恢复时一并评估

**重开流程**: 用户 ack → 读本节 + §6 / §7 原任务定义 → 开新分支 (不污染主 retrospective) → 生成产物 + 评估 → 补 RETROSPECTIVE Appendix + _template/ 新补丁候选 (若有).

---

## §11 附录 — v2 方法论自检

### 本 PLAN 诞生流程与 Rule D 合规

1. **Writer** = 主 session (pivot 后重写) — **非 subagent**, 作为过渡产物
2. **Reviewer** = 第 9 种 subagent_type (oh-my-claudecode:architect, 前 8 种外) 独立审 — 已于 2026-04-21 PM 完成, 产 `dev/evidence/phase2_v2_reviewer.md` Verdict CONDITIONAL_PASS 84% (3 HIGH 全修 + 5 MEDIUM 全修 + 5 LOW 全修)
3. **Rule D 合规性分析**: 主 session 写作 + 独立 subagent 审核, 两 lane 不同 context, 不同 subagent_type — **合规**
4. **本次 pivot 流程自检** (M4 fix — 归因深化 3 层, 规则 C 预写):
   - **保留下来**: Rule D 严格 + 证据驱动 + 用户 Q1/Q2 ack 不松 + 第 9 种 subagent_type 架构级独立审 catch 住多条 v2 自身的伪约束 (H3 Chat mode / M5 证据 3 归因 / L2 "只能"口径)
   - **必须补上 (3 层审查盲区, M4 深化)**:
     - **层 1 (Writer 叙事范式)**: v1 Q7 "Mode A/B 两独立" 被 8 种 subagent_type **全部继承**, 无回 WebFetch 原文核对. **范式锁定**问题, 与 subagent_type 多样性无关. 补丁 **#10a** (`_template/03_research.md` Writer 立场警示).
     - **层 2 (跨 Phase 回溯盲)**: Reviewer 审查焦点由前 Phase 提供 spec 决定, **不会倒回去质疑 research**. v1 Phase 2 reviewer 只审 planner 推论, 不质疑 research 源头叙事. 补丁 **#10b.1** (`_template/04_plan.md` planner 接 research 时加 "**核心约束原文回溯**" 段, 强制回 Phase 1 A 级 URL 原文).
     - **层 3 (用户反问作最后防线)**: 用户 review 是**外部触发**, 不是 Rule D 链的胜利. Rule D 在架构级盲区上不足, 需要 Rule E (用户优先级) 的反向审查机制作补. 补丁 **#10b.2** (`_template/04_plan.md` + `_template/06_review.md` 加 "**Phase 2 PASS 前用户反问 gate**" — Phase 2 PASS 前主 session 必主动**向用户提一次开放式反问** "本 PLAN 有没有看起来过重 / 过复杂 / 违反直觉的地方?", 作架构级盲区防线).
   - **关键决策**: 用户 review 质疑是 pivot 救援; 第 9 种 subagent_type (architect) 再 catch H3/M5/L2; 教训: Rule D 8 lane 都过不等于架构没问题, 必须有架构级 reviewer + 用户反问 gate 双锚.

### 第 9 种 subagent_type 选择 (已完成)

**已派**: `oh-my-claudecode:architect` (Phase 2 v2 Reviewer, 2026-04-21 PM 完成)

- Verdict: **CONDITIONAL_PASS 84%** (3 HIGH + 5 MEDIUM + 5 LOW + 3 Q-REV 全 ack + 5 SUGGESTION)
- 产物: `dev/evidence/phase2_v2_reviewer.md` (主 session 代写落盘, reviewer read-only)
- HIGH 级 findings 全部已在本 PLAN v2 此轮修订中闭合 (H1 §3.2 契约 / H2 §3.2 蕴含式断言 / H3 §3.4 + §6 P3.3 验证子步骤)
- MEDIUM 级全部闭合 (M1 P3.4.5 / M2 A5' / M3 P3.4 smoke 扩 / M4 §11 归因 3 层深化 + 补丁 #10a/10b / M5 engrained #6 归因降级)
- LOW 级全部闭合 (L1 §3.3 合并 / L2 Executive Summary + §3 前缀 / L3 P3.9 子步骤 e / L4 research.md 重复段删 / L5 Writer #2 日志废止提醒)
- Q-REV 主 session auto mode 默认 ack: Q-REV-1 接受假设待验证 / Q-REV-2 接受 A5' / Q-REV-3 接受双锚 (已在本 PLAN 修订中落实)

### Rule D 链 9-lane 完整性

| # | Subagent type | Phase | 产物 |
|---|--------------|-------|------|
| 1 | general-purpose | P1 Writer #1 | research.md 初版 |
| 2 | oh-my-claudecode:verifier | P1 Reviewer #1 | phase1_reviewer.md (已归档) |
| 3 | oh-my-claudecode:executor | P1 Writer #2 | research.md 修正版 |
| 4 | oh-my-claudecode:critic | P1 Reviewer #2 | phase1_reviewer2.md (已归档) |
| 5 | oh-my-claudecode:planner | P2v1 Writer #3 | PLAN_v1 (归档) |
| 6 | oh-my-claudecode:analyst | P2v1 Reviewer #3 | phase2_reviewer.md (归档) |
| 7 | feature-dev:code-architect | P2v1 Writer #4 | PLAN v1.1 (归档) |
| 8 | pr-review-toolkit:code-reviewer | P2v1 Reviewer #4 | phase2_reviewer2.md (归档) |
| — | 主 session (非 subagent) | **P2v2 Writer (pivot)** | PLAN.md v2 |
| **9** | **oh-my-claudecode:architect** | **P2v2 Reviewer (第 9 种)** | **phase2_v2_reviewer.md (本次)** |

Phase 3/4/5 继续延伸 Rule D 链 (目标第 10-13 种 subagent_type), 每阶段至少 1 种新类型.

### 审查焦点 (给第 9 种 subagent_type)

1. Q1 红线 (0 Req 变量丢失) 在 slot 从 30 → ≤50 过程中是否**更易守**? 还是引入新漏?
2. 三 WebFetch 证据链是否闭合? 有无 UI 未验证假设?
3. §3.3 分享档位策略是否覆盖用户 ABC 三场景完整使用旅程?
4. Phase A 简化 (A5 降级) 是否丢失了必要前置动作?
5. P12 降级是否真的无风险? 有无边界场景需要 hard rule?
6. §6 Task 分解相对 v1 是否确实干掉了伪复杂度, 而非丢了必要步骤?
7. RETROSPECTIVE.md 预写段 (§11) 对 pivot 教训的归因是否到位?
8. 本 PLAN 自身是否有新的"叙事合成伪约束" (e.g. 某句 "Scope X 只能通过 Y 实现")?

---

*v2 重写日期: 2026-04-21 (架构 pivot 同日). 来源: Phase 1 research.md v2 + user Rule E ack + user Q1/Q2 ack + 2026-04-21 pivot 决策 (见 `archive/v1_.../ARCHITECTURE_PIVOT_RECORD.md`).*
