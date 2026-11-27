# T4.1 总闸 attempt 3 — 不通过 (CONDITIONAL) 指针

<!-- chain: E (plans) -->
> 状态: CONDITIONAL, 等主人回答问题 A (2026-11-27). 本文件只做规则 B 的索引, 正文不复制.

- **输入**: HEAD `4a5dd1d` (KB 树 `63f857774a42cfaa71798705ad40ab51bc5e378a`; 台账 md5 `16024ac09721cb3f8519cd68fa455196`, R2L 78 条改标之后); brief `subagent_prompts/t4_gate_reviewer_v3.0.md`; 预跑日志 `work/t4/gate_prerun.log` (在 `a88a585` 上跑); 主人原话 `evidence/checkpoints/t4_owner_confirmation.md` (两节); 裁定表 `evidence/checkpoints/t4_user_decisions.md` §000 / §000b / §000c.
- **产物**: 审查者报告原文 `evidence/t4_gate_raw/attempt3_report.md`; 誊录 `evidence/checkpoints/t4_gate_review.md` §attempt 3.
- **技术判定**: G-TB1-9 无 NOT_MET (MET 4: G-TB2 / 6 / 7 / 8; MET_WITH_CONDITION 5: G-TB1 / 3 / 4 / 5 / 9); 审查者自挑 10 条改标 10 / 10 HOLDS; 78 条改标与总闸样本 84 / T4.2 预筛 42 / 主人抽查 6 的交集 0; 裁定来源三问都判 "足够" (带已公开的局限); attempt 2 的缺口除 "ATOM_ERR / PDF_TYPO 补抽" 判部分关外都判已关.
- **业务判定**: 不能 PASS — 第三轮已查出的 4 条多标 PDF_TYPO (`ig34_p0412_a006` / `a007` / `a008`、`ig34_p0413_a010`) 仍在台账里, 审查者复核为 NOT_HOLD (应为 EXACT); 按写死的口径 "任一样本 NOT_HOLD → 不 PASS". 主人被问过一次 (问题 A), 回的是「继续」, 没有选; 主控没有替他定. 不挡闸但要主人表态: M-9 追认、问题 B (`ig34_p0293_a038`).
- **下一 attempt 输入**: 主人对问题 A 的选择. A1 (改回 EXACT): writer `oh-my-claudecode:executor` 按 `work/t4/supp/relabel_pending.json` 的 `typo-overlabel` 组改 4 条 (预演数字: U-1 B 不变 99.2651%, strict 9493/9933 = 95.5703%; `work/t4/supp/scenarios.json` 最后一项) → reviewer `oh-my-claudecode:code-reviewer` 复跑逐行核 → 改 `scripts/t4/t4_supp_report.py` 的 `DECIDED` / `NOT_APPLIED` 断言并重生成 → `t0_mutation_head.sh --make-baseline` + 变异 → `t4_gate_prerun.sh` → 对这一处做 delta 闸审. A2 (维持): 需主人说明理由, 再送闸审判断这 4 条能否作为已知例外.
- **结局 (2026-11-27 夜, 追加; 上文不改)**: 主人直接回答 「A1、B1、追认 M-9」 → R3L 批 (提交 `d794fb6`) 把 4 条改回 EXACT, reviewer PASS; delta 闸审结果见 `evidence/checkpoints/t4_gate_review.md` "§attempt 3 delta".
