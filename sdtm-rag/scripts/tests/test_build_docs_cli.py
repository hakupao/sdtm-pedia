"""C1 Task 6: CLI. 抽取层 monkeypatch, 不碰真实 PDF."""
from scripts.study import build_docs
from scripts.study.split_sections import Section

SEC = Section("2.1", 2, "2.1 目的", "2.1 目的\n本文。\n", 1, 1)


def test_cli_reports_gate_results_and_writes_chunks(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(build_docs, "extract_pages", lambda _p: ["2.1 目的\n本文。\n"])
    n = build_docs.build_one(tmp_path / "docs", doc_no=1, pdf=tmp_path / "x.pdf",
                             study_id="st01", version="vNEW")
    out = capsys.readouterr().out
    assert n == 1
    assert "编号闸" in out and "分割完备闸" in out
    assert (tmp_path / "docs" / "st01__doc01__s2_1.md").exists()


def test_cli_raises_when_partition_incomplete(tmp_path, monkeypatch):
    monkeypatch.setattr(build_docs, "extract_pages", lambda _p: ["2.1 目的\n本文。\n"])
    monkeypatch.setattr(build_docs, "split_sections", lambda _pages: [])
    # 空章节树不该被当成「成功但 0 节」静默通过
    try:
        build_docs.build_one(tmp_path / "docs", 1, tmp_path / "x.pdf", "st01", "vNEW")
    except ValueError as e:
        assert "0 节" in str(e)
    else:
        raise AssertionError("空章节树必须响亮失败")


def test_cli_subdivides_oversized_sections_and_reports_it(tmp_path, monkeypatch, capsys):
    """超限节必须在写盘前切开, 且切了要说 —— 静默切分和静默截断一样不可接受。"""
    # 行数按真实上限取: 8191 token 预算下需要 ~3000 行日文才会溢出
    long_page = "2.1 目的\n" + "".join(f"行{i}あいうえおかきくけこ\n" for i in range(3000))
    monkeypatch.setattr(build_docs, "extract_pages", lambda _p: [long_page])
    n = build_docs.build_one(tmp_path / "docs", 1, tmp_path / "x.pdf", "st01", "vNEW")
    out = capsys.readouterr().out
    written = sorted(p.name for p in (tmp_path / "docs").iterdir())
    assert n == len(written) > 1
    assert "二次切分" in out
    assert all(name.startswith("st01__doc01__s2_1__part") for name in written)


def test_cli_output_chunks_stay_under_embedding_limit(tmp_path, monkeypatch):
    """闸的参照物是 ingest 侧真实使用的分词器与上限, 不是 CLI 自报的数字。"""
    from scripts.ingest import EMBED_MAX_TOKENS, count_tokens
    long_page = "2.1 目的\n" + "".join(f"行{i}あいうえおかきくけこ\n" for i in range(3000))
    monkeypatch.setattr(build_docs, "extract_pages", lambda _p: [long_page])
    build_docs.build_one(tmp_path / "docs", 1, tmp_path / "x.pdf", "st01", "vNEW")
    for f in (tmp_path / "docs").iterdir():
        assert count_tokens(f.read_text(encoding="utf-8")) <= EMBED_MAX_TOKENS, f.name


def test_cli_covers_front_matter_and_reports_the_full_coverage_gate(tmp_path, monkeypatch, capsys):
    """L1 修复: 首锚点之前的内容必须成 chunk, 且 CLI 要打印全文覆盖闸的结果。

    真实文档里这块是 16,880 字符 (卷首 p1-10 + 首锚点页前段), 长期不在任何 chunk
    里而三把闸全绿 —— 因为旧闸的口径是「首锚点行起」, 对它天然免疫。
    """
    front = "治験実施計画書\n実施医療機関一覧\n"
    body = "2.1 目的\n本文。\n"
    monkeypatch.setattr(build_docs, "extract_pages", lambda _p: [front, body])

    n = build_docs.build_one(tmp_path / "docs", 1, tmp_path / "x.pdf", "st01", "vNEW")
    out = capsys.readouterr().out
    names = sorted(p.name for p in (tmp_path / "docs").iterdir())

    assert "全文覆盖闸" in out
    assert names == ["st01__doc01__s2_1.md", "st01__doc01__sfront01.md"]
    assert n == 2
    # 卷首正文逐字, 不 strip
    assert (tmp_path / "docs" / "st01__doc01__sfront01.md").read_text(
        encoding="utf-8").endswith(front)


def test_cli_full_coverage_gate_is_not_decorative(tmp_path, monkeypatch):
    """闸必须真的会红: 把卷首切分函数打成哑巴 (返回空), 全文覆盖闸应当拦下。"""
    front = "治験実施計画書\n実施医療機関一覧\n"
    monkeypatch.setattr(build_docs, "extract_pages", lambda _p: [front, "2.1 目的\n本文。\n"])
    monkeypatch.setattr(build_docs, "split_front_matter", lambda _p, excluded_pages: [])
    try:
        build_docs.build_one(tmp_path / "docs", 1, tmp_path / "x.pdf", "st01", "vNEW")
    except AssertionError as e:
        assert "未覆盖" in str(e)
    else:
        raise AssertionError("卷首没被覆盖时全文覆盖闸必须红")
