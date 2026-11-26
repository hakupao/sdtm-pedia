# T2 B-CE reviewer

## attempt 1 (oh-my-claudecode:code-reviewer / opus; base = HEAD d84a225, 未提交工作树)

**verdict: CONDITIONAL** (writer 8 处改动全部核实正确; 全扫发现 2 处表格逐格差异 + 1 处 writer 依据错误需登记/主控定, 见修正清单)

### 命令 (可复跑; S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CE_reviewer)
```
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  -> KB tables 12; OK 8 / UNPARSEABLE 4; cells compared 322; diffs 0; exit 1 (RED 仅因全局 PDF_ONLY 331)
  -> 本批页 148-155 内 PDF_ONLY 仅 p148 relrec (sec 6.2.2 BE, 非本域)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  -> RESULT: RED; 51 条回归全在他批页 (p118/174/215-263/289/311/363-396); p148-155 / CE 文件 0 条
fp_match.norm(verbatim) in norm(CE/assumptions.md): ig34_p0148_a015 True; ig34_p0148_a017 (spec 首句) True
  (fp_after verdict 显示 PARTIAL 但 hit_target=CE/assumptions.md; 直接 norm 子串判定命中)
grep -rn CEBODYSYS knowledge_base -> 0 行 (rc=1); CE/spec.md:140 `### CEBODSYS`; pdftotext p149 -> CEBODSYS
pdftoppm -r 110 p148-155 + p151 局部 250dpi; pdftotext -layout p150-153; pdftotext -bbox p155
$S/scan.py (KB 句->PDF) / $S/rev.py (PDF 句->KB) 规范化子串双向扫描
python3 tools/check_links.py 2>&1 | grep "live docs"  -> live docs: 42
```

### writer 8 处改动核实
| # | KB 行 | 核 | 证据 |
|---|---|---|---|
| 1 | assumptions.md:3-5 | 一致 (逐字) | p148 "CE – Description/Overview … would not be classified as adverse events." |
| 2 | assumptions.md:7-9 | 一致 (逐字; 格式同 SM/CM 先例) | p148 "ce.xpt, Clinical Events — Events. One record per event per subject, Tabulation." |
| 3 | assumptions.md:11 | 一致 (PDF 原标题) | p150 "CE – Assumptions" |
| 4 | assumptions.md:15 | 一致 | p150 "--SDTH, --SHOSP, --SDISAB, --SLIFE" (layout: "--" 行末折行接 "SLIFE") |
| 5 | assumptions.md:16 | 一致; 旧改写句删除合规 (该行仅承载 1c) | p150 "would be reported in AE; death would also be a reason for study discontinuation" |
| 6 | examples.md:60 | 一致 | p152 ce.xpt Row 1 CEENDTC "2005-10-12" |
| 7 | examples.md:46 | 一致 | p152 "Other, Specify:" | "_____________" 分属两格 |
| 8 | examples.md:75-76 | 一致 | p153 layout "--/---/--" ×2 |

- T-1 依据成立: p152 Row 5 "Topic Variables,for" — 逗号后缺空格为 PDF 自身排版错, 正确写法由英文常规即可定, KB "Variables, for" 正确.
- O4: 核实, PDF 与 KB 均为 CEBODSYS, KB 无 CEBODYSYS; 无需改 KB, 可关闭.
- 主控裁定 `**CRF: CE Example N — …**` 描述名按 B-AE L-2 保留, 不计问题.

### 问题表
| ref | 检查项 | 问题 | 证据 (PDF 页 + ≤25 词) |
|---|---|---|---|
| C-1 examples.md:13-16 (Ex1 CRF, 未触碰 unparseable) | G-TB4/全扫表格原子 | 第 3 列 "Start Date of First Episode" 4 格 KB 为 `___ / ___ / ___`, PDF 为空; 第 2 列 KB `( ) No  ( ) Yes`, PDF 无任何选项符号, 仅 "No" / "Yes". KB 自写占位. writer 报告称此表 "与 p151 一致" 不成立 | p151 250dpi 局部渲染: Rash 行 "No Yes" + 空格; 4 行同 |
| C-2 examples.md:43-46 (Ex2 CRF, 已触碰) | G-TB4 | 8 个日期格 KB `___ / ___ / ___ (dd/mmm/yyyy)`, PDF 为 `_ _ / _ _ _ / _ _ _ _` (2/3/4 位掩码, 无空格分组). writer 在 #8 对 Ex3 采用 PDF 字面, 同批同类 Ex2 未统一 | p152 layout: "Nausea o Yes _ _ / _ _ _ / _ _ _ _ _ _ / _ _ _ / _ _ _ _" |
| C-3 examples.md:101-102,123-125,148-150 USUBJID (8 格) | PDF_TYPO 依据 | writer 称 PDF "ABC -US-701-002" 的间隙 1.95pt 为字距. 实测同行 FRACTURE→TREATMENTS 词间隙 1.96pt (423.05−421.09), 与 ABC→-US 1.95pt (187.70−185.75) 相同 → PDF 确有空格, 非字距. KB 去空格未登记 | p155 bbox pr Row 3; 渲染 p153-155 均显示 "ABC -US-701-002" |

### 修正清单 (CONDITIONAL, writer attempt 2)
1. C-1: examples.md:13-16 第 3 列 4 格清空; 第 2 列 `( ) No  ( ) Yes` → `No  Yes` (PDF 无符号). 改正 checkpoint 中 ":11 与 p151 一致" 的表述.
2. C-2: examples.md:43-46 8 个日期格 → `__/___/____ (dd/mmm/yyyy)` (PDF 字面, 与 #8 同口径).
3. C-3: 登记 T-2 (USUBJID 空格, 全部 8 处一致带空格, 正确值不能由 PDF 自身确定) → 按 B-CP 规则应照录 + T4; 但 USUBJID 含空格不合理, 写入 "需主控定" 二选一: (a) 照录 "ABC -US-701-002" + T4; (b) 保留 KB "ABC-US-701-002" + T-2 登记. 主控定后执行. 注: census 3.5pt 空格阈值会把此类真实空格并词, census OK 不能作为该格依据.

### 人工逐格表 (渲染图)
**assumptions.md:20 情形表 (p150, 未触碰)**: 表头 Situation / Value of CEPRESP / Value of CEOCCUR / Value of CESTAT 一致; Spontaneously… 三格空 一致; Prespecified event occurred Y/Y/空 一致; did not occur Y/N/空 一致; has no response Y/空/NOT DONE 一致. → 0 差.

**examples.md:11 Ex1 CRF (p151, 未触碰)**: 表头 Clinical Sign / Did it occur? / Start Date of First Episode 一致; PDF 标题行 "Record start dates…" → KB :9 段落 (逐字, 可接受); Rash/Wheezing/Edema/Conjunctivitis 第 1 列 一致; 第 2 列 差异 (C-1, 多 `( )`); 第 3 列 差异 (C-1, 多占位).

**examples.md:41 Ex2 CRF (p152, 已触碰)**:
| 行 | col1 | col2 | Date Started | Date Ended | Severity |
|---|---|---|---|---|---|
| 表头 | Event (PDF 跨 2 列) 一致 | 空 一致 | 一致 | 一致 | 一致 |
| Nausea | 一致 | ○Yes ○No → ( ) 一致 (符号映射) | 掩码差 C-2 | 掩码差 C-2 | Mild/Moderate/Severe 一致 |
| Vomit | 一致 | 一致 | C-2 | C-2 | 一致 |
| Diarrhea | 一致 | 一致 | C-2 | C-2 | 一致 |
| Other, Specify: | 一致 (#7) | 横线 一致 (#7) | C-2 | C-2 | 一致 |

**examples.md:72 Ex3 CRF (p153, 已触碰)**: PDF 无列表头, 仅标题行 "Bone Fracture Assessment" (→ KB :70 标签); 10 行:
Which fracture? 一致 (○→( ); "number_____"→"number ___" 横线长度); Date of collection `--/---/--` 一致; Date of fracture 一致; How did fracture occur? 4 选项 一致; location `_____`→`___` 一致 (横线长度); laterality 3 选项 一致; therapeutic measures required? Yes/No/Unknown 一致; select all (□→[ ]) Casting/immobilization / Traction / Surgery 一致; complications? 一致; select all 3 项 (含 "specify location ______") 一致. → 0 实质差.

**其余 8 张 Row 表**: census_after OK, 另对渲染 p151/152/153-155 逐行抽核: Ex1 ce, Ex2 ce (含 #6), mh (2 行), suppmh, ce (3 行), suppce, pr (3 行), relrec 一致 (USUBJID 空格见 C-3).

### 双向全扫
- KB→PDF (scan.py, 非表格行逐句): 仅 MISS = 3 个 `**CRF: CE Example N — …**` 标签 (主控裁定保留) + assumptions.md:15 (pdftotext 非 layout 把 "--\nSLIFE" 输出成 "-SLIFE" 的抽取伪差, layout/渲染确认 KB 正确, 非问题).
- PDF→KB (rev.py, §6.2.3 Description/Spec 首句 + p150 Assumptions 起至 6.2.4 前): 所有叙述句命中; 未命中仅为表格单元碎片 (已人工逐格)、页脚、合并标题.
- 表格原子: 见上 12 张表.

### R2 recheck
本批 t2_recheck = 0. R3 新增 #4/#5 已核 (见上).

### G-TB6 结构行签字
- assumptions.md:3 `## CE – Description/Overview` (PDF 标题) ✓; :7 `## CE – Specification` ✓; :11 `## CE – Assumptions` ✓.
- examples.md:42 / :73 表分隔线 ✓ (未变).
- examples.md:72 表头 `| Question | Response Options |`: KB 自写结构头 (PDF 无列头), Markdown 表必需, 非解释性内容, 签字保留 (非阻断; writer 未列出, 记录于此).

### 非阻断 / 交主控 (LOW)
- L-1 选项符号映射 ○→`( )`, □→`[ ]` (CE Ex2/Ex3); 同项目 FA 保留 "○" 字面, KB 全局不一致 — 交 O 级统一口径, 本批不改.
- L-2 写入横线长度 (Ex3 `_____`/`______` → `___`) 未逐字; 无信息损失, 可选.
- L-3 PDF 内部不一致: suppmh/suppce USUBJID `001-001` vs 父表 `ABC -US-701-002`; KB 照录 PDF, 列 T4 候选, 不改.
- L-4 fp_match 对 a015/a017 给 PARTIAL 而 norm 子串命中, 疑脚本判档口径, 不影响本批.

### 授权范围 / 副作用
- `git diff HEAD -- knowledge_base/domains/CE/`: 仅 assumptions.md + examples.md (白名单); spec.md 未动; assumptions 改动限 Description/Spec 首句/PDF 原标题 + 1b/1c 逐词级 (追加授权覆盖). 无标题/锚点变动, 已有正确表行未被改坏.
- check_links live docs = 42.

## attempt 2 (delta 复审; 主控裁 C-3 = (a) 照录 + T4 T-2, suppmh/suppce `001-001` 照录 + T4 T-3)

**verdict: PASS**

### 命令
```
git diff HEAD -- knowledge_base/domains/CE    # 全量看; assumptions.md md5 3f9e0f67… 与 attempt 1 同, 未动
md5 -q CE/examples.md -> 5dbcacf128e69598450aeaf44664ebbd (与 writer attempt 2 报告一致)
grep -c "ABC -US-701-002" CE/examples.md -> 8 行; grep -c "ABC-US-701-002" -> 0
grep -c "__/___/____ (dd/mmm/yyyy)" CE/examples.md -> 4 行 (每行 2 格 = 8 格)
table_census.py --manifest $S/manifest.json --out $S/census_after2.json -> OK 8 / UNPARSEABLE 4, cells 322, diffs 0
fp_match.py ... --regress-out $S/fp_regress2.jsonl -> 60 条; 与 attempt 1 相比新增 9 条: p153-155 8 条 (见下) + p0179_a0018 (他批页, 不计)
python3 tools/check_links.py 2>&1 | grep "live docs" -> 42
```

### delta 逐格核 (渲染 p151 250dpi 局部 / p152 / p153-155 110dpi)
| ref | KB 行 | 核 |
|---|---|---|
| C-1 Ex1 CRF | examples.md:13-16 | 4 行: 第 1 列 Rash/Wheezing/Edema/Conjunctivitis 一致; 第 2 列 `No  Yes` 一致 (PDF 无符号, 上下两行 No/Yes); 第 3 列空 一致. 0 差 |
| C-2 Ex2 CRF | examples.md:43-46 | 8 个日期格 `__/___/____ (dd/mmm/yyyy)` = PDF `_ _ / _ _ _ / _ _ _ _` + "(dd/mmm/yyyy)" 一致; 其余格未变 (attempt 1 已核). 0 差 |
| C-3 USUBJID | examples.md:101-102 (mh 2), :123-125 (ce 3), :148-150 (pr 3) | 8 格 = PDF "ABC -US-701-002" 照录 一致; 同行其余格未变 |
| T-3 | examples.md:110-111, :133-136 | suppmh/suppce `001-001` 照录 PDF, 未改 ✓ |

- 范围: diff 仅 CE/assumptions.md (同 attempt 1) + CE/examples.md; 无其他行改动, 无标题/锚点变动.

### fp_match 新增回归 (预期, 非 writer 缺陷)
ig34_p0153_a0034, p0154_a0002/a0013/a0014/a0015/a0029/a0030, p0155_a0002: 均 TABLE_ROW, 原子 verbatim 为 `ABC-US-701-002` (抽取时并词), KB 按主控 C-3(a) 照录 PDF 空格后不再 EXACT 命中. 属裁定直接后果; 原子账本需随 T-2 T4 结论更正 (若用户最终选去空格, 回归自然消失).

### 非阻断 (LOW)
- L-5 writer attempt 2 的 T-2 登记仍写 "间隙 < 3.5pt 空格阈值, 疑为字距" 作为候选值依据; 实测与同行词间隙相同 (1.95 vs 1.96pt), 该依据不成立. 仅为 checkpoint 措辞, 建议 T4 提交用户时改为 "依据: USUBJID 惯例不含空格; PDF 8 处一致带空格".
- L-1..L-4 同 attempt 1, 不变.

### 结论
attempt 1 的 C-1/C-2/C-3 全部按清单/裁定落实; 12 张表 G-TB4 全部 OK 或人工逐格 0 差; G-TB6 新增行均有 PDF 出处 (结构头 `| Question | Response Options |` 已签字). PASS.
