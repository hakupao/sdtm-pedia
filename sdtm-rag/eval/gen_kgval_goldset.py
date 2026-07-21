"""KG-value eval — deterministic gold-set generator (writer-blind foundation).

Selects HELD-OUT entities per family and computes ground-truth answers straight from
MetaStore / GraphEngine (the production indices). The gold here is later re-derived
INDEPENDENTLY from raw meta.yaml by a reviewer agent (SP1-reconcile pattern) so a
MetaStore bug cannot make gold and the ON-arm injection wrong-consistent.

Output: eval/kgval_candidates.json
  - "candidates": full records (subject + gold count + gold items + sources) — for
    assembly + the independent reviewer.
  - "writer_view": blinded subset ({family, ref, subject, subject_name, threshold}) —
    the ONLY thing the blind question-writer agents receive (no gold leaked).

Deterministic: fixed sort keys + evenly-spaced rank picks (no RNG) → reproducible.
Run from sdtm-rag/:  .venv/bin/python eval/gen_kgval_goldset.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from server.config import settings  # noqa: E402
from server.graph_engine import GraphEngine  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402

# Entities already used in SP3 test set / probes / 140q (q103 TAETORD, q104 VISITDY).
# Question SUBJECTS must avoid these (anti-overfitting held-out). True ANSWERS may still
# contain them (e.g. the most-shared codelist IS C66742) — that is unavoidable and fine.
HELD_OUT_CODELISTS = {"C66742", "C66728", "C66767"}
HELD_OUT_VARIABLES = {
    "TAETORD", "EPOCH", "AESER", "AGE", "VISITDY",
    # universal ID vars: in (nearly) all 63 domains → "all domains" is guessable, boring
    "STUDYID", "DOMAIN", "USUBJID", "SUBJID",
}
HELD_OUT_DOMAINS = {"AE", "CM", "DM"}

N_PER_FAMILY = 10


def _spread(items: list, k: int) -> list:
    """Pick k items evenly spaced across a sorted list (deterministic, keeps the
    full high→low range so gold cardinalities span easy→hard)."""
    if len(items) <= k:
        return list(items)
    step = (len(items) - 1) / (k - 1)
    return [items[round(i * step)] for i in range(k)]


def build(store: MetaStore, eng: GraphEngine) -> list[dict]:
    cands: list[dict] = []

    # ── impact_codelist (10): codelist → affected domains + variables (SP3-only) ──
    cl_rows = []
    for code in sorted(store.known_ctcodes):
        if code in HELD_OUT_CODELISTS:
            continue
        doms = store.domains_for_codelist(code)
        vars_ = store.variables_for_codelist(code)
        if len(doms) >= 2:  # need non-trivial reach for a discriminating impact question
            cl_rows.append((code, doms, vars_))
    cl_rows.sort(key=lambda r: (-len(r[1]), r[0]))
    for i, (code, doms, vars_) in enumerate(_spread(cl_rows, N_PER_FAMILY), 1):
        cl = store.codelist(code)
        cands.append({
            "ref": f"ic{i:02d}", "family": "impact_codelist",
            "subject": code, "subject_name": cl["name"] if cl else code,
            "expect_count": len(doms), "expect_kind": "impacted_domains",
            "gold_domains": doms, "gold_variables": vars_,
            "n_variables": len(vars_),
            "expected_facts": doms,  # set-recall checks domain codes appear in answer
            "expected_sources": [cl["termfile"]] if cl and cl.get("termfile") else [],
        })

    # ── impact_variable (10): variable → domains it appears in (SP2/SP3 overlap) ──
    var_rows = []
    for v in sorted(store.known_variables):
        if v in HELD_OUT_VARIABLES:
            continue
        doms = store.domains_for_variable(v)
        if 2 <= len(doms) < store.n_domains:  # multi-domain but not universal
            var_rows.append((v, doms))
    # top-N by domain-spread: in this KB only ~8 variables are widespread (big cliff
    # after the universal/ID vars are held out), so take the highest-cardinality cases
    # for the sharpest OFF-vs-ON contrast rather than an even spread.
    var_rows.sort(key=lambda r: (-len(r[1]), r[0]))
    for i, (v, doms) in enumerate(var_rows[:N_PER_FAMILY], 1):
        attrs = store.variable_attributes(v) or {}
        cands.append({
            "ref": f"iv{i:02d}", "family": "impact_variable",
            "subject": v, "subject_name": attrs.get("label", v),
            "expect_count": len(doms), "expect_kind": "impacted_domains",
            "gold_domains": doms,
            "expected_facts": doms,
            "expected_sources": ["VARIABLE_INDEX.md"],
        })

    # ── aggregate (10): 5 threshold + 5 most-shared ──
    # Thresholds chosen so the gold cardinality is DISTINCT per question (the KB has a
    # cliff: ~24 vars in >=2d, 18 in >=3d, 10 in >=4d, 9 in >=5d, flat 8 for 8..35d, 5 in
    # >=40d). Gold is stored for BOTH the inclusive ("at least N" -> >=N) and strict
    # ("more than N" -> >=N+1) readings; assembly PINS gold to the writer's final wording
    # (the engine itself parses strict/inclusive the same way), so blind phrasing can't
    # silently desync gold. expect_count defaults to the inclusive reading.
    thresholds = [3, 4, 5, 10, 40]
    for i, n in enumerate(thresholds, 1):
        incl = [v for v, _ in eng.variables_in_min_domains(n)]
        strict = [v for v, _ in eng.variables_in_min_domains(n + 1)]
        cands.append({
            "ref": f"ag{i:02d}", "family": "aggregate", "subtype": "threshold",
            "subject": f">={n}", "subject_name": f"variables appearing in {n} or more domains",
            "threshold": n,
            "expect_count": len(incl), "expect_kind": "variables_in_min_domains",
            "gold_variables_inclusive": incl, "gold_variables_strict": strict,
            "expected_facts": incl,  # repinned in assembly to match final wording
            "expected_sources": ["VARIABLE_INDEX.md"],
        })
    top = eng.most_shared_codelists(5)
    top1 = top[0]
    ms_single = [
        "most reused codelist overall",
        "controlled-terminology codelist used by the most variables",
        "single most widely shared codelist across SDTM domains",
    ]
    for i, desc in enumerate(ms_single, 1):
        cands.append({
            "ref": f"ms{i:02d}", "family": "aggregate", "subtype": "most_shared",
            "subject": desc, "subject_name": desc,
            "expect_count": None, "expect_kind": "most_shared_single",
            "gold_answer_code": top1["code"], "gold_answer_name": top1["name"],
            "gold_n_variables": top1["n_variables"], "gold_n_domains": top1["n_domains"],
            "expected_facts": [top1["code"], top1["name"]],
            "expected_sources": ["VARIABLE_INDEX.md"],
        })
    # 2 list-style most-shared (gold = top-k set -> richer set-recall)
    ms_list = [("the three most frequently reused codelists", 3),
               ("several of the most commonly shared codelists", 5)]
    for j, (desc, k) in enumerate(ms_list, 1):
        topk = eng.most_shared_codelists(k)
        codes = [t["code"] for t in topk]
        cands.append({
            "ref": f"ms{3 + j:02d}", "family": "aggregate", "subtype": "most_shared_list",
            "subject": desc, "subject_name": desc, "top_k": k,
            "expect_count": k, "expect_kind": "most_shared_list",
            "gold_codes": codes, "gold_names": [t["name"] for t in topk],
            "expected_facts": codes,
            "expected_sources": ["VARIABLE_INDEX.md"],
        })

    # ── relationship (10): domain → same-class + curated related domains (SP3-only) ──
    # Class-stratified round-robin so the 10 span observation classes (Events /
    # Interventions / Findings / Findings About / Special-Purpose / Trial Design /
    # Relationship) instead of front-loading 5 near-identical Findings domains (all
    # same_class≈29). Within each class, prefer curated-relation-rich domains.
    by_class: dict[str, list[tuple]] = {}
    for d in sorted(store.known_domains):
        if d in HELD_OUT_DOMAINS:
            continue
        sc = store.same_class(d)
        rc = [r["target"] for r in store.relations_curated(d)]
        if not (sc or rc):
            continue
        cls = (store.domain_info(d) or {}).get("class", "?")
        by_class.setdefault(cls, []).append((d, sc, rc))
    for cls in by_class:
        by_class[cls].sort(key=lambda t: (-len(t[2]), -len(t[1]), t[0]))
    classes = sorted(by_class)
    picked: list[tuple] = []
    rank = 0
    while len(picked) < N_PER_FAMILY and rank < max(len(v) for v in by_class.values()):
        for cls in classes:
            if rank < len(by_class[cls]) and len(picked) < N_PER_FAMILY:
                picked.append(by_class[cls][rank])
        rank += 1
    for i, (d, sc, rc) in enumerate(picked, 1):
        info = store.domain_info(d) or {}
        cands.append({
            "ref": f"rl{i:02d}", "family": "relationship",
            "subject": d, "subject_name": info.get("label", d),
            "domain_class": info.get("class"),
            "expect_count": len(sc), "expect_kind": "same_class_domains",
            "gold_same_class": sc, "gold_curated_targets": rc,
            "expected_facts": sorted(set(sc) | set(rc)),
            "expected_sources": [f"domains/{d}/"],
        })

    return cands


def main() -> int:
    store = MetaStore(settings.meta_path)
    eng = GraphEngine(store)
    cands = build(store, eng)

    # blinded writer view — NO gold counts / item sets leaked
    writer_view = []
    for c in cands:
        wv = {"ref": c["ref"], "family": c["family"], "subject": c["subject"],
              "subject_name": c["subject_name"]}
        if "subtype" in c:
            wv["subtype"] = c["subtype"]
        if "threshold" in c:
            wv["threshold"] = c["threshold"]
        if "domain_class" in c:
            wv["domain_class"] = c["domain_class"]
        writer_view.append(wv)

    out = {"n": len(cands), "candidates": cands, "writer_view": writer_view}
    path = Path(__file__).resolve().parent / "kgval_candidates.json"
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    # sanity summary
    from collections import Counter
    fam = Counter(c["family"] for c in cands)
    print(f"Wrote {len(cands)} candidates to {path}")
    for f in ("impact_codelist", "impact_variable", "aggregate", "relationship"):
        print(f"  {f}: {fam[f]}")
    print("\nCardinality ranges (gold count):")
    for f in ("impact_codelist", "impact_variable", "relationship"):
        cnts = [c["expect_count"] for c in cands if c["family"] == f]
        print(f"  {f}: min={min(cnts)} max={max(cnts)} vals={cnts}")
    print("  aggregate thresholds:",
          [(c["threshold"], c["expect_count"]) for c in cands
           if c.get("subtype") == "threshold"])
    print("  most_shared gold:",
          sorted({c["gold_answer_code"] for c in cands if c.get("subtype") == "most_shared"}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
