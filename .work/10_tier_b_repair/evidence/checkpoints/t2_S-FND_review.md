# T2S S-FND reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (无 CRITICAL/HIGH/MEDIUM; 5 条 LOW 观察, 不阻断)

- 对象: `git diff HEAD -- knowledge_base/domains/{EG,OE,UR,PE,SS,DA}` (HEAD `056d8cc`), 12 文件 +73/-15. scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-FND_reviewer/`
  自用脚本 (不复用 writer 的): `speccmp.py` / `ctdump.py` / `ctpart.py` (pdftotext -bbox 按表头 x 分列, 逐变量逐字段 + CT 列分类), `bscan.py` (k2p/p2k 逐句), `ascan.py` (pdf_atoms 全类型原子 → 本域三文件, fp_match.norm), diff 新增行逐字检查 (仅空白归一, 不归一 dash/引号). 渲染: p180 顶部; p186/299/313/316/343 左半 (CT 列) 130dpi; p304 relrec+oe 160dpi 三段; p305 全页; p312 全页; p316 PELAT 行 200dpi; p301 asm 3 行 200dpi.
- 授权范围: 本批改动 12 文件全部 ∈ kb_files, 另 DA/assumptions.md (narrow) diff 仅 H1 后 +4 行 (§6.3 标题 + 引言句), 其余未动. 工作树内其他域 (AG/CP/EC/EX/GF/IS/LB/MB/MS/PC/PP/PR) 改动属并行批. EG/OE/UR/PE examples.md 未动.

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-FND_reviewer
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1; KB tables 20: OK 18 / DIFF 2; cells 2136; diffs 5 (= OE T-1 ×1 + T-2 ×4)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # exit 1 RED; 67 regress; 对 t2_fp_expected_regressions.jsonl 差集 7, 全在别批页 (p199/200/206 CP, p240 IS, p255 MS); 本批页 (180,185-192,298-305,312-318,342-344) 回归 0
for d p in EG 185,186,187,188 OE 299,300,301 UR 312,313,314 PE 316,317 SS 342,343; do python3 -I $S/speccmp.py $S $d $p; done   # 非 CT 字段仅 PELAT notes 差 (T-1); CT 差仅 U5/U6
python3 -I $S/ctpart.py $S EG OE UR PE SS          # CT 列逐变量分类 (见下)
for d lo hi in EG 185 192 OE 298 305 UR 312 315 PE 315 318 SS 342 344; do python3 -I $S/ascan.py $d $lo $hi; python3 -I $S/bscan.py k2p $lo $hi knowledge_base/domains/$d/assumptions.md knowledge_base/domains/$d/examples.md; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### 页范围复核 (O20)
- EG 185-192 (p185 上部 dd/ds/relrec + 叙述属 §6.3.2; p193 首行 §6.3.4 IE) — 同意 writer, json 已更正 hi=192. OE 298-305 (p298 上部 NV Ex2; p305 中部 §6.3.7.6 RP 起). UR 312-315 (p312 上部 RE suppre/di; p315 中部 §6.3.8 起). PE 315-318 (p318 下部 §6.3.9 起). SS 342-344 (p342 上部 SC Ex2/Ex3; p344 下部 §6.3.12 起). DA 引言 p180 顶部.
- census PDF_ONLY 落在本批页的 8 项 (p185 dd/ds/relrec; p298 nv; p312 suppre/di; p342 sc ×2) + pdf_unparsed p342 sc.xpt — 均别节, 不计 (writer 记 7, sc 两张计一; 不影响结论).

### 双向全扫 — 逐页 (reviewer 自己的计数; atoms = pdf_atoms 该页全部原子 / fp_match.norm 直接命中本域三文件)
| 页 | 原子 / 直接命中 | PDF→KB 未命中定性 | KB→PDF | 表 / spec | 结论 |
|---|---|---|---|---|---|
| 185 | 30 / 4 | 17 = §6.3.2 DD 别节; a018 节号标题 (= H1); 余为 spec 表头/行 (逐字段见 spec) | EG/asm 1-9 全有出处 | spec STUDYID..USUBJID 逐字段一致; DOMAIN U6 | 一致 |
| 186 | 15 / 0 | 全为 spec TABLE_ROW (格式不同, 逐字段核) | — | 14 变量逐字段一致 (EGSPID 页首行 layout 人工); CT `*` 2 渲染确认; U5 7 | 一致 |
| 187 | 21 / 0 | 同上 | — | 逐字段一致 (EGXFN 页首行人工); U5 9 | 一致 |
| 188 | 18 / 14 | spec 行 + 脚注 ¹ 写法 | 脚注逐字 | EGELTM 页首行人工 (ISO 8601 duration); asm 1-10 逐句命中 | 一致 |
| 189 | 12 / 12 | — | asm 11 仅 U+2011 ‑‑LOINC (既有排版) | — | 一致 |
| 190 | 32 / 15 | 表行 (census OK); a027 原子漏 "10-second" (layout = KB:58) | 全有出处 | Ex1/Ex2/Ex3 census OK | 一致 |
| 191 | 30 / 9 | 表行 (census OK) | 同 | census OK | 一致 |
| 192 | 10 / 6 | 表行 | 同 | Ex4 census OK | 一致 |
| 298 | 25 / 2 | a001-a022 NV Ex2 别节; a023 节号标题 | OE/asm 3-5 有出处 | — | 一致 |
| 299 | 25 / 3 | spec 行 | OE/asm 7-9 有出处 | 逐字段一致; `*` 3 渲染确认; U5 5, U6 1 | 一致 |
| 300 | 22 / 0 | spec 行 | — | 逐字段一致; U5 13 | 一致 |
| 301 | 18 / 4 | spec 行; a011-a013 原子乱码 (渲染 asm 3 = KB: --NSPCES / --ORREF / --STREFN, 原子作 --NOTES/--SUFFIX/--ORREFL); a017/a018 原子差 (layout = KB) | asm 1-3 逐句一致 (asm 3 仅 PDF "-- FAST" 断行) | 脚注逐字; U5 1 | 一致 |
| 302 | 29 / 16 | 表行 (census OK) | Ex1/Ex2 叙述 + 列表全有出处 | census OK | 一致 |
| 303 | 31 / 21 | 表行 | 同 | census OK | 一致 |
| 304 | 29 / 17 | 表行; a020-a023 原子 "installation" — 渲染与文本层均 "instillation" = KB | 同 | census_items 逐格 (下) | 一致 (T-1/T-2) |
| 305 | 32 / 6 | 表行 (census OK); a011+ RP 别节 | 同 | census OK | 一致 |
| 312 | 27 / 5 | a001-a010 RE 别节; a011 节号标题; spec 行 | UR/asm 3-9 有出处 | 逐字段一致; U5 1, U6 1; 首句 "per per" 渲染确认 (U-1) | 一致 |
| 313 | 24 / 0 | spec 行 | — | 逐字段一致; `*` 3 渲染确认; U5 13 | 一致 |
| 314 | 21 / 12 | spec 行; 脚注 ¹ 写法 | 脚注 + asm 1 + Ex1 叙述逐句 | U5 1 | 一致 |
| 315 | UR 26 / 14; PE 26 / 12 | 互为别节 + 表行 + 节号标题 | PE/asm 1-25 全有出处 (CDASH 段拆段, 文字逐字) | UR Ex1/Ex2 census OK | 一致 |
| 316 | 24 / 3 | spec 行 | PE/asm 27-29 有出处 | 逐字段一致, 唯 PELAT notes (T-1); `*` 4 渲染确认; U5 5, U6 1 | 一致 |
| 317 | 17 / 7 | spec 行; 脚注 ¹ | asm 逐句 | U5 4 | 一致 |
| 318 | 21 / 13 | QRS 别节; 表行 | Ex1 叙述 | census OK | 一致 |
| 342 | 25 / 4 | SC 别节; a018 节号标题; spec 行 | SS/asm 3-9 有出处 | 逐字段一致; U6 1 | 一致 |
| 343 | 23 / 3 | spec 行 | 脚注 + asm 1 | `*` 2 渲染确认; U5 6 | 一致 |
| 344 | 21 / 14 | TU 别节 | asm 2-4 + Ex1 叙述 + `**ss.xpt**` | census OK | 一致 |
- 补充 layout 文本逐句 p2k (bscan): 未命中全部为 spec 表多列交错文本 (已由 speccmp 逐字段覆盖) 或别节文本; 无本域叙述缺失.
- k2p: SS 0 未命中; EG/OE/UR/PE 未命中仅表行 (census OK) + EG asm 11 U+2011 排版 + OE relrec 表头 IDVARVAL (T-1).

### spec.md Controlled Terms 逐变量 (bbox 分列 + layout grep + 渲染三法)
| 域 | 变量 | `*` (PDF=KB) | 空=空 | 字面值一致 | U6 | U5 | 非 CT 字段 |
|---|---|---|---|---|---|---|---|
| EG | 44 (bbox 40 + 页首行 STUDYID/EGSPID/EGXFN/EGELTM 人工) | 2: EGCAT EGSCAT | 22 | 3: EGDTC EGRFTDTC EGELTM | 1 | 16 (p186 7 / p187 9) | 全一致, 顺序同 |
| OE | 52 | 3: OETSTDTL OECAT OESCAT | 26 | 3: OEDTC OEELTM OERFTDTC | 1 | 19 (5/13/1) | 全一致 |
| UR | 43 | 3: URTSTDTL URCAT URSCAT | 21 | 3: URDTC URELTM URRFTDTC | 1 | 15 (1/13/1) | 全一致 |
| PE | 30 | 4: PETESTCD PETEST PECAT PESCAT | 15 | 1: PEDTC | 1 | 9 (5/4) | 唯 PELAT notes = T-1 |
| SS | 22 | 2: SSCAT SSSCAT | 12 | 1: SSDTC | 1 | 6 | 全一致 |
- `*` 合计 PDF 14 = KB 14; layout `(Char|Num) +\* ` 计数 p186 2 / p299 3 / p313 3 / p316 4 / p343 2, 其余 9 个 spec 页 0 (非脚注 `*` 0). 与 writer 更正段计数一致.

### census_items 人工逐格 (渲染 p304 160dpi, 不采信 writer)
| 表 | 行 | 结果 |
|---|---|---|
| OE/examples.md:121-124 relrec.xpt | 表头 8 列 | 仅 col6 PDF `IDVARAL` / KB `IDVARVAL` (T-1 沿用) |
| | r1 | XYZ / PR / 空 / PRLNKID / 空 / ONE / 13 一致 |
| | r2 | XYZ / OE / 空 / OELNKID / 空 / MANY / 13 一致 |
| OE/examples.md:140-145 oe.xpt | 表头 21 列 | 一致 |
| | r1 | OD / 1 / EYDCOMGR / Eye Drop Comfort Grade / OECAT PDF OCCULAR COMFORT vs KB OCULAR (T-2) / 1/1/1 / EYE / RIGHT / VISUAL ANALOG SCALE / STUDY SUBJECT / 1 / VISIT 1 / 2011-02-11T09:00 / UPON INSTILLATION / 1 — 余 20 格一致 |
| | r2 | OD / 2 / 10/10/10 / RIGHT / 2011-02-11T09:01 / 1 MINUTE POST-INSTILLATION / 2 — 仅 OECAT T-2 |
| | r3 | OS / 1 (U-1 照录) / 1/1/1 / LEFT / 2011-05-01T09:00 / UPON INSTILLATION / 1 — 仅 OECAT T-2 |
| | r4 | OS / 2 / 10/10/10 / LEFT / 2011-05-01T09:01 / 1 MINUTE POST-INSTILLATION / 2 — 仅 OECAT T-2 |
- T-2 依据复核: p305 suppoe IDVAR=OECAT 的 IDVARVAL = "OCULAR COMFORT" (渲染). 本批 KB 表无 UNPARSEABLE / pdf_unparsed 触碰.

### gaps / intros / footnote 逐项
| 项 | 位置 | 逐字 (仅空白归一对 layout) | 签字 |
|---|---|---|---|
| intro §6.3 (p180) | DA/assumptions.md:3-5, H1 后、`## DA – Description/Overview` 前 | 逐字; 渲染确认 PDF 冒号后直接 6.3.1, **无域列表** | ✔ |
| EG S | EG/assumptions.md:7-9 (Description 与 Assumptions 之间) | 逐字 (— em dash 同 PDF) | ✔ |
| EG F | EG/spec.md:402, EGRFTDTC `---` 后、Cross References (:404) 前 | 逐字 | ✔ |
| OE D/S/A | OE/assumptions.md:3/7/11 | 逐字 | ✔ |
| OE F | OE/spec.md:474 (Cross References :476 前) | 逐字 | ✔ |
| UR D/S/A | UR/assumptions.md:3/7/11 | 逐字, 含 PDF "per per" (U-1) | ✔ |
| UR F | UR/spec.md:393 (:395 前) | 逐字 | ✔ |
| PE D/S | PE/assumptions.md:23/27, `### PE - Alignment…` 段后、`## PE – Assumptions` 前 = PDF p315-316 顺序 | 逐字 | ✔ |
| PE F | PE/spec.md:276 (:278 前) | 逐字 | ✔ |
| SS D/S/A | SS/assumptions.md:3/7/11 | 逐字 | ✔ |
| SS F | SS/spec.md:204 (:206 前) | 逐字 | ✔ |
- 每个 spec.md 脚注仅 1 份 (grep "In this column" = 1), 无旧副本残留. footnote_moves 空.

### 结构 / 删除 / 词级 / D6 逐条签字
| # | 改动 | 依据 | 签字 |
|---|---|---|---|
| S-1 | DA `## §6.3 Models for Findings Domains` | p180 标题; § 前缀同 AE §6.2 先例 | ✔ |
| S-2 | EG `## EG – Specification` | p185 | ✔ |
| S-3 | OE/UR/SS 各 3 个 `## XX – …` 标题 | p298/299/301, p312/314, p342/343 (en dash 同 PDF) | ✔ |
| S-4 | PE `## PE – Description/Overview` / `## PE – Specification` | p315/p316 | ✔ |
| S-5 | SS/examples.md:7 `**ss.xpt**` | p344 "ss.xpt" 表前标签 (R3); 同目录 UR 用无粗体 `ur.xpt`, 格式差异不影响内容 | ✔ |
| D-1 | 14 处 CT 空 → `*` | 渲染 5 页逐格 | ✔ |
| W-1 / D-2 | PE/spec.md:174 laterallity → laterality (PE T-1) | p316 文本层 + 200dpi 渲染确认 PDF "laterallity."; 同行 Label "Laterality", OELAT/URLAT 同句 (p300/p313) 为 "laterality" → PDF 自身可定, KB 写正确值合规 | ✔ |
| U-1 | UR spec 首句 "per location per per visit" 照录 | p312 渲染确认; 正确值 (删 per / 补 "time point") PDF 自身无法唯一确定 (OE 同位为 "per time point per visit") → 照录 + T4 合规 | ✔ |
- G-TB6: diff 新增 44 非空行 (+73 含空行), 逐行对 PDF 页 layout 文本 43 命中, 唯一不命中 = PE T-1 (预期). 结构行: 11 个 `##` 标题、5 个 `> ¹` 引用块前缀、14 个 CT 字段前缀、`**…**` 标签粗体. 无出处 0.
- D6: 无新增 D6, 也无应加未加; spec.md `> Class|Structure` 行与 Cross References 为 U8 导航.

### 问题表 (全部 LOW, 不阻断)
| ref | 检查项 | 问题 | 建议 |
|---|---|---|---|
| L-1 UR/spec.md:3 | U-1 一致性 | 既有导航行 `> Class: Findings \| Structure: … per location per per visit per subject` 亦含 "per per" | 登记到 U-1 T4 条目: 用户若裁定改正, 两处 (assumptions.md:9 + spec.md:3) 同改 |
| L-2 fp_match 全局 | 并行批回归 | 7 条非预期回归 (ig34_p0199_a020, p0200_a006/a007, p0206_a001/a003 → CP; p0240_a004 → IS; p0255_a021 → MS) 不属本批 | 主控转给对应批 reviewer 定性 |
| L-3 t2_S-FND.md 页范围段 | 计数 | writer 本批页 PDF_ONLY 记 7, census 为 8 项 (p342 sc.xpt ×2) + 1 unparsed | 仅记录, 结论不变 |
| L-4 SS/examples.md:3 | 标题层级 | `##### Example 1` 与同类 `## Example N` 不一致 | 按主控 S-FND 裁定不改 (规则 6), 记录 |
| L-5 t2_S-FND.md 逐页日志 | 证据准确性 | 初版逐页计数 (C-code 格数, EGSPID 页) 有误, 已在同 attempt 更正段修正; reviewer 独立计数与更正后一致 | 无需动作 |

### R2 recheck
- 本批 json 无 `t2_recheck[]`; 全扫未发现改写丢短语项. 新增 REAL_GAP 0.

### 总结
- G-TB4: census 20 表 = OK 18 + DIFF 2 (5 格, 全为已登记 OE T-1/T-2); census_items 2 表渲染逐格一致 (差异仅已登记 T-n).
- spec: 5 域 191 变量非 CT 字段逐字段一致 (唯 PE T-1 已改); CT `*` 14/14; U5 65 / U6 5 归 S-CT 未动.
- G-TB6: 新增 44 行全有出处或为签字结构行; 无出处 0. fp_match 本批页回归 0. check_links live docs 42.
