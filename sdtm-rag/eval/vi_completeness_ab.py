"""截断 vs 完整 context 的对照 — 本单元"改动前/后"数字的来源。

不做两次全量重灌: 同一问句喂两份 context (旧的 15 条截断版 / 新的完整版) 跑同一模型,
变量隔离得更干净 (只有那段正文变了)。

答题调用复用 eval/run_eval.py 的方式 (rag.build_messages + litellm.completion),
不另起一套模型配置。temperature=0.0 保证配对可复算。

用法: .venv/bin/python -m eval.vi_completeness_ab
"""
from __future__ import annotations

import litellm

from server.config import settings as s
from server.rag import RAGEngine

# gold fact = 该码表引用列表按字母序的末位 (必在第 15 位之后 = 旧正文结构上答不出)。
#
# 判据用**裸变量名**而非 `DOMAIN.VAR` 点号形式: 模型合法地会用按域分组的表格作答
# (`| UR | URORRESU, URSTRESU |`), 点号形式在这种答案里永远不出现 —— 初版用点号匹配
# 把一次正确作答误判成"无判别力"。SDTM 变量名自带域前缀故裸名全局唯一, 且实测裸名在
# 截断 context 里同样不存在, 判别力未被削弱 (见 main() 里的两条前置断言)。
#
# 这是本项目第 1 条硬规矩的同一个病: 判据检查工具必须与被检查对象逐字同语义。
CASES = [
    ("C66742", "VSLOBXFL",
     "Which SDTM domain variables reference the No Yes Response codelist C66742? "
     "List them exhaustively."),
    ("C71620", "URSTRESU",
     "Which SDTM domain variables reference the Unit codelist C71620? "
     "List them exhaustively."),
]


def _truncate_ct_line(text: str, keep: int = 15) -> str:
    """把完整的 CT chunk 正文退回旧生成器的 15 条截断形态。"""
    head, sep, tail = text.partition("variable(s): ")
    if not sep:
        return text
    refs = [r.strip().rstrip(".") for r in tail.split(",")]
    if len(refs) <= keep:
        return text
    return f"{head}{sep}{', '.join(refs[:keep])} ... ({len(refs)} total)."


def _answer(rag: RAGEngine, question: str, context: str) -> str:
    resp = litellm.completion(
        model=s.default_model,
        messages=rag.build_messages(question, context),
        temperature=0.0,
    )
    return resp.choices[0].message.content or ""


def main() -> int:
    rag = RAGEngine(
        chroma_dir=s.chroma_dir, kb_root=s.kb_root, collection_name=s.collection_name,
        embedding_model=s.embedding_model, top_k=s.top_k,
        structured_lookup_enabled=s.structured_lookup_enabled,
        hybrid_enabled=s.hybrid_enabled, hybrid_fusion=s.hybrid_fusion,
        hybrid_alpha=s.hybrid_alpha, hybrid_pool=s.hybrid_pool,
        prompt_guardrail_enabled=s.prompt_guardrail_enabled,
    )
    failures = 0
    for code, gold_fact, question in CASES:
        full_ctx = rag.format_context(rag.retrieve(question))
        trunc_ctx = "\n".join(_truncate_ct_line(seg) for seg in full_ctx.split("\n"))
        assert gold_fact in full_ctx, f"{code}: gold 不在完整 context 里 — 检索侧先出了问题"
        assert gold_fact not in trunc_ctx, f"{code}: 截断没生效, 对照无意义"

        got_full = gold_fact in _answer(rag, question, full_ctx)
        got_trunc = gold_fact in _answer(rag, question, trunc_ctx)
        ok = got_full and not got_trunc
        failures += 0 if ok else 1
        print(f"{code}  gold={gold_fact}  截断版={got_trunc}  完整版={got_full}"
              f"  -> {'判别力成立' if ok else '无判别力'}")

    print("\n注: 这里隔离的是 context 变量, 证明的是因果, 不等于线上答题必然变好。")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
