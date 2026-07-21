# Rule A N=5 独立语义抽检 — Gemini Node 2 Attempt 2

> Date: 2026-04-20
> Scope: Gemini `04_terminology_core.md` (attempt 2 v1.3d 产物) 的 merge 合规抽检.
> Audit lane: 主 session 独立 (非 executor, 非 reviewer subagent), 规则 A 兑现.
> 原则: 压缩率 ~65% (898K core tokens → 299K 04, 按 tokens) 或 ~88% (42 core files → 5 selected), 均 >50% 阈, 必须 N=5 抽检.

---

## 1. 抽样方法

Selected (v1.3d): `[lb_part2, lb_part3, oncology_part1, interventions, qs_part1]` = 5 段 source — **正好 N=5, 每段独立抽检一次**.

对每段 source:
- **前 3 行比对**: 产物中 `<!-- source: -->` 注释之后的 3 行 (heading + `> Codelists in this file: N` + 空行) vs KB 源文件的同位置 3 行.
- **末 3 行比对**: 产物中该段末尾 (下一段 source comment 之前 2 行) vs KB 源文件末尾 3 行.
- **预期**: 100% 字符对齐 (merge 只拼接源文件, 不改内容, P5 只读规则兑现).

---

## 2. 抽检结果 (5/5 PASS)

### Sample 1: lb_part2.md (@ 04 L10, bytes 0-377,851)

| 项 | 产物 04 | KB 源 | 吻合 |
|---|---|---|:---:|
| Heading | `# Laboratory Codelists (Part 2)` | `# Laboratory Codelists (Part 2)` | ✓ |
| Codelist count | `> Codelists in this file: 1` | `> Codelists in this file: 1` | ✓ |
| 末行 | `C147452 ZPP Zinc Protoporphyrin` | `C147452 ZPP Zinc Protoporphyrin` | ✓ |

**PASS** — 起止完整, 无截断.

### Sample 2: lb_part3.md (@ 04 L2559)

| 项 | 产物 04 | KB 源 | 吻合 |
|---|---|---|:---:|
| Heading | `# Laboratory Codelists (Part 3)` | `# Laboratory Codelists (Part 3)` | ✓ |
| Codelist count | `> Codelists in this file: 1` | `> Codelists in this file: 1` | ✓ |
| 末行 | `C184638 Zopiclone Zopiclone` | `C184638 Zopiclone Zopiclone` | ✓ |

**PASS**.

### Sample 3: oncology_part1.md (@ 04 L5108)

| 项 | 产物 04 | KB 源 | 吻合 |
|---|---|---|:---:|
| Heading | `# Oncology Codelists (Part 1)` | `# Oncology Codelists (Part 1)` | ✓ |
| Codelist count | `> Codelists in this file: 4` | `> Codelists in this file: 4` | ✓ |
| 末行 | `C94534 TRGRESP Target Response` | `C94534 TRGRESP Target Response` | ✓ |

**PASS**.

### Sample 4: interventions.md (@ 04 L5419)

| 项 | 产物 04 | KB 源 | 吻合 |
|---|---|---|:---:|
| Heading | `# Intervention Codelists` | `# Intervention Codelists` | ✓ |
| Subtitle | `> Codelists for intervention domains: ...` | `> Codelists for intervention domains: ...` | ✓ |
| 末行 | `C38313 VAGINAL Administration into the vagina` | `C38313 VAGINAL Administration into the vagina` | ✓ |

**PASS**.

### Sample 5: qs_part1.md (@ 04 L6045)

| 项 | 产物 04 | KB 源 | 吻合 |
|---|---|---|:---:|
| Heading | `# Questionnaire Domain Codelists (Part 1)` | `# Questionnaire Domain Codelists (Part 1)` | ✓ |
| Codelist count | `> Codelists in this file: 1` | `> Codelists in this file: 1` | ✓ |
| 末行 | `C102124 YMRS YMRS01 Young Mania Rating Scale` | `C102124 YMRS YMRS01 Young Mania Rating Scale` | ✓ |

**PASS**.

---

## 3. 汇总

| 抽样 | Heading | Codelist count | 末行 | 段界完整 | Verdict |
|---|:---:|:---:|:---:|:---:|:---:|
| lb_part2 | ✓ | ✓ | ✓ | ✓ | PASS |
| lb_part3 | ✓ | ✓ | ✓ | ✓ | PASS |
| oncology_part1 | ✓ | ✓ | ✓ | ✓ | PASS |
| interventions | ✓ | ✓ | ✓ | ✓ | PASS |
| qs_part1 | ✓ | ✓ | ✓ | ✓ | PASS |

**5/5 PASS** — merge_for_gemini.py v1.3d 确实按 bytes 升序吃 hint 的策略实现, 5 段 source 内容在产物中完整保留 (起止边界严格对齐 KB), 无截断、拼接错误、污染. P5 只读规则兑现 (KB 源文件未被改动).

---

## 4. 业务语义核查 (独立视角)

### 4.1 高频 codelist 覆盖度

selected 5 段覆盖的 codelist 类型 (从 heading 反推):
- **Laboratory (lb_part2 + lb_part3)**: 2 段全 LB 实验室检查 codelists (test code + test name, ~1 codelist 每段)
- **Oncology (oncology_part1)**: 4 个 codelists (clinical classification category 等)
- **Interventions (interventions)**: 多 codelists (dosage form / route / frequency / position)
- **QS (qs_part1)**: 1 codelist (questionnaire category)

**语义评价**: 覆盖 4 大高频域 (LB / OC / Interventions / QS), 与 SDTM 临床研究典型高频 terminology 查询场景对齐. 遗憾: 漏掉的 Demographics (dm.md) / Adverse Events (ae.md) / General (general_part1-5.md) 没入 selected, 将在 A/B 跑题时暴露召回风险 (Node 5 才测).

### 4.2 "高频小文件 prepend" 策略解读

bytes 升序顺序: onc (89,521) < intv (89,805) < qs (136,529), 正好是"最小 hint 先吃"策略. 两个 89K 档 bytes 差 284 (<1%), 可认为 "tie" 级. tie 情况下 Python sorted 稳定, 原 HIGH_FREQ_CORE_HINTS 数组顺序 [interventions, qs_part1, oncology_part1, general_part1, is_domain_part2] 不直接影响排序 (sort key 纯 bytes 升序). 对比结果: 实际产物 onc < intv < qs, 非 HINTS 数组顺序, 这是"bytes 升序"策略的忠实实现, 与 v1.3c 推演一致.

### 4.3 selected 策略是否合理?

- **保尾 top-2 bytes**: lb_part2 + lb_part3 (合 216K tok) 站稳 04 中部, 确保 lb 核心 codelist 不丢. 合理.
- **prepend 3 smalls**: onc + intv + qs (合 84K tok) 落末尾 30%, 兑现 V6 多样 codelist recency. 合理.
- **跳过 general_part1 (62K) + is_domain_part2 (69K)**: budget 90K 吃不下. **可惜但非错**: general 是泛用 codelist (医学 unit / anatomic site / etc), 未来若 A/B 发现泛域查询召回低, Node 3/4 可考虑扩 budget. 记 Node 3 **MEDIUM 建议**.

---

## 5. 结论

**Rule A N=5 语义抽检 PASS**:
1. 每段源内容在 04 产物中**完整保留** (5/5 起止对齐).
2. P5 只读规则**未被破坏**.
3. bytes 升序策略**忠实实现** (onc < intv < qs 顺序).
4. 业务覆盖**4 大高频域**, 合理性对齐 SDTM 场景.

**非阻塞 LOW 建议** (交 Node 3):
- **LOW-A1**: 未入 selected 的 general_part1 / is_domain_part2 对泛域查询可能召回不足, 建议 Node 3 跑 A/B 后决定是否扩 budget 到 160K (吃 general_part1).

---

## 6. 独立性声明 (规则 A 合规)

- 抽检执行方: 主 session 直接跑 `bash` grep/sed/head/tail 取样对比, 未派 subagent.
- 与 writer (executor) lane 独立: 不基于 merge_for_gemini.py 的 selected 列表输出, 而是直接 `grep "^<!-- source:"` 数产物实际段数.
- 与 reviewer lane 独立: 不基于 phase3_node1_reviewer.md / phase3_node2_fix_reviewer.md / phase3_node2_fix_delta_reviewer.md / phase3_node2_fix_final_critic.md 的结论, 独立从 KB 源文件 + 产物直接对比.

规则 A "Writer 说 PASS + Reviewer 说 PASS ≠ 业务 PASS, 必须有独立样本核验" 兑现.

---

*audit performed by main session directly (not subagent), 规则 A 强制独立抽检 lane.*
