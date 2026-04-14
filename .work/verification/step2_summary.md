# Step 2 验证总表 — examples.md

> 生成日期: 2026-04-14
> 验证来源: SDTMIG v3.4 PDF
> 方法: Sonnet 并行对比 + Opus 修复

---

## 汇总统计

| 项目 | 数量 |
|------|------|
| 验证域总数 | 63 |
| PASS（无问题） | 33 |
| FAIL → 已修复 | 30 |
| 未发现遗留问题 | 0 |

---

## 逐域验证结果总表

| # | 组 | Domain | PDF 页码 | 结果 | 问题数 | 主要问题概述 |
|---|----|---------|---------:|------|--------|-------------|
| 1 | 01 | AE | 140-142 | ✅ PASS | 0 | — |
| 2 | 01 | AG | 95-97 | ✅ PASS（修复后） | 1 | Example 2 ag.xpt 缺 AGDOSU 列 |
| 3 | 01 | BE | 145-148 | ✅ PASS（修复后） | 3 | 缺 suppbe.xpt；bs.xpt Row 2/3 数据错误 |
| 4 | 02 | BS | 198-199 | ✅ PASS | 0 | — |
| 5 | 02 | CE | 151-155 | ✅ PASS | 0 | — |
| 6 | 02 | CM | 101-103 | ✅ PASS | 0 | — |
| 7 | 03 | CO | 61-62 | ✅ PASS | 0 | — |
| 8 | 03 | CP | 208-220 | ✅ PASS（修复后） | 2 | Example 1a CPMRKSTR/CPRESTYP 数据错误 |
| 9 | 03 | CV | 289 | ✅ PASS（修复后） | 1 | Example 2 多余 NCVALTYP 列 |
| 10 | 04 | DA | 181-182 | ✅ PASS（修复后） | 3 | Example 1/2 缺 DASCAT 列；Example 3 缺 DASPID 列 |
| 11 | 04 | DD | 184-185 | ✅ PASS | 0 | — |
| 12 | 04 | DM | 68-78 | ✅ PASS（修复后） | 2 | Example 4/6 CRF Metadata 不完整 |
| 13 | 05 | DS | 158-167 | ✅ PASS（修复后） | 3 | Example 10 缺4张表；Example 11 缺 ta.xpt 及说明文字 |
| 14 | 05 | DV | 179 | ✅ PASS | 0 | — |
| 15 | 05 | EC | 111-120 | ✅ PASS（修复后） | 2 | Example 7 ECLNKID Row 2/4 缺时间戳 |
| 16 | 06 | EG | 189-192 | ✅ PASS（修复后） | 3 | Example 2 描述错误；Example 3 仅3行(应24行)；Example 4 列序错误 |
| 17 | 06 | EX | 111-120 | ✅ PASS | 0 | — |
| 18 | 06 | FA | 367-375 | ✅ PASS（修复后） | 3 | Example 1/4/6 各缺关联数据集 |
| 19 | 07 | FT | 323-324 | ✅ PASS（修复后） | 2 | Row 6 FTBLFL 空；缺 suppft.xpt |
| 20 | 07 | GF | 224-228 | ✅ PASS（修复后） | 1 | Example 3 用占位符替代实际16行表格 |
| 21 | 07 | HO | 169-171 | ✅ PASS（修复后） | 1 | Example 1 Row 6 HOENDTC 日期错误 |
| 22 | 08 | IE | 194 | ✅ PASS | 0 | — |
| 23 | 08 | IS | 233-241 | ✅ PASS（修复后） | 1 | Example 11 缺 is.xpt(9行)+suppis.xpt(5行) |
| 24 | 08 | LB | 246-248 | ✅ PASS（修复后） | 1 | Example 5 列名 ISSPEC → LBSPEC |
| 25 | 09 | MB | 256-262 | ✅ PASS | 0 | — |
| 26 | 09 | MH | 175-178 | ✅ PASS（修复后） | 1 | Example 5 Row 1 MHDTC `2019-011-02` → `2019-11-02` |
| 27 | 09 | MI | 266-267 | ✅ PASS | 0 | — |
| 28 | 10 | MK | 292-294 | ✅ PASS（修复后） | 1 | Example 2 缺 Row 7-16（10行 MCP 关节数据） |
| 29 | 10 | ML | 123-124 | ✅ PASS | 0 | — |
| 30 | 10 | MS | 256-262 | ✅ PASS | 0 | — |
| 31 | 11 | NV | 296-298 | ✅ PASS | 0 | — |
| 32 | 11 | OE | 301-305 | ✅ PASS（修复后） | 2 | Example 3 relrec 列名 IDVARAL；Example 4 缺 suppoe.xpt |
| 33 | 11 | OI | 442-443 | ✅ PASS | 0 | — |
| 34 | 12 | PC | 269-284 | ✅ PASS（修复后） | 3 | 主 pc.xpt(32行)、共享数据集(24行)、Methods A-D relrec 全部缺失 |
| 35 | 12 | PE | 318 | ✅ PASS | 0 | — |
| 36 | 12 | PP | 273-284 | ✅ PASS（修复后） | 4 | PPSEQ 错误；Example 3 缺 Rows 8-14；共享数据集行数错误且用文字替代 |
| 37 | 13 | PR | 127-128 | ✅ PASS | 0 | — |
| 38 | 13 | QS | 328-329 | ✅ PASS（修复后） | 2 | Example 1 缺 Row 9、Row 10 |
| 39 | 13 | RE | 310-312 | ✅ PASS（修复后） | 2 | Example 2 缺 suppre.xpt(4行) + di.xpt(1行) |
| 40 | 14 | RELREC | 429-431 | ✅ PASS | 0 | — |
| 41 | 14 | RELSPEC | 440 | ✅ PASS | 0 | 图形以 ASCII 树呈现，内容正确 |
| 42 | 14 | RELSUB | 439 | ✅ PASS | 0 | — |
| 43 | 15 | RP | 307 | ✅ PASS | 0 | — |
| 44 | 15 | RS | 334-339 | ✅ PASS | 0 | — |
| 45 | 15 | SC | 341-342 | ✅ PASS（修复后） | 3 | Example 2 SCMETHOD 截断；Row 2/3 SCDTC 日期格式渲染错误 |
| 46 | 16 | SE | 81-83 | ✅ PASS | 0 | — |
| 47 | 16 | SM | 85-86 | ✅ PASS（修复后） | 1 | ce.xpt Row 2 CESEQ 1 → 2 |
| 48 | 16 | SR | 378-381 | ✅ PASS（修复后） | 2 | Example 2 缺 ex.xpt(6行)；relrec.xpt(18行) 被文字替代 |
| 49 | 17 | SS | 343 | ✅ PASS（修复后） | 1 | 含 AI 生成虚假说明文字（PDF 该域无 examples） |
| 50 | 17 | SU | 132-133 | ✅ PASS | 0 | — |
| 51 | 17 | SUPPQUAL | 433-434 | ✅ PASS（修复后） | 2 | Example 1 QLABEL 错误；正文变量名 AETRTEMA → AETRTEM |
| 52 | 18 | SV | 89-91 | ✅ PASS | 0 | — |
| 53 | 18 | TA | 386-402 | ✅ PASS | 0 | 7个例子、109行数据全部匹配；含24幅图未收录 |
| 54 | 18 | TD | 415-417 | ✅ PASS | 0 | — |
| 55 | 19 | TE | 405 | ✅ PASS | 0 | — |
| 56 | 19 | TI | 420 | ✅ PASS | 0 | — |
| 57 | 19 | TM | 418 | ✅ PASS | 0 | — |
| 58 | 20 | TR | 353-358 | ✅ PASS（修复后） | 3 | Example 2+3 列名重复(TRSTRESU)；Row 26 TRSTAT/TREASND 空 |
| 59 | 20 | TS | 422-423 | ✅ PASS | 0 | — |
| 60 | 20 | TU | 353-358 | ✅ PASS | 0 | — |
| 61 | 21 | TV | 410-411 | ✅ PASS | 0 | 含1幅访视时间图未收录 |
| 62 | 21 | UR | 314-315 | ✅ PASS（修复后） | 2 | Example 1 表格被文字注释替代(含事实错误)；Example 2 完全缺失 |
| 63 | 21 | VS | 360-361 | ✅ PASS | 0 | — |

---

## 待补全图片清单（验证中记录）

| Domain | Example | PDF 页码 | 图片描述 |
|--------|---------|---------|---------|
| DM | Example 4 | 70-71 | Demographics Sample aCRF for Race（RACE01-07 + 4个子类别分支；红色=SDTMIG，灰色=CDASHIG） |
| DM | Example 5 | 74 | CRF Mock Example（中国民族子分类：HAN CHINESE/MANCHU/MIAO/UYGHUR/ZHUANG） |
| DM | Example 6 | 75 | Demographics Sample aCRF for Race（RACE01-07 + 2个子类别分支） |
| DM | Example 7 | 78 | CRF Mock Example（5种族选项+Unknown+Other；RACE/RACEOTH/RACEREAS） |
| TA | Example 1 | ~387-388 | Study Schema + Prospective/Retrospective/Blinded View（并行设计） |
| TA | Example 2 | ~389-391 | Crossover Trial 4视图 |
| TA | Example 3 | ~392-393 | Multiple Branches 4视图 |
| TA | Example 4 | ~394-396 | Cyclical Chemotherapy 5视图（含显式重复） |
| TA | Example 5 | ~397 | Different Chemo Durations 2视图 |
| TA | Example 6 | ~398 | Different Cycle Durations 2视图 |
| TA | Example 7 | ~400-401 | RTOG 93-09（Schema + Prospective/Retrospective） |
| TV | Example 1 | 409 | "Example Trial 1, Parallel Design Planned Visits"（访视时间轴图） |
| RELSPEC | Example 1 | 440 | Sample Specimen Relationship 层次结构图（已以 ASCII 树替代） |
