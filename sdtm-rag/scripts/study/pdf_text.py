"""PDF → 每页纯文本。**本模块是唯一碰子进程的地方** —— 切分逻辑全部在
split_sections.py 里对 list[str] 操作, 因而可以用合成文本完整测试, 不需要造 PDF。

用 poppler 的 pdftotext CLI (系统已装), 刻意不引入 Python PDF 依赖:
本轨只需要文本层, 而三份源 PDF 实测都有可用文本层 (不需要 OCR)。
"""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

_BIN = "pdftotext"
_INFO = "pdfinfo"


def require_pdftotext() -> None:
    """缺依赖立刻响亮失败。静默继续会产出一棵空章节树, 而空树不会让任何断言变红。"""
    if shutil.which(_BIN) is None:
        raise RuntimeError(
            f"{_BIN} not found — 本轨依赖 poppler CLI。macOS: brew install poppler"
        )


def count_pages(pdf: Path) -> int:
    require_pdftotext()
    r = subprocess.run([_INFO, str(pdf)], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"{_INFO} failed for {pdf.name}: {r.stderr.strip()}")
    m = re.search(r"^Pages:\s+(\d+)", r.stdout, re.MULTILINE)
    if not m:
        raise RuntimeError(f"{_INFO} gave no page count for {pdf.name}")
    return int(m.group(1))


def extract_pages(pdf: Path, n_pages: int | None = None) -> list[str]:
    """逐页抽取。返回 list, 索引 0 = 第 1 页。

    用 `-layout` 保留版面列关系 —— 日文文档里表格与缩进承载结构信息,
    不保留会把表格挤成一行, 后续切分与溯源都会失真。
    """
    require_pdftotext()
    total = n_pages if n_pages is not None else count_pages(pdf)
    out: list[str] = []
    for pg in range(1, total + 1):
        r = subprocess.run(
            [_BIN, "-layout", "-f", str(pg), "-l", str(pg), str(pdf), "-"],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            raise RuntimeError(f"{_BIN} failed on page {pg} of {pdf.name}: {r.stderr.strip()}")
        out.append(r.stdout)
    return out
