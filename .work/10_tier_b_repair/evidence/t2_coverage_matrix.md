# T2 覆盖矩阵 (T2 后扫描批定范围用)

<!-- chain: E (plans) -->
> 状态: 机械生成 (2026-11-26), 只读 KB. 机器可读: `work/t2_coverage_matrix.json`.

## 复跑命令

```bash
cd /Volumes/DevSSD/Project/sdtm-pedia
python3 .work/10_tier_b_repair/work/scratch/t2/global/t2_coverage_matrix.py
```

脚本在 gitignored 的 `work/scratch/t2/global/`; 输入 = `knowledge_base/**/*.md` (排除 terminology/ INDEX ROUTING VARIABLE_INDEX), `work/pdf_atoms.jsonl` (atom_id 前缀 `ig34_`, 不按 source 字段), `work/pdf_pages/ig34_p*.txt` (atom 缺失时回退), `work/t2_batches/B-*.json`, `evidence/checkpoints/t2_B-*.md` (writer 报告), `git log`.

## 判据

- PDF 节 = IG 编号标题 (HEADING 原子) 起, 至下一个同级或更高级编号标题止; 页 = [起页, 止页].
- 匹配: NFKC + 弯引号/en-em dash/省略号归一 + 去 markdown 标记 + 空白折叠 + 小写. EXACT = 整句子串命中; PARTIAL = 仅首/尾 45 字命中 (改写/截断); 短原子 (<40 字, 如域名列表项) 只在前一原子命中处后 15 行内命中才算 EXACT, 否则 SHORT_UNANCHORED (= 未承载).
- Description / spec 首句 / 脚注: 只在本域目录内找. Description = PDF `XX – Description/Overview` 后首句 EXACT 且 KB 有 `## … XX – Description` 标题. spec 首句 = PDF `xx.xpt, <Domain> — <Class>. One record per …` (原子拆开的自动拼接) 在本域目录 EXACT (spec.md `> Class: | Structure:` 行不算). Assumptions 标题 = KB `##+ … XX –/—/- Assumptions` (H1 `# XX — Assumptions` 不算). 脚注 = PDF 节内 "In this column, an asterisk …" 及 ²/³ 类 NOTE.
- 引言: 本节引言 = 域节标题与其后第一个 HEADING 之间的 SENTENCE/NOTE/LIST_ITEM; 父节引言 = 各祖先编号节同口径. 父节引言全 KB 搜 (不限域目录).
- 批口径 (writer checkpoint 字样): FINAL = (双向全扫 或 完整节页范围) 且 (O20 或 页范围); PARTIAL = 只有其一或仅通用授权; NARROW = 均无. 文件级: F = 批 FINAL 且该文件在 kb_files 或被 checkpoint 点名; P/N = 同条件但批非 FINAL; U = 批开过但该文件不在 kb_files 也未点名; - = 从未开批.
- Fm = 批 FINAL 但该文件不在 kb_files、只被 checkpoint 点名 (几乎全是 spec.md; 通用授权不含 spec.md, O21/O24/O26) → 计入未终版. assumptions.md 被点名即算 F (通用授权明确覆盖).
- 列缩写: 文件 a=assumptions.md e=examples.md s=spec.md; 粗体 = 缺口.

## 已知答案自检 (失败 = 匹配器错, 不是 KB 错)

- PASS O49 DS desc gap
- PASS O45 §6.1.3 intro 0 exact
- PASS O50 §6.2 intro 0 exact
- PASS O39 §6.3 intro 0 exact
- PASS O46 §9 intro in ch10
- PASS O47 §7.3 intro in TV/assumptions
- PASS O31 MO box heading+first sentence absent
- PASS grep -L ".xpt, " 17 dirs + LB (generic --.xpt only) == no own spec sentence in assumptions.md
- PASS grep -L en-dash Assumptions heading 19 dirs minus TE (em dash "## TE — Assumptions") == no ## XX - Assumptions
- PASS CM desc+spec+assum present

## 1. 域矩阵 (64 目录)

| 域 | PDF 节 | 页 | Desc | spec 首句 | Assum 标题 | 脚注 | 本节引言 | 父节引言 (§:EXACT/总) | 批 | 序 | 批口径 | 文件 |
|---|---|---|---|---|---|---|---|---|---|--:|---|---|
| AE | §6.2.1 | 133-143 | Y | Y | Y | **0/1** | - | §6.2:0/8 | B-AE | 12 | NARROW | a:N e:N s:N |
| AG | §6.1.1 | 92-98 | **缺** | **缺** | **缺** | **0/1** | - | §6.1:0/1 | - | - | 无批 | a:- e:- s:- |
| BE | §6.2.2 | 143-148 | Y | Y | Y | NA | 1/1 | §6.2:0/8 | B-BE | 29 | FINAL | a:F e:F s:Fm |
| BS | §6.3.5.2 | 196-199 | Y | Y | Y | **0/1** | 4/4 | §6.3:0/1 §6.3.5:3/3 | B-BS | 31 | FINAL | a:F e:F s:Fm |
| CE | §6.2.3 | 148-155 | Y | Y | Y | **0/1** | - | §6.2:0/8 | B-CE | 50 | FINAL | a:F e:F s:Fm |
| CM | §6.1.2 | 98-103 | Y | Y | Y | **0/1** | - | §6.1:0/1 | B-CM | 47 | FINAL | a:F e:F s:Fm |
| CO | §5.1 | 60-62 | Y | Y | Y | 1/1 | - | §5:2/2 | B-CO | 49 | FINAL | a:F e:F s:Fm |
| CP | §6.3.5.3 | 199-220 | Y | **缺** | Y | **0/1** | - | §6.3:0/1 §6.3.5:3/3 | B-CP | 6 | NARROW | a:N e:N s:U |
| CV | §6.3.7.2 | 286-290 | Y | Y | Y | **0/1** | 1/1 | §6.3:0/1 §6.3.7:4/4 | B-CV | 35 | FINAL | a:F e:F s:Fm |
| DA | §6.3.1 | 180-183 | Y | Y | Y | **0/1** | - | §6.3:0/1 | B-DA | 40 | FINAL | a:F e:F s:Fm |
| DD | §6.3.2 | 183-185 | Y | Y | Y | **0/1** | - | §6.3:0/1 | B-DD | 42 | FINAL | a:F e:F s:Fm |
| DI | §9.1 | 441-442 | NA | NA | NA | **0/1** | 4/4 | §9:4/4 | B-DI | 52 | FINAL | a:F |
| DM | §5.2 | 62-79 | Y | Y | Y | **0/2** | - | §5:2/2 | B-DM | 38 | FINAL | a:F e:F s:Fm |
| DS | §6.2.4 | 155-167 | **缺** | **缺** | **缺** | **0/1** | - | §6.2:0/8 | B-DS | 5 | NARROW | a:U e:N s:U |
| DV | §6.2.7 | 178-180 | Y | Y | Y | **0/1** | - | §6.2:0/8 | B-DV | 51 | FINAL | a:F e:F s:Fm |
| EC | §6.1.3.2 | 107-111 | Y | Y | Y | **0/1** | - | §6.1:0/1 §6.1.3:0/2 | B-EC | 25 | NARROW | a:N e:N s:U |
| EG | §6.3.3 | 185-193 | Y | **缺** | Y | **0/1** | - | §6.3:0/1 | B-EG | 11 | NARROW | a:N e:N s:N |
| EX | §6.1.3.1 | 104-107 | **缺** | **缺** | **缺** | **0/1** | - | §6.1:0/1 §6.1.3:0/2 | B-EX | 7 | NARROW | a:U e:N s:U |
| FA | §6.4.4 | 364-375 | Y | Y | **缺** | **0/1** | - | §6.4:1/1 | B-FA | 18 | NARROW | a:N e:N s:N |
| FT | §6.3.9.1 | 319-324 | Y | Y | Y | **0/1** | - | §6.3:0/1 §6.3.9:7/7 | B-FT | 43 | FINAL | a:F e:F s:Fm |
| GF | §6.3.5.4 | 220-228 | Y | Y | Y | 1/1 | - | §6.3:0/1 §6.3.5:3/3 | B-GF | 13 | NARROW | a:N e:N s:U |
| HO | §6.2.5 | 167-171 | Y | Y | Y | **0/1** | - | §6.2:0/8 | B-HO | 45 | FINAL | a:F e:F s:Fm |
| IE | §6.3.4 | 193-194 | Y | Y | Y | **0/1** | - | §6.3:0/1 | B-IE | 48 | FINAL | a:F e:F s:Fm |
| IS | §6.3.5.5 | 228-241 | Y | Y | Y | **0/1** | - | §6.3:0/1 §6.3.5:3/3 | B-IS | 8 | NARROW | a:N e:N s:N |
| LB | §6.3.5.6 | 241-248 | **缺** | **缺** | Y | 1/1 | - | §6.3:0/1 §6.3.5:3/3 | B-LB | 4 | PARTIAL | a:P e:P s:U |
| MB | §6.3.5.7.1 | 248-252 | Y | **缺** | Y | **0/1** | - | §6.3:0/1 §6.3.5:3/3 §6.3.5.7:0/1 | B-MB | 3 | NARROW | a:U e:N s:N |
| MH | §6.2.6 | 171-178 | Y | Y | Y | **0/1** | - | §6.2:0/8 | B-MH | 19 | FINAL | a:F e:F s:Fm |
| MI | §6.3.5.8 | 263-267 | Y | Y | Y | **0/1** | - | §6.3:0/1 §6.3.5:3/3 | B-MI | 46 | FINAL | a:F e:F s:Fm |
| MK | §6.3.7.3 | 290-294 | Y | Y | Y | **0/1** | - | §6.3:0/1 §6.3.7:4/4 | B-MK | 28 | FINAL | a:F e:F s:Fm |
| ML | §6.1.4 | 121-125 | Y | Y | Y | **0/1** | - | §6.1:0/1 | B-ML | 53 | FINAL | a:F e:F s:F |
| MS | §6.3.5.7.2 | 252-256 | Y | Y | Y | 1/1 | - | §6.3:0/1 §6.3.5:3/3 §6.3.5.7:0/1 | B-MS | 16 | NARROW | a:N e:N s:N |
| NV | §6.3.7.4 | 294-298 | Y | Y | Y | 1/1 | - | §6.3:0/1 §6.3.7:4/4 | B-NV | 34 | FINAL | a:F e:F s:Fm |
| OE | §6.3.7.5 | 298-305 | **缺** | **缺** | **缺** | **0/1** | - | §6.3:0/1 §6.3.7:4/4 | B-OE | 15 | PARTIAL | a:P e:P s:P |
| OI | §9.2 | 442-444 | Y文/无标题 | **缺** | **缺** | **0/1** | - | §9:4/4 | - | - | 无批 | a:- e:- s:- |
| PC | §6.3.5.9.1 | 267-271 | **缺** | Y | Y | **0/1** | - | §6.3:0/1 §6.3.5:3/3 | B-PCPP | 1 | NARROW | a:N e:N s:U |
| PE | §6.3.8 | 315-318 | **缺** | **缺** | Y | **0/1** | - | §6.3:0/1 | - | - | 无批 | a:- e:- s:- |
| PP | §6.3.5.9.2 | 271-275 | **缺** | **缺** | **缺** | **0/1** | - | §6.3:0/1 §6.3.5:3/3 | B-PCPP | 1 | NARROW | a:U e:N s:U |
| PR | §6.1.5 | 125-129 | **缺** | **缺** | **缺** | **0/1** | - | §6.1:0/1 | - | - | 无批 | a:- e:- s:- |
| QS | §6.3.9.2 | 324-329 | Y | Y | Y | **0/1** | - | §6.3:0/1 §6.3.9:7/7 | B-QS | 44 | FINAL | a:F e:F s:Fm |
| RE | §6.3.7.7 | 308-312 | Y | Y | Y | **0/1** | - | §6.3:0/1 §6.3.7:4/4 | B-RE | 32 | FINAL | a:F e:F s:Fm |
| RELREC | §8.2 | 429-430 | Y | Y | NA | **0/1** | 14/14 | §8:18/19 | B-REL | 21 | NARROW | a:N e:N s:N |
| RELSPEC | §8.8 | 439-441 | Y | Y | Y | **0/1** | 1/1 | §8:18/19 | B-REL | 21 | NARROW | a:N e:N s:N |
| RELSUB | §8.7 | 437-439 | Y | Y | Y | **0/1** | - | §8:18/19 | B-REL | 21 | NARROW | a:N e:N s:N |
| RP | §6.3.7.6 | 305-308 | Y | Y | Y | **0/1** | - | §6.3:0/1 §6.3.7:4/4 | B-RP | 23 | FINAL | a:F e:F s:Fm |
| RS | §6.3.9.3 | 329-339 | Y | Y | NA | **0/1** | - | §6.3:0/1 §6.3.9:7/7 | B-RS | 36 | FINAL | a:F e:F s:Fm |
| SC | §6.3.10 | 339-342 | Y | Y | Y | **0/1** | - | §6.3:0/1 | B-SC | 58 | FINAL | a:F e:F s:Fm |
| SE | §5.3 | 79-84 | Y | **缺** | Y | **0/1** | - | §5:2/2 | - | - | 无批 | a:- e:- s:- |
| SM | §5.4 | 84-86 | Y | Y | Y | **0/1** | - | §5:2/2 | B-SM | 33 | FINAL | a:F e:F s:Fm |
| SR | §6.4.5 | 375-382 | Y | Y | Y | **0/1** | - | §6.4:1/1 | B-SR | 20 | PARTIAL | a:P e:P s:P |
| SS | §6.3.11 | 342-344 | **缺** | **缺** | **缺** | **0/1** | - | §6.3:0/1 | - | - | 无批 | a:- e:- s:- |
| SU | §6.1.6 | 129-133 | Y | Y | Y | **0/1** | - | §6.1:0/1 | B-SU | 54 | FINAL | a:F e:F s:Fm |
| SUPPQUAL | §8.4 | 431-434 | NA | Y | NA | **0/1** | 20/20 | §8:18/19 | B-SUPPQUAL | 59 | FINAL | a:F e:F s:Fm |
| SV | §5.5 | 86-92 | Y | Y | Y | **0/1** | - | §5:2/2 | B-SV | 55 | FINAL | a:F e:F s:Fm |
| TA | §7.2.1 | 384-402 | Y | Y | **缺** | **0/1** | - | §7.2:2/2 | B-TA | 24 | NARROW | a:N e:N s:N |
| TD | §7.3.2 | 410-415 | **缺** | **缺** | **缺** | **0/1** | - | §7.3:5/5 | - | - | 无批 | a:- e:- s:- |
| TE | §7.2.2 | 402-407 | Y | Y | Y | **0/1** | - | §7.2:2/2 | B-TE | 30 | FINAL | a:F e:F s:Fm |
| TI | §7.4.1 | 416-417 | Y | Y | Y | **0/1** | - | §7.4:4/4 | B-TI | 56 | FINAL | a:F e:F s:Fm |
| TM | §7.3.3 | 415-415 | Y | Y | **缺** | **0/1** | - | §7.3:5/5 | - | - | 无批 | a:- e:- s:- |
| TR | §6.3.12.2 | 350-353 | Y文/无标题 | **缺** | **缺** | **0/1** | - | §6.3:0/1 §6.3.12:1/1 | B-TR | 2 | NARROW | a:N e:N s:U |
| TS | §7.4.2 | 417-425 | Y | Y | Y | **0/1** | - | §7.4:4/4 | B-TS | 39 | FINAL | a:F e:F s:Fm |
| TU | §6.3.12.1 | 344-350 | Y | Y | Y | **0/1** | - | §6.3:0/1 §6.3.12:1/1 | B-TU | 27 | FINAL | a:F e:F s:Fm |
| TV | §7.3.1 | 407-410 | Y | Y | Y | **0/1** | - | §7.3:5/5 | B-TV | 57 | FINAL | a:F e:F s:Fm |
| UR | §6.3.7.8 | 312-315 | **缺** | **缺** | **缺** | **0/1** | - | §6.3:0/1 §6.3.7:4/4 | - | - | 无批 | a:- e:- s:- |
| VS | §6.3.13 | 358-361 | Y | Y | Y | **0/1** | - | §6.3:0/1 | B-VS | 26 | FINAL | a:F e:F s:Fm |

## 2. 统计

- 缺 Description (14): AG (**缺**), DS (**缺**), EX (**缺**), LB (**缺**), OE (**缺**), OI (Y文/无标题), PC (**缺**), PE (**缺**), PP (**缺**), PR (**缺**), SS (**缺**), TD (**缺**), TR (Y文/无标题), UR (**缺**)
- 缺 spec 首句 (17): AG, CP, DS, EG, EX, LB, MB, OE, OI, PE, PP, PR, SE, SS, TD, TR, UR
- 缺 `## XX – Assumptions` 标题 (PDF 有) (14): AG, DS, EX, FA, OE, OI, PP, PR, SS, TA, TD, TM, TR, UR
- 缺 spec 表脚注 (58 域; 已承载 5: CO, GF, LB, MS, NV): AE, AG, BS, CE, CM, CP, CV, DA, DD, DI, DM, DS, DV, EC, EG, EX, FA, FT, HO, IE, IS, MB, MH, MI, MK, ML, OE, OI, PC, PE, PP, PR, QS, RE, RELREC, RELSPEC, RELSUB, RP, RS, SC, SE, SM, SR, SS, SU, SUPPQUAL, SV, TA, TD, TE, TI, TM, TR, TS, TU, TV, UR, VS
- 本节引言未全承载 (0): 
- 从未开批的域 (9): AG, OI, PE, PR, SE, SS, TD, TM, UR
- 批口径分布: FINAL 36, PARTIAL 4, NARROW 20 (共 60 批)
- 未终版全扫文件 (132): FINAL_MENTION 32, NARROW 47, NO_BATCH 31, PARTIAL 9, UNTOUCHED_IN_BATCH 13 — 清单见 §5.

## 3. §5–§9 章级 / 父节 / 无域节 引言承载 (O17/O39/O45/O46/O50)

| 节 | 标题 | 页 | 编号归属 | 引言原子 | EXACT/PARTIAL/未承载 | KB 位置 (首个命中) | 宿主文件级 / 节页在该批范围内 | 宿主 (先例/候选) |
|---|---|--:|---|--:|---|---|---|---|
| §5 | Models for Special-purpose Domains | 60 | - | 2 | 2/0/0 | `domains/CO/assumptions.md:5` | CO:F/in | CO (已承载) |
| §6 | Domain Models Based on the General Observation C | 92 | - | 0 | 0/0/0 | - | - | - |
| §6.1 | Models for Interventions Domains | 92 | - | 1 | 0/1/0 | `chapters/ch02_fundamentals.md:49` | ch02:N/**out** | 待定 (model/02 或 chapters) |
| §6.1.3 | Exposure Domains | 103 | - | 2 | 0/0/2 | - | - | EX/assumptions.md 顶 (O45) |
| §6.1.3.3 | Exposure/Exposure as Collected Examples | 111 | - | 0 | 0/0/0 | - | - | - |
| §6.2 | Models for Events Domains | 133 | - | 8 | 0/1/7 | `chapters/ch02_fundamentals.md:49` | ch02:N/**out** | 待定 (O50) |
| §6.3 | Models for Findings Domains | 180 | - | 1 | 0/1/0 | `chapters/ch02_fundamentals.md:49` | ch02:N/**out** | 待定 (O39) |
| §6.3.5 | Specimen-based Findings Domains | 194 | - | 3 | 3/0/0 | `domains/LB/assumptions.md:5` | LB:P/**out** | LB |
| §6.3.5.1 | Generic Specimen-based Lab Findings Domain Speci | 194 | - | 7 | 4/3/0 | `domains/LB/assumptions.md:11`, `domains/LB/assumptions.md:12`, `domains/LB/assumptions.md:13` … | LB:P/**out** | LB |
| §6.3.5.7 | Microbiology Domains | 248 | - | 1 | 0/1/0 | `domains/MB/assumptions.md:5` | MB:U/in | MB |
| §6.3.5.7.3 | Microbiology Specimen/Microbiology Susceptibilit | 256 | - | 0 | 0/0/0 | - | - | - |
| §6.3.5.9 | Pharmacokinetics Domains | 267 | - | 0 | 0/0/0 | - | - | PC |
| §6.3.5.9.3 | Relating PP Records to PC Records | 275 | - | 1 | 1/0/0 | `domains/PC/assumptions.md:21` | PC:N/in | PC |
| §6.3.6 | Morphology (MO) | 285 | - | 4 | 1/1/2 | `chapters/ch10_appendices.md:222`, `chapters/ch10_appendices.md:224` | ch10:-/**out** | NV §6.3.7 前 (O31) |
| §6.3.7 | Morphology/Physiology Domains | 285 | - | 4 | 4/0/0 | `domains/NV/assumptions.md:5` | NV:F/**out** | NV |
| §6.3.7.1 | Generic Morphology/Physiology Specification | 285 | - | 7 | 7/0/0 | `chapters/ch08_relationships.md:96`, `domains/NV/assumptions.md:11`, `domains/NV/assumptions.md:12` … | ch08:N/**out** NV:F/**out** | NV |
| §6.3.9 | Questionnaires, Ratings, and Scales (QRS) Domain | 318 | - | 7 | 7/0/0 | `domains/FT/assumptions.md:11`, `domains/FT/assumptions.md:12`, `domains/FT/assumptions.md:14` … | FT:F/**out** | FT |
| §6.3.9.3.1 | Disease Response Use Case | 332 | domains/RS | 0 | 0/0/0 | - | - | - |
| §6.3.9.3.2 | Clinical Classifications Use Case | 336 | domains/RS | 0 | 0/0/0 | - | - | - |
| §6.3.12 | Tumor/Lesion Domains | 344 | - | 1 | 1/0/0 | `domains/TU/assumptions.md:5` | TU:F/in | TU |
| §6.3.12.3 | Tumor Identification/Tumor Results Examples | 353 | - | 0 | 0/0/0 | - | - | - |
| §6.4 | Findings About Events or Interventions | 361 | - | 1 | 1/0/0 | `domains/FA/assumptions.md:19` | FA:N/**out** | FA |
| §6.4.1 | When to Use Findings About Events or Interventio | 361 | - | 25 | 18/7/0 | `domains/FA/assumptions.md:23`, `domains/FA/assumptions.md:25`, `domains/FA/assumptions.md:27` … | FA:N/**out** | FA |
| §6.4.2 | Naming Findings About Domains | 363 | - | 18 | 18/0/0 | `domains/FA/assumptions.md:69`, `domains/FA/assumptions.md:71`, `domains/FA/assumptions.md:73` … | FA:N/**out** | FA |
| §6.4.3 | Variables Unique to Findings About | 364 | - | 5 | 5/0/0 | `domains/FA/assumptions.md:103`, `domains/FA/assumptions.md:105`, `domains/FA/assumptions.md:107` … | FA:N/in | FA |
| §7 | Trial Design Model Datasets | 382 | - | 0 | 0/0/0 | - | - | - |
| §7.1 | Introduction to Trial Design Model Datasets | 382 | - | 0 | 0/0/0 | - | - | - |
| §7.1.1 | Purpose of the Trial Design Model | 382 | - | 11 | 11/0/0 | `domains/TA/assumptions.md:11`, `domains/TA/assumptions.md:13`, `domains/TA/assumptions.md:14` … | TA:N/**out** | TA |
| §7.1.2 | Definitions of Trial Design Concepts | 382 | - | 2 | 2/0/0 | `domains/TA/assumptions.md:27`, `domains/TA/assumptions.md:29` | TA:N/**out** | TA |
| §7.1.3 | Current and Future Contents of the Trial Design  | 383 | - | 20 | 20/0/0 | `domains/TA/assumptions.md:45`, `domains/TA/assumptions.md:46`, `domains/TA/assumptions.md:47` … | TA:N/**out** | TA |
| §7.2 | Experimental Design (TA and TE) | 384 | - | 2 | 2/0/0 | `domains/TA/assumptions.md:76`, `domains/TA/assumptions.md:78` | TA:N/in | TA |
| §7.2.1.1 | Trial Arms Issues | 402 | domains/TA | 0 | 0/0/0 | - | - | - |
| §7.2.2.1 | Trial Elements Issues | 405 | domains/TE | 0 | 0/0/0 | - | - | - |
| §7.3 | Schedule for Assessments (TV, TD, and TM) | 407 | - | 5 | 5/0/0 | `domains/TI/assumptions.md:5`, `domains/TV/assumptions.md:11`, `domains/TV/assumptions.md:7` … | TI:F/**out** TV:F/in | TV (O47) |
| §7.3.1.1 | Trial Visits Issues | 409 | domains/TV | 0 | 0/0/0 | - | - | - |
| §7.4 | Trial Eligibility and Summary (TI and TS) | 415 | - | 4 | 4/0/0 | `domains/TI/assumptions.md:10`, `domains/TI/assumptions.md:5`, `domains/TI/assumptions.md:7` … | TI:F/**out** | TI |
| §7.4.2.1 | Use of Null Flavor | 424 | domains/TS | 37 | 37/0/0 | `domains/TS/assumptions.md:100`, `domains/TS/assumptions.md:101`, `domains/TS/assumptions.md:102` … | TS:F/in | - |
| §7.5 | How to Model the Design of a Clinical Trial | 425 | - | 15 | 15/0/0 | `domains/TI/assumptions.md:40`, `domains/TI/assumptions.md:42`, `domains/TI/assumptions.md:43` … | TI:F/**out** | TI |
| §8 | Representing Relationships and Data | 427 | - | 19 | 18/1/0 | `chapters/ch08_relationships.md:10`, `chapters/ch08_relationships.md:11`, `chapters/ch08_relationships.md:12` … | ch08:N/in | - |
| §8.1 | Relating Groups of Records Within a Domain Using | 427 | - | 6 | 6/0/0 | `chapters/ch08_relationships.md:28`, `chapters/ch08_relationships.md:30` | ch08:N/in | - |
| §8.1.1 | --GRPID Example | 428 | - | 8 | 6/2/0 | `chapters/ch08_relationships.md:34`, `chapters/ch08_relationships.md:36`, `chapters/ch08_relationships.md:38` … | ch08:N/in | - |
| §8.2.1 | Related Records (RELREC) | 429 | domains/RELREC | 0 | 0/0/0 | - | - | - |
| §8.2.2 | RELREC Dataset Examples | 430 | domains/RELREC | 0 | 0/0/0 | - | - | - |
| §8.3 | Relating Datasets | 430 | - | 4 | 4/0/0 | `chapters/ch08_relationships.md:152`, `chapters/ch08_relationships.md:154` | ch08:N/in | - |
| §8.3.1 | RELREC Dataset Relationship Example | 431 | - | 0 | 0/0/0 | - | - | - |
| §8.4.1 | Supplemental Qualifiers (SUPP--) | 432 | domains/SUPPQUAL | 11 | 11/0/0 | `chapters/ch08_relationships.md:195`, `chapters/ch08_relationships.md:212`, `chapters/ch08_relationships.md:214` … | ch08:N/in | - |
| §8.4.2 | Submitting Supplemental Qualifiers in Separate D | 433 | domains/SUPPQUAL | 8 | 7/1/0 | `chapters/ch08_relationships.md:222` | ch08:N/in | - |
| §8.4.3 | SUPP-- Examples | 433 | domains/SUPPQUAL | 1 | 0/1/0 | `chapters/ch08_relationships.md:226` | ch08:N/in | - |
| §8.4.4 | When Not to Use Supplemental Qualifiers | 434 | domains/SUPPQUAL | 5 | 1/4/0 | `chapters/ch08_relationships.md:252`, `chapters/ch08_relationships.md:254`, `chapters/ch08_relationships.md:255` … | ch08:N/in | - |
| §8.5 | Relating Comments to a Parent Domain | 434 | - | 17 | 17/0/0 | `chapters/ch08_relationships.md:263`, `chapters/ch08_relationships.md:265`, `chapters/ch08_relationships.md:267` … | ch08:N/in | - |
| §8.6 | How to Determine Where Data Belong in SDTM-Compl | 435 | - | 0 | 0/0/0 | - | - | - |
| §8.6.1 | Guidelines for Determining the General Observati | 435 | - | 18 | 17/0/1 | `chapters/ch08_relationships.md:286`, `chapters/ch08_relationships.md:288`, `chapters/ch08_relationships.md:290` … | ch08:N/in | - |
| §8.6.2 | Guidelines for Forming New Domains | 435 | - | 11 | 11/0/0 | `chapters/ch08_relationships.md:296`, `chapters/ch08_relationships.md:298`, `chapters/ch08_relationships.md:300` | ch08:N/in | - |
| §8.6.3 | Guidelines for Differentiating Between Intervent | 436 | - | 23 | 15/8/0 | `chapters/ch08_relationships.md:304`, `chapters/ch08_relationships.md:306`, `chapters/ch08_relationships.md:308` … | ch08:N/in | - |
| §9 | Study References | 441 | - | 4 | 4/0/0 | `chapters/ch10_appendices.md:66`, `chapters/ch10_appendices.md:68`, `chapters/ch10_appendices.md:69` | ch10:-/**out** | ch10 (O46) + DI/OI 交叉引用 |

注: §6.1/§6.2/§6.3 的 PARTIAL 命中都是 `chapters/ch02_fundamentals.md:49` (§2.3 "…according to 1 of the 3 SDTM general observation classes: …") — 只是首 45 字前缀相同, 不是该引言句; §6.2 域列表 7 项 SHORT_UNANCHORED. 实质上三处类引言 KB 均无 (与 O39/O50 一致). §6.3.6 MO 框: 标题 + 首句无; 后 2 句在 `chapters/ch10_appendices.md:222-224` (变更附录) 有近似/原句 — O31 "全 KB 无" 需修正为 "MO 框标题与首句无".

宿主 F 但节页不在该域节/批 pdf_ranges 内、且该批 checkpoint 未提及该节号或页 (节正文未核, 须进扫描批): §7.3 `domains/TI/assumptions.md`

## 4. chapters / model 文件

| 文件 | 批 | 序 | 批口径 | 文件级 |
|---|---|--:|---|---|
| `chapters/ch01_introduction.md` | B-ch01 | 22 | NARROW | N |
| `chapters/ch02_fundamentals.md` | B-ch02 | 10 | NARROW | N |
| `chapters/ch03_submitting_data.md` | B-ch03 | 60 | FINAL | F |
| `chapters/ch04_general_assumptions.md` | B-ch04 | 14 | NARROW | N |
| `chapters/ch08_relationships.md` | B-ch08 | 17 | NARROW | N |
| `chapters/ch10_appendices.md` | - | - | 无批 | - |
| `model/01_concepts_and_terms.md` | B-model01 | 9 | NARROW | N |
| `model/02_observation_classes.md` | - | - | 无批 | - |
| `model/03_special_purpose_domains.md` | - | - | 无批 | - |
| `model/04_associated_persons.md` | - | - | 无批 | - |
| `model/05_study_level_data.md` | B-model05 | 37 | PARTIAL | P |
| `model/06_relationship_datasets.md` | B-model06 | 41 | FINAL | F |

## 5. 未终版全扫文件清单

- **NO_BATCH** (31): `domains/AG/assumptions.md`, `domains/AG/examples.md`, `domains/AG/spec.md`, `domains/OI/assumptions.md`, `domains/OI/examples.md`, `domains/OI/spec.md`, `domains/PE/assumptions.md`, `domains/PE/examples.md`, `domains/PE/spec.md`, `domains/PR/assumptions.md`, `domains/PR/examples.md`, `domains/PR/spec.md`, `domains/SE/assumptions.md`, `domains/SE/examples.md`, `domains/SE/spec.md`, `domains/SS/assumptions.md`, `domains/SS/examples.md`, `domains/SS/spec.md`, `domains/TD/assumptions.md`, `domains/TD/examples.md`, `domains/TD/spec.md`, `domains/TM/assumptions.md`, `domains/TM/examples.md`, `domains/TM/spec.md`, `domains/UR/assumptions.md`, `domains/UR/examples.md`, `domains/UR/spec.md`, `chapters/ch10_appendices.md`, `model/02_observation_classes.md`, `model/03_special_purpose_domains.md`, `model/04_associated_persons.md`
- **UNTOUCHED_IN_BATCH** (13): `domains/CP/spec.md`, `domains/DS/assumptions.md`, `domains/DS/spec.md`, `domains/EC/spec.md`, `domains/EX/assumptions.md`, `domains/EX/spec.md`, `domains/GF/spec.md`, `domains/LB/spec.md`, `domains/MB/assumptions.md`, `domains/PC/spec.md`, `domains/PP/assumptions.md`, `domains/PP/spec.md`, `domains/TR/spec.md`
- **NARROW** (47): `domains/AE/assumptions.md`, `domains/AE/examples.md`, `domains/AE/spec.md`, `domains/CP/assumptions.md`, `domains/CP/examples.md`, `domains/DS/examples.md`, `domains/EC/assumptions.md`, `domains/EC/examples.md`, `domains/EG/assumptions.md`, `domains/EG/examples.md`, `domains/EG/spec.md`, `domains/EX/examples.md`, `domains/FA/assumptions.md`, `domains/FA/examples.md`, `domains/FA/spec.md`, `domains/GF/assumptions.md`, `domains/GF/examples.md`, `domains/IS/assumptions.md`, `domains/IS/examples.md`, `domains/IS/spec.md`, `domains/MB/examples.md`, `domains/MB/spec.md`, `domains/MS/assumptions.md`, `domains/MS/examples.md`, `domains/MS/spec.md`, `domains/PC/assumptions.md`, `domains/PC/examples.md`, `domains/PP/examples.md`, `domains/RELREC/assumptions.md`, `domains/RELREC/examples.md`, `domains/RELREC/spec.md`, `domains/RELSPEC/assumptions.md`, `domains/RELSPEC/examples.md`, `domains/RELSPEC/spec.md`, `domains/RELSUB/assumptions.md`, `domains/RELSUB/examples.md`, `domains/RELSUB/spec.md`, `domains/TA/assumptions.md`, `domains/TA/examples.md`, `domains/TA/spec.md`, `domains/TR/assumptions.md`, `domains/TR/examples.md`, `chapters/ch01_introduction.md`, `chapters/ch02_fundamentals.md`, `chapters/ch04_general_assumptions.md`, `chapters/ch08_relationships.md`, `model/01_concepts_and_terms.md`
- **PARTIAL** (9): `domains/LB/assumptions.md`, `domains/LB/examples.md`, `domains/OE/assumptions.md`, `domains/OE/examples.md`, `domains/OE/spec.md`, `domains/SR/assumptions.md`, `domains/SR/examples.md`, `domains/SR/spec.md`, `model/05_study_level_data.md`
- **FINAL_MENTION** (32): `domains/BE/spec.md`, `domains/BS/spec.md`, `domains/CE/spec.md`, `domains/CM/spec.md`, `domains/CO/spec.md`, `domains/CV/spec.md`, `domains/DA/spec.md`, `domains/DD/spec.md`, `domains/DM/spec.md`, `domains/DV/spec.md`, `domains/FT/spec.md`, `domains/HO/spec.md`, `domains/IE/spec.md`, `domains/MH/spec.md`, `domains/MI/spec.md`, `domains/MK/spec.md`, `domains/NV/spec.md`, `domains/QS/spec.md`, `domains/RE/spec.md`, `domains/RP/spec.md`, `domains/RS/spec.md`, `domains/SC/spec.md`, `domains/SM/spec.md`, `domains/SU/spec.md`, `domains/SUPPQUAL/spec.md`, `domains/SV/spec.md`, `domains/TE/spec.md`, `domains/TI/spec.md`, `domains/TS/spec.md`, `domains/TU/spec.md`, `domains/TV/spec.md`, `domains/VS/spec.md`

## 6. 附录: 批口径判定依据 (writer checkpoint 命中行, 每批 ≤3 行)

| 批 | 序 | 口径 | 双向全扫/完整节页范围/O20|页范围/通用授权 | 命中行 |
|---|--:|---|---|---|
| B-PCPP | 1 | NARROW | 0/0/0/0 | - |
| B-TR | 2 | NARROW | 0/0/0/0 | - |
| B-MB | 3 | NARROW | 0/0/0/0 | - |
| B-LB | 4 | PARTIAL | 0/0/1/0 | ¦ (p241 is.xpt / suppis.xpt ×2 PDF_ONLY) ¦ 页范围溢出, 属 IS 批, 不处理 ¦ — ¦ |
| B-DS | 5 | NARROW | 0/0/0/0 | - |
| B-CP | 6 | NARROW | 0/0/0/0 | - |
| B-EX | 7 | NARROW | 0/0/0/0 | - |
| B-IS | 8 | NARROW | 0/0/0/0 | - |
| B-model01 | 9 | NARROW | 0/0/0/0 | - |
| B-ch02 | 10 | NARROW | 0/0/0/0 | - |
| B-EG | 11 | NARROW | 0/0/0/0 | - |
| B-AE | 12 | NARROW | 0/0/0/0 | - |
| B-GF | 13 | NARROW | 0/0/0/0 | - |
| B-ch04 | 14 | NARROW | 0/0/0/0 | - |
| B-OE | 15 | PARTIAL | 1/0/0/0 | ### 双向全扫 (含表格原子) |
| B-MS | 16 | NARROW | 0/0/0/0 | - |
| B-ch08 | 17 | NARROW | 0/0/0/0 | - |
| B-FA | 18 | NARROW | 0/0/0/0 | - |
| B-MH | 19 | FINAL | 1/0/2/0 | - 页范围: 'pdf_ranges' lo=171 已覆盖 §6.2.6 起始页 (p171 标题 / Description / Specification 首句), O20 无缺口; 实扫 p171-178 (p171 前半为 HO, p178 下半为 DV, 均非本批). / ### 双向全扫 (含表格原子; p171 §6.2.6 起 至 p178 §6.2.7 前) |
| B-SR | 20 | PARTIAL | 0/0/1/0 | - pdf_ranges ig34 375-381 covers whole §6.4.5 incl. intro page p375 (O20 OK). Note p375-378 Description/Spec/Assumptions belong to SR/assumptions.md + spec.md (not in kb_ |
| B-REL | 21 | NARROW | 0/0/0/0 | - |
| B-ch01 | 22 | NARROW | 0/0/0/0 | - |
| B-RP | 23 | FINAL | 2/0/1/0 | - pdf_ranges 覆盖核 (O20): RP 节 = p305 "6.3.7.6" 起 (Description/Overview + Spec 表) → p306 (Spec 表续 + Assumptions 1-3) → p307 (Assumption 3a/4 + Examples Ex1); p308 起为 6.3.7. / ### 双向全扫 (含表格原子) / - 双向全扫 (assumptions.md 全文 vs p305-307): PDF→KB: Description/Overview 句 (本次补)、spec 首句 (:9)、Assumptions 1/2/3/ |
| B-TA | 24 | NARROW | 0/0/0/0 | - |
| B-EC | 25 | NARROW | 0/0/0/0 | - |
| B-VS | 26 | FINAL | 1/0/1/0 | - pdf_ranges 核对 (O20): VS §6.3.13 起于 p358 (TR 表尾之后), Description/Specification 在 p358, spec 表 p358-360, Assumptions/Examples p360, Ex1 表跨 p360-361, p361 中部起 §6.4 FA. batc / ## 双向全扫 (p358-361 VS 部分) |
| B-TU | 27 | FINAL | 1/0/2/0 | - **页范围 (O20)**: 'pdf_ranges' lo=344 已含 §6.3.12 节首 (p344 下半: §6.3.12 引言段 + §6.3.12.1 标题 + TU Description 起始), 无缺口. / ### 双向全扫 (含表格原子) |
| B-MK | 28 | FINAL | 1/0/1/0 | - pdf_ranges 核对 (O20): ig34 p290-294 覆盖完整 MK 节: p290 = §6.3.7.3 标题 + Description/Overview + Specification 首句 + 规格表起; p291 规格表续; p292 Assumptions 1-3 + Ex1 叙述; p293 Ex1 表  / ## 双向全扫 (p290-294) |
| B-BE | 29 | FINAL | 1/0/1/0 | - pdf_ranges 覆盖核 (O20): BE 节 = p143 "6.2.2 Biospecimen Events (BE)" (节引言 NOTE + Description/Overview + spec 首句 + spec 表) → p144 (spec 续 + Assumptions 1-6b) → p145 (6c/7 + / ### 双向全扫 (含表格原子) |
| B-TE | 30 | FINAL | 1/0/4/0 | ## O20 页范围 / TE 节实际 PDF 范围 = **p402 (底部 7.2.2 标题 + Description/Overview) – p407 (7.3 之前)**. batch json 'pdf_ranges' 写 404-409 不对 (408-409 是 TV). 本批按 402-407 全扫; batch json 未改 (只登记), 供 / ## 双向全扫 (p402-407) |
| B-BS | 31 | FINAL | 1/0/2/0 | - 节页范围核 (O20): BS 节 = p196 下半 "6.3.5.2 Biospecimen Findings (BS)" (节引言 NOTE + Description/Overview + spec 首句 + spec 表起) → p197 (spec 续) → p198 (spec 末 + Assumptions 1-5 + / ### 双向全扫 (含表格原子) |
| B-RE | 32 | FINAL | 1/0/1/1 | - 白名单: examples.md (batch json) + assumptions.md (主控通用授权: Description/Overview / spec 首句 / 节引言 NOTE, 逐字) / - pdf_ranges 覆盖核 (O20): RE 节 = p308 "6.3.7.7 Respiratory System Findings (RE)" (无节引言 NOTE; Description/Overview + spec 首句 + spec 表) → p309-310 (spec 续 + 脚注 + Assumptions  / ### 双向全扫 (含表格原子) |
| B-SM | 33 | FINAL | 1/0/1/0 | - pdf_ranges 覆盖核 (O20): SM 节 = p84 "5.4 Subject Disease Milestones (SM)" (位于 DM Ex2 dm.xpt Row 2 续表之后; 无节引言 NOTE) → Description/Overview + spec 首句 + spec 表 + 脚注 + Assumpt / ### 双向全扫 (含表格原子) |
| B-NV | 34 | FINAL | 3/0/2/0 | ### 页范围核对 (O20) / - NV/assumptions.md 承载的 §6.3.7 / §6.3.7.1 = p285 (§6.3.7 概述段 + §6.3.7.1 引言 + 5 条 bullet) + **p286** (通用规格表 title + 12 行 + 脚注; 其后 §6.3.7.2 CV). batch pdf_pages 含 285 但**不含 / ### 双向全扫 (含表格原子) |
| B-CV | 35 | FINAL | 1/0/1/0 | - pdf_ranges 覆盖核 (O20): CV 节 = p286 下半页 "6.3.7.2 Cardiovascular System Findings (CV)" (无节引言 NOTE; Description/Overview + spec 首句 + spec 表首行; p286 上半页为 §6.3.7.1 通用表, 属 NV  / ### 双向全扫 (含表格原子) |
| B-RS | 36 | FINAL | 1/0/2/0 | - 节页范围核 (O20): §6.3.9.3 RS = p329 (节标题 + Description/Overview + spec 首句 + spec 表起) → p330-332 (spec 表续; p332 RS 共用引言句 + §6.3.9.3.1 + Disease Response Assumptions 1-2d) →  / ### 双向全扫 (含表格原子) |
| B-model05 | 37 | PARTIAL | 0/0/2/0 | - 页范围核 (O20): §5 起于 p51 ('sv20_p0051.txt' "5 Study-level Data"; p50 为 §4 AP), p64 起 §6 "Datasets for Representing Relationships" → **完整节 = p51-p63**, 与 batch pdf_ranges 5 |
| B-DM | 38 | FINAL | 1/0/3/0 | - **页范围核 (O20)**: §5.2 DM = p62 (节标题 "5.2 Demographics (DM)" + Description/Overview + spec 首句 + spec 表起) → p63-64 (spec 续 + 脚注 1/2) → p65-67 (Assumptions 1-10) → p68-78 ( / ### 双向全扫 (含表格原子) / - F-4: batch json 'pdf_ranges' hi=78 漏 p79 (Ex7 尾) → O20 同型. |
| B-TS | 39 | FINAL | 1/0/2/0 | - **节页范围核 (O20)**: §7.4.2 TS = p417 下半 (标题 "7.4.2 Trial Summary (TS)" + Description/Overview + Specification 首句 + spec 表) → p418 (spec 续 + Assumptions 1-10) → p419 (Assum / ### 双向全扫 (含表格原子) |
| B-DA | 40 | FINAL | 1/0/2/0 | - 页范围核 (O20): p180 顶部为 "6.3 Models for Findings Domains" 章引言 (2 句, 属 §6.3 而非 DA) → "6.3.1 Product Accountability (DA)" 标题 → Description/Overview → Specification 首句 + spec / ### 双向全扫 (含表格原子) |
| B-model06 | 41 | FINAL | 0/1/2/0 | - 页范围核定: SDTM v2.0 §6 起 p64 (标题 "6 Datasets for Representing Relationships"), p70 起 §7 → 完整节页范围 **p64-69** (= batch json pdf_ranges). p63 为 §4 Concept Map 图页, 不属本章. |
| B-DD | 42 | FINAL | 1/0/2/1 | - 白名单: examples.md (batch json, 本批无需改) + assumptions.md (主控通用授权: Description/Overview + spec 首句, 逐字; 结构照 CV/RE/CM 先例) / - 页范围核 (O20): DD 节 = p183 顶 "6.3.2 Death Details (DD)" (无节引言 NOTE; 直接 Description/Overview + Specification 首句 + spec 表 + 脚注) → p184 (Assumptions 1-5 + Examples Ex1 + Ex2  / ### 双向全 |
| B-FT | 43 | FINAL | 1/0/2/2 | - 白名单: examples.md (batch json) + assumptions.md (主控通用授权: Description/Overview + spec 首句 + 节开头引言; 见「需主控定」Q-1 关于 §6.3.9 父节引言的位置) / - 页范围核 (O20): §6.3.9 父节标题 + 引言在 p318 下半 (PE Ex1 之后); §6.3.9.1 FT = p319 (标题 + Description/Overview + spec 首句 + spec 表) → p320 (spec 续 + 脚注) → p321-323 (FT Assumptions 1-2 |
| B-QS | 44 | FINAL | 1/0/2/1 | - 白名单: examples.md (batch json) + assumptions.md (主控通用授权: Description/Overview + spec 首句; 逐词偏差) / - 节页范围核 (O20): §6.3.9.2 QS = p324 (节标题 "6.3.9.2 Questionnaires (QS)" 在 FT suppft 表之后; Description/Overview + spec 首句 + spec 表) → p325-326 (spec 表续 + 脚注) → p326 (QS – Assu / ### 双向全扫 (含表格原子) |
| B-HO | 45 | FINAL | 1/1/2/1 | - 白名单: examples.md (batch json) + assumptions.md (主控通用授权: Description/Overview + spec 首句, CM/BE 先例, 逐字) / - 完整节页范围核 (O20): §6.2.5 HO = p167 下半 ("6.2.5 Healthcare Encounters (HO)" 标题 + Description/Overview + spec 首句 + spec 表起) → p168 (spec 续) → p169 (spec 末 + 脚注 + Assumptions  / ### 双向全扫 (含表格原子) |
| B-MI | 46 | FINAL | 1/1/2/0 | - 完整节页范围 (O20): §6.3.5.8 = p263 下部 (节标题 + MI – Description/Overview 2 句; 上半页属 MB Ex3-4, 不碰) → p264 (MI – Specification 首句 + spec 表) → p265 (spec 表续 + 脚注 + MI – Assumption / ### 双向全扫 (含表格原子) |
| B-CM | 47 | FINAL | 1/0/2/0 | - 页范围核 (O20): CM 节 = p98 "6.1.2 Concomitant/Prior Medications (CM)" (无节引言 NOTE; Description/Overview + spec 首句 + spec 表) → p99-100 (spec 续; p100 Assumptions 1-3a) → p101  / ### 双向全扫 (含表格原子) |
| B-IE | 48 | FINAL | 1/0/1/0 | - pdf_ranges 覆盖核 (O20): IE 节 = p193 "6.3.4 Inclusion/Exclusion Criteria Not Met (IE)" (无节引言 NOTE; Description/Overview + spec 首句 + spec 表 + 脚注) → p194 (Assumptions 1-4 +  / ### 双向全扫 (含表格原子) |
| B-CO | 49 | FINAL | 1/0/2/0 | - 页范围核 (O20): p60 "5 Models for Special-purpose Domains" 章引言 2 句 → "5.1 Comments (CO)" Description/Overview + spec 首句 + spec 表 + 脚注 → p61 Assumptions 1-6 + Examples Ex1 R / ### 双向全扫 (含表格原子) |
| B-CE | 50 | FINAL | 1/0/2/0 | - 节页范围核 (O20): p148 下半 "6.2.3 Clinical Events (CE)" (Description/Overview + spec 首句 + spec 表) → p149-150 (spec 续; Assumptions 1-4) → p151 (5-6; Examples Ex1; Ex2 引言) → p1 / ### 双向全扫 (含表格原子) |
| B-DV | 51 | FINAL | 1/0/2/0 | - 页范围核 (O20): DV 节 = p178 中部 "6.2.7 Protocol Deviations (DV)" (上半页为 MH Ex 末表; p176-177 全为 MH) → Description/Overview + Specification 首句 + spec 表 → p179 (spec 续 + 脚注¹ + As / ### 双向全扫 (含表格原子) |
| B-DI | 52 | FINAL | 1/0/2/0 | - 页范围核 (O20): §9.1 = p441 单页 (p441 顶部 "9 Study References" 章引言 → "9.1 Device Identifiers" 1 段 5 行 → 同页 "9.2 Non-host Organism Identifiers (OI)" 开始). p440 末为 §8 RELSPEC Ex / ### 双向全扫 |
| B-ML | 53 | FINAL | 1/0/2/1 | - 白名单: examples.md + spec.md (batch json) + assumptions.md (主控通用授权: 仅 Description/Overview + spec 首句 + 节引言 NOTE, CM 先例, 逐字) / - 节页范围核 (O20): §6.1.4 ML = p121 (节标题 "6.1.4 Meal Data (ML)" + Description/Overview + spec 首句 + spec 表起) → p122 (spec 表末 + 脚注 + ML – Assumptions 1, 2 起) → p123 (2a/2b/3 +  / # |
| B-SU | 54 | FINAL | 1/0/3/2 | - 白名单: batch json kb_files = examples.md; assumptions.md 按通用主控授权 (Description/Overview + spec 首句, O17) / - 节页范围核 (O20): p129 "6.1.6 Substance Use (SU)" (Description/Overview + spec 首句 + spec 表) → p130-131 (spec 续 + 脚注; Assumptions 1-4) → p132 (5; Examples Ex1 叙述 Row 1-7) → * / ¦ 2 ¦ SU/assumptions.m |
| B-SV | 55 | FINAL | 1/0/2/1 | - 白名单: examples.md (batch json) + assumptions.md (通用授权: Description/Overview + spec 首句 + 节引言 NOTE; 追加授权: assumptions 列表逐词偏差) / - 页范围核 (O20): SV 节 = p86 中部 "5.5 Subject Visits (SV)" (p86 上部为 SM Ex 尾 ce.xpt, 不碰) → Description/Overview + spec 首句 + spec 表 (p86-87) → Assumptions 1-6 (p87) → 6 续-16 (p8 /  |
| B-TI | 56 | FINAL | 1/0/3/0 | - **节页范围核 (O20)**: §7.4 引言 = p415 末 (KB 承载于 TI/assumptions.md 顶部); §7.4.1 TI = p416 (节标题 + "TI – Proposed Removal of Variable TIRL" + Description/Overview + Specification / ### 双向全扫 ('python3 -I /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpa |
| B-TV | 57 | FINAL | 1/0/4/1 | - kb_files: TV/examples.md + 主控通用授权 TV/assumptions.md (Description/spec 首句/§7.3 引言 + assumptions 逐词修) / ## O20 页范围 / batch json 'pdf_ranges' 写 409-412 不对 (p410 下半-412 属 TD). 本批按 407-410 全扫; batch json 未改 (只登记, O20). |
| B-SC | 58 | FINAL | 1/0/2/0 | - 节页范围核 (O20): §6.3.10 SC = p339 下部 (节标题 "6.3.10 Subject Characteristics (SC)" + Description/Overview; 上部为 RS Ex1) → p340 (Specification 首句 + spec 表) → p341 (spec 续 + 脚注  / ### 双向全扫 (含表格原子) |
| B-SUPPQUAL | 59 | FINAL | 1/0/3/0 | - 节页范围 (O20): §8.4 = p431 (节标题 + 前 2 段) → p432 (attributions / 唯一性 / --GRPID 段 + §8.4.1 spec 首句 + spec 表) → p433 (表后 4 段 + §8.4.2 + §8.4.3 Ex1 + Ex2 引言) → p434 (suppqs 表  / ### 双向全扫 (含表格原子) / 3. batch json pdf_ranges (430-432) 偏移, 实际 §8.4 = p431-434 (O20). |
| B-ch03 | 60 | FINAL | 1/0/2/0 | - 页范围核 (O20): §3 = p17 ("3 Submitting Data in Standard Format") → p21 (3.2.2 Conformance 末条); p16 为 §2.7 末, p22 起 §4. batch pdf_ranges 17-21 **完整覆盖** (pdf_pages 只列 17). / ### 叙述双向全扫 (p17-p21) |

## 7. 建议扫描批分组 (每文件只进一批, 按共享父节分组)

| 批 | 范围 | 单元 | 文件数 | 缺口摘要 (Desc/spec/Assum/脚注) |
|---|---|---|--:|---|
| S-INT | §6.1 Interventions (+§6.1.3 引言 O45 → EX 顶) | AG, PR, EX, EC | 12 | AG:DSAF; PR:DSAF; EX:DSAF; EC:F |
| S-EVT | §6.2 Events | AE, DS | 6 | AE:F; DS:DSAF |
| S-SPC1 | §6.3.5 Specimen 上半 | CP, GF, IS, LB | 12 | CP:SF; GF:-; IS:F; LB:DS |
| S-SPC2 | §6.3.5.7 Micro + §6.3.5.9 PK | MB, MS, PC, PP | 12 | MB:SF; MS:-; PC:DF; PP:DSAF |
| S-FND | §6.3.3/§6.3.7/§6.3.8/§6.3.11 | EG, OE, UR, PE, SS | 15 | EG:SF; OE:DSAF; UR:DSAF; PE:DSF; SS:DSAF |
| S-TUFA | §6.3.12 Tumor + §6.4 FA/SR | TR, FA, SR | 9 | TR:DSAF; FA:AF; SR:F |
| S-TDM | §7 Trial Design | TA, TD, TM | 9 | TA:AF; TD:DSAF; TM:AF |
| S-SPREL | §5.3 SE + §8 RELREC/RELSUB/RELSPEC + §9.2 OI | SE, RELREC, RELSUB, RELSPEC, OI | 15 | SE:SF; RELREC:F; RELSUB:F; RELSPEC:F; OI:DSAF |
| S-CH | chapters 未终版 | ch01_introduction.md, ch02_fundamentals.md, ch04_general_assumptions.md, ch08_relationships.md, ch10_appendices.md | 5 | - |
| S-MODEL | model 未终版 (SDTM v2.0) | 01_concepts_and_terms.md, 02_observation_classes.md, 03_special_purpose_domains.md, 04_associated_persons.md, 05_study_level_data.md | 5 | - |
| S-SPEC | FINAL 域 spec.md: 全扫 (Fm 未逐格核, O21) + 表脚注 (先定 O24/O26 统一口径/放置) | BE, BS, CE, CM, CO, CV, DA, DD, DM, DV, FT, HO, IE, MH, MI, MK, ML, NV, QS, RE, RP, RS, SC, SM, SU, SUPPQUAL, SV, TE, TI, TS, TU, TV, VS | 33 | - |
| S-HOST | 宿主 F 文件承载的范围外非域节 (节正文未核): §7.3 | TI/assumptions.md | 1 | - |
| (宿主待主控定) | §6.1/§6.2/§6.3 类引言 (O39/O50, ch02 §2.3 只有近似句) + §6.3.6 MO 框标题/首句 (O31) | 无文件 | 0 | 宿主一定, 该引言并入拥有该文件的批 (ch02→S-CH, model/02→S-MODEL, NV/assumptions.md→S-HOST 或另开) |


缺口摘要字母: D=Description, S=spec 首句, A=Assumptions 标题, F=脚注. S-SPEC 外的批内脚注随本批做. 无 spec.md 的 FINAL 域 (脚注在 assumptions.md 处理): DI. 自检: 重复 0 / 未覆盖 0.

## 8. 局限

- 纯字符串机检: PARTIAL 可能是改写 (O33 类) 也可能是共享前缀假阳 (见 §3 注); EXACT 不等于位置正确. 承载判定须扫描批人工复核.
- BE §6.2.2 PDF 原子与页文本均未找到 spec 脚注 → 记 NA, 扫描批需看 PDF 原页 (p143-144) 确认.
- LB/CV/OE/MI/TU/DI 部分 spec 首句或脚注来自 `pdf_pages` 文本回退 (原子缺失/拆分), JSON `*_src` 字段标 `page_txt`.
- 文件级 F 判据宽松: checkpoint 只要点名该文件名即算 (单域批); spec.md 常被点名但未逐格扫 (O21), F 不代表 spec 表已逐格核.
- 批口径只看 writer checkpoint 字样, 不读 audit/review; B-OE 有 "双向全扫" 无页范围核, B-LB/B-SR/B-model05 有页范围字样无全扫 → PARTIAL.
## 9. 分组自检

- PASS scan batches: every file in exactly one batch
- PASS scan batches: every not-FINAL file covered
