# U2 Task 3 物理变异实证 (eval 侧 doc 通道接线)

> 2026-08-12 · 实现方自跑 (规则 D: 抽检方 B 另跑一轮, 见 plan Task 9 Step 2)
> 对象: `eval/run_eval.py` 的 `--study-docs` / `--doc-seats` / `--corpus` 与 federated 装配
> 断言方: `scripts/tests/test_run_eval_doc_channel.py`
> 数据红线: 本文件零真名零正文, 只有 flag 名 / 代码锚串 / 计数。

## 0. 一句话

plan 逐字给的 4 条断言**只杀得死 22 条变异里的 5 条**; 方向② (逐行问"这行改坏了谁会红")
的 18 条里 **17 条存活** —— 包括"把整个 doc 通道装配块删光"。补 6 条断言后 **22/22 全红**。

## 1. 基线与口径

| 项 | 值 |
|---|---|
| 开工全量 pytest | `1131 passed` |
| Task 3 新增测试 | `test_run_eval_doc_channel.py` 10 条 (plan 逐字 4 + 补强 6) |
| 收工全量 pytest | `1153 passed, 1 failed` — 唯一的红属**并发 agent** 的 in-flight 文件 (§4) |
| 收工全量 (排除并发文件) | `1129 passed, 0 failed` |
| 单跑本 task 相关三文件 | `59 passed` |

变异跑批口径: 每条对**当前实现态源码**做唯一命中的文本替换 (命中数 ≠ 1 即中止, 防止变异
跑成 no-op), 跑全量 `pytest -p no:warnings`, 记 failed 数, 再写回。跑完核验源码逐字复原。

## 2. 方向① — 从 plan 的 4 条断言出发, 找能杀死它的变异

| ID | 变异 | 全量 failed |
|---|---|---|
| A1 | 删掉 `--study-docs 需要 --federated` 的闸 | **2** |
| A2 | `_FederatedAdapter.__init__` 的 `corpus` 默认值 `"auto"` → `"study"` | **5** |
| A3 | `retrieve` 里 `corpus=self.corpus` 退回硬编码 `corpus="auto"` | **1** |
| A4 | `--corpus` 去掉 `choices=[...]` 白名单 | **2** |

四条全红。

## 3. 方向② — 逐行问"这行改坏了谁会红"

对新增/修改的**每一行**(含每个 kwarg) 各设一条变异:

| ID | 变异 | 全量 failed | 仅 plan 那 4 条时 |
|---|---|---|---|
| B1 | 删掉 `--study-docs` 的 `add_argument` | **26** | 0 ⚠ |
| B2 | 删掉 `--doc-seats` 的 `add_argument` | **2** | 0 ⚠ |
| B3 | `--doc-seats` `default=None` → `default=5` (吞掉 settings 回落) | **1** | 0 ⚠ |
| B4 | `--doc-seats` `type=int` → `type=str` | **1** | 0 ⚠ |
| B5 | 删掉 `--corpus` 的 `add_argument` | **26** | 0 ⚠ |
| B6 | `--corpus` `default="auto"` → `default="study"` | **17** | 0 ⚠ |
| B7 | 删掉 `--corpus 只在 --federated 下有意义` 的闸 | **1** | 0 ⚠ |
| B8 | 删掉 `study_engine = study_rag` (OFF 臂的回落) | **6** | 0 ⚠ |
| B9 | 删掉**整个** `if args.study_docs:` 装配块 + 联邦退回 `study_rag` | **2** | 0 ⚠ |
| B10 | `doc_seats` 的 settings 回落写死成常量 `5` | **2** | 0 ⚠ |
| B11 | docs 引擎 `collection_name` 指到 cards 库 | **1** | 0 ⚠ |
| B12 | docs 引擎 `top_k=doc_seats` → `top_k=args.top_k` (席位不下传) | **2** | 0 ⚠ |
| B13 | `StudyCorpusEngine(study_rag, docs_rag, …)` 两个实参装反 | **1** | 0 ⚠ |
| B14 | `FederatedEngine` 收 `study_rag` 而非 `study_engine` (建了但没接) | **2** | 0 ⚠ |
| B15 | adapter 调用处丢掉 `corpus=args.corpus` | **1** | 0 ⚠ |
| B16 | `self.corpus = corpus` → 恒 `"auto"` | **2** | 1 |
| B17 | docs 引擎 `structured_lookup_enabled=False` → `True` | **1** | 0 ⚠ |
| B18 | docs 引擎 `kb_root` 从 `study_kb_root` 改成 CDISC `kb_root` (破 U1 口径) | **1** | 0 ⚠ |

补强后 18/18 全红。⚠ = 补强前该变异对 plan 给的 4 条断言**完全隐形**。

## 4. 为什么 plan 的 4 条测不出来 (根因, 非"测试写少了")

`--study-docs` / `--corpus` **不存在**时, argparse 自己以
`error: unrecognized arguments: --study-docs` 退出, 抛的同样是 `SystemExit`。
故 `pytest.raises(SystemExit)` 在"闸拒绝"与"flag 根本没实现"两种情形下**同样绿**:

- plan 的 `test_study_docs_requires_federated` 在实现之前就已经 PASS;
- Step 2 "跑测试确认失败" 实测只有 **1 failed, 3 passed**, 与 plan 写的
  `Expected: FAIL — unrecognized arguments: --study-docs` 形态不符 (它确实 unrecognized,
  但那条测试并不因此变红)。

且 plan 的 4 条**没有一条进入 `main()` 的 federated 装配分支** (全部止步于 argparse 或直接
构造 adapter), 所以 `main()` 里新增的 27 行全部无断言覆盖。

补强的 6 条:

| 新断言 | 堵住 |
|---|---|
| `test_study_docs_error_is_the_gate_not_an_unknown_flag` | B1 (断言 stderr 无 `unrecognized` 且含闸文案) |
| `test_corpus_non_auto_requires_federated` | B5 / B7 |
| `test_corpus_choices_are_exactly_the_four` | B5 (断言 `invalid choice` + 四个选项都在) |
| `test_docs_engine_is_built_and_wrapped_and_corpus_reaches_the_adapter` | B2 B4 B9 B11 B12 B13 B14 B15 B17 B18 |
| `test_doc_seats_defaults_to_settings_not_a_hardcoded_constant` | B3 B10 (跑前把 `settings.study_docs_seats` 改成 9, 否则常量 5 与出厂值撞号照不出来) |
| `test_without_study_docs_the_federation_gets_the_bare_cards_engine` | B6 B8 |

装配锁用 stub 顶掉 `RAGEngine` / `create_router` / `FederatedEngine` / `run_evaluation`
(哨兵异常在装配完成处停住) ⇒ 零 chroma 零 embedding 零 LLM, 单文件 ~1s。

## 5. 复跑命令

```bash
cd sdtm-rag
# 断言现状
./.venv/bin/python -m pytest scripts/tests/test_run_eval_doc_channel.py -p no:warnings   # 10 passed
# 任一条变异: 按 §2/§3 的"变异"列改 eval/run_eval.py, 然后
./.venv/bin/python -m pytest -p no:warnings
# 改回后核验
git diff --stat eval/run_eval.py
```

## 6. 回归闸 (plan Task 3 Step 5) — 不加新 flag 时行为逐字不变

```bash
cd sdtm-rag && ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards --output /tmp/u2_t3_regress.json
./.venv/bin/python -c "
import json
a=json.load(open('/tmp/u2_t3_regress.json')); b=json.load(open('data/study/st01/eval/runs/v2_baseline_s2on.json'))
pa={r['id']:r['source_recall'] for r in a['results']}; pb={r['id']:r['source_recall'] for r in b['results']}
d={k:(pa[k],pb[k]) for k in pa if pa[k]!=pb[k]}
print('avg', a['summary']['source_recall_avg'], '| per-q diffs:', d)"
```

实测输出 (2026-08-12): `avg 0.875 | per-q diffs: {}` ⇒ **PASS**。

## 7. 本轮变异**不能**证明什么

1. 变异只证断言**会红**, 不证接线**跑得通** —— 装配锁全程 stub, 从未打开真 chroma
   collection。"`study_st01_docs` 里真有 114 个 chunk 且能被检索到"由 Task 4 的 sweep 负责,
   本轮零证据。
2. 22 条变异是**手挑**的, 不是穷举 —— 未覆盖的形态 (如 `hybrid_*` 三个 kwarg 传错、
   `embedding_model` 换掉) 仍可能无断言。抽检方 B 应独立设计, 不要照抄本表。
3. `--corpus both` 这一支**全程没被任何测试走过** (只测了 `auto` 与 `study`);
   spec §4.2 "both 判库下 doc 席位不缩" 在 eval 侧无断言。
4. 全量 pytest 期间**并发 agent 在改** `server/main.py` / `test_main_study_docs_wiring.py`,
   §1 的收工数字含其 in-flight 状态; 唯一的红
   (`test_docs_engine_shares_every_lever_with_the_cards_engine`) 属该 agent, 不属本 task ——
   排除后 `1129 passed, 0 failed`。
