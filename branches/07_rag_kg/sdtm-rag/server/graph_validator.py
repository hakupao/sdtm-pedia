"""SP5 graph-augmented validation (DESIGN §5.6): cross-domain checks for an
uploaded SDTM study, using the in-memory GraphEngine (meta.yaml) as the reference.
Deterministic, read-only, no Neo4j, no LLM. All findings are advisory (WARN/INFO).
"""
from __future__ import annotations

import pandas as pd

from server.graph_engine import GraphEngine
from server.validator import Finding

IMPACT_DOMAIN_THRESHOLD = 10
# Curated-relation targets that are relationship/special-purpose datasets, not partner
# domains a study would submit — excluded from completeness (see M1 in sp5_attempt_1.md).
_REL_DATASET_TARGETS = {"RELREC", "RELSPEC", "RELSUB", "SUPPQUAL", "SUPP", "CO"}


def check_completeness(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]:
    """Flag cross-domain relations whose partner domain is absent from the submission.

    Two tiers, matched to the meta.yaml curation's fidelity:

    * **RELREC -> WARN**: explicit ``mechanism == "RELREC"`` edges identify related
      *records* that belong together, so a missing partner is a real completeness gap.
      RELREC is treated as **symmetric** (a related-records relationship has two
      endpoints): the AE->CM / AE->PR edges also mean submitting CM or PR without AE
      warns. The KB asserts only these 2 RELREC pairs; RELREC linkage is otherwise
      study-specific, so this stays a narrow, high-confidence signal.

    * **other curated cross-domain relations -> INFO**: the remaining curated edges
      (Findings About, Shared Dataset, Specimen, Source Domain, ...) are LOW-fidelity
      curated_prose associations. A missing partner is surfaced as a soft, advisory hint,
      never a WARN. Targets that are relationship/special-purpose datasets (RELSPEC/RELSUB/
      SUPPQUAL/CO) are excluded — they are mechanisms, not partner domains to submit.

    All findings are advisory (never ERROR)."""
    submitted = {d.upper() for d in datasets}
    all_domains = set(engine.store.all_domains())

    # Build the RELREC partner map (symmetric) and the non-RELREC curated map once.
    relrec_partners: dict[str, set[str]] = {}
    curated: dict[str, list[tuple[str, str | None]]] = {}
    for dom in all_domains:
        for rel in engine.store.relations_curated(dom):
            target = str(rel["target"]).upper()
            if rel.get("mechanism") == "RELREC":
                relrec_partners.setdefault(dom, set()).add(target)
                relrec_partners.setdefault(target, set()).add(dom)  # symmetric
            elif target in all_domains and target not in _REL_DATASET_TARGETS:
                curated.setdefault(dom, []).append((target, rel.get("category")))

    findings: list[Finding] = []
    for dom in sorted(submitted):
        partners = relrec_partners.get(dom, set())
        for target in sorted(partners):
            if target not in submitted:
                findings.append(Finding(
                    "WARN", "GXDOM", None,
                    f"Domain {dom} is RELREC-linked to {target}, but {target} "
                    f"is not present in this study submission.",
                ))
        seen: set[str] = set()
        for target, category in curated.get(dom, []):
            if target in partners or target in submitted or target in seen:
                continue
            seen.add(target)
            label = f" ({category})" if category else ""
            findings.append(Finding(
                "INFO", "GXDOM", None,
                f"Domain {dom} is commonly related to {target}{label}, which is not "
                f"present in this study submission.",
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
        cl = engine.store.codelist(ct)
        # Skip extensible codelists: they are open-ended by design (e.g. Unit C71620 with
        # 830 terms), so different domains legitimately use disjoint value subsets (CM dose
        # units vs LB lab units). Only CLOSED codelists have a fixed value domain where
        # cross-domain divergence is a real signal. (Real-data FP on CDISCPILOT01.)
        if cl and cl.get("extensible"):
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
