# 范围外发现 (T1.4 时并入批次表)
| # | 来源 | 位置 | 问题 |
|---|---|---|---|
| O1 | T0 census | PC/assumptions.md pp.xpt; PC/examples.md; PP 表头 | 42 处 DIFF 落在 ledger 标 EXACT/EQUIV 的原子上 (整列错位, DYIDRGX_A→DY1DRGX_A, PPRFDTC→PPRFTDTC) → B-PCPP 整表逐格 |
| O2 | T1.1 | SUPPQUAL/examples.md:12-13 | AEOSP / "Clinically Medically Important SAE" / AETRTEMA; PDF p433 为 AESOSP / Other Medically Important SAE / AETRTEM |
| O3 | T1.1 | ig34_p0043_a015 | ledger 标 EQUIVALENT, KB 漏 --STRF 限制 (Q9 实证: 旧 EXACT/EQUIV 标签不可信) |
| O4 | T1.1 | spec NOT_FOUND | 变量名疑似笔误 MLGRID / CEBODYSYS / TAEFORD |
