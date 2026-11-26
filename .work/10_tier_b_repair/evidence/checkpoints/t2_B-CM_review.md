# T2 B-CM reviewer

## attempt 1 (审 writer attempt 1+2 终态; oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- 范围: CM 节 p98-103 (p98 6.1.2 Description/spec 首句 → p103 Ex5 止于 6.1.3); batch kb_files = CM/examples.md; 授权追加 CM/assumptions.md (3a/5 逐词 + 2c D-2 删句)。
- base = HEAD (`0192ae8`); `git diff HEAD -- knowledge_base/domains/CM/` = assumptions.md 3 行改、examples.md 1 行改; spec.md 未改 (`git diff --quiet` 0)。
- md5: assumptions.md `ee387c8140bdfd9dc63516b136d1ce18`, examples.md `01c3d7d7898ae19665c34b216eaccf58` (与 writer 报告一致)。
- KB 整体 diff 另有 CE/FT/HO/IE/MI/QS 改动 = 他批并行, 不计本批; 本批无白名单外改动。
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CM_reviewer/`

### 命令与结果 (可复跑, 在 repo 根)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CM_reviewer
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # exit 1 (RED 仅来自全局 PDF_ONLY); 本批 5 表 (:17 :36 :55 :71 :96) 全 OK; pdf_only/pdf_unparsed 在 p98-103 内 = 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # exit 1 RED; 51 条 regress, 页码集合 p118/174/215/218/254/257/258/260/262/263/289/311/363/364/370/373/374/396, p98-103 = 0 → 不计本批
python3 -I $S/scan.py    # KB→PDF: 散文 0 MISS; 表格 22 TMISS 全是 Ex5 折行单元格 (PRIOR RA/MEDICATIONS, RHEUMATOID/ARTHRITIS, 2020-02-/02 等), 人工核一致
python3 -I $S/rscan.py   # PDF→KB: 5 条"MISS"均为标题与句子拼接 (cm.xpt + Example N / 6.1.2 标题), 拆开后各句 grep -cF 均命中 1
pdftoppm -f 102 -l 102 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p102
grep -n "decode value in the dictionary, then CMDECOD will be left blank" knowledge_base/domains/CM/spec.md   # :84 (全行显示, 逐字)
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42 (= 基线)
```

### 改动逐条核 (G-TB6 反向溯源)
| diff 行 | 内容 | 出处 / 判定 |
|---|---|---|
| examples.md:39 USUBJID 1→2 | Ex2 Row 2 | p102 渲染图 Row 2 "ABC123 CM 2 1 VPA ANTI-CONVULSANT" → 一致 |
| examples.md:39 CMSEQ 2→1 | 同上 | 同上 (layout 文本亦 `2 1 VPA`) → 一致 |
| assumptions.md:22 3a "whether" | 逐词补 | p100 "used together to indicate whether the intervention in CMTRT was prespecified" → 一致 |
| assumptions.md:29 5 "variables" | 逐词补 | p101 "Although any identifier variables, timing variables, or interventions general" → 一致 |
| assumptions.md:18 2c 删末句 | D-2 | p100 2c 止于 "…external codelist element in the Define-XML document."; 被删句出自 p98 spec CMDECOD Notes, 保留副本 `CM/spec.md:84` 逐字存在 (全行未截断核) → 删除正确, 无信息丢失 |
- 新增结构行: 无 (无新标题/锚点/表头/分隔线)。

### 双向全扫 (含表格原子)
- KB→PDF: assumptions.md 全 29 行 + examples.md 全 103 行, 非表格句逐句在 p98-103 归一化文本 (弯/直引号、破折号) 中命中, 0 无出处; 无 KB 自写解释性内容 (D6 无), 无伪节号; `**cm.xpt**`、`**Row N:**`、`## Example N` 为导航。
- PDF→KB: p98 Description + spec 首句; p100-101 Assumptions 1-5 (含 2a-d/3a-c/4a); p101-103 Ex1-5 全部叙述与 Row 说明, 逐句在 KB 命中, 0 缺 (R2 无丢短语/交叉引用; "Section 4.5.3.2, Text Strings Greater than 200 Characters" 保留)。
- 弯引号/直引号差异 (p100 “ASPIRIN…”、sponsor’s; p102 study’s) 规范化等价, 照既有先例不改, 不计缺陷。
- p98-99 spec 表不在本批 (spec.md 未动, 非 kb_files)。

### 人工逐格 (表格原子)
| 表 | 核法 | 结果 |
|---|---|---|
| Ex1 :17 (10 行×11 列, p101-102) | layout 文本 + p102 渲染 (Row 9-10) | 一致 |
| Ex2 :36 (2×7, p102) | p102 渲染图逐格 | 一致 (含改后 Row 2) |
| Ex3 :55 (3×10, p102) | p102 渲染图逐格 (Row 3 CMOCCUR 空, CMSTAT NOT DONE, CMREASND "Didn't ask due to interruption") | 一致 |
| Ex4 :71 (6×11, p102-103) | p102 渲染 Row 1-3 + p103 layout Row 4-6 | 一致 |
| Ex5 :96 (6×15, p103 折行) | layout 文本折行合并逐格 (CMTRT/CMCAT/CMSCAT/CMINDC/CMDTC/CMENTPT; Row 1/3 CMSCAT 空; Row 5-6 CMPRESP/CMOCCUR 空) | 一致 |

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无 | — |

### R2 recheck
- t2_recheck = 0 条; atoms = 0 条。writer R3 新增 2 条 (#3/#4) 已核。

### 结论
PASS。改动全部有 PDF 出处, 授权范围内; 无副作用; census 5/5 OK; fp 无本批页回归; live docs 42。
