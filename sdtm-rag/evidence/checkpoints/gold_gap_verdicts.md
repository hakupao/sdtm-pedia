# gold 缺口独立判定 (Task 3 Step 6)

> 判定方: task3-adjudicator (独立 agent, 与扫描工具作者隔离 —— 规则 D)
> 输入: `evidence/checkpoints/gold_gap_scan.json` (140 题, 97 题有 unmatched, 共 182 条)
> 正文核验对象: **被召回 chunk 的实际正文**, 从 `data/chroma` 的 `sdtm_kb_v1` collection 按 (source, section) 取回 (182 条全部取到, 0 条 NOT FOUND), 必要时回 `knowledge_base/` 原文对行号
> 日期: 2026-08-07

**结论一句话**: 182 条里 **27 条判 `遗漏_应补`(涉及 26 题), 119 条 `相关但非权威_不补`, 36 条 `不相关_不补`**。q38 不是孤例 —— 存在一个与它同构的系统性缺口: **`terminology/core/*.md` 码表 chunk 抬头的 `Used by variable(s): …` 交叉引用行逐字回答"哪些变量/域用码表 C"与"变量 V 用哪个码表", 但 14 条这类命中不在 gold 里**, 且同题集内**同形题的 gold 写法互相矛盾**(q16/q92/q96/s01 收了 `terminology/core/*.md`, 孪生的 q43/q45/q46/q48 没收)。

---

## 1. 判定原则

### 1.1 门槛 (两条同时满足才判 `遗漏_应补`)

- **T1 字面性**: 被召回 chunk 的**正文**里存在一句/一段**逐字回答题干主问**(或某个自足的并列问)的陈述。仅"主题相关""同一个域""提到了这个变量""码号相邻"一律不算。
- **T2 权威性**: 该 chunk 是**一手陈述**(CDISC 原文段落 / 域规格 CDISC Notes / 域 assumptions 条目 / 码表本体), 不是**派生索引或导航桩**对同一事实的转述。

从 T1 派生的两条细则 (用于多问题干):

- **片段不算答案源**: 题干有明确主问时, 只答从属子问的 chunk 不补。例: q122 的 `DM/spec.md#DTHFL` 逐字答了"若受试者报告死亡 DM 要做什么", 但主问是"电话随访采集的生存状态与用药进哪些域", 未答 → 不补。
- **并列问算答案源**: 题干是两个自足并列问时, 完整答其中一问的 chunk 补。例: q25 "MHTERM 的角色是什么" + "MH 采集有哪些 assumption", `MH/spec.md#MHTERM` 完整答前者 → 补。

### 1.2 为什么必须有 T2 —— 本 KB 里有三层"看起来像答案"的东西

| 层 | 形态 | 可否作 gold |
|----|------|------------|
| 一手 | `chapters/*.md` 段落、`domains/*/spec.md` 的 CDISC Notes、`domains/*/assumptions.md` 条目、`model/*.md` 章节、`terminology/core/*.md` 码表本体 | **可** |
| 切块时注入的交叉引用 | `terminology/core/*.md` chunk 抬头的 `Used by variable(s): …` (由 `scripts/chunkers/terminology.py:260` 注入, **不在文件正文里**) | **可** —— 它与码表本体同处一个 chunk, chunk 整体能独立作答; 判定依据是 chunk 正文, 故按 chunk 算 |
| 纯派生索引 | `VARIABLE_INDEX.md` 的 `§二 域变量表` 与 `§三 CT 交叉引用: Cxxxxx` 一行映射 | **不可**(下有唯一例外) |

**唯一例外**: `VARIABLE_INDEX.md#§一 通用变量: X` 在"**某变量出现在哪些域 / 有几个域 / 标签是什么**"这类跨域枚举题上, 是本 KB 里唯一能作答的源, 题集自身也一贯把它当 gold (q07/q66/q77/q103-q107 皆如此)。此类题按 gold 补 (本轮只有 q73 一条)。

### 1.3 按 source 分组的通用理由与例外 (条数为实测, 合计 182)

| source 组 | 条数 | 应补/不补 | 通用理由 | 例外 |
|-----------|------|-----------|---------|------|
| `domains/*/spec.md#<单变量>` | 44 | 2 / 42 | 单个域单个变量的规格条目; 跨域枚举题里它答不了主问 | 该变量本身就是题干主问对象时补: q19 `DS/spec#DSDECOD`、q25 `MH/spec#MHTERM` |
| `terminology/core/*.md#<码表小节>` | 21 | 14 / 7 | chunk 抬头 `Used by variable(s)` + 码表本体 (名称/code/可扩展性/全部提交值), 一手且自足 | **码号或变量对不上就不补**: q22/q44 拿到单位表 C66770 (题干要 C66741)、q110 拿到 C78733 (题干要 C78734)、q71 拿到 C66797 与 C96777 (题干要 C78735)、q26 的 `eg_part2` 是 EGMETHOD 的表、q93 的 `EC/spec#ECDOSFRM` 变量对象不同 |
| `其余` (`domains/*/assumptions.md`, `model/02,03,06`) | 22 | 5 / 17 | 逐条按题干判 | 补 q10 `RS/assumptions#item_4`、q76 `model/06#6.6`、q91 `DS/assumptions#item_3`、q115 `SUPPQUAL/assumptions#overview`、q126 `model/03#Subject Elements (SE)` |
| `chapters/ch04_general_assumptions.md` | 15 | 3 / 12 | 多为过路提及或话题不对口 | 补 q38 §4.1.6、q82 §4.2.2、q117 §4.5.4 |
| `VARIABLE_INDEX.md#§一 通用变量: X` | 15 | 1 / 14 | 一行"标签+角色+出现在 N 个域"; 问机制/用法/派生依据一律答不了 | 仅跨域枚举题补: q73 RDOMAIN |
| `VARIABLE_INDEX.md#§三 CT 交叉引用` | 12 | 0 / 12 | 只有 `Cxxxxx — referenced by N variable(s): …` 一句, 无码表名/可扩展性/取值/Core | 无 |
| `model/01_concepts_and_terms.md#2.1` | 11 | 0 / 11 | 讲观测/域/五大变量角色/域码前缀; 11 次命中没有一次正面回答题干 (EPOCH、TAETORD、C78734 等词根本不在正文) | 无 |
| `domains/*/spec.md#Related Domains` | 11 | 0 / 11 | KB 生成的一行导航桩(`- **Trial Design:** [TE](../TE/) — arms use elements`), 是指针不是论述 | 无 |
| `domains/*/spec.md#Controlled Terminology` | 9 | 0 / 9 | 码表链接清单, 不含被问的规则/取值/机制 | 无 |
| `VARIABLE_INDEX.md#§二 域变量表` | 6 | 0 / 6 | `domains/XX/spec.md` 的冗余摘要, 且丢掉了 CDISC Notes (长度限制/填写规则); 命中多因变量名字面匹配 | 无 |
| `domains/*/examples.md` | 5 | 0 / 5 | 示例数据只演示单侧或旁支, 不陈述规则 | 无 |
| `chapters/ch08_relationships.md` | 4 | 2 / 2 | 按题判 | 补 q115 §8.4.1、q39 §8.6.3 |
| `chapters/ch01_introduction.md#whole_file` | 4 | 0 / 4 | 全章是文档目的/章节组织/版本变更 | 最贴边的 ch01:88 Core 图例行与 ch01:55 AP 文档行都是表格单元格, 非论述 (见 §5) |
| `terminology/core/*.md#<整文件 chunk>` | 3 | 0 / 3 | **已核** `lb_part2.md`/`microbiology_part2.md`/`general_part5.md` 三个文件的 chunk **没有** `Used by variable(s)` 行 (`grep -n "Used by variable" …` 无输出), 正文无法把码表连到题干变量, 也不枚举引用变量 | 无 |

复跑命令 (取 chunk 正文 / 核对 used-by 行):

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
python3 -c "import chromadb;c=chromadb.PersistentClient(path='data/chroma').get_collection('sdtm_kb_v1');\
a=c.get(include=['documents','metadatas']);\
print([d for d,m in zip(a['documents'],a['metadatas']) if m['section']=='Sex'][0][:200])"
grep -n "Used by variable" ../knowledge_base/terminology/core/{lb_part2,microbiology_part2,general_part5}.md   # 无输出 = 无该行
grep -n "Used by variable" scripts/chunkers/terminology.py                                                     # :260 注入点
```

### 1.4 本轮判定**没有**使用的输入 (口径声明)

扫描器作者提示了两条, 均已规避 —— 记录在此以便复核:

1. **`sim` 字段混量纲, 本轮判定完全未使用。** dense 路径存 `1.0 - distance`, BM25 路径直接塞 BM25 原始分 (`server/rag.py` docstring: "it is NOT a cosine; only used for ranking signal"), 清单里 4 条 `sim > 1.0` 即由此而来。逐条判定表**只保留 rank 列, 已删掉 sim 列**; 全文无一处理由依赖相似度高低 (`grep -n "sim\|相似度\|置信度" gold_gap_verdicts.md` 无输出)。判定唯一依据是 chunk 正文本身。
2. **清单来自单次检索取样, 但判定对象不受影响。** embedding 重复调用向量不逐位相同, 两次对照有 29-30/182 条 `sim` 漂移 (最大 |Δ|=0.0017); 条目身份 (题号/rank/source/section) 在 top-3 上稳定, 而本轮判的正是身份对应的那段正文, 故结论与该漂移无关。**推论**: 本文件的结论只对"这 182 条被召回过的条目"成立, 不能反过来当作"其他 chunk 不该进 gold"的证据 —— 没被这次 top-3 召回的正确答案源, 本轮扫不到, 也就没判。

---

---

## 2. 逐条判定表 (182 条, 按 scan 顺序)

`遗漏_应补` 条目的支撑正文行号与摘录集中在 §4, 表内只给一句理由。

| # | 题号 | 类别 | source | section | rank | verdict | 理由 |
|---|------|------|--------|---------|------|---------|------|
| 1 | q03 | single_domain | `domains/FA/examples.md` | `Example 6` | 2 | **相关但非权威_不补** | 是 FA 域的示例(按访视记录 AE 严重度), 只是恰好以 AE 为对象; 正文不含 AE 数据采集与编码的任何 assumption 条文。 |
| 2 | q21 | single_domain | `terminology/core/lb_part2.md` | `lb_part2` | 2 | **相关但非权威_不补** | 被召回的是整文件 chunk, 抬头只有 "# Laboratory Codelists (Part 2)" 与 "## Laboratory Test Code (C65047)"; 已核该文件无 "Used by variable(s)" 行, 故正文未把码表连到 LBTESTCD, 也无角色/命名长度约束。留观点见 §5。 |
| 3 | q21 | single_domain | `VARIABLE_INDEX.md` | `§三 CT 交叉引用: C65047` | 3 | **相关但非权威_不补** | 派生索引一行映射, 无码表内容与命名约束。 |
| 4 | q22 | single_domain | `terminology/core/vs.md` | `Units for Vital Signs Results` | 2 | **不相关_不补** | 召回的是单位码表 C66770 (VSORRESU/VSSTRESU), 不是题干要的 VSTESTCD 码表 C66741 —— 码表张冠李戴。 |
| 5 | q25 | single_domain | `domains/MH/spec.md` | `MHTERM` | 1 | **遗漏_应补** | 正文给出 MHTERM 的 Role=Topic / Core=Req / 定义 —— 完整回答 "MHTERM 的角色是什么" 这一半; 现 gold 只收了 assumptions 那一半。 |
| 6 | q25 | single_domain | `domains/MH/spec.md` | `Controlled Terminology` | 2 | **相关但非权威_不补** | MH 的码表链接清单, 既不给 MHTERM 角色也不含采集 assumption。 |
| 7 | q25 | single_domain | `domains/MH/spec.md` | `MHOCCUR` | 3 | **相关但非权威_不补** | MHOCCUR 的定义, 与题干两问(MHTERM 角色 / MH assumptions)都不对口。 |
| 8 | q26 | single_domain | `terminology/core/eg_part3.md` | `Holter ECG Test Code` | 2 | **遗漏_应补** | chunk 抬头 "Used by variable(s): EG.EGTESTCD" + "Holter ECG Test Code (C120523)"; 已核 domains/EG/spec.md:90 EGTESTCD 的 Controlled Terms = C71153; C120523, 故 C120523 确是题干所问 "codelist codes"(复数) 之一。 |
| 9 | q26 | single_domain | `terminology/core/eg_part2.md` | `ECG Test Method` | 3 | **不相关_不补** | 抬头写明 "Used by variable(s): EG.EGMETHOD", 是 EGMETHOD 的方法码表 C71151, 不是 EGTESTCD 的码表。 |
| 10 | q07 | cross_domain | `chapters/ch04_general_assumptions.md` | `4.1.3 Additional Timing Variables` | 2 | **相关但非权威_不补** | 4.1.3.1 讲 EPOCH 的赋值依据(Findings 用 --DTC、I/E 用 --STDTC)与置空规则, 既不枚举使用 EPOCH 的域, 也不给出 EPOCH 的用途定义。 |
| 11 | q07 | cross_domain | `model/01_concepts_and_terms.md` | `2.1 Model Concepts and Terms — Variables` | 3 | **不相关_不补** | 该 chunk 通篇未出现 EPOCH; 命中源于"变量/角色"泛化词面。 |
| 12 | q08 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: USUBJID` | 1 | **相关但非权威_不补** | 只给标签/角色/出现在 55 个域, 不解释 USUBJID 如何充当跨域连接键(题干问机制)。 |
| 13 | q08 | cross_domain | `domains/SUPPQUAL/spec.md` | `USUBJID` | 2 | **相关但非权威_不补** | 只是 SUPPQUAL 内 USUBJID 的定义("This is the value of USUBJID in the parent record(s)"), 是单域条目, 不构成跨域连接键的答案源。 |
| 14 | q08 | cross_domain | `chapters/ch04_general_assumptions.md` | `4.5.9 Baseline Values` | 3 | **不相关_不补** | 讲 --LOBXFL/--BLFL/ABLFL 基线标志, 与 USUBJID 无关。 |
| 15 | q09 | cross_domain | `domains/CM/spec.md` | `Related Domains` | 2 | **相关但非权威_不补** | KB 自动生成的导航桩(一行指针 "AE — adverse events treated by concomitant medication"), 未提 RELREC 机制。 |
| 16 | q09 | cross_domain | `domains/AE/spec.md` | `AECONTRT` | 3 | **相关但非权威_不补** | 只是"是否因该事件给了其他治疗"的 Y/N 变量定义, 不涉及 AE↔CM 的 RELREC 连接方式。 |
| 17 | q10 | cross_domain | `domains/RS/spec.md` | `Controlled Terminology` | 2 | **相关但非权威_不补** | 只是 RS 的码表清单, 不含 TR↔RS 的连接机制或标识变量说明。 |
| 18 | q10 | cross_domain | `domains/RS/assumptions.md` | `item_4` | 3 | **遗漏_应补** | 正文点名 RSLNKGRP / RSLNKID 是 RS 侧连回 TR 的标识变量并说明须在 RELREC 建关系 —— 正是题干问的 "每个链接方向用哪些标识变量" 的 RS→TR 方向。 |
| 19 | q28 | cross_domain | `VARIABLE_INDEX.md` | `FA — Findings About Events or Interventions (Findings About)` | 1 | **相关但非权威_不补** | 派生索引的 FA 变量表, 只给 FAOBJ 的标签/角色, 不说明它如何把 FA 记录挂到 AE/CM 父域(题干主问)。 |
| 20 | q28 | cross_domain | `domains/AE/spec.md` | `Related Domains` | 3 | **相关但非权威_不补** | 导航桩一行 "Findings About: FA — prespecified AE findings (AEPRESP)", 无 FAOBJ 机制。 |
| 21 | q29 | cross_domain | `domains/TA/spec.md` | `Related Domains` | 1 | **相关但非权威_不补** | 导航桩("TE — arms use elements"), 一行指针不是"四个试验设计域如何协同定义研究"的答案源, 且完全未涉及 TI。 |
| 22 | q29 | cross_domain | `domains/TE/spec.md` | `Related Domains` | 2 | **相关但非权威_不补** | 同上, 导航桩一行 "TA — elements compose arms"。 |
| 23 | q29 | cross_domain | `domains/TV/spec.md` | `Related Domains` | 3 | **相关但非权威_不补** | 同上, 导航桩一行 "TA — visits reference arms"。 |
| 24 | q30 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: RDOMAIN` | 1 | **相关但非权威_不补** | 本题问的是 CO 域引用其他域记录的机制; 索引行只给 RDOMAIN 标签与所在三域, 无机制说明。 |
| 25 | q30 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: IDVAR` | 2 | **相关但非权威_不补** | 同上, IDVAR 索引行只有标签与所在三域。 |
| 26 | q31 | cross_domain | `domains/EC/spec.md` | `Related Domains` | 1 | **相关但非权威_不补** | 导航桩一行 "EX — exposure as collected vs exposure", 不解释用途差异与选用时机。 |
| 27 | q31 | cross_domain | `domains/EX/spec.md` | `Related Domains` | 2 | **相关但非权威_不补** | 同上, 反向导航桩。 |
| 28 | q31 | cross_domain | `domains/EX/assumptions.md` | `item_5` | 3 | **相关但非权威_不补** | 只有一句 "Collected exposure data points are to be represented in the EC domain", 未说明 EX 的用途, 不足以构成 EC/EX 用途差异的答案源。留观点见 §5。 |
| 29 | q32 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: VISIT` | 1 | **相关但非权威_不补** | 索引行只枚举 VISIT 所在 36 个域, 不讲跨域一致用法, 也不涉及 SV 的作用(题干两问)。 |
| 30 | q32 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: VISITNUM` | 2 | **相关但非权威_不补** | 同上。 |
| 31 | q33 | cross_domain | `domains/RELREC/spec.md` | `RELID` | 2 | **相关但非权威_不补** | 只定义 RELID, 既不讲 RELSPEC, 也不讲数据集级关系。 |
| 32 | q33 | cross_domain | `domains/RELREC/assumptions.md` | `overview` | 3 | **相关但非权威_不补** | 逐字讲 RELREC(含 dataset-to-dataset), 但题干主问是 RELSPEC 是什么、如何在研究级定义关系; 该 chunk 全篇未提 RELSPEC。 |
| 33 | q34 | cross_domain | `terminology/core/general_part4.md` | `No Yes Response` | 2 | **遗漏_应补** | chunk 抬头逐条列出引用 C66742 的全部 domain.variable (AE.AESER … VS.VSLOBXFL) —— 同时直答 "哪些域共用" 与 "这些域里通常哪个变量用它"。 |
| 34 | q34 | cross_domain | `chapters/ch04_general_assumptions.md` | `4.3.3 Controlled Terminology Values` | 3 | **相关但非权威_不补** | 讲 Define-XML 里如何登记 CT 取值集合, 不枚举共用 C66742 的域与变量。 |
| 35 | q11 | concept | `model/01_concepts_and_terms.md` | `2.1 Model Concepts and Terms — Variables` | 1 | **相关但非权威_不补** | 正文只说"3 'general observation' classes"而不点名三者; 概念图节点虽出现 Events/Interventions/Findings, 属图元不属正文陈述。 |
| 36 | q11 | concept | `chapters/ch04_general_assumptions.md` | `4.1.4 Order of the Variables` | 3 | **相关但非权威_不补** | 讲变量排序, 三个类名仅以被引小节标题形式出现(3.1.1/3.1.2/3.1.3), 属引用而非回答。 |
| 37 | q12 | concept | `VARIABLE_INDEX.md` | `SR — Skin Response (Findings About)` | 2 | **不相关_不补** | SR 变量表里有 Core 列取值 Req/Exp/Perm, 但通篇不定义这三者含义; 命中源于列名字面。 |
| 38 | q12 | concept | `domains/SUPPQUAL/spec.md` | `Controlled Terminology` | 3 | **不相关_不补** | 两行码表链接, 与 Core 指派定义无关。 |
| 39 | q13 | concept | `chapters/ch08_relationships.md` | `8.4.1 Supplemental Qualifiers (SUPP--)` | 2 | **相关但非权威_不补** | SUPP-- 规格表的 Role 列出现 Identifier/Topic/Qualifier 取值, 但不定义 Topic/Qualifier/Identifier 三种角色的区别。 |
| 40 | q13 | concept | `VARIABLE_INDEX.md` | `SUPPQUAL — Supplemental Qualifiers for [domain name] (Relationship)` | 3 | **相关但非权威_不补** | 派生索引表, 同上只是 Role 列取值出现, 无角色定义。 |
| 41 | q14 | concept | `chapters/ch04_general_assumptions.md` | `4.1.6 Additional Guidance on Dataset Naming` | 1 | **相关但非权威_不补** | 只覆盖自定义域的域码保留规则(X/Y/Z); 题干主问"如何创建自定义域"的流程在 ch02 §2.6 (已核: ch02_fundamentals.md:128 "Process for creating a custom domain" 六步), 本节属片段。 |
| 42 | q14 | concept | `chapters/ch01_introduction.md` | `whole_file` | 3 | **不相关_不补** | 全章是文档目的/章节组织/版本变更, 无自定义域创建内容。 |
| 43 | q15 | concept | `chapters/ch01_introduction.md` | `whole_file` | 2 | **相关但非权威_不补** | ch01:88 有图例行 "Core \| 'Req'(Required), 'Exp'(Expected), or 'Perm'(Permissible)" 字面列出三类, 但只是规格表列说明, 不给定义, 更不含 Permissible 未采集时的处理规则(题干第二问)。留观点见 §5。 |
| 44 | q35 | concept | `model/01_concepts_and_terms.md` | `2.1 Model Concepts and Terms — Variables` | 3 | **相关但非权威_不补** | 该 chunk 讲变量角色与域码, 不解释 CT 是什么、如何约束取值 (CT 相关表述在同文件 §2.2, 属另一 chunk)。 |
| 45 | q36 | concept | `model/01_concepts_and_terms.md` | `2.1 Model Concepts and Terms — Variables` | 2 | **相关但非权威_不补** | 只有 "Timing variables — describe the timing of an observation" 一行分类, 不含 --DTC/--STDTC/--ENDTC 的构成与跨域结构。 |
| 46 | q37 | concept | `model/01_concepts_and_terms.md` | `2.1 Model Concepts and Terms — Variables` | 1 | **相关但非权威_不补** | 概念图有 "Special Purpose Domains" 节点, 但正文既不定义特殊用途数据集也不点名哪些域属于它。 |
| 47 | q37 | concept | `model/02_observation_classes.md` | `Overview` | 2 | **相关但非权威_不补** | 只说数据集分为 general observation class 与 special-purpose 两类, 不点名特殊用途域清单(题干主问)。 |
| 48 | q38 | concept | `chapters/ch04_general_assumptions.md` | `4.1.6 Additional Guidance on Dataset Naming` | 1 | **遗漏_应补** | 正文给出域码分配的另一条实体规则: 标准域码取自 CT codelist C66734; X/Y/Z 保留给自定义域, 第二位可为任意字母或数字 —— 直答 "两字符域码的规则"。与已补的 4.2.2 互补而非重复。 |
| 49 | q38 | concept | `domains/SV/spec.md` | `DOMAIN` | 2 | **相关但非权威_不补** | 只是 SV 的 DOMAIN 变量定义("Two-character abbreviation for the domain most relevant to the observation"), 不给域码分配规则。 |
| 50 | q38 | concept | `domains/TS/spec.md` | `DOMAIN` | 3 | **相关但非权威_不补** | 同上, 单域 DOMAIN 定义, 无字符/分配规则。 |
| 51 | q39 | concept | `domains/MI/spec.md` | `Model Definition` | 1 | **不相关_不补** | 整段只有一行 KB 交叉链接 "[Findings class definition](../../model/02_observation_classes.md)", 无正文内容。 |
| 52 | q39 | concept | `chapters/ch08_relationships.md` | `8.6.3 Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions` | 2 | **遗漏_应补** | 节首逐字定义 FA "initially created to represent findings about events, but can also be used for findings about interventions", 并给出判定表行区分 "event as a whole"(Events) 与 "multiple time-based findings about an event"(FA)。留观点见 §5。 |
| 53 | q39 | concept | `domains/DA/spec.md` | `Model Definition` | 3 | **不相关_不补** | 同上, 一行链接桩。 |
| 54 | q40 | concept | `model/01_concepts_and_terms.md` | `2.1 Model Concepts and Terms — Variables` | 2 | **相关但非权威_不补** | 不讲 collected vs derived, 也不讲 Origin metadata (Origin 在 ch04 §4.1.8)。 |
| 55 | q40 | concept | `chapters/ch01_introduction.md` | `whole_file` | 3 | **相关但非权威_不补** | ch01:92-94 "Derived Records and the use of --DRVFL" 只说 "--ORRES should be null 尚未被明文要求, 待未来版本澄清", 是版本待办说明, 不定义 collected/derived 差异, 也不讲 origin 如何标注。 |
| 56 | q41 | concept | `model/01_concepts_and_terms.md` | `2.1 Model Concepts and Terms — Variables` | 1 | **相关但非权威_不补** | 概念图有 Trial Design Model 节点, 正文不列 TDM 数据集也不讲它们承载什么研究级信息。 |
| 57 | q41 | concept | `chapters/ch04_general_assumptions.md` | `4.1.1 Review Study Data Tabulation Model and Implementation Guide` | 2 | **相关但非权威_不补** | 只在一句框架罗列中提到 "trial design model datasets", 属过路提及, 不回答"有哪些"与"捕获什么"。 |
| 58 | q16 | mixed | `VARIABLE_INDEX.md` | `§三 CT 交叉引用: C66769` | 2 | **相关但非权威_不补** | 派生索引的一行映射 (C66769 ↔ AE.AESEV), 不含码表名、可扩展性、取值; 权威源 terminology/core/ae.md 已在 gold。 |
| 59 | q16 | mixed | `domains/DM/examples.md` | `Example 7` | 3 | **不相关_不补** | DM 的 RACE 采集示例, 与 AESEV 取值/码表无关。 |
| 60 | q17 | mixed | `model/01_concepts_and_terms.md` | `2.1 Model Concepts and Terms — Variables` | 2 | **相关但非权威_不补** | 只把 Timing 列为五大角色之一("e.g., start date, end date"), 不讲 --DTC/--STDTC 后缀约定或 ISO 8601 格式。 |
| 61 | q19 | mixed | `domains/DS/spec.md` | `DSDECOD` | 1 | **遗漏_应补** | CDISC Notes 逐字给出 "Codelist 'NCOMPLT' is used for disposition events" 并列出 C66727 —— 直答第一问 (DSCAT=DISPOSITION EVENT 时 DSDECOD 用哪个码表)。孪生题 q91 的 gold 恰好含本文件, 判据不一致。 |
| 62 | q43 | mixed | `terminology/core/dm.md` | `Sex` | 2 | **遗漏_应补** | chunk 抬头 "Used by variable(s): DM.SEX" + "## Sex (C66731)" —— 逐字给出题干要的 codelist 名与 code。同形题 s01 的 gold 已含本文件, 判据不一致。 |
| 63 | q43 | mixed | `VARIABLE_INDEX.md` | `§三 CT 交叉引用: C66731` | 3 | **相关但非权威_不补** | 派生索引一行映射, 无码表名/取值/Core 指派; 权威答案源是 terminology/core/dm.md#Sex(本表已判应补)。 |
| 64 | q44 | mixed | `terminology/core/vs.md` | `Units for Vital Signs Results` | 2 | **不相关_不补** | 同 q22: 召回的是单位码表 C66770, 题干要的是 VSTESTCD 的 C66741。 |
| 65 | q45 | mixed | `terminology/core/dm.md` | `Race` | 2 | **遗漏_应补** | chunk 抬头 "Used by variable(s): DM.RACE" + "## Race (C74457)" + 全部提交值 —— 直答 "RACE 用哪个码表"。同形题 q92(ETHNIC) 的 gold 已含本文件, 判据不一致。 |
| 66 | q45 | mixed | `domains/DM/assumptions.md` | `item_6` | 3 | **相关但非权威_不补** | 讲多选种族如何用 SUPPDM 表示, 不回答 RACE 用哪个码表与 Core 指派。 |
| 67 | q46 | mixed | `terminology/core/ae.md` | `Outcome of Event` | 2 | **遗漏_应补** | chunk 抬头 "Used by variable(s): AE.AEOUT" + "## Outcome of Event (C66768)" + 六个提交值 —— 直答 AEOUT 是什么、用哪个 codelist code。同形题 q16 的 gold 已含本文件。 |
| 68 | q47 | mixed | `VARIABLE_INDEX.md` | `QS — Questionnaires (Findings)` | 1 | **相关但非权威_不补** | 派生索引表给出 QSCAT(Grouping Qualifier, C100129)/QSTESTCD(Topic) 的元数据行, 但不说明 QS 如何借 QSCAT 承载量表特异性(题干主问)。留观点见 §5。 |
| 69 | q47 | mixed | `chapters/ch04_general_assumptions.md` | `4.1.7 Splitting Domains` | 3 | **相关但非权威_不补** | 讲按 --CAT 拆分数据集与命名(QS36), 不讲 QSCAT 如何组织量表 / QSTESTCD 的题目级作用。 |
| 70 | q48 | mixed | `terminology/core/findings_about.md` | `Findings About Test Code` | 2 | **遗漏_应补** | chunk 抬头 "Used by variable(s): FA.FATESTCD" + "## Findings About Test Code (C101832)" + 大量 test code 示例 —— 题干两问(码表 code + 示例 test codes)全部逐字命中。同形题 q96 的 gold 已含本文件。 |
| 71 | q48 | mixed | `VARIABLE_INDEX.md` | `§三 CT 交叉引用: C101832` | 3 | **相关但非权威_不补** | 派生索引一行映射, 不含示例 test code(题干第二问); 权威源 findings_about.md 已判应补。 |
| 72 | s01 | single_domain | `VARIABLE_INDEX.md` | `§三 CT 交叉引用: C66731` | 3 | **相关但非权威_不补** | 派生索引一行映射, 不含四个提交值; 权威源(terminology/core/dm.md + DM/spec)均已在 gold。 |
| 73 | s03 | cross_domain | `domains/DM/assumptions.md` | `item_10` | 3 | **相关但非权威_不补** | item_10b 说 RFXSTDTC/RFXENDTC 代表首末次给药, 但未点名 EX 侧变量 EXSTDTC/EXENDTC 及回退变量 —— 题干问的正是"等于 EX 的哪个变量"。 |
| 74 | s05 | single_domain | `VARIABLE_INDEX.md` | `§三 CT 交叉引用: C66741` | 3 | **相关但非权威_不补** | 派生索引一行映射, 不含码表名、可扩展性、示例 TESTCD(题干三问); 权威源已在 gold。 |
| 75 | q58 | single_domain | `terminology/core/trial_design.md` | `Dictionary Name` | 2 | **不相关_不补** | 抬头写明 "Used by variable(s): TS.TSVCDREF", 是 C66788 字典名码表, 不是 TSPARMCD 的 C66738。 |
| 76 | q58 | single_domain | `VARIABLE_INDEX.md` | `TS — Trial Summary (Trial Design)` | 3 | **相关但非权威_不补** | 派生索引表虽含 TSPARMCD…C66738 一行, 但无长度上限(8 字符)且属 domains/TS/spec.md 的冗余摘要。留观点见 §5。 |
| 77 | q59 | single_domain | `terminology/core/other_part4.md` | `SDTM Death Diagnosis and Details Test Code` | 2 | **遗漏_应补** | chunk 抬头 "Used by variable(s): DD.DDTESTCD" + "(C116108)" + PRCDTH/SECDTH 等取值 —— 直答 DDTESTCD 是什么、码表 code 是什么。 |
| 78 | q59 | single_domain | `VARIABLE_INDEX.md` | `§三 CT 交叉引用: C116108` | 3 | **相关但非权威_不补** | 派生索引一行映射, 无码表内容; 权威源 other_part4.md 已判应补。 |
| 79 | q61 | single_domain | `terminology/core/microbiology_part2.md` | `microbiology_part2` | 2 | **相关但非权威_不补** | 整文件 chunk, 已核该文件无 "Used by variable(s)" 行, 正文未把 "Microbiology Test Code (C120527)" 连到 MBTESTCD, 也不含观察类。留观点见 §5。 |
| 80 | q61 | single_domain | `domains/MB/assumptions.md` | `item_1` | 3 | **相关但非权威_不补** | 讲 MBTEST/MBTSTDTL 的填法约定, 不给 MBTESTCD 的码表 code, 也不说 MB 属哪个观察类。 |
| 81 | q62 | single_domain | `terminology/core/other_part5.md` | `Subject Status Test Code` | 2 | **遗漏_应补** | chunk 抬头 "Used by variable(s): SS.SSTESTCD" + "(C124305)" + SURVSTAT/FUAVSTAT —— 直答 SSTESTCD 用哪个 CT。 |
| 82 | q62 | single_domain | `VARIABLE_INDEX.md` | `§三 CT 交叉引用: C124305` | 3 | **相关但非权威_不补** | 派生索引一行映射; 权威源 other_part5.md 已判应补。 |
| 83 | q66 | cross_domain | `domains/EX/assumptions.md` | `item_4` | 2 | **相关但非权威_不补** | 只说 EX 在特定条件下"可以加上 VISITNUM", 不枚举含 VISITNUM 的域(题干主问)。 |
| 84 | q66 | cross_domain | `chapters/ch04_general_assumptions.md` | `4.4.5 Clinical Encounters and Visits` | 3 | **相关但非权威_不补** | 讲 VISIT/VISITNUM/VISITDY 的填写规则, 不枚举哪些域含 VISITNUM。 |
| 85 | q67 | cross_domain | `domains/AE/spec.md` | `AESEV` | 2 | **不相关_不补** | AESEV 的码表是 C66769 而非题干的 C66742, 且 AESEV 不是 seriousness 变量 —— 命中属噪声。 |
| 86 | q67 | cross_domain | `terminology/core/general_part4.md` | `No Yes Response` | 3 | **遗漏_应补** | chunk 抬头把引用 C66742 的变量逐个列全, 其中 AE.AESER/AESDTH/AESHOSP/AESLIFE/AESMIE 正是题干要的 "AE seriousness 变量示例"; 变量条数也可由该表直接数出。 |
| 87 | q68 | cross_domain | `terminology/core/general_part4.md` | `Not Done` | 2 | **遗漏_应补** | chunk 抬头列出全部 --STAT 变量 (AG.AGSTAT … VS.VSSTAT) 直答 "哪些域用 C66789", 正文 "NOT DONE — Indicates a task, process or examination that has either not been initiated or completed" 直答 "--STAT 表示什么"。 |
| 88 | q68 | cross_domain | `domains/SS/spec.md` | `SSSTAT` | 3 | **相关但非权威_不补** | 单个域的 --STAT 变量定义, 不枚举"哪些域用 C66789"(题干主问)。 |
| 89 | q69 | cross_domain | `terminology/core/general_part5.md` | `general_part5` | 2 | **相关但非权威_不补** | 整文件 chunk, 已核无 "Used by variable(s)" 行, 正文只有 Unit(C71620) 的取值表, 不列引用它的变量(题干主问)。 |
| 90 | q69 | cross_domain | `domains/CM/spec.md` | `CMDOSU` | 3 | **相关但非权威_不补** | 只给 CMDOSU 一个变量的码表归属, 不构成"哪些变量共用 C71620"的枚举答案源。 |
| 91 | q71 | cross_domain | `terminology/core/general_part2.md` | `Category of Inclusion/Exclusion` | 2 | **不相关_不补** | 是 C66797 入排类别码表(IE.IECAT/TI.IECAT), 与题干的 EVAL C78735 无关。 |
| 92 | q71 | cross_domain | `domains/CO/spec.md` | `COEVALID` | 3 | **不相关_不补** | COEVALID 的码表是 C96777(Medical Evaluator Identifier), 不是 C78735。 |
| 93 | q72 | cross_domain | `domains/PC/spec.md` | `Related Domains` | 1 | **相关但非权威_不补** | 导航桩一行 "PP — pharmacokinetic concentrations → parameters", 不解释为何分成两个域。 |
| 94 | q72 | cross_domain | `domains/PP/spec.md` | `Related Domains` | 2 | **相关但非权威_不补** | 同上, 反向导航桩。 |
| 95 | q72 | cross_domain | `domains/PC/assumptions.md` | `overview` | 3 | **相关但非权威_不补** | 该 chunk 只有小节标题与一句"本节涵盖 PC 与 PP", 正文空转, 无关系说明。 |
| 96 | q73 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: RDOMAIN` | 1 | **遗漏_应补** | chunk 正文 "RDOMAIN (Related Domain Abbreviation) … Appears in 3 SDTM domains: CO, RELREC, SUPPQUAL" 逐字回答 "哪些特殊用途/关系域带 RDOMAIN" + 变量含义。同形跨域枚举题 (q07/q66/q77/q103-q107) 的 gold 都是 VARIABLE_INDEX §一, 唯独本题没写。 |
| 97 | q73 | cross_domain | `domains/RELREC/spec.md` | `RDOMAIN` | 3 | **相关但非权威_不补** | 给出 RDOMAIN 在 RELREC 内的定义, 但不回答"哪些特殊用途/关系域带 RDOMAIN"(题干主问)。 |
| 98 | q74 | cross_domain | `domains/AE/spec.md` | `Related Domains` | 1 | **相关但非权威_不补** | 导航桩, 不讲 SUPP-- 命名规则与回连变量。 |
| 99 | q74 | cross_domain | `domains/CM/spec.md` | `DOMAIN` | 2 | **不相关_不补** | CM 的 DOMAIN 变量定义, 与 SUPP-- 命名/回连无关。 |
| 100 | q75 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: USUBJID` | 3 | **相关但非权威_不补** | 题干问的是 USUBJID 之外还有哪些标识变量能标记记录来源; 该行只讲 USUBJID 自身。 |
| 101 | q76 | cross_domain | `VARIABLE_INDEX.md` | `RELSUB — Related Subjects (Relationship)` | 1 | **相关但非权威_不补** | 派生索引表, 且 RELSUB 是受试者间关系域, 不是 AP 域回连机制(APRELSUB)。 |
| 102 | q76 | cross_domain | `model/06_relationship_datasets.md` | `6.6 Associated Persons Related Subjects (APRELSUB)` | 2 | **遗漏_应补** | 正文 "Links associated persons to subjects" + 变量表给出 RSUBJID(Related Subject or Pool Identifier, Identifier) 与 SREL(Subject, Device, or Study Relationship, Record Qualifier) —— 直答 AP 如何连回受试者及这两个变量各自的角色。 |
| 103 | q77 | cross_domain | `chapters/ch04_general_assumptions.md` | `4.1.3 Additional Timing Variables` | 2 | **相关但非权威_不补** | 讲 EPOCH 赋值依据与置空, 不列使用 EPOCH 的域。 |
| 104 | q77 | cross_domain | `domains/TA/assumptions.md` | `item_12` | 3 | **相关但非权威_不补** | 一句"EPOCH may be used as a timing variable in other datasets, such as EX and DS"属 TA 内的顺带举例(仅 2 域), 不是"EPOCH 用在哪些域"的答案源。留观点见 §5。 |
| 105 | q81 | concept | `domains/TM/spec.md` | `DOMAIN` | 2 | **相关但非权威_不补** | 只有 "Two-character abbreviation for the domain, which must be TM", 不给首/次字符允许集合。 |
| 106 | q82 | concept | `chapters/ch04_general_assumptions.md` | `4.2.2 Two-character Domain Identifier` | 2 | **遗漏_应补** | 正文逐字写出 "Required Identifiers (STUDYID, DOMAIN, USUBJID)" 并解释 "Required identifiers are not prefixed because they are usually used as keys when merging/joining" —— 题干两问(哪些标识变量必需 / 其中受试者级标识是哪个)全部命中。 |
| 107 | q83 | concept | `VARIABLE_INDEX.md` | `§一 通用变量: RDOMAIN` | 1 | **相关但非权威_不补** | 题干问 RELREC 是什么/怎么用/RDOMAIN 在 RELREC 里做什么; 索引行只给标签与所在三域, 无 RELREC 用法。 |
| 108 | q83 | concept | `domains/RELREC/spec.md` | `Controlled Terminology` | 2 | **不相关_不补** | 两行码表链接(C66734/C78737), 不解释 RELREC 用法。 |
| 109 | q84 | concept | `chapters/ch04_general_assumptions.md` | `4.5.7 Presence or Absence of Prespecified Interventions and Events` | 3 | **相关但非权威_不补** | 讲 --PRESP/--OCCUR/--STAT 的填法, 不给 intervention 与 event 的定义(题干主问)。 |
| 110 | q85 | concept | `chapters/ch04_general_assumptions.md` | `4.1.6 Additional Guidance on Dataset Naming` | 2 | **相关但非权威_不补** | 讲自定义域 X/Y/Z 码保留, 与 AP 域命名规则无关。 |
| 111 | q85 | concept | `chapters/ch01_introduction.md` | `whole_file` | 3 | **相关但非权威_不补** | ch01:55 表格行 "SDTMIG-AP \| Associated Persons — data about persons who are not study subjects" 是相关文档清单的一格, 不讲 AP 域相对标准域码如何命名。 |
| 112 | q86 | concept | `model/01_concepts_and_terms.md` | `2.1 Model Concepts and Terms — Variables` | 3 | **相关但非权威_不补** | 该 chunk 无 Core 指派内容, 更无 Define-XML 中 Expected 变量未采集时的处理要求。 |
| 113 | q87 | concept | `domains/FA/spec.md` | `Related Domains` | 1 | **相关但非权威_不补** | 导航桩(列出 FA 的源域), 不给 SUPP-- 与 FA 的取舍判据。 |
| 114 | q87 | concept | `domains/FA/spec.md` | `FASCAT` | 2 | **不相关_不补** | FASCAT 变量定义("A further categorization of FACAT"), 与取舍判据无关。 |
| 115 | q87 | concept | `domains/FA/spec.md` | `Controlled Terminology` | 3 | **不相关_不补** | FA 码表清单, 与取舍判据无关。 |
| 116 | q88 | concept | `domains/DM/spec.md` | `ARMCD` | 1 | **相关但非权威_不补** | 确实逐字给出 ARMCD 限 20 字符且"not subject to the character restrictions that apply to TESTCD", 但只覆盖四个变量之一; 题干要的是 ETCD/TSPARMCD/ARMCD 与 --TESTCD 的对比集合。留观点见 §5。 |
| 117 | q88 | concept | `domains/TA/spec.md` | `ARMCD` | 2 | **相关但非权威_不补** | 同上, 与 DM 的 ARMCD 条目内容重复, 仍只覆盖一个变量。 |
| 118 | q88 | concept | `domains/TS/spec.md` | `TSPARMCD` | 3 | **相关但非权威_不补** | 逐字给出 TSPARMCD 限 8 字符、无特殊字符限制, 但同样只覆盖对比集合中的一项。 |
| 119 | q89 | concept | `domains/SV/assumptions.md` | `item_15` | 3 | **相关但非权威_不补** | item_15e/f 顺带说 --STRF/--ENRF、--STRTPT/--ENRTPT "could be used … although this seems unnecessary", 是 SV 域该不该加时间变量的告诫, 不是 Relative Timing 变量组的定义与取值说明。留观点见 §5。 |
| 120 | q90 | mixed | `VARIABLE_INDEX.md` | `§三 CT 交叉引用: C66729` | 3 | **相关但非权威_不补** | 派生索引一行映射, 不含肠外给药途径取值(题干第二问); 权威源 terminology/core/interventions.md 已在 gold。 |
| 121 | q91 | mixed | `domains/DS/assumptions.md` | `item_3` | 3 | **遗漏_应补** | 正文 "When DSTERM contains verbatim text, DSDECOD will use the extensible Controlled Terminology Codelist NCOMPLT" —— 直答 "disposition events 时 DSDECOD 用哪个码表"。孪生题 q19 的 gold 恰好含本文件, 判据不一致。 |
| 122 | q92 | mixed | `VARIABLE_INDEX.md` | `§三 CT 交叉引用: C66790` | 3 | **相关但非权威_不补** | 派生索引一行映射, 不含 ETHNIC 的允许取值; 权威源(DM/spec + terminology/core/dm.md)均已在 gold。 |
| 123 | q93 | mixed | `domains/EC/spec.md` | `ECDOSFRM` | 3 | **不相关_不补** | 题干问 EX 的 EXDOSFRM; 该条是 EC 的 ECDOSFRM, 变量对象不同(虽同用 C66726), 且无剂型取值。 |
| 124 | q94 | mixed | `domains/LB/examples.md` | `Example 3` | 3 | **相关但非权威_不补** | 示例演示了 LBORRES "-" 标准化为 LBSTRESC "NEGATIVE", 但不点名 LBSTRESC 引用的码表, 不构成题干主问的答案源。 |
| 125 | q96 | mixed | `domains/FA/assumptions.md` | `item_4` | 3 | **相关但非权威_不补** | 讲 FATEST/FATESTCD 取值应与父域变量名一致, 不给码表 code 与示例 test name。 |
| 126 | q98 | mixed | `domains/CM/assumptions.md` | `item_2` | 3 | **相关但非权威_不补** | 以 CMDOSU="MG" 举例说明 CMTRT 不含剂量信息, 不给 CMDOSU 的码表与单位取值。 |
| 127 | q99 | mixed | `VARIABLE_INDEX.md` | `§三 CT 交叉引用: C100129` | 3 | **相关但非权威_不补** | 派生索引一行映射, 无量表简称取值; 权威源 terminology/core/qs_part1.md 已在 gold。 |
| 128 | q101 | mixed | `VARIABLE_INDEX.md` | `§三 CT 交叉引用: C67152` | 3 | **相关但非权威_不补** | 派生索引一行映射, 无 TSPARM 参数名示例; 权威源 trial_design.md 已在 gold。 |
| 129 | q103 | cross_domain | `model/01_concepts_and_terms.md` | `2.1 Model Concepts and Terms — Variables` | 2 | **不相关_不补** | 通篇不含 TAETORD; 命中源于"变量/角色"泛化词面。 |
| 130 | q103 | cross_domain | `model/02_observation_classes.md` | `Overview` | 3 | **不相关_不补** | 同上, 不含 TAETORD 的域数与标签。 |
| 131 | q104 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: VISIT` | 1 | **不相关_不补** | 题干问 VISITDY; 召回的是兄弟变量 VISIT 的索引行, 变量不对。 |
| 132 | q104 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: VISITNUM` | 2 | **不相关_不补** | 同上, 兄弟变量 VISITNUM, 非 VISITDY。 |
| 133 | q105 | cross_domain | `domains/GF/spec.md` | `NHOID` | 2 | **相关但非权威_不补** | 给出 GF 内 NHOID 的标签与定义, 但题干主问是"哪些域含 NHOID"的枚举, 单域条目答不了。 |
| 134 | q105 | cross_domain | `domains/IS/spec.md` | `NHOID` | 3 | **相关但非权威_不补** | 同上, 单域条目。 |
| 135 | q106 | cross_domain | `domains/OE/assumptions.md` | `item_1` | 2 | **相关但非权威_不补** | 讲眼科中 FOCID 取 OD/OS/OU, 不枚举 FOCID 定义在哪些域(题干主问)。 |
| 136 | q106 | cross_domain | `domains/MB/spec.md` | `FOCID` | 3 | **相关但非权威_不补** | 给出 FOCID 的定义(答了第二问), 但单域条目答不了"定义在哪些域"这一主问。 |
| 137 | q107 | cross_domain | `domains/DM/spec.md` | `ARMCD` | 3 | **相关但非权威_不补** | 只给 DM 内 ARMCD 的说明, 不枚举同时含 ARM 与 ARMCD 的数据集(题干主问); 两条 VARIABLE_INDEX gold 已覆盖。 |
| 138 | q108 | cross_domain | `terminology/core/interventions.md` | `Route of Administration Response` | 2 | **遗漏_应补** | chunk 抬头 "Used by variable(s): AG.AGROUTE, CM.CMROUTE, EC.ECROUTE, EX.EXROUTE, PR.PRROUTE, SU.SUROUTE" —— 逐字、完整回答 "哪些 SDTM 变量受 C66729 管辖"。 |
| 139 | q108 | cross_domain | `domains/CM/spec.md` | `CMROUTE` | 3 | **相关但非权威_不补** | 单个变量的码表归属, 不构成"哪些变量受 C66729 管辖"的枚举答案源。 |
| 140 | q109 | cross_domain | `terminology/core/general_part2.md` | `Laterality` | 2 | **遗漏_应补** | chunk 抬头 "Used by variable(s): CV.CVLAT … VS.VSLAT" (17 个) —— 逐字回答 "哪些域变量引用 C99073"。 |
| 141 | q109 | cross_domain | `domains/UR/spec.md` | `URLAT` | 3 | **相关但非权威_不补** | 单个变量的码表归属, 不构成跨域枚举答案源。 |
| 142 | q110 | cross_domain | `terminology/core/general_part4.md` | `Specimen Condition` | 2 | **不相关_不补** | 该码表是 Specimen Condition C78733, 题干要的是 Specimen Type C78734 —— 相邻码号误命中。 |
| 143 | q110 | cross_domain | `model/01_concepts_and_terms.md` | `2.1 Model Concepts and Terms — Variables` | 3 | **不相关_不补** | 通篇不含 C78734 或标本类型变量。 |
| 144 | q111 | cross_domain | `terminology/core/interventions.md` | `Position` | 2 | **遗漏_应补** | chunk 抬头 "Used by variable(s): CV.CVPOS, EG.EGPOS, FT.FTPOS, MK.MKPOS, RE.REPOS, VS.VSPOS" —— 逐字回答 "哪些域含受 C71148 控制的体位变量"。 |
| 145 | q111 | cross_domain | `domains/CV/spec.md` | `CVPOS` | 3 | **相关但非权威_不补** | 单个变量的码表归属, 不构成"哪些域含受 C71148 控制的体位变量"的枚举答案源。 |
| 146 | q112 | cross_domain | `terminology/core/general_part4.md` | `Reference Range Indicator` | 2 | **遗漏_应补** | chunk 抬头 "Used by variable(s): CP.CPNRIND, IS.ISNRIND, LB.LBNRIND, MS.MSNRIND, OE.OENRIND" —— 逐字回答 "哪些域的哪些变量映射到 C78736"。 |
| 147 | q112 | cross_domain | `domains/IS/spec.md` | `ISNRIND` | 3 | **相关但非权威_不补** | 单个变量的码表归属, 不构成跨域枚举答案源。 |
| 148 | q113 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: IDVAR` | 1 | **相关但非权威_不补** | 索引行只给标签与所在三域, 不讲 SUPPDM 里 IDVAR/IDVARVAL 该填什么、为何 DM 与其他域不同。 |
| 149 | q113 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: IDVARVAL` | 2 | **相关但非权威_不补** | 同上。 |
| 150 | q113 | cross_domain | `domains/DM/spec.md` | `INVID` | 3 | **不相关_不补** | 研究者标识变量, 与 SUPPDM 的 IDVAR/IDVARVAL 填法无关。 |
| 151 | q114 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: USUBJID` | 1 | **相关但非权威_不补** | 不讲数据集级 RELREC 中 RELTYPE 的填法与 USUBJID/IDVARVAL 置空规则。 |
| 152 | q114 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: IDVARVAL` | 2 | **相关但非权威_不补** | 同上, 索引行无数据集级关系规则。 |
| 153 | q114 | cross_domain | `domains/RELREC/spec.md` | `RELID` | 3 | **相关但非权威_不补** | 只定义 RELID, 不涉及 RELTYPE 取值、USUBJID/IDVARVAL 置空、--SEQ 能否作连接键(题干三问)。 |
| 154 | q115 | cross_domain | `chapters/ch08_relationships.md` | `8.4.1 Supplemental Qualifiers (SUPP--)` | 1 | **遗漏_应补** | SUPP-- 规格表逐字给出 QORIG("QORIG is used to indicate the origin of this data") 与 QEVAL("Used only for results that are subjective … Should be null for records that contain objectively collected") —— 题干两问全中。 |
| 155 | q115 | cross_domain | `chapters/ch08_relationships.md` | `8.3.1 RELREC Dataset Relationship Example` | 2 | **不相关_不补** | 讲 RELREC 数据集级关系与 RELTYPE, 与 SUPP-- 的 QORIG/QEVAL 无关。 |
| 156 | q115 | cross_domain | `domains/SUPPQUAL/assumptions.md` | `overview` | 3 | **遗漏_应补** | 正文 "the origin (QORIG) of the value …, and the evaluator (QEVAL) to specify the role of the individual who assigned the value" + "For objective data, the value in QEVAL will be null" —— 同样逐字回答两问。 |
| 157 | q117 | cross_domain | `domains/SUPPQUAL/examples.md` | `Example 1` | 1 | **相关但非权威_不补** | 示例只展示单一评估者的 SUPPAE 记录(QEVAL=SPONSOR), 未演示同一 QNAM 两方判定并存的做法(题干主问)。 |
| 158 | q117 | cross_domain | `chapters/ch04_general_assumptions.md` | `4.5.4 Evaluators in the Interventions and Events Observation Classes` | 2 | **遗漏_应补** | 正文给出确切做法: 主评估进标准域、二次评估进 SUPP--, QNAM 末尾追加 "1"(满 8 字符则替换末位), 并用 QEVAL 记录评估者; 附 suppae.xpt 示例 (AESEV1/AEREL1, QEVAL=ADJUDICATION COMMITTEE) —— 正是题干"两方判定都不丢"的答案。 |
| 159 | q117 | cross_domain | `domains/AE/assumptions.md` | `item_7` | 3 | **相关但非权威_不补** | 讲 AE 严重性分类变量与 AEOSOSP 的 SUPPAE 用法, 不涉及主/次评估并存的表示方法。 |
| 160 | q118 | cross_domain | `VARIABLE_INDEX.md` | `§一 通用变量: EPOCH` | 1 | **相关但非权威_不补** | 索引行只列 EPOCH 所在 44 个域, 不讲 Findings vs I/E 各以哪个日期变量为准、无法判定时怎么办(题干两问)。 |
| 161 | q118 | cross_domain | `domains/TA/assumptions.md` | `item_12` | 3 | **相关但非权威_不补** | 只说不同 epoch 的 EPOCH 值必须相异, 不涉及派生依据。 |
| 162 | q119 | cross_domain | `domains/RELREC/spec.md` | `RELID` | 1 | **相关但非权威_不补** | 定义 RELID, 不区分 --LNKID 与 --LNKGRP。 |
| 163 | q119 | cross_domain | `domains/TU/spec.md` | `TULNKID` | 2 | **相关但非权威_不补** | 只给 TU 侧 --LNKID 的实例定义, 不做 --LNKID 与 --LNKGRP 的对比(题干主问)。 |
| 164 | q119 | cross_domain | `domains/TR/spec.md` | `TRLNKID` | 3 | **相关但非权威_不补** | 同上, TR 侧实例定义, 无对比。 |
| 165 | q120 | cross_domain | `chapters/ch04_general_assumptions.md` | `4.2.6 Grouping Variables and Categorization` | 2 | **不相关_不补** | 讲 --CAT/--SCAT/--GRPID 的分组层级, 与 AP 数据集中"人群组"的标识(POOLID/POOLDEF)无关。 |
| 166 | q121 | cross_domain | `domains/DM/spec.md` | `RFICDTC` | 1 | **相关但非权威_不补** | 给出 RFICDTC 定义, 但不覆盖二次知情同意如何取值, 也不说明 RFICDTC 与 RFPENDTC 合起来代表什么期间(题干两问)。 |
| 167 | q121 | cross_domain | `domains/DM/spec.md` | `RFPENDTC` | 2 | **相关但非权威_不补** | 同上, 单变量定义, 不给成对期间语义。 |
| 168 | q121 | cross_domain | `domains/DM/spec.md` | `RFENDTC` | 3 | **不相关_不补** | 是另一组参考期变量, 与 RFICDTC/RFPENDTC 这一对无关。 |
| 169 | q122 | cross_domain | `domains/DM/spec.md` | `DTHDTC` | 1 | **相关但非权威_不补** | 死亡日期变量定义; 题干主问是随访期采集的数据该进哪些域, DM 侧只是从属子问。留观点见 §5。 |
| 170 | q122 | cross_domain | `domains/DM/spec.md` | `DTHFL` | 2 | **相关但非权威_不补** | DTHFL 定义("Should be populated even when the death date is unknown")答的是从属子问, 不答主问"生存状态与合并用药进哪些域"。留观点见 §5。 |
| 171 | q122 | cross_domain | `domains/DM/spec.md` | `RFPENDTC` | 3 | **不相关_不补** | 参与期结束日定义, 与题干两问都不对口。 |
| 172 | q123 | cross_domain | `domains/TU/spec.md` | `Controlled Terminology` | 1 | **不相关_不补** | TU 的码表清单, 不讲 TU/TR 分工与解剖位置不重复存储。 |
| 173 | q123 | cross_domain | `domains/TR/spec.md` | `TRDY` | 2 | **不相关_不补** | 研究日变量定义, 与分工问题无关。 |
| 174 | q124 | cross_domain | `domains/AE/spec.md` | `AESDTH` | 1 | **相关但非权威_不补** | 定义 AE 侧死亡标志, 但不讲死因细节记在哪(DD)、处置事件记在哪(DS)、如何避免重复采集(题干三问)。 |
| 175 | q124 | cross_domain | `domains/DD/spec.md` | `Controlled Terminology` | 2 | **不相关_不补** | DD 的码表清单, 无记录归属规则。 |
| 176 | q124 | cross_domain | `domains/DS/spec.md` | `Controlled Terminology` | 3 | **不相关_不补** | DS 的码表清单, 无记录归属规则。 |
| 177 | q125 | cross_domain | `domains/CE/spec.md` | `CEPRESP` | 1 | **相关但非权威_不补** | CEPRESP 变量定义, 不给 CE 与 AE 的归属判据(题干主问)。 |
| 178 | q125 | cross_domain | `domains/AE/spec.md` | `Controlled Terminology` | 2 | **不相关_不补** | AE 的码表清单, 与 CE/AE 归属判据无关。 |
| 179 | q126 | cross_domain | `domains/DM/assumptions.md` | `item_4` | 2 | **相关但非权威_不补** | 讲 ARM/ACTARM 计划与实际治疗组的填法, 题干问的是 element(TE/SE)层面的计划 vs 实际与脱轨表示, 对象不同。 |
| 180 | q126 | cross_domain | `model/03_special_purpose_domains.md` | `Subject Elements (SE)` | 3 | **遗漏_应补** | 正文 "Describes the actual Elements … experienced by each subject. Planned elements are described in the Trial Design Model. … the SDTM allows for descriptions of an unplanned element (SEUPDES)" + 变量表 SEUPDES "Used only if ETCD has a value of 'UNPLAN'" —— 计划/实际/脱轨表示三问全中。 |
| 181 | q127 | cross_domain | `domains/BE/examples.md` | `Example 2` | 2 | **相关但非权威_不补** | 示例演示 BE 记录采集/离心/运输/分装等处理动作, 只覆盖"处理动作"一侧且属示例数据, 未与 BS(样本特征)对照。 |
| 182 | q127 | cross_domain | `terminology/core/other_part1.md` | `Biospecimen Characteristics Test Name` | 3 | **相关但非权威_不补** | 抬头 "Used by variable(s): BS.BSTEST" + 取值含 Size/Length/Mass, 只覆盖"样本特征"一侧且未点明域分工。留观点见 §5。 |
---

## 3. 汇总

| verdict | 条数 | 占比 | 涉及题数 |
|---------|------|------|---------|
| `遗漏_应补` | **27** | 14.8% | **26** |
| `相关但非权威_不补` | 119 | 65.4% | 79 |
| `不相关_不补` | 36 | 19.8% | 27 |
| 合计 | 182 | 100% | 97 |

`遗漏_应补` 涉及的题号 (26 题):

```
q10  q19  q25  q26  q34  q38  q39  q43  q45  q46  q48  q59  q62
q67  q68  q73  q76  q82  q91  q108 q109 q111 q112 q115 q117 q126
```

按缺口成因分三类:

| 成因 | 条数/题数 | 题号 | 说明 |
|------|------|------|------|
| **A. 码表交叉引用行未收** (q38 的同构缺口) | 14 条 / 14 题 | q26 q34 q43 q45 q46 q48 q59 q62 q67 q68 q108 q109 q111 q112 (q34/q67 共用同一 chunk) | `terminology/core/*.md` 码表 chunk 抬头的 `Used by variable(s)` 逐字回答"哪些变量用码表 C"/"变量 V 用哪个码表", 且**同题集内同形题的 gold 写法自相矛盾** |
| **B. 两问题干只收了一半** | 9 条 / 8 题 | q19 q25 q39 q82 q91 q115(×2) q117 q126 | 题干两个自足并列问, gold 只写了其中一问的源 |
| **C. 判据与题集自身惯例不一致** | 4 条 / 4 题 | q10 q38 q73 q76 | 同形题按惯例该收的源没收 |

---

## 4. `遗漏_应补` 清单 (含支撑正文行号 + 原文摘录 + 建议 gold 写法)

**匹配语义提醒 (给实施方)**: `eval/run_eval.py:75 source_matches` 里 `路径#节$` 是 **section 精确相等**(非正则), 故 `8.4.1 Supplemental Qualifiers (SUPP--)` 这种含括号的节名可以直接写, 无需转义。`expected_sources` 是 **AND**(`check_source_recall` 按 `n_hit/n_groups` 算部分召回), `expected_sources_any` 是 **OR 组**(整组算 1 个 group)。下表"建议形态"一列区分:

- **OR** = 与现有 gold 中的某条互为等价答案源, 应并成 `expected_sources_any` 组, 否则会把题目改严;
- **AND** = 回答的是另一个并列问, 直接追加进 `expected_sources`。

| # | 题号 | 建议 gold 写法 | 建议形态 | 支撑正文 (文件:行) | 原文摘录 |
|---|------|---------------|---------|-------------------|---------|
| 1 | q10 | `domains/RS/assumptions.md#item_4$` | AND (补 RS→TR 方向) | `knowledge_base/domains/RS/assumptions.md:18` | "The RSLNKGRP variable is used to provide a link between the records in a findings domain (e.g., Tumor/Lesion Results, TR …) that contribute to a record in the RS domain. Records should exist in the RELREC dataset to support this relationship. A RELREC relationship could also be defined using RSLNKID …" |
| 2 | q19 | `domains/DS/spec.md#DSDECOD$` | OR (与 `domains/DS/assumptions.md` 等价) | `knowledge_base/domains/DS/spec.md:77-84` | "**Controlled Terms:** C66727; C114118; C150811 … There are separate codelists used for DSDECOD where the choice depends on the value of DSCAT. Codelist \"NCOMPLT\" is used for disposition events …" |
| 3 | q25 | `domains/MH/spec.md#MHTERM$` | AND (答"MHTERM 的角色") | `knowledge_base/domains/MH/spec.md:68-74` | "### MHTERM … **Label:** Reported Term for the Medical History … **Role:** Topic … **Core:** Req … **CDISC Notes:** Verbatim or preprinted CRF term for the medical condition or event." |
| 4 | q26 | `terminology/core/eg_part3.md#Holter ECG Test Code$` | AND (EGTESTCD 的第二个码表) | chunk 抬头 + `knowledge_base/terminology/core/eg_part3.md:245`; 佐证 `knowledge_base/domains/EG/spec.md:90` | chunk: "Used by variable(s): EG.EGTESTCD." / 文件: "## Holter ECG Test Code (C120523)" / EG spec:90: "**Controlled Terms:** C71153; C120523" |
| 5 | q34 | `terminology/core/general_part4.md#No Yes Response$` | OR (与 `VARIABLE_INDEX.md#§三 CT 交叉引用: C66742$` 等价) | chunk 抬头 + `knowledge_base/terminology/core/general_part4.md:5` | chunk: "Used by variable(s): AE.AECONTRT, AE.AEPRESP, AE.AESCAN, … VS.VSLOBXFL." / 文件: "## No Yes Response (C66742)" |
| 6 | q38 | `chapters/ch04_general_assumptions.md#4.1.6 Additional Guidance on Dataset Naming$` | OR (与已补的 §4.2.2 等价) | `knowledge_base/chapters/ch04_general_assumptions.md:55-59` | "(See the SDTM Domain Abbreviation codelist, C66734, in CDISC Controlled Terminology … for standard domain codes.) … domain codes beginning with the letters X, Y, and Z have been reserved for the creation of custom domains. Any letter or number may be used in the second position." |
| 7 | q39 | `chapters/ch08_relationships.md#8.6.3 Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions$` | OR (与 `model/02_observation_classes.md` 等价) | `knowledge_base/chapters/ch08_relationships.md:317, 336` | :317(节内首段) "The Findings About (FA) domain was initially created to represent findings about events, but can also be used for findings about interventions." / :336(判定表行 "If this is data about an event, does it apply to the event as a whole?") "A \"No\" answer suggests that there are multiple time-based findings about an event, and that these data should be treated as Findings About data." |
| 8 | q43 | `terminology/core/dm.md#Sex$` | OR (与 `domains/DM/spec.md` 等价; 对齐 s01 的写法) | chunk 抬头 + `knowledge_base/terminology/core/dm.md:54` | chunk: "Used by variable(s): DM.SEX." / 文件: "## Sex (C66731)" + F/M/U/UNDIFFERENTIATED 四值 |
| 9 | q45 | `terminology/core/dm.md#Race$` | OR (与 `domains/DM/spec.md` 等价; 对齐 q92 的写法) | chunk 抬头 + `knowledge_base/terminology/core/dm.md:39` | chunk: "Used by variable(s): DM.RACE." / 文件: "## Race (C74457)" + 8 个提交值 |
| 10 | q46 | `terminology/core/ae.md#Outcome of Event$` | OR (与 `domains/AE/spec.md` 等价; 对齐 q16 的写法) | chunk 抬头 + `knowledge_base/terminology/core/ae.md:30` | chunk: "Used by variable(s): AE.AEOUT." / 文件: "## Outcome of Event (C66768)" + FATAL/RECOVERED 等 6 值 |
| 11 | q48 | `terminology/core/findings_about.md#Findings About Test Code$` | OR (与 `domains/FA/spec.md` 等价; 对齐 q96 的写法) | chunk 抬头 + `knowledge_base/terminology/core/findings_about.md:5` | chunk: "Used by variable(s): FA.FATESTCD." / 文件: "## Findings About Test Code (C101832)" + ABSCNUM/CUMEXP 等 test code |
| 12 | q59 | `terminology/core/other_part4.md#SDTM Death Diagnosis and Details Test Code$` | OR (与 `domains/DD/spec.md` 等价) | chunk 抬头 + `knowledge_base/terminology/core/other_part4.md:555` | chunk: "Used by variable(s): DD.DDTESTCD." / 文件: "## SDTM Death Diagnosis and Details Test Code (C116108)" + PRCDTH/SECDTH |
| 13 | q62 | `terminology/core/other_part5.md#Subject Status Test Code$` | OR (与 `domains/SS/spec.md` 等价) | chunk 抬头 + `knowledge_base/terminology/core/other_part5.md:123` | chunk: "Used by variable(s): SS.SSTESTCD." / 文件: "## Subject Status Test Code (C124305)" + SURVSTAT/FUAVSTAT |
| 14 | q67 | `terminology/core/general_part4.md#No Yes Response$` | OR (与 `VARIABLE_INDEX.md#§三 CT 交叉引用: C66742$` 等价) | chunk 抬头 + `knowledge_base/terminology/core/general_part4.md:5` | chunk 抬头含 "AE.AESER, AE.AESDTH, AE.AESHOSP, AE.AESLIFE, AE.AESMIE" —— 正是题干要的 AE seriousness 变量示例 |
| 15 | q68 | `terminology/core/general_part4.md#Not Done$` | OR (与 `VARIABLE_INDEX.md#§三 CT 交叉引用: C66789$` 等价) | chunk 抬头 + `knowledge_base/terminology/core/general_part4.md:16` | chunk: "Used by variable(s): AG.AGSTAT, BS.BSSTAT, … VS.VSSTAT." / 文件: "## Not Done (C66789)" + "NOT DONE — Indicates a task, process or examination that has either not been initiated or completed." |
| 16 | q73 | `VARIABLE_INDEX.md#§一 通用变量: RDOMAIN$` | OR (与 `model/06_relationship_datasets.md` 等价; 对齐 q07/q66/q77/q103-q107 的惯例) | chunk 正文; 源表 `knowledge_base/VARIABLE_INDEX.md:37` | chunk: "RDOMAIN (Related Domain Abbreviation) — Record Qualifier* variable, type Char, Core Req*. Appears in 3 SDTM domains: CO, RELREC, SUPPQUAL." / 源表行: `\| RDOMAIN \| 3 \| CO, RELREC, SUPPQUAL \| Related Domain Abbreviation \|` |
| 17 | q76 | `model/06_relationship_datasets.md#6.6 Associated Persons Related Subjects (APRELSUB)$` | AND (答 AP 回连机制 + 两变量角色) | `knowledge_base/model/06_relationship_datasets.md:129-141` | "**Structure:** One record per associated person relationship / Links associated persons to subjects." + 变量表 "RSUBJID \| Related Subject or Pool Identifier \| Char \| Identifier" 与 "SREL \| Subject, Device, or Study Relationship \| Char \| Record Qualifier" |
| 18 | q82 | `chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$` | OR (与 `model/02_observation_classes.md` 等价) | `knowledge_base/chapters/ch04_general_assumptions.md:263, 268`; 节头 `:255` | "- Required Identifiers (STUDYID, DOMAIN, USUBJID)" … "Required identifiers are not prefixed because they are usually used as keys when merging/joining observations." |
| 19 | q91 | `domains/DS/assumptions.md#item_3$` | OR (与 `domains/DS/spec.md` 等价; 与 q19 对称) | `knowledge_base/domains/DS/assumptions.md:16-21` | "When DSTERM contains verbatim text, DSDECOD will use the extensible Controlled Terminology Codelist NCOMPLT. For example, DSTERM = \"Subject moved\" might be coded to DSDECOD = \"LOST TO FOLLOW-UP\"." |
| 20 | q108 | `terminology/core/interventions.md#Route of Administration Response$` | OR (与 `VARIABLE_INDEX.md#§三 CT 交叉引用: C66729$` 等价) | chunk 抬头 + `knowledge_base/terminology/core/interventions.md:483` | chunk: "Used by variable(s): AG.AGROUTE, CM.CMROUTE, EC.ECROUTE, EX.EXROUTE, PR.PRROUTE, SU.SUROUTE." / 文件: "## Route of Administration Response (C66729)" |
| 21 | q109 | `terminology/core/general_part2.md#Laterality$` | OR (与 `VARIABLE_INDEX.md#§三 CT 交叉引用: C99073$` 等价) | chunk 抬头 + `knowledge_base/terminology/core/general_part2.md:205` | chunk: "Used by variable(s): CV.CVLAT, EC.ECLAT, EX.EXLAT, … VS.VSLAT." (17 个) / 文件: "## Laterality (C99073)" |
| 22 | q111 | `terminology/core/interventions.md#Position$` | OR (与 `VARIABLE_INDEX.md#§三 CT 交叉引用: C71148$` 等价) | chunk 抬头 + `knowledge_base/terminology/core/interventions.md:313` | chunk: "Used by variable(s): CV.CVPOS, EG.EGPOS, FT.FTPOS, MK.MKPOS, RE.REPOS, VS.VSPOS." / 文件: "## Position (C71148)" |
| 23 | q112 | `terminology/core/general_part4.md#Reference Range Indicator$` | OR (与 `VARIABLE_INDEX.md#§三 CT 交叉引用: C78736$` 等价) | chunk 抬头 + `knowledge_base/terminology/core/general_part4.md:63` | chunk: "Used by variable(s): CP.CPNRIND, IS.ISNRIND, LB.LBNRIND, MS.MSNRIND, OE.OENRIND." / 文件: "## Reference Range Indicator (C78736)" |
| 24 | q115 | `chapters/ch08_relationships.md#8.4.1 Supplemental Qualifiers (SUPP--)$` | OR (与 `domains/SUPPQUAL/spec.md` 及下一行三选一) | `knowledge_base/chapters/ch08_relationships.md:203`(QORIG 行), `:204`(QEVAL 行); 节头 `:189` | "QORIG … Because QVAL can represent a mixture of collected (on a CRF), derived, or assigned items, QORIG is used to indicate the origin of this data." / "QEVAL … Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain objectively collected …" |
| 25 | q115 | `domains/SUPPQUAL/assumptions.md#overview$` | OR (同上组) | `knowledge_base/domains/SUPPQUAL/assumptions.md:5`(QORIG/QEVAL 职责), `:7`(QEVAL 何时置空) | "…the origin (QORIG) of the value (see Section 4.1.8, Origin Metadata), and the evaluator (QEVAL) to specify the role of the individual who assigned the value…" + "For objective data, the value in QEVAL will be null. For subjective data, the value in QEVAL should reflect the role of the person or institution assigning the value" |
| 26 | q117 | `chapters/ch04_general_assumptions.md#4.5.4 Evaluators in the Interventions and Events Observation Classes$` | OR (与 `chapters/ch08_relationships.md` 等价) | `knowledge_base/chapters/ch04_general_assumptions.md:1371`; 节头 `:1365` | "For observations that have primary and secondary evaluations of specific qualifier variables, sponsors should put data from the primary evaluation into the standard domain dataset and data from the secondary evaluation into the Supplemental Qualifier datasets (SUPP--). Within each SUPP-- record, the value for QNAM should be formed by appending a \"1\" to the corresponding standard domain variable name." + suppae.xpt 示例 (AESEV1/AEREL1, QEVAL = ADJUDICATION COMMITTEE) |
| 27 | q126 | `model/03_special_purpose_domains.md#Subject Elements (SE)$` | OR (与 `domains/SE/assumptions.md` 等价) | `knowledge_base/model/03_special_purpose_domains.md:97-113` | "Describes the actual Elements (blocks of time) experienced by each subject during the study. Planned elements are described in the Trial Design Model. Because actual data does not always follow the plan, the SDTM allows for descriptions of an unplanned element for subjects (SEUPDES)." + 变量表 "SEUPDES … Used only if ETCD has a value of \"UNPLAN\"" |

### 4.1 实施方必须先决策的一件事

第 5/14 行与第 2/19 行是**同一个 chunk 被两道题分别命中**、以及**同一道题的两个等价源**:

- `terminology/core/general_part4.md#No Yes Response$` 同时是 q34 与 q67 的应补项 (两题都问 C66742);
- q19 与 q91 是孪生题, 现有 gold 一个收 `DS/spec.md` 一个收 `DS/assumptions.md` —— 建议**两题统一成同一个 OR 组** `[domains/DS/spec.md#DSDECOD$, domains/DS/assumptions.md#item_3$]` + `terminology/core/disposition.md`, 而不是各补各的。

同理, §4 里 14 条 A 类缺口的根因是 gold 写法不统一, 建议**成组统一**而非逐题打补丁: 凡"变量 V 的码表 code / 码表 C 覆盖哪些变量"型题, gold 一律写成 `expected_sources_any: [domains/X/spec.md#V$, terminology/core/<file>.md#<码表名>$, VARIABLE_INDEX.md#§三 CT 交叉引用: C…$]`。

---

## 5. 我的不确定项 (判不准 / 判得勉强的)

下列 10 条我给了 `不补`(或勉强给了 `应补`), 但门槛卡在灰区, 建议实施方复核。**若要改判, 请只改这几条, 不要顺手放宽 §1 的门槛。**

| 题号 | source#section | 我的判定 | 卡在哪 |
|------|---------------|---------|--------|
| q39 | `chapters/ch08_relationships.md#8.6.3 …` | **应补 (勉强)** | ch08:317 确实逐字定义了 FA "represent findings about events … also findings about interventions", 但题干第二问"与标准 Findings 类有何不同"该节几乎没正面写 (那句对比在 ch08:289, 属另一 chunk); 而现 gold `model/02_observation_classes.md:182` 已把 FA 定义得更准 ("a subtype of Findings … with the addition of the --OBJ variable")。若认为"gold 已有更好的源就不必补", 这条该退回 `相关但非权威_不补` |
| q47 | `VARIABLE_INDEX.md#QS — Questionnaires (Findings)` | 不补 | 索引表逐字给出 `QSTESTCD \| Question Short Name \| Topic` 与 `QSCAT \| … \| Grouping Qualifier \| C100129`, 严格按"字面答某一问"读是命中了"QSTESTCD 起什么 role"; 我按 T2(派生索引) 否掉。若判定方认为"role"就该按 SDTM Role 列理解, 这条该翻 |
| q58 | `VARIABLE_INDEX.md#TS — Trial Summary (Trial Design)` | 不补 | 同上: 索引表含 `TSPARMCD … C66738`, 字面答了"码表 code"这一问, 但丢了题干另一问的长度上限(8 字符); 按 T2 否掉 |
| q88 | `domains/TS/spec.md#TSPARMCD` / `DM/spec.md#ARMCD` / `TA/spec.md#ARMCD` | 不补 (3 条) | 这三条**确实逐字**给出"TSPARMCD 限 8 字符、无特殊字符限制"和"ARMCD 限 20 字符、不受 TESTCD 字符限制"; 我按"片段不算答案源"否掉 —— 题干要的是 ETCD/TSPARMCD/ARMCD 与 --TESTCD 四者的对比集合, 单条只覆盖一项, 补进 AND 组反而会让判据错判。若改成 OR 组则可补 |
| q15 | `chapters/ch01_introduction.md#whole_file` | 不补 | ch01:88 图例行逐字写了 "Core \| \"Req\" (Required), \"Exp\" (Expected), or \"Perm\" (Permissible)", 字面答了"三类 Core 指派是哪三类"; 但那是规格表列说明的一格, 无定义、无题干第二问(Permissible 未采集时怎么办)的任何内容 |
| q77 | `domains/TA/assumptions.md#item_12` | 不补 | 该条逐字说 "EPOCH may be used as a timing variable in other datasets, such as Exposure (EX) and Disposition (DS)" —— 字面同时答了"列举几个用 EPOCH 的域"和"它是什么类型的变量"; 我因它只举 2 个域且属 TA 内顺带举例而否掉。若"several"按 2 个也算, 这条该翻 |
| q31 | `domains/EX/assumptions.md#item_5` | 不补 | "Collected exposure data points are to be represented in the EC domain" 字面答了 EC 的用途/使用时机, 但完全没写 EX 的用途, 半边答案 |
| q89 | `domains/SV/assumptions.md#item_15` | 不补 | item_15e/f 顺带描述了 --STRF/--ENRF 与 --STRTPT/--ENRTPT 的取值形态(before/during/after 参考期), 字面沾到题干第二问; 但整条的语境是"SV 域该不该加这些变量", 且已有 ch04 全文件 gold 覆盖 |
| q122 | `domains/DM/spec.md#DTHFL` | 不补 | "Should be populated even when the death date is unknown" 字面答了"若受试者报告死亡 DM 要做什么"; 按"片段不算答案源"否掉 (主问是随访数据进哪些域)。若判定方认为该题两问并列, 这条该翻 |
| q21 / q61 | `terminology/core/lb_part2.md#lb_part2` / `microbiology_part2.md#microbiology_part2` | 不补 | 这两个整文件 chunk 里有 "## Laboratory Test Code (C65047)" / "## Microbiology Test Code (C120527)", 正是题干要的码表 code, 但**没有** `Used by variable(s)` 行把码表连到 LBTESTCD/MBTESTCD (已 grep 核实)。要判"字面答了"就得默认读者已知"Laboratory Test Code 就是 LBTESTCD 的表" —— 这正是本项目翻过车的那种推断, 故不补 |
| q127 | `terminology/core/other_part1.md#Biospecimen Characteristics Test Name` | 不补 | 抬头 "Used by variable(s): BS.BSTEST" + 取值含 Size/Length/Mass, 字面指向"样本特征在 BS", 但题干要的是 BE(处理动作) 与 BS(样本特征) 的**分工对照**, 该 chunk 只有一侧 |

### 5.1 一条方法学提醒

本轮 14 条 A 类应补项全部依赖 chunk 抬头的 `Used by variable(s)` 行, 而**那行不在 `knowledge_base/` 文件正文里** —— 它由 `scripts/chunkers/terminology.py:260` 在切块时注入。这意味着:

1. 判定成立的前提是"判定依据 = 被召回 chunk 的正文", 这与本任务协议一致;
2. 但**若日后改了 chunker 或关掉该注入, 这 14 条 gold 会同时失效**。建议补 gold 的同时加一条 chunk 层断言 (仿 `evidence/checkpoints/rule_A_chunk_atom_alignment.md` 的做法): "terminology 码表 chunk 必须以 `Used by variable(s):` 开头", 否则这批 gold 会在无人察觉时变成永久假阴性。

---

## 6. Step 7 实施记录 (由实施方 task3-impl 填写, 2026-08-07)

判定的 27 条 `遗漏_应补` **全部落地**, 涉及 26 题。零条被"因不好写而跳过", 零条为凑数硬补。
§5 的 10 条灰区**维持原判未翻**(见下 §6.3)。

### 6.1 OR/AND 形态: 4 处偏离本文件的建议, 全部朝"不放宽"方向

本文件 §4 的「建议形态」列有 20 条标 OR。实施时逐条对照了 `check_source_recall` docstring 的
OR 组使用纪律第 1 条(**每个成员必须独立覆盖全部 expected_facts**), 有 4 条不满足, 改判为 AND:

| 题号 | 本文件建议 | 实际采用 | 不满足纪律的理由 (实测) |
|---|---|---|---|
| q43 | OR | **AND** | 题干明确要"**describe the Core designation**"。`terminology/core/dm.md#Sex$` 的 chunk 正文只有 `Used by variable(s): DM.SEX` + 码表名/code/Extensible/提交值, **没有 Core 指派**(Core=Req 只在 `domains/DM/spec.md`)。并成 OR = 只召回码表 chunk 也算满分, 而它答不出 Core |
| q45 | OR | **AND** | 同上, 题干问 "what is its Core designation"; `#Race$` chunk 无 Core(Exp) |
| q62 | OR | **AND** | 题干第一问是 "**What is the SS domain**" + 要 Findings/Topic; 码表 chunk 只有 SSTESTCD 的 code 与取值, 描述不了域本身 |
| q39 | OR | **AND** | `ch08#8.6.3` 无 `FAOBJ`, 而题干第二问"与标准 Findings 有何不同"正靠 FAOBJ 区分(现 gold `model/02` 有)。本文件 §5 自己也把这条列为"勉强应补" |

其余 16 条 OR 建议全部照采。**采用 OR 的判断依据**: 新源与被替换的现有 gold 各自独立回答全题 ——
「码表 C 覆盖哪些变量」族(q34/q67/q68/q108/q109/q111/q112)是最干净的一类: 现 gold 是派生索引
`VARIABLE_INDEX §三` 的一行, 新源是码表 chunk 抬头, **两者都逐条枚举同一个变量全集**, 互为等价。

### 6.2 成组统一, 未逐题打补丁

- **「码表 C 覆盖哪些变量」族 7 题** → 统一 `OR: [VARIABLE_INDEX §三 Cxxxxx$, terminology/core/*.md#<码表名>$]`
- **「变量 V 用哪个码表」族** → 统一把 `terminology/core/*.md#<码表名>$` 收进 gold; 这与题集**既有 17 题**
  (`q16/q90/q92/q94/q95/q96/q97/q98/q99/q101/q102/s01/s04/s05/q19/q91/q93`)的
  `[domains/X/spec.md, terminology/core/*.md]` 写法同向, 只是升级成 section 级(路径级对
  多 chunk 大文件判别力≈0)。q43/q45/q62 走 AND 正是**对齐 s01/q92 的既有 AND 写法**
- **孪生题 q19/q91** → 按 §4.1 建议统一成同一组: 两题现在都是
  `AND: [terminology/core/disposition.md]` + `OR: [DS/spec.md#DSDECOD$, DS/assumptions.md#item_3$]`,
  彻底消除"一个收 spec 一个收 assumptions"的自相矛盾

### 6.3 §5 灰区 10 条: 维持原判

未翻任何一条(q39 的**形态**由 OR 改 AND, 但**verdict 仍是应补**, 不属翻案)。
理由: 判定方已按统一门槛判过, 个案翻盘会破坏门槛一致性。列为 follow-up。

### 6.4 逐题前后 diff

| 题号 | 形态 | 改前 gold | 改后 gold | recall 前→后 |
|---|---|---|---|---|
| q10 | AND | AND: `domains/TR/assumptions.md`, `domains/TR/spec.md` | AND: `domains/TR/assumptions.md`, `domains/TR/spec.md`, `domains/RS/assumptions.md#item_4$` | 1.0 → 1.0 |
| q19 | OR | AND: `domains/DS/assumptions.md`, `terminology/core/disposition.md` | AND: `terminology/core/disposition.md`<br>OR: `domains/DS/spec.md#DSDECOD$`, `domains/DS/assumptions.md#item_3$` | 1.0 → 1.0 |
| q25 | AND | AND: `domains/MH/assumptions.md` | AND: `domains/MH/assumptions.md`, `domains/MH/spec.md#MHTERM$` | 1.0 → 1.0 |
| q26 | AND | AND: `domains/EG/spec.md` | AND: `domains/EG/spec.md`, `terminology/core/eg_part3.md#Holter ECG Test Code$` | 1.0 → 1.0 |
| q34 | OR | AND: `VARIABLE_INDEX.md#§三 CT 交叉引用: C66742$` | OR: `VARIABLE_INDEX.md#§三 CT 交叉引用: C66742$`, `terminology/core/general_part4.md#No Yes Response$` | 1.0 → 1.0 |
| q38 | OR | AND: `chapters/ch02`, `chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$` | AND: `chapters/ch02`<br>OR: `chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$`, `chapters/ch04_general_assumptions.md#4.1.6 Additional Guidance on Dataset Naming$` | 0.0 → 0.5  **变** |
| q39 | AND | AND: `model/02_observation_classes.md` | AND: `model/02_observation_classes.md`, `chapters/ch08_relationships.md#8.6.3 Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions$` | 1.0 → 1.0 |
| q43 | AND | AND: `domains/DM/spec.md` | AND: `domains/DM/spec.md`, `terminology/core/dm.md#Sex$` | 1.0 → 1.0 |
| q45 | AND | AND: `domains/DM/spec.md` | AND: `domains/DM/spec.md`, `terminology/core/dm.md#Race$` | 1.0 → 1.0 |
| q46 | OR | AND: `domains/AE/spec.md` | OR: `domains/AE/spec.md`, `terminology/core/ae.md#Outcome of Event$` | 1.0 → 1.0 |
| q48 | OR | AND: `domains/FA/spec.md` | OR: `domains/FA/spec.md`, `terminology/core/findings_about.md#Findings About Test Code$` | 1.0 → 1.0 |
| q59 | OR | AND: `domains/DD/spec.md` | OR: `domains/DD/spec.md`, `terminology/core/other_part4.md#SDTM Death Diagnosis and Details Test Code$` | 1.0 → 1.0 |
| q62 | AND | AND: `domains/SS/spec.md` | AND: `domains/SS/spec.md`, `terminology/core/other_part5.md#Subject Status Test Code$` | 1.0 → 1.0 |
| q67 | OR | AND: `VARIABLE_INDEX.md#§三 CT 交叉引用: C66742$` | OR: `VARIABLE_INDEX.md#§三 CT 交叉引用: C66742$`, `terminology/core/general_part4.md#No Yes Response$` | 1.0 → 1.0 |
| q68 | OR | AND: `VARIABLE_INDEX.md#§三 CT 交叉引用: C66789$` | OR: `VARIABLE_INDEX.md#§三 CT 交叉引用: C66789$`, `terminology/core/general_part4.md#Not Done$` | 1.0 → 1.0 |
| q73 | OR | AND: `model/06_relationship_datasets.md` | OR: `model/06_relationship_datasets.md`, `VARIABLE_INDEX.md#§一 通用变量: RDOMAIN$` | 1.0 → 1.0 |
| q76 | AND | AND: `model/04_associated_persons.md` | AND: `model/04_associated_persons.md`, `model/06_relationship_datasets.md#6.6 Associated Persons Related Subjects (APRELSUB)$` | 1.0 → 1.0 |
| q82 | OR | AND: `model/02_observation_classes.md` | OR: `model/02_observation_classes.md`, `chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$` | 1.0 → 1.0 |
| q91 | OR | AND: `domains/DS/spec.md`, `terminology/core/disposition.md` | AND: `terminology/core/disposition.md`<br>OR: `domains/DS/spec.md#DSDECOD$`, `domains/DS/assumptions.md#item_3$` | 1.0 → 1.0 |
| q108 | OR | AND: `VARIABLE_INDEX.md#§三 CT 交叉引用: C66729$` | OR: `VARIABLE_INDEX.md#§三 CT 交叉引用: C66729$`, `terminology/core/interventions.md#Route of Administration Response$` | 1.0 → 1.0 |
| q109 | OR | AND: `VARIABLE_INDEX.md#§三 CT 交叉引用: C99073$` | OR: `VARIABLE_INDEX.md#§三 CT 交叉引用: C99073$`, `terminology/core/general_part2.md#Laterality$` | 1.0 → 1.0 |
| q111 | OR | AND: `VARIABLE_INDEX.md#§三 CT 交叉引用: C71148$` | OR: `VARIABLE_INDEX.md#§三 CT 交叉引用: C71148$`, `terminology/core/interventions.md#Position$` | 1.0 → 1.0 |
| q112 | OR | AND: `VARIABLE_INDEX.md#§三 CT 交叉引用: C78736$` | OR: `VARIABLE_INDEX.md#§三 CT 交叉引用: C78736$`, `terminology/core/general_part4.md#Reference Range Indicator$` | 1.0 → 1.0 |
| q115 | OR | AND: `domains/SUPPQUAL/spec.md` | OR: `domains/SUPPQUAL/spec.md`, `chapters/ch08_relationships.md#8.4.1 Supplemental Qualifiers (SUPP--)$`, `domains/SUPPQUAL/assumptions.md#overview$` | 1.0 → 1.0 |
| q117 | OR | AND: `chapters/ch08_relationships.md` | OR: `chapters/ch08_relationships.md`, `chapters/ch04_general_assumptions.md#4.5.4 Evaluators in the Interventions and Events Observation Classes$` | 1.0 → 1.0 |
| q126 | OR | AND: `domains/SE/assumptions.md`, `domains/TE/spec.md` | AND: `domains/TE/spec.md`<br>OR: `domains/SE/assumptions.md`, `model/03_special_purpose_domains.md#Subject Elements (SE)$` | 0.5 → 0.5 |

**26 题里只有 q38 的分数变了 (0.0 → 0.5)**。其余 25 题改前改后同分 —— 这正是预期:
它们本来就命中了现有 gold, 补进来的是**判据视野**(让真正的权威源被判据看见), 不是分数。
换句话说, 这 26 处改动**没有制造任何"白得的分"**。

### 6.5 chunk 层断言已就位

`scripts/tests/test_terminology_usage_line.py` (4 条断言)。锁住 14 条 A 类 gold 依赖的
`Used by variable(s):` 抬头 —— 该行由 `scripts/chunkers/terminology.py` 注入, **实测不在
`knowledge_base/terminology/core/*.md` 的 42 个文件中任何一个里**(`grep` 零命中)。
闸是 gold 驱动的(随 gold 自动扩张), 不是"所有码表 chunk 都必须有" —— 实测 258 个
terminology chunk 只有 134 个(51%)带该行, 注入是有条件的, 写成全量断言会当场误报。

**已反向验证会红**(两个分支都验了, 见 task-3-report.md), 不是从没红过的闸。
