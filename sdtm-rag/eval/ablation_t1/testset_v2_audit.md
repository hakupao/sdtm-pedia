# test_set_v2.yml — 新增 48 题语义审计 (独立审计者 / 规则 A + D)

> 审计者: verifier subagent (不是出题人)
> 审计日期: 2026-06-09
> 范围: v2 里 id 不在 v1 的 48 道新题 = q54-q101
> 方法: 逐题真打开每个 expected_source 文件, 语义核验 (1) gold 真答得上 (2) 分类正确 (3) gold 完整 (4) 题目无歧义
> 评测口径: source recall = 子串匹配 (`expected in retrieved_source`); expected_facts 大小写不敏感子串匹配

## 统计

| 维度 | 数量 |
|------|------|
| 总新题 | 48 |
| PASS (无需改) | 43 |
| 需修 (FIX/FLAG) | 5 |
| —— 其中 高严重度 (分类错/gold 不全/gold 不对) | 1 (q101) |
| —— 其中 中严重度 (gold 源次优/可补) | 4 (q89, q94, q96, q97/q98/q99/q100 见说明) |

实质性"需修"清单 (去重后): **q101 (高), q89 (中), q94 (中), q96 (中)** + 一类共性观察 (mixed 单源, 见末尾)。

---

## 逐题审计表

### Single Domain (q54-q65)

| id | 类别 | 判定 | 问题描述 | 建议修法 |
|----|------|------|----------|----------|
| q54 | single_domain | PASS | DV/spec.md: Class=Events, DVTERM=Protocol Deviation Term (Topic). 四个 fact 全部语义命中。 | 无 |
| q55 | single_domain | PASS | DS/spec.md: Class=Events, DSTERM (Topic, label "Reported Term for the Disposition Event"), 结构行含 "disposition"。题问 DSTERM 角色, 文件可答。 | 无 |
| q56 | single_domain | PASS | SU/spec.md: Class=Interventions, SUTRT=Reported Name of Substance (Topic)。全命中。 | 无 |
| q57 | single_domain | PASS | PR/spec.md: Class=Interventions, PRTRT=Reported Name of Procedure, Core=Req。全命中。 | 无 |
| q58 | single_domain | PASS | TS/spec.md: Trial Summary, TSPARMCD=C66738 (Topic), CDISC Notes 明写 "limited to 8 characters"。全命中。 | 无 |
| q59 | single_domain | PASS | DD/spec.md: DDTESTCD Controlled Terms=C116108 (Topic)。题问 DDTESTCD 的 codelist code = C116108, 正确。 | 无 |
| q60 | single_domain | PASS | CE/spec.md: Class=Events, CETERM (Topic, label "Reported Term for the Clinical Event")。全命中。 | 无 |
| q61 | single_domain | PASS | MB/spec.md: Class=Findings, MBTESTCD=C120527 (Topic)。全命中。 | 无 |
| q62 | single_domain | PASS | SS/spec.md: SSTESTCD=C124305 (Topic), Class=Findings。全命中。 | 无 |
| q63 | single_domain | PASS (措辞依赖) | SC/spec.md: 结构行 "One record per characteristic per visit per subject" 含 "one record per characteristic"; 标题/正文含 "Subject Characteristics", Class=Findings。大小写不敏感命中。 | 无 (若 matcher 改大小写敏感需复查, EOF 已自标) |
| q64 | single_domain | PASS (措辞依赖) | PC/spec.md: 结构行含 "concentration" 和 "analyte", Class=Findings。命中。 | 无 |
| q65 | single_domain | PASS (措辞依赖) | DA/spec.md: 结构 "One record per product accountability finding per subject" 含 "Product Accountability"(标题) + "per subject", Class=Findings。命中。 | 无 |

### Cross Domain (q66-q77)

| id | 类别 | 判定 | 问题描述 | 建议修法 |
|----|------|------|----------|----------|
| q66 | cross_domain | PASS | VARIABLE_INDEX.md: VISITNUM 行 (36 域) 含 LB, VS; Label "Visit Number"。全命中, 真分布题。 | 无 |
| q67 | cross_domain | PASS | VARIABLE_INDEX.md: C66742 CT 行 (共 123 个) 含 AE.AESER, AE.AESDTH。"how many" 由 "共 123 个" 可答。 | 无 |
| q68 | cross_domain | PASS | VARIABLE_INDEX.md: C66789 行 (36 域 --STAT) 含各域 STAT; Label "Completion Status"。可答哪些域 + --STAT 含义。 | 无 |
| q69 | cross_domain | PASS | VARIABLE_INDEX.md: C71620 行 (58 个) 含 EX.EXDOSU, CM.CMDOSU。全命中。 | 无 |
| q70 | cross_domain | PASS | RELSUB/spec.md: RSUBJID (Related Subject or Pool Identifier), USUBJID, SREL 全在; 可答 RSUBJID 持有什么。 | 无 |
| q71 | cross_domain | PASS | VARIABLE_INDEX.md: C78735 行 (19 个) 含 PE.PEEVAL; "EVAL" 子串命中。 | 无 |
| q72 | cross_domain | PASS | chapters/ch08_relationships.md §8.6.2: PC/PP 区别 (PC=concentration, PP=parameter), 解释为何分两域 (多 topic / 不同结构)。全命中。 | 无 |
| q73 | cross_domain | PASS | model/06_relationship_datasets.md: RDOMAIN "2-character abbreviation for the domain of the parent record(s)" — "parent"+"2-character" 命中。 | 无 |
| q74 | cross_domain | PASS | model/06: Naming Convention "suppae.xpt", RDOMAIN, "supp--.xpt" 全在。命中 (suppae/supp-- 大小写不敏感)。 | 无 |
| q75 | cross_domain | PASS | model/02 §3.1.4: "at least 1 of: USUBJID, SPDEVID, or POOLID"。三 fact 全在。 | 无 |
| q76 | cross_domain | PASS | model/04_associated_persons.md: APID, RSUBJID, SREL 链接机制全述。命中。 | 无 |
| q77 | cross_domain | PASS | VARIABLE_INDEX.md: EPOCH 行 (44 域) 含 AE, EX; Role=Timing。命中。 | 无 |

### Concept (q78-q89)

| id | 类别 | 判定 | 问题描述 | 建议修法 |
|----|------|------|----------|----------|
| q78 | concept | PASS | ch04 §4.2.1: --TESTCD "limited to 8 characters and cannot start with a number, nor ... characters other than letters, numbers, or underscores"。三 fact 全在。 | 无 |
| q79 | concept | PASS | ch04 §4.2.5: "Missing values are represented as null. When a test is not performed, use --STAT = NOT DONE and --REASND"。null/NOT DONE/STAT/REASND 全在。 | 无 |
| q80 | concept | PASS | ch04 §4.3.7: "Use of Yes and No Values" + "single checkbox indicates Yes ... permissible to populate only 1 value"。Yes/No/single checkbox 全在。 | 无 |
| q81 | concept | PASS | ch04 §4.2.2: "2-character domain code is limited to A-Z for the first character, and A-Z, 0-9 for the second"。2-character/A-Z/0-9 全在。 | 无 |
| q82 | concept | PASS | model/02 §3.1.4: "STUDYID, DOMAIN, and --SEQ are required ... must also include at least 1 of: USUBJID, SPDEVID, or POOLID"。STUDYID/DOMAIN/SEQ/USUBJID 全在 (SEQ 以 "--SEQ" 出现)。 | 无 |
| q83 | concept | PASS | model/06: RELREC 表含 RDOMAIN (Identifier), 述 link records/datasets。RELREC/RDOMAIN/Identifier 全在。 | 无 |
| q84 | concept | PASS | ch08 §8.6.1: "An intervention is something ... expected to have a physiological effect" / "An event is something that happens ... spontaneously"。intervention/event/physiological effect 全在。 | 无 |
| q85 | concept | PASS | model/04: "Associated Persons", prefix "AP", "APDM" 例。全在。 | 无 |
| q86 | concept | PASS | ch04 §4.1.5: Expected 变量 "may contain some null values ... comment must be included in the Define-XML document"。Expected/null/Define-XML 全在。 | 无 |
| q87 | concept | PASS | ch08 §8.6.3: "the choices ... are a supplemental qualifier or in an FA record. ... represented as a supplemental qualifier unless ... stored in FA"。Findings About/supplemental qualifier/event 全在。 | 无 |
| q88 | concept | PASS | ch04 §4.2.1: ETCD/TSPARMCD 限 8 字符无字符限制; "ARMCD is limited to 20 characters"。四 fact 全在。 | 无 |
| q89 | concept | **FLAG (中)** | gold 指 model/02_observation_classes.md §3.1.5。该文件确**含** --STRF/--ENRF/--STRTPT 及值 (BEFORE), 子串全命中, 技术上可答。**但**相对时间变量"取什么值/用法规则"的**权威专章是 ch04_general_assumptions.md §4.4.7 "Use of Relative Timing Variables"** (含完整值集 BEFORE/DURING/DURING-AFTER/AFTER/UNKNOWN 及限制)。种子问题判断正确。 | 把 `chapters/ch04_general_assumptions.md` **加入** expected_sources (与 model/02 并列), 让追全类逼近 100% 时不漏掉更对症的源。分类(concept)无需改。 |

### Mixed (q90-q101)

| id | 类别 | 判定 | 问题描述 | 建议修法 |
|----|------|------|----------|----------|
| q90 | mixed | PASS | EX/spec.md: EXROUTE=C66729; terminology/core/interventions.md (C66729) 含 INTRAVENOUS (BOLUS/DRIP 子串命中)。真双源。 | 无 |
| q91 | mixed | PASS | DS/spec.md: DSDECOD Controlled Terms=C66727; terminology/core/disposition.md (C66727) 含 "LOST TO FOLLOW-UP"。真双源。 | 无 |
| q92 | mixed | PASS | DM/spec.md: ETHNIC=C66790; terminology/core/dm.md (C66790) 含 "HISPANIC OR LATINO"。真双源 (EOF 已注: 值在 dm.md, spec 只给变量+码)。 | 无 |
| q93 | mixed | PASS | EX/spec.md: EXDOSFRM=C66726; terminology/core/interventions.md (C66726) 含 "TABLET"。真双源。 | 无 |
| q94 | mixed | **FLAG (中)** | 仅 1 个 gold = LB/spec.md。LBORRES/LBSTRESC/C102580 三 fact **全在 LB/spec.md** (LBSTRESC Controlled Terms=C102580)。一个文件即答全 → 不符合 mixed "必须 ≥2 源" 定义。 | 改类为 **single_domain**; 或保留 mixed 但补第二源 (如 terminology/core/lb_part4.md, C102580 在此)。 |
| q95 | mixed | PASS | DD/spec.md: DDTEST=C116107, Class=Findings。三 fact 全在单文件 — 但题面只需域 spec, 且其他 mixed 同构, 不单独挑。见 q94 共性说明。 | 见末尾共性 |
| q96 | mixed | **FLAG (中)** | 仅 1 个 gold = FA/spec.md。FATEST/C101833 两 fact **全在 FA/spec.md**。一个文件即答全 → 不符合 mixed 定义。 | 改类为 single_domain; 或补 terminology/core/findings_about.md (C101833 在此)。 |
| q97 | mixed | PASS (类别偏) | 仅 1 个 gold = TI/spec.md。IECAT=C66797/IETESTCD 全在 TI/spec.md。语义可答, 但同 q94 属"单源 mixed"。题面无需第二源。 | 见末尾共性 (可降级 single_domain) |
| q98 | mixed | PASS (类别偏) | 仅 1 个 gold = CM/spec.md。CMDOSU/C71620/"Dose Units" 全在 CM/spec.md。单源 mixed。 | 见末尾共性 |
| q99 | mixed | PASS (类别偏) | 仅 1 个 gold = QS/spec.md。QSORRESU/C71620/"per question"(结构行) 全在 QS/spec.md。单源 mixed。 | 见末尾共性 |
| q100 | mixed | PASS (类别偏) | 仅 1 个 gold = TA/spec.md。ARMCD(Topic)/ETCD(Element Code) 全在 TA/spec.md。单源 mixed (纯结构题, 无 terminology 成分)。 | 见末尾共性 (此题最像 single_domain) |
| q101 | mixed | **FIX (高)** | 仅 1 个 gold = TS/spec.md。TSPARM/C67152/"40 characters" 三 fact **全在 TS/spec.md** (TSPARM Controlled Terms=C67152, CDISC Notes "cannot be longer than 40 characters")。一个文件答全 → 应是 single_domain, 不是 mixed。种子问题判断正确。 | 改类为 **single_domain** (推荐); 或若要保 mixed 须补第二独立源 (如 terminology/core/trial_design.md, C67152 在此)。 |

---

## 共性观察: "单源 mixed" 一类 (q94, q95, q96, q97, q98, q99, q100, q101)

按四类别定义, **mixed = 必须 ≥2 个不同来源综合 (典型 spec.md + terminology) 才能完整回答**。
下列新 mixed 题的 gold 只列了 1 个 domain spec 文件, 且该单文件即可答全 expected_facts:

- **q101** (TS): TSPARM + C67152 + 40 chars 全在 TS/spec.md → 高严重度 (种子已点名), 建议改 single_domain。
- **q94** (LB): LBORRES/LBSTRESC/C102580 全在 LB/spec.md → 中, 改 single_domain 或补 lb_part4.md。
- **q96** (FA): FATEST/C101833 全在 FA/spec.md → 中, 改 single_domain 或补 findings_about.md。
- **q95, q97, q98, q99, q100**: 同构, gold 单 spec 文件即答全。其中 q100 (TA: ARMCD/ETCD) 纯结构无 terminology 成分, 最像 single_domain。

**根因**: 这批 mixed 题里, codelist **code** (Cxxxxx) 本身就印在 domain spec 的 "Controlled Terms" 字段, 所以"变量+码+长度/角色"类问题单 spec 即可答; 只有当问题要求**列出 codelist 里的具体值/术语** (如 q90 INTRAVENOUS, q91 LOST TO FOLLOW-UP, q92 HISPANIC OR LATINO, q93 TABLET) 时才真需要 terminology 第二源。前者(q94/q96/q101 等)实为 single_domain。

**两条修法路线 (交主决策, 本审计不改 yml)**:
1. **重分类**: 把单源、且 expected_facts 不含具体 codelist 值的题 (q94/q96/q101, 可能含 q95/q97/q98/q99/q100) 降为 single_domain。优点: 类别定义自洽; 缺点: mixed 计数从 25 降。
2. **补第二源**: 给这些题各补一个 terminology gold (code 对应的 terminology/core/*.md), 并可微调题面要求"列出该 codelist 的具体值", 使其真正成为双源题。优点: 保住 mixed 计数与跨源检索压力测试; 缺点: 改动较大, 且要确保题面真的逼着模型去 terminology 文件。

> 注: 上面 v2 header 声明 "Category totals (v2): mixed (25)"。若采路线 1 重分类, header 计数需同步更新 (q01-q48 区块的旧 mixed 题不在本次审计范围, 仅动 q90-q101 新题)。

---

## 结构 vs 语义结论

- **结构层** (gold 文件存在 + expected_facts 可定位): 48/48 通过, 与交接一致。
- **语义层** (本审计): gold 文件**语义上真能答**的题 = 48/48 (含 FLAG 的 q89/q94/q96/q101 也都能从所列 gold 子串命中并语义答出)。
- **真正问题不在"答不上", 而在"分类/源选择不最优"**:
  - 1 道分类错 (q101, mixed→single_domain) — 高。
  - 1 道源次优 (q89, 应并入 ch04 §4.4.7) — 中。
  - 2+ 道单源 mixed 不符 mixed 定义 (q94/q96, 及共性里的 q95/q97/q98/q99/q100) — 中。
- 无"题目歧义/多合理答案/依赖 KB 外知识"的题; 所有新题措辞清晰、像真实用户提问。
