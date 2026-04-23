# Gemini Gems — Q10 SUPP 深化 + SUPPTS 前提纠错 (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/56461d8b5465a7cd
> **题类**: Q10 (H1 SUPP + SUPPTS premise)
> **R1 baseline**: PASS+ (SUPPTS 纠错)

## Raw 回答

- **(a) QORIG** (Origin): CRF/DERIVED/ASSIGNED/PROTOCOL, 建议必填; **QEVAL** (Evaluator): 主观评价时填 (INVESTIGATOR/INDEPENDENT ASSESSOR), 客观保 null
- **(b)** **SUPPQUAL scope**: GOC (Events/Findings/Interventions) + DM. **"SUPPTS" 纠错**: "SDTMIG v3.4 **不设 SUPPTS**, 也不允许为 Trial Design 域 (TS/TA/TE/TV/TI) 创建补充域" ✓. **长 TSVAL 处理**: TSVAL1 / TSVAL2 / ... / TSVALn 横向拆分, **严禁创建 SUPPTS** ✓
- **(c) SUPPAE 定位**: USUBJID + RDOMAIN="AE" + IDVAR="AESEQ" + IDVARVAL=字符类型 (即使 AE.AESEQ 是 Num)
- **(d)** 200 字符上限 + QNAM 加序号 (EXTTERM1/EXTTERM2) + QLABEL 保一致 / Continuation 注

## Self-score verdict

**PASS+** — **SUPPTS 前提纠错 明文识破** ✓ (v6 CO-5 AHP-V2 变体成功锚点)
- (b) **"SDTMIG v3.4 不设 SUPPTS" + 不允许 Trial Design 补充域** ✓ 强识别 — R1 已 PASS+, R2 保持
- TSVAL1-TSVALn 替代方案 ✓
- (c) RDOMAIN/IDVAR/IDVARVAL 三键 ✓ + 字符类型精确
- (d) 200 + QNAM 序号拆分 ✓
- 微瑕: QORIG Core 标 "Perm" (实际 SUPPQUAL spec = Req) MINOR, 不 downgrade PASS+

**R1 vs R2**: 对齐 PASS+. **SUPPTS 纠错 robust**.
