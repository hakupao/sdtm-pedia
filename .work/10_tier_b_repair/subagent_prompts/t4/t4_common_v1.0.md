# T4 attempt 2 前置核查 — 共用背景 v1.0
<!-- chain: E (plans) -->
- 仓库 `/Volumes/DevSSD/Project/sdtm-pedia`. 产品 `knowledge_base/` (KB, 英文 Markdown), 由 CDISC PDF 抽取. 本项目 (10 旁枝 Tier B, 目录 `.work/10_tier_b_repair/`) 修补 KB 与 PDF 的差异, 并给每个 PDF 原子一个终态标签 (ledger `work/coverage_ledger.wc.jsonl`).
- **KB 当前冻结**: 你不得修改 `knowledge_base/`、ledger、registry、任何既有文件, 不 commit. 只允许写 brief 指定的那一个输出文件.
- PDF 文本层: `.work/10_tier_b_repair/work/pdf_pages/ig34_pNNNN.txt` (SDTMIG v3.4) / `sv20_pNNNN.txt` (SDTM v2.0), `pdftotext -layout`, 页号 = PDF 物理页. 原 PDF: `source/cdisc/SDTMIG v3.4 (no header footer).pdf` / `source/cdisc/SDTM_v2.0.pdf`; 用 Read 工具带 `pages` 参数看渲染页 (同页号). 表格列对齐、字形 (引号/破折号/勾选符) 有疑问以渲染页为准. 词级坐标: `work/pdf_bbox/ig34_pNNNN.tsv`.
- 终态标签定义见 `.work/10_tier_b_repair/subagent_prompts/t4_gate_reviewer_v1.0.md` "背景" 节.
- PDF 笔误登记: `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` (按 id 查; handling = "KB 写正确值" / "照录").
- 规则 D: 你是独立审查者, 与写者、各批 auditor、总闸审查者都不是同一 agent. 用户质量标准接近 100%. 拿不准就写 "看不出" 并说明缺什么, 不要因为 "看起来大概对" 就判成立.
- 输出用中文; 每条必须给可复核依据 (文件:行 / 渲染页号). 引 PDF 原文每处 ≤ 25 词.
