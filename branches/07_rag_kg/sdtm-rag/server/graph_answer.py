"""SP3 graph answer channel: detect relationship/impact/aggregate intent + assemble
authoritative graph facts (and an advisory block for curated relations) for injection.
Conservative by construction: zero hardcoded q-ids/variables; misfire is at worst recall-
additive true facts; correctness of cardinalities is back-stopped by the grounding gate.
Intent vocab is deliberately DISJOINT from SP2's distribution/count vocab (use/include/
which-domains) so plain SP2 queries never trip the graph channel (spec §5.4)."""
from __future__ import annotations

import re

from server.graph_engine import GraphEngine
from server.structured_answer import CheckableCount, StructuredFacts

_VAR_TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9]{1,7}\b")
_CT_TOKEN_RE = re.compile(r"\bC\d{4,6}\b")

# Impact/cascade — distinct from SP2 dist verbs (use/include/appear/carry/share).
_IMPACT_CUES = ("affect", "affects", "affected", "impact", "impacts", "impacted",
                "change", "changes", "changing", "depend", "depends", "depending",
                "cascade", "downstream", "knock-on", "ripple")
# Relationship discovery.
_REL_CUES = ("related to", "relationship", "relationships", "linked", "connected",
             "connection", "associated with", "association")
# Cross-domain aggregate (graph-wide, not SP2 per-entity counts).
_AGG_CUES = ("more than", "at least", "most shared", "most common", "most widely used",
             "in the events class", "in the findings class", "in the interventions class",
             "in the special-purpose class", "in the trial design class",
             "in the relationship class", " class?", " class ")


def detect_graph_intents(query: str) -> set[str]:
    ql = query.lower()
    intents: set[str] = set()
    if any(c in ql for c in _IMPACT_CUES):
        intents.add("impact")
    if any(c in ql for c in _REL_CUES):
        intents.add("relationship")
    if any(c in ql for c in _AGG_CUES):
        intents.add("aggregate")
    return intents


class GraphAnswerer:
    def __init__(self, engine: GraphEngine):
        self.engine = engine
        self.store = engine.store

    def _vars(self, q: str) -> list[str]:
        return [t for t in _VAR_TOKEN_RE.findall(q) if t in self.store.known_variables]

    def _codelists(self, q: str) -> list[str]:
        return [c for c in _CT_TOKEN_RE.findall(q) if c in self.store.known_ctcodes]

    def _domains(self, q: str) -> list[str]:
        ql = q.lower()
        if "domain" not in ql and "sdtm" not in ql:   # SP2-style context guard vs PR/DM collisions
            return []
        return [t for t in _VAR_TOKEN_RE.findall(q) if t in self.store.known_domains]

    def _classes(self, q: str) -> list[str]:
        ql = q.lower()
        return [c for c in self.engine.class_sizes() if c.lower() in ql]

    def resolve(self, query: str) -> StructuredFacts | None:
        intents = detect_graph_intents(query)
        if not intents:
            return None
        lines: list[str] = []
        adv: list[str] = []
        counts: list[CheckableCount] = []

        if "impact" in intents:
            for code in dict.fromkeys(self._codelists(query)):
                imp = self.engine.impact_of_codelist(code)
                if imp:
                    lines.append(
                        f"- Changing codelist **{code}** ({imp['name']}) affects "
                        f"**{imp['n_variables']}** variables across **{imp['n_domains']}** "
                        f"domains: {', '.join(imp['domains'])}.")
                    counts.append(CheckableCount(code, "impacted_domains", imp["n_domains"]))
                    counts.append(CheckableCount(code, "impacted_variables", imp["n_variables"]))
            for var in dict.fromkeys(self._vars(query)):
                imp = self.engine.impact_of_variable(var)
                if imp:
                    lines.append(
                        f"- Changing variable **{var}** affects **{imp['n_domains']}** "
                        f"domains: {', '.join(imp['domains'])}.")
                    counts.append(CheckableCount(var, "impacted_domains", imp["n_domains"]))

        if "relationship" in intents:
            for dom in dict.fromkeys(self._domains(query)):
                rel = self.engine.domain_relations(dom)
                if not rel:
                    continue
                sc = rel["structural"]["same_class"]
                if sc:
                    lines.append(f"- Domain **{dom}** is in the same class as: {', '.join(sc)}.")
                for c in rel["curated"]:
                    mech = f" via {c['mechanism']}" if c.get("mechanism") else ""
                    note = f" — {c['note']}" if c.get("note") else ""
                    adv.append(f"- {dom} → {c['target']}{mech}{note}")

        if "aggregate" in intents:
            m = re.search(r"\b(\d{1,3})\b", query)
            if m and ("variable" in query.lower()):
                n = int(m.group(1))
                res = self.engine.variables_in_min_domains(n)
                if res:
                    listed = ", ".join(f"{v} ({c})" for v, c in res[:50])
                    lines.append(f"- **{len(res)}** variables appear in ≥ {n} domains: {listed}.")
            for cls in dict.fromkeys(self._classes(query)):
                doms = self.engine.domains_in_class(cls)
                lines.append(f"- The **{cls}** class has **{len(doms)}** domains: {', '.join(doms)}.")
                counts.append(CheckableCount(cls, "class_domains", len(doms)))
            if "most shared" in query.lower() or "most common" in query.lower():
                top = self.engine.most_shared_codelists(5)
                listed = ", ".join(f"{t['code']} ({t['name']}, {t['n_variables']} vars)" for t in top)
                lines.append(f"- Most-shared codelists: {listed}.")

        if not lines and not adv:
            return None
        return StructuredFacts(text_block="\n".join(lines),
                               checkable_counts=counts,
                               advisory_block="\n".join(adv))
