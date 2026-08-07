"""层①: top-k 同质簇挤占的结构量化 (确定性, 零 LLM)。

同质簇 = top-k 里 section 名字面相同的多个条目。它们通常是模板化内容
(63 个域的同名变量行: DOMAIN / STUDYID / USUBJID / VISIT / EPOCH …),
正文逐字近似, 会对含该字面的问句齐刷刷高分, 占满 top-k。

**本探针只描述结构, 不判定好坏。** 挤占是否有害由层② 的 context A/B + judge 判定
(evidence/checkpoints/crowding_layer2.md) —— 用 gold 判据永远判不出来, 因为 S1
前置注入已经确定性地钉死了 gold recall。

已知限制: "同质"只按 section 名字面相同认定, 不含语义近似 (不同域的
`Related Domains` vs `Overview` 这类照不出来)。刻意的确定性取舍。

**逐题数字的可复现性 (Task 3B 实测, 详见 `evidence/checkpoints/topk_jitter.md`)**:
top-15 的**成分**跨独立进程会变 (Chroma HNSW 在一批正文逐字节相同的重复 chunk 之间
选谁, 进程内偏向单一状态 ~95%, 换进程会变)。故:

- `max_cluster` 及基于它的聚合可引用, 但豁免**有条件** —— 抖动换的是"哪个域"而这些
  chunk 的 section 恒为 `DOMAIN`, 即**换人不换 section**; 一旦 churn 跨出簇
  (Task 6 去重 / Task 8 重灌索引 / 改切分或 section 命名 / 改 top_k、hybrid_pool、
  融合权重), 豁免立即失效, 必须重测。见 topk_jitter.md §5.6。
- `dup_seats` / `distinct_sections` 的逐题值**已知有题会变** (q47 接近四六开, q117)。
  验稳走本模块的 `--cross-process` 模式, 它复用 `eval.jitter_probe` 的跨进程取样
  —— **进程内循环 N 次不是 N 个独立样本**, 严重偏向单一状态。
- **排位一律不可复现**: `composition` 里的先后、以及具体哪个域填了某席位, 都由 ingest
  分批噪声决定。"14 席被 §DOMAIN 占掉"可引用, "AE 排在 FA 前面"不可引用。

跑批 (从 sdtm-rag/ 起):
  .venv/bin/python -m eval.crowding_probe --output evidence/checkpoints/crowding_layer1.json
  .venv/bin/python -m eval.crowding_probe --cross-process 20 --ids q38,q47,q117 \\
    --stability-output evidence/checkpoints/crowding_layer1_stability.json
"""
from __future__ import annotations

import argparse
import json
from collections import Counter


def crowding_stats(chunks) -> dict:
    """top-k 组成的挤占统计。dup_seats = 同名 section 占用的**多余**席位总数。"""
    cnt = Counter(getattr(c, "section", None) for c in chunks)
    if not cnt:
        return {"dup_seats": 0, "max_cluster": 0,
                "max_cluster_section": None, "distinct_sections": 0}
    top_sec, top_n = cnt.most_common(1)[0]
    return {
        "dup_seats": sum(n - 1 for n in cnt.values() if n > 1),
        "max_cluster": top_n,
        "max_cluster_section": top_sec,
        "distinct_sections": len(cnt),
    }


# ---- 跨进程验稳 (Task 3B 硬要求) --------------------------------------------

# 分布的取值键: 只用三个**集合**统计, 不含 `max_cluster_section`。
# 理由: 多个 section 并列最大时, `Counter.most_common(1)` 的胜者由插入顺序决定,
# 而插入顺序 = top-k 的**排位** —— 排位不可复现 (topk_jitter.md §4)。把它塞进
# 分布键, 会把排位噪声伪装成"统计量不稳"。max_cluster=1 的题更是全凭排位。
_STAT_KEYS = ("max_cluster", "dup_seats", "distinct_sections")


class _Seat:
    """只带 section 的席位占位符 —— `crowding_stats` 只看这一个属性。

    跨进程取样回来的是 chunk_id 列表 (`stability_across_processes` 的口径, 用
    chunk_id 是因为"文件名#section"会把 63 个 `spec.md#DOMAIN` 塌缩成 1 个 key),
    统计前需按索引元数据还原 section。
    """

    __slots__ = ("section",)

    def __init__(self, section):
        self.section = section


def sections_by_chunk_id(collection, chunk_ids) -> dict:
    """`chunk_id -> section`, 取自活索引元数据。

    未知 id 直接抛错: Chroma 的 `get()` 对不存在的 id **静默返回空**, 落到统计里
    就是一个凭空多出来的 `None` 簇 (会同时抬高 dup_seats、压低 distinct_sections)。
    宁可红, 不许静默造簇。
    """
    ids = sorted(set(chunk_ids))
    if not ids:
        return {}
    got = collection.get(ids=ids, include=["metadatas"])
    out = {i: (m or {}).get("section") for i, m in zip(got["ids"], got["metadatas"],
                                                      strict=True)}
    missing = [i for i in ids if i not in out]
    if missing:
        raise KeyError(f"索引里没有这些 chunk_id: {missing[:5]} (共 {len(missing)} 个) "
                       "—— 索引与取样结果不同源, 统计会凭空多出 None 簇")
    return out


def stats_distribution(runs, sections: dict) -> dict:
    """多次独立运行的 chunk_id 列表 -> 挤占统计的**取值分布**。

    刻意只报分布不报众数: 众数会把 q47 那种接近四六开的题写成一个确定值。
    `values` 按出现次数降序, 次数相同再按取值排序 —— 保证复跑的输出逐字可比。
    """
    dist = Counter()
    for run in runs:
        st = crowding_stats([_Seat(sections[cid]) for cid in run])
        dist[tuple(st[k] for k in _STAT_KEYS)] += 1
    values = [dict(zip(_STAT_KEYS, k, strict=True), n_procs=n)
              for k, n in sorted(dist.items(), key=lambda kv: (-kv[1], kv[0]))]
    return {"n_runs": sum(dist.values()), "n_distinct_values": len(dist),
            "values": values}


def crowding_across_processes(question: str, n_procs: int, sections_of,
                              config: str = "hybrid", top_k: int = 15,
                              runner=None) -> dict:
    """跨**独立进程**取样下, 本题挤占统计的取值分布。

    取样一律走 `eval.jitter_probe.stability_across_processes` —— 本项目刚为"同一逻辑
    存在第二份实现"付过代价, 跨进程取样只许有一个来源。进程内循环不算独立样本
    (实测 60 次里 57:3 ≈ 95% 偏向单一状态)。

    `sections_of(chunk_ids) -> dict` 由调用方注入 (生产用 `sections_by_chunk_id`),
    测试可注入假映射, 从而不起真进程也能验聚合口径。

    ⚠️ `n_procs=20` 是**检出不稳定的下限**, 不足以刻画分布尾部: 稀有态在 1/20 量级,
    且不同批次见到的状态集合不同。结论只许写"见到 N 种取值", **不许把次数当概率**。
    """
    from eval.jitter_probe import stability_across_processes

    rep = stability_across_processes(question, n_procs=n_procs, config=config,
                                     top_k=top_k, runner=runner)
    sections = sections_of({cid for run in rep["runs"] for cid in run})
    out = stats_distribution(rep["runs"], sections)
    out.update({"n_procs": rep["n_procs"], "distinct_sets": rep["distinct_sets"],
                "sometimes": rep["sometimes"]})
    return out


# ---- 跑批 -------------------------------------------------------------------


def _engine(top_k: int):
    from server.config import settings
    from server.rag import RAGEngine

    return RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model, top_k=top_k,
        structured_lookup_enabled=True, hybrid_enabled=True,
        hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=settings.hybrid_pool,
    )


def _run_single_shot(qs, top_k: int, output: str) -> int:
    rag = _engine(top_k)
    rows = []
    for i, q in enumerate(qs, 1):
        chunks = rag.retrieve(q["question"], top_k=top_k)
        st = crowding_stats(chunks)
        rows.append({
            "id": q["id"], "category": q["category"], "n": len(chunks), **st,
            # 单次快照: 顺序与"哪个域填了某席位"都是噪声, 不可引用 (见模块 docstring)
            "composition": [
                {"source": c.source, "section": c.section,
                 "sim": round(c.similarity, 4),
                 "via_lookup": bool(getattr(c, "via_lookup", False))}
                for c in chunks
            ],
        })
        print(f"[{i}/{len(qs)}] {q['id']} dup={st['dup_seats']} "
              f"max={st['max_cluster']}(§{st['max_cluster_section']})", flush=True)

    with open(output, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
        f.write("\n")

    n = len(rows)
    print(f"\n===== 层① 汇总 (题数 {n}, k={top_k}) =====")
    for thr in (3, 5, 8):
        m = sum(1 for r in rows if r["max_cluster"] >= thr)
        print(f"  最大同名 section 簇 >= {thr:2d} 席: {m:3d} 题 ({m / n * 100:.1f}%)")
    print(f"  平均 dup_seats: {sum(r['dup_seats'] for r in rows) / n:.2f} / {top_k}")
    print(f"  平均 distinct_sections: {sum(r['distinct_sections'] for r in rows) / n:.2f}")
    print("\n-- 挤占最重的 15 题 (按 max_cluster; 同值间的先后无意义):")
    for r in sorted(rows, key=lambda x: (-x["max_cluster"], x["id"]))[:15]:
        print(f"  {r['id']:>6} {r['category']:<13} max={r['max_cluster']:2d} "
              f"§{r['max_cluster_section']}  dup={r['dup_seats']}")
    print(f"\n明细: {output}")
    return 0


def _run_cross_process(qs, top_k: int, n_procs: int, output: str) -> int:
    rag = _engine(top_k)
    rows = {}
    for i, q in enumerate(qs, 1):
        rep = crowding_across_processes(
            q["question"], n_procs=n_procs, top_k=top_k,
            sections_of=lambda ids: sections_by_chunk_id(rag.collection, ids),
        )
        rows[q["id"]] = rep
        vals = " | ".join(
            f"({v['max_cluster']},{v['dup_seats']},{v['distinct_sections']})×{v['n_procs']}"
            for v in rep["values"])
        print(f"[{i}/{len(qs)}] {q['id']} 取值 {rep['n_distinct_values']} 种: {vals} "
              f"(成分 {rep['distinct_sets']} 种)", flush=True)

    payload = {
        "_meta": {
            "what": "跨独立进程取样下, 层① 三个集合统计的取值分布",
            "sampling": "eval.jitter_probe.stability_across_processes (真子进程)",
            "why_cross_process": "进程内循环 N 次不是 N 个独立样本: 实测 60 次里 "
                                 "57:3 ≈ 95% 偏向单一状态, 系统性低估状态分布",
            "n_procs_is_a_floor": "n_procs 是检出不稳定的下限, 不足以刻画分布尾部 "
                                  "(稀有态在 1/20 量级, 且不同批次见到的状态集合不同)。"
                                  "只可读作'见到 N 种取值', 次数不是概率。",
            "no_rank": "分布键不含 max_cluster_section: 并列时它由插入顺序(=排位)决定, "
                       "而排位不可复现。",
            "n_procs": n_procs, "top_k": top_k, "config": "hybrid + structured_lookup",
        },
        "questions": rows,
    }
    with open(output, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write("\n")

    unstable = [qid for qid, r in rows.items() if r["n_distinct_values"] > 1]
    print(f"\n===== 跨进程验稳汇总 ({len(rows)} 题 × {n_procs} 进程) =====")
    print(f"  统计取值见到 >1 种的题: {len(unstable)}/{len(rows)} {unstable}")
    print(f"  明细: {output}")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="层① 同质簇挤占结构探针")
    p.add_argument("test_set", nargs="?", default="eval/test_set_v3.yml")
    p.add_argument("--top-k", type=int, default=15)
    p.add_argument("--output", default="evidence/checkpoints/crowding_layer1.json")
    p.add_argument("--ids", default=None,
                   help="逗号分隔题号, 只跑这些题 (缺省全集)")
    p.add_argument("--cross-process", type=int, default=0, metavar="N",
                   help="改跑跨进程验稳: 每题起 N 个独立进程, 报统计取值分布")
    p.add_argument("--stability-output",
                   default="evidence/checkpoints/crowding_layer1_stability.json")
    args = p.parse_args(argv)

    from eval.run_eval import load_test_set

    qs = load_test_set(args.test_set)   # 走它而非裸 yaml: 拦拼错的 gold 键 / 无 gold 题
    if args.ids:
        wanted = [s.strip() for s in args.ids.split(",")]
        by_id = {q["id"]: q for q in qs}
        missing = [i for i in wanted if i not in by_id]
        if missing:
            raise SystemExit(f"题号不在 {args.test_set}: {missing}")
        qs = [by_id[i] for i in wanted]

    if args.cross_process:
        return _run_cross_process(qs, args.top_k, args.cross_process,
                                  args.stability_output)
    return _run_single_shot(qs, args.top_k, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
