"""Build the Neo4j exploration layer from data/meta/meta.yaml (SP4).

meta.yaml (SP1, reconcile-verified) is the ONLY source. Production answering
keeps running the in-memory DictBackend; this importer feeds a separate local
Neo4j (bolt://127.0.0.1:7687) for interactive exploration (Browser + cookbook).

Graph model (spec 2026-07-08 §3 + plan deviations D1-D4, data-grounded):
  Nodes: Domain(63, DI stub excluded) / Variable(1541 = 1523 IG + 18
         model-only) / Codelist(1005) / Class(8) / ModelChapter(4)
  Edges: HAS_VARIABLE(1917, per-domain role/type/core on the edge) /
         USES_CT(542 cross-domain union, `domains` list property for
         per-domain precision — C119013/FOCID lesson) / IN_CLASS(63) /
         DEFHOME(59, Variable->ModelChapter) / RELATED_TO(52, advisory)

Production isolation (spec hard constraint): NEVER import this module from
server/ — the neo4j driver lives in the dev extra only. The extract layer
below is pure (no neo4j import) so unit tests run with Neo4j stopped.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

import yaml

Graph = dict[str, dict[str, list[dict[str, Any]]]]


def load_meta(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        meta = yaml.safe_load(fh)
    for key in ("meta_version", "domains", "codelists", "model_defhome"):
        if key not in meta:
            raise ValueError(f"meta.yaml missing top-level key: {key} ({path})")
    return meta


def extract_graph(meta: dict) -> Graph:
    real = [d for d in meta["domains"] if d["counts_toward_63"]]

    domain_nodes = [
        {"code": d["domain"], "label": d["label"], "class": d["class"],
         "structure": d["structure"], "n_variables": len(d["variables"])}
        for d in real
    ]

    # Variable nodes: first-seen attrs in meta["domains"] file order — same
    # semantics as MetaStore._var_attrs, so Browser node props match production.
    var_nodes: dict[str, dict] = {}
    has_variable: list[dict] = []
    ct_domains: dict[tuple[str, str], list[str]] = {}
    class_count: Counter[str] = Counter()
    in_class: list[dict] = []
    related: list[dict] = []
    for d in real:
        class_count[d["class"]] += 1
        in_class.append({"domain": d["domain"], "class": d["class"]})
        for r in d["relations_curated"]:
            related.append({"src": d["domain"], "dst": r["target"],
                            "mechanism": r["mechanism"], "note": r["note"],
                            "category": r["category"], "fidelity": r["fidelity"],
                            "advisory": True})
        for v in d["variables"]:
            if v["name"] not in var_nodes:
                var_nodes[v["name"]] = {
                    "name": v["name"], "label": v["label"], "role": v["role"],
                    "type": v["type"], "core": v["core"], "model_only": False,
                }
            has_variable.append({"domain": d["domain"], "var": v["name"],
                                 "role": v["role"], "type": v["type"], "core": v["core"]})
            for code in v["ct_codes"]:
                ct_domains.setdefault((v["name"], code), []).append(d["domain"])

    codelist_nodes = [
        {"code": c["ct_code"], "name": c["name"], "extensible": c["extensible"],
         "term_count": c["term_count"], "termfile": c["termfile"]}
        for c in meta["codelists"]
    ]
    known_codes = {c["code"] for c in codelist_nodes}
    uses_ct = [{"var": var, "code": code, "domains": sorted(doms)}
               for (var, code), doms in sorted(ct_domains.items())]

    class_nodes = [{"name": name, "n_domains": n}
                   for name, n in sorted(class_count.items())]

    # Deviation D3/D4: defhome targets are model chapter files; 18 of the 59
    # variables are model-level only (no IG domain) — materialize them as
    # Variable nodes flagged model_only so all 59 DEFHOME edges exist.
    chapter_nodes = [{"path": p} for p in sorted(set(meta["model_defhome"].values()))]
    defhome = [{"var": var, "chapter": chap}
               for var, chap in sorted(meta["model_defhome"].items())]
    for row in defhome:
        if row["var"] not in var_nodes:
            var_nodes[row["var"]] = {"name": row["var"], "model_only": True}

    # Loud-fail source validation (reconcile_meta._require spirit).
    real_codes = {d["domain"] for d in real}
    bad_rel = [r for r in related if r["dst"] not in real_codes]
    if bad_rel:
        raise ValueError(f"relations_curated targets not in real domains: {bad_rel}")
    bad_ct = [r for r in uses_ct if r["code"] not in known_codes]
    if bad_ct:
        raise ValueError(f"ct_codes not in codelists section: {bad_ct}")

    return {
        "nodes": {"Domain": domain_nodes,
                  "Variable": sorted(var_nodes.values(), key=lambda v: v["name"]),
                  "Codelist": codelist_nodes, "Class": class_nodes,
                  "ModelChapter": chapter_nodes},
        "edges": {"HAS_VARIABLE": has_variable, "USES_CT": uses_ct,
                  "IN_CLASS": in_class, "DEFHOME": defhome, "RELATED_TO": related},
    }
