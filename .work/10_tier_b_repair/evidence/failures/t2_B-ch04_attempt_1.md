# B-ch04 attempt 1 归档 (规则 B)

- 输入: base HEAD `6fea5638720e4505be6263ec440953cb8d13fe3b`; ch04 md5 `ebd6a616cec349a4cf30c3c0848b6b72`; work/t2_batches/B-ch04.json (29 atoms + 4 recheck, census DIFF 6, O3/O12); 主控续裁 1-5 和 D6.
- 产物: `t2_B-ch04_attempt_1.patch` (= attempt 1 + 续 + 续 2 对 base 的 git diff; ch04 md5 `0df37d796ad96eca4723f5382100dcc1`, +104/−50); checkpoint t2_B-ch04.md §attempt 1 / 续 / 续 2; writer.jsonl 前 64 行.
- 技术判定 (reviewer, t2_B-ch04_review.md): CONDITIONAL. atoms/recheck 全部逐字落地, census 只剩 DIFF 1 (T-1), fp 回归 0, live docs 42.
- 业务判定: 未过. 有 2 类未执行: (a) R2 插入后旧改写句/冗余 KB note 没按 D2 删 (C1-C5); (b) 本批已改段落中 R3 丢的短语没补 (C6-C10).
- 下一 attempt 输入: 不回滚, 在 md5 0df37d79… 基础上做 C1-C5 删除 (每处 fp 复跑) + C6-C10 逐字补; T-2 的 T4 登记补 reviewer 参考说明; 主控裁定这些都在本批做完, 不交 T3.
