# dev/ — 开发过程产物 (冷区)

> 本目录是 Phase 6.5 v2 执行过程的完整快照: 脚本 + evidence + AB 报告 + checkpoints + 测试矩阵.
> 日常部署**不必看**, 复盘/考古/重跑脚本时才进.
> 内容在 reorg 前分散在 `scripts_v2/`, `output_v2/`, `output_v2/evidence_v2/` 三处.

## 内容清单

| 子路径 | 来源 (reorg 前) | 内容 | 何时看 |
|--------|-----------------|------|--------|
| `scripts/` | `scripts_v2/` | 6 个构建脚本 | 想重跑 v2 批次或移植脚本到新项目 |
| `evidence/` | `output_v2/evidence_v2/` | trace.jsonl + _progress.json + subagent_prompts/ 等 49 份 | 想重现某个决策 / Rule B (失败归档) 查询 |
| `ab_reports/` | `output_v2/STAGE_V2.*_AB_REPORT.md` | 5 批 A/B 测试报告 (v2.5 被 v2.6 合并 skipped) | 想看某批具体 PASS/FAIL 细节 |
| `checkpoints/` | `output_v2/CHECKPOINT_V2.*_HANDOFF.md` | 6 份 Cowork 自动执行 handoff | 想看每个 hard checkpoint 的 Cowork 执行手册 |
| `test_results.md` | `output_v2/test_results_v2.md` | T1-T22 + T-core-reb/T-supp-reb 完整矩阵 + v2.1-v2.6 stage 汇总 | 想做 Phase 7 回归 baseline |

## Reorg 前→后路径映射表

脚本内 hardcoded 路径和 evidence 内历史引用保持 **reorg 前状态不变**. 如果要重跑或追溯:

| reorg 前 (脚本/evidence 里写的) | reorg 后 (实际位置) |
|--------------------------------|---------------------|
| `ai_platforms/claude_projects/output_v2/00_routing.md` | `ai_platforms/claude_projects/current/uploads/00_routing.md` |
| `ai_platforms/claude_projects/output_v2/*.md` (上传文件) | `ai_platforms/claude_projects/current/uploads/*.md` |
| `ai_platforms/claude_projects/output_v2/system_prompt_v2.md` | `ai_platforms/claude_projects/current/system_prompt.md` |
| `ai_platforms/claude_projects/output_v2/upload_manifest_v2.md` | `ai_platforms/claude_projects/current/upload_manifest.md` |
| `ai_platforms/claude_projects/output_v2/evidence_v2/*` | `ai_platforms/claude_projects/dev/evidence/*` |
| `ai_platforms/claude_projects/output_v2/STAGE_V2.*_AB_REPORT.md` | `ai_platforms/claude_projects/dev/ab_reports/STAGE_V2.*_AB_REPORT.md` |
| `ai_platforms/claude_projects/output_v2/CHECKPOINT_V2.*_HANDOFF.md` | `ai_platforms/claude_projects/dev/checkpoints/CHECKPOINT_V2.*_HANDOFF.md` |
| `ai_platforms/claude_projects/output_v2/rag_decay_curve.md` | `ai_platforms/claude_projects/docs/rag_decay_curve.md` |
| `ai_platforms/claude_projects/output_v2/phase7_handoff.md` | `ai_platforms/claude_projects/docs/phase7_handoff.md` |
| `ai_platforms/claude_projects/output_v2/test_results_v2.md` | `ai_platforms/claude_projects/dev/test_results.md` |
| `ai_platforms/claude_projects/scripts_v2/*.py` | `ai_platforms/claude_projects/dev/scripts/*.py` |
| `ai_platforms/claude_projects/RETROSPECTIVE_V2.md` | `ai_platforms/claude_projects/docs/RETROSPECTIVE_V2.md` |
| `ai_platforms/claude_projects/PLAN_V2.md` | `ai_platforms/claude_projects/docs/PLAN_V2.md` |
| `ai_platforms/claude_projects/capacity_research.md` | `ai_platforms/claude_projects/docs/capacity_research.md` |

## 重跑脚本注意事项

- 脚本内 `OUTPUT_DIR = REPO_ROOT / "ai_platforms" / "claude_projects" / "output_v2"` 类常量是 reorg 前的路径, 需手动改为 `.../current/uploads/` 或 `.../docs/` 视场景
- `EVIDENCE_DIR` 类似需改为 `.../dev/evidence/`
- v2.6 终态后无重跑需求. 如果要跑新的批次 (v2.7+), 建议基于 reorg 后路径从零写新脚本, 不重用这些

## 为什么不改脚本/evidence 的路径?

历史记录价值 > 重跑便利. Evidence 里的 `_progress.json`, `trace.jsonl` 是事件流时序记录, `reviewer` 报告里引用的路径是当时写的, 改路径会模糊"谁在什么时间做了什么". Reorg 只改**导航层**文件 (README/索引/当前入口), 不改**历史层**文件.

---

*更新: 2026-04-20 晚 reorg.*
