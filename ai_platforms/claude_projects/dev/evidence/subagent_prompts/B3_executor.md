# B3 Executor Prompt

## 上下文
你正在执行 SDTM Phase 6.5 v2 扩容的 Task B3 (PLAN_V2.md §4 / design doc §2.5).

## 你的任务
写 `ai_platforms/claude_projects/scripts_v2/score_codelists.py`, 圈定批 4 (top 200) 和批 5 (200-500 名) 的 codelist.

## 算法 (严格按此实现)
```
score = 0.5 * normalize(domain_ref_count)  # 被多少 domain spec.md 引用
      + 0.3 * sigmoid_term(term_count)     # codelist 内 Term 数 (中等最优)
      + 0.2 * (50 if codelist_name in T_codelist_hits else 0)

T_codelist_hits = ["NY", "AERELN", "FREQ", "PROBLEM_TYPE"]
(NY 对应 C66742; 只匹配 codelist_name 字符串)

normalize: min-max, [0, 1]

sigmoid_term: 用于给中等 Term 数的 codelist 最高分 (太小 < 3 几乎无信息, 太大 > 500 难以展开)
公式: sigmoid 中心在 30, 衰减: 两端低、中间高.
简化实现:
  f(n) = 1 / (1 + abs(log10(n + 1) - log10(30))) if n > 0 else 0
  返回值 [0, 1], 30 项附近最高, 1 或 1000 项时衰减.
```

## 输入
- `knowledge_base/terminology/` 目录 (三子目录: `core/`, `questionnaires/`, `supplementary/`)
- 每个 .md 文件可含多个 codelist, 每个以 `## ` 标题开始
- codelist 提取规则: 从每个 .md 文件中用正则 `^## ([A-Z][A-Z0-9_]+)` 提取 codelist 名 (如 `NY`, `AERELN`, `FREQ`)
- Term 数统计: 每个 codelist 段内匹配形如 `| C?\d+ \|` 的表格行 (或其他一致方法: 统计 codelist 段内 markdown table body 行数)
- domain_ref_count: grep `knowledge_base/domains/*/spec.md` 中该 codelist name 出现次数总和

## 产出
- `scripts_v2/score_codelists.py` (CLI: `python3 score_codelists.py` from 仓库根)
- stdout 三段:
```
# 批 4 top 200 (按 score 降序)
NY: 0.95
AERELN: 0.88
...
(200 行)

# 批 5 rank 201-500 (按 score 降序)
XXX: 0.52
YYY: 0.51
...
(300 行)

# 统计
Total codelists: ~1005
Top 200 coverage: N_codelists, 估 M_tokens (基于 Term 数 × 30 tokens/term 估算)
Rank 201-500 coverage: N2_codelists, 估 M2_tokens
```

## 强制要求
- P5 只读 knowledge_base/
- 幂等 (sorted stable)
- tiktoken 不强制 (因只是估算, 可简化为 `term_count * 30`)
- 脚本顶部 docstring 解释 sigmoid_term 选择

## 完成标准
1. 脚本跑通无错
2. stdout 含三段 (top 200 + 201-500 + 统计)
3. 统计 total ≈ 1005 (±5%)
4. T_codelist_hits 4 个应出现在 top 200 (因加分 10.0 显著)

## 不要做
- 不要修改 knowledge_base/
- 不要写 .md 文档
- 不要引入非标准库 (Python 3 stdlib 即可)

## 工作目录
`/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/`

## 参考
- v1 `scripts/count_tokens.py` (tiktoken 用法, 若需要)
- `scripts_v2/score_domains.py` (同类脚本, 可参考结构)
- terminology 文件示例: 先 Read `knowledge_base/terminology/core/general.md` 头 200 行了解格式
