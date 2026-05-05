# P0 Writer PDF — 原子化 prompt v1.9

> Version: v1.9 (2026-04-29, post P2 Pilot cycle paired-sync with `P0_writer_md_v1.9.md`)
> 基于 v1.8 (2026-04-30) + P2 Pilot evidence
> 角色: Writer PDF (原子化), 独立 subagent
> v1.9 变更 over v1.8 (PDF-side scope): **N21 carry-forward unchanged** (PDF-side 已 ban writer-family since round 10); MD-side P2 Pilot 实证 N21 应扩到 MD-side, 反向证实 PDF-side N21 决策正确. PDF-side prompt 主体 carry-forward unchanged; 仅 paired-sync 注释 + status promotion 同步.

## 角色硬约束 + N21 ban writer-family (v1.7/v1.8 carry-forward unchanged)

参 `archive/v1.7_final_2026-04-30/P0_writer_pdf_v1.7.md` §角色硬约束 + §N21 (PDF-side EMERGENCY-CRITICAL ban from round 10).

═══════════════════════════════════════════════════════════════════
## v1.9 PAIRED-SYNC NOTES (PDF-side cross-format applicability of MD-side patches)
═══════════════════════════════════════════════════════════════════

### §C-1 (sub-line SENTENCE) — N/A PDF-side direct, but matcher cross-format relevant

PDF-side originals 已是 sentence-level (PDF 没有 markdown line 概念, 原子化按段落 + 句子). C-1 主要影响 P4a matcher 设计 (PDF sentence ↔ MD sub-line sentence 匹配粒度对齐).

### §C-2 (N21 全 ban writer-family) — PDF-side carry-forward unchanged

PDF-side N21 since round 10 cut (commit ?, 2026-04-29). MD-side 现在追上. PDF-side prompt 不变, status promotion 同步: **N21 现在是 PDF + MD all-side 全 ban**.

### §C-3 R-MD-Slice-Hard — 概念扩到 PDF-side hard page range

PDF-side dispatch 派发用 page range (而非 line range). C-3 PDF-side 等价: dispatch "pages N-M" → writer MUST cover all atoms in [N, M] inclusive, 不得在 N..M 内提前停止 (semantic boundary 不是停止信号).

P1 round 14 大部分 batches 已 implicit 满足此规则 (page-boundary 在 reconciler 阶段校验). v1.9 显式 codify 作 R-PDF-Page-Hard 同 hardness 等级.

### §C-4 Hook 22 NEW — PDF-side adapter

PDF-side Hook 22 等价: writer DONE 前自校验 last atom `page == dispatch_pages_end` 且 `page_region` 含 "bottom" 或 "full" (除非 dispatch 是 partial-page scope). 防 PDF-side page-shortfall silent failure.

### §C-5 TABLE_HEADER line_end ≤ line_start+1 — PDF-side N/A

PDF-side TABLE_HEADER 用 `page` + `page_region` 锚, 不是 line range. C-5 MD-only.

### §C-6 bold non-HEADING — PDF-side N/A

PDF visual bold 通过 multimodal 视觉判读, 已 codify 在 v1.7 §A-N23. PDF-side 不受 C-6 影响.

### §C-7 LIST_ITEM full prefix + multi-sentence — PDF-side cross-applicability

PDF-side 也应满足 (P1 round 14 实测 executor 已合规). v1.9 显式 codify 同 MD-side.

### §C-8 file field full repo-relative path — PDF-side carry-forward

PDF-side file field 已是 PDF 路径 (`source/SDTM_v2.0.pdf` / `source/SDTMIG v3.4 (no header footer).pdf`), full path 已合规. C-8 MD-only.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9 sync)
═══════════════════════════════════════════════════════════════════

- **N21 PDF + MD all-side blanket ban**: **STRONGLY VALIDATED** post P2 Pilot Attempt 1 (MD-side 实证 reproduce PDF-side N21 trigger pattern). PDF-side N21 since round 10 + 4 successful rounds = 1877 atoms 0 hallucination; MD-side now joins. v1.9 状态: blanket all-side, no exceptions.
- **H_C content-conditional reliability hypothesis** (round 14 D-MS-NEW-14-5): **REJECTED**. P2 Pilot Attempt 1 反证 narrative content writer-family 也不可信. PDF-side 实测早已暗示 (P1 round 5-10 evidence accumulated to N21 trigger).
- **R-PDF-Page-Hard rule**: NEW STATUS, paired-sync with R-MD-Slice-Hard. PDF dispatcher hardness baseline.

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.7 | 2026-04-29 | post P1 round 10 cut EMERGENCY-CRITICAL: N21 SCOPED PDF-side blanket ban writer-family |
| v1.8 | 2026-04-30 | post P1 round 12 cut: 5 NEW patches N24-N28 paired-sync; N21 PDF-side carry-forward |
| **v1.9** | **2026-04-29** | **post P2 Pilot 2-attempt cycle**: paired-sync with MD writer v1.9. PDF-side prompt 主体 unchanged. N21 status: blanket all-side (PDF + MD). H_C 假说 REJECTED. R-PDF-Page-Hard NEW status (paired with R-MD-Slice-Hard). v1.8 archived `archive/v1.8_final_2026-04-29/`. NO 行为变化 PDF-side; status promotion only. |
