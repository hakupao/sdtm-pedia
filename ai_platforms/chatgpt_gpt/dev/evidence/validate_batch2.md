# ChatGPT GPTs 产物校验 — stage batch2

> Generated: 2026-04-21T05:53:47Z
> Script: `dev/scripts/validate_chatgpt_stage.py` (v1.5)
> Scope: V1 非空 / V2 段数 (manifest truth) / V3 P12 覆盖 (逐段) / V4 P13 注释位置 / V5 token 上限 / V6 md5 / V7 单表跨 heading

## 结果矩阵

| 文件 | batch | V1 | V2 | V3 | V4 | V5 | V7 | V6 (md5) |
|------|:-----:|:--:|:--:|:--:|:--:|:--:|:--:|:---------|
| 05_domain_assumptions_all.md | batch2 | PASS | PASS | PASS | PASS | PASS | PASS | md5=79b1069c7424d3c3edad630be14e653d |
| 06_domain_examples_all.md | batch2 | PASS | PASS | PASS | PASS | PASS | PASS | md5=04bc0a05ef072ede1b7df1b487ec7485 |
| 07_terminology_core_high_freq.md | batch2 | PASS | PASS | PASS | PASS | PASS | PASS | md5=951b6d6ce541c24f95bd565c921d5644 |
| 08_terminology_quest_and_supp.md | batch2 | PASS | PASS | PASS | PASS | PASS | PASS | md5=0c0bf135146215515a49227b76b3c925 |
| 09_terminology_core_mid_tail.md | batch2 | PASS | PASS | PASS | PASS | PASS | PASS | md5=efca218aaf6ad17980de323735d45e67 |

## 细节 (FAIL 诊断)

- 05_domain_assumptions_all.md: all PASS
- 06_domain_examples_all.md: all PASS
- 07_terminology_core_high_freq.md: all PASS
- 08_terminology_quest_and_supp.md: all PASS
- 09_terminology_core_mid_tail.md: all PASS

## 汇总

- 文件数: 5
- 全 PASS: 5/5
- FAIL: 0
