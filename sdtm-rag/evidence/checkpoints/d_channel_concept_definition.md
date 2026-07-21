# (d) 概念定义→chapters/model 通道 — Kickoff 分诊 + q73/q119 双通道 SHIP

> 状态: **q73 + q119 双通道 SHIPPED** (2026-06-15) — retrieval-only v3 140q:
> cross 95.0→**99.0%** (q73 +2 / q119 +2), single/concept/mixed 100%, 0 回归, pytest 250,
> Rule D code-reviewer **q73 APPROVE_WITH_NITS** (已修) + **q119 APPROVE** (clean)。
> **q126 = 永久 known limitation** (双重独立阻断)。
> 入口: `TODO_retrieval_quality.md §6`。研究法: 6-agent workflow (3 题并行分诊 + 数据源清单 +
> 对抗式 over-fire + 综合) + 主 session 独立复核 (推翻 workflow 对 q119 的 defer) + Rule D。

## 背景 (为什么立这个通道)

S4 修后 cross 卡 **95.0% 零 margin**。残留 q73/q119/q126 同根: 概念/定义型 gold 在
chapters/ 或 model/, 题面不点名域, 现有 S1/s3 通道 (域/变量/CT 码→spec 或 VARIABLE_INDEX)
全够不到。§6 要求"立项先调研, 先分诊三题各自可达性"。

## 三题分诊结论

| 题 | gold | 现状误路由 | 判定 | 根因 |
|----|------|-----------|------|------|
| **q73** | model/06 | →VARIABLE_INDEX (分布意图) | **BUILT ✅** | RDOMAIN 定义家在 model/06; 干净 pattern 级锚 |
| **q119** | ch04 | →RELREC/TU/TR spec | **BUILT ✅** | `--LNKID/--LNKGRP` 通用前缀定义在 ch04; 比较意图锚 |
| **q126** | SE/assumptions + TE/spec | →[] (零锚) | **永久 DEFER** | 题面零实体锚 + 架构阻断 |

### q73 — 已实现 (pattern 级, 零回归)

**机制 (channel d-model)**:
- **BUILD**: 解析 `model/*.md` 变量定义表 (6 列 `| # | VAR | Label | Type | Role | Notes |`),
  建 `var → 单一 model 文件` 的 def-home 映射。**载重判别 = 6 列形状** (隔离 6 列定义表 vs
  5 列 usage 表 [末列是 Role 非 Notes]); 非空 Notes 是次级过滤。保留条件: Notes 行只在
  **唯一**一个 model 文件 (剔 DOMAIN/USUBJID/POOLID 等跨文件歧义) + 排除 `--` 前缀。
  产出 **59 条** def-home, RDOMAIN→model/06。
- **RESOLVE**: 严格定义动词锚 `_DEFVERB_RE` = `what does/is [the] <VAR> [variable]
  (do|identify|define|mean|represent|capture)`。`<VAR>` 大小写敏感 (大写, 同
  `_QUERY_VAR_TOKEN_RE`), 周围散文用 scoped `(?i:...)`。命中且 var 在 def-home 映射 →
  union-add 该 model 文件; 否则 []。
- **接入**: resolve() 早退守卫纳入 concept_defs (使无其他意图的纯定义题也能触发); 注入在
  terminology 块后, 复用既有去重尾。**纯 union-add, 不删**。

**为什么 pattern 级 (非 example-tuned, 用户敏感点)**:
- 映射覆盖 59 个变量 (非只 RDOMAIN), 全 KB 表结构数据驱动, 代码零处引用 q73/q83/题面/变量名。
- **8 道集外探针** (workflow + 主复核): 应触发 3 (RELTYPE/QNAM→model/06, ETCD→model/03)
  全对; 不应触发 5 (分布 ARMCD / 属性 RACE Core / 术语 SEX codelist / 比较 RFSTDTC-RFENDTC /
  "EPOCH used for") 全静默。严格动词表是载重: 加 used/role/bare-mention 会把高频变量
  (RACE/SEX/EPOCH→model/03) 喷进分布/术语/属性题。

**验证 (五层, 全过)**:
1. 通道在 140q 上**恰触发 q73+q83** (均 gold model/06, adds_gold)。q73 (cross) 0→100 载重;
   q83 (concept) cosine 已有 model/06, union-add 冗余无害。
2. **零回归 gate** (retrieval-only v3 140q diff vs `v3_on_fixed.json`): cross 95.0→**97.0**,
   q73 0→100, **回归 0 题**, 其余类别稳 100。产物 `eval/ablation_t1/v3_on_dchannel.{json,log}`。
3. **pytest 244** (新增 `TestConceptDefinitionChannel` 8 用例: 2 canary [RDOMAIN/EPOCH 守 6 列
   隔离不变量] + map 卫生 + q73 union-add + 集外泛化 + must-not-fire battery + 小写不捕获)。
4. **Rule D 异 type** (`oh-my-claudecode:code-reviewer`): **APPROVE_WITH_NITS** (0 CRITICAL/HIGH)。
   独立复跑 pytest 244 + retrieval diff (0 回归确认) + git stash 对照 (确认新行为) + 确认 pattern 级。
   - **MED (doc 正确性) 已采纳**: 我原 docstring 把判别器归因"非空 Notes 单元", 审查员钉出真正
     载重的是 **6 列形状** (5 列 usage 表末列是 Role; 放宽 `!=6` 会把 RDOMAIN 推成多文件 un-fix
     q73)。已重写 docstring + 加 inline 注释 + 加 EPOCH 第二 canary。
   - LOW (EPOCH canary / `--` 冗余守卫) 采纳/记录; INFO 2 项 (定义 under-match 设计取舍 / q83 nit)
     无需动 (q83 nit 主复核实测确为 q73+q83, 审查员 scan 偏差)。

### q119 — 已实现 (channel d-generic, pattern 级, 零回归)

**workflow 综合曾判 DEFER**, 理由: q119 与 q114 锚不可分 (都 RELREC + 通用 --XXX token)。
**主 session 独立复核推翻该理由**: 两题**意图可分**, 非 example 级 ——
- q119: "what exactly is the **difference between** the --LNKID and --LNKGRP **variables**" = 定义/比较意图。
- q114: "...how should I populate RELTYPE... **is it acceptable to use** --SEQ **as the join key**?" = 用法意图。
- q68/q71: "**which domains use** --STAT" = 分布意图 (gold VARIABLE_INDEX)。

**机制 (channel d-generic)**: 通用 `--` 前缀变量是 SDTM 跨域变量约定, 权威定义在 ch04 General
Assumptions (非任何域 spec)。`_query_generic_var_definition(query, dist_intent)` 触发条件:
ch04 存在 AND **非**分布意图 AND 有 `--XXX` token AND ( ("difference between" + **≥2 个不同 `--`
token**) OR `_DASH_DEFVERB_RE` [q73 式动词锚加在 `--` token 上] ) → union-add ch04; 否则 []。
- regex 修: `_DASHVAR_RE = (?<![A-Za-z-])--[A-Z]{2,8}(?![A-Za-z-])` (workflow 指出 `\b--` 匹配空;
  负向前后视另排除连字符防 `--SEQ--ENDTC`/`--SE-Q` 畸形撞 ≥2 计数)。
- ch04 文件 glob `chapters/ch04*.md` 发现 (非硬编码, KB 改名优雅降级)。
- dist 抑制复用既有 `_is_distribution_intent`, 守住 q68/q71 → VARIABLE_INDEX。

**pattern 级证明 (非 example-tuned)**: 140q 上**恰触发 q119** (是题集只有 1 道通用变量定义题,
非规则窄), 但 Rule D 独立集外电池 **8/8 应触发** (--STDTC/--ENDTC, --DUR, --LOC/--LAT, --TESTCD,
--ORRES/--STRESC, 复数 "Differences between" 等, 全非 q119 的变量) + **10/10 应静默** (分布/用法/
无 `--` 比较/单 token 比较)。代码零处引用 q119/--LNKID/--LNKGRP。

**验证**: resolve(q119) union-add ch04 ✓; retrieval-only v3 cross 97→**99.0** (q73 后再 +2),
q119 0→100, **0 回归**; pytest 250 (+`TestGenericVarDefinitionChannel` 6 用例);
**Rule D code-reviewer APPROVE** (clean, 0 CRITICAL/HIGH/MED; 1 LOW [畸形 token 正则加固, 已采纳]
+ 2 INFO [doc bullet 已补 / dist-suppress recall ceiling 记录])。

### q126 — 永久 known limitation (双重独立阻断)

1. **零实体锚 + 不可泛化**: 每个区分性短语 ("study elements"/"planned element"/"off-plan"/
   "assigned arm"/"really experienced") 在 140q 中**恰命中 1 题 (q126 自己)** = 单例真阳 =
   q126 硬编码 (违反 pattern 级硬约束); 放宽到单词 ("arm"→5q/"element"→2q) 喷到 8+ 非 SE/TE
   gold 题。"off-plan" 在 KB 0 命中。
2. **架构阻断**: q126 SE gold = `domains/SE/assumptions.md`, 但 `domain_to_spec` **只映 spec.md**
   (零非 spec 目标); 且同一锚要给 SE 出 assumptions、给 TE 出 spec —— 需新的 sub-file 判别器,
   架构当前没有。现状 resolve()=[] cosine 兜底是正确保守行为。
→ **记为 §6 预警的"无实体锚概念对比边界案", 不修** (修=例级作弊 + 架构件双缺)。

## 改动文件

- `server/structured_lookup.py` —
  - q73 (3a): `_DEFVERB_RE` + `var_to_model_defhome` + `_build_model_defhome_index()` +
    `_query_concept_definition()`
  - q119 (3b): `_DASHVAR_RE`/`_COMPARE_RE`/`_DASH_DEFVERB_RE` + `general_assumptions_file` (ch04 glob) +
    `_query_generic_var_definition()`
  - resolve() 接入: 两通道均 union-add 尾 + 纳入早退守卫
- `scripts/tests/test_structured_lookup.py` — `TestConceptDefinitionChannel` (8) +
  `TestGenericVarDefinitionChannel` (6); 共 pytest 250
- `eval/ablation_t1/v3_on_dchannel{,2}.{json,log}` — 零回归 gate 产物 (q73 / q73+q119)
- 生产语义: structured_lookup 默认开, 两通道随之生效; KB/向量索引/提示词未动

## 残留 / 下一杠杆

- **q126**: 永久 known limitation (上, 双重独立阻断 — 例级作弊 + 架构 spec.md-only 缺 sub-file 判别器)。
- cross 现 **99.0%** (retrieval-only v3, q73+q119 后); single/concept/mixed 100%。剩余 cross 缺口
  主要是 q126 (defer)。若将来要 q126 → 需架构件 (domain_to_spec sub-file 判别器)。
