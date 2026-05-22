# Phase A.A5 — 4 Reviewer Subagent Prompts (留底)

> 4 个 background reviewer subagents fire 2026-05-20 PM post writer completion
> Rule D: writer subagent_type = `oh-my-claudecode:executor`; reviewers = 4 different subagent_type (writer ≠ reviewer strict)
> Slot mapping:
> - A5.1 Gemini v9 → `pr-review-toolkit:code-reviewer` (slot #22)
> - A5.2 ChatGPT v3 → `oh-my-claudecode:scientist` (slot #23)
> - A5.3 Claude v3 → `oh-my-claudecode:critic` (slot #24)
> - A5.4 NotebookLM v3 → `oh-my-claudecode:verifier` (slot #25)

详细 prompts 见各 fire call inline. 此文件作为 留底 audit trail per Tier 3 ceremony.

Common N=5 spot-check sample questions (mental trace, no Chrome MCP):
- Q1: "BECAT 是 sponsor-extensible 吗?" (v1.3 A2 BECAT EXTRACTION 验; R1 KB-grounding + R5 premise correction)
- Q2: "PP RELREC Method A 是哪种 1-to-many 关系?" (v1.3 Q-S2 method label drift; R3 method label anchor for ChatGPT, R1 KB-grounding for others)
- Q3: "HIV Ag/Ab combo 测试 → IS 还是 MB?" (v8.1 H1 reviewer fix; R3 IS scope shift regex trigger)
- Q4: "麻疹 IgG → 哪个 domain?" (v8.1 CO-1e IS scope shift; R3 IS scope shift regex)
- Q5: "AESEV 是 Required 吗?" (default KB-grounding 验; R1 + R2 AHP regex `^[A-Z]{2,5}[A-Z0-9]{0,12}$` fire → KB double-check)

Special tasks:
- **A5.1 Gemini**: 评估 282L vs 240L upper band borderline. Writer 解释 reasonable? 若 NOT, condense suggestion specific.
- **A5.2 ChatGPT**: 验 Method label anchor 4 mappings vs KB `knowledge_base/domains/PP/examples.md` §6.3.5.9.3 (A=Many-Many / B=One-Many / C=Many-One / D=One-One byte-exact).
- **A5.3 Claude**: 验 prompt 不重复 A3.1 pipeline fix 内容; 7-file KB structure 一致 with `dev/scripts/build_v2_stage.py` actual output.
- **A5.4 NotebookLM**: 验 footer Sources citation style byte-byte preserved (not just rephrased) vs v1.3 LIVE.

Output: `evidence/checkpoints/a5_<platform>_reviewer_audit.md`
Verdict: PASS / PASS_WITH_OBSERVATIONS / NEEDS_REVISION
