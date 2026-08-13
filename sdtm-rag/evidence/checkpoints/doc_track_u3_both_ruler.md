# doc 轨 U3 Task 2 — `both` 档确定性尺子 (只量不改)

> 状态: **DONE** · 日期 2026-08-13 · 单元 = doc 轨 U3「判库欠账」Task 2
> 分支 `doc-track-u3` · **零生产代码改动** (`eval/run_eval.py:739` 已支持 `--corpus both`)
> 数据红线: 题集 / 语料 / 逐题题面全在 `data/study/`(gitignored)。**本文件零真名零正文, 只有 id 与数字。**

## 0. 一句话

`both` 档此前**一条尺子都没有**而生产已在跑它; 本轮建成三档确定性尺子(9 次跑批, 三遍全一致):
**doc 侧 1.0000 分毫不动, 代价全部落在卡片侧 —— 0.8750 → 0.8229 (−5.21pt), 归因闭合到 4 题**。
代价来自席位不对称: `both` 把 cards 从 15 席砍到 8 席, 而 doc 的 8 席**不随 k 缩放**,
于是 doc 在 study 半边的占比 35% → 50%。**本单元只量不改。**

补测判库分布(§4)后还知道两件事: `both` 在 cards 侧生产触发 **5/51**(活的, 不是死配置),
但那 4 道脆弱题当前**都没被判到 `both`** ⇒ **这 −5.21pt 现在一分没付**, 属于**悬着的**代价而非正在流血的伤口。

## 1. 三档口径

| 档 | 命令要点 | cdisc 席 | cards 席 | doc 席 |
|---|---|---|---|---|
| **B1** doc 30 题 @ `both` | `--corpus both --study-docs` | 8 | 8 | 8 |
| **B2** cards 51 题 @ `both` | `--corpus both --study-docs` | 8 | 8 | 8 |
| **B3** doc 30 题 @ `study` N=8 | `--corpus study --study-docs --doc-seats 8` | 0 | 15 | 8 |

B3 的作用是**隔离变量**: 它与 B1 的 doc 席位同为 8, 差别只在 cards 是否被减半 + 是否掺 cdisc。
(B1/B2 不传 `--doc-seats`, 走默认值; 实测 `settings.study_docs_seats = 8`, `.env` 无覆盖 ⇒ 三档 doc 席位同为 8。)

## 2. 数字 (检索侧 source recall, 确定性, 零 LLM 判库)

### 2.1 三档均值 —— 逐遍列出

| 档 | r1 | r2 | r3 | 参照 |
|---|---|---|---|---|
| **B1** doc @ `both` | **1.0000** | **1.0000** | **1.0000** | U1 doc-only 上界 100.0% |
| **B2** cards @ `both` | **0.8229** | **0.8229** | **0.8229** | U2 study 档 **0.8750** |
| **B3** doc @ `study` N=8 | **1.0000** | **1.0000** | **1.0000** | U1 k=8 曲线 1.0000 |

⚠ **报数口径**: 上表取产物的 `summary.source_recall_avg`(除以 `n_scored`)。
`compare_runs` 打印的 `avg` 除以 `results` 全行数, cards 题集 51 行里有 **3 行 `out_of_scope`**
(其 `source_recall` 记 1.0), 故它给 B2 打 0.8333 / 给 U2 参照打 0.8824 —— **两者都不是本表的口径**。
账: `0.8229*48 + 3*1.0 = 42.5`, `42.5/51 = 0.8333` ✓。**逐题 diff 与稳定性判定不受此影响**(按 id 比, 与除数无关)。

### 2.2 三遍稳定性 —— **三档全部三遍全一致, 零不稳定题**

```
u3_both_docs       unstable across 3 runs: 0   rc=0
u3_both_cards      unstable across 3 runs: 0   rc=0
u3_study_docs_n8   unstable across 3 runs: 0   rc=0
```
不稳定题 id 清单: **空**。复跑:
```bash
cd sdtm-rag
for b in u3_both_docs u3_both_cards u3_study_docs_n8; do
  ./.venv/bin/python -m eval.compare_runs \
    "data/study/st01/eval/runs/${b}_r1.json" \
    "data/study/st01/eval/runs/${b}_r2.json" \
    "data/study/st01/eval/runs/${b}_r3.json"; done
```
⚠ 「三遍一致」在本仓**不是免费的**: U2 §5-1 实测检索非确定性源在 embedding API。
本轮三档共 **111 个逐题分数**(30 + 51 + 30)三遍零变动 ⇒ 下游拿这三个数做对照时不必再担心噪声。

### 2.3 B2 vs U2 study 档 —— 「cards 15 席 → 8 席」的代价

**0.8750 → 0.8229, Δ = −0.0521 (−5.21pt)**。逐题降级 **4 题**, 其余 44 题 Δ0:

| id | `study` 档 | `both` 档 | 丢分 |
|---|---|---|---|
| st01_v11_q19 | 1.0 | 0.5 | 0.5 |
| st01_v2_q14 | 1.0 | **0.0** | 1.0 |
| st01_v2_q15 | 1.0 | 0.5 | 0.5 |
| st01_v2_q21 | 1.0 | 0.5 | 0.5 |

**归因闭合**: `0.5+1.0+0.5+0.5 = 2.5`, `2.5/48 = 0.0521` = 均值差, **无残差** ⇒
这 4 题是全部代价, 不存在第 5 题在别处偷偷抵消。
`st01_v2_q14` 是唯一**归零**题(1.0 → 0.0), 在 `both` 下 gold 一条都没召回。

该清单在 **r1/r2/r3 三次配对里逐字相同**(不是从 r1 外推):
```bash
for i in 1 2 3; do ./.venv/bin/python -m eval.compare_runs \
  "data/study/st01/eval/runs/u2_cards_docon_N8_r${i}.json" \
  "data/study/st01/eval/runs/u3_both_cards_r${i}.json"; done
```

### 2.4 B1 vs B3 —— doc 侧在 `both` 下**一分不丢**

```
pairwise diff: 0        unstable across 2 runs: 0        两边均 1.0000
```
r2/r3 配对同样 `diff: 0`。
```bash
for i in 1 2 3; do ./.venv/bin/python -m eval.compare_runs \
  "data/study/st01/eval/runs/u3_study_docs_n8_r${i}.json" \
  "data/study/st01/eval/runs/u3_both_docs_r${i}.json"; done
```
⚠ **这个绿灯判别力低**: doc 侧 N=8 已经**满分饱和**, 没有上行空间。
它能证伪「both 伤 doc」(掉分会显示), 但**看不见 doc 占比 35%→50% 带来的任何增益** ——
增益在这个题集上无处显现。别把 `diff: 0` 读成「不对称无害」。

### 2.5 harness 校准 (本轮额外做的, brief 未要求)

B3 与 U1 已落盘的 k=8 曲线点**逐题 diff = 0**, 均值同为 1.0000:
```bash
./.venv/bin/python -m eval.compare_runs \
  data/study/st01/eval/runs/docs_v1_kcurve_k8.json \
  data/study/st01/eval/runs/u3_study_docs_n8_r1.json     # pairwise diff: 0
```
⇒ 本轮用的 harness 与 U1/U2 建曲线时是同一把尺, B1 的 1.0000 因此可与历史数字并排读。

## 3. 席位不对称的记录 (**本单元不改**)

### 3.1 事实

- `server/federation.py:129-131`
  ```python
  k_each = math.ceil(k / 2)                            # k=15 -> 8
  cd = self.cdisc.retrieve(..., top_k=k_each)          # cdisc 8
  st = self.study.retrieve(question, top_k=k_each)     # cards 8; doc_seats 没传
  ```
- `server/study_corpus.py:46-47`
  ```python
  def retrieve(self, question, *, top_k=None, doc_seats=None):
      seats = self.doc_seats if doc_seats is None else doc_seats   # 8, 不随 top_k 缩放
  ```

`k_each` 只缩放**卡片席**; `doc_seats` 是 `StudyCorpusEngine` 的**实例属性**(`__init__` 就固定),
`federation.py` 既没传也无从按比例缩它。结果:

| 档 | cdisc | cards | docs | doc 占 study 半边 |
|---|---|---|---|---|
| `study` | 0 | 15 | 8 | 8/23 = **34.8%** |
| `both` | 8 | 8 | 8 | 8/16 = **50.0%** |

**这个抬升不是任何人的裁定**, 是「`doc_seats` 写成引擎属性而非 k 的比例」掉出来的副产物。

### 3.2 为什么本单元不改

1. **本 task 的合同是建尺子, 不是调参**。`both` 此前零尺子, 现在才第一次有基线;
   在基线落盘的同一轮里改被测对象, 等于把「改动的效果」和「基线本身」搅在一起, 之后谁也说不清。
2. **改了往哪个方向也还没有依据**: 2.4 已说明本题集**看不见** doc 加权的增益,
   只看得见 cards 的 −5.21pt。只拿得到代价、拿不到收益时改配比, 是在没有目标函数的情况下调参。
3. **代价当前不落在生产路径上**(见 §4 触发率), 不构成必须立刻动的理由。

⇒ 交给下游单元决策。本文件提供的是决策所需的数字, 不是决策。

## 4. `both` 在生产里到底被触发多少 (brief 记为「未测」, 本轮补测为**实测**)

不测这一条, §2 的三个数就只是"某个从未发生的配置下的数"。故补跑 `--corpus auto`
(生产路径, 不强制档) 各 3 遍, 产物 `u3aux_auto_{docs,cards}_{1,2,3}.json`(同样 gitignored)。

### 4.1 判库分布 (三遍完全一致)

| 题集 | `study` | `both` | `cdisc` | 均值 |
|---|---|---|---|---|
| doc 30 题 | 27 | **0** | 3 | 0.9000 |
| cards 51 题 | 45 | **5** | 1 | 0.8542 |

- **doc 侧: `both` 触发 0 次** ⇒ brief 那句「doc 30 题在 auto 下从不触发 `both`」**已由实测确认**
  (三遍均 0/30)。§2 的 B1 因此是**当前生产路径上不会发生**的配置。
- **cards 侧: `both` 触发 5/51** ⇒ **`both` 在生产里是活的**, 不是死配置。B2 量的是真实路径。
- doc 侧 `0.9000` 与 cdisc 3 题 **逐位复现 U2 的「判库损耗 10.00pt / 归因到 3 题」**
  (miss 的 3 题 id 与 U2 记录的 `q15`/`q17`/`q53` 一致)。

### 4.2 那 4 道降级题, 生产里被判到 `both` 了吗? —— **没有**

`auto` 与强制 `study` 的逐题 diff **只有 1 题**:
```bash
./.venv/bin/python -m eval.compare_runs \
  data/study/st01/eval/runs/u2_cards_docon_N8_r1.json \
  data/study/st01/eval/runs/u3aux_auto_cards_1.json
#   st01_v2_q07: 1.0 -> 0.0        (pairwise diff: 1)
```
`0.8750 − 1.0/48 = 0.8542` ✓ 账闭合。

由此可**推出**(产物不记逐题 routed 档, 以下是演绎, 不是直接观测):

1. §2.3 那 4 题(q19/q14/q15/q21)在 `auto` 下**都没被判到 `both`** ——
   若判到了, 它们的 auto 分就会等于 both 分(与 study 分不同), 必然出现在上面的 diff 里; 而它们没出现。
2. `st01_v2_q07` 在强制 `both` 下是满分(不在 4 题名单里), 却在 auto 下归零
   ⇒ 它就是那 **1 道被判到 `cdisc`** 的题(压根没进 study 引擎)。
3. 那 5 道被判到 `both` 的题, **其分数在 `both` 与 `study` 下相同**(否则会进 diff)。

**⇒ `both` 的 −5.21pt 代价, 在这个题集上当前生产一分没付**: 判库恰好把 4 道脆弱题都送去了 `study`。
⚠ 这是**当前 router 的巧合, 不是保证**。router 一变、题面一换, 这 4 题随时可能落进 `both`。
这正是「本单元只量不改、把数字留给下游决策」的理由 —— 代价是真的, 只是暂时没落在生产上。

## 5. 它看不见什么 (硬规矩 19)

本文件所有绿灯都只覆盖**检索侧 source recall**, 边界如下:

1. **答题侧完全未测**。三档没跑一次 LLM 答题, `fact=n/a`。cards 的 −5.21pt 会不会真的让答案变错、
   doc 占比升到 50% 会不会让答案变好 —— **本文件一个字都没说**。
2. **doc 侧 1.0000 是饱和值**(§2.4)。`diff: 0` 只证伪了「both 伤 doc」, 不构成「不对称无害」的证据;
   增益方向在这个题集上不可观测。
3. **强制档不经 LLM 判库**。三档的 `summary.routing` 记的是**被强制的档**(`federation.py:114-116`:
   `routed = corpus` 直接赋值, 仅当 `corpus == "auto"` 才调 `route_corpus`) ⇒
   这三个数是**判库正确时的上界**, 不含任何判库错误的代价。
4. **只测了 k=15 这一个工作点**。`k_each = ceil(k/2)` 与 `doc_seats=8` 的相对关系随 k 变化,
   换 `--top-k` 则本文全部数字失效。
5. **`compare_runs` 的 avg 不是本文口径**(§2.1)。引用本文数字时若改用 comparator 的均值,
   cards 档会系统性偏高约 1pt。
6. **只有 st01 一个研究**。`both` 的席位不对称对其他研究的影响未测。
7. **B2 的 4 题降级只做到「哪 4 题、丢多少」**, 没做到「为什么是这 4 题」——
   未核实它们的 gold 原本排在 cards 第 9-15 位(即恰好被砍掉的那 7 席)。归因闭合是**算术闭合**
   (丢分加总 = 均值差), **不是机制闭合**。
8. **§4.2 的三条结论是演绎, 不是观测**。`run_eval` 产物**不记逐题 routed 档**(`results` 的键里
   没有 routing/corpus 字段, 只有 `summary` 的聚合计数器), 所以「哪 5 题被判到 `both`」**我说不出**。
   §4.2 只能从"逐题 diff 里没出现"反推"没被判到 `both`" —— 逻辑成立, 但比直接观测弱一档。
   要坐实, 需要给产物加逐题 routed 字段(本单元不改代码, 未做)。
9. **判库分布只在这两个题集上量过**。5/51 是 cards 题集的触发率, **不是线上真实流量的触发率** ——
   真实用户问题的分布与题集分布不同, 本文件对线上触发率**一无所知**。
10. **`both` 的收益侧完全没量**。`both` 存在的理由是跨库问题(既要 CDISC 标准又要本研究做法),
    而这两个题集**都是单库题**。本文件只量到 `both` 的代价, 没量到它本该带来的好处 ——
    拿本文件去论证"`both` 不值得"是**误用**。

## 6. 产物与复跑

9 个跑批产物在 `data/study/st01/eval/runs/u3_{both_docs,both_cards,study_docs_n8}_r{1,2,3}.json`
(**gitignored**, 带题面全文, 不进 git)。全部复跑:

```bash
cd sdtm-rag
for i in 1 2 3; do
  ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
    --retrieval-only --hybrid --study-lookup --federated --corpus both --study-docs \
    --output "data/study/st01/eval/runs/u3_both_docs_r${i}.json"
  ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
    --retrieval-only --hybrid --study-lookup --federated --corpus both --study-docs \
    --output "data/study/st01/eval/runs/u3_both_cards_r${i}.json"
  ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
    --retrieval-only --hybrid --study-lookup --federated --corpus study --study-docs \
    --doc-seats 8 --output "data/study/st01/eval/runs/u3_study_docs_n8_r${i}.json"
done
```
§4 判库分布的 6 个产物 `u3aux_auto_{docs,cards}_{1,2,3}.json`(gitignored), 复跑 = 上面同样的命令
**去掉 `--corpus ...` 与 `--doc-seats`**(走默认 auto + `settings.study_docs_seats=8`):
```bash
for i in 1 2 3; do
  ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
    --retrieval-only --hybrid --study-lookup --federated --study-docs \
    --output "data/study/st01/eval/runs/u3aux_auto_docs_${i}.json"
  ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
    --retrieval-only --hybrid --study-lookup --federated --study-docs \
    --output "data/study/st01/eval/runs/u3aux_auto_cards_${i}.json"
done
```
⚠ B2 的 `rc=1` 是 `run_eval` 分数低于 85% 阈值的返回值, **不是跑批失败** —— 看产物, 不看 rc。

**本 task 零生产代码改动**: 全量测试 `./.venv/bin/python -m pytest` → **1203 passed** (34.29s), 与 U3 Task 1 后的基线一致。
