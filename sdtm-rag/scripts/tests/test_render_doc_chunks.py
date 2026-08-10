"""C1 Task 4: 渲染层. 文件名非识别性 / frontmatter 完整性 / 幂等."""
from scripts.study.render_doc_chunks import build_doc_chunks, chunk_filename, render_chunk
from scripts.study.split_sections import Section

SEC = Section(number="2.1", level=2, heading_line="2.1 目的",
              body="2.1 目的\n本試験の目的。\n", page_start=7, page_end=8)


def test_filename_is_non_identifying():
    """文件名只由 doc 序号 + 编号锚点生成 —— 标题文字是真实内容, 不许进文件名
    (Global Constraint 2)。这条闸挡的是「顺手用标题做 slug」这种最自然的写法。"""
    name = chunk_filename(1, "2.1")
    assert name == "st01__doc01__s2_1.md"
    assert "目的" not in name


def test_filename_handles_deep_numbering():
    assert chunk_filename(2, "3.10.2") == "st01__doc02__s3_10_2.md"


def test_filename_carries_part_only_when_section_was_subdivided():
    """未切分的节文件名不变 (与计划契约一致); 切开的节必须各自成文件, 否则
    后写的份会覆盖前一份 —— 那是静默丢正文。"""
    assert chunk_filename(1, "8.2") == "st01__doc01__s8_2.md"
    assert chunk_filename(1, "8.2", part=2, parts_total=3) == "st01__doc01__s8_2__part02.md"
    assert chunk_filename(1, "8.2", part=1, parts_total=3) == "st01__doc01__s8_2__part01.md"


def test_frontmatter_has_every_key_ingest_depends_on():
    text = render_chunk(SEC, "st01", 1, "vNEW")
    for key in ("study:", "doc_type:", "doc_no:", "section_number:",
                "page_start:", "page_end:", "version:"):
        assert key in text, key
    assert "doc_type: protocol_section" in text


def test_frontmatter_records_part_position():
    text = render_chunk(Section("8.2", 2, "8.2 甲", "本文\n", 63, 70, part=2, parts_total=3),
                        "st01", 1, "vNEW")
    assert "part: 2" in text and "parts_total: 3" in text


def test_body_is_verbatim_in_output():
    assert "本試験の目的。" in render_chunk(SEC, "st01", 1, "vNEW")


def test_page_range_is_recorded_for_provenance():
    text = render_chunk(SEC, "st01", 1, "vNEW")
    assert "page_start: 7" in text and "page_end: 8" in text


def test_build_is_idempotent_and_clears_stale_files(tmp_path):
    docs = tmp_path / "docs"
    stale = docs / "st01__doc01__s9_9.md"
    docs.mkdir()
    stale.write_text("old", encoding="utf-8")
    n1 = build_doc_chunks("st01", docs, 1, [SEC], "vNEW")
    first = (docs / "st01__doc01__s2_1.md").read_text(encoding="utf-8")
    n2 = build_doc_chunks("st01", docs, 1, [SEC], "vNEW")
    assert n1 == n2 == 1
    assert (docs / "st01__doc01__s2_1.md").read_text(encoding="utf-8") == first
    assert not stale.exists()


def test_build_writes_one_file_per_part(tmp_path):
    """变异自检: 若文件名忽略 part, 这条会掉到 1 个文件 —— 静默丢两份正文。"""
    parts = [Section("8.2", 2, "8.2 甲", f"本文{i}\n", 63, 70, part=i, parts_total=3)
             for i in (1, 2, 3)]
    n = build_doc_chunks("st01", tmp_path / "docs", 1, parts, "vNEW")
    written = sorted(p.name for p in (tmp_path / "docs").iterdir())
    assert n == 3 and len(written) == 3
    assert written == ["st01__doc01__s8_2__part01.md", "st01__doc01__s8_2__part02.md",
                       "st01__doc01__s8_2__part03.md"]
    bodies = "".join((tmp_path / "docs" / w).read_text(encoding="utf-8") for w in written)
    assert "本文1" in bodies and "本文2" in bodies and "本文3" in bodies
