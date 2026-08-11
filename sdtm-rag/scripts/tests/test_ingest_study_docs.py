"""C1 Task 5: ingest 合流. 合成 frontmatter, 零真名 (Global Constraint 8)."""
import pytest

from scripts.study.ingest_study import load_cards, load_doc_chunks

CARD = """---
study: st01
form_oid: FAKEFORM1
field_oid: FAKEIT1
---

# [偽フォーム一 FAKEFORM1] 偽項目ラベル一 (FAKEIT1)
"""

DOC = """---
study: st01
doc_type: protocol_section
doc_no: 1
section_number: 2.1
part: 1
parts_total: 1
page_start: 7
page_end: 8
version: vNEW
---

2.1 目的
本試験の目的。
"""


def _docs(tmp_path, name="st01__doc01__s2_1.md", text=DOC):
    d = tmp_path / "docs"
    d.mkdir(exist_ok=True)
    (d / name).write_text(text, encoding="utf-8")
    return d


def test_doc_chunk_metadata_shape(tmp_path):
    rec = load_doc_chunks(_docs(tmp_path))[0]
    m = rec["metadata"]
    assert m["study"] == "st01"
    assert m["file_type"] == "protocol_section"
    assert m["section"] == "2.1"
    assert m["source"] == "st01__doc01__s2_1.md"
    assert m["provenance"] == "doc01#p7-8"


def test_doc_chunk_domain_is_namespaced_not_empty(tmp_path):
    """domain='' 会静默逃出 RAGEngine._build_where 的域过滤 —— 与 load_cards 同款地雷。"""
    assert load_doc_chunks(_docs(tmp_path))[0]["metadata"]["domain"] == "doc01"


def test_doc_chunk_has_no_field_oid(tmp_path):
    """doc chunk 没有 field_oid —— S2 的确定性索引因此不会把它当卡片吃进去。"""
    assert "field_oid" not in load_doc_chunks(_docs(tmp_path))[0]["metadata"]


def test_missing_required_doc_key_fails_loud(tmp_path):
    bad = DOC.replace("section_number: 2.1\n", "")
    with pytest.raises(ValueError, match="section_number"):
        load_doc_chunks(_docs(tmp_path, text=bad))


def test_load_cards_still_requires_field_oid(tmp_path):
    """放宽必需键**只能**对 doc 轨生效; 卡片轨的既有防线一分不许松。"""
    cards = tmp_path / "cards"
    cards.mkdir()
    (cards / "st01__F__I.md").write_text(CARD.replace("field_oid: FAKEIT1\n", ""),
                                         encoding="utf-8")
    with pytest.raises(ValueError, match="field_oid"):
        load_cards(cards)


def test_missing_docs_dir_yields_empty_not_error(tmp_path):
    """C1 之前 docs/ 不存在 —— xlsx 轨必须照跑不误。"""
    assert load_doc_chunks(tmp_path / "nope") == []


def test_ids_do_not_collide_with_cards(tmp_path):
    doc_id = load_doc_chunks(_docs(tmp_path))[0]["id"]
    assert doc_id.startswith("st01__doc")


def test_multipart_chunk_records_part_in_provenance(tmp_path):
    """被二次切分的节: 溯源必须能区分是哪一份, 否则三份指向同一页区间无法定位。"""
    multi = (DOC.replace("part: 1", "part: 2").replace("parts_total: 1", "parts_total: 3")
                .replace("page_start: 7", "page_start: 63").replace("page_end: 8", "page_end: 70"))
    m = load_doc_chunks(_docs(tmp_path, "st01__doc01__s8_2__part02.md", multi))[0]["metadata"]
    assert m["provenance"] == "doc01#p63-70#part2of3"
    assert m["part"] == 2 and m["parts_total"] == 3


def test_part_defaults_to_single_when_keys_absent(tmp_path):
    """part/parts_total 是 C1 追加键; 缺失时按单份处理, 不炸。"""
    old = DOC.replace("part: 1\n", "").replace("parts_total: 1\n", "")
    m = load_doc_chunks(_docs(tmp_path, text=old))[0]["metadata"]
    assert m["part"] == 1 and m["parts_total"] == 1 and m["provenance"] == "doc01#p7-8"


def _study_fixture(tmp_path):
    """最小 study 目录: 1 张卡 + 1 个 doc chunk。"""
    cards = tmp_path / "cards"
    cards.mkdir()
    (cards / "st01__FAKEFORM1__FAKEIT1.md").write_text(CARD, encoding="utf-8")
    _docs(tmp_path)
    return tmp_path


def test_main_persists_docs_into_a_separate_collection(tmp_path, monkeypatch, capsys):
    """**分库是硬要求**: 章节 chunk 与 field card 同库时, 长篇章节在向量相似度上
    压过卡片, 占掉 top-5 的 1-4 席 —— 实测 study golden v2 87.5% → 78.1%
    (6 题回归 / 0 上升)。这条测试红了, 说明那个坑被重新挖开了。
    """
    from scripts.study import ingest_study as mod

    out = tmp_path / "st01"
    out.mkdir()
    _study_fixture(out)
    calls: list[tuple[str, list[str]]] = []
    monkeypatch.setattr(mod, "embed_texts", lambda texts: [[0.1] * 3 for _ in texts])
    monkeypatch.setattr(mod, "persist_study",
                        lambda _dir, col, recs, _emb: calls.append((col, [r["id"] for r in recs])))

    class _SP:
        study_id = "st01"
        cards_dir = out / "cards"
        docs_dir = out / "docs"
        out_dir = out

    monkeypatch.setattr(mod, "resolve_study", lambda _s: _SP())
    mod.main(["--study", "st01"])

    assert [c[0] for c in calls] == ["study_st01", "study_st01_docs"]
    cards_ids, docs_ids = calls[0][1], calls[1][1]
    assert cards_ids == ["st01__FAKEFORM1__FAKEIT1"]
    assert docs_ids == ["st01__doc01__s2_1"]
    assert not [i for i in cards_ids if "doc" in i], "doc chunk 混进了卡片 collection"
    assert "doc chunks 1" in capsys.readouterr().out


def test_main_drops_stale_docs_collection_when_docs_dir_empty(tmp_path, monkeypatch):
    """docs/ 清空却留着旧 collection = 静默陈旧数据, 必须响亮删掉。"""
    from scripts.study import ingest_study as mod

    out = tmp_path / "st01"
    (out / "cards").mkdir(parents=True)
    (out / "cards" / "st01__FAKEFORM1__FAKEIT1.md").write_text(CARD, encoding="utf-8")
    dropped: list[str] = []
    monkeypatch.setattr(mod, "embed_texts", lambda texts: [[0.1] * 3 for _ in texts])
    monkeypatch.setattr(mod, "persist_study", lambda *_a: None)
    monkeypatch.setattr(mod, "drop_collection_if_exists",
                        lambda _dir, col: dropped.append(col) or True)

    class _SP:
        study_id = "st01"
        cards_dir = out / "cards"
        docs_dir = out / "docs"      # 不存在
        out_dir = out

    monkeypatch.setattr(mod, "resolve_study", lambda _s: _SP())
    mod.main(["--study", "st01"])
    assert dropped == ["study_st01_docs"]


def test_s2_input_is_catalog_not_a_directory_scan():
    """S2 (零 LLM 确定性直查) 的输入是 catalog.json —— 由 xlsx 管线独家生成,
    doc 管线一个字都不动它。**doc chunk 因此在结构上进不了 S2**, 不是靠小心避开。

    这条断言钉的是**理由**: 若 StudyLookup 改成接受路径 / 扫目录, 它会红,
    提醒改动者重新评估 doc chunk 会不会污染那条通道。
    """
    import inspect

    from server.study_lookup import StudyLookup

    params = list(inspect.signature(StudyLookup.__init__).parameters)
    assert params[1] == "catalog", (
        f"S2 的首个入参变成了 {params[1]!r} —— 隔离理由可能已失效, 重新评估 doc chunk 污染风险")
    ann = inspect.signature(StudyLookup.__init__).parameters["catalog"].annotation
    assert ann in (dict, "dict"), f"catalog 注解变成 {ann!r}, 可能已改为路径输入"


def test_doc_pipeline_does_not_write_catalog(tmp_path):
    """反向钉一次: doc 管线的产物目录与 catalog.json 无交集。"""
    from scripts.study.render_doc_chunks import build_doc_chunks
    from scripts.study.split_sections import Section

    docs = tmp_path / "docs"
    build_doc_chunks("st01", docs, 1,
                     [Section("2.1", 2, "2.1 目的", "2.1 目的\n本文。\n", 1, 1)], "vNEW")
    assert [p.name for p in docs.iterdir()] == ["st01__doc01__s2_1.md"]
    assert not (tmp_path / "catalog.json").exists()
