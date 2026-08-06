# S1 对 VARIABLE_INDEX 按字面定位 section — 设计

> 建立: 2026-08-07
> 来源: `sdtm-rag/evidence/checkpoints/cdisc_gold_section_granularity.md` §6.1 (section 化暴露的真缺陷)
> 路由: `milestones/07_rag_kg/NEXT_ROUND_KICKOFF.md` §2.D2
> 状态: 设计已认可, 待实施

## 1. 问题

`VARIABLE_INDEX.md` 在索引里有 222 个 chunk, 分三族互不相关的内容:

| 族 | section 形态 | chunk 数 |
|---|---|---|
| 通用变量 | `§一 通用变量: <VAR>` | 24 |
| 域变量表 | `<CODE> — <名称> (<class>)` | 63 |
| CT 交叉引用 | `§三 CT 交叉引用: C<code>` | 135 |

S1 (`StructuredLookup`) 把 18 道题确定性地解析到这个文件, 但**文件内选哪一块靠 cosine**
(`RAGEngine._lookup_chunks_for_file`)。VI 的 chunk 是极短结构化单行
(`CT Code C99073 — controlled terminology codelist referenced by 17 variable(s): …`),
对自然语言问句的 embedding 相似度近似噪声, 于是**文件内选块基本随机**。

section 级判据落地后这条缺陷显形: 18 题子集 100.00% → **75.00%**
(4 道完全打偏 q108/q109/q110/q112 + 1 道半命中 q107), CDISC 全集 **95.71%**。

**要的块一直在索引里, 只是 cosine 选不中。** 已实测:

```bash
cd sdtm-rag && .venv/bin/python - <<'PY'
import chromadb
c = chromadb.PersistentClient(path="data/chroma").get_collection("sdtm_kb_v1")
vi = next(m["source"] for m in c.get(include=["metadatas"])["metadatas"]
          if m.get("source", "").endswith("VARIABLE_INDEX.md"))
g = c.get(where={"$and": [{"source": {"$eq": vi}},
                          {"section": {"$eq": "§三 CT 交叉引用: C99073"}}]},
          include=["documents"])
print(len(g["ids"]), g["documents"][0][:80])
PY
# -> 1  CT Code C99073 — controlled terminology codelist referenced by 17 variable(s): CV.CVLAT, …
```

即 section 名在 Chroma 元数据里、可 `$and` 精确过滤、命中唯一一块, 且该块正文正是 q109 的 gold 内容。

## 2. 方案

题面已经点名了 CT 码 / 变量名。**用字面锚点定位 section, 不让 embedding 猜。**

### 2.1 锚点 → section 的映射从索引反建 (不拼格式串)

不写 `f"§三 CT 交叉引用: {code}"`。改为启动时读一次 VI 的全部 chunk 元数据, 用 section 尾部
token 反解, 建两张表: `ct_code -> section`、`variable -> section`。

理由是本轮第 1 条硬规矩的同一个病 (`NEXT_ROUND_KICKOFF.md` §3.1): **拼字符串等于让检查方与
被检查方各写一份格式定义, 早晚不同步**。lint 与真实判据不同语义已经制造过 8 条假阳性。
这里若 chunker 改了 section 命名, 拼串方案会**静默全 miss 并回落 cosine** —— 分数悄悄退回今天,
任何闸都拦不住 (偏差方向朝下但无声)。从索引反建则只有一份事实来源; 表建不出来就响亮失败。

代价: engine 生命周期内一次 `collection.get(where={"source": VI})` (222 行), 懒加载并缓存。

### 2.2 通道形状

- `StructuredLookup` 新增 `variable_index_anchors(query) -> list[str]`:
  复用既有 `_QUERY_CT_RE` (CT 码) 与 `_query_variables` (已知变量名) 抽锚点, 去重、保序,
  **上限 3** (与既有 `_MAX_DOMAIN_SPECS` 同值; top_k=15 下不挤压 cosine 名额)。
  返回的是**锚点 token**, 不是 section 串 —— 格式知识只存在于 RAGEngine 侧的反建映射里。
- `RAGEngine._apply_structured_lookup`: target 为 `VARIABLE_INDEX.md` 时走新路径 ——
  每个锚点查其 section, 用 `{"$and": [source, section]}` 精确取 1 块, **复用已算好的
  query embedding, 零新增 embedding round-trip**。其余 target 逐字节走原逻辑。
- 覆盖 §一 + §三 两族。域变量表 (63) 不做: 域码问题已由 `domains/<CODE>/spec.md` 通道承接,
  VI 内域表无题引用, 铺开只会与现有域通道重叠、浪费 top-k 名额。

### 2.3 回落 (新通道只能赢不能输)

- 锚点解析不出 → 回落今天的文件内 cosine 选块。
- 锚点解出但索引里无该 section → 跳过该锚点; 全部锚点都落空则回落 cosine。
- 映射表为空 (VI 一个 chunk 都没读到) → fail-loud, 因为这意味着索引/命名约定已崩, 静默降级
  会把"检索退化"伪装成"没有回归"。

## 3. 预期效果与回归面

- q108 / q109 / q110 / q112: 假命中 → 真命中 (0.00 → 1.00)。
- q107 (ARM + ARMCD 两节): 0.50 → 1.00。这道题的失分根因是"1 个文件只注入 1 块", 多锚点注入
  同时解除了这条限制。
- CDISC 全集 section 级判据 **95.71% → 预期 98.57%**。

> **数字口径**: 本轮的上限**不是 100%**。18 题子集上限才是 100%; 全集 140 题另有 q38
> (chapters 整文件单块, kickoff §2.A) 与 q126 (已归档 permanent known limit) 两道既有 miss,
> **不在本轮范围**, 合计封顶 -1.43pt。故验收看两个数: **18 题子集 75.00% → 100.00%** +
> 全集配对 diff 中 **其余 122 题逐位 Δ0**。

- **回归面 (必须逐题验证, 不接受"总分没掉"作为证据)**: 另外 13 道 VI 题今天靠 cosine 恰好选对,
  改后走字面通道。要逐题确认注入的 section 仍是该题 gold, 而非总分抵消。

## 4. 测试与验收

TDD 单测:
- 锚点抽取: 纯 CT 码 / 纯变量 / 混合 / 无锚点 / 重复去重 / 超上限截断。
- 映射反建: 从桩元数据建表; 域变量表 section 不进表; 表为空时 fail-loud。
- 回落: 索引缺该 section → 跳过; 全落空 → 与今天的 cosine 路径**逐字节同结果**。
- 非 VI target 不受影响。

闸:
```bash
cd sdtm-rag
.venv/bin/python -m pytest -q
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml \
    --retrieval-only --hybrid --structured-lookup      # 95.71% -> ?
```
配对 diff 报 18 题子集逐题 recall + 其余 122 题 Δ。

流程闸 (承接本轮硬规矩):
- **规则 D 三方隔离**: 实现 / 审查 / 抽检各用不同 `subagent_type`, 不自审。
- **规则 A 抽样总体 = 本轮实际变更集合 (18 题)**, 不是 140 题全集。
- 写"实测"必须附可复跑的一行命令。

## 5. 不做

- 域变量表族 (63 chunk) 的字面定位 —— 见 §2.2。
- 铺到 VI 以外的大文件 —— `cdisc_gold_section_granularity.md` §5 已实证 ch04 / 域 spec 的
  cosine 选块是健康的, 对它们做同类改动是负收益。
- q38 chunk 构造 (kickoff §2.A)、联邦答题 eval (§2.B) —— 独立单元, 另行排期。
