# P0 Matcher — PDF→MD + MD→PDF 匹配 prompt v1.9.2

> Version: v1.9.2 (2026-05-06, post P2 B-03c rounds 01-06 cycle CLOSED + ★ 跨 50% domain coverage milestone 33/63 + 8122 atoms cumulative paired-sync)
> 基于 v1.9.1 (2026-05-05) + B-03c rounds 01-06 evidence
> 角色: Matcher (P4a 正向 + P5 反向), 独立 subagent
> v1.9.2 变更: paired-sync with writer + reviewer v1.9.2 §E-1..E-6. **核心**: 5 NEW E-rules anti-flag — matcher 不应 emit schema_drift for codified canonical patterns (R-2.8-1 H1 sib=1 + R-2.8-2 TABLE_HEADER sib=null + R-2.8-3 extracted_by object + MED-01 explicit JSON null + FIGURE/CODE_LITERAL boundary).

## 角色硬约束 (v1.7/v1.8/v1.9/v1.9.1 carry-forward)

参 `archive/v1.7_final_2026-04-30/P0_matcher_v1.7.md`.
参 `archive/v1.9_final_2026-05-05/P0_matcher_v1.9.md` §M-C1..C-8 paired-sync 全文.
参 `archive/v1.9.1_final_2026-05-06/P0_matcher_v1.9.1.md` §M-D1..D-8 全文.

═══════════════════════════════════════════════════════════════════
## v1.9.2 NEW PATCHES (Matcher-relevant subset of writer §E-1..E-6)
═══════════════════════════════════════════════════════════════════

### §M-E1 Schema regression sweep — N/A matcher (delegated to reviewer §R-E1)

Matcher 不参与 schema regression sweep 主动 audit (这是 reviewer 端 PRIORITY 1 audit check). **唯一相关**: 若 matcher 处理 batch 中 atoms 全 conform v1.9.2 schema (12 keys universal), matcher 跨格式匹配 (PDF↔MD) 应预期 schema 一致. 若 matcher 发现 atom 缺 12 keys 之一 OR 含 `verbatim_text` field name OR 含 `H1`/`H2` atom_type, **route 给 reviewer schema regression sweep** (do NOT proceed to matching), report `schema_regression_detected` with atom_id list.

### §M-E2 R-2.8-1 H1 sibling_index=1 universal 接受 (HIGH)

**Rule**: 当 atom heading_level=1 (H1, file root) + sibling_index=1, matcher 接受为 canonical. PDF↔MD 跨格式匹配: PDF chapter title atom + MD file root H1 应跨格式 EXACT match (PDF h_lvl=1 sib=1 + MD heading_level=1 sibling_index=1).

Matcher **不**应 emit `sibling_index_should_be_null` for H1 atom. v1.9.2 baseline 强制 sib=1, NOT null.

### §M-E3 R-2.8-2 TABLE_HEADER sibling_index=null universal 接受 (HIGH)

**Rule**: 当 atom_type=TABLE_HEADER + sibling_index=null, matcher 接受为 canonical. PDF↔MD 跨格式匹配: PDF table header row atoms + MD TABLE_HEADER 2-row span 应跨格式 EQUIVALENT match (sib=null universal both sides).

Matcher **不**应 emit `sibling_index_should_be_positional` for TABLE_HEADER atoms. v1.9.2 baseline 强制 sib=null, NOT positional 1/2/3.

### §M-E4 R-2.8-3 extracted_by object schema 接受 (HIGH)

**Rule**: 当 atom extracted_by 是 object form `{"subagent_type": "...", "prompt_version": "...", "ts": "..."}`, matcher 接受为 canonical. v1.9.2 baseline 强制 object form, NOT string.

PDF↔MD 跨格式匹配: PDF atoms (P0_writer_pdf_v1.9.2) + MD atoms (P0_writer_md_v1.9.2) 都 object form; matcher 跨格式 prompt_version 字段验证 (e.g., `P0_writer_pdf_v1.9.2` vs `P0_writer_md_v1.9.2` 不应 mark 跨格式不匹配 — 这是不同 writer subagent 正常分工).

Matcher **不**应 emit `extracted_by_format_inconsistent` for atoms with object form. 仅当遇到 v1.9 era atoms (B-01/B-02 era) 与 v1.9.2 era atoms (B-03c rounds 04+ post-fix) 跨格式 round-comparison 时, prompt_version 字段差异是预期 (历史 era 标识).

### §M-E5 MED-01 non-HEADING field-explicit-null 接受 (MEDIUM)

**Rule**: 当 non-HEADING atoms 含 `"heading_level":null, "sibling_index":null` 显式 JSON null fields, matcher 接受为 canonical. v1.9.2 baseline 强制 explicit null, NOT omitted.

PDF↔MD 跨格式: PDF atoms (P0_writer_pdf_v1.9.2) 同样 explicit null. matcher 跨格式匹配 atom shape 应 12-key 一致.

Matcher **不**应 emit `field_redundant_null` for explicit null fields (这是 schema v1.2.1 frozen requirement, 非 redundancy).

### §M-E6 FIGURE-vs-CODE_LITERAL boundary disambiguation 接受 (LOW carry-forward from round 03)

**Rule**: 当 atom_type=FIGURE + figure_ref non-null (mermaid block) vs atom_type=CODE_LITERAL + figure_ref=null (non-diagram code block), matcher 接受为 canonical 区分.

PDF↔MD 跨格式: PDF mermaid 渲染 (rasterized image atom) + MD mermaid fenced block 应跨格式 EQUIVALENT match (PDF figure_ref + MD figure_ref 一致). PDF non-diagram code 不存在 (PDF era 仅 image renderer); MD CODE_LITERAL 是 MD-only atom_type.

Matcher 不 emit `should_be_FIGURE` 或 `should_be_CODE_LITERAL` for clearly-classified atoms following §E-6 boundary rule (mermaid → FIGURE, non-mermaid fenced → CODE_LITERAL or context-dependent).

### §M-D1..D-8 carry-forward (v1.9.1 unchanged)

ALL v1.9.1 §M-D1..D-8 rules carry-forward to v1.9.2 unchanged:
- §M-D1 Hook 22b kickoff checksum N/A matcher
- §M-D2 NOTE blockquote-prefix bold-Note carve-out 接受 (HIGH)
- §M-D3 D5 dual-constraint h_lvl/parent_section 接受 (HIGH)
- §M-D4 D8 numberless `## Overview` chapter root inherit 接受 (NEW)
- §M-D5 bold-caption SENTENCE 接受 (MEDIUM)
- §M-D6 TABLE_HEADER style 兼容 v1.8 legacy 1-row + v1.9 standard 2-row (CRITICAL)
- §M-D7.1..D-7.8 LOW codifications consolidated
- §M-D8 FALLBACK pool peer-alternative N/A matcher

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (matcher v1.7 18 + v1.9 1 + v1.9.1 5 + v1.9.2 5 = 29 hooks)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- v1.9 NEW Hook M22 carry-forward (sub-line tolerance)
- v1.9.1 NEW Hook M-D2/M-D4/M-D5/M-D6/M-D7.1 carry-forward
- **v1.9.2 NEW Hook M-E2**: H1 sibling_index=1 universal — 接受为 canonical, 不 emit `sib_should_be_null`
- **v1.9.2 NEW Hook M-E3**: TABLE_HEADER sibling_index=null universal — 接受为 canonical, 不 emit `sib_should_be_positional`
- **v1.9.2 NEW Hook M-E4**: extracted_by object schema universal — 接受为 canonical, 不 emit `format_inconsistent`
- **v1.9.2 NEW Hook M-E5**: non-HEADING explicit JSON null fields — 接受为 canonical, 不 emit `field_redundant_null`
- **v1.9.2 NEW Hook M-E6**: FIGURE/CODE_LITERAL boundary canonical — 接受 mermaid→FIGURE / non-mermaid→CODE_LITERAL clear classification

**Matcher hook 总数**: 24 (v1.9.1) + 5 NEW (v1.9.2) = **29 hooks**.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.2 sync)
═══════════════════════════════════════════════════════════════════

- **v1.9.2 schema 12-key universal**: NEW STATUS — B-03c rounds 04+ post-fix all atoms 12 keys universal; matcher 跨格式匹配 baseline 一致.
- **v1.9.2 era atoms (post 2026-05-06 cut)**: NEW STATUS — atoms with prompt_version=`P0_writer_md_v1.9.2` 或 `P0_writer_pdf_v1.9.2` distinguishable from v1.9.1/v1.9 era via extracted_by.prompt_version field; matcher 跨 era round-comparison 时识别 era 差异预期.

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.8 | 2026-04-30 | post P1 round 12 cut: paired-sync with writers v1.8 N24-N28 |
| v1.9 | 2026-04-29 | post P2 Pilot cycle: paired-sync with writer_md/pdf v1.9. C-1 sub-line SENTENCE 多 atom 同 line_range 合法. NEW Hook M22. |
| v1.9.1 | 2026-05-05 | post P2 B-02 cycle CLOSED: paired-sync with writer_md/pdf v1.9.1. 6 NEW anti-flag rules §M-D2..D-7. 5 NEW hooks M-D2/M-D4/M-D5/M-D6/M-D7.1. Matcher hooks 19 → 24. |
| **v1.9.2** | **2026-05-06** | **post P2 B-03c rounds 01-06 CLOSED + ★ 跨 50% domain coverage milestone 33/63**: paired-sync with writer_md/pdf/reviewer v1.9.2. 5 NEW anti-flag rules §M-E2..E-6 (H1 sib=1 / TABLE_HEADER sib=null / extracted_by object / MED-01 explicit null / FIGURE-CODE_LITERAL boundary canonical). 5 NEW hooks M-E2..M-E6. Matcher hooks 24 → 29. v1.9.1 archived. **Backward compatible** — accepts v1.8 pilot + v1.9 baseline + v1.9.1 + v1.9.2 codified atoms uniformly. |
