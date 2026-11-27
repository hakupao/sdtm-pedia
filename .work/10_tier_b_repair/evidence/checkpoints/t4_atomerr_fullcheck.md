# T4 加查: "原子抽错" (ATOM_ERR, S1-R1 类) 里没被单独逐条看过的那批 — 全检汇总

<!-- chain: E (plans) -->
> **后续 (2026-11-27 夜; 见文末 §8)**: 主人直接回答 「C1、D1、追认 M-10」 → 那 1 条已由 R4L 批改回 EXACT, 8 条按 D1 维持并登记了口径. 下面 §1-§7 是加查当时的记录 (台账 md5 `43809870…`), 数字与 "现在" 都指改台账之前, 没有回改.
> 状态 (加查当时): **本轮不通过 (按派发前写死的条款: NOT_HOLD 0 且 UNVERIFIABLE 0 才算通过)** — 83 条全检 = 成立 82 / **不成立 1** / 判不了 0. 不成立的 1 条是台账标签多标 (原子其实没抽错), 不是 KB 内容错. **另有 8 条 (登记 `B-CE T-2` 那一组) 判的是成立, 但成立与否取决于一条口径 (代码值内部的一个空格算不算空白归一), 审查者点名要上面定, 主控没有裁** (§5 "问题 D"). **台账没改, KB 没改; 改不改等主人直接定 (问题 C / 问题 D)**. 2026-11-27.
> 本汇总是主控写的, **没有送独立审查**.
> 写作者 = 主控 (任务 `task_5b6b27f6c68d`, 新会话). 判定全部出自独立审查者, 主控没有改判任何一条. 路径省略前缀 `.work/10_tier_b_repair/`.
> 来由: 总闸 attempt 3 把 "ATOM_ERR / PDF_TYPO 补抽" 判为部分关 (`evidence/t4_gate_raw/attempt3_report.md` D 项); 主人 2026-11-27 选了 "加查" (协调方在任务里转述的两句: 「先加查那 83 条再说」「加查，但不挡这次发版」; 不是在本主控聊天里直接发的).

## 1. 这批原子是哪些 (确切条数与筛法)

复跑 (仓库根; 脚本断言台账 md5 = `438098704becc84eda01a925b80defaa`):

```
python3 -I .work/10_tier_b_repair/scripts/t4/t4_atomerr_sample.py
```

| 集合 | 条数 | 取法 |
|---|--:|---|
| 终态 ATOM_ERR | 197 | 台账 `verdict == "ATOM_ERR"` |
| 其中 S1-R1 类 | 157 | `matched_by.rule == "S1-R1"` (其余 40 = C7 38 + C7-K4 2, 此前都已全检) |
| 此前已被独立审查者逐条判过 | 80 | 在 T4 各轮审查的**原始结果**里有自己的判定行: 补检 `evidence/t4_supp_raw/pack_3..5.md` 74 + 总闸样本 `evidence/t4_gate_raw/pack3.md` / `pack4.md` 5 + T4.2 预筛 `evidence/checkpoints/t4_human_prescreen.md` 1; 80 条此前判定全是成立 |
| **从未被逐条判过** | **77** | 157 − 80. 清单: `work/t4/atomerr/atomerr_population.json` 的 `new` |

- 总闸报告估的 "约 83" = 157 − 74 (只扣了补检那一层). 确切数是 **77**; 差的 6 条是总闸样本 5 条 + 预筛 1 条.
- 本轮实际送审 **83 条 = 77 条 (首次) + 那 6 条 (盲复检)**: 6 条与 77 条用同一个层名、按页号混排, 审查者分不出. 这样既覆盖主人说的 "那 83 条", 又能看新审查者与先前审查者是否一致.
- 边界 (如实; 这些原子都**留在** 77 条里照查, 没有因此排除):
  - 77 条里 6 条有 T3 批 auditor 的一行勾 (`evidence/step_T3_audit.md:99-106`): `ig34_p0154_a0014`、`ig34_p0161_a0012`、`ig34_p0167_a0010`、`ig34_p0337_a002`、`ig34_p0348_a010`、`ig34_p0374_a011`.
  - 很多条的台账 `basis` 指向 T2 某批 reviewer / auditor 的一行话 — 那是这个标签的**出处** (被检验的说法), 不算独立复核.
  - 预筛那 1 条的先前判定来自 `general-purpose` (T4.2 的 AI 预筛), 不是人工判定.
- 77 条的构成: 表格行 38 / 列表项 28 / 句 6 / 表头 3 / Note 2; T3 前的旧标签 EQUIVALENT 42 / EXACT 29 / PARTIAL 5 / IE 1.

## 2. 谁审的, 怎么审的

- 口径 (派发前写死并提交, `bf303d8`): `subagent_prompts/t4/t4_atomerr_s1r1_v1.0.md` — 判定口径沿用补检 brief `t4_supp_fullcheck_v1.0.md` 的 `TRIAGE_ATOM_ERR` 层 (两半都核: ① 原子 ≠ PDF; ② KB = PDF; 表格行逐格), 只增加了输出要求 (不成立须写哪一半; 涉及已登记笔误须写登记号).
- 审查者: `oh-my-claudecode:tracer` (opus) ×4, 新实例, 只读, 并行, 全检不抽样. 与主控、与产生这些标签的角色 (T1 scientist / critic, T2 / T3 executor, 各批 code-reviewer / verifier)、与总闸角色 (`feature-dev:code-reviewer`) 都不同. 四位都自述每条看了渲染页.
- 按 brief 写死的复看: 非 "成立" 的条目连同它在包里前后各 2 条 (共 5 条, 不给先前结论, 禁读先前结果文件) 交另一类型的独立审查者 `general-purpose` (opus) 盲判.
- 原始结果: `evidence/t4_atomerr_raw/pack_{1..4}.md`、`second_look.md` (审查者自己写的文件, 主控未改). 样本包 `work/t4/atomerr/atomerr_pack_{1..4}.md` / `atomerr_pack_second.md`.

## 3. 结果

复跑 (只读解析判定栏, 断言 83 行、编号与原子一一对应、无重复、行在对应的包里):

```
python3 -I .work/10_tier_b_repair/scripts/t4/t4_atomerr_report.py
```

| 层 | 条数 | 成立 | 不成立 | 判不了 |
|---|--:|--:|--:|--:|
| 首次逐条审 (77) | 77 | 76 | **1** | 0 |
| 盲复检 (6; 先前都判成立) | 6 | 6 | 0 | 0 |
| 合计 | 83 | 82 | 1 | 0 |

- 逐条清单 (机读): `work/t4/atomerr/verdicts.json`; 逐条依据在四个 `pack_N.md` 的表里.
- 盲复检 6 条 (`ig34_p0079_a009`、`ig34_p0190_a011`、`ig34_p0236_a008`、`ig34_p0240_a011`、`ig34_p0258_a021`、`ig34_p0373_a021`) 新旧审查者一致 6 / 6.
- 复看 5 条 (E10-E14): 第二位审查者与第一位逐条一致 (E12 不成立, 其余 4 条成立), 两人互不知情.
- 样本外的 KB 内容问题: 四份结果文件的这一节都写 "无" (包 2 / 3 / 4 各附了一句顺带看到的已登记笔误, 都注明不是新问题).
- 至此终态 ATOM_ERR 197 条与 PDF_TYPO 170 条**每一条**在某一轮独立审查的原始结果里都有自己的判定行 (脚本扫各轮结果表核的: 197 / 197、170 / 170; ATOM_ERR 里 S1-R1 157 = 74 + 6 + 77, C7 38 来自 `evidence/checkpoints/t4_u5_c7_fullcheck.md`, C7-K4 2 来自补检). 复跑:

```
python3 -I .work/10_tier_b_repair/scripts/t4/t4_atomerr_coverage.py
```

### 不成立的 1 条

| 编号 | 原子 | 现标签 | 两位审查者的判定 | 事实 |
|---|---|---|---|---|
| E12 | `ig34_p0124_a001` (p124, ML Example 1 `ml.xpt` 第 2 行, 表格行) | ATOM_ERR (S1-R1) | 都是 NOT_HOLD, 都是 "①不成立" | 原子 18 格与 PDF 第 2 行逐格一致, MIDSDTC 是完整的 `2015-09-03T17:00`; KB `knowledge_base/domains/ML/examples.md:42` 也与 PDF 逐格一致. 即: 原子没抽错, KB 逐字承载 → 按标签定义是 EXACT |

- 这个标签的出处: `evidence/checkpoints/t2_B-ML_review.md:70` 的一句顺带话 "p0124_a001 (MIDSDTC 截断) 供 ledger 修正参考" → 进了 `work/t1_errata.json` → S1-R1 规则优先于逐字命中.
- 主控的机械核对 (只读, 是主控做的, 不是审查者判定): ① 台账这一行自己就带着逐字命中 (`evidence.hit_file` = `ML/examples.md`, `hit_lines` = [42], `prev_verdict` = EXACT), S1-R1 的 157 条里带逐字命中的**只有这一条**; ② `work/t3_errata.json` 给它记的 `atom_in_pdf` = false — 该行在文本层里每格折成 2-4 行 (`work/pdf_pages/ig34_p0124.txt:2-5`), T3 的 K4 复核 (原子归一化后是否是 PDF 文本的子串) 对折行的表格行测不出来. 这是主控的推断. 命令:

```
python3 -I -c "
import json
L=[json.loads(l) for l in open('.work/10_tier_b_repair/work/coverage_ledger.wc.jsonl')]
print([r['pdf_atom_id'] for r in L if r['verdict']=='ATOM_ERR' and r['matched_by'].get('rule')=='S1-R1' and r['matched_by']['evidence'].get('hit_file')])"
```

## 4. 问题 C (要主人直接定; 主控不替他选)

`ig34_p0124_a001` 现在标 "原子抽错", 两位独立审查者都判它其实没抽错.

- **C1 (主控建议)**: 改回 "逐字有" (EXACT). 只改台账 1 条标签, 不动 KB. 做法比照 R3L: 把这条从原子抽错登记里撤掉, 让回写脚本按现有的逐字命中判出 EXACT (不是硬写标签); 执行者 `oh-my-claudecode:executor` → 结构审查 `oh-my-claudecode:code-reviewer` → 重建 T0 变异基线并重跑 → 由总闸角色判这一处.
- **C2**: 维持 "原子抽错". 需要主人说明理由; 台账里会留一条已被两位审查者判为不成立的标签.

数字影响 (在台账副本上实算; 副本只把这一行的 `verdict` 改成 EXACT, 工作台账 md5 前后都是 `43809870…`):

| 口径 | 现在 | 选 C1 之后 |
|---|---|---|
| 过闸口径 U-1 B | 9860/9933 = 99.2651% | 9860/9933 = 99.2651% (**不变**) |
| strict | 9493/9933 = 95.5703% | 9494/9933 = 95.5804% (+1 条) |
| mapped | 9493/9555 = 99.3511% | 9494/9556 = 99.3512% |
| 内容指标 | 8659/9555 = 90.6227% | 8660/9556 = 90.6237% |
| 终态计数 | EXACT 4710 / ATOM_ERR 197 | EXACT 4711 / ATOM_ERR 196 |

残留仍为 0 (EXACT 也是终态类), G-TB2 不变. 复跑: 上面的 `t4_atomerr_coverage.py` (在内存里的台账副本上算, 不写台账; 输出里 `C1` 那一行), 或手工:

```
python3 -I - <<'EOF'
import json
out=open('/tmp/ledger_e12_exact.jsonl','w',encoding='utf-8')
for l in open('.work/10_tier_b_repair/work/coverage_ledger.wc.jsonl',encoding='utf-8'):
    d=json.loads(l)
    if d['pdf_atom_id']=='ig34_p0124_a001': d['verdict']='EXACT'; l=json.dumps(d,ensure_ascii=False)+'\n'
    out.write(l)
EOF
python3 -I .work/10_tier_b_repair/scripts/t4/t4_coverage_decomp.py /tmp/ledger_e12_exact.jsonl
```

## 5. 判成立、但涉及已登记 PDF 笔误的 12 条

### 5a. 问题 D: `B-CE T-2` 那 8 条 — 成立与否取决于口径 (主控不裁; 要主人或总闸角色定)

原子: E18-E25 = `ig34_p0153_a0034`、`ig34_p0154_a0002` / `a0013` / `a0014` / `a0015` / `a0029` / `a0030`、`ig34_p0155_a0002` (CE Example 2 的 mh / ce / pr 表格行).

- 事实 (两位审查者一致): PDF 把 USUBJID 印成 "ABC -US-701-002" (连字符前多一个空格), KB 照录成带空格的写法 (登记 `B-CE T-2`, 处理 = 照录); 原子写成不带空格的 "ABC-US-701-002". 每条原子与 PDF **只差这一个空格**, 其余各格一致.
- 审查者怎么判的: 包 1 审查者 (E18-E21) 与包 2 审查者 (E22-E25) 都判 **HOLDS** (原子抽错成立), 依据 brief 里 "值类一个字符都要对".
- 为什么说取决于口径: 同一份 brief 还写着 "只是空白 … 这类归一化差异不算原子抽错". 包 2 审查者明确写了: 若把代码值内部的空格也算空白归一, 这几条的 ① 不成立, 应改判 NOT_HOLD (那样按定义是 EXACT). 这两句话都是 brief (主控写的, 沿用补检 brief) 里的, 审查者定不了哪句优先.
- 与此相关的两个既有事实 (供判断, 不是结论): ① 登记 `B-CE T-2` 自己把这个空格记为 PDF 的真实印刷差异 ("PDF 8 处一致带空格; 3.5pt 字距说法不成立"), U-7 A1-7 按委托代裁定为 A (照录), 其后记录为主人确认 (`t4_owner_confirmation.md` 第一节); ② 本项目的逐字匹配器在 KB 里匹配不到这 8 条原子 (台账 `hit_file` 为空), 即项目自己的归一化不把值内空格抹掉.
- 选项: **D1 (主控建议)** 维持 ATOM_ERR (值内空格算真实差异; 与两位审查者的判定、与登记 `B-CE T-2` 一致); **D2** 算空白归一 → 8 条改 EXACT; **D3** 改记 PDF_TYPO (原子与 PDF 的差别正是登记的那处笔误).
- 数字 (副本实算, 上面 `t4_atomerr_coverage.py` 的输出; 过闸口径三种选法都不变):

| 选法 | U-1 B | strict | 终态计数 |
|---|---|---|---|
| D1 维持 (= 现在) | 99.2651% | 9493/9933 = 95.5703% | EXACT 4710 / ATOM_ERR 197 / PDF_TYPO 170 |
| D2 改 EXACT (8 条) | 99.2651% | 9501/9933 = 95.6509% | EXACT 4718 / ATOM_ERR 189 |
| D3 改 PDF_TYPO (8 条) | 99.2651% | 95.5703% | ATOM_ERR 189 / PDF_TYPO 178 |
| C1 + D2 同时 (9 条 → EXACT) | 99.2651% | 9502/9933 = 95.6609% | EXACT 4719 / ATOM_ERR 188 |

### 5b. 另 4 条: 原子另有实质抽错, 同句又碰到已登记笔误 (成立; 只是台账缺登记指针)

| 原子 | 登记 | 情况 | 台账有无登记指针 |
|---|---|---|---|
| E26 `ig34_p0161_a0012` | `B-DS T-4` (KB 写正确值) | 原子另有实质抽错 (DSCAT / DSSCAT); 同句 PDF 印 "epocch", KB 写 "epoch" | **无** |
| E64 `ig34_p0337_a003` | `B-RS T-3` (KB 写正确值) | 原子另有实质抽错 (">-3"、"RSORRESRU"); 同句 PDF 印 "a a source", KB 写 "a source" | **无** |
| E71 `ig34_p0339_a001` | `B-RS T-6` (KB 写正确值) | 原子另有实质抽错 (整句改写、"--BODYSYS"); 同句 PDF 印 "--STRNC", KB 写 "--STNRC" | **无** |
| E79 `ig34_p0361_a016` | `B-FA T-2` (KB 写正确值) | 原子另有实质抽错 (漏 "so"); 同句 PDF 印 "Section 6.4.4.,", KB 写 "Section 6.4.4," | **无** |

- 现行规则是原子抽错登记优先 (先例 `t4_thaw_W3.md:94`), 标签 ATOM_ERR 与规则一致; 台账这 4 行的登记指针是空的 → 归入 "登记指针补全" 类后续项, 等下一次改台账时一并补, 本轮不动.

## 6. 包里指针偏的地方 (审查者已自己重新定位, 不影响判定)

E3 → `ch04:1478`; E19-E21 → `CE/examples.md:102` / `:123` / `:124`; E46 / E47 → `MB/examples.md:116` / `:122`; E51 (包里没给) → `PC/examples.md:146`; E65-E71 包里给的是 FT 副本, 实核 `RS/assumptions.md`; E63 / E64 原子页号标 p337, 内容实际在 p336.

## 7. 状态与后续

- KB 树 `63f857774a42cfaa71798705ad40ab51bc5e378a` 不变; 台账 md5 `438098704becc84eda01a925b80defaa` 不变; 没 push, 没打 tag, 没做 T4.3.
- 总闸报告那一项 ("ATOM_ERR / PDF_TYPO 补抽 = 部分关") 现在的事实: ATOM_ERR 与 PDF_TYPO 两类每一条都已有独立审查者的逐条判定; ATOM_ERR 里查出 1 条多标 (问题 C), 另 8 条取决于口径 (问题 D), 都待主人定. **这一项由 "部分关" 改判成什么, 不由主控判** (规则 D) — 由总闸角色 (`feature-dev:code-reviewer` 新实例) 或协调方判; 主人选了 C1 并改完之后, 可以和那一处的 delta 闸审一起判.
- 规则 B 归档: `evidence/failures/step_T4.AE_attempt_1.md`.

## 8. 后续: 主人的回答与 R4L (2026-11-27 夜)

- 主人在主控聊天里直接回答 (逐字): 「C1、D1、追认 M-10」 (`evidence/checkpoints/t4_owner_confirmation.md` 消息 5).
- **问题 C = C1**: `ig34_p0124_a001` 由 R4L 批改回 EXACT (提交 `65d6a0f`). 做法: 撤掉它的原子抽错登记 (原条目存进 `work/t3_errata.json` 的 `r4l_revoked`), 由现有的逐字命中规则 `live-hit` 判出 EXACT, 不是硬写标签. 执行者 `oh-my-claudecode:executor` (`evidence/checkpoints/t4_round4_ledger_W.md`) → 结构审查 `oh-my-claudecode:code-reviewer` PASS, 小修后 delta PASS (`evidence/checkpoints/t4_round4_ledger_review.md`). 清单外标签变化 0. 同批给 §5b 那 4 条补了登记指针 (只改 `evidence.registry`; 第三条的登记号全名是 `B-RS T-6 (RS 副本)`).
- **问题 D = D1**: `B-CE T-2` 那 8 条维持 ATOM_ERR. 口径登记在 `evidence/checkpoints/t4_user_decisions.md` §000c 问题 D 行: 代码值 / 标识符内部的空格是值的一部分, 差一个空格算真实差异, 不属于 "空白归一"; 加查 brief 文末已补这两句话的先后说明.
- **现值** (R4L 后; 台账 md5 `eef9bb14e5afab7e68a231ddd18cfa1c`; `python3 -I .work/10_tier_b_repair/scripts/t4/t4_coverage_decomp.py`): U-1 B 9860/9933 = 99.2651%; strict 9494/9933 = 95.5804%; mapped 9494/9556 = 99.3512%; 内容 8660/9556 = 90.6237%. 终态 EXACT 4711 / EQUIVALENT 3949 / IE 2559 / PDF_TYPO 170 / ATOM_ERR 196 / FIG 11. 与 §4 的预演值 (C1 那一列) 相同.
- 复跑说明: `scripts/t4/t4_atomerr_sample.py` 断言的是加查当时的台账, R4L 之后按设计会失败 (人群已固定在 `work/t4/atomerr/atomerr_population.json`); `t4_atomerr_report.py` 与 `t4_atomerr_coverage.py` 已改为对照改前备份 `work/coverage_ledger.wc.pre_r4l.jsonl`, 仍可复跑, 后者同时打印工作台账的现值.
- "ATOM_ERR / PDF_TYPO 补抽" 那一项的状态与问题 D 的处理是否足够: 交总闸角色判 (brief `subagent_prompts/t4_gate_reviewer_v3.2.md`), 结论见 `evidence/checkpoints/t4_gate_review.md` 文末.
