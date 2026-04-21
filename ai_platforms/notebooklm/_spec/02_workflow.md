# 02 工作流 — 6 阶段模板

从"要部署 X 平台"到"发布版 + 复盘归档完成"的完整流程骨架. 按 Tier 伸缩.

---

## 总览

```
Phase 0: 启动                 ← 确认 Tier / 填 platform_profile / 问用户优先级
Phase 1: 调研 (Research)      ← 八问八答 / capacity 机制 / 失败模式
Phase 2: 策略设计 + PLAN      ← 内容策略 / 批次切分 / PLAN 编写
Phase 3: 落地 (Batches)       ← N 批渐进 / 每批 A/B / 失败归档
Phase 4: 审查 & A/B            ← 三 lane 独立审 / 矩阵全跑 / 规则 A 抽检
Phase 5: 收束 (Closure)       ← RETROSPECTIVE / handoff / UPLOAD_TUTORIAL
                                Reorg 四层 / 更新上游索引 / commit+push
```

**总壁钟**: Tier 1 小平台 ~2-4 小时 / Tier 2 ~1-3 天 / Tier 3 ~3-7 天.

---

## Phase 0: 启动 (30-60 分钟)

### 目标

在动笔之前, 把项目的**边界、优先级、Tier 等级**全部钉死.

### 必须的 artifact

- [ ] `docs/platform_profile.md` (或合并进 research.md) — 至少 80% 填充
- [ ] 用户业务优先级明文 (**规则 E 强制**), 记入 `docs/PLAN.md §优先级`
- [ ] Tier 等级确认

### 关键动作

1. **读 `00_platform_profile.md`**, 对照本平台填空
2. **问用户**:
   - 覆盖优先级是什么? (e.g. "core > supp > quest")
   - 哪些内容必须 100% 命中? 哪些可只覆盖高频?
   - 分享需求? (私有 / 团队 / 公开)
   - 性能/时效需求?
3. **定 Tier**: 参照全局 CLAUDE.md `<workflow_tiers>`
   - <5 步, <1 小时 → Tier 1
   - 5-15 步, 半天-1 天 → Tier 2 (本范本默认)
   - >15 步或多天 → Tier 3

### 退出条件

用户和主控对"本次做什么/不做什么"达成一致, Tier 定档, profile 填完.

---

## Phase 1: 调研 (Research, 30-120 分钟)

### 目标

把平台的**不透明行为**/限制/官方承诺都落到文档, 为 PLAN 提供事实基础.

### 必须的 artifact

- [ ] `docs/research.md` (八问八答) 或 `docs/capacity_research.md`
- [ ] 每个答案**附官方或社区实测链接**
- [ ] "对 PLAN 的修订" 段

### 关键动作

1. **按 `03_research.md` 模板填八问八答**
2. 如果发现初始假设错 (e.g. Claude 的 "200K 硬约束" 实际是 3-4M), 把修订写进 PLAN §0 修订记录
3. 如果平台容量不透明, 做一次 calibration 预实验 (上传已知 N tokens 的 dummy 文件, 测 Δcapacity)

### 退出条件

PLAN 所需的所有假设都有来源 (官方 / 实测 / 类似项目经验).

### 可跳过

Tier 1 小平台 + 官方文档清晰 + 无历史坑 → 八问缩减为 3 问 (容量/分享/索引指示器).

---

## Phase 2: 策略设计 + PLAN (1-3 小时)

### 目标

把"怎么做这次部署"写成可执行的任务清单, 明示 checkpoint 级别.

### 必须的 artifact

- [ ] `docs/PLAN.md` (按 `04_plan.md` 模板)
- [ ] `docs/solution.md` 或 PLAN 内嵌 §内容策略 (按 `05_solution.md` 模板)

### 关键动作

1. **按 `05_solution.md` 定内容策略**:
   - 源文件合并粒度 (按平台文件数/大小限)
   - 批次数量 (容量/质量曲线决定)
   - System Prompt 累积段数
   - Deferred stub 是否需要
2. **按 `04_plan.md` 写 PLAN**:
   - §0 修订记录
   - §1 执行规则 P1-P10 + 规则 E
   - §2 文件结构 map
   - §3-§N 每批 Task 分解 + checkpoint 级别 (hard/soft/none)
3. **不要跳过**:
   - 每个 Task 必须明示 `checkpoint_level: hard|soft|none`
   - 每个 Task 必须写 "Files: Create/Modify/Read"
   - 每个并行 Task 必须标 `parallel_with`

### 退出条件

PLAN 通读一遍, 每个 Task 都是 "我知道接下来该做什么 + 谁 reviewer + 怎么判 PASS".

---

## Phase 3: 落地 (Batches, 1-5 天)

### 目标

按 PLAN 批次执行, 每批产出"上传 ready"的文件 + A/B 回归 + evidence 三层.

### 每批的完整循环

```
Batch N:
1. Writer lane (executor subagent) 跑脚本 / 写文件 → 产出 stage_vN.X_*.md
2. Reviewer lane (code-reviewer subagent, 不同 subagent_type) 审 → 产出 stage_vN.X_review.md
3. 主控独立抽样 (规则 A, N=5-10 样本) → 产出 stage_vN.X_audit.md
4. 用户在 Claude Project (或对应平台测试实例) 做 A/B 回归
5. A/B 结果写 ab_reports/STAGE_<N>_AB_REPORT.md + 更新 dev/test_results.md
6. Hard checkpoint: 等用户 ack 才能推下一批
7. 如有失败: archive 到 evidence/failures/stage_<N>_attempt_<M>.md (规则 B)
8. 更新 L1 evidence/_progress.json + L2 evidence/trace.jsonl
```

### 必须的 artifact (每批)

- [ ] `stage_vN.X_*.md` (产物)
- [ ] `stage_vN.X_audit.md` (规则 A 抽检)
- [ ] `stage_vN.X_review.md` (独立 reviewer)
- [ ] `ab_reports/STAGE_<N>_AB_REPORT.md`
- [ ] `evidence/checkpoints/CHECKPOINT_<N>_HANDOFF.md` (如是 hard checkpoint)
- [ ] `evidence/_progress.json` 更新
- [ ] `evidence/trace.jsonl` 追加事件

### 关键动作

- **规则 A**: 压缩率 >50% 或改写率 >50% 的步骤, 强制 N 样本 reviewer + N 样本主控, 不重叠
- **规则 B**: 任何失败都归档, 不删
- **规则 D**: executor 和 reviewer 绝不是同一 subagent_type
- **规则 E (本范本)**: 如打分阶段发现用户优先级和默认打分冲突, 立即暂停重算, 不等收尾才重平衡

### 退出条件

所有批次产物齐, A/B 矩阵目标题数 PASS, 没有 blocking failure.

---

## Phase 4: 审查 & A/B (每批内嵌, 加 1 次终态)

本阶段**不是独立 Phase**, 而是 Phase 3 每批的**强制子步骤**. 但终态需要做一次整合审查:

- [ ] 跑完整 A/B 矩阵 (不是只跑新增题)
- [ ] 检查所有批次的 regression (历史 PASS 的题是否还 PASS, 规则 P10)
- [ ] 独立 reviewer 看 RETROSPECTIVE 草稿 (规则 D)

见 `06_review.md`.

---

## Phase 5: 收束 (Closure, 2-4 小时)

### 目标

产出三件套 (RETROSPECTIVE / handoff / UPLOAD_TUTORIAL) + reorg 目录 + 更新上游索引.

### 必须的 artifact

- [ ] `docs/RETROSPECTIVE.md` (三段式, 规则 C)
- [ ] `docs/handoff.md` (如有下游)
- [ ] `current/UPLOAD_TUTORIAL.md` (10 章节用户教程)
- [ ] `current/` 目录重组 (去版本号)
- [ ] `ROADMAP.md` 状态更新
- [ ] 上游 `ai_platforms/README.md` 总览表更新
- [ ] 项目 `CLAUDE.md` Key Paths 新增入口
- [ ] Git commit + push

### 关键动作

1. **写 RETROSPECTIVE** (必三段):
   - 保留下来的做法 (推广)
   - 必须补上的缺口 (G1/G2/...)
   - 关键决策复盘
2. **Reorg 目录**到四层: `current/docs/dev/archive`
3. **Check change chains**: 项目 `CLAUDE.md` 若定义 chain (e.g. 本项目 Chain D), 顺手更新
4. **单 commit commit 所有收束变更**, 写一行什么提交了

### 退出条件

- 零 pending task
- A/B 矩阵全 PASS
- 三件套全产
- git push 无冲突
- 用户可按 UPLOAD_TUTORIAL 独立跑通部署

---

## Tier 伸缩速查

| 阶段 | Tier 1 | Tier 2 | Tier 3 |
|------|--------|--------|--------|
| Phase 0 | 直接定 | profile 填完 | profile + calibration |
| Phase 1 | 3 问 | 8 问 | 8 问 + calibration 实验 |
| Phase 2 | PLAN 简化为 checklist | 完整 PLAN | PLAN + subagent_prompts 模板预写 |
| Phase 3 | 1 批到位 | 2-5 批 + hard checkpoint | 5+ 批 + 全 evidence 三层 |
| Phase 4 | A/B 3-5 题 | A/B 10-15 题 | A/B 20+ 题 + 跨批 regression |
| Phase 5 | 一段话复盘 | 三段式 + handoff | 三段式 + handoff + rag_decay_curve (如需要) |

---

## 如果在某阶段卡住

| 卡点 | 处理 |
|------|------|
| 调研发现初始假设全错 | Pause, 重写 PLAN §0 修订记录, 再继续 |
| 某批 A/B 衰减 ≥2 题 | **立即停** (规则 P10), reviewer 归因, 写 failures/ |
| reviewer PASS 但主控抽样 FAIL | **尊重主控** (v1 G1 教训: 技术 PASS ≠ 业务 PASS), 重试 |
| Hard checkpoint 等用户 > 1 天 | 不推进, 记录等待状态到 `_progress.json.status = paused` |
| 批次数 /容量超预算 | 先看是不是内部冗余太多, 优先降冗余再考虑降覆盖 |

---

*来源: claude_projects v1 Phase 1-12 + v2 Phase A-H 流程抽象.*
