批次 S-MOD3 (T2-post 扫描批, model), attempt 1. 角色: writer.
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。严格按 `.work/10_tier_b_repair/subagent_prompts/t2s_scan_writer_v1.0.md` 执行, 它列出的必读文件全部先读 (t2_writer_v1.0.md 规则 1-11 / t2_dispatch_notes.md 含末尾 T2S 段及其后各条主控裁定 —— 特别是 S-MOD2 的 model/ 通用条 (Key Notes 列 D6、Structure 残留) / t1_user_ack.md (R1: SDTM v2.0 表行/列豁免口径) / t2_post_user_ack.md U1-U8)。批次文件 `.work/10_tier_b_repair/work/t2_batches/S-MOD3.json`。
本批文件: `model/05_study_level_data.md` (§5 Study-level Data sv20 p51-63)。源为 **SDTM v2.0** (`source/cdisc/SDTM_v2.0.pdf`, 页文本 `work/pdf_pages/sv20_pNNNN.txt`, 原子前缀 `sv20_`)。目标: 对每页做 PDF↔KB 双向逐句全扫 (含变量表), 修到与 PDF 一致; 13 个 census_items 每张渲染逐格核, 逐格表进 checkpoint。D6 措辞 `> KB note (not in SDTM v2.0):`。
历史: `t2_B-model05.md` (PARTIAL 批)。先例: `evidence/checkpoints/t2_S-MOD2.md` (同类 model 扫描批, 含主控对 Key Notes / Structure 的裁定)、`t2_B-model06.md`。
分段逐页做, 每段完成就写 checkpoint。页范围先复核 (O20)。终判以 layout + bbox + 渲染为准。有别的扫描批同时在跑, 只改本批文件。
回主控 ≤ 10 行。
