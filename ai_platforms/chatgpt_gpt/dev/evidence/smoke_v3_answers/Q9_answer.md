# Q9 (B6 — AESEV vs AETOXGR vs AESER) NCI CTCAE 严重度场景

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83b36-4f8c-83a7-9ee0-17f82f06bdd1
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: ~3 分钟

## 完整回答 (一句话总结摘录)

在 oncology + CTCAE v5 里:
- **AETOXGR** = CTCAE 分级 (0-5 grade)
- **AESEV** = MILD/MODERATE/SEVERE 强度词
- **AESER** = 是否 serious (Y/N)
- **三者相关但不等价**

如果只收了 CTCAE grade, 提交时填 AETOXGR, **AESEV 留空**, AESER 仍按 serious 规则单独处理.

### (a) AESEV 与 AETOXGR codelist

- AESEV: 三档定性强度词 — MILD / MODERATE / SEVERE
- AETOXGR: 整数分级 (CTCAE 0-5 或类似量表如 WHO Grade), 由 sponsor 在 CRF 收集时指定的 toxicity grading scale 决定 (AETOXGRS 记 scale 名称 "CTCAE v5.0")

### (b) Source vs Derive

- **如果方案在 CRF 里收集 CTCAE Grade, 那 CTCAE Grade 就是源数据**, AETOXGR 是 source 真实值
- **AESEV 可以通过预定义映射规则从 AETOXGR 派生** (如 Grade 1 → MILD, Grade 2 → MODERATE, Grade 3-4 → SEVERE), 但这是 sponsor 决定的 mapping rule, 必须在 Define-XML 里说明
- **更稳妥的做法**: 如果 CRF 没收集 AESEV, 就 AESEV 留空, 不强行 impute

### (c) AESER vs AESEV/AETOXGR 是否同一维度

**不是同一维度**.

- AESEV / AETOXGR 反映 clinical severity (严重程度强弱)
- AESER 是 regulatory seriousness (ICH E2A 6 项 SAE 标准: 死亡/危及生命/住院/致残/先天异常/其他重要医学事件)
- 两者独立: 一条 AE Grade 1 也可能 SAE (例如轻度过敏导致住院); 一条 AE Grade 5 必然 = 死亡, 那是 SAE 之一

**Grade 5 是否一定 Serious=Y**:
- CTCAE Grade 5 = death related to AE
- 死亡是 ICH E2A SAE 6 项之一, 因此 Grade 5 → AESER=Y, AESDTH=Y (如果 SAE 收集了)
- 但反向不成立: 不是所有 AESER=Y 都是 Grade 5

### (d) 只收 CTCAE Grade, AESEV 怎么填

**AESEV 留空 (null)**, 不要强行用 AETOXGR derive 出 AESEV 值.

理由:
- AESEV 是 source data (CRF 直接收集); 如果 CRF 不收集 AESEV, SDTM 就不应该捏造它
- 如需后续分析层用强度词, 由 ADaM 在 ADAE 里 derive (with imputation flag)
- AETOXGR 单独提交即可; AETOXGRS 字段标识用的是哪个 scale ("CTCAE v5.0")

**不能机械等价**:
- 不能因为 AETOXGR=3, 就默认补 AESEV=SEVERE
- 不能因为 AETOXGR=5, 就把 AESER 当成同义变量处理 (AESER 仍走 ICH E2A 6 项判定)

## 判据对齐

- (a) AESEV codelist (MILD/MOD/SEV) + AETOXGR (CTCAE grade 0-5) ✓
- (b) Source = CTCAE Grade (CRF 真实采集) ✓; AESEV 可 derive 但需 mapping rule ✓
- (c) AESER 不同维度 (regulatory ICH E2A 6 项) vs severity ✓; Grade 5 → AESER=Y 但反向不成立 ✓
- (d) AESEV 留空 (不强行 impute), AETOXGR 单独提交 ✓
- bonus: AETOXGRS 字段标 scale 名称 ✓
- bonus: ADaM derive 而非 SDTM derive 的层次区分 ✓
- bonus: AESDTH 与 AESER Grade 5 协同 ✓

源溯源命中:
- `<!-- source: knowledge_base/domains/AE/assumptions.md -->`
- `<!-- source: knowledge_base/domains/AE/examples.md -->`
- `<!-- source: knowledge_base/model/02_observation_classes.md -->`
- `<!-- source: knowledge_base/terminology/core/ae.md -->`

## 归因

PASS — Pure generalization. AE 三维 (severity / toxicity grade / seriousness) 完全分清, 不互相机械等价; CTCAE grade 5 → AESER=Y 单向关系答对; AESEV 留空策略正确 (不 impute). 思考时长正常.
