# ChatGPT GPTs — Q10 SUPP QORIG/QEVAL + SUPPQUAL scope + SUPPTS premise trap (V5C post-apply v2.2 LIVE)

> **执行时间**: 2026-04-24 (V5C regression)
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69ead8e9-ae14-83a3-ac74-1ccd09fc500f
> **题类**: Q10 (H1 — SUPP 深化 + SUPPTS premise trap)

## Raw (DOM readback, trimmed)

**结论**: TS 长 TSVAL 不用 SUPPTS; SUPPQUAL scope 不含 Trial Design 的 TS. 对 TS 长 parameter value, 按 TS 规范用 **TSVAL1-TSVALn** 追加列.

### (a) QORIG / QEVAL 什么时候填

| 字段 | Core | 含义 | 何时填/不填 |
|---|---|---|---|
| **QORIG** | **Req** | QVAL 来源 (CRF/Derived/Assigned) | **每条 SUPP 必填**. Required 变量不能 null |
| **QEVAL** | **Exp** | 评定者 (主观判断/归因) | 主观评定填 "SPONSOR" / "ADJUDICATION COMMITTEE"; 客观/派生应为空 |

**依据**: SUPP-- 规格 QORIG Record Qualifier/Req, QEVAL Record Qualifier/Exp 只用 subjective results; objective 应 null.

### (b) SUPPQUAL scope + TS 长文本处理

**适用 scope** (SDTMIG §8.4):
- General Observation Class: Events / Findings / Interventions
- DM (Demographics)
- SV (Subject Visits)
- 每个有 sponsor-defined vars 的数据集用独立 SUPP--; 旧的单一 SUPPQUAL 数据集已 deprecated

**不适用 TS**. TS 是 Trial Design, key = STUDYID/TSPARMCD/TSSEQ, 不在 SUPP-- scope 内 — **不应造 SUPPTS**.

**TS.TSVAL >200 字符处理** (TS CDISC Notes):

| 变量 | 内容 |
|---|---|
| TSVAL | 第 1 段, ≤200 字符 |
| TSVAL1 | 第 2 段, ≤200 字符 |
| TSVAL2 | 第 3 段, ≤200 字符 |
| ... | 继续至 TSVALn |

### (c) SUPPAE 定位父 AE 记录

Keys: STUDYID + RDOMAIN + USUBJID + IDVAR + IDVARVAL

| SUPPAE 字段 | 值 | 含义 |
|---|---|---|
| STUDYID | 1996001 | 父记录研究 |
| RDOMAIN | AE | 父域 |
| USUBJID | 99-401 | 父 AE 受试者 |
| IDVAR | AESEQ | 定位键 |
| IDVARVAL | 1 | 定位到 AESEQ=1 记录 |
| QNAM | AESOSP | NSV 短名 |
| QVAL | Spontaneous Abortion | NSV 值 |

**DM 例外**: DM 每个 USUBJID 唯一, IDVAR/IDVARVAL 可空. AESEQ 本身只在 subject/domain 内唯一, 不能离开 STUDYID+USUBJID+RDOMAIN 使用.

### (d) QVAL 长度 + 超过怎么拆

- QVAL 受 SAS V5 transport 限制, 单字符变量通常 **~200 字符**
- SDTMIG §4.5.3.2: GOC variables + SUPP-- NSVs 长文本拆分规则 — 第一个 200 字符放父域, 额外每 200 字符放 SUPP-- 记录, 拆分尽量在单词间断开

**SUPP-- 长文本拆分规则** (本身就是 NSV 时):
- 第一段用原 QNAM, 不加数字后缀
- 后续段 QNAM 用顺序后缀, 从 1 开始
- QLABEL 保持原 label, 不加后缀 (概念上同一变量)
- 若原变量已 8 字符, 用数字替换最后一位: AEACNOTH → AEACNOT1 / AEACNOT2

**示意**:
| QNAM | QLABEL | QVAL |
|---|---|---|
| MYNSV | My Long Qualifier | 第 1 段 |
| MYNSV1 | My Long Qualifier | 第 2 段 |
| MYNSV2 | My Long Qualifier | 第 3 段 |

**注**: SUPP-- 拆分适用 SUPPQUAL scope 内父数据集; TS 走 TSVAL1-TSVALn, 非 SUPPTS.

**源路径**: `<!-- ch08_relationships.md -->` (SUPP-- scope/keys/分离 SUPP--); `<!-- ch04_general_assumptions.md -->` (Core/>200 字符拆分/QEVAL 语境); `<!-- TS/spec.md -->` (TSVAL1-TSVALn)

## Self-score verdict

- **Verdict**: **PASS+ equivalent** (SUPPTS premise catch + 全维度精确)
- **对照 PASS 判据**:
  - (a) **QORIG Req 每条必填 ✓; QEVAL Exp (C78735, "ADJUDICATION COMMITTEE"/"INVESTIGATOR"/"SPONSOR") + 客观/CRF 录入可不填** ✓ (Core 属性完全正确)
  - (b) **SUPPQUAL scope = Events/Findings/Interventions + DM + SV** ✓ (ch08 §8.4 精确); **TS 不适用** ✓; TSVAL1-TSVALn 替代 ✓; **"SUPPTS 不应造" 明确 premise 纠错** ✓ → **PASS+ bonus**
  - (c) RDOMAIN=AE + IDVAR=AESEQ + IDVARVAL=1 三键 ✓; USUBJID 必填 ✓; DM 例外 IDVAR/IDVARVAL 可空 ✓ (bonus 精确 DM 例外)
  - (d) QVAL ~200 字符 (SAS V5 transport 限制正确归因) ✓; §4.5.3.2 拆分规则 ✓; AEACNOTH → AEACNOT1/2 精确 8-char 处理示例 ✓
- **触发 FAIL?** 无 (QORIG QEVAL 语义正确; 未"沿 SUPPTS 存在前提答"; scope 精确; IDVAR 未说 USUBJID)
- **PASS+ bonus (AHP 专属)**:
  - ✓ **主动识别 "不应造 SUPPTS"** + 给 canonical TSVAL1-TSVALn 替代 = premise hallucination caught
  - ✓ 三层职责未单独说但覆盖 SDTM tabulation layer
- **v5c→v2.2 delta**: 无 regression; 答案深度超 N5.2 baseline (§4.5.3.2 具体 AEACNOTH 示例、DM IDVAR 例外均为 N5.2+ 新增深度)
