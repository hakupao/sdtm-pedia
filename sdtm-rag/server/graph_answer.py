"""SP3 graph answer channel: detect relationship/impact intent + assemble
graph facts for injection into the LLM context.

Conservative by construction: zero hardcoded q-ids/variables; misfire is at worst
recall-additive true facts; correctness of cardinalities is back-stopped by the
grounding gate. Intent vocab is deliberately DISJOINT from SP2's distribution/count
vocab (use/include/which-domains) so plain SP2 queries never trip the graph channel.

NL surface covers two intent families:
  impact       — codelist/variable cascade ("affected if X changes", "downstream of X")
  relationship — single-domain discovery ("how is AE related to other domains?")

Aggregate queries (variables-in-min-domains / most-shared codelists) moved to the
dedicated AGG channel (server/aggregate_answer.py) after the KG value eval.

Class-roster queries ("how many domains in Events class?") are NOT exposed at the NL
layer: class names are common words ("Findings", "Events") → NL anchoring is inherently
fragile. The GraphEngine keeps domains_in_class/class_sizes for programmatic / SP4 use.

Relationship answers emit an authoritative same_class line (HIGH-fidelity structural
fact) plus an advisory block for curated (LOW-fidelity, prose-derived) relations.
Only the curated relations are marked advisory; same-class membership is authoritative.
"""
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

# Relationship discovery. Guards in resolve() further restrict to single-domain frames
# (no definition verb, not a specific-pair mechanism question with 2+ domains).
_REL_CUES = ("related to", "relationship", "relationships", "linked", "connected",
             "connection", "associated with", "association")

# Definition verbs — suppress relationship intent (definition = SP2/RAG territory).
_DEFINITION_VERBS = re.compile(
    r"\b(what\s+is|define|definition|describe|explains?)\b", re.IGNORECASE
)


def detect_graph_intents(query: str) -> set[str]:
    ql = query.lower()
    intents: set[str] = set()

    # Impact: any impact/cascade cue present
    if any(c in ql for c in _IMPACT_CUES):
        intents.add("impact")

    # Relationship: rel-discovery cue AND no definition verb
    if any(c in ql for c in _REL_CUES) and not _DEFINITION_VERBS.search(query):
        intents.add("relationship")

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
        if "domain" not in ql and "sdtm" not in ql:
            return []
        return [t for t in _VAR_TOKEN_RE.findall(q) if t in self.store.known_domains]

    def resolve(self, query: str) -> StructuredFacts | None:
        intents = detect_graph_intents(query)

        # Relationship guard: fire only for single-domain discovery (≤1 anchored domain).
        # Specific-pair mechanism questions ("how are TR and RS linked") have 2+ domains
        # and belong to SP2/RAG territory, not graph-discovery.
        if "relationship" in intents and len(self._domains(query)) >= 2:
            intents.discard("relationship")

        if not intents:
            return None

        lines: list[str] = []
        adv: list[str] = []
        counts: list[CheckableCount] = []

        if "impact" in intents:
            for code in dict.fromkeys(self._codelists(query)):
                imp = self.engine.impact_of_codelist(code)
                # Skip codelists not attached to any counts_toward_63 variable/domain.
                if imp and (imp["n_domains"] > 0 or imp["n_variables"] > 0):
                    lines.append(
                        f"- Changing codelist **{code}** ({imp['name']}) affects "
                        f"**{imp['n_variables']}** variables across **{imp['n_domains']}** "
                        f"domains: {', '.join(imp['domains'])}.")
                    counts.append(CheckableCount(code, "impacted_domains", imp["n_domains"]))
                    counts.append(CheckableCount(code, "impacted_variables", imp["n_variables"]))
            for var in dict.fromkeys(self._vars(query)):
                imp = self.engine.impact_of_variable(var)
                if imp and imp["n_domains"] > 0:
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

        if not lines and not adv:
            return None
        return StructuredFacts(text_block="\n".join(lines),
                               checkable_counts=counts,
                               advisory_block="\n".join(adv))
