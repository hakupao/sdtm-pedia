# NotebookLM 平台部署 PLAN v2 (2026-04-21 架构 pivot 后重写)

> **产出时间**: 2026-04-21
> **Writer**: 主 session (pivot 后重写, 非 subagent) — 作为 v1 → v2 架构修正过渡产物
> **审查链扩展**: v1 Phase 2 已烧 8 种 subagent_type (general-purpose / verifier / executor / critic / planner / analyst / code-architect / pr-review-toolkit:code-reviewer); v2 本 PLAN 计划派第 9 种独立 subagent_type 架构级审
> **所属 Phase**: 2 PLAN v2 (Phase 1 Research 已 PASS, Q7+§11 已 v2 重写)
> **项目 Tier**: **Tier 2** (5-15 step, 半天-1 天级)
> **v2 架构背景**: `archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md` 强制前读

---

## 执行摘要 (Executive Summary)

把 SDTM 293 md 知识库部署到 **NotebookLM Pro tier 单 notebook**, 采用 **concept cluster 合并到 ≤50 sources** 策略 (Pro 300 slot 的 16.7%, 主动压缩到 Free tier viewer 兼容水位). Scope ABC 三场景 (个人学习 / 小圈分享 / 公开分享) 通过**同一 notebook 的 3 档 Access Level 切换** (Restricted / Anyone with link / Public) 实现, 不使用多 notebook.

关键风险已降低: 最坏上传 ~50 次 (v1 最坏 353 次的 14%), A/B 题次 15 (v1 的 33%), indexing silent fail 风险面降低 ~85%, Req 零丢失在 50 slot 下比 v1 的 30 slot 更易守.

Q1 红线 (0 Req 变量丢失, 用户 2026-04-21 ack) 在 v2 下**向内收紧**: 50 slot 给 concept cluster 留更多 outlier 容错余地, 实现路径 `extract_req_vars.py` → 全集清单 → `cluster_req_variables.py` → ≤50 bucket → `req_vars_coverage_audit.md` ∅ gap 断言.

A/B 矩阵 15 题 (10 SMOKE v2 + 5 独有生成物评估), PASS 阈值 ≥13/15 (~87%). 分享档位在 Phase 3 末做一次 3 档切换演练 (不需要多 notebook 测试).

---

## Project Success Criteria (v2)

SDTM 1 notebook 部署的**业务成功定义**. 用户 2026-04-21 ack:

1. **Quality**: 单 notebook A/B ≥13/15 (~87%) AND **Req 变量零丢失** (Q1 红线) + 独有 5 题 ≥4/5 精确命中
2. **Completeness**: notebook + `instructions.md` + `UPLOAD_TUTORIAL` 10 章节 + `uploads/MANIFEST.md` + `cross_platform_compare.md` 全落盘
3. **Sharing**: 3 档切换演练 (Restricted → Anyone with link → Public → 回 Restricted) 四态全流畅, UI 状态符合预期
4. **Template contribution**: `_template/` 补丁候选 ≥10 条 (原 7 + pivot 后新增 3) 收束合并
5. **Cross-platform data**: 10 SMOKE v2 vs Claude v2.6 / ChatGPT GPTs / Gemini Gems 四平台对比
6. **Workflow replication**: 任何 SDTM 工作者凭 `current/uploads/` + `UPLOAD_TUTORIAL.md` 能 ≤1 天在自己账号上 (Pro / Free 皆可, ≤50 source 兼容) 独立重建等效 notebook

**分用户群 use-case success**:
- **Success A (Scope A, 用户本人)**: 30 秒内回答 SMOKE v2 Q1-Q3, citation 精确到 md 段
- **Success B (Scope B, ≤50 同事 Restricted 邀请)**: 5 位同事 onboard ≤10 分钟独立查 core domain spec
- **Success C (Scope B/C, Anyone with link 公开档)**: 陌生访客打开 notebook 能读懂 SMOKE v2 Q1-Q3, 不臆造

---

## §0 修订记录

| 版本 | 日期 | Writer | 变更 | 触发 |
|------|------|--------|------|------|
| v1 | 2026-04-21 AM | planner | 初版 (3 notebook × 30-293, 951 行) | Phase 1 PASS |
| v1.1 | 2026-04-21 AM | feature-dev:code-architect (W#4) | R3 analyst 6 必改 + Project Success Criteria + Phase A §2.5 + Q1=0 红线 + extract_req_vars.py 新脚本 | R3 审核 + 用户 Q1/Q2 ack |
| **v1.x SUPERSEDED** | 2026-04-21 PM | — | **整个 v1 架构归档** (`archive/v1_3notebook_SUPERSEDED_2026-04-21/PLAN_v1_3notebook.md`), 触发: 用户 review 质疑 3 notebook 架构 + 三 WebFetch 核实推翻 v1 三假设 | 用户 2026-04-21 PM 决策 |
| **v2** | 2026-04-21 PM | 主 session (pivot 后重写) | 架构改 **1 notebook × ≤50 sources + 分享档位 3 档切换**; 删除 §3 multi-notebook 段 / uploads_main/invite/public 三目录 / 45 题次 A/B / 353 次上传; Req 零丢失红线 slot 从 30 → ≤50 宽松化; Phase A A5 (webui batch capability) 降级为 soft; P12 降级为信息段; I8/C2.9 close; 继承资产 A-F (详 pivot record) | 用户 ack pivot + 三 WebFetch 证据闭合 |

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
| 6 | **分享不改 viewer 自己 tier source cap** — Free viewer 看共享 notebook 最多看 50 sources, 决定本次上限 | research.md Q7 v2 + Q8 |
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
│   └── cross_platform_compare.md                ← Phase 4 (4 平台 10 SMOKE v2 对比)
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

v1 Phase A 6 子动作 + A5 "webui batch upload 能力调研" (hard checkpoint) 在 v2 下降级: 单 notebook × ≤50 次上传, Web UI 手工拖拽即可, 不强制 Playwright 前置. Phase A 简化为 **4 子动作**:

| Task | 子动作 | 输入 | 输出 | Checkpoint | 估算工时 |
|------|-------|------|------|-----------|---------|
| **A1** Pre-upload audit | `wc -w` 293 md + Top 5 outlier 排序 + 500K cap 校验 | `knowledge_base/**/*.md` | `dev/evidence/pre_upload_audit.md` | **hard** | 15 分钟 |
| **A2** SDTM Req 变量 extraction | 跑 `extract_req_vars.py`, 从 `VARIABLE_INDEX.md` + `domains/*/spec.md` 抽 `Core=Req` 全集 | `knowledge_base/**` | `dev/evidence/req_vars_full_set.md` (~366 记录; 去重 ~100-120 独立) | **hard** (Q1=0 红线前置) | 1-2 小时 |
| **A3** Source bucket 设计 | 跑 `cluster_req_variables.py`, 按 concept cluster 重分到 ≤50 bucket | A2 产物 + 293 md | `dev/evidence/source_mapping.md` + `current/uploads/MANIFEST.md` (草) | **hard** | 2-3 小时 |
| **A4** Req 变量全覆盖审计 | 对照 A2 全集 vs A3 bucket 断言 ∅ gap | A2 + A3 产物 | `dev/evidence/req_vars_coverage_audit.md` ("Req 变量零缺集" 断言 + diff 表) | **hard** (Q1=0 自证) | 1-2 小时 |

**Phase A 总工时**: **4-7 小时** (Q2 保险 2x = 8-14 小时, 1 天内可收完). v1 Phase A 9-16h 估算被 Phase A 简化削 ~60%.

**Phase A 依赖图**:
- A1 独立
- A2 独立 (可与 A1 并行)
- A3 依赖 A2
- A4 依赖 A2 + A3

**推荐调度**: Day 1 并行 A1 + A2; Day 1-2 串行 A3 → A4.

**Phase A 完成判据** (进 §6 Phase 3 的 gate):
- 4 子动作 evidence 全部落盘
- A1/A2/A3/A4 全 hard checkpoint 用户 ack
- `req_vars_coverage_audit.md` 显式声明 "Req 变量零缺集" (∅ gap)
- ≤50 bucket 清单可用于 Web UI 上传

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
| A/B 矩阵 | 15 题: 10 SMOKE v2 + 5 独有 (Audio 2 + Mind Map 2 + Study Guide 1) |
| PASS 阈值 | ≥13/15 (~87%) AND 每个独有产出 ≥1 精确命中 AND **Req 变量零丢失** |

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

**≤50 source 建议 bucket 方案** (Phase A A3 产出 concrete 清单, 以下为示意; 最终 slot 分配由 cluster_req_variables.py 决定):

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

**Req 变量全覆盖审计** (Phase A A4):
1. `extract_req_vars.py` 产 `req_vars_full_set.md` (~366 记录去重 ~100-120)
2. `cluster_req_variables.py` 产 `source_mapping.md` 每 slot 含 Req 变量子集
3. 主 session 跑 diff: 全集 ∪ {slot Req} 必 = 全集 ∩ {slot Req} = 全集 (即 ∅ gap)
4. 断言写进 `req_vars_coverage_audit.md` 结尾段 "Q1=0 红线自证: 零漏集"
5. 触发规则 A (压缩 >50% 必 N=10 抽检) — 主 session 独立抽样 10 个 Req 变量 (优先选 non-core domain 的), 按名查 bucket, 必 100% 命中

### 3.3 分享档位策略 (3 档按需切换)

Scope ABC 三场景在**同一 notebook 分享档位切换**, 不多 notebook:

| 日常态 / 场景 | Access Level | 允许访客 | 使用方式 |
|-------------|------|---------|---------|
| **默认态 (Scope A 个人学习)** | **Restricted** (私有) | 仅 owner | 用户本人使用, 无分享泄漏风险 |
| Scope B 小圈分享 | **Restricted + invite** | ≤50 specific emails (personal Gmail 50-cap) | 按需邀请 SDTM 小组同事, 默认 Viewer, 极少数 Editor |
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

### 3.4 Chat mode: Custom + SDTM 专家 prompt

| 字段 | 值 |
|------|----|
| Chat custom goals 模式 | **Custom** (非 Default / Learning Guide) |
| 文本文件 | `current/instructions.md` (≤10,000 char) |
| 角色定位 | "你是 SDTM 数据标准专家, 熟悉 CDISC SDTMIG 3.4, 精通 63 域 + terminology + IG 章节" |
| 行为约束 | "回答时必 inline citation 源 md, 不在知识库外编造, 遇边界问题坦诚 '未收录', 优先引权威 IG + domain spec, 术语以 terminology/core 为准" |
| 回答规范 | "高频 Q 给精确变量 + Core (Req/Exp/Perm) + codelist ID (C-code), 边界 Q 给 assumptions + IG 章节引, 混淆 Q 显式对比" |
| SDTM-specific 锚点 | STUDYID 7 字段 / AESER Core=Exp (区别 AE Req) / LBNRIND HIGH/LOW/NORMAL 全写非短码 / --ACN vs --ACT / NCI EVS 引用时字面 URL |

**替代的范本组件**: v1/v2 `05_solution.md` 的 "System Prompt 累积段设计" **不适用**, 用本段 instructions.md 单一文本替代 + 精选 source `00_navigation.md` 作首源导航 (双入口: Chat custom mode + notebook 首源).

### 3.5 Audio / Mind Map / Study Guide 侧重

- **Audio Overview**: Deep Dive 长 podcast 3 期 (SAFETY group / EFFICACY group / PK group), 每期 30-45 min, 复用 source `02-03` / `11-14` / `14-17`
- **Mind Map**: 63 domain 跨域关系全景图, 优先回答 "X domain 依赖哪些? Y domain 被哪些引用?"
- **Study Guide**: IG 关键规则章节 (CM 拆分 / AE 升 SAE / QS-C 关联) 作 Socratic 引导
- **Briefing Doc**: SDTMIG 历史版本演进 (3.2 → 3.3 → 3.4 diff 概览, 外围资料)

---

## §4 执行步骤概览 (Phase A / 3 / 4 / 5)

| Phase | 主要 Task | 产出 | 估算工时 | Checkpoint |
|-------|----------|-----|---------|-----------|
| **Phase 2 v2 审** | 第 9 种 subagent_type 独立审本 PLAN | `dev/evidence/phase2_v2_reviewer.md` | 1-2 小时 | hard (主 session 接过再进 Phase 3) |
| **Phase A Setup** | A1 audit + A2 Req extract + A3 bucket + A4 coverage audit | 4 份 evidence + `uploads/MANIFEST.md` 草 | 4-7 小时 (Q2 保险 8-14) | 全 hard |
| **Phase 3 P3.0** | Pre-flight check (re-run A1/A4 确保最新) | audit log | 0.5 小时 | soft |
| **Phase 3 P3.1** | (可选) 跑 `merge_sources.py` 合成 ≤50 个 source 文件 | `current/uploads/<source_N>.md` × ≤50 | 1-2 小时 | soft |
| **Phase 3 P3.2** | Web UI 建 notebook + 单批上传 ≤50 source | notebook 创建 + sources 上传完 | 1-2 小时 (拖拽 + indexing) | hard (indexing smoke 前置) |
| **Phase 3 P3.3** | 贴 `instructions.md` 到 Chat custom goals Custom mode | Custom mode 激活 | 10 分钟 | soft |
| **Phase 3 P3.4** | Indexing smoke test (每 source tile 点开预览 + 3 题快速问答) | `dev/evidence/indexing_smoke.md` | 1 小时 | hard (silent fail 防线) |
| **Phase 3 P3.5** | Audio Overview × 3 长 Deep Dive 生成 (SAFETY / EFFICACY / PK) | 3 个 audio + 说明文本 | 30 分钟 (生成) + 1-2 天 (听完确认) | soft (per-day 20 rate 内) |
| **Phase 3 P3.6** | Mind Map 生成 + 跨域关系验证 | Mind Map 导出 PNG + 人工 checklist | 30 分钟 | soft |
| **Phase 3 P3.7** | Study Guide × 3 生成 + 人工读 | 3 份 Study Guide | 1 小时 | soft |
| **Phase 3 P3.8** | 15 题 A/B (10 SMOKE v2 + 5 独有) | `dev/ab_reports/notebook_ab.md` | 2-3 小时 | hard (≥13/15 PASS) |
| **Phase 3 P3.9** | 3 档切换演练 (Restricted → Anyone with link → Public → 回 Restricted) | `dev/evidence/share_level_toggle_drill.md` | 30 分钟 | hard |
| **Phase 4** | 跨 4 平台对比 + 回归 + 规则 A N=10 独立抽检 + 第 10 种 subagent_type 审 | `cross_platform_compare.md` + `phase4_reviewer.md` | 2-3 小时 | hard |
| **Phase 5** | RETROSPECTIVE (含 pivot 复盘) + UPLOAD_TUTORIAL + CLAUDE.md / MANIFEST / worklog / PROGRESS 更新 + `_template/` 10 补丁 PR + commit + push | 3 份终 doc + 多点更新 | 3-5 小时 | hard (规则 D 独立审) |

**Phase 3 总估工时**: ~8-12 小时 (Q2 保险 2x = 16-24 小时, 跨 1-2 天)

---

## §5 动作清单

1. **Phase 2 v2 审**: 派第 9 种 subagent_type (前 8 种外) 独立审本 PLAN, 锚定 Q1 红线在 pivot 过程未被破坏, 审架构决策自洽性
2. **Phase A1 pre-audit**: `wc -w` 排序 293 md, 确认无 >500K words outlier
3. **Phase A2 Req extract**: 跑 `extract_req_vars.py`, 产 `req_vars_full_set.md`
4. **Phase A3 bucket**: 跑 `cluster_req_variables.py` → `source_mapping.md` + `uploads/MANIFEST.md`
5. **Phase A4 audit**: diff 全集 vs bucket, 断言 ∅ gap, 规则 A N=10 抽检
6. **Phase A 完收 commit + 用户 hard checkpoint ack**
7. **Phase 3 上传 + indexing smoke + Custom mode + 独有产出生成 + 15 题 A/B + 3 档切换演练**
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

### P3.3 Custom mode 激活 (10 分钟)

- 子步骤: Chat → Configure → Custom mode → 贴 `instructions.md` 全文 (≤10K char) → Save
- Checkpoint: soft (P3.4 smoke 会间接验证)

### P3.4 Indexing smoke test (1 小时)

- 子步骤: (a) 点每 source tile 预览确认内容存在且格式未乱 (b) 问 3 个分布式 smoke 题 (首/中/尾各一, 分别引 source_01 / source_25 / source_50) 看 citation 是否精确回指
- Checkpoint: **hard** (silent fail 防线, 不过 gate 不进 Audio/Mind Map)
- 失败处理: 删重上传对应 source + 规则 B 归档

### P3.5 Audio Overview × 3 (生成 30 分钟 + 听 1-2 天)

- 子步骤: (a) Audio Overview → Deep Dive × 3 (SAFETY / EFFICACY / PK 主题各 prompt) (b) 每期 30-45 分钟, 用户抽听 (c) 录事实错误数 + 对照 source 核
- Checkpoint: soft (∃ <10% hallucination 算 PASS)
- 失败处理: instructions.md 微调 (加 "基于 source 绝不脑补") 再跑 1 期; per-day 20 cap 内可 retry

### P3.6 Mind Map + 3.7 Study Guide (各 30-60 分钟)

- Mind Map: 生成 → 导出 PNG → 对照 63 domain 清单 checklist
- Study Guide: 3 个 domain (AE / LB / CM) 各生成一份, 人工读

### P3.8 15 题 A/B (2-3 小时)

- 10 SMOKE v2 (共享 ChatGPT/Gemini) + 5 独有 (Audio 2 + Mind Map 2 + Study Guide 1)
- 产 `dev/ab_reports/notebook_ab.md`
- Checkpoint: **hard** (≥13/15 PASS, <13 走 P10 归因重构)

### P3.9 3 档切换演练 (30 分钟)

- 子步骤: (a) Restricted (默认) → 截屏 share panel (b) 切 Anyone with link → 生成链接, 匿名窗口 (非 Google 账号) 试打开 (应被要求登录) → 换另一 Google 账号打开 (应能看到 notebook) (c) 切 Public → 在 NotebookLM 公开画廊搜 (d) 回切 Restricted → 测旧链接是否失效
- 产出: `dev/evidence/share_level_toggle_drill.md` (4 态截屏 + PASS/FAIL 表)
- Checkpoint: **hard**

---

## §7 A/B 矩阵 (15 题, v2 单 notebook)

### 10 SMOKE v2 (从 `ai_platforms/SMOKE_QUESTIONS_V2.md` 继承, 对齐 ChatGPT/Gemini)

维度分布: 场景 3 + 规则 3 + 映射 2 + 鉴别 2 (与 ChatGPT/Gemini 双平台一致以便对比)

判据参考 SMOKE v2.1 最新版 (Q3 LBNRIND PASS = HIGH/LOW/NORMAL, FAIL = H/L/N 短码).

### 5 独有生成物评估

| # | 类型 | 题 | 评估方式 |
|---|------|---|---------|
| U1 | Audio Overview fidelity (高覆盖期) | 抽 SAFETY 组 Deep Dive 听 15 分钟, 勾事实错误 | ≤3 错误 PASS |
| U2 | Audio Overview fidelity (边界期) | 抽 PK 组 Deep Dive 听 10 分钟 (PK 偏少数 domain, 测边界) | ≤2 错误 PASS |
| U3 | Mind Map coverage (RELREC) | 生成 Mind Map, 查 "RELREC 关系" 是否覆盖所有会出现 RELREC 的 domain (AE/CM/MH/DS 等 10+) | ≥9/10 核心 domain 命中 PASS |
| U4 | Mind Map coverage (SUPP--) | 查 "SUPPQUAL 扩展" 是否覆盖所有 63 domain 的 SUPP-- pattern | ≥80% 有 SUPP 例的 domain 有标注 PASS |
| U5 | Study Guide 分层 | 生成 "AE 域 Socratic" Study Guide, 检查覆盖 Standard → IG → Examples 三层 | 三层齐全 PASS |

### PASS 阈值

- 总分 ≥13/15 (~87%) AND 每个独有产出至少 1 题 PASS (U1-U2 Audio ≥1 PASS / U3-U4 Mind Map ≥1 PASS / U5 Study Guide PASS)
- **Req 变量零丢失** 独立自证 (A4 产物, 非 A/B 题里)
- <13 触发 P10 归因: (a) source 缺失重 bucket / (b) instructions.md 微调 / (c) Chat mode 切回 Learning Guide 再测

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
- 跨 4 平台 10 SMOKE v2 对比 (Claude / ChatGPT / Gemini / NotebookLM)

### Phase 5 预留

- RETROSPECTIVE 过规则 D 独立审 (第 11-13 种 subagent_type)
- `_template/` 10 补丁 PR (ai_platforms/_template/ 只在 Phase 5 写入)

---

## §11 附录 — v2 方法论自检

### 本 PLAN 诞生流程与 Rule D 合规

1. **Writer** = 主 session (pivot 后重写) — **非 subagent**, 作为过渡产物
2. **Reviewer** = 第 9 种 subagent_type (前 8 种外) 独立审 — 尚未派发, 本 PLAN 写完即派
3. **Rule D 合规性分析**: 主 session 写作 + 独立 subagent 审核, 两 lane 不同 context, 不同 subagent_type — **合规**
4. **本次 pivot 流程自检** (规则 C 预写):
   - 保留下来: Rule D 严格 + 证据驱动 + 用户 Q1/Q2 ack 不松
   - 必须补上: Writer 叙事 → planner 结论的"伪约束检测"未在 v1 审查链中触发, 任何 reviewer 都没有 question "是否一定两独立 notebook" — 这是审查盲区, 需 _template 补丁 #10
   - 关键决策: 用户 review 质疑 是 pivot 救援 (本次教训: Rule D 8 lane 都过不等于架构没问题)

### 候选第 9 种 subagent_type (Phase 2 v2 审)

前 8 种已用: general-purpose / verifier / executor / critic / planner / analyst / code-architect / pr-review-toolkit:code-reviewer

候选 (架构级审):
- **`oh-my-claudecode:architect`** (read-only, 架构策略 + 调试思维, opus) — **推荐, 与本 PLAN 的架构级修订最契合**
- `pr-review-toolkit:type-design-analyzer` — 偏类型设计, 本次无强类型系统, 次选
- `superpowers:code-reviewer` — 偏代码, 本次 PLAN 偏架构文档
- `feature-dev:code-reviewer` — 通用 PR 审, 可考虑

**主 session 选择**: `oh-my-claudecode:architect` 做第 9 种独立审 (read-only → 主 session 代写 evidence 落盘)

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
