"""SP4 Gate 2 — every cookbook query executed via driver, anchored to the
production MetaStore/GraphEngine (equivalence lane; Gate 1 covers raw-yaml lane).
Also fails if a QUERIES entry has drifted from docs/cypher_cookbook.md text.

APOC is not installed on this local Neo4j (`brew install neo4j` bare install has
no plugins — verified via `RETURN apoc.version()` -> Unknown function). Queries 1
and 7 therefore use the plain-Cypher variants (UNWIND/collect(DISTINCT ...)
instead of apoc.coll.sort / apoc.coll.toSet+flatten); see docs/cypher_cookbook.md
"APOC 说明" for the empirical check.

Run: .venv/bin/python eval/prod_wirein/sp4_cookbook_golden.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from server.config import settings  # noqa: E402
from server.graph_engine import GraphEngine  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402

QUERIES: dict[str, str] = {
    # 与 docs/cypher_cookbook.md 各节 cypher 块逐字相同 (drift check 强制)
    "impact": """// 1 影响分析: 改一个 codelist 波及哪些域/变量 (参数化 C 码)
// USES_CT.domains = 该变量实际用此 CT 的域 (逐域精确, 与生产 GraphEngine 一致)
// 本机未装 APOC 插件, 用 collect(DISTINCT dom) 替代 apoc.coll.sort(...) (排序可省, 集合不变)
// :param code => 'C66742'
MATCH (c:Codelist {code: $code})<-[u:USES_CT]-(v:Variable)
UNWIND u.domains AS dom
RETURN c.code AS code, c.name AS codelist,
       count(DISTINCT v) AS n_variables, count(DISTINCT dom) AS n_domains,
       collect(DISTINCT dom) AS domains""",
    "min_domains": """// 2 变量跨域分布: 哪些变量出现在 ≥ N 个域 (参数化阈值)
// :param min => 20
MATCH (d:Domain)-[:HAS_VARIABLE]->(v:Variable)
WITH v.name AS var, count(d) AS n_domains
WHERE n_domains >= $min
RETURN var, n_domains ORDER BY n_domains DESC, var""",
    "same_class": """// 3 same-class 邻域: 与某域同 observation class 的其他域
// :param dom => 'DM'
MATCH (d:Domain {code: $dom})-[:IN_CLASS]->(k:Class)<-[:IN_CLASS]-(o:Domain)
WHERE o.code <> d.code
RETURN k.name AS class, collect(o.code) AS siblings""",
    "co_users": """// 4 codelist co-users: 与某变量共用同一 CT 的其他变量
// :param var => 'AECONTRT'
MATCH (v:Variable {name: $var})-[:USES_CT]->(c:Codelist)<-[:USES_CT]-(o:Variable)
RETURN c.code AS code, c.name AS codelist, count(o) AS n_others
ORDER BY n_others DESC""",
    "class_compass": """// 5 类罗盘: 某 observation class 下全部域 (SP3 因 class 名撞常用词未暴露 NL 的能力, Cypher 里安全)
// :param cls => 'Findings'
MATCH (d:Domain)-[:IN_CLASS]->(k:Class {name: $cls})
RETURN k.name AS class, k.n_domains AS n, collect(d.code) AS domains""",
    "defhome": """// 6 model_defhome 邻接: 某 model 章节定义的全部变量 (model_only=true 的变量只在 SDTM model 出现, 不在任何 IG 域)
// :param chapter => 'model/06_relationship_datasets.md'
MATCH (v:Variable)-[:DEFHOME]->(m:ModelChapter {path: $chapter})
RETURN m.path AS chapter, count(v) AS n, collect(v.name + CASE WHEN v.model_only THEN ' (model-only)' ELSE '' END) AS variables""",
    "most_shared": """// 7 most-shared 排名: 被最多变量共用的 codelist top-K (本机未装 APOC, 用 UNWIND 代替 apoc.coll.flatten/toSet)
// :param k => 5
MATCH (c:Codelist)<-[u:USES_CT]-(v:Variable)
UNWIND u.domains AS dom
WITH c, count(DISTINCT v) AS n_variables, count(DISTINCT dom) AS n_domains
RETURN c.code AS code, c.name AS name, n_variables, n_domains
ORDER BY n_variables DESC, code LIMIT $k""",
}


def main() -> int:
    load_dotenv(ROOT / ".env")
    cookbook = (ROOT / "docs" / "cypher_cookbook.md").read_text(encoding="utf-8")
    store = MetaStore(settings.meta_path)
    engine = GraphEngine(store)
    fails = 0

    def gate(name: str, ok: bool, detail: str) -> None:
        nonlocal fails
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
        fails += 0 if ok else 1

    for name, q in QUERIES.items():
        gate(f"drift:{name}", q.strip() in cookbook, "query text verbatim in cookbook")

    with GraphDatabase.driver(
        os.environ.get("NEO4J_URI", "bolt://127.0.0.1:7687"),
        auth=(os.environ.get("NEO4J_USER", "neo4j"), os.environ["NEO4J_PASSWORD"]),
    ) as driver, driver.session(database="neo4j") as s:
        rec = s.run(QUERIES["impact"], code="C66742").single()
        truth = engine.impact_of_codelist("C66742")
        gate("impact:C66742", (rec["n_variables"], rec["n_domains"])
             == (truth["n_variables"], truth["n_domains"]),
             f"{rec['n_variables']}/{rec['n_domains']} vs engine {truth['n_variables']}/{truth['n_domains']} (期望 123/41)")
        rec2 = s.run(QUERIES["impact"], code="C119013").single()
        t2 = engine.impact_of_codelist("C119013")
        gate("impact:C119013", (rec2["n_variables"], rec2["n_domains"])
             == (t2["n_variables"], t2["n_domains"]),
             f"逐域精确回归 (D2): {rec2['n_variables']}/{rec2['n_domains']} vs engine {t2['n_variables']}/{t2['n_domains']} (期望 1/1 非 1/3)")

        rows = [(r["var"], r["n_domains"]) for r in s.run(QUERIES["min_domains"], min=20)]
        gate("min_domains:20", rows == engine.variables_in_min_domains(20),
             f"{len(rows)} rows vs engine (期望 8)")

        rec = s.run(QUERIES["same_class"], dom="DM").single()
        gate("same_class:DM", sorted(rec["siblings"]) == engine.same_class_domains("DM"),
             f"{sorted(rec['siblings'])} (期望 CO,SE,SM,SV)")

        rows = [(r["code"], r["n_others"]) for r in s.run(QUERIES["co_users"], var="AECONTRT")]
        truth_cu = engine.codelist_co_users("AECONTRT")
        gate("co_users:AECONTRT",
             rows == [(c, len(v["others"])) for c, v in sorted(truth_cu.items())],
             f"{rows} (期望 [('C66742', 122)])")

        rec = s.run(QUERIES["class_compass"], cls="Findings").single()
        gate("class_compass:Findings", sorted(rec["domains"]) == engine.domains_in_class("Findings")
             and rec["n"] == 30, f"n={rec['n']} (期望 30)")

        chap = "model/06_relationship_datasets.md"
        rec = s.run(QUERIES["defhome"], chapter=chap).single()
        truth_dh = sorted(v for v, p in store.model_defhome_map.items() if p == chap)
        got = sorted(x.replace(" (model-only)", "") for x in rec["variables"])
        gate("defhome:ch06", got == truth_dh, f"{rec['n']} vars vs store {len(truth_dh)}")

        rows = [(r["code"], r["n_variables"], r["n_domains"])
                for r in s.run(QUERIES["most_shared"], k=5)]
        truth_ms = [(t["code"], t["n_variables"], t["n_domains"])
                    for t in engine.most_shared_codelists(5)]
        gate("most_shared:top5", rows == truth_ms, f"{rows}")

    print(f"{'ALL PASS' if fails == 0 else f'{fails} FAIL'}")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
