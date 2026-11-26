批次 S-CH4 (T2-post 扫描批, chapters), attempt 1. 角色: writer.
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。严格按 `.work/10_tier_b_repair/subagent_prompts/t2s_scan_writer_v1.0.md` 执行, 它列出的必读文件全部先读 (t2_writer_v1.0.md 规则 1-11 / t2_dispatch_notes.md 含末尾 T2S 段及其后各条主控裁定 / t1_user_ack.md / t2_post_user_ack.md U1-U8)。批次文件 `.work/10_tier_b_repair/work/t2_batches/S-CH4.json`。
本批只有 `chapters/ch04_general_assumptions.md` (§4 p22-59, ~1500 行), 无 spec.md / 域 gaps。目标: 对 p22-59 每页做 PDF↔KB 双向逐句全扫 (含表格/代码字面量/列表), 修到与 PDF 一致; census_items 中 23 张 C3 UNPARSEABLE 表 (CRF 示意、ae/suppae 例、日期精度表、--PRESP/--OCCUR 情况表等) 每张渲染逐格核, 逐格表进 checkpoint。D6 措辞 `> KB note (not in SDTMIG):`。
历史: `evidence/checkpoints/t2_B-ch04.md` + `t2_B-ch04_review*.md` + `t2_B-ch04_audit*.md` (B-ch04 auditor 曾 FAIL 后修; 其 PDF_TYPO / T-n / D6 登记继续有效, 复核后沿用编号)。样板: `evidence/checkpoints/t2_S-INT.md`。
文件大: 按 §4.1-§4.5 分段逐页做, checkpoint 逐页日志必须覆盖 p22-59 每一页; 每段完成就写 checkpoint (防中断丢失)。页范围先复核 (O20)。pdf_atoms 原子文本常有抽取噪声, 终判以 layout + bbox + 渲染为准。有别的扫描批同时在跑, 只改本文件。
回主控 ≤ 10 行。
