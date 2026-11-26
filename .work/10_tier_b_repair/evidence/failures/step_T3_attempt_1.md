# T3 attempt 1 — FAIL (独立审计)

> 2026-11-26. 规则 B 归档, 不删.

- **输入**: brief `subagent_prompts/t3_writer_v1.0.md` + 主控裁定 C1-C6 (`evidence/checkpoints/t3_recompute.md` §主控裁定)
- **产物快照**: `t3_attempt_1/` (ledger md5 634aedcfeccd820ee182a930ec39352c, decisions, errata; gzip)
  计数 EXACT 1000 / EQUIV 48 / IE 490 / ATOM_ERR 159 / PDF_TYPO 55 / FIG 11, 残留 46
- **技术判定**: 计数/允许集/逐字节/变异/live docs 全部复现一致 (`evidence/step_T3_audit.md`)
- **业务判定**: FAIL — 抽样 69 条错 2 (p0206_a009 应 PDF_TYPO; p0295_a020 C5 错位 EXACT), 全量另 7 条终态错 (E1 假 EXACT p0153_a0019; E2 NV p0294_a017/18/20 错位 EXACT; E4 p0334_a011/p0338_a006 应 PDF_TYPO)
- **根因**: K1 EXACT 候选取节 target 首个命中, 无词边界; K2 direct_hit 只复核自记命中文件 (自证, 假绿已复现); K3 T-n 只取 note 不取 ref; K4 R1 未核原子∉PDF; K11 短 verbatim 不计次数
- **下一 attempt 输入**: 审计必改项 1-6 + 主控裁定 C7 (三批 delta 复审 PASS, `t3_delta_rereview.md` → 45 残留与 K7 8 条 PDF_TYPO 均接受)
