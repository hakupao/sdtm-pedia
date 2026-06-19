# SP2 Task 13 — Phase 1 paired eval, attempt 1 (FAILURE: gate false positives)

> 2026-06-20 · Rule B archive. OFF-vs-ON paired eval, DeepSeek `deepseek/deepseek-chat`, temp=0, v3 140q.
> Arms: OFF = structured_lookup+hybrid+guardrail ON, structured-answer OFF. ON = + structured-answer.
> Outputs: `eval/prod_wirein/v3_sp2_off_t0.json` / `v3_sp2_on_t0.json`.

## Verdict: CHANNEL passes, GATE fails. Not a clean Task-13 PASS.

### Channel (injection) — PASS
- **q103 TAETORD**: fr 0.50→1.00 GREEN ("...TAETORD 出现在 43 个 SDTM 域... Planned Order of Element within Arm"). Channel fired.
- **q104 VISITDY**: fr 0.50→1.00 GREEN ("VISITDY...36 个 SDTM 域...Planned Study Day of Visit" + full domain list). Channel fired.
- **source_recall**: 0.9964 → 0.9964 (zero retrieval regression — Phase 1 doesn't touch retrieval, confirmed).
- **overall**: 0.8916 → 0.8916 (flat).
- **fact_recall by category**: concept +0.0034, single_domain +0.0187, mixed +0.0100, **cross_domain −0.0217**.
- **cross_domain −0.0217 dissected** (50 q): 5 regressed / 5 improved. Of the 5 regressors, **4 had the channel NOT fire** (q125/q116/q66/q73) → identical input both arms → DeepSeek temp=0 nondeterminism, NOT SP2. The 1 channel-fired "regressor" (q34) is itself a gate false-positive on a correct, more-complete answer. **Channel-fired questions net +1.08 fr summed** (q103/q104/q68/q77 up). Conclusion: no real channel-caused regression; the aggregate dip is hosted-model noise.

### Gate (apply_counting_gate) — FAIL: 36 false positives, 0 genuine
Channel fired on 56/140 questions; gate raised **36 violations across 26 questions; ALL 36 are false positives** (the correct expected value is present in the answer in every case; 4 also state physically-impossible domain counts >63).

**Root causes** (crude `_stated_numbers_near` heuristic):
1. **Kind conflation**: collects ANY integer in a sentence mentioning the subject. e.g. q34 C66742: model correctly said "包含 4 个值 ... 该 codelist 被 41 个 SDTM 域使用" — gate grabbed the term-count "4", missed "41" (it sits in the next sentence referring to the codelist by pronoun "该 codelist"), flagged "expected 41 stated 4".
2. **No plausibility bound**: flagged 200 (q27 IETEST, a char limit), 99 (q32), 100 (q67), 830 (q69 — a code/term number) as "domain counts" though only 63 domains exist.
3. **Pronoun reference**: the correctly-stated count is often in a sentence that refers to the subject as "this codelist/variable", which the subject-substring scope misses.
4. **Bilingual**: answers are frequently Chinese ("41 个 SDTM 域") even for English questions (pre-existing DeepSeek behavior), so English-only "N domains" patterns wouldn't help without bilingual handling.

**Key data point for the fix**: 36/36 false positives have `cc.value` (the correct count) present in the answer text. A gate that only fires when the correct value is ABSENT would have 0 false positives on this run.

## Next attempt input
Redesign the gate to high precision: fire ONLY when (a) the correct value is absent from the answer, (b) a stated number is plausible as that kind of count (domains ≤ n_domains), and (c) it is count-shaped near the subject+kind word (bilingual). Re-apply the fixed gate to the saved 140 ON answers (no eval re-run needed) → expect 0 violations. OPEN QUESTION for user: keep production "append correction" (Q5) with the precise gate, or make the gate eval-log-only (no answer mutation) since injection already delivers the count.

---

## Re-run 2026-06-20 (fresh OFF+ON full 140q, corroborates above)
独立重跑 (deepseek-chat temp0, 同配方), 结论一致, 数字略有 temp0 抖动差异:
- q103 fr 0.5→1.0 GREEN (含 "43" + "Planned Order of Element within Arm"); q104 fr 0.5→1.0 GREEN (含 "36" + "Planned Study Day of Visit" + 36 域全列). 两靶子 **0 闸 violation**.
- src 99.6%→99.6% (+0); fact AVG 78.7%→79.1% (+0.4); 净 +7 题 (15 gain / 8 drop).
- fact 分类: concept +3.1, mixed +2.0, cross_domain **−1.0**, single_domain **−0.6**.
- **8 drop 逐题核证**: 6/8 在通道未触发题 (q35/q66/q116/q125/q133/q136) = LLM temp0 非确定性噪声; 2/8 在通道触发题 (q25 "Verbatim"→中文"逐字"同义伪降; q34 "NY"→全称, 且 ON 由 OFF 误判 2 域→正确 41 域全列, 实为重大 gain). **0 真实通道稀释**.
- 计数闸独立复跑: **36 violation (非 0)**, 跨 26 题, 逐条抓触发句核证 **36/36 全误报** (字符限值 8/200/40/20, 术语数 4/52/106/135, 章节号 §4.4.5, 示例 99/Example5, 表行号, 另一变量 ETCD≠ARMCD). 模型实际域/变量计数均对; 闸非破坏性追加真事实, 从不产错答案.
- **验收**: (a) PASS, (b) PASS (真实零回归), (c) **字面 FAIL** (36≠0) / 实质 0 真矛盾. 故不作 clean three-criteria PASS commit.
- 证据 checkpoint: `evidence/checkpoints/sp2_phase1_paired_eval.md`. 数据: `v3_sp2_{off,on}_t0.json` + `v3_sp2_paired_t0.log`.
