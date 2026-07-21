# ChatGPT Q7 answer — Partial date SDTM/ADaM

**Verdict**: PASS+

## 核心结论
SDTMIG v3.4 允许 --DTC/--STDTC 保留 partial date precision; 不要为了"补全"而把未知日/月强行填成 01. SDTM 层**没有通用 partial date imputation 规则** (SDTMIG §4.4.2); imputation 走 ADaM.

## 场景填法

| 场景 | 推荐 SDTM 填法 | 不要这样做 |
|---|---|---|
| A: AE 2024-06 (无日) | `AESTDTC="2024-06"`, AESTDY=null | 2024-06-01 |
| B: CM 2024 (无月日) | `CMSTDTC="2024"`, CMSTDY=null | 2024-01-01 |
| C: 完全 Unknown | `AESTDTC=null`, 若有相对时序用 AESTRF/AESTRTPT | 造估算日期 |

## 依据
- **SDTMIG §4.4.2** 举例: "December, 2003" → 2003-12 ; "2003" → 2003
- **相对 timing 变量** (ch04):
  - 相对 study reference period: --STRF / --ENRF
  - 相对 reference time point: --STRTPT / --STTPT, --ENRTPT / --ENTPT
- **CM 例子**: CMSTDTC=null + CMSTRTPT="BEFORE" + CMSTTPT=<screening> + CMENRTPT="ONGOING" + CMENTPT=<final visit>
- **AE 例子**: AEENDTC=null + AEENRTPT="UNKNOWN" + AEENTPT=<final contact>

## (d) SDTM --STDTC 是否需要 imputation
**一般不需要也不应做**:
- 保留收集精度, partial 按 partial
- 完全没收集留空
- "prior/ongoing/before/unknown" 优先用相对 timing 变量, 不造日期
- AESTDTC=2024-06 ✓; AESTDTC=2024-06-01 的 SDTM 内补全不应做

Core 提醒:
- AE.AESTDTC = Expected (列必存在, 个记录可空)
- CM.CMSTDTC = Permissible

## (e) ADaM 需要 imputation 时 SDTM 记什么

通常做法:
1. **SDTM 保留原始精度**: AESTDTC="2024-06" / CMSTDTC="2024" / null
2. **SDTM 保留收集到的相对 timing**: CMSTRF, CMSTRTPT, CMSTTPT, AEENRTPT, AEENTPT
3. **ADaM 派生 imputed analysis date/datetime**, 算法在 define/SAP 说明

边界清晰: 分析 guidance 在 ADaM; imputed date 不回写 SDTM. 不把 disease milestone 参考日期当 imputation 填入实际日期.

## 实务细节
- **--STDY/--ENDY**: 需足够完整的实际日期才可靠; partial date 一般不填
- **EPOCH**: 不应 impute; 可依 CRF 结构/访视设计 assign; 无法确定则置空

## 源溯源
- ch04_general_assumptions.md (§4.4.2 partial date rule + relative timing)
- AE/spec.md (AESTDTC Core=Exp)
- CM/spec.md (CMSTDTC Core=Perm)

## 评分要点
- ✓ 3 场景全对 (2024-06 / 2024 / null)
- ✓ SDTMIG §4.4.2 锚点 + 具体例子 (2003-12 / 2003)
- ✓ SDTM 无通用 imputation 规则 + ADaM 边界
- ✓ (d) 不 imputation + 相对 timing 变量替代 (STRTPT/STTPT/ENRTPT/ENTPT)
- ✓ (e) SDTM 保留原始 + 相对 timing + ADaM 派生
- ✓ 补 Core=Exp vs Perm 差异 + STDY/EPOCH 实务点
