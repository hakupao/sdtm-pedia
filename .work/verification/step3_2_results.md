# Step 3-2: 验证 model/ 剩余 4 文件 (02, 03, 05, 06)

> 验证日期: 2026-04-14
> 验证方法: 逐段对照 SDTM_v2.0.pdf 原文，检查完整性（无遗漏）和准确性（无错误）
> 状态: 已完成

---

## 02_observation_classes.md (PDF p11-39)

**结果: FAIL → 修复后 PASS**

### 发现的问题

| # | 类型 | 域/节 | 描述 | 严重性 |
|---|------|-------|------|--------|
| 1 | **错误** | Identifiers | SPDEVID 标注 "AE domain only"，PDF 无此限制 | 中 |
| 2 | **错误** | Identifiers | 幽灵条目 "--REFID (duplicate role...)"，PDF 无此行 | 中 |
| 3 | **错误** | Identifiers | --RDEVID 列入 Identifiers 表，但 PDF 3.1.4 表中无此变量（属于 Ch4 AP） | 中 |
| 4 | **错误** | Identifiers | --RUNID 列入表中，但 PDF 3.1.4 Identifiers 表无此变量 | 中 |
| 5 | 遗漏 | Identifiers | 缺少 NHOID、FETUSID、--RECID（PDF #6,7,12） | 高 |
| 6 | **错误** | Timing | --XSTDY 标签 "Study Day of Start of Crossover Study Day"，PDF 为 "Start Day of Obs Relative to Exposure" | 高 |
| 7 | **错误** | Timing | --CHSTDY 标签 "Change of Study Day"，PDF 为 "Start Day of Obs Rel to Challenge Agent" | 高 |
| 8 | 遗漏 | Timing | 缺少 ~17 个时间变量：TAETORD, EPOCH, RPHASE, RPPLDY, RPPLSTDY, RPPLENDY, --NOMDY, --NOMLBL, --RPDY, --RPSTDY, --RPENDY, --XDY, --XENDY, --CHDY, --CHENDY, --EVLINT, --EVINTX | 高 |
| 9 | **错误** | Findings About | 列入 FAOBJ 变量，但 SDTM v2.0 表仅有 --OBJ | 低 |
| 10 | 不精确 | Findings | 描述为 "100+" 变量，PDF 实际精确为 100 个 | 低 |

### 无错误的部分

- Interventions 43 个变量：名称、标签、角色均准确
- Events 56 个变量：名称、标签、角色均准确
- Findings 关键变量分组（Topic/Result/Normal Range/Specimen）：内容准确
- Findings About --OBJ 变量描述准确

### 修复内容

1. Identifiers 表：删除 --RUNID、--RDEVID、幽灵 --REFID；补充 NHOID、FETUSID、--RECID；修正 SPDEVID 限制
2. Timing 表：补充 17 个缺失变量；修正 --XSTDY、--CHSTDY 标签
3. 删除 FAOBJ 行，修正 Findings 为 "100 variables"

---

## 03_special_purpose_domains.md (PDF p40-49)

**结果: FAIL → 修复后 PASS**

### 发现的问题

| # | 类型 | 域/节 | 描述 | 严重性 |
|---|------|-------|------|--------|
| 1 | **错误** | DM | SUBJID 角色写为 Identifier，PDF 为 **Topic** | 高 |
| 2 | **错误** | DM | RFCSTDTC 标签 "First Study Contact"，PDF 为 "First Challenge Agent Admin" | 高 |
| 3 | **错误** | DM | RFCENDTC 标签 "Last Study Contact"，PDF 为 "Last Challenge Agent Admin" | 高 |
| 4 | **错误** | DM | INVNAM 角色写为 Record Qualifier，PDF 为 Synonym Qualifier (INVID) | 中 |
| 5 | **错误** | DM | SBSTRAIN 角色写为 Record Qualifier，PDF 为 Variable Qualifier (STRAIN) | 中 |
| 6 | **错误** | DM | ARM 角色写为 Record Qualifier，PDF 为 Synonym Qualifier (ARMCD) | 中 |
| 7 | **错误** | DM | ACTARM 角色写为 Record Qualifier，PDF 为 Synonym Qualifier (ACTARMCD) | 中 |
| 8 | 遗漏 | CO | 缺少 POOLID、SPDEVID、COEVALID 变量 | 中 |
| 9 | **错误** | CO | 备注称 "CO domain does not include DOMAIN"，PDF 表中 DOMAIN 为 #2 | 中 |
| 10 | **错误** | SE | TAESSION 应为 TAETORD（变量名错误） | 高 |
| 11 | **错误** | SE | SEDUR 应为 SEUPDES（变量名+标签错误） | 高 |
| 12 | **幽灵域** | SJ | Subject Disease Journey 域不存在于 SDTM v2.0 | 严重 |
| 13 | 遗漏 | — | 缺少 Subject Repro Stages 域（PDF p46-47，10 个变量） | 严重 |
| 14 | **错误** | SM | SMDTC、SMDY、SMEVAL 为幽灵变量（PDF 无此三变量） | 高 |
| 15 | 遗漏 | SM | 缺少 SMSTDY、SMENDY 变量 | 高 |
| 16 | **错误** | DM Key Ref | RFCSTDTC/RFCENDTC 描述与 #2-3 相同错误 | 高 |

### 无错误的部分

- DM: 大部分变量名称、标签、类型准确（38 变量中 31 个正确）
- SV: 16 个变量全部正确（仅顺序与 PDF 不同）

### 修复内容

1. DM: 修正 SUBJID 角色为 Topic；修正 RFCSTDTC/RFCENDTC 标签；修正 INVNAM/SBSTRAIN/ARM/ACTARM 角色
2. CO: 补充 POOLID、SPDEVID、COEVALID；删除错误备注
3. SE: TAESSION→TAETORD, SEDUR→SEUPDES
4. 删除 SJ 域，替换为 Subject Repro Stages（含 10 个变量）
5. SM: 删除 SMDTC/SMDY/SMEVAL，补充 SMSTDY/SMENDY

---

## 05_study_level_data.md (PDF p51-63)

**结果: FAIL → 修复后 PASS**

### 发现的问题

| # | 类型 | 域/节 | 描述 | 严重性 |
|---|------|-------|------|--------|
| 1 | **错误** | TA | TAESSION→TAETORD（变量名错误） | 高 |
| 2 | **错误** | TA | TABESSION→TABRANCH（变量名错误） | 高 |
| 3 | **错误** | TA | TATESSION→TATRANS（变量名错误） | 高 |
| 4 | **错误** | TX | SET 角色写为 Record Qualifier，PDF 为 Synonym Qualifier (SETCD) | 中 |
| 5 | **幽灵** | TT | TTSEQ 不在 PDF 表中 | 高 |
| 6 | **错误** | TT | TTSTGCD→RSTGCD、TTSTAGE→RSTAGE（变量名错误） | 高 |
| 7 | 遗漏 | TT | 缺少 TTDUR 变量 | 中 |
| 8 | **错误** | TP | 几乎全部变量名错误：8/10 个变量名与 PDF 不符 | 严重 |
| 9 | **幽灵** | TD | TDSEQ 不在 PDF 表中 | 高 |
| 10 | **错误** | TD | TDTGTDTC→TDTGTPAI、TDMININT→TDMINPAI、TDMAXINT→TDMAXPAI | 高 |
| 11 | 遗漏 | TD | 缺少 TDNUMRPT 变量 | 高 |
| 12 | **错误** | TS | TSVALNF/TSVALCD/TSVCDREF/TSVCDVER 角色均为 Record Qualifier，PDF 均为 **Result Qualifier** | 高 |
| 13 | **错误** | AC | 变量列表包含 USUBJID/ACSPID/ACTRT/ACDTC（PDF 无此四变量） | 高 |
| 14 | 遗漏 | AC | 缺少 ACVALNF/ACVALCD/ACVCDREF/ACVCDVER | 高 |
| 15 | **错误** | DI | SPDEVID 角色写为 Topic，PDF 为 Identifier | 高 |
| 16 | **幽灵** | DI | DIVALU 不在 PDF 表中 | 高 |
| 17 | 遗漏 | DI | 缺少 DISEQ 变量 | 高 |
| 18 | **错误** | OI | NHOID 角色写为 Topic，PDF 为 Identifier | 高 |
| 19 | **错误** | OI | OITESTCD→OIPARMCD、OITEST→OIPARM、OIORRES→OIVAL（3 个变量名错误） | 高 |

### 无错误的部分

- TE (7 variables): 全部正确
- TV (9 variables): 全部正确
- TI (8 variables): 全部正确
- TM (5 variables): 全部正确

### 修复内容

1. TA: 修正 3 个变量名 + 标签
2. TX: 修正 SET 角色
3. TT: 删除 TTSEQ，修正 RSTGCD/RSTAGE，补充 TTDUR
4. TP: 完整重写变量列表
5. TD: 删除 TDSEQ，修正 3 个变量名，补充 TDNUMRPT
6. TS: 修正 4 个角色
7. AC: 完整重写变量列表
8. DI: 修正 SPDEVID 角色，删除 DIVALU，补充 DISEQ
9. OI: 修正 NHOID 角色，修正 3 个变量名

---

## 06_relationship_datasets.md (PDF p64-69)

**结果: FAIL → 修复后 PASS**

### 发现的问题

| # | 类型 | 域/节 | 描述 | 严重性 |
|---|------|-------|------|--------|
| 1 | **错误** | RELREC | RDOMAIN 角色写为 Record Qualifier，PDF 为 Identifier | 高 |
| 2 | **错误** | RELREC | IDVAR/IDVARVAL 角色写为 Record Qualifier，PDF 为 Identifier | 高 |
| 3 | **错误** | RELREC | RELID 角色写为 Identifier，PDF 为 Record Qualifier | 高 |
| 4 | **幽灵** | RELREC | DOMAIN 不在 PDF RELREC 表中 | 高 |
| 5 | **幽灵** | RELREC | RSUBJID 不在 PDF RELREC 表中 | 高 |
| 6 | 遗漏 | RELREC | 缺少 APID、SPDEVID 变量 | 高 |
| 7 | 遗漏 | SUPP-- | 缺少 APID、SPDEVID 变量 | 高 |
| 8 | **幽灵** | SUPP-- | "QNAM (C-code)" 和 "QLABEL (C-code)" 为幽灵条目 | 中 |
| 9 | **幽灵** | POOLDEF | DOMAIN 不在 PDF 表中 | 高 |
| 10 | 遗漏 | POOLDEF | 缺少 APID 变量 | 高 |
| 11 | **错误** | RELSUB | RSUBJID 角色写为 Record Qualifier，PDF 为 Identifier | 高 |
| 12 | **错误** | RELSUB | RSUBJID 标签 "Related Subject Identifier"，PDF 为 "Related Subject or Pool Identifier" | 高 |
| 13 | **错误** | RELSUB | SREL 角色写为 Topic，PDF 为 Record Qualifier | 高 |
| 14 | **错误** | RELSUB | SREL 标签 "Subject Relationship"，PDF 为 "Subject, Device, or Study Relationship" | 高 |
| 15 | **幽灵** | RELSUB | DOMAIN 不在 PDF 表中 | 高 |
| 16 | 遗漏 | RELSUB | 缺少 POOLID 变量 | 高 |
| 17 | **错误** | DR | SPDEVID 角色写为 Record Qualifier，PDF 为 Identifier | 中 |
| 18 | **错误** | APRELSUB | RSUBJID 角色写为 Record Qualifier，PDF 为 Identifier | 高 |
| 19 | **错误** | APRELSUB | RSUBJID 标签错误（同 #12） | 高 |
| 20 | **错误** | APRELSUB | SREL 角色写为 Topic，PDF 为 Record Qualifier | 高 |
| 21 | **错误** | APRELSUB | SREL 标签错误（同 #14） | 高 |
| 22 | **幽灵** | APRELSUB | DOMAIN 不在 PDF 表中 | 高 |
| 23 | 遗漏 | APRELSUB | 缺少 RDEVID 变量 | 高 |
| 24 | **幽灵** | RELSPEC | DOMAIN 不在 PDF 表中 | 高 |
| 25 | **错误** | RELSPEC | SPEC 角色写为 Record Qualifier，PDF 为 Variable Qualifier (REFID) | 中 |
| 26 | **错误** | RELSPEC | PARENT 角色写为 Record Qualifier，PDF 为 Identifier | 中 |
| 27 | 遗漏 | RELSPEC | 缺少 LEVEL 变量 | 高 |

### 系统性模式

- **DOMAIN 幽灵变量**: POOLDEF、RELSUB、APRELSUB、RELSPEC 表中均错误添加了 DOMAIN（PDF 中这些表没有 DOMAIN）
- **APID/SPDEVID 遗漏**: RELREC、SUPP-- 中均缺少 APID 和 SPDEVID
- **RSUBJID/SREL 标签一致性错误**: 在 RELSUB 和 APRELSUB 中重复出现相同的标签错误

### 无错误的部分

- 各表的 STUDYID、USUBJID 基本正确
- SUPP-- 的 QNAM/QLABEL/QVAL/QORIG/QEVAL 角色正确
- Summary 表结构正确

### 修复内容

1. RELREC: 删除 DOMAIN/RSUBJID，补充 APID/SPDEVID，修正 RDOMAIN/IDVAR/IDVARVAL/RELID 角色
2. SUPP--: 补充 APID/SPDEVID，删除 C-code 幽灵条目
3. POOLDEF: 删除 DOMAIN，补充 APID
4. RELSUB: 删除 DOMAIN，补充 POOLID，修正 RSUBJID/SREL 角色和标签
5. DR: 修正 SPDEVID 角色
6. APRELSUB: 删除 DOMAIN，补充 RDEVID，修正 RSUBJID/SREL 角色和标签
7. RELSPEC: 删除 DOMAIN，补充 LEVEL，修正 SPEC/PARENT 角色

---

## 总计

| 文件 | 错误数 | 遗漏数 | 幽灵数 | 总问题数 | 验证前 | 验证后 |
|------|--------|--------|--------|----------|--------|--------|
| 02_observation_classes | 5 | 2 | 2 | 10 | FAIL | PASS |
| 03_special_purpose_domains | 11 | 4 | 1 | 16 | FAIL | PASS |
| 05_study_level_data | 13 | 4 | 3 | 19 | FAIL | PASS |
| 06_relationship_datasets | 16 | 6 | 6 | 27 | FAIL | PASS |
| **合计** | **45** | **16** | **12** | **72** | | |
