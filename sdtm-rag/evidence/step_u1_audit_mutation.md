# U1 Task 9 — 独立抽检方 B: 四闸物理变异测试

> 抽检方: test-engineer (规则 D 隔离, 与实现方 / 抽检方 A 不同 session)
> 日期: 2026-08-12
> 对象: `eval/docs_gold_gates.py` 闸 A/B/C/D + `eval/gold_semantic_check.py` `--mode selfsuff`
> 方法: 把被检函数体首行插入 `return []` (恒绿), 跑**全量**单测, 记录红了几条 / 哪几条。
> 红线: 本文件进 git — 只给函数名 / 测试名 / 计数, 零 chunk 正文、零日文长串、零人名。

## 0. 基线与环境

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
git status --porcelain          # 空
./.venv/bin/python -m pytest -p no:warnings --tb=short
```

基线实测末行: `1119 passed in 26.23s` (全量 26s, 故每次变异都跑全量而非只跑单文件)。

变异手法说明: **插入早退 `return []` 而不是删除函数体**。原因有二 ——
(1) 保留原体 ⇒ 模块级 import (`lint_gold` 等) 仍被引用, 不会引入与闸无关的 NameError;
(2) 仓内 `scripts/tests/` 74 个文件**无** ruff/flake8/py_compile 类 lint 测试
(实测 `grep -rln "ruff\|flake8\|pylint\|compileall\|py_compile" scripts/tests/` 零命中),
故"不可达代码"不会制造假阳性失败。⇒ 变异后的每一条红都可归因于闸本身。

失败清单采集命令 (`-ra` 已在 pyproject `addopts`, 会打印 short summary):

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no 2>&1 | grep -E "^FAILED|passed|failed"
```

⚠ 不加 `-q`: `addopts = "-ra -q"` 已含一个, 再加会变 `-qq` 并关掉汇总行。

---

## 1. 闸 A `gate_gold_unique` (:50)

变异: 在 `def gate_gold_unique(...)` 下首行插 `return []`。
结果: **`4 failed, 1115 passed in 25.44s`** — 非装饰品。

| # | 红掉的测试 | 类别 |
|---|-----------|------|
| 1 | `test_gate_gold_unique_flags_multi_match` | 闸 A 专属脏侧 |
| 2 | `test_fixture_dirty_side_trips_each_gate_individually` | 四维独立性 |
| 3 | `test_run_all_gates_reports_every_gate` | 聚合器 gate 集合 |
| 4 | `test_main_exit_code_1_when_findings` | CLI 退出码 + `--json` 出口 |

判定: **PASS**。闸 A 有 1 条专属脏侧断言 + 3 条聚合层断言, 恒绿必被抓。

## 2. 闸 B `gate_anchor_unique` (:58)

变异: 在函数 docstring 之后、`findings: list[GateFinding] = []` 之前插 `return []`。
结果: **`19 failed, 1100 passed in 24.86s`** — 非装饰品, 且是四道闸里断言密度最高的。

红掉的 19 条 (16 条闸 B 专属 + 3 条聚合层):

```
test_gate_anchor_unique_flags_when_anchor_appears_in_extra_chunk
test_gate_anchor_unique_flags_short_anchor
test_gate_anchor_unique_flags_missing_anchor
test_gate_anchor_unique_flags_multi_gold_with_single_anchor
test_gate_anchor_unique_flags_anchor_and_anchors_both_given
test_gate_anchor_unique_flags_anchors_length_mismatch
test_gate_anchor_unique_flags_anchor_not_in_its_own_gold
test_gate_anchor_unique_flags_anchor_overflowing_to_non_gold
test_gate_anchor_unique_flags_anchors_with_or_group
test_gate_anchor_unique_flags_scalar_anchors
test_gate_anchor_unique_flags_short_anchor_inside_anchors
test_single_gold_path_unchanged_by_anchors_feature
test_gate_anchor_unique_flags_or_only_gold_with_fabricated_anchor
test_gate_anchor_unique_flags_question_without_any_gold
test_gate_anchor_unique_flags_anchor_in_wrong_chunk
test_gate_anchor_unique_flags_misaligned_multi_gold
test_fixture_dirty_side_trips_each_gate_individually     (聚合层)
test_run_all_gates_reports_every_gate                    (聚合层)
test_main_exit_code_1_when_findings                      (聚合层)
```

值得单独记的一点: 复审文档里列的**四条 fail-open 回归** (①OR-only+捏造锚串 /
②完全无 gold / ③锚串错位到别的 chunk / ④多 gold 半数错位) **全部在红名单里**
(`flags_or_only_gold_with_fabricated_anchor` / `flags_question_without_any_gold` /
`flags_anchor_in_wrong_chunk` / `flags_misaligned_multi_gold`)。
即那四条不是注释里的声明, 是可执行断言。

判定: **PASS**。

## 3. 闸 C `gate_fact_length` (:224)

变异: 在 `def gate_fact_length(...)` 下首行插 `return []`。
结果: **`7 failed, 1112 passed in 25.11s`** — 非装饰品。

| # | 红掉的测试 | 类别 |
|---|-----------|------|
| 1 | `test_gate_fact_length_flags_short_fact` | 短 fact |
| 2 | `test_gate_fact_length_flags_missing_facts` | 缺 `expected_facts` |
| 3 | `test_gate_fact_length_flags_two_char_upper_fragment` | `_ID_SHAPED` 量词下限 |
| 4 | `test_gate_fact_length_flags_id_shaped_with_trailing_newline` | `fullmatch` vs `.match` |
| 5 | `test_fixture_dirty_side_trips_each_gate_individually` | 四维独立性 |
| 6 | `test_run_all_gates_reports_every_gate` | 聚合器 gate 集合 |
| 7 | `test_main_exit_code_1_when_findings` | CLI 退出码 + `--json` |

判定: **PASS**。

## 4. 闸 D `gate_card_unanswerable` (:242)

变异: 在函数 docstring 之后、`findings: list[GateFinding] = []` 之前插 `return []`。
结果: **`8 failed, 1111 passed in 25.33s`** — 非装饰品。

| # | 红掉的测试 | 类别 |
|---|-----------|------|
| 1 | `test_gate_card_unanswerable_ignores_navigation_file_but_still_flags_field_card` | 导航文件双向 |
| 2 | `test_gate_card_unanswerable_flags_card_covering_all_terms` | 主脏侧 |
| 3 | `test_gate_card_unanswerable_is_case_insensitive` | 大小写 |
| 4 | `test_gate_card_unanswerable_requires_two_terms` | `< 2` 守卫 |
| 5 | `test_gate_card_unanswerable_flags_scalar_probe_terms` | YAML 标量守卫 |
| 6 | `test_fixture_dirty_side_trips_each_gate_individually` | 四维独立性 |
| 7 | `test_run_all_gates_reports_every_gate` | 聚合器 gate 集合 |
| 8 | `test_main_exit_code_1_when_findings` | CLI 退出码 + `--json` |

判定: **PASS**。

**四闸小结: 0 个装饰品。** 每道闸都至少有 1 条**专属**脏侧断言 (不依赖聚合层),
且三条聚合层断言 (`fixture_dirty_side_trips_each_gate_individually` /
`run_all_gates_reports_every_gate` / `main_exit_code_1_when_findings`) 对四道闸
**全部**响应 —— 即聚合器漏掉任一加数也会被抓。

---

## 5. `gold_semantic_check.py --mode selfsuff` — 独立复现 + 三处细分变异

上一轮声称"物理变异已验证会红"。本节**不采信**该句, 独立重跑, 并把 selfsuff 拆成
**判据 / 打印 / CLI 分派 / 两条可见性行** 分别变异 —— 因为"整块删掉会红"
**推不出**"里面每个信号都有断言"。

| 变异 | 改法 | 结果 | 判定 |
|------|------|------|------|
| S1 | `self_sufficient_golds` 首行 `return []` | `8 failed, 1111 passed` | 会红, **复现成立** |
| S2 | `_print_self_sufficiency` 首行 `return 0` | `2 failed, 1117 passed` | 会红 |
| S3 | `main` 里 `if args.mode == "selfsuff"` 改 `if False and ...` | `2 failed, 1117 passed` | 会红 |
| **S4** | **删 `print(f"[selfcov] ...")` 一行** | **`1119 passed`** | **🔴 全绿 = 装饰** |
| **S5** | **删末尾 `N 处单 gold 疑似自足 / M 道多 gold 题` 汇总行** | **`1119 passed`** | **🔴 全绿 = 装饰** |
| M6 (对照) | 删 `docs_gold_gates.main` 的 `print(f"[probe] ...")` 一行 | `2 failed, 1117 passed` | 会红 |

S1 红掉的 8 条:

```
test_selfsuff_flags_gold_that_alone_covers_every_fact
test_selfsuff_flags_once_the_weak_fact_is_also_covered
test_selfsuff_threshold_boundary_is_inclusive
test_selfsuff_does_not_treat_or_side_as_multi_gold
test_selfsuff_skips_facts_with_no_countable_unit
test_selfsuff_counts_paraphrased_gold
test_main_selfsuff_mode_exits_zero_with_findings
test_main_selfsuff_output_carries_no_prose
```

S2 / S3 / M6 红掉的分别是:

```
S2, S3: test_main_selfsuff_mode_exits_zero_with_findings
        test_main_selfsuff_output_carries_no_prose
M6:     test_main_prints_probe_binding_visibility
        test_probe_binding_visibility_does_not_change_exit_code
```

顺带核实一条容易假绿的写法: `test_main_selfsuff_output_carries_no_prose` 的主张是
"输出里**没有**正文", 这类"不含"断言对**空输出**恒真 —— 若它只写 `assert 正文串 not in out`,
那么 S2 (整个打印函数不打印) 应当照绿。实测 S2 打红了它 ⇒ 该用例**另有**一条
`assert "[SELF] q1" in out` 正向断言托底。**这条写法是对的, 记下来防止后人"简化"掉。**

### 🔴 被点名的装饰信号 (S4 / S5)

`_print_self_sufficiency` 的**两条可见性输出全部零断言**:

1. `[selfcov] {qid}: ...   (! = 单 gold 自足)` —— 每道多 gold 题逐 gold 的逐 fact 分数
2. `\n{N} 处单 gold 疑似自足 / {M} 道多 gold 题 (触发线 {T}) — 本项是**排序触发器不是闸**...`

删掉任意一条, 全量 `1119 passed`, 一条不红。检索确认零断言:

```bash
grep -rn "selfcov\|疑似自足\|多 gold 题 (触发线" scripts/tests/   # 零命中
```

**为什么这算装饰而不是小事** —— 该函数自己的 docstring 写着这两行存在的**唯一理由**:

> 照抄 `probe_binding` 的做法: 只报触发项, 后人无从判断这项判据对该题集**有没有约束力**
> —— 一份 0 触发的输出既可能是"题都很干净", 也可能是"它根本没看这些题",
> 两者长得一模一样。可见性行让这两种情形可分。

即: 这两行是**用来把"没触发"和"没运行"区分开**的取证信号。它们没断言 ⇒ 将来任何一次
重构/精简把它们删掉, CI 一声不吭, 而收口证据里引用的
「`0 处单 gold 疑似自足 / 10 道多 gold 题`」这句从此**无法区分**"题干净"与"它没看这些题"
—— 恰好退回该行要防的那一格。

**对照组 M6 让这条判定不可推诿**: 同一仓、同一作者、**同一设计意图**的闸 D 可见性行
(`[probe]`) **是被钉住的** (`test_main_prints_probe_binding_visibility`, 其 docstring
明写"没有这条断言, 把它从 `main` 删掉全套照绿")。selfsuff 侧**照抄了设计, 没照抄断言**。
两者差异不是口径分歧, 是漏做。

**修法** (不需要新 fixture, 照 `test_main_prints_probe_binding_visibility` 的形状):
在 `test_main_selfsuff_mode_exits_zero_with_findings` 里补两条整句断言 —— 一条
`assert "[selfcov] q1:" in out`, 一条 `assert "1 处单 gold 疑似自足 / 1 道多 gold 题" in out`
(整句匹配, 不要写 `"1 处" in out` —— 它是 `"11 处"` 的子串, 断言就成了"打了"而非"打对了",
与该文件 `M-1` 复审记过的那次同型)。

---

## 6. 限制清单 (每条注明"它看不见什么")

1. **变异粒度只到函数级 (四道闸)**。四道闸我做的是整函数恒绿, **没有**对闸内每个
   `continue` 分支逐个变异。**看不见**: 某个分支守卫失效但其他分支照常报的情形。
   缓解证据: 闸 B 红了 16 条专属用例、闸 D 红了 5 条, 每条各打一个分支, 分支覆盖看起来密
   —— 但这是**推断**, 不是分支级变异的实测。
2. **单测全部是合成 fixture, 对真实题集口径失明**。`test_docs_gold_gates.py` 里
   docs/cards/题集**全部**由 `tmp_path` 现造 (`A20 = "Y"*20`, `TERM_A`/`TERM_B`,
   `st01__F__I.md`), 零真实 chunk、零真实卡片。**看不见**: (a) 真实 114 个 chunk 上
   `match_names` 的子串歧义; (b) 真实 959 张卡的日文分词/大小写行为;
   (c) 真实 30 题题集的 YAML 形状 (如块标量尾换行、全角空格)。
   ⇒ **单测全绿 ≠ 这把尺子在真实题集上量对了。** 四闸对真实题集的判定必须另跑
   `python -m eval.docs_gold_gates <真实题集> --docs-dir ... --cards-dir ...` 取证,
   不能用本节的 `1119 passed` 顶替。
3. **本次只证"闸非恒绿", 没证"闸口径正确"**。变异测试的命题是
   「闸失效时测试会红」。它**看不见**闸和测试**一起**写错的情形 (两边同错则同绿)。
   闸 B 的 `98.6%` 口径论证、闸 D 的导航文件过滤口径, 属需要独立复核数据的活, 不在本节射程。
4. **闸 B / 闸 D 的已知语义盲区照旧存在, 且本次未触碰** (硬规矩 19):
   闸 B 只挡字面, 换措辞表达同一事实看不见; 闸 D 是字面筛, 语义等价卡片看不见。
   变异测试**不改善**这两条 —— 它只证明"字面那部分确实在工作"。
5. **`probe_binding` 的"绿灯不可证伪"问题本次未复量**。批 1 实测 12 题里 11 题闸 D
   不可触发。本次没有对当前 30 题题集重跑该可见性统计, **看不见**当前题集的闸 D 有效约束率。
6. ~~selfsuff 的 `THRESHOLD` 常量漂移未验证~~ → **已补测, 非限制**。
   M7: `THRESHOLD = 0.7` 改 `0.5` ⇒ `2 failed, 1117 passed`
   (`test_threshold_default_is_0_7` + `test_selfsuff_is_per_fact_not_aggregate`)。
   常量有钉子, 且额外有一条行为用例跟着变红 ⇒ 阈值不是摆设。

---

## 7. 总判定

| 对象 | 判定 |
|------|------|
| 闸 A / B / C / D | **全部非装饰品** (4 / 19 / 7 / 8 条红), 0 个被点名 |
| `selfsuff` 判据 + 打印 + CLI 分派 | 非装饰品 (8 / 2 / 2 条红), 上一轮"变异会红"**独立复现成立** |
| `[selfcov]` 可见性行 | **🔴 装饰品** — 删掉 `1119 passed` |
| selfsuff 汇总行 | **🔴 装饰品** — 删掉 `1119 passed` |

**这不阻塞四闸的绿灯结论**: 被点名的两处是 selfsuff 的**可见性输出**, 不是判据本身,
判据 (`self_sufficient_golds`) 实测有 8 条断言守着。但按硬规矩 18
「新加的取证信号必须当场补断言」, 这两行**属本单元新加**且**零断言**, 应在收口前补上
(修法见 §5, 两条整句断言即可, 不需要新 fixture)。

## 8. 收工三项证明

```
$ git status --porcelain
?? sdtm-rag/evidence/step_u1_audit.md
?? sdtm-rag/evidence/step_u1_audit_mutation.md

$ git diff HEAD --stat
(空 — tracked 文件零改动, 七次变异全部已还原)

$ git stash list
(空)

$ ./.venv/bin/python -m pytest -p no:warnings --tb=short | tail -3
........................................................................ [ 96%]
.......................................                                  [100%]
1119 passed in 24.84s
```

`git status` 的两条 `??` 是**新增证据文件**, 非变异残留:
`step_u1_audit.md` 属抽检方 A (本方未碰), `step_u1_audit_mutation.md` 即本文件。
tracked 文件零改动由 `git diff HEAD --stat` 空输出证明。

变异全程 **11 次** (A/B/C/D + S1/S2/S3/S4/S5 + 对照 M6/M7), 每次**单函数、单文件**,
每次跑完立刻 `git checkout -- <file>` 并 `git status --porcelain` 复核, 未 commit /
未 stash / 未建分支。

