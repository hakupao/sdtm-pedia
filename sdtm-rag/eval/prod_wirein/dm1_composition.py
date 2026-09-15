"""DM1 final-review finding I1: 组成实验 — D3(域码扩写)/D5(BM25 查询侧泛词停用) 对
CDISC 15 席检索构成的影响。T8 闸的 recall 数字看不见这个收益 (140q/48q 零回归本就是
判据, 不是"零收益"的证据) —— 这个脚本把"收益"换成组成分布来量, 而不是靠肉眼一次性观察。

量的是同一个问句在四种杠杆构型下, 15 席里 DS-specific / IG overview / other 各占几席,
以及 `domains/DS/assumptions.md` (域定义段) 落在第几席。问句本身是 CDISC 侧英文域码
问法, 不含 study 私有信息, 可以明文入库。

跑 (从 sdtm-rag/):
  .venv/bin/python eval/prod_wirein/dm1_composition.py
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from server.config import settings  # noqa: E402
from server.domain_expand import build_expander  # noqa: E402
from server.rag import RAGEngine  # noqa: E402

QUESTION = "本研究中，哪些数据适合进入 sdtm 的 ds domain？"
TOP_K = 15
ASSUMPTIONS_SOURCE = "domains/DS/assumptions.md"

# (label, domain_definition_seat, domain_expand, bm25_query_stopwords)
ARMS = [
    ("all OFF", False, False, False),
    ("D2 seat only", True, False, False),
    ("D2+D3 expand", True, True, False),
    ("D2+D3+D5 (shipped)", True, True, True),
]


def build(seat: bool, expand: bool, stopwords: bool) -> RAGEngine:
    return RAGEngine(
        chroma_dir=settings.chroma_dir,
        kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model,
        top_k=TOP_K,
        structured_lookup_enabled=True,
        domain_definition_seat=seat,
        domain_expander=build_expander(settings) if expand else None,
        hybrid_enabled=settings.hybrid_enabled,
        hybrid_fusion=settings.hybrid_fusion,
        hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=settings.hybrid_pool,
        bm25_query_stopwords=stopwords,
    )


def bucket(source: str) -> str:
    """DS-specific = domains/DS/ 下的 chunk; IG overview = chapters/ 或 model/ 章节
    (implementation guide 通论); 其余 (其他域 spec、VARIABLE_INDEX 等) 记 other。"""
    if source.startswith("domains/DS/"):
        return "DS-specific"
    if source.startswith("chapters/") or source.startswith("model/"):
        return "IG overview"
    return "other"


def main() -> int:
    print(f"question={QUESTION!r}  top_k={TOP_K}\n")
    print(f"{'arm':<22}{'DS-specific':>12}{'IG overview':>13}{'other':>7}  assumptions seats")
    for label, seat, expand, stopwords in ARMS:
        eng = build(seat, expand, stopwords)
        sources = [c.source for c in eng.retrieve(QUESTION)]
        counts = Counter(bucket(s) for s in sources)
        seats = [i + 1 for i, s in enumerate(sources) if s == ASSUMPTIONS_SOURCE]
        seat_str = ",".join(str(i) for i in seats) if seats else "-"
        print(
            f"{label:<22}{counts.get('DS-specific', 0):>12}{counts.get('IG overview', 0):>13}"
            f"{counts.get('other', 0):>7}  {seat_str}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
