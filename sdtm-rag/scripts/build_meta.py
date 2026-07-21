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

# A domain "counts toward the 63" iff it has a spec.md (the authoritative
# 63 in knowledge_base/INDEX.md are exactly the dirs WITH spec.md — this
# includes SUPPQUAL, which has a full spec). DI has only assumptions.md
# (no variables), so it is a stub: is_special=True, counts_toward_63=False.

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
    """Group domains by class; same_class[d] = sorted siblings (excl. self).
    Deterministic and COMPLETE (the curated 'Same class' prose may omit some)."""
    by_class: dict[str, list[str]] = defaultdict(list)
    for d in domains_out:
        if d["class"]:
            by_class[d["class"]].append(d["domain"])
    result: dict[str, list[str]] = {}
    for d in domains_out:
        sibs = [x for x in by_class.get(d["class"], []) if x != d["domain"]]
        result[d["domain"]] = sorted(sibs)
    return result



# 跨类策划边: "- **Treatment:** [CM](../CM/) — concomitant ... via RELREC"
# 必须有 [link]，从而排除无链接的 "**Same class (X):**" bullet。
_REL_RE = re.compile(
    r"^- \*\*(?P<cat>[^:]+):\*\*\s*\[(?P<tgt>[A-Z0-9]+)\]\([^)]*\)\s*[—-]\s*(?P<note>.*)$"
)
# 机制只在散文字面出现时才填，否则 None。
_MECH_RE = re.compile(r"\b(RELREC|RELSPEC|RELSUB|SUPPQUAL|SUPP)\b")


def _relations_curated(kb_root: Path, domain: str) -> list[dict]:
    spec = kb_root / "domains" / domain / "spec.md"
    if not spec.exists():
        return []
    lines = spec.read_text(encoding="utf-8").split("\n")
    # 只在 "### Related Domains" 小节内扫
    out: list[dict] = []
    in_section = False
    for line in lines:
        if line.startswith("### Related Domains"):
            in_section = True
            continue
        if in_section and line.startswith("### "):
            break
        if not in_section:
            continue
        m = _REL_RE.match(line)
        if not m:
            continue
        note = m.group("note").strip()
        mech = _MECH_RE.search(note)
        out.append(
            {
                "target": m.group("tgt"),
                "category": m.group("cat").strip(),
                "mechanism": mech.group(1) if mech else None,
                "note": note,
                "fidelity": "curated_prose",
            }
        )
    return out


def _model_defhome(kb_root: Path) -> dict[str, str]:
    """var -> model/*.md definition home. The 6-col definition table
    `| # | VAR | Label | Type | Role | Notes |` is isolated by len(inner)==6
    (the 5-col usage table's last cell is Role, not Notes). Keep only vars whose
    Notes-bearing 6-col rows live in EXACTLY ONE file; drop generic '--' vars."""
    model_dir = kb_root / "model"
    if not model_dir.exists():
        return {}
    tmp: dict[str, set[str]] = defaultdict(set)
    for f in sorted(model_dir.glob("*.md")):
        rel = f.relative_to(kb_root).as_posix()
        for raw in f.read_text(encoding="utf-8").splitlines():
            if "|" not in raw:
                continue
            cells = [c.strip() for c in raw.split("|")]
            inner = cells[1:-1]
            if len(inner) != 6:
                continue  # load-bearing discriminator (do NOT relax)
            num, var, _label, _type, _role, notes = inner
            if not num.isdigit():
                continue
            if not re.fullmatch(r"(?:--)?[A-Z][A-Z0-9]*", var):
                continue
            if not notes:
                continue
            tmp[var].add(rel)
    return {
        var: next(iter(files))
        for var, files in sorted(tmp.items())
        if len(files) == 1 and not var.startswith("--")
    }


_CL_HEADING_RE = re.compile(r"^##\s+(.+?)\s*\(([Cc]\d+)\)")


def _codelist_files(kb_root: Path) -> dict[str, str]:
    """ct_code -> kb-relative termfile path (first file whose heading defines it)."""
    out: dict[str, str] = {}
    term_dir = kb_root / "terminology"
    if not term_dir.exists():
        return out
    for f in sorted(term_dir.rglob("*.md")):
        rel = f.relative_to(kb_root).as_posix()
        for line in f.read_text(encoding="utf-8").splitlines():
            m = _CL_HEADING_RE.match(line)
            if m:
                out.setdefault(m.group(2).upper(), rel)
    return out


def _codelists(kb_root: Path, loader: SpecLoader) -> list[dict]:
    files = _codelist_files(kb_root)
    out: list[dict] = []
    for code, cl in sorted(loader.codelists.items()):
        out.append(
            {
                "ct_code": code,
                "name": cl.name,
                "extensible": cl.extensible,
                "term_count": len(cl.submission_values),
                "termfile": files.get(code, ""),
            }
        )
    return out


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
        has_spec = (domain_dir / "spec.md").exists()
        domains_out.append(
            {
                "domain": name,
                "class": ds.domain_class if ds else "",
                "label": _domain_label(kb_root, name),
                "structure": ds.structure if ds else "",
                "is_special": not has_spec,
                "counts_toward_63": has_spec,
                "variables": _variables(ds) if ds else [],
                "relations_curated": _relations_curated(kb_root, name),
            }
        )
    sc = _same_class_map(domains_out)
    for d in domains_out:
        d["same_class"] = sc[d["domain"]]

    return {
        "meta_version": 1,
        "generated_from": "knowledge_base/",
        "domains": domains_out,
        "model_defhome": _model_defhome(kb_root),
        "codelists": _codelists(kb_root, loader),
    }


def dump_meta(meta: dict, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        yaml.safe_dump(meta, sort_keys=True, allow_unicode=True, width=1000),
        encoding="utf-8",
    )


def main() -> None:
    # scripts -> sdtm-rag -> 07_rag_kg -> branches -> sdtm-pedia
    kb_root = Path(__file__).resolve().parents[2] / "knowledge_base"
    out = Path(__file__).resolve().parents[1] / "data" / "meta" / "meta.yaml"
    meta = build_meta(kb_root)
    dump_meta(meta, out)
    print(f"wrote {out} ({len(meta['domains'])} domains, "
          f"{len(meta['codelists'])} codelists)")


if __name__ == "__main__":
    main()
