# T4 加查 (ATOM_ERR S1-R1) attempt 1 — 不通过 (规则 B 归档)

<!-- chain: E (plans) -->
> 状态: **不通过; 等主人定问题 C 与问题 D** (2026-11-27). 失败数据全部保留, 未删未改.

- **输入**: HEAD `88e1918` 的 KB (树 `63f857774a42cfaa71798705ad40ab51bc5e378a`) 与台账 (md5 `438098704becc84eda01a925b80defaa`); 样本 `work/t4/atomerr/atomerr_sample.jsonl` (83 条 = 首次 77 + 盲复检 6; md5 `b1c4c2cfbc316849989cd92771ca5af3`), 包 `work/t4/atomerr/atomerr_pack_{1..4}.md`; brief `subagent_prompts/t4/t4_atomerr_s1r1_v1.0.md` (判定口径与后果派发前写死, 提交 `bf303d8`).
- **产物**: 审查者 (`oh-my-claudecode:tracer` ×4) 原始结果 `evidence/t4_atomerr_raw/pack_{1..4}.md`; 复看 (`general-purpose`) `evidence/t4_atomerr_raw/second_look.md`; 逐条机读 `work/t4/atomerr/verdicts.json`; 汇总 `evidence/checkpoints/t4_atomerr_fullcheck.md`.
- **技术判定**: 83 条 = HOLDS 82 / **NOT_HOLD 1** / UNVERIFIABLE 0. NOT_HOLD = `ig34_p0124_a001` (E12; ① 不成立: 原子与 PDF p124 `ml.xpt` 第 2 行逐格一致, 没抽错; KB `domains/ML/examples.md:42` 与 PDF 逐字一致). 第二位不同类型的独立审查者盲判结论相同. 盲复检 6 条与先前判定一致 6 / 6.
- **取决于口径的 8 条 (未裁)**: `B-CE T-2` 那组 E18-E25, 两位审查者都判 HOLDS, 但包 2 审查者写明 "若代码值内部的空格算空白归一则 ① 不成立" — brief 里 "空白归一不算抽错" 与 "值类一个字符都要对" 两句没说哪句优先 (brief 的缺口, 主控写的). 列为问题 D 交主人 / 总闸角色; 汇总 §5a.
- **业务判定**: 按写死条款 "通过 = NOT_HOLD 0 且 UNVERIFIABLE 0" → **不通过**. 不是 KB 内容错, 是台账标签多标 (ATOM_ERR 应为 EXACT). 对过闸口径 U-1 B 无影响 (99.2651% 不变); strict +1 条 (95.5703% → 95.5804%, 台账副本实算).
- **成因 (主控推断)**: 标签出自 `evidence/checkpoints/t2_B-ML_review.md:70` 的一句顺带话, 经 `work/t1_errata.json` 进入 S1-R1; T3 的 K4 复核 (原子是否是 PDF 文本层的子串) 对每格折行的表格行测不出来 (`work/t3_errata.json` 该条 `atom_in_pdf` = false). S1-R1 157 条里台账自带逐字命中的只有这一条.
- **下一 attempt 输入**: 主人对问题 C 的直接回答 (C1 改回 EXACT / C2 维持并说明理由) 与对问题 D 的回答 (D1 维持 / D2 改 EXACT / D3 改 PDF_TYPO). 下次再用这份 brief 须先把 "值内空格" 的口径写明. 选 C1 → 比照 R3L: writer `oh-my-claudecode:executor` (从原子抽错登记撤掉这一条, 由回写脚本按现有逐字命中判出 EXACT) → reviewer `oh-my-claudecode:code-reviewer` → `t0_mutation_head.sh --make-baseline` + 变异 → `t4_supp_report.py` / `t4_ack_lists.py` / `t4_coverage_decomp.py` 重跑 → 总闸角色对这一处做 delta 判断. 同批可顺带补 4 条登记指针 (`ig34_p0161_a0012` / `ig34_p0337_a003` / `ig34_p0339_a001` / `ig34_p0361_a016`; 汇总 §5).
