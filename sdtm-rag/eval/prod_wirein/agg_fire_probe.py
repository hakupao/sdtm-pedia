"""AGG fire-rate probe: for every question in a test set, record whether SP2 / AGG /
SP3 channels fire (resolve() not None). Gate for the held-out set: AGG >= 13/16.
Run: .venv/bin/python eval/prod_wirein/agg_fire_probe.py eval/test_set_agg_heldout.yml"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from server.aggregate_answer import AggregateAnswerer  # noqa: E402
from server.config import settings  # noqa: E402
from server.graph_answer import GraphAnswerer  # noqa: E402
from server.graph_engine import GraphEngine  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402


def main() -> int:
    test_set = Path(sys.argv[1])
    store = MetaStore(settings.meta_path)
    engine = GraphEngine(store)
    from server.structured_answer import StructuredAnswerer
    sp2, agg, sp3 = StructuredAnswerer(store), AggregateAnswerer(engine), GraphAnswerer(engine)
    qs = yaml.safe_load(test_set.read_text(encoding="utf-8"))

    rows = []
    for q in qs:
        rows.append({"id": q["id"], "category": q["category"],
                     "fired_sp2": sp2.resolve(q["question"]) is not None,
                     "fired_agg": agg.resolve(q["question"]) is not None,
                     "fired_sp3": sp3.resolve(q["question"]) is not None})

    out = ROOT / "eval" / "prod_wirein" / f"agg_fire_{test_set.stem}.json"
    out.write_text(json.dumps(rows, indent=2), encoding="utf-8")

    by_cat: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_cat[r["category"]].append(r)
    print(f"{'category':<24} {'n':>3} {'SP2':>8} {'AGG':>8} {'SP3':>8}")
    for cat in sorted(by_cat):
        g = by_cat[cat]
        n = len(g)
        f = [sum(r[k] for r in g) for k in ("fired_sp2", "fired_agg", "fired_sp3")]
        print(f"{cat:<24} {n:>3} {f[0]:>4}/{n} {f[1]:>4}/{n} {f[2]:>4}/{n}")
    n = len(rows)
    n_agg = sum(r["fired_agg"] for r in rows)
    silent = [r["id"] for r in rows if not r["fired_agg"]]
    print(f"\nAGG fired {n_agg}/{n}; silent: {silent}")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
