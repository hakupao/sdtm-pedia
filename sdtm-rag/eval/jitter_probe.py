"""top-k 抖动量化: 同 query 同参数重复检索, 看 top-15 的**成分**与**顺序**稳不稳。

为什么要有这个探针: 层① 的挤占数字 (`max_cluster` / `dup_seats`) 全部出自**单次**
top-15。若重复检索会换成分, 那些数字就不是稳定事实, 引用前必须先量化抖动。

条目标识一律用 **`chunk_id`**。用 `文件名#section` 会塌缩 —— 63 个域的文件名都是
`spec.md`、section 都是 `DOMAIN`, 14 条会缩成 1 个 key, 探针于是"证明"了稳定性。
`stability_report` 自带护栏: 全部标识去重后 <=1 种就抛 ValueError, 不让这种探针
静默地假装稳定。

跑批 (从 sdtm-rag/ 起):
  .venv/bin/python -m eval.jitter_probe --runs 12 --config both \\
    --output evidence/checkpoints/topk_jitter.json
"""
from __future__ import annotations

import argparse
import json
import math
import random
import time
from collections.abc import Sequence

# 层① (crowding) 里 max_cluster >= 5 的 11 题, 含挤占最重的 q38 (max_cluster=14)。
# 抖动只在同质簇尾部才有翻转空间, 所以量化就打这批最可能翻的题 —— 它们不抖, 挤占
# 更轻的题更不会抖; 它们抖, 层① 全表都要重算。
DEFAULT_IDS = [
    "q38", "q104", "q39", "q08", "q29", "q81", "q77", "q108", "q07", "q84", "q118",
]

DEFAULT_TEST_SET = "eval/test_set_v3.yml"


def stability_report(runs: Sequence[Sequence[str]]) -> dict:
    """多次运行的条目标识序列 -> 稳定性统计。

    - `distinct_sets`   成分 (集合) 有几种 —— >1 表示**集合统计不可复现**
    - `distinct_orders` 顺序有几种 —— >1 表示排位不可复现 (集合可能仍稳)
    - `stable_prefix`   从头起逐位完全一致的长度
    - `always`          每次都在的条目数
    - `sometimes`       出现过但非每次都在的条目数 (>0 即成分抖)
    """
    if not runs:
        raise ValueError("stability_report needs at least one run")
    ever: set[str] = set().union(*(set(r) for r in runs))
    if len(ever) <= 1:
        raise ValueError(
            f"indistinguishable identifiers: 全部 {sum(len(r) for r in runs)} 个条目"
            f"去重后只剩 {len(ever)} 种 ({sorted(ever)}) — 标识选错了 (要 chunk_id, "
            "不是文件名/section), 这样的探针只会假装稳定"
        )
    always = set.intersection(*(set(r) for r in runs))

    stable_prefix = 0
    for i in range(max(len(r) for r in runs)):
        col = {r[i] if i < len(r) else None for r in runs}
        if len(col) != 1:
            break
        stable_prefix = i + 1

    return {
        "n_runs": len(runs),
        "distinct_sets": len({frozenset(r) for r in runs}),
        "distinct_orders": len({tuple(r) for r in runs}),
        "stable_prefix": stable_prefix,
        "always": len(always),
        "sometimes": len(ever - always),
    }


def min_adjacent_gap(sims: Sequence[float]) -> float | None:
    """top-k 内相邻 similarity 的最小间隔。间隔比 embedding 抖动量还小的地方,
    浮点抖动就足以翻转顺序 —— 这是"为什么会抖"的量纲证据。"""
    if len(sims) < 2:
        return None
    return min(abs(a - b) for a, b in zip(sims, sims[1:], strict=False))


def dense_sims(rag, embedding: Sequence[float], top_k: int) -> tuple[list[str], dict]:
    """给定 query 向量, 拿纯 cosine 的 top-k 顺序与**全精度** similarity。

    为什么不复用 retrieve() 的 similarity: `RetrievedChunk.similarity` 建对象时就
    `round(..., 4)` 了, 同质簇里一堆条目会并列成 0.0 间隔 —— 那是显示精度产物,
    不是真实间隔, 没法和 1e-4 量级的抖动比大小。这里直接吃 Chroma 的 raw distance。
    走裸 collection.query, 不含 S1 注入与 BM25 融合: 这条通道的排序**就是**按 cosine,
    也正是 embedding 抖动唯一能直接翻的地方。"""
    res = rag.collection.query(
        query_embeddings=[list(embedding)], n_results=top_k, include=["distances"]
    )
    ids = list(res["ids"][0])
    sims = [1.0 - d for d in res["distances"][0]]
    return ids, dict(zip(ids, sims, strict=True))


def pair_margins(orders: Sequence[Sequence[str]], sims: Sequence[dict]) -> dict:
    """相邻对的**翻转余量**: 同一 query 的多个抖动向量下, 每个相邻对的 sim 差还剩多少。

    为什么要这个而不是只看"12 次有没有翻": 没翻可能是运气。余量把结论从"这 12 次
    没观察到"抬成"在实测到的抖动幅度下, 这对相差还有 X"。

    对每个基准相邻对 (a, b) (按第 1 次运行的顺序), 在每次运行里算 `sim(a)-sim(b)`:
      - `min_diff < 0`  该对在某次运行里**真翻了**
      - `drift`         该差值在多次运行间的波动幅度 (抖动的**微分**效应)

    关键对照量: 单条 sim 的绝对漂移 (`max_abs_sim_drift`) 通常远大于 `drift` ——
    query 向量整体平移会把同簇文档的 sim **同向**推动, 差值因此比单值稳得多。
    只看绝对漂移 > 间隔就断言"必翻", 会高估风险。
    """
    common = set.intersection(*(set(o) for o in orders))
    base = list(orders[0])
    pairs = []
    for a, b in zip(base, base[1:], strict=False):
        if a not in common or b not in common:
            continue
        diffs = [m[a] - m[b] for m in sims]
        pairs.append({
            "pair": [a, b],
            "gap": diffs[0],
            "min_diff": min(diffs),
            "drift": max(diffs) - min(diffs),
            "flipped": min(diffs) < 0,
        })
    drifts = [
        max(m[i] for m in sims) - min(m[i] for m in sims)
        for i in common
    ]
    return {
        "n_pairs": len(pairs),
        "n_common_members": len(common),
        # 严格并列 (gap == 0.0) 的对, `min_diff < 0` 永远判不出翻转 —— 差值恒为 0。
        # 这类对的先后本就是任意的, 故顺序种类数要独立记一份, 别只信 flipped。
        "distinct_orders": len({tuple(o) for o in orders}),
        "n_flipped_pairs": sum(1 for p in pairs if p["flipped"]),
        "min_margin": min((p["min_diff"] for p in pairs), default=None),
        "max_pair_diff_drift": max((p["drift"] for p in pairs), default=None),
        "max_abs_sim_drift": max(drifts, default=None),
        "tied_pairs": sum(1 for p in pairs if p["gap"] == 0.0),
        "pairs": pairs,
    }


def perturbed_vectors(
    vec: Sequence[float], l2: float, n: int, seed: int = 20260807
) -> list[list[float]]:
    """把抖动当**自变量**: 返回 n 个与 `vec` 相距恰好 `l2` 的向量 (随机方向)。

    为什么需要它 —— 采样验稳会系统性低估抖动。实测 embedding API 在一个时间窗里
    只返回**一小组离散向量** (350 秒内只见 2-3 种, 且重复出现), 所以"连跑 N 次"
    拿到的往往是同一个向量, N 次 ≠ N 个独立样本; 而向量真正换一批要等几十分钟到几小时。
    与其等它发生, 不如直接按实测幅度施加扰动, 一次把稳定性问到底 (且零 API 开销)。

    ⚠️ 随机方向**不是**真实抖动的分布 (真实抖动是量化式的、有结构的: 沿真实差值方向
    放大 5 倍都翻不动, 而同样长度的随机方向有约 10% 概率翻)。所以这里得到的频率是
    **敏感度上界**, 不是"每次调用的翻转概率"。它回答的是"这个统计量在这个幅度下稳不稳",
    不回答"多久会发生一次"。
    """
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        g = [rng.gauss(0, 1) for _ in range(len(vec))]
        norm = math.sqrt(sum(x * x for x in g))
        out.append([a + l2 * x / norm for a, x in zip(vec, g, strict=True)])
    return out


def retrieve_under_perturbation(rag, question: str, vectors, top_k: int) -> list[list]:
    """对每个给定的 query 向量跑一次生产检索, 返回各次的 chunk 列表。

    只替换 embedding 这一步 (`retrieve()` 每次调用只 embed 一次, 见 server/rag.py),
    BM25 侧对同一 query 文本本就是确定性的, 因此这里控制的正是唯一的抖动源。

    **不在这里算任何挤占统计** —— 统计口径归 Task 4 的 `crowding_stats` 独有,
    本模块不做第二份实现 (硬规矩: 判据不许有两个来源)。调用方自己往结果上套。
    """
    real = rag._embed_query
    out = []
    try:
        for v in vectors:
            rag._embed_query = lambda _t, _v=v: list(_v)
            out.append(rag.retrieve(question, top_k=top_k))
    finally:
        rag._embed_query = real
    return out


def embedding_jitter(vectors: Sequence[Sequence[float]]) -> dict:
    """重复 embed 同一 query 的向量 -> 逐位最大差值与 L2 距离 (均相对第 1 次)。

    这一项证明的是**抖动源**: BM25 给定相同 token 是确定性的, 只有 embedding 走
    远程 API。向量不逐位相同 = 抖动进了 dense 通道。"""
    base = vectors[0]
    max_abs = 0.0
    max_l2 = 0.0
    for v in vectors[1:]:
        max_abs = max(max_abs, max(abs(a - b) for a, b in zip(base, v, strict=True)))
        max_l2 = max(max_l2, math.sqrt(sum((a - b) ** 2 for a, b in zip(base, v, strict=True))))
    return {
        "n_calls": len(vectors),
        "dim": len(base),
        "identical": len({tuple(v) for v in vectors}) == 1,
        "max_abs_elementwise_diff": max_abs,
        "max_l2_distance": max_l2,
    }


# ---- 跑批 -------------------------------------------------------------------


def _engine(config: str, top_k: int):
    from server.config import settings
    from server.rag import RAGEngine

    kw: dict = {}
    if config == "hybrid":  # 生产口径: hybrid BM25 融合 + S1 直查
        kw = dict(
            structured_lookup_enabled=True, hybrid_enabled=True,
            hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
            hybrid_pool=settings.hybrid_pool,
        )
    return RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model, top_k=top_k, **kw,
    )


def probe_question(question: str, config: str, n_runs: int, top_k: int) -> dict:
    """同 query 同参数跑 n_runs 次, 每次**新建引擎**并重新 embed (模拟真实调用)。"""
    runs: list[list[str]] = []
    gaps: list[float] = []
    sims_first: list[float] = []
    for i in range(n_runs):
        rag = _engine(config, top_k)
        chunks = rag.retrieve(question, top_k=top_k)
        runs.append([c.chunk_id for c in chunks])
        sims = [c.similarity for c in chunks]
        g = min_adjacent_gap(sims)
        if g is not None:
            gaps.append(g)
        if i == 0:
            sims_first = sims
    rep = stability_report(runs)
    ever: set[str] = set().union(*(set(r) for r in runs))
    always = set.intersection(*(set(r) for r in runs))
    rep.update({
        "min_adjacent_gap": min(gaps) if gaps else None,
        "sim_first_run": sims_first,
        "unstable_members": sorted(ever - always),
        "runs": runs,
    })
    return rep


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="top-k 抖动量化探针")
    p.add_argument("--runs", type=int, default=12)
    p.add_argument("--config", choices=["hybrid", "dense", "both"], default="both")
    p.add_argument("--top-k", type=int, default=15)
    p.add_argument("--test-set", default=DEFAULT_TEST_SET)
    p.add_argument(
        "--ids", default=None,
        help="逗号分隔题号; 缺省用层① max_cluster>=5 的 11 题 (含 q38)",
    )
    p.add_argument("--output", required=True)
    args = p.parse_args(argv)

    import yaml

    with open(args.test_set, encoding="utf-8") as f:
        all_qs = yaml.safe_load(f)
    wanted = [s.strip() for s in args.ids.split(",")] if args.ids else DEFAULT_IDS
    by_id = {q["id"]: q for q in all_qs}
    missing = [i for i in wanted if i not in by_id]
    if missing:
        raise SystemExit(f"题号不在 {args.test_set}: {missing}")
    qs = [by_id[i] for i in wanted]

    configs = ["hybrid", "dense"] if args.config == "both" else [args.config]
    out: dict = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "n_runs": args.runs, "top_k": args.top_k, "test_set": args.test_set,
        "ids": wanted, "configs": {},
    }

    # 抖动源: 同一 query 重复 embed, 看向量是否逐位相同 (dense 引擎即可, 不含 BM25)。
    # 同一批向量复用两处: 量抖动幅度, 与量这点幅度在 cosine 排序上还剩多少余量。
    emb_engine = _engine("dense", args.top_k)
    from server.config import settings as _s

    pool = _s.hybrid_pool  # 生产 hybrid 的融合池深度: 成分能不能变, 就看这条线
    out["hybrid_pool"] = pool
    out["embedding_jitter"], out["raw_dense_gap"], out["dense_margin"] = {}, {}, {}
    out["pool_boundary"] = {}
    for q in qs:
        vecs = [emb_engine._embed_query(q["question"]) for _ in range(args.runs)]
        ej = embedding_jitter(vecs)
        pulls = [dense_sims(emb_engine, v, args.top_k) for v in vecs]
        gap = min_adjacent_gap([pulls[0][1][i] for i in pulls[0][0]])
        margin = pair_margins([o for o, _ in pulls], [m for _, m in pulls])
        # 池边界: hybrid 的 top-15 成分只可能因**进池名单**变化而变 (池内重排会被 RRF
        # 重新打分, 但池外的条目根本没机会参与)。所以真正要盯的是第 pool 与第 pool+1
        # 名之间那道线 —— 抖动把它俩换个位, 融合的输入就变了。
        bpulls = [dense_sims(emb_engine, v, pool + 1) for v in vecs]
        b_ids0, b_sims0 = bpulls[0]
        b_margin = pair_margins([o for o, _ in bpulls], [m for _, m in bpulls])
        out["pool_boundary"][q["id"]] = {
            "pool": pool,
            "set_stability": stability_report([o[:pool] for o, _ in bpulls]),
            "boundary_gap": b_sims0[b_ids0[pool - 1]] - b_sims0[b_ids0[pool]],
            "min_margin": b_margin["min_margin"],
            "n_flipped_pairs": b_margin["n_flipped_pairs"],
            "distinct_orders": b_margin["distinct_orders"],
        }
        out["embedding_jitter"][q["id"]] = ej
        out["raw_dense_gap"][q["id"]] = {"min_gap": gap}
        out["dense_margin"][q["id"]] = margin
        pb = out["pool_boundary"][q["id"]]
        print(f"[pool{pool}] {q['id']} set_distinct={pb['set_stability']['distinct_sets']} "
              f"boundary_gap={pb['boundary_gap']:.3e} flipped={pb['n_flipped_pairs']}",
              flush=True)
        print(f"[emb] {q['id']} identical={ej['identical']} "
              f"max|Δ|={ej['max_abs_elementwise_diff']:.3e} L2={ej['max_l2_distance']:.3e} "
              f"raw_min_gap={gap:.3e} tied={margin['tied_pairs']} "
              f"flipped_pairs={margin['n_flipped_pairs']} "
              f"sim_drift={margin['max_abs_sim_drift']:.3e} "
              f"pair_drift={margin['max_pair_diff_drift']:.3e}", flush=True)

    for cfg in configs:
        rows = {}
        for i, q in enumerate(qs, 1):
            r = probe_question(q["question"], cfg, args.runs, args.top_k)
            rows[q["id"]] = r
            print(f"[{cfg} {i}/{len(qs)}] {q['id']} sets={r['distinct_sets']} "
                  f"orders={r['distinct_orders']} prefix={r['stable_prefix']} "
                  f"sometimes={r['sometimes']} min_gap={r['min_adjacent_gap']}",
                  flush=True)
        out["configs"][cfg] = rows

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    print("\n===== 汇总 =====")
    for cfg, rows in out["configs"].items():
        n_set = sum(1 for r in rows.values() if r["distinct_sets"] > 1)
        n_ord = sum(1 for r in rows.values() if r["distinct_orders"] > 1)
        print(f"  {cfg:<7} 成分抖 {n_set}/{len(rows)} 题, 顺序抖 {n_ord}/{len(rows)} 题")
    n_emb = sum(1 for e in out["embedding_jitter"].values() if not e["identical"])
    print(f"  embedding 重复调用不逐位相同: {n_emb}/{len(qs)} 题")
    n_flip = sum(1 for m in out["dense_margin"].values() if m["n_flipped_pairs"])
    print(f"  纯 cosine 相邻对真被抖动翻转: {n_flip}/{len(qs)} 题")
    print(f"  明细: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
