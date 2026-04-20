# archive/ — 历史归档 (冻结, 只读)

> v1 所有产物 + 过渡性文档. **不要修改这里任何文件** — 它们是历史快照, 用于溯源和对照.

## 顶层

- [RETROSPECTIVE.md](RETROSPECTIVE.md) — v1 Step 1-12 复盘 (三段式 + 四条规则 A/B/C/D 已固化到全局 CLAUDE.md). 保留在 archive 顶层而非 v1/, 因为 v1 的四条规则是跨项目可迁移资产.

## v1/ (完整 v1 产物)

```
v1/
├── docs/
│   ├── PLAN.md                      方案 B 详细落地计划 + §7 Claude Code 执行手册
│   ├── UPLOAD_TUTORIAL.md           Step 13-14 手工操作手册 + T1-T8 测试矩阵
│   ├── claude_project_instructions.md  v1 System Prompt 蓝本
│   ├── claude_project_setup.md      v1 设置指南
│   └── V2_SESSION_STARTER.md        v2 启动 session 过渡产物 (含预授权 + 约束, 现无用保留归档)
│
├── scripts/  (v1 压缩脚本, 11 个 Python)
│   ├── build_all.py                 一键重建入口
│   ├── count_tokens.py              (v2 也复用)
│   ├── merge_specs.py, merge_model.py
│   ├── compress_assumptions.py, compress_chapters.py, compress_index.py, compress_var_index.py
│   ├── catalog_examples.py, catalog_terminology.py
│   └── _estimate_step9_floor.py
│
└── uploads/  (v1 最终上传产物 + 过程 evidence)
    ├── 00_routing.md ... 08_terminology_map.md  (9 个 v1 上传文件)
    ├── system_prompt.md
    ├── upload_manifest.md
    ├── capacity_check.md
    ├── test_results.md
    ├── _progress.json                L1 状态层
    ├── evidence/                     L2/L3 evidence (trace.jsonl + 12 份 step_NN_*.md + checkpoints/ + failures/ + subagent_prompts/)
    └── BASELINE_README.md            (原 output_v1_baseline/ 的 README, v1 归档说明)
```

## 为什么不删?

1. **对照基线**: v2 的 RAG 衰减曲线需要 v1 作为 baseline 数据点 (见 [../docs/rag_decay_curve.md](../docs/rag_decay_curve.md))
2. **规则源**: v1 复盘的四条规则 A/B/C/D 已固化全局 CLAUDE.md, RETROSPECTIVE.md 是这些规则的 "出处"
3. **审计溯源**: 未来如果有监管或审计需求, v1 完整 evidence 链 (trace.jsonl + subagent_prompts/ + failures/ + step evidence) 是可追溯凭证
4. **脚本复用种子**: v2 `scripts_v2/count_tokens.py` 就是从 v1 复制改写的

## 引用时的注意

`archive/v1/` 内文件的内部路径引用是 v1 执行时的语境 (e.g. `output/xxx.md`), 未随 reorg 更新. 对照:
- v1 时代 `ai_platforms/claude_projects/output/` → 现在 `ai_platforms/claude_projects/archive/v1/uploads/`
- v1 时代 `ai_platforms/claude_projects/scripts/` → 现在 `ai_platforms/claude_projects/archive/v1/scripts/`

---

*归档冻结: 2026-04-20 晚 reorg. 后续不再修改.*
