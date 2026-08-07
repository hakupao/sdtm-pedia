# 池深度不变性实测 (Task 5, 2026-08-07)

> 结论: **`POOL_DEEP_OK = false`** — 加深 `hybrid_pool` 会大幅改写生产 top-15。
> 附带结论: **`FUSE_OUT_DEEP_OK = true`** — 池深不动、只放长 `_hybrid_fuse` 的**输出**,
> top-15 逐位不变。Task 6 的 B 组据此能补满 15 席而不动池深 —— **但 139/140 题才能,
> q38 不能** (它的候选里 42/44 条同属 §DOMAIN, 配额 2/3/5 下分别只能凑 4/5/7 席),
> 那一题必须保留 fallback 口径。详见 §5。

工作目录 `sdtm-rag/`, 解释器 `.venv/bin/python`。探针 `eval/pool_depth_probe.py`,
单测 `scripts/tests/test_pool_depth_probe.py`。

---

## 1. 实验设计: 怎么把「池深度效应」和「跨进程抖动」分开

已知混杂 (Task 3B 实测): 检索结果**跨进程不稳定** —— 即使钉死 query 向量, 独立进程
跑同一条 query 仍可能换 top-15 尾部 (Chroma HNSW 在向量完全相同的重复 chunk 之间
返回谁不由 sim 决定); 且**进程内取样会系统性低估**这一维 (单进程连跑 60 次, 多数派
57/60 ≈ 95%)。

所以「一个进程跑 pool=30、另一个跑 pool=200, 比一比」是**无效设计** —— 比出来的差异
无法归因。本探针用五条臂拆开:

| 臂 | 比什么 | 抖动能否混入 |
|---|---|---|
| `algebraic` | **同一份** dense@200 / bm25@200 候选列表, 截到 30 与截到 200 分别过 `_hybrid_fuse` | **不能**。两侧输入逐位相同, `_hybrid_fuse` 是纯函数 |
| `candidate_prefix` | `_search(q,30)` vs `_search(q,200)[:30]`; BM25 同理 | 能 (单次调用) |
| `e2e` | 同进程、同一个引擎对象、同一份钉死向量, 交替跑 `[30,200,30,200]`, 只改 `hybrid_pool` | 由 **A/A 空白对照**扣掉 |
| `fuse_output_depth` | 池仍 30, 只把 `_hybrid_fuse` 输出从 15 放到 60 | 由 A/A 同一机制扣掉 |
| `seat_feasibility` | 同名 section 限 2/3/5 席时, 深融合候选最多能凑到几席 | 跨进程取**最小**席位数, 不用运气好的那个进程 |

**核心是 `e2e` 臂的 A/A 空白对照**。进程内调用序列 `[30, 200, 30, 200]`:

- **A/A 对** `(0,2)` `(1,3)` — 参数**完全相同**的两次调用。它们的不一致 = 这个进程内的
  **抖动本底**。
- **A/B 对** `(0,1)` `(2,3)` `(1,2)` `(0,3)` — 只差 `hybrid_pool` 一个变量。

判据: **A/B 的不一致必须超过 A/A**, 才能归因给池深度。A/A 全同而 A/B 有差 = 池深度
真有效应; 两者同样有差 = 那是抖动。

A/A 对跨越的调用间隔均为 2; A/B 四对中 `(0,1)` `(2,3)` `(1,2)` 的间隔是 1, **只有
`(0,3)` 是 3**。所以「A/A 全同 ⇒ 不能拿进程内随时间漂移解释 A/B」这条论证严格覆盖
A/B 四对中的**三对**; `(0,3)` 跨度大于任何 A/A 对, 单看它无法排除漂移。这不影响结论 ——
实测 A/A 恒 0 而 A/B 90% 不一致, 且间隔 1 的三对本身就足以定案, 更不必说零抖动的
`algebraic` 臂独立复现了同量级差异。

再跑 N 个独立进程, 一是重复 N 次上述配对 (样本数是真的), 二是顺带量出跨进程抖动的
实际幅度, 作为「这个混杂到底多大」的量纲。

query 向量在**父进程 embed 一次**, 所有子进程共用逐位相同的向量 —— embedding 这一维
被完全控制掉。

---

## 2. 命令与原始输出

### 2.1 主跑: 层① 挤占最重的 11 题 × 12 独立进程

```bash
cd sdtm-rag
.venv/bin/python -m eval.pool_depth_probe --procs 12 \
  --output evidence/checkpoints/pool_depth_invariance.json
```

```
题数 11  进程数 12  向量钉死 True  耗时 9.2s
[algebraic]        同候选截 30 vs 截 200, top-15 有差异的题: 10/11 ['q38', 'q104', 'q39', 'q08', 'q81', 'q77', 'q108', 'q07', 'q84', 'q118']
[candidate_prefix] _search(30) vs _search(200)[:30] 有差异的题: 8/11 ['q38', 'q104', 'q39', 'q29', 'q81', 'q77', 'q108', 'q84']
[e2e A/A 空白对照] 不一致 0/264 对, 最大逐位差 0
[e2e A/B 池深对照] 不一致 480/528 对, 最大逐位差 14
[fuse_output_depth] 池不动只放长融合输出到 60: 前 15 名有差异的题 0/11, 整条生产链有差异的题 0/11; 候选总数最小 38 条 (即 15 席之外余量 23)
[seat_feasibility] 配额=2: 凑不满 15 席的题 1/11 — q38=4席
[seat_feasibility] 配额=3: 凑不满 15 席的题 1/11 — q38=5席
[seat_feasibility] 配额=5: 凑不满 15 席的题 1/11 — q38=7席
[跨进程本底]       同题同参数, 12 进程结果不止一种的题: 1/11
POOL_DEEP_OK = False  ({'POOL_DEEP_OK': False, 'algebraic_ok': False, 'candidate_prefix_ok': False, 'e2e_ok': False, 'e2e_aa_mismatched': 0, 'e2e_ab_mismatched': 480, 'FUSE_OUT_DEEP_OK': True})
明细: evidence/checkpoints/pool_depth_invariance.json
```

### 2.2 全量: 题集 140 题 × 8 独立进程

```bash
cd sdtm-rag
.venv/bin/python -m eval.pool_depth_probe --procs 8 --ids all \
  --output evidence/checkpoints/pool_depth_invariance_all140.json
```

```
题数 140  进程数 8  向量钉死 True  耗时 22.2s
[algebraic]        同候选截 30 vs 截 200, top-15 有差异的题: 130/140 [...]
[candidate_prefix] _search(30) vs _search(200)[:30] 有差异的题: 58/140 [...]
[e2e A/A 空白对照] 不一致 0/2240 对, 最大逐位差 0
[e2e A/B 池深对照] 不一致 4032/4480 对, 最大逐位差 14
[fuse_output_depth] 池不动只放长融合输出到 60: 前 15 名有差异的题 0/140, 整条生产链有差异的题 0/140; 候选总数最小 37 条 (即 15 席之外余量 22)
[seat_feasibility] 配额=2: 凑不满 15 席的题 1/140 — q38=4席
[seat_feasibility] 配额=3: 凑不满 15 席的题 1/140 — q38=5席
[seat_feasibility] 配额=5: 凑不满 15 席的题 1/140 — q38=7席
[跨进程本底]       同题同参数, 8 进程结果不止一种的题: 6/140
POOL_DEEP_OK = False  ({'POOL_DEEP_OK': False, 'algebraic_ok': False, 'candidate_prefix_ok': False, 'e2e_ok': False, 'e2e_aa_mismatched': 0, 'e2e_ab_mismatched': 4032, 'FUSE_OUT_DEEP_OK': True})
明细: evidence/checkpoints/pool_depth_invariance_all140.json
```

(题号清单被上面截短; 完整清单在两份 JSON 的 `algebraic.mismatched` /
`candidate_prefix.mismatched` 字段。)

JSON 里的 `raw` 是**折叠存盘**的: 与 0 号进程逐字节相同的行折成
`{"id":…, "same_as_proc0": true}`, 差异行原样保留 (全量原样存盘 12 MB, 本仓 evidence
JSON 的量级是几百 KB)。读取前先过 `eval.pool_depth_probe.expand_raw()`。

### 2.3 派生统计 (从上面两份 JSON 重算)

```bash
cd sdtm-rag
.venv/bin/python -c "
import json, statistics
from collections import Counter
from eval.pool_depth_probe import positional_diff, expand_raw
for f in ['evidence/checkpoints/pool_depth_invariance.json','evidence/checkpoints/pool_depth_invariance_all140.json']:
    d=json.load(open(f,encoding='utf-8')); pq=d['per_question']; ids=d['ids']; raw=expand_raw(d['raw'])
    print('==',f.split('/')[-1],'procs',d['n_procs'],'题',len(ids))
    print(' A/B 全同的题:',[q for q in ids if pq[q]['ab_mismatched']==0])
    ad=[pq[q]['algebraic_max_diff'] for q in ids]; abd=[pq[q]['ab_max_diff'] for q in ids]
    print(' algebraic 逐位差 中位/均值/max:',statistics.median(ad),round(statistics.mean(ad),2),max(ad))
    print(' e2e A/B 逐位差 中位/均值/max:',statistics.median(abd),round(statistics.mean(abd),2),max(abd))
    worst=0;wq=None
    for qi,qid in enumerate(ids):
        for slot in (0,1):
            seqs=[p[qi]['e2e'][slot] for p in raw]
            m=max(positional_diff(a,b) for a in seqs for b in seqs)
            if m>worst: worst,wq=m,(qid,['pool30','pool200'][slot])
    unst=[q for q in ids if pq[q]['cross_proc_shallow']['distinct_orders']>1 or pq[q]['cross_proc_deep']['distinct_orders']>1]
    print(' 跨进程不稳题:',len(unst),unst,'最大跨进程逐位差',worst,wq)
    print(' candidate_prefix 不一致题数:',d['candidate_prefix']['n_mismatched_questions'])
    tot=[pq[q]['fuse_candidates'] for q in ids]; med=sorted(tot)[len(tot)//2]
    print(' 深融合候选总数 min/median:',min(tot),med,'-> 15 席之外余量 min/median:',min(tot)-15,med-15)
    if 'q38' in ids:
        qi=ids.index('q38'); comp=set()
        for p in raw:
            s=p[qi]['fuse_out_deep_sections']; c=Counter(s); top=c.most_common(1)[0][1]
            comp.add((len(s),top,len(s)-top))
        print(' q38 (候选总数, 最大簇, 非该簇) 跨进程取值:',sorted(comp))
        print(' q38 席位 配额2/3/5:',[pq['q38']['seats_by_quota'][k] for k in ('2','3','5')])
"
```

```
== pool_depth_invariance.json procs 12 题 11
 A/B 全同的题: ['q29']
 algebraic 逐位差 中位/均值/max: 11 9.27 14
 e2e A/B 逐位差 中位/均值/max: 12 10.18 14
 跨进程不稳题: 1 ['q38'] 最大跨进程逐位差 7 ('q38', 'pool30')
 candidate_prefix 不一致题数: 8
 深融合候选总数 min/median: 38 58 -> 15 席之外余量 min/median: 23 43
 q38 (候选总数, 最大簇, 非该簇) 跨进程取值: [(43, 41, 2), (44, 42, 2)]
 q38 席位 配额2/3/5: [4, 5, 7]
== pool_depth_invariance_all140.json procs 8 题 140
 A/B 全同的题: ['q04', 'q24', 'q25', 'q27', 'q06', 'q28', 'q29', 'q18', 'q74', 'q87', 'q113', 'q116', 'q119', 'q124']
 algebraic 逐位差 中位/均值/max: 7.0 7.11 14
 e2e A/B 逐位差 中位/均值/max: 6.0 6.16 14
 跨进程不稳题: 6 ['q05', 'q38', 'q80', 'q111', 'q120', 'q139'] 最大跨进程逐位差 9 ('q120', 'pool30')
 candidate_prefix 不一致题数: 58
 深融合候选总数 min/median: 37 51 -> 15 席之外余量 min/median: 22 36
 q38 (候选总数, 最大簇, 非该簇) 跨进程取值: [(43, 41, 2), (44, 42, 2)]
 q38 席位 配额2/3/5: [4, 5, 7]
```

(上面这段的 `candidate_prefix 不一致题数` 与 `跨进程不稳题` 两行**会随重跑变动** ——
见 §4 第 3 条。q38 的候选构成也在 `(43,41,2)` 与 `(44,42,2)` 之间摆动, 但**非该簇候选
恒为 2 条、席位恒为 4/5/7** —— 结论不受这点抖动影响。其余各行每次重跑一致。)

### 2.4 q38 为什么补不满席位 (独立复核, 不读上面的 JSON)

```bash
cd sdtm-rag
.venv/bin/python -c "
from collections import Counter
from eval.jitter_probe import _engine
from eval.run_eval import load_test_set
from eval.pool_depth_probe import seats_under_quota
qs={q['id']:q for q in load_test_set('eval/test_set_v3.yml')}
rag=_engine('hybrid',15); q=qs['q38']['question']; v=rag._embed_query(q)
d=rag._search(q,30,None,query_embedding=v); b=rag._bm25_search(q,30,None)
fused=rag._hybrid_fuse(d,b,60)
c=Counter(ch.section for ch in fused); sec=[ch.section for ch in fused]
print('[随抖动摆动] 候选总数', len(fused), '最大簇', c.most_common(1)[0])
print('[稳定] 其余 section:', [x for x in c.most_common() if x[1]<10])
print('[稳定] 最大簇之外的候选条数:', len(fused)-c.most_common(1)[0][1])
print('[稳定] 席位上限 配额2/3/5/13:', [seats_under_quota(sec,n,15) for n in (2,3,5,13)])
"
```

```
[随抖动摆动] 候选总数 43 最大簇 ('DOMAIN', 41)
[稳定] 其余 section: [('4.1.6 Additional Guidance on Dataset Naming', 1), ('4.2.2 Two-character Domain Identifier', 1)]
[稳定] 最大簇之外的候选条数: 2
[稳定] 席位上限 配额2/3/5/13: [4, 5, 7, 15]
```

这条命令**不读跑批产出的 JSON**, 直接现场检索再算 —— 与 §2.1/§2.2 的
`seat_feasibility` 臂互为独立核验。

第一行标 `[随抖动摆动]`: q38 正是跨进程不稳的题之一, 实测在 `(43, 41)` 与 `(44, 42)`
之间摆动, 重跑拿到哪个都正常。**结论不依赖它** —— 后三行每次都一样, 而定案靠的正是
「最大簇之外只有 2 条」与「配额 2/3/5 → 只能凑 4/5/7 席」。

---

## 3. 判读

**抖动本底 = 0, 池深效应 = 满格。** 两次跑批合计 **2504 组 A/A 对全部逐位相同,
最大逐位差 0**; 而 A/B 对 **4512/5008 (90%) 不一致, 最大逐位差 14/15**。A/A 与 A/B
在同一进程、同一引擎对象、同一份钉死向量下测得, 中间**只差 `hybrid_pool` 这一个赋值**。
抖动无法解释这个差异。

**`algebraic` 臂把这条结论钉成不可辩驳的。** 它两侧的输入是**同一个 python 列表的两个
切片**, `_hybrid_fuse` 是纯函数 —— 这条臂里抖动在物理上不存在。它仍然报出
**130/140 题 top-15 变了, 逐位差中位数 7/15**。

**机制** (brief 猜的那条路径, 实测坐实):

```bash
cd sdtm-rag
.venv/bin/python -c "
from eval.jitter_probe import _engine
from eval.run_eval import load_test_set
qs={q['id']:q for q in load_test_set('eval/test_set_v3.yml')}
rag=_engine('hybrid',15); q=qs['q104']['question']; v=rag._embed_query(q)
dense=rag._search(q,200,None,query_embedding=v); bm=rag._bm25_search(q,200,None)
dr={c.chunk_id:i for i,c in enumerate(dense)}; br={c.chunk_id:i for i,c in enumerate(bm)}
def rrf(P):
    s={}
    for lst in (dense[:P],bm[:P]):
        for r,c in enumerate(lst): s[c.chunk_id]=s.get(c.chunk_id,0.0)+1.0/(60+r+1)
    return s
s30,s200=rrf(30),rrf(200)
t30=[c.chunk_id for c in rag._hybrid_fuse(dense[:30],bm[:30],15)]
t200=[c.chunk_id for c in rag._hybrid_fuse(dense[:200],bm[:200],15)]
print('进入者:')
for cid in t200:
    if cid not in t30:
        print(f'  {cid:<45} dense_rank={dr.get(cid)} bm25_rank={br.get(cid)} score30={s30.get(cid,0):.5f} score200={s200[cid]:.5f}')
print('被挤出者:')
for cid in t30:
    if cid not in t200:
        print(f'  {cid:<45} dense_rank={dr.get(cid)} bm25_rank={br.get(cid)} score30={s30.get(cid,0):.5f} score200={s200.get(cid,0):.5f}')
"
```

```
进入者:
  domains/PE/spec.md#24                         dense_rank=7 bm25_rank=32 score30=0.01471 score200=0.02546
  domains/QS/spec.md#22                         dense_rank=6 bm25_rank=38 score30=0.01493 score200=0.02503
  domains/CV/spec.md#31                         dense_rank=12 bm25_rank=30 score30=0.01370 score200=0.02469
  domains/NV/spec.md#31                         dense_rank=14 bm25_rank=31 score30=0.01333 score200=0.02420
被挤出者:
  domains/DA/spec.md#21                         dense_rank=17 bm25_rank=29 score30=0.02393 score200=0.02393
  terminology/questionnaires/questionnaires_part42.md#8 dense_rank=None bm25_rank=1 score30=0.01613 score200=0.01613
  terminology/questionnaires/questionnaires_part42.md#2 dense_rank=None bm25_rank=2 score30=0.01587 score200=0.01587
  terminology/questionnaires/questionnaires_part43.md#0 dense_rank=None bm25_rank=3 score30=0.01562 score200=0.01562
```

正是 brief 预判的路径: dense 第 6-14 名、bm25 第 30-38 名的 chunk, 在 pool=30 时只拿到
dense 一项分 (~0.0147), 池加深到 200 后 bm25 那一项进账, 分数翻倍到 ~0.0255, 于是把
**bm25 第 1-3 名但完全不在 dense 池里**的条目 (~0.0161) 挤出 top-15。RRF 的加性结构
决定了「加深池 = 给跨通道重合项加分」, 这**不是**只在尾部加低分项。

**`candidate_prefix` 臂的额外发现: BM25 候选列表本身依赖请求深度, 原因是分数并列。**

```bash
cd sdtm-rag
.venv/bin/python -c "
from eval.jitter_probe import _engine
from eval.run_eval import load_test_set
qs={q['id']:q for q in load_test_set('eval/test_set_v3.yml')}
rag=_engine('hybrid',15); q=qs['q38']['question']
a=rag._bm25_search(q,30,None); b=rag._bm25_search(q,200,None)
print('a[:5]',[(c.chunk_id,c.similarity) for c in a[:5]])
print('b[:5]',[(c.chunk_id,c.similarity) for c in b[:5]])
print('set(a) == set(b[:30]):', set(c.chunk_id for c in a)==set(c.chunk_id for c in b[:30]))
"
```

```
a[:5] [('chapters/ch04_general_assumptions.md#5', 12.3623), ('domains/SV/spec.md#1', 10.3561), ('domains/IS/spec.md#1', 10.3061), ('domains/MS/spec.md#1', 10.3061), ('domains/TE/spec.md#1', 10.3061)]
b[:5] [('chapters/ch04_general_assumptions.md#5', 12.3623), ('domains/SV/spec.md#1', 10.3561), ('domains/SR/spec.md#1', 10.3061), ('domains/MB/spec.md#1', 10.3061), ('domains/BS/spec.md#1', 10.3061)]
set(a) == set(b[:30]): False
```

一大批域 spec chunk 的 BM25 得分**严格并列** (10.3061), `bm25s` 的 top-k 选择在并列项
之间取谁**随 k 而变** (`_bm25_search` 内 `k = max(n*4, n)`, n=30 取 120, n=200 取 800)。
这是确定性的 (同一 k 每次同样结果), 但意味着「加深池」还额外换掉了浅池本该有的候选 ——
池深度这个变量比预想的还脏。

**`FUSE_OUT_DEEP_OK = true` 是代码结构可证的, 不只是 140/140 的经验。**
读 `server/rag.py` 的 `_hybrid_fuse`: 参数 `k` **只出现在最后一行** `ranked[:k]` ——
`best` 字典的构建、RRF 分数表 `scores`、以及 `ranked = sorted(scores, ...)` 的全排序
都与 `k` 无关; `sorted` 是稳定排序, 并列项的先后由 `scores` 的插入序 (dense 先、
bm25 后) 决定, 同样与 `k` 无关。于是「深融合输出的前 k 名 = 浅融合输出的 k 名」是
函数结构的直接推论。`fuse_output_depth` 臂的 140/140 是对这条推论的**复核**, 不是它
唯一的依据 —— 结构论证比经验耐用 (换题集、换语料都不会翻)。

**但「B 组能补满 15 席」不是结构可证的, 而且实测有反例 (q38)。见 §5。**

---

## 4. 这些证据能证明什么、不能证明什么

**能证明**:

1. 在生产配置 (`hybrid_fusion=rrf`, `hybrid_alpha=0.5`, `structured_lookup_enabled=True`,
   `top_k=15`) 与 `eval/test_set_v3.yml` 这 140 题上, 把 `hybrid_pool` 从 30 改到 200,
   会改变 126/140 题的生产 top-15, 逐位差中位数 6/15、最高 14/15。
2. 该差异**不是**跨进程抖动 —— 同进程同参数的 2504 组对照全部逐位相同, 且零抖动的
   `algebraic` 臂独立复现了同量级的差异。
3. 池深不动、只放长 `_hybrid_fuse` 的输出到 60 时, 140/140 题的生产 top-15 逐位不变
   (且这一条另有代码结构论证支撑, 见 §3)。深融合候选**总数**最小 37 (中位 51),
   即 15 席之外余量最小 22 (中位 36)。
4. 同名 section 配额 2 / 3 / 5 下, **140 题里只有 q38 凑不满 15 席** (分别只能凑
   4 / 5 / 7 席)。其余 139 题在三档配额下都能补满。

**不能证明**:

1. **不能证明 pool=200 更差或更好。** 本 task 只问「变不变」, 没跑任何质量指标
   (source recall / 判分)。「变了」不等于「变坏了」。
2. **不能证明检索结果绝对可复现。** 跨进程抖动确实存在: 全量跑批 6/140 题在 8 个独立
   进程间出现 >1 种 top-15, 最大逐位差 9 (q120)。本 task 的设计是把这个混杂**隔离**在
   进程间, 不是消除它。Task 6 的 A/B 若跨进程执行, 这些题仍会带自身噪声。
   重跑累计观察到的不稳题号: q05 / q38 / q63 / q80 / q111 / q120 / q139
   (单次最多 7 题, 且**是下界** —— 进程越多只会观察到越多)。
3. **不能把 `candidate_prefix` 与「跨进程不稳题数」当稳定数字引用。** 这两项每条题只测
   一次单点调用, 本身会被抖动推动 —— 全量跑批重跑之间, `candidate_prefix` 在 58~59
   之间、跨进程不稳题数在 4~7 之间摆动。稳定可引的是 `algebraic` (130/140)、
   A/A = 0 / A/B = 4032, 以及席位可行性 (q38 = 4/5/7 席) —— 这几项每次重跑都一样。
4. **不能外推到别的融合配置。** 只测了 `rrf`。`weighted` 走 min-max 归一化, 池深度对它的
   影响机制不同 (归一化的分母会随池深变), 未测。
5. **不能外推到别的池深对。** 只测了 30 vs 200。30 vs 40 会小得多, 但仍非零 —— 上面的
   机制表明只要有跨通道重合项落在两个深度之间就会动。

---

## 5. 对 Task 6 的约束 (据此定案)

**A/B 三组统一用生产 `hybrid_pool=30`。** 不许给任一组加深池 —— 加深池会改写 126/140 题
的 top-15, 那个效应比配额本身可能产生的效应还大, 实验会被彻底污染。

**B 组腾席位的正确做法: 放长融合输出, 不动池深。** `_hybrid_fuse(dense, bm25, k)` 里
`k` 只出现在最后一行 `ranked[:k]`, 分数表与全排序都与 `k` 无关 (§3 的结构论证), 所以
把输出的 `k` 从 15 放到 60 只是多留几名, 前 15 名逐位不变。实测复核: 140/140 题前 15 名
零差异, 整条生产链 (含 S1 直查) 零差异。

于是 Task 6 应当:

- **A 组** = 生产原样 (`hybrid_pool=30`, 融合输出 15);
- **B 组** = `hybrid_pool=30` + 融合输出放长到 60, 在这条更长的排序上施加同名 section
  配额, 被挤掉的席位由**同一排序的下一位**补上;
- 两组的候选池、RRF 分数表完全相同, 唯一差异就是配额。

### 5.1 席位: 139/140 题能补满, q38 不能

**「候选总数 37 条、只要 15 席, 余量充裕」这个推理是错的** —— 备选本身绝大多数就是那个
超配额簇的成员。补位余量必须**按 section 数算, 不能按条数算**。

q38 实测: 深融合候选共 43~44 条 (跨进程摆动), 其中 **§DOMAIN 占 41~42 条, 非该簇只有
2 条**。于是席位上限 = `min(簇内配额, 42) + 2`:

| 配额 | 凑不满 15 席的题 (共 140 题) | q38 实际能凑到 |
|---|---|---|
| 2 | **1 题 (仅 q38)** | **4 席** |
| 3 | **1 题 (仅 q38)** | **5 席** |
| 5 | **1 题 (仅 q38)** | **7 席** |

三档配额一致: 140 题里**只有 q38** 补不满 —— 而它正是层② 最需要做 A/B 的那道题
(`max_cluster=14`, 全题集最高)。

**加大融合输出救不了 q38。** pool=30 时 dense/bm25 候选并集上限 60, q38 实际只有 43~44
条、其中 41~42 条同簇; 无论输出 `k` 放多大, 非 §DOMAIN 候选就只有 2 条。要补满只剩两条
路: **加深池** (本 task 已判 `POOL_DEEP_OK = false`, 明令禁止) 或**把配额放到 ≥13**
(对 `max_cluster=14` 的簇等于没有配额)。两条都不可取。

顺带记一句量纲: 余量上限受 `pool=30` 硬约束 —— 并集 ≤ 60, 故 15 席之外余量 ≤ 45。
**这正是 q38 无解的根本原因**: 池深锁死了候选总量, 而这批候选的 section 又高度同质。

### 5.2 结论

- **139/140 题**: B 组按上面的方式补满 15 席, 与 A 组唯一差异是配额, 实验干净,
  **没有 context 长度这个混杂因素**。brief 的 fallback 对这 139 题可以不用。
- **q38**: **必须保留 brief 的 fallback** —— 允许不足 15 席, 并声明「B 组 context 比
  A 组短, 这是配额的真实效果, 但也意味着该题的 A/B 差异含 context 长度这一混杂因素」。
  Task 6 报告里**单列**这一题, 不并入主结论。

**建议做成硬 gate 而不是自陈**: Task 6 逐题记录 B 组实际席位数, **席位数 < 15 的题一律
走 fallback 口径, 不许混进主结论**。判据可直接复用本探针的
`eval.pool_depth_probe.seats_under_quota(sections, quota, k)` —— 它是纯函数, 给定候选的
section 列表就能在跑 A/B 之前算出哪些题会不足席, 不必等结果出来再补救。
