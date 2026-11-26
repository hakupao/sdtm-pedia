批次 S-SPEC4 (T2-post 扫描批, spec-only), attempt 1. 角色: auditor (Rule A 独立抽检)。
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。严格按 `.work/10_tier_b_repair/subagent_prompts/t2s_scan_review_audit_v1.0.md` 的 Auditor 段执行, 并读 `t2_auditor_v1.0.md` / `t2_reviewer_common_brief.md` / `t2_dispatch_notes.md` (含 T2S 段及其后主控裁定) / `evidence/checkpoints/t2_post_user_ack.md` (U1-U8)。audit_matrix 唯一路径 `.work/10_tier_b_repair/audit_matrix.md`。
spec-only 批的总体口径 (覆盖 brief 的 P 定义): P = 本批 9 域 (RS SC TU VS SUPPQUAL TE TI TS TV) PDF spec 表的全部变量行 (每变量 1 个样本单元, 以 PDF 原页为准, 不依赖 pdf_atoms) + 各域 spec 表脚注; N = min(30, max(20, ceil(0.1×|P|))), seed 20261126; 1/3 取自 writer 改动的变量 (CT `*` 17 处) 与脚注, 其余随机。每样本对渲染图核该变量全部字段 (Order/Label/Type/CT/Role/Core/CDISC Notes 逐字; CT 的 C-code 记法与 DOMAIN CT 不计, U5/U6)。
改动未提交: `git diff HEAD -- knowledge_base/domains/{RS,SC,TU,VS,SUPPQUAL,TE,TI,TS,TV}/spec.md`; 别批并行改其他文件, 只看本批。先独立判, 判完才读 `evidence/checkpoints/t2_S-SPEC4.md` 与 `t2_S-SPEC4_review.md`。
回主控 ≤ 8 行。
