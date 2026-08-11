# Study C1: 文档型 PDF 章节化入库 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 st01 里唯一一份有真实章节结构的 PDF（113 页，日文为主）按编号标题确定性切成章节级 markdown chunk，与既有 959 张 field card 合并进同一个 `study_st01` collection，正文逐字保留。

**Architecture:** 三层分离 —— 薄 IO 层（`pdftotext` 子进程 → `list[str]` 每页文本）/ 纯逻辑层（页文本 → 章节树，可用合成数据完整测试）/ 渲染层（章节树 → 带 frontmatter 的 md）。切分正确性靠**两把从生成器之外反建的闸**：编号连续性校验（参照物是文档自身的编号序列）与**分割完备性断言**（拼回去必须逐字等于原文尾段）。ingest 侧改为「cards + docs 同批持久化」，因为 `persist_study` 是整 collection 重建。

**Tech Stack:** Python 3.14 / poppler `pdftotext`（系统 CLI，**不新增 Python 依赖**）/ chromadb / 既有 `scripts.ingest.embed_texts`

## Global Constraints

以下每条对**所有** Task 生效，实现时不得放宽：

1. **数据红线（spec §6）**：真实研究名、章节标题文字、正文内容**只允许**存在于 `sdtm-rag/data/study/`（已 gitignored）。进 git 的一切（代码、测试、plan、evidence、commit message）**零真名**。研究一律以代号 `st01` 指代。
2. **chunk 文件名必须是非识别性的**：形如 `st01__doc01__s2_1.md`（doc 序号 + 编号锚点 slug），**不得**由章节标题文字生成 slug —— 标题是真实内容。
3. **正文逐字保留**：本轨的「有损」只允许来自**切分位置**，不允许来自任何改写、摘要、翻译、清洗。禁止在管线里调用 LLM 改写正文。
4. **溯源必填**：每个 chunk 的 frontmatter 必须记 `page_start` / `page_end`，问题要能一步定位回源 PDF 页。
5. **幂等**：管线可重复跑，输出目录先清后写；重跑同一输入必须逐字节产出相同结果。
6. **fail-loud，不静默降级**：缺 `pdftotext`、编号不连续、分割不完备 —— 一律抛错并指出位置，不允许「跳过该节继续」。
7. **不碰 CDISC 主库**：只操作 `study_st01` collection（`persist_study` 既有语义）。
8. **测试零真实数据**：全部用合成日文/英文文本 fixture，不得把真实 PDF 或其抽出物写进 `scripts/tests/`。

## File Structure

| 文件 | 职责 |
|---|---|
| `scripts/study/paths.py`（改） | registry 增加 `doc_pdfs` 条目；`StudyPaths` 增加 `doc_pdfs: tuple[Path, ...]` 与 `docs_dir` |
| `scripts/study/pdf_text.py`（新） | **薄 IO 层**：`require_pdftotext()` / `extract_pages(pdf) -> list[str]`。唯一碰子进程的地方 |
| `scripts/study/split_sections.py`（新） | **纯逻辑**：`Section` dataclass / `find_anchors()` / `split_sections()` / `check_numbering()` / `assert_partition_complete()` |
| `scripts/study/render_doc_chunks.py`（新） | 章节树 → `data/study/<id>/docs/*.md`（frontmatter + 正文），含红线闸 |
| `scripts/study/ingest_study.py`（改） | `load_cards` 按 `doc_type` 分流必需键；新增 `load_doc_chunks`；main 合并两批一次 persist |
| `scripts/tests/test_pdf_text.py`（新） | IO 层：缺 `pdftotext` 时 fail-loud |
| `scripts/tests/test_split_sections.py`（新） | 切分逻辑主战场（合成文本） |
| `scripts/tests/test_render_doc_chunks.py`（新） | 文件名非识别性、frontmatter 完整性、幂等 |
| `scripts/tests/test_ingest_study_docs.py`（新） | 合流不抹卡、S2 不吃 doc chunk |
| `data/study/studies.local.yaml`（改，**本地不进 git**） | 注册 doc PDF 路径 |

---

### Task 1: registry 与路径解析支持 doc PDF

**Files:**
- Modify: `scripts/study/paths.py`
- Test: `scripts/tests/test_paths_doc_pdfs.py`（新建）

**Interfaces:**
- Produces: `StudyPaths.doc_pdfs: tuple[Path, ...]`（已存在性校验过的绝对路径，registry 中顺序保留）、`StudyPaths.docs_dir: Path`（= `out_dir / "docs"`）

- [x] **Step 1: 写失败测试**

```python
# scripts/tests/test_paths_doc_pdfs.py
import pytest
import yaml

from scripts.study.paths import resolve_study


def _write_registry(tmp_path, doc_names):
    src = tmp_path / "src"
    src.mkdir()
    (src / "cfg_new.xlsx").write_bytes(b"x")
    for n in doc_names:
        (src / n).write_bytes(b"%PDF-1.4\n")
    reg = {"st99": {"source_dir": str(src), "config_report_new": "cfg_new.xlsx",
                    "version_label_new": "vNEW", "doc_pdfs": list(doc_names)}}
    p = tmp_path / "studies.local.yaml"
    p.write_text(yaml.safe_dump(reg), encoding="utf-8")
    return p


def test_doc_pdfs_resolved_in_registry_order(tmp_path):
    reg = _write_registry(tmp_path, ["b.pdf", "a.pdf"])
    sp = resolve_study("st99", registry_path=reg)
    assert [p.name for p in sp.doc_pdfs] == ["b.pdf", "a.pdf"]
    assert all(p.is_absolute() for p in sp.doc_pdfs)


def test_docs_dir_sits_under_out_dir(tmp_path):
    reg = _write_registry(tmp_path, ["a.pdf"])
    sp = resolve_study("st99", registry_path=reg)
    assert sp.docs_dir == sp.out_dir / "docs"


def test_missing_doc_pdf_fails_loud(tmp_path):
    reg = _write_registry(tmp_path, ["a.pdf"])
    reg_data = yaml.safe_load(reg.read_text(encoding="utf-8"))
    reg_data["st99"]["doc_pdfs"] = ["a.pdf", "ghost.pdf"]
    reg.write_text(yaml.safe_dump(reg_data), encoding="utf-8")
    with pytest.raises(FileNotFoundError, match="ghost.pdf"):
        resolve_study("st99", registry_path=reg)


def test_doc_pdfs_defaults_to_empty_when_key_absent(tmp_path):
    """既有 st01 registry 没有 doc_pdfs 键 —— 不许因此炸掉 xlsx 轨。"""
    reg = _write_registry(tmp_path, [])
    reg_data = yaml.safe_load(reg.read_text(encoding="utf-8"))
    reg_data["st99"].pop("doc_pdfs")
    reg.write_text(yaml.safe_dump(reg_data), encoding="utf-8")
    assert resolve_study("st99", registry_path=reg).doc_pdfs == ()
```

- [x] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_paths_doc_pdfs.py -p no:warnings`
Expected: FAIL —— `AttributeError: 'StudyPaths' object has no attribute 'doc_pdfs'`

- [x] **Step 3: 实现**

在 `scripts/study/paths.py` 的 `StudyPaths` dataclass 末尾追加两个字段（放最后，避免破坏既有位置参数）：

```python
    doc_pdfs: tuple[Path, ...] = ()
    docs_dir: Path | None = None
```

在 `resolve_study()` 里，`out_dir` 计算之后、`return` 之前插入：

```python
    doc_pdfs: list[Path] = []
    for name in ent.get("doc_pdfs", []) or []:
        p = source_dir / name
        if not p.is_file():
            raise FileNotFoundError(f"{study_id}: doc pdf not found: {p}")
        doc_pdfs.append(p)
```

并把 `doc_pdfs=tuple(doc_pdfs), docs_dir=out_dir / "docs"` 加进 `StudyPaths(...)` 构造。

- [x] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_paths_doc_pdfs.py -p no:warnings`
Expected: 4 passed

- [x] **Step 5: 真实 registry 加条目（本地文件，不进 git）**

在 `data/study/studies.local.yaml` 的 `st01` 下加 `doc_pdfs:`，只列**那份 113 页的 PDF 文件名**（另两份表单版面的留给 C2）。加完自检：

```bash
.venv/bin/python -c "
from scripts.study.paths import resolve_study
sp = resolve_study('st01')
print('doc_pdfs 数量 =', len(sp.doc_pdfs), '| docs_dir =', sp.docs_dir)"
```
Expected: `doc_pdfs 数量 = 1`

- [x] **Step 6: 提交**

```bash
git add scripts/study/paths.py scripts/tests/test_paths_doc_pdfs.py
git commit -m "feat(study): paths 支持 doc PDF 注册 (C1 Task 1)"
```

---

### Task 2: PDF 文本抽取薄 IO 层

**Files:**
- Create: `scripts/study/pdf_text.py`
- Test: `scripts/tests/test_pdf_text.py`

**Interfaces:**
- Produces: `require_pdftotext() -> None`（缺失抛 `RuntimeError`）、`extract_pages(pdf: Path, n_pages: int | None = None) -> list[str]`（返回列表，索引 0 = 第 1 页）、`count_pages(pdf: Path) -> int`

- [x] **Step 1: 写失败测试**

```python
# scripts/tests/test_pdf_text.py
import pytest

from scripts.study import pdf_text


def test_require_pdftotext_raises_when_absent(monkeypatch):
    """缺依赖必须响亮失败 —— 静默产出空章节树比报错危险得多。"""
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
```

- [x] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_pdf_text.py -p no:warnings`
Expected: FAIL —— `ModuleNotFoundError: No module named 'scripts.study.pdf_text'`

- [x] **Step 3: 实现**

```python
# scripts/study/pdf_text.py
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
```

- [x] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_pdf_text.py -p no:warnings`
Expected: 4 passed

- [x] **Step 5: 对真实 PDF 冒烟（只报统计，不打印内容）**

```bash
.venv/bin/python -c "
from scripts.study.paths import resolve_study
from scripts.study.pdf_text import extract_pages, count_pages
sp = resolve_study('st01'); pdf = sp.doc_pdfs[0]
n = count_pages(pdf); pages = extract_pages(pdf, n)
print(f'页数={n} 抽出页数={len(pages)} 总字符={sum(len(p) for p in pages)} 空页数={sum(1 for p in pages if not p.strip())}')"
```
Expected: `页数=113 抽出页数=113`，空页数应为个位数

- [x] **Step 6: 提交**

```bash
git add scripts/study/pdf_text.py scripts/tests/test_pdf_text.py
git commit -m "feat(study): PDF 文本抽取薄 IO 层 (C1 Task 2)"
```

---

### Task 3: 章节切分 + 两把机器闸（**本计划的核心**）

**Files:**
- Create: `scripts/study/split_sections.py`
- Test: `scripts/tests/test_split_sections.py`

**Interfaces:**
- Produces:
  - `@dataclass(frozen=True) Section(number: str, level: int, heading_line: str, body: str, page_start: int, page_end: int)`
  - `find_anchors(pages: list[str]) -> list[tuple[int, int, str, str]]`  返回 `(page_1based, line_idx, number, full_line)`
  - `split_sections(pages: list[str]) -> list[Section]`
  - `check_numbering(sections: list[Section]) -> list[str]`  返回违规描述列表，空列表 = 通过
  - `assert_partition_complete(pages: list[str], sections: list[Section]) -> None`  不通过则 `AssertionError`

**设计依据（实测，勘察脚本见 Task 3 Step 5）**：那份 PDF 里
`n.m` 二层编号 **104 条且连续单调**（`2.1…2.7 | 3.1…3.10 | 4.1 4.2 | 5.1…`），
而顶层 `^\d+\s` **50 条里混入正文数字**（出现 `608`），非递减比例仅 38/49。
**故锚点只认二层及更深（`number` 含至少一个 `.`），顶层不作为切分点。**

- [x] **Step 1: 写失败测试**

```python
# scripts/tests/test_split_sections.py
"""切分逻辑全部用合成文本 —— 不碰真实 PDF, 不引入真名 (Global Constraint 8)。"""
import pytest

from scripts.study.split_sections import (
    assert_partition_complete,
    check_numbering,
    find_anchors,
    split_sections,
)

# 合成两页日文文档: 二层编号连续, 夹带一个会诱骗顶层匹配的正文数字
PAGES = [
    "治験実施計画書\n\n"
    "2.1 目的\n"
    "本試験の目的は安全性の評価である。\n"
    "対象は 608 例とする。\n"
    "2.2 対象\n"
    "選択基準を以下に示す。\n",
    "2.3 方法\n"
    "投与方法について記す。\n"
    "3.1 評価項目\n"
    "主要評価項目は奏効率とする。\n",
]


def test_anchors_only_pick_second_level_and_deeper():
    """顶层裸数字不作为锚点 —— 实测源文档里它会把正文数字 (608) 当成标题。"""
    nums = [a[2] for a in find_anchors(PAGES)]
    assert nums == ["2.1", "2.2", "2.3", "3.1"]
    assert "608" not in nums


def test_sections_carry_page_range():
    secs = split_sections(PAGES)
    assert [s.number for s in secs] == ["2.1", "2.2", "2.3", "3.1"]
    assert (secs[0].page_start, secs[0].page_end) == (1, 1)
    assert (secs[2].page_start, secs[2].page_end) == (2, 2)


def test_body_is_preserved_verbatim():
    """本轨唯一允许的有损是切分位置; 正文一个字都不许改 (Global Constraint 3)。"""
    body = split_sections(PAGES)[0].body
    assert "本試験の目的は安全性の評価である。" in body
    assert "対象は 608 例とする。" in body


def test_check_numbering_accepts_monotonic_sequence():
    assert check_numbering(split_sections(PAGES)) == []


def test_check_numbering_flags_backwards_child():
    bad = ["2.1 甲\n本文\n2.3 乙\n本文\n2.2 丙\n本文\n"]
    problems = check_numbering(split_sections(bad))
    assert problems and "2.2" in problems[0]


def test_check_numbering_flags_backwards_parent():
    bad = ["3.1 甲\n本文\n2.1 乙\n本文\n"]
    problems = check_numbering(split_sections(bad))
    assert problems and "2.1" in problems[0]


def test_partition_is_complete_and_non_overlapping():
    """把所有 section 拼回去必须逐字等于「首锚点及其之后」的全文。

    参照物是**原始页文本**, 不是切分器自己声称的任何数字 —— 护栏不许自洽
    (硬规矩 6)。切丢一段、切重一段、顺手 strip 掉一个空行, 这条都会红。
    """
    assert_partition_complete(PAGES, split_sections(PAGES))


def test_partition_assertion_actually_fires_when_a_section_is_dropped():
    """变异自检: 一道不会红的闸就是装饰 (硬规矩 18)。"""
    secs = split_sections(PAGES)
    with pytest.raises(AssertionError):
        assert_partition_complete(PAGES, secs[:-1])


def test_partition_assertion_fires_when_body_is_trimmed():
    secs = split_sections(PAGES)
    mutated = [secs[0].__class__(**{**secs[0].__dict__, "body": secs[0].body.strip()})] + secs[1:]
    with pytest.raises(AssertionError):
        assert_partition_complete(PAGES, mutated)


def test_no_anchors_yields_empty_and_does_not_crash():
    assert split_sections(["ただの本文。番号なし。\n"]) == []


def test_long_heading_line_is_not_an_anchor():
    """标题行短; 一行很长的正文即使以 n.m 开头也不是标题。"""
    long_line = "2.1 " + "あ" * 80
    assert find_anchors([long_line + "\n"]) == []
```

- [x] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_split_sections.py -p no:warnings`
Expected: FAIL —— `ModuleNotFoundError: No module named 'scripts.study.split_sections'`

- [x] **Step 3: 实现**

```python
# scripts/study/split_sections.py
"""页文本 → 章节树。纯逻辑, 无 IO —— 故可用合成文本完整测试。

**锚点为什么只认二层及更深** (实测依据, 那份 113 页文档):
  二层 `n.m` 104 条, 序列干净单调 (2.1…2.7 | 3.1…3.10 | 4.1 4.2 | 5.1…);
  顶层 `^\\d+\\s` 50 条里混入正文数字 (实测出现 608), 非递减比例仅 38/49。
  ⇒ 顶层不可靠, 不作切分点。顶层归属由二层编号的父号推出, 不另外识别。

**本模块提供两把闸, 参照物都在生成器之外**:
  1. check_numbering  —— 参照物是文档自身的编号序列;
  2. assert_partition_complete —— 参照物是原始页文本。
"""
from __future__ import annotations

import re
from dataclasses import dataclass

# 标题行: 行首最多 8 空格 + `n.m`(可更深) + 可选点 + 空白 + 非空白; 整行短。
_ANCHOR = re.compile(r"^[ \t]{0,8}(\d+(?:\.\d+){1,3})\.?[ \t]+(\S.*)$")
_MAX_HEADING_LEN = 60


@dataclass(frozen=True)
class Section:
    number: str
    level: int
    heading_line: str
    body: str
    page_start: int
    page_end: int


def find_anchors(pages: list[str]) -> list[tuple[int, int, str, str]]:
    """返回 (页码 1-based, 该页内行号 0-based, 编号, 整行原文)。"""
    out: list[tuple[int, int, str, str]] = []
    for pi, text in enumerate(pages, start=1):
        for li, line in enumerate(text.splitlines()):
            m = _ANCHOR.match(line)
            if m and len(line.strip()) <= _MAX_HEADING_LEN:
                out.append((pi, li, m.group(1), line))
    return out


def _flat(pages: list[str]) -> tuple[list[str], list[int]]:
    """展平成全局行列表, 并给出每行所属页码。切分在展平后的行序上做,
    这样跨页的一节能自然合并, 而页码范围仍可回算。"""
    lines: list[str] = []
    owner: list[int] = []
    for pi, text in enumerate(pages, start=1):
        for line in text.splitlines(keepends=True):
            lines.append(line)
            owner.append(pi)
    return lines, owner


def split_sections(pages: list[str]) -> list[Section]:
    lines, owner = _flat(pages)
    idx: list[tuple[int, str, str]] = []          # (全局行号, 编号, 整行)
    for gi, line in enumerate(lines):
        m = _ANCHOR.match(line.rstrip("\n"))
        if m and len(line.strip()) <= _MAX_HEADING_LEN:
            idx.append((gi, m.group(1), line.rstrip("\n")))
    sections: list[Section] = []
    for k, (gi, number, heading) in enumerate(idx):
        end = idx[k + 1][0] if k + 1 < len(idx) else len(lines)
        body = "".join(lines[gi:end])
        sections.append(Section(
            number=number,
            level=number.count(".") + 1,
            heading_line=heading,
            body=body,
            page_start=owner[gi],
            page_end=owner[end - 1] if end > gi else owner[gi],
        ))
    return sections


def check_numbering(sections: list[Section]) -> list[str]:
    """编号连续性闸。返回违规描述列表 (空 = 通过)。

    只查两条可机器判定的性质, 不猜语义:
      - 父号 (第一段) 非递减;
      - 同一父号内, 子号严格递增。
    违规不代表切分一定错 (源文档可能真的乱编号), 但**必须被人看到**,
    不许静默通过 —— 这是有损轨唯一的自动预警。
    """
    problems: list[str] = []
    last_parent = None
    last_child: dict[str, int] = {}
    for s in sections:
        head, *rest = s.number.split(".")
        parent, child = int(head), int(rest[0]) if rest else None
        if last_parent is not None and parent < last_parent:
            problems.append(f"父号回退: {s.number} (前一个父号 {last_parent}) p.{s.page_start}")
        last_parent = max(parent, last_parent) if last_parent is not None else parent
        if child is not None:
            prev = last_child.get(head)
            if prev is not None and child <= prev:
                problems.append(f"子号未递增: {s.number} (同父上一个 {head}.{prev}) p.{s.page_start}")
            last_child[head] = child
    return problems


def assert_partition_complete(pages: list[str], sections: list[Section]) -> None:
    """把所有 section 的 body 顺序拼接, 必须逐字等于「首锚点行起」的全文。

    参照物是**原始页文本**而非切分器自报的任何计数 —— 生成物的校验参照物
    必须来自生成器之外 (硬规矩 6)。丢一节 / 重一节 / 顺手 strip 一个空行, 全会红。
    """
    if not sections:
        return
    lines, _ = _flat(pages)
    joined = "".join(s.body for s in sections)
    first = "".join(lines).find(sections[0].heading_line)
    tail = "".join(lines)[first:]
    assert joined == tail, (
        f"分割不完备: 拼回 {len(joined)} 字符 vs 原文尾段 {len(tail)} 字符 "
        f"(差 {len(tail) - len(joined)})"
    )
```

- [x] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_split_sections.py -p no:warnings`
Expected: 11 passed

- [x] **Step 5: 对真实 PDF 跑两把闸（只报统计，不打印标题文字）**

```bash
.venv/bin/python -c "
from scripts.study.paths import resolve_study
from scripts.study.pdf_text import extract_pages
from scripts.study.split_sections import split_sections, check_numbering, assert_partition_complete
from collections import Counter
sp = resolve_study('st01')
pages = extract_pages(sp.doc_pdfs[0])
secs = split_sections(pages)
print('节数 =', len(secs), '| 层级分布 =', dict(sorted(Counter(s.level for s in secs).items())))
print('正文长度: 中位 %d / 最短 %d / 最长 %d' % (
    sorted(len(s.body) for s in secs)[len(secs)//2],
    min(len(s.body) for s in secs), max(len(s.body) for s in secs)))
p = check_numbering(secs)
print('编号闸违规 =', len(p)); [print('  ', x) for x in p[:10]]
assert_partition_complete(pages, secs); print('分割完备闸: PASS')"
```
Expected: 节数 ≈ 104；`分割完备闸: PASS`。
**编号闸若报违规，逐条读源 PDF 对应页确认是「源文档真的这么编号」还是「切分器切错了」，把结论写进 Task 6 的证据文件 —— 不许直接放宽正则让它变绿。**

- [x] **Step 6: 提交**

```bash
git add scripts/study/split_sections.py scripts/tests/test_split_sections.py
git commit -m "feat(study): 章节切分 + 编号连续性/分割完备性双闸 (C1 Task 3)"
```

---

### Task 4: 渲染 doc chunk（含红线闸）

**Files:**
- Create: `scripts/study/render_doc_chunks.py`
- Test: `scripts/tests/test_render_doc_chunks.py`

**Interfaces:**
- Consumes: `Section`（Task 3）、`StudyPaths.docs_dir` / `.doc_pdfs`（Task 1）
- Produces: `chunk_filename(doc_no: int, number: str) -> str`、`render_chunk(section, study_id, doc_no, version) -> str`、`build_doc_chunks(study_id, docs_dir, doc_no, sections, version) -> int`（返回写出文件数）

**frontmatter 契约**（Task 5 的 `load_doc_chunks` 依赖，键名不得改）：
`study` / `doc_type`（固定 `protocol_section`）/ `doc_no` / `section_number` / `page_start` / `page_end` / `version`

- [x] **Step 1: 写失败测试**

```python
# scripts/tests/test_render_doc_chunks.py
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


def test_frontmatter_has_every_key_ingest_depends_on():
    text = render_chunk(SEC, "st01", 1, "vNEW")
    for key in ("study:", "doc_type:", "doc_no:", "section_number:",
                "page_start:", "page_end:", "version:"):
        assert key in text, key
    assert "doc_type: protocol_section" in text


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
```

- [x] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_render_doc_chunks.py -p no:warnings`
Expected: FAIL —— `ModuleNotFoundError: No module named 'scripts.study.render_doc_chunks'`

- [x] **Step 3: 实现**

```python
# scripts/study/render_doc_chunks.py
"""Section → data/study/<id>/docs/*.md (frontmatter + 逐字正文)。

文件名**只**由 doc 序号与编号锚点生成 —— 章节标题是真实研究内容,
拿它做 slug 会让真名从文件名泄进 git status / 日志 / 报错信息 (Global Constraint 2)。
"""
from __future__ import annotations

import shutil
from pathlib import Path

from scripts.study.split_sections import Section

DOC_TYPE = "protocol_section"


def chunk_filename(doc_no: int, number: str) -> str:
    return f"st01__doc{doc_no:02d}__s{number.replace('.', '_')}.md"


def render_chunk(section: Section, study_id: str, doc_no: int, version: str) -> str:
    return (
        "---\n"
        f"study: {study_id}\n"
        f"doc_type: {DOC_TYPE}\n"
        f"doc_no: {doc_no}\n"
        f"section_number: {section.number}\n"
        f"page_start: {section.page_start}\n"
        f"page_end: {section.page_end}\n"
        f"version: {version}\n"
        "---\n\n"
        f"{section.body}"
    )


def build_doc_chunks(study_id: str, docs_dir: Path, doc_no: int,
                     sections: list[Section], version: str) -> int:
    """先清后写 —— 幂等 (Global Constraint 5), 且不留上一次跑的孤儿 chunk。"""
    if docs_dir.exists():
        shutil.rmtree(docs_dir)
    docs_dir.mkdir(parents=True)
    for s in sections:
        (docs_dir / chunk_filename(doc_no, s.number)).write_text(
            render_chunk(s, study_id, doc_no, version), encoding="utf-8")
    return len(sections)
```

- [x] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_render_doc_chunks.py -p no:warnings`
Expected: 6 passed

- [x] **Step 5: 提交**

```bash
git add scripts/study/render_doc_chunks.py scripts/tests/test_render_doc_chunks.py
git commit -m "feat(study): doc chunk 渲染 + 非识别性文件名闸 (C1 Task 4)"
```

---

### Task 5: ingest 合流（**最容易炸的一步**）

**Files:**
- Modify: `scripts/study/ingest_study.py`
- Test: `scripts/tests/test_ingest_study_docs.py`

**为什么必须合流**：`persist_study()` 第 62-64 行是 `delete_collection` + `create_collection` ——
**整个 collection 重建**。若把 doc chunk 单独跑一次 ingest，会当场抹掉已入库的 959 张 field card。
故 `main()` 必须一次性加载 cards + docs 再 persist。

**doc chunk 与 S2 的关系（已核实，比预想的更安全）**：`server/study_lookup.py:51` 的签名是
`StudyLookup(catalog: dict, aliases=None)` —— **S2 的输入是 `catalog.json`，它根本不读
cards/docs 目录**。而 `catalog.json` 完全由 xlsx 管线生成，本计划一个字都不动它。
⇒ **doc chunk 在结构上就进不了 S2 的确定性直查队列**，不是靠实现者小心避开的。
本任务**不改 S2**，只加一条钉住这个**结构性理由**的回归测试（见 Step 5）——
理由变了（比如哪天 S2 改成扫目录），测试要红。

**Interfaces:**
- Consumes: `chunk_filename` / frontmatter 契约（Task 4）
- Produces: `load_doc_chunks(docs_dir: Path) -> list[dict]`（与 `load_cards` 同形状：`{"id", "text", "metadata"}`）

- [x] **Step 1: 写失败测试**

```python
# scripts/tests/test_ingest_study_docs.py
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
```

- [x] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_ingest_study_docs.py -p no:warnings`
Expected: FAIL —— `ImportError: cannot import name 'load_doc_chunks'`

- [x] **Step 3: 实现**

在 `scripts/study/ingest_study.py` 顶部常量区加：

```python
_DOC_REQUIRED = ("study", "doc_type", "doc_no", "section_number", "page_start", "page_end")
```

在 `load_cards` 之后新增：

```python
def load_doc_chunks(docs_dir: Path) -> list[dict]:
    """文档型 chunk (protocol 章节)。与 field card 同形状, 但**没有 field_oid** ——
    S2 的确定性直查因此不会把它当卡片吃进去 (那条通道按 label/OID 建索引)。

    docs_dir 不存在时返回空列表: C1 之前没有 docs/, xlsx 轨必须照跑不误。
    """
    if not docs_dir.is_dir():
        return []
    out: list[dict] = []
    for p in sorted(docs_dir.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        fm = _parse_frontmatter(text)
        missing = [k for k in _DOC_REQUIRED if not fm.get(k)]
        if missing:
            raise ValueError(f"{p.name}: doc chunk frontmatter 缺必需键 {missing}")
        doc_ns = f"doc{int(fm['doc_no']):02d}"
        out.append({
            "id": p.stem,
            "text": text,
            "metadata": {
                "study": fm["study"],
                "version": fm.get("version", ""),
                "file_type": fm["doc_type"],
                # domain 不留空: 空串会静默逃出 RAGEngine._build_where 的过滤
                "domain": doc_ns,
                "section": fm["section_number"],
                "source": p.name,
                "provenance": f"{doc_ns}#p{fm['page_start']}-{fm['page_end']}",
            },
        })
    return out
```

改 `main()`：在 `resolve_study` 之后，把两批合并再 persist（**一次 persist，因为它整体重建 collection**）：

```python
    cards = load_cards(sp.cards_dir)
    docs = load_doc_chunks(sp.docs_dir)
    records = cards + docs
    print(f"field cards {len(cards)} + doc chunks {len(docs)} = {len(records)}")
```

其后原先所有用 `cards` 的地方（embed、persist）一律改用 `records`。

- [x] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_ingest_study_docs.py scripts/tests/test_ingest_study.py -p no:warnings`
Expected: 全部 passed（新 7 条 + 既有 ingest 测试零回归）

- [x] **Step 5: 钉住 S2 隔离的**结构性理由**（不是钉现象）**

隔离之所以成立，是因为 **S2 的输入是 `catalog.json`，不是目录扫描**。测试要钉的是这个理由 ——
哪天有人把 S2 改成扫 cards 目录，这条必须红。在 `scripts/tests/test_ingest_study_docs.py` 末尾追加：

```python
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
```

Run: `.venv/bin/python -m pytest scripts/tests/test_ingest_study_docs.py -p no:warnings`
Expected: 9 passed

- [x] **Step 6: 提交**

```bash
git add scripts/study/ingest_study.py scripts/tests/test_ingest_study_docs.py
git commit -m "feat(study): ingest 合流 cards + doc chunks, S2 隔离钉死 (C1 Task 5)"
```

---

### Task 6: 端到端全量跑 + 红线复扫 + 收口

**Files:**
- Create: `scripts/study/build_docs.py`（CLI 串起 Task 2-4）
- Create: `sdtm-rag/evidence/checkpoints/study_c1_doc_sections.md`
- Test: `scripts/tests/test_build_docs_cli.py`

- [x] **Step 1: 写 CLI 的失败测试**

```python
# scripts/tests/test_build_docs_cli.py
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
```

- [x] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_build_docs_cli.py -p no:warnings`
Expected: FAIL —— `ModuleNotFoundError: No module named 'scripts.study.build_docs'`

- [x] **Step 3: 实现 CLI**

```python
# scripts/study/build_docs.py
"""doc PDF → 章节 chunk 的 CLI。两把闸的结果一律打印, 不许静默。"""
from __future__ import annotations

import argparse
from pathlib import Path

from scripts.study.paths import resolve_study
from scripts.study.pdf_text import extract_pages
from scripts.study.render_doc_chunks import build_doc_chunks
from scripts.study.split_sections import (
    assert_partition_complete,
    check_numbering,
    split_sections,
)


def build_one(docs_dir: Path, doc_no: int, pdf: Path, study_id: str, version: str) -> int:
    pages = extract_pages(pdf)
    sections = split_sections(pages)
    if not sections:
        raise ValueError(f"doc{doc_no:02d}: 切出 0 节 —— 该 PDF 没有可识别的编号标题, "
                         "不要静默入库空结果")
    problems = check_numbering(sections)
    print(f"编号闸: {'PASS' if not problems else f'{len(problems)} 条违规'}")
    for p in problems:
        print(f"  ⚠ {p}")
    assert_partition_complete(pages, sections)
    print(f"分割完备闸: PASS ({len(sections)} 节, {len(pages)} 页)")
    return build_doc_chunks(study_id, docs_dir, doc_no, sections, version)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="study doc PDF → 章节 chunk")
    ap.add_argument("--study", required=True)
    args = ap.parse_args(argv)
    sp = resolve_study(args.study)
    total = 0
    for i, pdf in enumerate(sp.doc_pdfs, start=1):
        total += build_one(sp.docs_dir, i, pdf, args.study, sp.version_label_new)
    print(f"写出 chunk {total} 个 → {sp.docs_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [x] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_build_docs_cli.py -p no:warnings`
Expected: 2 passed

- [x] **Step 5: 全量跑 + 重灌 + 验证卡片没被抹掉**

```bash
.venv/bin/python -m scripts.study.build_docs --study st01
.venv/bin/python -m scripts.study.ingest_study --study st01
.venv/bin/python -c "
import chromadb
from collections import Counter
c = chromadb.PersistentClient(path='data/chroma').get_collection('study_st01')
got = c.get(include=['metadatas'])
print('总数 =', len(got['ids']))
print('按 file_type =', dict(Counter(m['file_type'] for m in got['metadatas'])))"
```
Expected: `field_card` 仍为 **959**（一张都不能少），`protocol_section` ≈ 104

- [x] **Step 6: 红线程序化复扫（不许人工豁免）**

```bash
.venv/bin/python -c "
import json, pathlib, subprocess
cat = json.load(open('data/study/st01/catalog.json'))
ID_FIELDS = ('oid','name','label','description','summary_format','question','alias')
vals = set()
def walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ID_FIELDS and isinstance(v, str) and v.strip(): vals.add(v.strip())
            walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
walk(cat); vals.add(cat['study'])
cand = {v for v in vals if len(v) >= 4}
tracked = subprocess.run(['git','ls-files'], capture_output=True, text=True).stdout.split()
hits = []
for f in tracked:
    p = pathlib.Path(f)
    if p.suffix not in ('.py','.md','.yml','.yaml','.json') or not p.exists(): continue
    t = p.read_text(encoding='utf-8', errors='ignore')
    hits += [(f, v) for v in cand if v in t]
print('命中:', [h for h in hits if h[1] != 'st01'] or '无 —— 已追踪文件零真名')"
git status --porcelain data/study | head    # 必须为空: study 产物一个都不许被追踪
```
Expected: `无 —— 已追踪文件零真名`；`git status` 对 `data/study` 输出为空

- [x] **Step 7: 规则 A 独立抽检（有损轨强制，spec §4）**

派**与实现方不同 `subagent_type`** 的抽检 agent，N=8 随机抽 8 个 chunk，逐条核对：
① 该节正文与源 PDF 对应页**逐字一致**（这是本轨唯一的有损点，必须人眼看过）；
② `page_start`/`page_end` 指向的页确实包含该节；
③ 文件名不含任何标题文字。
**要求抽检方边做边把结论落盘到文件**（本项目已吃过「agent 做完不回报」的亏），
结果写进 `evidence/step_c1_audit.md`。

- [x] **Step 8: 写收口证据**

`sdtm-rag/evidence/checkpoints/study_c1_doc_sections.md` 必须包含（**纯统计，无真名无正文**）：
页数 / 节数 / 层级分布 / 正文长度分位 / 编号闸违规条数**及逐条裁定**（源文档如此 vs 切分器错）/
分割完备闸结果 / collection 内 `field_card` 与 `protocol_section` 计数 / pytest 计数 /
红线复扫结果 / 规则 A 抽检结论 / **已知限制**（至少写清：顶层编号不作锚点因而顶层标题
不单独成节；表格跨页时 `-layout` 的列对齐可能在节边界处失真；C2 的两份表单版面 PDF 未处理）。

- [x] **Step 9: 全量测试 + 提交**

```bash
.venv/bin/python -m pytest -p no:warnings 2>&1 | tail -3
git add scripts/study/build_docs.py scripts/tests/test_build_docs_cli.py \
        sdtm-rag/evidence/checkpoints/study_c1_doc_sections.md
git commit -m "feat(study): C1 文档章节化端到端 + 收口证据"
```
Expected: 980 + 本计划新增测试数，0 failed

---

## Self-Review

**1. Spec coverage**（对 `docs/superpowers/specs/2026-07-31-study-rag-design.md`）
- §2「Protocol / workflow PDF → 章节级 markdown」→ Task 2-4、6 ✔
- §2「aCRF PDF → 页级粗切」→ **明确移交 C2**（本计划 Global Constraints 与 Task 6 Step 8 已写明）
- §3.2 chunk 形态表「heading path, 页码范围」→ `section_number` + `page_start/page_end`（Task 4 frontmatter）✔
- §4 有损轨「规则 A 抽检」→ Task 6 Step 7 ✔
- §4.1「问题一步定位到源」→ `provenance = doc01#p7-8`（Task 5）✔
- §4.1「幂等」→ Task 4 先清后写 + 幂等测试 ✔
- §6 红线 → Global Constraints 1-2 + Task 4 文件名闸 + Task 6 Step 6 程序化复扫 ✔
- §7.3「有损轨抽检 PASS 留痕」→ Task 6 Step 7-8 ✔
- §5「联邦检索」→ 不在本计划（doc chunk 进的是既有 `study_st01` collection，联邦路由无需改动）

**2. Placeholder scan**：无 TBD/TODO；每个代码步骤都给了可直接粘贴的实现；测试全部是真实断言而非「为上述写测试」。Task 6 Step 7 的抽检是人/agent 动作，已给出明确的三条核对项与产物路径。

**3. Type consistency**：`Section` 字段（`number/level/heading_line/body/page_start/page_end`）在 Task 3 定义，Task 4 的 `render_chunk`、Task 6 的 `build_one` 用的是同一组名字；`chunk_filename(doc_no, number)` 在 Task 4 定义、Task 6 测试引用一致；frontmatter 键名在 Task 4 产出、Task 5 `_DOC_REQUIRED` 消费，逐字对齐（`doc_type`/`doc_no`/`section_number`/`page_start`/`page_end`）。

**一处已知张力（留给执行者判断，不预先放宽）**：Task 3 Step 5 若编号闸报出违规，
**不许通过放宽正则让它变绿**。正确处置是逐条回源 PDF 裁定，并把裁定写进收口证据 ——
源文档真的乱编号是事实，切分器切错是缺陷，两者必须分开记。
