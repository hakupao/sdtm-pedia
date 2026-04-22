# Claude Projects — Q2 CP 流式 CD4+ ACTIVATED (R1 smoke v4.0)

> **执行时间**: 2026-04-22 PM | **题类**: Q2 (A2 v3.4 新域 CP)

## Raw 回答摘要

- **域**: CP (Cell Phenotype Findings) ✓ / Class: Findings / Structure: one-record-per-test-per-specimen-per-timepoint-per-visit-per-subject
- **决定性证据**: CPMETHOD spec "Ex: FLOW CYTOMETRY" + CPCAT "IMMUNOPHENOTYP..." (C181171) + IS assumption #4 "Flow cytometry data should be modeled in CP domain, §6.3.5.3"
- **(a) Topic**: CPTESTCD=TLYH (C181173) + CPTEST="T Lym Help" (C181174) — CP assumption #6a.i: CPTEST 填细胞群名, 非 marker/state
- **(b) 三类场景表**:
  | 场景 | CPTESTCD/CPTEST | CPSBMRKS | CPCELSTA | CPCSMRKS |
  |---|---|---|---|---|
  | 全部 T helper | TLYH / "T Lym Help" | 空 | 空 | 空 |
  | T helper 亚群 | TLYHS (C184351) / "T Lym Help Sub" | CXCR5+PD-1+ (Tfh) | 空 | 空 |
  | 活化 T helper (本案) | TLYH / "T Lym Help" | 空 | ACTIVATED | Ki67+ |
  - CPSBMRKS 定义亚群 vs CPCELSTA+CPCSMRKS 定义状态 — **正交语义不混用**
- **(c)** CPCELSTA=ACTIVATED (C64382) + CPCSMRKS=Ki67+ + CPMRKSTR="CD3+CD4+Ki67+" (Exp 完整 gate)
  - CP assumption #4 (配对规则) + #6a.ii (CPMRKSTR Exp) + #8 (marker string 格式: 无分隔, +/-/lo/mid/hi)
- **(d)** CPMETHOD=FLOW CYTOMETRY (C85492) + CPANMETH (算法) + CPSPEC=PBMC (C78734) + CPABCLID (抗体 clone ID) + CPBDAGNT (binding agent)
- **(e) CP vs LB vs IS vs MB boundary 表** (IS assumption #2 "phenotyping component that relies on using cell markers"):
  - 流式/CyTOF/免疫荧光 marker 识别 → CP
  - CBC 血常规 无 marker → LB
  - 血清 soluble analytes → LB (IS #6)
  - ADA 免疫原性 → IS
  - 微生物 Ag/Ab → MB (IS #5)
- **完整 CT C181172 Cell State 8 terms**: ACTIVATED (C64382) / APOPTOTIC / EXHAUSTED / NON-PROLIFERATING / NON-VIABLE / PROLIFERATING / SENESCENT / VIABLE

**源**: CP/spec.md (05_mega_spec:361-436) + CP/assumptions.md (06_assumptions:137-179) + IS/assumptions.md #4/#5/#6 (446-448) + terminology/core/cp_part2.md (13a:45-60) + cp_part*.md (13a:3769, 4117-4123, 4132)

## Verdict: **PASS+** (最完整, CDISC reviewer 级 + 8-term CT 全表 + 4-domain 边界表)
