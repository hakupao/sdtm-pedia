# .work/ MANIFEST — 文件清单与变更链

> **AI 工作入口文件** — 每次新 session 开始时先读此文件，了解文件布局和更新规则。
> 最后更新: 2026-04-20 晚 (Phase 6.5 Claude v2 终态完成 + reorg: claude_projects/ 重组为 current/docs/dev/archive 四层, 消除 output_v2/output_v1_baseline/output/ 混乱; 脚本与过程产物路径引用保留 reorg 前语境, 见各目录 README)

---

## 变更链 (Change Chains)

当你修改了某个文件，**必须沿链检查并更新所有关联文件**。
每个链有一个触发条件和一条更新路径。

---

### Chain A: 验证进度链

**触发**: 验证步骤完成、发现问题、步骤状态变更

```
03_verification/plan.md              ← 更新步骤状态
  ↓
03_verification/results/step*.md     ← 添加详细验证结果
  ↓
03_verification/issues_found.md      ← 汇总问题（如有）
  ↓
meta/findings.md                     ← 全局质量问题记录
  ↓
meta/worklog.md                      ← 记录工作内容
  ↓
progress.json                        ← 更新程序化进度
  ↓
../docs/PROGRESS.md                       ← 更新面向读者的进度看板
```

---

### Chain B: 工作日志链

**触发**: 任何阶段性工作完成

```
meta/worklog.md                      ← 记录做了什么
  ↓
progress.json                        ← 更新状态字段
  ↓
../docs/PROGRESS.md                       ← 更新看板
```

---

### Chain C: 新阶段启动链

**触发**: 开始新的工作阶段（如 Phase 6 优化）

```
0N_xxx/ (新目录)                     ← 创建工作文件
  ↓
meta/worklog.md                      ← 记录启动
  ↓
../docs/PROGRESS.md                       ← 更新看板
  ↓
MANIFEST.md (本文件)                  ← 注册新目录和文件
```

---

### Chain D: 溯源链

**触发**: knowledge_base/ 内容变更

```
knowledge_base/ 文件变更
  ↓
meta/mapping.md                      ← 更新源文件→产出映射（如有新源）
  ↓
../docs/TRACEABILITY.md                   ← 更新溯源矩阵
  ↓
meta/worklog.md                      ← 记录变更
```

---

### Chain E: 方案变更链

**触发**: 项目方案/架构调整

```
00_planning/*.md                     ← 修改方案文档
  ↓
meta/worklog.md                      ← 记录决策变更
  ↓
../docs/PROGRESS.md                       ← 如影响阶段则更新
  ↓
../README.md / ../README_CN.md       ← 如影响项目描述则更新
```

---

## 计划导航 (Plan Map)

所有计划/TODO 文件的从属关系、状态和执行顺序。新 session 开始时先看这里，决定该做什么。

```
03_verification/plan.md ──── Phase 5 验证主计划 ──── [已完成]
│
├─→ Step 0~3.6 ······························ [已完成]
│
├─→ repair_plan.md ── Issue 2 修复 ·········· [已完成/归档]
│   │  派生原因: Step 3-4/3-5 执行中发现内容空洞
│   │
│   └─→ followup_plan.md ── 残余风险排查 ··· [已完成]
│        内容: M1~M5 五项抽查任务
│
└─→ Step 4 汇总报告 ························ [已完成]
     产出: results/step4_summary_report.md

04_optimization/retrieval_optimization.md ── Phase 6 检索优化 ── [P0-P2 已完成, P3→Phase 7]
     内容: P0~P3 四项优化任务（ROUTING.md、反向索引等）
     前置: Phase 5 完成后再开始

ai_platforms/ ── Phase 6.5 AI 平台部署 ── [Claude v1 完成 (9/9 PASS); Claude v2 终态 v2.6 完成 (24/24 A/B PASS, 0 衰减, capacity 77%); 2026-04-20 Reorg 重组到 current/docs/dev/archive]
     总览: ai_platforms/README.md
     三平台路线: chatgpt_gpt/ROADMAP.md, claude_projects/ROADMAP.md, gemini_gems/ROADMAP.md
     **Claude 新结构入口**: claude_projects/README.md (指向 current/docs/dev/archive 四层)
     Claude 当前可部署 (v2.6): claude_projects/current/ (uploads/ 19 文件 + system_prompt.md + upload_manifest.md)
     Claude 方法论文档: claude_projects/docs/ (PLAN_V2 + RETROSPECTIVE_V2 + rag_decay_curve + phase7_handoff + capacity_research)
       - PLAN_V2.md (1852 行, 8 阶段 ~30 任务, 内部路径引用为 reorg 前语境, 见文件头 post-reorg note)
       - RETROSPECTIVE_V2.md (7 章复盘, 过 Rule D 独立复核 CONDITIONAL_PASS→PASS)
       - rag_decay_curve.md (7 数据点 v1→v2.6 + 4 段观察 + 结论 + 6 条 Phase 7 actionable)
       - phase7_handoff.md (6 条 actionable + 5 未解问题 + 5 步待办)
       - capacity_research.md (v1 Step 14 后 200K 假设修正)
     Claude 开发过程 (冷区): claude_projects/dev/ (reorg 前为 scripts_v2+output_v2/evidence_v2; 内部路径引用保留历史语境, 见 dev/README.md 映射表)
       - scripts/ 6 Python 脚本 (rebuild_chapters + extract_examples_data + extract_terminology_terms + score_domains + score_codelists + build_v2_stage)
       - evidence/ (trace.jsonl + _progress.json + _phase_summary.md + H1_reviewer.md + subagent_prompts/ 14 + checkpoints/ + failures/ + rag_decay_observations/)
       - ab_reports/ STAGE_V2.{1,2,3,4,6}_AB_REPORT.md (v2.5 被 v2.6 合并 skipped)
       - checkpoints/ CHECKPOINT_V2.{1..6}_HANDOFF.md
       - test_results.md (T1-T22 + 2 优先级验证完整矩阵)
     Claude 历史归档 (冻结): claude_projects/archive/
       - RETROSPECTIVE.md (v1 三段式 + 四条规则已固化全局 CLAUDE.md)
       - v1/docs/ (PLAN.md + UPLOAD_TUTORIAL.md + claude_project_instructions.md + claude_project_setup.md + V2_SESSION_STARTER.md 过渡产物)
       - v1/scripts/ (11 Python 脚本, build_all.py 一键重建)
       - v1/uploads/ (11 上传文件 + evidence/ + _progress.json + capacity_check.md + test_results.md + BASELINE_README.md)
     Claude 实际产出构成 (v2.6 终态 19 文件):
       - 00-08: v2.1 chapters byte-exact expand (重建 v1 结构)
       - 09: examples 高频 28 域 (v2.2, 112,697 tokens)
       - 10: examples 其余 35 域 (v2.3, 48,897 tokens) — 63 域 examples 全覆盖
       - 11a/11b/11c: terminology top 200 按 subdir 拆 (v2.4, 351,752 tokens)
       - 12a/12b/12c: terminology mid rank 201-500 按 subdir 拆 (v2.5, 377,939 tokens)
       - 13a/13c: terminology tail 用户优先级重平衡 (v2.6, 188,981 tokens; 6 giants Deferred stub, 13b by design 不存在)
     Claude v2 设计文档: docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md
     Claude v2 plan pointer: docs/superpowers/plans/2026-04-18-phase6.5-claude-v2-expansion.md (skill 约定)
     前置: Phase 6 P0-P2 完成（已满足）

05_rag_kg/ ── Phase 7 RAG + 知识图谱 + 数据集校验 ── [设计完成/待实施]
     设计文档: docs/DESIGN_RAG_KG.md
     session 记录: 05_rag_kg/session_2026-04-16_design.md
     前置: Phase 6 P0-P2 完成（已满足）
```

**下一步执行顺序建议**:
1. ~~`followup_plan.md` M1~M5 抽查（验证收尾）~~ ✅ 已完成
2. ~~`plan.md` Step 4 汇总报告（验证关门）~~ ✅ 已完成
3. ~~`retrieval_optimization.md` P0~P2（检索优化）~~ ✅ 已完成
4. `ai_platforms/` Phase 6.5 三平台部署 ← **当前位置**
5. `docs/DESIGN_RAG_KG.md` Phase 7 实施

---

## 目录结构

```
.work/
├── MANIFEST.md              ← 本文件（入口 + 链路图）
├── progress.json            ← 程序化进度追踪（脚本读写）
│
├── 00_planning/             ← Phase 0: 分析与方案设计
│   ├── source_relationship.md    源文件关系梳理
│   └── restructure_plan.md       知识库重构方案（核心方案文档）
│
├── 01_generation/           ← Phase 1: xlsx 自动生成
│   └── scripts/
│       ├── generate_spec.py       spec.md 生成脚本
│       ├── generate_terminology.py 术语文件生成脚本
│       └── validate_spec.py       spec.md 校验脚本
│
├── 02_indexing/             ← Phase 2: PDF 页码索引
│   ├── page_index.json           权威页码索引（63 域，全部 verified）
│   └── page_index_old.json       旧版备份
│
├── 03_verification/         ← Phase 5: 全量验证
│   ├── plan.md                   验证计划与进度总表
│   ├── issues_found.md           问题汇总
│   ├── followup_plan.md          后续排查计划（残余风险与盲区）
│   ├── repair_plan.md            Issue 2 修复计划（写/审分离流程）
│   ├── results/                  验证结果（按步骤编号）
│   │   ├── step1_assumptions.md
│   │   ├── step2_examples_summary.md
│   │   ├── step2_examples_detail.md
│   │   ├── step3_1_model_small.md
│   │   ├── step3_2_model_rest.md
│   │   ├── step3_3_chapters_small.md
│   │   ├── step3_4_ch04.md
│   │   ├── step3_5_ch08_ch10.md
│   │   └── step4_summary_report.md
│   ├── scans/                    图像溯源扫描
│   │   ├── ig_chapters.md
│   │   ├── ig_domains_d1~d4.md
│   │   ├── v20.md
│   │   └── image_inventory.md
│   └── rescan/                   重新扫描与问题调查
│       ├── a1~a7.md
│       ├── diff.md
│       └── issue1_investigation.md
│
├── 04_optimization/         ← Phase 6: 检索精度优化（P0-P2 已完成）
│   ├── retrieval_optimization.md  P0~P3 优化任务清单与执行结果
│   ├── p1_cross_reference_plan.md P1 交叉引用执行计划
│   ├── p2_variable_index_plan.md  P2 变量反向索引执行计划
│   └── scripts/
│       ├── generate_variable_index.py   P2 脚本（生成 VARIABLE_INDEX.md）
│       └── generate_cross_references.py P1 脚本（生成 Cross References 段）
│
├── 05_rag_kg/               ← Phase 7: RAG + 知识图谱 + 数据集校验
│   └── session_2026-04-16_design.md  设计讨论 session 记录（需求/方案/场景模拟/决策）
│
└── meta/                    ← 贯穿全程的元信息
    ├── worklog.md                 工作日志（中断恢复入口）
    ├── retrospective.md           阶段性反思（Issue 根因 + 四条预防规则）⚑ 必读
    ├── mapping.md                 源文件→产出文件映射
    ├── findings.md                质量问题全局记录
    └── user_actions.md            用户操作指南
```

## Phase 编号映射

| .work/ 目录 | 项目 Phase | 说明 |
|-------------|-----------|------|
| `00_planning/` | Phase 0 | 分析与方案设计 |
| `01_generation/` | Phase 1 | xlsx 自动生成 spec.md + terminology |
| `02_indexing/` | Phase 2 | PDF 页码索引 |
| *(无 .work/ 目录)* | Phase 3-4 | PDF 提取，产出直接写入 knowledge_base/ |
| `03_verification/` | Phase 5 | 全量验证 |
| `04_optimization/` | Phase 6 | 检索精度优化 (P0-P2 已完成) |
| *(根目录 `ai_platforms/`)* | Phase 6.5 | AI 平台部署 (进行中) |
| `05_rag_kg/` | Phase 7 | RAG + 知识图谱 + 数据集校验 (设计完成) |

## 快速参考

| 要做什么 | 先读 |
|---------|------|
| 恢复中断的工作 | `meta/worklog.md` → `progress.json` |
| 了解完整方案 | `00_planning/restructure_plan.md` |
| 查看验证状态 | `03_verification/plan.md` |
| 查 domain 页码 | `02_indexing/page_index.json` |
| 查源文件→产出映射 | `meta/mapping.md` |
| 查质量问题 | `meta/findings.md` |
| 查后续 TODO | `04_optimization/retrieval_optimization.md` |
| **Phase 6.5 AI 平台部署** | **`../ai_platforms/README.md`** — 三平台部署总览与路线图 |
| **Phase 6.5 Claude 入口 (reorg 后)** | **`../ai_platforms/claude_projects/README.md`** — 新结构 current/docs/dev/archive 导航 (2026-04-20) |
| **Phase 6.5 Claude 当前可部署** | **`../ai_platforms/claude_projects/current/`** — v2.6 终态, 19 文件 + system_prompt + upload_manifest |
| **Phase 6.5 Claude v1 复盘** | **`../ai_platforms/claude_projects/archive/RETROSPECTIVE.md`** — v1 Step 1-12 三段式 + 四条规则 A/B/C/D 固化 (2026-04-18) |
| **Phase 6.5 Claude v1 压缩计划** (archive) | **`../ai_platforms/claude_projects/archive/v1/docs/PLAN.md`** — v1 方案 B 详细落地计划 + §7 执行手册 |
| **Phase 6.5 Claude v1 上传教程** (archive) | **`../ai_platforms/claude_projects/archive/v1/docs/UPLOAD_TUTORIAL.md`** — v1 Step 13-14 手动操作 + T1-T8 测试 |
| **Phase 6.5 Claude 容量调研** | **`../ai_platforms/claude_projects/docs/capacity_research.md`** — 200K 假设错, paid 套餐 RAG 自动扩 10x, 实际容量 ~3-4M |
| **Phase 6.5 Claude v2 设计** | **`../docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md`** — 中庸 5 批 / ~50% 容量 / 16-18 文件 / RAG 衰减曲线 (2026-04-18) |
| **Phase 6.5 Claude v2 计划** | **`../ai_platforms/claude_projects/docs/PLAN_V2.md`** — 1852 行 / 8 阶段 / ~30 Tasks (内部路径 reorg 前语境) |
| **Phase 6.5 Claude v2 执行进度** | **`../ai_platforms/claude_projects/dev/evidence/_progress.json`** — status=completed, 5 checkpoints_acked (v2.1-v2.4 + v2.6), phase_final_metrics 快照 |
| **Phase 6.5 Claude v2 RAG 衰减曲线** | **`../ai_platforms/claude_projects/docs/rag_decay_curve.md`** — 7 数据点 + 4 段跨批观察 + 结论 + 6 条 Phase 7 actionable |
| **Phase 6.5 Claude v2 Phase 7 交接** | **`../ai_platforms/claude_projects/docs/phase7_handoff.md`** — 6 条 actionable + 5 问题 Q1-Q5 + 实施前 5 步待办 |
| **Phase 6.5 Claude v2 复盘** | **`../ai_platforms/claude_projects/docs/RETROSPECTIVE_V2.md`** — Rule C 强制产物, 7 章, 过 Rule D 独立复核 |
| **Phase 6.5 Claude v2 A/B 报告** | **`../ai_platforms/claude_projects/dev/ab_reports/STAGE_V2.{1,2,3,4,6}_AB_REPORT.md`** — 5 批 A/B 报告 (v2.5 合并 skipped), v2.6 终态 24/24 PASS |
| **Phase 6.5 Claude v2 测试矩阵** | **`../ai_platforms/claude_projects/dev/test_results.md`** — T1-T22 + T-core-reb/T-supp-reb + v2.1-v2.6 stage 汇总 |
| **Phase 6.5 Claude v2 H1 独立复核** | **`../ai_platforms/claude_projects/dev/evidence/H1_reviewer.md`** — RETROSPECTIVE_V2 过 code-reviewer CONDITIONAL_PASS → PASS evidence |
| **Phase 6.5 Claude v2 开发过程 (冷区)** | **`../ai_platforms/claude_projects/dev/`** — scripts/ + evidence/ + ab_reports/ + checkpoints/ + test_results.md (reorg 前路径映射见 dev/README.md) |
| **Phase 7 设计文档** | **`../docs/DESIGN_RAG_KG.md`** — RAG + 知识图谱 + 数据集校验 |
| Phase 7 session 记录 | `05_rag_kg/session_2026-04-16_design.md` |
| **AI 工作质量规则** | **`meta/retrospective.md`** ⚑ 四条预防规则必须遵守 |
| 查残余风险排查计划 | `03_verification/followup_plan.md` |
