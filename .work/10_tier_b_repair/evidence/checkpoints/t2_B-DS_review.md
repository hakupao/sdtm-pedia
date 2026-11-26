# T2 B-DS reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

范围: `git diff c3b7b56 -- knowledge_base/domains/DS/` (仅 DS/examples.md, 55+/55-; 其他 KB 文件属并行批次, 未审). scratch = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-DS_reviewer/`.

### 命令 (repo 根, S=上述 scratch)
```
python3 -I -c "...pdf_ranges -> $S/manifest.json"            # 同 prompt
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  -> exit 1; KB tables 21; OK 19 / DIFF 2; cells 1444; diffs 2 (= T-1 SESEQ 表头, T-2 "is")
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  -> exit 1 (RED); regressions 13 全部 CP(p215)/MB(p257-263) 原子, 0 条涉 DS (grep '/DS/' fp_regress.jsonl = 0)
python3 tools/check_links.py | tail   -> live docs: 42 (≤ 42)
python3 -I $S/scan.py   # 独立叙述扫描: KB 非表行逐句 ⊂ PDF p158-167 归一文本; PDF 句 ⊂ KB
pdftoppm -f N -l N -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/pN  (N=159,165,166)
```
- census PDF_ONLY / pdf_unparsed 落在 p155-167 的: 仅 p151-155 CE/MH/PR/relrec (6.2.3, 非本批), DS (6.2.4) 0.

### G-TB4 独立逐格复核 (方法: pdftotext -layout 列位置文本 `work/pdf_pages/ig34_p0159..0167.txt` 逐行目读 + p159/p166 渲染图; 未用 bbox 解析器)
| 表 | 改动格 | 结果 |
|---|---|---|
| Ex1 ds.xpt p159 | r4 DSSTDTC 10-31; r5 11-15; r7 11-20; r10 09-22; r11 10-31; r13 DSSEQ 3; r14 DSSEQ 2 + DSSTDTC 09-22; r16 10-29 | 全部一致 (渲染图确认折行日期); 未改行 r1-3,6,8,9,12,15,17-21 亦一致 |
| Ex4 ae.xpt p161 | 表头 AESCAN 位于 AEOUT 后; AESTDTC 09-29; 旗标 AESCAN..AESMIE = N N N Y N N N N | 一致 (23 列) |
| Ex5 / Ex6 ds.xpt p161/162 | DSTERM "CULTURES, PER PROTOCOL" | 一致 |
| Ex9 ds.xpt p163 | r3 2016-04-12 | 一致 |
| Ex10 te.xpt p163 | r4/r5/r6 TESTRL 句末 "." | 一致 |
| Ex10 se.xpt p165 | ELEMENT 列 8 值 (Screen/Drug-1/Drug 1 + Investigational Drug/Follow-up/…); r4 04-24/04-24; r5 02-04/02-21; r6 02-21; r8 04-29 | 一致; 表头 SESEQ ≠ PDF SDSEQ = T-1 |
| Ex10 ds.xpt p165 | r2 02-13; r3 03-13; r4 03-14; r5 04-19; r9 02-20; r12 04-24 | 一致 |
| Ex11 te.xpt p166 | r3 "AB +C" | 一致 (渲染图); "is" = T-2 |
| Ex11 ta.xpt p166 | r9 TAETORD = "6", r10 = "7" | 一致 (渲染图) |
| Ex11 se.xpt p166 | SEUPDES 空, TAETORD 0/1/2/6/8 | 一致 (渲染图) |
census 54 diffs ↔ writer.jsonl 54 census 行 (REPLACED 35 + TABLE_REBUILT 19), 一一对应.

### T-1..T-3 (KB 有意 ≠ PDF) 判定
| T | 判定 | 依据 |
|---|---|---|
| T-1 se.xpt 表头 SDSEQ→SESEQ | 成立 | 表头印刷错规则; SE spec 变量 SESEQ; 同文件 Ex11 se.xpt 表头 SESEQ |
| T-2 "where treatment AB +C"→"is AB +C" | 成立 (LOW 注) | 同表 r2 平行句 "where treatment is AB"; base KB 本已有 "is" (保留合理值). 依据属"同表平行行", 不在口径枚举的 4 类中字面出现, 供 auditor 知悉 |
| T-3 "(DSDTDTC)"→"(DSSTDTC)" | 成立 | 无此变量; 紧随 ds.xpt 同例表列 DSDTC/DSSTDTC + 句义 (participation ended) |
T-4/T-5/T-6 (epocch / recieved / " DG2INDG"): KB 保持正确拼写未动, 符合 PDF 自身拼写错规则.

### U-1..U-6 (照录 + T4) 判定: 全部确认无法由 PDF 自身单值确定
- U-1 SE "SCREEN" vs TE/TA "SCRN": 跨表, 哪侧错不可由同表确定 → T4 合理 (注: SE.ETCD ∈ TE 属 spec 约束, 用户若裁定 spec 可作依据则可改).
- U-2 Ex11 ds TAETORD=1 (筛选) vs TA/SE 0: 跨表 → T4. U-3 DSSEQ 3/2 与日期先后一致, PDF 明载, 非错. U-4 语法照录. U-5 dm Row 1,3 与 "Not all records are shown" 一致. U-6 空格照录.

### 叙述 N-1..N-12 (逐条对 PDF 原文)
N-1 p158 "non-completion of" ✓; N-2 p160 "and in the AE record was represented" ✓; N-3 = T-3; N-4 p161 ", as indicated by DSSCAT = "ISONIAZID"" ✓; N-5 p162 "for each of the 2 treatments" ✓; N-6 p165 "may be filled out before treatment starts … until treatment begins" ✓; N-7 p165 "the study participation follow-up epoch" ✓; N-8 p165 "drugs A and B to treatment with drugs A, B, and C" ✓; N-9 p166 TA 段 3 句 (AB arm match cycle numbers / ABC arm transition / not chronological) 逐字 ✓; N-10 p166 段落位于 ta.xpt 之后、"The SE dataset records…" 之前, 4 句逐字 ✓ (位置 = PDF); N-11 p167 "for the screening epoch" ✓; N-12 p167 Row 4 仅留首句, 3 句归 Row 6, "follow-up epoch" ✓ (位置/内容 = PDF).

### 删除 D-1..D-5 (逐条 diff)
| D | 删除内容 | 判定 |
|---|---|---|
| D-1 | "For the AB arm, TAETORD values are not chronological for this arm…" (拼接改写) | 合规; PDF 3 句完整替代, 无内容丢失 |
| D-2 | ta.xpt 前整段含 "Treatment with drugs A and B was stopped after cycle 2 due to toxicity associated with drug C." | 合规; 与 PDF 矛盾 (PDF: Drug C dropped cycle 2 / A+B stopped cycle 3); PDF 原文已在 ta.xpt 后 |
| D-3 | Row 4 尾部 3 句 | 合规; 移至 Row 6 (PDF 归属), 无丢失 |
| D-4 | "does not end until treatment starts, the screening epoch…" | 合规; 乱序改写, 已恢复 PDF |
| D-5 | "and AE record is represented" | 合规; 恢复 PDF 原词 |

### 独立叙述扫描 (检查 6) 结果
- KB→PDF 未命中 4 句: :89 (T-3), :120 (T-4), :241 (T-6), :377 (T-5) — 全部已登记; 所有 `**Row(s) …:**` 标签均在 PDF 中.
- PDF→KB 未命中: p158 DS assumptions 5/6 (非本文件), p167 HO 节 (非本文件), 及 ta.xpt 表格串行文本 (非叙述), T-4/T-6 原文. **无剩余叙述缺失 / 错配.**

### D6
- 扫描显示 DS/examples.md 无任何 PDF 无出处的解释性句子 → 无需 `> KB note (not in SDTMIG):`; 文件中亦无该标注 (一致). writer "KB_AUTHORED 无" 成立.

### G-TB6 结构行签字
- :101-102 ae.xpt 表头 + 分隔线 (补 AESCAN) — 签字; :292-293 se.xpt 表头 + 分隔线 (补 ELEMENT, SESEQ) — 签字. 其余 diff 行均为数据/叙述, 已逐条溯源 PDF. 无标题/锚点变动.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| :346 T-2 | PDF_TYPO 依据 | LOW: 依据为同表平行行, 非枚举类; 可接受, 请 auditor/T4 知悉 | p166 r2 "where treatment is AB" |
| :294/:298 U-1 | T4 | LOW 注: 若用户接受 spec (SE.ETCD ∈ TE.ETCD) 为依据, 可改 SCRN | p163 TE "SCRN"; p165 SE "SCREEN" |
| 全局 fp RED | 无副作用 | 13 条回归全属 CP/MB, 非 B-DS 造成 (需对应批 reviewer 关注) | fp_regress.jsonl |

R2 recheck: 本批 t2_recheck = 0, 无.
