# 答题侧可信度护栏 — 收口总结 (规则 C retro)

> 日期: 2026-06-09 (单 session, 接 P1 接入生产之后)
> 路由词: "RAG 答题护栏 开始任务" → `KICKOFF_answering_guardrail.md`
> 结果: **v2 PASS, SHIP_DEFAULT_ON** (v1 FAIL → Rule B 归档 → v2 重写过闸)
> 闸: 仅动系统提示词 (`_build_system_prompt`) + eval gold 修正; 不碰已验证检索层。

## 一句话

P1 Rule A 裁判挖出答题侧两类信任硬伤 (per-value C-code 幻觉 + 关系类误判 special-purpose)。本任务加**两条通用系统提示护栏** + **确定性码-grounding 检查器** (补 substring 指标盲区) 修掉。**v1 漏穿被对抗式裁判抓到 (Rule B), v2 重写后码 fabrication 确定性消除 (0/147) + 分类修复 + 零过度拒答。**

## 改动 (code)

| 文件 | 改动 |
|------|------|
| `server/rag.py` | `_GUARDRAIL_RULES` (rule 7 个体值默认 name-only+仅照搬整行+禁自信/递增/"not shown"; rule 8 据权威 Class 列分类, relationship≠special-purpose) + `prompt_guardrail_enabled` 参数 + 条件化 `_build_system_prompt` (OFF 逐字节一致) |
| `server/config.py` | `prompt_guardrail_enabled=True` (默认开, `SDTM_RAG_` env 可关) |
| `server/main.py` / `server/router.py` | 转发护栏参数 + log + `/info` 暴露 |
| `eval/run_eval.py` | `--guardrail` + `--full-answers` flag |
| `eval/test_set_v2.yml` | gold 修正 q02 (→真 7 Req) + q37 (移误判 SUPPQUAL→SE); scientist 独立 KB 核验 PASS |
| `eval/prod_wirein/check_code_grounding.py` | **新**: 确定性码-grounding 闸 (抽答案所有 Cxxxxx 对 context+KB 核 grounded/ungrounded/nonexistent) |
| `eval/prod_wirein/forensic_guardrail.py` | **新**: 配对全文取证 (护栏 off/on, 检索恒定) |

## 验证闸 (全过)

| 闸 | 方法 | 结果 |
|----|------|------|
| gold 修正 | `oh-my-claudecode:scientist` 独立 KB 核验 (规则 A 4.c) | PASS — q02/q37 双修正 KB 实证正确 |
| 代码审 | `oh-my-claudecode:code-reviewer` (异 type) | APPROVE_WITH_NITS (字节一致性实测; nit 已修) |
| 单测 | pytest scripts/tests/ | 214 passed |
| OFF 字节一致 | 重构原 prompt 对比 | **22453 chars 逐字节相等** (干净 A/B 前提) |
| 检索未腐化 | retrieval-only v2 102q | 99.0% 未动 (提示不碰检索) |
| **码 fabrication (确定性)** | `check_code_grounding.py` 全 102 ON-v2 | **147 码 100% grounded, 0 ungrounded, 0 nonexistent → PASS** (v1=10 违规) |
| **语义裁判 v1** | 4-lens scientist 对抗 panel (KB 核验) | **FAIL** — 抓 q93/q44 漏穿 + q37 变糟 (substring 指标全盲) → Rule B |
| **语义裁判 v2** | 3-lens scientist (over-refusal 决定性 + 分类 + ship) | **gate_pass=TRUE, SHIP_DEFAULT_ON** |
| fact recall | OFF 94.8→ON-v2 93.4 (-1.4pt) | 噪声带内 (OFF-vs-OFF 噪声底 ±0.9 avg/±3pt cat 实测); 裁判: 全由 4 子串假阴 [codepoint U+202F/U+2011/en-dash] + 5 正确弃答解释, 真回归=0 |

## v2 裁判判决 (Rule D, 异 type, KB 逐一核验)

- **code_fabrication: eliminated** (0/147; spot-check 码归属正确: q44 C25299=DIABP / q91 C49634=WITHDRAWAL BY SUBJECT 等)
- **q37_classification: fixed** (只列 DM/CO/SE/SM/SV, 抵住 SUPPQUAL "special-purpose dataset model" prose 诱饵, 用权威 ch03 Class 列)
- **over_refusal_count: 0** (9 drop 全是假阴/正确弃答, 无一是 context 有但答案漏)
- **real_regressions: []**

## 残留 known limitations (护栏两规则范围外, 已 ack)

1. **q93 INJECTION vs INJECTABLE**: 值名问题 (非码非类)。INJECTION/C42946 不在检索 context; 模型用 SU spec prose 里的 "INJECTABLE"。检索覆盖 artifact, 护栏管不到值名。
2. **q96 Diameter**: 标准值 C25285 未被检索 (在 other_part2.md)。检索覆盖。
3. **per-value 右归属全 102 未尽核**: 确定性 checker 覆盖全 102 码"在 context"; 右归属仅 bundle (8 含码题) spot-check。残留风险低 (模型抄行非记忆)。

## 方法论备注 (规则 A/B/C)

- **substring fact-recall 对两类目标缺陷完全盲** (q37 照样 100/100; q44/q93 编码不罚) → 必须 (a) 确定性码-grounding 检查器 + (b) 语义裁判 override。这是本 session 最重要的工具补强。
- **对抗式裁判挖出 v1 漏穿** (我眼检漏掉 q44 过度拒答探针反而新增编码) → Rule D 异 type 独立审是真闸非走过场。
- **DeepSeek temp=0 残留非确定性**: 噪声底 OFF-vs-OFF 实测 ±3pt category 摆动; fact 配对须语义 override。
- v1 失败归档 `evidence/failures/guardrail_v1_attempt_1.md` (规则 B, 不删)。

## 现成可复用资产

`eval/prod_wirein/`: `check_code_grounding.py` (确定性码闸) + `forensic_guardrail.py` (配对全文) + `judge_workflow{,_v2}.js` (对抗式语义裁判 workflow) + 全 raw JSON/log + 噪声底 (g_off_t0 vs g_off2_t0)。`run_eval.py --guardrail --full-answers`。
