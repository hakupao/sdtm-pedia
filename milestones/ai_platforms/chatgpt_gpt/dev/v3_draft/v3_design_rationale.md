# ChatGPT system_prompt v3 — Design Rationale

> Platform: ChatGPT GPT
> Writer: executor subagent (Rule D slot A2)
> Date: 2026-05-20
> Status: WRITER_PASS_REVIEWER_PENDING

---

## 1. Baseline vs New — Line / Section Diff

| Metric | v2.2 baseline | v3 new | Delta |
|--------|-------------|--------|-------|
| Total lines | 120L | 119L | -1L (-0.8%) |
| Sections | 7 (Role, KB, Routing, 回答規範, 边界处理, 工作流程, Starters) | 10 (Role, KB+Routing merged, R1-R5, Boundary, Starters) | restructured |
| Fossil annotations | present ("v2.2 新增", inline version markers) | 0 | -100% |
| Method label anchor | absent | present (PP §6.3.5.9.3, line 81) | NEW |
| regex-gated CO-N table | absent (implicit via prose) | explicit 4-trigger table (lines 68-78) | NEW |
| 5 essential rules | absent (distributed prose) | explicit R1-R5 headers | NEW |

**Note on line count**: v2.2 was nominally 120L but the header claimed "LIVE post smoke v4 R1 Q1 拼写 MINOR fix" — a fossil annotation. v3 is 119L, within the 64-120L target band.

---

## 2. R1-R5 Location + Line Numbers

| Rule | Header line | Content lines | Trigger |
|------|------------|--------------|---------|
| R1 — KB-Grounding Primary | 48 | 49-52 | always |
| R2 — Anti-Hallucination Triple-Anchor | 54 | 55-63 | regex-gated SDTM-shaped var |
| R3 — Domain Scope Guards + Method Label Anchors | 64 | 65-85 | regex match → anchor |
| R4 — Response Format | 87 | 88-96 | always |
| R5 — Premise Correction | 97 | 98-103 | conditional (wrong premise) |

---

## 3. regex-gated CO-N Table Location + Line Numbers

Section: `## R3 — Domain Scope Guards (regex-gated CO-N table)`, lines 64-85.

Code block containing triggers: lines 68-79.

| Trigger | Line | Pattern |
|---------|------|---------|
| biospecimen | 70 | `(biospecimen\|specimen\|sample\|血样\|尿样\|组织\|标本\|血液\|血浆\|血清)` |
| file format | 72 | `(XPT\|Dataset[ -]?JSON\|Define[ -]?XML\|JSON\|XML\|SAS)` |
| IS scope shift | 74 | `(antibody\|IgG\|IgM\|MMR\|HIV\|antimicrobial\|antibod)` |
| SDTM-shaped var | 76 | `^[A-Z]{2,5}[A-Z0-9]{0,12}$` |

All 4 triggers match design_spec_v9.md § 1.4 exactly.

---

## 4. 0 Fossil Annotation Self-Grep

```
grep -cE "v[0-9]+ 改動|v[0-9]+ 新增|post-R[0-9]" system_prompt_v3.md
→ 0 (exit 1, no matches)
```

Additional checks run:
```
grep -c "v2\.2 新增\|v2\.1 新增\|v1 新增\|LIVE post" system_prompt_v3.md
→ 0
```

v2.2 baseline had the following fossil markers removed:
- Header: `v2.2 LIVE post smoke v4 R1 Q1 拼写 MINOR fix — post-apply Q1 PASS 2026-04-24`
- Inline: `(v2.2 新增, smoke v4 R1 Q1 拼写 MINOR 修)` in 回答规范 section (original line 68)

All removed. Header now: `v3 LIVE 2026-05-20 — clean rewrite (post v1.3 light sanity feedback)`.

---

## 5. Method Label Anchor — Location + 4 Mappings

**Location**: Section `## R3`, line 81 (after the regex trigger table).

**Text**: `Method A = Many-to-Many | Method B = One-to-Many | Method C = Many-to-One | Method D = One-to-One`

**4 mappings confirmed**:
- Method A = Many-to-Many (MM)
- Method B = One-to-Many (OM)
- Method C = Many-to-One (MO)
- Method D = One-to-One (OO)

**Rationale**: v1.3 Phase C Q-S2 ChatGPT answered Method A=Many-to-One (= KB Method C), a label drift caused by internal prior overriding KB. The explicit anchor in R3 forces the model to look up §6.3.5.9.3 in `06_domain_examples_all.md` before assigning labels. Placed in R3 (domain scope guards) because PP-PC RELREC method labeling is a domain-specific scope issue.

---

## 6. Platform-Specific Carry-Over Checklist (design_spec § 2.2)

Per design_spec_v9.md § 2.2:

| Item | Status | Evidence |
|------|--------|---------|
| KB 9 文件 multi-step routing 保留 | PASS | KB table lines 10-30; routing table lines 32-45 |
| v2.2 fossil annotation 移除 | PASS | grep 0 (§4 above) |
| Method label anchor (PP §6.3.5.9.3) | PASS | Line 81, 4 mappings A=MM/B=OM/C=MO/D=OO |
| KB-grounding primary default | PASS | R1 lines 48-52; routing priority note line 45 |
| 5 essential rules R1-R5 | PASS | §2 table above |
| regex-gated CO-N 4 triggers | PASS | §3 table above; lines 70/72/74/76 |
| Header style per design_spec § 1.5 | PASS | Lines 1-3: `# <Title> — <Role>` + `> v3 LIVE ...` |
| 0 fossil annotation | PASS | §4 above |
| Line count 64-120L | PASS | 119L |

All carry-over items satisfied.

---

## 7. Rule A Self-Spot-Check Summary (5/5 PASS)

| Probe | Check | Result |
|-------|-------|--------|
| 1 | R1-R5 all present | PASS (lines 48/54/64/87/97) |
| 2 | regex-gated CO-N 4 triggers | PASS (lines 70/72/74/76) |
| 3 | 0 fossil annotation | PASS (grep=0) |
| 4 | Method label anchor 4 mappings | PASS (line 81) |
| 5 | Line count 64-120L | PASS (119L) |
