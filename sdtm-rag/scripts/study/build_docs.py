"""doc PDF → 章节 chunk 的 CLI。三把闸的结果一律打印, 不许静默。

闸 1 编号连续性 (参照物: 文档自身编号序列)
闸 2 分割完备性 (参照物: 原始页文本, 拼回去必须逐字相等)
闸 3 embedding 上限 (参照物: ingest 侧真实使用的分词器与硬上限, 见下)

闸 3 为什么必要: 入库的是**整个 md 文件** (frontmatter + 正文), 而
`scripts.ingest.embed_texts` 对超 8191 token 的文本是截断后继续 —— 文本入库但
向量只覆盖前半截, 计数与前两把闸全绿, 看不出来。故切分预算要扣掉 frontmatter,
写盘后再按文件实测一遍。
"""
from __future__ import annotations

import argparse
from pathlib import Path

from scripts.ingest import EMBED_MAX_TOKENS, count_tokens
from scripts.study.paths import resolve_study
from scripts.study.pdf_text import extract_pages
from scripts.study.render_doc_chunks import build_doc_chunks, render_chunk
from scripts.study.split_sections import (
    Section,
    assert_partition_complete,
    check_numbering,
    split_sections,
    subdivide_oversized,
)

# frontmatter 之外再留的安全余量: 分词在拼接边界上可能与分段计数差几个 token
_TOKEN_MARGIN = 32


def _body_budget(sections: list[Section], study_id: str, doc_no: int, version: str) -> int:
    """正文可用 token 预算 = 硬上限 - 最坏情况 frontmatter 开销 - 余量。"""
    overhead = max(
        count_tokens(render_chunk(
            Section(s.number, s.level, s.heading_line, "", s.page_start, s.page_end,
                    s.part, s.parts_total), study_id, doc_no, version))
        for s in sections
    )
    return EMBED_MAX_TOKENS - overhead - _TOKEN_MARGIN


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

    budget = _body_budget(sections, study_id, doc_no, version)
    chunks = subdivide_oversized(pages, sections, budget, count_tokens)
    split_map = {c.number: c.parts_total for c in chunks if c.parts_total > 1}
    print(f"二次切分 (预算 {budget} token/份): {len(sections)} 节 → {len(chunks)} 份"
          f"{'; 被切: ' + str(split_map) if split_map else '; 无节超限'}")
    assert_partition_complete(pages, chunks)
    print("分割完备闸 (切完后复查): PASS")

    written = build_doc_chunks(study_id, docs_dir, doc_no, chunks, version)
    over = [f.name for f in sorted(docs_dir.glob("*.md"))
            if count_tokens(f.read_text(encoding="utf-8")) > EMBED_MAX_TOKENS]
    if over:
        raise ValueError(
            f"embedding 上限闸: {len(over)} 个 chunk 超 {EMBED_MAX_TOKENS} token, "
            f"入库会被静默截断: {over[:5]}")
    print(f"embedding 上限闸: PASS (按文件实测, 上限 {EMBED_MAX_TOKENS})")
    return written


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
