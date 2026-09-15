"""DM2 T4: 总闸 OFF → None (一行不跑); ON → 构建; ON 但目录缺/超限 → 启动 RuntimeError (fail-loud)."""
import pytest
from server import main as main_mod
from server.config import Settings

def test_off_returns_none_without_touching_disk(tmp_path):
    s = Settings(dossier_enabled=False, dossier_docs_dir_override=str(tmp_path / "nope"),
                 dossier_cards_dir_override=str(tmp_path / "nope"))
    assert main_mod.maybe_build_dossier(s) is None

def test_on_missing_dir_fails_loud(tmp_path):
    s = Settings(dossier_enabled=True, dossier_docs_dir_override=str(tmp_path / "nope"),
                 dossier_cards_dir_override=str(tmp_path / "nope"))
    with pytest.raises(RuntimeError, match="dossier"):
        main_mod.maybe_build_dossier(s)

def test_on_builds(tmp_path):
    docs = tmp_path / "docs"; cards = tmp_path / "cards"; docs.mkdir(); cards.mkdir()
    (docs / "a.md").write_text("---\ndoc_type: protocol_section\nsection_number: 4.1\npart: 1\n---\n\n4.1 T\nB\n", encoding="utf-8")
    (cards / "c.md").write_text("---\nstudy: st99\nversion: V\ndoc_type: field_card\nform_oid: FA\nsource_row: 1\n---\n\n# [偽 FA] x (I) \n- 型: text (len 1) / 必須\n", encoding="utf-8")
    s = Settings(dossier_enabled=True, dossier_prt_sections=["4"],
                 dossier_docs_dir_override=str(docs), dossier_cards_dir_override=str(cards))
    d = main_mod.maybe_build_dossier(s)
    assert d is not None and d.sections == ("4.1",) and d.n_items == 1

def test_default_settings_have_dossier_on_with_s4_to_s12():
    s = Settings()
    assert s.dossier_enabled is True
    assert s.dossier_prt_sections == ["4", "5", "6", "7", "8", "9", "10", "11", "12"]
