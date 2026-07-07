"""AGG mini e2e analysis: OFF (SP2+SP3) vs ON (SP2+AGG+SP3), deepseek temp=0.
Gate: held-out subset set_recall Δ(ON−OFF) >= +10pp. Per-question regressions are
listed for causal triage, NOT auto-failed (kgval rl05 lesson: temp=0 still rewrites).
Run: .venv/bin/python eval/prod_wirein/analyze_agg_e2e.py"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

PW = Path(__file__).resolve().parent
sys.path.insert(0, str(PW))
from analyze_kgval import fact_present  # noqa: E402

ROOT = PW.parents[1]
GOLD = {q["id"]: q for q in yaml.safe_load(
    (ROOT / "eval" / "test_set_agg_e2e.yml").read_text(encoding="utf-8"))}


def load(arm: str) -> dict[str, dict]:
    data = json.loads((PW / f"agg_e2e_{arm}.json").read_text())
    return {r["id"]: r for r in data["results"]}


def set_recall(qid: str, res: dict) -> float:
    facts = GOLD[qid].get("expected_facts") or []
    ans = res.get("answer") or res.get("answer_preview") or ""
    if not facts:
        return 1.0
    return sum(fact_present(f, ans) for f in facts) / len(facts)


def main() -> int:
    off, on = load("off"), load("on")
    ids = [i for i in GOLD if i in off and i in on]
    excluded = [i for i in GOLD if i not in off or i not in on]
    if excluded:
        print(f"excluded (missing from an arm's results): {excluded}")
    rows = []
    for qid in ids:
        r_off, r_on = set_recall(qid, off[qid]), set_recall(qid, on[qid])
        rows.append({"id": qid, "heldout": not GOLD[qid].get("regression"),
                     "off": r_off, "on": r_on, "delta": r_on - r_off})

    def avg(sel, label):
        xs = [r for r in rows if sel(r)]
        if not xs:
            print(f"ERROR: no rows in the '{label}' subset - cannot compute an average "
                  "(check that both arms ran and IDs match test_set_agg_e2e.yml).")
            sys.exit(1)
        return (sum(r["off"] for r in xs) / len(xs), sum(r["on"] for r in xs) / len(xs))

    ho_off, ho_on = avg(lambda r: r["heldout"], "held-out")
    rg_off, rg_on = avg(lambda r: not r["heldout"], "regression")
    print(f"held-out   set_recall: OFF {ho_off:.1%} -> ON {ho_on:.1%}  Δ {ho_on-ho_off:+.1%}")
    print(f"regression set_recall: OFF {rg_off:.1%} -> ON {rg_on:.1%}  Δ {rg_on-rg_off:+.1%}")
    regressions = [r for r in rows if r["delta"] < 0]
    for r in regressions:
        print(f"  REGRESSION {r['id']}: {r['off']:.2f} -> {r['on']:.2f}  (needs causal triage)")
    (PW / "agg_e2e_analysis.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    gate = (ho_on - ho_off) >= 0.10
    print(f"\nGATE held-out Δ>=+10pp: {'PASS' if gate else 'FAIL'}")
    return 0 if gate else 1


if __name__ == "__main__":
    sys.exit(main())
