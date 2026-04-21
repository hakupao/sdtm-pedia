# 07 Subagent 调度协议

Phase 3 执行期间, subagent 派发的操作规范. 保证规则 D (写审分离) + P6 (上下文隔离) + P4 (checkpoint 分层).

---

## 角色 & subagent_type 映射

| 角色 | 职责 | 推荐 subagent_type (选一) |
|------|------|--------------------------|
| Writer | 写脚本 / 合并文件 / 写 System Prompt 段 / 写 PLAN-Task 产物 | `executor`, `oh-my-claudecode:executor`, `feature-dev:code-architect`, `oh-my-claudecode:writer` |
| Reviewer | 独立复核 Writer 产物, 出 verdict | `code-reviewer`, `oh-my-claudecode:code-reviewer`, `pr-review-toolkit:code-reviewer`, `feature-dev:code-reviewer` |
| Researcher | 外部调研 / 容量机制 / 平台限制 | `oh-my-claudecode:document-specialist`, `general-purpose`, `Explore` |
| Planner | 策略/架构设计 | `oh-my-claudecode:planner`, `feature-dev:code-architect`, `Plan` |
| Verifier (可选) | 终态验证 | `oh-my-claudecode:verifier`, `pr-review-toolkit:silent-failure-hunter` |

**强制**: Writer 与 Reviewer 必**不同 subagent_type** (规则 D). 即使都用 opus, subagent_type 也要不同.

---

## 派发前必备 (每次调用)

- [ ] **明确角色**: writer / reviewer / researcher / planner / verifier
- [ ] **选 subagent_type**: 从角色映射表
- [ ] **选 model**: 复杂度决定
  - `haiku` — 简单 lookup / 格式化
  - `sonnet` — 标准执行
  - `opus` — 架构 / 深度分析 / 审查 blocking 决策
- [ ] **写独立 prompt**: 不引用 conversation 隐含上下文
- [ ] **归档 prompt**: `dev/evidence/subagent_prompts/<stage>_<role>_<N>.md`

---

## Prompt 模板

### Writer (executor) 模板

```markdown
# 任务

<简述任务: e.g. 写脚本 extract_terminology_terms.py 抽取指定 codelist 的 Term 值>

## 输入

- PLAN: `<path>/PLAN.md` 的 Task <X.Y> 段
- 源文件: `knowledge_base/terminology/<...>`
- 依赖上一批产物: `<file_list>` (若有)

## 产物要求

- <输出路径>
- <格式规范>
- <token target>

## 强制约束

- 源文件只读 (P5)
- 不读 conversation 历史, 不读 reviewer 报告
- 打印 stage tokens: `[Stage vX.Y] <file>: <N> tokens (target ≤<X>K)`
- md5 幂等 (重跑应一致)

## 验收 (自检)

- [ ] <check 1>
- [ ] <check 2>
- [ ] <check 3>

## 完成后

- 更新 `dev/evidence/_progress.json` 加一条 stage 完成记录
- 追加 `dev/evidence/trace.jsonl` 一行 `{"event": "stage_done", ...}`
- 不要主动调用 reviewer, 等主控派发
```

### Reviewer 模板

```markdown
# 独立复核

<简述: e.g. 独立复核 Stage vB.2 examples 高频域合并产物>

## 输入 (仅读这些)

- PLAN: `<path>/PLAN.md` 的 Task <X.Y> 段 (验收标准)
- Writer 产物: `<produced_files>`
- 基线对照 (如有): `<baseline_files>`

## 不读

- Writer 的 prompt
- conversation 历史
- 其他 reviewer 的历史报告 (每次独立审)

## 审查 checks

1. **结构完整性**: 段数 == 源文件数? 格式合规?
2. **引用溯源**: 每段有源文件路径标注?
3. **token 目标**: 实测 tokens 在 target ± 10% 内?
4. **md5 幂等 (如果脚本)**: 重跑产物 md5 一致?
5. **规则合规**: P1-P10 + 规则 A/B/C/D 涉及本批的是否遵守?
6. **跨批 regression**: 本批改动是否影响前批产物? (e.g. System Prompt 追加段有没有破坏前段)
7. **平台特化**: 本批产物是否符合 platform_profile 的约束?

## Verdict

输出 **一个** 结论:
- **PASS**: 全部通过
- **CONDITIONAL_PASS**: 列 MEDIUM / LOW 改动建议 (可接受, 不 blocking)
- **FAIL**: 列 BLOCKING / HIGH 问题, 必须修

## 报告

写到 `dev/evidence/<stage>_reviewer.md`:

- checks 结果 (7 项)
- 严重度分级 (BLOCKING / HIGH / MEDIUM / LOW / COSMETIC)
- 证据 (引 Writer 产物的具体行 / 源文件对照)
```

### Researcher (文档调研) 模板

```markdown
# 调研任务

<e.g. 调研 ChatGPT GPTs 的 File Search / Knowledge 容量上限>

## 目标

回答 `03_research.md` 八问中的 <Q N>.

## 方法

- 优先: 官方文档
- 次: 社区实测 (知名博客 / 官方支持 thread)
- 禁止: 凭记忆回答 (训练数据可能过时)

## 产物

填入 `<platform>/docs/research.md` §Q <N>, 每条断言附链接.
```

---

## Checkpoint 分层 (P4)

每次 subagent 调用后, 决定是否 "硬停":

| 级别 | 触发 | 动作 |
|------|------|------|
| `none` | 低风险 (setup, 脚本测试, 简单 lookup) | 自动继续下一 step |
| `soft` | 中风险 (某批产物已成, reviewer PASS) | 主控独立抽样 (规则 A) 后决定 |
| `hard` | 高风险 (A/B 回归 / 容量决策 / Phase 切换 / 收束) | **停, 等用户 ack**, 不擅自连续推进 |

**每个 Task 的 checkpoint 级别必须写在 PLAN §3-§N**, 不要事后决定.

---

## 预授权 + Hard Checkpoint 混合

### 预授权 (用户明说 "继续, 一直继续即可")

用户主动允许**跳过 soft checkpoint**, 仅保留 hard. 节省反复 ack 的时间.

**Claude v1 数据**: 预授权 + 5 次 auto-continue 节省 ~30 分钟.

### Hard checkpoint 不受预授权影响

**不可逆大决策**永远需要 ack:
- A/B 回归结果 (continue / hold / rollback)
- 容量超预算
- 源文件污染警报
- 收束 push

### 判定方法

Writer/reviewer 在完成一个 Task 后, 自问:
1. 我做的事是否**可以反悔**? (不可反悔 → hard)
2. 是否影响**用户能看到的东西**? (影响 → hard)
3. 是否触发**规则 P10 / 失败归档**? (触发 → hard)
4. 否则 → soft (走规则 A 抽样后推进).

---

## Prompt 归档 (规则 B + P6)

**每次 subagent 调用的 prompt 必须落盘**, 不论成功或失败.

**路径**: `dev/evidence/subagent_prompts/<stage>_<role>_<N>.md`

**命名示例**:
- `subagent_prompts/B2_executor_examples_merge.md`
- `subagent_prompts/B2_reviewer_examples_merge.md`
- `subagent_prompts/H1_reviewer_retrospective.md`

**归档价值**:
- 复盘时能重放
- 做 prompt 变体实验 (e.g. "如果 reviewer prompt 改这句话, verdict 会变吗")
- Tier 3 项目强制全留; Tier 2 关键节点留 (e.g. 每批 1 份 writer + 1 份 reviewer); Tier 1 可省

**反例 (v1 G3 教训)**: "subagent_prompts/ 只留了 9/14" = 半截反而有"记录完整"的错觉. 全留或不留, 不留半截.

---

## 并行化 (节省时间)

### 可并行的 Task 对

- 无数据依赖的 Step (e.g. B1 build + B2 build 互不读彼此产物)
- writer + researcher 混合 (researcher 不影响 writer 产物)

### PLAN 中标 `parallel_with`

```markdown
### Task B.1: chapters 展开
- parallel_with: Task B.2 (无依赖)

### Task B.2: model 合并
- parallel_with: Task B.1
```

**Claude v1 数据**: Step 4/5 并行节省 ~3 分钟 / Step 7/8/9 并行节省 ~10 分钟.

### 不可并行

- Writer → Reviewer (必串, Reviewer 要读 Writer 产物)
- Reviewer → 主控抽样 (可并行, 但主控不读 Reviewer 报告, 规则 A)
- 终态 A/B → 收束 (必串)

---

## Subagent 失败处理

### Writer 失败

- 归档 `dev/evidence/failures/stage_<N>_attempt_<M>.md` (规则 B)
- 内容: 输入 / 产物 (如有) / 技术判定 / 业务判定 / 下一 attempt 输入调整
- 重试 attempt+1, 新 prompt 调整产物描述或 subagent_type
- 连续 3 次失败 → hard checkpoint, 问用户 continue/rollback/重定义

### Reviewer FAIL verdict

- Writer 看 reviewer 报告, 改产物, 再派发 reviewer
- 注意**不能让同一 reviewer 审自己建议后的改动** (conflict of interest), 换另一 reviewer subagent_type 审第二遍, 或回到主控抽样

### 主控抽样 FAIL 但 reviewer PASS

- **尊重主控** (v1 G1 教训)
- 重新派发 writer, prompt 里附主控 FAIL 的具体样本问题
- 不要"辩论" reviewer 的 PASS (结构和语义是不同维度)

---

## 调度记录落到 trace.jsonl

每次派发应追加 trace.jsonl:

```jsonl
{"ts": "2026-04-20T10:15:00Z", "event": "executor_dispatched", "stage": "vB.2", "role": "writer", "subagent_type": "executor", "model": "opus", "prompt_file": "subagent_prompts/B2_executor_examples_merge.md"}
{"ts": "2026-04-20T10:47:00Z", "event": "executor_done", "stage": "vB.2", "verdict": "success", "output_files": ["stage_vB.2_examples_high.md"]}
{"ts": "2026-04-20T10:48:00Z", "event": "reviewer_dispatched", "stage": "vB.2", "subagent_type": "code-reviewer", "model": "opus"}
{"ts": "2026-04-20T11:05:00Z", "event": "reviewer_done", "stage": "vB.2", "verdict": "PASS"}
```

---

## 范例参考

Claude v2 完整 subagent 调度记录: `claude_projects/dev/evidence/subagent_prompts/` (14 份) + `trace.jsonl` (65 events). 值得照搬结构.

---

*来源: claude_projects v1 G3 "subagent_prompts 半留" 教训 + v2 14 次 executor/reviewer 调用 + 全局 CLAUDE.md 规则 D/P6.*
