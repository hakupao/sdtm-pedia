# Q9 Answer — SUPPAE 边界 + QNAM/QLABEL/QVAL 示例

- URL: https://gemini.google.com/u/1/gem/3b572e310813/17b69b342445e583
- 模式: Pro
- Date: 2026-04-21

## 答案摘要

### 1. SUPPAE 作用

- **补充限定词域** (Supplemental Qualifiers for AE) — 存储无法映射到 SDTMIG 标准变量的非标 qualifier
- 通过 **IDVAR** (通常 AESEQ) + **IDVARVAL** 与 AE 域实现一对一/多对一关联
- 保持主域标准结构不被破坏

### 2. 何时走 SUPPAE (标准优先, 非标入补)

| 规则 | 说明 |
|------|------|
| 非 SDTMIG 定义变量 | 如 AESI (特殊兴趣不良事件), Spec 无对应变量 |
| 非通用 Qualifier | AE 域 Spec 已有 AESEV/AEREL 等不走 SUPPAE |
| 严禁伪造变量名 | 不符合 AE.xxxx 命名规范的必须入 SUPPAE |

### 3. 典型例子: AESI 标记

**场景**: Sponsor 需收集某 AE 是否为 "Adverse Event of Special Interest", AE 域无该变量.

**SUPPAE 数据示例**:

| RDOMAIN | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
|---------|-------|----------|------|--------|------|
| AE | AESEQ | 10 | AESI | Adverse Event of Special Interest | Y |

**三字段解析**:
- **QNAM** = `AESI` (Qualifier Name, ≤8 字符短代号)
- **QLABEL** = `Adverse Event of Special Interest` (Label, ≤40 字符描述)
- **QVAL** = `Y` (实际观测值)

**关联关系**: IDVAR=`AESEQ` + IDVARVAL=`10` → 指向 AE 域 AESEQ=10 的那条 AE 记录.

### 4. 源路径 (CO-3)

- knowledge_base/chapters/ch08_supplemental_qualifiers.md §8.4.1 (General Assumptions for Supplemental Qualifiers)
- knowledge_base/domains/AE/spec.md (辅助参考 — 确认标准变量范围)

## v2.1 判据对齐

| PASS 判据 | 结果 |
|----------|------|
| SUPPAE 存标准 AE 域未定义的补充变量 (非标存储本质) | ✅ 明确 |
| 标准 AE 变量能放下的不走 SUPPAE (避免重复) | ✅ "标准优先, 非标入补"原则 |
| 典型例子 (AESI/AERESPPD/AECOV19 类有效即可) | ✅ AESI 合格 |
| QNAM = 短代号 (≤8 字符) | ✅ AESI 4 字符 |
| QLABEL = Label 描述 (≤40 字符) | ✅ "Adverse Event of Special Interest" 符合 |
| QVAL = 实际观测值 | ✅ "Y" 明确 |
| 提及 RDOMAIN/USUBJID/IDVAR/IDVARVAL 结构变量 (但不作 example 核心) | ✅ 表格列给出 + 解释 |
| 源路径 CO-3 (ch08 §8.4.1 + AE spec) | ✅ 合规 |

| FAIL 判据 | 结果 |
|----------|------|
| 把 AE 标准变量 (如 AESEV) 当 SUPPAE 示例 (错位) | ✅ 未触 |
| 臆造 QNAM 用 "AE" 前缀超 8 字符 | ✅ 未触 (AESI 仅 4 字符) |
| 不解释 SUPPAE 的"非标存储"本质 | ✅ 未触 (§1 明确解释) |

## 注意

- 示例 QNAM="AESI" 以 "AE" 开头但总长 ≤8 字符, 符合 SDTM 命名规范 (FAIL 判据针对的是超 8 字符情形)
- 表格后 "Export to Sheets" 是 Gemini UI 的本地化按钮, 不影响答案内容

## Verdict: **PASS** (1.0 分)

主判据全通过: SUPPAE 非标存储本质 ✅ / 标准优先非标入补原则 ✅ / AESI 典型例子 ✅ / QNAM/QLABEL/QVAL 三字段完整 ✅ / 8 字符限制 ✅ / 40 字符限制 ✅ / IDVAR=AESEQ 关联关系 ✅ / CO-3 源路径 ✅.

AESI 例子选择合理 (真实 Sponsor 场景高频使用), 三字段 + 关联键结构完整展示. ch08 §8.4.1 SUPP 通用章节引用准确.
