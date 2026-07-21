"""Deterministic CT-code grounding check (closes the substring metric's blind spot).

The paired fact-recall metric is blind to per-value C-code fabrication (a wrong code is not
penalized; q37/q44/q93 scored fine while emitting fabricated codes). This checker is the
deterministic gate the semantic judge recommended: for each answer it extracts every NCI
"C" code and classifies it as
  GROUNDED      — the code string appears in the question's re-retrieved context, OR
  UNGROUNDED    — not in context but exists somewhere in the KB (mis-cited), OR
  NONEXISTENT   — not anywhere in the knowledge_base (pure fabrication).
Rule 7 says every emitted code must be GROUNDED; UNGROUNDED+NONEXISTENT are violations.

Retrieval is guardrail-independent, so context is rebuilt with the production levers on.

Run from sdtm-rag/:
  .venv/bin/python eval/prod_wirein/check_code_grounding.py [forensic.json] [on|off]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from server.config import settings  # noqa: E402
from server.rag import RAGEngine  # noqa: E402

CODE_RE = re.compile(r"\bC\d{4,6}\b")
KB = settings.kb_root


def kb_code_set() -> set[str]:
    """Every distinct Cxxxxx that literally occurs anywhere in the knowledge base."""
    codes: set[str] = set()
    for md in KB.rglob("*.md"):
        codes.update(CODE_RE.findall(md.read_text(encoding="utf-8")))
    return codes


def prod_engine() -> RAGEngine:
    return RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name, embedding_model=settings.embedding_model,
        top_k=settings.top_k, structured_lookup_enabled=True, hybrid_enabled=True,
        hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=settings.hybrid_pool,
    )


def main() -> int:
    fpath = sys.argv[1] if len(sys.argv) > 1 else "eval/prod_wirein/forensic_guardrail.json"
    arm = sys.argv[2] if len(sys.argv) > 2 else "on"
    here = Path(__file__).parent
    fpath = fpath if Path(fpath).is_absolute() else str(here.parents[1] / fpath) if not Path(fpath).exists() else fpath
    raw = json.loads(Path(fpath).read_text())
    # Accept two shapes: forensic list [{id, question, on/off:{answer}}] OR a run_eval
    # report {summary, results:[{id, question, answer, answer_preview}]}.
    if isinstance(raw, dict) and "results" in raw:
        data = [{"id": r["id"], "question": r["question"],
                 arm: {"answer": r.get("answer", r.get("answer_preview", ""))}}
                for r in raw["results"] if r.get("answer") or r.get("answer_preview")]
    else:
        data = raw
    kb_codes = kb_code_set()
    eng = prod_engine()

    print(f"arm={arm}  file={fpath}  KB distinct codes={len(kb_codes)}")
    print(f"{'qid':6s} {'codes':5s} {'ground':6s} {'unground':8s} {'NONEXIST':8s}  ungrounded/nonexistent detail")
    print("-" * 110)
    tot = {"codes": 0, "grounded": 0, "ungrounded": 0, "nonexistent": 0}
    per_q = []
    for entry in data:
        qid = entry["id"]
        answer = entry[arm]["answer"]
        ctx = eng.format_context(eng.retrieve(entry["question"]))
        codes = CODE_RE.findall(answer)
        grounded = [c for c in codes if c in ctx]
        not_in_ctx = [c for c in codes if c not in ctx]
        nonexistent = [c for c in not_in_ctx if c not in kb_codes]
        ungrounded = [c for c in not_in_ctx if c in kb_codes]  # exists in KB but not in this context
        tot["codes"] += len(codes); tot["grounded"] += len(grounded)
        tot["ungrounded"] += len(ungrounded); tot["nonexistent"] += len(nonexistent)
        bad = ""
        if ungrounded:
            bad += "UNGROUNDED=" + ",".join(sorted(set(ungrounded)))
        if nonexistent:
            bad += "  NONEXISTENT=" + ",".join(sorted(set(nonexistent)))
        flag = "  <<<" if (ungrounded or nonexistent) else ""
        print(f"{qid:6s} {len(codes):5d} {len(grounded):6d} {len(ungrounded):8d} {len(nonexistent):8d}  {bad}{flag}")
        per_q.append({"id": qid, "n_codes": len(codes), "grounded": len(grounded),
                      "ungrounded": sorted(set(ungrounded)), "nonexistent": sorted(set(nonexistent))})
    print("-" * 110)
    print(f"TOTAL  codes={tot['codes']}  grounded={tot['grounded']}  "
          f"ungrounded(mis-cited)={tot['ungrounded']}  NONEXISTENT(fabricated)={tot['nonexistent']}")
    viol = tot["ungrounded"] + tot["nonexistent"]
    print(f"RULE-7 VIOLATIONS (ungrounded + nonexistent) = {viol}  "
          f"-> {'PASS (0 ungrounded codes)' if viol == 0 else 'FAIL'}")
    out = here / f"code_grounding_{arm}.json"
    out.write_text(json.dumps({"file": fpath, "arm": arm, "totals": tot, "per_q": per_q},
                              indent=2, ensure_ascii=False))
    print(f"saved -> {out}")
    return 0 if viol == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
