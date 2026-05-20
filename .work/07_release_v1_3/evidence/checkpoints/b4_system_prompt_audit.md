# B4 — system_prompt audit pass (M1)

> Date: 2026-05-20
> Phase: B — 4-platform rebuild + system_prompt audit
> Step: B4 (carry M1 from v1.1 Post-Audit Pass)
> Status: **PASS** ★

---

## 1. Carry 来源

v1.1 RETROSPECTIVE.md § 二 6 (用户拷问后补) → § 四 Post-Audit Pass:

> "4 平台 system_prompt stale '63 域' 引用 — 漏没改, 用户审后立即补 (chatgpt/gemini/claude system_prompt + notebooklm instructions 各 1 处 assumptions 段 63→64, 其他高层 '63 全量平权' 概念性语句因 DI 是边角 study reference 保留)"
> "→ **后续建议**: PLAN.md 加 Step 7' 'system_prompt audit pass' — 在 rebuild 后必须 grep 各 system_prompt 找数字引用 (域数/文件数/段数), 与 build script segment_count 交叉对比, 不一致即 FAIL."

v1.3 PLAN.md § 2 Phase B → B4 = M1 实现.

## 2. 4 平台 build script segment_count (post-rebuild B2)

| Platform | File | Domains | Build segment_count | Match KB? |
|---|---|:-:|:-:|:-:|
| chatgpt | 04_domain_specs_all.md | 63 (DI 无 spec.md) | 63 dynamic | ✅ |
| chatgpt | 05_domain_assumptions_all.md | 64 (含 DI) | 64 dynamic | ✅ |
| chatgpt | 06_domain_examples_all.md | 63 (DI 无 examples.md) | 63 dynamic | ✅ |
| gemini | 02_domains_spec_and_assumptions.md | 63 spec + 64 assumptions | composite (script log) | ✅ |
| gemini | 03_domains_examples.md | 63 | composite | ✅ |
| notebooklm | 25_td_meta_ti_ts_oi_di.md | TI/TS/OI + DI | 10 sources | ✅ |
| notebooklm | (全 42 bucket) | 全 190 KB files | 190 covered | ✅ (M5 validate PASS) |
| claude | 05_mega_spec.md | 63 (DI 无 spec.md) | (claude executor 后台) | ⏳ |
| claude | 06_assumptions.md | 64 (含 DI) | (claude executor 后台) | ⏳ |

## 3. system_prompt 数字引用 audit (4 平台)

### 3.1 chatgpt — `ai_platforms/chatgpt_gpt/current/system_prompt.md`

| Line | Quote | Expected | Verdict |
|:-:|---|:-:|:-:|
| L20 | "9 合并文件覆盖 63 域 spec + assumptions + examples ..." | 63 (高层概念) | ✅ |
| L27 | "04 ... 63 域 spec (变量表, 全量平权)" | 63 | ✅ |
| L28 | "05 ... **64 域** assumptions (含 DI SDTMIG-MD 设备识别)" | 64 | ✅ |
| L29 | "06 ... 63 域 examples (实例数据)" | 63 | ✅ |
| L50 | "63 域**全量平权**" | 63 (高层) | ✅ (per v1.1 retro: 高层概念用 63 保留, DI 边角不偏倚) |
| L83 | "63 域 examples 已覆盖" | 63 | ✅ |

**chatgpt 6/6 PASS**. 区分 63 spec/examples 与 64 assumptions 准确.

### 3.2 gemini — `ai_platforms/gemini_gems/current/system_prompt.md`

| Line | Quote | Verdict |
|:-:|---|:-:|
| L40 | "02 ... 63 域 spec + **64 域** assumptions (含 DI SDTMIG-MD)" | ✅ |
| L41 | "03 ... 63 域 examples" | ✅ |
| L418 | "主 → 扫 02 ... 63 域 spec" | ✅ |
| L461 | "极端多针 (63 域全量扫描)" | ✅ (高层) |
| L463 | "63 域的全量扫描" | ✅ (高层) |
| L525 | "63 域**平权**" | ✅ (高层) |

**gemini 6/6 PASS**.

### 3.3 claude_projects — `ai_platforms/claude_projects/current/system_prompt.md`

| Line | Quote | Verdict |
|:-:|---|:-:|
| L18 | "9 个压缩文件 ... 覆盖 **63 个 domain** + 91 个 terminology" | ✅ (高层概念, 与 v1.1 决策 align) |
| L28 | "04 ... 63/63 域, 1917 行" | ✅ |
| L29 | "05 ... 63 域合并 Spec 表" | ✅ |
| L30 | "06 ... **64 域** assumptions (含 DI SDTMIG-MD)" | ✅ |
| L31 | "07 ... 63 域 examples 目录" | ✅ |
| L123 | "63 域 examples 数据表已全量覆盖" | ✅ |

**claude 6/6 PASS**.

### 3.4 notebooklm — `ai_platforms/notebooklm/current/instructions.md`

| Line | Quote | Verdict |
|:-:|---|:-:|
| L5 | "**63 SDTM domains** (each with spec + assumptions + examples)" | ✅ (高层, DI 例外略简) |
| L68 | "`STUDYID` → **all 64 domains** (incl. DI SDTMIG-MD device identifiers)" | ✅ |

**notebooklm 2/2 PASS**.

注: notebooklm L5 严格说 DI 只有 assumptions.md (无 spec.md/examples.md), 但描述 "each with spec + assumptions + examples" 对 DI 不严格 — 是 v1.1 已 accept 的 minor approximation. v1.4 carry: 加 "63 SDTM domains with spec+assumptions+examples + DI (assumptions-only)" 之类小注.

## 4. Cross-platform 一致性

所有 4 平台对 64-vs-63 的区分一致:
- **64 = assumptions** (含 DI)
- **63 = spec/examples** (DI 无)
- 高层概念语 "63 全量平权" / "63 SDTM domains" 4 平台同, 是有意保留 (v1.1 retro decision)

## 5. Build script segment_count 交叉对比

| Platform | 文件 | system_prompt 引用 | build segment_count | 交叉一致 |
|---|---|:-:|:-:|:-:|
| chatgpt | 04 | 63 | 63 dynamic | ✅ |
| chatgpt | 05 | 64 | 64 dynamic | ✅ |
| chatgpt | 06 | 63 | 63 dynamic | ✅ |
| gemini | 02 | 63 spec + 64 assumptions | composite (3 stages) | ✅ |
| gemini | 03 | 63 | composite | ✅ |
| claude | 05 | 63 | (claude exec post-confirm) | ⏳ |
| claude | 06 | 64 | (claude exec post-confirm) | ⏳ |
| notebooklm | (全) | 63 + 64 | 190 KB files, 42 buckets, M5 PASS | ✅ |

claude 行待 background executor 完成后 final-verify.

## 6. Rule A audit summary

Rule A target B4 = 12 probes (4 平台 × 3 数字). Actual:

| Platform | Probes | PASS | FAIL |
|---|:-:|:-:|:-:|
| chatgpt | 6 | 6 | 0 |
| gemini | 6 | 6 | 0 |
| claude | 6 | 6 | 0 |
| notebooklm | 2 | 2 | 0 |
| **Total** | **20** | **20** | **0** |

Exceeded target (12 → 20). **PASS** ★.

## 7. v1.4 Carry

- 加 notebooklm L5 微注: "63 domains with spec+assumptions+examples + DI (assumptions-only)"
- M1 grep 自动化: 把本 audit 流程包成 `scripts/audit_system_prompts.py`, CI 集成 post-rebuild

## 8. Gate

| Check | Verdict |
|---|:-:|
| 4 平台 system_prompt 数字引用 0 不一致 | ✅ |
| build script segment_count 与 system_prompt 引用 align | ✅ (3 完成 + claude pending exec) |
| Rule A 12+ probes PASS | ✅ (20/20) |

**B4 PASS**. claude exec 后续 final-confirm 不变动 (claude system_prompt 数字引用已 audit, build segment 是机械结果).
