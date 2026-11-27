# T4.1 补检 ("0 抽中" 各类全检) + Q9 扩检 + 第二轮补检 — 汇总

<!-- chain: E (plans) -->
> 状态: **补检 PRE_EXISTING 层不通过 → 触发 Q9 升级; Q9 扩检与第二轮补检已跑完; 共查出 82 条标签应改, 主人都已直接定, 全部已执行: 78 条 (1A / 2A / 3A / 7b-A) 由 R2L 批, 4 条多标的 PDF_TYPO (问题 A = A1) 由 R3L 批; 1 条判不了的 (问题 B = B1) 维持 PDF_TYPO 并写明无法判定** (2026-11-27). KB 未改; 台账 `60729f7b…` → (R2L) `16024ac0…` → (R3L) `43809870…`; 备份 `work/coverage_ledger.wc.pre_r2l.jsonl` / `work/coverage_ledger.wc.pre_r3l.jsonl`; 见 `t4_round2_ledger_W.md` / `t4_round2_ledger_review.md` / `t4_round2_ledger_audit.md` 与 `t4_round3_ledger_W.md` / `t4_round3_ledger_review.md`.
> 审查: `oh-my-claudecode:tracer` (opus) 独立实例, 只读: 补检 8 + Q9 8 + 第二轮 8. 原始结果由审查者自己写入 `evidence/t4_supp_raw/`、`evidence/t4_q9_raw/`、`evidence/t4_round2_raw/`. 本文件 §1-§6 是主控用 `scripts/t4/t4_supp_report.py` 从原始结果机械汇总的, 不改判 (规则 D); 文末一节是主控手写的 "独立审查 B 的处理".
> 口径 (派发前写死): `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md`, `t4_q9_extension_v1.0.md`, `t4_supp_round2_v1.0.md`. 规则 B 归档: `evidence/failures/step_T4.SUPP_attempt_1.md`. 对本汇总的独立审查原文: `evidence/t4_gap_review_raw/review_b.md`.

## 1. 复跑

```bash
T=.work/10_tier_b_repair
python3 -I $T/scripts/t3/t3_direct_hit.py --out $T/work/t4/supp/direct_hit_head.json   # GREEN; pre_existing: R2L 之前 58 (补检取的就是这 58 条), R2L 之后 52 (其中 6 条改标后不再是 EXACT)
python3 -I $T/scripts/t4/t4_supp_sample.py     # 补检 203 条 / 8 包
python3 -I $T/scripts/t4/t4_q9_sample.py       # Q9 192 条 / 8 包 (seed 20261131)
python3 -I $T/scripts/t4/t4_round2_sample.py   # 第二轮 135 条 / 7 包 (seed 20261132)
python3 -I $T/scripts/t4/t4_round2b_sample.py  # 第二轮补充 40 条 / 2 包
python3 -I $T/scripts/t4/t4_supp_report.py     # 本文件 + t4_relabel_pending.md (台账只读; 各选法在改前备份台账的副本上预演)
```
- 这些抽样脚本不触碰总闸 / 人工样本文件 (`gate_sample.jsonl` `67b1013f496096df483eb300a66150d6`, `human_sample.jsonl` `5b4212ee6b5deb873ab29d7f13e17232`); 它们只 exec `t4_sample.py` / `t4_render.py` 的定义段.
- 样本 md5: supp `0fb5799b821c5a4dc900b39fbf86bf86`; q9 `5ad82bea9a68db72616a19f414afd5de`; round2 `f212fc3c7e8aacf10c1b94c1534de3bc`; round2b `6f9a13b8bbfa2dbe74b5361accd04f2f`.

## 2. 补检: 总体与结果 (全检, 不抽样)

总体取自 HEAD 的台账与决策表; 一个原子只进它命中的第一层; 已被总闸审查者判过的 (gate 84 条) 与 U-5 C7 全检过的 (38 条) 不重复审.

| 层 | 终态 | 总体 | 已在 gate 样本 | 本次审 | HOLDS | HOLDS_AS_EQUIV | NOT_HOLD | UNVERIFIABLE | 层结论 |
|---|---|--:|--:|--:|--:|--:|--:|--:|---|
| PRE_EXISTING | EXACT | 58 | 0 | 58 | 26 | 30 | 2 | 0 | **不通过** |
| FIG | FIGURE_DEFERRED | 11 | 0 | 11 | 11 | 0 | 0 | 0 | 通过 |
| TRIAGE_ATOM_ERR | ATOM_ERR | 74 | 0 | 74 | 74 | 0 | 0 | 0 | 通过 |
| TRIAGE_RELOCATE | EXACT | 3 | 0 | 3 | 3 | 0 | 0 | 0 | 通过 |
| TRIAGE_LOCATE | — | 0 | 0 | 0 | — | — | — | — | 总体为空 (T1 的 28 条 LOCATE 在 T1.4 定批时按 `ruling:LOCATE-LB` 转成了 REAL_GAP, 归 B-LB 批; `t2_batch_table.md:18`) |
| RULE_T1-two-agent+T2-rework | EQUIVALENT | 27 | 2 | 25 | 25 | 0 | 0 | 0 | 通过 |
| RULE_T2-fix+deltaRereviewPASS+auditPASS | EQUIVALENT | 5 | 0 | 5 | 5 | 0 | 0 | 0 | 通过 |
| RULE_live-hit(was-IE-ack) | EXACT | 19 | 0 | 19 | 19 | 0 | 0 | 0 | 通过 |
| RULE_C1-manual-PDF+KB | EQUIVALENT | 3 | 0 | 3 | 3 | 0 | 0 | 0 | 通过 |
| RULE_C7-K4-rereview | ATOM_ERR | 2 | 0 | 2 | 2 | 0 | 0 | 0 | 通过 |
| RULE_T1-two-agent | EQUIVALENT | 3 | 0 | 3 | 3 | 0 | 0 | 0 | 通过 |
| **合计** | | | | **203** | **171** | **30** | **2** | **0** | |

- `FIG` 11 条 = 终态 FIGURE_DEFERRED 全部 = triage 类 FIGURE 全部 (同一批原子); 审查者逐条看了渲染页, 并核了 KB 里的 Mermaid 再现与原图不矛盾.
- attempt 1 审查者点名的规则计数与今天不同, 原因是解冻轮 (W3) 改了规则名, 不是总体漏算:

| 规则 | attempt 1 时 (`3a24a1c` 的决策表) | HEAD | 变化来源 (旧规则 → 新规则: 条数) |
|---|--:|--:|---|
| `T1-two-agent` | 17 | 3 | — |
| `T1-two-agent+T2-rework` | 13 | 27 | `T1-two-agent` → 本规则: 14 |
| `T2-fix+deltaRereviewPASS+auditPASS` | 5 | 5 | — |
| `live-hit(was-IE-ack)` | 18 | 19 | `IE-ack` → 本规则: 1 |
| `C1-manual-PDF+KB` | 3 | 3 | — |
| `C7-K4-rereview` | 2 | 2 | — |

### 2.1 NOT_HOLD (2 条, 都在 PRE_EXISTING 层)

| # | atom_id | 终态 | 审查者结论 (摘) | 原始结果 |
|--:|---|---|---|---|
| 57 | `sv20_p0069_a001` | EXACT | 见下方 N1 | `evidence/t4_supp_raw/pack_2.md:50` |
| 58 | `sv20_p0069_a003` | EXACT | 见下方 N1 | `evidence/t4_supp_raw/pack_2.md:51` |

含义: 这两条是 SDTM v2.0 §6.6 APRELSUB 变量表的 APID / RDEVID 行. KB 该表只有 5 列 (# / Variable / Label / Type / Role), 这 5 格与 PDF 一致; PDF 的 Notes 格文字 KB 本表没有, 06 的旧匹配器把它们配到了 §4 的另一张表上, 所以旧 EXACT 不成立. **不是 KB 写错**: v2.0 变量表只收精简列是 T1.4 R1 用户已裁定的做法; 问题在旧标签.

### 2.2 HOLDS_AS_EQUIV (30 条, 都在 PRE_EXISTING 层; 内容成立, 标签级别偏高)

| 原因 | 条数 | 原子 |
|---|--:|---|
| ML CRF: PDF 用粗体 X 标选中项, KB 写 `[X]` / `[ ]` | 6 | `ig34_p0123_a009`, `ig34_p0123_a010`, `ig34_p0123_a011`, `ig34_p0123_a016`, `ig34_p0123_a017`, `ig34_p0123_a018` |
| 已登记 PDF 笔误造成的差异 (B-BE T-3); 标签宜为 PDF_TYPO | 1 | `ig34_p0147_a025` |
| 同格分行合并 / 填空线长度 (CE CRF p153) | 1 | `ig34_p0153_a0002` |
| PDF 省略列字符 `…` (U+2026), KB 写 `...` (EG Ex3 表, p191) | 19 | `ig34_p0191_a001`, `ig34_p0191_a003`, `ig34_p0191_a005`, `ig34_p0191_a006`, `ig34_p0191_a007`, `ig34_p0191_a008` … |
| 已登记 PDF 笔误造成的差异 (B-MB T-1); 标签宜为 PDF_TYPO | 2 | `ig34_p0262_a016`, `ig34_p0262_a017` |
| 已登记 PDF 笔误造成的差异 (B-NV T-2); 标签宜为 PDF_TYPO | 1 | `ig34_p0296_a023` |

这 30 条在各覆盖率口径里仍算已覆盖 (EXACT 与 EQUIVALENT 同计); 其中 4 条登记笔误的进 `t4_relabel_pending.md` (改 PDF_TYPO 会影响 strict 口径). 其余 26 条归入 "标签级别" 后续项 (同 U-10⑤), 不改.

## 3. Q9 扩检 (PRE_EXISTING 层不通过 → 按 PLAN §9 Q9 升级)

- 范围内、本项目没改过的旧标签 (stock), **不含标题类原子** (G-TB1 的定义就是 "非 HEADING"): 4968 条 = EXACT 1753 / EQUIVALENT 2334 / INTENTIONAL_EXCLUDE 881. 范围内另有 stock 标题类原子 EXACT 149 / EQUIVALENT 167, 不在指纹复验里也不在 Q9 里 (其中 11 条因台账指针跨文档在第二轮 XDOC 层审过, 见 §4).
- 旧 EXACT: `scripts/t3/t3_direct_hit.py` 做的是全量指纹复验 — 原子文字须在它的目标文件里逐字命中并锚在本节. 它检查 1758 条 (上面 1753 条 + 5 条虽在决策表里但标签未变的), 命中不了的 58 条就是 §2 的 PRE_EXISTING 层 (全部审完). **它验不了两件事**: ① 目标文件属于另一份 PDF 的 KB 文件时不做节锚点检查 (`t3_common.py` 的 `anchor_ok` 直接放行), 即不判 "文字落在哪份文档"; ② 原子抽取时把 PDF 的笔误 "顺手改对" 了的, 原子文字 = KB 改正值, 指纹照样命中 — 这两类分别由第二轮的 XDOC 层与 TYPO_SIB 层补 (§4).
- 旧 EQUIVALENT 指纹验不了, 另定方案: SDTM v2.0 的 127 条**全检** (出问题的正是 v2.0 变量表); SDTMIG v3.4 的 2207 条按原子类型分层随机抽 65 条 (seed 20261131).

| 层 | 总体 | 本次审 | HOLDS | NOT_HOLD_R1 | NOT_HOLD | UNVERIFIABLE |
|---|--:|--:|--:|--:|--:|--:|
| Q9_SV20_EQUIV | 127 | 127 | 76 | 49 | 2 | 0 |
| Q9_IG34_EQUIV | 2207 | 65 | 65 | 0 | 0 | 0 |

- **SDTM v2.0**: 127 条里 51 条旧 EQUIVALENT 不成立 — 49 条是变量表行 / 表头 (NOT_HOLD_R1: KB 精简列对, PDF 其它列的内容 KB 本表没收), 2 条是目录条目被跨文档配到了 SDTMIG ch10 (`sv20_p0003_a011` / `a012`). 都不是 KB 内容错.
- **SDTMIG v3.4**: 抽 65 条 0 错 → 错误率 95% 置信上界约 **4.5%** (1 − 0.05^(1/65)). 若把总闸对照层判过的 8 条也算上 (另一个抽样框), 73 条 0 错 → 约 4.0%. 两个数都是近似: 按简单随机算, 实际是按原子类型分层且不按比例. **这不等于全检**; 是否够由主人定.
- NOT_HOLD_R1 按 PDF 页分布: p46 1, p47 1, p52 5, p53 7, p55 8, p56 4, p57 4, p58 6, p59 9, p60 1, p65 1, p69 2.
- 与 Q9 brief 的一处偏离 (收紧, 不是放宽): brief 的后果条款写 "NOT_HOLD_R1 → 台账改标 IE (R1, 用户已 ack 的类别)"; 实际没有直接改, 而是列入待改清单请主人定 — 协调方 2026-11-27 指示 "不按委托代裁处理, 先不改台账" (`t4_coordinator_note_20261127.md`), 且 R1 当时 ack 的是列出的 70 条, 这 51 条不在其中.

## 4. 第二轮补检 (独立审查 B 指出的三处没覆盖到)

| 层 | 取法 | 本次审 | 结果 |
|---|---|--:|---|
| XDOC | 范围内 stock EXACT / EQUIVALENT (含标题类) 且台账 `md_atom_ids` 只指向另一份文档的 KB 文件; 这一筛法筛出 57 条 (与第 1 稿的 "57 条待改" 只是数字相同, 无关), 其中 30 条已在 Q9 / 补检审过 | 27 (全检) | HOLDS 24 / NOT_HOLD_XDOC 0 / NOT_HOLD_R1 0 / NOT_HOLD 3 / UNVERIFIABLE 0 |
| TYPO_SIB | 范围内 EXACT / EQUIVALENT, 与某条 "KB 写正确值" 登记同页 (±1), 原子文字含改正值且与登记所在 KB 行重合 ≥ 0.8; 候选 70 条, 其中 7 条已审过 | 63 (全检) | TYPO_AFFECTED 10 / NOT_AFFECTED 53 / NOT_HOLD 0 / UNVERIFIABLE 0 |
| TYPO_SIB2 | 同上但原子文字**不含**改正值, 只取 EQUIVALENT (EXACT 须逐字命中 KB, 覆盖笔误处的 EXACT 原子必含改正值); 候选 40 条 | 40 (全检) | TYPO_AFFECTED 5 / NOT_AFFECTED 35 / NOT_HOLD 0 / UNVERIFIABLE 0 |
| PDF_TYPO | (第二轮当时, R2L 之前) 终态 PDF_TYPO 149 条里未被任何审查者看过的 144 条, 按判定规则分层各抽 15 (seed 20261132) | 45 (抽样) | HOLDS 45 / NOT_HOLD 0 / UNVERIFIABLE 0 |

- **XDOC**: 没有跨文档误配 — 16 条 SDTMIG 非标题原子与 8 条标题原子的内容都在 SDTMIG 自己的 KB 文件里 (台账指针指向 model/ 只是旧匹配器的指针问题). 3 条 NOT_HOLD 都是标题类, 属口径问题而非内容问题: `ig34_p0079_a001` (5.3 SE) 与 `ig34_p0442_a001` (9.2 OI) — KB 域文件标题 `# XX — 域名` 不带 PDF 节号; `ig34_p0441_a006` (9.1 Device Identifiers) — KB 对应标题是自拟的 `## DI – Description/Overview (§9.1)`. 审查者指出 64 个域目录里 57 个同型. 标题类不在 G-TB1 范围内; 口径交主人定 (`t4_owner_decisions_round2.md`).
- **TYPO_SIB / TYPO_SIB2**: 15 条原子所在处 PDF 印的是已登记的笔误、KB 是改正值, 现标签 EXACT / EQUIVALENT 不准 → 进待改清单 (改 PDF_TYPO). 其余候选的笔误实际在同页别处.
- **PDF_TYPO**: 抽 45 条 0 错 → 错误率 95% 上界约 6.4% (同样是近似). 连同总闸样本里判过的 5 条共 50 条看过; PDF_TYPO 类**不是全检**. attempt 1 要求的 "ATOM_ERR / PDF_TYPO 合计补抽到 ≥ 30" 现为: ATOM_ERR 侧 C7 38 + triage 74 + K4 2 全检, PDF_TYPO 侧抽 45.
- **TYPO 筛法的盲区 (delta 复审 M5; 如实)**: ① 只按登记的 `pdf_page` ±1 取原子, 而有些登记实际跨多页 (页段写在 `pdf_value` / `basis` 的文字里); ② 与 KB 行比重合度时只用登记给的行号; ③ TYPO_SIB2 不收 EXACT. delta 复审者另用 "PDF 笔误写法的 token 在全 KB 不存在" 做全量反查, **范围内没有找到漏掉的原子**, 但 195 条 "KB 写正确值" 登记里有 73 条 (空格 / 标点类笔误) 抽不出可用 token, 测不了. 主控用更宽的筛法 (改正值在 KB 的所有出现行都算) 重筛: 范围内另有 169 条候选、范围外 142 条候选, **都没有审** (宽筛法噪声大; 是否审交主人定).
- **范围外的已登记笔误同类原子 (delta 复审 H4)**: 第二轮 TYPO 层只取了范围内. delta 复审者在文本层 (未看渲染页) 确认范围外有 6 条同类: `ig34_p0083_a020` (S-SPREL SE T-1, 现 EXACT)、`ig34_p0304_a026` ~ `a029` (B-OE T-2, 现 EQUIVALENT)、`ig34_p0316_a023` (S-FND PE T-1, 现 EQUIVALENT). 上一轮 U-8 把范围外同类的 4 条改成了 PDF_TYPO. 这 6 条在第二轮时未经 tracer 审, 未进待改清单, 交主人定 (一页问题 7); 后续: 主人选 7b = A, 第三轮审查者对渲染页逐条确认, 已并入清单 (见下一节).
- 范围外 (只列不审): 台账指针跨文档的旧标签另有 146 条在 §5.0 范围外 (PARTIAL 113 / EQUIVALENT 21 / EXACT 12), 其中 SDTM v2.0 第 74 页 14 条已被 Q9 审查者指认为配到了 SDTMIG 附录 F. 清单 `work/t4/round2/round2_population.json` 的 `xdoc_out_of_scope`.

## 4b. 第三轮补检 (主人 2026-11-27 选定的追加审查: 4a = B / 4b = B / 4c = B / 7b = A)

口径 `subagent_prompts/t4/t4_supp_round3_v1.0.md`; 样本 `work/t4/round3/round3_sample.jsonl` (md5 `9eeb5b78863e2caf34da34c6c90a5528`; seed 20261133); 原始结果 `evidence/t4_round3_raw/` (tracer ×13).

| 层 | 取法 | 本次审 | 结果 |
|---|---|--:|---|
| R3_IG34_EQUIV | SDTMIG 旧 EQUIVALENT (范围内, 非标题) 未审的 2046 条里按原子类型比例抽 150 | 150 (抽样) | HOLDS 150 / TYPO_AFFECTED 0 / NOT_HOLD 0 / UNVERIFIABLE 0 |
| R3_PDF_TYPO | 终态 PDF_TYPO 里此前没人审过的全部 99 条 | 99 (全检) | HOLDS 94 / **NOT_HOLD 4** / **UNVERIFIABLE 1** |
| R3_HEADING | 范围内 stock 标题类 (EXACT / EQUIVALENT) 未审的 305 条里按比例抽 60 | 60 (抽样) | HOLDS 55 / HOLDS_AS_EQUIV 5 / NOT_HOLD_SELF 0 / NOT_HOLD 0 / UNVERIFIABLE 0 |
| R3_XTYPO | delta 复审者在文本层指出的范围外 6 条 | 6 (全检, 看渲染页) | TYPO_AFFECTED 6 / NOT_AFFECTED 0 / NOT_HOLD 0 / UNVERIFIABLE 0 |

- **SDTMIG 旧 EQUIVALENT**: 两次随机抽样合计 215 条 (65 + 150) 0 错 → 错误率 95% 置信上界约 1.4% (近似: 分层抽样按简单随机算). 另有 16 条跨文档指针的全检 0 错. 仍**不是全检**: 范围内这类标签共 2207 条.
- **PDF_TYPO**: 至此 (R2L 之前) 终态 PDF_TYPO 149 条全部经独立审查者看过 (总闸样本 5 + 第二轮 45 + 第三轮 99); R2L 新进入 PDF_TYPO 的 25 条本身就来自第二轮 / 第三轮审查者逐条判的 TYPO_AFFECTED, R2L 后共 174 条, R3L 后 170 条. 结果: 4 条**多标** — `ig34_p0412_a006`; `ig34_p0412_a007`; `ig34_p0412_a008`; `ig34_p0413_a010` — 登记的笔误 (`S-TDM TD T-1` / `T-4`) 其实在相邻原子 / 另一张表头里, 这 4 条自己的 PDF 原文没有笔误, KB 与 PDF 逐字一致, 标签应为 EXACT. (`t3_recompute.md` 早就记过 "S-TDM TD T-1 有 2 条可能多标".) 这是标签方向与问题 3 相反的新发现 (改回 EXACT 对 U-1 B 口径无影响, strict 口径 +4 条); 当时待主人定, 主人后来选 A1 (消息 4), 已由 R3L 批改回 EXACT.
- **判不了的 1 条**: `ig34_p0293_a038` (登记 `B-MK T-2`: PDF 写 "REPLACEMENT/ SURGICAL" 多一个空格). 该处正好是表格单元格折行 (`pdftotext -bbox`: "REPLACEMENT/" 与 "SURGICAL" 在上下两行), 文本层与渲染页都无法判定有没有空格; 登记自己也注了 "折行歧义而非确证印刷错". KB 写 "REPLACEMENT/SURGICAL", 两种情况下内容都没错; 悬而未决的只是标签 (PDF_TYPO 还是 EXACT). 按 brief 该层因此**不算全通过**.
- **标题类**: 60 条内容全部成立, 无 KB 自拟标题、无缺节. 5 条 HOLDS_AS_EQUIV = PDF 标题 "X – Examples" 用 en dash, KB 文件首行 `# X — Examples` 用 em dash (标 EXACT 的应为 EQUIVALENT; 标签级别后续项). 连同第二轮 11 条, 标题类共审 71 / 316.
- **范围外笔误同类 6 条**: 全部对渲染页确认 (`S-SPREL SE T-1` 1 条 / `B-OE T-2` 4 条 / `S-FND PE T-1` 1 条) → 按主人 7b = A 并入改台账.
- 第三轮审查者顺带记的事项: p220 "at runtime to for measuring" 疑似 PDF 多一个词, 未登记, KB 照录 (`CP/examples.md:305`; `pack_2.md`); `TS/assumptions.md` NullFlavor 表与 `TA/assumptions.md:94` 有 KB 自拟的表头 / 标题 (`pack_6.md` / `pack_12.md`); 登记文字不准或前后矛盾: `B-CP T-3`、`S-SPC1 CP T-16a` (漏记一处未闭合引号)、`S-SPC2 N-1` / `N-2`、`B-NV N-1` / `N-2` 的 `basis` 写 "照录" 而 `handling` 是 "KB 写正确值" (`pack_8.md` / `pack_9.md`); 决策表登记指针应补: `ig34_p0355_a027` 与 p356 第 27 行原子补 `B-TR T-1`, 另有 3 条漏列第二个登记 id (`pack_8.md`); `MH/assumptions.md:27` 闭引号方向 (U-9(b) 已定照录; `pack_7.md`). `pack_4.md` 说 `CP/spec.md` 缺规格表脚注 — 主控核实为误报 (脚注在 `CP/spec.md:564`, 原子 `ig34_p0204_a013` 标 EXACT 成立).

## 5. 后果 (按派发前写死的条款)

- PRE_EXISTING 层 NOT_HOLD ≥ 1 → Q9 升级已触发并执行到 §3 / §4; **主控不自行结案**. 需要主人定的事列在 `t4_owner_decisions_round2.md`.
- 待改标签共 82 条, 逐条清单与各选法下的闸数字 (在台账副本上算) 见 `t4_relabel_pending.md`. 这些都是闸口径层面的事, 须主人本人定 (总闸 attempt 2 C 项; 协调方指示); PDF_TYPO 每条须用户 ack (G-TB1). **主人 2026-11-27 在主控聊天里直接定了全部 82 条** (原话 `t4_owner_confirmation.md` 第二轮一节): 先定 78 条 (消息 2), 由 R2L 批落到台账 (`60729f7b…` → `16024ac0…`); 那 4 条多标的 PDF_TYPO 第一次问时未答 (消息 3), 总闸 attempt 3 把它判为唯一挡闸项后再问, 主人答 A1 (消息 4), 由 R3L 批改回 EXACT (`16024ac0…` → `43809870…`). 两批清单外标签变化都是 0. 判不了的 1 条 (`ig34_p0293_a038`) 主人答 B1: 维持 PDF_TYPO, 写明 "折行处无法判定有没有空格".
- 补检其余 9 个非空层 (145 条) 通过: FIG 11、triage ATOM_ERR 74、RELOCATE 3、六条规则类 57.

## 6. 审查者顺带记录的事项 (都不改 KB; KB 冻结)

需要定口径的 (已并入给主人的一页):
- 标题后缀: Q9 包 1 的 Q19-Q26 (8 条 v2.0 目录条目) KB 标题带 `(TE)` 等域代码后缀, 审查者按 "附加信息不改原意" 判 HOLDS 并提醒 "若任何附加都算标题文字不同, 这 8 条要改判" (`evidence/t4_q9_raw/pack_1.md`). 主控依据: U-10① 已定 "(XX) 后缀为保留的检索导航, 只补登记" (`t4_user_decisions.md` §000), 维持 HOLDS.
- 域标题不带节号 / DI 自拟标题: 见 §4 XDOC.
- `sv20` §6.4 RELSUB / §6.5 DR 的 KB 表也只有 5 列, PDF 对应表有 C-code 与 Definition 格 (`evidence/t4_supp_raw/pack_2.md` 样本外发现; 审查者写 "需要 owner 定口径"). 与 R1 同类; 这两节不在 §5.0 范围内.
- KB 排版: `knowledge_base/domains/EG/examples.md:62-87` (Ex3 表) 省略列写 `...`, PDF p190-191 是 `…` (U+2026). 这 26 行在 S-TYPO 残余清单里归类 `table_elision` (`work/t2_batches/S-TYPO.residual.jsonl`; 全表 1091 行 = kb_nav 685 / body 235 / heading 144 / table_elision 26 / kb_note 1). 这 26 行 = EG 例 3 表 25 行 (`:62`, `:64-87`; `:63` 是表格分隔线) + `knowledge_base/domains/RE/examples.md:15` 1 行 (同样是表头用 `...` 表示省略列). U-9(c) 当时说的是 "残余 230 行", 与文件行数对不上, **不能确认 U-9(c) 的 "接受现状" 覆盖这 26 行**. 受影响的 19 条 p191 原子现标签仍是 EXACT (审查者判 HOLDS_AS_EQUIV, 即按定义应为 EQUIVALENT; 归标签级别后续项, 未改).

PDF 自身不一致 (前两条未登记):
- sv20 p69 SREL 行 Notes 写 "subject or pool identified in RDEVID", p50 同句写 "device" (`evidence/t4_q9_raw/pack_5.md`).
- ig34 p440 图中 SPC-003 标 "(Brain)", 同页表写 TISSUE (`evidence/t4_supp_raw/pack_6.md`).
- ig34 p277 叙述 / p278 Method B 表: 叙述说第 14-26 行 RELID 为 2 / `DY8DRGX`, 表里这些行印 RELID 1, 第 26 行 IDVARVAL 印 `DY1DRGX` (`evidence/t4_round2_raw/pack_sib_3.md`). 这一处**已登记**: `t4_user_decisions.md` A1-20 / `B-PCPP T-4` (照录 + T4), 不是新发现.
- 登记页号: `B-CP T-5` 的 `pdf_page` 写 211, 该行实际在 p212 (`pack_sib2_1.md`); `B-IS T-6` 写 241 实为 239 (解冻轮 W1 已发现). 都留到改台账那一批更正.

台账 / 登记的指针类 (不影响标签):
- 若干 `md_atom_ids` 指向别的域 / 文件 (如 `ig34_p0153_a0009` → DM; `ig34_p0255_a036` → MS examples; XDOC 层 27 条); 原子页号偏一页 (`ig34_p0169_a0025` 等实在 p170; `ig34_p0057_a001` 实在 p56; `ig34_p0442_a001` 实在 p441).
- `ig34_p0355_a027` (PDF_TYPO): 决策表登记指针只列 `B-TR T-3`, 漏 `B-TR T-1` (`evidence/t4_round2_raw/pack_typo_2.md`). `chapters/ch08_relationships.md:228` 也承载了 `B-SUPPQUAL T-1` 的改正值, 登记的位置清单没列这一行 (`pack_sib_3.md`).
- 登记 `S-CH4 T-10e` (p43 两句之间缺空格) 落在 `ig34_p0043_a022` 与 `a023` 的交界; 仅空白差异; 审查者判 `a022` NOT_AFFECTED 并提示 "若从严, 受影响的可能是下一个原子"; `a023` 未经审查者看, 主控按 "EXACT 允许空白归一" 认为两条都成立 (`pack_sib_1.md` R29; 同页 `S-CH4 T-10d` 的相邻原子同理).
- 样本包里的 KB 指针多处近似, 审查者都自行重新定位.

标签级别 (内容成立; 记后续, 同 U-10⑤):
- 旧 EXACT / EQUIVALENT 实为 "原子抽错 + KB 与 PDF 一致" (按定义更接近 ATOM_ERR): 补检 PRE_EXISTING 层 #3、#4、#11-#16、#19-#26、#46-#48、#51、#53 (见 `evidence/t4_supp_raw/pack_1.md` / `pack_2.md` 各行说明); Q9 的 `ig34_p0057_a006`、`ig34_p0068_a004` 及包 6 的 Q132-Q135、Q146; 第二轮 `pack_sib_2.md` 附注的 8 条 (R55 / R56 / R59 / R60 / R63 / R64 / R66 / R75)、`pack_sib_1.md` 的 R34 / R43 / R50、`pack_sib2_1.md` 的 S8 / S10 / S15 / S17 / S19 (审查者: "S8 更贴切的标签是 ATOM_ERR, 请定")、`pack_sib2_2.md` 的 S21 / S22 / S23 / S27 (审查者: "是否进入标签级别后续项由你决定")、`pack_sib_3.md` 提到的 `ig34_p0147_a024` / `a025`; delta 复审者另指出 `ig34_p0280_a045` (未审; 原子写 `DYIDRGX_A`, PDF 与 KB 都是 `DY1DRGX_A`). 主控处理: 一律记标签级别后续项, 不在本轮改 (与 U-10⑤ 同).
- 范围内 sv20 标题类旧 EQUIVALENT 共 5 条: 3 条在 XDOC 层审过 (成立); `sv20_p0052_a010`、`sv20_p0054_a001` 两条没有审 (台账指针不跨文档, 不在任何一层的取法里).
- 原子抽取本身的问题 (只影响台账, KB 对): p69 原子 a023-a032 把两张 se.xpt 的值混在一起、p77 原子 a015-a018 把 dm.xpt 抽成 suppdm (`evidence/t4_supp_raw/pack_3.md`); `sv20_p0053_a018` 把 Notes 文字放进 Definition 格 (`evidence/t4_q9_raw/pack_3.md`).
- KB 附加信息: `CE/spec.md:261,279`、`HO/spec.md:81` 的受控术语格比 PDF 多写了 NCI C-code (`evidence/t4_supp_raw/pack_4.md`; S-CT 批 U5/U6 的做法, 各 spec.md 有统一 KB note, 这三格是否在其覆盖内待核).

<!-- REVIEW: 以下由主控手写 / 誊录, 脚本重跑时原样保留 -->

## 独立审查 B 的处理 (主控手写; 审查原文 `evidence/t4_gap_review_raw/review_b.md`)

审查者 `oh-my-claudecode:code-reviewer` (opus), 对象 HEAD `1df9f60` 的第 1 稿. 结论 **CONDITIONAL, HIGH 4**; 数字与 395 条逐条判定全部复现. 逐条处理:

| # | 严重度 | 审查意见 (摘) | 处理 |
|--:|---|---|---|
| 1 | HIGH | 漏报同类原子 `ig34_p0147_a026` (B-BE T-3); PRE_EXISTING 层看不见 "原子文字 = KB 改正值 ≠ PDF" | 采纳. 按建议做了反查: 第二轮 TYPO_SIB 63 条 + TYPO_SIB2 40 条由独立审查者全检 (§4), 确认 15 条 (含 a026), 连同原 4 条共 19 条进待改清单; §3 写明指纹复验验不了这一类 |
| 2 | HIGH | 给主人一页的 "第 74 页 3 条" 实为 14 条; "不影响任何一道闸" 与给出的数字自相矛盾; U-8 不是 "同类" | 采纳. 一页重写 (问题 7): 范围外跨文档指针共 146 条 (第 74 页 14 条); 写明不在 G-TB1 / G-TB2 范围内但进 G-TB3; 各选法实算; U-8 的说法改为 "上一轮范围外的 4 条已登记笔误是改了标签的" |
| 3 | HIGH | 确认来源多写了 "主人对协调方说过会去发 / 时间线吻合" | **不采纳为事实错**: 这两点在协调方消息原文里有, 是主控给审查者的 brief 漏给了. 已把协调方原文留档 `t4_coordinator_note_20261127.md` (注明是转达), 各文档改为引用该留档 |
| 4 | HIGH (把握中等) | "SDTMIG 没有 v2.0 那种结构性原因" 不成立: 16 条 SDTMIG 旧 EQUIVALENT 的台账指针指向 model/, 抽样没抽到 | 采纳. 该句已删. 这 16 条连同 11 条标题类 (共 27 条) 作 XDOC 层全检 (§4): 无跨文档误配, 3 条标题口径问题交主人 (一页问题 6) |
| 5 | MEDIUM | 置信上界合并了 gate 8 条, brief 要求报 65 条的 | 采纳. §3 与一页都先报 65 条的 4.5%, 再注 73 条的 4.0%, 并写明是近似 (分层抽样按简单随机算) |
| 6 | MEDIUM | 没写明总体不含 HEADING; 指纹复验不查 "落在哪份文档"; 1753 vs 1758 | 采纳. §3 写明; 标题类 316 条未查列为一页问题 4c; 范围内 sv20 标题 3 条已在 XDOC 层审 (成立) |
| 7 | MEDIUM | PDF_TYPO 149 条里 142 条没人看过, 没写明 | 采纳. 第二轮分层抽 45 条 (0 错, §4); 写明不是全检; 是否全看列为一页问题 4b |
| 8 | MEDIUM | 审查者的 "需复议" 没转述 (Q19-Q26 标题后缀; §6.4 / §6.5 五列表) | 采纳. §6 补上并写明依据 |
| 9 | MEDIUM | M-4 写成 "待追认", 与确认记录不一致; §000b 标题过时 | 采纳. `t4_ack_lists.py` / `t4_ack_lists.md` / `t4_user_decisions.md` §000b 已改为 "M-1 ~ M-7 按 `t4_owner_confirmation.md` 的记录已追认, M-8 待追认" |
| 10 | MEDIUM | 两份文档选项不一致; 目录条目应单独成问; 预测性措辞; "未单独算" 可算 | 采纳. 一页重写: 变量表行 / 目录条目 / 笔误原子各成一问; 选项只在一页里写, `t4_relabel_pending.md` 只列组与数字; 各选法数字由脚本实算 (`work/t4/supp/scenarios.json`); 删去 "总闸会再点名" |
| 11 | LOW | "其余 10 层" 应为 9 | 已改 (失败归档 / HANDOFF / audit_matrix / 本文件) |
| 12 | LOW | `relabel_pending` 的 G-TB2 标注错 | 已改: 表头写明是字面口径, 并注范围内口径 174/174 |
| 13 | LOW | 标签级别项列得不全; 几条审查者观察没转述 | 采纳. §6 补全 |
| 14 | LOW | 没写明偏离 Q9 brief 的后果条款; "PLAN §3.1 B5" 引用不当 | 采纳. §3 末条写明偏离 (收紧) 及原因; 不再引 B5 |
| 15 | LOW | 失败归档的输入 HEAD 应为 `c555bd8` | 已改 |
| 16 | LOW (待核) | "EG 省略号已由 U-9(c) 定" 无法确认; LOCATE 的原因写错 | 采纳. 核实: 残余清单 1091 行, EG 那 26 行归 `table_elision`, 与 U-9(c) 的 "230 行" 对不上 → 改为单独问主人 (一页问题 8); LOCATE 行改为 "28 条按 `ruling:LOCATE-LB` 转 REAL_GAP" |

改动后的文档 (本文件、`t4_relabel_pending.md`、`t4_owner_decisions_round2.md` 第 2 稿等) 由同类型的新审查实例做了 delta 复审, 见下.

## delta 复审 C 的处理 (主控手写; 审查原文 `evidence/t4_gap_review_raw/review_c.md`)

审查者 `oh-my-claudecode:code-reviewer` (opus, 新实例), 对象 HEAD `1b30197` 的第 2 稿. 结论 **CONDITIONAL, HIGH 4 / MEDIUM 5 / LOW 13**; 第二轮 175 条判定、72 条清单、9 行各选法数字全部独立复现; D 项 (待改 72 条) PASS, F 项 (未确认写成已确认) PASS. 逐条处理:

| # | 严重度 | 审查意见 (摘) | 处理 |
|---|---|---|---|
| H1 | HIGH | 标题类原子其实计入 G-TB3; 一页写成 "不在任何一道闸的范围内" | 采纳. 一页问题 4c / 6 改为 "不在 G-TB1 范围内, 但计入 G-TB3"; 4c 的建议由 A 改为 B |
| H2 | HIGH | 问题 6 选项 A 的理由 "节号在各节小标题里已有" 不成立 | 采纳. 删去; 改写为事实 (64 个域目录里 44 个任何标题都不带 PDF 节号; 主控复算一致) |
| H3 | HIGH | 问题 8: 那 19 条现标签是 EXACT 不是 "等价"; 26 行 = EG 25 + RE 1, 漏了 `RE/examples.md:15` | 采纳. 一页问题 8 与本文件 §6 已改 |
| H4 | HIGH | 范围外的已登记笔误同类原子没筛没报 (文本层确认 6 条) | 部分采纳. 6 条与范围外候选数写进本文件 §4 与一页问题 7b, 各选法数字实算 (`scenarios.json` 的 `all_xtypo`); **没有**先派独立审查逐条确认 — 范围外是否花这个工夫交主人定 (7b 选项 A / B / C). 这 6 条未进待改清单 |
| M1 | MEDIUM | 第二轮标签级别附注没转述全 | 采纳. §6 补全 (含审查者的 "请定" 原话与 `ig34_p0280_a045`); 一页的 "约 60 条" 改 "约 80 条" |
| M2 | MEDIUM | 问题 9 第 1 处 "KB 都是照 PDF 原样录" 不准 | 采纳. 改为 "p69 那句 KB 没收, p50 那句照录", 并注与问题 1 选 B 的关系 |
| M3 | MEDIUM | 问题 6 没给条数与数字影响 | 采纳. 主控数得域级标题原子 62 条, 现标 EQUIVALENT 39 条 (范围内 21); 从严降为 PARTIAL 时 U-1 B 不变、内容指标 90.6247% → 90.2166% (在三组都改的副本上实算); 一页加选项 C |
| M4 | MEDIUM | 问题 7 的区间默认配错的都记 IE | 采纳. 一页 7a 与 `t4_relabel_pending.md` §2 写明假设及两种例外情形 |
| M5 | MEDIUM | 范围内 TYPO 筛法有盲区, 结论只能算待核 | 采纳为如实披露: §4 写明三处盲区、复审者的反查结果与 73 条测不了; 主控宽筛得范围内 169 / 范围外 142 条候选未审; 是否再查列为一页问题 4d. **没有**追加审查 |
| L1 | LOW | `t4_t0_refresh.md` 的 "问题 4" 应为 "问题 5" | 已改 |
| L2 | LOW | T-10e 相邻原子 "按定义成立" 是主控判断 | 已改写 (§6) |
| L3 | LOW | 待改清单里 B-PCPP T-2 / T-3 应写确定的 id | 已改: 脚本从审查者原始结果该行读出确认的 id (15 条各 1 个, 断言唯一) |
| L4 | LOW | PDF_TYPO 实际看过 51 条 | 一页 4b 加注 (第 51 条只经 AI 预筛, 不计) |
| L5 | LOW | 未建议选项后的评价括注有诱导之嫌 | 已改: 评价移到建议项并标 "主控的理由" |
| L6 | LOW | "您上一轮确认的" 未带 "按记录" 限定 | 已改 |
| L7 | LOW | 问题 5 没提 M4d0 / M4d 的变化 | 已补 |
| L8 | LOW | p278 的叙述实在 p277 | 已改 |
| L9 | LOW | XDOC 的 "57 条" 与第 1 稿的 "57 条待改" 同数易混 | 已加注 |
| L10 | LOW | `audit_matrix.md` "同页同行" 不准 | 已改 |
| L11 | LOW | 范围内 sv20 标题类 EQUIVALENT 5 条里 2 条没交代 | §6 写明: `sv20_p0052_a010`、`sv20_p0054_a001` 未审 |
| L12 | LOW | M-7 的更正发生在主人确认之后 | `t4_user_decisions.md` M-7 行已注 |
| L13 | LOW | 协调方留档是主控自己誊录的 | 留档状态行已写明这一局限 |

**这次处理后的第 3 稿没有再送审** (再审下去每轮都会有新的 LOW; 改动都是照复审者给的改法做的). 留给总闸 attempt 3 的独立审查者一并看.
