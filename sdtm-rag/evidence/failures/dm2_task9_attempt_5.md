# DM2 T9 attempt 5 — 新留出 + 语言修法后仍未达 §0‴ 目标 (2026-09-25)

> 规则 B 归档。判据 §0‴ (`d507936`); 判定 §2.5。

## 输入
- 代码 `28f60c7` (规则句 `7b9bdd0` + 答题语言行); `dossier:"on"`。
- 题: 新留出 dm09 IE / dm10 MH / dm11 EX / dm12 PC (盲出题, gitignored `test_set_domain_mapping_v2_holdout.yml`) + 回归 dm05 / dm07。
- 复跑: `.venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py --no-resume --yml test_set_domain_mapping_v1.yml,test_set_domain_mapping_v2_holdout.yml --qids dm09,dm10,dm11,dm12,dm05,dm07 --out-subdir dm2_e2e_attempt5 --require-no-fallback --dossier on`

## 技术判定
- G0 PASS。

## 业务判定 — FAIL (目标每模型 6/6)
- 字面: opus 5/6 (dm09 示例值 1 个错 OID), sonnet 4/6 (dm10 边缘候选 precision / dm05 称 AE 无 --CAT)。宽口径: opus 6/6, sonnet 5/6。
- 有效: 语言 12/12 (sonnet dm05 两轮同病消失); 空域分支 2/2; 泛化首次有数据。

## 下一 attempt 输入 (待用户裁定)
- opus: 唯一失败模式 = 示例值里自造 OID ⇒ 规则 (3) 已覆盖「anywhere」, 可考虑加「举例也只能用一览中的真实 OID」; 或接受 5/6 + 宽口径 6/6 恢复 opus 的 auto。
- sonnet: 失败分散 (把「上下文未见」当「标准不存在」/ 边缘候选 / precision 余量) ⇒ 暂不建议对 sonnet 恢复 auto。
- 判据: 示例值入核 / 候选三态 / 族简写口径 / 同标准域竞争 仍需写死。
