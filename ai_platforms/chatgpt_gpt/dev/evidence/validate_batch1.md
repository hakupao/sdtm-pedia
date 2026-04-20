# ChatGPT GPTs 产物校验 — stage batch1

> Generated: 2026-04-20T09:38:15Z
> Script: `dev/scripts/validate_chatgpt_stage.py` (v1.1)
> Scope: V1 非空 / V2 段数 (manifest truth) / V3 P12 覆盖 (逐段) / V4 P13 注释位置 / V5 token 上限 / V6 md5 / V7 单表跨 heading

## 结果矩阵

| 文件 | batch | V1 | V2 | V3 | V4 | V5 | V7 | V6 (md5) |
|------|:-----:|:--:|:--:|:--:|:--:|:--:|:--:|:---------|
| 01_navigation.md | batch1 | PASS | PASS | PASS | PASS | PASS | PASS | md5=555d17e5ee0ae2d357b8ee2a3ba94d20 |
| 02_chapters_all.md | batch1 | PASS | PASS | PASS | PASS | PASS | PASS | md5=07a2edaf55abab8e9d08a790e6db5a8b |
| 03_model_all.md | batch1 | PASS | PASS | PASS | PASS | PASS | PASS | md5=7fcf70b5c1035a4372013c7c238ff59c |
| 04_domain_specs_all.md | batch1 | PASS | PASS | PASS | PASS | PASS | PASS | md5=7904673feeef463333a56ec8d3625af0 |

## 细节 (FAIL 诊断)

- 01_navigation.md: all PASS
- 02_chapters_all.md: all PASS
- 03_model_all.md: all PASS
- 04_domain_specs_all.md: all PASS

## 汇总

- 文件数: 4
- 全 PASS: 4/4
- FAIL: 0
