# B2 Reviewer Prompt

## 上下文
独立复核 Phase 6.5 v2 Task B2 产出 (executor 已完成).
设计: design doc §2.3 + PLAN_V2.md §4 Task B2.
规则 D (审阅隔离): 你 (code-reviewer) 不是 executor, 本次复核独立.

## 复核目标
`ai_platforms/claude_projects/scripts_v2/score_domains.py`

## 复核步骤
1. Read 脚本源
2. Read B2_executor.md (设计规范) 对比实现
3. 从仓库根跑两次 `python3 ai_platforms/claude_projects/scripts_v2/score_domains.py`, 对比输出 (idempotent 验证)
4. 抽样验证:
   - a. 用户 20 域 (DM/SE/DS/BS/BE/MI/GF/PR/CM/EX/TU/TR/RS/SS/DD/LB/FA/CE/MH/SU) 全在必选
   - b. T_test_hits 6 域 (AE/PC/PP/EX/MH/LB) 全在必选 (EX/MH/LB 与用户重合, 应标 `must (user)` 或 `must (T_test_hits)` 之一, 不能漏)
   - c. 推荐合并总数 ∈ [25, 28]
5. 算法检查:
   - normalize 是否用 min-max? 是否对极端值敏感? (源码确认)
   - T_test_hits 加分 `0.2 * 20 = 4` 是否显著推高 (应明显优先于纯打分域)
6. 幂等性 (步骤 3)
7. 只读性: grep 脚本内是否有 `open(..., 'w')` / `os.remove` / `shutil.move` → 不应有

## 输出 (严格按此 Markdown 写到 `ai_platforms/claude_projects/output_v2/evidence_v2/B2_review.md`)

```markdown
# B2 Review — score_domains.py

> 复核日期: YYYY-MM-DD
> Reviewer: oh-my-claudecode:code-reviewer (model=opus)

## 结论
PASS / FAIL

## 抽样验证
- 用户 20 域全在必选: ✓/✗
- T_test_hits 6 域全在必选: ✓/✗
- 推荐合并总数: N (target 25-28): ✓/✗
- 幂等: ✓/✗
- 只读: ✓/✗

## 算法复核
- normalize 方法: min-max / z-score / 其他
- 极端值处理合理?
- T_test_hits 加分权重是否显著?

## 关键发现 (≤ 200 字)
...

## 下一步
如 PASS: 进 Task B3
如 FAIL: 列具体修复项, 回 executor
```

## 不要做
- 不要修改 score_domains.py
- 不要改 knowledge_base/
- 不要 PASS 存疑的点 (规则 A: 结构 PASS ≠ 业务 PASS)
- 输出只写到 B2_review.md, 其余只在对话回复中简报

## 工作目录
`/Users/bojiangzhang/MyProject/SDTM-compare/`
