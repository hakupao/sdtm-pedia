# T4.1 第三轮补检 — 包 2 结果 (R3_IG34_EQUIV, T26-T50)

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T06:37:10Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round3_v1.0.md` (R3_IG34_EQUIV 层)
- 看过的渲染页: SDTMIG v3.4 p220 (T29 段落原文 "(HA5) and rows 5-7"、"at runtime to for"), p425 (T43/T45: NullFlavor 表续行 WARNING 与层级列表)
- 用过的命令:
  - `sed -n "<N>p" knowledge_base/...` 逐条确认包里 KB 指针行在 HEAD 文件中真实存在
  - `python3 -I scratchpad/r3_2/cmp.py`: 取 `pdf_pages/ig34_pNNNN.txt` 对应行拼接, 归一化 (空白 / 弯直引号 / `**` / `<br>` / 项目符号) 并去掉行首 "Row(s) N-M:" / "N." / "c." 标记后, 判断 PDF 文本是否为 KB 行的子串; 不是则逐词 diff → 23 条 (除 T37/T38) 全部 SUBSTR, 无差异词
  - `grep -rn` 在 `knowledge_base/` 中定位 T37 / T38 (包中 KB 指针为 "(无)")
  - `awk` 取每条 KB 行之前最近的标题; `grep -n 'Example N'` 取 PDF 各页例号, 核位置 (所属例 / 节)
  - `grep` `work/t2_pdf_typo_registry.jsonl` 按相关页号查登记
  - `pdftoppm -r 110 -f 220/425` 输出到 scratchpad

## 逐条判定

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| T26 | ig34_p0211_a005 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0211.txt:15-17 (Example 2, p211:5); `knowledge_base/domains/CP/examples.md:73` (## Example 2) | 实为逐字 (仅行首加粗) |
| T27 | ig34_p0211_a008 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0211.txt:23-25; `knowledge_base/domains/CP/examples.md:79` (## Example 2) | 实为逐字 |
| T28 | ig34_p0214_a017 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0214.txt:41-45 (Example 5, p214:38); `knowledge_base/domains/CP/examples.md:171` (## Example 5) | 实为逐字. "GATE and GATEDEF" KB 照录 PDF, 已登记 `REG CP N-1` (照录+T4), KB=PDF, 不构成 TYPO_AFFECTED |
| T29 | ig34_p0220_a003 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0220.txt:5-11 + 渲染页 p220 (Example 9 起于 p219:56); `knowledge_base/domains/CP/examples.md:305` (## Example 9) | 实为逐字. 原子抽错: 原子写 "(HA5). Rows 5-7 show…", PDF 与 KB 均为 "(HA5) and rows 5-7 show…". PDF "at runtime to for measuring" KB 照录 (KB=PDF; 未见登记, 不影响判定) |
| T30 | ig34_p0237_a008 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0237.txt:15-16 (Example 6, p237:3; Example 7 在 :30); `knowledge_base/domains/IS/examples.md:136` (## Example 6) | 实为逐字 (弯引号 ’ 一致) |
| T31 | ig34_p0246_a010 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0246.txt:26 (Example 1); `knowledge_base/domains/LB/examples.md:10` (## Example 1) | 实为逐字 |
| T32 | ig34_p0258_a002 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0258.txt:2 (Example 2 起于 p257:39); `knowledge_base/domains/MB/examples.md:47` (### Example 2) | 实为逐字 |
| T33 | ig34_p0260_a002 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0260.txt:5-7 (Example 3 起于 p259:32); `knowledge_base/domains/MB/examples.md:105` (### Example 3) | 实为逐字; 值 100.3/100.4/100.5 一致 |
| T34 | ig34_p0261_a015 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0261.txt:24-26 (仍属 Example 3); `knowledge_base/domains/MB/examples.md:175` (### Example 3) | 实为逐字 |
| T35 | ig34_p0261_a016 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0261.txt:27-29; `knowledge_base/domains/MB/examples.md:177` (### Example 3) | 实为逐字 |
| T36 | ig34_p0270_a006 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0270.txt:9 (Example 1); `knowledge_base/domains/PC/examples.md:17` (### Example 1) | 实为逐字 |
| T37 | ig34_p0282_a031 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0282.txt:37-38 (Example 4, Method A); `knowledge_base/domains/PC/examples.md:401` (### Example 4 → #### Method A, :390/:398) | 包中 KB 指针为 "(无)", 自行 grep 定位. 实为逐字; PCGRPID 三值与 "CMAX" 一致 |
| T38 | ig34_p0284_a015 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0284.txt:46-47 (§6.3.5.9.3 实施建议第 4 点); `knowledge_base/domains/PC/assumptions.md:123` (### PC-PP – Suggestions for Implementing RELREC…, 位于 ## §6.3.5.9.3 下) | 包中 KB 指针为 "(无)", 自行 grep 定位. 实为逐字 (含序号 "4.") |
| T39 | ig34_p0345_a002 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0345.txt:2; `knowledge_base/domains/TU/assumptions.md:17` (## TU – Description/Overview) | 实为逐字 |
| T40 | ig34_p0356_a025 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0356.txt:40 (Example 3, p356:15); `knowledge_base/domains/TR/examples.md:62` (## Example 3 (continued from TU)) | 实为逐字 |
| T41 | ig34_p0406_a002 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0406.txt:2; `knowledge_base/domains/TE/examples.md:61` (## Trial Elements Issues → ### Granularity of Trial Elements) | 实为逐字 (含 "c.") |
| T42 | ig34_p0406_a032 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0406.txt:46; `knowledge_base/domains/TE/examples.md:94` (### Transitions Between Elements) | 实为逐字 |
| T43 | ig34_p0425_a016 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0425.txt:20 + 渲染页 p425 (层级列表 Unknown 下第 3 级); `knowledge_base/domains/TS/assumptions.md:106` (### Use of Null Flavor, 同层级缩进) | 实为逐字. PDF 列表 "Quantity sufficient" vs 表 "Sufficient quantity" 的内部不一致已登记 `B-TS T-7` (照录+T4), KB=PDF, 不构成 TYPO_AFFECTED |
| T44 | ig34_p0426_a001 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0426.txt:3-4 (§7.5, 起于渲染页 p425 底); `knowledge_base/domains/TI/assumptions.md:45` (## §7.5 How to Model the Design of a Clinical Trial) | 实为逐字. KB 无 ch07 章节文件, §7.5 整节以带节号标题放在 TI/assumptions.md (紧接 §7.4 TI/TS), 节归属清楚, 视为位置成立 |
| T45 | ig34_p0425_a002 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p425 顶: 表续页, WARNING 为 MSK 行 (p424 末行 "2 MSK Masked") 的续行, 仅占 Definition 列, 粗体居中; `knowledge_base/domains/TS/assumptions.md:90` (MSK 行 Definition 格内 `<br>` + 粗体) | 文字逐字; 结构差异 = PDF 独立续行 → KB 并入 MSK 定义格, 归属关系与 PDF 一致, 信息等价 |
| T46 | ig34_p0015_a009 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0015.txt:18-19; `knowledge_base/chapters/ch02_fundamentals.md:135` (## 2.7 → ### Must NEVER be used…) | 实为逐字 (KB 另加了一个小标题, 不影响) |
| T47 | ig34_p0020_a031 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0020.txt:41-42; `knowledge_base/chapters/ch03_submitting_data.md:100` (### 3.2.1.1 Primary Keys) | 实为逐字 (整段含前后句) |
| T48 | ig34_p0037_a022 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0037.txt:29-31; `knowledge_base/chapters/ch04_general_assumptions.md:683` (### 4.3.5) | 实为逐字 |
| T49 | ig34_p0039_a019 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0039.txt:21-22; `knowledge_base/chapters/ch04_general_assumptions.md:758` (### 4.4.1) | 实为逐字 (仅 "DTC" 加粗). 同页 `S-CH4 N-1` 位于 KB:756 另一句, 与本原子无关 |
| T50 | ig34_p0046_a009 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0046.txt:14-15; `knowledge_base/chapters/ch04_general_assumptions.md:1072` (### 4.4.10 Representing Time Points) | 实为逐字 |

## 计数 (R3_IG34_EQUIV, 本包 25 条)

| 判定 | 条数 |
|---|---|
| HOLDS | 25 (其中 24 条实为逐字; T45 文字逐字、结构为续行并格) |
| TYPO_AFFECTED | 0 |
| NOT_HOLD | 0 |
| UNVERIFIABLE | 0 |

- 原子抽错 (KB 与 PDF 一致): T29.
- 涉及已登记 "照录+T4" 条目、KB=PDF (非 TYPO_AFFECTED): T28 (`REG CP N-1`), T43 (`B-TS T-7`).

## 样本外发现的 KB 内容问题

无 (新发现). 附注: T29 所在 PDF 句 "imposed on the assay at runtime to for measuring background binding" (p220 Rows 2-7) 疑为 PDF 多字笔误, KB `knowledge_base/domains/CP/examples.md:305` 照录; 在 `work/t2_pdf_typo_registry.jsonl` 中未查到登记. KB=PDF, 不影响本包判定, 仅供主控决定是否补登.
