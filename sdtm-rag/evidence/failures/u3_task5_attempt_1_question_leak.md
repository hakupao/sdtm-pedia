# U3 Task 5 attempt 1 —— 红线测试自身把题面泄进 pytest 输出

> 归档日期: 2026-08-13 (规则 B). 未删, 因为这条错误是「红线测试反倒是泄漏源」这一类的样本。

## 输入

task-5-brief.md Step 2 给的测试骨架, 其中两条按原样写成了**裸比较题面字符串**:

```python
def test_final_gold_preserves_draft_questions():
    draft = {x["id"]: x["question"] for x in yaml.safe_load(DRAFT.read_text(...))}
    final = {x["id"]: x["question"] for x in yaml.safe_load(FINAL.read_text(...))}
    assert final == draft
```

以及本 session 新加的反 cherry-pick 断言, 初版写成 `assert _load(FINAL) == _deterministic_split(_load(DRAFT))`
—— 比的是整条 dict, 含 `question`。

## 产物 / 现象

做变异 M1 (把 `u3_doc_01` 与 `u3_doc_02` 的 group 对调) 验证断言灵敏度时, 变异断言如期变红,
但 pytest 的 `--tb=short` 输出把 diff 两边**整条 dict 打了出来**, 其中包含手順書题面全文
(日文一整句, 含本研究固有的判定区分措辞)。

## 技术判定

断言本身没错, 检出能力也没问题 —— 错在**失败路径的输出面**。
本仓对 `run_routing_eval` 的 stdout 有成套红线测试 (`test_main_stdout_never_prints_question_text`
等), 但没人管**测试自己**失败时打什么。pytest 输出会进 CI 日志, 而 CI 日志不 gitignored。
于是「防题面进 git」的那条测试, 在它变红的那天自己把题面送出去。

## 业务判定

FAIL. 这不是理论风险: 变异一跑就实际打出来了。红线的成立条件是「所有路径」, 一条例外即失效。

## 修法 (attempt 2, 已交付)

- 题面只比 `sha256(question)[:16]` 摘要 —— 改一个字摘要就变, 检出能力不打折, 失败时只打 id + 十六进制。
- 划分相关断言改比 `(id, gold, group, chapter)` 四元组投影, 题面根本不进这条断言。
- 文件头写死 ⚠ 条: 本文件任何断言**不得直接比较题面字符串**, 供 code review 执行。

## 复验 (可复跑)

```bash
cd sdtm-rag
# 三个变异各跑一遍, 检查 pytest 全部输出里是否出现任何一条题面原文
# (脚本见 task-5-report.md §5; 判据 = 「题面泄漏进 pytest 输出 = 0 条」)
```

实测结果: M1 / M2 / M3 三个变异下, 泄漏条数均为 0 (修前 M1 为非 0)。

## 下一 attempt 的输入

无 —— attempt 2 已通过。遗留给后续单元的规矩: 凡是断言对象里含题面的测试,
一律先投影/摘要再比, 否则就是把红线的执行者变成红线的破坏者。
