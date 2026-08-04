from pathlib import Path

import pytest
import yaml

from scripts.study import paths as paths_mod
from scripts.study.paths import STUDY_DATA_ROOT, StudyPaths, resolve_study


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


def _write_registry_with_id(tmp_path: Path, study_id: str) -> Path:
    reg = _write_registry(tmp_path)
    data = yaml.safe_load(reg.read_text())
    data[study_id] = data.pop("st01")
    reg.write_text(yaml.safe_dump(data), encoding="utf-8")
    return reg


# I-2 回归: 生产路径 (registry_path=None) 下 out_dir 逃逸 STUDY_DATA_ROOT 必须拒绝,
# 且是 raise 而非 assert (python -O 下 assert 被剥).
def test_production_out_dir_escape_raises(tmp_path, monkeypatch):
    reg = _write_registry_with_id(tmp_path, "../evil")
    monkeypatch.setattr(paths_mod, "DEFAULT_REGISTRY", reg)
    with pytest.raises(RuntimeError, match="STUDY_DATA_ROOT"):
        resolve_study("../evil")


# I-2 回归 (正路径): 生产路径下 out_dir 落在 STUDY_DATA_ROOT 之下.
def test_production_out_dir_within_root(tmp_path, monkeypatch):
    reg = _write_registry(tmp_path)
    monkeypatch.setattr(paths_mod, "DEFAULT_REGISTRY", reg)
    sp = resolve_study("st01")
    assert sp.out_dir == (STUDY_DATA_ROOT / "st01").resolve()
    assert sp.out_dir.is_relative_to(STUDY_DATA_ROOT)


# I-3 回归: 相对 registry_path + 任意 cwd, out_dir 仍是绝对路径且锚在注册表旁.
def test_relative_registry_path_gives_absolute_out_dir(tmp_path, monkeypatch):
    _write_registry(tmp_path)
    monkeypatch.chdir(tmp_path)
    sp = resolve_study("st01", registry_path="studies.local.yaml")
    assert sp.out_dir.is_absolute()
    assert sp.out_dir == (tmp_path / "st01").resolve()


# 空串守卫: registry_path="" 不得静默回落到生产注册表并旁路安全闸.
# DEFAULT_REGISTRY 换成有效注册表: 若空串回落, 旧码会成功解析而非抛错 (CI 上无本地注册表也不假绿).
def test_empty_registry_path_rejected(tmp_path, monkeypatch):
    reg = _write_registry(tmp_path)
    monkeypatch.setattr(paths_mod, "DEFAULT_REGISTRY", reg)
    with pytest.raises(FileNotFoundError):
        resolve_study("st01", registry_path="")


# ---- P3: _file() optional 分支 ----

def test_optional_key_absent_returns_none(tmp_path):
    reg = _write_registry(tmp_path)
    data = yaml.safe_load(reg.read_text())
    del data["st01"]["demo_export"], data["st01"]["config_report_old"]
    del data["st01"]["version_label_old"]
    reg.write_text(yaml.safe_dump(data), encoding="utf-8")
    sp = resolve_study("st01", registry_path=reg)
    assert sp.demo_export is None and sp.config_report_old is None
    assert sp.version_label_old is None


def test_optional_file_missing_raises(tmp_path):
    reg = _write_registry(tmp_path)
    data = yaml.safe_load(reg.read_text())
    data["st01"]["demo_export"] = "absent_demo.xlsx"
    reg.write_text(yaml.safe_dump(data), encoding="utf-8")
    with pytest.raises(FileNotFoundError, match="demo_export"):
        resolve_study("st01", registry_path=reg)
