# P0 Writer PDF — 原子化 prompt v1.9.2

> Version: v1.9.2 (2026-05-06, post P2 B-03c rounds 01-06 cycle CLOSED paired-sync with `P0_writer_md_v1.9.2.md`)
> 基于 v1.9.1 (2026-05-05) + B-03c rounds 01-06 evidence (MD-side driven)
> 角色: Writer PDF (原子化), 独立 subagent
> v1.9.2 变更 over v1.9.1 (PDF-side scope): **carry-forward unchanged主体**; 仅 paired-sync notes for MD-side §E-1..E-6 cross-format applicability + schema 12-key 强制 (PDF-side 同 schema, atoms 跨格式 shape 一致) + status promotions sync.

## 角色硬约束 + N21 ban writer-family (v1.7/v1.8/v1.9/v1.9.1 carry-forward unchanged)

参 `archive/v1.7_final_2026-04-30/P0_writer_pdf_v1.7.md` §角色硬约束 + §N21 (PDF-side EMERGENCY-CRITICAL ban from round 10).
参 `archive/v1.9_final_2026-05-05/P0_writer_pdf_v1.9.md` §C-1..C-8 paired-sync notes 全文.
参 `archive/v1.9.1_final_2026-05-06/P0_writer_pdf_v1.9.1.md` §D-1..D-8 paired-sync notes 全文.

═══════════════════════════════════════════════════════════════════
## v1.9.2 PAIRED-SYNC NOTES (PDF-side cross-format applicability of MD-side E-rules)
═══════════════════════════════════════════════════════════════════

### §E-1 Dispatch contract: explicit JSON template + reference working atom — PDF-side 等价 (CRITICAL)

PDF-side dispatch prompt template (P1 era + future P3+ if any) MUST follow same standard as MD-side §E-1:

1. **Explicit JSON template** showing all schema fields with EXACT names. PDF atom schema has additional `page` field (vs MD's `line_start`/`line_end`); else identical to MD schema.
2. **Reference to working production atom** (e.g., point to `evidence/checkpoints/P1_round_14_batch_55_atoms.jsonl` or pilot atoms as gold reference).
3. **Explicit "NEVER" anti-patterns**:
- ❌ `verbatim_text` → use `verbatim`
- ❌ `atom_type: "H1"`/`"H2"` → use `atom_type: "HEADING"`
- ❌ Missing `page` (PDF) or `line_start`/`line_end` (MD) → REQUIRED int fields
- ❌ Missing `figure_ref` → REQUIRED (null for non-FIGURE)
- ❌ `extracted_by` string form → use object schema

**PDF-side baseline**: P1 closure complete (535/535 = 100% 2026-04-29 with v1.8 baseline). All P1 round 14 atoms already conform v1.9 schema 11-key (PDF-side has `page` instead of `line_start`/`line_end` pair, otherwise 11 vs MD 12 keys identical). Round 06 §E-1 codification protects future P3+ batches (if any) from same regression class.

**Hook 22c PDF-side**: pre-DONE schema self-validate — writer MUST verify each atom 11 keys (PDF) with EXACT names + R-2.8-1/2/3 + extracted_by object before writing JSONL. DONE report MUST include `schema_self_validate: PASS` confirmation.

### §E-2 R-2.8-1 H1 sibling_index=1 universal — PDF-side 等价 (HIGH)

PDF-side H1 atom (chapter title) 同样 sibling_index=1 universal. P1 era 12487 atoms all H1 sib=1 universal (verify post-fact). v1.9.2 codification PDF-side carry. Writer DONE report MUST include `r_2_8_1_h1_sib_idx_1: PASS` confirmation for any future P3+ batches.

### §E-3 R-2.8-2 TABLE_HEADER sibling_index=null universal — PDF-side 等价 (HIGH)

PDF-side TABLE_HEADER atoms 同样 sibling_index=null universal. P1 era TABLE_HEADER atoms (~290 cumulative pre-MD-side codify) all sib=null universal. v1.9.2 codification PDF-side carry.

**Note**: PDF-side TABLE_HEADER `line_end - line_start = 1` (Hook A1 v1.9 baseline). Same as MD-side.

### §E-4 R-2.8-3 extracted_by object schema universal — PDF-side 等价 (HIGH)

PDF-side `extracted_by` 同样 object schema with EXACTLY 3 fields: `subagent_type`, `prompt_version` (e.g., `P0_writer_pdf_v1.9.2`), `ts`. P1 era 12487 atoms verified post-round-04 codify (extracted_by object form sustained 0 violation P1).

### §E-5 MED-01 non-HEADING field-explicit-null — PDF-side 等价 (MEDIUM)

PDF-side non-HEADING atoms 同样 `heading_level=null` AND `sibling_index=null` EXPLICIT JSON null fields. P1 era atoms verified post-round-05 codify (sustained 0 violation P1).

### §E-6 FIGURE-vs-CODE_LITERAL boundary — PDF-side **N/A** for CODE_LITERAL

PDF-side does NOT have CODE_LITERAL atom_type (PDF rendering 不 distinguish text-as-code from text-as-narrative; visual rendering is the source of truth, no fenced markup). PDF-side FIGURE atoms = rasterized image atoms (mermaid block in MD source → rendered diagram image in PDF rendering).

PDF↔MD 跨格式: MD CODE_LITERAL atoms (literal codelist values like `"AE"`) 在 PDF 中 representation 通常是 inline italic 或 quoted text, atom_type=SENTENCE 在 PDF-side. matcher M-E6 跨格式 boundary 处理.

### §D-1..D-8 carry-forward (v1.9.1 PDF-side paired-sync unchanged)

ALL v1.9.1 §D-1..D-8 paired-sync notes carry-forward to v1.9.2 unchanged.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.2 sync)
═══════════════════════════════════════════════════════════════════

- **N21 PDF-side ban**: STRONGLY VALIDATED EXTENDED (P1 closure 535/535 + B-03c rounds 01-06 cumulative N21-banned 0 violation 跨格式)
- **PDF-side schema 11-key universal**: SUSTAINED (P1 closure 12487 atoms verified)
- **PDF-side R-2.8-1/2/3 + MED-01 + Hook 22c**: NEW STATUS CODIFIED (v1.9.2 paired-sync; PDF-side P3+ batches if any 强制 enforce)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.9 | 2026-04-29 | post P2 Pilot cycle: paired-sync with writer_md v1.9 |
| v1.9.1 | 2026-05-05 | post P2 B-02 cycle CLOSED paired-sync: §D-1..D-8 PDF-side cross-format notes + status promotions |
| **v1.9.2** | **2026-05-06** | **post P2 B-03c rounds 01-06 CLOSED**: paired-sync with writer_md/reviewer/matcher v1.9.2. 6 NEW E-rules cross-format applicability notes (E-1 dispatch JSON template + E-2/E-3/E-4 R-2.8-1/2/3 explicit codify + E-5 MED-01 explicit null + E-6 FIGURE/CODE_LITERAL boundary N/A PDF). Hook 22c PDF-side schema self-validate. v1.9.1 archived. **Backward compatible** — P1 closure 12487 atoms byte-exact preserved. |
