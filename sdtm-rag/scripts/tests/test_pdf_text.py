"""C1 Task 2: PDF 文本抽取薄 IO 层. 子进程全部 monkeypatch, 不碰真实 PDF."""
import pytest

from scripts.study import pdf_text


def test_require_pdftotext_raises_when_absent(monkeypatch):
    """缺依赖必须响亮失败 —— 静默产出空章节树比报错危险得多."""
    monkeypatch.setattr(pdf_text.shutil, "which", lambda _name: None)
    with pytest.raises(RuntimeError, match="pdftotext"):
        pdf_text.require_pdftotext()


def test_require_pdftotext_passes_when_present(monkeypatch):
    monkeypatch.setattr(pdf_text.shutil, "which", lambda _name: "/usr/bin/pdftotext")
    pdf_text.require_pdftotext()


def test_extract_pages_returns_one_entry_per_page(monkeypatch, tmp_path):
    calls = []

    class _R:
        returncode = 0

        def __init__(self, page):
            self.stdout = f"page{page}"

    def fake_run(cmd, **_kw):
        page = int(cmd[cmd.index("-f") + 1])
        calls.append(page)
        return _R(page)

    monkeypatch.setattr(pdf_text.shutil, "which", lambda _n: "/usr/bin/pdftotext")
    monkeypatch.setattr(pdf_text.subprocess, "run", fake_run)
    pdf = tmp_path / "x.pdf"
    pdf.write_bytes(b"%PDF")
    assert pdf_text.extract_pages(pdf, n_pages=3) == ["page1", "page2", "page3"]
    assert calls == [1, 2, 3]


def test_extract_pages_raises_on_pdftotext_failure(monkeypatch, tmp_path):
    class _R:
        returncode = 1
        stdout = ""
        stderr = "boom"

    monkeypatch.setattr(pdf_text.shutil, "which", lambda _n: "/usr/bin/pdftotext")
    monkeypatch.setattr(pdf_text.subprocess, "run", lambda *_a, **_k: _R())
    pdf = tmp_path / "x.pdf"
    pdf.write_bytes(b"%PDF")
    with pytest.raises(RuntimeError, match="boom"):
        pdf_text.extract_pages(pdf, n_pages=1)
