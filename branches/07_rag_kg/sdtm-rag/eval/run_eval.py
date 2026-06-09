"""Phase 1D Full Evaluation runner.

Modes:
  --retrieval-only   Score source recall only (no LLM calls, fast+free)
  (default)          Full: retrieval + LLM answer + fact recall

Flags:
  --model MODEL      Override LLM model string (bypasses Router, uses litellm directly)
                     e.g. anthropic/claude-sonnet-4-6, deepseek/deepseek-chat
  --threshold FLOAT  Override pass/fail threshold (default 0.85)
  --tag TAG          Label added to output JSON for cross-model comparison

Run from sdtm-rag/:
  python eval/run_eval.py eval/test_set_v0.yml --retrieval-only
  python eval/run_eval.py eval/test_set_v0.yml
  python eval/run_eval.py eval/test_set_v0.yml --output eval/baseline_report.json
  python eval/run_eval.py eval/test_set_v1.yml --model anthropic/claude-sonnet-4-6 --tag sonnet --output eval/report_sonnet.json
  python eval/run_eval.py eval/test_set_v1.yml --model deepseek/deepseek-chat --tag deepseek --threshold 0.80 --output eval/report_deepseek.json
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import litellm
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from server.config import settings  # noqa: E402
from server.llm_config import create_router  # noqa: E402
from server.rag import RAGEngine  # noqa: E402

TOP_K = 15


def load_test_set(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_source_recall(
    retrieved_sources: list[str],
    expected_sources: list[str],
) -> tuple[float, list[str], list[str]]:
    hits: list[str] = []
    misses: list[str] = []
    for exp in expected_sources:
        found = any(exp in src for src in retrieved_sources)
        if found:
            hits.append(exp)
        else:
            misses.append(exp)
    recall = len(hits) / len(expected_sources) if expected_sources else 1.0
    return recall, hits, misses


def check_fact_recall(
    answer: str,
    expected_facts: list[str],
) -> tuple[float, list[str], list[str]]:
    answer_lower = answer.lower()
    hits: list[str] = []
    misses: list[str] = []
    for fact in expected_facts:
        if fact.lower() in answer_lower:
            hits.append(fact)
        else:
            misses.append(fact)
    recall = len(hits) / len(expected_facts) if expected_facts else 1.0
    return recall, hits, misses


def run_evaluation(
    test_set: list[dict],
    rag: RAGEngine,
    router=None,
    retrieval_only: bool = False,
    direct_model: str | None = None,
    top_k: int = TOP_K,
    temperature: float | None = None,
) -> list[dict]:
    results: list[dict] = []
    for q in test_set:
        qid = q["id"]
        print(f"[{qid}] {q['question'][:60]}...", end=" ", flush=True)
        t0 = time.perf_counter()

        chunks = rag.retrieve(q["question"], top_k=top_k)
        retrieved_sources = [c.source for c in chunks]

        src_recall, src_hits, src_misses = check_source_recall(
            retrieved_sources, q.get("expected_sources", [])
        )

        result: dict = {
            "id": qid,
            "category": q["category"],
            "question": q["question"],
            "source_recall": round(src_recall, 4),
            "source_hits": src_hits,
            "source_misses": src_misses,
            "top5_sources": retrieved_sources[:5],
            "top5_similarities": [c.similarity for c in chunks[:5]],
        }

        if not retrieval_only and (router is not None or direct_model is not None):
            context = rag.format_context(chunks)
            messages = rag.build_messages(q["question"], context)

            comp_kwargs: dict = {"messages": messages}
            if temperature is not None:
                comp_kwargs["temperature"] = temperature  # 0.0 => deterministic paired runs
            for _attempt in range(5):
                try:
                    if direct_model is not None:
                        response = litellm.completion(model=direct_model, **comp_kwargs)
                    else:
                        response = router.completion(model="default", **comp_kwargs)
                    break
                except Exception as exc:
                    if "rate_limit" in str(exc).lower() or "429" in str(exc):
                        wait = 30 * (2 ** _attempt)
                        print(f"\n  [RATE LIMIT] waiting {wait}s...", end=" ", flush=True)
                        time.sleep(wait)
                    else:
                        raise

            answer = response.choices[0].message.content or ""
            usage = {}
            if response.usage:
                usage = {
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens,
                }

            fact_recall, fact_hits, fact_misses = check_fact_recall(
                answer, q.get("expected_facts", [])
            )
            result.update({
                "fact_recall": round(fact_recall, 4),
                "fact_hits": fact_hits,
                "fact_misses": fact_misses,
                "answer_preview": answer[:600],
                "usage": usage,
                "model": direct_model if direct_model is not None else getattr(response, "model", "unknown"),
            })

        elapsed = time.perf_counter() - t0
        result["elapsed_s"] = round(elapsed, 2)

        tag = "SRC" if retrieval_only else "FULL"
        src_pct = f"{src_recall:.0%}"
        fact_pct = f"{result.get('fact_recall', 0):.0%}" if not retrieval_only else "n/a"
        print(f"[{tag}] src={src_pct} fact={fact_pct} {elapsed:.1f}s")
        results.append(result)

    return results


def print_summary(
    results: list[dict],
    retrieval_only: bool = False,
    threshold: float = 0.85,
    model: str | None = None,
) -> dict:
    n = len(results)
    avg_src = sum(r["source_recall"] for r in results) / n
    src_by_cat: dict[str, list[float]] = {}
    for r in results:
        src_by_cat.setdefault(r["category"], []).append(r["source_recall"])

    print("\n" + "=" * 60)
    print("EVAL SUMMARY")
    print("=" * 60)
    print(f"Questions: {n}")
    if model:
        print(f"Model:     {model}")
    print(f"Threshold: {threshold:.0%}")
    print(f"Source recall (avg): {avg_src:.1%}")
    for cat, vals in sorted(src_by_cat.items()):
        print(f"  {cat}: {sum(vals)/len(vals):.1%} ({len(vals)} q)")

    summary: dict = {
        "n_questions": n,
        "model": model,
        "threshold": threshold,
        "source_recall_avg": round(avg_src, 4),
        "source_recall_by_category": {
            cat: round(sum(vals) / len(vals), 4) for cat, vals in sorted(src_by_cat.items())
        },
    }

    if not retrieval_only:
        avg_fact = sum(r.get("fact_recall", 0) for r in results) / n
        total_tokens = sum(r.get("usage", {}).get("total_tokens", 0) for r in results)
        print(f"Fact recall (avg):   {avg_fact:.1%}")
        print(f"Total tokens used:   {total_tokens:,}")

        fact_by_cat: dict[str, list[float]] = {}
        for r in results:
            fact_by_cat.setdefault(r["category"], []).append(r.get("fact_recall", 0))
        for cat, vals in sorted(fact_by_cat.items()):
            print(f"  {cat}: {sum(vals)/len(vals):.1%}")

        overall = (avg_src + avg_fact) / 2
        print(f"\nOverall (src+fact avg): {overall:.1%}")
        verdict = "PASS" if overall >= threshold else "FAIL"
        print(f"Threshold: {threshold:.0%}  ->  {verdict}")
        summary.update({
            "fact_recall_avg": round(avg_fact, 4),
            "fact_recall_by_category": {
                cat: round(sum(vals) / len(vals), 4) for cat, vals in sorted(fact_by_cat.items())
            },
            "overall": round(overall, 4),
            "total_tokens": total_tokens,
            "verdict": verdict,
        })
    else:
        verdict = "PASS" if avg_src >= threshold else "FAIL"
        print(f"\nThreshold: {threshold:.0%}  ->  {verdict} (retrieval-only)")
        summary.update({"verdict": verdict})

    failures = [r for r in results if r["source_recall"] < 1.0]
    if failures:
        print(f"\nQuestions with source misses ({len(failures)}):")
        for r in failures:
            print(f"  {r['id']}: src={r['source_recall']:.0%} miss={r['source_misses']}")

    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Phase 1D Full Evaluation")
    parser.add_argument("test_set", help="Path to test_set YAML file")
    parser.add_argument("--retrieval-only", action="store_true")
    parser.add_argument("--output", help="Save results JSON to file")
    parser.add_argument(
        "--model",
        default=None,
        help="Override LLM model string (bypasses Router, uses litellm directly). "
             "E.g. anthropic/claude-sonnet-4-6, deepseek/deepseek-chat",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.85,
        help="Pass/fail threshold (default 0.85)",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=TOP_K,
        help=f"Chunks retrieved per query (default {TOP_K}); T1 ablation lever",
    )
    parser.add_argument(
        "--rerank",
        action="store_true",
        help="T2: enable Cohere rerank (wide pool -> rerank -> top_k). Needs COHERE_API_KEY",
    )
    parser.add_argument(
        "--rerank-candidates",
        type=int,
        default=None,
        help="T2 candidate pool size before rerank (default settings.rerank_candidates=100)",
    )
    parser.add_argument(
        "--query-expansion",
        choices=["none", "multiquery", "hyde", "hyde_rrf"],
        default=None,
        help="T4: rewrite query before search. multiquery=decompose+RRF, hyde=hypothetical doc, "
             "hyde_rrf=fuse original+hyde (augment, not replace)",
    )
    parser.add_argument(
        "--structured-lookup",
        action="store_true",
        help="S1: deterministic structured-lookup union-add (var/CT-code -> gold "
             "file via spec.md xref + VARIABLE_INDEX). Off by default.",
    )
    parser.add_argument(
        "--hybrid",
        action="store_true",
        help="S2: hybrid BM25 (bm25s) over indexed chunks, additively fused with "
             "dense cosine (RRF default). Re-floats literal-token hits. Off by default.",
    )
    parser.add_argument(
        "--hybrid-fusion",
        choices=["rrf", "weighted"],
        default=None,
        help="S2 fusion method (default settings.hybrid_fusion=rrf). weighted uses --hybrid-alpha.",
    )
    parser.add_argument(
        "--hybrid-alpha",
        type=float,
        default=None,
        help="S2 weighted-fusion dense weight (1-alpha=BM25; default settings.hybrid_alpha=0.5)",
    )
    parser.add_argument(
        "--hybrid-pool",
        type=int,
        default=None,
        help="S2 per-list fusion pool depth (default settings.hybrid_pool=100)",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=None,
        help="Answer-model sampling temperature. Default None = provider default "
             "(non-deterministic). Set 0.0 for deterministic paired off/on comparisons.",
    )
    parser.add_argument(
        "--tag",
        default=None,
        help="Optional label added to output JSON for cross-model comparison",
    )
    args = parser.parse_args(argv)

    test_set = load_test_set(args.test_set)
    print(f"Loaded {len(test_set)} questions from {args.test_set}")

    rag = RAGEngine(
        chroma_dir=settings.chroma_dir,
        kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model,
        top_k=args.top_k,
        rerank_enabled=args.rerank,
        rerank_model=settings.rerank_model,
        rerank_candidates=(
            args.rerank_candidates
            if args.rerank_candidates is not None
            else settings.rerank_candidates
        ),
        query_expansion=args.query_expansion or settings.query_expansion,
        expansion_model=settings.expansion_model,
        expansion_n_queries=settings.expansion_n_queries,
        structured_lookup_enabled=args.structured_lookup,
        hybrid_enabled=args.hybrid,
        hybrid_fusion=args.hybrid_fusion or settings.hybrid_fusion,
        hybrid_alpha=(
            args.hybrid_alpha if args.hybrid_alpha is not None else settings.hybrid_alpha
        ),
        hybrid_pool=(
            args.hybrid_pool if args.hybrid_pool is not None else settings.hybrid_pool
        ),
    )
    rerank_info = (
        f", rerank={rag.rerank_model} pool={rag.rerank_candidates}" if args.rerank else ""
    )
    expand_info = (
        f", expansion={rag.query_expansion}({rag.expansion_model})"
        if rag.query_expansion != "none" else ""
    )
    lookup_info = ", structured_lookup=ON" if args.structured_lookup else ""
    hybrid_info = (
        f", hybrid={rag.hybrid_fusion}"
        + (f"(alpha={rag.hybrid_alpha})" if rag.hybrid_fusion == "weighted" else "")
        if args.hybrid else ""
    )
    print(f"RAG engine: {rag.collection.count()} chunks, model={settings.default_model}, top_k={args.top_k}{rerank_info}{expand_info}{lookup_info}{hybrid_info}")

    router = None
    if not args.retrieval_only:
        if args.model:
            print(f"LLM mode: direct litellm, model={args.model}")
        else:
            router = create_router(settings)
            print(f"LLM router: {len(router.model_list)} models")

    print()
    results = run_evaluation(
        test_set, rag, router, args.retrieval_only, direct_model=args.model,
        top_k=args.top_k, temperature=args.temperature,
    )
    summary = print_summary(
        results,
        retrieval_only=args.retrieval_only,
        threshold=args.threshold,
        model=args.model,
    )
    summary["top_k"] = args.top_k
    if args.rerank:
        summary["rerank"] = {
            "model": rag.rerank_model,
            "candidates": rag.rerank_candidates,
        }
    if rag.query_expansion != "none":
        summary["query_expansion"] = {
            "mode": rag.query_expansion,
            "model": rag.expansion_model,
            "n_queries": rag.expansion_n_queries,
        }
    if args.structured_lookup:
        summary["structured_lookup"] = True
    if args.hybrid:
        summary["hybrid"] = {
            "fusion": rag.hybrid_fusion,
            "alpha": rag.hybrid_alpha if rag.hybrid_fusion == "weighted" else None,
        }

    if args.output:
        out: dict = {"summary": summary, "results": results}
        if args.tag:
            out["tag"] = args.tag
        Path(args.output).write_text(
            json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"\nResults saved to {args.output}")

    return 0 if summary["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
