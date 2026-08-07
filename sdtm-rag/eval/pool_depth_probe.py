"""池深度不变性: 加深 `hybrid_pool` 会不会改变生产 top-15?

**为什么不能只"跑一次浅池、跑一次深池、比一比"**: 检索结果**跨进程不稳定**
(Task 3B 实测: 钉死 query 向量后, 8 个独立进程跑同一条 query 仍会换尾部;
Chroma 的 HNSW 在向量完全相同的重复 chunk 之间返回谁不由 sim 决定)。
所以"浅池一次 vs 深池一次"比出来的差异, 无法区分是**池深度**造成的还是**抖动**造成的。

本探针用**同进程配对 + A/A 空白对照**把这两者分开, 共三条臂:

- `algebraic`  同一份 dense@200 / bm25@200 候选列表, 分别截到 30 与 200 再走
  `_hybrid_fuse`。两侧输入**逐位相同**, 抖动在此臂里不存在 —— 它单独量
  "给定同一批候选, 融合池截断深度本身"的效应。
  **不能**回答: Chroma / BM25 在 n=30 与 n=200 两次调用下候选列表是否前缀一致。
- `candidate_prefix`  正是上面那个前提: `_search(q, 30)` 是否等于 `_search(q, 200)[:30]`,
  BM25 同理。这一臂把"候选列表本身依赖于请求深度"这条路径单独暴露出来。
- `fuse_output_depth`  **池深不动**, 只把 `_hybrid_fuse` 的**输出**截断 k 从 15 放到 60。
  RRF 分数只由候选在两份列表里的 rank 决定 —— 池不变则分数表不变, 放长输出只是
  多留几名, 前 15 名必然逐位不变。这一臂用实测把"必然"钉死, 并顺带量出
  **补位余量** (融合后还剩多少条可用)。Task 6 的 B 组要"腾席位再补满 15",
  需要的是**更深的融合输出**, 不是更深的池 —— 这两件事常被混为一谈。
- `e2e`  生产整条链 (hybrid 融合 + S1 直查) 在同一进程内交替跑
  `[30, 200, 30, 200]`, **同一个引擎对象、同一份钉死的 query 向量**, 只改
  `hybrid_pool`。于是:
    * A/A 对 `(0,2)` `(1,3)` —— 两次参数**完全相同**的调用, 是这个进程里的**抖动本底**;
    * A/B 对 `(0,1)` `(2,3)` `(1,2)` `(0,3)` —— 只差 `hybrid_pool` 这一个变量。
  判据: **A/B 的不一致必须超过 A/A 的不一致**, 才能归因给池深度。
  A/A 全同而 A/B 有差 = 池深度真有效应; 两者同样有差 = 那是抖动, 不是池深度。

跨进程再跑 N 份, 用来量抖动在**跨进程**这一维的幅度 (进程内取样会系统性低估它)。

跑批 (从 sdtm-rag/ 起):
  .venv/bin/python -m eval.pool_depth_probe --procs 12 \\
    --output evidence/checkpoints/pool_depth_invariance.json
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from collections.abc import Sequence
from pathlib import Path

# 层① (crowding) 里 max_cluster >= 5 的 11 题 + q38。同质簇越深, top-15 尾部离
# 池边界越近, 加深池最可能在这里翻出东西 —— 它们不动, 挤占更轻的题更不会动。
DEFAULT_IDS = [
    "q38", "q104", "q39", "q08", "q29", "q81", "q77", "q108", "q07", "q84", "q118",
]

DEFAULT_TEST_SET = "eval/test_set_v3.yml"
SHALLOW = 30   # 生产 hybrid_pool
DEEP = 200     # 候选深池
# 进程内调用序列: 交替是为了让 A/A 对 (同参数) 与 A/B 对 (只差池深) 都存在,
# 且 A/A 对跨越的调用间隔 (2) 不小于 A/B 对 (1) —— A/A 全同就不能拿"进程内随时间漂移"
# 解释 A/B 的差异。
SEQ = [SHALLOW, DEEP, SHALLOW, DEEP]
AA_PAIRS = [(0, 2), (1, 3)]
AB_PAIRS = [(0, 1), (2, 3), (1, 2), (0, 3)]
# 融合**输出**放长到这个深度 (池仍是 SHALLOW): B 组腾出席位后的补位来源。
FUSE_OUT = 60


def positional_diff(a: Sequence[str], b: Sequence[str]) -> int:
    """逐位不同的位置数 (长度不等时, 缺位算作不同)。

    "逐位相同"是本 task 的判据 —— 集合相同但顺序不同, 对下游 context 拼装
    仍是不同的输入, 不能算不变。
    """
    n = max(len(a), len(b))
    pa = list(a) + [None] * (n - len(a))
    pb = list(b) + [None] * (n - len(b))
    return sum(1 for x, y in zip(pa, pb, strict=True) if x != y)


def pair_stats(seqs: Sequence[Sequence[str]], pairs: Sequence[tuple[int, int]]) -> dict:
    """给定一个进程内的调用序列, 统计指定配对的不一致情况。"""
    diffs = [positional_diff(seqs[i], seqs[j]) for i, j in pairs]
    return {
        "n_pairs": len(diffs),
        "n_mismatched": sum(1 for d in diffs if d),
        "max_positional_diff": max(diffs) if diffs else 0,
        "diffs": diffs,
    }


def cross_process_stability(runs: Sequence[Sequence[str]]) -> dict:
    """同一参数下 N 个独立进程的结果有几种 —— 这是抖动的**跨进程**幅度。"""
    if not runs:
        raise ValueError("cross_process_stability needs at least one run")
    ever: set[str] = set().union(*(set(r) for r in runs))
    if len(ever) <= 1:
        raise ValueError(
            f"indistinguishable identifiers: 去重后只剩 {len(ever)} 种 — 标识选错了 "
            "(要 chunk_id), 这样的探针只会假装稳定"
        )
    always = set.intersection(*(set(r) for r in runs))
    return {
        "n_runs": len(runs),
        "distinct_orders": len({tuple(r) for r in runs}),
        "distinct_sets": len({frozenset(r) for r in runs}),
        "sometimes": len(ever - always),
    }


def compact_raw(proc_results: Sequence[Sequence[dict]]) -> list[list[dict]]:
    """存盘用: 与 0 号进程**逐字节相同**的行折成一个标记, 差异行原样保留。

    为什么: N 个进程的意义正是"它们应当相同", 于是绝大多数行是重复的 —— 全量
    140 题 × 8 进程原样存盘 12 MB, 而本仓 evidence JSON 的量级是几百 KB。
    折叠只压掉"相同"这个已被聚合统计断言过的事实, **差异行一条不删** —— 需要人肉
    核对的恰恰是它们。用 `expand_raw()` 还原后可复算全部派生统计。
    """
    if not proc_results:
        return []
    base = {r["id"]: r for r in proc_results[0]}
    out = [list(proc_results[0])]
    for proc in proc_results[1:]:
        out.append([
            {"id": r["id"], "same_as_proc0": True} if r == base[r["id"]] else r
            for r in proc
        ])
    return out


def expand_raw(raw: Sequence[Sequence[dict]]) -> list[list[dict]]:
    """`compact_raw` 的逆运算。"""
    base = {r["id"]: r for r in raw[0]}
    return [[base[r["id"]] if r.get("same_as_proc0") else r for r in proc]
            for proc in raw]


def verdict(agg: dict) -> dict:
    """由三条臂的聚合结果给出 POOL_DEEP_OK。

    真值条件 (全部满足):
      1. `algebraic` 臂零差异 —— 同一批候选下, 截 30 与截 200 的 top-15 逐位相同;
      2. `candidate_prefix` 臂零差异 —— 深池请求的前 30 名与浅池请求逐位相同;
      3. `e2e` 臂的 A/B 不一致数 **不超过** A/A 不一致数 —— 池深度没有带来
         超出抖动本底的额外变化。

    第 3 条刻意写成"不超过 A/A"而不是"为零": 抖动本底若非零, 要求 A/B 为零既
    不可能也没意义 —— 那样连"A 组自己和自己比"都过不了。POOL_DEEP_OK 断言的是
    **池深度不引入超出既有抖动的变化**, 不是"检索结果绝对可复现"。
    """
    alg_ok = agg["algebraic"]["n_mismatched_questions"] == 0
    cand_ok = agg["candidate_prefix"]["n_mismatched_questions"] == 0
    aa = agg["e2e"]["aa"]["n_mismatched"]
    ab = agg["e2e"]["ab"]["n_mismatched"]
    e2e_ok = ab <= aa
    return {
        "POOL_DEEP_OK": bool(alg_ok and cand_ok and e2e_ok),
        "algebraic_ok": alg_ok,
        "candidate_prefix_ok": cand_ok,
        "e2e_ok": e2e_ok,
        "e2e_aa_mismatched": aa,
        "e2e_ab_mismatched": ab,
        # 独立于 POOL_DEEP_OK 的第二个结论: 池深不动、只放长融合输出, 是否无损。
        # POOL_DEEP_OK=false 时 Task 6 靠的就是它。
        "FUSE_OUT_DEEP_OK": agg["fuse_output_depth"]["n_mismatched_questions"] == 0
        and agg["fuse_output_depth"]["e2e_n_mismatched_questions"] == 0,
    }


# ---- 子进程 -----------------------------------------------------------------


def _worker(payload: dict) -> list[dict]:
    """一个独立进程: 建 **一个** 引擎, 对每题钉死 query 向量, 跑三条臂。

    三条臂共用同一个引擎对象与同一份向量 —— 池深度是这中间**唯一**变动的量。
    """
    from server.config import settings
    from server.rag import RAGEngine

    top_k = payload["top_k"]
    rag = RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model, top_k=top_k,
        structured_lookup_enabled=True, hybrid_enabled=True,
        hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=SHALLOW,
    )
    real_embed = rag._embed_query
    out = []
    for item in payload["items"]:
        q, vec = item["question"], item["vector"]
        rag._embed_query = (lambda _t, _v=vec: list(_v)) if vec else real_embed

        # 臂 e2e: 只改 hybrid_pool, 其余一切不动
        seq = []
        for pool in SEQ:
            rag.hybrid_pool = pool
            seq.append([c.chunk_id for c in rag.retrieve(q, top_k=top_k)])
        rag.hybrid_pool = SHALLOW

        # 臂 e2e_deep_fuse: 池仍是 SHALLOW, 只让融合**多吐几名** (Task 6 的 B 组管线,
        # 去掉配额本身)。S1 直查仍按 k 填满, 故若这一臂与 e2e[0] 逐位相同, 就证明
        # "给 B 组一个补位储备"不需要动池深, 也就不引入池深这个混杂变量。
        real_fuse = rag._hybrid_fuse
        rag._hybrid_fuse = lambda d, b, _k, _f=real_fuse: _f(d, b, FUSE_OUT)
        deep_fuse_e2e = [c.chunk_id for c in rag.retrieve(q, top_k=top_k)]
        rag._hybrid_fuse = real_fuse

        qv = rag._embed_query(q)
        # 臂 candidate_prefix: 候选列表本身是否依赖请求深度
        dense_30 = rag._search(q, SHALLOW, None, query_embedding=qv)
        dense_deep = rag._search(q, DEEP, None, query_embedding=qv)
        bm25_30 = rag._bm25_search(q, SHALLOW, None)
        bm25_deep = rag._bm25_search(q, DEEP, None)

        # 臂 algebraic: 同一份深池候选, 截两种深度再融合 (零抖动)
        fuse30 = [c.chunk_id
                  for c in rag._hybrid_fuse(dense_deep[:SHALLOW], bm25_deep[:SHALLOW], top_k)]
        fuse200 = [c.chunk_id
                   for c in rag._hybrid_fuse(dense_deep[:DEEP], bm25_deep[:DEEP], top_k)]

        # 臂 fuse_output_depth: 同一份浅池候选, 融合输出截 top_k vs 截 FUSE_OUT
        fout_k = [c.chunk_id for c in rag._hybrid_fuse(dense_30, bm25_30, top_k)]
        fout_deep = [c.chunk_id for c in rag._hybrid_fuse(dense_30, bm25_30, FUSE_OUT)]

        out.append({
            "id": item["id"],
            "e2e": seq,
            "e2e_deep_fuse": deep_fuse_e2e,
            "fuse_out_k": fout_k,
            "fuse_out_deep": fout_deep,
            "dense_30": [c.chunk_id for c in dense_30],
            "dense_deep_head": [c.chunk_id for c in dense_deep[:SHALLOW]],
            "bm25_30": [c.chunk_id for c in bm25_30],
            "bm25_deep_head": [c.chunk_id for c in bm25_deep[:SHALLOW]],
            "fuse_30": fuse30,
            "fuse_200": fuse200,
            "n_dense_deep": len(dense_deep),
            "n_bm25_deep": len(bm25_deep),
        })
    rag._embed_query = real_embed
    return out


def _run_procs(payload: dict, n_procs: int, runner=None) -> list[list[dict]]:
    """起 n_procs 个**真正独立的 python 进程**, 每个跑一遍全部题目。

    子进程失败当场抛出: 静默跳过会让样本数虚高, 而这个探针的意义就在样本数是真的。
    用 subprocess 而非 multiprocessing —— 后者的 spawn 从 heredoc/REPL 调用会挂死
    (与 eval/jitter_probe.py 同一理由)。
    """
    if runner is not None:
        return runner(payload, n_procs)
    if n_procs < 2:
        raise ValueError("跨进程对照至少要 2 个进程")

    import concurrent.futures as cf
    import subprocess
    import tempfile

    root = str(Path(__file__).resolve().parent.parent)

    def one(_i):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                         encoding="utf-8") as f:
            json.dump(payload, f)
            path = f.name
        try:
            r = subprocess.run(
                [sys.executable, "-m", "eval.pool_depth_probe", "--worker", path],
                cwd=root, capture_output=True, text=True, check=True,
            )
            return json.loads(r.stdout)
        except subprocess.CalledProcessError as exc:
            raise RuntimeError(f"子进程失败: {exc.stderr[-2000:]}") from exc
        finally:
            Path(path).unlink(missing_ok=True)

    with cf.ThreadPoolExecutor(max_workers=min(n_procs, 8)) as ex:
        return list(ex.map(one, range(n_procs)))


# ---- 聚合 -------------------------------------------------------------------


def aggregate(proc_results: Sequence[Sequence[dict]]) -> dict:
    """把 N 个进程 × M 题的原始结果收成三条臂的判据。"""
    ids = [r["id"] for r in proc_results[0]]
    by_q: dict[str, list[dict]] = {qid: [] for qid in ids}
    for proc in proc_results:
        for row in proc:
            by_q[row["id"]].append(row)

    alg_bad, cand_bad, fout_bad, fout_e2e_bad = [], [], [], []
    headroom = []
    aa_total = {"n_pairs": 0, "n_mismatched": 0, "max_positional_diff": 0}
    ab_total = {"n_pairs": 0, "n_mismatched": 0, "max_positional_diff": 0}
    per_q = {}
    for qid, rows in by_q.items():
        alg_diffs = [positional_diff(r["fuse_30"], r["fuse_200"]) for r in rows]
        cand_diffs = [
            max(positional_diff(r["dense_30"], r["dense_deep_head"]),
                positional_diff(r["bm25_30"], r["bm25_deep_head"]))
            for r in rows
        ]
        aa = [pair_stats(r["e2e"], AA_PAIRS) for r in rows]
        ab = [pair_stats(r["e2e"], AB_PAIRS) for r in rows]
        for src, dst in ((aa, aa_total), (ab, ab_total)):
            for s in src:
                dst["n_pairs"] += s["n_pairs"]
                dst["n_mismatched"] += s["n_mismatched"]
                dst["max_positional_diff"] = max(
                    dst["max_positional_diff"], s["max_positional_diff"])
        # 融合输出放长: 前 top_k 名是否逐位不变 (以及整条生产链是否逐位不变)
        k = len(rows[0]["fuse_out_k"])
        fout_diffs = [positional_diff(r["fuse_out_k"], r["fuse_out_deep"][:k]) for r in rows]
        fout_e2e_diffs = [positional_diff(r["e2e"][0], r["e2e_deep_fuse"]) for r in rows]
        q_headroom = min(len(r["fuse_out_deep"]) for r in rows)
        headroom.append(q_headroom)

        if any(alg_diffs):
            alg_bad.append(qid)
        if any(cand_diffs):
            cand_bad.append(qid)
        if any(fout_diffs):
            fout_bad.append(qid)
        if any(fout_e2e_diffs):
            fout_e2e_bad.append(qid)
        per_q[qid] = {
            "algebraic_max_diff": max(alg_diffs),
            "candidate_prefix_max_diff": max(cand_diffs),
            "fuse_out_max_diff": max(fout_diffs),
            "fuse_out_e2e_max_diff": max(fout_e2e_diffs),
            "fuse_candidates": q_headroom,
            "aa_mismatched": sum(s["n_mismatched"] for s in aa),
            "ab_mismatched": sum(s["n_mismatched"] for s in ab),
            "aa_max_diff": max(s["max_positional_diff"] for s in aa),
            "ab_max_diff": max(s["max_positional_diff"] for s in ab),
            # 跨进程: 同一池深下, N 个进程各自的第 1 次调用有几种结果
            "cross_proc_shallow": cross_process_stability([r["e2e"][0] for r in rows]),
            "cross_proc_deep": cross_process_stability([r["e2e"][1] for r in rows]),
        }

    agg = {
        "algebraic": {
            "n_questions": len(by_q),
            "n_mismatched_questions": len(alg_bad),
            "mismatched": alg_bad,
        },
        "candidate_prefix": {
            "n_questions": len(by_q),
            "n_mismatched_questions": len(cand_bad),
            "mismatched": cand_bad,
        },
        "fuse_output_depth": {
            "n_questions": len(by_q),
            "fuse_out": FUSE_OUT,
            "n_mismatched_questions": len(fout_bad),
            "mismatched": fout_bad,
            "e2e_n_mismatched_questions": len(fout_e2e_bad),
            "e2e_mismatched": fout_e2e_bad,
            # 补位余量: 融合后可用条目数的最小值 (B 组腾席位后能从这里补回来)
            "min_fuse_candidates": min(headroom),
            "median_fuse_candidates": sorted(headroom)[len(headroom) // 2],
        },
        "e2e": {"aa": aa_total, "ab": ab_total},
        "per_question": per_q,
    }
    agg["verdict"] = verdict(agg)
    return agg


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="hybrid_pool 深度不变性探针")
    p.add_argument("--procs", type=int, default=12)
    p.add_argument("--top-k", type=int, default=15)
    p.add_argument("--test-set", default=DEFAULT_TEST_SET)
    p.add_argument("--ids", default=None,
                   help="逗号分隔题号; 缺省用层① max_cluster>=5 的 11 题 (含 q38); "
                        "'all' = 题集全量")
    p.add_argument("--no-pin", action="store_true",
                   help="不钉 query 向量 (与生产完全一致, embedding 抖动叠加进来)")
    p.add_argument("--output", default=None)
    p.add_argument("--worker", default=None, help="内部用: 子进程模式")
    args = p.parse_args(argv)

    if args.worker:
        with open(args.worker, encoding="utf-8") as f:
            payload = json.load(f)
        print(json.dumps(_worker(payload)))
        return 0

    if not args.output:
        raise SystemExit("--output 是必需的 (除非 --worker)")

    from eval.jitter_probe import _engine
    from eval.run_eval import load_test_set

    by_id = {q["id"]: q for q in load_test_set(args.test_set)}
    if args.ids == "all":
        wanted = list(by_id)
    elif args.ids:
        wanted = [s.strip() for s in args.ids.split(",")]
    else:
        wanted = DEFAULT_IDS
    missing = [i for i in wanted if i not in by_id]
    if missing:
        raise SystemExit(f"题号不在 {args.test_set}: {missing}")

    # query 向量在**父进程 embed 一次**, 所有子进程共用逐位相同的向量 ——
    # embedding 这一维被完全控制掉, 剩下的不一致只可能来自 Chroma 与池深度。
    emb = None if args.no_pin else _engine("dense", args.top_k)
    items = []
    for qid in wanted:
        q = by_id[qid]["question"]
        items.append({"id": qid, "question": q,
                      "vector": None if emb is None else emb._embed_query(q)})
    payload = {"top_k": args.top_k, "items": items}

    t0 = time.time()
    proc_results = _run_procs(payload, args.procs)
    agg = aggregate(proc_results)
    agg.update({
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "n_procs": args.procs, "top_k": args.top_k, "test_set": args.test_set,
        "ids": wanted, "vector_pinned": emb is not None,
        "shallow_pool": SHALLOW, "deep_pool": DEEP, "seq": SEQ,
        "elapsed_sec": round(time.time() - t0, 1),
    })
    agg["raw"] = compact_raw(proc_results)
    agg["raw_compacted"] = True  # 读取前先过 expand_raw()

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(agg, f, ensure_ascii=False, indent=1)

    v = agg["verdict"]
    print(f"题数 {len(wanted)}  进程数 {args.procs}  向量钉死 {agg['vector_pinned']}  "
          f"耗时 {agg['elapsed_sec']}s")
    print(f"[algebraic]        同候选截 30 vs 截 200, top-15 有差异的题: "
          f"{agg['algebraic']['n_mismatched_questions']}/{len(wanted)} "
          f"{agg['algebraic']['mismatched'] or ''}")
    print(f"[candidate_prefix] _search(30) vs _search(200)[:30] 有差异的题: "
          f"{agg['candidate_prefix']['n_mismatched_questions']}/{len(wanted)} "
          f"{agg['candidate_prefix']['mismatched'] or ''}")
    aa, ab = agg["e2e"]["aa"], agg["e2e"]["ab"]
    print(f"[e2e A/A 空白对照] 不一致 {aa['n_mismatched']}/{aa['n_pairs']} 对, "
          f"最大逐位差 {aa['max_positional_diff']}")
    print(f"[e2e A/B 池深对照] 不一致 {ab['n_mismatched']}/{ab['n_pairs']} 对, "
          f"最大逐位差 {ab['max_positional_diff']}")
    fo = agg["fuse_output_depth"]
    print(f"[fuse_output_depth] 池不动只放长融合输出到 {fo['fuse_out']}: "
          f"前 {args.top_k} 名有差异的题 {fo['n_mismatched_questions']}/{len(wanted)}, "
          f"整条生产链有差异的题 {fo['e2e_n_mismatched_questions']}/{len(wanted)}; "
          f"补位余量最小 {fo['min_fuse_candidates']} 条")
    n_cross = sum(1 for r in agg["per_question"].values()
                  if r["cross_proc_shallow"]["distinct_orders"] > 1
                  or r["cross_proc_deep"]["distinct_orders"] > 1)
    print(f"[跨进程本底]       同题同参数, {args.procs} 进程结果不止一种的题: "
          f"{n_cross}/{len(wanted)}")
    print(f"POOL_DEEP_OK = {v['POOL_DEEP_OK']}  ({v})")
    print(f"明细: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
