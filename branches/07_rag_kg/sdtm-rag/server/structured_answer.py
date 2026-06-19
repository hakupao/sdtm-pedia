"""Deterministic structured-answer channel (SP2 Phase 1).

resolve(query) anchors known entities against the full meta.yaml vocabulary, detects
generic capability-intent cues, and assembles a StructuredFacts bundle of TRUE facts to
inject into the LLM context. Conservative by construction: zero hardcoded q-ids or
variable names; intent misfire is at worst recall-additive (extra true facts), never a
wrong answer; correctness of counts is back-stopped by the grounding gate, decoupled
from intent detection."""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from server.meta_store import MetaStore

# Generic language shapes — NOT tied to any q-id or variable. Each cue gates firing.
_COUNT_CUES = ("how many", "number of", "count of", "how much")
_ENUM_CUES = ("which domain", "what domain", "list ", "all domains", "every domain",
              "which variables", "what variables", "enumerate")
_ATTR_CUES = ("label", "role", "core designation", " core ", "data type", " type ",
              "what is the label", "definition of")
_CODELIST_CUES = ("codelist", "controlled term", "ct code", "terminology", "code list")


def detect_intents(query: str) -> set[str]:
    ql = query.lower()
    intents: set[str] = set()
    if any(c in ql for c in _COUNT_CUES):
        intents.add("count")
    if any(c in ql for c in _ENUM_CUES):
        intents.add("enumerate")
    if any(c in ql for c in _ATTR_CUES):
        intents.add("attribute")
    if any(c in ql for c in _CODELIST_CUES):
        intents.add("codelist")
    return intents


@dataclass(frozen=True)
class CheckableCount:
    subject: str   # e.g. "TAETORD"
    kind: str      # "domains" | "variables"
    value: int     # e.g. 43


@dataclass
class StructuredFacts:
    text_block: str
    checkable_counts: list[CheckableCount] = field(default_factory=list)


_VAR_TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9]{1,7}\b")
_CT_TOKEN_RE = re.compile(r"\bC\d{4,6}\b")


class StructuredAnswerer:
    def __init__(self, store: MetaStore):
        self.store = store

    def _anchored_variables(self, query: str) -> list[str]:
        # only uppercase tokens that are real meta.yaml variables (entity anchoring)
        return [t for t in _VAR_TOKEN_RE.findall(query) if t in self.store.known_variables]

    def _anchored_codelists(self, query: str) -> list[str]:
        return [c for c in _CT_TOKEN_RE.findall(query) if c in self.store.known_ctcodes]

    def _anchored_domains(self, query: str) -> list[str]:
        # Gate: only anchor 2-letter domain codes when the query carries an SDTM/domain context
        # signal. Without this, common English abbreviations (PR, DM, CO, IS, …) collide with
        # SDTM domain codes and cause false anchoring on off-topic queries.
        # Variable anchoring (long tokens) and codelist anchoring (Cxxxx) are unaffected.
        ql = query.lower()
        if "domain" not in ql and "sdtm" not in ql:
            return []
        return [t for t in _VAR_TOKEN_RE.findall(query) if t in self.store.known_domains]

    def resolve(self, query: str) -> StructuredFacts | None:
        intents = detect_intents(query)
        if not intents:
            return None  # must-not-fire: entity without capability intent
        variables = self._anchored_variables(query)
        codelists = self._anchored_codelists(query)
        domains = self._anchored_domains(query)
        if not variables and not codelists and not domains:
            # corpus-total fallback: explicit SDTM-wide count, no specific entity anchored
            ql = query.lower()
            corpus = any(p in ql for p in ("sdtm", "in total", "altogether", "the model"))
            if corpus and ("count" in intents or "enumerate" in intents):
                lines: list[str] = []
                if "domain" in ql:
                    lines.append(
                        f"- SDTM defines exactly **{self.store.n_domains}** domains."
                    )
                if "variable" in ql:
                    lines.append(
                        f"- SDTM defines **{self.store.n_unique_variables}** unique variables "
                        f"({self.store.n_variable_entries} variable entries across all domains)."
                    )
                if lines:
                    return StructuredFacts(
                        text_block="\n".join(lines), checkable_counts=[]
                    )
            return None  # must-not-fire: no anchored entity and no corpus phrase

        lines_: list[str] = []
        counts: list[CheckableCount] = []

        for var in dict.fromkeys(variables):  # de-dupe, preserve order
            attr = self.store.variable_attributes(var)
            if attr is None:
                continue
            domains_ = self.store.domains_for_variable(var)
            n = len(domains_)
            lines_.append(
                f"- **{var}** — {attr['label']} "
                f"(Role: {attr['role']}; Type: {attr['type']}; Core: {attr['core']})."
            )
            lines_.append(f"  Appears in exactly **{n}** SDTM domains: {', '.join(domains_)}.")
            if attr["ct_codes"]:
                lines_.append(
                    f"  Controlled-terminology codes: {', '.join(attr['ct_codes'])}."
                )
            counts.append(CheckableCount(var, "domains", n))

        for code in dict.fromkeys(codelists):
            cl = self.store.codelist(code)
            if cl is None:
                continue
            doms = self.store.domains_for_codelist(code)
            vars_ = self.store.variables_for_codelist(code)
            lines_.append(
                f"- **{code}** — codelist \"{cl['name']}\" "
                f"(extensible: {cl['extensible']}; {cl['term_count']} terms; "
                f"file {cl['termfile']}). "
                f"Used by {len(vars_)} variables across {len(doms)} domains: {', '.join(doms)}."
            )
            if "enumerate" in intents:
                lines_.append(
                    f"  Variables using it: {', '.join(vars_)}."
                )
            counts.append(CheckableCount(code, "domains", len(doms)))
            counts.append(CheckableCount(code, "codelist_variables", len(vars_)))

        for dom in dict.fromkeys(domains):
            info = self.store.domain_info(dom)
            if info is None:
                continue
            nv = info["n_variables"]
            lines_.append(
                f"- Domain **{dom}** — {info['label']} "
                f"(Class: {info['class']}; Structure: {info['structure']}). "
                f"Contains exactly **{nv}** variables."
            )
            counts.append(CheckableCount(dom, "variables", nv))
            if "enumerate" in intents:
                lines_.append(
                    f"  Variables: {', '.join(self.store.variables_in_domain(dom))}."
                )

        if not lines_:
            return None
        return StructuredFacts(text_block="\n".join(lines_), checkable_counts=counts)


_FACTS_HEADER = "## Structured Facts (authoritative, exhaustive, from SDTM metadata)"


def augment_context(facts: StructuredFacts | None, context: str) -> str:
    """Prepend the authoritative facts block ahead of the retrieved context.
    Shared by router.py (prod) and run_eval.py (eval) for identical wire-in."""
    if facts is None:
        return context
    return f"{_FACTS_HEADER}\n\n{facts.text_block}\n\n---\n\n{context}"
