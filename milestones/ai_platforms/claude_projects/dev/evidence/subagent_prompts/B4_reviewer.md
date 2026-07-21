# B4 Reviewer Prompt

## 上下文
独立复核 Phase 6.5 v2 Task B4 产出 (executor 已完成, handoff 到新 session).
设计: PLAN_V2.md §4 Task B4 + subagent_prompts/B4_executor.md (executor 说明).
规则 D: 你 (code-reviewer) 是独立 agent, 不能代写/修改.

## 复核目标
`ai_platforms/claude_projects/scripts_v2/build_v2_stage.py`

## 复核步骤
1. Read `ai_platforms/claude_projects/scripts_v2/build_v2_stage.py`
2. Read `ai_platforms/claude_projects/output_v2/evidence_v2/subagent_prompts/B4_executor.md` 对比设计
3. 从仓库根跑 `python3 ai_platforms/claude_projects/scripts_v2/build_v2_stage.py --stage v2.1 --dry-run`, 验证:
   - stdout 含 8 步 `[DRY] Step N:` 行
   - 不实际改任何文件 (Run 前后 `git status` 应相同, 或 stage 检查 output_v2/*.md md5 不变)
4. 分支完整性检查:
   - v2.1 分支完整 (调 rebuild_chapters_full.py 或检查其存在)
   - v2.2-v2.5 分支可 stub, 但 --stage v2.3 --dry-run 应打印可读 TODO 而不崩溃
5. STAGE_MAP 硬编码与 executor prompt §stage 映射一致 (5 键 v2.1-v2.5)
6. 幂等性检查: 假想连跑两次 --stage v2.1 (非 dry-run), upload_manifest_v2.md 不重复追加 (grep stage 行去重逻辑)
7. 只读 knowledge_base: grep 脚本里 `knowledge_base` 的使用, 不应有 write/open('w')/remove
8. system_prompt_v2.md 修订策略: 脚本使用 `<!-- stage v2.X begin/end -->` 标记段替换 (非盲目 append)
9. --dry-run 真的不改文件 (grep write_text / open('w') 等, 确认被 dry_run flag gate 住)

## 输出 (纯文本回复我, 我会落盘)
按以下 Markdown 结构返回:

```markdown
# B4 Review — build_v2_stage.py

> 复核日期: 2026-04-18
> Reviewer: oh-my-claudecode:code-reviewer (model=opus)

## 结论
PASS / FAIL

## --dry-run 输出
- 8 步打印: ✓/✗
- 不改文件: ✓/✗ (证据)

## 分支完整性
- v2.1 (chapters) 分支完整: ✓/✗
- v2.2-v2.5 stub 可读不崩: ✓/✗ (抽一个 --stage v2.3 --dry-run 示例)

## STAGE_MAP 一致性
- 5 键 v2.1-v2.5: ✓/✗
- 与 executor prompt 硬编码映射一致: ✓/✗

## 幂等 + 只读
- upload_manifest 去重逻辑: ✓/✗ (具体行号或代码片段)
- _progress.completed_stages 去重: ✓/✗
- knowledge_base 只读: ✓/✗
- --dry-run gate 所有写操作: ✓/✗

## system_prompt_v2.md 修订策略
- 使用 `<!-- stage v2.X begin/end -->` 标记段替换: ✓/✗

## 关键发现 (≤ 200 字)
...

## 下一步
如 PASS: 进 Task C1 (rebuild_chapters_full.py + chapters 全展开)
如 FAIL: 列具体修复项 (给 executor 下个 attempt)
```

## 不要做
- 不修改脚本或 knowledge_base
- 不 PASS 存疑的点 (e.g. 幂等性无证据直接 PASS 是违规)
- 不输出到文件 (你无 Write 工具), 只回复纯文本

## 工作目录
`/Users/bojiangzhang/MyProject/SDTM-compare/`
