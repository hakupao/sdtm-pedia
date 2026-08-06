# CDISC 判据 section 粒度化 — 收口 checkpoint

> 状态: **DONE** (2026-08-06) — 勘察 + fail-loud 硬前置 + 18 题 gold 改写 + 新基线 + 引用点同步
> 勘察报告: `.superpowers/sdd/cdisc-section-probe.md`
> 范围: **只做 `VARIABLE_INDEX.md` 这 18 题**, 不铺全题集 (依据见 §5)

---

## ⚠️ 基线记账变更 — 引用前必读

```
CDISC 检索基线 (eval/test_set_v3.yml 140q, --retrieval-only --hybrid --structured-lookup)

        旧 (路径级判据)  98.93%
        新 (section 级判据) 95.71%          Δ -3.21 pt
```

**这是判据变准, 不是检索回归。检索侧一行代码没动。**

证据: 本次新旧两个数字用的是**同一份 top-15 检索结果**, 只换了判据 —— 未被改写的
**122 道题 recall 逐位不变 (98.77% → 98.77%)**, 变化全部落在改写的 18 题内 (100.00% → 75.00%)。
`server/rag.py` / `server/structured_lookup.py` / `server/federation.py` 本次零改动。

**旧数字 98.93% 的水分实测约 3pt**, 来自 4 道假命中 (q108/q109/q110/q112) + 1 道半假命中 (q107)。
旧口径下这 5 题合计白得 4.5 分 / 140 = 3.21pt。

引用纪律:
- **95.71% 与历史 98.93% 不可直接比较** —— 判据变更, 不是同一把尺子。
- 旧口径 98.93% 仍可复算 (题集旧版在 git 历史里), 历史 run 记录不作废。
- 引用 95.71% 时必须带上 "section 级判据" 限定, 一如引用 81.07% 必须带 "hybrid-only"。

---

## 1. 问题: 路径级判据对 222-chunk 单文件判别力 ≈ 0

`eval/test_set_v3.yml` 140 题里 **18 题 (12.9%)** 的 gold 是 `VARIABLE_INDEX.md`,
而该文件在索引里有 **222 chunk**。`check_source_recall` 按**路径子串**匹配 —— 命中这 222 个中的
**任意一个**即判满分。

VARIABLE_INDEX 的 222 chunk 恰好是 **222 个互不相同的 section**, 分三个**互不相关**的族:

| 族 | section 形态 | chunk 数 |
|---|---|---|
| 通用变量 | `§一 通用变量: <VAR>` | 24 |
| 域变量表 | `<CODE> — <名称> (<class>)` | 63 |
| CT 交叉引用 | `§三 CT 交叉引用: C<code>` | 135 |

即"答对了是哪个文件"就给分, 而该文件里装着三类毫不相干的东西。

### 成因: S1 注入 + 路径级判据的闭环

`StructuredLookup.resolve()` 对这 18 题**全部**解析出 `VARIABLE_INDEX.md`, S1 再用**文件内
cosine** 取"最相关的 1 个 chunk"前置注入。VI 的 chunk 是极短结构化单行
(`CT Code C99073 — … referenced by 17 variable(s): …`), 与自然语言问句的 embedding 相似度
近乎噪声, 于是文件内选块基本随机。

于是: **S1 保证"VI 的某个 chunk"必在 top-k → 路径级 gold 必满分 → 与选块对错无关。**
`§三 CT 交叉引用: C66734` 这一个坏 chunk 在 q34/q109/q111/q112 **四题都占 rank0**, 不是偶发抖动。

---

## 2. 18 题逐题判定 + 改写前后 recall

判据: **被召回的那个 chunk 本身**能否回答该题, 而非"该文件里有没有这段文字"。

| qid | 问的内容 | 应命中 section | 实际召回 (rank) | 判定 | 旧 | 新 |
|---|---|---|---|---|---|---|
| q07 | EPOCH 分布 | `§一 通用变量: EPOCH` | ✓ rank0 | 真命中 | 1.00 | 1.00 |
| q34 | C66742 共享域 | `§三 CT 交叉引用: C66742` | ✓ rank4 | 真命中 | 1.00 | 1.00 |
| q66 | VISITNUM 分布 | `§一 通用变量: VISITNUM` | ✓ rank0 | 真命中 | 1.00 | 1.00 |
| q67 | C66742 引用数 | `§三 CT 交叉引用: C66742` | ✓ rank12 | 真命中 | 1.00 | 1.00 |
| q68 | C66789 / --STAT | `§三 CT 交叉引用: C66789` | ✓ rank0 | 真命中 | 1.00 | 1.00 |
| q69 | C71620 剂量单位 | `§三 CT 交叉引用: C71620` | ✓ rank4 | 真命中 | 1.00 | 1.00 |
| q71 | C78735 EVAL | `§三 CT 交叉引用: C78735` | ✓ rank0 | 真命中 | 1.00 | 1.00 |
| q77 | EPOCH 分布 | `§一 通用变量: EPOCH` | ✓ rank0 | 真命中 | 1.00 | 1.00 |
| q103 | TAETORD 域数/标签 | `§一 通用变量: TAETORD` | ✓ rank2 | 真命中 | 1.00 | 1.00 |
| q104 | VISITDY 域数/标签 | `§一 通用变量: VISITDY` | ✓ rank0 | 真命中 | 1.00 | 1.00 |
| q105 | NHOID 域/标签 | `§一 通用变量: NHOID` | ✓ rank0 | 真命中 | 1.00 | 1.00 |
| q106 | FOCID 域/标签 | `§一 通用变量: FOCID` | ✓ rank0 | 真命中 | 1.00 | 1.00 |
| q111 | C71148 体位 | `§三 CT 交叉引用: C71148` | ✓ rank8 | 真命中 | 1.00 | 1.00 |
| **q107** | ARM + ARMCD 标签 | `§一…: ARM` **和** `…ARMCD` | 仅 ARMCD (rank0) | **半假命中** | 1.00 | **0.50** |
| **q108** | C66729 给药途径 | `§三 CT 交叉引用: C66729` | ✗ 实召 `CM — Concomitant…` | **假命中** | 1.00 | **0.00** |
| **q109** | C99073 侧别 | `§三 CT 交叉引用: C99073` | ✗ 实召 `§三…: C66734` | **假命中** | 1.00 | **0.00** |
| **q110** | C78734 标本类型 | `§三 CT 交叉引用: C78734` | ✗ 实召 `BS — Biospecimen…` | **假命中** | 1.00 | **0.00** |
| **q112** | C78736 参考范围指示 | `§三 CT 交叉引用: C78736` | ✗ 实召 `§三…: C66734` | **假命中** | 1.00 | **0.00** |

**13 真命中 / 4 假命中 / 1 半假命中。** 子集 100.00% → **75.00%**。

### 假命中不是擦边, 是完全打偏

- **q109** 要 `C99073, TU.TULAT, FA.FALAT, PE.PELAT`。实召 chunk 全文:
  `CT Code C66734 — controlled terminology codelist referenced by 3 variable(s): CO.RDOMAIN, RELREC.RDOMAIN, SUPPQUAL.RDOMAIN.`
  与侧别毫无关系。正确的 C99073 chunk (含 17 个 --LAT) 根本没进 top-15。
- **q112** 同样召回 C66734 (RDOMAIN), 要的是 C78736 (LBNRIND/ISNRIND/OENRIND)。
- **q108** 召回 CM 域变量表, 只能给 `CM.CMROUTE`; gold 还要 `EX.EXROUTE, SU.SUROUTE`。
- **q110** 召回 BS 域变量表, 只能给 `BSSPEC`; gold 要 `RELSPEC.SPEC, LB.LBSPEC, PC.PCSPEC`。

---

## 3. 改动清单

### 3.1 Step 1 (commit `bfc9ad7`) — `路径#` 空 section fail-loud (硬前置)

Plan B Phase 1 checkpoint 记录的硬前置。改写前实测的旧行为:

```python
check_source_recall(["…/VARIABLE_INDEX.md"], ["VARIABLE_INDEX.md#"],
                    retrieved_sections=[None])     # -> (1.0, [...], [])  满分
```

`sec = ""` 时 `"" in (s or "")` 恒 True, 该 gold 不但退化成路径匹配, 还绕过了 docstring 承诺的
"section 为 None 的条目永不命中 section 级 gold" —— **比纯路径写法更松**。改写 gold 时手滑打空
一个 section, 会静默把该题退回本次正要消灭的无判别力口径, 偏差单向朝上、幅度小, 任何闸都拦不住。

修法: `_matches` 里 split 后先校验 `sec.strip()` 非空; 空 section 校验**早于** `retrieved_sections`
缺失校验 (空 section 是 gold 写法错误, 与调用方给没给无关)。TDD 4 条新测试先红后绿。

### 3.2 Step 2 (本 commit) — `路径#节$` 精确匹配语法

section 判据是**子串**语义, 而 VARIABLE_INDEX 有 **6 组 section 互为子串**:

```
§一 通用变量: ARM     ⊂ §一 通用变量: ARMCD
§一 通用变量: IDVAR   ⊂ §一 通用变量: IDVARVAL
§一 通用变量: IETEST  ⊂ §一 通用变量: IETESTCD
§一 通用变量: MIDS    ⊂ §一 通用变量: MIDSTYPE
§一 通用变量: VISIT   ⊂ §一 通用变量: VISITDY
§一 通用变量: VISIT   ⊂ §一 通用变量: VISITNUM
```

q107 要 ARM + ARMCD 两节却只召回 ARMCD, 子串语义下 `#§一 通用变量: ARM` 会被 ARMCD 的 chunk
**冒名命中**, 该题照样满分 —— 正是 section 化要消灭的那种假命中, 只是换到了 section 层。

> **通用教训**: 凡"标识符 + 子串匹配"的判据, 都要问一句"有没有更长的兄弟标识符"。
>
> **但必须各库各自验证, 不能照搬结论** (2026-08-06 的一次实际误判): 本项一度写成
> "子串匹配在两个库制造了同一种病", 引用 study 侧某题作为同形态实例。经 study 侧复核,
> 那题实为**真命中** —— 该处 gold 带 `.md` 后缀, 后缀本身提供了判别力, 兄弟卡并不构成子串;
> 那批"多匹配"发现是 lint 工具的**假阳性** (工具剥掉 `.md` 再匹配, 严于真实判据)。
> study 侧真正失去判别力的是另一条**家族前缀** gold。
>
> 即: 隐患的**形态**确实跨库同源, 但某一处是否真的中招, 取决于该库 gold 的**实际写法**。
> CDISC 侧 `ARM` ⊂ `ARMCD` 是**实测确认**的真碰撞 (q107 的 ARM gold 确实命中了 ARMCD 的
> chunk, 见本文件 §3.2 单测); study 侧那处不是。**判据检查工具必须与被检查的判据逐字同语义**,
> 否则会制造连锁误判。

修法: gold 以 `$` 结尾 = 精确匹配整个 section; 不带 `$` 时子串语义**逐字节不变** (Phase 0 契约
及其单测全部保留)。全库无 section 含 `$`, 该标记不与真实 section 冲突 (已实测)。
`路径#$` (空 section 的另一种写法) 同样 fail-loud。TDD 3 条新测试先红后绿。

### 3.3 Step 2 — 18 题 gold 改写

18 题 → 19 条 gold (q107 拆两条), 全部带 `$` 精确匹配。映射规则可机械推导:

> **题面点名 CT 码 → `§三 CT 交叉引用: <码>`; 题面点名通用变量 → `§一 通用变量: <变量>`。**

不是逐题手工凑数, 也不构成对 example 的"对症下药"。19 个 section 字符串**全部实测精确存在于索引**。
统一加 `$` 而非只给 q107 加: 免疫当前及未来任何 section 子串碰撞, 且 ingest 若改 section 命名
会**响亮**全失败而非静默漏判 —— 保守方向。

---

## 4. Step 3 — 新基线与配对 diff

```
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml \
    --retrieval-only --hybrid --structured-lookup
```

| 口径 | 140 题 | 18 题子集 | 其余 122 题 |
|---|---|---|---|
| 旧 (路径级) | **98.93%** | 100.00% | 98.77% |
| 新 (section 级) | **95.71%** | **75.00%** | **98.77%** (逐位不变) |
| Δ | **-3.21 pt** | -25.00 pt | **0** |

逐题变化**只有 5 题**, 与勘察预估**精确吻合** (预估严格口径 95.71%, 实测 95.71%):

```
q107: 1.00 -> 0.50      q108: 1.00 -> 0.00      q109: 1.00 -> 0.00
q110: 1.00 -> 0.00      q112: 1.00 -> 0.00
```

分类别: concept 96.0% / cross_domain **90.0%** / mixed 100.0% / single_domain 100.0%
(失分全部集中在 cross_domain, 正是 VI 题所在类别)。阈值 85% → **PASS**。

其余 2 道 miss (q38 `chapters/ch02` 0%, q126 `domains/TE/spec.md` 50%) 是**改写前既有**的
已知 miss, 与本次无关 (q126 是已归档的 permanent known limit)。

全量测试: **808 → 815 passed** (+4 fail-loud, +3 精确匹配)。

---

## 5. 为什么只做 VARIABLE_INDEX — 收窄范围的依据

按 gold 反查文件 chunk 数, 次级候选实测**健康**, 对它们做 section 化是**负收益**:

| gold | chunk 数 | 引用题数 | 实测 | 结论 |
|---|---|---|---|---|
| `VARIABLE_INDEX.md` | **222** | **18** | 4 假 + 1 半假 | **唯一结构性坏点, 做** |
| `chapters/ch04_general_assumptions.md` | 47 | 16 | **14/16 rank0 就是正确节** | 不做 |
| `domains/*/spec.md` | 20–66 | ~65 | 抽检 8 题正确变量行都在前 3 | 不做 |

**chunk 数不是正确的风险指标, 主题同质性才是。**

- ch04 各节是**成段散文**, 与问句语义高度重合, cosine 本来就选得准
  (q12→`4.1.5 Core Designations`, q79→`4.2.5 Missing Values`, q81→`4.2.2 Domain Identifier` …)。
- 域 spec 的 20–66 个 chunk **全部属于同一个域**, 召回"错行"仍在正确主题内; 路径级判据在这里
  已隐含"答对了是哪个域"。
- 而 VI 的 222 chunk 横跨 24 变量 + 63 域 + 135 codelist, 三族之间毫无关系。

无收益的改动等于纯风险: 铺开会把"cosine 选了同域邻近行"这种无害情况误判成 miss, 维护面翻几倍。

---

## 6. 已知限制 / 后续

1. **这 4 道假命中暴露的是真实检索缺陷, 尚未修**。S1 对 VI 的文件内选块用 cosine, 而 VI 的
   结构化单行 chunk 对自然语言问句语义近噪声。正解是让 S1 在 VI 内部按 **CT 码 / 变量名字面**
   定位 section (题面已经点名了码), 而不是靠 embedding 猜。**section 化只是把缺陷暴露出来,
   修它是下一步** —— 修完这 4 题应能重回满分, 且那时的满分是真的。
2. **q107 的 ARM 一半是真 miss**, 同上归因 (S1 单文件只注入 1 chunk, 天然给不出两节)。
3. **gold 选错文件属另一类问题, 未处理**: q134 / q64 等问"域用途 / 一条记录的结构", 答案实际在
   `assumptions.md` overview, gold 却写 `spec.md`。与 section 粒度无关, 单独入 backlog。
4. **本次只覆盖 `test_set_v3.yml`**。其他题集 (agg / kgval / sp3 等) 未排查是否有同类大文件 gold。

---

## 7. 复跑

```bash
cd sdtm-rag
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml \
    --retrieval-only --hybrid --structured-lookup        # 95.71% (section 级)
.venv/bin/python -m pytest scripts/tests/test_source_recall_section.py  # 14 passed
```

旧口径 98.93% 复算: `git show bfc9ad7:sdtm-rag/eval/test_set_v3.yml` 取回旧题集即可。
