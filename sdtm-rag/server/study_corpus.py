"""U2: study 侧语料组合器 — field cards + 手順書章节 chunk (spec 2026-08-12 §4)。

设计要点:
- **加席不抢席**: cards 引擎的 top_k 原样传下去, doc 另取 seats 席追加在后。C1 实测
  同库混装会让长篇章节在向量相似度上压过卡片 (87.50% → 78.1%, 6 题回归), 所以这里
  既不同库也不共享席位 —— cards 的召回在结构上不可能被 doc 改变。
- **不做跨库分数排序**: 沿用联邦既有纪律 (两库相似度分布不可比)。
- **system_prompt 只来自 cards 引擎**: docs 引擎的 kb_root 指向 cards/ (RAGEngine 硬要求
  ROUTING.md/INDEX.md, docs/ 没有), 它自己的 system_prompt 描述的是卡片库, 读了就是错的。
- **本类不出 build_messages**: 联邦答题走 `FederatedEngine.build_messages` → cdisc 引擎
  (`federation.py:148`), 对本类只读 `system_prompt` (`:156/158`) 与 `retrieve/format_context`
  (`:122/129/143`)。留一份自己的 build_messages = 零测试守护的死代码; 删掉后真有人调它会
  AttributeError 响亮失败 (断言见 test_engine_builds_no_messages_of_its_own)。
- **retrieve 不收 `**kw`**: 席位数是本单元唯一的自变量, `**kw` 会把 `doc_seat=8` 这类拼写错
  静默吞成默认席位。联邦从不给 study 引擎传 domain/file_type (`federation.py:122/129`)。
"""
from __future__ import annotations

CARD_FILE_TYPE = "field_card"
DOC_FILE_TYPE = "protocol_section"

_DOC_CORPUS_RULES = (
    "\n\n## Study document rules\n"
    "- 本研究のコンテキストには 2 種類ある: 【EDC 項目カード】 (入力項目の定義) と "
    "【手順書章節】 (本研究自身の手順・計画文書の節)。どちらに基づく記述かを必ず示すこと。\n"
    "- 手順書章節は節番号を伴う。引用時は節番号を保持すること。\n"
)


class StudyCorpusEngine:
    """cards 引擎 + docs 引擎の組合せ。FederatedEngine から見た鴨型は RAGEngine と同じ。"""

    def __init__(self, cards, docs, *, doc_seats: int):
        if doc_seats < 0:
            raise ValueError(f"doc_seats must be >= 0, got {doc_seats}")
        self.cards = cards
        self.docs = docs
        self.doc_seats = doc_seats

    @property
    def system_prompt(self) -> str:
        return self.cards.system_prompt + _DOC_CORPUS_RULES

    def retrieve(self, question: str, *, top_k=None, doc_seats=None):
        seats = self.doc_seats if doc_seats is None else doc_seats
        if seats < 0:  # per-call 与 __init__ 同纪律: 非法席位数响亮失败, 不静默当 0
            raise ValueError(f"doc_seats must be >= 0, got {seats}")
        chunks = list(self.cards.retrieve(question, top_k=top_k))
        if seats <= 0:
            return chunks
        seen = {c.chunk_id for c in chunks}
        for d in self.docs.retrieve(question, top_k=seats):
            if d.chunk_id in seen:
                continue
            seen.add(d.chunk_id)
            chunks.append(d)
        return chunks

    def format_context(self, chunks) -> str:
        cards = [c for c in chunks if c.file_type != DOC_FILE_TYPE]
        docs = [c for c in chunks if c.file_type == DOC_FILE_TYPE]
        parts = []
        if cards:
            parts.append("## 【EDC 項目カード】\n" + self.cards.format_context(cards))
        if docs:
            parts.append("## 【手順書章節】\n" + self.docs.format_context(docs))
        return "\n\n".join(parts)
