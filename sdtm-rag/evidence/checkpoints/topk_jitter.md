# top-k 抖动量化 (Task 3B)

> 日期: 2026-08-07 · 探针 `eval/jitter_probe.py`
> 数据: **`topk_jitter_multiprocess.json`(20 进程 × 140 题, 定论主依据)** · `topk_jitter_perturbation.json`(向量扰动, 佐证)
> · `topk_jitter.json` + `topk_jitter_sample1.json`(第一版的单进程采样, 保留作反面教材)
> 起因: Task 1 评审同 query 同参数连跑两次, top-15 **第 9 位起成分变化**; 控制器随后用 chunk_id 跑 5 次却全稳定 → 当时判"抖动偶发"。
> 层① 的 `max_cluster` / `dup_seats` / "28.6%" 全部出自**单次** top-15, 在量化清楚之前不许当稳定事实引用。
>
> **结论经过一次推翻**: 单进程采样判 `false` → 跨进程取样判 **`true`**。评审的观察是对的, 我第一版的探针有结构性盲区。§0 记录了全过程。

## 结论

**`JITTER_AFFECTS_STATS = true`**

> ⚠️ **本结论是修正后的第二版**。第一版判 `false`, 依据是"528 次采样里成分零变化"。
> 那个依据**出自一个有结构性盲区的探针**: 所有循环都在同一个进程里, 而抖动主因是**跨进程**的。
> 依据作废 —— 见 §0.1。测量本身没错, 但它测的不是我以为的那个东西。

top-15 的**成分确实会变**, 三个独立测量一致:

| 测量 | top-15 成分变过 | 三个汇总统计变过 | `max_cluster` 变过 |
|---|---|---|---|
| **20 个独立进程 × 140 题** (生产口径, §0.2b) | **5/140** (q31,q38,q47,q120,q133) | **1/140** (q47) | **0/140** |
| 同上但 query 向量逐位固定 (只含 HNSW 抖动) | 3/140 (q38,q117,q120) | 1/140 (q117) | 0/140 |
| 8400 次实测幅度的向量扰动 (进程内, §0.3) | 5/140 (q31,q38,q39,q46,q47) | 1/140 (q47) | 0/140 |

**成分变 ⇒ 按 brief 判定表第 3 行, `JITTER_AFFECTS_STATS = true`**: Task 4 必须多次取样、报告每题稳定性,
**且取样必须跨独立进程** —— 进程内取样对单一状态有 ~95% 的强偏向, 会系统性低估状态分布 (§0.1)。

但这个 true **不是一句"全都不可信"**, 分寸要带上:

- **`max_cluster` 在全部三个测量里一次没变** (0/140 × 3) → 凡是基于 `max_cluster` 阈值的聚合数字
  (如"28.6% 的题被同质簇挤占") **不受影响, 不需要重算**。
  **这不是巧合, 且是有条件的 —— 机制与失效条件见 §5.6, 引用该豁免时必须一起带上。**
- **`dup_seats` / `distinct_sections` 会变的是 q47 与 q117 两题** (并集)。q47 在生产口径下
  **接近四六开** (`(2,2,13)` 12/20 进程 vs `(2,1,14)` 8/20) —— 不是罕见抖动, **它的逐题值不能当事实**。
- 其余 138 题的席位账在所有测量里都不动: 会换的席位**几乎总是同一批逐字节重复的 chunk 互换** (§4),
  而按 section 名计席位的统计不看"是哪个域"。

**排位则一律不可复现**, 这点两版结论一致, 且理由是结构性的 (§4): 挤占席位的 chunk 正文逐字节相同,
先后由 ingest 分批噪声决定。

本结论只对**当前切割线 (`top_k=15` + `hybrid_pool=30`)** 成立。改 k、改池深、改融合权重或重灌索引, 都要重测。

---

## 0. 第一版判 false 是怎么错的 (方法论, 比结论本身更该被记住)

### 0.1 错在哪 —— 探针**在同一个进程里**循环, 而抖动的主因是**跨进程**的

先排除一个被怀疑过的解释: **探针确实每次都重新 embed**。直接在 `RAGEngine` 类上打点计数:

```
_embed_query 调用次数: 12   (12 次循环, 每次 retrieve 只 embed 一次 => 期望 12)  ✓
不同向量指纹数:       2     46de3891 x9, 049e9dff x3     <- 少数派 25%, 抽到了
top-15: 成分种类=1 顺序种类=1 sometimes=0                  <- 12 次仍全同
```

**少数派向量抽到了, 成分还是没变。** 所以"没重新 embed"不是原因, "12 次都没抽到少数派"也不是。

真正的原因: **`retrieve` 的不确定性主要来自检索侧, 而它在一个进程内是确定的。**
固定一份**逐位相同**的 query 向量 (落盘复用)、且 BM25 索引顺序指纹在所有进程里都相同,
8 个独立进程跑纯 dense top-31:

```
vec=46de3891 top31fp=937fe3f9 | 末6: TA,TU,VS,SR,TE,TV     x7
vec=46de3891 top31fp=b408d7d5 | 末6: TA,TU,VS,DS,RP,TR     x1   <- 同一份向量, 换了人
```

Chroma 走 **HNSW 近似**最近邻; 在一批**向量完全相同**的重复 chunk (§4) 之间, 它返回谁不由 sim 决定。

**进程内不是"量不到", 而是"严重偏向"** (这条第一版写错过, 见 §0.1c)。单进程连跑 60 次
(每次新建 `RAGEngine` + 现场 embed) 实测:

```
向量指纹分布 : {'46de3891': 40, '049e9dff': 17, '3f46ee9b': 3}
top15 指纹分布: {'d09cfd9e': 57, 'e2f3f77d': 3}     <- 进程内出现 2 种状态, 不是 1 种
top15 状态切换在第 9,10,44,45,54,55 次; 向量切换十几次  <- 两者不同步
```

多数派 **57/60 ≈ 95%**。偏向这么强, 一个 12 次的 block 约有 `0.95^12 ≈ 54%` 概率全同 ——
第一版的 block 多数报"零变化"**由此即可解释, 不需要"进程内锁死"这种更强的假设**。

**同题同样 20 次检索, 只差在不在同一个进程里**:

| 口径 | 成分种类 | 顺序种类 | `sometimes` |
|---|---|---|---|
| 旧 (单进程内循环 20 次, 每次新建引擎 + 重新 embed) | **1** | 1 | **0** |
| 新 (20 个独立进程, 各自 embed) | **4** | 4 | **4** |

```
14/20 进程: ch04,SV,TS,ML,DA,PR,CO,CV,TE,BS,NV,PC,UR,DD,TU
 4/20 进程: ch04,SV,TS,ML,DA,PR,CO,CV,BS,NV,PC,UR,DD,TU,OE     <- 评审 run1 (逐位相同)
 1/20 进程: ch04,SV,TS,ML,DA,PR,CO,CV,BS,NV,PC,TR,UR,DD,TU
 1/20 进程: ch04,SV,TS,ML,DA,PR,CO,CV,BS,NV,PC,RP,UR,DD,TU
```

**这 4 种里没有评审 run2** (run2 第 9 位 TE **且**第 13 位 TR, 上面没有一种同时含二者) ——
第一版报告说"run1/run2 都在这 4 种里", **那句是错的**。

但 run2 并非没复现: 在 §0.2b 的 **fixed_vector 批次**里, 有 **1/20** 个进程给出了与 run2
**逐位相同**的成分 (`evidence/checkpoints/topk_jitter_multiprocess.json` →
`questions.q38.fixed_vector.distinct_compositions`)。而那一批的 20 个进程里又没有 live 批次
见到的某个状态。**即: 不同批次见到的状态集合不同, 稀有态在 1/20 量级。**

⇒ **`n_procs=20` 是"检出不稳定"的下限, 不足以"刻画分布尾部"。** q47 那种接近四六开的分布
20 次够用; 1/20 那种稀有态显然不够。

**`sometimes == 0` 是取样严重偏向造成的, 作废。**

### 0.1c 两条被证伪的表述 (第一版写错, 此处存档)

| 第一版写的 | 实测证伪 | 订正 |
|---|---|---|
| "进程内循环 N 次**只等于 1 个样本**" | 单进程 60 次里 top-15 出现 **2 种**状态 (57 : 3); 且状态切换与向量切换**不同步** | 进程内**严重偏向单一状态** (~95%), 会大幅低估状态分布 —— 不是量不到 |
| "评审 run1 与 run2 都在这 4 种里" | 那 4 种没有一种同时含 TE 与 TR | run1 命中其中一种; **run2 是另一种状态**, 在 fixed_vector 批次里 1/20 复现 |

两条都曾以**机制断言**的形式写进源码 docstring / JSON `_meta` / 给 Task 4 的硬要求, 已全部改准。
**给 Task 4 的操作要求不变 (仍必须跨进程), 变的是理由的准确度。**

### 0.1b embedding 侧的"抽签"也成立, 但不是主因

评审量到的每次调用独立抽签、分布偏斜 (少数派 ~3/18) 与我的观测一致 (少数派 3/12、15/60)。
它**确实**是一个抖动源 (§3 的向量差 max\|Δ\|~1e-4 / L2~9e-4), 但单靠它翻不动 q38 的 top-15 ——
上面那次 12 连跑抽到 3 次少数派、成分照旧。两个源的分离量化见 §0.3 的两行结果。

~~原第一版把主因归给"embedding 一个时间窗锁定一个向量"~~ —— **该模型错了**, 已按上述替换。

### 0.2 两条独立的真实反例

**(a) 评审的两次** (约 03:0x, 生产口径 hybrid + S1, q38, top_k=15):

```
run1: ch04, SV, TS, ML, DA, PR, CO, CV, BS, NV, PC, UR, DD, TU, OE
run2: ch04, SV, TS, ML, DA, PR, CO, CV, TE, BS, NV, PC, TR, UR, DD
差集: run1 独有 {TU, OE}; run2 独有 {TE, TR}
```

run2 = run1 在第 9 位插入 `TE`、第 13 位插入 `TR`, 把尾部的 `TU`/`OE` 挤出 15 名的切割线。
**这是换人, 不是换位。**

**(b) 我自己的两次**, 相隔约 10 分钟, 同一进程外同一代码同一索引 (`_engine("hybrid", 15)` + `retrieve(top_k=15)`):

```
14:2x: ch04, SV, TS, ML, DA, PR, CO, CV, BS, NV, PC, UR, DD, TU, OE   ← 与评审 run1 逐位相同
14:3x: ch04, SV, TS, ML, DA, PR, CO, CV, TE, BS, NV, PC, UR, DD, TU   ← TE 进, OE 出
```

**第一版的 528 次全部落在 14:2x 那个状态里。** 索引未动过 (`data/chroma/*/data_level0.bin` 停在 8 月 4 日),
代码未动过 —— 排除了"重灌索引"和"配置差异"这两个替代解释。

### 0.2b 定论measurement: 20 个独立进程 × 140 题

这是**判定所依据的主测量**, 产物 `evidence/checkpoints/topk_jitter_multiprocess.json`。
两种模式分离两个抖动源:

```bash
# 每个进程: 建 hybrid 引擎, 对全 140 题跑生产检索, 存 top-15 与 section 计数
# 模式 A 固定向量 (一次性 embed 全部 140 题后落盘复用) => 只含检索侧 HNSW 抖动
# 模式 B 各进程现场 embed                              => 生产口径, 两源叠加
for i in $(seq 1 20); do .venv/bin/python <worker> $i & done; wait
```

| | 模式 A 固定向量 (只含 HNSW) | 模式 B 现场 embed (生产口径) |
|---|---|---|
| top-15 **成分**变过 | **3/140** (q38, q117, q120) | **5/140** (q31, q38, q47, q120, q133) |
| **section 多重集**变过 | 2/140 | 4/140 |
| **三个汇总统计**变过 | **1/140** (q117) | **1/140** (q47) |
| **`max_cluster`** 变过 | **0/140** | **0/140** |

q47 在生产口径下相当不稳: `(max_cluster,dup_seats,distinct_sections)` 为 `(2,2,13)` 占 12/20 进程、
`(2,1,14)` 占 8/20 —— **接近四六开, 不是罕见抖动**。q117 在模式 A 下 1/20 翻。

**只有 `max_cluster` 扛住了全部测量** (两个模式各 2800 次检索, 加 §0.3 的 8400 次扰动, 全 0/140)。

### 0.3 控制变量: 不再采样等它发生

这一节量的是**另一个源**: embedding 侧的向量抖动 (与 §0.1 的进程维度正交)。
与其等 API 抽到不同向量, 不如**把扰动当自变量**:
取一个真实 query 向量, 施加实测幅度 (L2 = 8.756e-04) 的扰动, 直接喂进 `retrieve()`
(`retrieve` 每次调用只 embed 一次, 故替换 `_embed_query` 即可完全控制唯一的抖动源; BM25 侧对同一
query 文本本就确定)。

```bash
.venv/bin/python - <<'PY'
import json, time
from collections import Counter
import yaml
from eval.jitter_probe import _engine, perturbed_vectors, retrieve_under_perturbation

N, L2, SEED = 60, 8.756e-04, 20260807   # L2 = 实测真实抖动幅度 (7.98e-04 ~ 2.16e-03)
with open("eval/test_set_v3.yml", encoding="utf-8") as f:
    qs = yaml.safe_load(f)
rag = _engine("hybrid", 15)
churn, sec_churn = [], []
for i, q in enumerate(qs, 1):
    v0 = rag._embed_query(q["question"])
    runs = retrieve_under_perturbation(
        rag, q["question"], perturbed_vectors(v0, L2, N, SEED), top_k=15)
    sets = {frozenset(c.chunk_id for c in r) for r in runs}
    multisets = Counter(tuple(sorted(Counter(c.section for c in r).items())) for r in runs)
    if len(sets) > 1: churn.append(q["id"])
    if len(multisets) > 1: sec_churn.append(q["id"])
print("top-15 成分变过:", len(churn), churn)
print("section 多重集变过:", len(sec_churn), sec_churn)
PY
```
```
top-15 成分变过:    5 ['q31', 'q38', 'q39', 'q46', 'q47']
section 多重集变过: 3 ['q31', 'q46', 'q47']
```

完整产物 (含每题各多重集及其出现次数): `evidence/checkpoints/topk_jitter_perturbation.json`
(140 题 × 60 次 = 8400 次生产检索, 用时 131.5 秒, **零 API 调用**)。

按统计量分层 (从该 JSON 读出):

```
max_cluster         0/140  []
dup_seats           1/140  ['q47']
distinct_sections   1/140  ['q47']

q47 明细: max_cluster=2 dup_seats=1 distinct_sections=14  —— 46/60 次
          max_cluster=2 dup_seats=2 distinct_sections=13  —— 14/60 次
q31/q46: 多重集变了, 但三个汇总统计不变 (换的是两个各占 1 席的 section, 席位账不动)
```

⚠️ **随机方向不是真实抖动的分布**: 沿两个真实 API 向量之差的方向放大到 5 倍 (L2=4.4e-03) 都翻不动 top-15,
而同样长度的**随机**方向约 10% 会翻。所以这里的频率是**敏感度上界**, 回答"这个统计量在这个幅度下稳不稳",
**不回答"每次调用有多大概率翻"**。真实的每次调用频率由 §0.2b 的跨进程测量给出
(生产口径 20 个进程里, q47 的统计取值是 12 : 8)。

**复跑说明 (别把它当成对不上)**: 扰动方向由 `seed` 定死可复现, 但**基准向量 `v0` 是当场调 API 取的**,
而 API 返回的是一小组离散向量之一 (§0.1) —— 所以逐题结果**条件于你那次拿到哪个基准向量**。
实测: 两次完整的 140 题扫描结果**完全一致** (都是 成分 5 / 多重集 3 / 汇总统计 1, 题号也相同);
但一次只挑 7 题的复核里 `q46` 没抖 —— **q46 处在边界上**, 换个基准向量就不翻了。
稳的是结论的三层分布 (`max_cluster` 0、汇总统计 1 题、成分 5 题), 边界题的名单可能小幅出入。

### 0.4 该记住的教训

**凡"跑 N 次都一样"的稳定性结论, 先证明这 N 次是 N 个独立样本 —— 而且要先问清"独立"是相对哪个维度。**

我第一版栽在这里两次:
1. 先怀疑是 embedding 没重新调 → **打点计数排除了** (12/12 次都调了, 还抽到了少数派向量)。
2. 真正的盲区在**进程**这一维: 探针把 N 次循环全放在一个进程里, 而 `retrieve` 的主要不确定性
   (Chroma HNSW 在重复 chunk 之间选谁) **进程内是确定的**。于是 N 次循环共享同一个"抽签结果",
   44 个 block 齐刷刷报"零变化"。

**教训的可操作形式**: 写稳定性探针时, 先列出所有可能影响结果的层 (进程 / 引擎实例 / 网络调用 /
随机种子 / 索引状态), 再逐层问"我的 N 次循环有没有真的让这一层变化"。**没变的那层, 就是你的盲区。**
最省事的验证: 拿一个**已知会变**的现象 (这里是评审的两次 run) 去打探针 —— 探针复现不出来, 就是探针有问题。

---

## 1. 复现命令

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag

# ① 定论所依据的控制变量扫描 (全 140 题 x 60 次扰动, 131 秒, 零 API 调用) —— 见 §0.3 的完整脚本
#    产物 evidence/checkpoints/topk_jitter_perturbation.json

# ② 采样口径探针 (第一版依据; 仍是量化抖动源与间隔的工具, 但**不足以判成分稳定性**)
.venv/bin/python -m eval.jitter_probe --runs 12 --config both \
  --output evidence/checkpoints/topk_jitter.json

# ③ 探针自己的单元测试
.venv/bin/python -m pytest scripts/tests/test_jitter_probe.py -v
```

**打谁**: 层① 里 `max_cluster >= 5` 的 11 题 (`q38 q104 q39 q08 q29 q81 q77 q108 q07 q84 q118`,
含挤占最重的 q38 max_cluster=14)。抖动只在同质簇尾部才有翻转空间, 所以量化就打最可能翻的这批 ——
它们不抖, 挤占更轻的题更不会抖。

**⚠️ 条目标识用 `chunk_id`, 不是 `文件名#section`**。控制器首版探针用后者, 63 个域的文件名都是 `spec.md`、
section 都是 `DOMAIN` → 14 条塌缩成 1 个字符串, 探针于是"证明"了稳定性。
`stability_report` 现在自带护栏: 所有标识去重后 ≤ 1 种就抛 `ValueError("indistinguishable identifiers: ...")`,
`test_identifiers_must_be_distinguishable` 锁住它。

---

## 2. 检索稳定性

格式: `成分种类数 / 顺序种类数 / 逐位稳定前缀 / 非每次都在的条目数`

样本2 (committed `topk_jitter.json`, 每题 12 次) —— **11 题两个配置全部 `1 / 1 / 15 / 0`**:

| 题 | hybrid (生产口径) | dense-only |
|---|---|---|
| q38 | 1 / 1 / 15 / 0 | 1 / 1 / 15 / 0 |
| q104 | 1 / 1 / 15 / 0 | 1 / 1 / 15 / 0 |
| q39 | 1 / 1 / 15 / 0 | 1 / 1 / 15 / 0 |
| q08 | 1 / 1 / 15 / 0 | 1 / 1 / 15 / 0 |
| q29 | 1 / 1 / 15 / 0 | 1 / 1 / 15 / 0 |
| q81 | 1 / 1 / 15 / 0 | 1 / 1 / 15 / 0 |
| q77 | 1 / 1 / 15 / 0 | 1 / 1 / 15 / 0 |
| q108 | 1 / 1 / 15 / 0 | 1 / 1 / 15 / 0 |
| q07 | 1 / 1 / 15 / 0 | 1 / 1 / 15 / 0 |
| q84 | 1 / 1 / 15 / 0 | 1 / 1 / 15 / 0 |
| q118 | 1 / 1 / 15 / 0 | 1 / 1 / 15 / 0 |

样本1 (`topk_jitter_sample1.json`, 另一次独立的 12 次, 早 8 分钟) 同表只有一处不同:

| 题 | hybrid | dense |
|---|---|---|
| q08 | 1 / 1 / 15 / 0 | **1 / 2 / 10 / 0** |

> 样本1 由本探针的**早期修订**产出: 检索循环 (`probe_question` / `stability_report`) 与当前版本相同,
> 缺的是后加的 `embedding_jitter` / `dense_margin` / `pool_boundary` 三段测量, 故该文件只有 `configs` 段
> (文件内 `_note` 键写了同一句)。留着它的唯一理由: **唯一一次观察到的抖动就在里面**, 删掉证据就只剩"没观察到"。

### 2.1 跨时间窗比对 (两个样本相隔 8 分钟)

```bash
.venv/bin/python - <<'PY'
import json
def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)
a = load("evidence/checkpoints/topk_jitter_sample1.json")
b = load("evidence/checkpoints/topk_jitter.json")
print("样本1", a["generated_at"], " 样本2", b["generated_at"])
for cfg in ("hybrid", "dense"):
    for q in a["ids"]:
        ra, rb = a["configs"][cfg][q], b["configs"][cfg][q]
        setsame = {frozenset(r) for r in ra["runs"]} == {frozenset(r) for r in rb["runs"]}
        ordsame = {tuple(r) for r in ra["runs"]} == {tuple(r) for r in rb["runs"]}
        if not (setsame and ordsame):
            print(f"[{cfg}] {q}: 集合跨样本相同={setsame} 顺序跨样本相同={ordsame}")
print("done")
PY
```
```
样本1 2026-08-07T13:48:02+0900  样本2 2026-08-07T13:55:46+0900
[dense] q08: 集合跨样本相同=True 顺序跨样本相同=False
done
```

**22 组 (11 题 × 2 配置) 里, 21 组跨样本连顺序都逐位相同; 唯一的例外 q08 也只是顺序变, 集合相同。**

### 2.2 唯一一次实测到的抖动: dense q08, 12 次里的第 4 次

第 11-13 位三条**轮转**, 前 10 位与后 2 位逐位相同, **集合完全一致**:

```
pos 11: domains/AE/spec.md#2  ->  domains/FA/spec.md#2
pos 12: domains/FA/spec.md#2  ->  domains/GF/spec.md#2
pos 13: domains/GF/spec.md#2  ->  domains/AE/spec.md#2
集合相同: True
```

这三条正文**逐字节相同** (都是 `### USUBJID` 模板行), 见 §4 —— 翻转发生在"内容完全一样、
谁排前面本来就没有意义"的三条之间。

---

## 3. 抖动源: embedding 重复调用不逐位相同 (11/11 题)

| 题 | emb 逐位相同 | emb max\|Δ\| | emb L2 | 单条 sim 漂移 | 相邻对**差值**漂移 | top-15 最小间隔 | 严格并列对 | 池边界间隔 |
|---|---|---|---|---|---|---|---|---|
| q38 | False | 7.63e-05 | 8.76e-04 | 3.18e-05 | 3.36e-05 | 0.00e+00 | 4/14 | 0.00e+00 |
| q104 | False | 9.16e-05 | 8.88e-04 | 5.75e-05 | 3.88e-05 | 0.00e+00 | 1/14 | 7.41e-05 |
| q39 | False | 6.10e-05 | 8.26e-04 | 8.29e-06 | 1.01e-06 | 0.00e+00 | 10/14 | 1.52e-02 |
| q08 | False | 1.22e-04 | 9.01e-04 | 5.86e-05 | 7.34e-05 | 0.00e+00 | 5/14 | 8.46e-06 |
| q29 | False | 9.16e-05 | 7.98e-04 | 4.94e-05 | 4.04e-05 | 5.57e-04 | 0/14 | 1.71e-03 |
| q81 | False | 9.16e-05 | 8.28e-04 | 5.07e-05 | 3.49e-05 | 0.00e+00 | 10/14 | 1.13e-06 |
| q77 | False | 1.22e-04 | 9.53e-04 | 8.79e-05 | 4.90e-05 | 3.50e-05 | 0/14 | 3.38e-04 |
| q108 | False | 1.22e-04 | 9.49e-04 | 1.04e-04 | 1.57e-04 | 1.01e-04 | 0/14 | 4.43e-04 |
| q07 | False | 1.22e-04 | 1.17e-03 | 4.15e-05 | 5.75e-05 | 2.49e-05 | 0/14 | 1.38e-03 |
| q84 | False | 1.83e-04 | 2.16e-03 | 1.90e-04 | 1.41e-04 | 0.00e+00 | 2/14 | 0.00e+00 |
| q118 | False | 1.22e-04 | 1.16e-03 | 4.06e-05 | 3.59e-05 | 1.60e-04 | 0/14 | 1.37e-03 |

读法:

- **`identical` 全 False**: 同一 query 连调 12 次 embedding API, 12 个向量**没有一次逐位相同**。
  与 Task 3 的独立指纹一致 —— 那次 29 条 `sim` 漂移里, 4 条 BM25 量纲的**一条都没漂**
  (BM25 给定相同 token 是确定性的、不过 embedding), 抖动源只在 embedding 通道。
- **间隔必须用全精度算**。`RetrievedChunk.similarity` 建对象时就 `round(..., 4)` 了 (`server/rag.py:589`),
  拿它算间隔会得到一堆假的 0。表里的间隔全部走裸 `collection.query` 的 raw distance。
  (hybrid 配置下 `similarity` 还**混量纲** —— BM25 命中的条目填的是 BM25 分, 见 `server/rag.py:666` ——
  所以探针 stdout 里 hybrid 那列的 `min_gap` 不可解读, 本表的间隔一律取 dense 通道。)
- **单条 sim 漂移 (1e-5 ~ 1.9e-4) 远小于向量 L2 漂移 (~9e-4)**, 而**相邻对差值的漂移**通常更小
  (q39 只有 1.01e-06)。原因: query 向量的扰动 δ 对同簇文档的 sim 是**同向**推动
  (`Δsim_i = δ·d_i`, 同簇 `d_i` 彼此接近 → 差值 `δ·(d_i−d_j)` 更小)。
  **只拿"L2 漂移 9e-4 > 间隔 3.5e-5"就断言"必翻", 会高估风险** —— 单元测试
  `test_pair_margins_absolute_drift_vs_differential_drift` 专门锁这个区别。
- **"严格并列对" = 全精度 sim 完全相等的相邻对** (q39/q81 各 10/14)。这类对差值**恒为 0**,
  抖动无法通过 sim 把它翻过来; 谁前谁后由 Chroma 的 HNSW 决定 —— 稳定, 但也**任意**。

---

## 4. 为什么这么多并列: 库里存着逐字节重复的 chunk (全库实测)

```bash
.venv/bin/python - <<'PY'
from collections import defaultdict
from server.config import settings
import chromadb
c = chromadb.PersistentClient(path=str(settings.chroma_dir)).get_collection(settings.collection_name)
r = c.get(include=['embeddings', 'documents'])
by = defaultdict(list)
for i, doc, e in zip(r['ids'], r['documents'], r['embeddings']):
    by[doc].append((i, tuple(e)))
dup = {k: v for k, v in by.items() if len(v) > 1}
print('总 chunk:', len(r['ids']))
print('重复正文种类:', len(dup), '涉及 chunk:', sum(len(v) for v in dup.values()))
same = sum(1 for v in dup.values() if len({e for _, e in v}) == 1)
print('向量也完全一致的正文种类:', same, '向量不一致的:', len(dup) - same)
for k, v in sorted(dup.items(), key=lambda kv: -len(kv[1]))[:3]:
    print(' 规模', len(v), '向量种类', len({e for _, e in v}), repr(k[:60]))
PY
```
```
总 chunk: 4315
重复正文种类: 47 涉及 chunk: 373
向量也完全一致的正文种类: 7 向量不一致的: 40
 规模 61 向量种类 17 '### STUDYID\n- **Order:** 1\n- **Label:** Study Identifier\n- *'
 规模 57 向量种类 16 '### DOMAIN\n- **Order:** 2\n- **Label:** Domain Abbreviation\n-'
 规模 48 向量种类 16 '### USUBJID\n- **Order:** 3\n- **Label:** Unique Subject Ident'
```

**这是层① 挤占的物理来源, 也是"排位无意义"的物理来源**:

1. 63 个域的 `spec.md` 里, `STUDYID`/`DOMAIN`/`USUBJID` 这些通用变量行**逐字节相同** (61/57/48 条)。
2. 但它们在库里的**向量不同**: 61 条相同正文分裂成 **17 种**向量。ingest 按 batch 调 embedding API
   (`scripts/ingest.py` `EMBED_BATCH_SIZE=100`), **同批得到同一向量, 跨批就不同** ——
   也就是说, **索引里已经烙进了 embedding API 的非确定性**。
3. 于是 61 条内容完全一样的 chunk 拿到 17 档只差 ~1e-5 的 sim。**谁排第 11 位、谁第 12 位,
   由 ingest 当天落在哪个 batch 决定, 不由相关性决定。**
4. 查询侧的抖动 (§3) 恰是同一量级, 于是能在这些"内容等价"的条目间来回翻 —— §2.2 里 q08 的
   AE/FA/GF 轮转正是如此 (三条正文逐字节相同, 其中 `FA` 与 `GF` 向量**完全相同**、
   `AE` 与它们差 max\|Δ\|=1.22e-04 —— 落在了不同的 ingest batch)。

---

## 5. 判定

| 观察 | 命中 brief 判定表 | 结论 |
|---|---|---|
| 成分变: 20 进程 × 140 题下 5/140; 扰动 8400 次下 5/140; 真实世界两条实例 (§0.2) | **第 3 行: 成分变** | `JITTER_AFFECTS_STATS = **true**` |

**以下 §5.1-§5.5 是第一版 (采样口径) 的分析, 保留原样不删** —— 它们的测量都成立, 只是当时被我用来支撑
一个反了的结论。保留的价值: §5.1 解释了"为什么成分比排位稳得多"(仍然正确, 且正是
`max_cluster` 0/140 变化的原因), §5.2/§5.3 正是把我引向 §0 那个方法论错误的现场。

> 阅读提示: 凡 §5.x 里出现"528 次没变"的措辞, 一律按 §0.1 打折 —— 那 528 次全在**单个进程内**,
> 而进程内取样对单一状态有 ~95% 的强偏向, 因此系统性低估状态分布 (**不是**完全量不到, 见 §0.1c)。

### 5.1 结构上为什么成分比排位稳 (不只是"没观察到")

决定 top-15 成分的是**第 15 名与第 16 名之间那道线**。实测这道线的全精度间隔:

```bash
.venv/bin/python - <<'PY'
import yaml
from eval.jitter_probe import _engine, dense_sims
with open("eval/test_set_v3.yml", encoding="utf-8") as f:
    by_id = {q["id"]: q for q in yaml.safe_load(f)}
rag = _engine("dense", 16)
for qid in ["q38","q104","q39","q08","q29","q81","q77","q108","q07","q84","q118"]:
    vecs = [rag._embed_query(by_id[qid]["question"]) for _ in range(3)]
    ids0, s0 = dense_sims(rag, vecs[0], 16)
    a, b = ids0[14], ids0[15]
    gaps = [s[a] - s[b] for _, s in (dense_sims(rag, v, 16) for v in vecs) if a in s and b in s]
    print(f"{qid:>6}  gap={gaps[0]:.3e}  3次范围=[{min(gaps):.3e},{max(gaps):.3e}] "
          f"翻转={sum(1 for g in gaps if g < 0)}")
PY
```
```
   q38  gap=1.550e-06  3次范围=[1.550e-06,1.550e-06] 翻转=0
  q104  gap=5.681e-04  3次范围=[5.681e-04,5.707e-04] 翻转=0
   q39  gap=0.000e+00  3次范围=[0.000e+00,0.000e+00] 翻转=0
   q08  gap=7.987e-06  3次范围=[7.987e-06,7.987e-06] 翻转=0
   q29  gap=1.033e-04  3次范围=[1.033e-04,1.185e-04] 翻转=0
   q81  gap=0.000e+00  3次范围=[0.000e+00,0.000e+00] 翻转=0
   q77  gap=1.121e-03  3次范围=[1.121e-03,1.121e-03] 翻转=0
  q108  gap=1.363e-03  3次范围=[1.363e-03,1.449e-03] 翻转=0
   q07  gap=1.973e-04  3次范围=[1.973e-04,1.993e-04] 翻转=0
   q84  gap=6.020e-06  3次范围=[6.020e-06,6.437e-06] 翻转=0
  q118  gap=5.677e-04  3次范围=[5.624e-04,5.677e-04] 翻转=0
```

**5/11 题的 15/16 名间隔 ≤ 8e-06** (q38 1.55e-06, q39 与 q81 严格为 0, q84 6.02e-06, q08 7.99e-06) ——
拿它跟"单条 sim 漂移 ~1e-4"比, 看起来必翻。**但这道线两侧恰恰是内容等价的重复 chunk**,
所以真正决定翻不翻的**差值**几乎不漂: 三次采样里这些间隔要么逐位不变, 要么只动 4e-7 (q84),
远小于间隔本身。这才是成分稳的原因, 而不是运气。

### 5.2 连跑会低估抖动吗 —— 把取样在时间上铺开

12 次连跑有个隐患: **同一 query 连调 API 可能拿回同一个向量** (本次测量中确实见过
`identical=True` 的 2 次采样), 那 12 次就不是 12 个独立样本。故补一次**时间铺开**的取样:
15 次、每次隔 25 秒、共 350 秒, 同时记录向量指纹与 top-15 / top-30 集合。

```bash
.venv/bin/python - <<'PY'
import hashlib, time, yaml
from eval.jitter_probe import _engine, dense_sims
N, GAP = 15, 25
with open("eval/test_set_v3.yml", encoding="utf-8") as f:
    by_id = {q["id"]: q for q in yaml.safe_load(f)}
rag = _engine("dense", 31)
hist = {q: [] for q in ("q38", "q08")}
for k in range(N):
    for qid in hist:
        v = rag._embed_query(by_id[qid]["question"])
        ids, _ = dense_sims(rag, v, 31)
        hist[qid].append((hashlib.sha1(repr(v).encode()).hexdigest()[:8],
                          frozenset(ids[:15]), frozenset(ids[:30]), ids[29], ids[30]))
    if k < N - 1:
        time.sleep(GAP)
for qid, rows in hist.items():
    print(f"{qid}: 取样 {len(rows)} 次, 跨 {(N-1)*GAP}s")
    print(f"   不同的 embedding 向量: {len({r[0] for r in rows})} 种")
    print(f"   不同的 top-15 集合:    {len({r[1] for r in rows})} 种")
    print(f"   不同的 top-30 集合:    {len({r[2] for r in rows})} 种")
    print(f"   第30名出现过: {sorted({r[3].split('/')[1] for r in rows})}"
          f"  第31名出现过: {sorted({r[4].split('/')[1] for r in rows})}")
PY
```
```
q38: 取样 15 次, 跨 350s
   不同的 embedding 向量: 3 种
   不同的 top-15 集合:    1 种
   不同的 top-30 集合:    1 种
   第30名出现过: ['HO']  第31名出现过: ['RP']
q08: 取样 15 次, 跨 350s
   不同的 embedding 向量: 2 种
   不同的 top-15 集合:    1 种
   不同的 top-30 集合:    1 种
   第30名出现过: ['UR']  第31名出现过: ['MS', 'RE']
```

**embedding API 返回的是一小组离散向量** (350 秒内只见到 2-3 种, 且会重复出现), 不是连续随机游走。
在这一小组向量上, top-15 与 top-30 的集合都不变; 只有 q08 的第 31 位在 MS / RE 之间来回。

### 5.3 池 (top-30) 的成分**跨时间窗确实变过** —— 这是本报告最该被后人看见的一条

上面那个窗口里 q38 的第 30 名恒为 `HO`。窗口结束一分钟后再拉一次:

```bash
.venv/bin/python - <<'PY'
import yaml
from eval.jitter_probe import _engine, dense_sims
with open("eval/test_set_v3.yml", encoding="utf-8") as f:
    by_id = {q["id"]: q for q in yaml.safe_load(f)}
rag = _engine("dense", 31)
ids, s = dense_sims(rag, rag._embed_query(by_id["q38"]["question"]), 31)
doms = [i.split('/')[1] for i in ids]
print("当前 top-31:", doms)
for d in ("TE", "HO", "TV", "RP"):
    print(f"  {d}: 在 top-30 里={d in doms[:30]}  在 top-31 里={d in doms}")
PY
```
```
当前 top-31: [..., 'TA', 'TU', 'VS', 'SR', 'TE', 'TV']
  TE: 在 top-30 里=True   在 top-31 里=True
  HO: 在 top-30 里=False  在 top-31 里=False
  TV: 在 top-30 里=False  在 top-31 里=True
  RP: 在 top-30 里=False  在 top-31 里=False
```

**`HO` 原本占着第 30 名 (15/15 次), 一分钟后整个跌出 top-31, 由 `TE` 顶上。**
生产 hybrid 恰好按 `hybrid_pool=30` 取 dense 前 30 名进 RRF —— 也就是说,
**融合的输入名单跨时间窗是会变的**, 不只是"池外一步之遥在动"。

为什么这仍然不动摇 `JITTER_AFFECTS_STATS = false`, 两条独立理由:

1. **实测**: §2.1 的跨样本比对 (相隔 8 分钟的两个窗口, 22 组) 显示 top-15 集合**逐题相同**。
   换人发生在第 26-31 名 (那一带 sim 全部 ≈ 0.66893, 见 §3), 没有传导到 top-15。
2. **结构**: 换上换下的双方 (`HO` / `TE` / `TV` / `RP` … ) 全是 §DOMAIN 那个**逐字节重复类**的成员。
   就算某次换人真的传导进 top-15, 也是**拿一条 `### DOMAIN` 换另一条 `### DOMAIN`** ——
   而 `max_cluster` / `dup_seats` 数的是 **section 名占了几席**, 不问是哪个域的那一席。
   **变的恰好是这些统计不看的那一维。**

### 5.4 这条证据能证明什么

- 生产口径 (hybrid + S1) 下, 11 道挤占最重的题, 两个时间窗共 24 次独立运行, top-15 **成分与顺序都没变过**;
  跨样本比对集合逐题相同。
- 抖动源已定位: 重复调用 embedding, 11/11 题**向量不逐位相同** (max\|Δ\| ~1e-4 / L2 ~9e-4),
  且返回值是一小组离散向量 (§5.2)。
- 抖动能翻的位置已定位: 内容**逐字节相同**、sim 只差 ~1e-5 的同质簇内部 (§2.2 那次轮转就在这里)。
- 集合统计与排位统计的稳健性**不同**: 前者稳 (§5.1 结构理由 + §5.3 不变性理由), 后者不稳。

### 5.5 这条证据不能证明什么

1. ~~**不能证明 top-15 成分永远稳定。**~~ **已被 §0 推翻: 成分确实会变。** 下面这条原文保留,
   是第一版在单进程盲区下写的。
   而且**池的成分已经实测会变** (§5.3) —— 只是这次没传导到 top-15。
   若日后有人调大 `hybrid_pool`、改融合权重、或把 k 从 15 改成别的值, **本结论必须重测**:
   切割线一动, 它落在哪个并列组中间就重新掷骰子了。
2. **不能证明并列条目的先后稳定。** Chroma 走 HNSW **近似**最近邻; 严格并列时 (差值恒为 0)
   谁前谁后不由 sim 决定, 24 次一致不等于实现保证。同一批测量里还看到: 同一时间窗内
   把 `n_results` 从 31 改成 40, 第 31 名从 `TV` 变成 `RP` (各 4 次, 交替跑, 每次都复现) ——
   **近似检索的返回尾巴与请求深度有关**。这与 query 抖动是两回事, 但同样让"第 N 名是谁"不可当事实。
3. **不能证明跨时间/跨环境成立。** 全部数据采于 2026-08-07 15:00 前后同一小时内、同一 embedding
   端点 (`text-embedding-3-small`)。评审那次真实看到的第 9 位变化发生在别的时刻,
   **本次没复现它不等于它没发生**; 能说的是: 那种变化若是同质簇内的轮转 (与 §2.2 实测的 q08 形态一致),
   则集合仍不变, 层① 数字仍成立。
4. **不能用来给检索质量背书。** 稳定 ≠ 正确。61 条内容等价的 chunk 稳定地占着 top-15,
   这是稳定的**挤占**, 不是稳定的**好**。好坏归层② (Task 6)。

### 5.6 `max_cluster` 豁免的机制与失效条件 (引用豁免必须连这段一起带)

只写"0/140"是不够的 —— 下一个人无法判断这个豁免**在什么条件下失效**。

**机制**: 抖动换掉的永远是"**哪个域**"(实测: TE ↔ OE ↔ TR ↔ RP), 而这些 chunk 全都是
`domains/*/spec.md#1`, section **一律是 `DOMAIN`**。换人不换 section ⇒ §DOMAIN 簇的**席位数恒定**。

**为什么这是结构必然而非巧合**: 重复 chunk 之所以成为 HNSW 的歧义源, 正因为它们**正文逐字节相同**
(§4: 4315 条里 373 条正文重复); 而**正文相同就意味着 section 相同**。
所以 **抖动天然发生在簇内部** —— 它换的恰好是按 section 名计席位的统计**不看**的那一维。

**失效条件 (任一成立就必须重测)**:

1. **churn 跨出簇** —— q47 / q117 就是现成的反例: 它们的换人跨了 section 名, 于是
   `dup_seats` / `distinct_sections` 立刻不稳。所以豁免只覆盖 `max_cluster`, 不覆盖另两个。
2. **Task 6 去重** —— 去掉重复 chunk 就等于拆掉歧义源, 整个前提消失。
3. **Task 8 重灌索引** —— 重新分批 embed, §4 的 17 档向量重排。
4. **改 chunk 切分或 section 命名** —— "正文相同 ⇒ section 相同"这一步就断了。
5. 改 `top_k` / `hybrid_pool` / 融合权重 —— 切割线换位置。

> **[2026-08-07 Task 8] 条件 3 与 4 已触发, 本节的逐题数字对新索引失效, 已重测。**
> chapters 取消"整文件单块"档 (ch01/02/03 按 H2 切), 索引重灌 **4315 → 4329**。
> 上文 §4 的 "4315 条里 373 条正文重复" 是当时的实测记录, 保留不改写。
> 重测结论 (140 题层① + q38/q47/q117 × 20 进程) 见
> `evidence/checkpoints/chapters_chunking.md` §6 / §6.1: 豁免的机制前提在新索引下依然成立
> (q38 反而 churn 归零), 但**数字一律以重测值为准, 不得沿用本文件的旧值**。

---

## 6. 对 Task 4 的具体要求 (按 `true` 修订)

1. **必须跨独立进程取样。这是硬要求, 不是优化。** 进程内循环 N 次 = 1 个样本 (§0.1: 同样 20 次,
   单进程报"成分种类 1", 20 个独立进程报"成分种类 4")。用 `stability_across_processes(...)`,
   它起真正的子进程 (`subprocess`, 不是 `multiprocessing` —— 后者从 heredoc/REPL 调会挂死, 实测挂满 10 分钟):

   ```python
   from eval.jitter_probe import stability_across_processes
   rep = stability_across_processes(question, n_procs=20, config="hybrid", top_k=15)
   # rep["runs"] 是 20 个进程各自的 top-15 chunk_id 列表; 往上套你的 crowding_stats
   ```
   `n_procs < 2` 会直接抛错 —— 不给"1 个进程也算验过稳"留后门。

   **`n_procs=20` 是"检出不稳定"的下限, 不是"刻画分布"的够用值** (§0.1): 稀有态出现在 1/20 量级,
   不同批次见到的状态集合还不一样。q47 那种四六开的分布 20 次够描述; 要给稀有态一个可信频率,
   得再上一个量级。**报告里只说"见到 N 种状态", 别把 20 次的频率当概率写。**

   可选叠加: `perturbed_vectors` + `retrieve_under_perturbation` 在进程内按实测幅度扰动 query 向量
   (零 API 开销, 140 题 131 秒)。它量的是**另一个**源, 不能替代跨进程取样。

2. **逐题报告稳定性, 不许只报众数。** 每题至少给: 众数值 + 不同取值的个数 + 各自出现次数。
   当前已知不稳: **q47**(生产口径 20 进程下 `(2,2,13)` 12 次 vs `(2,1,14)` 8 次 —— **接近四六开**)、
   **q117**(固定向量下 1/20)。两题都必须点名, **不能把 q47 的 `dup_seats` 当事实写**。
3. **哪些已发布数字要重算**:
   - `max_cluster` 及一切基于它的聚合 (含 **"28.6%"**): **不用重算** —— 三个测量全部 0/140。
     **引用时必须连 §5.6 的机制与失效条件一起带**: 豁免成立是因为"正文逐字节相同 ⇒ section 相同
     ⇒ 抖动天然在簇内部"; Task 6 去重 / Task 8 重灌 / 改切分或 section 命名, 任一发生即失效。
   - `dup_seats` / `distinct_sections` 的**逐题值**: q47 必须按分布报告, q117 需标注; 其余 138 题稳定。
   - 任何**按排位**的结论: 一律作废, 不是重算的问题 (§4 结构理由)。
4. **探针只许输出集合统计, 不许输出排位结论。** `crowding_stats` 那四个字段都不看顺序, 保持这样。
   不要新增"簇头排在第几位""top-3 里有几条属于簇"这类依赖排位的字段。
5. **`composition` 明细可以留, 但必须标清是单次快照。** 数组里的顺序、以及具体哪个域填了某席位,
   都是噪声决定的 (§4)。**"AE 排在 FA 前面"不可引用; "有 14 席被 §DOMAIN 占掉"可引用。**
6. **证据里必须写这句可复现性声明** (brief 硬要求, 已按 `true` 改写, 原样抄):

   > 本表逐题数字出自**单次** top-15 (生产口径 hybrid + S1), 并已按 Task 3B 的口径做过稳定性验证:
   > **20 个独立进程**各跑一遍全 140 题 (跨进程取样是必须的 —— 进程内取样严重偏向单一状态, ~95%),
   > 结果 `max_cluster` **0/140 题**变化, `dup_seats` / `distinct_sections` **1/140 题**变化 (q47);
   > 另有 8400 次向量扰动的独立测量结论一致。
   > 故基于 `max_cluster` 的数字可直接引用; **q47 (接近四六开) 与 q117 的
   > `dup_seats`/`distinct_sections` 不稳定, 已按分布单独标注**。
   > 抖动的完整量化与方法论见 `evidence/checkpoints/topk_jitter.md`
   > (含"同进程内重复 N 次不是 N 个独立样本"这一坑, 以及根因: Chroma HNSW 在一批向量完全相同的
   > 重复 chunk 之间的选择进程内稳定、换进程会变)。
   > **排位一律不可复现**, 本表不含也不支持任何按排位下的结论。

7. **若重灌索引 / 改 `top_k` / 改 `hybrid_pool` / 改融合权重, 全部重测。** 本结论只对
   "k=15 + pool=30 + 当前索引"这条切割线成立。重灌会重新分批调 embedding, §4 的 17 档向量会重排。

---

## 7. 探针自己的测试

```bash
.venv/bin/python -m pytest scripts/tests/test_jitter_probe.py -v
```
→ **14 passed** (4 brief + 3 + 4 + 3)。brief 给的 4 条 (统计口径 + 标识可区分性护栏) 逐字落地; 另补 3 条, 覆盖后加的
`min_adjacent_gap` / `pair_margins` —— 它们产出的数字进了 §3 表, 不能没测:

- `test_min_adjacent_gap` —— 取最小的那一对; 全精度并列返回 0.0; 不足一对返回 None
- `test_pair_margins_detects_real_flip` —— 真翻转必须被记成 `flipped`, `min_margin` 为负
- `test_pair_margins_absolute_drift_vs_differential_drift` —— 两条 sim 各漂 0.01 但**差值不漂**时
  不许报翻转风险 (锁住 §3 那个"别用绝对漂移吓自己"的口径)

另 4 条覆盖修正版新增的扰动注入 (Task 4 要靠它验稳, 它自己必须先被验):

- `test_perturbed_vectors_hits_requested_distance` —— 扰动幅度**恰好**是请求的 L2; 不就地改输入
- `test_perturbed_vectors_is_deterministic_given_seed` —— 同 seed 逐位重现 (证据要能复跑)
- `test_retrieve_under_perturbation_feeds_each_vector_and_restores_embed` —— 每个向量都真被用上, 用完还原
- `test_retrieve_under_perturbation_restores_embed_on_error` —— 检索抛错也必须还原,
  否则引擎被永久钉在假向量上, 后续所有检索静默作废

再 3 条覆盖跨进程取样 (第一版盲区的补丁):

- `test_stability_across_processes_rejects_single_process` —— `n_procs < 2` 必须抛错。
  不给"1 个进程也算验过稳"留后门 —— 第一版的教训正是"样本数看着大、独立样本数其实是 1"
- `test_stability_across_processes_aggregates_runner_output` —— 注入 runner 验聚合口径与固定向量透传
- `test_stability_across_processes_real_subprocess_smoke` (`@pytest.mark.slow`) —— **真起 2 个子进程**。
  上面两条都注入 fake runner, 只验聚合与透传; 而**整个改判压在真实子进程这条路径上**,
  它若因 cwd / 模块名 / 序列化起不来, 那两条一条都不会红。只断言"跑得通且形状对", 不断言稳定性

全量:

```bash
.venv/bin/python -m pytest -q --junit-xml=/tmp/j.xml   # 本仓 pytest 吞末行统计, 数字读 xml
```
→ **896 passed, 0 failed** (本 task 之前实测基线 **882**, 本 task +14)。
