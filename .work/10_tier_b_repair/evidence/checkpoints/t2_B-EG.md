# T2 B-EG writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `0dc4f145adcf3c652640d6a488bf508b98fd104e`
- md5 EG/examples.md: before `eff4aad9078b6ddf987e4390d3d60db1` → after `3a8db61a1f763f1f89638340f9a9771c` (行数 110 不变; 仅表格行改动)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-EG_writer/`
  (examples.before.md, apply.py = Ex1 整表按渲染图重写 + Ex2 插 EGSTRESN 列 + Ex4 两格, 每处断言旧值; prose_scan.py; census_before/after.json; fp_before/after.jsonl;
  渲染图 p189-192 150dpi + za/zb-190 (Ex1 左右半 300dpi) + zc-192 (Ex4 右半 300dpi); before_root/ = 改前 KB 镜像供 before 跑工具)
- 数据来源: 所有改动格对照渲染图 (layout 文本仅辅助). 本批 atoms 2 (REAL_GAP 1 / VALUE_DIFF 1), t2_recheck 0; census DIFF 3 表 (67 diffs) 全处理; pdf_only 0; unparseable 0.
- O6 标注纠正: out_of_scope O6 写 "EG Example 3 整表损坏", 实为 **KB/PDF Example 1** (KB :23-36, p190; triage 理由本身也指 :25-36). KB Example 3 (:62-87, p190-191) census OK, 逐行与 p190-191 一致, 未改.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | EG/examples.md:23-24 | census:23 HEADER | TABLE_REBUILT | 表头 `EGNAM, EGCLSIG, EGDRVFL` → PDF 序 `EGNAM, EGLOBXFL, EGDRVFL, EGCLSIG` (加 EGLOBXFL 列, 全空); 分隔线同步 | 190 |
| 2 | :25-36 | census:23 CELL×60 + ig34_p0190_a011 (Row 9) | TABLE_REBUILT | 12 行全部按渲染图重写 (不是挪列: 旧 KB r5/r6 的 Y 在 EGCLSIG 位, 应在 EGDRVFL). 全行: EGXFN PQW43787B→PQW436789-07.xml (r1-11); EGNAM Test/Lab→"Test Lab" (r1-11, r12 空); VISIT Screening→"Screening 1"; EGDTC 2003-04-36 / 15T11:58 → 2003-04-15T11:58. 单格: r1 EGCLSIG N, r2 EGCLSIG Y; r5/r6 EGDRVFL Y, EGCLSIG 空; r6 EGSTRESC/N 448→446; r7/r8 EGTESTCD SPRATRY→SPRTARRY; r9 STSTWUN→STSTWUW, EGTEST 去掉 KB 多出的 "Changes: nonspecific or Enlargement"; r10 CHPTEN2→CHYPTENL; r11 EGCAT FINDING→空, EGORRES/EGSTRESC "OTHER/INCORRECT …"→"OTHER INCORRECT ELECTRODE PLACEMENT" | 190 |
| 3 | :48-49 | census:48 HEADER | REPLACED | 加 PDF 的 EGSTRESN 列 (EGSTRESC 后, 5 行全空); 分隔线同步 | 190 |
| 4 | :50 | census:48 r1 VISIT | REPLACED | SCREEN 1 → SCREEN I | 190 |
| 5 | :51 | census:48 r2 EGORRES/EGSTRESC | REPLACED | NORMAL → ABNORMAL (两格) | 190 |
| 6 | :105 | census:101 r3 EGDTC | REPLACED | 2014-02-11T14:32:12.3 → …14:32:13.3 | 192 |
| 7 | :108 | census:101 r6 EGDTC | REPLACED | 2014-02-11T15:32:13.3 → …15:32:14.2 | 192 |
| 8 | — | ig34_p0185_a020 | SKIPPED_STRUCT | EG Description/Overview 句 (PDF p185, 位于 EG Specification 前). KB 惯例在 `<DOMAIN>/assumptions.md` H1 后 `## EG – Description/Overview` (CM/CP/IS/MB/DM…); EG/assumptions.md **不在本批 kb_files**, 也不在任何其他批 → 不写 examples.md (位置错), 交主控: 扩白名单或补小批 (同 O13 VS 处理). 目前 KB 仅 terminology/core/general_part4.md:188 (CT 定义) 有同文 | 185 |

- atoms 覆盖率自查: atoms 2 = 清单 atom 行 2 (#2 a011, #8 a020). 改动 7 行 / 跳过 1.
- Ex4 Rows 4/7 (lane notes "ATOM_ERR, KB 与 PDF 一致"): 对 zc-192 渲染图复核, KB r4 (…14:32:13.3, RR Interval, Single Measurement) / r7 (…15:32:14.2) 与 PDF 一致, 未改. census 的 :105/:108 是 Rows 3/6, 与该说明无关, 为真 KB 错, 已修 (#6/#7).

### census 表处理

| census ref (before 行号) | 处理 | 结果 (after) |
|---|---|---|
| :23 Ex1 (61 = HEADER 1 + CELL 60) | #1-2 整表重建 | OK |
| :48 Ex2 (4 = HEADER 1 + CELL 3) | #3-5 | OK |
| :101 Ex4 (2) | #6-7 | OK |
| :62 Ex3 | 未动 | OK (改前改后) |

- 汇总: before `DIFF 3 / OK 1, cells 1118, diffs 67` → after `OK 4, cells 1135, diffs 0`. (RESULT RED 来自 manifest 外 PDF_ONLY 335 张, 改前改后相同, 与本批无关.)
- writer.jsonl 69 行 = 2 atoms + 67 census diffs (HEADER 各 1 行).

```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-EG_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-EG.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json          # before: 加 --kb-root $S/before_root/knowledge_base
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl                                              # before: 同上 --kb-root
python3 -I $S/prose_scan.py            # before: python3 -I $S/prose_scan.py $S/examples.before.md
```

### fp_match (改前 vs 改后, 全量)
- **回归 0** (无原子从命中变未命中). 新命中 6: ig34_p0190_a002 (Ex1 表头), p0190_a020/a021/a022 (Ex2 表头 + r1/r2), p0192_a005/a008 (Ex4 r3/r6). 全量 hit_target 3751 → 3757.
- p189-192 改后仍未命中 = 原子抽取错 (ATOM_ERR), KB 按渲染图正确:
  - Ex1 r1-r12 (p0190_a003-a014): 原子 EGXFN 记作 "P0W436789" (渲染图 PQW), VISIT 漏 wrap 行的 "1", r1 EGTESTCD "EGHRM" (渲染图 EGHRMN), r11 原子漏 EGCAT 空格.
  - Ex2 r3 (p0190_a023): 原子 VISITNUM 4 (渲染图 3).
  - Ex3 (p0190_a030-a032, p0191_a001-a021): 原子 VISIT 断行 / 省略号 "..", 与 KB "..." 写法差; census Ex3 OK.
  - Ex4 r4/r7 (p0192_a006/a009): 原子 EGTEST "Single Beat Measurement" (渲染图 "Single Measurement"); 与 lane notes 一致.
  - p0190_a027 (Ex3 叙述): 原子漏 "10-second"; KB 与 PDF 一致.
- p185-188 未命中原子属 EG spec 表 / 其他批 (见范围外), 本批不动; ig34_p0185_a020 见 #8.
- **预期 fp 回归 (PDF_TYPO 改正引起)**: 无 — 本批没有把任何格改成偏离 PDF 的值.

### 双向叙述扫描 (R3; prose_scan.py, p189-192)
- PDF→KB: 改前改后同为 3 条未命中: ig34_p0189_a001 / a002 (EG assumption 10b / 11, 属 EG/assumptions.md, grep 该文件 2 处命中 → 已在), ig34_p0190_a027 (ATOM_ERR, 见上). examples.md 无叙述缺失.
- KB→PDF: 0 句未命中 (无 KB 自写 / 超出 PDF 句子). 标题 `# EG — Examples` / `## Example N` / `**eg.xpt**` 为结构行.
- 新增 atom 清单: 无 (R3 无缺口).
- 未做 (仅格式, 同 B-DS/B-IS 口径): p189 Rows 5-6 PDF 弯引号 “Y”、p190/191 "subject’s" 弯撇号, KB 直引号未改.

### PDF_TYPO / PDF 自相矛盾 (KB 均照录 PDF, 未改; 登记供 T4 用户裁定)

| T | 位置 | PDF 内矛盾 | KB 处理 | 依据 |
|---|---|---|---|---|
| T-1 | Ex1 叙述 Rows 7-10 (:15) | 叙述 EGCAT = "FINDINGS", 表 EGCAT = FINDING | 两处均照录 PDF | 正确值不能由 PDF 自身唯一确定 (CT 层面未核) |
| T-2 | Ex2 叙述 Rows 1-3 (:42) | 叙述 Visit "SCREEN 2", 表 VISIT = SCREEN II | 照录 | 同上; 可能是同一访视的两种写法 |
| T-3 | Ex2 叙述 Rows 1-3 (:42) | "principal investigation", 表 EGEVAL = PRINCIPAL INVESTIGATOR | 照录 | 疑 PDF 笔误, 但改正会偏离原句, 留用户裁 |

- 以上全部照录 → 对 fp_match 无回归.

### 删除清单
- 无 D2 删除. 仅 VALUE_DIFF / 表头跟 PDF 的旧值替换 (Ex1 :23-36 整表旧值、Ex2 3 格、Ex4 2 格), 见变更清单.

### 触碰过的 unparseable 表
- 无 (本批 unparseable 0; 三张改动表 census 均可机检, after 全 OK). reviewer 仍须按 dispatch notes 用渲染图独立复核 Ex1 重建表.

### 范围外发现
- X-1 (主控定): ig34_p0185_a020 EG Description/Overview 需落 EG/assumptions.md (不在任何批白名单) — 同 O13 型.
- X-2: ig34_p0185_a022 EG spec 数据集标题句 ("eg.xpt, ECG Test Results — Findings. One record per …, Tabulation.") 在 EG/spec.md:3 是改写 ("> Class: Findings | Structure: …"); 属 D3 已列 R4-blocked 的 4 条数据集标题行之一 (CE/EG/DD/SU), 仅记录.
- X-3: O6 标签 "Example 3" 应为 "Example 1" (见上), 建议主控修正 out_of_scope_findings.md 描述.

### git diff --stat
```
 knowledge_base/domains/EG/examples.md | 46 +++++++++++++++++------------------
 1 file changed, 23 insertions(+), 23 deletions(-)
```
- 本批只改 EG/examples.md; 工作区其他改动 (AE/GF/ch02/ch04 等) 为并行批次, 非本 writer.

## attempt 1 续 (主控扩 kb_files += EG/assumptions.md, 2026-11-26)

- EG/assumptions.md md5: before `662bdb98bda2d0c6d9d51a1d949daa66` → after `cfe168a016c17f5081718357133c96d3` (+6 行)

| # | kb_file:line (改后) | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 9 | EG/assumptions.md:3-5 | ig34_p0185_a020 (原 #8 SKIPPED_STRUCT → 本次落地) | INSERTED | H1 后新增 `## EG – Description/Overview` (PDF 原标题) + 定义句逐字 ("A findings domain that contains ECG data, … if collected or derived.") ; 格式仿 SC/assumptions.md | 185 |
| 10 | EG/assumptions.md:7 | R3 PDF 标题 "EG – Assumptions" | INSERTED | 新增 `## EG – Assumptions` 标题 (PDF p188 原标题; SC 同惯例); 未改 H1 / 已有锚点 | 188 |

- 双向扫描 (assumptions 1-11 vs p188-189 "EG – Assumptions" 至 "EG - Examples"): 归一 (合并空白, U+2011 → "-", 去编号) 后 PDF 文本 == KB 文本 → 0 缺口 / 0 KB 自写. p188 顶部 spec 表尾 + 脚注属 EG/spec.md, 不在本文件.
- 锚点: `grep -rn "EG/assumptions.md#"` (knowledge_base docs web/src tools AGENT_GUIDE README) 0 命中, 新增标题不影响链接.
- fp_match (全量, 对 attempt 1 base 的 fp_before): 回归 0; 新命中 8 = 本批 7 (p0185_a020 + 前述 6) + ig34_p0223_a012 (GF/assumptions.md, 并行批 B-GF 改动所致, 非本批). hit_target 3751 → 3759.
- `python3 tools/check_links.py | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (基线 42, 未升).
- git diff --stat (本批): EG/examples.md 46 (+23/-23), EG/assumptions.md +6.
