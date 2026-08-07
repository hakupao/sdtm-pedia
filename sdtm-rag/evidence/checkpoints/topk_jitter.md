# top-k 抖动量化 (Task 3B)

> 日期: 2026-08-07 · 探针 `eval/jitter_probe.py` · 数据 `evidence/checkpoints/topk_jitter.json`(样本2) + `topk_jitter_sample1.json`(样本1)
> 起因: Task 1 评审同 query 同参数连跑两次, top-15 **第 9 位起成分变化**; 控制器随后用 chunk_id 跑 5 次却全稳定 → 抖动**偶发**。
> 层① 的 `max_cluster` / `dup_seats` / "28.6%" 全部出自**单次** top-15, 在量化清楚之前不许当稳定事实引用。

## 结论

**`JITTER_AFFECTS_STATS = false`**

528 次检索 (11 题 × 12 次 × 2 配置 × 2 个时间窗) 里, top-15 的**成分**一次没变 (`sometimes == 0` 全表,
跨样本比对集合也逐题相同)。唯一一次变化是**顺序**变化: dense q08 在 24 次里的 1 次, 第 11-13 位三条轮转,
**集合不变**。命中 brief 判定表第 2 行 —— `max_cluster` / `dup_seats` 是**集合统计**, 不看顺序,
故 **Task 4 单次取样即可, 层① 已发布的数字不需要重算**。

但**排位不可复现**: 任何"第 N 位是什么""排在前面所以更相关"的结论无效。理由不止是"观察到过一次翻转",
而是 §4 的结构事实 —— 挤占席位的那些 chunk **正文逐字节相同**, 它们之间的先后由 ingest 分批噪声决定。

⚠️ 两条必须跟着结论一起被引用的限定:

- **dense 池 (top-30, 即 hybrid 融合的输入) 的成分跨时间窗实测会变** (§5.3: `HO` 占了 15/15 次的第 30 名,
  一分钟后整个跌出 top-31)。它这次没传导到 top-15, 且换上换下的双方同属同一批逐字节重复的 chunk ——
  **变的正是"哪个域"这一维, 而 `max_cluster`/`dup_seats` 数的是"section 名占几席", 不看这一维。**
- 本结论只对**当前切割线 (`top_k=15` + `hybrid_pool=30`)** 成立。改 k、改池深、改融合权重或重灌索引, 都要重测 (§5.5-1, §6-5)。

---

## 1. 复现命令

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag

# 主探针: 11 题 x 12 次 x 2 配置 = 264 次检索, 每次新建 RAGEngine 并重新 embed
.venv/bin/python -m eval.jitter_probe --runs 12 --config both \
  --output evidence/checkpoints/topk_jitter.json

# 探针自己的单元测试 (统计口径 + 标识可区分性护栏)
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
| 528 次里成分种类数恒 = 1、`sometimes == 0` 全表; 顺序种类数出现过一次 = 2 | **第 2 行: 顺序变但成分不变** | `JITTER_AFFECTS_STATS = **false**` |

`max_cluster` / `dup_seats` / `distinct_sections` 都在 top-15 的**集合**上算 (`Counter(section)` 不看顺序),
而成分在 528 次检索、两个时间窗里一次没变 → 层① 数字不因抖动而变。

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

1. **不能证明 top-15 成分永远稳定。** 这是"528 次没观察到 + 两条理由", 不是形式证明。
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

---

## 6. 对 Task 4 的具体要求

1. **单次取样即可**, 不必跑 N 次取交集/众数。理由: 成分统计在 528 次运行、两个时间窗里零变化 (§2),
   且有两条结构理由 (§5.1 切割线两侧是重复 chunk、差值几乎不漂; §5.3 会变的那一维正是这些统计不看的一维)。
2. **证据里必须写这句可复现性声明** (brief 硬要求, 原样抄):

   > 本表数字出自**单次** top-15 (生产口径 hybrid + S1)。抖动已由 Task 3B 量化
   > (`evidence/checkpoints/topk_jitter.md`): 11 道挤占最重的题各跑 24 次、跨两个时间窗,
   > top-15 **成分零变化** (`sometimes == 0` 全表), 故集合统计 (`max_cluster` / `dup_seats` /
   > `distinct_sections`) 可单次取样; 但**排位不可复现**, 本表不含也不支持任何按排位下的结论。
   > 另注: dense 池 (top-30) 的成分**跨时间窗实测会变**, 换上换下的双方同属同一批逐字节重复的
   > chunk, 故按 section 名计席位的统计对它不敏感 (Task 3B §5.3)。

3. **探针只许输出集合统计, 不许输出排位结论。** `crowding_stats` 的四个字段
   (`dup_seats` / `max_cluster` / `max_cluster_section` / `distinct_sections`) 都不看顺序, 保持这样。
   不要新增"簇头排在第几位""top-3 里有几条属于簇"这类**依赖排位**的字段 —— 那类数字不可复现 (§5.3)。
4. **`composition` 明细可以留, 但要标清它是单次快照。** 数组里的**顺序**、以及**具体哪个域**填了某个席位,
   都是噪声决定的 (§4): 61 条逐字节相同的 chunk 谁进 top-15, 由 ingest 分批决定。
   **"AE 排在 FA 前面"不可引用; "有 14 席被 §DOMAIN 占掉"可引用。**
5. **若日后重灌索引 (re-ingest), 层① 数字必须重算。** 重灌会重新分批调 embedding, §4 的 17 档向量会重排,
   同质簇内谁进 top-15 会变。簇的**规模**大概率不变, 但这需要重测, 不能沿用本结论。
   **同理, 改 `top_k`、改 `hybrid_pool`、改融合权重, 也都要重测** —— 本结论只对"k=15 + pool=30"这条切割线成立 (§5.5-1)。

---

## 7. 探针自己的测试

```bash
.venv/bin/python -m pytest scripts/tests/test_jitter_probe.py -v
```
→ **7 passed**。brief 给的 4 条 (统计口径 + 标识可区分性护栏) 逐字落地; 另补 3 条, 覆盖后加的
`min_adjacent_gap` / `pair_margins` —— 它们产出的数字进了 §3 表, 不能没测:

- `test_min_adjacent_gap` —— 取最小的那一对; 全精度并列返回 0.0; 不足一对返回 None
- `test_pair_margins_detects_real_flip` —— 真翻转必须被记成 `flipped`, `min_margin` 为负
- `test_pair_margins_absolute_drift_vs_differential_drift` —— 两条 sim 各漂 0.01 但**差值不漂**时
  不许报翻转风险 (锁住 §3 那个"别用绝对漂移吓自己"的口径)

全量:

```bash
.venv/bin/python -m pytest -q --junit-xml=/tmp/j.xml   # 本仓 pytest 吞末行统计, 数字读 xml
```
→ **889 passed, 0 failed** (本 task 之前实测基线 **882**, 本 task +7)。
