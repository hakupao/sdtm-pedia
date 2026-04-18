# B2 Review — score_domains.py

> 复核日期: 2026-04-18
> Reviewer: oh-my-claudecode:code-reviewer (model=opus, agent add749486336e87c4)

## 结论
**PASS**

## 抽样验证
- 用户 20 域全在必选: ✓ (DM/SE/DS/BS/BE/MI/GF/PR/CM/EX/TU/TR/RS/SS/DD/LB/FA/CE/MH/SU 全部标 `must (user)`)
- T_test_hits 6 域全在必选: ✓ (AE/PC/PP 标 `must (T_test_hits)`, EX/MH/LB 因与用户清单重合已标 `must (user)`, 通过 `set() | set()` 去重, 无重复、无遗漏)
- 推荐合并总数: **28** ∈ [25, 28] ✓ (必选 23 + 非必选 top-5: CP, EG, IS, MB, MS)
- 幂等: ✓ 两次运行 stdout byte-identical, md5 均为 `cba513e0817f54ba09bcf26353e6e239`
- 只读: ✓ grep `open(..., 'w'|'a')` / `os.remove` / `shutil.move|copy|rmtree` / `Path.write*` / `.unlink()` / `subprocess` 全部 no match; 导入仅 `re, sys, pathlib.Path, tiktoken` (加 `__future__`)

## 算法复核
- **normalize 方法**: min-max 实现正确 — `(v - lo) / (hi - lo)`, 退化场景 (`hi == lo`) 返回全 0.0 (line 103-115), docstring §2 有专门的"Why min-max"段落, 合规 `B2_executor.md` §"强制要求 4"
- **极端值处理**: 合理. min-max 对离群大值会压缩中位分, 但设计目标是排序 top-N, 非统计推断; 审阅时观察到 examples_tokens 量级跨度大 (UR=987 → IS=13694), 压缩后仍保留了单调序, 未影响排序合理性 (IS=0.53 居首, 与最长 examples 对应)
- **T_test_hits 加分权重**: 算法形式化地按 spec `0.2 * (20 if hit else 0)` 实现 (line 132), = 4.0 flat bonus, 相对 min-max 上限 0.8 呈 5× 压倒优势. 但语义上是**冗余 (harmless)** — 6 个 hit 已全部通过 `set(USER_MUST) | set(T_TEST_HITS)` 的 union 强制进入 must_set, 排序阶段又通过 `d not in must_set` 过滤掉, 加分对最终 merge 无影响. 冗余不是 defect (spec 明确要求), 记为观察而非问题.

## 关键发现

脚本质量扎实: docstring 完备 (含 min-max 选择理由), 类型注解齐全, 边界处理 (缺 examples.md→0 tokens, 缺 VARIABLE_INDEX→exit 2, 合并超限→降级裁剪) 均有覆盖. 确定性强 (`sorted()` 用于 domains / USER_MUST / extra_from_tests / merge_set, tiebreak `(-score, domain)` 稳定). 输出三段结构与 executor spec 完全一致. 非必选 top-5 (CP/EG/IS/MB/MS) 的 cross_ref + examples_tokens 抽样与脚本得分一致 (IS cross=17/tok=13694 → 0.53, EG cross=19/tok=5691 → 0.39), 信号计算无算子错误. 唯一语义冗余 (T_test_hits 加分对 merge 无影响) 是 spec 指定, 不作为 FAIL 依据.

## 下一步
**PASS → 进 Task B3**. merge_set (28 域) 可作为 batch 2 文件写入输入.
