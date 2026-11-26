批次 S-EVT (T2-post 扫描批试点), attempt 1. 角色: auditor (Rule A 独立抽检)。
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。严格按 `.work/10_tier_b_repair/subagent_prompts/t2s_scan_review_audit_v1.0.md` 的 Auditor 段执行, 并读 `t2_auditor_v1.0.md` / `t2_reviewer_common_brief.md` / `t2_dispatch_notes.md` (含 T2S 段) / `evidence/checkpoints/t2_post_user_ack.md` (U1-U8)。
批次文件 `.work/10_tier_b_repair/work/t2_batches/S-EVT.json` (AE p133-142, DS p155-167, §6.2 引言 p133)。改动未提交: `git diff HEAD -- knowledge_base/domains/AE knowledge_base/domains/DS`。先独立判, 判完才读 `evidence/checkpoints/t2_S-EVT.md` 与 `t2_S-EVT_review.md`。seed 20261126。
回主控 ≤ 8 行。
