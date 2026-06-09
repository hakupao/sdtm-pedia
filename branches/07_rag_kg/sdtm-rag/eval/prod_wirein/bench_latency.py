"""Step 3 latency: startup BM25 build + per-query retrieve() overhead.

Measures the cost the wire-in adds: (1) one-time BM25 index build at engine init,
(2) per-query retrieve() latency OFF (plain cosine) vs ON (S1+hybrid), and within
ON, split by whether S1 fired (S1-firing queries do extra Chroma source-filtered
lookups; embed-once means they add NO extra embedding round-trips). LLM answer
latency is separate and dominates total /ask time — this isolates retrieval only.
"""
from __future__ import annotations

import statistics
import sys
import time
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from server.config import settings  # noqa: E402
from server.rag import RAGEngine  # noqa: E402

QUESTIONS = [
    q["question"]
    for q in yaml.safe_load((Path(__file__).resolve().parents[1] / "test_set_v2.yml").read_text())
]


def build(structured: bool, hybrid: bool) -> tuple[RAGEngine, float]:
    t0 = time.perf_counter()
    eng = RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name, embedding_model=settings.embedding_model,
        top_k=settings.top_k, structured_lookup_enabled=structured,
        hybrid_enabled=hybrid, hybrid_fusion=settings.hybrid_fusion,
        hybrid_alpha=settings.hybrid_alpha, hybrid_pool=settings.hybrid_pool,
    )
    return eng, time.perf_counter() - t0


def pcts(xs: list[float]) -> str:
    xs = sorted(xs)
    p = lambda q: xs[min(len(xs) - 1, int(q * len(xs)))]
    return (f"n={len(xs)} p50={statistics.median(xs)*1000:.0f}ms "
            f"p95={p(0.95)*1000:.0f}ms max={max(xs)*1000:.0f}ms mean={statistics.mean(xs)*1000:.0f}ms")


def timed(eng: RAGEngine) -> list[float]:
    for q in QUESTIONS[:3]:  # warmup
        eng.retrieve(q)
    out = []
    for q in QUESTIONS:
        t0 = time.perf_counter()
        eng.retrieve(q)
        out.append(time.perf_counter() - t0)
    return out


def main() -> int:
    print("=" * 64)
    print("STEP 3 LATENCY — retrieval only (LLM answer time excluded)")
    print("=" * 64)

    off, t_off = build(False, False)
    print(f"\nstartup init (OFF, no BM25): {t_off*1000:.0f}ms")
    on, t_on = build(True, True)
    print(f"startup init (ON, builds BM25 over {on.collection.count()} chunks): {t_on*1000:.0f}ms")
    print("  ^ one-time, at server boot")

    lat_off = timed(off)
    lat_on = timed(on)

    # split ON by whether S1 fired
    fired, not_fired = [], []
    for q, t in zip(QUESTIONS, lat_on):
        (fired if on._structured_lookup.resolve(q) else not_fired).append(t)

    print(f"\nper-query retrieve():")
    print(f"  OFF (plain cosine)       : {pcts(lat_off)}")
    print(f"  ON  (all queries)        : {pcts(lat_on)}")
    if fired:
        print(f"  ON  (S1 fired)           : {pcts(fired)}")
    if not_fired:
        print(f"  ON  (S1 not fired)       : {pcts(not_fired)}")
    print(f"\n  median overhead ON vs OFF: "
          f"{(statistics.median(lat_on)-statistics.median(lat_off))*1000:+.0f}ms")
    print("=" * 64)
    return 0


if __name__ == "__main__":
    sys.exit(main())
