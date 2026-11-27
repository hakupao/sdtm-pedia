# T4.2 人工抽样包 (交用户判定)

<!-- chain: E (plans) -->
> 状态: **待用户判定** (样本备于 2026-11-27, 主控只备样本, 不替用户判).
> 生成: `python3 -I .work/10_tier_b_repair/scripts/t4/t4_sample.py` → `python3 -I .work/10_tier_b_repair/scripts/t4/t4_render.py` (确定性, 可复跑; 本文件由脚本整体重写, 判定请在复跑前誊出或复跑后回填).
> 种子: 正式层 20261128, 风险层 20261129. 与 T4.1 总闸 72 条 (seed 20261127) 互不重叠.

## 怎么判

- **判据** (PLAN T4.2, hard 闸): 每条看 "KB 现文" 是否忠实承载 "PDF 原文" 的信息. 内容错误 = 漏信息 / 改了意思 / 值不对 / 放错位置. 闸要求 **内容错误 0**.
- "PDF 原文" 取自 PDF 文本层 (`work/pdf_pages/*.txt`, pdftotext 版式), 自动定位, 表格列对齐可能乱; 有疑问以原 PDF (`source/cdisc/SDTMIG v3.4 (no header footer).pdf` / `SDTM_v2.0.pdf`, 同页号) 为准.
- "原子 verbatim" 是早期抽取物, 已知有抽错 (终态 ATOM_ERR 的就是这类), 只作对照, 不作判据.
- 终态 ATOM_ERR: 判 "原子确实与 PDF 不符, 且 KB 按 PDF 写对了" 即正确. 终态 PDF_TYPO: 判 "PDF 确有笔误, KB 处理与登记一致" 即正确 (改不改由 `t4_user_decisions.md` 另行裁定). 终态 INTENTIONAL_EXCLUDE: 判 "这条不进 KB 合理" (KB 现文一栏为空属正常).
- KB 行号是本仓 HEAD (KB 内容 = 00a2e93) 的当前行号.

## 分层

| 层 | N | 总体 | 说明 |
|---|--:|--:|---|
| REWRITE_OK | 10 | 91 | T1 判 "KB 改写但信息等价" 的原子 |
| REAL_GAP | 10 | 237 | T1 判 "KB 真缺" 并在 T2 补的原子 |
| VALUE_DIFF | 5 | 96 | T1 判 "KB 值与 PDF 不符" 的原子 |
| IE | 5 | 513 | T1 判 "有意不收" 的原子 |
| RISK_ANCHORLESS (加层) | 12 | 508 | T3 判 EXACT 但 KB 命中处没有可核的节号锚 (`work/t3_t4_risk_anchorless.txt`); 按原因分层: "no governing numbered heading" 442 抽 8, "atom section has no number" 66 抽 4 (N 与分层为主控取值) |

- 总体排除: `MANUAL_01`/`MANUAL_02` (无 ledger 行)、残留 `ig34_p0056_a006` (另列 `t4_user_decisions.md` 待裁).
- PLAN 写 "VALUE_DIFF+IE 10", 主控按 5+5 拆. 风险层 8:4 而总体 442:66, 有意加重 "atom section has no number" 一类 (更易错位).
- 本包共 42 条 (PLAN 正式 30 + 风险加层 12). 风险层是加层: 正式闸 = 前 30 条; 风险层若判出错, 主控按 PLAN Q9 同口径扩为该类全量复核.

## 判定汇总 (用户填)

| 层 | 内容正确 | 内容错误 | 看不出 |
|---|--:|--:|--:|
| REWRITE_OK (10) | | | |
| REAL_GAP (10) | | | |
| VALUE_DIFF+IE (10) | | | |
| RISK_ANCHORLESS (12) | | | |
