# KG 价值 eval — 判定与证据 (checkpoint)

> 路由词「KG 价值 eval 开始任务」产物。立项 `KG_VALUE_EVAL_KICKOFF.md` / 计划 `KG_VALUE_EVAL_PLAN.md`。
> 日期 2026-06-21。Tier 2 验证任务。
> **唯一问题**: SP1-3 的 KG 答题通道是否真让端到端 LLM 答案变好 (不只是注入的事实正确)? → 决定 SP4/SP5 投不投。

## 实验设计 (用户批准 3 决策)

- **3 臂** (拎出 SP3 边际): `arm0` 纯检索 (structured_lookup+hybrid) / `arm1` +SP2 (structured-answer: 计数/穷举/属性/CT) / `arm2` +SP2+SP3 (再加 graph: 影响/关系/聚合 = 生产配置)。temp=0 配对。
- **3 模型**: `deepseek/deepseek-chat` (ds) + `openai/gpt-4o` (gpt4o, 跨厂商) + `openai/gpt-5.4` (gpt54, 真前沿)。judge 固定 `deepseek/deepseek-chat` (语义, per-gold-fact)。
  - 原选 Claude Sonnet 4.6 (生产默认模型) 被 Anthropic 余额卡住 → 换 gpt-4o；用户再要 gpt-5.4 加验。
- **40 题 / 4 family**: impact_codelist / impact_variable / aggregate / relationship (各 10)。**盲写** (4 写手 agent 无 graph 源访问) + **gold 程序导** (gen_kgval_goldset.py from meta.yaml) + **独立 reconcile** (raw-yaml 另一码路, 40/40 ✓) + **独立 reviewer** (Rule D, 39/40 ok + 1 rephrase)。
- **3 指标**: cardinality_correct (确定性, 答案含正确基数) / set_recall (确定性, 词边界+大小写敏感, 避 2 字母域码假阳) / judge fact-recall (语义, 主用于 most_shared)。

## Fire-rate (关键诊断: SP3 NL 触发面太窄)

盲写自然措辞下, 各通道实际触发率:

| family | SP2 fired | SP3 fired |
|--------|-----------|-----------|
| impact_codelist | 10/10 | 8/10 |
| impact_variable | 5/10 | 3/10 |
| aggregate | 4/10 | **2/10** |
| relationship | 2/10 | 5/10 |
| **ALL** | **21/40** | **18/40 (45%)** |

→ **SP3 图通道在 45% 的自然问题上根本不注入** (剩 22 题 graph 静默)。aggregate 尤其惨 (2/10): "3 or more"/"40+"/"most reused"/"most widely shared" 都不命中 SP3 那套极窄触发词 (`at least`/`more than`/`most shared`/`most common`)。**这是盲写诚实暴露的——没有为凑触发词改措辞 (反过拟合硬纪律)。**

## 结果 (judge fact-recall, 整体)

| 模型 | arm0 检索 | arm1 +SP2 | arm2 +SP2+SP3 | ΔSP2 | ΔSP3 |
|------|-----------|-----------|----------------|------|------|
| ds   | 64% | 80% | 81% | **+16pp** | +1pp |
| gpt4o| 57% | 73% | 77% | **+16pp** | +4pp |
| gpt54| 59% | 72% | (arm2 缺) | **+14pp** | n/a |

**三模型一致: SP2 大跳 ~+15pp; SP3 边际 ≈ 0。**

### Per-family ΔSP2 / ΔSP3 (ds; gpt4o 同向)

> **度量主次 (Rule A 后修正)**: 以**确定性 set_recall** (词边界, 免疫 judge 缺陷) 为主, judge 为佐证。judge 对「只报基数不列举」答案判松 (gpt4o iv01: 答"36 domains"零列举却 judge 1.0) → impact_variable 的 judge ΔSP2 虚高; set_recall 已捕获 (gpt4o impact_variable setR 90% vs judge 100%)。

| family | ΔSP2 (set_recall) | ΔSP3 (set_recall) | 说明 |
|--------|------|------|------|
| impact_codelist | **+34pp** | +0 | SP2 的 CT 穷举已答满; SP3 impact_of_codelist 输出**逐字冗余** (ic01 byte-identical) |
| impact_variable | **+14pp** (ds) / +6 (gpt4o) | +0 | SP2 穷举已覆盖 var→域 (judge +15 虚高, 见上) |
| aggregate | −1pp | **+11pp** (gpt4o +17) | **SP3 唯一正向生态位**: variables_in_min_domains / most_shared, SP2 不做 |
| relationship | +9pp (ds) | **0pp (修正后)** | judge 表面 −10pp = **rl05 假象** (该题 SP3 未触发, arm1≡arm2, 纯解码变异); 排除 rl05 或只看 SP3 真触发题 → ΔSP3=0 两模型 |

### Fire 条件下 ΔSP3 (只看图真触发的 18 题)
- ds: setR/judge arm1 90% → arm2 96% (+6pp); card 100→92 (−8, 小 N 噪)
- gpt4o: setR/judge arm1 80% → arm2 90% (+9pp)
→ **即使图触发, arm1 (SP2) 已 80-90%, SP3 边际仅 +6~9pp** (SP2 已覆盖大半)。

### SP3-unique ΔSP3 (图触发 ∧ SP2 静默 = SP3 唯一能加价值处, 6 题: iv10/ms05/rl04/rl06/rl07/rl09)
- ds: setR/judge 74% → 88% (**+13pp**)
- gpt4o: setR/judge 67% → 83% (**+17pp**)
→ **SP3 确实在 SP2 够不着的 6/40 题上独立加 +13~17pp** (relationship 发现 + aggregate 列表)。但只 6 题, 稀释到整体 ≈ 0。

### 翻绿 (cardinality 0→1)
- SP3 (arm1→arm2): ds **0 题**, gpt4o 1 题 (ag02)。
- whole-KG (arm0→arm2): ds 8 题 / gpt4o 10 题 — **全部由 SP2 翻绿**, 非 SP3。

## 机制证据 (ic01 redundancy)
同一 codelist-impact 问题, SP2 与 SP3 注入几乎逐字相同 (both: "...across 44 domains: AE, AG, CE, ...[同 44 列表]")。SP2 经 CT 通道、SP3 经 impact_of_codelist——**同数据两条路, SP3 对 impact 完全冗余**。

## Rule A 独立抽检 (N=8, critic agent 对抗式, 第三条 lane)

**裁定: ACCEPT-WITH-RESERVATIONS** (gold 可信; headline SP2 大 / SP3≈0 经所有修正后成立; 3 个 MAJOR 是数字精度/解读修正, 非方向翻转)。

- **gold 可信** ✓: 8 题 gold 两路独立 (MetaStore + raw-yaml) 逐一复现; same_class 对称一致。
- **SP2/SP3 冗余确认** ✓: ic01 两通道注入 44 域列表 byte-identical。
- **MAJOR-1 judge 判松 (iv01)**: gpt4o iv01 答"appears in exactly 36 domains"零列举却 judge 1.0 (2/240 cells, 仅 ON 臂; 对称 arm1/arm2 → **ΔSP3 不受影响**; 确定性 set_recall 免疫并已捕获)。修正: 以 set_recall 为主, impact_variable judge ΔSP2 不引用。
- **MAJOR-2 「relationship 反伤」是误判**: ds relationship judge −10pp **全部来自 rl05** (该题 `fired_sp3=False`, live resolve intents=∅, arm1/arm2 context 相同 → 1.0→0.0 是 temp=0 解码变异)。**修正后 relationship ΔSP3 = 0.000 (两模型)**; 无任何 SP3 真触发的题出现退化。**此修正强化 (非削弱) SP3≈0**。
- **MAJOR-3 rl08 gold 过度规定**: 问"same observation class as DS" 但 gold 并入 curated 的 DM (DM 是 Special-Purpose ≠ DS 的 Events 类) → 正确的纯同类答案被罚 (6/7 上限)。压低 relationship **绝对** recall, 不影响 deltas (各臂同罚)。建议: relationship gold 按问法钉定 (同类问→same_class only; 关系问→+curated), 同 aggregate 阈值钉定模式。
- **Minor**: rl02 把结构同类算作"link" (语义宽窄之争, 留 author 定义); count≠facts 数 6 题 harmless (card_applies=False); 小基数 cardinality 弱信号 (靠 ΔON-OFF 抵消)。
- **缺口**: 无第二 judge / 自洽校验 (单 judge=deepseek 与 ds 答题臂同族); 无 n>1 方差控制 (rl05 显示 temp=0 仍有 1.0↔0.0 重写摆动); gpt54 仅 2 臂。
- **judge 净评**: OFF 臂偏严 (合理, 拒绝 hedge "may also use X" → 轻微抬高 ΔSP2), 仅 iv01 一处判松。确定性指标为主即稳。

## 判定 (verdict) — Rule A 终确 (ACCEPT-WITH-RESERVATIONS)

> 以确定性 set_recall (免疫 judge 缺陷) 为主; 3 模型, ds+gpt4o 完整 3-臂, gpt54 确认 SP2。

1. **KG 答题通道整体 vs 纯检索: 大赢** (set_recall +13~14pp / judge +14~16pp), **价值几乎全来自 SP2** (确定性计数/穷举/CT), 已生产默认 ON。三模型一致 (ds/gpt4o/gpt54 arm0→arm1 全 +14~16pp judge)。
2. **SP3 (图层) 端到端边际 ≈ 0** (set_recall +2~4pp)。唯一稳定正向 = **aggregate 聚合** (variables_in_min_domains / most_shared, SP2 不做, set_recall +11~17pp) + 6 题 SP3-unique (+13~17pp); 被三因素稀释到整体 ≈0: (a) NL 触发率 **45%**, (b) impact 上与 SP2 **byte-identical 冗余**, (c) relationship 上 **ΔSP3=0** (原 −10pp 经 Rule A 证实为 rl05 非触发解码变异, 非 SP3 退化)。SP3 翻绿题: ds 0 / gpt4o 1 (ag02)。
3. **对 SP4/SP5 的含义 (核心交付)**: **图层不足以靠答案质量证明继续投资 SP4/SP5**。SP4 (Neo4j/可视化) / SP5 (图校验器) 只在「要交互式图浏览 UX 作产品功能」时才值得 — **不是精度/答案质量决策**。若要榨取 SP3 已有价值, 性价比最高的不是 SP4/SP5, 而是: ① 拓宽 SP3 的 NL 触发面 (45%→更高, 当前最大瓶颈) ② 把 aggregate 聚合能力并入 SP2 通道 (SP3 唯一独有价值, 可低成本迁移)。
4. **诚实更正**: 初版「SP3 注入反伤 relationship」结论**被 Rule A 推翻** — 那是 rl05 (SP3 未触发) 单题解码变异, 非因果。修正后 SP3 在任何真触发的题上**不退化**。此更正反而**坐实 SP3≈0**。

## 限制 / 诚实缺口

- **gpt54 arm2 未采集**: OpenAI 配额在 arm2 中途耗尽 (见 `failures/`)。ΔSP3 由 ds+gpt4o 两个完整 3-臂模型确认; gpt54 仅确认 SP2 (arm0/arm1)。
- **aggregate small-N**: 每 family 10 题, aggregate 内含 5 阈值+5 most-shared, per-family delta 有噪; cardinality 小基数 (2-5) 有巧合命中 (ΔON-OFF 抵消)。
- **judge 用 deepseek (与 ds 答题臂同族)**: 自评偏松风险 → 确定性指标 (card/set_recall) 为主, Rule A 核 judge。
- **relationship gold = same_class ∪ curated**: 与「好的关系答案应说什么」未必一致 → Rule A 裁决伤害真伪。

## 产物清单
`eval/test_set_kg_value.yml` · `gen_kgval_goldset.py` · `reconcile_kgval_gold.py` · `assemble_kgval_testset.py` · `prod_wirein/kgval_fire_probe.py` · `prod_wirein/analyze_kgval.py` · `prod_wirein/kgval_{arm0,arm1,arm2}_{ds,gpt4o}.json` + `kgval_{arm0,arm1}_gpt54.json` · `prod_wirein/kgval_analysis.json` · `kgval_authored_*.json` + `kgval_review.json`。
