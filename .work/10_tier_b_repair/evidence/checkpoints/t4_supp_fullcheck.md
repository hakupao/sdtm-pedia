# T4.1 补检 ("0 抽中" 各类全检) + Q9 扩检 — 汇总

<!-- chain: E (plans) -->
> 状态: **补检 PRE_EXISTING 层不通过 (2 条 NOT_HOLD) → 触发 Q9 升级; Q9 扩检已跑完, 结论待主人裁定** (2026-11-27). 其余各层通过. KB 未改; 台账未改.
> 审查: `oh-my-claudecode:tracer` (opus) × 16 个独立实例 (补检 8 + Q9 8), 只读; 原始结果由审查者自己写入 `evidence/t4_supp_raw/pack_{1..8}.md` 与 `evidence/t4_q9_raw/pack_{1..8}.md`. 本文件是主控用 `scripts/t4/t4_supp_report.py` 从原始结果机械汇总的, 不改判 (规则 D).
> 口径 (派发前写死): `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md`, `subagent_prompts/t4/t4_q9_extension_v1.0.md`. 规则 B 归档: `evidence/failures/step_T4.SUPP_attempt_1.md`.

## 1. 复跑

```bash
T=.work/10_tier_b_repair
python3 -I $T/scripts/t3/t3_direct_hit.py --out $T/work/t4/supp/direct_hit_head.json   # pre_existing 58 (GREEN)
python3 -I $T/scripts/t4/t4_supp_sample.py   # 203 条 / 8 包; 不触碰 gate / human 样本文件
python3 -I $T/scripts/t4/t4_q9_sample.py     # 192 条 / 8 包 (seed 20261131)
python3 -I $T/scripts/t4/t4_supp_report.py   # 本文件 + t4_relabel_pending.md (台账只读)
```
- 样本 md5: `work/t4/supp/supp_sample.jsonl` `0fb5799b821c5a4dc900b39fbf86bf86`; `work/t4/q9/q9_sample.jsonl` `5ad82bea9a68db72616a19f414afd5de`. 总闸 / 人工样本文件未动 (`gate_sample.jsonl` `67b1013f496096df483eb300a66150d6`, `human_sample.jsonl` `5b4212ee6b5deb873ab29d7f13e17232`).

## 2. 补检: 总体与结果 (全检, 不抽样)

总体取自 HEAD 的台账与决策表; 一个原子只进它命中的第一层; 已被总闸审查者判过的 (gate 84 条) 与 U-5 C7 全检过的 (38 条) 不重复审.

| 层 | 终态 | 总体 | 已在 gate 样本 | 本次审 | HOLDS | HOLDS_AS_EQUIV | NOT_HOLD | UNVERIFIABLE | 层结论 |
|---|---|--:|--:|--:|--:|--:|--:|--:|---|
| PRE_EXISTING | EXACT | 58 | 0 | 58 | 26 | 30 | 2 | 0 | **不通过** |
| FIG | FIGURE_DEFERRED | 11 | 0 | 11 | 11 | 0 | 0 | 0 | 通过 |
| TRIAGE_ATOM_ERR | ATOM_ERR | 74 | 0 | 74 | 74 | 0 | 0 | 0 | 通过 |
| TRIAGE_RELOCATE | EXACT | 3 | 0 | 3 | 3 | 0 | 0 | 0 | 通过 |
| TRIAGE_LOCATE | — | 0 | 0 | 0 | — | — | — | — | 总体为空 (T1 的 LOCATE 类在 T2 已全部定位) |
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

这 30 条在各覆盖率口径里仍算已覆盖 (EXACT 与 EQUIVALENT 同计); 其中 4 条登记笔误的见 `t4_relabel_pending.md` (改 PDF_TYPO 会影响 strict 口径). 其余 26 条归入 "标签级别" 后续项 (同 U-10⑤), 不改.

## 3. Q9 扩检 (PRE_EXISTING 层不通过 → 按 PLAN §9 Q9 升级)

- 范围内、本项目没改过的旧标签 (stock) 共 4968 条: EXACT 1753 / EQUIVALENT 2334 / INTENTIONAL_EXCLUDE 881.
- 旧 EXACT: 已由 `t3_direct_hit.py` 全量指纹复验, 命中不了的 58 条就是上面的 PRE_EXISTING 层 (全部审完). Q9 写的 "全量指纹复验" 对 EXACT 已做完.
- 旧 EQUIVALENT 指纹验不了, 另定方案: SDTM v2.0 的 127 条**全检** (出问题的正是 v2.0 变量表); SDTMIG v3.4 的 2207 条按原子类型分层随机抽 65 条 (seed 20261131; 另有 8 条已在总闸对照层判过, 全成立).

| 层 | 总体 | 本次审 | HOLDS | NOT_HOLD_R1 | NOT_HOLD | UNVERIFIABLE |
|---|--:|--:|--:|--:|--:|--:|
| Q9_SV20_EQUIV | 127 | 127 | 76 | 49 | 2 | 0 |
| Q9_IG34_EQUIV | 2207 | 65 | 65 | 0 | 0 | 0 |

- **SDTM v2.0**: 127 条里 51 条旧 EQUIVALENT 不成立 — 49 条是变量表行 / 表头 (NOT_HOLD_R1: KB 精简列对, PDF 其它列的内容 KB 本表没收), 2 条是目录条目被跨文档配到了 SDTMIG ch10 (`sv20_p0003_a011` / `a012`). 都不是 KB 内容错.
- **SDTMIG v3.4**: 抽 65 条 0 错; 连同总闸对照层的 8 条共 73 条 0 错. 0 错时错误率的 95% 置信上界约 4.0% (按 1 − 0.05^(1/n), n = 73; 假设简单随机, 实际是分层抽). **这不等于全检**; 2207 条是否全检由主人定 (按每包 26 条约需 85 个审查实例).
- NOT_HOLD_R1 按 PDF 表分布: p46 1, p47 1, p52 5, p53 7, p55 8, p56 4, p57 4, p58 6, p59 9, p60 1, p65 1, p69 2.

## 4. 后果 (按派发前写死的条款)

- PRE_EXISTING 层 NOT_HOLD ≥ 1 → Q9 升级已触发并执行到 §3; **主控不自行结案**. 需要主人定的事列在 `t4_owner_decisions_round2.md`.
- 待改标签共 57 条, 逐条清单与改后各闸数字 (在台账副本上算) 见 `t4_relabel_pending.md`. **台账现在没改** (md5 仍 `60729f7b…`): IE 要逐条清单经用户 ack 才生效 (PLAN B5), PDF_TYPO 每条要用户 ack (G-TB1).
- 其余各层 (145 条) 通过: FIG 11、triage ATOM_ERR 74、RELOCATE 3、六条规则类 57.

## 5. 审查者顺带记录的事项 (都不改 KB; KB 冻结)

- KB 观察 (排版): `knowledge_base/domains/EG/examples.md:62-87` (Ex3 表) 省略列写 `...`, PDF p190-191 是 `…` (U+2026). S-TYPO 闭表含 `...`↔`…`, 该文件有 48 行在残余清单 (`work/t2_batches/S-TYPO.residual.jsonl`; U-9(c) 代裁 "接受现状").
- PDF 自身不一致, 未登记: sv20 p69 SREL 行 Notes 写 "subject or pool identified in RDEVID", p50 同句写 "device" (`evidence/t4_q9_raw/pack_5.md`); ig34 p440 图中 SPC-003 标 "(Brain)", 同页表写 TISSUE (`evidence/t4_supp_raw/pack_6.md`).
- 范围外旧标签同类错配 (未改, 只记): `sv20_p0074_a001` (PARTIAL) / `a002` / `a003` (EXACT) 被配到 SDTMIG `ch10_appendices.md` 的 Appendix F (`evidence/t4_q9_raw/pack_2.md`).
- 台账指针类 (不影响标签): 若干 `md_atom_ids` 指向别的域 / 文件 (如 `ig34_p0153_a0009` → DM; `ig34_p0255_a036` → MS examples); 原子页号偏一页 (`ig34_p0169_a0025` 等实在 p170; `ig34_p0057_a001` 实在 p56). 样本包里的 KB 指针多处近似, 审查者都自行重新定位.
- 标签级别 (内容成立): `ig34_p0057_a006`、`ig34_p0068_a004` (旧 EQUIVALENT, 实为原子抽错 + KB 逐字); 补检 #3 / #4 (旧 EXACT, 实为原子抽错).

