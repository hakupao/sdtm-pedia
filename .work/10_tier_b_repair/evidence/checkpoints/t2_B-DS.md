# T2 B-DS writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `c3b7b560ac5a4cab450fe1e1c0b7b1f631ffd22e`
- md5 before: DS/examples.md `b2dac284bbd62bf03b3e9c0cc1d537a8`; after `ff4645266f9e831ba6d4afb84de0f192` (行数 413 不变)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-DS_writer/` (examples.before.md, apply.py 44 组精确替换, 每组断言命中次数 (Ex5/Ex6 DSTERM 一组命中 2 次, 其余 1 次), census_before/after.json, fp_before/after.jsonl, p159-167 渲染图 110dpi)
- 数据来源: 改动格逐一对照 p159/p161/p162/p163/p165/p166/p167 渲染图 + `pdftotext -layout`; p160/p164 渲染图已生成 (Ex2-3、Ex10 TA/DM/EX 表 census OK, 以 layout 文本核).
- 本批 atoms 0 / t2_recheck 0; census DIFF 11 表 (54 diffs) 全部处理; pdf_only 0. 叙述缺失按 R3 补 (见"新增 atom 清单").

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | DS/examples.md:28 | census:23 r4 DSSTDTC | REPLACED | 2003-10-15 → 2003-10-31 | 159 |
| 2 | :29 | census:23 r5 DSSTDTC | REPLACED | 2003-11-21 → 2003-11-15 | 159 |
| 3 | :31 | census:23 r7 DSSTDTC | REPLACED | 2003-11-22 → 2003-11-20 | 159 |
| 4 | :34 | census:23 r10 DSSTDTC | REPLACED | 2003-09-30 → 2003-09-22 | 159 |
| 5 | :35 | census:23 r11 DSSTDTC | REPLACED | 2003-10-20 → 2003-10-31 | 159 |
| 6 | :37 | census:23 r13 DSSEQ | REPLACED | 2 → 3 (见 U-3) | 159 |
| 7 | :38 | census:23 r14 DSSEQ, DSSTDTC | REPLACED | DSSEQ 3 → 2; DSSTDTC 2003-09-30 → 2003-09-22 | 159 |
| 8 | :40 | census:23 r16 DSSTDTC | REPLACED | 2003-10-31 → 2003-10-29 (与 Rows 14-16 叙述 "DSDTC 不同于 DSSTDTC" 一致) | 159 |
| 9 | :101-103 | census:101 ae.xpt HEADER/ROW_SHAPE/CELL×3 | TABLE_REBUILT | 表头补 AESCAN (AEOUT 后); 行 1 AESTDTC 09-28 → 09-29; 旗标列 6 → 8 格 (AESCAN N … AESMIE N), 原行少 2 格导致 AESDTH 错位 | 161 |
| 10 | :130 | census:128 r1 DSTERM | REPLACED | "CULTURES. PER" → "CULTURES, PER" | 161 |
| 11 | :150 | census:148 r1 DSTERM | REPLACED | 同上 | 162 |
| 12 | :206 | census:202 r3 DSSTDTC | REPLACED | 2016-04-10 → 2016-04-12 | 163 |
| 13 | :231-233 | census:226 r4/5/6 TESTRL | REPLACED | 句末补 "." ×3 | 163 |
| 14 | :292-301 | census:292 se.xpt HEADER + CELL×14 | TABLE_REBUILT | 表头补 ELEMENT 列 (ETCD 后) + 8 行 ELEMENT 值; r4 SESTDTC/SEENDTC → 04-24/04-24; r5 → 02-04/02-21; r6 SESTDTC → 02-21; r8 SESTDTC → 04-29; 表头 SDSEQ → SESEQ (T-1) | 165 |
| 15 | :320-323, :327, :330 | census:317 r2/3/4/5/9/12 DSSTDTC | REPLACED | 03-13→02-13; 03-14→03-13; 03-19→03-14; 04-20→04-19; 03-23→02-20; 04-25→04-24 | 165 |
| 16 | :346 | census:342 r3 TESTRL | REPLACED (+T-2) | "is AB+C" → "is AB +C" (空格照 PDF; "is" 保留) | 166 |
| 17 | :363-364 | census:355 r9/r10 TATRANS | REPLACED | TAETORD = "5" → "6" / "7" | 166 |
| 18 | :383-387 | census:381 r1-5 SEUPDES/TAETORD ×10 | REPLACED | 值从 SEUPDES 列移到 TAETORD 列 (KB 列错位); SEUPDES 空 | 166 |
| 19 | :15 | R3 N-1 (ig34_p0158_a0023) | INSERTED | 补 "non-completion of" | 158 |
| 20 | :87 | R3 N-2 (ig34_p0160_a0026) | REPLACED | 改写句恢复 PDF 原文 ("and in the AE record was represented"; 见 D-5, U-4) | 160 |
| 21 | :89 | R3 N-3 (ig34_p0160_a0028) | REPLACED (+T-3) | "(DSDTDTC)" → "(DSSTDTC)" | 160 |
| 22 | :122 | R3 N-4 (ig34_p0161_a0013) | INSERTED | 句末补 ", as indicated by DSSCAT = "ISONIAZID"" | 161 |
| 23 | :175 | R3 N-5 (ig34_p0162_a0019) | INSERTED | 补 "for each of the 2 treatments" | 162 |
| 24 | :307 | R3 N-6 (ig34_p0165_a0013) | REPLACED | 乱序句 → PDF 原文 ("may be filled out before treatment starts … until treatment begins"; D-4) | 165 |
| 25 | :313 | R3 N-7 (ig34_p0165_a0016) | INSERTED | 补 "the" | 165 |
| 26 | :336 | R3 N-8 (ig34_p0165_a0034) | INSERTED | 补 "drugs A and B to treatment with" | 165 |
| 27 | :349 | R3 N-9 (ig34_p0166_a0009/a0010/a0011) | REPLACED | 补 AB arm / ABC arm 两句, 拼接错的 "For the AB arm, TAETORD values…" 恢复为 PDF 第 3 句 (D-1) | 166 |
| 28 | :371 | R3 N-10 (ig34_p0166_a0029-a0032) | MOVED | 段落从 ta.xpt 前移到 ta.xpt 后 (PDF 位置); 错句 "stopped after cycle 2 due to toxicity" → PDF 两句 (Drug C cycle 2 / A+B cycle 3 progression) (D-2) | 166 |
| 29 | :393 | R3 N-11 (ig34_p0167_a0004) | INSERTED | 补 "the" | 167 |
| 30 | :395 / :399 | R3 N-12 (ig34_p0167_a0005/a0007) | MOVED | Row 4 尾部 3 句 (未完成治疗/DSSTDTC 定义/末次给药) 移回 Row 6; "follow-up element" → PDF "follow-up epoch" (D-3) | 167 |

### census 表处理

| census ref (before 行号) | 处理 | 结果 |
|---|---|---|
| :23 Ex1 ds.xpt (9) | #1-8 | OK |
| :101 Ex4 ae.xpt (5) | #9 | OK |
| :128 Ex5 ds.xpt (1) | #10 | OK |
| :148 Ex6 ds.xpt (1) | #11 | OK |
| :202 Ex9 ds.xpt (1) | #12 | OK |
| :226 Ex10 te.xpt (3) | #13 | OK |
| :292 Ex10 se.xpt (15) | #14 | DIFF 1 残留 = 表头 SESEQ (T-1) |
| :317 Ex10 ds.xpt (6) | #15 | OK |
| :342 Ex11 te.xpt (1) | #16 | DIFF 1 残留 = "is" (T-2) |
| :355 Ex11 ta.xpt (2) | #17 | OK |
| :381 Ex11 se.xpt (10) | #18 | OK |

- 汇总: before `OK 10 / DIFF 11, cells 1434, diffs 54` → after `OK 19 / DIFF 2, cells 1444, diffs 2 (全为登记 T-1/T-2)`. 范围内 PDF_ONLY before = after = p154-155 pr.xpt / p155 relrec.xpt (PR 节, 非本批文件).

```
S=<scratch>; python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-DS.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl   # 改前同法得 fp_before.jsonl
python3 tools/check_links.py | tail -1   # live docs: 42 (基线 42)
```

### fp_match
- 改前/改后全 KB 跑, 比 hit_target/hit_any 涉及 DS/examples.md 的原子: 变化 0, 回归 0.
- 原因: fp 台账无 p158-167 DS 例子原子 (DS/examples 只作为 p353-358 TU/TR 原子的候选 target 出现, 命中均在 TU/TR). 故 T-3..T-6 的"改 KB 偏离 PDF 拼写"**不产生 fp_match 回归**; 若日后台账纳入 p158-167 原子, 预期回归点 = :89 (DSSTDTC), :120 (epoch), :241 (DG2INDG), :346 ("is"), :292 (SESEQ).

### 新增 atom 清单 (R3, 叙述缺失; atom_id 取 work/pdf_atoms.jsonl)
- N-1 :15 p0158_a0023; N-2 :87 p0160_a0026; N-3 :89 p0160_a0028; N-4 :122 p0161_a0013; N-5 :175 p0162_a0019; N-6 :307 p0165_a0013;
  N-7 :313 p0165_a0016; N-8 :336 p0165_a0034; N-9 :349 p0166_a0009-a0011; N-10 :371 p0166_a0029-a0032; N-11 :393 p0167_a0004; N-12 :395/:399 p0167_a0005/a0007.
- 未做 (仅格式): p161 Ex5 Rows 1/2,4/3,5 中 PDF 粗体 "treatment"/"study" 未加 Markdown 粗体; Ex1 Row 7 / Ex3 Row 4 PDF 弯引号/弯撇号, KB 直引号未改.

### 删除清单 (reviewer 逐条确认)

| # | 原位置 (base 行号) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | :349 "For the AB arm, TAETORD values are not chronological for this arm" (把 AB 句头接到 ABC 句尾的拼接改写) | :349 PDF 3 句 | R2 残留改写 (该行无 fp 台账原子) | — |
| D-2 | :351 整段 (ta.xpt 前) 含错句 "Treatment with drugs A and B was stopped after cycle 2 due to toxicity associated with drug C." | :371 (ta.xpt 后, PDF 位置) PDF 原文 4 句 | 与 PDF 矛盾 + 位置错; 先插后删 | :371 |
| D-3 | :395 Row 4 尾部 3 句 | :399 Row 6 (PDF 归属) | 归属错; 先插后删; "element" → PDF "epoch" | :399 |
| D-4 | :307 "does not end until treatment starts, the screening epoch does not end until treatment starts" | PDF 原文 | 乱序改写, 与 PDF 语义不同 | — |
| D-5 | :87 "and AE record is represented" | "and in the AE record was represented" | 词替换型改写, 该行无其他原子 → 恢复 PDF 原词 | — |

### PDF_TYPO 清单 (正确值可由 PDF 自身确定 → KB 写正确值)

| # | 位置 | PDF | KB | 依据 |
|---|---|---|---|---|
| T-1 | :292 Ex10 se.xpt 表头 | SDSEQ | SESEQ | SE spec 变量名 SESEQ; 同文件 Ex11 se.xpt (p166) 表头 SESEQ; 表头印刷错规则. census 残留 1 |
| T-2 | :346 Ex11 te r3 TESTRL | "where treatment AB +C" | "where treatment is AB +C" | 漏 "is": 同表 r2 平行句 "where treatment is AB". 空格 "AB +C" 无法由 PDF 确定 → 照录 (见 U-6). census 残留 1 |
| T-3 | :89 Ex4 叙述 | "(DSDTDTC)" | "(DSSTDTC)" | 无此变量; 句指参与结束日 = DSSTDTC (同表列). 改前 KB 照抄 PDF 错 |
| T-4 | :120 Ex5 Row 1 | "epocch" | "epoch" | 拼写错, KB 已是正确拼写 (未动) |
| T-5 | :377 Ex11 Row 5 | "recieved" | "received" | 同上 (未动) |
| T-6 | :241 Ex10 TA Rows 3, 7 | `" DG2INDG"` (引号内前导空格) | `"DG2INDG"` | ETCD 值无空格 (同页 TA 表); KB 未动 |

### 照录 PDF, 供主控 / T4 用户裁 (KB = PDF)
- U-1 :294/:298 Ex10 se.xpt ETCD "SCREEN" vs 同例 TE/TA "SCRN" (跨表不一致; 规则未列跨表为可确定依据 → 照录).
- U-2 :407-409 Ex11 ds.xpt 筛选期 3 行 TAETORD = 1, 而 TA/SE 筛选元素 TAETORD = 0 (跨表).
- U-3 :37-38 Ex1 subject 123104 DSSEQ RANDOMIZED=3 / COMPLETED=2 (与其他受试者相反, 但与 DSSTDTC 先后 09-30 / 09-22 一致, 非错; 照 PDF 改). 另 :34/:38 筛选完成 DSSTDTC 09-22 早于随机化 09-30, PDF 明载.
- U-4 :87 PDF 原句语法 "and in the AE record" 照录.
- U-5 :264-265 Ex10 dm.xpt Row 1, 3 (无 Row 2): 例 10 叙述 "Not all records are shown", 非 typo; KB = PDF, 未动.
- U-6 :346 "AB +C" 空格 (见 T-2).

### KB_AUTHORED
- 无 (本文件无 KB 自写导航/占位).

### 范围外发现
- 无.

### 触碰过的 unparseable 表
- 无.

### git diff --stat -- kb_files
```
 knowledge_base/domains/DS/examples.md | 110 +++++++++++++++++-----------------
 1 file changed, 55 insertions(+), 55 deletions(-)
```

### 叙述原子扫描 (补充; census 不覆盖叙述, fp 台账无 p158-167 原子)
- 方法: p158-167 全部 SENTENCE/LIST_ITEM 原子 (work/pdf_atoms.jsonl) 归一 (去 `**`、合并空白、弯引号直化) 后在 DS/examples.md 中做子串检查.
```
python3 -I - <<'PY'   # repo root
import json,re
def n(s): s=s.replace('**','').replace('\u201c','"').replace('\u201d','"').replace('\u2019',"'").replace('\t',' '); return re.sub(r'\s+',' ',s).strip()
K=n(open('knowledge_base/domains/DS/examples.md').read())
for l in open('.work/10_tier_b_repair/work/pdf_atoms.jsonl'):
    d=json.loads(l); m=re.match(r'ig34_p0(\d+)_',d['atom_id'])
    if m and 158<=int(m.group(1))<=167 and d['atom_type'] in ('SENTENCE','LIST_ITEM') and n(d['verbatim']) not in K: print(d['atom_id'])
PY
```
- 结果 (改后) 未命中 9 条: p0158_a0001-a0004 (DS assumptions 内容, 非本文件), p0167_a0020 (HO 节) — 不属本文件;
  p0160_a0028 (T-3 DSSTDTC), p0161_a0012 (T-4 epocch), p0164_a0004 (T-6 " DG2INDG"), p0166_a0035 (T-5 recieved) — 即**预期回归清单**, 全部已登记. 无其他叙述缺失.
- 原子抽取错 (T3 台账注意): ig34_p0167_a0010 (Ex11 ds.xpt) 表头记作 `DSEQ`, 渲染 p167 为 `DSSEQ`.

### 标签更正 (同 attempt)
- jsonl 中 T-1 (:292 SESEQ)、T-2 (:346 "is")、T-3 (:89 DSSTDTC) 为 KB **偏离 PDF** 的改动, action = REPLACED (note 标 T-n); SKIPPED_PDF_TYPO 只用于 KB 未动的 T-4/T-5/T-6. 变更清单 #14/#16/#21 同此口径.
- jsonl census ref 格式 `census:DS/examples.md:<改前 KB 行>:<row>:<col>`, 共 54 行 = census diffs 54.
