# T2 B-MH reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS** (附 1 条非阻断意见 F-1 给主控: T-2 依据需更正, 建议列 T4 让用户确认)

- 审查对象: writer attempt 1 + 续 终态; md5 实测 assumptions `c4469c2749e81dd20d713d7bd04d6e8a` / examples `d7642d4811cca46e92979906328848a2` = writer 续 声明值.
- diff 基线 259cd49; `git diff --stat 259cd49 955e9d5 -- knowledge_base/domains/MH` 为空 (B-MS commit 未动 MH). 整 KB diff 中 MH 以外文件 (ch02/ch08/FA/MB/MS/TA/model02) 属 955e9d5 或并行批 (B-FA/B-ch08/B-TA/B-SUPPQUAL), 非本批.
- 独立方法: `pdftoppm -r 130` 渲染 p171/p174-p178 (源 `source/cdisc/SDTMIG v3.4 (no header footer).pdf`) 目视逐格; 叙述另用 `pdftotext` (非 layout) 自写归一脚本双向扫. scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-MH_reviewer/`.

### 命令 / exit code
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-MH_reviewer
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1 (RESULT RED = manifest 外全局 PDF_ONLY; p171-178 内 pdf_only 0)
  -> MH: assumptions:36 UNPARSEABLE (人工, 见下); examples:13/39/60/83 OK; examples:104 DIFF 1 = r1 MHDTC kb 2019-11-02 / pdf 2019-011-02 (T-2)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # exit 1, 全局 regress 48
  -> regress 与 targets 含 domains/MH/ 的 join: 仅 ig34_p0174_a0012 (T-1, 预期); 其余 47 条属他批页
  -> MH 区 (p171_a0009..p178_a0012) 未命中: p0171_a0015..p0172_a0012 (spec 表行, 属 spec.md, 范围外 O-MH-1), p0173_a0007 (T-3), p0174_a0012 (T-1), p0178_a0005 (T-2)
python3 -I $S/scan.py $S        # 双向逐句扫, 结果见下
python3 tools/check_links.py | grep "live docs"   # 写本文件后复跑: live docs 42 (基线 42)
```

### 1. 新增节 / spec 首句 / 叙述修正 (对 p171-p174 渲染 + 文本)
| ref | KB 行 | 结论 |
|---|---|---|
| `## MH – Description/Overview` | assumptions:5 | p171 标题逐字 (en dash) ✓; 位置同 CM/AE 先例 ✓ |
| `## MH – Specification` + 首句 | :9, :11 | p171 "mh.xpt, Medical History — Events. One record per medical history event per subject, Tabulation." 逐字 ✓; 位于 Description 与 Assumptions 之间 = CM/AE 先例 ✓ |
| 2b | :19 | 补 "The modified term is listed in MHMODIFY." = p172 ✓ |
| 2d D-1 | :21 | 删句 "It is expected that this variable will be populated." — 全部 pdf_pages 仅 p0138 (AE) 含此句, MH p173 2d 无 ✓ 删除正确 |
| 3a.i | :26 | "Medical History" = p173 ✓ (原 KB 重复词) |
| 4a | :31 | ", respectively" = p173 ✓ |
| 6b T-1 | :51 | 见 §4 |

### 2. 人工逐格: assumptions:36 4d 表 (census UNPARSEABLE; 对 p174 渲染)
| 行 | Situation | Value of MHPRESP | Value of MHOCCUR | Value of MHSTAT | 结论 |
|---|---|---|---|---|---|
| 表头 | Situation | Value of MHPRESP | Value of MHOCCUR | Value of MHSTAT | 一致 (PDF 表头两行折行) |
| 1 | Spontaneously reported event occurred | 空 | 空 | 空 | 一致 |
| 2 | Pre-specified event occurred | Y | Y | 空 | 一致 |
| 3 | Pre-specified event did not occur | Y | N | 空 | 一致 |
| 4 | Pre-specified event has no response | Y | 空 | NOT DONE | 一致 |

### 3. 例子表逐格 (改动格 + 整行复核; 对 p175-p178 渲染)
| 表 | 行 | 格 | KB 终态 | 渲染 | 结论 |
|---|---|---|---|---|---|
| Ex1 (p175) | 表头 | 列序 | Row…MHDECOD, MHEVDTYP, MHCAT, MHSCAT, MHBODSYS, MHSTDTC, MHENRTPT, MHENTPT (15 列) | 同 | 一致 |
| Ex1 | r1-r3 | MHEVDTYP / MHSTDTC / MHENTPT | 空 / 空 / 2004-09-18 | 空 / 空 / 2004-09-18 | 一致 (×3 行) |
| Ex1 | r4 | MHEVDTYP / MHSTDTC / MHENRTPT / MHENTPT | SYMPTOM ONSET / 2004-09-17 / 空 / 空 | 同 | 一致 |
| Ex1 | r5 | MHEVDTYP / MHSTDTC | DIAGNOSIS / 2004-09-19 | 同 | 一致 |
| Ex1 | r1-r5 | 其余格 (GRPID CHF r4-5, TERM, DECOD, CAT, SCAT, BODSYS, ENRTPT) | 逐格 | 同 | 一致 |
| Ex2 (p176) | 表头 | 列序 | …MHCAT, MHSCAT, MHPRESP, MHOCCUR, MHBODSYS, MHSTDTC, MHENRF (14 列) | 同 | 一致 |
| Ex2 | r1-r3 | PRESP/OCCUR/BODSYS/ENRF | 空/空/Respiratory system disorders, Central and peripheral nervous system disorders, Musculoskeletal system disorders / DURING/AFTER, DURING/AFTER, BEFORE | 同 | 一致 |
| Ex2 | r4 | 全行 | ISCHEMIC STROKE / Ischaemic Stroke / STROKE HISTORY / 空×4 / 2004-09-17T07:30 / 空 | 同 | 一致 |
| Ex2 | r5-r7 | PRESP/OCCUR | Y/Y | Y/Y | 一致 |
| Ex2 | r8 | PRESP/OCCUR | Y/N | Y/N | 一致 |
| Ex3 (p176-177) | r4 | MHREASND / VISITNUM | 空 / 1 | 空 / 1 | 一致 |
| Ex3 | r8 | MHOCCUR | Y | Y | 一致 |
| Ex3 | r1-r10 | 其余格 (含 r10 NOT DONE / FORGOT TO ASK) | 逐格 | 同 | 一致 |
| Ex4 (p177) | r1 / r4 | MHOCCUR | Y / Y | Y / Y | 一致; r2/r3 N 一致 |
| Ex5 (p178) | r4 | MHENDTC / MHENRTPT / MHENTPT | 2019-10-20 / 空 / 空 | 同 | 一致 |
| Ex5 | r3 | MHENRTPT / MHENTPT | BEFORE / 2019-12-08 | 同 | 一致 |
| Ex5 | r1 | MHDTC | 2019-11-02 | 2019-011-02 | T-2 (见 F-1) |
叙述: Ex1 Rows 1-3 / Rows 4-5 (:7/:9) 与 p175 逐字 ✓ (D-2 "indicates the body system for which the event was collected", "Ongoing"; D-3 删 Ex2 Row 4 串入句, "start dates of"); Ex2 Rows 1-3 (:31) 补 "on using --STRF and --ENRF" = p176 ✓.

### 4. PDF_TYPO
| T | 判定 | 依据 |
|---|---|---|
| T-1 6b MHENDTYP→MHEVDTYP | 同意 keep-correct | 同句前半 MHEVDTYP、6a、p171 spec 行; MHENDTYP 在全部 pdf_pages 仅出现于 p174 此处 |
| T-2 Ex5 r1 MHDTC 2019-011-02 | 同意 KB 现值保留 (主控已裁 M-2), **但依据不成立 → F-1** | "011" 删一位可得 11 或 01, 2019-01-02 同样合法; MHDY −2 无 RFSTDTC 可反推, r2 为另一受试者 → PDF 自身不能唯一确定 |
| T-3 3a.ii 引号/逗号后空格 | 同意 | 纯标点印刷 (弯引号方向 + 多空格), 字词无歧义, KB 规范写法可由同句其他引号确定 |

### 5. :53 KB note (D6)
- 前缀 `> KB note (not in SDTMIG):` 符合 domains/ 口径 ✓; 英文措辞通顺.
- 事实逐项核: PDF p174 印 MHENDTYP ✓; 6a 定义 MHEVDTYP ✓; p171 spec 行 MHEVDTYP ✓ (KB MH/spec.md:95 `### MHEVDTYP`, 无 MHENDTYP); MH 例 (p175/p177)、SM 例 (p85)、FA 例 (p371) 均用 MHEVDTYP ✓. 与 PDF 不矛盾, 按 D6 保留 ✓.

### 6. 双向全扫 (scan.py, 非 layout 文本)
- KB→PDF 未命中全部已处置: 结构行 (H1×2, 6.2.6/Description/Specification/Assumptions 标题, `## Example 1-5`) — PDF 有对应标题或纯导航; 4d 表行 (已人工逐格); :51 (T-1); :53 (D6); :55 (PDF "--\nSMIE" 折行, 对 p174 渲染 14 个限定词 --SER…--SMIE 逐个一致); examples:25-27 (`- ` 列表前缀, 内容 = p175 bullet).
- PDF→KB 未命中全部为脚本切分伪差: 页脚粘连 ("© 2021 …"/"Page N")、表格碎片 (已逐格)、"\n大写" 切句造成的半句 (MHREASND 句、6b/7 句均在 KB :34/:51/:55)、T-3 句. 无真实缺失.
- 标题/锚点: 原 `## 6.2.6 Medical History (MH)` / `## MH – Assumptions` 未变; examples H1 `# MH — Examples` 与 CM/AE/IS/GF/OE 同惯例.

### G-TB6 结构行签字
assumptions:5 `## MH – Description/Overview` ✓ | :9 `## MH – Specification` ✓ | :11 spec 首句 (PDF 逐字) ✓ | :36 4d 表头 ✓ | :37 分隔线 (未改) ✓ | :53 `> KB note (not in SDTMIG):` 前缀 ✓ | examples:13 Ex1 表头 ✓ :14 分隔线 ✓ | :39 Ex2 表头 ✓ :40 分隔线 ✓. 新增/改动行无出处词句: 0 (除 D6 note).

### 删除清单确认
D-1 ✓ (AE p138 串入, 非 MH PDF) | D-2 ✓ (:7 恢复 p175 原文) | D-3 ✓ (:9 删 Ex2 Row 4 句, p175 Ex1 无) | D-4 ✓ (旧值替换, 均对渲染核).

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| F-1 census:examples:104 r1 MHDTC (T-2) | PDF_TYPO 取舍规则 | 主控 M-2 依据 "011 唯一合法读法是 11" 不成立 (01 亦合法); 按规则属不可确定 → 应列 T4 用户裁定. 非阻断: KB 值为改前既有值, 本批未改该格 | p178 Ex5 r1 "2019-011-02" |

### R2 recheck
t2_recheck = 0, atoms = 0 → 无判定项.

### 汇总
G-TB4: 5 表 (4 OK + Ex5 DIFF 1 = T-2) + 4d 表人工逐格一致; G-TB6: 新增/改动行无出处 0 (D6 note 1 处合规); fp MH 回归仅 p0174_a0012 (预期); live docs 42 ≤ 42.

## 续 签字 (writer attempt 1 续 2, T-2 delta)
- delta: examples.md:106 Ex5 r1 MHDTC `2019-11-02` → `2019-011-02`; 对 p178 渲染 r1 MHDTC "2019-011-" / "02" 折行 = 一致. md5 assumptions `c4469c27…` 不变, examples `216c920a870d40a08430b12f2a0d3e77`; MH diff --stat 37+/31- → 38+/32- (仅多此 1 行).
- census (`$S/census2.json`, exit 1 = 全局 PDF_ONLY): MH examples 13/39/60/83/104 全 OK, assumptions:36 UNPARSEABLE (已人工逐格). fp (`$S/fp2.jsonl`, exit 1): targets 含 MH 的回归仅 ig34_p0174_a0012 (T-1); p0178_a0005 现命中 MH/examples.md. check_links live docs 42 ≤ 42.
- T-2 登记 "照录 + T4 用户裁定" 符合 PDF_TYPO 取舍规则; F-1 关闭. **verdict 维持 PASS**.
