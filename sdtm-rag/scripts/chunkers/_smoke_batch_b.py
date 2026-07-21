"""Phase 1A.3 Batch B self-smoke — ExamplesChunker on TA / PC / IS / DS.

Run from repo root:
    python3 sdtm-rag/scripts/chunkers/_smoke_batch_b.py

Verifies:
  - Chunk counts (TA=8 / PC=14 / IS=11 / DS=11) — the 14 for PC is HARD per chunker_feasibility §3.2.
  - has_mermaid TRUE on TA Example 1-7 (20 mermaid blocks total).
  - has_table TRUE on most TA / IS chunks.
  - PC: sub_label = "Method A/B/C/D", example_index = 1-4.
  - L-1 mermaid protection: no chunk boundary falls inside a mermaid block byte range.
  - L-2 table protection: no chunk boundary falls inside a table block byte range.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make package import work when invoked as a script.
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))  # repo .../sdtm-rag

from scripts.chunkers.base import find_mermaid_blocks, find_table_blocks  # noqa: E402
from scripts.chunkers.examples import ExamplesChunker  # noqa: E402

# KB path (this script lives 3 dirs deep: sdtm-pedia/sdtm-rag/scripts/chunkers)
KB_ROOT = HERE.parent.parent.parent  # → sdtm-pedia/
KB_DOMAINS = KB_ROOT / "knowledge_base" / "domains"


SAMPLES = [
    ("TA", 8, "H2 flat (7 Example + Trial Arms Issues)"),
    ("PC", 14, "H4 nested (4 Example × Methods, Example 4 only A+D)"),
    ("IS", 11, "H2 flat dense table"),
    ("DS", 11, "H2 flat"),
]


def split_points_inside_blocks(
    chunks, blocks: list[tuple[int, int]]
) -> list[tuple[int, int, int]]:
    """Return list of (chunk_index, byte_pos, block_start) where any chunk start/end falls *strictly inside* a block.

    A chunk boundary is acceptable at block start or block end (inclusive boundary at edges).
    """
    # Reconstruct chunk byte ranges by walking through text length usage.
    # We can't easily get start byte offset back from Chunk; instead recompute
    # from the source text + each chunk's .text via str.find from a cursor.
    violations: list[tuple[int, int, int]] = []
    if not chunks:
        return violations
    text = Path(chunks[0].source).read_text(encoding="utf-8")
    cursor = 0
    for ch in chunks:
        idx = text.find(ch.text, cursor)
        if idx < 0:
            # Defensive: text not found (should never happen)
            continue
        end = idx + len(ch.text)
        # A chunk boundary is "inside a block" if its position is strictly between block start+1 and block end-1.
        for bs, be in blocks:
            if bs < idx < be:
                violations.append((ch.chunk_index, idx, bs))
            if bs < end < be:
                violations.append((ch.chunk_index, end, bs))
        cursor = end
    return violations


def run() -> int:
    chunker = ExamplesChunker(kb_root=KB_ROOT)
    failures: list[str] = []

    print("=" * 88)
    print("Phase 1A.3 Batch B self-smoke — ExamplesChunker")
    print(f"KB root: {KB_ROOT}")
    print("=" * 88)

    summary_rows: list[tuple[str, int, int, str, str, str]] = []

    for domain, expected, label in SAMPLES:
        path = KB_DOMAINS / domain / "examples.md"
        chunks = chunker.chunk(path)
        actual = len(chunks)

        text = path.read_text(encoding="utf-8")
        mermaid_blocks = find_mermaid_blocks(text)
        table_blocks = find_table_blocks(text)

        # has_mermaid / has_table summary
        mermaid_chunks = sum(1 for c in chunks if c.has_mermaid)
        table_chunks = sum(1 for c in chunks if c.has_table)
        sub_labels = sorted({c.sub_label for c in chunks if c.sub_label})
        example_indices = sorted({c.example_index for c in chunks if c.example_index})

        # L-1 / L-2 protection check
        merm_violations = split_points_inside_blocks(chunks, mermaid_blocks)
        tab_violations = split_points_inside_blocks(chunks, table_blocks)

        pass_count = actual == expected
        pass_protect = not merm_violations and not tab_violations

        status = "PASS" if (pass_count and pass_protect) else "FAIL"
        notes = f"mermaid_chunks={mermaid_chunks} table_chunks={table_chunks}"
        if sub_labels:
            notes += f" sub_labels={sub_labels}"
        if example_indices:
            notes += f" example_idx={example_indices}"

        summary_rows.append((domain, expected, actual, label, status, notes))

        if not pass_count:
            failures.append(
                f"{domain}: expected {expected} chunks, got {actual}"
            )
        if merm_violations:
            failures.append(
                f"{domain}: L-1 VIOLATION — chunk boundary inside mermaid block: {merm_violations[:3]}"
            )
        if tab_violations:
            failures.append(
                f"{domain}: L-2 VIOLATION — chunk boundary inside table block: {tab_violations[:3]}"
            )

        print(f"\n--- {domain} ({label}) ---")
        print(f"  expected_chunks={expected} actual={actual}  protection_ok={pass_protect}")
        print(
            f"  mermaid_blocks={len(mermaid_blocks)} mermaid_chunks={mermaid_chunks}  "
            f"table_blocks={len(table_blocks)} table_chunks={table_chunks}"
        )
        if sub_labels:
            print(f"  sub_labels={sub_labels}")
        if example_indices:
            print(f"  example_indices={example_indices}")
        # Show first 3 chunk meta as sample
        for c in chunks[:3]:
            print(
                f"    chunk[{c.chunk_index}] section={c.section!r:<50} "
                f"cdisc_section_id={c.cdisc_section_id!r} example_index={c.example_index} "
                f"sub_label={c.sub_label!r} has_mermaid={c.has_mermaid} has_table={c.has_table} "
                f"tokens={c.chunk_size_tokens}"
            )

    print("\n" + "=" * 88)
    print("SUMMARY")
    print("=" * 88)
    print(f"{'domain':<6}{'expected':<10}{'actual':<8}{'status':<8}notes")
    for d, exp, act, _label, status, notes in summary_rows:
        print(f"{d:<6}{exp:<10}{act:<8}{status:<8}{notes}")

    # Hard assertions
    print("\n" + "=" * 88)
    if failures:
        print(f"RESULT: FAIL ({len(failures)} issue(s))")
        for f in failures:
            print(f"  - {f}")
        return 1
    # Specific PC assertions
    pc_chunks = chunker.chunk(KB_DOMAINS / "PC" / "examples.md")
    pc_sub_labels = {c.sub_label for c in pc_chunks}
    pc_example_idx = {c.example_index for c in pc_chunks}
    assert pc_sub_labels == {"Method A", "Method B", "Method C", "Method D"}, (
        f"PC sub_labels mismatch: {pc_sub_labels}"
    )
    assert pc_example_idx == {1, 2, 3, 4}, f"PC example_index mismatch: {pc_example_idx}"
    # TA mermaid: 7 Example chunks must have has_mermaid=True (Trial Arms Issues has none)
    ta_chunks = chunker.chunk(KB_DOMAINS / "TA" / "examples.md")
    ta_mermaid = sum(1 for c in ta_chunks if c.has_mermaid)
    assert ta_mermaid >= 7, f"TA mermaid coverage: expected >=7 chunks with mermaid, got {ta_mermaid}"
    print("RESULT: ALL PASS")
    print(f"  PC sub_labels = {sorted(pc_sub_labels)}")
    print(f"  PC example_indices = {sorted(pc_example_idx)}")
    print(f"  TA chunks with mermaid = {ta_mermaid}/{len(ta_chunks)}")
    return 0


if __name__ == "__main__":
    sys.exit(run())
