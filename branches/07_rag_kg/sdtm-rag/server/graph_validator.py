"""SP5 graph-augmented validation (DESIGN §5.6): cross-domain checks for an
uploaded SDTM study, using the in-memory GraphEngine (meta.yaml) as the reference.
Deterministic, read-only, no Neo4j, no LLM. All findings are advisory (WARN/INFO).
"""
from __future__ import annotations

import pandas as pd

from server.graph_engine import GraphEngine
from server.validator import Finding

IMPACT_DOMAIN_THRESHOLD = 10
_RELATIONSHIP_DATASETS = {"RELREC", "RELSPEC", "RELSUB"}


def check_completeness(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]:
    """WARN when a submitted domain is RELREC-linked to a target domain absent from
    the submission. mechanism==None is back-filled to the target when the target is
    itself a relationship dataset (deterministic structural inference, SP5-local)."""
    submitted = {d.upper() for d in datasets}
    findings: list[Finding] = []
    for dom in sorted(submitted):
        for rel in engine.store.relations_curated(dom):
            target = str(rel["target"]).upper()
            mech = rel.get("mechanism")
            if mech is None and target in _RELATIONSHIP_DATASETS:
                mech = target
            if mech == "RELREC" and target not in submitted:
                findings.append(Finding(
                    "WARN", "GXDOM", None,
                    f"Domain {dom} is RELREC-linked to {target}, but {target} "
                    f"is not present in this study submission.",
                ))
    return findings


def check_ct_cascade(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]:
    """WARN when the distinct actual values used for a shared codelist differ across
    domains (a codelist used by >=2 submitted domains should have a consistent value
    domain). Advisory only — different coverage is legitimate, hence WARN not ERROR."""
    cascade: dict[str, dict[str, set[str]]] = {}
    for dom, df in datasets.items():
        dom = dom.upper()
        for col in df.columns:
            for ct in engine.store.ct_codes_for_variable(str(col).upper()):
                vals = {str(v).strip() for v in df[col].dropna().unique() if str(v).strip()}
                if vals:
                    cascade.setdefault(ct, {}).setdefault(dom, set()).update(vals)
    findings: list[Finding] = []
    for ct in sorted(cascade):
        dom_vals = cascade[ct]
        if len(dom_vals) < 2:
            continue
        union = set().union(*dom_vals.values())
        if any(vals != union for vals in dom_vals.values()):
            cl = engine.store.codelist(ct)
            name = cl["name"] if cl else ct
            detail = "; ".join(f"{d}={sorted(v)}" for d, v in sorted(dom_vals.items()))
            findings.append(Finding(
                "WARN", "GCASCADE", None,
                f"Codelist {ct} ({name}) has inconsistent values across domains: {detail}",
            ))
    return findings
