# T2 B-CO writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `0192ae8d904b28a945c50e04241f25c8cf709cf0` (CO 文件改前工作树 clean)
- md5: CO/examples.md `40ec7fe09db523bd5ad1a20228b5c1f5` → `713f8e2b6d342d355db904a3389eb3be` (32 行不变); CO/assumptions.md `8025cc723e281b4fbc1f61c253d61cc3` 未动; CO/spec.md `0c2126612d53ad3ca291439246d0dad7` 未动
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CO_writer/` (examples/assumptions.before.md, p60-62 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 0 / t2_recheck 0; census DIFF 1 表 (2 CELL, KB 行 28); pdf_only 0; unparseable 0; out_of_scope 0.
- 页范围核 (O20): p60 "5 Models for Special-purpose Domains" 章引言 2 句 → "5.1 Comments (CO)" Description/Overview + spec 首句 + spec 表 + 脚注 → p61 Assumptions 1-6 + Examples Ex1 Row 1-5 叙述 → p62 Row 6-8 叙述 + co.xpt 表; p62 后半 "5.2 Demographics (DM)" 起属 B-DM, 未碰. batch lo/hi = 60-62 **完整覆盖**.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | CO/examples.md:28 | census:examples.md:28:4:COVAL1 | REPLACED | Row 4 COVAL1 空 → `Remaining text` (渲染图 COVAL1 列) | 62 |
| 2 | CO/examples.md:28 | census:examples.md:28:4:COVAL2 | REPLACED | Row 4 COVAL2 `Remaining text` → 空 (渲染图 COVAL2 列空) | 62 |

- 覆盖率自查: atoms 0; census 2 格 = #1-2 (全部处理). 非 PDF_TYPO: Row 4 只有 2 段文本, 放 COVAL1 与 Assumption 4 ("next 200 in COVAL1") 一致, 照 PDF.

### census 表处理
| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:23 Ex1 co.xpt (2 CELL) | #1-2 | OK (cells 120, diffs 0) |

### 双向全扫 (含表格原子)
- PDF→KB: p60 章引言/Description/spec 首句 + p61-62 Assumptions 1-6、Row 1-8 叙述: 去连字符折行 + 空白规范化后逐句子串比对 KB (assumptions.md + examples.md) → 仅 1 句缺 (见"需主控定" M-1); 其余为标题行 (`CO – Examples`/`Example 1`, KB 已有对应标题). co.xpt 8 行 × 15 列对 p62 渲染图逐格人工核: 表头/列序/列数/Row 列一致, 改后 0 差.
- KB→PDF: examples.md 全 32 行均有 PDF 对应 (标题/`**co.xpt**` 为导航); assumptions.md 全 34 行均有 PDF 对应 (:17 为 p60 spec 表脚注, 已在 PDF). 无 KB 自写解释性内容 (D6 无), 无伪节号.
- fp_match 改后 p60-62: EXACT 15 / EQUIVALENT 25 / INTENTIONAL_EXCLUDE 19 / PARTIAL 1 (ig34_p0061_a003, T1 triage 已判 PRESENT, matcher 列表格式假阳); regress 中 p006[0-2]/CO 行 = 0 (全量 51 行 regress 为他批工作树改动, 如 p0363 §6.4.2).

### 新增 atom 清单 (R3)
- 无 (M-1 待主控定).

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:28 COVAL2 旧值 | 同行 COVAL1 | VALUE_DIFF 旧值替换 (#1-2) | — |

### PDF_TYPO 清单
- 无.

### 需主控定
- M-1: p60 §5 章引言第 2 句 ("Special-purpose domains provide specific, standardized structures to represent additional important information that does not fit any of the general observation classes.") 在 CO/assumptions.md:5 缺 (KB 只有第 1 句; R2 缺句). fp 基线 ig34_p0060_a003 以 model/03 的改写判 EQUIVALENT. 该段属 §5 章级引言 (非 5.1 CO 节开头), 超出 "本域节开头引言 NOTE" 授权的字面范围, 故未改. 建议: 授权后在 :5 句末接续补入原句 (同段, 逐字).

### 范围外发现
- 无 (spec.md 不在白名单, 未扫).

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CO_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-CO.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # status OK 1, diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -cE 'p006[0-2]|CO/' $S/fp_regress.jsonl   # 0
for p in 60 61 62; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/CO/examples.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

## attempt 2 (M-1 主控授权, 2026-11-26)
- 变更: `knowledge_base/domains/CO/assumptions.md:5` 句末接续补入 p60 §5 章引言第 2 句 (同段, 逐字; PDF 中两句同段). 其余行未动 (34 行不变).
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 3 | CO/assumptions.md:5 | M-1 (ig34_p0060_a003, R2 缺句) | INSERTED | 首句后补 "Special-purpose domains provide specific, standardized structures …" | 60 |
- 逐字核: `pdftotext -f 60 -l 60 -layout "source/cdisc/SDTMIG v3.4 (no header footer).pdf" - | sed -n 2,3p | sed 's/^ *//;s/ *$//' | tr '\n' ' ' | sed 's/ $//'` 与 `sed -n 5p knowledge_base/domains/CO/assumptions.md` → IDENTICAL (折行处为整词边界).
- md5: CO/assumptions.md `8025cc723e281b4fbc1f61c253d61cc3` → `dd7bc3c0da71c01e08f67c173ee4c5e0`; examples.md 仍 `713f8e2b6d342d355db904a3389eb3be`.
- 删除: 无. `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42.
- git diff --stat: assumptions.md 2 +-, examples.md 2 +- (2 files, 2 insertions, 2 deletions).
- M-1 状态: **已处理**.
