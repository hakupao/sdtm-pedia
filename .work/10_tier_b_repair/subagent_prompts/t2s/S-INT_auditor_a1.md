批次 S-INT (T2-post 扫描批), attempt 1. 角色: auditor (Rule A 独立抽检)。
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。严格按 `.work/10_tier_b_repair/subagent_prompts/t2s_scan_review_audit_v1.0.md` 的 Auditor 段执行, 并读 `t2_auditor_v1.0.md` / `t2_reviewer_common_brief.md` / `t2_dispatch_notes.md` (含 T2S 段) / `evidence/checkpoints/t2_post_user_ack.md` (U1-U8)。样板: `evidence/checkpoints/t2_S-EVT_audit.md`。
批次文件 `.work/10_tier_b_repair/work/t2_batches/S-INT.json` (AG p92-97, PR p125-128, EX p104-107, EC p107-110, §6.1.3 父节+共用例 p103-120; §6.1 引言 p92)。改动未提交: `git diff HEAD -- knowledge_base/domains/{AG,PR,EX,EC}`; 别批并行改其他文件, 只看本批。先独立判, 判完才读 `evidence/checkpoints/t2_S-INT.md` 与 `t2_S-INT_review.md`。seed 20261126。
回主控 ≤ 8 行。
