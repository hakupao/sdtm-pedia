# B-ch04 attempt 2 归档 (规则 B)

- 输入: attempt 1 终态 (md5 0df37d79…) + reviewer CONDITIONAL C1-C10 + 主控裁定 (全部在本批做) + reviewer a2 PASS 后的可选项 (三行 "Example when … checked:").
- 产物: `t2_B-ch04_attempt_2.patch` (= `git diff 6fea563 -- ch04`, 336 行; ch04 md5 `545883c16b8d4f3e161f3176df3c517a`, +111/−63); checkpoint §attempt 2 / attempt 2 续.
- 技术判定: reviewer a2 PASS; auditor (t2_B-ch04_audit.md) seeded 样本 0/10 错, fp 回归 0, live docs 42.
- 业务判定: FAIL. auditor 全扫发现 R2 丢失 3 处: F1 ch04:865 缺 "(see Section 7.3.1, Trial Visits)"; F2 ch04:1349 缺原因从句 "because they represent multiple values for a single variable" (实质语义丢失); F3 ch04:1328 缺 URL. 根因: writer / reviewer 只查了 atoms 和本批改过的行; ledger 标为 EQUIVALENT/EXACT、没进 T1 分诊的原子没人逐句对 PDF.
- 下一 attempt 输入: 不回滚, 在 md5 545883c1… 基础上补 F1-F3; 并对 p22-59 每个 PDF 原子 (SENTENCE / LIST_ITEM / HEADING / CROSS_REF / NOTE, 共 839 条) 与 ch04 做规范化子串比对, 不命中的逐条对 PDF 原页定性, 同类丢失一并补齐.
