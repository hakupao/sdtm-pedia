批次 S-MOD2 (T2-post 扫描批, model), attempt 1. 角色: writer.
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。严格按 `.work/10_tier_b_repair/subagent_prompts/t2s_scan_writer_v1.0.md` 执行, 它列出的必读文件全部先读 (t2_writer_v1.0.md 规则 1-11 / t2_dispatch_notes.md 含末尾 T2S 段及其后各条主控裁定 / t1_user_ack.md (注意 R1: SDTM v2.0 表行 IE 规则) / t2_post_user_ack.md U1-U8)。批次文件 `.work/10_tier_b_repair/work/t2_batches/S-MOD2.json`。
本批只有 `model/02_observation_classes.md`, 源为 **SDTM v2.0** (`source/cdisc/SDTM_v2.0.pdf`, 页文本 `work/pdf_pages/sv20_pNNNN.txt`, 原子前缀 `sv20_`), §3.1 The General Observation Classes sv20 p11-39。目标: 对每页做 PDF↔KB 双向逐句全扫 (含变量表), 修到与 PDF 一致; 15 张 C3 UNPARSEABLE 变量表每张渲染逐格核 (先查 R1 对 v2.0 表行的 IE 口径, 按口径处理), 逐格表进 checkpoint。D6 措辞 `> KB note (not in SDTM v2.0):`。
历史: `evidence/checkpoints/t2_B-model01.md` 与 `t2_B-FA.md` (曾触碰本文件), 以及 `t2_B-model06.md` (model 类批先例)。样板: `evidence/checkpoints/t2_S-INT.md`。
文件大: 分段逐页做, 每段完成就写 checkpoint。页范围先复核 (O20)。终判以 layout + bbox + 渲染为准。有别的扫描批同时在跑, 只改本文件。
回主控 ≤ 10 行。
