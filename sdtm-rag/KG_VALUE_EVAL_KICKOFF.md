# KG 价值 eval — kickoff (路由词「KG 价值 eval 开始任务」)

> 创建 2026-06-20 (SP3 收尾时立项)。**目标: 证明 SP1-3 的 KG 答题通道「真的让答案变好了」, 而不只是「注入的事实正确」。**
> 背景: SP3 的三门都是**确定性**的 (引擎 vs meta.yaml 穷举对账 + 140q 零污染 + 盲写 10 题基数对账), 但**从没用真模型测过 OFF-vs-ON 的端到端答案质量**。这是 evidence-over-assumptions 闭环缺的最后一块。

## 要回答的唯一问题
在影响/关系/聚合类问题上, **开 KG (`graph_answer_enabled` ON / `--graph-answer`) 的答案, 比不开 (只靠检索 cosine+hybrid+structured_lookup) 是否显著更准/更全?**
- 若 ON ≫ OFF → KG 价值坐实, 可继续投 SP4/SP5。
- 若 ON ≈ OFF → 事实注进 context 了但模型没用好 (可能要调答题提示/注入格式), 先别投 SP4/SP5。
- 若 ON < OFF (污染) → 不该发生 (140q 零污染已证), 若出现要查。

## 现有资产 (别重造)
- `eval/test_set_sp3_graph.yml` — 盲写 10 题图能力探针 (impact/aggregate/structural/relationship), 带 `expect_*` (meta.yaml 导真值)。**太少, 不够做 eval**。
- `eval/prod_wirein/sp3_graph_probes.py` — held-out + 140q 零污染探针 (确定性, 非 LLM)。
- `eval/run_eval.py` — 支持 `--graph-answer` / `--structured-lookup` / `--hybrid` / `--judge` / `--temperature` / `--full-answers`; 标准题集格式见 `eval/test_set_v3.yml` (含 `expected_facts` / 来源)。
- 主力模型 DeepSeek (`.env` default; ~$0.0075/题, 便宜)。

## 建议步骤 (fresh session 执行)
> 这是**验证任务**不是新功能。若题集设计/指标有不确定, 先 `superpowers:brainstorming` 问 2-3 个 (题量? 指标? 是否扩 family?); 否则直接按下面跑。

1. **盲写图能力 eval 题集 (~25-30 题, 反过拟合)** — 在 `eval/test_set_v3.yml` **同格式** (带 `expected_facts` + `expected_sources`) 新建 `eval/test_set_kg_value.yml`, 4 family: impact(codelist→域/变量 + 变量→域) / aggregate(变量跨>N域 + most_shared) / relationship(单域→相关域) / [可选 structural]。**gold 从 meta.yaml 程序导** (impacted 集合 + 基数 + 相关域); **措辞自然, 不照抄 GraphAnswerer 的 cue 词** (盲写, 防过拟合); 实体尽量用**非 SP3 测试集**的 (held-out)。题集本身可用一个 subagent 盲写 + 另一 subagent 独立核 gold vs meta.yaml (写审分离)。
2. **OFF-vs-ON 配对跑** (确定性 temp=0):
   ```bash
   # OFF arm (检索杠杆开, 但 graph 关)
   .venv/bin/python eval/run_eval.py eval/test_set_kg_value.yml \
     --model deepseek/deepseek-chat --temperature 0 --structured-lookup --hybrid \
     --judge --full-answers --output eval/prod_wirein/kgval_off.json
   # ON arm (加 --graph-answer)
   .venv/bin/python eval/run_eval.py eval/test_set_kg_value.yml \
     --model deepseek/deepseek-chat --temperature 0 --structured-lookup --hybrid --graph-answer \
     --judge --full-answers --output eval/prod_wirein/kgval_on.json
   ```
3. **配对分析** (`eval/prod_wirein/analyze_paired.py` 或新驱动): 逐题 OFF vs ON 的 fact-recall(judge), 算每 family 的 ON−OFF 提升; 列具体翻绿的题。**关键看 impact/aggregate**: OFF 没注入时模型能不能自己数对 "43 域" (大概率不能 → ON 应大幅领先)。
4. **规则 A 抽检** (独立, 非 writer): 抽 N=5-8 题人核 judge 没判松/判严 (judge 对 "列出 43 个域" 这种完整性判定容易偏); 对 meta.yaml 真值核。
5. **判定 + 归档**: 写 `evidence/checkpoints/kg_value_eval.md` (OFF/ON 数字表 + 每 family 提升 + verdict + 翻绿例); 失败/意外归 `evidence/failures/`。更新 `KG_ROADMAP.md` + memory: KG 价值 = 证实/证伪。

## 注意 / 坑
- **judge 对「穷举完整性」易判松**: 题问 "哪些域" 期望列全 43 个, 模型列 10 个 judge 可能仍判 covered。指标要区分 "基数对" (确定性可查, 接地闸已校) vs "集合列全" (judge); 建议两个都报。
- **OFF arm 不是裸检索**: 检索杠杆 (structured_lookup+hybrid) 仍开, 所以 OFF 也可能命中 VARIABLE_INDEX 等 — 这正是要测的对照 (KG 是否在检索之上再加价值)。
- 反过拟合硬纪律 (沿用): 题集盲写、gold 从 meta.yaml、实体尽量 held-out、写审分离。
- 成本: ~30题×2臂×(答+judge) DeepSeek ≈ 几毛钱; temp=0 配对。
- 这是 **Tier 2** 验证任务: PLAN-lite + evidence/checkpoints + 失败归档 + 一段 retro 即可, 不必 Tier 3 仪式。

## 产出
`eval/test_set_kg_value.yml` + 2 个 eval json + `evidence/checkpoints/kg_value_eval.md` + verdict 回填 KG_ROADMAP/PROGRESS/memory。
