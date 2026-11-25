# C refactor (Node 4) attempt_1 FAIL: V8b inline codelist pattern false positive

> 2026-04-21 C 方案 executor (opus)

## 输入
- PLAN: `ai_platforms/gemini_gems/docs/PLAN_V2_C.md`
- 04 writer-authored: `ai_platforms/gemini_gems/current/uploads/04_business_scenarios_and_cross_domain.md`
- V8 pattern: `r"^\s*\|\s*C\d{5,7}\s*\|\s*\w+"` with hard_max=5

## 产物 (attempt_1)
- 04 `§3.1 常问 codelist 索引` 采用标准 markdown 表格格式:
  ```
  | C66742 | No Yes Response | AESER, ... |
  | C66769 | Severity/... | AESEV (... MILD/MODERATE/SEVERE) |
  ...
  ```
- 26 行命中 V8b pattern → FAIL
- validate rc=1 HARD FAIL

## 技术判定
- pattern 本意检测"inline codelist Term 值表" (如 C66742 YES = "Yes" 这样的 Term 枚举表)
- pattern 实际匹配任何 "| Cxxxxx | word" 格式, 无法区分"CT Code → codelist 名"(合法) vs "CT Code → Term 值"(违规)
- V8 的 executable 定义与业务意图有 gap

## 业务判定
- §3.1 的内容**本来就合规** — 只列 CT Code + codelist 英文名 + 应用变量, 无 Term 值
- "YES/NO/MILD" 这类字符在 codelist 名中作为示例出现 (如 "3 档: MILD/MODERATE/SEVERE") 不是 inline Term 值定义
- 但 pattern 无法识别, 需调整 04 格式 (绕 pattern) 或调 validate (改 pattern)

## 下一 attempt 输入
- 选方案: **改 04 格式** (保持 V8 规则不变, 让未来 inline 真 Term 值的 04 仍会 FAIL)
- 做法: §3.1 从 markdown 表格改为**无项目符号列表** (`- \`C66742\` — "No Yes Response" codelist; 应用: ...`)
- 反引号包裹 CT Code 避开 `| Cxxxxx |` pattern
- 保留完整语义 (CT Code + codelist 名 + 应用变量)

## 结果 (attempt_2, 本 executor 同 session 内)
- §3.1 改列表格式, 运行 validate rc=0 PASS
- V8b: inline codelist lines matched 0 < 5 PASS
- 04 tokens: 30,488 (从 30,262 增加 226, 列表格式微扩)

## Rule B 总结
- 这是 pattern 误判问题, 非业务内容错
- 未来迭代: 可考虑 v2.1 validate pattern 收紧检 "Y"/"N"/"MILD"/"SEVERE" 等实际 Term 值 pattern
