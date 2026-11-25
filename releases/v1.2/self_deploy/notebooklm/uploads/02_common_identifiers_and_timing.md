# 02_common_identifiers_and_timing

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `02`
> - **Concept**: 9 通用 Req + 24 跨域变量详 (来自 VARIABLE_INDEX.md Section 一)
> - **Merged files**: 0
> - **Words**: 1,080
> - **Chars**: 4,979
> - **Auto source**: `variable_index_common` (merge_sources.py 从 knowledge_base/VARIABLE_INDEX.md §一 抽取 24 跨域通用变量详表 (含 9 个 Core=Req), 无需从 knowledge_base 合并独立文件.)

---
## 跨域通用变量 — 快速识别

本 source 汇集所有在 2+ 域出现的通用变量, 共 24 个. SDTM 数据建模时, 这些变量
**每域重复出现但定义一致**, 是做跨域 join / 做 RELREC / 做 SUPPQUAL 时的锚点.

### 9 个 Core=Req 通用变量 (跨域强制必填, Q1 红线)

| 变量 | 出现域数 | 说明 |
|------|---------|------|
| `STUDYID` | 63 | 所有 SDTM 域首字段, 研究唯一标识, Char type |
| `DOMAIN` | 59 | 除 RELREC/RELSPEC/RELSUB/SUPPQUAL 4 个关系域外都有; 固定 2-3 字母代码 |
| `USUBJID` | 55 | 除 OI/TA/TD/TE/TI/TM/TS/TV 8 个 Trial Design + OI 域外都有 |
| `ETCD` | 3 | SE, TA, TE; Element Code, Topic 变量 |
| `IECAT` | 2 | IE, TI; 纳排标准 category |
| `IETEST` | 2 | IE, TI; 纳排准则全称 |
| `IETESTCD` | 2 | IE, TI; 纳排准则短名 |
| `MIDSTYPE` | 2 | SM, TM; Disease Milestone Type |
| `RDOMAIN` | 3 | CO, RELREC, SUPPQUAL; Related Domain Abbreviation (Req*, 星号表 Core 依域而异) |

### Timing/Visit 家族 (跨域高频, 多数 Perm, 但模式一致)

| 变量 | 出现域数 | Role | Core |
|------|---------|------|------|
| `VISITNUM` | 36 | Timing* | Exp* |
| `VISIT` | 36 | Timing* | Perm* |
| `VISITDY` | 36 | Timing | Perm |
| `EPOCH` | 44 | Timing | Perm* |
| `TAETORD` | 43 | Timing | Perm* |

### Arm/Element 家族 (Trial Design 与实际临床数据桥接)

| 变量 | 出现域数 | 说明 |
|------|---------|------|
| `ARM` | 3 | DM, TA, TV; Description of Planned Arm |
| `ARMCD` | 3 | DM, TA, TV; Planned Arm Code (连 DM 和 Trial Design) |
| `ELEMENT` | 3 | SE, TA, TE; 元素描述 |

### 关系域三件套 (CO/RELREC/SUPPQUAL 共用)

| 变量 | 出现域数 | 说明 |
|------|---------|------|
| `IDVAR` | 3 | CO, RELREC, SUPPQUAL; 被指向变量名 |
| `IDVARVAL` | 3 | CO, RELREC, SUPPQUAL; 被指向变量的值 |
| `RDOMAIN` | 3 | CO, RELREC, SUPPQUAL; 被指向域名 |

### 其他跨域变量

| 变量 | 出现域数 | 说明 |
|------|---------|------|
| `SPDEVID` | 6 | AE, BE, BS, EG, GF, RE; Sponsor Device Identifier |
| `NHOID` | 4 | GF, IS, MS, OI; Non-Host Organism Identifier |
| `FOCID` | 3 | MB, NV, OE; Focus of Study-Specific Interest |
| `MIDS` | 2 | ML, SM; Disease Milestone Instance Name |
| `IESCAT` | 2 | IE, TI; Inclusion/Exclusion Subcategory |

---

## VARIABLE_INDEX.md §一 原始表 (24 跨域变量)

以下为 knowledge_base/VARIABLE_INDEX.md §一 原始内容, 列出每个通用变量的
Label / Type / Role / Core / 具体出现的域名清单.

## 一、通用变量（出现在 2+ 个域，共 24 个）

| 变量名 | 域数 | 出现的域 | Label | Type | Role | Core |
|--------|------|---------|-------|------|------|------|
| STUDYID | 63 | 所有域 | Study Identifier | Char | Identifier | Req |
| DOMAIN | 59 | 除 RELREC, RELSPEC, RELSUB, SUPPQUAL 外所有域 | Domain Abbreviation | Char | Identifier | Req |
| USUBJID | 55 | 除 OI, TA, TD, TE, TI, TM, TS, TV 外所有域 | Unique Subject Identifier | Char | Identifier | Req* |
| EPOCH | 44 | AE, AG, CE, CM, CP, CV, DA, DS, DV, EC, EG, EX, FA, FT, HO, IE, IS, LB, MB, MH, MI, MK, ML, MS, NV, OE, PC, PE, PP, PR, QS, RE, RP, RS, SC, SE, SR, SS, SU, TA, TR, TU, UR, VS | Epoch | Char | Timing | Perm* |
| TAETORD | 43 | AE, AG, CE, CM, CP, CV, DA, DV, EC, EG, EX, FA, FT, HO, IE, IS, LB, MB, MH, MI, MK, ML, MS, NV, OE, PC, PE, PP, PR, QS, RE, RP, RS, SC, SE, SR, SS, SU, TA, TR, TU, UR, VS | Planned Order of Element within Arm | Num | Timing | Perm* |
| VISIT | 36 | AG, BE, BS, CP, CV, DA, EG, FA, FT, GF, IE, IS, LB, MB, MI, MK, ML, MS, NV, OE, PC, PE, PR, QS, RE, RP, RS, SC, SR, SS, SV, TR, TU, TV, UR, VS | Visit Name | Char | Timing* | Perm* |
| VISITDY | 36 | AG, BE, BS, CP, CV, DA, EG, FA, FT, GF, IE, IS, LB, MB, MI, MK, ML, MS, NV, OE, PC, PE, PR, QS, RE, RP, RS, SC, SR, SS, SV, TR, TU, TV, UR, VS | Planned Study Day of Visit | Num | Timing | Perm |
| VISITNUM | 36 | AG, BE, BS, CP, CV, DA, EG, FA, FT, GF, IE, IS, LB, MB, MI, MK, ML, MS, NV, OE, PC, PE, PR, QS, RE, RP, RS, SC, SR, SS, SV, TR, TU, TV, UR, VS | Visit Number | Num | Timing* | Exp* |
| SPDEVID | 6 | AE, BE, BS, EG, GF, RE | Sponsor Device Identifier | Char | Identifier | Perm |
| NHOID | 4 | GF, IS, MS, OI | Non-Host Organism Identifier | Char | Identifier | Perm* |
| ARM | 3 | DM, TA, TV | Description of Planned Arm | Char | Synonym Qualifier | Exp* |
| ARMCD | 3 | DM, TA, TV | Planned Arm Code | Char | Record Qualifier* | Exp* |
| ELEMENT | 3 | SE, TA, TE | Description of Element | Char | Synonym Qualifier | Perm* |
| ETCD | 3 | SE, TA, TE | Element Code | Char | Topic* | Req |
| FOCID | 3 | MB, NV, OE | Focus of Study-Specific Interest | Char | Identifier | Perm |
| IDVAR | 3 | CO, RELREC, SUPPQUAL | Identifying Variable | Char | Record Qualifier* | Perm* |
| IDVARVAL | 3 | CO, RELREC, SUPPQUAL | Identifying Variable Value | Char | Record Qualifier* | Exp* |
| RDOMAIN | 3 | CO, RELREC, SUPPQUAL | Related Domain Abbreviation | Char | Record Qualifier* | Req* |
| IECAT | 2 | IE, TI | Inclusion/Exclusion Category | Char | Grouping Qualifier | Req |
| IESCAT | 2 | IE, TI | Inclusion/Exclusion Subcategory | Char | Grouping Qualifier | Perm |
| IETEST | 2 | IE, TI | Inclusion/Exclusion Criterion | Char | Synonym Qualifier | Req |
| IETESTCD | 2 | IE, TI | Inclusion/Exclusion Criterion Short Name | Char | Topic | Req |
| MIDS | 2 | ML, SM | Disease Milestone Instance Name | Char | Timing* | Perm* |
| MIDSTYPE | 2 | SM, TM | Disease Milestone Type | Char | Record Qualifier* | Req |

> \* Core 值后带星号表示该变量在不同域中 Core 不完全一致，以最常见值显示。

---
