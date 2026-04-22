# Q10 — Gemini SDTM Expert 回答 (A10 — SUPP-- 家族 QORIG/QEVAL + 层级 + 父记录定位 + QVAL 拆分)

> 期望核心: (a) QORIG Req (origin) + QEVAL Perm (evaluator, CRF 原数据留空, DERIVED/第三方必填); (b) SUPPAE=subject-level 有 USUBJID vs SUPPTS=study-level 无 USUBJID 仅 STUDYID; (c) STUDYID + USUBJID + RDOMAIN + IDVAR + IDVARVAL 联合键定位; (d) QVAL ≤200 字符 (SAS XPT V5), 超长拆多条 QNAM=DESC1/DESC2 + QLABEL Part1/Part2
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/6b4ca78b26e23b51
> 时间: 2026-04-22
> Mode: Pro

## 完整回答

### (a) QORIG 与 QEVAL 的必填时机与含义

- **QORIG (Origin)**: 表示补充数据的来源 (CRF, eDT, DERIVED, PRO).
  - 何时必填: 通常 Core=Req 或 Exp (基于 Traceability 原则视为必填). 每条 SUPP 记录都必须交代出处.
- **QEVAL (Evaluator)**: 表示数据的评估者或衍生方 (INVESTIGATOR, SPONSOR, VENDOR).
  - 何时必填 / 何时不填: Core=Perm. 当数据直接在 CRF 上收集 (原始数据) 时, QEVAL 留空 (Null). 当数据 Sponsor 衍生 (QORIG="DERIVED"), 或第三方 (中心实验室、独立阅片委员会) 评估时, 必须填入角色 (如 SPONSOR 或 INDEPENDENT ASSESSOR).

源路径: `knowledge_base/02_domains_spec_and_assumptions.md` (SUPPQUAL 结构 spec) + `knowledge_base/chapters/ch04_general_assumptions.md` (Traceability)

### (b) SUPPTS 与 SUPPAE 的层级区别

根本区别在于 **数据层级 (Observation Level)** 不同:

- **SUPPAE (Subject-level)**: AE 是受试者级别数据. SUPPAE **必须包含 USUBJID**, 补充的是某受试者的某条 AE 记录.
- **SUPPTS (Study-level)**: TS (Trial Summary) 是研究/试验级别数据 (计划入组人数、试验盲法等). SUPPTS **不包含 USUBJID**, 唯一标识最高只到 STUDYID.

源路径: `knowledge_base/01_navigation_and_quick_reference.md` (Trial Design vs General Observation 架构)

### (c) SUPPAE 如何通过 RDOMAIN+IDVAR+IDVARVAL 定位父记录

一条 SUPPAE 需要 **5 个变量的联合键** 精准 Join 到具体 AE 记录:

1. **STUDYID**: 锁定具体项目.
2. **USUBJID**: 锁定具体受试者 ("是哪位病人的 AE").
3. **RDOMAIN**: 取值 "AE", 明确目标父域 ("去 AE 域找").
4. **IDVAR**: 取值父域标识变量名, 绝大多数是 **AESEQ**.
5. **IDVARVAL**: 父域该变量的具体值 (字符串格式), 如 "1" 或 "2".

**USUBJID 的用法**: 联表查询 (Merge) 的第一把钥匙. 先通过 STUDYID + USUBJID 圈定该受试者的所有 AE, 再利用 IDVAR (AESEQ) + IDVARVAL ("1") 精确命中. 没有 USUBJID, 即使有 AESEQ 也会与其它受试者的 AESEQ=1 发生混淆.

源路径: `knowledge_base/04_business_scenarios_and_cross_domain.md` §4 跨域规则及 SUPP 映射场景

### (d) QVAL 长度上限与超长拆分规则

- **长度上限**: QVAL 最大物理长度 **200 字符** (SAS V5 Transport / XPT 规范, SDTM 提交通行限制).
- **超过怎么拆**: 拆分为多条 SUPP 记录.
  - **拆分策略**: 顺序后缀递增 QNAM 区分, 如 QNAM="DESC1" (前 200 字符), QNAM="DESC2" (后续字符).
  - **配套标签**: QLABEL 标记连贯部分, 如 "Description Part 1" / "Description Part 2".
  - 后端 ADaM/统计程师通过同一父记录下的 DESC1/DESC2 拼接还原完整文本.

源路径: `knowledge_base/chapters/ch04_general_assumptions.md` (长文本截断与超长字符串处理)

## 判据对齐

| 维度 | 期望 | 实际 | Hit |
|------|------|------|-----|
| (a) QORIG 含义 | Origin (CRF/DERIVED 等) Req | Origin + CRF/eDT/DERIVED/PRO + Req 视角 | ✅ |
| (a) QEVAL 含义 | Evaluator, Perm, CRF 原数据不填, 第三方/衍生填 | Evaluator + SPONSOR/INDEPENDENT ASSESSOR/VENDOR + Perm + CRF 留空 + 衍生/第三方必填 | ✅ |
| (b) SUPPAE subject vs SUPPTS study | SUPPAE 有 USUBJID; SUPPTS 无 USUBJID 仅 STUDYID | SUPPAE Subject-level 含 USUBJID; SUPPTS Study-level 无 USUBJID 仅 STUDYID | ✅ |
| (c) 联合键 | STUDYID + USUBJID + RDOMAIN + IDVAR + IDVARVAL + USUBJID 作用 | 5 键齐全 + RDOMAIN="AE" + IDVAR=AESEQ + IDVARVAL="1" + USUBJID 第一把钥匙解释 | ✅ |
| (d) QVAL ≤200 | 200 字符 SAS XPT V5 | 200 字符 SAS V5 Transport XPT | ✅ |
| (d) 拆分规则 | QNAM DESC1/DESC2 + QLABEL Part 1/2 | QNAM DESC1/DESC2 + QLABEL Description Part 1/2 + ADaM 拼接还原 | ✅ |

## Verdict

**PASS** — 全部 4 子问题 (a/b/c/d) 精准命中. QORIG/QEVAL Core 属性 (Req/Perm) 和 CRF-原数据 vs DERIVED/第三方的填空规则清晰; Subject-level (SUPPAE USUBJID) vs Study-level (SUPPTS 仅 STUDYID) 层级对比干净; 5 键联合定位 (STUDYID+USUBJID+RDOMAIN+IDVAR+IDVARVAL) + USUBJID "第一把钥匙" 解释教科书级; QVAL 200 字符 SAS V5 XPT 上限 + DESC1/DESC2 拆分 + QLABEL Part 1/2 + ADaM 拼接链条完整. 04 引用 1 次 (§4 跨域) 直接命中业务弹药包.

- 04 引用: 1 次 (§4 SUPP 映射场景), **属 04 业务弹药包直接命中**
- CO-2 触发: 无
- Score: 1 / 1
