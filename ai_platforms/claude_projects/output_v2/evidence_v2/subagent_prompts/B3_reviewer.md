# B3 Reviewer Prompt

## 上下文
独立复核 Phase 6.5 v2 Task B3 产出 (executor 已完成).
设计: design doc §2.5 + PLAN_V2.md §4 Task B3.
规则 D: 你 (code-reviewer) 是独立 agent, 不能代写/修改.

## 复核目标
`ai_platforms/claude_projects/scripts_v2/score_codelists.py`

## 复核步骤
1. Read 脚本源
2. Read `output_v2/evidence_v2/subagent_prompts/B3_executor.md` 对比设计
3. 从仓库根跑两次 `python3 ai_platforms/claude_projects/scripts_v2/score_codelists.py`, 对比输出 (idempotent)
4. 抽样验证:
   - a. Total codelist 数 ≈ 1005 (±5%)
   - b. T_codelist_hits 中至少 NY/FREQ 2 个在 top 200 (已存在的 codelist)
   - c. AERELN/PROBLEM_TYPE 的报告是 "not mapped" 而非崩溃
   - d. top 200 估 token ∈ [150K, 300K] (目标 ~200K)
   - e. rank 201-500 估 token ∈ [250K, 500K] (目标 ~300-400K)
5. 算法检查:
   - sigmoid_term 实现公式是否正确 `1 / (1 + abs(log10(n+1) - log10(30)))`, n=0 → 0
   - 抽样 3 个 codelist 的 term_count 人工核对 (Read knowledge_base/terminology/ 对应文件)
   - domain_ref_count 准确 (抽 2 个 codelist 人工 grep domains/*/spec.md)
6. 只读性 (grep 脚本, 不应有 write/remove/subprocess)
7. 幂等 (步骤 3)

## 输出 (纯文本回复我, 我会落盘)
按以下 Markdown 结构返回:

```markdown
# B3 Review — score_codelists.py

> 复核日期: 2026-04-18
> Reviewer: oh-my-claudecode:code-reviewer (model=opus)

## 结论
PASS / FAIL

## 抽样验证 (5 项)
- Total ≈ 1005: ✓/✗
- NY/FREQ in top 200: ✓/✗
- AERELN/PROBLEM_TYPE 报告为 not mapped 不崩: ✓/✗
- top 200 估 token ∈ [150K, 300K]: ✓/✗
- rank 201-500 估 token ∈ [250K, 500K]: ✓/✗

## 算法复核
- sigmoid_term 实现:
- 3 个 codelist term_count 人工核对:
- 2 个 codelist domain_ref 人工核对:

## 幂等 + 只读
- 幂等: ✓/✗
- 只读: ✓/✗ (grep 结果)

## 关键发现 (≤ 200 字)
...

## 下一步
如 PASS: 进 Task B4
如 FAIL: 列具体修复项
```

## 不要做
- 不修改脚本或 knowledge_base
- 不 PASS 存疑的点
- 不输出到文件 (你无 Write 工具), 只回复纯文本

## 工作目录
`/Users/bojiangzhang/MyProject/SDTM-compare/`
