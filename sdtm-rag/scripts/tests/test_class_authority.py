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
    """反方向: 表被改坏时必须**当场炸**, ⛔ 不许返回一个短表让下游静默恒真。
    ⚠ match 收紧到 "抽取端失效" (而非泛泛的 "权威表") —— 两条 fail-loud 分支
    (本测试的行数/Class 数不足分支, 与下面 test_loader_fails_loud_when_header_missing
    的表头找不到分支) 的消息都含 "权威表", 松匹配分辨不出到底是哪条分支炸的。"""
    (tmp_path / "chapters").mkdir()
    (tmp_path / "chapters" / "ch03_submitting_data.md").write_text(
        "| Dataset | Description | Class | Structure |\n|---|---|---|---|\n| AE | x | Events | y |\n",
        encoding="utf-8")
    with pytest.raises(ValueError, match="抽取端失效"):
        load_class_authority(tmp_path)


def test_loader_fails_loud_when_header_missing(tmp_path: Path):
    """与上面那条互相独立的另一条炸点: 表头行本身就找不到 (ch03 结构变了/表头文字改了),
    必须报"表头没找到", ⛔ 不能被误判成"行数不足"分支 —— 这条测试原来完全没人钉,
    松匹配 "权威表" 时两条分支都能让任何一条测试通过, 分辨不出到底炸的是哪条。"""
    (tmp_path / "chapters").mkdir()
    (tmp_path / "chapters" / "ch03_submitting_data.md").write_text(
        "# 这份文件没有权威表表头\n\n随便写点别的内容, 不含 Dataset/Description/Class 表头行。\n",
        encoding="utf-8")
    with pytest.raises(ValueError, match="表头没找到"):
        load_class_authority(tmp_path)


def test_loader_fails_loud_on_row_count_alone(tmp_path: Path):
    """F-1: 隔离 _MIN_ROWS —— 构造一张行数 < 60 但 Class 种类已经 ≥6 (_MIN_CLASSES 过关)
    的表, 让 "行数不足" 单独触发, 不靠 "Class 种类不够" 顺带兜底。⚠ 原先 4 条测试里
    唯一覆盖此分支的 test_loader_fails_loud_on_a_broken_table 用的是 1 行/1 Class,
    两道阈值同时不达标, 分不清到底是 _MIN_ROWS 还是 _MIN_CLASSES 在起作用;
    _MIN_ROWS 若被删掉/失效, 本测试是唯一会变红的哨兵。"""
    (tmp_path / "chapters").mkdir()
    (tmp_path / "chapters" / "ch03_submitting_data.md").write_text(
        "| Dataset | Description | Class | Structure |\n"
        "|---|---|---|---|\n"
        "| AE | x | Events | y |\n"
        "| LB | x | Findings | y |\n"
        "| FA | x | Findings About | y |\n"
        "| CM | x | Interventions | y |\n"
        "| RELREC | x | Relationship | y |\n"
        "| CO | x | Special Purpose | y |\n"
        "| TA | x | Trial Design | y |\n",
        encoding="utf-8")
    with pytest.raises(ValueError, match="抽取端失效"):
        load_class_authority(tmp_path)


def test_markdown_render_round_trips():
    """塞进提示词的那张表必须仍然含每一行 —— 渲染端漏行 = 裁判看不到那个 dataset。"""
    m = load_class_authority()
    md = authority_table_markdown(m)
    assert md.count("\n") >= len(m), "渲染行数少于映射条目数"
    for ds in ("AE", "SUPP--", "TA"):
        assert f"| {ds} |" in md
