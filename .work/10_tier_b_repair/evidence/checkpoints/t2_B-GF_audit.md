# T2 B-GF auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

- 范围: `git diff 3c716a7 -- knowledge_base/domains/GF/` (assumptions.md + examples.md); md5 现值 assumptions `4dc691a9138d65f67ee0bc7b06138a3a` / examples `177549cde963a5bef080b00317476c66` = writer 续 2 终值.
- 先独立判 (读 PDF 原页 + KB), 判完才对照 writer/reviewer 报告.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-GF_auditor/` (sample.json, prose_check.txt, cells.txt, 渲染裁切 ex1L/ex1M/ex2/ex4/w225 png)

### 抽样
- 命令: t2_auditor_v1.0.md §抽样 脚本原样 (b="B-GF", seed=20261126) → `$S/sample.json`
- 结果: **C=1, P=20, N=10**; C 1 + P−C 9.
- 复核: `prose_check.py` (原子 verbatim 归一后子串查 GF 两文件) + 人工读 `work/pdf_pages/ig34_p02{20,25,27}.txt` + p225 110dpi 渲染图.

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0227_a021 | p227:37-39 Ex5 GFTEST "Single Nucleotide Variation" 用于 SNP… 5 句 | examples.md:151 | 否 | 是 | 是 (Ex5, Findings 段后, NHOID 段前 = PDF 顺序) | C 原子 (REAL_GAP), 逐字命中 |
| 2 | ig34_p0227_a014 | p227:22-24 Ex5 引言 "3 datasets (MB, MS + GF)…" | examples.md:137 | 否 | 是 | 是 | 逐字 |
| 3 | ig34_p0220_a025 | p220:67 Description "GF domain is used for findings from … nucleic acids…" | assumptions.md:9 (另 :19 assumption 1 内) | 否 | 是 | 是 | 逐字 |
| 4 | ig34_p0225_a001 | p225:1 Ex1 Row 8 copy number ratio | examples.md:21 | 否 | 是 | 是 | 逐字 |
| 5 | ig34_p0225_a015 | p225:50 Ex2 Row 3 homozygous for reference | examples.md:58 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0225_a006 | p225:38 "The DI example shows the device type and manufacturer … ACME GenePanel 500." | examples.md:41 | 否 | 是 | 是 (Ex1 DI 段后, di.xpt 前) | 原子文本 "DI domain example" 与 PDF 不符 = ATOM_ERR; layout 文本与 110dpi 渲染图均为 "DI example", KB 逐字 = PDF |
| 7 | ig34_p0225_a019 | p225:65-66 Ex3 引言 ACTB/GAPDH… "respresented" | examples.md:70 | 否 | 是 | 是 | 仅 PDF 拼写错 respresented→represented (T-3, 按 PDF_TYPO 规则登记); 原子另含抽取错 "rerspresented" |
| 8 | ig34_p0225_a002 | p225:2 Ex1 Row 9 copy number interpretation | examples.md:23 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0227_a004 | p227:5 Ex4 Rows 2-6 MSI detected per subregion | examples.md:122 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0227_a002 | p227:2-3 Ex4 引言 MSI / capillary electrophoresis | examples.md:118 | 否 | 是 | 是 | 逐字 (D-6 删除副本的保留处) |

- **独有丢失 0 / 10; 忠实度错误 0 / 10.**

### 表格 10 格复核 (重建 Ex1/Ex2/Ex4 gf.xpt vs 渲染 PDF; 格由 seed 20261126 从三表全部非 Row 格随机抽)
命令: `$S/cells.txt` 生成脚本 (random.Random(20261126).sample); 渲染 `pdftoppm -r 400 -x/-y/-W/-H` (p225 Ex1 左/中段, p225 Ex2 300dpi, p227 Ex4 250dpi); Ex4 r4 另对 layout 文本 p227:14.

| # | 表 KB 行 | Row / 列 | KB | PDF 渲染 | 一致 |
|---|---|---|---|---|---|
| 1 | Ex1 :36 | 8 / GFSYMTYP | GENE WITH PROTEIN PRODUCT | GENE WITH PROTEIN PRODUCT | 是 |
| 2 | Ex1 :36 | 8 / SPDEVID | ACME GenePanel 500 | ACME GenePanel 500 | 是 |
| 3 | Ex1 :29 | 1 / GFGENREF | GRCh37.75 | GRCh37.75 | 是 |
| 4 | Ex2 :65 | 2 / GFSEQ | 2 | 2 | 是 |
| 5 | Ex2 :65 | 2 / GFDY | -3 | -3 | 是 |
| 6 | Ex1 :30 | 2 / GFTSTDTL | PREDICTED CODING SEQUENCE CHANGE | PREDICTED CODING SEQUENCE CHANGE | 是 |
| 7 | Ex4 :131 | 4 / GFSEQ | 4 | 4 (layout p227:14, MONO-27 行) | 是 |
| 8 | Ex1 :33 | 5 / GFSEQID | ENST00000278616.4 | ENST00000278616.4 | 是 |
| 9 | Ex1 :34 | 6 / GFREFID | TRF001338 | TRF001338 | 是 |
| 10 | Ex2 :65 | 2 / GFSTREFC | G/G | G/G (GFORRES G/T, GFORREF G/G, GFSTRESC G/T, GFSTREFC G/G) | 是 |

- 顺带目视: Ex1 表头 33 列顺序、GFXFN 路径 `…LCNL-361/…`、GFNAM ACME SEQUENCING LLC、Ex4 r1 GFTSTDTL MICROSATELLITE INSTABILITY OVERALL STATUS / GFXFN msi_abc_gf.csv / GFRUNID MSI-010418 与渲染一致. 10/10 一致.

### D-5..D-8 删除核 + 锚点
- D-5 assumptions 标题 "## GF – Example 4 (p227)": PDF p220-224 assumptions 区无此节 (p224:20 起为 "GF – Examples"), KB 自写 → 删无损.
- D-6 Ex4 引言: 保留于 examples.md:118 (样本 #10 逐字核过) → 无损.
- D-7 NHOID Note 段: p227:40-41, 保留于 examples.md:153 逐字 → 无损.
- D-8 脚注旧句 "codelists will be available … cancer.gov": `grep -l cancer.gov pdf_pages/ig34_p022*.txt` 无命中; 新句 = p223:27 逐字 → 删的是非 PDF 内容, 无损.
- 交叉引用 assumptions.md:43 → `examples.md#example-4` / `#example-5`: 同目录 examples.md:116 `## Example 4`、:135 `## Example 5` 存在, slug 可解析.
- assumption 9 `--ORNRHI` (p224:18 PDF "ORNRHI,--STNRLO", T-6 改正) 合 PDF_TYPO 规则 (同列表 21 项全带 "--").

### G-TB8
- trace: writer (`oh-my-claudecode:executor`) subagent_done ×3 (02:17:23Z / 02:19:10Z / 02:25:22Z 续 2 = 最后 KB 改动); reviewer (`oh-my-claudecode:code-reviewer`) CONDITIONAL 02:24:21Z → **续签字 PASS 02:26:13Z, 晚于 writer 最后改动**. 两文件 mtime 2026-11-26T11:24:53+0900 (=02:24:53Z) ≤ reviewer PASS; 现 md5 = writer 续 2 记录值, reviewer 之后无改动.
- `agent: main` 记录 6 条, 无一涉及 GF / KB 写入. → G-TB8 通过.

### 结论
- 独有丢失 0, 忠实度错误 0, 表格 10 格 0 差异, D-5..D-8 无 PDF 内容丢失, 锚点可解析, G-TB8 通过 → **B-GF PASS**.
- 观察 (非阻断): U-1 (Ex2 GFMETHOD REAL_TIME 照录)、U-2 (MB r1 MBREFID INFLU0101 照录)、T-2 (MBTEST Identification) 待 T4 用户裁定, 本审未改判.
