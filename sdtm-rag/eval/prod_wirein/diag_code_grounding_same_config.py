"""V-1 诊断 (⛔ 不是判据): 用与生成完全一致的检索口径重建上下文, 量化 check_code_grounding.py
的口径差假阳性。

判据仍然是 `check_code_grounding.py` 的原口径结果 —— 本脚本**不修改也不替代**它。
存在理由: `check_code_grounding.py::prod_engine()` 写死 `structured_lookup_enabled=True,
hybrid_enabled=True`, 而 `run_eval.py` 这两个 lever 默认关。两者口径不同时, 判 ungrounded
所用的 top-15 不是模型当时看见的 top-15。

内置否定控制: 假码 C99999 必须不在重建上下文里 —— 否则说明 ctx 退化成了全库,
"全部 grounded" 就是脚本 bug 而不是结论。控制失败即 fail-loud。

跑法 (从 sdtm-rag/):
  .venv/bin/python eval/prod_wirein/diag_code_grounding_same_config.py \
      evidence/checkpoints/verified_runs/run_opus-5.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).parent))

from check_code_grounding import CODE_RE, kb_code_set  # noqa: E402

from server.config import settings  # noqa: E402
from server.rag import RAGEngine  # noqa: E402

FAKE_CODE = "C99999"


def generation_matched_engine() -> RAGEngine:
    """与 run_eval.py 不给任何检索 flag 时的实参一致 (rerank/expansion/lookup/hybrid 全关)。"""
    return RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name, embedding_model=settings.embedding_model,
        top_k=settings.top_k,
        rerank_enabled=False, query_expansion="none",
        structured_lookup_enabled=False, hybrid_enabled=False,
    )


def main() -> int:
    report_path = Path(sys.argv[1] if len(sys.argv) > 1
                       else "evidence/checkpoints/verified_runs/run_opus-5.json")
    if not report_path.is_absolute():
        report_path = ROOT / report_path
    report = json.loads(report_path.read_text())
    eng = generation_matched_engine()
    kb = kb_code_set()

    tot = {"codes": 0, "grounded": 0, "ungrounded": 0, "nonexistent": 0}
    per_q = []
    for r in report["results"]:
        ctx = eng.format_context(eng.retrieve(r["question"]))
        if FAKE_CODE in ctx:
            raise SystemExit(
                f"否定控制失败: {FAKE_CODE} 出现在 {r['id']} 的重建上下文里 ⇒ ctx 已退化成全库, "
                "本次 grounded 统计不可信"
            )
        codes = CODE_RE.findall(r["answer"])
        missing = [c for c in codes if c not in ctx]
        ungrounded = sorted({c for c in missing if c in kb})
        nonexistent = sorted({c for c in missing if c not in kb})
        tot["codes"] += len(codes)
        tot["grounded"] += len(codes) - len(missing)
        tot["ungrounded"] += sum(1 for c in missing if c in kb)
        tot["nonexistent"] += sum(1 for c in missing if c not in kb)
        per_q.append({"id": r["id"], "n_codes": len(codes),
                      "ungrounded": ungrounded, "nonexistent": nonexistent})
        if ungrounded or nonexistent:
            print(f"{r['id']:6s} codes={len(codes):3d}  "
                  f"UNGROUNDED={','.join(ungrounded) or '-'}  "
                  f"NONEXISTENT={','.join(nonexistent) or '-'}")

    print("-" * 90)
    print(f"否定控制: {FAKE_CODE} 在全部 {len(per_q)} 题的重建上下文中均未出现 ✓")
    print(f"SAME-CONFIG TOTALS: {tot}")
    out = Path(__file__).parent / f"diag_same_config_{report_path.stem}.json"
    out.write_text(json.dumps(
        {"source_run": str(report_path), "config": "generation-matched "
         "(structured_lookup=OFF, hybrid=OFF, rerank=OFF, expansion=none)",
         "negative_control": {"code": FAKE_CODE, "found_in_any_ctx": False},
         "totals": tot, "per_q": per_q}, indent=2, ensure_ascii=False))
    print(f"saved -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# ⚠ 2026-09-03 起本脚本已被**判据脚本本身**取代: `check_code_grounding.py` 现在读报告
# 落盘的 `retrieval_levers` 重建 (口径不再写死), 并内置保真闸 + 否定控制。
# 保留本文件只为让 evidence 里那次 V-1 诊断measurement 仍可原样复跑, 新工作不要用它。
