from pathlib import Path

import pytest
import yaml

from scripts.study.paths import StudyPaths, resolve_study


def _write_registry(tmp_path: Path) -> Path:
    src = tmp_path / "src_study"
    src.mkdir()
    (src / "new.xlsx").touch()
    (src / "old.xlsx").touch()
    reg = tmp_path / "studies.local.yaml"
    reg.write_text(yaml.safe_dump({
        "st01": {
            "version_label_new": "VNEW",
            "version_label_old": "VOLD",
            "source_dir": str(src),
            "config_report_new": "new.xlsx",
            "config_report_old": "old.xlsx",
            "demo_export": None,
        }
    }), encoding="utf-8")
    return reg


def test_resolve_study_returns_paths(tmp_path):
    reg = _write_registry(tmp_path)
    sp = resolve_study("st01", registry_path=reg)
    assert isinstance(sp, StudyPaths)
    assert sp.config_report_new.name == "new.xlsx" and sp.config_report_new.exists()
    assert sp.config_report_old is not None and sp.config_report_old.exists()
    assert sp.demo_export is None
    assert sp.out_dir.name == "st01"
    assert sp.cards_dir == sp.out_dir / "cards"


def test_resolve_study_unknown_id_raises(tmp_path):
    reg = _write_registry(tmp_path)
    with pytest.raises(KeyError):
        resolve_study("st99", registry_path=reg)


def test_resolve_study_missing_file_raises(tmp_path):
    reg = _write_registry(tmp_path)
    data = yaml.safe_load(reg.read_text())
    data["st01"]["config_report_new"] = "absent.xlsx"
    reg.write_text(yaml.safe_dump(data), encoding="utf-8")
    with pytest.raises(FileNotFoundError):
        resolve_study("st01", registry_path=reg)


def test_resolve_study_accepts_str_registry_path(tmp_path):
    reg = _write_registry(tmp_path)
    sp = resolve_study("st01", registry_path=str(reg))
    assert isinstance(sp, StudyPaths)
    assert sp.study_id == "st01"
    assert sp.config_report_new.exists()
    assert sp.out_dir.name == "st01"
