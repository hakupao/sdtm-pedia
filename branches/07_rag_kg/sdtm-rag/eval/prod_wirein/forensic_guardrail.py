"""Regenerate FULL (untruncated) guardrail-OFF vs guardrail-ON answers for the Rule A
independent semantic judge of the answer-side trust guardrail.

Both arms keep the production retrieval levers ON (structured_lookup + hybrid); the
ONLY thing toggled is the system-prompt guardrail (config.prompt_guardrail_enabled).
The 102q paired eval only stores truncated previews, so the judge needs full text to
rule on (a) per-value CT-code fabrication being gone, (b) q37 misclassification fixed,
(c) NO over-refusal -- grounded codelist codes (e.g. C66729 in spec.md) must survive.

Run from sdtm-rag/:  .venv/bin/python eval/prod_wirein/forensic_guardrail.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import litellm
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from server.config import settings  # noqa: E402
from server.rag import RAGEngine  # noqa: E402

MODEL = "deepseek/deepseek-chat"

# Purposive subset for the judge (full text), 3 strata:
#   DEFECT TARGETS   — must be FIXED by the guardrail
#   OVER-REFUSAL     — correct answer carries a GROUNDED codelist code/class; the
#                      guardrail must NOT suppress it (false-positive probe)
#   REGRESSION SPREAD— one+ per category, confirm no global answer harm
SUBSET = [
    # defect targets
    "q37", "q90", "q91", "q93",
    # over-refusal probes (gold = a grounded codelist C-code, or a grounded class)
    "q16", "q43", "q44", "s01", "s05", "q19",
    # regression spread across categories
    "q01", "q24", "q34", "q66", "q38", "q100",
]


def engine(guardrail: bool) -> RAGEngine:
    """Production-config engine (retrieval levers ON), guardrail toggled."""
    return RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name, embedding_model=settings.embedding_model,
        top_k=settings.top_k,
        structured_lookup_enabled=True, hybrid_enabled=True,
        hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=settings.hybrid_pool,
        prompt_guardrail_enabled=guardrail,
    )


def answer_with(eng: RAGEngine, ctx: str, q: str) -> str:
    """One completion using `eng`'s system prompt over a shared, pre-built context."""
    msgs = eng.build_messages(q, ctx)
    resp = litellm.completion(model=MODEL, messages=msgs, temperature=0.0)
    return resp.choices[0].message.content or ""


def main() -> int:
    here = Path(__file__).parent
    qset = {q["id"]: q for q in yaml.safe_load(Path("eval/test_set_v2.yml").read_text())}
    off, on = engine(False), engine(True)
    out = []
    # Optional CLI override: `forensic_guardrail.py <out.json> qid1 qid2 ...` regenerates
    # full off/on text for an arbitrary subset (used to give the judge full text for the
    # paired-eval fact DROPS, which the default 16q subset does not all cover).
    out_path = here / "forensic_guardrail.json"
    subset = SUBSET
    if len(sys.argv) > 1:
        out_path = here / sys.argv[1]
        if len(sys.argv) > 2:
            subset = sys.argv[2:]
    for qid in subset:
        if qid not in qset:
            print(f"[{qid}] NOT IN TEST SET -- skipped")
            continue
        q = qset[qid]
        # The guardrail is prompt-only and never touches retrieve(), so retrieval is
        # identical across arms: retrieve ONCE and feed the same context to both prompts.
        # Only the system prompt (guardrail off vs on) varies -> clean paired comparison.
        chunks = on.retrieve(q["question"])
        ctx = on.format_context(chunks)
        a_off = answer_with(off, ctx, q["question"])
        a_on = answer_with(on, ctx, q["question"])
        out.append({
            "id": qid, "category": q["category"], "question": q["question"],
            "expected_facts": q.get("expected_facts", []),
            "expected_sources": q.get("expected_sources", []),
            "sources": [c.source for c in chunks],
            "off": {"answer": a_off},
            "on": {"answer": a_on},
        })
        print(f"[{qid}] done")
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"wrote {len(out)} pairs -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
