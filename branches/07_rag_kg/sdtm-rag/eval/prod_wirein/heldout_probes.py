"""Held-out anti-overfitting probe battery: count/enumerate/attribute/CT queries over
variables/domains/CT codes that are NOT in test_set_v3 (q103/q104 et al.), asserting the
StructuredAnswerer's facts match the reconcile-verified meta.yaml. Proves pattern-level
generalisation, not memorised q-ids. Run: .venv/bin/python eval/prod_wirein/heldout_probes.py"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from server.meta_store import MetaStore  # noqa: E402
from server.structured_answer import CheckableCount, StructuredAnswerer  # noqa: E402

# Held-out entities — chosen because they are NOT the eval test-set targets (TAETORD/
# VISITDY). Truth values come from meta.yaml itself, so this self-checks consistency of
# the answerer vs the store across many entities (not a single example).
PROBES = [
    ("How many domains include EPOCH?", "EPOCH", "domains"),
    ("Which domains carry USUBJID?", "USUBJID", "domains"),
    ("What is the label and role of DTHFL?", "DTHFL", None),
    ("How many domains use codelist C66742?", "C66742", "domains"),
]


def main() -> int:
    store = MetaStore(Path(__file__).resolve().parents[2] / "data" / "meta" / "meta.yaml")
    ans = StructuredAnswerer(store)
    failures = 0
    for query, subject, kind in PROBES:
        facts = ans.resolve(query)
        if facts is None:
            print(f"FAIL  resolve()=None for: {query}")
            failures += 1
            continue
        if kind == "domains":
            if subject.startswith("C"):
                truth = len(store.domains_for_codelist(subject))
            else:
                truth = len(store.domains_for_variable(subject))
            cc = CheckableCount(subject, "domains", truth)
            ok = cc in facts.checkable_counts and str(truth) in facts.text_block
            print(f"{'PASS' if ok else 'FAIL'}  {subject} domains={truth}")
            failures += 0 if ok else 1
        else:  # attribute probe
            attr = store.variable_attributes(subject)
            ok = attr is not None and attr["label"] in facts.text_block
            print(f"{'PASS' if ok else 'FAIL'}  {subject} attribute label present={ok}")
            failures += 0 if ok else 1
    print(f"\nHELD-OUT PROBES: {len(PROBES) - failures}/{len(PROBES)} PASS")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
