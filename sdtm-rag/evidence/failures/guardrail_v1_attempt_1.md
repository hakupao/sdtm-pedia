# 失败归档 (规则 B) — 答题护栏 v1 (attempt 1) 未过 gate

> 日期: 2026-06-09
> 判定者: 对抗式多-lens 语义裁判 workflow (4 scientist lens + synthesis, 全 opus, KB 逐一核验; run wf_d51fba36-56e)
> 结论: **gate_pass = FALSE** — 不删代码, 改 wording 进 v2

## v1 输入 (wording)

`server/rag.py` `_GUARDRAIL_RULES` v1:
- Rule 7: "Never output an NCI controlled-terminology code unless that exact code appears verbatim in the retrieved context... do NOT reconstruct, guess, increment, or infer a code from memory."
- Rule 8: "Do not assert that a domain belongs to an SDTM class unless the retrieved context explicitly states that membership."

## 技术判定 (裁判, KB 核验)

| 靶 | 判定 | 证据 |
|----|------|------|
| q90 | ✅ fixed | 38 个递增编码 → 0, 路由 name-only, 仅留 grounded C66729 |
| q91 | ✅ fixed | per-value 码 0, 仅留 grounded C66727; 缺定义优雅降级 |
| **q93** | ❌ not_fixed | ON 仍编 "INJECTABLE=C42944" (KB: C42944=INHALANT; 无 plain INJECTABLE codelist 值). OFF 给 name-only → **守护臂更差** |
| **q44** | ❌ regression (NEW) | ON 新增 6 个错 VSTESTCD per-value 码 (TEMP=C49677[KB:HR]/WEIGHT=C49678[KB:RESP]/HEIGHT=C49679[KB:MAP]/O2SAT=C49670[KB:mmHg]/RESP=C49675/MAP=C49672). **C49675+C49672 全 KB grep 为空 = 纯编造**. OFF 只给 codelist 码 0 个 per-value 码 → 守护臂更差. 直接违反 rule 7 (vs.md 在检索源里) |
| **q37** | ❌ not_fixed + 局部回归 | ON 把 RELREC+SUPPQUAL 并进单一"explicitly identified as belonging to Special-Purpose"表 (与真成员 DM/CO/SE/SM/SV 同列). 权威 ch03 Class 列 = "Relationship". OFF 至少对冲分隔 → ON 更强的假断言 |
| 过度拒答 | ✅ 无 | 7 探针 grounded codelist 码全存活 (C66769/C66727/C66731/C66741); q16/s05 反升 |
| fact 回归 | ✅ 零真回归 | 8/10 drop 子串假阴 (token 实际在 ON 答案里); q02 噪声底内; src 99.0% 确定不变 |

## 业务判定

**不可上线** (default-ON). 临床 KB 里一个错码即 blocker. 守护臂在 q44/q93 比无守护臂**注入更多错码**, 在 q37 注入更强假分类. 净: q90/q91 真修复 (高价值, mass-fabrication 类), 但 targeted defect 在 small/familiar codelist 上**漏穿**.

## 根因 (裁判机制诊断)

两条规则都检查 **presence-of-a-string**, 非 **authoritativeness**:
1. **Rule 7 漏洞**: "码 verbatim 出现" 挡不住模型在 small/familiar codelist (VS/dose-form) 上的**自信编码** + 递增猜 + "present but not shown" 自我合理化. q90/q91 修复只因 codelist 巨大 (150+ 行) 模型放弃枚举 → name-only. small codelist 模型自信 → 顶穿.
2. **Rule 8 漏洞**: KB 自身 IG 级松散措辞 ("RELREC special-purpose dataset" in assumptions.md) 满足 "context states", citation-presence 橡皮图章盖过权威 ch03 Class 列.
3. **指标盲**: substring fact-recall 对两类缺陷完全盲 (q37 照样 100/100; q44/q93 编码不罚分) → 配对 eval 闸抓不到, 仅语义裁判抓到.

## 下一 attempt (v2) 调整输入

- **R1 (rule 7 重写)**: per-value 个体码**默认 name-only**; 仅当该值**自己那一行 (值名+码同现)** 字面在 context 才可附码; 显式禁 (a) 凭记忆/自信, (b) 递增/类比邻码, (c) "in source but not shown" 合理化. (q90/q91 已证 name-only 是安全可行行为 → 扩到 VSTESTCD/EXDOSFRM.)
- **R2 (rule 8 重写)**: 分类须据**权威 class designation** (Class 列 / 明确 "the following domains are <category>" 枚举), 非 domain 自身 assumptions 松散 prose; 加一般原则: relationship dataset (Class='Relationship') ≠ Special-Purpose. (一般 pattern, 不点 q37/RELREC 题号.)
- **新增确定性闸**: `check_code_grounding.py` — 抽答案所有 Cxxxxx, 逐一对**重检索 context** 核 grounded/ungrounded, 补 substring 盲区. v1/v2 before-after 对比.
- 反过拟合: v2 仍是通用 pattern; 出测试集外探针验泛化 ([[feedback_prompt_anti_cheating]]).

## 保留产物 (不删)

- v1 eval: `eval/prod_wirein/{g_off_t0,g_on_t0,g_off2_t0}.json` + forensic + paired analysis (噪声底 + drops 全保留, 重跑复盘最贵资料).
- 裁判全文: 本 session transcript / task wditd3m30.output (4 lens + synthesis 逐题 KB 证据).
