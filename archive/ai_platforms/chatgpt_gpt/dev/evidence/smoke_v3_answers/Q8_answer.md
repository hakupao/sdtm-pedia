# Q8 (B5 — EPOCH Trial Design 与 Subject-level 关系)

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83966-48c0-83ab-9060-f923a4d02c36
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: 长 (~3-4 分钟)

## 完整回答 (要点摘录)

### (a) Subject-level EPOCH 与 TA/TE 关系

**1) TA/TE 定义的是"计划中的 epoch / element"**:
- TA 用 arm path 上的 element 序列表达设计, 给 element 赋 EPOCH
- TE 定义 element 本身及其起始/结束规则
- TA assumptions 还说: EPOCH 是跨 arms 做比较的概念基础, 同一 EPOCH 名称在不同 arm 间应当"可比较"
- 相同 ARMCD + EPOCH 的 TA 记录集合, 本质上描述了一个 **study cell**

**2) Subject-level domains 里 EPOCH 是"把一条实际观测挂到哪个设计阶段"**:

Ch4 对 subject-level EPOCH 的规则非常直接:
- **Findings 域** (LB.EPOCH 等) 应基于 `--DTC`
- **Events/Interventions 域** (AE.EPOCH, CM.EPOCH 等) 应基于 `--STDTC`

也就是说:
- TA/TE: 定义计划设计
- AE/LB/CM/...: 把具体受试者的一条记录归到某个设计 epoch
- **SE: 连接两者的"桥"** — SE 描述受试者实际经过哪些 element; 若按计划走, SE.EPOCH 与其所属 arm 在 TA 中的 EPOCH 一致

**3) SE 是实际受试者路径的关键中介**.

### (b) Controlled terminology 权威清单

**双层认知**:
- **CT 根源是 C99079** (CDISC EPOCH codelist)
- **研究内权威的 epoch 列表是 TA 中定义并在 Define-XML 中声明的研究特定 permissible values**

TA 上每个 arm-element 组合都带有 EPOCH; 同一个研究实际有哪些 epochs, 是由 TA 设计出来的; EPOCH 值必须能区分不同 epoch (例如 3 个 treatment epochs 不能都叫 TREATMENT).

SDTMIG Ch4: 当某变量用了一个 codelist, 并不是 codelist 里的所有值都属于该研究的 planned collection; Define-XML 只应包含研究实际允许的 permissible values.

### (c) Wash-out 期 AE.EPOCH

**结论**: 如果该 wash-out 在研究设计里被建模为独立 epoch, 就填那个 wash-out epoch. **不是填"治疗期1", 也不是填"治疗期2", 而是填设计中实际定义的那个 epoch 名称.**

判定流程:
1. 先看 TA: 该 trial 是否定义了独立 wash-out epoch
2. 再看 SE: 该受试者实际何时进入该 element
3. AE.EPOCH 作为 Events 域 timing 变量, 应按 AESTDTC (事件开始时间) 所落入的 epoch 赋值

**重要细节**: TE examples 说设计粒度是 sponsor judgment. 同一个 trial, treatment 后的 rest/washout 可以建成独立 washout epoch 也可以并入前后某个 treatment epoch. 因此你不能抽象地说"wash-out 一律填 WASHOUT", 要填 TA/TE 实际定义的那个 epoch 名称.

**边界规则**:
- 如果只有日期没有时间, 正好落在 transition date 上, sponsor 需要在 Define-XML 里说明判定算法
- Ch4 还规定: **不要 impute EPOCH**; 如果无法确定 observation 属于哪个 epoch, EPOCH 应为 **null**

### (d) AE.EPOCH 能否填 TA 未定义过的全新 epoch

**一般不应让 AE.EPOCH 出现一个该研究 TA 未定义、Define-XML 也未声明的全新 epoch 值.**

理由:
- TA assumptions: 同名 EPOCH 在不同 arms 间应有可比性, 不同 epoch 必须有不同值
- 如果在某个 subject 的 AE 上临时造一个 TA 从未定义过的 epoch 值, 会失去 trial design 上的可比性, 也破坏了 EPOCH 作为 study-design 概念的初衷
- Ch4: 不能确定 observation 属于哪个 epoch 时, EPOCH 应该为 null

**重要例外语境**: SE assumptions 允许 sponsor 对 **unplanned elements** 决定赋什么 EPOCH, 并在 Define-XML 说明方法. 示例: 一个 subject 接受了错误治疗, 被表示为 unplanned element, sponsor 仍给它赋了 EPOCH = BLINDED TREATMENT. 这说明:
- 可以有 unplanned element
- 但它的 EPOCH 仍然应尽量映射到已有的研究 epoch 概念
- 不是说可以随意发明一个 TA 里从未定义过、只在某个 subject AE 上出现的新 epoch 名称

源溯源:
- `<!-- source: knowledge_base/chapters/ch04_general_assumptions.md -->`
- `<!-- source: knowledge_base/domains/TA/assumptions.md -->`
- `<!-- source: knowledge_base/domains/TE/assumptions.md -->`
- `<!-- source: knowledge_base/domains/SE/assumptions.md -->`
- `<!-- source: knowledge_base/domains/TA/examples.md -->`
- `<!-- source: knowledge_base/domains/TE/examples.md -->`
- `<!-- source: knowledge_base/domains/SE/examples.md -->`

## 判据对齐

- (a) TA/TE 计划 vs subject-level 实际, SE 桥梁 ✓; Findings (--DTC) vs Events (--STDTC) 区分正确 ✓
- (b) C99079 codelist + TA/Define-XML permissible values 双层 ✓
- (c) wash-out AE.EPOCH = TA/TE 实际定义的那个名称, 不能套用通用"WASHOUT" ✓; sponsor 设计粒度判断 ✓
- (d) 一般不应填新 epoch ✓; SE unplanned 例外仍需 Define-XML 声明 ✓
- bonus: AESTDTC 而非 AEENDTC 决定归属 (Events 域规则) ✓
- bonus: 不能 impute EPOCH; 无法确定 → null ✓
- bonus: study cell = ARMCD + EPOCH 概念 ✓
- bonus: 同名 EPOCH 跨 arm 可比性 ✓

## 归因

PASS — Pure generalization (无任何 epoch 文档专题). 7 个 KB 锚点 (ch04 + TA/TE/SE 各两份) 全命中. 三层论述 (TA/TE 设计 / SE 中介 / subject-level 实际) + 两子层 (CT C99079 / 研究 permissible values) 都答对; (c) 的 sponsor 设计粒度区分极非 trivial; (d) SE unplanned 边界例外指出但守住"应映射到已有研究 epoch"原则. 思考较长但产出深度匹配.
