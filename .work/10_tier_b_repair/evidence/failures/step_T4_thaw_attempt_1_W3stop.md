# T4 解冻轮 W3 第一次停止 (中间失败) 指针

<!-- chain: E (plans) -->
> 状态: 中间失败, 已由主控决定后在同一 writer 续跑解决 (2026-11-27). 规则 B 索引, 正文不复制.

- **输入**: 解冻后 KB (W1+W2, 工作树); 规格 `subagent_prompts/t4/t4_thaw_spec_v1.0.md` §3.
- **产物**: `evidence/checkpoints/t4_thaw_W3.md` §1-§5 (第一次停止时的全部记录, 原样保留); 当时 ledger md5 `da4eb100…` (两遍一致).
- **技术判定**: FAIL — `s0_classify` NEW 27; `t3_direct_hit` RED (unexplained 2: p0419_a011/a013); t3_mutation 基线 RED, M3 失效 (CRF 改后模式 0 替换).
- **业务判定**: 未产出错误标签; 失败原因 = U-7 改正确值后 16 个原子旧标签失效而 K3b 规则挂不上 (描述型 pdf_value / <3 字符差异 / registry 页号错 / 规则 (a)).
- **下一 attempt 输入**: 主控五项决定 (`t4_thaw_W3.md` "attempt 1 续" 节开头; `t4_user_decisions.md` §000b M-3..M-7) → 续跑结果 ledger `60729f7b…`, s0 NEW 0, direct_hit GREEN.
