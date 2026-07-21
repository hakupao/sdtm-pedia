# AGG 通道 — 五门验收 checkpoint (2026-07-07)

> Spec `docs/superpowers/specs/2026-07-07-aggregate-answer-widening-design.md` / Plan `docs/superpowers/plans/2026-07-07-agg-aggregate-answer-channel.md`。
> aggregate 能力从 SP3 graph_answer 拆出独立 `AggregateAnswerer` 通道 + pattern-level 触发重写; **默认 ON** (`aggregate_answer_enabled`, env 可回滚)。
> 收口口径: **用户批准「诚实披露」(2026-07-07)** — 形式门全过 + 泛化率分族如实披露, 最高级长尾入 backlog。

## 五门结果

| 门 | 结果 |
|----|------|
| 1 单测电池 | **PASS** — 48 测试 (must-fire 9 形状类 / must-not-fire 上界·版本号·散文·跨从句·量化dozen·词形近似 / golden 逐字等价 / 控制流三边); 全套 460/460 |
| 2 140q 零污染 | **PASS 0/140** — GA+AGG 双通道, 每轮 pattern 扩展后重跑 (5 轮全 ALL PASS); artifact `agg_zero_pollution_probe.txt` |
| 3 fire-rate | **形式 PASS + 诚实披露** (见下节) — r3 门 15/16 ≥13; Rule D 揭示盲写收敛重叠 → novelty-check 补充轮: 阈值族 novel 4/4=100%, 最高级族 2/8=25%, 合计 6/12 |
| 4 ds 端到端 | **PASS** — held-out set_recall OFF 58.3% → ON **100%** (Δ**+41.7pp** ≥ +10pp); 回归 45.9%→100% (Δ+54.1pp); 26 题**零退化**; 审查者独立复算逐数吻合 |
| 5 质量 | **PASS** — ruff/mypy clean; Rule D REQUEST_CHANGES→整改完成 (`agg_ruleD_review.md`); Rule A N=6 AUDIT_PASS 零错配 (`agg_ruleA_audit.md`) |

## Fire-rate 诚实披露 (Rule D HIGH-1)

- **盲写收敛现象**: 同一 need card 跨轮盲写会收敛到相似措辞 — r3 与烧毁 r1/r2 有 4 条逐字 + ~7 条近逐字重叠 (含驱动修复的原句), r3 的 15/16 高估独立泛化。
- **修正口径 (novelty-check ≥0.6 Jaccard, 工具 `eval/novelty_check.py`)**: 真 novel 补充集 12 题 → 词汇修复后 **6/12**; 分族: **阈值族 4/4 (100%)**, **最高级族 2/8 (25%)**。
- **对比基线**: kgval 时代 SP3 aggregate 触发 2/10 (20%); 现 kgval 回归 10/10, r1/r2/r3 集各 15/16。
- **安全模型**: 不触发 = 与无通道等价 (纯检索回答), **永不致害**; 触发 = 注入可对账真事实。
- 修复史 (全部 shape-level, Rule D 逐条判定无按题硬编): r1 4/16 → 6 形状类 (0866b66) → 收紧 2 轮 (d37d86e/2468c4f) → r2 12/16 → +N-plus/top-N (4b8bf6e) → r3 15/16 门过 (40aeb9b) → anchor 同义词 datasets/vars (1da8c4e)。失败归档 `evidence/failures/agg_attempt_{1,2}.md`。

## 已知限 (silent 侧, 只丢 recall 不注错)

KL-1 双插入 ("as many as six separate domains, or even more") · KL-2 隐喻最高级 ("the clear champion") · KL-3 "most often" 无 "the" · KL-4 最高级长尾造册 (§R5-4: 多词间隔比较级 / "widest reach" 无 spread-noun / adopted·recycled 前置分词 / "top ones") — **等 dogfood 真实信号决定是否再投** (⚑ 按钮 backlog)。

## Backlog (注入侧, accept-documented)

MED-3 (优先): superlative 维度错配 ("largest number of terms" 注入 by-variables 排名, 可能误导) → spread-noun 宾语限定 variables/domains; MED-1 数量绑定方向; MED-2 "the most recent" 修饰语; LOW-1 "and up"。

## 流程改进 (入 retro)

盲写 fire-rate 门必须带 **novelty check** (本单元方法论缺口, Rule D 抓出); 工具已沉淀 `eval/novelty_check.py`, 下次盲写门直接复用。

## 产物清单

代码: `server/aggregate_answer.py` (新) + `graph_answer.py`(删 aggregate 回归纯图)/`config.py`/`main.py`/`run_eval.py`(改)。测试: `scripts/tests/test_aggregate_answer.py` (48) + `test_graph_answer.py` 迁移。评测: `test_set_agg_heldout{,_burned_r1,_burned_r2}.yml` + `test_set_agg_supplement.yml` + `test_set_agg_e2e.yml` + `gen_agg_heldout.py` + `novelty_check.py` + `prod_wirein/{agg_fire_probe,analyze_agg_e2e}.py` + `agg_e2e_{off,on}.json`。证据: 本文件 + `agg_rule{D,A}_*.md` + `agg_zero_pollution_probe.txt` + `failures/agg_attempt_{1,2}.md`。
