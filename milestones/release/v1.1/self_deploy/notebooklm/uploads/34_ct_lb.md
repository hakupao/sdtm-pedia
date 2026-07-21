# 34_ct_lb

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `34`
> - **Concept**: CT core: lab codelists (~180K words, 单 slot 内)
> - **Merged files**: 4
> - **Words**: 129,606
> - **Chars**: 807,306
> - **Sources**:
>   - `terminology/core/lb_part1.md`
>   - `terminology/core/lb_part2.md`
>   - `terminology/core/lb_part3.md`
>   - `terminology/core/lb_part4.md`

---
## Source: `terminology/core/lb_part1.md`

# Laboratory Codelists (Part 1)

> Codelists in this file: 1

## Laboratory Analytical Method Calculation Formula (C160922)

Extensible: Yes

| Code | CDISC Submission Value | CDISC Synonym(s) | CDISC Definition |
|------|----------------------|-------------------|------------------|
| C172486 | ASH FIBROSURE FORMULA | ASH FibroSURE Formula; ASH Test | A proprietary algorithm derived from the FibroTest liver fibrosis algorithm that is used to measure liver fibrosis, hepatic steatosis, and alcoholic steatohepatitis. It includes ten serum markers: alpha-2-macroglobulin, apolipoprotein A1, total bilirubin, gamma-glutamyltransferase, haptoglobin, alanine aminotransferase, aspartate aminotransferase, glucose, total cholesterol, and triglycerides, and adjusts for age, gender, height, and weight. (NCI) |
| C161338 | CKD-EPI CREATININE FORMULA |  | A formula to estimate glomerular filtration rate that takes into account sex, age, race, and serum creatinine (SCr). eGFR(mL/min/1.73 m2)=141 x min(SCr/k, 1)^a x max(SCr/k, 1)^-1.209 x 0.993^Age x 1.018 [if female] x 1.159 [if black] where: SCr is in mg/dL; k=0.7 for Female and 0.9 for Male; a=-0.329 for female and -0.411 for male. (Levey AS, Stevens LA, Schmid CH, Zhang YL, Castro AF, Feldman HI, Kusek JW, Eggers P, Van Lente F, Greene T. A new equation to estimate glomerular filtration rate. Ann Intern Med. 2009;150:604-612.) |
| C161340 | CKD-EPI CREATININE-CYSTATIN C FORMULA |  | A formula to estimate glomerular filtration rate that takes into account sex, age, race, serum creatinine (SCr) and serum cystatin C (Scys). eGFR(mL/min/1.73 m2)=135 x min(SCr/k, 1)a x max(SCr/k, 1)-0.601 x min(Scys/0.8, 1)-0.375 x max(Scys/0.8, 1)-0.711 x 0.995^Age x 0.969 [if female] x 1.08 [if black]. (Inker LA, Schmid CH, Tighiouart H, et al. Estimating glomerular filtration rate from serum creatinine and cystatin C. N Engl J Med. 2012;367(1):20-29.) |
| C161339 | CKD-EPI CYSTATIN C FORMULA |  | A formula to estimate glomerular filtration rate that takes into account sex, age, race, and serum cystatin C (Scys). eGFR(mL/min/1.73 m2)=133 x min(Scys/0.8, 1)^-0.499 x max (Scys/0.8, 1)^-1.328 x 0.996^Age x 0.932 [if female]. (Inker LA, Schmid CH, Tighiouart H, et al. Estimating glomerular filtration rate from serum creatinine and cystatin C. N Engl J Med. 2012;367(1):20-29.) |
| C161341 | CKD-EPI FORMULA | Chronic Kidney Disease Epidemiology Collaboration Formula; CKD-EPI GFR Formula | An unspecified CKD-EPI-based formula to estimate glomerular filtration rate that takes into account factors such as sex, age, race, and biomarker measurements. |
| C161342 | COCKCROFT-GAULT FORMULA |  | A formula to estimate creatinine clearance that takes into account sex, age, weight, and serum creatinine (SCr). CCr=(140 - Age) x Wgt (Kg) / 72xCrt (mg/dL) x 1 (if M) or 0.85 (if F), for conventional units. CCr=(140 - Age) x Wgt (Kg) / 72xCrt (MCMOL/L) x 88.4 x 1 (if M) or 0.85 (if F) [If Wgt is in lbs; Wgt (Kg) = Wgt (lbs) x 0.45], for SI units. (Cockcroft, D.W. and M.H. Gault. Prediction of creatinine clearance from serum creatinine. Nephron. 1976. 16(1):31-41.) |
| C172489 | FIBROMETER FORMULA |  | A formula that estimates liver pathology through the assessment of a six-parameter blood test, taking into account subject age. Fibrometer regression function = -0.007 platelets (Giga/L) - 0.049 prothrombin index (%) + 0.012 aspartate aminotransferase (UI/L) + 0.005 alpha2-macroglobulin (mg/dL) + 0.021 hyaluronate (g/L) - 0.270 urea (mmol/L) + 0.027 age (years) + 3.718. (Cales P, Oberti F, Michalak S et al. A novel panel of blood markers to assess the degree of liver fibrosis. Hepatology. 2005 Dec;42(6):1373-81.) |
| C170576 | FIBROSIS 4 FORMULA | FIB-4 Formula | A formula that estimates liver pathology through the assessment of a three-parameter blood test, taking into account subject age. FIB-4 = age ([yr] x AST [U/L]) / ((PLT [10(9)/L]) x (ALT [U/L])(1/2)). (Sterling RK, Lissen E, Clumeck N, et. al. Development of a simple noninvasive index to predict significant fibrosis patients with HIV/HCV co-infection. Hepatology 2006;43:1317-1325.) |
| C172485 | FIBROTEST FORMULA | FibroSURE Formula; FibroTest Formula; FibroTest-HCV Formula; FibroTest/FibroSURE Formula | A formula that estimates liver pathology through the assessment of a six-parameter blood test, taking into account subject age and sex. z = 4.467 x log10[Alpha2-Macroglobulin(g/L)] - 1.357 x log10[Haptoglobulin(g/L) + 1.017 x log10[Gamma Glutamyl Transferase (IU/L)] +0.0281 x [Age] + 1.737 x log10[Bilirubin umol/L] - 1.184 x [Apolipoprotein A1(g/L)] + 0.301 x [Sex (female=0, Male=1) - 5.54. (US Patent 6631330) |
| C174289 | GMI % FORMULA | Glucose Management Indicator % Formula | A formula to calculate the glucose management indicator (GMI) as a percentage. GMI = 3.31 + 0.02392 x [mean glucose in mg/dL]. (Richard M. Bergenstal, Roy W. Beck, Kelly L. Close, et al. Glucose Management Indicator (GMI): A New Term for Estimating A1C From Continuous Glucose Monitoring. Diabetes Care 2018 Nov; 41(11): 2275-2280.) |
| C174290 | GMI MMOL/MOL FORMULA | Glucose Management Indicator mmol/mol Formula | A formula to calculate the glucose management indicator (GMI) in mmol/mol. GMI = 12.71 + 4.70587 x [mean glucose in mmol/L]. (Richard M. Bergenstal, Roy W. Beck, Kelly L. Close, et al. Glucose Management Indicator (GMI): A New Term for Estimating A1C From Continuous Glucose Monitoring. Diabetes Care 2018 Nov; 41(11): 2275-2280.) |
| C172488 | HEPASCORE FORMULA | Hepatoscore Formula | A formula that estimates liver pathology through the assessment of a four-parameter blood test, taking into account subject age and sex. Hepascore = y/(1 + y) with y = exp (-4.185818 - (0.0249 x age) + (0.7464 x 1 if male, 0 if female gender) + (1.0039 x a2 macroglobulin) + (0.0302 x hyaluronate) + (0.0691 x bilirubin) - (0.0012 x gamma-glutamyl transferase)). (Adams LA, Bulsara M, Rossi E et al. Hepascore: an accurate validated predictor of liver fibrosis in chronic hepatitis C infection. Clin Chem. 2005 Oct;51(10):1867-73.) |
| C181401 | IDMS-MDRD STUDY EQUATION WITH JSN-CKDI COEFFICIENT 0.741 IMAI 2007 |  | A formula to estimate glomerular filtration rate in Japanese subjects that takes into account age, sex, and serum creatinine. eGFR (mL/min/1.73 m2) = 0.741 x SCr^-1.154 x 175 x Age^-0.203 x 0.742 (if female). (Enyu Imai, Masaru Horio, Kosaku Nitta, Kunihiro Yamagata, Kunitoshi Iseki, Yusuke Tsukamoto, Sadayoshi Ito, Hirofumi Makino, Akira Hishida, Seiichi Matsuo. Modification of the Modification of Diet in Renal Disease (MDRD) Study Equation for Japan. Am J Kidney Dis. 2007 Dec;50(6):927-37.) |
| C161343 | MDRD 4 VARIABLE FORMULA |  | A formula to estimate glomerular filtration rate that takes into account age, sex, race, and serum creatinine (Scr). eGFR (mL/min/1.73 m2) = 186 x (Scr)^-1.154 x (Age)^-0.203 x (0.742 if female) x (1.210 if African American). (Levey AS, Bosch JP, Lewis JB, Greene T, Rogers N, Roth D. A more accurate method to estimate glomerular filtration rate from serum creatinine: a new prediction equation. Modification of Diet in Renal Disease Study Group. Ann Intern Med. 1999;130:461-70.) |
| C161344 | MDRD 5 VARIABLE FORMULA |  | A formula to estimate glomerular filtration rate that takes into account age, sex, race, serum creatinine and serum urea nitrogen. eGFR (mL/min/1.73 m = 270 x creatinine (mg/dl)^-1.007 x age^-0.180 x 1.178 (if black) x 0.762 (if female) x serum urea nitrogen^-0.169. (Levey AS, Greene T, Kusek JW, Beck GJ, MDRD study group. A simplified equation to predict glomerular filtration rate from serum creatinine. J Am Soc Nephrol 2000; 11: A0828.) |
| C161345 | MDRD 6 VARIABLE FORMULA |  | A formula to estimate glomerular filtration rate that takes into account age, sex, race, serum creatinine, serum urea nitrogen, and albumin. eGFR (mL/min/1.73 m2) = 170 x (SCr/88.4)^-0.999 x age^-0.176 x (SU x 2.78)^-0.170 x albumin^0.318 x (0.762, if female) x (1.18, if African American). (Levey AS, Greene T, Kusek JW, Beck GJ, MDRD study group. A simplified equation to predict glomerular filtration rate from serum creatinine. J Am Soc Nephrol 2000; 11: A0828.) |
| C161346 | MDRD ENZYMATIC FORMULA | IDMS MDRD | A formula to estimate glomerular filtration rate that takes into account age, sex, race, and serum creatinine. eGFR (mL/min/1.73 m2)=175 x (serum Cr [conv mg/dL])^-1.154 x (Age)^ -0.203 x (0.742 if female) x (1.212 if black), for conventional units. eGFR=175 x (serum Cr [SI UMOL/L]/88.4)^-1.154 x (Age)^ -0.203 x (0.742 if female) x (1.212 if black), for SI units. (Levey AS, Stevens LA, Schmid CH, Zhang YL, Castro AF, 3rd, Feldman HI, et al. A new equation to estimate glomerular filtration rate. Ann Intern Med. 2009;150(9):604-12.) |
| C161347 | MDRD ENZYMATIC JAPANESE FORMULA |  | A formula to estimate glomerular filtration rate in Japanese subjects that takes into account age, sex, and serum creatinine. eGFR (ml/min/1.73m2) = 194 x PD93 power^-1.094 x Age power^- 0.287 x Sex; where PD93 = Serum Cr (mg/dL), Sex = 1.00 for male and 0.739 for female. (Imai E, Horio M, Nitta K, Yamagata K, Iseki K, Tsukamoto Y, Ito S, Makino H, Hishida A, Matsuo S. Modification of the Modification of Diet in Renal Disease (MDRD) Study equation for Japan. Am J Kidney Dis. 2007 Dec;50(6):927-37.) |
| C176295 | MDRD FORMULA | MDRD GFR Formula; Modification of Diet in Renal Disease Formula | An unspecified MDRD-based formula to estimate glomerular filtration rate that takes into account factors such as sex, age, race, and biomarker measurements. |
| C172487 | NASH FIBROSURE FORMULA | NASH FibroSURE Formula; NASH Test | A proprietary algorithm derived from the FibroTest liver fibrosis algorithm that is used to measure liver fibrosis, hepatic steatosis, and non-alcoholic steatohepatitis. It includes ten serum markers: alpha-2-macroglobulin, apolipoprotein A1, total bilirubin, gamma-glutamyltransferase, haptoglobin, alanine aminotransferase, aspartate aminotransferase, glucose, total cholesterol, and triglycerides, and adjusts for age, gender, height, and weight. (NCI) |
| C161348 | SCHWARTZ METHOD FOR CHILDREN FORMULA |  | A formula to estimate glomerular filtration rate in children that takes into account age, height, and serum creatinine. eGFR (mL/min/1.73 m2) = k x Height (cm)/Serum creatinine (mg/dL) where k=0.33 for pre-term babies, 0.45 for full-term babies and 0.55 for girls ages 1-13 or 0.70 for boys ages 1-13. (Schwartz GJ, Gauthier B. A simple estimate of glomerular filtration rate in adolescent boys. J Pediatr. 1985 Mar;106(3):522-6.) |

## Source: `terminology/core/lb_part2.md`

# Laboratory Codelists (Part 2)

> Codelists in this file: 1

## Laboratory Test Code (C65047)

Extensible: Yes

| Code | CDISC Submission Value | CDISC Synonym(s) | CDISC Definition |
|------|----------------------|-------------------|------------------|
| C100429 | A1AGLP | Alpha-1 Acid Glycoprotein | A measurement of the alpha-1 acid glycoprotein in a biological specimen. |
| C181404 | A1ANTRPF | Alpha-1 Antitrypsin, Functional | A measurement of the functional alpha-1 antitrypsin in a biological specimen. |
| C80167 | A1ANTRYP | Alpha-1 Antitrypsin; Serum Trypsin Inhibitor | A measurement of the alpha-1 antitrypsin in a biological specimen. |
| C186022 | A1MCGEXR | Alpha-1 Microglobulin Excretion Rate | A measurement of the amount of alpha-1 microglobulin being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C100462 | A1MCREAT | Alpha-1 Microglobulin/Creatinine | A relative measurement (ratio or percentage) of the alpha-1 microglobulin to creatinine in a biological specimen. |
| C100461 | A1MICG | Alpha-1 Microglobulin; Protein HC | A measurement of the alpha-1 microglobulin in a biological specimen. |
| C80168 | A2MACG | Alpha-2 Macroglobulin | A measurement of the alpha-2 macroglobulin in a biological specimen. |
| C172524 | A73OXC | 7-Alpha hydroxy-4-cholesten-3-one; 7-alpha-Hydroxy-4-cholesten-3-one | A measurement of the 7-alpha-hydroxy-4-cholesten-3-one in a biological specimen. |
| C154761 | AAMAPAC | Alpha-Aminoadipate; Alpha-Aminoadipic Acid | A measurement of the alpha-aminoadipic acid in a biological specimen. |
| C154759 | AAMBTAC | Alpha-aminobutyrate; Alpha-Aminobutyric Acid; Homoalanine | A measurement of the alpha-aminobutyric acid in a biological specimen. |
| C100430 | AAP | Alanine Aminopeptidase | A measurement of the alanine aminopeptidase in a biological specimen. |
| C189527 | AATZPL | AAT Z-Polymer; Alpha-1 Antitrypsin Z-Polymer | A measurement of the polymers of Z-variant alpha-1 antitrypsin in a biological specimen. |
| C184526 | ABFBCA | AB-FUBINACA | A measurement of the synthetic cannabinoid AB-FUBINACA in a biological specimen. |
| C111124 | ABNCE | Abnormal Cells | A measurement of the abnormal cells in a biological specimen. |
| C150835 | ABNCECE | Abnormal Cells/Total Cells | A relative measurement (ratio or percentage) of abnormal cells to total cells in a biological specimen. |
| C150834 | ABNCELE | Abnormal Cells/Leukocytes | A relative measurement (ratio or percentage) of abnormal cells to leukocytes in a biological specimen. |
| C125939 | ABO | ABO Blood Group | The characterization of the blood type of an individual by testing for the presence of A antigen and B antigen on the surface of red blood cells. |
| C135397 | ABOA1 | ABO A1 Subtype | The characterization of the ABO blood group A1 subtype in an individual. (NCI) |
| C184527 | ABPNCA | AB-PINACA | A measurement of the synthetic cannabinoid AB-PINACA in a biological specimen. |
| C74699 | ACANT | Acanthocytes | A measurement of the acanthocytes in a biological specimen. |
| C74633 | ACANTRBC | Acanthocytes/Erythrocytes | A relative measurement (ratio or percentage) of acanthocytes to all erythrocytes in a biological specimen. |
| C80169 | ACE | Angiotensin Converting Enzyme | A measurement of the angiotensin converting enzyme in a biological specimen. |
| C135398 | ACETAMIN | Acetaminophen; Paracetamol | A measurement of the acetaminophen in a biological specimen. |
| C92247 | ACETOAC | Acetoacetate; Acetoacetic Acid | A measurement of the acetoacetic acid in a biological specimen. |
| C147288 | ACETONE | Acetone | A measurement of the acetone in a biological specimen. |
| C74838 | ACH | Acetylcholine | A measurement of the acetylcholine hormone in a biological specimen. |
| C96560 | ACHE | Acetylcholinesterase | A measurement of the acetylcholinesterase in a biological specimen. |
| C96559 | ACHRAB | Acetylcholine Receptor Antibody | A measurement of the acetylcholine receptor antibody in a biological specimen. |
| C80163 | ACPHOS | Acid Phosphatase | A measurement of the acid phosphatase in a biological specimen. |
| C147289 | ACRNCRNF | Acylcarnitine/Carnitine, Free | A relative measurement (ratio or percentage) of the acylcarnitine to free carnitine in a biological specimen. |
| C189522 | ACSPGM | Acid Sphingomyelinase | A measurement of the acid sphingomyelinase in a biological specimen. |
| C103348 | ACT | Activated Clotting Time; Activated Coagulation Time | A measurement of the inhibition of blood coagulation in response to anticoagulant therapies. |
| C189521 | ACTACEXR | Acetoacetate Excretion Rate; Acetoacetic Acid Excretion Rate | A measurement of the amount of acetoacetic acid being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C184510 | ACTB | Actin Beta; B-Actin; Beta-Actin | A measurement of the beta-actin in a biological specimen. |
| C74780 | ACTH | Adrenocorticotropic Hormone; Corticotropin | A measurement of the adrenocorticotropic hormone in a biological specimen. |
| C156535 | ACYCRNTN | Acylcarnitine | A measurement of the acylcarnitine in a biological specimen. |
| C156534 | ACYGLYCN | Acylglycine | A measurement of the acylglycine in a biological specimen. |
| C92286 | ACYLCAOX | Acyl CoA Oxidase; Acyl Coenzyme A Oxidase; Fatty Acyl Coenzyme A Oxidase | A measurement of the acyl coenzyme A oxidase in a biological specimen. |
| C147290 | ADAM8 | A Disintegrin And Metalloproteinase Domain 8; ADAM Metallopeptidase Domain 8; CD156a Antigen | A measurement of the ADAM metallopeptidase domain 8 protein in a biological specimen. |
| C187684 | ADAMTS13 | A Disintegrin-Like And Metalloprotease (Reprolysin Type) With Thrombospondin Type 1 Motif, 13; ADAM Metallopeptidase With Thrombospondin Type 1 Motif 13; von Willebrand Coagulation Factor Cleaving Protease ADAMTS13 | A measurement of the von Willebrand coagulation factor cleaving protease, ADAMTS13, in a biological specimen. |
| C184529 | ADBPNCA | ADB-PINACA | A measurement of the synthetic cannabinoid ADB-PINACA in a biological specimen. |
| C74847 | ADH | Antidiuretic Hormone; Vasopressin | A measurement of the antidiuretic hormone in a biological specimen. |
| C158233 | ADMA | Asymmetric Dimethylarginine; N,N-dimethylarginine | A measurement of asymmetric dimethylarginine in a biological specimen. |
| C187830 | ADMTS13A | A Disintegrin-Like And Metalloprotease (Reprolysin Type) With Thrombospondin Type 1 Motif, 13 Activity; ADAM Metallopeptidase With Thrombospondin Type 1 Motif 13 Activity; ADAMTS13 Activity; von Willebrand Coagulation Factor Cleaving Protease ADAMTS13 Activity | A measurement of the biological activity of von Willebrand coagulation factor cleaving protease, ADAMTS13, in a biological specimen. |
| C102257 | ADP | Adenosine Diphosphate | A measurement of the adenosine diphosphate in a biological specimen. |
| C74839 | ADPNCTN | Adiponectin | A measurement of the total adiponectin hormone in a biological specimen. |
| C132363 | ADPNHMW | Adiponectin, High Molecular Weight | A measurement of the high molecular weight adiponectin hormone in a biological specimen. |
| C74913 | ADSDNA | Anti-Double Stranded DNA | A measurement of the anti-double stranded DNA antibody in a biological specimen. |
| C98706 | AFACTXAA | Anti-Factor Xa Activity | A measurement of the ability of antithrombin to inactivate activated Factor X in a biological specimen. This test is used to monitor low molecular weight or unfractionated heparin levels in a biological specimen. |
| C74732 | AFP | Alpha Fetoprotein; Alpha-1-Fetoprotein | A measurement of the alpha fetoprotein in a biological specimen. |
| C147291 | AFPADJBW | Alpha Fetoprotein Adj for Body Weight | A measurement of alpha fetoprotein, which has been adjusted for body weight, in a biological specimen. |
| C96562 | AFPL1 | Alpha Fetoprotein L1 | A measurement of the alpha fetoprotein L1 in a biological specimen. |
| C96563 | AFPL2 | Alpha Fetoprotein L2 | A measurement of the alpha fetoprotein L2 in a biological specimen. |
| C96564 | AFPL3 | Alpha Fetoprotein L3 | A measurement of the alpha fetoprotein L3 in a biological specimen. |
| C96565 | AFPL3AFP | A Fetoprotein L3/A Fetoprotein | A relative measurement (ratio or percentage) of alpha fetoprotein L3 to total alpha fetoprotein in a biological specimen. |
| C124334 | AG1_5 | 1,5-Anhydroglucitol | A measurement of the 1,5-anhydroglucitol in a biological specimen. |
| C111126 | AHBDH | Alpha Hydroxybutyrate Dehydrogenase | A measurement of the alpha-hydroxybutyrate dehydrogenase in a biological specimen. |
| C181418 | AHTRZLM | Alpha-Hydroxytriazolam | A measurement of the alpha-hydroxytriazolam a biological specimen. |
| C122091 | ALA | Alanine | A measurement of the alanine in a biological specimen. |
| C147292 | ALA1ALB | Apolipoprotein A1/Apolipoprotein B | A relative measurement (ratio or percentage) of the Apolipoprotein A1 to Apolipoprotein B in a biological specimen. |
| C158222 | ALAALB | Apolipoprotein A/Apolipoprotein B | A relative measurement (ratio) of the total apolipoprotein A to apolipoprotein B in a biological specimen. |
| C64431 | ALB | Albumin; Microalbumin | A measurement of the albumin protein in a biological specimen. |
| C147293 | ALBC | Albumin Clearance | A measurement of the albumin clearance in a biological specimen. |
| C74761 | ALBCREAT | Albumin/Creatinine; Microalbumin/Creatinine Ratio | A relative measurement (ratio) of the albumin to the creatinine in a biological specimen. |
| C150814 | ALBEXR | Albumin Excretion Rate | A measurement of the amount of albumin excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C158228 | ALBGALB | Glycated Albumin/Albumin; Glycosylated Albumin/Albumin | A relative measurement (ratio or percentage) of the glycated albumin to total albumin in a biological specimen. |
| C74894 | ALBGLOB | Albumin/Globulin | The ratio of albumin to globulin in a biological specimen. |
| C122092 | ALBGLYCA | Glycated Albumin | A measurement of the glycated albumin present in a biological specimen. |
| C154734 | ALBIDX | Albumin Index | A relative measurement (ratio) of the albumin in cerebrospinal fluid to albumin in serum or plasma in a biological specimen. |
| C103453 | ALBPROT | Albumin/Total Protein | A relative measurement (ratio or percentage) of the albumin to total protein in a biological specimen. |
| C154743 | ALDEPX | Aldrin Epoxidase | A measurement of the aldrin epoxidase in a biological specimen. |
| C74731 | ALDOLASE | Aldolase | A measurement of the aldolase enzyme in a biological specimen. |
| C74841 | ALDSTRN | Aldosterone | A measurement of the aldosterone hormone in a biological specimen. |
| C184566 | ALFNTNL | Alfentanil | A measurement of the alfentanil in a biological specimen. |
| C154762 | ALLOILE | Alloisoleucine | A measurement of the alloisoleucine in a biological specimen. |
| C184519 | ALOX5 | 5-Lipoxygenase; 5-LO; 5-LOX; ALOX5; Arachidonate 5-Lipoxygenase | A measurement of the arachidonate 5-lipoxygenase in a biological specimen. |
| C64432 | ALP | Alkaline Phosphatase | A measurement of the alkaline phosphatase in a biological specimen. |
| C147294 | ALPBALP | Alk Phos, Bone/Total Alk Phos; Alkaline Phosphatase, Bone/Total Alkaline Phosphatase | A relative measurement (ratio or percentage) of the bone specific alkaline phosphatase isoform to total alkaline phosphatase in a biological specimen. |
| C92287 | ALPBS | Bone Specific Alkaline Phosphatase | A measurement of the bone specific alkaline phosphatase isoform in a biological specimen. |
| C79438 | ALPCREAT | Alkaline Phosphatase/Creatinine | A relative measurement (ratio or percentage) of the alkaline phosphatase to creatinine in a biological specimen. |
| C165942 | ALPEXR | Alkaline Phosphatase Excretion Rate | A measurement of the amount of alkaline phosphatase being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C147295 | ALPIALP | Alk Phos, Intestinal/Total Alk Phos; Alkaline Phosphatase, Intestinal/Total Alkaline Phosphatase | A relative measurement (ratio or percentage) of the intestinal specific alkaline phosphatase isoform to total alkaline phosphatase in a biological specimen. |
| C119266 | ALPIS | Intestinal Specific Alkaline Phosphatase | A measurement of the intestinal specific alkaline phosphatase isoform in a biological specimen. |
| C139091 | ALPISOE | Alkaline Phosphatase Isoenzyme | A measurement of the alkaline phosphatase isoenzyme in a biological specimen. |
| C147296 | ALPLALP | Alk Phos, Liver/Total Alk Phos; Alkaline Phosphatase, Liver/Total Alkaline Phosphatase | A relative measurement (ratio or percentage) of the liver specific alkaline phosphatase isoform to total alkaline phosphatase in a biological specimen. |
| C189497 | ALPLBALP | Alk Phos, Liver + Bone/Total Alk Phos | A relative measurement (ratio or percentage) of the liver and bone specific alkaline phosphatase isoforms to total alkaline phosphatase in a biological specimen. |
| C119267 | ALPLS | Liver Specific Alkaline Phosphatase | A measurement of the liver specific alkaline phosphatase isoform in a biological specimen. |
| C184508 | ALPPALP | Alk Phos, Placental/Total Alk Phos; Alkaline Phosphatase, Placental/Total Alkaline Phosphatase | A relative measurement (ratio or percentage) of the placental specific alkaline phosphatase isoform to total alkaline phosphatase in a biological specimen. |
| C184509 | ALPPS | Placental Specific Alkaline Phosphatase | A measurement of the placental specific alkaline phosphatase isoform in a biological specimen. |
| C75370 | ALPRZLM | Alprazolam | A measurement of the alprazolam present in a biological specimen. |
| C163419 | ALS | Acid Labile Subunit; ALS; IGFALS; Insulin Like Growth Factor Binding Protein Acid Labile Subunit | A measurement of the acid labile subunit in a biological specimen. |
| C64433 | ALT | Alanine Aminotransferase; SGPT | A measurement of the alanine aminotransferase in a biological specimen. |
| C106498 | ALTAST | ALT/AST | A relative measurement (ratio or percentage) of the alanine aminotransferase (ALT) to aspartate aminotransferase (AST) present in a sample. |
| C103349 | ALTCPHRL | Alpha Tocopherol | A measurement of the alpha tocopherol in a biological specimen. |
| C111127 | ALUMINUM | Al; Aluminum | A measurement of aluminum in a biological specimen. |
| C184539 | AM2201 | AM-2201; AM2201 | A measurement of the synthetic cannabinoid AM-2201 in a biological specimen. |
| C184538 | AM694N5H | AM694 N-5-hydroxypentyl | A measurement of the synthetic cannabinoid metabolite AM694 N-5-hydroxypentyl in a biological specimen. |
| C81975 | AMA | Antimitochondrial Antibodies; Mitochondrial Antibody | A measurement of the antimitochondrial antibodies in a biological specimen. |
| C147297 | AMABARAB | ACH Receptor Modulation Antibody/ACH Receptor Antibody; ACH Receptor Modulatn Ab/ACH Receptor Ab | A relative measurement (ratio or percentage) of the acetylcholine receptor modulation antibody to the total acetylcholine receptor antibodies in a biological specimen. |
| C132364 | AMACR | Alpha-Methylacyl Coenzyme A Racemase | A measurement of the alpha-methylacyl coenzyme A racemase in a biological specimen. |
| C75363 | AMBRBTL | Amobarbital | A measurement of the amobarbital present in a biological specimen. |
| C132365 | AMCRMRNA | AMACR mRNA | A measurement of the alpha-methylacyl coenzyme A racemase mRNA in a biological specimen. |
| C120625 | AMH | Anti-Mullerian Hormone | A measurement of the anti-Mullerian hormone in a biological specimen. |
| C186023 | AMITRPTL | Amitriptyline | A measurement of the amitriptyline in a biological specimen. |
| C74799 | AMMONIA | Ammonia; NH3 | A measurement of the ammonia in a biological specimen. |
| C186024 | AMNM | Ammonium; Ammonium Ion; NH4+ | A measurement of the ammonium ion (NH4+) in a biological specimen. |
| C186025 | AMNMCRT | Ammonium/Creatinine | A relative measurement (ratio) of ammonium to creatinine in a biological specimen. |
| C81183 | AMNOACID | AA; Amino Acids | A measurement of the total amino acids in a biological specimen. |
| C74666 | AMORPHSD | Amorphous Debris; Amorphous Sediment | A measurement of the amorphous sediment present in a biological specimen. |
| C75347 | AMPEA | Alpha-Methylphenethylamine; Amphetamine | A measurement of the alpha-methylphenethylamine in a biological specimen. |
| C74687 | AMPHET | Amphetamine | A measurement of any amphetamine class drug present in a biological specimen. |
| C102262 | AMPHETD | d-amphetamine; Dextroamphetamine | A measurement of the dextroamphetamine in a biological specimen. |
| C64434 | AMYLASE | Amylase | A measurement of the total enzyme amylase in a biological specimen. |
| C111243 | AMYLASEM | Macroamylase | A measurement of macroamylase in a biological specimen. |
| C98767 | AMYLASEP | Amylase, Pancreatic; Pancreatic Amylase Isoenzyme | A measurement of the pancreatic enzyme amylase in a biological specimen. |
| C98780 | AMYLASES | Amylase, Salivary; Salivary Amylase Isoenzyme | A measurement of the salivary enzyme amylase in a biological specimen. |
| C103352 | AMYLB38 | Amyloid Beta 1-38; Amyloid Beta 38; Amyloid Beta 38 Protein | A measurement of amyloid beta protein which is composed of peptides 1 to 38 in a biological specimen. |
| C103353 | AMYLB40 | Amyloid Beta 1-40; Amyloid Beta 40; Amyloid Beta 40 Protein | A measurement of amyloid beta protein which is composed of peptides 1 to 40 in a biological specimen. |
| C184518 | AMYLB41 | Amyloid Beta 1-41; Amyloid Beta 41; Amyloid Beta 41 Protein | A measurement of amyloid beta protein which is composed of peptides 1 to 41 in a biological specimen. |
| C84809 | AMYLB42 | Amyloid Beta 1-42; Amyloid Beta 42; Amyloid Beta 42 Protein | A measurement of amyloid beta protein which is composed of peptides 1 to 42 in a biological specimen. |
| C125940 | AMYLOIDA | Amyloid A | A measurement of the total amyloid A in a biological specimen. |
| C81999 | AMYLOIDB | Amyloid, Beta; Beta Amyloid | A measurement of the total amyloid beta in a biological specimen. |
| C81998 | AMYLOIDP | Amyloid P; Amyloid P Component; SAP; Serum Amyloid P Component | A measurement of the total amyloid P in a biological specimen. |
| C74916 | ANA | Antinuclear Antibodies | A measurement of the total antinuclear antibodies (antibodies that attack the body's own tissue) in a biological specimen. |
| C176313 | ANAB | Anti-Neutrophil Antibody | A measurement of the total anti-neutrophil antibody in a biological specimen. |
| C147298 | ANABASN | Anabasine | A measurement of the anabasine in a biological specimen. |
| C147299 | ANAG | Alpha-N-acetylglucosaminidase | A measurement of the alpha-N-acetylglucosaminidase in a biological specimen. |
| C122093 | ANAIGGAB | Antinuclear IgG Antibody | A measurement of the antinuclear IgG antibody in a biological specimen. |
| C120626 | ANCAB | Anti-Neutrophil Cytoplasmic Antibody | A measurement of the anti-neutrophil cytoplasmic antibody in a biological specimen. |
| C147300 | ANCATYAB | Anti-Neutrophil Cytoplasmic Antibody, Atypical; Neutrophil Cytoplasmic Ab, Atypical | A measurement of the atypical (cytoplasmic staining usually uniform and no interlobular accentuation) neutrophil cytoplasmic antibodies in a biological specimen. |
| C147301 | ANCCLSAB | Anti-Neutrophil Cytoplasmic Antibody, Classic; Neutrophil Cytoplasmic Ab, Classic | A measurement of the classic (cytoplasmic granular fluorescence with central interlobular accentuation) neutrophil cytoplasmic antibodies in a biological specimen. |
| C163420 | ANCIGAB | Anti-Neutrophil Cytoplasmic IgG Antibody | A measurement of the anti-neutrophil cytoplasmic IgG antibody in a biological specimen. |
| C147302 | ANCPNCAB | Anti-Neutrophil Cytoplasmic Antibody, Perinuclear; Neutrophil Cytoplasmic Ab, Perinuclear | A measurement of the perinuclear (perinuclear staining without nuclear extension) neutrophil cytoplasmic antibodies in a biological specimen. |
| C74842 | ANDSTNDL | Androstenediol | A measurement of the androstenediol metabolite in a biological specimen. |
| C74843 | ANDSTNDN | 4-Androstenedione; Androstenedione | A measurement of the androstenedione hormone in a biological specimen. |
| C186026 | ANDSTRN | Androsterone | A measurement of the androsterone in a biological specimen. |
| C91372 | ANGLBIND | Antiglobulin Test, Indirect; Indirect Coombs Test | A test that uses Coombs' reagent to detect the presence of anti-erythrocyte antibodies in a biological specimen. |
| C81974 | ANGLOBDR | Antiglobulin Test Polyspecific, Direct; Antiglobulin Test, Direct; Direct Coombs Test | A measurement of the antibody or complement-coated erythrocytes in a biological specimen in vivo. |
| C111128 | ANGPT1 | Angiopoietin 1 | A measurement of angiopoietin 1 in a biological specimen. |
| C163421 | ANGPT2 | ANG2; Angiopoietin 2 | A measurement of angiopoietin 2 in a biological specimen. |
| C74844 | ANGTNS1 | Angiotensin I | A measurement of the angiotensin I hormone in a biological specimen. |
| C74845 | ANGTNS2 | Angiotensin II | A measurement of the angiotensin II hormone in a biological specimen. |
| C74846 | ANGTNSGN | Angiotensin Precursor; Angiotensinogen | A measurement of the angiotensinogen hormone in a biological specimen. |
| C74685 | ANIONG | Anion Gap | A computed estimate of the unmeasured anions (those other than the chloride and bicarbonate anions) in a biological specimen. |
| C147303 | ANIONG3 | Anion Gap 3 | A computed estimate of the unmeasured anions (computed as sodium minus the chloride and bicarbonate) in a biological specimen. |
| C147304 | ANIONG4 | Anion Gap 4 | A computed estimate of the unmeasured anions (computed as the difference between the sum of serum sodium + serum potassium and the sum of the serum bicarbonate+ chloride) in a biological specimen. |
| C74797 | ANISO | Anisocytes; Anisocytosis | A measurement of the variability in the size of the red blood cells in a whole blood specimen. |
| C161354 | ANISOCHR | Anisochromia | A measurement of the color variation of erythrocytes in a biological specimen. |
| C184568 | ANLRDN | Anileridine | A measurement of the anileridine in a biological specimen. |
| C74886 | ANP | Atrial Natriuretic Peptide; Atriopeptin | A measurement of the atrial natriuretic peptide in a biological specimen. |
| C172523 | ANPPROMR | Mid-Reg Pro-Atrial Natriuretic Peptide; Mid-Regional Pro-Atrial Natriuretic Peptide; MR-proANP; MRproANP | A measurement of the mid-regional pro-atrial natriuretic peptide in a biological specimen. |
| C139088 | ANPPRONT | N-terminal pro-Atrial Natriuretic Peptide; N-Terminal ProA-type Natriuretic Peptide; NT proANP II | A measurement of the N-terminal proA-type natriuretic peptide in a biological specimen. |
| C81958 | ANTHRMA | Antithrombin Activity; Antithrombin III Activity | A measurement of the antithrombin activity in a biological specimen. |
| C81977 | ANTHRMAG | Antithrombin; Antithrombin Antigen; Antithrombin III; Antithrombin III Antigen | A measurement of the antithrombin antigen in a biological specimen. |
| C74691 | ANTIDPRS | Antidepressants | A measurement of any antidepressant class drug present in a biological specimen. |
| C120627 | ANUAB | Anti-Nucleosome Antibody | A measurement of the anti-nucleosome antibody in a biological specimen. |
| C172525 | APAPCYS | Acetaminophen Protein Adduct; Acetaminophen-Cysteine Adduct; APAP-CYS; APAP-Protein | A measurement of the acetaminophen-cysteine adducts in a biological specimen. |
| C102258 | APLAB | Antiphospholipid Antibodies | A measurement of the total antiphospholipid antibodies in a biological specimen. |
| C161372 | APLASCPD | APTT-LA Screen to Confirm Percent Difference; PTT-LA Screen to Confirm Pct Difference | A measurement to confirm the presence of Lupus anticoagulants, calculated as [(Screen aPTT - Confirm aPTT)/Screen aPTT]x100. |
| C124335 | APLIGGAB | Anti-Phospholipid IgG Antibody | A measurement of the antiphospholipid IgG antibody in a biological specimen. |
| C124336 | APLIGMAB | Anti-Phospholipid IgM Antibody | A measurement of the antiphospholipid IgM antibody in a biological specimen. |
| C103351 | APLSMA2 | Alpha-2 Antiplasmin; Alpha-2 Plasmin Inhibitor | A measurement of the alpha-2 antiplasmin in a biological specimen. |
| C122094 | APLSMA2A | Alpha-2 Antiplasmin Activity | A measurement of the alpha-2 antiplasmin activity in a biological specimen. |
| C124337 | APOA | Apolipoprotein A | A measurement of the total apolipoprotein A in a biological specimen. |
| C74733 | APOA1 | Apolipoprotein A1 | A measurement of the apolipoprotein A1 in a biological specimen. |
| C82000 | APOA2 | Apolipoprotein AII | A measurement of the apolipoprotein AII in a biological specimen. |
| C103354 | APOA4 | Apolipoprotein A4 | A measurement of the apolipoprotein A4 in a biological specimen. |
| C103355 | APOA5 | Apolipoprotein A5 | A measurement of the apolipoprotein A5 in a biological specimen. |
| C74734 | APOB | Apolipoprotein B | A measurement of the total apolipoprotein B in a biological specimen. |
| C120628 | APOB100 | Apolipoprotein B100 | A measurement of the apolipoprotein B100 in a biological specimen. |
| C120629 | APOB48 | Apolipoprotein B48 | A measurement of the apolipoprotein B48 in a biological specimen. |
| C103356 | APOBAPA1 | Apolipoprotein B/Apolipoprotein A1 | A relative measurement (ratio or percentage) of the Apolipoprotein B to Apolipoprotein A1 in a biological specimen. |
| C120630 | APOC1 | Apolipoprotein CI | A measurement of the apolipoprotein CI in a biological specimen. |
| C100427 | APOC2 | Apolipoprotein C2; Apolipoprotein CII | A measurement of the apolipoprotein C2 in a biological specimen. |
| C82001 | APOC3 | Apolipoprotein CIII | A measurement of the apolipoprotein CIII in a biological specimen. |
| C82002 | APOE | Apolipoprotein E | A measurement of the apolipoprotein E in a biological specimen. |
| C92293 | APOE4 | Apolipoprotein E4 | A measurement of the apolipoprotein E4 in a biological specimen. |
| C82003 | APOH | Apolipoprotein H | A measurement of the apolipoprotein H in a biological specimen. |
| C100428 | APOJ | Apolipoprotein J; Clusterin | A measurement of the apolipoprotein J in a biological specimen. |
| C111130 | APOJCRT | Apolipoprotein J/Creatinine; Clusterin/Creatinine | A relative measurement (ratio or percentage) of the apolipoprotein J to creatinine in a biological specimen. |
| C119268 | APPA | Amyloid Alpha Precursor Protein | A measurement of the amyloid alpha precursor protein present in a biological specimen. |
| C105438 | APPB | Amyloid Beta Precursor; Amyloid Beta Precursor Protein; Amyloid Precursor Beta; Amyloid Precursor Protein | A measurement of the amyloid beta precursor protein present in a biological specimen. |
| C179695 | APPEAR | Specimen Appearance | The outward or visible aspect of a specimen. |
| C119269 | APPT | Total Amyloid Precursor Protein | A measurement of the total amyloid precursor protein present in a biological specimen. |
| C184578 | APRBRBTL | Aprobarbital | A measurement of the aprobarbital in a biological specimen. |
| C156512 | APRI | APRI Score; AST to Platelet Ratio Index | A calculation that indicates the likely presence of liver cirrhosis and fibrosis, measured as the relative measurement of aspartate aminotransferase (AST) to AST upper limit of normal, divided by the platelet count, and multiplied by 100. |
| C111123 | APRIL | A Proliferation-Inducing Ligand; CD256; TNFSF13; Tumor Necrosis Factor Ligand Superfamily Member 13 | A measurement of the a proliferation-inducing ligand in a biological specimen. |
| C100471 | APROTCRS | Activated Protein C Resistance; Factor V Leiden Screen | A measurement of the resistance in the anticoagulation response to activated protein C in a biological specimen. |
| C38462 | APTT | Activated Partial Thromboplastin Time | A measurement of the length of time that it takes for clotting to occur when activating reagents are added to a biological specimen. The test is partial due to the absence of tissue factor (Factor III) from the reaction mixture. |
| C161369 | APTTLAAC | APTT-LA Actual/Control; Lupus Anticoagulant Sensitive APTT Actual/Control | A relative measurement (ratio or percentage) of the Lupus anticoagulant sensitive APTT in a subject's specimen when compared to a control specimen. |
| C102277 | APTTLAS | APTT-LA; Lupus Anticoagulant Sensitive APTT | A measurement of the length of time that it takes for clotting to occur when a lupus sensitive reagent is added to a plasma specimen. |
| C98862 | APTTSTND | Activated Partial Thromboplastin Time/Standard Thromboplastin Time; Activated PTT/Standard; Activated PTT/Standard PTT | A relative measurement (ratio or percentage) of the subject's activated partial thromboplastin time to a standard or control partial thromboplastin time. |
| C102259 | ARA | Arachidonic Acid | A measurement of the arachidonic acid present in a biological specimen. |
| C122095 | ARG | Arginine | A measurement of the arginine in a biological specimen. |
| C154763 | ARGSAC | Argininosuccinate; Argininosuccinic Acid | A measurement of the argininosuccinic acid in a biological specimen. |
| C177974 | ARPIPZL | Aripiprazole | A measurement of the aripiprazole in a biological specimen. |
| C124338 | ARR | Aldosterone/Renin Activity | A relative measurement (ratio) of the aldosterone to renin activity in a biological specimen. |
| C147305 | ARSENIC | Arsenic; As | A measurement of the arsenic in a biological specimen. |
| C177985 | ASENAPN | Asenapine | A measurement of the asenapine in a biological specimen. |
| C163422 | ASMACT | Alpha-Actin 2; Alpha-SMA; Alpha-Smooth Muscle Actin | A measurement of the alpha-smooth muscle actin in a biological specimen. |
| C122096 | ASN | Asparagine | A measurement of the asparagine in a biological specimen. |
| C122097 | ASP | Aspartate; Aspartic Acid | A measurement of the aspartic acid in a biological specimen. |
| C92269 | ASSDNA | Anti-Single Stranded DNA IgG | A measurement of the anti-single stranded DNA IgG antibody in a biological specimen. |
| C64467 | AST | Aspartate Aminotransferase; SGOT | A measurement of the aspartate aminotransferase in a biological specimen. |
| C81978 | ASTAG | Aspartate Aminotransferase Antigen; SGOT Antigen | A measurement of the aspartate aminotransferase antigen in a biological specimen. |
| C176297 | ASTALT | AST/ALT | A relative measurement (ratio or percentage) of the aspartate aminotransferase (AST) to alanine aminotransferase (ALT) present in a sample. |
| C158225 | ASTCK | Aspartate Aminotransferase/CPK; Aspartate Aminotransferase/Creatine Kinase; AST/Creatine Kinase | A relative measurement (ratio) of the aspartate aminotransferase to creatine kinase in a biological specimen. |
| C117830 | ASTCREAT | Aspartate Aminotransferase/Creatinine | A relative measurement (ratio or percentage) of the aspartate aminotransferase to creatinine in a biological specimen. |
| C186027 | ASTDLG3A | 3-Alpha-Androstanediol Glucuronide | A measurement of the 3-alpha-androstanediol glucuronide in a biological specimen. |
| C142272 | ASYNP | Alpha Synuclein Protein | A measurement of the alpha synuclein protein in a biological specimen. |
| C147306 | ATHMBAAC | Antithrombin Activity Actual/Antithrombin Activity Control; Antithrombin Activity Actual/Control; Antithrombin Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of antithrombin in a subject's specimen when compared to the same activity in a control specimen. |
| C170592 | ATHMBAC | Antithrombin Actual/Control; Antithrombin Actual/Normal | A relative measurement (ratio or percentage) of the Antithrombin in a subject's specimen when compared to a control specimen. |
| C154726 | ATHPIDX | AIP; Atherogenic Index; Atherogenic Index of Plasma | A measurement of the base 10 logarithm of the ratio of molar concentration of plasma triglyceride to high density lipoprotein cholesterol in a biological specimen. |
| C147307 | ATP | Adenosine Triphosphate | A measurement of the adenosine triphosphate in a biological specimen. |
| C103350 | ATPVITE | Alpha Tocopherol/Vitamin E | A relative measurement (ratio or percentage) of alpha-tocopherol to the total vitamin E in a biological specimen. |
| C74657 | AUERRODS | Auer Rods | A measurement of the Auer rods (elongated needle structures that are found in the cytoplasm of leukemic blasts and are formed by clumps of azurophilic granular material) in a biological specimen. |
| C165943 | AXL | ARK; AXL Receptor Tyrosine Kinase; JTK11; Tyro7; UFO | A measurement of the AXL receptor tyrosine kinase in a biological specimen. |
| C116185 | AZURGRAN | Azurophilic Granulation; Azurophilic Granules | An observation of azurophilic granules in a biological specimen. |
| C127607 | B1BGLP | Beta-1B Glycoprotein; Hemopexin; HPX | A measurement of the beta-1B glycoprotein in a biological specimen. |
| C147308 | B2G1GAAB | Beta-2 Glycoprotein 1 IgA Antibody | A measurement of the beta-2 glycoprotein 1 IgG antibodies in a biological specimen. |
| C103358 | B2G1GGAB | Beta-2 Glycoprotein 1 IgG Antibody | A measurement of the Beta-2 glycoprotein 1 IgG antibodies in a biological specimen. |
| C103359 | B2G1GMAB | Beta-2 Glycoprotein 1 IgM Antibody | A measurement of the Beta-2 glycoprotein 1 IgM antibodies in a biological specimen. |
| C81979 | B2GLYAB | Beta-2 Glycoprotein Antibody | A measurement of the beta-2 glycoprotein antibody in a biological specimen. |
| C127608 | B2MCREAT | Beta-2 Microglobulin/Creatinine | A relative measurement (ratio) of the beta-2 microglobulin to creatinine in a biological specimen. |
| C81980 | B2MICG | Beta-2 Microglobulin | A measurement of the beta-2 microglobulin in a biological specimen. |
| C64469 | BACT | Bacteria | A measurement of the bacteria in a biological specimen. |
| C111135 | BAFF | B-Cell Activating Factor | A measurement of the B-cell activating factor in a biological specimen. |
| C154764 | BALA | Beta Alanine | A measurement of the beta alanine in a biological specimen. |
| C154765 | BAMBTAC | BABA; Beta-aminobutyrate; Beta-Aminobutyric Acid | A measurement of the beta-aminobutyric acid in a biological specimen. |
| C74688 | BARB | Barbiturates | A measurement of any barbiturate class drug present in a biological specimen. |
| C147309 | BASEDEF | Base Deficit | A measurement of the amount of alkali required to return a biological specimen to a normal pH under standard conditions. |
| C119270 | BASEEXCS | Actual Base Excess; Base Excess | A calculated measurement of the amount of acid required to return blood to a normal pH under standard conditions. |
| C64470 | BASO | Basophils | A measurement of the basophils in a biological specimen. |
| C130154 | BASOB | Basophils Band Form | A measurement of the banded basophils in a biological specimen. |
| C130155 | BASOBLE | Basophils Band Form/Leukocytes | A relative measurement (ratio or percentage) of the banded basophils to leukocytes in a biological specimen. |
| C98865 | BASOCE | Basophils/Total Cells | A relative measurement (ratio or percentage) of the basophils to total cells in a biological specimen (for example a bone marrow specimen). |
| C96670 | BASOIM | Immature Basophils | A measurement of the immature basophils in a biological specimen. |
| C96671 | BASOIMLE | Immature Basophils/Leukocytes | A relative measurement (ratio or percentage) of immature basophils to total leukocytes in a biological specimen. |
| C64471 | BASOLE | Basophils/Leukocytes | A relative measurement (ratio or percentage) of the basophils to leukocytes in a biological specimen. |
| C135399 | BASOMM | Basophilic Metamyelocytes | A measurement of the basophilic metamyelocytes in a biological specimen. |
| C135400 | BASOMYL | Basophilic Myelocytes | A measurement of the basophilic myelocytes in a biological specimen. |
| C181448 | BASOMYLY | Basophilic Myelocytes/Lymphocytes | A relative measurement (ratio or percentage) of the basophilic myelocytes to lymphocytes in a biological specimen (for example a bone marrow specimen). |
| C135401 | BASOSG | Basophils, Segmented | A measurement of the segmented basophils in a biological specimen. |
| C123455 | BCEFNCTN | Beta-cell Function | A measurement of the beta cell function (insulin production and secretion) in a biological specimen. |
| C170577 | BCMAS | Soluble B Cell Maturation Antigen; Soluble BCM; Soluble BCMA; Soluble CD269; Soluble TNF Receptor Superfamily Member 17; Soluble TNFRSF13A | A measurement of the soluble B cell maturation antigen in a biological specimen. |
| C122102 | BD2 | Beta-defensin 2 | A measurement of the beta-defensin 2 in a biological specimen. |
| C82004 | BDNF | Brain-Derived Neurotrophic Factor | A measurement of the brain-derived neurotrophic factor in a biological specimen. |
| C100472 | BETACRTN | b-Carotene; Beta Carotene; Beta Carotin | A measurement of the beta carotene in a biological specimen. |
| C172517 | BETAINES | Betaines | A measurement of the betaine class compounds in a biological specimen. |
| C184531 | BFTNN | Bufotenine | A measurement of the bufotenine in a biological specimen. |
| C172497 | BGTCPHRL | Beta and Gamma Tocopherol; Beta+Gamma Tocopherol | A measurement of the beta and gamma tocopherol in a biological specimen. |
| C186028 | BHBACTAC | Beta-Hydroxybutyrate/Acetoacetate | A relative measurement (ratio) of the beta-hydroxybutyrate to acetoacetate in a biological specimen. |
| C189520 | BHBEXR | 3-Hydroxybutyrate Excretion Rate; B-Hydroxybutyrate Excretion Rate; Beta-Hydroxybutyrate Excretion Rate; BHB Excretion Rate | A measurement of the amount of beta-Hydroxybutyrate being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C96568 | BHYXBTR | 3-Hydroxybutyrate; B-Hydroxybutyrate; Beta-Hydroxybutyrate; Beta-Hydroxybutyric Acid; BHB | A measurement of the total Beta-hydroxybutyrate in a biological specimen. |
| C74667 | BICARB | Bicarbonate; HCO3 | A measurement of the bicarbonate in a biological specimen. |
| C64481 | BILDIR | Direct Bilirubin | A measurement of the conjugated or water-soluble bilirubin in a biological specimen. |
| C158226 | BILDIRBI | Direct Bilirubin/Bilirubin | A relative measurement (ratio or percentage) of the direct bilirubin to total bilirubin in a biological specimen. |
| C74800 | BILEAC | Bile Acid; Bile Acids; Bile Salt; Bile Salts | A measurement of the total bile acids in a biological specimen. |
| C38037 | BILI | Bilirubin; Total Bilirubin | A measurement of the total bilirubin in a biological specimen. |
| C64483 | BILIND | Indirect Bilirubin | A measurement of the unconjugated or non-water-soluble bilirubin in a biological specimen. |
| C74700 | BITECE | Bite Cells | A measurement of the bite cells (erythrocytes with the appearance of a bite having been removed, due to oxidative hemolysis) in a biological specimen. |
| C111136 | BJPROT | Bence-Jones Protein | A measurement of the total Bence-Jones protein in a biological specimen. |
| C74605 | BLAST | Blasts | A measurement of the blast cells in a biological specimen. |
| C150836 | BLASTCE | Blasts/Total Cells | A relative measurement (ratio or percentage) of the blasts to total cells in a biological specimen. |
| C147311 | BLASTERY | Basophilic Erythroblast | A measurement of the basophilic erythroblasts in a biological specimen taken from a non-human organism. |
| C103407 | BLASTIMM | Immunoblastic Lymphocytes; Immunoblasts | A measurement of the immunoblasts in a biological specimen. |
| C64487 | BLASTLE | Blasts/Leukocytes | A relative measurement (ratio or percentage) of the blasts to leukocytes in a biological specimen. |
| C74630 | BLASTLM | Leukemic Blasts | A measurement of the leukemic blasts (lymphoblasts that remain in an immature state even when outside the bone marrow) in a biological specimen. |
| C147312 | BLASTNCE | Blasts/Nucleated Cells | A relative measurement (ratio or percentage) of the blasts to the total nucleated cells in a biological specimen. |
| C100446 | BLASTRUB | Proerythroblast; Pronormoblast; Rubriblast | A measurement of the rubriblasts in a biological specimen. |
| C89775 | BLEEDT | Bleeding Time; Clotting Time Homeostasis | A measurement of the time from the start to cessation of an induced bleed. |
| C127609 | BLISTCE | Blister Cell | A measurement of the blister cells in a biological specimen. |
| C106535 | BLSTIMLY | Immunoblasts/Lymphocytes; Lymphocytes, Immunoblastic/Lymphocytes | A relative measurement (ratio or percentage) of immunoblasts to all lymphocytes present in a sample. |
| C74641 | BLSTLMLY | Leukemic Blasts/Lymphocytes | A relative measurement (ratio or percentage) of the leukemic blasts (immature lymphoblasts) to mature lymphocytes in a biological specimen. |
| C102278 | BLSTLY | Lymphoblasts | A measurement of the lymphoblasts (immature cells that differentiate to form lymphocytes) in a biological specimen. |
| C105444 | BLSTLYLE | Lymphoblasts/Leukocytes | A relative measurement (ratio or percentage) of the lymphoblasts to leukocytes in a biological specimen. |
| C189503 | BLSTLYLY | Lymphoblasts/Lymphocytes | A relative measurement (ratio or percentage) of the lymphoblasts to lymphocytes in a biological specimen. |
| C98761 | BLSTMBCE | Myeloblasts/Total Cells | A relative measurement (ratio or percentage) of the myeloblasts to total cells in a biological specimen (for example a bone marrow specimen). |
| C98752 | BLSTMGK | Megakaryoblasts | A measurement of the megakaryoblasts in a biological specimen. |
| C98753 | BLSTMKCE | Megakaryoblasts/Total Cells | A relative measurement (ratio or percentage) of the megakaryoblasts to total cells in a biological specimen (for example a bone marrow specimen). |
| C187813 | BLSTMKLE | Megakaryoblasts/Leukocytes | A relative measurement (ratio or percentage) of megakaryoblasts to total leukocytes in a biological specimen. |
| C189501 | BLSTNM | Normoblasts | A measurement of the normoblasts in a biological specimen. |
| C98764 | BLSTNMCE | Normoblasts/Total Cells | A relative measurement (ratio or percentage) of the normoblasts to total cells in a biological specimen (for example a bone marrow specimen). |
| C98870 | BLSTRBCE | Proerythroblast/Total Cells; Pronormoblasts/Total Cells; Rubriblast/Total Cells | A relative measurement (ratio or percentage) of the rubriblasts to total cells in a biological specimen (for example a bone marrow specimen). |
| C100419 | BLSTRSID | Ringed Sideroblasts | A measurement of the ringed sideroblasts (abnormal nucleated erythroblasts with a large number of iron deposits in the perinuclear mitochondria, forming a ring around the nucleus) in a biological specimen. |
| C100418 | BLSTSID | Sideroblast | A measurement of the sideroblasts (nucleated erythroblasts with iron granules in the cytoplasm) in a biological specimen. |
| C174314 | BLYCE | B-Cell Lymphocytes; B-Cells; B-Lymphocytes | A measurement of the B-lymphocytes in a biological specimen. |
| C174317 | BLYCECE | B-Lymphocytes/Total Cells | A relative measurement (ratio or percentage) of the B-lymphocytes to total cells in a biological specimen. |
| C174316 | BLYCELE | B-Lymphocytes/Leukocytes | A relative measurement (ratio or percentage) of the B-lymphocytes to leukocytes in a biological specimen. |
| C174315 | BLYCELY | B-Lymphocytes/Lymphocytes | A relative measurement (ratio or percentage) of the B-lymphocytes to total lymphocytes in a biological specimen. |
| C128951 | BLYMXM | B-lymphocyte Crossmatch | A measurement to determine human leukocyte antigens (HLA) histocompatibility between the recipient and the donor by examining the presence or absence of the recipient's anti-HLA antibody reactivity towards HLA antigens expressed on the donor B-lymphocytes. |
| C74735 | BNP | B-Type Natriuretic Peptide; Brain Natriuretic Peptide | A measurement of the brain (B-type) natriuretic peptide in a biological specimen. |
| C82032 | BNPPRO | Pro-Brain Natriuretic Peptide; ProB-type Natriuretic Peptide; proBNP | A measurement of the proB-type natriuretic peptide in a biological specimen. |
| C96610 | BNPPRONT | N-terminal pro-Brain Natriuretic Peptide; N-Terminal ProB-type Natriuretic Peptide; NT proBNP II | A measurement of the N-terminal proB-type natriuretic peptide in a biological specimen. |
| C74692 | BNZDZPN | Benzodiazepine | A measurement of any benzodiazepine class drug present in a biological specimen. |
| C75350 | BNZLCGN | Benzoylecgonine | A measurement of the benzoylecgonine in a biological specimen. |
| C75380 | BOLDNON | Boldenone | A measurement of the boldenone in a biological specimen. |
| C184579 | BOLSTRN | Bolasterone | A measurement of the bolasterone in a biological specimen. |
| C120631 | BPIAB | Bactericidal/Permeability-Inc Protein Ab; BPI Auto-antibody | A measurement of the bactericidal/permeability-increasing protein antibody in a biological specimen. |
| C184608 | BRBTL | Barbital | A measurement of the barbital in a biological specimen. |
| C184609 | BRMZPM | Bromazepam | A measurement of the bromazepam in a biological specimen. |
| C184639 | BRVRCTM | Brivaracetam | A measurement of the brivaracetam in a biological specimen. |
| C177973 | BRXPIPZL | Brexpiprazole | A measurement of the brexpiprazole in a biological specimen. |
| C74634 | BTECERBC | Bite Cells/Erythrocytes | A relative measurement (ratio or percentage) of bite cells (erythrocytes with the appearance of a bite having been removed, due to oxidative hemolysis) to all erythrocytes in a biological specimen. |
| C165772 | BTK | Agammaglobulinemia Tyrosine Kinase; ATK; B-cell Progenitor Kinase; Bruton Tyrosine Kinase; Bruton's Tyrosine Kinase; Tyrosine-protein kinase BTK | A measurement of the Bruton's tyrosine kinase in a biological specimen. |
| C165944 | BTKFR | Bruton's Tyrosine Kinase, Free | A measurement of the free Bruton's tyrosine kinase in a biological specimen. |
| C75364 | BTLBARTL | Butabarbital | A measurement of the butabarbital in a biological specimen. |
| C75365 | BTLBTL | Butalbital | A measurement of the butalbital present in a biological specimen. |
| C184610 | BTRPHNL | Butorphanol | A measurement of the butorphanol in a biological specimen. |
| C111142 | BUCHE | Acylcholine Acylhydrolase; Butyrylcholinesterase; Non-neuronal Cholinesterase; Plasma Cholinesterase; Pseudocholinesterase | A measurement of the total butyrylcholinesterase in a biological specimen. |
| C75352 | BUPREN | Buprenorphine | A measurement of the buprenorphine drug present in a biological specimen. |
| C74701 | BURRCE | Burr Cells; Echinocytes | A measurement of the Burr cells (erythrocytes characterized by the presence of small, blunt projections evenly distributed across the cell surface) in a biological specimen. |
| C184532 | BUTYLN | Butylone | A measurement of the butylone in a biological specimen. |
| C184554 | BZP | 1-benzylpiperazine; Benzylpiperazine; N-benzylpiperazine | A measurement of the benzylpiperazine in a biological specimen. |
| C130068 | C130068 | Bermuda Grass Pollen IgE | A measurement of the Cynodon dactylon pollen antigen IgE antibody in a biological specimen. |
| C130069 | C130069 | Bermuda Grass Pollen IgA | A measurement of the Cynodon dactylon pollen antigen IgA antibody in a biological specimen. |
| C130070 | C130070 | Bermuda Grass Pollen IgG | A measurement of the Cynodon dactylon pollen antigen IgG antibody in a biological specimen. |
| C130071 | C130071 | Bermuda Grass Pollen IgG4 | A measurement of the Cynodon dactylon pollen antigen IgG4 antibody in a biological specimen. |
| C130072 | C130072 | Birch Pollen IgE | A measurement of the Betula pollen antigen IgE antibody in a biological specimen. |
| C130073 | C130073 | Birch Pollen IgA | A measurement of the Betula pollen antigen IgA antibody in a biological specimen. |
| C130074 | C130074 | Birch Pollen IgG | A measurement of the Betula pollen antigen IgG antibody in a biological specimen. |
| C130075 | C130075 | Birch Pollen IgG4 | A measurement of the Betula pollen antigen IgG4 antibody in a biological specimen. |
| C130076 | C130076 | Silver Birch Pollen IgE | A measurement of the Betula verrucosa pollen antigen IgE antibody in a biological specimen. |
| C130077 | C130077 | Silver Birch Pollen IgA | A measurement of the Betula verrucosa pollen antigen IgA antibody in a biological specimen. |
| C130078 | C130078 | Silver Birch Pollen IgG | A measurement of the Betula verrucosa pollen antigen IgG antibody in a biological specimen. |
| C130079 | C130079 | Silver Birch Pollen IgG4 | A measurement of the Betula verrucosa pollen antigen IgG4 antibody in a biological specimen. |
| C130080 | C130080 | Cocksfoot Grass Pollen IgE; Orchard Grass Pollen IgE | A measurement of the Dactylis glomerata pollen antigen IgE antibody in a biological specimen. |
| C130081 | C130081 | Cocksfoot Grass Pollen IgA; Orchard Grass Pollen IgA | A measurement of the Dactylis glomerata pollen antigen IgA antibody in a biological specimen. |
| C130082 | C130082 | Cocksfoot Grass Pollen IgG; Orchard Grass Pollen IgG | A measurement of the Dactylis glomerata pollen antigen IgG antibody in a biological specimen. |
| C130083 | C130083 | Cocksfoot Grass Pollen IgG4; Orchard Grass Pollen IgG4 | A measurement of the Dactylis glomerata pollen antigen IgG4 antibody in a biological specimen. |
| C130084 | C130084 | English Plantain Pollen IgE | A measurement of the Plantagio lanceolata pollen antigen IgE antibody in a biological specimen. |
| C130085 | C130085 | English Plantain Pollen IgA | A measurement of the Plantagio lanceolata pollen antigen IgA antibody in a biological specimen. |
| C130086 | C130086 | English Plantain Pollen IgG | A measurement of the Plantagio lanceolata pollen antigen IgG antibody in a biological specimen. |
| C130087 | C130087 | English Plantain Pollen IgG4 | A measurement of the Plantagio lanceolata pollen antigen IgG4 antibody in a biological specimen. |
| C130088 | C130088 | Timothy Grass Pollen IgE | A measurement of the Phleum pratense pollen antigen IgE antibody in a biological specimen. |
| C130089 | C130089 | Timothy Grass Pollen IgA | A measurement of the Phleum pratense pollen antigen IgA antibody in a biological specimen. |
| C130090 | C130090 | Timothy Grass Pollen IgG | A measurement of the Phleum pratense pollen antigen IgG antibody in a biological specimen. |
| C130091 | C130091 | Timothy Grass Pollen IgG4 | A measurement of the Phleum pratense pollen antigen IgG4 antibody in a biological specimen. |
| C130092 | C130092 | Western Ragweed Pollen IgE | A measurement of the Ambrosia psilostachya pollen antigen IgE antibody in a biological specimen. |
| C130093 | C130093 | Western Ragweed Pollen IgA | A measurement of the Ambrosia psilostachya pollen antigen IgA antibody in a biological specimen. |
| C130094 | C130094 | Western Ragweed Pollen IgG | A measurement of the Ambrosia psilostachya pollen antigen IgG antibody in a biological specimen. |
| C130095 | C130095 | Western Ragweed Pollen IgG4 | A measurement of the Ambrosia psilostachya pollen antigen IgG4 antibody in a biological specimen. |
| C130100 | C130100 | Mixed Antigen IgE Antibody | A measurement of the mixed antigen IgE antibody in a biological specimen. |
| C130101 | C130101 | Tree Mix Pollen Antigen IgE Antibody | A measurement of the tree mix pollen antigen IgE antibody in a biological specimen. |
| C130102 | C130102 | Tree Mix Pollen Antigen IgG Antibody | A measurement of the tree mix pollen antigen IgG antibody in a biological specimen. |
| C130103 | C130103 | Grass Mix Pollen Antigen IgE Antibody | A measurement of the grass mix pollen antigen IgE antibody in a biological specimen. |
| C130104 | C130104 | Grass Mix Pollen Antigen IgG Antibody | A measurement of the grass mix pollen antigen IgG antibody in a biological specimen. |
| C130105 | C130105 | Grass Mix Pollen Antigen IgA Antibody | A measurement of the grass mix pollen antigen IgA antibody in a biological specimen. |
| C130106 | C130106 | Weed Mix Pollen Antigen IgE Antibody | A measurement of the weed mix pollen antigen IgE antibody in a biological specimen. |
| C130107 | C130107 | Weed Mix Pollen Antigen IgG Antibody | A measurement of the weed mix pollen antigen IgG antibody in a biological specimen. |
| C130108 | C130108 | Weed Mix Pollen Antigen IgA Antibody | A measurement of the weed mix pollen antigen IgA antibody in a biological specimen. |
| C130109 | C130109 | Mold Mix Antigen IgE Antibody | A measurement of the mold mix antigen IgE antibody in a biological specimen. |
| C130110 | C130110 | Mold Mix Antigen IgG Antibody | A measurement of the mold mix antigen IgG antibody in a biological specimen. |
| C130111 | C130111 | Mold Mix Antigen IgA Antibody | A measurement of the mold mix antigen IgA antibody in a biological specimen. |
| C130112 | C130112 | Animal Mix Antigen IgE Antibody | A measurement of the animal mix antigen IgE antibody in a biological specimen. |
| C130113 | C130113 | Animal Mix Antigen IgG Antibody | A measurement of the animal mix antigen IgG antibody in a biological specimen. |
| C130114 | C130114 | Industrial Mix Antigen IgE Antibody | A measurement of the industrial mix antigen IgE antibody in a biological specimen. |
| C130115 | C130115 | Industrial Mix Antigen IgG Antibody | A measurement of the industrial mix antigen IgG antibody in a biological specimen. |
| C130116 | C130116 | Bee Mix Antigen IgE Antibody | A measurement of the bee mix antigen IgE antibody in a biological specimen. |
| C130117 | C130117 | Bee Mix Antigen IgG Antibody | A measurement of the bee mix antigen IgG antibody in a biological specimen. |
| C130118 | C130118 | Bee Mix Antigen IgG4 Antibody | A measurement of the bee mix antigen IgG4 antibody in a biological specimen. |
| C130119 | C130119 | Dairy Mix Antigen IgG Antibody | A measurement of the dairy mix antigen IgG antibody in a biological specimen. |
| C130120 | C130120 | Shellfish Mix Antigen IgE Antibody | A measurement of the shellfish mix antigen IgE antibody in a biological specimen. |
| C130121 | C130121 | Shellfish Mix Antigen IgG Antibody | A measurement of the shellfish mix antigen IgG antibody in a biological specimen. |
| C130122 | C130122 | Nut Mix Antigen IgE Antibody | A measurement of the nut mix antigen IgE antibody in a biological specimen. |
| C130123 | C130123 | Nut Mix Antigen IgG Antibody | A measurement of the nut mix antigen IgG antibody in a biological specimen. |
| C130124 | C130124 | Cat Dander Antigen IgE Antibody | A measurement of the Felis catus dander antigen IgE antibody in a biological specimen. |
| C130125 | C130125 | Cat Dander Antigen IgG Antibody | A measurement of the Felis catus dander antigen IgG antibody in a biological specimen. |
| C130126 | C130126 | Cat Dander Antigen IgA Antibody | A measurement of the Felis catus dander antigen IgA antibody in a biological specimen. |
| C130127 | C130127 | Cat Dander Antigen IgG4 Antibody | A measurement of the Felis catus dander antigen IgG4 antibody in a biological specimen. |
| C130128 | C130128 | Dog Dander Antigen IgE Antibody | A measurement of the Canis lupus dander antigen IgE antibody in a biological specimen. |
| C130129 | C130129 | Dog Dander Antigen IgG Antibody | A measurement of the Canis lupus dander antigen IgG antibody in a biological specimen. |
| C130130 | C130130 | Dog Dander Antigen IgA Antibody | A measurement of the Canis lupus dander antigen IgA antibody in a biological specimen. |
| C130131 | C130131 | Dog Dander Antigen IgG4 Antibody | A measurement of the Canis lupus dander antigen IgG4 antibody in a biological specimen. |
| C130132 | C130132 | American House Dust Mite IgE Antibody; D. farinae Antigen IgE Antibody; Dermatophagoides farinae IgE Antibody | A measurement of the Dermatophagoides farinae antigen IgE antibody in a biological specimen. |
| C130133 | C130133 | American House Dust Mite IgG Antibody; D. farinae Antigen IgG Antibody; Dermatophagoides farinae IgG Antibody | A measurement of the Dermatophagoides farinae antigen IgG antibody in a biological specimen. |
| C130134 | C130134 | D. pteronyssinus Antigen IgE Antibody; Dermatophagoides pteronyssinus IgE Antibody; European House Dust Mite IgE Antibody | A measurement of the Dermatophagoides pteronyssinus antigen IgE antibody in a biological specimen. |
| C130135 | C130135 | D. pteronyssinus Antigen IgG Antibody; Dermatophagoides pteronyssinus IgG Antibody; European House Dust Mite IgG Antibody | A measurement of the Dermatophagoides pteronyssinus antigen IgG antibody in a biological specimen. |
| C130136 | C130136 | American Cockroach Antigen IgE Antibody | A measurement of the Periplaneta americana antigen IgE antibody in a biological specimen. |
| C130137 | C130137 | American Cockroach Antigen IgA Antibody | A measurement of the Periplaneta americana antigen IgA antibody in a biological specimen. |
| C130138 | C130138 | American Cockroach Antigen IgG Antibody | A measurement of the Periplaneta americana antigen IgG antibody in a biological specimen. |
| C130139 | C130139 | American Cockroach Antigen IgG4 Antibody | A measurement of the Periplaneta americana antigen IgG4 antibody in a biological specimen. |
| C130140 | C130140 | German Cockroach Antigen IgE Antibody | A measurement of the Blattella germanica antigen IgE antibody in a biological specimen. |
| C130141 | C130141 | German Cockroach Antigen IgA Antibody | A measurement of the Blattella germanica antigen IgA antibody in a biological specimen. |
| C130142 | C130142 | German Cockroach Antigen IgG Antibody | A measurement of the Blattella germanica antigen IgG antibody in a biological specimen. |
| C130143 | C130143 | German Cockroach Antigen IgG4 Antibody | A measurement of the Blattella germanica antigen IgG4 antibody in a biological specimen. |
| C147276 | C147276 | Arachis hypogaea Antigen IgE Antibody; Peanut Antigen IgE Antibody | A measurement of the Arachis hypogaea antigen IgE antibody in a biological specimen. |
| C147277 | C147277 | Bread Wheat Antigen IgE Antibody; Triticum aestivum Antigen IgE Antibody | A measurement of the Triticum aestivum antigen IgE antibody in a biological specimen. |
| C147278 | C147278 | Glycine max Antigen IgE Antibody; Soybean Antigen IgE Antibody | A measurement of the Glycine max antigen IgE antibody in a biological specimen. |
| C147279 | C147279 | Corn Antigen IgE Antibody; Zea mays Antigen IgE Antibody | A measurement of the Zea mays antigen IgE antibody in a biological specimen. |
| C147280 | C147280 | Cow Milk Protein Antigen IgE Antibody | A measurement of the cow milk protein antigen IgE antibody in a biological specimen. |
| C147281 | C147281 | Egg White Antigen IgE Antibody | A measurement of the egg white antigen IgE antibody in a biological specimen. |
| C147282 | C147282 | White Oak Pollen IgE Antibody | A measurement of the Quercus alba pollen antigen IgE antibody in a biological specimen. |
| C147283 | C147283 | White Elm Pollen IgG Antibody | A measurement of the Ulmus americana pollen antigen IgG antibody in a biological specimen. |
| C147284 | C147284 | Boxelder Pollen IgE Antibody | A measurement of the Acer negundo pollen antigen IgE antibody in a biological specimen. |
| C147285 | C147285 | Common Ragweed Pollen IgE Antibody | A measurement of the Ambrosia elatior pollen antigen IgE antibody in a biological specimen. |
| C165875 | C165875 | Bermuda Grass Pollen IgE AB RAST Score | A classification of the amount of Cynodon dactylon pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165876 | C165876 | Birch Pollen IgE AB RAST Score | A classification of the amount of Betula pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165877 | C165877 | Cat Dander IgE AB RAST Score | A classification of the amount of Felis catus dander antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165878 | C165878 | German Cockroach IgE AB RAST Score | A classification of the amount of Blattella germanica antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165879 | C165879 | American House Dust Mite IgE Antibody RAST Score; D. farinae IgE AB RAST Score; Dermatophagoides farinae IgE Antibody RAST Score | A classification of the amount of Dermatophagoides farinae IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165880 | C165880 | D. pteronyssinus IgE AB RAST Score; Dermatophagoides pteronyssinus IgE Antibody RAST Score; European House Dust Mite IgE Antibody RAST Score | A classification of the amount of Dermatophagoides pteronyssinus antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165881 | C165881 | White Elm Pollen IgE Antibody | A measurement of the Ulmus americana pollen antigen IgE antibody in a biological specimen. |
| C165882 | C165882 | White Elm Pollen IgE AB RAST Score | A classification of the amount of Ulmus americana pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165883 | C165883 | Orchard Grass Pollen IgE AB RAST Score | A classification of the amount of Dactylis glomerata pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165884 | C165884 | Olive Tree Pollen IgE Antibody | A measurement of the Olea europaea pollen antigen IgE antibody in a biological specimen. |
| C165885 | C165885 | Olive Tree Pollen IgE AB RAST Score | A classification of the amount of Olea europaea pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165886 | C165886 | White Oak Pollen IgE AB RAST Score | A classification of the amount of Quercus alba pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165887 | C165887 | English Plantain Pollen IgE AB RAST Score; EnglishPlantain Pollen IgE AB RAST Score | A classification of the amount of Plantagio lanceolata pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165888 | C165888 | Russian Thistle Pollen IgE Antibody | A measurement of the Salsola tragus pollen antigen IgE antibody in a biological specimen. |
| C165889 | C165889 | Russian Thistle Pollen IgE AB RAST Score | A classification of the amount of Salsola tragus pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165890 | C165890 | Timothy Grass Pollen IgE AB RAST Score | A classification of the amount of Phleum pratense pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165891 | C165891 | Western Ragweed Pollen IgE AB RAST Score | A classification of the amount of Ambrosia psilostachya pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165892 | C165892 | Wild Rye Pollen IgE Antibody | A measurement of the Elymus tricoides pollen antigen IgE antibody in a biological specimen. |
| C165893 | C165893 | Wild Rye Pollen IgE AB RAST Score | A classification of the amount of Elymus tricoides pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165894 | C165894 | American House Dust Mite IgG4 Antibody; D. farinae Antigen IgG4 Antibody; Dermatophagoides farinae IgG4 Antibody | A measurement of the Dermatophagoides farinae antigen IgG4 antibody in a biological specimen. |
| C165895 | C165895 | Johnson Grass Pollen IgG4 Antibody | A measurement of the Sorghum halepense pollen IgG4 antibody in a biological specimen. |
| C165896 | C165896 | D. pteronyssinus Antigen IgG4 Antibody; Dermatophagoides pteronyssinus IgG4 Antibody; European House Dust Mite IgG4 Antibody | A measurement of the Dermatophagoides pteronyssinus antigen IgG4 antibody in a biological specimen. |
| C165897 | C165897 | Bermuda Grass Pollen IgG AB RAST Score | A classification of the amount of Cynodon dactylon pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165898 | C165898 | Birch Pollen IgG AB RAST Score | A classification of the amount of Betula pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165899 | C165899 | Silver Birch Pollen IgG AB RAST Score | A classification of the amount of Betula verrucosa pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165900 | C165900 | Cocksfoot Grass Pollen IgG RAST Score; Orchard Grass Pollen IgG AB RAST Score | A classification of the amount of Dactylis glomerata pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165901 | C165901 | English Plantain Pollen IgG AB RAST Score; EnglishPlantain Pollen IgG AB RAST Score | A classification of the amount of Plantagio lanceolata pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165902 | C165902 | Timothy Grass Pollen IgG AB RAST Score | A classification of the amount of Phleum pratense pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165903 | C165903 | Western Ragweed Pollen IgG AB RAST Score | A classification of the amount of Ambrosia psilostachya pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165904 | C165904 | Tree Mix Pollen IgG AB RAST Score | A classification of the amount of tree mix pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165905 | C165905 | Grass Mix Pollen IgG AB RAST Score | A classification of the amount of tree grass pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165906 | C165906 | Weed Mix Pollen IgG AB RAST Score | A classification of the amount of weed mix pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165907 | C165907 | Mold Mix IgG AB RAST Score | A classification of the amount of mold mix  IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165908 | C165908 | Animal Mix IgG AB RAST Score | A classification of the amount of animal mix IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165909 | C165909 | Industrial Mix IgG AB RAST Score | A classification of the amount of industrial mix IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165910 | C165910 | Bee Mix IgG AB RAST Score | A classification of the amount of bee mix IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165911 | C165911 | Dairy Mix IgG AB RAST Score | A classification of the amount of dairy mix IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165912 | C165912 | Shellfish Mix IgG AB RAST Score | A classification of the amount of shellfish mix IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165913 | C165913 | Nut Mix IgG AB RAST Score | A classification of the amount of nut mix IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165914 | C165914 | Cat Dander IgG AB RAST Score | A classification of the amount of Felis cattus dander IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165915 | C165915 | Dog Dander IgG AB RAST Score | A classification of the amount of Canis lupus IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165916 | C165916 | American House Dust Mite IgG Antibody RAST Score; D. farinae IgG AB RAST Score | A classification of the amount of D. farinae antigen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165917 | C165917 | D. pteronyssinus Antigen IgG AB RAST Score; Dermatophagoides pteronyssinus IgG Antibody; European House Dust Mite IgG Antibody | A classification of the amount of D. pteronyssinus antigen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165918 | C165918 | American Cockroach IgG AB RAST Score | A classification of the amount of Periplaneta americana antigen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165919 | C165919 | German Cockroach IgG AB RAST Score | A classification of the amount of Blattella germanica antigen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165920 | C165920 | White Elm Pollen IgG AB RAST Score | A classification of the amount of Ulmus americana pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165921 | C165921 | Silver Birch Pollen IgE AB RAST Score | A classification of the amount of Betula pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165922 | C165922 | Mixed Antigen IgE Antibody RAST Score | A classification of the amount of mixed antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165923 | C165923 | Tree Mix Pollen IgE AB RAST Score | A classification of the amount of tree mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165924 | C165924 | Grass Mix Pollen IgE AB RAST Score | A classification of the amount of grass mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165925 | C165925 | Weed Mix Pollen IgE AB RAST Score | A classification of the amount of weed mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165926 | C165926 | Mold Mix IgE AB RAST Score | A classification of the amount of mold mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165927 | C165927 | Animal Mix IgE AB RAST Score | A classification of the amount of animal mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165928 | C165928 | Industrial Mix IgE AB RAST Score | A classification of the amount of industrial mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165929 | C165929 | Bee Mix IgE AB RAST Score | A classification of the amount of bee mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165930 | C165930 | Shellfish Mix IgE AB RAST Score | A classification of the amount of shellfish mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165931 | C165931 | Nut Mix IgE AB RAST Score | A classification of the amount of nut mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165932 | C165932 | Dog Dander IgE AB RAST Score | A classification of the amount of canis lupus dander IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165933 | C165933 | American Cockroach IgE AB RAST Score | A classification of the amount of Periplaneta americana antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165934 | C165934 | Arachis hypogaea IgE AB RAST Score | A classification of the amount of Arachis hypogaea antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165935 | C165935 | Triticum aestivum IgE AB RAST Score | A classification of the amount of Triticum aestivum antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165936 | C165936 | Glycine max IgE AB RAST Score | A classification of the amount of Glycine max antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165937 | C165937 | Zea mays IgE AB RAST Score | A classification of the amount of Zea mays IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165938 | C165938 | Cow Milk Protein IgE AB RAST Score | A classification of the amount of cow milk protein IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165939 | C165939 | Egg White IgE AB RAST Score | A classification of the amount of egg white antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165940 | C165940 | Boxelder Pollen IgE AB RAST Score | A classification of the amount of Acer negundo pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165941 | C165941 | Common Ragweed Pollen IgE AB RAST Score | A classification of the amount of Ambrosia artemisiifolia pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C177958 | C177958 | Anacardium occidentale Nut Antigen IgE Antibody; Cashew Antigen IgE Antibody | A measurement of the cashew antigen IgE antibody in a biological specimen. |
| C177959 | C177959 | Triticum Species Antigen IgE Antibody; Wheat Antigen IgE Antibody | A measurement of any of the Triticum species of wheat antigen IgE antibody in a biological specimen. |
| C177960 | C177960 | Corylus Species Nut Antigen IgE Antibody; Hazelnut Antigen IgE Antibody | A measurement of the hazelnut antigen IgE antibody in a biological specimen. |
| C177961 | C177961 | Juglans Species Nut Antigen IgE Antibody; Walnut Antigen IgE Antibody | A measurement of the walnut antigen IgE antibody in a biological specimen. |
| C147313 | C1INH | Complement C1 Esterase Inhibitor | A measurement of the complement C1 esterase inhibitor in a biological specimen. |
| C186029 | C1Q | Complement C1q | A measurement of the complement C1q in a biological specimen. |
| C80173 | C1QAB | Complement C1q Antibody | A measurement of the complement C1q antibody in a biological specimen. |
| C80174 | C3 | Complement C3 | A measurement of the complement C3 in a biological specimen. |
| C80175 | C3A | Complement C3a | A measurement of the complement C3a in a biological specimen. |
| C163423 | C3ADARG | Acylation-Stimulating Protein; ASP; Complement C3a DesArg | A measurement of the complement C3a DesArg in a biological specimen. |
| C80176 | C3B | Complement C3b | A measurement of the complement C3b in a biological specimen. |
| C184521 | C3C | Complement C3c | A measurement of the complement C3c in a biological specimen. |
| C119271 | C3DAB | Complement C3d Antibody | A measurement of the complement C3d antibody in a biological specimen. |
| C165945 | C3M | Collagen III Neo-Peptide C3M | A measurement of the collagen III neo-peptide C3M in a biological specimen. |
| C80177 | C4 | Complement C4 | A measurement of the complement C4 in a biological specimen. |
| C80178 | C4A | Complement C4a | A measurement of the complement C4a in a biological specimen. |
| C127610 | C4D | Complement C4d | A measurement of the complement C4d in a biological specimen. |
| C160935 | C5 | Complement C5 | A measurement of the total complement C5 in a biological specimen. |
| C80179 | C5A | Complement C5a | A measurement of the complement C5a in a biological specimen. |
| C158235 | C5B9 | Complement C5b-9 | A measurement of the complement C5b-9 in a biological specimen. |
| C170579 | C5B9S | sC5b-9; Smac; Soluble Complement C5b-9; Soluble MAC; Soluble Membrane Attack Complex; TCC; Terminal Complement Complex | A measurement of the soluble complement C5b-9 in a biological specimen. |
| C161357 | C5FR | Complement C5, Free | A measurement of the free complement C5 in a biological specimen. |
| C64488 | CA | Calcium | A measurement of the calcium in a biological specimen. |
| C79089 | CA125AG | CA125; CA125AG; Cancer Antigen 125; Carbohydrate Antigen 125; MUC16; Mucin-16; Mucin-16, Cell Surface Associated | A measurement of the cancer antigen 125 in a biological specimen. |
| C103362 | CA15_3AG | Cancer Antigen 15-3; Carbohydrate Antigen 15-3 | A measurement of the cancer antigen 15-3 in a biological specimen. |
| C81982 | CA19_9AG | Cancer Antigen 19-9; Carbohydrate Antigen 19-9 | A measurement of the cancer antigen 19-9 in a biological specimen. |
| C103361 | CA1AG | Cancer Antigen 1 | A measurement of the cancer antigen 1 in a biological specimen. |
| C172526 | CA242AG | Cancer Antigen 242; Carbohydrate Antigen 242 | A measurement of the cancer antigen 242 in a biological specimen. |
| C111143 | CA2729AG | Cancer Antigen 27-29 | A measurement of the cancer antigen 27-29 in a biological specimen. |
| C187794 | CA50AG | CA50; Cancer Antigen 50; Carbohydrate Antigen 50 | A measurement of the cancer antigen 50 in a biological specimen. |
| C106505 | CA72_4AG | CA 72-4; Cancer Antigen 72-4; Carbohydrate Antigen 72-4 | A measurement of the cancer antigen 72-4 in a biological specimen. |
| C74702 | CABOT | Cabot Rings | A measurement of the Cabot rings (red-purple staining, threadlike, ring or figure 8 shaped filaments in an erythrocyte) in a biological specimen. |
| C96589 | CACLR | Calcium Clearance | A measurement of the volume of serum or plasma that would be cleared of calcium by excretion of urine for a specified unit of time (e.g. one minute). |
| C119272 | CACR | Calcium Corrected | A measurement of calcium, which has been corrected using an unspecified protein, in a biological specimen. |
| C154753 | CACRALB | Calcium Corrected for Albumin | A measurement of calcium, which has been corrected for albumin, in a biological specimen. |
| C79439 | CACREAT | Calcium/Creatinine | A relative measurement (ratio or percentage) of the calcium to creatinine in a biological specimen. |
| C147314 | CACRTP | Calcium Corrected for Total Protein | A measurement of calcium, which has been corrected for total protein, in a biological specimen. |
| C150815 | CAEXR | Calcium Excretion Rate | A measurement of the amount of calcium being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C75346 | CAFFEINE | Caffeine | A measurement of the caffeine in a biological specimen. |
| C81948 | CAION | Calcium, Ionized | A measurement of the ionized calcium in a biological specimen. |
| C125941 | CAIONPH | Calcium, Ionized pH Adjusted | A measurement of the pH adjusted ionized calcium in a biological specimen. |
| C125942 | CALB | Calbindin | A measurement of the total calbindin in a biological specimen. |
| C82005 | CALPRO | Calprotectin | A measurement of the calprotectin in a biological specimen. |
| C124339 | CAMP | Cyclic Adenosine 3,5-Monophosphate | A measurement of cyclic adenosine 3,5-monophosphate in a biological specimen. |
| C186030 | CAMPCRT | Cyclic Adenosine 3,5-Monophosphate/Creatinine; Cyclic Adenosine Monophosphate/Creat; Cyclic Adenosine Monophosphate/Creatinine | A relative measurement (ratio) of the cyclic adenosine 3,5-monophosphate to creatinine in a biological specimen. |
| C176310 | CAN | Coefficient of Nitrogen Absorption | A measurement of the coefficient of nitrogen absorption in a biological specimen. |
| C74689 | CANNAB | Cannabinoids | A measurement of any cannabinoid class drug present in a biological specimen. |
| C165946 | CANNABM | Cannabinoid Metabolites; Cannabis Metabolites; Marijuana Metabolites | A measurement of any cannabinoid drug class metabolite(s) present in a biological specimen. |
| C135402 | CANNABS | Cannabinoids, Synthetic | A measurement of any synthetic cannabinoid class drug present in a biological specimen. |
| C187793 | CAOXAEXR | Calcium Oxalate Excretion Rate | A measurement of the amount of calcium oxalate being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C139087 | CAPHOS | Calcium/Phosphate; Calcium/Phosphorus | A relative measurement (ratio) of the calcium to phosphorus in a biological specimen. |
| C103360 | CAPHOSPD | Calcium - Phosphorus Product | A measurement of the product of the calcium and phosphate measurements in a biological specimen. |
| C96591 | CARBXHGB | Carboxyhemoglobin | A measurement of the carboxyhemoglobin, carbon monoxide-bound hemoglobin, in a biological specimen. |
| C177975 | CARIPRZN | Cariprazine | A measurement of the cariprazine in a biological specimen. |
| C74682 | CARNIT | Carnitine | A measurement of the total carnitine in a biological specimen. |
| C92288 | CARNITAT | Carnitine Acetyl Transferase | A measurement of the carnitine acetyl transferase in a biological specimen. |
| C74677 | CARNITF | Carnitine, Free | A measurement of the free carnitine in a biological specimen. |
| C163424 | CARNTEXR | Carnitine Excretion Rate | A measurement of the amount of carnitine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C142273 | CARTP | CART; Cocaine Amphetamine-Reg Transcript Prot; Cocaine and Amphetamine-Regulated Transcript Protein | A measurement of the cocaine and amphetamine-regulated transcript protein in a biological specimen. |
| C74763 | CASTS | Casts | A statement that indicates casts were looked for in a biological specimen. |
| C96590 | CASULPH | Calcium Sulphate | A measurement of the calcium sulphate in a biological specimen. |
| C184534 | CATHNON | Cathinone | A measurement of the cathinone in a biological specimen. |
| C103357 | CATNINB | Beta Catenin | A measurement of the beta catenin in a biological specimen. |
| C135403 | CBA | Ba Fragment of Complement Factor B; Ba Fragment of Factor B; Complement Ba | A measurement of the Ba fragment of complement factor B in a biological specimen. |
| C172510 | CBANH9 | CA9; CAIX; Carbonic Anhydrase 9 | A measurement of the carbonic anhydrase 9 in a biological specimen. |
| C80172 | CBB | Bb Fragment of Complement Factor B; Bb Fragment of Factor B; Complement Bb | A measurement of the Bb fragment of complement factor B in a biological specimen. |
| C172520 | CBS | Cystathionine Beta-Synthase | A measurement of the cystathionine beta-synthase in a biological specimen. |
| C74850 | CCK | Cholecystokinin; Pancreozymin | A measurement of the cholecystokinin hormone in a biological specimen. |
| C130156 | CCL12 | Chemokine (C-C Motif) Ligand 12; Monocyte Chemotactic Protein 5 | A measurement of the CCL12, chemokine (C-C motif) ligand 12, in a biological specimen. |
| C165947 | CCL13 | C-C Motif Chemokine Ligand 13; Chemokine (C-C Motif) Ligand 13; CKb10; MCP-4; NCC1; SCYA13; SCYL1 | A measurement of the CCL13, chemokine (C-C motif) ligand 13, in a biological specimen. |
| C165948 | CCL16 | Chemokine (C-C Motif) Ligand 16; CKb12; HCC-4; ILINCK; LCC-1; LEC; LMC; Mtn-1; NCC4; SCYA16; SCYL4 | A measurement of the CCL16, chemokine (C-C motif) ligand 16, in a biological specimen. |
| C112236 | CCL17 | ABCD-2; Chemokine (C-C Motif) Ligand 17; SCYA17; TARC; Thymus and Activation Regulated Chemokine | A measurement of the CCL17, chemokine (C-C motif) ligand 17, in a biological specimen. |
| C112237 | CCL18 | AMAC-1; AMAC1; Chemokine (C-C Motif) Ligand 18; CKB7; DC-CK1; DCCK1; Macrophage inflammatory protein-4; MIP4; PARC; Pulmonary and Activation-Regulated Chemokine; SCYA18 | A measurement of the CCL18, chemokine (C-C motif) ligand 18, in a biological specimen. |
| C130157 | CCL19 | Chemokine (C-C Motif) Ligand 19; Macrophage Inflammatory Protein 3 Beta; MIP3B | A measurement of the CCL19, chemokine (C-C motif) ligand 19, in a biological specimen. |
| C161362 | CCL20 | CCL20; Chemokine (C-C Motif) Ligand 20; LARC; Liver Activation Regulated Chemokine; Macrophage Inflammatory Protein-3 Alpha; MIP3A | A measurement of the chemokine (C-C motif) ligand 20 in a biological specimen. |
| C147315 | CCL21 | 6Ckine; Chemokine (C-C Motif) Ligand 21; Secondary Lymphoid Tissue Chemokine | A measurement of the CCL21, chemokine (C-C motif) ligand 21, in a biological specimen. |
| C165949 | CCL23 | Chemokine (C-C Motif) Ligand 23; CK-BETA-8; Ckb-8-1; CKb8; Hmrp-2a; MIP3; MPIF-1; SCYA23 | A measurement of the CCL23, chemokine (C-C motif) ligand 23, in a biological specimen. |
| C165950 | CCL25 | Chemokine (C-C Motif) Ligand 25; Ckb15; SCYA25; TECK | A measurement of the CCL25, chemokine (C-C motif) ligand 25, in a biological specimen. |
| C156520 | CCL2EXR | Chemokine (C-C Motif) Ligand 2 Excr Rate; Chemokine (C-C Motif) Ligand 2 Excretion Rate; MCP1 Excretion Rate | A measurement of the amount of chemokine (C-C Motif) ligand 2 being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C130158 | CCL7 | Chemokine (C-C Motif) Ligand 7; MCP3; Monocyte Chemotactic Protein 3 | A measurement of the CCL7, chemokine (C-C motif) ligand 7, in a biological specimen. |
| C165951 | CCL8 | Chemokine (C-C Motif) Ligand 8; HC14; MCP2; SCYA10; SCYA8 | A measurement of the CCL8, chemokine (C-C motif) ligand 8, in a biological specimen. |
| C96595 | CCPAB | Cyclic Citrullinated Peptide Antibody | A measurement of the cyclic citrullinated peptide antibody in a biological specimen. |
| C147316 | CCPIGGAB | Cyclic Citrullinated Peptide IgG Ab; Cyclic Citrullinated Peptide IgG Antibody | A measurement of the cyclic citrullinated peptide IgG antibody in a biological specimen. |
| C122103 | CCR5 | C-C Chemokine Receptor Type 5; CD195 | A measurement of the CCR5, chemokine (C-C motif) receptor type 5, in a biological specimen. |
| C154728 | CD163S | Soluble CD163 | A measurement of the soluble CD163 in a biological specimen. |
| C187826 | CD38S | Cyclic ADP Ribose Hydrolase; Soluble CD38 | A measurement of the soluble CD38 protein in a biological specimen. |
| C172498 | CDCA | Chenic Acid; Chenocholic Acid; Chenodeoxycholate; Chenodeoxycholic Acid | A measurement of the chenodeoxycholate in a biological specimen. |
| C176239 | CDCACM | Chenodeoxycholate Compounds; Chenodeoxycholic Acid Compounds | A measurement of the chenodeoxycholic acid, glycochenodeoxycholic acid, and taurochenodeoxycholic acid in a biological specimen. |
| C101016 | CDT | Carbohydrate-Deficient Transferrin | A measurement of transferrin with a reduced number of carbohydrate moieties in a biological specimen. |
| C125943 | CDTTFRN | Carb-Deficient Transferrin/Transferrin | A relative measurement (ratio or percentage) of the carbohydrate-deficient transferrin to total transferrin in a biological specimen. |
| C81983 | CEA | Carcinoembryonic Antigen | A measurement of the carcinoembryonic antigen in a biological specimen. |
| C172511 | CEACAM1 | BGP; Biliary Glycoprotein; Carcinoembryonic Antigen Cell Adhesion Molecule 1; CD66a; CEA Cell Adhesion Molecule 1; CEA Related Cell Adhesion Molecule 1 | A measurement of the carcinoembryonic antigen (CEA) cell adhesion molecule 1 in a biological specimen. |
| C96592 | CEC | Circulating Endothelial Cells | A measurement of the circulating endothelial cells in a biological specimen. |
| C111234 | CEIMCE | Immature Cells/Total Cells | A relative measurement (ratio or percentage) of the immature hematopoietic cells to total cells in a biological specimen. |
| C48938 | CELLS | Cells | A measurement of the total cells in a biological specimen. |
| C96672 | CELLSIM | Immature Cells | A measurement of the total immature cells in a blood specimen. |
| C111153 | CELLULAR | Cellularity; Cellularity Grade | A measurement of the degree, quality or condition of cells in a biological specimen. |
| C17768 | CEMORPH | Cell Morphology | An examination or assessment of the form and structure of cells. |
| C111154 | CENTROAB | Centromere B Antibodies | A measurement of centromere B antibodies in a biological specimen. |
| C120632 | CETP | Cholesteryl Ester Transfer Protein | A measurement of the cholesteryl ester transfer protein in a biological specimen. |
| C103380 | CETPA | Cholesteryl Ester Transfer Protein Act | A measurement of the biological activity of cholesteryl ester transfer protein in a biological specimen. |
| C176311 | CFA | Coefficient of Fat Absorption | A measurement of the coefficient of fat absorption in a biological specimen. |
| C122108 | CGA | Chromogranin A | A measurement of the chromogranin A in a biological specimen. |
| C161374 | CGADJMW | Choriogonadotropin Adj for Maternal Wt; Choriogonadotropin Adjusted for Maternal Weight | A measurement of choriogonadotropin, which has been adjusted for maternal body weight, in a biological specimen. |
| C111165 | CGMP | Cyclic Guanosine Monophosphate | A measurement of the cyclic guanosine 3,5-monophosphate in a biological specimen. |
| C147317 | CH100 | CH100; Complement CH100; Total Hemolytic Complement CH100 | A measurement of the complement required to lyse 100 percent of red blood cells in a biological specimen. |
| C100423 | CH50 | CH50; Complement CH50; Total Hemolytic Complement CH50 | A measurement of the complement required to lyse 50 percent of red blood cells in a biological specimen. |
| C139067 | CHCM | Corpuscular HGB Concentration Mean | A direct measurement of the concentration of hemoglobin within individual erythrocytes in a biological specimen, reported as a mean. |
| C138970 | CHCMR | Ret. Corpuscular HGB Concentration Mean; Reticulocyte Corpuscular Hemoglobin Concentration Mean | An indirect measurement of the average concentration of hemoglobin per reticulocyte in a biological specimen, calculated as the ratio of hemoglobin to hematocrit. |
| C139066 | CHCNT | Cellular Hemoglobin Content; CH; Corpuscular Hemoglobin Content | A measurement of the mean erythrocyte hemoglobin content within an individual erythrocyte, calculated as the product of cell volume and cell hemoglobin concentration. |
| C181430 | CHDH7A25 | 7alpha,25-Dihydroxycholesterol | A measurement of the 7alpha,25-dihydroxycholesterol in a biological specimen. |
| C181431 | CHDH7A27 | 7alpha,27-Dihydroxycholesterol | A measurement of the 7alpha,27-dihydroxycholesterol in a biological specimen. |
| C139068 | CHDW | Corpuscular Hemoglobin Concentration Distribution Width; Corpuscular HGB Conc Distribution Width | A measurement of the standard deviation of hemoglobin concentrations in erythrocytes in a biological specimen, calculated as the standard deviation of hemoglobin content divided by the mean hemoglobin content. |
| C139069 | CHDWR | Ret Corpuscular HGB Conc Distr Width; Reticulocyte Corpuscular Hemoglobin Distribution Width | A measurement of the standard deviation of hemoglobin concentrations in reticulocytes in a biological specimen, calculated as the standard deviation of hemoglobin content divided by the mean hemoglobin content. |
| C181423 | CHE24S25 | 24(S),25-Epoxycholesterol | A measurement of the 24(S),25-epoxycholesterol in a biological specimen. |
| C187795 | CHITTDS | Chitinase 1; Chitotriosidase; Chitotriosidase-1 | A measurement of the chitotriosidase-1 in a biological specimen. |
| C120633 | CHLMCRN | Chylomicrons | A measurement of the chylomicrons in a biological specimen. |
| C174302 | CHLMCRNT | Chylomicron Triglyceride | A measurement of the chylomicron triglyceride in a biological specimen. |
| C184612 | CHLRHDRT | Chloral Hydrate; Mickey Finn; Trichloroacetaldehyde Monohydrate | A measurement of the chloral hydrate in a biological specimen. |
| C177968 | CHLRPMZN | Chlorpromazine | A measurement of the chlorpromazine in a biological specimen. |
| C105586 | CHOL | Cholesterol; Total Cholesterol | A measurement of the cholesterol in a biological specimen. |
| C172499 | CHOLATE | Cholate; Cholic Acid | A measurement of the cholate in a biological specimen. |
| C176232 | CHOLCM | Cholate Compounds; Cholic Acid Compounds | A measurement of the cholic acid, glycocholic acid, hyocholic acid, and taurocholic acid in a biological specimen. |
| C181420 | CHOLH20S | 20(S)-Hydroxycholesterol; 20-Alpha-Hydroxycholesterol | A measurement of the 20(S)-hydroxycholesterol in a biological specimen. |
| C181421 | CHOLH22R | 22(R)-Hydroxycholesterol | A measurement of the 22(R)-hydroxycholesterol in a biological specimen. |
| C181422 | CHOLH22S | 22(S)-Hydroxycholesterol | A measurement of the 22(S)-hydroxycholesterol in a biological specimen. |
| C181424 | CHOLH24R | 24(R)-Hydroxycholesterol | A measurement of the 24(R)-hydroxycholesterol in a biological specimen. |
| C181425 | CHOLH24S | 24(S)-Hydroxycholesterol | A measurement of the 24(S)-hydroxycholesterol in a biological specimen. |
| C181426 | CHOLH25 | 25-Hydroxycholesterol | A measurement of the 25-hydroxycholesterol in a biological specimen. |
| C181427 | CHOLH27 | 27-Hydroxycholesterol | A measurement of the 27-hydroxycholesterol in a biological specimen. |
| C181432 | CHOLH7A | 7alpha-Hydroxycholesterol | A measurement of the 7alpha-hydroxycholesterol in a biological specimen. |
| C181433 | CHOLH7B | 7beta-Hydroxycholesterol | A measurement of the 7beta-hydroxycholesterol in a biological specimen. |
| C80171 | CHOLHDL | Cholesterol/HDL-Cholesterol | A relative measurement (ratio or percentage) of total cholesterol to high-density lipoprotein cholesterol (HDL-C) in a biological specimen. |
| C92289 | CHOLINES | Cholinesterase | A measurement of the cholinesterase in a biological specimen. |
| C181434 | CHOLK7 | 7-Ketocholesterol; 7-Oxocholesterol | A measurement of the 7-ketocholesterol in a biological specimen. |
| C156514 | CHOLOH4B | 4-Beta-Hydroxycholesterol | A measurement of the 4-beta-hydroxycholesterol in a biological specimen. |
| C181435 | CHOLSTNL | 5alpha-Cholestanol; Beta-Cholestanol; Cholestanol; Dehydrocholesterol; Zymostanol | A measurement of the cholestanol in a biological specimen. |
| C181436 | CHOLSULF | Cholesterol Sulfate | A measurement of the cholesterol sulfate in a biological specimen. |
| C147318 | CHRMTNAB | Chromatin Antibodies | A measurement of the chromatin antibodies in a biological specimen. |
| C111159 | CHYTRYP | Chymotrypsin | A measurement of the total chymotrypsin in a biological specimen. |
| C127611 | CIC | Circulating Immune Complexes | A measurement of the circulating immune complexes in a biological specimen. |
| C122109 | CIT | Citrulline | A measurement of the citrulline in a biological specimen. |
| C122110 | CITCREAT | Citrate/Creatinine; Citric Acid/Creatinine | A relative measurement (ratio or percentage) of the citrate to creatinine in a biological specimen. |
| C92248 | CITRATE | Citrate; Citric Acid | A measurement of the citrate in a biological specimen. |
| C163425 | CITRTEXR | Citrate Excretion Rate | A measurement of the amount of citrate being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C64489 | CK | CPK; Creatine Kinase; Creatine Phosphokinase | A measurement of the total creatine kinase in a biological specimen. |
| C64490 | CKBB | Creatine Kinase BB | A measurement of the homozygous B-type creatine kinase in a biological specimen. |
| C79466 | CKBBCK | Creatine Kinase BB/Total Creatine Kinase | A relative measurement (ratio or percentage) of the BB-type creatine kinase to total creatine kinase in a biological specimen. |
| C64491 | CKMB | Creatine Kinase MB | A measurement of the heterozygous MB-type creatine kinase in a biological specimen. |
| C79441 | CKMBCK | Creatine Kinase MB/Total Creatine Kinase | A relative measurement (ratio or percentage) of the MB-type creatine kinase to total creatine kinase in a biological specimen. |
| C64494 | CKMM | Creatine Kinase MM | A measurement of the homozygous M-type creatine kinase in a biological specimen. |
| C79442 | CKMMCK | Creatine Kinase MM/Total Creatine Kinase | A relative measurement (ratio or percentage) of the MM-type creatine kinase to total creatine kinase in a biological specimen. |
| C147319 | CKMT1CK | CK, Macromolecular Type 1/Total CK; Creatine Kinase, Macromolecular Type 1/Total Creatine Kinase | A relative measurement (ratio or percentage) of the macromolecular type 1 creatine kinase to total creatine kinase in a biological specimen. |
| C147320 | CKMT2CK | CK, Macromolecular Type 2/Total CK; Creatine Kinase, Macromolecular Type 2/Total Creatine Kinase | A relative measurement (ratio or percentage) of the macromolecular type 2 creatine kinase to total creatine kinase in a biological specimen. |
| C64495 | CL | Chloride | A measurement of the chloride in a biological specimen. |
| C96594 | CLARITY | Clarity | A measurement of the transparency of a biological specimen. |
| C106509 | CLCLR | Chloride Clearance | A measurement of the volume of serum or plasma that would be cleared of chloride by excretion of urine for a specified unit of time (e.g. one minute). |
| C79440 | CLCREAT | Chloride/Creatinine | A relative measurement (ratio or percentage) of the chloride to creatinine in a biological specimen. |
| C74848 | CLCTONN | Calcitonin | A measurement of the calcitonin hormone in a biological specimen. |
| C74849 | CLCTRIOL | Calcitriol | A measurement of the calcitriol hormone in a biological specimen. |
| C135405 | CLEPNSQE | Columnar Epi Cells/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the columnar epithelial cells to non-squamous epithelial cells in a biological specimen. |
| C150816 | CLEXR | Chloride Excretion Rate | A measurement of the amount of chloride being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C139082 | CLNZPM | Clonazepam | A measurement of the clonazepam present in a biological specimen. |
| C184613 | CLOBAZAM | Clobazam; cloBAZam | A measurement of the clobazam in a biological specimen. |
| C184581 | CLOSTBL | Clostebol | A measurement of the clostebol in a biological specimen. |
| C181438 | CLOTRTC | Clot Retraction; Clot Retraction, Qualitative | A qualitative assessment of clot retraction in a biological specimen. |
| C181437 | CLOTRTCT | Clot Retraction Time | A measurement of the amount of time it takes for a clot to retract, or pull away from, the wall of a glass collection container. |
| C184580 | CLPHTRMN | Chlorphentermine | A measurement of the chlorphentermine in a biological specimen. |
| C75371 | CLRDZPXD | Chlordiazepoxide | A measurement of the chlordiazepoxide present in a biological specimen. |
| C139077 | CLRZPT | Clorazepate | A measurement of the clorazepate present in a biological specimen. |
| C187805 | CLT | Clot Lysis Time; ECLT; ELT; Euglobulin Clot Lysis Time; Euglobulin Lysis Time | A measurement of the amount of time it takes for dissolution of a fibrin clot in a biological specimen. |
| C102261 | CLUECE | Clue Cells | A measurement of the clue cells in a biological specimen. |
| C186031 | CLZPMAOM | Clonazepam and/or Metabolites | A measurement of the clonazepam and/or its metabolite(s) present in a biological specimen, for an assay that can measure both clonazepam and its metabolites. |
| C139084 | CMONOX | Carbon Monoxide | A measurement of the carbon monoxide in a biological specimen. |
| C163426 | CMPK2 | Cytidine-Uridine Monophosphate Kinase 2; Cytidine/Uridine Monophosphate Kinase 2 | A measurement of the cytidine-uridine monophosphate kinase 2 in a biological specimen. |
| C122111 | CNTIGGAB | Centromere IgG Antibody; Centromere Protein B | A measurement of the centromere IgG antibody in a biological specimen. |
| C64545 | CO2 | Carbon Dioxide | A measurement of the carbon dioxide gas in a biological specimen. |
| C112239 | COAGIDX | CI; Coagulation Index | A measurement of the efficiency of coagulation of a biological specimen. This is calculated by a mathematical formula that takes into account the R value, K value, angle and maximum amplitude of clot formation. |
| C172490 | COCAAOM | Cocaine and/or Metabolites | A measurement of the cocaine and/or its metabolite(s) present in a biological specimen, for an assay that can measure both cocaine and its metabolites. |
| C156510 | COCAETH | Cocaethylene; Cocaine Ethyl | A measurement of the cocaethylene present in a biological specimen. |
| C74690 | COCAINE | Cocaine | A measurement of the cocaine present in a biological specimen. |
| C172491 | COCAM | Cocaine Metabolites | A measurement of any cocaine drug class metabolite(s) present in a biological specimen. |
| C142274 | COCBNZEC | Cocaine Benzoylecgonine Ecgonine | A measurement of the cocaine, benzoylecgonine, and/or ecgonine in a biological specimen. |
| C74877 | CODEINE | Codeine | A measurement of the codeine present in a biological specimen. |
| C103383 | COL4 | Collagen Type IV | A measurement of the collagen type IV in a biological specimen. |
| C64546 | COLOR | Color | A measurement of the color of a biological specimen. |
| C111145 | COMP | Cartilage Oligomeric Matrix Protein | A measurement of the cartilage oligomeric matrix protein in a biological specimen. |
| C102282 | CONDUCTU | Urine Conductivity | A measurement of the urine conductivity which is a non-linear function of the electrolyte concentration in the urine. |
| C95110 | CONSIST | Consistency | A description about the firmness or make-up of an entity. |
| C127612 | COPEP | Copeptin | A measurement of the copeptin in a biological specimen. |
| C111161 | COPPER | Copper; Cu | A measurement of copper in a biological specimen. |
| C147321 | COQ10 | Coenzyme Q10; Ubiquinone 10 | A measurement of the ubiquinone 10 in a biological specimen. |
| C106512 | CORCREAT | Cortisol/Creatinine | A relative measurement (ratio or percentage) of the cortisol to creatinine present in a sample. |
| C88113 | CORTFR | Cortisol, Free | A measurement of the free, unbound cortisol in a biological specimen. |
| C74781 | CORTISOL | Cortisol; Total Cortisol | A measurement of the cortisol in a biological specimen. |
| C186032 | CORTOLA | Alpha Cortol; alpha-Cortol | A measurement of the alpha cortol in a biological specimen. |
| C186033 | CORTOLNA | Alpha Cortolone; alpha-Cortolone | A measurement of the alpha cortolone in a biological specimen. |
| C92249 | COTININE | Cotinine | A measurement of the cotinine in a biological specimen. |
| C165953 | CPB2 | Carboxypeptidase B2; CPU; PCPB; TAFI | A measurement of the carboxypeptidase B2 in a biological specimen. |
| C150837 | CPEPCRT | C-peptide/Creatinine | A relative measurement (ratio or percentage) of the C-peptide to creatinine in a biological specimen. |
| C187796 | CPEPEXR | C-Peptide Excretion Rate | A measurement of the amount of C-peptide being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C74736 | CPEPTIDE | C-peptide | A measurement of the C (connecting) peptide of insulin in a biological specimen. |
| C147322 | CRBMZPN | Carbamazepine | A measurement of the carbamazepine in a biological specimen. |
| C122112 | CRDIGAAB | Cardiolipin IgA Antibody | A measurement of the cardiolipin IgA antibody in a biological specimen. |
| C111144 | CRDIGGAB | Anti-Cardiolipin IgG Antibody; Cardiolipin IgG Antibody | A measurement of the cardiolipin IgG antibody in a biological specimen. |
| C103363 | CRDIGMAB | Cardiolipin IgM Antibody | A measurement of the cardiolipin IgM antibodies in a biological specimen. |
| C64547 | CREAT | Creatinine | A measurement of the creatinine in a biological specimen. |
| C25747 | CREATCLR | Creatinine Clearance | A measurement of the volume of serum or plasma that would be cleared of creatinine by excretion of urine for a specified unit of time (e.g. one minute). |
| C150817 | CREATEXR | Creatinine Excretion Rate | A measurement of the amount of creatinine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C74703 | CRENCE | Crenated Cells | A measurement of the crenated cells in a biological specimen. |
| C74851 | CRH | Corticotropin Releasing Factor; Corticotropin Releasing Hormone | A measurement of the corticotropin releasing hormone in a biological specimen. |
| C100432 | CRLPLSMN | Caeruloplasmin; Ceruloplasmin | A measurement of ceruloplasmin in a biological specimen. |
| C147323 | CRNTESTR | Carnitine Esters | A measurement of the total carnitine esters in a biological specimen. |
| C64548 | CRP | C Reactive Protein | A measurement of the C reactive protein in a biological specimen. |
| C184611 | CRSPRDL | Carisoprodol | A measurement of the carisoprodol in a biological specimen. |
| C147324 | CRTCLRBS | Creatinine Clearance Adjusted for BSA | A measurement of the volume of serum or plasma that would be cleared of creatinine by excretion of urine for a specified unit of time (e.g. one minute), adjusted for body surface area. |
| C150847 | CRTCLRE | Creatinine Clearance, Estimated | An estimate of the volume of serum or plasma that would be cleared of creatinine by excretion of urine for a specified unit of time (e.g. one minute). |
| C106511 | CRTCREAT | Corticosterone/Creatinine | A relative measurement (ratio or percentage) of the corticosterone to creatinine present in a sample. |
| C163427 | CRTFREXR | Cortisol, Free Excretion Rate | A measurement of the amount of free cortisol being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C186034 | CRTN | Carotene | A measurement of the total carotenes in a biological specimen. |
| C79434 | CRTRONE | Corticosterone | A measurement of corticosterone in a biological specimen. |
| C147325 | CRYGLBSR | Cryoglobulin Volume/Serum Volume | A relative measurement (ratio or percentage) of the volume of cryoglobulin to total serum volume in a biological specimen. |
| C147326 | CRYOFBRN | Cryofibrinogen | A measurement of the cryofibrinogen in a biological specimen. |
| C111164 | CRYOGLBN | Cryoglobulin | A measurement of cryoglobulin in a biological specimen. |
| C74673 | CRYSTALS | Crystals | A statement that indicates crystals were looked for in a biological specimen. |
| C120634 | CSAB | Cathepsin Antibody | A measurement of the total cathepsin antibody in a biological specimen. |
| C74762 | CSBACT | Bacterial Casts | A measurement of the bacterial casts present in a biological specimen. |
| C96588 | CSBROAD | Broad Casts | A measurement of the broad casts in a biological specimen. |
| C74764 | CSCELL | Cellular Casts | A measurement of the cellular (white blood cell, red blood cell, epithelial and bacterial) casts present in a biological specimen. |
| C150838 | CSCYL | Cylindroid Casts; Cylindroid Pseudocasts | A measurement of cylindroid casts (casts with a tapering end) in a biological specimen. |
| C74779 | CSEPI | Epithelial Casts | A measurement of the epithelial cell casts present in a biological specimen. |
| C112220 | CSEPI846 | 846-Epitope; Aggrecan Chondroitin Sulfate Epitope 846; Chondroitin Sulfate Epitope 846; Chondroitin Sulfate Proteoglycan 1 Epitope 846; CS846 | A measurement of the 846 epitope present on the chondroitin sulfate chains of aggrecan in a biological specimen. |
| C174229 | CSEPIR | Renal Epithelial Casts | A measurement of the renal epithelial cell casts in a biological specimen. |
| C174292 | CSEPIRT | Renal Tubular Epithelial Casts | A measurement of the renal tubular epithelial cell casts in a biological specimen. |
| C74766 | CSFAT | Fatty Casts | A measurement of the fatty casts present in a biological specimen. |
| C154735 | CSFIGIDX | CSF IgG Index; CSF Index; IgG Index | A relative measurement (ratio) of the IgG to albumin in cerebrospinal fluid to the IgG to albumin in serum. |
| C74768 | CSGRAN | Granular Casts | A measurement of the granular (coarse and fine) casts present in a biological specimen. |
| C74765 | CSGRANC | Granular Coarse Casts | A measurement of the coarse granular casts present in a biological specimen. |
| C74769 | CSGRANF | Granular Fine Casts | A measurement of the fine granular casts present in a biological specimen. |
| C74770 | CSHYAL | Hyaline Casts | A measurement of the hyaline casts present in a biological specimen. |
| C174305 | CSHYGR | Hyalogranular Casts | A measurement of the hyalogranular casts in a biological specimen. |
| C74771 | CSMIX | Mixed Casts | A measurement of the mixed (the cast contains a mixture of cell types) casts present in a biological specimen. |
| C186035 | CSPATH | Non-Hyalin Casts; Non-Hyaline Casts; Pathologic Casts | A measurement of the pathologic (non-hyaline) casts present in a biological specimen. |
| C189518 | CSPIG | Pigment Casts; Pigmented Casts | A measurement of the pigment casts present in a biological specimen. |
| C74772 | CSRBC | Erythrocyte Casts; RBC Casts | A measurement of the red blood cell casts present in a biological specimen. |
| C74776 | CSUNCLA | Unclassified Casts | A measurement of the unclassifiable casts present in a biological specimen. |
| C74777 | CSWAX | Waxy Casts | A measurement of the waxy casts present in a biological specimen. |
| C74778 | CSWBC | WBC Casts | A measurement of the white blood cell casts present in a biological specimen. |
| C96593 | CTC | Circulating Tumor Cells | A measurement of the circulating tumor cells in a biological specimen. |
| C186036 | CTCAPOP | Circulating Tumor Cells, Apoptotic | A measurement of the apoptotic circulating tumor cells in a biological specimen. |
| C186037 | CTCHLMN | Catecholamines | A measurement of the total catecholamines in a biological specimen. |
| C186038 | CTCTRAD | Circulating Tumor Cells, Traditional | A measurement of the traditional circulating tumor cells in a biological specimen. |
| C189504 | CTGF | Cellular Communication Network Factor 2; CN2; Connective Tissue Growth Factor; IGFBP8 | A measurement of the connective tissue growth factor in a biological specimen. |
| C189500 | CTLCREAT | Citrulline/Creatinine | A relative measurement (ratio or percentage) of the citrulline to creatinine in a biological specimen. |
| C147327 | CTLPRM | Citalopram | A measurement of the citalopram present in a biological specimen. |
| C189494 | CTLPRMD | Desmethyl Citalopram; Desmethylcitalopram; Norcitalopram | A measurement of the desmethylcitalopram in a biological specimen. |
| C189655 | CTLPRMDD | Di-Desmethylcitalopram | A measurement of the di-desmethylcitalopram in a biological specimen. |
| C80160 | CTOT | Complement Total; Total Hemolytic Complement | A measurement of the total complement in a biological specimen. |
| C82038 | CTXI | C-Terminal Telopeptide of Type I Collagen; Type I Collagen C-Telopeptides; Type I Collagen X-linked C-telopeptide | A measurement of the type I collagen cross-linked C-telopeptides in a biological specimen. |
| C187792 | CTXIB | Beta Isomer of C-Terminal Telopeptide of Type I Collagen; Type I Collagen C-Telopeptides Beta | A measurement of the beta isomer of type I collagen cross-linked C-telopeptides in a biological specimen. |
| C127613 | CTXICRT | Type I Collagen C-Telopeptides/Creat; Type I Collagen X-Linked C-Telopeptides/Creatinine | A relative measurement (ratio or percentage) of the type I collagen cross-linked C-telopeptides to creatinine in a biological specimen. |
| C82040 | CTXII | Type II Collagen C-Telopeptides; Type II Collagen X-Linked C-Telopeptides | A measurement of the type II collagen cross-linked C-telopeptides in a biological specimen. |
| C122113 | CTXIICRT | Type II Collagen C-Telopeptides/Creat; Type II Collagen X-Linked C-Telopeptides/Creatinine | A relative measurement (ratio or percentage) of the type II collagen cross-linked C-telopeptides to creatinine in a biological specimen. |
| C161361 | CX3CL1 | Chemokine (C-X3-C motif) Ligand 1; Fractalkine; Neurotactin | A measurement of the chemokine (C-X3-C motif) ligand 1 in a biological specimen. |
| C128952 | CXCL1 | Chemokine (C-X-C Motif) Ligand 1; GRO Alpha; GRO/KC; Melanoma Growth Stimulating Activity, Alpha | A measurement of the CXCL1, chemokine (C-X-C motif) ligand 1, in a biological specimen. |
| C112238 | CXCL10 | Chemokine (C-X-C Motif) Ligand 10; Interferon Gamma-induced Protein 10; Interferon-inducible Protein-10; IP-10; Small-inducible Cytokine B10 | A measurement of the CXCL10, chemokine (C-X-C motif) ligand 10, in a biological specimen. |
| C161360 | CXCL11 | Chemokine (C-X-C Motif) Ligand 11; I-TAC; IFN-inducible T Cell Alpha Chemoattractant; ITAC | A measurement of the chemokine (C-X-C motif) ligand 11 in a biological specimen. |
| C165954 | CXCL12 | Chemokine (C-X-C Motif) Ligand 12; IRH; PBSF; SCYB12; SDF1; SDF1A; SDF1B; Stromal Cell-Derived Factor-1 Alpha; Stromal Cell-Derived Factor-1 Beta; TLSF; TPAR1 | A measurement of the CXCL12, chemokine (C-X-C motif) ligand 12, in a biological specimen. |
| C147328 | CXCL13 | B Lymphocyte Chemoattractant; Chemokine (C-X-C Motif) Ligand 13 | A measurement of the CXCL13, chemokine (C-X-C motif) ligand 13, in a biological specimen. |
| C186039 | CXCL2 | Chemokine (C-X-C Motif) Ligand 2; GRO Beta; GRO2; MIP2-Alpha | A measurement of the CXCL2, chemokine (C-X-C motif) ligand 2, in a biological specimen. |
| C147329 | CXCL3 | Chemokine (C-X-C Motif) Ligand 3; GRO Gamma; Macrophage Inflammatory Protein 2-Beta; MIP2 Beta; MIP2B | A measurement of the CXCL3, chemokine (C-X-C motif) ligand 3, in a biological specimen. |
| C147330 | CXCL4 | Chemokine (C-X-C Motif) Ligand 4; Oncostatin A; Platelet Factor 4; PLF4 | A measurement of the CXCL4, chemokine (C-X-C motif) ligand 4, in a biological specimen. |
| C130159 | CXCL6 | Chemokine (C-X-C Motif) Ligand 6; GCP2; Granulocyte Chemotactic Protein 2 | A measurement of the CXCL6, chemokine (C-X-C motif) ligand 6, in a biological specimen. |
| C165955 | CXCL7 | B-TG1; Beta-TG; Chemokine (C-X-C Motif) Ligand 7; CTAP-III; CTAP3; CTAPIII; LA-PF4; LDGF; MDGF; NAP-2; Neutrophil-Activating Peptide 2; PBP; PPBP; Pro-Platelet Basic Protein; SCYB7; TC1; TC2; TGB; TGB1; THBGB; THBGB1 | A measurement of the pro-platelet basic protein in a biological specimen. |
| C165956 | CXCL9 | Chemokine (C-X-C Motif) Ligand 9; CMK; crg-10; Humig; MIG; SCYB9 | A measurement of the CXCL9, chemokine (C-X-C motif) ligand 9, in a biological specimen. |
| C100431 | CXCR3 | CD183; Chemokine (C-X-C Motif) Receptor 3; CXCR3; GPR9 | A measurement of the CXCR3, chemokine (C-X-C motif) receptor 3, in a biological specimen. |
| C187797 | CXCR4 | CD184; Chemokine (C-X-C Motif) Receptor 4; LPS-Associated Protein 3; Stromal Cell-Derived Factor 1 Receptor | A measurement of the CXCR4, chemokine (C-X-C motif) receptor 4, in a biological specimen. |
| C105590 | CYAMMBIU | Acid Ammonium Urate Crystals; Ammonium Biurate Crystals; Ammonium Urate Crystals | A measurement of the ammonium biurate crystals present in a biological specimen. |
| C74759 | CYAMMOX | Ammonium Oxalate Crystals | A measurement of the ammonium oxalate crystals present in a urine specimen. |
| C74665 | CYAMORPH | Amorphous Crystals | A measurement of the amorphous (Note: phosphate or urate, depending on pH) crystals present in a biological specimen. |
| C92243 | CYAMPPH | Amorphous Phosphate Crystals | A measurement of the amorphous phosphate crystals in a biological specimen. |
| C92244 | CYAMPURT | Amorphous Urate Crystals | A measurement of the amorphous urate crystals in a biological specimen. |
| C74668 | CYBILI | Bilirubin Crystals | A measurement of the bilirubin crystals present in a biological specimen. |
| C74669 | CYCACAR | Calcium Carbonate Crystals | A measurement of the calcium carbonate crystals present in a biological specimen. |
| C74670 | CYCAOXA | Calcium Oxalate Crystals | A measurement of the calcium oxalate crystals present in a biological specimen. |
| C74671 | CYCAPHOS | Calcium Phosphate Crystals | A measurement of the calcium phosphate crystals present in a biological specimen. |
| C124340 | CYCASULF | Calcium Sulfate Crystals | A measurement of the calcium sulfate crystals present in a biological specimen. |
| C74672 | CYCHOL | Cholesterol Crystals | A measurement of the cholesterol crystals present in a biological specimen. |
| C74674 | CYCYSTIN | Cystine Crystals | A measurement of the cystine crystals present in a biological specimen. |
| C135407 | CYDCPHOS | Dicalcium Phosphate Crystals | A measurement of dicalcium phosphate crystals in a biological specimen. |
| C156533 | CYDRUG | Drug Crystals | A measurement of the drug crystals in a biological specimen. |
| C130160 | CYFRA18 | Cytokeratin 18 Fragment | A measurement of the cytokeratin 18 fragment in a biological specimen. |
| C106514 | CYFRA211 | CYFRA21-1; Cytokeratin 19 Fragment 21-1 | A measurement of the cytokeratin 19 fragment 21-1 in a biological specimen. |
| C112288 | CYHGBC | Hemoglobin C Crystals | A measurement of hemoglobin C crystals in a biological specimen. |
| C74754 | CYHIPPAC | Hippurate Crystals; Hippuric Acid Crystals | A measurement of the hippuric acid crystals present in a biological specimen. |
| C74680 | CYLEUC | Leucine Crystals | A measurement of the leucine crystals present in a biological specimen. |
| C74681 | CYMSU | Monosodium Urate Crystals; Sodium Urate Crystals | A measurement of the monosodium urate crystals present in a biological specimen. |
| C161355 | CYP2C9 | Cytochrome P450 2C9 | A measurement of the cytochrome P450 2C9 enzyme in a biological specimen. |
| C174304 | CYPHOS | Phosphate Crystals | A measurement of the total phosphate crystals in a biological specimen. |
| C106513 | CYSCREAT | Cystatin C/Creatinine | A relative measurement (ratio or percentage) of the cystatin C to creatinine present in a sample. |
| C189517 | CYSLTR1 | CysLTR1; Cysteinyl Leukotriene Receptor 1 | A measurement of the cysteinyl leukotriene receptor 1 in a biological specimen. |
| C81951 | CYSTARCH | Starch Crystals; Starch Granules | A measurement of the starch crystals in a biological specimen. |
| C92290 | CYSTATC | Cystatin C | A measurement of the cystatin C in a biological specimen. |
| C172518 | CYSTEINE | Cysteine | A measurement of the cysteine in a biological specimen. |
| C147331 | CYSTHION | Cystathionine | A measurement of the cystathionine in a biological specimen. |
| C105441 | CYSTINE | Cystine | A measurement of the cystine in a biological specimen. |
| C74755 | CYSULFA | Sulfa Crystals; Sulfonamide Crystals | A measurement of the sulfa crystals present in a biological specimen. |
| C74756 | CYTRPHOS | Ammonium Magnesium Phosphate Crystals; Struvite Crystals; Triple Phosphate Crystals | A measurement of the triple phosphate crystals present in a biological specimen. |
| C74683 | CYTYRO | Tyrosine Crystals | A measurement of the tyrosine crystals present in a biological specimen. |
| C74757 | CYUNCLA | Unclassified Crystals | A measurement of the unclassifiable crystals present in a biological specimen. |
| C74684 | CYURIAC | Uric Acid Crystals | A measurement of the uric acid crystals (including acid urate and urate crystals) present in a biological specimen. |
| C156537 | DALA | 5-Aminolevulinic Acid; 5ALA; dALA; Delta Aminolevulinate; Delta Aminolevulinic Acid | A measurement of the delta aminolevulinic acid in a biological specimen. |
| C156538 | DALACRT | Delta Aminolevulinate/Creatinine | A relative measurement (ratio or percentage) of the delta aminolevulinate to creatinine in a biological specimen. |
| C172500 | DCA | Deoxycholate; Deoxycholic Acid | A measurement of the deoxycholate in a biological specimen. |
| C156536 | DCCARNIT | C10; Decanoylcarnitine | A measurement of the decanoylcarnitine in a biological specimen. |
| C82621 | DDIMER | D-Dimer | A measurement of the d-dimers in a biological specimen. |
| C154769 | DDNAIGAB | Anti-Double Stranded DNA IgG | A measurement of the double stranded DNA IgG antibody in a biological specimen. |
| C163428 | DDX58 | DEAD Box Protein 58; DExD/H-Box Helicase 58; Probable ATP-Dependent RNA Helicase DDX58 | A measurement of the DEAD box protein 58 in a biological specimen. |
| C172512 | DECORIN | DCN; Decorin | A measurement of the decorin in a biological specimen. |
| C45781 | DENSITY | Density | A measurement of the compactness of a biological specimen expressed in mass per unit volume. |
| C186040 | DESIPRMN | Desipramine | A measurement of the desipramine in a biological specimen. |
| C184614 | DETHPRPN | Diethylpropion | A measurement of the diethylpropion in a biological specimen. |
| C135408 | DFI | DNA Fragmentation Index | A measurement of the deoxyribonucleic acid fragmentation within the nucleated cells of a biological specimen. |
| C111190 | DGNWBC | Degenerated Leukocytes; Degenerated WBC; Degenerated White Blood Cells | A measurement of the degenerated leukocytes (leukocytes that show deterioration in form or function) in a biological specimen. |
| C74852 | DHEA | Dehydroepiandrosterone; Dehydroisoandrosterone | A measurement of the dehydroepiandrosterone hormone in a biological specimen. |
| C96629 | DHEAS | Dehydroepiandrosterone Sulfate; DHEA Sulfate; DHEA-S; sDHEA | A measurement of the sulfated Dehydroepiandrosterone in a biological specimen. |
| C101017 | DHPG | 3,4-Dihydroxyphenylglycol; 3.4 Dihydroxyphenylglycol | A measurement of the catecholamine metabolite, 3,4-Dihydroxyphenylglycol in a biological specimen. |
| C74853 | DHT | Androstanalone; Androstanolone; Dihydrotestosterone | A measurement of the dihydrotestosterone hormone in a biological specimen. |
| C74878 | DIHYDCDN | Dihydrocodeine | A measurement of the dihydrocodeine present in a biological specimen. |
| C165957 | DKK1 | Dickkopf WNT Signaling Pathway Inhibitor 1; DKK-1; SK | A measurement of the dickkopf WNT signaling pathway inhibitor 1 in a biological specimen. |
| C172519 | DMG | Dimethylglycine | A measurement of the dimethylglycine in a biological specimen. |
| C184536 | DMTNN | Dimethyltryptamine; DMT; N,N-Dimethyltryptamine | A measurement of the N,N-dimethyltryptamine in a biological specimen. |
| C135409 | DNA | Deoxyribonucleic Acid | A measurement of a targeted deoxyribonucleic acid (DNA) in a biological specimen. |
| C81973 | DNAAB | Anti-DNA Antibodies; Anti-ds-DNA Antibodies | A measurement of the anti-DNA antibodies in a biological specimen. |
| C100463 | DNASEBAB | Anti-Dnase B; DNase-B Antibody | A measurement of Dnase-B antibody in a biological specimen. |
| C174298 | DNPSEPHD | (+)-Norpseudoephedrine; Cathine; D-Norpseudoephedrine | A measurement of the D-norpseudoephedrine in a biological specimen. |
| C74610 | DOHLE | Dohle Bodies | A measurement of the Dohle bodies (blue-gray, basophilic, leukocyte inclusions located in the peripheral cytoplasm of neutrophils) in a biological specimen. |
| C103345 | DOPAC | 3,4-Dihydroxyphenylacetic Acid | A measurement of the 3,4-dihydroxyphenylacetic acid in a biological specimen. |
| C163429 | DOPAMEXR | Dopamine Excretion Rate | A measurement of the amount of dopamine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C74854 | DOPAMINE | Dopamine | A measurement of the dopamine hormone in a biological specimen. |
| C184582 | DOXMTST | Desoxymethyltestosterone | A measurement of the desoxymethyltestosterone in a biological specimen. |
| C186041 | DOXPNAOM | Doxepin and/or Metabolites | A measurement of the doxepin and/or its metabolite(s) present in a biological specimen, for an assay that can measure both doxepin and its metabolites. |
| C79443 | DPD | Deoxypyridinoline | A measurement of the deoxypyridinoline in a biological specimen. |
| C79444 | DPDCREAT | Deoxypyridinoline/Creatinine | A relative measurement (ratio or percentage) of the deoxypyridinoline to creatinine in a biological specimen. |
| C184569 | DPHNOXLT | Diphenoxylate | A measurement of the diphenoxylate in a biological specimen. |
| C184540 | DPIPANON | Dipipanone | A measurement of the dipipanone in a biological specimen. |
| C177992 | DPPIV | Dipeptidyl Peptidase-4 | A measurement of the dipeptidyl peptidase-4 in a biological specimen. |
| C184583 | DRSTNLN | Dromostanolone; Drostanolone; Medrosteron; Medrotestron; Metholone | A measurement of the drostanolone in a biological specimen. |
| C78139 | DRUGSCR | Drug Screen | An indication of the presence or absence of recreational drugs or drugs of abuse in a biological specimen. |
| C161373 | DRVTSCPD | dRVVT Screen to Confirm Pct Difference; dRVVT Screen to Confirm Percent Difference | A measurement to confirm the presence of Lupus anticoagulants, calculated as [(Screen dRVVT - Confirm dRVVT)/Screen dRVVT]x100. |
| C96696 | DRVVT | Dilute Russell's Viper Venom Time; Lupus Anticoagulant Test | A measurement of the time it takes a plasma sample to clot after adding dilute Russell's viper venom. |
| C103386 | DRVVTRT | Dilute Russell's Viper Venom Time Ratio; Lupus Anticoagulant Ratio | A relative measurement of the dilute Russell's viper venom time in a subject sample to a control sample. |
| C163430 | DRVVTSCR | DRVVT Screen to Confirm Ratio | A relative measurement (ratio) of the dilute Russell's viper venom time without the presence of excess phospholipid to the dRVVT in the presence of excess phospholipid. |
| C122114 | DSG1AB | Desmoglein 1 Antibody | A measurement of the desmoglein 1 antibody in a biological specimen. |
| C122115 | DSG3AB | Desmoglein 3 Antibody | A measurement of the desmoglein 3 antibody in a biological specimen. |
| C147333 | DSVLFXN | Desvenlafaxine; O-Desmethylvenlafaxine | A measurement of the desvenlafaxine present in a biological specimen. |
| C100441 | DTPACLR | DTPA Clearance | A measurement of the volume of serum or plasma that would be cleared of Diethylenetriamine pentaacetate (DTPA) by excretion of urine for a specified unit of time (e.g. one minute). |
| C187798 | DULOXTN | Duloxetine | A measurement of the duloxetine in a biological specimen. |
| C186042 | DXCSD11 | 11-Deoxycorticoids; 11-Deoxycorticosteroid; 11-Deoxycorticosteroids | A measurement of the total 11-deoxycorticosteroids in a biological specimen. |
| C186043 | DXCSL11 | 11-Deoxycortisol | A measurement of the 11-deoxycortisol in a biological specimen. |
| C186044 | DXCSL21 | 21-Deoxycortisol | A measurement of the 21-deoxycortisol in a biological specimen. |
| C186045 | DXCSN11 | 11-Deoxycorticosterone; 21-Hydroxyprogesterone; Cortexone; Deoxycortone; Desoxycortone | A measurement of the 11-deoxycorticosterone in a biological specimen. |
| C186046 | DXCSN21 | 21-Deoxycorticosterone | A measurement of the 21-deoxycorticosterone in a biological specimen. |
| C75372 | DZPM | Diazepam | A measurement of the diazepam present in a biological specimen. |
| C163431 | E1S | E1S; Estrone 3-Sulfate; Estrone Sulfate | A measurement of the estrone sulfate in a biological specimen. |
| C142275 | EAGLUC | EAG; Estimated Average Glucose; Glucose, Estimated; Glucose, Estimated Average | A computed estimate of the blood glucose based on the value of the glycated hemoglobin |
| C96598 | ECCENTCY | Eccentrocytes | A measurement of the eccentrocytes (erythrocytes in which the hemoglobin is localized to a particular portion of the cell, noticeable as localized staining) in a biological specimen. |
| C100422 | ECT | Ecarin Clotting Time | A measurement of the activity of thrombin inhibitors in a biological specimen based on the generation of meizothrombin. |
| C163432 | EDMAB | Endomysial Antibody; Endomysium Antibody | A measurement of the endomysial antibody in a biological specimen. |
| C147334 | EDMIGAAB | Endomysial IgA Antibody; Endomysium IgA Antibody | A measurement of the endomysial IgA antibody in a biological specimen. |
| C184644 | EDN | Eosinophil Protein-X; Eosinophil-Derived Neurotoxin; RAF3; Ribonuclease A Family Member 2 | A measurement of the eosinophil-derived neurotoxin in a biological specimen. |
| C100440 | EDTACLR | EDTA Clearance | A measurement of the volume of serum or plasma that would be cleared of Ethylenediamine tetraacetic acid (EDTA) by excretion of urine for a specified unit of time (e.g. one minute). |
| C82009 | EGF | Epidermal Growth Factor | A measurement of the epidermal growth factor in a biological specimen. |
| C112273 | EGFR | Epidermal Growth Factor Receptor; ERBB1; HER1 | A measurement of the epidermal growth factor receptor in a biological specimen. |
| C181452 | EGFRFR | Epidermal Growth Factor Receptor, Free | A measurement of the free (unbound) epidermal growth factor receptor in a biological specimen. |
| C82028 | ELA1 | Pancreatic Elastase 1 | A measurement of the pancreatic elastase 1 in a biological specimen. |
| C82029 | ELA1PMN | Pancreatic Elastase 1, Polymorphonuclear | A measurement of the polymorphonuclear pancreatic elastase 1 in a biological specimen. |
| C82026 | ELA2 | Neutrophil Elastase | A measurement of the neutrophil elastase in a biological specimen. |
| C82027 | ELA2PMN | Neutrophil Elastase, Polymorphonuclear | A measurement of the polymorphonuclear neutrophil elastase in a biological specimen. |
| C64549 | ELLIPCY | Elliptocytes | A measurement of the elliptocytes (elliptically shaped cell with blunt ends and a long axis twice the length of its short axis) in a biological specimen. |
| C184555 | EMA | Ethylamphetamine; Etilamfetamine; N-Ethylamphetamine | A measurement of the ethylamphetamine in a biological specimen. |
| C82010 | ENA78 | Epith Neutrophil-Activating Peptide 78 | A measurement of the epithelial neutrophil-activating peptide in a biological specimen. |
| C92270 | ENAAB | Anti-ENA; Extractable Nuclear Antigen Antibody | A measurement of the extractable nuclear antigen antibody in a biological specimen. |
| C172509 | ENDOSTN | Collagen Type XVIII Alpha 1 Chain; Endostatin | A measurement of the endostatin in a biological specimen. |
| C82008 | ENDOTH1 | Endothelin-1 | A measurement of the endothelin-1 in a biological specimen. |
| C187800 | ENDOTH3 | Endothelin-3; ET-3 | A measurement of the endothelin-3 in a biological specimen. |
| C82011 | ENRAGE | Extracell Newly Ident RAGE Bind Protein; S100 Calcium Binding Protein A12 | A measurement of the extracellular newly identified RAGE (receptor for advanced glycation end products) binding protein in a biological specimen. |
| C64550 | EOS | Eosinophils | A measurement of the eosinophils in a biological specimen. |
| C114216 | EOSB | Eosinophils Band Form | A measurement of the banded eosinophils in a biological specimen. |
| C114217 | EOSBLE | Eosinophils Band Form/Leukocytes | A relative measurement (ratio or percentage) of the banded eosinophils to leukocytes in a biological specimen. |
| C98720 | EOSCE | Eosinophils/Total Cells | A relative measurement (ratio or percentage) of the eosinophils to total cells in a biological specimen (for example a bone marrow specimen). |
| C96673 | EOSIM | Immature Eosinophils | A measurement of the immature eosinophils in a biological specimen. |
| C96674 | EOSIMLE | Immature Eosinophils/Leukocytes | A relative measurement (ratio or percentage) of immature eosinophils to total leukocytes in a biological specimen. |
| C64604 | EOSLE | Eosinophils/Leukocytes | A relative measurement (ratio or percentage) of the eosinophils to leukocytes in a biological specimen. |
| C84819 | EOSMM | Eosinophilic Metamyelocytes | A measurement of the eosinphilic metamyelocytes in a biological specimen. |
| C84821 | EOSMYL | Eosinophilic Myelocytes | A measurement of the eosinophilic myelocytes in a biological specimen. |
| C181449 | EOSMYLLY | Eosinophilic Myelocytes/Lymphocytes | A relative measurement (ratio or percentage) of the eosinophilic myelocytes to lymphocytes in a biological specimen (for example a bone marrow specimen). |
| C135411 | EOSNSQE | Eosinophils/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the eosinophils to non-squamous epithelial cells in a biological specimen. |
| C150840 | EOSNUCCE | Eosinophils/Nucleated Cells | A relative measurement (ratio or percentage) of eosinophils to nucleated cells in a biological specimen. |
| C165958 | EOSPSD | Pseudo-Eosinophils | A measurement of the pseudo-eosinophils in a biological specimen. |
| C165959 | EOSPSDLE | Pseudo-Eosinophils/Leukocytes | A relative measurement (ratio or percentage) of the pseudo-eosinophils to the leukocytes in a biological specimen. |
| C135412 | EOSSG | Eosinophils, Segmented | A measurement of the segmented eosinophils in a biological specimen. |
| C81952 | EOTAXIN1 | Chemokine Ligand 11; Eotaxin-1 | A measurement of the eotaxin-1 in a biological specimen. |
| C81953 | EOTAXIN2 | Chemokine Ligand 24; Eotaxin-2 | A measurement of the eotaxin-2 in a biological specimen. |
| C81954 | EOTAXIN3 | CCL26; Chemokine (C-C Motif) Ligand 26; Chemokine Ligand 26; Eotaxin-3 | A measurement of the eotaxin-3 in a biological specimen. |
| C174296 | EPHD | Ephedrine | A measurement of the ephedrine in a biological specimen. |
| C64605 | EPIC | Epithelial Cells | A measurement of the epithelial cells in a biological specimen. |
| C130161 | EPICCE | Epithelial Cells/Total Cells | A relative measurement (ratio or percentage) of the epithelial cells to total cells in a biological specimen. |
| C187801 | EPICCLMP | Epithelial Cell Clumps | A measurement of the epithelial cell clumps in a biological specimen. |
| C79445 | EPIN | Adrenaline; Epinephrine | A measurement of the epinephrine hormone in a biological specimen. |
| C163433 | EPINEXR | Epinephrine Excretion Rate | A measurement of the amount of epinephrine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C135413 | EPINSQCE | Non-Squamous Epithelial Cells | A measurement of the non-squamous epithelial cells in a biological specimen. |
| C135414 | EPINSQE | Epi Cells/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the epithelial cells to non-squamous epithelial cells in a biological specimen. |
| C170595 | EPIRCE | Renal Epithelial Cells | A measurement of the renal epithelial cells in a biological specimen. |
| C74698 | EPIROCE | Round Epithelial Cells | A measurement of the round epithelial cells present in a biological specimen. |
| C132366 | EPISCECE | Squamous Epithelial Cells/Total Cells | A relative measurement (ratio or percentage) of the squamous epithelial cells to total cells in a biological specimen. |
| C74773 | EPISQCE | Squamous Cells; Squamous Epithelial Cells | A measurement of the squamous epithelial cells present in a biological specimen. |
| C74774 | EPISQTCE | Squamous Transitional Epithelial Cells | A measurement of the squamous transitional epithelial cells present in a biological specimen. |
| C92251 | EPITCE | Transitional Epithelial Cells | A measurement of the transitional epithelial cells present in a biological specimen. |
| C74775 | EPITUCE | Renal Tubular Epithelial Cells; Tubular Epithelial Cells | A measurement of the tubular epithelial cells present in a biological specimen. |
| C74855 | EPO | Erythropoietin; Hematopoietin | A measurement of the erythropoietin hormone in a biological specimen. |
| C163434 | EPSTI1 | BRESI1; Epithelial Stromal Interaction Protein 1 | A measurement of the epithelial stromal interaction protein 1 in a biological specimen. |
| C154719 | ERCECE | Erythroid Cells/Total Cells | A relative measurement (ratio or percentage) of the erythroid cells to total cells in a biological specimen. |
| C135415 | ERCEMIDX | Erythroid Maturation Index | A relative measurement (ratio) of the sum of erythroid maturation phase cells (pool) to the sum of erythroid proliferative phase cells (pool) in a biological specimen. |
| C135416 | ERCEMPOL | Erythroid Maturation Pool | A measurement of the erythroid maturation phase cells (polychromatic rubricytes, normochromic rubricytes, and metarubricytes) in a biological specimen. |
| C154720 | ERCENC | Erythroid Cells/Nucleated Cells | A relative measurement (ratio or percentage) of the erythroid cells to total nucleated cells in a biological specimen. |
| C135417 | ERCEPIDX | Erythroid Proliferation Index | A relative measurement (ratio) of the sum of erythroid proliferative phase cells (pool) to the sum of erythroid maturation phase cells (pool) in a biological specimen. |
| C135418 | ERCEPPOL | Erythroid Proliferation Pool | A measurement of the erythroid proliferative phase cells (rubriblasts, prorubricytes, and basophilic rubricytes) in a biological specimen. |
| C186047 | ERFE | Erythroferrone | A measurement of the erythroferrone in a biological specimen. |
| C187802 | ERPCE | Erythroid Precursor Cells; Erythroid Precursors | A measurement of the erythroid precursors in a biological specimen. |
| C187803 | ERPCECE | Erythroid Precursor Cells/Total Cells; Erythroid Precursors/Total Cells | A relative measurement (ratio or percentage) of the erythroid precursors to total cells in a biological specimen. |
| C187804 | ESCTLPRM | Escitalopram | A measurement of the escitalopram in a biological specimen. |
| C154736 | ESELECT | E-Selectin | A measurement of total E-selectin in a biological specimen. |
| C119273 | ESELS | sE-selectin; Soluble E-Selectin | A measurement of the soluble E-Selectin in a biological specimen. |
| C74611 | ESR | Biernacki Reaction; Erythrocyte Sedimentation Rate | The distance (e.g. millimeters) that red blood cells settle in unclotted blood over a specified unit of time (e.g. one hour). |
| C184615 | ESTAZLM | Estazolam | A measurement of the estazolam in a biological specimen. |
| C150842 | ESTFR | Estradiol, Free | A measurement of the unbound estradiol in a biological specimen. |
| C150843 | ESTFREST | Estradiol, Free/Estradiol | A relative measurement (ratio or percentage) of unbound estradiol to total estradiol in a biological specimen. |
| C112274 | ESTRCPT | ER; ESR; Estrogen Receptor; Oestrogen Receptor | A measurement of estrogen receptor protein in a biological specimen. |
| C74782 | ESTRDIOL | Estradiol; Oestradiol | A measurement of the estradiol in a biological specimen. |
| C74856 | ESTRIOL | Estriol; Oestriol | A measurement of the estriol hormone in a biological specimen. |
| C81963 | ESTRIOLF | Estriol, Free; Unconjugated Estriol | A measurement of the free estriol in a biological specimen. |
| C147335 | ESTROGEN | Estrogen; Oestrogen | A measurement of the estrogen hormone in a biological specimen. |
| C74857 | ESTRONE | Estrone; Oestrone | A measurement of the estrone hormone in a biological specimen. |
| C170584 | ETG | Ethyl Glucuronide | A measurement of the ethyl glucuronide in a biological specimen. |
| C170583 | ETGETS | Ethyl Glucuronide Ethyl Sulfate | A measurement of the ethyl glucuronide and/or ethyl sulfate in a biological specimen. |
| C74693 | ETHANOL | Alcohol; Ethanol | A measurement of the ethanol present in a biological specimen. |
| C184616 | ETHCHVNL | Ethchlorvynol | A measurement of the ethchlorvynol in a biological specimen. |
| C184584 | ETHESTNL | Ethylestrenol | A measurement of the ethylestrenol in a biological specimen. |
| C184617 | ETHNMATE | Ethinamate | A measurement of the ethinamate in a biological specimen. |
| C102266 | ETP | Endogenous Thrombin Potential | A measurement of the total concentration of thrombin generated in the presence of a substrate in a plasma or blood sample. |
| C102263 | ETPAUC | Endogenous Thrombin Potential Area Under Curve; ETP Area Under Curve | A measurement of the area under the thrombin generation curve. |
| C102264 | ETPLT | Endogenous Thrombin Potential Lag Time; ETP Lag Time | A measurement of time from the start of the thrombin generation test to the point where a predetermined amount of thrombin is generated. |
| C102265 | ETPLTR | Endogenous Thrombin Potential Lag Time Relative; ETP Lag Time Relative | A relative measurement (ratio or percentage) of time from the start of the thrombin generation test to the point where a predetermined amount of thrombin is generated. |
| C102267 | ETPPH | Endogenous Thrombin Potential Peak Height; ETP Peak Height | A measurement of the maximum concentration of thrombin generated during a thrombin generation test. |
| C102268 | ETPPHR | Endogenous Thrombin Potential Peak Height Relative; ETP Peak Height Relative | A relative (ratio or percentage) of the maximum concentration of thrombin generated during a thrombin generation test. |
| C102269 | ETPTP | Endogenous Thrombin Potential Time to Peak; ETP Time to Peak | A measurement of the time it takes to generate the maximum concentration of thrombin. |
| C102270 | ETPTPR | Endogenous Thrombin Potential Time to Peak Relative; ETP Time to Peak Relative | A relative (ratio or percentage) measurement of the time it takes to generate the maximum concentration of thrombin. |
| C170585 | ETS | Ethyl Sulfate | A measurement of the ethyl sulfate in a biological specimen. |
| C176304 | EUDCA | Epimerized Ursodeoxycholate; Epimerized Ursodeoxycholic Acid | A measurement of the epimerized ursodeoxycholate in a biological specimen. |
| C184640 | EZOGABIN | Ezogabine | A measurement of the ezogabine in a biological specimen. |
| C82012 | FABP1 | FABP1; Fatty Acid Binding Protein 1; L-FABP; L-Type Fatty Acid-Binding Protein; Liver Fatty Acid-Binding Protein | A measurement of the fatty acid binding protein 1 in a biological specimen. |
| C106521 | FABP3 | Fatty Acid Binding Protein 3 | A measurement of the fatty acid binding protein 3 in a biological specimen. |
| C96626 | FACTII | Factor II; Prothrombin | A measurement of the coagulation factor II in a biological specimen. |
| C81959 | FACTIII | Factor III; Tissue Factor, CD142 | A measurement of the coagulation factor III in a biological specimen. |
| C98725 | FACTIX | Christmas Factor; Factor IX | A measurement of the coagulation factor IX in a biological specimen. |
| C103395 | FACTIXA | Christmas Factor Activity; Factor IX Activity | A measurement of the biological activity of coagulation factor IX in a biological specimen. |
| C98726 | FACTV | Factor V; Labile Factor | A measurement of the coagulation factor V in a biological specimen. |
| C103396 | FACTVA | Factor V Activity; Labile Factor Activity | A measurement of the biological activity of coagulation factor V in a biological specimen. |
| C81960 | FACTVII | Factor VII; Proconvertin; Stable Factor | A measurement of the coagulation factor VII in a biological specimen. |
| C103397 | FACTVIIA | Factor VII Activity; Proconvertin Activity; Stable Factor Activity | A measurement of the biological activity of coagulation factor VII in a biological specimen. |
| C81961 | FACTVIII | Anti-hemophilic Factor; Factor VIII | A measurement of the coagulation factor VIII in a biological specimen. |
| C102271 | FACTVL | Factor V Leiden | A measurement of the coagulation factor V Leiden in a biological specimen. |
| C98799 | FACTVW | von Willebrand Factor; von Willebrand Factor Antigen | A measurement of the von Willebrand coagulation factor in a biological specimen. |
| C122117 | FACTVWA | von Willebrand Factor Activity | A measurement of the biological activity of von Willebrand coagulation factor in a biological specimen. |
| C147336 | FACTVWMU | von Willebrand Factor Multimers | A measurement of the von Willebrand Factor multimers (an aggregate of multiple von Willebrand factor antigens that are held together with non-covalent bonds) in a biological specimen. |
| C98727 | FACTX | Factor X | A measurement of the coagulation factor X in a biological specimen. |
| C122118 | FACTXA | Factor X Activity | A measurement of the biological activity of coagulation factor X in a biological specimen. |
| C163435 | FACTXI | Factor XI | A measurement of the factor XI in a biological specimen. |
| C163436 | FACTXIA | Factor XI Activity | A measurement of the biological activity of coagulation factor XI in a biological specimen. |
| C163437 | FACTXII | Factor XII | A measurement of the factor XII in a biological specimen. |
| C163438 | FACTXIIA | Factor XII Activity | A measurement of the biological activity of coagulation factor XII in a biological specimen. |
| C112277 | FACTXIII | Factor XIII; Fibrin Stabilizing Factor | A measurement of the coagulation factor XIII in a biological specimen. |
| C102272 | FACTXIV | Autoprothrombin IIA; Factor XIV; Protein C; Protein C Antigen | A measurement of the coagulation factor XIV in a biological specimen. |
| C105442 | FACTXIVA | Factor XIV Activity; Protein C Activity; Protein C Function | A measurement of the biological activity of coagulation factor XIV in a biological specimen. |
| C124341 | FAI | Free Androgen Index | A measurement of the androgen status in a biological specimen. This is calculated by a mathematical formula that takes into account the total testosterone level, sex hormone binding globulin, and a constant. |
| C165960 | FAS | ALPS1A; APT1; CD95; Fas Cell Surface Death Receptor; FAS1; FASTM; TNF Receptor Superfamily Member 6; TNFRSF6 | A measurement of the Fas cell surface death receptor in a biological specimen. |
| C96648 | FAT | Fat | A measurement of the fat in a biological specimen. |
| C80200 | FATACFR | Free Fatty Acid; Non-Esterified Fatty Acid, Free | A measurement of the total non-esterified fatty acids in a biological specimen. |
| C80206 | FATACFRS | Free Fatty Acid, Saturated; Non-esterified Fatty Acid, Saturated | A measurement of the saturated non-esterified fatty acids in a biological specimen. |
| C80209 | FATACFRU | Free Fatty Acid, Unsaturated; Non-esterified Fatty Acid, Unsaturated | A measurement of the unsaturated non-esterified fatty acids in a biological specimen. |
| C147337 | FATACVLC | Fatty Acids, Very Long Chain | A measurement of the very long chain fatty acids (containing 22 or more carbon atoms) in a biological specimen. |
| C81947 | FATBODOV | Fat Bodies, Oval | A measurement of the oval-shaped fat bodies, usually renal proximal tubular cells with lipid aggregates in the cytoplasm, in a biological specimen. |
| C98728 | FATDROP | Fat Droplet | A measurement of the triglyceride aggregates within a biological specimen. |
| C156516 | FATLVIDX | Fatty Liver Index; FLI | A calculation that indicates the likely presence of fatty liver disease, taking into account waist circumference, body mass index, triglyceride concentrations, and gamma-glutamyltransferase activity. (Bedogni G, Bellentani S, Miglioli L, Masutti F, Passalacqua M, Castiglione A, Tiribelli C. The Fatty Liver Index: a simple and accurate predictor of hepatic steatosis in the general population. BMC Gastroenterol. 2006 Nov 2;6:33.) |
| C187806 | FATTOTSD | Fat/Total Solids | A relative measurement (ratio or percentage) of the fat to total solid material in a biological specimen (for example a stool specimen). |
| C172507 | FBNCTCE | Fibronectin, Cellular; Insoluble Fibronectin | A measurement of the cellular fibronectin in a biological specimen. |
| C92786 | FBNCTFT | Fibronectin, Fetal | A measurement of the fetal isoform of fibronectin in a biological specimen |
| C177951 | FBNCTMFT | Fibronectin, Maternal + Fetal | A measurement of the maternal plasma fibronectin and fetal fibronectin in a biological specimen. |
| C172508 | FBNCTPL | Fibronectin, Plasma; Soluble Fibronectin | A measurement of the plasma fibronectin in a biological specimen. |
| C105443 | FBRTST | FibroSURE Score; FibroTest Score | A biomarker test that measures liver pathology through the assessment of a six-parameter blood test (for Alpha-2-macroglobulin, Haptoglobin, Apolipoprotein A1, Gamma-glutamyl transpeptidase (GGT), Total bilirubin, and Alanine aminotransferase (ALT)), taking into account the age and gender of the patient. |
| C154752 | FCT8INH | Factor VIII Inhibitor | A measurement of the factor VIII Inhibitor in a biological specimen. |
| C103398 | FCTVIIAA | Factor VIIa Activity | A measurement of the biological activity of coagulation factor VIIa in a biological specimen. |
| C103399 | FCTVIIIA | Anti-hemophilic Factor Activity; Factor VIII Activity; Factor VIII:C | A measurement of the biological activity of coagulation factor VIII in a biological specimen. |
| C174313 | FCTXIIIA | Factor XIII Activity | A measurement of the biological activity of coagulation factor XIII in a biological specimen. |
| C82013 | FDP | Fibrin Degradation Products | A measurement of the fibrin degradation products in a biological specimen. |
| C114219 | FECA | Fractional Calcium Excretion | A measurement of the fractional excretion of calcium that is computed based upon the concentrations of calcium and creatinine in both blood and urine. |
| C114220 | FECL | Fractional Chloride Excretion | A measurement of the fractional excretion of chloride that is computed based upon the concentrations of chloride and creatinine in both blood and urine. |
| C114222 | FEK | Fractional Potassium Excretion | A measurement of the fractional excretion of potassium that is computed based upon the concentrations of potassium and creatinine in both blood and urine. |
| C122119 | FEMG | Fractional Magnesium Excretion | A measurement of the fractional excretion of magnesium that is computed based upon the concentrations of magnesium and creatinine in both blood and urine. |
| C184525 | FEN3M | 3-Methylfentanyl | A measurement of the 3-methylfentanyl in a biological specimen. |
| C107435 | FENA | Fractional Sodium Excretion | A measurement of the fractional excretion of sodium that is computed based upon the concentrations of sodium and creatinine in both blood and urine. |
| C184528 | FENACE | Acetyl Fentanyl; Acetylfentanyl | A measurement of the acetylfentanyl in a biological specimen. |
| C184537 | FENAM | Alpha-Methylfentanyl | A measurement of the alpha-methylfentanyl in a biological specimen. |
| C184530 | FENBOHT | Beta-Hydroxythiofentanyl | A measurement of the beta-hydroxythiofentanyl in a biological specimen. |
| C184533 | FENBUT | Butyrfentanyl; Butyryl Fentanyl; Butyrylfentanyl | A measurement of the butyrylfentanyl in a biological specimen. |
| C184618 | FENCMFMN | Fencamfamin; Fencamfamine | A measurement of the fencamfamin in a biological specimen. |
| C184619 | FENFLRMN | Fenfluramine | A measurement of the fenfluramine in a biological specimen. |
| C184541 | FENFUR | Furanyl Fentanyl; Furanylfentanyl | A measurement of the furanylfentanyl in a biological specimen. |
| C184558 | FENPF | Para-Fluorofentanyl | A measurement of the para-fluorofentanyl in a biological specimen. |
| C184620 | FENPRPRX | Fenproporex | A measurement of the fenproporex in a biological specimen. |
| C147338 | FENTANYL | Fentanyl | A measurement of the fentanyl in a biological specimen. |
| C184607 | FENVAL | Valeryl Fentanyl; Valerylfentanyl | A measurement of the valerylfentanyl in a biological specimen. |
| C147339 | FEP | Erythrocyte Protoporphyrin, Free | A measurement of the free erythrocyte protoporphyrin (zinc bound plus unbound protoporphyrin) in a biological specimen. |
| C114221 | FEPI | Fractional Inorganic Phosphate Excretion; Fractional Phosphorus Excretion | A measurement of the fractional excretion of phosphorus that is computed based upon the concentrations of phosphorus and creatinine in both blood and urine. |
| C74737 | FERRITIN | Ferritin | A measurement of the ferritin in a biological specimen. |
| C154727 | FGF19 | FGF 19; Fibroblast Growth Factor 19 | A measurement of the fibroblast growth factor 19 in a biological specimen. |
| C112280 | FGF21 | FGF 21; Fibroblast Growth Factor 21 | A measurement of the fibroblast growth factor 21 in a biological specimen. |
| C96650 | FGF23 | Fibroblast Growth Factor 23; Phosphatonin | A measurement of the total fibroblast growth factor 23 in a biological specimen. |
| C135419 | FGF23C | Fibroblast Growth Factor 23, C-Terminal | A measurement of the C-terminal fibroblast growth factor 23 in a biological specimen. |
| C135420 | FGF23I | Fibroblast Growth Factor 23, Intact | A measurement of the intact fibroblast growth factor 23 in a biological specimen. |
| C130162 | FGF9 | FGF 9; Fibroblast Growth Factor 9 | A measurement of the fibroblast growth factor 9 in a biological specimen. |
| C82014 | FGFBF | FGF2; Fibroblast Growth Factor Basic Form | A measurement of the basic form of fibroblast growth factor in a biological specimen. |
| C189498 | FIBMONO | Fibrin Monomer; Soluble Fibrin Monomer | A measurement of the fibrin monomer in a biological specimen. |
| C64606 | FIBRINO | Fibrinogen; Fibrinogen Antigen | A measurement of the total fibrinogen (functional and non-functional) in a biological specimen. |
| C139075 | FIBRINOF | Fibrinogen, Functional | A measurement of the functional fibrinogen (fibrinogen that is capable of being converted to fibrin) in a biological specimen. |
| C38082 | FIO2 | Fraction of Inspired Oxygen | A measurement of the volumetric fraction of oxygen in the inhaled gas. |
| C170588 | FIXAAC | Factor IX Activity Actual/Control; Factor IX Activity Actual/Factor IX Activity Control; Factor IX Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of factor IX dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C139081 | FLNTRZPM | Flunitrazepam | A measurement of the flunitrazepam present in a biological specimen. |
| C75373 | FLRZPM | Flurazepam | A measurement of the flurazepam present in a biological specimen. |
| C174307 | FLT3 | CD135; FMS-like Receptor Tyrosine Kinase 3 | A measurement of the FMS-like receptor tyrosine kinase 3 in a biological specimen. |
| C174306 | FLT3L | FMS-like Tyrosine Kinase 3 Ligand | A measurement of the FMS-like tyrosine kinase 3 ligand in a biological specimen. |
| C171508 | FLUDOUTE | Fluid Output, Estimated | An estimate of the total volume of fluid discharged over a set period of time. |
| C171455 | FLUIDOUT | Fluid Output | A measurement of the total volume of fluid discharged over a set period of time. |
| C122120 | FLUORIDE | Fluoride | A measurement of the fluoride in a biological specimen. |
| C158219 | FLUOXTN | Fluoxetine | A measurement of the fluoxetine drug present in a biological specimen. |
| C187816 | FLUOXTNN | Norfluoxetine | A measurement of the norfluoxetine in a biological specimen. |
| C177980 | FLUPHZN | Fluphenazine | A measurement of the fluphenazine in a biological specimen. |
| C147340 | FLUVOXAM | Fluvoxamine | A measurement of the fluvoxamine present in a biological specimen. |
| C184585 | FLXMSTRN | Fluoxymesterone | A measurement of the fluoxymesterone in a biological specimen. |
| C186048 | FNZPMAOM | Flunitrazepam and/or Metabolites | A measurement of the flunitrazepam and/or its metabolite(s) present in a biological specimen, for an assay that can measure both flunitrazepam and its metabolites. |
| C132367 | FOLHMRNA | Folate Hydrolase mRNA | A measurement of the folate hydrolase mRNA in a biological specimen. |
| C147341 | FPP | Protoporphyrin, Free | A measurement of the free protoporphyrin (unbound to iron in hemoglobin) in a biological specimen. |
| C161349 | FRFEABS | Fractional Iron Absorption | A relative measurement (ratio or percentage) of the iron absorbed into tissue or cells to the total available iron. |
| C186049 | FRNG | Glycated Ferritin | A measurement of the glycated ferritin in a biological specimen. |
| C186050 | FRNGFRN | Glycated Ferritin/Ferritin | A relative measurement (ratio or percentage) of the glycated ferritin to total ferritin in a biological specimen. |
| C172521 | FRTNHC | Apoferritin; Ferritin Heavy Chain; FTH; FTH1 | A measurement of the ferritin heavy chain in a biological specimen. |
| C172522 | FRTNLC | Ferritin Light Chain; FTL; L Apoferritin | A measurement of the ferritin light chain in a biological specimen. |
| C74678 | FRUCT | Fructosamine; Glycated Serum Protein | A measurement of the fructosamine in a biological specimen. |
| C147342 | FRUCTOSE | Fructose | A measurement of the fructose in a biological specimen. |
| C161350 | FRUMCRTP | Fructosamine Corrected for Total Protein | A measurement of fructosamine, which has been corrected for total protein, in a biological specimen. |
| C186051 | FRZPMAOM | Flurazepam and/or Metabolites | A measurement of the flurazepam and/or its metabolite(s) present in a biological specimen, for an assay that can measure both flurazepam and its metabolites. |
| C74783 | FSH | Follicle Stimulating Hormone | A measurement of the follicle stimulating hormone (FSH) in a biological specimen. |
| C154813 | FUNGI | Fungi; Fungus | A measurement of the fungi in a biological specimen. |
| C147343 | FUNGIFIL | Fungi, Filamentous | A measurement of the filamentous fungi in a biological specimen. |
| C147344 | FUNGYLK | Fungi, Yeast-Like | A measurement of the yeast-like fungi in a biological specimen. |
| C184586 | FURAZBL | Furazabol | A measurement of the furazabol in a biological specimen. |
| C170587 | FVAAC | Factor V Activity Actual/Control; Factor V Activity Actual/Factor V Activity Control; Factor V Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of factor V dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C170589 | FVIIAAC | Factor VII Activity Actual/Control; Factor VII Activity Actual/Factor VII Activity Control; Factor VII Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of factor VII dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C147345 | FVIIIAAC | Factor VIII Activity Actual/Control; Factor VIII Activity Actual/Factor VIII Activity Control; Factor VIII Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of factor VIII dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C170586 | FXAAC | Factor X Activity Actual/Control; Factor X Activity Actual/Factor X Activity Control; Factor X Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of factor X dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C170590 | FXAC | Factor X Actual/Control; Factor X Actual/Normal | A relative measurement (ratio or percentage) of the factor X in a subject's specimen when compared to a control specimen. |
| C147346 | FXIVAAC | Factor XIV Activity Actual/Control; Factor XIV Activity Actual/Factor XIV Activity Control; Factor XIV Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of factor XIV dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C170594 | FXIVAC | Factor XIV Actual/Control; Protein C Actual/Control | A relative measurement (ratio or percentage) of the factor XIV in a subject's specimen when compared to a control specimen. |
| C80184 | G6PD | Glucose-6-Phosphate Dehydrogenase | A measurement of the glucose-6-phosphate dehydrogenase in a biological specimen. |
| C139065 | G6PDA | Glucose-6-Phosphate Dehydrogenase Act | A measurement of the biological activity of glucose-6-phosphate dehydrogenase in a biological specimen. |
| C132368 | G6PDRBC | G6PD-Deficient Erythrocytes | A measurement of the glucose-6-phosphate dehydrogenase deficient erythrocytes in a biological specimen. |
| C132369 | G6PDRBRB | G6PD-Deficient Erythrocytes/Erythrocytes | A relative measurement (ratio or percentage) of G6PD-deficient erythrocytes to total erythrocytes in a biological specimen. |
| C189502 | GAA | Acid Alpha-Glucosidase; Acid Maltase; Alpha-1,4-glucosidase | A measurement of the acid alpha-glucosidase in a biological specimen. |
| C82015 | GAD1 | Glutamic Acid Decarboxylase 1; Glutamic Acid Decarboxylase 67 | A measurement of the glutamic acid decarboxylase 1 in a biological specimen. |
| C82016 | GAD2 | Glutamic Acid Decarboxylase 2; Glutamic Acid Decarboxylase 65 | A measurement of the glutamic acid decarboxylase 2 in a biological specimen. |
| C82017 | GAD2AB | Glutamic Acid Decarboxylase 2 Antibody; Glutamic Acid Decarboxylase 65 Antibody | A measurement of the glutamic acid decarboxylase 2 antibody in a biological specimen. |
| C96653 | GADAB | GAD Antibody; Glutamic Acid Decarboxylase Antibody | A measurement of the glutamic acid decarboxylase antibody in a biological specimen. |
| C81308 | GAL | Galactose | A measurement of the galactose in a biological specimen. |
| C186052 | GAL1PHOS | Galactose-1-Phosphate | A measurement of the galactose-1-phosphate in a biological specimen. |
| C81251 | GAL1PUT | G1PUT; Galactose 1 Phosphate Uridyl Transferase; Galactose-1-Phos Uridylyltransferase; Galactose-1-Phosphate Uridylyltransferase; GALT | A measurement of the galactose-1-phosphate uridyltransferase in a biological specimen. |
| C80182 | GALANIN | Galanin | A measurement of the galanin in a biological specimen. |
| C163439 | GALM | Galactose Mutarotase | A measurement of the galactose mutarotase in a biological specimen. |
| C154766 | GAMBTAC | GABA; Gamma-aminobutyrate; Gamma-Aminobutyric Acid | A measurement of the gamma-aminobutyric acid in a biological specimen. |
| C184524 | GAPDH | GAPDH; Glyceraldehyde 3 Phosphate Dehydrogenase; Glyceraldehyde-3-Phosphate Dehydrogenase | A measurement of the glyceraldehyde-3-phosphate dehydrogenase in a biological specimen. |
| C74858 | GASTRIN | Gastrin | A measurement of the gastrin hormone in a biological specimen. |
| C116211 | GATCPHRL | Gamma Tocopherol | A measurement of the gamma tocopherol in a biological specimen. |
| C184520 | GBA | Beta-Glucocerebrosidase; GBA; Glucocerebrosidase Beta; Glucosylceramidase; Glucosylceramidase Beta | A measurement of the glucosylceramidase beta in a biological specimen. |
| C163440 | GBP1 | Guanylate Binding Protein 1 | A measurement of the guanylate binding protein 1 in a biological specimen. |
| C163441 | GBP2 | Guanylate Binding Protein 2 | A measurement of the guanylate binding protein 2 in a biological specimen. |
| C176305 | GCDCA | Glycochenodeoxycholate; Glycochenodeoxycholic Acid | A measurement of the glycochenodeoxycholate in a biological specimen. |
| C176299 | GCHT | Cholylglycine; Glycocholate; Glycocholic Acid | A measurement of the glycocholate in a biological specimen. |
| C82018 | GCSF | Granulocyte Colony Stimulating Factor | A measurement of the granulocyte colony stimulating factor in a biological specimen. |
| C150845 | GDA | Guanase; Guanine Aminohydrolase; Guanine Deaminase | A measurement of the guanine deaminase in a biological specimen. |
| C135422 | GDF11 | BMP-11; Bone Morphogenetic Protein 11; Growth Differentiation Factor 11 | A measurement of the growth differentiation factor 11 in a biological specimen. |
| C181406 | GDF15 | GDF-15; Growth Differentiation Factor 15; Macrophage Inhibitory Cytokine-1; MIC-1 | A measurement of the growth differentiation factor 15 in a biological specimen. |
| C135423 | GDF8 | Growth Differentiation Factor 8; Myostatin | A measurement of the growth differentiation factor 8 in a biological specimen. |
| C165961 | GDIGA1 | Galactose-Deficient IgA1; Gd-IgA1 | A measurement of the galactose-deficient IgA1 in a biological specimen. |
| C124342 | GEC | Galactose Elimination Capacity | A liver function test that measures galactose elimination capacity in a biological specimen. |
| C189528 | GFAP | Glial Fibrillary Acidic Protein | A measurement of the glial fibrillary acidic protein in a biological specimen. |
| C90505 | GFR | Glomerular Filtration Rate | A kidney function test that measures the fluid volume that is filtered from the kidney glomeruli to the Bowman's capsule per unit of time. |
| C98734 | GFRBSA | Glomerular Filtration Rate Adj for BSA | A measurement of the glomerular filtration rate adjusted for body surface area. |
| C100450 | GFRBSB2M | GFR from B-2 Microglobulin Adj for BSA | A measurement of the glomerular filtration rate (GFR) based on the clearance of beta-2 microglobulin after adjusting it for the body surface area. |
| C100449 | GFRBSBTP | GFR from Beta-Trace Protein Adj for BSA | A measurement of the glomerular filtration rate (GFR) based on the clearance of beta-trace protein after adjusting it for the body surface area. |
| C127614 | GFRBSCCC | GFR from Cystatin C and Creat Adj BSA | An estimation of the glomerular filtration rate adjusted for body surface area based on cystatin C and creatinine. |
| C98735 | GFRBSCRT | GFR from Creatinine Adjusted for BSA | An estimation of the glomerular filtration rate adjusted for body surface area based on creatinine. |
| C163442 | GFRBSCU | GFR from Creat and UreaN Adj BSA; GFR from Creatinine and Urea Nitrogen Adjusted for BSA | An estimation of the glomerular filtration rate adjusted for body surface area based on creatinine and urea nitrogen. |
| C163443 | GFRBSCUA | GFR from Creat,UreaN,Alb Adj BSA; GFR from Creatinine, Urea Nitrogen and Albumin Adjusted for BSA | An estimation of the glomerular filtration rate adjusted for body surface area based on creatinine, urea nitrogen, and albumin. |
| C98736 | GFRBSCYC | GFR from Cystatin C Adjusted for BSA | An estimation of the glomerular filtration rate adjusted for body surface area based on cystatin C. |
| C110935 | GFRE | Glomerular Filtration Rate, Estimated | A kidney function test that estimates the fluid volume that is filtered from the kidney glomeruli to the Bowman's capsule per unit of time. |
| C64847 | GGT | Gamma Glutamyl Transferase | A measurement of the gamma glutamyl transferase in a biological specimen. |
| C79446 | GGTCREAT | Gamma Glutamyl Transferase/Creatinine | A relative measurement (ratio or percentage) of the gamma glutamyl transferase to creatinine in a biological specimen. |
| C165962 | GGTEXR | Gamma Glutamyl Transferase Excretion Rate | A measurement of the amount of gamma glutamyl transferase being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C75357 | GHB | 4-Hydroxybutanoic Acid; Gamma-Hydroxybutyrate; Gamma-Hydroxybutyric Acid | A measurement of the gamma-hydroxybutyrate in a biological specimen. |
| C163444 | GHBP | GH Binding Protein; Growth Hormone Binding Protein; Somatotropin Receptor | A measurement of the growth hormone binding protein in a biological specimen. |
| C112286 | GHRELIN | Ghrelin; Growth Hormone Secretagogue Receptor Ligand; Motilin-related Peptide; Total Ghrelin | A measurement of total ghrelin in a biological specimen. |
| C112219 | GHRELINA | Active Ghrelin | A measurement of active ghrelin in a biological specimen. |
| C106537 | GIPI | Glucose-dep Insulinotropic Pep, Intact; Intact Gastric Inhibitory Polypeptide; Intact GIP; Intact Glucose-dependent Insulinotropic Peptide | A measurement of the intact (containing amino acids 1-42) glucose-dependent insulinotropic peptide in a biological specimen. |
| C184522 | GL1 | GL1; Glucocerebroside; Glucosylceramide | A measurement of the glucosylceramide in a biological specimen. |
| C142276 | GLBCREAT | Globulin/Creatinine | A relative measurement (ratio or percentage) of the globulin to creatinine in a biological specimen. |
| C176308 | GLCHT | Glycolithocholate; Glycolithocholic Acid | A measurement of the glycolithocholate in a biological specimen. |
| C172493 | GLCTN3 | Galactose-Specific Lectin 3; Galectin-3; GALIG; MAC-2 | A measurement of the galectin-3 in a biological specimen. |
| C186053 | GLCTN3BP | Galectin-3 Binding Protein; LGALS3BP; M2BP; Mac-2 Binding Protein | A measurement of the galectin-3 binding protein in a biological specimen. |
| C147347 | GLDAB | Gliadin Antibody | A measurement of the total gliadin antibodies in a biological specimen. |
| C79448 | GLDH | Glutamate Dehydrogenase | A measurement of the glutamate dehydrogenase in a biological specimen. |
| C147348 | GLDIGAAB | Gliadin IgA Antibody | A measurement of the gliadin IgA antibody in a biological specimen. |
| C147349 | GLDIGGAB | Gliadin IgG Antibody | A measurement of the gliadin IgG antibody in a biological specimen. |
| C122121 | GLN | Glutamine | A measurement of the glutamine in a biological specimen. |
| C163445 | GLOBA | Alpha Globulin | A measurement of the total alpha globulins in a biological specimen. |
| C92252 | GLOBA1 | A1-Globulin; Alpha-1 Globulin | A measurement of the proteins contributing to the alpha 1 fraction in a biological specimen. |
| C92253 | GLOBA1PT | Alpha-1 Globulin/Total Protein | A relative measurement (ratio or percentage) of alpha-1-fraction proteins to total proteins in a biological specimen. |
| C92254 | GLOBA2 | A2-Globulin; Alpha-2 Globulin | A measurement of the proteins contributing to the alpha 2 fraction in a biological specimen. |
| C92255 | GLOBA2PT | Alpha-2 Globulin/Total Protein | A relative measurement (ratio or percentage) of alpha-2-fraction proteins to total proteins in a biological specimen. |
| C92256 | GLOBB | Beta Globulin | A measurement of the proteins contributing to the beta fraction in a biological specimen. |
| C119274 | GLOBB1 | Beta-1 Globulin | A measurement of the beta-1 globulin in a biological specimen. |
| C142277 | GLOBB1BP | Beta-1 Globulin/Beta Protein | A relative measurement (ratio or percentage) of the beta-1-fraction proteins to the total beta protein fraction in a biological specimen. |
| C119275 | GLOBB1PT | Beta-1 Globulin/Total Protein | A relative measurement (ratio or percentage) of beta-1-fraction proteins to total proteins in a biological specimen. |
| C119276 | GLOBB2 | Beta-2 Globulin | A measurement of the beta-2 globulin in a biological specimen. |
| C119277 | GLOBB2PT | Beta-2 Globulin/Total Protein | A relative measurement (ratio or percentage) of beta-2-fraction proteins to total proteins in a biological specimen. |
| C92294 | GLOBBPT | Beta Globulin/Total Protein | A relative measurement (ratio or percentage) of beta fraction proteins to total proteins in a biological specimen. |
| C92257 | GLOBG | Gamma Globulin | A measurement of the proteins contributing to the gamma fraction in a biological specimen. |
| C92295 | GLOBGPT | Gamma Globulin/Total Protein | A relative measurement (ratio or percentage) of gamma fraction proteins to total proteins in a biological specimen. |
| C74738 | GLOBUL | Globulin | A measurement of the globulin protein in a biological specimen. |
| C80183 | GLP1 | Glucagon-Like Peptide-1; Total Glucagon-Like Peptide-1 | A measurement of the total glucagon-like peptide-1 in a biological specimen. |
| C80164 | GLP1AC | Glucagon-Like Peptide-1, Active Form | A measurement of the active form of glucagon-like peptide-1 in a biological specimen. |
| C154768 | GLP1IAC | Glucagon-Like Peptide-1, Inactive Form | A measurement of the inactive form of glucagon-like peptide-1 in a biological specimen. |
| C150844 | GLTRCE | Glitter Cells | A measurement of the glitter cells in a biological specimen. |
| C184571 | GLTTHMD | Glutethimide | A measurement of the glutethimide in a biological specimen. |
| C132370 | GLUBD13 | 1,3-Beta-D-Glucan | A measurement of the 1,3-beta-D-glucan in a biological specimen. |
| C105585 | GLUC | Glucose | A measurement of the glucose in a biological specimen. |
| C74859 | GLUCAGON | Glucagon | A measurement of the glucagon hormone in a biological specimen. |
| C96652 | GLUCCLR | Glucose Clearance | A measurement of the volume of serum or plasma that would be cleared of glucose by excretion of urine for a specified unit of time (e.g. one minute). |
| C79447 | GLUCCRT | Glucose/Creatinine | A relative measurement (ratio or percentage) of the glucose to creatinine in a biological specimen. |
| C150818 | GLUCEXR | Glucose Excretion Rate | A measurement of the amount of glucose being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C163446 | GLUCPE | Plasma Equivalent Glucose | A measurement of the plasma equivalent glucose in a biological specimen. |
| C163447 | GLUCPED | Plasma Equivalent Glucose Distribution | A measurement of the plasma equivalent glucose distribution in a biological specimen. |
| C176296 | GLUCWBE | Whole Blood Equivalent Glucose | A measurement of the whole blood equivalent glucose in a biological specimen. |
| C186054 | GLURLGLU | Glucose, Enriched/Glucose; Glucose, Radiolabeled/Glucose | A relative measurement (ratio or percentage) of radiolabeled glucose to total glucose in a biological specimen. |
| C74739 | GLUTAM | Glutamate; Glutamic Acid | A measurement of the glutamate in a biological specimen. |
| C122122 | GLY | Glycine | A measurement of the glycine in a biological specimen. |
| C158221 | GLYCREAT | Glycine/Creatinine | A relative measurement (ratio) of the glycine to the creatinine in a biological specimen. |
| C132371 | GLYCRL | Glycerol | A measurement of the total glycerol in a biological specimen. |
| C100448 | GLYCRLFR | Free Glycerin; Free Glycerol | A measurement of the amount of unbound glycerol in a biological specimen. |
| C184516 | GM3 | Ganglioside GM3; Monosialodihexosylganglioside | A measurement of the ganglioside GM3 in a biological specimen. |
| C82019 | GMCSF | Granulocyte Macrophage Colony Stm Factor | A measurement of the granulocyte macrophage colony stimulating factor in a biological specimen. |
| C174310 | GMI | Glucose Management Indicator | An approximate measure (expressed as a % or mmol/mol) of an individual's expected hemoglobin A1c/hemoglobin level, based on the mean glucose measured over a period of at least 10 days by continuous glucose monitoring. |
| C74860 | GNRH | Gonadotropin Releasing Hormone; Luteinising Hormone Releasing Hormone | A measurement of the gonadotropin releasing hormone in a biological specimen. |
| C80186 | GOLD | Gold | A measurement of the gold in a biological specimen. |
| C187807 | GPDA | Glycylproline Dipeptidyl Aminopeptidase; GPDA | A measurement of the glycylproline dipeptidyl aminopeptidase in a biological specimen. |
| C96654 | GRAN | Granulocytes; Polymorphonuclear Leukocytes | A measurement of the granulocytes in a biological specimen. |
| C186055 | GRANB | Banded Granulocytes; Granulocytes Band Form | A measurement of the banded granulocytes in a biological specimen. |
| C127615 | GRANBCE | Granulocytes Band Form/Total Cells | A relative measurement (ratio or percentage) of the banded granulocytes to total cells in a biological specimen. |
| C98866 | GRANCE | Granulocytes/Total Cells | A relative measurement (ratio or percentage) of the granulocytes to total cells in a biological specimen (for example a bone marrow specimen). |
| C96675 | GRANIM | Immature Granulocytes | A measurement of the total immature granulocytes in a biological specimen. |
| C100445 | GRANIMLE | Immature Granulocytes/Leukocytes | A relative measurement (ratio or percentage) of the immature granulocytes to leukocytes in a biological specimen (for example a bone marrow specimen). |
| C147351 | GRANLE | Granulocytes/Leukocytes; Polymorphonuclear Leukocytes/Leukocytes | A relative measurement (ratio or percentage) of the granulocytes to total leukocytes in a biological specimen. |
| C186056 | GRANSG | Granulocytes Segmented | A measurement of the segmented granulocytes in a biological specimen. |
| C127616 | GRANSGCE | Granulocytes Segmented/Total Cells | A relative measurement (ratio or percentage) of the segmented granulocytes to total cells in a biological specimen. |
| C165963 | GRANULIN | Granulin | A measurement of the granulin in a biological specimen. |
| C165964 | GRN | Progranulin | A measurement of the progranulin in a biological specimen. |
| C186057 | GRO | Growth Regulated Oncogene | A measurement of the total growth regulated oncogene proteins in a biological specimen. |
| C74861 | GRWHIH | Growth Hormone Inhibiting Hormone; Somatostatin | A measurement of the growth hormone inhibiting hormone in a biological specimen. |
| C74862 | GRWHRH | Growth Hormone Releasing Hormone; Somatocrinin | A measurement of the growth hormone releasing hormone in a biological specimen. |
| C80185 | GST | Glutathione S-Transferase, Total | A measurement of the total glutathione-s-transferase in a biological specimen. |
| C79433 | GSTAL | Alpha Glutathione-S-Transferase | A measurement of the alpha form of glutathione S-transferase in a biological specimen. |
| C80166 | GSTALCRT | Glutathione S-Transferase, Alpha/Creat | A relative measurement (ratio or percentage) of the alpha glutathione-S-transferase to creatinine in a biological specimen. |
| C119278 | GSTALEXR | Alpha-GST Excretion Rate | A measurement of the amount of Alpha Glutathione-S-Transferase being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C79435 | GSTCREAT | Glutathione-S-Transferase/Creatinine | A relative measurement (ratio or percentage) of the glutathione S-transferase to creatinine in a biological specimen. |
| C79457 | GSTMU | Mu Glutathione-S-Transferase | A measurement of the mu form of glutathione S-transferase in a biological specimen. |
| C79458 | GSTMUCRT | Mu Glutathione-S-Transferase/Creatinine | A relative measurement (ratio or percentage) of the mu gamma glutamyl transpeptidase to creatinine in a biological specimen. |
| C80203 | GSTPI | Glutathione S-Transferase, Pi | A measurement of the Pi glutathione-s-transferase in a biological specimen. |
| C119279 | GSTPIEXR | Pi-GST Excretion Rate | A measurement of the amount of Pi Glutathione-S-Transferase being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C80207 | GSTTH | Glutathione S-Transferase, Theta | A measurement of the theta glutathione-s-transferase in a biological specimen. |
| C163449 | GSTY1 | Glutathione S-Transferase, Y1 | A measurement of the Y1 subunit of glutathione-s-transferase in a biological specimen. |
| C176302 | GUDCA | Glycoursodeoxycholate; Glycoursodeoxycholic Acid | A measurement of the glycoursodeoxycholate in a biological specimen. |
| C80165 | GUSA | Glucuronidase, Alpha | A measurement of the alpha glucuronidase in a biological specimen. |
| C80170 | GUSB | Glucuronidase, Beta | A measurement of the beta glucuronidase in a biological specimen. |
| C181419 | H2FLRZPM | 2-Hydroxyethylflurazepam; Hydroxyethylflurazepam | A measurement of the hydroxyethylflurazepam a biological specimen. |
| C186058 | H411DC6A | 6-Alpha Hydroxytetrahydro-11-Dehydrocorticosterone; 6a OH-tetrahydro-11-DeH-Corticosterone | A measurement of the 6-alpha hydroxytetrahydro-11-dehydrocorticosterone in a biological specimen. |
| C186059 | H411DS6A | 6-Alpha Hydroxytetrahydro-11-Deoxycortisol; 6a OH-tetrahydro-11-Deoxycortisol | A measurement of the 6-alpha hydroxytetrahydro-11-deoxycortisol in a biological specimen. |
| C165965 | HAHA | Human Anti-Human Antibody | A measurement of the total human anti-human antibody in a biological specimen. |
| C74604 | HAIRYCE | Hairy Cells | A measurement of the hairy cells (b-cell lymphocytes with hairy projections from the cytoplasm) in a biological specimen. |
| C103405 | HALBAB | Human Albumin Antibody | A measurement of the human albumin antibody in a biological specimen. |
| C75343 | HALLUC | Hallucinogen | A measurement of any hallucinogenic class drug present in a biological specimen. |
| C177964 | HALOPRDL | Haloperidol | A measurement of the haloperidol in a biological specimen. |
| C177954 | HALPRZLA | Alpha-Hydroxyalprazolam | A measurement of the alpha-hydroxyalprazolam in a biological specimen. |
| C147352 | HALPRZLM | Hydroxyalprazolam | A measurement of the total hydroxyalprazolam present in a biological specimen. |
| C103406 | HAMAB | HAMA; Human Anti-Mouse Antibody | A measurement of the human anti-mouse antibody in a biological specimen. |
| C74740 | HAPTOG | Haptoglobin | A measurement of the haptoglobin protein in a biological specimen. |
| C98740 | HASIGEAB | Human Anti-Sheep IgE Antibody | A measurement of the human anti-sheep IgE antibodies in a biological specimen. |
| C98741 | HASIGGAB | Human Anti-Sheep IgG Antibody | A measurement of the human anti-sheep IgG antibodies in a biological specimen. |
| C98742 | HASIGMAB | Human Anti-Sheep IgM Antibody | A measurement of the human anti-sheep IgM antibodies in a biological specimen. |
| C163450 | HBA1A | Glycated Hemoglobin 1A; Glycosylated Hemoglobin 1A; Hemoglobin A1A | A measurement of the glycosylated hemoglobin A1A in a biological specimen. |
| C163451 | HBA1B | Glycated Hemoglobin 1B; Glycosylated Hemoglobin 1B; Hemoglobin A1B | A measurement of the glycosylated hemoglobin A1B in a biological specimen. |
| C64849 | HBA1C | Glycated Hemoglobin; Glycosylated Hemoglobin A1C; HbA1c; Hemoglobin A1C | A measurement of the glycosylated hemoglobin A1C in a biological specimen. |
| C111207 | HBA1CHGB | Hemoglobin A1C/Hemoglobin | A relative measurement (ratio or percentage) of the glycosylated hemoglobin to total hemoglobin in a biological specimen. |
| C147353 | HBA2PHB | Hemoglobin A2 Prime/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin A2 prime to total hemoglobin in a biological specimen. |
| C147354 | HBBARTHB | Hemoglobin Barts/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin Barts to total hemoglobin in a biological specimen. |
| C147355 | HBCOHGB | Carboxyhemoglobin/Total Hemoglobin | A relative measurement (ratio or percentage) of the amount of carboxyhemoglobin compared to total hemoglobin in a biological specimen. |
| C147356 | HBGCHTHB | Hemoglobin G Coushatta/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin G Coushatta to total hemoglobin in a biological specimen. |
| C158234 | HBHIB | HBH Inclusion Bodies; Hemoglobin H Inclusion Bodies; HGH Inclusion Bodies | A measurement of the hemoglobin H inclusion bodies in a biological specimen. |
| C147357 | HBLEPRHB | Hemoglobin Lepore/Total Hemoglobin | A relative measurement (ratio or percentage) of the Lepore hemoglobin to total hemoglobin in a biological specimen. |
| C147358 | HBOARBHB | Hemoglobin O-Arab/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin O-Arab to total hemoglobin in a biological specimen. |
| C147359 | HBOXHGB | FO2 Hb; Fractioned Oxyhemoglobin; Oxyhemoglobin/Total Hemoglobin | A relative measurement (ratio or percentage) of the amount of oxyhemoglobin compared to total hemoglobin in a biological specimen. |
| C64851 | HCG | Choriogonadotropin Beta; Pregnancy Test | A measurement of the Choriogonadotropin Beta in a biological specimen. |
| C147360 | HCGFR | Choriogonadotropin Beta, Free | A measurement of the free choriogonadotropin beta in a biological specimen. |
| C147128 | HCGND | Choriogonadotropin | A measurement of the total choriogonadotropin in a biological specimen. |
| C147361 | HCGNDI | Choriogonadotropin, Intact | A measurement of the intact choriogonadotropin in a biological specimen. |
| C186060 | HCH4 | H+CH4; Hydrogen+Methane | A measurement of the hydrogen and methane in a biological specimen. |
| C176300 | HCHT | Hyocholate; Hyocholic Acid | A measurement of the hyocholate in a biological specimen. |
| C181428 | HCOA3 | 3-HCOA; 3-Hydroxy-5-cholestenoic acid; 3beta-Hydroxy-5-Cholestenoic Acid | A measurement of the 3beta-hydroxy-5-cholestenoic acid in a biological specimen. |
| C64796 | HCT | Erythrocyte Volume Fraction; EVF; Hematocrit; Packed Cell Volume; PCV | The percentage of a whole blood specimen that is composed of red blood cells (erythrocytes). |
| C105587 | HDL | HDL Cholesterol | A measurement of the high density lipoprotein cholesterol in a biological specimen. |
| C80187 | HDL2 | HDL-Cholesterol Subclass 2 | A measurement of the high-density lipoprotein (HDL) cholesterol subclass 2 in a biological specimen. |
| C80188 | HDL3 | HDL-Cholesterol Subclass 3 | A measurement of the high-density lipoprotein (HDL) cholesterol subclass 3 in a biological specimen. |
| C147362 | HDLCCHOL | HDL Cholesterol/Total Cholesterol | A relative measurement (ratio or percentage) of the amount of HDL cholesterol compared to total cholesterol in a biological specimen. |
| C100425 | HDLCLDLC | HDL Cholesterol/LDL Cholesterol | A relative measurement (ratio or percentage) of the amount of HDL cholesterol compared to LDL cholesterol in a biological specimen. |
| C156513 | HDLPL | HDL Phospholipid; HDL-PL | A measurement of the high density lipoprotein phospholipid in a biological specimen. |
| C103402 | HDLPSZ | HDL Particle Size | A measurement of the average particle size of high-density lipoprotein in a biological specimen. |
| C189510 | HDR51AGT | HLA-DR51 Antigen Type | The identification of the type of human leukocyte antigen, class II, antigen-D-related 51 (HLA-DR51), in a biological specimen. |
| C189511 | HDR52AGT | HLA-DR52 Antigen Type | The identification of the type of human leukocyte antigen, class II, antigen-D-related 52 (HLA-DR52), in a biological specimen. |
| C189512 | HDR53AGT | HLA-DR53 Antigen Type | The identification of the type of human leukocyte antigen, class II, antigen-D-related 53 (HLA-DR53), in a biological specimen. |
| C106525 | HDW | Hemoglobin Concentration Distribution Width; Hemoglobin Distribution Width | A measurement of the distribution of the hemoglobin concentration in red blood cells. |
| C139070 | HDWR | Ret Hemoglobin Distribution Width; Reticulocyte Hemoglobin Concentration Distribution Width | A measurement of the distribution of the hemoglobin concentration in reticulocytes. |
| C163452 | HE4 | Human Epididymis Protein 4 | A measurement of the human epididymis protein 4 in a biological specimen. |
| C74709 | HEINZ | Heinz Bodies; Heinz-Erhlich Bodies | A measurement of the Heinz bodies (small round inclusions within the body of a red blood cell) in a biological specimen. |
| C111206 | HEINZRBC | Heinz Bodies/Erythrocytes | A relative measurement (ratio or percentage) of the erythrocytes that contain heinz bodies to total erythrocytes in a biological specimen. |
| C74658 | HELMETCE | Helmet Cells | A measurement of the Helmet cells (specialized Keratocytes with two projections on either end that are tapered and hornlike) in a biological specimen. |
| C165966 | HELMOV10 | Helicase MOV-10 Protein; Moloney Leukemia Virus 10 Protein | A measurement of helicase MOV-10 protein in a biological specimen. |
| C111208 | HEMOLYSI | Hemolysis; Hemolytic Index | A measurement of the destruction of red blood cells in a biological specimen. |
| C165967 | HEPARIN | Heparin | A measurement of the heparin in a biological specimen. |
| C174387 | HEPCIDIN | Hepcidin | A measurement of the total hepcidin in a biological specimen. |
| C112312 | HER2 | ERBB2; HER2/NEU; Human Epidermal Growth Factor Receptor 2 | A measurement of HER2 protein in a biological specimen. |
| C112291 | HER2S | HER2 Antigen; HER2/NEU Antigen; HER2/NEU Shed Antigen; Soluble HER2; Soluble HER2/NEU | A measurement of the soluble HER2 protein in a biological specimen. |
| C163453 | HERC5 | E3 ISG15--Protein Ligase HERC5; HECT and RLD Domain Containing E3 Ubiquitin Protein Ligase 5; Hect Domain and RLD 5 | A measurement of the hect domain and RLD 5 in a biological specimen. |
| C116186 | HETRPH | Heterophils | A measurement of heterophils (granular leukocytes) in a biological specimen from avian species. |
| C116187 | HETRPHLE | Heterophils/Leukocytes | A relative measurement (ratio or percentage) of heterophils to leukocytes in a biological specimen from avian species. |
| C181411 | HEXA | Beta-Hexosaminidase Subunit Alpha; Beta-N-Acetylhexosaminidase Subunit Alpha; Hexosaminidase A; Hexosaminidase Subunit A; Hexosaminidase Subunit Alpha; N-Acetyl-Beta-Glucosaminidase Subunit Alpha | A measurement of the hexosaminidase A in a biological specimen. |
| C96668 | HEXK | Hexokinase | A measurement of the hexokinase in a biological specimen. |
| C64848 | HGB | Hemoglobin; Hemoglobin Monomer | A measurement of the total erythrocyte associated hemoglobin in a biological specimen. |
| C92258 | HGBA | Hemoglobin A | A measurement of the hemoglobin A in a biological specimen. |
| C147363 | HGBA1HGB | Hemoglobin A1/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin A1 to total hemoglobin in a biological specimen. |
| C92259 | HGBA2 | Hemoglobin A2 | A measurement of the hemoglobin A2 in a biological specimen. |
| C81277 | HGBA2HGB | Hemoglobin A2/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin A2 to total hemoglobin in a biological specimen. |
| C81276 | HGBAHGB | Hemoglobin A/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin A to total hemoglobin in a biological specimen. |
| C92260 | HGBB | Hemoglobin B | A measurement of the hemoglobin B in a biological specimen. |
| C92261 | HGBC | Hemoglobin C | A measurement of the hemoglobin C in a biological specimen. |
| C81278 | HGBCHGB | Hemoglobin C/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin C to total hemoglobin in a biological specimen. |
| C156515 | HGBCS | Hemoglobin Casts | A measurement of the hemoglobin casts present in a biological specimen. |
| C147364 | HGBDHGB | Hemoglobin D/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin D to total hemoglobin in a biological specimen. |
| C124343 | HGBDOXY | Deoxyhemoglobin | A measurement of the deoxyhemoglobin, hemoglobin without oxygen, in a biological specimen. |
| C147365 | HGBEHGB | Hemoglobin E/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin E to total hemoglobin in a biological specimen. |
| C92262 | HGBF | Fetal Hemoglobin; Hemoglobin F | A measurement of the hemoglobin F in a biological specimen. |
| C147366 | HGBFHGB | Hemoglobin F/Total Hemoglobin | A relative measurement (ratio or percentage) of the fetal hemoglobin (hemoglobin F) to total hemoglobin in a biological specimen. |
| C161363 | HGBFPATN | Hemoglobin Fraction Pattern | A description of the hemoglobin fraction pattern in a biological specimen. |
| C127617 | HGBFR | Hemoglobin, Free | A measurement of the hemoglobin external to erythrocytes in a biological specimen. |
| C96689 | HGBMET | Methemoglobin | A measurement of the methemoglobin in a biological specimen. |
| C147367 | HGBMHGB | FMET HB; Fractionated Methemoglobin; Methemoglobin/Total Hemoglobin | A relative measurement (ratio or percentage) of the amount of methemoglobin compared to total hemoglobin in a biological specimen. |
| C96616 | HGBOXY | Oxyhemoglobin | A measurement of the oxyhemoglobin, oxygen-bound hemoglobin, in a biological specimen. |
| C122123 | HGBS | Hemoglobin S; Sickle Hemoglobin | A measurement of the hemoglobin S in a biological specimen. |
| C81279 | HGBSHGB | Hemoglobin S/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin S to total hemoglobin in a biological specimen. |
| C135425 | HGBTET | Hemoglobin Tetramer | A measurement of the hemoglobin tetramer in a biological specimen. |
| C103845 | HGBVAR | Hemoglobin Variants | A statement that indicates a defined set of hemoglobin variants were looked for in a biological specimen. |
| C135426 | HGF | Hepatocyte Growth Factor | A measurement of the hepatocyte growth factor in a biological specimen. |
| C172514 | HGFR | c-Met; Hepatocyte Growth Factor Receptor; MET Proto-Oncogene, Receptor Tyrosine Kinase; Tyrosine-Protein Kinase Met | A measurement of the hepatocyte growth factor receptor in a biological specimen. |
| C181453 | HGFRFR | Hepatocyte Growth Factor Receptor, Free | A measurement of the free (unbound) hepatocyte growth factor receptor in a biological specimen. |
| C187809 | HGPRT | Hypoxanthine-Guanine Phosphoribosyltransferase; Hypoxanthine-Guanine PRT | A measurement of the hypoxanthine-guanine phosphoribosyltransferase in a biological specimen. |
| C122124 | HIS | Histidine | A measurement of the histidine in a biological specimen. |
| C112293 | HIST1AB | Histone 1 Antibody | A measurement of the total histone 1 antibodies in a biological specimen. |
| C112294 | HIST2AAB | Histone 2A Antibody | A measurement of the total histone 2A antibodies in a biological specimen. |
| C112295 | HIST2BAB | Histone 2B Antibody | A measurement of the total histone 2B antibodies in a biological specimen. |
| C112296 | HIST3AB | Histone 3 Antibody | A measurement of the total histone 3 antibodies in a biological specimen. |
| C112297 | HIST4AB | Histone 4 Antibody | A measurement of the total histone 4 antibodies in a biological specimen. |
| C111209 | HISTAB | Anti-Histone Antibodies; Histone Antibodies | A measurement of histone antibodies in a biological specimen. |
| C80189 | HISTAMIN | Histamine | A measurement of the histamine in a biological specimen. |
| C154746 | HLAA | HLA Class IA Antigen | A measurement of the HLA class IA antigen in a biological specimen. |
| C181440 | HLAA03 | HLA A03 Antigen; HLA-A03 Antigen | A measurement of the HLA A03 antigen in a biological specimen. |
| C181441 | HLAA2 | HLA A2 Antigen; HLA-A2 Antigen | A measurement of the HLA A2 antigen in a biological specimen. |
| C128953 | HLAA23A | HLA-A23 Antibody | A measurement of the human leukocyte antigen A23 (HLA-A23) antibody in a biological specimen. |
| C181442 | HLAA24 | HLA A24 Antigen; HLA-A24 Antigen | A measurement of the HLA A24 antigen in a biological specimen. |
| C128954 | HLAA2AB | HLA-A2 Antibody | A measurement of the human leukocyte antigen A2 (HLA-A2) antibody in a biological specimen. |
| C181443 | HLAA3 | HLA A3 Antigen; HLA-A3 Antigen | A measurement of the HLA A3 antigen in a biological specimen. |
| C128955 | HLAAAGT | HLA-A Antigen Type | The identification of the type of human leukocyte antigen, class I, group A (HLA-A), in a biological specimen. |
| C128956 | HLAAMSC | HLA-A Mismatch Count | A measurement to determine the number of mismatches between the recipient and the donor for the human leukocyte antigen, class I, group A (HLA-A). |
| C154747 | HLAB | HLA Class IB Antigen | A measurement of the HLA class IB antigen in a biological specimen. |
| C100460 | HLAB27AG | HLA-B27 Antigen; Human Leukocyte Antigen B27 | A measurement of the human leukocyte antigen B27 (HLA-B27) in a biological specimen. |
| C128957 | HLABAGT | HLA-B Antigen Type | The identification of the type of human leukocyte antigen, class I, group B (HLA-B), in a biological specimen. |
| C128958 | HLABMSC | HLA-B Mismatch Count | A measurement to determine the number of mismatches between the recipient and the donor for the human leukocyte antigen, class I, group B (HLA-B). |
| C154748 | HLAC | HLA Class IC Antigen | A measurement of the HLA class IC antigen in a biological specimen. |
| C181439 | HLACW | HLA Cw Antigen; HLA-Cw Antigen | A measurement of the HLA Cw antigen in a biological specimen. |
| C181417 | HLADPA1 | HLA DP Alpha1 Antigen; HLA-DP Alpha1 Antigen | A measurement of the HLA DP alpha1 antigen in a biological specimen. |
| C181444 | HLADPB | HLA DP Beta Antigen; HLA-DP Beta Antigen | A measurement of the total HLA DP beta antigen in a biological specimen. |
| C154751 | HLADPB1 | HLA DP Beta1 Antigen | A measurement of the HLA DP beta1 antigen in a biological specimen. |
| C186061 | HLADQ2 | HLA DQ2 Antigen; HLA-DQ2 Antigen | A measurement of the HLA DQ2 antigen in a biological specimen. |
| C186062 | HLADQ8 | HLA DQ8 Antigen; HLA-DQ8 Antigen | A measurement of the HLA DQ8 antigen in a biological specimen. |
| C181416 | HLADQA1 | HLA DQ Alpha1 Antigen; HLA-DQ Alpha1 Antigen | A measurement of the HLA DQ alpha1 antigen in a biological specimen. |
| C154750 | HLADQB1 | HLA DQ Beta1 Antigen | A measurement of the HLA DQ beta1 antigen in a biological specimen. |
| C176962 | HLADR | HLA DR Antigen; HLA-DR Antigen | A measurement of the total HLA DR antigen in a biological specimen. |
| C128959 | HLADR51A | HLA-DR51 Antibody | A measurement of the human leukocyte antigen DR51 (HLA-DR51) antibody in a biological specimen. |
| C128960 | HLADR52A | HLA-DR52 Antibody | A measurement of the human leukocyte antigen DR52 (HLA-DR52) antibody in a biological specimen. |
| C128961 | HLADR53A | HLA-DR53 Antibody | A measurement of the human leukocyte antigen DR53 (HLA-DR53) antibody in a biological specimen. |
| C128962 | HLADRAGT | HLA-DR Antigen Type | The identification of the type of human leukocyte antigen, class II, antigen-D-related (HLA-DR), in a biological specimen. |
| C181192 | HLADRB | HLA DR Beta Antigen; HLA-DR Beta Antigen | A measurement of the total HLA DR beta antigen in a biological specimen. |
| C154749 | HLADRB1 | HLA DR Beta1 Antigen | A measurement of the HLA DR beta1 antigen in a biological specimen. |
| C181415 | HLADRB2 | HLA DR Beta2 Antigen; HLA-DR Beta2 Antigen | A measurement of the HLA DR beta2 antigen in a biological specimen. |
| C181412 | HLADRB3 | HLA DR Beta3 Antigen; HLA-DR Beta3 Antigen | A measurement of the HLA DR beta3 antigen in a biological specimen. |
| C181413 | HLADRB4 | HLA DR Beta4 Antigen; HLA-DR Beta4 Antigen | A measurement of the HLA DR beta4 antigen in a biological specimen. |
| C181414 | HLADRB5 | HLA DR Beta5 Antigen; HLA-DR Beta5 Antigen | A measurement of the HLA DR beta5 antigen in a biological specimen. |
| C128963 | HLADRMSC | HLA-DR Mismatch Count | A measurement to determine the number of mismatches between the recipient and the donor for the human leukocyte antigen, class II, antigen-D-related (HLA-DR). |
| C128964 | HLAIAB | HLA Class I Antibody | A measurement of the human leukocyte antigen (HLA) antibody class I in a biological specimen. |
| C128965 | HLAIIAB | HLA Class II Antibody | A measurement of the human leukocyte antigen (HLA) antibody class II in a biological specimen. |
| C128966 | HLAIIPRA | HLA Class II Panel Reactive Antibody | A measurement of the panel reactive antibody (the reactivity between host immune cells and donor) human leukocyte antigen class II in a biological specimen. |
| C128967 | HLAIPRA | HLA Class I Panel Reactive Antibody | A measurement of the panel reactive antibody (the reactivity between host immune cells and donor) human leukocyte antigen class I in a biological specimen. |
| C128933 | HLAMSC | HLA Mismatch Count | A measurement to determine the number of mismatches between the recipient and the donor for the human leukocyte antigens (HLA). |
| C139078 | HLZPM | Halazepam | A measurement of the halazepam present in a biological specimen. |
| C96659 | HMOSIDRN | Hemosiderin | A measurement of the hemosiderin complex in a biological specimen. |
| C154758 | HOMOCIT | Homocitrulline | A measurement of the homocitrulline in a biological specimen. |
| C74741 | HOMOCY | Homocysteine | A measurement of the homocysteine amino acid in a biological specimen. |
| C181409 | HORBCRBC | Hypochromic Erythrocytes/Erythrocytes | A relative measurement (ratio or percentage) of the hypochromic erythrocytes to total erythrocytes in a biological specimen. |
| C74704 | HOWJOL | Howell-Jolly Bodies | A measurement of the Howell-Jolly bodies (spherical, blue-black condensed DNA inclusions within the body of a red blood cell that appear under Wright-stain) in a biological specimen. |
| C64802 | HPOCROM | Hypochromia; Hypochromic Erythrocytes | An observation which indicates that the hemoglobin concentration in a red blood cell specimen has fallen below a specified level. |
| C181408 | HRRBCRBC | Hyperchromic Erythrocytes/Erythrocytes | A relative measurement (ratio or percentage) of the hyperchromic erythrocytes to total erythrocytes in a biological specimen. |
| C135427 | HRYCECE | Hairy Cells/Total Cells | A relative measurement (ratio or percentage) of the hairy cells to total cells in a biological specimen. |
| C135428 | HRYCELE | Hairy Cells/Leukocytes | A relative measurement (ratio or percentage) of the hairy cells (B-cell lymphocytes with hairy projections from the cytoplasm) to all leukocytes in a biological specimen. |
| C74640 | HRYCELY | Hairy Cells/Lymphocytes | A relative measurement (ratio or percentage) of the hairy cells (b-cell lymphocytes with hairy projections from the cytoplasm) to all lymphocytes in a biological specimen . |
| C147368 | HSP70 | Heat Shock Protein 70 | A measurement of the heat shock protein 70 in a biological specimen. |
| C147369 | HSP90A | Heat Shock Protein 90 Alpha | A measurement of the heat shock protein 90 alpha in a biological specimen. |
| C142279 | HTTP | Huntingtin Protein | A measurement of the huntingtin protein in a biological specimen. |
| C142280 | HTTPM | Huntingtin Protein, Mutant | A measurement of the mutant huntingtin protein in a biological specimen. |
| C74863 | HVA | Homovanillic Acid | A measurement of the homovanillic acid metabolite in a biological specimen. |
| C186063 | HXANSD11 | 11-Hydroxyandrostenedione | A measurement of the 11-hydroxyandrostenedione in a biological specimen. |
| C186064 | HXANST11 | 11-Hydroxyandrosterone | A measurement of the 11-hydroxyandrosterone in a biological specimen. |
| C186065 | HXCSD17 | 17-Hydroxycorticoid; 17-Hydroxycorticosteroid; 17-Hydroxycorticosteroids | A measurement of the 17-hydroxycorticosteroids in a biological specimen. |
| C186066 | HXCSL18 | 18-Hydroxycortisol | A measurement of the 18-hydroxycortisol in a biological specimen. |
| C186067 | HXCSN18 | 18-Hydroxycorticosterone | A measurement of the 18-hydroxycorticosterone in a biological specimen. |
| C186068 | HXDX18 | 18-Hydroxydeoxycorticosterone | A measurement of the 18-hydroxydeoxycorticosterone in a biological specimen. |
| C186069 | HXETCL11 | 11-Hydroxyetiocholanolone | A measurement of the 11-hydroxyetiocholanolone in a biological specimen. |
| C187788 | HXNE4 | 4-HNE; 4-hydroxy-2-nonenal; 4-Hydroxynonenal; HNE | A measurement of the 4-hydroxynonenal in a biological specimen. |
| C186070 | HXPRGN17 | 17-Hydroxypregnenolone | A measurement of the 17-hydroxypregnenolone in a biological specimen. |
| C112319 | HYALUAC | Hyaluronic Acid | A measurement of hyaluronic acid in a biological specimen. |
| C74879 | HYDCDN | Hydrocodone | A measurement of the hydrocodone present in a biological specimen. |
| C154732 | HYDMDZ1 | 1'-Hydroxymidazolam; 1-Hydroxymidazolam; Alpha-Hydroxymidazolam | A measurement of the 1-Hydroxymidazolam present in a biological specimen. |
| C154731 | HYDMDZ4 | 4-Hydroxymidazolam | A measurement of the 4-hydroxymidazolam present in a biological specimen. |
| C74880 | HYDMRPHN | Hydromorphone | A measurement of the hydromorphone present in a biological specimen. |
| C102275 | HYDROGEN | Hydrogen | A measurement of the hydrogen in a biological specimen. |
| C96669 | HYPERCHR | Hyperchromia; Hyperchromic Erythrocytes | A measurement of the prevalence of the erthrocytes with an elevated hemoglobin concentration. |
| C147370 | HYPGST17 | 17-Hydroxyprogesterone; 17-OHP | A measurement of the 17-Hydroxyprogesterone in a biological specimen. |
| C80190 | HYPRLN | Hydroxyproline | A measurement of the total hydroxyproline in a biological specimen. |
| C74612 | HYPSEGCE | Hypersegmented Cells | A measurement of the hypersegmented (more than five lobes) neutrophils in a biological specimen. |
| C154767 | HYXLYS | Hydroxylysine | A measurement of the hydroxylysine in a biological specimen. |
| C119284 | IA2AB | Insulinoma-Associated Protein 2 Antibody | A measurement of the insulinoma-associated protein 2 antibody in a biological specimen. |
| C163454 | IA5OHEXR | 5-Hydroxyindoleacetic Acid Excretion Rate; 5-HydroxyindoleaceticAcid Excretion Rate | A measurement of the amount of 5-hydroxyindoleacetic acid being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C112217 | IAA5OH | 5-Hydroxyindoleacetate; 5-Hydroxyindoleacetic Acid | A measurement of 5-hydroxyindoleacetic acid in a biological specimen. |
| C170578 | IAA5OHCR | 5-Hydroxyindoleacetic Acid/Creatinine | A relative measurement (ratio or percentage) of the 5-hydroxyindoleacetic acid to creatinine in a biological specimen. |
| C184514 | IAPOB | IDL Apolipoprotein B | A measurement of the apolipoprotein B in the intermediate density lipoprotein fraction of a biological specimen. |
| C127622 | IAPP | Amylin; Islet Amyloid Polypeptide | A measurement of the islet amyloid polypeptide in a biological specimen. |
| C74718 | IBCT | Total Iron Binding Capacity | A measurement of the amount of iron needed to fully saturate the transferrin in a biological specimen. |
| C74719 | IBCU | Unsaturated Iron Binding Capacity | A measurement of the binding capacity of unsaturated iron in a biological specimen. |
| C81985 | IC512AB | IA-2 Antibody; ICA-512 Antibody; Islet Antigen 2 Autoantibody; Islet Cell 512 Antibody; Islet Cell Antigen 512 Autoantibody | A measurement of the islet cell 512 antibody in a biological specimen. |
| C81986 | IC512AG | Islet Cell 512 Antigen | A measurement of the islet cell 512 antigen in a biological specimen. |
| C154725 | ICAB | Islet Cell Antibody | A measurement of the total islet cell antibodies in a biological specimen. |
| C122126 | ICAIGGAB | Islet Cell Cytoplasmic IgG Antibody | A measurement of the islet cell cytoplasmic IgG antibody in a biological specimen. |
| C124344 | ICAM | Intercellular Adhesion Molecule | A measurement of the total intercellular adhesion molecule in a biological specimen. |
| C124345 | ICAM1 | CD54; Intercellular Adhesion Molecule 1 | A measurement of the intercellular adhesion molecule 1 in a biological specimen. |
| C165968 | ICAM3 | Intercellular Adhesion Molecule 3 | A measurement of the intercellular adhesion molecule 3 in a biological specimen. |
| C184512 | ICG | Indocyanine Green | A measurement of the indocyanine green in a biological specimen. |
| C184513 | ICGCLR | Indocyanine Green Clearance | A measurement of the volume of serum or plasma that would be cleared of indocyanine green by excretion for a specified unit of time (e.g. one minute). |
| C111232 | ICTERUSI | Icteric Index; Icterus | A measurement of the yellow color of a biological specimen, due to the presence of bile pigments. |
| C112325 | IDL | IDL Cholesterol; Intermediate Density Lipoprotein | A measurement of the intermediate density lipoprotein in a biological specimen. |
| C187810 | IDLLDL | IDL Cholesterol/LDL Cholesterol | A relative measurement (ratio) of the amount of intermediate density lipoprotein cholesterol compared to low density lipoprotein cholesterol in a biological specimen. |
| C116197 | IDLP | IDL Particles; Intermediate Density Lipoproteins Particles | A measurement of the concentration of IDL particles in a biological specimen. |
| C189507 | IDLT | IDL Triglyceride | A measurement of the intermediate density lipoprotein triglyceride in a biological specimen. |
| C147371 | IDLVLDL3 | IDL Cholesterol and VLDL Cholesterol Subtype 3; IDL+VLDL Cholesterol Subtype 3 | A measurement of the intermediate density lipoprotein cholesterol and the very low density lipoprotein cholesterol subtype 3 in a biological specimen. |
| C163455 | IFI27 | Interferon Alpha-Induced Protein 27; Interferon Alpha-Inducible Protein 27 | A measurement of the interferon alpha-inducible protein 27 in a biological specimen. |
| C163456 | IFI44 | Interferon-Induced Protein 44 | A measurement of the interferon-induced protein 44 in a biological specimen. |
| C163457 | IFI44L | Interferon-Induced Protein 44-Like | A measurement of the interferon-induced protein 44-like in a biological specimen. |
| C163458 | IFI6 | Interferon Alpha-Inducible Protein 6 | A measurement of the interferon alpha-inducible protein 6 in a biological specimen. |
| C163459 | IFIT1 | Interferon-Induced 56 kDa Protein; Interferon-Induced Protein With Tetratricopeptide Repeats 1 | A measurement of the interferon-induced 56 KDa protein in a biological specimen. |
| C163460 | IFIT3 | Interferon-Induced 60 kDa Protein; Interferon-Induced Protein With Tetratricopeptide Repeats 3 | A measurement of the interferon-induced 60 KDa protein in a biological specimen. |
| C81994 | IFNA | Interferon Alpha | A measurement of the total interferon alpha in a biological specimen. |
| C184646 | IFNA2 | Interferon Alpha Type 2 | A measurement of the interferon alpha type 2 in a biological specimen. |
| C81995 | IFNB | Interferon Beta | A measurement of the interferon beta in a biological specimen. |
| C81996 | IFNG | Interferon Gamma | A measurement of the interferon gamma in a biological specimen. |
| C81969 | IGA | Immunoglobulin A | A measurement of the total immunoglobulin A in a biological specimen. |
| C184515 | IGAC3 | IgA/C3; IgA/Complement C3; Immunoglobulin A/Complement C3 | A relative measurement (ratio) of the immunoglobulin A to complement C3 in a biological specimen. |
| C111233 | IGAGM | IgG IgM IgA Total | A measurement of the total IgG, IgM, and IgA in a biological specimen. |
| C98745 | IGD | Immunoglobulin D | A measurement of the Immunoglobulin D in a biological specimen. |
| C81970 | IGE | Immunoglobulin E | A measurement of the Immunoglobulin E in a biological specimen. |
| C74864 | IGF1 | Insulin-like Growth Factor-1 | A measurement of the insulin-like growth factor-1 in a biological specimen. |
| C74865 | IGF2 | Insulin-like Growth Factor-2 | A measurement of the insulin-like growth factor-2 in a biological specimen. |
| C128968 | IGFBP1 | Insulin-Like Growth Factor Binding Prot1; Insulin-Like Growth Factor Binding Protein 1 | A measurement of the total insulin-like growth factor binding protein 1 in a biological specimen. |
| C128969 | IGFBP2 | Insulin-Like Growth Factor Binding Prot2; Insulin-Like Growth Factor Binding Protein 2 | A measurement of the insulin-like growth factor binding protein 2 in a biological specimen. |
| C112322 | IGFBP3 | Insulin-Like Growth Factor Binding Prot3; Insulin-Like Growth Factor Binding Protein 3 | A measurement of the insulin-like growth factor binding protein 3 in a biological specimen. |
| C165969 | IGFBP7 | AGM; FSTL2; IBP-7; IGFBP-7; IGFBP-7v; IGFBPRP1; Insulin-Like Growth Factor Binding Prot7; Insulin-like Growth Factor Binding Protein 7; MAC25; PSF; RAMSVPS; TAF | A measurement of the insulin-like growth factor binding protein 7 in a biological specimen. |
| C81971 | IGG | Immunoglobulin G | A measurement of the total immunoglobulin G in a biological specimen. |
| C122127 | IGG1 | Immunoglobulin G Subclass 1 | A measurement of the immunoglobulin G subclass 1 in a biological specimen. |
| C122128 | IGG2 | Immunoglobulin G Subclass 2 | A measurement of the immunoglobulin G subclass 2 in a biological specimen. |
| C122129 | IGG3 | Immunoglobulin G Subclass 3 | A measurement of the immunoglobulin G subclass 3 in a biological specimen. |
| C122130 | IGG4 | Immunoglobulin G Subclass 4 | A measurement of the immunoglobulin G subclass 4 in a biological specimen. |
| C147372 | IGGALB | IgG/Albumin; Immunoglobulin G/Albumin | A relative measurement (ratio or percentage) of the immunoglobulin G to albumin in a biological specimen. |
| C147373 | IGGC | IgG Clearance | A measurement of the IgG clearance in a biological specimen. |
| C147374 | IGGCALBC | IgG Clearance/Albumin Clearance | A relative measurement (ratio) of the IgG clearance to albumin clearance in a biological specimen. |
| C119285 | IGGCREAT | Immunoglobulin G/Creatinine | A relative measurement (ratio or percentage) of the immunoglobulin G to creatinine in a biological specimen. |
| C147375 | IGGSYNRT | IgG Synthesis Rate | A measurement of the IgG synthesis rate in a biological specimen. |
| C154737 | IGHG2 | Immunoglobulin Heavy Constant Gamma 2 | A measurement of the immunoglobulin heavy constant gamma 2 in a biological specimen. |
| C154738 | IGHG4 | Immunoglobulin Heavy Constant Gamma 4 | A measurement of the immunoglobulin heavy constant gamma 4 in a biological specimen. |
| C81972 | IGM | Immunoglobulin M | A measurement of the total immunoglobulin M in a biological specimen. |
| C117835 | IGSOL | Soluble Immunoglobulin | A measurement of the soluble total immunoglobulin in a biological specimen. |
| C128970 | IL122340 | Interleukin 12+23 p40 | A measurement of the p40 subunit of the interleukins 12 and 23 in a biological specimen. |
| C172513 | IL18BP | Interleukin 18 Binding Protein | A measurement of the interleukin 18 binding protein in a biological specimen. |
| C156519 | IL18EXR | Interleukin 18 Excretion Rate | A measurement of the amount of interleukin 18 being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C156518 | IL1EXR | Interleukin 1 Excretion Rate | A measurement of the amount of interleukin 1 being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C165970 | IL1R2 | CD121b; CDw121b; IL-1R-2; IL-1RT2; IL1R2c; IL1RB; Interleukin 1 Receptor Type 2 | A measurement of the interleukin 1 receptor type 2 in a biological specimen. |
| C142281 | IL1RL1 | Interleukin 1 Receptor-Like 1; Protein ST2; sST2 | A measurement of the interleukin 1 receptor-like 1 in a biological specimen. |
| C117836 | IL1SR1 | Soluble Interleukin-1 Receptor Type I | A measurement of the soluble interleukin-1 receptor type I in a biological specimen. |
| C158147 | IL2R | Interleukin 2 Receptor | A measurement of the interleukin 2 receptor in a biological specimen. |
| C142282 | IL2RA | CD25; IL-2Ra; Interleukin 2 Receptor Subunit Alpha | A measurement of the interleukin 2 receptor subunit alpha in a biological specimen. |
| C142283 | IL2RB | IL-2Rb; Interleukin 2 Receptor Subunit Beta | A measurement of the interleukin 2 receptor subunit beta in a biological specimen. |
| C158220 | IL2SR | sCD25; Soluble CD25; Soluble IL-2Ra; Soluble Interleukin 2 Receptor; Soluble Interleukin 2 Receptor Subunit Alpha | A measurement of the soluble interleukin 2 receptor in a biological specimen. |
| C117837 | IL6SR | Soluble Interleukin 6 Receptor | A measurement of the soluble interleukin 6 receptor in a biological specimen. |
| C103410 | ILE | Isoleucine | A measurement of the isoleucine in a biological specimen. |
| C177984 | ILOPRDN | Iloperidone | A measurement of the iloperidone in a biological specimen. |
| C186071 | IMIPRMN | Imipramine | A measurement of the imipramine in a biological specimen. |
| C81869 | IMMGLB | Immunoglobulin | A measurement of the total immunoglobulin in a biological specimen. |
| C147376 | IMMGLC | Immunoglobulin Light Chains | A measurement of the total immunoglobulin (kappa and lambda) light chains in a biological specimen. |
| C156517 | IMMGLCFR | Immunoglobulin Light Chains, Free | A measurement of the total free immunoglobulin (kappa and lambda) light chains in a biological specimen. |
| C116184 | INCLBOD | Inclusion Bodies | A measurement of the inclusion bodies in a biological specimen. |
| C161375 | INCLBRBC | Erythrocyte Inclusion Bodies | A measurement of the erythrocyte inclusion bodies in a biological specimen. |
| C82044 | INDICAN | Indican | A measurement of the indican present in a biological specimen. |
| C81987 | INGAPAB | Islet Neogenesis Assoc Protein Antibody | A measurement of the islet neogenesis associated protein antibody in a biological specimen. |
| C82020 | INHIBINA | Inhibin A | A measurement of the inhibin A in a biological specimen. |
| C96681 | INHIBINB | Inhibin B | A measurement of the inhibin B in a biological specimen. |
| C98748 | INLCLR | Inulin Clearance | A measurement of the volume of serum or plasma that would be cleared of inulin by excretion of urine for a specified unit of time (e.g. one minute). |
| C64805 | INR | Prothrombin Intl. Normalized Ratio | A ratio that represents the prothrombin time for a plasma specimen, divided by the result for a control plasma specimen, further standardized for the International Sensitivity Index of the tissue factor (thromboplastin) used in the test. |
| C119286 | INSAAB | Insulin Autoantibody | A measurement of the antibody to endogenous insulin in a biological specimen. |
| C119287 | INSAB | Insulin Antibody | A measurement of the antibody to insulin in a biological specimen. |
| C147377 | INSLNFR | Insulin, Free | A measurement of the free insulin in a biological specimen. |
| C74788 | INSULIN | Insulin | A measurement of the insulin in a biological specimen. |
| C186072 | INSULINI | Insulin, Intact | A measurement of the intact insulin in a biological specimen. |
| C123458 | INSULINR | Insulin Resistance | A measurement of the insulin resistance (a cell's inability to respond to insulin) in a biological specimen. |
| C123459 | INSULINS | Insulin Sensitivity | A measurement of the insulin sensitivity (cells are stimulated by lower than normal insulin levels) in a biological specimen. |
| C74805 | INTLK1 | Interleukin 1 | A measurement of the interleukin 1 in a biological specimen. |
| C74806 | INTLK10 | Interleukin 10 | A measurement of the interleukin 10 in a biological specimen. |
| C74807 | INTLK11 | Interleukin 11 | A measurement of the interleukin 11 in a biological specimen. |
| C74808 | INTLK12 | Interleukin 12; Interleukin 12 p70 | A measurement of the interleukin 12 in a biological specimen. |
| C127623 | INTLK12B | Interleukin 12 Beta; Interleukin 12 Beta Subunit; Interleukin 12 p40; Interleukin 12 p40 Subunit | A measurement of p40 subunit of Interleukin 12 in a biological specimen. |
| C74809 | INTLK13 | Interleukin 13 | A measurement of the interleukin 13 in a biological specimen. |
| C74810 | INTLK14 | Interleukin 14 | A measurement of the interleukin 14 in a biological specimen. |
| C74811 | INTLK15 | Interleukin 15 | A measurement of the interleukin 15 in a biological specimen. |
| C74812 | INTLK16 | Interleukin 16 | A measurement of the interleukin 16 in a biological specimen. |
| C74813 | INTLK17 | IL-17A; Interleukin 17; Interleukin 17A | A measurement of the interleukin 17 in a biological specimen. |
| C74814 | INTLK18 | Interleukin 18 | A measurement of the interleukin 18 in a biological specimen. |
| C74815 | INTLK19 | Interleukin 19 | A measurement of the interleukin 19 in a biological specimen. |
| C122131 | INTLK1A | Interleukin 1 Alpha | A measurement of interleukin 1 alpha in a biological specimen. |
| C112323 | INTLK1B | IL-1B; IL1Beta; Interleukin 1 Beta; Interleukin 1B | A measurement of interleukin 1 beta in a biological specimen. |
| C112324 | INTLK1RA | IL-1RA; Interleukin 1 Receptor Antagonist | A measurement of the interleukin 1 receptor antagonist in a biological specimen. |
| C74816 | INTLK2 | Interleukin 2 | A measurement of the interleukin 2 in a biological specimen. |
| C74817 | INTLK20 | Interleukin 20 | A measurement of the interleukin 20 in a biological specimen. |
| C74818 | INTLK21 | Interleukin 21 | A measurement of the interleukin 21 in a biological specimen. |
| C74819 | INTLK22 | Interleukin 22 | A measurement of the interleukin 22 in a biological specimen. |
| C74820 | INTLK23 | Interleukin 23; Interleukin 23 p59 | A measurement of the interleukin 23 in a biological specimen. |
| C74821 | INTLK24 | Interleukin 24 | A measurement of the interleukin 24 in a biological specimen. |
| C74822 | INTLK25 | Interleukin 25 | A measurement of the interleukin 25 in a biological specimen. |
| C74823 | INTLK26 | Interleukin 26 | A measurement of the interleukin 26 in a biological specimen. |
| C74824 | INTLK27 | Interleukin 27 | A measurement of the interleukin 27 in a biological specimen. |
| C74825 | INTLK28 | Interleukin 28 | A measurement of the interleukin 28 in a biological specimen. |
| C74826 | INTLK29 | Interleukin 29 | A measurement of the interleukin 29 in a biological specimen. |
| C74827 | INTLK3 | Interleukin 3 | A measurement of the interleukin 3 in a biological specimen. |
| C74828 | INTLK30 | Interleukin 30 | A measurement of the interleukin 30 in a biological specimen. |
| C74829 | INTLK31 | Interleukin 31 | A measurement of the interleukin 31 in a biological specimen. |
| C74830 | INTLK32 | Interleukin 32 | A measurement of the interleukin 32 in a biological specimen. |
| C74831 | INTLK33 | Interleukin 33 | A measurement of the interleukin 33 in a biological specimen. |
| C74832 | INTLK4 | Interleukin 4 | A measurement of the interleukin 4 in a biological specimen. |
| C74833 | INTLK5 | Interleukin 5 | A measurement of the interleukin 5 in a biological specimen. |
| C74834 | INTLK6 | Interleukin 6 | A measurement of the interleukin 6 in a biological specimen. |
| C74835 | INTLK7 | Interleukin 7 | A measurement of the interleukin 7 in a biological specimen. |
| C74836 | INTLK8 | Interleukin 8 | A measurement of the interleukin 8 in a biological specimen. |
| C74837 | INTLK9 | Interleukin 9 | A measurement of the interleukin 9 in a biological specimen. |
| C125945 | INULIN | Inulin | A measurement of the inulin in a biological specimen. |
| C181193 | IODINE | Iodine | A measurement of the total iodine in a biological specimen. |
| C181445 | IODINEFR | Iodine, Free | A measurement of the free (unbound) iodine in a biological specimen. |
| C100439 | IOHEXCLR | Iohexol Clearance | A measurement of the volume of serum or plasma that would be cleared of Iohexol by excretion of urine for a specified unit of time (e.g. one minute). |
| C125946 | IOHEXOL | Iohexol | A measurement of iohexol in a biological specimen. |
| C98749 | IOTCLR | Iothalamate Clearance | A measurement of the volume of serum or plasma that would be cleared of iothalamate by excretion of urine for a specified unit of time (e.g. one minute). |
| C98750 | IOTCLRBS | Iothalamate Clearance Adjusted for BSA | A measurement of the volume of serum or plasma that would be cleared of iothalamate by excretion of urine for a specified unit of time (e.g. one minute), adjusted for body surface area. |
| C102276 | IRF | Immature Reticulocyte Fraction | A measurement of the immature reticulocyte fraction present in a biological specimen. |
| C74679 | IRON | FE; Iron | A measurement of the iron in a biological specimen. |
| C150819 | IRONEXR | Iron Excretion Rate | A measurement of the amount of iron being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C163461 | ISG15 | ISG15 Ubiquitin-Like Modifier; Ubiquitin-Like Protein ISG15 | A measurement of the ubiquitin-like protein ISG15 in a biological specimen. |
| C80180 | ISOPRF2 | F2-Isoprostane | A measurement of the F2-isoprostane in a biological specimen. |
| C100459 | JO1AB | Jo-1 Antibody | A measurement of the Jo-1 antibody in a biological specimen. |
| C184542 | JWH018 | JWH-018; JWH018 | A measurement of the synthetic cannabinoid JWH-018 in a biological specimen. |
| C184543 | JWH073 | JWH-073; JWH073 | A measurement of the synthetic cannabinoid JWH-073 in a biological specimen. |
| C184546 | JWH081 | JWH-081; JWH081 | A measurement of the synthetic cannabinoid JWH-081 in a biological specimen. |
| C184547 | JWH122 | JWH-122; JWH122 | A measurement of the synthetic cannabinoid JWH-122 in a biological specimen. |
| C184544 | JWH200 | JWH-200; JWH200 | A measurement of the synthetic cannabinoid JWH-200 in a biological specimen. |
| C184545 | JWH250 | JWH-250; JWH250 | A measurement of the synthetic cannabinoid JWH-250 in a biological specimen. |
| C184548 | JWH398 | JWH-398; JWH398 | A measurement of the synthetic cannabinoid JWH-398 in a biological specimen. |
| C64853 | K | Potassium | A measurement of the potassium in a biological specimen. |
| C147379 | KAPPALC | Kappa Light Chain | A measurement of the total kappa light chains in a biological specimen. |
| C184549 | KBEMIDON | Ketobemidone | A measurement of the ketobemidone in a biological specimen. |
| C106560 | KCLR | Potassium Clearance | A measurement of the volume of serum or plasma that would be cleared of potassium by excretion of urine for a specified unit of time (e.g. one minute). |
| C79462 | KCREAT | Potassium/Creatinine | A relative measurement (ratio or percentage) of the potassium to creatinine in a biological specimen. |
| C147380 | KERAT | Keratocyte | A measurement of the keratocytes in a biological specimen. |
| C184587 | KETAMINE | Ketamine | A measurement of the ketamine in a biological specimen. |
| C111239 | KETONEBD | Ketone Bodies | A measurement of the ketone bodies (acetone, acetoacetic acid, beta-hydroxybutyric acid, beta-ketopentanoate and beta-hydroxypentanoate) in a biological specimen. |
| C64854 | KETONES | Ketones | A measurement of the ketones in a biological specimen. |
| C150820 | KEXR | Potassium Excretion Rate | A measurement of the amount of potassium being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C123557 | KI67 | Ki-67; KI67; MKI67; pKi-67 | A measurement of the Ki-67 protein in a biological specimen. |
| C100433 | KIM1 | Hepatitis A Virus Cellular Receptor 1; Kidney Injury Molecule-1; KIM-1 | A measurement of the kidney injury molecule-1 (Kim-1) in a biological specimen. |
| C177955 | KIM1CRT | Kidney Injury Molecule-1/Creatinine | A relative measurement (ratio or percentage) of the kidney injury molecule-1 to creatinine in a biological specimen. |
| C163462 | KIM1EXR | Kidney Injury Molecule-1 Excretion Rate | A measurement of the amount of kidney injury molecule-1 being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C165971 | KIM1S | Soluble Hepatitis A Virus Cellular Receptor 1; Soluble Kidney Injury Molecule-1; Soluble KIM-1 | A measurement of the soluble kidney injury molecule-1 in a biological specimen. |
| C154724 | KL6 | KL-6; Krebs von den Lungen-6 Antigen | A measurement of the Krebs von den Lungen-6 in a biological specimen. |
| C98730 | KLCFR | Bence-Jones, Kappa; Kappa Light Chain, Free | A measurement of the free kappa light chain in a biological specimen. |
| C161351 | KLCLLC | Kappa Lambda Ratio; Kappa Light Chain/Lambda Light Chain | A relative measurement (ratio) of the total kappa light chain to total lambda light chain in a biological specimen. |
| C98731 | KLCLLCFR | Kappa Lt Chain,Free/Lambda Lt Chain,Free | A relative measurement (ratio or percentage) of the free kappa light chain to the free lambda light chain in a biological specimen. |
| C132372 | KLHIGGAB | Keyhole Limpet Hemocyanin IgG Antibody | A measurement of the keyhole limpet hemocyanin IgG antibody in a biological specimen. |
| C132373 | KLHIGMAB | Keyhole Limpet Hemocyanin IgM Antibody | A measurement of the keyhole limpet hemocyanin IgM antibody in a biological specimen. |
| C132374 | KLK2 | Kallikrein-2 | A measurement of the kallikrein-2 in a biological specimen. |
| C127624 | KLOTHO | Klotho | A measurement of the total klotho protein in a biological specimen. |
| C96688 | KRCYMG | Megakaryocytes | A measurement of the megakaryocytes per unit of a biological specimen. |
| C98867 | KRCYMGCE | Megakaryocytes/Total Cells | A relative measurement (ratio or percentage) of the megakaryocytes to total cells in a biological specimen (for example a bone marrow specimen). |
| C154722 | KRCYMGLE | Megakaryocytes/Leukocytes | A relative measurement (ratio or percentage) of the megakaryocytes to leukocytes in a biological specimen. |
| C186073 | KTANST11 | 11-Ketoandrosterone | A measurement of the 11-ketoandrosterone in a biological specimen. |
| C189519 | KTBDEXR | Ketone Bodies Excretion Rate | A measurement of the amount of ketone bodies being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C186074 | KTETCL11 | 11-Ketoetiocholanolone | A measurement of the 11-ketoetiocholanolone in a biological specimen. |
| C186075 | KTGSTR17 | 17-Ketogenic steroids | A measurement of the total 17-ketogenic steroids in a biological specimen. |
| C186076 | KTSTR17 | 17-Ketosteroids | A measurement of the total 17-ketosteroids in a biological specimen. |
| C96682 | KURLOFCE | Kurloff Cells | A measurement of the large secretory granule-containing immune cells in a biological specimen taken from members of certain genera of the Caviidae family. |
| C154740 | KYNURNN | Kynurenine | A measurement of the kynurenine in a biological specimen. |
| C184641 | LACOSMD | Lacosamide | A measurement of the lacosamide in a biological specimen. |
| C79450 | LACTICAC | 2-hydroxypropanoic acid; Lactate; Lactic Acid | A measurement of the lactic acid in a biological specimen. |
| C186077 | LACTOSE | Lactose | A measurement of the lactose in a biological specimen. |
| C154741 | LACTULOS | Lactulose | A measurement of the lactulose in a biological specimen. |
| C172504 | LAG3S | Soluble CD223 Antigen; Soluble LAG-3; Soluble Lymphocyte Activation Gene 3 Protein; Soluble Lymphocyte Activation Gene-3 | A measurement of the soluble lymphocyte activation gene-3 protein in a biological specimen. |
| C125947 | LAM | Lipoarabinomannan | A measurement of the lipoarabinomannan in a biological specimen. |
| C122132 | LAP | Leucine Aminopeptidase | A measurement of the total leucine aminopeptidase present in a biological specimen. |
| C189508 | LAPOB | LDL Apolipoprotein B | A measurement of the apolipoprotein B in the low density lipoprotein fraction of a biological specimen. |
| C176240 | LCHLCM | Lithocholate Compounds; Lithocholic Acid Compounds | A measurement of the lithocholic acid, glycolithocholic acid, and taurolithocholic acid in a biological specimen. |
| C176307 | LCHT | Lithocholate; Lithocholic Acid | A measurement of the lithocholate in a biological specimen. |
| C106539 | LCN2 | Lipocalin-2; Neutrophil Gelatinase-Associated Lipocalin; NGAL; Oncogene 24p3 | A measurement of lipocalin-2 in a biological specimen. |
| C106540 | LCN2CREA | Lipocalin-2/Creatinine; Neutrophil Gelatinase-Associated Lipocalin/Creatinine; NGAL/Creatinine | A relative measurement (ratio or percentage) of the lipocalin-2 to creatinine present in a sample. |
| C147381 | LCTHSPGM | Lecithin/Sphingomyelin; LS Ratio | A relative measurement (ratio) of the lecithin to sphingomyelin in a biological specimen. |
| C64855 | LDH | Lactate Dehydrogenase | A measurement of the lactate dehydrogenase in a biological specimen. |
| C74887 | LDH1 | LDH Isoenzyme 1 | A measurement of the lactate dehydrogenase isoenzyme 1 in a biological specimen. |
| C79451 | LDH1LDH | LDH Isoenzyme 1/LDH | A relative measurement (ratio or percentage) of the lactate dehydrogenase isoenzyme 1 to total lactate dehydrogenase in a biological specimen. |
| C74888 | LDH2 | LDH Isoenzyme 2 | A measurement of the lactate dehydrogenase isoenzyme 2 in a biological specimen. |
| C79452 | LDH2LDH | LDH Isoenzyme 2/LDH | A relative measurement (ratio or percentage) of the lactate dehydrogenase isoenzyme 2 to total lactate dehydrogenase in a biological specimen. |
| C74889 | LDH3 | LDH Isoenzyme 3 | A measurement of the lactate dehydrogenase isoenzyme 3 in a biological specimen. |
| C79453 | LDH3LDH | LDH Isoenzyme 3/LDH | A relative measurement (ratio or percentage) of the lactate dehydrogenase isoenzyme 3 to total lactate dehydrogenase in a biological specimen. |
| C74890 | LDH4 | LDH Isoenzyme 4 | A measurement of the lactate dehydrogenase isoenzyme 4 in a biological specimen. |
| C79454 | LDH4LDH | LDH Isoenzyme 4/LDH | A relative measurement (ratio or percentage) of the lactate dehydrogenase isoenzyme 4 to total lactate dehydrogenase in a biological specimen. |
| C74891 | LDH5 | LDH Isoenzyme 5 | A measurement of the lactate dehydrogenase isoenzyme 5 in a biological specimen. |
| C79455 | LDH5LDH | LDH Isoenzyme 5/LDH | A relative measurement (ratio or percentage) of the lactate dehydrogenase isoenzyme 5 to total lactate dehydrogenase in a biological specimen. |
| C79449 | LDHCREAT | Lactate Dehydrogenase/Creatinine | A relative measurement (ratio or percentage) of the lactate dehydrogenase to creatinine in a biological specimen. |
| C165972 | LDHEXR | Lactate Dehydrogenase Excretion Rate | A measurement of the amount of lactate dehydrogenase being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C105588 | LDL | LDL Cholesterol | A measurement of the low density lipoprotein cholesterol in a biological specimen. |
| C121182 | LDLHDL | LDL Cholesterol/HDL Cholesterol | A relative measurement (ratio) of the low density lipoprotein cholesterol to high density lipoprotein cholesterol in a biological specimen. |
| C119288 | LDLOXAB | Oxidized LDL Cholesterol Antibody | A measurement of the total oxidized low density lipoprotein cholesterol antibody in a biological specimen. |
| C120635 | LDLOXI | Oxidized LDL Cholesterol | A measurement of the oxidized low density lipoprotein cholesterol in a biological specimen. |
| C120636 | LDLP | LDL Particles | A measurement of the concentration of the total LDL particles in a biological specimen. |
| C120637 | LDLPATT | LDL Subtype Pattern | A description of the low density lipoprotein particle pattern (an interpretation of the amounts of LDL particles based on size and density) in a biological specimen. |
| C103412 | LDLPSZ | LDL Particle Size | A measurement of the average particle size of low-density lipoprotein in a biological specimen. |
| C189506 | LDLT | LDL Triglyceride | A measurement of the low density lipoprotein triglyceride in a biological specimen. |
| C147382 | LEAD | Lead; Pb | A measurement of the lead in a biological specimen. |
| C127625 | LEIM | Immature Leukocytes | A measurement of the immature leukocytes in a biological specimen. |
| C127626 | LEIMLE | Immature Leukocytes/Leukocytes | A relative measurement (ratio or percentage) of the immature leukocytes to leukocytes in a biological specimen. |
| C74866 | LEPTIN | Leptin | A measurement of the leptin hormone in a biological specimen. |
| C174293 | LEPTO | Leptocytes | A measurement of the leptocytes in a biological specimen. |
| C122133 | LEU | Leucine | A measurement of the leucine in a biological specimen. |
| C64856 | LEUKASE | Leukocyte Esterase | A measurement of the enzyme which indicates the presence of white blood cells in a biological specimen. |
| C116195 | LEUKCE | Leukemic Cells; Residual Leukemic Cells | A measurement of the leukemic cells in a biological specimen. |
| C147383 | LEUKCRBC | Leukocytes Corrected for Nucleated Erythrocytes; Leuks Corrected for Nucl Erythrocytes | A measurement of the leukocytes corrected for nucleated erythrocytes in a biological specimen. |
| C79467 | LGLUCLE | Large Unstained Cells/Leukocytes | A relative measure (ratio or percentage) of the large unstained cells to leukocytes in a biological specimen. |
| C74659 | LGUNSCE | Large Unstained Cells | A measurement of the large, peroxidase-negative cells which cannot be further characterized (i.e. as large lymphocytes, virocytes, or stem cells) present in a biological specimen. |
| C74790 | LH | Luteinizing Hormone; Lutropin | A measurement of the luteinizing hormone in a biological specimen. |
| C130163 | LIF | Leukemia Inhibitory Factor | A measurement of leukemia inhibitory factor in a biological specimen. |
| C117840 | LIPASEG | Gastric Triacylglycerol Lipase; Lipase, Gastric; LIPF | A measurement of the gastric triacylglycerol lipase in a biological specimen. |
| C187808 | LIPASEH | Hepatic Triacylglycerol Lipase; Lipase, Hepatic; LIPH | A measurement of the hepatic triacylglycerol lipase in a biological specimen. |
| C117841 | LIPASEP | Lipase, Pancreatic; Pancreatic Triacylglycerol Lipase; PNLIP | A measurement of the pancreatic triacylglycerol lipase in a biological specimen. |
| C117748 | LIPASET | Lipase; Total Lipase; Triacylglycerol Lipase | A measurement of the total triacylglycerol lipase in a biological specimen. |
| C117842 | LIPASLAL | Acid Cholesteryl Ester Hydrolase; LAL; LIPA; Lipase, Lysosomal Acid; Lysosomal Lipase | A measurement of the lysosomal acid lipase in a biological specimen. |
| C111242 | LIPEMIAI | Lipemia; Lipemic Index | A measurement of the abnormally high concentration of lipid in a biological specimen. |
| C74949 | LIPID | Lipid; Total Lipid | A measurement of the total lipids (cholesterol, lipoproteins, and triglycerides) in a biological specimen. |
| C142284 | LIQUFT | Liquefaction Time | A measurement of the time it takes for a gelatinous or semi-solid substance to change to a liquid. |
| C189505 | LITHIUM | Lithium | A measurement of the lithium in a biological specimen. |
| C96683 | LKM1AB | Liver Kidney Microsomal Type 1 Antibody; LKM-1 | A measurement of the liver kidney microsomal type 1 antibody in a biological specimen. |
| C100456 | LKM1IAAB | Liver Kidney Microsomal Type 1 IgA Ab | A measurement of the liver kidney microsomal type 1 IgA antibodies in a biological specimen. |
| C100454 | LKM1IGAB | Liver Kidney Microsomal Type 1 IgG Ab | A measurement of the liver kidney microsomal type 1 IgG antibodies in a biological specimen. |
| C100455 | LKM1IMAB | Liver Kidney Microsomal Type 1 IgM Ab | A measurement of the liver kidney microsomal type 1 IgM antibodies in a biological specimen. |
| C98732 | LLCFR | Bence-Jones, Lambda; Lambda Light Chain, Free | A measurement of the free lambda light chain in a biological specimen. |
| C147384 | LMBDLC | Lambda Light Chain | A measurement of the total lambda light chains in a biological specimen. |
| C184621 | LOPRAZLM | Loprazolam | A measurement of the loprazolam in a biological specimen. |
| C177977 | LOXAPN | Loxapine | A measurement of the loxapine in a biological specimen. |
| C82022 | LPA | Lipoprotein-a | A measurement of the lipoprotein-a in a biological specimen. |
| C174291 | LPL | Lipoprotein Lipase | A measurement of the lipoprotein lipase in a biological specimen. |
| C120638 | LPPLA2 | Lipoprotein Associated Phospholipase A2 | A measurement of the lipoprotein associated phospholipase A2 in a biological specimen. |
| C165973 | LRG1 | HMFT1766; Leucine Rich Alpha-2-Glycoprotein 1 | A measurement of the leucine rich alpha-2-glycoprotein 1 in a biological specimen. |
| C184622 | LRMZPM | Lormetazepam | A measurement of the lormetazepam in a biological specimen. |
| C75374 | LRZPM | Lorazepam | A measurement of the lorazepam present in a biological specimen. |
| C75354 | LSD | Acid; Lysergate Diethylamide; Lysergic Acid Diethylamide | A measurement of the lysergic acid diethylamine (LSD) in a biological specimen. |
| C172495 | LSELS | sL-Selectin; Soluble CD62L; Soluble L-Selectin | A measurement of the soluble L-selectin in a biological specimen. |
| C132375 | LTA | Lymphotoxin Alpha; TNF-beta; Tumor Necrosis Factor Beta | A measurement of the lymphotoxin alpha in a biological specimen. |
| C103413 | LTB4 | Leukotriene B4 | A measurement of the leukotriene B4 in a biological specimen. |
| C189516 | LTC4SN | Leukotriene C4 Synthase | A measurement of the leukotriene C4 synthase in a biological specimen. |
| C103414 | LTD4 | Leukotriene D4 | A measurement of the leukotriene D4 in a biological specimen. |
| C103415 | LTE4 | Leukotriene E4 | A measurement of the leukotriene E4 in a biological specimen. |
| C82021 | LTF | Lactoferrin; Lactotransferrin | A measurement of the lactoferrin in a biological specimen. |
| C120639 | LTFAB | Lactoferrin Antibody | A measurement of the lactoferrin antibody in a biological specimen. |
| C177963 | LURASIDN | Lurasidone | A measurement of the lurasidone in a biological specimen. |
| C147385 | LVFBRSC | Liver Fibrosis Score | A scoring system that evaluates liver pathology through the assessment of multiple blood test parameters, taking into account additional demographic factors such as the age and/or gender of the subject. |
| C184572 | LVRPHNL | Levorphanol | A measurement of the levorphanol in a biological specimen. |
| C147386 | LVTRCTM | Levetiracetam | A measurement of the levetiracetam in a biological specimen. |
| C163463 | LY6E | Lymphocyte Antigen 6 Family Member E; Lymphocyte Antigen 6E | A measurement of the lymphocyte antigen 6E in a biological specimen. |
| C51949 | LYM | Lymphocytes | A measurement of the lymphocytes in a biological specimen. |
| C119289 | LYMA | Lymphocytes Activated | A measurement of the total activated lymphocytes in a biological specimen. |
| C64818 | LYMAT | Lymphocytes Atypical; Lymphocytes, Variant; Reactive Lymphocytes | A measurement of the atypical lymphocytes in a biological specimen. |
| C64819 | LYMATLE | Lymphocytes Atypical/Leukocytes; Lymphocytes, Variant/Leukocytes; Reactive Lymphocytes/Leukocytes | A relative measurement (ratio or percentage) of the atypical lymphocytes to leukocytes in a biological specimen. |
| C74654 | LYMATLY | Atypical Lymphocytes/Lymphocytes; Lymphocytes Atypical/Lymphocytes; Reactive Lymphocytes/Lymphocytes; Variant Lymphocytes/Lymphocytes | A relative measurement (ratio or percentage) of the atypical lymphocytes to all lymphocytes in a biological specimen. |
| C98751 | LYMCE | Lymphocytes/Total Cells | A relative measurement (ratio or percentage) of the lymphocytes to total cells in a biological specimen (for example a bone marrow specimen). |
| C147387 | LYMCLF | Lymphocytes, Clefted | A measurement of the clefted lymphocytes in a biological specimen. |
| C147388 | LYMCLFLE | Lymphocytes, Clefted/Leukocytes | A relative measurement (ratio or percentage) of the clefted lymphocytes to total leukocytes in a biological specimen. |
| C100444 | LYMIM | Immature Lymphocytes | A measurement of the immature lymphocytes in a biological specimen. |
| C100443 | LYMIMLE | Immature Lymphocytes/Leukocytes | A relative measurement (ratio or percentage) of the immature lymphocytes to leukocytes in a biological specimen. |
| C64820 | LYMLE | Lymphocytes/Leukocytes | A relative measurement (ratio or percentage) of the lymphocytes to leukocytes in a biological specimen. |
| C158236 | LYMLG | Large Lymphocytes | A measurement of the large lymphocytes (approximately between 10 um and 20 um in diameter) in a biological specimen. |
| C74613 | LYMMCE | Lymphoma Cells | A measurement of the malignant lymphocytes in a biological specimen. |
| C186078 | LYMMCECE | Lymphoma Cells/Total Cells | A relative measurement (ratio or percentage) of the lymphoma cells to total cells in a biological specimen. |
| C147389 | LYMMCELE | Lymphoma Cells/Leukocytes | A relative measurement (ratio or percentage) of the malignant lymphocytes to all leukocytes in a biological specimen. |
| C74910 | LYMMCELY | Lymphoma Cells/Lymphocytes | A relative measurement (ratio or percentage) of the malignant lymphocytes to all lymphocytes in a biological specimen. |
| C186079 | LYMNE | Lymphocytes/Neutrophils | A relative measurement (ratio) of lymphocytes to neutrophils in a biological specimen. |
| C135430 | LYMNSQE | Lymphocytes/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the lymphocytes to non-squamous epithelial cells in a biological specimen. |
| C139064 | LYMPHOID | Lymphoid Cells | A measurement of the total lymphoid lineage cells in a biological specimen. |
| C81955 | LYMPHOTC | Chemokine Ligand 1; Lymphotactin | A measurement of the lymphotactin in a biological specimen. |
| C74618 | LYMPL | Plasmacytoid Lymphocytes; Plymphocytes | A measurement of the plasmacytoid lymphocytes (lymphocytes with peripherally clumped chromatin and often deep blue cytoplasm, and that appear similar to plasma cells) in a biological specimen. |
| C158229 | LYMPLLE | Plasmacytoid Lymphocytes/Leukocytes | A relative measurement (ratio or percentage) of the plasmacytoid lymphocytes to all leukocytes in a biological specimen. |
| C74648 | LYMPLLY | Plasmacytoid Lymphocytes/Lymphocytes | A relative measurement (ratio or percentage) of the plasmacytoid lymphocytes (lymphocytes with peripherally clumped chromatin and often deep blue cytoplasm, and that appear similar to plasma cells) to all lymphocytes in a biological specimen. |
| C111329 | LYMVAC | Vacuolated Lymphocytes | A measurement of the vacuolated lymphocytes in a biological specimen. |
| C127627 | LYMVACLE | Vacuolated Lymphocytes/Leukocytes | A relative measurement (ratio or percentage) of the vacuolated lymphocytes to leukocytes in a biological specimen. |
| C122134 | LYS | Lysine | A measurement of the lysine in a biological specimen. |
| C184523 | LYSOGL1 | Glucopsychosine; Glucosylsphingosine; Lyso-GL1 | A measurement of the glucopsychosine in a biological specimen. |
| C120640 | LYSOZYME | Lysozyme | A measurement of lysozyme in a biological specimen. |
| C184550 | MABCHMCA | MAB-CHMINACA | A measurement of the synthetic cannabinoid MAB-CHMINACA in a biological specimen. |
| C147390 | MACROBLD | Macroscopic Blood; Visible Blood | A measurement of the blood in body products such as a urine or stool sample, and visibly detectable on gross examination. |
| C64821 | MACROCY | Macrocytes | A measurement of the macrocytes in a biological specimen. |
| C154742 | MANNITOL | Mannitol | A measurement of the mannitol in a biological specimen. |
| C111246 | MASTCE | Mast Cells; Mastocytes | A measurement of the mast cells in a biological specimen. |
| C111247 | MASTCECE | Mast Cells/Total Cells | A relative measurement (ratio or percentage) of the mast cells to total cells in a biological specimen. |
| C187812 | MASTCELE | Mast Cells/Leukocytes | A relative measurement (ratio or percentage) of mast cells to total leukocytes in a biological specimen. |
| C74614 | MAYHEG | May-Hegglin Anomaly | A measurement of the May-Hegglin anomaly in a blood sample. This anomaly is characterized by large, misshapen platelets and the presence of Dohle bodies in leukocytes. |
| C184623 | MAZINDOL | Mazindol | A measurement of the mazindol in a biological specimen. |
| C122135 | MBP | Myelin Basic Protein | A measurement of the myelin basic protein in a biological specimen. |
| C177957 | MCA2 | 2-Methylcitrate; 2-Methylcitric Acid; MCA; Methylcitrate; Methylcitric Acid | A measurement of the 2-methylcitrate in a biological specimen. |
| C184552 | MCATHNON | Ephedrone; Methcathinone | A measurement of the methcathinone in a biological specimen. |
| C64797 | MCH | Ery. Mean Corpuscular Hemoglobin | A measurement of the mean amount of hemoglobin per erythrocyte in a biological specimen, calculated as the product of hemoglobin times ten, divided by the number of erythrocytes. |
| C64798 | MCHC | Ery. Mean Corpuscular HGB Concentration | An indirect measurement of the average concentration of hemoglobin per erythrocyte in a biological specimen, calculated as the ratio of hemoglobin to hematocrit. |
| C82025 | MCP1 | CCL2; Chemokine (C-C Motif) Ligand 2; Monocyte Chemotactic Protein 1 | A measurement of the monocyte chemotactic protein 1 in a biological specimen. |
| C74798 | MCPHG | Macrophages | A measurement of the macrophages in a biological specimen. |
| C111244 | MCPHGCE | Macrophages/Total Cells | A relative measurement (ratio or percentage) of the macrophages to total cells in a biological specimen. |
| C123460 | MCPHGLE | Macrophages/Leukocytes | A relative measurement (ratio or percentage) of the macrophages to leukocytes in a biological specimen. |
| C135431 | MCPHNSQE | Macrophages/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the macrophages to non-squamous epithelial cells in a biological specimen. |
| C92291 | MCPROT | Abnormal Gamma Protein Band; M Protein; M-Spike Paraprotein; M-Spike Protein; Monoclonal Immunoglobulin Protein; Monoclonal Protein; Monoclonal Protein Spike; Myeloma Protein; Paraprotein | A measurement of homogenous immunoglobulin resulting from the proliferation of a single clone of plasma cells in a biological specimen. |
| C80191 | MCSF | Macrophage Colony Stimulating Factor | A measurement of the macrophage colony stimulating factor in a biological specimen. |
| C64799 | MCV | Ery. Mean Corpuscular Volume; Erythrocytes Mean Corpuscular Volume; RBC Mean Corpuscular Volume | A measurement of the mean cellular volume per erythrocyte in a biological specimen. |
| C114215 | MCVRETIC | MCV Reticulocytes; MCVr; Mean Corpuscular Volume Reticulocytes | A measurement of the mean volume of reticulocytes in a biological specimen. |
| C174294 | MDA | 3,4-methylenedioxyamphetamine | A measurement of the 3,4-methylenedioxyamphetamine in a biological specimen. |
| C187811 | MDALD | Malondialdehyde; MDA | A measurement of the malondialdehyde in a biological specimen. |
| C81956 | MDC | C-C Motif Chemokine Ligand 22; CCL22; Chemokine (C-C Motif) Ligand 22; Chemokine Ligand 22; Macrophage-Derived Chemokine | A measurement of the macrophage-derived chemokine in a biological specimen. |
| C174295 | MDEA | 3,4-methylenedioxy-N-ethylamphetamine; Eve; MDE | A measurement of the 3,4-methylenedioxy-N-ethylamphetamine in a biological specimen. |
| C75359 | MDMA | 3,4-methylenedioxymethamphetamine; Ecstasy | A measurement of the 3,4-methylenedioxymethamphetamine (MDMA) in a biological specimen. |
| C139083 | MDZLM | Midazolam | A measurement of the midazolam present in a biological specimen. |
| C139079 | MDZPM | Medazepam | A measurement of the medazepam present in a biological specimen. |
| C147391 | MECONIUM | Meconium | A measurement of the meconium in a biological specimen. |
| C111250 | MENGL | Meningeal Cells | A measurement of the mengingeal cells in a biological specimen. |
| C111251 | MENGLCE | Meningeal Cells/Total Cells | A relative measurement (ratio or percentage) of the meningeal cells to total cells in a biological specimen. |
| C147392 | MEPRDN | Meperidine | A measurement of the meperidine in a biological specimen. |
| C127628 | MERCECE | Erythroid Precursors/Total Cells; Maturing Erythroid Cells/Total Cells; Maturing Erythroid/Total Cells; Total Erythroid Precursors/Total Cells | A relative measurement (ratio or percentage) of the maturing erythroid cells to total cells in a biological specimen. |
| C147393 | MERCURY | Hg; Mercury | A measurement of the mercury in a biological specimen. |
| C75355 | MESCALIN | 3,4,5-trimethoxyphenethylamine; Mescaline | A measurement of the mescaline in a biological specimen. |
| C177979 | MESORDZN | Mesoridazine | A measurement of the mesoridazine in a biological specimen. |
| C122238 | MET | Methionine | A measurement of the methionine in a biological specimen. |
| C74615 | METAMY | Metamyelocytes | A measurement of the metamyelocytes (small, myelocytic neutrophils with an indented nucleus) in a biological specimen. |
| C98754 | METAMYCE | Metamyelocytes/Total Cells | A relative measurement (ratio or percentage ) of the metamyelocytes (small, myelocytic neutrophils with an indented nucleus) to total cells in a biological specimen (for example a bone marrow specimen). |
| C74645 | METAMYLE | Metamyelocytes/Leukocytes | A relative measurement (ratio or percentage) of the metamyelocytes (small, myelocytic neutrophils with an indented nucleus) to all leukocytes in a biological specimen. |
| C116198 | METANEPH | Metadrenaline; Metanephrine | A measurement of the metanephrine in a biological specimen. |
| C163468 | METANEXR | Metanephrine Excretion Rate | A measurement of the amount of metanephrine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C128971 | METARBCE | Metarubricyte/Total Cells | A relative measurement (ratio or percentage) of the metarubricytes to total cells in a biological specimen. |
| C165974 | METARBLE | Metarubricytes/Leukocytes | A relative measurement (ratio or percentage) of the metarubricytes to leukocytes in a biological specimen. |
| C128972 | METARUB | Acidophilic Erythroblast; Metarubricyte; Orthochromatophilic Normoblast; Orthochromic Erythroblast; Orthochromic Normoblast | A measurement of the metarubricytes in a biological specimen. |
| C187814 | METASE | Methyltransferase | A measurement of the total methyltransferase in a biological specimen. |
| C75348 | METHAMPH | Methamphetamine | A measurement of the methamphetamine drug present in a biological specimen. |
| C186080 | METHANE | CH4; Methane | A measurement of the methane in a biological specimen. |
| C147394 | METHANOL | Methanol | A measurement of the methanol in a biological specimen. |
| C74881 | METHDN | Methadone | A measurement of the methadone present in a biological specimen. |
| C170581 | METHPHEN | Methylphenidate | A measurement of the methylphenidate in a biological specimen. |
| C74882 | METHQLDN | Methaqualone | A measurement of the methaqualone present in a biological specimen. |
| C184624 | MFENRX | Mefenorex | A measurement of the mefenorex in a biological specimen. |
| C64840 | MG | Magnesium | A measurement of the magnesium in a biological specimen. |
| C79436 | MGB | Myoglobin | A measurement of myoglobin in a biological specimen. |
| C106546 | MGBCREAT | Myoglobin/Creatinine | A relative measurement (ratio or percentage) of the myoglobin to creatinine present in a sample. |
| C79456 | MGCREAT | Magnesium/Creatinine | A relative measurement (ratio or percentage) of the magnesium to creatinine in a biological specimen. |
| C175951 | MGION | Magnesium, Ionized | A measurement of the ionized magnesium in a biological specimen. |
| C172502 | MICA | MHC Class I Chain Related Protein A | A measurement of the MHC class I chain related protein A in a biological specimen. |
| C64822 | MICROCY | Microcytes | A measurement of the microcytes in a biological specimen. |
| C116199 | MIDCEF | Mid Cell Fraction; Mid Cells | A measurement of the mid cell fraction, including eosinophils, basophils, monocytes and other precursor white blood cells, in a biological specimen. |
| C163464 | MIP1 | Macrophage Inflammatory Protein 1 | A measurement of total macrophage inflammatory protein 1 in a biological specimen. |
| C82023 | MIP1A | Chemokine Ligand 3; Macrophage Inflammatory Protein 1 Alpha | A measurement of the macrophage inflammatory protein 1 alpha in a biological specimen. |
| C82024 | MIP1B | Chemokine Ligand 4; Macrophage Inflammatory Protein 1 Beta | A measurement of the macrophage inflammatory protein 1 beta in a biological specimen. |
| C130164 | MIP1G | Macrophage Inflammatory Protein 1 Gamma | A measurement of the macrophage inflammatory protein 1 gamma in a biological specimen. |
| C147395 | MITOM2AB | Mitochondrial M2 Antibody | A measurement of the mitochondrial antibodies of M2 specificity in a biological specimen. |
| C135432 | MKCMKBMP | Megakaryocyte and Megakaryoblast Morph; Megakaryocyte and Megakaryoblast Morphology | An examination or assessment of the form and structure of megakaryoblasts and megakaryocytes. |
| C74867 | MLATONIN | Melatonin | A measurement of the melatonin hormone in a biological specimen. |
| C74660 | MLIGCE | Malignant Cells, NOS | A measurement of the malignant cells of all types in a biological specimen. |
| C74643 | MLIGCEBC | Malignant Cells, NOS/Blood Cells | A relative measurement (ratio or percentage) of the malignant cells of all types to all blood cells in a biological specimen. |
| C187815 | MLNCPRN | Milnacipran | A measurement of the milnacipran in a biological specimen. |
| C16790 | MLR | Mixed Leukocyte Reaction; Mixed Lymphocyte Reaction | A measurement of the histocompatibility at the HL-A locus between two populations of lymphocytes taken from two separate individuals. |
| C163465 | MM2IGAB | Mitochondrial M2 IgG Antibody | A measurement of the mitochondrial IgG antibodies of M2 specificity in a biological specimen. |
| C96690 | MMA | Methylmalonate; Methylmalonic Acid | A measurement of the methylmalonic acid in a biological specimen. |
| C181407 | MMARG | Monomethylarginine; Tilarginine | A measurement of the monomethylarginine in a biological specimen. |
| C163466 | MMIF | Macrophage Migration Inhibitory Factor; MIF | A measurement of the macrophage migration inhibitory factor in a biological specimen. |
| C80192 | MMP1 | Interstitial Collagenase; Matrix Metalloproteinase 1 | A measurement of the matrix metalloproteinase 1 in a biological specimen. |
| C80193 | MMP2 | Gelatinase A; Matrix Metalloproteinase 2 | A measurement of the matrix metalloproteinase 2 in a biological specimen. |
| C80194 | MMP3 | Matrix Metalloproteinase 3; Stromelysin 1 | A measurement of the matrix metalloproteinase 3 in a biological specimen. |
| C80195 | MMP7 | Matrilysin; Matrix Metalloproteinase 7 | A measurement of the matrix metalloproteinase 7 in a biological specimen. |
| C80196 | MMP8 | Matrix Metalloproteinase 8; Neutrophil Collagenase | A measurement of the matrix metalloproteinase 8 in a biological specimen. |
| C80197 | MMP9 | Gelatinase B; Matrix Metalloproteinase 9 | A measurement of the matrix metalloproteinase 9 in a biological specimen. |
| C127629 | MMYCECE | Maturing Myeloid/Total Cells | A relative measurement (ratio or percentage) of the maturing myeloid cells to total cells in a biological specimen. |
| C154757 | MNC | Mononuclear Cells; Mononucleated Cells | A measurement of the mononuclear cells in a biological specimen. |
| C187790 | MNCAT | Mononuclear Cells Atypical | A measurement of the atypical mononuclear cells in a biological specimen. |
| C187791 | MNCATLE | Mononuclear Cells Atypical/Leukocytes | A relative measurement (ratio or percentage) of the atypical mononuclear cells to leukocytes in a biological specimen. |
| C111276 | MOCYCE | Monocytoid Cells | A measurement of the monocytoid cells in a biological specimen. |
| C111277 | MOCYCECE | Monocytoid Cells/Total Cells | A relative measurement (ratio or percentage) of the monocytoid cells to total cells in a biological specimen. |
| C120641 | MOCYCELE | Monocytoid Cells/Leukocytes | A relative measurement (ratio or percentage) of the monocytoid cells to leukocytes in a biological specimen. |
| C184628 | MODAFNIL | Modafinil | A measurement of the modafinil in a biological specimen. |
| C184626 | MOHXITAL | Methohexital | A measurement of the methohexital in a biological specimen. |
| C177981 | MOLINDN | Molindone | A measurement of the molindone in a biological specimen. |
| C147396 | MONMPHLE | Monocytes and Macrophages/Leukocytes | A relative measurement (ratio or percentage) of the monocytes and macrophages to total leukocytes in a biological specimen. |
| C64823 | MONO | Monocytes | A measurement of the monocytes in a biological specimen. |
| C74631 | MONOBL | Monoblasts | A measurement of the monoblast cells in a biological specimen. |
| C187677 | MONOBLCE | Monoblasts/Total Cells | A relative measurement (ratio or percentage) of the monoblasts to total cells in a biological specimen. |
| C74646 | MONOBLLE | Monoblasts/Leukocytes | A relative measurement (ratio or percentage) of the monoblasts to leukocytes in a biological specimen. |
| C98872 | MONOCE | Monocytes/Total Cells | A relative measurement (ratio or percentage) of the monocytes to total cells in a biological specimen (for example a bone marrow specimen). |
| C96676 | MONOIM | Immature Monocytes | A measurement of the immature monocytes in a biological specimen. |
| C96677 | MONOIMLE | Immature Monocytes/Leukocytes | A relative measurement (ratio or percentage) of immature monocytes to total leukocytes in a biological specimen. |
| C64824 | MONOLE | Monocytes/Leukocytes | A relative measurement (ratio or percentage) of the monocytes to leukocytes in a biological specimen. |
| C106544 | MONOMA | Monocytes/Macrocytes | A relative measurement (ratio or percentage) of the monocytes to macrocytes present in a sample. |
| C135433 | MONONSQE | Monocytes/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the monocytes to non-squamous epithelial cells in a biological specimen. |
| C147397 | MONOPTPT | M Protein/Total Protein; M-Spike Protein/Total Protein; Monoclonal Protein Spike/Total Protein; Monoclonal Protein/Total Protein; Myeloma Protein/Total Protein | A relative measurement (ratio or percentage) of the monoclonal protein to total protein in a biological specimen. |
| C184535 | MORPHDS | Desomorphine | A measurement of the desomorphine in a biological specimen. |
| C184570 | MORPHET | Ethylmorphine | A measurement of the ethylmorphine in a biological specimen. |
| C74883 | MORPHINE | Morphine | A measurement of the morphine present in a biological specimen. |
| C184556 | MORPHNC | Nicomorphine | A measurement of the nicomorphine in a biological specimen. |
| C184557 | MORPHNR | Normorphine | A measurement of the normorphine in a biological specimen. |
| C96686 | MPC | Mean Platelet Component | A measurement of the mean platelet component (platelet activity) in a blood specimen. |
| C184551 | MPHDRN | Mephedrone | A measurement of the mephedrone in a biological specimen. |
| C75366 | MPHNBRB | Mephobarbital; Methylphenobarbital | A measurement of the methylphenobarbital in a biological specimen. |
| C186081 | MPIGISO | Immunoglobulin Immunofixation Interpretation; Monoclonal Prot Immunoglobulin Isotype; Monoclonal Protein Immunoglobulin Class; Monoclonal Protein Immunoglobulin Isotype | The identification of the monoclonal protein immunoglobulin isotype in a biological specimen. |
| C114214 | MPM | Mean Platelet Dry Mass | A measurement of the mean platelet dry mass in a biological specimen. |
| C80198 | MPO | Myeloperoxidase | A measurement of the myeloperoxidase in a biological specimen. |
| C92280 | MPOAB | Myeloperoxidase Antibody | A measurement of the myeloperoxidase antibody in a biological specimen. |
| C184625 | MPRBMATE | Meprobamate | A measurement of the meprobamate in a biological specimen. |
| C163467 | MPROTEXR | M Protein Excretion Rate; M-Spike Protein Excretion Rate; Monoclonal Protein Excretion Rate; Monoclonal Protein Spike Excretion Rate; Myeloma Protein Excretion Rate | A measurement of the amount of Monoclonal Protein being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C158218 | MPROTR | Monoclonal Protein Band Region; Monoclonal Protein Region; Monoclonal Protein Spike Region | The identification of the protein zone (e.g., alpha-1 globulin, beta globulin, etc.) within which the monoclonal protein is observed. |
| C184591 | MPRYLON | Methyprylon | A measurement of the methyprylon in a biological specimen. |
| C74730 | MPV | Mean Platelet Volume | A measurement of the average size of the platelets present in a blood sample. |
| C119290 | MPXI | Myeloperoxidase Index | The mean peroxidase activity index or staining intensity of the neutrophil population relative to the archetype. |
| C187789 | MSHA | Alpha Melanocyte Stimulating Hormone; Alpha-MSH | A measurement of the alpha melanocyte stimulating hormone in a biological specimen. |
| C147398 | MSTHCE | Mesothelial Cells | A measurement of the mesothelial cells in a biological specimen. |
| C147399 | MSTHCELE | Mesothelial Cells/Leukocytes | A relative measurement (ratio or percentage) of the mesothelial cells to total leukocytes in a biological specimen. |
| C184588 | MSTRLN | Mesterelone; Mesterolone | A measurement of the mesterolone in a biological specimen. |
| C184590 | MTESTOS | Methyltestosterone | A measurement of the methyltestosterone in a biological specimen. |
| C184589 | MTHSTRN | Methasterone | A measurement of the methasterone in a biological specimen. |
| C186082 | MTHXT3 | 3-Methoxytyramine | A measurement of the total 3-methoxytyramine in a biological specimen. |
| C186083 | MTHXT3FR | 3-Methoxytyramine, Free | A measurement of the free 3-methoxytyramine in a biological specimen. |
| C147400 | MTNEPHFR | Metanephrine, Free | A measurement of the free metanephrine in a biological specimen. |
| C177991 | MTNMTEXR | Metanephrine+Normetanephrine Excr Rate; Metanephrine+Normetanephrine Excretion Rate | A measurement of the amount of metanephrine and normetanephrine being excreted in a biological specimen over a defined amount of time (e.g., one hour). |
| C177990 | MTNNMTN | Metanephrine+Normetanephrine | A measurement of the metanephrine and normetanephrine in a biological specimen. |
| C74721 | MUCTHR | Mucous Threads | A measurement of the mucous threads present in a biological specimen. |
| C127630 | MUG | Murinoglobulin | A measurement of the murinoglobulin in a biological specimen. |
| C163469 | MX1 | Interferon-Induced GTP-Binding Protein Mx1; Interferon-Induced Protein p78 | A measurement of the interferon-induced protein P78 in a biological specimen. |
| C74632 | MYBLA | Myeloblasts | A measurement of the myeloblast cells in a biological specimen. |
| C64825 | MYBLALE | Myeloblasts/Leukocytes | A relative measurement (ratio or percentage) of the myeloblasts to leukocytes in a biological specimen. |
| C92283 | MYBLAT1 | Type I Myeloblasts | A measurement of type I myeloblast cells per unit of a biological specimen. |
| C92284 | MYBLAT2 | Type II Myeloblasts | A measurement of type II myeloblast cells per unit of a biological specimen. |
| C92285 | MYBLAT3 | Type III Myeloblasts | A measurement of type III myeloblast cells per unit of a biological specimen. |
| C135434 | MYCEMIDX | Myeloid Maturation Index | A relative measurement (ratio) of the sum of myeloid maturation phase cells (pool) to the sum of myeloid proliferative phase cells (pool) in a biological specimen. |
| C135435 | MYCEMPOL | Myeloid Maturation Pool | A measurement of the myeloid maturation phase cells (metamyelocytes, band neutrophils, and segmented neutrophils) in a biological specimen. |
| C135436 | MYCEPIDX | Myeloid Proliferation Index | A relative measurement (ratio) of the sum of myeloid proliferative phase cells (pool) to the sum of myeloid maturation phase cells (pool) in a biological specimen. |
| C135437 | MYCEPPOL | Myeloid Proliferation Pool | A measurement of the myeloid proliferative phase cells (myeloblasts, promyelocytes, and myelocytes) in a biological specimen. |
| C74662 | MYCY | Myelocytes | A measurement of the myelocytes in a biological specimen. |
| C98868 | MYCYCE | Myelocytes/Total Cells | A relative measurement (ratio or percentage) of the myelocytes to total cells in a biological specimen (for example a bone marrow specimen). |
| C64826 | MYCYLE | Myelocytes/Leukocytes | A relative measurement (ratio or percentage) of the myelocytes to leukocytes in a biological specimen. |
| C103418 | MYELINAB | Myelin Antibodies | A measurement of the myelin antibodies in a biological specimen. |
| C106547 | MYL3 | Cardiac myosin light chain 1; Myosin light chain 1, slow-twitch muscle B/ventricular isoform; Myosin Light Chain 3 | A measurement of myosin light chain 3 in a biological specimen. |
| C130165 | MYPC | Myeloid Progenitor Cells | A measurement of the myeloid progenitor cells in a biological specimen. |
| C186084 | MYPCCE | Myeloid Progenitor Cells/Total Cells | A relative measurement (ratio or percentage) of the myeloid progenitor cells to total cells in a biological specimen. |
| C92242 | MYPCERPC | Myeloid/Erythroid Ratio | A relative measurement of myeloid progenitor cells to erythrocyte precursor cells in a biological specimen. |
| C106568 | NACLR | Sodium Clearance | A measurement of the volume of serum or plasma that would be cleared of sodium by excretion of urine for a specified unit of time (e.g. one minute). |
| C79464 | NACREAT | Sodium/Creatinine | A relative measurement (ratio or percentage) of the sodium to creatinine in a biological specimen. |
| C79459 | NAG | N-Acetyl Glucosamide; N-Acetyl Glucosamine | A measurement of N-acetyl glucosamide (sugar derivative) in a biological specimen. |
| C103419 | NAGASE | Beta-N-acetyl-D-glucosaminidase; N-acetyl-beta-D-glucosaminidase | A measurement of the N-acetyl-beta-D-glucosaminidase (enzyme) in a biological specimen. |
| C163470 | NAGASECR | N-acetyl-B-D-glucosaminidase/Creatinine | A relative measurement (ratio or percentage) of the N-acetyl-beta-D-glucosaminidase to creatinine in a biological specimen. |
| C165975 | NAGASEXR | N-acetyl-beta-D-glucosaminidase Excretion Rate; NAGASE Excretion Rate | A measurement of the amount of N-acetyl-beta-D-glucosaminidase being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C79460 | NAGCREAT | N-Acetyl Glucosamide/Creatinine | A relative measurement (ratio or percentage) of the N-acetyl glucosamide to creatinine in a biological specimen. |
| C122137 | NAK | Sodium/Potassium | A relative measurement (ratio or percentage) of the sodium to potassium in a biological specimen. |
| C184592 | NALORPHN | Allorphine; Antorphine; N-allylnormorphine; Nalorphine | A measurement of the nalorphine in a biological specimen. |
| C75377 | NANDRLN | Nandrolone; Norandrostenolone; Nortestosterone | A measurement of the nandrolone in a biological specimen. |
| C184553 | NAPHYRON | Naphyrone | A measurement of the naphyrone in a biological specimen. |
| C154744 | NCCPTN | Nociceptin; Orphanin FQ | A measurement of the nociceptin in a biological specimen. |
| C184593 | NCLOSTBL | Norclostebol | A measurement of the norclostebol in a biological specimen. |
| C79437 | NCTD5P | 5 Prime Nucleotidase; 5'-Ribonucleotide Phosphohydrolase | A measurement of the 5'-nucleotidase in a biological specimen. |
| C177967 | NDMOLZPN | Desmethylolanzapine; DMO; N-Desmethylolanzapine; Norolanzapine | A measurement of the N-desmethylolanzapine in a biological specimen. |
| C163471 | NDMTASE | N-Demethylase | A measurement of the N-Demethylase in a biological specimen. |
| C181403 | NDSMT | N-Desmethyltramadol; N-DSMT | A measurement of the N-desmethyltramadol in a biological specimen. |
| C80199 | NEOPTERN | Neopterin | A measurement of the neopterin in a biological specimen. |
| C184645 | NEPHRIN | Nephrin; NPHS1 Adhesion Molecule, Nephrin | A measurement of the nephrin in a biological specimen. |
| C181450 | NEUMYLLY | Neutrophilic Myelocytes/Lymphocytes | A relative measurement (ratio or percentage) of the neutrophilic myelocytes to lymphocytes in a biological specimen (for example a bone marrow specimen). |
| C63321 | NEUT | Neutrophils | A measurement of the neutrophils in a biological specimen. |
| C116200 | NEUTAGR | Agranular Neutrophils | A measurement of the agranular neutrophils in a biological specimen. |
| C64830 | NEUTB | Neutrophils Band Form | A measurement of the banded neutrophils in a biological specimen. |
| C187701 | NEUTBCE | Neutrophils Band Form/Total Cells | A relative measurement (ratio or percentage) of the banded neutrophils to total cells in a biological specimen. |
| C64831 | NEUTBLE | Neutrophils Band Form/Leukocytes | A relative measurement (ratio or percentage) of the banded neutrophils to leukocytes in a biological specimen. |
| C120642 | NEUTBNE | Neutrophils Band Form/ Neutrophils | A relative measurement (ratio or percentage) of banded neutrophils to total neutrophils in a biological specimen. |
| C98763 | NEUTCE | Neutrophils/Total Cells | A relative measurement (ratio or percentage) of the neutrophils to total cells in a biological specimen (for example a bone marrow specimen). |
| C111166 | NEUTCYBS | Cytoplasmic Basophilia Neutrophil | A measurement of the neutrophils in a biological specimen showing a dark staining pattern in the cytoplasm due to increased acidic content. |
| C96651 | NEUTGT | Giant Neutrophils | A measurement of the giant neutrophils in a biological specimen. |
| C116201 | NEUTHYGR | Hypogranular Neutrophils | A measurement of the hypogranular neutrophils in a biological specimen. |
| C96678 | NEUTIM | Immature Neutrophils | A measurement of the total immature neutrophils in a biological specimen. |
| C100442 | NEUTIMLE | Immature Neutrophils/Leukocytes | A relative measurement (ratio or percentage) of the immature neutrophils to leukocytes in a biological specimen. |
| C64827 | NEUTLE | Neutrophils/Leukocytes | A relative measurement (ratio or percentage) of the neutrophils to leukocytes in a biological specimen. |
| C116202 | NEUTLS | Left Shift Neutrophils | An observation of the above normal incidence of immature neutrophils, including band neutrophils and neutrophil precursors in a biological specimen. |
| C141271 | NEUTLY | Neutrophils/Lymphocytes | A relative measurement (ratio) of the neutrophils to lymphocytes in a biological specimen. |
| C84822 | NEUTMM | Neutrophilic Metamyelocytes | A measurement of the neutrophilic metamyelocytes in a biological specimen. |
| C189509 | NEUTMMCE | Neutrophilic Metamyelocytes/Total Cells | A relative measurement (ratio or percentage) of the neutrophilic metamyelocytes to total cells in a biological specimen. |
| C84823 | NEUTMY | Neutrophilic Myelocytes | A measurement of the neutrophilic myelocytes in a biological specimen. |
| C135438 | NEUTNSQE | Neutrophils/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the neutrophils to non-squamous epithelial cells in a biological specimen. |
| C187823 | NEUTPPH | Neutrophils with Pseudo Pelger-Huet Nucleus; Pseudo Pelger-Huet Neutrophils | A measurement of the neutrophils with a Pelger-Huet-like nucleus (hyposegmented) in a biological specimen. |
| C81997 | NEUTSG | Neutrophils, Segmented | A measurement of the segmented neutrophils in a biological specimen. |
| C154755 | NEUTSGB | Neutrophils, Segmented + Band Form | A measurement of the segmented and band form neutrophils in a biological specimen. |
| C154756 | NEUTSGBP | Neutrophils, Seg + Band Form + Precursor; Neutrophils, Segmented + Band Form + Precursors | A measurement of the segmented and band form neutrophils, metamyelocytes, myelocytes, promyelocytes, and myeloblasts in a biological specimen. |
| C187679 | NEUTSGCE | Neutrophils, Segmented/Total Cells | A relative measurement (ratio or percentage) of segmented neutrophils to total cells in a biological specimen. |
| C82045 | NEUTSGLE | Neutrophils, Segmented/Leukocytes | A relative measurement (ratio or percentage) of segmented neutrophils to leukocytes in a biological specimen. |
| C120643 | NEUTSGNE | Neutrophils, Segmented/Neutrophils | A relative measurement (ratio or percentage) of segmented neutrophils to total neutrophils in a biological specimen. |
| C132376 | NEUTTOXC | Neutrophilic Toxic Change | A measurement of any type of toxic change in cells of the neutrophilic lineage in a biological specimen. |
| C74628 | NEUTVAC | Vacuolated Neutrophils | A measurement of the neutrophils containing small vacuoles in a biological specimen. |
| C172501 | NFHP | Phosphorylated Neurofilament Heavy Chain | A measurement of the phosphorylated neurofilament heavy chain in a biological specimen. |
| C142285 | NFLP | NEFL; Neurofilament Light Chain Protein; Neurofilament Light Polypeptide; NF-L; Protein Phosphatase 1, Regulatory Subunit 110 | A measurement of the neurofilament light chain protein in a biological specimen. |
| C135439 | NGF | Nerve Growth Factor | A measurement of the nerve growth factor in a biological specimen. |
| C186085 | NHDLLDL | Non-HDL Cholesterol/LDL Cholesterol | A relative measurement (ratio or percentage) of the non-HDL cholesterol to LDL cholesterol in a biological specimen. |
| C147401 | NHMCE | Nonhematic Cells | A measurement of the cells of nonhematopoietic origin in a biological specimen. |
| C147402 | NHMCELE | Nonhematic Cells/Leukocytes | A relative measurement (ratio) of the nonhematic cells to total leukocytes in a biological specimen. |
| C177952 | NHYDCDN | Norhydrocodone | A measurement of the norhydrocodone in a biological specimen. |
| C147403 | NICOTINE | Nicotine | A measurement of the nicotine in a biological specimen. |
| C161352 | NITRATE | Nitrate; Nitric Acid | A measurement of the nitrate in a biological specimen. |
| C112360 | NITRICOX | Nitric Oxide; NO | A measurement of the nitric oxide in a biological specimen. |
| C64810 | NITRITE | Nitrite | A measurement of the nitrite in a biological specimen. |
| C98762 | NKCE | Natural Killer Cells | A measurement of the total natural killer cells in a biological specimen. |
| C116203 | NKCEFUNC | Natural Killer Cell Activity; Natural Killer Cell Function | A measurement of the natural killer cell function in a biological specimen. |
| C163473 | NKINA | Neurokinin A; NKA; Substance K | A measurement of the neurokinin A in a biological specimen. |
| C181258 | NKLY | Natural Killer Cells/Lymphocytes; NK Cells/Lym | A relative measurement (ratio or percentage) of the natural killer cells to lymphocytes in a biological specimen. |
| C147404 | NMH | N-methylhistamine | A measurement of the N-methylhistamine in a biological specimen. |
| C156509 | NMP22 | Nuclear Matrix Protein 22; Nuclear Mitotic Apparatus Protein 1; NUMA1 | A measurement of the nuclear matrix protein 22 in a biological specimen. |
| C120644 | NOHDLHDL | Non-HDL Cholesterol/HDL Cholesterol | A relative measurement (ratio or percentage) of non-high density lipoprotein cholesterol to high density lipoprotein cholesterol in a biological specimen. |
| C116204 | NONHDL | Non-HDL Cholesterol; Non-High Density Lipoprotein | A measurement of the non-high density lipoprotein cholesterol in a biological specimen. |
| C163472 | NOREPEXR | Norepinephrine Excretion Rate | A measurement of the amount of norepinephrine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C74868 | NOREPIN | Noradrenaline; Norepinephrine | A measurement of the norepinephrine hormone in a biological specimen. |
| C147405 | NORMBASO | Basophilic Normoblast | A measurement of the basophilic normoblasts in a biological specimen taken from a non-human organism. |
| C163474 | NORMEEXR | Normetanephrine Excretion Rate | A measurement of the amount of normetanephrine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C122138 | NORMETA | Normetanephrine | A measurement of the normetanephrine in a biological specimen. |
| C186086 | NORMETFR | Normetanephrine, Free | A measurement of the free normetanephrine in a biological specimen. |
| C147406 | NORNCTN | Nornicotine | A measurement of the nornicotine in a biological specimen. |
| C186087 | NORTRPTL | Nortriptyline | A measurement of the nortriptyline in a biological specimen. |
| C177953 | NOXYCDN | Noroxycodone | A measurement of the noroxycodone in a biological specimen. |
| C100434 | NPAP | Non-Prostatic Acid Phosphatase | A measurement of the non-prostatic acid phosphatase in a biological specimen. |
| C74892 | NPY | Neuropeptide Y | A measurement of the neuropeptide Y in a biological specimen. |
| C139076 | NRDZPM | Desmethyldiazepam; N-Desmethyldiazepam; Nordazepam; Nordiazepam | A measurement of the nordazepam present in a biological specimen. |
| C184594 | NRENDRLN | Norethandrolone | A measurement of the norethandrolone in a biological specimen. |
| C165977 | NRP1 | BDCA4; CD304; Neuropilin-1; NP1; NRP; VEGF165R | A measurement of the neuropilin-1 in a biological specimen. |
| C186088 | NRPROPOX | Norpropoxyphene | A measurement of the norpropoxyphene in a biological specimen. |
| C116205 | NSE | Enolase 2; Gamma-enolase; Neuron Specific Enolase | A measurement of the neuron specific enolase in a biological specimen. |
| C142286 | NSPMTSPM | Normal Sperm/Total Sperm; Sperm Morphology | A measurement (ratio or percentage) of the normal spermatozoa to total spermatozoa in a biological specimen. |
| C120645 | NTELOCRT | N-telopeptide/Creatinine | A relative measurement (ratio or percentage) of the N-telopeptide to creatinine in a biological specimen. |
| C74743 | NTELOP | N-telopeptide | A measurement of the N-telopeptide in a biological specimen. |
| C163475 | NTENS | Neurotensin; NTS | A measurement of the neurotensin in a biological specimen. |
| C147407 | NTRLFAT | Neutral Fats | A measurement of the total neutral fats in a biological specimen. |
| C184629 | NTRZPM | Nitrazepam | A measurement of the nitrazepam in a biological specimen. |
| C82039 | NTXI | Type I Collagen N-Telopeptides; Type I Collagen X-Linked N-Telopeptides | A measurement of the type I collagen cross-linked N-telopeptides in a biological specimen. |
| C147408 | NTXICRT | T1 Collagen X-link N-Telopeptides/Creat; Type I Collagen X-linked N-Telopeptides/Creatinine | A relative measurement (ratio or percentage) of the type 1 collagen cross-linked N-telopeptides to creatinine in a biological specimen. |
| C82041 | NTXII | Type II Collagen N-Telopeptides; Type II Collagen X-Linked N-Telopeptides | A measurement of the type II collagen cross-linked N-telopeptides in a biological specimen. |
| C186089 | NTZPMAOM | Nitrazepam and/or Metabolites | A measurement of the nitrazepam and/or its metabolite(s) present in a biological specimen, for an assay that can measure both nitrazepam and its metabolites. |
| C150841 | NUCCE | Nucleated Cells | A measurement of the nucleated cells in a biological specimen. |
| C114213 | NUCSWELL | Nuclear Swelling | A measurement of the expansion of the nucleus of the cells in a biological specimen. |
| C111284 | O2CT | Oxygen Content | A measurement of the amount of oxygen content in a biological specimen. |
| C163476 | OAS1 | 2-5-Oligoadenylate Synthase 1 | A measurement of the 2-5-oligoadenylate synthase 1 in a biological specimen. |
| C163477 | OAS2 | 2-5-Oligoadenylate Synthase 2 | A measurement of the 2-5-oligoadenylate synthase 2 in a biological specimen. |
| C163478 | OAS3 | 2-5-Oligoadenylate Synthase 3 | A measurement of the 2-5-oligoadenylate synthase 3 in a biological specimen. |
| C74686 | OCCBLD | Occult Blood | A measurement of the blood in body products such as a urine or stool sample, not detectable on gross examination. |
| C163479 | ODMTASE | O-Demethylase | A measurement of the O-Demethylase in a biological specimen. |
| C181402 | ODSMT | Desmetramadol; O-Desmethyltramadol; O-DSMT | A measurement of the O-desmethyltramadol in a biological specimen. |
| C174309 | OH8DXG2 | 8-Hydroxy-2'-Deoxyguanosine; 8-oxo-dG | A measurement of the 8-hydroxy-2'-deoxyguanosine in a biological specimen. |
| C177970 | OH9RS | 9-Hydroxyrisperidone; Paliperidone | A measurement of the 9-hydroxyrisperidone in a biological specimen. |
| C172492 | OHDG8 | 8-Hydroxydeoxyguanosine; 8-OHdG | A measurement of the 8-hydroxydeoxyguanosine in a biological specimen. |
| C150833 | OHF6B | 6 Beta-Hydrocortisol; 6 Beta-Hydroxycortisol; 6 beta-OHF | A measurement of 6 beta-hydroxycortisol in a biological specimen. |
| C177966 | OLANZAPN | Olanzapine | A measurement of the olanzapine in a biological specimen. |
| C122139 | OLIGBAND | Oligoclonal Bands | A measurement of the oligoclonal bands in a biological specimen. |
| C116206 | OPG | OCIF; Osteoclastogenesis Inhibitory Factor; Osteoprotegerin; TNFRS11B; Tumor Necrosis Factor Receptor Superfamily Member 11b | A measurement of the osteoprotegerin in a biological specimen. |
| C74796 | OPIATE | Opiate | A measurement of any opiate class drug present in a biological specimen. |
| C124349 | OPN | Osteopontin | A measurement of the osteopontin in a biological specimen. |
| C177962 | OPNCRT | Osteopontin/Creatinine | A relative measurement (ratio or percentage) of the osteopontin to creatinine in a biological specimen. |
| C122140 | ORNITHIN | Ornithine | A measurement of the ornithine in a biological specimen. |
| C132377 | OSM | Oncostatin M | A measurement of the oncostatin M in a biological specimen. |
| C74801 | OSMLTY | Osmolality | A measurement of the osmoles of solute per unit of biological specimen. |
| C74802 | OSMRTY | Osmolarity | A measurement of the osmoles of solute per liter of solution. |
| C74744 | OSTEOC | Osteocalcin | A measurement of the osteocalcin in a biological specimen. |
| C142287 | OVALCY | Ovalocytes | A measurement of the ovalocytes (oval shaped cell with rounded ends and a long axis less than twice its short axis) in a biological specimen. |
| C117983 | OXACREAT | Oxalate/Creatinine | A relative measurement (ratio or percentage) of the oxalate to creatinine in a biological specimen. |
| C163480 | OXAEXR | Oxalate Excretion Rate | A measurement of the amount of oxalate being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C92250 | OXALATE | Ethanedioate; Oxalate | A measurement of the oxalate in a biological specimen. |
| C75381 | OXANDRLN | Ossandrolone; Oxandrolone | A measurement of the oxandrolone in a biological specimen. |
| C147409 | OXMORPHN | Oxymorphone | A measurement of the Oxymorphone in a biological specimen. |
| C184595 | OXMSTRN | Oxymesterone | A measurement of the oxymesterone in a biological specimen. |
| C75388 | OXMTHLN | Oxymethalone; Oxymethenolone; Oxymetholone | A measurement of the oxymetholone in a biological specimen. |
| C96614 | OXYCAP | Oxygen Capacity | A measurement of the maximum amount of oxygen that can be combined chemically with hemoglobin in a volume of blood. |
| C74884 | OXYCDN | Oxycodone; Oxycontin | A measurement of the oxycodone present in a biological specimen. |
| C60832 | OXYSAT | Oxygen Saturation | A measurement of the oxygen-hemoglobin saturation of a volume of blood. |
| C74869 | OXYTOCIN | Oxytocin; Oxytoxin | A measurement of the oxytocin hormone in a biological specimen. |
| C75375 | OXZPM | Oxazepam | A measurement of the oxazepam present in a biological specimen. |
| C96625 | P1NP | Amino-terminal propeptide of type 1 procollagen; P1NP Aminoterm Type 1; Procollagen 1 N-Terminal Propeptide | A measurement of the procollagen 1 N-terminal propeptide in a biological specimen. |
| C128973 | P3NP | Procollagen 3 N-Terminal Propeptide | A measurement of the procollagen 3 N-terminal propeptide in a biological specimen. |
| C102279 | P50OXYGN | P50 Oxygen | A measurement of the partial pressure of oxygen when hemoglobin is half saturated in a biological specimen. |
| C186090 | PABA | Para-Aminobenzoate; Para-Aminobenzoic Acid | A measurement of the para-aminobenzoate in a biological specimen. |
| C111292 | PAF | Platelet Activating Factor | A measurement of the platelet activating factor in a biological specimen. |
| C189315 | PAHPP | 4-Aminohippurate; P-Amino Hippuric Acid; P-Aminohippurate; PAH; Para Aminohippurate; Para Aminohippuric Acid; Para-Amino Hippuric Acid; Para-Aminohippurate | A measurement of the para aminohippurate in a biological specimen. |
| C189530 | PAHPPCLR | 4-Aminohippurate Clearance; P-Amino Hippuric Acid Clearance; P-Aminohippurate Clearance; PAH Clearance; Para Aminohippurate Clearance; Para Aminohippuric Acid Clearance; Para-Amino Hippuric Acid Clearance; Para-Aminohippurate Clearance | A measurement of the volume of serum or plasma that would be cleared of para aminohippurate by excretion of urine for a specified unit of time (e.g. one minute). |
| C82030 | PAI1 | Plasminogen Activator Inhibitor-1 | A measurement of the plasminogen activator inhibitor-1 in a biological specimen. |
| C81989 | PAI1AG | Plasminogen Activator Inhibitor-1 AG | A measurement of the plasminogen activator inhibitor-1 antigen in a biological specimen. |
| C80204 | PAP | Prostatic Acid Phosphatase | A measurement of the prostatic acid phosphatase in a biological specimen. |
| C82031 | PAPPA | Pregnancy-Associated Plasma Protein-A | A measurement of the pregnancy-associated plasma protein-A in a biological specimen. |
| C74616 | PAPPEN | Pappenheimer Bodies | A measurement of the cells containing Pappenheimer Bodies (violet or blue staining ferritin granules usually found along the periphery of the red blood cells) in a biological specimen. |
| C184630 | PARALD | Paraldehyde | A measurement of the paraldehyde in a biological specimen. |
| C116207 | PARICEAB | Anti-Parietal Cell Antibody; Parietal Cell Antibody | A measurement of the parietal cell antibody in a biological specimen. |
| C147410 | PAROXET | Paroxetine | A measurement of the paroxetine present in a biological specimen. |
| C184559 | PB223C | PB-22 3-carboxyindole | A measurement of the synthetic cannabinoid metabolite PB-22 3-carboxyindole in a biological specimen. |
| C184560 | PB225F3C | 5-fluoro PB-22 3-carboxyindole | A measurement of the synthetic cannabinoid metabolite 5-fluoro PB-22 3-carboxyindole in a biological specimen. |
| C156539 | PBG | Porphobilinogen | A measurement of the porphobilinogen in a biological specimen. |
| C156540 | PBGCREAT | Porphobilinogen/Creatinine | A relative measurement (ratio or percentage) of the porphobilinogen to creatinine in a biological specimen. |
| C132378 | PC3MPSAM | PCA3 mRNA/PSA mRNA | A relative measurement (ratio) of the prostate cancer antigen 3 mRNA to prostate specific antigen mRNA in a biological specimen. |
| C132379 | PCA3MRNA | Prostate Cancer Antigen 3 mRNA | A measurement of the prostate cancer antigen 3 mRNA in a biological specimen. |
| C111294 | PCDW | Platelet Component Distribution Width | A measurement of a marker of platelet shape change in a biological specimen. |
| C177983 | PCHLRPZN | Prochlorperazine | A measurement of the prochlorperazine in a biological specimen. |
| C120646 | PCNAG | Cyclin; Proliferating Cell Nuclear Antigen | A measurement of the proliferating cell nuclear antigen in a biological specimen. |
| C82625 | PCO2 | Partial Pressure Carbon Dioxide | A measurement of the pressure of carbon dioxide in a biological specimen. |
| C147411 | PCO2ADJT | Partial Pressure Carbon Dioxide Adj Temp | A measurement of the pressure of carbon dioxide, which has been adjusted for body temperature, in a biological specimen. |
| C74694 | PCP | Phencyclidine; Phenylcyclohexylpiperidine | A measurement of the phencyclidine present in a biological specimen. |
| C120647 | PCSK9 | Proprotein Convertase Subtilisin/Kexin 9 | A measurement of the proprotein convertase subtilisin/kexin type 9 in a biological specimen. |
| C186091 | PCSK9FR | Proprotein Convertase Subtilisin/Kexin Type 9; Prprot Cnvrtase Subtilisin-Kexin 9, Free | A measurement of the free proprotein convertase subtilisin/kexin type 9 in a biological specimen. |
| C103430 | PCT | Procalcitonin | A measurement of the procalcitonin in a biological specimen. |
| C172505 | PD1S | Soluble CD279; Soluble PD-1; Soluble PD1; Soluble Programmed Cell Death Protein 1; Soluble Programmed Death-1 | A measurement of the soluble programmed death-1 protein in a biological specimen. |
| C163481 | PDGFAA | PDGF Isoform AA; Platelet Derived Growth Factor IsoformAA; Platelet Derived Growth Factor-AA Isoform | A measurement of the platelet derived growth factor isoform AA in a biological specimen. |
| C116208 | PDGFAB | PDGF Isoform AB; Platelet Derived Growth Factor IsoformAB; Platelet Derived Growth Factor-AB Isoform | A measurement of the platelet derived growth factor isoform AB in a biological specimen. |
| C172503 | PDL1S | Soluble CD274; Soluble PD-L1; Soluble PDL1; Soluble Programmed Death Ligand 1 | A measurement of the soluble programmed death ligand 1 in a biological specimen. |
| C81962 | PDW | Platelet Distribution Width | A measurement of the range of platelet sizes in a biological specimen. |
| C135472 | PECAM1 | CD31; CD31 Antigen; PECAM; PECAM-1; PECAM1; Platelet And Endothelial Cell Adhesion Molecule 1; Platelet Endo Cell Adhesion Molecule 1; Platelet Endothelial Adhesion Molecule | A measurement of the platelet and endothelial cell adhesion molecule 1 in a biological specimen. |
| C74617 | PELGERH | Pelger Huet Anomaly; Pelger-Huet Cells; PHA | A measurement of the Pelger-Huet Anomaly (nuclei of granulocytes appear rod-like, bilobed, peanut, or dumbbell shaped) in a biological specimen. |
| C81988 | PEMAB | Pemphigoid Antibodies | A measurement of the pemphigoid antibodies in a biological specimen. |
| C184631 | PEMOLINE | Pemoline | A measurement of the pemoline in a biological specimen. |
| C184561 | PENDRN | Pentedrone | A measurement of the pentedrone in a biological specimen. |
| C184562 | PENTYLN | Pentylone | A measurement of the pentylone in a biological specimen. |
| C100122 | PEPSNG | Pepsinogen | A measurement of the pepsinogen in a biological specimen. |
| C100469 | PEPSNGA | Pepsinogen A; PGA | A measurement of the pepsinogen A in a biological specimen. |
| C100470 | PEPSNGC | Pepsinogen C; PGC | A measurement of the pepsinogen C in a biological specimen. |
| C100467 | PEPSNGI | Pepsinogen I; PGI | A measurement of the pepsinogen I in a biological specimen. |
| C100468 | PEPSNGII | Pepsinogen II; PGII | A measurement of the pepsinogen II in a biological specimen. |
| C127632 | PERCECE | Proliferating Erythroid/Total Cells | A relative measurement (ratio or percentage) of the proliferating erythroid cells to total cells in a biological specimen. |
| C112395 | PERIOSTN | OSF2; Osteoblast Specific Factor 2; Periostin; POSTN | A measurement of the periostin in a biological specimen. |
| C177988 | PERPHNZN | Perphenazine | A measurement of the perphenazine in a biological specimen. |
| C119291 | PF2AI8CR | 8-Iso-PGF2alpha/Creatinine | A relative measurement (ratio or percentage) of the prostaglandin F2 alpha isoform 8 to creatinine in a biological specimen. |
| C147412 | PF4HCIAB | Platelet Factor 4 Heparin Complex Induced Antibody; Platelet Fctr 4 Heparin Cmplx Induced Ab | A measurement of the platelet factor 4 heparin complex induced antibody in a biological specimen. |
| C111295 | PFCT | PFCT; Platelet Function Closure Time | A measurement of the platelet function closure time in a biological specimen. |
| C103343 | PG | Prostaglandin | A measurement of the total prostaglandin in a biological specimen. |
| C165978 | PGAG | Platelet-Granulocyte Agg; Platelet-Granulocyte Aggregates | A measurement of the aggregates composed of platelets and granulocytes in a biological specimen. |
| C103431 | PGD2 | Prostaglandin D2 | A measurement of the prostaglandin D2 in a biological specimen. |
| C189515 | PGD2R2 | Prostaglandin D2 Receptor 2 | A measurement of the prostaglandin D2 receptor 2 in a biological specimen. |
| C103432 | PGD2S | Beta-Trace Protein; Prostaglandin D2 Synthase | A measurement of the prostaglandin D2 synthase in a biological specimen. |
| C103434 | PGE1 | Prostaglandin E1 | A measurement of the prostaglandin E1 in a biological specimen. |
| C103435 | PGE2 | Prostaglandin E2 | A measurement of the prostaglandin E2 in a biological specimen. |
| C103433 | PGES | Prostaglandin E Synthase | A measurement of the prostaglandin E synthase in a biological specimen. |
| C103436 | PGF1A | Prostaglandin F1 Alpha | A measurement of the prostaglandin F1 alpha in a biological specimen. |
| C103437 | PGF2A | Prostaglandin F2 Alpha | A measurement of the prostaglandin F2 alpha in a biological specimen. |
| C119292 | PGF2AI8 | 8-Iso-Prostaglandin F2 Alpha | A measurement of the prostaglandin F2 alpha isoform 8 in a biological specimen. |
| C45997 | PH | pH | The negative logarithm (base 10) of the concentration of hydronium ions, which is used as a measure of the acidity or alkalinity of a fluid. |
| C161367 | PHADJT | pH Adjusted for Body Temp | A measurement of pH, which has been adjusted for body temperature, in a biological specimen. |
| C81280 | PHE | Phenylalanine | A measurement of the phenylalanine in a biological specimen. |
| C74695 | PHENTHZ | Dibenzothiazine; Phenothiazine | A measurement of the phenothiazine present in a biological specimen. |
| C147413 | PHENYTN | Phenytoin | A measurement of the phenytoin in a biological specimen. |
| C81281 | PHETYR | Phenylalanine/Tyrosine | A relative measurement (ratio) of the phenylalanine to tyrosine in a biological specimen. |
| C75368 | PHNBRBTL | Phenobarbital | A measurement of the phenobarbital present in a biological specimen. |
| C184597 | PHNDMTZN | Phendimetrazine | A measurement of the phendimetrazine in a biological specimen. |
| C147414 | PHNKET | Phenyl Ketones; Phenylketones | A measurement of the total phenylketones in a biological specimen |
| C184574 | PHNMTZN | Phenmetrazine | A measurement of the phenmetrazine in a biological specimen. |
| C184573 | PHNZCN | Phenazocine | A measurement of the phenazocine in a biological specimen. |
| C64857 | PHOS | Inorganic Phosphate; Phosphate; Phosphorus | A measurement of the phosphate in a biological specimen. |
| C106553 | PHOSCLR | Phosphate Clearance | A measurement of the volume of serum or plasma that would be cleared of phosphate by excretion of urine for a specified unit of time (e.g. one minute). |
| C79461 | PHOSCRT | Phosphate/Creatinine | A relative measurement (ratio or percentage) of the phosphate to creatinine in a biological specimen. |
| C150821 | PHOSEXR | Phosphorus Excretion Rate | A measurement of the amount of phosphorus being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C96623 | PHOSLPD | Phospholipid | A measurement of the phospholipids in a biological specimen. |
| C174299 | PHTRMN | Phentermine; Phenyl-tertiary-butylamine | A measurement of the phentermine in a biological specimen. |
| C82033 | PICP | Procollagen Type I Carboxy Term Peptide | A measurement of the procollagen-1 carboxy-terminal peptide in a biological specimen. |
| C177987 | PIMOZIDE | Pimozide | A measurement of the pimozide in a biological specimen. |
| C184633 | PIPRDROL | Pipradrol | A measurement of the pipradrol in a biological specimen. |
| C150846 | PIVKAII | DCP; Des-Gammacarboxyprothrombin; PIVKA-II; Protein Induced by Vitamin K Absence-II; Protein Induced by Vitamin K Absence/Antagonist-II | A measurement of the protein induced by vitamin K absence-II in a biological specimen. |
| C156530 | PKM | Pyruvate Kinase Muscle Isozyme | A measurement of the total pyruvate kinase muscle isozymes (M1 and M2) in a biological specimen. |
| C156532 | PKM1 | Pyruvate Kinase Isozyme M1 | A measurement of the pyruvate kinase isozyme M1 in a biological specimen. |
| C156531 | PKM2 | Pyruvate Kinase Isozyme M2 | A measurement of the pyruvate kinase isozyme M2 in a biological specimen. |
| C181405 | PLA2 | Phospholipase A2 | A measurement of the total phospholipase A2 in a biological specimen. |
| C114210 | PLAGGCVT | Platelet Aggregation Curve Type | The classification of the curve pattern that is formed as a result of platelet aggregation. |
| C114211 | PLAGMAMP | Platelet Aggregation Mean Amplitude | An average of the measurements of the magnitude of the platelet aggregation in a biological specimen. |
| C114212 | PLAGMCVT | Platelet Aggregation Mean Curve Type | The classification of the curve pattern that is formed as the average result of the platelet aggregation curve measurements. |
| C51951 | PLAT | Platelets | A measurement of the platelets (non-nucleated thrombocytes) in a biological specimen. |
| C103427 | PLATAGGR | Platelet Aggregation; Platelet Function | A measurement of the association of platelets to one another via adhesion molecules in a biological sample. |
| C147415 | PLATAGRN | Platelets, Agranular | A measurement of the agranular platelets in a biological specimen. |
| C154733 | PLATBIZ | Bizarre Platelets | A measurement of the bizarre platelets (large with abnormal morphology and shape) in a biological specimen. |
| C96624 | PLATCLMP | Platelet Clumps; PLT Clumps | A measurement of the platelet clumps in a biological specimen. |
| C135440 | PLATEST | Platelets, Estimated | An estimated measurement of the platelets (non-nucleated thrombocytes) in a biological specimen. |
| C74728 | PLATGNT | Giant Platelets | A measurement of the giant (larger than 7um in diameter) platelets in a biological specimen. |
| C100424 | PLATHCT | Platelet Hematocrit; Thrombocytocrit | A relative measurement (ratio or percentage) of the proportion of the volume of blood taken up by platelets. |
| C154723 | PLATIM | Immature Platelets; Reticulated Platelets | A measurement of the immature platelets in a biological specimen. |
| C74729 | PLATLRG | Large Platelets | A measurement of the large (between 4 um and 7um in diameter) platelets in a biological specimen. |
| C116209 | PLATSAT | Platelet Satellitism | An examination or assessment of the platelet satellitism (platelet rosetting around cells) in a biological specimen. |
| C163482 | PLCGF | PGF; PIGF; Placental Growth Factor; PLGF | A measurement of the placental growth factor in a biological specimen. |
| C127633 | PLG | Plasminogen | A measurement of the plasminogen (antigen) in a biological specimen. |
| C158237 | PLP | Active Vitamin B6; Pyridoxal Phosphate | A measurement of the pyridoxal phosphate in a biological specimen. |
| C163483 | PLSCR1 | Phospholipid Scramblase 1 | A measurement of the phospholipid scramblase 1 in a biological specimen. |
| C147416 | PLSIMCCE | Immature Plasma Cells/Total Cells | A relative measurement (ratio or percentage) of the immature plasma cells (plasmacytes) to total cells in a biological specimen. |
| C96679 | PLSIMCE | Immature Plasma Cells | A measurement of the immature plasma cells in a biological specimen. |
| C96680 | PLSIMCLY | Immature Plasma Cells/Lymphocytes | A relative measurement (ratio or percentage) of immature plasma cells to total lymphocytes in a biological specimen. |
| C74661 | PLSMCE | Mature Plasma Cells; Plasmacytes; Plasmocytes | A measurement of the mature plasma cells (plasmacytes) in a biological specimen. |
| C98869 | PLSMCECE | Mature Plasma Cells/Total Cells | A relative measurement (ratio or percentage) of the mature plasma cells (plasmacytes) to total cells in a biological specimen (for example a bone marrow specimen). |
| C74911 | PLSMCELY | Mature Plasma Cells/Lymphocytes | A relative measurement (ratio or percentage) of the mature plasma cells (plasmacytes) to all lymphocytes in a biological specimen. |
| C172494 | PLSNCE | Clonal Plasma Cells; Monoclonal Plasma Cells; Monotypic Plasma Cells; Neoplastic Plasma Cells | A measurement of the neoplastic plasma cells in a biological specimen. |
| C74619 | PLSPCE | Plasmablast; Precursor Plasma Cells | A measurement of the precursor (blast stage) plasma cells (antibody secreting cells derived from B cells via antigen stimulation) in a biological specimen. |
| C74650 | PLSPCELY | Precursor Plasma Cells/Lymphocytes | A relative measurement (ratio or percentage) of the precursor (blast stage) plasma cells (antibody secreting cells derived from B cells via antigen stimulation) to all lymphocytes in a biological specimen. |
| C128974 | PLSTCE | Total Plasma Cells | A measurement of the total plasma cells in a biological specimen. |
| C187987 | PLSTCECE | Total Plasma Cells/Total Cells | A relative measurement (ratio or percentage) of the total plasma cells to total cells in a biological specimen. |
| C128975 | PLSTCELE | Total Plasma Cells/Leukocytes | A relative measurement (ratio or percentage) of the total plasma cells to leukocytes in a biological specimen. |
| C189499 | PLSTCELY | Total Plasma Cells/Lymphocytes | A relative measurement (ratio or percentage) of the total plasma cells to lymphocytes in a biological specimen. |
| C111293 | PLTAGAMP | Platelet Aggregation Amplitude | A measurement of the magnitude of the platelet aggregation in a biological specimen. |
| C170580 | PLTIMPLT | Immature Platelet Fraction; Immature Platelets/Total Platelets; IPF; Reticulated Platelets/Total Platelets | A relative measurement (ratio or percentage) of immature platelets to total platelets in a biological specimen. |
| C161353 | PLTLPLT | Large Platelets/Total Platelets; Platelet Large Cell Ratio; PLCR | A relative measurement (ratio or percentage) of large platelets to total platelets in a biological specimen. |
| C111296 | PLTMORPH | Platelet Morphology | An examination or assessment of the form and structure of platelets. |
| C132380 | PMDW | Platelet Mass Distribution Width | A measurement which represents the variation defined by two standard deviations of the platelet dry mass distribution in a biological specimen. |
| C127634 | PMYCECE | Proliferating Myeloid Cells/Total Cells | A relative measurement (ratio or percentage) of the proliferating myeloid cells to total cells in a biological specimen. |
| C80201 | PNCTPP | Pancreatic Polypeptide | A measurement of the pancreatic polypeptide in a biological specimen. |
| C75367 | PNTBRBTL | Pentobarbital | A measurement of the pentobarbital present in a biological specimen. |
| C184632 | PNTZOCIN | Pentazocine | A measurement of the pentazocine in a biological specimen. |
| C71251 | PO2 | PaO2; Partial Pressure Oxygen; Po2; pO2 | A measurement of the pressure of oxygen in a biological specimen. |
| C147417 | PO2ADJT | Partial Pressure Oxygen Adj for Temp | A measurement of the pressure of oxygen, which has been adjusted for body temperature, in a biological specimen. |
| C119293 | PO2FIO2 | PAO2/FIO2; PP Arterial O2/Fraction Inspired O2 | A relative measurement (ratio or percentage) of the force per unit area (pressure) of oxygen dissolved in arterial blood to the percentage oxygen of an inhaled mixture of gasses. |
| C79602 | POIKILO | Poikilocytes | A measurement of the odd-shaped erythrocytes in a whole blood specimen. |
| C74649 | POIKRBC | Poikilocytes/Erythrocytes | A relative measurement (ratio or percentage) of the poikilocytes, or irregularly shaped erythrocytes, to all erythrocytes in a biological specimen. |
| C64803 | POLYCHR | Polychromasia | A measurement of the blue-staining characteristic of newly generated erythrocytes. |
| C147418 | POLYERY | Polychromatophilic Erythroblast | A measurement of the polychromatophilic erythroblasts in a biological specimen taken from a non-human organism. |
| C147419 | POLYNORM | Polychromatophilic Normoblast | A measurement of the polychromatophilic normoblasts in a biological specimen taken from a non-human organism. |
| C120648 | PORPH | Porphyrin | A measurement of the total porphyrin in a biological specimen. |
| C174297 | PPA | Beta-Hydroxyamphetamine; Norephedrine; Phenylpropanolamine | A measurement of the phenylpropanolamine in a biological specimen. |
| C161358 | PPI | Inorganic Pyrophosphate | A measurement of the inorganic pyrophosphate in a biological specimen. |
| C187819 | PPIA | Cyclophilin A; CYPA; Peptidylprolyl Isomerase A; Rotamase A | A measurement of the peptidylprolyl isomerase A in a biological specimen. |
| C147420 | PPTDCALB | Phosphatidylcholine/Albumin | A relative measurement (ratio or percentage) of the phosphatidylcholine to albumin in a biological specimen. |
| C187820 | PPTDETH | PEth; Phosphatidylethanol | A measurement of the total phosphatidylethanol in a biological specimen. |
| C116210 | PRAB | Panel Reactive Antibody; Percent Reactive Antibody; PRA Score | A measurement of the panel reactive antibody that is achieved by mixing and assessing the reactivity between the recipient's immune cells and the donor's human leukocyte antigen, in which anti-HLA class I and class II antibody specificities are measured separately in a biological specimen. |
| C132381 | PRABC | Calculated Panel Reactive Antibody | A measurement of the calculated panel reactive antibody, which is based on the number/type of unacceptable HLA antigens to which an organ recipient has been sensitized, and which algorithmically estimates the level of sensitization in the recipient. The CPRA is computed from HLA antigen frequencies in a given donor population using both anti-HLA class I and class II antibody specificities; it also represents the percentage of actual organ donors that express one or more unacceptable HLA antigens to which a recipient may react adversely. |
| C132382 | PRCTC | Prostate Circulating Tumor Cells | A measurement of the prostate circulating tumor cells in a biological specimen. |
| C100435 | PREALB | Prealbumin; Thyroxine-binding Prealbumin; Transthyretin | A measurement of the prealbumin in a biological specimen. |
| C184642 | PREGBLN | Pregabalin | A measurement of the pregabalin in a biological specimen. |
| C147421 | PRGNENLN | Pregnenolone | A measurement of the pregnenolone in a biological specimen. |
| C186092 | PRGNNDL | Pregnanediol | A measurement of the pregnanediol in a biological specimen. |
| C111299 | PRINSINS | Proinsulin/Insulin Ratio | A relative measurement (ratio or percentage) of the proinsulin to insulin in a biological specimen. |
| C64829 | PRLYMLE | Prolymphocytes/Leukocytes | A relative measurement (ratio or percentage) of prolymphocytes to leukocytes in a biological specimen. |
| C184596 | PRMPNL | Perampanel | A measurement of the perampanel in a biological specimen. |
| C122141 | PRO | Proline | A measurement of the proline in a biological specimen. |
| C165979 | PROC6 | C-terminal Pro-Peptide of the Alpha 3 Type VI Collagen Chain; Endotrophin; Pro-C6 | A measurement of the pro-C6 in a biological specimen. |
| C184567 | PRODINEA | Alphaprodine | A measurement of the alphaprodine in a biological specimen. |
| C74791 | PROGEST | Progesterone | A measurement of the progesterone hormone in a biological specimen. |
| C117846 | PROGESTR | NR3C3; PGR; PgR; PR; Progesterone Receptor | A measurement of the progesterone receptor protein in a biological specimen. |
| C156523 | PROGRP | Pro-gastrin Releasing Peptide; proGRP | A measurement of the pro-gastrin releasing peptide in a biological specimen. |
| C81967 | PROINSUL | Proinsulin | A measurement of the proinsulin in a biological specimen. |
| C74870 | PROLCTN | Prolactin | A measurement of the prolactin hormone in a biological specimen. |
| C74620 | PROLYM | Prolymphocytes | A measurement of the prolymphocytes in a biological specimen. |
| C74651 | PROLYMLY | Prolymphocytes/Lymphocytes | A relative measurement (ratio or percentage) of the prolymphocytes to all lymphocytes in a biological specimen. |
| C187678 | PROMONCE | Promonocytes/Total Cells | A relative measurement (ratio or percentage) of the promonocytes to total cells in a biological specimen (for example a bone marrow specimen). |
| C74652 | PROMONLE | Promonocytes/Leukocytes | A relative measurement (ratio or percentage) of the promonocytes to all leukocytes in a biological specimen. |
| C74621 | PROMONO | Promonocytes | A measurement of the promonocytes in a biological specimen. |
| C74622 | PROMY | Promyelocytes | A measurement of the promyelocytes (immature myelocytes) in a biological specimen. |
| C117847 | PROMYB | Promyeloblasts | A measurement of the promyeloblasts in a biological specimen. |
| C98773 | PROMYCE | Promyelocytes/Total Cells | A relative measurement (ratio or percentage) of the promyelocytes (immature myelocytes) to total cells in a biological specimen (for example a bone marrow specimen). |
| C74653 | PROMYLE | Promyelocytes/Leukocytes | A relative measurement (ratio or percentage) of the promyelocytes (immature myelocytes) to all leukocytes in a biological specimen. |
| C74885 | PROPOX | Propoxyphene | A measurement of the propoxyphene present in a biological specimen. |
| C128976 | PRORUB | Basophilic Erythroblast; Basophilic Normoblast; Prorubricyte | A measurement of the prorubricytes in a biological specimen. |
| C128977 | PRORUBCE | Prorubricyte/Total Cells | A relative measurement (ratio or percentage) of the prorubricytes to total cells in a biological specimen. |
| C64858 | PROT | Protein | A measurement of the total protein in a biological specimen. |
| C79463 | PROTCRT | Protein/Creatinine | A relative measurement (ratio or percentage) of the total protein to creatinine in a biological specimen. |
| C150822 | PROTEXR | Protein Excretion Rate | A measurement of the amount of total protein being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C92240 | PROTOSML | Protein/Osmolality; Protein/Osmolality Ratio | A relative measurement (ratio or percentage) of total proteins to the osmolality of a biological specimen. |
| C147422 | PROTPATN | Protein Pattern | A measurement of the protein band pattern in a biological specimen. |
| C100436 | PROTS | Protein S | A measurement of the total protein S in a biological specimen. |
| C122142 | PROTSFR | Protein S, Free | A measurement of the unbound protein S in a biological specimen. |
| C184598 | PRSTNZL | Prostanozol | A measurement of the prostanozol in a biological specimen. |
| C120649 | PRTN3AB | Proteinase 3 Antibody | A measurement of the proteinase 3 antibody in a biological specimen. |
| C139080 | PRZPM | Prazepam | A measurement of the prazepam present in a biological specimen. |
| C17634 | PSA | Prostate Specific Antigen | A measurement of the total prostate specific antigen in a biological specimen. |
| C132383 | PSAF | Prostate Specific Antigen, Free | A measurement of the unbound prostate-specific antigen in a biological specimen. |
| C132384 | PSAFPSAT | PSA, Free/PSA | A relative measurement (percentage) of the free prostate specific antigen to total prostate specific antigen in a biological specimen. |
| C132385 | PSAMRNA | Prostate Specific Antigen mRNA | A measurement of the prostate-specific antigen mRNA in a biological specimen. |
| C74696 | PSDEPHD | Pseudoephedrine | A measurement of the pseudoephedrine present in a biological specimen. |
| C147423 | PSDGLSRF | Phosphatidylglycerol/Lung Surfactant; Phosphatidylglycerol/Pulmonary Surfactant | A relative measurement (ratio) of the phosphatidylglycerol to total lung surfactant in a biological specimen. |
| C117850 | PSELECT | GMP-140; P-Selectin | A measurement of total P-selectin in a biological specimen. |
| C120650 | PSELECTS | Soluble P-Selectin | A measurement of the soluble P-selectin in a biological specimen. |
| C122143 | PSIGAAB | Phosphatidylserine IgA Antibody | A measurement of the phosphatidylserine IgA antibody in a biological specimen. |
| C122144 | PSIGGAB | Phosphatidylserine IgG Antibody | A measurement of the phosphatidylserine IgG antibody in a biological specimen. |
| C122145 | PSIGMAB | Phosphatidylserine IgM Antibody | A measurement of the phosphatidylserine IgM antibody in a biological specimen. |
| C75356 | PSLCYBN | Magic Mushrooms; Psilocybin; Psilocybine | A measurement of the psilocybin in a biological specimen. |
| C120651 | PSP100AB | P100 Polymyositis-scleroderma Autoag Ab | A measurement of the p100 polymyositis-scleroderma overlap syndrome-associated autoantigen antibody in a biological specimen. |
| C62656 | PT | Prothrombin Time | A blood clotting measurement that evaluates the extrinsic pathway of coagulation. |
| C98774 | PTA | Factor II Activity; Prothrombin Activity | A measurement of the biological activity of coagulation factor prothrombin in a biological specimen. |
| C170591 | PTAC | Prothrombin Time Actual/Control | A relative measurement (ratio or percentage) of the prothrombin time in a subject's specimen when compared to a control specimen. |
| C176312 | PTAUAB42 | Phosphorylated Tau Prot/Amyloid Beta1-42; Phosphorylated Tau Protein/Amyloid Beta 1-42 | A relative measurement (ratio) of the phosphorylated Tau protein to amyloid beta 1-42 in a biological specimen. |
| C189514 | PTF1 | Prothrombin Fragment 1 | A measurement of the prothrombin fragment 1 in a biological specimen. |
| C82034 | PTF1_2 | Prothrombin Fragments 1 + 2 | A measurement of the prothrombin fragments 1 and 2 in a biological specimen. |
| C189513 | PTF2 | Prothrombin Fragment 2 | A measurement of the prothrombin fragment 2 in a biological specimen. |
| C81964 | PTHCT | Parathyrin Hormone, C-Terminal; Parathyroid Hormone, C-Terminal | A measurement of the C-terminal fragment of parathyroid hormone in a biological specimen. |
| C74784 | PTHFG | Parathyrin Hormone, Fragmented; Parathyroid Hormone, Fragmented | A measurement of the fragmented parathyroid hormone in a biological specimen. |
| C74789 | PTHI | Parathyrin, Intact; Parathyroid Hormone, Intact | A measurement of the intact parathyroid hormone (consisting of amino acids 1-84 or 7-84) in a biological specimen. |
| C81965 | PTHMM | Parathyrin Hormone, Mid-Molecule; Parathyroid Hormone, Mid-Molecule | A measurement of the mid-molecule fragment of parathyroid hormone in a biological specimen. |
| C81966 | PTHNT | Parathyrin Hormone, N-Terminal; Parathyroid Hormone, N-Terminal | A measurement of the N-terminal fragment of parathyroid hormone in a biological specimen. |
| C117851 | PTHRP | Parathyrin Hormone-related Protein; Parathyroid Hormone-related Peptide; Parathyroid Hormone-related Protein | A measurement of parathyroid hormone-related protein in a biological specimen. |
| C103451 | PTHW | Parathyrin Hormone, Whole; Parathyroid Hormone, Whole | A measurement of the whole parathyroid hormone (consisting of amino acids 1-84) in a biological specimen. |
| C147424 | PTSAAC | Protein S Activity Actual/Control; Protein S Activity Actual/Normal; Protein S Activity Actual/Protein S Activity Control | A relative measurement (ratio or percentage) of the biological activity of protein S in a subject's specimen when compared to the same activity in a control specimen. |
| C170593 | PTSAC | Protein S Actual/Control | A relative measurement (ratio or percentage) of the protein S in a subject's specimen when compared to a control specimen. |
| C147425 | PTSFAAC | Protein S Free Activity Actual/Control; Protein S Free Activity Actual/Normal; Protein S Free Activity Actual/Protein S Free Activity Control | A relative measurement (ratio or percentage) of the biological activity of free protein S in a subject's specimen when compared to the same activity in a control specimen. |
| C170596 | PTSFAC | Protein S, Free Actual/Control | A relative measurement (ratio or percentage) of the free protein S in a subject's specimen when compared to a control specimen. |
| C178140 | PTT | Partial Thromboplastin Time | A measurement of the length of time that it takes for clotting to occur when no activating reagents are added to a biological specimen. The test is partial due to the absence of tissue factor (Factor III) from the reaction mixture. |
| C187818 | PTTSTND | Partial Thromboplastin Time/Standard Thromboplastin Time; PTT/Standard; PTT/Standard PTT | A relative measurement (ratio or percentage) of the subject's partial thromboplastin time to a standard or control partial thromboplastin time. |
| C161359 | PUS | Pus | A measurement of the pus in a biological specimen. |
| C147426 | PYDCREAT | Pyridinoline/Creatinine | A relative measurement (ratio or percentage) of the pyridinoline to creatinine in a biological specimen. |
| C156470 | PYK | PK; Pyruvate Kinase | A measurement of the total pyruvate kinase in a biological specimen. |
| C189346 | PYKCE | Karyopyknotic Cells; Pyknotic Cells | A measurement of the pyknotic cells in a biological specimen. |
| C156524 | PYOCYTES | Pyocytes | A measurement of the pyocytes in a biological specimen. |
| C80211 | PYRIDNLN | Pyridinoline | A measurement of the pyridinoline in a biological specimen. |
| C184643 | PYROVLRN | Pyrovalerone | A measurement of the pyrovalerone in a biological specimen. |
| C147427 | PYRUVATE | Pyruvate; Pyruvic Acid | A measurement of the pyruvate in a biological specimen. |
| C80202 | PYY | Peptide Tyrosine Tyrosine; Peptide YY | A measurement of the peptide YY in a biological specimen. |
| C177965 | QUETIAPN | Quetiapine | A measurement of the quetiapine in a biological specimen. |
| C184634 | QUZPM | Quazepam | A measurement of the quazepam in a biological specimen. |
| C165980 | RAGE | Advanced Glycosylation End-Product Specific Receptor; AGER; Receptor Advanced Glycation Endproducts | A measurement of the receptor advanced glycation endproducts in a biological specimen. |
| C117852 | RANKL | Receptor Activator Nuclear KappaB Ligand; Receptor Activator of Nuclear Kappa-B Ligand | A measurement of the receptor activator of nuclear kappa-B ligand in a biological specimen. |
| C81957 | RANTES | Chemokine Ligand 5; Reg upon Act Normal T-cell Exprd Secrtd | A measurement of the RANTES (regulated on activation, normally, T-cell expressed, and secreted) chemokine in a biological specimen. |
| C51946 | RBC | Erythrocytes; Red Blood Cells | A measurement of the total erythrocytes in a biological specimen. |
| C111197 | RBCAGGLU | Autoagglutination; Erythrocyte Agglutination; RBC Agglutination | A measurement of the erythrocyte agglutination in a biological specimen. |
| C92245 | RBCCLMP | Erythrocyte Cell Clumps; RBC Aggregates; RBC Clumps; Red Blood Cell Clumps | A measurement of red blood cell clumps in a biological specimen. |
| C117853 | RBCDIPOP | Dimorphic Erythrocyte Population; Dimorphic RBC Population | Examination of a biological specimen to detect the presence of dimorphic erythrocyte population. |
| C150839 | RBCDYRBC | Dysmorphic Erythrocytes/Erythrocytes | A measurement (ratio or percentage) of dysmorphic erythrocytes to total erythrocytes in a biological specimen. |
| C135441 | RBCDYSM | Dysmorphic Erythrocytes | A measurement of the dysmorphic erythrocytes in a biological specimen. |
| C116212 | RBCFRAG | Erythrocyte Fragment; RBC Fragment | A measurement of the red blood cell fragments (red cell fragments that have a reticular-like shape with rounded ends and no spicules, differentiating them from schistocytes and acanthocytes) in a biological specimen. |
| C96605 | RBCGHOST | Erythrocyte Ghosts; RBC Ghosts | A measurement of the erythrocyte ghosts (erythrocytes in which hemoglobin has been removed through hemolysis) in a biological specimen. |
| C92296 | RBCMORPH | Erythrocyte Cell Morphology; RBC Morphology; Red Blood Cell Morphology | An examination or assessment of the form and structure of red blood cells. |
| C74705 | RBCNUC | Nucleated Erythrocytes; Nucleated Red Blood Cells | A measurement of the nucleated erythrocytes (large, immature nucleated erythrocytes) in a biological specimen. |
| C82046 | RBCNUCLE | Nucleated Erythrocytes/Leukocytes | A relative measurement (ratio or percentage) of nucleated erythrocytes to leukocytes in a biological specimen. |
| C74647 | RBCNURBC | Nucleated Erythrocytes/Erythrocytes; Nucleated Red Blood Cells/Erythrocytes | A relative measurement (ratio or percentage) of the nucleated erythrocytes (large, immature nucleated erythrocytes) to all erythrocytes in a biological specimen. |
| C100437 | RBP | Retinol Binding Protein | A measurement of the total retinol binding protein in a biological specimen. |
| C189526 | RBP1 | Retinol Binding Protein 1 | A measurement of the retinol binding protein 1 in a biological specimen. |
| C189525 | RBP2 | Retinol Binding Protein 2 | A measurement of the retinol binding protein 2 in a biological specimen. |
| C189524 | RBP3 | Retinol Binding Protein 3 | A measurement of the retinol binding protein 3 in a biological specimen. |
| C189523 | RBP4 | Retinol Binding Protein 4 | A measurement of the retinol binding protein 4 in a biological specimen. |
| C154729 | RBPCREAT | Retinol Binding Protein/Creatinine | A relative measurement (ratio or percentage) of the retinol binding protein to creatinine in a biological specimen. |
| C147428 | RDCSUB | Reducing Substances | A measurement of the reducing substances (e.g., sugars, glutathione, creatinine, uric acid, and ascorbic acid) in a biological specimen. |
| C147429 | RDCSUG | Reducing Sugars | A measurement of the reducing sugars in a biological specimen. |
| C64800 | RDW | Erythrocytes Distribution Width; RDW-CV; Red Blood Cell Distribution Width; Red Cell Volume Distribution Width | A relative measurement (ratio or percentage) of the standard deviation of the red blood cell volume to the mean distribution of the red blood cell volume in a biological specimen. |
| C139074 | RDWR | RDWr; Ret Volume Distribution Width; Reticulocyte Volume Distribution Width | A relative measurement (ratio or percentage) of the standard deviation of the reticulocyte volume to the mean distribution of the reticulocyte volume in a biological specimen. |
| C139072 | RDWRCV | RDWr-CV; Red Cell Volume Distribution Width Coefficient of Variation in Reticulocytes; Ret RDW Coefficient of Variation; Reticulocyte Volume Distribution Width Coefficient of Variation | A measurement of the volume dispersion within a reticulocyte population, calculated as the standard deviation of the mean reticulocyte volume divided by the mean reticulocyte volume, multiplied by 100 to convert to a percentage. |
| C139073 | RDWRSD | RDWr-SD; Red Cell Volume Distribution Width Standard Deviation in Reticulocytes; Ret RDW Standard Deviation; Reticulocyte Volume Distribution Width Standard Deviation | A measurement of the volume dispersion within a reticulocyte population, calculated as the width of the distribution curve at the 20 percent frequency level. |
| C139071 | RDWSD | RDW Standard Deviation; RDW-SD; Red Cell Volume Distribution Width Standard Deviation | A measurement of the volume dispersion within an erythrocyte population, calculated as the width of the distribution curve at the 20 percent frequency level. |
| C74893 | RENIN | Active Renin; Angiotensinogenase; Direct Renin; Renin | A measurement of the renin in a biological specimen. |
| C111305 | RENINA | Renin Activity | A measurement of the renin activity in a biological specimen. |
| C80205 | RESISTIN | Resistin | A measurement of the resistin in a biological specimen. |
| C102274 | RETCRRBC | HCT Corrected Reticulocytes/Erythrocytes | A relative measurement (ratio or percentage) of the hematocrit corrected reticulocytes to erythrocytes in a biological specimen. |
| C51947 | RETI | Reticulocytes | A measurement of the reticulocytes in a biological specimen. |
| C187680 | RETICE | Reticulocytes/Total Cells | A relative measurement (ratio or percentage) of reticulocytes to total cells in a biological specimen. |
| C98776 | RETICH | CHr; Ret. Corpuscular Hemoglobin Content; Reticulocyte Cellular Hemoglobin Content | A measurement of the average total amount of hemoglobin per reticulocyte. |
| C116188 | RETIH | High Absorption Reticulocytes | A measurement of the high absorption reticulocytes in a biological specimen. |
| C102273 | RETIHCR | Hematocrit Corrected Reticulocytes | A measurement of the hematocrit corrected reticulocytes in a biological specimen. |
| C116189 | RETIHRTC | High Absorption Retic/Reticulocytes | A relative measurement (ratio or percentage) of the high absorption reticulocytes to total reticulocytes in a biological specimen. |
| C116190 | RETIL | Low Absorption Reticulocytes | A measurement of the low absorption reticulocytes in a biological specimen. |
| C116191 | RETILRTC | Low Absorption Retic/Reticulocytes | A relative measurement (ratio or percentage) of the low absorption reticulocytes to total reticulocytes in a biological specimen. |
| C116192 | RETIM | Medium Absorption Reticulocytes | A measurement of the medium absorption reticulocytes in a biological specimen. |
| C116193 | RETIMRTC | Medium Absorption Retic/Reticulocytes | A relative measurement (ratio or percentage) of the medium absorption reticulocytes to total reticulocytes in a biological specimen. |
| C187824 | RETINOAC | Retinoate; Retinoic Acid | A measurement of the retinoic acid in a biological specimen. |
| C64828 | RETIRBC | Reticulocytes/Erythrocytes | A relative measurement (ratio or percentage) of reticulocytes to erythrocytes in a biological specimen. |
| C135442 | RETPALM | Retinol Palmitate; Retinyl Palmitate; Vitamin A Palmitate | A measurement of the endogenous retinyl palmitate vitamin A in a biological specimen. |
| C74717 | RF | Rheumatoid Factor | A measurement of the rheumatoid factor antibody in a biological specimen. |
| C120652 | RFIGAAB | Rheumatoid Factor IgA Antibody | A measurement of the rheumatoid factor IgA antibody in a biological specimen. |
| C120653 | RFIGGAB | Rheumatoid Factor IgG Antibody | A measurement of the rheumatoid factor IgG antibody in a biological specimen. |
| C120654 | RFIGMAB | Rheumatoid Factor IgM Antibody | A measurement of the rheumatoid factor IgM antibody in a biological specimen. |
| C92948 | RH | Rh Factor | A measurement of non-specified Rhesus factor antigen(s) in a biological specimen. |
| C125948 | RHD | RhD Factor | A measurement of the Rhesus factor D antigen in a biological specimen. |
| C170582 | RITALAC | Ritalinic Acid | A measurement of the ritalinic acid in a biological specimen. |
| C120655 | RLP | RLP Cholesterol | A measurement of the cholesterol remnant-like particles in a biological specimen. |
| C120656 | RMNTLP | Remnant Lipoprotein | A measurement of the remnant lipoproteins in a biological specimen. |
| C132301 | RNA | Ribonucleic Acid | A measurement of a targeted ribonucleic acid (RNA) in a biological specimen. |
| C120657 | RNP70AB | Ribonucleoprotein-70 Antibody; snRNP70 Antibody | A measurement of the small nuclear ribonucleoprotein 70 antibody in a biological specimen. |
| C100457 | RNPAB | Ribonucleoprotein Antibody; Ribonucleoprotein Extractable Nuclear Antibody; RNP Antibody | A measurement of the total ribonucleoprotein antibodies in a biological specimen. |
| C120658 | RNPSMAB | Ribonucleoprotein Smith Complex Antibody | A measurement of the ribonucleoprotein Smith complex antibody in a biological specimen. |
| C122146 | ROM | Reactive Oxygen Metabolite | A measurement of the reactive oxygen metabolite in a biological specimen. |
| C74624 | ROULEAUX | Rouleaux Formation | A measurement of the stacking red blood cells in a biological specimen. |
| C142288 | ROUNDCE | Round Cells | A measurement of the round cells (round shaped cells mainly comprised of white blood cells and immature spermatogenic cells) in a biological specimen. |
| C122147 | RP3IGGAB | RNA Polymerase III IgG Antibody | A measurement of the RNA polymerase III IgG antibody in a biological specimen. |
| C142289 | RPA1 | Renal Papillary Antigen 1 | A measurement of the renal papillary antigen 1 in a biological specimen. |
| C120659 | RPPAB | Ribosomal P Protein Antibody | A measurement of the total ribosomal P protein antibody in a biological specimen. |
| C147430 | RPTLAAC | Reptilase Activity Actual/Control; Reptilase Activity Actual/Normal; Reptilase Activity Actual/Reptilase Activity Control | A relative measurement (ratio or percentage) of the biological activity of reptilase dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C96628 | RPTLTIME | Reptilase Time | A measurement of the time it takes a plasma sample to clot after adding the active enzyme reptilase. |
| C163484 | RSAD2 | Cytomegalovirus-Induced Gene 5 Protein; Radical S-adenosyl Methionine Domain-Containing Protein 2 | A measurement of the cytomegalovirus-induced gene 5 protein in a biological specimen. |
| C177971 | RSOH9RS | Risperidone+9-Hydroxyrisperidone; Risperidone+Paliperidone | A measurement of the risperidone and 9-hydroxyrisperidone in a biological specimen. |
| C177969 | RSPDN | Risperidone | A measurement of the risperidone in a biological specimen. |
| C81968 | RT3 | Triiodothyronine, Reverse | A measurement of the reverse triiodothyronine in a biological specimen. |
| C128978 | RUB | Polychromatophilic Erythroblast; Polychromatophilic Normoblast; Rubricyte | A measurement of the rubricytes in a biological specimen. |
| C129006 | RUBCE | Rubricyte/Total Cells | A relative measurement (ratio or percentage) of the rubricytes to total cells in a biological specimen. |
| C154730 | S100A8 | S100 Calcium Binding Protein A8 | A measurement of the S100 calcium binding protein A8 in a biological specimen. |
| C127635 | S100B | S100 Calcium-Binding Protein B | A measure of the S100 calcium-binding protein B in a biological specimen. |
| C165981 | S6PHS | Phos-S6 Ribosomal Protein; Phosphorylated S6 protein of the 40S ribosomal subunit | A measurement of the phosphorylated S6 protein of the 40S ribosomal subunit in a biological specimen. |
| C165982 | SAA1 | PIG4; SAA1; Serum Amyloid A-1 Protein; Serum Amyloid A1 | A measurement of the serum amyloid A1 in a biological specimen. |
| C186093 | SAAG | SAAG; Serum-Ascites Albumin Gradient | A measurement of the serum-ascites albumin gradient, calculated by subtracting the amount of albumin in ascites fluid from the albumin in serum. |
| C172516 | SAHOMC | S-adenosyl-L-homocysteine; S-Adenosylhomocysteine; SAH | A measurement of the S-adenosylhomocysteine in a biological specimen. |
| C147431 | SALCYLT | Salicylates | A measurement of the salicylates in a biological specimen. |
| C172515 | SAMETH | S-adenosyl-L-methionine; S-Adenosylmethionine; SAM-e; SAMe; SAMMY | A measurement of the S-adenosylmethionine in a biological specimen. |
| C174311 | SAO2FIO2 | Oxygen Saturation/Fraction Inspired O2 | A relative measurement (ratio or percentage) of the oxygen-hemoglobin saturation of a volume of blood to the volumetric fraction of oxygen in the inhaled gas. |
| C154760 | SARCOSIN | N-Methylglycine; Sarcosine | A measurement of the sarcosine in a biological specimen. |
| C184635 | SBUTRMN | Sibutramine | A measurement of the sibutramine in a biological specimen. |
| C75369 | SCBRBTL | Secobarbital | A measurement of the secobarbital present in a biological specimen. |
| C120660 | SCCAG | Squamous Cell Carcinoma Antigen | A measurement of the squamous cell carcinoma antigen in a biological specimen. |
| C82035 | SCF | KIT Ligand; Stem Cell Factor | A measurement of the stem cell factor in a biological specimen. |
| C186094 | SCHISRBC | Schistocytes/Erythrocytes | A relative measure (ratio or percentage) of schistocytes to erythrocytes in a biological specimen. |
| C74706 | SCHISTO | Schistocytes | A measurement of the schistocytes (fragmented red blood cells) in a biological specimen. |
| C74656 | SCKCERBC | Sickle Cells/Erythrocytes | A relative measurement (ratio or percentage) of the sickle cells (sickle shaped red blood cells) to all erythrocytes in a biological specimen. |
| C74626 | SCKLCE | Drepanocytes; Sickle Cells | A measurement of the sickle cells (sickle shaped red blood cells) in a biological specimen. |
| C100458 | SCL70AB | Scl-70 Antibody; Scleroderma-70 Antibody | A measurement of the total Scl-70 antibody in a biological specimen. |
| C122148 | SCL70GAB | Scl-70 IgG Antibody; Scleroderma-70 IgG Antibody | A measurement of the Scl-70 IgG antibody in a biological specimen. |
| C154745 | SCN | Thiocyanate | A measurement of the thiocyanate in a biological specimen. |
| C186095 | SCNYLACT | Succinylacetone | A measurement of the succinylacetone in a biological specimen. |
| C79465 | SDH | Sorbitol Dehydrogenase | A measurement of the sorbitol dehydrogenase in a biological specimen. |
| C158232 | SDMA | N,N'-dimethylarginine; Symmetric Dimethylarginine | A measurement of the symmetric dimethylarginine in a biological specimen. |
| C187825 | SE | Selenium | A measurement of the selenium in a biological specimen. |
| C74871 | SECRETIN | Secretin | A measurement of the secretin hormone in a biological specimen. |
| C105744 | SEDEXAM | Microscopic Sediment Analysis; Sediment Analysis; Sediment Examination | An observation, assessment or examination of the sediment in a biological specimen. |
| C122149 | SER | Serine | A measurement of the serine in a biological specimen. |
| C147432 | SERTRAL | Sertraline | A measurement of the sertraline present in a biological specimen. |
| C187817 | SERTRALN | Norsertraline | A measurement of the norsertraline in a biological specimen. |
| C74625 | SEZCE | Sezary Cells | A measurement of the Sezary cells (atypical lymphocytes with cerebriform nuclei) in a biological specimen. |
| C158231 | SEZCELE | Sezary Cells/Leukocytes | A relative measurement (ratio or percentage) of the Sezary cells to all leukocytes in a biological specimen. |
| C74655 | SEZCELY | Sezary Cells/Lymphocytes | A relative measurement (ratio or percentage of the Sezary cells (atypical lymphocytes with cerebriform nuclei) to all lymphocytes in a biological specimen. |
| C111322 | SFTPD | SP-D; Surfactant Protein D | A measurement of the surfactant protein D in a biological specimen. |
| C165983 | SH2D1A | DSHP; Duncan Disease SH2-Protein; EBVS; IMD5; LYP; MTCP1; SAP; SAP/SH2D1A; SH2 Domain Containing 1A Protein; XLP; XLPD; XLPD1 | A measurement of the SH2 domain containing 1A protein in a biological specimen. |
| C74745 | SHBG | Sex Hormone Binding Globulin; Sex Hormone Binding Protein | A measurement of the sex hormone binding (globulin) protein in a biological specimen. |
| C177989 | SHH | Sonic Hedgehog | A measurement of the sonic hedgehog protein in a biological specimen. |
| C132386 | SICAM1 | Soluble Intercell Adhesion Molecule 1 | A measurement of the soluble intercellular adhesion molecule 1 in a biological specimen. |
| C186096 | SICAM4 | Soluble Intercell Adhesion Molecule 4; Soluble Intercellular Adhesion Molecule 4 | A measurement of the soluble intercellular adhesion molecule 4 in a biological specimen. |
| C74876 | SIXMAM | 6-Monoacetylmorphine | A measurement of the 6-monoacetylmorphine present in a biological specimen. |
| C120661 | SJSA52AB | Sjogrens SS-A52 Antibody | A measurement of the Sjogrens SS-A52 antibody in a biological specimen. |
| C120662 | SJSA60AB | Sjogrens SS-A60 Antibody | A measurement of the Sjogrens SS-A60 antibody in a biological specimen. |
| C92236 | SJSSAAB | Ro Antibody; Sjogrens SS-A Antibody | A measurement of the Sjogrens SS-A antibody in a biological specimen. |
| C92237 | SJSSBAB | La Antibody; Sjogrens SS-B Antibody | A measurement of the Sjogrens SS-B antibody in a biological specimen. |
| C122150 | SLAIGGAB | Soluble Liver Antigen IgG Antibody | A measurement of the soluble liver antigen IgG antibody in a biological specimen. |
| C100438 | SLTFRNRC | Soluble Transferrin Receptor | A measurement of the soluble transferrin receptor in a biological specimen. |
| C114223 | SLXAG | Sialyl Lewis X Antigen; Sialyl Lex; Sialyl SSEA-1 Antigen; Sialyl-CD15; SLeX | A measurement of the sialyl stage-specific embryonic antigen-1 in a biological specimen. |
| C74627 | SMDGCE | Basket Cells; Gumprecht Shadow Cells; Shadow Cells; Smudge Cells | A measurement of the smudge cells (the nuclear remnant of a ruptured white blood cell) in a biological specimen. |
| C119294 | SMDGCELE | Basket Cells/Leukocytes; Gumprecht Shadow Cells/Leukocytes; Shadow Cells/Leukocytes; Smudge Cells/Leukocytes | A relative measurement (ratio or percentage) of smudge cells to leukocytes in a biological specimen. |
| C189495 | SMRP | Soluble Mesothelin Related Peptides; Soluble Mesothelin Related Proteins | A measurement of the soluble mesothelin related peptides in a biological specimen. |
| C92281 | SMTHAB | Smith Antibody; Smith Extractable Nuclear Antibody | A measurement of the total Smith antibodies in a biological specimen. |
| C111317 | SMUSCAB | Anti-Smooth Muscle Antibody; Smooth Muscle Antibody | A measurement of the total smooth muscle antibody in a biological specimen. |
| C122151 | SMUSCGAB | Actin IgG Antibody; Smooth Muscle IgG Antibody | A measurement of the smooth muscle IgG antibody in a biological specimen. |
| C114224 | SO2 | Sulfur Dioxide | A measurement of the sulfur dioxide in a biological specimen. |
| C64809 | SODIUM | Sodium | A measurement of the sodium in a biological specimen. |
| C150823 | SODMEXR | Sodium Excretion Rate | A measurement of the amount of sodium being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C80360 | SOMATRO | Growth Hormone; Somatotrophin; Somatotropin | A measurement of the somatotrophin (growth) hormone in a biological specimen. |
| C117857 | SOST | Sclerostin | A measurement of the sclerostin in a biological specimen. |
| C74663 | SPERM | Spermatozoa | A measurement of the spermatozoa cells present in a biological specimen. |
| C102281 | SPERMMTL | Sperm Motility | A measurement of the sperm capable of forward, progressive movement in a semen specimen. |
| C161366 | SPERMP | Spermatozoa, Progressive | A measurement of the progressive spermatozoa (motile in a forward direction) in a biological specimen. |
| C64832 | SPGRAV | Specific Gravity | A ratio of the density of a fluid to the density of water. |
| C74707 | SPHERO | Spherocytes | A measurement of the spherocytes (small, sphere-shaped red blood cells) in a biological specimen. |
| C120663 | SPLA2II | Type II Secretory Phospholipase A2 | A measurement of the type II secretory phospholipase A2 in a biological specimen. |
| C142290 | SPMAGGLU | Sperm Agglutination | A measurement of the motile spermatozoa agglutination in a biological specimen. |
| C142291 | SPMAGGR | Sperm Aggregation | A measurement of the immotile spermatozoa aggregation in a biological specimen. |
| C147433 | SPMMSPM | Motile Sperm/Total Sperm | A relative measurement (ratio or percentage) of the motile sperm to total sperm in a biological specimen. |
| C161365 | SPMPSPM | Spermatozoa, Progressive/Spermatozoa | A relative measurement (ratio or percentage) of the progressive spermatozoa to total spermatozoa in a biological specimen. |
| C106569 | SPWEIGHT | Specimen Weight | A measurement of the weight of a biological specimen. |
| C74872 | SRTONIN | Serotonin | A measurement of the serotonin hormone in a biological specimen. |
| C165984 | SSTR2 | Somatostatin Receptor Type 2; SRIF-1 | A measurement of the somatostatin receptor type 2 in a biological specimen. |
| C156469 | STAT3 | Signal Transducer and Activator of Transcription 3; STAT3 | A measurement of the STAT3 (signal transducer and activator of transcription 3) in a biological specimen. |
| C156521 | STAT3P | Phosphorylated STAT3; pSTAT3 | A measurement of the phosphorylated STAT3 (signal transducer and activator of transcription 3) in a biological specimen. |
| C156522 | STAT3PS3 | Phosphorylated STAT3/STAT3; pSTAT3/STAT3 | A relative measurement (ratio or percentage) of the phosphorylated STAT3 to total STAT3 in a biological specimen. |
| C154721 | STBSEXCS | Standard Base Excess | A calculated measurement of the amount of acid required to return blood with hemoglobin at 5g/dL, which is used as a surrogate for extracellular fluid, to a normal pH under standard conditions. |
| C96567 | STIPBASO | Basophilic Stippling | A measurement of the basophilic stippling in a biological specimen. |
| C184600 | STNBLN | Deacetylanatrofin; Stenbolone | A measurement of the stenbolone in a biological specimen. |
| C184599 | STNZLL | Stanozolol | A measurement of the stanozolol in a biological specimen. |
| C74708 | STOMCY | Stomatocytes | A measurement of the stomatocytes (red blood cells with an oval or rectangular area of central pallor, producing the appearance of a cell mouth) in a biological specimen. |
| C135443 | STROPONI | Skeletal Troponin I; sTnl | A measurement of the total skeletal troponin I in a biological specimen. |
| C177993 | STS | Steroid Sulfatase; Steryl-sulfatase | A measurement of the steroid sulfatase in a biological specimen. |
| C184575 | SUFNTNL | Sufentanil | A measurement of the sufentanil in a biological specimen. |
| C122153 | SULFATE | Sulfate; Sulphate | A measurement of the sulfate in a biological specimen. |
| C92533 | SVCAM1 | Soluble Vasc Cell Adhesion Molecule 1 | A measurement of the soluble vascular cell adhesion molecule 1 in a biological specimen. |
| C74747 | T3 | Total T3; Triiodothyronine | A measurement of the total (free and bound) triiodothyronine in a biological specimen. |
| C74787 | T3FR | Free T3; Triiodothyronine, Free | A measurement of the free triiodothyronine in a biological specimen. |
| C74748 | T3UP | T3RU; T3U; Triiodothyronine Uptake | A measurement of the binding of triiodothyronine to thyroxine binding globulin protein in a biological specimen. |
| C74794 | T4 | Thyroxine; Total T4 | A measurement of the total (free and bound) thyroxine in a biological specimen. |
| C74786 | T4FR | Free T4; Thyroxine, Free | A measurement of the free thyroxine in a biological specimen. |
| C170598 | T4FRIDX | Thyroxine, Free Index | A measurement of the thyroid status in a biological specimen. This is calculated by a mathematical formula that takes into account the total thyroxine and unbound thyroxine binding globulins. |
| C120664 | T4FRIND | Thyroxine, Free, Indirect | An indirect measurement of the free thyroxine in a biological specimen. |
| C163486 | TAP1 | Antigen Peptide Transporter 1; Peptide Transporter TAP1 | A measurement of the peptide transporter TAP1 in a biological specimen. |
| C106574 | TAT | Thrombin/Antithrombin; Thrombin/Antithrombin III | A relative measurement (ratio or percentage) of the thrombin to antithrombin present in a sample. |
| C161371 | TATC | TAT; Thrombin Antithrombin Complex; Thrombin Antithrombin Complex Antigen | A measurement of the thrombin-antithrombin complexes in a biological specimen. |
| C187821 | TAU181P | Phosphorylated Tau 181; Phosphorylated Tau Protein 181 | A measurement of the phosphorylated Tau protein 181 in a biological specimen. |
| C158223 | TAURCRT | Taurine/Creatinine | A relative measurement (ratio) of the taurine to the creatinine in a biological specimen. |
| C122154 | TAURINE | Tauric Acid; Taurine | A measurement of the taurine in a biological specimen. |
| C74746 | TBG | Thyroxine Binding Globulin | A measurement of the thyroxine binding globulin protein in a biological specimen. |
| C189496 | TBP | TATA Box Binding Protein; TATA-Binding Protein | A measurement of the TATA-box binding protein in a biological specimen. |
| C176306 | TCDCA | Taurochenodeoxycholate; Taurochenodeoxycholic Acid | A measurement of the taurochenodeoxycholate in a biological specimen. |
| C176301 | TCHT | Taurocholate; Taurocholic Acid | A measurement of the taurocholate in a biological specimen. |
| C117859 | TDTAG | Terminal Deoxynucleotidyl Transferase Ag; Terminal Deoxynucleotidyl Transferase Antigen | A measurement of the terminal deoxynucleotidyl transferase antigen in a biological specimen. |
| C64801 | TEARDCY | Dacryocytes; Tear Shaped Erythrocytes; Teardrop Cells | A measurement of dacryocytes in a biological specimen. |
| C74793 | TESTOS | Testosterone; Total Testosterone | A measurement of the total (free and bound) testosterone in a biological specimen. |
| C117860 | TESTOSBA | Bioavailable Testosterone | A measurement of bioavailable testosterone in a biological specimen. |
| C74785 | TESTOSFR | Testosterone, Free | A measurement of the free testosterone in a biological specimen. |
| C147434 | TESTOSWB | Testosterone, Weakly Bound | A measurement of the weakly bound testosterone (testosterone bound to albumin) in a biological specimen. |
| C82037 | TFERRIN | Transferrin | A measurement of the total transferrin in a biological specimen. |
| C98792 | TFRRNSAT | Iron Binding Capacity Saturation; Iron Saturation; Iron to TIBC; Transferrin Saturation | A measurement of the iron bound to transferrin in a biological specimen. |
| C165985 | TGFA | Transforming Growth Factor Alpha | A measurement of the transforming growth factor alpha in a biological specimen. |
| C122155 | TGFB | Transforming Growth Factor Beta | A measurement of the total transforming growth factor beta in a biological specimen. |
| C117861 | TGFB1 | Transforming Growth Factor Beta 1 | A measurement of the transforming growth factor beta 1 in a biological specimen. |
| C165986 | TGFB2 | G-TSF; LDS4; TGF-beta2; Transforming Growth Factor Beta 2 | A measurement of the transforming growth factor beta 2 in a biological specimen. |
| C165987 | TGFB3 | ARVD; ARVD1; LDS5; RNHF; TGF-beta3; Transforming Growth Factor Beta 3 | A measurement of the transforming growth factor beta 3 in a biological specimen. |
| C103446 | TGLOB | TG; Thyroglobulin | A measurement of the thyroglobulin in a biological specimen. |
| C147435 | TGLOBRR | Thyroglobulin Recovery Rate | A measurement of the thyroglobulin recovery rate in a biological specimen obtained by measuring the thyroglobulin concentration before and after a known amount of thyroglobulin has been added to the specimen. |
| C135444 | THBD | BDCA3; Thrombomodulin | A measurement of the thrombomodulin in a biological specimen. |
| C147436 | THC | Delta-9-Tetrahydrocannabinol; Tetrahydrocannabinol; THC | A measurement of the tetrahydrocannabinol in a biological specimen. |
| C142293 | THCCOOH | 11-Nor-Delta9-THC-9-Carboxylic Acid; THC-COOH | A measurement of 11-nor-delta-9-tetrahydrocannabinol-9-carboxylic acid present in a biological specimen. |
| C186097 | THDCSL5A | 5-Alpha Tetrahydrocortisol | A measurement of the 5-alpha tetrahydrocortisol in a biological specimen. |
| C184577 | THEBAINE | Thebaine | A measurement of the thebaine in a biological specimen. |
| C105445 | THEOPHYL | Theophylline | A measurement of the Theophylline present in a biological specimen. |
| C184602 | THGSTNON | Tetrahydrogestrinone | A measurement of the tetrahydrogestrinone in a biological specimen. |
| C184604 | THIOPNTL | Thiopental | A measurement of the thiopental in a biological specimen. |
| C177978 | THIORDZN | Thioridazine | A measurement of the thioridazine in a biological specimen. |
| C177976 | THIOTHXN | Thiothixene | A measurement of the thiothixene in a biological specimen. |
| C147437 | THMBAAC | Thrombin Activity Actual/Control; Thrombin Activity Actual/Normal; Thrombin Activity Actual/Thrombin Activity Control | A relative measurement (ratio or percentage) of the biological activity of thrombin dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C184603 | THMYLL | Thiamylal | A measurement of the thiamylal in a biological specimen. |
| C122156 | THR | Threonine | A measurement of the threonine in a biological specimen. |
| C158224 | THRCREAT | Threonine/Creatinine | A relative measurement (ratio) of the threonine to the creatinine in a biological specimen. |
| C74873 | THRMPTN | Thrombopoietin | A measurement of the thrombopoietin hormone in a biological specimen. |
| C111283 | THROMNUC | Nucleated Thrombocytes; Thrombocytes | A measurement of the nucleated platelets, namely thrombocytes, in a biological specimen. This is typically measured in birds and other non-mammalian vertebrates. |
| C81990 | THYAB | Thyroid Antibodies | A measurement of the thyroid antibodies in a biological specimen. |
| C81992 | THYATAB | Thyroid Antithyroglobulin Antibodies | A measurement of the thyroid antithyroglobulin antibodies in a biological specimen. |
| C96639 | THYPXD | Thyroid Peroxidase; Thyroperoxidase | A measurement of the thyroperoxidase in a biological specimen. |
| C96638 | THYPXDAB | Thyroid Antimicrosomal Antibody; Thyroperoxidase Antibody | A measurement of the thyroperoxidase antibody in a biological specimen. |
| C163487 | TIMM10 | Translocase Inner Mitochondrial Membr 10; Translocase of Inner Mitochondrial Membrane 10 | A measurement of the translocase of inner mitochondrial membrane 10 in a biological specimen. |
| C82036 | TIMP1 | Tissue Inhibitor of Metalloproteinase 1 | A measurement of the tissue inhibitor of metalloproteinase 1 in a biological specimen. |
| C106575 | TIMP1CRE | TIMP1/Creatinine; Tissue Inhibitor of Metalloproteinase 1/Creatinine | A relative measurement (ratio or percentage) of the tissue inhibitor of metalloproteinase 1 to creatinine present in a sample. |
| C165988 | TIMP3 | HSMRK222; K222; K222TA2; Metalloproteinase Inhibitor 3; SFD; Tissue Inhibitor of Metalloproteinase 3 | A measurement of the tissue inhibitor of metalloproteinase 3 in a biological specimen. |
| C120665 | TK | Thymidine Kinase | A measurement of the total thymidine kinase in a biological specimen. |
| C135445 | TK1 | Thymidine Kinase 1; Thymidine Kinase, Cytosolic | A measurement of the thymidine kinase 1 in a biological specimen. |
| C135446 | TK2 | Thymidine Kinase 2; Thymidine Kinase, Mitochondrial | A measurement of the thymidine kinase 2 in a biological specimen. |
| C132387 | TKG | T-Kininogen | A measurement of the total T-kininogen in a biological specimen. |
| C176309 | TLCHT | Taurolithocholate; Taurolithocholic Acid | A measurement of the taurolithocholate in a biological specimen. |
| C122157 | TLYCE | T-Cell Lymphocytes; T-Cells; T-Lymphocytes | A measurement of the total thymocyte-derived lymphocytes in a biological specimen. |
| C128979 | TLYMXM | T-lymphocyte Crossmatch | A measurement to determine human leukocyte antigens (HLA) histocompatibility between the recipient and the donor by examining the presence or absence of the recipient's anti-HLA antibody reactivity towards HLA antigens expressed on the donor T-lymphocytes. |
| C184563 | TMEPRDN | Trimeperidine | A measurement of the trimeperidine in a biological specimen. |
| C75376 | TMZPM | Temazepam | A measurement of the temazepam present in a biological specimen. |
| C74751 | TNF | Tumor Necrosis Factor; Tumor Necrosis Factor alpha | A measurement of the total tumor necrosis factor (cachexin) cytokine in a biological specimen. |
| C165989 | TNF10 | APO2L; CD253; TL2; TNF-Related Apoptosis-Inducing Ligand; TNFSF10; TNLG6A; TRAIL | A measurement of the total tumor necrosis factor superfamily member 10 in a biological specimen. |
| C165990 | TNF12 | APO3L; DR3LG; TNF Superfamily Member 12; TNLG4A; TWEAK | A measurement of the total tumor necrosis factor superfamily member 12 in a biological specimen. |
| C156525 | TNF12EXR | TNF Superfamily Member 12 Excretion Rate; TWEAK Excretion Rate | A measurement of the amount of TNF superfamily member 12 being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C156526 | TNF12S | Soluble TNF Superfamily Member 12; Soluble TNFSF12 | A measurement of soluble tumor necrosis factor superfamily member 12 in a biological specimen. |
| C174308 | TNF5S | Soluble CD154; Soluble CD40 Ligand; Soluble CD40L; Soluble CD40LG; Soluble gp39; Soluble T-BAM; Soluble TNF Superfamily Member 5; Soluble TNFSF5; Soluble TRAP | A measurement of the soluble tumor necrosis factor superfamily member 5 in a biological specimen. |
| C117862 | TNFAPI | TNF-a Production Inhibition; TNF-a Production Inhibitory Activity | A measurement of TNF-a production inhibitory activity in a biological specimen. |
| C120666 | TNFR1 | CD120a; Tumor Necrosis Factor Receptor 1 | A measurement of the tumor necrosis factor receptor 1 (CD120a) in a biological specimen. |
| C165991 | TNFR1B | CD120b; p75; p75TNFR; TBPII; TNF Receptor 1B; TNF-R-II; TNF-R75; TNFBR; TNFR1B; TNFR2; TNFR80; Tumor Necrosis Factor Receptor 2 | A measurement of the tumor necrosis factor receptor superfamily member 1B in a biological specimen. |
| C174312 | TNFR5S | Soluble B-cell Surface Antigen CD40; Soluble Bp50; Soluble CD40; Soluble CDW40; Soluble p50; Soluble TNF Receptor Superfamily Mem 5; Soluble TNF Receptor Superfamily Member 5; Soluble TNFRSF5; Soluble Tumor Necrosis Factor Receptor Superfamily, Member 5 | A measurement of the soluble tumor necrosis factor receptor superfamily member 5 (CD40) in a biological specimen. |
| C117749 | TNFSR | Soluble Tumor Necrosis Factor Receptor | A measurement of the total soluble tumor necrosis factor receptor in a biological specimen. |
| C117863 | TNFSR1 | Soluble TNF Receptor Type I | A measurement of the soluble tumor necrosis factor receptor type I in a biological specimen. |
| C117864 | TNFSR2 | Soluble CD120b; Soluble TNF Receptor 1B; Soluble TNF Receptor Type II; Soluble TNFR1B | A measurement of the soluble tumor necrosis factor receptor type II in a biological specimen. |
| C187827 | TOMREG2 | Tomoregulin-2; Transmembrane Protein With EGF-Like And Two Follistatin-Like Domains 2 | A measurement of the tomoregulin-2 in a biological specimen. |
| C96641 | TOXGRAN | Toxic Granulation | A measurement of the toxic granulation in granulocytic blood cells. |
| C127813 | TOXVAC | Toxic Vacuolation | A measurement of the toxic vacuolation in any of the granulocytic blood cells. |
| C81993 | TPAAG | Tissue Plasminogen Activator Antigen | A measurement of the tissue plasminogen activator antigen in a biological specimen. |
| C163488 | TPAG | Tissue Polypeptide Antigen; TPA | A measurement of the tissue polypeptide antigen in a biological specimen. |
| C184576 | TPNTDL | Tapentadol | A measurement of the tapentadol in a biological specimen. |
| C84811 | TPRONP | Non-Phosphorylated Tau Protein | A measurement of the non-phosphorylated Tau protein in a biological specimen. |
| C84810 | TPROT | Tau Protein; Total Tau Protein | A measurement of the total Tau protein in a biological specimen. |
| C163489 | TPROTFR | Tau Protein, Free | A measurement of the free tau protein in a biological specimen. |
| C84812 | TPROTP | Phosphorylated Tau Protein | A measurement of the phosphorylated Tau protein in a biological specimen. |
| C117865 | TRACP5B | Tartrate-Resistant Acid Phosphatase 5b; TRAP5B | A measurement of tartrate-resistant acid phosphatase 5b in a biological specimen. |
| C161376 | TRAMADOL | Tramadol | A measurement of the tramadol present in a biological specimen. |
| C163490 | TRANK1 | TPR and Ankyrin Repeat-Containing Protein 1; TPR-Ankyrin Repeat-Containing Protein 1 | A measurement of the TPR-ankyrin repeat-containing protein 1 in a biological specimen. |
| C80208 | TRAP | Total Radical-Trap Antioxidant Potential | A measurement of the ability of the antioxidants in a biological specimen to buffer free radicals in a suspension. |
| C100420 | TRCYANDP | Tricyclic Antidepressants | A measurement of tricyclic antidepressants in a biological specimen. |
| C96636 | TRGTCE | Codocytes; Target Cells | A measurement of the target cells in a biological specimen. |
| C74874 | TRH | Thyrotropin Releasing Factor; Thyrotropin Releasing Hormone | A measurement of the thyrotropin releasing hormone in a biological specimen. |
| C92238 | TRICH | Trichomonas | Examination of a biological specimen to detect the presence of any protozoan belonging to the Trichomonas genus. |
| C177982 | TRIFLPZN | Trifluoperazine | A measurement of the trifluoperazine in a biological specimen. |
| C64812 | TRIG | Triglycerides | A measurement of the triglycerides in a biological specimen. |
| C121183 | TRIGHDL | Triglycerides/HDL Cholesterol | A relative measurement (ratio or percentage) of the triglycerides to high density lipoprotein cholesterol in a biological specimen. |
| C163491 | TRIM21 | E3 Ubiquitin-Protein Ligase TRIM21; Ro(SS-A); Sjogren Syndrome Type A Antigen; Tripartite Motif Containing Protein 21 | A measurement of the tripartite motif containing protein 21 in a biological specimen. |
| C187799 | TRIM33 | E3 Ubiquitin-Protein Ligase TRIM33; Tripartite Motif Containing 33 | A measurement of the E3 ubiquitin-protein ligase TRIM33 in a biological specimen. |
| C163492 | TRIM38 | Tripartite Motif Containing Protein 38 | A measurement of the tripartite motif containing protein 38 in a biological specimen. |
| C184605 | TRNBLN | 17beta-Trenbolone; Trenbolone; Trienbolone | A measurement of the trenbolone in a biological specimen. |
| C74749 | TROPONI | Troponin I | A measurement of the actin binding troponin in a biological specimen. |
| C135447 | TROPONI1 | Slow-Twitch Skeletal Muscle Troponin I; ssTnI; Troponin I Type 1 | A measurement of the troponin I type 1 (slow twitch skeletal muscle) in a biological specimen. |
| C127636 | TROPONI2 | Fast-Twitch Skeletal Muscle Troponin I; fsTnI; Troponin I Type 2 | A measurement of the troponin I type 2 (fast twitch skeletal muscle) in a biological specimen. |
| C135448 | TROPONI3 | Cardiac Troponin I; cTnI; TNNC1; Troponin I Type 3 | A measurement of the troponin I type 3 (cardiac muscle) in a biological specimen. |
| C111327 | TROPONIN | Troponin | A measurement of the total troponin in a biological specimen. |
| C74750 | TROPONT | Troponin T | A measurement of the tropomyosin binding troponin in a biological specimen. |
| C154739 | TRP | Tryptophan | A measurement of the tryptophan in a biological specimen. |
| C135449 | TRP1TRG1 | Trypsin 1 and Trypsinogen 1 | A measurement of the trypsin 1 and trypsinogen 1 in a biological specimen. |
| C163493 | TRPCRT | Tryptophan/Creatinine | A relative measurement (ratio or percentage) of the tryptophan to creatinine in a biological specimen. |
| C135450 | TRPTRG | Trypsin and Trypsinogen | A measurement of the total trypsin and total trypsinogen in a biological specimen. |
| C163494 | TRYPSIN | Trypsin | A measurement of the trypsin in a biological specimen. |
| C92292 | TRYPTASE | Tryptase | A measurement of the tryptase in a biological specimen. |
| C187828 | TRZDN | Trazodone | A measurement of the trazodone in a biological specimen. |
| C181451 | TRZLM | Triazolam | A measurement of the triazolam in a biological specimen. |
| C64813 | TSH | Thyroid Stimulating Hormone; Thyrotropin | A measurement of the thyrotropin in a biological specimen. |
| C122158 | TSHRAB | Thyroid Stimulating Hormone Receptor Antibody; Thyrotropin Receptor Antibody | A measurement of the thyrotropin receptor antibody in a biological specimen. |
| C181446 | TSHT4FR | Thyroid Stimulating Hormone/Free T4; Thyrotropin/Thyroxine, Free | A relative measurement (ratio) of the thyrotropin to free thyroxine in a biological specimen. |
| C147438 | TSI | Thyroid Stimulating Immunoglobulin | A measurement of the thyroid stimulating immunoglobulin in a biological specimen. |
| C161368 | TSIAC | Thyroid Stimulating Immunoglobulin Actual/Control; Thyroid Stimulating Immunoglobulin Actual/Normal; TSI Actual/Control | A relative measurement (ratio or percentage) of the thyroid stimulating immunoglobulin in a subject's specimen when compared to a control specimen. |
| C184511 | TSLP | Thymic Stromal Lymphopoietin | A measurement of the thymic stromal lymphopoietin in a biological specimen. |
| C163495 | TSP1 | THBS1; Thrombospondin 1 | A measurement of the thrombospondin 1 in a biological specimen. |
| C181429 | TST4OH | 4-Hydroxytestosterone | A measurement of the 4-hydroxytestosterone in a biological specimen. |
| C147439 | TSTFTSTT | Testosterone, Free/Testosterone | A relative measurement (ratio or percentage) of the amount of the bioavailable testosterone compared to total testosterone in a biological specimen. |
| C147440 | TSTFWTST | Testosterone Free+Weakly Bound/Testost; Testosterone, Free and Weakly Bound/Testosterone | A relative measurement (ratio or percentage) of the free and weakly bound testosterone to total testosterone in a biological specimen. |
| C184601 | TSTLCTN | Testolactone | A measurement of the testolactone in a biological specimen. |
| C128980 | TSTSFRPT | Testosterone, Free/Total Protein | A relative measurement (ratio or percentage) of free testosterone to total proteins in a biological specimen. |
| C80365 | TT | Thrombin Time | A measurement of the time it takes a plasma sample to clot after adding the active enzyme thrombin. (NCI) |
| C161370 | TTAC | Thrombin Time Actual/Control | A relative measurement (ratio or percentage) of the thrombin time in a subject's specimen when compared to a control specimen. |
| C147441 | TTGIGAAB | Tissue Transglutaminase IgA Antibody | A measurement of the tissue transglutaminase IgA antibody in a biological specimen. |
| C163496 | TTGIGGAB | Tissue Transglutaminase IgG Antibody | A measurement of the tissue transglutaminase IgG antibody in a biological specimen. |
| C147442 | TTGIGMAB | Tissue Transglutaminase IgM Antibody | A measurement of the tissue transglutaminase IgM antibody in a biological specimen. |
| C176303 | TUDCA | Tauroursodeoxycholate; Tauroursodeoxycholic Acid | A measurement of the tauroursodeoxycholate in a biological specimen. |
| C74723 | TURB | Turbidity | A measurement of the opacity of a biological specimen. |
| C103445 | TXB2 | Thromboxane B2 | A measurement of the thromboxane B2 in a biological specimen. |
| C103344 | TXB2_D11 | 11-Dehydro-Thromboxane B2 | A measurement of the 11-dehydro-thromboxane B2 in a biological specimen. |
| C163497 | TXB2D11R | 11-Dehydro-Thromboxane B2 Excretion Rate | A measurement of the amount of 11-dehydro-thromboxane B2 being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C122159 | TYR | Tyrosine | A measurement of the tyrosine in a biological specimen. |
| C184564 | U47700 | Pink; Pinky; U-47700; U4; U47700 | A measurement of the synthetic cannabinoid U-47700 in a biological specimen. |
| C147443 | UBQN | Ubiquitin Protein | A measurement of the total ubiquitin protein in a biological specimen. |
| C189529 | UCHL1 | Ubiquitin C-Terminal Hydrolase L1; Ubiquitin Carboxy-Terminal Hydrolase L1; UCH-L1 | A measurement of the ubiquitin C-terminal hydrolase L1 in a biological specimen. |
| C176298 | UDCA | Ursodeoxycholate; Ursodeoxycholic Acid; Ursodiol | A measurement of the ursodeoxycholate in a biological specimen. |
| C176238 | UDCACM | Ursodeoxycholate Compounds; Ursodeoxycholic Acid Compounds | A measurement of the ursodeoxycholic acid, glycoursodeoxycholic acid, tauroursodeoxycholic acid, and epimerized ursodeoxycholic acid in a biological specimen. |
| C112241 | UNSPCE | Unspecified Cells | A measurement of the cells not otherwise identified or specified in a biological specimen. |
| C114225 | UNSPCECE | Unspecified Cells/Total Cells | A relative measurement (ratio or percentage) of the cells not otherwise identified or specified to total cells in a biological specimen. |
| C161364 | UNSPCELE | Unspecified Cells/Leukocytes | A relative measurement (ratio or percentage) of the cells not otherwise identified or specified to leukocytes in a biological specimen. |
| C181447 | UPA | uPA; Urokinase Plasminogen Activator | A measurement of the urokinase plasminogen activator in a biological specimen. |
| C184565 | UR144 | UR-144; UR144 | A measurement of the synthetic cannabinoid UR-144 in a biological specimen. |
| C64814 | URATE | Urate; Uric Acid | A measurement of the urate in a biological specimen. |
| C117866 | URATECRT | Urate/Creatinine | A relative measurement (ratio or percentage) of the urate to creatinine in a biological specimen. |
| C163498 | URATEEXR | Urate Excretion Rate | A measurement of the amount of urate being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C64815 | UREA | Urea | A measurement of the urea in a biological specimen. |
| C96645 | UREACRT | Urea/Creatinine | A relative measurement (ratio or percentage) of the urea to creatinine in a biological specimen. |
| C125949 | UREAN | Urea Nitrogen | A measurement of the urea nitrogen in a biological specimen. |
| C125950 | UREANCRT | Urea Nitrogen/Creatinine | A relative measurement (ratio or percentage) of the urea nitrogen to creatinine in a biological specimen. |
| C163499 | UREANEXR | Urea Nitrogen Excretion Rate | A measurement of the amount of urea nitrogen being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C64816 | UROBIL | Urobilinogen | A measurement of the urobilinogen in a biological specimen. |
| C163500 | UROTHCE | Urothelial Cells | A measurement of urothelial cells in a biological specimen. |
| C156528 | V25HD2 | 25-Hydroxycalciferol; 25-Hydroxyergocalciferol; 25-Hydroxyvitamin D2; Ercalcidiol | A measurement of the 25-Hydroxyvitamin D2 in a biological specimen. |
| C156529 | V25HD3 | 25-Hydroxycholecalciferol; 25-Hydroxyvitamin D; 25-Hydroxyvitamin D3; Calcidiol; Calcifediol; Inactive Vitamin D | A measurement of the 25-Hydroxyvitamin D3 in a biological specimen. |
| C122160 | VAL | Valine | A measurement of the valine in a biological specimen. |
| C181410 | VALPRATE | Valproate; Valproic Acid | A measurement of the valproate in a biological specimen. |
| C184517 | VAPOB | VLDL Apolipoprotein B | A measurement of the apolipoprotein B in the very low density lipoprotein fraction of a biological specimen. |
| C130166 | VBCE | Viable Cells | A measurement of the viable cells in a biological specimen. |
| C82042 | VCAM1 | Vascular Cell Adhesion Molecule 1 | A measurement of the vascular cell adhesion molecule 1 in a biological specimen. |
| C92514 | VEGF | Vascular Endothelial Growth Factor | A measurement of the vascular endothelial growth factor in a biological specimen. |
| C132389 | VEGFA | Vascular Endothelial Growth Factor A | A measurement of the vascular endothelial growth factor A in a biological specimen. |
| C163501 | VEGFC | Vascular Endothelial Growth Factor C | A measurement of the vascular endothelial growth factor C in a biological specimen. |
| C172496 | VEGFD | FIGF; Vascular Endothelial Growth Factor D | A measurement of the vascular endothelial growth factor D in a biological specimen. |
| C165992 | VEGFR1S | Soluble Vasc Endoth Growth Factor Rec1; Soluble Vascular Endothelial Growth Factor Receptor 1 | A measurement of the soluble vascular endothelial growth factor receptor 1 in a biological specimen. |
| C156527 | VEGFR2 | Vasc Endothelial Growth Factor Rec 2; Vascular Endothelial Growth Factor Receptor 2 | A measurement of the vascular endothelial growth factor receptor 2 in a biological specimen. |
| C165993 | VEGFR2S | Soluble Vasc Endoth Growth Factor Rec2; Soluble Vascular Endothelial Growth Factor Receptor 2 | A measurement of the soluble vascular endothelial growth factor receptor 2 in a biological specimen. |
| C165994 | VEGFR3S | Soluble Vasc Endoth Growth Factor Rec3; Soluble Vascular Endothelial Growth Factor Receptor 3 | A measurement of the soluble vascular endothelial growth factor receptor 3 in a biological specimen. |
| C147444 | VENLAFAX | Venlafaxine | A measurement of the venlafaxine present in a biological specimen. |
| C184606 | VINBRBTL | Vinbarbital | A measurement of the vinbarbital in a biological specimen. |
| C163502 | VIP | Vasoactive Intestinal Polypeptide; VIP | A measurement of vasoactive intestinal polypeptide in a biological specimen. |
| C75912 | VISC | Visc; Viscosity | The resistance of a liquid to sheer forces and flow. (NCI) |
| C74895 | VITA | Retinol; Vitamin A | A measurement of the Vitamin A in a biological specimen. |
| C74896 | VITB1 | Thiamine; Vitamin B1 | A measurement of the thiamine in a biological specimen. |
| C64817 | VITB12 | Cobalamin; Vitamin B12 | A measurement of the Vitamin B12 in a biological specimen. |
| C74897 | VITB17 | Amygdalin; Vitamin B17 | A measurement of the Vitamin B17 in a biological specimen. |
| C74898 | VITB2 | Riboflavin; Vitamin B2 | A measurement of the riboflavin in a biological specimen. |
| C74899 | VITB3 | Niacin; Vitamin B3 | A measurement of the niacin in a biological specimen. |
| C74900 | VITB5 | Pantothenic Acid; Vitamin B5 | A measurement of the Vitamin B5 in a biological specimen. |
| C74901 | VITB6 | Pyridoxine; Vitamin B6 | A measurement of the Vitamin B6 in a biological specimen. |
| C74902 | VITB7 | Biotin; Vitamin B7 | A measurement of the Vitamin B7 in a biological specimen. |
| C74676 | VITB9 | Folate; Folic Acid; Vitamin B9 | A measurement of the folic acid in a biological specimen. |
| C74903 | VITC | Ascorbate; Ascorbic Acid; Vitamin C | A measurement of the Vitamin C in a biological specimen. |
| C74904 | VITD2 | Calciferol; Ergocalciferol; Viosterol; Vitamin D2 | A measurement of the Vitamin D2 in a biological specimen. |
| C179751 | VITD23 | Calciferol + Cholecalciferol; Vitamin D2 + Vitamin D3 | A measurement of the vitamin D2 and vitamin D3 in a biological specimen. |
| C147445 | VITD23OH | Vitamin D + Metabolites; Vitamin D2 + Vitamin D3 + 25-Hydroxy Vitamin D2 + 25-Hydroxy Vitamin D3; Vitamin D2 D3 25-OH | A measurement of the vitamin D2, vitamin D3 and their metabolites in a biological specimen. |
| C74905 | VITD3 | Calciol; Cholecalciferol; Colecalciferol; Vitamin D; Vitamin D3 | A measurement of the Vitamin D3 in a biological specimen. |
| C172506 | VITDBP | DBP; GC Vitamin D Binding Protein; VDBP; Vitamin D Binding Protein | A measurement of the vitamin D binding protein in a biological specimen. |
| C74906 | VITE | Vitamin E | A measurement of the Vitamin E in a biological specimen. |
| C103448 | VITECHOL | Vitamin E/Cholesterol | A relative measurement (ratio or percentage) of vitamin E to total cholesterol in a biological specimen. |
| C74907 | VITK | Naphthoquinone; Vitamin K | A measurement of the total Vitamin K in a biological specimen. |
| C103449 | VITK1 | Phylloquinone; Phytomenadione; Vitamin K1 | A measurement of the Vitamin K1 in a biological specimen. |
| C105589 | VLDL | VLDL Cholesterol | A measurement of the very low density lipoprotein cholesterol in a biological specimen. |
| C120667 | VLDL1 | VLDL Cholesterol Subtype 1 | A measurement of the very low density lipoprotein cholesterol subtype 1 in a biological specimen. |
| C120668 | VLDL2 | VLDL Cholesterol Subtype 2 | A measurement of the very low density lipoprotein cholesterol subtype 2 in a biological specimen. |
| C120669 | VLDL3 | VLDL Cholesterol Subtype 3 | A measurement of the very low density lipoprotein cholesterol subtype 3 in a biological specimen. |
| C103450 | VLDLPSZ | VLDL Particle Size | A measurement of the average particle size of very-low-density lipoprotein in a biological specimen. |
| C174303 | VLDLT | VLDL Triglyceride | A measurement of the very low density lipoprotein triglyceride in a biological specimen. |
| C174301 | VLDLTCT | VLDL Trig + Chylomicron Trig; VLDL Triglyceride + Chylomicron Triglyceride | A measurement of the very low density lipoprotein triglyceride and chylomicron triglyceride in a biological specimen. |
| C187829 | VLZDN | Vilazodone | A measurement of the vilazodone in a biological specimen. |
| C74875 | VMA | Vanillyl Mandelic Acid; Vanillylmandelate; Vanilmandelic Acid | A measurement of the vanillyl mandelic acid metabolite in a biological specimen. |
| C163503 | VMAEXR | Vanillyl Mandelic Acid Excretion Rate | A measurement of the amount of vanillyl mandelic acid being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C74720 | VOLUME | Volume | A measurement of the volume of a biological specimen. |
| C187832 | VRTOXTN | Vortioxetine | A measurement of the vortioxetine in a biological specimen. |
| C179752 | VTD2125 | 1,25-Dihydroxycalciferol; 1,25-Dihydroxyergocalciferol; 1,25-Dihydroxyvitamin D2; Ercalcitriol | A measurement of the 1,25-dihydroxyvitamin D2 in a biological specimen. |
| C179753 | VTD23125 | 1,25-Di(OH)vitamin D2 + 1,25-Di(OH)vitamin D3; 1,25-Dihydroxyvitamin D2 + 1,25-Dihydroxyvitamin D3; 1,25-DihydroxyvitD2+1,25-DihydroxyvitD3 | A measurement of the 1,25-dihydroxyvitamin D2 and 1,25-dihydroxyvitamin D3 in a biological specimen. |
| C147446 | VTD2D3IT | 25-Hydroxyvit D2 + 25-Hydroxyvit D3 | A measurement of the total inactive vitamin D2 and vitamin D3 in a biological specimen. |
| C179754 | VTD3125 | 1,25-Dihydroxycholecalciferol; 1,25-Dihydroxyvitamin D; 1,25-Dihydroxyvitamin D3; Calcitriol | A measurement of the 1,25-dihydroxyvitamin D3 in a biological specimen. |
| C156511 | VTD32425 | 24,25-Dihydroxycholecalciferol; 24,25-Dihydroxyvitamin D; 24,25-Dihydroxyvitamin D3 | A measurement of the 24,25-dihydroxyvitamin D3 in a biological specimen. |
| C165995 | VTRNCTN | V75; Vitronectin; VN; VNT; VTN | A measurement of the vitronectin in a biological specimen. |
| C147447 | VWFAAC | von Will Factor Act Actual/Control; von Willebrand Factor Activity Actual/Normal; von Willebrand Factor Activity Actual/von Willebrand Factor Activity Control | A relative measurement (ratio or percentage) of the biological activity of the von Willebrand factor dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C170597 | VWFAC | von Will Factor Actual/Control; von Willebrand Factor Actual/Control; von Willebrand Factor Actual/Normal; von Willebrand Factor Actual/von Willebrand Factor Control | A relative measurement (ratio or percentage) of the von Willebrand factor in a subject's specimen when compared to a control specimen. |
| C51948 | WBC | Leukocytes; White Blood Cells | A measurement of the leukocytes in a biological specimen. |
| C135451 | WBCCE | Leukocytes/Total Cells; WBC/Total Cells | A relative measurement (ratio or percentage) of the leukocytes to total cells in a biological specimen. |
| C92246 | WBCCLMP | Leukocyte Cell Clumps; WBC Clumps; White Blood Cell Clumps | A measurement of white blood cell clumps in a biological specimen. |
| C98493 | WBCDIFF | Leukocyte Cell Differential; Leukocyte Cell Fraction; Leukocyte Diff | An overall assessment of the leukocyte subtype distribution in a biological specimen. |
| C92297 | WBCMORPH | Leukocyte Cell Morphology; WBC Morphology; White Blood Cell Morphology | An examination or assessment of the form and structure of white blood cells. |
| C127637 | WDR26 | CDW2; Macrophage Inflammatory Protein-2; MIP2; WD Repeat-Containing Protein 26 | A measurement of the WD repeat-containing protein 26 in a biological specimen. |
| C186098 | XLSXLSD | Xylose/Xylose Dose | A relative measurement (percentage) of the xylose in a biological specimen to an administered dose of xylose. |
| C147449 | XNTHCHR | Xanthochromia | A measurement of the yellowish appearance of a biological specimen due to the presence of bilirubin produced by the degradation of heme from erythrocytes that have entered the biological specimen. |
| C186099 | XYLOSE | Xylose | A measurement of the xylose in a biological specimen. |
| C74664 | YEAST | Yeast Cells | A measurement of the yeast cells present in a biological specimen. |
| C106504 | YEASTBUD | Budding Yeast; Yeast Budding | A measurement of the budding yeast present in a biological specimen. |
| C92239 | YEASTHYP | Yeast Hyphae | A measurement of the yeast hyphae present in a biological specimen. |
| C142294 | YKL40P | Chitinase-3-Like Protein 1; YKL-40 Protein | A measurement of the YKL-40 protein in a biological specimen. |
| C184636 | ZALEPLON | Zaleplon | A measurement of the zaleplon in a biological specimen. |
| C80210 | ZINC | Zinc | A measurement of the zinc in a biological specimen. |
| C177986 | ZIPRASDN | Ziprasidone | A measurement of the ziprasidone in a biological specimen. |
| C184637 | ZOLPIDEM | Zolpidem | A measurement of the zolpidem in a biological specimen. |
| C184638 | ZOPCLN | Zopiclone | A measurement of the zopiclone in a biological specimen. |
| C147452 | ZPP | Zinc Protoporphyrin | A measurement of the zinc protoporphyrin (zinc bound protoporphyrin) in a biological specimen. |

## Source: `terminology/core/lb_part3.md`

# Laboratory Codelists (Part 3)

> Codelists in this file: 1

## Laboratory Test Name (C67154)

Extensible: Yes

| Code | CDISC Submission Value | CDISC Synonym(s) | CDISC Definition |
|------|----------------------|-------------------|------------------|
| C179752 | 1,25-Dihydroxyvitamin D2 | 1,25-Dihydroxycalciferol; 1,25-Dihydroxyergocalciferol; 1,25-Dihydroxyvitamin D2; Ercalcitriol | A measurement of the 1,25-dihydroxyvitamin D2 in a biological specimen. |
| C179754 | 1,25-Dihydroxyvitamin D3 | 1,25-Dihydroxycholecalciferol; 1,25-Dihydroxyvitamin D; 1,25-Dihydroxyvitamin D3; Calcitriol | A measurement of the 1,25-dihydroxyvitamin D3 in a biological specimen. |
| C179753 | 1,25-DihydroxyvitD2+1,25-DihydroxyvitD3 | 1,25-Di(OH)vitamin D2 + 1,25-Di(OH)vitamin D3; 1,25-Dihydroxyvitamin D2 + 1,25-Dihydroxyvitamin D3; 1,25-DihydroxyvitD2+1,25-DihydroxyvitD3 | A measurement of the 1,25-dihydroxyvitamin D2 and 1,25-dihydroxyvitamin D3 in a biological specimen. |
| C132370 | 1,3-Beta-D-Glucan | 1,3-Beta-D-Glucan | A measurement of the 1,3-beta-D-glucan in a biological specimen. |
| C124334 | 1,5-Anhydroglucitol | 1,5-Anhydroglucitol | A measurement of the 1,5-anhydroglucitol in a biological specimen. |
| C154732 | 1-Hydroxymidazolam | 1'-Hydroxymidazolam; 1-Hydroxymidazolam; Alpha-Hydroxymidazolam | A measurement of the 1-Hydroxymidazolam present in a biological specimen. |
| C163497 | 11-Dehydro-Thromboxane B2 Excretion Rate | 11-Dehydro-Thromboxane B2 Excretion Rate | A measurement of the amount of 11-dehydro-thromboxane B2 being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C103344 | 11-Dehydro-Thromboxane B2 | 11-Dehydro-Thromboxane B2 | A measurement of the 11-dehydro-thromboxane B2 in a biological specimen. |
| C186042 | 11-Deoxycorticosteroids | 11-Deoxycorticoids; 11-Deoxycorticosteroid; 11-Deoxycorticosteroids | A measurement of the total 11-deoxycorticosteroids in a biological specimen. |
| C186045 | 11-Deoxycorticosterone | 11-Deoxycorticosterone; 21-Hydroxyprogesterone; Cortexone; Deoxycortone; Desoxycortone | A measurement of the 11-deoxycorticosterone in a biological specimen. |
| C186043 | 11-Deoxycortisol | 11-Deoxycortisol | A measurement of the 11-deoxycortisol in a biological specimen. |
| C186063 | 11-Hydroxyandrostenedione | 11-Hydroxyandrostenedione | A measurement of the 11-hydroxyandrostenedione in a biological specimen. |
| C186064 | 11-Hydroxyandrosterone | 11-Hydroxyandrosterone | A measurement of the 11-hydroxyandrosterone in a biological specimen. |
| C186069 | 11-Hydroxyetiocholanolone | 11-Hydroxyetiocholanolone | A measurement of the 11-hydroxyetiocholanolone in a biological specimen. |
| C186073 | 11-Ketoandrosterone | 11-Ketoandrosterone | A measurement of the 11-ketoandrosterone in a biological specimen. |
| C186074 | 11-Ketoetiocholanolone | 11-Ketoetiocholanolone | A measurement of the 11-ketoetiocholanolone in a biological specimen. |
| C142293 | 11-Nor-Delta9-THC-9-Carboxylic Acid | 11-Nor-Delta9-THC-9-Carboxylic Acid; THC-COOH | A measurement of 11-nor-delta-9-tetrahydrocannabinol-9-carboxylic acid present in a biological specimen. |
| C186065 | 17-Hydroxycorticosteroids | 17-Hydroxycorticoid; 17-Hydroxycorticosteroid; 17-Hydroxycorticosteroids | A measurement of the 17-hydroxycorticosteroids in a biological specimen. |
| C186070 | 17-Hydroxypregnenolone | 17-Hydroxypregnenolone | A measurement of the 17-hydroxypregnenolone in a biological specimen. |
| C147370 | 17-Hydroxyprogesterone | 17-Hydroxyprogesterone; 17-OHP | A measurement of the 17-Hydroxyprogesterone in a biological specimen. |
| C186075 | 17-Ketogenic steroids | 17-Ketogenic steroids | A measurement of the total 17-ketogenic steroids in a biological specimen. |
| C186076 | 17-Ketosteroids | 17-Ketosteroids | A measurement of the total 17-ketosteroids in a biological specimen. |
| C186067 | 18-Hydroxycorticosterone | 18-Hydroxycorticosterone | A measurement of the 18-hydroxycorticosterone in a biological specimen. |
| C186066 | 18-Hydroxycortisol | 18-Hydroxycortisol | A measurement of the 18-hydroxycortisol in a biological specimen. |
| C186068 | 18-Hydroxydeoxycorticosterone | 18-Hydroxydeoxycorticosterone | A measurement of the 18-hydroxydeoxycorticosterone in a biological specimen. |
| C163476 | 2-5-Oligoadenylate Synthase 1 | 2-5-Oligoadenylate Synthase 1 | A measurement of the 2-5-oligoadenylate synthase 1 in a biological specimen. |
| C163477 | 2-5-Oligoadenylate Synthase 2 | 2-5-Oligoadenylate Synthase 2 | A measurement of the 2-5-oligoadenylate synthase 2 in a biological specimen. |
| C163478 | 2-5-Oligoadenylate Synthase 3 | 2-5-Oligoadenylate Synthase 3 | A measurement of the 2-5-oligoadenylate synthase 3 in a biological specimen. |
| C177957 | 2-Methylcitrate | 2-Methylcitrate; 2-Methylcitric Acid; MCA; Methylcitrate; Methylcitric Acid | A measurement of the 2-methylcitrate in a biological specimen. |
| C181420 | 20(S)-Hydroxycholesterol | 20(S)-Hydroxycholesterol; 20-Alpha-Hydroxycholesterol | A measurement of the 20(S)-hydroxycholesterol in a biological specimen. |
| C186046 | 21-Deoxycorticosterone | 21-Deoxycorticosterone | A measurement of the 21-deoxycorticosterone in a biological specimen. |
| C186044 | 21-Deoxycortisol | 21-Deoxycortisol | A measurement of the 21-deoxycortisol in a biological specimen. |
| C181421 | 22(R)-Hydroxycholesterol | 22(R)-Hydroxycholesterol | A measurement of the 22(R)-hydroxycholesterol in a biological specimen. |
| C181422 | 22(S)-Hydroxycholesterol | 22(S)-Hydroxycholesterol | A measurement of the 22(S)-hydroxycholesterol in a biological specimen. |
| C181424 | 24(R)-Hydroxycholesterol | 24(R)-Hydroxycholesterol | A measurement of the 24(R)-hydroxycholesterol in a biological specimen. |
| C181423 | 24(S),25-Epoxycholesterol | 24(S),25-Epoxycholesterol | A measurement of the 24(S),25-epoxycholesterol in a biological specimen. |
| C181425 | 24(S)-Hydroxycholesterol | 24(S)-Hydroxycholesterol | A measurement of the 24(S)-hydroxycholesterol in a biological specimen. |
| C156511 | 24,25-Dihydroxyvitamin D3 | 24,25-Dihydroxycholecalciferol; 24,25-Dihydroxyvitamin D; 24,25-Dihydroxyvitamin D3 | A measurement of the 24,25-dihydroxyvitamin D3 in a biological specimen. |
| C181426 | 25-Hydroxycholesterol | 25-Hydroxycholesterol | A measurement of the 25-hydroxycholesterol in a biological specimen. |
| C147446 | 25-Hydroxyvit D2 + 25-Hydroxyvit D3 | 25-Hydroxyvit D2 + 25-Hydroxyvit D3 | A measurement of the total inactive vitamin D2 and vitamin D3 in a biological specimen. |
| C156528 | 25-Hydroxyvitamin D2 | 25-Hydroxycalciferol; 25-Hydroxyergocalciferol; 25-Hydroxyvitamin D2; Ercalcidiol | A measurement of the 25-Hydroxyvitamin D2 in a biological specimen. |
| C156529 | 25-Hydroxyvitamin D3 | 25-Hydroxycholecalciferol; 25-Hydroxyvitamin D; 25-Hydroxyvitamin D3; Calcidiol; Calcifediol; Inactive Vitamin D | A measurement of the 25-Hydroxyvitamin D3 in a biological specimen. |
| C181427 | 27-Hydroxycholesterol | 27-Hydroxycholesterol | A measurement of the 27-hydroxycholesterol in a biological specimen. |
| C103345 | 3,4-Dihydroxyphenylacetic Acid | 3,4-Dihydroxyphenylacetic Acid | A measurement of the 3,4-dihydroxyphenylacetic acid in a biological specimen. |
| C101017 | 3,4-Dihydroxyphenylglycol | 3,4-Dihydroxyphenylglycol; 3.4 Dihydroxyphenylglycol | A measurement of the catecholamine metabolite, 3,4-Dihydroxyphenylglycol in a biological specimen. |
| C174295 | 3,4-methylenedioxy-N-ethylamphetamine | 3,4-methylenedioxy-N-ethylamphetamine; Eve; MDE | A measurement of the 3,4-methylenedioxy-N-ethylamphetamine in a biological specimen. |
| C174294 | 3,4-methylenedioxyamphetamine | 3,4-methylenedioxyamphetamine | A measurement of the 3,4-methylenedioxyamphetamine in a biological specimen. |
| C75359 | 3,4-methylenedioxymethamphetamine | 3,4-methylenedioxymethamphetamine; Ecstasy | A measurement of the 3,4-methylenedioxymethamphetamine (MDMA) in a biological specimen. |
| C186027 | 3-Alpha-Androstanediol Glucuronide | 3-Alpha-Androstanediol Glucuronide | A measurement of the 3-alpha-androstanediol glucuronide in a biological specimen. |
| C186082 | 3-Methoxytyramine | 3-Methoxytyramine | A measurement of the total 3-methoxytyramine in a biological specimen. |
| C186083 | 3-Methoxytyramine, Free | 3-Methoxytyramine, Free | A measurement of the free 3-methoxytyramine in a biological specimen. |
| C184525 | 3-Methylfentanyl | 3-Methylfentanyl | A measurement of the 3-methylfentanyl in a biological specimen. |
| C181428 | 3beta-Hydroxy-5-Cholestenoic Acid | 3-HCOA; 3-Hydroxy-5-cholestenoic acid; 3beta-Hydroxy-5-Cholestenoic Acid | A measurement of the 3beta-hydroxy-5-cholestenoic acid in a biological specimen. |
| C156514 | 4-Beta-Hydroxycholesterol | 4-Beta-Hydroxycholesterol | A measurement of the 4-beta-hydroxycholesterol in a biological specimen. |
| C154731 | 4-Hydroxymidazolam | 4-Hydroxymidazolam | A measurement of the 4-hydroxymidazolam present in a biological specimen. |
| C187788 | 4-Hydroxynonenal | 4-HNE; 4-hydroxy-2-nonenal; 4-Hydroxynonenal; HNE | A measurement of the 4-hydroxynonenal in a biological specimen. |
| C181429 | 4-Hydroxytestosterone | 4-Hydroxytestosterone | A measurement of the 4-hydroxytestosterone in a biological specimen. |
| C79437 | 5 Prime Nucleotidase | 5 Prime Nucleotidase; 5'-Ribonucleotide Phosphohydrolase | A measurement of the 5'-nucleotidase in a biological specimen. |
| C186097 | 5-Alpha Tetrahydrocortisol | 5-Alpha Tetrahydrocortisol | A measurement of the 5-alpha tetrahydrocortisol in a biological specimen. |
| C184560 | 5-fluoro PB-22 3-carboxyindole | 5-fluoro PB-22 3-carboxyindole | A measurement of the synthetic cannabinoid metabolite 5-fluoro PB-22 3-carboxyindole in a biological specimen. |
| C112217 | 5-Hydroxyindoleacetic Acid | 5-Hydroxyindoleacetate; 5-Hydroxyindoleacetic Acid | A measurement of 5-hydroxyindoleacetic acid in a biological specimen. |
| C170578 | 5-Hydroxyindoleacetic Acid/Creatinine | 5-Hydroxyindoleacetic Acid/Creatinine | A relative measurement (ratio or percentage) of the 5-hydroxyindoleacetic acid to creatinine in a biological specimen. |
| C163454 | 5-HydroxyindoleaceticAcid Excretion Rate | 5-Hydroxyindoleacetic Acid Excretion Rate; 5-HydroxyindoleaceticAcid Excretion Rate | A measurement of the amount of 5-hydroxyindoleacetic acid being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C150833 | 6 Beta-Hydroxycortisol | 6 Beta-Hydrocortisol; 6 Beta-Hydroxycortisol; 6 beta-OHF | A measurement of 6 beta-hydroxycortisol in a biological specimen. |
| C74876 | 6-Monoacetylmorphine | 6-Monoacetylmorphine | A measurement of the 6-monoacetylmorphine present in a biological specimen. |
| C186058 | 6a OH-tetrahydro-11-DeH-Corticosterone | 6-Alpha Hydroxytetrahydro-11-Dehydrocorticosterone; 6a OH-tetrahydro-11-DeH-Corticosterone | A measurement of the 6-alpha hydroxytetrahydro-11-dehydrocorticosterone in a biological specimen. |
| C186059 | 6a OH-tetrahydro-11-Deoxycortisol | 6-Alpha Hydroxytetrahydro-11-Deoxycortisol; 6a OH-tetrahydro-11-Deoxycortisol | A measurement of the 6-alpha hydroxytetrahydro-11-deoxycortisol in a biological specimen. |
| C172524 | 7-alpha-Hydroxy-4-cholesten-3-one | 7-Alpha hydroxy-4-cholesten-3-one; 7-alpha-Hydroxy-4-cholesten-3-one | A measurement of the 7-alpha-hydroxy-4-cholesten-3-one in a biological specimen. |
| C181434 | 7-Ketocholesterol | 7-Ketocholesterol; 7-Oxocholesterol | A measurement of the 7-ketocholesterol in a biological specimen. |
| C181430 | 7alpha,25-Dihydroxycholesterol | 7alpha,25-Dihydroxycholesterol | A measurement of the 7alpha,25-dihydroxycholesterol in a biological specimen. |
| C181431 | 7alpha,27-Dihydroxycholesterol | 7alpha,27-Dihydroxycholesterol | A measurement of the 7alpha,27-dihydroxycholesterol in a biological specimen. |
| C181432 | 7alpha-Hydroxycholesterol | 7alpha-Hydroxycholesterol | A measurement of the 7alpha-hydroxycholesterol in a biological specimen. |
| C181433 | 7beta-Hydroxycholesterol | 7beta-Hydroxycholesterol | A measurement of the 7beta-hydroxycholesterol in a biological specimen. |
| C174309 | 8-Hydroxy-2'-Deoxyguanosine | 8-Hydroxy-2'-Deoxyguanosine; 8-oxo-dG | A measurement of the 8-hydroxy-2'-deoxyguanosine in a biological specimen. |
| C172492 | 8-Hydroxydeoxyguanosine | 8-Hydroxydeoxyguanosine; 8-OHdG | A measurement of the 8-hydroxydeoxyguanosine in a biological specimen. |
| C119291 | 8-Iso-PGF2alpha/Creatinine | 8-Iso-PGF2alpha/Creatinine | A relative measurement (ratio or percentage) of the prostaglandin F2 alpha isoform 8 to creatinine in a biological specimen. |
| C119292 | 8-Iso-Prostaglandin F2 Alpha | 8-Iso-Prostaglandin F2 Alpha | A measurement of the prostaglandin F2 alpha isoform 8 in a biological specimen. |
| C177970 | 9-Hydroxyrisperidone | 9-Hydroxyrisperidone; Paliperidone | A measurement of the 9-hydroxyrisperidone in a biological specimen. |
| C96565 | A Fetoprotein L3/A Fetoprotein | A Fetoprotein L3/A Fetoprotein | A relative measurement (ratio or percentage) of alpha fetoprotein L3 to total alpha fetoprotein in a biological specimen. |
| C111123 | A Proliferation-Inducing Ligand | A Proliferation-Inducing Ligand; CD256; TNFSF13; Tumor Necrosis Factor Ligand Superfamily Member 13 | A measurement of the a proliferation-inducing ligand in a biological specimen. |
| C184526 | AB-FUBINACA | AB-FUBINACA | A measurement of the synthetic cannabinoid AB-FUBINACA in a biological specimen. |
| C184527 | AB-PINACA | AB-PINACA | A measurement of the synthetic cannabinoid AB-PINACA in a biological specimen. |
| C111124 | Abnormal Cells | Abnormal Cells | A measurement of the abnormal cells in a biological specimen. |
| C150834 | Abnormal Cells/Leukocytes | Abnormal Cells/Leukocytes | A relative measurement (ratio or percentage) of abnormal cells to leukocytes in a biological specimen. |
| C150835 | Abnormal Cells/Total Cells | Abnormal Cells/Total Cells | A relative measurement (ratio or percentage) of abnormal cells to total cells in a biological specimen. |
| C135397 | ABO A1 Subtype | ABO A1 Subtype | The characterization of the ABO blood group A1 subtype in an individual. (NCI) |
| C125939 | ABO Blood Group | ABO Blood Group | The characterization of the blood type of an individual by testing for the presence of A antigen and B antigen on the surface of red blood cells. |
| C74699 | Acanthocytes | Acanthocytes | A measurement of the acanthocytes in a biological specimen. |
| C74633 | Acanthocytes/Erythrocytes | Acanthocytes/Erythrocytes | A relative measurement (ratio or percentage) of acanthocytes to all erythrocytes in a biological specimen. |
| C135398 | Acetaminophen | Acetaminophen; Paracetamol | A measurement of the acetaminophen in a biological specimen. |
| C172525 | Acetaminophen-Cysteine Adduct | Acetaminophen Protein Adduct; Acetaminophen-Cysteine Adduct; APAP-CYS; APAP-Protein | A measurement of the acetaminophen-cysteine adducts in a biological specimen. |
| C189521 | Acetoacetic Acid Excretion Rate | Acetoacetate Excretion Rate; Acetoacetic Acid Excretion Rate | A measurement of the amount of acetoacetic acid being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C92247 | Acetoacetic Acid | Acetoacetate; Acetoacetic Acid | A measurement of the acetoacetic acid in a biological specimen. |
| C147288 | Acetone | Acetone | A measurement of the acetone in a biological specimen. |
| C96559 | Acetylcholine Receptor Antibody | Acetylcholine Receptor Antibody | A measurement of the acetylcholine receptor antibody in a biological specimen. |
| C74838 | Acetylcholine | Acetylcholine | A measurement of the acetylcholine hormone in a biological specimen. |
| C96560 | Acetylcholinesterase | Acetylcholinesterase | A measurement of the acetylcholinesterase in a biological specimen. |
| C184528 | Acetylfentanyl | Acetyl Fentanyl; Acetylfentanyl | A measurement of the acetylfentanyl in a biological specimen. |
| C147297 | ACH Receptor Modulatn Ab/ACH Receptor Ab | ACH Receptor Modulation Antibody/ACH Receptor Antibody; ACH Receptor Modulatn Ab/ACH Receptor Ab | A relative measurement (ratio or percentage) of the acetylcholine receptor modulation antibody to the total acetylcholine receptor antibodies in a biological specimen. |
| C189502 | Acid Alpha-Glucosidase | Acid Alpha-Glucosidase; Acid Maltase; Alpha-1,4-glucosidase | A measurement of the acid alpha-glucosidase in a biological specimen. |
| C163419 | Acid Labile Subunit | Acid Labile Subunit; ALS; IGFALS; Insulin Like Growth Factor Binding Protein Acid Labile Subunit | A measurement of the acid labile subunit in a biological specimen. |
| C80163 | Acid Phosphatase | Acid Phosphatase | A measurement of the acid phosphatase in a biological specimen. |
| C189522 | Acid Sphingomyelinase | Acid Sphingomyelinase | A measurement of the acid sphingomyelinase in a biological specimen. |
| C103348 | Activated Coagulation Time | Activated Clotting Time; Activated Coagulation Time | A measurement of the inhibition of blood coagulation in response to anticoagulant therapies. |
| C38462 | Activated Partial Thromboplastin Time | Activated Partial Thromboplastin Time | A measurement of the length of time that it takes for clotting to occur when activating reagents are added to a biological specimen. The test is partial due to the absence of tissue factor (Factor III) from the reaction mixture. |
| C100471 | Activated Protein C Resistance | Activated Protein C Resistance; Factor V Leiden Screen | A measurement of the resistance in the anticoagulation response to activated protein C in a biological specimen. |
| C98862 | Activated PTT/Standard | Activated Partial Thromboplastin Time/Standard Thromboplastin Time; Activated PTT/Standard; Activated PTT/Standard PTT | A relative measurement (ratio or percentage) of the subject's activated partial thromboplastin time to a standard or control partial thromboplastin time. |
| C112219 | Active Ghrelin | Active Ghrelin | A measurement of active ghrelin in a biological specimen. |
| C92286 | Acyl Coenzyme A Oxidase | Acyl CoA Oxidase; Acyl Coenzyme A Oxidase; Fatty Acyl Coenzyme A Oxidase | A measurement of the acyl coenzyme A oxidase in a biological specimen. |
| C156535 | Acylcarnitine | Acylcarnitine | A measurement of the acylcarnitine in a biological specimen. |
| C147289 | Acylcarnitine/Carnitine, Free | Acylcarnitine/Carnitine, Free | A relative measurement (ratio or percentage) of the acylcarnitine to free carnitine in a biological specimen. |
| C156534 | Acylglycine | Acylglycine | A measurement of the acylglycine in a biological specimen. |
| C147290 | ADAM Metallopeptidase Domain 8 | A Disintegrin And Metalloproteinase Domain 8; ADAM Metallopeptidase Domain 8; CD156a Antigen | A measurement of the ADAM metallopeptidase domain 8 protein in a biological specimen. |
| C187830 | ADAMTS13 Activity | A Disintegrin-Like And Metalloprotease (Reprolysin Type) With Thrombospondin Type 1 Motif, 13 Activity; ADAM Metallopeptidase With Thrombospondin Type 1 Motif 13 Activity; ADAMTS13 Activity; von Willebrand Coagulation Factor Cleaving Protease ADAMTS13 Activity | A measurement of the biological activity of von Willebrand coagulation factor cleaving protease, ADAMTS13, in a biological specimen. |
| C187684 | ADAMTS13 | A Disintegrin-Like And Metalloprotease (Reprolysin Type) With Thrombospondin Type 1 Motif, 13; ADAM Metallopeptidase With Thrombospondin Type 1 Motif 13; von Willebrand Coagulation Factor Cleaving Protease ADAMTS13 | A measurement of the von Willebrand coagulation factor cleaving protease, ADAMTS13, in a biological specimen. |
| C184529 | ADB-PINACA | ADB-PINACA | A measurement of the synthetic cannabinoid ADB-PINACA in a biological specimen. |
| C102257 | Adenosine Diphosphate | Adenosine Diphosphate | A measurement of the adenosine diphosphate in a biological specimen. |
| C147307 | Adenosine Triphosphate | Adenosine Triphosphate | A measurement of the adenosine triphosphate in a biological specimen. |
| C74839 | Adiponectin | Adiponectin | A measurement of the total adiponectin hormone in a biological specimen. |
| C132363 | Adiponectin, High Molecular Weight | Adiponectin, High Molecular Weight | A measurement of the high molecular weight adiponectin hormone in a biological specimen. |
| C74780 | Adrenocorticotropic Hormone | Adrenocorticotropic Hormone; Corticotropin | A measurement of the adrenocorticotropic hormone in a biological specimen. |
| C112220 | Aggrecan Chondroitin Sulfate Epitope 846 | 846-Epitope; Aggrecan Chondroitin Sulfate Epitope 846; Chondroitin Sulfate Epitope 846; Chondroitin Sulfate Proteoglycan 1 Epitope 846; CS846 | A measurement of the 846 epitope present on the chondroitin sulfate chains of aggrecan in a biological specimen. |
| C116200 | Agranular Neutrophils | Agranular Neutrophils | A measurement of the agranular neutrophils in a biological specimen. |
| C100430 | Alanine Aminopeptidase | Alanine Aminopeptidase | A measurement of the alanine aminopeptidase in a biological specimen. |
| C64433 | Alanine Aminotransferase | Alanine Aminotransferase; SGPT | A measurement of the alanine aminotransferase in a biological specimen. |
| C122091 | Alanine | Alanine | A measurement of the alanine in a biological specimen. |
| C147293 | Albumin Clearance | Albumin Clearance | A measurement of the albumin clearance in a biological specimen. |
| C150814 | Albumin Excretion Rate | Albumin Excretion Rate | A measurement of the amount of albumin excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C154734 | Albumin Index | Albumin Index | A relative measurement (ratio) of the albumin in cerebrospinal fluid to albumin in serum or plasma in a biological specimen. |
| C64431 | Albumin | Albumin; Microalbumin | A measurement of the albumin protein in a biological specimen. |
| C74761 | Albumin/Creatinine | Albumin/Creatinine; Microalbumin/Creatinine Ratio | A relative measurement (ratio) of the albumin to the creatinine in a biological specimen. |
| C74894 | Albumin/Globulin | Albumin/Globulin | The ratio of albumin to globulin in a biological specimen. |
| C103453 | Albumin/Total Protein | Albumin/Total Protein | A relative measurement (ratio or percentage) of the albumin to total protein in a biological specimen. |
| C74731 | Aldolase | Aldolase | A measurement of the aldolase enzyme in a biological specimen. |
| C74841 | Aldosterone | Aldosterone | A measurement of the aldosterone hormone in a biological specimen. |
| C124338 | Aldosterone/Renin Activity | Aldosterone/Renin Activity | A relative measurement (ratio) of the aldosterone to renin activity in a biological specimen. |
| C154743 | Aldrin Epoxidase | Aldrin Epoxidase | A measurement of the aldrin epoxidase in a biological specimen. |
| C184566 | Alfentanil | Alfentanil | A measurement of the alfentanil in a biological specimen. |
| C147294 | Alk Phos, Bone/Total Alk Phos | Alk Phos, Bone/Total Alk Phos; Alkaline Phosphatase, Bone/Total Alkaline Phosphatase | A relative measurement (ratio or percentage) of the bone specific alkaline phosphatase isoform to total alkaline phosphatase in a biological specimen. |
| C147295 | Alk Phos, Intestinal/Total Alk Phos | Alk Phos, Intestinal/Total Alk Phos; Alkaline Phosphatase, Intestinal/Total Alkaline Phosphatase | A relative measurement (ratio or percentage) of the intestinal specific alkaline phosphatase isoform to total alkaline phosphatase in a biological specimen. |
| C189497 | Alk Phos, Liver + Bone/Total Alk Phos | Alk Phos, Liver + Bone/Total Alk Phos | A relative measurement (ratio or percentage) of the liver and bone specific alkaline phosphatase isoforms to total alkaline phosphatase in a biological specimen. |
| C147296 | Alk Phos, Liver/Total Alk Phos | Alk Phos, Liver/Total Alk Phos; Alkaline Phosphatase, Liver/Total Alkaline Phosphatase | A relative measurement (ratio or percentage) of the liver specific alkaline phosphatase isoform to total alkaline phosphatase in a biological specimen. |
| C184508 | Alk Phos, Placental/Total Alk Phos | Alk Phos, Placental/Total Alk Phos; Alkaline Phosphatase, Placental/Total Alkaline Phosphatase | A relative measurement (ratio or percentage) of the placental specific alkaline phosphatase isoform to total alkaline phosphatase in a biological specimen. |
| C165942 | Alkaline Phosphatase Excretion Rate | Alkaline Phosphatase Excretion Rate | A measurement of the amount of alkaline phosphatase being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C139091 | Alkaline Phosphatase Isoenzyme | Alkaline Phosphatase Isoenzyme | A measurement of the alkaline phosphatase isoenzyme in a biological specimen. |
| C64432 | Alkaline Phosphatase | Alkaline Phosphatase | A measurement of the alkaline phosphatase in a biological specimen. |
| C79438 | Alkaline Phosphatase/Creatinine | Alkaline Phosphatase/Creatinine | A relative measurement (ratio or percentage) of the alkaline phosphatase to creatinine in a biological specimen. |
| C154762 | Alloisoleucine | Alloisoleucine | A measurement of the alloisoleucine in a biological specimen. |
| C186032 | Alpha Cortol | Alpha Cortol; alpha-Cortol | A measurement of the alpha cortol in a biological specimen. |
| C186033 | Alpha Cortolone | Alpha Cortolone; alpha-Cortolone | A measurement of the alpha cortolone in a biological specimen. |
| C147291 | Alpha Fetoprotein Adj for Body Weight | Alpha Fetoprotein Adj for Body Weight | A measurement of alpha fetoprotein, which has been adjusted for body weight, in a biological specimen. |
| C96562 | Alpha Fetoprotein L1 | Alpha Fetoprotein L1 | A measurement of the alpha fetoprotein L1 in a biological specimen. |
| C96563 | Alpha Fetoprotein L2 | Alpha Fetoprotein L2 | A measurement of the alpha fetoprotein L2 in a biological specimen. |
| C96564 | Alpha Fetoprotein L3 | Alpha Fetoprotein L3 | A measurement of the alpha fetoprotein L3 in a biological specimen. |
| C74732 | Alpha Fetoprotein | Alpha Fetoprotein; Alpha-1-Fetoprotein | A measurement of the alpha fetoprotein in a biological specimen. |
| C163445 | Alpha Globulin | Alpha Globulin | A measurement of the total alpha globulins in a biological specimen. |
| C79433 | Alpha Glutathione-S-Transferase | Alpha Glutathione-S-Transferase | A measurement of the alpha form of glutathione S-transferase in a biological specimen. |
| C111126 | Alpha Hydroxybutyrate Dehydrogenase | Alpha Hydroxybutyrate Dehydrogenase | A measurement of the alpha-hydroxybutyrate dehydrogenase in a biological specimen. |
| C187789 | Alpha Melanocyte Stimulating Hormone | Alpha Melanocyte Stimulating Hormone; Alpha-MSH | A measurement of the alpha melanocyte stimulating hormone in a biological specimen. |
| C142272 | Alpha Synuclein Protein | Alpha Synuclein Protein | A measurement of the alpha synuclein protein in a biological specimen. |
| C103349 | Alpha Tocopherol | Alpha Tocopherol | A measurement of the alpha tocopherol in a biological specimen. |
| C103350 | Alpha Tocopherol/Vitamin E | Alpha Tocopherol/Vitamin E | A relative measurement (ratio or percentage) of alpha-tocopherol to the total vitamin E in a biological specimen. |
| C100429 | Alpha-1 Acid Glycoprotein | Alpha-1 Acid Glycoprotein | A measurement of the alpha-1 acid glycoprotein in a biological specimen. |
| C189527 | Alpha-1 Antitrypsin Z-Polymer | AAT Z-Polymer; Alpha-1 Antitrypsin Z-Polymer | A measurement of the polymers of Z-variant alpha-1 antitrypsin in a biological specimen. |
| C80167 | Alpha-1 Antitrypsin | Alpha-1 Antitrypsin; Serum Trypsin Inhibitor | A measurement of the alpha-1 antitrypsin in a biological specimen. |
| C181404 | Alpha-1 Antitrypsin, Functional | Alpha-1 Antitrypsin, Functional | A measurement of the functional alpha-1 antitrypsin in a biological specimen. |
| C92252 | Alpha-1 Globulin | A1-Globulin; Alpha-1 Globulin | A measurement of the proteins contributing to the alpha 1 fraction in a biological specimen. |
| C92253 | Alpha-1 Globulin/Total Protein | Alpha-1 Globulin/Total Protein | A relative measurement (ratio or percentage) of alpha-1-fraction proteins to total proteins in a biological specimen. |
| C186022 | Alpha-1 Microglobulin Excretion Rate | Alpha-1 Microglobulin Excretion Rate | A measurement of the amount of alpha-1 microglobulin being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C100461 | Alpha-1 Microglobulin | Alpha-1 Microglobulin; Protein HC | A measurement of the alpha-1 microglobulin in a biological specimen. |
| C100462 | Alpha-1 Microglobulin/Creatinine | Alpha-1 Microglobulin/Creatinine | A relative measurement (ratio or percentage) of the alpha-1 microglobulin to creatinine in a biological specimen. |
| C122094 | Alpha-2 Antiplasmin Activity | Alpha-2 Antiplasmin Activity | A measurement of the alpha-2 antiplasmin activity in a biological specimen. |
| C103351 | Alpha-2 Antiplasmin | Alpha-2 Antiplasmin; Alpha-2 Plasmin Inhibitor | A measurement of the alpha-2 antiplasmin in a biological specimen. |
| C92254 | Alpha-2 Globulin | A2-Globulin; Alpha-2 Globulin | A measurement of the proteins contributing to the alpha 2 fraction in a biological specimen. |
| C92255 | Alpha-2 Globulin/Total Protein | Alpha-2 Globulin/Total Protein | A relative measurement (ratio or percentage) of alpha-2-fraction proteins to total proteins in a biological specimen. |
| C80168 | Alpha-2 Macroglobulin | Alpha-2 Macroglobulin | A measurement of the alpha-2 macroglobulin in a biological specimen. |
| C154761 | Alpha-Aminoadipic Acid | Alpha-Aminoadipate; Alpha-Aminoadipic Acid | A measurement of the alpha-aminoadipic acid in a biological specimen. |
| C154759 | Alpha-Aminobutyric Acid | Alpha-aminobutyrate; Alpha-Aminobutyric Acid; Homoalanine | A measurement of the alpha-aminobutyric acid in a biological specimen. |
| C119278 | Alpha-GST Excretion Rate | Alpha-GST Excretion Rate | A measurement of the amount of Alpha Glutathione-S-Transferase being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C177954 | Alpha-Hydroxyalprazolam | Alpha-Hydroxyalprazolam | A measurement of the alpha-hydroxyalprazolam in a biological specimen. |
| C181418 | Alpha-Hydroxytriazolam | Alpha-Hydroxytriazolam | A measurement of the alpha-hydroxytriazolam a biological specimen. |
| C132364 | Alpha-Methylacyl Coenzyme A Racemase | Alpha-Methylacyl Coenzyme A Racemase | A measurement of the alpha-methylacyl coenzyme A racemase in a biological specimen. |
| C184537 | Alpha-Methylfentanyl | Alpha-Methylfentanyl | A measurement of the alpha-methylfentanyl in a biological specimen. |
| C75347 | Alpha-Methylphenethylamine | Alpha-Methylphenethylamine; Amphetamine | A measurement of the alpha-methylphenethylamine in a biological specimen. |
| C147299 | Alpha-N-acetylglucosaminidase | Alpha-N-acetylglucosaminidase | A measurement of the alpha-N-acetylglucosaminidase in a biological specimen. |
| C163422 | Alpha-Smooth Muscle Actin | Alpha-Actin 2; Alpha-SMA; Alpha-Smooth Muscle Actin | A measurement of the alpha-smooth muscle actin in a biological specimen. |
| C184567 | Alphaprodine | Alphaprodine | A measurement of the alphaprodine in a biological specimen. |
| C75370 | Alprazolam | Alprazolam | A measurement of the alprazolam present in a biological specimen. |
| C106498 | ALT/AST | ALT/AST | A relative measurement (ratio or percentage) of the alanine aminotransferase (ALT) to aspartate aminotransferase (AST) present in a sample. |
| C111127 | Aluminum | Al; Aluminum | A measurement of aluminum in a biological specimen. |
| C184539 | AM-2201 | AM-2201; AM2201 | A measurement of the synthetic cannabinoid AM-2201 in a biological specimen. |
| C184538 | AM694 N-5-hydroxypentyl | AM694 N-5-hydroxypentyl | A measurement of the synthetic cannabinoid metabolite AM694 N-5-hydroxypentyl in a biological specimen. |
| C132365 | AMACR mRNA | AMACR mRNA | A measurement of the alpha-methylacyl coenzyme A racemase mRNA in a biological specimen. |
| C130137 | American Cockroach Antigen IgA Antibody | American Cockroach Antigen IgA Antibody | A measurement of the Periplaneta americana antigen IgA antibody in a biological specimen. |
| C130136 | American Cockroach Antigen IgE Antibody | American Cockroach Antigen IgE Antibody | A measurement of the Periplaneta americana antigen IgE antibody in a biological specimen. |
| C130138 | American Cockroach Antigen IgG Antibody | American Cockroach Antigen IgG Antibody | A measurement of the Periplaneta americana antigen IgG antibody in a biological specimen. |
| C130139 | American Cockroach Antigen IgG4 Antibody | American Cockroach Antigen IgG4 Antibody | A measurement of the Periplaneta americana antigen IgG4 antibody in a biological specimen. |
| C165933 | American Cockroach IgE AB RAST Score | American Cockroach IgE AB RAST Score | A classification of the amount of Periplaneta americana antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165918 | American Cockroach IgG AB RAST Score | American Cockroach IgG AB RAST Score | A classification of the amount of Periplaneta americana antigen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C81183 | Amino Acids | AA; Amino Acids | A measurement of the total amino acids in a biological specimen. |
| C186023 | Amitriptyline | Amitriptyline | A measurement of the amitriptyline in a biological specimen. |
| C74799 | Ammonia | Ammonia; NH3 | A measurement of the ammonia in a biological specimen. |
| C105590 | Ammonium Biurate Crystals | Acid Ammonium Urate Crystals; Ammonium Biurate Crystals; Ammonium Urate Crystals | A measurement of the ammonium biurate crystals present in a biological specimen. |
| C74759 | Ammonium Oxalate Crystals | Ammonium Oxalate Crystals | A measurement of the ammonium oxalate crystals present in a urine specimen. |
| C186024 | Ammonium | Ammonium; Ammonium Ion; NH4+ | A measurement of the ammonium ion (NH4+) in a biological specimen. |
| C186025 | Ammonium/Creatinine | Ammonium/Creatinine | A relative measurement (ratio) of ammonium to creatinine in a biological specimen. |
| C75363 | Amobarbital | Amobarbital | A measurement of the amobarbital present in a biological specimen. |
| C74665 | Amorphous Crystals | Amorphous Crystals | A measurement of the amorphous (Note: phosphate or urate, depending on pH) crystals present in a biological specimen. |
| C92243 | Amorphous Phosphate Crystals | Amorphous Phosphate Crystals | A measurement of the amorphous phosphate crystals in a biological specimen. |
| C74666 | Amorphous Sediment | Amorphous Debris; Amorphous Sediment | A measurement of the amorphous sediment present in a biological specimen. |
| C92244 | Amorphous Urate Crystals | Amorphous Urate Crystals | A measurement of the amorphous urate crystals in a biological specimen. |
| C74687 | Amphetamine | Amphetamine | A measurement of any amphetamine class drug present in a biological specimen. |
| C64434 | Amylase | Amylase | A measurement of the total enzyme amylase in a biological specimen. |
| C98767 | Amylase, Pancreatic | Amylase, Pancreatic; Pancreatic Amylase Isoenzyme | A measurement of the pancreatic enzyme amylase in a biological specimen. |
| C98780 | Amylase, Salivary | Amylase, Salivary; Salivary Amylase Isoenzyme | A measurement of the salivary enzyme amylase in a biological specimen. |
| C125940 | Amyloid A | Amyloid A | A measurement of the total amyloid A in a biological specimen. |
| C119268 | Amyloid Alpha Precursor Protein | Amyloid Alpha Precursor Protein | A measurement of the amyloid alpha precursor protein present in a biological specimen. |
| C103352 | Amyloid Beta 1-38 | Amyloid Beta 1-38; Amyloid Beta 38; Amyloid Beta 38 Protein | A measurement of amyloid beta protein which is composed of peptides 1 to 38 in a biological specimen. |
| C103353 | Amyloid Beta 1-40 | Amyloid Beta 1-40; Amyloid Beta 40; Amyloid Beta 40 Protein | A measurement of amyloid beta protein which is composed of peptides 1 to 40 in a biological specimen. |
| C184518 | Amyloid Beta 1-41 | Amyloid Beta 1-41; Amyloid Beta 41; Amyloid Beta 41 Protein | A measurement of amyloid beta protein which is composed of peptides 1 to 41 in a biological specimen. |
| C84809 | Amyloid Beta 1-42 | Amyloid Beta 1-42; Amyloid Beta 42; Amyloid Beta 42 Protein | A measurement of amyloid beta protein which is composed of peptides 1 to 42 in a biological specimen. |
| C105438 | Amyloid Beta Precursor Protein | Amyloid Beta Precursor; Amyloid Beta Precursor Protein; Amyloid Precursor Beta; Amyloid Precursor Protein | A measurement of the amyloid beta precursor protein present in a biological specimen. |
| C81998 | Amyloid P | Amyloid P; Amyloid P Component; SAP; Serum Amyloid P Component | A measurement of the total amyloid P in a biological specimen. |
| C81999 | Amyloid, Beta | Amyloid, Beta; Beta Amyloid | A measurement of the total amyloid beta in a biological specimen. |
| C147298 | Anabasine | Anabasine | A measurement of the anabasine in a biological specimen. |
| C74842 | Androstenediol | Androstenediol | A measurement of the androstenediol metabolite in a biological specimen. |
| C74843 | Androstenedione | 4-Androstenedione; Androstenedione | A measurement of the androstenedione hormone in a biological specimen. |
| C186026 | Androsterone | Androsterone | A measurement of the androsterone in a biological specimen. |
| C111128 | Angiopoietin 1 | Angiopoietin 1 | A measurement of angiopoietin 1 in a biological specimen. |
| C163421 | Angiopoietin 2 | ANG2; Angiopoietin 2 | A measurement of angiopoietin 2 in a biological specimen. |
| C80169 | Angiotensin Converting Enzyme | Angiotensin Converting Enzyme | A measurement of the angiotensin converting enzyme in a biological specimen. |
| C74844 | Angiotensin I | Angiotensin I | A measurement of the angiotensin I hormone in a biological specimen. |
| C74845 | Angiotensin II | Angiotensin II | A measurement of the angiotensin II hormone in a biological specimen. |
| C74846 | Angiotensinogen | Angiotensin Precursor; Angiotensinogen | A measurement of the angiotensinogen hormone in a biological specimen. |
| C184568 | Anileridine | Anileridine | A measurement of the anileridine in a biological specimen. |
| C130112 | Animal Mix Antigen IgE Antibody | Animal Mix Antigen IgE Antibody | A measurement of the animal mix antigen IgE antibody in a biological specimen. |
| C130113 | Animal Mix Antigen IgG Antibody | Animal Mix Antigen IgG Antibody | A measurement of the animal mix antigen IgG antibody in a biological specimen. |
| C165927 | Animal Mix IgE AB RAST Score | Animal Mix IgE AB RAST Score | A classification of the amount of animal mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165908 | Animal Mix IgG AB RAST Score | Animal Mix IgG AB RAST Score | A classification of the amount of animal mix IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C147303 | Anion Gap 3 | Anion Gap 3 | A computed estimate of the unmeasured anions (computed as sodium minus the chloride and bicarbonate) in a biological specimen. |
| C147304 | Anion Gap 4 | Anion Gap 4 | A computed estimate of the unmeasured anions (computed as the difference between the sum of serum sodium + serum potassium and the sum of the serum bicarbonate+ chloride) in a biological specimen. |
| C74685 | Anion Gap | Anion Gap | A computed estimate of the unmeasured anions (those other than the chloride and bicarbonate anions) in a biological specimen. |
| C161354 | Anisochromia | Anisochromia | A measurement of the color variation of erythrocytes in a biological specimen. |
| C74797 | Anisocytes | Anisocytes; Anisocytosis | A measurement of the variability in the size of the red blood cells in a whole blood specimen. |
| C81973 | Anti-DNA Antibodies | Anti-DNA Antibodies; Anti-ds-DNA Antibodies | A measurement of the anti-DNA antibodies in a biological specimen. |
| C154769 | Anti-Double Stranded DNA IgG | Anti-Double Stranded DNA IgG | A measurement of the double stranded DNA IgG antibody in a biological specimen. |
| C74913 | Anti-Double Stranded DNA | Anti-Double Stranded DNA | A measurement of the anti-double stranded DNA antibody in a biological specimen. |
| C98706 | Anti-Factor Xa Activity | Anti-Factor Xa Activity | A measurement of the ability of antithrombin to inactivate activated Factor X in a biological specimen. This test is used to monitor low molecular weight or unfractionated heparin levels in a biological specimen. |
| C120625 | Anti-Mullerian Hormone | Anti-Mullerian Hormone | A measurement of the anti-Mullerian hormone in a biological specimen. |
| C176313 | Anti-Neutrophil Antibody | Anti-Neutrophil Antibody | A measurement of the total anti-neutrophil antibody in a biological specimen. |
| C120626 | Anti-Neutrophil Cytoplasmic Antibody | Anti-Neutrophil Cytoplasmic Antibody | A measurement of the anti-neutrophil cytoplasmic antibody in a biological specimen. |
| C163420 | Anti-Neutrophil Cytoplasmic IgG Antibody | Anti-Neutrophil Cytoplasmic IgG Antibody | A measurement of the anti-neutrophil cytoplasmic IgG antibody in a biological specimen. |
| C120627 | Anti-Nucleosome Antibody | Anti-Nucleosome Antibody | A measurement of the anti-nucleosome antibody in a biological specimen. |
| C124335 | Anti-Phospholipid IgG Antibody | Anti-Phospholipid IgG Antibody | A measurement of the antiphospholipid IgG antibody in a biological specimen. |
| C124336 | Anti-Phospholipid IgM Antibody | Anti-Phospholipid IgM Antibody | A measurement of the antiphospholipid IgM antibody in a biological specimen. |
| C92269 | Anti-Single Stranded DNA IgG | Anti-Single Stranded DNA IgG | A measurement of the anti-single stranded DNA IgG antibody in a biological specimen. |
| C74691 | Antidepressants | Antidepressants | A measurement of any antidepressant class drug present in a biological specimen. |
| C74847 | Antidiuretic Hormone | Antidiuretic Hormone; Vasopressin | A measurement of the antidiuretic hormone in a biological specimen. |
| C81974 | Antiglobulin Test, Direct | Antiglobulin Test Polyspecific, Direct; Antiglobulin Test, Direct; Direct Coombs Test | A measurement of the antibody or complement-coated erythrocytes in a biological specimen in vivo. |
| C91372 | Antiglobulin Test, Indirect | Antiglobulin Test, Indirect; Indirect Coombs Test | A test that uses Coombs' reagent to detect the presence of anti-erythrocyte antibodies in a biological specimen. |
| C81975 | Antimitochondrial Antibodies | Antimitochondrial Antibodies; Mitochondrial Antibody | A measurement of the antimitochondrial antibodies in a biological specimen. |
| C74916 | Antinuclear Antibodies | Antinuclear Antibodies | A measurement of the total antinuclear antibodies (antibodies that attack the body's own tissue) in a biological specimen. |
| C122093 | Antinuclear IgG Antibody | Antinuclear IgG Antibody | A measurement of the antinuclear IgG antibody in a biological specimen. |
| C102258 | Antiphospholipid Antibodies | Antiphospholipid Antibodies | A measurement of the total antiphospholipid antibodies in a biological specimen. |
| C147306 | Antithrombin Activity Actual/Control | Antithrombin Activity Actual/Antithrombin Activity Control; Antithrombin Activity Actual/Control; Antithrombin Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of antithrombin in a subject's specimen when compared to the same activity in a control specimen. |
| C81958 | Antithrombin Activity | Antithrombin Activity; Antithrombin III Activity | A measurement of the antithrombin activity in a biological specimen. |
| C170592 | Antithrombin Actual/Control | Antithrombin Actual/Control; Antithrombin Actual/Normal | A relative measurement (ratio or percentage) of the Antithrombin in a subject's specimen when compared to a control specimen. |
| C81977 | Antithrombin Antigen | Antithrombin; Antithrombin Antigen; Antithrombin III; Antithrombin III Antigen | A measurement of the antithrombin antigen in a biological specimen. |
| C124337 | Apolipoprotein A | Apolipoprotein A | A measurement of the total apolipoprotein A in a biological specimen. |
| C158222 | Apolipoprotein A/Apolipoprotein B | Apolipoprotein A/Apolipoprotein B | A relative measurement (ratio) of the total apolipoprotein A to apolipoprotein B in a biological specimen. |
| C74733 | Apolipoprotein A1 | Apolipoprotein A1 | A measurement of the apolipoprotein A1 in a biological specimen. |
| C147292 | Apolipoprotein A1/Apolipoprotein B | Apolipoprotein A1/Apolipoprotein B | A relative measurement (ratio or percentage) of the Apolipoprotein A1 to Apolipoprotein B in a biological specimen. |
| C103354 | Apolipoprotein A4 | Apolipoprotein A4 | A measurement of the apolipoprotein A4 in a biological specimen. |
| C103355 | Apolipoprotein A5 | Apolipoprotein A5 | A measurement of the apolipoprotein A5 in a biological specimen. |
| C82000 | Apolipoprotein AII | Apolipoprotein AII | A measurement of the apolipoprotein AII in a biological specimen. |
| C74734 | Apolipoprotein B | Apolipoprotein B | A measurement of the total apolipoprotein B in a biological specimen. |
| C103356 | Apolipoprotein B/Apolipoprotein A1 | Apolipoprotein B/Apolipoprotein A1 | A relative measurement (ratio or percentage) of the Apolipoprotein B to Apolipoprotein A1 in a biological specimen. |
| C120628 | Apolipoprotein B100 | Apolipoprotein B100 | A measurement of the apolipoprotein B100 in a biological specimen. |
| C120629 | Apolipoprotein B48 | Apolipoprotein B48 | A measurement of the apolipoprotein B48 in a biological specimen. |
| C100427 | Apolipoprotein C2 | Apolipoprotein C2; Apolipoprotein CII | A measurement of the apolipoprotein C2 in a biological specimen. |
| C120630 | Apolipoprotein CI | Apolipoprotein CI | A measurement of the apolipoprotein CI in a biological specimen. |
| C82001 | Apolipoprotein CIII | Apolipoprotein CIII | A measurement of the apolipoprotein CIII in a biological specimen. |
| C82002 | Apolipoprotein E | Apolipoprotein E | A measurement of the apolipoprotein E in a biological specimen. |
| C92293 | Apolipoprotein E4 | Apolipoprotein E4 | A measurement of the apolipoprotein E4 in a biological specimen. |
| C82003 | Apolipoprotein H | Apolipoprotein H | A measurement of the apolipoprotein H in a biological specimen. |
| C100428 | Apolipoprotein J | Apolipoprotein J; Clusterin | A measurement of the apolipoprotein J in a biological specimen. |
| C111130 | Apolipoprotein J/Creatinine | Apolipoprotein J/Creatinine; Clusterin/Creatinine | A relative measurement (ratio or percentage) of the apolipoprotein J to creatinine in a biological specimen. |
| C184578 | Aprobarbital | Aprobarbital | A measurement of the aprobarbital in a biological specimen. |
| C161369 | APTT-LA Actual/Control | APTT-LA Actual/Control; Lupus Anticoagulant Sensitive APTT Actual/Control | A relative measurement (ratio or percentage) of the Lupus anticoagulant sensitive APTT in a subject's specimen when compared to a control specimen. |
| C161372 | APTT-LA Screen to Confirm Pct Difference | APTT-LA Screen to Confirm Percent Difference; PTT-LA Screen to Confirm Pct Difference | A measurement to confirm the presence of Lupus anticoagulants, calculated as [(Screen aPTT - Confirm aPTT)/Screen aPTT]x100. |
| C184519 | Arachidonate 5-Lipoxygenase | 5-Lipoxygenase; 5-LO; 5-LOX; ALOX5; Arachidonate 5-Lipoxygenase | A measurement of the arachidonate 5-lipoxygenase in a biological specimen. |
| C102259 | Arachidonic Acid | Arachidonic Acid | A measurement of the arachidonic acid present in a biological specimen. |
| C147276 | Arachis hypogaea Antigen IgE Antibody | Arachis hypogaea Antigen IgE Antibody; Peanut Antigen IgE Antibody | A measurement of the Arachis hypogaea antigen IgE antibody in a biological specimen. |
| C165934 | Arachis hypogaea IgE AB RAST Score | Arachis hypogaea IgE AB RAST Score | A classification of the amount of Arachis hypogaea antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C122095 | Arginine | Arginine | A measurement of the arginine in a biological specimen. |
| C154763 | Argininosuccinic Acid | Argininosuccinate; Argininosuccinic Acid | A measurement of the argininosuccinic acid in a biological specimen. |
| C177974 | Aripiprazole | Aripiprazole | A measurement of the aripiprazole in a biological specimen. |
| C147305 | Arsenic | Arsenic; As | A measurement of the arsenic in a biological specimen. |
| C177985 | Asenapine | Asenapine | A measurement of the asenapine in a biological specimen. |
| C122096 | Asparagine | Asparagine | A measurement of the asparagine in a biological specimen. |
| C81978 | Aspartate Aminotransferase Antigen | Aspartate Aminotransferase Antigen; SGOT Antigen | A measurement of the aspartate aminotransferase antigen in a biological specimen. |
| C64467 | Aspartate Aminotransferase | Aspartate Aminotransferase; SGOT | A measurement of the aspartate aminotransferase in a biological specimen. |
| C117830 | Aspartate Aminotransferase/Creatinine | Aspartate Aminotransferase/Creatinine | A relative measurement (ratio or percentage) of the aspartate aminotransferase to creatinine in a biological specimen. |
| C122097 | Aspartic Acid | Aspartate; Aspartic Acid | A measurement of the aspartic acid in a biological specimen. |
| C156512 | AST to Platelet Ratio Index | APRI Score; AST to Platelet Ratio Index | A calculation that indicates the likely presence of liver cirrhosis and fibrosis, measured as the relative measurement of aspartate aminotransferase (AST) to AST upper limit of normal, divided by the platelet count, and multiplied by 100. |
| C176297 | AST/ALT | AST/ALT | A relative measurement (ratio or percentage) of the aspartate aminotransferase (AST) to alanine aminotransferase (ALT) present in a sample. |
| C158225 | AST/Creatine Kinase | Aspartate Aminotransferase/CPK; Aspartate Aminotransferase/Creatine Kinase; AST/Creatine Kinase | A relative measurement (ratio) of the aspartate aminotransferase to creatine kinase in a biological specimen. |
| C158233 | Asymmetric Dimethylarginine | Asymmetric Dimethylarginine; N,N-dimethylarginine | A measurement of asymmetric dimethylarginine in a biological specimen. |
| C154726 | Atherogenic Index of Plasma | AIP; Atherogenic Index; Atherogenic Index of Plasma | A measurement of the base 10 logarithm of the ratio of molar concentration of plasma triglyceride to high density lipoprotein cholesterol in a biological specimen. |
| C74886 | Atrial Natriuretic Peptide | Atrial Natriuretic Peptide; Atriopeptin | A measurement of the atrial natriuretic peptide in a biological specimen. |
| C74654 | Atypical Lymphocytes/Lymphocytes | Atypical Lymphocytes/Lymphocytes; Lymphocytes Atypical/Lymphocytes; Reactive Lymphocytes/Lymphocytes; Variant Lymphocytes/Lymphocytes | A relative measurement (ratio or percentage) of the atypical lymphocytes to all lymphocytes in a biological specimen. |
| C74657 | Auer Rods | Auer Rods | A measurement of the Auer rods (elongated needle structures that are found in the cytoplasm of leukemic blasts and are formed by clumps of azurophilic granular material) in a biological specimen. |
| C165943 | AXL Receptor Tyrosine Kinase | ARK; AXL Receptor Tyrosine Kinase; JTK11; Tyro7; UFO | A measurement of the AXL receptor tyrosine kinase in a biological specimen. |
| C116185 | Azurophilic Granules | Azurophilic Granulation; Azurophilic Granules | An observation of azurophilic granules in a biological specimen. |
| C111135 | B-Cell Activating Factor | B-Cell Activating Factor | A measurement of the B-cell activating factor in a biological specimen. |
| C128951 | B-lymphocyte Crossmatch | B-lymphocyte Crossmatch | A measurement to determine human leukocyte antigens (HLA) histocompatibility between the recipient and the donor by examining the presence or absence of the recipient's anti-HLA antibody reactivity towards HLA antigens expressed on the donor B-lymphocytes. |
| C174314 | B-Lymphocytes | B-Cell Lymphocytes; B-Cells; B-Lymphocytes | A measurement of the B-lymphocytes in a biological specimen. |
| C174316 | B-Lymphocytes/Leukocytes | B-Lymphocytes/Leukocytes | A relative measurement (ratio or percentage) of the B-lymphocytes to leukocytes in a biological specimen. |
| C174315 | B-Lymphocytes/Lymphocytes | B-Lymphocytes/Lymphocytes | A relative measurement (ratio or percentage) of the B-lymphocytes to total lymphocytes in a biological specimen. |
| C174317 | B-Lymphocytes/Total Cells | B-Lymphocytes/Total Cells | A relative measurement (ratio or percentage) of the B-lymphocytes to total cells in a biological specimen. |
| C64469 | Bacteria | Bacteria | A measurement of the bacteria in a biological specimen. |
| C74762 | Bacterial Casts | Bacterial Casts | A measurement of the bacterial casts present in a biological specimen. |
| C120631 | Bactericidal/Permeability-Inc Protein Ab | Bactericidal/Permeability-Inc Protein Ab; BPI Auto-antibody | A measurement of the bactericidal/permeability-increasing protein antibody in a biological specimen. |
| C184608 | Barbital | Barbital | A measurement of the barbital in a biological specimen. |
| C74688 | Barbiturates | Barbiturates | A measurement of any barbiturate class drug present in a biological specimen. |
| C147309 | Base Deficit | Base Deficit | A measurement of the amount of alkali required to return a biological specimen to a normal pH under standard conditions. |
| C119270 | Base Excess | Actual Base Excess; Base Excess | A calculated measurement of the amount of acid required to return blood to a normal pH under standard conditions. |
| C147311 | Basophilic Erythroblast | Basophilic Erythroblast | A measurement of the basophilic erythroblasts in a biological specimen taken from a non-human organism. |
| C135399 | Basophilic Metamyelocytes | Basophilic Metamyelocytes | A measurement of the basophilic metamyelocytes in a biological specimen. |
| C135400 | Basophilic Myelocytes | Basophilic Myelocytes | A measurement of the basophilic myelocytes in a biological specimen. |
| C181448 | Basophilic Myelocytes/Lymphocytes | Basophilic Myelocytes/Lymphocytes | A relative measurement (ratio or percentage) of the basophilic myelocytes to lymphocytes in a biological specimen (for example a bone marrow specimen). |
| C147405 | Basophilic Normoblast | Basophilic Normoblast | A measurement of the basophilic normoblasts in a biological specimen taken from a non-human organism. |
| C96567 | Basophilic Stippling | Basophilic Stippling | A measurement of the basophilic stippling in a biological specimen. |
| C130154 | Basophils Band Form | Basophils Band Form | A measurement of the banded basophils in a biological specimen. |
| C130155 | Basophils Band Form/Leukocytes | Basophils Band Form/Leukocytes | A relative measurement (ratio or percentage) of the banded basophils to leukocytes in a biological specimen. |
| C64470 | Basophils | Basophils | A measurement of the basophils in a biological specimen. |
| C135401 | Basophils, Segmented | Basophils, Segmented | A measurement of the segmented basophils in a biological specimen. |
| C64471 | Basophils/Leukocytes | Basophils/Leukocytes | A relative measurement (ratio or percentage) of the basophils to leukocytes in a biological specimen. |
| C98865 | Basophils/Total Cells | Basophils/Total Cells | A relative measurement (ratio or percentage) of the basophils to total cells in a biological specimen (for example a bone marrow specimen). |
| C130116 | Bee Mix Antigen IgE Antibody | Bee Mix Antigen IgE Antibody | A measurement of the bee mix antigen IgE antibody in a biological specimen. |
| C130117 | Bee Mix Antigen IgG Antibody | Bee Mix Antigen IgG Antibody | A measurement of the bee mix antigen IgG antibody in a biological specimen. |
| C130118 | Bee Mix Antigen IgG4 Antibody | Bee Mix Antigen IgG4 Antibody | A measurement of the bee mix antigen IgG4 antibody in a biological specimen. |
| C165929 | Bee Mix IgE AB RAST Score | Bee Mix IgE AB RAST Score | A classification of the amount of bee mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165910 | Bee Mix IgG AB RAST Score | Bee Mix IgG AB RAST Score | A classification of the amount of bee mix IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C111136 | Bence-Jones Protein | Bence-Jones Protein | A measurement of the total Bence-Jones protein in a biological specimen. |
| C74692 | Benzodiazepine | Benzodiazepine | A measurement of any benzodiazepine class drug present in a biological specimen. |
| C75350 | Benzoylecgonine | Benzoylecgonine | A measurement of the benzoylecgonine in a biological specimen. |
| C184554 | Benzylpiperazine | 1-benzylpiperazine; Benzylpiperazine; N-benzylpiperazine | A measurement of the benzylpiperazine in a biological specimen. |
| C130069 | Bermuda Grass Pollen IgA | Bermuda Grass Pollen IgA | A measurement of the Cynodon dactylon pollen antigen IgA antibody in a biological specimen. |
| C165875 | Bermuda Grass Pollen IgE AB RAST Score | Bermuda Grass Pollen IgE AB RAST Score | A classification of the amount of Cynodon dactylon pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130068 | Bermuda Grass Pollen IgE | Bermuda Grass Pollen IgE | A measurement of the Cynodon dactylon pollen antigen IgE antibody in a biological specimen. |
| C165897 | Bermuda Grass Pollen IgG AB RAST Score | Bermuda Grass Pollen IgG AB RAST Score | A classification of the amount of Cynodon dactylon pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130070 | Bermuda Grass Pollen IgG | Bermuda Grass Pollen IgG | A measurement of the Cynodon dactylon pollen antigen IgG antibody in a biological specimen. |
| C130071 | Bermuda Grass Pollen IgG4 | Bermuda Grass Pollen IgG4 | A measurement of the Cynodon dactylon pollen antigen IgG4 antibody in a biological specimen. |
| C154764 | Beta Alanine | Beta Alanine | A measurement of the beta alanine in a biological specimen. |
| C100472 | Beta Carotene | b-Carotene; Beta Carotene; Beta Carotin | A measurement of the beta carotene in a biological specimen. |
| C103357 | Beta Catenin | Beta Catenin | A measurement of the beta catenin in a biological specimen. |
| C92256 | Beta Globulin | Beta Globulin | A measurement of the proteins contributing to the beta fraction in a biological specimen. |
| C92294 | Beta Globulin/Total Protein | Beta Globulin/Total Protein | A relative measurement (ratio or percentage) of beta fraction proteins to total proteins in a biological specimen. |
| C172497 | Beta+Gamma Tocopherol | Beta and Gamma Tocopherol; Beta+Gamma Tocopherol | A measurement of the beta and gamma tocopherol in a biological specimen. |
| C119274 | Beta-1 Globulin | Beta-1 Globulin | A measurement of the beta-1 globulin in a biological specimen. |
| C142277 | Beta-1 Globulin/Beta Protein | Beta-1 Globulin/Beta Protein | A relative measurement (ratio or percentage) of the beta-1-fraction proteins to the total beta protein fraction in a biological specimen. |
| C119275 | Beta-1 Globulin/Total Protein | Beta-1 Globulin/Total Protein | A relative measurement (ratio or percentage) of beta-1-fraction proteins to total proteins in a biological specimen. |
| C127607 | Beta-1B Glycoprotein | Beta-1B Glycoprotein; Hemopexin; HPX | A measurement of the beta-1B glycoprotein in a biological specimen. |
| C119276 | Beta-2 Globulin | Beta-2 Globulin | A measurement of the beta-2 globulin in a biological specimen. |
| C119277 | Beta-2 Globulin/Total Protein | Beta-2 Globulin/Total Protein | A relative measurement (ratio or percentage) of beta-2-fraction proteins to total proteins in a biological specimen. |
| C147308 | Beta-2 Glycoprotein 1 IgA Antibody | Beta-2 Glycoprotein 1 IgA Antibody | A measurement of the beta-2 glycoprotein 1 IgG antibodies in a biological specimen. |
| C103358 | Beta-2 Glycoprotein 1 IgG Antibody | Beta-2 Glycoprotein 1 IgG Antibody | A measurement of the Beta-2 glycoprotein 1 IgG antibodies in a biological specimen. |
| C103359 | Beta-2 Glycoprotein 1 IgM Antibody | Beta-2 Glycoprotein 1 IgM Antibody | A measurement of the Beta-2 glycoprotein 1 IgM antibodies in a biological specimen. |
| C81979 | Beta-2 Glycoprotein Antibody | Beta-2 Glycoprotein Antibody | A measurement of the beta-2 glycoprotein antibody in a biological specimen. |
| C81980 | Beta-2 Microglobulin | Beta-2 Microglobulin | A measurement of the beta-2 microglobulin in a biological specimen. |
| C127608 | Beta-2 Microglobulin/Creatinine | Beta-2 Microglobulin/Creatinine | A relative measurement (ratio) of the beta-2 microglobulin to creatinine in a biological specimen. |
| C184510 | Beta-Actin | Actin Beta; B-Actin; Beta-Actin | A measurement of the beta-actin in a biological specimen. |
| C154765 | Beta-Aminobutyric Acid | BABA; Beta-aminobutyrate; Beta-Aminobutyric Acid | A measurement of the beta-aminobutyric acid in a biological specimen. |
| C123455 | Beta-cell Function | Beta-cell Function | A measurement of the beta cell function (insulin production and secretion) in a biological specimen. |
| C122102 | Beta-defensin 2 | Beta-defensin 2 | A measurement of the beta-defensin 2 in a biological specimen. |
| C189520 | Beta-Hydroxybutyrate Excretion Rate | 3-Hydroxybutyrate Excretion Rate; B-Hydroxybutyrate Excretion Rate; Beta-Hydroxybutyrate Excretion Rate; BHB Excretion Rate | A measurement of the amount of beta-Hydroxybutyrate being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C96568 | Beta-Hydroxybutyrate | 3-Hydroxybutyrate; B-Hydroxybutyrate; Beta-Hydroxybutyrate; Beta-Hydroxybutyric Acid; BHB | A measurement of the total Beta-hydroxybutyrate in a biological specimen. |
| C186028 | Beta-Hydroxybutyrate/Acetoacetate | Beta-Hydroxybutyrate/Acetoacetate | A relative measurement (ratio) of the beta-hydroxybutyrate to acetoacetate in a biological specimen. |
| C184530 | Beta-Hydroxythiofentanyl | Beta-Hydroxythiofentanyl | A measurement of the beta-hydroxythiofentanyl in a biological specimen. |
| C172517 | Betaines | Betaines | A measurement of the betaine class compounds in a biological specimen. |
| C74667 | Bicarbonate | Bicarbonate; HCO3 | A measurement of the bicarbonate in a biological specimen. |
| C74800 | Bile Acid | Bile Acid; Bile Acids; Bile Salt; Bile Salts | A measurement of the total bile acids in a biological specimen. |
| C74668 | Bilirubin Crystals | Bilirubin Crystals | A measurement of the bilirubin crystals present in a biological specimen. |
| C38037 | Bilirubin | Bilirubin; Total Bilirubin | A measurement of the total bilirubin in a biological specimen. |
| C117860 | Bioavailable Testosterone | Bioavailable Testosterone | A measurement of bioavailable testosterone in a biological specimen. |
| C130073 | Birch Pollen IgA | Birch Pollen IgA | A measurement of the Betula pollen antigen IgA antibody in a biological specimen. |
| C165876 | Birch Pollen IgE AB RAST Score | Birch Pollen IgE AB RAST Score | A classification of the amount of Betula pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130072 | Birch Pollen IgE | Birch Pollen IgE | A measurement of the Betula pollen antigen IgE antibody in a biological specimen. |
| C165898 | Birch Pollen IgG AB RAST Score | Birch Pollen IgG AB RAST Score | A classification of the amount of Betula pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130074 | Birch Pollen IgG | Birch Pollen IgG | A measurement of the Betula pollen antigen IgG antibody in a biological specimen. |
| C130075 | Birch Pollen IgG4 | Birch Pollen IgG4 | A measurement of the Betula pollen antigen IgG4 antibody in a biological specimen. |
| C74700 | Bite Cells | Bite Cells | A measurement of the bite cells (erythrocytes with the appearance of a bite having been removed, due to oxidative hemolysis) in a biological specimen. |
| C74634 | Bite Cells/Erythrocytes | Bite Cells/Erythrocytes | A relative measurement (ratio or percentage) of bite cells (erythrocytes with the appearance of a bite having been removed, due to oxidative hemolysis) to all erythrocytes in a biological specimen. |
| C154733 | Bizarre Platelets | Bizarre Platelets | A measurement of the bizarre platelets (large with abnormal morphology and shape) in a biological specimen. |
| C74605 | Blasts | Blasts | A measurement of the blast cells in a biological specimen. |
| C64487 | Blasts/Leukocytes | Blasts/Leukocytes | A relative measurement (ratio or percentage) of the blasts to leukocytes in a biological specimen. |
| C147312 | Blasts/Nucleated Cells | Blasts/Nucleated Cells | A relative measurement (ratio or percentage) of the blasts to the total nucleated cells in a biological specimen. |
| C150836 | Blasts/Total Cells | Blasts/Total Cells | A relative measurement (ratio or percentage) of the blasts to total cells in a biological specimen. |
| C89775 | Bleeding Time | Bleeding Time; Clotting Time Homeostasis | A measurement of the time from the start to cessation of an induced bleed. |
| C127609 | Blister Cell | Blister Cell | A measurement of the blister cells in a biological specimen. |
| C184579 | Bolasterone | Bolasterone | A measurement of the bolasterone in a biological specimen. |
| C75380 | Boldenone | Boldenone | A measurement of the boldenone in a biological specimen. |
| C92287 | Bone Specific Alkaline Phosphatase | Bone Specific Alkaline Phosphatase | A measurement of the bone specific alkaline phosphatase isoform in a biological specimen. |
| C165940 | Boxelder Pollen IgE AB RAST Score | Boxelder Pollen IgE AB RAST Score | A classification of the amount of Acer negundo pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C147284 | Boxelder Pollen IgE Antibody | Boxelder Pollen IgE Antibody | A measurement of the Acer negundo pollen antigen IgE antibody in a biological specimen. |
| C74735 | Brain Natriuretic Peptide | B-Type Natriuretic Peptide; Brain Natriuretic Peptide | A measurement of the brain (B-type) natriuretic peptide in a biological specimen. |
| C82004 | Brain-Derived Neurotrophic Factor | Brain-Derived Neurotrophic Factor | A measurement of the brain-derived neurotrophic factor in a biological specimen. |
| C177973 | Brexpiprazole | Brexpiprazole | A measurement of the brexpiprazole in a biological specimen. |
| C184639 | Brivaracetam | Brivaracetam | A measurement of the brivaracetam in a biological specimen. |
| C96588 | Broad Casts | Broad Casts | A measurement of the broad casts in a biological specimen. |
| C184609 | Bromazepam | Bromazepam | A measurement of the bromazepam in a biological specimen. |
| C165772 | Bruton's Tyrosine Kinase | Agammaglobulinemia Tyrosine Kinase; ATK; B-cell Progenitor Kinase; Bruton Tyrosine Kinase; Bruton's Tyrosine Kinase; Tyrosine-protein kinase BTK | A measurement of the Bruton's tyrosine kinase in a biological specimen. |
| C165944 | Bruton's Tyrosine Kinase, Free | Bruton's Tyrosine Kinase, Free | A measurement of the free Bruton's tyrosine kinase in a biological specimen. |
| C184531 | Bufotenine | Bufotenine | A measurement of the bufotenine in a biological specimen. |
| C75352 | Buprenorphine | Buprenorphine | A measurement of the buprenorphine drug present in a biological specimen. |
| C74701 | Burr Cells | Burr Cells; Echinocytes | A measurement of the Burr cells (erythrocytes characterized by the presence of small, blunt projections evenly distributed across the cell surface) in a biological specimen. |
| C75364 | Butabarbital | Butabarbital | A measurement of the butabarbital in a biological specimen. |
| C75365 | Butalbital | Butalbital | A measurement of the butalbital present in a biological specimen. |
| C184610 | Butorphanol | Butorphanol | A measurement of the butorphanol in a biological specimen. |
| C184532 | Butylone | Butylone | A measurement of the butylone in a biological specimen. |
| C111142 | Butyrylcholinesterase | Acylcholine Acylhydrolase; Butyrylcholinesterase; Non-neuronal Cholinesterase; Plasma Cholinesterase; Pseudocholinesterase | A measurement of the total butyrylcholinesterase in a biological specimen. |
| C184533 | Butyrylfentanyl | Butyrfentanyl; Butyryl Fentanyl; Butyrylfentanyl | A measurement of the butyrylfentanyl in a biological specimen. |
| C64548 | C Reactive Protein | C Reactive Protein | A measurement of the C reactive protein in a biological specimen. |
| C122103 | C-C Chemokine Receptor Type 5 | C-C Chemokine Receptor Type 5; CD195 | A measurement of the CCR5, chemokine (C-C motif) receptor type 5, in a biological specimen. |
| C187796 | C-Peptide Excretion Rate | C-Peptide Excretion Rate | A measurement of the amount of C-peptide being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C74736 | C-peptide | C-peptide | A measurement of the C (connecting) peptide of insulin in a biological specimen. |
| C150837 | C-peptide/Creatinine | C-peptide/Creatinine | A relative measurement (ratio or percentage) of the C-peptide to creatinine in a biological specimen. |
| C74702 | Cabot Rings | Cabot Rings | A measurement of the Cabot rings (red-purple staining, threadlike, ring or figure 8 shaped filaments in an erythrocyte) in a biological specimen. |
| C75346 | Caffeine | Caffeine | A measurement of the caffeine in a biological specimen. |
| C125942 | Calbindin | Calbindin | A measurement of the total calbindin in a biological specimen. |
| C74848 | Calcitonin | Calcitonin | A measurement of the calcitonin hormone in a biological specimen. |
| C74849 | Calcitriol | Calcitriol | A measurement of the calcitriol hormone in a biological specimen. |
| C103360 | Calcium - Phosphorus Product | Calcium - Phosphorus Product | A measurement of the product of the calcium and phosphate measurements in a biological specimen. |
| C74669 | Calcium Carbonate Crystals | Calcium Carbonate Crystals | A measurement of the calcium carbonate crystals present in a biological specimen. |
| C96589 | Calcium Clearance | Calcium Clearance | A measurement of the volume of serum or plasma that would be cleared of calcium by excretion of urine for a specified unit of time (e.g. one minute). |
| C154753 | Calcium Corrected for Albumin | Calcium Corrected for Albumin | A measurement of calcium, which has been corrected for albumin, in a biological specimen. |
| C147314 | Calcium Corrected for Total Protein | Calcium Corrected for Total Protein | A measurement of calcium, which has been corrected for total protein, in a biological specimen. |
| C119272 | Calcium Corrected | Calcium Corrected | A measurement of calcium, which has been corrected using an unspecified protein, in a biological specimen. |
| C150815 | Calcium Excretion Rate | Calcium Excretion Rate | A measurement of the amount of calcium being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C74670 | Calcium Oxalate Crystals | Calcium Oxalate Crystals | A measurement of the calcium oxalate crystals present in a biological specimen. |
| C187793 | Calcium Oxalate Excretion Rate | Calcium Oxalate Excretion Rate | A measurement of the amount of calcium oxalate being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C74671 | Calcium Phosphate Crystals | Calcium Phosphate Crystals | A measurement of the calcium phosphate crystals present in a biological specimen. |
| C124340 | Calcium Sulfate Crystals | Calcium Sulfate Crystals | A measurement of the calcium sulfate crystals present in a biological specimen. |
| C96590 | Calcium Sulphate | Calcium Sulphate | A measurement of the calcium sulphate in a biological specimen. |
| C64488 | Calcium | Calcium | A measurement of the calcium in a biological specimen. |
| C125941 | Calcium, Ionized pH Adjusted | Calcium, Ionized pH Adjusted | A measurement of the pH adjusted ionized calcium in a biological specimen. |
| C81948 | Calcium, Ionized | Calcium, Ionized | A measurement of the ionized calcium in a biological specimen. |
| C79439 | Calcium/Creatinine | Calcium/Creatinine | A relative measurement (ratio or percentage) of the calcium to creatinine in a biological specimen. |
| C139087 | Calcium/Phosphorus | Calcium/Phosphate; Calcium/Phosphorus | A relative measurement (ratio) of the calcium to phosphorus in a biological specimen. |
| C132381 | Calculated Panel Reactive Antibody | Calculated Panel Reactive Antibody | A measurement of the calculated panel reactive antibody, which is based on the number/type of unacceptable HLA antigens to which an organ recipient has been sensitized, and which algorithmically estimates the level of sensitization in the recipient. The CPRA is computed from HLA antigen frequencies in a given donor population using both anti-HLA class I and class II antibody specificities; it also represents the percentage of actual organ donors that express one or more unacceptable HLA antigens to which a recipient may react adversely. |
| C82005 | Calprotectin | Calprotectin | A measurement of the calprotectin in a biological specimen. |
| C103361 | Cancer Antigen 1 | Cancer Antigen 1 | A measurement of the cancer antigen 1 in a biological specimen. |
| C79089 | Cancer Antigen 125 | CA125; CA125AG; Cancer Antigen 125; Carbohydrate Antigen 125; MUC16; Mucin-16; Mucin-16, Cell Surface Associated | A measurement of the cancer antigen 125 in a biological specimen. |
| C103362 | Cancer Antigen 15-3 | Cancer Antigen 15-3; Carbohydrate Antigen 15-3 | A measurement of the cancer antigen 15-3 in a biological specimen. |
| C81982 | Cancer Antigen 19-9 | Cancer Antigen 19-9; Carbohydrate Antigen 19-9 | A measurement of the cancer antigen 19-9 in a biological specimen. |
| C172526 | Cancer Antigen 242 | Cancer Antigen 242; Carbohydrate Antigen 242 | A measurement of the cancer antigen 242 in a biological specimen. |
| C111143 | Cancer Antigen 27-29 | Cancer Antigen 27-29 | A measurement of the cancer antigen 27-29 in a biological specimen. |
| C187794 | Cancer Antigen 50 | CA50; Cancer Antigen 50; Carbohydrate Antigen 50 | A measurement of the cancer antigen 50 in a biological specimen. |
| C106505 | Cancer Antigen 72-4 | CA 72-4; Cancer Antigen 72-4; Carbohydrate Antigen 72-4 | A measurement of the cancer antigen 72-4 in a biological specimen. |
| C165946 | Cannabinoid Metabolites | Cannabinoid Metabolites; Cannabis Metabolites; Marijuana Metabolites | A measurement of any cannabinoid drug class metabolite(s) present in a biological specimen. |
| C74689 | Cannabinoids | Cannabinoids | A measurement of any cannabinoid class drug present in a biological specimen. |
| C135402 | Cannabinoids, Synthetic | Cannabinoids, Synthetic | A measurement of any synthetic cannabinoid class drug present in a biological specimen. |
| C125943 | Carb-Deficient Transferrin/Transferrin | Carb-Deficient Transferrin/Transferrin | A relative measurement (ratio or percentage) of the carbohydrate-deficient transferrin to total transferrin in a biological specimen. |
| C147322 | Carbamazepine | Carbamazepine | A measurement of the carbamazepine in a biological specimen. |
| C101016 | Carbohydrate-Deficient Transferrin | Carbohydrate-Deficient Transferrin | A measurement of transferrin with a reduced number of carbohydrate moieties in a biological specimen. |
| C64545 | Carbon Dioxide | Carbon Dioxide | A measurement of the carbon dioxide gas in a biological specimen. |
| C139084 | Carbon Monoxide | Carbon Monoxide | A measurement of the carbon monoxide in a biological specimen. |
| C172510 | Carbonic Anhydrase 9 | CA9; CAIX; Carbonic Anhydrase 9 | A measurement of the carbonic anhydrase 9 in a biological specimen. |
| C96591 | Carboxyhemoglobin | Carboxyhemoglobin | A measurement of the carboxyhemoglobin, carbon monoxide-bound hemoglobin, in a biological specimen. |
| C147355 | Carboxyhemoglobin/Total Hemoglobin | Carboxyhemoglobin/Total Hemoglobin | A relative measurement (ratio or percentage) of the amount of carboxyhemoglobin compared to total hemoglobin in a biological specimen. |
| C165953 | Carboxypeptidase B2 | Carboxypeptidase B2; CPU; PCPB; TAFI | A measurement of the carboxypeptidase B2 in a biological specimen. |
| C81983 | Carcinoembryonic Antigen | Carcinoembryonic Antigen | A measurement of the carcinoembryonic antigen in a biological specimen. |
| C122112 | Cardiolipin IgA Antibody | Cardiolipin IgA Antibody | A measurement of the cardiolipin IgA antibody in a biological specimen. |
| C111144 | Cardiolipin IgG Antibody | Anti-Cardiolipin IgG Antibody; Cardiolipin IgG Antibody | A measurement of the cardiolipin IgG antibody in a biological specimen. |
| C103363 | Cardiolipin IgM Antibody | Cardiolipin IgM Antibody | A measurement of the cardiolipin IgM antibodies in a biological specimen. |
| C177975 | Cariprazine | Cariprazine | A measurement of the cariprazine in a biological specimen. |
| C184611 | Carisoprodol | Carisoprodol | A measurement of the carisoprodol in a biological specimen. |
| C92288 | Carnitine Acetyl Transferase | Carnitine Acetyl Transferase | A measurement of the carnitine acetyl transferase in a biological specimen. |
| C147323 | Carnitine Esters | Carnitine Esters | A measurement of the total carnitine esters in a biological specimen. |
| C163424 | Carnitine Excretion Rate | Carnitine Excretion Rate | A measurement of the amount of carnitine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C74682 | Carnitine | Carnitine | A measurement of the total carnitine in a biological specimen. |
| C74677 | Carnitine, Free | Carnitine, Free | A measurement of the free carnitine in a biological specimen. |
| C186034 | Carotene | Carotene | A measurement of the total carotenes in a biological specimen. |
| C111145 | Cartilage Oligomeric Matrix Protein | Cartilage Oligomeric Matrix Protein | A measurement of the cartilage oligomeric matrix protein in a biological specimen. |
| C177958 | Cashew Antigen IgE Antibody | Anacardium occidentale Nut Antigen IgE Antibody; Cashew Antigen IgE Antibody | A measurement of the cashew antigen IgE antibody in a biological specimen. |
| C74763 | Casts | Casts | A statement that indicates casts were looked for in a biological specimen. |
| C130126 | Cat Dander Antigen IgA Antibody | Cat Dander Antigen IgA Antibody | A measurement of the Felis catus dander antigen IgA antibody in a biological specimen. |
| C130124 | Cat Dander Antigen IgE Antibody | Cat Dander Antigen IgE Antibody | A measurement of the Felis catus dander antigen IgE antibody in a biological specimen. |
| C130125 | Cat Dander Antigen IgG Antibody | Cat Dander Antigen IgG Antibody | A measurement of the Felis catus dander antigen IgG antibody in a biological specimen. |
| C130127 | Cat Dander Antigen IgG4 Antibody | Cat Dander Antigen IgG4 Antibody | A measurement of the Felis catus dander antigen IgG4 antibody in a biological specimen. |
| C165877 | Cat Dander IgE AB RAST Score | Cat Dander IgE AB RAST Score | A classification of the amount of Felis catus dander antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165914 | Cat Dander IgG AB RAST Score | Cat Dander IgG AB RAST Score | A classification of the amount of Felis cattus dander IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C186037 | Catecholamines | Catecholamines | A measurement of the total catecholamines in a biological specimen. |
| C120634 | Cathepsin Antibody | Cathepsin Antibody | A measurement of the total cathepsin antibody in a biological specimen. |
| C184534 | Cathinone | Cathinone | A measurement of the cathinone in a biological specimen. |
| C172511 | CEA Cell Adhesion Molecule 1 | BGP; Biliary Glycoprotein; Carcinoembryonic Antigen Cell Adhesion Molecule 1; CD66a; CEA Cell Adhesion Molecule 1; CEA Related Cell Adhesion Molecule 1 | A measurement of the carcinoembryonic antigen (CEA) cell adhesion molecule 1 in a biological specimen. |
| C17768 | Cell Morphology | Cell Morphology | An examination or assessment of the form and structure of cells. |
| C48938 | Cells | Cells | A measurement of the total cells in a biological specimen. |
| C74764 | Cellular Casts | Cellular Casts | A measurement of the cellular (white blood cell, red blood cell, epithelial and bacterial) casts present in a biological specimen. |
| C111153 | Cellularity | Cellularity; Cellularity Grade | A measurement of the degree, quality or condition of cells in a biological specimen. |
| C111154 | Centromere B Antibodies | Centromere B Antibodies | A measurement of centromere B antibodies in a biological specimen. |
| C122111 | Centromere IgG Antibody | Centromere IgG Antibody; Centromere Protein B | A measurement of the centromere IgG antibody in a biological specimen. |
| C100432 | Ceruloplasmin | Caeruloplasmin; Ceruloplasmin | A measurement of ceruloplasmin in a biological specimen. |
| C130156 | Chemokine (C-C Motif) Ligand 12 | Chemokine (C-C Motif) Ligand 12; Monocyte Chemotactic Protein 5 | A measurement of the CCL12, chemokine (C-C motif) ligand 12, in a biological specimen. |
| C165947 | Chemokine (C-C Motif) Ligand 13 | C-C Motif Chemokine Ligand 13; Chemokine (C-C Motif) Ligand 13; CKb10; MCP-4; NCC1; SCYA13; SCYL1 | A measurement of the CCL13, chemokine (C-C motif) ligand 13, in a biological specimen. |
| C165948 | Chemokine (C-C Motif) Ligand 16 | Chemokine (C-C Motif) Ligand 16; CKb12; HCC-4; ILINCK; LCC-1; LEC; LMC; Mtn-1; NCC4; SCYA16; SCYL4 | A measurement of the CCL16, chemokine (C-C motif) ligand 16, in a biological specimen. |
| C112236 | Chemokine (C-C Motif) Ligand 17 | ABCD-2; Chemokine (C-C Motif) Ligand 17; SCYA17; TARC; Thymus and Activation Regulated Chemokine | A measurement of the CCL17, chemokine (C-C motif) ligand 17, in a biological specimen. |
| C112237 | Chemokine (C-C Motif) Ligand 18 | AMAC-1; AMAC1; Chemokine (C-C Motif) Ligand 18; CKB7; DC-CK1; DCCK1; Macrophage inflammatory protein-4; MIP4; PARC; Pulmonary and Activation-Regulated Chemokine; SCYA18 | A measurement of the CCL18, chemokine (C-C motif) ligand 18, in a biological specimen. |
| C130157 | Chemokine (C-C Motif) Ligand 19 | Chemokine (C-C Motif) Ligand 19; Macrophage Inflammatory Protein 3 Beta; MIP3B | A measurement of the CCL19, chemokine (C-C motif) ligand 19, in a biological specimen. |
| C156520 | Chemokine (C-C Motif) Ligand 2 Excr Rate | Chemokine (C-C Motif) Ligand 2 Excr Rate; Chemokine (C-C Motif) Ligand 2 Excretion Rate; MCP1 Excretion Rate | A measurement of the amount of chemokine (C-C Motif) ligand 2 being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C161362 | Chemokine (C-C Motif) Ligand 20 | CCL20; Chemokine (C-C Motif) Ligand 20; LARC; Liver Activation Regulated Chemokine; Macrophage Inflammatory Protein-3 Alpha; MIP3A | A measurement of the chemokine (C-C motif) ligand 20 in a biological specimen. |
| C147315 | Chemokine (C-C Motif) Ligand 21 | 6Ckine; Chemokine (C-C Motif) Ligand 21; Secondary Lymphoid Tissue Chemokine | A measurement of the CCL21, chemokine (C-C motif) ligand 21, in a biological specimen. |
| C165949 | Chemokine (C-C Motif) Ligand 23 | Chemokine (C-C Motif) Ligand 23; CK-BETA-8; Ckb-8-1; CKb8; Hmrp-2a; MIP3; MPIF-1; SCYA23 | A measurement of the CCL23, chemokine (C-C motif) ligand 23, in a biological specimen. |
| C165950 | Chemokine (C-C Motif) Ligand 25 | Chemokine (C-C Motif) Ligand 25; Ckb15; SCYA25; TECK | A measurement of the CCL25, chemokine (C-C motif) ligand 25, in a biological specimen. |
| C130158 | Chemokine (C-C Motif) Ligand 7 | Chemokine (C-C Motif) Ligand 7; MCP3; Monocyte Chemotactic Protein 3 | A measurement of the CCL7, chemokine (C-C motif) ligand 7, in a biological specimen. |
| C165951 | Chemokine (C-C Motif) Ligand 8 | Chemokine (C-C Motif) Ligand 8; HC14; MCP2; SCYA10; SCYA8 | A measurement of the CCL8, chemokine (C-C motif) ligand 8, in a biological specimen. |
| C128952 | Chemokine (C-X-C Motif) Ligand 1 | Chemokine (C-X-C Motif) Ligand 1; GRO Alpha; GRO/KC; Melanoma Growth Stimulating Activity, Alpha | A measurement of the CXCL1, chemokine (C-X-C motif) ligand 1, in a biological specimen. |
| C112238 | Chemokine (C-X-C Motif) Ligand 10 | Chemokine (C-X-C Motif) Ligand 10; Interferon Gamma-induced Protein 10; Interferon-inducible Protein-10; IP-10; Small-inducible Cytokine B10 | A measurement of the CXCL10, chemokine (C-X-C motif) ligand 10, in a biological specimen. |
| C161360 | Chemokine (C-X-C Motif) Ligand 11 | Chemokine (C-X-C Motif) Ligand 11; I-TAC; IFN-inducible T Cell Alpha Chemoattractant; ITAC | A measurement of the chemokine (C-X-C motif) ligand 11 in a biological specimen. |
| C165954 | Chemokine (C-X-C Motif) Ligand 12 | Chemokine (C-X-C Motif) Ligand 12; IRH; PBSF; SCYB12; SDF1; SDF1A; SDF1B; Stromal Cell-Derived Factor-1 Alpha; Stromal Cell-Derived Factor-1 Beta; TLSF; TPAR1 | A measurement of the CXCL12, chemokine (C-X-C motif) ligand 12, in a biological specimen. |
| C147328 | Chemokine (C-X-C Motif) Ligand 13 | B Lymphocyte Chemoattractant; Chemokine (C-X-C Motif) Ligand 13 | A measurement of the CXCL13, chemokine (C-X-C motif) ligand 13, in a biological specimen. |
| C186039 | Chemokine (C-X-C Motif) Ligand 2 | Chemokine (C-X-C Motif) Ligand 2; GRO Beta; GRO2; MIP2-Alpha | A measurement of the CXCL2, chemokine (C-X-C motif) ligand 2, in a biological specimen. |
| C147329 | Chemokine (C-X-C Motif) Ligand 3 | Chemokine (C-X-C Motif) Ligand 3; GRO Gamma; Macrophage Inflammatory Protein 2-Beta; MIP2 Beta; MIP2B | A measurement of the CXCL3, chemokine (C-X-C motif) ligand 3, in a biological specimen. |
| C147330 | Chemokine (C-X-C Motif) Ligand 4 | Chemokine (C-X-C Motif) Ligand 4; Oncostatin A; Platelet Factor 4; PLF4 | A measurement of the CXCL4, chemokine (C-X-C motif) ligand 4, in a biological specimen. |
| C130159 | Chemokine (C-X-C Motif) Ligand 6 | Chemokine (C-X-C Motif) Ligand 6; GCP2; Granulocyte Chemotactic Protein 2 | A measurement of the CXCL6, chemokine (C-X-C motif) ligand 6, in a biological specimen. |
| C165955 | Chemokine (C-X-C Motif) Ligand 7 | B-TG1; Beta-TG; Chemokine (C-X-C Motif) Ligand 7; CTAP-III; CTAP3; CTAPIII; LA-PF4; LDGF; MDGF; NAP-2; Neutrophil-Activating Peptide 2; PBP; PPBP; Pro-Platelet Basic Protein; SCYB7; TC1; TC2; TGB; TGB1; THBGB; THBGB1 | A measurement of the pro-platelet basic protein in a biological specimen. |
| C165956 | Chemokine (C-X-C Motif) Ligand 9 | Chemokine (C-X-C Motif) Ligand 9; CMK; crg-10; Humig; MIG; SCYB9 | A measurement of the CXCL9, chemokine (C-X-C motif) ligand 9, in a biological specimen. |
| C100431 | Chemokine (C-X-C Motif) Receptor 3 | CD183; Chemokine (C-X-C Motif) Receptor 3; CXCR3; GPR9 | A measurement of the CXCR3, chemokine (C-X-C motif) receptor 3, in a biological specimen. |
| C187797 | Chemokine (C-X-C Motif) Receptor 4 | CD184; Chemokine (C-X-C Motif) Receptor 4; LPS-Associated Protein 3; Stromal Cell-Derived Factor 1 Receptor | A measurement of the CXCR4, chemokine (C-X-C motif) receptor 4, in a biological specimen. |
| C161361 | Chemokine (C-X3-C Motif) Ligand 1 | Chemokine (C-X3-C motif) Ligand 1; Fractalkine; Neurotactin | A measurement of the chemokine (C-X3-C motif) ligand 1 in a biological specimen. |
| C176239 | Chenodeoxycholate Compounds | Chenodeoxycholate Compounds; Chenodeoxycholic Acid Compounds | A measurement of the chenodeoxycholic acid, glycochenodeoxycholic acid, and taurochenodeoxycholic acid in a biological specimen. |
| C172498 | Chenodeoxycholate | Chenic Acid; Chenocholic Acid; Chenodeoxycholate; Chenodeoxycholic Acid | A measurement of the chenodeoxycholate in a biological specimen. |
| C187795 | Chitotriosidase | Chitinase 1; Chitotriosidase; Chitotriosidase-1 | A measurement of the chitotriosidase-1 in a biological specimen. |
| C184612 | Chloral Hydrate | Chloral Hydrate; Mickey Finn; Trichloroacetaldehyde Monohydrate | A measurement of the chloral hydrate in a biological specimen. |
| C75371 | Chlordiazepoxide | Chlordiazepoxide | A measurement of the chlordiazepoxide present in a biological specimen. |
| C106509 | Chloride Clearance | Chloride Clearance | A measurement of the volume of serum or plasma that would be cleared of chloride by excretion of urine for a specified unit of time (e.g. one minute). |
| C150816 | Chloride Excretion Rate | Chloride Excretion Rate | A measurement of the amount of chloride being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C64495 | Chloride | Chloride | A measurement of the chloride in a biological specimen. |
| C79440 | Chloride/Creatinine | Chloride/Creatinine | A relative measurement (ratio or percentage) of the chloride to creatinine in a biological specimen. |
| C184580 | Chlorphentermine | Chlorphentermine | A measurement of the chlorphentermine in a biological specimen. |
| C177968 | Chlorpromazine | Chlorpromazine | A measurement of the chlorpromazine in a biological specimen. |
| C176232 | Cholate Compounds | Cholate Compounds; Cholic Acid Compounds | A measurement of the cholic acid, glycocholic acid, hyocholic acid, and taurocholic acid in a biological specimen. |
| C172499 | Cholate | Cholate; Cholic Acid | A measurement of the cholate in a biological specimen. |
| C74850 | Cholecystokinin | Cholecystokinin; Pancreozymin | A measurement of the cholecystokinin hormone in a biological specimen. |
| C181435 | Cholestanol | 5alpha-Cholestanol; Beta-Cholestanol; Cholestanol; Dehydrocholesterol; Zymostanol | A measurement of the cholestanol in a biological specimen. |
| C74672 | Cholesterol Crystals | Cholesterol Crystals | A measurement of the cholesterol crystals present in a biological specimen. |
| C181436 | Cholesterol Sulfate | Cholesterol Sulfate | A measurement of the cholesterol sulfate in a biological specimen. |
| C105586 | Cholesterol | Cholesterol; Total Cholesterol | A measurement of the cholesterol in a biological specimen. |
| C80171 | Cholesterol/HDL-Cholesterol | Cholesterol/HDL-Cholesterol | A relative measurement (ratio or percentage) of total cholesterol to high-density lipoprotein cholesterol (HDL-C) in a biological specimen. |
| C103380 | Cholesteryl Ester Transfer Protein Act | Cholesteryl Ester Transfer Protein Act | A measurement of the biological activity of cholesteryl ester transfer protein in a biological specimen. |
| C120632 | Cholesteryl Ester Transfer Protein | Cholesteryl Ester Transfer Protein | A measurement of the cholesteryl ester transfer protein in a biological specimen. |
| C92289 | Cholinesterase | Cholinesterase | A measurement of the cholinesterase in a biological specimen. |
| C161374 | Choriogonadotropin Adj for Maternal Wt | Choriogonadotropin Adj for Maternal Wt; Choriogonadotropin Adjusted for Maternal Weight | A measurement of choriogonadotropin, which has been adjusted for maternal body weight, in a biological specimen. |
| C64851 | Choriogonadotropin Beta | Choriogonadotropin Beta; Pregnancy Test | A measurement of the Choriogonadotropin Beta in a biological specimen. |
| C147360 | Choriogonadotropin Beta, Free | Choriogonadotropin Beta, Free | A measurement of the free choriogonadotropin beta in a biological specimen. |
| C147128 | Choriogonadotropin | Choriogonadotropin | A measurement of the total choriogonadotropin in a biological specimen. |
| C147361 | Choriogonadotropin, Intact | Choriogonadotropin, Intact | A measurement of the intact choriogonadotropin in a biological specimen. |
| C147318 | Chromatin Antibodies | Chromatin Antibodies | A measurement of the chromatin antibodies in a biological specimen. |
| C122108 | Chromogranin A | Chromogranin A | A measurement of the chromogranin A in a biological specimen. |
| C174302 | Chylomicron Triglyceride | Chylomicron Triglyceride | A measurement of the chylomicron triglyceride in a biological specimen. |
| C120633 | Chylomicrons | Chylomicrons | A measurement of the chylomicrons in a biological specimen. |
| C111159 | Chymotrypsin | Chymotrypsin | A measurement of the total chymotrypsin in a biological specimen. |
| C96592 | Circulating Endothelial Cells | Circulating Endothelial Cells | A measurement of the circulating endothelial cells in a biological specimen. |
| C127611 | Circulating Immune Complexes | Circulating Immune Complexes | A measurement of the circulating immune complexes in a biological specimen. |
| C96593 | Circulating Tumor Cells | Circulating Tumor Cells | A measurement of the circulating tumor cells in a biological specimen. |
| C186036 | Circulating Tumor Cells, Apoptotic | Circulating Tumor Cells, Apoptotic | A measurement of the apoptotic circulating tumor cells in a biological specimen. |
| C186038 | Circulating Tumor Cells, Traditional | Circulating Tumor Cells, Traditional | A measurement of the traditional circulating tumor cells in a biological specimen. |
| C147327 | Citalopram | Citalopram | A measurement of the citalopram present in a biological specimen. |
| C163425 | Citrate Excretion Rate | Citrate Excretion Rate | A measurement of the amount of citrate being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C92248 | Citrate | Citrate; Citric Acid | A measurement of the citrate in a biological specimen. |
| C122110 | Citrate/Creatinine | Citrate/Creatinine; Citric Acid/Creatinine | A relative measurement (ratio or percentage) of the citrate to creatinine in a biological specimen. |
| C122109 | Citrulline | Citrulline | A measurement of the citrulline in a biological specimen. |
| C189500 | Citrulline/Creatinine | Citrulline/Creatinine | A relative measurement (ratio or percentage) of the citrulline to creatinine in a biological specimen. |
| C147319 | CK, Macromolecular Type 1/Total CK | CK, Macromolecular Type 1/Total CK; Creatine Kinase, Macromolecular Type 1/Total Creatine Kinase | A relative measurement (ratio or percentage) of the macromolecular type 1 creatine kinase to total creatine kinase in a biological specimen. |
| C147320 | CK, Macromolecular Type 2/Total CK | CK, Macromolecular Type 2/Total CK; Creatine Kinase, Macromolecular Type 2/Total Creatine Kinase | A relative measurement (ratio or percentage) of the macromolecular type 2 creatine kinase to total creatine kinase in a biological specimen. |
| C96594 | Clarity | Clarity | A measurement of the transparency of a biological specimen. |
| C184613 | Clobazam | Clobazam; cloBAZam | A measurement of the clobazam in a biological specimen. |
| C186031 | Clonazepam and/or Metabolites | Clonazepam and/or Metabolites | A measurement of the clonazepam and/or its metabolite(s) present in a biological specimen, for an assay that can measure both clonazepam and its metabolites. |
| C139082 | Clonazepam | Clonazepam | A measurement of the clonazepam present in a biological specimen. |
| C139077 | Clorazepate | Clorazepate | A measurement of the clorazepate present in a biological specimen. |
| C184581 | Clostebol | Clostebol | A measurement of the clostebol in a biological specimen. |
| C187805 | Clot Lysis Time | Clot Lysis Time; ECLT; ELT; Euglobulin Clot Lysis Time; Euglobulin Lysis Time | A measurement of the amount of time it takes for dissolution of a fibrin clot in a biological specimen. |
| C181437 | Clot Retraction Time | Clot Retraction Time | A measurement of the amount of time it takes for a clot to retract, or pull away from, the wall of a glass collection container. |
| C181438 | Clot Retraction | Clot Retraction; Clot Retraction, Qualitative | A qualitative assessment of clot retraction in a biological specimen. |
| C102261 | Clue Cells | Clue Cells | A measurement of the clue cells in a biological specimen. |
| C112239 | Coagulation Index | CI; Coagulation Index | A measurement of the efficiency of coagulation of a biological specimen. This is calculated by a mathematical formula that takes into account the R value, K value, angle and maximum amplitude of clot formation. |
| C156510 | Cocaethylene | Cocaethylene; Cocaine Ethyl | A measurement of the cocaethylene present in a biological specimen. |
| C142273 | Cocaine Amphetamine-Reg Transcript Prot | CART; Cocaine Amphetamine-Reg Transcript Prot; Cocaine and Amphetamine-Regulated Transcript Protein | A measurement of the cocaine and amphetamine-regulated transcript protein in a biological specimen. |
| C172490 | Cocaine and/or Metabolites | Cocaine and/or Metabolites | A measurement of the cocaine and/or its metabolite(s) present in a biological specimen, for an assay that can measure both cocaine and its metabolites. |
| C142274 | Cocaine Benzoylecgonine Ecgonine | Cocaine Benzoylecgonine Ecgonine | A measurement of the cocaine, benzoylecgonine, and/or ecgonine in a biological specimen. |
| C172491 | Cocaine Metabolites | Cocaine Metabolites | A measurement of any cocaine drug class metabolite(s) present in a biological specimen. |
| C74690 | Cocaine | Cocaine | A measurement of the cocaine present in a biological specimen. |
| C74877 | Codeine | Codeine | A measurement of the codeine present in a biological specimen. |
| C176311 | Coefficient of Fat Absorption | Coefficient of Fat Absorption | A measurement of the coefficient of fat absorption in a biological specimen. |
| C176310 | Coefficient of Nitrogen Absorption | Coefficient of Nitrogen Absorption | A measurement of the coefficient of nitrogen absorption in a biological specimen. |
| C165945 | Collagen III Neo-Peptide C3M | Collagen III Neo-Peptide C3M | A measurement of the collagen III neo-peptide C3M in a biological specimen. |
| C103383 | Collagen Type IV | Collagen Type IV | A measurement of the collagen type IV in a biological specimen. |
| C64546 | Color | Color | A measurement of the color of a biological specimen. |
| C135405 | Columnar Epi Cells/Non-Squam Epi Cells | Columnar Epi Cells/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the columnar epithelial cells to non-squamous epithelial cells in a biological specimen. |
| C165941 | Common Ragweed Pollen IgE AB RAST Score | Common Ragweed Pollen IgE AB RAST Score | A classification of the amount of Ambrosia artemisiifolia pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C147285 | Common Ragweed Pollen IgE Antibody | Common Ragweed Pollen IgE Antibody | A measurement of the Ambrosia elatior pollen antigen IgE antibody in a biological specimen. |
| C135403 | Complement Ba | Ba Fragment of Complement Factor B; Ba Fragment of Factor B; Complement Ba | A measurement of the Ba fragment of complement factor B in a biological specimen. |
| C80172 | Complement Bb | Bb Fragment of Complement Factor B; Bb Fragment of Factor B; Complement Bb | A measurement of the Bb fragment of complement factor B in a biological specimen. |
| C147313 | Complement C1 Esterase Inhibitor | Complement C1 Esterase Inhibitor | A measurement of the complement C1 esterase inhibitor in a biological specimen. |
| C80173 | Complement C1q Antibody | Complement C1q Antibody | A measurement of the complement C1q antibody in a biological specimen. |
| C186029 | Complement C1q | Complement C1q | A measurement of the complement C1q in a biological specimen. |
| C80174 | Complement C3 | Complement C3 | A measurement of the complement C3 in a biological specimen. |
| C163423 | Complement C3a DesArg | Acylation-Stimulating Protein; ASP; Complement C3a DesArg | A measurement of the complement C3a DesArg in a biological specimen. |
| C80175 | Complement C3a | Complement C3a | A measurement of the complement C3a in a biological specimen. |
| C80176 | Complement C3b | Complement C3b | A measurement of the complement C3b in a biological specimen. |
| C184521 | Complement C3c | Complement C3c | A measurement of the complement C3c in a biological specimen. |
| C119271 | Complement C3d Antibody | Complement C3d Antibody | A measurement of the complement C3d antibody in a biological specimen. |
| C80177 | Complement C4 | Complement C4 | A measurement of the complement C4 in a biological specimen. |
| C80178 | Complement C4a | Complement C4a | A measurement of the complement C4a in a biological specimen. |
| C127610 | Complement C4d | Complement C4d | A measurement of the complement C4d in a biological specimen. |
| C160935 | Complement C5 | Complement C5 | A measurement of the total complement C5 in a biological specimen. |
| C161357 | Complement C5, Free | Complement C5, Free | A measurement of the free complement C5 in a biological specimen. |
| C80179 | Complement C5a | Complement C5a | A measurement of the complement C5a in a biological specimen. |
| C158235 | Complement C5b-9 | Complement C5b-9 | A measurement of the complement C5b-9 in a biological specimen. |
| C147317 | Complement CH100 | CH100; Complement CH100; Total Hemolytic Complement CH100 | A measurement of the complement required to lyse 100 percent of red blood cells in a biological specimen. |
| C100423 | Complement CH50 | CH50; Complement CH50; Total Hemolytic Complement CH50 | A measurement of the complement required to lyse 50 percent of red blood cells in a biological specimen. |
| C80160 | Complement Total | Complement Total; Total Hemolytic Complement | A measurement of the total complement in a biological specimen. |
| C189504 | Connective Tissue Growth Factor | Cellular Communication Network Factor 2; CN2; Connective Tissue Growth Factor; IGFBP8 | A measurement of the connective tissue growth factor in a biological specimen. |
| C95110 | Consistency | Consistency | A description about the firmness or make-up of an entity. |
| C127612 | Copeptin | Copeptin | A measurement of the copeptin in a biological specimen. |
| C111161 | Copper | Copper; Cu | A measurement of copper in a biological specimen. |
| C139066 | Corpuscular Hemoglobin Content | Cellular Hemoglobin Content; CH; Corpuscular Hemoglobin Content | A measurement of the mean erythrocyte hemoglobin content within an individual erythrocyte, calculated as the product of cell volume and cell hemoglobin concentration. |
| C139068 | Corpuscular HGB Conc Distribution Width | Corpuscular Hemoglobin Concentration Distribution Width; Corpuscular HGB Conc Distribution Width | A measurement of the standard deviation of hemoglobin concentrations in erythrocytes in a biological specimen, calculated as the standard deviation of hemoglobin content divided by the mean hemoglobin content. |
| C139067 | Corpuscular HGB Concentration Mean | Corpuscular HGB Concentration Mean | A direct measurement of the concentration of hemoglobin within individual erythrocytes in a biological specimen, reported as a mean. |
| C79434 | Corticosterone | Corticosterone | A measurement of corticosterone in a biological specimen. |
| C106511 | Corticosterone/Creatinine | Corticosterone/Creatinine | A relative measurement (ratio or percentage) of the corticosterone to creatinine present in a sample. |
| C74851 | Corticotropin Releasing Hormone | Corticotropin Releasing Factor; Corticotropin Releasing Hormone | A measurement of the corticotropin releasing hormone in a biological specimen. |
| C74781 | Cortisol | Cortisol; Total Cortisol | A measurement of the cortisol in a biological specimen. |
| C163427 | Cortisol, Free Excretion Rate | Cortisol, Free Excretion Rate | A measurement of the amount of free cortisol being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C88113 | Cortisol, Free | Cortisol, Free | A measurement of the free, unbound cortisol in a biological specimen. |
| C106512 | Cortisol/Creatinine | Cortisol/Creatinine | A relative measurement (ratio or percentage) of the cortisol to creatinine present in a sample. |
| C92249 | Cotinine | Cotinine | A measurement of the cotinine in a biological specimen. |
| C147280 | Cow Milk Protein Antigen IgE Antibody | Cow Milk Protein Antigen IgE Antibody | A measurement of the cow milk protein antigen IgE antibody in a biological specimen. |
| C165938 | Cow Milk Protein IgE AB RAST Score | Cow Milk Protein IgE AB RAST Score | A classification of the amount of cow milk protein IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C64490 | Creatine Kinase BB | Creatine Kinase BB | A measurement of the homozygous B-type creatine kinase in a biological specimen. |
| C79466 | Creatine Kinase BB/Total Creatine Kinase | Creatine Kinase BB/Total Creatine Kinase | A relative measurement (ratio or percentage) of the BB-type creatine kinase to total creatine kinase in a biological specimen. |
| C64491 | Creatine Kinase MB | Creatine Kinase MB | A measurement of the heterozygous MB-type creatine kinase in a biological specimen. |
| C79441 | Creatine Kinase MB/Total Creatine Kinase | Creatine Kinase MB/Total Creatine Kinase | A relative measurement (ratio or percentage) of the MB-type creatine kinase to total creatine kinase in a biological specimen. |
| C64494 | Creatine Kinase MM | Creatine Kinase MM | A measurement of the homozygous M-type creatine kinase in a biological specimen. |
| C79442 | Creatine Kinase MM/Total Creatine Kinase | Creatine Kinase MM/Total Creatine Kinase | A relative measurement (ratio or percentage) of the MM-type creatine kinase to total creatine kinase in a biological specimen. |
| C64489 | Creatine Kinase | CPK; Creatine Kinase; Creatine Phosphokinase | A measurement of the total creatine kinase in a biological specimen. |
| C147324 | Creatinine Clearance Adjusted for BSA | Creatinine Clearance Adjusted for BSA | A measurement of the volume of serum or plasma that would be cleared of creatinine by excretion of urine for a specified unit of time (e.g. one minute), adjusted for body surface area. |
| C25747 | Creatinine Clearance | Creatinine Clearance | A measurement of the volume of serum or plasma that would be cleared of creatinine by excretion of urine for a specified unit of time (e.g. one minute). |
| C150847 | Creatinine Clearance, Estimated | Creatinine Clearance, Estimated | An estimate of the volume of serum or plasma that would be cleared of creatinine by excretion of urine for a specified unit of time (e.g. one minute). |
| C150817 | Creatinine Excretion Rate | Creatinine Excretion Rate | A measurement of the amount of creatinine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C64547 | Creatinine | Creatinine | A measurement of the creatinine in a biological specimen. |
| C74703 | Crenated Cells | Crenated Cells | A measurement of the crenated cells in a biological specimen. |
| C147326 | Cryofibrinogen | Cryofibrinogen | A measurement of the cryofibrinogen in a biological specimen. |
| C147325 | Cryoglobulin Volume/Serum Volume | Cryoglobulin Volume/Serum Volume | A relative measurement (ratio or percentage) of the volume of cryoglobulin to total serum volume in a biological specimen. |
| C111164 | Cryoglobulin | Cryoglobulin | A measurement of cryoglobulin in a biological specimen. |
| C74673 | Crystals | Crystals | A statement that indicates crystals were looked for in a biological specimen. |
| C154735 | CSF IgG Index | CSF IgG Index; CSF Index; IgG Index | A relative measurement (ratio) of the IgG to albumin in cerebrospinal fluid to the IgG to albumin in serum. |
| C124339 | Cyclic Adenosine 3,5-Monophosphate | Cyclic Adenosine 3,5-Monophosphate | A measurement of cyclic adenosine 3,5-monophosphate in a biological specimen. |
| C186030 | Cyclic Adenosine Monophosphate/Creat | Cyclic Adenosine 3,5-Monophosphate/Creatinine; Cyclic Adenosine Monophosphate/Creat; Cyclic Adenosine Monophosphate/Creatinine | A relative measurement (ratio) of the cyclic adenosine 3,5-monophosphate to creatinine in a biological specimen. |
| C96595 | Cyclic Citrullinated Peptide Antibody | Cyclic Citrullinated Peptide Antibody | A measurement of the cyclic citrullinated peptide antibody in a biological specimen. |
| C147316 | Cyclic Citrullinated Peptide IgG Ab | Cyclic Citrullinated Peptide IgG Ab; Cyclic Citrullinated Peptide IgG Antibody | A measurement of the cyclic citrullinated peptide IgG antibody in a biological specimen. |
| C111165 | Cyclic Guanosine Monophosphate | Cyclic Guanosine Monophosphate | A measurement of the cyclic guanosine 3,5-monophosphate in a biological specimen. |
| C150838 | Cylindroid Casts | Cylindroid Casts; Cylindroid Pseudocasts | A measurement of cylindroid casts (casts with a tapering end) in a biological specimen. |
| C172520 | Cystathionine Beta-Synthase | Cystathionine Beta-Synthase | A measurement of the cystathionine beta-synthase in a biological specimen. |
| C147331 | Cystathionine | Cystathionine | A measurement of the cystathionine in a biological specimen. |
| C92290 | Cystatin C | Cystatin C | A measurement of the cystatin C in a biological specimen. |
| C106513 | Cystatin C/Creatinine | Cystatin C/Creatinine | A relative measurement (ratio or percentage) of the cystatin C to creatinine present in a sample. |
| C172518 | Cysteine | Cysteine | A measurement of the cysteine in a biological specimen. |
| C189517 | Cysteinyl Leukotriene Receptor 1 | CysLTR1; Cysteinyl Leukotriene Receptor 1 | A measurement of the cysteinyl leukotriene receptor 1 in a biological specimen. |
| C74674 | Cystine Crystals | Cystine Crystals | A measurement of the cystine crystals present in a biological specimen. |
| C105441 | Cystine | Cystine | A measurement of the cystine in a biological specimen. |
| C163426 | Cytidine-Uridine Monophosphate Kinase 2 | Cytidine-Uridine Monophosphate Kinase 2; Cytidine/Uridine Monophosphate Kinase 2 | A measurement of the cytidine-uridine monophosphate kinase 2 in a biological specimen. |
| C161355 | Cytochrome P450 2C9 | Cytochrome P450 2C9 | A measurement of the cytochrome P450 2C9 enzyme in a biological specimen. |
| C130160 | Cytokeratin 18 Fragment | Cytokeratin 18 Fragment | A measurement of the cytokeratin 18 fragment in a biological specimen. |
| C106514 | Cytokeratin 19 Fragment 21-1 | CYFRA21-1; Cytokeratin 19 Fragment 21-1 | A measurement of the cytokeratin 19 fragment 21-1 in a biological specimen. |
| C163484 | Cytomegalovirus-Induced Gene 5 Protein | Cytomegalovirus-Induced Gene 5 Protein; Radical S-adenosyl Methionine Domain-Containing Protein 2 | A measurement of the cytomegalovirus-induced gene 5 protein in a biological specimen. |
| C111166 | Cytoplasmic Basophilia Neutrophil | Cytoplasmic Basophilia Neutrophil | A measurement of the neutrophils in a biological specimen showing a dark staining pattern in the cytoplasm due to increased acidic content. |
| C82621 | D-Dimer | D-Dimer | A measurement of the d-dimers in a biological specimen. |
| C174298 | D-Norpseudoephedrine | (+)-Norpseudoephedrine; Cathine; D-Norpseudoephedrine | A measurement of the D-norpseudoephedrine in a biological specimen. |
| C130132 | D. farinae Antigen IgE Antibody | American House Dust Mite IgE Antibody; D. farinae Antigen IgE Antibody; Dermatophagoides farinae IgE Antibody | A measurement of the Dermatophagoides farinae antigen IgE antibody in a biological specimen. |
| C130133 | D. farinae Antigen IgG Antibody | American House Dust Mite IgG Antibody; D. farinae Antigen IgG Antibody; Dermatophagoides farinae IgG Antibody | A measurement of the Dermatophagoides farinae antigen IgG antibody in a biological specimen. |
| C165894 | D. farinae Antigen IgG4 Antibody | American House Dust Mite IgG4 Antibody; D. farinae Antigen IgG4 Antibody; Dermatophagoides farinae IgG4 Antibody | A measurement of the Dermatophagoides farinae antigen IgG4 antibody in a biological specimen. |
| C165879 | D. farinae IgE AB RAST Score | American House Dust Mite IgE Antibody RAST Score; D. farinae IgE AB RAST Score; Dermatophagoides farinae IgE Antibody RAST Score | A classification of the amount of Dermatophagoides farinae IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165916 | D. farinae IgG AB RAST Score | American House Dust Mite IgG Antibody RAST Score; D. farinae IgG AB RAST Score | A classification of the amount of D. farinae antigen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130134 | D. pteronyssinus Antigen IgE Antibody | D. pteronyssinus Antigen IgE Antibody; Dermatophagoides pteronyssinus IgE Antibody; European House Dust Mite IgE Antibody | A measurement of the Dermatophagoides pteronyssinus antigen IgE antibody in a biological specimen. |
| C130135 | D. pteronyssinus Antigen IgG Antibody | D. pteronyssinus Antigen IgG Antibody; Dermatophagoides pteronyssinus IgG Antibody; European House Dust Mite IgG Antibody | A measurement of the Dermatophagoides pteronyssinus antigen IgG antibody in a biological specimen. |
| C165896 | D. pteronyssinus Antigen IgG4 Antibody | D. pteronyssinus Antigen IgG4 Antibody; Dermatophagoides pteronyssinus IgG4 Antibody; European House Dust Mite IgG4 Antibody | A measurement of the Dermatophagoides pteronyssinus antigen IgG4 antibody in a biological specimen. |
| C165880 | D. pteronyssinus IgE AB RAST Score | D. pteronyssinus IgE AB RAST Score; Dermatophagoides pteronyssinus IgE Antibody RAST Score; European House Dust Mite IgE Antibody RAST Score | A classification of the amount of Dermatophagoides pteronyssinus antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165917 | D. pteronyssinus IgG AB RAST Score | D. pteronyssinus Antigen IgG AB RAST Score; Dermatophagoides pteronyssinus IgG Antibody; European House Dust Mite IgG Antibody | A classification of the amount of D. pteronyssinus antigen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C64801 | Dacryocytes | Dacryocytes; Tear Shaped Erythrocytes; Teardrop Cells | A measurement of dacryocytes in a biological specimen. |
| C130119 | Dairy Mix Antigen IgG Antibody | Dairy Mix Antigen IgG Antibody | A measurement of the dairy mix antigen IgG antibody in a biological specimen. |
| C165911 | Dairy Mix IgG AB RAST Score | Dairy Mix IgG AB RAST Score | A classification of the amount of dairy mix IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C163428 | DEAD Box Protein 58 | DEAD Box Protein 58; DExD/H-Box Helicase 58; Probable ATP-Dependent RNA Helicase DDX58 | A measurement of the DEAD box protein 58 in a biological specimen. |
| C156536 | Decanoylcarnitine | C10; Decanoylcarnitine | A measurement of the decanoylcarnitine in a biological specimen. |
| C172512 | Decorin | DCN; Decorin | A measurement of the decorin in a biological specimen. |
| C111190 | Degenerated Leukocytes | Degenerated Leukocytes; Degenerated WBC; Degenerated White Blood Cells | A measurement of the degenerated leukocytes (leukocytes that show deterioration in form or function) in a biological specimen. |
| C96629 | Dehydroepiandrosterone Sulfate | Dehydroepiandrosterone Sulfate; DHEA Sulfate; DHEA-S; sDHEA | A measurement of the sulfated Dehydroepiandrosterone in a biological specimen. |
| C74852 | Dehydroepiandrosterone | Dehydroepiandrosterone; Dehydroisoandrosterone | A measurement of the dehydroepiandrosterone hormone in a biological specimen. |
| C156537 | Delta Aminolevulinate | 5-Aminolevulinic Acid; 5ALA; dALA; Delta Aminolevulinate; Delta Aminolevulinic Acid | A measurement of the delta aminolevulinic acid in a biological specimen. |
| C156538 | Delta Aminolevulinate/Creatinine | Delta Aminolevulinate/Creatinine | A relative measurement (ratio or percentage) of the delta aminolevulinate to creatinine in a biological specimen. |
| C45781 | Density | Density | A measurement of the compactness of a biological specimen expressed in mass per unit volume. |
| C172500 | Deoxycholate | Deoxycholate; Deoxycholic Acid | A measurement of the deoxycholate in a biological specimen. |
| C124343 | Deoxyhemoglobin | Deoxyhemoglobin | A measurement of the deoxyhemoglobin, hemoglobin without oxygen, in a biological specimen. |
| C79443 | Deoxypyridinoline | Deoxypyridinoline | A measurement of the deoxypyridinoline in a biological specimen. |
| C79444 | Deoxypyridinoline/Creatinine | Deoxypyridinoline/Creatinine | A relative measurement (ratio or percentage) of the deoxypyridinoline to creatinine in a biological specimen. |
| C135409 | Deoxyribonucleic Acid | Deoxyribonucleic Acid | A measurement of a targeted deoxyribonucleic acid (DNA) in a biological specimen. |
| C186040 | Desipramine | Desipramine | A measurement of the desipramine in a biological specimen. |
| C189494 | Desmethylcitalopram | Desmethyl Citalopram; Desmethylcitalopram; Norcitalopram | A measurement of the desmethylcitalopram in a biological specimen. |
| C122114 | Desmoglein 1 Antibody | Desmoglein 1 Antibody | A measurement of the desmoglein 1 antibody in a biological specimen. |
| C122115 | Desmoglein 3 Antibody | Desmoglein 3 Antibody | A measurement of the desmoglein 3 antibody in a biological specimen. |
| C184535 | Desomorphine | Desomorphine | A measurement of the desomorphine in a biological specimen. |
| C184582 | Desoxymethyltestosterone | Desoxymethyltestosterone | A measurement of the desoxymethyltestosterone in a biological specimen. |
| C147333 | Desvenlafaxine | Desvenlafaxine; O-Desmethylvenlafaxine | A measurement of the desvenlafaxine present in a biological specimen. |
| C102262 | Dextroamphetamine | d-amphetamine; Dextroamphetamine | A measurement of the dextroamphetamine in a biological specimen. |
| C189655 | Di-Desmethylcitalopram | Di-Desmethylcitalopram | A measurement of the di-desmethylcitalopram in a biological specimen. |
| C75372 | Diazepam | Diazepam | A measurement of the diazepam present in a biological specimen. |
| C135407 | Dicalcium Phosphate Crystals | Dicalcium Phosphate Crystals | A measurement of dicalcium phosphate crystals in a biological specimen. |
| C165957 | Dickkopf WNT Signaling Path Inhibitor 1 | Dickkopf WNT Signaling Pathway Inhibitor 1; DKK-1; SK | A measurement of the dickkopf WNT signaling pathway inhibitor 1 in a biological specimen. |
| C184614 | Diethylpropion | Diethylpropion | A measurement of the diethylpropion in a biological specimen. |
| C74878 | Dihydrocodeine | Dihydrocodeine | A measurement of the dihydrocodeine present in a biological specimen. |
| C74853 | Dihydrotestosterone | Androstanalone; Androstanolone; Dihydrotestosterone | A measurement of the dihydrotestosterone hormone in a biological specimen. |
| C103386 | Dilute Russell's Viper Venom Time Ratio | Dilute Russell's Viper Venom Time Ratio; Lupus Anticoagulant Ratio | A relative measurement of the dilute Russell's viper venom time in a subject sample to a control sample. |
| C96696 | Dilute Russell's Viper Venom Time | Dilute Russell's Viper Venom Time; Lupus Anticoagulant Test | A measurement of the time it takes a plasma sample to clot after adding dilute Russell's viper venom. |
| C172519 | Dimethylglycine | Dimethylglycine | A measurement of the dimethylglycine in a biological specimen. |
| C117853 | Dimorphic Erythrocyte Population | Dimorphic Erythrocyte Population; Dimorphic RBC Population | Examination of a biological specimen to detect the presence of dimorphic erythrocyte population. |
| C177992 | Dipeptidyl Peptidase-4 | Dipeptidyl Peptidase-4 | A measurement of the dipeptidyl peptidase-4 in a biological specimen. |
| C184569 | Diphenoxylate | Diphenoxylate | A measurement of the diphenoxylate in a biological specimen. |
| C184540 | Dipipanone | Dipipanone | A measurement of the dipipanone in a biological specimen. |
| C64481 | Direct Bilirubin | Direct Bilirubin | A measurement of the conjugated or water-soluble bilirubin in a biological specimen. |
| C158226 | Direct Bilirubin/Bilirubin | Direct Bilirubin/Bilirubin | A relative measurement (ratio or percentage) of the direct bilirubin to total bilirubin in a biological specimen. |
| C135408 | DNA Fragmentation Index | DNA Fragmentation Index | A measurement of the deoxyribonucleic acid fragmentation within the nucleated cells of a biological specimen. |
| C100463 | DNase-B Antibody | Anti-Dnase B; DNase-B Antibody | A measurement of Dnase-B antibody in a biological specimen. |
| C130130 | Dog Dander Antigen IgA Antibody | Dog Dander Antigen IgA Antibody | A measurement of the Canis lupus dander antigen IgA antibody in a biological specimen. |
| C130128 | Dog Dander Antigen IgE Antibody | Dog Dander Antigen IgE Antibody | A measurement of the Canis lupus dander antigen IgE antibody in a biological specimen. |
| C130129 | Dog Dander Antigen IgG Antibody | Dog Dander Antigen IgG Antibody | A measurement of the Canis lupus dander antigen IgG antibody in a biological specimen. |
| C130131 | Dog Dander Antigen IgG4 Antibody | Dog Dander Antigen IgG4 Antibody | A measurement of the Canis lupus dander antigen IgG4 antibody in a biological specimen. |
| C165932 | Dog Dander IgE AB RAST Score | Dog Dander IgE AB RAST Score | A classification of the amount of canis lupus dander IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165915 | Dog Dander IgG AB RAST Score | Dog Dander IgG AB RAST Score | A classification of the amount of Canis lupus IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C74610 | Dohle Bodies | Dohle Bodies | A measurement of the Dohle bodies (blue-gray, basophilic, leukocyte inclusions located in the peripheral cytoplasm of neutrophils) in a biological specimen. |
| C163429 | Dopamine Excretion Rate | Dopamine Excretion Rate | A measurement of the amount of dopamine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C74854 | Dopamine | Dopamine | A measurement of the dopamine hormone in a biological specimen. |
| C186041 | Doxepin and/or Metabolites | Doxepin and/or Metabolites | A measurement of the doxepin and/or its metabolite(s) present in a biological specimen, for an assay that can measure both doxepin and its metabolites. |
| C184583 | Drostanolone | Dromostanolone; Drostanolone; Medrosteron; Medrotestron; Metholone | A measurement of the drostanolone in a biological specimen. |
| C156533 | Drug Crystals | Drug Crystals | A measurement of the drug crystals in a biological specimen. |
| C78139 | Drug Screen | Drug Screen | An indication of the presence or absence of recreational drugs or drugs of abuse in a biological specimen. |
| C161373 | dRVVT Screen to Confirm Pct Difference | dRVVT Screen to Confirm Pct Difference; dRVVT Screen to Confirm Percent Difference | A measurement to confirm the presence of Lupus anticoagulants, calculated as [(Screen dRVVT - Confirm dRVVT)/Screen dRVVT]x100. |
| C163430 | DRVVT Screen to Confirm Ratio | DRVVT Screen to Confirm Ratio | A relative measurement (ratio) of the dilute Russell's viper venom time without the presence of excess phospholipid to the dRVVT in the presence of excess phospholipid. |
| C100441 | DTPA Clearance | DTPA Clearance | A measurement of the volume of serum or plasma that would be cleared of Diethylenetriamine pentaacetate (DTPA) by excretion of urine for a specified unit of time (e.g. one minute). |
| C187798 | Duloxetine | Duloxetine | A measurement of the duloxetine in a biological specimen. |
| C135441 | Dysmorphic Erythrocytes | Dysmorphic Erythrocytes | A measurement of the dysmorphic erythrocytes in a biological specimen. |
| C150839 | Dysmorphic Erythrocytes/Erythrocytes | Dysmorphic Erythrocytes/Erythrocytes | A measurement (ratio or percentage) of dysmorphic erythrocytes to total erythrocytes in a biological specimen. |
| C154736 | E-Selectin | E-Selectin | A measurement of total E-selectin in a biological specimen. |
| C187799 | E3 Ubiquitin-Protein Ligase TRIM33 | E3 Ubiquitin-Protein Ligase TRIM33; Tripartite Motif Containing 33 | A measurement of the E3 ubiquitin-protein ligase TRIM33 in a biological specimen. |
| C100422 | Ecarin Clotting Time | Ecarin Clotting Time | A measurement of the activity of thrombin inhibitors in a biological specimen based on the generation of meizothrombin. |
| C96598 | Eccentrocytes | Eccentrocytes | A measurement of the eccentrocytes (erythrocytes in which the hemoglobin is localized to a particular portion of the cell, noticeable as localized staining) in a biological specimen. |
| C100440 | EDTA Clearance | EDTA Clearance | A measurement of the volume of serum or plasma that would be cleared of Ethylenediamine tetraacetic acid (EDTA) by excretion of urine for a specified unit of time (e.g. one minute). |
| C147281 | Egg White Antigen IgE Antibody | Egg White Antigen IgE Antibody | A measurement of the egg white antigen IgE antibody in a biological specimen. |
| C165939 | Egg White IgE AB RAST Score | Egg White IgE AB RAST Score | A classification of the amount of egg white antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C64549 | Elliptocytes | Elliptocytes | A measurement of the elliptocytes (elliptically shaped cell with blunt ends and a long axis twice the length of its short axis) in a biological specimen. |
| C102266 | Endogenous Thrombin Potential | Endogenous Thrombin Potential | A measurement of the total concentration of thrombin generated in the presence of a substrate in a plasma or blood sample. |
| C163432 | Endomysial Antibody | Endomysial Antibody; Endomysium Antibody | A measurement of the endomysial antibody in a biological specimen. |
| C147334 | Endomysial IgA Antibody | Endomysial IgA Antibody; Endomysium IgA Antibody | A measurement of the endomysial IgA antibody in a biological specimen. |
| C172509 | Endostatin | Collagen Type XVIII Alpha 1 Chain; Endostatin | A measurement of the endostatin in a biological specimen. |
| C82008 | Endothelin-1 | Endothelin-1 | A measurement of the endothelin-1 in a biological specimen. |
| C187800 | Endothelin-3 | Endothelin-3; ET-3 | A measurement of the endothelin-3 in a biological specimen. |
| C130085 | English Plantain Pollen IgA | English Plantain Pollen IgA | A measurement of the Plantagio lanceolata pollen antigen IgA antibody in a biological specimen. |
| C130084 | English Plantain Pollen IgE | English Plantain Pollen IgE | A measurement of the Plantagio lanceolata pollen antigen IgE antibody in a biological specimen. |
| C130086 | English Plantain Pollen IgG | English Plantain Pollen IgG | A measurement of the Plantagio lanceolata pollen antigen IgG antibody in a biological specimen. |
| C130087 | English Plantain Pollen IgG4 | English Plantain Pollen IgG4 | A measurement of the Plantagio lanceolata pollen antigen IgG4 antibody in a biological specimen. |
| C165887 | EnglishPlantain Pollen IgE AB RAST Score | English Plantain Pollen IgE AB RAST Score; EnglishPlantain Pollen IgE AB RAST Score | A classification of the amount of Plantagio lanceolata pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165901 | EnglishPlantain Pollen IgG AB RAST Score | English Plantain Pollen IgG AB RAST Score; EnglishPlantain Pollen IgG AB RAST Score | A classification of the amount of Plantagio lanceolata pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C184644 | Eosinophil-Derived Neurotoxin | Eosinophil Protein-X; Eosinophil-Derived Neurotoxin; RAF3; Ribonuclease A Family Member 2 | A measurement of the eosinophil-derived neurotoxin in a biological specimen. |
| C84819 | Eosinophilic Metamyelocytes | Eosinophilic Metamyelocytes | A measurement of the eosinphilic metamyelocytes in a biological specimen. |
| C84821 | Eosinophilic Myelocytes | Eosinophilic Myelocytes | A measurement of the eosinophilic myelocytes in a biological specimen. |
| C181449 | Eosinophilic Myelocytes/Lymphocytes | Eosinophilic Myelocytes/Lymphocytes | A relative measurement (ratio or percentage) of the eosinophilic myelocytes to lymphocytes in a biological specimen (for example a bone marrow specimen). |
| C114216 | Eosinophils Band Form | Eosinophils Band Form | A measurement of the banded eosinophils in a biological specimen. |
| C114217 | Eosinophils Band Form/Leukocytes | Eosinophils Band Form/Leukocytes | A relative measurement (ratio or percentage) of the banded eosinophils to leukocytes in a biological specimen. |
| C64550 | Eosinophils | Eosinophils | A measurement of the eosinophils in a biological specimen. |
| C135412 | Eosinophils, Segmented | Eosinophils, Segmented | A measurement of the segmented eosinophils in a biological specimen. |
| C64604 | Eosinophils/Leukocytes | Eosinophils/Leukocytes | A relative measurement (ratio or percentage) of the eosinophils to leukocytes in a biological specimen. |
| C135411 | Eosinophils/Non-Squam Epi Cells | Eosinophils/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the eosinophils to non-squamous epithelial cells in a biological specimen. |
| C150840 | Eosinophils/Nucleated Cells | Eosinophils/Nucleated Cells | A relative measurement (ratio or percentage) of eosinophils to nucleated cells in a biological specimen. |
| C98720 | Eosinophils/Total Cells | Eosinophils/Total Cells | A relative measurement (ratio or percentage) of the eosinophils to total cells in a biological specimen (for example a bone marrow specimen). |
| C81952 | Eotaxin-1 | Chemokine Ligand 11; Eotaxin-1 | A measurement of the eotaxin-1 in a biological specimen. |
| C81953 | Eotaxin-2 | Chemokine Ligand 24; Eotaxin-2 | A measurement of the eotaxin-2 in a biological specimen. |
| C81954 | Eotaxin-3 | CCL26; Chemokine (C-C Motif) Ligand 26; Chemokine Ligand 26; Eotaxin-3 | A measurement of the eotaxin-3 in a biological specimen. |
| C174296 | Ephedrine | Ephedrine | A measurement of the ephedrine in a biological specimen. |
| C135414 | Epi Cells/Non-Squam Epi Cells | Epi Cells/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the epithelial cells to non-squamous epithelial cells in a biological specimen. |
| C112273 | Epidermal Growth Factor Receptor | Epidermal Growth Factor Receptor; ERBB1; HER1 | A measurement of the epidermal growth factor receptor in a biological specimen. |
| C181452 | Epidermal Growth Factor Receptor, Free | Epidermal Growth Factor Receptor, Free | A measurement of the free (unbound) epidermal growth factor receptor in a biological specimen. |
| C82009 | Epidermal Growth Factor | Epidermal Growth Factor | A measurement of the epidermal growth factor in a biological specimen. |
| C176304 | Epimerized Ursodeoxycholate | Epimerized Ursodeoxycholate; Epimerized Ursodeoxycholic Acid | A measurement of the epimerized ursodeoxycholate in a biological specimen. |
| C163433 | Epinephrine Excretion Rate | Epinephrine Excretion Rate | A measurement of the amount of epinephrine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C79445 | Epinephrine | Adrenaline; Epinephrine | A measurement of the epinephrine hormone in a biological specimen. |
| C82010 | Epith Neutrophil-Activating Peptide 78 | Epith Neutrophil-Activating Peptide 78 | A measurement of the epithelial neutrophil-activating peptide in a biological specimen. |
| C74779 | Epithelial Casts | Epithelial Casts | A measurement of the epithelial cell casts present in a biological specimen. |
| C187801 | Epithelial Cell Clumps | Epithelial Cell Clumps | A measurement of the epithelial cell clumps in a biological specimen. |
| C64605 | Epithelial Cells | Epithelial Cells | A measurement of the epithelial cells in a biological specimen. |
| C130161 | Epithelial Cells/Total Cells | Epithelial Cells/Total Cells | A relative measurement (ratio or percentage) of the epithelial cells to total cells in a biological specimen. |
| C163434 | Epithelial Stromal Interaction Protein 1 | BRESI1; Epithelial Stromal Interaction Protein 1 | A measurement of the epithelial stromal interaction protein 1 in a biological specimen. |
| C64797 | Ery. Mean Corpuscular Hemoglobin | Ery. Mean Corpuscular Hemoglobin | A measurement of the mean amount of hemoglobin per erythrocyte in a biological specimen, calculated as the product of hemoglobin times ten, divided by the number of erythrocytes. |
| C64798 | Ery. Mean Corpuscular HGB Concentration | Ery. Mean Corpuscular HGB Concentration | An indirect measurement of the average concentration of hemoglobin per erythrocyte in a biological specimen, calculated as the ratio of hemoglobin to hematocrit. |
| C64799 | Ery. Mean Corpuscular Volume | Ery. Mean Corpuscular Volume; Erythrocytes Mean Corpuscular Volume; RBC Mean Corpuscular Volume | A measurement of the mean cellular volume per erythrocyte in a biological specimen. |
| C111197 | Erythrocyte Agglutination | Autoagglutination; Erythrocyte Agglutination; RBC Agglutination | A measurement of the erythrocyte agglutination in a biological specimen. |
| C92245 | Erythrocyte Cell Clumps | Erythrocyte Cell Clumps; RBC Aggregates; RBC Clumps; Red Blood Cell Clumps | A measurement of red blood cell clumps in a biological specimen. |
| C92296 | Erythrocyte Cell Morphology | Erythrocyte Cell Morphology; RBC Morphology; Red Blood Cell Morphology | An examination or assessment of the form and structure of red blood cells. |
| C116212 | Erythrocyte Fragment | Erythrocyte Fragment; RBC Fragment | A measurement of the red blood cell fragments (red cell fragments that have a reticular-like shape with rounded ends and no spicules, differentiating them from schistocytes and acanthocytes) in a biological specimen. |
| C96605 | Erythrocyte Ghosts | Erythrocyte Ghosts; RBC Ghosts | A measurement of the erythrocyte ghosts (erythrocytes in which hemoglobin has been removed through hemolysis) in a biological specimen. |
| C161375 | Erythrocyte Inclusion Bodies | Erythrocyte Inclusion Bodies | A measurement of the erythrocyte inclusion bodies in a biological specimen. |
| C147339 | Erythrocyte Protoporphyrin, Free | Erythrocyte Protoporphyrin, Free | A measurement of the free erythrocyte protoporphyrin (zinc bound plus unbound protoporphyrin) in a biological specimen. |
| C74611 | Erythrocyte Sedimentation Rate | Biernacki Reaction; Erythrocyte Sedimentation Rate | The distance (e.g. millimeters) that red blood cells settle in unclotted blood over a specified unit of time (e.g. one hour). |
| C64800 | Erythrocytes Distribution Width | Erythrocytes Distribution Width; RDW-CV; Red Blood Cell Distribution Width; Red Cell Volume Distribution Width | A relative measurement (ratio or percentage) of the standard deviation of the red blood cell volume to the mean distribution of the red blood cell volume in a biological specimen. |
| C51946 | Erythrocytes | Erythrocytes; Red Blood Cells | A measurement of the total erythrocytes in a biological specimen. |
| C186047 | Erythroferrone | Erythroferrone | A measurement of the erythroferrone in a biological specimen. |
| C154720 | Erythroid Cells/Nucleated Cells | Erythroid Cells/Nucleated Cells | A relative measurement (ratio or percentage) of the erythroid cells to total nucleated cells in a biological specimen. |
| C154719 | Erythroid Cells/Total Cells | Erythroid Cells/Total Cells | A relative measurement (ratio or percentage) of the erythroid cells to total cells in a biological specimen. |
| C135415 | Erythroid Maturation Index | Erythroid Maturation Index | A relative measurement (ratio) of the sum of erythroid maturation phase cells (pool) to the sum of erythroid proliferative phase cells (pool) in a biological specimen. |
| C135416 | Erythroid Maturation Pool | Erythroid Maturation Pool | A measurement of the erythroid maturation phase cells (polychromatic rubricytes, normochromic rubricytes, and metarubricytes) in a biological specimen. |
| C187802 | Erythroid Precursor Cells | Erythroid Precursor Cells; Erythroid Precursors | A measurement of the erythroid precursors in a biological specimen. |
| C187803 | Erythroid Precursor Cells/Total Cells | Erythroid Precursor Cells/Total Cells; Erythroid Precursors/Total Cells | A relative measurement (ratio or percentage) of the erythroid precursors to total cells in a biological specimen. |
| C135417 | Erythroid Proliferation Index | Erythroid Proliferation Index | A relative measurement (ratio) of the sum of erythroid proliferative phase cells (pool) to the sum of erythroid maturation phase cells (pool) in a biological specimen. |
| C135418 | Erythroid Proliferation Pool | Erythroid Proliferation Pool | A measurement of the erythroid proliferative phase cells (rubriblasts, prorubricytes, and basophilic rubricytes) in a biological specimen. |
| C74855 | Erythropoietin | Erythropoietin; Hematopoietin | A measurement of the erythropoietin hormone in a biological specimen. |
| C187804 | Escitalopram | Escitalopram | A measurement of the escitalopram in a biological specimen. |
| C184615 | Estazolam | Estazolam | A measurement of the estazolam in a biological specimen. |
| C74782 | Estradiol | Estradiol; Oestradiol | A measurement of the estradiol in a biological specimen. |
| C150842 | Estradiol, Free | Estradiol, Free | A measurement of the unbound estradiol in a biological specimen. |
| C150843 | Estradiol, Free/Estradiol | Estradiol, Free/Estradiol | A relative measurement (ratio or percentage) of unbound estradiol to total estradiol in a biological specimen. |
| C74856 | Estriol | Estriol; Oestriol | A measurement of the estriol hormone in a biological specimen. |
| C81963 | Estriol, Free | Estriol, Free; Unconjugated Estriol | A measurement of the free estriol in a biological specimen. |
| C112274 | Estrogen Receptor | ER; ESR; Estrogen Receptor; Oestrogen Receptor | A measurement of estrogen receptor protein in a biological specimen. |
| C147335 | Estrogen | Estrogen; Oestrogen | A measurement of the estrogen hormone in a biological specimen. |
| C163431 | Estrone Sulfate | E1S; Estrone 3-Sulfate; Estrone Sulfate | A measurement of the estrone sulfate in a biological specimen. |
| C74857 | Estrone | Estrone; Oestrone | A measurement of the estrone hormone in a biological specimen. |
| C74693 | Ethanol | Alcohol; Ethanol | A measurement of the ethanol present in a biological specimen. |
| C184616 | Ethchlorvynol | Ethchlorvynol | A measurement of the ethchlorvynol in a biological specimen. |
| C184617 | Ethinamate | Ethinamate | A measurement of the ethinamate in a biological specimen. |
| C170583 | Ethyl Glucuronide Ethyl Sulfate | Ethyl Glucuronide Ethyl Sulfate | A measurement of the ethyl glucuronide and/or ethyl sulfate in a biological specimen. |
| C170584 | Ethyl Glucuronide | Ethyl Glucuronide | A measurement of the ethyl glucuronide in a biological specimen. |
| C170585 | Ethyl Sulfate | Ethyl Sulfate | A measurement of the ethyl sulfate in a biological specimen. |
| C184555 | Ethylamphetamine | Ethylamphetamine; Etilamfetamine; N-Ethylamphetamine | A measurement of the ethylamphetamine in a biological specimen. |
| C184584 | Ethylestrenol | Ethylestrenol | A measurement of the ethylestrenol in a biological specimen. |
| C184570 | Ethylmorphine | Ethylmorphine | A measurement of the ethylmorphine in a biological specimen. |
| C102263 | ETP Area Under Curve | Endogenous Thrombin Potential Area Under Curve; ETP Area Under Curve | A measurement of the area under the thrombin generation curve. |
| C102265 | ETP Lag Time Relative | Endogenous Thrombin Potential Lag Time Relative; ETP Lag Time Relative | A relative measurement (ratio or percentage) of time from the start of the thrombin generation test to the point where a predetermined amount of thrombin is generated. |
| C102264 | ETP Lag Time | Endogenous Thrombin Potential Lag Time; ETP Lag Time | A measurement of time from the start of the thrombin generation test to the point where a predetermined amount of thrombin is generated. |
| C102268 | ETP Peak Height Relative | Endogenous Thrombin Potential Peak Height Relative; ETP Peak Height Relative | A relative (ratio or percentage) of the maximum concentration of thrombin generated during a thrombin generation test. |
| C102267 | ETP Peak Height | Endogenous Thrombin Potential Peak Height; ETP Peak Height | A measurement of the maximum concentration of thrombin generated during a thrombin generation test. |
| C102270 | ETP Time to Peak Relative | Endogenous Thrombin Potential Time to Peak Relative; ETP Time to Peak Relative | A relative (ratio or percentage) measurement of the time it takes to generate the maximum concentration of thrombin. |
| C102269 | ETP Time to Peak | Endogenous Thrombin Potential Time to Peak; ETP Time to Peak | A measurement of the time it takes to generate the maximum concentration of thrombin. |
| C82011 | Extracell Newly Ident RAGE Bind Protein | Extracell Newly Ident RAGE Bind Protein; S100 Calcium Binding Protein A12 | A measurement of the extracellular newly identified RAGE (receptor for advanced glycation end products) binding protein in a biological specimen. |
| C92270 | Extractable Nuclear Antigen Antibody | Anti-ENA; Extractable Nuclear Antigen Antibody | A measurement of the extractable nuclear antigen antibody in a biological specimen. |
| C184640 | Ezogabine | Ezogabine | A measurement of the ezogabine in a biological specimen. |
| C80180 | F2-Isoprostane | F2-Isoprostane | A measurement of the F2-isoprostane in a biological specimen. |
| C96626 | Factor II | Factor II; Prothrombin | A measurement of the coagulation factor II in a biological specimen. |
| C81959 | Factor III | Factor III; Tissue Factor, CD142 | A measurement of the coagulation factor III in a biological specimen. |
| C170588 | Factor IX Activity Actual/Control | Factor IX Activity Actual/Control; Factor IX Activity Actual/Factor IX Activity Control; Factor IX Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of factor IX dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C103395 | Factor IX Activity | Christmas Factor Activity; Factor IX Activity | A measurement of the biological activity of coagulation factor IX in a biological specimen. |
| C98725 | Factor IX | Christmas Factor; Factor IX | A measurement of the coagulation factor IX in a biological specimen. |
| C170587 | Factor V Activity Actual/Control | Factor V Activity Actual/Control; Factor V Activity Actual/Factor V Activity Control; Factor V Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of factor V dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C103396 | Factor V Activity | Factor V Activity; Labile Factor Activity | A measurement of the biological activity of coagulation factor V in a biological specimen. |
| C102271 | Factor V Leiden | Factor V Leiden | A measurement of the coagulation factor V Leiden in a biological specimen. |
| C98726 | Factor V | Factor V; Labile Factor | A measurement of the coagulation factor V in a biological specimen. |
| C170589 | Factor VII Activity Actual/Control | Factor VII Activity Actual/Control; Factor VII Activity Actual/Factor VII Activity Control; Factor VII Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of factor VII dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C103397 | Factor VII Activity | Factor VII Activity; Proconvertin Activity; Stable Factor Activity | A measurement of the biological activity of coagulation factor VII in a biological specimen. |
| C81960 | Factor VII | Factor VII; Proconvertin; Stable Factor | A measurement of the coagulation factor VII in a biological specimen. |
| C103398 | Factor VIIa Activity | Factor VIIa Activity | A measurement of the biological activity of coagulation factor VIIa in a biological specimen. |
| C147345 | Factor VIII Activity Actual/Control | Factor VIII Activity Actual/Control; Factor VIII Activity Actual/Factor VIII Activity Control; Factor VIII Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of factor VIII dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C103399 | Factor VIII Activity | Anti-hemophilic Factor Activity; Factor VIII Activity; Factor VIII:C | A measurement of the biological activity of coagulation factor VIII in a biological specimen. |
| C154752 | Factor VIII Inhibitor | Factor VIII Inhibitor | A measurement of the factor VIII Inhibitor in a biological specimen. |
| C81961 | Factor VIII | Anti-hemophilic Factor; Factor VIII | A measurement of the coagulation factor VIII in a biological specimen. |
| C170586 | Factor X Activity Actual/Control | Factor X Activity Actual/Control; Factor X Activity Actual/Factor X Activity Control; Factor X Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of factor X dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C122118 | Factor X Activity | Factor X Activity | A measurement of the biological activity of coagulation factor X in a biological specimen. |
| C170590 | Factor X Actual/Control | Factor X Actual/Control; Factor X Actual/Normal | A relative measurement (ratio or percentage) of the factor X in a subject's specimen when compared to a control specimen. |
| C98727 | Factor X | Factor X | A measurement of the coagulation factor X in a biological specimen. |
| C163436 | Factor XI Activity | Factor XI Activity | A measurement of the biological activity of coagulation factor XI in a biological specimen. |
| C163435 | Factor XI | Factor XI | A measurement of the factor XI in a biological specimen. |
| C163438 | Factor XII Activity | Factor XII Activity | A measurement of the biological activity of coagulation factor XII in a biological specimen. |
| C163437 | Factor XII | Factor XII | A measurement of the factor XII in a biological specimen. |
| C174313 | Factor XIII Activity | Factor XIII Activity | A measurement of the biological activity of coagulation factor XIII in a biological specimen. |
| C112277 | Factor XIII | Factor XIII; Fibrin Stabilizing Factor | A measurement of the coagulation factor XIII in a biological specimen. |
| C147346 | Factor XIV Activity Actual/Control | Factor XIV Activity Actual/Control; Factor XIV Activity Actual/Factor XIV Activity Control; Factor XIV Activity Actual/Normal | A relative measurement (ratio or percentage) of the biological activity of factor XIV dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C105442 | Factor XIV Activity | Factor XIV Activity; Protein C Activity; Protein C Function | A measurement of the biological activity of coagulation factor XIV in a biological specimen. |
| C170594 | Factor XIV Actual/Control | Factor XIV Actual/Control; Protein C Actual/Control | A relative measurement (ratio or percentage) of the factor XIV in a subject's specimen when compared to a control specimen. |
| C102272 | Factor XIV | Autoprothrombin IIA; Factor XIV; Protein C; Protein C Antigen | A measurement of the coagulation factor XIV in a biological specimen. |
| C165960 | Fas Cell Surface Death Receptor | ALPS1A; APT1; CD95; Fas Cell Surface Death Receptor; FAS1; FASTM; TNF Receptor Superfamily Member 6; TNFRSF6 | A measurement of the Fas cell surface death receptor in a biological specimen. |
| C81947 | Fat Bodies, Oval | Fat Bodies, Oval | A measurement of the oval-shaped fat bodies, usually renal proximal tubular cells with lipid aggregates in the cytoplasm, in a biological specimen. |
| C98728 | Fat Droplet | Fat Droplet | A measurement of the triglyceride aggregates within a biological specimen. |
| C96648 | Fat | Fat | A measurement of the fat in a biological specimen. |
| C187806 | Fat/Total Solids | Fat/Total Solids | A relative measurement (ratio or percentage) of the fat to total solid material in a biological specimen (for example a stool specimen). |
| C82012 | Fatty Acid Binding Protein 1 | FABP1; Fatty Acid Binding Protein 1; L-FABP; L-Type Fatty Acid-Binding Protein; Liver Fatty Acid-Binding Protein | A measurement of the fatty acid binding protein 1 in a biological specimen. |
| C106521 | Fatty Acid Binding Protein 3 | Fatty Acid Binding Protein 3 | A measurement of the fatty acid binding protein 3 in a biological specimen. |
| C147337 | Fatty Acids, Very Long Chain | Fatty Acids, Very Long Chain | A measurement of the very long chain fatty acids (containing 22 or more carbon atoms) in a biological specimen. |
| C74766 | Fatty Casts | Fatty Casts | A measurement of the fatty casts present in a biological specimen. |
| C156516 | Fatty Liver Index | Fatty Liver Index; FLI | A calculation that indicates the likely presence of fatty liver disease, taking into account waist circumference, body mass index, triglyceride concentrations, and gamma-glutamyltransferase activity. (Bedogni G, Bellentani S, Miglioli L, Masutti F, Passalacqua M, Castiglione A, Tiribelli C. The Fatty Liver Index: a simple and accurate predictor of hepatic steatosis in the general population. BMC Gastroenterol. 2006 Nov 2;6:33.) |
| C184618 | Fencamfamin | Fencamfamin; Fencamfamine | A measurement of the fencamfamin in a biological specimen. |
| C184619 | Fenfluramine | Fenfluramine | A measurement of the fenfluramine in a biological specimen. |
| C184620 | Fenproporex | Fenproporex | A measurement of the fenproporex in a biological specimen. |
| C147338 | Fentanyl | Fentanyl | A measurement of the fentanyl in a biological specimen. |
| C172521 | Ferritin Heavy Chain | Apoferritin; Ferritin Heavy Chain; FTH; FTH1 | A measurement of the ferritin heavy chain in a biological specimen. |
| C172522 | Ferritin Light Chain | Ferritin Light Chain; FTL; L Apoferritin | A measurement of the ferritin light chain in a biological specimen. |
| C74737 | Ferritin | Ferritin | A measurement of the ferritin in a biological specimen. |
| C82013 | Fibrin Degradation Products | Fibrin Degradation Products | A measurement of the fibrin degradation products in a biological specimen. |
| C189498 | Fibrin Monomer | Fibrin Monomer; Soluble Fibrin Monomer | A measurement of the fibrin monomer in a biological specimen. |
| C64606 | Fibrinogen | Fibrinogen; Fibrinogen Antigen | A measurement of the total fibrinogen (functional and non-functional) in a biological specimen. |
| C139075 | Fibrinogen, Functional | Fibrinogen, Functional | A measurement of the functional fibrinogen (fibrinogen that is capable of being converted to fibrin) in a biological specimen. |
| C154727 | Fibroblast Growth Factor 19 | FGF 19; Fibroblast Growth Factor 19 | A measurement of the fibroblast growth factor 19 in a biological specimen. |
| C112280 | Fibroblast Growth Factor 21 | FGF 21; Fibroblast Growth Factor 21 | A measurement of the fibroblast growth factor 21 in a biological specimen. |
| C96650 | Fibroblast Growth Factor 23 | Fibroblast Growth Factor 23; Phosphatonin | A measurement of the total fibroblast growth factor 23 in a biological specimen. |
| C135419 | Fibroblast Growth Factor 23, C-Terminal | Fibroblast Growth Factor 23, C-Terminal | A measurement of the C-terminal fibroblast growth factor 23 in a biological specimen. |
| C135420 | Fibroblast Growth Factor 23, Intact | Fibroblast Growth Factor 23, Intact | A measurement of the intact fibroblast growth factor 23 in a biological specimen. |
| C130162 | Fibroblast Growth Factor 9 | FGF 9; Fibroblast Growth Factor 9 | A measurement of the fibroblast growth factor 9 in a biological specimen. |
| C82014 | Fibroblast Growth Factor Basic Form | FGF2; Fibroblast Growth Factor Basic Form | A measurement of the basic form of fibroblast growth factor in a biological specimen. |
| C172507 | Fibronectin, Cellular | Fibronectin, Cellular; Insoluble Fibronectin | A measurement of the cellular fibronectin in a biological specimen. |
| C92786 | Fibronectin, Fetal | Fibronectin, Fetal | A measurement of the fetal isoform of fibronectin in a biological specimen |
| C177951 | Fibronectin, Maternal + Fetal | Fibronectin, Maternal + Fetal | A measurement of the maternal plasma fibronectin and fetal fibronectin in a biological specimen. |
| C172508 | Fibronectin, Plasma | Fibronectin, Plasma; Soluble Fibronectin | A measurement of the plasma fibronectin in a biological specimen. |
| C105443 | FibroTest Score | FibroSURE Score; FibroTest Score | A biomarker test that measures liver pathology through the assessment of a six-parameter blood test (for Alpha-2-macroglobulin, Haptoglobin, Apolipoprotein A1, Gamma-glutamyl transpeptidase (GGT), Total bilirubin, and Alanine aminotransferase (ALT)), taking into account the age and gender of the patient. |
| C171455 | Fluid Output | Fluid Output | A measurement of the total volume of fluid discharged over a set period of time. |
| C171508 | Fluid Output, Estimated | Fluid Output, Estimated | An estimate of the total volume of fluid discharged over a set period of time. |
| C186048 | Flunitrazepam and/or Metabolites | Flunitrazepam and/or Metabolites | A measurement of the flunitrazepam and/or its metabolite(s) present in a biological specimen, for an assay that can measure both flunitrazepam and its metabolites. |
| C139081 | Flunitrazepam | Flunitrazepam | A measurement of the flunitrazepam present in a biological specimen. |
| C122120 | Fluoride | Fluoride | A measurement of the fluoride in a biological specimen. |
| C158219 | Fluoxetine | Fluoxetine | A measurement of the fluoxetine drug present in a biological specimen. |
| C184585 | Fluoxymesterone | Fluoxymesterone | A measurement of the fluoxymesterone in a biological specimen. |
| C177980 | Fluphenazine | Fluphenazine | A measurement of the fluphenazine in a biological specimen. |
| C186051 | Flurazepam and/or Metabolites | Flurazepam and/or Metabolites | A measurement of the flurazepam and/or its metabolite(s) present in a biological specimen, for an assay that can measure both flurazepam and its metabolites. |
| C75373 | Flurazepam | Flurazepam | A measurement of the flurazepam present in a biological specimen. |
| C147340 | Fluvoxamine | Fluvoxamine | A measurement of the fluvoxamine present in a biological specimen. |
| C174307 | FMS-like Receptor Tyrosine Kinase 3 | CD135; FMS-like Receptor Tyrosine Kinase 3 | A measurement of the FMS-like receptor tyrosine kinase 3 in a biological specimen. |
| C174306 | FMS-like Tyrosine Kinase 3 Ligand | FMS-like Tyrosine Kinase 3 Ligand | A measurement of the FMS-like tyrosine kinase 3 ligand in a biological specimen. |
| C132367 | Folate Hydrolase mRNA | Folate Hydrolase mRNA | A measurement of the folate hydrolase mRNA in a biological specimen. |
| C74783 | Follicle Stimulating Hormone | Follicle Stimulating Hormone | A measurement of the follicle stimulating hormone (FSH) in a biological specimen. |
| C38082 | Fraction of Inspired Oxygen | Fraction of Inspired Oxygen | A measurement of the volumetric fraction of oxygen in the inhaled gas. |
| C114219 | Fractional Calcium Excretion | Fractional Calcium Excretion | A measurement of the fractional excretion of calcium that is computed based upon the concentrations of calcium and creatinine in both blood and urine. |
| C114220 | Fractional Chloride Excretion | Fractional Chloride Excretion | A measurement of the fractional excretion of chloride that is computed based upon the concentrations of chloride and creatinine in both blood and urine. |
| C161349 | Fractional Iron Absorption | Fractional Iron Absorption | A relative measurement (ratio or percentage) of the iron absorbed into tissue or cells to the total available iron. |
| C122119 | Fractional Magnesium Excretion | Fractional Magnesium Excretion | A measurement of the fractional excretion of magnesium that is computed based upon the concentrations of magnesium and creatinine in both blood and urine. |
| C114221 | Fractional Phosphorus Excretion | Fractional Inorganic Phosphate Excretion; Fractional Phosphorus Excretion | A measurement of the fractional excretion of phosphorus that is computed based upon the concentrations of phosphorus and creatinine in both blood and urine. |
| C114222 | Fractional Potassium Excretion | Fractional Potassium Excretion | A measurement of the fractional excretion of potassium that is computed based upon the concentrations of potassium and creatinine in both blood and urine. |
| C107435 | Fractional Sodium Excretion | Fractional Sodium Excretion | A measurement of the fractional excretion of sodium that is computed based upon the concentrations of sodium and creatinine in both blood and urine. |
| C124341 | Free Androgen Index | Free Androgen Index | A measurement of the androgen status in a biological specimen. This is calculated by a mathematical formula that takes into account the total testosterone level, sex hormone binding globulin, and a constant. |
| C80200 | Free Fatty Acid | Free Fatty Acid; Non-Esterified Fatty Acid, Free | A measurement of the total non-esterified fatty acids in a biological specimen. |
| C80206 | Free Fatty Acid, Saturated | Free Fatty Acid, Saturated; Non-esterified Fatty Acid, Saturated | A measurement of the saturated non-esterified fatty acids in a biological specimen. |
| C80209 | Free Fatty Acid, Unsaturated | Free Fatty Acid, Unsaturated; Non-esterified Fatty Acid, Unsaturated | A measurement of the unsaturated non-esterified fatty acids in a biological specimen. |
| C100448 | Free Glycerol | Free Glycerin; Free Glycerol | A measurement of the amount of unbound glycerol in a biological specimen. |
| C161350 | Fructosamine Corrected for Total Protein | Fructosamine Corrected for Total Protein | A measurement of fructosamine, which has been corrected for total protein, in a biological specimen. |
| C74678 | Fructosamine | Fructosamine; Glycated Serum Protein | A measurement of the fructosamine in a biological specimen. |
| C147342 | Fructose | Fructose | A measurement of the fructose in a biological specimen. |
| C154813 | Fungi | Fungi; Fungus | A measurement of the fungi in a biological specimen. |
| C147343 | Fungi, Filamentous | Fungi, Filamentous | A measurement of the filamentous fungi in a biological specimen. |
| C147344 | Fungi, Yeast-Like | Fungi, Yeast-Like | A measurement of the yeast-like fungi in a biological specimen. |
| C184541 | Furanylfentanyl | Furanyl Fentanyl; Furanylfentanyl | A measurement of the furanylfentanyl in a biological specimen. |
| C184586 | Furazabol | Furazabol | A measurement of the furazabol in a biological specimen. |
| C132368 | G6PD-Deficient Erythrocytes | G6PD-Deficient Erythrocytes | A measurement of the glucose-6-phosphate dehydrogenase deficient erythrocytes in a biological specimen. |
| C132369 | G6PD-Deficient Erythrocytes/Erythrocytes | G6PD-Deficient Erythrocytes/Erythrocytes | A relative measurement (ratio or percentage) of G6PD-deficient erythrocytes to total erythrocytes in a biological specimen. |
| C124342 | Galactose Elimination Capacity | Galactose Elimination Capacity | A liver function test that measures galactose elimination capacity in a biological specimen. |
| C163439 | Galactose Mutarotase | Galactose Mutarotase | A measurement of the galactose mutarotase in a biological specimen. |
| C81308 | Galactose | Galactose | A measurement of the galactose in a biological specimen. |
| C81251 | Galactose-1-Phos Uridylyltransferase | G1PUT; Galactose 1 Phosphate Uridyl Transferase; Galactose-1-Phos Uridylyltransferase; Galactose-1-Phosphate Uridylyltransferase; GALT | A measurement of the galactose-1-phosphate uridyltransferase in a biological specimen. |
| C186052 | Galactose-1-Phosphate | Galactose-1-Phosphate | A measurement of the galactose-1-phosphate in a biological specimen. |
| C165961 | Galactose-Deficient IgA1 | Galactose-Deficient IgA1; Gd-IgA1 | A measurement of the galactose-deficient IgA1 in a biological specimen. |
| C80182 | Galanin | Galanin | A measurement of the galanin in a biological specimen. |
| C186053 | Galectin-3 Binding Protein | Galectin-3 Binding Protein; LGALS3BP; M2BP; Mac-2 Binding Protein | A measurement of the galectin-3 binding protein in a biological specimen. |
| C172493 | Galectin-3 | Galactose-Specific Lectin 3; Galectin-3; GALIG; MAC-2 | A measurement of the galectin-3 in a biological specimen. |
| C92257 | Gamma Globulin | Gamma Globulin | A measurement of the proteins contributing to the gamma fraction in a biological specimen. |
| C92295 | Gamma Globulin/Total Protein | Gamma Globulin/Total Protein | A relative measurement (ratio or percentage) of gamma fraction proteins to total proteins in a biological specimen. |
| C64847 | Gamma Glutamyl Transferase | Gamma Glutamyl Transferase | A measurement of the gamma glutamyl transferase in a biological specimen. |
| C79446 | Gamma Glutamyl Transferase/Creatinine | Gamma Glutamyl Transferase/Creatinine | A relative measurement (ratio or percentage) of the gamma glutamyl transferase to creatinine in a biological specimen. |
| C116211 | Gamma Tocopherol | Gamma Tocopherol | A measurement of the gamma tocopherol in a biological specimen. |
| C154766 | Gamma-Aminobutyric Acid | GABA; Gamma-aminobutyrate; Gamma-Aminobutyric Acid | A measurement of the gamma-aminobutyric acid in a biological specimen. |
| C75357 | Gamma-Hydroxybutyrate | 4-Hydroxybutanoic Acid; Gamma-Hydroxybutyrate; Gamma-Hydroxybutyric Acid | A measurement of the gamma-hydroxybutyrate in a biological specimen. |
| C165962 | GammaGlutamyl Transferase Excretion Rate | Gamma Glutamyl Transferase Excretion Rate | A measurement of the amount of gamma glutamyl transferase being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C184516 | Ganglioside GM3 | Ganglioside GM3; Monosialodihexosylganglioside | A measurement of the ganglioside GM3 in a biological specimen. |
| C74858 | Gastrin | Gastrin | A measurement of the gastrin hormone in a biological specimen. |
| C130141 | German Cockroach Antigen IgA Antibody | German Cockroach Antigen IgA Antibody | A measurement of the Blattella germanica antigen IgA antibody in a biological specimen. |
| C130140 | German Cockroach Antigen IgE Antibody | German Cockroach Antigen IgE Antibody | A measurement of the Blattella germanica antigen IgE antibody in a biological specimen. |
| C130142 | German Cockroach Antigen IgG Antibody | German Cockroach Antigen IgG Antibody | A measurement of the Blattella germanica antigen IgG antibody in a biological specimen. |
| C130143 | German Cockroach Antigen IgG4 Antibody | German Cockroach Antigen IgG4 Antibody | A measurement of the Blattella germanica antigen IgG4 antibody in a biological specimen. |
| C165878 | German Cockroach IgE AB RAST Score | German Cockroach IgE AB RAST Score | A classification of the amount of Blattella germanica antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165919 | German Cockroach IgG AB RAST Score | German Cockroach IgG AB RAST Score | A classification of the amount of Blattella germanica antigen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C100450 | GFR from B-2 Microglobulin Adj for BSA | GFR from B-2 Microglobulin Adj for BSA | A measurement of the glomerular filtration rate (GFR) based on the clearance of beta-2 microglobulin after adjusting it for the body surface area. |
| C100449 | GFR from Beta-Trace Protein Adj for BSA | GFR from Beta-Trace Protein Adj for BSA | A measurement of the glomerular filtration rate (GFR) based on the clearance of beta-trace protein after adjusting it for the body surface area. |
| C163442 | GFR from Creat and UreaN Adj BSA | GFR from Creat and UreaN Adj BSA; GFR from Creatinine and Urea Nitrogen Adjusted for BSA | An estimation of the glomerular filtration rate adjusted for body surface area based on creatinine and urea nitrogen. |
| C163443 | GFR from Creat,UreaN,Alb Adj BSA | GFR from Creat,UreaN,Alb Adj BSA; GFR from Creatinine, Urea Nitrogen and Albumin Adjusted for BSA | An estimation of the glomerular filtration rate adjusted for body surface area based on creatinine, urea nitrogen, and albumin. |
| C98735 | GFR from Creatinine Adjusted for BSA | GFR from Creatinine Adjusted for BSA | An estimation of the glomerular filtration rate adjusted for body surface area based on creatinine. |
| C98736 | GFR from Cystatin C Adjusted for BSA | GFR from Cystatin C Adjusted for BSA | An estimation of the glomerular filtration rate adjusted for body surface area based on cystatin C. |
| C127614 | GFR from Cystatin C and Creat Adj BSA | GFR from Cystatin C and Creat Adj BSA | An estimation of the glomerular filtration rate adjusted for body surface area based on cystatin C and creatinine. |
| C112286 | Ghrelin | Ghrelin; Growth Hormone Secretagogue Receptor Ligand; Motilin-related Peptide; Total Ghrelin | A measurement of total ghrelin in a biological specimen. |
| C96651 | Giant Neutrophils | Giant Neutrophils | A measurement of the giant neutrophils in a biological specimen. |
| C74728 | Giant Platelets | Giant Platelets | A measurement of the giant (larger than 7um in diameter) platelets in a biological specimen. |
| C147347 | Gliadin Antibody | Gliadin Antibody | A measurement of the total gliadin antibodies in a biological specimen. |
| C147348 | Gliadin IgA Antibody | Gliadin IgA Antibody | A measurement of the gliadin IgA antibody in a biological specimen. |
| C147349 | Gliadin IgG Antibody | Gliadin IgG Antibody | A measurement of the gliadin IgG antibody in a biological specimen. |
| C189528 | Glial Fibrillary Acidic Protein | Glial Fibrillary Acidic Protein | A measurement of the glial fibrillary acidic protein in a biological specimen. |
| C150844 | Glitter Cells | Glitter Cells | A measurement of the glitter cells in a biological specimen. |
| C74738 | Globulin | Globulin | A measurement of the globulin protein in a biological specimen. |
| C142276 | Globulin/Creatinine | Globulin/Creatinine | A relative measurement (ratio or percentage) of the globulin to creatinine in a biological specimen. |
| C98734 | Glomerular Filtration Rate Adj for BSA | Glomerular Filtration Rate Adj for BSA | A measurement of the glomerular filtration rate adjusted for body surface area. |
| C90505 | Glomerular Filtration Rate | Glomerular Filtration Rate | A kidney function test that measures the fluid volume that is filtered from the kidney glomeruli to the Bowman's capsule per unit of time. |
| C110935 | Glomerular Filtration Rate, Estimated | Glomerular Filtration Rate, Estimated | A kidney function test that estimates the fluid volume that is filtered from the kidney glomeruli to the Bowman's capsule per unit of time. |
| C74859 | Glucagon | Glucagon | A measurement of the glucagon hormone in a biological specimen. |
| C80183 | Glucagon-Like Peptide-1 | Glucagon-Like Peptide-1; Total Glucagon-Like Peptide-1 | A measurement of the total glucagon-like peptide-1 in a biological specimen. |
| C80164 | Glucagon-Like Peptide-1, Active Form | Glucagon-Like Peptide-1, Active Form | A measurement of the active form of glucagon-like peptide-1 in a biological specimen. |
| C154768 | Glucagon-Like Peptide-1, Inactive Form | Glucagon-Like Peptide-1, Inactive Form | A measurement of the inactive form of glucagon-like peptide-1 in a biological specimen. |
| C184523 | Glucopsychosine | Glucopsychosine; Glucosylsphingosine; Lyso-GL1 | A measurement of the glucopsychosine in a biological specimen. |
| C96652 | Glucose Clearance | Glucose Clearance | A measurement of the volume of serum or plasma that would be cleared of glucose by excretion of urine for a specified unit of time (e.g. one minute). |
| C150818 | Glucose Excretion Rate | Glucose Excretion Rate | A measurement of the amount of glucose being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C174310 | Glucose Management Indicator | Glucose Management Indicator | An approximate measure (expressed as a % or mmol/mol) of an individual's expected hemoglobin A1c/hemoglobin level, based on the mean glucose measured over a period of at least 10 days by continuous glucose monitoring. |
| C105585 | Glucose | Glucose | A measurement of the glucose in a biological specimen. |
| C142275 | Glucose, Estimated Average | EAG; Estimated Average Glucose; Glucose, Estimated; Glucose, Estimated Average | A computed estimate of the blood glucose based on the value of the glycated hemoglobin |
| C186054 | Glucose, Radiolabeled/Glucose | Glucose, Enriched/Glucose; Glucose, Radiolabeled/Glucose | A relative measurement (ratio or percentage) of radiolabeled glucose to total glucose in a biological specimen. |
| C139065 | Glucose-6-Phosphate Dehydrogenase Act | Glucose-6-Phosphate Dehydrogenase Act | A measurement of the biological activity of glucose-6-phosphate dehydrogenase in a biological specimen. |
| C80184 | Glucose-6-Phosphate Dehydrogenase | Glucose-6-Phosphate Dehydrogenase | A measurement of the glucose-6-phosphate dehydrogenase in a biological specimen. |
| C106537 | Glucose-dep Insulinotropic Pep, Intact | Glucose-dep Insulinotropic Pep, Intact; Intact Gastric Inhibitory Polypeptide; Intact GIP; Intact Glucose-dependent Insulinotropic Peptide | A measurement of the intact (containing amino acids 1-42) glucose-dependent insulinotropic peptide in a biological specimen. |
| C79447 | Glucose/Creatinine | Glucose/Creatinine | A relative measurement (ratio or percentage) of the glucose to creatinine in a biological specimen. |
| C184520 | Glucosylceramidase Beta | Beta-Glucocerebrosidase; GBA; Glucocerebrosidase Beta; Glucosylceramidase; Glucosylceramidase Beta | A measurement of the glucosylceramidase beta in a biological specimen. |
| C184522 | Glucosylceramide | GL1; Glucocerebroside; Glucosylceramide | A measurement of the glucosylceramide in a biological specimen. |
| C80165 | Glucuronidase, Alpha | Glucuronidase, Alpha | A measurement of the alpha glucuronidase in a biological specimen. |
| C80170 | Glucuronidase, Beta | Glucuronidase, Beta | A measurement of the beta glucuronidase in a biological specimen. |
| C79448 | Glutamate Dehydrogenase | Glutamate Dehydrogenase | A measurement of the glutamate dehydrogenase in a biological specimen. |
| C74739 | Glutamate | Glutamate; Glutamic Acid | A measurement of the glutamate in a biological specimen. |
| C82015 | Glutamic Acid Decarboxylase 1 | Glutamic Acid Decarboxylase 1; Glutamic Acid Decarboxylase 67 | A measurement of the glutamic acid decarboxylase 1 in a biological specimen. |
| C82017 | Glutamic Acid Decarboxylase 2 Antibody | Glutamic Acid Decarboxylase 2 Antibody; Glutamic Acid Decarboxylase 65 Antibody | A measurement of the glutamic acid decarboxylase 2 antibody in a biological specimen. |
| C82016 | Glutamic Acid Decarboxylase 2 | Glutamic Acid Decarboxylase 2; Glutamic Acid Decarboxylase 65 | A measurement of the glutamic acid decarboxylase 2 in a biological specimen. |
| C96653 | Glutamic Acid Decarboxylase Antibody | GAD Antibody; Glutamic Acid Decarboxylase Antibody | A measurement of the glutamic acid decarboxylase antibody in a biological specimen. |
| C122121 | Glutamine | Glutamine | A measurement of the glutamine in a biological specimen. |
| C80166 | Glutathione S-Transferase, Alpha/Creat | Glutathione S-Transferase, Alpha/Creat | A relative measurement (ratio or percentage) of the alpha glutathione-S-transferase to creatinine in a biological specimen. |
| C80203 | Glutathione S-Transferase, Pi | Glutathione S-Transferase, Pi | A measurement of the Pi glutathione-s-transferase in a biological specimen. |
| C80207 | Glutathione S-Transferase, Theta | Glutathione S-Transferase, Theta | A measurement of the theta glutathione-s-transferase in a biological specimen. |
| C80185 | Glutathione S-Transferase, Total | Glutathione S-Transferase, Total | A measurement of the total glutathione-s-transferase in a biological specimen. |
| C163449 | Glutathione S-Transferase, Y1 | Glutathione S-Transferase, Y1 | A measurement of the Y1 subunit of glutathione-s-transferase in a biological specimen. |
| C79435 | Glutathione-S-Transferase/Creatinine | Glutathione-S-Transferase/Creatinine | A relative measurement (ratio or percentage) of the glutathione S-transferase to creatinine in a biological specimen. |
| C184571 | Glutethimide | Glutethimide | A measurement of the glutethimide in a biological specimen. |
| C122092 | Glycated Albumin | Glycated Albumin | A measurement of the glycated albumin present in a biological specimen. |
| C158228 | Glycated Albumin/Albumin | Glycated Albumin/Albumin; Glycosylated Albumin/Albumin | A relative measurement (ratio or percentage) of the glycated albumin to total albumin in a biological specimen. |
| C186049 | Glycated Ferritin | Glycated Ferritin | A measurement of the glycated ferritin in a biological specimen. |
| C186050 | Glycated Ferritin/Ferritin | Glycated Ferritin/Ferritin | A relative measurement (ratio or percentage) of the glycated ferritin to total ferritin in a biological specimen. |
| C184524 | Glyceraldehyde-3-Phosphate Dehydrogenase | GAPDH; Glyceraldehyde 3 Phosphate Dehydrogenase; Glyceraldehyde-3-Phosphate Dehydrogenase | A measurement of the glyceraldehyde-3-phosphate dehydrogenase in a biological specimen. |
| C132371 | Glycerol | Glycerol | A measurement of the total glycerol in a biological specimen. |
| C147278 | Glycine max Antigen IgE Antibody | Glycine max Antigen IgE Antibody; Soybean Antigen IgE Antibody | A measurement of the Glycine max antigen IgE antibody in a biological specimen. |
| C165936 | Glycine max IgE AB RAST Score | Glycine max IgE AB RAST Score | A classification of the amount of Glycine max antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C122122 | Glycine | Glycine | A measurement of the glycine in a biological specimen. |
| C158221 | Glycine/Creatinine | Glycine/Creatinine | A relative measurement (ratio) of the glycine to the creatinine in a biological specimen. |
| C176305 | Glycochenodeoxycholate | Glycochenodeoxycholate; Glycochenodeoxycholic Acid | A measurement of the glycochenodeoxycholate in a biological specimen. |
| C176299 | Glycocholate | Cholylglycine; Glycocholate; Glycocholic Acid | A measurement of the glycocholate in a biological specimen. |
| C176308 | Glycolithocholate | Glycolithocholate; Glycolithocholic Acid | A measurement of the glycolithocholate in a biological specimen. |
| C176302 | Glycoursodeoxycholate | Glycoursodeoxycholate; Glycoursodeoxycholic Acid | A measurement of the glycoursodeoxycholate in a biological specimen. |
| C187807 | Glycylproline Dipeptidyl Aminopeptidase | Glycylproline Dipeptidyl Aminopeptidase; GPDA | A measurement of the glycylproline dipeptidyl aminopeptidase in a biological specimen. |
| C80186 | Gold | Gold | A measurement of the gold in a biological specimen. |
| C74860 | Gonadotropin Releasing Hormone | Gonadotropin Releasing Hormone; Luteinising Hormone Releasing Hormone | A measurement of the gonadotropin releasing hormone in a biological specimen. |
| C74768 | Granular Casts | Granular Casts | A measurement of the granular (coarse and fine) casts present in a biological specimen. |
| C74765 | Granular Coarse Casts | Granular Coarse Casts | A measurement of the coarse granular casts present in a biological specimen. |
| C74769 | Granular Fine Casts | Granular Fine Casts | A measurement of the fine granular casts present in a biological specimen. |
| C165963 | Granulin | Granulin | A measurement of the granulin in a biological specimen. |
| C82018 | Granulocyte Colony Stimulating Factor | Granulocyte Colony Stimulating Factor | A measurement of the granulocyte colony stimulating factor in a biological specimen. |
| C82019 | Granulocyte Macrophage Colony Stm Factor | Granulocyte Macrophage Colony Stm Factor | A measurement of the granulocyte macrophage colony stimulating factor in a biological specimen. |
| C186055 | Granulocytes Band Form | Banded Granulocytes; Granulocytes Band Form | A measurement of the banded granulocytes in a biological specimen. |
| C127615 | Granulocytes Band Form/Total Cells | Granulocytes Band Form/Total Cells | A relative measurement (ratio or percentage) of the banded granulocytes to total cells in a biological specimen. |
| C186056 | Granulocytes Segmented | Granulocytes Segmented | A measurement of the segmented granulocytes in a biological specimen. |
| C127616 | Granulocytes Segmented/Total Cells | Granulocytes Segmented/Total Cells | A relative measurement (ratio or percentage) of the segmented granulocytes to total cells in a biological specimen. |
| C96654 | Granulocytes | Granulocytes; Polymorphonuclear Leukocytes | A measurement of the granulocytes in a biological specimen. |
| C147351 | Granulocytes/Leukocytes | Granulocytes/Leukocytes; Polymorphonuclear Leukocytes/Leukocytes | A relative measurement (ratio or percentage) of the granulocytes to total leukocytes in a biological specimen. |
| C98866 | Granulocytes/Total Cells | Granulocytes/Total Cells | A relative measurement (ratio or percentage) of the granulocytes to total cells in a biological specimen (for example a bone marrow specimen). |
| C130105 | Grass Mix Pollen Antigen IgA Antibody | Grass Mix Pollen Antigen IgA Antibody | A measurement of the grass mix pollen antigen IgA antibody in a biological specimen. |
| C130103 | Grass Mix Pollen Antigen IgE Antibody | Grass Mix Pollen Antigen IgE Antibody | A measurement of the grass mix pollen antigen IgE antibody in a biological specimen. |
| C130104 | Grass Mix Pollen Antigen IgG Antibody | Grass Mix Pollen Antigen IgG Antibody | A measurement of the grass mix pollen antigen IgG antibody in a biological specimen. |
| C165924 | Grass Mix Pollen IgE AB RAST Score | Grass Mix Pollen IgE AB RAST Score | A classification of the amount of grass mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165905 | Grass Mix Pollen IgG AB RAST Score | Grass Mix Pollen IgG AB RAST Score | A classification of the amount of tree grass pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C135422 | Growth Differentiation Factor 11 | BMP-11; Bone Morphogenetic Protein 11; Growth Differentiation Factor 11 | A measurement of the growth differentiation factor 11 in a biological specimen. |
| C181406 | Growth Differentiation Factor 15 | GDF-15; Growth Differentiation Factor 15; Macrophage Inhibitory Cytokine-1; MIC-1 | A measurement of the growth differentiation factor 15 in a biological specimen. |
| C135423 | Growth Differentiation Factor 8 | Growth Differentiation Factor 8; Myostatin | A measurement of the growth differentiation factor 8 in a biological specimen. |
| C163444 | Growth Hormone Binding Protein | GH Binding Protein; Growth Hormone Binding Protein; Somatotropin Receptor | A measurement of the growth hormone binding protein in a biological specimen. |
| C74861 | Growth Hormone Inhibiting Hormone | Growth Hormone Inhibiting Hormone; Somatostatin | A measurement of the growth hormone inhibiting hormone in a biological specimen. |
| C74862 | Growth Hormone Releasing Hormone | Growth Hormone Releasing Hormone; Somatocrinin | A measurement of the growth hormone releasing hormone in a biological specimen. |
| C186057 | Growth Regulated Oncogene | Growth Regulated Oncogene | A measurement of the total growth regulated oncogene proteins in a biological specimen. |
| C150845 | Guanine Deaminase | Guanase; Guanine Aminohydrolase; Guanine Deaminase | A measurement of the guanine deaminase in a biological specimen. |
| C163440 | Guanylate Binding Protein 1 | Guanylate Binding Protein 1 | A measurement of the guanylate binding protein 1 in a biological specimen. |
| C163441 | Guanylate Binding Protein 2 | Guanylate Binding Protein 2 | A measurement of the guanylate binding protein 2 in a biological specimen. |
| C74604 | Hairy Cells | Hairy Cells | A measurement of the hairy cells (b-cell lymphocytes with hairy projections from the cytoplasm) in a biological specimen. |
| C135428 | Hairy Cells/Leukocytes | Hairy Cells/Leukocytes | A relative measurement (ratio or percentage) of the hairy cells (B-cell lymphocytes with hairy projections from the cytoplasm) to all leukocytes in a biological specimen. |
| C74640 | Hairy Cells/Lymphocytes | Hairy Cells/Lymphocytes | A relative measurement (ratio or percentage) of the hairy cells (b-cell lymphocytes with hairy projections from the cytoplasm) to all lymphocytes in a biological specimen . |
| C135427 | Hairy Cells/Total Cells | Hairy Cells/Total Cells | A relative measurement (ratio or percentage) of the hairy cells to total cells in a biological specimen. |
| C139078 | Halazepam | Halazepam | A measurement of the halazepam present in a biological specimen. |
| C75343 | Hallucinogen | Hallucinogen | A measurement of any hallucinogenic class drug present in a biological specimen. |
| C177964 | Haloperidol | Haloperidol | A measurement of the haloperidol in a biological specimen. |
| C74740 | Haptoglobin | Haptoglobin | A measurement of the haptoglobin protein in a biological specimen. |
| C177960 | Hazelnut Antigen IgE Antibody | Corylus Species Nut Antigen IgE Antibody; Hazelnut Antigen IgE Antibody | A measurement of the hazelnut antigen IgE antibody in a biological specimen. |
| C102274 | HCT Corrected Reticulocytes/Erythrocytes | HCT Corrected Reticulocytes/Erythrocytes | A relative measurement (ratio or percentage) of the hematocrit corrected reticulocytes to erythrocytes in a biological specimen. |
| C105587 | HDL Cholesterol | HDL Cholesterol | A measurement of the high density lipoprotein cholesterol in a biological specimen. |
| C100425 | HDL Cholesterol/LDL Cholesterol | HDL Cholesterol/LDL Cholesterol | A relative measurement (ratio or percentage) of the amount of HDL cholesterol compared to LDL cholesterol in a biological specimen. |
| C147362 | HDL Cholesterol/Total Cholesterol | HDL Cholesterol/Total Cholesterol | A relative measurement (ratio or percentage) of the amount of HDL cholesterol compared to total cholesterol in a biological specimen. |
| C103402 | HDL Particle Size | HDL Particle Size | A measurement of the average particle size of high-density lipoprotein in a biological specimen. |
| C156513 | HDL Phospholipid | HDL Phospholipid; HDL-PL | A measurement of the high density lipoprotein phospholipid in a biological specimen. |
| C80187 | HDL-Cholesterol Subclass 2 | HDL-Cholesterol Subclass 2 | A measurement of the high-density lipoprotein (HDL) cholesterol subclass 2 in a biological specimen. |
| C80188 | HDL-Cholesterol Subclass 3 | HDL-Cholesterol Subclass 3 | A measurement of the high-density lipoprotein (HDL) cholesterol subclass 3 in a biological specimen. |
| C147368 | Heat Shock Protein 70 | Heat Shock Protein 70 | A measurement of the heat shock protein 70 in a biological specimen. |
| C147369 | Heat Shock Protein 90 Alpha | Heat Shock Protein 90 Alpha | A measurement of the heat shock protein 90 alpha in a biological specimen. |
| C163453 | Hect Domain and RLD 5 | E3 ISG15--Protein Ligase HERC5; HECT and RLD Domain Containing E3 Ubiquitin Protein Ligase 5; Hect Domain and RLD 5 | A measurement of the hect domain and RLD 5 in a biological specimen. |
| C74709 | Heinz Bodies | Heinz Bodies; Heinz-Erhlich Bodies | A measurement of the Heinz bodies (small round inclusions within the body of a red blood cell) in a biological specimen. |
| C111206 | Heinz Bodies/Erythrocytes | Heinz Bodies/Erythrocytes | A relative measurement (ratio or percentage) of the erythrocytes that contain heinz bodies to total erythrocytes in a biological specimen. |
| C165966 | Helicase MOV-10 Protein | Helicase MOV-10 Protein; Moloney Leukemia Virus 10 Protein | A measurement of helicase MOV-10 protein in a biological specimen. |
| C74658 | Helmet Cells | Helmet Cells | A measurement of the Helmet cells (specialized Keratocytes with two projections on either end that are tapered and hornlike) in a biological specimen. |
| C102273 | Hematocrit Corrected Reticulocytes | Hematocrit Corrected Reticulocytes | A measurement of the hematocrit corrected reticulocytes in a biological specimen. |
| C64796 | Hematocrit | Erythrocyte Volume Fraction; EVF; Hematocrit; Packed Cell Volume; PCV | The percentage of a whole blood specimen that is composed of red blood cells (erythrocytes). |
| C92258 | Hemoglobin A | Hemoglobin A | A measurement of the hemoglobin A in a biological specimen. |
| C81276 | Hemoglobin A/Total Hemoglobin | Hemoglobin A/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin A to total hemoglobin in a biological specimen. |
| C147363 | Hemoglobin A1/Total Hemoglobin | Hemoglobin A1/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin A1 to total hemoglobin in a biological specimen. |
| C163450 | Hemoglobin A1A | Glycated Hemoglobin 1A; Glycosylated Hemoglobin 1A; Hemoglobin A1A | A measurement of the glycosylated hemoglobin A1A in a biological specimen. |
| C163451 | Hemoglobin A1B | Glycated Hemoglobin 1B; Glycosylated Hemoglobin 1B; Hemoglobin A1B | A measurement of the glycosylated hemoglobin A1B in a biological specimen. |
| C64849 | Hemoglobin A1C | Glycated Hemoglobin; Glycosylated Hemoglobin A1C; HbA1c; Hemoglobin A1C | A measurement of the glycosylated hemoglobin A1C in a biological specimen. |
| C111207 | Hemoglobin A1C/Hemoglobin | Hemoglobin A1C/Hemoglobin | A relative measurement (ratio or percentage) of the glycosylated hemoglobin to total hemoglobin in a biological specimen. |
| C147353 | Hemoglobin A2 Prime/Total Hemoglobin | Hemoglobin A2 Prime/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin A2 prime to total hemoglobin in a biological specimen. |
| C92259 | Hemoglobin A2 | Hemoglobin A2 | A measurement of the hemoglobin A2 in a biological specimen. |
| C81277 | Hemoglobin A2/Total Hemoglobin | Hemoglobin A2/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin A2 to total hemoglobin in a biological specimen. |
| C92260 | Hemoglobin B | Hemoglobin B | A measurement of the hemoglobin B in a biological specimen. |
| C147354 | Hemoglobin Barts/Total Hemoglobin | Hemoglobin Barts/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin Barts to total hemoglobin in a biological specimen. |
| C112288 | Hemoglobin C Crystals | Hemoglobin C Crystals | A measurement of hemoglobin C crystals in a biological specimen. |
| C92261 | Hemoglobin C | Hemoglobin C | A measurement of the hemoglobin C in a biological specimen. |
| C81278 | Hemoglobin C/Total Hemoglobin | Hemoglobin C/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin C to total hemoglobin in a biological specimen. |
| C156515 | Hemoglobin Casts | Hemoglobin Casts | A measurement of the hemoglobin casts present in a biological specimen. |
| C147364 | Hemoglobin D/Total Hemoglobin | Hemoglobin D/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin D to total hemoglobin in a biological specimen. |
| C106525 | Hemoglobin Distribution Width | Hemoglobin Concentration Distribution Width; Hemoglobin Distribution Width | A measurement of the distribution of the hemoglobin concentration in red blood cells. |
| C147365 | Hemoglobin E/Total Hemoglobin | Hemoglobin E/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin E to total hemoglobin in a biological specimen. |
| C92262 | Hemoglobin F | Fetal Hemoglobin; Hemoglobin F | A measurement of the hemoglobin F in a biological specimen. |
| C147366 | Hemoglobin F/Total Hemoglobin | Hemoglobin F/Total Hemoglobin | A relative measurement (ratio or percentage) of the fetal hemoglobin (hemoglobin F) to total hemoglobin in a biological specimen. |
| C161363 | Hemoglobin Fraction Pattern | Hemoglobin Fraction Pattern | A description of the hemoglobin fraction pattern in a biological specimen. |
| C147356 | Hemoglobin G Coushatta/Total Hemoglobin | Hemoglobin G Coushatta/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin G Coushatta to total hemoglobin in a biological specimen. |
| C158234 | Hemoglobin H Inclusion Bodies | HBH Inclusion Bodies; Hemoglobin H Inclusion Bodies; HGH Inclusion Bodies | A measurement of the hemoglobin H inclusion bodies in a biological specimen. |
| C147357 | Hemoglobin Lepore/Total Hemoglobin | Hemoglobin Lepore/Total Hemoglobin | A relative measurement (ratio or percentage) of the Lepore hemoglobin to total hemoglobin in a biological specimen. |
| C147358 | Hemoglobin O-Arab/Total Hemoglobin | Hemoglobin O-Arab/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin O-Arab to total hemoglobin in a biological specimen. |
| C122123 | Hemoglobin S | Hemoglobin S; Sickle Hemoglobin | A measurement of the hemoglobin S in a biological specimen. |
| C81279 | Hemoglobin S/Total Hemoglobin | Hemoglobin S/Total Hemoglobin | A relative measurement (ratio or percentage) of the hemoglobin S to total hemoglobin in a biological specimen. |
| C135425 | Hemoglobin Tetramer | Hemoglobin Tetramer | A measurement of the hemoglobin tetramer in a biological specimen. |
| C103845 | Hemoglobin Variants | Hemoglobin Variants | A statement that indicates a defined set of hemoglobin variants were looked for in a biological specimen. |
| C64848 | Hemoglobin | Hemoglobin; Hemoglobin Monomer | A measurement of the total erythrocyte associated hemoglobin in a biological specimen. |
| C127617 | Hemoglobin, Free | Hemoglobin, Free | A measurement of the hemoglobin external to erythrocytes in a biological specimen. |
| C111208 | Hemolytic Index | Hemolysis; Hemolytic Index | A measurement of the destruction of red blood cells in a biological specimen. |
| C96659 | Hemosiderin | Hemosiderin | A measurement of the hemosiderin complex in a biological specimen. |
| C165967 | Heparin | Heparin | A measurement of the heparin in a biological specimen. |
| C172514 | Hepatocyte Growth Factor Receptor | c-Met; Hepatocyte Growth Factor Receptor; MET Proto-Oncogene, Receptor Tyrosine Kinase; Tyrosine-Protein Kinase Met | A measurement of the hepatocyte growth factor receptor in a biological specimen. |
| C181453 | Hepatocyte Growth Factor Receptor, Free | Hepatocyte Growth Factor Receptor, Free | A measurement of the free (unbound) hepatocyte growth factor receptor in a biological specimen. |
| C135426 | Hepatocyte Growth Factor | Hepatocyte Growth Factor | A measurement of the hepatocyte growth factor in a biological specimen. |
| C174387 | Hepcidin | Hepcidin | A measurement of the total hepcidin in a biological specimen. |
| C116186 | Heterophils | Heterophils | A measurement of heterophils (granular leukocytes) in a biological specimen from avian species. |
| C116187 | Heterophils/Leukocytes | Heterophils/Leukocytes | A relative measurement (ratio or percentage) of heterophils to leukocytes in a biological specimen from avian species. |
| C96668 | Hexokinase | Hexokinase | A measurement of the hexokinase in a biological specimen. |
| C181411 | Hexosaminidase A | Beta-Hexosaminidase Subunit Alpha; Beta-N-Acetylhexosaminidase Subunit Alpha; Hexosaminidase A; Hexosaminidase Subunit A; Hexosaminidase Subunit Alpha; N-Acetyl-Beta-Glucosaminidase Subunit Alpha | A measurement of the hexosaminidase A in a biological specimen. |
| C116189 | High Absorption Retic/Reticulocytes | High Absorption Retic/Reticulocytes | A relative measurement (ratio or percentage) of the high absorption reticulocytes to total reticulocytes in a biological specimen. |
| C116188 | High Absorption Reticulocytes | High Absorption Reticulocytes | A measurement of the high absorption reticulocytes in a biological specimen. |
| C74754 | Hippuric Acid Crystals | Hippurate Crystals; Hippuric Acid Crystals | A measurement of the hippuric acid crystals present in a biological specimen. |
| C80189 | Histamine | Histamine | A measurement of the histamine in a biological specimen. |
| C122124 | Histidine | Histidine | A measurement of the histidine in a biological specimen. |
| C112293 | Histone 1 Antibody | Histone 1 Antibody | A measurement of the total histone 1 antibodies in a biological specimen. |
| C112294 | Histone 2A Antibody | Histone 2A Antibody | A measurement of the total histone 2A antibodies in a biological specimen. |
| C112295 | Histone 2B Antibody | Histone 2B Antibody | A measurement of the total histone 2B antibodies in a biological specimen. |
| C112296 | Histone 3 Antibody | Histone 3 Antibody | A measurement of the total histone 3 antibodies in a biological specimen. |
| C112297 | Histone 4 Antibody | Histone 4 Antibody | A measurement of the total histone 4 antibodies in a biological specimen. |
| C111209 | Histone Antibodies | Anti-Histone Antibodies; Histone Antibodies | A measurement of histone antibodies in a biological specimen. |
| C181440 | HLA A03 Antigen | HLA A03 Antigen; HLA-A03 Antigen | A measurement of the HLA A03 antigen in a biological specimen. |
| C181441 | HLA A2 Antigen | HLA A2 Antigen; HLA-A2 Antigen | A measurement of the HLA A2 antigen in a biological specimen. |
| C181442 | HLA A24 Antigen | HLA A24 Antigen; HLA-A24 Antigen | A measurement of the HLA A24 antigen in a biological specimen. |
| C181443 | HLA A3 Antigen | HLA A3 Antigen; HLA-A3 Antigen | A measurement of the HLA A3 antigen in a biological specimen. |
| C128964 | HLA Class I Antibody | HLA Class I Antibody | A measurement of the human leukocyte antigen (HLA) antibody class I in a biological specimen. |
| C128967 | HLA Class I Panel Reactive Antibody | HLA Class I Panel Reactive Antibody | A measurement of the panel reactive antibody (the reactivity between host immune cells and donor) human leukocyte antigen class I in a biological specimen. |
| C154746 | HLA Class IA Antigen | HLA Class IA Antigen | A measurement of the HLA class IA antigen in a biological specimen. |
| C154747 | HLA Class IB Antigen | HLA Class IB Antigen | A measurement of the HLA class IB antigen in a biological specimen. |
| C154748 | HLA Class IC Antigen | HLA Class IC Antigen | A measurement of the HLA class IC antigen in a biological specimen. |
| C128965 | HLA Class II Antibody | HLA Class II Antibody | A measurement of the human leukocyte antigen (HLA) antibody class II in a biological specimen. |
| C128966 | HLA Class II Panel Reactive Antibody | HLA Class II Panel Reactive Antibody | A measurement of the panel reactive antibody (the reactivity between host immune cells and donor) human leukocyte antigen class II in a biological specimen. |
| C181439 | HLA Cw Antigen | HLA Cw Antigen; HLA-Cw Antigen | A measurement of the HLA Cw antigen in a biological specimen. |
| C181417 | HLA DP Alpha1 Antigen | HLA DP Alpha1 Antigen; HLA-DP Alpha1 Antigen | A measurement of the HLA DP alpha1 antigen in a biological specimen. |
| C181444 | HLA DP Beta Antigen | HLA DP Beta Antigen; HLA-DP Beta Antigen | A measurement of the total HLA DP beta antigen in a biological specimen. |
| C154751 | HLA DP Beta1 Antigen | HLA DP Beta1 Antigen | A measurement of the HLA DP beta1 antigen in a biological specimen. |
| C181416 | HLA DQ Alpha1 Antigen | HLA DQ Alpha1 Antigen; HLA-DQ Alpha1 Antigen | A measurement of the HLA DQ alpha1 antigen in a biological specimen. |
| C154750 | HLA DQ Beta1 Antigen | HLA DQ Beta1 Antigen | A measurement of the HLA DQ beta1 antigen in a biological specimen. |
| C186061 | HLA DQ2 Antigen | HLA DQ2 Antigen; HLA-DQ2 Antigen | A measurement of the HLA DQ2 antigen in a biological specimen. |
| C186062 | HLA DQ8 Antigen | HLA DQ8 Antigen; HLA-DQ8 Antigen | A measurement of the HLA DQ8 antigen in a biological specimen. |
| C176962 | HLA DR Antigen | HLA DR Antigen; HLA-DR Antigen | A measurement of the total HLA DR antigen in a biological specimen. |
| C181192 | HLA DR Beta Antigen | HLA DR Beta Antigen; HLA-DR Beta Antigen | A measurement of the total HLA DR beta antigen in a biological specimen. |
| C154749 | HLA DR Beta1 Antigen | HLA DR Beta1 Antigen | A measurement of the HLA DR beta1 antigen in a biological specimen. |
| C181415 | HLA DR Beta2 Antigen | HLA DR Beta2 Antigen; HLA-DR Beta2 Antigen | A measurement of the HLA DR beta2 antigen in a biological specimen. |
| C181412 | HLA DR Beta3 Antigen | HLA DR Beta3 Antigen; HLA-DR Beta3 Antigen | A measurement of the HLA DR beta3 antigen in a biological specimen. |
| C181413 | HLA DR Beta4 Antigen | HLA DR Beta4 Antigen; HLA-DR Beta4 Antigen | A measurement of the HLA DR beta4 antigen in a biological specimen. |
| C181414 | HLA DR Beta5 Antigen | HLA DR Beta5 Antigen; HLA-DR Beta5 Antigen | A measurement of the HLA DR beta5 antigen in a biological specimen. |
| C128933 | HLA Mismatch Count | HLA Mismatch Count | A measurement to determine the number of mismatches between the recipient and the donor for the human leukocyte antigens (HLA). |
| C128955 | HLA-A Antigen Type | HLA-A Antigen Type | The identification of the type of human leukocyte antigen, class I, group A (HLA-A), in a biological specimen. |
| C128956 | HLA-A Mismatch Count | HLA-A Mismatch Count | A measurement to determine the number of mismatches between the recipient and the donor for the human leukocyte antigen, class I, group A (HLA-A). |
| C128954 | HLA-A2 Antibody | HLA-A2 Antibody | A measurement of the human leukocyte antigen A2 (HLA-A2) antibody in a biological specimen. |
| C128953 | HLA-A23 Antibody | HLA-A23 Antibody | A measurement of the human leukocyte antigen A23 (HLA-A23) antibody in a biological specimen. |
| C128957 | HLA-B Antigen Type | HLA-B Antigen Type | The identification of the type of human leukocyte antigen, class I, group B (HLA-B), in a biological specimen. |
| C128958 | HLA-B Mismatch Count | HLA-B Mismatch Count | A measurement to determine the number of mismatches between the recipient and the donor for the human leukocyte antigen, class I, group B (HLA-B). |
| C100460 | HLA-B27 Antigen | HLA-B27 Antigen; Human Leukocyte Antigen B27 | A measurement of the human leukocyte antigen B27 (HLA-B27) in a biological specimen. |
| C128962 | HLA-DR Antigen Type | HLA-DR Antigen Type | The identification of the type of human leukocyte antigen, class II, antigen-D-related (HLA-DR), in a biological specimen. |
| C128963 | HLA-DR Mismatch Count | HLA-DR Mismatch Count | A measurement to determine the number of mismatches between the recipient and the donor for the human leukocyte antigen, class II, antigen-D-related (HLA-DR). |
| C128959 | HLA-DR51 Antibody | HLA-DR51 Antibody | A measurement of the human leukocyte antigen DR51 (HLA-DR51) antibody in a biological specimen. |
| C189510 | HLA-DR51 Antigen Type | HLA-DR51 Antigen Type | The identification of the type of human leukocyte antigen, class II, antigen-D-related 51 (HLA-DR51), in a biological specimen. |
| C128960 | HLA-DR52 Antibody | HLA-DR52 Antibody | A measurement of the human leukocyte antigen DR52 (HLA-DR52) antibody in a biological specimen. |
| C189511 | HLA-DR52 Antigen Type | HLA-DR52 Antigen Type | The identification of the type of human leukocyte antigen, class II, antigen-D-related 52 (HLA-DR52), in a biological specimen. |
| C128961 | HLA-DR53 Antibody | HLA-DR53 Antibody | A measurement of the human leukocyte antigen DR53 (HLA-DR53) antibody in a biological specimen. |
| C189512 | HLA-DR53 Antigen Type | HLA-DR53 Antigen Type | The identification of the type of human leukocyte antigen, class II, antigen-D-related 53 (HLA-DR53), in a biological specimen. |
| C154758 | Homocitrulline | Homocitrulline | A measurement of the homocitrulline in a biological specimen. |
| C74741 | Homocysteine | Homocysteine | A measurement of the homocysteine amino acid in a biological specimen. |
| C74863 | Homovanillic Acid | Homovanillic Acid | A measurement of the homovanillic acid metabolite in a biological specimen. |
| C74704 | Howell-Jolly Bodies | Howell-Jolly Bodies | A measurement of the Howell-Jolly bodies (spherical, blue-black condensed DNA inclusions within the body of a red blood cell that appear under Wright-stain) in a biological specimen. |
| C103405 | Human Albumin Antibody | Human Albumin Antibody | A measurement of the human albumin antibody in a biological specimen. |
| C165965 | Human Anti-Human Antibody | Human Anti-Human Antibody | A measurement of the total human anti-human antibody in a biological specimen. |
| C103406 | Human Anti-Mouse Antibody | HAMA; Human Anti-Mouse Antibody | A measurement of the human anti-mouse antibody in a biological specimen. |
| C98740 | Human Anti-Sheep IgE Antibody | Human Anti-Sheep IgE Antibody | A measurement of the human anti-sheep IgE antibodies in a biological specimen. |
| C98741 | Human Anti-Sheep IgG Antibody | Human Anti-Sheep IgG Antibody | A measurement of the human anti-sheep IgG antibodies in a biological specimen. |
| C98742 | Human Anti-Sheep IgM Antibody | Human Anti-Sheep IgM Antibody | A measurement of the human anti-sheep IgM antibodies in a biological specimen. |
| C112312 | Human Epidermal Growth Factor Receptor 2 | ERBB2; HER2/NEU; Human Epidermal Growth Factor Receptor 2 | A measurement of HER2 protein in a biological specimen. |
| C163452 | Human Epididymis Protein 4 | Human Epididymis Protein 4 | A measurement of the human epididymis protein 4 in a biological specimen. |
| C142279 | Huntingtin Protein | Huntingtin Protein | A measurement of the huntingtin protein in a biological specimen. |
| C142280 | Huntingtin Protein, Mutant | Huntingtin Protein, Mutant | A measurement of the mutant huntingtin protein in a biological specimen. |
| C74770 | Hyaline Casts | Hyaline Casts | A measurement of the hyaline casts present in a biological specimen. |
| C174305 | Hyalogranular Casts | Hyalogranular Casts | A measurement of the hyalogranular casts in a biological specimen. |
| C112319 | Hyaluronic Acid | Hyaluronic Acid | A measurement of hyaluronic acid in a biological specimen. |
| C74879 | Hydrocodone | Hydrocodone | A measurement of the hydrocodone present in a biological specimen. |
| C102275 | Hydrogen | Hydrogen | A measurement of the hydrogen in a biological specimen. |
| C186060 | Hydrogen+Methane | H+CH4; Hydrogen+Methane | A measurement of the hydrogen and methane in a biological specimen. |
| C74880 | Hydromorphone | Hydromorphone | A measurement of the hydromorphone present in a biological specimen. |
| C147352 | Hydroxyalprazolam | Hydroxyalprazolam | A measurement of the total hydroxyalprazolam present in a biological specimen. |
| C181419 | Hydroxyethylflurazepam | 2-Hydroxyethylflurazepam; Hydroxyethylflurazepam | A measurement of the hydroxyethylflurazepam a biological specimen. |
| C154767 | Hydroxylysine | Hydroxylysine | A measurement of the hydroxylysine in a biological specimen. |
| C80190 | Hydroxyproline | Hydroxyproline | A measurement of the total hydroxyproline in a biological specimen. |
| C176300 | Hyocholate | Hyocholate; Hyocholic Acid | A measurement of the hyocholate in a biological specimen. |
| C96669 | Hyperchromia | Hyperchromia; Hyperchromic Erythrocytes | A measurement of the prevalence of the erthrocytes with an elevated hemoglobin concentration. |
| C181408 | Hyperchromic Erythrocytes/Erythrocytes | Hyperchromic Erythrocytes/Erythrocytes | A relative measurement (ratio or percentage) of the hyperchromic erythrocytes to total erythrocytes in a biological specimen. |
| C74612 | Hypersegmented Cells | Hypersegmented Cells | A measurement of the hypersegmented (more than five lobes) neutrophils in a biological specimen. |
| C64802 | Hypochromia | Hypochromia; Hypochromic Erythrocytes | An observation which indicates that the hemoglobin concentration in a red blood cell specimen has fallen below a specified level. |
| C181409 | Hypochromic Erythrocytes/Erythrocytes | Hypochromic Erythrocytes/Erythrocytes | A relative measurement (ratio or percentage) of the hypochromic erythrocytes to total erythrocytes in a biological specimen. |
| C116201 | Hypogranular Neutrophils | Hypogranular Neutrophils | A measurement of the hypogranular neutrophils in a biological specimen. |
| C187809 | Hypoxanthine-Guanine PRT | Hypoxanthine-Guanine Phosphoribosyltransferase; Hypoxanthine-Guanine PRT | A measurement of the hypoxanthine-guanine phosphoribosyltransferase in a biological specimen. |
| C111232 | Icteric Index | Icteric Index; Icterus | A measurement of the yellow color of a biological specimen, due to the presence of bile pigments. |
| C184514 | IDL Apolipoprotein B | IDL Apolipoprotein B | A measurement of the apolipoprotein B in the intermediate density lipoprotein fraction of a biological specimen. |
| C112325 | IDL Cholesterol | IDL Cholesterol; Intermediate Density Lipoprotein | A measurement of the intermediate density lipoprotein in a biological specimen. |
| C187810 | IDL Cholesterol/LDL Cholesterol | IDL Cholesterol/LDL Cholesterol | A relative measurement (ratio) of the amount of intermediate density lipoprotein cholesterol compared to low density lipoprotein cholesterol in a biological specimen. |
| C116197 | IDL Particles | IDL Particles; Intermediate Density Lipoproteins Particles | A measurement of the concentration of IDL particles in a biological specimen. |
| C189507 | IDL Triglyceride | IDL Triglyceride | A measurement of the intermediate density lipoprotein triglyceride in a biological specimen. |
| C147371 | IDL+VLDL Cholesterol Subtype 3 | IDL Cholesterol and VLDL Cholesterol Subtype 3; IDL+VLDL Cholesterol Subtype 3 | A measurement of the intermediate density lipoprotein cholesterol and the very low density lipoprotein cholesterol subtype 3 in a biological specimen. |
| C147373 | IgG Clearance | IgG Clearance | A measurement of the IgG clearance in a biological specimen. |
| C147374 | IgG Clearance/Albumin Clearance | IgG Clearance/Albumin Clearance | A relative measurement (ratio) of the IgG clearance to albumin clearance in a biological specimen. |
| C111233 | IgG IgM IgA Total | IgG IgM IgA Total | A measurement of the total IgG, IgM, and IgA in a biological specimen. |
| C147375 | IgG Synthesis Rate | IgG Synthesis Rate | A measurement of the IgG synthesis rate in a biological specimen. |
| C177984 | Iloperidone | Iloperidone | A measurement of the iloperidone in a biological specimen. |
| C186071 | Imipramine | Imipramine | A measurement of the imipramine in a biological specimen. |
| C96670 | Immature Basophils | Immature Basophils | A measurement of the immature basophils in a biological specimen. |
| C96671 | Immature Basophils/Leukocytes | Immature Basophils/Leukocytes | A relative measurement (ratio or percentage) of immature basophils to total leukocytes in a biological specimen. |
| C96672 | Immature Cells | Immature Cells | A measurement of the total immature cells in a blood specimen. |
| C111234 | Immature Cells/Total Cells | Immature Cells/Total Cells | A relative measurement (ratio or percentage) of the immature hematopoietic cells to total cells in a biological specimen. |
| C96673 | Immature Eosinophils | Immature Eosinophils | A measurement of the immature eosinophils in a biological specimen. |
| C96674 | Immature Eosinophils/Leukocytes | Immature Eosinophils/Leukocytes | A relative measurement (ratio or percentage) of immature eosinophils to total leukocytes in a biological specimen. |
| C96675 | Immature Granulocytes | Immature Granulocytes | A measurement of the total immature granulocytes in a biological specimen. |
| C100445 | Immature Granulocytes/Leukocytes | Immature Granulocytes/Leukocytes | A relative measurement (ratio or percentage) of the immature granulocytes to leukocytes in a biological specimen (for example a bone marrow specimen). |
| C127625 | Immature Leukocytes | Immature Leukocytes | A measurement of the immature leukocytes in a biological specimen. |
| C127626 | Immature Leukocytes/Leukocytes | Immature Leukocytes/Leukocytes | A relative measurement (ratio or percentage) of the immature leukocytes to leukocytes in a biological specimen. |
| C100444 | Immature Lymphocytes | Immature Lymphocytes | A measurement of the immature lymphocytes in a biological specimen. |
| C100443 | Immature Lymphocytes/Leukocytes | Immature Lymphocytes/Leukocytes | A relative measurement (ratio or percentage) of the immature lymphocytes to leukocytes in a biological specimen. |
| C96676 | Immature Monocytes | Immature Monocytes | A measurement of the immature monocytes in a biological specimen. |
| C96677 | Immature Monocytes/Leukocytes | Immature Monocytes/Leukocytes | A relative measurement (ratio or percentage) of immature monocytes to total leukocytes in a biological specimen. |
| C96678 | Immature Neutrophils | Immature Neutrophils | A measurement of the total immature neutrophils in a biological specimen. |
| C100442 | Immature Neutrophils/Leukocytes | Immature Neutrophils/Leukocytes | A relative measurement (ratio or percentage) of the immature neutrophils to leukocytes in a biological specimen. |
| C96679 | Immature Plasma Cells | Immature Plasma Cells | A measurement of the immature plasma cells in a biological specimen. |
| C96680 | Immature Plasma Cells/Lymphocytes | Immature Plasma Cells/Lymphocytes | A relative measurement (ratio or percentage) of immature plasma cells to total lymphocytes in a biological specimen. |
| C147416 | Immature Plasma Cells/Total Cells | Immature Plasma Cells/Total Cells | A relative measurement (ratio or percentage) of the immature plasma cells (plasmacytes) to total cells in a biological specimen. |
| C154723 | Immature Platelets | Immature Platelets; Reticulated Platelets | A measurement of the immature platelets in a biological specimen. |
| C170580 | Immature Platelets/Total Platelets | Immature Platelet Fraction; Immature Platelets/Total Platelets; IPF; Reticulated Platelets/Total Platelets | A relative measurement (ratio or percentage) of immature platelets to total platelets in a biological specimen. |
| C102276 | Immature Reticulocyte Fraction | Immature Reticulocyte Fraction | A measurement of the immature reticulocyte fraction present in a biological specimen. |
| C103407 | Immunoblasts | Immunoblastic Lymphocytes; Immunoblasts | A measurement of the immunoblasts in a biological specimen. |
| C106535 | Immunoblasts/Lymphocytes | Immunoblasts/Lymphocytes; Lymphocytes, Immunoblastic/Lymphocytes | A relative measurement (ratio or percentage) of immunoblasts to all lymphocytes present in a sample. |
| C81969 | Immunoglobulin A | Immunoglobulin A | A measurement of the total immunoglobulin A in a biological specimen. |
| C184515 | Immunoglobulin A/Complement C3 | IgA/C3; IgA/Complement C3; Immunoglobulin A/Complement C3 | A relative measurement (ratio) of the immunoglobulin A to complement C3 in a biological specimen. |
| C98745 | Immunoglobulin D | Immunoglobulin D | A measurement of the Immunoglobulin D in a biological specimen. |
| C81970 | Immunoglobulin E | Immunoglobulin E | A measurement of the Immunoglobulin E in a biological specimen. |
| C122127 | Immunoglobulin G Subclass 1 | Immunoglobulin G Subclass 1 | A measurement of the immunoglobulin G subclass 1 in a biological specimen. |
| C122128 | Immunoglobulin G Subclass 2 | Immunoglobulin G Subclass 2 | A measurement of the immunoglobulin G subclass 2 in a biological specimen. |
| C122129 | Immunoglobulin G Subclass 3 | Immunoglobulin G Subclass 3 | A measurement of the immunoglobulin G subclass 3 in a biological specimen. |
| C122130 | Immunoglobulin G Subclass 4 | Immunoglobulin G Subclass 4 | A measurement of the immunoglobulin G subclass 4 in a biological specimen. |
| C81971 | Immunoglobulin G | Immunoglobulin G | A measurement of the total immunoglobulin G in a biological specimen. |
| C147372 | Immunoglobulin G/Albumin | IgG/Albumin; Immunoglobulin G/Albumin | A relative measurement (ratio or percentage) of the immunoglobulin G to albumin in a biological specimen. |
| C119285 | Immunoglobulin G/Creatinine | Immunoglobulin G/Creatinine | A relative measurement (ratio or percentage) of the immunoglobulin G to creatinine in a biological specimen. |
| C154737 | Immunoglobulin Heavy Constant Gamma 2 | Immunoglobulin Heavy Constant Gamma 2 | A measurement of the immunoglobulin heavy constant gamma 2 in a biological specimen. |
| C154738 | Immunoglobulin Heavy Constant Gamma 4 | Immunoglobulin Heavy Constant Gamma 4 | A measurement of the immunoglobulin heavy constant gamma 4 in a biological specimen. |
| C147376 | Immunoglobulin Light Chains | Immunoglobulin Light Chains | A measurement of the total immunoglobulin (kappa and lambda) light chains in a biological specimen. |
| C156517 | Immunoglobulin Light Chains, Free | Immunoglobulin Light Chains, Free | A measurement of the total free immunoglobulin (kappa and lambda) light chains in a biological specimen. |
| C81972 | Immunoglobulin M | Immunoglobulin M | A measurement of the total immunoglobulin M in a biological specimen. |
| C81869 | Immunoglobulin | Immunoglobulin | A measurement of the total immunoglobulin in a biological specimen. |
| C116184 | Inclusion Bodies | Inclusion Bodies | A measurement of the inclusion bodies in a biological specimen. |
| C82044 | Indican | Indican | A measurement of the indican present in a biological specimen. |
| C64483 | Indirect Bilirubin | Indirect Bilirubin | A measurement of the unconjugated or non-water-soluble bilirubin in a biological specimen. |
| C184513 | Indocyanine Green Clearance | Indocyanine Green Clearance | A measurement of the volume of serum or plasma that would be cleared of indocyanine green by excretion for a specified unit of time (e.g. one minute). |
| C184512 | Indocyanine Green | Indocyanine Green | A measurement of the indocyanine green in a biological specimen. |
| C130114 | Industrial Mix Antigen IgE Antibody | Industrial Mix Antigen IgE Antibody | A measurement of the industrial mix antigen IgE antibody in a biological specimen. |
| C130115 | Industrial Mix Antigen IgG Antibody | Industrial Mix Antigen IgG Antibody | A measurement of the industrial mix antigen IgG antibody in a biological specimen. |
| C165928 | Industrial Mix IgE AB RAST Score | Industrial Mix IgE AB RAST Score | A classification of the amount of industrial mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165909 | Industrial Mix IgG AB RAST Score | Industrial Mix IgG AB RAST Score | A classification of the amount of industrial mix IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C82020 | Inhibin A | Inhibin A | A measurement of the inhibin A in a biological specimen. |
| C96681 | Inhibin B | Inhibin B | A measurement of the inhibin B in a biological specimen. |
| C161358 | Inorganic Pyrophosphate | Inorganic Pyrophosphate | A measurement of the inorganic pyrophosphate in a biological specimen. |
| C119287 | Insulin Antibody | Insulin Antibody | A measurement of the antibody to insulin in a biological specimen. |
| C119286 | Insulin Autoantibody | Insulin Autoantibody | A measurement of the antibody to endogenous insulin in a biological specimen. |
| C123458 | Insulin Resistance | Insulin Resistance | A measurement of the insulin resistance (a cell's inability to respond to insulin) in a biological specimen. |
| C123459 | Insulin Sensitivity | Insulin Sensitivity | A measurement of the insulin sensitivity (cells are stimulated by lower than normal insulin levels) in a biological specimen. |
| C74788 | Insulin | Insulin | A measurement of the insulin in a biological specimen. |
| C147377 | Insulin, Free | Insulin, Free | A measurement of the free insulin in a biological specimen. |
| C186072 | Insulin, Intact | Insulin, Intact | A measurement of the intact insulin in a biological specimen. |
| C128968 | Insulin-Like Growth Factor Binding Prot1 | Insulin-Like Growth Factor Binding Prot1; Insulin-Like Growth Factor Binding Protein 1 | A measurement of the total insulin-like growth factor binding protein 1 in a biological specimen. |
| C128969 | Insulin-Like Growth Factor Binding Prot2 | Insulin-Like Growth Factor Binding Prot2; Insulin-Like Growth Factor Binding Protein 2 | A measurement of the insulin-like growth factor binding protein 2 in a biological specimen. |
| C112322 | Insulin-Like Growth Factor Binding Prot3 | Insulin-Like Growth Factor Binding Prot3; Insulin-Like Growth Factor Binding Protein 3 | A measurement of the insulin-like growth factor binding protein 3 in a biological specimen. |
| C165969 | Insulin-Like Growth Factor Binding Prot7 | AGM; FSTL2; IBP-7; IGFBP-7; IGFBP-7v; IGFBPRP1; Insulin-Like Growth Factor Binding Prot7; Insulin-like Growth Factor Binding Protein 7; MAC25; PSF; RAMSVPS; TAF | A measurement of the insulin-like growth factor binding protein 7 in a biological specimen. |
| C74864 | Insulin-like Growth Factor-1 | Insulin-like Growth Factor-1 | A measurement of the insulin-like growth factor-1 in a biological specimen. |
| C74865 | Insulin-like Growth Factor-2 | Insulin-like Growth Factor-2 | A measurement of the insulin-like growth factor-2 in a biological specimen. |
| C119284 | Insulinoma-Associated Protein 2 Antibody | Insulinoma-Associated Protein 2 Antibody | A measurement of the insulinoma-associated protein 2 antibody in a biological specimen. |
| C124345 | Intercellular Adhesion Molecule 1 | CD54; Intercellular Adhesion Molecule 1 | A measurement of the intercellular adhesion molecule 1 in a biological specimen. |
| C165968 | Intercellular Adhesion Molecule 3 | Intercellular Adhesion Molecule 3 | A measurement of the intercellular adhesion molecule 3 in a biological specimen. |
| C124344 | Intercellular Adhesion Molecule | Intercellular Adhesion Molecule | A measurement of the total intercellular adhesion molecule in a biological specimen. |
| C184646 | Interferon Alpha Type 2 | Interferon Alpha Type 2 | A measurement of the interferon alpha type 2 in a biological specimen. |
| C81994 | Interferon Alpha | Interferon Alpha | A measurement of the total interferon alpha in a biological specimen. |
| C163455 | Interferon Alpha-Inducible Protein 27 | Interferon Alpha-Induced Protein 27; Interferon Alpha-Inducible Protein 27 | A measurement of the interferon alpha-inducible protein 27 in a biological specimen. |
| C163458 | Interferon Alpha-Inducible Protein 6 | Interferon Alpha-Inducible Protein 6 | A measurement of the interferon alpha-inducible protein 6 in a biological specimen. |
| C81995 | Interferon Beta | Interferon Beta | A measurement of the interferon beta in a biological specimen. |
| C81996 | Interferon Gamma | Interferon Gamma | A measurement of the interferon gamma in a biological specimen. |
| C163459 | Interferon-Induced 56 kDa Protein | Interferon-Induced 56 kDa Protein; Interferon-Induced Protein With Tetratricopeptide Repeats 1 | A measurement of the interferon-induced 56 KDa protein in a biological specimen. |
| C163460 | Interferon-Induced 60 kDa Protein | Interferon-Induced 60 kDa Protein; Interferon-Induced Protein With Tetratricopeptide Repeats 3 | A measurement of the interferon-induced 60 KDa protein in a biological specimen. |
| C163456 | Interferon-Induced Protein 44 | Interferon-Induced Protein 44 | A measurement of the interferon-induced protein 44 in a biological specimen. |
| C163457 | Interferon-Induced Protein 44-Like | Interferon-Induced Protein 44-Like | A measurement of the interferon-induced protein 44-like in a biological specimen. |
| C163469 | Interferon-Induced Protein p78 | Interferon-Induced GTP-Binding Protein Mx1; Interferon-Induced Protein p78 | A measurement of the interferon-induced protein P78 in a biological specimen. |
| C122131 | Interleukin 1 Alpha | Interleukin 1 Alpha | A measurement of interleukin 1 alpha in a biological specimen. |
| C112323 | Interleukin 1 Beta | IL-1B; IL1Beta; Interleukin 1 Beta; Interleukin 1B | A measurement of interleukin 1 beta in a biological specimen. |
| C156518 | Interleukin 1 Excretion Rate | Interleukin 1 Excretion Rate | A measurement of the amount of interleukin 1 being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C112324 | Interleukin 1 Receptor Antagonist | IL-1RA; Interleukin 1 Receptor Antagonist | A measurement of the interleukin 1 receptor antagonist in a biological specimen. |
| C165970 | Interleukin 1 Receptor Type 2 | CD121b; CDw121b; IL-1R-2; IL-1RT2; IL1R2c; IL1RB; Interleukin 1 Receptor Type 2 | A measurement of the interleukin 1 receptor type 2 in a biological specimen. |
| C142281 | Interleukin 1 Receptor-Like 1 | Interleukin 1 Receptor-Like 1; Protein ST2; sST2 | A measurement of the interleukin 1 receptor-like 1 in a biological specimen. |
| C74805 | Interleukin 1 | Interleukin 1 | A measurement of the interleukin 1 in a biological specimen. |
| C74806 | Interleukin 10 | Interleukin 10 | A measurement of the interleukin 10 in a biological specimen. |
| C74807 | Interleukin 11 | Interleukin 11 | A measurement of the interleukin 11 in a biological specimen. |
| C127623 | Interleukin 12 Beta | Interleukin 12 Beta; Interleukin 12 Beta Subunit; Interleukin 12 p40; Interleukin 12 p40 Subunit | A measurement of p40 subunit of Interleukin 12 in a biological specimen. |
| C74808 | Interleukin 12 | Interleukin 12; Interleukin 12 p70 | A measurement of the interleukin 12 in a biological specimen. |
| C128970 | Interleukin 12+23 p40 | Interleukin 12+23 p40 | A measurement of the p40 subunit of the interleukins 12 and 23 in a biological specimen. |
| C74809 | Interleukin 13 | Interleukin 13 | A measurement of the interleukin 13 in a biological specimen. |
| C74810 | Interleukin 14 | Interleukin 14 | A measurement of the interleukin 14 in a biological specimen. |
| C74811 | Interleukin 15 | Interleukin 15 | A measurement of the interleukin 15 in a biological specimen. |
| C74812 | Interleukin 16 | Interleukin 16 | A measurement of the interleukin 16 in a biological specimen. |
| C74813 | Interleukin 17 | IL-17A; Interleukin 17; Interleukin 17A | A measurement of the interleukin 17 in a biological specimen. |
| C172513 | Interleukin 18 Binding Protein | Interleukin 18 Binding Protein | A measurement of the interleukin 18 binding protein in a biological specimen. |
| C156519 | Interleukin 18 Excretion Rate | Interleukin 18 Excretion Rate | A measurement of the amount of interleukin 18 being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C74814 | Interleukin 18 | Interleukin 18 | A measurement of the interleukin 18 in a biological specimen. |
| C74815 | Interleukin 19 | Interleukin 19 | A measurement of the interleukin 19 in a biological specimen. |
| C142282 | Interleukin 2 Receptor Subunit Alpha | CD25; IL-2Ra; Interleukin 2 Receptor Subunit Alpha | A measurement of the interleukin 2 receptor subunit alpha in a biological specimen. |
| C142283 | Interleukin 2 Receptor Subunit Beta | IL-2Rb; Interleukin 2 Receptor Subunit Beta | A measurement of the interleukin 2 receptor subunit beta in a biological specimen. |
| C158147 | Interleukin 2 Receptor | Interleukin 2 Receptor | A measurement of the interleukin 2 receptor in a biological specimen. |
| C74816 | Interleukin 2 | Interleukin 2 | A measurement of the interleukin 2 in a biological specimen. |
| C74817 | Interleukin 20 | Interleukin 20 | A measurement of the interleukin 20 in a biological specimen. |
| C74818 | Interleukin 21 | Interleukin 21 | A measurement of the interleukin 21 in a biological specimen. |
| C74819 | Interleukin 22 | Interleukin 22 | A measurement of the interleukin 22 in a biological specimen. |
| C74820 | Interleukin 23 | Interleukin 23; Interleukin 23 p59 | A measurement of the interleukin 23 in a biological specimen. |
| C74821 | Interleukin 24 | Interleukin 24 | A measurement of the interleukin 24 in a biological specimen. |
| C74822 | Interleukin 25 | Interleukin 25 | A measurement of the interleukin 25 in a biological specimen. |
| C74823 | Interleukin 26 | Interleukin 26 | A measurement of the interleukin 26 in a biological specimen. |
| C74824 | Interleukin 27 | Interleukin 27 | A measurement of the interleukin 27 in a biological specimen. |
| C74825 | Interleukin 28 | Interleukin 28 | A measurement of the interleukin 28 in a biological specimen. |
| C74826 | Interleukin 29 | Interleukin 29 | A measurement of the interleukin 29 in a biological specimen. |
| C74827 | Interleukin 3 | Interleukin 3 | A measurement of the interleukin 3 in a biological specimen. |
| C74828 | Interleukin 30 | Interleukin 30 | A measurement of the interleukin 30 in a biological specimen. |
| C74829 | Interleukin 31 | Interleukin 31 | A measurement of the interleukin 31 in a biological specimen. |
| C74830 | Interleukin 32 | Interleukin 32 | A measurement of the interleukin 32 in a biological specimen. |
| C74831 | Interleukin 33 | Interleukin 33 | A measurement of the interleukin 33 in a biological specimen. |
| C74832 | Interleukin 4 | Interleukin 4 | A measurement of the interleukin 4 in a biological specimen. |
| C74833 | Interleukin 5 | Interleukin 5 | A measurement of the interleukin 5 in a biological specimen. |
| C74834 | Interleukin 6 | Interleukin 6 | A measurement of the interleukin 6 in a biological specimen. |
| C74835 | Interleukin 7 | Interleukin 7 | A measurement of the interleukin 7 in a biological specimen. |
| C74836 | Interleukin 8 | Interleukin 8 | A measurement of the interleukin 8 in a biological specimen. |
| C74837 | Interleukin 9 | Interleukin 9 | A measurement of the interleukin 9 in a biological specimen. |
| C119266 | Intestinal Specific Alkaline Phosphatase | Intestinal Specific Alkaline Phosphatase | A measurement of the intestinal specific alkaline phosphatase isoform in a biological specimen. |
| C98748 | Inulin Clearance | Inulin Clearance | A measurement of the volume of serum or plasma that would be cleared of inulin by excretion of urine for a specified unit of time (e.g. one minute). |
| C125945 | Inulin | Inulin | A measurement of the inulin in a biological specimen. |
| C181193 | Iodine | Iodine | A measurement of the total iodine in a biological specimen. |
| C181445 | Iodine, Free | Iodine, Free | A measurement of the free (unbound) iodine in a biological specimen. |
| C100439 | Iohexol Clearance | Iohexol Clearance | A measurement of the volume of serum or plasma that would be cleared of Iohexol by excretion of urine for a specified unit of time (e.g. one minute). |
| C125946 | Iohexol | Iohexol | A measurement of iohexol in a biological specimen. |
| C98750 | Iothalamate Clearance Adjusted for BSA | Iothalamate Clearance Adjusted for BSA | A measurement of the volume of serum or plasma that would be cleared of iothalamate by excretion of urine for a specified unit of time (e.g. one minute), adjusted for body surface area. |
| C98749 | Iothalamate Clearance | Iothalamate Clearance | A measurement of the volume of serum or plasma that would be cleared of iothalamate by excretion of urine for a specified unit of time (e.g. one minute). |
| C150819 | Iron Excretion Rate | Iron Excretion Rate | A measurement of the amount of iron being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C74679 | Iron | FE; Iron | A measurement of the iron in a biological specimen. |
| C127622 | Islet Amyloid Polypeptide | Amylin; Islet Amyloid Polypeptide | A measurement of the islet amyloid polypeptide in a biological specimen. |
| C81985 | Islet Cell 512 Antibody | IA-2 Antibody; ICA-512 Antibody; Islet Antigen 2 Autoantibody; Islet Cell 512 Antibody; Islet Cell Antigen 512 Autoantibody | A measurement of the islet cell 512 antibody in a biological specimen. |
| C81986 | Islet Cell 512 Antigen | Islet Cell 512 Antigen | A measurement of the islet cell 512 antigen in a biological specimen. |
| C154725 | Islet Cell Antibody | Islet Cell Antibody | A measurement of the total islet cell antibodies in a biological specimen. |
| C122126 | Islet Cell Cytoplasmic IgG Antibody | Islet Cell Cytoplasmic IgG Antibody | A measurement of the islet cell cytoplasmic IgG antibody in a biological specimen. |
| C81987 | Islet Neogenesis Assoc Protein Antibody | Islet Neogenesis Assoc Protein Antibody | A measurement of the islet neogenesis associated protein antibody in a biological specimen. |
| C103410 | Isoleucine | Isoleucine | A measurement of the isoleucine in a biological specimen. |
| C100459 | Jo-1 Antibody | Jo-1 Antibody | A measurement of the Jo-1 antibody in a biological specimen. |
| C165895 | Johnson Grass Pollen IgG4 Antibody | Johnson Grass Pollen IgG4 Antibody | A measurement of the Sorghum halepense pollen IgG4 antibody in a biological specimen. |
| C184542 | JWH-018 | JWH-018; JWH018 | A measurement of the synthetic cannabinoid JWH-018 in a biological specimen. |
| C184543 | JWH-073 | JWH-073; JWH073 | A measurement of the synthetic cannabinoid JWH-073 in a biological specimen. |
| C184546 | JWH-081 | JWH-081; JWH081 | A measurement of the synthetic cannabinoid JWH-081 in a biological specimen. |
| C184547 | JWH-122 | JWH-122; JWH122 | A measurement of the synthetic cannabinoid JWH-122 in a biological specimen. |
| C184544 | JWH-200 | JWH-200; JWH200 | A measurement of the synthetic cannabinoid JWH-200 in a biological specimen. |
| C184545 | JWH-250 | JWH-250; JWH250 | A measurement of the synthetic cannabinoid JWH-250 in a biological specimen. |
| C184548 | JWH-398 | JWH-398; JWH398 | A measurement of the synthetic cannabinoid JWH-398 in a biological specimen. |
| C132374 | Kallikrein-2 | Kallikrein-2 | A measurement of the kallikrein-2 in a biological specimen. |
| C147379 | Kappa Light Chain | Kappa Light Chain | A measurement of the total kappa light chains in a biological specimen. |
| C98730 | Kappa Light Chain, Free | Bence-Jones, Kappa; Kappa Light Chain, Free | A measurement of the free kappa light chain in a biological specimen. |
| C161351 | Kappa Light Chain/Lambda Light Chain | Kappa Lambda Ratio; Kappa Light Chain/Lambda Light Chain | A relative measurement (ratio) of the total kappa light chain to total lambda light chain in a biological specimen. |
| C98731 | Kappa Lt Chain,Free/Lambda Lt Chain,Free | Kappa Lt Chain,Free/Lambda Lt Chain,Free | A relative measurement (ratio or percentage) of the free kappa light chain to the free lambda light chain in a biological specimen. |
| C147380 | Keratocyte | Keratocyte | A measurement of the keratocytes in a biological specimen. |
| C184587 | Ketamine | Ketamine | A measurement of the ketamine in a biological specimen. |
| C184549 | Ketobemidone | Ketobemidone | A measurement of the ketobemidone in a biological specimen. |
| C189519 | Ketone Bodies Excretion Rate | Ketone Bodies Excretion Rate | A measurement of the amount of ketone bodies being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C111239 | Ketone Bodies | Ketone Bodies | A measurement of the ketone bodies (acetone, acetoacetic acid, beta-hydroxybutyric acid, beta-ketopentanoate and beta-hydroxypentanoate) in a biological specimen. |
| C64854 | Ketones | Ketones | A measurement of the ketones in a biological specimen. |
| C132372 | Keyhole Limpet Hemocyanin IgG Antibody | Keyhole Limpet Hemocyanin IgG Antibody | A measurement of the keyhole limpet hemocyanin IgG antibody in a biological specimen. |
| C132373 | Keyhole Limpet Hemocyanin IgM Antibody | Keyhole Limpet Hemocyanin IgM Antibody | A measurement of the keyhole limpet hemocyanin IgM antibody in a biological specimen. |
| C123557 | Ki-67 | Ki-67; KI67; MKI67; pKi-67 | A measurement of the Ki-67 protein in a biological specimen. |
| C163462 | Kidney Injury Molecule-1 Excretion Rate | Kidney Injury Molecule-1 Excretion Rate | A measurement of the amount of kidney injury molecule-1 being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C100433 | Kidney Injury Molecule-1 | Hepatitis A Virus Cellular Receptor 1; Kidney Injury Molecule-1; KIM-1 | A measurement of the kidney injury molecule-1 (Kim-1) in a biological specimen. |
| C177955 | Kidney Injury Molecule-1/Creatinine | Kidney Injury Molecule-1/Creatinine | A relative measurement (ratio or percentage) of the kidney injury molecule-1 to creatinine in a biological specimen. |
| C127624 | Klotho | Klotho | A measurement of the total klotho protein in a biological specimen. |
| C154724 | Krebs von den Lungen-6 | KL-6; Krebs von den Lungen-6 Antigen | A measurement of the Krebs von den Lungen-6 in a biological specimen. |
| C96682 | Kurloff Cells | Kurloff Cells | A measurement of the large secretory granule-containing immune cells in a biological specimen taken from members of certain genera of the Caviidae family. |
| C154740 | Kynurenine | Kynurenine | A measurement of the kynurenine in a biological specimen. |
| C184641 | Lacosamide | Lacosamide | A measurement of the lacosamide in a biological specimen. |
| C165972 | Lactate Dehydrogenase Excretion Rate | Lactate Dehydrogenase Excretion Rate | A measurement of the amount of lactate dehydrogenase being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C64855 | Lactate Dehydrogenase | Lactate Dehydrogenase | A measurement of the lactate dehydrogenase in a biological specimen. |
| C79449 | Lactate Dehydrogenase/Creatinine | Lactate Dehydrogenase/Creatinine | A relative measurement (ratio or percentage) of the lactate dehydrogenase to creatinine in a biological specimen. |
| C79450 | Lactic Acid | 2-hydroxypropanoic acid; Lactate; Lactic Acid | A measurement of the lactic acid in a biological specimen. |
| C120639 | Lactoferrin Antibody | Lactoferrin Antibody | A measurement of the lactoferrin antibody in a biological specimen. |
| C82021 | Lactoferrin | Lactoferrin; Lactotransferrin | A measurement of the lactoferrin in a biological specimen. |
| C186077 | Lactose | Lactose | A measurement of the lactose in a biological specimen. |
| C154741 | Lactulose | Lactulose | A measurement of the lactulose in a biological specimen. |
| C147384 | Lambda Light Chain | Lambda Light Chain | A measurement of the total lambda light chains in a biological specimen. |
| C98732 | Lambda Light Chain, Free | Bence-Jones, Lambda; Lambda Light Chain, Free | A measurement of the free lambda light chain in a biological specimen. |
| C158236 | Large Lymphocytes | Large Lymphocytes | A measurement of the large lymphocytes (approximately between 10 um and 20 um in diameter) in a biological specimen. |
| C74729 | Large Platelets | Large Platelets | A measurement of the large (between 4 um and 7um in diameter) platelets in a biological specimen. |
| C161353 | Large Platelets/Total Platelets | Large Platelets/Total Platelets; Platelet Large Cell Ratio; PLCR | A relative measurement (ratio or percentage) of large platelets to total platelets in a biological specimen. |
| C74659 | Large Unstained Cells | Large Unstained Cells | A measurement of the large, peroxidase-negative cells which cannot be further characterized (i.e. as large lymphocytes, virocytes, or stem cells) present in a biological specimen. |
| C79467 | Large Unstained Cells/Leukocytes | Large Unstained Cells/Leukocytes | A relative measure (ratio or percentage) of the large unstained cells to leukocytes in a biological specimen. |
| C74887 | LDH Isoenzyme 1 | LDH Isoenzyme 1 | A measurement of the lactate dehydrogenase isoenzyme 1 in a biological specimen. |
| C79451 | LDH Isoenzyme 1/LDH | LDH Isoenzyme 1/LDH | A relative measurement (ratio or percentage) of the lactate dehydrogenase isoenzyme 1 to total lactate dehydrogenase in a biological specimen. |
| C74888 | LDH Isoenzyme 2 | LDH Isoenzyme 2 | A measurement of the lactate dehydrogenase isoenzyme 2 in a biological specimen. |
| C79452 | LDH Isoenzyme 2/LDH | LDH Isoenzyme 2/LDH | A relative measurement (ratio or percentage) of the lactate dehydrogenase isoenzyme 2 to total lactate dehydrogenase in a biological specimen. |
| C74889 | LDH Isoenzyme 3 | LDH Isoenzyme 3 | A measurement of the lactate dehydrogenase isoenzyme 3 in a biological specimen. |
| C79453 | LDH Isoenzyme 3/LDH | LDH Isoenzyme 3/LDH | A relative measurement (ratio or percentage) of the lactate dehydrogenase isoenzyme 3 to total lactate dehydrogenase in a biological specimen. |
| C74890 | LDH Isoenzyme 4 | LDH Isoenzyme 4 | A measurement of the lactate dehydrogenase isoenzyme 4 in a biological specimen. |
| C79454 | LDH Isoenzyme 4/LDH | LDH Isoenzyme 4/LDH | A relative measurement (ratio or percentage) of the lactate dehydrogenase isoenzyme 4 to total lactate dehydrogenase in a biological specimen. |
| C74891 | LDH Isoenzyme 5 | LDH Isoenzyme 5 | A measurement of the lactate dehydrogenase isoenzyme 5 in a biological specimen. |
| C79455 | LDH Isoenzyme 5/LDH | LDH Isoenzyme 5/LDH | A relative measurement (ratio or percentage) of the lactate dehydrogenase isoenzyme 5 to total lactate dehydrogenase in a biological specimen. |
| C189508 | LDL Apolipoprotein B | LDL Apolipoprotein B | A measurement of the apolipoprotein B in the low density lipoprotein fraction of a biological specimen. |
| C105588 | LDL Cholesterol | LDL Cholesterol | A measurement of the low density lipoprotein cholesterol in a biological specimen. |
| C121182 | LDL Cholesterol/HDL Cholesterol | LDL Cholesterol/HDL Cholesterol | A relative measurement (ratio) of the low density lipoprotein cholesterol to high density lipoprotein cholesterol in a biological specimen. |
| C103412 | LDL Particle Size | LDL Particle Size | A measurement of the average particle size of low-density lipoprotein in a biological specimen. |
| C120636 | LDL Particles | LDL Particles | A measurement of the concentration of the total LDL particles in a biological specimen. |
| C120637 | LDL Subtype Pattern | LDL Subtype Pattern | A description of the low density lipoprotein particle pattern (an interpretation of the amounts of LDL particles based on size and density) in a biological specimen. |
| C189506 | LDL Triglyceride | LDL Triglyceride | A measurement of the low density lipoprotein triglyceride in a biological specimen. |
| C147382 | Lead | Lead; Pb | A measurement of the lead in a biological specimen. |
| C147381 | Lecithin/Sphingomyelin | Lecithin/Sphingomyelin; LS Ratio | A relative measurement (ratio) of the lecithin to sphingomyelin in a biological specimen. |
| C116202 | Left Shift Neutrophils | Left Shift Neutrophils | An observation of the above normal incidence of immature neutrophils, including band neutrophils and neutrophil precursors in a biological specimen. |
| C74866 | Leptin | Leptin | A measurement of the leptin hormone in a biological specimen. |
| C174293 | Leptocytes | Leptocytes | A measurement of the leptocytes in a biological specimen. |
| C122132 | Leucine Aminopeptidase | Leucine Aminopeptidase | A measurement of the total leucine aminopeptidase present in a biological specimen. |
| C74680 | Leucine Crystals | Leucine Crystals | A measurement of the leucine crystals present in a biological specimen. |
| C165973 | Leucine Rich Alpha-2-Glycoprotein 1 | HMFT1766; Leucine Rich Alpha-2-Glycoprotein 1 | A measurement of the leucine rich alpha-2-glycoprotein 1 in a biological specimen. |
| C122133 | Leucine | Leucine | A measurement of the leucine in a biological specimen. |
| C130163 | Leukemia Inhibitory Factor | Leukemia Inhibitory Factor | A measurement of leukemia inhibitory factor in a biological specimen. |
| C74630 | Leukemic Blasts | Leukemic Blasts | A measurement of the leukemic blasts (lymphoblasts that remain in an immature state even when outside the bone marrow) in a biological specimen. |
| C74641 | Leukemic Blasts/Lymphocytes | Leukemic Blasts/Lymphocytes | A relative measurement (ratio or percentage) of the leukemic blasts (immature lymphoblasts) to mature lymphocytes in a biological specimen. |
| C116195 | Leukemic Cells | Leukemic Cells; Residual Leukemic Cells | A measurement of the leukemic cells in a biological specimen. |
| C92246 | Leukocyte Cell Clumps | Leukocyte Cell Clumps; WBC Clumps; White Blood Cell Clumps | A measurement of white blood cell clumps in a biological specimen. |
| C98493 | Leukocyte Cell Differential | Leukocyte Cell Differential; Leukocyte Cell Fraction; Leukocyte Diff | An overall assessment of the leukocyte subtype distribution in a biological specimen. |
| C92297 | Leukocyte Cell Morphology | Leukocyte Cell Morphology; WBC Morphology; White Blood Cell Morphology | An examination or assessment of the form and structure of white blood cells. |
| C64856 | Leukocyte Esterase | Leukocyte Esterase | A measurement of the enzyme which indicates the presence of white blood cells in a biological specimen. |
| C51948 | Leukocytes | Leukocytes; White Blood Cells | A measurement of the leukocytes in a biological specimen. |
| C135451 | Leukocytes/Total Cells | Leukocytes/Total Cells; WBC/Total Cells | A relative measurement (ratio or percentage) of the leukocytes to total cells in a biological specimen. |
| C103413 | Leukotriene B4 | Leukotriene B4 | A measurement of the leukotriene B4 in a biological specimen. |
| C189516 | Leukotriene C4 Synthase | Leukotriene C4 Synthase | A measurement of the leukotriene C4 synthase in a biological specimen. |
| C103414 | Leukotriene D4 | Leukotriene D4 | A measurement of the leukotriene D4 in a biological specimen. |
| C103415 | Leukotriene E4 | Leukotriene E4 | A measurement of the leukotriene E4 in a biological specimen. |
| C147383 | Leuks Corrected for Nucl Erythrocytes | Leukocytes Corrected for Nucleated Erythrocytes; Leuks Corrected for Nucl Erythrocytes | A measurement of the leukocytes corrected for nucleated erythrocytes in a biological specimen. |
| C147386 | Levetiracetam | Levetiracetam | A measurement of the levetiracetam in a biological specimen. |
| C184572 | Levorphanol | Levorphanol | A measurement of the levorphanol in a biological specimen. |
| C117748 | Lipase | Lipase; Total Lipase; Triacylglycerol Lipase | A measurement of the total triacylglycerol lipase in a biological specimen. |
| C117840 | Lipase, Gastric | Gastric Triacylglycerol Lipase; Lipase, Gastric; LIPF | A measurement of the gastric triacylglycerol lipase in a biological specimen. |
| C187808 | Lipase, Hepatic | Hepatic Triacylglycerol Lipase; Lipase, Hepatic; LIPH | A measurement of the hepatic triacylglycerol lipase in a biological specimen. |
| C117842 | Lipase, Lysosomal Acid | Acid Cholesteryl Ester Hydrolase; LAL; LIPA; Lipase, Lysosomal Acid; Lysosomal Lipase | A measurement of the lysosomal acid lipase in a biological specimen. |
| C117841 | Lipase, Pancreatic | Lipase, Pancreatic; Pancreatic Triacylglycerol Lipase; PNLIP | A measurement of the pancreatic triacylglycerol lipase in a biological specimen. |
| C111242 | Lipemic Index | Lipemia; Lipemic Index | A measurement of the abnormally high concentration of lipid in a biological specimen. |
| C74949 | Lipid | Lipid; Total Lipid | A measurement of the total lipids (cholesterol, lipoproteins, and triglycerides) in a biological specimen. |
| C125947 | Lipoarabinomannan | Lipoarabinomannan | A measurement of the lipoarabinomannan in a biological specimen. |
| C106539 | Lipocalin-2 | Lipocalin-2; Neutrophil Gelatinase-Associated Lipocalin; NGAL; Oncogene 24p3 | A measurement of lipocalin-2 in a biological specimen. |
| C106540 | Lipocalin-2/Creatinine | Lipocalin-2/Creatinine; Neutrophil Gelatinase-Associated Lipocalin/Creatinine; NGAL/Creatinine | A relative measurement (ratio or percentage) of the lipocalin-2 to creatinine present in a sample. |
| C120638 | Lipoprotein Associated Phospholipase A2 | Lipoprotein Associated Phospholipase A2 | A measurement of the lipoprotein associated phospholipase A2 in a biological specimen. |
| C174291 | Lipoprotein Lipase | Lipoprotein Lipase | A measurement of the lipoprotein lipase in a biological specimen. |
| C82022 | Lipoprotein-a | Lipoprotein-a | A measurement of the lipoprotein-a in a biological specimen. |
| C142284 | Liquefaction Time | Liquefaction Time | A measurement of the time it takes for a gelatinous or semi-solid substance to change to a liquid. |
| C189505 | Lithium | Lithium | A measurement of the lithium in a biological specimen. |
| C176240 | Lithocholate Compounds | Lithocholate Compounds; Lithocholic Acid Compounds | A measurement of the lithocholic acid, glycolithocholic acid, and taurolithocholic acid in a biological specimen. |
| C176307 | Lithocholate | Lithocholate; Lithocholic Acid | A measurement of the lithocholate in a biological specimen. |
| C147385 | Liver Fibrosis Score | Liver Fibrosis Score | A scoring system that evaluates liver pathology through the assessment of multiple blood test parameters, taking into account additional demographic factors such as the age and/or gender of the subject. |
| C96683 | Liver Kidney Microsomal Type 1 Antibody | Liver Kidney Microsomal Type 1 Antibody; LKM-1 | A measurement of the liver kidney microsomal type 1 antibody in a biological specimen. |
| C100456 | Liver Kidney Microsomal Type 1 IgA Ab | Liver Kidney Microsomal Type 1 IgA Ab | A measurement of the liver kidney microsomal type 1 IgA antibodies in a biological specimen. |
| C100454 | Liver Kidney Microsomal Type 1 IgG Ab | Liver Kidney Microsomal Type 1 IgG Ab | A measurement of the liver kidney microsomal type 1 IgG antibodies in a biological specimen. |
| C100455 | Liver Kidney Microsomal Type 1 IgM Ab | Liver Kidney Microsomal Type 1 IgM Ab | A measurement of the liver kidney microsomal type 1 IgM antibodies in a biological specimen. |
| C119267 | Liver Specific Alkaline Phosphatase | Liver Specific Alkaline Phosphatase | A measurement of the liver specific alkaline phosphatase isoform in a biological specimen. |
| C184621 | Loprazolam | Loprazolam | A measurement of the loprazolam in a biological specimen. |
| C75374 | Lorazepam | Lorazepam | A measurement of the lorazepam present in a biological specimen. |
| C184622 | Lormetazepam | Lormetazepam | A measurement of the lormetazepam in a biological specimen. |
| C116191 | Low Absorption Retic/Reticulocytes | Low Absorption Retic/Reticulocytes | A relative measurement (ratio or percentage) of the low absorption reticulocytes to total reticulocytes in a biological specimen. |
| C116190 | Low Absorption Reticulocytes | Low Absorption Reticulocytes | A measurement of the low absorption reticulocytes in a biological specimen. |
| C177977 | Loxapine | Loxapine | A measurement of the loxapine in a biological specimen. |
| C102277 | Lupus Anticoagulant Sensitive APTT | APTT-LA; Lupus Anticoagulant Sensitive APTT | A measurement of the length of time that it takes for clotting to occur when a lupus sensitive reagent is added to a plasma specimen. |
| C177963 | Lurasidone | Lurasidone | A measurement of the lurasidone in a biological specimen. |
| C74790 | Luteinizing Hormone | Luteinizing Hormone; Lutropin | A measurement of the luteinizing hormone in a biological specimen. |
| C102278 | Lymphoblasts | Lymphoblasts | A measurement of the lymphoblasts (immature cells that differentiate to form lymphocytes) in a biological specimen. |
| C105444 | Lymphoblasts/Leukocytes | Lymphoblasts/Leukocytes | A relative measurement (ratio or percentage) of the lymphoblasts to leukocytes in a biological specimen. |
| C189503 | Lymphoblasts/Lymphocytes | Lymphoblasts/Lymphocytes | A relative measurement (ratio or percentage) of the lymphoblasts to lymphocytes in a biological specimen. |
| C163463 | Lymphocyte Antigen 6E | Lymphocyte Antigen 6 Family Member E; Lymphocyte Antigen 6E | A measurement of the lymphocyte antigen 6E in a biological specimen. |
| C119289 | Lymphocytes Activated | Lymphocytes Activated | A measurement of the total activated lymphocytes in a biological specimen. |
| C64818 | Lymphocytes Atypical | Lymphocytes Atypical; Lymphocytes, Variant; Reactive Lymphocytes | A measurement of the atypical lymphocytes in a biological specimen. |
| C64819 | Lymphocytes Atypical/Leukocytes | Lymphocytes Atypical/Leukocytes; Lymphocytes, Variant/Leukocytes; Reactive Lymphocytes/Leukocytes | A relative measurement (ratio or percentage) of the atypical lymphocytes to leukocytes in a biological specimen. |
| C51949 | Lymphocytes | Lymphocytes | A measurement of the lymphocytes in a biological specimen. |
| C147387 | Lymphocytes, Clefted | Lymphocytes, Clefted | A measurement of the clefted lymphocytes in a biological specimen. |
| C147388 | Lymphocytes, Clefted/Leukocytes | Lymphocytes, Clefted/Leukocytes | A relative measurement (ratio or percentage) of the clefted lymphocytes to total leukocytes in a biological specimen. |
| C64820 | Lymphocytes/Leukocytes | Lymphocytes/Leukocytes | A relative measurement (ratio or percentage) of the lymphocytes to leukocytes in a biological specimen. |
| C186079 | Lymphocytes/Neutrophils | Lymphocytes/Neutrophils | A relative measurement (ratio) of lymphocytes to neutrophils in a biological specimen. |
| C135430 | Lymphocytes/Non-Squam Epi Cells | Lymphocytes/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the lymphocytes to non-squamous epithelial cells in a biological specimen. |
| C98751 | Lymphocytes/Total Cells | Lymphocytes/Total Cells | A relative measurement (ratio or percentage) of the lymphocytes to total cells in a biological specimen (for example a bone marrow specimen). |
| C139064 | Lymphoid Cells | Lymphoid Cells | A measurement of the total lymphoid lineage cells in a biological specimen. |
| C74613 | Lymphoma Cells | Lymphoma Cells | A measurement of the malignant lymphocytes in a biological specimen. |
| C147389 | Lymphoma Cells/Leukocytes | Lymphoma Cells/Leukocytes | A relative measurement (ratio or percentage) of the malignant lymphocytes to all leukocytes in a biological specimen. |
| C74910 | Lymphoma Cells/Lymphocytes | Lymphoma Cells/Lymphocytes | A relative measurement (ratio or percentage) of the malignant lymphocytes to all lymphocytes in a biological specimen. |
| C186078 | Lymphoma Cells/Total Cells | Lymphoma Cells/Total Cells | A relative measurement (ratio or percentage) of the lymphoma cells to total cells in a biological specimen. |
| C81955 | Lymphotactin | Chemokine Ligand 1; Lymphotactin | A measurement of the lymphotactin in a biological specimen. |
| C132375 | Lymphotoxin Alpha | Lymphotoxin Alpha; TNF-beta; Tumor Necrosis Factor Beta | A measurement of the lymphotoxin alpha in a biological specimen. |
| C75354 | Lysergic Acid Diethylamide | Acid; Lysergate Diethylamide; Lysergic Acid Diethylamide | A measurement of the lysergic acid diethylamine (LSD) in a biological specimen. |
| C122134 | Lysine | Lysine | A measurement of the lysine in a biological specimen. |
| C120640 | Lysozyme | Lysozyme | A measurement of lysozyme in a biological specimen. |
| C184550 | MAB-CHMINACA | MAB-CHMINACA | A measurement of the synthetic cannabinoid MAB-CHMINACA in a biological specimen. |
| C111243 | Macroamylase | Macroamylase | A measurement of macroamylase in a biological specimen. |
| C64821 | Macrocytes | Macrocytes | A measurement of the macrocytes in a biological specimen. |
| C80191 | Macrophage Colony Stimulating Factor | Macrophage Colony Stimulating Factor | A measurement of the macrophage colony stimulating factor in a biological specimen. |
| C82023 | Macrophage Inflammatory Protein 1 Alpha | Chemokine Ligand 3; Macrophage Inflammatory Protein 1 Alpha | A measurement of the macrophage inflammatory protein 1 alpha in a biological specimen. |
| C82024 | Macrophage Inflammatory Protein 1 Beta | Chemokine Ligand 4; Macrophage Inflammatory Protein 1 Beta | A measurement of the macrophage inflammatory protein 1 beta in a biological specimen. |
| C130164 | Macrophage Inflammatory Protein 1 Gamma | Macrophage Inflammatory Protein 1 Gamma | A measurement of the macrophage inflammatory protein 1 gamma in a biological specimen. |
| C163464 | Macrophage Inflammatory Protein 1 | Macrophage Inflammatory Protein 1 | A measurement of total macrophage inflammatory protein 1 in a biological specimen. |
| C163466 | Macrophage Migration Inhibitory Factor | Macrophage Migration Inhibitory Factor; MIF | A measurement of the macrophage migration inhibitory factor in a biological specimen. |
| C81956 | Macrophage-Derived Chemokine | C-C Motif Chemokine Ligand 22; CCL22; Chemokine (C-C Motif) Ligand 22; Chemokine Ligand 22; Macrophage-Derived Chemokine | A measurement of the macrophage-derived chemokine in a biological specimen. |
| C74798 | Macrophages | Macrophages | A measurement of the macrophages in a biological specimen. |
| C123460 | Macrophages/Leukocytes | Macrophages/Leukocytes | A relative measurement (ratio or percentage) of the macrophages to leukocytes in a biological specimen. |
| C135431 | Macrophages/Non-Squam Epi Cells | Macrophages/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the macrophages to non-squamous epithelial cells in a biological specimen. |
| C111244 | Macrophages/Total Cells | Macrophages/Total Cells | A relative measurement (ratio or percentage) of the macrophages to total cells in a biological specimen. |
| C147390 | Macroscopic Blood | Macroscopic Blood; Visible Blood | A measurement of the blood in body products such as a urine or stool sample, and visibly detectable on gross examination. |
| C64840 | Magnesium | Magnesium | A measurement of the magnesium in a biological specimen. |
| C175951 | Magnesium, Ionized | Magnesium, Ionized | A measurement of the ionized magnesium in a biological specimen. |
| C79456 | Magnesium/Creatinine | Magnesium/Creatinine | A relative measurement (ratio or percentage) of the magnesium to creatinine in a biological specimen. |
| C74660 | Malignant Cells, NOS | Malignant Cells, NOS | A measurement of the malignant cells of all types in a biological specimen. |
| C74643 | Malignant Cells, NOS/Blood Cells | Malignant Cells, NOS/Blood Cells | A relative measurement (ratio or percentage) of the malignant cells of all types to all blood cells in a biological specimen. |
| C187811 | Malondialdehyde | Malondialdehyde; MDA | A measurement of the malondialdehyde in a biological specimen. |
| C154742 | Mannitol | Mannitol | A measurement of the mannitol in a biological specimen. |
| C111246 | Mast Cells | Mast Cells; Mastocytes | A measurement of the mast cells in a biological specimen. |
| C187812 | Mast Cells/Leukocytes | Mast Cells/Leukocytes | A relative measurement (ratio or percentage) of mast cells to total leukocytes in a biological specimen. |
| C111247 | Mast Cells/Total Cells | Mast Cells/Total Cells | A relative measurement (ratio or percentage) of the mast cells to total cells in a biological specimen. |
| C80192 | Matrix Metalloproteinase 1 | Interstitial Collagenase; Matrix Metalloproteinase 1 | A measurement of the matrix metalloproteinase 1 in a biological specimen. |
| C80193 | Matrix Metalloproteinase 2 | Gelatinase A; Matrix Metalloproteinase 2 | A measurement of the matrix metalloproteinase 2 in a biological specimen. |
| C80194 | Matrix Metalloproteinase 3 | Matrix Metalloproteinase 3; Stromelysin 1 | A measurement of the matrix metalloproteinase 3 in a biological specimen. |
| C80195 | Matrix Metalloproteinase 7 | Matrilysin; Matrix Metalloproteinase 7 | A measurement of the matrix metalloproteinase 7 in a biological specimen. |
| C80196 | Matrix Metalloproteinase 8 | Matrix Metalloproteinase 8; Neutrophil Collagenase | A measurement of the matrix metalloproteinase 8 in a biological specimen. |
| C80197 | Matrix Metalloproteinase 9 | Gelatinase B; Matrix Metalloproteinase 9 | A measurement of the matrix metalloproteinase 9 in a biological specimen. |
| C74661 | Mature Plasma Cells | Mature Plasma Cells; Plasmacytes; Plasmocytes | A measurement of the mature plasma cells (plasmacytes) in a biological specimen. |
| C74911 | Mature Plasma Cells/Lymphocytes | Mature Plasma Cells/Lymphocytes | A relative measurement (ratio or percentage) of the mature plasma cells (plasmacytes) to all lymphocytes in a biological specimen. |
| C98869 | Mature Plasma Cells/Total Cells | Mature Plasma Cells/Total Cells | A relative measurement (ratio or percentage) of the mature plasma cells (plasmacytes) to total cells in a biological specimen (for example a bone marrow specimen). |
| C127628 | Maturing Erythroid Cells/Total Cells | Erythroid Precursors/Total Cells; Maturing Erythroid Cells/Total Cells; Maturing Erythroid/Total Cells; Total Erythroid Precursors/Total Cells | A relative measurement (ratio or percentage) of the maturing erythroid cells to total cells in a biological specimen. |
| C127629 | Maturing Myeloid Cells/Total Cells | Maturing Myeloid/Total Cells | A relative measurement (ratio or percentage) of the maturing myeloid cells to total cells in a biological specimen. |
| C74614 | May-Hegglin Anomaly | May-Hegglin Anomaly | A measurement of the May-Hegglin anomaly in a blood sample. This anomaly is characterized by large, misshapen platelets and the presence of Dohle bodies in leukocytes. |
| C184623 | Mazindol | Mazindol | A measurement of the mazindol in a biological specimen. |
| C114215 | MCV Reticulocytes | MCV Reticulocytes; MCVr; Mean Corpuscular Volume Reticulocytes | A measurement of the mean volume of reticulocytes in a biological specimen. |
| C96686 | Mean Platelet Component | Mean Platelet Component | A measurement of the mean platelet component (platelet activity) in a blood specimen. |
| C114214 | Mean Platelet Dry Mass | Mean Platelet Dry Mass | A measurement of the mean platelet dry mass in a biological specimen. |
| C74730 | Mean Platelet Volume | Mean Platelet Volume | A measurement of the average size of the platelets present in a blood sample. |
| C147391 | Meconium | Meconium | A measurement of the meconium in a biological specimen. |
| C139079 | Medazepam | Medazepam | A measurement of the medazepam present in a biological specimen. |
| C116193 | Medium Absorption Retic/Reticulocytes | Medium Absorption Retic/Reticulocytes | A relative measurement (ratio or percentage) of the medium absorption reticulocytes to total reticulocytes in a biological specimen. |
| C116192 | Medium Absorption Reticulocytes | Medium Absorption Reticulocytes | A measurement of the medium absorption reticulocytes in a biological specimen. |
| C184624 | Mefenorex | Mefenorex | A measurement of the mefenorex in a biological specimen. |
| C98752 | Megakaryoblasts | Megakaryoblasts | A measurement of the megakaryoblasts in a biological specimen. |
| C187813 | Megakaryoblasts/Leukocytes | Megakaryoblasts/Leukocytes | A relative measurement (ratio or percentage) of megakaryoblasts to total leukocytes in a biological specimen. |
| C98753 | Megakaryoblasts/Total Cells | Megakaryoblasts/Total Cells | A relative measurement (ratio or percentage) of the megakaryoblasts to total cells in a biological specimen (for example a bone marrow specimen). |
| C135432 | Megakaryocyte and Megakaryoblast Morph | Megakaryocyte and Megakaryoblast Morph; Megakaryocyte and Megakaryoblast Morphology | An examination or assessment of the form and structure of megakaryoblasts and megakaryocytes. |
| C96688 | Megakaryocytes | Megakaryocytes | A measurement of the megakaryocytes per unit of a biological specimen. |
| C154722 | Megakaryocytes/Leukocytes | Megakaryocytes/Leukocytes | A relative measurement (ratio or percentage) of the megakaryocytes to leukocytes in a biological specimen. |
| C98867 | Megakaryocytes/Total Cells | Megakaryocytes/Total Cells | A relative measurement (ratio or percentage) of the megakaryocytes to total cells in a biological specimen (for example a bone marrow specimen). |
| C74867 | Melatonin | Melatonin | A measurement of the melatonin hormone in a biological specimen. |
| C111250 | Meningeal Cells | Meningeal Cells | A measurement of the mengingeal cells in a biological specimen. |
| C111251 | Meningeal Cells/Total Cells | Meningeal Cells/Total Cells | A relative measurement (ratio or percentage) of the meningeal cells to total cells in a biological specimen. |
| C147392 | Meperidine | Meperidine | A measurement of the meperidine in a biological specimen. |
| C184551 | Mephedrone | Mephedrone | A measurement of the mephedrone in a biological specimen. |
| C184625 | Meprobamate | Meprobamate | A measurement of the meprobamate in a biological specimen. |
| C147393 | Mercury | Hg; Mercury | A measurement of the mercury in a biological specimen. |
| C75355 | Mescaline | 3,4,5-trimethoxyphenethylamine; Mescaline | A measurement of the mescaline in a biological specimen. |
| C177979 | Mesoridazine | Mesoridazine | A measurement of the mesoridazine in a biological specimen. |
| C147398 | Mesothelial Cells | Mesothelial Cells | A measurement of the mesothelial cells in a biological specimen. |
| C147399 | Mesothelial Cells/Leukocytes | Mesothelial Cells/Leukocytes | A relative measurement (ratio or percentage) of the mesothelial cells to total leukocytes in a biological specimen. |
| C184588 | Mesterolone | Mesterelone; Mesterolone | A measurement of the mesterolone in a biological specimen. |
| C74615 | Metamyelocytes | Metamyelocytes | A measurement of the metamyelocytes (small, myelocytic neutrophils with an indented nucleus) in a biological specimen. |
| C74645 | Metamyelocytes/Leukocytes | Metamyelocytes/Leukocytes | A relative measurement (ratio or percentage) of the metamyelocytes (small, myelocytic neutrophils with an indented nucleus) to all leukocytes in a biological specimen. |
| C98754 | Metamyelocytes/Total Cells | Metamyelocytes/Total Cells | A relative measurement (ratio or percentage ) of the metamyelocytes (small, myelocytic neutrophils with an indented nucleus) to total cells in a biological specimen (for example a bone marrow specimen). |
| C163468 | Metanephrine Excretion Rate | Metanephrine Excretion Rate | A measurement of the amount of metanephrine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C116198 | Metanephrine | Metadrenaline; Metanephrine | A measurement of the metanephrine in a biological specimen. |
| C177991 | Metanephrine+Normetanephrine Excr Rate | Metanephrine+Normetanephrine Excr Rate; Metanephrine+Normetanephrine Excretion Rate | A measurement of the amount of metanephrine and normetanephrine being excreted in a biological specimen over a defined amount of time (e.g., one hour). |
| C177990 | Metanephrine+Normetanephrine | Metanephrine+Normetanephrine | A measurement of the metanephrine and normetanephrine in a biological specimen. |
| C147400 | Metanephrine, Free | Metanephrine, Free | A measurement of the free metanephrine in a biological specimen. |
| C128972 | Metarubricyte | Acidophilic Erythroblast; Metarubricyte; Orthochromatophilic Normoblast; Orthochromic Erythroblast; Orthochromic Normoblast | A measurement of the metarubricytes in a biological specimen. |
| C128971 | Metarubricyte/Total Cells | Metarubricyte/Total Cells | A relative measurement (ratio or percentage) of the metarubricytes to total cells in a biological specimen. |
| C165974 | Metarubricytes/Leukocytes | Metarubricytes/Leukocytes | A relative measurement (ratio or percentage) of the metarubricytes to leukocytes in a biological specimen. |
| C74881 | Methadone | Methadone | A measurement of the methadone present in a biological specimen. |
| C75348 | Methamphetamine | Methamphetamine | A measurement of the methamphetamine drug present in a biological specimen. |
| C186080 | Methane | CH4; Methane | A measurement of the methane in a biological specimen. |
| C147394 | Methanol | Methanol | A measurement of the methanol in a biological specimen. |
| C74882 | Methaqualone | Methaqualone | A measurement of the methaqualone present in a biological specimen. |
| C184589 | Methasterone | Methasterone | A measurement of the methasterone in a biological specimen. |
| C184552 | Methcathinone | Ephedrone; Methcathinone | A measurement of the methcathinone in a biological specimen. |
| C96689 | Methemoglobin | Methemoglobin | A measurement of the methemoglobin in a biological specimen. |
| C147367 | Methemoglobin/Total Hemoglobin | FMET HB; Fractionated Methemoglobin; Methemoglobin/Total Hemoglobin | A relative measurement (ratio or percentage) of the amount of methemoglobin compared to total hemoglobin in a biological specimen. |
| C122238 | Methionine | Methionine | A measurement of the methionine in a biological specimen. |
| C184626 | Methohexital | Methohexital | A measurement of the methohexital in a biological specimen. |
| C96690 | Methylmalonic Acid | Methylmalonate; Methylmalonic Acid | A measurement of the methylmalonic acid in a biological specimen. |
| C170581 | Methylphenidate | Methylphenidate | A measurement of the methylphenidate in a biological specimen. |
| C75366 | Methylphenobarbital | Mephobarbital; Methylphenobarbital | A measurement of the methylphenobarbital in a biological specimen. |
| C184590 | Methyltestosterone | Methyltestosterone | A measurement of the methyltestosterone in a biological specimen. |
| C187814 | Methyltransferase | Methyltransferase | A measurement of the total methyltransferase in a biological specimen. |
| C184591 | Methyprylon | Methyprylon | A measurement of the methyprylon in a biological specimen. |
| C172502 | MHC Class I Chain Related Protein A | MHC Class I Chain Related Protein A | A measurement of the MHC class I chain related protein A in a biological specimen. |
| C64822 | Microcytes | Microcytes | A measurement of the microcytes in a biological specimen. |
| C116199 | Mid Cell Fraction | Mid Cell Fraction; Mid Cells | A measurement of the mid cell fraction, including eosinophils, basophils, monocytes and other precursor white blood cells, in a biological specimen. |
| C172523 | Mid-Reg Pro-Atrial Natriuretic Peptide | Mid-Reg Pro-Atrial Natriuretic Peptide; Mid-Regional Pro-Atrial Natriuretic Peptide; MR-proANP; MRproANP | A measurement of the mid-regional pro-atrial natriuretic peptide in a biological specimen. |
| C139083 | Midazolam | Midazolam | A measurement of the midazolam present in a biological specimen. |
| C187815 | Milnacipran | Milnacipran | A measurement of the milnacipran in a biological specimen. |
| C147395 | Mitochondrial M2 Antibody | Mitochondrial M2 Antibody | A measurement of the mitochondrial antibodies of M2 specificity in a biological specimen. |
| C163465 | Mitochondrial M2 IgG Antibody | Mitochondrial M2 IgG Antibody | A measurement of the mitochondrial IgG antibodies of M2 specificity in a biological specimen. |
| C165922 | Mixed Antigen IgE AB RAST Score | Mixed Antigen IgE Antibody RAST Score | A classification of the amount of mixed antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130100 | Mixed Antigen IgE Antibody | Mixed Antigen IgE Antibody | A measurement of the mixed antigen IgE antibody in a biological specimen. |
| C74771 | Mixed Casts | Mixed Casts | A measurement of the mixed (the cast contains a mixture of cell types) casts present in a biological specimen. |
| C16790 | Mixed Lymphocyte Reaction | Mixed Leukocyte Reaction; Mixed Lymphocyte Reaction | A measurement of the histocompatibility at the HL-A locus between two populations of lymphocytes taken from two separate individuals. |
| C184628 | Modafinil | Modafinil | A measurement of the modafinil in a biological specimen. |
| C130111 | Mold Mix Antigen IgA Antibody | Mold Mix Antigen IgA Antibody | A measurement of the mold mix antigen IgA antibody in a biological specimen. |
| C130109 | Mold Mix Antigen IgE Antibody | Mold Mix Antigen IgE Antibody | A measurement of the mold mix antigen IgE antibody in a biological specimen. |
| C130110 | Mold Mix Antigen IgG Antibody | Mold Mix Antigen IgG Antibody | A measurement of the mold mix antigen IgG antibody in a biological specimen. |
| C165926 | Mold Mix IgE AB RAST Score | Mold Mix IgE AB RAST Score | A classification of the amount of mold mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165907 | Mold Mix IgG AB RAST Score | Mold Mix IgG AB RAST Score | A classification of the amount of mold mix  IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C177981 | Molindone | Molindone | A measurement of the molindone in a biological specimen. |
| C74631 | Monoblasts | Monoblasts | A measurement of the monoblast cells in a biological specimen. |
| C74646 | Monoblasts/Leukocytes | Monoblasts/Leukocytes | A relative measurement (ratio or percentage) of the monoblasts to leukocytes in a biological specimen. |
| C187677 | Monoblasts/Total Cells | Monoblasts/Total Cells | A relative measurement (ratio or percentage) of the monoblasts to total cells in a biological specimen. |
| C186081 | Monoclonal Prot Immunoglobulin Isotype | Immunoglobulin Immunofixation Interpretation; Monoclonal Prot Immunoglobulin Isotype; Monoclonal Protein Immunoglobulin Class; Monoclonal Protein Immunoglobulin Isotype | The identification of the monoclonal protein immunoglobulin isotype in a biological specimen. |
| C163467 | Monoclonal Protein Excretion Rate | M Protein Excretion Rate; M-Spike Protein Excretion Rate; Monoclonal Protein Excretion Rate; Monoclonal Protein Spike Excretion Rate; Myeloma Protein Excretion Rate | A measurement of the amount of Monoclonal Protein being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C158218 | Monoclonal Protein Region | Monoclonal Protein Band Region; Monoclonal Protein Region; Monoclonal Protein Spike Region | The identification of the protein zone (e.g., alpha-1 globulin, beta globulin, etc.) within which the monoclonal protein is observed. |
| C92291 | Monoclonal Protein | Abnormal Gamma Protein Band; M Protein; M-Spike Paraprotein; M-Spike Protein; Monoclonal Immunoglobulin Protein; Monoclonal Protein; Monoclonal Protein Spike; Myeloma Protein; Paraprotein | A measurement of homogenous immunoglobulin resulting from the proliferation of a single clone of plasma cells in a biological specimen. |
| C147397 | Monoclonal Protein/Total Protein | M Protein/Total Protein; M-Spike Protein/Total Protein; Monoclonal Protein Spike/Total Protein; Monoclonal Protein/Total Protein; Myeloma Protein/Total Protein | A relative measurement (ratio or percentage) of the monoclonal protein to total protein in a biological specimen. |
| C82025 | Monocyte Chemotactic Protein 1 | CCL2; Chemokine (C-C Motif) Ligand 2; Monocyte Chemotactic Protein 1 | A measurement of the monocyte chemotactic protein 1 in a biological specimen. |
| C147396 | Monocytes and Macrophages/Leukocytes | Monocytes and Macrophages/Leukocytes | A relative measurement (ratio or percentage) of the monocytes and macrophages to total leukocytes in a biological specimen. |
| C64823 | Monocytes | Monocytes | A measurement of the monocytes in a biological specimen. |
| C64824 | Monocytes/Leukocytes | Monocytes/Leukocytes | A relative measurement (ratio or percentage) of the monocytes to leukocytes in a biological specimen. |
| C106544 | Monocytes/Macrocytes | Monocytes/Macrocytes | A relative measurement (ratio or percentage) of the monocytes to macrocytes present in a sample. |
| C135433 | Monocytes/Non-Squam Epi Cells | Monocytes/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the monocytes to non-squamous epithelial cells in a biological specimen. |
| C98872 | Monocytes/Total Cells | Monocytes/Total Cells | A relative measurement (ratio or percentage) of the monocytes to total cells in a biological specimen (for example a bone marrow specimen). |
| C111276 | Monocytoid Cells | Monocytoid Cells | A measurement of the monocytoid cells in a biological specimen. |
| C120641 | Monocytoid Cells/Leukocytes | Monocytoid Cells/Leukocytes | A relative measurement (ratio or percentage) of the monocytoid cells to leukocytes in a biological specimen. |
| C111277 | Monocytoid Cells/Total Cells | Monocytoid Cells/Total Cells | A relative measurement (ratio or percentage) of the monocytoid cells to total cells in a biological specimen. |
| C181407 | Monomethylarginine | Monomethylarginine; Tilarginine | A measurement of the monomethylarginine in a biological specimen. |
| C187790 | Mononuclear Cells Atypical | Mononuclear Cells Atypical | A measurement of the atypical mononuclear cells in a biological specimen. |
| C187791 | Mononuclear Cells Atypical/Leukocytes | Mononuclear Cells Atypical/Leukocytes | A relative measurement (ratio or percentage) of the atypical mononuclear cells to leukocytes in a biological specimen. |
| C154757 | Mononuclear Cells | Mononuclear Cells; Mononucleated Cells | A measurement of the mononuclear cells in a biological specimen. |
| C74681 | Monosodium Urate Crystals | Monosodium Urate Crystals; Sodium Urate Crystals | A measurement of the monosodium urate crystals present in a biological specimen. |
| C74883 | Morphine | Morphine | A measurement of the morphine present in a biological specimen. |
| C147433 | Motile Sperm/Total Sperm | Motile Sperm/Total Sperm | A relative measurement (ratio or percentage) of the motile sperm to total sperm in a biological specimen. |
| C79457 | Mu Glutathione-S-Transferase | Mu Glutathione-S-Transferase | A measurement of the mu form of glutathione S-transferase in a biological specimen. |
| C79458 | Mu Glutathione-S-Transferase/Creatinine | Mu Glutathione-S-Transferase/Creatinine | A relative measurement (ratio or percentage) of the mu gamma glutamyl transpeptidase to creatinine in a biological specimen. |
| C74721 | Mucous Threads | Mucous Threads | A measurement of the mucous threads present in a biological specimen. |
| C127630 | Murinoglobulin | Murinoglobulin | A measurement of the murinoglobulin in a biological specimen. |
| C103418 | Myelin Antibodies | Myelin Antibodies | A measurement of the myelin antibodies in a biological specimen. |
| C122135 | Myelin Basic Protein | Myelin Basic Protein | A measurement of the myelin basic protein in a biological specimen. |
| C74632 | Myeloblasts | Myeloblasts | A measurement of the myeloblast cells in a biological specimen. |
| C64825 | Myeloblasts/Leukocytes | Myeloblasts/Leukocytes | A relative measurement (ratio or percentage) of the myeloblasts to leukocytes in a biological specimen. |
| C98761 | Myeloblasts/Total Cells | Myeloblasts/Total Cells | A relative measurement (ratio or percentage) of the myeloblasts to total cells in a biological specimen (for example a bone marrow specimen). |
| C74662 | Myelocytes | Myelocytes | A measurement of the myelocytes in a biological specimen. |
| C64826 | Myelocytes/Leukocytes | Myelocytes/Leukocytes | A relative measurement (ratio or percentage) of the myelocytes to leukocytes in a biological specimen. |
| C98868 | Myelocytes/Total Cells | Myelocytes/Total Cells | A relative measurement (ratio or percentage) of the myelocytes to total cells in a biological specimen (for example a bone marrow specimen). |
| C135434 | Myeloid Maturation Index | Myeloid Maturation Index | A relative measurement (ratio) of the sum of myeloid maturation phase cells (pool) to the sum of myeloid proliferative phase cells (pool) in a biological specimen. |
| C135435 | Myeloid Maturation Pool | Myeloid Maturation Pool | A measurement of the myeloid maturation phase cells (metamyelocytes, band neutrophils, and segmented neutrophils) in a biological specimen. |
| C130165 | Myeloid Progenitor Cells | Myeloid Progenitor Cells | A measurement of the myeloid progenitor cells in a biological specimen. |
| C186084 | Myeloid Progenitor Cells/Total Cells | Myeloid Progenitor Cells/Total Cells | A relative measurement (ratio or percentage) of the myeloid progenitor cells to total cells in a biological specimen. |
| C135436 | Myeloid Proliferation Index | Myeloid Proliferation Index | A relative measurement (ratio) of the sum of myeloid proliferative phase cells (pool) to the sum of myeloid maturation phase cells (pool) in a biological specimen. |
| C135437 | Myeloid Proliferation Pool | Myeloid Proliferation Pool | A measurement of the myeloid proliferative phase cells (myeloblasts, promyelocytes, and myelocytes) in a biological specimen. |
| C92242 | Myeloid/Erythroid Ratio | Myeloid/Erythroid Ratio | A relative measurement of myeloid progenitor cells to erythrocyte precursor cells in a biological specimen. |
| C92280 | Myeloperoxidase Antibody | Myeloperoxidase Antibody | A measurement of the myeloperoxidase antibody in a biological specimen. |
| C119290 | Myeloperoxidase Index | Myeloperoxidase Index | The mean peroxidase activity index or staining intensity of the neutrophil population relative to the archetype. |
| C80198 | Myeloperoxidase | Myeloperoxidase | A measurement of the myeloperoxidase in a biological specimen. |
| C79436 | Myoglobin | Myoglobin | A measurement of myoglobin in a biological specimen. |
| C106546 | Myoglobin/Creatinine | Myoglobin/Creatinine | A relative measurement (ratio or percentage) of the myoglobin to creatinine present in a sample. |
| C106547 | Myosin Light Chain 3 | Cardiac myosin light chain 1; Myosin light chain 1, slow-twitch muscle B/ventricular isoform; Myosin Light Chain 3 | A measurement of myosin light chain 3 in a biological specimen. |
| C184536 | N,N-Dimethyltryptamine | Dimethyltryptamine; DMT; N,N-Dimethyltryptamine | A measurement of the N,N-dimethyltryptamine in a biological specimen. |
| C79459 | N-Acetyl Glucosamide | N-Acetyl Glucosamide; N-Acetyl Glucosamine | A measurement of N-acetyl glucosamide (sugar derivative) in a biological specimen. |
| C79460 | N-Acetyl Glucosamide/Creatinine | N-Acetyl Glucosamide/Creatinine | A relative measurement (ratio or percentage) of the N-acetyl glucosamide to creatinine in a biological specimen. |
| C163470 | N-acetyl-B-D-glucosaminidase/Creatinine | N-acetyl-B-D-glucosaminidase/Creatinine | A relative measurement (ratio or percentage) of the N-acetyl-beta-D-glucosaminidase to creatinine in a biological specimen. |
| C103419 | N-acetyl-beta-D-glucosaminidase | Beta-N-acetyl-D-glucosaminidase; N-acetyl-beta-D-glucosaminidase | A measurement of the N-acetyl-beta-D-glucosaminidase (enzyme) in a biological specimen. |
| C163471 | N-Demethylase | N-Demethylase | A measurement of the N-Demethylase in a biological specimen. |
| C177967 | N-Desmethylolanzapine | Desmethylolanzapine; DMO; N-Desmethylolanzapine; Norolanzapine | A measurement of the N-desmethylolanzapine in a biological specimen. |
| C181403 | N-Desmethyltramadol | N-Desmethyltramadol; N-DSMT | A measurement of the N-desmethyltramadol in a biological specimen. |
| C147404 | N-methylhistamine | N-methylhistamine | A measurement of the N-methylhistamine in a biological specimen. |
| C74743 | N-telopeptide | N-telopeptide | A measurement of the N-telopeptide in a biological specimen. |
| C120645 | N-telopeptide/Creatinine | N-telopeptide/Creatinine | A relative measurement (ratio or percentage) of the N-telopeptide to creatinine in a biological specimen. |
| C139088 | N-Terminal ProA-type Natriuretic Peptide | N-terminal pro-Atrial Natriuretic Peptide; N-Terminal ProA-type Natriuretic Peptide; NT proANP II | A measurement of the N-terminal proA-type natriuretic peptide in a biological specimen. |
| C96610 | N-Terminal ProB-type Natriuretic Peptide | N-terminal pro-Brain Natriuretic Peptide; N-Terminal ProB-type Natriuretic Peptide; NT proBNP II | A measurement of the N-terminal proB-type natriuretic peptide in a biological specimen. |
| C165975 | NAGASE Excretion Rate | N-acetyl-beta-D-glucosaminidase Excretion Rate; NAGASE Excretion Rate | A measurement of the amount of N-acetyl-beta-D-glucosaminidase being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C184592 | Nalorphine | Allorphine; Antorphine; N-allylnormorphine; Nalorphine | A measurement of the nalorphine in a biological specimen. |
| C75377 | Nandrolone | Nandrolone; Norandrostenolone; Nortestosterone | A measurement of the nandrolone in a biological specimen. |
| C184553 | Naphyrone | Naphyrone | A measurement of the naphyrone in a biological specimen. |
| C116203 | Natural Killer Cell Function | Natural Killer Cell Activity; Natural Killer Cell Function | A measurement of the natural killer cell function in a biological specimen. |
| C98762 | Natural Killer Cells | Natural Killer Cells | A measurement of the total natural killer cells in a biological specimen. |
| C172494 | Neoplastic Plasma Cells | Clonal Plasma Cells; Monoclonal Plasma Cells; Monotypic Plasma Cells; Neoplastic Plasma Cells | A measurement of the neoplastic plasma cells in a biological specimen. |
| C80199 | Neopterin | Neopterin | A measurement of the neopterin in a biological specimen. |
| C184645 | Nephrin | Nephrin; NPHS1 Adhesion Molecule, Nephrin | A measurement of the nephrin in a biological specimen. |
| C135439 | Nerve Growth Factor | Nerve Growth Factor | A measurement of the nerve growth factor in a biological specimen. |
| C142285 | Neurofilament Light Chain Protein | NEFL; Neurofilament Light Chain Protein; Neurofilament Light Polypeptide; NF-L; Protein Phosphatase 1, Regulatory Subunit 110 | A measurement of the neurofilament light chain protein in a biological specimen. |
| C163473 | Neurokinin A | Neurokinin A; NKA; Substance K | A measurement of the neurokinin A in a biological specimen. |
| C116205 | Neuron Specific Enolase | Enolase 2; Gamma-enolase; Neuron Specific Enolase | A measurement of the neuron specific enolase in a biological specimen. |
| C74892 | Neuropeptide Y | Neuropeptide Y | A measurement of the neuropeptide Y in a biological specimen. |
| C165977 | Neuropilin-1 | BDCA4; CD304; Neuropilin-1; NP1; NRP; VEGF165R | A measurement of the neuropilin-1 in a biological specimen. |
| C163475 | Neurotensin | Neurotensin; NTS | A measurement of the neurotensin in a biological specimen. |
| C147407 | Neutral Fats | Neutral Fats | A measurement of the total neutral fats in a biological specimen. |
| C147300 | Neutrophil Cytoplasmic Ab, Atypical | Anti-Neutrophil Cytoplasmic Antibody, Atypical; Neutrophil Cytoplasmic Ab, Atypical | A measurement of the atypical (cytoplasmic staining usually uniform and no interlobular accentuation) neutrophil cytoplasmic antibodies in a biological specimen. |
| C147301 | Neutrophil Cytoplasmic Ab, Classic | Anti-Neutrophil Cytoplasmic Antibody, Classic; Neutrophil Cytoplasmic Ab, Classic | A measurement of the classic (cytoplasmic granular fluorescence with central interlobular accentuation) neutrophil cytoplasmic antibodies in a biological specimen. |
| C147302 | Neutrophil Cytoplasmic Ab, Perinuclear | Anti-Neutrophil Cytoplasmic Antibody, Perinuclear; Neutrophil Cytoplasmic Ab, Perinuclear | A measurement of the perinuclear (perinuclear staining without nuclear extension) neutrophil cytoplasmic antibodies in a biological specimen. |
| C82026 | Neutrophil Elastase | Neutrophil Elastase | A measurement of the neutrophil elastase in a biological specimen. |
| C82027 | Neutrophil Elastase, Polymorphonuclear | Neutrophil Elastase, Polymorphonuclear | A measurement of the polymorphonuclear neutrophil elastase in a biological specimen. |
| C84822 | Neutrophilic Metamyelocytes | Neutrophilic Metamyelocytes | A measurement of the neutrophilic metamyelocytes in a biological specimen. |
| C189509 | Neutrophilic Metamyelocytes/Total Cells | Neutrophilic Metamyelocytes/Total Cells | A relative measurement (ratio or percentage) of the neutrophilic metamyelocytes to total cells in a biological specimen. |
| C84823 | Neutrophilic Myelocytes | Neutrophilic Myelocytes | A measurement of the neutrophilic myelocytes in a biological specimen. |
| C181450 | Neutrophilic Myelocytes/Lymphocytes | Neutrophilic Myelocytes/Lymphocytes | A relative measurement (ratio or percentage) of the neutrophilic myelocytes to lymphocytes in a biological specimen (for example a bone marrow specimen). |
| C132376 | Neutrophilic Toxic Change | Neutrophilic Toxic Change | A measurement of any type of toxic change in cells of the neutrophilic lineage in a biological specimen. |
| C64830 | Neutrophils Band Form | Neutrophils Band Form | A measurement of the banded neutrophils in a biological specimen. |
| C120642 | Neutrophils Band Form/ Neutrophils | Neutrophils Band Form/ Neutrophils | A relative measurement (ratio or percentage) of banded neutrophils to total neutrophils in a biological specimen. |
| C64831 | Neutrophils Band Form/Leukocytes | Neutrophils Band Form/Leukocytes | A relative measurement (ratio or percentage) of the banded neutrophils to leukocytes in a biological specimen. |
| C187701 | Neutrophils Band Form/Total Cells | Neutrophils Band Form/Total Cells | A relative measurement (ratio or percentage) of the banded neutrophils to total cells in a biological specimen. |
| C63321 | Neutrophils | Neutrophils | A measurement of the neutrophils in a biological specimen. |
| C154756 | Neutrophils, Seg + Band Form + Precursor | Neutrophils, Seg + Band Form + Precursor; Neutrophils, Segmented + Band Form + Precursors | A measurement of the segmented and band form neutrophils, metamyelocytes, myelocytes, promyelocytes, and myeloblasts in a biological specimen. |
| C154755 | Neutrophils, Segmented + Band Form | Neutrophils, Segmented + Band Form | A measurement of the segmented and band form neutrophils in a biological specimen. |
| C81997 | Neutrophils, Segmented | Neutrophils, Segmented | A measurement of the segmented neutrophils in a biological specimen. |
| C82045 | Neutrophils, Segmented/Leukocytes | Neutrophils, Segmented/Leukocytes | A relative measurement (ratio or percentage) of segmented neutrophils to leukocytes in a biological specimen. |
| C120643 | Neutrophils, Segmented/Neutrophils | Neutrophils, Segmented/Neutrophils | A relative measurement (ratio or percentage) of segmented neutrophils to total neutrophils in a biological specimen. |
| C187679 | Neutrophils, Segmented/Total Cells | Neutrophils, Segmented/Total Cells | A relative measurement (ratio or percentage) of segmented neutrophils to total cells in a biological specimen. |
| C64827 | Neutrophils/Leukocytes | Neutrophils/Leukocytes | A relative measurement (ratio or percentage) of the neutrophils to leukocytes in a biological specimen. |
| C141271 | Neutrophils/Lymphocytes | Neutrophils/Lymphocytes | A relative measurement (ratio) of the neutrophils to lymphocytes in a biological specimen. |
| C135438 | Neutrophils/Non-Squam Epi Cells | Neutrophils/Non-Squam Epi Cells | A relative measurement (ratio or percentage) of the neutrophils to non-squamous epithelial cells in a biological specimen. |
| C98763 | Neutrophils/Total Cells | Neutrophils/Total Cells | A relative measurement (ratio or percentage) of the neutrophils to total cells in a biological specimen (for example a bone marrow specimen). |
| C74899 | Niacin | Niacin; Vitamin B3 | A measurement of the niacin in a biological specimen. |
| C184556 | Nicomorphine | Nicomorphine | A measurement of the nicomorphine in a biological specimen. |
| C147403 | Nicotine | Nicotine | A measurement of the nicotine in a biological specimen. |
| C161352 | Nitrate | Nitrate; Nitric Acid | A measurement of the nitrate in a biological specimen. |
| C186089 | Nitrazepam and/or Metabolites | Nitrazepam and/or Metabolites | A measurement of the nitrazepam and/or its metabolite(s) present in a biological specimen, for an assay that can measure both nitrazepam and its metabolites. |
| C184629 | Nitrazepam | Nitrazepam | A measurement of the nitrazepam in a biological specimen. |
| C112360 | Nitric Oxide | Nitric Oxide; NO | A measurement of the nitric oxide in a biological specimen. |
| C64810 | Nitrite | Nitrite | A measurement of the nitrite in a biological specimen. |
| C181258 | NK Cells/Lym | Natural Killer Cells/Lymphocytes; NK Cells/Lym | A relative measurement (ratio or percentage) of the natural killer cells to lymphocytes in a biological specimen. |
| C154744 | Nociceptin | Nociceptin; Orphanin FQ | A measurement of the nociceptin in a biological specimen. |
| C116204 | Non-HDL Cholesterol | Non-HDL Cholesterol; Non-High Density Lipoprotein | A measurement of the non-high density lipoprotein cholesterol in a biological specimen. |
| C120644 | Non-HDL Cholesterol/HDL Cholesterol | Non-HDL Cholesterol/HDL Cholesterol | A relative measurement (ratio or percentage) of non-high density lipoprotein cholesterol to high density lipoprotein cholesterol in a biological specimen. |
| C186085 | Non-HDL Cholesterol/LDL Cholesterol | Non-HDL Cholesterol/LDL Cholesterol | A relative measurement (ratio or percentage) of the non-HDL cholesterol to LDL cholesterol in a biological specimen. |
| C84811 | Non-Phosphorylated Tau Protein | Non-Phosphorylated Tau Protein | A measurement of the non-phosphorylated Tau protein in a biological specimen. |
| C100434 | Non-Prostatic Acid Phosphatase | Non-Prostatic Acid Phosphatase | A measurement of the non-prostatic acid phosphatase in a biological specimen. |
| C135413 | Non-Squamous Epithelial Cells | Non-Squamous Epithelial Cells | A measurement of the non-squamous epithelial cells in a biological specimen. |
| C147401 | Nonhematic Cells | Nonhematic Cells | A measurement of the cells of nonhematopoietic origin in a biological specimen. |
| C147402 | Nonhematic Cells/Leukocytes | Nonhematic Cells/Leukocytes | A relative measurement (ratio) of the nonhematic cells to total leukocytes in a biological specimen. |
| C184593 | Norclostebol | Norclostebol | A measurement of the norclostebol in a biological specimen. |
| C139076 | Nordazepam | Desmethyldiazepam; N-Desmethyldiazepam; Nordazepam; Nordiazepam | A measurement of the nordazepam present in a biological specimen. |
| C163472 | Norepinephrine Excretion Rate | Norepinephrine Excretion Rate | A measurement of the amount of norepinephrine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C74868 | Norepinephrine | Noradrenaline; Norepinephrine | A measurement of the norepinephrine hormone in a biological specimen. |
| C184594 | Norethandrolone | Norethandrolone | A measurement of the norethandrolone in a biological specimen. |
| C187816 | Norfluoxetine | Norfluoxetine | A measurement of the norfluoxetine in a biological specimen. |
| C177952 | Norhydrocodone | Norhydrocodone | A measurement of the norhydrocodone in a biological specimen. |
| C142286 | Normal Sperm/Total Sperm | Normal Sperm/Total Sperm; Sperm Morphology | A measurement (ratio or percentage) of the normal spermatozoa to total spermatozoa in a biological specimen. |
| C163474 | Normetanephrine Excretion Rate | Normetanephrine Excretion Rate | A measurement of the amount of normetanephrine being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C122138 | Normetanephrine | Normetanephrine | A measurement of the normetanephrine in a biological specimen. |
| C186086 | Normetanephrine, Free | Normetanephrine, Free | A measurement of the free normetanephrine in a biological specimen. |
| C189501 | Normoblasts | Normoblasts | A measurement of the normoblasts in a biological specimen. |
| C98764 | Normoblasts/Total Cells | Normoblasts/Total Cells | A relative measurement (ratio or percentage) of the normoblasts to total cells in a biological specimen (for example a bone marrow specimen). |
| C184557 | Normorphine | Normorphine | A measurement of the normorphine in a biological specimen. |
| C147406 | Nornicotine | Nornicotine | A measurement of the nornicotine in a biological specimen. |
| C177953 | Noroxycodone | Noroxycodone | A measurement of the noroxycodone in a biological specimen. |
| C186088 | Norpropoxyphene | Norpropoxyphene | A measurement of the norpropoxyphene in a biological specimen. |
| C187817 | Norsertraline | Norsertraline | A measurement of the norsertraline in a biological specimen. |
| C186087 | Nortriptyline | Nortriptyline | A measurement of the nortriptyline in a biological specimen. |
| C156509 | Nuclear Matrix Protein 22 | Nuclear Matrix Protein 22; Nuclear Mitotic Apparatus Protein 1; NUMA1 | A measurement of the nuclear matrix protein 22 in a biological specimen. |
| C114213 | Nuclear Swelling | Nuclear Swelling | A measurement of the expansion of the nucleus of the cells in a biological specimen. |
| C150841 | Nucleated Cells | Nucleated Cells | A measurement of the nucleated cells in a biological specimen. |
| C74705 | Nucleated Erythrocytes | Nucleated Erythrocytes; Nucleated Red Blood Cells | A measurement of the nucleated erythrocytes (large, immature nucleated erythrocytes) in a biological specimen. |
| C74647 | Nucleated Erythrocytes/Erythrocytes | Nucleated Erythrocytes/Erythrocytes; Nucleated Red Blood Cells/Erythrocytes | A relative measurement (ratio or percentage) of the nucleated erythrocytes (large, immature nucleated erythrocytes) to all erythrocytes in a biological specimen. |
| C82046 | Nucleated Erythrocytes/Leukocytes | Nucleated Erythrocytes/Leukocytes | A relative measurement (ratio or percentage) of nucleated erythrocytes to leukocytes in a biological specimen. |
| C130122 | Nut Mix Antigen IgE Antibody | Nut Mix Antigen IgE Antibody | A measurement of the nut mix antigen IgE antibody in a biological specimen. |
| C130123 | Nut Mix Antigen IgG Antibody | Nut Mix Antigen IgG Antibody | A measurement of the nut mix antigen IgG antibody in a biological specimen. |
| C165931 | Nut Mix IgE AB RAST Score | Nut Mix IgE AB RAST Score | A classification of the amount of nut mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165913 | Nut Mix IgG AB RAST Score | Nut Mix IgG AB RAST Score | A classification of the amount of nut mix IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C163479 | O-Demethylase | O-Demethylase | A measurement of the O-Demethylase in a biological specimen. |
| C181402 | O-Desmethyltramadol | Desmetramadol; O-Desmethyltramadol; O-DSMT | A measurement of the O-desmethyltramadol in a biological specimen. |
| C74686 | Occult Blood | Occult Blood | A measurement of the blood in body products such as a urine or stool sample, not detectable on gross examination. |
| C177966 | Olanzapine | Olanzapine | A measurement of the olanzapine in a biological specimen. |
| C122139 | Oligoclonal Bands | Oligoclonal Bands | A measurement of the oligoclonal bands in a biological specimen. |
| C165885 | Olive Tree Pollen IgE AB RAST Score | Olive Tree Pollen IgE AB RAST Score | A classification of the amount of Olea europaea pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165884 | Olive Tree Pollen IgE Antibody | Olive Tree Pollen IgE Antibody | A measurement of the Olea europaea pollen antigen IgE antibody in a biological specimen. |
| C132377 | Oncostatin M | Oncostatin M | A measurement of the oncostatin M in a biological specimen. |
| C74796 | Opiate | Opiate | A measurement of any opiate class drug present in a biological specimen. |
| C130081 | Orchard Grass Pollen IgA | Cocksfoot Grass Pollen IgA; Orchard Grass Pollen IgA | A measurement of the Dactylis glomerata pollen antigen IgA antibody in a biological specimen. |
| C165883 | Orchard Grass Pollen IgE AB RAST Score | Orchard Grass Pollen IgE AB RAST Score | A classification of the amount of Dactylis glomerata pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130080 | Orchard Grass Pollen IgE | Cocksfoot Grass Pollen IgE; Orchard Grass Pollen IgE | A measurement of the Dactylis glomerata pollen antigen IgE antibody in a biological specimen. |
| C165900 | Orchard Grass Pollen IgG AB RAST Score | Cocksfoot Grass Pollen IgG RAST Score; Orchard Grass Pollen IgG AB RAST Score | A classification of the amount of Dactylis glomerata pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130082 | Orchard Grass Pollen IgG | Cocksfoot Grass Pollen IgG; Orchard Grass Pollen IgG | A measurement of the Dactylis glomerata pollen antigen IgG antibody in a biological specimen. |
| C130083 | Orchard Grass Pollen IgG4 | Cocksfoot Grass Pollen IgG4; Orchard Grass Pollen IgG4 | A measurement of the Dactylis glomerata pollen antigen IgG4 antibody in a biological specimen. |
| C122140 | Ornithine | Ornithine | A measurement of the ornithine in a biological specimen. |
| C74801 | Osmolality | Osmolality | A measurement of the osmoles of solute per unit of biological specimen. |
| C74802 | Osmolarity | Osmolarity | A measurement of the osmoles of solute per liter of solution. |
| C74744 | Osteocalcin | Osteocalcin | A measurement of the osteocalcin in a biological specimen. |
| C124349 | Osteopontin | Osteopontin | A measurement of the osteopontin in a biological specimen. |
| C177962 | Osteopontin/Creatinine | Osteopontin/Creatinine | A relative measurement (ratio or percentage) of the osteopontin to creatinine in a biological specimen. |
| C116206 | Osteoprotegerin | OCIF; Osteoclastogenesis Inhibitory Factor; Osteoprotegerin; TNFRS11B; Tumor Necrosis Factor Receptor Superfamily Member 11b | A measurement of the osteoprotegerin in a biological specimen. |
| C142287 | Ovalocytes | Ovalocytes | A measurement of the ovalocytes (oval shaped cell with rounded ends and a long axis less than twice its short axis) in a biological specimen. |
| C163480 | Oxalate Excretion Rate | Oxalate Excretion Rate | A measurement of the amount of oxalate being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C92250 | Oxalate | Ethanedioate; Oxalate | A measurement of the oxalate in a biological specimen. |
| C117983 | Oxalate/Creatinine | Oxalate/Creatinine | A relative measurement (ratio or percentage) of the oxalate to creatinine in a biological specimen. |
| C75381 | Oxandrolone | Ossandrolone; Oxandrolone | A measurement of the oxandrolone in a biological specimen. |
| C75375 | Oxazepam | Oxazepam | A measurement of the oxazepam present in a biological specimen. |
| C119288 | Oxidized LDL Cholesterol Antibody | Oxidized LDL Cholesterol Antibody | A measurement of the total oxidized low density lipoprotein cholesterol antibody in a biological specimen. |
| C120635 | Oxidized LDL Cholesterol | Oxidized LDL Cholesterol | A measurement of the oxidized low density lipoprotein cholesterol in a biological specimen. |
| C74884 | Oxycodone | Oxycodone; Oxycontin | A measurement of the oxycodone present in a biological specimen. |
| C96614 | Oxygen Capacity | Oxygen Capacity | A measurement of the maximum amount of oxygen that can be combined chemically with hemoglobin in a volume of blood. |
| C111284 | Oxygen Content | Oxygen Content | A measurement of the amount of oxygen content in a biological specimen. |
| C60832 | Oxygen Saturation | Oxygen Saturation | A measurement of the oxygen-hemoglobin saturation of a volume of blood. |
| C174311 | Oxygen Saturation/Fraction Inspired O2 | Oxygen Saturation/Fraction Inspired O2 | A relative measurement (ratio or percentage) of the oxygen-hemoglobin saturation of a volume of blood to the volumetric fraction of oxygen in the inhaled gas. |
| C96616 | Oxyhemoglobin | Oxyhemoglobin | A measurement of the oxyhemoglobin, oxygen-bound hemoglobin, in a biological specimen. |
| C147359 | Oxyhemoglobin/Total Hemoglobin | FO2 Hb; Fractioned Oxyhemoglobin; Oxyhemoglobin/Total Hemoglobin | A relative measurement (ratio or percentage) of the amount of oxyhemoglobin compared to total hemoglobin in a biological specimen. |
| C184595 | Oxymesterone | Oxymesterone | A measurement of the oxymesterone in a biological specimen. |
| C75388 | Oxymetholone | Oxymethalone; Oxymethenolone; Oxymetholone | A measurement of the oxymetholone in a biological specimen. |
| C147409 | Oxymorphone | Oxymorphone | A measurement of the Oxymorphone in a biological specimen. |
| C74869 | Oxytocin | Oxytocin; Oxytoxin | A measurement of the oxytocin hormone in a biological specimen. |
| C117850 | P-Selectin | GMP-140; P-Selectin | A measurement of total P-selectin in a biological specimen. |
| C120651 | P100 Polymyositis-scleroderma Autoag Ab | P100 Polymyositis-scleroderma Autoag Ab | A measurement of the p100 polymyositis-scleroderma overlap syndrome-associated autoantigen antibody in a biological specimen. |
| C102279 | P50 Oxygen | P50 Oxygen | A measurement of the partial pressure of oxygen when hemoglobin is half saturated in a biological specimen. |
| C82028 | Pancreatic Elastase 1 | Pancreatic Elastase 1 | A measurement of the pancreatic elastase 1 in a biological specimen. |
| C82029 | Pancreatic Elastase 1, Polymorphonuclear | Pancreatic Elastase 1, Polymorphonuclear | A measurement of the polymorphonuclear pancreatic elastase 1 in a biological specimen. |
| C80201 | Pancreatic Polypeptide | Pancreatic Polypeptide | A measurement of the pancreatic polypeptide in a biological specimen. |
| C116210 | Panel Reactive Antibody | Panel Reactive Antibody; Percent Reactive Antibody; PRA Score | A measurement of the panel reactive antibody that is achieved by mixing and assessing the reactivity between the recipient's immune cells and the donor's human leukocyte antigen, in which anti-HLA class I and class II antibody specificities are measured separately in a biological specimen. |
| C74616 | Pappenheimer Bodies | Pappenheimer Bodies | A measurement of the cells containing Pappenheimer Bodies (violet or blue staining ferritin granules usually found along the periphery of the red blood cells) in a biological specimen. |
| C189530 | Para Aminohippurate Clearance | 4-Aminohippurate Clearance; P-Amino Hippuric Acid Clearance; P-Aminohippurate Clearance; PAH Clearance; Para Aminohippurate Clearance; Para Aminohippuric Acid Clearance; Para-Amino Hippuric Acid Clearance; Para-Aminohippurate Clearance | A measurement of the volume of serum or plasma that would be cleared of para aminohippurate by excretion of urine for a specified unit of time (e.g. one minute). |
| C189315 | Para Aminohippurate | 4-Aminohippurate; P-Amino Hippuric Acid; P-Aminohippurate; PAH; Para Aminohippurate; Para Aminohippuric Acid; Para-Amino Hippuric Acid; Para-Aminohippurate | A measurement of the para aminohippurate in a biological specimen. |
| C186090 | Para-Aminobenzoate | Para-Aminobenzoate; Para-Aminobenzoic Acid | A measurement of the para-aminobenzoate in a biological specimen. |
| C184558 | Para-Fluorofentanyl | Para-Fluorofentanyl | A measurement of the para-fluorofentanyl in a biological specimen. |
| C184630 | Paraldehyde | Paraldehyde | A measurement of the paraldehyde in a biological specimen. |
| C81964 | Parathyroid Hormone, C-Terminal | Parathyrin Hormone, C-Terminal; Parathyroid Hormone, C-Terminal | A measurement of the C-terminal fragment of parathyroid hormone in a biological specimen. |
| C74784 | Parathyroid Hormone, Fragmented | Parathyrin Hormone, Fragmented; Parathyroid Hormone, Fragmented | A measurement of the fragmented parathyroid hormone in a biological specimen. |
| C74789 | Parathyroid Hormone, Intact | Parathyrin, Intact; Parathyroid Hormone, Intact | A measurement of the intact parathyroid hormone (consisting of amino acids 1-84 or 7-84) in a biological specimen. |
| C81965 | Parathyroid Hormone, Mid-Molecule | Parathyrin Hormone, Mid-Molecule; Parathyroid Hormone, Mid-Molecule | A measurement of the mid-molecule fragment of parathyroid hormone in a biological specimen. |
| C81966 | Parathyroid Hormone, N-Terminal | Parathyrin Hormone, N-Terminal; Parathyroid Hormone, N-Terminal | A measurement of the N-terminal fragment of parathyroid hormone in a biological specimen. |
| C103451 | Parathyroid Hormone, Whole | Parathyrin Hormone, Whole; Parathyroid Hormone, Whole | A measurement of the whole parathyroid hormone (consisting of amino acids 1-84) in a biological specimen. |
| C117851 | Parathyroid Hormone-related Protein | Parathyrin Hormone-related Protein; Parathyroid Hormone-related Peptide; Parathyroid Hormone-related Protein | A measurement of parathyroid hormone-related protein in a biological specimen. |
| C116207 | Parietal Cell Antibody | Anti-Parietal Cell Antibody; Parietal Cell Antibody | A measurement of the parietal cell antibody in a biological specimen. |
| C147410 | Paroxetine | Paroxetine | A measurement of the paroxetine present in a biological specimen. |
| C147411 | Partial Pressure Carbon Dioxide Adj Temp | Partial Pressure Carbon Dioxide Adj Temp | A measurement of the pressure of carbon dioxide, which has been adjusted for body temperature, in a biological specimen. |
| C82625 | Partial Pressure Carbon Dioxide | Partial Pressure Carbon Dioxide | A measurement of the pressure of carbon dioxide in a biological specimen. |
| C147417 | Partial Pressure Oxygen Adj for Temp | Partial Pressure Oxygen Adj for Temp | A measurement of the pressure of oxygen, which has been adjusted for body temperature, in a biological specimen. |
| C71251 | Partial Pressure Oxygen | PaO2; Partial Pressure Oxygen; Po2; pO2 | A measurement of the pressure of oxygen in a biological specimen. |
| C178140 | Partial Thromboplastin Time | Partial Thromboplastin Time | A measurement of the length of time that it takes for clotting to occur when no activating reagents are added to a biological specimen. The test is partial due to the absence of tissue factor (Factor III) from the reaction mixture. |
| C186035 | Pathologic Casts | Non-Hyalin Casts; Non-Hyaline Casts; Pathologic Casts | A measurement of the pathologic (non-hyaline) casts present in a biological specimen. |
| C184559 | PB-22 3-carboxyindole | PB-22 3-carboxyindole | A measurement of the synthetic cannabinoid metabolite PB-22 3-carboxyindole in a biological specimen. |
| C132378 | PCA3 mRNA/PSA mRNA | PCA3 mRNA/PSA mRNA | A relative measurement (ratio) of the prostate cancer antigen 3 mRNA to prostate specific antigen mRNA in a biological specimen. |
| C74617 | Pelger Huet Anomaly | Pelger Huet Anomaly; Pelger-Huet Cells; PHA | A measurement of the Pelger-Huet Anomaly (nuclei of granulocytes appear rod-like, bilobed, peanut, or dumbbell shaped) in a biological specimen. |
| C184631 | Pemoline | Pemoline | A measurement of the pemoline in a biological specimen. |
| C81988 | Pemphigoid Antibodies | Pemphigoid Antibodies | A measurement of the pemphigoid antibodies in a biological specimen. |
| C184632 | Pentazocine | Pentazocine | A measurement of the pentazocine in a biological specimen. |
| C184561 | Pentedrone | Pentedrone | A measurement of the pentedrone in a biological specimen. |
| C75367 | Pentobarbital | Pentobarbital | A measurement of the pentobarbital present in a biological specimen. |
| C184562 | Pentylone | Pentylone | A measurement of the pentylone in a biological specimen. |
| C100469 | Pepsinogen A | Pepsinogen A; PGA | A measurement of the pepsinogen A in a biological specimen. |
| C100470 | Pepsinogen C | Pepsinogen C; PGC | A measurement of the pepsinogen C in a biological specimen. |
| C100467 | Pepsinogen I | Pepsinogen I; PGI | A measurement of the pepsinogen I in a biological specimen. |
| C100468 | Pepsinogen II | Pepsinogen II; PGII | A measurement of the pepsinogen II in a biological specimen. |
| C100122 | Pepsinogen | Pepsinogen | A measurement of the pepsinogen in a biological specimen. |
| C163486 | Peptide Transporter TAP1 | Antigen Peptide Transporter 1; Peptide Transporter TAP1 | A measurement of the peptide transporter TAP1 in a biological specimen. |
| C80202 | Peptide YY | Peptide Tyrosine Tyrosine; Peptide YY | A measurement of the peptide YY in a biological specimen. |
| C187819 | Peptidylprolyl Isomerase A | Cyclophilin A; CYPA; Peptidylprolyl Isomerase A; Rotamase A | A measurement of the peptidylprolyl isomerase A in a biological specimen. |
| C184596 | Perampanel | Perampanel | A measurement of the perampanel in a biological specimen. |
| C112395 | Periostin | OSF2; Osteoblast Specific Factor 2; Periostin; POSTN | A measurement of the periostin in a biological specimen. |
| C177988 | Perphenazine | Perphenazine | A measurement of the perphenazine in a biological specimen. |
| C161367 | pH Adjusted for Body Temp | pH Adjusted for Body Temp | A measurement of pH, which has been adjusted for body temperature, in a biological specimen. |
| C45997 | pH | pH | The negative logarithm (base 10) of the concentration of hydronium ions, which is used as a measure of the acidity or alkalinity of a fluid. |
| C184573 | Phenazocine | Phenazocine | A measurement of the phenazocine in a biological specimen. |
| C74694 | Phencyclidine | Phencyclidine; Phenylcyclohexylpiperidine | A measurement of the phencyclidine present in a biological specimen. |
| C184597 | Phendimetrazine | Phendimetrazine | A measurement of the phendimetrazine in a biological specimen. |
| C184574 | Phenmetrazine | Phenmetrazine | A measurement of the phenmetrazine in a biological specimen. |
| C75368 | Phenobarbital | Phenobarbital | A measurement of the phenobarbital present in a biological specimen. |
| C74695 | Phenothiazine | Dibenzothiazine; Phenothiazine | A measurement of the phenothiazine present in a biological specimen. |
| C174299 | Phentermine | Phentermine; Phenyl-tertiary-butylamine | A measurement of the phentermine in a biological specimen. |
| C81280 | Phenylalanine | Phenylalanine | A measurement of the phenylalanine in a biological specimen. |
| C81281 | Phenylalanine/Tyrosine | Phenylalanine/Tyrosine | A relative measurement (ratio) of the phenylalanine to tyrosine in a biological specimen. |
| C147414 | Phenylketones | Phenyl Ketones; Phenylketones | A measurement of the total phenylketones in a biological specimen |
| C174297 | Phenylpropanolamine | Beta-Hydroxyamphetamine; Norephedrine; Phenylpropanolamine | A measurement of the phenylpropanolamine in a biological specimen. |
| C147413 | Phenytoin | Phenytoin | A measurement of the phenytoin in a biological specimen. |
| C165981 | Phos-S6 Ribosomal Protein | Phos-S6 Ribosomal Protein; Phosphorylated S6 protein of the 40S ribosomal subunit | A measurement of the phosphorylated S6 protein of the 40S ribosomal subunit in a biological specimen. |
| C106553 | Phosphate Clearance | Phosphate Clearance | A measurement of the volume of serum or plasma that would be cleared of phosphate by excretion of urine for a specified unit of time (e.g. one minute). |
| C174304 | Phosphate Crystals | Phosphate Crystals | A measurement of the total phosphate crystals in a biological specimen. |
| C64857 | Phosphate | Inorganic Phosphate; Phosphate; Phosphorus | A measurement of the phosphate in a biological specimen. |
| C79461 | Phosphate/Creatinine | Phosphate/Creatinine | A relative measurement (ratio or percentage) of the phosphate to creatinine in a biological specimen. |
| C147420 | Phosphatidylcholine/Albumin | Phosphatidylcholine/Albumin | A relative measurement (ratio or percentage) of the phosphatidylcholine to albumin in a biological specimen. |
| C187820 | Phosphatidylethanol | PEth; Phosphatidylethanol | A measurement of the total phosphatidylethanol in a biological specimen. |
| C147423 | Phosphatidylglycerol/Lung Surfactant | Phosphatidylglycerol/Lung Surfactant; Phosphatidylglycerol/Pulmonary Surfactant | A relative measurement (ratio) of the phosphatidylglycerol to total lung surfactant in a biological specimen. |
| C122143 | Phosphatidylserine IgA Antibody | Phosphatidylserine IgA Antibody | A measurement of the phosphatidylserine IgA antibody in a biological specimen. |
| C122144 | Phosphatidylserine IgG Antibody | Phosphatidylserine IgG Antibody | A measurement of the phosphatidylserine IgG antibody in a biological specimen. |
| C122145 | Phosphatidylserine IgM Antibody | Phosphatidylserine IgM Antibody | A measurement of the phosphatidylserine IgM antibody in a biological specimen. |
| C181405 | Phospholipase A2 | Phospholipase A2 | A measurement of the total phospholipase A2 in a biological specimen. |
| C163483 | Phospholipid Scramblase 1 | Phospholipid Scramblase 1 | A measurement of the phospholipid scramblase 1 in a biological specimen. |
| C96623 | Phospholipid | Phospholipid | A measurement of the phospholipids in a biological specimen. |
| C150821 | Phosphorus Excretion Rate | Phosphorus Excretion Rate | A measurement of the amount of phosphorus being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C172501 | Phosphorylated Neurofilament Heavy Chain | Phosphorylated Neurofilament Heavy Chain | A measurement of the phosphorylated neurofilament heavy chain in a biological specimen. |
| C156521 | Phosphorylated STAT3 | Phosphorylated STAT3; pSTAT3 | A measurement of the phosphorylated STAT3 (signal transducer and activator of transcription 3) in a biological specimen. |
| C156522 | Phosphorylated STAT3/STAT3 | Phosphorylated STAT3/STAT3; pSTAT3/STAT3 | A relative measurement (ratio or percentage) of the phosphorylated STAT3 to total STAT3 in a biological specimen. |
| C176312 | Phosphorylated Tau Prot/Amyloid Beta1-42 | Phosphorylated Tau Prot/Amyloid Beta1-42; Phosphorylated Tau Protein/Amyloid Beta 1-42 | A relative measurement (ratio) of the phosphorylated Tau protein to amyloid beta 1-42 in a biological specimen. |
| C187821 | Phosphorylated Tau Protein 181 | Phosphorylated Tau 181; Phosphorylated Tau Protein 181 | A measurement of the phosphorylated Tau protein 181 in a biological specimen. |
| C84812 | Phosphorylated Tau Protein | Phosphorylated Tau Protein | A measurement of the phosphorylated Tau protein in a biological specimen. |
| C119279 | Pi-GST Excretion Rate | Pi-GST Excretion Rate | A measurement of the amount of Pi Glutathione-S-Transferase being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C189518 | Pigment Casts | Pigment Casts; Pigmented Casts | A measurement of the pigment casts present in a biological specimen. |
| C177987 | Pimozide | Pimozide | A measurement of the pimozide in a biological specimen. |
| C184633 | Pipradrol | Pipradrol | A measurement of the pipradrol in a biological specimen. |
| C163482 | Placental Growth Factor | PGF; PIGF; Placental Growth Factor; PLGF | A measurement of the placental growth factor in a biological specimen. |
| C184509 | Placental Specific Alkaline Phosphatase | Placental Specific Alkaline Phosphatase | A measurement of the placental specific alkaline phosphatase isoform in a biological specimen. |
| C163447 | Plasma Equivalent Glucose Distribution | Plasma Equivalent Glucose Distribution | A measurement of the plasma equivalent glucose distribution in a biological specimen. |
| C163446 | Plasma Equivalent Glucose | Plasma Equivalent Glucose | A measurement of the plasma equivalent glucose in a biological specimen. |
| C74618 | Plasmacytoid Lymphocytes | Plasmacytoid Lymphocytes; Plymphocytes | A measurement of the plasmacytoid lymphocytes (lymphocytes with peripherally clumped chromatin and often deep blue cytoplasm, and that appear similar to plasma cells) in a biological specimen. |
| C158229 | Plasmacytoid Lymphocytes/Leukocytes | Plasmacytoid Lymphocytes/Leukocytes | A relative measurement (ratio or percentage) of the plasmacytoid lymphocytes to all leukocytes in a biological specimen. |
| C74648 | Plasmacytoid Lymphocytes/Lymphocytes | Plasmacytoid Lymphocytes/Lymphocytes | A relative measurement (ratio or percentage) of the plasmacytoid lymphocytes (lymphocytes with peripherally clumped chromatin and often deep blue cytoplasm, and that appear similar to plasma cells) to all lymphocytes in a biological specimen. |
| C81989 | Plasminogen Activator Inhibitor-1 AG | Plasminogen Activator Inhibitor-1 AG | A measurement of the plasminogen activator inhibitor-1 antigen in a biological specimen. |
| C82030 | Plasminogen Activator Inhibitor-1 | Plasminogen Activator Inhibitor-1 | A measurement of the plasminogen activator inhibitor-1 in a biological specimen. |
| C127633 | Plasminogen | Plasminogen | A measurement of the plasminogen (antigen) in a biological specimen. |
| C111292 | Platelet Activating Factor | Platelet Activating Factor | A measurement of the platelet activating factor in a biological specimen. |
| C111293 | Platelet Aggregation Amplitude | Platelet Aggregation Amplitude | A measurement of the magnitude of the platelet aggregation in a biological specimen. |
| C114210 | Platelet Aggregation Curve Type | Platelet Aggregation Curve Type | The classification of the curve pattern that is formed as a result of platelet aggregation. |
| C114211 | Platelet Aggregation Mean Amplitude | Platelet Aggregation Mean Amplitude | An average of the measurements of the magnitude of the platelet aggregation in a biological specimen. |
| C114212 | Platelet Aggregation Mean Curve Type | Platelet Aggregation Mean Curve Type | The classification of the curve pattern that is formed as the average result of the platelet aggregation curve measurements. |
| C103427 | Platelet Aggregation | Platelet Aggregation; Platelet Function | A measurement of the association of platelets to one another via adhesion molecules in a biological sample. |
| C96624 | Platelet Clumps | Platelet Clumps; PLT Clumps | A measurement of the platelet clumps in a biological specimen. |
| C111294 | Platelet Component Distribution Width | Platelet Component Distribution Width | A measurement of a marker of platelet shape change in a biological specimen. |
| C163481 | Platelet Derived Growth Factor IsoformAA | PDGF Isoform AA; Platelet Derived Growth Factor IsoformAA; Platelet Derived Growth Factor-AA Isoform | A measurement of the platelet derived growth factor isoform AA in a biological specimen. |
| C116208 | Platelet Derived Growth Factor IsoformAB | PDGF Isoform AB; Platelet Derived Growth Factor IsoformAB; Platelet Derived Growth Factor-AB Isoform | A measurement of the platelet derived growth factor isoform AB in a biological specimen. |
| C81962 | Platelet Distribution Width | Platelet Distribution Width | A measurement of the range of platelet sizes in a biological specimen. |
| C135472 | Platelet Endothelial Adhesion Molecule 1 | CD31; CD31 Antigen; PECAM; PECAM-1; PECAM1; Platelet And Endothelial Cell Adhesion Molecule 1; Platelet Endo Cell Adhesion Molecule 1; Platelet Endothelial Adhesion Molecule | A measurement of the platelet and endothelial cell adhesion molecule 1 in a biological specimen. |
| C147412 | Platelet Fctr 4 Heparin Cmplx Induced Ab | Platelet Factor 4 Heparin Complex Induced Antibody; Platelet Fctr 4 Heparin Cmplx Induced Ab | A measurement of the platelet factor 4 heparin complex induced antibody in a biological specimen. |
| C111295 | Platelet Function Closure Time | PFCT; Platelet Function Closure Time | A measurement of the platelet function closure time in a biological specimen. |
| C100424 | Platelet Hematocrit | Platelet Hematocrit; Thrombocytocrit | A relative measurement (ratio or percentage) of the proportion of the volume of blood taken up by platelets. |
| C132380 | Platelet Mass Distribution Width | Platelet Mass Distribution Width | A measurement which represents the variation defined by two standard deviations of the platelet dry mass distribution in a biological specimen. |
| C111296 | Platelet Morphology | Platelet Morphology | An examination or assessment of the form and structure of platelets. |
| C116209 | Platelet Satellitism | Platelet Satellitism | An examination or assessment of the platelet satellitism (platelet rosetting around cells) in a biological specimen. |
| C165978 | Platelet-Granulocyte Agg | Platelet-Granulocyte Agg; Platelet-Granulocyte Aggregates | A measurement of the aggregates composed of platelets and granulocytes in a biological specimen. |
| C51951 | Platelets | Platelets | A measurement of the platelets (non-nucleated thrombocytes) in a biological specimen. |
| C147415 | Platelets, Agranular | Platelets, Agranular | A measurement of the agranular platelets in a biological specimen. |
| C135440 | Platelets, Estimated | Platelets, Estimated | An estimated measurement of the platelets (non-nucleated thrombocytes) in a biological specimen. |
| C79602 | Poikilocytes | Poikilocytes | A measurement of the odd-shaped erythrocytes in a whole blood specimen. |
| C74649 | Poikilocytes/Erythrocytes | Poikilocytes/Erythrocytes | A relative measurement (ratio or percentage) of the poikilocytes, or irregularly shaped erythrocytes, to all erythrocytes in a biological specimen. |
| C64803 | Polychromasia | Polychromasia | A measurement of the blue-staining characteristic of newly generated erythrocytes. |
| C147418 | Polychromatophilic Erythroblast | Polychromatophilic Erythroblast | A measurement of the polychromatophilic erythroblasts in a biological specimen taken from a non-human organism. |
| C147419 | Polychromatophilic Normoblast | Polychromatophilic Normoblast | A measurement of the polychromatophilic normoblasts in a biological specimen taken from a non-human organism. |
| C156539 | Porphobilinogen | Porphobilinogen | A measurement of the porphobilinogen in a biological specimen. |
| C156540 | Porphobilinogen/Creatinine | Porphobilinogen/Creatinine | A relative measurement (ratio or percentage) of the porphobilinogen to creatinine in a biological specimen. |
| C120648 | Porphyrin | Porphyrin | A measurement of the total porphyrin in a biological specimen. |
| C106560 | Potassium Clearance | Potassium Clearance | A measurement of the volume of serum or plasma that would be cleared of potassium by excretion of urine for a specified unit of time (e.g. one minute). |
| C150820 | Potassium Excretion Rate | Potassium Excretion Rate | A measurement of the amount of potassium being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C64853 | Potassium | Potassium | A measurement of the potassium in a biological specimen. |
| C79462 | Potassium/Creatinine | Potassium/Creatinine | A relative measurement (ratio or percentage) of the potassium to creatinine in a biological specimen. |
| C119293 | PP Arterial O2/Fraction Inspired O2 | PAO2/FIO2; PP Arterial O2/Fraction Inspired O2 | A relative measurement (ratio or percentage) of the force per unit area (pressure) of oxygen dissolved in arterial blood to the percentage oxygen of an inhaled mixture of gasses. |
| C139080 | Prazepam | Prazepam | A measurement of the prazepam present in a biological specimen. |
| C100435 | Prealbumin | Prealbumin; Thyroxine-binding Prealbumin; Transthyretin | A measurement of the prealbumin in a biological specimen. |
| C74619 | Precursor Plasma Cells | Plasmablast; Precursor Plasma Cells | A measurement of the precursor (blast stage) plasma cells (antibody secreting cells derived from B cells via antigen stimulation) in a biological specimen. |
| C74650 | Precursor Plasma Cells/Lymphocytes | Precursor Plasma Cells/Lymphocytes | A relative measurement (ratio or percentage) of the precursor (blast stage) plasma cells (antibody secreting cells derived from B cells via antigen stimulation) to all lymphocytes in a biological specimen. |
| C184642 | Pregabalin | Pregabalin | A measurement of the pregabalin in a biological specimen. |
| C82031 | Pregnancy-Associated Plasma Protein-A | Pregnancy-Associated Plasma Protein-A | A measurement of the pregnancy-associated plasma protein-A in a biological specimen. |
| C186092 | Pregnanediol | Pregnanediol | A measurement of the pregnanediol in a biological specimen. |
| C147421 | Pregnenolone | Pregnenolone | A measurement of the pregnenolone in a biological specimen. |
| C165979 | Pro-C6 | C-terminal Pro-Peptide of the Alpha 3 Type VI Collagen Chain; Endotrophin; Pro-C6 | A measurement of the pro-C6 in a biological specimen. |
| C156523 | Pro-gastrin Releasing Peptide | Pro-gastrin Releasing Peptide; proGRP | A measurement of the pro-gastrin releasing peptide in a biological specimen. |
| C82032 | ProB-type Natriuretic Peptide | Pro-Brain Natriuretic Peptide; ProB-type Natriuretic Peptide; proBNP | A measurement of the proB-type natriuretic peptide in a biological specimen. |
| C103430 | Procalcitonin | Procalcitonin | A measurement of the procalcitonin in a biological specimen. |
| C177983 | Prochlorperazine | Prochlorperazine | A measurement of the prochlorperazine in a biological specimen. |
| C96625 | Procollagen 1 N-Terminal Propeptide | Amino-terminal propeptide of type 1 procollagen; P1NP Aminoterm Type 1; Procollagen 1 N-Terminal Propeptide | A measurement of the procollagen 1 N-terminal propeptide in a biological specimen. |
| C128973 | Procollagen 3 N-Terminal Propeptide | Procollagen 3 N-Terminal Propeptide | A measurement of the procollagen 3 N-terminal propeptide in a biological specimen. |
| C82033 | Procollagen Type I Carboxy Term Peptide | Procollagen Type I Carboxy Term Peptide | A measurement of the procollagen-1 carboxy-terminal peptide in a biological specimen. |
| C117846 | Progesterone Receptor | NR3C3; PGR; PgR; PR; Progesterone Receptor | A measurement of the progesterone receptor protein in a biological specimen. |
| C74791 | Progesterone | Progesterone | A measurement of the progesterone hormone in a biological specimen. |
| C165964 | Progranulin | Progranulin | A measurement of the progranulin in a biological specimen. |
| C81967 | Proinsulin | Proinsulin | A measurement of the proinsulin in a biological specimen. |
| C111299 | Proinsulin/Insulin Ratio | Proinsulin/Insulin Ratio | A relative measurement (ratio or percentage) of the proinsulin to insulin in a biological specimen. |
| C74870 | Prolactin | Prolactin | A measurement of the prolactin hormone in a biological specimen. |
| C120646 | Proliferating Cell Nuclear Antigen | Cyclin; Proliferating Cell Nuclear Antigen | A measurement of the proliferating cell nuclear antigen in a biological specimen. |
| C127632 | Proliferating Erythroid/Total Cells | Proliferating Erythroid/Total Cells | A relative measurement (ratio or percentage) of the proliferating erythroid cells to total cells in a biological specimen. |
| C127634 | Proliferating Myeloid Cells/Total Cells | Proliferating Myeloid Cells/Total Cells | A relative measurement (ratio or percentage) of the proliferating myeloid cells to total cells in a biological specimen. |
| C122141 | Proline | Proline | A measurement of the proline in a biological specimen. |
| C74620 | Prolymphocytes | Prolymphocytes | A measurement of the prolymphocytes in a biological specimen. |
| C64829 | Prolymphocytes/Leukocytes | Prolymphocytes/Leukocytes | A relative measurement (ratio or percentage) of prolymphocytes to leukocytes in a biological specimen. |
| C74651 | Prolymphocytes/Lymphocytes | Prolymphocytes/Lymphocytes | A relative measurement (ratio or percentage) of the prolymphocytes to all lymphocytes in a biological specimen. |
| C74621 | Promonocytes | Promonocytes | A measurement of the promonocytes in a biological specimen. |
| C74652 | Promonocytes/Leukocytes | Promonocytes/Leukocytes | A relative measurement (ratio or percentage) of the promonocytes to all leukocytes in a biological specimen. |
| C187678 | Promonocytes/Total Cells | Promonocytes/Total Cells | A relative measurement (ratio or percentage) of the promonocytes to total cells in a biological specimen (for example a bone marrow specimen). |
| C117847 | Promyeloblasts | Promyeloblasts | A measurement of the promyeloblasts in a biological specimen. |
| C74622 | Promyelocytes | Promyelocytes | A measurement of the promyelocytes (immature myelocytes) in a biological specimen. |
| C74653 | Promyelocytes/Leukocytes | Promyelocytes/Leukocytes | A relative measurement (ratio or percentage) of the promyelocytes (immature myelocytes) to all leukocytes in a biological specimen. |
| C98773 | Promyelocytes/Total Cells | Promyelocytes/Total Cells | A relative measurement (ratio or percentage) of the promyelocytes (immature myelocytes) to total cells in a biological specimen (for example a bone marrow specimen). |
| C74885 | Propoxyphene | Propoxyphene | A measurement of the propoxyphene present in a biological specimen. |
| C120647 | Proprotein Convertase Subtilisin/Kexin 9 | Proprotein Convertase Subtilisin/Kexin 9 | A measurement of the proprotein convertase subtilisin/kexin type 9 in a biological specimen. |
| C128976 | Prorubricyte | Basophilic Erythroblast; Basophilic Normoblast; Prorubricyte | A measurement of the prorubricytes in a biological specimen. |
| C128977 | Prorubricyte/Total Cells | Prorubricyte/Total Cells | A relative measurement (ratio or percentage) of the prorubricytes to total cells in a biological specimen. |
| C189515 | Prostaglandin D2 Receptor 2 | Prostaglandin D2 Receptor 2 | A measurement of the prostaglandin D2 receptor 2 in a biological specimen. |
| C103432 | Prostaglandin D2 Synthase | Beta-Trace Protein; Prostaglandin D2 Synthase | A measurement of the prostaglandin D2 synthase in a biological specimen. |
| C103431 | Prostaglandin D2 | Prostaglandin D2 | A measurement of the prostaglandin D2 in a biological specimen. |
| C103433 | Prostaglandin E Synthase | Prostaglandin E Synthase | A measurement of the prostaglandin E synthase in a biological specimen. |
| C103434 | Prostaglandin E1 | Prostaglandin E1 | A measurement of the prostaglandin E1 in a biological specimen. |
| C103435 | Prostaglandin E2 | Prostaglandin E2 | A measurement of the prostaglandin E2 in a biological specimen. |
| C103436 | Prostaglandin F1 Alpha | Prostaglandin F1 Alpha | A measurement of the prostaglandin F1 alpha in a biological specimen. |
| C103437 | Prostaglandin F2 Alpha | Prostaglandin F2 Alpha | A measurement of the prostaglandin F2 alpha in a biological specimen. |
| C103343 | Prostaglandin | Prostaglandin | A measurement of the total prostaglandin in a biological specimen. |
| C184598 | Prostanozol | Prostanozol | A measurement of the prostanozol in a biological specimen. |
| C132379 | Prostate Cancer Antigen 3 mRNA | Prostate Cancer Antigen 3 mRNA | A measurement of the prostate cancer antigen 3 mRNA in a biological specimen. |
| C132382 | Prostate Circulating Tumor Cells | Prostate Circulating Tumor Cells | A measurement of the prostate circulating tumor cells in a biological specimen. |
| C132385 | Prostate Specific Antigen mRNA | Prostate Specific Antigen mRNA | A measurement of the prostate-specific antigen mRNA in a biological specimen. |
| C17634 | Prostate Specific Antigen | Prostate Specific Antigen | A measurement of the total prostate specific antigen in a biological specimen. |
| C132383 | Prostate Specific Antigen, Free | Prostate Specific Antigen, Free | A measurement of the unbound prostate-specific antigen in a biological specimen. |
| C80204 | Prostatic Acid Phosphatase | Prostatic Acid Phosphatase | A measurement of the prostatic acid phosphatase in a biological specimen. |
| C150822 | Protein Excretion Rate | Protein Excretion Rate | A measurement of the amount of total protein being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C150846 | Protein Induced by Vitamin K Absence-II | DCP; Des-Gammacarboxyprothrombin; PIVKA-II; Protein Induced by Vitamin K Absence-II; Protein Induced by Vitamin K Absence/Antagonist-II | A measurement of the protein induced by vitamin K absence-II in a biological specimen. |
| C147422 | Protein Pattern | Protein Pattern | A measurement of the protein band pattern in a biological specimen. |
| C147424 | Protein S Activity Actual/Control | Protein S Activity Actual/Control; Protein S Activity Actual/Normal; Protein S Activity Actual/Protein S Activity Control | A relative measurement (ratio or percentage) of the biological activity of protein S in a subject's specimen when compared to the same activity in a control specimen. |
| C170593 | Protein S Actual/Control | Protein S Actual/Control | A relative measurement (ratio or percentage) of the protein S in a subject's specimen when compared to a control specimen. |
| C147425 | Protein S Free Activity Actual/Control | Protein S Free Activity Actual/Control; Protein S Free Activity Actual/Normal; Protein S Free Activity Actual/Protein S Free Activity Control | A relative measurement (ratio or percentage) of the biological activity of free protein S in a subject's specimen when compared to the same activity in a control specimen. |
| C100436 | Protein S | Protein S | A measurement of the total protein S in a biological specimen. |
| C170596 | Protein S, Free Actual/Control | Protein S, Free Actual/Control | A relative measurement (ratio or percentage) of the free protein S in a subject's specimen when compared to a control specimen. |
| C122142 | Protein S, Free | Protein S, Free | A measurement of the unbound protein S in a biological specimen. |
| C64858 | Protein | Protein | A measurement of the total protein in a biological specimen. |
| C79463 | Protein/Creatinine | Protein/Creatinine | A relative measurement (ratio or percentage) of the total protein to creatinine in a biological specimen. |
| C92240 | Protein/Osmolality | Protein/Osmolality; Protein/Osmolality Ratio | A relative measurement (ratio or percentage) of total proteins to the osmolality of a biological specimen. |
| C120649 | Proteinase 3 Antibody | Proteinase 3 Antibody | A measurement of the proteinase 3 antibody in a biological specimen. |
| C98774 | Prothrombin Activity | Factor II Activity; Prothrombin Activity | A measurement of the biological activity of coagulation factor prothrombin in a biological specimen. |
| C189514 | Prothrombin Fragment 1 | Prothrombin Fragment 1 | A measurement of the prothrombin fragment 1 in a biological specimen. |
| C189513 | Prothrombin Fragment 2 | Prothrombin Fragment 2 | A measurement of the prothrombin fragment 2 in a biological specimen. |
| C82034 | Prothrombin Fragments 1 + 2 | Prothrombin Fragments 1 + 2 | A measurement of the prothrombin fragments 1 and 2 in a biological specimen. |
| C64805 | Prothrombin Intl. Normalized Ratio | Prothrombin Intl. Normalized Ratio | A ratio that represents the prothrombin time for a plasma specimen, divided by the result for a control plasma specimen, further standardized for the International Sensitivity Index of the tissue factor (thromboplastin) used in the test. |
| C170591 | Prothrombin Time Actual/Control | Prothrombin Time Actual/Control | A relative measurement (ratio or percentage) of the prothrombin time in a subject's specimen when compared to a control specimen. |
| C62656 | Prothrombin Time | Prothrombin Time | A blood clotting measurement that evaluates the extrinsic pathway of coagulation. |
| C147341 | Protoporphyrin, Free | Protoporphyrin, Free | A measurement of the free protoporphyrin (unbound to iron in hemoglobin) in a biological specimen. |
| C186091 | Prprot Cnvrtase Subtilisin-Kexin 9, Free | Proprotein Convertase Subtilisin/Kexin Type 9; Prprot Cnvrtase Subtilisin-Kexin 9, Free | A measurement of the free proprotein convertase subtilisin/kexin type 9 in a biological specimen. |
| C132384 | PSA, Free/PSA | PSA, Free/PSA | A relative measurement (percentage) of the free prostate specific antigen to total prostate specific antigen in a biological specimen. |
| C187823 | Pseudo Pelger-Huet Neutrophils | Neutrophils with Pseudo Pelger-Huet Nucleus; Pseudo Pelger-Huet Neutrophils | A measurement of the neutrophils with a Pelger-Huet-like nucleus (hyposegmented) in a biological specimen. |
| C165958 | Pseudo-Eosinophils | Pseudo-Eosinophils | A measurement of the pseudo-eosinophils in a biological specimen. |
| C165959 | Pseudo-Eosinophils/Leukocytes | Pseudo-Eosinophils/Leukocytes | A relative measurement (ratio or percentage) of the pseudo-eosinophils to the leukocytes in a biological specimen. |
| C74696 | Pseudoephedrine | Pseudoephedrine | A measurement of the pseudoephedrine present in a biological specimen. |
| C75356 | Psilocybin | Magic Mushrooms; Psilocybin; Psilocybine | A measurement of the psilocybin in a biological specimen. |
| C187818 | PTT/Standard | Partial Thromboplastin Time/Standard Thromboplastin Time; PTT/Standard; PTT/Standard PTT | A relative measurement (ratio or percentage) of the subject's partial thromboplastin time to a standard or control partial thromboplastin time. |
| C161359 | Pus | Pus | A measurement of the pus in a biological specimen. |
| C189346 | Pyknotic Cells | Karyopyknotic Cells; Pyknotic Cells | A measurement of the pyknotic cells in a biological specimen. |
| C156524 | Pyocytes | Pyocytes | A measurement of the pyocytes in a biological specimen. |
| C80211 | Pyridinoline | Pyridinoline | A measurement of the pyridinoline in a biological specimen. |
| C147426 | Pyridinoline/Creatinine | Pyridinoline/Creatinine | A relative measurement (ratio or percentage) of the pyridinoline to creatinine in a biological specimen. |
| C158237 | Pyridoxal Phosphate | Active Vitamin B6; Pyridoxal Phosphate | A measurement of the pyridoxal phosphate in a biological specimen. |
| C184643 | Pyrovalerone | Pyrovalerone | A measurement of the pyrovalerone in a biological specimen. |
| C156532 | Pyruvate Kinase Isozyme M1 | Pyruvate Kinase Isozyme M1 | A measurement of the pyruvate kinase isozyme M1 in a biological specimen. |
| C156531 | Pyruvate Kinase Isozyme M2 | Pyruvate Kinase Isozyme M2 | A measurement of the pyruvate kinase isozyme M2 in a biological specimen. |
| C156530 | Pyruvate Kinase Muscle Isozyme | Pyruvate Kinase Muscle Isozyme | A measurement of the total pyruvate kinase muscle isozymes (M1 and M2) in a biological specimen. |
| C156470 | Pyruvate Kinase | PK; Pyruvate Kinase | A measurement of the total pyruvate kinase in a biological specimen. |
| C147427 | Pyruvate | Pyruvate; Pyruvic Acid | A measurement of the pyruvate in a biological specimen. |
| C184634 | Quazepam | Quazepam | A measurement of the quazepam in a biological specimen. |
| C177965 | Quetiapine | Quetiapine | A measurement of the quetiapine in a biological specimen. |
| C74772 | RBC Casts | Erythrocyte Casts; RBC Casts | A measurement of the red blood cell casts present in a biological specimen. |
| C139071 | RDW Standard Deviation | RDW Standard Deviation; RDW-SD; Red Cell Volume Distribution Width Standard Deviation | A measurement of the volume dispersion within an erythrocyte population, calculated as the width of the distribution curve at the 20 percent frequency level. |
| C122146 | Reactive Oxygen Metabolite | Reactive Oxygen Metabolite | A measurement of the reactive oxygen metabolite in a biological specimen. |
| C117852 | Receptor Activator Nuclear KappaB Ligand | Receptor Activator Nuclear KappaB Ligand; Receptor Activator of Nuclear Kappa-B Ligand | A measurement of the receptor activator of nuclear kappa-B ligand in a biological specimen. |
| C165980 | Receptor Advanced Glycation Endproducts | Advanced Glycosylation End-Product Specific Receptor; AGER; Receptor Advanced Glycation Endproducts | A measurement of the receptor advanced glycation endproducts in a biological specimen. |
| C147428 | Reducing Substances | Reducing Substances | A measurement of the reducing substances (e.g., sugars, glutathione, creatinine, uric acid, and ascorbic acid) in a biological specimen. |
| C147429 | Reducing Sugars | Reducing Sugars | A measurement of the reducing sugars in a biological specimen. |
| C81957 | Reg upon Act Normal T-cell Exprd Secrtd | Chemokine Ligand 5; Reg upon Act Normal T-cell Exprd Secrtd | A measurement of the RANTES (regulated on activation, normally, T-cell expressed, and secreted) chemokine in a biological specimen. |
| C120656 | Remnant Lipoprotein | Remnant Lipoprotein | A measurement of the remnant lipoproteins in a biological specimen. |
| C174229 | Renal Epithelial Casts | Renal Epithelial Casts | A measurement of the renal epithelial cell casts in a biological specimen. |
| C170595 | Renal Epithelial Cells | Renal Epithelial Cells | A measurement of the renal epithelial cells in a biological specimen. |
| C142289 | Renal Papillary Antigen 1 | Renal Papillary Antigen 1 | A measurement of the renal papillary antigen 1 in a biological specimen. |
| C174292 | Renal Tubular Epithelial Casts | Renal Tubular Epithelial Casts | A measurement of the renal tubular epithelial cell casts in a biological specimen. |
| C111305 | Renin Activity | Renin Activity | A measurement of the renin activity in a biological specimen. |
| C74893 | Renin | Active Renin; Angiotensinogenase; Direct Renin; Renin | A measurement of the renin in a biological specimen. |
| C147430 | Reptilase Activity Actual/Control | Reptilase Activity Actual/Control; Reptilase Activity Actual/Normal; Reptilase Activity Actual/Reptilase Activity Control | A relative measurement (ratio or percentage) of the biological activity of reptilase dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C96628 | Reptilase Time | Reptilase Time | A measurement of the time it takes a plasma sample to clot after adding the active enzyme reptilase. |
| C80205 | Resistin | Resistin | A measurement of the resistin in a biological specimen. |
| C139069 | Ret Corpuscular HGB Conc Distr Width | Ret Corpuscular HGB Conc Distr Width; Reticulocyte Corpuscular Hemoglobin Distribution Width | A measurement of the standard deviation of hemoglobin concentrations in reticulocytes in a biological specimen, calculated as the standard deviation of hemoglobin content divided by the mean hemoglobin content. |
| C139070 | Ret Hemoglobin Distribution Width | Ret Hemoglobin Distribution Width; Reticulocyte Hemoglobin Concentration Distribution Width | A measurement of the distribution of the hemoglobin concentration in reticulocytes. |
| C139072 | Ret RDW Coefficient of Variation | RDWr-CV; Red Cell Volume Distribution Width Coefficient of Variation in Reticulocytes; Ret RDW Coefficient of Variation; Reticulocyte Volume Distribution Width Coefficient of Variation | A measurement of the volume dispersion within a reticulocyte population, calculated as the standard deviation of the mean reticulocyte volume divided by the mean reticulocyte volume, multiplied by 100 to convert to a percentage. |
| C139073 | Ret RDW Standard Deviation | RDWr-SD; Red Cell Volume Distribution Width Standard Deviation in Reticulocytes; Ret RDW Standard Deviation; Reticulocyte Volume Distribution Width Standard Deviation | A measurement of the volume dispersion within a reticulocyte population, calculated as the width of the distribution curve at the 20 percent frequency level. |
| C139074 | Ret Volume Distribution Width | RDWr; Ret Volume Distribution Width; Reticulocyte Volume Distribution Width | A relative measurement (ratio or percentage) of the standard deviation of the reticulocyte volume to the mean distribution of the reticulocyte volume in a biological specimen. |
| C98776 | Ret. Corpuscular Hemoglobin Content | CHr; Ret. Corpuscular Hemoglobin Content; Reticulocyte Cellular Hemoglobin Content | A measurement of the average total amount of hemoglobin per reticulocyte. |
| C138970 | Ret. Corpuscular HGB Concentration Mean | Ret. Corpuscular HGB Concentration Mean; Reticulocyte Corpuscular Hemoglobin Concentration Mean | An indirect measurement of the average concentration of hemoglobin per reticulocyte in a biological specimen, calculated as the ratio of hemoglobin to hematocrit. |
| C51947 | Reticulocytes | Reticulocytes | A measurement of the reticulocytes in a biological specimen. |
| C64828 | Reticulocytes/Erythrocytes | Reticulocytes/Erythrocytes | A relative measurement (ratio or percentage) of reticulocytes to erythrocytes in a biological specimen. |
| C187680 | Reticulocytes/Total Cells | Reticulocytes/Total Cells | A relative measurement (ratio or percentage) of reticulocytes to total cells in a biological specimen. |
| C187824 | Retinoic Acid | Retinoate; Retinoic Acid | A measurement of the retinoic acid in a biological specimen. |
| C189526 | Retinol Binding Protein 1 | Retinol Binding Protein 1 | A measurement of the retinol binding protein 1 in a biological specimen. |
| C189525 | Retinol Binding Protein 2 | Retinol Binding Protein 2 | A measurement of the retinol binding protein 2 in a biological specimen. |
| C189524 | Retinol Binding Protein 3 | Retinol Binding Protein 3 | A measurement of the retinol binding protein 3 in a biological specimen. |
| C189523 | Retinol Binding Protein 4 | Retinol Binding Protein 4 | A measurement of the retinol binding protein 4 in a biological specimen. |
| C100437 | Retinol Binding Protein | Retinol Binding Protein | A measurement of the total retinol binding protein in a biological specimen. |
| C154729 | Retinol Binding Protein/Creatinine | Retinol Binding Protein/Creatinine | A relative measurement (ratio or percentage) of the retinol binding protein to creatinine in a biological specimen. |
| C135442 | Retinyl Palmitate | Retinol Palmitate; Retinyl Palmitate; Vitamin A Palmitate | A measurement of the endogenous retinyl palmitate vitamin A in a biological specimen. |
| C92948 | Rh Factor | Rh Factor | A measurement of non-specified Rhesus factor antigen(s) in a biological specimen. |
| C125948 | RhD Factor | RhD Factor | A measurement of the Rhesus factor D antigen in a biological specimen. |
| C120652 | Rheumatoid Factor IgA Antibody | Rheumatoid Factor IgA Antibody | A measurement of the rheumatoid factor IgA antibody in a biological specimen. |
| C120653 | Rheumatoid Factor IgG Antibody | Rheumatoid Factor IgG Antibody | A measurement of the rheumatoid factor IgG antibody in a biological specimen. |
| C120654 | Rheumatoid Factor IgM Antibody | Rheumatoid Factor IgM Antibody | A measurement of the rheumatoid factor IgM antibody in a biological specimen. |
| C74717 | Rheumatoid Factor | Rheumatoid Factor | A measurement of the rheumatoid factor antibody in a biological specimen. |
| C74898 | Riboflavin | Riboflavin; Vitamin B2 | A measurement of the riboflavin in a biological specimen. |
| C132301 | Ribonucleic Acid | Ribonucleic Acid | A measurement of a targeted ribonucleic acid (RNA) in a biological specimen. |
| C100457 | Ribonucleoprotein Antibody | Ribonucleoprotein Antibody; Ribonucleoprotein Extractable Nuclear Antibody; RNP Antibody | A measurement of the total ribonucleoprotein antibodies in a biological specimen. |
| C120658 | Ribonucleoprotein Smith Complex Antibody | Ribonucleoprotein Smith Complex Antibody | A measurement of the ribonucleoprotein Smith complex antibody in a biological specimen. |
| C120657 | Ribonucleoprotein-70 Antibody | Ribonucleoprotein-70 Antibody; snRNP70 Antibody | A measurement of the small nuclear ribonucleoprotein 70 antibody in a biological specimen. |
| C120659 | Ribosomal P Protein Antibody | Ribosomal P Protein Antibody | A measurement of the total ribosomal P protein antibody in a biological specimen. |
| C100419 | Ringed Sideroblasts | Ringed Sideroblasts | A measurement of the ringed sideroblasts (abnormal nucleated erythroblasts with a large number of iron deposits in the perinuclear mitochondria, forming a ring around the nucleus) in a biological specimen. |
| C177969 | Risperidone | Risperidone | A measurement of the risperidone in a biological specimen. |
| C177971 | Risperidone+9-Hydroxyrisperidone | Risperidone+9-Hydroxyrisperidone; Risperidone+Paliperidone | A measurement of the risperidone and 9-hydroxyrisperidone in a biological specimen. |
| C170582 | Ritalinic Acid | Ritalinic Acid | A measurement of the ritalinic acid in a biological specimen. |
| C120655 | RLP Cholesterol | RLP Cholesterol | A measurement of the cholesterol remnant-like particles in a biological specimen. |
| C122147 | RNA Polymerase III IgG Antibody | RNA Polymerase III IgG Antibody | A measurement of the RNA polymerase III IgG antibody in a biological specimen. |
| C74624 | Rouleaux Formation | Rouleaux Formation | A measurement of the stacking red blood cells in a biological specimen. |
| C142288 | Round Cells | Round Cells | A measurement of the round cells (round shaped cells mainly comprised of white blood cells and immature spermatogenic cells) in a biological specimen. |
| C74698 | Round Epithelial Cells | Round Epithelial Cells | A measurement of the round epithelial cells present in a biological specimen. |
| C100446 | Rubriblast | Proerythroblast; Pronormoblast; Rubriblast | A measurement of the rubriblasts in a biological specimen. |
| C98870 | Rubriblast/Total Cells | Proerythroblast/Total Cells; Pronormoblasts/Total Cells; Rubriblast/Total Cells | A relative measurement (ratio or percentage) of the rubriblasts to total cells in a biological specimen (for example a bone marrow specimen). |
| C128978 | Rubricyte | Polychromatophilic Erythroblast; Polychromatophilic Normoblast; Rubricyte | A measurement of the rubricytes in a biological specimen. |
| C129006 | Rubricyte/Total Cells | Rubricyte/Total Cells | A relative measurement (ratio or percentage) of the rubricytes to total cells in a biological specimen. |
| C165889 | Russian Thistle Pollen IgE AB RAST Score | Russian Thistle Pollen IgE AB RAST Score | A classification of the amount of Salsola tragus pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165888 | Russian Thistle Pollen IgE Antibody | Russian Thistle Pollen IgE Antibody | A measurement of the Salsola tragus pollen antigen IgE antibody in a biological specimen. |
| C172516 | S-Adenosylhomocysteine | S-adenosyl-L-homocysteine; S-Adenosylhomocysteine; SAH | A measurement of the S-adenosylhomocysteine in a biological specimen. |
| C172515 | S-Adenosylmethionine | S-adenosyl-L-methionine; S-Adenosylmethionine; SAM-e; SAMe; SAMMY | A measurement of the S-adenosylmethionine in a biological specimen. |
| C154730 | S100 Calcium Binding Protein A8 | S100 Calcium Binding Protein A8 | A measurement of the S100 calcium binding protein A8 in a biological specimen. |
| C127635 | S100 Calcium-Binding Protein B | S100 Calcium-Binding Protein B | A measure of the S100 calcium-binding protein B in a biological specimen. |
| C147431 | Salicylates | Salicylates | A measurement of the salicylates in a biological specimen. |
| C154760 | Sarcosine | N-Methylglycine; Sarcosine | A measurement of the sarcosine in a biological specimen. |
| C74706 | Schistocytes | Schistocytes | A measurement of the schistocytes (fragmented red blood cells) in a biological specimen. |
| C186094 | Schistocytes/Erythrocytes | Schistocytes/Erythrocytes | A relative measure (ratio or percentage) of schistocytes to erythrocytes in a biological specimen. |
| C100458 | Scl-70 Antibody | Scl-70 Antibody; Scleroderma-70 Antibody | A measurement of the total Scl-70 antibody in a biological specimen. |
| C122148 | Scl-70 IgG Antibody | Scl-70 IgG Antibody; Scleroderma-70 IgG Antibody | A measurement of the Scl-70 IgG antibody in a biological specimen. |
| C117857 | Sclerostin | Sclerostin | A measurement of the sclerostin in a biological specimen. |
| C75369 | Secobarbital | Secobarbital | A measurement of the secobarbital present in a biological specimen. |
| C74871 | Secretin | Secretin | A measurement of the secretin hormone in a biological specimen. |
| C105744 | Sediment Examination | Microscopic Sediment Analysis; Sediment Analysis; Sediment Examination | An observation, assessment or examination of the sediment in a biological specimen. |
| C187825 | Selenium | Selenium | A measurement of the selenium in a biological specimen. |
| C122149 | Serine | Serine | A measurement of the serine in a biological specimen. |
| C74872 | Serotonin | Serotonin | A measurement of the serotonin hormone in a biological specimen. |
| C147432 | Sertraline | Sertraline | A measurement of the sertraline present in a biological specimen. |
| C165982 | Serum Amyloid A1 | PIG4; SAA1; Serum Amyloid A-1 Protein; Serum Amyloid A1 | A measurement of the serum amyloid A1 in a biological specimen. |
| C186093 | Serum-Ascites Albumin Gradient | SAAG; Serum-Ascites Albumin Gradient | A measurement of the serum-ascites albumin gradient, calculated by subtracting the amount of albumin in ascites fluid from the albumin in serum. |
| C74745 | Sex Hormone Binding Globulin | Sex Hormone Binding Globulin; Sex Hormone Binding Protein | A measurement of the sex hormone binding (globulin) protein in a biological specimen. |
| C74625 | Sezary Cells | Sezary Cells | A measurement of the Sezary cells (atypical lymphocytes with cerebriform nuclei) in a biological specimen. |
| C158231 | Sezary Cells/Leukocytes | Sezary Cells/Leukocytes | A relative measurement (ratio or percentage) of the Sezary cells to all leukocytes in a biological specimen. |
| C74655 | Sezary Cells/Lymphocytes | Sezary Cells/Lymphocytes | A relative measurement (ratio or percentage of the Sezary cells (atypical lymphocytes with cerebriform nuclei) to all lymphocytes in a biological specimen. |
| C165983 | SH2 Domain Containing 1A Protein | DSHP; Duncan Disease SH2-Protein; EBVS; IMD5; LYP; MTCP1; SAP; SAP/SH2D1A; SH2 Domain Containing 1A Protein; XLP; XLPD; XLPD1 | A measurement of the SH2 domain containing 1A protein in a biological specimen. |
| C130120 | Shellfish Mix Antigen IgE Antibody | Shellfish Mix Antigen IgE Antibody | A measurement of the shellfish mix antigen IgE antibody in a biological specimen. |
| C130121 | Shellfish Mix Antigen IgG Antibody | Shellfish Mix Antigen IgG Antibody | A measurement of the shellfish mix antigen IgG antibody in a biological specimen. |
| C165930 | Shellfish Mix IgE AB RAST Score | Shellfish Mix IgE AB RAST Score | A classification of the amount of shellfish mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165912 | Shellfish Mix IgG AB RAST Score | Shellfish Mix IgG AB RAST Score | A classification of the amount of shellfish mix IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C114223 | Sialyl SSEA-1 Antigen | Sialyl Lewis X Antigen; Sialyl Lex; Sialyl SSEA-1 Antigen; Sialyl-CD15; SLeX | A measurement of the sialyl stage-specific embryonic antigen-1 in a biological specimen. |
| C184635 | Sibutramine | Sibutramine | A measurement of the sibutramine in a biological specimen. |
| C74626 | Sickle Cells | Drepanocytes; Sickle Cells | A measurement of the sickle cells (sickle shaped red blood cells) in a biological specimen. |
| C74656 | Sickle Cells/Erythrocytes | Sickle Cells/Erythrocytes | A relative measurement (ratio or percentage) of the sickle cells (sickle shaped red blood cells) to all erythrocytes in a biological specimen. |
| C100418 | Sideroblast | Sideroblast | A measurement of the sideroblasts (nucleated erythroblasts with iron granules in the cytoplasm) in a biological specimen. |
| C130077 | Silver Birch Pollen IgA | Silver Birch Pollen IgA | A measurement of the Betula verrucosa pollen antigen IgA antibody in a biological specimen. |
| C165921 | Silver Birch Pollen IgE AB RAST Score | Silver Birch Pollen IgE AB RAST Score | A classification of the amount of Betula pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130076 | Silver Birch Pollen IgE | Silver Birch Pollen IgE | A measurement of the Betula verrucosa pollen antigen IgE antibody in a biological specimen. |
| C165899 | Silver Birch Pollen IgG AB RAST Score | Silver Birch Pollen IgG AB RAST Score | A classification of the amount of Betula verrucosa pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130078 | Silver Birch Pollen IgG | Silver Birch Pollen IgG | A measurement of the Betula verrucosa pollen antigen IgG antibody in a biological specimen. |
| C130079 | Silver Birch Pollen IgG4 | Silver Birch Pollen IgG4 | A measurement of the Betula verrucosa pollen antigen IgG4 antibody in a biological specimen. |
| C92236 | Sjogrens SS-A Antibody | Ro Antibody; Sjogrens SS-A Antibody | A measurement of the Sjogrens SS-A antibody in a biological specimen. |
| C120661 | Sjogrens SS-A52 Antibody | Sjogrens SS-A52 Antibody | A measurement of the Sjogrens SS-A52 antibody in a biological specimen. |
| C120662 | Sjogrens SS-A60 Antibody | Sjogrens SS-A60 Antibody | A measurement of the Sjogrens SS-A60 antibody in a biological specimen. |
| C92237 | Sjogrens SS-B Antibody | La Antibody; Sjogrens SS-B Antibody | A measurement of the Sjogrens SS-B antibody in a biological specimen. |
| C135443 | Skeletal Troponin I | Skeletal Troponin I; sTnl | A measurement of the total skeletal troponin I in a biological specimen. |
| C92281 | Smith Antibody | Smith Antibody; Smith Extractable Nuclear Antibody | A measurement of the total Smith antibodies in a biological specimen. |
| C111317 | Smooth Muscle Antibody | Anti-Smooth Muscle Antibody; Smooth Muscle Antibody | A measurement of the total smooth muscle antibody in a biological specimen. |
| C122151 | Smooth Muscle IgG Antibody | Actin IgG Antibody; Smooth Muscle IgG Antibody | A measurement of the smooth muscle IgG antibody in a biological specimen. |
| C74627 | Smudge Cells | Basket Cells; Gumprecht Shadow Cells; Shadow Cells; Smudge Cells | A measurement of the smudge cells (the nuclear remnant of a ruptured white blood cell) in a biological specimen. |
| C119294 | Smudge Cells/Leukocytes | Basket Cells/Leukocytes; Gumprecht Shadow Cells/Leukocytes; Shadow Cells/Leukocytes; Smudge Cells/Leukocytes | A relative measurement (ratio or percentage) of smudge cells to leukocytes in a biological specimen. |
| C106568 | Sodium Clearance | Sodium Clearance | A measurement of the volume of serum or plasma that would be cleared of sodium by excretion of urine for a specified unit of time (e.g. one minute). |
| C150823 | Sodium Excretion Rate | Sodium Excretion Rate | A measurement of the amount of sodium being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C64809 | Sodium | Sodium | A measurement of the sodium in a biological specimen. |
| C79464 | Sodium/Creatinine | Sodium/Creatinine | A relative measurement (ratio or percentage) of the sodium to creatinine in a biological specimen. |
| C122137 | Sodium/Potassium | Sodium/Potassium | A relative measurement (ratio or percentage) of the sodium to potassium in a biological specimen. |
| C170577 | Soluble B Cell Maturation Antigen | Soluble B Cell Maturation Antigen; Soluble BCM; Soluble BCMA; Soluble CD269; Soluble TNF Receptor Superfamily Member 17; Soluble TNFRSF13A | A measurement of the soluble B cell maturation antigen in a biological specimen. |
| C154728 | Soluble CD163 | Soluble CD163 | A measurement of the soluble CD163 in a biological specimen. |
| C187826 | Soluble CD38 | Cyclic ADP Ribose Hydrolase; Soluble CD38 | A measurement of the soluble CD38 protein in a biological specimen. |
| C170579 | Soluble Complement C5b-9 | sC5b-9; Smac; Soluble Complement C5b-9; Soluble MAC; Soluble Membrane Attack Complex; TCC; Terminal Complement Complex | A measurement of the soluble complement C5b-9 in a biological specimen. |
| C119273 | Soluble E-Selectin | sE-selectin; Soluble E-Selectin | A measurement of the soluble E-Selectin in a biological specimen. |
| C112291 | Soluble HER2 | HER2 Antigen; HER2/NEU Antigen; HER2/NEU Shed Antigen; Soluble HER2; Soluble HER2/NEU | A measurement of the soluble HER2 protein in a biological specimen. |
| C117835 | Soluble Immunoglobulin | Soluble Immunoglobulin | A measurement of the soluble total immunoglobulin in a biological specimen. |
| C132386 | Soluble Intercell Adhesion Molecule 1 | Soluble Intercell Adhesion Molecule 1 | A measurement of the soluble intercellular adhesion molecule 1 in a biological specimen. |
| C186096 | Soluble Intercell Adhesion Molecule 4 | Soluble Intercell Adhesion Molecule 4; Soluble Intercellular Adhesion Molecule 4 | A measurement of the soluble intercellular adhesion molecule 4 in a biological specimen. |
| C158220 | Soluble Interleukin 2 Receptor | sCD25; Soluble CD25; Soluble IL-2Ra; Soluble Interleukin 2 Receptor; Soluble Interleukin 2 Receptor Subunit Alpha | A measurement of the soluble interleukin 2 receptor in a biological specimen. |
| C117837 | Soluble Interleukin 6 Receptor | Soluble Interleukin 6 Receptor | A measurement of the soluble interleukin 6 receptor in a biological specimen. |
| C117836 | Soluble Interleukin-1 Receptor Type I | Soluble Interleukin-1 Receptor Type I | A measurement of the soluble interleukin-1 receptor type I in a biological specimen. |
| C165971 | Soluble Kidney Injury Molecule-1 | Soluble Hepatitis A Virus Cellular Receptor 1; Soluble Kidney Injury Molecule-1; Soluble KIM-1 | A measurement of the soluble kidney injury molecule-1 in a biological specimen. |
| C172495 | Soluble L-Selectin | sL-Selectin; Soluble CD62L; Soluble L-Selectin | A measurement of the soluble L-selectin in a biological specimen. |
| C122150 | Soluble Liver Antigen IgG Antibody | Soluble Liver Antigen IgG Antibody | A measurement of the soluble liver antigen IgG antibody in a biological specimen. |
| C172504 | Soluble Lymphocyte Activation Gene-3 | Soluble CD223 Antigen; Soluble LAG-3; Soluble Lymphocyte Activation Gene 3 Protein; Soluble Lymphocyte Activation Gene-3 | A measurement of the soluble lymphocyte activation gene-3 protein in a biological specimen. |
| C189495 | Soluble Mesothelin Related Peptides | Soluble Mesothelin Related Peptides; Soluble Mesothelin Related Proteins | A measurement of the soluble mesothelin related peptides in a biological specimen. |
| C120650 | Soluble P-Selectin | Soluble P-Selectin | A measurement of the soluble P-selectin in a biological specimen. |
| C172503 | Soluble Programmed Death Ligand 1 | Soluble CD274; Soluble PD-L1; Soluble PDL1; Soluble Programmed Death Ligand 1 | A measurement of the soluble programmed death ligand 1 in a biological specimen. |
| C172505 | Soluble Programmed Death-1 | Soluble CD279; Soluble PD-1; Soluble PD1; Soluble Programmed Cell Death Protein 1; Soluble Programmed Death-1 | A measurement of the soluble programmed death-1 protein in a biological specimen. |
| C174312 | Soluble TNF Receptor Superfamily Mem 5 | Soluble B-cell Surface Antigen CD40; Soluble Bp50; Soluble CD40; Soluble CDW40; Soluble p50; Soluble TNF Receptor Superfamily Mem 5; Soluble TNF Receptor Superfamily Member 5; Soluble TNFRSF5; Soluble Tumor Necrosis Factor Receptor Superfamily, Member 5 | A measurement of the soluble tumor necrosis factor receptor superfamily member 5 (CD40) in a biological specimen. |
| C117863 | Soluble TNF Receptor Type I | Soluble TNF Receptor Type I | A measurement of the soluble tumor necrosis factor receptor type I in a biological specimen. |
| C117864 | Soluble TNF Receptor Type II | Soluble CD120b; Soluble TNF Receptor 1B; Soluble TNF Receptor Type II; Soluble TNFR1B | A measurement of the soluble tumor necrosis factor receptor type II in a biological specimen. |
| C156526 | Soluble TNF Superfamily Member 12 | Soluble TNF Superfamily Member 12; Soluble TNFSF12 | A measurement of soluble tumor necrosis factor superfamily member 12 in a biological specimen. |
| C174308 | Soluble TNF Superfamily Member 5 | Soluble CD154; Soluble CD40 Ligand; Soluble CD40L; Soluble CD40LG; Soluble gp39; Soluble T-BAM; Soluble TNF Superfamily Member 5; Soluble TNFSF5; Soluble TRAP | A measurement of the soluble tumor necrosis factor superfamily member 5 in a biological specimen. |
| C100438 | Soluble Transferrin Receptor | Soluble Transferrin Receptor | A measurement of the soluble transferrin receptor in a biological specimen. |
| C117749 | Soluble Tumor Necrosis Factor Receptor | Soluble Tumor Necrosis Factor Receptor | A measurement of the total soluble tumor necrosis factor receptor in a biological specimen. |
| C92533 | Soluble Vasc Cell Adhesion Molecule 1 | Soluble Vasc Cell Adhesion Molecule 1 | A measurement of the soluble vascular cell adhesion molecule 1 in a biological specimen. |
| C165992 | Soluble Vasc Endoth Growth Factor Rec1 | Soluble Vasc Endoth Growth Factor Rec1; Soluble Vascular Endothelial Growth Factor Receptor 1 | A measurement of the soluble vascular endothelial growth factor receptor 1 in a biological specimen. |
| C165993 | Soluble Vasc Endoth Growth Factor Rec2 | Soluble Vasc Endoth Growth Factor Rec2; Soluble Vascular Endothelial Growth Factor Receptor 2 | A measurement of the soluble vascular endothelial growth factor receptor 2 in a biological specimen. |
| C165994 | Soluble Vasc Endoth Growth Factor Rec3 | Soluble Vasc Endoth Growth Factor Rec3; Soluble Vascular Endothelial Growth Factor Receptor 3 | A measurement of the soluble vascular endothelial growth factor receptor 3 in a biological specimen. |
| C165984 | Somatostatin Receptor Type 2 | Somatostatin Receptor Type 2; SRIF-1 | A measurement of the somatostatin receptor type 2 in a biological specimen. |
| C80360 | Somatotrophin | Growth Hormone; Somatotrophin; Somatotropin | A measurement of the somatotrophin (growth) hormone in a biological specimen. |
| C177989 | Sonic Hedgehog | Sonic Hedgehog | A measurement of the sonic hedgehog protein in a biological specimen. |
| C79465 | Sorbitol Dehydrogenase | Sorbitol Dehydrogenase | A measurement of the sorbitol dehydrogenase in a biological specimen. |
| C64832 | Specific Gravity | Specific Gravity | A ratio of the density of a fluid to the density of water. |
| C179695 | Specimen Appearance | Specimen Appearance | The outward or visible aspect of a specimen. |
| C106569 | Specimen Weight | Specimen Weight | A measurement of the weight of a biological specimen. |
| C142290 | Sperm Agglutination | Sperm Agglutination | A measurement of the motile spermatozoa agglutination in a biological specimen. |
| C142291 | Sperm Aggregation | Sperm Aggregation | A measurement of the immotile spermatozoa aggregation in a biological specimen. |
| C102281 | Sperm Motility | Sperm Motility | A measurement of the sperm capable of forward, progressive movement in a semen specimen. |
| C74663 | Spermatozoa | Spermatozoa | A measurement of the spermatozoa cells present in a biological specimen. |
| C161366 | Spermatozoa, Progressive | Spermatozoa, Progressive | A measurement of the progressive spermatozoa (motile in a forward direction) in a biological specimen. |
| C161365 | Spermatozoa, Progressive/Spermatozoa | Spermatozoa, Progressive/Spermatozoa | A relative measurement (ratio or percentage) of the progressive spermatozoa to total spermatozoa in a biological specimen. |
| C74707 | Spherocytes | Spherocytes | A measurement of the spherocytes (small, sphere-shaped red blood cells) in a biological specimen. |
| C120660 | Squamous Cell Carcinoma Antigen | Squamous Cell Carcinoma Antigen | A measurement of the squamous cell carcinoma antigen in a biological specimen. |
| C74773 | Squamous Epithelial Cells | Squamous Cells; Squamous Epithelial Cells | A measurement of the squamous epithelial cells present in a biological specimen. |
| C132366 | Squamous Epithelial Cells/Total Cells | Squamous Epithelial Cells/Total Cells | A relative measurement (ratio or percentage) of the squamous epithelial cells to total cells in a biological specimen. |
| C74774 | Squamous Transitional Epithelial Cells | Squamous Transitional Epithelial Cells | A measurement of the squamous transitional epithelial cells present in a biological specimen. |
| C154721 | Standard Base Excess | Standard Base Excess | A calculated measurement of the amount of acid required to return blood with hemoglobin at 5g/dL, which is used as a surrogate for extracellular fluid, to a normal pH under standard conditions. |
| C184599 | Stanozolol | Stanozolol | A measurement of the stanozolol in a biological specimen. |
| C81951 | Starch Crystals | Starch Crystals; Starch Granules | A measurement of the starch crystals in a biological specimen. |
| C156469 | STAT3 | Signal Transducer and Activator of Transcription 3; STAT3 | A measurement of the STAT3 (signal transducer and activator of transcription 3) in a biological specimen. |
| C82035 | Stem Cell Factor | KIT Ligand; Stem Cell Factor | A measurement of the stem cell factor in a biological specimen. |
| C184600 | Stenbolone | Deacetylanatrofin; Stenbolone | A measurement of the stenbolone in a biological specimen. |
| C177993 | Steroid Sulfatase | Steroid Sulfatase; Steryl-sulfatase | A measurement of the steroid sulfatase in a biological specimen. |
| C74708 | Stomatocytes | Stomatocytes | A measurement of the stomatocytes (red blood cells with an oval or rectangular area of central pallor, producing the appearance of a cell mouth) in a biological specimen. |
| C186095 | Succinylacetone | Succinylacetone | A measurement of the succinylacetone in a biological specimen. |
| C184575 | Sufentanil | Sufentanil | A measurement of the sufentanil in a biological specimen. |
| C74755 | Sulfa Crystals | Sulfa Crystals; Sulfonamide Crystals | A measurement of the sulfa crystals present in a biological specimen. |
| C122153 | Sulfate | Sulfate; Sulphate | A measurement of the sulfate in a biological specimen. |
| C114224 | Sulfur Dioxide | Sulfur Dioxide | A measurement of the sulfur dioxide in a biological specimen. |
| C111322 | Surfactant Protein D | SP-D; Surfactant Protein D | A measurement of the surfactant protein D in a biological specimen. |
| C158232 | Symmetric Dimethylarginine | N,N'-dimethylarginine; Symmetric Dimethylarginine | A measurement of the symmetric dimethylarginine in a biological specimen. |
| C132387 | T-Kininogen | T-Kininogen | A measurement of the total T-kininogen in a biological specimen. |
| C128979 | T-lymphocyte Crossmatch | T-lymphocyte Crossmatch | A measurement to determine human leukocyte antigens (HLA) histocompatibility between the recipient and the donor by examining the presence or absence of the recipient's anti-HLA antibody reactivity towards HLA antigens expressed on the donor T-lymphocytes. |
| C122157 | T-Lymphocytes | T-Cell Lymphocytes; T-Cells; T-Lymphocytes | A measurement of the total thymocyte-derived lymphocytes in a biological specimen. |
| C147408 | T1 Collagen X-link N-Telopeptides/Creat | T1 Collagen X-link N-Telopeptides/Creat; Type I Collagen X-linked N-Telopeptides/Creatinine | A relative measurement (ratio or percentage) of the type 1 collagen cross-linked N-telopeptides to creatinine in a biological specimen. |
| C184576 | Tapentadol | Tapentadol | A measurement of the tapentadol in a biological specimen. |
| C96636 | Target Cells | Codocytes; Target Cells | A measurement of the target cells in a biological specimen. |
| C117865 | Tartrate-Resistant Acid Phosphatase 5b | Tartrate-Resistant Acid Phosphatase 5b; TRAP5B | A measurement of tartrate-resistant acid phosphatase 5b in a biological specimen. |
| C189496 | TATA Box Binding Protein | TATA Box Binding Protein; TATA-Binding Protein | A measurement of the TATA-box binding protein in a biological specimen. |
| C84810 | Tau Protein | Tau Protein; Total Tau Protein | A measurement of the total Tau protein in a biological specimen. |
| C163489 | Tau Protein, Free | Tau Protein, Free | A measurement of the free tau protein in a biological specimen. |
| C122154 | Taurine | Tauric Acid; Taurine | A measurement of the taurine in a biological specimen. |
| C158223 | Taurine/Creatinine | Taurine/Creatinine | A relative measurement (ratio) of the taurine to the creatinine in a biological specimen. |
| C176306 | Taurochenodeoxycholate | Taurochenodeoxycholate; Taurochenodeoxycholic Acid | A measurement of the taurochenodeoxycholate in a biological specimen. |
| C176301 | Taurocholate | Taurocholate; Taurocholic Acid | A measurement of the taurocholate in a biological specimen. |
| C176309 | Taurolithocholate | Taurolithocholate; Taurolithocholic Acid | A measurement of the taurolithocholate in a biological specimen. |
| C176303 | Tauroursodeoxycholate | Tauroursodeoxycholate; Tauroursodeoxycholic Acid | A measurement of the tauroursodeoxycholate in a biological specimen. |
| C75376 | Temazepam | Temazepam | A measurement of the temazepam present in a biological specimen. |
| C117859 | Terminal Deoxynucleotidyl Transferase Ag | Terminal Deoxynucleotidyl Transferase Ag; Terminal Deoxynucleotidyl Transferase Antigen | A measurement of the terminal deoxynucleotidyl transferase antigen in a biological specimen. |
| C184601 | Testolactone | Testolactone | A measurement of the testolactone in a biological specimen. |
| C147440 | Testosterone Free+Weakly Bound/Testost | Testosterone Free+Weakly Bound/Testost; Testosterone, Free and Weakly Bound/Testosterone | A relative measurement (ratio or percentage) of the free and weakly bound testosterone to total testosterone in a biological specimen. |
| C74793 | Testosterone | Testosterone; Total Testosterone | A measurement of the total (free and bound) testosterone in a biological specimen. |
| C74785 | Testosterone, Free | Testosterone, Free | A measurement of the free testosterone in a biological specimen. |
| C147439 | Testosterone, Free/Testosterone | Testosterone, Free/Testosterone | A relative measurement (ratio or percentage) of the amount of the bioavailable testosterone compared to total testosterone in a biological specimen. |
| C128980 | Testosterone, Free/Total Protein | Testosterone, Free/Total Protein | A relative measurement (ratio or percentage) of free testosterone to total proteins in a biological specimen. |
| C147434 | Testosterone, Weakly Bound | Testosterone, Weakly Bound | A measurement of the weakly bound testosterone (testosterone bound to albumin) in a biological specimen. |
| C147436 | Tetrahydrocannabinol | Delta-9-Tetrahydrocannabinol; Tetrahydrocannabinol; THC | A measurement of the tetrahydrocannabinol in a biological specimen. |
| C184602 | Tetrahydrogestrinone | Tetrahydrogestrinone | A measurement of the tetrahydrogestrinone in a biological specimen. |
| C184577 | Thebaine | Thebaine | A measurement of the thebaine in a biological specimen. |
| C105445 | Theophylline | Theophylline | A measurement of the Theophylline present in a biological specimen. |
| C74896 | Thiamine | Thiamine; Vitamin B1 | A measurement of the thiamine in a biological specimen. |
| C184603 | Thiamylal | Thiamylal | A measurement of the thiamylal in a biological specimen. |
| C154745 | Thiocyanate | Thiocyanate | A measurement of the thiocyanate in a biological specimen. |
| C184604 | Thiopental | Thiopental | A measurement of the thiopental in a biological specimen. |
| C177978 | Thioridazine | Thioridazine | A measurement of the thioridazine in a biological specimen. |
| C177976 | Thiothixene | Thiothixene | A measurement of the thiothixene in a biological specimen. |
| C122156 | Threonine | Threonine | A measurement of the threonine in a biological specimen. |
| C158224 | Threonine/Creatinine | Threonine/Creatinine | A relative measurement (ratio) of the threonine to the creatinine in a biological specimen. |
| C147437 | Thrombin Activity Actual/Control | Thrombin Activity Actual/Control; Thrombin Activity Actual/Normal; Thrombin Activity Actual/Thrombin Activity Control | A relative measurement (ratio or percentage) of the biological activity of thrombin dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C161371 | Thrombin Antithrombin Complex | TAT; Thrombin Antithrombin Complex; Thrombin Antithrombin Complex Antigen | A measurement of the thrombin-antithrombin complexes in a biological specimen. |
| C161370 | Thrombin Time Actual/Control | Thrombin Time Actual/Control | A relative measurement (ratio or percentage) of the thrombin time in a subject's specimen when compared to a control specimen. |
| C80365 | Thrombin Time | Thrombin Time | A measurement of the time it takes a plasma sample to clot after adding the active enzyme thrombin. (NCI) |
| C106574 | Thrombin/Antithrombin | Thrombin/Antithrombin; Thrombin/Antithrombin III | A relative measurement (ratio or percentage) of the thrombin to antithrombin present in a sample. |
| C111283 | Thrombocytes | Nucleated Thrombocytes; Thrombocytes | A measurement of the nucleated platelets, namely thrombocytes, in a biological specimen. This is typically measured in birds and other non-mammalian vertebrates. |
| C135444 | Thrombomodulin | BDCA3; Thrombomodulin | A measurement of the thrombomodulin in a biological specimen. |
| C74873 | Thrombopoietin | Thrombopoietin | A measurement of the thrombopoietin hormone in a biological specimen. |
| C163495 | Thrombospondin 1 | THBS1; Thrombospondin 1 | A measurement of the thrombospondin 1 in a biological specimen. |
| C103445 | Thromboxane B2 | Thromboxane B2 | A measurement of the thromboxane B2 in a biological specimen. |
| C184511 | Thymic Stromal Lymphopoietin | Thymic Stromal Lymphopoietin | A measurement of the thymic stromal lymphopoietin in a biological specimen. |
| C135445 | Thymidine Kinase 1 | Thymidine Kinase 1; Thymidine Kinase, Cytosolic | A measurement of the thymidine kinase 1 in a biological specimen. |
| C135446 | Thymidine Kinase 2 | Thymidine Kinase 2; Thymidine Kinase, Mitochondrial | A measurement of the thymidine kinase 2 in a biological specimen. |
| C120665 | Thymidine Kinase | Thymidine Kinase | A measurement of the total thymidine kinase in a biological specimen. |
| C147435 | Thyroglobulin Recovery Rate | Thyroglobulin Recovery Rate | A measurement of the thyroglobulin recovery rate in a biological specimen obtained by measuring the thyroglobulin concentration before and after a known amount of thyroglobulin has been added to the specimen. |
| C103446 | Thyroglobulin | TG; Thyroglobulin | A measurement of the thyroglobulin in a biological specimen. |
| C81990 | Thyroid Antibodies | Thyroid Antibodies | A measurement of the thyroid antibodies in a biological specimen. |
| C81992 | Thyroid Antithyroglobulin Antibodies | Thyroid Antithyroglobulin Antibodies | A measurement of the thyroid antithyroglobulin antibodies in a biological specimen. |
| C147438 | Thyroid Stimulating Immunoglobulin | Thyroid Stimulating Immunoglobulin | A measurement of the thyroid stimulating immunoglobulin in a biological specimen. |
| C96638 | Thyroperoxidase Antibody | Thyroid Antimicrosomal Antibody; Thyroperoxidase Antibody | A measurement of the thyroperoxidase antibody in a biological specimen. |
| C96639 | Thyroperoxidase | Thyroid Peroxidase; Thyroperoxidase | A measurement of the thyroperoxidase in a biological specimen. |
| C122158 | Thyrotropin Receptor Antibody | Thyroid Stimulating Hormone Receptor Antibody; Thyrotropin Receptor Antibody | A measurement of the thyrotropin receptor antibody in a biological specimen. |
| C74874 | Thyrotropin Releasing Hormone | Thyrotropin Releasing Factor; Thyrotropin Releasing Hormone | A measurement of the thyrotropin releasing hormone in a biological specimen. |
| C64813 | Thyrotropin | Thyroid Stimulating Hormone; Thyrotropin | A measurement of the thyrotropin in a biological specimen. |
| C181446 | Thyrotropin/Thyroxine, Free | Thyroid Stimulating Hormone/Free T4; Thyrotropin/Thyroxine, Free | A relative measurement (ratio) of the thyrotropin to free thyroxine in a biological specimen. |
| C74746 | Thyroxine Binding Globulin | Thyroxine Binding Globulin | A measurement of the thyroxine binding globulin protein in a biological specimen. |
| C74794 | Thyroxine | Thyroxine; Total T4 | A measurement of the total (free and bound) thyroxine in a biological specimen. |
| C170598 | Thyroxine, Free Index | Thyroxine, Free Index | A measurement of the thyroid status in a biological specimen. This is calculated by a mathematical formula that takes into account the total thyroxine and unbound thyroxine binding globulins. |
| C74786 | Thyroxine, Free | Free T4; Thyroxine, Free | A measurement of the free thyroxine in a biological specimen. |
| C120664 | Thyroxine, Free, Indirect | Thyroxine, Free, Indirect | An indirect measurement of the free thyroxine in a biological specimen. |
| C130089 | Timothy Grass Pollen IgA | Timothy Grass Pollen IgA | A measurement of the Phleum pratense pollen antigen IgA antibody in a biological specimen. |
| C165890 | Timothy Grass Pollen IgE AB RAST Score | Timothy Grass Pollen IgE AB RAST Score | A classification of the amount of Phleum pratense pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130088 | Timothy Grass Pollen IgE | Timothy Grass Pollen IgE | A measurement of the Phleum pratense pollen antigen IgE antibody in a biological specimen. |
| C165902 | Timothy Grass Pollen IgG AB RAST Score | Timothy Grass Pollen IgG AB RAST Score | A classification of the amount of Phleum pratense pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130090 | Timothy Grass Pollen IgG | Timothy Grass Pollen IgG | A measurement of the Phleum pratense pollen antigen IgG antibody in a biological specimen. |
| C130091 | Timothy Grass Pollen IgG4 | Timothy Grass Pollen IgG4 | A measurement of the Phleum pratense pollen antigen IgG4 antibody in a biological specimen. |
| C106575 | TIMP1/Creatinine | TIMP1/Creatinine; Tissue Inhibitor of Metalloproteinase 1/Creatinine | A relative measurement (ratio or percentage) of the tissue inhibitor of metalloproteinase 1 to creatinine present in a sample. |
| C82036 | Tissue Inhibitor of Metalloproteinase 1 | Tissue Inhibitor of Metalloproteinase 1 | A measurement of the tissue inhibitor of metalloproteinase 1 in a biological specimen. |
| C165988 | Tissue Inhibitor of Metalloproteinase 3 | HSMRK222; K222; K222TA2; Metalloproteinase Inhibitor 3; SFD; Tissue Inhibitor of Metalloproteinase 3 | A measurement of the tissue inhibitor of metalloproteinase 3 in a biological specimen. |
| C81993 | Tissue Plasminogen Activator Antigen | Tissue Plasminogen Activator Antigen | A measurement of the tissue plasminogen activator antigen in a biological specimen. |
| C163488 | Tissue Polypeptide Antigen | Tissue Polypeptide Antigen; TPA | A measurement of the tissue polypeptide antigen in a biological specimen. |
| C147441 | Tissue Transglutaminase IgA Antibody | Tissue Transglutaminase IgA Antibody | A measurement of the tissue transglutaminase IgA antibody in a biological specimen. |
| C163496 | Tissue Transglutaminase IgG Antibody | Tissue Transglutaminase IgG Antibody | A measurement of the tissue transglutaminase IgG antibody in a biological specimen. |
| C147442 | Tissue Transglutaminase IgM Antibody | Tissue Transglutaminase IgM Antibody | A measurement of the tissue transglutaminase IgM antibody in a biological specimen. |
| C165991 | TNF Receptor 1B | CD120b; p75; p75TNFR; TBPII; TNF Receptor 1B; TNF-R-II; TNF-R75; TNFBR; TNFR1B; TNFR2; TNFR80; Tumor Necrosis Factor Receptor 2 | A measurement of the tumor necrosis factor receptor superfamily member 1B in a biological specimen. |
| C165989 | TNF Superfamily Member 10 | APO2L; CD253; TL2; TNF-Related Apoptosis-Inducing Ligand; TNFSF10; TNLG6A; TRAIL | A measurement of the total tumor necrosis factor superfamily member 10 in a biological specimen. |
| C156525 | TNF Superfamily Member 12 Excretion Rate | TNF Superfamily Member 12 Excretion Rate; TWEAK Excretion Rate | A measurement of the amount of TNF superfamily member 12 being excreted in a biological specimen over a defined period of time (e.g. one hour). |
| C165990 | TNF Superfamily Member 12 | APO3L; DR3LG; TNF Superfamily Member 12; TNLG4A; TWEAK | A measurement of the total tumor necrosis factor superfamily member 12 in a biological specimen. |
| C117862 | TNF-a Production Inhibition | TNF-a Production Inhibition; TNF-a Production Inhibitory Activity | A measurement of TNF-a production inhibitory activity in a biological specimen. |
| C187827 | Tomoregulin-2 | Tomoregulin-2; Transmembrane Protein With EGF-Like And Two Follistatin-Like Domains 2 | A measurement of the tomoregulin-2 in a biological specimen. |
| C119269 | Total Amyloid Precursor Protein | Total Amyloid Precursor Protein | A measurement of the total amyloid precursor protein present in a biological specimen. |
| C74718 | Total Iron Binding Capacity | Total Iron Binding Capacity | A measurement of the amount of iron needed to fully saturate the transferrin in a biological specimen. |
| C128974 | Total Plasma Cells | Total Plasma Cells | A measurement of the total plasma cells in a biological specimen. |
| C128975 | Total Plasma Cells/Leukocytes | Total Plasma Cells/Leukocytes | A relative measurement (ratio or percentage) of the total plasma cells to leukocytes in a biological specimen. |
| C189499 | Total Plasma Cells/Lymphocytes | Total Plasma Cells/Lymphocytes | A relative measurement (ratio or percentage) of the total plasma cells to lymphocytes in a biological specimen. |
| C187987 | Total Plasma Cells/Total Cells | Total Plasma Cells/Total Cells | A relative measurement (ratio or percentage) of the total plasma cells to total cells in a biological specimen. |
| C80208 | Total Radical-Trap Antioxidant Potential | Total Radical-Trap Antioxidant Potential | A measurement of the ability of the antioxidants in a biological specimen to buffer free radicals in a suspension. |
| C96641 | Toxic Granulation | Toxic Granulation | A measurement of the toxic granulation in granulocytic blood cells. |
| C127813 | Toxic Vacuolation | Toxic Vacuolation | A measurement of the toxic vacuolation in any of the granulocytic blood cells. |
| C163490 | TPR-Ankyrin Repeat-Containing Protein 1 | TPR and Ankyrin Repeat-Containing Protein 1; TPR-Ankyrin Repeat-Containing Protein 1 | A measurement of the TPR-ankyrin repeat-containing protein 1 in a biological specimen. |
| C161376 | Tramadol | Tramadol | A measurement of the tramadol present in a biological specimen. |
| C98792 | Transferrin Saturation | Iron Binding Capacity Saturation; Iron Saturation; Iron to TIBC; Transferrin Saturation | A measurement of the iron bound to transferrin in a biological specimen. |
| C82037 | Transferrin | Transferrin | A measurement of the total transferrin in a biological specimen. |
| C165985 | Transforming Growth Factor Alpha | Transforming Growth Factor Alpha | A measurement of the transforming growth factor alpha in a biological specimen. |
| C117861 | Transforming Growth Factor Beta 1 | Transforming Growth Factor Beta 1 | A measurement of the transforming growth factor beta 1 in a biological specimen. |
| C165986 | Transforming Growth Factor Beta 2 | G-TSF; LDS4; TGF-beta2; Transforming Growth Factor Beta 2 | A measurement of the transforming growth factor beta 2 in a biological specimen. |
| C165987 | Transforming Growth Factor Beta 3 | ARVD; ARVD1; LDS5; RNHF; TGF-beta3; Transforming Growth Factor Beta 3 | A measurement of the transforming growth factor beta 3 in a biological specimen. |
| C122155 | Transforming Growth Factor Beta | Transforming Growth Factor Beta | A measurement of the total transforming growth factor beta in a biological specimen. |
| C92251 | Transitional Epithelial Cells | Transitional Epithelial Cells | A measurement of the transitional epithelial cells present in a biological specimen. |
| C163487 | Translocase Inner Mitochondrial Membr 10 | Translocase Inner Mitochondrial Membr 10; Translocase of Inner Mitochondrial Membrane 10 | A measurement of the translocase of inner mitochondrial membrane 10 in a biological specimen. |
| C187828 | Trazodone | Trazodone | A measurement of the trazodone in a biological specimen. |
| C130101 | Tree Mix Pollen Antigen IgE Antibody | Tree Mix Pollen Antigen IgE Antibody | A measurement of the tree mix pollen antigen IgE antibody in a biological specimen. |
| C130102 | Tree Mix Pollen Antigen IgG Antibody | Tree Mix Pollen Antigen IgG Antibody | A measurement of the tree mix pollen antigen IgG antibody in a biological specimen. |
| C165923 | Tree Mix Pollen IgE AB RAST Score | Tree Mix Pollen IgE AB RAST Score | A classification of the amount of tree mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165904 | Tree Mix Pollen IgG AB RAST Score | Tree Mix Pollen IgG AB RAST Score | A classification of the amount of tree mix pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C184605 | Trenbolone | 17beta-Trenbolone; Trenbolone; Trienbolone | A measurement of the trenbolone in a biological specimen. |
| C181451 | Triazolam | Triazolam | A measurement of the triazolam in a biological specimen. |
| C92238 | Trichomonas | Trichomonas | Examination of a biological specimen to detect the presence of any protozoan belonging to the Trichomonas genus. |
| C100420 | Tricyclic Antidepressants | Tricyclic Antidepressants | A measurement of tricyclic antidepressants in a biological specimen. |
| C177982 | Trifluoperazine | Trifluoperazine | A measurement of the trifluoperazine in a biological specimen. |
| C64812 | Triglycerides | Triglycerides | A measurement of the triglycerides in a biological specimen. |
| C121183 | Triglycerides/HDL Cholesterol | Triglycerides/HDL Cholesterol | A relative measurement (ratio or percentage) of the triglycerides to high density lipoprotein cholesterol in a biological specimen. |
| C74748 | Triiodothyronine Uptake | T3RU; T3U; Triiodothyronine Uptake | A measurement of the binding of triiodothyronine to thyroxine binding globulin protein in a biological specimen. |
| C74747 | Triiodothyronine | Total T3; Triiodothyronine | A measurement of the total (free and bound) triiodothyronine in a biological specimen. |
| C74787 | Triiodothyronine, Free | Free T3; Triiodothyronine, Free | A measurement of the free triiodothyronine in a biological specimen. |
| C81968 | Triiodothyronine, Reverse | Triiodothyronine, Reverse | A measurement of the reverse triiodothyronine in a biological specimen. |
| C184563 | Trimeperidine | Trimeperidine | A measurement of the trimeperidine in a biological specimen. |
| C163491 | Tripartite Motif Containing Protein 21 | E3 Ubiquitin-Protein Ligase TRIM21; Ro(SS-A); Sjogren Syndrome Type A Antigen; Tripartite Motif Containing Protein 21 | A measurement of the tripartite motif containing protein 21 in a biological specimen. |
| C163492 | Tripartite Motif Containing Protein 38 | Tripartite Motif Containing Protein 38 | A measurement of the tripartite motif containing protein 38 in a biological specimen. |
| C74756 | Triple Phosphate Crystals | Ammonium Magnesium Phosphate Crystals; Struvite Crystals; Triple Phosphate Crystals | A measurement of the triple phosphate crystals present in a biological specimen. |
| C147277 | Triticum aestivum Antigen IgE Antibody | Bread Wheat Antigen IgE Antibody; Triticum aestivum Antigen IgE Antibody | A measurement of the Triticum aestivum antigen IgE antibody in a biological specimen. |
| C165935 | Triticum aestivum IgE AB RAST Score | Triticum aestivum IgE AB RAST Score | A classification of the amount of Triticum aestivum antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C177959 | Triticum Species Antigen IgE Antibody | Triticum Species Antigen IgE Antibody; Wheat Antigen IgE Antibody | A measurement of any of the Triticum species of wheat antigen IgE antibody in a biological specimen. |
| C135447 | Troponin I Type 1 | Slow-Twitch Skeletal Muscle Troponin I; ssTnI; Troponin I Type 1 | A measurement of the troponin I type 1 (slow twitch skeletal muscle) in a biological specimen. |
| C127636 | Troponin I Type 2 | Fast-Twitch Skeletal Muscle Troponin I; fsTnI; Troponin I Type 2 | A measurement of the troponin I type 2 (fast twitch skeletal muscle) in a biological specimen. |
| C135448 | Troponin I Type 3 | Cardiac Troponin I; cTnI; TNNC1; Troponin I Type 3 | A measurement of the troponin I type 3 (cardiac muscle) in a biological specimen. |
| C74749 | Troponin I | Troponin I | A measurement of the actin binding troponin in a biological specimen. |
| C74750 | Troponin T | Troponin T | A measurement of the tropomyosin binding troponin in a biological specimen. |
| C111327 | Troponin | Troponin | A measurement of the total troponin in a biological specimen. |
| C135449 | Trypsin 1 and Trypsinogen 1 | Trypsin 1 and Trypsinogen 1 | A measurement of the trypsin 1 and trypsinogen 1 in a biological specimen. |
| C135450 | Trypsin and Trypsinogen | Trypsin and Trypsinogen | A measurement of the total trypsin and total trypsinogen in a biological specimen. |
| C163494 | Trypsin | Trypsin | A measurement of the trypsin in a biological specimen. |
| C92292 | Tryptase | Tryptase | A measurement of the tryptase in a biological specimen. |
| C154739 | Tryptophan | Tryptophan | A measurement of the tryptophan in a biological specimen. |
| C163493 | Tryptophan/Creatinine | Tryptophan/Creatinine | A relative measurement (ratio or percentage) of the tryptophan to creatinine in a biological specimen. |
| C161368 | TSI Actual/Control | Thyroid Stimulating Immunoglobulin Actual/Control; Thyroid Stimulating Immunoglobulin Actual/Normal; TSI Actual/Control | A relative measurement (ratio or percentage) of the thyroid stimulating immunoglobulin in a subject's specimen when compared to a control specimen. |
| C74775 | Tubular Epithelial Cells | Renal Tubular Epithelial Cells; Tubular Epithelial Cells | A measurement of the tubular epithelial cells present in a biological specimen. |
| C120666 | Tumor Necrosis Factor Receptor 1 | CD120a; Tumor Necrosis Factor Receptor 1 | A measurement of the tumor necrosis factor receptor 1 (CD120a) in a biological specimen. |
| C74751 | Tumor Necrosis Factor | Tumor Necrosis Factor; Tumor Necrosis Factor alpha | A measurement of the total tumor necrosis factor (cachexin) cytokine in a biological specimen. |
| C74723 | Turbidity | Turbidity | A measurement of the opacity of a biological specimen. |
| C187792 | Type I Collagen C-Telopeptides Beta | Beta Isomer of C-Terminal Telopeptide of Type I Collagen; Type I Collagen C-Telopeptides Beta | A measurement of the beta isomer of type I collagen cross-linked C-telopeptides in a biological specimen. |
| C82038 | Type I Collagen C-Telopeptides | C-Terminal Telopeptide of Type I Collagen; Type I Collagen C-Telopeptides; Type I Collagen X-linked C-telopeptide | A measurement of the type I collagen cross-linked C-telopeptides in a biological specimen. |
| C127613 | Type I Collagen C-Telopeptides/Creat | Type I Collagen C-Telopeptides/Creat; Type I Collagen X-Linked C-Telopeptides/Creatinine | A relative measurement (ratio or percentage) of the type I collagen cross-linked C-telopeptides to creatinine in a biological specimen. |
| C82039 | Type I Collagen N-Telopeptides | Type I Collagen N-Telopeptides; Type I Collagen X-Linked N-Telopeptides | A measurement of the type I collagen cross-linked N-telopeptides in a biological specimen. |
| C92283 | Type I Myeloblasts | Type I Myeloblasts | A measurement of type I myeloblast cells per unit of a biological specimen. |
| C82040 | Type II Collagen C-Telopeptides | Type II Collagen C-Telopeptides; Type II Collagen X-Linked C-Telopeptides | A measurement of the type II collagen cross-linked C-telopeptides in a biological specimen. |
| C122113 | Type II Collagen C-Telopeptides/Creat | Type II Collagen C-Telopeptides/Creat; Type II Collagen X-Linked C-Telopeptides/Creatinine | A relative measurement (ratio or percentage) of the type II collagen cross-linked C-telopeptides to creatinine in a biological specimen. |
| C82041 | Type II Collagen N-Telopeptides | Type II Collagen N-Telopeptides; Type II Collagen X-Linked N-Telopeptides | A measurement of the type II collagen cross-linked N-telopeptides in a biological specimen. |
| C92284 | Type II Myeloblasts | Type II Myeloblasts | A measurement of type II myeloblast cells per unit of a biological specimen. |
| C120663 | Type II Secretory Phospholipase A2 | Type II Secretory Phospholipase A2 | A measurement of the type II secretory phospholipase A2 in a biological specimen. |
| C92285 | Type III Myeloblasts | Type III Myeloblasts | A measurement of type III myeloblast cells per unit of a biological specimen. |
| C74683 | Tyrosine Crystals | Tyrosine Crystals | A measurement of the tyrosine crystals present in a biological specimen. |
| C122159 | Tyrosine | Tyrosine | A measurement of the tyrosine in a biological specimen. |
| C184564 | U-47700 | Pink; Pinky; U-47700; U4; U47700 | A measurement of the synthetic cannabinoid U-47700 in a biological specimen. |
| C147321 | Ubiquinone 10 | Coenzyme Q10; Ubiquinone 10 | A measurement of the ubiquinone 10 in a biological specimen. |
| C189529 | Ubiquitin C-Terminal Hydrolase L1 | Ubiquitin C-Terminal Hydrolase L1; Ubiquitin Carboxy-Terminal Hydrolase L1; UCH-L1 | A measurement of the ubiquitin C-terminal hydrolase L1 in a biological specimen. |
| C147443 | Ubiquitin Protein | Ubiquitin Protein | A measurement of the total ubiquitin protein in a biological specimen. |
| C163461 | Ubiquitin-Like Protein ISG15 | ISG15 Ubiquitin-Like Modifier; Ubiquitin-Like Protein ISG15 | A measurement of the ubiquitin-like protein ISG15 in a biological specimen. |
| C74776 | Unclassified Casts | Unclassified Casts | A measurement of the unclassifiable casts present in a biological specimen. |
| C74757 | Unclassified Crystals | Unclassified Crystals | A measurement of the unclassifiable crystals present in a biological specimen. |
| C74719 | Unsaturated Iron Binding Capacity | Unsaturated Iron Binding Capacity | A measurement of the binding capacity of unsaturated iron in a biological specimen. |
| C112241 | Unspecified Cells | Unspecified Cells | A measurement of the cells not otherwise identified or specified in a biological specimen. |
| C161364 | Unspecified Cells/Leukocytes | Unspecified Cells/Leukocytes | A relative measurement (ratio or percentage) of the cells not otherwise identified or specified to leukocytes in a biological specimen. |
| C114225 | Unspecified Cells/Total Cells | Unspecified Cells/Total Cells | A relative measurement (ratio or percentage) of the cells not otherwise identified or specified to total cells in a biological specimen. |
| C184565 | UR-144 | UR-144; UR144 | A measurement of the synthetic cannabinoid UR-144 in a biological specimen. |
| C163498 | Urate Excretion Rate | Urate Excretion Rate | A measurement of the amount of urate being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C64814 | Urate | Urate; Uric Acid | A measurement of the urate in a biological specimen. |
| C117866 | Urate/Creatinine | Urate/Creatinine | A relative measurement (ratio or percentage) of the urate to creatinine in a biological specimen. |
| C163499 | Urea Nitrogen Excretion Rate | Urea Nitrogen Excretion Rate | A measurement of the amount of urea nitrogen being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C125949 | Urea Nitrogen | Urea Nitrogen | A measurement of the urea nitrogen in a biological specimen. |
| C125950 | Urea Nitrogen/Creatinine | Urea Nitrogen/Creatinine | A relative measurement (ratio or percentage) of the urea nitrogen to creatinine in a biological specimen. |
| C64815 | Urea | Urea | A measurement of the urea in a biological specimen. |
| C96645 | Urea/Creatinine | Urea/Creatinine | A relative measurement (ratio or percentage) of the urea to creatinine in a biological specimen. |
| C74684 | Uric Acid Crystals | Uric Acid Crystals | A measurement of the uric acid crystals (including acid urate and urate crystals) present in a biological specimen. |
| C102282 | Urine Conductivity | Urine Conductivity | A measurement of the urine conductivity which is a non-linear function of the electrolyte concentration in the urine. |
| C64816 | Urobilinogen | Urobilinogen | A measurement of the urobilinogen in a biological specimen. |
| C181447 | Urokinase Plasminogen Activator | uPA; Urokinase Plasminogen Activator | A measurement of the urokinase plasminogen activator in a biological specimen. |
| C163500 | Urothelial Cells | Urothelial Cells | A measurement of urothelial cells in a biological specimen. |
| C176238 | Ursodeoxycholate Compounds | Ursodeoxycholate Compounds; Ursodeoxycholic Acid Compounds | A measurement of the ursodeoxycholic acid, glycoursodeoxycholic acid, tauroursodeoxycholic acid, and epimerized ursodeoxycholic acid in a biological specimen. |
| C176298 | Ursodeoxycholate | Ursodeoxycholate; Ursodeoxycholic Acid; Ursodiol | A measurement of the ursodeoxycholate in a biological specimen. |
| C111329 | Vacuolated Lymphocytes | Vacuolated Lymphocytes | A measurement of the vacuolated lymphocytes in a biological specimen. |
| C127627 | Vacuolated Lymphocytes/Leukocytes | Vacuolated Lymphocytes/Leukocytes | A relative measurement (ratio or percentage) of the vacuolated lymphocytes to leukocytes in a biological specimen. |
| C74628 | Vacuolated Neutrophils | Vacuolated Neutrophils | A measurement of the neutrophils containing small vacuoles in a biological specimen. |
| C184607 | Valerylfentanyl | Valeryl Fentanyl; Valerylfentanyl | A measurement of the valerylfentanyl in a biological specimen. |
| C122160 | Valine | Valine | A measurement of the valine in a biological specimen. |
| C181410 | Valproate | Valproate; Valproic Acid | A measurement of the valproate in a biological specimen. |
| C163503 | Vanillyl Mandelic Acid Excretion Rate | Vanillyl Mandelic Acid Excretion Rate | A measurement of the amount of vanillyl mandelic acid being excreted in a biological specimen over a defined amount of time (e.g. one hour). |
| C74875 | Vanillyl Mandelic Acid | Vanillyl Mandelic Acid; Vanillylmandelate; Vanilmandelic Acid | A measurement of the vanillyl mandelic acid metabolite in a biological specimen. |
| C156527 | Vasc Endothelial Growth Factor Rec 2 | Vasc Endothelial Growth Factor Rec 2; Vascular Endothelial Growth Factor Receptor 2 | A measurement of the vascular endothelial growth factor receptor 2 in a biological specimen. |
| C82042 | Vascular Cell Adhesion Molecule 1 | Vascular Cell Adhesion Molecule 1 | A measurement of the vascular cell adhesion molecule 1 in a biological specimen. |
| C132389 | Vascular Endothelial Growth Factor A | Vascular Endothelial Growth Factor A | A measurement of the vascular endothelial growth factor A in a biological specimen. |
| C163501 | Vascular Endothelial Growth Factor C | Vascular Endothelial Growth Factor C | A measurement of the vascular endothelial growth factor C in a biological specimen. |
| C172496 | Vascular Endothelial Growth Factor D | FIGF; Vascular Endothelial Growth Factor D | A measurement of the vascular endothelial growth factor D in a biological specimen. |
| C92514 | Vascular Endothelial Growth Factor | Vascular Endothelial Growth Factor | A measurement of the vascular endothelial growth factor in a biological specimen. |
| C163502 | Vasoactive Intestinal Polypeptide | Vasoactive Intestinal Polypeptide; VIP | A measurement of vasoactive intestinal polypeptide in a biological specimen. |
| C147444 | Venlafaxine | Venlafaxine | A measurement of the venlafaxine present in a biological specimen. |
| C130166 | Viable Cells | Viable Cells | A measurement of the viable cells in a biological specimen. |
| C187829 | Vilazodone | Vilazodone | A measurement of the vilazodone in a biological specimen. |
| C184606 | Vinbarbital | Vinbarbital | A measurement of the vinbarbital in a biological specimen. |
| C75912 | Viscosity | Visc; Viscosity | The resistance of a liquid to sheer forces and flow. (NCI) |
| C74895 | Vitamin A | Retinol; Vitamin A | A measurement of the Vitamin A in a biological specimen. |
| C64817 | Vitamin B12 | Cobalamin; Vitamin B12 | A measurement of the Vitamin B12 in a biological specimen. |
| C74897 | Vitamin B17 | Amygdalin; Vitamin B17 | A measurement of the Vitamin B17 in a biological specimen. |
| C74900 | Vitamin B5 | Pantothenic Acid; Vitamin B5 | A measurement of the Vitamin B5 in a biological specimen. |
| C74901 | Vitamin B6 | Pyridoxine; Vitamin B6 | A measurement of the Vitamin B6 in a biological specimen. |
| C74902 | Vitamin B7 | Biotin; Vitamin B7 | A measurement of the Vitamin B7 in a biological specimen. |
| C74676 | Vitamin B9 | Folate; Folic Acid; Vitamin B9 | A measurement of the folic acid in a biological specimen. |
| C74903 | Vitamin C | Ascorbate; Ascorbic Acid; Vitamin C | A measurement of the Vitamin C in a biological specimen. |
| C172506 | Vitamin D Binding Protein | DBP; GC Vitamin D Binding Protein; VDBP; Vitamin D Binding Protein | A measurement of the vitamin D binding protein in a biological specimen. |
| C179751 | Vitamin D2 + Vitamin D3 | Calciferol + Cholecalciferol; Vitamin D2 + Vitamin D3 | A measurement of the vitamin D2 and vitamin D3 in a biological specimen. |
| C147445 | Vitamin D2 D3 25-OH | Vitamin D + Metabolites; Vitamin D2 + Vitamin D3 + 25-Hydroxy Vitamin D2 + 25-Hydroxy Vitamin D3; Vitamin D2 D3 25-OH | A measurement of the vitamin D2, vitamin D3 and their metabolites in a biological specimen. |
| C74904 | Vitamin D2 | Calciferol; Ergocalciferol; Viosterol; Vitamin D2 | A measurement of the Vitamin D2 in a biological specimen. |
| C74905 | Vitamin D3 | Calciol; Cholecalciferol; Colecalciferol; Vitamin D; Vitamin D3 | A measurement of the Vitamin D3 in a biological specimen. |
| C74906 | Vitamin E | Vitamin E | A measurement of the Vitamin E in a biological specimen. |
| C103448 | Vitamin E/Cholesterol | Vitamin E/Cholesterol | A relative measurement (ratio or percentage) of vitamin E to total cholesterol in a biological specimen. |
| C74907 | Vitamin K | Naphthoquinone; Vitamin K | A measurement of the total Vitamin K in a biological specimen. |
| C103449 | Vitamin K1 | Phylloquinone; Phytomenadione; Vitamin K1 | A measurement of the Vitamin K1 in a biological specimen. |
| C165995 | Vitronectin | V75; Vitronectin; VN; VNT; VTN | A measurement of the vitronectin in a biological specimen. |
| C184517 | VLDL Apolipoprotein B | VLDL Apolipoprotein B | A measurement of the apolipoprotein B in the very low density lipoprotein fraction of a biological specimen. |
| C120667 | VLDL Cholesterol Subtype 1 | VLDL Cholesterol Subtype 1 | A measurement of the very low density lipoprotein cholesterol subtype 1 in a biological specimen. |
| C120668 | VLDL Cholesterol Subtype 2 | VLDL Cholesterol Subtype 2 | A measurement of the very low density lipoprotein cholesterol subtype 2 in a biological specimen. |
| C120669 | VLDL Cholesterol Subtype 3 | VLDL Cholesterol Subtype 3 | A measurement of the very low density lipoprotein cholesterol subtype 3 in a biological specimen. |
| C105589 | VLDL Cholesterol | VLDL Cholesterol | A measurement of the very low density lipoprotein cholesterol in a biological specimen. |
| C103450 | VLDL Particle Size | VLDL Particle Size | A measurement of the average particle size of very-low-density lipoprotein in a biological specimen. |
| C174301 | VLDL Trig + Chylomicron Trig | VLDL Trig + Chylomicron Trig; VLDL Triglyceride + Chylomicron Triglyceride | A measurement of the very low density lipoprotein triglyceride and chylomicron triglyceride in a biological specimen. |
| C174303 | VLDL Triglyceride | VLDL Triglyceride | A measurement of the very low density lipoprotein triglyceride in a biological specimen. |
| C74720 | Volume | Volume | A measurement of the volume of a biological specimen. |
| C147447 | von Will Factor Act Actual/Control | von Will Factor Act Actual/Control; von Willebrand Factor Activity Actual/Normal; von Willebrand Factor Activity Actual/von Willebrand Factor Activity Control | A relative measurement (ratio or percentage) of the biological activity of the von Willebrand factor dependent coagulation in a subject's specimen when compared to the same activity in a control specimen. |
| C170597 | von Will Factor Actual/Control | von Will Factor Actual/Control; von Willebrand Factor Actual/Control; von Willebrand Factor Actual/Normal; von Willebrand Factor Actual/von Willebrand Factor Control | A relative measurement (ratio or percentage) of the von Willebrand factor in a subject's specimen when compared to a control specimen. |
| C122117 | von Willebrand Factor Activity | von Willebrand Factor Activity | A measurement of the biological activity of von Willebrand coagulation factor in a biological specimen. |
| C147336 | von Willebrand Factor Multimers | von Willebrand Factor Multimers | A measurement of the von Willebrand Factor multimers (an aggregate of multiple von Willebrand factor antigens that are held together with non-covalent bonds) in a biological specimen. |
| C98799 | von Willebrand Factor | von Willebrand Factor; von Willebrand Factor Antigen | A measurement of the von Willebrand coagulation factor in a biological specimen. |
| C187832 | Vortioxetine | Vortioxetine | A measurement of the vortioxetine in a biological specimen. |
| C177961 | Walnut Antigen IgE Antibody | Juglans Species Nut Antigen IgE Antibody; Walnut Antigen IgE Antibody | A measurement of the walnut antigen IgE antibody in a biological specimen. |
| C74777 | Waxy Casts | Waxy Casts | A measurement of the waxy casts present in a biological specimen. |
| C74778 | WBC Casts | WBC Casts | A measurement of the white blood cell casts present in a biological specimen. |
| C127637 | WD Repeat-Containing Protein 26 | CDW2; Macrophage Inflammatory Protein-2; MIP2; WD Repeat-Containing Protein 26 | A measurement of the WD repeat-containing protein 26 in a biological specimen. |
| C130108 | Weed Mix Pollen Antigen IgA Antibody | Weed Mix Pollen Antigen IgA Antibody | A measurement of the weed mix pollen antigen IgA antibody in a biological specimen. |
| C130106 | Weed Mix Pollen Antigen IgE Antibody | Weed Mix Pollen Antigen IgE Antibody | A measurement of the weed mix pollen antigen IgE antibody in a biological specimen. |
| C130107 | Weed Mix Pollen Antigen IgG Antibody | Weed Mix Pollen Antigen IgG Antibody | A measurement of the weed mix pollen antigen IgG antibody in a biological specimen. |
| C165925 | Weed Mix Pollen IgE AB RAST Score | Weed Mix Pollen IgE AB RAST Score | A classification of the amount of weed mix pollen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165906 | Weed Mix Pollen IgG AB RAST Score | Weed Mix Pollen IgG AB RAST Score | A classification of the amount of weed mix pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130093 | Western Ragweed Pollen IgA | Western Ragweed Pollen IgA | A measurement of the Ambrosia psilostachya pollen antigen IgA antibody in a biological specimen. |
| C165891 | Western Ragweed Pollen IgE AB RAST Score | Western Ragweed Pollen IgE AB RAST Score | A classification of the amount of Ambrosia psilostachya pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130092 | Western Ragweed Pollen IgE | Western Ragweed Pollen IgE | A measurement of the Ambrosia psilostachya pollen antigen IgE antibody in a biological specimen. |
| C165903 | Western Ragweed Pollen IgG AB RAST Score | Western Ragweed Pollen IgG AB RAST Score | A classification of the amount of Ambrosia psilostachya pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C130094 | Western Ragweed Pollen IgG | Western Ragweed Pollen IgG | A measurement of the Ambrosia psilostachya pollen antigen IgG antibody in a biological specimen. |
| C130095 | Western Ragweed Pollen IgG4 | Western Ragweed Pollen IgG4 | A measurement of the Ambrosia psilostachya pollen antigen IgG4 antibody in a biological specimen. |
| C165882 | White Elm Pollen IgE AB RAST Score | White Elm Pollen IgE AB RAST Score | A classification of the amount of Ulmus americana pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165881 | White Elm Pollen IgE Antibody | White Elm Pollen IgE Antibody | A measurement of the Ulmus americana pollen antigen IgE antibody in a biological specimen. |
| C165920 | White Elm Pollen IgG AB RAST Score | White Elm Pollen IgG AB RAST Score | A classification of the amount of Ulmus americana pollen IgG antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C147283 | White Elm Pollen IgG Antibody | White Elm Pollen IgG Antibody | A measurement of the Ulmus americana pollen antigen IgG antibody in a biological specimen. |
| C165886 | White Oak Pollen IgE AB RAST Score | White Oak Pollen IgE AB RAST Score | A classification of the amount of Quercus alba pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C147282 | White Oak Pollen IgE Antibody | White Oak Pollen IgE Antibody | A measurement of the Quercus alba pollen antigen IgE antibody in a biological specimen. |
| C176296 | Whole Blood Equivalent Glucose | Whole Blood Equivalent Glucose | A measurement of the whole blood equivalent glucose in a biological specimen. |
| C165893 | Wild Rye Pollen IgE AB RAST Score | Wild Rye Pollen IgE AB RAST Score | A classification of the amount of Elymus tricoides pollen antigen IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C165892 | Wild Rye Pollen IgE Antibody | Wild Rye Pollen IgE Antibody | A measurement of the Elymus tricoides pollen antigen IgE antibody in a biological specimen. |
| C147449 | Xanthochromia | Xanthochromia | A measurement of the yellowish appearance of a biological specimen due to the presence of bilirubin produced by the degradation of heme from erythrocytes that have entered the biological specimen. |
| C186099 | Xylose | Xylose | A measurement of the xylose in a biological specimen. |
| C186098 | Xylose/Xylose Dose | Xylose/Xylose Dose | A relative measurement (percentage) of the xylose in a biological specimen to an administered dose of xylose. |
| C106504 | Yeast Budding | Budding Yeast; Yeast Budding | A measurement of the budding yeast present in a biological specimen. |
| C74664 | Yeast Cells | Yeast Cells | A measurement of the yeast cells present in a biological specimen. |
| C92239 | Yeast Hyphae | Yeast Hyphae | A measurement of the yeast hyphae present in a biological specimen. |
| C142294 | YKL-40 Protein | Chitinase-3-Like Protein 1; YKL-40 Protein | A measurement of the YKL-40 protein in a biological specimen. |
| C184636 | Zaleplon | Zaleplon | A measurement of the zaleplon in a biological specimen. |
| C147279 | Zea mays Antigen IgE Antibody | Corn Antigen IgE Antibody; Zea mays Antigen IgE Antibody | A measurement of the Zea mays antigen IgE antibody in a biological specimen. |
| C165937 | Zea mays IgE AB RAST Score | Zea mays IgE AB RAST Score | A classification of the amount of Zea mays IgE antibody, using the RAST (radioallergosorbent test) scoring system, in a biological specimen. |
| C147452 | Zinc Protoporphyrin | Zinc Protoporphyrin | A measurement of the zinc protoporphyrin (zinc bound protoporphyrin) in a biological specimen. |
| C80210 | Zinc | Zinc | A measurement of the zinc in a biological specimen. |
| C177986 | Ziprasidone | Ziprasidone | A measurement of the ziprasidone in a biological specimen. |
| C184637 | Zolpidem | Zolpidem | A measurement of the zolpidem in a biological specimen. |
| C184638 | Zopiclone | Zopiclone | A measurement of the zopiclone in a biological specimen. |

## Source: `terminology/core/lb_part4.md`

# Laboratory Codelists (Part 4)

> Codelists in this file: 2

## Laboratory Test Standard Character Result (C102580)

Extensible: Yes

| Code | CDISC Submission Value | CDISC Synonym(s) | CDISC Definition |
|------|----------------------|-------------------|------------------|
| C14157 | BORDERLINE |  | Straddling the dividing line between two categories. |
| C48658 | INDETERMINATE | Inconclusive | Cannot distinguish between two or more possible values in the current context. (NCI) |
| C50913 | INVALID | INV | Not valid data. |
| C38757 | NEGATIVE |  | A finding of normality following an examination or investigation looking for the presence of a microorganism, disease, or condition. |
| C38758 | POSITIVE |  | An observation confirming something, such as the presence of a disease, condition, or microorganism. |
| C80218 | TRACE |  | A barely detectable amount. |

## Test Method Sensitivity (C179589)

Extensible: Yes

| Code | CDISC Submission Value | CDISC Synonym(s) | CDISC Definition |
|------|----------------------|-------------------|------------------|
| C179820 | HIGH SENSITIVITY |  | Any test methodology that is able to detect or quantify a finding at a high sensitivity level, as compared to the sensitivities of other concurrently available methods. |
| C179821 | LOW SENSITIVITY |  | Any test methodology that is able to detect or quantify a finding at a low sensitivity level, as compared to the sensitivities of other concurrently available methods. |
| C179822 | ULTRA-HIGH SENSITIVITY |  | Any test methodology that is able to detect or quantify a finding at an ultra-high sensitivity level, as compared to the sensitivities of other concurrently available methods. |
