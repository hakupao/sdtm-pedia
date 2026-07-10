"""SP6: mine implicit cross-domain relations from IG prose (advisory layer).

Reads knowledge_base/domains/<D>/{assumptions,examples}.md for a cluster and
emits data/meta/implicit_relations.json. NEVER writes meta.yaml. Deterministic
where possible (explicit links, co-occurrence); LLM only for data-flow, with a
verbatim-quote gate + adversarial verification.
"""
from __future__ import annotations

import re
from pathlib import Path

KB_ROOT = Path(__file__).resolve().parents[4] / "knowledge_base"
SEEDS = ["TU", "TR", "RS", "PR", "MI"]
CONF_THRESHOLD = 0.6
MAX_FLOW_PER_PAIR = 2

_DOMAIN_TOKEN = re.compile(r"\b([A-Z]{2,4})\b")


def load_prose(kb_root: Path, domains: list[str]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for d in domains:
        base = kb_root / "domains" / d
        out[d] = {
            kind: (base / f"{kind}.md").read_text(encoding="utf-8")
            if (base / f"{kind}.md").exists() else ""
            for kind in ("assumptions", "examples")
        }
    return out


def resolve_cluster(kb_root: Path, seeds: list[str]) -> list[str]:
    """seeds + one-hop: any known domain code literally named in a seed's prose."""
    known = {p.name for p in (kb_root / "domains").iterdir() if p.is_dir()}
    prose = load_prose(kb_root, seeds)
    found: set[str] = set(seeds)
    for d in seeds:
        text = prose[d]["assumptions"] + "\n" + prose[d]["examples"]
        for tok in _DOMAIN_TOKEN.findall(text):
            if tok in known and tok != d:
                found.add(tok)
    return sorted(found)


_MECH = re.compile(r"\b(RELREC|RELSPEC|RELSUB|SUPPQUAL|SUPP[A-Z]{2})\b")


def _edge(src, tgt, kind, directed, relation, quote, src_file, line, conf,
          extractor, verified, note="") -> dict:
    return {
        "id": f"{kind[:4]}:{src}>{tgt}:{line}",
        "source": src, "target": tgt, "kind": kind, "directed": directed,
        "relation": relation,
        "evidence": {"quote": quote.strip(), "source_file": src_file, "line": line},
        "confidence": conf, "extractor": extractor,
        "verified": verified, "verify_note": note,
    }


def extract_explicit_links(prose: dict, domains: list[str]) -> list[dict]:
    dom_set = set(domains)
    out: list[dict] = []
    for d, kinds in prose.items():
        for kind in ("assumptions", "examples"):
            src_file = f"knowledge_base/domains/{d}/{kind}.md"
            for i, line in enumerate(kinds[kind].split("\n"), 1):
                m = _MECH.search(line)
                if not m:
                    continue
                mech = m.group(1)
                for other in _DOMAIN_TOKEN.findall(line):
                    if other in dom_set and other != d:
                        out.append(_edge(d, other, "explicit_link", False, mech,
                                         line, src_file, i, 0.95, "regex", True))
    return out


def extract_cooccurrence(prose: dict, domains: list[str], min_count: int = 2) -> list[dict]:
    dom_set = set(domains)
    pair_count: dict[tuple[str, str], int] = {}
    for d, kinds in prose.items():
        text = kinds["assumptions"] + "\n" + kinds["examples"]
        for other in _DOMAIN_TOKEN.findall(text):
            if other in dom_set and other != d:
                key = tuple(sorted((d, other)))
                pair_count[key] = pair_count.get(key, 0) + 1
    out: list[dict] = []
    for (a, b), c in sorted(pair_count.items()):
        if c >= min_count:
            out.append(_edge(a, b, "co_occurrence", False, "",
                             f"{a}/{b} co-mentioned {c}x", "(co-occurrence)", 0,
                             min(0.5 + 0.1 * c, 0.9), "count", True))
    return out
