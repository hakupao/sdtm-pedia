# U6 抽检方 B — 变异测试报告

> 角色: doc 轨 U6 抽检方 B (规则 D 五方之一, 独立 session, 与 Task 实施方 / 审查方 / 抽检 A 不同 context)
> 日期: 2026-08-18
> 对象: U6 新建 / 修缮的**闸与仪器**共 8 个源文件
> 方法: 逐条源码变异 → 跑对应测试 → 记 KILLED / SURVIVED / EQUIVALENT → 还原并自检
> 红线: 本报告零题面、零真名; 只含题号 / 测试函数名 / 源码片段 (源码本身已在 git) / 计数

---

## 0. 结论 (先说结果)

**235 条源码变异, KILLED 197 / SURVIVED 38** (其中 8 条经论证为**等价变异**, 1 条是我自己设计得
太弱的变异)。杀灭率 197/235 = **83.8%**; 剔掉等价变异后 197/227 = **86.8%**。存活里剩下的
**29 条构成 15 条 finding**: 高 1 / 中 10 / 低 4。冻结期基线与收尾复跑均为 **1654 passed**。

全部 38 条 SURVIVED 都**再用全量 1654 条复判过一遍**, 无一条被别的测试文件杀掉 (每次复判的
`restored_clean` 皆为 true, 输出皆为 `1654 passed`) —— 即这 38 条确实是"改坏源码而测试全绿"。

> **复验后记 (2026-08-18, `f2244e7`)**: 补杀波之后用同一套变异集重跑过一遍, **29 条 finding 变异
> 全部转 KILLED**, F-01..F-15 无一留作 known limit; 终态存活 9 条 = 8 条等价 + 1 条我自己设计过弱的
> 变异 (F08, 其守卫本体有锚)。**§0-§8 保持复验前的原貌不动** (它们是补杀波的输入), 复验结果与
> 终态存活清单见 **§9**。

| 文件 | 变异 | KILLED | SURVIVED | 其中等价 | 计入缺口 |
|------|-----:|-------:|---------:|---------:|---------:|
| `eval/u6_gate_verdict.py` | 36 | 30 | 6 | 0 | 6 |
| `eval/u6_answer_verdict.py` | 44 | 40 | 4 | 1 | 3 |
| `server/routing_signals.py` | 26 | 16 | 10 | 3 | 7 |
| `server/federation.py` | 25 | 21 | 4 | 3 | 1 |
| `server/study_lookup.py` | 30 | 28 | 2 | 0 | 2 |
| `eval/u6_calibrate_signals.py` | 26 | 19 | 7 | 0 | 6 (+1 弱变异) |
| `eval/run_routing_eval.py` | 36 | 32 | 4 | 1 | 3 |
| `eval/run_eval.py` | 12 | 11 | 1 | 0 | 1 |
| **合计** | **235** | **197** | **38** | **8** | **29** |

**一句话读法**: U6 的**判据本体与接线**几乎钉得密不透风 —— 条款 1/2/3/4/7 的每一半、每个阈值、
每个方向, off/on 双臂开关的每一环 (flag 闸 → 工厂 → 引擎 → summary → 回执), G1 那条最贵的裁定
的**两个方向**, 以及两条把题面写进日志的红线写法, 全部当场被杀。**缺口集中在两处**:

1. **F-01 (唯一的高)**: Task 9 冻结的词表与正则**只有阳性对照, 没有阴性对照** —— 而这些件的
   全部价值恰恰在"不该 fire 的时候不 fire"。把红线词表塞进临床概念词、把 CT 码位数放宽、把
   为 CJK 专门写的两侧边界拆掉, 1654 条测试**全绿**。
2. **一批"合取/并集只测了一半"** (F-02/03/04/08/12): 组量闸只测 dev 不测 heldout、三遍纪律只测
   baseline 一臂、`divergent` 只测 net 半而 docstring 自称覆盖两半、规则 (c) 只测"两个信号都死"、
   meta 校验只测"整个 meta 缺失"而不测"`generated_at` 为空"。

三条 finding 另做了**后果实证**而不是只写推理 (§5)。其中一条把我自己的推断推翻了: A17 (F-12) 我原判
"只是错话术", 实测是**直接放行** —— 一份没有跑批时刻的 run 会被收下, 因此该条由「低」上调为「中」。

*(本文件边做边落盘, 下面各节按完成顺序追加。)*

---

## 1. harness 自证 (先证仪器, 再用仪器)

变异 harness 放 scratchpad (不进 git), 每条变异走固定七步:

```
净树自检 (只看本审计的 8 个目标源文件)
  → purge __pycache__ (eval/ server/ scripts/ 三棵子树)
  → 打补丁 (锚点必须**恰好出现 1 次**, 否则 ANCHOR_FAIL)
  → py_compile 前置检查
  → purge __pycache__ (清掉 py_compile 自己写的 pyc)
  → pytest (对应测试文件)
  → git checkout 还原 + purge + git status 空自检 (restored_clean)
```

两道 purge + 一道 compile 是 U5 踩实过的两个坑 (假阴性 / 假还原) 的防线。**harness 不许自证清白靠声明**,
故先跑四条自检变异:

| id | 变异 | 期望 | 实测 | 判定 |
|----|------|------|------|------|
| S0 | `LEGACY_FLOOR = 178 ((` 故意语法错 | compile 检查抓住, 不进 pytest | `COMPILE_FAIL: SyntaxError: '(' was never closed` | ✅ compile 闸有效 |
| S1 | 阳性对照 `LEGACY_FLOOR 178 → 999` | KILLED | `13 failed, 52 passed` | ✅ 测试真的会红 |
| S2 | 阴性对照 (只改注释) | SURVIVED | `65 passed` | ✅ harness 不假杀 |
| S3 | 锚点不存在 | ANCHOR_FAIL (不静默跳过) | `anchor occurs 0 times (need 1)` | ✅ 无声跳过被堵死 |

S0 是硬要求 3 点名的那条: 若 compile 检查缺席, 一条语法错变异会让 pytest 直接 collect error 而被读成
"KILLED" —— 那是**假杀**, 它会把一条根本没被执行过的变异记成有效覆盖。S2 是它的对偶: 若 purge 缺席,
一条真变异可能因 stale pycache 被读成 SURVIVED (**假活**)。两条对照同时成立, harness 才可用。

**跑批中途 harness 真的坏过一次, 如实记下来**: 第 F 组跑到一半时 `git checkout -- <file>` 返回 128
(同一工作树上另有 agent 在跑 git, 撞上 index.lock), 那条变异**留在了工作树里**。是"每条变异开跑前
先做净树自检"这一步当场把后续整组拦停 (`HARNESS_ABORT: tree dirty before: M eval/u6_calibrate_signals.py`),
没有一条结果被脏树污染。修法: `restore()` 改成重试 6 次并**以 `git status` 为准再确认一次**, 确认不了
就抛。受影响的 F15-F25 全部重跑。—— 这正是"假还原"这个坑的真实形态: 它不是理论风险。

**冻结期基线**: 变异开始前全量 `pytest` = **1654 passed in 44.30s** (rc=0)。

**判定口径**: 主判用「对应测试文件」快集 (秒级); 凡 SURVIVED 的, 一律**再用全量 1654 条复判一次**,
避免"别的测试文件其实能杀"被误记成缺口。下表 SURVIVED 均为全量复判后的结果。

**还原自检**: 每条变异的 `restored_clean` 逐条为 true (8 个目标源文件 `git status --porcelain` 为空)。

---

## 2. 逐组结果

### 2.1 `eval/u6_gate_verdict.py` (七条款判定) — 36 条, KILLED 30 / SURVIVED 6

| id | 变异 | 判定 | 杀它的测试 (首条) |
|----|------|------|--------------------|
| A01 | `LEGACY_FLOOR` 178→177 | KILLED | `test_clause1_legacy_floor_is_178` |
| A02 | `C2_GAP_PT` 25→100 | KILLED | `test_clause2_gap_boundary_is_25pt` |
| A03 | `C3_DEV_MIN` 10→0 | KILLED | `test_clause3_dev_floor_is_10` |
| A04 | `GROUP_N` 12→24 | KILLED | 37 条红 (分母与组量闸共用常量) |
| A05 | **对调** `DUAL_GATE_GROUPS` 两格互换 | KILLED | `test_clause4_and_clause7_do_not_read_the_same_group` |
| A06 | `_rev_sha` 退回整串比 | KILLED | `test_shared_git_rev_between_base_and_after_warns` |
| A07 | `_rev_sha` 前缀判 `g`→`v` | KILLED | 同上 |
| A08 | 脏树告警失灵 (`-dirty`→`-clean`) | KILLED | `test_dirty_git_rev_warns_but_does_not_fail` |
| A09 | **并集/交集** `shared` 由 `&` 改 `|` | **SURVIVED** | — |
| A10 | `shared` 不再剔除 `unknown` | KILLED | `test_unknown_git_rev_does_not_trigger_shared_warning` |
| A11 | **合取半** `need` 丢掉双列闸两组 | KILLED | `test_missing_group_is_rejected` |
| A12 | **合取半** 组量闸只查 dev 不查 heldout | **SURVIVED** | — |
| A13 | 组量闸 `!=`→`<` (组变大不拦) | **SURVIVED** | — |
| A14 | 双列闸组量一致性 `>1`→`>2` | KILLED | `test_dual_gate_group_size_mismatch_is_rejected` |
| A15 | **合取半** 组量一致性只看 baseline | KILLED | 同上 |
| A16 | **合取半** 三遍纪律只查 baseline 份数 | **SURVIVED** | — |
| A17 | **合取半** `generated_at` 为空不再拦 | **SURVIVED** | — |
| A18 | 批内重复闸恒不触发 | KILLED | `test_duplicate_run_within_the_after_batch_is_rejected` |
| A19 | **合取半** I-2 拷贝闸丢掉 summary 半 | **SURVIVED** | — |
| A20 | **合取半** I-2 拷贝闸丢掉 meta 半 | KILLED | `test_same_summary_but_different_run_is_not_rejected` |
| A21 | **对调** `_dual_gate` 的 fatal/exact 两列互换 | KILLED | 17 条红 |
| A22 | **合取半** 双列闸只留 exact 半 | KILLED | `test_dual_gate_fatal_allows_equal_but_not_increase` |
| A23 | **合取半** 双列闸只留 fatal 半 | KILLED | `test_clause4_exact_column_trips` |
| A24 | exact 半容差 1→2 | KILLED | `test_dual_gate_exact_allows_drop_of_exactly_one` 等 4 条 |
| A25 | **对调** `_dual_gate` 调用处 baseline/after 互换 | KILLED | 15 条红 |
| A26 | **合取半** 条款1 丢掉 legacy floor 半 | KILLED | `test_clause1_legacy_floor_is_178` |
| A27 | **合取半** 条款1 丢掉 fatal=0 半 | KILLED | `test_clause1_any_non_final_fatal_trips` |
| A28 | **对调** 条款1 读 baseline 而非 after | KILLED | 10 条红 |
| A29 | 条款1 `all`→`any` | KILLED | `test_clause1_reads_every_run_not_just_the_first` |
| A30 | **对调** 条款2 拿 dev 去比 heldout | KILLED | `test_clause2_measures_heldout_against_dev_not_the_reverse` |
| A31 | **对调** dev/heldout 百分比两式互换 | KILLED | 同上 |
| A32 | 条款3 边界 `>=`→`>` | KILLED | `test_clause3_dev_floor_is_10` |
| A33 | rc 丢掉条款4/7 | KILLED | `test_clause4_exact_column_trips` 等 7 条 |
| A34 | rc `all`→`any` | KILLED | 8 条红 |
| A35 | **对调** clause5 的 final 过滤取反 | KILLED | `test_clause5_final_group_is_report_only` |
| A36 | clause6 不稳定判据 `>1`→`>2` | KILLED | `test_clause6_flags_only_the_unstable_ids` |

条款判定层的**判据本体** (1/2/3/4/7 的每一半、每个阈值、每个方向) 全部有测试钉住 —— 包括三条
「对调型」(A05 / A21 / A25 / A28 / A30 / A31 / A35) 与所有合取半拆解 (A11 / A15 / A20 / A22 / A23 /
A26 / A27)。6 条存活全部落在**产物校验闸** (`validate_inputs` / `_check_groups` / `_warn_provenance`),
即"判据之前那一圈守门人"—— 详见 §4。

### 2.2 `eval/u6_answer_verdict.py` (E1 支配 / E4 并集 / I-1 抑制 / divergent) — 44 条, KILLED 40 / SURVIVED 4

| id | 变异 | 判定 | 杀它的测试 (首条) |
|----|------|------|--------------------|
| B01 | `E4_MAX_UNION[cards]` 9→99 | KILLED | `test_e4_threshold_boundary_per_family` |
| B02 | **对调** E4 上限 cards/docs 两格互换 | KILLED | 同上 |
| B03 | `CHEAP_WORD` 去掉可比池限定 | KILLED | `test_frozen_thresholds_are_literal` |
| B04 | `_EPS` 1e-9→1e-1 | KILLED | `test_divergent_readings_flag` |
| B05 | 三遍纪律 `!=`→`<` (四遍放行) | **SURVIVED** | — |
| B06 | 表头题量闸 `!=`→`>` | KILLED | `test_rejects_wrong_n_questions_in_any_run` |
| B07 | judge 在场闸失灵 | KILLED | `test_rejects_run_without_judge` |
| B08 | 计分行数闸 `!=`→`>` | KILLED | `test_rejects_row_count_mismatch` |
| B09 | 支配严格小于→非严格 | KILLED | `test_dominance_boundary_is_strict` |
| B10 | **对调** 支配的 cost/gain 两支互换 | KILLED | `test_dominance_is_two_sided_swap_flips_cost_and_gain` |
| B11 | **对调** `mean_gap` 的 A/B 两臂互换 | KILLED | `test_dominance_amount_is_the_three_run_mean_gap` |
| B12 | **析取半** 支配 parse 守卫只看 A 臂 | KILLED | `test_dominance_requires_all_six_values_parse_ok` |
| B13 | **合取半** `n_all_parse_ok` 只核 A 臂 | KILLED | 同上 |
| B14 | I-1 probe `n=0` 守卫失灵 | KILLED | `test_probe_n_zero_is_rejected` |
| B15 | I-1 阈值边界 `>=`→`>` | KILLED | `test_i1_threshold_boundary` |
| B16 | family 查表守卫取反 | KILLED | `test_rejects_unknown_family` |
| B17 | **对调** off/on 两臂 (`_raw_maps`) | KILLED | 13 条红 |
| B18 | **对调** off/on 两臂 (`stability`) | KILLED | 10 条红 |
| B19 | 两臂题集一致守卫拆除 | KILLED | `test_rejects_mismatched_question_sets_across_arms` |
| B20 | **对调** `paired_effect` 两臂互换 | KILLED | 6 条红 |
| B21 | `caliber` 子集标记键去掉 | KILLED | `test_stable_half_carries_a_caliber_marker` |
| B22 | **对调** 稳定半 cost/gain 差式符号互换 | **SURVIVED** | — (等价, 见 §4) |
| B23 | **并集半** 支配代价不并入 E1 | KILLED | `test_dominance_amount_is_the_three_run_mean_gap` |
| B24 | **并集半** 支配收益不并入 E1 | KILLED | `test_dominance_is_two_sided_swap_flips_cost_and_gain` |
| B25 | **对调** 支配 cost/gain 并入方向互换 | KILLED | 12 条红 |
| B26 | **并集/交集** `dominance_ids` 由 `|` 改 `&` | KILLED | `test_dominance_boundary_is_strict` |
| B27 | **并集半** `stable_moved` 只算 cost 半 | **SURVIVED** | — |
| B28 | **对调** `dominance_only_ids` 差集方向反转 | KILLED | `test_dominance_only_ids_names_what_the_worst_bound_ruler_added` |
| B29 | **并集 vs 拼接** E4 union 改列表相加 | KILLED | `test_e4_union_deduplicates_overlapping_ids_at_the_gate_boundary` |
| B30 | **并集/交集** E4 union 由 `|` 改 `&` | KILLED | `test_e4_is_a_union_not_a_per_arm_check` |
| B31 | E4 闸边界 `<=`→`<` | KILLED | `test_e4_threshold_boundary_per_family` |
| B32 | E4 闸查表写死 cards 上限 | KILLED | 同上 |
| B33 | **合取半** divergent 丢掉 agg 非零半 | **SURVIVED** | — |
| B34 | **合取半** divergent 丢掉 net 非零半 | KILLED | `test_divergent_false_when_one_reading_is_zero` |
| B35 | divergent 符号判 `!=`→`==` | KILLED | `test_divergent_false_when_both_readings_agree` |
| B36 | **对调** 聚合差式 B−A 改 A−B | KILLED | `test_aggregate_is_b_minus_a_oriented_like_paired_net` |
| B37 | **对调** 配对净额 gain−cost 改 cost−gain | KILLED | 同上 |
| B38 | E4 闸响判词 `None`→advisory | KILLED | `test_e4_union_gate_trips` |
| B39 | cheap 判据由 ids 空改 pt 读数为 0 | KILLED | `test_cost_reported_even_when_pt_rounds_to_zero` |
| B40 | **合取半** I-1 抑制丢掉 pass 半 | KILLED | `test_i1_threshold_boundary` |
| B41 | I-1 抑制项名改 E4 | KILLED | `test_i1_fail_suppresses_verdict_word` |
| B42 | rc: E4 闸响不再改 rc | KILLED | `test_e4_union_gate_trips` |
| B43 | **对调** rc 由 I-1 决定而非 E4 | KILLED | 同上 |
| B44 | E1 pt 分母由 n_scored 改可比池 | KILLED | `test_pt_denominator_is_n_scored_not_expected_n` |

U5 §9-3 点名的四类硬要求在本文件上全部有钉子: 并集 vs 拼接 (B29)、并集 vs 交集 (B26 / B30)、
off/on 两臂对调 (B17 / B18 / B20)、cost/gain 方向对调 (B10 / B25 / B37)。判词口径的三条
(`CHEAP_WORD` 词面 B03、cheap 靠 ids 而非 pt B39、E4 闸响判词为 None B38) 也各有专测。

### 2.3 `server/routing_signals.py` (信号层本体) — 26 条, KILLED 16 / SURVIVED 10

| id | 变异 | 判定 | 杀它的测试 (首条) |
|----|------|------|--------------------|
| C01 | 白名单多一个表外理由 | KILLED | `test_contract_map_and_whitelist_are_one_source` |
| C02 | 白名单半: 只留 `study_sig` | KILLED | 17 条红 |
| C03 | **对调** 方向表两格互换 | KILLED | 15 条红 |
| C04 | 方向表两格塌成同一理由 | KILLED | 11 条红 |
| C05 | 词表混入未归一化词条 (大写) | KILLED | `test_terms_are_already_in_matching_normal_form` |
| C06 | 词表混入临床概念词 (红线) | **SURVIVED** | — |
| C07 | CT 码位数 `{5,6}`→`{4,6}` | **SURVIVED** | — |
| C08 | CT 码正则去掉两侧 ASCII 边界 | **SURVIVED** | — |
| C09 | 变量形态正则去掉左边界 | **SURVIVED** | — |
| C10 | 变量形态正则去掉右边界 | **SURVIVED** | — |
| C11 | `_alt` 长词优先排序取消 | **SURVIVED** | — (等价, 见 §4) |
| C12 | `_norm` 丢掉 `.lower()` | **SURVIVED** | — |
| C13 | 归一化 NFKC→NFC | KILLED | `test_cdisc_signal_fires_on_code_shapes` |
| C14 | **G1 回归**: study 信号退回 `resolve` 任意命中 | KILLED | `test_signal_layer_does_not_fire_on_the_weak_channel` 等 8 条 |
| C15 | **析取半** cdisc 信号丢掉结构词表半 | KILLED | `test_cdisc_signal_fires_on_struct_terms` |
| C16 | **析取半** 丢掉 CT 码半 | KILLED | `test_cdisc_signal_fires_on_code_shapes` |
| C17 | **析取半** 丢掉变量形态半 | KILLED | 同上 |
| C18 | 词表比对用未小写串 | KILLED | `test_cdisc_signal_is_case_insensitive_on_terms` |
| C19 | CT 码 / 变量形态改在小写串上搜 | KILLED | `test_cdisc_signal_fires_on_code_shapes` |
| C20 | **对调** `widen_reason` 两分支的信号侧互换 | KILLED | 15 条红 |
| C21 | **对调** `widen_reason` 返回的理由两格互换 | KILLED | 11 条红 |
| C22 | `both` 也进 cdisc 分支 | KILLED | `test_widen_only_never_fires_outside_the_two_single_corpora` |
| C23 | `build_signals` catalog 缺失不再抛 | **SURVIVED** | — |
| C24 | **对调** 传入的 `study_lookup` 被忽略 | KILLED | `test_build_signals_reuses_a_given_lookup_without_touching_disk` |
| C25 | `build_signals` 改成可返回 None | **SURVIVED** | — (等价, 见 §4) |
| C26 | 别名表路径不再传入 (通道③ 空转) | **SURVIVED** | — |

**这是本次审计密度最低的一块**: 10 条存活里 7 条压在 Task 9 冻结的词表 / 正则上 (C06-C12)。
契约面 (白名单 / 方向表 / widen-only / 生产同源) 反而全被钉死 —— 缺口不在"接线", 在"标定件本身"。

### 2.4 `server/federation.py` (decide_corpus / 信号消费) — 25 条, KILLED 21 / SURVIVED 4

| id | 变异 | 判定 | 杀它的测试 (首条) |
|----|------|------|--------------------|
| D01 | **合取半** 丢掉 `corpus in (cdisc, study)` 半 | **SURVIVED** | — (等价, 见 §4) |
| D02 | **合取半** 丢掉 `signals is not None` 半 | **SURVIVED** | — |
| D03 | `both` 纳入纠偏范围 | **SURVIVED** | — (等价, 见 §4) |
| D04 | **契约半** 白名单闸拆除 | KILLED | `test_decide_corpus_rejects_reasons_outside_the_whitelist` |
| D05 | **契约半** 方向闸拆除 | KILLED | `test_decide_corpus_rejects_a_reason_that_contradicts_the_routed_corpus` |
| D06 | **对调** 两条契约的 `kind` 哨兵互换 | KILLED | 同上 |
| D07 | 旁路收窄成 `except ValueError` | KILLED | `test_decide_corpus_treats_a_raising_signal_layer_as_no_widen` |
| D08 | 旁路后 `reason` 不清零 | KILLED | 7 条红 |
| D09 | **红线** warning 带异常原文 | KILLED | `test_rendered_warning_has_no_question_text` |
| D10 | **红线** warning 打 `exc_info` | KILLED | 同上 |
| D11 | widen-only 打破: 拓宽改成换库 | KILLED | `test_decide_corpus_widens_single_corpus_to_both` |
| D12 | 拓宽发生但观测字段不记 | KILLED | 同上 |
| D13 | 观测字段记了但库没拓宽 | KILLED | 9 条红 |
| D14 | `route_corpus` 取值白名单拆除 | KILLED | `test_route_bad_output_falls_back_both` |
| D15 | **对调** 兜底 fallback 标志 True→False | KILLED | `test_decide_corpus_keeps_fallback_flag_on_router_failure` |
| D16 | **析取半** JSON 定位守卫丢掉 `end<=start` 半 | **SURVIVED** | — (等价, 见 §4) |
| D17 | `last_signal_widened` 恒 None | KILLED | `test_engine_auto_widens_and_records_the_reason` |
| D18 | **对调** 两个观测属性赋值互换 | KILLED | 同上 |
| D19 | 构造期不预置观测属性 | KILLED | `test_signals_default_to_none_and_widened_attr_exists_before_any_retrieve` |
| D20 | 强制档不清零观测属性 | KILLED | `test_last_signal_widened_clears_on_the_next_forced_retrieve` |
| D21 | both 配额 `ceil`→`floor` | KILLED | `test_both_quota_ceil_half_each_no_score_sort` |
| D22 | **对调** both 拼接顺序 | KILLED | 同上 |
| D23 | corpus 参数校验只留 auto | KILLED | `test_invalid_corpus_rejected` |
| D24 | **对调** `_system_for` 两支互换 | KILLED | `test_build_messages_system_per_corpus` |
| D25 | `_SignalContractError` 的 kind 被改写 | KILLED | `test_decide_corpus_rejects_reasons_outside_the_whitelist` |

两条红线变异 (D09 / D10 —— 把题面写进服务端 warning 的两种写法) **都被专测当场杀死**, 这是本次
审计里最让人放心的一格。4 条存活全部是"双重守卫的外层"或"更宽的错误消息", 逐条论证见 §4。

### 2.5 `server/study_lookup.py` (strong_hit / _channel_hits) — 30 条, KILLED 28 / SURVIVED 2

| id | 变异 | 判定 | 杀它的测试 (首条) |
|----|------|------|--------------------|
| E01 | **析取半** `strong_hit` 丢通道① | KILLED | `test_strong_hit_true_for_each_strong_channel` |
| E02 | **析取半** 丢通道③ | KILLED | 同上 |
| E03 | **析取半** 丢通道②a | KILLED | 同上 |
| E04 | **G1 回归** `strong_hit` 收编弱通道②b | KILLED | `test_strong_hit_false_for_the_weak_single_token_channel` |
| E05 | **对调** `strong_hit` 只认弱通道 | KILLED | 5 条红 |
| E06 | ②a 门槛 `>=2`→`>=1` | KILLED | `test_weak_single_token_channel_does_not_widen` |
| E07 | ②a 合取改析取 (交集变并集) | KILLED | `test_three_token_intersection_requires_all_three_segments` |
| E08 | **合取半** ②a cap 上限拆除 | KILLED | `test_oversized_intersection_does_not_fire` |
| E09 | **合取半** ②b cap 上限拆除 | KILLED | 8 条红 |
| E10 | **对调** ① label 子串判定取反 | KILLED | 17 条红 |
| E11 | ① 歧义 cap `<=`→`>=` | KILLED | `test_ambiguous_label_over_cap_is_skipped` |
| E12 | **合取半** ③ 别名丢 `in qn` 半 | KILLED | `test_strong_hit_ignores_hits_that_resolve_would_skip` |
| E13 | **合取半** ③ 别名丢去重半 | KILLED | `test_same_form_synonyms_yield_one_scope` |
| E14 | **对调** resolve 入队优先级反转 | KILLED | `test_intersection_is_enqueued_before_single_token_hits` |
| E15 | resolve 总 cap 拆除 | KILLED | `test_total_cards_capped_at_10` |
| E16 | resolve 去重拆除 | KILLED | `test_intersection_is_enqueued_before_single_token_hits` |
| E17 | 拉丁 token 最短 3→2 位 | KILLED | `test_latin_token_regex_boundary_semantics` |
| E18 | 拉丁 token 去掉 ASCII 边界 | KILLED | 同上 |
| E19 | `_MIN_SEG_LEN` 3→2 | KILLED | `test_min_seg_len_matches_token_regex_lower_bound` |
| E20 | `_MIN_LABEL_LEN` 4→2 | KILLED | `test_label_length_bound_is_exactly_four` |
| E21 | `_MAX_CARDS_PER_MATCH` 8→100 | KILLED | 9 条红 |
| E22 | 归一化丢掉去空白 | KILLED | `test_whitespace_normalization_matches_query` |
| E23 | label 入索引门槛 `>=`→`>` | KILLED | `test_label_length_bound_is_exactly_four` |
| E24 | **对调** OID 家族键首段→末段 | KILLED | `test_family_does_not_cross_form_with_shared_first_segment` |
| E25 | 段索引不去重 | **SURVIVED** | — |
| E26 | 空别名守卫拆除 | KILLED | `test_alias_empty_term_rejected` |
| E27 | 别名指向不存在 form 的守卫拆除 | KILLED | `test_alias_unknown_form_fails_loud` |
| E28 | `from_paths` catalog 缺失静默降级 | KILLED | `test_from_paths_missing_catalog_fails_loud` |
| E29 | `strong_hit` 另起一套筛选 (单一定义被打破) | KILLED | `test_strong_hit_ignores_hits_that_resolve_would_skip` |
| E30 | token 去重取消 | **SURVIVED** | — |

G1 那条判据 (强通道认 ①②a③、弱通道②b 不认) 是本单元最贵的一处裁定, 它的**两个方向**都有测试:
收编弱通道会红 (E04), 只认弱通道也会红 (E05)。`strong_hit` 与 `resolve` 共用 `_channel_hits`
这条"单一定义"也有专测钉住 (E29)。

### 2.6 `eval/u6_calibrate_signals.py` (可见集标定台) — 26 条, KILLED 19 / SURVIVED 7

| id | 变异 | 判定 | 杀它的测试 (首条) |
|----|------|------|--------------------|
| F01 | 可见集半: 只留 legacy | KILLED | 17 条红 |
| F02 | **封存破口**: 可见集混进 heldout | KILLED | 16 条红 |
| F03 | **对调** (c) 操作性读法 detect→widen | KILLED | `test_accepted_requires_all_three_rules` |
| F04 | **对调** 可见集过滤取反 | KILLED | `test_visible_subset_keeps_only_legacy_and_dev` |
| F05 | 缺组守卫只查多出不查缺失 | KILLED | `test_visible_subset_raises_when_a_visible_group_is_absent` |
| F06 | 读入处过滤拆除 (封存组进内存) | KILLED | `test_load_base_preds_drops_invisible_ids` |
| F07 | 基线缺题守卫拆除 | KILLED | `test_load_base_preds_raises_when_a_visible_id_is_missing` |
| F08 | 非法 pred 守卫放宽一个取值 | **SURVIVED** | — |
| F08b | 非法 pred 守卫**整条**拆除 | 见下 | — |
| F09 | 探针不看方向 | **SURVIVED** | — |
| F10 | **对调** 探针异常时按命中计 | **SURVIVED** | — |
| F11 | 重放 fallback 守卫拆除 | **SURVIVED** | — |
| F12 | **对调** widen 计数记进 detector 桶 | KILLED | `test_widen_fire_ids_are_listed_by_signal_and_group` |
| F13 | **对调** base/sim 两次 score_run 互换 | KILLED | `test_rule_a_fails_when_legacy_exact_drops` |
| F14 | **对调** `d_exact` 差式方向反转 | KILLED | `test_simulate_scores_baseline_and_widened_per_group` |
| F15 | 规则 (a) 改为允许降 1 | KILLED | `test_rule_a_fails_when_legacy_exact_drops` |
| F16 | **对调** 规则 (a)(b) 的两组互换 | KILLED | 同上 |
| F17 | 规则 (b) 容差 1→2 | KILLED | `test_rule_b_allows_at_most_one_dev_exact_drop` |
| F18 | 规则 (c) `all`→`any` | **SURVIVED** | — |
| F19 | **对调** operative 读法标记取反 | KILLED | `test_rule_c_reports_both_readings_and_marks_the_operative_one` |
| F20 | accepted 的 `or` 改 `and` | KILLED | 14 条红 |
| F21 | accepted `all`→`any` | KILLED | `test_rule_c_dead_signal_fails` |
| F22 | 非操作性读法也进 accepted | KILLED | `test_accepted_requires_all_three_rules` |
| F23 | 落盘产物混入 `sim_preds` 中间量 | **SURVIVED** | — |
| F24 | rc 与 accepted 脱钩 (恒 0) | **SURVIVED** | — |
| F25 | 离线模拟绕开 `decide_corpus` | KILLED | `test_simulate_matches_decide_corpus_per_question` |

F25 被杀是这一格最关键的一条: 模块 docstring 声称"离线模拟与真跑等价, 因为走的是生产那条同一
函数", 而这条声称**有可执行的锚** —— 改成自己直接问信号层就红。

### 2.7 `eval/run_routing_eval.py` (U6 修缮点) — 36 条, KILLED 32 / SURVIVED 4

| id | 变异 | 判定 | 杀它的测试 (首条) |
|----|------|------|--------------------|
| G01 | `LEGACY_EXACT_FLOOR` 178→170 | KILLED | `test_policy_constants_match_spec` |
| G02 | 组量期望表 final 4→3 | KILLED | `test_final_group_has_four_including_v2_q07` |
| G03 | **对调** 组量表 dev/heldout 两格互换 | KILLED | `test_policy_constants_match_spec` |
| G04 | `FINAL_IDS` 丢掉 T3 补的第 4 题 | KILLED | 23 条红 |
| G05 | `V2_FINAL_IDS` 清空 | KILLED | 27 条红 |
| G06 | `AUTHORED_GROUPS` 收编 final | KILLED | `test_docs_routing_gold_rejects_self_declared_reserved_group` |
| G07 | final 组恒等 FINAL_IDS 的第二道闸拆除 | KILLED | `test_final_group_must_equal_final_ids` |
| G08 | 组题量闸拆除 | KILLED | `test_trimmed_u1_doc_set_raises` |
| G09 | gold id 重名闸拆除 | KILLED | `test_duplicate_id_across_sets_raises` |
| G10 | **对调** fatal 判据由 both 改 cdisc | KILLED | 15 条红 |
| G11 | **合取半** `score_run.passed` 丢 fatal 半 | **SURVIVED** | — |
| G12 | **合取半** `score_run.passed` 丢阈值半 | KILLED | `test_both_is_nonfatal_but_not_exact` |
| G13 | 未知 group 守卫拆除 | KILLED | `test_score_by_group_rejects_unknown_group` |
| G14 | **对调** fatal 口径「除 final」→「只 final」 | KILLED | 10 条红 |
| G15 | **合取半** 条款1 丢 legacy floor 半 | KILLED | `test_gate_verdict_fails_when_legacy_below_floor` |
| G16 | **合取半** 条款1 丢 fatal=0 半 | KILLED | `test_gate_verdict_counts_non_final_fatal` |
| G17 | **I-4 回归**: by_group 保留组级 `passed` | KILLED | `test_by_group_has_no_passed_key` |
| G18 | **红线**: by_group 保留 `fatal_items` | KILLED | `test_gate_verdict_excludes_final_from_fatal` |
| G19 | legacy 参照物守卫拆除 | KILLED | `test_gate_verdict_raises_without_legacy_subset` |
| G20 | **I-1 回归**: `--runs` 三遍纪律守卫拆除 | KILLED | `test_runs_guard_rejects_non_three` |
| G21 | **A-3 回归**: `generated_at` 写死常量 | KILLED | `test_each_run_gets_its_own_generated_at` |
| G22 | 假标签: meta 的 `signal_layer` 恒写 off | KILLED | `test_signal_layer_on_builds_signals_through_the_production_factory` |
| G23 | `--out-prefix` 被忽略 (U6 修缮点) | KILLED | `test_meta_writes_the_out_prefix` 等 5 条 |
| G24 | **对调** `--signal-layer` on/off 两臂互换 | KILLED | `test_signal_layer_defaults_off_and_bypasses_the_signal_layer` |
| G25 | `--signal-layer` 默认 off→on | KILLED | 同上 |
| G26 | 工厂返回 None 的响亮失败拆除 | KILLED | `test_signal_layer_on_refuses_a_null_factory` |
| G27 | 信号层不传给 `decide_corpus` | KILLED | `test_signal_layer_on_builds_signals_through_the_production_factory` |
| G28 | 稳定性判据 `==1`→`>=1` (恒 100%) | **SURVIVED** | — |
| G29 | **合取半** 稳定性行守卫丢 allow 半 | **SURVIVED** | — |
| G30 | **对调** `all_passed` 由与改或 | KILLED | `test_main_rc_follows_gate_verdict` |
| G31 | **对调** u1_doc / final 分组互换 | KILLED | 22 条红 |
| G32 | docs gold 的 group 白名单闸拆除 | KILLED | `test_docs_routing_gold_rejects_self_declared_reserved_group` |
| G33 | `_git_rev` 去掉 `--dirty` | KILLED | `test_git_rev_marks_dirty_worktree` |
| G34 | `load_v2_final` 整份题集并入 | KILLED | 23 条红 |
| G35 | 补充 gold 空文件守卫拆除 | **SURVIVED** | — |
| G36 | **红线**: gold 加载异常消息带整条 item | KILLED | `test_gold_loader_error_message_carries_no_question_text` |

U6 在本文件上的四处修缮 (meta 逐 run / `--out-prefix` / 三遍守卫 / `--signal-layer` 接线) **全部
有专测钉住**, 且 A-3、I-1、I-4 三条历史审查修缮点的回归变异也都当场被杀 (G21 / G20 / G17)。

### 2.8 `eval/run_eval.py` (`--signal-layer` 透传与镜像闸) — 12 条, KILLED 11 / SURVIVED 1

| id | 变异 | 判定 | 杀它的测试 (首条) |
|----|------|------|--------------------|
| H01 | on 不再要求 `--federated` | KILLED | `test_signal_layer_requires_federated` |
| H02 | on + 强制判库不再拦 (假标签面) | KILLED | `test_signal_layer_on_rejects_a_forced_corpus` |
| H03 | **对调** 强制判库闸方向反转 | KILLED | `test_explicit_corpus_auto_with_signal_layer_on_is_accepted` |
| H04 | 信号层另造一份 `study_lookup` | KILLED | `test_signal_layer_on_reuses_the_s2_lookup` |
| H05 | 工厂返回 None 的响亮失败拆除 (镜像闸) | KILLED | `test_signal_layer_on_refuses_a_none_factory_result` |
| H06 | **对调** on/off 两臂开关反转 | KILLED | 8 条红 |
| H07 | 信号层构造了但没接到联邦引擎 | KILLED | `test_signal_layer_on_passes_the_signals_into_the_engine` |
| H08 | `summary.signal_layer` 恒写 off | KILLED | `test_summary_records_signal_layer` |
| H09 | `summary` 不再落 `signal_layer` | KILLED | 同上 + `..._off` |
| H10 | `--signal-layer` 默认 off→on | KILLED | 22 条红 |
| H11 | 回执行 `signal_layer` 打死值 | KILLED | `test_federated_receipt_prints_signal_layer` |
| H12 | **对调** 回执 `routing` 判词与 corpus 脱钩 | **SURVIVED** | — |

答题侧 off/on 双臂的**唯一开关**这条链路 (flag 闸 → 工厂 → 引擎 → summary → 回执) 每一环都有钉子,
H07 (构造了但没接上) 这条最容易漏的也被杀。

---

## 3. SURVIVED 分流: 等价变异 (说理)

以下 8 条**改了源码但观测不到差别**, 不算测试缺口。逐条给论证 (不是"看起来没影响"这种话)。

### 3.1 B22 — 稳定半 cost/gain 差式符号互换 (真等价, 且暴露一处结构冗余)

`compare_arms` 先用 U5 口径算稳定半的额:

```python
cost = {i: stable_a[i] - stable_b[i] for i in stable_half["confirmed_cost_ids"]}
...
cost.update(dom_cost)
```

论证: `i` 属 `confirmed_cost_ids` ⇒ 两臂各自三遍**全稳定** ⇒ `va=[x,x,x]`, `vb=[y,y,y]` 且 `x>y`。
于是 `max(vb)=y < x=min(va)`, 即 `i` **必然**也在 `dom_cost` 里, 且其额 `mean(va)-mean(vb) = x-y`
恰等于 `stable_a[i]-stable_b[i]`。`cost.update(dom_cost)` 因此把上一行写的每个键**逐个覆盖成同值** ——
无论上一行写的是 `a-b` 还是 `b-a`。gain 侧同理。

⇒ 该变异不可观测 = **EQUIVALENT**。附带结论: 上面那两行在当前实现下是**结构冗余** (输出全被
覆盖)。这不是缺陷 —— 源码注释本身就写了"两种口径的额相等" —— 但它意味着这两行没有、也不可能
有独立的测试锚。若将来支配的定义放宽 (例如允许档内不稳定的贴边情形), 这条覆盖关系会断, 而那时
这两行会**突然重新生效且无人看守**。

### 3.2 C11 — `_alt` 的长词优先排序取消

`_alt` 的产物只被 `_DOMAIN_VAR_RE` 用, 而该正则在生产里只以 `bool(_DOMAIN_VAR_RE.search(q))`
被消费。交替式的分支顺序改变的是回溯路径, 不改变"在某位置是否存在一个能整体匹配 (含尾部负向
前瞻) 的分支" —— 引擎会把所有分支试遍。⇒ 布尔结果恒同 = **EQUIVALENT**。源码注释对此已有正确
判断 ("排序只是省掉那一轮回溯")。

### 3.3 C23 — `build_signals` 的 catalog 存在性守卫拆除

拆掉 `if not catalog.exists(): raise FileNotFoundError(...)` 后, 执行落到
`StudyLookup.from_paths(catalog, ...)` → `Path(catalog).read_text()` → **同样抛 FileNotFoundError,
且 OS 消息里同样带着那个路径**。而专测 `test_build_signals_raises_on_missing_catalog_never_returns_none`
断言的正是 `pytest.raises(FileNotFoundError)` + `"nope.json" in str(e)` ⇒ 两条路径对该测试不可分。

⇒ 行为面 **EQUIVALENT** (异常类与路径信息一致)。差别只在自定义消息
("信号层的 study 半边没有数据源, 拒绝半装配") 丢失。**这条消息本身没有测试锚** —— 属可记不可改的
观察, 不作为缺口计。

### 3.4 C25 — `build_signals` 改成可返回 None

变异写成 `return RoutingSignals(study_lookup) if study_lookup else None`。`StudyLookup` 既未定义
`__bool__` 也未定义 `__len__` ⇒ 实例恒真; 测试替身 `FakeLookup` 同理。⇒ 该分支在任何现实输入下
都取不到 None = **EQUIVALENT**。("永不返回 None" 这条契约由
`test_build_signals_reuses_a_given_lookup_without_touching_disk` 的 `s.study_lookup is sl` 与
上面那条 raise 测试共同守住。)

### 3.5 D01 / D03 — `decide_corpus` 里"只问单库"的外层判定

D01 (丢掉 `corpus in ("cdisc","study")` 半) 与 D03 (把 `both` 也纳入) 都让 `both` 判定去问信号层。
但内层还有一道: `RoutingSignals.widen_reason` 对 `routed="both"` 恒返回 None (专测
`test_widen_only_never_fires_outside_the_two_single_corpora` 钉住); 即便换成一个乱返回理由的信号层,
方向闸 `WIDEN_REASON_BY_CORPUS[corpus]` 对 `"both"` 会抛 `KeyError` → 落进旁路 → `reason=None`。
两条路的**返回值恒同** ⇒ **EQUIVALENT**。差别只在多一次无用调用与一条 warning。

### 3.6 D16 — `route_corpus` 的 JSON 定位守卫丢掉 `end <= start` 半

丢掉后 `raw[start:end+1]` 会切出空串或畸形串, `json.loads` 随即抛 —— 而整个 `try` 的
`except Exception` 把两种破法**归到同一出口** `("both", True)`。⇒ 返回值恒同 = **EQUIVALENT**;
守卫只是把错因写得好看些, 而错因不出 `try`。

### 3.7 G11 — `score_run["passed"]` 丢掉 fatal 半

追踪消费者: `gate_verdict` 在组装 `by_group` 时**显式剔除** `passed` (I-4 修缮, 由 G17 的测试守住),
顶层 `passed` 是它自己按条款 1 重算的 (`overall["fatal"] == 0 and legacy_exact >= FLOOR`, 由 G15/G16
守住)。`main()` 用的是后者。⇒ `score_run["passed"]` 在**生产路径上没有消费者**, 该变异不可观测 =
**EQUIVALENT**。

(附注: 同一个死字段的**另一半** (阈值半, G12) 反倒有测试断言 `test_both_is_nonfatal_but_not_exact`。
这不是缺陷, 是死字段上覆盖不对称的自然结果。)

### 3.8 F08 — 弱变异, 不计入缺口

F08 只是把一个具体取值 `"junk"` 加进合法集, 而专测用的是别的非法取值, 故未红。补跑
**F08b (把整条守卫拆掉)** ⇒ **KILLED** (`test_load_base_preds_raises_on_invalid_pred`)。
⇒ 该守卫有锚, F08 是变异设计得太弱, 不作为 finding。

---

## 4. findings (测试缺口)

严重度口径: **高** = 该缺口能让一次真实的判据/红线失守而全绿; **中** = 能让一层守卫或一处
取证静默失效, 但另有第二道拦得住或后果只影响可信度; **低** = 只影响话术 / 告警质量 / 罕见形态。

编号按最初的严重度排列; **F-12 在 §5 探针 3 之后由「低」上调为「中」**, 位置未动 (改号会让
已发出的引用对不上)。故 F-11 / F-13 / F-14 / F-15 是仅存的四条「低」。

### F-01 (高) Task 9 冻结的词表与正则**只有阳性对照, 没有阴性对照**

存活变异: **C06 / C07 / C08 / C09 / C10** —— 五条全在 `server/routing_signals.py` 的标定件上。

| 变异 | 后果 | 为什么现有测试拦不住 |
|------|------|----------------------|
| C06 词表混入临床概念词 | 红线「零临床概念」失守 | `test_terms_contain_no_clinical_concepts` 是**黑名单**实现 (`("病","癌","検査値","薬","投与量","mg","腫")`); 本域最核心的那类临床词根本不含这些字根, 照样进得来 |
| C07 CT 码位数 `{5,6}`→`{4,6}` | 4 位形态开始误触 | 阴性对照 `test_cdisc_signal_stays_silent_on_non_standard_shapes` 只有"纯数字"与"3 位大写", 没有"C + 4 位数字" |
| C08 CT 码去掉两侧 ASCII 边界 | 码形态可在更长串内部被切出 | 同上, 阴性集无"嵌在更长 ASCII 串里"的形态 |
| C09 / C10 变量形态正则去掉左/右边界 | 变量名嵌在更长大写串里也算命中 | 阳性侧覆盖很细 (含"紧贴假名"与"全角"两个真实坑), 阴性侧一条都没有 |

**为什么这条排最高**: 这五处正是 Task 9 花整轮标定才收敛下来的东西, 而标定收敛的判据恰恰是
"**别多触**" (起点版 `[A-Z]{4,8}` 在可见集上误触 6 题, 每触 −1 exact, 模拟 legacy 173 < 阈值 178)。
也就是说, 这些件的价值全在**不该 fire 的时候不 fire**, 而测试只钉住了"该 fire 时会 fire"。
现在把词表放宽或把边界拆掉, 1654 条测试**全绿**; 唯一能发现的途径是有人记得手工重跑
`eval/u6_calibrate_signals`, 而那不是闸, 是纪律。

建议 (不在本审计职责内实施): 给 `test_routing_signals.py` 补一组阴性参数化 —— C+4 位、
嵌套 ASCII 串里的码/变量、以及一条"词表里每一条都必须能在 VARIABLE_INDEX / 结构词汇白名单
里找到出处"的正向白名单闸 (取代黑名单)。

### F-02 (中) 组量闸的**另一半与另一方向**无对照

存活变异: **A12** (只查 dev 不查 heldout)、**A13** (`!=`→`<`, 组变大不拦)。

`test_dev_group_size_must_match_the_percentage_denominator` 把 `dev` 改成 `n=11` —— 一个组、一个
方向。于是: (a) `heldout` 组量漂移无人拦, 而条款 2 的 `heldout_pct` 分母写死 `GROUP_N=12`,
组量变了那个百分比就失义; (b) 组量**变大**同样无人拦。

第二道防线: `run_routing_eval.load_gold` 的 `EXPECTED_GROUP_SIZES` 会在产出 run 时先拦一次
(G08 被杀证明它有锚)。所以这不是"能直接翻结论"的洞, 而是"判定件自己的独立校验只兑现了一半"。

### F-03 (中) 三遍纪律的对照只做了一臂、一个方向

存活变异: **A16** (`u6_gate_verdict` 只查 baseline 份数)、**B05** (`u6_answer_verdict` `!=`→`<`)。

`test_input_validation_needs_three_each` 传 `validate_inputs(BASE[:2], BASE)` —— 只短了 baseline
一臂; after 臂 (**正被判定的那一批**) 传两份会照样放行。答题侧同理: 只测了"少于 3 份", 没测
"多于 3 份"。

### F-04 (中) 答题侧两处"合取/并集的另一半"各缺一格

存活变异: **B27**、**B33**。

- **B27**: `stable_moved = set(cost) | set(gain)` 丢掉 gain 半仍全绿。专测
  `test_dominance_only_ids_names_what_the_worst_bound_ruler_added` 的两道题 (q1/q2) **都在 cost 侧**,
  gain 侧的"稳定半已收 ⇒ 不算支配独有"这条从未被量过。后果: 有收益的批次会把 gain 侧的题
  错报进 `dominance_only_ids`, 而这一格正是 U5 §9-1 要求"判词有多少压在最坏界尺子上"的拆分依据。
- **B33**: `divergent = abs(agg)>eps and abs(net)>eps and 符号相反` 丢掉 **agg 半**仍全绿。
  专测 `test_divergent_false_when_one_reading_is_zero` 构造的是 `paired_net_pt == 0` 且
  `aggregate != 0`；镜像形态 (agg 为 0 而 net 非 0) 没有。**该测试的 docstring 自称覆盖
  "去掉非 0 判"**, 实测只覆盖两半里的一半 —— 这种"文档比测试宽"的地方最值得记一笔。

### F-05 (中) `_norm` 是自检闸的量尺, 却不在生产路径上

存活变异: **C12**。

`routing_signals._norm` (NFKC + lower) 在本模块内**没有任何调用点** —— `_cdisc_signal` 走的是
内联的 `_nfkc(q)` + `.lower()`。`_norm` 的唯一消费者是测试
`test_terms_are_already_in_matching_normal_form`。于是删掉 `_norm` 里的 `.lower()`:
生产行为一字不变 (故不红), 但那条自检闸从此接受大写词条 —— 而大写词条正是它存在的理由
(C05 单独施加会红, 见 §5 探针 1)。

**这是一处"闸与被测对象脱钩"**: 自检量的是一个副本, 副本改了没人知道, 而副本一改, 原本能杀 C05
的那道闸就失效了。

### F-06 (中) 通道③ 的工厂接线无对照

存活变异: **C26** (`build_signals` 不再把 `settings.study_aliases_path` 传给 `StudyLookup`)。

`test_build_signals_tolerates_a_missing_alias_table` 只断言"缺别名表时工厂不抛"; 没有一条断言
**别名表在场时它真的被读进来了**。而 `StudyLookup.stats()` 的 docstring 已经点名了这个坑:
"别名 0 条 = 通道③完全没通电" 与 "别名表加载成功" 在外部表现一致。通道③ 同时是 `strong_hit`
的强通道之一 (E02 被杀), 它整条静默空转 ⇒ study 侧信号覆盖面缩水而所有测试全绿。

### F-07 (中) ②a「多 token」语义只靠一次 token 去重保障, 无对照

存活变异: **E30** (`tokens = list(dict.fromkeys(...))` → `list(...)`)。

去重一拆, 同一个 token 在题面里出现两次就让 `len(tokens) >= 2` 成立, 交集退化成该单 token 的
命中集 ⇒ **弱通道②b 的形态从 ①②a③ 的后门走成了"强通道"**。这正是 G1 判死的那条路的变形
(Task 9 实测: 弱通道每触一次 −1 exact)。实证见 §5 探针 2。

### F-08 (中) 标定台的探针与出口 rc 无对照

存活变异: **F09 / F10 / F11 / F23 / F24**, 外加 **F18**。

- **F09** 探针不看方向 (任意理由都算"信号活着")、**F10** 探针异常按命中计 —— 两条都让规则 (c)
  的 `detect` 读法虚高, 而 (c) 正是"无死信号"这条预登记选择规则的操作性读法。
- **F11** 重放 fallback 守卫拆除 —— 模块 docstring 明说"一次静默 fallback 在计数上与一次 widen
  无法区分", 该守卫却无对照 (第二道: `load_base_preds` 的非法 pred 闸有锚, 见 F08b)。
- **F18** 规则 (c) `all`→`any`: `test_rule_c_dead_signal_fails` 用的 `Silent()` 让**两个**信号都死,
  `any` 与 `all` 同为 False ⇒ "只死一个信号"的形态从未被量。
- **F23** `sim_preds` 混进 `--json-out` 落盘产物 (中间量进证据件) 无对照。
- **F24** `main()` 的 `return 0 if report["accepted"] else 1` 改成恒 0 仍全绿 —— **标定台的出口 rc
  没有任何测试**, 而复跑/CI 正是靠 rc 判断这版词表是否被采纳。

### F-09 (中) 三遍稳定性统计无判别力对照

存活变异: **G28** (`len({...}) == 1` → `>= 1`)。

`stability: N/M 题三遍判定一致` 这一行是要被引用的取证数字, 但测试只断言 `"stability:" in out`
(见 `test_default_runs_is_three_and_needs_no_flag`), 没有一条断言那个 **N 的值**。把判据改成恒真,
这行就永远打印 "254/254 三遍一致" —— 一个恒报满分的稳定性仪器, 全绿。

### F-10 (中) 回执里 `routing=LLM(light)/forced` 判词无对照

存活变异: **H12**。

源码注释记着这处曾经的缺陷: "corpus 曾硬编码 auto: 强制档跑批的屏幕与日志因此自称 auto"。
`signal_layer=` 那一格修好后有了专测 (H11 被杀), 但**同一行里的 `routing=` 判词**至今无对照 ——
把它写死成 `LLM(light)`, 强制档跑批的回执会再次自称走了 LLM 路由。同一类缺陷、同一行、只修了一半。

### F-11 (低) 产物出处告警的阴性对照缺一格

存活变异: **A09** (`shared` 由 `&` 改 `|`)。

两条相关测试分别是"两批同 sha ⇒ 告警"与"两批都 unknown ⇒ 不告警"; 缺的是**"两批 sha 不同 ⇒
不告警"**。改成并集后, 只要两批各自有版本号, 告警就恒响 —— 一条恒响的告警等于没有告警
(而它正是 I-2 的弱形态探测器)。只告警不进 rc, 故记低。

### F-12 (中) 产物 meta 校验的析取另一半 —— 实测是**放行**, 不是错话术

存活变异: **A17** (`"meta" not in r or not r["meta"].get("generated_at")` 只留前半)。

`test_input_validation_needs_meta` 用 `del b[0]["meta"]` —— 只打前半。我原以为后半失守顶多换成
一条错话术 (指望批内去重闸接住), **实测推翻了这个推断** (§5 探针 3): 三份里只要有**一份**
`generated_at` 为空串, 另两份时戳互不相同, 去重闸就不响, **整批直接通过**。

`generated_at` 是 run json 里唯一的跑批时刻凭证, 也是 I-2 批内去重闸的全部原料 —— 一份没有时刻的
run 被当成合法证据收下, 且此后它与任何一份 run 都"不重复"。故记中而非低。

### F-13 (低) I-2 拷贝闸合取的第一半无阴性对照

存活变异: **A19**。

`test_input_validation_same_content_rejected` 用 `deepcopy(BASE)` (summary 与 meta 同时相同),
`test_same_summary_but_different_run_is_not_rejected` 覆盖了 meta 半; 缺的是"meta 相同而 summary
不同 ⇒ 不该拦"。实务上 `generated_at` 是微秒时戳, 该形态几乎构造不出来 ⇒ 假阳性面接近零, 记低。

### F-14 (低) 段索引去重 / 补充 gold 空文件 / debug flag 组合 三处无 fixture

- **E25** `for seg in set(segs)` → `for seg in segs`: OID 里出现重复段时, 同一张卡会被重复计进
  `_segment_index`, 把 `_MAX_CARDS_PER_MATCH` 的计数灌高 ⇒ 本该 fire 的命中被 cap 挡掉。
  合成 catalog 里没有重复段的 item。
- **G35** `load_supplement` 的空文件守卫拆除仍全绿 (docs gold 侧的同款守卫有锚 —— G08 被杀)。
  第二道: 空补充集会让 `EXPECTED_GROUP_SIZES` 的 legacy 数对不上。
- **G29** `if args.runs >= 3 and not args.allow_nonstandard_runs` 丢掉后半仍全绿:
  `test_nonstandard_runs_flag_suppresses_stability_and_forces_nonzero_rc` 用的是 `--runs 1`,
  于是 `--runs 3 --allow-nonstandard-runs` 这个组合 (调试 flag 的 "rc 恒非 0" 承诺) 无人守。

### F-15 (低) 分层守卫的外层不可观测

存活变异: **D02** (丢掉 `signals is not None` 半)。

丢掉后 `None.widen_reason(...)` 抛 `AttributeError` → 被旁路吞掉 → 返回值与原来**逐位相同**,
但每题多一条 `signal_layer_error` warning。`decide_corpus` docstring 承诺 "signals=None (默认) 时
逐位等于裸 route_corpus" —— 这条承诺的**返回值面**有测试, **日志面**没有。

---

## 5. 后果实证 (不只写推理)

三条 finding 的后果用**实际施加变异 + 极小断言**量了一遍, 而不是只靠读代码。探针脚本与变异
harness 同源 (同一套 purge / compile / 还原), 结束时 `git status` 自检为空。**其中探针 3 的结果
推翻了我原本的推断, 见下。**

### 探针 1 / 1b — F-05: 自检闸能被"改一个生产不用的函数"解除武装

```
== 探针 1: C05(词表混入大写词条) 单独 —— 自检闸应当红 ==
self-check offenders: ['SDTM']
self-check verdict : FAIL(会红)

== 探针 1b: C05 + C12(_norm 丢 lower) 复合 —— 自检闸是否被解除武装 ==
self-check offenders: []
self-check verdict : PASS(全绿)
```

读法: 单独塞一个大写词条, `test_terms_are_already_in_matching_normal_form` 会红 (闸有效);
**再顺手删掉 `_norm` 的 `.lower()`** —— 一个生产路径根本不调用的函数 —— 同一个闸就全绿了。
两处改动各自都不影响生产行为, 合在一起就把红线词表的归一化纪律注销掉。

### 探针 2 — F-07: 重复一次 token 就把弱通道抬成强通道

用合成 catalog (两张卡同属段 `QST`, 与 `test_study_lookup.py` 同款零真实 OID/label):

```
[基线]  single : False   repeat : False
[E30]   single : False   repeat : True
```

读法: 基线下"提一次 token"与"提两次同一个 token"都**不**触发 `strong_hit` (弱通道②b 不算依据,
G1 裁定)。去掉 token 去重后, 同一个 token 重复出现就让 `len(tokens) >= 2` 成立, ②a 的交集退化成
该单 token 的命中集 ⇒ `strong_hit` 变 True。**G1 判死的那条路从重复词这个后门走通了。**

### 探针 3 — F-12: 后果比我预估的重 (推断被实测推翻)

```
[基线]  SystemExit: baseline 第 1 份 run 缺 meta.generated_at — 先用 Task 1 修缮后的 ... 重产
[A17]   NO ERROR (放行)
```

我原先推断 A17 只会"换成一条错话术"(以为批内去重闸会接住)。**实测是直接放行**: 只要三份里
有**一份** `generated_at` 为空串, 其余两份时戳互不相同 ⇒ 去重闸不响 ⇒ 整批通过。
`generated_at` 是 run json 里唯一的跑批时刻凭证, 也是批内去重闸的全部原料。
⇒ **F-12 由「低」上调为「中」**。(键**完全缺失**时会在后面那行抛 `KeyError` —— 消息来自无关代码,
同样不是这条守卫在说话。)

---

## 6. 复跑

**基线 (本报告全部判定的参照点)**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
./.venv/bin/python -m pytest -o addopts="-q" -p no:warnings      # 1654 passed
```

**单条变异的手工复跑配方** (三步; 与 harness 逐位同流程)

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
# 1) 打补丁 (以 F-01 的 C06 为例: 往冻结词表里塞一个临床概念词)
#    编辑 server/routing_signals.py, 在 CDISC_STRUCT_TERMS 的 "sdtm", 之后加一行 "有害事象",
# 2) 清 pycache + compile 前置检查 (缺这两步会得到假阴性/假还原)
find eval server scripts -name __pycache__ -type d -exec rm -rf {} +
./.venv/bin/python -m py_compile server/routing_signals.py
# 3) 跑对应测试 (存活 = 全绿)
./.venv/bin/python -m pytest -o addopts="" -q --tb=no -rf -p no:warnings \
    scripts/tests/test_routing_signals.py scripts/tests/test_federation.py \
    scripts/tests/test_main_signal_wiring.py scripts/tests/test_u6_calibrate_signals.py
# 4) 还原并自检
git checkout -- server/routing_signals.py && git status --porcelain -- server eval
```

**每个源文件的快集** (主判用; SURVIVED 一律再用全量复判):

| 源文件 | 快集测试文件 |
|--------|--------------|
| `eval/u6_gate_verdict.py` | `test_u6_gate_verdict` |
| `eval/u6_answer_verdict.py` | `test_u6_answer_verdict` |
| `server/routing_signals.py` | `test_routing_signals` `test_federation` `test_main_signal_wiring` `test_u6_calibrate_signals` `test_run_eval_flags` `test_run_eval_federated` |
| `server/federation.py` | 上一行 + `test_federation_api` `test_router_structured` `test_run_routing_eval` |
| `server/study_lookup.py` | `test_study_lookup` `test_routing_signals` `test_main_study_lookup_wiring` `test_run_eval_federated` `test_study_corpus` `test_federation` |
| `eval/u6_calibrate_signals.py` | `test_u6_calibrate_signals` |
| `eval/run_routing_eval.py` | `test_run_routing_eval` `test_u6_calibrate_signals` `test_u3_gold_redline` `test_run_eval_flags` |
| `eval/run_eval.py` | `test_run_eval_{flags,federated,judge,doc_channel}` `test_main_signal_wiring` `test_run_routing_eval` `test_u6_calibrate_signals` |

**存活变异的确切补丁**见 §8 附录 (逐条 `old` → `new`), 照抄即可复现 SURVIVED。

**红线自检**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
./.venv/bin/python scripts/leakscan_evidence.py evidence/step_u6_audit_mutation.md --min-len 12
./.venv/bin/python scripts/leakscan_evidence.py evidence/step_u6_audit_mutation.md --min-len 8 --show 20
```

---

## 7. 收尾自检

| 项 | 命令 | 结果 |
|----|------|------|
| 目标源文件净树 | `git status --porcelain -- eval server scripts` | 空 |
| 全量复跑 | `./.venv/bin/python -m pytest -o addopts="-q" -p no:warnings` | **1654 passed** (同冻结期基线) |
| 题面泄漏闸 | `leakscan_evidence.py ... --min-len 12` | **CLEAN rc=0** (306 needles / 6 个 gold set 全可读) |
| 泄漏闸人工判读 | 同上 `--min-len 8 --show 30` | 24 条命中**全部来自 `eval/test_set_v3.yml`** (公开英文 CDISC 题集, 本身进 git), 且全部是通用英文词片段 (`question` / `standard` / `structur` / `summary` / `including` / `single` …); **四个 `data/study/` 的 gitignored 题集零命中** —— 正是脚本 docstring 点名的通用词假阳性类, 非泄漏 |

38 条 SURVIVED 的全量复判各自跑完一次 1654 条, 每次 `restored_clean=true`; 加上这一次收尾复跑,
"改坏 → 测试全绿 → 还原干净"这条链上每一步都有可复跑的凭证。

---

## 8. 附录: 存活变异的确切补丁 (38 条)

照抄即可复现 SURVIVED。锚点在各文件中均**唯一出现一次** (harness 对此有自检: 出现 0 次或 >1 次一律 ANCHOR_FAIL, 不静默跳过)。

### A09 — `eval/u6_gate_verdict.py`

并集/交集: shared 由 & 改 | (I-2 弱形态告警恒响)

```diff
- shared = (sha.get("baseline", set()) & sha.get("after", set())) - {"unknown"}
+ shared = (sha.get("baseline", set()) | sha.get("after", set())) - {"unknown"}
```

### A12 — `eval/u6_gate_verdict.py`

合取半: 组量闸只查 dev 不查 heldout

```diff
-             for name in ("dev", "heldout"):
-                 if groups[name]["n"] != GROUP_N:
+             for name in ("dev",):
+                 if groups[name]["n"] != GROUP_N:
```

### A13 — `eval/u6_gate_verdict.py`

组量闸 != -> < (组变大不拦)

```diff
-                 if groups[name]["n"] != GROUP_N:
+                 if groups[name]["n"] < GROUP_N:
```

### A16 — `eval/u6_gate_verdict.py`

合取半: 三遍纪律只查 baseline 份数

```diff
-     if len(base) != 3 or len(after) != 3:
+     if len(base) != 3:
```

### A17 — `eval/u6_gate_verdict.py`

合取半: meta 在场但 generated_at 空不再拦

```diff
-             if "meta" not in r or not r["meta"].get("generated_at"):
+             if "meta" not in r:
```

### A19 — `eval/u6_gate_verdict.py`

合取半: I-2 拷贝闸丢掉 summary 逐字相同那一半

```diff
-     if bdump & adump and {r["meta"]["generated_at"] for r in base} & {
-             r["meta"]["generated_at"] for r in after}:
+     if {r["meta"]["generated_at"] for r in base} & {
+             r["meta"]["generated_at"] for r in after}:
```

### B05 — `eval/u6_answer_verdict.py`

三遍纪律 != -> < (四遍也放行)

```diff
-     if len(runs) != 3:
+     if len(runs) < 3:
```

### B22 — `eval/u6_answer_verdict.py`

对调: 稳定半 cost/gain 的差式符号互换

```diff
-     cost = {i: stable_a[i] - stable_b[i] for i in stable_half["confirmed_cost_ids"]}
-     gain = {i: stable_b[i] - stable_a[i] for i in stable_half["confirmed_gain_ids"]}
+     cost = {i: stable_b[i] - stable_a[i] for i in stable_half["confirmed_cost_ids"]}
+     gain = {i: stable_a[i] - stable_b[i] for i in stable_half["confirmed_gain_ids"]}
```

### B27 — `eval/u6_answer_verdict.py`

并集半: stable_moved 只算 cost 半

```diff
-     stable_moved = set(cost) | set(gain)
+     stable_moved = set(cost)
```

### B33 — `eval/u6_answer_verdict.py`

合取半: divergent 丢掉 agg 非零那一半

```diff
-     divergent = abs(agg) > _EPS and abs(net) > _EPS and (agg > 0) != (net > 0)
+     divergent = abs(net) > _EPS and (agg > 0) != (net > 0)
```

### C06 — `server/routing_signals.py`

词表混入临床概念词 (红线: 零临床概念)

```diff
- CDISC_STRUCT_TERMS = (
-     "sdtm",
+ CDISC_STRUCT_TERMS = (
+     "sdtm",
+     "有害事象",
```

### C07 — `server/routing_signals.py`

CT 码位数 5,6 -> 4,6 (放宽形态)

```diff
- _CT_CODE_RE = re.compile(r"(?<![A-Za-z0-9_])C\d{5,6}(?![A-Za-z0-9_])")
+ _CT_CODE_RE = re.compile(r"(?<![A-Za-z0-9_])C\d{4,6}(?![A-Za-z0-9_])")
```

### C08 — `server/routing_signals.py`

CT 码正则去掉两侧 ASCII 边界 (子串误触)

```diff
- _CT_CODE_RE = re.compile(r"(?<![A-Za-z0-9_])C\d{5,6}(?![A-Za-z0-9_])")
+ _CT_CODE_RE = re.compile(r"C\d{5,6}")
```

### C09 — `server/routing_signals.py`

变量形态正则去掉左边界

```diff
-     rf"(?<![A-Za-z0-9_])(?:(?:{_alt(_SDTM_DOMAIN_CODES)})(?:{_alt(_SDTM_VAR_ROOTS)})"
+     rf"(?:(?:{_alt(_SDTM_DOMAIN_CODES)})(?:{_alt(_SDTM_VAR_ROOTS)})"
```

### C10 — `server/routing_signals.py`

变量形态正则去掉右边界

```diff
-     rf"|{_alt(_SDTM_STANDALONE_VARS)})(?![A-Za-z0-9_])"
+     rf"|{_alt(_SDTM_STANDALONE_VARS)})"
```

### C11 — `server/routing_signals.py`

_alt 长词优先排序取消 (自称只影响回溯)

```diff
-     return "|".join(sorted(words, key=len, reverse=True))
+     return "|".join(sorted(words, key=len, reverse=False))
```

### C12 — `server/routing_signals.py`

_norm 丢掉 lower (词表比对大小写敏感)

```diff
-     return _nfkc(s).lower()
+     return _nfkc(s)
```

### C23 — `server/routing_signals.py`

build_signals catalog 缺失不再抛 (半装配静默通过)

```diff
-         if not catalog.exists():
-             raise FileNotFoundError(
+         if False:
+             raise FileNotFoundError(
```

### C25 — `server/routing_signals.py`

build_signals 改成可返回 None (调用侧 None 语义 = 未装配)

```diff
-     return RoutingSignals(study_lookup)
+     return RoutingSignals(study_lookup) if study_lookup else None
```

### C26 — `server/routing_signals.py`

别名表路径不再传入 (通道③ 静默空转)

```diff
-         study_lookup = StudyLookup.from_paths(catalog, settings.study_aliases_path)
+         study_lookup = StudyLookup.from_paths(catalog, None)
```

### D01 — `server/federation.py`

合取半: 丢掉 corpus in (cdisc,study) 半 (both 也送去问信号层)

```diff
-     if signals is not None and corpus in ("cdisc", "study"):
+     if signals is not None:
```

### D02 — `server/federation.py`

合取半: 丢掉 signals 非 None 半 (未挂信号层时 AttributeError)

```diff
-     if signals is not None and corpus in ("cdisc", "study"):
+     if corpus in ("cdisc", "study"):
```

### D03 — `server/federation.py`

both 纳入纠偏范围 (both 已是最宽, 不该再问)

```diff
-     if signals is not None and corpus in ("cdisc", "study"):
+     if signals is not None and corpus in ("cdisc", "study", "both"):
```

### D16 — `server/federation.py`

析取半: JSON 定位守卫丢掉 end<=start 半

```diff
-         if start < 0 or end <= start:
+         if start < 0:
```

### E25 — `server/study_lookup.py`

段索引不去重 (重复段把 cap 计数灌满)

```diff
-             for seg in set(segs):
+             for seg in segs:
```

### E30 — `server/study_lookup.py`

token 去重取消 (dict.fromkeys 拆掉, 重复 token 灌 single_token)

```diff
-         tokens = list(dict.fromkeys(_LATIN_TOKEN_RE.findall(query)))
+         tokens = list(_LATIN_TOKEN_RE.findall(query))
```

### F08 — `eval/u6_calibrate_signals.py`

基线 pred 非法守卫拆除 (重放 fallback 与一次拓宽同形)

```diff
-     bad = sorted(i for i, p in preds.items() if p not in VALID_CORPORA)
+     bad = sorted(i for i, p in preds.items() if p not in (*VALID_CORPORA, "junk"))
```

### F09 — `eval/u6_calibrate_signals.py`

探针不看方向 (任意理由都算信号活着)

```diff
-         return signals.widen_reason(routed, question) == WIDEN_REASON_BY_CORPUS[routed]
+         return signals.widen_reason(routed, question) is not None
```

### F10 — `eval/u6_calibrate_signals.py`

对调: 探针异常时按命中计 (坏信号层被读成活着)

```diff
-     except Exception:
-         return False
+     except Exception:
+         return True
```

### F11 — `eval/u6_calibrate_signals.py`

重放 fallback 守卫拆除 (静默 fallback 与一次 widen 同形)

```diff
-         if fallback:
-             raise ValueError(
+         if False:
+             raise ValueError(
```

### F18 — `eval/u6_calibrate_signals.py`

规则 (c) all -> any (一个信号活着就算无死信号)

```diff
-             "pass": all(n >= 1 for n in counts.values()), "counts": counts,
+             "pass": any(n >= 1 for n in counts.values()), "counts": counts,
```

### F23 — `eval/u6_calibrate_signals.py`

落盘产物混入 sim_preds 中间量

```diff
-             json.dumps({k: v for k, v in report.items() if k != "sim_preds"},
+             json.dumps({k: v for k, v in report.items()},
```

### F24 — `eval/u6_calibrate_signals.py`

rc 与 accepted 脱钩 (恒 0)

```diff
-     return 0 if report["accepted"] else 1
+     return 0
```

### G11 — `eval/run_routing_eval.py`

合取半: score_run 的 passed 丢掉 fatal 半

```diff
- "passed": acc >= EXACT_THRESHOLD and not fatal_items}
+ "passed": acc >= EXACT_THRESHOLD}
```

### G28 — `eval/run_routing_eval.py`

稳定性判据 ==1 -> >=1 (恒 100% 稳定)

```diff
-         if len({p[g["id"]] for p in per_run_preds}) == 1
+         if len({p[g["id"]] for p in per_run_preds}) >= 1
```

### G29 — `eval/run_routing_eval.py`

合取半: 稳定性行的守卫丢掉 allow_nonstandard 半

```diff
-     if args.runs >= 3 and not args.allow_nonstandard_runs:
+     if args.runs >= 3:
```

### G35 — `eval/run_routing_eval.py`

补充 gold 的空文件守卫拆除 (闸悄悄变松)

```diff
-     if not items:  # 空文件 / 全被注释掉: 静默返回 [] = 闸悄悄变松
-         raise ValueError(f"路由补充 gold 为空: {path} —— 闸口不完整, 拒绝继续")
+     if False:
+         raise ValueError(f"路由补充 gold 为空: {path} —— 闸口不完整, 拒绝继续")
```

### H12 — `eval/run_eval.py`

对调: 回执行的 routing 判词与 corpus 取值脱钩 (强制档自称 LLM)

```diff
- f"routing={'LLM(light)' if args.corpus == 'auto' else 'forced'}"
+ f"routing={'LLM(light)'}"
```

---

## 9. 冻结期终态存活清单 (复验 @ f2244e7)

补杀波 (`f2244e7`, +45 测试) 之后, 用**同一套变异集**对新测试面重跑了一遍。本节是复验结果与
终态存活清单; §0-§8 保持复验前的原貌不动 (那是补杀波的输入, 改了就对不上账)。

### 9.1 复验条件

| 项 | 值 |
|----|----|
| 复验 HEAD | `f2244e7` (`test(u6-t12): 补杀波 — 抽检 B 29 条存活变异全部转 KILLED`) |
| 复验基线 | 净树 + 全量 **1699 passed in 38.08s** (原审计基线为 1654) |
| 变异集 | 原 38 条 SURVIVED 全部重跑 (等价 8 条**未抽样, 全跑**) + 2 条新增 |
| harness | scratchpad 原件仍在, 未重建 |

**等价 8 条为什么全跑而不抽 2 条**: 我的等价论证是对**返回值**成立的; 补杀波若补了以调用探针 /
日志面为观测点的测试 (D01/D03 尤其可能), 等价关系就会被更强的观测面打破 —— 那种情况下"抽样
通过"会漏掉真实的转杀。全跑只多花几秒, 而且只有全跑才配得上"终态清单"这四个字。

### 9.2 harness 在新树上的自证 (先证仪器)

测试面换了, 仪器必须重证一次, 不能沿用昨天的结论:

| id | 期望 | 实测 @ f2244e7 |
|----|------|----------------|
| S0 哨兵语法错 | COMPILE_FAIL | `COMPILE_FAIL: SyntaxError: '(' was never closed` ✅ |
| S1 阳性对照 | KILLED | 11 条红 ✅ |
| S2 阴性对照 (只改注释) | SURVIVED | 全绿 ✅ |
| S3 锚点不存在 | ANCHOR_FAIL | `anchor occurs 0 times` ✅ |

### 9.3 A17 的锚点被加固改掉了 —— 重导, 外加一条回退闸

补杀波唯一的源码改动落在 A17 那一行, 原锚点因此**在新源码里不存在**。这是变异复验最容易出事的
一格: 锚点消失时若 harness 静默跳过, 那条变异会被记成"已修"而实际从未施加。这里 S3 那道
ANCHOR_FAIL 自检正是为它准备的。处理:

- **A17 (重导)**: 在加固后的新行上施加**同一语义**的变异 (丢掉 `generated_at` 那一半)
  → **KILLED** by `test_input_validation_rejects_a_blank_generated_at`。
- **A17b (新增)**: 把加固**整条回退**成补杀波之前的写法
  → **KILLED** by 同一条测试。⇒ 加固自身有锚, 回退即红 (印证补杀波 commit message 的说法)。

### 9.4 复验结果: 39 条 → KILLED 30 / SURVIVED 9

**29 条 finding 变异全部转 KILLED**, 逐条列出杀它的**新**测试:

| id | 原 finding | 杀它的新测试 |
|----|-----------|--------------|
| A09 | F-11 | `test_distinct_git_revs_do_not_trigger_the_shared_warning` |
| A12 / A13 | F-02 | `test_group_size_gate_covers_both_groups_and_both_directions` |
| A16 | F-03 | `test_input_validation_needs_three_in_the_after_batch_too` |
| A17 | F-12 | `test_input_validation_rejects_a_blank_generated_at` |
| A19 | F-13 | `test_shared_generated_at_alone_is_not_a_copy_error` |
| B05 | F-03 | `test_rejects_arm_with_more_than_three_runs` |
| B27 | F-04 | `test_dominance_only_ids_subtracts_the_gain_side_too` |
| B33 | F-04 | `test_divergent_false_when_the_aggregate_reading_is_zero` |
| C06 | F-01 | `test_terms_contain_no_clinical_concepts` + `test_frozen_lexicon_and_patterns_are_literal` |
| C07 / C08 | F-01 | `test_ct_code_shape_stays_silent_outside_the_frozen_bounds` + 冻结闸 |
| C09 / C10 | F-01 | `test_variable_shape_stays_silent_inside_a_longer_ascii_run` + 冻结闸 |
| C12 | F-05 | `test_norm_is_nfkc_plus_lowercase` |
| C26 | F-06 | `test_build_signals_actually_loads_the_alias_table_when_present` |
| D02 | F-15 | `test_decide_corpus_without_signals_is_silent_too` |
| E25 | F-14 | `test_repeated_oid_segment_is_counted_once_against_the_cap` |
| E30 | F-07 | `test_repeating_one_token_does_not_promote_the_weak_channel` |
| F09 / F10 | F-08 | `test_a_broken_signal_layer_never_counts_as_alive` |
| F11 | F-08 | `test_simulate_refuses_a_pred_that_replays_into_a_fallback` |
| F18 | F-08 | `test_rule_c_fails_when_only_one_of_the_two_signals_is_alive` |
| F23 | F-08 | `test_json_out_excludes_the_intermediate_sim_preds` |
| F24 | F-08 | `test_main_rc_follows_accepted` |
| G28 | F-09 | `test_stability_counts_only_ids_that_agree_across_all_three_runs` |
| G29 | F-14 | `test_nonstandard_flag_still_forces_nonzero_rc_at_three_runs` |
| G35 | F-14 | `test_supplement_gold_empty_file_raises` |
| H12 | F-10 | `test_federated_receipt_routing_word_follows_the_corpus` |
| A17b | (新增回退闸) | `test_input_validation_rejects_a_blank_generated_at` |

**F-01..F-15 十五条 finding 全部落地**, 无一条留作 known limit。

### 9.5 终态存活清单 (9 条)

9 条仍存活, **全部再用全量 1699 条复判过** (`restored_clean` 逐条 true, 输出皆 `1699 passed`):

| id | 类别 | 复验结论 |
|----|------|----------|
| B22 | 等价 | 论证仍成立 —— 支配并集必逐键覆盖稳定半, 且额相等 |
| C11 | 等价 | 论证仍成立 —— 交替式顺序不改 `bool(search)` |
| C23 | 等价 | 论证仍成立 —— 拆守卫后 `read_text` 抛同类同路径异常 |
| C25 | 等价 | 论证仍成立 —— `StudyLookup` 恒真, 取不到 None |
| D01 | 等价 | 论证仍成立 —— 内层 `widen_reason("both")` 恒 None, 返回值不变 |
| D03 | 等价 | 同 D01 |
| D16 | 等价 | 论证仍成立 —— 两种破法同落 `except` → 同一 fallback |
| G11 | 等价 | 论证仍成立 —— `score_run["passed"]` 生产无消费者 |
| **F08** | **非等价 (弱变异)** | 仍存活, 详见 9.6 |

⇒ **非等价存活 K = 1** (F08), 不是 0。这一条我按原样报出来, 不并进等价项。

### 9.6 F08 的残留: 守卫会响, 但"哪些 pred 算合法"没有锚

`u6_calibrate_signals.load_base_preds` 的非法 pred 守卫本体**有锚** —— 整条拆掉 (F08b) 在补杀波
前后都是 KILLED (`test_load_base_preds_raises_on_invalid_pred`)。存活的是它的**合法集**:

| 变异 | 方向 | 结果 |
|------|------|------|
| F08 | 放宽: `p not in (*VALID_CORPORA, "junk")` | SURVIVED |
| **F08c** (本次新增) | 收紧: `p not in ("cdisc", "study")` —— 连合法的 `both` 也拒 | **SURVIVED** |

两个方向都不红 ⇒ 该守卫的合法集**完全没有被钉住**, 现有测试只证明"某个非法值会被拒"。

**严重度: 低, 且方向安全。** F08c 那种收紧形态一跑真实基线就会当场炸 (模块 docstring 自己算过:
legacy 181 题里那 2 道不 exact 的题 pred 必为 `both`) —— 是 fail-loud, 不是静默给错结论;
F08 那种放宽形态需要 run json 里恰好出现 `"junk"` 这个字面值才会显形。

修法 (一行, 若认为值得): 把守卫的合法集断言成字面 —— 与 C06/C07 那条
`test_frozen_lexicon_and_patterns_are_literal` 同形。**我不主张现在就改**: 本条既 fail-loud 又
需要构造性输入才触发, 和补杀波刚关掉的那 29 条不是一个量级。列在这里是为了不留口头约定。

### 9.7 一条不算 finding 的观察 (F-01 的修法形状)

C06-C10 这五条现在由两层拦住: 语义层 (黑名单补齐词根 / 阴性对照参数化) + **冻结层**
(`test_frozen_lexicon_and_patterns_are_literal` 把 8 条词表与两条正则钉成字面)。冻结层是这轮
真正的主力 —— 任何改动都红, 不依赖黑名单猜得全不全。

需要说清楚的是它**改变了缺口的形状而不是消灭了语义判据**: 将来若有一次正当的重新标定, 改词表的人
必须同时改那条字面断言, 而那一刻语义上唯一的守门人仍是黑名单。这不是缺陷 —— 在"词表冻结"这个
前提下, 冻结闸正是对的机制 (它把"改了没人知道"变成"改了必须显式声明")。记在这里只是让下一个
重新标定的人知道: **红的那一刻不是阻碍, 是要求你把新词表的出处写进 review**。

### 9.8 复验收尾自检

| 项 | 命令 | 结果 |
|----|------|------|
| 目标源文件净树 | `git status --porcelain -- eval server scripts` | 空 |
| 复验基线 / 收尾复跑 | `./.venv/bin/python -m pytest -o addopts="-q" -p no:warnings` | **1699 passed** |
| 9 条存活的全量复判 | harness `tests: ["ALL"]` | 9/9 皆 `1699 passed`, `restored_clean` 全 true |
| harness 自证 | 见 §9.2 | 四条对照全部成立 |
