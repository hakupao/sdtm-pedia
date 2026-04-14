# Step 2: Examples.md 验证详细结果

> 验证日期: 2026-04-14
> 状态: 已完成（63 域全部 PASS）
> 汇总总表: [step2_summary.md](step2_summary.md)

## 验证方法

- **检查项**: Example 编号完整、描述文字无截断、表格列名/行数/数值正确、换行层级一致
- **分组**: 按首字母排序，每组 3 域，共 21 组
- **工作流**: 第 01-02 组 Opus 单线程对照；第 03 组起 Sonnet 并行对比 + Opus 修复
- **共享区段**: EX/EC、MB/MS、TU/TR、PC/PP 四对共享 examples，先到域做完整验证，后到域确认一致性

---

## 第 01 组: AE, AG, BE

### AE (Adverse Events) — PASS

- PDF 页码: examples p140-142
- Example 数量: PDF 6 个 / MD 6 个 ✓
- 验证日期: 2026-04-14

| Example | 描述文字 | Row 说明 | 表格 | 结果 |
|---------|---------|---------|------|------|
| 1 | ✓ | Rows 1-2, Row 3 ✓ | ae.xpt 3行×26列 ✓ | PASS |
| 2 | ✓ | Rows 1-2, Row 3 ✓ | ae.xpt 3行×19列 ✓ | PASS |
| 3 | ✓ | (无 Row 说明) ✓ | ae.xpt 2行×12列 ✓ | PASS |
| 4 | ✓ | Row 1, Rows 2-4, Rows 5-6 ✓ | ae.xpt 6行×14列 ✓ | PASS |
| 5 | ✓ | Row 1, Row 2 ✓ | ae.xpt 2行×30列 ✓ | PASS |
| 6 | ✓ | Row 1, Row 2 ✓ | ae.xpt 2行×24列 ✓ | PASS |

图片: 无

---

### AG (Procedure Agents) — FAIL → 已修复

- PDF 页码: examples p95-97
- Example 数量: PDF 2 个 / MD 2 个 ✓
- 验证日期: 2026-04-14

| Example | 描述文字 | Row 说明 | 表格 | 结果 |
|---------|---------|---------|------|------|
| 1 | ✓ | Row 1, Rows 2-4 ✓ | ag.xpt 4行 ✓ | PASS |
| 2 | ✓ | Row 1-3 + 跨域说明 ✓ | cm.xpt 1行 ✓, ag.xpt 1行 **FAIL**, re.xpt 3行 ✓, di.xpt 1行 ✓, relrec.xpt 3行 ✓ | **FAIL → 已修复** |

#### 问题清单

| # | 严重程度 | 问题 | 状态 |
|---|---------|------|------|
| 1 | 中等 | Example 2 ag.xpt 表头缺少 AGDOSU 列（AGDOSE 与 AGDOSFRM 之间），导致 15 列表头对 16 个数据值 | **已修复** |

图片: 无

---

### BE (Biospecimen Events) — FAIL → 已修复

- PDF 页码: examples p145-148
- Example 数量: PDF 2 个 / MD 2 个 ✓
- 验证日期: 2026-04-14

| Example | 描述文字 | Row 说明 | 表格 | 结果 |
|---------|---------|---------|------|------|
| 1 | ✓ | Row 1, Rows 2-4, Row 5 + BS Row 说明 ✓ | be.xpt 5行 ✓, **suppbe.xpt 缺失**, bs.xpt 3行 **FAIL**, relrec.xpt 4行 ✓ | **FAIL → 已修复** |
| 2 | ✓ | Row 1-10 + BS/SUPP/RELSPEC 说明 ✓ | be.xpt 10行 ✓, suppbe.xpt 6行 ✓, bs.xpt 7行 ✓, relspec.xpt 6行 ✓, relrec.xpt 6行 ✓, References ✓ | PASS |

#### 问题清单

| # | 严重程度 | 问题 | 状态 |
|---|---------|------|------|
| 1 | 严重 | Example 1 缺少 suppbe.xpt 表（PDF p145 有 1 行：BESPEC/Specimen Type/TISSUE） | **已修复** |
| 2 | 中等 | Example 1 bs.xpt Row 2 缺少 BSSTRESN 值（应为 -80），导致 18 值对 19 列 | **已修复** |
| 3 | 中等 | Example 1 bs.xpt Row 3 缺少 BSSTRESU 空单元格 + BSDTC 错误（"5-0" 应为 "2005-03-20"） | **已修复** |

图片: 无

---

## 第 02 组: BS, CE, CM

### BS (Biospecimen Findings) — PASS

- PDF 页码: examples p198-199
- Example 数量: PDF 1 个 / MD 1 个 ✓
- 验证日期: 2026-04-14

| Example | 描述文字 | Row 说明 | 表格 | 结果 |
|---------|---------|---------|------|------|
| 1 | ✓ | Rows 1-2, Row 3, Row 4 ✓ | bs.xpt 4行×21列 ✓ | PASS |

图片: 无

---

### CE (Clinical Events) — PASS

- PDF 页码: examples p151-155
- Example 数量: PDF 3 个 / MD 3 个 ✓
- 验证日期: 2026-04-14

| Example | 描述文字 | Row 说明 | 表格 | 结果 |
|---------|---------|---------|------|------|
| 1 | ✓ | Rows 1-3, Row 4 ✓ | CRF表 ✓, ce.xpt 4行×9列 ✓ | PASS |
| 2 | ✓ | Rows 1-2, Row 3-5 ✓ | CRF表 ✓, ce.xpt 5行×13列 ✓ | PASS |
| 3 | ✓ | Row 1-2 (MH), Row 1, Rows 2-3 (CE), Rows 1-2, Rows 3-4 (RELREC) ✓ | CRF表 ✓, mh.xpt 2行 ✓, suppmh.xpt 2行 ✓, ce.xpt 3行 ✓, suppce.xpt 4行 ✓, pr.xpt 3行 ✓, relrec.xpt 4行 ✓ | PASS |

图片: 无

---

### CM (Concomitant/Prior Medications) — PASS

- PDF 页码: examples p101-103
- Example 数量: PDF 5 个 / MD 5 个 ✓
- 验证日期: 2026-04-14

| Example | 描述文字 | Row 说明 | 表格 | 结果 |
|---------|---------|---------|------|------|
| 1 | ✓ | Rows 1-6, Rows 7-9, Row 10 ✓ | cm.xpt 10行×11列 ✓ | PASS |
| 2 | ✓ | (无 Row 说明) ✓ | cm.xpt 2行×7列 ✓ | PASS |
| 3 | ✓ | Row 1-3 ✓ | cm.xpt 3行×10列 ✓ | PASS |
| 4 | ✓ | Rows 1-3, Rows 4-6 ✓ | cm.xpt 6行×11列 ✓ | PASS |
| 5 | ✓ | Row 1-4, Rows 5-6 ✓ | cm.xpt 6行×15列 ✓ | PASS |

图片: 无

---

## 第 03 组: CO, CP, CV

### CO (Comments) — PASS

- PDF 页码: examples p61-62
- Example 数量: PDF 1 个 / MD 1 个 ✓
- 验证日期: 2026-04-14

| Example | 描述文字 | Row 说明 | 表格 | 结果 |
|---------|---------|---------|------|------|
| 1 | ✓ | Rows 1-8 (8条) ✓ | co.xpt 8行×15列 ✓ | PASS |

图片: 无

---

### CP (Cell Phenotyping) — FAIL → 已修复

- PDF 页码: examples p208-220
- Example 数量: PDF 9 个 / MD 9 个 ✓（Example 1 含 1a/1b 两个子例）
- 验证日期: 2026-04-14

| Example | 描述文字 | Row 说明 | 表格 | 结果 |
|---------|---------|---------|------|------|
| 1a | ✓ | Rows 1-3, 4-5, 6-7, 8-11, 12-13, 14-15, Row 16 ✓ | cp.xpt 16行×19列；2处数据错误已修复 | FAIL→修复 |
| 1b | ✓ | Rows 1, 2-3, 4 ✓ | cp.xpt 4行×21列 ✓ | PASS |
| 2 | ✓ | Rows 1-2, 3-4, 5-6, 7-8, 9-11 ✓ | 简化说明 (11行×24列) ✓ | PASS |
| 3 | ✓ | Rows 1-3, 4-5, 6, 7-9, 10-11, 12 ✓ | 简化说明 (12行) ✓ | PASS |
| 4 | ✓ | Rows 1-3, 4-6, 7 ✓ | 简化说明 (7行) ✓ | PASS |
| 5 | ✓ | Rows 1-3, 4-8 ✓ | 简化说明 (8行) ✓ | PASS |
| 6 | ✓ | Rows 1-6, 7-10, 11-14, 15-18, 19-32 ✓ | 简化说明 (32行) ✓ | PASS |
| 7 | ✓ | Rows 1, 2, 3 ✓ | 简化说明 (3行) ✓ | PASS |
| 8 | ✓ | Rows 1-3, 4-6, 7-8, 9-11 ✓ | 简化说明 (11行) ✓ | PASS |
| 9 | ✓ | Row 1, Rows 2-14 ✓ | 简化说明 (14行) ✓ | PASS |

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 1a Row 5 CPMRKSTR | 分母 `CD45+CD3+CD19+CD14-CD56-` 错误（不对应任何标准细胞群） | 改为 `CD45+FSC SSC`（与 Row 2 淋巴细胞 CPMRKSTR 一致） |
| 2 | Example 1a Row 15 CPRESTYP | NK Cells/Leuk 为百分比，误填 NUMBER CONCENTRATION | 改为 NUMBER FRACTION |

图片: 无

---

### CV (Cardiovascular System Findings) — FAIL → 已修复

- PDF 页码: examples p289
- Example 数量: PDF 2 个 / MD 2 个 ✓
- 验证日期: 2026-04-14

| Example | 描述文字 | Row 说明 | 表格 | 结果 |
|---------|---------|---------|------|------|
| 1 | ✓ | (无单独 Row 说明) ✓ | cv.xpt 5行×15列 ✓ | PASS |
| 2 | ✓ | (无单独 Row 说明) ✓ | cv.xpt 8行×18列；多余列已删除 | FAIL→修复 |

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 2 表格列头 | 多余 NCVALTYP 列（PDF 中无此独立列；NCVALTYP 是 Row 1 的 CVTESTCD 值） | 删除多余列，表格从 19 列恢复为 18 列 |

图片: 无

---

## 第 04 组: DA, DD, DM

### DA (Drug Accountability) — FAIL → 已修复

- PDF 页码: examples p181-182
- Example 数量: PDF 3 个 / MD 3 个 ✓
- 验证日期: 2026-04-14

| Example | 描述文字 | Row 说明 | 表格 | 结果 |
|---------|---------|---------|------|------|
| 1 | ✓ | (无 Row 说明) ✓ | da.xpt 6行；缺 DASCAT 列导致列值错位，已修复 | FAIL→修复 |
| 2 | ✓ | (无 Row 说明) ✓ | da.xpt 2行；缺 DASCAT 列导致列值错位，已修复 | FAIL→修复 |
| 3 | 轻微差异已修复 | Rows 1-2, 3-4, 5-6 ✓ | da.xpt 6行；缺 DASPID 列，已修复 | FAIL→修复 |

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 1 表格 | 缺 DASCAT 列（DACAT 与 DAORRES 之间），导致 rows 1-4 DAORRES/DAORRESU/DASTRESC 列值错位 | 添加 DASCAT 列（Bottle A/B），修正 rows 1-4 各结果列值，表格从 18→19 列 |
| 2 | Example 2 表格 | 缺 DASCAT 列，rows 1-2 列值错位 | 添加 DASCAT 列（Drug A/B），修正结果列值，表格从 16→17 列 |
| 3 | Example 3 表格 | 缺 DASPID 列（DAGRPID 与 DATESTCD 之间），值 1/1/2/2/1/1 完全丢失 | 添加 DASPID 列，表格从 16→17 列 |
| 4 | Example 3 描述文字 | "the volume of formula remaining after feeding" | 改为 "the volume remaining after feeding" |

图片: 无

---

### DD (Death Details) — PASS

- PDF 页码: examples p184-185
- Example 数量: PDF 2 个 / MD 2 个 ✓
- 验证日期: 2026-04-14

| Example | 描述文字 | Row 说明 | 表格 | 结果 |
|---------|---------|---------|------|------|
| 1 | ✓ | Rows 1-2, 3-4, 5-7 ✓ | dd.xpt 7行×10列 ✓ | PASS |
| 2 | ✓ | Rows 1-2, Row 3 (ds.xpt) ✓ | ae.xpt 1行×13列 ✓; dd.xpt 1行×10列 ✓; ds.xpt 3行×10列 ✓; relrec.xpt 3行×8列 ✓ | PASS |

图片: 无

---

### DM (Demographics) — FAIL → 已修复

- PDF 页码: examples p68-78
- Example 数量: PDF 7 个 / MD 7 个 ✓
- 验证日期: 2026-04-14

| Example | 描述文字 | Row 说明 | 表格 | 结果 |
|---------|---------|---------|------|------|
| 1 | (无) | (无) | dm.xpt 6行×25列 ✓ | PASS |
| 2 | ✓ | Rows 1-5 (dm), Rows 1-3/4-6/7/8-9/10-11 (se) ✓ | dm.xpt 5行×10列 ✓; se.xpt 11行×8列 ✓ | PASS |
| 3 | ✓ | Rows 1-3 (dm), Rows 1-3/4-5/6-8 (se) ✓ | dm.xpt 3行×10列 ✓; se.xpt 8行×8列 ✓ | PASS |
| 4 | ✓ (含 aCRF 图片说明) | Row 1-3 (dm), Rows 1-2/3-5 (suppdm) ✓ | CRF Metadata 14列已修复; dm.xpt 3行✓; suppdm.xpt 5行✓ | FAIL→修复 |
| 5 | ✓ | Row 1, Rows 2-3 ✓ | dm.xpt 2行✓; suppdm.xpt 3行✓ | PASS |
| 6 | ✓ (含 aCRF 图片说明) | Row 1-3 (dm), Rows 1-3 (suppdm) ✓ | CRF Metadata 展开为全表已修复; dm.xpt 3行✓; suppdm.xpt 3行✓ | FAIL→修复 |
| 7 | ✓ (含 CRF Mock 说明) | Rows 1-2/Row 3/Row 4 (dm), Row 1/Row 2 (suppdm) ✓ | dm.xpt 4行✓; suppdm.xpt 2行✓ | PASS |

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 4 CRF Metadata | 仅 11 列，缺 Pre-specified Value、Query Display、Hidden 三列 | 扩展为 14 列，所有行添加空值，CRACE05-CRACE10 的 Hidden 列填入 CRACE05-CRACE10 |
| 2 | Example 6 CRF Metadata | 用"Same structure as Example 4"摘要替代，未展开全表；丢失 Order 差异（3-9 vs 1-7）及子类别行数量差异 | 展开为独立 14 列完整表（RACE01-07 Order=3-9，仅含 CRACE05-10/11-17 两个子类别行，无 AMERICAN INDIAN 和 WHITE 子类别行） |

**图片记录（新增至图片清单）:**

| Domain | Example | PDF 页码 | 图片描述 |
|--------|---------|---------|---------|
| DM | Example 4 | 第 70-71 页 | Demographics Sample aCRF for Race（含 RACE01-07 及 4 个子类别分支：AMERICAN INDIAN/ALASKA NATIVE、ASIAN、BLACK OR AFRICAN AMERICAN、WHITE）；变量名红色=SDTMIG，灰色=CDASHIG |
| DM | Example 5 | 第 74 页 | CRF Mock Example（中国区域民族子分类：HAN CHINESE/MANCHU/MIAO/UYGHUR/ZHUANG；ETHNIC 变量标注） |
| DM | Example 6 | 第 75 页 | Demographics Sample aCRF for Race（含 RACE01-07 及 2 个子类别分支：ASIAN、BLACK OR AFRICAN AMERICAN；与 Example 4 相比无 AMERICAN INDIAN 和 WHITE 子类别） |
| DM | Example 7 | 第 78 页 | CRF Mock Example（5 种族选项 + Unknown + Other；RACE/RACEOTH/RACEREAS 变量标注） |

---

## 第 05 组: DS, DV, EC

### DS (Disposition) — FAIL → 已修复

- PDF 页码: examples p158-167
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 10 | 缺少 te.xpt(6行)/dm.xpt(2行)/ex.xpt(6行)/se.xpt(8行) | 按 PDF 添加所有缺失表格 |
| 2 | Example 11 | 缺少 ta.xpt(15行) | 按 PDF 添加 ta.xpt |
| 3 | Example 11 | Row 4 说明文字不完整 | 补充"For this study, that was defined as 4 weeks after the start of the last treatment element." |

图片: 无

---

### DV (Protocol Deviations) — PASS

- PDF 页码: examples p179
- 验证日期: 2026-04-14
- 结果: PASS，无问题

图片: 无

---

### EC (Exposure as Collected) — FAIL → 已修复

- PDF 页码: examples p111-120（与 EX 共享）
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 7 Row 2 ECLNKID | `20090213` → `20090213T1000` | 已修复 |
| 2 | Example 7 Row 4 ECLNKID | `20090220` → `20090220T1100` | 已修复 |

图片: 无

---

## 第 06 组: EG, EX, FA

### EG (ECG Test Results) — FAIL → 已修复

- PDF 页码: examples p189-192
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 2 描述文字 | "an RR measurement" → "no RR measurement" | 已修复 |
| 2 | Example 3 eg.xpt | 仅 3 行，PDF 有 24 行 | 扩展为 24 行，VISIT 统一为 VISIT 2 |
| 3 | Example 4 eg.xpt | 列顺序错误，VISITDY 缺失 | 重写表格，恢复正确列序和 EGLOBXFL/VISITNUM/VISIT/VISITDY/EGDTC |

图片: 无

---

### EX (Exposure) — PASS

- PDF 页码: examples p111-120（与 EC 共享）
- 验证日期: 2026-04-14
- 结果: PASS，无问题

图片: 无

---

### FA (Findings About) — FAIL → 已修复

- PDF 页码: examples p367-375
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 1 | 缺少 ex.xpt(1行) | 添加 ex.xpt |
| 2 | Example 4 | 缺少 ae.xpt(2行) + Row 1/Row 2 说明 | 添加 ae.xpt 及说明 |
| 3 | Example 6 | 缺少 ae.xpt、faae.xpt(6行)、relrec.xpt | 添加所有缺失表格 |

图片: 无

---

## 第 07 组: FT, GF, HO

### FT (Functional Tests) — FAIL → 已修复

- PDF 页码: examples p323-324
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 1 Row 6 FTBLFL | 空 → `Y` | 已修复 |
| 2 | Example 1 | 缺少 suppft.xpt(1行) | 添加 suppft.xpt（FTASSTDV=Assistance Device, CANE） |

图片: 无

---

### GF (Genomics Findings) — FAIL → 已修复

- PDF 页码: examples p224-228
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 3 | placeholder → 实际表格缺失 | 按 PDF 添加 16 行 gf.xpt + di.xpt(2行) |

图片: 无

---

### HO (Healthcare Encounters) — FAIL → 已修复

- PDF 页码: examples p169-171
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 1 Row 6 HOENDTC | `2011-06-11` → `2011-09-11` | 已修复 |

图片: 无

---

## 第 08 组: IE, IS, LB

### IE (Inclusion/Exclusion Criteria Not Met) — PASS

- PDF 页码: examples p194
- 验证日期: 2026-04-14
- 结果: PASS

图片: 无

---

### IS (Immunogenicity Specimen Assessments) — FAIL → 已修复

- PDF 页码: examples p233-241
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 11 | 缺少 is.xpt(9行) + suppis.xpt(4行+1行) + 说明文字 | 按 PDF 添加全部内容 |

图片: 无

---

### LB (Laboratory Test Results) — FAIL → 已修复

- PDF 页码: examples p246-248
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 5 表头 | `ISSPEC` → `LBSPEC` | 已修复 |

图片: 无

---

## 第 09 组: MB, MH, MI

### MB (Microbiology Specimen) — PASS

- PDF 页码: examples p256-262（与 MS 共享）
- 验证日期: 2026-04-14
- 结果: PASS

图片: 无

---

### MH (Medical History) — FAIL → 已修复

- PDF 页码: examples p175-178
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 5 Row 1 MHDTC | `2019-011-02` → `2019-11-02` | 已修复 |

图片: 无

---

### MI (Microscopic Findings) — PASS

- PDF 页码: examples p266-267
- 验证日期: 2026-04-14
- 结果: PASS

图片: 无

---

## 第 10 组: MK, ML, MS

### MK (Musculoskeletal System Findings) — FAIL → 已修复

- PDF 页码: examples p292-294
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 2 | 缺少 Row 7-16（10行 METACARPOPHALANGEAL JOINTs 1-5） | 按 PDF 添加 |

图片: 无

---

### ML (Mesh Location) — PASS

- PDF 页码: examples p123-124
- 验证日期: 2026-04-14
- 结果: PASS

图片: 无

---

### MS (Microbiology Susceptibility) — PASS

- PDF 页码: examples p256-262（与 MB 共享）
- 验证日期: 2026-04-14
- 结果: PASS

图片: 无

---

## 第 11 组: NV, OE, OI

### NV (Nervous System Findings) — PASS

- PDF 页码: examples p296-298
- 验证日期: 2026-04-14
- 结果: PASS

图片: 无

---

### OE (Ophthalmic Examinations) — FAIL → 已修复

- PDF 页码: examples p301-305
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 3 relrec.xpt 表头 | `IDVARAL` → `IDVARVAL` | 已修复 |
| 2 | Example 4 | 缺少 suppoe.xpt（OERESCRT=10-point VAS） | 添加 suppoe.xpt(1行) |

图片: 无

---

### OI (Ophthalmic Instrument Examinations) — PASS

- PDF 页码: examples p442-443
- 验证日期: 2026-04-14
- 结果: PASS

图片: 无

---

## 第 12 组: PC, PE, PP

### PC (Pharmacokinetics Concentrations) — FAIL → 已修复

- PDF 页码: examples p269-284（与 PP 共享）
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 1 | 缺少主 pc.xpt 表格（32行） | 按 PDF 添加完整表格 |
| 2 | 共享 PC Dataset | 缺少24行实际数据 | 按 PDF 添加24行表格 |
| 3 | Methods A-D | 缺少全部 relrec.xpt 表格 | 按 PDF 添加 4 组 relrec 表格 |

图片: 无

---

### PE (Physical Examination) — PASS

- PDF 页码: examples p318
- 验证日期: 2026-04-14
- 结果: PASS

图片: 无

---

### PP (Pharmacokinetics Parameters) — FAIL → 已修复

- PDF 页码: examples p273-284（与 PC 共享）
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 1 | 仅16行，PDF有24行；DAY 14 PPSEQ错误(8-16→15-23) | 扩展为24行，修正PPSEQ |
| 2 | Example 2 | 缺少 PPSCAT 列 | 添加 PPSCAT 列 |
| 3 | Example 3 | 缺少 Row 8-14 数据 | 按 PDF 添加 |
| 4 | 共享 PP Dataset | 行数错误(14→12)，用文字描述替代实际表格 | 替换为12行实际表格 |

图片: 无

---

## 第 13 组: PR, QS, RE

### PR (Procedures) — PASS

- PDF 页码: examples p127-128
- 验证日期: 2026-04-14
- 结果: PASS

图片: 无

---

### QS (Questionnaires) — FAIL → 已修复

- PDF 页码: examples p328-329
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 1 | 缺少 Row 9(SWLS0104, CDISC01.100014) | 已添加 |
| 2 | Example 1 | 缺少 Row 10(SWLS0105, CDISC01.100014) | 已添加 |

图片: 无

---

### RE (Drug-Disease Interaction) — FAIL → 已修复

- PDF 页码: examples p310-312
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 2 | 缺少 suppre.xpt(4行) | 按 PDF 添加（REBRESFL/REIRESFL/REIRREA1/REIRREA2） |
| 2 | Example 2 | 缺少 di.xpt(1行) | 按 PDF 添加（SPIROMETER） |

图片: 无

---

## 第 14 组: RELREC, RELSPEC, RELSUB

### RELREC (Related Records) — PASS

- PDF 页码: examples p429-431
- 验证日期: 2026-04-14
- 结果: PASS（4 个 examples 全部匹配）

图片: 无

---

### RELSPEC (Relationship to Reference Specimen) — PASS

- PDF 页码: examples p440
- 验证日期: 2026-04-14
- 结果: PASS（表格完整；图形以 ASCII 树呈现，内容正确）

图片: 1 幅（p440，层次结构图，已用 ASCII 表示）

---

### RELSUB (Related Subjects) — PASS

- PDF 页码: examples p439
- 验证日期: 2026-04-14
- 结果: PASS（dm.xpt 3行 + relsub.xpt 6行 全部匹配）

图片: 无

---

## 第 15 组: RP, RS, SC

### RP (Reproductive System Findings) — PASS

- PDF 页码: examples p307
- 验证日期: 2026-04-14
- 结果: PASS（21行全部匹配，RPDTC 值已正确）

图片: 无

---

### RS (Disease Response) — PASS

- PDF 页码: examples p334-339
- 验证日期: 2026-04-14
- 结果: PASS（4 个 examples，含 Disease Response×3 + Clinical Classifications×1，全部匹配）

图片: 无

---

### SC (Subject Characteristics) — FAIL → 已修复

- PDF 页码: examples p341-342
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 2 Row 1 SCMETHOD | `MENSTRUAL` → `MENSTRUAL HISTORY` | 已修复 |
| 2 | Example 2 Row 2 SCDTC | `20-17-04-01`（PDF渲染问题）→ `2017-04-01` | 已修复 |
| 3 | Example 2 Row 3 SCDTC | `20-17-06-10`（PDF渲染问题）→ `2017-06-10` | 已修复 |

图片: 无

---

## 第 16 组: SE, SM, SR

### SE (Subject Elements) — PASS

- PDF 页码: examples p81-83
- 验证日期: 2026-04-14
- 结果: PASS

图片: 无

---

### SM (Subject Disease Milestones) — FAIL → 已修复

- PDF 页码: examples p85-86
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | ce.xpt Row 2 CESEQ | `1` → `2` | 已修复 |

图片: 无

---

### SR (Skin Response) — FAIL → 已修复

- PDF 页码: examples p378-381
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 2 | 缺少 ex.xpt(6行) | 按 PDF p379 添加 |
| 2 | Example 2 relrec.xpt | 18行表格被文字描述替代 | 按 PDF p380 添加完整18行 |

图片: 无

---

## 第 17 组: SS, SU, SUPPQUAL

### SS (Subject Status) — FAIL → 已修复

- PDF 页码: examples p343
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | 文件内容 | 含 AI 生成的虚假说明文字（非 PDF 内容） | 替换为简洁准确说明（该域在 SDTMIG v3.4 中无 examples） |

图片: 无

---

### SU (Substance Use) — PASS

- PDF 页码: examples p132-133
- 验证日期: 2026-04-14
- 结果: PASS（7行全部匹配）

图片: 无

---

### SUPPQUAL (Supplemental Qualifiers) — FAIL → 已修复

- PDF 页码: examples p433-434
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 1 Row 1 QLABEL | `Other Medically Important SAE` → `Clinically Medically Important SAE` | 已修复 |
| 2 | Example 1 正文 | 变量名 `AETRTEMA` → `AETRTEM` | 已修复 |

图片: 无

---

## 第 18 组: SV, TA, TD

### SV (Subject Visits) — PASS

- PDF 页码: examples p89-91
- 验证日期: 2026-04-14
- 结果: PASS（tv.xpt 8行、ds.xpt 6行、sv.xpt 15行 全部匹配）

图片: 无

---

### TA (Trial Arms) — PASS

- PDF 页码: examples p386-402
- 验证日期: 2026-04-14
- 结果: PASS（7 个 examples，共 109 行 ta.xpt 数据，全部匹配）

图片: 24 幅以上（各 Example 的 Schema/Prospective/Retrospective/Blinded View 图；MD 中未收录）

---

### TD (Trial Disease Assessments) — PASS

- PDF 页码: examples p415-417
- 验证日期: 2026-04-14
- 结果: PASS（3 个 examples，td.xpt 列名/行数正确）

图片: 无

---

## 第 19 组: TE, TI, TM

### TE (Trial Elements) — PASS

- PDF 页码: examples p405
- 验证日期: 2026-04-14
- 结果: PASS（3 个 examples，全部匹配；Transitions 表及 Issues 小节也匹配）

图片: 无

---

### TI (Trial Inclusion/Exclusion Criteria) — PASS

- PDF 页码: examples p420
- 验证日期: 2026-04-14
- 结果: PASS（6行全部匹配）

图片: 无

---

### TM (Trial Disease Milestones) — PASS

- PDF 页码: examples p418
- 验证日期: 2026-04-14
- 结果: PASS（2行全部匹配）

图片: 无

---

## 第 20 组: TR, TS, TU

### TR (Tumor Results) — FAIL → 已修复

- PDF 页码: examples p353-358（与 TU 共享）
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 2+3 表头第15列 | `TRSTRESN`（重复）→ `TRSTRESU` | 已修复 |
| 2 | Example 2 Row 26 TRSTAT | 空 → `NOT DONE` | 已修复 |
| 3 | Example 2 Row 26 TREASND | 空 → `POOR IMAGE INEQUALITY` | 已修复 |

图片: 无

---

### TS (Trial Summary) — PASS

- PDF 页码: examples p422-423
- 验证日期: 2026-04-14
- 结果: PASS（4 个 examples，共 92 行，全部匹配）

图片: 无

---

### TU (Tumor Findings) — PASS

- PDF 页码: examples p353-358（与 TR 共享）
- 验证日期: 2026-04-14
- 结果: PASS（3 个 examples，tu.xpt + supptu.xpt 全部匹配）

图片: 无

---

## 第 21 组: TV, UR, VS

### TV (Trial Visits) — PASS

- PDF 页码: examples p410-411
- 验证日期: 2026-04-14
- 结果: PASS（两个 tv.xpt 表格各5行，全部匹配；Issues 小节完整）

图片: 1 幅（p409，"Example Trial 1, Parallel Design Planned Visits" 访视时间图；MD 中未收录）

---

### UR (Urinary System Findings) — FAIL → 已修复

- PDF 页码: examples p314-315
- 验证日期: 2026-04-14

**问题清单（已修复）:**

| # | 位置 | 问题 | 修复内容 |
|---|------|------|---------|
| 1 | Example 1 | ur.xpt 实际表格缺失，被文字注释替代（且含事实错误：N→"ABSENT"，Y→"PRESENT"） | 按 PDF p314 添加完整5行表格 |
| 2 | Example 2 | 整个 Example 缺失 | 按 PDF p315 添加描述文字 + 3行表格 |

图片: 无

---

### VS (Vital Signs) — PASS

- PDF 页码: examples p360-361
- 验证日期: 2026-04-14
- 结果: PASS（13行×25列全部匹配）

图片: 无

