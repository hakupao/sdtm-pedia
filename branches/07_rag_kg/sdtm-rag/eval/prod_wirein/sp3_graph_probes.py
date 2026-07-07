"""SP3+AGG anti-overfitting probes:
(A) held-out queries over entities NOT in eval test sets — channel facts must match
    the GraphEngine ground truth (test_graph_engine pins the engine to raw meta.yaml).
(B) 140q zero-pollution — GraphAnswerer.resolve() AND AggregateAnswerer.resolve() must
    return None for EVERY question in test_set_v3.yml (SP1/SP2/retrieval questions;
    graph/aggregate must not inject into them).
Run: .venv/bin/python eval/prod_wirein/sp3_graph_probes.py"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from server.aggregate_answer import AggregateAnswerer  # noqa: E402
from server.config import settings  # noqa: E402
from server.graph_answer import GraphAnswerer  # noqa: E402
from server.graph_engine import GraphEngine  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402

GRAPH_HELD_OUT = [
    ("What is affected if codelist C66728 changes?", "C66728", "impacted_domains"),
    ("Which domains are impacted by changing AGE?", "AGE", "impacted_domains"),
    ("How is DM related to other domains?", None, None),
]
AGG_HELD_OUT = [
    "Which variables appear in at least 30 domains?",
    "Any variables used across 20+ domains?",
    "What's the most reused controlled terminology?",
]


def main() -> int:
    store = MetaStore(settings.meta_path)
    engine = GraphEngine(store)
    ga = GraphAnswerer(engine)
    agg = AggregateAnswerer(engine)
    fails = 0

    # (A) graph held-out facts present + cardinality matches engine
    for q, subj, kind in GRAPH_HELD_OUT:
        facts = ga.resolve(q)
        if facts is None:
            print(f"FAIL (A) graph resolve None: {q}")
            fails += 1
            continue
        if subj and kind:
            truth = store.domains_for_codelist(subj) if subj.startswith("C") \
                else store.domains_for_variable(subj)
            cc = [c for c in facts.checkable_counts if c.subject == subj and c.kind == kind]
            ok = cc and cc[0].value == len(truth)
            print(f"{'PASS' if ok else 'FAIL'} (A) {subj} {kind}={len(truth)}")
            fails += 0 if ok else 1
        else:
            print(f"PASS (A) graph fired: {q}")

    # (A') AGG held-out fires
    for q in AGG_HELD_OUT:
        ok = agg.resolve(q) is not None
        print(f"{'PASS' if ok else 'FAIL'} (A') agg fired: {q}")
        fails += 0 if ok else 1

    # (B) zero-pollution over the 140q — BOTH channels silent
    raw = yaml.safe_load((Path(__file__).resolve().parents[2] / "eval" / "test_set_v3.yml").read_text())
    polluted: list[tuple[str, str]] = []

    def walk(node):
        if isinstance(node, dict):
            q = node.get("question")
            if isinstance(q, str):
                if ga.resolve(q) is not None:
                    polluted.append(("graph", q))
                if agg.resolve(q) is not None:
                    polluted.append(("agg", q))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(raw)
    if polluted:
        fails += len(polluted)
        print(f"FAIL (B) fired on {len(polluted)} non-graph q (first 5): {polluted[:5]}")
    else:
        print("PASS (B) 140q zero-pollution: graph AND aggregate silent on all test_set_v3 questions")

    print(f"\nSP3+AGG PROBES: {'ALL PASS' if fails == 0 else str(fails) + ' FAIL'}")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
