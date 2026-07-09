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
