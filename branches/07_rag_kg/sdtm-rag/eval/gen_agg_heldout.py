"""AGG held-out set builder. Two modes:
  --candidates   emit agg_heldout_candidates.json (information-need cards for the
                 blind writers; NO trigger vocabulary, NO kgval questions)
  --assemble Q.json
                 take writer output (ref -> question wording), re-pin gold to the final
                 wording (strict vs inclusive), write test_set_agg_heldout.yml +
                 test_set_agg_e2e.yml (heldout + kgval aggregate regression rows).

The strict/inclusive wording classifier here is DELIBERATELY separate code from
server/aggregate_answer.py (no import) so a detection-regex bug cannot silently
propagate into gold. Anti-overfitting: thresholds differ from kgval's [3,4,5,10,40].
Run: .venv/bin/python eval/gen_agg_heldout.py --candidates
     .venv/bin/python eval/gen_agg_heldout.py --assemble eval/agg_heldout_authored.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from server.config import settings  # noqa: E402
from server.graph_engine import GraphEngine  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402

CAND = ROOT / "eval" / "agg_heldout_candidates.json"
HELDOUT = ROOT / "eval" / "test_set_agg_heldout.yml"
E2E = ROOT / "eval" / "test_set_agg_e2e.yml"
KGVAL = ROOT / "eval" / "test_set_kg_value.yml"

# held-out thresholds — disjoint from kgval's [3, 4, 5, 10, 40]
THRESHOLDS = [2, 6, 9, 12, 18, 25, 30, 38]

SUPERLATIVE_CARDS = [
    ("as01", "the single codelist that is attached to the largest number of variables", 1),
    ("as02", "the codelist reused across the widest spread of SDTM domains", 1),
    ("as03", "which controlled-terminology set gets recycled most often between variables", 1),
    ("as04", "the top few codelists ranked by how many variables draw on them", 5),
    ("as05", "the three codelists shared by the greatest count of variables", 3),
    ("as06", "the four most heavily reused codelists in the standard", 4),
    ("as07", "which codelist would you call the workhorse — used by more variables than any other", 1),
    ("as08", "the champion codelist by variable usage", 1),
]

_STRICT_WORDS = re.compile(
    r"\b(?<!no )(?<!not )(more than|greater than|over|exceed)", re.IGNORECASE)


def build_candidates() -> None:
    eng = GraphEngine(MetaStore(settings.meta_path))
    cards = []
    for i, n in enumerate(THRESHOLDS, 1):
        cards.append({
            "ref": f"ah{i:02d}", "subtype": "threshold", "threshold": n,
            "need": (f"which SDTM variables occur in {n} SDTM domains or in even more "
                     f"domains than that (express the quantity requirement in your own "
                     f"natural English)"),
        })
    for ref, need, k in SUPERLATIVE_CARDS:
        cards.append({"ref": ref, "subtype": "superlative", "top_k": k, "need": need})
    # gold snapshots stored alongside so --assemble never re-reads a changed KB silently
    for c in cards:
        if c["subtype"] == "threshold":
            n = c["threshold"]
            c["gold_inclusive"] = [v for v, _ in eng.variables_in_min_domains(n)]
            c["gold_strict"] = [v for v, _ in eng.variables_in_min_domains(n + 1)]
        else:
            top = eng.most_shared_codelists(c["top_k"])
            c["gold_codes"] = [t["code"] for t in top]
            c["gold_names"] = [t["name"] for t in top]
    CAND.write_text(json.dumps(cards, indent=2), encoding="utf-8")
    print(f"Wrote {len(cards)} candidate cards -> {CAND}")


def assemble(authored_path: str) -> None:
    authored = json.loads(Path(authored_path).read_text())  # {ref: question}
    cards = {c["ref"]: c for c in json.loads(CAND.read_text())}
    rows = []
    for ref, question in sorted(authored.items()):
        c = cards[ref]
        if c["subtype"] == "threshold":
            strict = bool(_STRICT_WORDS.search(question))
            gold = c["gold_strict"] if strict else c["gold_inclusive"]
            rows.append({
                "id": ref, "category": "aggregate_threshold", "question": question,
                "expected_facts": gold, "expect_count": len(gold),
                "card_applies": True,
                "gold_reading": "strict" if strict else "inclusive",
            })
        else:
            rows.append({
                "id": ref, "category": "aggregate_superlative", "question": question,
                "expected_facts": c["gold_codes"][:c["top_k"]],
                "expect_count": None, "card_applies": False,
            })
    HELDOUT.write_text(yaml.safe_dump(rows, sort_keys=False, allow_unicode=True),
                       encoding="utf-8")
    print(f"Wrote {len(rows)} held-out questions -> {HELDOUT}")

    kg = yaml.safe_load(KGVAL.read_text())
    reg = [dict(q, regression=True) for q in kg
           if q["id"].startswith(("ag", "ms")) and q["category"] == "aggregate"]
    E2E.write_text(yaml.safe_dump(rows + reg, sort_keys=False, allow_unicode=True),
                   encoding="utf-8")
    print(f"Wrote {len(rows) + len(reg)} e2e questions -> {E2E}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--candidates", action="store_true")
    p.add_argument("--assemble", metavar="AUTHORED_JSON")
    a = p.parse_args()
    if a.candidates:
        build_candidates()
    elif a.assemble:
        assemble(a.assemble)
    else:
        p.print_help()
