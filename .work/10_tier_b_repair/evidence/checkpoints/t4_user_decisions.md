# T4 用户裁定汇总 (O25)
> 状态: **已代裁 (委托代裁, 非主人逐条裁定)** 2026-11-27 — 见下方 §000; §00 表 "用户选" 列保持空白 (那一列留给主人本人). 原稿: 主控 T4 整理 2026-11-27; T2S.REG executor 草拟 2026-11-26. 确认层级 (2026-11-27 接手主控整理, 各层分开记, 互不替代): ① §000 = 协调 bot 受托代裁; ② T4.2 口径与 6 条判定 = 经协调方转达的主人选择 (`t4_human_verdicts.md`); ③ `t4_owner_confirmation.md` (提交 `c555bd8`) = 上一任主控会话 (T4 attempt 2) 记录的 "主人在该会话直接输入「确认」并四项全选: U-1 口径 / T4.2 方案 / 追认 M-1..M-7 / §000 全部". 接手主控与协调方都没有在别处再看到那条原文; 协调方 2026-11-27 说明其依据 = 时间线 + 主人对协调方说过 "可以, 我去发" + 该记录 (协调方消息原文留档 `t4_coordinator_note_20261127.md`; 是转达), 并指示以该记录为准往下走、局限 (一个词加多选勾选, 无截图) 照其自述保留; 是否足够由总闸 attempt 3 判断. ④ 第二轮待主人本人回答的事 (72 条待改标签 / 几处抽查是否够 / M-8 / 域标题口径 / 范围外 146 条 / EG 省略号 / 两处补登记) 在 `t4_owner_decisions_round2.md`, **不按委托代裁处理**.
> 来源: `evidence/checkpoints/t2_B-*.md` / `t2_S-*.md` (含 _review / _audit 改判)、`work/out_of_scope_findings.md` O1-O61、`evidence/checkpoints/t2_post_user_ack.md`、`evidence/checkpoints/t1_lane_notes.md` "T4 汇总须列" 条、`work/t1_errata.json` (pending_user 4 条为 T1 REAL_GAP 争议, 非 typo, 不入本表)。
> 机读登记: `work/t2_pdf_typo_registry.jsonl` (现 274 行: 草拟时 269, T4 整理 270, 解冻轮 +2, 第二轮改台账 R2L +2; 位置列按当时 HEAD 重定位, 以文件为准)。引文 ≤ 25 词/处。

## 00. T4 待用户裁定总览 (主控整理 2026-11-27; 逐项勾选即可)

> 主控只整理, 不替用户选. "主控建议" 只是建议. (本表写于总闸 attempt 1 之后, 当时 KB 冻结在 00a2e93 内容; 之后按 §000 代裁做过一次解冻轮 `a59c2d3`, 现 KB 再次冻结在该内容上. 表内数字是 attempt 1 当时的值, 现值见 `t4_attempt2_report.md` §4.)
> 总闸结论见 `evidence/checkpoints/t4_gate_review.md`: 样本 84/84 成立, 但闸门证据层判 **不通过 (CONDITIONAL)**, 下列 U-1 ~ U-5 是关闭总闸的必要裁定.

| # | 事项 | 选项 | 主控建议 | 用户选 |
|---|---|---|---|---|
| U-1 | **G-TB3 覆盖率口径** (详见 `t4_gate_review.md` §4). 06 公式照套 = strict **96.0741%** (低于 06 的 99.02%); 新三类 (ATOM_ERR/PDF_TYPO/FIG) 从分母去掉 = mapped **99.3578%**; 下降几乎全部来自 319 行 "06 算覆盖 → 现标 ATOM_ERR/PDF_TYPO/FIG" | A = mapped 过闸, 并列报 strict + 内容指标 (EXACT+EQUIV) 90.70% / B = ATOM_ERR+PDF_TYPO 算覆盖、FIG 算未覆盖 (99.27%) 过闸, 并列报 strict / C = 只认 strict (闸不过) | A 或 B (审查者意见同); 不论哪个都并列报 strict | ☐A ☐B ☐C |
| U-2 | **残留 `ig34_p0056_a006`** (§4.5.3.2 表格行, G-TB1/G-TB2 不过的唯一原因). PDF p56 `work/pdf_pages/ig34_p0056.txt:37-40` 三列均为 "When splitting a text string into several records, the text should be split between words to improve readability." + "Not applicable."; KB `knowledge_base/chapters/ch04_general_assumptions.md:1478` 四格与 PDF 逐字一致; 原子 verbatim 第 2/3 格漏 "to improve readability"、缺句点 → 原子抽错 | A = 改标 ATOM_ERR (ledger 改一行, 不动 KB) / B = 改标 EQUIVALENT / C = 维持 PARTIAL 残留 (G-TB1 不达标) | A | ☐A ☐B ☐C |
| U-3 | **G-TB2 结构父节口径**: 父节只看 §5.0 范围内子节 (170/174) 还是 PLAN 字面 "所有子节" (155/174, 另 15 节仅因范围外子节不过) | A = 范围内口径 / B = 字面口径 | A (范围外子节不在本项目授权内) | ☐A ☐B |
| U-4 | **G-TB6 C 层** (MERMAID 322 / TABLE_TOKENS 680 等 1370 行) 接受按抽样 (30 行 + HEADING 21 全量) 过, 还是要逐行签字 | A = 接受抽样 / B = 要求逐行 | A | ☐A ☐B |
| U-5 | **ATOM_ERR 197 / PDF_TYPO 122 / FIGURE_DEFERRED 11 确认** (单位 = 原子; 逐条表 `evidence/checkpoints/t4_ack_lists.md`). 总闸补充层抽 ATOM_ERR 4 + PDF_TYPO 4 全成立; 其中 C7 规则 38 条 ATOM_ERR 未逐条证明 | A = 整类确认 / B = 先补抽 (如 C7 38 条全检) 再确认 | B (C7 38 条) 后 A | ☐A ☐B |
| U-6 | **T4.2 人工抽样** `evidence/checkpoints/t4_human_sample.md` 42 条 (正式 30 + 风险层 12) 逐条判 | 在该文件内勾 | — | (见文件) |
| U-7 | **本文件 §1 A 组 107 行 + §2 B 组 15 行** 逐条 A/B (A = 维持照录 / B = 改候选值; B 组: 维持 keep-correct / 否决改回 PDF). 机读登记 270 行 = KB 写正确值 174 + 照录+T4 96 | 在表内勾 | 见各行 "主控建议" | (见表) |
| U-8 | **范围外 K3b 4 条** (`work/t3_t4_k3b_out_of_scope.txt`; 原子不在 §5.0, T3 未改): ① `ig34_p0026_a037` PDF p26 "VISTNUM" (B-ch04 T-7), KB ch04:200 写 VISITNUM, ledger stock PARTIAL; ② `ig34_p0082_a025` PDF p82 表头 "BIRTHDTC" (S-SPREL SE T-1), KB SE/examples.md:44 写 BRTHDTC, ledger stock **EXACT** (实非逐字); ③④ `ig34_p0342_a006/a007` PDF p342 SCDTC "20-17-04-01"/"20-17-06-10" (B-SC T-1), KB SC/examples.md:35 写 2017-04-01 / 2017-06-10, ledger stock EQUIVALENT | 每条: A = ledger 改标 PDF_TYPO (与范围内同类一致, 不动 KB) / B = 维持 stock 标签 (范围外不动) | A (②的 EXACT 标签不成立) | ① ☐A ☐B ② ☐A ☐B ③ ☐A ☐B ④ ☐A ☐B |
| U-9 | **S-TYPO 追加** (见文末 "主控补注"): (a) CRF 选项符号口径 (PDF ○□ vs KB `( )`/`[ ]`; CE 用 `( )` 而 FA 用 `○`, 不统一; 候选见 `evidence/checkpoints/t2_S-TYPO.md`); (b) MH `History“` ×2 方向; (c) S-TYPO 残余 230 行 (`work/t2_batches/S-TYPO.residual.jsonl`) | (a) A = 照 PDF 字形 / B = 维持 KB 写法; (b) A = 照录 / B = 改正方向; (c) A = 接受现状 / B = 人工逐行 | (a) 用户定; (b) A; (c) A | (a) ☐A ☐B (b) ☐A ☐B (c) ☐A ☐B |
| U-10 | **总闸新报 KB 观察项** (KB 冻结, 只记录): ① `model/05_study_level_data.md:29/45` 等 5.1.x 标题加了 PDF 没有的 "(TE)" "(TA)" 后缀 (与 A5-1/A5-11 同类); ② `domains/CE/examples.md:39` CRF 标题 KB 自拟无 KB note; ③ `chapters/ch02_fundamentals.md:158/:167` KB 自拟标题无 D6 标注; ④ PDF p354 "Lymph Nodes State" vs p355 "Lymph Node State" 未登记; ⑤ 标签口径: 原子抽错但 KB 对的原子有的标 ATOM_ERR、有的标 EXACT/EQUIV; stock EQUIV 实为逐字; ⑥ (2026-11-27 下游答复时发现) `model/06_relationship_datasets.md:177-178` RELSPEC REFID/SPEC 的 Notes 列旧 KB 有 C-code、重写后为空, 而 `model/03` SE 表 TAETORD/EPOCH 的 Notes 列仍放 C-code, 做法不一致; ⑦ `domains/PC/examples.md` 有无编号的 `## PC – Examples` 层, 其他域 examples.md 没有这一层 (详 `evidence/checkpoints/t4_downstream_notes.md`) | 每条: A = 解冻后修 / 补登记 / B = 不处理 | A (①-④); ⑤ 记 D7 后续 | ☐A ☐B (逐条备注) |
| U-11 | **O51 Mermaid 统一渲染** (TA/DM/model05/TV/TD) 与 **A5-14 D6 前缀口径** (主控意见见 A5-14 行) | 随 T4.3 前处理 / 推迟 | 解冻后一次做 | ☐处理 ☐推迟 |

## 000. 裁定记录: 委托代裁 (2026-11-27)

> **性质**: 下列裁定**不是主人逐条裁定**. 主人于 2026-11-27 把本清单的选择题委托给协调 bot「sdtm开发」, 委托原话: 「之前那些选项，你可以替我分析后决定嘛。我听从你的建议」. 裁定人 = 协调 bot「sdtm开发」(受托代裁); 执行 = 本项目主控. 是否足以替代 "用户认可记录" 由 T4.1 总闸审查者判断.
> **委托不覆盖 U-6** (T4.2 人工闸): AI 预筛 (`t4_human_prescreen.md` 42/42 + 解冻后 `t4_human_prescreen_postthaw.md` 4/4) 不是人工判定. 之后主人 (经协调方转达) 本人把 T4.2 改为 "AI 预筛 42 + 主人抽查 6", 判 6/6 内容正确 → 登记 `t4_human_verdicts.md` (attempt 2 审查时仓内无主人原话独立凭证, 判 "需主人确认 / 可核性不足"; 其后的记录见本文件状态行 ③ ④).

| # | 代裁 | 附加条件 / 执行说明 | 证据 |
|---|---|---|---|
| U-1 | **B**: ATOM_ERR + PDF_TYPO 算覆盖、FIG 算未覆盖 (99.27% 口径) 过闸; 并列报 strict 96.07% 与内容指标 | 前提 = U-5 全检成立 (已成立, 38/38); 全检改变标签则按新标签重算 (未改变) | `t4_u5_c7_fullcheck.md` |
| U-2 | **A**: `ig34_p0056_a006` 改标 ATOM_ERR, 只改台账 | 不动 KB | — |
| U-3 | **A**: 父节只看范围内子节 | — | — |
| U-4 | **A**: 接受抽样 | — | — |
| U-5 | **B**: 先全检 C7 38 条 (独立审查者), 全部成立 → 整类确认 | 全检结果 38 成立 / 0 不成立 / 0 看不出 → ATOM_ERR 197 / PDF_TYPO 122 / FIG 11 整类确认 (委托代裁) | `t4_u5_c7_fullcheck.md` (oh-my-claudecode:tracer) |
| U-6 | **不在委托内**: 仅 AI 预筛 | 预筛者 general-purpose (与各批 auditor、总闸审查者不同); 主人本人 (经转达) 选 "预筛 + 抽查 6", 判 6/6 → `t4_human_verdicts.md` | `t4_human_prescreen.md` |
| U-7 | A1-A3 默认 A, 仅单值可定时 B; 草拟 B 逐行复核; A4 = A; A5 按主控建议 (A5-12/A5-15 = A, 其余 B); A6 = B; B 组维持, 不能单值定的否决 | 复核 (pr-review-toolkit:code-reviewer): 草拟 B 26 行 → 维持 B 21 / 改回 A 5 (A2-12, A3-24, A3-28, A3-31, A3-32); B 组 15 维持 / 0 否决. A2-16 草拟候选值 (PPGRPID) 有误, 审查者按同页 relrec 更正为 "PC records with PCGRPID" (代裁同意按审查者值). A2-5 扩到 :48/:50. 行数: 任务原述 "40 行", 实数 A1-A3 26 + A5 13 + A6 2 = 41 (代裁: 以实数为准) | `t4_u7_rowcheck.md` |
| U-8 | 四条都 **A**: 台账改标 PDF_TYPO, 不动 KB | — | — |
| U-9 | (a) S-TYPO **口径 A (按渲染外观)**: CE 39 + ch04 19 = 58 处, ML 保持 `[X]`/`[ ]`; (b) MH `History“` **A** 照录; (c) 残余 230 行 **A** 接受现状 | (a) 指 `t2_S-TYPO.md` 的口径名, 不是 §00 (a) 行的字母 | `t2_S-TYPO.md` "CRF 符号" |
| U-10 | ①②③④ **A** (解冻后修或补登记; ① 按 S-MOD3 主控规则 "(XX)" 后缀为保留的检索导航 → 只补登记, 不改 KB); ⑤ 记后续; ⑥ 本次不处理, 记后续, **将来改前先通知 sdtm-rag** (rag 读该列是否为空); ⑦ 不处理, 照 PDF | — | — |
| U-11 | **处理**: Mermaid 统一渲染 + A5-14 前缀口径 (按主控意见), 本次解冻一次做完 | 解冻前渲染 42/42 OK (`scripts/t4/t4_mermaid_render.sh`) | — |
| 追加 Q1 | A5-3 照做 (TS 表加第 6 列, 同 TT/TP 承载) | 在 `t4_downstream_notes.md` 写明 rag 定义出处映射新增 TSVALCD/TSVCDREF/TSVCDVER → model/05, 解冻后用 rag 只读脚本 `defhome_rules.py` 实算并贴结果; 超出这 3 条且判断不了 → 停下问 | — |
| 追加 Q2 | A2-16 按审查者值执行 | 登记写明草拟候选值有误、由审查者更正 | `t4_u7_rowcheck.md` |
| 追加 Q3 | B-MK T-1 MK 表范围 en dash 本次不改, 记后续 | — | — |

### 000b. 主控决定 (实施层, **不在委托代裁内**; 总闸 attempt 2 要求单列. M-1 ~ M-7: 按 `t4_owner_confirmation.md` 的记录已由主人追认; M-8: 主人第二轮问题 5 已追认 (见 §000c); M-9: 主人 2026-11-27 消息 4 已追认 (见 §000c); M-10: 主人 2026-11-27 消息 5 「C1、D1、追认 M-10」已追认 (见 §000c); **M-11 待主人追认** (不挡闸))
| # | 决定 | 出处 |
|---|---|---|
| M-1 | 解冻门禁替代证明: `typo_assert --plan` / `ct_assert` 结构性 FAIL, 以 W1 拆分验证 + reviewer 逐条归因代替; S-TYPO.fixed 追加 58 行 CRF 放行 | `t4_thaw_review.md` 主控追认 |
| M-2 | TT/TP DOMAIN 格保留在 Usage Restrictions 列下 (避免改 rag 所读内容), 记后续 | 同上 |
| M-3 | W3 打标机制 = 逐原子 s0 条目 + registry 事实修正 6 行 (B-NV 页号, B-TS pdf_value); 不改 K3b 规则 | `t4_thaw_W3.md` attempt 1 续 |
| M-4 | `ig34_p0362_a010` ATOM_ERR → PDF_TYPO (K3b(b) 口径; ack 清单记在 U-7 名下, 实为主控决定) | 同上 |
| M-5 | t3_mutation M3 换靶 (DM/spec.md:219); CE p153 14 原子块级补核 | 同上 |
| M-6 | 5 条 `> Note:` 行反向溯源豁免 (整行锚定) | 同上 |
| M-7 | ack 清单 "决定来源" 归属 (U-5 / U-2 / U-8 / U-7) | 同上. 2026-11-27 接手主控更正一处登记错误: `ig34_p0362_a010` 原记在 U-7 名下, 实为 M-4 → `scripts/t4/t4_ack_lists.py` 加 `MAIN_CTRL` 后重生成 (U-7 23 → 22, 主控决定 M-4 1; 其余行不变). 注: 这处更正发生在 `t4_owner_confirmation.md` 所记的确认之后, 那次追认是否覆盖它, 留给总闸 attempt 3 判断 |
| M-8 | (接手主控; 不在 `t4_owner_confirmation.md` 第一节所记范围内; **主人 2026-11-27 第二轮问题 5 已追认**, 见 §000c) T0 变异在现 KB 上重证时 M4a 换靶: 原靶 (MB 第二份 suppbe 副本) 已被 D2 去重删掉 → 改用 PDF p431 relrec Ex1 的两份 KB 副本 (ch08 / RELREC), 只变异 ch08 那份; 现 KB 基线另存 `work/t4/t0_head/`, T0 基线不覆盖 | `t4_t0_refresh.md` §3 |
| M-9 | (接手主控; **主人 2026-11-27 消息 4 「A1、B1、追认 M-9」已追认**; 主人第二轮定的是 "改哪些标签", 下面这些是落地时的机制选择, 不是他定的) 第二轮改台账 (R2L) 的实施做法: ① 范围外 6 条笔误同类没照规格字面 "比照 U-8 keep 清单", 而是走 errata R2 + 运行时 pdf / kb 行 token 断言 (原因: 这 6 条没被 K3b 触及, 写进 keep 清单会撞断言, 且 ack 清单会把来源误归 U-8); ② IE 53 条用新规则 `T4-R2L-owner-IE`, `IE flip not in t1_ie_final` 断言只对它放行, `t1_ie_final.md` 不加这 53 条; ③ 范围内 19 条不走 `s0_classify` 条目, 做成 errata 里的逐原子登记绑定; ④ 登记表新字段 `other_kb_lines` (B-SUPPQUAL T-1) 与 `t4_r2l_fix` (记更正前后); 9 行登记文字 / 页号更正 + 2 行新登记 (后者 = 问题 9 = A); 5 条原子补登记指针 (不改标签); ⑤ 新写行沿用固定 `ts` 2026-11-26T12:00:00Z / `prompt_version` t3_writer_v1.0 (为了让没改判的行逐字节不变), 决定日期写在 `evidence.t4_r2l` 里. 标签结果: 78 条恰按主人选的清单, 清单外 0 条 | `t4_round2_ledger_W.md` §1 / §2 / §5; reviewer `t4_round2_ledger_review.md`; auditor `t4_round2_ledger_audit.md` |
| M-10 | (接手主控; **主人 2026-11-27 消息 5 「C1、D1、追认 M-10」已追认**; 主人定的是 "这 4 条改回 EXACT" (A1), 下面是落地时的机制选择, 不是他定的; 产生于他追认 M-9 之后) R3L 的实施做法: ① 数据清单新建 `work/t4_r3l_relabel.json`, 不并入 R2L 的清单; ② keep 清单里这 4 条的 action 由 `keep_k3b` 改为新值 `t4_r3l_drop` (条目不删, 记 before → after); ③ `t3_writeback.py` 在 K3b 登记扫描之后先断言 "这 4 条当前的触及恰好等于清单声明的登记 id", 再把触及拿掉, 之后走现有判定 (结果 = live-hit EXACT), 不新增判定分支; K3b 规则本身不改; ④ 这 4 条强制重写为 TB 行、`batch_id` = T4-R3L (其中 2 条与 T3 前基线同为 EXACT, 不强制重写就没有决定来源); ⑤ `t3_rules.json` 新键 `K3b_t4_r3l_dropped`; 沿用固定 `ts`; ⑥ 本批不另设语义 auditor (语义依据 = 第三轮审查者与总闸 attempt 3 审查者两次独立复核). 标签结果: 恰好这 4 条, 清单外 0 条 | `t4_round3_ledger_W.md` §2 / §6; reviewer `t4_round3_ledger_review.md` |
| M-11 | (加查会话主控, **待主人追认**; 不挡闸 — 总闸 delta 审查者 2026-11-27 指出须登记; 主人定的是 "这 1 条改回 EXACT" (C1), 下面是落地时的机制选择, 不是他定的) R4L 的实施做法: ① 数据清单新建 `work/t4_r4l_relabel.json` (由一次性脚本 `scripts/t4/t4_r4l_build.py` 生成), 不并入前两批的清单; ② 在 `scripts/t3/t3_errata_build.py` 里**撤销**这条原子的 t1 原子抽错登记 (`work/t1_errata.json` 不改; 原条目原样存进 `work/t3_errata.json` 的 `r4l_revoked`), 之后由原有判定路径 `live-hit` 判出 EXACT, 不是事后改标签; ③ 这一行在台账里重写为本项目的行并标批号 `T4-R4L`; ④ 新行的 `ts` 沿用固定值 (早于决定日, 决定日期记在 `evidence.t4_r4l.decision`); ⑤ **没有另设语义抽检**, trace 里这一批只有 "执行者 + 结构审查者" 两类角色 — 这 1 条的语义由加查的两位互不知情的审查者与总闸 delta 审查者共三次独立核验, 后者兼作第三个不同类型的独立核验; ⑥ 清单用 `work/t4/atomerr/verdicts.json` 里 NOT_HOLD 的集合做交叉断言 (整链从此读这份审查者判定文件); ⑦ 同批给 4 条 ATOM_ERR 行补登记指针 (只改 `evidence.registry`), 规格里把其中一个登记号写得不全, 执行者用了登记表里的全名 `B-RS T-6 (RS 副本)` | `t4_round4_ledger_W.md`; `t4_round4_ledger_review.md`; `evidence/t4_gate_raw/attempt3_delta2_report.md` C / H 项 |

### 000c. 第二轮: 主人本人裁定 (2026-11-27, 在接手主控聊天里直接回答; **不是委托代裁**)

> 原话与收到时间: `t4_owner_confirmation.md` 第二轮一节 (消息 1 「可以没问题」→ 主控追问并逐项列出建议选项 → 消息 2 「是，都按建议」→ 第三轮结果出来后主控再问问题 A / B → 消息 3 「继续」, 未答 A / B → 总闸 attempt 3 判问题 A 为唯一挡闸项, 主控第三次提问 → 消息 4 「A1、B1、追认 M-9」 → 总闸 PASS 之后加查查出问题 C / D, 主控提问 → 消息 5 「C1、D1、追认 M-10」, 在同一文件 "第三个会话" 一节). 提问页 `t4_owner_decisions_round2.md` (第 3 稿). 依据的核查: `t4_supp_fullcheck.md`.

| 问题 | 主人选 | 执行 | 状态 |
|---|---|---|---|
| 1 (51 条 v2.0 变量表行) | A: 改记 INTENTIONAL_EXCLUDE | 改台账批 R2L (`subagent_prompts/t4/t4_round2_ledger_spec_v1.0.md`) | **已执行** (writer `t4_round2_ledger_W.md`; reviewer PASS `t4_round2_ledger_review.md`; auditor 33/33 `t4_round2_ledger_audit.md`) |
| 2 (2 条 v2.0 目录条目) | A: 改记 INTENTIONAL_EXCLUDE | 同上 | 同上 |
| 3 (19 条受已登记笔误影响的原子) | A: 改记 PDF_TYPO | 同上 | 同上 |
| 4a (SDTMIG 旧 EQUIVALENT) | B: 再抽 150 条 | 第三轮 R3_IG34_EQUIV: 150 条 0 错 (累计 215 条 0 错) | 已做 |
| 4b (PDF_TYPO 类) | B: 剩下 99 条全看 | 第三轮 R3_PDF_TYPO: 94 成立 / 4 多标 / 1 判不了 | 已做; 引出问题 A / B |
| 4c (标题类旧标签) | B: 抽 60 条 | 第三轮 R3_HEADING: 60 条内容全成立 (5 条标签级别) | 已做 |
| 4d (笔误同类筛法的盲区) | A: 到此为止 | 不再追加; 盲区写在 `t4_supp_fullcheck.md` §4 | 已定 |
| 5 (M-8, T0 变异 M4a 换靶) | 追认 | — | 已追认 |
| 6 (域文件标题不带节号) | A: 登记为认可的写法, 不动 KB | **本行即登记**: KB 域文件的标题写成 `# 域代码 — 域名` (不带 PDF 节号) 是认可的 KB 写法, 对应的标题类原子按 EQUIVALENT 计; 另, `knowledge_base/domains/DI/assumptions.md:10` 的 `## DI – Description/Overview (§9.1)` 是 KB 自拟标题 (PDF 为 "9.1 Device Identifiers"), 登记为 KB 自拟标题一类 (同 O60 / A5-11), 不改 KB | 已登记 |
| 7a (范围外跨文档指针 146 条) | C: 这次不动 | 记为已知局限 (清单 `work/t4/round2/round2_population.json` 的 `xdoc_out_of_scope`) | 已定 |
| 7b (范围外笔误同类) | A: 独立审查确认后改记 PDF_TYPO | 第三轮 R3_XTYPO 6 条全部对渲染页确认 → 并入 R2L | 已执行 (同问题 1 行) |
| 8 (EG / RE 省略号) | A: 接受现状 | 不改 KB; `EG/examples.md` 例 3 表 25 行 + `RE/examples.md:15` 用 `...` 而 PDF 为 `…`, 登记为接受的排版差异 | 已登记 |
| 9 (两处 PDF 自身不一致) | A: 补登记 | 登记表加两行 (随 R2L): `T4R2 sv20 N-1`、`T4R2 RELSPEC N-1` | 已登记 |
| **A** (4 条多标的 PDF_TYPO 是否改回 EXACT) | 第一次问: 未答 (消息 3 「继续」); 总闸 attempt 3 判它为唯一挡闸项后再问 → **A1: 改回 EXACT** (消息 4) | 改台账批 R3L (`subagent_prompts/t4/t4_round3_ledger_spec_v1.0.md`) | **已执行** (writer `t4_round3_ledger_W.md`; reviewer PASS `t4_round3_ledger_review.md`; 4 条现由 live-hit 判为 EXACT, 清单外变化 0) |
| **B** (`ig34_p0293_a038` 判不了的怎么记) | 第一次问: 未答; 再问 → **B1: 维持 PDF_TYPO 并写明无法判定** (消息 4) | 标签不动; 无法判定之处 = 折行处有没有空格 (登记 `B-MK T-2` 已注折行歧义; 第三轮与总闸审查者都判 UNVERIFIABLE, KB 两种情况下都对) | 已登记 |
| M-9 (R2L 机制选择) | **追认** (消息 4) | — | 已追认 |
| **C** (加查查出的 1 条多标 ATOM_ERR `ig34_p0124_a001` 是否改回 EXACT) | **C1: 改回 EXACT** (消息 5 「C1、D1、追认 M-10」, 2026-11-27 夜, 主人在加查会话聊天里直接发) | 依据 `t4_atomerr_fullcheck.md` §4; 两位互不知情的独立审查者都判 "原子没抽错, KB 逐字承载" | 改台账批 R4L (`subagent_prompts/t4/t4_round4_ledger_spec_v1.0.md`); 结果见 `t4_round4_ledger_W.md` / `t4_round4_ledger_review.md` |
| **D** (口径: `B-CE T-2` 那 8 条原子与 PDF 只差代码值里的一个空格, 算原子抽错还是空白归一) | **D1: 维持 ATOM_ERR** (消息 5) | **本行即登记的口径**: 代码值 / 标识符 (如 USUBJID) 内部的空格是值的一部分, 原子与 PDF 在这里差一个空格算真实差异 (原子抽错成立), **不属于** "空白归一"; "空白归一" 只指词与词之间、行首行尾、折行处的空白. 与登记 `B-CE T-2` (PDF 8 处带空格, KB 照录) 一致. 依据 `t4_atomerr_fullcheck.md` §5a | 标签不动 (8 条仍 ATOM_ERR); 加查 brief 已补先后说明 (`subagent_prompts/t4/t4_atomerr_s1r1_v1.0.md` 文末 "v1.0 之后的口径补注") |
| M-10 (R3L 机制选择) | **追认** (消息 5) | — | 已追认 |

## 0. 用法
- 每行二选一: **A = 维持现状** (KB 照录 PDF), **B = 改为候选值**。"主控建议" 列是登记员草拟, 主控审后可改。
- 口径 (沿用 dispatch "PDF_TYPO 取舍规则"): 正确值能由 PDF 自身单值确定 → KB 写正确值; 否则照录 + T4。下列 A 组都是 "不能单值确定" 的项。建议列对 "语法只有一种补法" 的项倾向 B (与已接受的 B-IS T-5 / B-ch01 T-1 keep-correct 同口径), 对 "多种修法" 的项倾向 A。
- 同一 PDF 问题有多个 KB 副本的, 表中逐个列出, 裁定时一并改。

## 1. A 组: 照录 + T4 待用户 A/B

### A1 表格格值: 日期 / 编号 / ID / 单位 (正确值 PDF 自身不能单值确定)

| # | 批次 / id | 位置 | PDF 原值 (A=维持照录) | 候选值 (B) | 依据 | 主控建议 (草拟) | 用户选 |
|---|---|---|---|---|---|---|---|
| A1-1 | B-AE U-1 | `domains/AE/examples.md:82` | p142 Ex5 r2 AEENDY 25 | AEENDY 24 或 AEENDTC 2018-05-11 | AESTDTC 2018-05-01=Day 15 → 05-10 应为 Day 24; 日期/Day 谁错不可单值 | A | ☐A ☐B |
| A1-2 | B-AE U-2 | `domains/AE/examples.md:97` | p142 Ex6 r2 AEENDTC 2014-11-27 | AEENDTC 2018-11-27 (仅改年份) | 早于 AESTDTC, 年份必错; 按 Day 推得 11-28 ≠ 11-27, 非单值 | A | ☐A ☐B |
| A1-3 | B-AE U-3 | `domains/AE/examples.md:96` | p142 Ex6 USUBJID r1 002 / r2 001 | 两行同一 USUBJID (001 或 002) | 同 SPDEVID、AESEQ 1/2、叙述同一受试者; 哪个对不可定 | A | ☐A ☐B |
| A1-4 | B-AE U-4 | `domains/AE/examples.md:97` | p142 Ex6 r2 AESTDY 78 | AESTDY 80 | r1 Day 27=2018-09-01 推得 10-24 应为 Day 80 | A | ☐A ☐B |
| A1-5 | B-AE U-5 | `domains/AE/examples.md:96` | p142 Ex6 r1 AERLDEV CAUSAL | CAUSAL RELATIONSHIP (原 KB 值) | 原 KB CAUSAL RELATIONSHIP; KB 无 ISO 14155 码表可证 | A | ☐A ☐B |
| A1-6 | B-BE O28 | `domains/BE/examples.md:122` | p147 Ex2 bs r1 BSORRES 12 mL vs BSSTRESC/N 6 | BSORRES 6 mL 或 STRESC/N 12 | PDF 内部不一致, 无法由 PDF 定正确值 (O28) | A | ☐A ☐B |
| A1-7 | B-CE T-2 | `domains/CE/examples.md:101` | p153 USUBJID ABC -US-701-002 (mh/ce/pr 8 格) | ABC-US-701-002 (去空格) | USUBJID 惯例不含空格; PDF 8 处一致带空格 (O44: 3.5pt 字距说法不成立) | A (PDF 8 处一致); 若重 ID 惯例则 B | ☐A ☐B |
| A1-8 | B-CE T-3 | `domains/CE/examples.md:110` | p153 suppmh/suppce USUBJID 001-001 | supp USUBJID = 父表 USUBJID | 与父表 ABC -US-701-002 不一致, PDF 内部矛盾 | A | ☐A ☐B |
| A1-9 | B-DS U-1 | `domains/DS/examples.md:294` | p165 Ex10 se ETCD SCREEN | ETCD SCRN (SE.ETCD 须∈TE.ETCD, spec 约束) | 同例 TE/TA 为 SCRN; 跨表不可定 (reviewer: 可用 SE.ETCD∈TE spec) | B (spec 约束可单值定) | ☐A ☐B |
| A1-10 | B-DS U-2 | `domains/DS/examples.md:407` | p167 Ex11 ds 筛选 3 行 TAETORD=1 | TAETORD 0 (同 TA 筛选元素) | TA/SE 筛选元素 TAETORD=0; 跨表 | A | ☐A ☐B |
| A1-11 | B-EX T-5 | `domains/EX/examples.md:300` | p117 Ex6 ex EXENDTC 24 行全空 | EXENDTC = 同行 EXSTDTC (Assumption 4b) | EXENDY 有值; Assumption 4b 要求点给药复制 EXSTDTC; 自填属生成 | A (自填 24 格属生成) | ☐A ☐B |
| A1-12 | B-FA T-10 | `domains/FA/examples.md:321` | p375 Ex6 relrec STUDYID ABC vs ae/faae XYZ | relrec STUDYID XYZ | 跨表矛盾; USUBJID 亦不一致, 无单值 | A | ☐A ☐B |
| A1-13 | B-GF U-1 | `domains/GF/examples.md:64` | p225 GFMETHOD REAL_TIME POLYMERASE CHAIN REACTION ×3 | REAL-TIME POLYMERASE CHAIN REACTION (去下划线) / CT 全称 …ASSAY | 引言 real-time…; CT C51962 为 REAL-TIME … ASSAY, 不单值 | A | ☐A ☐B |
| A1-14 | B-GF U-2 | `domains/GF/examples.md:145` | p227 MB r1 MBREFID INFLU0101 | INFLU0101.1 | GF/MS r1 为 INFLU0101.1; 可能有意 | A | ☐A ☐B |
| A1-15 | B-IS U-1 | `domains/IS/examples.md:117` | p236 ISSEQ 同受试者内重复 (Ex5/10/11 共 18 格) | ISSEQ 按受试者连续编号 (18 格) | spec 要求唯一但 any valid number, 正确编号不可单值 | A | ☐A ☐B |
| A1-16 | B-IS U-3 | `domains/IS/examples.md:164` | p237 Ex7 r3/r4 VISIT 1 ISDTC 2017-08-27 | ISDTC 2017-07-27 | 同受试者 Ex5/Ex8 VISIT 1=2017-07-27; 跨例 | A | ☐A ☐B |
| A1-17 | B-MH T-2 | `domains/MH/examples.md:106` | p178 Ex5 r1 MHDTC 2019-011-02 | 2019-11-02 或 2019-01-02 | 可读 2019-11-02 或 2019-01-02, 不单值 | A | ☐A ☐B |
| A1-18 | B-MS T-4 | `domains/MS/examples.md:80` | p262 suppms QNAM MSMEDTYPE (9 字符) | QNAM MSMEDTYP (8 字符) | QNAM≤8; 正确值非 PDF 自证 | A | ☐A ☐B |
| A1-19 | B-OE U-1 | `domains/OE/examples.md:144` | p304 Ex4 OESEQ 1/2/1/2 | OESEQ 3/4 (OS 行) | 同受试者 SEQ 重复, 正确编号不可定 | A | ☐A ☐B |
| A1-20 | B-PCPP T-4 | `domains/PC/examples.md:85` | p277 文字 Rows 14-26 RELID 2/DY8DRGX vs 表 RELID 1/DY1DRGX | 文字改 RELID 1 / DY1DRGX, 或表改 RELID 2 | PDF 文字与表矛盾 | A | ☐A ☐B |
| A1-21 | B-PCPP T-7 | `domains/PP/examples.md:16` | p271 Ex1 PPSTRESU H | PPSTRESU h (UNIT CT 值小写, 同列一致) | 同列 h; UNIT CT C25529 提交值为 h (terminology/core/other_part3.md:212) | B | ☐A ☐B |
| A1-22 | B-SC T-2 | `domains/SC/examples.md:36` | p342 Row 3 SCDTC 2017-06-10 vs SCDY 297 | SCDY 296 或 SCDTC 2017-06-11 | 按 Row 1/2 推应为 296; 日期/SCDY 谁错不可定 (O52) | A | ☐A ☐B |
| A1-23 | B-SM T-2 | `domains/SM/examples.md:39` | p86 ce r1 CEENDTC 2013-09-01T2:30 | CEENDTC 2013-09-01T12:30 (原 KB 自推值) | 早于 CESTDTC T11:00; 正确时刻 PDF 无证 | A | ☐A ☐B |
| A1-24 | B-SR T-2 | `domains/SR/examples.md:97` | p380 表 SRDTC 14:08:24 vs 叙述 53h56m | 改叙述为 53h38m 或改表为 14:26 | PDF 表与叙述自相矛盾, 无第三来源 | A | ☐A ☐B |
| A1-25 | B-ch04 T-2 | `chapters/ch04_general_assumptions.md:1327` | p53 lb r7 说明 LBDRVFL=Y, 表列 LBLOBXFL | 表头 LBLOBXFL→LBDRVFL, 或叙述改 LBLOBXFL | 仅 visit 3 r7 有 Y, 疑表头错标 | A | ☐A ☐B |

### A2 变量名 / 参数码 / 代码写法

| # | 批次 / id | 位置 | PDF 原值 (A=维持照录) | 候选值 (B) | 依据 | 主控建议 (草拟) | 用户选 |
|---|---|---|---|---|---|---|---|
| A2-1 | B-ch03 T-4 | `chapters/ch03_submitting_data.md:52` | p18 IS Keys ISSCMBCL | ISMSCBCE (p456 新增变量) | 全书仅此处; 候选 ISMSCBCE (p456) | A | ☐A ☐B |
| A2-2 | B-PCPP T-8 | `domains/PC/examples.md:284` | p280 散文 DYIDRGX_A / DYIDRGX_HALF | DY1DRGX_A / DY1DRGX_HALF (同页表值) | 文本层即如此, 与表 DY1DRGX_* 不一致 | B | ☐A ☐B |
| A2-3 | B-PCPP T-8b | `domains/PC/examples.md:278` | p280 Ex3 引言 DYDRGX_HALF | DY1DRGX_HALF | 应为 DY1DRGX_HALF, 不单值 | B | ☐A ☐B |
| A2-4 | B-TS T-2 | `domains/TS/assumptions.md:43` | p419 正文 "Dose" vs 表 DOSE | TSPARMCD = "DOSE" (CT 参数码) | 大小写不一致 | B (CT 可定) | ☐A ☐B |
| A2-5 | B-TS T-3 | `domains/TS/assumptions.md:43` | p419 DOSFREQ vs Ex4 DOSFRQ | DOSFRQ (CT C-code 参数码) | 两处互异 | B (CT 可定) | ☐A ☐B |
| A2-6 | B-TS T-4 | `domains/TS/assumptions.md:57` | p419 OUTMSPR vs Ex1 OUTMSPRI | OUTMSPRI (CT 参数码) | 两处互异 | B (CT 可定) | ☐A ☐B |
| A2-7 | B-TS T-6 | `domains/TS/assumptions.md:115` | p425 MAXAGE vs 参数 AGEMAX | AGEMAX case (CT 参数码) | PDF 内不一致 | B (CT 可定) | ☐A ☐B |
| A2-8 | B-SM O32 | `domains/SM/examples.md:7` | p85 Row 1 叙述 SMDY | SMSTDY (Rows 2-3 叙述同变量) | 非 SM 变量 (疑 SMSTDY); 不能唯一确定 (O32) | B | ☐A ☐B |
| A2-9 | B-EG T-1 | `domains/EG/examples.md:15` | p189 叙述 EGCAT="FINDINGS" vs 表 FINDING | 叙述 EGCAT = "FINDING" (同表) | 叙述与表矛盾, 无第三证据 | A | ☐A ☐B |
| A2-10 | B-EG T-2 | `domains/EG/examples.md:42` | p190 叙述 SCREEN 2 vs 表 SCREEN II | 叙述 "SCREEN II" (同表 VISIT) | 可能同一访视两种写法 | A | ☐A ☐B |
| A2-11 | B-ch02 T-1 | `chapters/ch02_fundamentals.md:176` | p16 Trials Sets domain | Trial Sets (sv20 p53 §5.1.2) | SDTMIG 自身无 Trial Sets; sv20 p53 §5.1.2 标题 | B | ☐A ☐B |
| A2-12 | S-TUFA TR T-5 | `domains/TR/spec.md:264` | p351 TAETORD Notes Epoch associated with… | Number that gives the planned order of the element within the arm. (FA/SR 同变量) | 与 Label 不符; 候选 = FA/SR 同变量 Notes | B | ☐A ☐B |
| A2-13 | REG CP N-1 | `domains/CP/examples.md:171` | p214 GATE and GATEDEF show the gating strategy | CPGATE and CPGATDEF | p214 原文; 变量名应为 CPGATE/CPGATDEF? 与 T-15 同型但为泛型省略写法, 未登记 | A (泛型省略写法, 新发现) | ☐A ☐B |
| A2-14 | REG BS N-1 | `domains/BS/assumptions.md:23` | p198 Assumption 5 --ORNLO, --ORNHI | --ORNRLO, --ORNRHI (同 GF T-6 列表写法) | 非标准变量名 (应 --ORNRLO/--ORNRHI); 同句 --STRNLO 已按 T-3 改正, 处理不一致 | B (与同句 T-3 口径一致) | ☐A ☐B |
| A2-15 | S-SPC2 N-1 | `domains/PC/examples.md:299` | p281 PP records with PCSEQ values | PC records with PCSEQ | 应为 PC records (PCSEQ 属 PC), 照录 | B (PCSEQ 属 PC, 单值) | ☐A ☐B |
| A2-16 | S-SPC2 N-2 | `domains/PC/examples.md:333` | p281 PP records with PGRPID values | PPGRPID values | 应为 PPGRPID, 照录 | B (单值) | ☐A ☐B |

### A3 叙述语法 / 措辞 (单一补全建议 B, 多解建议 A)

| # | 批次 / id | 位置 | PDF 原值 (A=维持照录) | 候选值 (B) | 依据 | 主控建议 (草拟) | 用户选 |
|---|---|---|---|---|---|---|---|
| A3-1 | B-DM N-1 | `domains/DM/examples.md:24` | p68 The arm actual arm variables are null | The arm and actual arm variables are null | 疑缺 and, 不能由 PDF 自身确定 | A | ☐A ☐B |
| A3-2 | B-DS U-4 | `domains/DS/examples.md:87` | p160 and in the AE record was represented | The relationship between the DS record and the AE record | PDF 原句语法瑕疵 | B (删 in, 单一) | ☐A ☐B |
| A3-3 | B-DS U-6 | `domains/DS/examples.md:346` | p166 AB +C (空格) | AB+C (去空格) | 空格是否多余不可定 | A | ☐A ☐B |
| A3-4 | B-DV T-1 | `domains/DV/examples.md:17` | p179 DVTERM 末尾句点 | 去尾句点 (同 spec Notes 引用值) | spec Notes 引同值句点在引号外; verbatim 尾句点不构成可证错 | A | ☐A ☐B |
| A3-5 | B-EG T-3 | `domains/EG/examples.md:42` | p190 principal investigation | principal investigator (同表 EGEVAL) | 表 EGEVAL=PRINCIPAL INVESTIGATOR; 改正属语义改写 | B | ☐A ☐B |
| A3-6 | B-FA T-3 | `domains/FA/assumptions.md:19` | p361 These type of assessments | These types of assessments | 语法类 | A | ☐A ☐B |
| A3-7 | B-FA T-4 | `domains/FA/assumptions.md:39` | p362 thought be related | thought to be related | 漏词 (语法) | B (单一补全) | ☐A ☐B |
| A3-8 | B-FA T-6 | `domains/FA/assumptions.md:51` | p363 FA may provided | FA may provide | 语法类 | B (单一补全) | ☐A ☐B |
| A3-9 | B-FA T-8 | `domains/FA/examples.md:183` | p372 used to populated FADTC | used to populate FADTC | 语法类 | B (单一补全) | ☐A ☐B |
| A3-10 | B-IS U-2 | `domains/IS/examples.md:101` | p235 RSV-protein B ×3 | RSV-protein Z ×3 | 语境疑应为 Z, PDF 未明载 | A | ☐A ☐B |
| A3-11 | B-IS U-4 | `domains/IS/examples.md:193` | p239 expressed in by the opsonization index | expressed by / expressed in | 删 in 或删 by 皆通 | A | ☐A ☐B |
| A3-12 | B-MB T-4 | `domains/MB/examples.md:171` | p261 sputum (Ex3 实为灌洗液) | lavage fluid sample | PDF 原文如此, 不可单值 | A | ☐A ☐B |
| A3-13 | B-MI O43 | `domains/MI/examples.md:23` | p266 is a represented in a derived record | is represented in a derived record | 语法错, 不可唯一确定 (O43) | A | ☐A ☐B |
| A3-14 | B-NV N-1 | `domains/NV/assumptions.md:23` | p294 may included | may include | PDF 语法, 照录 | B (单一补全) | ☐A ☐B |
| A3-15 | B-NV N-2 | `domains/NV/examples.md:63` | p297 links the each | links each | PDF 语法, 照录 | B (删 the, 单一) | ☐A ☐B |
| A3-16 | B-ch08 T-7 | `chapters/ch08_relationships.md:443` | p440 therefore is does not | therefore it does not / therefore does not | is→it 或删 is 两解 | A | ☐A ☐B |
| A3-17 | B-REL T-7 (RELSPEC 副本) | `domains/RELSPEC/assumptions.md:19` | p440 therefore is does not | 同 ch08 T-7, 两处同改 | is→it 或删 is 两解 (=ch08 T-7) | A | ☐A ☐B |
| A3-18 | B-ch08 T-8 | `chapters/ch08_relationships.md:321` | p436 whether the data represent as an event or a finding | represent an event / are represented as an event | 删 as 或 are represented as 均有 PDF 先例 | A | ☐A ☐B |
| A3-19 | B-ch03 T-3 (ch03) | `chapters/ch03_submitting_data.md:71` | p19 per location per per visit | per location per visit / per location per time point per visit | p19/p312 同为 per per; 少词或多词不可定 (OE 同位 per time point) | A; 三处同改 | ☐A ☐B |
| A3-20 | S-FND UR U-1 (assumptions) | `domains/UR/assumptions.md:9` | p312 per location per per visit | 同 ch03 T-3 | p19/p312 同为 per per; 少词或多词不可定 (OE 同位 per time point) | A; 三处同改 | ☐A ☐B |
| A3-21 | S-FND UR U-1 / O55 (spec) | `domains/UR/spec.md:3` | p312 per location per per visit | 同 ch03 T-3 | p19/p312 同为 per per; 少词或多词不可定 (OE 同位 per time point) | A; 三处同改 | ☐A ☐B |
| A3-22 | B-TA T-3 | `domains/TA/examples.md:363` | p392 (Open DRUG X and Rescue) | (Open Drug A and Rescue) | 图块 Open A / TDM Open Drug A; 不可唯一 | A | ☐A ☐B |
| A3-23 | B-TA T-5 | `domains/TA/examples.md:385` | p392 Example 7 in Section 5.2 vs §7.2.1.1 DM Example 3 | DM Example 3 (§7.2.1.1 说法) | PDF 两处 DM 例号不同 | A | ☐A ☐B |
| A3-24 | B-TE T-1 | `domains/TE/examples.md:102` | p407 First dose of treatment in Element | First dose of treatment Element (去 in, 3:2 多数) | 表/叙述矛盾 (3:2 无 in, reviewer 倾向去 in) | B | ☐A ☐B |
| A3-25 | B-TE T-2 | `domains/TE/examples.md:103` | p407 16 days … WBC recovers | At least 16 days … WBC recovered (同 Ex3) | 与 Ex3 Row 4 措辞多处不同, 无唯一值 | A | ☐A ☐B |
| A3-26 | B-TS T-5 | `domains/TS/assumptions.md:65` | p425 14 terms vs 表 15 行 | among its 15 terms | 含 NA 行计数不一 | A | ☐A ☐B |
| A3-27 | B-TS T-7 | `domains/TS/assumptions.md:106` | p425 Quantity sufficient vs 表 Sufficient quantity | Sufficient quantity (同表) | PDF 内不一致 | A | ☐A ☐B |
| A3-28 | S-CH10 T-3 | `chapters/ch10_appendices.md:386` | p457 in version the underwent | in the version that underwent | 语法错, 正确词无依据 | B (单一补全) | ☐A ☐B |
| A3-29 | S-TDM TD U-1 | `domains/TD/examples.md:161` | p414 repeats every 24 weeks (week 120, week 144, etc.) | repeats every 12 weeks (同图/表) | 图 Sched 3/表 P12W=12 周; 同句 week 96→120/144 只与 24 自洽 | A (同句周数只与 24 自洽) | ☐A ☐B |
| A3-30 | S-TDM TD U-2 | `domains/TD/spec.md:39` | p411 This must be a referenced from the ADaM ADSL | must be referenced / must be a reference | be referenced / a reference 二义 | A | ☐A ☐B |
| A3-31 | S-SPREL SE T-2 | `domains/SE/spec.md:39` | p79 to be consistent chronological order | to be consistent with chronological order | 缺 with | B (单一补全); SM 副本同改 | ☐A ☐B |
| A3-32 | REG SM N-1 (同 SE T-2) | `domains/SM/spec.md:39` | p84 SMSEQ Should be assigned to be consistent chronological order | 同 SE T-2 | p84 同 SE T-2 (缺 with); S-SPREL 只登记 SE 副本 | 随 SE T-2 | ☐A ☐B |
| A3-33 | S-SPREL OI T-1 | `domains/OI/spec.md:39` | p441 Sequence number to given to ensure | Sequence number given to ensure | 语法 | A | ☐A ☐B |
| A3-34 | B-ch04 N-1 | `chapters/ch04_general_assumptions.md:863` | p41 solidus or foreword slash [/] | forward slash | PDF 拼写 foreword (应 forward), 照录 | B (拼写, 单值) | ☐A ☐B |

### A4 未编号标点 / 空格 / 人名照录 (S-TYPO 必须不动)

| # | 批次 / id | 位置 | PDF 原值 (A=维持照录) | 候选值 (B) | 依据 | 主控建议 (草拟) | 用户选 |
|---|---|---|---|---|---|---|---|
| A4-1 | S-CH10 N-1 | `chapters/ch10_appendices.md:384` | p453 codelists . | codelists. | PDF 原文多空格 | A | ☐A ☐B |
| A4-2 | S-SPREL OI T-2 | `domains/OI/spec.md:30` | p441 OIVAL . (句点前空格) | OIVAL. | PDF 排版 | A | ☐A ☐B |
| A4-3 | S-SPEC1 N-1 | `domains/DM/spec.md:296` | p64 Services;2016 | Services; 2016 | 无空格, 不在裁定内 | A | ☐A ☐B |
| A4-4 | S-CH10 N-2 | `chapters/ch10_appendices.md:409` | p459 Section 9.3 PB was part of | Section 9.3 PB, which was part of | PDF 语法 | A | ☐A ☐B |
| A4-5 | S-CH10 N-3 | `chapters/ch10_appendices.md:388` | p452 Nov, 2021 | Nov 2021 | PDF 原文 | A | ☐A ☐B |
| A4-6 | S-CH10 N-4 | `chapters/ch10_appendices.md:60` | p445 Ben Qgunsulire / Gbenga Ogunsulire | 两处人名统一 | 人名写法两处不同 | A | ☐A ☐B |
| A4-7 | B-REL N-1 (RELREC 副本) | `domains/RELREC/examples.md:42` | p430 正文 "COMBO 1" vs 表 COMBO1 | "COMBO1" (同表) | PDF 自相矛盾 | A; 两处同改 | ☐A ☐B |
| A4-8 | B-ch08 N-1 | `chapters/ch08_relationships.md:135` | p430 正文 COMBO 1 vs 表 COMBO1 | 同上 | PDF 自相矛盾 | A | ☐A ☐B |
| A4-9 | B-REL N-2 (RELSPEC 副本) | `domains/RELSPEC/examples.md:17` | p440 图 SPC-003 (Brain) vs relspec r5 TISSUE | 图注 (Tissue) | PDF 图表矛盾 | A; 两处同改 | ☐A ☐B |
| A4-10 | B-ch08 N-2 | `chapters/ch08_relationships.md:461` | p440 图 (Brain) vs relspec r5 TISSUE | 同上 | PDF 图表矛盾 | A | ☐A ☐B |
| A4-11 | B-ch02 N-1 | `chapters/ch02_fundamentals.md:106` | p14 (shown in the models as “--“) | “--” (右引号闭合) | 两个左引号, 与 pdftotext 码位一致 | A | ☐A ☐B |
| A4-12 | S-CH4 N-1 | `chapters/ch04_general_assumptions.md:756` | p39 (e.g. 2001-12-26T00:00:01) | (e.g., 2001-…) | 缺 e.g. 后逗号; 主控裁定 4 照 PDF | A (主控裁定 4 已定照 PDF) | ☐A ☐B |
| A4-13 | B-NV N-3 | `domains/NV/assumptions.md:23` | p294 句末无句点 | 句末补句点 | PDF 原样 | A | ☐A ☐B |
| A4-14 | S-INT N-1 | `domains/AG/spec.md:363` | p94 AGENRTPT Notes 同义句重复两次 | 删重复句 | PDF p94 原样即重复 | A | ☐A ☐B |
| A4-15 | S-TDM N-1 | `domains/TD/examples.md:157` | p414 - 3 days / + 1 week (符号后空格) | "+1 week" / "-3 days" (去空格) | PDF 本节写法之一; Ex1 bullet 1 无空格亦照录; S-TYPO 不归一 | A | ☐A ☐B |

### A6 与 U1 (排版字符照 PDF) 冲突的 keep-correct

| # | 批次 / id | 位置 | PDF 原值 (A=维持照录) | 候选值 (B) | 依据 | 主控建议 (草拟) | 用户选 |
|---|---|---|---|---|---|---|---|
| A6-1 | B-IS T-6 | `domains/IS/examples.md:205` | p241 STAPHYLOCOCCUS AUREUS–EPITOPE X (en dash) | en dash AUREUS–EPITOPE X (照 PDF, 按 U1) | 同例叙述 S. aureus-epitope X 用连字符 | B (U1 优先) | ☐A ☐B |
| A6-2 | B-TA T-4 | `domains/TA/examples.md:351` | p391 …10 mg – Placebo (en dash) | en dash "10 mg – Placebo" (照 PDF, 按 U1) | 同表其他行用 - | B (U1 优先) | ☐A ☐B |

### A5 结构 / 标题 / 口径 (O 项, 无单值正确答案)

| # | 来源 | 位置 | 现状 (A) | 候选 (B) | 依据 | 主控建议 (草拟) | 用户选 |
|---|---|---|---|---|---|---|---|
| A5-1 | O35-1 B-model05 / S-MOD3 M-2 | `model/05_study_level_data.md` 既有标题 | 标题缺 PDF 节号/原名; 5.1.1.1-2 / 5.1.3.1-2 / 5.1.4.1-3 共 7 个四级节与父节同为 `###` | 补 PDF 节号+原名, 四级节改 `####` | 规则 6 保留现状; S-MOD3 核过改 `####` 无锚点风险 | B | ☐A ☐B |
| A5-2 | O35-2 | `model/05` TT/TP 表 "Notes" 列 | 列名 Notes | 列名改 "Usage Restrictions" (内容实为 PDF Usage Restrictions) | B-model05 writer | B | ☐A ☐B |
| A5-3 | O35-3 / S-MOD3 M-4 | `model/05` TS 表 TSVALCD/TSVCDREF/TSVCDVER | 不补 "Not in nonclinical trials" (R1 缺列不补) | 补进与 TT/TP 同一承载列 | TT/TP 同类值已在 Notes 列, 承载不一致 | B | ☐A ☐B |
| A5-4 | O35-4 / O38-2 | `model/05`、`model/06` Role 列括注 | 括注不统一; RELSPEC 有 "(REFID)", SUPP-- QLABEL 无 "(QNAM)" | 全部统一为 `Role (Variable(s) Qualified)` | S-MOD2 已沿用此写法 | B | ☐A ☐B |
| A5-5 | O38-1 | `model/06_relationship_datasets.md` 6.1-6.7 标题 / H1 | KB 标题 (如 6.6 "Related Subjects") | PDF 原标题 (6.6 "Relationships") | 规则 6 未改 | B | ☐A ☐B |
| A5-6 | O38-3 | `model/06` RELREC USUBJID/POOLID Notes | KB 自写 (PDF 空), 未标 D6 (主控 M-2a 维持) | 加 `> KB note (not in SDTMIG):` 或删 | R1 IE 行 | B (加 D6) | ☐A ☐B |
| A5-7 | O38-4 | `model/06` RELREC APID Notes | 截断, 缺 POOLDEF 句 | 补全 PDF 句 | B-model06 audit | B | ☐A ☐B |
| A5-8 | O41 / B-model06 review | `model/06_relationship_datasets.md:50` RELTYPE Combinations 表 (D6) + Summary 表 SUPP-- "Yes" | 保留 KB 自写表 (记录级解释, 并列 MANY/ONE) | 改为指向 ch08 的交叉引用或删; Summary "Yes" 改准确说法 | 与 SDTMIG ch08 (数据集级, 3 种组合) 不一致 | B | ☐A ☐B |
| A5-9 | O48 | `domains/TI/assumptions.md` §7.4 标题 | KB 标题 | PDF "7.4 Trial Eligibility and Summary (TI and TS)" | 规则 6 未改 | B | ☐A ☐B |
| A5-10 | O56 / S-SPC2 audit | `domains/PP/examples.md` "RELREC Method Quick Reference (PP-side view)" 整节 | D6 整节保留 | 换一行交叉引用到 PC/examples.md | KB 自写摘要, 与 PC/examples.md 部分重复 | B | ☐A ☐B |
| A5-11 | O60 (S-MOD2/S-MOD3/S-TDM/S-TUFA) | TA §7.1/§7.2 自拟标题 (X-4)、FA `## §6.4.4 FA – Description/Overview` 合并标题、MB H2 "and"、SS `#####` 层级 | 规则 6 保留 KB 自拟标题 | 统一改 PDF 原标题 (先核 0 入站链接), S-TYPO 后一次性脚本 + 抽检 | S-MOD2/S-MOD3 已在 0 入站链接时改 PDF 原标题, 口径不一 | B | ☐A ☐B |
| A5-12 | S-CH10 T-4 | `chapters/ch10_appendices.md:353` | 变更表 4.1 行在 4.5 后重复, 照录两行 | 删第二行 | p454 渲染确认 PDF 原样 | A (PDF 忠实) | ☐A ☐B |
| A5-13 | t1_lane_notes "T4 统一措辞" / B-REL audit | `domains/RELREC/assumptions.md:5` D6 行 | "KB note (not in SDTMIG): … are from the SDTMIG v3.4 §8 introduction" | 改措辞避免 "not in / from" 字面矛盾 | B-REL audit LOW | B | ☐A ☐B |
| A5-14 | t1_lane_notes | 全库 D6 前缀 | 说明来源/位置的 note 也用 `> KB note (not in SDTMIG):` | 这类 note 改用 `> Note:` | 前缀语义只适用于 KB 自写内容 | B (主控 T4 意见: 只说明来源/位置的 note 改 `> Note:`, KB 自写内容保留原前缀; KB 冻结期不改, 由用户定) | ☐A ☐B |
| A5-15 | S-CH8 需主控定 #2 / B-ch08 T-5 | `chapters/ch08_relationships.md:241` | 行内 `**Example 2:**` | 改独立行 `**Example 2**` (与 :100/:119/:133/:158/:230 统一) | 改后 census 因 PDF 标签无编号失配 (OK 10→9), 需 census 侧豁免 | A | ☐A ☐B |

### A6 说明
- B-IS T-6 / B-TA T-4: 当时按 "KB 保留 hyphen" 登记为 keep-correct, 但 U1 (排版字符照 PDF) 后应改成 PDF 的 en dash。两项不是错值, 属 U1 适用范围, 建议直接交 S-TYPO 执行 (B)。B-MK T-1 所在 MK 表范围 "51–75%" 等 en dash 同理 (KB 全表用 hyphen), 归 S-TYPO。

## 2. B 组: 已按 keep-correct 写正确值, reviewer / auditor 要求让用户知悉
否决 (= 改回照录 PDF) 时按 "若否决" 列回退。

| # | id | 位置 | PDF 原值 | KB 现值 | 依据 | 若否决 | 用户选 |
|---|---|---|---|---|---|---|---|
| B-1 | B-AE T-3 | `domains/AE/examples.md:75` | p142 "probably related to the event" | related to the device | 同表 r2 AERLDEV=PROBABLE / AEACNDEV=REMOVED; 改词判断, 信心中高 | 改回 event | ☐维持 ☐否决 |
| B-2 | B-IS T-5 | `domains/IS/examples.md:153` | p237 "participating a vaccine study" | participating in | 漏介词, 单一补全 (无同文平行句) | 删 in | ☐维持 ☐否决 |
| B-3 | B-NV T-1 | `domains/NV/examples.md:11` | p296 "an fluorodeoxyglucose" | a fluorodeoxyglucose | 冠词错, 归 "拼写错" 属扩展解释 (NV review L-3) | 改回 an | ☐维持 ☐否决 |
| B-4 | B-ch01 T-1 | `chapters/ch01_introduction.md:85` | p10 "a codelist not yet been developed" | has not yet been | p49 同短语 "has not yet been developed" 为旁证 | 删 has | ☐维持 ☐否决 |
| B-5 | B-ch01 T-2 | `chapters/ch01_introduction.md:109` | p10 MANY → "--LNKID (and not --LNKGRP)" | --LNKGRP (and not --LNKID) | 同段前句 + p31 §4 --LNKGRP 定义; 需互换两名 | 两名换回 | ☐维持 ☐否决 |
| B-6 | B-EX T-6 | `domains/EX/examples.md:362` | p118 "represented in mg/mL" | mg/kg | 同句 (mg/kg) + Ex7 ec ECDOSU=mg/kg | 改回 mg/mL | ☐维持 ☐否决 |
| B-7 | S-SPC1 CP T-21 | `domains/CP/assumptions.md:24` (另 :42, :72) | p199/200/206 --BNDAGT / --GATEDEF / CPBNDAGT | --BDAGNT / --GATDEF / CPBDAGNT | spec 变量名; 改的是 Description 泛型名 (S-SPC1 需主控定 #1) | 回退 4 处 | ☐维持 ☐否决 |
| B-8 | B-FA T-7 / T-9 | `domains/FA/examples.md:118` / `:228` | p370 "parent CE record" / p373 FAEVINTX | parent AE record / FAEVLINT | writer 原判照录, review C-3 改判 (同例自证) | 两处改回 | ☐维持 ☐否决 |
| B-9 | B-MS T-3 | `domains/MS/examples.md:80` | p262 suppms IDVAR MBREFID | MSREFID | RDOMAIN=MS, IDVARVAL=ms MSREFID (原判照录, 后改判) | 改回 MBREFID | ☐维持 ☐否决 |
| B-10 | B-TS T-1 | `domains/TS/examples.md:76` | p421 TSPARM "Trial Type" (TSPARMCD=TITLE) | Trial Title | Ex1/Ex4 同码; Row 1 说明 (writer Q-2 留回退口) | 改回 Trial Type | ☐维持 ☐否决 |
| B-11 | B-ch03 T-1 / T-2 | `chapters/ch03_submitting_data.md:37` / `:49` | p18 Keys BESDTC / TESTCD | BESTDTC / FTTESTCD | 全书仅此处; 主控已裁 keep-correct (派单曾要求 Keys 逐字) | 改回 PDF | ☐维持 ☐否决 |
| B-12 | S-SPEC1 T-3 | `domains/DM/spec.md:296` | p64 脚注² URL 后孤立 ")" | 删 ")" | 脚注全文无开括号 (原判照录, 后改判) | 补回 ")" | ☐维持 ☐否决 |
| B-13 | B-DS T-2 | `domains/DS/examples.md:346` | p166 "where treatment AB +C" | where treatment is AB +C | 同表 r2 平行句 (DS review LOW) | 删 is | ☐维持 ☐否决 |
| B-14 | B-CP T-2 / T-15 | `domains/CP/examples.md:202` / `:71` 等 8 处 | CPCSMRKR / CPGATEDEF | CPCSMRKS / CPGATDEF | spec/表头; 致 fp 回退 ig34_p0215_a018 / p0218_a014 (已接受) | 改回 PDF | ☐维持 ☐否决 |
| B-15 | B-MK T-2 | `domains/MK/examples.md:53` | p293 "REPLACEMENT/ SURGICAL" | REPLACEMENT/SURGICAL | r12 同值无空格; review L-1: 实为折行歧义, 非确证印刷错 | 无需操作 (知悉即可) | ☐维持 ☐否决 |

## 3. 观察项 (照录, 不需用户选择, 仅知悉)

| id | 位置 | PDF | 说明 |
|---|---|---|---|
| B-DS U-3 | `domains/DS/examples.md:37` | p159 Ex1 123104 DSSEQ RANDOMIZED=3/COMPLETED=2 | 与日期先后一致, reviewer 判非错; 仅知悉 |
| B-DS U-5 | `domains/DS/examples.md:212` | p165 Ex10 dm 仅 Row 1/3 | 叙述明载 Not all records are shown, 非 typo |
| B-TR T-4 | `domains/TR/examples.md:44` | p356 PDF r27 NT01 结果/状态全空 | review 裁定 PDF 忠实, 仅登记 (疑 PDF 漏 TRORRES) |
| S-CH10 T-5 | `chapters/ch10_appendices.md:317` | p452 deprecate MO in SDTMIG v3.4 vs p285 in a future version | PDF 内部不一致, 各节照本节 |
| S-TDM TD U-3 | `domains/TD/examples.md:98` | p413 文字 -1 week and + 1 week vs 表 P53D/P9W | PDF 文字与表不一致 |
| S-INT review L-3 | `domains/AG/assumptions.md:5` | p92 §6.1 引言以 ":" 结尾而无列表 | PDF 自身遗漏, KB 照录正确 |
| B-MB O-d | `domains/MB/examples.md` Ex3 Row 4 说明 | "rows 5-7" 而表只有 6 行 | PDF 原文, 照录 |
| B-RE writer | `domains/RE/examples.md:59` | — | 同句 "IRREA1" 与表 REIRREA2: 已由 B-RE T-1 改正, 列此备查 |

## 4. 已裁, 不再提交用户
- 用户规则级裁定 U1-U8 (`t2_post_user_ack.md`): O40/O42 排版字符与 CRF 符号 (U1/U4)、O15/O24/O26/O34 spec 脚注与 CT `*` (U2/U7)、O17/O18/O31/O39/O45/O46/O50 章级引言宿主 (U3)、O24 C-code 记法 (U5)、DOMAIN CT (U6)、Class/Structure 行与 Cross References (U8)。
- 主控已裁: B-MH T-2 改为照录 + T4 (仍在 A1 表); B-CP T-1..T-14 全部 keep-correct (CP review "T4 用户裁定项: 无"); B-TR T-4 PDF 忠实 (review 裁定); S-CH4 #11 "(e.g. 2001-…)" 照 PDF (裁定 4); S-CH10 ② p459 空 bullet 行不落、③ App A 补整表; S-TDM TD U-1 维持照录 + T4 (仍在 A3 表); S-TUFA (1) TR T-5 照录 + T4 (仍在 A2 表)。
- O28 / O32 / O43 / O44 / O52 / O53 / O55 已并入上表 (B-BE O28、B-SM O32、B-MI O43、B-CE T-2、B-SC T-2、B-ch03 T-3/T-4、S-FND UR U-1)。

## 5. 主控待定 (非用户项, 登记时未见裁定记录)
- S-SPREL 需主控定 #3: `chapters/ch10_appendices.md:64-69` §9 引言副本与 DI 顶部重复 (D2 候选: 改一行交叉引用)。
- S-SPREL 需主控定 #4: `domains/SE/assumptions.md:17` PDF `– DTC` 已改 `--DTC` (登记 S-SPREL N-1, keep-correct); 是否归 S-TYPO。
- O51: T2 期间新改 Mermaid (TA/DM/model05/TV/TD) 统一渲染一次。
- O36 / O29 / O57 / O58 / O61: ledger 与原子回写, 属 T3。

## 6. 给 S-TYPO 的 do-not-touch 规则 (由登记推出)
1. 所有 `kb_text_span` 为 do-not-touch: 照录项不得被 "修正", keep-correct 项不得被改回 PDF 字形。
2. **变量前缀 `--` 一律不转 en dash**: PDF 多处把 `--` 印成 `–` (B-ch04/S-CH4 T-9 `--TPTREF`、S-INT EX T-8 `--PRESP`、S-CH10 T-1 `--DRVFL`、S-SPREL N-1 `--DTC`、S-FND PESCAT `–CAT`)。U1 只管引号/破折号/省略号排版, 不含变量记法。
3. 登记 cat=typo-dnt 的 22 行是空格/引号/标点类 keep-correct (如 B-FA T-1 KB 已是 “findings about”, PDF 为两个右引号): 不得按 PDF 字形回退。
4. A4 组未编号照录项 (`codelists .`、`OIVAL .`、`Services;2016`、`Nov, 2021`、人名、ch02 `“--“`、`(e.g. 2001-`、TD `+ 1 week`、AG 重复句) 在用户裁定前保持 PDF 原样。
5. B-IS T-6 / B-TA T-4 / B-MK 范围 dash: 按 U1 改 en dash 是允许的 (见 A6)。

## 7. 统计
复跑: `python3 -c "import json,collections as C;R=[json.loads(l) for l in open('.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl')];print(len(R),C.Counter(r['handling'] for r in R),C.Counter(r.get('cat','-') for r in R))"`
- 登记总行数 269: KB 写正确值 173, 照录+T4 96, 定位失败 0。(T4 主控注 2026-11-27: 之后主控补登 SR T-5, 现为 270 行 = KB 写正确值 174 + 照录+T4 96; 复跑上行命令可核。)定位按 `git show HEAD:<file>` 内容 (HEAD b982581); 工作树另有 63 个 spec.md 未提交改动 (他批), 已核本表全部行在 HEAD 与工作树同行同片段。
- 照录+T4 96 行 = A1-A4 决策行 90 + A5 的 S-CH10 T-4 1 + 观察 5; A6 的 2 行属 keep-correct。A5 另列 O 项 / 口径项 14 条 (不在 jsonl)。
- cat 分布: - 210, U1冲突 2, new 3, obs 5, typo-dnt 22, unnum 16, unnum-sp 5, 知悉 6 ('-' = 普通编号项)。
- 状态断言 (锚在表头/行号的 3 项): EX Ex6 24 行 EXENDTC 非空 0; TR Ex2 r26 TRORRES/TRSTAT/TRREASND 全空 (TRDTC 2010-04-02); ch04 lb r7 LBLOBXFL = Y。
- A2 中 TS T-2/T-3/T-4/T-6 的 CT 依据: `grep -rhoE "\| (DOSFRQ|OUTMSPRI|AGEMAX|DOSE) \|[^|]*\|" knowledge_base/terminology` → 4 码各 1 处; PCPP T-7 依据 `terminology/core/other_part3.md:212` C25529 = h。CT 属 KB 术语表, 不是 SDTMIG 正文, 故仍列 T4。
- 新发现 (登记员, 未经 reviewer): REG CP N-1 `GATE and GATEDEF` (p214)、REG SM N-1 SMSEQ 缺 with (p84, SE T-2 镜像)、REG BS N-1 `--ORNLO, --ORNHI` (p198; 同句 --STRNLO 已按 B-BS T-3 改正, 口径不一)。

## 主控补注 (2026-11-26)
- REG 报 "未见裁定" 的两项已有主控裁定: S-SPREL #3 (ch10 §9 引言副本) → S-CH10 已按 D2 换成指向 DI 的交叉引用 (已提交 b80d263); S-SPREL #4 (SE `– DTC`→`--DTC`) → 属变量名前缀修正, 保留在 S-SPREL (已提交 669405f), 不归 S-TYPO。
- O51 Mermaid 统一渲染: 留 T4 (本表 A5 类)。
- REG 新发现 3 条 (未经 reviewer, 记 O62): CP N-1 / SM N-1 / BS N-1 —— 主控建议: BS N-1 与同句 B-BS T-3 统一 (KB 写正确值); SM N-1 与 SE T-2 同型 (照录 + T4); CP N-1 交 T4 核 p214 后定。
- SR T-5 (S-CT 写入) 已由主控补进 `work/t2_pdf_typo_registry.jsonl`。
- (S-TYPO) MH/assumptions.md:27 `History“` ×2: PDF p173 原文闭引号印成开引号, KB 照录 (U1); 供知悉 —— 是否改为正确方向由用户定。
- (S-TYPO) CRF 选项符号 (CE p152 18+ 处、ch04 p32/33、ML `[X]`、DM Mermaid ☐): PDF 实为 CourierNew 字母 `o` / Wingdings 字形, U4 "照 PDF ○□" 执行口径待定; 候选 A/B 与证据页见 `evidence/checkpoints/t2_S-TYPO.md`。
- (S-TYPO) 13 行多命中不一致 + 217 行 0 命中残余: 见 `work/t2_batches/S-TYPO.residual.jsonl`, T4 人工或接受现状。
