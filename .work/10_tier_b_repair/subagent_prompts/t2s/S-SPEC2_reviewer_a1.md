批次 S-SPEC2 (T2-post 扫描批, spec-only), attempt 1. 角色: reviewer.
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。严格按 `.work/10_tier_b_repair/subagent_prompts/t2s_scan_review_audit_v1.0.md` 的 Reviewer 段执行, 并读它引用的 `t2_reviewer_v1.0.md` / `t2_reviewer_common_brief.md` / `t2_dispatch_notes.md` (含末尾 T2S 段及其后主控裁定) / `evidence/checkpoints/t2_post_user_ack.md` (U1-U8) / `t1_user_ack.md`。
批次文件 `.work/10_tier_b_repair/work/t2_batches/S-SPEC2.json` (CE HO MH DV DA DD IE BS 共 8 个 spec.md; writer 复核页范围见报告)。writer 报告 `evidence/checkpoints/t2_S-SPEC2.md` + `work/t2_batches/S-SPEC2.writer.jsonl`。改动未提交: `git diff HEAD -- knowledge_base/domains/{CE,HO,MH,DV,DA,DD,IE,BS}/spec.md` (应只有 CT `*` 20 处 + 脚注 8 处)。另有扫描批同时改别的文件, 只看本批。
重点: 独立逐变量逐字段核 8 域 195 变量 (Order/Label/Type/Role/Core/CDISC Notes 逐字, R2 口径) —— 不得只用 writer 的 sc2.py (同源); 自己写列解析或用 layout + 渲染; 每域 "PDF 变量数 = KB 变量数 + 顺序" 计数闸; CT `*` 逐变量对渲染 (含 PDF 无 `*` 的域确认); 8 处脚注逐字 + U7 位置; BS 只从 p196 第 31 行后算 (前半页 §6.3.5.1 通用表)。U5/U6 不在本批。
回主控 ≤ 10 行。
