"""study field cards → chroma collection study_<id>. 只动自己的 collection."""
from __future__ import annotations

import argparse
from pathlib import Path

import chromadb

from scripts.ingest import CHROMA_DIR, embed_texts  # CHROMA_DIR: 与主库同目录不同 collection
from scripts.study.paths import resolve_study

_SKIP = {"INDEX.md", "ROUTING.md"}
_REQUIRED = ("study", "form_oid", "field_oid")


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
    collection = f"study_{sp.study_id}"
    print(f"cards={len(cards)} → collection={collection}")
    if args.dry_run:
        return
    embeddings = embed_texts([c["text"] for c in cards])
    persist_study(CHROMA_DIR, collection, cards, embeddings)
    (sp.out_dir / "ingested_at.txt").write_text(
        f"cards={len(cards)}\n", encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
