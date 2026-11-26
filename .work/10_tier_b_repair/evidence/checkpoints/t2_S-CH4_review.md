# T2S S-CH4 reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (无 CRITICAL/HIGH/MEDIUM; 4 条 LOW 观察, 不阻断)

- 对象: `git diff HEAD -- knowledge_base/chapters/ch04_general_assumptions.md` (1566→1584 行, md5 `40832488e41bf01dd3dd5b6b54e56b06` = writer delta 终态). 本批只改 ch04; 工作树其余 diff (ch08/ch10/model02) 属并行批, 不计. narrow_files 空.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH4_reviewer/`. 自写 `scan.py` (不复用 writer 脚本): 直接 `pdftotext -layout` PDF p22-59 (不用原子); KB 侧先剔 D6 块 (`> KB note` 引用块 + 紧随表/Mermaid/图注); 归一 = 去空白/连字符/markdown 符号, 统一引号 dash.
- 页范围复核: p22 首行 `4 Assumptions for Domain Models`, p59 末 = §4.5.9 收尾段, p60 起 §5 → **22-59 成立**.

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH4_reviewer
python3 -I $S/scan.py p2kt '\s{2,}|•'      # PDF 行→KB (散文 + 表格行, KB 表格去竖线后比): MISS 18, 全部定性 (见下)
python3 -I $S/scan.py k2p2                 # KB 句/表格→PDF: 未连续命中项均为 标题/导航/xpt 标签/多行单元格 (词级全命中) 或已登记 T-n
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1; OK 19 / UNPARSEABLE 38 / DIFF 1 (eg = T-1, diffs 2); p22-59 PDF_ONLY 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # exit 1 RED; 71 regress 全在 t2_fp_expected_regressions.jsonl; 本批页 p22-59 及 p115/p261 回归 0
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42; ch04 源无坏链
for p in $(seq 22 59); do pdftoppm -f $p -l $p -r 100 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done   # + p32/p33 130dpi
```

### 双向全扫 (p22-59)
- PDF→KB MISS 18 定性: p22:1 章标题 (= KB H1, 规则 6); 页脚 ×9 (p25/53/54); p26:55 VISTNUM = T-7; p37:2 = T-3; p43:13 `"ONGOING"'` = T-8; p49:11 occurrs = T-4; p53:28 Ex2 Row 1 LBSTRESC = T-5; p57:20 "result or of" = T-6; p59:18/26 baseline 表多行单元格折行 (渲染核一致). **无未定性缺口**.
- KB→PDF (D6 块外): 未命中 = 标题行 (节号/空格差)、`Source:`/`## Overview`/`## Appendix` 导航、`ae.xpt:` 等数据集标签 (U8 表前短标签)、:905/:906 列表内 D6 行、:932 T-8、:1344 T-5、:1582/:1584 交叉引用; 其余 74 项为多行表格单元格, 词级全命中且渲染逐格一致. **无 D6 块外无出处解释句**.
- 渲染逐页核: p28/30/31/32/33/35/36/38/39/40/41/42/43/44/45/46/47/48/51/52/53/55/56/58/59 已开图对照.

### census_items 逐格 (39 项, 不采信 writer; 行号 = 终态)
| # | KB 表 | PDF 页 | 结果 |
|---|---|---|---|
| 1 | :408 EXADJ CRF | p32 | 表头 2 格 + 3 行一致; 选项符号 = U4 (S-TYPO) |
| 2 | :425 Indication for analgesic CRF | p32 | PDF 单行双格无表头 → KB 右表头空, 6 选项一致 |
| 3 | :470 Eye Color CRF | p33 | 5 选项一致 |
| 4-6 | :482/:488/:494 SCTEST ×3 | p33 | 各 2 行 × 3 一致 (OTHER / GRAY / BLUEISH GRAY) |
| 7 | :504 伴随药 CRF | p33 | 问句 + 5 选项一致 |
| 8 | :514 CMTRT/CMPRESP | p33 | 3 行 × 2 一致 (DICLOFENAC 空) |
| 9-13 | :574/:580/:592/:598/:613 ae/suppae | p35 | 全格一致 |
| 14 | :619 suppae (AERELX/AEACNX) | p36 | 一致 |
| 15 | :695 主题变量表 | p38 | 6 行 × 4 一致 (DS Modified 空) |
| 16 | :766 精度表 | p39 | 8 行 × 4 一致; 首列表头 PDF 空 ✓ |
| 17 | :778 区间表 | p40 | 5 行 × 3 一致 |
| 18 | :1053 Collection Type | p45 | 3 行 × 4 一致 |
| 19-20 | :1095 VS / :1105 LB 时间点 | p46 | 各 4 行 × 6 一致 |
| 21-22 | :1131 Option 1 / :1154 Option 2 | p47/p48 | 19 行 × 5 一致 (合并格首行填值) |
| 23 | :1536 --PRESP 情况表 | p58 | 5 行 × 4 一致 |
| 24 | :52 Core 表 | p23 | D6 (KB_AUTHORED), 不矛盾, 未改 |
| 25 | :235 MK 表 | p28 | 2 行 × 7 一致 |
| 26-30 | :438/:442/:448/:452/:460 CMINDC/QNAM 小表 | p32 | 一致 |
| 31 | :787 省略分量表 | p40 | 7 行 × 4 一致 |
| 32 | :842 时长表 | p41 | 11 行 × 2 一致 |
| 33 | :918 lb.xpt visit | p42 | 4 行 × 5 一致 |
| 34-36 | :938 / :959 / :1078 D6 表 | p43/44/46 | D6, 与 PDF 句不矛盾, 未改 |
| 37 | :1353 eg.xpt | p53-54 | census DIFF 2 格 = T-1 (沿用) |
| 38 | :1475 >200 约定表 | p56 | 4 列 × 3 行 + 4 表头格逐格一致 (删 Convention 列后) |
| 39 | :1570 baseline 表 | p59 | 4 行 × 5 一致 |

### 删除 / 结构改动签字
| 项 | 签字 | 依据 |
|---|---|---|
| D-1 "at"→"(URL) … codes)." | ✓ | p23:24-25 原文 |
| D-2 "— xx.xpt" 拆行 ×6; "(xx.xpt)" ×3 | ✓ | p25/26 标题与 xpt 两行; p53-54 "Example n" 与 "lb.xpt" 分行 |
| D-3 "Options" ×3 / "#" ×3 | ✓ | p32/33 CRF 无表头词; p39/40 首列表头空 |
| D-4 / S-3 Convention 列 | ✓ | p56 PDF 4 列; Storage/Split rule/Label 为 KB 概括, 各行单元格 PDF 原文自身已表达, 且 §4.5.3.2 列表 :1405-1410 逐条承载 → 无信息丢失, 不需 D6 |
| D-5 Mermaid 节点 / "The medical event" | ✓ | p44 图框文字 "MHENTPT Assessment Date and Reference Time Point of 2006-11-02"、"2002"、"The medical event may or may not…" |
| D-6 / S-5 Appendix 去重 | ✓ | 副本在 EX/examples.md:239 (`## Example 6` :235, 唯一 → 锚点 example-6 有效) 与 MB/examples.md:156-158 (`### Example 3` :93-230 内, 唯一 → example-3 有效); fp p0115_a028→EX, p0261_a002/a003→MB 命中; 全库无 ch04 锚点入链; check_links ch04 无坏链 |
| **D-7/D-8/D-9 "Example 1/2/3"** | ✓ | **p35 渲染图与文本层均无 "Example N" 标签** (ae.xpt 表前直接是 "The following example includes…"、"For example, a sponsor…"、"For example, if Abcicin…"); 删除正确, 非 CONDITIONAL. (对照: p52-53 / p55-56 PDF 确有 "Example 1/2/3", KB 保留 ✓) |
| D-10/D-11 | ✓ | p43 同段连续文字, 无 "Important restriction"/"Caution" 标签 |
| D-12 | ✓ | p47 "Not all time points will…" 前无标签 |
| D-13 | ✓ | p55 "IETEST values in the…" 紧接 QLABEL 句, 无 "Exception" 标签 |
| D-14 | ✓ | p56 "The following domains have specialized conventions…" 前无标签 |
| S-1 编号/层级 (:328-376) | ✓ | p30 代码块 STUDYID/DOMAIN 同级、--CAT/--SCAT、USUBJID、--GRPID/--LNKID/--LNKGRP 三级; "For the subject" 下 "1."; c. 段 "Stress-test…" 另起 + i./ii./iii.; "Within subjects" 下 "1."; p31 --LNKID/--LNKGRP "1./2." |
| S-2 (:1117-1120) | ✓ | p47 4 条为圆点列表 |
| S-4 | ✓ | 同 D-2 |
| #13a/#14 图标题 ×3 | ✓ | p44 / p46 / p51 "Figure. …" 原文 |
| #10 "For example," ×2 / #3 "." / #11 "." + "e.g." | ✓ | p35:1 / p36 / p26:58 / p39:5,19 原文 (e.g. 照 PDF, 主控裁定 4) |

- Mermaid p44: 节点 2002 → 参考时间点 (实线) → 之后虚线延伸, CTP 框挂在参考时间点下; 与图逻辑一致; D6 已注明 "added edge labels not in the figure" ✓. p51 --ORRES→--STRESC→--STRESN 一致, D6 已注明增边 ✓.
- 列表渲染: i./ii./iii. 与既有 a./b./c. 同为缩进段落 (非 markdown 列表标记), 渲染为带前缀文字段, 层级可读; 不阻断.
- T-8 (p43 `"ONGOING"',`)、T-9 (p47 "(–TPTREF")、T-10 (p27 `") ."` / `"MKHNDPOS".This`; p32 "field :"; p43 "variables.As" / "CMSTRF.Some"; p51 "derived.For"; p54 "VSTESTCD= ") 均在原页/渲染确认, 依据成立.
- D6: 新增 0, 修改措辞 1 (:1003) ✓; 既有 D6 复核不矛盾.
- G-TB6: diff `+` 非空行全部有 PDF 出处或为结构行 (图标题 3、数据集名行 9、交叉引用 2); 无出处 0.

### LOW 观察 (不阻断)
| ref | 问题 | 建议 |
|---|---|---|
| L-1 :988/:1017/:1033 `**Example n: …**`, :341/:345/:367 粗体 | PDF 为常规字体 | S-CH1 口径: 强调差异不改 |
| L-2 :906 `- > KB note (not in SDTMIG): **VISIT**: …` | D6 以列表项形式嵌在 PDF 列表中 (既有) | 不矛盾, 保留; 可在 T3 统一 D6 版式 |
| L-3 :1305 D6 "--ORRESU and --STRESU should also be null" | PDF 未直述 NOT DONE 时单位 (既有 D6) | 不矛盾, 保留 |
| L-4 dash 类 (:1103 U+2212, :1477/:1491/:1520 "SUPP--" vs PDF en dash, :324 em dash 空格) | 排版字符 | 归 S-TYPO (writer 已登记范围外) |
