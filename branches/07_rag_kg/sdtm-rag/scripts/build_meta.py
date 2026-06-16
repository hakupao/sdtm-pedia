"""Generate data/meta/meta.yaml — the SP1 deterministic metadata layer.

Builds a per-domain structured registry from the read-only knowledge base
(spec.md + Cross References + terminology + model). No LLM. Idempotent.
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import yaml

from scripts.spec_loader import SpecLoader

# SUPPQUAL is a supplemental-qualifier structure, not one of the 63 standard
# domains (knowledge_base/INDEX.md counts 63, excluding SUPPQUAL).
_SPECIAL_DOMAINS = {"SUPPQUAL"}

_LABEL_RE = re.compile(r"^#\s+\w+\s*—\s*(.+?)\s*$")


def _parse_label(h1_line: str) -> str:
    """Extract the domain label from the spec.md H1, e.g.
    '# AE — Adverse Events' -> 'Adverse Events'. Returns '' if not a title."""
    m = _LABEL_RE.match(h1_line)
    return m.group(1).strip() if m else ""


def _domain_label(kb_root: Path, domain: str) -> str:
    spec = kb_root / "domains" / domain / "spec.md"
    if not spec.exists():
        return ""
    for line in spec.read_text(encoding="utf-8").split("\n")[:3]:
        if line.startswith("# "):
            return _parse_label(line)
    return ""


# ── Stubs for Task 2-6 (filled in per task) ──────────────────────────────

_CT_CODE_RE = re.compile(r"^C\d+$")


def _split_ct(controlled_terms: str) -> tuple[list[str], list[str]]:
    """Split a spec.md 'Controlled Terms' field into (C-codes, dict-tokens).
    Values are '; '-separated: a token is a CDISC C-code (^C\\d+$) or an
    external-dictionary/format token (MedDRA, LOINC, ISO 8601 ..., etc.)."""
    ct_codes: list[str] = []
    ct_dict: list[str] = []
    for tok in (t.strip() for t in controlled_terms.split(";")):
        if not tok:
            continue
        (ct_codes if _CT_CODE_RE.match(tok) else ct_dict).append(tok)
    return ct_codes, ct_dict


def _variables(ds) -> list[dict]:
    out: list[dict] = []
    for v in ds.variables:
        ct_codes, ct_dict = _split_ct(v.controlled_terms)
        out.append(
            {
                "name": v.name,
                "label": v.label,
                "role": v.role,
                "type": v.var_type,
                "core": v.core,
                "ct_codes": ct_codes,
                "ct_dict": ct_dict,
            }
        )
    return out


def _same_class_map(domains_out: list[dict]) -> dict[str, list[str]]:
    raise NotImplementedError


def _relations_curated(kb_root: Path, domain: str) -> list[dict]:
    raise NotImplementedError


def _model_defhome(kb_root: Path) -> dict[str, str]:
    raise NotImplementedError


def _codelists(kb_root: Path) -> list[dict]:
    raise NotImplementedError


# ── Main builder ──────────────────────────────────────────────────────────

def build_meta(kb_root: Path) -> dict:
    loader = SpecLoader(kb_root)
    domains_out: list[dict] = []
    domains_dir = kb_root / "domains"
    for domain_dir in sorted(domains_dir.iterdir()):
        if not domain_dir.is_dir():
            continue
        name = domain_dir.name.upper()
        ds = loader.get_domain(name)
        domains_out.append(
            {
                "domain": name,
                "class": ds.domain_class if ds else "",
                "label": _domain_label(kb_root, name),
                "structure": ds.structure if ds else "",
                "is_special": name in _SPECIAL_DOMAINS,
                "counts_toward_63": name not in _SPECIAL_DOMAINS,
                "variables": _variables(ds) if ds else [],
            }
        )
    return {
        "meta_version": 1,
        "generated_from": "knowledge_base/",
        "domains": domains_out,
    }
