# Claude Q8 answer — CT Extensible + MedDRA binding

**Verdict**: PASS+

## (a) Extensible 语义
- **No (Fixed)**: 封闭集, 必须完全匹配 CDISC Term, 不可增/改/删 — sponsor 扩 = conformance 违规
- **Yes**: 开放集, 已发布 Term 首选, 可 addition-only (不可改/删已有, 不可重定义 submission value)
- 无论 Yes/No, study 用到的 permissible values 都要在 Define-XML codelist metadata 列出 (§4.3.1-§4.3.3)

## (b) 例子

**Non-Extensible**:
- C66742 No Yes Response (4): N/Y/U/NA — 123 个 `--` 变量 (AESER/AEPRESP/LBFAST)
- **C66769 Severity (3): MILD/MODERATE/SEVERE** — AESEV
- C66731 Sex — DM.SEX
- C66767 Action Taken — AE.AEACN

**Extensible**:
- C71113 Frequency (101 terms) — DOSFRQ
- C71620 Unit (500+) — --ORRESU/--STRESU
- **C65047 Laboratory Test Code (2536)** — LB.LBTESTCD
- C99079 Epoch (12) — Timing EPOCH

## (c) AETERM vs AESEV — 三层 CT 绑定模式

| 变量 | Role | Core | CT | 实际来源 |
|---|---|---|---|---|
| AETERM | Topic | Req | **空** | verbatim, 不绑任何字典 |
| AELLT | Var Qualifier | Exp | MedDRA | LLT (外部字典) |
| AEDECOD | Synonym Qualifier | Req | MedDRA | PT |
| AESOC | Var Qualifier | Exp | MedDRA | SOC |
| AESEV | Record Qualifier | Perm | **C66769** | CDISC CT Non-Ext |

### 关键区分
1. **AETERM 不绑 CT 也不绑 MedDRA** — CT 列空 (§4.3.6 "topic variable for Events often stored as verbatim text")
2. **AEDECOD/AELLT/AESOC 绑 MedDRA** — MedDRA 是外部字典非 CDISC CT, Define-XML 用 `ExternalCodeList` 声明名+版本 (§4.3.5)
3. **AESEV Non-Ext**: 只能 MILD/MODERATE/SEVERE. 若 CTCAE 5 档 → 放 **AETOXGR** (无 CT 绑定), 不是 AESEV

### 4 层语义映射
| 语义层 | 绑定 | 例 |
|---|---|---|
| Verbatim 原文 | 无 | AETERM, CMTRT |
| 外部字典编码 | MedDRA/WHODrug/LOINC/SNOMED | AEDECOD, CMDECOD, LBLOINC |
| CDISC CT Non-Ext | 固定码表 | AESEV, AESER, SEX |
| CDISC CT Ext | 可扩码表 | LBTESTCD, --DOSFRQ, EPOCH |

## (d) Sponsor 扩 LBTESTCD → Define-XML

LBTESTCD 绑 C65047 (Ext=Yes). Define-XML 需:

1. **Codelist 显式列出 study 用到的所有值** (§4.3.3): sponsor-extended 和 CDISC 原生并列在同一 `<CodeList>`, 通过 `<EnumeratedItem>` 列出
2. **区分原生 vs 扩展** (Define-XML 2.1):
   - 原生 → `nci:ExtCodeID` 指向 NCI C-code
   - 扩展 → 无 `nci:ExtCodeID`, 仅 `CodedValue` + `Decode/TranslatedText`
   - codelist 根节点 `def:StandardOID` → CDISC CT 版本, `def:IsNonStandard` 标识非 CDISC 扩展 (2.1 特性)
3. **同步扩 LBTEST (C67154)**: Ext=Yes, LBTESTCD ≤ 8 字符 / LBTEST ≤ 40 字符, 一一对应 (§4.2.9)
4. **若有 LOINC 映射**: 填 LBLOINC (外部 LOINC 字典), 国际标准可追溯
5. **文档化扩展理由**: Define-XML `<Description>` 或 SDRG 说明 (新型 biomarker / 避免未来冲突)

### Non-Ext 对比
若扩 AESEV (C66769 Non-Ext): 上述全不成立 — conformance 违规, FDA/PMDA 会 reject. 改用 AETOXGR 或 SUPPAE QNAM.

## 源溯源
- ch04 §4.3.1-§4.3.6 → 02_chapters.md
- AE/LB spec → 05_mega_spec.md
- C66742/C66769 → 11a_terminology_high_core.md
- C65047 → **13a Deferred to Phase 7 RAG** (2,536 terms 太大), 完整 Term 见源 knowledge_base/terminology/core/lb_part2.md

## 评分要点
- ✓ (a) Ext=No/Yes + addition-only 精确约束 + 无论 Yes/No 必列 Define-XML
- ✓ (b) 4+4 例子, C-code + term 数 + 用于变量全对
- ✓ (c) **AETERM 不绑 CT 也不绑 MedDRA** 关键判断完整
- ✓ (c) 4 层 CT 绑定语义总表 (Verbatim/外部字典/CDISC Non-Ext/CDISC Ext)
- ✓ (c) AETOXGR 5 档 CTCAE 替代 AESEV 的深度 insight
- ✓ (d) 5 条 Define-XML 具体要求 + 2.1 特性 (nci:ExtCodeID, def:IsNonStandard, StandardOID)
- ✓ (d) LBTESTCD ≤ 8 + LBTEST ≤ 40 具体长度
- ✓ (d) LOINC 映射补充 + Non-Ext 反例对比 + AESEV 扩 → AETOXGR/SUPPAE 正解
- ✓ C65047 Deferred to Phase 7 RAG 坦诚边界
