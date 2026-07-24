"""Build a self-contained interactive SDTM knowledge-graph viewer (single HTML).

Source of truth: data/meta/meta.yaml (via build_neo4j.extract_graph — pure, no
Neo4j). Emits kg_viewer.html: a zero-dependency, offline, shareable page with a
hand-rolled force-directed graph and three scoped, readable views:

  1. 结构总览   Class (8) -> Domain (63)          [IN_CLASS]
  2. 域钻取     a Domain -> its Variables -> Codelists  [HAS_VARIABLE / USES_CT]
  3. 码表影响   a Codelist -> the Domains that use it   [USES_CT aggregated]

Colors: the dataviz reference categorical palette (validated CVD-safe) for the 8
SDTM classes; node TYPE encoded by shape+size (no 9th hue). Light/dark themed.

Run:  cd sdtm-rag && .venv/bin/python scripts/build_kg_viewer.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # scripts -> sdtm-rag
IMPL_PATH = ROOT / "data" / "meta" / "implicit_relations.json"
sys.path.insert(0, str(ROOT / "scripts"))

from build_neo4j import extract_graph, load_meta  # noqa: E402  (pure, no neo4j import)


def build_data() -> dict:
    graph = extract_graph(load_meta(ROOT / "data" / "meta" / "meta.yaml"))
    nodes, edges = graph["nodes"], graph["edges"]

    classes = [{"name": c["name"], "n": c["n_domains"]} for c in nodes["Class"]]
    domains = [
        {"code": d["code"], "label": d["label"], "cls": d["class"],
         "struct": d["structure"], "nv": d["n_variables"]}
        for d in nodes["Domain"]
    ]

    has_var = [[e["domain"], e["var"]] for e in edges["HAS_VARIABLE"]]
    uses_ct = [[e["var"], e["code"], e["domains"]] for e in edges["USES_CT"]]

    # variable label/role/core only for names actually shown (in a domain)
    shown_vars = {v for _, v in has_var} | {u[0] for u in uses_ct}
    var_info: dict[str, dict] = {}
    for v in nodes["Variable"]:
        if v["name"] in shown_vars:
            var_info[v["name"]] = {
                "l": v.get("label", v["name"]),
                "r": v.get("role", ""),
                "c": v.get("core", ""),
            }

    ref_codes = {u[1] for u in uses_ct}
    cls_codes = {
        c["code"]: {"n": c["name"], "e": bool(c["extensible"]), "t": c["term_count"]}
        for c in nodes["Codelist"] if c["code"] in ref_codes
    }

    # curated inter-domain relations (RELATED_TO) for the click-to-inspect panel
    related = [
        [e["src"], e["dst"], e.get("mechanism") or "", e.get("category") or "", e.get("note") or ""]
        for e in edges["RELATED_TO"]
    ]

    implicit = None
    if IMPL_PATH.exists():
        raw = json.loads(IMPL_PATH.read_text(encoding="utf-8"))
        implicit = {"domains": raw["meta"]["domains"],
                    "edges": [e for e in raw["edges"]]}  # 已含 evidence/confidence/kind

    return {
        "classes": classes,
        "domains": domains,
        "vars": var_info,
        "hasVar": has_var,
        "usesCt": uses_ct,
        "clsCodes": cls_codes,
        "related": related,
        "implicit": implicit,
        "counts": {
            "domain": len(domains), "variable": len(nodes["Variable"]),
            "codelist": len(nodes["Codelist"]), "cls": len(classes),
        },
    }


VIEWER_DIR = ROOT / "viewer"


def assemble_template() -> str:
    """Inline viewer/{style.css,app.js} into template.html. Output identical in
    shape to the former inline TEMPLATE (still contains the __DATA__ placeholder)."""
    html = (VIEWER_DIR / "template.html").read_text(encoding="utf-8")
    css = (VIEWER_DIR / "style.css").read_text(encoding="utf-8")
    js = (VIEWER_DIR / "app.js").read_text(encoding="utf-8")
    return html.replace("__STYLE__", css).replace("__APP__", js)


TEMPLATE = assemble_template()   # module attribute: existing tests read this


def main() -> None:
    data = build_data()
    payload = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    payload = payload.replace("<", "\\u003c")
    html = TEMPLATE.replace("__DATA__", payload)
    out = ROOT / "kg_viewer.html"
    out.write_text(html, encoding="utf-8")
    kb = len(html.encode("utf-8")) / 1024
    print(f"wrote {out}  ({kb:.0f} KB)")
    print("counts:", data["counts"])
    print(f"vars shown={len(data['vars'])}  ref codelists={len(data['clsCodes'])}  "
          f"hasVar={len(data['hasVar'])}  usesCt={len(data['usesCt'])}")


if __name__ == "__main__":
    main()
