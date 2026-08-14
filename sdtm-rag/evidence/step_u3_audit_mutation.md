# U3 Task 9 Step 3 — 抽检方 B 变异测试报告 (规则 D 独立 session)

> 角色: 抽检方 B (test-engineer), 独立 session, 未读抽检方 A 的报告 (`evidence/step_u3_audit.md`)。
> 方法: 对本单元新增的全部断言做变异测试, 逐条给 KILLED / SURVIVED; SURVIVED 当场补最小断言并复验。
> **红线声明**: 本报告零题面正文。所有 pytest 输出经机械 scrubber (逐字匹配三个 gitignored yml
> 里全部非白名单键的字符串值) 过滤后才落盘; gold 数据只以 id / group / 数字形态出现。
> 未打开 `data/study/st01/eval/heldout_banned_terms.txt`。

*(报告边做边写 —— 每完成一个变异立即落盘该行。)*

---

## §0 环境与基线

| 项 | 值 |
|---|---|
| 仓库 / 分支 | `/Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag` / `doc-track-u3` |
| HEAD | `0b5578bb4baa9972d03562001870d2922afd5a0b` |
| MERGE_BASE | `9a97d35b` |
| 全量基线 | **1259 passed in 34.46s** (`./.venv/bin/python -m pytest -p no:warnings --tb=no`) |
| 针对性模块 | `test_run_routing_eval.py` + `test_compare_runs.py` + `test_u3_gold_redline.py` = **82 passed in 1.28s** |
| 变异 harness | scratchpad 脚本: apply → 针对性 pytest → restore → sha256 逐字节核对 (见 §6) |
| **本轮结果** | **69 条变异 / 首轮 KILLED 56 · SURVIVED 11 → 补 10 条断言 (16 case) 后 SURVIVED 0** |

题面 scrubber (报告零题面的机械保证): 从三个 gitignored yml 里取出**全部非白名单键**的字符串值
(白名单 = `id`/`gold`/`group`/`chapter`/`expected_sources`/`out_of_scope`, 共 244 条敏感串),
对任何 pytest 原始输出逐字匹配替换后才允许落盘; 命中内容从不打印, 只报条数与字符数。
收尾对本报告自身复扫: **命中 0 条**。

被审面 (`git diff 9a97d35b..HEAD -- eval/ scripts/tests/`, 1086 insertions):

| 文件 | 性质 |
|---|---|
| `eval/compare_runs.py` | 整文件新 (101 行) |
| `eval/run_routing_eval.py` | 新增 `load_u1_doc_gold` / `load_docs_routing_gold` / `score_by_group` / `gate_verdict` / 7 个策略常量 / `load_gold` 三道闸 / `main` 改判据 |
| `eval/u3_task8_verdict.py` | 整文件新 (66 行, 判定脚本) |
| `scripts/tests/test_compare_runs.py` | 整文件新 (17 条) |
| `scripts/tests/test_u3_gold_redline.py` | 整文件新 (12 条, 含 2 个 parametrize×2) |
| `scripts/tests/test_run_routing_eval.py` | 新增部分 (+385 行) |

---

## §1 变异总表

方向: ① 从断言出发 / ② 从代码行出发 / ③ 从断言的逻辑形状出发 (对调型)

| # | 方向 | 目标 (file:symbol) | 变异内容 | 预期红的断言 | 实际 | 处置 |
|---|---|---|---|---|---|---|
| M01 | ② | `run_routing_eval:load_gold` | 删掉 `EXPECTED_GROUP_SIZES` 题量闸整块 (6 行) | `test_trimmed_*_raises` | **KILLED** (2 条) | — |
| M02 | ② | `run_routing_eval:load_gold` | 删掉 `final 组 ≡ FINAL_IDS` 恒等闸整块 (6 行) | `test_final_group_must_equal_final_ids` | **KILLED** (1 条) | — |
| M03 | ② | `run_routing_eval:load_docs_routing_gold` | 删掉 `AUTHORED_GROUPS` 白名单校验整块 | `test_docs_routing_gold_rejects_self_declared_reserved_group` | **KILLED** (2 条) | — |
| M04 | ② | `run_routing_eval:load_u1_doc_gold` | 删掉 `FINAL_IDS 缺失` 校验整块 (3 行) | `test_missing_final_id_raises` | ⚠ **SURVIVED** | 补 A1 → 转 KILLED (§4) |
| M05 | ② | `run_routing_eval:LEGACY_EXACT_FLOOR` | 178 → 170 (放宽阈值族) | `test_policy_constants_match_spec` | **KILLED** (1 条) | — |
| M06 | ② | `run_routing_eval:EXACT_THRESHOLD` | 0.95 → 0.50 (放宽阈值族) | `test_both_is_nonfatal_but_not_exact` | **KILLED** (1 条) | — |
| M07 | ③ | `run_routing_eval:AUTHORED_GROUPS` | 集合放宽: 混入 `"final"` (数据文件即可自称豁免) | `..._rejects_self_declared_reserved_group[final]` | **KILLED** (2 条) | — |
| M08 | ③ | `run_routing_eval:score_run` | 条件反转 `pred != "both"` → `pred == "both"` | 全部 fatal 类断言 | **KILLED** (19 条) | — |
| M09 | ② | `run_routing_eval:score_run` | fatal 分支恒假 (`elif False`) | 全部 fatal 类断言 | **KILLED** (17 条) | — |
| M10 | ③ | `run_routing_eval:gate_verdict` | 对调: `group != "final"` → `group == "final"` | `test_every_non_final_group_is_watched` 等 | **KILLED** (13 条) | — |
| M11 | ③ | `run_routing_eval:gate_verdict` | 悄悄放松: 排除项扩成 `("final","u1_doc")` | `test_every_non_final_group_is_watched[U1]` | **KILLED** (7 条) | — |
| M12 | ③ | `run_routing_eval:gate_verdict` | 悄悄放松: 排除项扩成 `("final","heldout")` | 同上 `[H1]` | **KILLED** (8 条) | — |
| M13 | ③ | `run_routing_eval:gate_verdict` | 双口径混用: `overall` 改从全集算 (final 计入 fatal) | `test_gate_verdict_excludes_final_from_fatal` | **KILLED** (10 条) | — |
| M14 | ③ | `run_routing_eval:gate_verdict` | 对调比较方向 `legacy_exact >= FLOOR` → `<=` | `test_gate_verdict_fails_when_legacy_below_floor` | **KILLED** (2 条) | — |
| M15 | ② | `run_routing_eval:gate_verdict` | 删掉「legacy 子集缺失」参照物守卫 | `test_gate_verdict_raises_without_legacy_subset` | **KILLED** (1 条) | — |
| M16 | ② | `run_routing_eval:score_by_group` | 删掉未知 group 校验整块 | `test_score_by_group_rejects_unknown_group` | **KILLED** (3 条) | — |
| M17 | ③ | `run_routing_eval:score_by_group` | 差集方向对调 `{gold组} - GROUPS` → `GROUPS - {gold组}` | 同上 + 3 条 gate 测试 | **KILLED** (4 条) | — |
| M18 | ② | `run_routing_eval:load_docs_routing_gold` | 删掉空文件闸整块 | `test_empty_docs_routing_gold_raises` | ⚠ **SURVIVED** | 补 A2 → 转 KILLED |
| M19 | ② | `run_routing_eval:load_u1_doc_gold` | 删掉 `load_test_set` 前置空检查 | `test_empty_u1_doc_set_raises` | **KILLED** (2 条) | — |
| M20 | ② | `run_routing_eval:load_u1_doc_gold` | 删掉 `path.exists()` 守卫 | `test_missing_u1_doc_set_raises` | **KILLED** (1 条) | — |
| M21 | ③ | `run_routing_eval:load_u1_doc_gold` | 对调三元: `final`/`u1_doc` 标反 | 14 条 (含 `..._tags_every_item_with_a_group`) | **KILLED** (14 条) | — |
| M22 | ② | `run_routing_eval:FINAL_IDS` | 豁免名单收窄到 2 题 | `test_policy_constants_match_spec` 等 | **KILLED** (13 条) | — |
| M23 | ② | `run_routing_eval:EXPECTED_GROUP_SIZES` | `heldout` 12 → 11 (逐组题量, Task 3 定向) | `test_policy_constants_match_spec` + 真数据闸 | **KILLED** (2 条) | — |
| M24 | ③ | `run_routing_eval:load_gold` | 恒等 → 子集: `!=` → `not final_ids <= set(...)` | 「final 组**少**塞题」方向 | ⚠ **SURVIVED** | 补 A3 → 转 KILLED |
| M25 | ② | `run_routing_eval:load_gold` | 删掉 id 重复闸整块 | `test_duplicate_id_across_sets_raises` | **KILLED** (1 条) | — |
| M26 | ③ | `run_routing_eval:gate_verdict` | 上报值与判据值脱钩: `legacy_floor` 打死 178 | `test_gate_verdict_excludes_final_from_fatal` | **KILLED** (1 条) | — |
| M27 | ② | `run_routing_eval:gate_verdict` | 删过滤: `by_group` 不再剔除 `fatal_items` (泄漏门) | 同上 | **KILLED** (1 条) | — |
| M28 | ③ | `run_routing_eval:main` | 双口径混用: `all_passed` 换回 `score_run` 旧全集口径 | `test_main_rc_follows_gate_verdict` | **KILLED** (1 条) | — |
| M29 | ② | `run_routing_eval:main` | 删掉 `groups:` 输出行 (条款 2/3/4 原料消失) | `test_main_prints_fatal_ids_not_questions` | **KILLED** (1 条) | — |
| M30 | ② | `run_routing_eval:main` | `PASS(条款1)` → 裸 `PASS` (限定词被抹掉) | 无 | ⚠ **SURVIVED** | 补 A4 → 转 KILLED |
| M31 | ② | `compare_runs:load_scores` | 删掉空 `results` 闸整块 | `test_load_scores_rejects_empty_results` | **KILLED** (1 条) | — |
| M32 | ② | `compare_runs:load_scores` | 删掉重复 id 闸整块 | `test_load_scores_rejects_duplicate_id` | **KILLED** (1 条) | — |
| M33 | ③ | `compare_runs:diff_scores` | 集合运算方向: 并集 `|` → 交集 `&` | `test_diff_detects_missing_key_on_either_side` | **KILLED** (1 条) | — |
| M34 | ③ | `compare_runs:diff_scores` | 条件反转: `!=` → `==` (只留相等项) | 同上 | **KILLED** (1 条) | — |
| M35 | ② | `compare_runs:unstable_ids` | 边界: `len(runs) < 2` → `< 1` | `test_unstable_ids_requires_two_runs` | **KILLED** (1 条) | — |
| M36 | ③ | `compare_runs:unstable_ids` | 键集只取第一遍 `set().union(*runs)` → `set(runs[0])` | `..._flags_key_present_in_only_some_runs` | **KILLED** (1 条) | — |
| M37 | ② | `compare_runs:unstable_ids` | 边界: 判定阈 `> 1` → `> 2` | 4 条 | **KILLED** (4 条) | — |
| M38 | ② | `compare_runs:main` | 删掉同路径去重闸 (自我比对恒稳) | `test_main_rejects_same_path_passed_twice` | **KILLED** (1 条) | — |
| M39 | ③ | `compare_runs:load_summary_avg` | 双口径混用: 缺键时静默回退自算均值 | `..._returns_none_when_summary_absent` | **KILLED** (2 条) | — |
| M40 | ③ | `compare_runs:main` | 对调返回码: `1 if unstable else 0` → 反转 | 5 条 | **KILLED** (5 条) | — |
| M41 | ② | `compare_runs:main` | 边界: 静默丢掉第 3 遍及以后 (`args.runs[:2]`) | `..._reads_every_run_not_just_the_first_two` | **KILLED** (1 条) | — |
| M42 | ② | `compare_runs:main` | 删掉逐题 pairwise diff 输出整块 (5 行) | 无 | ⚠ **SURVIVED** | 补 A5 → 转 KILLED |
| M43 | ② | `u3_task8_verdict:条款1` | 放宽阈值: `legacy_exact >= 178` → `>= 170` | 无 (整文件零测试) | ⚠ **SURVIVED** | 补 A7 → 转 KILLED |
| M44 | ③ | `u3_task8_verdict:条款1` | 双口径: `fatal_excl_final == 0` → `>= 0` (恒真) | 无 | ⚠ **SURVIVED** | 补 A7 → 转 KILLED |
| M45 | ③ | `u3_task8_verdict:条款2` | **对调两个口径**: `hold >= dev-25` → `dev >= hold-25` | 无 | ⚠ **SURVIVED** | 补 A8 → 转 KILLED |
| M46 | ③ | `u3_task8_verdict:条款4` | **对调两个操作数**: `b-a <= 1` → `a-b <= 1` | 无 | ⚠ **SURVIVED** | 补 A9 → 转 KILLED |
| M47 | ② | `u3_task8_verdict:条款3` | 放宽阈值: `dev >= 10` → `>= 5` | 无 | ⚠ **SURVIVED** | 补 A10 → 转 KILLED |
| M48 | ③ | `run_routing_eval` (组合) | **M04 + M24 同时施加** (两道 final 名单闸是否互为唯一守护) | `test_missing_final_id_raises` | **KILLED** (1 条) | 见 §3 分析 |
| M49 | ② | `run_routing_eval:AUTHORED_GROUPS` | 白名单**收窄** (删掉 `ambiguous_both`, Task 3 定向) | 21 条 | **KILLED** (21 条) | — |
| M50 | ② | `run_routing_eval:GROUPS` | 顺序改变 (`legacy` 挪到末尾) | `test_policy_constants_match_spec` | **KILLED** (1 条) | — |
| M51 | ② | `run_routing_eval:load_gold` | 删标注: ja 补充题不再打 `group="legacy"` | 14 条 | **KILLED** (14 条) | — |
| M52 | ② | `run_routing_eval:score_by_group` | 空组不再丢弃 (静默进结果 dict, 参照物守卫失效) | `test_gate_verdict_raises_without_legacy_subset` | **KILLED** (1 条) | — |
| M53 | ② | `run_routing_eval:score_run` | 边界: 上报的 `n` 少一 (口径与实际脱钩) | 10 条 | **KILLED** (10 条) | — |
| M54 | ③ | `run_routing_eval:gate_verdict` | 双口径混用: `fatal_ids_excl_final` 改从全集汇总 | `test_gate_verdict_excludes_final_from_fatal` | **KILLED** (2 条) | — |
| M55 | ② | `run_routing_eval:main` | `detail` 不再含题面 (为红线把明细也删了) | `..._writes_detail_with_questions_to_runs_dir_only` | **KILLED** (1 条) | — |
| M56 | ② | `run_routing_eval:main` | 泄漏门: 逐题 `detail` 被塞进 `summary` | 同上 | **KILLED** (1 条) | — |
| M57 | ② | `run_routing_eval:load_docs_routing_gold` (+`load_supplement`) | **Task 5 红线修法改回 `{q!r}`** (整条 item 含题面进异常消息) | 无 | ⚠ **SURVIVED** | 补 A6 → 转 KILLED |

### §1.1 gitignored gold 数据文件变异 (删题族主战场) + git 状态变异

| # | 方向 | 目标 | 变异内容 | 实际 | 红的断言 |
|---|---|---|---|---|---|
| D1 | ① | `routing_gold_docs.yml` | **删整组**: `heldout` 12 题全删 (42→30) | **KILLED** (5 条) | 划分/摘要/对称性/真数据题量闸 |
| D2 | ① | `routing_gold_docs.yml` | **删单题**: 删第一条 (42→41) | **KILLED** (3 条) | `..._preserves_draft_questions` / `..._deterministic_split_...` / 题量闸 |
| D3 | ① | `routing_gold_docs.yml` | **删到剩极少**: 只留 1 题 (42→1) | **KILLED** (5 条) | 同 D1 |
| D4 | ① | `test_set_docs_v1.yml` | 删掉 `FINAL_IDS` 之一 (`docs_v1_q53`, 30→29) | **KILLED** (2 条) | `load_u1_doc_gold` 的 FINAL_IDS 闸 |
| D5 | ① | `test_set_docs_v1.yml` | 删到只剩 `FINAL_IDS` 三题 (30→3) | **KILLED** (2 条) | 题量闸 (`u1_doc: (0, 27)`) |
| D6 | ② | `routing_gold_docs_draft.yml` | 语义等价重 dump (仅字节变) | **KILLED** (1 条) | `test_draft_is_frozen_at_the_authored_bytes` |
| D7 | ③ | `routing_gold_docs.yml` | **对调型 cherry-pick**: 一对 dev/heldout 互换, 组量仍 12/12 | **KILLED** (1 条) | **仅** `..._is_exactly_the_deterministic_split_of_the_draft` |
| D8 | ① | `routing_gold_docs.yml` | 改题面 (摘要 `30c9bb87b88c`→`5eb64a828dfa`) | **KILLED** (1 条) | **仅** `test_final_gold_preserves_draft_questions` |
| D9 | ① | git 索引 | `git add -f` 把 gitignored gold 加进索引 | **KILLED** (2 条) | `test_gold_file_is_not_tracked[path1]` + `..._is_gitignored[path1]` |
| D10 | ① | `sdtm-rag/.gitignore` | 取消 `data/study/` 忽略规则 | **KILLED** (2 条) | `test_gold_file_is_gitignored[path0/1]` |

D1-D5 的失败消息可读性实测 (经 scrubber, 只含 id/组名/计数):
`ValueError: gold 组题量与 spec §5.2 不符 (实际, 期望): {'heldout': (0, 12)} —— 闸口题量被改动, 拒绝继续`;
`... {'u1_doc': (0, 27)} ...`; `... FINAL_IDS 缺失 ['docs_v1_q53'] —— 条款 5 无报告对象, 拒绝继续`。
**结论: 删题一定红, 且消息直接点名「哪一组、少了几题」, 可读。**

---

## §2 必测变异族 (spec §8 点名)

### §2.1 删题族 — 8 条, 全 KILLED

覆盖三种删法 × 两个 gitignored gold 文件 (D1-D5), 外加改题面 (D8) 与 git 状态 (D9/D10)。

| 删法 | 哪个闸红 | 消息可读吗 |
|---|---|---|
| **整组删** (heldout 12 题, D1) | `load_gold` 题量闸 + 划分/对称性 4 条 | ✅ `{'heldout': (0, 12)}` —— 直接点名组与差额 |
| **单题删** (D2) | 题量闸 + `..._preserves_draft_questions` + `..._deterministic_split_...` | ✅ `{'dev': (11, 12)}` |
| **删到剩极少** (42→1, D3) | 题量闸一次点名 4 组 + 对称性 | ✅ `{'dev': (1,12), 'heldout': (0,12), 'distractor_cdisc': (0,12), 'ambiguous_both': (0,6)}` |
| **删 FINAL_IDS 之一** (D4) | `load_u1_doc_gold` 的 FINAL_IDS 闸 | ✅ `FINAL_IDS 缺失 ['docs_v1_q53'] —— 条款 5 无报告对象` |
| **U1 删到只剩 FINAL_IDS 三题** (D5) | 题量闸 | ✅ `{'u1_doc': (0, 27)}` |

**结论**: spec §7「不许从 gold 删题」有真正的执行者。消息一律只含组名 / id / 计数 ——
删题的红灯本身不构成泄漏风险, 可以直接贴进证据文件 (上表即是)。

补充: 源码侧把题量闸整块删掉 (M01) 立刻被 `test_trimmed_*_raises` 两条抓住,
所以「闸被拆掉」和「题被删掉」两个方向都有断言。

### §2.2 放宽阈值族 — 5 条

| 阈值 | 变异 | 结果 |
|---|---|---|
| `LEGACY_EXACT_FLOOR` 178→170 | M05 | **KILLED** — `test_policy_constants_match_spec` (Task 1 修复轮已补, 「已修确认」) |
| `EXACT_THRESHOLD` 0.95→0.50 | M06 | **KILLED** — `test_both_is_nonfatal_but_not_exact` |
| `EXPECTED_GROUP_SIZES.heldout` 12→11 | M23 | **KILLED** — 常量断言 + 真数据闸各一条 |
| `u3_task8_verdict` 条款 1 floor 178→170 | M43 | ⚠ **SURVIVED** → 补 A7 |
| `u3_task8_verdict` 条款 3 `dev>=10`→`>=5` | M47 | ⚠ **SURVIVED** → 补 A10 |

**注意分裂**: 同一个 178, 写在 `run_routing_eval` 里有断言盯着, 抄进判定脚本的那一份没有。
阈值被复制到第二处而只有第一处受守护, 是这一族最值得记的形态。

### §2.3 双口径混用族 — 9 条

| 变异 | 结果 |
|---|---|
| M13 `fatal_excl_final` 改从全集算 (final 计入) | **KILLED** (10 条) |
| M11 / M12 排除项从 `final` 悄悄扩成 `(final,u1_doc)` / `(final,heldout)` | **KILLED** (7 / 8 条) —— `test_every_non_final_group_is_watched` 逐组参数化正面拦住 |
| M54 `fatal_ids_excl_final` 改从全集 `by_group` 汇总 | **KILLED** (2 条) |
| M28 `main` 的 `all_passed` 换回 `score_run` 旧全集口径 | **KILLED** (1 条) |
| M08 / M09 `score_run` 的 `pred != "both"` 反转 / 恒假 | **KILLED** (19 / 17 条) |
| M39 `load_summary_avg` 缺键时静默回退自算 | **KILLED** (2 条) |
| M45 判定脚本条款 2 的 `hold`/`dev` 互换 | ⚠ **SURVIVED** → 补 A8 |
| M46 判定脚本条款 4 的基线/改动后互换 | ⚠ **SURVIVED** → 补 A9 |

`run_routing_eval` 侧的双口径防线**完好**且是本单元最结实的一段 —— 尤其 `_G7`
(覆盖全部 7 组) 配 `test_every_non_final_group_is_watched` 逐组参数化, 把「排除项多写一组」
这个最自然的悄悄放松形态正面钉死。判定脚本侧则是完全裸奔。

---

## §3 已知历史盲区定向探针

### §3.1 Task 3 修过的三处 — 全部**已修确认**, 且站得住

| 探针 | 变异 | 结果 |
|---|---|---|
| `AUTHORED_GROUPS` 白名单 | M07 放宽 (混入 `final`) / M49 收窄 (删 `ambiguous_both`) | **KILLED** 2 条 / 21 条 —— 两个方向都有断言 |
| `final` 组 ≡ `FINAL_IDS` 恒等断言 | M02 整块删 / M22 名单收窄 / **M24 恒等→子集** | 前两个 KILLED; **M24 SURVIVED** (见 §3.4) |
| `EXPECTED_GROUP_SIZES` 逐组题量 | M23 改一组数 / M01 删整块 | **KILLED** 2 条 / 2 条 |

### §3.2 Task 5 泄漏修法 — **已修确认**, 三档 tb 实测零泄漏

制造真失败 (三种畸形形态), 逐档统计题面命中数。**统计方式**: 把三个 gitignored yml 里
全部非白名单键的字符串值逐字匹配原始输出, 只记条数与字符数, 命中内容不落盘。

| 失败形态 | `--tb=short` | `--tb=long` | `--tb=auto` (不写 --tb, 默认) |
|---|---|---|---|
| P1 条目缺 `id` (Task 5 原变异复刻, 打 `_load` 这条路) | 零泄漏 ✓ | 零泄漏 ✓ | 零泄漏 ✓ |
| P2 条目缺 `gold` (打生产码 `load_docs_routing_gold` 的 gold 校验) | 零泄漏 ✓ | 零泄漏 ✓ | 零泄漏 ✓ |
| P3 条目缺 `question` (打生产码缺键 raise) | 零泄漏 ✓ | 零泄漏 ✓ | 零泄漏 ✓ |

**P4 诚实边界复核**: 文件头自陈「`--showlocals` 仍会露」—— 实测属实, 同一失败下
三档均 **含泄漏 2 条 / 1025 字符 (已抑制)**。自陈与实测一致, 没有夸大也没有隐瞒。

### §3.3 Task 1 deferred 项 — 撞上 1 个, 按「已知 deferred」处理

- **CLI avg 口径**: 修复轮 2 已修, M39 (缺键回退自算) 被两条断言抓住 —— 已不是 deferred。
- `sorted` 无 `PYTHONHASHSEED` 守护 / `rc=1` 双义: 本轮未新增证据, 维持 deferred, 不计新 finding。

### §3.4 新发现的盲区形态: 两道闸互为唯一守护 (M04 + M24)

这是本轮最值得记的结构性发现, 也是 U2 §4.1 方向③ 的一个新变种。

`final` 名单被两道闸守着 —— `load_u1_doc_gold` 的「FINAL_IDS 缺失」与 `load_gold` 的
「final 组 ≡ FINAL_IDS」。实测:

- 单删前者 (M04) → **SURVIVED**: `test_missing_final_id_raises` 的 `match="FINAL_IDS"`
  转而命中了**后者**的消息 (那条消息里恰好也有 `FINAL_IDS` 这七个字符), 断言绿着,
  但它盯的已经不是它名字所说的那道闸。
- 单把后者放宽成子集判断 (M24) → **SURVIVED**: `test_final_group_must_equal_final_ids`
  只造了「多塞一题」, 少塞的方向由前者兜着。
- **同时施加 (M48) → KILLED**: 两道都塌了才有测试红。

即: 每道闸各自都可以被静默拆掉, 断言集合只保证「两道之中至少剩一道」。
`load_u1_doc_gold` 还被 `test_real_gold_files_match_expected_sizes` 直接调用,
那条路上根本没有兜底。修法是让每道闸各自按**函数边界**被钉住, 并 match 本闸独有的措辞
(A1 用 `"条款 5 无报告对象"`, A3 用 `"缺少"`), 而不是共有的 `FINAL_IDS` 字样。

### §3.5 新发现: 红线修法自身没有回归守卫 (M57) — 本轮最重要的一条

`load_docs_routing_gold` / `load_supplement` 的异常消息在 Task 5 从 `f"...: {q!r}"`
改成只打序号与 id。把它**改回去** (M57):

- 针对性模块 82 条 **全绿**, 全量 1259 条也全绿 —— 没有任何断言察觉。
- 而同一畸形数据 (条目缺 `id` 但保留 `question`) 下实测:
  基线态三档 tb 均**零泄漏**; M57 变异态三档均 **含泄漏 1 条 / 76 字符 (已抑制)**。

即: 本仓最硬的那条红线, 其生产码侧的修法此前只靠人记得, 没有机器守着。
`test_u3_gold_redline.py` 文件头写着「红线的成立条件是『所有路径』」并列出三条路,
第 3 条 (生产码异常消息) 恰恰是唯一没有断言的一条。已补 A6。

> 一处细节值得留档: 第一次探这个洞时我删的是条目的 `question` 字段, 结果零泄漏 ——
> 因为 `{q!r}` 打的那个 dict 里正好没有题面了。**探针把自己要找的东西先删掉了。**
> 换成「缺 `id` 但留 `question`」才复现。同类探针今后要先确认畸形形态保留了敏感字段。

---

## §4 SURVIVED 处置与补断言清单

首轮 67 条变异 → **KILLED 56 / SURVIVED 11**。11 条全部当场补断言并复验转 KILLED。

### §4.1 补的断言 (10 条断言 / 16 个 test case)

| # | 对应变异 | 落点 | 断言一句话 |
|---|---|---|---|
| **A1** | M04 | `test_run_routing_eval.py::test_load_u1_doc_gold_itself_rejects_missing_final_id` | 按**函数边界**调 `load_u1_doc_gold`, match 本闸独有措辞 `"条款 5 无报告对象"` |
| **A2** | M18 | `test_empty_docs_routing_gold_raises` (原地加 `match="为空"`) | 与兄弟测试 `test_empty_u1_doc_set_raises` 的 match 口径对齐, 分辨得出是哪道闸红 |
| **A3** | M24 | `..._final_group_must_not_be_short_of_final_ids` | final 组**少**一题的方向, match `"缺少"` |
| **A4** | M30 | `..._main_qualifies_the_verdict_with_the_clause_it_checks` (×2 参数) | stdout 判定词必须带 `(条款1)` 限定 |
| **A5** | M42 | `test_compare_runs.py::test_main_prints_the_pairwise_diff_section` | 两遍比对必须真的打出 `pairwise diff: N` 段头与逐题行 |
| **A6** | M57 | `..._gold_loader_error_message_carries_no_question_text` (×2 参数) | 两个 loader 的异常消息不得含题面, 且仍须能定位到第几条 |
| **A7** | M43/M44 | `test_u3_task8_verdict.py` ×2 | 条款 1 的 floor 与 fatal 判据各自可触发 |
| **A8** | M45 | 同上 `..._clause_2_measures_heldout_against_dev_not_the_reverse` | 条款 2 的**方向**: dev 满分 / held-out 零分必须触发 |
| **A9** | M46 | 同上 `..._clause_4_measures_drop_from_baseline_not_the_reverse` | 条款 4 的**方向**: 干扰题从基线掉下去必须触发 |
| **A10** | M47 | 同上 `..._clause_3_triggers_below_the_dev_floor` + 底稿全 PASS + 三组归因 ×3 | 条款 3 阈值; 并核「只有该条红」以保证归因 |

新增测试模块 `scripts/tests/test_u3_task8_verdict.py` (9 个 case): 判定脚本此前**零测试**,
而它是本单元 FAIL 结论的唯一出处。做法是在 `tmp_path` 里造合成 run 产物再跑真脚本
(脚本按相对路径读 `runs/`, 用 cwd 隔离), 不碰真实产物、不发 LLM 请求、合成题面是占位串。

### §4.2 复验: 11 条 SURVIVED 全部转 KILLED

| 变异 | 复验后红的断言 |
|---|---|
| M04 | `test_load_u1_doc_gold_itself_rejects_missing_final_id` |
| M18 | `test_empty_docs_routing_gold_raises` ×2 |
| M24 | `test_final_group_must_not_be_short_of_final_ids` |
| M30 | `..._qualifies_the_verdict_with_the_clause_it_checks` ×2 |
| M42 | `test_main_prints_the_pairwise_diff_section` |
| M57 | `..._error_message_carries_no_question_text` ×2 |
| **M57a** (新增, 只改 `load_docs_routing_gold` 一处) | `...[load_docs_routing_gold]` —— 参数化两分支各自有效, 非靠另一处兜底 |
| **M57b** (新增, 只改 `load_supplement` 一处) | `...[load_supplement]` |
| M43 / M44 | `..._clause_1_triggers_when_legacy_is_below_the_floor` / `..._on_any_non_final_fatal` |
| M45 | `..._clause_2_measures_heldout_against_dev_not_the_reverse` + 归因用例 `[heldout]` |
| M46 | `..._clause_4_measures_drop_from_baseline_not_the_reverse` + 归因用例 `[distractor]` |
| M47 | `..._clause_3_triggers_below_the_dev_floor` |

含 M57a/M57b 两条新增单点变异, **本轮变异总数 69 条, 最终 SURVIVED 0 条**。

---

## §5 三方向覆盖自述

**方向① 从断言出发** (逐条新断言问「什么样的实现 bug 会让它红」, 构造该 bug):
覆盖了新增断言的每一条。`test_u3_gold_redline.py` 12 条全部由 D1-D10 十条数据/git 状态变异
逐条打到 (删题 / 改题面 / 对调划分 / 改 draft 字节 / `git add -f` / 改 `.gitignore`);
`test_compare_runs.py` 17 条由 M31-M42 打到; `test_run_routing_eval.py` 新增部分由
M01-M30 + M49-M57 打到。**发现两条断言并非在盯自己名字所说的东西** (M04 的 `match="FINAL_IDS"`
命中了另一道闸; M18 的裸 `pytest.raises(ValueError)` 命中了题量闸)。

**方向② 从代码行出发** (逐块新增源码行问「这行改坏了谁会红」):
`eval/` 三个文件的每个新增逻辑块至少一个变异, 三种手法齐备 ——
删整块 (M01/M02/M03/M04/M15/M16/M18/M19/M20/M25/M27/M29/M31/M32/M38/M42)、
改边界值 (M05/M06/M22/M23/M35/M37/M41/M43/M47/M53)、
集合运算方向 (见方向③)。`u3_task8_verdict.py` 66 行整文件此前**零测试**, 5 条变异全存活,
是「删光整块一条不红」在本单元的对应物 —— 只不过这里不用删, 改一个比较符就够。

**方向③ 从断言的逻辑形状出发 (对调型)** —— 共 19 条, 是本轮占比最高的一族:
`!=`↔`==` (M08/M10/M34)、差集方向对调 (M17: `{gold组}-GROUPS` ↔ `GROUPS-{gold组}`)、
并集↔交集 (M33)、`>=`↔`<=` (M14)、恒等↔子集 (M24)、三元两支对调 (M21)、
排除项扩大 (M11/M12)、口径互换 (M13/M28/M54/M39)、返回码反转 (M40)、
键集只取首遍 (M36)、**判定脚本两个口径互换 (M45) 与两个操作数互换 (M46)**、
数据侧 cherry-pick 对调 (D7)。
其中 **M24 / M45 / M46 三条对调型存活**, 占全部存活数的 27% —— 与「对调型是集合/差集类断言的
系统性盲区」这个先验一致, 本轮把本仓的命中记录从 5 次推到 8 次。

D7 值得单独说: 一对 dev/heldout 互换后组量仍是 12/12, 全仓**只有**
`test_final_gold_is_exactly_the_deterministic_split_of_the_draft` 一条断言能看见它 ——
该文件头对此的自述属实, 不是自夸。同理 D8 (改题面) 也只有
`test_final_gold_preserves_draft_questions` 一条。这两条是单点故障, 但确实存在。

---

## §6 sha256 复原核对表

变异纪律: 每次变异前记 sha256, 变异后只跑针对性模块, 复原后逐字节核对; 任何一次不一致立即中止。
**69 次变异 × 每次一轮核对, 全部 EXACT MATCH, 零次 MISMATCH。**

| 文件 | 基线 sha256 | 全部变异复原后 | 核对 |
|---|---|---|---|
| `eval/run_routing_eval.py` | `dcfd0ec0…6764700a` | `dcfd0ec0…6764700a` | **EXACT** |
| `eval/compare_runs.py` | `0462fbb3…3d86df4e` | `0462fbb3…3d86df4e` | **EXACT** |
| `eval/u3_task8_verdict.py` | `ec985a82…2530f988a`(*) | 同左 | **EXACT** |
| `scripts/tests/test_u3_gold_redline.py` | `e1bffc80…6abcadabe`(*) | 同左 (未改) | **EXACT** |
| `data/study/st01/eval/routing_gold_docs.yml` (gitignored) | `b48e3f2e…82aa2bcb` | 同左 | **EXACT** |
| `data/study/st01/eval/routing_gold_docs_draft.yml` (gitignored) | `b1373fd8…88d94099` | 同左 | **EXACT** |
| `data/study/st01/eval/test_set_docs_v1.yml` (gitignored) | `e00b8cbd…9bfa4520a3`(*) | 同左 | **EXACT** |
| `sdtm-rag/.gitignore` | `dc916685…903b3245f`(*) | 同左 | **EXACT** |

(*) 表中截断显示; 完整值见下方 harness 输出。三个 gitignored 数据文件在动手前已复制到
session scratchpad 备份, 复原一律从备份 `cp` 回来再核 sha, 不依赖 git。

**我主动修改并保留的两个测试文件** (补断言, 属预期变更):

| 文件 | 改前 sha256 | 改后 sha256 |
|---|---|---|
| `scripts/tests/test_run_routing_eval.py` | `c9d272f3e150b0a3b09340f12cb74543c80e682ed91a25149766313975741b41` | `38d3fee97259af847c81d9e3d8ece9b953fec56369fadcff405c56842f3ec951` |
| `scripts/tests/test_compare_runs.py` | `7cc91516c16544c3a644b5c60d57dc2efc53c85f6fb8c12fce5d3e8becf0410b` | `acb7edc4d8645e2e4a2b26da350b0d6bddcd76481188ee16e5434199559e9d60` |
| `scripts/tests/test_u3_task8_verdict.py` | (新建) | `32b10428b2b3702b9c9f20b491e1fefd3e80b08d43b2f8734cecde7b424164d4` |

收尾核对 (harness `verify`, 全部 OK):

```
OK  eval/run_routing_eval.py  dcfd0ec04f8370a82bd18e82b154a9782d78fa67ed1a55b3332fbcfd6764700a
OK  eval/compare_runs.py  0462fbb3dde04d8e14064fc13cd2787286febeab88544b0d03bed03d3b86df4e
OK  eval/u3_task8_verdict.py  ec985a823e3c582d93e0c3c35373763742fe4108e01dd95e741c66c2530f988a
OK  scripts/tests/test_run_routing_eval.py  38d3fee97259af847c81d9e3d8ece9b953fec56369fadcff405c56842f3ec951
OK  scripts/tests/test_compare_runs.py  acb7edc4d8645e2e4a2b26da350b0d6bddcd76481188ee16e5434199559e9d60
OK  scripts/tests/test_u3_gold_redline.py  e1bffc801bf6c22f9e63f170ece10584ba998062f350a7a27f842a16abcadabe
OK  scripts/tests/test_u3_task8_verdict.py  32b10428b2b3702b9c9f20b491e1fefd3e80b08d43b2f8734cecde7b424164d4
OK  data/study/st01/eval/routing_gold_docs.yml  b48e3f2ed98fb1a567b3baa29057c8c2af760572fe92859487c78b6282aa2bcb
OK  data/study/st01/eval/routing_gold_docs_draft.yml  b1373fd81214b11816b817b5c24539fac3e9753c6f1ada7b34f4921b88d94099
OK  data/study/st01/eval/test_set_docs_v1.yml  e00b8cbd95aaffe61ff6548c70d3d700d23b0abc67398e1b26594bd9fa4520a3
```

**未碰** `server/` 与 `data/study/st01/docs/` (`git status --short` 对这两个路径为空);
**未打开** `data/study/st01/eval/heldout_banned_terms.txt`。
git 状态变异 (D9 `git add -f` / D10 改 `.gitignore`) 在同一条命令内完成施加与复原,
复原后 `git status --short` 已核对回到原状。

---

## §7 收尾: 全量 pytest + git status

复跑命令 (与基线同一条):

```
./.venv/bin/python -m pytest -p no:warnings --tb=no
```

末两行:

```
...................................................                      [100%]
1275 passed in 35.25s
```

基线 1259 → **1275 passed** (+16 = 本轮补的 16 个 test case), **0 failed / 0 error**。

`git status --short`:

```
 M scripts/tests/test_compare_runs.py
 M scripts/tests/test_run_routing_eval.py
?? evidence/step_u3_audit.md
?? evidence/step_u3_audit_mutation.md
?? scripts/tests/test_u3_task8_verdict.py
```

逐条说明:
- `M scripts/tests/test_compare_runs.py` (+17 行) / `M scripts/tests/test_run_routing_eval.py` (+69 行) —— 我补的断言, 只增不删 (`85 insertions(+), 1 deletion(-)`, 那 1 删是 A2 把裸 `pytest.raises(ValueError)` 换成带 `match=` 的同一行)。
- `?? scripts/tests/test_u3_task8_verdict.py` —— 我新建的测试模块 (A7-A10)。
- `?? evidence/step_u3_audit_mutation.md` —— 本报告。
- `?? evidence/step_u3_audit.md` —— **抽检方 A 的报告, 与我无关**。session 开始前即已是未跟踪状态, 我全程未读、未改 (规则 D 独立性)。

被审的三个源文件 (`eval/run_routing_eval.py` / `eval/compare_runs.py` / `eval/u3_task8_verdict.py`)
**不在 git status 中出现** = 69 次变异全部干净复原。

---

## §8 一句话结论

`eval/run_routing_eval.py` 与 `eval/compare_runs.py` 的断言集合**结实**——
59 条变异只漏 6 条, 且漏的都是「守卫被另一道守卫的消息意外覆盖」或「只写在注释里的意图」,
不是判定逻辑本身。真正的缺口有两个, 都已补上:
**(1) `eval/u3_task8_verdict.py` 整文件零测试** —— 它是本单元 FAIL 结论的唯一出处,
5 条变异 (含两条对调型) 能把结论翻面而不留痕迹;
**(2) Task 5 的红线修法没有回归守卫** —— 改回 `{q!r}` 全仓 1259 条全绿, 而实测真泄题面。
