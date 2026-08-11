# doc 轨 kickoff — study 文档型 chunk 的尺子与接线

> 建立: 2026-08-11 (C1 收口当日) · 路由词: **「doc 轨 开始任务」**
> 前置: C1 DONE (`sdtm-rag/evidence/checkpoints/study_c1_doc_sections.md`)
> 数据红线: 一切进 git 的内容零真名零正文, 研究一律代号 `st01` (同 C1 Global Constraint 1)

## 0. 现状一句话

st01 的 113 页文档已切成 **114 个章节 chunk**, 入了**独立 collection `study_st01_docs`**,
逐字保真已被独立抽检确认 (N=9 + 全集 114)。**但它检索不到** —— 没有任何检索路径读那个
collection。field card 侧 `study_st01` = 959 张, study golden v2 **87.50%, 与基线逐题 Δ0**。

## 1. 本单元的顺序是硬的: 尺子先于接线

**不许先接线**。理由 (这个仓已经吃过两次同样的亏, 见 §4):

- 现有 48 题 study golden v2 **全是 field card 题, 对 doc chunk 零判别力** —— 先接线的话,
  接完也说不出"好了没有"。
- 分库只解决了**检索侧**挤占。**答题侧 context 席位挤占是同一个坑, 还没碰** —— 长篇章节
  进了 prompt 会挤掉卡片, 没有 doc 侧尺子时这件事**看不见**。
- 判据必须**先于**数据写死 (硬规矩: 见 `cap_recall_sweep.md` 的做法), 含自毁条款。

## 2. 工作单元 (按依赖顺序, 不要跳)

### U1 doc 侧题集 (先做, 属设计单元 ⇒ 先 brainstorm)

产出: doc 侧 gold 题集 + 可执行判据闸。要在动手前定死的口径:

1. **判据粒度**: chunk 文件名? `section_number`? 页区间? —— C1 的 `provenance` 是
   `doc01#p63-70[#part2of3]`, 天然支持"节 + 页 + 份"三级, 选哪级要写理由。
2. **gold 唯一性**: 抄 study 轨已有的两把闸 (`eval/lint_gold.py` 的 AND/OR 双侧唯一性 +
   端到端"只有 gold 能得分"), **不要**重新发明。注意 `lint_gold.py` 现在只作用于 study 轨
   catalog, 对 doc chunk 需要扩展或另写。
3. **⚠ L1 覆盖缺口要在写题时逐题裁定**: 首锚点之前 **66,200 字符 = 全文 27.42%** 不属于
   任何 chunk (目录 49,320 排除合理; **卷首 + 第 1 章约 16,880 字符是实体内容**)。
   凡是答案落在未覆盖区的题, **当场标注"接线也答不出"**, 不要混进计分池 —— 否则会把一个
   覆盖决策伪装成检索失败。这一步的产物就是 §3 那个"要不要给卷首做 chunk 型"的决策依据。
4. **样本量与题型配比**: 至少覆盖 —— 单节可答 / 跨节需聚合 / 被 `part` 切开的节 (2 个家族)
   / 表格类 (L6 的 2 处疑似被切断的表格正好做探针)。
5. **fact gold 不要再写 1-2 词碎片** —— 这个仓已确认那类 gold 会让 fact-recall 顶格失去
   分辨力 (`llm_judge_fact_recall.md`, 121/140 顶格)。

### U2 接线 (U1 有尺子之后)

选项 (要在 U1 的题集上比, 不要凭直觉选):
- (a) 联邦加**第三引擎** (cdisc / study-cards / study-docs), 走既有 `server/federation.py` 判库;
- (b) study 引擎内部**显式通道** (类似 S2 那样的 union-add, 但按 file_type 分池取席);
- (c) 同库 + per-file_type 配额 —— **C1 已实测同库直接混 = 87.50% → 78.1%**, 若走这条必须
  先证明配额能挡住那 6 题的回归, 且要记住"配额安全 ≠ 配额有收益"的旧账。

**接线后的硬验收 (缺一不可)**:
1. field card 侧 48 题 **逐题 Δ0** (与 `runs/v2_baseline_s2on.json` 比, 87.50%);
2. doc 侧题集有可复现的基线数字, 且**判别力被证明** (反事实: 关掉 doc 通道该掉分);
3. 答题侧 (非 retrieval-only) 至少一组: doc chunk 进 context 后**卡片题答案没变差** ——
   这是分库没覆盖的那半个坑。

### U3 C2 (另两份表单版面 PDF)

933 页 / 212 页, 短行占比 83%/80% = 表单版面, C1 已明确移交。**排在 U2 之后** —— 接线前
入库只是把不可检索的库做大一倍。走页级粗切 (spec `docs/superpowers/specs/2026-07-31-study-rag-design.md` §2)。

### U4 L6 表格切点约束 (最后)

3 个 `part` 切点里 2 个疑似切断表格 (`8.2` 2→3、`22.1` 1→2, 两侧均多列形态)。
**等 U1 的表格类题能测出"表格被切是否真伤答案"再动** —— 否则又是一次没判据的修法。

## 3. 明确悬着的决策 (需要用户裁定, 不要替他定)

- **L1**: 卷首 + 第 1 章约 16,880 字符要不要成 chunk? 需要新 chunk 型 (无编号锚点)。
  建议在 U1 逐题裁定完之后再问 —— 那时能给出"多少题因此答不出"的数字。

## 4. 硬规矩 (本轮新增/复发的, 必守)

- **17. 「派了审查」≠「审过了」** —— C1 里抽检报告落了盘但**返回摘要没回传**, 实现方读盘
  自救。派 agent 时要求**边做边落盘**; 拿不到报告就当那一环没发生并在证据里点名。
- **17b (C1 新增). 核验方自己也会算错** —— C1 实现方复核抽检数字时把未覆盖量算成 66,086,
  错在"按文件名排序当成文档顺序"+"frontmatter 切分每文件多留一个换行"。
  **凡是关键数字, 用非自洽写法复算一遍** (C1 的做法: 直接断言 `allbody == full[66200:]`)。
- **18. 新加的取证信号当场补断言**, 否则它是装饰。
- **19 (C1 新增). 有损轨的完备性闸要写清它的口径边界** —— C1 的完备闸只管"首锚点之后",
  对 27.42% 的未覆盖**天然免疫**。闸绿不等于内容都在。**引用任何闸的绿灯时必须同时写它看不见什么。**
- **并发隔离**: 抽检进行中不要改产物目录 (C1 犯过, 靠 sha256 事后补证)。

## 5. 开工自检命令

```bash
cd sdtm-rag
.venv/bin/python -m pytest -p no:warnings                     # → 1036 passed
.venv/bin/python -c "
import chromadb; cl = chromadb.PersistentClient(path='data/chroma')
print({c.name: c.count() for c in cl.list_collections()})"    # → sdtm_kb_v1 4329 / study_st01 959 / study_st01_docs 114
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards --output /tmp/chk.json   # → 87.5%
```
三条对不上就先查环境, 不要在错的基线上开工。
