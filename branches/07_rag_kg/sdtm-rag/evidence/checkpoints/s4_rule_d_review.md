# S4 三修 Rule D 独立代码审查记录

> 审查者: `oh-my-claudecode:code-reviewer` (异 subagent_type; writer=main session)
> 日期: 2026-06-12 | 对象: `server/structured_lookup.py` 三修 + `scripts/tests/test_structured_lookup.py` (新)
> 审查者独立动作: 复跑 pytest 235 全过 / `git stash` 对照存量行为 / grep logic 验证零 eval 题面 token / KB 长名清单实查 (5 斜杠名 + 2 短词名) / 合成边界探针 (多斜杠 token、空备选、确定性构建)

## Verdict: **APPROVE_WITH_NITS** (0 CRITICAL / 0 HIGH / 2 MED / 4 LOW)

## Findings 与处置

| # | 级别 | 内容 | 处置 |
|---|------|------|------|
| 1 | MED | 变体循环一次只解一个斜杠 token; 未来 KB 出现双斜杠名会静默注册半解析变体 (现 KB 0 例, latent) | ✅ 已采纳: 测试加多斜杠守卫断言, 未来 fail loudly |
| 2 | MED | "datasets" 同义词使部分单域题被前置注入 VARIABLE_INDEX (union-add 只增不删, 零回归 gate 实测 0 伤害; 残余风险=top-15 尾部稀释) | ✅ 已采纳: 加 var+datasets+verb 单域题保序探针 (`test_datasets_synonym_is_recall_additive`) |
| 3 | LOW | **存量**: "Procedures"(10)/"Disposition"(11) 过 ≥10 阈值裸匹配, 泛义散文误注入 PR/DS — git stash 确认本修未引入未恶化 | 记录为 known boundary (s4 result §known boundaries); 不反应式修 |
| 4 | LOW | re.escape 时序 (变体组装后 escape) 正确; `\s+` 锚与 split 归一一致 — 检查过, 无需修 | 无动作 |
| 5 | LOW | 排序键 pattern 串长→长名长度是正确修复 (锚定后缀会污染串长); 等长平局按 dict 插入序, 确定性但未显式 | 记录; 可选二级排序键留待后续 |
| 6 | LOW | 环境无 ty/mypy, 以 py_compile + 236 pytest 兜底 | 基建注记, 非缺陷 |

## 反过拟合确认 (审查原文要点)

- "Genuinely pattern-level, not example-tuned" — logic 中 grep `q1xx`/`Cumulative`/`ARMCD`/
  `VISITNUM`/`SITEID` 仅命中注释 (解释泛化依据), 零命中逻辑。
- 修 (b) 通用变换自动覆盖 IE/TI/TU/TR 共 5 斜杠名 10 变体, 非只修动机题 CM。
- 修 (c) 锚定 pattern 实测: "Exposure data set"(有空格)/"exposuredomain"(无边界)/
  q96 "Cumulative Exposure)" 全不 fire; 排除 "data" 锚是对的 ("the Comments data" 不 fire)。
- 测试质量: 集外泛化探针 + 负例/撞车例 + 独立重推导的 map 卫生不变量 — "non-tautological"。
- 保守性保持: no-intent → `[]`, union-add 不删 cosine 命中, `_MAX_DOMAIN_SPECS=3` cap 不变, OFF 臂构造上不受影响。

## 采纳后复验

2 MED 测试加固落地后全量 pytest **236 passed**。
