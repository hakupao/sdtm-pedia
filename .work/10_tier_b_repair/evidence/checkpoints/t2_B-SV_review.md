# T2 B-SV reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base = HEAD (`beaefa9`), `git diff HEAD -- knowledge_base/domains/SV/` = assumptions.md (+6/-2) + examples.md (+1/-1); spec.md 未动. md5 与 writer 报告一致 (`5d7f4b1b…` / `7c5768b9…` / `2208d850…`).
- 页范围: SV 节 = p86 中部 "5.5 Subject Visits (SV)" → p91 (p86 上部 ce.xpt 属 SM, 未触碰; p92 起 §6). 渲染 p86-91 @110dpi 于 scratch `t2_B-SV_reviewer/`.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SV_reviewer/`

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SV_reviewer
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  -> KB tables: 3; status: {'OK': 3}; cells compared: 397; diffs: 0  (exit 1 仅因全局 PDF_ONLY 336, 无落在 p86-91 的本批表)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  -> RESULT: RED (60 条回归, 全在他批页 p257-263 等; p86-91 回归 0). fp 原子集不含 p86-91 页 (抽样集), 本批由人工/脚本全扫兜底.
python3 tools/check_links.py 2>&1 | grep "live docs"  -> broken relative links: 18668 (live docs: 42)
```

### 变更逐条核 (G-TB6 反向溯源)
| diff 行 | 检查 | 结论 | 证据 (PDF 页 + ≤25 词) |
|---|---|---|---|
| assumptions.md:5 | 新增 a003 | 一致, 独立段 | p86 "A special purpose domain that contains information for each subject's actual and planned visits." |
| assumptions.md:7 前 4 句 | 新增 a004-a007 | 逐字一致, 与原有 "The method for deriving…" 同段 (渲染图第 2 段) | p86 "Unless the beginning and end of each visit is collected, populating the SV dataset will involve derivations." |
| assumptions.md:9 | a011 改义恢复 + 另起段 | 一致; 渲染图第 3 段起于 "The SV dataset provides reviewers…" | p86 "supports the identification of planned but not expected visits due to a subject not completing the study." |
| assumptions.md:51 | 15b was collected→was recorded | 一致 (同条前句 "data was collected" 未动, 正确) | p88 "not necessary to submit the date on which information about the visit was recorded." |
| examples.md:53 | ds Row 6 DSSTDY 28→26 | 渲染 p90 Row 6 DSSTDY = 26 | p90 ds Row 6 "…TREATMENT 2020-03-16 2020-03-16 26" |
- 新增非空行 4 (assumptions :5/:7/:9/:51) + 1 (examples :53), 无出处 0. 新增空行 2 (段落分隔) = 结构行, 签字: 对应 p86 3 段切分, OK. 无新增标题/锚点/表头.
- 删除短语 D-1 "planned but not completed visits": KB 自写改义, PDF 无此句, 删除正确 (仅承载 a011).

### 双向全扫 (p86 中-p91, 含表格原子)
- 脚本法 (独立实现: PDF 文本层去页脚、去表格行、句切分, 与 KB assumptions+examples 互查): 残差全部可解释 — (a) 标题与首句粘连切分伪差 (Description 首句 / Ex1 首句, 人工确认在 KB), (b) spec 表单元格与脚注 1 (属 spec.md, 白名单外, 见 F-1), (c) tv/ds/sv 表格碎片 (另行逐格核), (d) Row 5 句号 = T-1.
- KB→PDF: assumptions.md 全文 (Description 3 段、spec 首句、Assumptions 1-16 含 4a-d / 15a-f) 与 examples.md 全文逐句均在 PDF p86-91; 无 KB 自写内容, 无 D6 项.
- 渲染图人工逐格 (独立于 census):

| 表 | PDF 页 | KB 行 | 结果 |
|---|---|---|---|
| tv.xpt 8 行 x 8 列 | p89 | examples.md:21-28 | 一致 (Row 1/8 VISITDY 空; Row 3-7 TVENRL 空; Row 8 "FOLLOW-UP" 折行合并) |
| ds.xpt Rows 1-4 x 13 列 | p89 | :48-51 | 一致 (Row 1-2 DSSTDY 空; Row 3 -6; Row 4 72; Row 1/3 DSSCAT 空) |
| ds.xpt Rows 5-6 | p90 | :52-53 | 一致 (Row 5 -6; Row 6 26 — 改后) |
| sv.xpt Rows 1-8 x 17 列 | p90 | :81-88 | 一致 (Row 4 SVREASOC "SUBJECT LACKED TRANSPORTATION", SVCNTMOD/日期/DY 空; Row 6 SVSTDY/ENDY 30) |
| sv.xpt Rows 9-15 | p91 | :89-95 | 一致 (Row 13 "CLINIC CLOSED DUE TO BAD WEATHER"; Row 14 VISITNUM 4.1, VISIT/PRESP/OCCUR 空, REMOTE AUDIO VIDEO, SVEPCHGI Y, EVALUATION OF AE; Row 15 TELEPHONE CALL, Y, 26/26) |

### PDF_TYPO 核
- T-1 (p89 ds 说明 "Row 5: Shows informed consent for subject 101" 无句点; 渲染图确认): 同组 Row 1-6 其余说明均以句点结尾 → PDF 自身可定, KB 保留句点. 依据成立.

### R2 recheck
- t2_recheck 0 条; atoms 0 条. 无.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无阻断问题 | — |
| 信息 I-1 (LOW, 不需改) | 数据一致性 | ds Row 6 DSSTDY 与 sv Row 15 SVSTDY 均 26, 按 Day1=2020-02-19 推算 2020-03-16 应为 27; 但 PDF 表与 Row 15 叙述 ("study day 26") 自洽, KB 照录 PDF 正确, 不登记 | p90/p91 |

### 无副作用
- SV 改动仅 assumptions.md (授权: Description/Overview + 列表逐词偏差) 与 examples.md (batch kb_files); spec.md 未动; 标题/锚点未变; 表既有正确行未改. 工作树中他批文件不计.
- writer 范围外发现 F-1 (spec 脚注 → O26) / F-2 (直撇号 → O40) 认同, 不属本批.

live docs: 42
