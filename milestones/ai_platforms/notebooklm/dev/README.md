# NotebookLM — `dev/` 开发区导航

> 过程产物、证据链、A/B 报告、脚本冷区. 用户视角走 [`../current/`](../current/), 方法论走 [`../docs/`](../docs/).

---

## 路径约定

本 `dev/` 下一切路径都**故意保留执行时刻的语境**. 如果未来 reorg (把 v1 搬 archive/v1/), 脚本里的 `dev/evidence/xxx.md` 等 hardcoded 路径**不改**, 由本 README 的映射表承担"翻译"职责 (目前 v1 尚未发布, 无映射条目).

---

## 子目录

| 目录 | 用途 | 写入时机 |
|------|------|---------|
| `evidence/` | L1 `_progress.json` (唯一事实源) + L2 `trace.jsonl` (Tier 3 才必要) + L3 `subagent_prompts/` / `failures/` / `checkpoints/` | 每次 Phase 推进 |
| `evidence/subagent_prompts/` | writer/reviewer subagent 接到的完整 prompt (规则 D 审计用) | 每次派发 subagent 时 |
| `evidence/failures/` | 失败归档 (规则 B, 不删) — `stage_NN_attempt_X.md` | 任何 attempt 失败时 |
| `evidence/checkpoints/` | 每批 hard checkpoint handoff 文档 | 每次 hard checkpoint 必停 |
| `ab_reports/` | 每批 A/B 测试报告 `STAGE_<N>_AB_REPORT.md` | 本平台单批, 终态 1 份 |
| `checkpoints/` | Cowork / 自动执行 handoff | 按需 |
| `scripts/` | 构建/合并/上传脚本 (如果需要把 293 md 合并到 50 sources) | Phase 2/3 |

---

## 本平台简化说明

- **Tier 2** 但偏轻 — 单批上传, 无 RAG 衰减实验, trace.jsonl **可跳** (Tier 3 才强制)
- **规则 A (语义抽检)** 因为无大规模改写, 初步判断**不触发** (只做文件合并非压缩). Phase 2 PLAN 复核
- **规则 B (失败不删)** 按常规执行
- **规则 C (RETROSPECTIVE)** Tier 2 强制, Phase 5 必出
- **规则 D (写审分离)** subagent_type 至少用 2 种, 每 Phase 审查不得同 type

---

## 和主流程的差异速查

| 范本字段 | 本平台差异 | 记录位置 |
|---------|---------|---------|
| `capacity calibration` (Q8) | 跳过 — 官方硬指标透明 | `docs/platform_profile.md §B` |
| `System Prompt 累积设计` | 不适用 — 平台无 Custom Instructions | `docs/platform_profile.md §D` |
| `A/B 矩阵 10 题` | 扩到 15 (+ 5 独有生成物) | `docs/platform_profile.md §G` |
| `多批上传` | 单批 | 本文件 |

---

*建立日期: 2026-04-21.*
