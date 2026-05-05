# P0 Writer PDF — 原子化 prompt v1.9.1

> Version: v1.9.1 (2026-05-05, post P2 B-02 cycle CLOSED paired-sync with `P0_writer_md_v1.9.1.md`)
> 基于 v1.9 (2026-04-29) + B-02 cycle evidence
> 角色: Writer PDF (原子化), 独立 subagent
> v1.9.1 变更 over v1.9 (PDF-side scope): **carry-forward unchanged主体**; 仅 paired-sync notes for MD-side §D-1..D-8 cross-format applicability + STATUS PROMOTIONS 同步 + FALLBACK pool peer-alternative promotion.

## 角色硬约束 + N21 ban writer-family (v1.7/v1.8/v1.9 carry-forward unchanged)

参 `archive/v1.7_final_2026-04-30/P0_writer_pdf_v1.7.md` §角色硬约束 + §N21 (PDF-side EMERGENCY-CRITICAL ban from round 10).
参 `archive/v1.9_final_2026-05-05/P0_writer_pdf_v1.9.md` §C-1..C-8 paired-sync notes 全文.

═══════════════════════════════════════════════════════════════════
## v1.9.1 PAIRED-SYNC NOTES (PDF-side cross-format applicability of MD-side D-rules)
═══════════════════════════════════════════════════════════════════

### §D-1 Hook 22b kickoff numeric claim grep checksum — PDF-side 等价

PDF-side kickoff (P1 round 11+ baseline) 主要 numeric claims = page range / atom_count 估 / drift cal target page. PDF-side kickoff 写前 verify:

- page range: 用 page_index.json 校验 dispatch pages 在 PDF 总页范围内
- atom_count 估: 用 historical per-page 平均 (current ~22-30 atoms/page in P1) calibrate
- drift cal target: 跨 round cadence (e.g., batch 42 → 45 → 48 ...) verify

PDF-side未来 P3+ batches (if any) sustains §D-1 spirit: orchestrator preflight verify numeric claims; writer Rule-B trust source PDF over kickoff.

**v1.9.1 PDF-side baseline**: P1 closure complete (535/535 = 100% 2026-04-29). PDF-side writer prompt 主要 reference 价值 = matcher P4a 跨 PDF↔MD 匹配粒度 + future updates 时 baseline.

### §D-2 D7 NOTE blockquote-prefix bold-Note carve-out — PDF-side 等价

PDF visual NOTE patterns 已 codify v1.7+ (visual indent + 加粗 / italic / box separator). PDF-side blockquote 是 markdown 概念, PDF rendering 通常对应 indent + 加粗 box. multimodal 视觉判读已 cover.

v1.9.1 PDF-side 不 add new rule, 只 status sync: **NOTE atom_type 在 PDF-side carve-out cover 视觉 indent + 加粗 + box patterns; MD-side D7 extends to blockquote-prefix variant** — 两侧 semantic alignment.

### §D-3 D5 markdown-uniform numbered Heading dual-constraint — PDF-side 部分等价

PDF-side h_lvl 通过 visual font size / numbering depth 推断, 不依 markdown `#` count. PDF-side 不会发生 "markdown markup 与 semantic 错开" 因为 PDF 没有 markup. PDF-side h_lvl 与 parent_section 总是 semantic-correct.

v1.9.1 PDF-side 不 add new rule. MD-side D5 仅 MD scope.

### §D-4 D8 numberless `## Overview` chapter root inherit — PDF-side 等价

PDF-side 也常见 chapter 前置 narrative section (无 numbered sub-section 标号). PDF-side parent_section 已合规 chapter root inherit (P1 round 5+ evidence: chapter 引言 atoms inherit `§N [Chapter Title]`).

v1.9.1 PDF-side 不 add new rule. MD-side D8 是同 family 的 markdown-specific manifestation.

### §D-5 bold-caption SENTENCE retention rule — PDF-side N/A 直接

PDF visual bold 通过 multimodal 视觉判读, 已 codify 在 v1.7 §A-N23 (PDF visual emphasis 不自动 → HEADING). bold-caption SENTENCE 模式 PDF-side 等价 = 视觉粗体 caption inline w/ paragraph flow → SENTENCE.

v1.9.1 PDF-side 不 add new rule. MD-side D5 codify markdown-specific bold marker (`**...**`) variant.

### §D-6 TABLE_HEADER style 兼容 — PDF-side N/A

PDF-side TABLE_HEADER 用 `page` + `page_region` 锚, 不是 line range. PDF-side 不存在 line_end - line_start ≤ 1 概念. C-5/D-6 MD-only.

### §D-7 LOW codifications group — PDF-side 部分等价

- **§D-7.2 Axis 5 STRONGLY VALIDATED**: PDF-side 早期 codify (P1 round 14 N6 extension); v1.9.1 status sync — STRONGLY VALIDATED EXTENDED PDF + MD all-side
- **§D-7.4/7.6 S-02/S-04 等价**: PDF-side numberless H3 sib chain 各 H2 parent restart sib=1 + section 末尾 narrative inherit closest H2/H3 — pre-v1.9 已 implicit 应用
- **§D-7.7 D6 letter-prefix appendix-style H2**: PDF-side appendix 视觉 letter-prefix (e.g., Appendix A/B) 已 codify v1.5+ (P1 evidence). v1.9.1 status sync.
- **§D-7.8 schema v1.2.1**: PDF-side atoms 已 sustained schema v1.2.1 (P1 round 14 cumulative 12,487 atoms 0 schema violation). v1.9.1 status sync.
- **其他 LOW (§D-7.1/7.3/7.5/7.9/7.10/7.11/7.12/7.13)**: MD-only or housekeeping; PDF-side N/A 直接.

### §D-8 FALLBACK pool peer-alternative status — PDF-side 应用

PDF-side P1 batches 主体用 `oh-my-claudecode:executor`. P2 B-02 cycle 验证 `general-purpose` 等同 quality. v1.9.1 PDF-side baseline 同 update:

**PDF Writer pool** (peer-alternative):
- `oh-my-claudecode:executor` (preferred)
- `general-purpose` (peer-alternative, P2 B-02 sustained 7-batch validation transferable to PDF-side per recipe family-agnostic principle)

**PDF Reviewer pool** (peer-alternative):
- `oh-my-claudecode:scientist` / `code-reviewer` / `critic` (preferred)
- `pr-review-toolkit:code-reviewer` (peer-alternative)
- `feature-dev:code-reviewer` (peer-alternative inter-cycle)

**N21 ban list** (sustained PDF + MD all-side, unchanged): 5 writer-family agents banned (`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer`, `oh-my-claudecode:document-specialist`).

注: `general-purpose` **NOT** in N21 ban list (peer-alternative writer pool per writer_md §D-8 + B-02 sustained 7-batch validation).

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.1 sync with B-02 cycle evidence)
═══════════════════════════════════════════════════════════════════

- **N21 PDF + MD all-side blanket ban**: STRONGLY VALIDATED EXTENDED (P1 round 14 全闭 12,487 atoms + B-02 1,983 atoms 0 writer-family contamination)
- **FALLBACK pool peer-alternative**: NEW STATUS — applies cross-format (PDF + MD); recipe family-agnostic principle (P1 round 14 D-MS-7 cumulative 7-burn omc + 7-burn codex + 4-burn Plan single-agent + B-02 7-burn general-purpose all sustained)
- **Axis 5 STRONGLY VALIDATED EXTENDED**: PDF + MD all-side (P1 round 14 + B-02)
- **R-PDF-Page-Hard rule** (v1.9 NEW STATUS): SUSTAINED — P1 closure complete 0 page-shortfall failure
- **H_C content-conditional reliability hypothesis**: REJECTED (sustained from v1.9; P2 Pilot Attempt 1 + B-02 9 batches 0 narrative-content writer-family contamination opportunity since N21 blanket ban)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.7 | 2026-04-29 | post P1 round 10 cut EMERGENCY-CRITICAL: N21 SCOPED PDF-side blanket ban writer-family |
| v1.8 | 2026-04-30 | post P1 round 12 cut: 5 NEW patches N24-N28 paired-sync; N21 PDF-side carry-forward |
| v1.9 | 2026-04-29 | post P2 Pilot 2-attempt cycle: paired-sync with MD writer v1.9. N21 status: blanket all-side. R-PDF-Page-Hard NEW status. |
| **v1.9.1** | **2026-05-05** | **post P2 B-02 cycle CLOSED + cumulative audit GREEN-LIGHT 30/30=100%**: paired-sync with MD writer v1.9.1 8 NEW D-rules. PDF-side prompt 主体 unchanged. STATUS PROMOTIONS sustained: N21 EXTENDED + FALLBACK pool peer-alternative + Axis 5 EXTENDED + R-PDF-Page-Hard SUSTAINED + H_C REJECTED sustained. v1.9 archived `archive/v1.9_final_2026-05-05/`. NO 行为变化 PDF-side; status promotion + paired-sync notes only. |
