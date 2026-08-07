"""gold 完整性反例扫描: 列出每题 top-N 中"不被任何 gold 匹配"的检索条目。

用途: 找 q38 那类**判据遗漏**——检索找对了权威源, 但 gold 里没写, 于是被判 miss
(假失分), 或虽然别的 gold 命中了、真正的权威源却从未被判据看见 (判据视野盲区)。

本工具**只描述, 不判定**: 输出交独立 agent 逐条审"这是不是该题遗漏的权威源"。
匹配一律走 eval.run_eval.source_matches, 不自带第二份实现 (硬规矩 1)。
"""
from __future__ import annotations

import argparse
import json

import yaml

from eval.run_eval import source_matches


def unmatched_in_top_n(chunks, expected_sources, n=3, any_of=None):
    """返回 top-n 里不被任何 gold (AND 组 + OR 组合并看) 匹配的条目。

    逐条判定 (每条自成一个单元素列表) 而非整体判定: 我们要的是"**这一条**有没有
    被某条 gold 认领", 而 source_matches 的语义是"gold 在**整个列表**里有没有命中"。
    传整个列表会让 rank1 因为 rank3 命中而被误判为已认领。
    """
    golds = list(expected_sources or []) + list(any_of or [])
    out = []
    for rank, c in enumerate(list(chunks)[:n], 1):
        sec = getattr(c, "section", None)
        if any(source_matches(g, [c.source], [sec]) for g in golds):
            continue
        out.append({
            "rank": rank,
            "source": c.source,
            "section": sec,
            "sim": round(c.similarity, 4),
        })
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description="扫描 gold 完整性反例")
    p.add_argument("test_set")
    p.add_argument("--top-n", type=int, default=3)
    p.add_argument("--top-k", type=int, default=15)
    p.add_argument("--output", required=True)
    args = p.parse_args(argv)

    from server.config import settings
    from server.rag import RAGEngine

    rag = RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model, top_k=args.top_k,
        structured_lookup_enabled=True, hybrid_enabled=True,
        hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=settings.hybrid_pool,
    )

    rows = []
    qs = yaml.safe_load(open(args.test_set))
    for i, q in enumerate(qs, 1):
        chunks = rag.retrieve(q["question"], top_k=args.top_k)
        um = unmatched_in_top_n(
            chunks, q.get("expected_sources", []), n=args.top_n,
            any_of=q.get("expected_sources_any"),
        )
        rows.append({
            "id": q["id"], "category": q["category"], "question": q["question"],
            "gold": q.get("expected_sources", []),
            "gold_any": q.get("expected_sources_any"),
            "unmatched_top3": um,
        })
        print(f"[{i}/{len(qs)}] {q['id']} unmatched={len(um)}", flush=True)

    json.dump(rows, open(args.output, "w"), ensure_ascii=False, indent=1)
    n_any = sum(1 for r in rows if r["unmatched_top3"])
    print(f"\n{n_any}/{len(rows)} 题的 top-{args.top_n} 含未被 gold 匹配的条目")
    print(f"明细: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
