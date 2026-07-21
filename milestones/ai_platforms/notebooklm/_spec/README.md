# ai_platforms/_template/ — 平台部署范本

本目录是 AI 平台知识库部署的**通用规范**, 抽象自 Phase 6.5 Claude Projects v2 (33 commits / 5+1 批渐进 / 24/24 A/B PASS / 0 衰减) 沉淀的方法论.

> **服务对象**: 同一套 SDTM 知识库向多个 AI 平台 (Claude Projects / ChatGPT GPTs / Gemini Gems / 未来新平台) 的部署工作.
> **不是**: 单次的部署脚本. 本范本是**流程 + 文档 + 调度 + 审查**的骨架, 具体填充由每平台自己完成.

---

## 如何使用

1. **新起一个平台部署**: 在 `ai_platforms/<platform_name>/` 下新建目录
2. `cp -r _template/* <platform_name>/_spec/` (建议放到子目录 `_spec/`, 不污染平台业务目录)
3. 打开 `APPLY_CHECKLIST.md`, 按步骤逐项填空 + 替换
4. 填完后把"本范本"/"template" 等提示语删掉, 该平台即形成正式工作文档

**不要**直接修改本 `_template/` 目录的原文件, 这里是所有平台的 upstream single source of truth.

---

## 覆盖的 10 个维度

| # | 文件 | 维度 | 适用 Tier |
|---|------|------|----------|
| 00 | [platform_profile.md](00_platform_profile.md) | 平台适配层: RAG 机制 / 容量 / 分享 / 失败模式 | 强制 |
| 01 | [directory_structure.md](01_directory_structure.md) | 目录结构: current/docs/dev/archive 四层 | 强制 |
| 02 | [workflow.md](02_workflow.md) | 工作流: 6 阶段 (调研→策略→PLAN→批次→审查→收束) | 强制 |
| 03 | [research.md](03_research.md) | 前置调研: 八问八答格式 (容量/RAG/限制) | 强制 (首次平台) |
| 04 | [plan.md](04_plan.md) | PLAN 模板: P1-P10 规则 + 规则 E 用户优先级早问 | 强制 |
| 05 | [solution.md](05_solution.md) | 内容策略 + 落地方案: 批次 / System Prompt 累积 / Deferred stub | 强制 |
| 06 | [review.md](06_review.md) | 三 lane 审查 + A/B 回归矩阵 | 强制 |
| 07 | [agent_dispatch.md](07_agent_dispatch.md) | subagent 调度: executor/reviewer 分 lane + checkpoint 级别 | 强制 |
| 08 | [evidence.md](08_evidence.md) | 数据产物分层: L1 progress / L2 trace / L3 prompts+failures | Tier 2/3 强制 |
| 09 | [closure.md](09_closure.md) | 收束三件套: RETROSPECTIVE + handoff + UPLOAD_TUTORIAL | 强制 |

---

## 来源 & 继承关系

- **基底**: 全局 `~/.claude/CLAUDE.md` 四条规则 A/B/C/D (语义抽检 / 失败归档 / Retro 强制 / 写审分离)
- **实证**: `ai_platforms/claude_projects/` 全套产物 (v1 baseline + v2 终态 v2.6 + 两份 RETROSPECTIVE)
- **候选规则 E (本范本新增)**: 用户业务优先级必须在 PLAN §打分阶段即确认, 不能等事后重平衡 (本次 Claude v2.5→v2.6 G1 教训, 见 `claude_projects/docs/phase7_handoff.md` §2.6)
- **Tier 分级**: 见 `~/.claude/CLAUDE.md <workflow_tiers>` (Tier 1/2/3 定义)

## 本范本**不强制包含**的产物

按需产出, 不是每个平台都要:

| 产物 | 触发条件 |
|------|---------|
| `rag_decay_curve.md` | 平台 RAG 机制不透明 + 需要量化质量 vs 规模曲线 (Claude Projects 典型) |
| `capacity_research.md` | 平台官方未公开容量算法 (Claude Projects 典型, ChatGPT/Gemini 有官方限额时可简化) |
| 跨批 `subagent_prompts/` 全留 | Tier 3 或做 agent 行为变体实验时才必要 |
| Deferred stub 模式 | 平台容量硬上限 + 存在 MedDRA/LOINC 级超大表 (>500 terms) |
| 6+ 批渐进上传 | 平台需摸 RAG 衰减拐点 (Claude). ChatGPT 20 文件硬限下通常 1-2 批; Gemini 1M 窗口通常 1 批 |

---

## 范本产出的文档地图 (适用所有平台)

每个平台应用后, 目录应长这样 (路径以 `ai_platforms/<platform>/` 为根):

```
<platform>/
├── README.md                    ← 本平台入口 (新结构导航)
├── ROADMAP.md                   ← 本平台路线 (状态/容量/A/B/决策)
├── current/                     ← 发布版 (用户视角, 无版本号)
│   ├── README.md                发布版总览 + 能力范围
│   ├── UPLOAD_TUTORIAL.md       完整部署教程
│   ├── system_prompt.md         平台的 Custom Instructions
│   ├── upload_manifest.md       上传清单 + token 统计
│   └── uploads/                 最终上传的 N 个文件
├── docs/                        ← 方法论 (开发者视角)
│   ├── PLAN.md                  开发计划
│   ├── RETROSPECTIVE.md         收束复盘 (规则 C)
│   ├── research.md              前置调研 (如做)
│   └── handoff.md               下游交接 (如有)
├── dev/                         ← 开发过程冷区
│   ├── README.md                路径映射表 + 重跑注意
│   ├── scripts/                 构建脚本
│   ├── evidence/                L1 progress + L2 trace + L3 prompts/failures
│   ├── ab_reports/              A/B 测试报告 (每批一份)
│   ├── checkpoints/             Hard checkpoint handoff 文档
│   └── test_results.md          A/B 矩阵完整记录
└── archive/                     ← 历史归档 (冻结, 只读)
    ├── README.md                归档说明
    ├── RETROSPECTIVE.md         (如有上一版) 上一版复盘
    └── v*/                      历史版本全产物
```

其中 `current/` 是**对用户**、`docs/`+`dev/`+`archive/` 是**对开发者**, 两视角严格剥离.

---

## 维护

- 未来每完成一个新平台部署, 把该平台独有的经验/缺口补充进本范本 (PR 到 `_template/` 目录)
- 候选规则 E 在累积到至少 2 个项目的独立证据后, 再考虑提到全局 `~/.claude/CLAUDE.md`

*建立日期: 2026-04-20 (来源: claude_projects/ v2.6 reorg 后抽象)*
