# Q9 — Gemini SDTM Expert 回答 (A9 — Pinnacle 21 FAIL 分类 + cSDRG 策略)

> 期望核心: 5-6 大类 FAIL + 每类 1 例 + "什么时候修 (Fix) vs 什么时候在 Reviewer's Guide 文档化 (Document)" 策略
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/aa55e39c20befe72
> 时间: 2026-04-22
> Mode: Pro

## 完整回答

处理 Pinnacle 21 (P21) 的验证报告是递交准备阶段最耗时但也最关键的环节之一. P21 本质上是将 SDTMIG 规则、FDA/PMDA 递交指南以及 NCI 控制术语库 (CT) 具象化为机器可读的校验逻辑.

### 常见 P21 报错大类与典型例子

**1. Core 属性违规 (Required/Expected 变量缺失)**

P21 会严格检查变量是否满足其 Core 属性的最低要求.

- 典型例子: AE.AESEQ (Core: Req) 为空, 或者 DM.ACTARM (Core: Exp) 变量在数据集中完全缺失.
- 源路径: `knowledge_base/domains/AE/spec.md` §AESEQ + `knowledge_base/domains/DM/spec.md` §ACTARM

**2. 控制术语 (Controlled Terminology, CT) 违规**

数据值未严格映射到 CDISC 官方支持的 Submission Value.

- 典型例子: LB.LBNRIND 被错误映射为单字符 "H"/"L", 而 CDISC 官方要求全拼 ("HIGH"/"LOW"/"NORMAL").
- 源路径: `knowledge_base/chapters/ch04_general_assumptions.md` (Controlled Terminology). LBNRIND CT Code=C78736, 具体 Term 查 NCI EVS Browser.

**3. ISO 8601 日期/时间格式错误**

所有 Timing 变量必须严格遵循 ISO 8601.

- 典型例子: AE.AESTDTC 写成 `10-MAY-2023` (非 ISO) 或带不支持的 Z 时区标识符.
- 源路径: `knowledge_base/chapters/ch04_general_assumptions.md` §4.1.4.1

**4. 跨域一致性 / 引用完整性 (Cross-Domain Integrity)**

域与域之间关联数据必须对齐.

- 典型例子: AE 或 VS 域出现某 USUBJID, 但 DM 域无该受试者 (Missing subject in DM).
- 源路径: `knowledge_base/domains/DM/assumptions.md`

**5. 字典编码不一致 (Dictionary Coding Mismatches)**

AE 或药物编码与 Define-XML 声明的字典版本不匹配.

- 典型例子: AE.AEDECOD 的值与当前声明的 MedDRA 版本 PT 拼写不一致.
- 源路径: `knowledge_base/domains/AE/assumptions.md`

**6. 键值序列或去重违规 (Duplicate Records)**

同一受试者同一时间点同一次测试缺乏唯一标识符.

- 典型例子: VS 同一 USUBJID 出现两条 VSTESTCD/VSDTC/VSTPTNUM 全同记录, 无 VSLOC/VSLAT 修饰变量区分.
- 源路径: `knowledge_base/domains/VS/assumptions.md`

### 实战策略: 什么时候修 (Fix) vs 什么时候写文档 (Document)?

核心原则: **真实反映数据的原始收集状态**.

**🟢 必须修改数据代码 (Fix)**:

- **映射逻辑错误**: LBNRIND="H" 或日期格式错误, 明显是 Programmer ETL 阶段错误, 必须代码端修复.
- **遗漏提取**: EDC 确实收集了数据但映射时遗漏 (如 AESEQ 未正确生成), 必须补齐.
- **拼写与大小写问题**: CT 值 "MILD" 错拼 "MIld" 等.

**🟡 保留原貌并在 cSDRG (Reviewer's Guide) 中解释 (Document)**:

- **数据确实未收集 (Exp 变量为空)**: DM.ACTARM Exp 变量空 (受试者随机化后吃药前退出), P21 报 Warning. **不填值**, 在 cSDRG 解释 "ACTARM is null for subject X because they discontinued prior to receiving any study drug."
- **超出 CT 覆盖范围的合法业务扩展**: 罕见病研究产生全新 VSTESTCD, **保留该项**, 在 cSDRG 和 Define-XML 扩展术语列表说明, 并注明正在向 CDISC 申请纳入.
- **符合医学逻辑的"异常"时序**: 粗略部分日期导致的 End < Start (Start=2023-05, End=2023-05-01), EDC 原文如此且医学合理, **保留**, cSDRG 解释.

## 判据对齐

| 维度 | 期望 | 实际 | Hit |
|------|------|------|-----|
| 5-6 大类 FAIL | 5-6 分类 | 6 大类 (Core违规 / CT违规 / ISO 8601 / Cross-Domain / Dict Coding / Duplicate) | ✅ |
| 每类 1 典型例子 | 具体触发例 | 6 类各有典型例 (AESEQ / LBNRIND H/L / AESTDTC format / Missing USUBJID / AEDECOD MedDRA / VS dup) | ✅ |
| Fix 场景 | 映射错/遗漏/拼写 | 映射逻辑错 + 遗漏提取 + 拼写大小写 | ✅ |
| Document 场景 (cSDRG) | 数据未收集/合法扩展/医学逻辑 | 未收集 Exp 空值 + 合法 CT 扩展 + 医学合理异常时序 | ✅ |
| cSDRG 术语使用 | Reviewer's Guide / cSDRG | cSDRG 明确提及 | ✅ |

## Verdict

**PASS** — 6 大类 P21 FAIL 分类全面 (Core / CT / ISO 8601 / Cross-Domain / Dict Coding / Duplicate), 每类典型例子具体且合规 (LBNRIND H/L 直接对齐 v5b §1.9 LBNRIND 全拼规则, ACTARM 对齐 v5b §1.6 DM 硬锚点). Fix vs Document 决策策略清晰三维度 (映射/收集/医学逻辑). cSDRG 概念正确. 超期望质量.

- 04 引用: 0 次 (业务 Pinnacle 21 工具层不触 04 业务场景, 合理)
- CO-2 触发: 1 次 (LBNRIND C78736 字典引 NCI EVS), 合理
- Score: 1 / 1
