# Gemini Q9 answer — Pinnacle 21 FAIL 分类

**Verdict**: PASS

## 5 大类 FAIL (Error/Warning)

1. **变量缺失/属性错误**: "Required variable [X] not found" (AESEQ 缺); "Variable length too long" (> 200 字符未拆)
2. **CT 违规**: "Value not found in codelist" (LBNRIND 填 H 而非 HIGH; NY 非扩展字典填自定义值)
3. **时间逻辑/格式**: Start > End; ISO 8601 错 (2024/06/15 应 2024-06-15)
4. **Key 约束/跨域引用**: "Duplicate record"; "ACTARMCD value not found in TA"; USUBJID 在 DM 不存在
5. **衍生/原始冲突**: Study Day --DY mismatch (Day 0 错, RFSTDTC 当日应 Day 1)

## 修 vs 文档化

### 必须修
- Required 变量缺失 / Core=Exp 已收集未映射
- Non-extensible CT 错值
- ISO 8601 格式错 / 明显逻辑颠倒 / Day 0 错
- USUBJID 跨域不一致 / Duplicate / 非法字符

### 文档化 (ADRG / Define-XML)
- Extensible codelist 新增合法值 → Define-XML 声明 + ADRG 说明
- 真实业务临床实测值逻辑反常已核实 → Data Query 文档化
- Exp 变量全空因研究未收集 + 无法衍生 → ADRG 说明

## 源路径
- ch03 §3.2.2 (Conformance)
- ch04 §4.4.3 (Study Day), §4.4.4 (ISO 8601), §8.4 (SUPP--)
- 04_business_scenarios §1.3 (LBNRIND), §1.6 (DM), §1.15 (CT)

## 评分要点
- ✓ 5 类 FAIL (题目要求 5-6 类, 满足最低)
- ✓ Fix vs Document 判据清晰
- ✓ Non-ext 必修 / Ext 新值文档化 正确
- ✓ Day 0 反例具体
- △ 无 Rule ID 示意 (Claude 有 SD10xx)
- △ 无 FDA TRC (Claude 有 TRC 自动拒收层)
- △ 类别数 5 (最低), ChatGPT/Claude 6+
- △ 无 cSDRG 每条 5 字段清单 (Claude 有)

## 与其他平台对比
- ChatGPT PASS+: 6 类 + 三问法决策 + Must Fix / Explain 两篮
- Claude PASS+ (**最强**): 6 类 + Rule ID 示意 + **TRC 自动拒收层** + cSDRG 5 字段 + 边界声明坦诚
- Gemini PASS: 5 类 + 修/文档化清晰, 但无 Rule ID 无 TRC
- NBLM 预期 PUNT (架构 in-KB-only)
