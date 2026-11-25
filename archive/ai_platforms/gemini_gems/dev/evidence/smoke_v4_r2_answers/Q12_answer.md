# Gemini Gems — Q12 CT 版本锁定 (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **题类**: Q12 (D2 bonus)
> **R1 baseline**: PASS

## Raw 回答

- **(a)** 锁用 research start 时版本 (而非 DBL 即时最新); Ongoing 不同步每季度更新; 中途有 planned upgrade 决策时整体迁移, 否则 keep start version
- **(b)** Define-XML MetaDataVersion + CodeList element 通过 **standardOID** 和 **StandardVersion** 属性标 CDISC CT 发布日期 (e.g., "2022-03-25"); ExternalCodeList 引用 NCI EVS Dictionary=CDISC CT + Version
- **(c)** **AETERM (Verbatim) 不受影响** (原始字面不变); **AEDECOD (MedDRA Preferred Term) 受影响**, DBL 前全量 recode 到 v27 单一版本; nSDRG 声明 MedDRA 版本
- **(d)** Retired/alias CT: 坚持锁定版本技术合规; 或 query NCI EVS Alias/Retire → 映射 PT → SUPP-- 保原始 → nSDRG 文档化变更逻辑

## Self-score verdict

**PASS** — CT 锁用原则正确 + Define-XML StandardVersion/ExternalCodeList + MedDRA 单一版本 recode 路径 + retire/alias 文档化. 对齐 R1 PASS.
