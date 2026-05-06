# .work/ MANIFEST — 文件清单与变更链

> **AI 工作入口** — 新 session 先读 `.work/AGENT_GUIDE.md` (一页纸), 再回本文件查结构 + 链路.
> 最后更新: 2026-05-06

本文件只列**文件结构 + 变更链 + Key Paths 指针**. 当前进度看 `docs/PROGRESS.md`. 历史细节看 `.work/meta/worklog/INDEX.md` (按 phase 拆分).

---

## 变更链 (Change Chains)

修改某文件后, **必须沿链检查并更新所有关联文件**. 每个链有触发条件 + 一条更新路径.

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
meta/worklog/phase03_verification.md ← 记录工作内容
  ↓
progress.json                        ← 更新程序化进度
  ↓
../docs/PROGRESS.md                  ← 更新面向读者的进度看板
```

### Chain B: 工作日志链

**触发**: 任何阶段性工作完成

```
meta/worklog/phase{NN}_xxx.md        ← 按 phase 记录做了什么
  ↓
{相应 phase 的} _progress.json        ← 更新状态字段
  ↓
../docs/PROGRESS.md                  ← 更新看板
```

### Chain C: 新阶段启动链

**触发**: 开始新的工作阶段

```
0N_xxx/ (新目录)                     ← 创建工作文件
  ↓
meta/worklog/phase{NN}_xxx.md        ← 记录启动 (新建文件 + 加进 INDEX.md)
  ↓
../docs/PROGRESS.md                  ← 更新看板
  ↓
MANIFEST.md (本文件)                  ← 注册新目录到下方目录结构表
```

### Chain D: 溯源链

**触发**: knowledge_base/ 内容变更

```
knowledge_base/ 文件变更
  ↓
meta/mapping.md                      ← 更新源文件→产出映射 (如有新源)
  ↓
../docs/TRACEABILITY.md              ← 更新溯源矩阵
  ↓
meta/worklog/phase0N_xxx.md          ← 记录变更
```

### Chain E: 方案变更链

**触发**: 项目方案/架构调整

```
00_planning/*.md                     ← 修改方案文档
  ↓
meta/worklog/phase00_planning.md     ← 记录决策变更
  ↓
../docs/PROGRESS.md                  ← 如影响阶段则更新
  ↓
../README.md / ../README_CN.md       ← 如影响项目描述则更新
```

### Chain J: 日本同事交付链 (docs/jp/, iTMS 様 納品)

**触发**: `docs/jp/` 配下任何文件修改

```
docs/jp/PLAN.md / EXECUTION_PLAN.md       ← 規範改訂
  ↓ docs/jp/_progress.json (Tier 2 schema)
  ↓ docs/jp/CHANGELOG.md
  ↓ docs/jp/glossary/{term_blacklist,term_mapping}.yml  (用語規律変更時)
  ↓ docs/jp/templates/style_guide.xlsx                  (配色/フォント変更時)
  ↓ .work/MANIFEST.md                                   (入口登録 + Quick Ref)
  ↓ .work/meta/worklog/phase_jp_delivery.md             (作業記録)
  ↓ ../CLAUDE.md Key Paths                              (新規 Key Path のみ)
```

下流 (J'): `EXECUTION_PLAN.md` 改訂時は `prompts/`, `failures/`, `scripts/` 整合性を確認.

### Chain REFACTOR-v1: 项目重构链 (临时, 段 3 close 后删)

**触发**: `.work/refactor_v1/` 配下修改. 完整链定义见该目录 `PLAN.md` header. 简化指针: `PLAN.md → _progress.json → path_migration.md → MANIFEST.md → meta/worklog/phase_meta_refactor.md → ../CLAUDE.md`.

---

## 计划导航 (Plan Map)

各 phase 主计划文件入口 + 依赖关系. **状态看 `docs/PROGRESS.md`**, 本图只显示结构.

```
03_verification/plan.md ── Phase 5 验证主计划
│
├─→ Step 0~3.6 详细验证结果在 results/
├─→ repair_plan.md ── Issue 2 修复 (派生)
│   └─→ followup_plan.md ── M1~M5 残余风险
└─→ Step 4 汇总报告 (results/step4_summary_report.md)

04_optimization/retrieval_optimization.md ── Phase 6 检索优化
     P0~P3 任务清单, 前置 = Phase 5 完成

05_rag_kg/ ── Phase 7 RAG + 知识图谱 + 数据集校验
     设计在 docs/DESIGN_RAG_KG.md, session 记录在 05_rag_kg/

06_deep_verification/PLAN.md ── 字面级 PDF→KB 深审 (旁枝)
     当前 P2 B-03c 进行中. multi_session/ 含 batch/round kickoff.

07_website/phase{6,7,8}/PLAN.md ── 公开站点 (closed)
     prod sdtm-pedia.pages.dev. handoffs 在 meta/website_phase*_handoff_*.md.

ai_platforms/ ── Phase 6.5 AI 平台部署 (旁枝, 双平台锁步)
     总览 ai_platforms/README.md; 锁步 SYNC_BOARD.md; 范本 _template/.

docs/jp/ ── iTMS 納品旁枝 (Chain J)
     入口 docs/jp/PLAN.md + EXECUTION_PLAN.md (Excel 主体)
```

---

## 目录结构

```
.work/
├── AGENT_GUIDE.md           ← 一页纸 agent 进入指引 (优先读)
├── MANIFEST.md              ← 本文件 (结构 + 链路)
├── 00_planning/             ← Phase 0: 分析与方案设计
├── 01_generation/           ← Phase 1: xlsx 自动生成 (scripts/)
├── 02_indexing/             ← Phase 2: PDF 页码索引 (page_index.json)
├── 03_verification/         ← Phase 5: 全量验证 (plan + issues + results/ + scans/ + rescan/)
├── 04_optimization/         ← Phase 6: 检索优化 (P0-P2 完成)
├── 05_rag_kg/               ← Phase 7: RAG + KG (设计完成)
├── 06_deep_verification/    ← 字面级 PDF→KB 深审 (旁枝, 占 .work/ 体积大头)
├── 07_website/              ← Phase 6-8 公开站点 (closed)
├── refactor_v1/             ← 项目重构 v1 (临时, 段 3 close 后归档)
└── meta/
    ├── worklog/             ← 工作日志 (按 phase 拆分, INDEX.md 入口)
    ├── retrospective.md     ← 阶段性反思 + 四条预防规则 ⚑ 必读
    ├── mapping.md           ← 源文件→产出映射
    ├── findings.md          ← 质量问题全局记录
    ├── notes/               ← 工作笔记类
    └── *_handoff_*.md       ← 段间 / phase 间 handoff 记录
```

## Phase 编号映射

| .work/ 目录 | 项目 Phase | 说明 |
|-------------|-----------|------|
| `00_planning/` | Phase 0 | 分析与方案设计 |
| `01_generation/` | Phase 1 | xlsx 自动生成 spec.md + terminology |
| `02_indexing/` | Phase 2 | PDF 页码索引 |
| *(无 .work/ 目录)* | Phase 3-4 | PDF 提取, 直接写 knowledge_base/ |
| `03_verification/` | Phase 5 | 全量验证 |
| `04_optimization/` | Phase 6 | 检索精度优化 (P0-P2 完成) |
| *(根 `ai_platforms/`)* | Phase 6.5 | AI 平台部署 (双平台锁步进行中) |
| `05_rag_kg/` | Phase 7 | RAG + KG + 数据集校验 (设计完成) |
| `06_deep_verification/` | 06 (旁枝) | 字面级 PDF→KB 深审 (P2 进行中) |
| `07_website/` | 07 Website | sdtm-pedia 公司发布版静态网站 (closed) |

---

## Quick Reference (核心入口指针)

详细路径速查见 `.work/AGENT_GUIDE.md` + `CLAUDE.md` Key Paths. 本表只列入口级.

| 找什么 | 去哪 |
|--------|------|
| 当前进度看板 | `docs/PROGRESS.md` (唯一状态源) |
| 历史工作日志 | `meta/worklog/INDEX.md` → 各 phase 文件 |
| 完整方案 | `00_planning/restructure_plan.md` |
| 验证状态 | `03_verification/plan.md` |
| Domain 页码 | `02_indexing/page_index.json` |
| 源→产出映射 | `meta/mapping.md` |
| 质量问题 | `meta/findings.md` |
| AI 工作四条规则 | `meta/retrospective.md` ⚑ 必读 |
| 06 Deep Verification | `06_deep_verification/PLAN.md` + `multi_session/` |
| Phase 6.5 总览 | `../ai_platforms/README.md` + `SYNC_BOARD.md` |
| Phase 6.5 范本 | `../ai_platforms/_template/README.md` |
| Phase 7 设计 | `../docs/DESIGN_RAG_KG.md` |
| 07 Website 入口 | `07_website/phase{6,7,8}/PLAN.md` |
| docs/jp/ 入口 | `../docs/jp/PLAN.md` + `EXECUTION_PLAN.md` |
| 重构 v1 | `refactor_v1/PLAN.md` |
