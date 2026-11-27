# T3 回写独立审计 (规则 A / 规则 D)

<!-- chain: E (plans) -->
> 状态: **终审 PASS (attempt 4, 见本文件 §attempt 4 终审, 约 :479)**; attempt 1-3 FAIL 已归档 `evidence/failures/step_T3_attempt_*.md`. (T4 主控 2026-11-27 改状态行; 原状态行: **FAIL** (2026-11-26).) 审计者: `oh-my-claudecode:verifier`, 与 writer (`oh-my-claudecode:executor`) 不是同一个 agent.
> 审计范围: T3.1 回写和 T3.2 重算, 以 `evidence/checkpoints/t3_recompute.md` 的 §主控裁定 C1-C6 (v2) 为准.
> 本次只读. 改动只有两处: 本文件, 以及临时目录 `work/scratch/t3_audit/` (已被 gitignore). 没有改 KB、ledger、脚本, 也没有 commit.
> 审计时 ledger md5 = `634aedcfeccd820ee182a930ec39352c`, pre_t3 备份 = `620c4a19…`, 真 KB 全部 .md 拼接后 md5 = `b3a040150c53a4256ea0dde645bd7d07` (前后不变).

## 0. 结论

**FAIL.** 分层抽样 69 个原子 (70 个样本位; `ig34_p0432_a026` 同时落在 EQUIVALENT 层和 T2S 层), 其中 **2 条终态不成立**. 按规则 "任何 1 条错 → FAIL" 判定.

另外, 对全体样本做性质扫描时, 又发现 **7 条终态错误**和 2 个脚本缺陷. 后者会造成假绿, 并已经用变异测试复现.

计数层面全部一致:
- 改动集 ⊆ 允许集, 未改行逐字节一致;
- EXACT 1000 / EQUIV 48 / IE 490 / ATOM_ERR 159 / PDF_TYPO 55 / FIGURE_DEFERRED 11, 残留 46;
- 变异测试和 live docs 都能复现.

所以问题**不在计数**, 而在**单条判定规则**:
- EXACT 的取靶过宽, 而且不检查词边界;
- 规则 6 只看 note, 不看 ref;
- S1 的 R1/R2 判定有误;
- 直接命中复验只核对自己记下的 hit_file, 是自证.

## 1. 代码审 (t3_writeback / t3_direct_hit / t3_global_coverage / t3_reverse_trace)

| # | 位置 | 问题 | 后果 (实测) | 级别 |
|---|---|---|---|---|
| K1 | `t3_writeback.py` `targets()` + `decide()` 的 `hit = next(f for f in tg if v in kb_norm(f))` | 候选靶的来源和顺序: 先放 section `md_target_files` 排序后的结果 (含 `VARIABLE_INDEX.md`、`chapters/*`、`model/*`), 后放 kb_loc / writer / remap. 取第一个命中的文件, 子串匹配不检查词边界 | 假 EXACT 和错位 EXACT (见 §3.2 E1-E3) | **HIGH** |
| K2 | `t3_direct_hit.py` 对 TB 行的处理 `tg = [hit_file]` | 只复核 writer 自己记下的 hit_file, 等于自证 | 在 kbcopy2 里删掉 CE `[ ] Surgery`、EX/EC 的全部 `ec.xpt` 标签、NV/spec `### VISITNUM` 整块之后, 结果仍是 **GREEN** (见 §5.3) | **HIGH** |
| K3 | `decide()` 规则 6 `re.findall(r"\bT-(\d+)", w["note"])` | 只从 note 里取 T-n. ref 里写的 `T-19:ig34_p0206_a009` 不会被识别 | 已登记的 PDF_TYPO 被判成 EQUIVALENT (`ig34_p0206_a009`, 抽样错 1). 同类 writer 行还有 10 条, 都是 stock 判定, 不在本次翻转范围内 (B-GF ×6, B-IS ×2, B-ch02 ×1, S-SPC1 `p0205_a005`) | **HIGH** |
| K4 | `t3_errata_build.py` 的 R1/R2 判定 (清单类别 → 照录 → T-n → 其余判 R1) | 判 R1 前没有核对 "原子 ∉ PDF". basis 写的是 "verbatim 与 PDF 页文本不符", 与事实相反 | 2 条本应是 PDF_TYPO 的被判成 ATOM_ERR (§3.2 E4) | **HIGH** |
| K5 | 允许集断言 `changed id outside allowed` | `new_rows` 本来就只从 ALLOWED 生成, 这条断言恒真 | 独立复算结果为 ⊆ 成立 (§2), 但断言本身没有防护作用 | LOW |
| K6 | IE 断言 `IE_FINAL` 用正则抓 `t1_ie_final.md` 中出现的所有 id | 该文件 5 节都是 IE 类别 (SPEC_TABLE_ROW / VERSION_MISMATCH / SPEC_TABLE_HEADER / REDUNDANT_WITH_SPEC / CODE_LITERAL_IE), 当前不构成绕过. 但它只按 "id 出现在文件里" 判, 不按所在节判 | 当前无影响 | LOW |
| K7 | C3 口径 | CONDITIONAL 批 (B-PCPP/B-CP/B-LB) 的 fix 行不被采信 (正确). 但这三批的 registry 照样支撑 PDF_TYPO: 有 8 条 (S1-R2 7 + writer-Tn 1, 如 `p0215_a017` B-CP T-3、`p0218_a014` B-CP T-15) | 口径不一致, 需主控裁定. EXACT live-hit 57 条有当场命中作独立证据, 不受影响 | MEDIUM |
| K8 | 重复 id | 11 个重复 id 两行一起改写. 只有 `sv20_p0004_a003` 发生翻转 (PARTIAL,PARTIAL → EXACT,EXACT), 处理正确 | — | OK |
| K9 | `verdict_ptr` 弱回退 ("最后一行含 PASS") | `t2_B-GF_audit.md:56` 指到了 trace 行 ("续签字 PASS"), 而 :60 才是真正的结论行. 人工核过该批确为 PASS | 指针不准, 但判定不受影响 | LOW |
| K10 | `t3_reverse_trace.py` | `MERMAID` 类整块不做任何检查; `TABLE_TOKENS` 的比对单位是任意 PDF 页对的词袋, 不限定该表所在页 | 宽口径类别需要靠抽样补 (§4) | MEDIUM |
| K11 | 短 verbatim 只判 "有无", 不判个数 | 同节同文本的多个 EXACT 原子可能共用 1 处 KB 出现 | 6 组: `ec.xpt` 4 原子 / 词边界内 0 处 (hit 在 ch04 的 `relrec.xpt`); `relrec.xpt` 3/1 (ch04); `ce.xpt` 3/1; `da.xpt` 2/1; `dd.xpt` 2/1; `aesmie = "y"` 2/1 | MEDIUM |

`t3_global_coverage.py`: 公式与 docstring 一致. 我用 pre_t3 复现出 06 口径的 99.0192%, 与 writer 一致. 没有发现问题.

## 2. 独立复算 (不 import t3_* 模块, 只用 `scripts/fp_match.py` 的 norm / norm_pdf)

命令:
```bash
python3 -I .work/10_tier_b_repair/work/scratch/t3_audit/a1_diff.py   # ledger 前后 diff + 允许集 + 计数
python3 -I .work/10_tier_b_repair/work/scratch/t3_audit/a2_props.py  # 全体 TB 行性质扫描 (原子∈PDF? 原子∈KB?)
python3 -I .work/10_tier_b_repair/work/scratch/t3_audit/a6_boundary.py  # TB EXACT 词边界复核
```

| 核对项 | 结果 |
|---|---|
| 行数 | pre 12487 / post 12491 (追加 4 行: `ig34_p0017_a029` / `p0042_a007` / `p0048_a012` / `p0396_a004`, 都不在 pre 中) |
| 改动行 | 1760 行 (+4 追加). 改动的字段只有 verdict、matched_by (各 1760); category、exclusion_reason、approved_by 只在 IE 行改动 (各 490). 每条改动行 phase == TB, verdict 都与原值不同 |
| 未改行 | 逐字节一致, 且 id 次序未动 |
| 允许集 | triage ∪ t3_t2s_atoms ∪ errata (atom_err ∪ target_remap) = 1851, 与 pdf_atoms 取交后为 **1849**. 改动 id 共 1763 个, **全部在允许集内** (集合外 0) |
| 终态计数 (按原子) | EXACT **1000** (live-hit 977 + was-IE 23) / EQUIVALENT **48** (T1 两 agent 16 + T1+T2 改写 13 + T2 fix+PASS 16 + C1 3) / IE **490** / ATOM_ERR **159** / PDF_TYPO **55** (S1-R2 31 + writer-Tn 24) / FIGURE_DEFERRED **11** — 与 writer 报告**完全一致** |
| 残留 | 允许集内仍是非终态的原子共 46 个 (PARTIAL 26 / MISPLACED 20), 与 `t3_audit_sets/residual.txt` 的集合差为 ∅ |

性质扫描 (全体 TB 行, PDF 取 p-1..p+1 页):
- EXACT: 117 条原子 ∉ PDF, 是表行或排版差异, 抽样里有这类, 都没问题. 词边界失败 9 条 (见 K1). 244 条命中 >1 个 KB 文件.
- ATOM_ERR: **2 条原子 ∈ PDF** (见 E4). 2 条原子 ∈ KB: `p0124_a001` 是原子被截断, 成为 KB 行的子串, 没问题; `p0009_a024` 是通用表头, 没问题.
- PDF_TYPO: 1 条原子 ∈ KB (`p0198_a012`: 原子 = KB ≠ PDF 'part the', B-T-2 已登记, 可以接受). 25 条原子 ∉ PDF, 都是表行.

## 3. 分层抽样 (seed 20261126, `a3_sample.py`)

命令: `python3 -I .work/10_tier_b_repair/work/scratch/t3_audit/a3_sample.py && python3 -I .work/10_tier_b_repair/work/scratch/t3_audit/a4_dossier.py EXACT,EQUIVALENT,ATOM_ERR,PDF_TYPO,T2S,C5,IE`.
每条都打开了 `work/pdf_pages/` 的 PDF 页文本和现 KB 文件的对应行 (grep 或 sed 定位), 逐条判定.

### 3.1 样本表

| 层 (全集) | atom | 终态 | KB 位置 / 依据 | 判定 |
|---|---|---|---|---|
| EXACT (977) | ig34_p0235_a021 | EXACT | IS/examples.md:91 = PDF row 5 | ✓ |
| | ig34_p0210_a015 | EXACT | CP/examples.md:45 = PDF row 13 | ✓ |
| | ig34_p0011_a027 | EXACT | ch02:37 | ✓ |
| | ig34_p0282_a047 | EXACT | PC/examples.md:420 | ✓ |
| | ig34_p0344_a020 | EXACT | TU/assumptions.md:13 | ✓ |
| | ig34_p0016_a021 | EXACT | ch02:182 `- POOLID` | ✓ |
| | sv20_p0004_a018 | EXACT | model/01:18 | ✓ |
| | ig34_p0124_a023 | EXACT | ML/examples.md:72 | ✓ |
| | ig34_p0142_a020 | EXACT | AE/examples.md:90 | ✓ |
| | ig34_p0289_a004 | EXACT | CV/examples.md:5 | ✓ |
| | ig34_p0080_a010 | EXACT | hit_file 是 ch08:96 (位置不对), 但 SE/spec.md:123 也有该行 | ✓ (指针不准, 见 K1) |
| | ig34_p0285_a002 | EXACT | NV/assumptions.md:5, 在 §6.3.6 MO 节下 (S-HOST 插入) | ✓ |
| | ig34_p0282_a050 | EXACT | PC/examples.md:423 | ✓ |
| | ig34_p0125_a003 | EXACT | PR/assumptions.md:5 | ✓ |
| | ig34_p0018_a037 | EXACT | ch03:49 `ft.xpt` | ✓ |
| EQUIVALENT (48) | ig34_p0152_a0014/a0009/a0012/a0010 | EQUIV | CE/examples.md:41-46 CRF 表, 用 ( ) 表示 PDF 的 o. 语义与 PDF 一致 | ✓ ×4 |
| | ig34_p0153_a0013/a0018/a0024/a0022/a0009 | EQUIV | CE/examples.md:77-83, 用 ( ) / [ ] 表示 ○/□ | ✓ ×5 |
| | ig34_p0118_a007 | EQUIV | EX/examples.md:350: Personal reason 在第 3 次访视, = PDF p118:9 (原子列序有误) | ✓ |
| | ig34_p0115_a030 | EQUIV | EX/examples.md:245-247 双层表头 = PDF | ✓ |
| | ig34_p0432_a026 | EQUIV | SUPPQUAL/spec.md:98 (原子为 "1 In", 有空格, 所以 norm 后不命中) | ✓ |
| | ig34_p0116_a019 | EQUIV | EX/examples.md:276 `BOTTLE 2`/`TREATMENT 2` = PDF 折行 (原子截断) | ✓ |
| | ig34_p0056_a005 | EQUIV | ch04:1477 = PDF p56:32-36 (原子是改写过的) | ✓ |
| | **ig34_p0206_a009** | EQUIV | CP/assumptions.md:82 写 `CPSBMRKS`, PDF/原子写 `CPSMRKS`. 这是已登记的 **S-SPC1 CP T-19 (另有 T-16a)** 有意偏离 | **✗ 应为 PDF_TYPO** (K3) |
| ATOM_ERR (159) | ig34_p0348_a010 | ATOM_ERR | 原子 `TUTEST`, PDF/KB 为 `TUTESTs` (TU/assumptions.md:76) | ✓ |
| | ig34_p0154_a0014 | ATOM_ERR | 原子 `ABC-US-701-002`, PDF/KB 为 `ABC -US-701-002` (B-CE T-2 照录 + T4) | ✓ (T4 待裁) |
| | ig34_p0112_a009 | ATOM_ERR | `[Field] \| [Value]` 是合成表头, PDF 中没有 | ✓ |
| | ig34_p0226_a010/a013/a021 | ATOM_ERR | 原子 `ABU3908AS2`/`1s37d5`/`.fasta.gz`/`ENST…466554` ≠ PDF `ABU3908A52`/`hs37d5`/`.fastq.gz`/`ENST…646664`, KB = PDF (GF/examples.md:89/91/100) | ✓ ×3 |
| | ig34_p0374_a011 | ATOM_ERR | FA/examples.md:263-265: 合并格与 PDF 渲染一致 | ✓ |
| | ig34_p0161_a0012 | ATOM_ERR | 原子 `DSCAT`, PDF/KB 为 `DSSCAT` (DS/examples.md:120) | ✓ |
| | ig34_p0337_a002 | ATOM_ERR | 原子 `RSORRESRU` / `or original`, PDF/KB 为 `RSORRESU` / `for original` (RS/assumptions.md:80) | ✓ |
| | ig34_p0167_a0010 | ATOM_ERR | 原子 `DSEQ`, PDF/KB 为 `DSSEQ` (DS/examples.md:405) | ✓ |
| PDF_TYPO (55) | ig34_p0118_a017 | PDF_TYPO | B-EX T-6 mg/mL→mg/kg, EX/examples.md:362 | ✓ |
| | ig34_p0257_a016 | PDF_TYPO | B-MS T-1, MS/examples.md:31 中 MSSTRESC=25 | ✓ |
| | ig34_p0215_a017 | PDF_TYPO | B-CP T-3 补右括号, CP/examples.md:200 | ✓ (依据来自 CONDITIONAL 批, K7) |
| | ig34_p0010_a023 | PDF_TYPO | B-ch01 T-2: ch01:109 中 MANY → `--LNKGRP` | ✓ |
| | ig34_p0200_a006 | PDF_TYPO | S-SPC1 T-17 sting→string, CP/assumptions.md:40 | ✓ |
| | ig34_p0263_a020 | PDF_TYPO | B-MB T-2/T-3 (MBGPRID / MBTRESN), MB/examples.md:241 | ✓ |
| | ig34_p0218_a014 | PDF_TYPO | B-CP T-15 CPGATEDEF→CPGATDEF, CP/examples.md:267 | ✓ (K7) |
| | ig34_p0356_a002 / p0355_a025 | PDF_TYPO | B-TR T-1 Row/TRSEQ 重编号, TR/examples.md:45/:41 | ✓ ×2 |
| | ig34_p0198_a012 | PDF_TYPO | B-BS T-2 'part the', BS/assumptions.md:19 | ✓ |
| T2S 来源 (228) | ig34_p0155_a0017 | EXACT | DS/assumptions.md:9 | ✓ |
| | ig34_p0438_a011 | EQUIV | RELSUB/spec.md:53 (原子为 "1 In", 有空格) | ✓ |
| | ig34_p0249_a002 | EXACT | MB/assumptions.md:13 | ✓ |
| | sv20_p0049_a002 | EXACT | model/03:199 | ✓ |
| | sv20_p0062_a002 | EXACT | model/05:297 | ✓ |
| | sv20_p0050_a009 | EXACT | model/04:25 | ✓ |
| | sv20_p0047_a017 | EXACT | model/03:170 (在 SV 节内; hit 指针指向 :83, 那是另一节中的同句) | ✓ |
| | ig34_p0317_a011 | EXACT | PE/spec.md:276 | ✓ |
| | ig34_p0432_a026 | EQUIV | 同上 | ✓ |
| | sv20_p0047_a014 | EXACT | model/03:168 | ✓ |
| C5 IE→EXACT (23) | ig34_p0183_a020 | EXACT | DD/spec.md:114 | ✓ |
| | ig34_p0193_a025 | EXACT | IE/spec.md:168 | ✓ |
| | ig34_p0296_a005 | EXACT | hit 在 NV/assumptions.md:44 (通用表的脚注), 但 NV/spec.md:384 也有该行 | ✓ |
| | **ig34_p0295_a020** | EXACT | 唯一命中是 NV/assumptions.md:40, 属于 **§6.3.7.1 通用 Morphology/Physiology 表**, 不是 §6.3.7.4 NV 表. NV/spec.md 中 VISITNUM 是字段块格式 (:275), 不逐字. 原 IE SPEC_TABLE_ROW 才是正确终态 | **✗ 错位 EXACT** (K1) |
| | ig34_p0288_a018 | EXACT | CV/spec.md:384 | ✓ |
| 残留 IE (490) | ig34_p0187_a016 / p0187_a019 | IE | EG/spec.md:322-327 / :349-354, 字段块与 PDF 一致 | ✓ ×2 |
| | ig34_p0121_a029 | IE | ML/spec.md:205-210 | ✓ |
| | ig34_p0331_a002 | IE | RS/spec.md:241-246 | ✓ |
| | ig34_p0295_a017 | IE | NV/spec.md:250-255 | ✓ |

抽样结果: **67/69 成立, 2 条错** (`ig34_p0206_a009`, `ig34_p0295_a020`) → **FAIL**.

### 3.2 抽样之外, 性质扫描发现的终态错误 (都需要修正)

| # | atom | 现终态 | 事实 | 应为 |
|---|---|---|---|---|
| E1 | ig34_p0153_a0019 `\| \| o Surgery \|` | EXACT | 命中 TA/examples.md:995 中的 "consent t**o surgery**", 是没有词边界造成的假命中. 真实内容在 CE/examples.md:81 `[ ] Surgery`, 同组兄弟原子都是 EQUIVALENT | EQUIVALENT (T1 两 agent) |
| E2 | ig34_p0294_a017 / a018 / a020, ig34_p0295_a020 (C5) | EXACT | NV 规范表的表头、STUDYID、USUBJID、VISITNUM 只命中 §6.3.7.1 通用表 (NV/assumptions.md:29/31/33/40) | 回到 IE (SPEC_TABLE_HEADER / ROW) |
| E3 | ig34_p0111_a016, p0112_a025, p0118_a022, p0120_a001 `ec.xpt` | EXACT | hit_file 是 ch04, 命中的是 "rel**rec.xpt**". EX/EC examples 里有 8 处 `ec.xpt`, 内容大概率还在, 但证据指针是错的 | 在 EX/EC 中按词边界重新取靶 |
| E4 | ig34_p0334_a011, ig34_p0338_a006 | ATOM_ERR | 原子 = PDF ("symptomatic determination" / "an resolution"). KB 有意改写, 分别登记为 **B-RS T-8** / **B-RS T-5 (RS 副本)**. errata 的 basis "verbatim 与 PDF 页文本不符" 不成立 | PDF_TYPO |

## 4. G-TB6: writer 自定义类抽样 (seed 20261126, `a8_g6.py` / `a9_rowpdf.py`)

复跑命令: `python3 -I .work/10_tier_b_repair/scripts/t3/t3_reverse_trace.py --out .work/10_tier_b_repair/work/scratch/t3_audit/reverse_trace.json`
结果: added 5336 行, traced 100%, 各类计数与 writer 一致 (TABLE_TOKENS 680 / MERMAID 322 / KB_NOTE 248 / SPEC_FIELD 61 / XREF_D2 23 / HEADING_NOT_IN_PDF 21 / KB_NOTE_SCOPE 15).

抽样 30 行, 另加 HEADING_NOT_IN_PDF 全部 21 行:

| 类 | N | 核法 | 结果 |
|---|--:|---|---|
| TABLE_TOKENS | 12 | 按行号逐格对 PDF 表行: model/02:173 ↔ sv20 p22 row 6; TU/assumptions:101 ↔ p349:29; ch10:28 ↔ p444; model/03:217 ↔ sv20 p49:26; CP/examples:160 ↔ p214:17 (0.6); MK/examples:56 ↔ p293:47; PC/assumptions:61 ↔ p276; model/05:205 ↔ sv20 p58:54; LB/assumptions:39 ↔ p196:5; model/05:80 ↔ sv20 p53:47; model/04:40 ↔ sv20 p50:26; MS/examples:23 ↔ p257 | 12/12 与 PDF 逐格一致 |
| MERMAID | 5 | TA/examples:212/417/710/923, TV/examples:39 | 图节点文字不在 PDF 文本层, T3 无法用文本核. T2 已有对照渲染页的图审 (例如 `t2_S-TDM_audit.md:60`、B-TA/B-TV review), 每张图前都有 D6 注. **不可疑, 但 T3 不提供独立证据** |
| KB_NOTE | 5 | model/02:3, ch04:936, RELSUB/spec:55, TA/examples:533, model/06:167 | 都是带 D6 标签的 KB 说明或导航 ✓ |
| SPEC_FIELD | 3 | PE/TM/LB spec:18 `Controlled Terms: <域码>` | U6 规则产物 ✓ |
| XREF_D2 | 2 | MS/examples:7, model/06:182 | 是 D2 指针, live docs 没有增加 ✓ |
| KB_NOTE_SCOPE | 3 | model/02:336 (--DTC row 10 ↔ sv20 p35:47; Notes 列在 :316 的 D6 声明下), model/06:194, model/02:166 | ✓ |
| HEADING_NOT_IN_PDF | 21 (全量) | ch02:158/167 (改写自 PDF §2.7 引言句, 下方正文为 PDF 原文); PP/examples:112/165 (KB 自写节, 有 D6); TA/assumptions:90/94; model/01:1、model/02:1 文件标题; model/02:91、model/03:147 "Variables (N variables)"; model/04:15 "AP Domain Rules"; model/05 的 10 个 "PDF 标题 + (域码)" | 都是结构或 KB 标签, 没有错误内容. LOW: ch02:158/167 是 KB 自拟标题, 不带 D6 注 |

G-TB6 抽样没有发现内容错误. 宽口径的局限见 K10.

## 5. 复跑: checkpoint §0 的变异测试与 live docs

### 5.1 writer 的变异测试

writer 脚本复制一份, 只把 S 改到 `scratch/t3_audit`, 不碰 writer 的 scratch:
```bash
sed 's#S=$T/work/scratch/t3; K=$S/kbcopy#S=$T/work/scratch/t3_audit; K=$S/kbcopy#' .work/10_tier_b_repair/scripts/t3/t3_mutation.sh > .work/10_tier_b_repair/work/scratch/t3_audit/mutation_copy.sh
bash .work/10_tier_b_repair/work/scratch/t3_audit/mutation_copy.sh
```

结果 (日志 `scratch/t3_audit/mutation.log`):
- M0: GREEN;
- M1: 删 `ig34_p0133_a021` 后 **RED** (tb_exact_miss = [ig34_p0133_a021]); 在同一份拷贝上跑 fp 回归得 72 条, 被删原子不在其中;
- M2: 复原后 GREEN;
- 真 KB md5 前后都是 `b3a04015…`.

结论: **可复现**.

### 5.2 直接命中复验与 live docs

- `python3 -I .work/10_tier_b_repair/scripts/t3/t3_direct_hit.py`:
  - TB 1000 条, stock 1769 条;
  - tb_exact_miss 0, unexplained 0, pre_existing 63;
  - GREEN, rc=0. 与 writer 一致.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` 的输出为 `broken relative links: 18668 (live docs: 42)`, ≤ 42 ✓.

### 5.3 审计者追加的变异测试: 证明 K2 会假绿

```bash
K=.work/10_tier_b_repair/work/scratch/t3_audit/kbcopy2; rm -rf $K; cp -R knowledge_base $K
# 删 CE "[ ] Surgery"; 把 EX/examples.md 的 7 处、EC/examples.md 的 1 处 \bec\.xpt 改名; 删 NV/spec.md 的 "### VISITNUM" 整块
python3 -I .work/10_tier_b_repair/scripts/t3/t3_direct_hit.py --kb-root $K   # → tb_exact_miss 0, RESULT: GREEN  (应为 RED)
```

真 KB md5 前后不变.

## 6. 必改项 (修完后重跑 T3.1 / T3.2, 并对改动层重新抽样)

1. **K1 EXACT 取靶**
   - 先在主靶 (writer kb_file / triage kb_loc / remap) 中查, 都不中才扩到 section 靶;
   - 子串匹配加词边界;
   - 规范表行、表头、脚注类原子, 命中行所在的 `##` 节必须对应原子所在节 (或该域的 spec.md);
   - 修正 E1、E2 (共 5 条, 含抽样错的 `p0295_a020`) 和 E3 (重新取靶).
2. **K3 规则 6** 同时从 ref 里取 T-n. 修正 `ig34_p0206_a009` → PDF_TYPO (S-SPC1 CP T-19 / T-16a). 另外 10 条 stock 判定的同类 writer 行要列入 T4 清单.
3. **K4 S1 判定**
   - 判 R1 前断言 `norm(原子) ∉ norm_pdf(p-1..p+1)`; 原子在 PDF 中、且有 registry 的, 改判 R2;
   - 修正 E4 (`p0334_a011` → PDF_TYPO B-RS T-8; `p0338_a006` → PDF_TYPO B-RS T-5), 并修正它们的 basis.
4. **K2 直接命中复验** 改为独立取靶 (不信 hit_file) 并检查词边界. 把 §5.3 的 kbcopy2 变异加进 `t3_mutation.sh`, 要求结果为 RED.
5. **K11** 短 CODE_LITERAL (`*.xpt`) 加个数核对: 同节同文本的原子数 ≤ 目标文件中按词边界计的出现次数. 6 组要逐条复核.
6. **主控裁定 (K7)**: 依据来自 CONDITIONAL 批 (B-PCPP/B-CP/B-LB) registry 的 8 条 PDF_TYPO, 是否与 C3 同样处理.

修完后, 预计计数变化: EXACT −5 (E1、E2), EQUIV ±1, IE +4, PDF_TYPO +3, ATOM_ERR −2. 残留 46 不变, G-TB3 mapped 口径基本不变.

## 7. 审计脚本与产物 (`work/scratch/t3_audit/`, gitignored)

- 脚本: `a1_diff.py` `a2_props.py` `a3_sample.py` `a4_dossier.py` `a5_target.py` `a6_boundary.py` `a7_tn_ref.py` `a8_g6.py` `a9_rowpdf.py` `mutation_copy.sh`
- 产物: `sample.json` `g6_sample.json` `props.json` `residual_indep.json` `reverse_trace.json` `direct_hit.json`, 以及 `*.log`

---

## §attempt 2 复审 (2026-11-26, `oh-my-claudecode:verifier`, 只读)

> 对象: `t3_recompute.md` §attempt 2. 审计时 ledger md5 = `67931321905eeef1eeef7f212555122f` (writer 报告值一致); 真 KB 全部 .md 拼接 md5 = `b3a040150c53a4256ea0dde645bd7d07`, 审计前后不变.
> 新增的审计脚本放在 `work/scratch/t3_audit/` 下: `b1_diff.py` `b2b_indep_hits.py` `b3_anchor_cat.py` `b4_sample.py` `b5_dossier.py` `b6_exact_reg.py` `mutation_a2.sh` (另有 `kbcopy2/3`、`a2/`、`*.log`).

### A2-0 结论

**FAIL.**
- 改动层抽样 47 条 (K3 15 + C7 10 + K1 12 + 旧层 10), 其中 **1 条终态不成立**: `ig34_p0228_a009`.
- 全量性质扫描又找出 **2 条同类错误**: `ig34_p0205_a005`、`ig34_p0247_a020`.

这 3 条都是同一个规则缺口 (K3b), 性质与 attempt 1 的 `p0206_a009` 相同: KB 有意偏离 PDF 且已登记, ledger 却标 EXACT, 这处偏离就进不了 T4 的 PDF_TYPO 用户 ack 清单.

attempt 1 的其余必改项都已落地, 计数、变异测试、live docs 都能复现.

### A2-1 attempt 1 必改项是否落地

| 项 | 核法 | 结果 |
|---|---|---|
| K1 取靶 + 词边界 + 节锚 | 读 `t3_common.valid_hits` / `anchor_ok`; 复查 E1/E2/E3; 重跑 `a6_boundary.py` | 已落地. E1 `p0153_a0019` → EQUIVALENT; E2 `p0294_a017/a018/a020`、`p0295_a020` → IE; E3 四条 `ec.xpt` → EX/examples.md 7 处. 词边界剩 4 条, 都是 `¹In this column` 前面的 "1", 属合法例外. 残留问题见 A2-4 |
| K2 复验独立取靶 | 我的 kbcopy2 (删 CE `[ ] Surgery`、改名 EX/EC `ec.xpt`、删 NV/spec `### VISITNUM`) 跑新版 `t3_direct_hit.py --kb-root kbcopy2` | **RED**: tb_exact_miss 4, anchor_lost 3. 新拷贝 kbcopy3 和真 KB 都是 **GREEN** (TB 1018 / stock 1767 / pre_existing 61) |
| writer 新 `t3_mutation.sh` | 复制到 `scratch/t3_audit/a2` 后运行 (`mutation_a2.sh`) | M0 绿 / M1 红 / M2 绿 / M3、M4、M5、M6 红 / M7 绿; 真 KB md5 前后 `b3a04015…`. **可复现** |
| K3 规则 6 读 ref | `p0206_a009` 现为 PDF_TYPO (S-SPC1 CP T-19) ✓. 用 `a7_tn_ref.py` 重扫 attempt 1 列出的 10 条 | 13 条已成 PDF_TYPO. 4 条仍是 EXACT: `p0228_a009` ✗、`p0205_a005` ✗ (见 A2-3); `p0228_a002` (T-5 只补句号, 原子 = PDF 且是 KB 的子串) ✓; `p0016_a019` (B-ch02 T-1 照录) ✓ |
| K4 R1 判定 | `a2_props.py` | ATOM_ERR 159 条都满足 "原子 ∉ PDF 窗" ✓. E4 `p0334_a011` → PDF_TYPO (B-RS T-8), `p0338_a006` → PDF_TYPO (B-RS T-5) ✓ |
| K11 计数 | 同节同文本的短 EXACT 原子数 vs 不同命中行数 | 全部 ≥ n: `ec.xpt` 4/7、`relrec.xpt` 3/7 (都在 EX/examples)、`ce.xpt` 3/3、`da.xpt` 2/3、`dd.xpt` 2/2 ✓ |
| K7 → C7 | 读 `t3_delta_rereview.md` (code-reviewer, 三批 `## B-XX — PASS`, 抽 6 条与 PDF 一致) | 依据成立. 45 条的处理见 A2-3 C7 层 |

### A2-2 独立复算 (`b1_diff.py`, 允许集 = triage ∪ T2S ∪ errata 键 ∪ `t3_attempt2_rules.json` 的 K3_extra)

| 核对项 | 结果 |
|---|---|
| 行数 | pre 12487 / post 12492 (追加 5 行: 原 4 行 + `sv20_p0006_a020`, 都不在 pre 中) |
| 改动行 | 1853 行 + 追加 5 行. 改动字段只有 verdict / matched_by; IE 行另改 category / exclusion_reason / approved_by (496). 每条改动行 phase 都是 TB, verdict 都与原值不同 |
| 未改行 | 逐字节一致 |
| 允许集 | 1905, 与 pdf_atoms 取交后为 **1903** ✓. 改动 id 共 1857 个, 允许集外 **0** |
| 终态计数 | EXACT **1018** (live-hit 1001 + was-IE 17) / EQUIV **92** / IE **496** / ATOM_ERR **159** (S1-R1 157 + C7 2) / PDF_TYPO **81** (S1-R2 33 + writer-Tn 48) / FIG **11**, 与 writer 报告一致 ✓ |
| 残留 | 1 条 (`ig34_p0056_a006`, PARTIAL), 与 `residual.txt` 集合差为 ∅ ✓ |
| diff 文件 | 147 行: K3 扩展 54 / C7 45 / K1 改靶 38 / K1 降级 7 / K3 ref 1 / K4 1 / 规则变更 1, 与报告一致 |
| live docs | `python3 tools/check_links.py 2>&1 \| grep "live docs"` 的输出为 `(live docs: 42)` ✓ |

### A2-3 改动层抽样 (seed 20261126, `b4_sample.py` / `b5_dossier.py`; 每条都对了 PDF 页文本和现 KB 行)

| 层 (全集) | 样本 | 结果 |
|---|---|---|
| K3 PDF_TYPO (23) | p0414_a006 (TD T-2 `restarted.`), p0412_a009 (TD T-1 单句点), p0115_a009 (EX T-4 protocol-specified), p0433_a017 (ch08 T-3 `SQAPFAMH).`), p0119_a011 (EX T-2 `--LNKID.`), p0236_a005 (IS T-3 NON-STUDY-RELATED), p0237_a018 (IS T-5 participating in) | 7/7 ✓. 原子 = PDF, KB = registry 的 kb_value (TD/examples、EX/examples:207/403、ch08、IS/examples:108/153) |
| K3 EXACT (27) | p0363_a004, p0361_a013, p0440_a003, p0363_a009, p0361_a015, p0362_a004 (FA/assumptions; RELSPEC/assumptions:19) | 6 ✓ |
| | **ig34_p0228_a009** | **✗.** 原子和 KB (GF/examples.md:169) 都写 `GFLNKID matches MSLNKID`, PDF p228 写 `GFLINKID`. 这是登记过的 **B-GF T-4** (KB 写正确值), 终态应为 **PDF_TYPO** |
| K3 EQUIV (4) | p0362_a006 | ✓ (FA/assumptions.md:31, 与原子只差句末点; stock 判定, 不是本次 TB 翻转) |
| C7 (45) | p0214_a014 (CP:165 row 7 STIMDX 3.5), p0277_a005/a007/a008/a010/a014 (PC/assumptions.md:93/95/96/98/102, 其中 PPSEQ 5/6/8/13 与 PDF 一致), p0213_a013 (CP:134 MNPMNNP), p0270_a013 (PC/examples:27 `A554134-10`), p0214_a012 (CP:163 row 5 2.6 %), p0247_a021 ATOM_ERR (LB/examples:69 PrThr/1999-06-19) | 10/10 ✓. KB 与 PDF 逐格一致. LOW: 多数原子 verbatim 抽取错得很重 (例如 p0214_a014 的值整体不同), 判 EQUIVALENT 而不是 ATOM_ERR, 口径偏宽, 不判为错 |
| K1 改靶/降级 (45) | p0198_a008 (BS/spec:321), p0112_a025 / p0118_a022 (EX `ec.xpt`), p0294_a017 / p0294_a020 → IE, p0151_a0019 (CE CRF `Yes`), p0154_a0027 (CE:144 `pr.xpt`), p0182_a023 (DA), p0151_a0022 (CE `ce.xpt`), p0258_a028 (MB SUPP 表头), p0155_a0007 (CE:158 relrec), p0354_a026 | 12/12 ✓. 指针问题: `p0354_a026` (TU 的 SUPPTU 表头) 的 hit_file 是 **NV/examples.md:28**, 正确位置 TU/examples.md:68 也有同一行. 内容在, 但 K1 改靶在这里没到位 |
| 旧层 (未改 1715) | p0015_a023, p0214_a002, p0154_a0010, p0013_a011, p0118_a031, p0258_a019 ATOM_ERR (MB:76 `VISIT 1`), p0185_a025 IE, p0120_a011, p0077_a015 ATOM_ERR (DM suppdm 表头 = PDF), p0079_a009 ATOM_ERR (SE `--DTC`) | 10/10 ✓, 没有回退 |

抽样结果: **46/47 成立** → FAIL.

全量扫描 (`b6_exact_reg.py` 及其加宽版: 允许集内 EXACT 中原子 ∉ PDF 窗、且同页 registry 的 kb_value 或 kb_text_span ⊂ 原子, 再人工排除不相关的行) 又找到 2 条同类错误:

| atom | 现终态 | 事实 | 应为 |
|---|---|---|---|
| ig34_p0205_a005 | EXACT (K3 扩展, stock 判定未变) | 原子和 KB 写 `CPCSMRKS`, PDF p205 asm 4 写 `CPSCMRKS` ×3 (**S-SPC1 CP T-16b**) | PDF_TYPO |
| ig34_p0247_a020 | EXACT (TB live-hit) | 原子和 KB 的 Ex3 表头写 `LBSTNRHI`, PDF p247:70 写 `LBSTRNHI` (**B-LB T-1**) | PDF_TYPO |

### A2-4 `t3_common.valid_hits` 审查 + 独立实现对比

**代码审**:
- 逐行 norm 后用空格拼接, 跨行匹配没问题.
- 词边界规则正确; 唯一例外是 `¹In this column`, 合理.
- `anchor_ok` 的规则: "最近的编号标题; 中途遇到同级或更高级的无编号标题就截断管辖".

**弱点**: 以下三种情况 anchor_ok 直接放行, 节锚检查实际为空:
- 原子所在节没有编号 (如 `RELSPEC – Specification`);
- 命中文件与原子来自不同 PDF;
- 命中行上方没有管辖它的编号标题 (domain 文件大多如此).

统计 (`b3_anchor_cat.py`): 1018 条 EXACT 中真正被锚检查约束的只有 **522** 条; 其余 438 条 "无管辖编号标题"、57 条 "原子无节号"、1 条跨 PDF, 共 496 条只受词边界约束.

**独立实现** (`b2b_indep_hits.py`, 不 import t3_*):
- 整文件正则, 含词边界;
- 锚: 最近的编号标题, 遇到同级或更高级的无编号标题即截断. 第一版不截断, 结果在 LB/NV 的 `## XX – …` 节误拒 6 条, 修正后重跑;
- 再与 writer 的 hit_lines 求交.

结果 **1018/1018 一致, 0 分歧.**

对上面 496 条锚为空的 EXACT, 又补做了 "命中文件所属 domain 与原子节名 / triage kb_loc 是否对得上" 的检查:
- 绝大多数是 KB 的正常结构: 章节总述放在首个域文件顶部, 例如 §6.2 → AE/assumptions、§6.4 → FA/assumptions、§6.3.5.1 → LB/assumptions;
- 只有 `p0354_a026` (指到 NV) 和 `p0285_a005` (指到 ch10:319 的 Appendix E 重复段; NV/assumptions:11 也有) 两条指针不准, 内容都在.

结论: 匹配器本身没有发现错判. 两边共用同一个匹配器 (writer 自报的风险) 在这次独立对比中没有暴露问题. 剩下的风险是上述 496 条锚为空.

### A2-5 必改项

1. **K3b (HIGH) — 原子已带正确值时, live-hit 遮盖了 registry 偏离.** `tn_applies` 要求 "PDF 侧值出现在该原子", 但抽取器有时已经把 PDF 笔误改正了, 这时原子 ≠ PDF 而 KB = 原子.
   - 补一条规则, 并在 writeback 中加断言: 原子 ∉ norm_pdf(p-1..p+1)、同批同页 registry 的 kb_value ⊂ 原子、pdf_value 中的特征词 ∉ 原子 → PDF_TYPO (与 attempt 1 `p0198_a012` 走 errata 得 PDF_TYPO 的口径一致).
   - 修正 `ig34_p0228_a009` (B-GF T-4)、`ig34_p0205_a005` (S-SPC1 CP T-16b)、`ig34_p0247_a020` (B-LB T-1), 然后重扫全量.
2. **K1 指针 (LOW)**: `ig34_p0354_a026` → TU/examples.md:68; `ig34_p0285_a005` → NV/assumptions.md:11. 改法: domain 文件同为 tier1 时, 优先选与原子节名或 kb_loc domain 一致的文件.
3. **C5 一致性 (LOW)**: `ig34_p0296_a005` 被降为 IE, 但 NV/spec.md:384 逐字有这句脚注. 原因是 NV/spec.md 不在靶里. 同类的 DD/IE/CV 脚注都是 EXACT; 建议把原子所在 domain 的 spec.md 加入 footnote 类原子的靶. 全量只有这 1 条.
4. **风险登记 (MEDIUM, 不阻断)**: 496 条 EXACT 的节锚检查为空, 写进 T4 风险清单, 或在 T4 人工抽样中加一层.

修完后按 A2-3 的口径, 对 K3b 涉及的层重新抽样即可. 其余层本轮已过.

---

## §attempt 3 复审 (2026-11-26, `oh-my-claudecode:verifier`, 只读)

> 对象: `t3_recompute.md` §attempt 3. ledger md5 = `63cd2d8666c209db18ef8eca5e840418` (与报告一致); 真 KB 拼接 md5 = `b3a04015…`, 前后不变.
> 新增审计脚本 (`work/scratch/t3_audit/`): `c1_diff.py` `c2_regscan.py` `c3_sample.py` `c4_dossier.py`, 以及日志 `mutation_a3.log`.
> 判定口径按主控要求: PDF_TYPO 多标属保守方向, 不算错; 已登记的偏离被标成 EXACT 或 EQUIVALENT, 算错.

### A3-0 结论

**FAIL.** T3 本次写入的层没有问题, 问题出在全量扫描.

- **T3 写入层干净.** 抽样 52 条全部成立 (K3b 15 / C7→ATOM_ERR 12 / K1 14+C5 1 / 旧层 10). 计数、允许集、变异测试、live docs 都复现.
- **全量扫描 (第 4 项) 发现 §5.0 范围内仍有 3 条已登记偏离被标成 EQUIVALENT**, 另有 1 条 EXACT 和 2 条待人工确认. 这些都是 P4a 时代留下的 stock 标签, 不在允许集里, writer 的 K3b 规则没有扫到.
- 修复量小: 把这些原子并入 K3b 允许集, 重跑后核对这几条即可.

### A3-1 attempt 2 必改项是否落地

| 项 | 结果 |
|---|---|
| K3b 三条 | `p0228_a009` 依据 B-GF T-4, `p0205_a005` 依据 S-SPC1 CP T-16b, `p0247_a020` 依据 B-LB T-1, 现均为 **PDF_TYPO**, 命中行就是登记行 ✓ |
| 指针 | `p0354_a026` → TU/examples.md:68 ✓; `p0285_a005` → NV/assumptions.md:11 ✓ |
| C5 | `p0296_a005` 由 IE 改为 EXACT (NV/spec.md:384) ✓ |
| 风险登记 | `work/t3_t4_risk_anchorless.txt` 共 508 行 ✓ |
| 变异测试 | 我的 `mutation_a2.sh`, 与 writer 新版 t3_mutation.sh 改写路径后的版本逐字相同, 复跑结果为 M0 绿 / M1 红 / M2 绿 / M3–M6 红 / M7 绿, 真 KB md5 不变. kbcopy2 上 `t3_direct_hit` 为 RED (tb_exact_miss 4 / anchor_lost 3); 真 KB 上为 GREEN (TB 1016 / stock 1763 / pre_existing 59) ✓ |
| 独立匹配器 | `b2b_indep_hits.py` 与 writer 结果 1016/1016 一致; 词边界失败只剩 4 条, 都是 `¹In` 前的 "1" 例外 ✓ |
| live docs | 42 ✓ |

### A3-2 独立复算 (`c1_diff.py`; 允许集 = attempt 2 + K3b_extra)

| 项 | 结果 |
|---|---|
| 允许集 | 与 pdf_atoms 取交后 **1933** ✓. 改动 id 1888 个 (改写 1884 行 + 追加 5 行), 允许集外 0 |
| 未改行 | 逐字节一致. 每条改动行 phase 都是 TB, verdict 都与原值不同 |
| 计数 | EXACT **1016** / EQUIV **54** / IE **494** / ATOM_ERR **197** (S1-R1 157 + C7 38 + C7-K4 2) / PDF_TYPO **116** (S1-R2 33 + writer-Tn 38 + K3b 45) / FIG **11**, 残留 **1** (`p0056_a006`) ✓ |
| diff | 98 行: C7 38 / K3b 扩展 30 / K3b 改判 15 / K1 14 / C5 1 ✓ |

### A3-3 抽样 (seed 20261126)

| 层 | 样本 | 结果 |
|---|---|---|
| K3b (45 抽 15) | p0336_a005 (B-RS T-1 REPSONSE), p0328_a007 (RS T-6 QS 副本 STRNC), p0085_a019 (SM T-3 hyypoglycemic), p0414_a013 (TD T-4 表头), p0113_a011 (EX T-3 ottles), p0228_a009, p0247_a020, p0205_a005, p0428_a008 (ch08 T-2 GMGRPID, PDF Rows 7-9 句中同错), p0115_a009 (EX T-4), p0304_a012 (OE T-1 IDVARAL), p0267_a006 (MI T-1 MIDRVL), p0224_a013 (GF T-1 inheritabilty), p0142_a014 (AE T-4 表头首格), p0228_a002 (GF T-5 句号) | **15/15 成立.** 每条所在行都有登记偏离, KB 行 = registry 的 kb_value. 后两条是纯标点登记, 按主控口径接受 |
| C7→ATOM_ERR (38 抽 12) | p0277_a004/a009/a011/a012/a014/a015 (PC/assumptions.md:90-103 的 pp 表), p0271_a009/a011 (PC/examples.md:55/57), p0218_a002 (CP:255 表头), p0212_a006 (CP:97), p0247_a022 (LB/examples:70), p0214_a011 (CP:162) | **KB 与 PDF 一致: 12/12** (硬条件). 原子是否真抽错: **12/12 是真抽错, 不是折行假象, 折行假象比例 0/12**. 例如: PPSEQ 被写成行号 (PDF 是 13/14/10/7/9…); pp 表 PPGRPID 列错位; `A554134-19` (PDF -21); p0271_a011 写了两个日期 (PDF 只有 12T08:00); CP 表头 CPGATE/CPGATDEF 重复、`OPCAT`、`CPTRESU`; CPSPID 2 (PDF 3); `PtFtv` (PDF PrThr); p0214_a011 整行数值不同 |
| K1 改命中 (14, 全核) + C5 (1) | p0063_a022 (DM/spec:198), p0133_a013 (AE/asm:8, §6.2 总述), p0281_a034/a049、p0282_a035、p0283_a011/a012 (PC/examples, 14 处 relrec, K11 计数够), p0285_a005, p0354_a026, p0437_a016/17/18 (ch08:349), p0440_a003 (ch08:443), sv20_p0009_a013 (model/01:172); C5 p0296_a005 | 15/15 ✓ |
| 旧层 (抽 10) | p0364_a017, p0425_a014, sv20_p0002_a003 (IE), p0057_a002 (ATOM_ERR), p0185_a022, p0295_a008 (IE), p0195_a011, p0142_a010, p0271_a016, p0187_a006 (IE) | 10/10 ✓, 无回退 |

### A3-4 全量: EXACT / EQUIVALENT 与 registry 登记偏离的交叉扫描

脚本 `c2_regscan.py` 为独立实现, 没有 import t3_*:
- 只取不是 "照录" 的 registry 条目, 去掉中文说明后做 token 差: pd = PDF 侧独有, kd = KB 侧独有;
- 对每个同页或相邻页的 EXACT / EQUIVALENT 原子, 判以下两种情况:
  - (i) 原子带 kd, 且 PDF 窗里没有 kd: 抽取器已经改正, 实际是 KB = 原子 ≠ PDF;
  - (ii) 原子带 pd, 且登记的 KB 文件里已经没有 pd: 原子 = PDF, KB 有意改了.

| 类别 | 结果 |
|---|---|
| **TB 写入的 EXACT / EQUIV** | 4 个候选, 人工核过都是噪声 (`MBREFID` 在 MB 原子中本就正确; B-MS T-3 只涉及 suppms; "that" 是 B-TI T-1 的停用词): **0 条真问题** ✓. writer 的 K3b 断言在 TB 层成立 |
| **stock 标签, 在 §5.0 范围内, 不在允许集中** | **✗ 3 条已确认.** 都是登记偏离被标成 EQUIVALENT (P4a 标签, T2 修正之后没有回写): `ig34_p0018_a012`: 原子 = PDF `BESDTC`, KB ch03:37 为 `BESTDTC` (**B-ch03 T-1**); `ig34_p0018_a036`: 原子 = PDF `TESTCD`, KB ch03:49 为 `FTTESTCD` (**B-ch03 T-2**); `ig34_p0213_a009`: 原子 = PDF `MonoSub`, KB CP:130 为 `Mono Sub` (**B-CP T-6**). 这三条登记都不在 `K3b_unusable_registry` 中, 说明是 writer 的触及规则漏了 |
| stock, §5.0 内, 待人工确认 | `ig34_p0068_a010` (B-DM T-2 ISLANDER[S]) 和 `ig34_p0142_a015` (B-AE T-1 2018-04-26): 原子与 KB 行差异很大, 整行像是抽错了, 需要人工判断是 ATOM_ERR 还是 PDF_TYPO; 现为 EQUIVALENT |
| stock EXACT, §5.0 内 | `ig34_p0132_a014`: 原子 = PDF `SUENTTP`, KB SU/examples:19 已改为 `SUENTPT` (**B-SU T-1**), 原子在全 KB 中逐字不命中. 已列在 direct_hit 的 pre_existing 59 中, 但它不是"从未有指纹", 而是登记偏离造成的不命中, 应改为 PDF_TYPO |
| stock, §5.0 范围外 | `p0082_a025` (S-SPREL SE T-1 BIRTHDTC, EXACT), `p0342_a006/a007` (B-SC T-1 日期, EQUIV). 只记录, 交 T4 |

### A3-5 必改项

1. 把 A3-4 的 §5.0 内 stock 原子并入 K3b 允许集: `p0018_a012`、`p0018_a036`、`p0213_a009`、`p0132_a014`, 外加人工确认后的 `p0068_a010`、`p0142_a015`. 重跑后这几条应为 PDF_TYPO, 或经人工判为 ATOM_ERR.
2. 找出 K3b 触及规则为什么漏了这些原子. 推测: (a) 规则的 n-gram 语境要求过严 (`BESDTC` / `TESTCD` 出现在表格单元格里); 或者候选原子只在已有 TB 行或固定页范围内生成. 修好后在 writeback 加一条断言, 覆盖 §5.0 内**全部** EXACT / EQUIVALENT, 而不只是 TB 行. 我的 `c2_regscan.py` 可以作对照, 但它的 token 法有噪声, 需要人工过滤.
3. 复审只需核对上述几条和新断言的输出; 其余层本轮已过, 不必重新抽样.

---

## §attempt 4 复审 (2026-11-26, `oh-my-claudecode:verifier`, 只读, 只复核改动层)

> 对象: `t3_recompute.md` §attempt 4 / §A4.3. ledger md5 = `a8011432d42e1e9db0e3fd775cf28fad` (与报告一致); 真 KB = `b3a04015…` (不变).
> 新增审计产物: `work/scratch/t3_audit/d1_diff.py`、`regscan_a4.txt`、`mutation_a4.log`.

### A4-0 结论

**CONDITIONAL.**
- 终态层面: 6 条改判全部成立; 对 §5.0 内全部 EXACT/EQUIV 做独立 registry 扫描, 真问题为 0; 计数、变异测试、live docs 都复现.
- 唯一的必改项是可复现性: `t3_writeback.py` 硬读 attempt 3 的冻结判定文件, 来决定 21 条范围外原子的 K3b 归属 (见 A4-3).

### A4-1 6 条改判逐条核 (PDF 原页 + 现 KB)

| atom | 现终态 | PDF | KB | 判定 |
|---|---|---|---|---|
| ig34_p0018_a012 | PDF_TYPO | p18:16 BE Keys `BESDTC` | ch03:37 `BESTDTC` (B-ch03 T-1) | ✓ |
| ig34_p0018_a036 | PDF_TYPO | p18:45 FT Keys `TESTCD` | ch03:49 `FTTESTCD` (B-ch03 T-2) | ✓ |
| ig34_p0213_a009 | PDF_TYPO | p213 Ex3 r2 `MonoSub` | CP/examples.md:130 `Mono Sub` (B-CP T-6) | ✓ |
| ig34_p0132_a014 | PDF_TYPO | p132 `SUENTTP` | SU/examples.md:19 `SUENTPT` (B-SU T-1) | ✓ |
| ig34_p0068_a010 (人工) | PDF_TYPO | `ig34_p0068.txt:20-25` row 6: ABC12302002 / 02002 / 2006-02-03 / 2006-04-05 / 2006-02-03 / 2006-04-05 / 2006-01-10 / 2006-04-25 / GONZALEZ, E / 1956-05-05 / 49 YEARS F / …PACIFIC **ISLANDERS** / NOT HISPANIC… / A Drug A A Drug A / USA | DM/examples.md:14 逐格与 PDF 一致, 只有 RACE 写 `…ISLANDER` (B-DM T-2) | ✓ (原子抽错多格, 已在 manual.json 写明) |
| ig34_p0142_a015 (人工) | PDF_TYPO | `ig34_p0142.txt:21-22` row 1: … AESER N … N N N N N N N Y N Y / 2018-04-21 / **2014-04-26** / 5 / 10 | AE/examples.md:81 逐格与 PDF 一致, 只有 AEENDTC 写 `2018-04-26` (B-AE T-1) | ✓ |

另外 4 条只是规则归属从 writer-Tn 改为 K3b (`p0206_a009`、`p0236_a014`、`p0236_a015`、`p0427_a011`), 终态都仍是 PDF_TYPO, 没有影响.

### A4-2 修后 K3b: 独立复跑与漏判方向评估

**独立复跑.** 命令: `python3 -I .work/10_tier_b_repair/work/scratch/t3_audit/c2_regscan.py > …/regscan_a4.txt`, 再按 §5.0 范围过滤.
- 上轮确认的 4 条和待人工的 2 条已全部消失.
- §5.0 内剩下的候选都是我这个 token 法的已知噪声, 逐类核过:
  - B-BE T-2 (`2005-03-20`, p145 BE 行与 p146 BS r1/r2): 登记只涉及 BS r3 的残缺 "5-0"; 其余行在 PDF 里本来就是 2005-03-20, 只是文本层折行把它切开了.
  - B-CP T-5 (`T12:20`, p211 rows 1-5): 登记只涉及 r6; 其余行的值本来就是 T12:20, 同样是折行.
  - B-MS T-3 (`MBREFID`): 登记只涉及 MS supp; MB 原子写的就是正确值.
  - B-TI T-1 (`that`): 停用词.
- 结论: **§5.0 内 EXACT/EQUIV 的真问题为 0** (TB 层和 stock 层都是 0). 这与 writer 扩大后的断言 (命中 0) 一致.

**两项规则改动会不会造成新的漏判:**
1. **特征词免邻词** (规则 a/b): 放宽之后被判为"触及"的原子只会更多, 也就是 PDF_TYPO 多标, 属于主控认可的保守方向, **不会造成漏判**. 规则 (c) 仍要求严格 n-gram, 不影响同行误标的防护.
2. **(a) 的新排除条件** (PDF 侧 token 也不能出现在原子自己的其他 tier1 KB 文件里): 这一条**理论上会造成漏判**. 场景是: 原子 = PDF (带错误 token), 而原子的另一个 tier1 文件因为别的上下文正好也合法地含有这个 token. 这时 (a) 被排除; (c) 又因为原子不再命中 KB 而救不回来.
   - 实测: 我的扫描没有用这条排除, 等于是不带排除条件的对照. 在 §5.0 内, 被这条排除挡掉的只有 B-MS T-3 的 `MBREFID` 类, 那正是本来就该排除的噪声. **没有发现因此漏掉的真偏离**.
   - 建议 (LOW): 在 writeback 中记录被排除的 (原子, 登记) 对, 输出计数, 方便日后复核.

### A4-3 可复现性: 对冻结判定文件的依赖

代码在 `t3_writeback.py:452-456`:
```python
A3_DONE = set(json.load(open(f"{W}/t3_attempt3/t3_writeback_decisions.attempt3.json")))
K3B_OUT = {i: K3B.pop(i) for i in [i for i in K3B if i in T4_ONLY or (not in_scope(i) and i not in ALLOWED and i not in A3_DONE)]}
```

- **实测影响:** K3b_extra 36 条中, 有 **21 条范围外原子**的 PDF_TYPO 只靠 `i in A3_DONE` 保留. 例如 `ig34_p0336_a005`、`p0328_a007`、`p0304_a012`、`p0414_a013`, 以及 TD T-1 那一行的 `p0412_a006/7/8`.
- **判断: 这构成对上轮产物的依赖, 不能从源头复跑.**
  - 文件缺失时脚本直接抛 FileNotFoundError.
  - 这个文件本身是旧版本 `t3_writeback.py` 的输出, 而且目前未纳入 git (`git status` 显示 `?? work/t3_attempt3/`).
  - 一旦 attempt 3 重跑或被清理, 这 21 条的终态会悄悄改变.
  - 这不是同一次运行内的自循环, 但属于跨版本的输出回读, 与 "ledger 只由源数据 + 规则生成" 的要求冲突.
- 另外, `T4_ONLY` 把 3 个 atom id 硬编码在脚本里, 也应移到数据文件中.

### A4-4 复跑与复算

| 项 | 命令 | 结果 |
|---|---|---|
| 独立复算 | `python3 -I .work/10_tier_b_repair/work/scratch/t3_audit/d1_diff.py` | 允许集 **1939**; 改动 id 1894 个 (改写 1890 行 + 追加 5 行), 允许集外 0; 未改行逐字节一致; EXACT **1016** / EQUIV **54** / IE **494** / ATOM_ERR **197** / PDF_TYPO **122** (K3b 55 + S1-R2 33 + writer-Tn 34) / FIG **11**; 残留 **1**, 与 residual.txt 一致 ✓ |
| 变异测试 | `bash …/scratch/t3_audit/mutation_a2.sh` (与 writer 版本改路径后逐字相同) | M0 绿 / M1 红 / M2 绿 / M3–M6 红 / M7 绿; 真 KB 不变 ✓. kbcopy2 上 direct_hit 为 RED ✓ |
| 直接命中 | `python3 -I .work/10_tier_b_repair/scripts/t3/t3_direct_hit.py` | GREEN: TB 1016 / stock 1762 / pre_existing 58 ✓ |
| 独立匹配器 | `b2b_indep_hits.py` | 1016/1016 一致 ✓ |
| live docs | `python3 tools/check_links.py 2>&1 \| grep "live docs"` | 42 ✓ |

### A4-5 必改项

1. **(必改) 去掉对冻结判定文件的依赖.**
   - 把 21 条范围外的 K3b 原子和 `T4_ONLY` 的 3 条, 固化为一份显式清单 (例如 `work/t3_k3b_out_of_scope_keep.json`).
   - 每条写明 atom_id、registry id、判据 (a/b/c/c′)、PDF 行和 KB 行; `t3_writeback.py` 只读这份清单.
   - 删掉 `A3_DONE` 后从源头重跑, 断言 ledger md5 仍为 `a8011432…`. 复核时只需对一下 md5 和这份清单.
2. (LOW) 记录 (a) 排除条件挡掉的 (原子, 登记) 对并输出计数.

第 1 项落实并复核通过后可转 PASS.

---

## §attempt 4 终审 (2026-11-26, `oh-my-claudecode:verifier`)

> 范围: 只复核 §attempt 4 复审 A4-5 的必改项 1, 即可复现性 (对应 `t3_recompute.md` §A4.5).
> 本节为主控授权的源头复跑, 运行期间改写了 `work/` 下的 T3 产物: 先备份到 `work/scratch/t3_audit/a4final_backup/`, 跑完逐个比对 md5 全部一致; `t3_attempt1/2/3` 已原样放回.

**结论: PASS.** ledger 可以从源头复跑出同一结果, 不再依赖上一轮产物.

### 1. grep: 对上轮产物的读取与硬编码 id

| 检查 | 命令 | 结果 |
|---|---|---|
| 读取 `work/t3_attempt*/` | `grep -nE "t3_attempt\|attempt[0-9]\|_DONE\|T4_ONLY"`, 范围: `t3_writeback / t3_errata_build / t3_direct_hit / t3_common / t3_t2s_atoms / t3_report / t3_recompute` | **0 处** ✓. 只有 `t3_attempt_diff.py` (diff 工具, 不参与判定) 和 `t3_build_keep.py` (一次性生成器) 引用 |
| writeback 读入的文件 | `grep -o 'open(f"{W}/…"'` | 只读 pdf_pages、`t3_c1_manual.json`、`t3_errata.json`、`t3_k3b_manual.json`、`t3_k3b_out_of_scope_keep.json`、`triage_merged.json` 和各 lj 源. `t3_rules.json` 只写不读, 不存在自回读 ✓ |
| 硬编码 id | `grep -nE '"(ig34\|sv20)_p…"'` | `A3_DONE` / `T4_ONLY` 已删除 ✓. 剩余 3 处都是带证据的常量, 前几轮已审, 不属于回读上轮输出: writeback:201-202 (C7-K4 两条, 指向 `t3_delta_rereview.md` 行号); errata_build:101-161 (`p0198_a012` R2 绑定 B-BS T-2; `p0240_a004` / `p0245_a007` remap). `s0_classify.py` 的分类表是 S0 定性数据. LOW: 可以视需要迁到数据文件 |

### 2. 隐藏 attempt 目录后从源头复跑

我自己执行 (不使用 writer 的 hidden 路径):
```bash
T=.work/10_tier_b_repair; S=$T/work/scratch/t3; A=$T/work/scratch/t3_audit
mv $T/work/t3_attempt1 $T/work/t3_attempt2 $T/work/t3_attempt3 $A/hidden_attempts/
# 以下按 §A4.5 的顺序: fp_match (in-scope) → kb_t2base → fp_match scope=all ×2 → s0_classify → t3_t2s_atoms → t3_errata_build → t3_writeback --ts 2026-11-26T12:00:00Z
mv $A/hidden_attempts/t3_attempt* $T/work/
```

输出:
- fp 回归 72 / 82;
- s0_classify `BAD []`, R1 32 / R2 23 / R3 28, R4 = 0;
- t2s 解析失败的 ref 片段 0;
- writeback: `K3b keep list: 24 entries, failing pdf/kb re-check: [] | rule (a) own-file exclusions: 6`, `extended assertion … hits = 0`, `ASSERT: OK`.

复跑前后 md5 比对 (备份见 `a4final_backup/md5_{before,after}.txt`, `diff` 无差异):

| 文件 | md5 |
|---|---|
| `coverage_ledger.wc.jsonl` | **`a8011432d42e1e9db0e3fd775cf28fad`** ✓ (= 要求值) |
| `t3_errata.json` | `1d27f0fa…` ✓ |
| `t3_t2s_atoms.jsonl` | `33ef2fe0…` ✓ |
| `t3_fp_expected_regressions.jsonl` | `78b22b1c…` ✓ |
| `t3_rules.json` | `2d93678f…` ✓ |
| `t3_writeback_decisions.json` | `60d61a77…` ✓ |

### 3. keep 清单抽 5 条 (seed 20261126)

| atom | action / 登记 | PDF 行 | KB 行 | 判定 |
|---|---|---|---|---|
| ig34_p0377_a021 | keep_k3b / B-SR T-3 (a) | p377:50 `reactogencity` | SR/assumptions.md:15 `reactogenicity` | ✓ |
| ig34_p0082_a025 | t4_only / S-SPREL SE T-1 | p82:36 `BIRTHDTC` | SE/examples.md:44 `BRTHDTC` | ✓ |
| ig34_p0414_a013 | keep_k3b / S-TDM TD T-4 (b) | p414:29 `TDTGPAI` | TD/examples.md:167 `TDTGTPAI` | ✓ |
| ig34_p0412_a008 | keep_k3b / S-TDM TD T-1 (c′) | 清单写 p412:1, token `assessments` | TD/examples.md:40 (KB 为单句点) | 偏离属实: 实际偏离行是 **p412:17** `assessments..`. 清单的 PDF 定位指错了行, 运行时断言只查 token 是否在该行, 通用词 `assessments` 在第 1 行也能通过. 终态属主控认可的保守多标 → ✓ (指针 LOW) |
| ig34_p0342_a007 | t4_only / B-SC T-1 | 清单写 p342:9 (表头), token `scdtc` | SC/examples.md:35 `2017-04-01` | 偏离属实: 实际错值在 **p342:16/21/23** `20-17-` / `06-10` (折行). 定位用的是表头词, 证据偏弱; 该条只列入清单、不改终态 → ✓ (指针 LOW) |

### 4. 遗留 (LOW, 不阻断)

- keep 清单里 c′ 类和 t4_only 类的 PDF 定位 token 太通用 (`assessments`、`scdtc`), 运行时断言约束不住. 建议改成指向登记偏离值本身的行 (p412:17、p342:16/21/23), 并要求 token 是 PDF 侧的差异值.
- 硬编码的证据常量 (C7-K4 两条、errata 三处) 可以视需要迁到数据文件.
