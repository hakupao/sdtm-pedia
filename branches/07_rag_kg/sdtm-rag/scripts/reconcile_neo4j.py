"""Independent reconciliation for the SP4 Neo4j exploration layer (Gate 1).

Deliberately does NOT reuse the importer's traversal: expected values are
re-derived from a raw yaml.safe_load of data/meta/meta.yaml with its own code
shapes (set/dict comprehensions), then compared against the live Neo4j via
read-only driver queries. Rule A lane: N=9 stratified entity neighborhoods
(3 Domain / 3 Variable / 2 Codelist / 1 Class, seeded RNG) compared edge-by-edge,
plus 2 fixed anchor checks (Domain:AE RELATED_TO, Codelist:C66742 users) that
guarantee non-empty positive-membership coverage on the two sparsest edge types
regardless of what the random sample draws.

Honest disclosure (reconcile_meta.py discipline): both sides ultimately trace
to meta.yaml — this breaks *code-path* tautology (importer bug classes: dropped
rows, wrong direction, attr mixups, silent MATCH misses), not source error.
Source-vs-KB truth was already gated by SP1 reconcile_meta.py.

Usage:
  .venv/bin/python scripts/reconcile_neo4j.py                 # full gate, exit 0/1
  .venv/bin/python scripts/reconcile_neo4j.py --snapshot F    # canonical full-graph dump
"""

from __future__ import annotations

import os
import random
import sys
from pathlib import Path

import yaml
from dotenv import load_dotenv
from neo4j import GraphDatabase

SEED = 20260708


def _load(meta_path: Path) -> tuple[dict, list[dict]]:
    meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
    real = [d for d in meta["domains"] if d["counts_toward_63"]]
    return meta, real


def expected_from_yaml(meta_path: Path) -> dict:
    meta, real = _load(meta_path)
    ig_vars = {v["name"] for d in real for v in d["variables"]}
    model_only = set(meta["model_defhome"]) - ig_vars
    pairs = {(v["name"], c) for d in real for v in d["variables"] for c in v["ct_codes"]}

    def domain_nbhd(code: str) -> dict:
        d = next(x for x in real if x["domain"] == code)
        return {
            "props": (d["label"], d["class"], d["structure"], len(d["variables"])),
            "has_variable": {(v["name"], v["role"], v["type"], v["core"]) for v in d["variables"]},
            "in_class": d["class"],
            "related_to": {(r["target"], r["mechanism"], r["category"], r["note"], r["fidelity"])
                           for r in d["relations_curated"]},
        }

    def variable_nbhd(name: str) -> dict:
        doms = {d["domain"] for d in real for v in d["variables"] if v["name"] == name}
        cts = {(c, tuple(sorted(d["domain"] for d in real
                                for v in d["variables"]
                                if v["name"] == name and c in v["ct_codes"])))
               for d2 in real for v2 in d2["variables"] if v2["name"] == name
               for c in v2["ct_codes"]}
        return {"domains": doms, "uses_ct": cts,
                "defhome": meta["model_defhome"].get(name)}

    def codelist_nbhd(code: str) -> dict:
        c = next(x for x in meta["codelists"] if x["ct_code"] == code)
        return {"props": (c["name"], c["extensible"], c["term_count"], c["termfile"]),
                "users": {var for (var, ct) in pairs if ct == code}}

    def class_nbhd(name: str) -> dict:
        doms = {d["domain"] for d in real if d["class"] == name}
        return {"n_domains": len(doms), "domains": doms}

    return {
        "node_counts": {"Domain": len(real), "Variable": len(ig_vars | model_only),
                        "Codelist": len(meta["codelists"]),
                        "Class": len({d["class"] for d in real}),
                        "ModelChapter": len(set(meta["model_defhome"].values()))},
        "edge_counts": {"HAS_VARIABLE": sum(len(d["variables"]) for d in real),
                        "USES_CT": len(pairs), "IN_CLASS": len(real),
                        "DEFHOME": len(meta["model_defhome"]),
                        "RELATED_TO": sum(len(d["relations_curated"]) for d in real)},
        "real_domains": sorted(d["domain"] for d in real),
        "ig_vars": sorted(ig_vars), "codelist_codes": sorted(c["ct_code"] for c in meta["codelists"]),
        "classes": sorted({d["class"] for d in real}),
        "domain_nbhd": domain_nbhd, "variable_nbhd": variable_nbhd,
        "codelist_nbhd": codelist_nbhd, "class_nbhd": class_nbhd,
    }


def _driver():
    root = Path(__file__).resolve().parents[1]
    load_dotenv(root / ".env")
    password = os.environ.get("NEO4J_PASSWORD")
    if not password:
        raise SystemExit("NEO4J_PASSWORD missing in sdtm-rag/.env")
    return GraphDatabase.driver(os.environ.get("NEO4J_URI", "bolt://127.0.0.1:7687"),
                                auth=(os.environ.get("NEO4J_USER", "neo4j"), password))


def _rows(session, cypher: str, **params) -> list:
    return [r.data() for r in session.run(cypher, **params)]


def reconcile(meta_path: Path) -> list[dict]:
    exp = expected_from_yaml(meta_path)
    report: list[dict] = []

    def check(name, expected, actual):
        report.append({"check": name, "expected": expected, "actual": actual,
                       "ok": expected == actual})

    with _driver() as driver, driver.session(database="neo4j") as s:
        got_nodes = {r["label"]: r["n"] for r in _rows(
            s, "MATCH (n) RETURN labels(n)[0] AS label, count(*) AS n")}
        got_edges = {r["t"]: r["n"] for r in _rows(
            s, "MATCH ()-[r]->() RETURN type(r) AS t, count(*) AS n")}
        for label, n in exp["node_counts"].items():
            check(f"nodes:{label}", n, got_nodes.get(label, 0))
        check("nodes:no_extra_labels", sorted(exp["node_counts"]), sorted(got_nodes))
        for etype, n in exp["edge_counts"].items():
            check(f"edges:{etype}", n, got_edges.get(etype, 0))
        check("edges:no_extra_types", sorted(exp["edge_counts"]), sorted(got_edges))

        # Rule A lane — N=9 stratified neighborhoods, edge-by-edge.
        rng = random.Random(SEED)
        for code in rng.sample(exp["real_domains"], 3):
            e = exp["domain_nbhd"](code)
            props = _rows(s, "MATCH (d:Domain {code:$c}) RETURN d.label AS l, d.class AS k, "
                             "d.structure AS st, d.n_variables AS nv", c=code)[0]
            check(f"nbhd:Domain:{code}:props", e["props"],
                  (props["l"], props["k"], props["st"], props["nv"]))
            hv = {(r["v"], r["role"], r["type"], r["core"]) for r in _rows(
                s, "MATCH (d:Domain {code:$c})-[h:HAS_VARIABLE]->(v:Variable) "
                   "RETURN v.name AS v, h.role AS role, h.type AS type, h.core AS core", c=code)}
            check(f"nbhd:Domain:{code}:HAS_VARIABLE", e["has_variable"], hv)
            k = _rows(s, "MATCH (d:Domain {code:$c})-[:IN_CLASS]->(k:Class) RETURN k.name AS k", c=code)
            check(f"nbhd:Domain:{code}:IN_CLASS", e["in_class"], k[0]["k"] if k else None)
            rel = {(r["t"], r["m"], r["cat"], r["note"], r["f"]) for r in _rows(
                s, "MATCH (d:Domain {code:$c})-[r:RELATED_TO]->(b:Domain) RETURN b.code AS t, "
                   "r.mechanism AS m, r.category AS cat, r.note AS note, r.fidelity AS f", c=code)}
            check(f"nbhd:Domain:{code}:RELATED_TO", e["related_to"], rel)
        for name in rng.sample(exp["ig_vars"], 3):
            e = exp["variable_nbhd"](name)
            doms = {r["d"] for r in _rows(
                s, "MATCH (d:Domain)-[:HAS_VARIABLE]->(v:Variable {name:$n}) RETURN d.code AS d", n=name)}
            check(f"nbhd:Variable:{name}:domains", e["domains"], doms)
            cts = {(r["c"], tuple(r["ds"])) for r in _rows(
                s, "MATCH (v:Variable {name:$n})-[u:USES_CT]->(c:Codelist) "
                   "RETURN c.code AS c, u.domains AS ds", n=name)}
            check(f"nbhd:Variable:{name}:USES_CT", e["uses_ct"], cts)
            dh = _rows(s, "MATCH (v:Variable {name:$n})-[:DEFHOME]->(m:ModelChapter) "
                          "RETURN m.path AS p", n=name)
            check(f"nbhd:Variable:{name}:DEFHOME", e["defhome"], dh[0]["p"] if dh else None)
        for code in rng.sample(exp["codelist_codes"], 2):
            e = exp["codelist_nbhd"](code)
            props = _rows(s, "MATCH (c:Codelist {code:$c}) RETURN c.name AS n, c.extensible AS x, "
                             "c.term_count AS tc, c.termfile AS tf", c=code)[0]
            check(f"nbhd:Codelist:{code}:props", e["props"],
                  (props["n"], props["x"], props["tc"], props["tf"]))
            users = {r["v"] for r in _rows(
                s, "MATCH (v:Variable)-[:USES_CT]->(c:Codelist {code:$c}) RETURN v.name AS v", c=code)}
            check(f"nbhd:Codelist:{code}:users", e["users"], users)
        for name in rng.sample(exp["classes"], 1):
            e = exp["class_nbhd"](name)
            doms = {r["d"] for r in _rows(
                s, "MATCH (d:Domain)-[:IN_CLASS]->(k:Class {name:$n}) RETURN d.code AS d", n=name)}
            check(f"nbhd:Class:{name}:domains", e["domains"], doms)
            nd = _rows(s, "MATCH (k:Class {name:$n}) RETURN k.n_domains AS nd", n=name)[0]["nd"]
            check(f"nbhd:Class:{name}:n_domains", e["n_domains"], nd)

        # Fixed anchors (not random) — guarantee non-empty positive-membership
        # coverage on the two edge types the N=9 sample happened to land on
        # empty-set comparisons for. Reuse the same expected_from_yaml
        # derivations and Cypher patterns as the loops above.
        ae_related = exp["domain_nbhd"]("AE")["related_to"]
        rel_ae = {(r["t"], r["m"], r["cat"], r["note"], r["f"]) for r in _rows(
            s, "MATCH (d:Domain {code:$c})-[r:RELATED_TO]->(b:Domain) RETURN b.code AS t, "
               "r.mechanism AS m, r.category AS cat, r.note AS note, r.fidelity AS f", c="AE")}
        check("anchor:Domain:AE:RELATED_TO", ae_related, rel_ae)

        c66742_users = exp["codelist_nbhd"]("C66742")["users"]
        users_c66742 = {r["v"] for r in _rows(
            s, "MATCH (v:Variable)-[:USES_CT]->(c:Codelist {code:$c}) RETURN v.name AS v",
            c="C66742")}
        check("anchor:Codelist:C66742:users", c66742_users, users_c66742)
    return report


def snapshot(out_path: Path) -> None:
    """Canonical full-graph dump (sorted lines) — run after each of two builds,
    byte-diff proves idempotency (spec §2)."""
    lines: list[str] = []
    with _driver() as driver, driver.session(database="neo4j") as s:
        for r in _rows(s, "MATCH (n) RETURN labels(n)[0] AS label, properties(n) AS p"):
            props = ";".join(f"{k}={r['p'][k]!r}" for k in sorted(r["p"]))
            lines.append(f"NODE|{r['label']}|{props}")
        for r in _rows(s, "MATCH (a)-[e]->(b) RETURN labels(a)[0] AS la, properties(a) AS pa, "
                          "type(e) AS t, properties(e) AS pe, labels(b)[0] AS lb, properties(b) AS pb"):
            # assumes node identifiers are unique across labels (Domain code / Variable name /
            # Codelist code / Class name / ModelChapter path don't collide in this dataset);
            # used only for the idempotency byte-diff, not the counts reconcile
            key = lambda lab, p: p.get("code") or p.get("name") or p.get("path")  # noqa: E731
            props = ";".join(f"{k}={r['pe'][k]!r}" for k in sorted(r["pe"]))
            lines.append(f"EDGE|{r['t']}|{key(r['la'], r['pa'])}->{key(r['lb'], r['pb'])}|{props}")
    out_path.write_text("\n".join(sorted(lines)) + "\n", encoding="utf-8")
    print(f"wrote {out_path} ({len(lines)} lines)")


def main() -> None:
    here = Path(__file__).resolve()
    meta_path = here.parents[1] / "data" / "meta" / "meta.yaml"
    if "--snapshot" in sys.argv:
        snapshot(Path(sys.argv[sys.argv.index("--snapshot") + 1]))
        return
    report = reconcile(meta_path)
    for c in report:
        flag = "OK " if c["ok"] else "FAIL"
        exp_s, act_s = str(c["expected"]), str(c["actual"])
        if len(exp_s) > 120:            # 邻域集合太长, 摘要化输出
            exp_s, act_s = f"<set of {len(c['expected'])}>", f"<set of {len(c['actual'])}>"
        print(f"[{flag}] {c['check']}: expected={exp_s} actual={act_s}")
    n_fail = sum(not c["ok"] for c in report)
    print(f"{len(report) - n_fail}/{len(report)} checks passed")
    if n_fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
