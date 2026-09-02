"""ch03 的 Dataset-level Metadata 表是 guardrail rule 8 的权威出处 —— (b) 层的全部判定
都拿它做锚。⚠ 抽取端一旦失效 (表头改了/切割错了), 下游"与权威表一致"会退化成
"与空表一致" = 恒真 (retrospective 规则 6 成因 A) ⇒ 本文件的闸重点全在抽取端本身。"""
from pathlib import Path

import pytest

from eval.prod_wirein.class_authority import authority_table_markdown, load_class_authority

_EXPECTED_CLASSES = {
    "Events", "Findings", "Findings About", "Interventions",
    "Relationship", "Special Purpose", "Study Reference", "Trial Design",
}


def test_authority_has_every_dataset_and_class():
    """尺寸下限 + 取值集合双向钉。⛔ 只断"非空"不够: 抽出 1 行也非空, 而下游判定照绿。"""
    m = load_class_authority()
    assert len(m) >= 60, f"抽取端失效, 只拿到 {len(m)} 行: {sorted(m)[:5]}"
    assert set(m.values()) == _EXPECTED_CLASSES, f"Class 取值集合变了: {sorted(set(m.values()))}"


def test_authority_spot_values():
    """绝对值锚 —— 每个 Class 至少钉一个真实条目。集合断言对"全表塌成一个 Class"无分辨力。"""
    m = load_class_authority()
    assert m["AE"] == "Events"
    assert m["LB"] == "Findings"
    assert m["FA"] == "Findings About"
    assert m["CM"] == "Interventions"
    assert m["RELREC"] == "Relationship"
    assert m["CO"] == "Special Purpose"
    assert m["TA"] == "Trial Design"


def test_supp_is_keyed_by_the_pattern_not_the_word():
    """⚠ 实测坑: 表里的键是 `SUPP--`, 而 ch03 里 "SUPPQUAL" 出现 **0 次**。
    ⇒ 「SUPPQUAL is a special-purpose dataset」这种断言**按字面查不到**。
    Task 3 的提示词必须显式告诉裁判这个变体, 否则它会把查不到当成"没断言"。"""
    m = load_class_authority()
    assert m["SUPP--"] == "Relationship"
    assert "SUPPQUAL" not in m


def test_loader_fails_loud_on_a_broken_table(tmp_path: Path):
    """反方向: 表被改坏时必须**当场炸**, ⛔ 不许返回一个短表让下游静默恒真。"""
    (tmp_path / "chapters").mkdir()
    (tmp_path / "chapters" / "ch03_submitting_data.md").write_text(
        "| Dataset | Description | Class | Structure |\n|---|---|---|---|\n| AE | x | Events | y |\n",
        encoding="utf-8")
    with pytest.raises(ValueError, match="权威表"):
        load_class_authority(tmp_path)


def test_markdown_render_round_trips():
    """塞进提示词的那张表必须仍然含每一行 —— 渲染端漏行 = 裁判看不到那个 dataset。"""
    m = load_class_authority()
    md = authority_table_markdown(m)
    assert md.count("\n") >= len(m), "渲染行数少于映射条目数"
    for ds in ("AE", "SUPP--", "TA"):
        assert f"| {ds} |" in md
