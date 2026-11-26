# T2 reviewer / auditor 共用 brief (主控 2026-11-26)
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。
- reviewer: 严格按 `.work/10_tier_b_repair/subagent_prompts/t2_reviewer_v1.0.md`; auditor: 严格按 `t2_auditor_v1.0.md`。两者都必读遵守 `t2_dispatch_notes.md` 全部口径 (双向全扫含表格原子、渲染图逐格核、不截断输出、D6 逐条确认)。
- `{{base_commit}}` = `HEAD` (本批改动未提交, `git diff HEAD -- <本批文件>`), auditor `{{seed}}` = `20261126`。
- writer 授权范围见 `t2_writer_common_brief.md` (assumptions.md 仅 Description/Overview、spec 首句、节引言 NOTE、PDF 原有小标题); 核授权范围外无改动。
- 先读 writer 报告 `evidence/checkpoints/t2_<batch>.md` 了解改动 (auditor: 先独立判再对照)。抽样 / 全扫页范围 = 本域完整 PDF 节页范围 (writer 报告中已核), 不只 batch json 的 pdf_pages; auditor 的 P 中 kb_files 含本批实际改动的全部文件。
- PDF_TYPO 每条核依据 (PDF 自身可定 → KB 写正确值; 不可定 → 照录 + T4)。
- fp_match 全局 RED 中他批页码的回归不计本批; 只看本批页码/文件。
- 工作树可能同时有别批未提交改动, 只看本批文件。
- scratch 只用 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_<batch>_<role>/`。只读 KB; 禁止 git stash/checkout/reset/commit。evidence 里 markdown 链接用反引号包住 (不嵌套)。trace ts 用 `date -u` 真实时间。
- 输出: reviewer → `evidence/checkpoints/t2_<batch>_review.md` + trace 一行; auditor → `t2_<batch>_audit.md` + `audit_matrix.md` 追加一行 (格式照已有 T2 行) + trace 一行。`python3 tools/check_links.py 2>&1 | grep "live docs"` 记录 (基线 42)。回主控 ≤ 10 行。
