# Q5 — PK 采样 LLOQ 以下值的记录 (v2.1)

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e73be9-7490-83a3-adaf-9b3c2bcbadc2
**Date**: 2026-04-21
**Thought for**: 1m 35s

## 原题

药代动力学 (PK) 研究中, 采样点的血药浓度检测值低于实验室定量下限 (LLOQ). 按 SDTMIG v3.4 PC 域 assumptions, 应该如何填写 PCORRES (原始结果) / PCSTRESN (标准数值) / PCSTRESC (标准字符) / PCLLOQ (定量下限)? 为什么不能直接写 0?

## ChatGPT 答案 (完整)

**结论先说**:

在 **PC (Pharmacokinetics Concentrations)** 里, 若采样点浓度 **低于定量下限 LLOQ**, **不要把结果写成 0**. 应保留"低于定量下限"这一事实本身:

| 变量 | 建议填写 |
|------|---------|
| PCORRES | 填原始实验室结果, 例如 `BLQ` / `BQL` / `<LLOQ` / `<0.10`, 按原始采集或实验室报告方式保留 |
| PCSTRESC | 填标准字符结果; 若原结果是 `BLQ` 或带 `<` 的不等式, PCSTRESC 也应保留该字符表达, 而不是改成数值 0 |
| PCSTRESN | **留空 (null)**, 因为这类结果不是可直接提交的确定数值 |
| PCLLOQ | 填该记录对应的定量下限数值, 例如 0.10 |

### 依据有三层

**1. PC 变量定义**: PCORRES 是"原始结果", PCSTRESC 是"标准字符结果", PCSTRESN 只用于"标准数值结果". 只有当标准结果本身是数值时, 才进入 PCSTRESN.

**2. Findings 通则 (适用于 PC)**: SDTMIG 4.5.1 规定:
- `--ORRES` 有值时, `--STRESC` 也必须有值;
- `--STRESN` 只放数值型标准结果;
- 如果结果带有字符修饰、导致不能直接做字符转数值 (例如 <1、>10000 这类不等式), 应把该表达放在 `--STRESC`, 而 `--STRESN` 置空; 任何为分析目的的数值替代或插补, 只能在 ADaM 里做, 不应回写到 SDTM.

**3. SDTMIG 示例的直接类比**: 在通用 Findings 示例里, `BLQ` 是直接收集并复制到 `LBSTRESC` 的, `LBSTRESN` 留空; 而带 `<` 的结果也保留不等式符号, `LBSTRESN` 不填. 在 PC example 里也能看到同样模式: PC 记录中有 PCORRES = BLQ、PCSTRESC = BLQ、PCSTRESN 空、PCLLOQ = 0.10.

### 为什么不能直接写 0

**1. 0 和 "<LLOQ" 不是同一个意思**
- `0` 表示"测得浓度就是零";
- `<LLOQ` 表示"有一个上界, 但真实值未知, 只知道低于可可靠定量的阈值".

**2. 写 0 会丢失原始信息**: SDTM 的 PCORRES/PCSTRESC 目标是忠实保留采集/报告结果; 把 BLQ 改成 0, 等于把"不可定量"改造成"确定为零".

**3. 写 0 会制造伪数值**: SDTMIG 明确把带 `</>` 的结果视为不应直接进 `--STRESN` 的情况; 同理, BLQ 也不应在 SDTM 中硬改成数值. **若分析需要用 0、LLOQ/2、missing 等规则, 那是分析层 (ADaM) 的规则, 不是 SDTM 层**.

### 一个最贴近的 PC 填法示例

| 变量 | 值 |
|------|-----|
| PCTESTCD | 例如 DRUGX |
| PCORRES | BLQ |
| PCORRESU | ng/mL (若实验室给了单位, 可保留; 有时也可空) |
| PCSTRESC | BLQ |
| PCSTRESN | null |
| PCSTRESU | ng/mL (若有标准单位) |
| PCLLOQ | 0.10 |

### 源溯源

- `<!-- source: knowledge_base/domains/PC/spec.md -->`
- `<!-- source: knowledge_base/domains/PC/examples.md -->`
- `<!-- source: knowledge_base/chapters/ch04_general_assumptions.md -->`

补一句边界说明: 我这次检索里直接命中的 PC assumptions 段落没有把 "BLQ/LLOQ 不能写 0" 单独展开成一句话, 但 PC 示例 + Findings 通则 已经把 SDTM 提交层面的处理方式说明得很清楚, 且二者是一致的.

## 判据对齐 (v2.1)

- ✅ PCORRES = "<LLOQ" 或 BLQ/BQL 字符 (多种常见表达列全)
- ✅ PCSTRESC = BLQ 或 "<LLOQ" (字符标准化保留)
- ✅ **PCSTRESN = null/留空** (核心判据, 未填 0)
- ✅ PCLLOQ = 实测 LLOQ 数值 (例 0.10)
- ✅ 解释三层 (变量定义 / Findings 通则 / SDTMIG 示例)
- ✅ 解释为什么不能写 0 (三条: 语义不同 / 丢失原始 / 伪数值)
- ✅ **加分**: ADaM vs SDTM 分层指出插补归 ADaM (专业增值)
- ✅ 引 PC/spec.md + PC/examples.md + ch04 通则 3 源
- ✅ 边界声明: 坦诚指出 PC assumptions 段没有单独句, 依据是 PC 示例 + Findings 通则 (规则 D 坦诚边界)

## Verdict: **PASS** (1/1)

## 归因

系统 prompt v2.1 + PC knowledge 命中, 4 个变量填写全对 + "为什么不能写 0" 三论点完整 + ADaM/SDTM 分层指出 (加分专业). 坦诚 PC assumptions 段没原句, 靠 Findings 通则 + 示例合推 (规则 D 边界). 源溯源 3 源完整.
