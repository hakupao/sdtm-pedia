# SMOKE_V4 R3 — Reviewer Subagent Prompt Template (Rule D 隔离)

> 主 session 派 reviewer subagent 时, 用这个 template 作 prompt 骨架. 替换 `__Q_NUM__` / `__Q_BODY__` / `__JUDGE_CRITERIA__` / `__ANSWER_PATHS__`.
> Reviewer subagent_type 必须**不是**主 session 角色 (Rule D). 推荐 `oh-my-claudecode:scientist` (R3 内首次, 跨 run 不算重) 或 `feature-dev:code-reviewer`.

---

## Template

```
你是 SMOKE_V4 R3 跨平台评测 reviewer. 不要看主 session 已写的 inline self-score (`r3/evidence/<platform>/q__Q_NUM__.md` 末尾段), 独判.

# 输入

## 题文 (Q__Q_NUM__)

__Q_BODY__

## 评分判据 (引 SMOKE_V4.md §2 Q__Q_NUM__ 段)

__JUDGE_CRITERIA__

包含:
- 核心 PASS 判据 (必中)
- FAIL 判据 (触即 FAIL)
- AHP 题: PASS+ 条件 (识破错前提 + 纠正 + 给 canonical 路径)
- KB 锚点 (期望答案应引哪个 SDTM 章节 / domain / variable)

## 4 平台答案路径

请用 Read 工具读 4 份文件 raw content, 不只读末尾 inline self-score:

- Gemini: __ANSWER_PATHS__.gemini (`r3/evidence/gemini/q__Q_NUM__.md`)
- ChatGPT: __ANSWER_PATHS__.chatgpt (`r3/evidence/chatgpt/q__Q_NUM__.md`)
- NotebookLM: __ANSWER_PATHS__.notebooklm (`r3/evidence/notebooklm/q__Q_NUM__.md`)
- Claude: __ANSWER_PATHS__.claude (`r3/evidence/claude/q__Q_NUM__.md`)

# 任务

对 4 平台答案各打 verdict:

- **PASS** (1.0): 核心判据全中, 无 FAIL 判据
- **PASS+** (1.25, AHP 专属): PASS + 主动识破错前提 + 给 canonical 路径
- **PARTIAL** (0.5): 核心判据 ≥50% + 0-1 小缺漏
- **FAIL** (0): 核心判据 <50% OR 触 FAIL 判据
- **PUNT** (0, policy-correct): 模型拒答 + 拒答理由是边界, 不是 hallucination

# 输出格式 (写到 `r3/evidence/_reviews/q__Q_NUM___review.md`)

```markdown
# Q__Q_NUM__ Reviewer Verdict

> Reviewer subagent: `__SUBAGENT_TYPE__` (e.g., oh-my-claudecode:scientist)
> Run timestamp: <ISO date>
> Reviewer ≠ main session (Rule D ✓)

## 题文摘要 (1-2 句)

...

## 4 平台 verdict

| 平台 | 我的判 | 主 session inline self-score | 一致? |
|---|---|---|---|
| Gemini | PASS / PARTIAL / FAIL / PUNT | (从 q__Q_NUM__.md 末尾抽) | ✓/✗ |
| ChatGPT | ... | ... | ... |
| NotebookLM | ... | ... | ... |
| Claude | ... | ... | ... |

## 详细 reasoning (每平台一段, 3-5 句)

### Gemini
- 核心判据命中: [列具体哪些]
- 缺漏 / FAIL 触发: [列具体]
- KB 锚是否引对: [是/否, 引了什么]
- 与主 session 不一致点 (若有): [说明谁更对, 给证据]

### ChatGPT
...
### NotebookLM
...
### Claude
...

## 跨平台对比 (1 段)

- 哪个平台答得最完整? 为什么?
- 哪个平台触 hallucination 风险 (FAIL 判据)? 为什么?
- 4 平台对 KB 锚的引用一致性: 全引同一个章节 / 各引各的?

## Rule D 自检

- [ ] 我 (reviewer subagent_type=__SUBAGENT_TYPE__) ≠ 主 session
- [ ] 我没读主 session 的 inline self-score 再判
- [ ] 我独立从题文 + 判据 + 4 raw 答案推 verdict

## 不一致 carry-over (若与主 session 冲突)

主 session 在 R3_RETROSPECTIVE 决策段决断最终 verdict. 我的 verdict 留作独立记录。
```

# 注意

- **不要** 读 R1/R2 retrospective 干扰, 只看 R3 这次答案
- **不要** 给"该平台总体能力" 综合分, 只判这一题
- 4 raw 答案路径里末尾段有主 session inline self-score, **跳过那段不读** (避免锚定偏差)
- 若答案文件不存在 / 答案为空 (status=aborted), 标 N/A, 不打 FAIL (FAIL 是答错, N/A 是没答)
```

---

## 派发示例 (主 session 用 Agent 工具)

```
Agent({
  description: "R3 Q3 reviewer",
  subagent_type: "oh-my-claudecode:scientist",
  prompt: "<上面 template 替换好的内容>"
})
```

17 题 → 17 个 reviewer call, 可在 Phase B 后并行派发 (不等所有题答完再派, 题 N+5 答完时已可派 Q_N+5 的 reviewer 与跑题流水线).

## 失败处理

reviewer 输出文件未生成 / verdict 格式不合规 → 主 session 单独重派该题 reviewer (用不同 subagent_type 也行, 但需在 R3_RETROSPECTIVE 记录).
