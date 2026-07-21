# NotebookLM Q7 answer — Partial date SDTM/ADaM

**Verdict**: PASS
**Citation count**: 7+ ([29_ig_ch04_general_assumptions.md] × 7, [28_ig_ch01_ch02_ch03.md] × 1)

## 原则
SDTMIG v3.4 原生支持 partial date, 遵循"如实反映收集数据"原则, 通过**右截断** (right truncation) 或连字符 (-) 占位表达部分缺失, **不做 imputation**.

## 3 场景

| 场景 | 填法 | 规则 |
|---|---|---|
| A: AE 2024 年 6 月 (无日) | `AESTDTC = "2024-06"` | 缺日+时间时月后右截断 |
| B: CM 2024 年 (无月日) | `CMSTDTC = "2024"` | 仅保留 4 位数字年份, 后续全截 |
| C: 完全 Unknown | `AESTDTC = null` | §明确: completely missing → null. 若有"持续中/之前"用 AEENRTPT="UNKNOWN", 绝对时间变量保持空 |

## (d) SDTM --STDTC imputation? ✓
**不需要且不应该**:
- SDTM 核心目的 = 展示原始收集/接收的数据 (data as originally collected or received) [28_ig_ch01_ch02_ch03.md]
- 缺失组件必须直接表现为截断或连字符缺失
- **Partial dates 不能用于在 SDTM 中推导 Study Day (--DY 变量)** — SDTM 拒绝 Tabulation 层面数学推导或插补

## (e) ADaM imputation 时 SDTM 额外记什么? ✓
**SDTM 层面不需要为插补添加任何额外变量或记录**:
- SDTM 只需在 --STDTC 如实存储 partial ISO 8601 字符串 ("2024-06")
- 插补动作 (如补 "2024-06-01" 或计算 ABLFL) 完全在 ADaM (ADSL/BDS) 通过分析代码执行
- ADaM 的具体指导由 ADaM 实施指南规范 (不在 SDTM Project 范围)

## 评分要点
- ✓ 3 场景全对 (2024-06 / 2024 / null)
- ✓ 每场景 inline citation
- ✓ (d) 2 重拒绝理由 (SDTM 定位 + partial 不推 Study Day)
- ✓ (e) **关键正解: SDTM 不加额外变量** — 避开 Gemini 的 --DTF 幻觉陷阱
- ✓ 提 AEENRTPT="UNKNOWN" 相对时间补救
- ✓ ch01/02/03 + ch04 2 source 交叉引用
- △ 无 §4.4.2 表行锚点 (Claude 答有 "表行 6/7")
- △ 无 Solidus 区间 (Claude 答有)
- △ 无 §4.4.7 Example 3 AE Unknown 范本

## Carry-over
- F-1 小表渲染: 本答无复杂表格, 未触
- F-3 citation: 主要 [29_ig_ch04_general_assumptions.md] 对应 ch04, 正确映射到 partial date 章节 — 比 Q6 更合理
- **AHP 识破**: 正确避开 --DTF 假属性 (Gemini 误报), 值得记录作 v4 anti-hallucination baseline
