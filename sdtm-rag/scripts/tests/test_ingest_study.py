"""study 卡片 ingest 测试 (Task 10): 元数据映射 + collection 级隔离。"""

from pathlib import Path

import chromadb
import pytest

from scripts.study.ingest_study import load_cards, persist_study

CARD = """---
study: st01
version: VNEW
doc_type: field_card
form_oid: FAKEFORM1
field_oid: FAKEIT1
source_sheet: Items and Groups
source_row: 5
generated_by: build_field_cards.py
---

# [偽フォーム一 FAKEFORM1] 偽項目ラベル一 (FAKEIT1)
- 型: integer / 必須
"""


@pytest.fixture()
def cards_dir(tmp_path) -> Path:
    d = tmp_path / "cards"
    d.mkdir()
    (d / "st01__FAKEFORM1__FAKEIT1.md").write_text(CARD, encoding="utf-8")
    (d / "INDEX.md").write_text("# idx", encoding="utf-8")
    (d / "ROUTING.md").write_text("# r", encoding="utf-8")
    return d


def test_load_cards_metadata(cards_dir):
    cards = load_cards(cards_dir)
    assert len(cards) == 1                      # INDEX/ROUTING 跳过
    c = cards[0]
    assert c["id"] == "st01__FAKEFORM1__FAKEIT1"
    assert c["metadata"]["domain"] == "FAKEFORM1"
    assert c["metadata"]["file_type"] == "field_card"
    assert c["metadata"]["field_oid"] == "FAKEIT1"
    assert "偽項目ラベル一" in c["text"]


def test_load_cards_rejects_missing_required_keys(tmp_path):
    """缺 frontmatter → 响亮报错, 而非静默产出 domain='' 逃出检索过滤。"""
    d = tmp_path / "cards"
    d.mkdir()
    (d / "st01__BAD__BAD1.md").write_text("# 无 frontmatter\n", encoding="utf-8")
    with pytest.raises(ValueError, match="st01__BAD__BAD1.md"):
        load_cards(d)


def test_persist_study_leaves_other_collections(tmp_path, cards_dir):
    client = chromadb.PersistentClient(path=str(tmp_path / "chroma"))
    other = client.create_collection("sdtm_kb_v1", metadata={"hnsw:space": "cosine"})
    other.add(ids=["x"], documents=["doc"], embeddings=[[0.0] * 3])
    cards = load_cards(cards_dir)
    persist_study(tmp_path / "chroma", "study_st01", cards,
                  [[0.1] * 3 for _ in cards])
    client2 = chromadb.PersistentClient(path=str(tmp_path / "chroma"))
    assert client2.get_collection("sdtm_kb_v1").count() == 1     # 未被破坏
    col = client2.get_collection("study_st01")
    assert col.count() == 1
    got = col.get(ids=["st01__FAKEFORM1__FAKEIT1"], include=["metadatas"])
    assert got["metadatas"][0]["form_oid"] == "FAKEFORM1"
