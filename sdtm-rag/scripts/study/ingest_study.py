"""study field cards → chroma collection study_<id>. 只动自己的 collection."""
from __future__ import annotations

import argparse
from pathlib import Path

import chromadb

from scripts.ingest import CHROMA_DIR, embed_texts  # CHROMA_DIR: 与主库同目录不同 collection
from scripts.study.paths import resolve_study

_SKIP = {"INDEX.md", "ROUTING.md"}
_REQUIRED = ("study", "form_oid", "field_oid")
_DOC_REQUIRED = ("study", "doc_type", "doc_no", "section_number", "page_start", "page_end")
# 章节 chunk 的独立 collection 后缀 (C1: 与 field card 分库, 理由见 main())
DOCS_SUFFIX = "_docs"


def _parse_frontmatter(text: str) -> dict[str, str]:
    parts = text.split("---\n")
    meta: dict[str, str] = {}
    if len(parts) >= 3:
        for line in parts[1].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta


def load_cards(cards_dir: Path) -> list[dict]:
    cards: list[dict] = []
    for p in sorted(cards_dir.glob("*.md")):
        if p.name in _SKIP:
            continue
        text = p.read_text(encoding="utf-8")
        fm = _parse_frontmatter(text)
        missing = [k for k in _REQUIRED if not fm.get(k)]
        if missing:
            # domain='' 会静默逃出 RAGEngine._build_where 过滤, 必须在 ingest 前拦住
            raise ValueError(f"{p.name}: frontmatter 缺必需键 {missing}")
        cards.append({
            "id": p.stem,
            "text": text,
            "metadata": {
                "study": fm["study"],
                "version": fm.get("version", ""),
                # domain/file_type/section 是有意映射: 复用 RAGEngine._build_where 过滤键
                "file_type": fm.get("doc_type", "field_card"),
                "domain": fm["form_oid"],
                "form_oid": fm["form_oid"],
                "field_oid": fm["field_oid"],
                "section": fm["form_oid"],
                # source 是检索侧的引用标识 (run_eval source recall 部分匹配 + webchat 显示),
                # 与 CDISC chunk 的文件路径语义对齐; xlsx 溯源另存 provenance
                "source": p.name,
                "provenance": f"{fm.get('source_sheet', '')}#row{fm.get('source_row', '')}",
            },
        })
    return cards


def load_doc_chunks(docs_dir: Path) -> list[dict]:
    """文档型 chunk (protocol 章节)。与 field card 同形状, 但**没有 field_oid** ——
    S2 的确定性直查因此不会把它当卡片吃进去 (那条通道按 label/OID 建索引)。

    docs_dir 不存在时返回空列表: C1 之前没有 docs/, xlsx 轨必须照跑不误。
    """
    if not docs_dir.is_dir():
        return []
    out: list[dict] = []
    for p in sorted(docs_dir.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        fm = _parse_frontmatter(text)
        missing = [k for k in _DOC_REQUIRED if not fm.get(k)]
        if missing:
            raise ValueError(f"{p.name}: doc chunk frontmatter 缺必需键 {missing}")
        doc_ns = f"doc{int(fm['doc_no']):02d}"
        part, parts_total = int(fm.get("part", 1) or 1), int(fm.get("parts_total", 1) or 1)
        prov = f"{doc_ns}#p{fm['page_start']}-{fm['page_end']}"
        if parts_total > 1:
            # 同一节的多份共用页区间, 不带份号就无法一步定位回源 (Global Constraint 4)
            prov = f"{prov}#part{part}of{parts_total}"
        out.append({
            "id": p.stem,
            "text": text,
            "metadata": {
                "study": fm["study"],
                "version": fm.get("version", ""),
                "file_type": fm["doc_type"],
                # domain 不留空: 空串会静默逃出 RAGEngine._build_where 的过滤
                "domain": doc_ns,
                "section": fm["section_number"],
                "part": part,
                "parts_total": parts_total,
                "source": p.name,
                "provenance": prov,
            },
        })
    return out


def persist_study(chroma_dir: Path, collection: str, cards: list[dict],
                  embeddings: list[list[float]]) -> None:
    client = chromadb.PersistentClient(path=str(chroma_dir))
    # Recreate own collection only — 同目录的主库 collection 不碰
    existing = [c.name for c in client.list_collections()]
    if collection in existing:
        client.delete_collection(collection)
    col = client.create_collection(name=collection, metadata={"hnsw:space": "cosine"})
    for i in range(0, len(cards), 1000):
        batch = cards[i : i + 1000]
        col.add(
            ids=[c["id"] for c in batch],
            documents=[c["text"] for c in batch],
            embeddings=embeddings[i : i + 1000],
            metadatas=[c["metadata"] for c in batch],
        )


def drop_collection_if_exists(chroma_dir: Path, collection: str) -> bool:
    client = chromadb.PersistentClient(path=str(chroma_dir))
    if collection in [c.name for c in client.list_collections()]:
        client.delete_collection(collection)
        return True
    return False


def main(argv=None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--study", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    sp = resolve_study(args.study)
    cards = load_cards(sp.cards_dir)
    if not cards:
        # 空数据换掉一个好 collection 比不换更糟
        raise SystemExit(f"no cards found in {sp.cards_dir}")
    docs = load_doc_chunks(sp.docs_dir)
    collection = f"study_{sp.study_id}"
    docs_collection = f"{collection}{DOCS_SUFFIX}"
    print(f"field cards {len(cards)} → {collection}; doc chunks {len(docs)} → {docs_collection}")
    if args.dry_run:
        return
    # 分库: 章节 chunk **不进卡片 collection**。实测同库混装时长篇章节在向量
    # 相似度上压过卡片, 占掉 top-5 的 1-4 席, study golden v2 87.5% → 78.1%
    # (6 题回归 / 0 上升)。persist_study 只重建自己那个 collection, 故两批互不抹。
    persist_study(CHROMA_DIR, collection, cards, embed_texts([c["text"] for c in cards]))
    if docs:
        persist_study(CHROMA_DIR, docs_collection, docs,
                      embed_texts([d["text"] for d in docs]))
    else:
        # docs/ 被清空却留着旧 collection = 静默陈旧数据, 宁可响亮删掉
        dropped = drop_collection_if_exists(CHROMA_DIR, docs_collection)
        if dropped:
            print(f"docs 目录为空 → 已删除陈旧 collection {docs_collection}")
    (sp.out_dir / "ingested_at.txt").write_text(
        f"cards={len(cards)}\ndoc_chunks={len(docs)}\n", encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
