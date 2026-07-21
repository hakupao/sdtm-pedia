# Q13 (G1 — RWD/Observational SDTM, NS/SUPPDM 2024 文档应用)

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e8413d-0950-83a3-b189-e1e05bca9efb
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: **4m 55s** (本批最长)

## 完整回答 (要点摘录)

### 开场诚实声明

模型主动声明: 无法直接逐字核对 CDISC 2024《Considerations for SDTM Implementation in Observational Studies and Real-World Data v1.0》, 因为该文档本身**不在当前已上传知识库**, 且环境**外部检索不可用**. 因此回答将基于 SDTMIG v3.4 / SDTM v2.0 现有规则推断 2024 文档大概率落地方式, **把"直接有底座证据"和"推断"分开标注**.

### (a) RWD/observational 场景下自然失效的 3 类 conformance rule

**最典型自然不适用的, 不是 SDTM 基础结构规则, 而是依赖前瞻性 trial design 的规则**:

1. **Trial Arm / Trial Design 依赖型规则**
   - 例: DM 里 ARM/ARMCD/ACTARM/ACTARMCD 必须来自 TA (Trial Arms)
   - 若研究本身没有 planned arm, 这类规则就没有现实基础
   - SDTMIG 明确说 DM 这些 arm 变量要来自 TA, 或为 null

2. **Planned Visit 依赖型规则**
   - SDTMIG 要求 planned visits 的 VISIT/VISITNUM/VISITDY 必须与 TV (Trial Visits) 一致
   - 但 observational/RWD 常见真实世界接触, 临床 encounter, 远程随访, 机会性采集
   - 不一定有 protocol-defined TV → 此类一致性规则自然弱化或失效

3. **EPOCH / TAETORD 等 study-design construct 规则**
   - SDTMIG 直接把 EPOCH 定义为 study-design construct
   - 若不能确定 epoch, 应为 null
   - 没有清晰前瞻性 epoch/element/arm 设计时, EPOCH/TAETORD 等设计导出变量往往不适用

**反过来不会自然失效的**: SDTM 结构底座本身 — 主键思路, USUBJID 唯一性, ISO 8601 时间格式, SUPP-- 连接方式, 标准变量不能随意改名等.

### (b) 没有 planned ARM 的观察性研究 DM 域 ARM/ARMCD 处理

**处理原则**: DM.ARMCD = null, DM.ARM = null

按 SDTMIG: 如果 ARMCD 为 null, 则 ARM 必须也为 null, 并且 ARMNRS 要填原因. 如果研究也不存在 actual arm 概念, 则 ACTARMCD/ACTARM 同样应为 null, 用同一个 ARMNRS 说明.

**详细规则**:
- DM.ARMCD: 未分配 → null + ARMNRS populated
- DM.ARM: 未分配 → null + ARMNRS populated
- DM.ACTARMCD/DM.ACTARM: 未分配或实际路径不对应任何 planned arm → null + ARMNRS populated
- DM.ARMNRS 标准例子: **"NOT ASSIGNED" / "SCREEN FAILURE" / "ASSIGNED, NOT TREATED" / "UNPLANNED TREATMENT"**

**最稳妥的纯 observational 研究 DM 处理**:
- ARMCD = null
- ARM = null
- ACTARMCD = null
- ACTARM = null
- ARMNRS = **"NOT ASSIGNED"** (最贴近 SDTMIG 语义的值)

### (c) 2024+ NS (Non-Standard Domain) vs 传统 SUPPQUAL 区别

**诚实约束**: 模型说"不能确认 2024 文档对 NS 的正式术语定义, 但按 SDTMIG 逻辑边界可清楚表述".

**1) SUPPQUAL (SUPP--) 是什么**:
- 给现有父记录补一个非标准变量的机制
- relationship dataset, 一条 SUPP-- 记录对应某父域某条记录上的一个补充 qualifier
- 键结构: STUDYID, RDOMAIN, USUBJID, IDVAR, IDVARVAL, QNAM
- DM 特例: IDVAR/IDVARVAL 可空 (DM 每 USUBJID 仅 1 条记录)
- 标准域不能新增任意变量, 非标准变量进 SUPP--
- 用于 NSVs: other-specify / 多值 qualifier / 长文本拆分 / secondary evaluator attribution 等

**2) NS / Non-Standard Domain 更像什么**:
- 若数据 different in nature and do not fit into an existing published domain → 创建 custom domain
- 若数据 not directly related to records in a parent domain → 不应放 supplemental qualifiers, 应进 separate general observation class domain or special-purpose domain

**对照表 (按 SDTMIG 逻辑推断)**:

| 比较点 | SUPPQUAL | NS / Non-Standard Domain |
|---|---|---|
| 本质 | 父记录的补充变量 | 独立的数据主题/独立观察 |
| 物理形式 | SUPP-- relationship dataset | 一个单独 domain |
| 是否依赖父记录 | 强依赖 | 不一定依赖单一父记录 |
| 适合的数据 | other-specify, 附加属性, 多选拆分, 长文本, 附加 evaluator | 反复出现, 可独立成行, 有自己 topic/timing/key 的 observation 集合 |
| 键 | 跟着父记录键走 | 自己有 domain-level key / natural key |

**一句话版**:
- SUPPQUAL 是"给现有记录加列的竖表化表示"
- NS/自定义域是"这批数据本身就该另起一张表"

**observational/RWD 最常见分界**:
- 稀疏, 附属性 → SUPP--
- 成体系, 可重复, 可定时, 可独立分析 → 独立域

### (d) SUPPDM 可补什么 observational 特有数据

**最稳一条**: SUPPDM 可补"仍然属于 subject-level, 且本质上是 DM 单条 subject 记录的附加属性"的 observational 特有数据.

**SUPPDM 合适补充的常见类**:
- 更细粒度人口学自我认同: 细分种族/民族/原住民类别, 国家/地区特异 ethnicity subcategory, 多选 race/ethnicity 附加值
- 单次采集, 静态或近静态的 subject-level 背景属性: 数据来源标签 (registry cohort / claims-only / EHR-linked), 受试者层面 source-system ID / registry ID / network ID, 单次定义的保险类型/教育水平/职业/居住类型/照护者状态, 入组路径/招募来源/consent subtype

**SUPPDM 不适合的边界**:
- 更像客观 subject characteristic → SDTMIG 建议考虑 **SC (Subject Characteristics)** 而非 SUPPDM
- 不是 DM 那条 subject 记录的附属属性而是独立 observation → 不应放 SUPPDM, 应另建域
- 随时间变化 (保险状态/居住状态/护理方式/就诊接触方式反复发生) → 不是 DM/SUPPDM 该承载的对象, 适合单独域或 visit/encounter 相关域

**实务化判断句**:
> SUPPDM 适合"one-subject-one-record 的 DM 还差一点说明"的 observational 信息;
> 不适合"有时间轴, 可重复, 可成主题"的真实世界观测.

## 判据对齐

- (a) **3 类失效规则全到位** ✓ (Trial Arm / Planned Visit / EPOCH+TAETORD); 反向声明哪些不会失效 (主键/USUBJID/ISO 8601/SUPP--/标准变量名) ✓
- (b) ARMCD=null + ARM=null + ACTARM=null + ARMNRS="NOT ASSIGNED" ✓; ARMNRS 4 标准 codelist 值列出 ✓
- (c) **诚实声明 NS 在 v3.4 KB 外** ✓; 按 SDTMIG ch02/ch08 逻辑推断对照表 5 维度 (本质/物理形式/依赖/适合数据/键) ✓; 一句话总结清晰 ✓
- (d) SUPPDM 适合 vs 不适合 边界清楚 ✓; SC 对照 ✓; 时间轴/可重复 → 独立域 边界 ✓
- bonus: 主动区分"直接底座证据" vs "推断" ✓ (本批最高诚实度)
- bonus: SUPPDM vs SC 对比 (而非简单填鸭) ✓
- bonus: 实务化判断句 (one-subject-one-record vs 有时间轴) ✓

源溯源命中:
- `knowledge_base/domains/DM/assumptions.md`
- `knowledge_base/domains/DM/spec.md`
- `knowledge_base/domains/DM/examples.md`
- `knowledge_base/chapters/ch02_fundamentals.md`
- `knowledge_base/chapters/ch08_relationships.md`

## 归因

PASS — Constrained generalization. **2024 RWD 文档 KB 0**, 模型最高诚实度: 直接声明无法逐字核对外部文档 + 标注"基于 SDTMIG v3.4 推断". 仍能用 v3.4 trial design / DM ARM/ARMCD / SUPP-- / ch02 custom domain 4 个原生概念把 4 子问题答完整. (c) 5 维度对照表是非 trivial 加分项 (一般 LLM 会含糊带过 NS 概念). (d) SUPPDM vs SC 边界 + "时间轴决定独立域 vs SUPP" 实务句是观察性研究的精准判断框架. **思考 4m 55s 是本批最长**, 与文档外推断 + 多原生概念整合一致.
