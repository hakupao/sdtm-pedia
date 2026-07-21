"""SP3 in-memory graph layer over the SP1 meta.yaml / SP2 MetaStore.

Pure Python, no networkx (that is the swappable backend's job). GraphEngine exposes the
high-level relationship/impact/aggregate query API; it traverses via a GraphBackend
(topology only — node metadata such as names/labels always comes from meta.yaml/MetaStore).
DictBackend implements the backend from MetaStore's reverse indices. A future networkx /
Neo4j backend reimplements only the three primitives; GraphEngine + NL + gate are unchanged.
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable

from server.meta_store import MetaStore

# Edge types (string-typed so a non-dict backend can map them however it likes).
HAS_VARIABLE = "HAS_VARIABLE"   # Domain -> Variable
IN_DOMAIN = "IN_DOMAIN"         # Variable -> Domain
USES_CT = "USES_CT"             # Variable -> Codelist
CT_USED_BY = "CT_USED_BY"       # Codelist -> Variable
CT_IN_DOMAIN = "CT_IN_DOMAIN"   # Codelist -> Domain
BELONGS_TO = "BELONGS_TO"       # Domain -> Class
CLASS_HAS = "CLASS_HAS"         # Class -> Domain
SAME_CLASS = "SAME_CLASS"       # Domain -> Domain
DEFHOME = "DEFHOME"             # Variable -> model file
RELATED_TO = "RELATED_TO"       # Domain -> Domain (curated, LOW fidelity; carries edge_data)


@runtime_checkable
class GraphBackend(Protocol):
    def nodes_of_type(self, ntype: str) -> list[str]: ...
    def out_neighbors(self, node: str, edge_type: str) -> list[str]: ...
    def edge_data(self, src: str, dst: str, edge_type: str) -> dict | None: ...


class DictBackend:
    """GraphBackend backed by MetaStore reverse indices (topology only)."""

    def __init__(self, store: MetaStore):
        self.store = store
        self._classes = sorted(
            {info["class"] for d in store.known_domains
             if (info := store.domain_info(d)) is not None}
        )
        self._class_to_domains: dict[str, list[str]] = {}
        for d in sorted(store.known_domains):
            info = store.domain_info(d)
            assert info is not None, f"known domain {d!r} missing domain_info"
            self._class_to_domains.setdefault(info["class"], []).append(d)

    def nodes_of_type(self, ntype: str) -> list[str]:
        if ntype == "Domain":
            return sorted(self.store.known_domains)
        if ntype == "Variable":
            return sorted(self.store.known_variables)
        if ntype == "Codelist":
            return sorted(self.store.known_ctcodes)
        if ntype == "Class":
            return list(self._classes)
        return []

    def out_neighbors(self, node: str, edge_type: str) -> list[str]:
        s = self.store
        if edge_type == HAS_VARIABLE:
            return s.variables_in_domain(node)
        if edge_type == IN_DOMAIN:
            return s.domains_for_variable(node)
        if edge_type == USES_CT:
            return s.ct_codes_for_variable(node)
        if edge_type == CT_USED_BY:
            return s.variables_for_codelist(node)
        if edge_type == CT_IN_DOMAIN:
            return s.domains_for_codelist(node)
        if edge_type == SAME_CLASS:
            return s.same_class(node)
        if edge_type == BELONGS_TO:
            info = s.domain_info(node)
            return [info["class"]] if info else []
        if edge_type == CLASS_HAS:
            return list(self._class_to_domains.get(node, []))
        if edge_type == DEFHOME:
            f = s.model_defhome(node)
            return [f] if f else []
        if edge_type == RELATED_TO:
            return [r["target"] for r in s.relations_curated(node)]
        return []

    def edge_data(self, src: str, dst: str, edge_type: str) -> dict | None:
        if edge_type == RELATED_TO:
            for r in self.store.relations_curated(src):
                if r["target"] == dst:
                    return r
        return None


class GraphEngine:
    """High-level relationship/impact/aggregate queries over a GraphBackend.

    Topology comes from the backend (swappable); node metadata (names/labels) comes from
    the MetaStore. All methods are case-insensitive at entry and return None/[] for unknown
    entities (never raise)."""

    def __init__(self, store: MetaStore, backend: GraphBackend | None = None):
        self.store = store
        self.backend = backend if backend is not None else DictBackend(store)

    # ── impact / cascade ──
    def impact_of_codelist(self, code: str) -> dict | None:
        cl = self.store.codelist(code)
        if cl is None:
            return None
        c = code.upper()
        domains = sorted(self.backend.out_neighbors(c, CT_IN_DOMAIN))
        variables = sorted(self.backend.out_neighbors(c, CT_USED_BY))
        return {"code": c, "name": cl["name"], "domains": domains, "variables": variables,
                "n_domains": len(domains), "n_variables": len(variables)}

    def impact_of_variable(self, var: str) -> dict | None:
        v = var.upper()
        if v not in self.store.known_variables:
            return None
        domains = sorted(self.backend.out_neighbors(v, IN_DOMAIN))
        return {"var": v, "domains": domains, "n_domains": len(domains)}

    # ── cross-domain aggregates ──
    def variables_in_min_domains(self, n: int) -> list[tuple[str, int]]:
        out: list[tuple[str, int]] = []
        for v in self.backend.nodes_of_type("Variable"):
            cnt = len(self.backend.out_neighbors(v, IN_DOMAIN))
            if cnt >= n:
                out.append((v, cnt))
        out.sort(key=lambda t: (-t[1], t[0]))
        return out

    def domains_in_class(self, cls: str) -> list[str]:
        canon = {c.casefold(): c for c in self.backend.nodes_of_type("Class")}.get(cls.casefold())
        if canon is None:
            return []
        return sorted(self.backend.out_neighbors(canon, CLASS_HAS))

    def class_sizes(self) -> dict[str, int]:
        return {c: len(self.backend.out_neighbors(c, CLASS_HAS))
                for c in self.backend.nodes_of_type("Class")}

    def most_shared_codelists(self, k: int = 10) -> list[dict]:
        rows: list[dict[str, int | str]] = []
        for c in self.backend.nodes_of_type("Codelist"):
            nv = len(self.backend.out_neighbors(c, CT_USED_BY))
            nd = len(self.backend.out_neighbors(c, CT_IN_DOMAIN))
            cl = self.store.codelist(c)
            rows.append({"code": c, "name": cl["name"] if cl else c,
                         "n_variables": nv, "n_domains": nd})
        rows.sort(key=lambda r: (-int(r["n_variables"]), str(r["code"])))
        return rows[:k]

    # ── structural neighborhood / co-usage ──
    def same_class_domains(self, dom: str) -> list[str]:
        return self.backend.out_neighbors(dom.upper(), SAME_CLASS)

    def codelist_co_users(self, var: str) -> dict[str, dict]:
        v = var.upper()
        out: dict[str, dict] = {}
        for code in self.backend.out_neighbors(v, USES_CT):
            others = [x for x in self.backend.out_neighbors(code, CT_USED_BY) if x != v]
            cl = self.store.codelist(code)
            out[code] = {"name": cl["name"] if cl else code, "others": sorted(others)}
        return out

    def domain_relations(self, dom: str) -> dict | None:
        d = dom.upper()
        if d not in self.store.known_domains:
            return None
        curated = []
        for t in self.backend.out_neighbors(d, RELATED_TO):
            ed = self.backend.edge_data(d, t, RELATED_TO) or {}
            curated.append(ed)
        return {"structural": {"same_class": self.backend.out_neighbors(d, SAME_CLASS)},
                "curated": curated}
