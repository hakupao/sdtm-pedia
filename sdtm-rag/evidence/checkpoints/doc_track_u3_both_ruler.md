# doc 轨 U3 Task 2 — `both` 档确定性尺子 (只量不改)

> 状态: **DONE** · 日期 2026-08-13 · 单元 = doc 轨 U3「判库欠账」Task 2
> 分支 `doc-track-u3` · **零生产代码改动** (`eval/run_eval.py:739` 已支持 `--corpus both`)
> 数据红线: 题集 / 语料 / 逐题题面全在 `data/study/`(gitignored)。**本文件零真名零正文, 只有 id 与数字。**

## 0. 一句话

`both` 档此前**一条尺子都没有**而生产已在跑它; 本轮建成三档确定性尺子(9 次跑批, 三遍全一致):
**doc 侧 1.0000 分毫不动, 代价全部落在卡片侧 —— 0.8750 → 0.8229 (−5.21pt), 归因闭合到 4 题**。
⚠ 「doc 侧不动」的证据强度**低于**卡片侧那个数: 它是**结构恒等**(两档 doc 检索入参恒同),
不是测出来的稳健性 —— 详见 §2.4, 别拿它当「席位不对称无害」的证据。
代价来自席位不对称: `both` 把 cards 从 15 席砍到 8 席, 而 doc 的 8 席**不随 k 缩放**,
于是 doc 在 study 半边的占比 35% → 50%。**本单元只量不改。**

补测判库分布(§4)后还知道两件事: `both` 在 cards 侧生产触发 **5/51**(活的, 不是死配置),
但那 4 道脆弱题当前**都没被判到 `both`** ⇒ **这 −5.21pt 现在一分没付**, 属于**悬着的**代价而非正在流血的伤口。

## 1. 三档口径

| 档 | 命令要点 | cdisc 席 | cards 席 | doc 席 |
|---|---|---|---|---|
| **B1** doc 30 题 @ `both` | `--corpus both --study-docs` | 8 | 8 | 8 |
| **B2** cards **51 行 / 48 计分** @ `both` | `--corpus both --study-docs` | 8 | 8 | 8 |
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

⚠ **报数口径**: 上表取产物的 `summary.source_recall_avg` —— 它除以 `n_scored`(**48**), 不是
`results` 的行数(**51**)。cards 题集 51 行里有 **3 行 `out_of_scope`**, 其 `source_recall` 恒记 1.0。

**⏱ 关于 `compare_runs` 打印的 `avg`(已过期, 保留作历史记录)**: 在本文件 commit 时刻
(`761c6ef`)的 comparator 除以全 51 行, 会给 B2 打 **0.8333** / 给 U2 参照打 **0.8824**,
与本表口径不同(账: `0.8229*48 + 3*1.0 = 42.5`, `42.5/51 = 0.8333` ✓)。
**该口径漂移已由 `92d8ca8` 修复** —— 现 CLI 直接照抄产物自称的 `summary.source_recall_avg`,
且 `n=` 已改名 `rows=`。今天照 §2.2 复跑会看到 `rows=51 avg=0.8229`, **与本表一致**。
(此段是给"拿着旧文档、旧 checkout 的读者"用的; 该 finding 正是由本 task 的实战使用暴露并回流修掉的。)

**逐题 diff 与稳定性判定在两个版本下都不受影响**(按 id 比, 与除数无关)。

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

### 2.3 B2 vs U2 study 档 —— 「cards 15 席 → 8 席」的代价 (除数 = **48 计分题**, 非 51 行)

**0.8750 → 0.8229, Δ = −0.0521 (−5.21pt)**。逐题降级 **4 题**, 其余 44 计分题 Δ0:

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
⚠⚠ **这个 `diff: 0` 不是「测出来的稳健性」, 是结构恒等 —— 该比对根本不是可失败的检验。**

原因**不是**「doc 侧满分饱和、没有上行空间」(本文件初版这么写, **是错的**, 见下方反证):

- `federation.py:124`(`study` 档)与 `:131`(`both` 档)**都不传 `doc_seats`**
- ⇒ `study_corpus.py:47` 两档同取 `self.doc_seats` = **8**
- ⇒ `study_corpus.py:54` `self.docs.retrieve(question, top_k=seats)` **两档入参逐字相同**
- 唯一可能造成差异的是去重集 `seen`(由 cards 结果构成), 但 cards 与 doc 的 chunk id
  **命名空间不相交** —— 实测 `study_st01` 959 个 id ∩ `study_st01_docs` 114 个 id = **0**:
  ```bash
  ./.venv/bin/python -c "
  import chromadb; cl=chromadb.PersistentClient(path='data/chroma')
  a=set(cl.get_collection('study_st01').get(include=[])['ids'])
  b=set(cl.get_collection('study_st01_docs').get(include=[])['ids'])
  print(len(a), len(b), len(a&b))"      # 959 114 0
  ```
  ⇒ `seen` **不可能**丢掉任何 doc chunk。

**⇒ 对 doc-gold 的 source_recall, B1 与 B3 恒等, 与分数高低无关。**

**反证实验**(U3 审查方设计并首跑, 我复跑确认): 把 doc 席位压到 3, doc 侧掉到 **0.8667**,
30 题里 **6 题不满分** —— **明确脱离饱和, 有充分上/下行空间** —— 恒等性依然成立:
```bash
for c in both study; do
  ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
    --retrieval-only --hybrid --study-lookup --federated --corpus $c --study-docs \
    --doc-seats 3 --output "data/study/st01/eval/runs/rev_t2_${c}_docs_n3.json"; done
./.venv/bin/python -m eval.compare_runs \
  data/study/st01/eval/runs/rev_t2_study_docs_n3.json \
  data/study/st01/eval/runs/rev_t2_both_docs_n3.json
# run 1: rows=30 avg=0.8667 / run 2: rows=30 avg=0.8667
# unstable across 2 runs: 0        pairwise diff: 0
# 逐题 source_recall 与 source_hits 全等: True   (6/30 < 1.0)
```

**⇒ 给下游的行动项(重要)**: **不要**为了"让增益显形"去换更难的工作点或更难的题集 ——
U1 `doc_track_u1_question_set.md:239` 备着一个 k=5 = 88.33% 的诊断工作点, 照那条路走
**保证仍是 `diff: 0`**, 白烧一轮跑批与评审; 更糟的是拿到第二个 `diff: 0` 后极易被误读成
「反复验证了不对称无害」—— 那正是本节警告不要下的结论。
**doc 加权的增益只能在答题侧, 或在对「位置 / 库间竞争」敏感的指标上测**, 在本指标上永远测不到。

📌 **席位事实(别把占比读反)**: doc 的**绝对席位两档均为 8, 一个字没变**; 变的只是 study
半边的分母(23 → 16)。§3 那句「**在 study 半边**占比 35% → 50%」的限定词是必须的 ——
若按**整个 context** 算, 方向反而是**略降**: `study` 档 8/(15+8) = 34.8%,
`both` 档 8/(8+8+8) = **33.3%**, 因为 `both` 是在原有基础上**追加** 8 个 cdisc 席
(总块数 23 → 24), **不是**把席位重新分配。

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
2. **改了往哪个方向也还没有依据**: §2.4 已说明本指标**在结构上不可能**显现 doc 加权的增益
   (换题集换工作点都不行), 只看得见 cards 的 −5.21pt。只拿得到代价、拿不到收益时改配比,
   是在没有目标函数的情况下调参。**要先有一把能看见收益的尺子**(答题侧, 或对位置/竞争敏感的指标)。
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
  ⚠ **这条结论依赖一个前提: 这 5 次是 LLM 判定的 `both`, 不是异常兜底的 `both`。**
  `route_corpus` 在**任何异常**下都返回 `("both", True)`(`federation.py:71` docstring / `:89-90`),
  而 `run_eval.py:562` 只 `self.routed.append(routed)`、`:978` 只 `Counter(retriever.routed)`
  —— **`fallback` 标志被丢弃**, 计数器把两条路径合并。若不写这个前提, `{'both': 5}` 同样可以
  读成"router 崩了 5 次", 那 B2 量的就是**降级路径**, 该修的也变成 router 稳定性。
  **本轮实测该前提成立**: 6 次 auto 跑批共 243 次判库(81 题 × 3 遍)全部 `fallback=False`,
  `route_corpus_fallback_both` 零命中:
  ```bash
  grep -c "route_corpus_fallback_both" <auto 跑批日志>          # 0
  grep -o "fallback=[A-Za-z]*" <auto 跑批日志> | sort | uniq -c  # 243 fallback=False
  ```
  ⚠ **该证据不可从落盘产物重建** —— 产物不记 `fallback`, 上述 grep 跑的是本轮 auto 批次的
  **stdout 日志(含题面全文, 按红线未落盘、未进 git)**。下游要复核, 需按 §6 重跑 auto 批次
  并对**自己那一份**日志跑同样两条 grep。(见 §5 第 11 条)
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
2. **B1 vs B3 对 doc-gold source_recall 是结构恒等, 不是可失败的检验**(§2.4)。
   两档的 doc 检索是同一次调用同一参数(`doc_seats` 恒 8), 且 cards/doc 的 id 命名空间不相交
   ⇒ 该比对**不可能**产生非零结果, **换题集、换工作点都不行**(已用 doc 席位 = 3、
   doc 侧 0.8667/6 题不满分的反证实验证实)。它既不能证明「both 不伤 doc」是测出来的,
   也永远看不见 doc 加权的增益。**别把 `diff: 0` 读成「不对称无害」。**
3. **强制档不经 LLM 判库**。三档的 `summary.routing` 记的是**被强制的档**(`federation.py:114-116`:
   `routed = corpus` 直接赋值, 仅当 `corpus == "auto"` 才调 `route_corpus`) ⇒
   这三个数是**判库被固定时**的数, 不含任何判库错误的代价 —— 但**不等于「判库正确时」的数**:
   §4.1 实测 `auto` 把 cards 45/51、docs 27/30 判去 `study`, 把全部题强制成 `both`
   恰恰不是正确判库会做的事(B1 更是 §4.1 所说"生产路径上不会发生"的配置)。
4. **只测了 k=15 这一个工作点**。`k_each = ceil(k/2)` 与 `doc_seats=8` 的相对关系随 k 变化,
   换 `--top-k` 则本文全部数字失效。
5. ~~**`compare_runs` 的 avg 不是本文口径**~~ —— **该边界已于 `92d8ca8` 消失**(§2.1)。
   在 `761c6ef` 时刻它成立(comparator 除以 51 行, cards 档系统性偏高约 1pt);
   现 CLI 已改读产物自称的 `summary.source_recall_avg`, 与本文口径一致。
   **保留此条仅作历史记录** —— 若你手上的 checkout 早于 `92d8ca8`, 这条仍然适用。
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
11. **routing 计数器不分「LLM 判的 `both`」与「异常兜底的 `both`」**(§4.1)。
    `route_corpus` 任何异常都返回 `("both", True)`, 而产物**只存 `routed`、不存 `fallback`**
    ⇒ 单看产物无法区分这两者。本轮已用跑批日志核到 243 次判库全 `fallback=False`,
    但**那份日志按红线未落盘**, 下游只能重跑后自行核。
    ⚠ 长期风险: 日后 router 换模型若开始偶发异常, 同一个计数器仍打 `both: N`,
    「触发率上升」会被读成"跨库问题变多了", 真相却是 router 在崩。
12. **`both` 是「追加」不是「重分配」**(§2.4 席位事实)。总块数 23 → 24, doc 绝对席位恒为 8;
    doc 占**整个 context** 的比例实际 34.8% → **33.3%**(略降)。只有「**study 半边**」这个
    分母下才是 35% → 50%。引用占比时**必须带限定词**, 否则方向会被读反。

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
