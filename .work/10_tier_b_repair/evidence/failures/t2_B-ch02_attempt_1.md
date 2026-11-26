# B-ch02 attempt 1 失败归档 (规则 B)

- 输入: work/t2_batches/B-ch02.json + 主控裁定 (续2); base HEAD 553b14b.
- 产物: `t2_B-ch02_attempt_1.patch` (ch02 vs 553b14b, attempt 1 + 续 + 续2 终态, md5 d5f9f9b1888b2e304e3104a3cf6cfa5e).
- 技术判定: fp p11-16 回归 0, live docs 42; reviewer 签字.
- 业务判定 (auditor, evidence/checkpoints/t2_B-ch02_audit.md): **FAIL** — F1 ch02:203 KB 自写小标题 "(not fully evaluated for human clinical trials)" 与 PDF p15/p16 "have not (yet) been evaluated" 改义 (基线已有, 本批未动). 非阻断 O1: §1 内容复制自 ch01 所属节, 与 D2 去重口径有张力.
- 下一 attempt 输入: F1 小标题括号改 PDF 措辞; 主控更正续2 #4-6 → §1 摘录整块改一行交叉引用到 ch01 (完整内容由 B-ch01 保证).
