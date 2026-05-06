# 我的 AI 协作工作流 v1.0 (2026-04-18 定稿)

> 来源: SDTM-compare Phase 6.5 复盘 + AI 优化后的精炼版.
> 定位: **Tier 分档 + 4 条硬规则 + 骨架模板**. 适用于和 AI 协作的任何多 step 任务.
> 完整模板: `~/.claude/templates/workflow-tier{2,3}.md`.

---

## 一句话定位

> 结构检查 ≠ 语义检查. 流程仪式 ≠ 流程规范. 先分档, 再照骨架跑, 踩坑归档, 收尾必复盘.

---

## 0. 起手三分钟 (新项目进来第一件事)

1. **评估体量** → 选 Tier (见 §1)
2. **建骨架** → 按 Tier 的目录清单创建 (见 §3)
3. **写 PLAN.md** → 先 TL;DR 200 字, 再五段式 (见 §4)
4. **确定规则触发点** → 哪些 step 压缩率 >50% (需规则 A 抽检) / 哪些 step 不可逆 (需 hard checkpoint)

不要一上来就写代码或叫 agent. 这三步不做, 后面一定返工.

---

## 1. 分档 (Tier 1/2/3)

| Tier | 判定条件 | 配备 | 典型耗时 |
|:----:|---------|------|---------|
| **1** | <5 step, <1h, 可回滚 | 直接跑, 收尾 1 段 retro 口头即可 | 十几分钟到 1 小时 |
| **2** | 5-15 step, 半天-1天, 多文件改动 | PLAN.md + `_progress.json` + `evidence/checkpoints/` + `evidence/failures/` + `RETROSPECTIVE.md` | 半天-1 天 |
| **3** | >15 step 或多天, 高 stakes (不可重来/多平台部署) | Tier 2 基础上 + `trace.jsonl` + `subagent_prompts/` 全留 + `audit_matrix.md` | 多天 |

**判定口径**:
- 任务里是否有"压缩率 >50% 且错了要重跑"的步骤? → **至少 Tier 2**
- 任务是否跨多次对话 / 多 session? → **至少 Tier 2, 有恢复需求则 Tier 3**
- 错了能立刻 git revert 重来? → Tier 1 就够

---

## 2. 四条硬规则 (不分 Tier, 全员适用)

| 规则 | 内容 | 触发场景 | 违反后果 |
|:----:|------|---------|---------|
| **A 语义抽检** | 压缩率 >50% 或改写率 >50% 的 step, 强制 N 样本独立抽检 (N 预先写进 PLAN, 典型 N=20), 结果留 `evidence/step_NN_audit.md` | 任何压缩/改写 | 结构 PASS 但业务 FAIL, 产物要重做 |
| **B 失败归档** | 任何失败 attempt 归档到 `failures/step_NN_attempt_X.md`, 含输入/产物/技术判定/业务判定/下一 attempt 输入, 绝不 rm | 任何 retry | 下次重跑无参考, 白踩坑 |
| **C Retro 强制** | Tier 2/3 收尾前写 RETROSPECTIVE.md, 三段: 保留/补上/决策复盘 | Tier 2/3 收尾 | 下个项目同坑再踩 |
| **D 审阅隔离** | Writer 和 Reviewer 不能是同一 agent 同一 session, 即使都用 opus 也要 `subagent_type` 不同 | 每个 step | 自审 = 无审, PASS 没有意义 |

---

## 3. 骨架目录

### Tier 2 (最低配)

```
<project-root>/
├── PLAN.md              # 五段式, 含 TL;DR
├── _progress.json       # 单一状态源
├── evidence/
│   ├── checkpoints/     # ckpt_step_NN.md
│   └── failures/        # step_NN_attempt_X.md (绝不删)
└── RETROSPECTIVE.md     # 收尾必写
```

### Tier 3 (Tier 2 + 额外)

```
evidence/
├── trace.jsonl                # 自动 append, 每事件一行 JSON
├── subagent_prompts/          # 全留, 按 step_NN_<role>.md 命名
│   └── step_NN_executor.md
└── audit_matrix.md            # 所有高压缩 step 的抽检汇总表
```

---

## 4. PLAN.md 骨架

```markdown
# <项目名> — Plan

> TL;DR: <200 字, 目标+选定方案+主要风险, 3 个月后你自己要能一眼复原>

## 1. 需求 (why)
- 背景
- 核心矛盾 (现状 vs 要求)
- 衍生需求

## 2. 方案候选
| # | 路径 | 可达效果 | 核心问题 |

## 3. 决策
- 选了哪个, 理由
- 关键边界决策表 (D1-D.N)
- 风险识别 + 应对

## 4. 实施 (Step 表)
| Step | 任务 | 输入 | 输出 | 目标指标 | Checkpoint 级别 | Parallel With |

## 5. 验证
- L1 结构检查 (文件数/大小/md5/schema)
- L2 语义抽检 (哪些 step 触发规则 A, N 是多少)
```

**关键**: Step 表里必须明示每个 step 的 **Checkpoint 级别** 和 **Parallel With**. 这两个列缺了就等于没写 PLAN.

---

## 5. 每 Step 三角色

```
主控 (你 + 总调度 Claude)
  ├─ Writer (executor, 写产物, opus/sonnet 按复杂度)
  └─ Reviewer (code-reviewer, 不同 agent, verdict: PASS/CONDITIONAL/FAIL)
```

流程:
1. 主控喂 prompt 给 Writer
2. Writer 交产物, Writer prompt 归档到 `evidence/subagent_prompts/`
3. 主控喂产物+标准给 Reviewer (必须是不同 agent)
4. Reviewer 给 verdict
5. 如压缩/改写率 >50% → 主控做规则 A 抽检
6. 判: 继续 / 重试 / checkpoint 停

---

## 6. Checkpoint 规则

| 级别 | 何时用 | 处理 |
|:-----|-------|------|
| **hard** | 不可逆决策 / 压缩率 >50% / 首次遇到的操作 | **停**, 等用户 ack, 写 `evidence/checkpoints/ckpt_step_NN.md` |
| **soft** | 中段进度汇报 / phase 切换 | 汇报即可, auto-continue |
| **none** | 小步骤 / 幂等 | 直跑 |

**预授权**: 用户可说"继续，一直继续即可"跳过 soft 和 none.
**边界**: hard 永远不能被预授权跳过, 就算你开了 auto-mode.

---

## 7. 语义抽检 (规则 A 实操)

`evidence/step_NN_audit.md` 模板:

```markdown
# Step NN — 语义抽检

> 抽样 N=20, 随机来源: <如: 5 域 × 4 变量>
> 标准: 独有信息丢失率 ≤5% 为 PASS

| # | 样本 | 源内容片段 | 产物内容片段 | 独有丢失? |
|---|------|-----------|-------------|:---------:|
| 1 | AE.AGE | "May be derived from RFSTDTC..." | (无) | ✗ (丢失) |
| 2 | ... | ... | ... | ✓ (保留) |

独有丢失率: X/20 = Y%
业务判定: **PASS / FAIL**
若 FAIL: 根因 + 重试方案
```

**关键**: 抽样要**独立**, 不能只抽 executor 声明覆盖的. 随机抽, 才能揪出 executor 的盲区.

---

## 8. 失败归档 (规则 B 实操)

`failures/step_NN_attempt_X.md` 模板:

```markdown
# Step NN Attempt X — 失败归档

> 归档时间: YYYY-MM-DD HH:MM
> 技术判定: PASS/CONDITIONAL/FAIL (reviewer verdict)
> 业务判定: FAIL (用户决策)
> 为何"失败": <一句话>

## 1. 输入
## 2. 产物 (文件 + md5, 可能会被下一 attempt 覆盖)
## 3. 技术验证 (哪些 PASS, 哪些 FAIL)
## 4. 业务不可接受的原因 (数据驱动)
## 5. 用户决策 (retry 还是 accept)
## 6. 对下一 attempt 的输入 (修改建议)
```

---

## 9. Retro 模板 (规则 C 实操)

`RETROSPECTIVE.md` 模板:

```markdown
# <项目> — 复盘

> 范围 / 产出 / 状态

## 1. 保留下来的做法 (R1-R.N, 推广到其他项目)
## 2. 必须补上的 (G1-G.N, 这次漏了)
## 3. 关键决策复盘 (几个关键节点的为什么这样选)
## 4. 可迁移规则 (写进全局 CLAUDE.md 的候选)
## 5. 本次过度工程化, 下次不必做的
## 附: 工作量数据 (token/耗时/subagent 数/retry 数/源污染)
```

---

## 10. 禁止清单 (血泪教训)

- ❌ 一个 agent 自写自审
- ❌ 删失败 attempt
- ❌ PLAN.md 不写 TL;DR
- ❌ 压缩率 >50% 只靠结构检查
- ❌ Tier 2/3 项目跳过 retro
- ❌ `subagent_prompts/` 只留一半
- ❌ Tier 1 小任务套 Tier 3 仪式
- ❌ Tier 3 大项目裸跑不记 trace
- ❌ 状态分散写三份 (选一个主)
- ❌ 无 `recovery_hint`, 断 session 就废

---

## 11. 推荐调度模式

- **并行**: PLAN 里标 `parallel_with`, 主控在同一 message 里多 tool 调用
- **串行 + hard checkpoint**: 不可逆 step / 首次操作
- **阶段汇报**: Tier 3 每 3-5 step 写一条 `phase_report` 到 trace, 避免 budget 失控看不见

---

## 12. 未来迭代空间 (v1 留下的 TODO)

1. **状态单一源**: 现在 `_progress.json` + `trace.jsonl` + `evidence/step_NN.md` 仍有重叠, v2 要选一个当主, 其他从它生成
2. **抽检样本自动化**: 现在靠人手点样, 未来可以脚本化"随机抽 N 个样本 diff"
3. **Tier 自动判定**: 输入任务描述 → AI 建议 Tier, 避免直觉偏差
4. **跨项目规则库**: 规则 A/B/C/D 之外, 未来项目里揪出的新规则统一进全局 CLAUDE.md `<personal_operating_principles>`

---

## 13. 一句话带走

> **先分档, 照骨架跑, 规则 A 别偷懒, retro 别跳过. 直觉走到某个点会掺水, 硬规则是反掺水的锚.**
