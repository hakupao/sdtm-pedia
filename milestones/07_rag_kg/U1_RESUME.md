# doc 轨 U1 — ✅ CLOSED (有条件) 2026-08-12 · 本文件转为历史只读

> **路由词「U1 续跑 开始任务」已作废** —— U1 的 Task 1-10 全部完成。
> 下一单元 = **U2 接线**, 路由词「**doc 轨 开始任务**」→ `DOC_TRACK_KICKOFF.md`。
> **收口证据 (先读它, 不要从本文件的旧"下一步"开工)** →
> `sdtm-rag/evidence/checkpoints/doc_track_u1_question_set.md`
> 数据红线: 本文件进 git, **零真名零正文**。题集/笔记/失败归档全在 `sdtm-rag/data/study/`(gitignored)。

## 0. 收口结果 (2026-08-12)

30 题计分池建成并**三方独立核验**通过 (规则 D 五方不同 session)。**两把尺子, 引用时都要报**:

| 尺子 | 值 | 量什么 |
|---|---|---|
| doc-only 上界 (k=15, 生产档) | **100.0%** | 接线损耗的参照 (spec §6.1) |
| 诊断档 k=5 | **88.33%** | 判别力 (5 题非满分; `q01`/`q43` 的 gold 完全不在 top-5) |

⛔ **上界 100% 触发了 spec §7 第一条自毁条款 (≥95% ⇒ 题集退回重写)。**
阈值与判定规则**自始至终未改**; 当场停下上报后, **用户裁定豁免**(理由: 该条款对 114 chunk
的小库不适用) **+ 改用双尺子**, 题集不重写。
**引用纪律: 必须写成「触发了, 用户豁免」, 写成「四闸全绿一次过」就是伪造记录。**

以下 §1-§11 是 Task 8 开工前的历史交接内容, **保留供追溯**, 但其中的「下一步 / 续跑第一步」
已被本节取代。

## 1. 开工自检 (五条对不上先查环境, 别在错的基线上开工)

```bash
cd sdtm-rag
.venv/bin/python -m pytest -p no:warnings                                   # → 1119 passed
P=data/study/st01/eval/test_set_docs_v1.yml
.venv/bin/python -m eval.docs_gold_gates $P --docs-dir data/study/st01/docs \
  --cards-dir data/study/st01/cards          # → 30 题 0 finding · 闸 D 对 2/30 有约束力 · EXIT=0
.venv/bin/python -m eval.lint_gold $P --docs-dir data/study/st01/docs        # → 0 条 · EXIT=0
.venv/bin/python -m eval.gold_semantic_check $P --docs-dir data/study/st01/docs            # → 0 触发
.venv/bin/python -m eval.gold_semantic_check $P --docs-dir data/study/st01/docs --mode selfsuff
                                              # → 只报 q24 (已人工判为真跨节, 属正常触发)
git status --porcelain                        # → 3 个 tracked 文件被改 (见 §8), 或已 commit 则为空
```

现状数字: **30 题 · 79 条 fact · 章覆盖 17 · L6 探针 2 (q41/q57)**
· 配比 `single_section 12 / cross_section 8 / part_family 5 / table 5` (与 spec §5 逐项一致)
· fact 数分布 `1:3 / 2:14 / 3:7 / 4:4 / 5:1 / 6:1` · L1 池 **0 条**(见 §6)

## 2. 依据文档

| 什么 | 在哪 |
|---|---|
| spec (判据 / 配比 / **自毁条款**) | `docs/superpowers/specs/2026-08-11-doc-track-u1-doc-question-set-design.md` |
| plan (Task 8 命令逐字在 §Task 8) | `docs/superpowers/plans/2026-08-11-doc-track-u1-doc-question-set.md` |
| **出题笔记 (1157 行, 最全)** | `sdtm-rag/data/study/st01/eval/DOCS_V1_NOTES.md` |
| 各环报告 (出题/审题/审计/勘察/实测) | `.superpowers/sdd/2026-08-11-doc-track-u1-doc-question-set/task-{6,7}-*.md` |
| 题集 / 锚串 / 归档 (**不进 git**) | `sdtm-rag/data/study/st01/eval/` |

**NOTES 里必读四段**: `R7` 转移性规律 · `R11` 已知限制 · `R12.4` 操作化三条检查 · **`D` PRT/EDC 归因框架**。

## 3. Task 8 要做什么

```bash
cd sdtm-rag
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
  --retrieval-only --hybrid \
  --collection study_st01_docs --kb-root data/study/st01/cards \
  --output data/study/st01/eval/runs/docs_v1_upper_bound.json
# 再跑一遍到 ..._rerun.json, 逐题比对 source_recall 必须完全相同 (PASS 条件第 2 条)
```

> `--kb-root cards/` **不是混库**: `RAGEngine.__init__` 硬要求 kb_root 下有 `ROUTING.md` 与 `INDEX.md`
> (docs/ 没有), 而 retrieval-only 下 kb_root **只进 system prompt 不参与检索**;
> hybrid 的 BM25 索引从 **collection 自身**建。**这句必须原样进证据**, 否则下一个人会读成混库。

### ⛔ 三条自毁条款 (spec §7, 2026-08-11 用户定稿, **不许改阈值、不许改判定规则**)

| 触发 | 判定 |
|---|---|
| doc-only 上界 **≥ 95%** | 题集**退回重写** |
| doc-only 上界 **≤ 40%** | 题集**退回重写** |
| 闸 2(卡片答不出) 筛掉 > 出题总量 50% | 当场停下报告用户 (三批实测 4.5%/20%/22.2%, **未触发**) |

**量的是 `source_recall`, 不是 fact-recall** —— retrieval-only 不产生答案, fact 侧不参与该基线。

## 4. 🔴 归因框架 (用户 2026-08-12 提供, 影响一切解读)

**EDC 的设计基于 PRT, 但两者仍有非原则性出入。PRT 偏理论, EDC 偏落地。**

- **PRT 出的题在 EDC 侧答不出, 不一定是检索失败** —— 归因先分清「PRT 有而 EDC 结构上就没有」与「检索没找到」。
  **doc 轨题集的失分不得默认归因到检索质量。**
- 由此: 闸 D 低约束力 (2/30) **不是闸设计坏**, 是两侧语域在流程/手续域结构性不相交
  (审题方 60 词扫描: 缺席 **59/60**)。**「装饰闸」这个说法要改口径。**
- 「卡片答不出」对 PRT 流程题是**常态不是成就**; 低污染率**不构成「题出得好」的证据**。
- **本段支持 C1 价值假设, 但它是领域论据不是实证** —— 不许与「低污染率」那个测量合并引用
  (后者对 C1 **零信息量**)。实证等 U2。
- **Task 8 不受影响**: 上界基线是 PRT chunk 答 PRT 题, 不涉跨源。

## 5. 已知限制 (引用任何绿灯时必须同时写, 不许压缩成「四闸全绿」)

1. **闸 B 只挡字面**, 语义等价看不见。本单元实测栽过一次 (q46 四闸全绿而 gold 漏写真实存在)。
2. **闸 D 对 28/30 题不可触发**, 其绿灯**不可证伪** —— 是「未检验」不是「通过」(口径见 §4)。
3. **逐 gold 锚串证明「答案分布在这几块」, 不证明「这几块之外没有答案」。**
4. **part 家族 5 题的来源隔离不适用** (用户裁定接受), 不能用于论证题集与切分器无共谋。
5. **语义自查触发线脆弱**: 唯一真实 gold 漏写 (q46) 覆盖率 **0.775**, 线 0.7 —— 余量 **0.075**。
6. **闸 C 零余量**: 全池最短 fact 正好 **12 字 = 阈值**。任何缩短一字的改写都会红。
7. **`--mode selfsuff` 不在默认输出里** —— 跑默认命令看不到单 gold 自足性。**须写进 Task 10 收口清单。**
8. **本题集必须跑 `--judge`**: `check_fact_recall` 是裸子串匹配, 而 79 条 fact 全是 12–78 字完整句;
   另有 **11 条含 `-layout` 的数字-单位空格**。不跑 judge 会得到接近零的 fact-recall, **与检索质量无关**。
9. **L6 探针 n=2 且供给已尽**: 全语料 113 切点勘察 (无抽样) 判定可探针**仅 1 个**, 即 q41/q57 所在那个。
   q57 的判定是**生成侧**实测 (n=18, 单模型单温度), **不是检索侧**; 换模型或修剪切口**可能翻转**。
10. **`s10_3` 的两个表体在 PDF 文本层就已丢失** (非切分器) ⇒ 该主题**无 gold 可依, 不得出题**。
11. 三道题只有 1 条 fact (`q04`/`q42`/`q51`) ⇒ fact-recall 退化成 0/1 二值。
12. **`q57` 的 `anchors[0]` 含定长空格串** ⇒ 换 poppler 版本重抽语料会被闸 B 误报成假红。

## 6. L1 池 = 0 条 —— 这个 0 几乎没有信息量

三批指派范围**全部从 p017 起, 没人被派去卷首出题, 那里不可能产出题** ⇒ **0 是指派的结构性后果, 不是语料性质。**

裁定「卷首要不要做 chunk」请用: **概要区 (p001–p010) 30 字窗 44.1% / 60 字窗 29.6%**(逐字口径 ⇒ 是**下界**);
**不要**用被目次(占 82.4%)稀释的 8.3%/5.2%。
另: **30 题里只有 q20 一条锚串逐字命中卷首**(规范化空白后) ⇒ 卷首做 chunk 的代价是**可控且具体的**。

## 7. 🔴 红线

- 题集 / 锚串 / 笔记 / 失败归档 **只许**落在 `sdtm-rag/data/study/`(gitignored)
- **不得整段引用 chunk 正文** —— 实测 **27/114 个 chunk 含个人可识别信息**
  (联系方式形态 12 ∪ 人名形态 4 ∪ 第 20 章名簿 18), **且这是下界**(人名模式只覆盖一种写法)。
  举证只给**文件名 + 位置描述 + 计数**。
- 写进测试 fixture 的任何 ID 形态串, 落盘前必须 `grep -rlw '<串>' sdtm-rag/data/study/` 确认 0 命中
- **进 git 的文件落盘前跑一次红线自查**: 新增文本里有无 ≥12 字日文串同时出现在某 chunk 正文里
  (controller 本 session 靠这条抓到自己一次 17 字泄漏)

## 8. 未提交的 tracked 改动 (若 §1 自检显示树不干净)

| 文件 | 改了什么 |
|---|---|
| `docs/superpowers/plans/...-doc-question-set.md` | Task 7 的 L6 目标改「能加则加」+ 计数命令改结构化键 + 取材禁区 |
| `sdtm-rag/eval/gold_semantic_check.py` | 新增 `--mode selfsuff` 单 gold 自足性检查 (不改原 overlap 行为) |
| `sdtm-rag/scripts/tests/test_gold_semantic_check.py` | +13 测试 (1106 → 1119); 物理变异已验证会红 |

## 9. 上一 session 最贵的东西 —— 第八类失败形态

交接旧版 §4 记的七次都是「**绿灯不可能变红**」。本 session 出现的是**镜像**:
「**红灯从未发生过**」—— 把**推断**写成**实测语气**。共 **6 例**, 含 controller 自己 1 例。

**共同点: 六例全部由复现驳回抓出, 无一次自查发现。且每一方都至少犯一次。**

> **对策 (与「变异必须先看到它变红」并列): 写「实测」必附可复跑命令。没跑就不写。**
> 假实测比缺陷更害人 —— **它让下一个人跳过复验**。

**同期还有三次「数字分歧实为口径差」**(q27 覆盖率 / プロトコール 计数 / 锚串卷首命中),
每次都是**先查两边规范化口径**才避免误驳。**核对数字对不上时, 先查口径, 别急着判谁错。**

## 10. ⚠ 一条流程结论 (比任何技术发现都该传下去)

**「边做边落盘 + 最终回传」写进 brief 对 agent 的约束力接近零。**
本 session 措辞逐次加重 (最后写到「已有 5 个 agent 栽在这条上, 别当第六个」), 结果 **7 个 agent 里 6 个零回传**。

**有效的不是措辞, 是 controller 的固定动作**:

> **派 subagent 后, controller 必须主动查盘 + 索取补发, 不要依赖 brief 里的回传要求。**
> 补发不是补救, 是**流程的正常一环** —— 本 session 6 次补发中有 4 次内容比首次交付更硬
> (口径撤回 / 假实测订正 / n=7 实测细节 / 对上游数字的订正)。

## 11. 续跑第一步

1. 跑 §1 五条自检
2. 读 §4 (归因框架) 与 §5 (已知限制) —— 这两段决定你怎么解读 Task 8 的数字
3. 跑 Task 8 两遍, 逐题比对 `source_recall`
4. **对三条自毁条款**。触发了**不许改阈值**, 当场报告用户
5. 之后 Task 9 (闸 D 实测复核 N=6 + 规则 A 独立抽检 N=8) → Task 10 (收口证据 + Chain B)

**派 subagent 时**: 规则 D 要求出题方与审题方**不同 `subagent_type`、不同 session`;
本 session 已用过 `general-purpose`(出题) / `claude`(审题·审计) / `oh-my-claudecode:{executor,scientist,test-engineer,explore}`。
