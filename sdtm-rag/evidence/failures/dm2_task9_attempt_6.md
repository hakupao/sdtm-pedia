# DM2 T9 attempt 6 — Opus 补跑 5/6, 未达 §0⁗ 目标 (2026-09-25)

> 规则 B 归档。判据 §0⁗ (`da6e96c` + 跑前补注 `0b71822`); 判定 §2.6。

## 输入
- 代码 `0b71822` (规则句补示例值 / 保留语气候选 / 缺席≠不存在 + 审查修订); 仅 opus-5; 同 attempt 5 题集。
- 复跑: `.venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py --no-resume --yml test_set_domain_mapping_v1.yml,test_set_domain_mapping_v2_holdout.yml --qids dm09,dm10,dm11,dm12,dm05,dm07 --models opus-5 --out-subdir dm2_e2e_attempt6 --require-no-fallback --dossier on`

## 技术判定
- G0 PASS。

## 业务判定 — FAIL (5/6)
- dm10 中文问日文答 (语言行已正确追加, 仍漂移)。attempt 5 失败模式 (示例值自造 OID) 未复现。
- 两轮 opus 均 5/6, 失败题不同 ⇒ 低频采样尾部, 不是单一可修的规则层模式。

## 下一 attempt 输入 (待用户裁定)
- 结构性后验闸候选: 生成后确定性核验 (答案中 OID 形 token ∈ 一览; 答题语言字符计数与问句一致), 不过 → 自动重生成一次或在答案顶部显式警示。复用 `eval/prod_wirein/check_code_grounding.py` 思路。
- 或: 接受 opus ≈5/6 (主口径) 按模型恢复 auto, 并在徽章上标「研读答案须人工核对」。
- 判据余项: ④⁗「专门」定义、③⁗ 作用域、⑦ 计数口径。
