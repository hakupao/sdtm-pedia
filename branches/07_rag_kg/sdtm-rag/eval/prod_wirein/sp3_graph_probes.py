"""SP3 anti-overfitting probes:
(A) held-out graph queries over entities NOT in eval test sets — GraphAnswerer facts must
    match the GraphEngine ground truth (which test_graph_engine already pins to raw meta.yaml).
(B) 140q zero-pollution — GraphAnswerer.resolve() must return None for EVERY question in
    test_set_v3.yml (those are SP1/SP2/retrieval questions; graph must not inject into them).
Run: .venv/bin/python eval/prod_wirein/sp3_graph_probes.py"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from server.config import settings  # noqa: E402
from server.graph_answer import GraphAnswerer  # noqa: E402
from server.graph_engine import GraphEngine  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402

HELD_OUT = [
    ("What is affected if codelist C66728 changes?", "C66728", "impacted_domains"),
    ("Which domains are impacted by changing AGE?", "AGE", "impacted_domains"),
    ("Which variables appear in at least 30 domains?", None, None),
    ("How is DM related to other domains?", None, None),
]


def main() -> int:
    store = MetaStore(settings.meta_path)
    ga = GraphAnswerer(GraphEngine(store))
    fails = 0

    # (A) held-out facts present + cardinality matches engine
    for q, subj, kind in HELD_OUT:
        facts = ga.resolve(q)
        if facts is None:
            print(f"FAIL (A) resolve None: {q}")
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
            print(f"PASS (A) fired: {q}")

    # (B) zero-pollution over the 140q
    raw = yaml.safe_load((Path(__file__).resolve().parents[2] / "eval" / "test_set_v3.yml").read_text())
    polluted = []

    def walk(node):
        if isinstance(node, dict):
            if isinstance(node.get("question"), str) and ga.resolve(node["question"]) is not None:
                polluted.append(node["question"])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(raw)
    if polluted:
        fails += len(polluted)
        print(f"FAIL (B) graph fired on {len(polluted)} non-graph q (first 5): {polluted[:5]}")
    else:
        print("PASS (B) 140q zero-pollution: GraphAnswerer silent on all test_set_v3 questions")

    print(f"\nSP3 PROBES: {'ALL PASS' if fails == 0 else str(fails) + ' FAIL'}")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
