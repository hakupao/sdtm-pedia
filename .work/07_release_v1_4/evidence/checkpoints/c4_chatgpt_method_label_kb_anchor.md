# C4 — ChatGPT Method label KB anchor in PP/examples.md (2026-05-22)

> **Phase**: C
> **Task**: Task #6
> **Type**: KB edit (1 段 mapping table add)

## 1. Change

`knowledge_base/domains/PP/examples.md` §6.3.5.9.3 RELREC Method Quick Reference 段:

**Added** 在 introduction 段后, Method A 节前, 1 个新 H3 subsection `### Method label mapping (anti-drift anchor)` 含:

| Method | Cardinality | PC-side IDVAR | PP-side IDVAR |
|--------|-------------|---------------|---------------|
| **A** | Many-to-Many | `PCGRPID` | `PPGRPID` |
| **B** | One-to-Many | `PCSEQ` | `PPGRPID` |
| **C** | Many-to-One | `PCGRPID` | `PPSEQ` |
| **D** | One-to-One | `PCSEQ` | `PPSEQ` |

+ 1 段说明 "These four pairs are the canonical mappings from SDTMIG v3.4 §6.3.5.9.3. When answering Method-label questions, cite this table directly — do not infer labels from cardinality alone."

## 2. Source verification

KB 原文 §6.3.5.9.3 已有 4 个 H3 小节 (line 133/140/147/169):
- Method A — Many to Many, Using **PCGRPID and PPGRPID** (p277) ✓
- Method B — One to Many, Using **PCSEQ and PPGRPID** (pp 277-278) ✓
- Method C — Many to One, Using **PCGRPID and PPSEQ** (p278) ✓
- Method D — One to One, Using **PCSEQ and PPSEQ** (pp 278-280) ✓

**Mapping table 内容与原 H3 节头 byte-aligned**, 不引入新事实, 仅提升可检索性 / cross-reference anchor.

## 3. Why this anchor

v1.3 Phase C Q-S2 finding: ChatGPT GPT 答 PP RELREC Method 时出现 label drift (4 IDVAR 组合正确但 A/B/C/D 标签错位). v1.4 双层 anchor:
- **Prompt 层 (A2, done)**: ChatGPT v3 system_prompt L78 `Method A = Many-to-Many | Method B = One-to-Many | Method C = Many-to-One | Method D = One-to-One`
- **KB 层 (C4, this)**: PP/examples.md §6.3.5.9.3 mapping table — 让 4 平台 bundle rebuild 后都看到 KB 内的显式 mapping (不依赖各平台 prompt 单独锚)

## 4. Impact

- **触发 3 平台 bundle rebuild** (Task #7): ChatGPT (PP/examples 在 04_examples_data.md) + Claude (在 bundle 09 examples_data_high) + NotebookLM (在 bucket 16 PP/PC)
- **Gemini 不 rebuild** (ABANDONED per c0_gemini_drop_ack.md)
- 触发 Q-S2 三平台 sanity 复测 (Task #8) 验不 regression

## 5. Byte delta

`knowledge_base/domains/PP/examples.md`: +13 行 (1 H3 header + 1 spacer + 6 table 行 + 1 spacer + 2 段说明 + 2 spacer)

## 6. Next

- Task #6 → completed
- Task #7 (3 平台 rebuild) → ready to start (待 C1/C2 完成或并行 — 不互相阻塞)
- Task #8 (Q-S2 sanity 复测) → blocked by #7
