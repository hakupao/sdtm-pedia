# T3 attempt 2 — FAIL (独立审计复审)

> 2026-11-26. 规则 B 归档.

- **输入**: attempt 1 审计必改项 1-6 + C7 (`step_T3_attempt_1.md`)
- **产物快照**: `t3_attempt_2/` (ledger md5 67931321905eeef1eeef7f212555122f); EXACT 1018 / EQUIV 92 / IE 496 / ATOM_ERR 159 / PDF_TYPO 81 / FIG 11, 残留 1
- **技术判定**: K1/K2/K4/K11/C7 落地; 独立复算全一致; valid_hits 独立实现 1018/1018 一致 (`evidence/step_T3_audit.md` §attempt 2 复审)
- **业务判定**: FAIL — 抽样 47 错 1 (p0228_a009), 全量同因 +2 (p0205_a005, p0247_a020): 应 PDF_TYPO 被标 EXACT
- **根因**: K3b — `tn_applies` 要求 PDF 侧值出现在原子里; 抽取器已改正笔误的原子 (原子=KB≠PDF) 被 live-hit 盖成 EXACT, 登记偏离漏出 T4 ack 清单
- **下一 attempt 输入**: K3b 规则 + 断言 + 全量重扫; 指针 p0354_a026 / p0285_a005; C5 p0296_a005 (NV/spec 候选); 496 条节锚无效 EXACT 进 T4 风险; C7 口径 (原子∉PDF → ATOM_ERR)
