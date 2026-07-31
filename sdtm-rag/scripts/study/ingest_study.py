"""study field cards → chroma collection study_<id>. 只动自己的 collection."""
from __future__ import annotations

import argparse
from pathlib import Path

import chromadb

from scripts.ingest import embed_texts
from scripts.study.paths import resolve_study

_SKIP = {"INDEX.md", "ROUTING.md"}


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
        cards.append({
            "id": p.stem,
            "text": text,
            "metadata": {
                "study": fm.get("study", ""),
                "version": fm.get("version", ""),
                # domain/file_type/section 是有意映射: 复用 RAGEngine._build_where 过滤键
                "file_type": fm.get("doc_type", "field_card"),
                "domain": fm.get("form_oid", ""),
                "form_oid": fm.get("form_oid", ""),
                "field_oid": fm.get("field_oid", ""),
                "section": fm.get("form_oid", ""),
                "source": f"{fm.get('source_sheet', '')}#row{fm.get('source_row', '')}",
            },
        })
    return cards


def persist_study(chroma_dir: Path, collection: str, cards: list[dict],
                  embeddings: list[list[float]]) -> None:
    client = chromadb.PersistentClient(path=str(chroma_dir))
    try:
        client.delete_collection(collection)
    except Exception:
        pass
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
    collection = f"study_{sp.study_id}"
    print(f"cards={len(cards)} → collection={collection}")
    if args.dry_run:
        return
    embeddings = embed_texts([c["text"] for c in cards])
    from scripts.ingest import CHROMA_DIR  # data/chroma, 与主库同目录不同 collection
    persist_study(CHROMA_DIR, collection, cards, embeddings)
    (sp.out_dir / "ingested_at.txt").write_text(
        f"cards={len(cards)}\n", encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
