"""gold 唯一性 lint — 合成数据, 零真实 OID/label."""
import json
import pytest
from eval.lint_gold import lint_gold

CARDS = ["stx__FRM_A__ITEM_R", "stx__FRM_A__ITEM_RX", "stx__FRM_A__XITEM_R",
         "stx__FRM_B__SOLO", "stx__FRM_C__FAM_1", "stx__FRM_C__FAM_2"]


def _catalog(tmp_path):
    items = []
    for c in CARDS:
        _, form, oid = c.split("__")
        items.append({"form_oid": form, "item_oid": oid, "label": "偽ラベル"})
    p = tmp_path / "catalog.json"
    p.write_text(json.dumps({"study": "stx", "items": items}), encoding="utf-8")
    return p


def _raw_testset(tmp_path, questions):
    import yaml
    p = tmp_path / "ts.yml"
    p.write_text(yaml.safe_dump({"questions": questions}, allow_unicode=True), encoding="utf-8")
    return p


def _testset(tmp_path, golds):
    qs = [{"id": f"q{i:02d}", "question": "偽質問", "expected_sources": g}
          for i, g in enumerate(golds)]
    return _raw_testset(tmp_path, qs)


def test_unique_gold_passes(tmp_path):
    ts = _testset(tmp_path, [["stx__FRM_B__SOLO"]])
    assert lint_gold(ts, _catalog(tmp_path)) == []


def test_substring_of_sibling_is_flagged(tmp_path):
    # 卡名 ..__ITEM_R 是兄弟卡 ..__ITEM_RX 的前缀 → 子串匹配下命中干扰卡也算对
    ts = _testset(tmp_path, [["stx__FRM_A__ITEM_R"]])
    f = lint_gold(ts, _catalog(tmp_path))
    assert len(f) == 1 and f[0].n_matches == 2


def test_oid_level_substring_alone_is_not_flagged(tmp_path):
    # ITEM_R ⊂ XITEM_R 只在 OID 层成立; 带 form 前缀的完整卡名不互相包含。
    # 匹配必须与 check_source_recall 一样在完整卡名上做, 否则会误报好 gold。
    ts = _testset(tmp_path, [["stx__FRM_A__XITEM_R"]])
    assert lint_gold(ts, _catalog(tmp_path)) == []


def test_family_prefix_gold_is_flagged(tmp_path):
    ts = _testset(tmp_path, [["stx__FRM_C__FAM_"]])
    f = lint_gold(ts, _catalog(tmp_path))
    assert len(f) == 1 and f[0].n_matches == 2


def test_md_suffix_stripped_before_match(tmp_path):
    ts = _testset(tmp_path, [["stx__FRM_B__SOLO.md"]])
    assert lint_gold(ts, _catalog(tmp_path)) == []


def test_gold_matching_nothing_is_flagged(tmp_path):
    # 打错的 gold 恒 miss, 比多匹配更隐蔽 (永远 0 分, 看起来像检索差)
    ts = _testset(tmp_path, [["stx__FRM_Z__NOPE"]])
    f = lint_gold(ts, _catalog(tmp_path))
    assert len(f) == 1 and f[0].n_matches == 0


def test_max_matches_option_allows_declared_families(tmp_path):
    # 家族题合法: 显式声明允许 N 卡
    ts = _testset(tmp_path, [["stx__FRM_C__FAM_"]])
    assert lint_gold(ts, _catalog(tmp_path), max_matches=2) == []


def test_per_question_gold_max_matches_overrides_default(tmp_path):
    # 逐题声明: 只放宽这一题, 不把全卷阈值抬高
    ts = _raw_testset(tmp_path, [
        {"id": "q00", "question": "偽質問", "expected_sources": ["stx__FRM_C__FAM_"],
         "gold_max_matches": 2},
        {"id": "q01", "question": "偽質問", "expected_sources": ["stx__FRM_A__ITEM_R"]},
    ])
    f = lint_gold(ts, _catalog(tmp_path))
    assert [(x.qid, x.n_matches) for x in f] == [("q01", 2)]


def test_out_of_scope_question_is_skipped(tmp_path):
    ts = _raw_testset(tmp_path, [
        {"id": "q00", "question": "偽質問", "expected_sources": ["stx__FRM_C__FAM_"],
         "out_of_scope": True},
    ])
    assert lint_gold(ts, _catalog(tmp_path)) == []
