# NotebookLM — Q4 LB vs MB vs IS 三场景 (R1 smoke v4.0)

> **执行时间**: 2026-04-22 晚 | **题类**: Q4 (B1 域边界) | **Fresh chat**: ✓ (删除 history 后重启)

## Raw 回答摘要

- **场景 A (抗麻疹病毒 IgG baseline)**: **IS** ✓ — ISTESTCD=MBIGGAB, ISBDAGNT=MEASLES MORBILLIVIRUS, ISCAT=NON-STUDY-RELATED IMMUNOGENICITY (C120525 Req Topic)
- **场景 B (ADA)**: **IS** ✓ — ISTESTCD=ADA_BAB (Binding Antidrug Antibody), ISBDAGNT=药物名, ISTSTOPO=SCREEN/CONFIRM/QUANTIFY
- **场景 C (Mtb 培养)**: **MB** ✓ — MBTESTCD=MTB, MBTSTDTL=DETECTION, MBORRES=POSITIVE (C120527 Req)

**边界规则**: LB 细胞因子/补体 + 常规生化 / MB 微生物直接检出 / IS 免疫原性. IS vs MB 例外: Ag/Ab 组合检测归 MB. MB vs MS: 药敏测试走 MS.

**Citation**: 多 inline [18_fnd_device_da_dd_gf_is.md] [15_fnd_biomarkers_mb_mi_ms_mk.md] + assumptions

## Verdict: **PASS** (全 3 场景准确映射 + Topic 变量 + 边界规则完整)
