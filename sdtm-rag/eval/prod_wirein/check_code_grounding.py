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
from server.domain_expand import build_expander  # noqa: E402
from server.rag import RAGEngine  # noqa: E402

CODE_RE = re.compile(r"\bC\d{4,6}\b")
KB = settings.kb_root

# `run_eval.py` 不给任何检索 flag 时的实参。给**没有** `retrieval_levers` 字段的老报告
# 兜底用。⛔ 不是"安全默认"而是"最可能的猜测" —— 猜错由 check_fidelity 当场炸。
_RUN_EVAL_DEFAULT_LEVERS = {
    "top_k": 15,  # run_eval.TOP_K
    "structured_lookup": False,
    "hybrid": False,
    "rerank": False,
    "query_expansion": "none",
}


# KB 里不存在的码, 用作否定控制。它若出现在"上下文"里, 说明上下文不是 top-k 而是整库。
FAKE_CODE = "C99999"


class ReconstructionMismatchError(RuntimeError):
    """重建的检索结果与生成时落盘的不一致 ⇒ 上下文不是模型看见的那个 ⇒ 不出数。"""


class DegenerateContextError(RuntimeError):
    """上下文退化 (疑似整库) ⇒ 什么码都会"grounded" ⇒ 假 PASS ⇒ 不出数。"""


def assert_context_not_degenerate(qid: str, ctx: str) -> None:
    """否定控制: 保真闸比的是 `retrieve()` 的输出, 拦不住 `format_context` 把整库拼进来。

    整库拼进来会让每个码都判 grounded —— 这是本判据唯一的假 PASS 通道, 必须单独堵。
    """
    if FAKE_CODE in ctx:
        raise DegenerateContextError(
            f"{qid}: 否定控制失败 —— KB 中不存在的 {FAKE_CODE} 出现在重建上下文里 ⇒ "
            "上下文疑似退化成整库, grounded 统计不可信, 拒绝出数。"
        )


def kb_code_set() -> set[str]:
    """Every distinct Cxxxxx that literally occurs anywhere in the knowledge base."""
    codes: set[str] = set()
    for md in KB.rglob("*.md"):
        codes.update(CODE_RE.findall(md.read_text(encoding="utf-8")))
    return codes


def levers_from_report(raw) -> dict:
    """报告落盘的检索实参; 老报告 (无该字段) 退回 run_eval 默认。

    ⚠ V-1: 这里曾经写死 `structured_lookup=ON, hybrid=ON`, 与生成口径不符,
    导致 102 题无一还原、8 条 ungrounded 全是假阳性。
    """
    summary = raw.get("summary", {}) if isinstance(raw, dict) else {}
    return {**_RUN_EVAL_DEFAULT_LEVERS, **summary.get("retrieval_levers", {})}


def engine_kwargs_from_levers(levers: dict) -> dict:
    return {
        "top_k": levers["top_k"],
        "structured_lookup_enabled": levers["structured_lookup"],
        # T4 起才有的通道。缺键 = 那轮跑的时候它还不存在 = OFF。这里**必须**显式给值:
        # RAGEngine 的构造默认是 True, 不给就会按一条老报告重建出多一条注入通道的引擎,
        # top5 与落盘的对不上, check_fidelity 把整批老档案判成重建失败。
        "domain_definition_seat": levers.get("domain_definition_seat", False),
        "hybrid_enabled": levers["hybrid"],
        "rerank_enabled": levers["rerank"],
        "query_expansion": levers["query_expansion"],
        # T5 起才有的通道。缺键 = 那轮跑的时候它还不存在 = OFF (同 domain_definition_seat)。
        # `settings.domain_expand_enabled` 默认 True, 不显式给 None 就会按老报告重建出一台
        # 会扩写问句的引擎 ⇒ 稠密/BM25 查的不是当时那段文本, top5 与落盘的对不上。
        # lever 落的是 bool, 引擎收的是对象 —— 造对象只在 True 分支发生 (本函数对老报告
        # 保持零 IO)。
        "domain_expander": (
            build_expander(settings) if levers.get("domain_expand", False) else None
        ),
        # T6 起才有的通道。缺键 = 那轮跑的时候它还不存在 = OFF (同 domain_definition_seat /
        # domain_expander): RAGEngine 构造默认是 True, 不给就会按老报告重建出一台会停用
        # 泛用语的引擎 ⇒ query 侧 BM25 tokenize 用的停用表和当时那轮不一致, top5 对不上。
        "bm25_query_stopwords": levers.get("bm25_query_stopwords", False),
    }


def check_fidelity(qid: str, recorded_top5: list, rebuilt_top5: list) -> None:
    """重建的 top5 必须与报告落盘的 `top5_sources` **逐位相同**。

    顺序算数: `format_context` 按序拼上下文。集合相同顺序不同 = 没还原。
    """
    if list(recorded_top5) != list(rebuilt_top5):
        raise ReconstructionMismatchError(
            f"{qid}: 重建的检索结果 != 生成时落盘的 top5_sources ⇒ 重建口径不对, 拒绝出数。\n"
            f"  落盘: {list(recorded_top5)}\n"
            f"  重建: {list(rebuilt_top5)}\n"
            f"  查 report['summary']['retrieval_levers'] 与本机 chroma 索引是否同一版。"
        )


def prod_engine(levers: dict | None = None) -> RAGEngine:
    """按 `levers` 重建生成时的引擎 (默认走 run_eval 无 flag 的实参)。"""
    return RAGEngine(
        chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
        collection_name=settings.collection_name, embedding_model=settings.embedding_model,
        hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=settings.hybrid_pool,
        **engine_kwargs_from_levers(levers or _RUN_EVAL_DEFAULT_LEVERS),
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
                 "top5_sources": r.get("top5_sources"),
                 arm: {"answer": r.get("answer", r.get("answer_preview", ""))}}
                for r in raw["results"] if r.get("answer") or r.get("answer_preview")]
    else:
        data = raw
    kb_codes = kb_code_set()
    levers = levers_from_report(raw)
    eng = prod_engine(levers)

    print(f"arm={arm}  file={fpath}  KB distinct codes={len(kb_codes)}")
    print(f"retrieval levers (rebuilt to match generation): {levers}")
    print(f"{'qid':6s} {'codes':5s} {'ground':6s} {'unground':8s} {'NONEXIST':8s}  ungrounded/nonexistent detail")
    print("-" * 110)
    tot = {"codes": 0, "grounded": 0, "ungrounded": 0, "nonexistent": 0}
    per_q = []
    n_verified = 0
    for entry in data:
        qid = entry["id"]
        answer = entry[arm]["answer"]
        chunks = eng.retrieve(entry["question"])
        # V-1 保真闸: 重建对不上落盘的检索结果 ⇒ 上下文不是模型看见的那个 ⇒ 当场炸, 不出数
        recorded = entry.get("top5_sources")
        if recorded is not None:
            check_fidelity(qid, recorded, [c.source for c in chunks][:5])
            n_verified += 1
        ctx = eng.format_context(chunks)
        assert_context_not_degenerate(qid, ctx)
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
    if n_verified:
        print(f"重建保真: {n_verified}/{len(data)} 题的 top5 与生成时落盘的一致 ✓")
    else:
        print("⚠ 重建保真**未验证**: 输入没有 top5_sources (老 forensic 格式) ⇒ "
              "无法证明重建的上下文就是模型当时看见的那个, 下面的数字据此打折。")
    print(f"TOTAL  codes={tot['codes']}  grounded={tot['grounded']}  "
          f"ungrounded(mis-cited)={tot['ungrounded']}  NONEXISTENT(fabricated)={tot['nonexistent']}")
    viol = tot["ungrounded"] + tot["nonexistent"]
    print(f"RULE-7 VIOLATIONS (ungrounded + nonexistent) = {viol}  "
          f"-> {'PASS (0 ungrounded codes)' if viol == 0 else 'FAIL'}")
    out = here / f"code_grounding_{arm}.json"
    out.write_text(json.dumps({"file": fpath, "arm": arm, "retrieval_levers": levers,
                               "fidelity_verified": f"{n_verified}/{len(data)}",
                               "totals": tot, "per_q": per_q},
                              indent=2, ensure_ascii=False))
    print(f"saved -> {out}")
    return 0 if viol == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
