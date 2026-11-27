# T4.1 第三轮补检 — pack_4 (R3_IG34_EQUIV, T76-T100) 审查结果

- 审查者: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T06:35:50Z (`date -u`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round3_v1.0.md` (R3_IG34_EQUIV 层)
- 看过的渲染页: p71 (DM Example 4 aCRF)、p75 (DM Example 6 aCRF)、p118 (EX Example 7 CRF + ec.xpt)、p68 (DM Example 1 dm.xpt 顶部, `pdftoppm -r 220` 裁切)
- 用过的命令: `sed -n` / `cat -n` 读 `work/pdf_pages/ig34_p00{18,32,61,62,68,70,71,72,73,74,75,76,112,117,118,141,201,202,204,311,401,406,417,424,441,449}.txt`; `grep -rnF "<原句>" knowledge_base` 逐句定位; `grep -n "^#" ...` 核所属节; `grep -n ... work/t2_pdf_typo_registry.jsonl`; `pdftoppm -r 220 -f 68 -l 68 -x 0 -y 0 -W 3000 -H 450 -png`

## 逐条判定

| # | atom_id | 层 | 终态 | 判定 | 依据 | 说明 |
|---|---|---|---|---|---|---|
| T76 | `ig34_p0401_a004` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0401.txt:14`; `knowledge_base/domains/TA/examples.md:972` | 实为逐字; 位于 TA Example 7 Trial Design Matrix 前 |
| T77 | `ig34_p0406_a011` | 同 | EQUIVALENT | HOLDS | `ig34_p0406.txt:10-12`; `knowledge_base/domains/TE/examples.md:67` (节 `### Distinguishing Elements, Study Cells, and Epochs` :65, 属 `## Trial Elements Issues` :48) | 实为逐字 |
| T78 | `ig34_p0417_a018` | 同 | EQUIVALENT | HOLDS | `ig34_p0417.txt:24-25`; `knowledge_base/domains/TS/assumptions.md:5` | 实为逐字 (同段含后句 "This domain is not subject oriented.") |
| T79 | `ig34_p0424_a006` | 同 | EQUIVALENT | HOLDS | `ig34_p0424.txt:9-11`; `knowledge_base/domains/TS/assumptions.md:67` (节 `### Use of Null Flavor` :63) | 实为逐字; P43Y / P6M 值一致 |
| T80 | `ig34_p0424_a009` | 同 | EQUIVALENT | HOLDS | `ig34_p0424.txt:15-16`; `knowledge_base/domains/TS/assumptions.md:69` | 实为逐字 |
| T81 | `ig34_p0424_a010` | 同 | EQUIVALENT | HOLDS | `ig34_p0424.txt:16-18`; `knowledge_base/domains/TS/assumptions.md:69` | 实为逐字 |
| T82 | `ig34_p0441_a002` | 同 | EQUIVALENT | HOLDS | `ig34_p0441.txt:2`; `knowledge_base/domains/DI/assumptions.md:5` (节 `## §9 Study References` :3) | 实为逐字. 包内指针 `model/05_study_level_data.md:256` 是另一份文档 (SDTM v2.0) 的近似句, 不是对应处; 真位置在 DI 文件内显式 §9 节 (KB 无 ch09 章节文件) |
| T83 | `ig34_p0448_a013` | 同 | EQUIVALENT | HOLDS | `ig34_p0449.txt:11-12`; `knowledge_base/chapters/ch10_appendices.md:173` | 实为逐字 (PDF 在 p449) |
| T84 | `ig34_p0032_a022` | 同 | EQUIVALENT | HOLDS | `ig34_p0032.txt:41-42` (选项 2 小表); `knowledge_base/chapters/ch04_general_assumptions.md:448-450` | 1 列小表 CMINDC / FRACTURE, 位于选项 2 下, 与 PDF 一致 (包内指针 :456 为后一句 Note) |
| T85 | `ig34_p0071_a013` | 同 | EQUIVALENT | HOLDS | 渲染页 p71 (Example 4 aCRF 的 "BLACK OR AFRICAN AMERICAN" 块); `knowledge_base/domains/DM/examples.md:136,155,172,192` | 信息点: 提示语 "Select each value that applies if the subject answered "BLACK OR AFRICAN AMERICAN". Check all that apply." (:192) / 问题 "Which of the following racial designations best describes you?" (:192) / CRACE11-CRACE17 (:136,:172,:192) / SUPPDM.QVAL 映射句 (:192) / 7 个复选项 AFRICAN…BLACK CENTRAL AMERICAN (:136,:172,:192) / <RACEC codelist> ↔ (RACEC) (:192). 全在 Example 4 内, 一个不少 |
| T86 | `ig34_p0118_a002` | 同 | EQUIVALENT | HOLDS | 渲染页 p118 CRF 表; `knowledge_base/domains/EX/examples.md:343-344` | Intended Dose 两行三访视逐格: V1 粗体 10 mg/kg, V2/V3 粗体 7.5 mg/kg, 与 PDF 粗体选中一致 (KB 去掉项目符号). 原子 verbatim 列序抽错 (原子抽错) |
| T87 | `ig34_p0141_a019` | 同 | EQUIVALENT | HOLDS | `ig34_p0141.txt:35`; `knowledge_base/domains/AE/examples.md:43` (AE Example 3) | 实为逐字, 16 列逐格一致 |
| T88 | `ig34_p0202_a001` | 同 | EQUIVALENT | HOLDS | `ig34_p0202.txt:1-3` (CP 规格表续页重复表头); `knowledge_base/domains/CP/spec.md` (66 个 `### 变量` 节, 每节 Label/Type/Controlled Terms/Role/Core/CDISC Notes 字段) | 续页重复表头, KB 以全库统一的逐变量字段格式承载 7 列 (Variable Name → `###` 标题; Controlled Terms, Codelist or Format¹ → `Controlled Terms` 字段). 与 `t4_gate_raw/pack3.md` #50 (AE 续页表头) 同一做法. 注: 列名缩写、上标 ¹ 无对应 → 见样本外发现 1 |
| T89 | `ig34_p0311_a011` | 同 | EQUIVALENT | HOLDS | `ig34_p0311.txt:12`; `knowledge_base/domains/RE/examples.md:27` (Example 1 di.xpt) | 实为逐字. 对应 Example 1 (:27); :74 是 Example 2 的同样表头 |
| T90 | `ig34_p0311_a028` | 同 | EQUIVALENT | HOLDS | `ig34_p0311.txt:30`; `knowledge_base/domains/RE/examples.md:49` (Example 2 re.xpt) | 实为逐字, 16 列一致 |
| T91 | `ig34_p0018_a014` | 同 | EQUIVALENT | HOLDS | `ig34_p0018.txt:17-18`; `knowledge_base/chapters/ch03_submitting_data.md:38` (§3.2.1) | 实为逐字, 7 格一致 |
| T92 | `ig34_p0018_a022` | 同 | EQUIVALENT | HOLDS | `ig34_p0018.txt:25-26`; `ch03_submitting_data.md:42` | 实为逐字, 7 格一致 |
| T93 | `ig34_p0018_a024` | 同 | EQUIVALENT | HOLDS | `ig34_p0018.txt:27-28`; `ch03_submitting_data.md:43` | 实为逐字, 7 格一致 |
| T94 | `ig34_p0018_a032` | 同 | EQUIVALENT | HOLDS | `ig34_p0018.txt:38-39`; `ch03_submitting_data.md:47` | 实为逐字, 7 格一致 |
| T95 | `ig34_p0018_a042` | 同 | EQUIVALENT | HOLDS | `ig34_p0018.txt:53-56`; `ch03_submitting_data.md:52` | 实为逐字, 7 格一致 (键 7 个变量顺序一致) |
| T96 | `ig34_p0061_a021` | 同 | EQUIVALENT | HOLDS | `ig34_p0061.txt:31`; `knowledge_base/domains/CO/examples.md:13` | 实为逐字 (仅加粗) |
| T97 | `ig34_p0062_a002` | 同 | EQUIVALENT | HOLDS | `ig34_p0062.txt:4-5`; `knowledge_base/domains/CO/examples.md:17` | 实为逐字 (仅加粗) |
| T98 | `ig34_p0068_a006` | 同 | EQUIVALENT | HOLDS | `ig34_p0068.txt:7-9` + 渲染页 p68; `knowledge_base/domains/DM/examples.md:10` (Example 1) | 26 格逐格一致: ABC12301002 / 01002 / 2006-01-15 / 2006-02-28 / 2006-01-15 / 2006-02-28 / 2006-01-04 / 2006-03-26 / 01 / JOHNSON, M / 1955-03-22 / 50 / YEARS / M / WHITE / NOT HISPANIC OR LATINO / P / Placebo / P / Placebo / 空 / 空 / USA. 原子抽错 (原子写 0102、JOHNSON, JANE、1953-03-22, 且缺 RFX 列) |
| T99 | `ig34_p0075_a006` | 同 | EQUIVALENT | HOLDS | 渲染页 p75 (Example 6 aCRF 第 1 行); `knowledge_base/domains/DM/examples.md:303,332` (Example 6) | 信息点: 完成说明 "Study participants should self-report race, with race being asked about after ethnicity." / 问题 "...(More than one choice is acceptable.)" / RACE01 → RACE / 复选项 AMERICAN INDIAN OR ALASKA NATIVE / <RACE codelist> ↔ (RACE): 全在 :332 (Mermaid R1 也有). 包内指针 :180 是 Example 4 的同名行 (Order 1), 本原子属 Example 6 (PDF p76 Order 3 ↔ KB :332 Order 3) |
| T100 | `ig34_p0112_a023` | 同 | EQUIVALENT | HOLDS | `ig34_p0112.txt:24`; `knowledge_base/domains/EX/examples.md:82` | Injection 3 的 Side = RIGHT, 一致 |

## 计数 (R3_IG34_EQUIV, 25 条)

- HOLDS: 25 (备注实为逐字 19 条: T76-T83, T87, T89-T98; 非逐字等价 6 条: T84, T85, T86, T88, T99, T100; 原子抽错注记: T86, T98)
- TYPO_AFFECTED: 0
- NOT_HOLD: 0
- UNVERIFIABLE: 0

## 样本外发现 (不算样本判定, 不修)

1. `knowledge_base/domains/CP/spec.md` 未见 CP 规格表脚注 ¹ "In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses." (PDF `ig34_p0204.txt:24`); 同脚注在 PC / UR / SE / VS / PE / SC / SM 等 spec.md 末有. 未查台账中该脚注原子的标签, 仅记录.
2. `knowledge_base/domains/EX/examples.md:362` "Scheduled dose is represented in mg/kg" ≠ PDF p118 "mg/mL" — 已登记 `B-EX T-6` (KB 写正确值), 不算问题, 仅备查.
