# Q4 (B1 — LB vs MB vs IS 边界) 三场景选域

> Date: 2026-04-22 / Account: bojiang.zhang.0904@gmail.com / Fresh chat

---

## 题

以下 3 个实验室检验结果, 在 SDTMIG v3.4 下分别记录到哪个域 (LB / MB / IS)?
- 场景 A: 疫苗试验, baseline 检测受试者血清中抗麻疹病毒 IgG 抗体滴度 (测过往感染或接种史), 数值 1:128
- 场景 B: 抗肿瘤单抗治疗后, 受试者血清中检测抗药物抗体 (ADA) 阳性/阴性 + 滴度
- 场景 C: 受试者痰样做结核杆菌 (Mycobacterium tuberculosis) 培养, 结果 positive

每个场景给出: (i) 域名; (ii) 理由 (为什么不是另外两个域); (iii) Topic 变量值示例. v3.4 下边界规则是什么?

## NotebookLM 答 (full text)

在 SDTMIG v3.4 框架下, 这三个场景的检验结果应分别归入 **IS、IS 和 MB** 域。以下是详细的分类理由、Topic 变量示例及 v3.4 边界规则。

### 场景 A: 基线期检测抗麻疹病毒 IgG 抗体滴度

被测物质: 抗麻疹病毒 IgG 抗体 (测量自然感染或过往接种史) **归属域: IS (Immunogenicity Specimen Assessments)**

(i) 域名: **IS**
(ii) 理由 (边界分析): 根据 IS 域假设 2, IS 域不仅用于记录对试验治疗的免疫反应, 还用于记录由过敏原、微生物 (或疫苗) 诱导的宿主免疫反应 (如抗微生物的抗体反应) [1]。即使这是基线期 (用于评估自然感染或过往非研究疫苗的免疫力), 它依然是测量免疫原性反应, 必须放入 IS 域 [2]。为了与研究疫苗诱导的反应区分开, 通常将 `ISCAT` 赋值为 `NON-STUDY-RELATED IMMUNOGENICITY` [2]。
- 为什么不是 MB: MB 用于直接识别样本中病原体 (微生物或其抗原) 的存在 [3,4]。场景 A 测量的是宿主产生的抗体, 而非病毒本身。
- 为什么不是 LB: 虽然 LB 包含一般实验室检查, 但针对特定抗原/微生物的免疫应答抗体明确由 IS 域接管 [1]。

(iii) Topic 变量示例:
- `ISTESTCD` (Req): `RBOIGGAB`
- `ISTEST` (Req): `Rubeola IgG Antibody`
- 注: 使用 NCI C120525/C120526 受控术语 [5,6]。或可使用 ISTESTCD = `MBIGGAB` (Microbial-induced IgG Antibody) 配合 `ISBDAGNT` (Perm) = `MEASLES VIRUS` [7,8]。

### 场景 B: 抗肿瘤单抗治疗后的抗药抗体 (ADA) 检测

被测物质: ADA (Anti-Drug Antibody) 阳性/阴性及滴度 **归属域: IS**

(i) 域名: **IS**
(ii) 理由: IS 域设立初衷及核心作用就是记录评估治疗 (如生物制品、药物、疫苗) 是否在受试者体内诱发了免疫反应的数据 [1]。
- 为什么不是 LB: ADA 是免疫原性测量, 不是常规生化。
- 为什么不是 MB: ADA 不涉及微生物直接检出。

(iii) Topic 变量示例:
- 配合 `ISTESTOO` (Test Operational Objective, Perm) 填入 `SCREEN`、`CONFIRM` 或 `QUANTIFY` 以区分检测层级 [9,11]
- `ISBDAGNT` 填药物名

### 场景 C: 痰样结核杆菌 (Mycobacterium tuberculosis) 培养

被测物质: 结核杆菌 (鉴定其存在) **归属域: MB (Microbiology Specimen)**

(i) 域名: **MB**
(ii) 理由 (边界分析): 针对病原体或抗原的直接鉴定测试 (不论使用培养、核酸扩增 NAAT、还是革兰氏染色), 均记录在 MB 域 [3,4]。
- 为什么不是 IS: 培养结核杆菌是直接检测病原体本身的存在, 而不是测定宿主对其产生的免疫 (抗体) 反应 [1,3]。
- 为什么不是 LB: 虽然尿液分析、白细胞计数等在 LB 域, 但直接定性/定量特定微生物的发现属于 Microbiology 类, 应当记录在专门的 MB 域中 [3,12]。

(iii) Topic 变量示例:
- `MBTESTCD` (Req): `MTB`
- `MBTEST` (Req): `Mycobacterium tuberculosis`
- 注: 配合 `MBORRES` (Exp) = `POSITIVE` [13]。来自受控术语 NCI C120527/C120528 [5,6]。

### SDTMIG v3.4 下的 LB / MB / IS 边界判定规则

- **IS 与 LB 的边界**: 任何测量宿主对治疗、微生物、自身抗原产生抗体或细胞介导的免疫反应均在 IS 域 [1]。**核心例外**: 细胞因子 (Cytokines)、趋化因子 (chemokines) 以及补体蛋白 (complement proteins) 的测量被归类为一般性临床检验, 必须记录在 LB 域 [1]。
- **IS 与 MB 的边界**: ... (后续提及 MS 用于药敏 MIC, MI 用于组织病理)
- **LB 与 MI (Microscopic Findings) 的边界**: 血液、尿液中游离细胞的常规形态学/计数显微镜检查归在 LB 域 [12]; 组织样本的组织学/组织病理学显微镜检查归在 MI 域 [12]。

## Verdict

| Criterion | Required | Got | Status |
|---|---|---|:---:|
| Scenario A → IS (v3.4 update) | IS, with anti-microbial Ab in IS scope | IS + ISCAT=NON-STUDY-RELATED IMMUNOGENICITY + assumption 2 cited | ✅ |
| Scenario B (ADA) → IS | IS | IS + ISTESTOO operational objective | ✅ |
| Scenario C (Mtb culture) → MB | MB | MB + MBTESTCD=MTB + MBORRES=POSITIVE | ✅ |
| Boundary rule v3.4 | IS=immune response, MB=direct detection, LB=routine | 完整 IS/LB/MB 三元 + cytokine 在 LB 例外 + MI 边界 | ✅ |
| 给出理由 + Topic 示例 | (i)(ii)(iii) 全 | All 3 scenarios with full (i)(ii)(iii) | ✅ |

**Verdict**: ✅ **PASS** (1 / 1) — 5 项判据全中。Scenario A 正确识别 v3.4 IS scope 扩展 (anti-microbial antibody 全归 IS, 含 baseline), 配合 ISCAT 区分。Scenario C 直接检出 → MB. 加分: cytokine 在 LB 例外明文 + MI 组织病理边界 + ISTESTOO SCREEN/CONFIRM/QUANTIFY 三档。无 FAIL 触发。
