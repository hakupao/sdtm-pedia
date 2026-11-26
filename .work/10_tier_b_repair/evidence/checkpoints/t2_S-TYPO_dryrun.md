# S-TYPO attempt 1 — DRY-RUN 报告 (writer, 2026-11-26)

> 状态: **dry-run 完成, KB 未改** (HEAD 44fb042; `typo_assert.py` 对仓库 knowledge_base 跑结果 PASS = 与 HEAD 相同)

## 0. 产物与复跑命令

| 产物 | 路径 | 提交 |
|---|---|---|
| 计划生成 (+ `--apply` 只能写 scratch 副本) | `scripts/t2s/typo_plan.py` | 是 |
| 断言 (独立于 plan 逻辑, 只看 HEAD vs 目标树) | `scripts/t2s/typo_assert.py` | 是 |
| 变异测试 | `scripts/t2s/typo_mutate.py` | 是 |
| 计划 (每处替换一行) | `work/t2_batches/S-TYPO.plan.jsonl` (394 行) | 是 |
| 固定清单 (渲染核过; 断言只在这些位置放行括号/数字类改动) | `work/t2_batches/S-TYPO.fixed.jsonl` (43 行) | 是 |
| 残余清单 (只含 KB 侧信息, 不含 PDF 文本) | `work/t2_batches/S-TYPO.residual.jsonl` (1101 行) | 是 |
| raw 模式页文本、渲染图、stats、变异副本 | scratch `t2s_S-TYPO_writer/` | 否 |

复跑 (`$S` = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-TYPO_writer`):

```
# 1) raw 第二来源 (layout 来源 = work/pdf_pages)
cd source/cdisc; for p in $(seq 1 461); do pdftotext -raw -enc UTF-8 -f $p -l $p "SDTMIG v3.4 (no header footer).pdf" $S/raw/ig34_p$(printf %04d $p).txt; done
for p in $(seq 1 74); do pdftotext -raw -enc UTF-8 -f $p -l $p SDTM_v2.0.pdf $S/raw/sv20_p$(printf %04d $p).txt; done
# 2) 计划 + 固定清单 + 残余 (stats -> $S/typo_stats.json)
python3 .work/10_tier_b_repair/scripts/t2s/typo_plan.py $S/raw      # -> "plan 394 resid lines 1101 errs 34" (34 = registry 计数 WARN, 见 §6)
# 3) 变异测试 (含正对照 HEAD+plan, 与 repo 树 == HEAD)
python3 .work/10_tier_b_repair/scripts/t2s/typo_mutate.py $S        # -> MUTATION SUITE OK
# 4) 正式断言 (正式写入后跑; 现在跑 = 证明 KB 未动)
python3 .work/10_tier_b_repair/scripts/t2s/typo_assert.py [--plan .work/10_tier_b_repair/work/t2_batches/S-TYPO.plan.jsonl]
# 计数
python3 -c "import json,collections as C;P=[json.loads(l) for l in open('.work/10_tier_b_repair/work/t2_batches/S-TYPO.plan.jsonl')];print(len(P),C.Counter(p['class'] for p in P),len({(p['file'],p['line']) for p in P}),len({p['file'] for p in P}))"
```

## 1. 方法

- **页范围**: B 批 `pdf_ranges` (B-REL 无 file 键 → 套全部 kb_files; B-DI 只有 `pdf_pages` [441] → 用之) ∪ S 批 `sections` (S-SPEC* 只给 spec.md; S-HOST unit 去括注); domains/ 文件取**本域目录所有文件范围的并集** (= 本域所在节)。202 个文件全部有范围 (首跑时 DI 3 行无范围, 已补 B-DI pdf_pages)。model/ 用 sv20。
- **单位**: KB 行内每个排版单位 (SQ `' ’ ‘` / DQ `" “ ”` / DASH `- – —` / ELL `...` `…`)。表格按单元格切段; 去掉 markdown 语法 (列表符、`**`、链接目标、HTML 标签、转义符; spec.md 的 `- **Label:**` 字段前缀)。
- **匹配**: 段内去全部空白 + 排版类归一 (同类字符折成一个记号; `--X`/PDF `–X` 折成变量记号; PDF U+2011/U+2010 折成 `-`, 不作 after_char), 以该单位为中心取窗口 (24/24 → 16/16 → 10/10 → 单侧 16/10, 至少 6 个字母数字; 表格短格 <6 字母数字时用整格, 至少 3 个) 在**该文件页范围**内的 layout + raw 两份文本里找。**所有命中给出同一 PDF 字符**才算解决; 不同 → 不一致; 0 命中 → 残余。计划里 341 条匹配类字符改动 (394 − 固定清单 43 − 空格 10): 实际左右上下文字母数字合计 ≥24 的 326 条, 12-23 的 15 条, <12 的 0 条 (Rule A 可把这 15 条单列一层); 2 条来自单侧窗口 0/16 (ch08:328 两个引号)。计划行无一位于单独一行 `> KB note` 标注的表/段之下 (已查)。
- **em dash 两侧空格 (O59)**: 只在目标字符为 – / — 且所有命中对该侧给出同一结论 (PDF 折行处 = 无证据, 不改) 时增删一个空格。
- **○ □ / 上标**: pdftotext 不可信 → 枚举全部候选 (`( )` `[ ]` `[X]` `☐` `○` `◦` `^1^` 行首 `1In`), 逐页渲染定字形 (§5), 写成固定清单。
- **do-not-touch (保护位置, 匹配时可读、不可改)**: registry 270 条每个 `kb_text_span` 在该文件的**所有出现位置**; `--X` 变量前缀; 标题行; 代码块 (含 Mermaid); HTML 注释; `> KB note` 块; 行内代码; URL / 链接目标; 列表符; 表格 `|`; `**`; S-CT 的 `(SHORT) Cxxxx`。
- **字形抽查 (渲染 vs pdftotext)**: p29 em dash 无空格 (`variables—such`)、p41 `"Pn…"`、p293 `51–75%`、p139 `“Y”` / `sponsor’s` 弯引号与同页直引号 `"Serious?"`, 都与 pdftotext 给出的字符一致。字体核查用 `pdftohtml -xml -i -stdout -f P -l P <pdf>` 看字符所属 fontspec。

## 2. 计划: 按替换类计数 (394 处 / 164 行 / 52 个文件)

| 类 | chapters | domains | model | 合计 |
|---|---:|---:|---:|---:|
| dq: 直 → 左 “ | 28 | 111 | 0 | 139 |
| dq: 直 → 右 ” | 28 | 107 | 0 | 135 |
| sq: 直 → 右 ’ | 6 | 49 | 0 | 55 |
| crf: `( )` → ○ (固定清单, CE p152/p153) | 0 | 33 | 0 | 33 |
| crf: `[ ]` → □ (固定清单, CE p153) | 0 | 6 | 0 | 6 |
| space: 删 em dash 两侧空格 (O59) | 4 | 6 | 0 | 10 |
| dash: hyphen → en (MK 51–75% / 26–50%, SUPPQUAL + ch08 Scale–Cognitive) | 1 | 4 | 0 | 5 |
| ell: `...` → … | 3 | 1 | 0 | 4 |
| sup: `^1^ ` → ¹ (ch08 4 处 spec 脚注, 固定清单) | 4 | 0 | 0 | 4 |
| dash: em → en (ch04:194, ch08:82 `RELREC – Specification`) | 2 | 0 | 0 | 2 |
| dash: em → hyphen (ch08:78 `RELREC - Description/Overview`, PDF p429 原样) | 1 | 0 | 0 | 1 |
| **弯 → 直 (任一方向)** | 0 | 0 | 0 | **0** |

- PDF 本身混用 (如 LB `LBTEST = "HCT"` 与 `LBSTAT = “NOT DONE”` 同句; MB `(e.g., “COLONY COUNT", "VIRAL LOAD")`): 计划逐字照 PDF, 改后同行会出现直弯混排, 这是忠实于 PDF, 不是错误。
- 正对照: HEAD + plan 写入 scratch 副本后 `typo_assert.py --plan` PASS (52 文件 / 164 行 / 0 违规)。

## 3. 覆盖率 (按目录; 排版单位行 = 去掉标题 / KB note / 代码后, 含 ≥1 个排版单位的行)

| 指标 | chapters | domains | model |
|---|---:|---:|---:|
| ① 合格行 (含排版单位) | 610 | 5090 | 192 |
| ② 全部单位命中且一致 (= 已解决) | 592 (97.0%) | 4191 (82.3%) | 151 (78.6%) |
| 　其中 与 PDF 相同 (无需改) | 562 | 4073 | 151 |
| 　其中 已入计划 (匹配类) | 30 | 118 | 0 |
| ③ 已知与 PDF 不同的行 (命中且字符不同, 含不一致) | 34 | 133 | 0 |
| ④ 其中已入计划且整行解决 (**覆盖率 = ④/③**) | 29 (85.3%) | 117 (88.0%) | — |
| ⑤ 有不一致单位的行 | 2 | 11 | 0 |
| ⑥ 有 0 命中单位的行 | 13 | 883 | 41 |
| 　其中 KB 自写导航 (Cross References / 链接行 / `> Class` 行) | 2 | 681 | 2 |
| 　其中 示例表省略列 `...` 格 | 0 | 26 | 0 |
| 　其中 其它 (无法判断是否与 PDF 不同) | 11 | 176 | 39 |
| ⑦ 被 do-not-touch 拦下的行 (registry / 需定规则) | 3 | 6 | 0 |
| (另) 跳过: 标题行 / KB note 行 | 36 / 10 | 405 / 107 | 13 / 24 |

- 固定清单另覆盖 CE/examples.md 11 行 (43-46、74、77、79-83; 39 处) 与 ch08 4 行 (不计入 ②④)。计划行合计 = 匹配类 149 + 固定清单 15 = 164。
- **0 命中 ≠ 与 PDF 相同**: ⑥ "其它" 226 行 (chapters 11 / domains 176 / model 39) 无法判断; 集中在 spec.md Label / CDISC Notes 跨列折行、示例表格跨行、sv20 表格 (EG 22、model/02 21、TR 17、FA 16、LB 16、RP 15、MH 14、PP 12、TU 11 行)。按单位计 (domains): 0 命中 hyphen 205、`"` 49、`—` 11、`--` 11 (CE `--/---/--` 日期占位 6、LB/NV `--.xpt` / `| -- |` 5)、弯引号 5、`'` 1; model `"` 56、`-` 22; chapters `-` 12、`"` 5。
- fp_match / 覆盖矩阵对排版不敏感, 不作闸 (按 brief)。

## 4. 残余清单分类与建议处置 (`work/t2_batches/S-TYPO.residual.jsonl`)

| 类 | 行数 | 内容 | 建议 |
|---|---:|---|---|
| R1 0 命中 (其它) | 226 | 见 §3 ⑥ | 不改。若要更高覆盖: 第二轮用 bbox 单元格级解析 (sc2/speccmp2 的列切分) 只对 spec.md / 示例表重跑, 或由 auditor 抽样渲染 |
| R2 KB 自写导航 | 685 | 659 个 `—` 在 Cross References / 链接说明行 (`[…](….md) — …`) | 保持 (PDF 无对应, 属 U8 导航) |
| R3 表格省略列 | 26 | 示例表 `| ... |` 列省略 (51 个) | 保持 (KB 省略记号, 非 PDF 文本) |
| R4 多命中不一致 | 13 | ch04:793 `--12-15`; ch08:38 `CMGRPID="COMBO THPY 2"`; IS ex:108; TA ex:351-357 (`5-10-P` / `5mg-10mg-Placebo`, 7 行); TU assumptions:68-70 `TUTEST = "Tumor Identification"` | 人工对渲染逐个定 (13 行), 定后可加入固定清单 |
| R5 registry do-not-touch | 6 | B-IS T-6 `AUREUS-EPITOPE X` (IS ex:205-207, PDF en dash); B-MK T-1 `MODERATE-SEVERE; 76-95%` (MK ex:52/57, PDF en dash); B-TA T-4 `5 mg - 10 mg - Placebo` (TA ex:351) | **需主控定**: t4_user_decisions §6 第 5 条说这三项可按 U1 改 en dash, 本任务说 span 一律不动; dry-run 按不动处理 |
| R6 需定规则 (表外) | 3 | ch04:1485 / 1514 `Supplemental Qualifiers -- SUPP-- Datasets` (PDF `–`, `--`→`–` 是 2→1 字符); ch04:1101 `VSDTC−VSRFTDTC` (KB U+2212, PDF `-`) | **需主控定**: S-TYPO.json scope 写了 "CH4 的 U+2212 减号、'--' 代 en dash 按 PDF", 但闭表没有这两种; 若批准, 断言须加两条窄类 (只放行这 3 个位置) |
| R7 标题 (O60) | 142 | 123 行 KB `—` vs PDF `–` (如 `## XX — Assumptions` 对 PDF `XX – Assumptions`); 其余 19 行 PDF 本身 `-`/`–` 混用 (RELREC/RELSUB/RELSPEC/CP/GF/SE/RS) | 只登记, 交 T4 / O60 统一 (改标题影响锚点) |
| R8 KB note 内 | 1 | ch04:983 (KB 自写引号) | 保持 |

## 5. ○ □ / 上标 固定清单 (渲染定字形)

| KB 位置 | KB 现状 | PDF 页 / 渲染字形 | 处置 |
|---|---|---|---|
| CE/examples.md:43-46 | `( )` ×18 | p152 渲染为小圆, 但 PDF 字符是 CourierNew 字母 `o` (pdftohtml 字体核查: 与 ch04 p33 列表符号同字体同字符, 18 处) | **计划** → ○, 依据是 U4 点名 "CE 的 ( ) / [ ] 改回", **不是**字形不同; 证据强度低于 p153 (p153 是真 ○ □, 21 处)。主控若要求 ch04 与 CE 同口径, 这 18 处应与 ch04 一起定 |
| CE/examples.md:74-83 | `( )` ×15, `[ ]` ×6 | p153 ○ / □ | **计划** → ○ / □ |
| ch08:96/212/363/438 | `^1^ In this column` | 渲染 p429 (RELREC) / p432 (SUPPQUAL) / p438 (RELSUB) / p439 (RELSPEC): 上标 ¹ 紧贴 "In", 无空格 | **计划** → `¹In this column` (同时删 1 个空格) |
| FA/examples.md (28 行) | ○ | p367-374: pdftohtml 字体核查为 Arial 中的 U+25CB (非字母 o), 渲染 p369 为 ○ | 已一致, 不改 |
| AE/assumptions.md:61/63 | `[ ] Yes [ ] No` | p139 字面 `[ ]` | 已一致, 不改 |
| ch04:410-412 | `[ ]` ×3 | p32 Wingdings 坏字形 (钟形图标, pdftotext 空) | **需定**: 不是 ○ / □; 建议保持 `[ ]` 或改 ○ |
| ch04:427-432, 472-476, 506-510 | `[ ]` ×16 | p32/p33 Courier New 字母 `o` 列表符号 (渲染为小写 o) | **需定**: 视觉近 ○, 字符是 `o`; 建议改 ○ (须用户 / 主控批准后进固定清单) |
| ML/examples.md:16-18, 27-29 | `[X]` / `[ ]` | p123 只有 `X` 勾记号, 未勾选项无框 | **需定**: 表外字符 (`[X]`, 无框); 建议保持 |
| DM/examples.md Mermaid | `☐` ×~60, `○` | 在代码块 (Mermaid) 内 | 代码块不动; 若要统一 `☐`→`□` 需另批 (O51 Mermaid 渲染时一并) |

## 6. 断言与变异测试

`typo_assert.py` 规则: 只比 HEAD 与目标树; 文件增删 / 范围外文件改动 / 行数变化 → FAIL; 标题、代码块、HTML 注释、KB note 行改动 → FAIL; 其余改动行逐 difflib 操作核: 不碰保护位置, 去空白后两侧都只含闭表单位且**逐单位同类** (引号不能变 dash, `'` 不能变 `“`, 单位数不变), 空格增删只允许紧邻结果为 – / — 的位置, 且只允许空格; 括号 / 数字类改动只在固定清单位置放行; registry 每个 span 在文件内出现次数不变。`--plan` 另核目标树 == HEAD + 计划。

| # | 植入缺陷 (HEAD+plan 副本上, 不带 --plan 跑) | 位置 | 退出码 | 结果 |
|---|---|---|---:|---|
| C0 | 正对照: HEAD + plan (--plan) | — | 0 | PASS ✔ |
| C1 | 正对照: 仓库 knowledge_base == HEAD | — | 0 | PASS ✔ |
| M1 | 字母改动 (`NOT DONE`→`NOT DONF`) | ch04:1319 | 1 | FAIL ✔ |
| M2 | 删一个连字符 (`sponsor-defined`) | ch01:84 | 1 | FAIL ✔ |
| M3 | 改标题 (`—`→`–`) | AE/assumptions:1 | 1 | FAIL ✔ |
| M4 | `--TESTCD`→`–TESTCD` | ch04:74 | 1 | FAIL ✔ |
| M5 | registry span B-TA T-4 hyphen→en | TA/examples:351 | 1 | FAIL ✔ |
| M5b | registry span B-FA T-1 弯→直 | FA/assumptions:9 | 1 | FAIL ✔ |
| M6 | 表外字符替换 (`“`→`«`) | ch04:1319 | 1 | FAIL ✔ |
| M7 | 多删一个引号 | ch04:1319 | 1 | FAIL ✔ |
| M8 | 删普通词间空格 | ch01:84 | 1 | FAIL ✔ |
| M9 | 跨类替换 (`'`→`“`) | ch02:83 | 1 | FAIL ✔ |
| M10 | 代码块 (Mermaid) 内改引号 | DM/examples:117 | 1 | FAIL ✔ |
| M11 | KB note 内改 | ch02:115 | 1 | FAIL ✔ |
| M12 | 范围外文件 (terminology) | terminology/core/ae.md:10 | 1 | FAIL ✔ |
| M13 | 固定清单外 `[ ]`→`□` | ch04:472 | 1 | FAIL ✔ |
| M14 | 非变量 `--`→`–` | ch04:1485 | 1 | FAIL ✔ |
| M15 | 行内代码内 hyphen→en | ch04:725 | 1 | FAIL ✔ |
| M16 | hyphen 旁删空格 (`RELREC — Desc`→`RELREC-Desc`) | ch08:78 | 1 | FAIL ✔ (初版放行, 已修: 空格规则只看改后字符) |
| M16b | 日期 hyphen 旁加空格 | ch04:106 | 1 | FAIL ✔ |
| M17 | 插入一行 | AE/assumptions:7 | 1 | FAIL ✔ |
| M18 | 列表符 `-`→`–` | AE/spec:7 | 1 | FAIL ✔ |
| M19 | 固定清单位置给错字形 (○→□) | CE/examples:43 | 1 | FAIL ✔ |
| M20 | 固定清单上标改错数字 (¹→²) | ch08:96 | 1 | FAIL ✔ |

- 变异测试的教训: M16 首跑漏网 (空格规则看了改前行的 `—`, 而计划把该处改成了 hyphen)。已改为只看改后字符, 重跑 22/22 FAIL + 2 正对照 PASS。
- **registry 计数 WARN 34 条**: `span_count_in_file` 与 HEAD 实际出现次数不符 (如 B-AE T-4 `| Row` 记 1、实为 6; B-GF T-5 记 40、实为 2), 原因是登记时计数口径不一 (按表 / 按行)。本批对每个 span 的**全部出现位置**加保护, 比登记更严, 结论不受影响; 计数本身建议由登记表维护者修正。

## 7. 需主控 / 用户定的规则

1. **R5 (U1 冲突)**: B-IS T-6 / B-TA T-4 / B-MK T-1 的 span 改不改成 PDF 的 en dash (§6 第 5 条说允许; 本任务说 span 不动)。
2. **R6 (表外)**: `--`→`–` (ch04 2 处) 与 U+2212→`-` (ch04 1 处) 是否并入闭表 (S-TYPO.json scope 写了按 PDF)。
3. **CRF (U4 边界)**: ch04 p32/p33 的 `o` 列表符号 / Wingdings 坏字形, ML `[X]`, DM Mermaid `☐`: 照 U4 改 ○ / □, 还是保持。
4. **R4 不一致 13 行**: 由主控指定人工对渲染, 还是留给 T4。
5. **R1 0 命中 226 行**: 接受现状 (只改有证据的), 还是加一轮 bbox 单元格级匹配。
6. ch08:78 / 82 的粗体伪标题 `**RELREC — Description/Overview**` / `**RELREC — Specification**` 按正文进了计划 (→ PDF `-` / `–`), 而同文件 `### RELSUB — …` / `### RELSPEC — …` 是标题, 归 O60 不动 → 改后同文件口径不一; 主控定: 这 2 行也移出交 O60, 还是照计划。
7. `knowledge_base/.omc/` 下有 OMC hook 生成的未跟踪文件 (非本批产物, 未删); `typo_assert.py` 因此跳过所有以点开头的路径。
8. Rule A 分层建议: 写入后的 auditor 按类分层抽 (dq 左 / dq 右 / sq / crf / space / dash / ell / sup), 另从 R1/R4 抽 10 条核 "不改" 是否正确。
