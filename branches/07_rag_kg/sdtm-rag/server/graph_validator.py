"""SP5 graph-augmented validation (DESIGN §5.6): cross-domain checks for an
uploaded SDTM study, using the in-memory GraphEngine (meta.yaml) as the reference.
Deterministic, read-only, no Neo4j, no LLM. All findings are advisory (WARN/INFO).
"""
from __future__ import annotations

import pandas as pd

from server.graph_engine import GraphEngine
from server.validator import Finding

IMPACT_DOMAIN_THRESHOLD = 10


def check_completeness(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]:
    """WARN when a submitted domain is RELREC-linked to a *partner domain* absent from
    the submission.

    Only edges with an explicit ``mechanism == "RELREC"`` identify a missing partner
    DOMAIN (e.g. AE -> CM, AE -> PR). The spec's proposed back-fill (null mechanism +
    target in {RELREC,RELSPEC,RELSUB} => infer mechanism) is intentionally dropped:
    verification against meta.yaml showed those null-mechanism edges have the
    *relationship dataset itself* as their target (LB/BS/IS/MB/MS -> RELSPEC, "specimen
    hierarchy"), i.e. the target IS the mechanism, not a partner domain to be present.
    Back-filling them would emit nonsensical "X is RELSPEC-linked to RELSPEC, absent"
    warnings. So RELSPEC/RELSUB relationships are out of completeness scope by design.
    (See evidence/failures/sp5_attempt_1.md; corroborated by Rule A + Rule D reviews.)"""
    submitted = {d.upper() for d in datasets}
    findings: list[Finding] = []
    for dom in sorted(submitted):
        for rel in engine.store.relations_curated(dom):
            if rel.get("mechanism") != "RELREC":
                continue
            target = str(rel["target"]).upper()
            if target not in submitted:
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
        # WARN only on *non-nested* divergence: two domains whose value sets each
        # contain something the other lacks (a genuine inconsistency). Legitimate
        # coverage differences where one domain's values are a subset of another's
        # (e.g. AE={Y} vs MH={Y,N,U}) are NOT flagged — that was a false-positive source.
        sets = sorted(dom_vals.items())
        diverges = any(
            not (a[1] <= b[1] or b[1] <= a[1])
            for i, a in enumerate(sets)
            for b in sets[i + 1:]
        )
        if diverges:
            cl = engine.store.codelist(ct)
            name = cl["name"] if cl else ct
            detail = "; ".join(f"{d}={sorted(v)}" for d, v in sorted(dom_vals.items()))
            findings.append(Finding(
                "WARN", "GCASCADE", None,
                f"Codelist {ct} ({name}) has inconsistent values across domains: {detail}",
            ))
    return findings


def check_impact(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]:
    """INFO advisory: flag high-impact variables/codelists present in the data
    (a variable or its codelist spanning >= IMPACT_DOMAIN_THRESHOLD domains) so the
    user knows changes there have wide cross-domain effect. Never pass/fail.

    Identifier-role variables (STUDYID/DOMAIN/USUBJID/--SEQ) are skipped: they are
    universal by construction, so their wide spread is trivially known and flagging
    them is pure noise (they would fire in every dataset)."""
    findings: list[Finding] = []
    for dom in sorted(datasets):
        df = datasets[dom]
        seen_vars: set[str] = set()
        seen_cts: set[str] = set()
        for col in df.columns:
            var = str(col).upper()
            if var not in seen_vars:
                seen_vars.add(var)
                iv = engine.impact_of_variable(var)
                attrs = engine.store.variable_attributes(var)
                role = attrs["role"] if attrs else None
                if (iv and iv["n_domains"] >= IMPACT_DOMAIN_THRESHOLD
                        and role != "Identifier"):
                    findings.append(Finding(
                        "INFO", "GIMPACT", var,
                        f"{var} is high-impact: appears in {iv['n_domains']} domains; "
                        f"changes have wide cross-domain effect.",
                    ))
            for ct in engine.store.ct_codes_for_variable(var):
                if ct in seen_cts:
                    continue
                seen_cts.add(ct)
                ic = engine.impact_of_codelist(ct)
                if ic and ic["n_domains"] >= IMPACT_DOMAIN_THRESHOLD:
                    findings.append(Finding(
                        "INFO", "GIMPACT", var,
                        f"Codelist {ct} ({ic['name']}) used by {var} is high-impact: "
                        f"{ic['n_domains']} domains / {ic['n_variables']} variables.",
                    ))
    return findings


def run_graph_checks(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]:
    """Run all three SP5 graph checks over a submitted study. Returns merged findings
    (all WARN/INFO). datasets maps uppercase domain code -> its DataFrame."""
    return (
        check_impact(datasets, engine)
        + check_completeness(datasets, engine)
        + check_ct_cascade(datasets, engine)
    )
