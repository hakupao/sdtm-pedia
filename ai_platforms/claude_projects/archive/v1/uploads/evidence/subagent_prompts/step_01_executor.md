# Step 1 executor Prompt
> 调用时间: 2026-04-17 11:15
> Agent: oh-my-claudecode:executor
> Model: opus

## Description
Write count_tokens.py tiktoken utility

## Prompt

## 上下文
你正在执行 SDTM Phase 6.5 Claude Project 压缩部署的 Step 1。
完整计划见 `ai_platforms/claude_projects/PLAN.md` §7.4 Step 1。
本 Step 是基础工具，后续 Step 2-12 全部依赖本脚本测 token。

## 你的输入
- 无源文件（纯工具脚本）
- 依赖库: `tiktoken`（若未安装，脚本顶部用 `import tiktoken` 即可，系统已装）
- 编码: `cl100k_base`（与 GPT-4 / Claude 近似，与 PLAN §附录 A 实测 2,527,153 tokens 一致）

## 你的产出
1. 写脚本: `ai_platforms/claude_projects/scripts/count_tokens.py`
2. 功能:
   - CLI: `python count_tokens.py <path>`
   - `<path>` 若是文件 → 输出 `<file>: <N> tokens`
   - `<path>` 若是目录 → 递归统计所有 `.md` 文件，输出每个文件一行 + 最后一行 `TOTAL: <N> tokens`
   - 使用 `tiktoken.get_encoding("cl100k_base")`
   - 支持 `--total-only` 仅打印总数
   - 支持多路径: `python count_tokens.py file1.md file2.md`（合并统计）
3. 放在 `ai_platforms/claude_projects/scripts/` 下
4. 脚本必须幂等、只读源文件、无副作用

## 验证（你必须自测后再返回）
cd 到 `/Users/bojiangzhang/MyProject/SDTM-compare` 然后跑:

```
python3 ai_platforms/claude_projects/scripts/count_tokens.py knowledge_base/ROUTING.md
```

**预期输出包含**: `2657 tokens`（这是 PLAN.md §附录 A 的实测值，与之偏差须 ≤1%）

再跑一次，确认幂等:
```
python3 ai_platforms/claude_projects/scripts/count_tokens.py knowledge_base/INDEX.md
```
**预期**: `5032 tokens`（PLAN 附录 A 值）

## 强制要求
- 源文件只读 (P5)，不修改 knowledge_base/ 任何文件
- 脚本第一行加 shebang `#!/usr/bin/env python3`
- 脚本顶部加简短 module docstring 说明用途
- 不要写 README 或 Markdown 说明文档
- 不要解释你做了什么，只报告结果

## 完成标准
在最终消息中打印一行确认：
`[Step 1 DONE] scripts/count_tokens.py: ROUTING.md=<实测数> tokens, INDEX.md=<实测数> tokens`

并报告：
1. 脚本行数
2. 若实测与 PLAN 附录 A 偏差 >1%，明确说明

## 不要做
- 不要修改 knowledge_base/ 任何文件
- 不要创建 output/ 下任何文件（本 Step 不产出内容文件）
- 不要修改 PLAN.md / _progress.json / trace.jsonl（主控负责）
- 不要写使用说明文档（docstring 足够）

## Subagent 返回结论
（返回后由主控粘贴）
