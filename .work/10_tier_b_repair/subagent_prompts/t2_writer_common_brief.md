工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。严格按 `.work/10_tier_b_repair/subagent_prompts/t2_writer_v1.0.md` 执行 (模板变量 batch_id 见上, attempt = 1)，并必读遵守 `.work/10_tier_b_repair/subagent_prompts/t2_dispatch_notes.md` 全部补充口径 (它覆盖模板中冲突处) 与 `.work/10_tier_b_repair/evidence/checkpoints/t1_user_ack.md` (R1-R4, D1-D7)。参考已完成同类批次的报告格式: `.work/10_tier_b_repair/evidence/checkpoints/t2_B-BE.md`。

通用主控授权 (本批生效):
- 除 batch json `kb_files` 外，允许改本域 `assumptions.md`，**仅限**: 补入/修正 PDF 的 `<XX> – Description/Overview` 段、spec 首句 ("xx.xpt, <Domain> — <Class>. One record per …")、以及本域节开头 (节标题与 Description 之间) 的引言 NOTE —— 全部逐字按 PDF，位置/格式照 CM / BE 先例。assumptions 列表本身若有错，记入范围外发现，不改。
- 先核本域在 PDF 中的完整节页范围 (O20: batch json 的 pdf_pages/pdf_ranges 可能不全或偏移)，在 checkpoint 写明；对完整节页范围做 PDF↔KB 双向全扫 (含表格原子)，批内发现的 PDF 叙述缺失按 R3 补。
- scratch 只用 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_<batch_id>_writer/` (替代模板第 11 条路径)。
- 多批并行: 只改本批文件；**禁止 git stash / checkout / reset / commit**；取基线用 `git show HEAD:<file>`。
- `python3 tools/check_links.py 2>&1 | grep "live docs"` 须仍为 42。evidence 里 markdown 链接写法用反引号包住。
- 有需主控裁定的事项 (超出上述授权) 写进 checkpoint "需主控定" 并停在该项，不自行扩大范围。回主控 ≤ 10 行。
- trace ts 用 `date -u +%Y-%m-%dT%H:%M:%SZ` 取真实时间, 不写占位整点 (B-RE writer 曾写 05:00Z/05:30Z).
