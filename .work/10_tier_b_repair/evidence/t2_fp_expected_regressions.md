# T2 fp_match 全局回归定性 (HEAD 50c3958)

> 状态: **已完成** (2026-11-26). 只读 KB; 未改 `work/t1_errata.json` (主控合并).
> 机器可读: `work/t2_fp_expected_regressions.jsonl` (atom_id / class / note), 供后续 reviewer diff.

## 1. 口径说明

`scripts/fp_match.py` 判定:

- `hit_target`: `norm(verbatim)` 是否为某个 **target 文件** 的子串. target = 台账 `md_atom_ids` 所在文件 ∪ `section_coverage.wc.jsonl` 的 `md_target_files`. 台账固定, 所以内容迁到别的文件后不会自动跟上.
- `hit_any`: 在 target 外整个 KB 任一文件命中 (只给出 glob 序第一个文件, 不是"正确位置").
- `verdict`: 原样抄自固定台账 `coverage_ledger.wc.jsonl`, **不反映 KB 现状**. REGRESS 行打印的 EXACT/EQUIVALENT 只是 T1 时的判定, 不能当作"现在仍 EXACT".
- **回归** = baseline `hit_target` 为真, 当前为假. 与 verdict、hit_any 无关. `new_hits` 只作参考, 不影响 RED/GREEN.
- `norm()` 只把 markdown 记号 (星号、下划线、反引号、竖线、`>`、`#`、反斜杠、`~`) 换成空格、统一引号/破折号、合并空白、转小写; **不去句点、不去空格内差异**. 所以多一个 `.` 或多一个空格 (CV `Cross-sec.`、DV `PERFORMED.`、CE `ABC -US`) 就会回归.
- fp_match **不读 errata**. 已登记在 `t3_atom_err` / `t3_target_remap` 里的条目仍计入回归数, 所以全局跑永远是 RED. 实查 (`grep -rn "t1_errata\|t3_atom_err\|t3_target_remap" scripts/`): 现有脚本只有 `t1_merge.py` 读 errata 的 `kb_loc` / `pending_user`, **没有任何脚本消费 `t3_atom_err` / `t3_target_remap`**; T3 回写须新写或扩展脚本.
- **注意 `t3_recompute.py --downgrade`**: 它把 `--regress-out` 文件里每条原子的 EXACT/EQUIVALENT 降为 MISSING. 若直接喂 `regress_head.jsonl`, 本文件 60 条良性回归会全部被降为 MISSING. 应先减去本清单 (或按 errata 过滤) 再喂.

writer 与 reviewer 数量不同的原因:

| 跑法 | baseline | KB | 得到什么 |
|---|---|---|---|
| reviewer 常用 | 固定 `work/fp_baseline.jsonl` (T0 时点) | HEAD 工作区 | **累计**回归: 所有已提交批 + 工作区中并行批的改动. 随批次提交单调上升 (48 → 60) |
| writer 常用 | 本批改前 KB 拷贝 (`--kb-root $S/basekb` 跑出 `fp_before`) 或同一 baseline 后按 target 过滤 | 改后 | **本批增量** (2-4 条) |

两者都对, 只是范围不同. 判"本批有无非预期回归"应: 全局清单 − 本文件 60 条 (或 diff 前后两次全局跑), 剩下的才归本批.

## 2. 复跑命令

```bash
G=.work/10_tier_b_repair/work/scratch/t2/global   # gitignored (work/.gitignore: scratch/)
mkdir -p $G
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $G/fp_head.jsonl \
  --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $G/regress_head.jsonl   # regressions=60 new_hits=736, exit 1
python3 -I $G/dump_regress.py      # 每条: verbatim / baseline hit / 当前 hit_any / errata / 最长公共子串上下文
python3 -I $G/verify_regress.py    # 每条: target 中最像的 KB 行, 原子与 KB 的词级 diff, 两侧差异词是否在 PDF p..p+1
python3 -I $G/classify.py          # 分类 + 断言 (60 条全覆盖, 每条 KB 侧/PDF 侧证据词实测) → work/t2_fp_expected_regressions.jsonl
# 期望输出: BAD []  Counter({'R3': 25, 'R1': 24, 'R2': 11})
diff <(jq -r .atom_id $G/regress_head.jsonl | sort) <(jq -r .atom_id .work/10_tier_b_repair/work/t2_fp_expected_regressions.jsonl | sort)   # 后续批: 空 = 无新回归
```

`classify.py` 对每条做了: `from fp_match import norm`; `norm(verbatim) in norm(新 target 文件)`; KB 侧证据词 ∈ `norm(KB 文件)`; PDF 侧证据词 ∈ `norm_pdf(pdf_pages p, p+1)`. 表格行的 PDF 文本层有单元格换行 (VISIT `1` / WEEK `5` / USUBJID 尾 `601` 落到下一行), 整行子串无法直查, 改为对 `work/pdf_pages/ig34_p0258.txt:23-39`、`p0289.txt:28-52`、`p0260.txt:10-20`、`p0263.txt:25-31`、`p0257.txt:11-30` 逐格人工核对 (见依据列).

## 3. 计数

| 类别 | 含义 | 条数 |
|---|---|---|
| R1 | 原子抽取错 (原子 ≠ PDF, KB = PDF) → `t3_atom_err` | 24 |
| R2 | KB 有意偏离 PDF (PDF_TYPO 修正 / 保留值, 有 T-n) → `t3_atom_err` | 11 |
| R3 | 内容迁移 (RELOCATE / D2 去重), 新位置命中 → `t3_target_remap` | 25 |
| R4 | 真丢失 (KB 找不到 PDF 原文) | **0** |
| 合计 | | 60 |

errata 缺口 (t3_atom_err ∪ t3_target_remap 都没有逐条键) 共 33 条: CE 8 条、`ig34_p0174_a0012`、B-FA 23 条 (只有组键 `_B-FA`, 按 atom_id 查会漏, 建议展开为逐条键)、`ig34_p0396_a009`. 另有 3 条需要**两个**键: `ig34_p0257_a010` / `ig34_p0257_a016` (原 target MB/examples.md 的副本已被 B-MS D-5 删除, 改正 verbatim 后还须 remap → `knowledge_base/domains/MS/examples.md`), `ig34_p0218_a014` (B-CP D-19 删 assumptions 附录, 现在 `knowledge_base/domains/CP/examples.md:267`).

## 4. 逐条清单

证据列: `v∈KB` = 原子 verbatim 归一后是否在新 target 中; `kbTok` / `pdfTok` = KB 侧 / PDF 侧差异证据词实测 (None = 表格换行, 人工核); `atom∈PDF` = 原子是否为 PDF p..p+1 文本子串.

| atom_id | 类别 | 依据 | 新 target | 证据 | 建议 errata 键 |
|---|---|---|---|---|---|
| ig34_p0118_a017 | R2 | B-EX T-6 PDF_TYPO mg/mL→mg/kg | `domains/EX/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True | t3_atom_err (已有) |
| ig34_p0153_a0034 | R1 | 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定) | `domains/CE/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (**缺**) |
| ig34_p0154_a0002 | R1 | 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定) | `domains/CE/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (**缺**) |
| ig34_p0154_a0013 | R1 | 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定) | `domains/CE/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (**缺**) |
| ig34_p0154_a0014 | R1 | 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定) | `domains/CE/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (**缺**) |
| ig34_p0154_a0015 | R1 | 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定) | `domains/CE/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (**缺**) |
| ig34_p0154_a0029 | R1 | 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定) | `domains/CE/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (**缺**) |
| ig34_p0154_a0030 | R1 | 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定) | `domains/CE/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (**缺**) |
| ig34_p0155_a0002 | R1 | 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定) | `domains/CE/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (**缺**) |
| ig34_p0174_a0012 | R2 | B-MH T-1 PDF_TYPO 第二处 MHENDTYP→MHEVDTYP (原子=PDF) | `domains/MH/assumptions.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True | t3_atom_err (**缺**) |
| ig34_p0179_a0018 | R1 | 原子丢 DVTERM 句点; PDF p179 为 `PERFORMED.`, KB 同 (B-DV E-1) | `domains/DV/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (已有) |
| ig34_p0215_a018 | R2 | B-CP T-2 PDF_TYPO CPCSMRKR→CPCSMRKS | `domains/CP/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True | t3_atom_err (已有) |
| ig34_p0218_a014 | R2 | B-CP T-15 PDF_TYPO CPGATEDEF→CPGATDEF; 另 B-CP D-19 删 assumptions 附录副本, 现在 CP/examples.md:267 | `domains/CP/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True | t3_atom_err (次: t3_target_remap→CP/examples.md) (已有) |
| ig34_p0254_a040 | R3 | B-MS 迁移: 原子命中于 MS/spec.md (已在 t3_target_remap) | `domains/MS/spec.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap (已有) (已有) |
| ig34_p0254_a042 | R3 | B-MS 迁移: 原子命中于 MS/spec.md (已在 t3_target_remap) | `domains/MS/spec.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap (已有) (已有) |
| ig34_p0257_a010 | R1 | 原子抄自旧 KB 错值 (MSORRES/MSSTRESC 空; PDF r3 = 1/1); 另 B-MS D-5 去 MB 副本, 现在 MS/examples.md:25 | `domains/MS/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有; 次: remap→MS/examples.md) (已有) |
| ig34_p0257_a016 | R2 | B-MS T-1 r9 MSSTRESC PDF 空, KB 保留 25 (原子=PDF); 另 D-5 去 MB 副本, 现在 MS/examples.md:31 | `domains/MS/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有; 次: remap→MS/examples.md) (已有) |
| ig34_p0258_a019 | R1 | 原子抄自旧 KB 错值: VISIT 缺 `1` (PDF p258 VISIT 列换行为 `VISIT 1`) (B-MB) | `domains/MB/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0258_a020 | R1 | 原子抄自旧 KB 错值: VISIT 缺 `1` (PDF p258 VISIT 列换行为 `VISIT 1`) (B-MB) | `domains/MB/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0258_a021 | R1 | 原子抄自旧 KB 错值: VISIT 缺 `1` (PDF p258 VISIT 列换行为 `VISIT 1`) (B-MB) | `domains/MB/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0258_a022 | R1 | 原子抄自旧 KB 错值: VISIT 缺 `1` (PDF p258 VISIT 列换行为 `VISIT 1`) (B-MB) | `domains/MB/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0258_a023 | R1 | 原子抄自旧 KB 错值: VISIT 缺 `1` (PDF p258 VISIT 列换行为 `VISIT 1`) (B-MB) | `domains/MB/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0258_a024 | R1 | 原子抄自旧 KB 错值: VISIT 缺 `1` (PDF p258 VISIT 列换行为 `VISIT 1`) (B-MB) | `domains/MB/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0260_a009 | R1 | 原子 BEREFID `100`; PDF p260 r4 = `100.3` (B-MB) | `domains/MB/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0260_a015 | R1 | 原子 BELNKID `3`; PDF p260 r10 BELNKID 空 (B-MB) | `domains/MB/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0262_a029 | R2 | B-MS T-3 PDF_TYPO IDVAR MBREFID→MSREFID | `domains/MS/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True | t3_atom_err (已有) (已有) |
| ig34_p0262_a030 | R2 | B-MS T-3 PDF_TYPO IDVAR MBREFID→MSREFID | `domains/MS/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True | t3_atom_err (已有) (已有) |
| ig34_p0263_a020 | R2 | B-MB T-3 PDF_TYPO 表头 MBTRESN→MBSTRESN; 另 PDF 印刷 MBGPRID, 原子与 KB 均为 MBGRPID (B-MB T-2) | `domains/MB/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0263_a021 | R1 | 原子 VISIT `WEEK 1`; PDF p263 VISIT 列换行为 `WEEK 5` (B-MB) | `domains/MB/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0263_a022 | R1 | 原子 VISIT `WEEK 1`; PDF p263 VISIT 列换行为 `WEEK 5` (B-MB) | `domains/MB/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0289_a024 | R1 | 原子漏 `Cross-sec.` 句点; PDF p289 文本层 rows 7-8 为 `Cross-sec.` (ig34_p0289.txt:48,52), KB 同 (B-CV #5/#6) | `domains/CV/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0289_a025 | R1 | 原子漏 `Cross-sec.` 句点; PDF p289 文本层 rows 7-8 为 `Cross-sec.` (ig34_p0289.txt:48,52), KB 同 (B-CV #5/#6) | `domains/CV/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0311_a035 | R2 | B-RE T-1 PDF_TYPO IREEA2→IRREA2 | `domains/RE/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True | t3_atom_err (已有) (已有) |
| ig34_p0363_a011 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0363_a012 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0363_a013 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0363_a015 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0363_a016 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0363_a017 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0363_a018 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0363_a019 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a001 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a002 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a003 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a004 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a005 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a006 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a007 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a008 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a009 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a011 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a012 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a013 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a017 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a018 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0364_a019 | R3 | B-FA RELOCATE §6.4.2/§6.4.3 (ch02/model02 → FA/assumptions.md; checkpoint 表 #3/#4, review H 节 23 条) | `domains/FA/assumptions.md` | v∈KB=True; kbTok=None; pdfTok=None; atom∈PDF=True | t3_target_remap→domains/FA/assumptions.md (现仅 `_B-FA` 组键) (**缺**) |
| ig34_p0370_a021 | R2 | B-FA T-7 PDF_TYPO parent CE→AE | `domains/FA/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True | t3_atom_err (已有) (已有) |
| ig34_p0373_a013 | R2 | B-FA T-9 PDF_TYPO FAEVINTX→FAEVLINT | `domains/FA/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True | t3_atom_err (已有) (已有) |
| ig34_p0374_a011 | R1 | 原子把 AE ID 行与合并格说明抽成同一行, 与渲染不符; KB :263 为 4 空格 + 说明合并格, :265 为 AE ID…Visit 6 (按渲染分两行, 9 列) | `domains/FA/examples.md` | v∈KB=False; kbTok=True; pdfTok=None; atom∈PDF=False | t3_atom_err (已有) (已有) |
| ig34_p0396_a009 | R1 | 原子 `represents`; PDF p396 为 `represented this rule`, KB 同 (B-TA #31) | `domains/TA/examples.md` | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False | t3_atom_err (**缺**) |

## 5. R4 (真丢失)

无. 60 条中每条都在 KB 中找到了对应 PDF 原文 (R1/R2 为同位置差异词已核, R3 为新文件逐字命中).

## 6. 备注

- B-FA 组 23 条 (p0363_a011-a013, a015-a019; p0364_a001-a009, a011-a013, a017-a019) 逐条 `norm(verbatim) in norm(FA/assumptions.md)` = True; p0364_a013 表头 `| FATESTCD | FATEST |` 的 hit_any 显示 FA/examples.md 只是 glob 序, assumptions 中同样命中. p0363_a014 仍命中原 target, 不在清单. 与 `evidence/checkpoints/t2_B-FA_review.md` H 节 23 条一致 (writer 报 24 / 27 有重复计数).
- 分类判据统一为: KB = PDF 且原子 ≠ PDF → R1; KB 有意 ≠ PDF → R2. 按此 CE 8 条 (B-CE T-2 照录 PDF 带空格) 与 DV p0179_a0018 (照录句点) 同归 R1. 若用户日后裁定 CE 去空格, 这 8 条自动恢复命中, 届时从 errata 移除.
- `ig34_p0254_a040` / `a042` (VISITNUM / VISIT 代码字面量) 已在 `t3_target_remap` → MS/spec.md, 当前命中.
- 本清单只覆盖 baseline 曾命中、现不命中的原子; baseline 即未命中的原子 (如 B-MH 的 p0173_a0007 T-3) 不在 fp 回归口径内.
