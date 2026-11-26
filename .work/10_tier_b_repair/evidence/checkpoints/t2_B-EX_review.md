# T2 B-EX reviewer verdict

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (T-5 已按规则转 T4 用户裁定; 无 CONDITIONAL 修正项)

- 审查对象: `knowledge_base/domains/EX/examples.md` md5 `89f1a955a45627f18d252b4d1f139fb1` (461 行, = writer 续 after); `git diff 470b473 -- knowledge_base/domains/EX/` 只含该文件 (KB 其他改动 ch04/CP/DS 属并行批, 不在本审范围).
- 真值: `source/cdisc/SDTMIG v3.4 (no header footer).pdf` 重新 `pdftotext -layout` (p111-119) + `pdftoppm` 渲染 (p115/p117 @110-120dpi, p118 CRF @200dpi). scratch: `$S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-EX_reviewer/`.
- **独立方法 (非 writer bbox 解析器)**: `$S/interleave.py` — 每个 KB 单元格去空白后, 须能按列序切分为 [主行片段 + 折行片段] 恰好拼出 layout 文本主行/续行 (动态规划, 全行全部字符消费完才算 OK); 不折行的表 (Ex6 ex.xpt) 用表头列起点切分 `$S/cmp.py`.
  变异自检 (证明检查有效): Ex6 ec 行2/行14 ECDOSFRM 改回 CAPSULE → FAIL; Ex7 ec EPOCH 改 "VISIT TREATMENT" → FAIL; Ex7 列序换回 → FAIL; Ex7 ECLNKID 去掉 T1000 → FAIL; Ex2 VISITNUM 置空 → FAIL.

### 命令与结果 (可复跑)
```
S=<上面 scratch>; P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
for p in 111 112 115 116 117 118 119; do pdftotext -layout -f $p -l $p "$P" $S/L$p.txt; done
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # status {'UNPARSEABLE': 11, 'OK': 19, 'DIFF': 1}; diffs 3 = relrec.xpt :407 Row 列 3/4/5 vs PDF 6/3/4 (T-1)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # RESULT: RED, 13 regress: p0215 (CP) / p0257,p0258,p0260,p0263 (MB) — p104-120 (EX) 0 条
python3 tools/check_links.py | tail -1   # live docs: 42 (≤ 42)
```

### 逐格核对 (独立方法)
| 表 | KB 行 | PDF 页 | 格数 | 结果 |
|---|---|---|---|---|
| Ex2 ec.xpt (+VISITNUM) | :86-90 | 112 | 表头 24 + 3×24=72 | 表头一致; 3 行全一致 |
| Ex6 ec.xpt (12 偶数行 ECDOSFRM) | :263-288 | 116-117 | 表头 21 + 24×21=504 | 表头与 p116/p117 两处表头一致; 24 行全一致 (偶数行 ECDOSU/ECDOSFRM 均 TABLET, COATED) |
| Ex6 ex.xpt (8→24 行 + EXELTM) | :298-323 | 117 | 表头 19 + 24×19=456 | 456 格 0 差异; EXENDTC 24 格全空 = PDF 渲染该列空白 (目视确认) |
| Ex7 ec.xpt (列序/EPOCH/ECLNKID) | :368-375 | 118 | 表头 24 + 6×24=144 | 全一致; 列序 ECADJ→VISITNUM→VISIT→EPOCH; EPOCH=TREATMENT×6; ECLNKID 行2/4 带 T1000/T1100, 行6 20090227 (PDF 本无 T) |

### 人工逐格: Ex7 CRF (:339-356) vs p118 渲染 @200dpi
| KB 行 | 标签 | V1 | V2 | V3 | 判定 |
|---|---|---|---|---|---|
| 表头 | Visit | 1 | 2 | 3 | 一致 |
| Intended Dose | 10 mg/kg | **粗** | 常 | 常 | 一致 |
| (续) | 7.5 mg/kg | 常 | **粗** | **粗** | 一致 |
| Reason for Dose Adjustment | Dose-limiting toxicity | 常 | **粗** | 常 | 一致 |
| Dose Administered | Yes | **粗** | **粗** | 常 | 一致 |
| (续) | No | 常 | 常 | **粗** | 一致 |
| (续) | If no, give reason: | 常 ×3 | | | 一致 |
| (续) | Treatment discontinued due to disease progression | 常 ×3 | | | 一致 |
| (续) | Other, specify: | 常 | 常 | **Other, specify:** + "Personal reason" (PDF 下划线, 非粗) | 一致 |
| Date | | 13-FEB-2009 | 20-FEB-2009 | 27-FEB-2009 | 一致 |
| Start Time (24 hour clock) | | 10:00 | 11:00 | 空 | 一致 |
| End Time (24 hour clock) | | 10:45 | 11:20 | 空 | 一致 |
| Amount (mL) | | 99 mL | 35 mL | 0 mL | 一致 |
| Concentration | | 5.5 mg/mL | 4.12 mg/mL | 4.12 mg/mL | 一致 |
| If dose was adjusted, what was the reason: | Injection site reaction | 常 | **粗** | 常 | 一致 |
| (续) | Adverse event / Other, specify: | 常 ×3 | | | 一致 |
旧 KB 错 (V3 Dose Administered=Yes; Reason V2+V3; "Personal reason" 放在 adjusted-reason 行) 均已按 PDF 改正.

### 人工逐格: Ex6 CRF ×2 (:243-248, :252-257) vs p115/p116
- 表头/分隔/数据行均 10 格; "Period 1" 落第 1 列 (PDF 跨 Day..End Date/Time 5 列), "Period 2" 落第 6 列 — 与渲染一致. 数据 3+3 行 60 格对 layout 全一致 (Subject 56789001: p115 行 37-39; 56789003: p116 行 5-7).

### PDF_TYPO 判定 (按 "补充口径" 取舍规则)
| T | PDF 证据 | 判定 |
|---|---|---|
| T-1 relrec Row 1,2,6,3,4,6 (p119) | layout 行 19-24 确为 "6 ... VSLNKID" / "3 ... ECLNKGRP" | 可由同表连续编号 + "Rows 1-3 / Rows 4-6" 确定 → KB 1-6 正确 |
| T-2 "using --LNKID, ." (p119) | 确有 ", ." | 标点印刷错, KB "--LNKID." 正确 |
| T-3 "ottles A, B and C" (p113 l13) | 确 | 同列表 "bottles" → KB 正确 |
| T-4 "protocol specified unit" (p115) | 确无连字符 | 同节其他处均 protocol-specified → 可接受 (属拼写风格统一, 无信息差) |
| T-5 EXENDTC 24 格空 (p117) | 渲染确认该列空白; EXENDY 有值; Assumption 4b (p107) "EXSTDTC should be copied to EXENDTC" | **同意照录 + T4**: 整列空 (非孤立错格) 更像示例作者取舍; 虽 spec 规则可推出候选值, 自填 24 格 = 生成 PDF 没有的内容, 交用户裁定. 用户若裁定"按 spec 补", 值 = 同行 EXSTDTC |

### RELOCATE / 新增 atom
| ref | 检查 | 结果 |
|---|---|---|
| Rows 1-12 / 13-24 (:292, :294) | PDF p117: 两条说明在 "The EX dataset shows the unblinded administrations." 之后、ex.xpt 之前 | 位置正确; 原处 (ec.xpt 前) 已删且未留指针 (符合 dispatch notes); 文字与 layout 逐字一致 |
| ig34_p0111_a004 :9 `**Exposure CRF:**` | p111 l6 "Exposure CRF:" | 一致 |
| ig34_p0112_a008 :63 `**Exposure CRF**` | p112 l10 "Exposure CRF" (无冒号) | 一致 |
| ig34_p0112_a030 :92 "because this location" | p112 l36-37 | 一致 |
| ig34_p0115_a028 :237 "The following CRFs show data for 2 subjects." | p115 l32 (位于 Ex6 引言后、Subject 前) | 一致, 位置对 |
| Ex7 引言拆段 :327-329 | p117 两段 | 一致 |

### G-TB6 反向溯源 (diff 80 增 / 53 删, 逐行)
- 所有新增/改动数据行与叙述行在 PDF p111/112/115/116/117/118 可找到 (上表). 无出处词句: 0.
- 结构行签字: Ex2 ec 表头+分隔 (p112 表头); Ex6 CRF 表头+分隔 ×2 (p115/116); Ex6 ex.xpt 表头+分隔 (p117); Ex7 CRF 表头 `| Visit | 1 | 2 | 3 |`+分隔 (p118 首行); Ex7 ec 表头+分隔 (p118); CRF 续行空标签格 (版式, 对应 PDF 同格多选项) — 均签字.
- :3 `> KB note (not in SDTMIG): Examples for EX and EC are shared in Section 6.1.3.3…` — KB 自写, 与 PDF 不矛盾 (p111 节号 6.1.3.3 属实), D6 标注正确. `**CRF:**` (Ex5/6/7/8) 与 `**Subject ABC123-0201**` 属纯导航短标签, 按 D6 范围行不加标注 — 同意.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| :339-356 Ex7 CRF | 格式 (LOW) | 项目符号 "•" 与填写下划线 "____" 未录; writer 已说明 (避免 Markdown 强调误解析), 不丢信息 | p118 "Other, specify: ____" |
| :237-239 | 格式 (LOW) | 新补句 "The following CRFs show…" 后仍保留导航标签 `**CRF:**`, 略冗余; 不阻断 | p115 l32 |
| T-5 | 待用户 | EXENDTC 照录空值, 已登记 T4 | p117 EXENDTC 列空 |

### EX/EC 重复例子归属裁定 (供 B-EC)
- PDF 节号: 6.1.3 Exposure Domains → 6.1.3.1 EX (p104) / 6.1.3.2 EC (p107) / **6.1.3.3 Exposure/Exposure as Collected Examples (p111-120)**. 例子集是 6.1.3 下的共享兄弟节, 不隶属 6.1.3.1 或 6.1.3.2.
- 裁定: **以 `knowledge_base/domains/EX/examples.md` 为唯一归属副本** — 理由: 节标题 EX 在前; EX 副本完整 (Example 1-8, EC 副本缺 Example 4); 且本批已按 PDF 修正. B-EC 按 D2: `EC/examples.md` 去重为一行交叉引用至 EX/examples.md (EC 现有错: Ex2 缺 VISITNUM、Ex6 Rows 说明错位、Ex7 EPOCH/列序错, 不必再逐格修).

### 完整性
- atoms 10/10 有 action (REAL_GAP 2 随 CRF 重建插入; VALUE_DIFF 8 已改), 原子 verbatim 走样处 writer 以 PDF 为准 — 核对属实. census DIFF 5 表全部处理, 残留仅 T-1. 本批 pdf_only / pdf_unparsed 0. t2_recheck 无.
