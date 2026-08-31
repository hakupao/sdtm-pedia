# 联网通道语义抽检 (规则 A)

> 联网答案不可复算, **不进 gold set** —— 本表是它唯一的质量证据。
> ⚠ 机检只能查形状; **人判两列必须人眼逐条判**, 不得由脚本判 PASS。
> ⚠ **本表 (v3, 2026-08-31) 三条限定, 阅读前先看**:
> 1. **样本量 n=2** —— 任何一行「零码」的观察 (第 1/2 题) 都只是这次运行的证据, 不构成 Rule 9(b) 在统计意义上的有效性证明。
> 2. 第 3 题两个 ⛔ 码见下方附录「已结构性排除」标注: 该轮 `搜索次数=0`, 判定依据是结构性的 (没联网就没有网页内容能进 context), 不是靠「最近引用标记」那条弱启发式。
> 3. **`机检: Web句含硬事实词` 这一列是 v4/v5 (代码审查后) 才加的新机检, v3 跑批时不存在**; 现已用**当前实现**对本轮已落盘的答案原文 (`web_channel_spotcheck_answers.md`) 离线回填, 数字真实、可零成本复算 (纯本地文本扫描, 无网络无 LLM, 见下方附录末尾的复跑命令)。⚠ 但这一列只是**关键词形状扫描**: 命中为 0 不等于 Rule 9(b) 的 class/category 归属与 Core/Role/Type 两样干净, 只等于「没查到这几个特定关键词」——不用这些词的归属表述依然全漏。

| # | 问题 | 机检: CT 码 | web_status | web_searches_ok | 搜索次数 | 机检: [Web:] 数 | 机检: [Source:] 数 | 机检: Web句含硬事实词 | 人判: 标注是否规矩 | 人判: 借鉴是否标推测 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | How do other teams handle EDC fields that don't map to any s | ✅ 无 | ok | 2 | 2 | 6 | 23 | 2 | ⬜ 待判 | ⬜ 待判 |
| 2 | What do practitioners say about overusing SUPPQUAL versus cr | ✅ 无 | ok | 2 | 2 | 5 | 12 | 0 | ⬜ 待判 | ⬜ 待判 |
| 3 | How is Findings About (FA) used in practice versus a custom  | ⛔ C101833,C101832 | ok | 0 | 0 | 0 | 22 | 0 | ⬜ 待判 | ⬜ 待判 |

## 判读规则

- **CT 码列出现任何码 = 立即查**: Rule 9(b) 禁止从网页产出 `Cxxxxx`、class/category 归属、Core/Role/Type。
  码若能在 `knowledge_base/` 找到且答案标的是 `[Source:]`, 属正常 (KB 来源);
  标 `[Web:]` 却带码 = **红线破**。
- **`搜索次数` 列 = 0 时优先看它, 比「最近引用标记」这条弱启发式更硬**: 该轮没有触发任何工具调用 ⇒ context 内不可能混入任何网页内容 ⇒ Rule 9(b) 的触发条件从未成立——这一行任何 CT 码命中都只能来自 KB, 可直接判非红线破 (第 3 题即此情形, 见下方附录), 不需要再去核对最近引用标记。
- **`web_status`/`web_searches_ok` 直接给出联网是否真的发生** —— 比『`[Web:]` 数为 0 ⇒ 可能没真联网』这种间接推断可靠: `web_searches_ok` > 0 才是真的搜到了结果; `web_status` 应为 `ok`, 非 `ok` (如 `partial`/`disabled`/`quota_exceeded`/`failed`/`off`) 说明联网本身有问题或不完整 (`partial` = 有成有败, 不是全灭)。
- **`机检: Web句含硬事实词` 只是形状扫描, 不是判定**: 命中不等于红线破, 只是提示该段混着 Core/Role/Class 一类硬事实词汇又带 `[Web:` 引用, 值得人多看一眼。本表三行的数字由**当前实现**离线回填 (见上方限定 3), 逐条命中列在下方附录, 已人眼核过——**命中为 0 仍只代表没查到这几个特定关键词, 不代表这两样硬事实真的没被违反**。
- 人判两列必须逐条看答案原文, 不看就填 = 抽检失效 (规则 A 的意义就在这)。

## 附录: CT 码标注上下文 (机器只定位, 不判读)

> ⚠ **「最近引用标记」是启发式定位, 不是来源判定。** 绝对字符距离只能告诉你「这个码附近最近的标记是什么」, **推不出**「这个码来自那个来源」 —— 同一段落可能引了多个来源, 物理最近的标记未必是这个码的事实依据所在。红线判定必须**读原文片段**确认该码的事实依据来自哪一边, 不能只看这一列的标签。`搜索次数==0` 的行不适用这条弱路径, 见下方「已结构性排除」标注。

### 第 3 题: How is Findings About (FA) used in practice versus a custom findings domain?

- **已结构性排除**: 本轮零工具调用 (`搜索次数=0`, `web_searches_ok=0`) ⇒ context 内无任何网页内容 ⇒ Rule 9(b) 适用前提未成立, 下面两个码只可能来自 KB。(不依赖下面的「最近引用」这条启发式, 那条只是交叉验证。)
- **`C101833`** @ char 5626 — 最近引用标记是 `[Source:...]` (距 `C101833` 101 字符): `[Source: domains/FA/assumptions.md]`
  > …ise be added. [Source: domains/FA/assumptions.md] - `FATEST` — Label "Findings About Test Name", Char, Synonym Qualifier, **Req**, Controlled Terms **C101833**, value ≤ 40 characters; CT lives in a general FATEST codelist plus several therapeutic-area-specific codelists. `FATESTCD` uses **C101832**. [Sourc…
- **`C101832`** @ char 5766 — 最近引用标记是 `[Source:...]` (距 `C101832` 11 字符): `[Source: domains/FA/spec.md]`
  > …d Terms **C101833**, value ≤ 40 characters; CT lives in a general FATEST codelist plus several therapeutic-area-specific codelists. `FATESTCD` uses **C101832**. [Source: domains/FA/spec.md] [Source: VARIABLE_INDEX.md] - `FACAT` (Label "Category for Findings About", Char, Grouping Qualifier, **Perm**, no CT…

## 附录: [Web:] 段落里的 Core/Role/Class 等硬事实关键词 (机器只定位, 不判读)

> 本节与主表该列同为**离线回填**: v3 跑批时这项机检还不存在, 现用**当前实现**
> (`eval/web_channel_spotcheck.py` 的 `_hard_fact_keyword_hits()`, v5 段落级扫描) 对本轮
> 已落盘的答案原文重跑得出。纯本地文本扫描, **无网络、无 LLM**, 与那次花过钱的运行记录
> (主表其余机检数字、CT 码附录的字符位置与距离) 无关, 后者一个字节未动。

复跑命令 (在 `sdtm-rag/` 下, 纯本地, 输出应为 `Q1 2` / `Q2 0` / `Q3 0`):

```sh
.venv/bin/python - <<'PY'
import re, sys; sys.path.insert(0, '.')
from eval.web_channel_spotcheck import _hard_fact_keyword_hits
src = open('evidence/checkpoints/web_channel_spotcheck_answers.md', encoding='utf-8').read()
parts = re.split(r'^## 第 (\d+) 题: (.*)$', src, flags=re.M)   # 按题头切; 答案正文自 body 第 5 行起
for i in range(1, len(parts), 3):
    ans = '\n'.join(parts[i + 2].split('\n')[4:]).rstrip('\n')
    print('Q' + parts[i], len(_hard_fact_keyword_hits(ans)))
PY
```

### 第 1 题: How do other teams handle EDC fields that don't map to any standard SDTM domain?

- 关键词 `Qualifier`: …- **判断フローとして「SUPPQUAL / FA / カスタム Findings ドメイン」の三択で整理する**のが定番の議論の立て方のようです。Salyers/Lewis/Wood のPharmaSUG 2015 論文は表題そのものが "Supplemental Qualifiers, Findings About, or a Custom Findings Domain" で、非標準変数提出時の考慮点を扱っています [Web: https://pharmasug.org/proceedings/2015/DS/PharmaSUG-2015-DS15.pdf (retrieved 2026-08-31)]。…
- 关键词 `qualifier`: …- **「まずカスタムドメインを作りたくなる衝動を抑えて SUPP-- を使え」という指針**を掲げるブログもあります [Web: https://omophub.com/blog/sdtm-clinical-trials (retrieved 2026-08-31)]。ただしこれは単純化しすぎで、標準側は「独自質問票なら QS へ」「data are different in nature なら custom domain 可」と述べており [Source: chapters/ch02_fundamentals.md -- 2.6 Creating a New Domain]、SUPP-- は**あくまで親レコードに対する非標準 qualifier の器**です。この Web 記述は無条件には採用しないことを推奨します。…

### 第 2/3 题

(无命中。第 3 题该轮 `搜索次数=0`, 答案里没有任何 `[Web:` 段落, 扫描范围为空 —— 这个 0 是"没有可扫的范围", 不是"扫过了很干净"。)
