# Gemini Gems v2.0 C 方案校验报告

> Generated: 2026-04-21T10:26:35Z
> Stages validated: navigation, spec_plus_assumptions, examples_only, business_scenarios
> Total tokens: 637,648 (target ~820,000)

## 校验矩阵

| file | exists | bytes | tokens | target | segments | V1 | V2 | V4 | V8 | md5 (head12) |
|------|:------:|------:|-------:|-------:|---------:|:--:|:--:|:--:|:--:|--------------|
| 01_navigation_and_quick_reference.md | Y | 476,877 | 124,515 | 150,000 | 15 | PASS | PASS | PASS | - | ee199795281d |
| 02_domains_spec_and_assumptions.md | Y | 919,567 | 240,453 | 400,000 | 126 | PASS | PASS | PASS | - | 57a00f3bc239 |
| 03_domains_examples.md | Y | 664,912 | 220,657 | 280,000 | 63 | PASS | PASS | PASS | - | 8c8ae684b7d4 |
| 04_business_scenarios_and_cross_domain.md | Y | 136,914 | 52,023 | 60,000 | 1 | PASS | PASS | PASS | PASS | 765446fc8545 |

## V3 累计 token 判定

- Total: **637,648** tokens
- Target (C 方案): ~820,000
- Warn threshold: >900,000
- Hard threshold (1M 窗口): >1,000,000

- **V3 PASS**: total 637,648 ≤ warn 阈.

## 备注 (逐文件)

### 04_business_scenarios_and_cross_domain.md
- V2 INFO: 1 segments (writer-authored, no KB source required)
- V8a PASS: size 136,914 > 10,000
- V8b PASS: inline codelist lines matched 0 (<5)

## 判定

- rc=0 (PASS)
