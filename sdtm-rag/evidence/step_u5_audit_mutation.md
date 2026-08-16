# U5 收口 Step — 抽检方 B 变异测试报告 (规则 D 独立 session)

> 角色: 抽检方 B (test-engineer), 独立 session, 未读抽检方 A 的报告 (`evidence/step_u5_audit.md`,
> session 开始前即为未跟踪状态, 全程未打开)。
> 方法: 对 U5 三个新增面的判定逻辑做系统性变异测试, 逐条给 KILLED / SURVIVED;
> 存活的按 controller 冻结期纪律分流 (纯测试可杀 → 当场补; 需改 `eval/*.py` 或 `server/*.py` → 冻结上报)。
> **红线声明**: 本报告零题面、零 gold 真名、零 `st01__` 前缀。全程未打开任何 `data/study/**`
> 数据文件与题集 yml; 引用的 pytest 输出只有测试节点名 (`test_*`), 变异用的 fixture 全是
> 合成 id (`q0`/`d0`/`ca0`/`z00` 之类)。落盘前机械扫描 `st01` / `_v11_q` / `_v2_q`:
> 本报告内仅本红线声明自身提及 `st01` 二字 (2 处);
> `git diff -U0 scripts/tests/ | grep '^+'` 的新增行 **0 命中** (既有文件里那 3 处
> 命中全是 HEAD 原有行: 冻结常量断言与 collection/kb-root 互斥用例, 非我所写)。

*(报告边做边写 —— 每批变异跑完立即落盘该批行。)*

---

## §0 环境与基线

| 项 | 值 |
|---|---|
| 仓库 / 分支 | `/Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag` / `doc-track-u5` |
| HEAD | `b25c6229` (`docs(u5): plan Task 3 契约段注记 CLI 已改具名 flag`) |
| MERGE_BASE | `main` (U5 被审面 = `git diff main...HEAD`, 922 insertions) |
| 全量基线 | **1328 passed in 35.37s** (`./.venv/bin/python -m pytest -p no:warnings --tb=no`) |
| 针对性 4 模块基线 | **79 passed in 1.14s** |
| 变异 harness | scratchpad 脚本: backup(sha256) → apply → 清 pycache → 针对性 pytest → restore → 再清 pycache → sha256 逐字节核对 (见 §6) |
| **本轮结果** | **148 条有效变异 / 补测试前 KILLED 108 · SURVIVED 39 · FLAKY-KILL 1 → 补 25 个 test case 后 KILLED 144 · 仅剩 4 条等价变异** |
| **冻结期存活变异** | **0 条** (§4) |

被审面 (`git diff main...HEAD`):

| 文件 | 性质 | 变异数 |
|---|---|---|
| `eval/u5_verdict.py` | 整文件新 (181 行, 六段判定脚本) | 99 |
| `eval/rejudge_run.py` | 整文件新 (79 行, I1 探针) | 28 |
| `eval/run_eval.py` | 新增 `attach_routing_fields` + adapter 的 `routed_fallback` + main 接线 (+14 行) | 15 |
| `server/federation.py` | 新增 `last_route_fallback` 观测属性 (+5 行) | 7 |

三个搜索方向 (U2 §4.1: 三方向不等价, 都要跑):

| 方向 | 做法 | 条数 |
|---|---|---|
| ① 从断言出发 | 读每条既有断言, 问「什么更弱的实现仍能满足它」 | (并入 ②③ 的选题依据) |
| ② 从代码行出发 | 逐行问「这行改坏谁会红」, 新增段每一行都过一遍 | 110 |
| ③ 从断言的逻辑形状出发 | **对调型**: study/both 输入对调 · cost/gain 定义对调 · probes/controls 文件对调 · routed/fallback 字段对调 · 极性/家族/分支体对调 | 39 |

### 已知情报的验证结果 (审查方 mutation-lite 报的 5 条存活)

| 审查方编号 | 本轮对应 | 补测试前 | 备注 |
|---|---|---|---|
| M-N 删 cheap 判定的 docs 合取 | A60 | ⚠ SURVIVED **复现** | 另补 A61 (删 cards 半边) = KILLED, 证明只有 docs 半边没覆盖 |
| M-A pt 分母改 n_compared | A22 / A23 | **未复现** (两条都 KILLED) | 既有 `test_paired_effect_two_sided_and_pt_math` 用 n_scored=48 而 common=3, 分母一换就红 |
| M-J 删 E4 并集 both 半边 | A67 | ⚠ SURVIVED **复现** | 另补 A68/A69/A70/A71 四条同族, **全部存活** — 缺口比审查方报的大 |
| M-B 去 sorted | A16 | ⚠ SURVIVED (flaky, 8 次抽样 3 KILLED / 5 SURVIVED) | 见 §2 「flaky 杀手」段 |
| M-D probes 多键弱化 | A31 (⊆) / A29 (⊇) | A31 KILLED · **A29 ⚠ SURVIVED** | 弱化方向不同结论不同: 「允许缺键」有覆盖, 「允许多余键」没有 |

**共同 pattern 沿用与扩展**: 审查方总结的「合取/并集项只测一半」在本轮被系统性扫了一遍
(每个 `and` / `|` / 多键字典 / 多族循环 / 三遍复跑 / 四题脆弱池都单独拆半变异), 命中 22 条存活。
另外发现两个审查方未提的同源 pattern:
**(a) 「多族只测一族」** —— docs 家族在 I2 阈值、E 代价、E4 池上全线零覆盖 (A47/A48/A58/A59/A60/A69);
**(b) 「多遍只测一遍」** —— 三遍复跑的产物闸只要验首遍就全绿 (D16), 因为老 fixture 是 `[run] * 3`。

---

## §1 变异总表

方向: ② 从代码行出发 / ③ 从断言逻辑形状出发 (对调型)。
「补测试前」= HEAD 原样测试集下的结果; 「补测试后」= 本轮补测试后复验结果。
KILLED 后括号内为红掉的 case 数; 杀手列只记首个红掉的 case。

| # | 方向 | 目标 | 变异内容 | 补测试前 | 补测试后 / 杀手 |
|---|---|---|---|---|---|
| A01 | 2 | `u5_verdict:I1_MIN_SAME_RATE` | 阈值放宽 0.95→0.50 | KILLED (4) | — |
| A02 | 2 | `u5_verdict:I2_MAX_UNSTABLE` | 阈值放宽 {7,4}→{20,20} | KILLED (4) | — |
| A03 | 2 | `u5_verdict:I3_POS_MIN/I3_NEG_MAX` | 双阈值放宽 0.80/0.20→0.10/0.90 | KILLED (4) | — |
| A04 | 3 | `u5_verdict:I3_POS_MIN/I3_NEG_MAX` | 对调: 两常量值互换 (阳性阈=0.20, 阴性阈=0.80) | KILLED (4) | — |
| A05 | 2 | `u5_verdict:EXPECTED_N` | 题量 cards 48→47 | KILLED (5) | — |
| A06 | 3 | `u5_verdict:EXPECTED_N` | 对调: cards/docs 题量互换 (48↔30) | KILLED (1) | — |
| A07 | 2 | `u5_verdict:FRAGILE_4` | 脆弱池缩到 3 题 | KILLED (1) | — |
| A08 | 2 | `u5_verdict:CONTROL_KEYS` | 闸键集少一位 (阴性对照可缺席) | KILLED (29) | — |
| A09 | 2 | `u5_verdict:PROBE_KEYS` | 探针键集少一位 | KILLED (28) | — |
| A10 | 2 | `u5_verdict:scores_by_id` | 删 out_of_scope 跳过 (OOS 行计入分数) | KILLED (1) | — |
| A11 | 2 | `u5_verdict:scores_by_id` | parse_ok 缺省值 False→True (旧产物默认可信) | ⚠ SURVIVED | KILLED · `test_scores_by_id_treats_missing_parse_ok_key_as_untrusted` |
| A12 | 2 | `u5_verdict:scores_by_id` | 无视 parse_ok, 一律取 judge_fact_recall | KILLED (3) | — |
| A13 | 2 | `u5_verdict:stability` | 删三遍题集一致闸 | KILLED (1) | — |
| A14 | 2 | `u5_verdict:stability` | 合取只留一半: 删 `None in vals` (三遍全 parse 失败判稳定) | KILLED (1) | — |
| A15 | 2 | `u5_verdict:stability` | 合取只留一半: 删 `len(set(vals)) != 1` (翻分判稳定) | KILLED (9) | — |
| A16 | 2 | `u5_verdict:stability` | 去 sorted (不稳定清单顺序不确定) [审查方 M-B] | SURVIVED (3/8 抽样, hash seed 依赖) | KILLED 8/8 · `test_stability_unstable_list_is_deterministically_sorted` (新增, 确定性) |
| A17 | 3 | `u5_verdict:stability` | 对调: 稳定/不稳定两分支体互换 | KILLED (24) | — |
| A18 | 2 | `u5_verdict:stability` | ids 取三遍并集而非首遍 (题集差异被吞) | SURVIVED | **等价变异** (见 §3) |
| A19 | 3 | `u5_verdict:paired_effect` | 对调: cost/gain 定义互换 (代价记成收益) | KILLED (7) | — |
| A20 | 2 | `u5_verdict:paired_effect` | cost 判据 > → >= (平局计入代价) | KILLED (9) | — |
| A21 | 2 | `u5_verdict:paired_effect` | gain 判据 > → >= (平局计入收益) | KILLED (4) | — |
| A22 | 2 | `u5_verdict:paired_effect` | pt 分母 n_scored→n_compared [审查方 M-A] | KILLED (1) | — |
| A23 | 2 | `u5_verdict:paired_effect` | cost pt 分母单边改 n_compared (只坏 cost 半边) | KILLED (1) | — |
| A24 | 3 | `u5_verdict:paired_effect` | 对调: 配对集 交集 → 并集 (单侧不稳定题也进配对) | KILLED (4) | — |
| A25 | 2 | `u5_verdict:paired_effect` | 去掉 pt 的 100× 缩放 (读数变成比例) | KILLED (2) | — |
| A26 | 2 | `u5_verdict:paired_effect` | n_compared 改成 len(cost)+len(gain) (配对分母失真) | ⚠ SURVIVED | KILLED · `test_paired_effect_n_compared_counts_ties_not_just_movers` |
| A27 | 2 | `u5_verdict:build_verdict` | 删 controls 键集闸 | KILLED (2) | — |
| A28 | 2 | `u5_verdict:build_verdict` | controls 键集闸弱化成 ⊆ (允许缺键) | KILLED (1) | — |
| A29 | 2 | `u5_verdict:build_verdict` | controls 键集闸弱化成 ⊇ (允许多余键) | ⚠ SURVIVED | KILLED · `test_build_verdict_rejects_extra_control_key` |
| A30 | 2 | `u5_verdict:build_verdict` | 删 probes 键集闸 | KILLED (1) | — |
| A31 | 2 | `u5_verdict:build_verdict` | probes 键集闸弱化成 ⊆ [审查方 M-D 同族] | KILLED (1) | — |
| A32 | 2 | `u5_verdict:build_verdict` | 删对照极性绑定断言 | KILLED (1) | — |
| A33 | 2 | `u5_verdict:build_verdict` | 删 controls 零信息量闸 (全 parse 失败也过) | KILLED (1) | — |
| A34 | 2 | `u5_verdict:build_verdict` | 零信息量闸神经化 (== 0 → < 0) | KILLED (1) | — |
| A35 | 2 | `u5_verdict:build_verdict` | i3 合取只留阳性半 (阴性对照失守不判) | KILLED (2) | — |
| A36 | 2 | `u5_verdict:build_verdict` | i3 合取只留阴性半 | KILLED (1) | — |
| A37 | 3 | `u5_verdict:build_verdict` | 对调: i3 阳/阴筛选词互换 (阳性按阴性判) | KILLED (20) | — |
| A38 | 2 | `u5_verdict:build_verdict` | i3 阳性边界 >= → > (== 阈值被判失守) | KILLED (1) | — |
| A39 | 2 | `u5_verdict:build_verdict` | i3 阴性边界 <= → <  | KILLED (1) | — |
| A41 | 2 | `u5_verdict:build_verdict` | i1 判据 >= → > (边界) | KILLED (1) | — |
| A42 | 2 | `u5_verdict:build_verdict` | i1 只看 cards 半边 (docs 探针失守不降级) | KILLED (2) | — |
| A43 | 2 | `u5_verdict:build_verdict` | 删 n_questions 表头闸 | KILLED (4) | — |
| A44 | 2 | `u5_verdict:build_verdict` | 删 judge_model 断言 (漏 --judge 的 run 也收) | KILLED (1) | — |
| A45 | 2 | `u5_verdict:build_verdict` | 删计分行数闸 (产物残缺也收) | KILLED (1) | — |
| A46 | 3 | `u5_verdict:build_verdict` | 对调: 家族识别改取 cfg 后缀 (cards_/docs_ → study/both) | KILLED (33) | — |
| A47 | 2 | `u5_verdict:build_verdict` | I2 阈值查表族硬编码成 cards (docs 用 7 而非 4) | ⚠ SURVIVED | KILLED · `test_i2_docs_threshold_is_independent_of_cards[5-False]` |
| A48 | 2 | `u5_verdict:build_verdict` | I2 只判 cards 两档 (docs 不稳定不拦) | ⚠ SURVIVED | KILLED · `test_i2_docs_threshold_is_independent_of_cards[5-False]` |
| A49 | 2 | `u5_verdict:build_verdict` | I2 边界 <= → < | KILLED (2) | — |
| A50 | 2 | `u5_verdict:build_verdict` | I1 落盘分母改成 same_rate (分母字段失真) | KILLED (2) | — |
| A51 | 2 | `u5_verdict:build_verdict` | n_orig_parse_fail 硬下标 → .get (缺键静默落 None) | KILLED (1) | — |
| A52 | 2 | `u5_verdict:build_verdict` | 自毁合取只留 i3 半 (I2 触发不再拦 E) | KILLED (3) | — |
| A53 | 2 | `u5_verdict:build_verdict` | 自毁合取只留 i2 半 (I3 触发不再拦 E) [M-N 同族] | KILLED (3) | — |
| A54 | 3 | `u5_verdict:build_verdict` | 对调: E2 自毁事由二选一互换 | KILLED (2) | — |
| A55 | 2 | `u5_verdict:build_verdict` | 自毁 rc 2 → 0 (触发也报全过) | KILLED (6) | — |
| A56 | 2 | `u5_verdict:build_verdict` | 自毁时 E 置空字典而非 None (下游读成有结论) | KILLED (2) | — |
| A57 | 3 | `u5_verdict:build_verdict` | 对调: cards 侧 study/both 入参互换 | KILLED (3) | — |
| A58 | 3 | `u5_verdict:build_verdict` | 对调: docs 侧 study/both 入参互换 | ⚠ SURVIVED | KILLED · `test_docs_side_cost_is_reported_with_the_docs_denominator` |
| A59 | 3 | `u5_verdict:build_verdict` | 对调: docs 侧 pt 分母用 cards 题量 (家族分母错配) | ⚠ SURVIVED | KILLED · `test_docs_side_cost_is_reported_with_the_docs_denominator` |
| A60 | 2 | `u5_verdict:build_verdict` | cheap 合取删 docs 半边 [审查方 M-N] | ⚠ SURVIVED | KILLED · `test_docs_side_cost_is_reported_with_the_docs_denominator` |
| A61 | 2 | `u5_verdict:build_verdict` | cheap 合取删 cards 半边 | KILLED (3) | — |
| A62 | 2 | `u5_verdict:build_verdict` | cheap 判据回退到 pt 读数 (round 舍零即判 cheap) | KILLED (1) | — |
| A63 | 3 | `u5_verdict:build_verdict` | 对调: cheap 读 gain_ids 而非 cost_ids | KILLED (4) | — |
| A64 | 3 | `u5_verdict:build_verdict` | 对调: E2 结论词互换 (cheap↔cost_reported) | KILLED (7) | — |
| A65 | 3 | `u5_verdict:build_verdict` | 对调: E3 的 study/both 分值来源互换 | KILLED (2) | — |
| A66 | 3 | `u5_verdict:build_verdict` | 对调: E3 的 stable_study/stable_both 来源互换 | ⚠ SURVIVED | KILLED · `test_e3_covers_every_fragile_question_and_separates_the_two_stability_sides` |
| A67 | 2 | `u5_verdict:build_verdict` | E4 cards 并集删 both 半边 [审查方 M-J] | ⚠ SURVIVED | KILLED · `test_e4_unions_both_sides_per_family_and_stays_sorted` |
| A68 | 2 | `u5_verdict:build_verdict` | E4 cards 并集删 study 半边 | ⚠ SURVIVED | KILLED · `test_e4_unions_both_sides_per_family_and_stays_sorted` |
| A69 | 2 | `u5_verdict:build_verdict` | E4 docs 并集删 both 半边 | ⚠ SURVIVED | KILLED · `test_e4_unions_both_sides_per_family_and_stays_sorted` |
| A70 | 3 | `u5_verdict:build_verdict` | 对调: E4 并集 → 交集 (只报两侧都不稳定的) | ⚠ SURVIVED | KILLED · `test_e4_unions_both_sides_per_family_and_stays_sorted` |
| A71 | 3 | `u5_verdict:build_verdict` | 对调: E4 家族互换 (cards 位放 docs 池) | ⚠ SURVIVED | KILLED · `test_e4_unions_both_sides_per_family_and_stays_sorted` |
| A72 | 3 | `u5_verdict:build_verdict` | 对调: 收尾 rc 三元互换 (I1 降级报 0, 全过报 3) | KILLED (17) | — |
| A73 | 3 | `u5_verdict:build_verdict` | 对调: advisory_only 极性反转 | KILLED (3) | — |
| A74 | 2 | `u5_verdict:build_verdict` | I2 counts 改报稳定题数 (读数与 unstable 清单脱钩) | KILLED (4) | — |
| A75 | 3 | `u5_verdict:main` | 对调: probes 两份产物文件互换 (cards↔docs) | ⚠ SURVIVED | KILLED · `test_main_binds_probe_identity` |
| A76 | 3 | `u5_verdict:main` | 对调: controls 家族互换 (docs 位收 cards 产物) | KILLED (1) | — |
| A77 | 3 | `u5_verdict:main` | 对调: controls 极性互换 (阳性位收阴性产物) | KILLED (4) | — |
| A78 | 3 | `u5_verdict:main` | 对调: runs 的 cards study/both 互换 | ⚠ SURVIVED | KILLED · `test_main_binds_study_and_both_run_identity` |
| A79 | 2 | `u5_verdict:main` | rc 不传播: return rc → return 0 | ⚠ SURVIVED | KILLED · `test_main_propagates_advisory_rc_and_prints_the_verdict` |
| A80 | 2 | `u5_verdict:main` | 三遍 nargs=3 → nargs='+' (两遍也收) | ⚠ SURVIVED | KILLED · `test_main_requires_exactly_three_runs_per_config` |
| A81 | 2 | `u5_verdict:main` | 对照 flag 改成非必填 (缺对照静默为 None) | KILLED (1) | — |
| A40a | 2 | `u5_verdict:build_verdict` | 删整块 probe n=0 闸 (含 for 头) | KILLED (2) | — |
| A40b | 2 | `u5_verdict:build_verdict` | probe n=0 闸神经化 (== 0 → < 0) | KILLED (2) | — |
| A82 | 3 | `u5_verdict:build_verdict` | 对调: stability 返回值两元互换 (稳定池当不稳定池用) | KILLED (21) | — |
| A84 | 2 | `u5_verdict:build_verdict` | I3 不落盘 avg (只留 pass, 读数人看不到对照实测值) | KILLED (2) | — |
| A85 | 2 | `u5_verdict:build_verdict` | 删产物里的 thresholds 自述块 (冻结判据失去审计追溯) | ⚠ SURVIVED | KILLED · `test_verdict_archives_the_frozen_thresholds_it_judged_by` |
| A86 | 2 | `u5_verdict:build_verdict` | E4 去 sorted (不可判池顺序不确定) | ⚠ SURVIVED | KILLED · `test_e4_unions_both_sides_per_family_and_stays_sorted` |
| A87 | 2 | `u5_verdict:main` | 删 rc 与 E2 结论的终端回显 (跑批现场唯一人读出口) | ⚠ SURVIVED | KILLED · `test_main_propagates_advisory_rc_and_prints_the_verdict` |
| A88 | 3 | `u5_verdict:build_verdict` | 对调: I1 落盘的 n 与 n_orig_parse_fail 两字段互换 | KILLED (2) | — |
| B01 | 2 | `rejudge_run:rejudge` | 删 out_of_scope 跳过 (OOS 行进 I1 分母) | KILLED (1) | — |
| B02 | 2 | `rejudge_run:rejudge` | 删全文答案闸 (无 answer 也硬跑) | KILLED (1) | — |
| B03 | 2 | `rejudge_run:rejudge` | orig parse_ok 缺省 False→True (旧产物默认可信) | KILLED (1) | — |
| B04 | 3 | `rejudge_run:rejudge` | 对调: orig parse_ok 分支极性反转 | KILLED (10) | — |
| B05 | 3 | `rejudge_run:rejudge` | 对调: judge 入参 question/answer 互换 | ⚠ SURVIVED | KILLED · `test_judge_receives_question_answer_facts_model_in_that_order` |
| B06 | 2 | `rejudge_run:rejudge` | facts 硬下标 → .get (题集对不上静默跑空事实集) | KILLED (1) | — |
| B07 | 3 | `rejudge_run:rejudge` | 对调: verdict is None 分支极性反转 | KILLED (5) | — |
| B08 | 2 | `rejudge_run:rejudge` | recall 取 verdict[1] 而非 [0] (取错元组位) | KILLED (6) | — |
| B09 | 2 | `rejudge_run:rejudge` | recall 精度 4 位 → 1 位 (口径变粗, same 判定放宽) | ⚠ SURVIVED | KILLED · `test_rejudged_recall_keeps_four_decimals` |
| B10 | 3 | `rejudge_run:rejudge` | 对调: same 判据 == → != | ⚠ SURVIVED | KILLED · `test_rejudged_recall_keeps_four_decimals` |
| B11 | 2 | `rejudge_run:rejudge` | 重判 parse 失败行记 same=True (仪器失败算复现) | KILLED (1) | — |
| B12 | 3 | `rejudge_run:rejudge` | 对调: scored 过滤极性反转 (只留 orig parse 失败行) | KILLED (7) | — |
| B13 | 2 | `rejudge_run:rejudge` | n 改报 len(rows) (排除行仍计入分母读数) | KILLED (3) | — |
| B14 | 2 | `rejudge_run:rejudge` | same_rate 分母 len(scored) → len(rows) | ⚠ SURVIVED | KILLED · `test_denominators_with_mixed_excluded_and_scored_rows` |
| B15 | 2 | `rejudge_run:rejudge` | n_orig_parse_fail 改报 len(rows) (与真排除数脱钩) | ⚠ SURVIVED | KILLED · `test_denominators_with_mixed_excluded_and_scored_rows` |
| B16 | 2 | `rejudge_run:rejudge` | n_orig_parse_fail 恒 0 (排除行不上报) | KILLED (3) | — |
| B17 | 2 | `rejudge_run:rejudge` | n_rejudge_parse_fail 统计域 scored → rows | SURVIVED | **等价变异** (见 §3) |
| B18 | 3 | `rejudge_run:rejudge` | 对调: n_rejudge_parse_fail 统计极性反转 | KILLED (1) | — |
| B19 | 2 | `rejudge_run:rejudge` | same_rate 不 round (口径与产物精度约定脱钩) | ⚠ SURVIVED | KILLED · `test_same_flag_polarity_on_asymmetric_fixture` |
| B20 | 2 | `rejudge_run:rejudge` | 空 scored 兜底 0.0 → 1.0 (无样本报满分复现) | KILLED (1) | — |
| B21 | 2 | `rejudge_run:rejudge` | rows 不落盘 (逐题取证消失) | KILLED (5) | — |
| B22 | 2 | `rejudge_run:main` | judge 模型硬下标 → .get (缺键静默当对得上) | KILLED (1) | — |
| B23 | 3 | `rejudge_run:main` | 对调: 模型一致性判据 != → == | KILLED (2) | — |
| B24 | 2 | `rejudge_run:main` | 删模型一致性闸整块 | KILLED (1) | — |
| B25 | 3 | `rejudge_run:main` | 对调: 事实集取 expected_sources 而非 expected_facts | ⚠ SURVIVED | KILLED · `test_main_feeds_expected_facts_not_expected_sources` |
| B26 | 2 | `rejudge_run:main` | 重判用 run 里的模型而非 --judge-model (闸过后口径回落) | SURVIVED | **等价变异** (见 §3) |
| C01 | 2 | `run_eval:attach_routing_fields` | 删长度一致闸 | KILLED (1) | — |
| C02 | 2 | `run_eval:attach_routing_fields` | 长度闸 != → < | KILLED (1) | — |
| C03 | 2 | `run_eval:attach_routing_fields` | zip 去 strict=True (fallback 列表长度失配静默截断) | ⚠ SURVIVED | KILLED · `test_attach_routing_fields_fails_loud_when_the_two_evidence_lists_desync` |
| C04 | 3 | `run_eval:attach_routing_fields` | 对调: routed / routed_fallback 两字段互换 | KILLED (3) | — |
| C05 | 2 | `run_eval:attach_routing_fields` | fallback 恒写 None (值传递断链) | KILLED (2) | — |
| C06 | 2 | `run_eval:attach_routing_fields` | fallback 全写最后一次 (串题) | KILLED (2) | — |
| C07 | 2 | `run_eval:attach_routing_fields` | routed 全写最后一次 (串题) | KILLED (2) | — |
| C08 | 2 | `run_eval:attach_routing_fields` | 只写首题 (部分写入) | KILLED (3) | — |
| C09 | 2 | `run_eval:_FederatedAdapter` | adapter 恒记 None fallback | KILLED (3) | — |
| C10 | 2 | `run_eval:_FederatedAdapter` | getattr 缺省 None → False (缺属性伪装成已判无回落) | KILLED (2) | — |
| C11 | 3 | `run_eval:_FederatedAdapter` | 对调: routed 记成入参 corpus 而非引擎判库 | KILLED (6) | — |
| C12 | 2 | `run_eval:main` | 删主线 attach_routing_fields 调用 (产物无逐题取证) | KILLED (1) | — |
| C13 | 2 | `run_eval:_FederatedAdapter` | routed_fallback 与 routed 记录次序互换 (等价性探针) | SURVIVED | **等价变异** (见 §3) |
| C14 | 2 | `federation:FederatedEngine.retrieve` | 删每题 fallback 清位 (强制档串上一题的标志) | KILLED (1) | — |
| C15 | 2 | `federation:FederatedEngine.retrieve` | 清位值 None → False (强制档伪装成已判无回落) | KILLED (2) | — |
| C16 | 2 | `federation:FederatedEngine.retrieve` | auto 档不记 fallback | KILLED (1) | — |
| C17 | 3 | `federation:FederatedEngine.retrieve` | 对调: fallback 记成判库名而非布尔 | KILLED (1) | — |
| C18 | 2 | `federation:FederatedEngine.__init__` | 删构造期属性初始化 (首题前读会 AttributeError) | ⚠ SURVIVED | KILLED · `test_last_route_fallback_exists_before_any_retrieve` |
| C19 | 3 | `federation:FederatedEngine.retrieve` | 对调: fallback 布尔取反 | KILLED (1) | — |
| D01 | 2 | `u5_verdict:stability` | 只读首遍分数 (三遍复跑退化成一遍) | KILLED (9) | — |
| D02 | 2 | `u5_verdict:build_verdict` | controls 逐条闸只查首个对照 | KILLED (2) | — |
| D03 | 2 | `u5_verdict:build_verdict` | I3 读数改取首行 recall 而非 avg (字段错取) | ⚠ SURVIVED | KILLED · `test_i3_reads_the_control_avg_field_not_a_single_row` |
| D07 | 2 | `rejudge_run:rejudge` | orig 排除判据改成 `is False` (缺键行不再排除) | KILLED (1) | — |
| D12 | 3 | `u5_verdict:build_verdict` | 对调: 行数闸的家族查表反转 (cards 行数按 docs 判) | KILLED (28) | — |
| D16 | 2 | `u5_verdict:build_verdict` | 三道产物闸只验首遍 run (第 2/3 遍残缺可蒙混) | ⚠ SURVIVED | KILLED · `test_build_verdict_checks_all_three_runs_not_just_the_first[1]` |
| D17 | 2 | `u5_verdict:stability` | 只取前两遍 run (三遍稳定性退化成两遍) | KILLED (1) | — |
| D18 | 2 | `u5_verdict:build_verdict` | probe n=0 闸只查首个探针 | KILLED (1) | — |
| D20 | 2 | `u5_verdict:build_verdict` | E3 只报脆弱池首题 (另 3 题失踪) | ⚠ SURVIVED | KILLED · `test_e3_covers_every_fragile_question_and_separates_the_two_stability_sides` |
| D21 | 2 | `u5_verdict:build_verdict` | I2 落盘只留 cards 两档 (docs 计数与清单失踪) | KILLED (22) | — |
| D22 | 2 | `u5_verdict:build_verdict` | E 只算 cards 家族 | ⚠ SURVIVED | KILLED · `test_docs_side_cost_is_reported_with_the_docs_denominator` |
| D23 | 2 | `rejudge_run:rejudge` | orig 字段改记重判值 (same 恒真) | KILLED (3) | — |
| D25 | 2 | `run_eval:_FederatedAdapter` | 删 routed_fallback 列表初始化 | KILLED (11) | — |
| D26 | 2 | `run_eval:attach_routing_fields` | 长度闸改比 routed_fallback (等价性探针) | ⚠ SURVIVED | KILLED · `test_attach_routing_fields_fails_loud_when_the_two_evidence_lists_desync` |
| D27 | 3 | `federation:FederatedEngine.retrieve` | 对调: fallback 清位挪到 auto 分支之后 (auto 档也被清) | KILLED (1) | — |

### 作废条目

| # | 原意图 | 作废理由 |
|---|---|---|
| A40 | 删 probe n=0 闸 | 删除留下悬空 `for` 体 → SyntaxError, 模块导不进来。**语法不合法的变异不算变异** (它"杀掉"整个模块, 不测任何断言)。已拆成 A40a (删整块含 `for` 头) / A40b (条件神经化 `== 0 → < 0`), 两条均 KILLED |

> harness 后来加了 `compile()` 前置检查 + pytest `-rfE`: 早期只用 `-rf` 时, 收集期 ERROR
> **不会**出现在 short summary 里 → 语法坏掉的变异会被误读成 SURVIVED。这是本轮唯一一次
> harness 自身的假阴性, 发现后全批 148 条用新 harness 重跑了一遍, 只有 A40 中招。

---

## §2 补测试前存活的 39 条 + 1 条 flaky — 逐条处置

### 2.1 处置纪律 (controller 裁定) 与本轮判断标准

| 情形 | 处置 |
|---|---|
| 只动 `scripts/tests/*.py` 就能杀 | 当场补测试, 变异复验转红 |
| 杀掉需要改 `eval/*.py` 或 `server/*.py` **任何一行** (含判定语义/口径/输出字段) | **不许改**, 记入 §4 冻结期存活清单, 交下一单元 |
| 阈值常量 / 判定规则 | 绝对不碰 (只做临时变异, 逐条还原) |

**本轮判断标准 (逐条实际问过的问题)**: 「该变异改变了 `build_verdict` / `rejudge` /
`attach_routing_fields` 的**可观测输出**吗?」

- 若**是** → 一定能用一个只喂输入、只读输出的新 case 钉住 ⇒ 纯测试可杀 ⇒ 当场补;
- 若**否** (对所有可能输入输出都相同) → 那是**等价变异**, 不是覆盖缺口, 补测试也杀不掉, 也不需要杀;
- 若可观测但**当前实现的行为本身需要改**才能钉住 → 才进 §4 冻结清单。

39 条里 **35 条属第一类** (纯测试补网, 全部当场转红), **4 条属第二类** (等价变异, §3),
**第三类 0 条** —— 即本轮没有任何一条存活变异需要动判定脚本, 详见 §4。

### 2.2 按缺口性质归并 (35 条 → 补 25 个 case)

| 缺口 | 存活变异 | 补的 case | 为什么老断言照不出来 |
|---|---|---|---|
| G1 判分可信度缺省值 | A11 | `test_scores_by_id_treats_missing_parse_ok_key_as_untrusted` | 老 fixture 每行都显式带 `judge_parse_ok`, 缺省值 (`.get(..., False)`) 那条路零覆盖 |
| G2 不稳定清单顺序不确定 | A16 (flaky) · A86 | `test_stability_unstable_list_is_deterministically_sorted` · `test_e4_unions_both_sides_per_family_and_stays_sorted` | 见 2.3 |
| G3 配对分母口径 | A26 | `test_paired_effect_n_compared_counts_ties_not_just_movers` | 老 fixture 里没有"两侧都稳定且同分"的题, `n_compared` 与"有变化的题数"数值上碰巧相等 |
| G4 闸键集只防缺键不防多键 | A29 | `test_build_verdict_rejects_extra_control_key` | 两条既有用例都是**删**键; 多塞一份极性合法的对照能悄悄改变 I3 判定面 |
| G5 **docs 家族全线零覆盖** | A47 A48 A58 A59 A60 A69 D22 | `test_i2_docs_threshold_is_independent_of_cards[4/5]` · `test_docs_side_cost_is_reported_with_the_docs_denominator` | 老 fixture 的 docs 两侧同分同稳定 ⇒ docs 的 I2 阈值 (4)、E 代价、pt 分母 (30) 全部不可观测 |
| G6 E3 只验了"两侧都稳定"的一题 | A66 D20 | `test_e3_covers_every_fragile_question_and_separates_the_two_stability_sides` | `stable_study`/`stable_both` 在老 fixture 里同为 True ⇒ 对调不可见; 只报首题也不可见 |
| G7 E4 并集四个半边 + 家族分离 | A67 A68 A70 A71 (+A69 见 G5) | `test_e4_unions_both_sides_per_family_and_stays_sorted` | 老 fixture 里 E4 恒为 `{"cards": [], "docs": []}` —— 空集怎么删怎么换都相等 |
| G8 产物不自带判据 | A85 | `test_verdict_archives_the_frozen_thresholds_it_judged_by` | 无人断言 `thresholds` 块; 阈值只活在代码里, 归档 json 事后无法自证按什么判 |
| G9 I3 读数字段错取 | D03 | `test_i3_reads_the_control_avg_field_not_a_single_row` | 老 `_ctl` 造的每行 `recall` 都等于 `avg` ⇒ 读 avg 还是读首行不可分 |
| G10 三遍产物闸只验首遍 | D16 | `test_build_verdict_checks_all_three_runs_not_just_the_first[0/1/2]` | 老 fixture 是 `[同一份 run] * 3`, 第 2/3 遍残缺照不出来 |
| G11 main 级身份绑定 (probe / study-both) | A75 A78 | `test_main_binds_probe_identity` · `test_main_binds_study_and_both_run_identity` | 两份 probe 的 `n` 与两组 run 的分数在老 fixture 里都对称 ⇒ 对调不可见 |
| G12 rc 传播与终端回显 | A79 A87 | `test_main_propagates_advisory_rc_and_prints_the_verdict` | 老用例只断言 happy path 的 `main()==0`; `return rc → return 0` 与删掉 print 全绿 |
| G13 三遍复跑的 arity | A80 | `test_main_requires_exactly_three_runs_per_config` | `nargs=3` 松成 `'+'` 后两遍也收, I2 稳定性口径失义 |
| G14 judge 入参绑定 | B05 B25 | `test_judge_receives_question_answer_facts_model_in_that_order` · `test_main_feeds_expected_facts_not_expected_sources` | 老桩 `lambda *a` 吃任意实参不记账 ⇒ question/answer 对调、事实集取错字段都全绿 |
| G15 重判分精度口径 | B09 | `test_rejudged_recall_keeps_four_decimals` | 老桩只返回 0.5/1.0, `round(x, 4)` 与 `round(x, 1)` 结果相同 |
| G16 same 极性 + same_rate round | B10 B19 | `test_same_flag_polarity_on_asymmetric_fixture` | 老 fixture 是"1 同 1 异", 极性取反后 `n_same` 仍是 1 —— **对调型的教科书级盲区** |
| G17 混合行 (排除行 + 计分行) 的分母 | B14 B15 | `test_denominators_with_mixed_excluded_and_scored_rows` | 老用例要么全排除要么全计分 ⇒ `len(scored)` 与 `len(rows)` 从不分叉 |
| G18 两条取证链错位守卫 | C03 (+D26) | `test_attach_routing_fields_fails_loud_when_the_two_evidence_lists_desync` | 长度闸只比 `routed` vs `results`; `routed`/`routed_fallback` 之间靠 `zip(strict=True)`, 而 adapter 不变量让两者永远等长 ⇒ 去掉 strict 无人发现 |
| G19 观测属性构造期缺席 | C18 | `test_last_route_fallback_exists_before_any_retrieve` | 首次 `retrieve` 前该属性不存在时, eval 侧 `getattr(..., None)` 兜底会把"缺属性"读成"没回落" |

### 2.3 flaky 杀手 (A16 / M-B): 「有覆盖」与「稳定有覆盖」不是一回事

审查方把 **M-B (去 `sorted`)** 报为存活。本轮 8 次独立抽样得到 **3 次 KILLED / 5 次 SURVIVED**:

```
A16  KILLED / SURVIVED / KILLED / SURVIVED / KILLED / SURVIVED / SURVIVED / SURVIVED
```

原因是既有 `test_stability_flags_flip_and_parse_fail` 里的不稳定集合只有 **2 个元素**,
CPython 的 `PYTHONHASHSEED` 随机化让集合迭代序**约一半概率碰巧就是升序**。
也就是说这条守卫既不是"没覆盖", 也不是"有覆盖", 而是**掷硬币覆盖** —— 在 CI 上会表现成
偶发红, 在本地单跑则大概率绿。**审查方与我在同一条变异上得到不同结论, 根因就是这个随机性,
不是双方谁做错了。**

补的 `test_stability_unstable_list_is_deterministically_sorted` 用 12 个 id
(碰巧升序的概率 ~1/12!), 复验 **8/8 KILLED**。同族的 E4 排序 (A86) 由 8 元素并集的
新用例覆盖, 也是确定性的。

---

## §3 等价变异 (4 条) —— 不是缺口, 无需补测试

这 4 条对**所有**输入的可观测输出都与原码相同, 因此任何测试都杀不掉它们; 逐条附等价性论证:

| # | 变异 | 等价性论证 |
|---|---|---|
| A18 | `stability`: `ids = set(maps[0])` → 三遍并集 | 下一句就是「任一 map 的键集 ≠ ids 则 raise」。原码 raise ⟺ 三遍键集不全等于首遍 ⟺ 三遍不全等; 变异 raise ⟺ 存在 map ≠ 并集 ⟺ 三遍不全等 (若全等则并集 = 首遍)。两者的通过集与 raise 集逐点相同 |
| B17 | `n_rejudge_parse_fail` 统计域 `scored` → `rows` | `rows \ scored` 恰是 `{"id":…, "orig_parse_fail": True}` 形状的行, 不含 `parse_fail` 键 ⇒ `.get("parse_fail")` 为 `None` (falsy) ⇒ 两个求和恒相等 |
| B26 | `rejudge(...)` 传 `run_model` 而非 `a.judge_model` | 该行只有在「`run_model != a.judge_model` 则 raise」之后才可达 ⇒ 到达此处时两者必然相等 |
| C13 | adapter 里 `routed` / `routed_fallback` 两次 `append` 顺序互换 | 第二次 append 的取值来自 `self.fed.last_route_fallback`, 与 `self.routed` 无任何别名或读依赖 ⇒ 两种顺序产生同一对列表 |

> 备注: 同批里 **D26** (长度闸改比 `routed_fallback`) 初看也像等价 (adapter 不变量保证两列表等长),
> 但它**可区分** —— 新增的 desync 用例手工破坏该不变量后, 原码抛 `ValueError` (strict zip)、
> 变异抛 `RuntimeError`, 已 KILLED。这条提醒: 「靠调用方不变量成立」≠ 「等价」。

---

## §4 冻结期存活变异清单

**本轮 0 条。**

判断标准 (§2.1 已列, 此处复述结论): 39 条存活变异逐条问「杀掉它是否必须改
`eval/*.py` 或 `server/*.py` 任何一行」——

- 35 条: **否**。它们都改变了纯函数 (`scores_by_id` / `stability` / `paired_effect` /
  `build_verdict` / `rejudge` / `attach_routing_fields`) 或 `main()` 的可观测输出
  (返回值 / 落盘 json 字段 / stdout / 抛异常类型), 只需要**新的输入组合**就能钉住。
  这些输入组合此前不存在, 纯属 fixture 覆盖面的问题, 与判定语义无关。
  → 全部当场补测试, 复验转红 (§1 表末列)。
- 4 条: **不适用** —— 等价变异, 改判定脚本也杀不掉 (§3)。
- 0 条: 需要改判定语义 / 口径 / 输出字段。

**关键一点**: 本轮补的 25 个 case **没有一个**要求判定脚本改变行为 —— 每个 case 的期望值
都是**先跑当前实现取到、再确认符合 spec §5 语义**后写下的。
补测试前后 `eval/u5_verdict.py` / `eval/rejudge_run.py` / `eval/run_eval.py` /
`server/federation.py` 的 sha256 **逐字节未变** (§6), 满足 spec §5.3-2「跑批后判据一字不改」。

---

## §5 本轮补的测试 (25 个 case, 只动 `scripts/tests/*.py`)

| 文件 | 新增 case | 内容 |
|---|---|---|
| `scripts/tests/test_u5_verdict.py` | 18 (含 2 个 parametrize: 2 档 + 3 档) | G1-G13 |
| `scripts/tests/test_rejudge_run.py` | 5 | G14-G17 (含记账型 judge 桩 `_recorder`) |
| `scripts/tests/test_run_eval_federated.py` | 1 | G18 |
| `scripts/tests/test_federation.py` | 1 | G19 |

对既有代码的唯一改动是测试 helper `_main_argv` 加了一个默认 `None` 的 `cards_both` 形参
(2 行), 用于构造 study/both 非对称的 main 级 fixture; 既有调用点行为不变。

全部新 case 的 fixture 均为合成 id, 不引用任何 gold / 题集文件, 不打 judge API
(`_recorder` / `_boom` 桩), 零网络零费用。

---

## §6 还原核验 (byte 级)

harness 每条变异的固定流程:

```
purge(__pycache__/.pytest_cache) → apply → purge → compile() 语法检查
  → pytest (-p no:warnings --tb=no -q -rfE) → 从 scratchpad 备份 cp 回来
  → purge → sha256 与 backup manifest 逐字节比对
```

`purge` 在 apply 前后各做一次, 且用 `rglob("__pycache__")` 全仓扫 —— 本单元已实证
**同秒写入的 .pyc 会造成假还原** (源码还原了但解释器仍加载旧字节码, 表现为"变异还活着"或
"变异复验假绿")。148 条变异 **`restore_bad` 全为空**, 无一次 sha 不符。

被审的四个源文件, 施加变异前后 sha256:

| 文件 | 动手前 sha256 | 收尾 sha256 | 结论 |
|---|---|---|---|
| `eval/u5_verdict.py` | `4e8bf7c0…55ad20c2` | `4e8bf7c0…55ad20c2` | **EXACT** |
| `eval/rejudge_run.py` | `a81fda9d…0eba3412e7` | 同左 | **EXACT** |
| `eval/run_eval.py` | `6c853c96…727c37d4` | 同左 | **EXACT** |
| `server/federation.py` | `df7d3edb…c7d658be` | 同左 | **EXACT** |

完整值 (收尾实测):

```
4e8bf7c0e3c8c82b3c99ee21c311f79f5e81b4a5aece302d15234ae255ad20c2  eval/u5_verdict.py
a81fda9dd0aca0692d15f79c1c72ab39b568b55d45a842e809f06c0eba3412e7  eval/rejudge_run.py
6c853c96a22e5971f2431b54964bae83d90ea8fd632bf5b8e079eeee727c37d4  eval/run_eval.py
df7d3edbdba6632b0c4e0404359e11162392b2f34888d89ca694ce45c7d658be  server/federation.py
```

**我主动修改并保留的四个测试文件** (补 case, 属预期变更):

| 文件 | 改前 sha256 | 改后 sha256 |
|---|---|---|
| `scripts/tests/test_u5_verdict.py` | `a3618e2101bd0e44c43f8e8fb2db538060e52f2785d36ae3a563e9aed9162b21` | `e06666171310c533b021a50306170e064dd2e817e8673a1d20942df77bac712d` |
| `scripts/tests/test_rejudge_run.py` | `3f9920a5655fb8aac715ec1e5487087600ddbb8cbe2e260ab30958621972db79` | `41241c420c2cbe1bdfcb601f54850b0d9f9524b6fa67e3d662e644cc25989682` |
| `scripts/tests/test_run_eval_federated.py` | `eb1ce524de22c4d392598635181e5231d97aa4cab2c80e2cbb161a10b8549534` | `9e5f6332416fe6fe1dbc0ab38f0e0e59714e91606cc8448f54e64bb2f45a97d4` |
| `scripts/tests/test_federation.py` | `9d36d0ba2112a475fe9755c0eba485b723cd85dfa9592668b576a6b2ec05fd70` | `68cf569216bdc0fa370cdc77d278b30237e2012cdf96e6ad043330622ea1921b` |

**未碰**: `data/**` (全程未打开任何数据/题集文件)、`docs/**`、`milestones/**`、
`server/` 除 `federation.py` 外的任何文件。所有变异均在同一条 harness 调用内施加并复原。

---

## §7 收尾: 全量 pytest + git status

复跑命令 (与基线同一条):

```
./.venv/bin/python -m pytest -p no:warnings --tb=no
```

末两行:

```
.........................................................                [100%]
1353 passed in 37.82s
```

基线 1328 → **1353 passed** (+25 = 本轮补的 25 个 case), **0 failed / 0 error**。
针对性 4 模块: 79 → **104 passed**; 连跑 5 次全绿 (不同 hash seed), 新 case 无 flaky。

`git status --short`:

```
 M scripts/tests/test_federation.py
 M scripts/tests/test_rejudge_run.py
 M scripts/tests/test_run_eval_federated.py
 M scripts/tests/test_u5_verdict.py
?? evidence/step_u5_audit.md
?? evidence/step_u5_audit_mutation.md
```

逐条说明:

- 四个 ` M` 全是测试文件 —— 我补的 case (`281 insertions(+), 2 deletions(-)`,
  那 2 删是 `_main_argv` 签名与其中一行调用的原地改写)。
- `?? evidence/step_u5_audit_mutation.md` —— 本报告。
- `?? evidence/step_u5_audit.md` —— **抽检方 A 的报告, 与我无关**。session 开始前即已是
  未跟踪状态, 我全程未读、未改 (规则 D 独立性)。

被审的四个源文件 (`eval/u5_verdict.py` / `eval/rejudge_run.py` / `eval/run_eval.py` /
`server/federation.py`) **不出现在 git status 中** = 148 次变异全部干净复原。

---

## §8 一句话结论

`eval/u5_verdict.py` 与 `eval/rejudge_run.py` 的**闸类断言**(键集 / 极性 / 零信息量 /
表头 / 行数 / judge 模型 / 阈值边界)**很结实** —— 单条闸的删除、神经化、边界移位、极性反转
几乎全被当场杀掉; 真正的系统性缺口只有一种形状, 且完全符合审查方总结的 pattern 并可再细分成三层:

1. **合取/并集只测一半** (cheap 的 docs 项、E4 的四个半边、键集闸的多键方向);
2. **多族只测一族** —— docs 家族在 I2 阈值、E 代价与 pt 分母、E4 池上**全线零覆盖**,
   这是本轮最大的一片空白 (7 条存活), 而它恰恰是 U5 这个单元真正要量的那一侧;
3. **多遍/多题只测一遍一题** —— 三遍复跑的产物闸只验首遍即全绿, 脆弱池只报首题即全绿。

再加两条方法论层面的收获:
**(a)** 「有覆盖」不等于「稳定有覆盖」—— M-B 是掷硬币覆盖, 这解释了审查方与我在同一条变异上
的结论分歧 (§2.3);
**(b)** 语法不合法的变异必须先筛掉, 且 pytest 的 `-rf` 会隐藏收集期 ERROR ——
harness 本身若不查语法就会把"模块导不进来"误读成"断言杀不掉"(§1 作废条目)。

35 条可杀存活变异已全部当场补测试转红, 4 条为等价变异, **冻结期存活变异 0 条**;
`eval/*.py` 与 `server/*.py` 逐字节未动, spec §5.3-2「跑批后判据一字不改」保持成立。
