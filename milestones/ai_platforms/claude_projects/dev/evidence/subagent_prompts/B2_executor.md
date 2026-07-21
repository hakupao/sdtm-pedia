# B2 Executor Prompt

## 上下文
你正在执行 SDTM Phase 6.5 v2 扩容的 Task B2 (PLAN_V2.md §4)。
完整设计见 `docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md` §2.3。

## 你的任务
写 `ai_platforms/claude_projects/scripts_v2/score_domains.py`, 圈定批 2 高频域。

## 算法 (严格按此实现)
```
score = 0.4 * normalize(cross_ref_count)   # VARIABLE_INDEX.md 中该域被引用次数
      + 0.4 * normalize(examples_tokens)   # domains/<X>/examples.md 文件 token 数
      + 0.2 * (20 if domain in T_test_hits else 0)

T_test_hits = ["AE", "PC", "PP", "EX", "MH", "LB"]
normalize: 用 min-max (value - min) / (max - min), 产出 [0, 1]
```

## 输入
- `knowledge_base/VARIABLE_INDEX.md` (cross_ref 来源, 读文件, grep 每个域名出现次数)
- `knowledge_base/domains/<domain>/examples.md` (若不存在视为 0 tokens)
- 用户必选 20 域清单 (硬编码在脚本内):
  `["DM", "SE", "DS", "BS", "BE", "MI", "GF", "PR", "CM", "EX", "TU", "TR", "RS", "SS", "DD", "LB", "FA", "CE", "MH", "SU"]`
- tiktoken cl100k_base (与 v1 count_tokens.py 一致)

## 产出
- `scripts_v2/score_domains.py` (CLI: `python3 score_domains.py`)
- stdout 格式 (三段):
```
# 必选域 (用户清单 + T_test_hits, 去重)
DM: must (user)
SE: must (user)
...
AE: must (T_test_hits)
PC: must (T_test_hits)
...

# 打分排序 (除必选外, top 20)
VS: 0.78
EG: 0.75
...

# 推荐合并清单 (必选 + top N 直至总数 25-28):
[DM, SE, ..., AE, PC, PP, VS, EG, IE, QS]  # 共 <N> 域
```

## 强制要求
- P5: 只读 `knowledge_base/`, 不允许任何 Write/Edit
- 脚本幂等 (同输入同输出, 用 sorted() 确保顺序稳定)
- 用 tiktoken cl100k_base
- 必须在脚本顶部 docstring 解释 normalize 算法选择 (min-max)
- 若 examples.md 不存在, examples_tokens = 0 (不报错)

## 完成标准
1. 脚本文件存在 `scripts_v2/score_domains.py`
2. `python3 scripts_v2/score_domains.py` 跑通无错
3. stdout 含三段 (必选 / 打分 / 推荐合并)
4. 推荐合并清单总数 ∈ [25, 28]
5. 必选域包含 20 用户域 + AE/PC/PP/EX/MH/LB (去重后应该 24-26 个必选)

## 不要做
- 不要修改 knowledge_base/
- 不要写 .md 文档
- 不要解释做了什么, 只输出必要的运行结果和文件路径
- 不要引入非标准库 (只用 Python 3 stdlib + tiktoken)

## 工作目录
`/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/`

## 参考
- v1 脚本 `scripts/count_tokens.py` (同级目录, 复用 tiktoken 调用方式)
- VARIABLE_INDEX.md 格式示例: 在文件里找 "| AE |" 等 domain 列
