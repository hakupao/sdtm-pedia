# Phase 6.5 Claude Projects — 复盘

> 范围: Step 1-12 (2026-04-17, commit `ec4cecb` → `ad14f6a`)
> 产出: 11 个压缩文件 (192,036 tokens), 14 次 subagent 调用, 2 次重试, 0 次源污染
> 状态: 等待 Step 13 手动上传

---

## 1. 保留下来的做法 (推广到其他项目)

| # | 做法 | 理由 |
|---|------|------|
| R1 | PLAN.md 五段式 (需求→方案→取舍→实施→验证) | 决策有纸面 trail, 3 个月后能复原 why |
| R2 | 失败归档不删 (`failures/step_06_attempt_1.md`) | 失败数据最贵, 重跑时是参考 |
| R3 | Writer ≠ Reviewer (不同 agent 或至少不同 model) | 同一 agent 自审 = 无审 |
| R4 | 源只读 + 产物独立目录 | git status `knowledge_base/` 全程 clean 是可验证的防御 |
| R5 | 预授权 + 硬 checkpoint 两级 | 低风险 auto-continue, 高风险停下来等 ack |

## 2. 必须补上的 (这次漏了)

| # | 缺口 | 补法 |
|---|------|------|
| G1 | **语义抽检不统一**: Step 6 做了 20 样本审计揪出 20% 信息丢失, Step 7/9 没做同等审计 | 下次: 压缩率 >50% 的步骤强制 N 样本抽检, N 写进 PLAN |
| G2 | **状态三写**: `_progress.json` + `trace.jsonl` + `evidence/step_NN.md` 在记同一件事 | 下次: 选一个当 single source of truth, 其他从它生成 |
| G3 | **subagent_prompts/ 只留了 9/14**: 半截反而有"记录完整"的错觉 | 下次: 全留或不留, 不留半截 |
| G4 | **Checkpoint 触发规则隐式**: "什么算关键 step" 没写进 PLAN | 下次: PLAN §4 每个 step 明示 checkpoint 级别 (hard/soft/none) |

## 3. 关键决策复盘

### 3.1 Step 6 — 技术 PASS 被业务 FAIL (最重要的一次)

- **reviewer 给了 PASS**: Level 4 方案 58,706 tokens, 63/63 域结构完整, md5 稳定
- **主控做了独立抽样**: 20 个变量里 4 个是独有信息 (AGE 推导式、VSPOS 枚举、COUNTRY、SEX)
- **用户决定**: 否决 PASS, 重试"混合 Notes 保留"方案, 最终 65,993 tokens (超目标 10%, 在 accept_window 内)
- **教训**: **结构检查 ≠ 语义检查**. reviewer 的 PASS 不能免掉业务抽样这一刀

### 3.2 预授权 "继续，一直继续即可"

- 用了 5 次 auto-continue, 省掉 5 次等待 ≈ 30 分钟
- 但 Step 6/12 依然停下等 ack, 因为这两个是不可逆大决策
- **推广**: 预授权边界要明示哪些 step 可以跳, 哪些不能跳

### 3.3 并行化 Step 4/5 + Step 7/8/9

- Step 4/5 各 ~3min, 并行后总 ~3min (节省 ~3min)
- Step 7/8/9 各 5-7min, 并行后 ~7min (节省 ~10min)
- **推广**: 无数据依赖的 step 默认并行, PLAN 里标 `parallel_with`

## 4. 四条可迁移规则 (已固化到全局 CLAUDE.md)

1. **规则 A (语义抽检)**: 压缩率 >50% 或改写率 >50% 的步骤, 强制 N 样本独立抽检, N 写 PLAN, 结果留 evidence.
2. **规则 B (失败归档)**: 任何 attempt 都不删, 归档到 `failures/step_NN_attempt_X.md`, 含输入/产物/技术判定/业务判定/下一 attempt 输入.
3. **规则 C (Retro 强制)**: Tier 2/3 项目收尾前必写 RETROSPECTIVE.md, 至少三段: 保留/补上/决策复盘.
4. **规则 D (审阅隔离)**: Writer 和 Reviewer 不能是同一 agent 同一 session, 即使都用 opus.

## 5. 这次留下但不一定每次都做

- `trace.jsonl` (61 条) — 大项目值得, 小项目过度
- `evidence/step_NN_*.md` × 11 — 同上
- `subagent_prompts/` 全留 — 除非做 agent 行为分析, 否则过度

---

## 附: 工作量数据

| 指标 | 值 |
|------|------|
| 源 tokens | 2,527,153 |
| 压缩后 tokens | 192,036 (92.4% 压缩) |
| 脚本行数 | ~2,000 行 Python (11 个脚本) |
| Subagent 调用 | 14 次 (executor 8 + reviewer 5 + verifier 1) |
| 重试 | 2 次 (Step 6 + Step 8 attempt 2) |
| 主控 checkpoint | 4 次 (Step 3/5/6/12) |
| 源文件污染 | 0 |
| 壁钟时间 | ~2.5 小时 |
