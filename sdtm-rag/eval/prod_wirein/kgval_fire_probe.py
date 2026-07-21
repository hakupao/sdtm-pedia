"""KG-value eval — fire-rate instrumentation (the diagnostic the verdict hinges on).

For every question in test_set_kg_value.yml, record whether the SP2 channel
(StructuredAnswerer) and/or the SP3 channel (GraphAnswerer) actually FIRE (resolve() is
not None). This separates the three failure modes when ON≈OFF:
  - channel never fired  -> NL detection recall gap (engine fine, routing too narrow)
  - fired but no gain    -> injection format / model-didn't-use problem
  - fired and gained     -> genuine end-to-end value

Output: eval/prod_wirein/kgval_fire.json + a per-family fire-rate table.
Run from sdtm-rag/:  .venv/bin/python eval/prod_wirein/kgval_fire_probe.py"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from server.config import settings  # noqa: E402
from server.graph_answer import GraphAnswerer  # noqa: E402
from server.graph_engine import GraphEngine  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402
from server.structured_answer import StructuredAnswerer  # noqa: E402

TEST_SET = ROOT / "eval" / "test_set_kg_value.yml"
OUT = ROOT / "eval" / "prod_wirein" / "kgval_fire.json"


def main() -> int:
    store = MetaStore(settings.meta_path)
    sp2 = StructuredAnswerer(store)
    sp3 = GraphAnswerer(GraphEngine(store))
    qs = yaml.safe_load(TEST_SET.read_text(encoding="utf-8"))

    rows = []
    for q in qs:
        f2 = sp2.resolve(q["question"]) is not None
        f3 = sp3.resolve(q["question"]) is not None
        rows.append({"id": q["id"], "family": q["category"],
                     "fired_sp2": f2, "fired_sp3": f3})

    OUT.write_text(json.dumps(rows, indent=2), encoding="utf-8")

    # per-family fire-rate table
    by_fam: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_fam[r["family"]].append(r)
    print(f"Fire-rate over {len(rows)} questions ({TEST_SET.name}):\n")
    print(f"{'family':<18} {'n':>3} {'SP2 fired':>10} {'SP3 fired':>10}")
    for fam in sorted(by_fam):
        g = by_fam[fam]
        n = len(g)
        s2 = sum(r["fired_sp2"] for r in g)
        s3 = sum(r["fired_sp3"] for r in g)
        print(f"{fam:<18} {n:>3} {s2:>4}/{n} {100*s2/n:>4.0f}% {s3:>4}/{n} {100*s3/n:>4.0f}%")
    n = len(rows)
    print(f"{'ALL':<18} {n:>3} "
          f"{sum(r['fired_sp2'] for r in rows):>4}/{n}      "
          f"{sum(r['fired_sp3'] for r in rows):>4}/{n}")
    print(f"\nWrote {OUT}")
    # honest callout: questions where SP3 silent (graph cannot help end-to-end there)
    silent3 = [r["id"] for r in rows if not r["fired_sp3"]]
    if silent3:
        print(f"\nSP3 silent on {len(silent3)}/{n} (graph injects nothing there): {silent3}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
