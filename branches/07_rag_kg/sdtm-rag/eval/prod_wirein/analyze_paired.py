"""Step 2 paired-analysis: levers OFF vs ON (same model, same v2 102q).

The gate is NOT "ON fact recall >= 93%"; it is the PAIRED comparison:
  - source recall should jump (retrieval gain carries into the full pipeline)
  - fact recall must NOT regress (no answer dilution from injected chunks)
  - any per-question fact DROP (ON < OFF) is a dilution signal -> inspected
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).parent


def load(name: str) -> dict:
    return json.loads((HERE / name).read_text())


def by_cat(results: list[dict], key: str) -> dict[str, float]:
    acc: dict[str, list[float]] = {}
    for r in results:
        acc.setdefault(r["category"], []).append(r.get(key, 0.0))
    return {c: round(sum(v) / len(v), 4) for c, v in sorted(acc.items())}


def avg(results: list[dict], key: str) -> float:
    return round(sum(r.get(key, 0.0) for r in results) / len(results), 4)


def main() -> int:
    off_name = sys.argv[1] if len(sys.argv) > 1 else "step2_full_off.json"
    on_name = sys.argv[2] if len(sys.argv) > 2 else "step2_full_on.json"
    off = load(off_name)
    on = load(on_name)
    print(f"OFF={off_name}  ON={on_name}")
    ro = {r["id"]: r for r in off["results"]}
    rn = {r["id"]: r for r in on["results"]}

    print("=" * 72)
    print("STEP 2 PAIRED FULL EVAL — DeepSeek, v2 102q — OFF vs ON")
    print("=" * 72)

    for label, key in (("SOURCE recall", "source_recall"), ("FACT recall", "fact_recall")):
        co, cn = by_cat(off["results"], key), by_cat(on["results"], key)
        print(f"\n{label} by category (off -> on, delta):")
        for cat in sorted(set(co) | set(cn)):
            o, n = co.get(cat, 0), cn.get(cat, 0)
            print(f"  {cat:14s} {o:6.1%} -> {n:6.1%}  ({n-o:+.1%})")
        ao, an = avg(off["results"], key), avg(on["results"], key)
        print(f"  {'AVG':14s} {ao:6.1%} -> {an:6.1%}  ({an-ao:+.1%})")

    # Per-question FACT diffs (the dilution probe)
    drops, gains = [], []
    for qid in ro:
        fo = ro[qid].get("fact_recall", 0.0)
        fn = rn.get(qid, {}).get("fact_recall", 0.0)
        if fn < fo - 1e-9:
            drops.append((qid, ro[qid]["category"], fo, fn, rn[qid].get("fact_misses")))
        elif fn > fo + 1e-9:
            gains.append((qid, ro[qid]["category"], fo, fn))

    print("\n" + "-" * 72)
    print(f"PER-QUESTION FACT DIFF: {len(drops)} drop(s), {len(gains)} gain(s)")
    if drops:
        print("\n  DROPS (ON < OFF) — dilution candidates, inspect each:")
        for qid, cat, fo, fn, miss in drops:
            print(f"    {qid} [{cat}] {fo:.0%} -> {fn:.0%}  newly-missed={miss}")
    else:
        print("  No fact-recall drops: zero dilution signal at substring-match level. ✓")
    if gains:
        print("\n  GAINS (ON > OFF):")
        for qid, cat, fo, fn in gains:
            print(f"    {qid} [{cat}] {fo:.0%} -> {fn:.0%}")

    # Gate verdict
    fact_off_avg = avg(off["results"], "fact_recall")
    fact_on_avg = avg(on["results"], "fact_recall")
    fact_on_cat = by_cat(on["results"], "fact_recall")
    no_cat_below_93 = all(v >= 0.93 for v in fact_on_cat.values())
    net_ok = fact_on_avg >= fact_off_avg - 0.01  # allow 1pt substring-match noise band
    print("\n" + "=" * 72)
    print("GATE:")
    print(f"  fact ON avg {fact_on_avg:.1%} vs OFF {fact_off_avg:.1%} "
          f"-> net {'OK' if net_ok else 'REGRESSION'} (1pt noise band)")
    print(f"  all categories fact ON >= 93%: {no_cat_below_93}  {fact_on_cat}")
    print(f"  dilution drops needing explanation: {len(drops)}")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
