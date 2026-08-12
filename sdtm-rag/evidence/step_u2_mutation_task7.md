# U2 Task 7 物理变异实证 (阳性/阴性对照 harness)

> 2026-08-12 · 实现方自跑 (规则 D: 审阅/抽检另派 subagent)
> 对象: `eval/judge_controls.py` (新) — `sample_ids` / `positive_answer` / `main`
> 断言方: `scripts/tests/test_judge_controls.py` (新, 11 条 = plan 逐字 4 + 补强 7)
> 数据红线: 本文件零真名零正文, 只有代码锚串 / 计数 / 可复跑命令。

## 0. 一句话

16 条变异, **两轮**跑批。第一轮 (只有 plan 给的 4 条断言) **11 条存活**; 补 7 条断言后
**14/16 全红**, 剩下 2 条绿是**独立证明过的正确绿** (一条死代码、一条 no-op 变异), 不是装饰断言。
存活的 11 条里最危险的两条 (**C1 阳阴两臂对调** / **C2 judge 传参对调**) 都是方向③对调型 ——
它们会让自毁条款 4 读出**完全相反**的结论, 而 judge 本身完好。

## 1. 基线与口径

| 项 | 值 |
|---|---|
| 开工全量 pytest | `1170 passed` |
| 首跑失败形态 | `ModuleNotFoundError: No module named 'eval.judge_controls'` (collection error) |
| plan 4 条实现后 | `4 passed` |
| 本 task 新增测试 | 11 条 (plan 逐字 4 + 判别力补强 7) |
| 收工全量 pytest | `1181 passed, 0 failed` (= 1170 + 11) |
| 变异跑批 sha 基线 | `eval/judge_controls.py 3f7d48433dc2` |

跑批口径 (Global Constraint 11):

- 脚本在**私有子目录** `<scratchpad>/task7/`, 不与并发 agent 共享路径 (并发: controller 在跑
  Task 4 的 eval sweep, 只写 gitignored 的 `data/`);
- 变异 = 对**当前实现态源码**做锚定文本替换, **锚点命中数 ≠ 1 当场中止**并记 `ABORT`, 不产生结论;
- 每轮 `subprocess` 子超时 600s; 每轮 `finally` 里按开跑前留下的**原始字节**写回并核 sha256;
- 每轮前写 `PENDING_MUTATION` 标记, 复原后删除;
- 收尾打印 `RESTORED True` + 逐文件 sha 对照 + `PENDING marker present: False`。

两轮收尾均为:

```
eval/judge_controls.py before=3f7d48433dc2 after=3f7d48433dc2 identical=True
RESTORED True
PENDING marker present: False
```

## 2. 两轮对照总表

`failed` = 全量 pytest 的 failed 条数。轮1 = 只有 plan 的 4 条断言; 轮2 = 补强后的 11 条。

| ID | 方向 | 变异 | 轮1 | 轮2 |
|---|---|---|---|---|
| A1 | ① 从断言出发 | `sample_ids` 去掉 `sorted(ids)` **[plan 指定]** | 1 | **3** |
| A2 | ① | `positive_answer` 返回 `""` **[plan 指定]** | 1 | **3** |
| A3 | ① | 上界闸 `n > len(ids)` 拆掉 | 1 | **1** |
| A4 | ① | 抽样公式分母 `n+1` → `n+2` (位置整体前移) | 1 | **3** |
| B1 | ② 从代码行出发 | `main()` 阴性臂整条死掉 (两 mode 都喂 gold) | **0** | **1** |
| B2 | ② | `temperature=0.0` → `1.0` | **0** | **1** |
| B3 | ② | `judge_model=a.judge_model` → 写死默认常量 | (脏) | **1** |
| B4 | ② | `--mode` 去掉 `required=True` | **0** | **1** |
| B5 | ② | parse 失败题当 `0.0` 混进均值 | **0** | **1** |
| B6 | ② | 绕过 `sample_ids`, 改取文件前 n 题 | **0** | **2** |
| B7 | ② | 退化分支 `idx = list(range(n))` 倒序 | **0** | **0** ✅正确绿 |
| C1 | ③ 对调型 | **阳性/阴性两臂互换** | **0** | **2** |
| C2 | ③ 对调型 | **judge 的 `question`/`answer` 位置参数互换** | **0** | **4** |
| C3 | ③ 对调型 | 抽样结果**前两位互换** | 1 | **3** |
| C4 | ③ 对调型 | 阳性答案里 gold facts **顺序倒置** | **0** | **1** |
| C5 | ③ 顺序型 | 去掉 `idx` 外层 `sorted` | **0** | **0** ✅no-op |

轮1: 存活 11 (B1,B2,B3\*,B4,B5,B6,B7,C1,C2,C4,C5) · 轮2: 存活 2 (B7,C5, 均为正确绿)。

> **轮3 (收尾复跑)**: 轮2 之后为消掉 4 条 `E402` 把补强段的 import 移到了文件头, 测试文件
> 因此变过。16 条**原样复跑一遍**, 结果与轮2 **逐条相同** (`round3_final`), `RESTORED True`。
> 上表的轮2 列即为**当前入库代码**的实测值。

> \* B3 在轮1 记为 `failed=1`, 但杀掉的是**另一个文件**的
> `test_main_study_docs_wiring.py::test_settings_study_docs_defaults` —— 那是并发 agent 的
> commit `edf02dc` (`study_docs_seats` 5→8) 在我跑批中途落地造成的**跨 agent 竞态**, 与 B3 无关。
> 事后单独复跑该测试 **4/4 全绿**。故 B3 在轮1 的真实结论是**存活**, 上表按存活计。
> ⇒ 记账教训: 跑批期间有并发 commit 时, `failed` 计数必须配失败**节点名**才能归因,
> 只看条数会把别人的红算成自己的绿灯。

## 3. 方向② — 从代码行出发: `main()` 是零覆盖的

plan 给的 4 条断言只覆盖 `sample_ids` 与 `positive_answer` 两个纯函数。**`main()` 的 30 行
一行都没被执行过** —— 轮1 里 B1/B2/B4/B5/B6 五条全部存活即为逐条实证。

这与 Task 3 的事故同形 (删光 27 行装配块, plan 的 4 条断言一条不红), 但成因不同:
Task 3 是 argparse 的 `SystemExit` 把"闸拒绝"与"flag 不存在"混成一种; 本 task 是 CLI 入口
**压根没有测试进入过**。补强的 7 条里有 6 条是为 `main()` 加的, judge 全 stub
(`monkeypatch.setattr(jc, "check_fact_recall_judge", fake_judge)`), 零 LLM 零网络。

其中 **B5 值得单列**: spec §5.3 逐字要求 `judge_parse_ok=False` 的题不许混进均值。把它当
`0.0` 计入后, 一次 judge **解析故障**看起来会跟一次真实低分一模一样 —— 这正是自毁条款 4
要防的"尺子坏了却读成数据坏了"。补强前这条禁令**无人守**。

## 4. 方向③ — 对调型: 本 task 的核心盲区

plan 4 条断言的逻辑形状:

| 断言 | 形状 | 对调型盲区 |
|---|---|---|
| `got == sample_ids(ids, 6)` | **同源比对** | 任何确定性变异两边同时变 ⇒ 结构上不可能红 |
| `sample_ids(reversed) == sample_ids(ids)` | **同源比对** | 同上; 只能抓"顺序敏感", 抓不到"顺序错但一致" |
| `len(got) == len(set(got)) == 6` | 集合/计数 | 位置对调完全不可见 |
| `got == [ids[i] for i in (4,8,…)]` | **逐位钉死** | ← 唯一钉方向的一条 |
| `"fact one" in a and "fact two" in a` | **成员** | 顺序、分隔符、额外内容全不可见 |

⇒ `sample_ids` 的输出顺序**恰好**被第 4 条钉住 (C3 轮1 即红); 但 `positive_answer` 的
成员断言与整个 `main()` 都对对调型敞开。三条对调型变异 C1/C2/C4 轮1 **全部存活**。

### 4.1 C5 是 no-op, 绿了**不能**算断言是装饰品

"去掉 `idx = sorted({...})` 的外层 `sorted`" 看起来是最自然的顺序变异, 实测轮1/轮2 都绿。
但它绿的原因不是断言弱, 而是**变异根本没改变行为** —— CPython 的小整数 set 对本用例按升序迭代:

```bash
cd sdtm-rag && ./.venv/bin/python -c "
s = {(k*30)//7 for k in range(1,7)}
print('set iter :', list(s)); print('sorted   :', sorted(s)); print('NO-OP    :', list(s)==sorted(s))"
#   set iter : [4, 8, 12, 17, 21, 25]
#   sorted   : [4, 8, 12, 17, 21, 25]
#   NO-OP    : True
```

故真正的顺序探针用的是 **C3 (返回值前两位互换)**: 集合相等、条数相等、去重相等、
"不取首题"相等, **只有位置变了**。它在轮1 就红, 证明 plan 的第 4 条断言不是装饰品。

> 这条是 Task 3b「锚点必须恰好命中一次」之外的**第二类** no-op 陷阱: 锚点命中了、
> 文本也真的改了, 但**语义等价**。没有独立证明就把它记成"断言是装饰品", 会导致去补一条
> 根本不缺的断言。

### 4.2 两条 HIGH 存活项的后果 (为什么必须补断言)

- **C1 (阳阴两臂对调)**: 产出答案的**集合**一字不变, 只有 mode↔answer 的**配对方向**翻转。
  跑出来阳性 ≈0.0 / 阴性 ≈1.0 ⇒ 自毁条款 4 双向触发, 现场会判成"judge 尺子失效", 实际
  judge 完好、harness 反了。杀它的断言必须**钉方向**: 阳性臂逐字等于 gold 拼接, 阴性臂
  一个 gold fact 都不含且跨题恒为同一常量句。只断"两臂不同"无效 —— 互换后它们照样不同。
- **C2 (judge `question`/`answer` 位置参数对调)**: 两者同为 `str`, **不抛 TypeError**。
  阳性模式下 judge 实际被问的是"题干是否覆盖了 gold", 阳性对照假性崩到 ≈0 ⇒ 同样错判成
  judge 坏了。轮2 杀 4 条, 是全批最响的一条。

## 5. 两条正确绿 (计划没提到的问题)

### 5.1 B7 — `sample_ids` 的退化分支是**死代码**

```python
    if len(idx) != n:  # 小池子撞位: 退化成前 n 个不重复位置, 仍与分数无关
        idx = list(range(n))
```

在守卫 `n <= len(ids)` 之下**不可达**。`idx` 只由 `(L, n)` 决定, 全枚举 `1<=n<=L<=300` 零命中:

```bash
cd sdtm-rag && ./.venv/bin/python -c "
hits = [(L,n) for L in range(1,301) for n in range(1,L+1)
        if len({(k*L)//(n+1) for k in range(1,n+1)}) != n]
print('fallback reachable pairs:', hits, 'count=', len(hits))"
#   fallback reachable pairs: [] count= 0
```

解析证明: 相邻位置差为 `L/(n+1)`。`L >= n+1` 时该差 `>= 1`, `floor` 严格递增; `L == n` 时
`floor(k*n/(n+1)) == k-1` (k=1..n), 同样两两不等。两种情形都恰好产出 n 个不同位置。

⇒ 该分支绿是**正确**的, 不是装饰断言。**实现按计划逐字保留, 未删** (删它属计划外改动,
留给审查方裁定; 参照 Task 1 里 `build_messages` 由审查方实证后才删的先例)。

### 5.2 `sample_ids` 对重复 id 不去重 (低危, 仅记账)

`sample_ids(["a","a","b"], 3)` 返回 `["a","a","b"]`。生产路径上 ids 来自
`list(qs)` 而 `qs` 是以 id 为键的 dict ⇒ **由构造保证唯一**, 本 task 不改。
按硬规矩 19 记此处绿灯同样"由构造保证, 判别力低"。

## 6. 复跑命令 (逐字)

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
./.venv/bin/python -m pytest scripts/tests/test_judge_controls.py -p no:warnings   # 11 passed
./.venv/bin/python -m pytest -p no:warnings                                        # 1181 passed
```

变异跑批 (私有子目录, 需自备 `mutate.py` + `muts.json`, 见本文件 §1 口径):

```bash
cd <scratchpad>/task7 && <repo>/sdtm-rag/.venv/bin/python mutate.py <round-tag> muts.json
```

## 6.1 ruff 残留 3 条 (均为 plan 逐字照抄的后果, 未擅自改)

```
eval/judge_controls.py:43:46 SIM115  Use a context manager for opening files   # yaml.safe_load(open(...))
eval/judge_controls.py:64:19 SIM115  Use a context manager for opening files   # json.dump(..., open(...))
scripts/tests/test_judge_controls.py:6:1 I001  Import block is un-sorted       # plan 写的 `sample_ids, positive_answer`
```

仓库当前 `ruff check .` 本身有 **93 条**未清 ⇒ ruff 不是本仓的闸。三条都出自 plan 的逐字代码,
按"与计划不符就停下报告"的纪律**保留原样**并在此记账, 由审查方裁定是否修。

## 7. 尚未证实的部分 (硬规矩 19)

1. 本 task **一次真 judge 都没打过** —— 11 条测试全 stub。"阳性会得高分、阴性会得低分"
   这件事本身属 Task 8 Step 1, 本 task 只保证 harness 把对的东西喂到对的位置。
2. 抽样规则的**代表性**未验: 它只保证与分数无关 + 确定性 + 散开, 不保证抽中的 6 题
   在难度上代表全池。
3. `check_fact_recall_judge` 内部的重试/限流退避未在本 task 覆盖 (`eval/run_eval.py:276-292`,
   本脚本按计划不重复实现)。
