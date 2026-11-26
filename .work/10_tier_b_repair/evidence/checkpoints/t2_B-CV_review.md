# T2 B-CV reviewer

## attempt 1 (2026-11-26T04:38:28Z, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base = HEAD (8e5016e), 本批文件未提交改动; scratch `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CV_reviewer/`
- 节页范围核: §6.3.7.2 CV = p286 下半页 (Description/Overview + Specification 首句 + spec 表首行) → p287-288 (spec 续 + 脚注 + CV – Assumptions 1-2) → p289 (CV – Examples Ex1/Ex2); p290 起 MK. p286 上半页 §6.3.7.1 通用表属 B-NV, 未碰. batch lo/hi 286-289 完整覆盖.
- 本批 diff: 仅 `knowledge_base/domains/CV/assumptions.md` (+10) 与 `knowledge_base/domains/CV/examples.md` (3 行改); `CV/spec.md` 未动. 工作树 NV/RS 改动属他批, 不计.
- md5 (与 writer 报告一致): assumptions `2fc68d6a9db973b6df5115de8e06ad80`, examples `71e6f9abbe39847649e907a3202e464b`, spec `de8c6d00e0a9dddeadd8c872d509170e`.

### 命令与关键输出 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CV_reviewer; P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
git diff HEAD --stat -- knowledge_base/domains/CV/      # 2 files, 13+/3-
pdftotext -f 286 -l 286 -raw "$P" - | tr '\n' ' ' | sed 's/  */ /g' | grep -o "A findings domain that contains physiological.*vessels\." | tr -d '\n' | cmp - <(sed -n 5p knowledge_base/domains/CV/assumptions.md | tr -d '\n')   # IDENTICAL
pdftotext -f 286 -l 286 -raw "$P" - | grep "^cv.xpt" | sed 's/ *$//' | tr -d '\n' | cmp - <(sed -n 9p knowledge_base/domains/CV/assumptions.md | tr -d '\n')   # IDENTICAL
pdftotext -f 286 -l 288 -raw "$P" - | grep "^CV –" | xxd     # 标题 U+2013 (e2 80 93), 与 KB "## CV –" 字节一致
# manifest = batch pdf_ranges + CV/assumptions.md (286-289)
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1 (全局 PDF_ONLY 337; 页 286-289 内 0); KB tables 2, status OK 2, diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # RESULT: RED (全局)
grep -E '"ig34_p028[6-9]' $S/fp_regress.jsonl   # 仅 a024, a025
for p in 286 288 289; do pdftoppm -f $p -l $p -r 130 -png "$P" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### 检查结果
1. 完整: atoms 1 (ig34_p0286_a017) → INSERTED, fp_after hit_target = CV/assumptions.md (baseline null). t2_recheck 0. census DIFF 1 表 3 格全处理, census_after OK. 页 286-289 pdf_only 0, pdf_unparsed 0.
2. G-TB4: Ex1 / Ex2 两张 cv.xpt census OK; 另对 p289 130dpi 渲染图独立人工逐格核 (下表).
3. G-TB6 反向溯源: 新增/改动行均在 PDF 找到出处 (签字清单); 无自造词句.
4. 位置: Description/Overview + Specification 首句 + Assumptions 标题按 CM 先例置于 assumptions.md 顶部, 顺序同 PDF (Description → Specification → [spec 表在 spec.md] → Assumptions).
5. 无副作用: 原 assumptions 1-2 逐字未变 (与 p288 -raw 规范化文本一致); examples.md 只改 3 格 CVTEST; 无既有标题/锚点改动; 均在授权范围.
6. R2 recheck: 无条目.
7. D6: 两文件无 KB 自写解释性内容; 文件 H1 / Example N 标题 / cv.xpt 表前标签为既有导航.
8. 双向全扫 (p286 下半-p289): PDF→KB 叙述 (Description, spec 首句, Assumptions 1-2, Ex1/Ex2 引言) 与表格原子全在 KB; KB→PDF 两文件逐行有出处. spec 表 (p286-288) 属 spec.md, 不在本批.

### 回归核 (主控指定): ig34_p0289_a024 / a025
- pdf_atoms verbatim 为 "Minor/Major Axis Cross-sec Diameter, MVS" (无点); baseline 已标 in_pdf_page: false (原子与 PDF 不符信号).
- p289 渲染图 Ex2 行 7/8 CVTEST 清晰为 "Cross-sec." (带点), 行 3-6 为 "Cross-sec" (无点); pdftotext -layout 同. CT C139052/C139053 = "… Cross-sec. Diameter, MVS", C127576 (EVS) 无点, 与 PDF 逐行一致.
- 结论: writer 说法成立, 回归属原子抽取错, KB 现值正确, 不计本批退化. 建议主控在 pdf_atoms 勘误登记这两条.

### 人工逐格表 (p289 渲染 130dpi)
| 表 | 行 | 结果 |
|---|---|---|
| Ex1 cv.xpt | 表头 15 列 (Row…CVDTC) | 一致 |
| Ex1 | 行 1-3 (CVGRPID 2; ANEURIND/DISECIND/STANFADC; Y/Y/CLASS A; THORACIC AORTA) | 一致 |
| Ex1 | 行 4-5 (CVGRPID 空; ANEURIND; N; SUPRARENAL / INFRARENAL AORTA) | 一致 |
| Ex1 | 全行 ABC123/CV/002-2004/TRANSTHORACIC ECHOCARDIOGRAPHY/2/BASELINE/2015-06-09T14:20 | 一致 |
| Ex2 cv.xpt | 表头 18 列 (Row…CVDTC, 含 CVCAT/CVORRESU/CVSTRESN/CVSTRESU) | 一致 |
| Ex2 | 行 1 NCVALTYP "Native Cardiac Valve Intervention Type"; NATIVE, WITHOUT INTERVENTION ×2; 单位/数值空; CVLOC AORTIC VALVE | 一致 (改后) |
| Ex2 | 行 2 SIZE/Size/REDUCED ×2; CVLOC AORTIC VALVE ANNULUS | 一致 |
| Ex2 | 行 3-6 MNDIAEVS/MJDIAEVS/MNDIAEVD/MJDIAEVD "… Cross-sec Diameter, EVS/EVD"; 2.18/2.48/1.92/2.58 cm | 一致 |
| Ex2 | 行 7-8 MNDIAMVS/MJDIAMVS "… Cross-sec. Diameter, MVS"; 2.11/2.39 cm | 一致 (改后) |
| Ex2 | 全行 CVCAT VALVULAR STRUCTURE, COMMON; TRANSTHORACIC ECHOCARDIOGRAPHY; 5; MONTH 2; 2015-08-05T11:15 | 一致 |

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无阻断问题 | — |
| CV/spec.md:3 (范围外, LOW) | 观察 | spec.md 头部既有 Class/Structure 摘要行与新增 spec 首句信息重复; 不在本批授权, 不改, 仅记录 | p286 "cv.xpt, Cardiovascular System Findings — Findings. One record per …" |

### G-TB6 结构行 / 新增行签字清单
| KB 行 | 内容 | 出处 / 判定 |
|---|---|---|
| assumptions.md:3 | 标题 CV – Description/Overview | p286 原小标题, 签字 |
| assumptions.md:5 | Description 句 | p286 逐字 (cmp IDENTICAL) |
| assumptions.md:7 | 标题 CV – Specification | p286 原小标题, 签字 |
| assumptions.md:9 | spec 首句 | p286 逐字 (cmp IDENTICAL) |
| assumptions.md:11 | 标题 CV – Assumptions | p288 原小标题, 签字 |
| assumptions.md:2/4/6/8/10 | 空行 | 结构 |
| examples.md:25/31/32 | CVTEST 3 格 | p289 渲染图 + CT C139050/52/53 |

### 结论
PASS. 无 CONDITIONAL 修正项. live docs 42 (基线 42).
