"""SP6: mine implicit cross-domain relations from IG prose (advisory layer).

Reads knowledge_base/domains/<D>/{assumptions,examples}.md for a cluster and
emits data/meta/implicit_relations.json. NEVER writes meta.yaml. Deterministic
where possible (explicit links, co-occurrence); LLM only for data-flow, with a
verbatim-quote gate + adversarial verification.
"""
from __future__ import annotations

import json
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


_FLOW_PROMPT = """You are analyzing SDTM Implementation Guide prose for two domains.
Domain {A} text:
---
{TA}
---
Domain {B} text:
---
{TB}
---
Identify DIRECTED data-flow relations between {A} and {B} that the text SUPPORTS
(e.g. "{A} measurements are recorded in {B}"). For each, return an object:
{{"source": "<{A} or {B}>", "target": "<the other>", "relation": "<short phrase>",
  "quote": "<VERBATIM sentence copied exactly from the text above that supports it>",
  "confidence": <0..1>}}
Rules: quote MUST be copied verbatim from the text; if nothing is clearly supported,
return []. Return ONLY a JSON array."""


def _complete_json(prompt: str, model: str) -> list[dict]:
    import litellm
    resp = litellm.completion(model=model, temperature=0,
                              messages=[{"role": "user", "content": prompt}])
    txt = resp["choices"][0]["message"]["content"].strip()
    txt = re.sub(r"^```(?:json)?|```$", "", txt, flags=re.M).strip()
    try:
        data = json.loads(txt)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def extract_data_flow(prose: dict, domains: list[str], model: str,
                      complete=_complete_json) -> list[dict]:
    out: list[dict] = []
    doms = sorted(domains)
    for i, a in enumerate(doms):
        for b in doms[i + 1:]:
            ta = prose.get(a, {}).get("assumptions", "") + prose.get(a, {}).get("examples", "")
            tb = prose.get(b, {}).get("assumptions", "") + prose.get(b, {}).get("examples", "")
            if not ta or not tb:
                continue
            cands = complete(_FLOW_PROMPT.format(A=a, B=b, TA=ta[:6000], TB=tb[:6000]), model)
            for c in cands[:MAX_FLOW_PER_PAIR * 2]:
                s, t = c.get("source"), c.get("target")
                if {s, t} != {a, b}:
                    continue
                src_file = f"knowledge_base/domains/{s}/examples.md"
                out.append(_edge(s, t, "data_flow", True, c.get("relation", ""),
                                 c.get("quote", ""), src_file, 0,
                                 float(c.get("confidence", 0.0)), "llm", False))
    return out


def quote_in_source(edge: dict, kb_root: Path) -> bool:
    q = edge["evidence"]["quote"].strip()
    rel = edge["evidence"]["source_file"].replace("knowledge_base/", "")
    for kind in ("examples", "assumptions"):
        # try the declared file, then the sibling kind (LLM may misattribute)
        cand = kb_root / rel
        for p in {cand, cand.with_name(f"{kind}.md")}:
            if p.exists() and q and q in p.read_text(encoding="utf-8"):
                return True
    return False


_VERIFY_PROMPT = """A relation was extracted from SDTM IG prose:
  {S} --[{R}]--> {T}   (directed)
Supporting quote: "{Q}"
Try hard to REFUTE it. Does the quote actually support THIS directed relation
(right direction, right domains)? If uncertain, refute. Return ONLY:
[{{"refuted": <true|false>, "reason": "<short>"}}]"""


def verify_data_flow_edge(edge: dict, model: str, judge=_complete_json) -> dict:
    out = judge(_VERIFY_PROMPT.format(S=edge["source"], T=edge["target"],
                R=edge["relation"], Q=edge["evidence"]["quote"]), model)
    verdict = out[0] if out else {"refuted": True, "reason": "no verdict"}
    return {"verified": not bool(verdict.get("refuted", True)),
            "note": str(verdict.get("reason", ""))}


def build_implicit_relations(kb_root: Path, seeds: list[str], model: str,
                             complete=_complete_json, judge=_complete_json) -> dict:
    cluster = resolve_cluster(kb_root, seeds)
    prose = load_prose(kb_root, cluster)
    edges = extract_explicit_links(prose, cluster) + extract_cooccurrence(prose, cluster)
    rejected: list[dict] = []
    per_pair: dict[tuple, int] = {}
    for e in extract_data_flow(prose, cluster, model, complete=complete):
        if not quote_in_source(e, kb_root):
            e["verify_note"] = "gate1: quote not found in source"; rejected.append(e); continue
        v = verify_data_flow_edge(e, model, judge=judge)
        e["verified"], e["verify_note"] = v["verified"], v["note"]
        key = tuple(sorted((e["source"], e["target"])))
        if not v["verified"] or e["confidence"] < CONF_THRESHOLD \
           or per_pair.get(key, 0) >= MAX_FLOW_PER_PAIR:
            rejected.append(e); continue
        per_pair[key] = per_pair.get(key, 0) + 1
        edges.append(e)
    return {
        "meta": {"version": 1, "cluster_seeds": seeds, "domains": cluster,
                 "generated_from": "knowledge_base/domains/<D>/{assumptions,examples}.md",
                 "confidence_threshold": CONF_THRESHOLD},
        "edges": sorted(edges, key=lambda e: (e["kind"], e["source"], e["target"])),
        "_rejected": rejected,
    }
