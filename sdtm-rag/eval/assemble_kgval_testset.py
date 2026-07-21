"""KG-value eval — assemble test_set_kg_value.yml from blind questions + gold.

Joins: kgval_candidates.json (deterministic gold, reconciled) + the 4 blind-authored
question files + kgval_review.json (independent reviewer fixes). Emits a self-contained
gold test set. Aggregate-threshold gold is PINNED to each question's final wording using
the SAME strict/inclusive parse the GraphAnswerer engine uses, so gold == what the ON arm
would inject (no silent desync from blind phrasing).

Run from sdtm-rag/ AFTER the authoring + review agents have written their files:
  .venv/bin/python eval/assemble_kgval_testset.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
EVAL = ROOT / "eval"

AUTHORED = {
    "impact_codelist": EVAL / "kgval_authored_impact_codelist.json",
    "impact_variable": EVAL / "kgval_authored_impact_variable.json",
    "aggregate": EVAL / "kgval_authored_aggregate.json",
    "relationship": EVAL / "kgval_authored_relationship.json",
}
ORDER = ([f"ic{i:02d}" for i in range(1, 11)] + [f"iv{i:02d}" for i in range(1, 11)]
         + [f"ag{i:02d}" for i in range(1, 6)] + [f"ms{i:02d}" for i in range(1, 6)]
         + [f"rl{i:02d}" for i in range(1, 11)])


def pin_threshold(question: str, cand: dict) -> tuple[list[str], int]:
    """Match the engine: first number + strict(more than/greater than/over)/inclusive."""
    ql = question.lower()
    m = re.search(r"\b(\d{1,3})\b", question)
    n = int(m.group(1)) if m else cand["threshold"]
    if n != cand["threshold"]:
        print(f"  WARN {cand['ref']}: question number {n} != intended {cand['threshold']}")
    strict = "more than" in ql or "greater than" in ql or "over " in ql
    if strict:
        return cand["gold_variables_strict"], len(cand["gold_variables_strict"])
    return cand["gold_variables_inclusive"], len(cand["gold_variables_inclusive"])


def main() -> int:
    cands = {c["ref"]: c for c in json.loads((EVAL / "kgval_candidates.json").read_text())["candidates"]}

    questions: dict[str, str] = {}
    for path in AUTHORED.values():
        for row in json.loads(path.read_text()):
            questions[row["ref"]] = row["question"]

    review_path = EVAL / "kgval_review.json"
    review: dict[str, dict] = {}
    if review_path.exists():
        for v in json.loads(review_path.read_text())["verdicts"]:
            review[v["ref"]] = v
        n_fixed = sum(1 for v in review.values() if not v["ok"])
        print(f"Review loaded: {len(review)} verdicts, {n_fixed} flagged (using suggested rephrasings)")
    else:
        print("WARN: no kgval_review.json — assembling from raw authored questions")

    missing = [r for r in ORDER if r not in questions]
    if missing:
        print(f"ERROR: missing authored questions for {missing}")
        return 1

    entries = []
    for ref in ORDER:
        c = cands[ref]
        q = questions[ref]
        rv = review.get(ref)
        if rv and not rv["ok"] and rv.get("suggested_question"):
            q = rv["suggested_question"]  # apply independent reviewer's natural fix

        e: dict = {"id": ref, "category": c["family"], "question": q}
        fam = c["family"]
        if fam in ("impact_codelist", "impact_variable"):
            e["expected_facts"] = c["gold_domains"]
            e["expect_count"] = c["expect_count"]
            e["card_applies"] = True
        elif c.get("subtype") == "threshold":
            facts, cnt = pin_threshold(q, c)
            e["expected_facts"] = sorted(facts)
            e["expect_count"] = cnt
            e["card_applies"] = True
            e["subtype"] = "threshold"
        elif c.get("subtype") == "most_shared":
            e["expected_facts"] = [c["gold_answer_code"], c["gold_answer_name"]]
            e["expect_count"] = None
            e["card_applies"] = False
            e["subtype"] = "most_shared"
        elif c.get("subtype") == "most_shared_list":
            e["expected_facts"] = c["gold_codes"]
            e["expect_count"] = c["top_k"]
            e["card_applies"] = False
            e["subtype"] = "most_shared_list"
        elif fam == "relationship":
            e["expected_facts"] = sorted(set(c["gold_same_class"]) | set(c["gold_curated_targets"]))
            # cardinality skipped: "how many relationships" is ambiguous (same_class vs curated)
            e["expect_count"] = len(c["gold_same_class"])
            e["card_applies"] = False
        e["expected_sources"] = c.get("expected_sources", [])
        entries.append(e)

    header = (
        "# eval/test_set_kg_value.yml — KG-value 3-arm eval (40 q, 4 families)\n"
        "# Blind-authored (4 family-writer agents, no access to graph_answer/engine source),\n"
        "# gold derived deterministically from meta.yaml (eval/gen_kgval_goldset.py),\n"
        "# reconciled via an independent raw-yaml path (eval/reconcile_kgval_gold.py),\n"
        "# reviewed by an independent scientist agent (Rule D). expected_facts = gold item\n"
        "# set for deterministic set-recall (word-boundary, case-sensitive in the analyzer);\n"
        "# expect_count + card_applies drive the cardinality metric. See KG_VALUE_EVAL_PLAN.md.\n"
    )
    out = EVAL / "test_set_kg_value.yml"
    out.write_text(header + yaml.safe_dump(entries, sort_keys=False, allow_unicode=True,
                                           default_flow_style=False, width=1000),
                   encoding="utf-8")
    print(f"Wrote {len(entries)} questions to {out}")
    card_n = sum(1 for e in entries if e.get("card_applies"))
    print(f"  cardinality-metric applies to {card_n}/40")
    return 0


if __name__ == "__main__":
    sys.exit(main())
