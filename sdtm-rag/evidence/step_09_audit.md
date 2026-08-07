# Step 09 — 规则 A 独立语义抽检

> 抽检方: task9-auditor (独立第三方, 非本轮实现方/评审方 — 规则 D 隔离)
> 日期: 2026-08-07
> 抽样总体: **本轮变更集合** (非变更后全库) — 三块: ① 27 条改动 gold (涉 26 题); ② chapters chunker 取消整文件单块档 + 重灌索引; ③ 新增判据/闸
> N = 8 (plan 写死), 按风险配比, 非平均分配

---

## 0. 复跑环境与全局命令

本文所有数字均出自以下命令, 可原样复跑 (cwd = `sdtm-rag/`):

```bash
# (A) 独立重跑检索评测
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --hybrid \
  --structured-lookup --output /tmp/audit_rerun.json

# (B) 三道闸
.venv/bin/python -m pytest scripts/tests/test_section_gold_exists.py \
  scripts/tests/test_terminology_usage_line.py scripts/tests/test_source_match_shared.py -q

# (C) 从 chroma 取 chunk 正文 (本文所有"正文摘录"的来源)
.venv/bin/python -c "
import chromadb
c=chromadb.PersistentClient(path='data/chroma').get_collection('sdtm_kb_v1')
a=c.get(include=['documents','metadatas'])
for d,m in zip(a['documents'],a['metadatas']):
    if m['source'].endswith('terminology/core/dm.md') and m['section']=='Sex': print(d)"

# (D) gold 计数
.venv/bin/python -c "
import sys; sys.path.insert(0,'.')
from eval.run_eval import load_test_set
qs=load_test_set('eval/test_set_v3.yml')
term=[(q['id'],g) for q in qs for g in ((q.get('expected_sources') or [])+(q.get('expected_sources_any') or [])) if '#' in str(g) and 'terminology/core' in str(g)]
sec=[(q['id'],g) for q in qs for g in ((q.get('expected_sources') or [])+(q.get('expected_sources_any') or [])) if '#' in str(g)]
print(len(term), len(sec), sum(1 for q in qs if q.get('expected_sources_any')))"
```

**(A) 独立复现结果** (未采信任何既有 JSON, 全新跑):

```
source_recall_avg = 0.9917   (140 题, retrieval-only, hybrid + structured_lookup)
by category: concept 0.9733 / cross_domain 0.99 / mixed 1.0 / single_domain 1.0
Questions with source misses (2):
  q38:  src=33%  miss=['chapters/ch02', 'chapters/ch04...#4.2.2 Two-character Domain Identifier$']
  q126: src=50%  miss=['domains/TE/spec.md']
```

与仓内 `evidence/checkpoints/gold_integrity_after.json` **逐位相同** (`source_recall_avg` 0.9917, 四个 category 全同)。
且 **q38 recall 仍 0.3333、q126 仍 0.5** —— 实现方主动声明的两条限制, 本抽检独立证实为真, 未被粉饰。

**(D) 计数复现**: terminology section gold = **14**, 全题集 section gold = **49**, OR 组题 = **15**。三个数与文档声称逐一相同。

---

## 1. 抽样清单 (8 个, 及选它的理由)

| # | 样本 | 所属块 | 为什么抽它 (风险) |
|---|------|--------|------------------|
| S1 | q43 `terminology/core/dm.md#Sex$` | ① | 14 条依赖**注入抬头**的 gold 的代表; 抬头不在 KB 正文, 判据建在生成物上 = 最高风险 |
| S2 | q46 `terminology/core/ae.md#Outcome of Event$` | ① | 本轮把它从 OR **撤回 AND** 的决策; 撤回对不对直接决定判别力 |
| S3 | q108 `terminology/core/interventions.md#Route of Administration Response$` | ① | OR 组 + 大码表 chunk (12635 字符), 检验"成员独立覆盖全部 facts" |
| S4 | q38 三源 AND (§4.2.2 / §4.1.6 / ch02) | ① | 本轮唯一分数变动题; "两节互补不可互替" 是撤回 OR 的**唯一**理由, 必须验 |
| S5 | **全部 15 个 OR 组的纪律第 1 条机械扫描** | ① | OR 组是本轮引入的**全新计分单位** (改前使用数 = 0), 且 `check_source_recall` docstring 记过一次实际翻车 |
| S6 | ch01/ch02/ch03 切分后 chunk 边界 + 丢失前言 | ② | 语义单元是否被切断 / 前言不入索引是否致上下文缺失 |
| S7 | `test_terminology_usage_line.py` (抬头 chunk 层闸) | ③ | S1 的 14 条 gold 全靠它锁住; 闸若不会红 = 装饰 |
| S8 | `test_section_gold_exists.py` (section gold 存在性闸) | ③ | 49 条 section gold 的静默失效防线; 同上 |

---

## 2. 逐样本核验

### S1 — q43 `terminology/core/dm.md#Sex$` (代表 14 条注入抬头 gold) → **PASS**

题干: *"What is the controlled terminology codelist for the SEX variable in the DM domain? Provide the codelist code and describe the Core designation."*

从 chroma 实取该 chunk 正文 (命令 C), **首行即注入抬头**:

```
Used by variable(s): DM.SEX.

## Sex (C66731)

Extensible: No

| Code | CDISC Submission Value | ... |
| C16576 | F | Female | ... |
```

- **T1 字面性**: 第 1 行 `Used by variable(s): DM.SEX.` + 第 3 行 `## Sex (C66731)` 合起来逐字回答"DM 的 SEX 变量用哪个码表 / 码表 code 是什么" → 成立。
- 抬头确实**不在** `knowledge_base/terminology/core/dm.md` 正文里 (S7 的闸 `test_usage_line_is_injected_not_authored` 全库扫 `terminology/core/*.md` 无一命中, 绿)。判定方按 chunk 正文判、而非按 KB 文件判, **口径正确**。
- 另抽验同族 3 条, 抬头均实存: `ae.md#Outcome of Event` → `Used by variable(s): AE.AEOUT.`; `eg_part3.md#Holter ECG Test Code` → `Used by variable(s): EG.EGTESTCD.`; `interventions.md#Route of Administration Response` → `Used by variable(s): AG.AGROUTE, CM.CMROUTE, EC.ECROUTE, EX.EXROUTE, PR.PRROUTE, SU.SUROUTE.`
- 14 条全量由 S7 的闸覆盖 (绿)。

⚠️ 遗留风险 (非缺陷, 属结构事实): Core 指派 (`Req`) **不在**码表 chunk 里, 只在 `domains/DM/spec.md`。q43 写成 AND (两源都要), 正确。

### S2 — q46 从 OR 撤回 AND → **PASS (撤回是对的)**

题干要 `AEOUT` + `C66768` + **`Perm`** 三个 fact。实测码表 chunk 正文:

```
'Perm' in chunk  -> False
'C66768' in chunk -> True
```

Core 指派 `Perm` 只在 `domains/AE/spec.md`, 码表 chunk 里没有。若并成 OR, 只召回码表 chunk 也判满分而答不出 `Perm` —— 正是 `check_source_recall` docstring 纪律第 1 条要挡的。**撤回 AND 的技术判定成立**, 且与 q43/q45/q59/q62 同形处理一致。

### S3 — q108 OR 组成员独立覆盖 → **PASS**

题干 4 个 fact: `C66729` / `CM.CMROUTE` / `EX.EXROUTE` / `SU.SUROUTE`。
新增成员 `terminology/core/interventions.md#Route of Administration Response$` 正文抬头一行即列出全部三个变量, 第 3 行给出 `C66729`:

```
Used by variable(s): AG.AGROUTE, CM.CMROUTE, EC.ECROUTE, EX.EXROUTE, PR.PRROUTE, SU.SUROUTE.
## Route of Administration Response (C66729)
```

4/4 fact 独立覆盖。另一成员 `VARIABLE_INDEX.md#§三 CT 交叉引用: C66729$` 亦 4/4。**该 OR 组两成员均合格。** q109 / q111 / q112 / q67 / q82 / q48 同形, 机械扫描亦全绿 (见 S5)。

### S4 — q38 "§4.2.2 与 §4.1.6 互补, 不可互替" → **PASS**

撤回 OR 的唯一理由是两节互补。实测两 chunk 正文 (命令 C):

```
              'two-character'  'Two-character'  '2-character'
§4.1.6            False            False           False
§4.2.2            False            True            True
```

- §4.2.2 正文: *"the 2-character domain identifier is used as a prefix… The 2-character domain code is limited to A-Z for the first character, and A-Z, 0-9 for the second character."* → 逐字答"两字符域码的规则"。
- §4.1.6 正文**全文不含**任何 two-character/2-character 变体, 讲的是 `dm.xpt` 命名 + X/Y/Z 自定义域保留 + "Any letter or number may be used in the second position"。
- 两节**确为互补**, 并成 OR 会让只召回 §4.1.6 也判满分而答不出域码字符集规则。**撤回 OR 的技术判定成立**, 且与 yml 内注释所写完全一致 (注释未夸大)。
- q38 recall 仍 0.3333 (命令 A 实测), miss `chapters/ch02` 与 `§4.2.2` —— 挤占证据完整保留在账本里, 未被 OR 抹掉。**这正是撤回 OR 想要的效果, 已兑现。**

### S5 — 全部 15 个 OR 组的纪律第 1 条机械扫描 → **⚠️ 发现问题 (见 §3)**

`check_source_recall` docstring 第 136 行把纪律写成硬规矩:

> `1. any_of 的每个成员必须**独立覆盖全部 expected_facts**;`

我按该条逐字扫描全部 15 个 OR 组 (脚本: 每个成员 → `source_matches` 在全索引上取回它匹配的所有 chunk 正文 → 逐条 `expected_facts` 做大小写不敏感子串, 与 `check_fact_recall` 同口径):

| 结果 | 题号 |
|------|------|
| 合格 (7) | q48 q67 q82 q108 q109 q111 q112 |
| **不合格 (8)** | q19 q34 q68 q73 q91 q115 q117 q126 |

**但机械结果不等于业务结论。** 我逐条读了 8 条不合格的成员正文, 结论分两层 (详见 §3):
- **5 条属"语义答得了、只是措辞与 expected_facts 不同源"** (q115 q117 q19 q91 q126) —— 源判定 (T1/T2) 站得住, 缺陷在 facts 与单一源措辞强耦合。
- **1 条属真正的语义弱成员** (q73)。
- **2 条属既有题目缺陷, 非本轮引入** (q34 q68)。

### S6 — ch01/ch02/ch03 切分后的语义完整性 → **PASS**

`chapters.py` 取消 "≤20KB → 整文件单块" 档后, 索引实测 ch01=5 / ch02=9 / ch03=3 chunk (共 4329, 与声称一致); 全库 `section == 'whole_file'` 的 chunk 数 = **0** (无残留)。

逐块查边界 (每块首 110 / 末 90 字符):

- **ch01 (5 块)**: 每块首行均为 `## 1.x <标题>`, 末尾均落在段落或表格自然结束处 (如 `[3]` 末尾 `| **Core** | "Req"…"Perm" (Permissible) |`)。无跨块截断的表格或句子。
- **ch02 (9 块)**: 同上。含 mermaid 的 `2.6 Creating a New Domain` 完整落在一块内 (`[6]`, 3155 字符, 首行即 ` ```mermaid `)。
- **ch03 (3 块)**: 最大块 `[1] 3.2 …` 为 4400 token / 17171 字符, 低于 8191 token 的 embedding 上限, 无截断风险。边界干净。
  ⚠️ 附带观察 (非本轮引入): ch03 源文档把 `## 3.2.2 Conformance` 写成 H2 而 3.2.1 等在 H2 内, 属源文档标题层级不一致, 切分忠实反映了它。

**首个 H2 前的前言丢失 — 实测无害**:

```bash
for f in ch01_introduction ch02_fundamentals ch03_submitting_data; do
  awk '/^## /{exit} {print}' knowledge_base/chapters/$f.md; done
```

丢的全部内容仅两行 (以 ch02 为例):

```
# SDTMIG v3.4 — Chapter 2: Fundamentals of the SDTM

Source: SDTMIG v3.4, Section 2 (Pages 13-20)
```

三条判据说明它无害:
1. 全库实测 **含 `Source: SDTMIG` 的 chunk 数 = 0** —— ch04-ch10 (早已按 H2/H3 切) 从来就没有这行。本次改动是把 ch01-03 **对齐到既有行为**, 不是新增一类损失。
2. 章标题经 metadata `source` 保留, 且 `server/rag.py:853` 拼 context 时写的是 `### [{i}] {c.source} -- {c.section}` —— 模型看得见章文件名与节名, 章身份未丢。
3. 每块首行自带 `## 1.x / 2.x / 3.x` 编号, 自我标识。仅 ch02 两块 (`Section 1 Context (Reference Material)` / `Findings About — Naming…`) 无编号, 但其章身份仍由 source 路径提供。

### S7 — 抬头 chunk 层闸: 是否真在检验它声称的东西 → **PASS (已变异验证)**

闸声称: 14 条 gold 依赖的注入抬头必须真实存在, 否则静默变永久假阴性。
我做了**变异测试** —— 一道不会红的闸就是装饰:

```bash
sed -i '' 's|terminology/core/dm.md#Sex\$|terminology/core/dm.md#SexRENAMED$|' eval/test_set_v3.yml
.venv/bin/python -m pytest scripts/tests/test_terminology_usage_line.py -q
```

结果 **按预期变红**:

```
AssertionError: 以下 gold 在索引里找不到对应 chunk (会静默恒 miss):
    q43: terminology/core/dm.md#SexRENAMED$
```

四个断言的职责分工经查是实的, 非形式绿:
- `test_there_are_terminology_section_golds_to_check` — 护栏的护栏 (解析坏掉→0 条→空转通过), 下限 10, 实测 14。
- `test_usage_line_is_injected_not_authored` — 锁住"这行不在 KB 正文"这个前提本身, 且注释明写"若哪天真被写进正文, 本闸会红: 那是好消息, 但应重新评估而非删断言" —— 方向正确。
- `test_every_terminology_gold_chunk_carries_the_usage_line` — 逐条锁, 已变异验证会红。
- `test_injection_still_alive_at_scale` — 防"逐条还在但机制已废"的假绿, 下限 100 / 实测 134 (51%)。用下限而非全等的理由 (注入有条件) 经查属实。

### S8 — section gold 存在性闸 → **PASS (已变异验证)**

同一次变异中改了 q38/q82 的 §4.2.2 section 名, 闸**按预期变红**并把三条全报出来:

```
AssertionError: 以下 section 级 gold 在索引里不存在 —— 它们会静默恒 miss:
    q38: chapters/ch04_general_assumptions.md#4.2.2 Two-char Domain Ident$
    q43: terminology/core/dm.md#SexRENAMED$
    q82: chapters/ch04_general_assumptions.md#4.2.2 Two-char Domain Ident$
```

关键设计点核实无误: 它**不自带第二份匹配实现**, 直接 `from eval.run_eval import source_matches` (第 19 行), 把整个索引当作"被召回 chunk"喂进去。这正是上一轮 lint 剥 `.md` 造 8 条假阳性的对策, 落实到位。`test_source_match_shared.py:49` 另用源码断言 `"source_matches(" in src` 钉住 `check_source_recall` 必须委托 —— 结构保证而非口头约定。

复原后三个测试文件 **13 passed**, 题集无我的变异残留 (`grep -n "RENAMED\|Two-char Domain Ident" eval/test_set_v3.yml` 无输出)。

---

## 3. 发现的问题

### 【中】OR 组纪律第 1 条被本轮自己新建的 OR 组违反 — 5 题判别力实质下降

本轮把 15 题从 AND 改成 OR 组 (`expected_sources_any`, 改前全题集使用数 = 0)。`check_source_recall` docstring 第 136 行的纪律第 1 条要求"每个成员独立覆盖全部 expected_facts", 实现方对 q43/q45/q46/q59/q62 **正确执行了该纪律** (拒绝并成 OR), 却对自己新建的 OR 组**未同样执行**。

**真正有业务后果的是这 5 题 —— 它们的 OR 组是该题的唯一计分单位** (无 AND 成员), 故只命中最弱成员即得 `source_recall = 1.0`:

| 题 | 最弱成员 | 该成员覆盖的 fact | 性质 |
|----|---------|------------------|------|
| q117 | `chapters/ch04…#4.5.4 Evaluators…$` | **0 / 4** | 新增成员 |
| q73 | `VARIABLE_INDEX.md#§一 通用变量: RDOMAIN$` | 1 / 3 | 新增成员 |
| q115 | `domains/SUPPQUAL/assumptions.md#overview$` | 1 / 3 | 新增成员 |
| q68 | 两成员均缺 `Completion Status` | 2 / 3 | 既有缺陷 (见下) |
| q34 | `VARIABLE_INDEX.md#§三 CT 交叉引用: C66742$` | 1 / 2 | 该成员是**改前的原 gold**, 非本轮引入 |

**但我逐条读了成员正文, 必须把结论分开 —— 不能只报机械结果**:

- **q117 / q115 属"语义答得了, 措辞不同源"**。ch04 §4.5.4 正文写的是 *"sponsors should put data from the primary evaluation into the standard domain dataset and data from the secondary evaluation into the Supplemental Qualifier datasets (SUPP--). …the value for QNAM should be formed by appending a '1'…"* 并附 `ADJUDICATION COMMITTEE` 的 SUPPAE 示例表 —— 它**确实**回答了 q117 的主问 (两份判定如何并存不覆盖)。SUPPQUAL/assumptions#overview 同理, 含 *"For objective data, the value in QEVAL will be null."* 直接答 q115 的"何时留空"。**判定方的 T1/T2 源判定站得住, 我不推翻。** 缺陷在另一处: `expected_facts` 是照 ch08 的措辞逐字抄的 (`'first 6 columns (STUDYID...QNAM) should be unique'`、`'AETRTEMI'`), 与单一源强耦合。后果是 **source_recall 与 fact_recall 会系统性背离** —— 只召回 §4.5.4 时 source 判满分、fact 判 0。
- **q73 是唯一真正语义弱的新增成员**。VI 那条一行正文全文为: `RDOMAIN (Related Domain Abbreviation) — Record Qualifier* variable, type Char, Core Req*. Appears in 3 SDTM domains: CO, RELREC, SUPPQUAL.` 题干是并列两问 ("哪些域携带 RDOMAIN" + "RDOMAIN 标识什么"), 它只答得了前一半, 后一半只有变量标签、没有 `parent` / `2-character` 的实质陈述。按判定方**自己写的 §1.1 细则**"并列问算答案源→补", 补它是对的; 但 q25 同形态 (`MH/spec#MHTERM` 答两问之一) 本轮是补成 **AND**, q73 却补成 **OR**。**同一轮内同形态两种处理, 且 OR 的那个让 1/2 问的答案拿满分。**
- **q34 / q68 非本轮引入**。q68 更值得单记: 题干称 "the Completion Status codelist (C66789)", 但实测 KB 里 C66789 的码表名是 **`Not Done`**; `Completion Status` 是 `--STAT` 的**变量标签**, 只出现在 `VARIABLE_INDEX.md` §二 域变量表行与各域 spec, 而这两处都不在 q68 的 gold 里。**该 fact 在现 gold 下不可满足** —— 属既有出题缺陷, 本轮未引入也未修复。
- **q19 / q91 / q126 我判不构成问题**: 它们保留了 AND 成员, expected_facts 分摊在 AND 与 OR 两侧 (如 q126 的 `One record per planned Element` 由 AND 成员 `domains/TE/spec.md` 承担)。纪律第 1 条按字面套到"有 AND 成员的题"上过严, 不宜据此判缺陷。

**为什么这条没被任何闸拦住 (机制层面)**: `eval/lint_gold.py` 是 **study 轨**的闸 (需要 card catalog), 且第 66 行对 section 级 gold 直接 `raise ValueError`, **根本不作用于 `test_set_v3.yml`**。它的 `or_groups()` 注释明写"语义上『每个成员能否独立回答该题』**由人判**"。本轮就是这个人工环节漏了。**结论: 纪律第 1 条在主题集上目前无任何自动闸, 唯一防线是人, 而本轮该防线未生效。**

**对头条数字的影响**: 99.17% 里, q117/q73/q115 这三题当前实测**均已命中强成员**, 故**本次数字未被虚高** (命令 A 的 miss 列只有 q38/q126 可佐证)。问题是**未来**: 检索一旦退化到只够着弱成员, 分数不会掉 —— 判别力的损失是隐性的、只在回归时才显形。

### 【低】我自身的流程失误 — 在多 agent 并发下变异了共享工作文件

S7/S8 的变异测试我直接 `sed` 改了仓内 `eval/test_set_v3.yml` 再复原。期间另一 agent 并发编辑了同一文件 (q38 注释里指向 gitignored `.superpowers/…` 的指针改成了 `evidence/checkpoints/crowding_and_gold_integrity.md §2.1`)。

**终态已核实无损**: 我的变异无残留 (grep 无输出); 对方那条指针修改**完整保留在工作区**; 三个闸复跑 13 passed; 评测复跑 0.9917 与仓内一致。但正确做法应是在 `/tmp` 副本上变异。记录在此供复盘, 不掩饰。

---

## 4. 未能核实的事项

- ⚠️ **无法从证据验证**: 本轮"新簇结论改单次快照口径" (commit 4109732) 与跨进程抖动探针的统计充分性, 不在 N=8 抽样内, 未独立核验。
- ⚠️ **无法从证据验证**: 层② 判定作废 (量具饱和) 的原始论证 — 按 plan 属已知事项, 未复核。
- 未召回过的 chunk 是否本该进 gold: `gold_gap_verdicts.md` §1.4 已自陈其结论只对"这 182 条被召回过的条目"成立。本抽检**同样受此边界限制**, 不能反证 gold 现在完整。

---

## 5. 总体判定

> ## **有条件 PASS**

**支持 PASS 的部分 (7/8 样本干净)**:
- 14 条注入抬头 gold 的正文依据**逐条属实**, 判定口径 (按 chunk 正文而非 KB 文件) 正确 (S1)。
- 两次"撤回 OR 改 AND"的技术判定 (q46 / q38) **均经正文实测证实成立**, 注释未夸大 (S2 / S4)。
- chapters 切分**未切断任何语义单元**, 丢失前言仅为 H1 标题 + 页码溯源两行, 且全库本就无一 chunk 携带该行 —— 属对齐既有行为, 无害 (S6)。
- 两道新闸**经变异测试证实会红**, 且结构上强制复用 `source_matches` 不自带第二实现 (S7 / S8)。
- 头条数字 **0.9917 独立复现, 与仓内逐位一致**; q38 / q126 两条已声明限制**独立证实为真**, 未被粉饰。

**条件 (需实现方处置后方可判无条件 PASS)**:
1. **q73** — 同形态的 q25 补成 AND 而 q73 补成 OR, 二者择一统一 (建议 q73 改 AND, 理由与 q46/q59 同)。
2. **q117 / q115** — 源判定无误, 但需在 yml 就地记明"expected_facts 措辞绑定 ch08/spec 一侧, OR 成员命中时 fact_recall 会背离", 否则下一个人会把背离误读成检索缺陷。
3. **纪律第 1 条在主题集上无自动闸**这一事实需显式入档 (现只散见于 `lint_gold.py` 的 docstring, 而该文件根本不作用于 `test_set_v3.yml`) —— 否则下一轮同样漏。
4. **q68** 的 `Completion Status` 在现 gold 下不可满足, 建议单开条目跟踪 (**非本轮引入, 不阻塞本轮收口**)。

**判定理由**: 本轮的**核心主张全部经独立核验成立** —— 判据依据属实、撤回 OR 的两处判断正确、切分无语义损伤、闸真会红、数字可复现且限制未隐瞒。不判无条件 PASS 的唯一原因是: 实现方对 OR 纪律第 1 条**只在拒绝时执行、在自建时未执行**, 造成 3 题 (q73/q115/q117) 判别力实质下降。该缺陷**不影响本轮已出的 99.17%**, 属对未来回归的隐性风险, 故为"有条件"而非 FAIL。
