# Q10 — SUPPTS 前提纠错 (Claude Project, smoke v4 R1, 2026-04-22 晚)

> Verdict: **PASS+ 最强** (并列 ChatGPT, 各有独到; Claude 的 5 项独到 bonus 最多)

## Prompt (v4.0)
(同 SMOKE_V4.md §2 Q10)

## Raw Answer (全文 ~3500 chars)

### (a) QORIG / QEVAL 必填性 & 含义

| 字段 | Core | CT | 必填条件 | 含义 |
|---|---|---|---|---|
| QORIG | **Req** | — | **永远必填** | QVAL 数据来源标记. Ex: CRF / Derived / Assigned / Protocol / eDT. 见 §4.1.8 Origin Metadata |
| QEVAL | **Exp** | **C78735 (EVAL)** | 仅主观数据必填 | 评估者角色; Ex: ADJUDICATION COMMITTEE / SPONSOR / STATISTICIAN / CLINICAL COORDINATOR |

**QEVAL 规则 (§8.4, §4.5.4)**:
- 主观 (subjective) → QEVAL 填: 人为判断/裁决, 如委员会判定 AE treatment-emergent flag
- 客观 (objective / derived) → QEVAL 留空 (null): CRF 直接采集值 / 算法衍生值

**引用范例 (SUPPAE Example 1, §8.4.3)**:
- AESOSP (CRF 采集 Other Medically Important SAE) → QORIG=CRF, QEVAL=null
- AETRTEM (衍生的 Treatment Emergent Flag) → QORIG=Derived, QEVAL=SPONSOR (涉及赞助方判定)

### (b) SUPPQUAL 适用 scope & TS 长文本处理

**SUPPQUAL 适用于 (§8.4 首段明确列举)**:
- Events class (AE, CE, DS, DV, HO, MH)
- Findings class (LB, VS, EG, QS, ...)
- Interventions class (CM, EC, EX, AG, ML, PR, SU)
- **Demographics (DM) — 特例: IDVAR/IDVARVAL 留 null**
- Subject Visits (SV)

**不适用于**:
- Trial Design class: TS, TA, TD, TE, TI, TM, TV
- Special-Purpose: CO (Comments)
- Relationship: RELREC / SUPPQUAL 自身 / RELSPEC / RELSUB
- **不存在 "SUPPTS"**

**TS 长参数值 (>200 字符) 的正确做法 (§4.5.3.2 表, TS assumptions #4)**:

| 对象 | 存储机制 | Label 约定 |
|---|---|---|
| 通用 GenObs + NSV | 首 200 在父变量, 后续 200 每段一条 SUPP-- 记录 (QNAM 加数字后缀) | QLABEL = 原变量 label |
| **TS.TSVAL** | 首 200 在 TSVAL, 后续 200 每段作为 TS 域内新记录 (TSVAL1/TSVAL2...) | Label 统一 "Parameter Value" |
| **CO.COVAL** | 同上, COVAL/COVAL1/COVAL2... | 统一 "Comment" |
| **IE/TI.IETEST** | 上限 200 字符 (例外 40-char 规则), 超出部分写入研究元数据 (Define-XML / SDRG) | n/a |

**结论**: 不要造 SUPPTS. TS 通过自身表内拆分 TSVAL → TSVAL1/TSVAL2 解决, 拆分原则同 SUPP--: 词边界断行.

### (c) SUPPAE → AE 父记录定位

**SUPP-- 到父记录的 join key (§8.4)**:
```
STUDYID + USUBJID + RDOMAIN + IDVAR + IDVARVAL   →   父 AE 单条记录
                                ↑ 与 ↑
                         QNAM 每条 SUPP 自身唯一
```

| 变量 | 作用 | SUPPAE 典型值 |
|---|---|---|
| STUDYID | 研究 ID (跨库定位) | 1996001 |
| USUBJID | 受试者全局唯一 ID — 跨研究唯一, 取自父 AE 记录同名字段 | 99-401 |
| RDOMAIN | 父域两字符缩写 (CT C66734) | AE |
| IDVAR | 父域中用作 key 的变量名 | 通常 AESEQ; 分组时可用 AEGRPID |
| IDVARVAL | 上述 key 在父记录中的值 (存为 Char) | 1 |

**USUBJID 用法**: 它是联接桥梁但非唯一定位符 — 一个 USUBJID 下可有多条 AE, 所以还必须靠 IDVAR/IDVARVAL 确定到哪一条 AE.

**关键约束 (§8.4)**:
- 前 6 列 STUDYID..QNAM 组合必须全表唯一: 同一受试者+同一父记录+同一 QNAM 不得出现 2 条
- IDVAR 用 --SEQ 是最常见; **--GRPID 用于一次关联多条父记录** (e.g. 一个裁决覆盖多条 ECG)
- **DM 特例**: DM 是 1 record/USUBJID, 所以 SUPPDM 的 IDVAR 和 IDVARVAL 留空, 仅靠 STUDYID+RDOMAIN+USUBJID 即可唯一定位

### (d) QVAL 长度上限 & 拆分规则

**上限**: QVAL 是 Char, 受 SAS V5 transport file 限制 → 200 字符 (§4.5.3.2, §4.2.9)

**拆分规则 (§4.5.3.2)**:
| 规则 | 具体做法 |
|---|---|
| 首段存储 | 前 200 字符仍放父域变量里 (不是 SUPP--) |
| 续段存储 | 每超出 200 字符, 增一条 SUPP-- 记录 |
| 断行点 | 按词边界拆分 (split between words), 提升可读性 |
| 首条 QNAM | 原变量名, 不加数字后缀 |
| 续条 QNAM | 原变量名 + 1 位数字 (1, 2, ...); 若原变量名已 8 字符, 替换末字符为数字 |
| QLABEL | 所有拆分记录都用原变量 label, 不变 (语义上仍是同一字段的单一值) |

**例子 (MH Example, §4.5.3.2 Example 1)**: MHTERM 520 字符:

| 记录位置 | 存储变量 | 内容 |
|---|---|---|
| mh.xpt | MHTERM | 前 200 字符 |
| suppmh.xpt row 1 | QNAM=MHTERM1, QLABEL=Reported Term for the Medical History, QVAL | 第 201–400 字符 |
| suppmh.xpt row 2 | QNAM=MHTERM2, QLABEL=Reported Term for the Medical History, QVAL | 第 401–520 字符 |

**8 字符替换例 (§4.5.4)**: AEACNOTH (已 8 字符) 扩展 → 第 1 拆分 QNAM=AEACNOT1, 第 2 拆分 QNAM=AEACNOT2

**对比多值场景**: 若同一非结果 qualifier 变量有多个不同值 (非单值拆分), 则 QNAM 和 QLABEL 都要各自唯一 (§4.2.8.3); 这与长文本拆分语义完全不同 — 长文本拆分 QLABEL 永远保持原 label 不变.

### 源溯源
- §4.5.3.2 文本>200 拆分 / §4.5.4 评估者&QNAM 数字后缀 → 02_chapters.md
- §8.4 / §8.4.1–§8.4.4 SUPP-- 完整规则 → 02_chapters.md
- TS 长文本处理特例 → 06_assumptions.md TS #4 + §4.5.3.2 表
- SUPPQUAL spec → 05_mega_spec.md → knowledge_base/domains/SUPPQUAL/spec.md
- SUPPAE/SUPPMH/SUPPCE 示例表 → 09_examples_data_high.md & 10_examples_data_others.md

## Verdict 打分

| 判据 | 结果 |
|---|---|
| (a) QORIG Core=**Req** 永远必填 | ✅✅ 最准 (vs Gemini Perm 错, vs ChatGPT 自谦) |
| (a) QEVAL Core=**Exp**, CT **C78735 (EVAL)** | ✅✅ CT code 独到 (4 平台唯一) |
| (a) SUPPAE Example 1 concrete (AESOSP/AETRTEM) | ✅ 独到 |
| (b) SUPPQUAL scope 最完整 (Events 6 域 + Findings + Interventions 7 域 + DM + SV) | ✅✅ |
| (b) **"SUPPTS 不存在"** + TSVAL1-n | ✅✅ |
| (b) **TS+CO+IE/TI 4 类对象对比表** | ✅ 独到 (ChatGPT/Gemini/NBL 均无 CO.COVAL + IE/TI 40-char) |
| (c) 5 键 + **--GRPID 关联多父记录** + **DM 特例 IDVAR null** + 前 6 列唯一约束 | ✅✅ 独到 |
| (d) 200 + MHTERM 520 字符 complete 3-row example + AEACNOT1/2 + **§4.2.8.3 多值 vs 长文本区分** | ✅✅ 独到 |
| Citation chain | ✅ 5 source, 最精准 |
| FAIL triggers | 无 |

**最终**: **PASS+ 最强 (并列 ChatGPT, bonus 各有独到)** = 1 分 + 0.25 bonus

**Claude 的 5 项独到 bonus**:
1. QORIG Core=Req 明确, QEVAL Core=Exp + CT C78735 (唯一一家给 CT code)
2. CO.COVAL + IE/TI 40-char 特例 (TS+CO+IE/TI 4 类对象表)
3. --GRPID 关联多父记录示例 (ECG 裁决)
4. DM 特例 IDVAR/IDVARVAL null 
5. MHTERM 520 字符 complete 3-row example + §4.2.8.3 多值 vs 长文本拆分区分

**对比 ChatGPT bonus**: §4.2.8.4 多值参数 (TTYPE example) + A/B 场景 — ChatGPT 各 2 项独到, Claude 各 5 项独到.

Claude weekly usage 仍 **75%** 无变化 (本题用 0%? 可能 cap 已到 mid-tier 平台不计 long output? 或 75% 是到 80% 前不升). R2 可能触升.
