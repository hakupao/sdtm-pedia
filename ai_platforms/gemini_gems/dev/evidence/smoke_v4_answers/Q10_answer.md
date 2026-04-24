# Gemini Gems — Q10 SUPP QORIG/QEVAL + SUPPQUAL scope + SUPPTS premise trap (V5C post-apply v7 LIVE)

> **执行时间**: 2026-04-24 (V5C regression)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/d0bb9ac9831057f0
> **题类**: Q10 (H1 — SUPP 深化 + SUPPTS premise trap)

## Raw (DOM readback)

### (a) QORIG 与 QEVAL

- **QORIG (Origin)**
  - 含义: 非标变量 NSV 原始来源
  - 必填性: **Exp (Expected)** ⚠️ (PASS 判据是 Req, Gemini 答 Exp — MINOR miss)
  - 填法: CRF / DERIVED / ASSIGNED / VENDOR

- **QEVAL (Evaluator)**
  - 含义: QVAL 由特定人员评估时记录评估者
  - 必填性: **Perm (Permissible)** ⚠️ (PASS 判据是 Exp, Gemini 答 Perm — MINOR miss)
  - 填法: 需要区分评估主体时填; 不适用时 null

### (b) SUPPQUAL 适用范围 + TS 长文本

- **适用**: General Observation Classes (Interventions/Events/Findings) + DM 域
  - ⚠️ Gemini 未提 SV (Subject Visits), PASS 判据含 SV — MINOR miss
- **TS 处理**: **不适用 SUPPTS ✓** (premise caught) — "TS 属 Trial Design 模型, SDTM 规定 Trial Design 域 (TS/TA/TE/TI/TV) 不得创建对应 SUPP--"
- **长文本**: TSPARMCD 对应长 TSVAL 超 200 字符应通过 **TSVAL1/TSVAL2/.../TSVALn** 拆分
- **原则**: 只 Subject-level (含 USUBJID) 用 SUPP--; TS 是 Study-level 元数据

### (c) 关联机制定位父记录

- USUBJID: 与父记录完全一致 (首要条件)
- RDOMAIN: 父域缩写 "AE"
- IDVAR: 用于定位的变量名, AE 域通常 "AESEQ"
- IDVARVAL: IDVAR 具体数值 (若 AESEQ=5 则 IDVARVAL="5")
- 注意: NSV 属受试者级别 (对整 DM 域生效), IDVAR 可 null, IDVARVAL 也 null ✓

### (d) QVAL 长度上限 + 拆分

- **长度上限: 200 个字符** (Gemini 说法; 严格 PASS 判据是 "QVAL 自身无显式业务长度规定, 200 是父域 GOC 变量拆分阈值")
- 拆分: 多个记录垂直拆分, 相同 QNAM/IDVAR/IDVARVAL; QLABEL 区分顺序
- **SDTMIG v3.4 推荐**: 极冗长文本 Findings 类可考虑 CO (Comments) + COVAL1-COVALn; 或 SUPP-- 中按 QNAM 命名规则 (REAS1, REAS2) 手动管理

**源路径**: `knowledge_base/chapters/ch08_supplemental_qualifiers.md §8.4`; `TS/assumptions.md` (TSVALn); `01_navigation` §8.4.1

## Self-score verdict

- **Verdict**: **PASS** with MINOR carry-over (SUPPTS premise caught = PASS+ equivalent on AHP; but Core 属性 QORIG/QEVAL 弱)
- **对照 PASS 判据**:
  - (a) QORIG 含义 ✓ (CRF/DERIVED/ASSIGNED/VENDOR); **QORIG Core 错答 Exp (应 Req)** ⚠️ MINOR; QEVAL 含义 ✓; **QEVAL Core 错答 Perm (应 Exp)** ⚠️ MINOR
  - (b) SUPPQUAL scope Events/Findings/Interventions + DM ✓, **SV 漏** ⚠️ MINOR; **"SUPPTS 不适用 + Trial Design 不得创 SUPP--" 主动识破** ✓ → **PASS+ bonus**; TSVAL1-TSVALn ✓
  - (c) USUBJID / RDOMAIN="AE" / IDVAR="AESEQ" / IDVARVAL 具体值 ✓; IDVAR 可 null (DM) ✓
  - (d) QVAL 200 字符 (非严格但业界常识) ✓; 拆分规则描述 ✓; **CO (Comments) + COVAL1-COVALn 替代 — 加分 (PASS 判据未要求但精确)**
- **触发 FAIL?** 无 (未"沿 SUPPTS 存在前提", 未 IDVAR=USUBJID 错误)
- **PASS+ bonus (AHP 专属)**:
  - ✓ **SUPPTS premise 主动识破** + TSVAL1-TSVALn canonical 替代
- **v5c→v7 delta (MINOR carry-over)**:
  - ⚠️ **NEW MINOR**: QORIG Core Req 错答 Exp / QEVAL Core Exp 错答 Perm — Core 属性精度弱 (Gemini Core 答案与 KB `domains/SUPPQUAL/spec.md` 不符). Non-blocking; 可 v7.1 optional patch 强 SUPP-- Core 锚点 (同 CO-1/CO-1b 风格)
  - ⚠️ SV 漏, SUPP-- scope 略缩水
- **跨平台观察 (Rule E)**: ChatGPT Q10 Core 属性精度 > Gemini (QORIG Req/QEVAL Exp ChatGPT 正确, Gemini 错); ChatGPT §4.5.3.2 AEACNOTH 8-char 示例 Gemini 未提. Gemini 答 CO+COVAL1-n 替代 ChatGPT 未提. 跨平台互补.
