# C2R L1 — EDC OID 对照表 (答题时确定性 label 补齐)

> 状态: **DONE** (2026-09-09) · 单元 `PLAN_c2r_pdf_bypass.md` §1 L1 · Tier 2
> 复审: 独立 subagent (规则 D, 异 session) → **PASS with nits**, MINOR-1~4 + NIT 已全部修完并重测
> 本文所有 "实测" 数字均附可复跑命令 (无命令 = 不算实测)

## 1. 做了什么, 为什么

**起点缺陷** (dogfood 2026-09-09 10:49, LB Form 身高体重题): 卡片里的 `- 非表示アクティビティ:`
行只有裸 OID, 模型照抄, 人读不懂"这个活动到底是哪一步"。

**修法**: 答题时在上下文末尾确定性附一张 `OID = 官方日语名` 对照表, 数据源只有 `catalog.json`,
零 LLM 参与; 同时给 study 侧 system prompt 加一条命名规则 (初出必须併記官方名 + 查不到就不许猜
+ 对照表不许当 `[Source:]` 引用)。覆盖 activity / form / event 三类 OID。

## 2. 硬约束: 不碰卡片文本

把名字写进卡片本文是最直觉的做法, **已被实证否决**: 卡片间共享文本会造成检索挤占回归
(见 `evidence/failures/t4_step7_retrieval_regression.md`)。因此本单元的全部改动位于
**答题时的上下文拼装**, 检索层 (`retrieve` / `_search` / `_apply_study_lookup` / chunk / 向量库)
一行不动 —— 这条约束由 §4.2 的 AST 函数级 diff 与 §4.3 的 golden 复跑双向背书。

## 3. 设计落点 (三处)

| 位置 | 内容 |
|---|---|
| `server/study_lookup.py::StudyLookup.glossary_for` | 文本 → `[(oid, 名前)]`; 有界匹配 (`_bounded_re`), catalog 顺序, 去重 |
| `server/rag.py::RAGEngine.glossary_block` / `format_context` | 组块; `format_context(chunks, *, glossary=True)`, CDISC 引擎逐字节不变 |
| `server/study_corpus.py::StudyCorpusEngine.format_context` | cards 传 `glossary=False`, 组合后**整段文脈末尾出一次** |

三条设计要点:

1. **匹配用有界一致, 不是裸子串。** 短 OID 不得在长 OID 内部误命中 (`XACT_A2` 不许从
   `XACT_A2_LB` 里匹配出来) —— 否则上下文会主张一条 catalog 里不存在的事实。日文不在
   `[A-Za-z0-9_]` 内, 紧贴假名/汉字的 OID 照常命中。112 条模式在 `__init__` 里预编译。
2. **扫描对象 = 已拼装好的上下文字符串本身。** 与模型实际读到的字符串一一对应, 因此
   "4000 字截断之后的 OID 被翻译, 出现在对照表里却不在正文中" 这类幽灵行在结构上不可能发生。
3. **对照表在形态上不许像 chunk。** chunk 是 `---` 分隔 + `### [N] src` 标题; 对照表**不加**
   前置 `---`, 标题降一级用 `####`, 并由 prompt 明说它不是检索到的文档、不许给它编 `[Source:]`。

单库 study 路径 (未启用 docs) 由 `RAGEngine.format_context` 自己出一次; 启用 docs 时由组合器
统一出一次 (cards 侧被 `glossary=False` 关掉), 因此**任何路径下都恰好一张表**。

## 4. 实测证据

### 4.1 全量测试

```bash
uv run pytest -p no:warnings --ignore=scripts/tests/test_pdf_context.py
# → 2147 passed, 0 failed, exit 0
```

`--ignore` 的原因: 同期并行 agent 的在途文件 `scripts/tests/test_pdf_context.py` 引用了尚未落地的
`server.pdf_context`, 收集期就 ImportError。该报错与本单元无关 (本单元不碰这两个文件), 但不排除在外
就拿不到本单元的绿。

L1 新增测试 23 条 (`test_study_lookup.py` +19 / `test_study_corpus.py` +3 / `test_federation.py` +1),
计数命令:

```bash
for f in test_study_lookup test_study_corpus test_federation; do
  echo -n "$f: "; echo "$(grep -cE '^def test_' scripts/tests/$f.py) - \
$(git show HEAD:sdtm-rag/scripts/tests/$f.py | grep -cE '^def test_')" | bc
done
```

⚠ 2147 这个总数**不能全记在本单元头上**: 同期有并行 agent 在同一工作树增删测试。本单元自己的
增量以上面 23 条为准。

### 4.2 AST 函数级 diff — 检索层零改动

比 `git diff` 强的地方: 它按函数比对源码文本, 能直接回答"检索链有没有被动过", 不受注释/空行干扰。

```bash
uv run python - <<'PY'
import ast, subprocess
for f in ["server/rag.py", "server/study_lookup.py", "server/study_corpus.py"]:
    old = subprocess.run(["git","show",f"HEAD:sdtm-rag/{f}"],capture_output=True,text=True).stdout
    new = open(f, encoding="utf-8").read()
    fx = lambda s: {n.name: ast.get_source_segment(s, n) for n in ast.walk(ast.parse(s))
                    if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    o, w = fx(old), fx(new)
    print(f, "->", sorted(k for k in set(o)|set(w) if o.get(k) != w.get(k)))
PY
```

实测输出:

```
server/rag.py -> ['_build_system_prompt', 'format_context', 'glossary_block']
server/study_lookup.py -> ['__init__', '_add_gloss', '_bounded_contains', '_bounded_re', 'glossary_for']
server/study_corpus.py -> ['format_context']
```

即 `retrieve` / `_search` / `_apply_study_lookup` / `_apply_structured_lookup` / `_embed_query` /
`_rerank` / `_rrf_fuse` / `build_messages` / `resolve` / `_channel_hits` / `resolve_events` /
`strong_hit` 全部**逐字节相同**。

⚠ 名单里 `_bounded_contains` 出现了, 需要说清: 它的改动是**把正则构造抽成 `_bounded_re` 后委托**,
模式串一字未改 (抽出来是为了让 glossary 的 112 条能预编译, 同时不让"边界怎么算"有第二份定义)。
它的唯一消费方 `resolve_events` 本体逐字节未变, 相关用例 (`test_study_lookup_events.py`) 全绿。

`git diff --stat` 侧证: 无任何 `data/` / `scripts/ingest*` / chunker 改动。

### 4.3 study golden v2 (48 题, retrieval-only, 零 LLM)

```bash
uv run python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards \
  --output data/study/st01/eval/runs/c2r_l1_golden_v2.json
```

| 指标 | 本次 | 基线 (`study_golden_v2.md`) |
|---|---|---|
| source_recall_avg | 0.875 | 0.875 |
| n_scored | 48 | 48 |

逐位一致 = 检索零回归。run JSON 存 `data/study/st01/eval/runs/c2r_l1_golden_v2.json`
(该目录 gitignored, 因为含真实题面与卡片名)。

### 4.4 doc 侧覆盖 — MINOR-1 的判据

复审指出对照表若只在 cards 引擎内部出, 手順書章節里的 OID 不会被翻译。实测该缺口非空:

```bash
uv run python - <<'PY'
import json, pathlib
from server.study_lookup import StudyLookup
lk = StudyLookup(json.load(open("data/study/st01/catalog.json", encoding="utf-8")))
docs = sorted(pathlib.Path("data/study/st01/docs").glob("*.md"))
hit = [(d.name, len(lk.glossary_for([d.read_text(encoding="utf-8")]))) for d in docs]
n = [x for x in hit if x[1]]
print(f"doc files={len(docs)} with_oid={len(n)} rows={sum(c for _, c in n)}")
PY
# → doc files=125 with_oid=20 rows=27
```

125 个手順書章節里 20 个含 catalog OID, 共 27 条可翻译 ⇒ 采纳 MINOR-1, 对照表上移到组合器,
扫描 cards+docs 合并后的整段文脈。

### 4.5 demo (起点缺陷那张卡)

```bash
# 卡文件名含真实 item OID, 本文不能直写 (红线) ⇒ 用 redline-safe 选择子, 结果唯一确定
CARD=data/study/st01/cards/$(ls data/study/st01/cards | grep -E '__LB__W' | sort | tail -1)
uv run python - "$CARD" <<'PY'
import json, sys
from server.study_lookup import StudyLookup
lk = StudyLookup(json.load(open("data/study/st01/catalog.json", encoding="utf-8")))
rows = lk.glossary_for([open(sys.argv[1], encoding="utf-8").read()])
for oid, name in rows:
    print(f"- {oid} = {name}")
print(f"# rows={len(rows)}")
PY
```

实测 `rows=14` (activity 13 + form 1), 形如:

```
- A_XXX_YY = <イベント名> › <アクティビティ名>
- <FORM> = <フォーム名>
```

完整输出 (含真实取值) 存 `data/study/st01/eval/runs/c2r_l1_demo_weightstat.txt` (gitignored)。
**本文按红线只写形状与条数**, 真值不落进受版本控制的文件。

其中一条边界用例在真实数据上得到验证: 该卡只写了带 `_LB` 后缀的那个活动 OID, 而 catalog 里
另有一个去掉该后缀的**真实且不同**的活动; 对照表没有把后者混进来 —— 有界匹配生效。

### 4.6 ruff

```bash
uv run ruff check --output-format=concise \
  server/rag.py server/study_lookup.py server/study_corpus.py \
  scripts/tests/test_study_lookup.py scripts/tests/test_study_corpus.py \
  scripts/tests/test_federation.py scripts/tests/test_web_rule9_prompt.py
# → 2 errors, 均为 server/rag.py 既有的 RET503 (HEAD 同样 2 条), 无新增
```

复审提出的 2 条 I001 (import 未排序) 已修 (`ruff check --fix --select I001`)。

### 4.7 红线闸

```bash
uv run python -m scripts.oidscan_evidence \
  server/rag.py server/study_lookup.py server/study_corpus.py \
  scripts/tests/test_study_lookup.py scripts/tests/test_study_corpus.py \
  scripts/tests/test_federation.py scripts/tests/test_web_rule9_prompt.py \
  evidence/checkpoints/c2r_l1_oid_glossary.md \
  --catalog data/study/st01/catalog.json
# → CLEAN
```

测试用的是 `X` 前缀合成 catalog (`GLOSSARY_CATALOG`), 与真实 catalog 零交集; prompt 里的书式
示例同样是占位符 (`A_XXX_YY` / `FRM` / `E_XXX`)。

## 5. 复审 MINOR 逐条修法

| 项 | 复审意见 | 修法 |
|---|---|---|
| MINOR-1 | 手順書章節的 OID 没被翻译 | 对照表上移到 `StudyCorpusEngine.format_context`, 扫 cards+docs 合并文脈; 新增测试用两节**不同**的 OID, 只扫一节的实现会红 |
| MINOR-2 | 对照表夹在卡片节与手順書节之间, 归属不明 | 同上, 移到整段末尾出一次; cards 侧由 `glossary=False` 关闭, 另有测试钉住"关不掉就会出两次" |
| MINOR-3 | catalog 行缺字段会让 `StudyLookup` 构造炸掉, 连累 S2 直查整层 | 三个池全改 `.get(...) or ""`; 缺 name 的行只是不进表。新增缺字段用例 |
| MINOR-4 | 2 条新 I001 | `ruff --fix --select I001` |
| NIT | 对照表长得像 chunk, 模型可能给它编 `[Source:]` | 去掉前置 `---`, 标题降为 `####`; prompt 新增一条"对照表不是 chunk, 不许附 `[Source:]`"; 书式示例补 form / event 两行 |
| NIT | prompt 说"文脈末尾"过死 | 改为"文脈中の「EDC OID 対応表」", 并有测试禁止"末尾"字样回潮 |

## 6. 已知限制

1. **2 字符 form OID 可能被日文正文偶然命中** (真实 21 个 form 里 7 个是 2 字符)。与
   `_MIN_FORM_OID_LEN` 已经吞下的是同一个天秤, 但代价轻得多: 只多出一行对照, 检索结果一条不动。
2. **对照表覆盖 study 侧文脈, 不覆盖 CDISC 节。** 联邦 both 判库下, 标准侧正文若出现同名字符串
   不会被翻译 —— 这是有意的: 对照表是本研究 catalog 的主张, 不是标准侧的。
3. **未做答题侧效果评测。** 本单元只证"对照表确定性正确 + 检索零回归", 模型是否真的照规则併記
   官方名, 属 V3 预登记题的判分范围 (`c2r_pre_registration.md`), 本单元不声称。
4. **`_bounded_contains` 的委托改写没有独立的变异验证**, 只靠既有 `resolve_events` 用例 + 模式串
   逐字未改。若后续要动边界语义, 应先补一条对拍测试。
