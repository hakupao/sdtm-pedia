"""sdtm-rag chunker package.

8 chunker modules (one per KB file type). All must inherit `BaseChunker` and
produce `Chunk` instances conforming to the metadata schema in
`../../PLAN.md` §7 (mandatory fields filled with `None` when not applicable —
per F-15, Chroma null vs missing semantics differ).

Config locks from `evidence/checkpoints/phase_1a_0_sanity.md` §4:
- L-1 mermaid: 状态机 (0 嵌套, 不用 stack)
- L-2 GFM pipe-table: 简单 regex (0 HTML)
- L-3 tiktoken cl100k_base 实测强制 (char/4 偏差最大 23.6% > 20%)
- L-4 chapters/ ≥ 50KB 强制 ^### 切 (ch04 §4.4 = 9598 cl100k > 8K embedding limit)
- L-5 terminology core part: H2=1 → part 模式 / H2>1 → codelist 模式

Phase 1A.3 implementation. Phase 1A.4 测试套件 covers TA / PC / IS / DS examples
+ LB part1-4 + ch04 + supplementary_part + 边界 case (per EXECUTION_PLAN §1A.4).
"""
