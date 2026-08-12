# U2 Task 3b 物理变异实证 (docs 引擎构造去重 + 两路径同源闸)

> 2026-08-12 · 实现方自跑 (规则 D: 审阅/抽检另派 subagent)
> 对象: `server/study_corpus.py` 的 `make_docs_engine` 工厂 · `server/main.py` lifespan ·
> `eval/run_eval.py` federated 分支
> 断言方: `scripts/tests/test_docs_engine_parity.py` (新, 4 条) ·
> `scripts/tests/test_study_corpus.py` 工厂段 (新, 10 条含 7 条 parametrize)
> 数据红线: 本文件零真名零正文, 只有代码锚串 / 计数 / 可复跑命令。

## 0. 一句话

13 条变异 **13/13 全红**。其中**共错型 C4** (两条路径同时把 docs 引擎指到卡片库) 证实了
Global Constraint 12③ 的预判: **本 task 核心的"两个 dict 相等"那一行对它完全无效**, 杀死它的
是紧随其后的方向断言 —— 逐字 traceback 见 §4。

## 1. 基线与口径

| 项 | 值 |
|---|---|
| 开工全量 pytest | `1138 passed` (`--ignore=scripts/tests/test_federation.py`, 并发 agent 在改) |
| 本 task 新增测试 | 14 条 (parity 4 + study_corpus 工厂段 10) |
| 收工全量 pytest | `1152 passed, 0 failed` (同上 ignore) |
| 首跑失败形态 | parity 3 failed / 1 passed; `test_study_corpus.py` collection ImportError |
| 变异跑批 sha 基线 | `study_corpus 74aa9d6d…` `main e4fbacea…` `run_eval 45240ec4…` |

跑批口径 (Global Constraint 11):

- 脚本在**私有子目录** `<scratchpad>/task3b/`, 不与并发 agent 共享路径;
- 变异 = 对**当前实现态源码**做锚定文本替换, **锚点命中数 ≠ 1 当场中止**
  (实测触发过 2 次: `top_k=seats,` 与 `seats=s.study_docs_seats,` 各自撞上注释/日志行里的
  同形串 —— 若无此闸, 这两条会跑成 no-op 而被误读成"断言是装饰品");
- 每轮 `subprocess` 子超时 300s; 每轮跑完立刻按开跑前留下的**原始字节**写回并核 sha256;
- 收尾打印 `RESTORED True` + 逐文件 sha 对照 + `PENDING marker present: False`。

## 2. 方向① — 从断言出发, 找能杀死它的变异

| ID | 变异 | 全量 failed |
|---|---|---|
| A1 | 工厂 `structured_lookup_enabled` 翻 `True` (docs 引擎误配成 CDISC 直查通道) | **7** |
| A2 | 工厂 `top_k=seats` 改写死常量 `15` (席位数调不动) | **8** |
| A3 | 工厂的 levers 冲突闸拆掉 (`clash = []`) | **7** |
| A4 | 把 `study_lookup` 从工厂自管键里删掉 (S2 可经 levers 混进 docs 引擎) | **1** |

A4 只死 1 条 (`test_factory_rejects_levers…[study_lookup]`) 是**设计如此**: 其余六个自管键
撞 Python 的 duplicate-keyword `TypeError`, 唯独 `study_lookup` 不与任何显式实参重名, 会被
**静默**透传 —— 那正是这条闸唯一非冗余的用途。

## 3. 方向② — 从代码行出发, 问"这行改坏了谁会红"

| ID | 变异 | 全量 failed |
|---|---|---|
| B1 | 生产侧**绕过工厂**: `main.py` 里放一份逐字相同的本地副本 (kwargs 一字不差) | **1** |
| B2 | 尺子侧**绕过工厂**: `run_eval.py` 里放一份逐字相同的本地副本 | **1** |
| B3 | 尺子侧 `study_levers` 漏掉 `rerank_enabled` (= Task 3 原缺陷的形状) | **2** |
| B4 | 生产侧 `study_levers` 漏掉 `hybrid_pool` (两台引擎**一起**丢, 差集不变) | **1** |
| B5 | 生产侧 `levers=study_levers` 改 `levers={}` (docs 引擎裸奔) | **3** |

B1/B2 是本 task 的**存在理由**: 两份副本参数一字不差 ⇒ 任何只比 kwargs 的断言都全绿,
唯一杀得死它的是 `test_both_paths_build_the_docs_engine_through_the_one_factory` (钉调用
本身)。B4 同理落在跨路径键集差断言上 —— 一路掉一个 lever, 另一路没掉。

## 4. 方向③ — 从断言的逻辑形状出发 (对调型 / 共错型)

本 task 的核心断言是 `{k: prod[k] …} == {k: evl[k] …}`, 属**集合/相等**形状, 正是
Global Constraint 12③ 点名的系统性盲区。四条针对性变异:

| ID | 变异 (双点, 差集/集合一字不变) | 全量 failed | 杀死它的那一行 |
|---|---|---|---|
| C1 | 尺子侧 `StudyCorpusEngine` 两台引擎**实参互换** | **1** | `study_engine.cards is engines[1]` (Task 3 遗留断言) |
| C2 | 生产侧 cards.`top_k` ↔ docs.`seats` **互换** (15/5) | **3** | 跨路径相等行 (只动了一条路径) |
| C3 | 尺子侧 cards ↔ docs 的 `collection_name` **互换** | **3** | 跨路径相等行 (同上) |
| C4 | **共错型**: 两条路径**同时**把 docs 引擎指到卡片库 | **7** | ⚠ **方向断言**, 不是相等行 |

C4 逐字 traceback (复跑命令见 §5):

```
>       assert prod["collection_name"] == settings.study_docs_collection_name
E       AssertionError: assert 'study_st01' == 'study_st01_docs'
```

即: 相等行 `{k: prod[k] …} == {k: evl[k] …}` 在 C4 下**照绿**(两边一起错, 仍然逐键相等),
下一行的方向断言才把它打红。**结论: 凡跨路径同源比对, 相等之后必须逐条钉"等在哪个值上",
否则"两条路径一起指错"是完全静默的**, 而那恰恰是复制粘贴式漂移最可能的落点。

C2/C3 是单路径对调, 相等行够用; 但同一形状一旦变成双路径 (C4) 相等行即失效 —— 两者的差别
只是"改了几处", 不是"改得多离谱"。

## 5. 复跑命令 (逐字)

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
# 全量 (并发 agent 在改 test_federation.py, 故排除)
./.venv/bin/python -m pytest -p no:warnings --ignore=scripts/tests/test_federation.py
# 本 task 三文件
./.venv/bin/python -m pytest scripts/tests/test_docs_engine_parity.py \
  scripts/tests/test_study_corpus.py scripts/tests/test_main_study_docs_wiring.py \
  scripts/tests/test_run_eval_doc_channel.py -p no:warnings
# 变异跑批 (脚本在私有 scratchpad, 不进 git):
#   <scratchpad>/task3b/mutate.py                 全 13 条
#   <scratchpad>/task3b/mutate.py --only=C2,C3,C4 指定条目
#   <scratchpad>/task3b/mutate.py --show=C4       单条 + 完整 traceback (看是哪一行杀的)
#   <scratchpad>/task3b/mutate.py --restore-only  崩溃后修复
```

## 6. 回归闸 (重构不许动数字)

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards --output /tmp/u2_t3b_regress.json
./.venv/bin/python -c "
import json
a=json.load(open('/tmp/u2_t3b_regress.json')); b=json.load(open('data/study/st01/eval/runs/v2_baseline_s2on.json'))
pa={r['id']:r['source_recall'] for r in a['results']}; pb={r['id']:r['source_recall'] for r in b['results']}
print('avg', a['summary']['source_recall_avg'], '| per-q diffs:', {k:(pa[k],pb[k]) for k in pa if pa[k]!=pb[k]})"
```

实测 `avg 0.875 | per-q diffs: {}` ✅

⚠ 该命令走的是**非联邦** `--collection` 路径, **不经过**本 task 改的 federated 装配块。
故另跑一条真正覆盖改动的 (`--federated --corpus study`, 零 LLM):
实测 `avg 0.875`, 逐题 diffs `{}` (2 次独立复跑一致)。

## 7. 已知会看不见什么 (硬规矩 19)

1. 跨路径闸只钉**工厂自管的 6 个键** (`chroma_dir/kb_root/collection_name/embedding_model/
   top_k/structured_lookup_enabled`) 逐键相等 + 键集差恰为 `EVAL_ONLY_LEVERS`。**lever 的
   取值**跨路径不比 —— 生产取 settings、eval 取 args 覆盖是 spec §4.6 保留的差异, 比了就把
   `--hybrid` 之类的覆盖能力钉死了。lever 一致性改由**同路径内** docs ≡ cards 两条镜像断言
   保证 (§3 B3/B4 即打在它们身上)。
2. 生产侧 lifespan 对 `rerank_*` / `query_expansion` 一族**一个字都不传** (cards 引擎同样
   不传 ⇒ 两台一起吃 `RAGEngine` 默认值)。若将来有人只给 cards 补上而不给 docs, 同路径镜像
   断言会红; 但若两台一起补成**同一个错值**, 本 task 的任何断言都看不见 (与 C4 同形)。
3. 全量口径排除了 `scripts/tests/test_federation.py` (并发 agent in-flight), 该文件对本
   task 的改动无覆盖关系, 但"排除"本身意味着这一轮没跑它。
