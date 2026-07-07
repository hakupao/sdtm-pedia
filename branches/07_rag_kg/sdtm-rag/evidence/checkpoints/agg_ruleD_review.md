# AGG 通道 — Rule D 全量审 (2026-07-07)

> Reviewer: 异 subagent_type (feature-dev:code-reviewer) + 最强模型, fresh context, 全 diff c42fff7..b586545 (13 commits) + spec/plan/evidence 对照。兼作 whole-branch 终审。

## Verdict: REQUEST_CHANGES → 全部整改完成 → 收口放行 (用户批准「诚实披露」口径)

## Findings 与整改

| 级别 | Finding | 整改 |
|------|---------|------|
| HIGH-1 | r3 "fresh blind" held-out 与烧毁 r1/r2 大面积收敛重叠 (4 逐字 + ~7 近逐字, 含驱动 pattern 修复的原句); 真新题仅 ~5 (5/5 fired)。"15/16 fresh" 不加限定不可入收口证据 | ① novelty-check 工具落盘 `eval/novelty_check.py` (内容词 Jaccard ≥0.6 判收敛); ② 补充轮 12 题 (writer G sonnet / H haiku, 卡片语义改写) 12/12 novel → fire 2/12 → 词汇修复后 6/12; ③ 分族口径披露进 `agg_channel_summary.md`; ④ 流程缺口记 retro |
| MED-1 | 阈值门不查数量绑定方向 ("domains contain >20 variables" 反向题触发) | accept-documented + backlog (spec §3a 原样平移; recall-additive 安全模型内; 140q clean) |
| MED-2 | 后置 "the most" 吃掉 "the most recent version" 修饰语 | accept-documented + backlog (收紧方向已记) |
| MED-3 | superlative 维度错配 ("largest number of terms" 注入 by-variables 排名) — 唯一可能致错答的类 | accept-documented + backlog **优先** (spread-noun 宾语限定 variables/domains) |
| LOW-1 | spec "and up" 后置家族未实现 | 记录 spec 偏差 (罕见措辞, 下批一并) |
| LOW-2 | 默认 ON 先于 Rule D/A 完成 (获批 plan 自带顺序) | 记录; 补测通过, 无需回翻 |
| LOW-3 | 零污染门无落盘 artifact | `evidence/checkpoints/agg_zero_pollution_probe.txt` ✓ (937f191) |
| Minor-b | Task 2 控制流三边未测 | 3 单测补齐 ✓ (937f191) |
| Minor-a/c/d/e/g | never-exceed 负向词 / run_eval 打印文案 / the-most-名词形态 / 进行时静默 / KL 已知限 | accept-documented (详 checkpoint 已知限段) |
| Minor-f | analyze excluded 无分臂归属 | drop (本次为空, 可从两 JSON 还原) |

## 反过拟合逐条 regex 判定 (核心关切)

全部 9 组 pattern 判定为**真语言形状类, 无一条按题硬编** (逐条表见审查原文, 存 session 记录)。烧毁题进单测作回归 = 已声明政策, 合规。对抗 must-not-fire 猎回: 上界表达族全部 fail closed ✓ ("at most/a maximum of/up to/capped at/stay under/cannot exceed/no more than six" 均静默)。

## 证据完整性抽核

fire 15/16 逐条核对 ✓; Δ+41.7pp 从 `agg_e2e_analysis.json` 手工重加复现 ✓; 两臂配置隔离核实 ✓ (仅 aggregate_answer flag 差异)。

## 整改后追加轮 (round 5, 1da8c4e)

Novelty 补充轮暴露 anchor 词汇缺口 (SDTM 用户说 "datasets"/"vars"): word-boundary 同义词集 `_VAR_WORD_RE`/`_DOMAIN_WORD_RE` 修复, 阈值族 novel 题 4/4 全触发; 140q 仍零污染; 剩余 6 沉默全为最高级措辞长尾 (§R5-4 造册, 未经授权不修)。**用户决策 2026-07-07: 诚实披露收口**, 长尾入 backlog, dogfood 信号决定后续。
