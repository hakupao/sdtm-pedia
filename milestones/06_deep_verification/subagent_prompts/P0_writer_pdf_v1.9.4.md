# P0 Writer PDF — 原子化 prompt v1.9.4

> Version: v1.9.4 (2026-05-11, post P2 B-03c rounds 10-12 CLOSED paired-sync with `P0_writer_md_v1.9.4.md`)
> 基于 v1.9.3 (2026-05-07) + B-03c rounds 10-12 evidence (MD-side driven; PDF-side scope unchanged)
> 角色: Writer PDF (原子化), 独立 subagent
> v1.9.4 变更 over v1.9.3 (PDF-side scope): post P1 CLOSURE (535/535 = 100% 2026-04-29); prompt retired from active production; maintained for audit reference only. Paired-sync with writer_md v1.9.4 §G-1..G-4 (PDF-side N/A for all G-rules — FIGURE-heavy domains, multi-slice, descriptive-title H3 all MD-side patterns).

## 角色硬约束 + N21 ban writer-family (v1.7/v1.8/v1.9/v1.9.1/v1.9.2/v1.9.3 carry-forward unchanged)

参 `archive/v1.7_final_2026-04-30/P0_writer_pdf_v1.7.md` §角色硬约束 + §N21 (PDF-side EMERGENCY-CRITICAL ban from round 10).
参 `archive/v1.9.3_final_2026-05-11/P0_writer_pdf_v1.9.3.md` §F-1..F-3 paired-sync notes 全文.

═══════════════════════════════════════════════════════════════════
## v1.9.4 PAIRED-SYNC NOTES (PDF-side cross-format applicability of MD-side G-rules)
═══════════════════════════════════════════════════════════════════

**Status note**: P1 PDF atomization CLOSED 2026-04-29 (12487 atoms 535/535 = 100%). PDF writer prompt retired from active production; maintained for audit reference + cross-format applicability of MD-side rules only.

### §G-1 §F-1 descriptive-title H3 title-agnostic — PDF-side N/A (MD-domain pattern)

§G-1 extends §F-1 §2.11 Plan B sub-namespace to include descriptive-title H3s. PDF-side does NOT have markdown H2/H3 syntax — PDF section numbering uses absolute page-anchored identifiers (e.g., `§6.3.5.9.3 [Title]`). Descriptive-title H3 is MD-domain pattern; PDF-side has analogous concept (PDF section titles can be descriptive) but does NOT use sib_idx-based namespace.

**PDF↔MD 跨格式 (matcher domain)**: When matcher cross-references an MD §G-1 trigger atom (e.g., `§TE.4.1 [Granularity of Trial Elements]`) with a PDF atom, the PDF atom's parent_section will be page-anchored absolute. Matcher §M-G-1 paired-sync rule: accept cross-format namespace divergence as canonical (do NOT flag schema_drift); use atom verbatim + page/line range as primary cross-format match key.

### §G-2 §2.4 multi-slice atom_id 续号 — PDF-side N/A (different chunking strategy)

§G-2 codifies multi-slice atom_id continuation across batch boundaries for MD-side §2.4 split files. PDF-side used different chunking strategy during P1 (page-range based, not slice-based). PDF atoms had `<batch>_a<N>` form without cross-slice continuation requirement.

**PDF↔MD 跨格式 (matcher domain)**: Matcher §M-G-2 multi-slice continuation acceptance is MD-domain only; PDF↔MD matching for multi-slice MD files matches each MD atom (regardless of which slice batch it came from) to corresponding PDF atom by verbatim + page/line range. Multi-slice atom_id continuation does NOT affect cross-format match.

### §G-3 §F-2 de-figure-naive STANDARD recipe — PDF-side N/A (different metric)

PDF-side ratio is atoms/page (not atoms/line). P1 closure baseline ~25-30 atoms/page (12487 / 535 ≈ 23.3 atoms/page). PDF-side does NOT use atoms/line ratio or de-figure-naive formula.

PDF-side FIGURE handling: PDF mermaid blocks rendered as images during P1; atom count for FIGURE pages used page-level estimate, not line-level. Future P3+ PDF batches (if any) would apply page-level adjustment analogous to §G-3 but separate codification.

### §G-4 §2.6 FIGURE-heavy estimate adjustment — PDF-side similar concept N/A direct (LOW)

PDF-side equivalent: page-content-density variation. PDF dense table pages vs sparse narrative pages have different atoms/page ratios. P1 closure data: range ~10-50 atoms/page driven by content type. PDF-side did NOT trigger FIGURE-heavy threshold (PDF mermaid rendered as embedded images, not source-line spans).

**FIGURE build-script defensive recipe (C-R12-07)**: Build-script issue applies to MD-side mermaid atom body generation (trailing-newline strip). PDF-side does NOT use build-script for mermaid body — PDF mermaid atoms reference page images. N/A PDF.

### §F-1..F-3 carry-forward (v1.9.3 PDF-side paired-sync unchanged)

ALL v1.9.3 §F-1..F-3 PDF-side paired-sync notes carry-forward to v1.9.4 unchanged.

### §E-1..E-6 carry-forward (v1.9.2 PDF-side paired-sync unchanged)

ALL v1.9.2 §E-1..E-6 PDF-side paired-sync notes carry-forward to v1.9.4 unchanged.

### §D-1..D-8 carry-forward (v1.9.1 PDF-side paired-sync unchanged)

ALL v1.9.1 §D-1..D-8 PDF-side paired-sync notes carry-forward to v1.9.4 unchanged.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.4 sync)
═══════════════════════════════════════════════════════════════════

- **N21 PDF-side ban**: STRONGLY VALIDATED EXTENDED (P1 closure 535/535 sustained; B-03c rounds 10-12 cumulative 18 batches all general-purpose 0 N21 violation cross-format).
- **PDF-side schema 11-key universal**: SUSTAINED (P1 closure 12487 atoms verified).
- **PDF-side §G-1..G-4 paired-sync**: NEW STATUS — PDF-side MD-domain G-rules cross-format awareness codified (§G-1 descriptive-title H3 N/A direct PDF + §G-2 multi-slice N/A direct PDF + §G-3 de-figure different metric + §G-4 FIGURE-heavy similar concept but N/A direct).
- **PDF-side cross-format match (matcher domain)**: SUSTAINED — matcher accepts MD §G-1/G-2 patterns as canonical without flagging cross-format namespace or atom_id divergence.
- **P1 CLOSURE post-status**: PDF writer prompt retired from active production (last production cycle 2026-04-29); v1.9.4 maintenance bump for paired-sync versioning consistency only.

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.9.1 | 2026-05-05 | post P2 B-02 cycle CLOSED paired-sync: §D-1..D-8 PDF-side cross-format notes. |
| v1.9.2 | 2026-05-06 | post P2 B-03c rounds 01-06 CLOSED: paired-sync §E-1..E-6 cross-format notes. |
| v1.9.3 | 2026-05-07 | post P2 B-03c rounds 07-09 CLOSED: paired-sync §F-1..F-3 cross-format notes. |
| **v1.9.4** | **2026-05-11** | **post P2 B-03c rounds 10-12 CLOSED**; post P1 CLOSURE (535/535 = 100% 2026-04-29); prompt retired from active production; maintained for audit reference only. Paired-sync with writer_md v1.9.4 §G-1..G-4 (PDF-side N/A for all G-rules — FIGURE-heavy domains, multi-slice, descriptive-title H3 all MD-side patterns). No new rules or hooks. v1.9.3 archived. **Backward compatible** — P1 closure 12487 atoms byte-exact preserved. |
