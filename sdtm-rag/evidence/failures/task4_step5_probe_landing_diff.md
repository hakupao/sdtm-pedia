# Task 4 Step 5 — 落库版 vs scratchpad 版探针的逐题差异 (规则 B 归档, 不删)

brief Step 5 的期望是"**逐值相同**" (gold 不参与本探针任何计算, 故 Task 1/3 改 gold 不应
影响任何数字)。实测**聚合全部逐值相同**, 但逐题比对发现 1 处标签差异 + 2 题成分变化。
本文件记录差异、根因判定, 以及为什么它**不**推翻 spec §0。

## 输入

- 旧: scratchpad 版探针 (`.superpowers/sdd/.../artifact-crowding_probe.py`) 的输出
  `<scratchpad>/crowding_layer1.json` (2026-08-07 11:26, Task 1/3 改 gold 之前跑的)
- 新: 落库版 `.venv/bin/python -m eval.crowding_probe --output evidence/checkpoints/crowding_layer1.json`

## 产物 / 技术判定

聚合 (spec §0 那 6 个数) **逐值相同**: ≥3 席 40 题 28.6% · ≥5 席 11 题 7.9% · ≥8 席 3 题 2.1% ·
平均 dup_seats 1.73 · 平均 distinct_sections 13.27 · 榜首 q38 max=14 §DOMAIN。

逐题 (140 题 × `dup_seats`/`max_cluster`/`max_cluster_section`/`distinct_sections`/`n`/`category`):

- **不同的只有 1 处**: q120 的 `max_cluster_section`, `whole_file` → `item_1`。
  三个集合统计 `(max_cluster, dup_seats, distinct_sections) = (2, 1, 14)` **两版相同**。
- `composition` 逐位比对: **2 题**变了 (q38, q120)。
  - q38: 出 `domains/{OE,TU}/spec.md` 入 `domains/{TE,TR}/spec.md` —— **section 多重集完全相同**
    (全是 `DOMAIN`)。这正是 topk_jitter.md §5.6 说的"换人不换 section", 现场再验一次。
  - q120: 出 `chapters/ch01_introduction.md#whole_file` 入 `domains/RELSUB/assumptions.md#item_1`
    —— **churn 跨出了 section 名**, 于是簇头标签从 `whole_file` 翻成 `item_1`。
- `sim` 漂移 (排除上面 2 题, 按 (source, section) 配对): 138 题里 **281 个条目**漂了,
  **max |Δ| = 0.0020**; 其中 **BM25 量纲 (sim>1) 的条目一条没漂**。与 Task 3 的实证同形
  (漂移源在 embedding 侧)。

## 业务判定

**不是口径改动, 不订正 spec §0。** 三条依据:

1. 差异形态与 gold 无关 (gold 不进任何计算), 与 Task 1/3 的改动也无关。
2. 差异形态**恰好等于** Task 3B 已量化的 top-15 抖动: q120 正是 3B 两种模式都报过成分变化的
   5 题之一, q38 亦然。落库版这次跑到的 q38 成分 (含 TE 与 TR) 与评审当初的 run2 同型。
3. 落库版自己的跨进程验稳 (16 题 × 20 进程, `crowding_layer1_stability.json`) 里,
   q120 见到 2 种成分但统计取值恒为 `(2,1,14)` —— 与两版单次快照都一致。

**但暴露了一个此前没写下来的缺陷**: `max_cluster_section` 在并列时由 `Counter.most_common(1)`
的插入顺序决定, 而插入顺序 = top-k **排位** —— 排位不可复现。实测 140 题里 **71 题**最大簇存在
并列, 其中 **49 题** `max_cluster == 1` (压根没有簇, 那个 section 名纯属排位产物)。
已处理: 跨进程分布的取值键**不含**该字段 (`_STAT_KEYS`), 并在
`evidence/checkpoints/crowding_layer1.md` §4 与模块 docstring 里写明使用禁忌。
q120 这次的翻转**不是**并列造成的 (两版都无并列), 是真成分变化; 但两件事共同说明:
**簇头的 section 名不是稳定事实, 只有簇的大小是。**

## 追加 (fix round 1): q120 又翻回去了 —— 第三个样本

为加 `max_cluster_section_tied` 字段而重跑 140 题 (同一命令), 逐题再比一次:
**唯一差异仍是 q120 的 `max_cluster_section`, 且这次翻回了 `whole_file`**。
三次单次快照的簇头名: `whole_file` (scratchpad) → `item_1` (首次落库) → `whole_file` (重跑),
三次的 `(max_cluster, dup_seats, distinct_sections)` 恒为 `(2,1,14)`, 与 20 进程跨进程分布一致。

**要点**: q120 的 `max_cluster_section_tied` **三次都是 false** —— 它的不稳定**不是并列造成的**,
所以新加的标记**照不出它**。故标记的语义必须写准: `tied=false` = "不是并列打破出来的",
**不等于"稳定"**。要判稳定性只能看跨进程分布。已写进 `crowding_layer1.md` §4 禁忌 2。

## 下一 attempt 的输入

- 引用层① 逐题数字时, 只引 `max_cluster` (含 §5.6 豁免条件); `dup_seats`/`distinct_sections`
  的逐题值对 q47 必须按分布报, q117 需标注; `max_cluster_section` 只在 `max_cluster ≥2`
  且无并列时可引。
- Task 6 去重 / Task 8 重灌索引之后, §5.6 豁免前提消失, **层① 全表必须重跑**,
  且重跑时应当再做一次本文件这种"逐题 + composition"比对, 而不是只比聚合 ——
  这次的 q120 就是只比聚合会漏掉的那一类。
