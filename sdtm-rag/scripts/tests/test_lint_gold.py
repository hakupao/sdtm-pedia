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
        _, frm, oid = c.split("__")
        items.append({"form_oid": frm, "item_oid": oid, "label": "偽ラベル"})
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


# ---- OR 组 (expected_sources_any) ----------------------------------------
# OR 组不增加分母却多一次命中机会, 是最容易制造虚高的地方 (check_source_recall
# 的 docstring 记过一次实际翻车), 但初版 lint 完全没检查它。


def test_or_only_question_is_linted(tmp_path):
    # v2 q20 的形态: 只有 expected_sources_any, 没有 expected_sources。
    # 初版按 expected_sources 迭代 → 整题零覆盖。
    ts = _raw_testset(tmp_path, [
        {"id": "q00", "question": "偽質問", "expected_sources_any": ["stx__FRM_C__FAM_"]},
    ])
    f = lint_gold(ts, _catalog(tmp_path))
    assert len(f) == 1 and f[0].n_matches == 2 and f[0].side == "OR"


def test_or_group_with_unique_members_passes(tmp_path):
    ts = _raw_testset(tmp_path, [
        {"id": "q00", "question": "偽質問",
         "expected_sources_any": ["stx__FRM_B__SOLO.md", "stx__FRM_C__FAM_1.md"]},
    ])
    assert lint_gold(ts, _catalog(tmp_path)) == []


def test_finding_marks_and_vs_or_side(tmp_path):
    ts = _raw_testset(tmp_path, [
        {"id": "q00", "question": "偽質問",
         "expected_sources": ["stx__FRM_A__ITEM_R"],
         "expected_sources_any": ["stx__FRM_C__FAM_"]},
    ])
    assert sorted((x.side, x.n_matches) for x in lint_gold(ts, _catalog(tmp_path))) == [
        ("AND", 2), ("OR", 2)]


def test_gold_max_matches_does_not_relax_or_members(tmp_path):
    # OR 本身已是"任一命中即得分"的放宽; 再叠加家族放宽 = 两层稀释相乘。
    # 故 gold_max_matches 只作用于 AND 侧, OR 成员恒要求唯一定位。
    ts = _raw_testset(tmp_path, [
        {"id": "q00", "question": "偽質問", "gold_max_matches": 2,
         "expected_sources": ["stx__FRM_C__FAM_"],
         "expected_sources_any": ["stx__FRM_C__FAM_"]},
    ])
    f = lint_gold(ts, _catalog(tmp_path))
    assert [(x.side, x.n_matches) for x in f] == [("OR", 2)]


def test_or_members_counted_identically_to_and(tmp_path):
    """两个 gold 键必须走同一套计数 —— 否则 OR 侧会重演"工具与判据不同语义"。"""
    cat = _catalog(tmp_path)
    golds = ["stx__FRM_B__SOLO.md", "stx__FRM_A__ITEM_R", "stx__FRM_C__FAM_",
             "stx__FRM_Z__NOPE"]
    for i, gold in enumerate(golds):
        and_ts = _raw_testset(tmp_path, [{"id": "q", "question": "偽質問",
                                          "expected_sources": [gold]}], name=f"and{i}")
        or_ts = _raw_testset(tmp_path, [{"id": "q", "question": "偽質問",
                                         "expected_sources_any": [gold]}], name=f"or{i}")
        # max_matches=-1 让 AND 侧无条件上报, 取到真实匹配数
        n_and = lint_gold(and_ts, cat, max_matches=-1)[0].n_matches
        or_f = lint_gold(or_ts, cat)
        assert bool(or_f) == (n_and != 1), gold
        if or_f:
            assert or_f[0].n_matches == n_and, gold


def test_cli_prints_or_group_visibility_line(tmp_path, capsys):
    """OR 组即使全部合格也要打一行 —— 判别力稀释是成员数与相关性的函数,
    确定性检查查不了, 只能保证审题人每次都看见它。"""
    from eval.lint_gold import main

    ts = _raw_testset(tmp_path, [
        {"id": "q00", "question": "偽質問",
         "expected_sources_any": ["stx__FRM_B__SOLO.md", "stx__FRM_C__FAM_1.md"]},
    ])
    exit_code = main([str(ts), "--catalog", str(_catalog(tmp_path))])
    out = capsys.readouterr().out
    assert exit_code == 0
    assert "[OR]" in out and "q00" in out


def test_doc_chunk_names_returns_filenames_with_md(tmp_path):
    from eval.lint_gold import doc_chunk_names
    d = tmp_path / "docs"
    d.mkdir()
    (d / "st01__doc01__s10_1.md").write_text("x", encoding="utf-8")
    (d / "st01__doc01__s10_10.md").write_text("x", encoding="utf-8")
    assert doc_chunk_names(d) == ["st01__doc01__s10_1.md", "st01__doc01__s10_10.md"]


def test_doc_chunk_names_refuses_empty_dir(tmp_path):
    from eval.lint_gold import doc_chunk_names
    d = tmp_path / "docs"
    d.mkdir()
    with pytest.raises(ValueError, match="空全集"):
        doc_chunk_names(d)


def test_lint_gold_against_docs_dir(tmp_path):
    """docs 侧 gold 唯一性走同一份 lint 逻辑。"""
    from eval.lint_gold import lint_gold
    d = tmp_path / "docs"
    d.mkdir()
    for n in ("st01__doc01__s10_1.md", "st01__doc01__s10_10.md"):
        (d / n).write_text("x", encoding="utf-8")
    ts = tmp_path / "ts.yml"
    ts.write_text(
        "- id: q1\n"
        "  expected_sources: ['st01__doc01__s10_1.md']\n"
        "- id: q2\n"
        "  expected_sources: ['st01__doc01__s10_1']\n",   # 不带 .md → 匹配 2 个
        encoding="utf-8",
    )
    findings = lint_gold(str(ts), docs_dir=d)
    assert [f.qid for f in findings] == ["q2"]
    assert findings[0].n_matches == 2


def test_lint_gold_requires_exactly_one_name_source(tmp_path):
    from eval.lint_gold import lint_gold
    ts = tmp_path / "ts.yml"
    ts.write_text("- id: q1\n  expected_sources: ['a.md']\n", encoding="utf-8")
    with pytest.raises(ValueError, match="catalog 与 docs-dir"):
        lint_gold(str(ts))
