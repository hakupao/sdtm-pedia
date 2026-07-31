"""CDISC ingest reset 测试 (Task 11): collection 级 reset, study_* 不受牵连。"""

import chromadb

from scripts import ingest
from scripts.ingest import reset_collection


def test_reset_collection_spares_others(tmp_path):
    cdir = tmp_path / "chroma"
    client = chromadb.PersistentClient(path=str(cdir))
    client.create_collection("sdtm_kb_v1")
    study = client.create_collection("study_st01")
    study.add(ids=["a"], documents=["d"], embeddings=[[0.0] * 3])

    reset_collection(cdir, "sdtm_kb_v1")

    c2 = chromadb.PersistentClient(path=str(cdir))
    assert c2.get_collection("study_st01").count() == 1
    assert "sdtm_kb_v1" not in {c.name for c in c2.list_collections()}


def test_reset_collection_missing_is_noop(tmp_path):
    reset_collection(tmp_path / "chroma", "absent")  # 不抛异常


def _stub_main(monkeypatch, tmp_path) -> list[str]:
    """让 main 只跑到 reset 就停 (collect_chunks 返回空 → 提前 return 2)。"""
    calls: list[str] = []
    monkeypatch.setattr(ingest, "CHROMA_DIR", tmp_path / "chroma")
    monkeypatch.setattr(ingest, "backup_existing_chroma", lambda d: None)
    monkeypatch.setattr(ingest, "reset_chroma_dir", lambda d: calls.append("full"))
    monkeypatch.setattr(ingest, "reset_collection", lambda d, n: calls.append(f"collection:{n}"))
    monkeypatch.setattr(ingest, "collect_chunks", lambda: ([], {}, []))
    return calls


def test_main_defaults_to_collection_reset(monkeypatch, tmp_path):
    calls = _stub_main(monkeypatch, tmp_path)
    assert ingest.main([]) == 2
    assert calls == [f"collection:{ingest.COLLECTION_NAME}"]


def test_main_full_reset_flag_keeps_old_behavior(monkeypatch, tmp_path):
    calls = _stub_main(monkeypatch, tmp_path)
    assert ingest.main(["--full-reset"]) == 2
    assert calls == ["full"]
