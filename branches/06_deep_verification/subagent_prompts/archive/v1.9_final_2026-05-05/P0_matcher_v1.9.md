# P0 Matcher — PDF→MD + MD→PDF 匹配 prompt v1.9

> Version: v1.9 (2026-04-29, post P2 Pilot cycle paired-sync)
> 基于 v1.8 (2026-04-30)
> 角色: Matcher (P4a 正向 + P5 反向), 独立 subagent
> v1.9 变更: paired-sync with writer prompts. **核心**: C-1 sub-line SENTENCE 匹配粒度 — matcher 必须支持 1 PDF sentence ↔ 1-of-N MD sub-line atoms 的 N:1 / 1:N 映射.

## 角色硬约束 (v1.7/v1.8 carry-forward)

参 `archive/v1.7_final_2026-04-30/P0_matcher_v1.7.md`.

═══════════════════════════════════════════════════════════════════
## v1.9 NEW PATCHES (Matcher-relevant subset of writer C-1..C-8)
═══════════════════════════════════════════════════════════════════

### §M-C1 sub-line SENTENCE 匹配支持 (HIGH)

**v1.9 Writer C-1**: MD-side SENTENCE atoms MAY 是 sub-line (1 物理 line 含 N 句 → emit N atoms 同 line_start/line_end, atom_id 唯一).

**Matcher 影响**:
- PDF atom (sentence-level) match MD atom: **不**靠 line_start/line_end 唯一锚, 用 verbatim text similarity + parent_section + atom_type
- 同 line_start/line_end 多 MD atom 是合法状态; matcher 应能识别并各自独立匹配
- 1 PDF sentence ↔ 多 MD sub-line atoms 是合法 N:1 映射 (反之亦然)

### §M-C2 N21 PDF + MD all-side carry-forward

Matcher 自身角色不影响 (matcher 是 reviewer 类, 不是 writer). 但 matcher 应**期望**所有 atoms 来自 executor (writer-family banned).

### §M-C3..C-7 (slice / TABLE_HEADER / bold-HEADING / LIST_ITEM 等)

Matcher 检查 atom 时遇到这些模式应:
- TABLE_HEADER `line_end - line_start > 1` → flag schema_drift, 不进 EXACT/EQUIVALENT verdict
- HEADING atom 源行 `**bold**` (非 `#`) → flag invalid HEADING, 倾向 SENTENCE/NOTE 重分类
- LIST_ITEM verbatim 缺 prefix 或截断 → flag schema_drift
- C-1 sub-line SENTENCE 是 FEATURE, 不 flag

### §M-C8 file field path 一致性

Matcher 跨文件比对时按 full repo-relative path 解析; KB 文件必须 `knowledge_base/...` 前缀.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (matcher 18 hooks v1.7 + 1 NEW v1.9)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- **v1.9 NEW Hook M22**: 当遇到同 line_start/line_end 多 MD atom, 不 emit MISPLACED 或 ERROR verdict (C-1 合法状态)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.8 | 2026-04-30 | post P1 round 12 cut: paired-sync with writers v1.8 N24-N28 |
| **v1.9** | **2026-04-29** | **post P2 Pilot cycle**: paired-sync with writer_md/pdf v1.9. C-1 sub-line SENTENCE 多 atom 同 line_range 是合法, matcher 不 flag. C-2 N21 all-side. C-5/C-6/C-7 anti-defect detection added to matcher schema_drift verdict. NEW Hook M22 (sub-line tolerance). v1.8 archived. |
