"""C1 Task 1: registry/路径解析支持 doc PDF. 合成 registry, 零真名 (Global Constraint 1/8)."""
import pytest
import yaml

from scripts.study.paths import resolve_study


def _write_registry(tmp_path, doc_names):
    src = tmp_path / "src"
    src.mkdir()
    (src / "cfg_new.xlsx").write_bytes(b"x")
    for n in doc_names:
        (src / n).write_bytes(b"%PDF-1.4\n")
    reg = {"st99": {"source_dir": str(src), "config_report_new": "cfg_new.xlsx",
                    "version_label_new": "vNEW", "doc_pdfs": list(doc_names)}}
    p = tmp_path / "studies.local.yaml"
    p.write_text(yaml.safe_dump(reg), encoding="utf-8")
    return p


def test_doc_pdfs_resolved_in_registry_order(tmp_path):
    reg = _write_registry(tmp_path, ["b.pdf", "a.pdf"])
    sp = resolve_study("st99", registry_path=reg)
    assert [p.name for p in sp.doc_pdfs] == ["b.pdf", "a.pdf"]
    assert all(p.is_absolute() for p in sp.doc_pdfs)


def test_docs_dir_sits_under_out_dir(tmp_path):
    reg = _write_registry(tmp_path, ["a.pdf"])
    sp = resolve_study("st99", registry_path=reg)
    assert sp.docs_dir == sp.out_dir / "docs"


def test_missing_doc_pdf_fails_loud(tmp_path):
    reg = _write_registry(tmp_path, ["a.pdf"])
    reg_data = yaml.safe_load(reg.read_text(encoding="utf-8"))
    reg_data["st99"]["doc_pdfs"] = ["a.pdf", "ghost.pdf"]
    reg.write_text(yaml.safe_dump(reg_data), encoding="utf-8")
    with pytest.raises(FileNotFoundError, match="ghost.pdf"):
        resolve_study("st99", registry_path=reg)


def test_doc_pdfs_defaults_to_empty_when_key_absent(tmp_path):
    """既有 st01 registry 没有 doc_pdfs 键 —— 不许因此炸掉 xlsx 轨."""
    reg = _write_registry(tmp_path, [])
    reg_data = yaml.safe_load(reg.read_text(encoding="utf-8"))
    reg_data["st99"].pop("doc_pdfs")
    reg.write_text(yaml.safe_dump(reg_data), encoding="utf-8")
    assert resolve_study("st99", registry_path=reg).doc_pdfs == ()
