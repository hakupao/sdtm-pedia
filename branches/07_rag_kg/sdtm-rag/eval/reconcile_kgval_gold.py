"""KG-value gold INDEPENDENT reconciler (Rule-D deterministic anchor).

Re-derives every gold value in eval/kgval_candidates.json straight from RAW meta.yaml
using a SEPARATE code path — deliberately does NOT import MetaStore / GraphEngine (the
same code the gold-set generator and the ON-arm injection use). Mirrors SP1's
reconcile_meta.py, which caught a systematic spec_loader bug precisely because it did not
reuse the production parser. If gold-gen wiring (or MetaStore) is wrong, gold and the
ON-arm facts would be wrong-CONSISTENT and the eval would silently pass; this catches it.

Run from sdtm-rag/:  .venv/bin/python eval/reconcile_kgval_gold.py
Exit 0 = every gold reconciles; non-zero = mismatch count (printed)."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def load_raw() -> dict:
    raw = yaml.safe_load((ROOT / "data" / "meta" / "meta.yaml").read_text(encoding="utf-8"))
    real = [d for d in raw["domains"] if d.get("counts_toward_63")]
    # var -> set(domains); (domain,var) per ct_code; codelist -> set(vars), set(domains)
    var_domains: dict[str, set[str]] = defaultdict(set)
    code_vars: dict[str, set[str]] = defaultdict(set)
    code_domains: dict[str, set[str]] = defaultdict(set)
    dom_meta: dict[str, dict] = {}
    for d in real:
        dom = d["domain"]
        dom_meta[dom] = d
        for v in d["variables"]:
            name = v["name"]
            var_domains[name].add(dom)
            for code in v["ct_codes"]:
                code_vars[code].add(name)
                code_domains[code].add(dom)
    return {"real": real, "var_domains": var_domains, "code_vars": code_vars,
            "code_domains": code_domains, "dom_meta": dom_meta,
            "codelists": {c["ct_code"]: c for c in raw["codelists"]}}


def vars_in_min(var_domains: dict[str, set[str]], n: int) -> list[str]:
    return sorted(v for v, ds in var_domains.items() if len(ds) >= n)


def most_shared(code_vars: dict[str, set[str]], code_domains: dict[str, set[str]],
                codelists: dict, k: int) -> list[str]:
    rows = [(c, len(code_vars[c]), len(code_domains.get(c, set()))) for c in codelists]
    # MetaStore/GraphEngine rank: n_variables desc, then code asc
    rows.sort(key=lambda r: (-r[1], r[0]))
    return [c for c, _, _ in rows[:k]]


def main() -> int:
    rec = load_raw()
    cands = json.loads((ROOT / "eval" / "kgval_candidates.json").read_text())["candidates"]
    fails: list[str] = []

    def check(ref: str, label: str, got, exp) -> None:
        if got != exp:
            fails.append(f"{ref} {label}: gold={exp!r} recompute={got!r}")

    for c in cands:
        ref, fam = c["ref"], c["family"]
        if fam == "impact_codelist":
            code = c["subject"]
            check(ref, "domains", sorted(rec["code_domains"].get(code, set())), c["gold_domains"])
            check(ref, "variables", sorted(rec["code_vars"].get(code, set())), c["gold_variables"])
            check(ref, "count", len(rec["code_domains"].get(code, set())), c["expect_count"])
        elif fam == "impact_variable":
            v = c["subject"]
            check(ref, "domains", sorted(rec["var_domains"].get(v, set())), c["gold_domains"])
            check(ref, "count", len(rec["var_domains"].get(v, set())), c["expect_count"])
        elif fam == "aggregate" and c.get("subtype") == "threshold":
            # compare as SETS — gold stores count-desc order, reconcile alpha; membership
            # is what matters for set-recall gold.
            n = c["threshold"]
            check(ref, "incl", set(vars_in_min(rec["var_domains"], n)), set(c["gold_variables_inclusive"]))
            check(ref, "strict", set(vars_in_min(rec["var_domains"], n + 1)), set(c["gold_variables_strict"]))
        elif fam == "aggregate" and c.get("subtype") == "most_shared":
            top1 = most_shared(rec["code_vars"], rec["code_domains"], rec["codelists"], 1)[0]
            check(ref, "most_shared_code", top1, c["gold_answer_code"])
        elif fam == "aggregate" and c.get("subtype") == "most_shared_list":
            topk = most_shared(rec["code_vars"], rec["code_domains"], rec["codelists"], c["top_k"])
            check(ref, "top_k_codes", topk, c["gold_codes"])
        elif fam == "relationship":
            d = c["subject"]
            dm = rec["dom_meta"].get(d, {})
            check(ref, "same_class", list(dm.get("same_class", [])), c["gold_same_class"])
            check(ref, "curated", [r["target"] for r in dm.get("relations_curated", [])],
                  c["gold_curated_targets"])

    print(f"Reconciled {len(cands)} candidates against raw meta.yaml (independent path).")
    if fails:
        print(f"\n{len(fails)} MISMATCH:")
        for f in fails:
            print("  " + f)
        return len(fails)
    print("ALL GOLD RECONCILES ✓ (gold-gen wiring + MetaStore verified against raw yaml)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
