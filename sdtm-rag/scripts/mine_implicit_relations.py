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
PROSE_WINDOW = 12000

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
            cands = complete(_FLOW_PROMPT.format(A=a, B=b, TA=ta[:PROSE_WINDOW],
                                                 TB=tb[:PROSE_WINDOW]), model)
            for c in cands[:MAX_FLOW_PER_PAIR * 2]:
                s, t = c.get("source"), c.get("target")
                if {s, t} != {a, b}:
                    continue
                src_file = f"knowledge_base/domains/{s}/examples.md"
                out.append(_edge(s, t, "data_flow", True, c.get("relation", ""),
                                 c.get("quote", ""), src_file, 0,
                                 float(c.get("confidence", 0.0)), "llm", False))
    return out


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _find_line(text: str, quote: str) -> int:
    key = _norm(quote)[:24]
    if not key:
        return 0
    for i, line in enumerate(text.split("\n"), 1):
        if key in _norm(line):
            return i
    return 0


def _target_in_quote(edge: dict) -> bool:
    """A directed data_flow edge's TARGET domain must be named in the quote."""
    return bool(re.search(rf"\b{re.escape(edge['target'])}[A-Z]*\b", edge["evidence"]["quote"]))


def quote_in_source(edge: dict, kb_root: Path) -> bool:
    q = _norm(edge["evidence"]["quote"])
    rel = edge["evidence"]["source_file"].replace("knowledge_base/", "")
    cand = kb_root / rel
    for p in dict.fromkeys([cand, cand.with_name("examples.md"), cand.with_name("assumptions.md")]):
        if not (p.exists() and q):
            continue
        text = p.read_text(encoding="utf-8")
        if q in _norm(text):
            edge["evidence"]["source_file"] = "knowledge_base/" + p.relative_to(kb_root).as_posix()
            edge["evidence"]["line"] = _find_line(text, edge["evidence"]["quote"])
            return True
    return False


_VERIFY_PROMPT = """A relation was extracted from SDTM IG prose:
  {S} --[{R}]--> {T}   (directed)
Supporting quote: "{Q}"
Refute if the quote does NOT explicitly name the target domain {T}, or does not
support data/information flowing from {S} to {T} (wrong direction counts as
refuted). Only accept if the quote names both {S} and {T} and supports the
{S}→{T} direction. Return ONLY:
[{{"refuted": <true|false>, "reason": "<short>"}}]"""


def verify_data_flow_edge(edge: dict, model: str, judge=_complete_json) -> dict:
    prompt = _VERIFY_PROMPT.format(S=edge["source"], T=edge["target"],
                                   R=edge["relation"], Q=edge["evidence"]["quote"])
    out = judge(prompt, model) or judge(prompt, model)   # one retry on empty/unparseable
    if not out:
        return {"verified": False, "note": "judge inconclusive (no parseable verdict) — rejected"}
    verdict = out[0]
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
            e["verify_note"] = "gate1: quote not found in source"
            rejected.append(e)
            continue
        if not _target_in_quote(e):
            e["verify_note"] = f"gate1b: target {e['target']} not named in quote"
            rejected.append(e)
            continue
        v = verify_data_flow_edge(e, model, judge=judge)
        e["verified"], e["verify_note"] = v["verified"], v["note"]
        key = tuple(sorted((e["source"], e["target"])))
        if not v["verified"]:
            rejected.append(e)
            continue          # verify_note already holds judge's refute reason
        if e["confidence"] < CONF_THRESHOLD:
            e["verify_note"] = f"below confidence threshold ({e['confidence']} < {CONF_THRESHOLD})"
            rejected.append(e)
            continue
        if per_pair.get(key, 0) >= MAX_FLOW_PER_PAIR:
            e["verify_note"] = f"per-pair cap reached ({MAX_FLOW_PER_PAIR}) for {key}"
            rejected.append(e)
            continue
        per_pair[key] = per_pair.get(key, 0) + 1
        edges.append(e)
    seen, deduped = set(), []
    for e in edges:
        k = (e["kind"], e["source"], e["target"], e["evidence"]["quote"])
        if k in seen:
            continue
        seen.add(k)
        deduped.append(e)
    idc: dict = {}
    for e in deduped:
        base = f'{e["kind"][:4]}:{e["source"]}>{e["target"]}:{e["evidence"]["line"]}'
        n = idc.get(base, 0)
        idc[base] = n + 1
        e["id"] = base if n == 0 else f"{base}#{n}"
    edges = deduped
    return {
        "meta": {"version": 1, "cluster_seeds": seeds, "domains": cluster,
                 "generated_from": "knowledge_base/domains/<D>/{assumptions,examples}.md",
                 "confidence_threshold": CONF_THRESHOLD},
        "edges": sorted(edges, key=lambda e: (e["kind"], e["source"], e["target"])),
        "_rejected": rejected,
    }


def write_outputs(result: dict, out_json: Path, audit_md: Path, failures_dir: Path) -> None:
    rejected = result.pop("_rejected", [])
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    if rejected:
        failures_dir.mkdir(parents=True, exist_ok=True)
        (failures_dir / "sp6_rejected_edges.json").write_text(
            json.dumps(rejected, ensure_ascii=False, indent=2), encoding="utf-8")
    by_kind: dict[str, int] = {}
    for e in result["edges"]:
        by_kind[e["kind"]] = by_kind.get(e["kind"], 0) + 1
    lines = ["# SP6 隐性关系抽检 (Rule A)\n",
             f"> 生成: 见 git;域: {', '.join(result['meta']['domains'])}\n",
             f"边计数: {by_kind};被毙: {len(rejected)}\n\n## N=8 分层抽检\n",
             "| # | 边 | 类型 | 引文命中? | 关系/方向对? | 判定 |\n|--|--|--|--|--|--|\n"]
    by_kind_edges: dict[str, list] = {}
    for e in result["edges"]:
        by_kind_edges.setdefault(e["kind"], []).append(e)
    sample = (by_kind_edges.get("data_flow", [])[:6] + by_kind_edges.get("explicit_link", [])[:1]
              + by_kind_edges.get("co_occurrence", [])[:1])[:8]
    for i, e in enumerate(sample, 1):
        lines.append(f"| {i} | {e['source']}→{e['target']} | {e['kind']} | 待核 | 待核 | 待填 |\n")
    audit_md.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    import argparse

    from dotenv import load_dotenv
    root = Path(__file__).resolve().parents[1]
    load_dotenv(root / ".env")
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="deepseek/deepseek-chat")
    ap.add_argument("--out", default=str(root / "data" / "meta" / "implicit_relations.json"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    result = build_implicit_relations(KB_ROOT, SEEDS, args.model)
    n = len(result["edges"])
    if args.dry_run:
        print(f"[dry-run] {n} edges, {len(result['_rejected'])} rejected")
        return
    write_outputs(result, Path(args.out),
                  root / "evidence" / "checkpoints" / "implicit_relations_audit.md",
                  root / "failures")
    print(f"wrote {args.out} ({n} edges)")


if __name__ == "__main__":
    main()
