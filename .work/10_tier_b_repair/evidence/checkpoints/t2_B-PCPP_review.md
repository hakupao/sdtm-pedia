# T2 B-PCPP reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: CONDITIONAL** (共 3 条修正, 无 HIGH 级数据错; 表格数据全部与 PDF 一致)

范围: `git diff 302ec4c -- knowledge_base/` 只涉及 PC/assumptions.md、PC/examples.md、PP/examples.md (白名单内 3 个文件, 白名单外无改动).
scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_BPCPP_reviewer/` (按主控指定; 含 laycmp.py 独立解析器、p274 渲染图)

### 命令 (可复跑)
```
S=<scratch>; python3 -I -c "...manifest..."   # 同 prompt
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  → status {'OK': 19, 'DIFF': 3, 'NO_PDF': 1, 'UNPARSEABLE': 1}; diffs 38; 本批页内 PDF_ONLY 0 (只剩 p267 mi/suppmi, 不属本批)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  → regressions=0 new_hits=10, RESULT: GREEN
python3 tools/check_links.py | tail -1 → live docs: 42 (不超过 42)
独立复核 (不走 table_census 的 bbox, 避免 writer 用 parse_pdf 生成表造成循环论证): $S/laycmp.py 用 pdftotext -layout 文本按表头列位置分列并拼接折行
  PC/examples.md:25 pc.xpt (p270-271) 32 行 × 31 列: 0 差异
  PC/assumptions.md:55 pc.xpt (p276) 24×29: 0 差异;  :86 pp.xpt (p277) 12×20: 0 差异
  PP/examples.md:16 pp.xpt Ex1 (p273) 24×19: 0 差异
```

### G-TB4 表格
| 表 | census | 结论 |
|---|---|---|
| PC/assumptions.md:29/55/86 | OK | 一致 (另经 layout 独立复核) |
| PC/examples.md:25 PC Ex1 (新建) | OK | 一致 (layout 复核 0 差) |
| PC/examples.md:75 Ex1 Method A r3 IDVAR | DIFF 1 | 登记 PDF_TYPO T-1, 成立 |
| PC/examples.md:89 Ex1 Method B r13/r26 RDOMAIN | DIFF 2 | T-2/T-3, 成立 (IDVAR=PPGRPID 的行 RDOMAIN 只能是 PP) |
| PC/examples.md:289 Ex3 Method A r3 | OK | DYIDRGX_A → DY1DRGX_A 与 p280 表一致 |
| PP/examples.md:16 PP Ex1 (重建) | OK | 一致 |
| PP/examples.md:56 Ex2 pp.xpt | NO_PDF (p274 居中) | 人工逐格见下 |
| PP/examples.md:70 SUPPPP | DIFF 35 | 人工逐格见下: 34 格为解析器列错位, 1 处表头 = T-6 |
| PP/examples.md:89 Ex3 pp.xpt | OK | 一致 |
| PP/examples.md:122 Method 映射表 | UNPARSEABLE | 未改动; 人工对 p275 方法列表: A PCGRPID+PPGRPID / B PCSEQ+PPGRPID / C PCGRPID+PPSEQ / D PCSEQ+PPSEQ, 一致 |
| PP/examples.md:154 Method C 节选 | OK | 人工对 p278 Method C 行 1-8 一致 |

#### 人工逐格: PP Ex2 pp.xpt (p274, 200dpi 渲染)
| Row | 结果 |
|---|---|
| 1 | 一致 (AUCINT / AUC from T1 to T2 / DRUG PARENT / NCA / 154.1 h*ng/L ×2 / PLASMA / LIN-LOG TRAPEZOIDAL METHOD / Y / 1 / 2001-02-01T12:00) |
| 2 | 一致 (DRUG METABOLITE 1, 144.5) |
| 3 | 一致 (DRUG METABOLITE 2, 294.7) |
| 4 | 一致 (RAAUC / Ratio AUC / 1.07 / 单位空 / DRUG METABOLITE 1 TO DRUG PARENT) |
| 5 | 一致 (0.52 / DRUG METABOLITE 2 TO METABOLITE 1) |
| 6 | 除 PPSEQ 外一致 (AUCIFO / AUC Infinity Obs / 520); PPSEQ PDF "1" vs KB "6" → T-5 |
| 7 | 除 PPSEQ 外一致 (AUCIFP / AUC Infinity Pred / 510); PPSEQ PDF "2" vs KB "7" → T-5 |
| 表头 | 20 列一致, 末列 PPRFTDTC (本批改对) |

#### 人工逐格: SUPPPP (p274 渲染)
| Row | 结果 |
|---|---|
| 1-6 | 一致: ABC-123 / PP / 123-1001 / PPSEQ / IDVARVAL 1..6 / PKCOND / Condition of PK Analysis / MULTIPLE DOSE, STEADY STATE / Collected / QEVAL 空 |
| 7 | 一致: IDVARVAL 7 / SINGLE DOSE / **QORIG 空** (PDF 该格无值, writer 改空正确) |
| 表头 | 第 3 列 PDF "DOMAIN", KB "RDOMAIN" → T-6 |

### PDF_TYPO 判定
| # | 判定 | 理由 |
|---|---|---|
| T-1 | 成立, KB 保留正确 | p277 r3 RDOMAIN PC 配 IDVAR PPGRPID 自相矛盾; 文字 "all PC records with GRPID = DY8_DRGX" |
| T-2/T-3 | 成立 | p278 r13/r26 IDVAR PPGRPID / IDVARVAL DY1DRGX 是 PP 侧, RDOMAIN PC 是错 |
| T-4 (MANUAL_02) | 成立, 两处照录正确 | p277 文字 "Rows 14-26 … RELID 2 … DY8DRGX" vs p278 表 RELID 1, r26 DY1DRGX |
| T-5 | 成立 | PPSEQ 同受试者重复 (1,2 已被 r1/r2 占用); SUPPPP IDVARVAL 1-7 指向 PPSEQ 6/7 |
| T-6 | 成立 | SUPPQUAL 结构变量为 RDOMAIN |
| T-7 PPSTRESU "H" | 成立 (疑似), 照录正确 | 新建表无 KB 旧值可保留, writer prompt 规则只说"不改 KB"; 交用户 T4 |
| T-8 散文 DYIDRGX_A / DYIDRGX_HALF + 同页 DYDRGX_HALF (PC/examples.md:278, 284-285) | 成立, 照录正确 | p280 文本层就是如此, 与同页表 DY1DRGX_* 不一致. **DYDRGX_HALF 须补登记为 T-8b** |

### 删除 / RELOCATE 判定 (已逐行比对 diff 的 `-` 行: 除下列各项与改值行外无其它删除)
| # | 判定 | 依据 |
|---|---|---|
| D-1 PP/examples.md p277 PP 表副本 | 合理 (D2 去重) | 留 PDF 所属节 §6.3.5.9.3 "PC-PP – Relating Records" 下 PC/assumptions.md:84-99 (逐格一致); 锚点 `#pc-pp--relating-records` 对应 `### PC-PP – Relating Records` 存在 |
| D-2 SUPPPP RELOCATE Ex1→Ex2 | 搬移合理 | p274 SUPPPP 引句 + 表在 Ex2 pp.xpt 之后、Example 3 之前; 搬后内容逐字未变 (仅 r7 QORIG 按 PDF 置空). **但原处留的指针行有问题, 见缺陷 #1** |
| D-3 "most common pattern" 括注 | 合理 (删扩写) | PDF 无此说; p284 只说 D 记录最多但"可能最易实现", B/C 为 hybrid |
| D-4 "This is what Many to One means…" | 合理 | 方向反了: p275 "Method C (many to one, using PCGRPID and PPSEQ)" = 多 PC 对一 PP |
| D-5 Cross-domain summary 节 | 合理 | 页码全错 (Ex2 实 p279, Ex3 p280, Ex4 p282-283); Ex3 实演示 A-D 四法, Ex4 只有 A (p282) 与 D (p283); 无链接指向 |

### KB_AUTHORED PP/examples.md:108-172 逐条裁定
| 现行号 | 内容 | 裁定 |
|---|---|---|
| :108 标题 | PDF p276-277 原标题 | keep |
| :110 "shared PP dataset contains 12 rows …" | 与 p277 表一致 | keep |
| :112 交叉引用 | D2 产物 | keep |
| :114 "*See PC examples …*" | 导航 | keep |
| :116 节标题 / :118 导语 (已删括注) | 导航 | keep |
| :120-127 Method 映射表 | 与 p275 一致 | keep |
| :129 "canonical mappings … cite this table directly" | 与 PDF 不矛盾的检索提示 | keep |
| :131 Method A 标题 "(p277)" | 页码对 | keep |
| :133-136 Method A 两条 | Rows 3-4 把 PDF "GRPID" 写成 PCGRPID/PPGRPID, 语义正确, 逐字原文在 PC/examples.md:72-73 | keep |
| :138 Method B "(pp 277-278)" + 两条 | 页码对, 内容一致 | keep |
| :145 Method C "(p278)" + 两条 + :152-163 节选表 | 一致 | keep |
| :165 "Reading the PP-side rows …" 首句 | 与表一致 | keep |
| :167 Method D 标题 "(pp 278-280)" | **错**: Ex1 Method D 在 p278 起、p279 止 (p279:35 已是 Example 2; p280 是 Ex2 Method C/D 与 Ex3) | **fix → `(pp 278-279)`**, 见缺陷 #2 |
| :169 "(the most verbose form)" | p284 "Method D results in the largest number of RELREC records" 支持 | keep |
| :171-172 两条 | 与 p278 一致 ("individual PP" 为改写, 不矛盾) | keep |

### G-TB6 反向溯源 (新增 / 改动行)
- PC/examples.md:11-21 (Ex1 叙述 9 行): norm 后逐条在 p270 命中 (11/11 含标题), 弯引号保留.
- PC/examples.md:25-58 PC Ex1 表: 见上, 逐格.
- PC/assumptions.md 21+12 行改值: 逐格对 p276/p277.
- PP/examples.md:9 / :82 (PPRFTDTC): p273 / p274 原文命中.
- PP/examples.md 表行: Ex1 24 行 / Ex3 16 行 / Ex2 表头 / SUPPPP 7 行: 逐格对 PDF.
- 结构行签字: PC/examples.md:5 `## PC – Examples` (p269:46 原标题, 位置与 "Due to space limitations" 顺序一致) ✔; :9 `### Example 1` ✔; :23 `**pc.xpt**` ✔; 表头分隔线 ✔; PP/examples.md:112 D2 交叉引用 ✔; PP/examples.md:68 `**supppp.xpt**` (PDF 无此标签, 随搬保留, 原已存在) ✔.
- 无出处: **PP/examples.md:43** (缺陷 #1).

### 问题表 (修正清单)
| ref | 检查项 | 问题 | 修正 | 证据 |
|---|---|---|---|---|
| #1 PP/examples.md:43 | G-TB6 / 位置 | RELOCATE 后在 Ex1 留了自写指针行 `> See [Example 2](#example-2) for this table (supppp.xpt; PDF p274 places it in Example 2).` "this table" 暗示 Ex1 有 SUPPPP, PDF Ex1 无. D2 "一行交叉引用" 只针对重复副本, RELOCATE (PLAN §6) 是移位, 不留指针 | 删除 :43 及其前一空行 | p273 Ex1 只有 pp.xpt, 后接 "Example 2" |
| #2 PP/examples.md:167 | 位置 (页码) | `### Method D … (pp 278-280)` 页码错 | 改为 `(pp 278-279)`; 全仓无指向此锚点的链接 (grep 0 命中) | p279:35 "Example 2" |
| #3 PP/examples.md:50 | 完整 (R2, 本批文件 + 本批页) | Ex2 Row 4 说明被截断, 止于 "liberates the PPTEST variable", 缺 "from having to house hyper-specific, pre-coordinated PK parameter values." (base 已缺, triage 漏) | 补齐句末; "pre-corrdinating" PDF 拼错, KB 写 "pre-coordinating" 登记 PDF_TYPO T-9 或改照录, 交主控 | p273 Row 4 末句 |
| (登记) T-8b PC/examples.md:278 | PDF_TYPO 清单 | "DYDRGX_HALF" 已照录但没进正式清单 | 写进 PDF_TYPO 清单 | p280:44 |

R2 recheck: 本批 `t2_recheck` 为空, 不适用.
