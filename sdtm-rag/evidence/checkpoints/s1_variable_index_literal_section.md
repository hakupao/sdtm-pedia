# S1 VARIABLE_INDEX 字面 section 定位 — 收口 checkpoint

> 状态: **DONE** (2026-08-07) — 三方隔离审查完成, 审查 2 HIGH + 抽检 1 代码缺陷全部已修
> 设计: `docs/superpowers/specs/2026-08-07-s1-variable-index-literal-section-design.md`
> 计划: `docs/superpowers/plans/2026-08-07-s1-variable-index-literal-section.md`
> 上游: `evidence/checkpoints/cdisc_gold_section_granularity.md` §6.1 (本缺陷由 section 化暴露)
> commit: `25da6cf` (锚点抽取) + `2667f63` (映射反建 + 注入接线)

---

## ⚠️ 引用前必读 — 与作废口径**三元组逐位全同**, 数字在这里没有判别力

```
CDISC 检索 (eval/test_set_v3.yml 140q, --retrieval-only --hybrid --structured-lookup)

                          140 题    18 题子集   其余 122 题
  作废口径 (路径级判据)    98.93%    100.00%     98.77%    ← 含约 3pt 水分 (4 假 + 1 半假命中)
  改动前   (section 级)    95.71%     75.00%     98.77%
  改动后   (section 级)    98.93%    100.00%     98.77%    ← 本次
```

**三个数与作废口径逐位全同, 这是结构必然, 不是巧合** (规则 A 抽检结论)。
两把尺子的分歧**只在这 18 题**; 本轮把 18 题全部拉满, 全集必然回到 `138.5/140`。
**以后任何一次 VI 子集满分都会再次撞上同一组数字。**

**因此: 数字对比表在这里没有判别力, 禁止用数字论证"本轮有效"。**

硬禁写法:
- ✗ `98.93% → 98.93% (Δ0)` —— 会被读成"什么都没发生"
- ✗ "恢复到历史水平 / 回到 98.93%" —— 暗示旧数字是合法基准; 旧数字含约 3pt 假命中水分
- ✗ 把旧路径级 98.93% 与新值**并排陈列在同一张基线表** —— 并排即制造"两次相同数字"的假象,
  旧行应划掉或压进脚注
- ✓ 唯一正确写法: `95.71% (section 级, 改动前) → 98.93% (section 级, 改动后, commit 2667f63)`

**判别只能靠 section 名, 不能靠分数**: 旧口径下 q109 召回 `§三 CT 交叉引用: C66734`
(RDOMAIN, 与题无关), 新口径下召回 `§三 CT 交叉引用: C99073` (17 个 `--LAT` 变量, 正是 gold)。
引用本轮成果时**必须**同时给出这条 section 级证据, 否则该引用无效。

---

## 1. 问题

`StructuredLookup` 把 18 道题确定性解析到 `VARIABLE_INDEX.md` 是对的, 但**文件内选哪一块靠 cosine**。
VI 的 222 个 chunk 是极短结构化单行, 对自然语言问句的 embedding 相似度近似噪声 → 文件内选块基本随机。
section 级判据落地后显形: 18 题子集 100.00% → 75.00% (4 假命中 + 1 半假命中)。

**要的块一直在索引里, 只是 cosine 选不中。**

## 2. 修法

| 环节 | 位置 | 做法 |
|---|---|---|
| 锚点抽取 | `server/structured_lookup.py::variable_index_anchors` | 复用既有 `_QUERY_CT_RE` + `_query_variables`; CT 码在前, 去重保序, 上限 `_MAX_VI_ANCHORS=3` |
| 锚点→section 映射 | `server/rag.py::_vi_section_map` | **从 Chroma 元数据反建**并缓存; 只假设 section 以 `: <TOKEN>` 结尾; 空表 fail-loud |
| 注入 | `server/rag.py::_lookup_chunks_for_variable_index` | `{"$and": [source, section]}` 精确过滤, 每锚点 1 块, 复用已算好的 query embedding |
| 回落 | 同上 | 锚点解不出 / section 不在索引 / 全落空 → 回落原 `_lookup_chunks_for_file` |

### 为什么不拼格式串 (关键设计决定)

`f"§三 CT 交叉引用: {code}"` 等于把同一份格式定义写两遍。ingest 侧改 section 命名时, 拼串方案会
**静默全 miss 并回落 cosine —— 分数无声退回改动前, 任何闸都拦不住** (偏差朝下但无声)。
这与本轮第 1 条硬规矩 (`NEXT_ROUND_KICKOFF.md` §3.1: 判据检查工具必须与被检查判据逐字同语义) 同源。
从索引反建则只有一份事实来源; 建不出来就响亮失败。

覆盖 `§一 通用变量` (24) + `§三 CT 交叉引用` (135) 两族; 域变量表 (63) 不做 —— 域码问题已由
`domains/<CODE>/spec.md` 通道承接。

## 3. 实测

### 3.1 映射反建对上索引实际构成

```bash
cd sdtm-rag && .venv/bin/python - <<'PY'
from pathlib import Path
import chromadb
from server.config import settings
from server.rag import RAGEngine
eng = RAGEngine.__new__(RAGEngine)
eng.kb_root = Path(settings.kb_root)
eng.collection = chromadb.PersistentClient(
    path=str(settings.chroma_dir)).get_collection(settings.collection_name)
eng._vi_sections = None
m = eng._vi_section_map()
ct = {k for k in m if k.startswith("C") and k[1:].isdigit()}
print(f"total={len(m)} ct={len(ct)} var={len(m) - len(ct)}")
PY
```
输出: `total=159 ct=135 var=24` —— 与索引实际的 `§三 135 + §一 24` 逐位相符 (域变量表 63 未进表, 符合设计)。

### 3.2 检索闸 + 逐题配对 diff

前后两份 report 均已落盘 (规则 B), 配对 diff 可**从工件复算, 不必 revert 重跑**:

| 工件 | 生成方式 |
|---|---|
| `evidence/checkpoints/s1_vi_after.json` | `.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup --output evidence/checkpoints/s1_vi_after.json` |
| `evidence/checkpoints/s1_vi_before.json` | 同上, 但先把字面通道 monkeypatch 回旧行为 (见下) |

```bash
# "改动前" 的复现: 字面通道退回"整文件 cosine 取 1 块", 其余逐字节不变
cd sdtm-rag && .venv/bin/python - <<'PY'
import sys
from server.rag import RAGEngine
RAGEngine._lookup_chunks_for_variable_index = (
    lambda self, query, query_embedding=None: self._lookup_chunks_for_file(
        query, self._VARIABLE_INDEX_REL, 1, query_embedding=query_embedding))
from eval.run_eval import main
sys.exit(main(["eval/test_set_v3.yml", "--retrieval-only", "--hybrid",
               "--structured-lookup", "--output",
               "evidence/checkpoints/s1_vi_before.json"]))
PY
```

| 口径 | 140 题 | 18 题 VI 子集 | 其余 122 题 |
|---|---|---|---|
| 改动前 (section 级) | 95.71% | 75.00% | 98.77% |
| 改动后 (section 级) | **98.93%** | **100.00%** | **98.77%** (逐位不变) |
| Δ | +3.21 pt | +25.00 pt | **0** |

18 题逐题:

| qid | 前 | 后 | | qid | 前 | 后 |
|---|---|---|---|---|---|---|
| q07 | 1.00 | 1.00 | | q106 | 1.00 | 1.00 |
| q34 | 1.00 | 1.00 | | **q107** | **0.50** | **1.00** |
| q66 | 1.00 | 1.00 | | **q108** | **0.00** | **1.00** |
| q67 | 1.00 | 1.00 | | **q109** | **0.00** | **1.00** |
| q68 | 1.00 | 1.00 | | **q110** | **0.00** | **1.00** |
| q69 | 1.00 | 1.00 | | q111 | 1.00 | 1.00 |
| q71 | 1.00 | 1.00 | | **q112** | **0.00** | **1.00** |
| q77 | 1.00 | 1.00 | | | | |
| q103-q105 | 1.00 | 1.00 | | | | |

**5 题上升, 0 题回归**; 另 13 道原本靠 cosine 恰好选对的题, 改走字面通道后仍全部命中 gold section。

全集剩余 2 道 miss 与本次无关: `q38: 0.0` (chapters 整文件单块, kickoff §2.A) /
`q126: 0.5` (已归档 permanent known limit)。

> 计划里预估的上限写作 98.57%, 实测 98.93% —— 差值来自把 q126 当成整题 miss 计, 实际它是 0.5 半命中。
> 预估偏保守, 非实现超出预期。

### 3.3 语义核验 (注入块正文真能回答, 不只是 recall 数字好看)

生产同配置在进程内起引擎直接 `retrieve()` (零 LLM 开销):

```bash
cd sdtm-rag && .venv/bin/python - <<'PY'
from server.config import settings as s
from server.rag import RAGEngine
eng = RAGEngine(chroma_dir=s.chroma_dir, kb_root=s.kb_root, collection_name=s.collection_name,
    embedding_model=s.embedding_model, top_k=s.top_k,
    structured_lookup_enabled=s.structured_lookup_enabled, hybrid_enabled=s.hybrid_enabled,
    hybrid_fusion=s.hybrid_fusion, hybrid_alpha=s.hybrid_alpha, hybrid_pool=s.hybrid_pool,
    prompt_guardrail_enabled=s.prompt_guardrail_enabled)
q = ("We need to report left/right/bilateral consistently wherever anatomical side is "
     "collected. Which domain variables reference the Laterality codelist C99073?")
for c in eng.retrieve(q):
    if c.via_lookup and c.source.endswith("VARIABLE_INDEX.md"):
        print(c.section, "|", c.text[:120].replace(chr(10), " "))
PY
```

| qid | 注入 section | 正文 |
|---|---|---|
| q107 | `§一 通用变量: ARM` + `§一 通用变量: ARMCD` (**两块**) | 各含 label 与 "Appears in 3 SDTM domains: DM, TA, TV" |
| q108 | `§三 CT 交叉引用: C66729` | 6 变量含 gold 要的 CM.CMROUTE / EX.EXROUTE / SU.SUROUTE |
| **q109** | `§三 CT 交叉引用: C99073` | 17 变量含 gold 要的 TU.TULAT / FA.FALAT / PE.PELAT (**TU.TULAT 在第 15 位 = 截断边界, 零余量**, 见已知限制 1) |
| q110 | `§三 CT 交叉引用: C78734` | 11 变量含 gold 要的 RELSPEC.SPEC / LB.LBSPEC / PC.PCSPEC |
| q112 | `§三 CT 交叉引用: C78736` | 5 变量含 gold 要的 LB.LBNRIND / IS.ISNRIND / OE.OENRIND |

q109 是本轮**最有说服力的判别样本**: 同一道题, 旧口径召回 C66734 (RDOMAIN, 与侧别无关),
新口径召回 C99073 —— 分数变化说明不了的事, 这条 section 名的变化说得清。

抽检方独立复核 N=11 (超 N≥6 要求), 逐题结论: **11 题语义均成立**, 注入正文真能回答, 非只是
section 名对上。其中 q34 / q68 判 PARTIAL —— VI §三 正文只列变量名不写码表名 ('NY' / 'Completion
Status' 不在 VI 块里), 由全上下文其他 chunk 补齐, 已复核 in-full-context=True。

q107 注入两块这件事本身就是"1 文件只注 1 块"限制的解除 —— 该题旧口径下结构上拿不到满分。

### 3.4 全量测试

```bash
cd sdtm-rag && .venv/bin/python -m pytest -p no:warnings 2>&1 | tail -1
```
`844 passed` (改动前 823, 新增 21 = 锚点 8 + 映射 6 + 注入 7)。

## 4. 已知限制

1. **VI §三 正文在 15 个变量处截断** (`... (N total)`), **非本轮引入, 但直接影响"100%"的读法**。
   宽码表 (C66742 有 123 个引用 / C71620 有 58 个) 的注入正文**结构上答不全**"哪些变量引用该码表"。
   section 级 source recall 对此**零判别力** —— 它只看 section 名对不对, 不看正文是否被截断。
   实测: q109 的 `TU.TULAT` 与 q69 的 `EX.EXDOSU` 都恰好压在**第 15 位**过关, **零余量**;
   C99073 被截掉的是 `UR.URLAT` 与 `VS.VSLAT` (`knowledge_base/VARIABLE_INDEX.md:2002`)。
   **修 VI ingest 的截断之前, 禁止把"18 题 100%"读作"VI 类问题已解决"。**
2. **锚点上限 3 的余量已耗尽 (非"无此形态")**: q104 的 anchors 恰好是 `['VISIT','VISITNUM','VISITDY']`
   = 打满上限, 且 gold `VISITDY` 落在第 3 位。题面再多点一个能解出 section 的变量, 该题就会失守。
   > 早先本条写作"当前题集无此形态", 属**事实错误**, 由规则 A 抽检推翻 (D-2)。
   > 修正前的锚点饥饿缺陷 (D-1: 上限截断发生在 section 解析之前) 已修, 见 §5。
3. **变量锚点依赖 `_query_variables` 的已知变量表** —— 表外变量不 fire, 回落 cosine。
4. **域变量表族 (63 chunk) 未覆盖** —— 设计上交给 `domains/<CODE>/spec.md` 通道, 未实测该假设是否
   对所有域码问句成立。
5. **回落纪律的准确措辞是"锚点命中即接管, 全落空才回落"**, 不是"只能赢不能输"。只要有一个锚点
   解出 section, 字面通道就接管该文件的注入名额, 即便 cosine 那一块本来更贴题。v3 实测未咬人
   (18/18 命中, 122 题 Δ0), 但改动它仍需逐题配对 diff 验收。
6. **回落路径仍是旧缺陷**: 未 fire 字面通道的 VI 问句, 选块质量与改动前完全相同。本次修的是
   "题面点名了码/变量"的那一类, 不是 VI 的全部问句。
7. **launchd 服务需重启才生效** —— 本次验证全部在进程内 / eval 侧完成; localhost:8000 上跑的仍是旧码。

## 5. 三方隔离 (规则 D)

| 角色 | 承担 | 首轮裁定 | 复审 |
|---|---|---|---|
| 实现 | 主 session | — | — |
| 审查 | `oh-my-claudecode:code-reviewer` (opus) | **REVISE** (2 HIGH / 3 MEDIUM / 5 LOW) | **APPROVE** |
| 抽检/验收 (规则 A, 抽样总体 = 18 题变更集) | `oh-my-claudecode:verifier` (opus) | **PASS** (代码/数字) + **REQUEST_CHANGES** (文档 3 项) | — |

**三方各自抓到了对方看不见的东西** —— 实现方自查全绿, 审查方与抽检方各抓到一条实现方漏掉的真缺陷,
且两者互不重叠 (抽检方查数字与语义, 抓到锚点饥饿; 审查方查失败模式落点, 抓到部署路径 502)。

### 5.1 抽检方 (规则 A) 的独立复算

抽检方**不信实现方的工件**, 自建基线 (monkeypatch 关掉字面通道) 重跑后逐位复算:

| 口径 | 实现方声称 | 抽检方独立复算 | 对齐 |
|---|---|---|---|
| 18 题子集 | 75.00% → 100.00% | 75.0000% → 100.0000% | ✅ |
| 其余 122 题 | 98.77% 逐位不变 | 98.7705% → 98.7705%, **逐题相同=True** | ✅ 不是均值巧合 |
| 全集 | 95.71% → 98.93% | 95.7143% → 98.9286% | ✅ |
| pytest | 823 → 844 | 844, 0 failed / 0 skipped | ✅ |

另核实: **18/18 全部 fire 字面通道**, 且 18 题的 gold section 全部由 `via_lookup=True` 的注入块
命中 (rank 0-2) —— 不存在"满分但通道空转"的题。但其中 **13 题在关闭新通道的基线下同样是 1.00**,
即**新通道的净增益只在 5 题**, 另 13 分是被接管而非挣来的。

### 5.2 修复清单 (全部已落地)

| 编号 | 来源 | 问题 | 修法 |
|---|---|---|---|
| **D-1** | 抽检 | **锚点饥饿**: 上限 3 的截断发生在 section 解析**之前**。`known_variables` 有 ~1500 个变量而 VI §一 只有 24 个有 section, 于是无 VI 条目的变量白占名额。实证: q107 题面加一句 "our EXDOSU and CMDOSU mappings aside" 就把 ARMCD 挤出字面通道 | **先 resolve 再 cap**: 常量移到 `RAGEngine._MAX_VI_SECTIONS`, 施加在 section 解析之后。新增 2 条测试, 其中一条断言"活下来的是能解出 section 的前 N 个"(旧 `test_capped_at_max` 只断言 `len==3`, 正是该缺陷的盲区) |
| **HIGH-1** | 审查 | **部署路径上必触发的 502**: `deploy.sh` 把 `data/chroma` 与 `knowledge_base` 一起拷到新目录, 但 chroma 里存的仍是构建树绝对路径 → 映射为空 → 请求期 raise → 140 题里 **71 题**走这条路, 全部 502, 且缓存永不赋值故每次都炸。改动前同样错配下是静默退化但**服务照常出答案** | 把响亮失败从**请求期**挪到**启动期**: `main.py` lifespan 在 S1 开着时预热 `_vi_section_map()`。部署错配在 launchd 启动即失败并写进 `api.launchd.log`, 而不是用户收到偶发 502。预热成功后表已缓存, 请求期那条 raise 不可达 |
| **HIGH-2** | 审查 | **guard 口径错位**: `if not mapping` 拦住了不可能发生的情况, 放过了真会发生的 —— §一 与 §三 由 chunker 两段独立代码生成, 只改一族完全现实; §一 改名后 24 个变量键全丢而 135 个 CT 键还在 → 非空 → 不 raise → 变量锚点题静默回落 cosine | ① 运行时 guard 改为**两族都必须在**; ② 新增 CI 漂移闸 `test_vi_section_map_matches_chunker_output` —— 现场跑 chunker 再与索引映射逐键比对, **不硬编码 135/24** 故 KB 增删 CT 码不误报, 而任一族命名漂移当场红。计划里那条一次性 shell 验证不在 CI 里、不会再跑, 这条是它的常驻替身 |
| MEDIUM-1 | 审查 | "只能赢不能输"的措辞强于代码保证 | docstring 与 §4 改为准确措辞: **锚点命中即接管, 全落空才回落** |
| MEDIUM-2 | 审查 | 验收"前"半边无持久工件, Δ0 声明只能靠 revert 重跑 | 前后两份 report 落盘 `evidence/checkpoints/s1_vi_{before,after}.json` + 复现命令入档 (§3.2) |
| MEDIUM-3 | 审查 | 缺"回落路径不得碰映射表"的负面测试 —— 若有人把 `_vi_section_map()` 上提到早退之前, 用健康 metas 的回落测试**照样绿**, 而生产开始对每道无锚点题 raise | 新增 `test_broken_map_does_not_break_the_no_anchor_path` (用建不出表的索引锁住) |
| LOW-1 | 审查 | `^(C\d{4,6}\|[A-Z][A-Z0-9]{1,})$` 第一分支是死代码 (CT 码已被第二分支覆盖), 读起来像做了长度校验实际没有 | 拆成两个各自承重的模式: `_VI_ANCHOR_RE` 管接受, `_VI_CT_RE` 管两族完整性分类 |
| LOW-2 | 审查 | `setdefault` 的先到先得依赖 Chroma `get()` 未定义的返回顺序 | 同尾 token 冲突时 raise (命名约定歧义应当响亮), 新增测试 |
| D-2 | 抽检 | checkpoint 已知限制 #2 写"当前题集无此形态"是**事实错误** —— q104 的 anchors 恰好打满 3 且 gold 在第 3 位 = 零余量 | 已改写 (见 §4.2)。这正是"写错的实测比缺陷更害人"那一类 |
| D-3 | 抽检 | VI §三 正文在 15 变量处截断, section 级判据对此**零判别力** | 入档为已知限制 1, 并明写禁止把"18 题 100%"读作"VI 类问题已解决" |
| LOW-3/4/5 | 审查 | 缓存无失效/无锁 (与既有 `_bm25` 同构) · 新测试文件 1 条 ruff I001 (`scripts/tests/` 既有 28 条) · 注入预算注释在 `top_k=5` 下不成立 | 仅记录, 未改。`server/` 三个改动文件 ruff **零新增** (改动前后同为 2 条) |

**审查方点名的"study 引擎不得走 S1"接线测试**: 复查发现既有
`test_enabled_injects_study_lookup_into_study_engine` 已含 `assert study["structured_lookup_enabled"] is False`,
该条已被锁住, 未重复添加。

### 5.3 复审 (APPROVE) — 两条 HIGH 均为**实证消除**, 非读码认可

审查方对自己提的修法做了独立实证:

- **HIGH-1 落点确认**: 用一个必抛的 lifespan 跑真 uvicorn → `EXIT_CODE=3` + 端口 `000 (connection refused)`
  + `Application startup failed. Exiting.` 全文入日志。配 plist 的 `KeepAlive=true` / `ThrottleInterval=10`,
  部署错配的表现是**每 10 秒崩溃重启一次、端口始终拒连**, 而非"起来但坏"。对比修复前: 服务正常起,
  只有 71/140 类问句 502, 运维只看到"偶发 502"。
- **HIGH-2 两闸互锁无缝** (对真 KB + 真索引三场实证):

  | 场景 | chunker 键 | 索引键 | 结果 |
  |---|---|---|---|
  | 今天 | 159 | 159 | 相等 → 绿 |
  | §一 改名, **未重灌** | 135 | 159 | 不等 → **漂移闸红** |
  | §一 改名, **已重灌** | 135 | 135 | 相等, 但 `_vi_section_map()` 在 assert 表达式里求值 → **运行时 guard raise** → pytest ERROR |

  第三行那个"相等但仍红"的接缝是关键 —— 两半之间没有夹缝。**KB 合法增删 CT 码不误报** (chunker
  与索引同源同变); 只有"改了 KB 没重灌"会红, 那是真阳性。
- **D-1 修法无新引入问题**: `variable_index_anchors` 全仓只有 1 个调用方 (无别处依赖旧的"已截断"契约);
  `sections` 不会重复 (section→token 是函数故 token→section 双射); v3 全集锚点数均 ≤3, 故本轮
  resolve-then-cap 与 cap-then-resolve 结果同一 (修的是**将来**会咬人的形状)。
- **stub 不构成"过度配合实现"**: `vi_map_calls` 只由生产代码那一次调用递增 (删掉预热即红);
  guard 有自己专属的敌意测试打在真 `_engine()` 上, 职责不重叠。

复审剩余 finding, **均已当场修掉**:

| 严重度 | 问题 | 修法 |
|---|---|---|
| MEDIUM | 漂移闸硬依赖 gitignore 掉的 `data/chroma`, 且本仓**没有 CI** (`.github/workflows` 不存在) —— 同事 clone 后这条是 **ERROR 不是 skip**, 会训练所有人"这条红了不用管", 恰好毁掉闸的意义。既有先例 `TestMetaKBDriftGuard` 读的是已入 git 的 `meta.yaml`; 这是**第一条要求生产 chroma 库的测试** | 只在**打不开库**时 `pytest.skip` 并给出重灌命令; **assert 本身绝不 skip**, 任何能跑服务的机器上闸全效 |
| LOW | "请求期那条 raise 不可达"只对 server 成立 —— `eval/run_eval.py` 与 `eval/prod_wirein/*` 直接构造 `RAGEngine` 不走 lifespan, 仍会撞上它 (那对批处理正是想要的行为) | 注释收窄为"server 路径下不可达", 并写明**删了 eval 侧就退回静默降级** |
| LOW | `assert study["structured_lookup_enabled"] is False` 是搭在 S2 注入测试里的断言; 预热落地后, 丢掉这把锁的后果从"study 侧静默退化"升级成"**启动即崩**" (study collection 里 VI 行数为 0) | 该行上方加注释"这行不是搭车, 重构 S2 时别删"+ 后果说明 |
| — (观察) | go-live 缺"确认服务真起来了"这一步 | `deploy/README.md` 新增步骤 5: `launchctl list \| grep com.sdtmrag.api` 的 last-exit-status 必须为 0, 并写明最常见死因 (只 rsync `data/chroma` 而不在服务目录重灌) 与解法 |

### 5.4 修复后复验 (零回归)

```bash
cd sdtm-rag && .venv/bin/python -m pytest -p no:warnings 2>&1 | tail -1   # 852 passed
```
- 全量测试 823 → **852** (+29; 首轮 21 + 修复轮 8)
- 检索三个数在修复后**逐位不变**: 全集 98.9286% / 18 题 100.0% / 122 题 98.7705% 逐题相同
- D-1 修复在真引擎上复验: 抽检方的反例变体现在两块都走字面通道 (修前只注入 ARM)

## 6. 复跑

```bash
cd sdtm-rag
.venv/bin/python -m pytest -p no:warnings 2>&1 | tail -1          # 852 passed
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml \
    --retrieval-only --hybrid --structured-lookup                 # 98.93% (section 级判据)
```

配对 diff 从已落盘工件复算 (不必重跑):

```bash
cd sdtm-rag && .venv/bin/python - <<'PY'
import json
load = lambda p: {x["id"]: x["source_recall"]
                  for x in (lambda d: d["results"] if isinstance(d, dict) else d)(json.load(open(p)))}
b, a = load("evidence/checkpoints/s1_vi_before.json"), load("evidence/checkpoints/s1_vi_after.json")
VI18 = ["q07","q34","q66","q67","q68","q69","q71","q77","q103","q104","q105","q106",
        "q107","q108","q109","q110","q111","q112"]
f = lambda d, ks: round(sum(d[k] for k in ks)/len(ks)*100, 4)
rest = [k for k in a if k not in set(VI18)]
print(f"全集 {f(b,list(a))} -> {f(a,list(a))} | 18题 {f(b,VI18)} -> {f(a,VI18)} | "
      f"122题 {f(b,rest)} -> {f(a,rest)} 逐位相同={all(b[k]==a[k] for k in rest)}")
print("变化题:", {k: (b[k], a[k]) for k in a if b[k] != a[k]})
PY
# 全集 95.7143 -> 98.9286 | 18题 75.0 -> 100.0 | 122题 98.7705 -> 98.7705 逐位相同=True
# 变化题: {'q107': (0.5, 1.0), 'q108': (0.0, 1.0), 'q109': (0.0, 1.0), 'q110': (0.0, 1.0), 'q112': (0.0, 1.0)}
```
