"""Regenerate FULL (untruncated) off-vs-on answers for a subset of questions at
temp=0, for the Rule A independent semantic judge. The 102q eval only stored
600-char previews; the judge needs full text to rule on real correctness/dilution.
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
# drops (5) + gains (5) + stratified spot-check across categories
SUBSET = ["q02", "q24", "q34", "q66", "q93",          # deterministic drops
          "q37", "s05", "q64", "q91", "q100",         # deterministic gains
          "q01", "q38", "q07", "q19", "q90"]          # spot-check (single/concept/cross/mixed/?)


def engine(structured: bool, hybrid: bool) -> RAGEngine:
    return RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name, embedding_model=settings.embedding_model,
        top_k=settings.top_k, structured_lookup_enabled=structured,
        hybrid_enabled=hybrid, hybrid_fusion=settings.hybrid_fusion,
        hybrid_alpha=settings.hybrid_alpha, hybrid_pool=settings.hybrid_pool,
    )


def answer(eng: RAGEngine, q: str) -> tuple[str, list[str]]:
    chunks = eng.retrieve(q)
    ctx = eng.format_context(chunks)
    msgs = eng.build_messages(q, ctx)
    resp = litellm.completion(model=MODEL, messages=msgs, temperature=0.0)
    return resp.choices[0].message.content or "", [c.source for c in chunks]


def main() -> int:
    qset = {q["id"]: q for q in yaml.safe_load(Path("eval/test_set_v2.yml").read_text())}
    off, on = engine(False, False), engine(True, True)
    out = []
    for qid in SUBSET:
        if qid not in qset:
            continue
        q = qset[qid]
        a_off, s_off = answer(off, q["question"])
        a_on, s_on = answer(on, q["question"])
        out.append({
            "id": qid, "category": q["category"], "question": q["question"],
            "expected_facts": q.get("expected_facts", []),
            "expected_sources": q.get("expected_sources", []),
            "off": {"answer": a_off, "sources": s_off},
            "on": {"answer": a_on, "sources": s_on},
        })
        print(f"[{qid}] done")
    Path("eval/prod_wirein/forensic_answers.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False)
    )
    print(f"wrote {len(out)} pairs -> eval/prod_wirein/forensic_answers.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
