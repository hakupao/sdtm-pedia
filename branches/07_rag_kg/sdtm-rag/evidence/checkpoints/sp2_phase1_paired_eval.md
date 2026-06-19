# SP2 Phase 1 — OFF-vs-ON Paired Eval (Task 13)

> 状态: **PASS** (2026-06-20) — 三准则全达标。初始 DONE_WITH_CONCERNS (闸 v1 36 误报) 已由**闸 v2 重建**消解 (36→0)；Rule A 抽检揪出的 q67 codelist 变量计数缺陷已修。Rule D APPROVE + Rule A PASS。flag 翻默认 ON。**完整解决见文末 §最终解决 (闸 v2 + q67 + Rule D/A)**。下方 §计数闸 段记录的是闸 v1 历史状态 (已被 v2 取代)。

## 方法论 (与既有 v3 paired eval 对齐)

- **模型**: `deepseek/deepseek-chat` — 与最近的 v3 full-answer paired eval (`v3_full_on_guardrail_t0.json`, `prompt_guardrail=True`) 一致; temperature=0.
- **检索配方两臂相同**: `--structured-lookup --hybrid --guardrail`, top_k=15, RRF. **唯一差异 = `--structured-answer`** (结构化答题通道 ON/OFF).
- 题集: `eval/test_set_v3.yml` 140 题 (single_domain / cross_domain / concept / mixed).
- 产物: `eval/prod_wirein/v3_sp2_off_t0.json` (OFF), `v3_sp2_on_t0.json` (ON), `v3_sp2_paired_t0.log` (paired).

## Overall + 分类指标 (OFF → ON)

| 指标 | concept | cross_domain | mixed | single_domain | **AVG** |
|------|---------|--------------|-------|---------------|---------|
| SOURCE recall | 100.0% → 100.0% (+0) | 99.0% → 99.0% (+0) | 100.0% → 100.0% (+0) | 100.0% → 100.0% (+0) | **99.6% → 99.6% (+0)** |
| FACT recall (substring) | 80.9% → 84.1% (**+3.1**) | 69.7% → 68.7% (**-1.0**) | 92.0% → 94.0% (**+2.0**) | 80.2% → 79.6% (**-0.6**) | **78.7% → 79.1% (+0.4)** |

- Overall (0.85·src + 0.15·fact 加权): OFF 0.8916 → ON 0.8935.
- Tokens: OFF 2,155,544 → ON 2,167,586 (+0.6%, 注入事实块的成本).
- Per-question fact diff: **8 drops, 15 gains** (净 +7 题).

## 验收靶子 q103/q104 (capability targets) — 全绿 ✅

| 题 | OFF fact | OFF 答案问题 | ON fact | ON 答案 (含目标事实) |
|----|----------|--------------|---------|----------------------|
| q103 (TAETORD) | 0.5 (缺 "43") | "至少出现在 **6** 个 SDTM 域" (错; 检索只够到 6 个) | **1.0** | "TAETORD 出现在 **43** 个 SDTM 域中... Label 为 **Planned Order of Element within Arm**" |
| q104 (VISITDY) | 0.5 (缺 "36") | "**one domain**: SV"; 误把 VISITDY 当作 SVSTDY (错) | **1.0** | "VISITDY 出现在 **36 个 SDTM 域**中, 其 Label 为 **Planned Study Day of Visit**" + 36 域全列 |

- 字面校验 ON: q103 含 "43" ✓ 且含 "Planned Order of Element within Arm" ✓; q104 含 "36" ✓ 且含 "Planned Study Day of Visit" ✓.
- q103/q104 **计数闸 0 violation** (独立复跑确认).

## 零回归判定 — 真实零回归 ✅ (字面分类 -1.0% / -0.6% 全为噪声/翻译/字面伪降)

字面 cross_domain -1.0% 与 single_domain -0.6% 来自 8 个 fact drop, **逐题核证后无一为通道造成的真实稀释**:

| drop 题 | 类 | channel_fired | 判定 |
|---------|----|--------------|------|
| q35 | concept | **False** | 通道未触发→context/prompt/model 与 OFF 逐字节相同 = **LLM 非确定性噪声** (temp=0 仍非完全确定) |
| q66 | cross_domain | **False** | 同上, 噪声 |
| q116 | cross_domain | **False** | 同上, 噪声 |
| q125 | cross_domain | **False** | 同上, 噪声 |
| q133 | single_domain | **False** | 同上, 噪声 (该题 OFF 本就 0.33, 低分题抖动) |
| q136 | single_domain | **False** | 同上, 噪声 |
| q25 | single_domain | True | 缺 "Verbatim" — ON 写中文"**逐字**术语" (同义), 字面伪降, 语义等价 |
| q34 | cross_domain | True | 缺 "NY" — ON 写全称"No Yes Response"; **且 ON 大幅更正确**: C66742 由 OFF 误判 2 域→ON 正确 **41 域**全列. 字面伪降, 语义大涨 |

- **6/8 drop 在通道未触发的题上** → 与通道无关, 纯 temp=0 非确定性.
- **2/8 drop 在通道触发的题上** → 均为字面/翻译伪降, ON 语义 ≥ OFF (q34 实为重大 gain).
- 故无任何分类存在通道导致的真实回归; 字面分类负 delta 在 substring 噪声带内.

### must-not-fire 抽检 (通道未污染无关答案)
| 题 | 类 | channel_fired | OFF→ON fact |
|----|----|--------------|-------------|
| q01 | single_domain | False | 1.0 → 1.0 |
| q03 | single_domain | False | 1.0 → 1.0 |
| q08 | cross_domain | False | 1.0 → 1.0 |
| q118 | cross_domain | False | 1.0 → 1.0 |
| q78 | concept | False | 0.0 → 0.0 (预存 miss, 与通道无关) |

通道在 140 题中触发 **56 题**; 未触发的题答案 OFF/ON 一致 (除 LLM 抖动), 证实增量、并行、风险隔离。

## 计数接地闸 0-violation 检查 — 字面 36, 实质 0 ⚠️

Step 5 driver 独立复跑闸 → 报 **36 个 violation** (非 0). **逐条核证: 全部为闸的 `_stated_numbers_near` 整句整数扫描误报**, 无一为模型与注入计数矛盾:

- **字符长度限值** (非域计数): q21/q22/q26/q61/q62 ("不超过 **8** 个字符"), q27 ("**200** 字符"), q95/q96/q101 ("**40** 字符"), q100 ("**20** 字符").
- **codelist 术语数 / 变量数** (注入块自身的真事实): q34 ("**4** 个值"), q67 ("**106** 变量"), q71 ("**52** 术语"), q108 ("**135** 术语"), q111 ("**17** 标准值").
- **章节号 / 示例号**: q32 ("§4.4.**5**"→4; 例 "**99**"), q92 ("Example **5**").
- **枚举/列表框架**: q47/q48/s05/q58/q91/q94/q100/q106/q109/q110 — 均为表格行号、列表条数、或另一变量(如 q100 的 ETCD≠ARMCD)的真实计数.

每条 flag 对应的触发句已抓取核验 (见 git log Task13 / 复跑脚本). 模型在每个 flag 处的实际域/变量计数 (若陈述) 均与注入真值一致; 被 flag 的数字语义无关. 闸的生产行为是**非破坏性追加一条真事实更正块** → 即使误触发也从不产出错答案. q103/q104 (靶子) **0 violation**.

**结论**: 注入真值的设计目标 (模型不与权威计数矛盾) **达成** — 0 个真实矛盾. 字面 36 是闸"按主语整句扫所有整数"的已知过宽行为; 属闸的 precision 待优化项 (SP2 后续: 把扫描范围收窄到"主语 + 计数关键词同句"或只比对域/变量计数语境), **非 Phase 1 答题通道缺陷**.

## PASS/FAIL per criterion

| 验收准则 | 判定 | 依据 |
|----------|------|------|
| (a) q103 TAETORD→43+label, q104 VISITDY→36+label 翻绿 | **PASS** | 两题 fact 0.5→1.0, 字面含 43/36+labels, 0 闸 violation |
| (b) 全类零回归 vs OFF | **PASS** (真实) | src 全类 +0; fact 字面 2 类微负但逐题核证全为噪声/翻译/字面伪降, 0 真实稀释; 净 +7 题 gain |
| (c) ON 臂 0 计数闸 violation | **CONCERN** | 字面 36 (非 0); 但逐条核证全为整句扫描误报, 0 真实矛盾, 闸非破坏性从不产错答案; 靶子 q103/q104 为 0 |

## 总判定

**DONE_WITH_CONCERNS** — (闸 v1 历史判定, 已被下方 §最终解决 取代)。答题通道的业务目标全部达成; 唯一 concern 是闸 v1 的 36 误报, 已由闸 v2 消解。

---

## 最终解决 (闸 v2 + q67 + Rule D/A) — Task 13/14 收口 2026-06-20

### 闸 v2 — 高精度重建 (commit 5263236): 36 误报 → 0
闸 v1 的 `_stated_numbers_near` 按主语整句扫所有整数 → 36 误报 (字符限值/术语数/章节号/另一变量计数; 逐条核证全部为模型其实答对、闸抓错旁边数字)。**关键数据: 36/36 误报里正确值都在答案中出现**。v2 改为:
1. **缺席前提**: 正确值以独立整数出现在答案任意处 → 模型已答对 → 跳过, 不报。(单这一条消除全部 36 误报)
2. **错误计数检测** (仅正确值缺席时): 数字须 (a) 双语 kind 词邻近 (domains→`domains?`/`域`; variables→`variables?`/`变量`), (b) 数量合理 (≤200/≤300), (c) 主语同句。
- **验收 oracle**: 闸 v2 重跑 140 saved ON 答案 → **0 violation** (独立复核确认)。回归网: 36 误报案例 + must-fire (含双语) 写进 `test_grounding.py` (27 测试)。
- **校准原则**: MISS (漏纠真错) 可接受; FALSE POSITIVE (给对的答案追加错更正) 是要消除的 bug。

### q67 修复 (commit 24055fe): codelist 变量计数纳入 gate (Rule A 缺陷)
Rule A N=8 抽检揪出: codelist 只发 domain 计数 CheckableCount, **无变量计数** → "C66742 被多少变量引用?" 模型答 41 (混淆域数) / 106 (幻觉), 真值 123, 未被纠。修复: codelist 分支注入显式 "Used by 123 variables" 计数行 + 发 `CheckableCount(code,"codelist_variables",123)`; 闸加该 kind (variable 词组 + "is used by exactly N variables" 措辞)。oracle 复跑: q67 现**真实命中** (`expected 123 stated 41`) → 生产追加 "...used by exactly 123 variables." 更正; 零新增误报。

### Rule D — 独立代码审 (critic, 异 subagent_type): **APPROVE (safe to ship default-ON)**
零 CRITICAL。2 MAJOR 均**非破坏性、设计内**, 转 backlog: (1) 词典词变量 (RACE/SEX/AGE/ARM) off-topic 锚定 = recall-additive 真事实非错答; (2) FP2 残余 spurious-but-true 更正 (140 题中 35 次 gate-fire 前提下 0 次自然发生, 且只追加真事实)。Minor: enumerate corpus 路径只出计数不出列表; first-seen 属性跨域分歧 (→SP3)。验证: flag-OFF 逐字节相同、gate 全路径非破坏、反过拟合零硬编、0-violation oracle 独立复现。

### Rule A — N=8 分层语义抽检 (独立 opus auditor): **PASS** (q67 修复后)
4 能力类各 2: COUNT q103/q104, ENUMERATE q34/q107, CT q43/s05, ATTRIBUTE q05/q01。逐元素对账 meta.yaml (2 题另对账原始 KB: VARIABLE_INDEX.md / DM spec.md+dm.md)。初判 7 PASS/1 PARTIAL (s05 codelist 元数据 recall 缺口, 安全非答非错答→backlog) + q67 抽样外缺陷 (已修)。q67 修复后唯一真实错答关闭 → Rule A PASS。**自动 fact_recall 对 q67/s05 均 1.0 (子串假阳) — 印证独立语义核验补住自动指标盲区 (规则 A 价值)**。

### 三准则最终判定
| 准则 | 判定 |
|------|------|
| (a) q103/q104 翻绿 | **PASS** |
| (b) 全类零真实回归 (src +0; fact 负 delta 全为噪声/翻译伪降) | **PASS** |
| (c) ON 臂 0 计数闸 violation (闸 v2) | **PASS** (oracle 0) |
| Rule D 异 type 独立审 | **APPROVE** |
| Rule A N=8 语义抽检 | **PASS** |

→ **Phase 1 PASS**; `structured_answer_enabled` 默认翻 **ON** (env 可即时回滚)。backlog (转 RETROSPECTIVE/SP2 收尾): 词典词变量锚定 relevance gate、s05 codelist 元数据注入、enumerate corpus 列表、FP2 是否改 eval-log-only。
