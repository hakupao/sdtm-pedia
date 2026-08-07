# chapters 切分策略 — 取消「整文件单块」档 (Task 8, 2026-08-07)

> 结论: `ChaptersChunker` 由三档改两档。ch01/ch02/ch03 从各 1 个整文件块变为按 H2 切
> (5 / 9 / 3)。索引 **4315 → 4329 (+14)**。140 题 gold **逐题零变化** (avg 0.9917 → 0.9917)。
> 层① `whole_file` 簇头消失, 且**这一次取样里未见任何新簇头** (单次快照口径, 见 §6)。
>
> **这份证据不能证明什么**: 它**没有**解决 q38 —— ch02 仍未进 top-15, 见 §6。
> 切分是结构改善, 不是 q38 的修复。

改动: `scripts/chunkers/chapters.py`(策略) + `scripts/tests/test_chapters.py`(锁)。

---

## 1. Before (改动前的基线)

```bash
cd sdtm-rag
.venv/bin/python -c "
from pathlib import Path
from scripts.chunkers.chapters import ChaptersChunker
kb = Path('../knowledge_base').resolve()
ck = ChaptersChunker(kb)
for f in sorted((kb / 'chapters').glob('*.md')):
    n_h2 = sum(1 for line in f.read_text(encoding='utf-8').splitlines() if line.startswith('## '))
    n_h3 = sum(1 for line in f.read_text(encoding='utf-8').splitlines() if line.startswith('### '))
    print(f'{f.name:35s} {f.stat().st_size:7d} B  H2={n_h2:2d} H3={n_h3:3d} -> {len(ck.chunk(f)):3d} chunks')"
```

实测输出 (git 9a73b57, 改动前):

```
ch01_introduction.md                  11070 B  H2= 5 H3=  4 ->   1 chunks
ch02_fundamentals.md                  18141 B  H2= 9 H3= 11 ->   1 chunks
ch03_submitting_data.md               19708 B  H2= 3 H3=  3 ->   1 chunks
ch04_general_assumptions.md          130532 B  H2= 7 H3= 47 ->  47 chunks
ch08_relationships.md                 51764 B  H2= 9 H3= 19 ->  19 chunks
ch10_appendices.md                    30233 B  H2= 7 H3= 12 ->   7 chunks
```

同期基线:

| 项 | 值 | 取数命令 |
|----|----|---------|
| `chunk_count` | **4315** | `curl -s localhost:8000/api/info` |
| chapter 类 chunk | 76 | chroma `where={'file_type':'chapter'}` |
| 全套 pytest | **951 passed, 0 failed, 0 skipped** | `pytest -q --junit-xml=/tmp/j_before.xml` |
| 140 题 source_recall_avg | **0.9917** | `evidence/checkpoints/gold_integrity_after.json` |

> pytest 末行统计在本 repo 会被吞, 一律读 junit xml:
> `.venv/bin/python -c "import xml.etree.ElementTree as ET;print(ET.parse('/tmp/j_before.xml').getroot().find('testsuite').attrib)"`

---

## 2. 改了什么

**策略**: 三档 → 两档 + 回落。

```
- size_bytes > 50KB          → `^### ` (H3)   ★ L-4 锁, 未动
- 20KB < size_bytes ≤ 50KB   → `^## `  (H2)
- size_bytes ≤ 20KB          → 整文件 1 块     ← 取消
+ size_bytes > 50KB          → `^### ` (H3)   ★ L-4 锁, 未动
+ 否则                        → `^## `  (H2); 无 H2 时回落整文件单块
```

被取消的那档为什么该取消: ch02 (18KB) 整章压成一个向量, 9 个主题共用一条 embedding,
任何一个主题的信号都被另外 8 个稀释。ch03 更荒谬 —— 19708 B, 差 **676 B** 就落进 H2 档,
分档边界纯属偶然。

**测试**: 原先锁死该档的两条被替换, 不是删除 ——

| 动作 | 测试 | 理由 |
|------|------|------|
| 删 | `test_ch01_produces_1_chunk` | 锁的是被取消的那一档, 策略变了它就是错的锁 |
| 删 | `test_ch01_section_is_whole_file` | 同上 |
| 增 | `test_ch01_splits_by_h2` | 新策略的等强度锁 (==5, 且无 whole_file) |
| 增 | `test_ch01_sections_carry_real_headings` | 锁 section 名是真标题 (1.1 / 1.5), 不是空串 |
| 增 | `test_ch02_splits_by_h2` | ==9, 且 §2.6 在 (q38 要的那一半) |
| 增 | `test_ch03_splits_by_h2` | ==3 |
| 增 | `test_file_without_headings_still_falls_back_to_whole_file` | **回落分支现在是唯一兜底**, 之前被 ≤20KB 档遮住从没被单独测过 |
| 增 | `test_large_chapter_still_splits_by_h3` | L-4 反向锁: 本改动不得动 ch04 |
| 增¹ | `test_every_chapter_chunk_under_embedding_limit` | **全量** token 上限闸, 见 §9 |
| 未动 | `test_ch04_produces_47_chunks` / `test_ch08_produces_19_chunks` | L-4, 不许动 |

¹ 评审后补 (Minor 2)。

断言值 5 / 9 / 3 是 §3 命令跑出来的真实块数, 与 H2 计数一致 (无"首个 H2 前的前言另成一块"
的情况, 原因见 §7)。**没有**用 `> 1` 之类的弱断言顶替。

---

## 3. After (改动后, 同一条命令)

```
ch01_introduction.md                  11070 B  H2= 5  ->   5 chunks  maxtok=1026
      - 1.1 Purpose
      - 1.2 Organization of this Document
      - 1.3 Relationship to Prior CDISC Documents
      - 1.4 How to Read this Implementation Guide
      - 1.5 Known Issues
ch02_fundamentals.md                  18141 B  H2= 9  ->   9 chunks  maxtok=805
      - Section 1 Context (Reference Material)
      - 2.1 Observations and Variables
      - 2.2 Datasets and Domains
      - 2.3 The General Observation Classes
      - 2.4 Datasets Other than General Observation Class Domains
      - 2.5 The SDTM Standard Domain Models
      - 2.6 Creating a New Domain
      - 2.7 SDTM Variables Not Allowed in the SDTMIG
      - Findings About — Naming Findings About Domains (Reference Material)
ch03_submitting_data.md               19708 B  H2= 3  ->   3 chunks  maxtok=4400
      - 3.1 Standard Metadata for Dataset Contents and Attributes
      - 3.2 Using the CDISC Domain Models in Regulatory Submissions — Dataset Metadata
      - 3.2.2 Conformance
ch04_general_assumptions.md          130532 B  H2= 7  ->  47 chunks  maxtok=3852
ch08_relationships.md                 51764 B  H2= 9  ->  19 chunks  maxtok=1418
ch10_appendices.md                    30233 B  H2= 7  ->   7 chunks  maxtok=4095
```

L-4 未被破坏: ch04 仍 47 块 / maxtok 3852 < 8000。新块最大 4400 tok (ch03 §3.2), 远低于
8191 embedding 上限。

---

## 4. 重灌索引

```bash
.venv/bin/python -m scripts.ingest 2>&1 | tail -25
launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api      # 服务持有 chroma 句柄, 必须重启
curl -s localhost:8000/api/info | .venv/bin/python -m json.tool | head -20
```

```
[chroma] collection 'sdtm_kb_v1' total = 4329
[done] total files chunked, 4329 chunks, 2,548,989 tokens, wallclock 105.9s, Chroma 224.3 MB
```

`/api/info` 实测: `"chunk_count": 4329`, `"index_fresh": true`,
`"index_freshness_reason": "index is in sync with knowledge_base"`。

**4315 → 4329 (+14) 是恒等式而非巧合**: chapters 由 76 → 90 块 (`+14`),
即 ch01 `1→5` (+4) + ch02 `1→9` (+8) + ch03 `1→3` (+2)。其余文件类型一块没动。

```bash
.venv/bin/python -c "
import chromadb; from pathlib import Path; from collections import Counter
col=chromadb.PersistentClient(path=str(Path('data/chroma').resolve())).get_collection('sdtm_kb_v1')
print('count', col.count())
print('whole_file chunks:', len(col.get(where={'section':'whole_file'})['ids']))
r=col.get(where={'file_type':'chapter'}, include=['metadatas'])
print('chapter chunks:', len(r['ids']), Counter(m['source'].split('/')[-1] for m in r['metadatas']))"
```
```
count 4329
whole_file chunks: 0
chapter chunks: 90 Counter({'ch04...': 47, 'ch08...': 19, 'ch02...': 9, 'ch10...': 7, 'ch01...': 5, 'ch03...': 3})
```

`section == "whole_file"` 在索引里**已归零** —— 之前只有 ch01/ch02/ch03 三条用它。
回落分支本身仍在代码里且有单测覆盖, 只是当前 KB 没有无 H2 的 chapter 文件触发它。

`reconcile_meta` 全 OK (8/8: 63 域 / 1917 变量条目 / 1523 变量名 / 1005 码表 / 37939 术语 /
TAETORD 43 / VISITDY 36 / raw_order 1917)。

---

## 5. 140 题零回归 (逐题, 不是只看平均)

```bash
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --hybrid \
  --structured-lookup --output evidence/checkpoints/chapters_split_after.json
```

逐题对照 (基线 `gold_integrity_after.json`):

```bash
.venv/bin/python -c "
import json
b=json.load(open('evidence/checkpoints/gold_integrity_after.json',encoding='utf-8'))
a=json.load(open('evidence/checkpoints/chapters_split_after.json',encoding='utf-8'))
bm={r['id']:r for r in b['results']}; am={r['id']:r for r in a['results']}
assert set(bm)==set(am)
n_rec=n_miss=n_hit=n_top5=0
for i in bm:
    rb,ra=bm[i],am[i]
    if rb['source_recall']!=ra['source_recall']: n_rec+=1; print('RECALL',i,rb['source_recall'],'->',ra['source_recall'])
    if sorted(rb['source_misses'])!=sorted(ra['source_misses']): n_miss+=1
    if sorted(rb['source_hits'])!=sorted(ra['source_hits']): n_hit+=1
    if rb['top5_sources']!=ra['top5_sources']: n_top5+=1
print('changed: recall=%d misses=%d hits=%d top5=%d / 140'%(n_rec,n_miss,n_hit,n_top5))
print('avg:', b['summary']['source_recall_avg'], '->', a['summary']['source_recall_avg'])"
```
```
changed: recall=0 misses=0 hits=0 top5=39 / 140
avg: 0.9917 -> 0.9917
```

- **`source_recall` / `source_hits` / `source_misses` 逐题 140/140 完全相同, 零下降零上升。**
  分类分解也逐位相同 (concept 0.9733 / cross_domain 0.99 / mixed 1.0 / single_domain 1.0)。
- 仍 miss 的两题与改动前**同一批同一条**: q38 (33%, miss `chapters/ch02` +
  `ch04#4.2.2`) 与 q126 (50%, miss `domains/TE/spec.md`, 已登记的永久 known limit)。
- **top5 成分 39/140 变了但判分一分没动**: 索引重灌本就会重排 (topk_jitter §4: 排位不可复现),
  且新增 14 块进了池子。**成分变而判分不变**恰恰说明变动发生在判分不敏感的位置。

> ⚠ 这条证据能证明"切分没打坏任何一题的 gold 命中";
> **不能**证明"答案质量没变"—— 它是 retrieval-only, 不出答案。答案侧要看层②。

### 5.1 闸的状态: passed 而非 skipped

`test_section_gold_exists.py` 在无索引时会 `pytest.skip` —— **skip 被当成绿是这类闸最常见
的失效方式**。实测它是真跑了:

```bash
.venv/bin/python -m pytest scripts/tests/test_section_gold_exists.py -v
# scripts/tests/test_section_gold_exists.py ..                    [100%]
# 2 passed
.venv/bin/python -c "
import sys; sys.path.insert(0,'.')
from scripts.tests.test_section_gold_exists import _section_golds
g=_section_golds(); print(len(g),'golds over',len({q for q,_ in g}),'questions')"
# 49 golds over 37 questions
```

全套 957 条里 **skipped=0**, 所以不存在"别处偷偷 skip"。49 条 section 级 gold 在新索引的
section 命名下全部仍可解析 —— 即 H2 切分**没有**改动任何既有 gold 依赖的 section 名
(它们指向的是 domains/ 与 ch04/ch08, 不在本次改动的三个文件里)。

---

## 6. 层①: 有没有制造出新的同质簇 (这是本 task 的主要风险)

```bash
.venv/bin/python -m eval.crowding_probe --output evidence/checkpoints/crowding_layer1_after_split.json
```

| 指标 (140 题, k=15) | before | after |
|---|---|---|
| mean `max_cluster` | 2.300 | **2.157** |
| mean `dup_seats` | 1.729 | **1.471** |
| mean `distinct_sections` | 13.271 | **13.529** |
| `max_cluster ≥ 3` 的题数 | 40 | **33** |
| `max_cluster ≥ 5` | 11 | 11 |
| `max_cluster ≥ 8` | 3 | 3 |

**新簇普查** (不止看簇头 —— 看**任何**在某题 top-15 里占 ≥2 席的 section 名):

```bash
.venv/bin/python -c "
import json; from collections import Counter
b=json.load(open('evidence/checkpoints/crowding_layer1.json',encoding='utf-8'))
a=json.load(open('evidence/checkpoints/crowding_layer1_after_split.json',encoding='utf-8'))
def clusters(rows):
    out=Counter()
    for r in rows:
        c=Counter(e['section'] for e in r['composition'])
        for sec,n in c.items():
            if n>=2: out[sec]+=1
    return out
cb,ca=clusters(b),clusters(a)
print('NEW:', {k:v for k,v in ca.items() if k not in cb})
print('GONE:', {k:v for k,v in cb.items() if k not in ca})"
```
```
NEW: {}
GONE: {'whole_file': 23, 'TAETORD': 1}
```

**这一次取样里没见到新簇 (0 个)。**

> ⚠ **口径限定**: 上面的普查是**单次快照**, 前后各跑一遍。而本轮自己的结论是 top-15 的
> **成分跨进程会变** (topk_jitter §0.1 / §4)。所以严格说法是「**这一次取样里没见到新簇**」,
> 不是「不存在新簇」—— 一个只在少数进程状态下才成形的簇, 单次快照照不出来。
> 支撑这个结论的不止快照: §6.1 的 3 题 × 20 进程跨进程取样里也没见到新簇头, 且
> `whole_file` 已从索引里**结构性归零** (0 条 chunk), 它不可能以任何进程状态回来。
> 但"其他 section 名会不会在别的进程状态下成新簇"这一问, 本证据**没有**回答。

`whole_file` 原本在 **23 题**的 top-15 里占 ≥2 席 —— 那是个纯人造簇:
ch01/ch02/ch03 三个**内容毫不相干**的整章共用同一个 section 名, 按字面被认成同质簇。
切完之后它彻底消失, 且没有任何新名字顶上来。

ch01/02/03 在全部 140 题 top-15 里占的席位: ch01 26→33, ch02 **48→98**, ch03 15→23。
ch02 席位翻倍且现在分散在 9 个**不同**的真实小节名下 —— 从"一个稀释块偶尔挤进来"变成
"多个具体小节各自按相关性竞争"。

### 6.1 `max_cluster` 豁免: 重灌索引已使其失效, 已重测

`topk_jitter.md` §5.6 明列失效条件 3「Task 8 重灌索引」与 4「改 chunk 切分」——
**两条本次都触发了**, 所以上表的 after 数字是重测值, **不是**沿用。豁免的机制前提
(「正文逐字节相同 ⇒ section 相同 ⇒ 抖动天然在簇内部」) 在重灌后重新验证:

```bash
.venv/bin/python -m eval.crowding_probe --cross-process 20 --ids q38,q47,q117 \
  --stability-output evidence/checkpoints/crowding_layer1_stability_after_split.json
```

| 题 | before (20 进程) | after (20 进程) |
|---|---|---|
| q38 | 1 种取值 `(14,13,2)`×20; `distinct_sets=3`, `sometimes=4` | 1 种取值 `(14,13,2)`×20; **`distinct_sets=1`, `sometimes=0`** |
| q47 | 2 种: `(2,2,13)`×12 \| `(2,1,14)`×8 | 2 种: `(2,2,13)`×14 \| `(2,1,14)`×6 (**同样两个取值**) |
| q117 | 1 种: `(2,2,13)`×20 | 1 种: **`(2,1,14)`**×20 |

读法:
- q38 **变得更稳**: 成分种类 3→1, churn 归零 —— 原来的 churn 成员之一正是那个飘忽的
  ch02 whole_file 块, 切开后它不再挤在切割线上。
- q47 取值集合**不变**, 只是 20 次里的次数从 12:8 变 14:6。按该文件 `_meta` 自己的告诫,
  **20 次的次数不是概率**, 这个差不可读作"更稳了"。
- q117 **取值变了** (`dup_seats` 2→1, `distinct` 13→14) 但仍 1 种取值 —— 少掉的那个重复席位
  就是 whole_file。这是**值的变化, 不是稳定性的变化**。

⚠ **本节的可引用边界**: 三题 × 20 进程只够说"见到 N 种状态", 不足以刻画分布尾部;
`max_cluster_section` 在并列时是排位产物 (落盘行带 `max_cluster_section_tied`, 为 true
即不可引用)。上表并列情况未逐题核, 故只引用三元组数值, 不引用簇头名字。

### 6.2 这次改动**没有**解决 q38 —— 必须写清

brief 的动机是 q38: 「ch02 whole_file dense #71 sim 0.5613, 而 ch04 §4.2.2 是 #1 sim 0.6970」。
切完之后实测 (dense-only, top_k=150):

```bash
.venv/bin/python -c "
from eval.run_eval import load_test_set
from server.config import settings
from server.rag import RAGEngine
q=[x for x in load_test_set('eval/test_set_v3.yml') if x['id']=='q38'][0]
rag=RAGEngine(chroma_dir=settings.chroma_dir, kb_root=settings.kb_root,
              collection_name=settings.collection_name,
              embedding_model=settings.embedding_model, top_k=150)
for i,c in enumerate(rag.retrieve(q['question']),1):
    s=c.source.split('knowledge_base/')[-1]
    if s.startswith('chapters/ch02') or '4.2.2' in (c.section or ''):
        print(f'#{i:3d} sim={c.similarity} {s} § {c.section}')"
```
```
#  1 sim=0.697 chapters/ch04_general_assumptions.md § 4.2.2 Two-character Domain Identifier
# 63 sim=0.6477 chapters/ch02_fundamentals.md § 2.2 Datasets and Domains
# 64 sim=0.6405 chapters/ch02_fundamentals.md § 2.5 The SDTM Standard Domain Models
# 70 sim=0.5963 chapters/ch02_fundamentals.md § 2.6 Creating a New Domain
# 72 sim=0.5849 chapters/ch02_fundamentals.md § Section 1 Context (Reference Material)
# 73 sim=0.5747 chapters/ch02_fundamentals.md § 2.7 SDTM Variables Not Allowed in the SDTMIG
# 80 sim=0.5573 chapters/ch02_fundamentals.md § 2.4 Datasets Other than General Observation Class Domains
# 88 sim=0.5361 chapters/ch02_fundamentals.md § Findings About — Naming Findings About Domains (Reference Material)
# 93 sim=0.5302 chapters/ch02_fundamentals.md § 2.1 Observations and Variables
```

- ch02 的**最好**块从 #71 / 0.5613 提到 **#63 / 0.6477** (+0.086 sim, +8 位)。
- 但真正回答 q38 的 **§2.6 Creating a New Domain 在 #70 / 0.5963** —— 只比原 whole_file
  好 0.035, **仍然远在 top-15 之外**。q38 的 `source_recall` 因此**仍是 33%**, 未变。
- 原因: q38 的 top-15 被 **14 席 §DOMAIN 簇**占满 (层① `max_cluster=14`)。切分改善的是
  ch02 一侧的信号强度, 但席位是被另一侧吃掉的 —— 那是 Task 6 (去重/配额) 的辖区, 不是切分能修的。

> ⚠ 前值 `#71 / 0.5613` **是 brief 引述的既有诊断, 本 task 未复测** (旧索引已被覆盖)。
> 后值 #63/#70 是上面那条命令的实测。两者跨索引比较, 排位本身不可复现 (topk_jitter §4),
> 故"提了 8 位"只应读作数量级, 不应读作精确位移。

---

## 7. 已知副作用: 首个 H2 之前的前言不再入索引

H2 切分从第一个 `## ` 开始, 之前的内容不进任何 chunk。实测被丢弃的量:

```bash
.venv/bin/python -c "
import re; from pathlib import Path
kb=Path('../knowledge_base').resolve()
for n in ['ch01_introduction.md','ch02_fundamentals.md','ch03_submitting_data.md']:
    t=(kb/'chapters'/n).read_text(encoding='utf-8')
    m=re.search(r'^## ', t, re.M); print(n, m.start(), 'B of', len(t)); print('  ', repr(t[:m.start()]))"
```
```
ch01_introduction.md  86 B of 11058   '# SDTMIG v3.4 — Chapter 1: Introduction\n\nSource: SDTMIG v3.4, Section 1 (Pages 7-12)\n\n'
ch02_fundamentals.md  99 B of 18115   '# SDTMIG v3.4 — Chapter 2: Fundamentals of the SDTM\n\nSource: ... Section 2 (Pages 13-20)\n\n'
ch03_submitting_data.md 109 B of 19698 '# SDTMIG v3.4 — Chapter 3: ...\n\nSource: ... Section 3 (Pages 17-21)\n\n'
```

丢的是 H1 标题 + 一行页码溯源, 合计 86/99/109 B (占各文件 0.6% / 0.5% / 0.6%)。

- 这**不是本次引入的新缺陷**: ch04 / ch08 / ch10 一直如此 (它们从不在整块档里)。
  本改动只是把这个既有行为扩展到另外三个文件。
- 140 题零回归说明当前题集不依赖这三行。
- 但它是**真实的信息损失**: "Pages 13-20" 这类页码溯源在索引里对 ch01/02/03 消失了。
  若将来要按页码答题, 应在 chunker 里把前言 prepend 到首块 (块数仍为 5/9/3, 断言不受影响),
  而不是恢复整块档。**本 task 未做此改动 —— 超出 brief 范围, 且会让 ch01/02/03 与
  ch04/08/10 行为不一致, 应作为独立单元统一处理。**

---

## 8. 测试与 4315 的引用同步

```bash
.venv/bin/python -m pytest -q --junit-xml=/tmp/j_after.xml >/dev/null 2>&1
.venv/bin/python -c "import xml.etree.ElementTree as ET;print(ET.parse('/tmp/j_after.xml').getroot().find('testsuite').attrib)"
```
```
{'errors': '0', 'failures': '0', 'skipped': '0', 'tests': '958', 'time': '23.320', ...}
```

951 → **958** = −2 (删掉锁旧档的两条) +6 (新锁) +2 (`test_chapter_chunk_size_tokens_positive`
的 parametrize 加了 ch02 / ch03) +1 (评审后补的全量 token 闸, §9)。**failures=0, skipped=0。**
`test_kb_crossref_completeness.py` 7 passed。

`4315` 的全库引用:

```bash
grep -rn "4315" --include="*.py" --include="*.md" --include="*.json" --include="*.yml" . | grep -v evidence/failures
```

命中全部落在 `evidence/checkpoints/vi_crossref_completeness.md` 与 `topk_jitter.md`,
**没有一处是断言** —— 它们是当时那一轮的实测记录。历史实测数字**不改写** (改了就成了伪造),
改为在 `topk_jitter.md` §5.6 追加一条 Task 8 的失效/重测记录, 指向本文件 §6.1。
`server/router.py` 的 `chunk_count` 是运行时 `collection.count()`, 无硬编码。

---

## 9. 全量 token 上限闸 (评审 Minor 2, 2026-08-07 补)

**缺口**: 改动前的 `< 8000` 断言只覆盖 ch04 (L-4 锁) 与 ch08。ch01/02/03/10 **无闸**。
这不是笔误而是结构性缝隙: L-4 只在 `>50KB` 触发, 而两档策略下 20-50KB 文件一律只按 H2 切。
若将来某章 H2 极少而正文极长, 会在**没有任何测试报警**的情况下越过 8191 embedding 上限 ——
越限的表现是 ingest 报错或该块被静默截断, 两种都难倒查。

新增 `test_every_chapter_chunk_under_embedding_limit`: 按目录遍历 `chapters/*.md`
(不写死文件名, 新增 chapter 自动纳入), 断言**任意** chunk `< 8000` tok。

**闸能不能咬得动** —— 只报"它绿了"是不够的, 绿也可能是因为它永远不会红:

```bash
.venv/bin/python -c "
from pathlib import Path
from scripts.chunkers.chapters import ChaptersChunker
KB=Path('../knowledge_base').resolve(); ck=ChaptersChunker(KB)
allc=[(f.name,c.section,c.chunk_size_tokens) for f in sorted((KB/'chapters').glob('*.md')) for c in ck.chunk(f)]
print('total chapter chunks:', len(allc)); print('max:', max(allc, key=lambda t:t[2]))
for thr in (8000, 4400, 4000):
    print(f'threshold {thr}: offenders={len([t for t in allc if t[2]>=thr])}')"
```
```
total chapter chunks: 90
max: ('ch03_submitting_data.md', '3.2 Using the CDISC Domain Models ... Dataset Metadata', 4400)
threshold 8000: offenders=0
threshold 4400: offenders=1
threshold 4000: offenders=2
```

覆盖 **90/90** 个 chapter chunk (之前只有 66 个: ch04 47 + ch08 19)。阈值降到真实最大值
4400 时闸**确实变红**, 说明它是活闸而非恒真式。当前最大 4400 tok, 距 8000 有 45% 余量。

> 这条闸能证明"chapter 类没有块会撑爆 embedding";
> **不能**证明其他 file_type 安全 —— 它只遍历 `chapters/`。
