# Claude Projects — SDTM 知识库部署 (入口)

> 状态: **v1 + v2 终态完成** (2026-04-20 reorg 完成)
> 当前 = v2.6 (19 上传文件 / 1,286,161 tokens / capacity 77% / 24/24 A/B PASS / 0 衰减全程)

## 四层结构

```
claude_projects/
├── README.md        ← 本文件 (入口)
├── ROADMAP.md        原始路线 (已完成, 加执行回顾)
│
├── current/          🟢 当前可部署产物 (v2.6 终态)
│   ├── uploads/      19 个 .md 文件 (00-13c)
│   ├── system_prompt.md
│   ├── upload_manifest.md
│   └── README.md     (部署指南)
│
├── docs/             🟡 方法论 & 一等参考 (暖区, 看就行)
│   ├── PLAN_V2.md
│   ├── RETROSPECTIVE_V2.md
│   ├── rag_decay_curve.md
│   ├── phase7_handoff.md       ← Phase 7 启动必读
│   ├── capacity_research.md
│   └── README.md
│
├── dev/              🔵 开发/过程产物 (冷区, 复盘或考古才进)
│   ├── scripts/      6 个构建脚本 (hardcoded 路径是 reorg 前语境, 见 dev/README.md)
│   ├── evidence/     trace.jsonl + _progress.json + subagent_prompts/ 等 49 份
│   ├── ab_reports/   5 批 A/B 测试报告
│   ├── checkpoints/  Cowork 自动执行 handoff
│   ├── test_results.md
│   └── README.md     (含 reorg 前→后路径映射表)
│
└── archive/          ⚫ 历史归档 (冻结, 只读)
    ├── RETROSPECTIVE.md  v1 复盘 (四条规则已固化全局 CLAUDE.md)
    └── v1/
        ├── docs/     PLAN.md + UPLOAD_TUTORIAL.md + 配套文档
        ├── scripts/  11 个 v1 脚本
        ├── uploads/  v1 的 11 上传文件 + evidence/
        └── README.md
```

## 按角色快速入口

**部署用户** (想把知识库上 Claude Project):
→ 读 [current/README.md](current/README.md), 把 `current/uploads/` 的 19 个文件全部上传, 贴 `current/system_prompt.md`.

**Phase 7 设计者** (接续做自建 RAG):
→ 必读顺序:
1. [docs/phase7_handoff.md](docs/phase7_handoff.md) (6 条 actionable + 5 未解问题 + 5 步待办)
2. [docs/rag_decay_curve.md](docs/rag_decay_curve.md) (7 数据点 + 结论 + 6 关键发现)
3. [docs/RETROSPECTIVE_V2.md](docs/RETROSPECTIVE_V2.md) §3 关键决策复盘

**复盘/考古** (想知道怎么跑到这里):
→ [docs/PLAN_V2.md](docs/PLAN_V2.md) + [docs/RETROSPECTIVE_V2.md](docs/RETROSPECTIVE_V2.md) + [dev/evidence/_phase_summary.md](dev/evidence/_phase_summary.md)

**重跑脚本** (非标准场景, 路径需手动 remap):
→ [dev/README.md](dev/README.md) (含 reorg 前→后路径映射表)

## 关键事实

| 指标 | v1 | v2.6 (当前) |
|------|-----|-------------|
| 上传文件数 | 9 | 19 |
| Tokens | 192,036 | 1,286,161 (+571%) |
| Capacity (UI 实测) | 12% | **77%** |
| A/B PASS | 8/8 | **24/24** |
| 回归衰减 | N/A | **0** (6 批 + 1 重平衡批全程) |
| 覆盖率 (用户优先级) | — | core 99.3% / supp 100% / quest 55.8% |

## Reorg 说明

本目录 2026-04-20 晚由原混乱平铺结构 (output_v2/ + output_v1_baseline/ + output/ + scripts/ + scripts_v2/ 平铺 + 大量根目录文档) 重组为当前 current/docs/dev/archive 四层.

**对历史文档的处理**: `docs/PLAN_V2.md` 和 `docs/RETROSPECTIVE_V2.md` 内部路径引用保留 reorg 前语境 (例如 "output_v2/xxx.md"), 以维持历史执行记录的准确性, 每份文件头部加 post-reorg note. 完整路径映射见 [dev/README.md](dev/README.md).

**对脚本的处理**: `dev/scripts/*.py` 中硬编码路径 (`output_v2`/`evidence_v2`/`scripts_v2`) 保持 reorg 前状态. 重跑脚本须手动 remap 路径 — 实际上 v2.6 终态后无重跑需求.

---

*Reorg 执行: 主控 Claude Opus 4.7 (1M context), 2026-04-20 晚. 详见 git commit `Phase 6.5 v2 reorg-A/B`.*
