# 待改标签清单 (补检 + Q9 扩检 + 第二轮补检查出; **未执行, 待主人裁定**)

<!-- chain: E (plans) -->
> 状态: **待主人裁定** (2026-11-27). 共 82 条. 台账 `work/coverage_ledger.wc.jsonl` 未改 (md5 `60729f7b64b7c1dfaf2174e394f6dd9c`). 本文件由 `scripts/t4/t4_supp_report.py` 生成; 依据是独立审查者的原始结果 ("原始结果" 列), 主控未改判.
> 为什么不直接改: 这些是闸口径层面的事, 须主人本人定 (总闸 attempt 2 C 项; 协调方 2026-11-27 指示, `t4_coordinator_note_20261127.md`); PDF_TYPO 每条须用户 ack (G-TB1); 主人已确认的 U-1 口径数字建立在当前台账上. (Q9 brief 原写 "NOT_HOLD_R1 → 改 IE", 这里收紧为先问主人.)

## 1. 三组 (提问与选项以 `t4_owner_decisions_round2.md` 为准, 这里只列组)

| 组 | 条数 | 现标签 → 建议 | 对应给主人一页的 |
|---|--:|---|---|
| R1-row | 49 | EQUIVALENT → INTENTIONAL_EXCLUDE | 问题 1 (主人选 A) |
| R1-row | 2 | EXACT → INTENTIONAL_EXCLUDE | 问题 1 (主人选 A) |
| registered-typo | 10 | EQUIVALENT → PDF_TYPO | 问题 3 (主人选 A) |
| registered-typo | 9 | EXACT → PDF_TYPO | 问题 3 (主人选 A) |
| registered-typo-oos | 5 | EQUIVALENT → PDF_TYPO | 问题 7b (主人选 A; 第三轮审查者已对渲染页确认) |
| registered-typo-oos | 1 | EXACT → PDF_TYPO | 问题 7b (主人选 A; 第三轮审查者已对渲染页确认) |
| typo-overlabel | 4 | PDF_TYPO → EXACT | 第三轮新发现, **待主人定** |
| v2.0-TOC | 2 | EQUIVALENT → INTENTIONAL_EXCLUDE | 问题 2 (主人选 A) |

## 2. 各选法下的闸数字 (在台账**副本**上实算; 工作台账 md5 断言不变)

| 选法 | 改几条 | G-TB3 U-1 B 口径 (过闸用; 闸线 99.0192%) | strict (并列报) | mapped | 内容指标 (EXACT+EQUIV) | G-TB1 范围内节 / 残留 | G-TB2 字面口径 |
|---|--:|---|---|---|---|---|---|
| 都不改 (现状) | 0 | 9913/9986 = 99.2690% | 9567/9986 = 95.8041% | 9567/9629 = 99.3561% | 8733/9629 = 90.6948% | 174/174 / 0 | 157/174 |
| 只改: 变量表行 → 有意不收 | 51 | 9862/9935 = 99.2652% | 9516/9935 = 95.7826% | 9516/9578 = 99.3527% | 8682/9578 = 90.6452% | 174/174 / 0 | 157/174 |
| 只改: 目录条目 → 有意不收 | 2 | 9911/9984 = 99.2688% | 9565/9984 = 95.8033% | 9565/9627 = 99.3560% | 8731/9627 = 90.6928% | 174/174 / 0 | 157/174 |
| 只改: 笔误原子 → PDF 笔误 | 19 | 9913/9986 = 99.2690% | 9548/9986 = 95.6139% | 9548/9610 = 99.3548% | 8714/9610 = 90.6764% | 174/174 / 0 | 157/174 |
| 变量表行 + 目录条目 | 53 | 9860/9933 = 99.2651% | 9514/9933 = 95.7817% | 9514/9576 = 99.3525% | 8680/9576 = 90.6433% | 174/174 / 0 | 157/174 |
| 变量表行 + 笔误原子 | 70 | 9862/9935 = 99.2652% | 9497/9935 = 95.5913% | 9497/9559 = 99.3514% | 8663/9559 = 90.6266% | 174/174 / 0 | 157/174 |
| 三组都改 (建议) | 72 | 9860/9933 = 99.2651% | 9495/9933 = 95.5905% | 9495/9557 = 99.3513% | 8661/9557 = 90.6247% | 174/174 / 0 | 157/174 |
| 三组都改 + 范围外 p74 的 14 条 → 有意不收 | 86 | 9846/9919 = 99.2640% | 9481/9919 = 95.5842% | 9481/9543 = 99.3503% | 8648/9543 = 90.6214% | 174/174 / 0 | 157/174 |
| 三组都改 + 范围外跨文档指针 146 条全 → 有意不收 (按都认 IE 计的情形) | 218 | 9714/9787 = 99.2541% | 9349/9787 = 95.5247% | 9349/9411 = 99.3412% | 8628/9411 = 91.6799% | 174/174 / 0 | 158/174 |
| 三组都改 + 范围外已登记笔误同类 6 条 → PDF 笔误 (= 主人已定的全部: 1A / 2A / 3A / 7b-A) | 78 | 9860/9933 = 99.2651% | 9489/9933 = 95.5301% | 9489/9551 = 99.3509% | 8655/9551 = 90.6188% | 174/174 / 0 | 157/174 |
| 主人已定的全部 + 4 条多标的 PDF 笔误 → 逐字 (待主人定) | 82 | 9860/9933 = 99.2651% | 9493/9933 = 95.5703% | 9493/9555 = 99.3511% | 8659/9555 = 90.6227% | 174/174 / 0 | 157/174 |

- G-TB2 的过闸口径是 "范围内" (U-3 A): 174/174; 表里最后一列是 `t3_recompute.py` 打印的字面口径值 (17 个结构父节仅因范围外子节不满), 两者在各选法下都不变.
- U-1 B 口径在所有选法下都高于闸线; strict 在所有选法下都低于 (与 attempt 2 相同的性质).
- 改成 "有意不收" 的原子同时离开分子和分母; 改成 PDF_TYPO 的在 U-1 B 口径下仍算覆盖, 在 strict / mapped / 内容指标里不算.
- 范围外的三行不在 G-TB1 / G-TB2 的范围内, 但 G-TB3 按整本台账算, 所以会动 G-TB3 的分子分母. "146 条全改" 是**假设配错的都认 IE** 的情形 (那 146 条里只有 p74 的 14 条被审查者看过; 其中 113 条现标 PARTIAL): 若有的内容自己文档的 KB 里也没有、又不认 IE, 应记未覆盖, 数字会比这一行更低; 若内容其实在 `model/` 里只是指针错, 标签不变. 所以这一行不是严格的下限.
- "范围外已登记笔误同类 6 条" 是 delta 复审者在文本层确认的, 未经 tracer 审, 不在下面 §3 的清单里.
- 改标只动标签, 不动 KB. 执行时走 writer (`oh-my-claudecode:executor`) → reviewer, 并在同一次回写里处理 registry `B-IS T-6` 页号 p241 → p239 (页号参与登记匹配 `t3_errata_build.py:150` / `t3_writeback.py:404`, 单独改有改变台账的风险) 与 `t4_supp_fullcheck.md` §6 所列的登记指针补全.

## 3. 逐条

| # | atom_id | 页 | 节 | 现标签 | 建议 | 组 | 理由 | 原始结果 |
|--:|---|--:|---|---|---|---|---|---|
| 1 | `sv20_p0046_a002` | 46 | §3.2.3.1 [Subject Elements] | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:26` |
| 2 | `sv20_p0047_a002` | 47 | §3.2.3.2 [Subject Repro Stages] | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:28` |
| 3 | `sv20_p0052_a012` | 52 | §5.1.1.2 Trial Arms | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:33` |
| 4 | `sv20_p0052_a013` | 52 | §5.1.1.2 Trial Arms | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:34` |
| 5 | `sv20_p0052_a014` | 52 | §5.1.1.2 Trial Arms | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:35` |
| 6 | `sv20_p0052_a016` | 52 | §5.1.1.2 Trial Arms | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:36` |
| 7 | `sv20_p0052_a017` | 52 | §5.1.1.2 Trial Arms | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:37` |
| 8 | `sv20_p0053_a004` | 53 | §5.1.1.2 Trial Arms | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:38` |
| 9 | `sv20_p0053_a011` | 53 | §5.1.2 Trial Sets | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:39` |
| 10 | `sv20_p0053_a012` | 53 | §5.1.2 Trial Sets | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:40` |
| 11 | `sv20_p0053_a014` | 53 | §5.1.2 Trial Sets | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:41` |
| 12 | `sv20_p0053_a015` | 53 | §5.1.2 Trial Sets | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:42` |
| 13 | `sv20_p0053_a016` | 53 | §5.1.2 Trial Sets | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:43` |
| 14 | `sv20_p0053_a018` | 53 | §5.1.2 Trial Sets | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:44` |
| 15 | `sv20_p0055_a005` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:20` |
| 16 | `sv20_p0055_a006` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:21` |
| 17 | `sv20_p0055_a007` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:22` |
| 18 | `sv20_p0055_a008` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:23` |
| 19 | `sv20_p0055_a009` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:24` |
| 20 | `sv20_p0055_a010` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:25` |
| 21 | `sv20_p0055_a011` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:26` |
| 22 | `sv20_p0055_a012` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:27` |
| 23 | `sv20_p0056_a012` | 56 | §5.1.4.1 Trial Visits | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:29` |
| 24 | `sv20_p0056_a013` | 56 | §5.1.4.1 Trial Visits | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:30` |
| 25 | `sv20_p0056_a015` | 56 | §5.1.4.1 Trial Visits | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:31` |
| 26 | `sv20_p0056_a016` | 56 | §5.1.4.1 Trial Visits | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:32` |
| 27 | `sv20_p0057_a005` | 57 | §5.1.4.2 Trial Disease Assessments | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:34` |
| 28 | `sv20_p0057_a008` | 57 | §5.1.4.2 Trial Disease Assessments | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:35` |
| 29 | `sv20_p0057_a009` | 57 | §5.1.4.2 Trial Disease Assessments | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:36` |
| 30 | `sv20_p0057_a010` | 57 | §5.1.4.2 Trial Disease Assessments | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:37` |
| 31 | `sv20_p0058_a005` | 58 | §5.1.4.3 Trial Disease Milestones | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:39` |
| 32 | `sv20_p0058_a006` | 58 | §5.1.4.3 Trial Disease Milestones | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:40` |
| 33 | `sv20_p0058_a007` | 58 | §5.1.4.3 Trial Disease Milestones | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:41` |
| 34 | `sv20_p0058_a015` | 58 | §5.1.5 Trial Inclusion/Exclusion Criteria | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:43` |
| 35 | `sv20_p0058_a017` | 58 | §5.1.5 Trial Inclusion/Exclusion Criteria | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:44` |
| 36 | `sv20_p0058_a018` | 58 | §5.1.5 Trial Inclusion/Exclusion Criteria | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:22` |
| 37 | `sv20_p0059_a001` | 59 | §5.1.5 Trial Inclusion/Exclusion Criteria | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:23` |
| 38 | `sv20_p0059_a002` | 59 | §5.1.5 Trial Inclusion/Exclusion Criteria | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:24` |
| 39 | `sv20_p0059_a010` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:27` |
| 40 | `sv20_p0059_a011` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:28` |
| 41 | `sv20_p0059_a012` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:29` |
| 42 | `sv20_p0059_a014` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:30` |
| 43 | `sv20_p0059_a015` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:31` |
| 44 | `sv20_p0059_a016` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:32` |
| 45 | `sv20_p0059_a017` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:33` |
| 46 | `sv20_p0060_a001` | 60 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:34` |
| 47 | `sv20_p0065_a003` | 65 | §6.1 [Related Records Dataset] | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:39` |
| 48 | `sv20_p0069_a001` | 69 | §6.6 [Associated Persons Relationships] | EXACT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_supp_raw/pack_2.md:50` |
| 49 | `sv20_p0069_a002` | 69 | §6.6 [Associated Persons Relationships] | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:43` |
| 50 | `sv20_p0069_a003` | 69 | §6.6 [Associated Persons Relationships] | EXACT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_supp_raw/pack_2.md:51` |
| 51 | `sv20_p0069_a004` | 69 | §6.6 [Associated Persons Relationships] | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:44` |
| 52 | `ig34_p0037_a002` | 37 | §4.3.2 Controlled Terminology Text Case | EQUIVALENT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-ch04 T-3 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib2_1.md:21` |
| 53 | `ig34_p0043_a010` | 43 | §4.4.7 [Use of Relative Timing Variables] | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 S-CH4 T-8 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib_1.md:18` |
| 54 | `ig34_p0047_a009` | 47 | §4.4.10 [Representing Time Points] | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 S-CH4 T-9 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib_1.md:21` |
| 55 | `ig34_p0064_a012` | 64 | §5.2 [Demographics (DM)] | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 S-SPEC1 T-3 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib_1.md:22` |
| 56 | `ig34_p0069_a004` | 69 | §5.2 [DM – Examples] | EQUIVALENT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-DM T-3 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib2_1.md:27` |
| 57 | `ig34_p0078_a022` | 78 | §5.2 [Demographics (DM)] | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-DM T-1 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib_1.md:25` |
| 58 | `ig34_p0119_a017` | 119 | §6.1.3.3 [Exposure/Exposure as Collected Exa | EQUIVALENT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-EX T-1 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib_1.md:31` |
| 59 | `ig34_p0147_a025` | 147 | §6.2.2 [Biospecimen Events (BE)] | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-BE T-3 (KB 写正确值) | `evidence/t4_supp_raw/pack_1.md:35` |
| 60 | `ig34_p0147_a026` | 147 | §6.2.2 [Biospecimen Events (BE)] | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-BE T-3 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib_1.md:35` |
| 61 | `ig34_p0201_a005` | 201 | §6.3.5.3 Cell Phenotype Findings (CP) | EQUIVALENT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 S-SPC1 CP T-20 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib2_1.md:32` |
| 62 | `ig34_p0212_a001` | 212 | §6.3.5.3 Cell Phenotype Findings (CP) | EQUIVALENT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-CP T-5 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib2_1.md:34` |
| 63 | `ig34_p0256_a007` | 256 | §6.3.5.7.2 Microbiology Susceptibility (MS) | EQUIVALENT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-MS T-5 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib2_2.md:17` |
| 64 | `ig34_p0262_a016` | 262 | §6.3.5.7 Microbiology Domains | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-MB T-1 (KB 写正确值) | `evidence/t4_supp_raw/pack_2.md:42` |
| 65 | `ig34_p0262_a017` | 262 | §6.3.5.7 Microbiology Domains | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-MB T-1 (KB 写正确值) | `evidence/t4_supp_raw/pack_2.md:43` |
| 66 | `ig34_p0277_a026` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | EQUIVALENT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-PCPP T-1 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib_3.md:22` |
| 67 | `ig34_p0278_a015` | 278 | §6.3.5.9.3 Relating PP Records to PC Records | EQUIVALENT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-PCPP T-2 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib_3.md:23` |
| 68 | `ig34_p0278_a028` | 278 | §6.3.5.9.3 Relating PP Records to PC Records | EQUIVALENT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-PCPP T-3 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib_3.md:24` |
| 69 | `ig34_p0296_a023` | 296 | §6.3.7.4 Nervous System Findings (NV) | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-NV T-2 (KB 写正确值) | `evidence/t4_supp_raw/pack_2.md:47` |
| 70 | `ig34_p0357_a014` | 357 | §6.3.12.3 Tumor Identification/Tumor Results | EQUIVALENT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-TR T-2 (KB 写正确值; 审查者在原始结果该行确认) | `evidence/t4_round2_raw/pack_sib_3.md:28` |
| 71 | `ig34_p0083_a020` | 83 | §5.3 [Subject Elements (SE)] | EXACT | PDF_TYPO | registered-typo-oos | 范围外; KB 与 PDF 的差异 = 已登记 PDF 笔误 S-SPREL SE T-1 (KB 写正确值; 审查者对渲染页确认) | `evidence/t4_round3_raw/pack_13_14.md:36` |
| 72 | `ig34_p0304_a026` | 304 | §6.3.7.5 Ophthalmic Examinations (OE) | EQUIVALENT | PDF_TYPO | registered-typo-oos | 范围外; KB 与 PDF 的差异 = 已登记 PDF 笔误 B-OE T-2 (KB 写正确值; 审查者对渲染页确认) | `evidence/t4_round3_raw/pack_13_14.md:37` |
| 73 | `ig34_p0304_a027` | 304 | §6.3.7.5 Ophthalmic Examinations (OE) | EQUIVALENT | PDF_TYPO | registered-typo-oos | 范围外; KB 与 PDF 的差异 = 已登记 PDF 笔误 B-OE T-2 (KB 写正确值; 审查者对渲染页确认) | `evidence/t4_round3_raw/pack_13_14.md:38` |
| 74 | `ig34_p0304_a028` | 304 | §6.3.7.5 Ophthalmic Examinations (OE) | EQUIVALENT | PDF_TYPO | registered-typo-oos | 范围外; KB 与 PDF 的差异 = 已登记 PDF 笔误 B-OE T-2 (KB 写正确值; 审查者对渲染页确认) | `evidence/t4_round3_raw/pack_13_14.md:39` |
| 75 | `ig34_p0304_a029` | 304 | §6.3.7.5 Ophthalmic Examinations (OE) | EQUIVALENT | PDF_TYPO | registered-typo-oos | 范围外; KB 与 PDF 的差异 = 已登记 PDF 笔误 B-OE T-2 (KB 写正确值; 审查者对渲染页确认) | `evidence/t4_round3_raw/pack_13_14.md:40` |
| 76 | `ig34_p0316_a023` | 316 | §6.3.8 Physical Examination (PE) | EQUIVALENT | PDF_TYPO | registered-typo-oos | 范围外; KB 与 PDF 的差异 = 已登记 PDF 笔误 S-FND PE T-1 (KB 写正确值; 审查者对渲染页确认) | `evidence/t4_round3_raw/pack_13_14.md:41` |
| 77 | `ig34_p0412_a006` | 412 | §7.3.2 Trial Disease Assessments (TD) – Exam | PDF_TYPO | EXACT | typo-overlabel | 登记的笔误不在这条原子里 (在相邻原子 / 另一张表); 这条 KB 与 PDF 逐字一致, 现标 PDF_TYPO 多标了 | `evidence/t4_round3_raw/pack_10.md:29` |
| 78 | `ig34_p0412_a007` | 412 | §7.3.2 Trial Disease Assessments (TD) – Exam | PDF_TYPO | EXACT | typo-overlabel | 登记的笔误不在这条原子里 (在相邻原子 / 另一张表); 这条 KB 与 PDF 逐字一致, 现标 PDF_TYPO 多标了 | `evidence/t4_round3_raw/pack_10.md:30` |
| 79 | `ig34_p0412_a008` | 412 | §7.3.2 Trial Disease Assessments (TD) – Exam | PDF_TYPO | EXACT | typo-overlabel | 登记的笔误不在这条原子里 (在相邻原子 / 另一张表); 这条 KB 与 PDF 逐字一致, 现标 PDF_TYPO 多标了 | `evidence/t4_round3_raw/pack_10.md:31` |
| 80 | `ig34_p0413_a010` | 413 | §7.3.2 Trial Disease Assessments (TD) – Exam | PDF_TYPO | EXACT | typo-overlabel | 登记的笔误不在这条原子里 (在相邻原子 / 另一张表); 这条 KB 与 PDF 逐字一致, 现标 PDF_TYPO 多标了 | `evidence/t4_round3_raw/pack_10.md:32` |
| 81 | `sv20_p0003_a011` | 3 | §0 [TOC] | EQUIVALENT | INTENTIONAL_EXCLUDE | v2.0-TOC | SDTM v2.0 目录条目, 对应章节 KB 未收 (同页 a009 / a010 已是 IE VERSION_MISMATCH) | `evidence/t4_q9_raw/pack_2.md:33` |
| 82 | `sv20_p0003_a012` | 3 | §0 [TOC] | EQUIVALENT | INTENTIONAL_EXCLUDE | v2.0-TOC | SDTM v2.0 目录条目, 对应章节 KB 未收 (同页 a009 / a010 已是 IE VERSION_MISMATCH) | `evidence/t4_q9_raw/pack_2.md:34` |

## 4. 复跑

```bash
python3 -I .work/10_tier_b_repair/scripts/t4/t4_supp_report.py
# 各选法的台账副本: work/scratch/t4/relabel_preview/ledger_<name>.jsonl (gitignored); 数字另存 work/t4/supp/scenarios.json
```

