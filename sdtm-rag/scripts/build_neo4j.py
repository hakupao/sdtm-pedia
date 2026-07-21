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

import os
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


# ── import layer (requires the dev-extra neo4j driver + a live local Neo4j) ──

BATCH_SIZE = 500

CONSTRAINTS = [
    "CREATE CONSTRAINT domain_code IF NOT EXISTS FOR (n:Domain) REQUIRE n.code IS UNIQUE",
    "CREATE CONSTRAINT variable_name IF NOT EXISTS FOR (n:Variable) REQUIRE n.name IS UNIQUE",
    "CREATE CONSTRAINT codelist_code IF NOT EXISTS FOR (n:Codelist) REQUIRE n.code IS UNIQUE",
    "CREATE CONSTRAINT class_name IF NOT EXISTS FOR (n:Class) REQUIRE n.name IS UNIQUE",
    "CREATE CONSTRAINT chapter_path IF NOT EXISTS FOR (n:ModelChapter) REQUIRE n.path IS UNIQUE",
]

NODE_CYPHER = {
    "Domain": ("UNWIND $rows AS r CREATE (:Domain {code: r.code, label: r.label, "
               "class: r.class, structure: r.structure, n_variables: r.n_variables})"),
    # r.role 等对 model-only 行不存在 -> Cypher null -> 属性自然缺省, 无需分支
    "Variable": ("UNWIND $rows AS r CREATE (:Variable {name: r.name, label: r.label, "
                 "role: r.role, type: r.type, core: r.core, model_only: r.model_only})"),
    "Codelist": ("UNWIND $rows AS r CREATE (:Codelist {code: r.code, name: r.name, "
                 "extensible: r.extensible, term_count: r.term_count, termfile: r.termfile})"),
    "Class": "UNWIND $rows AS r CREATE (:Class {name: r.name, n_domains: r.n_domains})",
    "ModelChapter": "UNWIND $rows AS r CREATE (:ModelChapter {path: r.path})",
}

EDGE_CYPHER = {
    "HAS_VARIABLE": ("UNWIND $rows AS r MATCH (d:Domain {code: r.domain}) "
                     "MATCH (v:Variable {name: r.var}) "
                     "CREATE (d)-[:HAS_VARIABLE {role: r.role, type: r.type, core: r.core}]->(v)"),
    "USES_CT": ("UNWIND $rows AS r MATCH (v:Variable {name: r.var}) "
                "MATCH (c:Codelist {code: r.code}) "
                "CREATE (v)-[:USES_CT {domains: r.domains}]->(c)"),
    "IN_CLASS": ("UNWIND $rows AS r MATCH (d:Domain {code: r.domain}) "
                 "MATCH (k:Class {name: r.class}) CREATE (d)-[:IN_CLASS]->(k)"),
    "DEFHOME": ("UNWIND $rows AS r MATCH (v:Variable {name: r.var}) "
                "MATCH (m:ModelChapter {path: r.chapter}) CREATE (v)-[:DEFHOME]->(m)"),
    # mechanism 可为 null -> 属性缺省; cookbook 查询用 `r.mechanism IS NULL` 语义
    "RELATED_TO": ("UNWIND $rows AS r MATCH (a:Domain {code: r.src}) "
                   "MATCH (b:Domain {code: r.dst}) "
                   "CREATE (a)-[:RELATED_TO {mechanism: r.mechanism, note: r.note, "
                   "category: r.category, fidelity: r.fidelity, advisory: r.advisory}]->(b)"),
}


def _batches(rows: list[dict], size: int = BATCH_SIZE):
    for i in range(0, len(rows), size):
        yield rows[i:i + size]


def import_graph(driver: Any, graph: Graph) -> dict[str, int]:
    """Wipe + full deterministic rebuild. Idempotent: two runs -> identical
    node/edge sets (Gate 1 snapshot diff proves it).

    Self-verifying: `UNWIND $rows AS r MATCH (...) CREATE (...)` silently
    skips a row when a MATCH fails to bind (e.g. missing endpoint) — no
    error, no warning. So counts[label]/counts[etype] must come from the
    driver's write-summary counters (actually created), not len(rows)
    (rows submitted); a mismatch is raised loud rather than deferred to
    Task 5's reconcile gate.
    """
    counts: dict[str, int] = {}
    with driver.session(database="neo4j") as session:
        session.run("MATCH (n) DETACH DELETE n")          # ~2.6k nodes: single tx fine
        for stmt in CONSTRAINTS:
            session.run(stmt)
        for label, rows in graph["nodes"].items():
            created = 0
            for chunk in _batches(rows):
                result = session.run(NODE_CYPHER[label], rows=chunk)
                created += result.consume().counters.nodes_created
            if created != len(rows):
                raise ValueError(
                    f"node import mismatch for {label}: created={created} "
                    f"expected={len(rows)}"
                )
            counts[label] = created
        for etype, rows in graph["edges"].items():
            created = 0
            for chunk in _batches(rows):
                result = session.run(EDGE_CYPHER[etype], rows=chunk)
                created += result.consume().counters.relationships_created
            if created != len(rows):
                raise ValueError(
                    f"edge import mismatch for {etype}: created={created} "
                    f"expected={len(rows)} (silent drop / missing endpoint?)"
                )
            counts[etype] = created
    return counts


def main() -> None:
    from dotenv import load_dotenv
    from neo4j import GraphDatabase

    root = Path(__file__).resolve().parents[1]            # scripts -> sdtm-rag
    load_dotenv(root / ".env")
    uri = os.environ.get("NEO4J_URI", "bolt://127.0.0.1:7687")
    user = os.environ.get("NEO4J_USER", "neo4j")
    password = os.environ.get("NEO4J_PASSWORD")
    if not password:
        raise SystemExit("NEO4J_PASSWORD missing — add it to sdtm-rag/.env (see deploy/README.md §Neo4j)")

    graph = extract_graph(load_meta(root / "data" / "meta" / "meta.yaml"))
    with GraphDatabase.driver(uri, auth=(user, password)) as driver:
        driver.verify_connectivity()
        counts = import_graph(driver, graph)
    print("imported " + " ".join(f"{k}={v}" for k, v in counts.items()))


if __name__ == "__main__":
    main()
