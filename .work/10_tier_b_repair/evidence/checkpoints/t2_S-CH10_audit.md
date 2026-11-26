# T2S.S-CH10 Auditor (Rule A) — attempt 1

> auditor: oh-my-claudecode:verifier (opus); 先独立判, 判完才读 `t2_S-CH10.md` / `t2_S-CH10_review.md`. 只读 KB.
> 范围: `knowledge_base/chapters/ch10_appendices.md` (git diff HEAD, +297/-184), PDF §10 p444-461.

## 抽样 (可复跑)
脚本 `scratchpad/t2s_S-CH10_auditor/sample.py` (session d6800696…), 要点:
- P = pdf_atoms 中 src=ig34, p444-461, atom_type ∈ SENTENCE/LIST_ITEM/NOTE/CROSS_REF/TABLE_ROW, parent_section 以 `§10` 或 `Appendix ` 开头 (Appendix A-F = §10.A-F; 边界页 §9.2 OI 原子排除), 去 ledger INTENTIONAL_EXCLUDE (75 = App A 名单 74 + App E 1). intros 无.
- C (writer.jsonl 涉及页 441/444/446/448/449/452/453/454/457/459/461 上的 P 原子) = 201; |P| = 311.
- N = min(30, max(20, ceil(0.1×311)), 311) = **30**; 先从 C 抽 ceil(N/3)=10, 余 20 从 P−已抽 随机. seed = 20261126.
- 结果: `{"P": 311, "C_writer_pages": 201, "N": 30, "k_writer": 10}`

## 样本判定 (TABLE_ROW 均对渲染图逐格: p446/447/448/449/450/451/453/454/456/458/460, pdftoppm -r 80; App D 原子页码比实页 -1, 以内容定位)
| # | atom_id | PDF 页 + 摘要 | KB ch10 行 | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0449_a042 | p450 App D 行 REGIMEN / RGM | :253 | 否 | 是 | App D | 渲染逐格一致 |
| 2 | ig34_p0449_a034 | p450 OVERDOSE / OD | :245 | 否 | 是 | App D | 同上 |
| 3 | ig34_p0446_a008 | p446 App B CDASH 行 | :99 | 否 | 是 | App B | 渲染: PDF 表无表头, KB 空表头一致 |
| 4 | ig34_p0453_a013 | p453 变更表 2.1 Observations and Variables / Revised definition… | :340 | 否 | 是 | App E | PDF 该格无 bullet, KB 亦无 |
| 5 | ig34_p0454_a002 | p454 4.4 行 4 个 bullet | :351 | 否 | 是 | App E | 渲染: 末 2 bullet 无句点, KB 照录 |
| 6 | ig34_p0446_a020 | p446 ICH E2A 行 | :111 | 否 | 是 | App B | 折行合并 |
| 7 | ig34_p0448_a042 | p449 ELEMENT / ET | :206 | 否 | 是 | App D | |
| 8 | ig34_p0449_a004 | p450 FLAG / FL | :215 | 否 | 是 | App D | |
| 9 | ig34_p0453_a017 | p453 组行 Section 3. Submitting Data… | :344 | 否 | 是 | App E | 组行粗体 = 导航格式 |
| 10 | ig34_p0448_a025 | p449 CLASS / CLAS | :189 | 否 | 是 | App D | |
| 11 | ig34_p0450_a014 | p451 TIME / TM | :272 | 否 | 是 | App D | |
| 12 | ig34_p0448_a004 | p448 C1 AESOSP / Other Medically Important SAE / AE | :163 | 否 | 是 | App C1 | 3 格一致 |
| 13 | ig34_p0452_a022 | p452 MO 框 "This led to the decision … deprecate MO in SDTMIG v3.4." | :317 | 否 | 是 | App E MO 小节 | 逐字; 与 p285 不一致属 PDF 内部 (T-5) |
| 14 | ig34_p0451_a014 | p451 TIME / TM (同表重复原子) | :272 | 否 | 是 | App D | |
| 15 | ig34_p0449_a036 | p450 PATTERN / PATT | :247 | 否 | 是 | App D | |
| 16 | ig34_p0458_a011 | p458 组行 Section 8. Representing Relationships and Data | :398 | 否 | 是 | App E | |
| 17 | ig34_p0448_a018 | p449 ASSAY / AS | :182 | 否 | 是 | App D | |
| 18 | ig34_p0458_a007 | p458 7.3.3 TM: TMDEF role Rule→Variable Qualifier … "MIDSTYPE" | :394 | 否 | 是 | App E | 渲染逐格; 2 句完整 |
| 19 | ig34_p0460_a002 | p460 Appendix E / This appendix / • updated to reflect overview v3.3→v3.4 | :418 | 否 | 是 | App E Appendices 子表 | 渲染有 bullet, KB 有 |
| 20 | ig34_p0452_a021 | p452 MO 框 "Since then, the team found … little added value." | :317 | 否 | 是 | App E MO 小节 | 逐字 |
| 21 | ig34_p0452_a014 | p452 throughout 列表 "Where numbered lists occurred in CDISC Notes…" | :307 | 否 | 是 | App E | 逐字 |
| 22 | ig34_p0451_a026 | p451 VEHICLE / V | :284 | 否 | 是 | App D | 表末行 |
| 23 | ig34_p0452_a003 | p452 "A Diff file … CDISC Library Archives … (URL) … not repeated here." | :292 | 否 | 是 | App E | 逐字含 URL |
| 24 | ig34_p0449_a013 | p450 INTERPRETATION / INTP | :224 | 否 | 是 | App D | |
| 25 | ig34_p0456_a002 | p456 6.2.6 MH / • Example 5 was added … prespecified events. | :372 | 否 | 是 | App E | |
| 26 | ig34_p0447_a003 | p447 SEND / Standard for Exchange of Non-Clinical Data | :130 | 否 | 是 | App B | |
| 27 | ig34_p0461_a004 | p461 Patent "By publication of this standard, no position is taken…" | :426 | 否 | 是 | App F | 逐字 |
| 28 | ig34_p0449_a030 | p450 ORIGIN / ORIG | :241 | 否 | 是 | App D | |
| 29 | ig34_p0448_a005 | p448 C1 AETRTEM / Treatment Emergent Flag / AE | :164 | 否 | 是 | App C1 | |
| 30 | ig34_p0451_a018 | p451 TRANSITION / TRANS | :276 | 否 | 是 | App D | |

**独有信息丢失 0 / 忠实度错误 0 / 位置错误 0.**

## 另查
- App D 全表机械对照: PDF p449-451 `pdftotext -layout` 106 行 vs KB :179-284 106 行, **有序 diff 完全一致** (2 列, 渲染确认 PDF 为单 2 列表, 旧 KB 4 列拼排已重建).
- App B 40 行 / App C1 3 行 / New Domains 5 行 / 变更表抽中行: 渲染逐格一致. App A 名单 (ledger IE, 不入 P) 抽查 p444-445: 表头 Name/Company、Qgunsulire / Anita Umesh 空公司格照 PDF.
- intros / gaps: batch json 均为空, 无项需落地. footnote: 本批无 spec.md.
- 无 PDF 出处行 (U8 口径): ch10:3 `Source:` 行、`### Fragment Reference Table` / `### General Changes Throughout` / `### Key Section-by-Section Changes` (KB 标题)、`## Section 9: Study References (p441)` + :141 一行交叉引用 (§9 引言 D2 → DI, 已核 `domains/DI/assumptions.md` `## §9 Study References` 承载 p441 原文 + 2 条目) — 均为纯导航, 不计忠实错误. 其余行均有 PDF 出处; 无 KB 自写解释性段 (旧 "Key Points" / "Rules for Using Fragments" / 名单摘要等改写已删, 信息由 PDF 原句承载).
- 删除行核: diff `-` 行全部为旧改写/拼排/摘要, 对应 PDF 原文现均在新行中 (含 6.2.3 "Clinical Events" 去 "(CE)" 照 p455, ISNCNDAGT→ISCNDAGT / LBDAGNT→LBBDAGNT 照 PDF).
- PDF_TYPO: T-1 `(–DRVFL)`→`--DRVFL` (渲染 p454 确认 PDF 单 en dash; 同表 4.4 行 --DRVFL 可定) 成立; T-4 4.1 行重复 (渲染 p454 确认 PDF 原样) 照录成立.
- 授权范围: `git diff HEAD --stat` 本批仅 ch10_appendices.md (工作树中 ch04/ch08/02_obs 属他批).
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` = 基线 42.
- G-TB8: trace.jsonl 行 354 writer (executor) subagent_done, 行 361 reviewer (code-reviewer) subagent_done PASS; 无 main 写 KB 记录.

## 对照 (判完后读)
writer `t2_S-CH10.md` / reviewer `t2_S-CH10_review.md` (PASS, 3 LOW) 与本独立判一致; 无分歧.

## 结论: **PASS** (N=30, 丢失 0, 忠实 0)
