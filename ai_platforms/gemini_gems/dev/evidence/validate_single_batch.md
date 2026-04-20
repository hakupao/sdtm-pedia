# Gemini Gems 单批校验报告

> Generated: 2026-04-20T09:39:00Z
> Stages validated: core, spec, knowledge, terminology
> Total tokens: 884,918 (target ≤800,000)

## 校验矩阵

| file | exists | bytes | tokens | target | segments | V1 | V2 | V4 | V6 | md5 (head12) |
|------|:------:|------:|-------:|-------:|---------:|:--:|:--:|:--:|:--:|--------------|
| 01_core_reference.md | Y | 476,866 | 124,512 | 120,000 | 15 | PASS | PASS | PASS | - | 7e212bf21277 |
| 02_domain_specs.md | Y | 675,446 | 185,785 | 168,000 | 63 | PASS | PASS | PASS | - | ee15430f82d8 |
| 03_domain_knowledge.md | Y | 909,002 | 275,318 | 225,000 | 126 | PASS | PASS | PASS | - | 6301b6e053ff |
| 04_terminology_core.md | Y | 1,111,314 | 299,303 | 200,000 | 5 | PASS | PASS | PASS | PASS | 68b904528240 |

## V3 累计 token 判定

- Total: **884,918** tokens
- Target (P11): ≤800,000
- Warn threshold (§8 R2): >900,000
- Hard threshold (1M 窗口): >1,000,000

- **V3 PASS**: total 884,918 **exceeds** target 800,000 (+10.6%) but remains below WARN threshold 900,000 (余 15,082) and 1M hard threshold; rc=0 correct per V3 3-tier band logic (PASS / WARN >900K / FAIL >1M). 描述笔误修正于 2026-04-20 Node 3 (Gemini LOW-1 AB reviewer carry-over).

## 备注 (逐文件)

### 04_terminology_core.md
- V2 INFO: 5 segments recorded (no min cap)
- V6 PASS: tail 30% has 3 terminology segments (≥3)

## 判定

- rc=0 (PASS)
