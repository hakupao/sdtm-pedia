批次 S-CH10 (T2-post 扫描批, chapters), attempt 1. 角色: writer.
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。严格按 `.work/10_tier_b_repair/subagent_prompts/t2s_scan_writer_v1.0.md` 执行, 它列出的必读文件全部先读 (t2_writer_v1.0.md 规则 1-11 / t2_dispatch_notes.md 含末尾 T2S 段及其后各条主控裁定 / t1_user_ack.md / t2_post_user_ack.md U1-U8)。批次文件 `.work/10_tier_b_repair/work/t2_batches/S-CH10.json`。
本批只有 `chapters/ch10_appendices.md` (§10 Appendices p444-461; 从未开批), 无 spec.md / 域 gaps。目标: 对 p444-461 每页做 PDF↔KB 双向逐句全扫 (含表格/代码字面量/列表), 修到与 PDF 一致; census_items 中 5 张 C3 UNPARSEABLE 表 (缩写表、QNAM 附录、keyword/fragment 表、域表、变更表) 每张渲染逐格核, 逐格表进 checkpoint。D6 措辞 `> KB note (not in SDTMIG):`。
历史: 无 T2 批。批次 json 的 notes 含 S-HOST / S-SPREL 转来的两项 (ch10:222 MO 句、ch10:64-69 §9 引言重复), 必须逐条处理并在 checkpoint 写明结论。样板: `evidence/checkpoints/t2_S-INT.md`。
文件大: 分段逐页做, checkpoint 逐页日志必须覆盖 p444-461 每一页; 每段完成就写 checkpoint (防中断丢失)。页范围先复核 (O20)。pdf_atoms 原子文本常有抽取噪声, 终判以 layout + bbox + 渲染为准。有别的扫描批同时在跑, 只改本文件。
回主控 ≤ 10 行。
