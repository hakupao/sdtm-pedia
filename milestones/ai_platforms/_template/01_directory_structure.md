# 01 目录结构 — 四层骨架 (current / docs / dev / archive)

本文件定义每个平台部署**必须**遵守的目录结构. 这是对"用户视角"和"开发者视角"的强制剥离.

---

## 强制骨架

```
ai_platforms/<platform>/
├── README.md                         ★ 本平台导航入口 (新结构下首屏文档)
├── ROADMAP.md                        ★ 本平台路线记录 (状态 / 容量 / A/B 数据 / 决策)
│
├── 🟢 current/                       [对用户] 发布版, 去版本号
│   ├── README.md                    发布版总览 + 能力范围 + 覆盖率数据 + 限制
│   ├── UPLOAD_TUTORIAL.md           ★ 完整部署教程 (10 章节, 30-90 分钟可落地)
│   ├── system_prompt.md             平台的 Custom Instructions (去掉 v1/v2 命名)
│   ├── upload_manifest.md           上传清单: 每个文件 token 数 / 内容概要 / 源文件路径
│   └── uploads/                     最终上传的 N 个文件
│
├── 🟡 docs/                          [对开发者] 方法论 / 一等参考
│   ├── README.md                    (可选) 目录索引 + 阅读顺序建议
│   ├── PLAN.md                      本次执行的完整 PLAN (含 §0 修订记录)
│   ├── RETROSPECTIVE.md             收束复盘 (规则 C 产物)
│   ├── research.md                  前置调研 (如果做了八问八答)
│   ├── capacity_research.md         容量机制专项调研 (如果平台容量不透明)
│   ├── handoff.md                   向下游交接 (如果有 Phase N+1)
│   └── rag_decay_curve.md           RAG 质量 vs 规模曲线 (仅 Claude 类需要)
│
├── 🔵 dev/                           [对开发者] 过程产物, 复盘/考古用
│   ├── README.md                    ★ 路径映射表 (reorg 前→后) + 重跑脚本注意事项
│   ├── scripts/                     构建脚本 (保留 hardcoded 路径为 reorg 前语境)
│   ├── evidence/                    三层 evidence (见 08_evidence.md)
│   │   ├── _progress.json           L1: single source of truth
│   │   ├── trace.jsonl              L2: append-only 事件流
│   │   ├── subagent_prompts/        L3: agent prompts 全留
│   │   ├── failures/                L3: 失败归档 (规则 B)
│   │   ├── checkpoints/             L3: 逐批 hard checkpoint 记录
│   │   └── stage_<N>_audit.md       L3: 每批语义抽检结果 (规则 A)
│   ├── ab_reports/                  每批 A/B 测试报告
│   ├── checkpoints/                 Cowork / 自动执行 handoff 文档
│   └── test_results.md              A/B 矩阵完整记录
│
└── ⚫ archive/                       [冻结] 历史归档, 只读
    ├── README.md                    归档说明 + 不要修改提醒
    ├── RETROSPECTIVE.md             (可选) 上一版 (e.g. v1) 复盘, 规则源或重要教训放顶层
    └── v*/                          历史版本全产物 (docs/ scripts/ uploads/ evidence/)
```

---

## 四层职责

| 层 | 视角 | 可变性 | 去版本号? | 谁看 |
|----|------|--------|---------|------|
| `current/` | 用户 / 部署者 | 随发布版更新 | **必须去版本号** (文件名不含 v1/v2) | 要部署知识库的人 |
| `docs/` | 开发者 | 规划阶段写一次, 收束修订一次 | 可保留版本号 (e.g. PLAN_V2) | 复盘 / 接 Phase N+1 / 迁移知识 |
| `dev/` | 开发者 (冷区) | 每批追加, 不删 | 保留 stage_vX.Y 等语境 | 考古 / 重跑 / 失败排查 |
| `archive/` | 开发者 (冻结) | **绝不修改** | 保留版本号 | 审计 / 对照基线 / 规则溯源 |

---

## 核心原则

### 1. current/ 严格去版本号

用户不应该看到 `v1`/`v2` 之类的内部迭代. 即使你做到 v5, 发布版就叫 `current/system_prompt.md`, 不叫 `current/system_prompt_v5.md`.

反例: `current/system_prompt_v2.md` (别人会问 "v1 在哪?")
正例: `current/system_prompt.md` + `current/README.md` 里写一句 "本发布版基于 v5 终态"

### 2. dev/ 的 hardcoded 路径故意保留 reorg 前语境

脚本/evidence 里的 `output_v2/xxx.md`, `scripts_v2/` 等路径**不要改**成 reorg 后的路径. 这些是执行时的"时间快照", 改路径会破坏事件流时序的事实性.

在 `dev/README.md` 里写一个**路径映射表** (见 `claude_projects/dev/README.md` 范例), 复盘者可以对照着看.

### 3. archive/ 顶层放"可跨项目迁移资产", v*/ 放该版本全产物

示例 (来自 `claude_projects/archive/`):
- `archive/RETROSPECTIVE.md` (顶层) — v1 复盘, 产出了四条规则 A/B/C/D, 是跨项目迁移资产
- `archive/v1/docs/`, `archive/v1/scripts/`, `archive/v1/uploads/` — v1 全产物冻结

### 4. docs/ 头部放 "post-reorg note"

如果某个 docs 文件 (e.g. PLAN.md) 是 reorg 前写的, 路径引用还是 reorg 前语境, 在文件顶部加一段:

```markdown
> ⚠️ Post-reorg note (<date>): 本文件内路径引用 (e.g. output_v2/*, scripts_v2/*) 为 reorg 前历史执行语境.
> 当前实际路径映射见 [dev/README.md](../dev/README.md).
```

---

## 入口 README / ROADMAP 要点

### `<platform>/README.md` 首屏必答三问

```markdown
## 我想做什么?

### 部署一个可用的 <PLATFORM_NAME> 实例
→ 直接去 [**current/**](current/), 读 [UPLOAD_TUTORIAL.md](current/UPLOAD_TUTORIAL.md).

### 理解这套知识库怎么做出来的 (方法论参考)
→ 去 [**docs/**](docs/) 看 PLAN / 复盘 / 调研.

### 考古 / 复盘 / 贡献改进
→ 去 [**dev/**](dev/) (过程产物) 或 [**archive/**](archive/) (早期迭代归档).
```

### `<platform>/ROADMAP.md` 首屏必答六问

1. 状态 (待开始 / 进行中 / 已完成) + 日期
2. 着重方向 (本平台独有优势)
3. 平台特性 (RAG / 容量 / 分享)
4. 内容策略 (最终采用的是什么)
5. 执行步骤 (Phase A-H 概览)
6. 验收标准 (A/B 矩阵 PASS 条件)

收束时把 §状态 从"待开始"改成"已完成 (<date>)", 并在文件顶部加"实际产出"一行.

---

## Reorg 时机

不要等收尾才 reorg. 推荐在两种时机 reorg:

| 时机 | 做什么 |
|------|-------|
| **v1 发布后** (如果有 v2 计划) | 把 v1 产物搬到 archive/v1/, 顶层 docs/scripts/uploads 留给 v2 |
| **v2 (或终态) 收束后** | 做本范本四层 reorg, 发布版去版本号进 current/ |

Claude 本次是**收束后 reorg**, 在 commits `87573bd` (reorg-A) / `80332e8` (reorg-B) / `bf8fcf0` (fix) 完成, 可供参考.

---

## 反例 (应避免)

| 反例 | 问题 |
|------|------|
| `ai_platforms/<platform>/output/`, `ai_platforms/<platform>/output_v2/` 平铺 | 用户不知道该看哪个. 本范本前期的 Claude 走过这个坑. |
| `current/system_prompt_v2.6.md` | 暴露内部版本号, 用户困惑. |
| 修改 `archive/v1/` 里的文件 | 破坏审计溯源, 也破坏 RAG 衰减曲线的 baseline 数据点. |
| 脚本/evidence 里路径随 reorg 改写 | 破坏事件流时序事实性. |
| README 不写"我想做什么?" 三问路由 | 用户不知道该进哪个子目录. |

---

*来源: claude_projects/ 2026-04-20 reorg 实践.*
