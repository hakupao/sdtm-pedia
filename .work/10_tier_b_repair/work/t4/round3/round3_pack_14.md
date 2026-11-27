# T4.1 第三轮补检包 14 — R3_XTYPO (6 条; 编号 T310-T315)

> 由 `scripts/t4/t4_round3_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 T).

### T310. `ig34_p0083_a020` — r3:R3_XTYPO

- PDF 页 83 · 原子类型 TABLE_HEADER · 所在节 `§5.3 [Subject Elements (SE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-SPREL SE T-1`: PDF 写 "dm 表头 BIRTHDTC (p82-84)" → KB 写 "BRTHDTC" (处理: KB 写正确值; 依据: DM spec 与 DM 例均 BRTHDTC; KB `knowledge_base/domains/SE/examples.md:44`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row | USUBJID | SUBJID | RFSTDTC | RFENDTC | SITEID | INVNAM | BIRTHDTC | AGE | AGEU | SEX | RACE | ETHNIC | ARMCD | ARM | ACTARMCD | ACTARM | ARMNRS | ACTARMUD | COUNTRY
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0083.txt` 第 1-1 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| Row USUBJID SUBJID RFSTDTC RFENDTC SITEID INVNAM BIRTHDTC AGE AGEU SEX RACE ETHNIC                             ARMCD ARM     ACTARMCD ACTARM ARMNRS ACTARMUD COUNTRY
  2| 3   791     003    2006-06- 2006-06- 01   SMITH, 1956-07-17 49 YEARS M WHITE NOT                               IO    IV-     IO       IV-ORAL                USA
~~~~

KB 现文: `knowledge_base/domains/SE/examples.md:44-44` (来源: fuzzy locate (score 0.95)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  44| | Row | USUBJID | SUBJID | RFSTDTC | RFENDTC | SITEID | INVNAM | BRTHDTC | AGE | AGEU | SEX | RACE | ETHNIC | ARMCD | ARM | ACTARMCD | ACTARM | ARMNRS | ACTARMUD | COUNTRY |
~~~~

### T311. `ig34_p0304_a026` — r3:R3_XTYPO

- PDF 页 304 · 原子类型 TABLE_ROW · 所在节 `§6.3.7.5 Ophthalmic Examinations (OE)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-OE T-2`: PDF 写 "OECAT OCCULAR COMFORT ×4" → KB 写 "OCULAR COMFORT" (处理: KB 写正确值; 依据: suppoe IDVARVAL=OCULAR COMFORT; KB `knowledge_base/domains/OE/examples.md:142`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | XYZ | OE | XYZ-100-0001 | OD | 1 | EYECOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | | OCULAR COMFORT | | EYE | RIGHT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT | 2011-02-11T09:00 | 1 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0304.txt` 第 26-31 行 (自动定位, 词覆盖 0.957; 版式以原 PDF 为准):

~~~~
 25| Row 3:          Represents the subject's assessment of ocular comfort in the left eye, upon instillation of a lubricant eye drop for dry eye.
 26| Row 4:          Represents the subject's assessment of ocular comfort in the left eye, 1 minute post-instillation of a lubricant eye drop for dry eye.
 27| oe.xpt
 28| Row STUDYID DOMAIN USUBJID              FOCID OESEQ OETESTCD OETEST                  OECAT         OEORRES OESTRESC OESTRESN OELOC OELAT OEMETHOD              OEEVAL       VISITNUM VISIT   OEDTC       OETPT            OETPTNUM
 29| 1   XYZ     OE     XYZ-100-             OD    1     EYDCOMGR Eye Drop                OCCULAR       1       1        1        EYE   RIGHT VISUAL                STUDY        1        VISIT   2011-02-    UPON             1
 30|                    0001                                      Comfort                 COMFORT                                             ANALOG                SUBJECT               1       11T09:00    INSTILLATION
 31|                                                              Grade                                                                       SCALE
 32| 2         XYZ       OE       XYZ-100-   OD    2     EYDCOMGR Eye Drop                OCCULAR       10      10       10       EYE   RIGHT VISUAL                STUDY        1        VISIT   2011-02-    1 MINUTE POST-   2
~~~~

KB 现文: `knowledge_base/domains/OE/examples.md:142-142` (来源: fuzzy locate (score 0.957)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 142| | 1 | XYZ | OE | XYZ-100-0001 | OD | 1 | EYDCOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 1 | 1 | 1 | EYE | RIGHT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT 1 | 2011-02-11T09:00 | UPON INSTILLATION | 1 |
~~~~

### T312. `ig34_p0304_a027` — r3:R3_XTYPO

- PDF 页 304 · 原子类型 TABLE_ROW · 所在节 `§6.3.7.5 Ophthalmic Examinations (OE)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-OE T-2`: PDF 写 "OECAT OCCULAR COMFORT ×4" → KB 写 "OCULAR COMFORT" (处理: KB 写正确值; 依据: suppoe IDVARVAL=OCULAR COMFORT; KB `knowledge_base/domains/OE/examples.md:142`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | XYZ | OE | XYZ-100-0001 | OD | 2 | EYECOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 10 | 10 | 10 | EYE | RIGHT | SCALE | STUDY SUBJECT | 1 | VISIT | 2011-02-11T09:01 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0304.txt` 第 26-33 行 (自动定位, 词覆盖 0.957; 版式以原 PDF 为准):

~~~~
 25| Row 3:          Represents the subject's assessment of ocular comfort in the left eye, upon instillation of a lubricant eye drop for dry eye.
 26| Row 4:          Represents the subject's assessment of ocular comfort in the left eye, 1 minute post-instillation of a lubricant eye drop for dry eye.
 27| oe.xpt
 28| Row STUDYID DOMAIN USUBJID              FOCID OESEQ OETESTCD OETEST                  OECAT         OEORRES OESTRESC OESTRESN OELOC OELAT OEMETHOD              OEEVAL       VISITNUM VISIT   OEDTC       OETPT            OETPTNUM
 29| 1   XYZ     OE     XYZ-100-             OD    1     EYDCOMGR Eye Drop                OCCULAR       1       1        1        EYE   RIGHT VISUAL                STUDY        1        VISIT   2011-02-    UPON             1
 30|                    0001                                      Comfort                 COMFORT                                             ANALOG                SUBJECT               1       11T09:00    INSTILLATION
 31|                                                              Grade                                                                       SCALE
 32| 2         XYZ       OE       XYZ-100-   OD    2     EYDCOMGR Eye Drop                OCCULAR       10      10       10       EYE   RIGHT VISUAL                STUDY        1        VISIT   2011-02-    1 MINUTE POST-   2
 33|                              0001                            Comfort                 COMFORT                                             ANALOG                SUBJECT               1       11T09:01    INSTILLATION
 34|                                                              Grade                                                                       SCALE
~~~~

KB 现文: `knowledge_base/domains/OE/examples.md:143-143` (来源: fuzzy locate (score 0.957)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 143| | 2 | XYZ | OE | XYZ-100-0001 | OD | 2 | EYDCOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 10 | 10 | 10 | EYE | RIGHT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT 1 | 2011-02-11T09:01 | 1 MINUTE POST-INSTILLATION | 2 |
~~~~

### T313. `ig34_p0304_a028` — r3:R3_XTYPO

- PDF 页 304 · 原子类型 TABLE_ROW · 所在节 `§6.3.7.5 Ophthalmic Examinations (OE)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-OE T-2`: PDF 写 "OECAT OCCULAR COMFORT ×4" → KB 写 "OCULAR COMFORT" (处理: KB 写正确值; 依据: suppoe IDVARVAL=OCULAR COMFORT; KB `knowledge_base/domains/OE/examples.md:142`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | XYZ | OE | XYZ-100-0001 | OS | 1 | EYECOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | | OCULAR COMFORT | | EYE | LEFT | SCALE | STUDY SUBJECT | 1 | VISIT | 2011-05-01T09:00 | 1 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0304.txt` 第 26-36 行 (自动定位, 词覆盖 0.955; 版式以原 PDF 为准):

~~~~
 25| Row 3:          Represents the subject's assessment of ocular comfort in the left eye, upon instillation of a lubricant eye drop for dry eye.
 26| Row 4:          Represents the subject's assessment of ocular comfort in the left eye, 1 minute post-instillation of a lubricant eye drop for dry eye.
 27| oe.xpt
 28| Row STUDYID DOMAIN USUBJID              FOCID OESEQ OETESTCD OETEST                  OECAT         OEORRES OESTRESC OESTRESN OELOC OELAT OEMETHOD              OEEVAL       VISITNUM VISIT   OEDTC       OETPT            OETPTNUM
 29| 1   XYZ     OE     XYZ-100-             OD    1     EYDCOMGR Eye Drop                OCCULAR       1       1        1        EYE   RIGHT VISUAL                STUDY        1        VISIT   2011-02-    UPON             1
 30|                    0001                                      Comfort                 COMFORT                                             ANALOG                SUBJECT               1       11T09:00    INSTILLATION
 31|                                                              Grade                                                                       SCALE
 32| 2         XYZ       OE       XYZ-100-   OD    2     EYDCOMGR Eye Drop                OCCULAR       10      10       10       EYE   RIGHT VISUAL                STUDY        1        VISIT   2011-02-    1 MINUTE POST-   2
 33|                              0001                            Comfort                 COMFORT                                             ANALOG                SUBJECT               1       11T09:01    INSTILLATION
 34|                                                              Grade                                                                       SCALE
 35| 3         XYZ       OE       XYZ-100-   OS    1     EYDCOMGR Eye Drop                OCCULAR       1       1        1        EYE   LEFT  VISUAL                STUDY        1        VISIT   2011-05-    UPON             1
 36|                              0001                            Comfort                 COMFORT                                             ANALOG                SUBJECT               1       01T09:00    INSTILLATION
 37|                                                              Grade                                                                       SCALE
~~~~

KB 现文: `knowledge_base/domains/OE/examples.md:144-144` (来源: fuzzy locate (score 0.955)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 144| | 3 | XYZ | OE | XYZ-100-0001 | OS | 1 | EYDCOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 1 | 1 | 1 | EYE | LEFT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT 1 | 2011-05-01T09:00 | UPON INSTILLATION | 1 |
~~~~

### T314. `ig34_p0304_a029` — r3:R3_XTYPO

- PDF 页 304 · 原子类型 TABLE_ROW · 所在节 `§6.3.7.5 Ophthalmic Examinations (OE)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-OE T-2`: PDF 写 "OECAT OCCULAR COMFORT ×4" → KB 写 "OCULAR COMFORT" (处理: KB 写正确值; 依据: suppoe IDVARVAL=OCULAR COMFORT; KB `knowledge_base/domains/OE/examples.md:142`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | XYZ | OE | XYZ-100-0001 | OS | 2 | EYECOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 10 | 10 | 10 | EYE | LEFT | SCALE | STUDY SUBJECT | 1 | VISIT | 2011-05-01T09:01 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0304.txt` 第 26-36 行 (自动定位, 词覆盖 0.958; 版式以原 PDF 为准):

~~~~
 25| Row 3:          Represents the subject's assessment of ocular comfort in the left eye, upon instillation of a lubricant eye drop for dry eye.
 26| Row 4:          Represents the subject's assessment of ocular comfort in the left eye, 1 minute post-instillation of a lubricant eye drop for dry eye.
 27| oe.xpt
 28| Row STUDYID DOMAIN USUBJID              FOCID OESEQ OETESTCD OETEST                  OECAT         OEORRES OESTRESC OESTRESN OELOC OELAT OEMETHOD              OEEVAL       VISITNUM VISIT   OEDTC       OETPT            OETPTNUM
 29| 1   XYZ     OE     XYZ-100-             OD    1     EYDCOMGR Eye Drop                OCCULAR       1       1        1        EYE   RIGHT VISUAL                STUDY        1        VISIT   2011-02-    UPON             1
 30|                    0001                                      Comfort                 COMFORT                                             ANALOG                SUBJECT               1       11T09:00    INSTILLATION
 31|                                                              Grade                                                                       SCALE
 32| 2         XYZ       OE       XYZ-100-   OD    2     EYDCOMGR Eye Drop                OCCULAR       10      10       10       EYE   RIGHT VISUAL                STUDY        1        VISIT   2011-02-    1 MINUTE POST-   2
 33|                              0001                            Comfort                 COMFORT                                             ANALOG                SUBJECT               1       11T09:01    INSTILLATION
 34|                                                              Grade                                                                       SCALE
 35| 3         XYZ       OE       XYZ-100-   OS    1     EYDCOMGR Eye Drop                OCCULAR       1       1        1        EYE   LEFT  VISUAL                STUDY        1        VISIT   2011-05-    UPON             1
 36|                              0001                            Comfort                 COMFORT                                             ANALOG                SUBJECT               1       01T09:00    INSTILLATION
 37|                                                              Grade                                                                       SCALE
~~~~

KB 现文: `knowledge_base/domains/OE/examples.md:145-145` (来源: fuzzy locate (score 0.958)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 145| | 4 | XYZ | OE | XYZ-100-0001 | OS | 2 | EYDCOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 10 | 10 | 10 | EYE | LEFT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT 1 | 2011-05-01T09:01 | 1 MINUTE POST-INSTILLATION | 2 |
~~~~

### T315. `ig34_p0316_a023` — r3:R3_XTYPO

- PDF 页 316 · 原子类型 TABLE_ROW · 所在节 `§6.3.8 Physical Examination (PE)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-FND PE T-1`: PDF 写 "PELAT Notes laterallity" → KB 写 "laterality" (处理: KB 写正确值; 依据: 同行 Label Laterality; OE/UR 同变量; KB `knowledge_base/domains/PE/spec.md:174`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| PELAT | Laterality | Char | (LAT) | Variable Qualifier | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0316.txt` 第 46-47 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 45|               Finding
 46| PELAT         Laterality          Char (LAT)              Variable     Qualifier for anatomical location or specimen further detailing laterallity. Examples: "RIGHT", "LEFT",                Perm
 47|                                                           Qualifier    "BILATERAL".
 48| PEMETHOD      Method of Test or   Char (METHOD)           Record       Method of the test or examination. Examples: "PALPATION", "PERCUSSION".                                                Perm
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

