"""gold 唯一性 lint — 合成数据, 零真实 OID/label."""
import json
import pytest
from eval.lint_gold import lint_gold

# 卡的裸名 (无后缀); lint 与 retrieval 一样在带 `.md` 的完整卡名上匹配。
CARDS = ["stx__FRM_A__ITEM_R", "stx__FRM_A__ITEM_RX", "stx__FRM_A__XITEM_R",
         "stx__FRM_B__SOLO", "stx__FRM_C__FAM_1", "stx__FRM_C__FAM_2"]
# 兄弟卡形态必须用 ITEM_RX (gold 的**超串**): 匹配在完整卡名上做, 而
# `stx__FRM_A__ITEM_R` 并不是 `stx__FRM_A__XITEM_R` 的子串 (中间隔着 X)。


def _catalog(tmp_path):
    items = []
    for c in CARDS:
        _, form, oid = c.split("__")
        items.append({"form_oid": form, "item_oid": oid, "label": "偽ラベル"})
    p = tmp_path / "catalog.json"
    p.write_text(json.dumps({"study": "stx", "items": items}), encoding="utf-8")
    return p


def _raw_testset(tmp_path, questions, name="ts"):
    import yaml
    p = tmp_path / f"{name}.yml"
    p.write_text(yaml.safe_dump({"questions": questions}, allow_unicode=True), encoding="utf-8")
    return p


def _testset(tmp_path, golds, name="ts"):
    qs = [{"id": f"q{i:02d}", "question": "偽質問", "expected_sources": g}
          for i, g in enumerate(golds)]
    return _raw_testset(tmp_path, qs, name)


def test_unique_gold_passes(tmp_path):
    ts = _testset(tmp_path, [["stx__FRM_B__SOLO.md"]])
    assert lint_gold(ts, _catalog(tmp_path)) == []


def test_bare_gold_prefix_of_sibling_is_flagged(tmp_path):
    # 不带 `.md` 的 gold 会被更长的兄弟卡吃掉: ITEM_R ⊂ ITEM_RX.md → 命中干扰卡也算对
    ts = _testset(tmp_path, [["stx__FRM_A__ITEM_R"]])
    f = lint_gold(ts, _catalog(tmp_path))
    assert len(f) == 1 and f[0].n_matches == 2


def test_md_suffix_gives_discrimination(tmp_path):
    # 同一张卡: 带 `.md` 唯一定位, 不带就被兄弟卡吃掉。
    # `.md` 参与匹配 (`…ITEM_R.md` 不是 `…ITEM_RX.md` 的子串), 故**有判别力**。
    cat = _catalog(tmp_path)
    with_md = _testset(tmp_path, [["stx__FRM_A__ITEM_R.md"]], name="with_md")
    without = _testset(tmp_path, [["stx__FRM_A__ITEM_R"]], name="without")
    assert lint_gold(with_md, cat) == []
    assert [x.n_matches for x in lint_gold(without, cat)] == [2]


def test_oid_level_substring_alone_is_not_flagged(tmp_path):
    # 语义边界: OID 层互含但完整卡名不互含 → 不该报。
    # 防止后人"修"成 OID 级匹配 —— 那会误报好 gold, 且与 check_source_recall 脱节。
    ts = _testset(tmp_path, [["stx__FRM_A__XITEM_R"]])
    assert lint_gold(ts, _catalog(tmp_path)) == []


def test_family_prefix_gold_is_flagged(tmp_path):
    ts = _testset(tmp_path, [["stx__FRM_C__FAM_"]])
    f = lint_gold(ts, _catalog(tmp_path))
    assert len(f) == 1 and f[0].n_matches == 2


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


def test_section_level_gold_raises(tmp_path):
    # `路径#节` 在 check_source_recall 下是双条件匹配, catalog 建模不了 →
    # 必须报错而非静默按字面数 (静默 = 工具与判据不同语义, 正是本 lint 要消灭的病)
    ts = _testset(tmp_path, [["stx__FRM_B__SOLO.md#1.2"]])
    with pytest.raises(ValueError, match="section"):
        lint_gold(ts, _catalog(tmp_path))


def test_lint_semantics_match_check_source_recall(tmp_path):
    """闸: lint 数出的匹配数必须与 check_source_recall 的判定逐条一致。

    lint 是"判据检查工具", 一旦与判据不同语义就会制造假阳性 (初版剥 `.md` 即如此,
    在真实题集上误报了 8 条)。这条断言让改动任一侧都变红。
    """
    from eval.run_eval import check_source_recall

    golds = ["stx__FRM_B__SOLO.md", "stx__FRM_A__ITEM_R", "stx__FRM_A__ITEM_R.md",
             "stx__FRM_C__FAM_", "stx__FRM_C__FAM_1.md", "stx__FRM_Z__NOPE",
             "stx__FRM_A__XITEM_R"]
    sources = [f"{c}.md" for c in CARDS]
    ts = _testset(tmp_path, [[g] for g in golds])
    # max_matches=-1: 没有 gold 能匹配 -1 张卡, 于是每条都进 findings, 拿到其真实匹配数
    counted = {f.gold: f.n_matches for f in lint_gold(ts, _catalog(tmp_path), max_matches=-1)}

    assert set(counted) == set(golds)
    for gold in golds:
        judged = sum(1 for src in sources if check_source_recall([src], [gold])[0] == 1.0)
        assert counted[gold] == judged, f"{gold}: lint={counted[gold]} judge={judged}"
