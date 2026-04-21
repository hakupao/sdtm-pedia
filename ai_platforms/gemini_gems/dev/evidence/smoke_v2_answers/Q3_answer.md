# Q3 — Gemini SDTM Expert answer

> URL: https://gemini.google.com/u/1/gem/3b572e310813/77c617999fcf105f
> Mode: Pro
> Run: 2026-04-21
> Note: First submit landed empty (ngModel sync issue); re-submitted after adding InputEvent dispatch. Q3 is turn 3 user in this conversation (turns 1+2 are gem auto-acks).

## 原题
受试者空腹 HbA1c 检验结果为 6.8%, 参考范围 4.0-6.0%, 实验室标注为"高". 请说明 SDTM LB 域中, 这次检验应该如何填写以下变量: LBTEST (检验名) / LBTESTCD (检验代码) / LBORRES (原始结果) / LBORRESU (原始单位) / LBSTRESC (标准化字符结果) / LBSTRESN (标准化数值) / LBSTRESU (标准化单位) / LBNRIND (参考范围指示)? 指出 LBNRIND 的三挡分类 (低 / 正常 / 高) 用什么代号.

## 答案全文

### 1. 变量映射结论

针对该受试者空腹 HbA1c 6.8%（参考范围 4.0-6.0%）的检验记录，在 SDTM LB (Laboratory Test Results) 域中应作如下映射：

- **LB.LBTEST** (Role: Topic, Core: Req): 填入 HbA1c 对应的标准名称（需依据对应 Controlled Terminology，通常如 Glycated Hemoglobin）。
- **LB.LBTESTCD** (Role: Identifier, Core: Req): 填入对应的测试简码（需依据 CT 规范，通常如 HBA1C）。
- **LB.LBORRES** (Role: Result, Core: Exp): 6.8 (存储收集到的原始字面结果)。
- **LB.LBORRESU** (Role: Variable Qualifier, Core: Exp): % (原始收集单位)。
- **LB.LBSTRESC** (Role: Result, Core: Exp): 6.8 (标准化后的字符型结果；当无定性符号且未发生数值转换时，通常直接取 LBORRES 的值)。
- **LB.LBSTRESN** (Role: Result, Core: Exp): 6.8 (标准化后的纯数值型结果，专供后续分析计算使用)。
- **LB.LBSTRESU** (Role: Variable Qualifier, Core: Exp): % (标准化后的单位，若无需向 SI 等标准单位折算则同原始单位)。
- **LB.LBNRIND** (Role: Variable Qualifier, Core: Exp): 填入代表实验室提示结果异常偏高的标准代码。

(注：对于参考范围的值，同时会映射进入 LB.LBORNRLO = 4.0 与 LB.LBORNRHI = 6.0)

### 2. 关于 LBNRIND 三挡分类代号 (依据边界约束 CO-2)

您询问了 LBNRIND 中"低 / 正常 / 高"的具体代号。

**本 Gem C 方案决策不 inline codelist Term 具体值。**

- CT Code `C78736` 对应 codelist 英文名: `<Reference Range Indicator>` (据本 Gem 索引核实)。
- Term 值查询: 请查 NCI EVS Browser: https://evsexplore.semantics.cancer.gov/evsexplore/ 搜索 C78736。

本 Gem 不 inline Term 值以保业务场景完整覆盖，不记忆/生成 NCI Code。

### 3. 依据

根据 Findings 类的通用假设，`--ORRES` 族变量如实反映原始获取记录，而 `--STRESC / --STRESN / --STRESU` 用于统一格式的数值标准化，以保证汇总统计的科学性。`--NRIND` 用于捕获观测结果相对正常参考区间边界 (`--ORNRLO` 和 `--ORNRHI`) 的分类定位或临床判读指示，必须强制使用其绑定的 Controlled Terminology 进行规范表达。

**源路径**: knowledge_base/domains/LB/spec.md §LBTEST, §LBTESTCD, §LBORRES, §LBSTRESC, §LBNRIND
knowledge_base/chapters/ch04_general_assumptions.md (Findings Observation Class section)
