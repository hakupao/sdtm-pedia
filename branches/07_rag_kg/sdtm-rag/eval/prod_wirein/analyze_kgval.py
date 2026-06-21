"""KG-value eval — paired 3-arm analyzer.

Joins the 6 eval runs (arm0/1/2 x deepseek/sonnet) with the gold test set and the
fire-rate probe, then reports the metrics that actually answer the question:

  cardinality_correct  deterministic: does the answer state the exact gold count?
                       (the sharpest OFF-vs-ON signal — OFF cannot enumerate a data-
                       specific count). Word-boundary; ON-OFF DELTA cancels coincidental
                       small-number hits, so the delta is the trustworthy figure.
  set_recall           deterministic: fraction of gold items (domain/var/CT codes) present
                       as WORD-BOUNDARY, CASE-SENSITIVE tokens (avoids the "EG"->"e.g.",
                       "DA"->"data" false positives a substring match would inflate).
  judge_recall         semantic (run_eval --judge); primary for most_shared (a naming Q).

Three deltas per family/model: ΔSP2 = arm1-arm0, ΔSP3 = arm2-arm1 (gates SP4/SP5),
Δwhole = arm2-arm0. Plus a FIRE-CONDITIONAL pass (ΔSP3 restricted to questions where the
graph channel actually fired) — distinguishes "SP3 has no value" from "SP3 never fired".

Run from sdtm-rag/:  .venv/bin/python eval/prod_wirein/analyze_kgval.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PW = ROOT / "eval" / "prod_wirein"
TEST_SET = ROOT / "eval" / "test_set_kg_value.yml"

ARMS = ["arm0", "arm1", "arm2"]
ARM_LABEL = {"arm0": "retrieval", "arm1": "+SP2", "arm2": "+SP2+SP3"}
MODELS = ["ds", "gpt4o", "gpt54"]  # Sonnet billing-blocked → cross-vendor: deepseek-chat / gpt-4o / gpt-5.4 (frontier)
FAMILIES = ["impact_codelist", "impact_variable", "aggregate", "relationship"]

_CODE_RE = re.compile(r"(?:C\d{3,6}|[A-Z][A-Z0-9]{1,7})\Z")


def fact_present(fact: str, answer: str) -> bool:
    """Code/token-like gold (domain code, var name, C-code) -> word-boundary CASE-SENSITIVE.
    Free-text gold (a codelist name phrase) -> case-insensitive substring."""
    if _CODE_RE.match(fact):
        return re.search(rf"\b{re.escape(fact)}\b", answer) is not None
    return fact.lower() in answer.lower()


def card_present(count: int, answer: str) -> bool:
    return re.search(rf"\b{count}\b", answer) is not None


def load_eval(model: str, arm: str) -> dict | None:
    p = PW / f"kgval_{arm}_{model}.json"
    if not p.exists():
        return None
    data = json.loads(p.read_text())
    return {r["id"]: r for r in data["results"]}


def mean(xs: list[float]) -> float:
    return sum(xs) / len(xs) if xs else float("nan")


def _fmt_delta(d: float) -> str:
    return "   -  " if d != d else f"{d:+5.0%}"


def main() -> int:
    gold = {q["id"]: q for q in yaml.safe_load(TEST_SET.read_text(encoding="utf-8"))}
    fire = {r["id"]: r for r in json.loads((PW / "kgval_fire.json").read_text())}

    # per (model, arm, id) -> metric dict
    cells: dict = {}
    have_models = []
    for model in MODELS:
        arms = {a: load_eval(model, a) for a in ARMS}
        if any(arms[a] is None for a in ARMS):
            print(f"[skip {model}] missing arm files: "
                  f"{[a for a in ARMS if arms[a] is None]}")
            continue
        have_models.append(model)
        for a in ARMS:
            for qid, q in gold.items():
                res = arms[a].get(qid)
                ans = (res or {}).get("answer") or (res or {}).get("answer_preview") or ""
                facts = q.get("expected_facts", [])
                sr = mean([1.0 if fact_present(f, ans) else 0.0 for f in facts]) if facts else float("nan")
                card = (card_present(q["expect_count"], ans)
                        if q.get("card_applies") and q.get("expect_count") is not None else None)
                jr = (res or {}).get("judge_fact_recall")
                cells[(model, a, qid)] = {"set_recall": sr, "card": card, "judge": jr}

    if not have_models:
        print("No complete model found. Run the eval arms first.")
        return 1

    report: dict = {"models": have_models, "by_model": {}}

    for model in have_models:
        print("\n" + "=" * 72)
        print(f"MODEL: {model}")
        print("=" * 72)

        # family x arm table
        def agg(metric: str, fam: str, arm: str, ids=None, model: str = model) -> float:
            pool = ids if ids is not None else [i for i, q in gold.items() if q["category"] == fam]
            vals = []
            for i in pool:
                v = cells[(model, arm, i)][metric]
                if metric == "card":
                    if v is not None:
                        vals.append(1.0 if v else 0.0)
                elif v == v:  # not NaN
                    vals.append(v)
            return mean(vals) if vals else float("nan")

        print(f"\n{'family':<17} {'arm':<11} {'card':>6} {'setR':>6} {'judge':>6}")
        fam_rows = {}
        for fam in FAMILIES:
            for arm in ARMS:
                c, s, j = agg("card", fam, arm), agg("set_recall", fam, arm), agg("judge", fam, arm)
                fam_rows[(fam, arm)] = (c, s, j)
                print(f"{fam:<17} {ARM_LABEL[arm]:<11} "
                      f"{'  -  ' if c != c else f'{c:>5.0%}'} "
                      f"{'  -  ' if s != s else f'{s:>5.0%}'} "
                      f"{'  -  ' if j != j else f'{j:>5.0%}'}")
            print("-" * 48)

        # overall
        for arm in ARMS:
            c = mean([1.0 if cells[(model, arm, i)]["card"] else 0.0
                      for i, q in gold.items() if cells[(model, arm, i)]["card"] is not None])
            s = mean([cells[(model, arm, i)]["set_recall"] for i in gold
                      if cells[(model, arm, i)]["set_recall"] == cells[(model, arm, i)]["set_recall"]])
            j = mean([cells[(model, arm, i)]["judge"] for i in gold
                      if cells[(model, arm, i)]["judge"] is not None])
            print(f"{'ALL':<17} {ARM_LABEL[arm]:<11} {c:>5.0%} {s:>5.0%} {j:>5.0%}")

        # deltas (the headline)
        print("\nDELTAS (percentage points)   ΔSP2=+SP2  ΔSP3=+graph(gates SP4/5)  Δwhole")
        print(f"{'family':<17} {'metric':<6} {'ΔSP2':>7} {'ΔSP3':>7} {'Δwhole':>7}")
        deltas = {}
        for fam in FAMILIES:
            for metric in ("card", "set_recall", "judge"):
                a0 = agg(metric, fam, "arm0")
                a1 = agg(metric, fam, "arm1")
                a2 = agg(metric, fam, "arm2")
                if a0 != a0 and a1 != a1 and a2 != a2:
                    continue
                d_sp2 = (a1 - a0) if (a0 == a0 and a1 == a1) else float("nan")
                d_sp3 = (a2 - a1) if (a1 == a1 and a2 == a2) else float("nan")
                d_all = (a2 - a0) if (a0 == a0 and a2 == a2) else float("nan")
                deltas[(fam, metric)] = (d_sp2, d_sp3, d_all)
                print(f"{fam:<17} {metric:<6} {_fmt_delta(d_sp2):>7} {_fmt_delta(d_sp3):>7} {_fmt_delta(d_all):>7}")

        # fire-conditional ΔSP3: only questions where the graph channel actually fired
        fired = [i for i in gold if fire.get(i, {}).get("fired_sp3")]
        print(f"\nFIRE-CONDITIONAL ΔSP3 (only the {len(fired)} questions where graph fired):")
        for metric in ("card", "set_recall", "judge"):
            a1 = agg(metric, "_fired", "arm1", ids=fired)
            a2 = agg(metric, "_fired", "arm2", ids=fired)
            if a1 == a1 and a2 == a2:
                print(f"  {metric:<10} arm1={a1:.0%} -> arm2={a2:.0%}  (ΔSP3={a2-a1:+.0%})")

        # SP3-UNIQUE: graph fired AND SP2 silent — the only place SP3 can add value SP2 cannot
        uniq = [i for i in gold if fire.get(i, {}).get("fired_sp3") and not fire.get(i, {}).get("fired_sp2")]
        print(f"\nSP3-UNIQUE ΔSP3 (graph fired AND SP2 silent — {len(uniq)} q): {uniq}")
        for metric in ("card", "set_recall", "judge"):
            a1 = agg(metric, "_u", "arm1", ids=uniq)
            a2 = agg(metric, "_u", "arm2", ids=uniq)
            if a1 == a1 and a2 == a2:
                print(f"  {metric:<10} arm1={a1:.0%} -> arm2={a2:.0%}  (ΔSP3={a2-a1:+.0%})")

        # turned-green: card 0->1 from arm1 to arm2 (SP3 fixed it) and arm0 to arm2 (KG fixed)
        tg_sp3 = [i for i in gold if cells[(model,'arm1',i)]["card"] is False and cells[(model,'arm2',i)]["card"] is True]
        tg_kg = [i for i in gold if cells[(model,'arm0',i)]["card"] is False and cells[(model,'arm2',i)]["card"] is True]
        print(f"\nTurned-green on cardinality  +SP3 (arm1->arm2): {tg_sp3}")
        print(f"Turned-green on cardinality  whole-KG (arm0->arm2): {tg_kg}")

        report["by_model"][model] = {
            "family_arm": {f"{f}|{a}": fam_rows[(f, a)] for (f, a) in fam_rows},
            "deltas": {f"{f}|{m}": deltas[(f, m)] for (f, m) in deltas},
            "fired_sp3_ids": fired,
            "turned_green_sp3": tg_sp3, "turned_green_kg": tg_kg,
        }

    (PW / "kgval_analysis.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nSaved {PW / 'kgval_analysis.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
