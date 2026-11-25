# ChatGPT GPTs — Q7 Partial Date + SDTM vs ADaM imputation (V5C post-apply v2.2 LIVE)

> **执行时间**: 2026-04-24 (V5C regression)
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69ead688-1818-83a2-aab3-0d53d799d0cb
> **题类**: Q7 (C2 — Partial date + ADaM imputation 边界)

## Raw (DOM readback, trimmed)

**结论**: SDTM 的 --STDTC 记录 "已知/收集到的精度", 不做日期填补; imputation 通常是 ADaM 分析层规则.

| 场景 | SDTM 填法 | 不应填成 |
|---|---|---|
| A. AE 开始于 2024 年 6 月 | **AESTDTC="2024-06"**; AESTDY 留空 | 不填 2024-06-01 或 2024-06-30 |
| B. 服药开始于 2024 年 | **CMSTDTC="2024"**; CMSTDY 留空 | 不填 2024-01-01 或 2024-12-31 |
| C. AE 开始日完全未知 | **AESTDTC=null**; AESTDY=null | 不填 UNK / UNKNOWN / 0000-00-00 / 2024--- |

**依据**: SDTMIG §4.4.1 ISO 8601 extended format; §4.4.2 partial precision (December 2003 → 2003-12; 2003 → 2003); 完全缺失 = null.

### (d) SDTM 的 --STDTC 需要做 imputation 吗?

**不需要, 也不应把 imputed date 放回 --STDTC**. AESTDTC/CMSTDTC 忠实表示收集精度: 年月填 YYYY-MM, 年填 YYYY, 完全不知 null. 同理 --STDY / --DY 只有完整日期时才算 (§4.4.4).

### (e) 如果 ADaM 需要 imputation, SDTM 还需要额外记什么吗?

**SDTM 本身不新增 imputed date 变量**. 推荐做法:
1. SDTM 保留原始 partial date (AESTDTC="2024-06")
2. ADaM 派生分析日期 (ASTDT / TRTSDT 等), 用 ADaM 变量或 metadata 说明 imputation 规则
3. 若 CRF 额外收集相对时间信息, SDTM 按收集内容保存相对 timing (不用于补日期):
   - **CMSTRF**: 开始相对于 study reference period (BEFORE 等)
   - **CMSTRTPT / CMSTTPT**: 开始相对某参考时间点
   - **AEENRTPT / AEENTPT**: AE 结束相对某参考时间点 (end unknown/ongoing)

**源路径**: `<!-- source: knowledge_base/chapters/ch04_general_assumptions.md -->` §4.4.1/§4.4.2/§4.4.4; `<!-- source: knowledge_base/domains/CM/spec.md -->`

## Self-score verdict

- **Verdict**: **PASS**
- **对照 PASS 判据**:
  - A: "2024-06" ✓ (未填 2024-06-01 / 2024-06-15)
  - B: "2024" ✓
  - C: null ✓ (未填 "UNKNOWN" / "1900-01-01")
  - (d) SDTM 不做 imputation ✓
  - (e) ADaM 职责; SDTM 保真 + 相对 timing 变量 ✓
- **触发 FAIL?** 无
- **加分**:
  - 明确列出 anti-pattern (不应填成) — 超 PASS 要求
  - 提 CMSTRF / CMSTRTPT / CMSTTPT / AEENRTPT / AEENTPT 相对 timing 变量作为替代 (非 SUPP)
  - 注意 --DY 只在完整日期时算 (正确避开 imputed date 污染 DY)
- **v5c→v2.2 delta**: 无 regression; 相对 timing 变量清单比 N5.2 baseline 更厚
