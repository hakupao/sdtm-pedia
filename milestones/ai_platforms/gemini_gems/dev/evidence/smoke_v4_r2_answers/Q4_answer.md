# Gemini Gems — Q4 LB/MB/IS 三场景 (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/fc0afcefd2e97e30
> **题类**: Q4 (B1 域边界, R1 PARTIAL)
> **R1 baseline**: PARTIAL (未严格逐场景, "通用原则" 避开)
> **v6 target fix**: "多场景题逐场景显式答" 强制规则

## Raw 回答 (DOM 原文)

**场景 A (抗麻疹 IgG baseline, 疫苗试验)**:
- (i) 域: **IS (Immunogenicity Specimen Assessments)** ✓
- (ii) 理由: IS 覆盖免疫原性评估 + 既往感染/接种抗体检测; 非 LB (不是常规生化/血液学); 非 MB (测抗体 = 免疫反应 surrogate, 非病毒本身)
- (iii) ISTEST="Measles Virus IgG Antibody" / ISTESTCD="MSLIGG"
- 源路径: IS/assumptions.md Assumption 1 + §12.3.1

**场景 B (ADA 抗药物抗体)**:
- (i) 域: **IS** ✓
- (ii) 理由: IS 域涵盖治疗性蛋白诱导的 ADA 检测, 属免疫原性评估核心; 非 LB (业务语义归 immunogenicity); 非 MB (ADA 不是微生物)
- (iii) ISTEST="Anti-Drug Antibody" / ISTESTCD="ADA"
- 源路径: IS/assumptions.md Assumption 2 + §12.3.1

**场景 C (Mtb 痰培养)**:
- (i) 域: **MB (Microbiology Specimen)** ✓
- (ii) 理由: MB 记录微生物鉴定 (细菌/病毒/真菌); 非 LB (不记微生物鉴定); 非 IS (测病原非免疫反应)
- (iii) MBTEST="Mycobacterium tuberculosis" / MBTESTCD="MYCOTB" / MBORRES="POSITIVE"
- 源路径: MB/assumptions.md + §12.5.1

**v3.4 边界规则总结 section** (streaming tail, DOM partial captured): 依据 04_business_scenarios §4.3 + 各域 Assumptions.

## Self-score verdict

**PASS+** — **R1 PARTIAL → R2 PASS 修复生效**

- 3 场景全对 (A=IS, B=IS, C=MB) ✓
- **每场景严格 (i) (ii) (iii) 三段式** ✓ — v6 "多场景题逐场景显式答" 规则 WORKING, 未使用 "通用原则" 避开
- 每场景"非其他域"理由 provided (non-A非B非C 对比) ✓
- 场景 A 正确识别 v3.4 IS scope 变化 (baseline anti-microbial antibody v3.4 统一归 IS, 非 v3.3 MB) ✓ — **R1 FAIL 判据 "场景 A 答 MB" 成功规避**
- 边界规则总结 section in progress at capture, 已给 IS (免疫应答) vs MB (微生物直接检出) vs LB (常规生化) 三分
- 源路径逐场景给 ✓ (CO-3 合规)

**R1 vs R2 对比**: R1 PARTIAL → R2 PASS+. **v6 Q4 micro-fix 明确生效**. 关键改善: 逐场景 (i)(ii)(iii) 结构化 + 场景 A 识别 v3.4 IS scope 变化.
