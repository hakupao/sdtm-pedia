# .work/ MANIFEST — 文件清单与变更链

> **AI 工作入口文件** — 每次新 session 开始时先读此文件，了解文件布局和更新规则。
> 最后更新: 2026-04-15

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
03_verification/plan.md ──── Phase 5 验证主计划 ──── [几乎完成]
│
├─→ Step 0~3.6 ······························ [已完成]
│
├─→ repair_plan.md ── Issue 2 修复 ·········· [已完成/归档]
│   │  派生原因: Step 3-4/3-5 执行中发现内容空洞
│   │
│   └─→ followup_plan.md ── 残余风险排查 ··· [待执行]
│        派生原因: 修复完成后反思，发现中风险区域+盲区
│        内容: M1~M5 五项抽查任务
│
└─→ Step 4 汇总报告 ························ [待执行]
     内容: 全量验证的最终报告

04_optimization/retrieval_optimization.md ── Phase 6 检索优化 ── [待执行/独立]
     内容: P0~P3 四项优化任务（ROUTING.md、反向索引等）
     前置: Phase 5 完成后再开始
```

**下一步执行顺序建议**:
1. `followup_plan.md` M1~M5 抽查（验证收尾）
2. `plan.md` Step 4 汇总报告（验证关门）
3. `retrieval_optimization.md` P0~P3（进入新阶段）

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
│   │   └── step3_5_ch08_ch10.md
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
├── 04_optimization/         ← Phase 6: 检索精度优化（待执行）
│   └── retrieval_optimization.md  P0~P3 优化任务清单
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
| `04_optimization/` | Phase 6 | 检索精度优化 (TODO) |

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
| **AI 工作质量规则** | **`meta/retrospective.md`** ⚑ 四条预防规则必须遵守 |
| 查残余风险排查计划 | `03_verification/followup_plan.md` |
