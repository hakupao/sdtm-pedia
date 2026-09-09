# C2R V3 attempt 1 — T6 未触发 (2026-09-09)

**输入**: 预登记 T6 (纯画面布局题, 点名 TME 表单; 真值题面见 gitignored `data/study/st01/eval/runs/c2r_v3/INDEX.md`), flag ON, 两模型。

**产物**: `data/study/st01/eval/runs/c2r_v3/B_*_T6.json` — `pdf_trigger=null`, `pdf_pages=null`; 两臂 prompt_tokens 逐位相同 (GPT 22,161 / Opus 28,549), 证明确实零附图, 不是附了没报。

**技术判定**: T6 无 R1/R2 词, 只能走 R3; R3 的相关性下限 (复审 M10, 预登记修订 r2) 要求 via_lookup 卡片或 `strong_hit`; T6 两者皆无 (`server/pdf_trigger.py` R3 分支返回 no-fire, 零 LLM 探针复现)。同一条下限正是让 N5 通过的那条。

**业务判定**: 预登记里 T6 是应触发题, 属真失败。根因是 r2 修订的下限口径过窄: 「问题显式点名了本研究的表单」在业务上就是相关性证据, 但 strong_hit 通道不覆盖表单名。

**下一 attempt 输入 (修订 r3, pattern 级, 非按例加词)**: R3 下限扩为三选一 — via_lookup 卡片 / strong_hit / `StudyLookup.resolve(question).form_scopes` 非空 (问题点名了表单)。N5 不点名任何 study 表单, 仍不触发 (测试钉死)。判分点不改。仅重跑 T6 (两臂 × 两模型 = 4 次调用)。

**attempt 1.5 (r3 字面实现)**: 三选一落地后 T6 仍不触发 — `form_scopes` 只由别名表填充 (生产 1 条), 不读 catalog 表单名。技术判定: r3 口径写错了数据源。修正为 r3b (从页索引 `names.forms` 判表单点名), 见预登记。

**attempt 2 (r3b) 结果**: T6 两模型均触发 R3 (6 页, prompt +10,077 / +7,950 token ≈ 1.3-1.7k/页); 判分交独立 Reviewer 补入 `evidence/step_c2r_v3_audit.md`。T1-T5 与 N 组未重跑 (r3b 仅放宽 R3 下限; T1-T5 走 R1/R2; N5 零 LLM 探针复核不触发)。
