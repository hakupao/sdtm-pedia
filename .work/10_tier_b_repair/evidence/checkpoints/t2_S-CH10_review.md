# T2S S-CH10 reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (无 CRITICAL/HIGH/MEDIUM; 3 条 LOW 观察, 不阻断)

- 对象: `git diff HEAD -- knowledge_base/chapters/ch10_appendices.md` (329 → 442 行; md5 after `9795f2f571f6240abaf14cae10c4ca7f` = writer 报告).
- 授权范围: `git diff HEAD --stat -- knowledge_base/` 共 4 文件; 本批只有 ch10 (∈ kb_files, narrow_files 空); ch04 / ch08 / model/02 属并行批 S-CH4 / S-CH8 / S-MOD2, 不计.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH10_reviewer/`
  自写脚本 (不复用 writer 的): `tabA.py` (App A: layout 按表头 Company 列 x 位置分列, 多行格合并, 逐行逐格对 KB), `tabB.py` (App B: layout 2+ 空格分列 + 续行合并), `tabD.py` (App D: 3 页 layout 分列), `seqE.py` (KB 段落/表格去 Markdown 后与 `pdftotext -raw` 页文本做**有序**词级 difflib, 输出全部非 equal opcode; 比 writer 的子串核更强 — 同时核顺序与 bullet 数). 渲染 110dpi p444-461 共 18 页, 看过 444/445/448/450/453/454/455/456/457/458/459 (其余页由 layout 有序比对覆盖, 无差异).

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH10_reviewer
P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
for p in $(seq 443 461); do pdftotext -layout -f $p -l $p "$P" $S/L$p.txt; pdftotext -raw -f $p -l $p "$P" $S/R$p.txt; done; pdftoppm -f 444 -l 461 -r 110 -png "$P" $S/r
python3 -I $S/tabA.py $S A          # 74 74, DIFF 0
python3 -I $S/tabB.py $S            # 40 40, DIFF 0
python3 -I $S/tabD.py $S            # 106 106, DIFF 0
python3 -I $S/seqE.py $S 333 418 453 460 "In addition to the general"   # 变更表 3 张: 非 equal 仅 页眉重复 ×6 / 折行连字符 ×6 / T-1 / T-2 / p459 空 bullet ×10
python3 -I $S/seqE.py $S 288 333 452 453 "Appendix E"    # 仅 KB 导航标题 2 (General Changes Throughout / Key Section-by-Section Changes)
python3 -I $S/seqE.py $S 145 175 448 449 "Appendix C:"   # 仅 URL/8-character 折行连字符 2 + 导航标题
python3 -I $S/seqE.py $S 7 10 444 444 "Appendix A"; python3 -I $S/seqE.py $S 90 93 446 446 "Appendix B"   # 0 差异 (尾部 delete = 表格, 另核)
python3 -I $S/seqE.py $S 422 442 461 461 "Appendix F"    # 576/576 词; 非 equal 仅既有文字弯/直引号 4 处 (S-TYPO) + 行内引导语句点 (KB H3, 规则 6)
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1; KB 8 表全部 UNPARSEABLE (无 Row 列) → 全部人工; PDF_ONLY 在 p444-461 = 0; pdf_unparsed (p274/p342) 非本批
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # RED; 71 regress 全部 ∈ t2_fp_expected_regressions.jsonl, 意外 0; p441-461 回归 0; p444-461 原子 121 = EQUIVALENT 103 + EXACT 18 (同 baseline)
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### 页范围复核 (O20)
- 同意 444-461: p443 = OI Ex 表 Row 6-14 (§9.2); p444 首行 `10 Appendices`; p461 = App F, PDF 共 461 页.

### 双向全扫 — 逐页 (reviewer 自己的计数)
| 页 | PDF→KB | KB→PDF | 表 (逐格) | 结论 |
|---|---|---|---|---|
| 444 | 句 2 (章标题 `10 Appendices` = KB H1) 全中; 表 35 行 (2 多行格合并) | KB:9 逐字; :11-49 | Name/Company 35×2 (tabA + 渲染) | 一致 |
| 445 | 表 39 行 (续表头) | :48-86 | 39×2; Anita Umesh Company 空 (渲染确认) | 一致 |
| 446 | 引言 1 句 + 表 32 行 (3 续行) | KB:92, :96-127 | 32×2 (tabB) | 一致; PDF 无表头 → KB 空表头成立 |
| 447 | 表 8 行 | :128-135 | 8×2 | 一致 |
| 448 | 5 段 + C1 标题 + 引言 + 表 3 行 | :147-165 | C1 3×3 + 表头 (渲染) | 一致 |
| 449 | 2 段 + 表 33 行 | :171-173, :177-211 | 33×2 (tabD) | 一致 |
| 450 | 表 47 行 | :212-258 | 47×2 (tabD + 渲染) | 一致 |
| 451 | 表 26 行 | :259-284 | 26×2 | 一致 |
| 452 | 引言 1 + bullet 2 + 引导句 + bullet 11 + MO 框 (标题 + 1 句 + bullet + 2 段) | :288-319 | — | 一致 (seqE 0 差异) |
| 453 | New Domains 5 行 + 引言 + 变更表 Section 1-4 组行 4 + 数据行 10 | :321-350 | 5×2 渲染; 变更表 seqE | 一致 |
| 454 | 4.2 续 + 4.4/4.5/4.1(重复)/Section 5 组/5/5.1/5.2 | :350-357 | seqE + 渲染 | 一致; T-1 |
| 455 | 5.2 续 - 6.2.4 (含 Section 6 组行) | :357-370 | seqE + 渲染 | 一致; "Clinical Events" 无 (CE) 渲染确认 |
| 456 | 6.2.4 续 - 6.3.5.5 | :370-383 | seqE + 渲染 | 一致; ISCNDAGT |
| 457 | 6.3.5.6 - 6.4.4 | :384-388 | seqE + 渲染 | 一致; LBBDAGNT; T-2; T-3; 子项 o×2 = KB ◦×2 |
| 458 | 6.4.4 续 - 8.2.2 (Section 7/8 组行) | :388-400 | seqE + 渲染 | 一致 |
| 459 | 8.4.1-8.8 + Section 9 组行 + 空 bullet 行 10 + §9 子表 1 行 + `Appendices` + 子表 2 行 | :401-416 | seqE + 渲染 | 一致; 空行 10 不落 (主控裁定 ②) |
| 460 | App D / App E 行 | :417-418 | seqE | 一致 |
| 461 | App F 6 段 (含 Note) | :422-442 | seqE 576/576 词 | 一致 (引号 S-TYPO) |

- 变更表主表计数 (reviewer 自数): 数据行 60 + Section 组行 9 = 69 (= census n_rows 69); §9 子表 1; Appendices 子表 4. bullet: PDF `•` 在 p453-460 共 171, 其中 p459 空行 10; seqE 有序匹配下其余 161 全部对上.
- 排版字符: 新插入文字 — 变更表直引号 66 处 = PDF p453-460 直引号 66; 单引号 8 = 8; 3.2 Section Name en dash `–` 照 PDF (HEAD 为 em dash); App F 新插 `(“the Policy”)` 用弯引号照 PDF. 既有文字 App F 直引号 vs PDF 弯引号 4 处 → S-TYPO, 不计.
- KB 导航行 (纯导航, 不 D6, 签字): H1 + `Source:` 行; `## Section 9: Study References (p441)` + :141 交叉引用; `### Fragment Reference Table`; `### General Changes Throughout`; `### Key Section-by-Section Changes`; `### No Other Warranties/Disclaimers` (= PDF 行内粗体引导语, 规则 6); `---` 分隔. 无其他无出处行; D6 标注 0 (同意).

### census_items 人工逐格 (不采信 writer)
| item | 改后行 | 页 | 方法 | 结果 |
|---|---|---|---|---|
| #36 glossary | :94 | 446-447 | tabB 40×2 + 渲染 | 40/40 一致; 5 格修正 (4 句点 + "[this document]") 均 = PDF |
| #37 C1 QNAM | :161 | 448 | 渲染 3×3 + 表头 | 一致; --REAS 格 = PDF 原句 (含 "for an intervention" / "It may be used") |
| #38 fragments | :177 | 449-451 | tabD 106×2 + p450 渲染 | 106/106 一致, 顺序 = PDF |
| #39 New Domains | :323 | 453 | 渲染 5×2 + 表头 | 一致 (`Domain | Domain Abbreviation`, 名称在前) |
| #40 变更表 | :335 / :407 / :413 | 453-460 | seqE 有序词级 + 渲染 p453-459 列归属 | 69+1+4 行一致; Section Name 列归属 (2.7 / 3.2 / 6.4.1 / 8.6.3 / 6.3.5.5 折行) 渲染确认 |
| (新) App A 名单 | :11 | 444-445 | tabA 74×2 + 渲染 p445 | 74/74 一致 |

### 删除清单签字 (D2/R2 依据)
| D | 内容 | 签字 | 依据 |
|---|---|---|---|
| D-1 | HEAD:11 App A 自写摘要 (含 "full list … available in the source PDF") | 同意 | KB 自写占位, 真表已补 (主控裁定 ③); 摘要中机构归类为 KB 推断, 无 PDF 出处 |
| D-2 | HEAD:66-69 §9 引言 + 2 bullet | 同意 | PDF p441 属 §9 非 §10; DI/assumptions.md:3-8 `## §9 Study References` 逐字承载 (HEAD 669405f, 与 p441 逐字核); ch10:141 交叉引用锚点 `#9-study-references` 有效, live docs 42 |
| D-3 | HEAD:81-87 `### Key Points` + 5 条 | 同意 | 5 条均为 :147-155 PDF 5 段的压缩复述 (R2 补原文后残留); 无独有信息; 全仓无入站锚点 |
| D-4 | HEAD:103/105/107-113 App D 改写段 + `### Rules for Using Fragments` 3 条 | 同意 | 信息全部在 :171-173 PDF 原文; "within the established naming conventions for the SUPP-- or --TESTCD variable being created" PDF 无 (自添) → D2 |
| D-5 | HEAD:119-181 4 列片段表 | 同意 | 重建为 2 列 106 行; KB 原 106 对 → 新表集合差 0 (tabD 对 PDF 0 差异) |
| D-6 | HEAD:194-204 / :208-215 / :230-305 旧改写 bullet / New Domains / 变更表 | 同意 | VALUE_DIFF 旧值被 PDF 原文替换; 旧值含错 (ISNCNDAGT / LBDAGNT / "Clinical Events (CE)" / 3.2 em dash / 4.1 重复行缺失); HEAD:218-224 MO 正文原样移动 (逐字未改) |
| D-7 | HEAD:216 `### Decommissioning of MO (Morphology)` | 同意 | PDF 原标题 "A note on the decommissioning of MO" 已补 (:311); 全 KB / web/src / docs 无 `ch10_appendices.md#` 入站链接 (grep 0) → S-TDM 口径删 |
| D-8 | HEAD:327 "WHETHER ARISING UNDER" 的 ARISING | 同意 | PDF p461 "WHETHER UNDER CONTRACT"; seqE App F 词级 0 差异 |

### 结构改动清单签字
| S | 签字 | 依据 |
|---|---|---|
| S1 App A 整表 74 行 | 同意 | p444-445; 主控裁定 ③ |
| S2 §9 块 → 交叉引用 | 同意 | 见 D-2 |
| S3 删 Key Points | 同意 | 见 D-3 |
| S4 App D 改写删除 + 表 2 列 | 同意 | PDF 单表 2 列 (p450 渲染) |
| S5 MO 标题 + 前移; New Domains 重建; 变更表拆 3 表 | 同意 | p452 MO 框在 New Domains (p453) 之前; p459 §9 / Appendices 为独立子表, 表头 "Change" (渲染) |

### PDF_TYPO 核依据
| T | 判定 | 依据 |
|---|---|---|
| T-1 `(–DRVFL)` → `--DRVFL` | 成立 (PDF 自身可定) | 同页 4.4 行 "the use of --DRVFL was clarified" (p454:17); 同一变量, en dash 为 "--" 自动替换 |
| T-2 `--TETM` → `--TERM` | 成立 (PDF 自身可定) | 全 PDF 仅 p457 出现 --TETM; 本行所述 §6.4.3 原句 p364:35 "FAOBJ should match the value in --TERM or --TRT … --DECOD"; 4.5 行 "--TRT or --TERM" |
| T-3 "version the underwent" | 照录成立 | 语法错, 正确词 PDF 内无依据可定 → 照录 + T4 |
| T-4 4.1 行重复 | 照录成立 | p454 渲染确认 4.1 行在 4.5 后再次出现; 主控裁定 ① |
| T-5 MO "deprecate MO in SDTMIG v3.4" | 照录成立 | ch10:317 = p452:35 逐字; p285:9 为 "in a future version of the SDTMIG" (NV/assumptions.md 照 p285); PDF 内部不一致, 各节照本节 |

### batch notes 结论
- ch10:222 (现 :317) MO 句 = p452 §10 原文, 保留不改 — 同意.
- §9 引言 → DI 交叉引用 — 同意; `live docs: 42`.
- p459 空 bullet 行 10 不落 — 同意 (主控裁定 ②, 无文字).

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| L-1 ch10:388 | 表示 | 6.4.4 `o` 子项写成 `<br>◦` 与父 bullet 同级, 层级只靠字形区分 | p457 渲染子项缩进; ch08 先例, 信息无损 — LOW, 不改 |
| L-2 ch10:94 | 表示 | 空表头 `| | |` (PDF 无表头) 在部分渲染器显示空行 | S-INT EX Ex2 先例 — LOW, 不改 |
| L-3 ch10:430/432/436 | 排版 | 既有 App F 直引号 vs PDF 弯引号 (“ ” ’) | U1 归 S-TYPO — LOW, 不计 |

无 REAL_GAP; 无无出处行; 无清单外删除; 无授权外改动.
