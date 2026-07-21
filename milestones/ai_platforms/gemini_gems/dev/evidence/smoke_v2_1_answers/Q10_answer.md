# Q10 Answer — RELREC vs SUPPAE/SUPPCM 选择

- URL: https://gemini.google.com/u/1/gem/3b572e310813/35cc6e1d775de61c
- 模式: Pro
- Date: 2026-04-21

## 答案摘要

### 1. 结论: 选 **RELREC** (非 SUPP)

### 2. 选择理由 (三条)

| 理由 | 说明 |
|------|------|
| **记录间关联** | RELREC 核心功能 — 建立不同域/同域内特定记录间逻辑关联; AE (头晕) 与 CM (复方降压药) 有因果关系, 是典型记录级关联 |
| **多对多支持** | RELREC 灵活处理"一 AE 多 CM 引起"或"一 CM 多 AE"复杂情况, 无需 SUPP-- 定义复杂非标变量 |
| **避免冗余** | SUPP-- 存 CMSEQ 这类交叉引用 ID 导致查询复杂; RELREC 使用标准 IDVAR/IDVARVAL 结构, 工具兼容性更好 |

### 3. RELREC vs SUPP-- 功能差异

| 特性 | RELREC | SUPP-- |
|------|--------|--------|
| **主要定位** | 建立联系 — 描述记录间逻辑关系 | 补充属性 — 为某记录增加标准变量外信息 |
| **数据结构** | IDVAR + IDVARVAL 指向目标记录 (--SEQ) | QNAM + QVAL 存具体补充数据 |
| **场景示例** | AE 与引起它的 CM 关联; AE 与 LB 跨域关联 | AE 的 CTCAE Grade (若非标变量); CM 具体给药频率补充 |
| **业务语义** | "这条 AE 和那条 CM 是相关的" | "这条记录有以下补充特征" |

### 4. RELREC 映射示例

| STUDYID | DOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|---------|--------|---------|-------|----------|---------|-------|
| XYZ | RELREC | 001 | AESEQ | 1 | CAUSAL | 1 |
| XYZ | RELREC | 001 | CMSEQ | 5 | CAUSAL | 1 |

**关键机制**: 通过相同 `RELID=1` 将 AESEQ=1 和 CMSEQ=5 两条记录绑定.

### 5. 源路径 (CO-3)

- knowledge_base/chapters/ch04_general_assumptions.md §4.1.8 (RELREC 规则)
- knowledge_base/domains/RELREC/spec.md (域定义)
- knowledge_base/business_scenarios_and_cross_domain.md §1.10 (跨域关联实践)

## v2.1 判据对齐

| PASS 判据 | 结果 |
|----------|------|
| 选 **RELREC** (非 SUPP) | ✅ 明确 |
| RELREC 负责跨域记录/同域跨记录之间的关系 | ✅ 明确 "记录间关联" 定位 |
| SUPP-- 负责单条记录补充非标变量, 不是跨记录关系 | ✅ 差异表明确 |
| 本场景 = AE + CM 两条独立记录之间有因果, 正是 RELREC 设计目的 | ✅ 理由 1 命中 |
| 提 RELREC 典型字段: IDVAR / IDVARVAL / RELID / RELTYPE | ✅ 表格给出 |
| 源路径 CO-3 (ch04 §4.1.8 + RELREC spec + business §1.10) | ✅ 合规 |

| FAIL 判据 | 结果 |
|----------|------|
| 选 SUPPAE 存 (错位) | ✅ 未触 |
| 不识别 RELREC 跨域关系本质 | ✅ 未触 |
| RELREC 和 SUPP-- 作用说反 | ✅ 未触 |

## 小错注意 (minor)

- 示例表格列 `DOMAIN` 值 "RELREC" (SDTM 通用 DOMAIN 变量, 正确), 但**未单列 RDOMAIN 字段** (RELREC 必含 Req 变量, 指向关联记录所在域如 "AE" / "CM"). 标准 RELREC 表应当:

  | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
  |---------|---------|---------|-------|----------|---------|-------|
  | XYZ | AE | 001 | AESEQ | 1 | ... | 1 |
  | XYZ | CM | 001 | CMSEQ | 5 | ... | 1 |

- 属结构细节小错, 不影响主判据 PASS. (RELREC 必 Req 变量: STUDYID, RDOMAIN, USUBJID, IDVAR, IDVARVAL, RELID)

## Verdict: **PASS** (1.0 分)

主判据全通过: RELREC 选择 ✅ / 跨记录关联本质 ✅ / SUPP-- 补充属性定位 ✅ / 多对多支持 ✅ / IDVAR+IDVARVAL+RELID 绑定机制 ✅ / RELTYPE=CAUSAL 业务语义 ✅ / CO-3 源路径 ✅.

RDOMAIN 字段小错为结构细节疏漏, 不影响核心判据. 整体答案清晰, 差异对比表和映射示例表两张结构化展示对 SDTM 实施者友好.
