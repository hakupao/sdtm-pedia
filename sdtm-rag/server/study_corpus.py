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

# 卡片侧没有对应常量: 分组用反选 (`!= DOC_FILE_TYPE`), 见 format_context —— 一个
# `CARD_FILE_TYPE` 常量全仓无引用, 留着只会诱导有人把反选改成正选 (那会让未知
# file_type 的 chunk 从 context 里静默消失)。
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
            parts.append("## 【EDC 項目カード】\n"
                         + self.cards.format_context(cards, glossary=False))
        if docs:
            parts.append("## 【手順書章節】\n" + self.docs.format_context(docs))
        ctx = "\n\n".join(parts)
        # L1 (EDC OID 対応表): 出すのは**組み合わせた文脈全体に対して末尾で一度だけ**。
        # cards 引擎の中で出させると (`glossary=False` を外すと) 二つ壊れる: ① 手順書
        # 章節に出てくる OID が訳されない (実測 125 doc 中 20 件に catalog の OID が
        # 出る) ② 対応表がカード節と手順書節の間に挟まって、どちらに掛かるのか形から
        # 読めない。docs 引擎には study_lookup を渡さない設計なので、対応表を引ける
        # 引擎は cards 側だけ —— 走査対象は `ctx` (両節を含む) を渡す。
        block = self.cards.glossary_block(ctx)
        return f"{ctx}\n\n{block}" if block else ctx


# ─────────────────────────── docs 引擎的唯一装配点 (Task 3b) ───────────────────────────
# docs 引擎被两条独立路径各造一次 (server/main.py 的 lifespan = 生产, eval/run_eval.py 的
# --study-docs 分支 = 尺子)。两处各抄一份参数清单则**没有任何东西钉它们相等**, 而漂移的
# 表现是"尺子全绿而生产是另一台引擎, 且不报错" —— 那会抽掉本单元全部数字的效力。
#
# 工厂**不读 settings 也不读 args**: 两侧各自解析自己的配置来源, 把解析结果传进来
# (eval 的 --hybrid 覆盖与生产的 settings 取值都因此保留)。被钉住的是**装配方式**,
# 不是取值来源。
DOCS_ENGINE_FIXED_KWARGS = {
    # S1 结构化直查是 CDISC 专属 (gold map 建在 spec.md xref + VARIABLE_INDEX 上,
    # 对 doc chunk 无定义)。
    "structured_lookup_enabled": False,
}

# 工厂自己写的键 + 恒不传的 study_lookup。levers 里出现任何一个 = 调用方在绕过本工厂的
# 约定。study_lookup 尤其危险: 它不与下面任何显式实参重名, 塞进去会**静默**给 docs 引擎
# 挂上 S2 直查 (S2 的数据源是 catalog.json, 对 doc chunk 同样无定义)。
_DOCS_ENGINE_OWNED_KWARGS = frozenset(
    {"chroma_dir", "kb_root", "collection_name", "embedding_model", "top_k", "study_lookup"}
    | set(DOCS_ENGINE_FIXED_KWARGS)
)


def make_docs_engine(rag_cls, *, chroma_dir, kb_root, collection_name,
                     embedding_model, seats, levers: dict):
    """把已解析好的配置装配成一台 docs 引擎。`seats` 即该引擎的 top_k。

    `levers` 是检索杠杆 (hybrid 一族 / rerank 一族 / query expansion 一族 / 答题护栏),
    调用方必须传**与同一次运行里 cards 引擎相同**的那一份。
    """
    clash = sorted(_DOCS_ENGINE_OWNED_KWARGS & set(levers))
    if clash:
        raise ValueError(
            f"levers must not carry docs-engine-owned kwargs: {clash}"
        )
    return rag_cls(
        chroma_dir=chroma_dir,
        kb_root=kb_root,
        collection_name=collection_name,
        embedding_model=embedding_model,
        # 惰性参数: StudyCorpusEngine.retrieve 每次都显式传 top_k=seats, 而 rag.py:263 是
        # `k = top_k or self.top_k` ⇒ 右支在组合器路径上永不取值。改这里调不动席位。
        top_k=seats,
        **DOCS_ENGINE_FIXED_KWARGS,
        **levers,
    )
