"""DM2 T4: 总闸 OFF → None (一行不跑); ON → 构建; ON 但目录缺/超限 → 启动 RuntimeError (fail-loud).
终审 I1: 一览条数 vs catalog.json 条数交叉核验 (不一致 = cards/ 漂移 → 拒启动)."""
import json

import pytest
from server import main as main_mod
from server.config import Settings


def _fixture(tmp_path):
    """→ (settings, cards_dir): 1 章 + 1 张卡的最小研读包夹具 (n_items == 1)."""
    docs = tmp_path / "docs"; cards = tmp_path / "cards"; docs.mkdir(); cards.mkdir()
    (docs / "a.md").write_text("---\ndoc_type: protocol_section\nsection_number: 4.1\npart: 1\n---\n\n4.1 T\nB\n", encoding="utf-8")
    (cards / "c.md").write_text("---\nstudy: st99\nversion: V\ndoc_type: field_card\nform_oid: FA\nsource_row: 1\n---\n\n# [偽 FA] x (I) \n- 型: text (len 1) / 必須\n", encoding="utf-8")
    s = Settings(dossier_enabled=True, dossier_prt_sections=["4"],
                 dossier_docs_dir_override=str(docs), dossier_cards_dir_override=str(cards))
    return s, cards

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
    s, _ = _fixture(tmp_path)
    d = main_mod.maybe_build_dossier(s)
    assert d is not None and d.sections == ("4.1",) and d.n_items == 1


def test_catalog_count_matches_builds(tmp_path):
    s, cards = _fixture(tmp_path)
    (cards.parent / "catalog.json").write_text(json.dumps({"items": [{"x": 1}]}), encoding="utf-8")
    d = main_mod.maybe_build_dossier(s)
    assert d is not None and d.n_items == 1


def test_catalog_count_mismatch_fails_loud(tmp_path):
    s, cards = _fixture(tmp_path)
    (cards.parent / "catalog.json").write_text(
        json.dumps({"items": [{"x": 1}, {"x": 2}]}), encoding="utf-8")
    with pytest.raises(RuntimeError, match="漂移"):
        main_mod.maybe_build_dossier(s)


def test_no_catalog_still_builds(tmp_path):
    """catalog 缺失 (override 目录 / 测试夹具) 只告警不拒启 —— 本文件不断言日志, 只钉不失败."""
    s, cards = _fixture(tmp_path)
    assert not (cards.parent / "catalog.json").exists()
    d = main_mod.maybe_build_dossier(s)
    assert d is not None and d.n_items == 1

def test_default_settings_have_dossier_on_with_s4_to_s12():
    s = Settings()
    assert s.dossier_enabled is True
    assert s.dossier_prt_sections == ["4", "5", "6", "7", "8", "9", "10", "11", "12"]


# ── 研读包答案闸的 index (spec 2026-09-25 §2): 缺失/坏掉 → None, 闸不跑, 不拒启动 ──

def test_gate_index_none_when_dossier_off(tmp_path):
    s, _ = _fixture(tmp_path)
    assert main_mod.maybe_build_dossier_gate_index(s, None) is None


def test_gate_index_none_when_catalog_missing_or_broken(tmp_path):
    s, cards = _fixture(tmp_path)
    d = main_mod.maybe_build_dossier(s)
    assert main_mod.maybe_build_dossier_gate_index(s, d) is None
    (cards.parent / "catalog.json").write_text("{not json", encoding="utf-8")
    assert main_mod.maybe_build_dossier_gate_index(s, d) is None


def test_gate_index_built_from_catalog(tmp_path):
    s, cards = _fixture(tmp_path)
    (cards.parent / "catalog.json").write_text(json.dumps(
        {"forms": [{"oid": "FORM_X"}], "items": [{"item_oid": "ITEM_Y1", "form_oid": "FORM_X"}]}),
        encoding="utf-8")
    d = main_mod.maybe_build_dossier(s)
    idx = main_mod.maybe_build_dossier_gate_index(s, d)
    assert idx is not None and idx.forms == {"FORM_X"} and idx.items == {"ITEM_Y1"}
    assert "DSDECOD" in idx.sdtm_names   # 白名单来自真实 KB (s.kb_root)


def test_gate_index_none_when_inconsistent_with_dossier(tmp_path):
    s, cards = _fixture(tmp_path)
    d = main_mod.maybe_build_dossier(s)
    cat = cards.parent / "catalog.json"
    # 一览 1 项, catalog 有 1 行但 forms 为空 ⇒ 闸不可用
    cat.write_text(json.dumps({"forms": [], "items": [{"item_oid": "ITEM_Y1"}]}), encoding="utf-8")
    assert main_mod.maybe_build_dossier_gate_index(s, d) is None
    # 项目数与研读包对不上 (直接喂一个 n_items 不同的研读包)
    cat.write_text(json.dumps({"forms": [{"oid": "FORM_X"}],
                               "items": [{"item_oid": "ITEM_Y1"}, {"item_oid": "ITEM_Y2"}]}),
                   encoding="utf-8")
    assert main_mod.maybe_build_dossier_gate_index(s, d) is None
