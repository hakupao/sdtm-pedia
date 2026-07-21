# P0 Writer PDF — 原子化 prompt v1.9.3

> Version: v1.9.3 (2026-05-07, post P2 B-03c rounds 07-09 CLOSED paired-sync with `P0_writer_md_v1.9.3.md`)
> 基于 v1.9.2 (2026-05-06) + B-03c rounds 07-09 evidence (MD-side driven; PDF-side scope unchanged)
> 角色: Writer PDF (原子化), 独立 subagent
> v1.9.3 变更 over v1.9.2 (PDF-side scope): **carry-forward unchanged主体**; 仅 paired-sync notes for MD-side §F-1..F-3 cross-format applicability.

## 角色硬约束 + N21 ban writer-family (v1.7/v1.8/v1.9/v1.9.1/v1.9.2 carry-forward unchanged)

参 `archive/v1.7_final_2026-04-30/P0_writer_pdf_v1.7.md` §角色硬约束 + §N21 (PDF-side EMERGENCY-CRITICAL ban from round 10).
参 `archive/v1.9.2_final_2026-05-07/P0_writer_pdf_v1.9.2.md` §E-1..E-6 paired-sync notes 全文.

═══════════════════════════════════════════════════════════════════
## v1.9.3 PAIRED-SYNC NOTES (PDF-side cross-format applicability of MD-side F-rules)
═══════════════════════════════════════════════════════════════════

### §F-1 §2.11 Plan B sub-namespace by sib_idx for numberless H2 with H3 children — PDF-side N/A or limited applicability (HIGH)

PDF-side semantic: PDF chapter/section structure renders headings via font size + visual hierarchy, NOT markdown `##`/`###` syntax. Concept of "numberless H2" does NOT directly translate (PDF Section/sub-section numbering is part of the document outline by design — chapters are numbered explicitly e.g., "6.3.5.9.3").

**PDF-side baseline**: P1 closure complete (12487 atoms 2026-04-29 with v1.8 baseline). PDF atoms parent_section uses absolute page-anchored section identifier (`§6.3.5.9.3 [Title]`), NOT MD-style sib_idx-based sub-namespace. §F-1 sib_idx-based hierarchy is MD-domain ONLY.

**PDF↔MD 跨格式 (matcher domain)**: When matcher cross-references an MD atom under §F-1 sub-namespace (e.g., `§RS.2.2 [References]`) with a PDF atom, the PDF atom's parent_section will be page-anchored absolute (`§6.x.y [Section title]` for PDF rendering of the same source content). Matcher §M-F-1 paired-sync rule: accept cross-format namespace divergence as canonical (do NOT flag schema_drift); use atom verbatim + page/line range as primary cross-format match key.

**Hook F-1 PDF-side**: N/A (PDF-side does NOT have §2.11 Plan B trigger). PDF writer DONE report unchanged.

### §F-2 atoms/line ratio empirical band 0.59-0.85 — PDF-side N/A (different metric)

PDF-side ratio is atoms/page (not atoms/line). P1 closure baseline ~25-30 atoms/page (12487 / 535 ≈ 23 atoms/page). PDF-side does NOT use atoms/line ratio for kickoff estimate.

PDF-side kickoff estimate uses atoms/page band TBD if/when P3+ batches arise.

### §F-3 Kickoff atom estimate calibration multi-level nested-list — PDF-side similar concept (LOW)

PDF-side equivalent: page-content-density variation. PDF dense table pages vs sparse narrative pages have different atoms/page ratios. P1 closure data: range ~10-50 atoms/page driven by content type. Future P3+ kickoffs (if any) should apply similar calibration discount factor for known content patterns.

### §E-1..E-6 carry-forward (v1.9.2 PDF-side paired-sync unchanged)

ALL v1.9.2 §E-1..E-6 PDF-side paired-sync notes carry-forward to v1.9.3 unchanged.

### §D-1..D-8 carry-forward (v1.9.1 PDF-side paired-sync unchanged)

ALL v1.9.1 §D-1..D-8 PDF-side paired-sync notes carry-forward to v1.9.3 unchanged.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.3 sync)
═══════════════════════════════════════════════════════════════════

- **N21 PDF-side ban**: STRONGLY VALIDATED EXTENDED (P1 closure 535/535 sustained; B-03c rounds 07-09 cumulative 30 batches all general-purpose 0 N21 violation cross-format).
- **PDF-side schema 11-key universal**: SUSTAINED (P1 closure 12487 atoms verified).
- **PDF-side §F-1..F-3 paired-sync**: NEW STATUS — PDF-side MD-domain rules cross-format awareness codified (§F-1 N/A direct PDF + §F-2 different metric + §F-3 similar concept).
- **PDF-side cross-format match (matcher domain)**: SUSTAINED — matcher accepts MD §F-1 sub-namespace as canonical without flagging cross-format namespace divergence.

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.9.1 | 2026-05-05 | post P2 B-02 cycle CLOSED paired-sync: §D-1..D-8 PDF-side cross-format notes. |
| v1.9.2 | 2026-05-06 | post P2 B-03c rounds 01-06 CLOSED: paired-sync §E-1..E-6 cross-format notes. |
| **v1.9.3** | **2026-05-07** | **post P2 B-03c rounds 07-09 CLOSED**: paired-sync with writer_md/reviewer/matcher v1.9.3. 3 NEW F-rules cross-format applicability notes (F-1 §2.11 Plan B MD-domain ONLY + F-2 different metric + F-3 similar concept). v1.9.2 archived. **Backward compatible** — P1 closure 12487 atoms byte-exact preserved. |
