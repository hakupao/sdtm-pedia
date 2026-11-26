批次 S-SPC1 (T2-post 扫描批), attempt 1. 角色: reviewer.
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。严格按 `.work/10_tier_b_repair/subagent_prompts/t2s_scan_review_audit_v1.0.md` 的 Reviewer 段执行, 并读它引用的 `t2_reviewer_v1.0.md` / `t2_reviewer_common_brief.md` / `t2_dispatch_notes.md` (含末尾 T2S 段) / `evidence/checkpoints/t2_post_user_ack.md` (U1-U8) / `t1_user_ack.md`。样板: `evidence/checkpoints/t2_S-EVT_review.md`。
批次文件 `.work/10_tier_b_repair/work/t2_batches/S-SPC1.json`。writer 报告 `evidence/checkpoints/t2_S-SPC1.md` + `work/t2_batches/S-SPC1.writer.jsonl`。改动未提交: `git diff HEAD -- knowledge_base/domains/{CP,GF,IS,LB}`。另有扫描批 S-INT/S-SPC2/S-FND 同时改别的文件, 只看本批 (p255 fp 回归属 S-SPC2)。
重点: 独立双向全扫 CP/GF/IS/LB (pdf_atoms 本段错多, 以 layout+bbox+渲染为准); 各 gaps; GF 脚注 MOVED; CT `*` 7 格 + CP 无 `*` 的确认; 词级修正 4 处; IS "Examples Notes" 22 行 D2 去重 (逐条核 examples.md 确有副本); CP 新 PDF_TYPO T-16..T-21 依据 (主控已裁: T-21 正确值可由 PDF spec 表自身确定 → KB 写正确值, 核依据是否成立); census_items 8 张渲染逐格。
回主控 ≤ 10 行。
