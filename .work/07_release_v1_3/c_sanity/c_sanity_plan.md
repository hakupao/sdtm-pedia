# v1.3 Phase C — light sanity plan (4 平台 × 4 题, post-upload)

> Date: 2026-05-20
> Scope: User option α 简化版 — 不跑 17 全题 (留 v1.4), 跑 4 平台 × 4 v1.3-targeted sanity
> Goal: 确认 4 平台 KB rebuild 实际生效 (PP RELREC / BECAT / TR typo / DI domain 4 个 v1.3 改动 reach 用户)

---

## 4 题 sanity (各题 target v1.3 KB 改动)

### Q-S1 — BECAT EXTRACTION (Phase A2 v1.3 改 KB)

> 在 SDTMIG v3.4 BE 域 (Biospecimen Events) 里, BECAT 变量除了 CDISC canonical 三个 examples (COLLECTION / PREPARATION / TRANSPORT) 之外, sponsor 还能扩展什么值? 给一个 DNA / molecular biology specimen processing 场景下的常见扩展例子, 并说明 BECAT 是否 sponsor-extensible.

**期望命中**:
- COLLECTION / PREPARATION / TRANSPORT 三个 CDISC canonical 例
- EXTRACTION (sponsor-extensible, DNA/molecular biology)
- BECAT is sponsor-extensible (CDISC Notes 明示)

### Q-S2 — PP RELREC linking (Phase A1 v1.3 改 KB)

> 在 SDTMIG v3.4 里, PP 域 (PK Parameters) 如何与 PC 域 (PK Concentrations) 通过 RELREC 数据集关联? 请简短列出 4 种 method (A/B/C/D), 说明每种用什么 IDVAR + IDVARVAL 组合 (例如 PCSEQ / PCGRPID / PPSEQ / PPGRPID), 并举一个 relrec.xpt 示例 (USUBJID = ABC-123-0001).

**期望命中**:
- Method A (Many to Many) — PCGRPID + PPGRPID
- Method B (One to Many) — PCSEQ + PPGRPID
- Method C (Many to One) — PCGRPID + PPSEQ
- Method D (One to One) — PCSEQ + PPSEQ
- relrec.xpt 表 (ABC-123-0001 PPSEQ 1..7 in Method C)

### Q-S3 — TR domain typo fix (Phase A3 §6.3.12.2 v1.3 改 KB)

> 在 TR 域 (Tumor Results) 标准化测量示例表里, 哪个变量存 "standardized result, original or standard unit, numeric value" (数值)? 哪个变量存 "standardized result, standard units" (单位字段)? 简短说明 TRSTRESN 与 TRSTRESU 的区别.

**期望命中**:
- TRSTRESN = standardized numeric value
- TRSTRESU = standardized unit (单位)
- 不会把 TRSTRESN 错标为 unit (v1.3 fixed the typo)

### Q-S4 — DI domain (NotebookLM bucket 25 重点)

> DI 域 (Device Identifiers) 是哪个 SDTMIG version 引入的? 它属于哪个 SDTM dataset class (Special-Purpose / Events / Findings / Trial Design / Study Reference)? 请列出 DI 主要变量 (至少 3 个 Core=Req 变量) + 描述其用途.

**期望命中**:
- SDTMIG-MD (Medical Devices, v3.0 / 引入 1.x)
- Study Reference (与 TI/TS/OI 同 class)
- Core variables: 至少 STUDYID, DOMAIN, USUBJID + DI-specific 变量

---

## 执行 strategy

### Quota
- Gemini Pro: 4 题/window (刚好够 sanity 4 题)
- ChatGPT / Claude / NotebookLM: 无 quota 限

### 顺序
按题串行 (而非按平台串行) — 这样 Gemini 单题 Pro response 长 时, 其他 3 平台可以 fire-and-forget 并行.

Per 题 flow:
1. Gemini fill + send → wait response (~30-60s)
2. ChatGPT fill + send → wait
3. Claude fill + send → wait
4. NotebookLM fill + send → wait
5. 主 session 评判 4 平台答案 (Strict 判据)
6. 写 evidence per 题

### Strict 判据 (per R3/R4 sanity)

| Verdict | 标准 |
|---|---|
| **PASS+** | 答出全部期望要点 + 额外深度 (PDF 行号 / cross-ref / extra example) |
| **PASS** | 答出全部期望要点, 无遗漏 |
| **PARTIAL** | 答出 ≥50% 要点 |
| **FAIL** | 跑题 / 关键变量名错 / 域错 / 幻觉 / 拒答 |

### 决策树

```
4 题 × 4 平台 = 16 cells
≥14/16 PASS (允许 ≤2 PARTIAL)
  → v1.3 sanity APPROVE → 进 Phase D cut release/v1.3/

≥1 FAIL on previously-PASS platform
  → halt + 写 fail report
  → 决策点: rollback / patch / accept doc

PARTIAL > 4
  → halt + 扩 sample 排查
```

---

## Evidence 路径

- `.work/07_release_v1_3/c_sanity/evidence/q_s{1,2,3,4}_<platform>.md` (16 文件)
- `.work/07_release_v1_3/c_sanity/C_SANITY_RETROSPECTIVE.md` (跑完后写)

---

## 开始

Q-S1 fire 顺序: Gemini → ChatGPT → Claude → NotebookLM.
