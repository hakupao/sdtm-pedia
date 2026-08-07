# VI 交叉引用完整性 — 收口 checkpoint

> 状态: **DONE** (2026-08-07) — 三方隔离审查完成; 审查 2 HIGH + 抽检 4 项全部已修, 并因此多修了一个既有缺陷
> 设计 `docs/superpowers/specs/2026-08-07-vi-truncation-completeness-design.md`
> 计划 `docs/superpowers/plans/2026-08-07-vi-truncation-completeness.md`
> 上游: `evidence/checkpoints/s1_variable_index_literal_section.md` §4 已知限制 1 (规则 A 抽检 D-3)

---

## ⚠️ 引用前必读 — v3 的 98.93% 一动不动是**预期**, 不是没效果

```
CDISC v3 检索闸 (140q, --retrieval-only --hybrid --structured-lookup, section 级判据)

    改动前  98.9286%
    改动后  98.9286%      140 题逐题相同, 变化集为空
```

**那把尺子对本修复结构上失明**: section 级 source recall 只看 section 名对不对,
**不看正文是否被截断**。本轮一个 section 名都没改, 所以它必然不动。

**引用本轮成果不得用 v3 数字。** 能证明"修好了"的只有:
- 层① 数据不变量 (§3.1): 3 红 → **7 绿** (含审查方要求补的两条外部锚)
- 层② context A/B (§3.2): 截断答不出 / 完整答得出
- 生产端到端 (§3.4): 答案含旧语料**结构上产不出**的变量

---

## 1. 问题

`VARIABLE_INDEX.md` §三 CT 交叉引用表每行只列前 15 个引用变量就写 `... (N total)`。
**该表是"哪些变量引用这个码表"的唯一权威来源**, 被截断意味着注入的 chunk 正文结构上答不全。

本轮实际修了**两个独立缺陷**, 第二个是三方审查在收口前抓出来的:

| # | 缺陷 | 规模 | 生成器 |
|---|---|---|---|
| 1 | **条数上限截断** —— VI §三 每行只列前 15 个就写 `... (N total)` | **9 / 135 行**, 隐藏 **226** 条 | `generate_variable_index.py:253` |
| 1 | 同病: 域 spec 交叉引用段上限 5 | 2 文件 (AE / LB), 隐藏 **10** 条 | `generate_cross_references.py:236` |
| 2 | **只取 CT 字段首码** (`re.match(r"(C\d+)")`) | **12 个码表在 §三 整行不存在**, **18** 个引用对遗漏 | `generate_variable_index.py:99` |

缺陷 1 最宽: `C66742` 123 / `C71620` 58 / `C99079` 44 / `C66789` 36 / `C66728` 26。

缺陷 2 详情: CT 字段可列多码 (`PP.PPORRESU = "C85494; C128684; C128683; C128685; C128686"`),
该变量对这几个码表都是真引用, 但只有首码进 §三。**§二 渲染全码串, 于是同一文件自相矛盾** ——
§二 说 `BS.BSSPEC` 引用 `C111114`, §三 里 `C111114` 一行都没有。缺失码表:
`C101834 C111114 C114118 C118971 C120522 C120523 C120524 C128683 C128684 C128685 C128686 C150811 C181169`
(12 个整行缺失 + `C111114` 缺条目)。

**与缺陷 1 同类同因**: 该表答不全, 而 section 名照常存在、检索侧判据看不出来。修法是
`extract_ct_code` → `extract_ct_codes` 收全码, §三 **135 → 147 行**。

**为什么现在修**: 上一轮把 18 题 VI 子集拉到 100.00%, 但那个分数**不能读作"VI 类问题已解决"**
—— q109 的 `TU.TULAT` 与 q69 的 `EX.EXDOSU` 都恰好排在**第 15 位 = 截断边界最后一位**, 属压线过关。
gold fact 只要落在第 15 位之后, source recall **仍判 1.00** 而正文根本答不出来。

## 2. 修法

删掉两个生成器的条数上限, 重生成 KB, 重灌索引。**KB 是生成物, 全程未手改。**

体积 **131.3 KiB → 133.8 KiB (+2527 B ≈ +2.5 KB)** —— 旧上限买到的就是这 2.5 KB, 代价是把该表
在最需要它的 9 个宽码表上变成半张表。最宽的 `C66742` 那行约 1.5K 字符, 远在 chunk 尺度内。

> ⚠️ 本段早先写作 "129.6 → 133.8 KB (+4.2 KB)" 并标着"实测非估算" —— **错的**, 129.6 对不上 VI
> 任何历史版本 (真实旧值 131.3 KiB), 因为把 Python 字符数与生成器打印的 KiB 混用, delta 报大 68%,
> 且写进了生成器源码注释。三方审查两方各自独立抓到。详见 §4.3。

**chunk 总数不是证据**: chunker 是逐行切块 (§一 每行 1 块 / §二 每 H3 1 块 / §三 每行 1 块),
无按尺寸再切, 所以行变多长 chunk 数都不变 —— 这是**结构恒等式, 不是观测**。第一轮重灌后
4303 = 基线同数看似"没影响", 实则必然; 第二轮修掉首码提取后 §三 135 → 147 行, chunk 数
随之 4303 → **4315 (+12)**, 同样是恒等式。**正文正确性由 chunk 层断言实测, 不看总数。**

生成器幂等已验: 二次运行零新增变更。改动前已确认生成器未漂移 (重生成与已提交 KB 唯一 diff 是日期行)。

## 3. 实测

### 3.1 层① 数据不变量 (主护栏, 零 LLM, 常驻)

`scripts/tests/test_kb_crossref_completeness.py` —— **先红后绿, 红是数据错不是代码错**:

| 断言 | 改动前 | 改动后 |
|---|---|---|
| 每 CT 行正文条目数 == 自己声称的 N | ❌ 9 行不符 | ✅ |
| VI 全文无截断标记 | ❌ 9 处 | ✅ |
| 域 spec 无截断标记 | ❌ AE / LB | ✅ |
| **§三 覆盖 spec.md 声明的每个 (码, 变量) 引用** ← 外部锚 | ❌ 12 码表整行缺失 + 18 引用对 | ✅ |
| **域 spec 交叉引用段 == 该 spec 自身变量表** ← 外部锚 | ✅ | ✅ |
| §三 行数 == spec.md 声明的不同码表数 | ❌ 135 vs 147 | ✅ |
| **索引里的 CT chunk 正文与 KB 逐条一致** | ❌ 9 个 chunk 不符 (C66742 缺 108 个) | ✅ |

**两条外部锚是审查方 REVISE 后补的, 也是本轮最重要的护栏。** 原先只有"条目数 == 该行自己
声称的 N", 而这两个值出自生成器**同一条 f-string** —— **自洽即通过**。审查方构造了伪造 KB
实证: 把切片放在计数之前 (`refs = sorted(...)[:15]` 再 `ref_count = len(refs)`, 最自然的
一行回归写法), 226 条静默消失而**当时的 5 条断言全绿**。缺陷 2 (12 个码表整行缺失) 正是
这个洞的**现实实例** —— 加上外部锚后它当场显形。

抽检方独立指出同一件事: 层① 对"集合本身对不对"零判别力 (把变量错关到某个码表照样绿);
该格由抽检方用 `source/cdisc/*.xlsx` 独立重算补上 (非 CI 常驻, 见 §6)。

chunk 层那条不能省: KB 对而索引是旧的照样答不出来, 且 `kb_freshness.py` 的存在动因正是
2026-08-04 实测到"部署中的向量库把 `VARIABLE_INDEX.md` 欠切 70%" —— **同一个文件有前科**。

```bash
cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_kb_crossref_completeness.py -q   # 7 passed
```

### 3.2 层② context A/B (改动前/后数字的来源)

不做两次全量重灌: 同一问句喂两份 context (旧的 15 条截断版 / 新的完整版), 同模型 temperature=0,
变量隔离得更干净。

```bash
cd sdtm-rag && .venv/bin/python -m eval.vi_completeness_ab
```

| 码表 | gold (字母序末位) | 截断 context | 完整 context | 判定 |
|---|---|---|---|---|
| `C66742` (N=123) | `VSLOBXFL` (第 123 位) | ❌ 答不出 | ✅ 答得出 | **判别力成立** |
| `C71620` (N=58) | `URSTRESU` (第 58 位) | ❌ 答不出 | ✅ 答得出 | **判别力成立** |

脚本内置两条前置断言 (gold 必须在完整 context 里 / 必须不在截断 context 里), 防止对照本身失效。

### 3.3 层② 独立 gold 集

`eval/test_set_vi_completeness.yml` (2 题, **不并入 v3**)。

```bash
cd sdtm-rag && .venv/bin/python eval/run_eval.py eval/test_set_vi_completeness.yml \
    --hybrid --structured-lookup --judge
```

| 口径 | 1 个 fact 时 (初版) | **2 个 fact 时 (现行)** |
|---|---|---|
| source recall | 100% | 100% |
| fact 子串 | 100% | 50% |
| **fact judge** | **100%** | **75%** |

**分数掉了是尺子变准, 不是回归。** 初版每题只钉 1 个 fact (字母序末位变量), 规则 A 抽检
发现 vic01 的答案写着 "123 variables across **50+ domains**"(另一次跑是 "53") 而**真值 41**
—— 这个可验证的事实错误在 1-fact 判据下**双双满分**。题干问的是"穷举", 只钉一个末位变量
证明不了穷举对不对。加上域数这个第二独立可判定量后, 它当场显形。

逐题:

| 题 | 末位变量 | 域数 | judge |
|---|---|---|---|
| vic01 (C66742) | ✅ `VSLOBXFL` | ❌ 真值 41, 答 "50+" | 0.5 |
| vic02 (C71620) | ✅ `URSTRESU` | 子串未中但语义表达正确 | 1.0 |

> **子串口径对域数这类事实天然不稳** (答案可写 "32 SDTM domains" / "across 32"),
> 故本题集**必须在 `--judge` 下读**, 与 yml 头部声明一致。

**vic01 的失分是真缺陷, 不是判据问题**: 模型能从 chunk 正文读对变量数 (123, 正文里直接写着),
却**不数域而是估**。这属**答题侧**缺陷, 本轮的 KB 数据修复不解决它 —— 见 §5 已知限制 6。

**出题规则 (规则驱动, 非挑例子)**:
> 凡 `N > 15` 的码表, 问"哪些变量引用它", gold fact 取位置 > 15 的条目 (按字母序末位)。

三层防线:
1. 规则作用于 **9 个宽码表全体**, 不是挑一个; 只落 2 道控体量, 其余 7 个由层① 全覆盖。
2. 规则可机械执行 —— 任何人拿它能重新生成同一批题, 不依赖"我知道哪里坏了"。
3. 真护栏是层① 的数据不变量; 题只是端到端佐证。**题与层① 冲突时以层① 为准。**

> `C71620` 与 v3 的 q69 是同一个码表, 但**不是重复题**: q69 的 gold 是 `EX.EXDOSU` (第 15 位,
> 旧正文可见), 本题问的是位置 > 15 的条目 —— 正是旧正文答不出来的那部分。

### 3.4 生产端到端

重启服务 (`launchctl kickstart -k`) 后:
- 启动期预热仍成立且**跟上了新数据**: `s1_vi_section_map entries=171` (= 147 CT + 24 通用变量;
  修首码提取前是 159 = 135 + 24); `ready chunks=4315`
- 冒烟一道宽码表题, 首个引用块 `§三 CT 交叉引用: C66742`, **答案含 `VSLOBXFL`** ——
  该变量在旧语料里**结构上不存在**。

### 3.5 连带闸 (全部实跑, 非推断)

| 闸 | 结果 |
|---|---|
| `scripts/reconcile_meta.py` | 8 项全 OK (含 `TAETORD->43` / `VISITDY->36` / 1917 entries / 1523 vars) |
| `scripts/check_index_freshness.py` | in sync (`f863e45445a6…`) |
| v3 检索闸 140 题 | **98.9286% → 98.9286%, 逐题相同, 变化集为空** —— 两轮重灌 (4303 / 4315 chunks) 后都成立 |
| 全量 pytest | **852 → 859 passed** (+7 = 层① 4 + chunk 层 1 + 外部锚 2) |

> 另有 2 条既有测试因写死 `222` / `135` 而在 §三 变 147 行时红。**没有把数字改成 234/147, 而是
> 改为对 KB 实际行数推导** (`test_variable_index.py::_kb_section_row_counts`) —— 硬编码计数正是
> 本轮反复栽的那类坑, 换个数字只是把下次踩雷推迟。

## 4. 过程中的三件事 (都必须点名)

### 4.1 顺带修好一个既有缺陷 (非本次引入)

重生成时冒出**第四个**文件变化: `knowledge_base/domains/PC/spec.md` 多了一行
`- [Relationships (Ch8)](...) — RELREC, SUPPQUAL usage`。

按计划"若有第四个文件变化, 停下查清"执行, 根因: `generate_cross_references.py` 的
`check_relrec_reference()` 读 `assumptions.md` 判断是否该加该链接; `PC/assumptions.md` 大篇幅讲
RELREC (PC↔PP 关联的四种方法) 故**确实该有**。而已提交的 `PC/spec.md` 生成于 `eb51ca5`
(Phase 6 P0+P1), **早于 06 深审给 `PC/assumptions.md` 补进那些 RELREC 正文**。

即: **生成器是对的, 已提交的 spec 自 06 以来陈旧了。** 爆炸半径就这一个域 (重生成只动了它)。

### 4.2 我自己造了一个判据缺陷并修掉

A/B 初版用 `DOMAIN.VAR` 点号形式做子串匹配, 判 `C71620` **无判别力**。查看原始答案后发现
模型**答对了** —— 它用按域分组的表格作答 (`| UR | URORRESU, URSTRESU |`), 点号形式在这种
答案里永远不出现。

改用**裸变量名** (SDTM 变量名自带域前缀故全局唯一), 并实测确认裸名在截断 context 里同样不存在,
判别力未被削弱。`expected_facts` 同步改。

**这是本项目第 1 条硬规矩的同一个病**: 判据检查工具必须与被检查对象逐字同语义。
上一轮是 lint 与真判据不同语义制造 8 条假阳性, 这一轮是 A/B 判据与答案表达形式不同语义,
把一次正确作答误判成失败。

### 4.3 我把估算值标成了"实测"

早先三处 (spec / checkpoint / **生成器源码注释**) 都写着 "129.6 → 133.8 KB (+4.2 KB) 实测非估算"。
真值是 `134473 → 137000 B = +2527 B ≈ +2.5 KB`。129.6 对不上 VI 任何一个历史版本 —— 因为我把
Python 的**字符数**与生成器打印的 **KiB** 混用, delta 报大 68%。

审查方与抽检方**各自独立**抓到。危害不在 2.5 vs 4.2, 在于其中一处是**生成器源码注释**, 会比两份
md 活得久, 而且标着"实测"。

这是本项目第 2 条硬规矩 ("写实测必须附可复跑的一行命令") 的反面教材: 我附了命令段落, 但**数字不是
从那条命令来的**。规矩要补一句: **标着"实测"的数字必须真的来自那条附上的命令, 且单位要对齐。**

## 5. 已知限制

1. **A/B 隔离的是 context 变量, 证明的是因果, 不等于线上答题必然变好**。真实查询的 context
   组成与本对照不同。
2. **只落 2 道端到端题**; 其余 7 个宽码表靠层① 的数据不变量而非端到端验证 —— 层① 证明的是
   "数据完整", 不是"模型用得上"。
3. **重灌改变全库 embedding**, v3 逐题 Δ0 是**实测**非推断 (两份 report 工件均在
   `evidence/checkpoints/`, 可从文件复算)。
4. **`VS.VSLOBXFL` / `UR.URSTRESU` 这类"字母序末位"是本轮的 gold 选法**, 不代表它们在业务上
   比中间位置的条目更重要; 选末位只为最大化与旧截断边界的距离。
5. **域 spec 交叉引用段只有 AE / LB 两个文件命中**, 样本太少, 无法评估该处修复的普遍收益。
6. **⚠️ 新浮现的答题侧缺陷 (本轮不修, 建议下一个单元)**: 宽码表问句下, 模型能从正文读对
   **变量数** (123, 正文直接写着) 却**估而不数域数** —— vic01 答 "50+ domains"/"53"(两次跑),
   真值 41。属答题侧, KB 数据修复不解决。当前 `vic01` 在 judge 口径下**故意保留失分**
   (0.5), 它是这个缺陷的常驻探针; **修好之前不要把它调绿**。
7. **`server/rag.py::format_context` 有 4000 字符截断** (`c.text[:4000]`), 与本轮同一失败
   模式的下游且**无任何断言**。§三 当前最长 1546 字符 (C66742), 余量 2.6x, **无现网问题**;
   但审查方实测索引里已有 **619 个 chunk 超 4000** (最长 78886, PK Parameters)。属既有问题,
   不在本轮范围, 入档备查。
8. **层① 的外部锚参照的是 `domains/*/spec.md`, 它是生成器的输入** —— 证明"输入→输出忠实",
   不证明"输入本身对"。输入正确性由规则 A 抽检用 `source/cdisc/*.xlsx` 独立重算覆盖 (§6),
   那条不是 CI 常驻。
9. **chunk 层断言在无索引的机器上 `pytest.skip`** —— 唯一的 chunk 层护栏会无声消失。本机确实
   跑了 (859 passed 无 skipped), 但 clone 出来的环境不会。审查方建议加 `KB_GATE_STRICT=1`
   开关把 skip 变 fail, 本轮未做。

## 6. 三方隔离 (规则 D)

| 角色 | 承担 | 裁定 |
|---|---|---|
| 实现 | 主 session | — |
| 审查 | `oh-my-claudecode:code-reviewer` (opus) | **REVISE** (2 HIGH / 4 MEDIUM / 4 LOW) |
| 抽检/验收 (规则 A, 抽样总体 = 9 个被截 CT 行 + 2 个域 spec 段) | `oh-my-claudecode:scientist` (opus) | **PASS** (数据正确性) + 4 项须入档 |

### 6.1 抽检方: 数据正确性用**外部源**逐条验证

抽检方拒绝用 spec.md (那是生成器的输入, 等于用输入验证输出), 改用
**`source/cdisc/SDTMIG_v3.4.xlsx` 的 `Variables` sheet** —— 与生成器无共享代码、无共享中间产物。

| 检查 | 覆盖 | 结果 |
|---|---|---|
| CT → 变量集合 双向差集 | **全部 135 码表** (要求 N≥5) | `codes with any diff: 0` |
| 变量级 CT 单元格逐字对照 | **1917 / 1917 变量** | `verbatim mismatches: 0` |
| 9 个被截码表三方数字 (KB 声称 / KB 实列 / xlsx 独算) | 9/9 | 全等, 双向差集空 |
| "没有多补" 抽样 | 26 条新增 (seed=7) | 26/26 OK |
| chunk 层 | 全部 135 | `problems: NONE`, 每码表 1 chunk 未被切碎 |
| AE / LB 整段 (不只 C66742) | 8 + 18 个码表 | 双向差集空, 顺序一致 |
| "隐藏 10 条" 独立复算 | 全 63 域扫描 | `len>5` 的 (域,码表) 对**恰好 2 个**, 8+2=10 ✓ |
| PC 连带修复的爆炸半径 | 全 63 域按生成器**精确**谓词扫 | 规则与现状零不一致, "就这一个域"成立 |
| 生成器幂等 | 重生成到 /tmp | **byte-identical** |

**局限 (抽检方自陈)**: 该路径证明 `xlsx → spec.md → §三 → chunk` 全链忠实, **不证明 xlsx 对 PDF
忠实** —— 那属 06 深审范围。

### 6.2 三方各自抓到了对方看不见的东西

| 来源 | 独有发现 |
|---|---|
| 审查方 | 层① **自洽即通过** (构造伪造 KB 实证 5 条断言全绿而 226 条静默消失); 域 spec 侧只有 marker 断言比 VI 侧弱; `.pyc` 入库; chunk 总数当证据是恒等式非观测 |
| 抽检方 | **vic01 答案 "53 domains" 而真值 41** —— 1-fact 判据视野外的事实错误; 用 xlsx 外部源证明补回的 226 条是**对的**而不只是"变多了" |
| 两方独立收敛 | **12 个码表整行缺失** (首码提取); **体积 +4.2 KB 是错的** (真值 +2.5 KB) |

实现方自查全绿, 三条真缺陷 (首码提取 / 自洽护栏 / 假实测数字) **一条都没自己发现**。

## 7. 复跑

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_kb_crossref_completeness.py -q   # 5 passed
.venv/bin/python -m eval.vi_completeness_ab                                    # 两题判别力成立
.venv/bin/python eval/run_eval.py eval/test_set_vi_completeness.yml \
    --hybrid --structured-lookup --judge                                       # fact 100%
.venv/bin/python scripts/reconcile_meta.py                                     # 8 项全 OK
.venv/bin/python scripts/check_index_freshness.py                              # in sync
.venv/bin/python -m pytest -p no:warnings 2>&1 | tail -1                       # 859 passed
```

v3 逐题 Δ0 从工件复算 (不必重跑):

```bash
cd sdtm-rag && .venv/bin/python - <<'PY'
import json
load = lambda p: {x["id"]: x["source_recall"]
                  for x in (lambda d: d["results"] if isinstance(d, dict) else d)(json.load(open(p)))}
a = load("evidence/checkpoints/s1_vi_after.json")
b = load("evidence/checkpoints/vi_trunc_v3_after.json")
diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
print("逐题相同:", not diff, "| 变化:", diff)
PY
# 逐题相同: True | 变化: {}
```
