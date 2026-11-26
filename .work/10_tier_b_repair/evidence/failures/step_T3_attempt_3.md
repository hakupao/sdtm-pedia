# T3 attempt 3 — FAIL (独立审计复审)

> 2026-11-26. 规则 B 归档.

- **输入**: attempt 2 必改项 (K3b / 指针 / C5 / C7 口径 / 风险登记)
- **产物快照**: `t3_attempt_3/` (ledger md5 63cd2d8666c209db18ef8eca5e840418); EXACT 1016 / EQUIV 54 / IE 494 / ATOM_ERR 197 / PDF_TYPO 116 / FIG 11, 残留 1
- **技术判定**: 必改项全落地; 复算/变异/独立匹配器一致; 抽样 52/52 (`evidence/step_T3_audit.md` §attempt 3 复审)
- **业务判定**: FAIL — 全量交叉扫描: §5.0 范围内 stock 标签 4 条登记偏离仍为 EXACT/EQUIV (p0018_a012, p0018_a036, p0213_a009, p0132_a014); 2 条待人工 (p0068_a010, p0142_a015)
- **根因**: K3b 触及规则只扫允许集 / TB 行, 未覆盖 §5.0 内 stock 标签; 表格格 n-gram 语境偏严
- **下一 attempt 输入**: 6 条并入允许集; K3b 断言扩到 §5.0 内全部 EXACT/EQUIV; 复审只核改动层
