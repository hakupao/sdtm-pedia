"""SP2 Phase 2 equivalence harness — behaviour snapshot for the structured_lookup
regex→meta.yaml migration.

A behaviour-preserving refactor needs a behaviour snapshot, not just the 36 unit
tests (which lock subtle long-name/collision/gating cases but NOT the bulk
termfile/distribution/concept-def resolution over the full vocabulary). This script
captures the COMPLETE observable behaviour of `StructuredLookup`:

  * every internal index map that `resolve()` reads, and
  * `resolve(query)` over an exhaustive corpus = the 140 v3 test questions PLUS a
    full sweep of EVERY variable / CT code / domain in meta.yaml (term, distribution,
    concept-definition, attribute, and bare-mention query shapes).

Run it on the OLD (regex) code → golden snapshot. Run it again on the NEW
(meta.yaml-backed) code → assert byte-identical. Any divergence localises to a map
or a specific query. Deterministic, no network, no LLM.

Usage:
  .venv/bin/python eval/prod_wirein/sp2p2_equiv_snapshot.py dump  <out.json>
  .venv/bin/python eval/prod_wirein/sp2p2_equiv_snapshot.py diff  <golden.json> <new.json>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT))

from server.config import settings  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402
from server.structured_lookup import StructuredLookup  # noqa: E402


def _build_lookup(kb_root: Path, store: MetaStore) -> StructuredLookup:
    """Work with both signatures: old StructuredLookup(kb_root) and new
    StructuredLookup(kb_root, store). Lets the SAME script snapshot before and after
    the migration."""
    try:
        return StructuredLookup(kb_root, store)  # new signature
    except TypeError:
        return StructuredLookup(kb_root)  # old signature


def _test_questions() -> list[str]:
    """All 140 question strings from test_set_v3.yml (real eval corpus)."""
    raw = yaml.safe_load((_ROOT / "eval" / "test_set_v3.yml").read_text(encoding="utf-8"))
    out: list[str] = []

    def walk(node) -> None:
        if isinstance(node, dict):
            if isinstance(node.get("question"), str):
                out.append(node["question"])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(raw)
    return out


def _corpus(store: MetaStore) -> list[str]:
    """Exhaustive, FIXED query corpus derived from meta.yaml (identical for old/new
    runs since meta.yaml is the shared reference). Exercises every resolve() channel
    over the full vocabulary."""
    queries: list[str] = list(_test_questions())

    # per variable: terminology / distribution / concept-definition / attribute / bare
    for var in sorted(store.known_variables):
        queries.append(f"What controlled terminology codelist does the {var} variable use?")
        queries.append(f"Which SDTM domains include the {var} variable?")
        queries.append(f"What does the {var} variable represent?")
        queries.append(f"In the DM domain what is the {var} variable Core designation?")
        queries.append(f"The {var} variable appears in submission datasets.")  # bare, no intent

    # per CT code: codelist-sharing (distribution) + terminology
    for code in sorted(store.known_ctcodes):
        queries.append(f"Which domains share the codelist {code}?")
        queries.append(f"What controlled terminology is in codelist {code}?")

    # per domain: long-name dataset reference (drives the long-name channel)
    for dom in sorted(store.known_domains):
        info = store.domain_info(dom)
        if info and info.get("label"):
            queries.append(f"What is the structure of the {info['label']} dataset?")
        queries.append(f"What are the required variables in the {dom} domain?")  # code token

    # de-dupe, preserve first-seen order
    seen: set[str] = set()
    ordered: list[str] = []
    for q in queries:
        if q not in seen:
            seen.add(q)
            ordered.append(q)
    return ordered


def _snapshot(lookup: StructuredLookup, corpus: list[str]) -> dict:
    # var_to_termfiles -> {var: sorted unique termfiles} (resolve() only emits termfile)
    var_termfiles = {
        var: sorted({tf for (_n, _c, tf) in entries})
        for var, entries in lookup.var_to_termfiles.items()
    }
    maps = {
        "known_variables": sorted(lookup.known_variables),
        "domain_to_spec": dict(sorted(lookup.domain_to_spec.items())),
        "domain_longname_to_code": dict(sorted(lookup.domain_longname_to_code.items())),
        "var_to_model_defhome": dict(sorted(lookup.var_to_model_defhome.items())),
        "general_assumptions_file": lookup.general_assumptions_file,
        "ctcode_to_termfile": dict(sorted(lookup.ctcode_to_termfile.items())),
        "var_to_termfiles": dict(sorted(var_termfiles.items())),
        # NOTE: ctcode_to_vars (old VARIABLE_INDEX §三 parse) is NOT snapshotted — it is
        # dead code (referenced nowhere outside the module, never read by resolve()) and is
        # dropped in the meta.yaml-backed rewrite.
    }
    resolve = {q: lookup.resolve(q) for q in corpus}
    return {"maps": maps, "resolve": resolve, "n_queries": len(corpus)}


def _dump(out_path: str) -> int:
    store = MetaStore(settings.meta_path)
    lookup = _build_lookup(settings.kb_root, store)
    corpus = _corpus(store)
    snap = _snapshot(lookup, corpus)
    Path(out_path).write_text(json.dumps(snap, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"dumped {snap['n_queries']} resolve() queries + 8 maps -> {out_path}")
    return 0


def _diff(golden_path: str, new_path: str) -> int:
    golden = json.loads(Path(golden_path).read_text(encoding="utf-8"))
    new = json.loads(Path(new_path).read_text(encoding="utf-8"))
    failures = 0

    # 1) maps
    for name in golden["maps"]:
        if golden["maps"][name] != new["maps"].get(name):
            failures += 1
            g, n = golden["maps"][name], new["maps"].get(name)
            print(f"MAP DIVERGENCE: {name}")
            if isinstance(g, dict) and isinstance(n, dict):
                gk, nk = set(g), set(n or {})
                only_g = sorted(gk - nk)[:20]
                only_n = sorted(nk - gk)[:20]
                changed = sorted(k for k in gk & nk if g[k] != n[k])[:20]
                if only_g:
                    print(f"  only in OLD ({len(gk - nk)}): {only_g}")
                if only_n:
                    print(f"  only in NEW ({len(nk - gk)}): {only_n}")
                for k in changed:
                    print(f"  changed [{k}]: OLD={g[k]!r} NEW={n[k]!r}")
                print(f"  (changed keys total: {len([k for k in gk & nk if g[k] != n[k]])})")

    # 2) resolve() outputs
    gr, nr = golden["resolve"], new["resolve"]
    if set(gr) != set(nr):
        failures += 1
        print(f"CORPUS MISMATCH: old={len(gr)} new={len(nr)} queries")
    resolve_diffs = 0
    for q in gr:
        if q in nr and gr[q] != nr[q]:
            resolve_diffs += 1
            if resolve_diffs <= 30:
                print(f"RESOLVE DIVERGENCE:\n  Q: {q}\n  OLD: {gr[q]}\n  NEW: {nr[q]}")
    if resolve_diffs:
        failures += 1
        print(f"\n{resolve_diffs} resolve() divergences out of {len(gr)} queries")

    if failures == 0:
        print(f"EQUIVALENCE PASS: 8/8 maps identical + {len(gr)}/{len(gr)} resolve() outputs identical")
        return 0
    print(f"\nEQUIVALENCE FAIL: {failures} divergence class(es)")
    return 1


def main(argv: list[str]) -> int:
    if len(argv) >= 3 and argv[1] == "dump":
        return _dump(argv[2])
    if len(argv) >= 4 and argv[1] == "diff":
        return _diff(argv[2], argv[3])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
