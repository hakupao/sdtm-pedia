# U1 Task 9 — 独立抽检方 A 报告

> 角色: 独立抽检方 A (规则 D 隔离: 与出题方 / 审题方 / controller 无共谋)
> 对象: `data/study/st01/eval/test_set_docs_v1.yml` 30 题的「题 – gold – 锚串」三元组
> 约束: 只核验, 不改题集不改产物; 不 import `eval/` 下任何被检模块; 自建参照物
> 日期: 2026-08-12

## 0. 数据红线声明

本报告**不含**任何 anchor 原文 / chunk 正文片段 / 人名 / 机构名 / 联系方式 / PDF 真实文件名。
举证一律只用: qid + chunk 文件名 + 页码 + 出现次数 + 判定。

## 1. 抽样规则 (先写死, 后取样)

**本节在读取 `test_set_docs_v1.yml` 内容之前写入。** 规则如下, 不可事后调整:

```
分层配比 (按 controller 指定的 3/2/2/1):
  single_section 3 / cross_section 2 / part_family 2 / table 1  = N=8

层内选取 (确定性伪随机, 与题目内容无关, 只依赖 qid 字符串):
  对该层每个 qid 计算  h(qid) = int(sha256(("u1t9-auditA:" + qid).encode()).hexdigest(), 16)
  按 h 升序排序, 取前 K 个 (K = 该层配额)
  平手 (不可能, sha256 碰撞) 时按 qid 字典序

禁止事项 (自我约束):
  - 不许"取前 8"
  - 不许看过数据后更换 seed 字符串或排序方向
  - seed 字符串固定为 "u1t9-auditA:"，本行写入后不再更改
```

可复跑命令 (抽样复现):

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && ./.venv/bin/python scripts_audit_a_sample.py
# (脚本落在 scratchpad, 见 §6 复跑附录; 逻辑即上方伪码)
```

## 2. 开工基线

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && \
  find data/study/st01/docs -name '*.md' | sort | xargs shasum -a 256 | shasum -a 256
```

开工值: `0f13797f1871a3ddbab9b4741560e6a38451fce9e0ebebacbdac69e7d4f78dfd` — 与 controller 给定值一致 ✅

---

## 3. 抽样结果

池子实测配比与 controller 声明一致: single_section 12 / cross_section 8 / part_family 5 / table 5 = 30 ✅

抽中 8 题:

| category | 配额 | 抽中 qid |
|---|---|---|
| single_section | 3 | q01, q02, q16 |
| cross_section | 2 | q20, q26 |
| part_family | 2 | q42, q43 |
| table | 1 | q53 |

> 复跑注意: 抽样脚本打印的 `h` 是 `h % 10**12` 的**截断显示值**, 排序用的是完整
> sha256 整数。故打印列表看上去不是单调升序 — 这是显示口径, 不是排序 bug。

## 4. 口径澄清 (判定前必须先定尺)

### 4.1 复数 `anchors` 题的 ② 口径与 controller 字面口径不同

controller 给的 ② 是「anchor 在 114 chunk 正文出现次数 == `expected_sources` 条数」。
读闸 B 源码 (`eval/docs_gold_gates.py` 第 81-99 行 docstring, 只读未 import) 后确认:
该口径**只适用于单 anchor 题**。多 gold 题 2026-08-12 已改判 (commit `1626f83`), 现口径为:

```
anchors[i] 必须落在 expected_sources[i] 解析出的每个 chunk 里,
且任何一条 anchor 都不得落到 gold 集合之外。
```

即 2-gold 题的每条 anchor 期望出现次数是 **1**, 不是 2。
理由 (闸 B 自述): 跨节题要的是**互补**, 单条共享锚串证明的是**重复**, 方向相反。

⇒ 对 q20 / q26, 我**两种口径都报**: 字面 ② 与逐 gold ②。若只按 controller 字面口径读,
这两题会被误判为 FAIL(1≠2) — 这正是"数字对不上先查口径"的那一格。

### 4.2 页码基准校准

frontmatter `page_start`/`page_end` 与 `pdftotext -f N -l N` 的 1-based PDF 物理页**同基准**。
证据: 10 条 anchor 的 PDF 命中页 **10/10 全部落在**各自 gold 声明的页区间内。
若存在系统性偏移 (封面/目次导致的 ±N), 不可能 10/10 全中。

### 4.3 匹配口径

- chunk 正文 = 自己写的正则 `\A---\r?\n.*?\r?\n---\r?\n` 剥掉 frontmatter (不 import 闸的实现)
- PDF 文本 = `pdftotext -layout` 与 `pdftotext`(raw) **两套都跑**, 互为对照
- 每条串同时跑 **exact** 与 **nospace** (去掉 `\s` + 全角空格 + U+00A0) 两种口径

## 5. 逐题三元组判定

判定符号: ✅PASS / ❌FAIL。`sha10` = 该 anchor 的 sha256 前 10 位 (指代用, 不泄露正文)。

### docs_v1_q01 — single_section, ch.2
- gold: `st01__doc01__s2_4.md` (p22-24), n_gold=1
- anchor sha10=`f9bb0bea66` len=49
- ① PDF p24 exact 命中 (layout 与 raw 一致) → **✅PASS**
- ② chunk 命中 1 个 / 共 1 次出现 == n_gold 1 → **✅PASS**
- ③ anchor 页 24 ∈ gold 区间 22-24 (贴右边界) → **✅PASS**

### docs_v1_q02 — single_section, ch.2
- gold: `st01__doc01__s2_5.md` (p24-25), n_gold=1
- anchor sha10=`6c98201426` len=45
- ① PDF p24 exact 命中 → **✅PASS**
- ② chunk 命中 1 / 1 次 == 1 → **✅PASS**
- ③ 页 24 ∈ 24-25 (贴左边界) → **✅PASS**
- 备注: q01 与 q02 的 anchor 同在 PDF p24, 因为 s2_4(22-24) 与 s2_5(24-25) 页区间在 p24 重叠。
  两条 anchor 各自只落在自己的 gold 正文里 (②仍为 1), 故不构成缺陷; 但见 §7 限制 L2。

### docs_v1_q16 — single_section, ch.7
- gold: `st01__doc01__s7_4.md` (p58-58), n_gold=1
- anchor sha10=`19e2ca1e37` len=40
- ① PDF p58 exact 命中 → **✅PASS**
- ② chunk 命中 1 / 1 次 == 1 → **✅PASS**
- ③ 页 58 ∈ 58-58 (单页节, 零冗余) → **✅PASS**

### docs_v1_q20 — cross_section, ch.11 (复数 anchors)
- gold: `st01__doc01__s11_2.md` (p81-85), `st01__doc01__s12_5.md` (p86-87), n_gold=2
- anchors: [0] sha10=`118642fa80` len=40 / [1] sha10=`7d46347350` len=26
- ① anchor[0] PDF p81 exact; anchor[1] PDF p86 exact → **✅PASS**
- ② 逐 gold 口径 (§4.1): anchor[0]→仅 `s11_2` (1 次), anchor[1]→仅 `s12_5` (1 次);
  **配对顺序正确** (anchors[i] ↔ expected_sources[i]), 无 anchor 溢出 gold 集合外 → **✅PASS**
  - controller 字面口径下为 1≠2 — 属口径差异, **非缺陷**, 详见 §4.1
- ③ p81 ∈ 81-85 ✅; p86 ∈ 86-87 ✅ → **✅PASS**
- ⚠ 观察: anchor[0] 在 **nospace** 口径下 PDF 还命中 **p4**(exact 口径不命中)。
  p4 属目次区。实测全 114 chunk 的页覆盖为 **p17-113**, p1-16 完全不在语料内,
  故该 p4 命中**不进入 chunk 计数**, ② 不受影响 (nospace 口径下 chunk 命中仍为 1)。
  见 §7 限制 L3。

### docs_v1_q26 — cross_section, ch.18 (复数 anchors)
- gold: `st01__doc01__s18_1.md` (p100-100), `st01__doc01__s18_2.md` (p100-100), n_gold=2
- anchors: [0] sha10=`e83a9d787c` len=34 / [1] sha10=`b7f6ce4ce7` len=34
- ① 两条均在 PDF p100 exact 命中 → **✅PASS**
- ② 逐 gold: anchor[0]→仅 `s18_1`(1 次), anchor[1]→仅 `s18_2`(1 次), 配对顺序正确, 无溢出 → **✅PASS**
- ③ 两个 gold 页区间均为 100-100, anchor 页 100 → 覆盖成立 → **✅PASS**
- ⚠ 该题 ③ **无判别力**: 两个 gold 声明同一页, 页覆盖检查无法区分二者。
  真正区分二者的是 ② 的逐 gold 落位 (已 PASS)。见 §7 限制 L4。

### docs_v1_q42 — part_family, ch.8
- gold: `st01__doc01__s8_2__part03.md` (p74-75, part 3/3), n_gold=1
- anchor sha10=`603cd1bf7b` len=62
- ① PDF p75 exact 命中 → **✅PASS**
- ② chunk 命中 1 / 1 次 == 1 → **✅PASS**; 关键: **未溢出到同族 part01/part02**
- ③ 页 75 ∈ 74-75 → **✅PASS**
- 同族页区间: part01 p63-69 / part02 p69-74 / part03 p74-75 — 相邻 part 在切点页重叠 (69, 74),
  故 ③ 对 part 家族判别力弱, 真正的判别力来自 ②。见 §7 限制 L2。

### docs_v1_q43 — part_family, ch.22
- gold: `st01__doc01__s22_1__part01.md` (p106-112, part 1/2), n_gold=1
- anchor sha10=`683db97055` len=50
- ① PDF p106 exact 命中 → **✅PASS**
- ② chunk 命中 1 / 1 次 == 1 → **✅PASS**; **未溢出到 part02**
- ③ 页 106 ∈ 106-112 → **✅PASS**
- 同族: part01 p106-112 (22404 字) / part02 p112-113 (2806 字), 切点页 112 重叠。
  anchor 落在 p106, 距切点远 ⇒ 该题**不构成切点探针**, 只证明 part01 可定位。见 §7 限制 L5。

### docs_v1_q53 — table, ch.3
- gold: `st01__doc01__s3_8.md` (p31-34), n_gold=1
- anchor sha10=`f373ae01b5` len=28
- ① PDF p33 exact 命中 (layout 与 raw 均命中 ⇒ 表格串未被 `-layout` 的列对齐破坏) → **✅PASS**
- ② chunk 命中 1 / 1 次 == 1 → **✅PASS**
- ③ 页 33 ∈ 31-34 → **✅PASS**

### 汇总表

| qid | category | n_gold | ① PDF 逐字 | ② chunk 计数 | ③ 页覆盖 |
|---|---|---|---|---|---|
| q01 | single_section | 1 | ✅ p24 | ✅ 1==1 | ✅ 22-24 |
| q02 | single_section | 1 | ✅ p24 | ✅ 1==1 | ✅ 24-25 |
| q16 | single_section | 1 | ✅ p58 | ✅ 1==1 | ✅ 58-58 |
| q20 | cross_section | 2 | ✅ p81/p86 | ✅ 逐 gold 1+1, 配对正确 | ✅ 81-85 / 86-87 |
| q26 | cross_section | 2 | ✅ p100/p100 | ✅ 逐 gold 1+1, 配对正确 | ✅ (但无判别力) |
| q42 | part_family | 1 | ✅ p75 | ✅ 1==1, 未溢出同族 | ✅ 74-75 |
| q43 | part_family | 1 | ✅ p106 | ✅ 1==1, 未溢出同族 | ✅ 106-112 |
| q53 | table | 1 | ✅ p33 | ✅ 1==1 | ✅ 31-34 |

**8/8 题三元组全部成立。0 FAIL。**

## 6. 附带观察 (非三元组, 不构成缺陷判定)

核 ② 时顺手量了 `expected_facts` 是否逐字出现在 gold chunk 正文里。结果:
21 条 fact 中 12 条 nospace 逐字命中, 9 条不逐字命中 (q01×1, q16×1, q20×2, q42×1, q43×4)。

**这不是缺陷**, 因为没有任何一道闸要求 fact 逐字出现在 chunk 里 —— 读源码确认:
闸 C (`gate_fact_length`, 第 224 行) 只查 `len(fact) >= 12` 或 ID 形态;
`check_fact_recall` (`eval/run_eval.py:187`) 是拿 fact 对 **answer** 做小写子串匹配,
不对 chunk 匹配。run_eval 自己的注释也写明该子串口径对改述系统性**低估** (实测约 11pt),
`--judge` 语义模式即为此而设。

正面佐证 (我实测): 9 条不逐字命中的 fact, **每一条**的最长逐字公共子串
(`LCS_in_gold`) 都等于它在**全 114 chunk 语料**里的最长公共子串 (`LCS_anywhere`),
即**没有任何一条 fact 的更长逐字来源在 gold 之外**; 且 LCS 占比 45%-75%,
字符集 100% 落在 gold 内。⇒ 这些 fact 是 gold chunk 的改述/重排, 不是无出处杜撰。

**但它有一个可操作的下游含义** (见 §7 限制 L6): 这 5 题若用**非 judge** 模式跑分,
fact-recall 会被子串口径系统性压低。建议 doc 轨接线跑分时默认开 `--judge`。

## 7. 限制清单 (每条注明"它看不见什么")

- **L1 — 抽样只有 8/30 (26.7%)**
  看不见: 未抽中的 22 题。本报告的 8/8 PASS **不能**外推为 30/30 PASS。
  按分层比例, 若全池存在 1 个坏题, N=8 抽中它的概率约 27%。
- **L2 — 页区间在节/part 边界重叠, ③ 是必要非充分条件**
  实测: 8 个 gold 的页区间平均被另外 2-5 个 chunk 触及 (q7_4 达 4 个)。
  看不见: 「anchor 页落在 gold 区间内」**不等于**「anchor 只可能来自该 gold」。
  ③ 挡的是页码写错, 挡不住"页码对但归属错"。真正的归属证据是 ②。
- **L3 — 目次页不在语料内, ② 的唯一性对"未来加页"不稳健**
  实测 chunk 页覆盖 = p17-113, p1-16 (含目次) 零覆盖。
  q20 的 anchor[0] 在 nospace 口径下在 PDF p4 另有一次命中。
  看不见: 若日后把目次页也章节化进语料, 该 anchor 将不再唯一, ② 会翻红。
  当前判 PASS 只在"语料 = 现 114 chunk"这个前提下成立。
- **L4 — 同页多 gold 时 ③ 零判别力**
  q26 的两个 gold 都声明 p100-100, ③ 对二者给同一答案。
  看不见: 该题的页覆盖检查无法证伪任何错配, 它的 PASS 是"没矛盾"而非"有证据"。
- **L5 — part_family 抽中的 2 题都不是切点探针**
  q42 anchor 在 p75 (part03 区间 74-75), q43 anchor 在 p106 (part01 区间 106-112, 切点在 112)。
  看不见: 「被切点劈开的内容能否被正确归位」这件 part_family 最该考的事,
  这 2 题都没考到。它们只证明 part 级 gold 可唯一定位, 未证明切点两侧不串味。
- **L6 — 我没有跑任何检索/答题, ①②③ 全是静态字面核验**
  看不见: 检索器是否真能把这些 gold 召回来; 模型是否真能答对; fact-recall 实际得分。
  三元组成立 = **尺子刻度对**, 不等于**被测系统能通过**。
- **L7 — 全部为逐字口径, 语义唯一性未验**
  闸 B 自己的 docstring 已声明这条边界; 我沿用同一边界。
  看不见: 别的 chunk 是否用**不同措辞**表达了同一事实 (那会让"唯一 gold"这个前提失效)。
  §6 的 LCS 观察只对 `expected_facts` 做了弱形式检查, 对 `anchor` 未做。
- **L8 — 我未独立验证 chunk 正文本身忠实于 PDF**
  我验的是 anchor 三方一致。看不见: chunk 正文里**没被 anchor 覆盖到**的部分
  (q43 的 part01 有 22404 字, anchor 只锚了 50 字) 是否有抽取错误/漏字/串页。
- **L9 — `-layout` 与 raw 两套抽取一致, 但都是 poppler**
  看不见: poppler 与 PDF 原始字形层的差异 (如连字、异体字、CID 映射)。
  两套口径同源, 不构成独立信源。

## 8. 收工基线

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && \
  find data/study/st01/docs -name '*.md' | sort | xargs shasum -a 256 | shasum -a 256
```

收工值: `0f13797f1871a3ddbab9b4741560e6a38451fce9e0ebebacbdac69e7d4f78dfd`

**开工 == 收工 ✅** ⇒ 抽检全程未触碰 `data/study/st01/docs/`。

### 并发污染排查

收工时 `git status` 显示 `sdtm-rag/eval/gold_semantic_check.py` 处于 modified —
系另一名抽检方对 `eval/` 做变异测试所致 (controller 已预告), **非本次抽检所为**。
本报告只新增 `evidence/step_u1_audit.md` 一个未跟踪文件。

该并发是否污染我的结论: **否**。理由:
1. 我全程未 import / 未运行 `eval/` 下任何模块 (硬约束 #1/#4), 只**读源码定口径**;
2. 我读过的三个文件 —— `eval/docs_gold_gates.py`、`eval/run_eval.py`、
   `data/study/st01/eval/test_set_docs_v1.yml` —— 收工时 `git status` 均为**干净**;
3. 我引用的多 gold 口径另有**已提交**的出处 (commit `1626f83`), 不依赖工作区状态。
4. 被改动的 `gold_semantic_check.py` 我从未读取, 也未参与任何判定。

排查命令:
```bash
git status --porcelain -- sdtm-rag/eval/docs_gold_gates.py \
  sdtm-rag/eval/run_eval.py sdtm-rag/data/study/st01/eval/test_set_docs_v1.yml
# 空输出 = 三者均未被并发改动
```

## 10. 总判定

**有条件 PASS** — 抽中的 8 题三元组 24/24 项 (8×①②③) 全部成立, 0 FAIL。

条件 (三条, 缺一则结论需重估):
- **C1**: 结论仅覆盖抽中的 8 题, **不外推**到未抽的 22 题 (限制 L1)。
- **C2**: ② 的唯一性以「语料 = 现 114 chunk (PDF p17-113)」为前提。
  若把目次页 (p1-16) 纳入语料, q20 的 anchor[0] 将不再唯一 (限制 L3)。
- **C3**: 结论是**字面级**的。「尺子刻度对」不等于「检索能召回、模型能答对」,
  也不排除别的 chunk 用不同措辞表达同一事实 (限制 L6/L7)。

## 9. 复跑附录

所有脚本落在 scratchpad (不进 repo), 逻辑已在上文写明, 可按需重建:

| 脚本 | 作用 |
|---|---|
| `sample_a.py` | §1 抽样规则的可执行实现 |
| `extract_pdf.py` | 经 `scripts.study.paths.resolve_study('st01')` 取 PDF, 逐页抽 layout+raw |
| `audit_a.py` | 三元组主核验 (①②③) |
| `audit_a2.py` | 页覆盖/重叠/part 家族/facts 附带检查 |
| `audit_a3.py` | facts miss 的 LCS 特征刻画 (不打印正文) |

未跑 / 不声称的事项 (防止把推断写成实测):
- 未跑 `eval/` 下任何模块, 未跑 pytest (controller 硬约束 #4)
- 未跑检索、未跑答题、未跑 fact-recall 评分 → §6 的下游影响是**推断**, 不是实测
- 未验证未抽中的 22 题

