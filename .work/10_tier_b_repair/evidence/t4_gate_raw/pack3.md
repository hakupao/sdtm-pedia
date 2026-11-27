<!-- 原样誊录: feature-dev:code-reviewer (opus) 对 `work/t4/gate_pack_3.md` 的回复, 2026-11-27. 主控未改动内容 (仅把绝对路径缩成仓库相对路径). -->

# T4.1 总闸独立审查：样本包 3（第 43-63 条，共 21 条）

**结论：21 条全部 HOLDS，没有 NOT_HOLD 或 UNVERIFIABLE。** 每条的 PDF 原文我都自己读了页文本层，KB 行也是自己 Grep 定位的，没有只信样本包里的指针。PDF 页 76 另外看了渲染页。本次只读，没有改任何文件。

文件路径都相对于仓库根。PDF 页文本在 `.work/10_tier_b_repair/work/pdf_pages/` 下，表中简写为 `ig34_pNNNN` 或 `sv20_pNNNN`。

## 1. 逐条判定

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF 文件:行 / 渲染页; KB 文件:行) | 原因 / 备注 |
|---|---|---|---|---|---|---|
| 43 | ig34_p0236_a008 | VALUE_DIFF | ATOM_ERR | HOLDS | ig34_p0236:21 表头含 ISSCAT（ISCAT 与 ISORRES 之间）；KB `knowledge_base/domains/IS/examples.md:113` 22 列表头含 ISSCAT | 抽取的原子文本漏了 ISSCAT，KB 按 PDF 写对了 |
| 44 | ig34_p0236_a010 | VALUE_DIFF | EXACT | HOLDS | ig34_p0236:25-27；KB `IS/examples.md:116` | 逐格一致。ISSEQ=2 与第 4 行重复，这是 PDF 原样，已按登记 B-IS U-1 照录 |
| 45 | ig34_p0236_a012 | VALUE_DIFF | EXACT | HOLDS | ig34_p0236:31-33；KB `IS/examples.md:118` | 逐格一致 |
| 46 | ig34_p0247_a022 | VALUE_DIFF | ATOM_ERR | HOLDS | ig34_p0247:73-74，LBRESTYP 为 `PrThr`；KB `knowledge_base/domains/LB/examples.md:70`，`PrThr`，29 列与 PDF 表头对齐 | 原子文本写成 `PtFtv`，与 PDF 不符；KB 正确。样本包指针 37-39 偏了，实际在第 70 行 |
| 47 | ig34_p0353_a016 | VALUE_DIFF | EXACT | HOLDS | ig34_p0353:31-32；KB `knowledge_base/domains/TU/examples.md:25` | 逐格一致 |
| 48 | ig34_p0355_a014 | VALUE_DIFF | PDF_TYPO | HOLDS | ig34_p0355:25-27，Row/TRSEQ 从 11 直接跳到 13；ig34_p0354:41-42 叙述写 "Rows 9-21 / Rows 22-27"；KB `knowledge_base/domains/TR/examples.md:30` 为 12，全表 1-27 连续；登记 `t2_pdf_typo_registry.jsonl:182` (B-TR T-1)，处理方式为 "KB 写正确值" | PDF 确实跳号；KB 现状与登记一致，其余值逐格相同 |
| 49 | ig34_p0121_a016 | IE | INTENTIONAL_EXCLUDE (SPEC_TABLE_ROW) | HOLDS | ig34_p0121:22；KB `knowledge_base/domains/ML/spec.md:86-93` | 标签、类型、角色、核心性、注释全部一致；CT 栏 (NY) 后加了 C66742（S-CT 批次补的码），信息等价 |
| 50 | ig34_p0135_a001 | IE | INTENTIONAL_EXCLUDE (SPEC_TABLE_HEADER) | HOLDS | ig34_p0135:1-3 是续页重复的规格表表头；`knowledge_base/domains/AE/spec.md` 每个变量都用 Label/Type/Controlled Terms/Role/Core/CDISC Notes 字段承载这些列（如 :203-210 AEBDSYCD） | 依据见本节表后第 1 点 |
| 51 | ig34_p0148_a028 | IE | INTENTIONAL_EXCLUDE (SPEC_TABLE_ROW) | HOLDS | ig34_p0148:39-41；KB `knowledge_base/domains/CE/spec.md:77-84` | 全字段一致 |
| 52 | ig34_p0149_a018 | IE | INTENTIONAL_EXCLUDE (SPEC_TABLE_ROW) | HOLDS | ig34_p0149:44-48，CT 栏为 `(STENRF)`；KB `CE/spec.md:248-255`，`(STENRF) C66728`，注释一致（KB 里 "Demographics)." 后多一个空格，属允许的空白差） | 原子文本把 CT 写成 `(STNREF)`，抽错了；但这不影响 IE 成立 |
| 53 | ig34_p0168_a0001 | IE | INTENTIONAL_EXCLUDE (SPEC_TABLE_ROW) | HOLDS | ig34_p0168:3-4；KB `knowledge_base/domains/HO/spec.md:23-30` | 全字段一致 |
| 54 | ig34_p0193_a006 | IE | INTENTIONAL_EXCLUDE (SPEC_TABLE_HEADER) | HOLDS | ig34_p0193:6-8 是规格表表头；`knowledge_base/domains/IE/spec.md` 用相同字段结构承载（如 :5-12 STUDYID） | 同第 50 条 |
| 55 | ig34_p0243_a011 | IE | INTENTIONAL_EXCLUDE (SPEC_TABLE_ROW) | HOLDS | ig34_p0243:35-39；KB `knowledge_base/domains/LB/spec.md:257-264` | 全字段一致，CT 栏加了 C78736 |
| 56 | ig34_p0264_a005 | IE | INTENTIONAL_EXCLUDE (SPEC_TABLE_ROW) | HOLDS | ig34_p0264:6；KB `knowledge_base/domains/MI/spec.md:5-12` | 全字段一致 |
| 57 | ig34_p0264_a021 | IE | INTENTIONAL_EXCLUDE (SPEC_TABLE_ROW) | HOLDS | ig34_p0264:41-42；KB `MI/spec.md:149-156` | 全字段一致，CT 栏加了 C71620 |
| 58 | ig34_p0265_a015 | IE | INTENTIONAL_EXCLUDE (SPEC_TABLE_ROW) | HOLDS | ig34_p0265:30-31；KB `MI/spec.md:320-327` | 全字段一致 |
| 59 | ig34_p0309_a007 | IE | INTENTIONAL_EXCLUDE (SPEC_TABLE_ROW) | HOLDS | ig34_p0309:16-17；KB `knowledge_base/domains/RE/spec.md:239-246` | 全字段一致，CT 栏加了 C99073 |
| 60 | sv20_p0047_a003 | IE | INTENTIONAL_EXCLUDE (VERSION_MISMATCH) | HOLDS | sv20_p0047:8-10；KB `knowledge_base/model/03_special_purpose_domains.md:155`：`1 \| STUDYID \| Study Identifier \| Char \| Identifier`；规则见 `t1_r1_r4_resolution.md:8` (R1-row) | 符合 R1-row：model/ 里有 5 列精简版（#/name/label/type/role 与 PDF 一致），缺 C-code 和 Definition 属本类别。样本包指针 :133 指到的是 SE 表 ETCD 行，实际在 :155 |
| 61 | ig34_p0042_a004 | CONTROL | EQUIVALENT | HOLDS | ig34_p0042:3-5；KB `knowledge_base/chapters/ch04_general_assumptions.md:883` | 该句在 KB 里逐字一致，只是 KB 把 PDF 同一段拆成了 877/879/881/883 几段。标为 EXACT 也成立 |
| 62 | ig34_p0076_a005 | CONTROL | EQUIVALENT | HOLDS | 渲染页 76 + ig34_p0076:22-29；KB `knowledge_base/domains/DM/examples.md:334`，14 列，checkbox 落在 List Style 列 | KB 与 PDF 逐字逐列一致，标为 EXACT 也成立。原子文本自身有误（"with race being asked" 重复一遍，只有 12 格），但 KB 正确 |
| 63 | ig34_p0141_a021 | CONTROL | EQUIVALENT | HOLDS | ig34_p0141:35-37，按列位推算 2005-10-29 在 AEDTC 列、19 在 AEDY 列；KB `knowledge_base/domains/AE/examples.md:46` | KB 逐字一致，标为 EXACT 也成立 |

**表后说明**

1. **第 50、54 条用的判定口径：** brief 指定的 `t1_ie_final.md` 只有 SPEC_TABLE_HEADER 的清单，没有类别定义；`t1_ie_candidates.md` 和 `t1_r1_r4_resolution.md` 里我也没找到。所以我自己定了一个口径：PDF 上确有该规格表表头，且对应 `spec.md` 用逐变量字段承载了每一列。两条都满足，判 HOLDS。建议补一条正式定义。
2. **第 61-63 条的标签：** 3 条 CONTROL 全是同一情况，KB 其实逐字承载，库存标签 EQUIVALENT 低报了覆盖程度。没有丢信息也没有改义，所以仍判 HOLDS。要不要统一改成 EXACT，请主控或用户裁定。

## 2. 计数

- HOLDS: 21
- NOT_HOLD: 0
- UNVERIFIABLE: 0

## 3. 样本外发现的 KB 内容问题

**无。**

顺带核对过的几处，都与登记一致，或者 KB 忠于 PDF：

- **已登记、KB 现状与登记相符：**
  - B-IS T-1/T-2：PDF p236 第 6、7 行 STUDYID 写成 RSC1230，KB 写 RSV1230。
  - B-IS T-3：PDF p236 叙述写 "NON-STUDY RELATED"，KB 写 "NON-STUDY-RELATED"。
  - B-LB T-1：PDF p247 表头写 LBSTRNHI，KB `LB/examples.md:67` 写 LBSTNRHI。
  - B-TU T-1：PDF p353 写 aorta-iliac，KB `TU/examples.md:13` 写 aorto-iliac。
- **PDF 自身前后不一致，未登记，KB 照录：** PDF p354:37-38 叙述写 TRTEST = "Lymph Nodes State"，而 p355 表内 TRTEST 是 "Lymph Node State"。KB `TR/examples.md:7` 与 `:34` 分别照录，不算 KB 错误；如需统一处理，可考虑补进 `t2_pdf_typo_registry.jsonl`。

**样本包和原子层的问题（不是 KB 内容问题）：**

- **指针偏移：** 第 46 条实际在 `LB/examples.md:70`（包里写 37-39），第 60 条实际在 `model/03_special_purpose_domains.md:155`（包里写 133）；第 50、54 条的指针来自模糊定位，指到的是无关变量行。
- **原子文本抽错，但终态不受影响：** 第 52 条 `(STNREF)`，应为 `(STENRF)`；第 62 条短语重复、少列。
