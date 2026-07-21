# Q10 (H1 — SUPP 深化) QORIG/QEVAL/QLABEL + SUPPTS vs SUPP--

> Date: 2026-04-22 / Account: bojiang.zhang.0904@gmail.com / Fresh chat (拆 4 条 sub-question 提交)

---

## 题

SDTM 的 SUPP-- (Supplemental Qualifiers) 家族里, 请回答:

- (a) 每条 SUPP 记录有 QNAM / QLABEL / QVAL / QORIG / QEVAL 5 个关键字段. QORIG 和 QEVAL 什么时候必填, 什么时候不填? 含义分别是?
- (b) SUPPTS (SUPP for Trial Summary) 和 SUPPAE (SUPP for AE) 的层级区别是什么? (subject-level vs study-level)
- (c) 一条 SUPPAE 记录如何通过 RDOMAIN + IDVAR + IDVARVAL 定位到具体的 AE 父记录? USUBJID 怎么用?
- (d) QVAL 长度上限是多少? 超过怎么拆?

## NotebookLM 答 (full text, 4 sub-message)

### Sub-message 1 (overview, 触发 d 拆分规则)

针对 SDTM 中的 SUPP-- 家族在 SDTMIG v3.4 中的核心定义、变量规范及关键业务规则:

**SUPP-- 核心目的**: 用于捕获无法容纳在标准 domain 中的非标准变量 (NSVs) 及其数据值, 同时也用于捕获由特定评估者做出的主观分类或归因 (attributions) [27_rel_suppqual.md].

**SUPP-- 变量列表**:

| Variable | Type | Role | Core | CT | Source |
|---|---|---|---|---|---|
| STUDYID | Char | Identifier | Req | | [27_rel_suppqual.md] |
| RDOMAIN | Char | Identifier | Req | C66734 | [27_rel_suppqual.md] |
| USUBJID | Char | Identifier | Req | | [27_rel_suppqual.md] |
| IDVAR | Char | Identifier | Exp | | [27_rel_suppqual.md] |
| IDVARVAL | Char | Identifier | Exp | | [27_rel_suppqual.md] |
| QNAM | Char | Topic | Req | | [27_rel_suppqual.md] |
| QLABEL | Char | Synonym Qualifier | Req | | [27_rel_suppqual.md] |
| QVAL | Char | Result Qualifier | Req | | [27_rel_suppqual.md] |
| QORIG | Char | Record Qualifier | Req | | [27_rel_suppqual.md] |
| QEVAL | Char | Record Qualifier | Exp | C78735 | [27_rel_suppqual.md] |

**QNAM 命名限制**: 最大长度 8 字符, 不能以数字开头, 除字母/数字/下划线外不能包含其他特殊字符 [27_rel_suppqual.md].

**(d) 处理超过 200 字符的长文本**: 如果标准 domain 中的变量文本长度超过 200 个字符:
1. 前 200 字符保留在父域变量中, 剩余文本需在单词之间截断并按每 200 字符切分, 存入 SUPP-- [29_ig_ch04_general_assumptions.md].
2. 此时 SUPP-- 中的 QNAM 应在原变量名后附加递增的数字 (如 `AEACNOTH` 分割为 `AEACNOT1`, `AEACNOT2`), 且 QLABEL 必须与原始域变量的 Label 完全一致 [29_ig_ch04_general_assumptions.md].

**何种数据不应放入 SUPP--**: 自由文本 comments → CO 域; 受试者特征 (国籍/双胞胎类型) → SC 域; Findings 解释 (ECG 判读) → 作为额外 Findings 记录 (EGTESTCD="INTP") [27_rel_suppqual.md].

### Sub-message 2 (a) QORIG / QEVAL

**QORIG (Origin)**:
- 含义: 指明非标准变量数据值 (QVAL) 的来源途径 [2]. 因为 QVAL 可能混合了 CRF 收集的数据、算法推导的数据或分配的数据, QORIG 用于向审阅者清晰传达该数据的最初出处 [2].
- 何时必填 / 不填: **永远必填**. 其 Core 属性为 **Req**, 任何一条 SUPP-- 记录都绝对不能将 QORIG 置空 [2]. 常见标准来源值: `CRF`、`Assigned`、`Derived` [2].

**QEVAL (Evaluator)**:
- 含义: 指明提供该主观结果或评估的人员、群体或机构的特定角色 (Role) [2]. 在 SDTM 中, SUPP-- 经常用来存储"归因" (attributions), 即特定评估者对观察结果做出的主观解释或临床意义分类 [1].
- 何时必填 / 不填: 取决于数据是"主观判断"还是"客观事实" (Core 属性为 **Exp**):
  - **填值** (主观数据): 当 QVAL 是主观分配的 (例如独立评审委员会对不良事件相关性的判定), QEVAL 必须填入对应的角色名称 (如 `ADJUDICATION COMMITTEE` 或 `SPONSOR`) [1].
  - **不填** (客观数据): 当 QVAL 是客观收集 (CRF 抄录) 或算法推导得出时, QEVAL 应该为空 (Should be null) [2].

**Codelist**: QEVAL 关联受控术语 **C78735** (Evaluator), 规范完整值: `INVESTIGATOR`、`ADJUDICATION COMMITTEE`、`STATISTICIAN`、`SPONSOR` 等 [2].

**Boundary note**: 千万不要为了填满栏位而给客观收集的补充数据硬塞 QEVAL (例如填 "INVESTIGATOR"). 只有主观判定/评估性质 (subjective data) 才需要 QEVAL, 客观收集/推导 (objectively collected or derived) 的 QEVAL 必须维持 null [2].

### Sub-message 3 (b) SUPPTS vs SUPPAE

**核心层级区别**: SUPPAE 是标准合法的 subject-level 补充数据集; **SUPPTS 实际在标准中是不存在/不合法的**, 因为 TS 属于 study-level 数据, 不适用 SUPPQUAL (Supplemental Qualifiers) 机制. [25_td_meta_ti_ts_oi.md, 27_rel_suppqual.md]

1. **SUPPAE (Subject-Level)**:
   - AE 属于 Events 观察类的 subject-level 数据域.
   - 用途边界: SUPPQUAL 结构专门用于为 general-observation class datasets (Interventions, Events, Findings)、DM 和 SV 存储 NSVs [27_rel_suppqual.md, 30_ig_ch08_ch10.md].
   - 层级关联: 在 SUPPAE 中, USUBJID (Char | Identifier | **Req**) 是强制必填的红线标准. 通过 IDVAR (Char | Identifier | **Exp**, 例如 AESEQ) 和 IDVARVAL 锚定具体的父级记录 [27_rel_suppqual.md].
   - 长文本存放: AE 域 AEACNOTH 超 200 字符时, 前 200 留主域, 超出部分存入 SUPPAE [29_ig_ch04_general_assumptions.md].

2. **SUPPTS (Study-Level — 不存在)**:
   - TS (Trial Summary) 属于 Trial Design 模型, 用于提供整个试验设计的摘要信息 [25_td_meta_ti_ts_oi.md].
   - 长文本存放: 对于 TS 域, 如果 TSVAL (Char | Result Qualifier | Exp) 的值超过 200 字符, **不能**放入 SUPP--. SDTM 规定直接在 TS 数据集内部增加派生列 **TSVAL1 至 TSVALn** 来拆分长文本 [25_td_meta_ti_ts_oi.md, 29_ig_ch04_general_assumptions.md].

**Boundary note**: SUPPQUAL 数据集严格面向 subject-level 记录的扩展方案. 任何 Trial Design 数据集 (TA, TE, TS, TI 等 study-level 数据) 均**没有对应的 SUPP-- 数据集**.

### Sub-message 4 (c) RDOMAIN + IDVAR + IDVARVAL 定位

一条 SUPPAE 记录通过复合键 (STUDYID, RDOMAIN, USUBJID, IDVAR, IDVARVAL) 准确关联到父域中的特定记录 [27_rel_suppqual.md, 30_ig_ch08_ch10.md].

- **RDOMAIN** (Related Domain Abbreviation): 指定父记录所在的域. 在 SUPPAE 中, 该值固定为 `AE` [27_rel_suppqual.md, 30_ig_ch08_ch10.md].
- **USUBJID** (Unique Subject Identifier): 限定该记录所属的受试者. 它的值必须与父记录 (AE 域不良事件记录) 的 USUBJID 完全一致, 确保附加修饰信息严格绑定在同一个受试者身上 [27_rel_suppqual.md, 30_ig_ch08_ch10.md].
- **IDVAR** (Identifying Variable): 指出父域中用于唯一标识记录的变量名. 在定位单条 AE 记录时, 通常使用 `AESEQ` (如果关联的是一组记录, 也可能使用分组变量 AEGRPID) [27_rel_suppqual.md, 30_ig_ch08_ch10.md].
- **IDVARVAL** (Identifying Variable Value): 指出父域中该标识变量的具体值. 例如, 关联到 AESEQ 为 1 的不良事件记录, IDVARVAL 必须填入 `1` [27_rel_suppqual.md, 30_ig_ch08_ch10.md].

**示例**: 将自定义变量 AEOSP (Other Medically Important SAE) 的值补充给受试者 "99-401" 的第 1 条不良事件记录, 在 SUPPAE 中填值: `RDOMAIN = "AE"`, `USUBJID = "99-401"`, `IDVAR = "AESEQ"`, `IDVARVAL = "1"` [27_rel_suppqual.md, 30_ig_ch08_ch10.md].

**Codelist**: RDOMAIN uses C66734 (SDTM Domain Abbreviation), value for Adverse Events is `AE` [33_ct_general.md].

## Verdict

| Criterion | Required | Got | Status |
|---|---|---|:---:|
| (a) QORIG = Origin, Req 永远必填 | Req + 来源含义 | Req + 永远必填 + CRF/Assigned/Derived 三种来源值 | ✅ |
| (a) QEVAL = Evaluator, Exp 条件填 | Exp + 主观/客观分支 | Exp + 主观填(Adj Committee/Sponsor)/客观置 null + C78735 codelist + INVESTIGATOR/ADJUDICATION COMMITTEE/STATISTICIAN/SPONSOR 全 | ✅ |
| (b) SUPPTS study-level vs SUPPAE subject-level | 层级清晰 | **超过 PASS 标准**: 直接指出 SUPPTS 在 SDTMIG 中**不合法/不存在** (TS Trial Design 不用 SUPPQUAL), 提供 TSVAL1...TSVALn 替代方案 | ✅+ |
| (c) RDOMAIN=AE | RDOMAIN="AE" | `RDOMAIN = "AE"` 固定值 | ✅ |
| (c) IDVAR=AESEQ + IDVARVAL=具体值 | "AESEQ"+"1" | `IDVAR="AESEQ"`+`IDVARVAL="1"` + AEGRPID 分组备选 | ✅ |
| (c) USUBJID 必填且对齐父域 | USUBJID Req 同步 | "USUBJID 必须与父记录 USUBJID 完全一致" + 99-401 示例 | ✅ |
| (d) 200 字符是父域 GOC 上限非 QVAL 自身 | 200 = 父域 cutoff, QVAL 自身无业务硬限 | 明文"标准 domain 中的变量文本长度超过 200 个字符" 触发拆分 (200 是父域 trigger), QNAM 加递增数字 AEACNOTH→AEACNOT1/AEACNOT2 | ✅ |
| (d) QLABEL 与父变量 Label 一致 | QLABEL 同步父域 | "QLABEL 必须与原始域变量的 Label 完全一致" 明文 | ✅ |

**Verdict**: ✅ **PASS** (1 / 1) — 8 项判据全中 + (b) **超 PASS 标准**: NotebookLM 直接指出 SUPPTS 不存在 (而非 PASS 草稿期望的 "SUPPTS USUBJID 可空"), 给出更准确的 TS 内部 TSVAL1...TSVALn 替代方案, 这比原 PASS 草稿对 SUPPTS 的设想 **更符合 SDTMIG v3.4 真实定义**. 加分: AEACNOTH→AEACNOT1/AEACNOT2 拆分细节 + QLABEL Label 一致性 + AEGRPID 分组备选 + 99-401 完整示例 + AEOSP 自定义变量场景. 无 FAIL 触发 (没把 200 字符归因为 QVAL 自身硬限, 没把 IDVAR 误写 USUBJID, 没把 SUPPTS 当 subject-level).

**附注 (chat 拆分原因)**: 由于输入框打字过程中段落间 Enter 触发自动 submit, Q10 实际拆成 4 条 sub-question 顺序提交 (overview + a + b + c), (d) 在 overview 中已被覆盖. 4 sub-message 内容并不互相依赖, 不构成 context cascade 污染. 等价于"分 4 题问完", 所有要点齐全.
