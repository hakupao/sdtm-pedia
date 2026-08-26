# 交接 — study 轨 workflow 事件层 (2026-08-26)

> 分支 `feat/study-workflow-events` · **25 commit · 未合并 · 测试 1780 全绿**
> 上一 session 用 SDD (6 Task × 规则 D 三方) 执行完毕, 最终整分支审查判 **有条件合并且条件已全部满足**。

## 0. ⛔ 唯一阻塞项: 合并决策未做

分支停在这里等你选。`main` 自分叉后未前进 (merge-base = main HEAD), 合并会是 fast-forward。

1. 本地合并回 `main`
2. 推送并开 PR
3. 保持现状

**在做这个决定之前不要开新工作** —— 后面 4 个候选单元都建立在这条分支上。

## 1. 这个分支交付了什么 (最终审查原话摘录)

1. **一处已在线上生效的生产缺陷修复**: 卡片标签 `適用範囲` → `非表示アクティビティ`,
   语义**相反**的错误, 231 张卡, 已重灌索引落到 localhost:8000。
   **它是 S3 退回后唯一存活的用户可见改动** (归因 A 臂实证逐题 Δ0 无责)。
2. **ConfigReport 三个从未被任何管线解析的 sheet 进 catalog** (`events` 14 / `activities` 77 /
   `assignments` 110), **带三道互证闸** —— 闸 A 四数来自 PDF 封面摘要 (独立来源非自证),
   闸 C 是 xlsx 内两处独立表示的转置互证。
   *「这不是"解析跑通了", 是"解析对不对有独立参照物" —— 本仓大多数解析工作没有这个。」*
3. **确定性推导 `collect_scope`** (form 分配 − item 隐藏清单), 并有**独立于尺子**的佐证:
   231/231 减法非平凡、**"有 hidden 但活动不在该 form 分配里 = 0"** (从数据自身一致性导出)。
4. **33 题 event 侧 gold** + lint 闸 + 白送分闸, 且经历了"发现尺子本身瞎了 → 收紧 → 重测"。
5. **`resolve_events` 事件查询通道**: 33 题 **21/33 = 63.64% (source-recall 口径)**。

## 2. 必须知道的三条边界 (否则会误读)

- **`resolve_events` 零生产调用方** —— 没有任何请求路径调它。所以下面那个 10.81% 当前**零害**。
- **全局 precision 仅 10.81%** (259 返回 / 28 与 gold 有交集); 12 个未命中题返回 157 条纯噪声。
  **接线前必须先定 precision 门槛并复测**, 否则 union-add 会把噪声灌进检索 (与 S3 同一教训)。
- **这个通道是 lookup 不是 retriever**: 能"给标识符 → 找记录"(`oid_name_mapping` 6/6 ·
  `item_collection_scope` 5/5 · `repeating_rule` 5/5), 不能"给描述 → 推断"。

## 3. 下一步的 4 个候选 (最终审查建议, 均**不属于**本分支)

| # | 单元 | 前置 | 一句话 |
|---|---|---|---|
| **C4** | **生产接线** (union-add 进检索) | **C3** | 这条通道真正产生用户可见价值的唯一路径。需要: 定接入点 + 定 precision 门槛 + 建卡片侧不回归闸 (S3 的教训) + 跑 study golden v2 |
| **C3** | precision 取舍单元 | 无 | "逐条相减"替代"整 form 让位" + 名称→assignment 入口。这两条是**同一个 precision 取舍的两半**, 应合成一个**带数据判据**的单元, 而不是各自反射性补齐 |
| **C2** | 红线闸接自动化 | 无 | `sdtm-rag/scripts/oidscan_evidence.py` 工程质量够 (19 单测/fail-closed/路径掩码/精确 allowlist) 但**只能靠人记得手跑**。本仓教训: 纸面规则等于没规则 |
| **C1** | 红线清理既有命中面 | 无 | `test_ja_tokenize.py` 等 6-7 个文件有真实 OID/label (**早于本轮数月**, 新 label 池才照出来)。需逐条判真假阳性 |

## 4. 我的建议

**先做合并决策, 然后 C2, 然后把 C3+C4 当一个单元。**

但在开 C4 之前, 有个更根本的问题值得先问: **这条通道值不值得接线?**
- 21/33 是**自己出的尺子**上的成绩; precision 10.81%
- 它能答的那三类 (给 OID 找记录 / 采集范围 / 重复规则) **有没有人真的会问**, 至今**没有外部证据**
- `sdtm-rag/dogfood_failures.md` (⚑ 真实使用失败捕获) **至今仍不存在, 一条都没捕获过**

⇒ 如果同事测试能跑起来、攒出真实提问, 那批数据既能回答"值不值得接线", 也是 U6 判库欠账
唯一不破封存纪律的新标定源。**这件事的优先级可能高于 C1-C4 任何一个。**

## 5. 关键留痕 (全在版本库, 不随 workspace 消失)

| 文件 | 内容 |
|---|---|
| `sdtm-rag/evidence/checkpoints/study_workflow_events.md` | 收口证据 (各闸实测 / 逐题未命中 / 已知限制) |
| `sdtm-rag/evidence/step_workflow_events_final_review.md` | **最终整分支审查** (含 C1-C4 与 deferred 逐条 triage) |
| `sdtm-rag/evidence/step_workflow_events_audit{,_review,_review_r2}.md` | 规则 D 三方核验 |
| `sdtm-rag/evidence/failures/t4_step7_retrieval_regression.md` | **S3 触发全过程** (三臂归因实验; "关系型数据进向量库会挤占"的第二个实证) |
| `sdtm-rag/evidence/failures/task5_s4_v1_human_judgment_rejected.md` | 被打回的首版 S4 判定 (规则 B) |
| `docs/superpowers/{specs,plans}/2026-08-25-study-workflow-events*` | spec / plan (plan 顶部有"设计基准以 checkpoint §2 为准"的指针) |

⚠ **控制方 ledger (65 条裁定) 在 `.superpowers/sdd/2026-08-25-study-workflow-events/progress.md`,
该目录 gitignored**。要留就现在拷出来。

## 6. 上一 session 控制方犯过、已记账的错 (供新 session 避坑)

1. **裁定记进 ledger 却没派发** —— 开工前预见到的问题 (Ruling P2) 没写进派工消息, 结果 10 题全灭
   并被误记为"结构性限制"; 靠规则 D 两方各自独立推翻才捞回来
2. **红线扫描有结构性盲区** —— 对照当前产物而非**源**, 于是"尚未解析进产物的那部分源"天然不可见
3. **基于部分阅读派工** (405 行报告读了 265 行)
4. **转述数字不带口径** (一个 "10/12" 实为定义差异, 另一口径下是 6/12)
5. **17 个真实 OID 一度进 git** (根因是控制方要求把 top15 对比写进失败归档) —— 已改写历史清除
