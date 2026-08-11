# doc 轨 U1 — st01 doc chunk 侧 gold 题集与判据 设计

> 日期: 2026-08-11 · 单元: doc 轨 U1 (kickoff `milestones/07_rag_kg/DOC_TRACK_KICKOFF.md` §2 U1)
> 前置: C1 DONE (`sdtm-rag/evidence/checkpoints/study_c1_doc_sections.md`)
> 后继: U2 检索接线 (本 spec **不涉及**接线方式的选择)
> 数据红线: 本文件进 git, 只含数字 / 编号 / 文件名 / 形态描述, **零真名零正文**
> (chunk 文件名的非识别性已由 C1 抽检的第三条硬判据确认)

## 1. 问题

C1 把 st01 那份 113 页文档切成 114 个 chunk 入了独立 collection `study_st01_docs`,
逐字保真已被独立抽检确认 —— **但没有任何检索路径读它**。

接线之前缺一把尺子: 现有 48 题 study golden v2 **全是 field card 题, 对 doc chunk 零判别力**。
不先有 doc 侧题集, 接完线也说不出"好了没有"。

**本单元只产出尺子, 不接线。**

## 2. 目标与非目标

**目标**

- 30 道计分题的 doc 侧 gold 题集, 四道**程序化入池闸**, 判定规则先于数据写死
- 一个可复现的 **doc-only 上界基线**数字 (直接打 `study_st01_docs`)
- 规则 A 独立抽检 (N=8) 过判

**非目标 (YAGNI, 明确不做)**

| 不做 | 理由 |
|---|---|
| 检索接线 (联邦第三引擎 / 显式通道 / 同库配额) | U2 的事; 本单元连选项都不比 |
| 答题侧 A/B 实测 | B 臂 (doc chunk 进 context) **需接线才存在**, U1 跑不了 |
| 改动 `test_set_study_v2.yml` | 87.50% 那把尺子必须保持逐题可比 |
| L1 覆盖决策 (卷首+第 1 章要不要成 chunk) | 本单元只产出**数字依据**, 裁定权在用户 |
| L6 切点修改 / C2 (另两份 PDF) | 分别闸在 U1、U2 之后 |

**但 fact gold 现在就写** —— 边际成本低; 事后补会有"照着结果写 gold"的嫌疑。

## 3. 判据粒度: chunk 文件名

gold 写 chunk 文件名 (形如 `st01__doc01__s10_1.md`), 判据**逐字复用现有
`check_source_recall`, 一行不改**。doc chunk 的 `source` 元数据实测就是文件名, 与 field card 同形。

C1 的 `provenance` 天然支持"节 / 页 / 份"三级, 选文件名的理由:

| 粒度 | 判定 |
|---|---|
| `section_number` | 对 `8.2` (3 份) / `22.1` (2 份) **一对多** —— 恰好在最该有判别力的 part 题上失去判别力 |
| 页区间 | 114 个 chunk 里 **57 个跨页**, 一个页区间对多个 chunk, 天然多匹配 |
| **chunk 文件名** ✅ | 与 `section + part` **一一映射**; **实测 114 个文件名零子串碰撞** (枚举全部 114×113 有序对, 结果空); 与卡片侧同形 ⇒ 判据机器零改动 |

零子串碰撞 ⇒ **不需要 `gold_max_matches`**, 30 题里不存在结构性白送。

选同形还有一条防御性理由: v2 出过一次 "lint 与被检查的判据不同语义 → 8 条假阳性 → 为迁就假阳性
删掉合法 gold" 的连锁误判。复用同一判据实现是最省的防法。

## 4. 出题与四道入池闸

四道闸**全部程序化、全部先于数据写死**。过不了闸的题不进计分池。

### 闸 1 — 来源隔离

出题只读 `pdftotext -layout` 逐页原文, **不读 `docs/` 下的 chunk 产物**。
定 gold 时才把答案落点映射到文件名。

防的是"照着切分边界出题" —— 那会让题集与切分器共谋, 测不出切分是否合理。

### 闸 2 — 卡片答不出 (用户裁定的入池条件)

题的答案落点必须在 `catalog.json` 的 959 张卡的 label / OID 上**字面找不到**。

理由: C2 的价值假设正是被"相对 959 张卡的增量是什么"打死的。同一问对 C1 同样成立 ——
若 doc 题卡片也能答, 那测的不是"文档有没有用", 而只是"文档有没有把卡片挤掉"。

执行: 全量走确定性字面筛; 另抽 **N=6** 题走**实测**复核 (在卡片库 `study_st01` 上跑检索 + 答题,
确认答不出) —— 确定性筛判的是"我认为语义等价", 有主观性, 必须有实测样本兜底。
这 6 题按题型分层抽 (单节 2 / 跨节 2 / part 1 / 表格 1), 不是随手取前 6。

### 闸 3 — 锚串唯一性 (零 LLM)

每题附一条**答案锚串** (**≥ 20 字符**, 防短串碰巧命中); 该串必须**落在该题的 gold chunk 里,
且不溢出到任何非 gold chunk**。无 gold 的题直接报 (锚串无从校验)。

> **口径修订 (2026-08-11, Task 2 复审实测逼出)**: 本条初版写的是「出现次数 == gold 数」,
> **那是错的**, 四条 fail-open 已实测复现:
> ① OR-only 题 (`expected_sources_any`) 与 ② 漏写 gold 的题 → `gold 数 = 0`, 捏造的锚串
> `出现 0 次 == 0` **判绿**, 而"锚串不在语料里"正是这道闸存在的唯一理由;
> ③ `gold=['a.md']` 但锚串只在 `b.md` → `1 == 1` **判绿** —— gold 与锚串指向两个不同
> chunk, 自相矛盾却合格;
> ④ `gold=['a.md','c.md']` 而锚串在 `a.md`/`b.md` → `2 == 2` **判绿**。
> 改为 membership 校验后, 数量不等必然导致 missing 或 extra 非空, 故**严格强于**原口径。
> gold → chunk 的解析必须复用 `lint_gold` 的匹配实现 (与闸 A 同一语义, 不许第二份)。

它把两件事同时变成可执行闸:

- gold 是不是**真的唯一能答** (而不是"我以为它唯一")
- 题是不是太泛 (好几个 chunk 都能答 ⇒ 出现次数 > gold 数, 当场红)

做法沿用 C1 抽检方的手法 (它用"样本正文串在全文 113 页出现次数均为 1"排除短串碰巧命中)。

> **已知限制 (当场写清, 不许粉饰)**: 锚串唯一 **≠ 语义唯一** —— 别的 chunk 可能换措辞表达
> 同一事实, 本闸看不见。它只挡字面。引用本闸的绿灯时必须同时写它看不见什么 (硬规矩 19)。

### 闸 4 — fact 长度

每条 `expected_facts` ≥ 12 字符, 或属 OID / 编号 / codelist ID 类。禁 1–2 词碎片。

依据: `llm_judge_fact_recall.md` 记录 fact-recall **121/140 顶格**, 根因是 fact gold 85% 是
1–2 词关键词碎片。在 doc 轨重犯 = 答题侧尺子出生即失明。

## 5. 题型配比 (30 计分题)

| 题型 | 题数 | 说明 |
|---|---|---|
| 单节可答 | 12 | gold 单 chunk |
| 跨节需聚合 | 8 | gold 多 chunk, AND |
| `part` 家族 | 5 | 覆盖 `8.2` (3 份) 与 `22.1` (2 份) 两个家族 |
| 表格类 | 5 | 含 L6 那 2 个疑似被切断的表格作探针 |

覆盖面: 22 个章号 (2–14, 16–22) 里**目标**覆盖 18–20 章 —— 这是配题目标, **不是 PASS 闸**
(PASS 闸只有 §7 那三条)。实际覆盖数写进证据。

**OR 组 (`expected_sources_any`) 一题都不用**: `lint_gold.py` 结构上不读该键 (v2 已记录),
用了就等于把该题移出闸外。跨节聚合题一律用 AND 表达。

**`part` 家族判据按答案落点定, 不设全局政策**:

- 答案完整落在某一份 → gold = 单份 (严, 有判别力)
- 答案被切点劈开 → gold = 两份 AND —— **这就是 L6 探针本身**: 若接线后这类题稳定失分,
  就是"表格被切真伤答案"的证据; U4 的切点约束等这个证据

**L1 区题另开一池, `known_gap: true` 不计分**: 首锚点之前 66,200 字符 (卷首 + 第 1 章
≈16,880 字符是实体内容) 不属于任何 chunk。答案落在该区的题**当场标注、单独记数、不进计分池**
—— 否则会把一个覆盖决策伪装成检索失败。这个计数就是 kickoff §3「要不要给卷首做 chunk 型」
的裁定依据, 裁定权在用户。

## 6. 产出

| # | 产物 | 位置 | 进 git? |
|---|---|---|---|
| 1 | doc 侧题集 | `sdtm-rag/data/study/st01/eval/test_set_docs_v1.yml` | **否** (含正文锚串) |
| 2 | 出题依据 / 逐题笔记 / 失败归档 | 同目录 `DOCS_V1_NOTES.md` | **否** |
| 3 | gold 唯一性 lint (扩 docs 侧) | `sdtm-rag/eval/lint_gold.py` | 是 |
| 4 | 四闸检查脚本 + 单测 (含变异测试) | `sdtm-rag/eval/` + `scripts/tests/` | 是 |
| 5 | doc-only 上界基线 + 收口证据 | `sdtm-rag/evidence/checkpoints/doc_track_u1_question_set.md` | 是 |

### 6.1 doc-only 上界基线 — 为什么 U1 必须给出数字

跑法 (**已实跑通, 零代码改动**):

```bash
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
  --retrieval-only --hybrid \
  --collection study_st01_docs --kb-root data/study/st01/cards \
  --output runs/docs_v1_upper_bound.json
```

> `--kb-root` 指 `cards/` **不是混库** —— `RAGEngine` 硬要求 kb_root 下有 `ROUTING.md` +
> `INDEX.md` (docs/ 没有), 而 retrieval-only 下 kb_root 只进 system prompt, 不参与检索;
> hybrid 的 BM25 索引从 **collection 自身**建。这一条必须写进 NOTES, 免得下一个人误读成混库。

这个数字是 **U2 的对照上界**: 接线后 doc 侧分数应逼近它, 差额 = 接线损耗。
没有它, U2 拿到任何分数都分不清是"题太难"还是"接线烂"。

### 6.2 规则 A 独立抽检 (N=8)

独立 agent (非同一 `subagent_type`、非同一 session) 复核「题 – gold – 锚串」三元组,
并对抽样题**实测**"卡片库上确实答不出"。

流程约束 (C1 教训): 抽检方必须**边做边落盘**; 拿不到报告就当那一环没发生并在证据里点名
(硬规矩 17)。抽检进行中**不改产物目录** (C1 犯过, 靠 sha256 事后补证)。

## 7. 判定规则与自毁条款 (先于数据写死, 事后不得修改)

**U1 PASS 条件 (缺一不可)**

1. 30 题全过四道闸, 检查脚本退出码 0
2. doc-only 上界基线可复现: 同命令两次跑**逐题相同**
3. 规则 A 抽检 N=8 过判

**自毁条款 (触发即退回重写, 不许改阈值)**

| 触发 | 判定 | 理由 |
|---|---|---|
| doc-only 上界 **≥ 95%** | 题集**退回重写**, 不许拿去当 U2 的尺子 | 上界都接近满分时, U2 接线后的分数无法区分"接线好"与"题太简单" |
| doc-only 上界 **≤ 40%** | 题集**退回重写** | 题/锚串脱离 chunk 实际, 量的不是检索 |
| 闸 2 筛掉的题 **> 出题总量 50%** | **当场停下并报告用户** | doc 与卡片信息重叠远超预期 ⇒ C1 的价值假设本身有问题 (与 C2 同一种死法), 继续出题是浪费 |

阈值由用户于 2026-08-11 确认按此定稿。

## 8. 本设计**不能**证明什么

- **doc chunk 接线后有没有业务价值** —— U1 只证明尺子有判别力, 价值要 U2 实测
- **答题侧席位挤占是否有害** —— B 臂需接线, 留 U2 (kickoff 硬验收第 3 条)
- **语义层面 gold 是否唯一** —— 闸 3 只挡字面 (见 §4 闸 3 的限制)。membership 修订解决的是
  "锚串有没有落在 gold 里", **不解决**"别的 chunk 会不会用另一种措辞表达同一事实"
- **PDF 文本层是否忠于版面** —— C1 的 L9 盲点在本轨同样存在 (参照物同为 poppler)

## 9. 开工自检 (三条对不上先查环境)

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

2026-08-11 本 spec 定稿时三条均已实跑通过。
