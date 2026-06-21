# KG 价值 eval — PLAN-lite (Tier 2)

> 立项 kickoff: `KG_VALUE_EVAL_KICKOFF.md`。本文件 = 执行计划 (用户 2026-06-21 批准 3 决策后定稿)。
> 唯一问题: **SP1-3 的 KG 答题通道是否真让端到端 LLM 答案变好** (不只是「注入的事实正确」)。
> 结果决定 SP4 (Neo4j/可视化) / SP5 (图校验器) 值不值得投。

## 用户批准的 3 决策 (2026-06-21)

1. **3 臂对照** (拎出 SP3 边际价值):
   - **Arm0 (retrieval)**: `--structured-lookup --hybrid` — 纯检索杠杆, 无答题通道注入
   - **Arm1 (+SP2)**: `+ --structured-answer` — 计数/穷举/属性/CT 确定性答题通道
   - **Arm2 (+SP2+SP3 = 生产)**: `+ --graph-answer` — 再加图 (影响/关系/聚合)
   - **关键 delta**: Arm2−Arm1 = **SP3 边际价值** (gate SP4/SP5); Arm1−Arm0 = SP2 价值; Arm2−Arm0 = 整条 KG 通道 headline
   - 注: kickoff 原 bash 的 ON 漏了 `--structured-answer` (非生产配置, 且混淆 SP2/SP3) → 已纠正为 3 臂
2. **2 模型**: `deepseek/deepseek-chat` (便宜默认) + `anthropic/claude-sonnet-4-6` (前沿稳健性); judge 固定 `deepseek/deepseek-chat` 跨 6 次运行一致 (temp=0)
3. **~40 题**: 4 family × 10

## Family 设计 (映射已接 NL 意图 + 覆盖 SP2→SP3 谱)

| family | 问法 | gold 来源 (meta.yaml/MetaStore/GraphEngine) | SP2/SP3 归属 |
|--------|------|---------------------------------------------|--------------|
| `impact_codelist` (10) | codelist C 码改动→影响哪些域/变量 | `domains_for_codelist` / `variables_for_codelist` | **SP3 only** (SP2 不做 codelist→域) |
| `impact_variable` (10) | 变量出现在多少/哪些域 | `domains_for_variable` | SP2/SP3 重叠 (穷举) |
| `aggregate` (10) | 跨 ≥N 域的变量 / 最常共享 codelist | `variables_in_min_domains` / `most_shared_codelists` | SP2(计数)+SP3(聚合) |
| `relationship` (10) | 域→同类域 + 策划相关域 | `same_class` / `relations_curated` | **SP3 only** |

预期 per-family 模式 (若 SP3 有价值): Arm2−Arm1 提升集中在 `impact_codelist` + `relationship`; `impact_variable`/`aggregate` 多在 Arm1(SP2) 已翻绿。

## 反过拟合硬纪律 (沿用 + 强化)

- **盲写**: 自然措辞, **绝不**为匹配 GraphAnswerer 触发词 (`affect/related to/at least/most shared`...) 调措辞 = 作弊。写手 agent 禁读 `server/graph_answer.py` / `graph_engine.py`。
- **gold 程序导**: 实体由 `eval/gen_kgval_goldset.py` 从 MetaStore/GraphEngine 选 + 算真值; **独立 reviewer 用 raw yaml 另一码路重算** (SP1 reconcile 模式, 防 MetaStore bug 与注入同源共错)。
- **held-out 实体**: 排除 SP3 测试集 + 140q 用过的 (C66742/C66728/TAETORD/EPOCH/AE/CM/AESER/AGE/DM...)。
- **写审分离 (Rule D)**: 写手 subagent ≠ reviewer subagent ≠ Rule A 抽检 scientist, 三个不同 lane。

## 指标 (3 个, 确定性优先)

1. **cardinality-correct** (确定性, PRIMARY): 答案是否含正确基数 (如 codelist→「12 域」)。OFF 臂无注入基本不可能数对 → 最锐 KG 信号。
2. **set-recall** (确定性子串, PRIMARY): gold 项 (域码/变量名) 作 token 出现于答案的比例 = 穷举完整性, 不靠 judge。
3. **judge fact-recall** (语义, SECONDARY): run_eval `--judge`, 容错释义; 标注「穷举完整性 judge 易判松」。

## Fire-rate 仪表 (kickoff 没写, 关键)

离线对每题跑 `StructuredAnswerer.resolve()` + `GraphAnswerer.resolve()` → 记录每题 SP2/SP3 是否 fire。分析两层:
- **边际** (全部题): 用户实际得到的端到端值
- **fire 条件下** (只看图真触发的题) Arm2−Arm1: 区分三态 —
  - fire 高 & fired-delta 大 → SP3 solid → 投 SP4/SP5
  - fired-delta 大但边际小 (fire 低) → SP3 能用但 NL recall 太窄 → 先修路由再投
  - fired-delta ≈ 0 → 注入了模型没用 → 注入格式问题

## 执行步骤

1. `eval/gen_kgval_goldset.py` (我写, 确定性): 选 held-out 实体/family + 算 gold → `eval/kgval_candidates.json`
2. **Workflow** 盲写+独审: 4 写手 (per family, blind) 出自然题 → 独立 reviewer (raw yaml 重算 gold + 审措辞 cue-leak/naturalness/held-out)
3. 组装 `eval/test_set_kg_value.yml` (写手题 + 脚本 gold, reviewer 过后)
4. `eval/prod_wirein/kgval_fire_probe.py`: 每题 fire 标注
5. 跑 6 臂 (3×2, background, temp=0, --judge --full-answers): `eval/prod_wirein/kgval_{arm0,arm1,arm2}_{ds,sonnet}.json`
6. `eval/prod_wirein/analyze_kgval.py`: per-family per-arm 3 指标 + deltas + fire 条件分析 + 翻绿例表
7. **Rule A 抽检** (scientist, N=8, 独立): 核 gold vs meta.yaml + judge 判松/判严 + cardinality 正确
8. 判定 + 归档: `evidence/checkpoints/kg_value_eval.md` (数字表+per-family delta+verdict+翻绿例); 意外→`evidence/failures/`; 回填 `KG_ROADMAP`/`PROGRESS`/memory; 一段 retro
9. 收尾 commit

## 产出

`eval/test_set_kg_value.yml` + `gen_kgval_goldset.py` + `kgval_fire_probe.py` + `analyze_kgval.py` + 6 eval json + `evidence/checkpoints/kg_value_eval.md` + verdict 回填三处。

## 成本

~40 题 × 3 臂 × 2 模型 × (答+judge) ≈ DeepSeek 几毛 + Sonnet 几块; temp=0 配对确定性。
