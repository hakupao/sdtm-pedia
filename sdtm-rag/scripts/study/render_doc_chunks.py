"""Section → data/study/<id>/docs/*.md (frontmatter + 逐字正文)。

文件名**只**由 doc 序号与编号锚点生成 —— 章节标题是真实研究内容,
拿它做 slug 会让真名从文件名泄进 git status / 日志 / 报错信息 (Global Constraint 2)。
"""
from __future__ import annotations

import shutil
from pathlib import Path

from scripts.study.split_sections import Section

DOC_TYPE = "protocol_section"


def chunk_filename(doc_no: int, number: str, part: int = 1, parts_total: int = 1) -> str:
    """未切分的节保持 `st01__docNN__sX_Y.md`; 被二次切分的节按份加 `__partKK`。

    份号必须进文件名: 同一节的多份共用编号, 不加区分会互相覆盖 (静默丢正文)。
    """
    stem = f"st01__doc{doc_no:02d}__s{number.replace('.', '_')}"
    if parts_total > 1:
        stem = f"{stem}__part{part:02d}"
    return f"{stem}.md"


def render_chunk(section: Section, study_id: str, doc_no: int, version: str) -> str:
    return (
        "---\n"
        f"study: {study_id}\n"
        f"doc_type: {DOC_TYPE}\n"
        f"doc_no: {doc_no}\n"
        f"section_number: {section.number}\n"
        f"part: {section.part}\n"
        f"parts_total: {section.parts_total}\n"
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
        name = chunk_filename(doc_no, s.number, s.part, s.parts_total)
        (docs_dir / name).write_text(
            render_chunk(s, study_id, doc_no, version), encoding="utf-8")
    return len(sections)
