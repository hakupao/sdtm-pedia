# DM2 T9 attempt 1 — L3 e2e 4/6 (目标 ≥5/6), 失败模式 = 类别轴混淆

> 日期: 2026-09-15 / 单元: DM2 Task 9 (L3 e2e 6 跑 + 异 agent 判分) / 判定: **业务 FAIL, 走 attempt 2 (只改 `_DOSSIER_RULES` 规则层)**
>
> 判据: `evidence/checkpoints/dm2_dossier_e2e.md` §0 (跑前预登记, commit `c1d57a6`)。
> 判分: 异 subagent (opus, 未参与生成 / 检索代码 / 判据撰写), 逐 run 报告在 gitignored
> `data/study/st01/eval/runs/dm2_e2e/judge_verdicts.md` (含真实 OID, 故不入版本库; 本文件只留无标识摘要)。

## 1. 输入 (跑了什么)

代码基线 **HEAD `37bcb3e`** ("feat(rag): DM2 T9 e2e runner")。跑批命令:

```
.venv/bin/python eval/prod_wirein/dm2_e2e_run.py     # 3 题 × 2 模型 = 6 次生产 /api/ask_stream
```

生效的规则句 (`server/router.py` @ `37bcb3e`, 逐字):

```python
_DOSSIER_RULES = (
    "\n\n## Study dossier rules\n"
    "- The context ends with 【本研究 研読パッケージ】: this study's protocol (PRT) chapters "
    "verbatim (part A) and the COMPLETE list of EDC items (part B). Study-side retrieval was "
    "skipped on purpose: part B is exhaustive, so if an item is not there, it does not exist.\n"
    "- Domain-level mapping questions: (1) enumerate the record categories the standard defines "
    "for the domain from 【標準 CDISC】 when that block is present; if it is absent, say so and "
    "enumerate from the standard as you know it, marked (推測); (2) for each category scan part B form by form for "
    "candidate items (status / date / reason), quoting each as `[form OID] item (OID)` exactly "
    "as written; (3) when the PRT defines the event (完了の定義 / 中止規準 / 登録手順 …), cite "
    "the section number from part A; (4) every EDC→SDTM assignment is inference — label it "
    "(推測); (5) say explicitly which categories have no candidate item.\n"
)
```

六跑的跑批摘要行 (脚本 `_summary_line` 原样, 无 study 标识):

```
dm01 opus-5    attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=105930 completion_tokens=11519 continue_rounds=0 truncated=False wall_seconds=202.1 answer_chars=5145
dm01 sonnet-5  attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=105930 completion_tokens=10741 continue_rounds=0 truncated=False wall_seconds=179.8 answer_chars=3446
dm02 opus-5    attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=106889 completion_tokens=13193 continue_rounds=0 truncated=False wall_seconds=232.3 answer_chars=4102
dm02 sonnet-5  attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=106889 completion_tokens=11810 continue_rounds=0 truncated=False wall_seconds=190.6 answer_chars=3382
dm05 opus-5    attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=107742 completion_tokens=14952 continue_rounds=0 truncated=False wall_seconds=255.8 answer_chars=6280
dm05 sonnet-5  attached=True reason=auto:domain+scope model_used=deepseek-v4-pro fell_back=True prompt_tokens=107742 completion_tokens=20314 continue_rounds=0 truncated=False wall_seconds=199.6 answer_chars=9667
```

⚠ **六跑全部 `fell_back=True`, `model_used=deepseek-v4-pro`** —— Bedrock 拒绝 Anthropic 模型,
请求的 `opus-5` / `sonnet-5` 都回退到同一个模型。**本轮不构成模型对比**, 只是同一模型在两条
请求路径下的两次采样; 判据 §0 的 "2 个模型" 在本轮实际退化为 "2 次采样"。

## 2. 产物: 判分总表

| run | 请求模型 (实跑) | ① 定义齐 | ② 候选齐 (零捏造) | ③ 标推测 | 判定 |
|-----|------------------|---------|--------------------|---------|------|
| dm01 / zh / DS | opus-5 (deepseek-v4-pro) | PASS 3/3 | PASS gold 4/4, 捏造 0 | PASS | **PASS** |
| dm01 / zh / DS | sonnet-5 (deepseek-v4-pro) | PASS 3/3 | PASS gold 4/4, 捏造 0 | PASS | **PASS** |
| dm02 / ja / DS | opus-5 (deepseek-v4-pro) | **FAIL 2/3** | PASS gold 4/4, 捏造 0 | PASS | **FAIL** |
| dm02 / ja / DS | sonnet-5 (deepseek-v4-pro) | **FAIL 2/3** | PASS gold 4/4, 捏造 0 | PASS | **FAIL** |
| dm05 / en / AE | opus-5 (deepseek-v4-pro) | PASS 3/3 | PASS gold 4/4, 捏造 0 | PASS (弱: 仅全局标记) | **PASS** |
| dm05 / en / AE | sonnet-5 (deepseek-v4-pro) | PASS 3/3 | PASS gold 4/4, 捏造 0 | PASS | **PASS** |

**4/6 PASS。** 判据 ② / ③ 六跑全过; 全部 2 处失分都落在判据 ①, 且都在同一题 (dm02)。

## 3. 技术判定

**(a) 研读包通道的 grounding 已证。** 六个答案合计约 450 处 EDC 项目 OID 主张,
判分 agent 用 part-B 一览逐个 grep, **捏造 0**; 额外做的更严校验 (OID 存在但挂错表单)
也是 **0 处**; 区间简写 (`…_1 … …_20` 形式) 逐号展开后无缺号。gold 卡点名六跑全 4/4,
无 3/4 边缘案例。→ "part B 穷尽 + 行式原样引用" 这套设计按预期工作, **不是本次失败的原因**。

**(b) 失败 = 类别轴混淆 (category-axis confusion), pattern 级。**
DS 域的记录类别沿 `DSCAT` 的 CT 取 3 个值 (`DISPOSITION EVENT` / `PROTOCOL MILESTONE` /
`OTHER EVENT`)。dm02 两跑都只列了前两个, 然后用**别的轴**把条数凑到 3:
- opus 路径: 把 `DISPOSITION EVENT` 按 `DSSCAT` 子类别再切一刀当第三类;
- sonnet 路径: 拿 IG ch04 的 "长期随访最终 disposition" (阶段/时点轴) 当第三类。

两跑全文都 0 次出现第三个 `DSCAT` 值, 且 §"无候选类别" 一节也**没有申报**它无候选 ——
即既没列举、也没显式豁免, 缺失是静默的。

**(c) 不是语料缺失, 是规则层缺约束。** 同域、同研读包、同一模型的 dm01 两跑把三类全列了,
说明检索层确实供了 DS 的类别定义。差别只在生成侧: 规则句第 (1) 步只说 "enumerate the record
categories the standard defines", 没说**沿哪条轴**穷举、也没要求 "每一个类别值各起一个小标题",
于是在候选一览 959 项的注意力挤压下, 类别枚举被压薄、并被就近的 `--SCAT` / 阶段轴顶替。
第 (5) 步 "say explicitly which categories have no candidate item" 挂在第 (1) 步的产物上 ——
第 (1) 步漏掉的类别, 第 (5) 步也就无从申报, 两条规则一起失效。

**(d) 触发条件跨域。** 凡 "域定义里分类轴不止一条" (`--CAT` vs `--SCAT` vs EPOCH/阶段)
的域都可能复现, 与 DS 无关。故修法必须在**模式级**: 说 "沿 `--CAT` 轴" 而不是说 "DS 有三类"。

**(e) 弱信号 (未判 FAIL, 但同属 pattern 级)。** dm05 opus 路径的 (推測) 标记只有开头一处
全局声明, 段内不复标 —— 若下游只摘表格, 标记就丢了。规则第 (4) 步 "every EDC→SDTM assignment
is inference — label it (推測)" 可以被 "开头声明一次即覆盖 below 全部" 这种读法满足。

## 4. 业务判定

**FAIL。** 4/6 < §0 预登记的 ≥5/6。判据 ② / ③ 的 6/6 不能抵扣 —— §0 规定三条全过才算该题 PASS。
按 §0 失败处置条款, 属于"只改 `_DOSSIER_RULES` 规则层措辞 (模式级), 不许加题面 example"的情形。

## 5. 下一 attempt (attempt 2) 的输入

`server/router.py` `_DOSSIER_RULES` 的规则层改写, 三点 (全部 pattern 级, 不含任何域名 / 类别值 / 题面 example):

1. **第 (1) 步改成沿 `--CAT` 轴逐类穷举**: 沿域自己的类别变量 (`--CAT`, 其 CT 在
   【標準 CDISC】块内时按块里的列) 枚举; **每一个类别值各起一个小标题**, 按标准的顺序,
   **在看任何 EDC 项目之前**; 不得用子类别 (`--SCAT`) / epoch / 时点轴替代类别轴。
2. **第 (2) 步与第 (5) 步合并**: 每个类别小标题下**要么**列候选项目, **要么**明写
   「候補なし / no candidate item in the EDC」—— 任何类别都不许被静默跳过。
   (合并是关键: 原来 (5) 依赖 (1) 的产物, (1) 漏了 (5) 就哑了; 合并后"漏"本身变成可见的空标题。)
3. **第 (4) 步要求逐条标记**: **每一条** EDC→SDTM 归属行内带 (推測), 不能只在开头做一次全局声明。

M5 的有条件措辞 (【標準 CDISC】块不在时要说出来并标 (推測)) 原样保留。
改后按 §0 重跑 **6 题全部** (`--no-resume`), 重新交异 agent 判分 (规则 D)。

**红线**: 不许写 "OTHER EVENT"、不许写 "DS has three categories"、不许引任何表单名 / 项目 OID /
日文字段 label —— 那是 example 级"对症下药", 会把 dm02 修绿而让跨域失败原样留着。
