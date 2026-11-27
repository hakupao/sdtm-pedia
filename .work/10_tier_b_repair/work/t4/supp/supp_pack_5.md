# T4.1 补检包 5/8 — TRIAGE_ATOM_ERR (24 条, 全检, 不抽样)

> 由 `scripts/t4/t4_supp_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续.

### 109. `ig34_p0169_a0029` — supp:TRIAGE_ATOM_ERR

- PDF 页 169 · 原子类型 TABLE_ROW · 所在节 `§6.2.5 Healthcare Encounters (HO)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:3946 (lane A pack_007; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 10 | ABC | HO | ABC123105 | 2 | HOSPITAL | | TREATMENT | 2011-10-11 | 2011-10-16 | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0170.txt` 第 13-13 行 (自动定位, 词覆盖 0.9; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 12| 9        ABC        HO         ABC123105     1          CARDIAC CATHETERIZATION LABORATORY                TREATMENT      2011-10-11    2011-10-11
 13| 10       ABC        HO         ABC123105     2          HOSPITAL                                          TREATMENT      2011-10-11    2011-10-15
 14| 11       ABC        HO         ABC123106     1          CARDIAC CATHETERIZATION LABORATORY                FOLLOW-UP      2011-11-07    2011-11-07
~~~~

KB 现文: `knowledge_base/domains/HO/examples.md:30-30` (来源: near triage kb_loc knowledge_base/domains/HO/examples.md:30 (score 0.9)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  30| | 10 | ABC | HO | ABC123105 | 2 | HOSPITAL | TREATMENT | 2011-10-11 | 2011-10-15 | |
~~~~

### 110. `ig34_p0170_a0004` — supp:TRIAGE_ATOM_ERR

- PDF 页 170 · 原子类型 TABLE_HEADER · 所在节 `§6.2.5 Healthcare Encounters (HO)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:3998 (lane A pack_007; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | USUBJID | HOSEQ | HOTERM | | HOCAT | HOSTDTC | HOENDTC | HOSTRTPT | HOENTPT |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0170.txt` 第 38-38 行 (自动定位, 词覆盖 0.909; 版式以原 PDF 为准):

~~~~
 37| ho.xpt
 38| Row      STUDYID   DOMAIN    USUBJID     HOSEQ   HOTERM                               HOCAT                     HOSTDTC            HOENDTC            HOENRTPT   HOENTPT
 39| 1        ABC       HO        ABC123101   1       HOSPITAL                             INITIAL HOSPITALIZATION   2011-06-08         2011-06-12
~~~~

KB 现文: `knowledge_base/domains/HO/examples.md:61-61` (来源: near triage kb_loc knowledge_base/domains/HO/examples.md:61 (score 0.909)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  61| | Row | STUDYID | DOMAIN | USUBJID | HOSEQ | HOTERM | HOCAT | HOSTDTC | HOENDTC | HOENRTPT | HOENTPT |
~~~~

### 111. `ig34_p0170_a0006` — supp:TRIAGE_ATOM_ERR

- PDF 页 170 · 原子类型 TABLE_ROW · 所在节 `§6.2.5 Healthcare Encounters (HO)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:4011 (lane A pack_007; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC | HO | ABC123101 | 2 | INTENSIVE CARE UNIT | | INITIAL HOSPITALIZATION | 2011-06-10 T 10:00 | 2011-06-10 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0170.txt` 第 40-42 行 (自动定位, 词覆盖 0.786; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 39| 1        ABC       HO        ABC123101   1       HOSPITAL                             INITIAL HOSPITALIZATION   2011-06-08         2011-06-12
 40| 2        ABC       HO        ABC123101   2       ICU                                  INITIAL HOSPITALIZATION   2011-06-08T11:00   2011-06-09T14:30
 41| 3        ABC       HO        ABC123101   3       REHABILITATION FACILITY              FOLLOW-UP CARE            2011-06-12         2011-06-22
 42| 4        ABC       HO        ABC123101   4       CARDIOLOGY UNIT                      FOLLOW-UP CARE            2011-06-25         2011-06-25
 43| 5        ABC       HO        ABC123101   5       OUTPATIENT PHYSICAL THERAPY          FOLLOW-UP CARE            2011-06-27         2011-06-27
~~~~

KB 现文: `knowledge_base/domains/HO/examples.md:64-66` (来源: near triage kb_loc knowledge_base/domains/HO/examples.md:64 (score 0.786)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  64| | 2 | ABC | HO | ABC123101 | 2 | ICU | INITIAL HOSPITALIZATION | 2011-06-08T11:00 | 2011-06-09T14:30 | | |
  65| | 3 | ABC | HO | ABC123101 | 3 | REHABILITATION FACILITY | FOLLOW-UP CARE | 2011-06-12 | 2011-06-22 | | |
  66| | 4 | ABC | HO | ABC123101 | 4 | CARDIOLOGY UNIT | FOLLOW-UP CARE | 2011-06-25 | 2011-06-25 | | |
~~~~

### 112. `ig34_p0192_a006` — supp:TRIAGE_ATOM_ERR

- PDF 页 192 · 原子类型 TABLE_ROW · 所在节 `§6.3.3 ECG Test Results (EG)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 MISPLACED) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:11482 (lane C pack_020; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | STUDY01 | EG | 2324-P0001 | 4 | 2 | RRSM | RR Interval, Single Beat Measurement | INTERVAL | SUPINE | 679 | msec | 679 | 679 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T14:32:13.3 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0192.txt` 第 8-10 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7| 3   STUDY01 EG     2324-           3     2        PRSB     PR Interval, Single    INTERVAL SUPINE 176    msec     176      176      msec     12 LEAD    LEAD II         1        SCREENING -7      2014-02-
  8|                    P0001                                   Beat                                                                              STANDARD                                              11T14:32:13.3
  9| 4   STUDY01 EG     2324-           4     2        RRSM     RR Interval, Single    INTERVAL SUPINE 679    msec     679      679      msec     12 LEAD    LEAD II         1        SCREENING -7      2014-02-
 10|                    P0001                                   Measurement                                                                       STANDARD                                              11T14:32:13.3
 11| 5   STUDY01 EG     2324-           5     2        QRSSB    QRS Duration,          INTERVAL SUPINE 95     msec     95       95       msec     12 LEAD    LEAD II         1        SCREENING -7      2014-02-
~~~~

KB 现文: `knowledge_base/domains/EG/examples.md:105-106` (来源: near triage kb_loc knowledge_base/domains/EG/examples.md:106 (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 105| | 3 | STUDY01 | EG | 2324-P0001 | 3 | 2 | PRSB | PR Interval, Single Beat | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T14:32:13.3 |
 106| | 4 | STUDY01 | EG | 2324-P0001 | 4 | 2 | RRSM | RR Interval, Single Measurement | INTERVAL | SUPINE | 679 | msec | 679 | 679 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T14:32:13.3 |
~~~~

### 113. `ig34_p0192_a009` — supp:TRIAGE_ATOM_ERR

- PDF 页 192 · 原子类型 TABLE_ROW · 所在节 `§6.3.3 ECG Test Results (EG)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 MISPLACED) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:11495 (lane C pack_020; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 7 | STUDY01 | EG | 2324-P0001 | 7 | 3 | RRSM | RR Interval, Single Beat Measurement | INTERVAL | SUPINE | 661 | msec | 661 | 661 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T15:32:14.2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0192.txt` 第 14-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13| 6   STUDY01 EG     2324-           6     3        PRSB     PR Interval, Single    INTERVAL SUPINE 169    msec     169      169      msec     12 LEAD    LEAD II         1        SCREENING -7      2014-02-
 14|                    P0001                                   Beat                                                                              STANDARD                                              11T15:32:14.2
 15| 7   STUDY01 EG     2324-           7     3        RRSM     RR Interval, Single    INTERVAL SUPINE 661    msec     661      661      msec     12 LEAD    LEAD II         1        SCREENING -7      2014-02-
 16|                    P0001                                   Measurement                                                                       STANDARD                                              11T15:32:14.2
 17| 8   STUDY01 EG     2324-           8     3        QRSSB    QRS Duration,          INTERVAL SUPINE 90     msec     90       90       msec     12 LEAD    LEAD II         1        SCREENING -7      2014-02-
~~~~

KB 现文: `knowledge_base/domains/EG/examples.md:108-109` (来源: near triage kb_loc knowledge_base/domains/EG/examples.md:109 (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 108| | 6 | STUDY01 | EG | 2324-P0001 | 6 | 3 | PRSB | PR Interval, Single Beat | INTERVAL | SUPINE | 169 | msec | 169 | 169 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T15:32:14.2 |
 109| | 7 | STUDY01 | EG | 2324-P0001 | 7 | 3 | RRSM | RR Interval, Single Measurement | INTERVAL | SUPINE | 661 | msec | 661 | 661 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T15:32:14.2 |
~~~~

### 114. `ig34_p0226_a008` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_HEADER · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:8897 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFSRPD | GFREFID | GFSPID | GFTESTCD | GFTEST | GFTSTOTL | GFORRES | GFORRESC | GFSTRESC | GFSTRESU | GFSEMREF | GFCHRCN | GFSYM | GFSTMYTP | GFSEQID | GFXFN | GFNAM | GFSPEC | GFMETHOD | GFANMETH | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 8-8 行 (自动定位, 词覆盖 0.8; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  7| gf.xpt
  8| Row   STUDYID   DOMAIN   USUBJID   SPDEVID     GFSEQ   GFGRPID   GFREFID      GFSPID     GFTESTCD   GFTEST          GFTSTDTL         GFORRES       GFORRESU   GFSTRESC      GFSTRESN      GFSTRESU   GFGENREF     GFCHROM   GFSYM   GFSYMTYP    GFSEQID             GFXFN               GFNAM   GFSPEC   GFMETHOD        GFANMETH       VISITNUM   VISIT   VISITDY   GFDTC   GFDY
  9| 1     ABC-123   GF       123101    ACME        1       1         ABU3908A52   AH749754   TRNSCPTN   Transcription   FRAGMENT         36                       36            36                       hs37d5       7         ACTB    GENE WITH   ENST00000646664.1   AH749754.fastq.gz   ACME    RNA      TARGETED                       1          VISIT   1         2018-   2
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:86-86` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:84 (score 0.8)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  86| | Row | STUDYID | DOMAIN | USUBJID | SPDEVID | GFSEQ | GFGRPID | GFREFID | GFSPID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFORRESU | GFSTRESC | GFSTRESN | GFSTRESU | GFGENREF | GFCHROM | GFSYM | GFSYMTYP | GFSEQID | GFXFN | GFNAM | GFSPEC | GFMETHOD | GFANMETH | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
~~~~

### 115. `ig34_p0226_a009` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:8910 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | ABC-123 | GF | 123101 | 1 | | ABU3908AS2 | AH749754 | TRNSCPTN | Transcription | FRAGMENT COUNT | 36 | | 36 | | 1s37d5 | | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000466554.1 | AH749754.fasta.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | | 2018-09-04 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 9-11 行 (自动定位, 词覆盖 0.871; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  8| Row   STUDYID   DOMAIN   USUBJID   SPDEVID     GFSEQ   GFGRPID   GFREFID      GFSPID     GFTESTCD   GFTEST          GFTSTDTL         GFORRES       GFORRESU   GFSTRESC      GFSTRESN      GFSTRESU   GFGENREF     GFCHROM   GFSYM   GFSYMTYP    GFSEQID             GFXFN               GFNAM   GFSPEC   GFMETHOD        GFANMETH       VISITNUM   VISIT   VISITDY   GFDTC   GFDY
  9| 1     ABC-123   GF       123101    ACME        1       1         ABU3908A52   AH749754   TRNSCPTN   Transcription   FRAGMENT         36                       36            36                       hs37d5       7         ACTB    GENE WITH   ENST00000646664.1   AH749754.fastq.gz   ACME    RNA      TARGETED                       1          VISIT   1         2018-   2
 10|                                    GenePanel                                                                        COUNT                                                                                                           PROTEIN                                                              TRANSCRIPTOME                             1                 09-04
 11|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING
 12| 2     ABC-123   GF       123101    ACME        2       1         ABU3908A52   AH749754   TRNSCPTN   Transcription   NORMALIZED       0.5679        /MBP       0.5679        0.5679        /MBP       hs37d5       7         ACTB    GENE WITH   ENST00000646664.1   AH749754.fastq.gz   ACME    RNA      TARGETED        FRAGMENTS      1          VISIT   1         2018-   2
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:88-88` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:86 (score 0.871)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  88| | 1 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 1 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | FRAGMENT COUNT | 36 | | 36 | 36 | | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
~~~~

### 116. `ig34_p0226_a010` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:8923 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC-123 | GF | 123101 | 2 | | ABU3908AS2 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 0.5679 | -MBP | 0.5679 | 0.5679 | MBP | 1s37d5 | | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000466554.1 | AH749754.fasta.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | FRAGMENTS PER KILOBASE MILLION FORMULA | 1 | VISIT 1 | | 2018-09-04 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 12-15 行 (自动定位, 词覆盖 0.895; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 11|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING
 12| 2     ABC-123   GF       123101    ACME        2       1         ABU3908A52   AH749754   TRNSCPTN   Transcription   NORMALIZED       0.5679        /MBP       0.5679        0.5679        /MBP       hs37d5       7         ACTB    GENE WITH   ENST00000646664.1   AH749754.fastq.gz   ACME    RNA      TARGETED        FRAGMENTS      1          VISIT   1         2018-   2
 13|                                    GenePanel                                                                        LEVEL                                                                                                           PROTEIN                                                              TRANSCRIPTOME   PER KILOBASE              1                 09-04
 14|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      MILLION
 15|                                                                                                                                                                                                                                                                                                                          FORMULA
 16| 3     ABC-123   GF       123101    ACME        3       1         ABU3908A52   AH749754   TRNSCPTN   Transcription   NORMALIZED       1.0523        /10^6      1.0523        1.0523        /10^6      hs37d5       7         ACTB    GENE WITH   ENST00000646664.1   AH749754.fastq.gz   ACME    RNA      TARGETED        COUNTS PER     1          VISIT   1         2018-   2
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:89-89` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:87 (score 0.895)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  89| | 2 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 2 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 0.5679 | /MBP | 0.5679 | 0.5679 | /MBP | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | FRAGMENTS PER KILOBASE MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
~~~~

### 117. `ig34_p0226_a011` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:8936 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | ABC-123 | GF | 123101 | 3 | | ABU3908AS2 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 1.0523 | 71P4 | 1.0523 | 1.0523 | 71P4 | 1s37d5 | | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000466554.1 | AH749754.fasta.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | COUNTS PER MILLION FORMULA | 1 | VISIT 1 | | 2018-09-04 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 16-18 行 (自动定位, 词覆盖 0.865; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 15|                                                                                                                                                                                                                                                                                                                          FORMULA
 16| 3     ABC-123   GF       123101    ACME        3       1         ABU3908A52   AH749754   TRNSCPTN   Transcription   NORMALIZED       1.0523        /10^6      1.0523        1.0523        /10^6      hs37d5       7         ACTB    GENE WITH   ENST00000646664.1   AH749754.fastq.gz   ACME    RNA      TARGETED        COUNTS PER     1          VISIT   1         2018-   2
 17|                                    GenePanel                                                                        LEVEL                                                                                                           PROTEIN                                                              TRANSCRIPTOME   MILLION                   1                 09-04
 18|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      FORMULA
 19| 4     ABC-123   GF       123101    ACME        4       1         ABU3908A52   AH749754   TRNSCPTN   Transcription   NORMALIZED       1.9935        /MBP       1.9935        1.9935        /MBP       hs37d5       7         ACTB    GENE WITH   ENST00000646664.1   AH749754.fastq.gz   ACME    RNA      TARGETED        TRANSCRIPTS    1          VISIT   1         2018-   2
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:90-90` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:88 (score 0.865)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  90| | 3 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 3 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 1.0523 | /10^6 | 1.0523 | 1.0523 | /10^6 | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | COUNTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
~~~~

### 118. `ig34_p0226_a012` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:8949 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | ABC-123 | GF | 123101 | 4 | | ABU3908AS2 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 1.9935 | -MBP | 1.9935 | 1.9935 | MBP | 1s37d5 | | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000466554.1 | AH749754.fasta.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | TRANSCRIPTS PER MILLION FORMULA | 1 | VISIT 1 | | 2018-09-04 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 18-20 行 (自动定位, 词覆盖 0.892; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 17|                                    GenePanel                                                                        LEVEL                                                                                                           PROTEIN                                                              TRANSCRIPTOME   MILLION                   1                 09-04
 18|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      FORMULA
 19| 4     ABC-123   GF       123101    ACME        4       1         ABU3908A52   AH749754   TRNSCPTN   Transcription   NORMALIZED       1.9935        /MBP       1.9935        1.9935        /MBP       hs37d5       7         ACTB    GENE WITH   ENST00000646664.1   AH749754.fastq.gz   ACME    RNA      TARGETED        TRANSCRIPTS    1          VISIT   1         2018-   2
 20|                                    GenePanel                                                                        LEVEL                                                                                                           PROTEIN                                                              TRANSCRIPTOME   PER MILLION               1                 09-04
 21|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      FORMULA
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:91-91` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:89 (score 0.892)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  91| | 4 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 4 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 1.9935 | /MBP | 1.9935 | 1.9935 | /MBP | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | TRANSCRIPTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
~~~~

### 119. `ig34_p0226_a013` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:8962 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 5 | ABC-123 | GF | 123101 | 5 | | ABU3908AS2 | AH749754 | TRNSCPTN | Transcription | PERCENTILE RANK | 0.37 | % | 0.37 | % | 1s37d5 | | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000466554.1 | AH749754.fasta.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | | 2018-09-04 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 21-23 行 (自动定位, 词覆盖 0.879; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 20|                                    GenePanel                                                                        LEVEL                                                                                                           PROTEIN                                                              TRANSCRIPTOME   PER MILLION               1                 09-04
 21|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      FORMULA
 22| 5     ABC-123   GF       123101    ACME        5       1         ABU3908A52   AH749754   TRNSCPTN   Transcription   PERCENTILE       0.37          %          0.37          0.37          %          hs37d5       7         ACTB    GENE WITH   ENST00000646664.1   AH749754.fastq.gz   ACME    RNA      TARGETED                       1          VISIT   1         2018-   2
 23|                                    GenePanel                                                                        RANK                                                                                                            PROTEIN                                                              TRANSCRIPTOME                             1                 09-04
 24|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:92-92` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:90 (score 0.879)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  92| | 5 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 5 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | PERCENTILE RANK | 0.37 | % | 0.37 | 0.37 | % | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
~~~~

### 120. `ig34_p0226_a014` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:8975 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 6 | ABC-123 | GF | 123101 | 6 | | ABU3908AS2 | AH749754 | TRNSCPTN | Transcription | GENETIC TRANSCRIPTION INDICATOR | no | | no | | 1s37d5 | | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000466554.1 | AH749754.fasta.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | | 2018-09-04 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 25-27 行 (自动定位, 词覆盖 0.875; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 24|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING
 25| 6     ABC-123   GF       123101    ACME        6       1         ABU3908A52   AH749754   TRNSCPTN   Transcription   GENETIC          no                       no                                     hs37d5       7         ACTB    GENE WITH   ENST00000646664.1   AH749754.fastq.gz   ACME    RNA      TARGETED                       1          VISIT   1         2018-   2
 26|                                    GenePanel                                                                        TRANSCRIPTION                                                                                                   PROTEIN                                                              TRANSCRIPTOME                             1                 09-04
 27|                                    250                                                                              INDICATOR                                                                                                       PRODUCT                                                              SEQUENCING
 28| 7     ABC-123   GF       123101    ACME        7       2         ABU3908A52   AH749754   TRNSCPTN   Transcription   FRAGMENT         23658                    23658         23658                    hs37d5       12        GAPDH   GENE WITH   ENST00000396861.5   AH749754.fastq.gz   ACME    RNA      TARGETED                       1          VISIT   1         2018-   2
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:93-93` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:91 (score 0.875)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  93| | 6 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 6 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | GENETIC TRANSCRIPTION INDICATOR | no | | no | | | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
~~~~

### 121. `ig34_p0226_a015` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:8988 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 7 | ABC-123 | GF | 123101 | 7 | 2 | ABU3908AS2 | AH749754 | TRNSCPTN | Transcription | FRAGMENT COUNT | 23658 | | 23658 | | 1s37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396615.5 | AH749754.fasta.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | | 2018-09-18 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 27-29 行 (自动定位, 词覆盖 0.882; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 26|                                    GenePanel                                                                        TRANSCRIPTION                                                                                                   PROTEIN                                                              TRANSCRIPTOME                             1                 09-04
 27|                                    250                                                                              INDICATOR                                                                                                       PRODUCT                                                              SEQUENCING
 28| 7     ABC-123   GF       123101    ACME        7       2         ABU3908A52   AH749754   TRNSCPTN   Transcription   FRAGMENT         23658                    23658         23658                    hs37d5       12        GAPDH   GENE WITH   ENST00000396861.5   AH749754.fastq.gz   ACME    RNA      TARGETED                       1          VISIT   1         2018-   2
 29|                                    GenePanel                                                                        COUNT                                                                                                           PROTEIN                                                              TRANSCRIPTOME                             1                 09-18
 30|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:94-94` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:92 (score 0.882)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  94| | 7 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 7 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | FRAGMENT COUNT | 23658 | | 23658 | 23658 | | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
~~~~

### 122. `ig34_p0226_a016` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:9001 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 8 | ABC-123 | GF | 123101 | 8 | 2 | ABU3908AS2 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 148.6268 | -MBP | 148.6268 | 148.6268 | MBP | 1s37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396615.5 | AH749754.fasta.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | FRAGMENTS PER KILOBASE MILLION FORMULA | 1 | VISIT 1 | | 2018-09-18 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 31-34 行 (自动定位, 词覆盖 0.902; 版式以原 PDF 为准):

~~~~
 30|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING
 31| 8     ABC-123   GF       123101    ACME        8       2         ABU3908A52   AH749754   TRNSCPTN   Transcription   NORMALIZED       148.6268      /MBP       148.6268      148.6268      /MBP       hs37d5       12        GAPDH   GENE WITH   ENST00000396861.5   AH749754.fastq.gz   ACME    RNA      TARGETED        FRAGMENTS      1          VISIT   1         2018-   2
 32|                                    GenePanel                                                                        LEVEL                                                                                                           PROTEIN                                                              TRANSCRIPTOME   PER KILOBASE              1                 09-18
 33|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      MILLION
 34|                                                                                                                                                                                                                                                                                                                          FORMULA
 35| 9     ABC-123   GF       123101    ACME        9       2         ABU3908A52   AH749754   TRNSCPTN   Transcription   NORMALIZED       691.5607      /10^6      691.5607      691.5607      /10^6      hs37d5       12        GAPDH   GENE WITH   ENST00000396861.5   AH749754.fastq.gz   ACME    RNA      TARGETED        COUNTS PER     1          VISIT   1         2018-   2
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:95-95` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:93 (score 0.902)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  95| | 8 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 8 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 148.6268 | /MBP | 148.6268 | 148.6268 | /MBP | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | FRAGMENTS PER KILOBASE MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
~~~~

### 123. `ig34_p0226_a017` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:9014 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 9 | ABC-123 | GF | 123101 | 9 | 2 | ABU3908AS2 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 691.5607 | 71P4 | 691.5607 | 691.5607 | 71P4 | 1s37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396615.5 | AH749754.fasta.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | COUNTS PER MILLION FORMULA | 1 | VISIT 1 | | 2018-09-18 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 35-37 行 (自动定位, 词覆盖 0.875; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 34|                                                                                                                                                                                                                                                                                                                          FORMULA
 35| 9     ABC-123   GF       123101    ACME        9       2         ABU3908A52   AH749754   TRNSCPTN   Transcription   NORMALIZED       691.5607      /10^6      691.5607      691.5607      /10^6      hs37d5       12        GAPDH   GENE WITH   ENST00000396861.5   AH749754.fastq.gz   ACME    RNA      TARGETED        COUNTS PER     1          VISIT   1         2018-   2
 36|                                    GenePanel                                                                        LEVEL                                                                                                           PROTEIN                                                              TRANSCRIPTOME   MILLION                   1                 09-18
 37|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      FORMULA
 38| 10    ABC-123   GF       123101    ACME        10      2         ABU3908A52   AH749754   TRNSCPTN   Transcription   NORMALIZED       521.716       /MBP       521.716       521.716       /MBP       hs37d5       12        GAPDH   GENE WITH   ENST00000396861.5   AH749754.fastq.gz   ACME    RNA      TARGETED        TRANSCRIPTS    1          VISIT   1         2018-   2
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:96-96` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:94 (score 0.875)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  96| | 9 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 9 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 691.5607 | /10^6 | 691.5607 | 691.5607 | /10^6 | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | COUNTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
~~~~

### 124. `ig34_p0226_a018` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:9027 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 10 | ABC-123 | GF | 123101 | 10 | 2 | ABU3908AS2 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 521.716 | -MBP | 521.716 | 521.716 | MBP | 1s37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396615.5 | AH749754.fasta.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | TRANSCRIPTS PER MILLION FORMULA | 1 | VISIT 1 | | 2018-09-18 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 37-39 行 (自动定位, 词覆盖 0.9; 版式以原 PDF 为准):

~~~~
 36|                                    GenePanel                                                                        LEVEL                                                                                                           PROTEIN                                                              TRANSCRIPTOME   MILLION                   1                 09-18
 37|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      FORMULA
 38| 10    ABC-123   GF       123101    ACME        10      2         ABU3908A52   AH749754   TRNSCPTN   Transcription   NORMALIZED       521.716       /MBP       521.716       521.716       /MBP       hs37d5       12        GAPDH   GENE WITH   ENST00000396861.5   AH749754.fastq.gz   ACME    RNA      TARGETED        TRANSCRIPTS    1          VISIT   1         2018-   2
 39|                                    GenePanel                                                                        LEVEL                                                                                                           PROTEIN                                                              TRANSCRIPTOME   PER MILLION               1                 09-18
 40|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      FORMULA
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:97-97` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:95 (score 0.9)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  97| | 10 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 10 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 521.716 | /MBP | 521.716 | 521.716 | /MBP | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | TRANSCRIPTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
~~~~

### 125. `ig34_p0226_a019` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:9040 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 11 | ABC-123 | GF | 123101 | 11 | 2 | ABU3908AS2 | AH749754 | TRNSCPTN | Transcription | PERCENTILE RANK | 0.99 | % | 0.99 | 0.99 | % | 1s37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396615.5 | AH749754.fasta.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | | 2018-09-18 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 40-42 行 (自动定位, 词覆盖 0.886; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 39|                                    GenePanel                                                                        LEVEL                                                                                                           PROTEIN                                                              TRANSCRIPTOME   PER MILLION               1                 09-18
 40|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      FORMULA
 41| 11    ABC-123   GF       123101    ACME        11      2         ABU3908A52   AH749754   TRNSCPTN   Transcription   PERCENTILE       0.99          %          0.99          0.99          %          hs37d5       12        GAPDH   GENE WITH   ENST00000396861.5   AH749754.fastq.gz   ACME    RNA      TARGETED                       1          VISIT   1         2018-   2
 42|                                    GenePanel                                                                        RANK                                                                                                            PROTEIN                                                              TRANSCRIPTOME                             1                 09-18
 43|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:98-98` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:96 (score 0.886)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  98| | 11 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 11 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | PERCENTILE RANK | 0.99 | % | 0.99 | 0.99 | % | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
~~~~

### 126. `ig34_p0226_a020` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:9053 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 12 | ABC-123 | GF | 123101 | 12 | 2 | ABU3908AS2 | AH749754 | TRNSCPTN | Transcription | GENETIC TRANSCRIPTION INDICATOR | yes | | yes | | 1s37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396615.5 | AH749754.fasta.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | | 2018-09-18 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 44-46 行 (自动定位, 词覆盖 0.879; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 43|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING
 44| 12    ABC-123   GF       123101    ACME        12      2         ABU3908A52   AH749754   TRNSCPTN   Transcription   GENETIC          yes                      yes                                    hs37d5       12        GAPDH   GENE WITH   ENST00000396861.5   AH749754.fastq.gz   ACME    RNA      TARGETED                       1          VISIT   1         2018-   2
 45|                                    GenePanel                                                                        TRANSCRIPTION                                                                                                   PROTEIN                                                              TRANSCRIPTOME                             1                 09-18
 46|                                    250                                                                              INDICATOR                                                                                                       PRODUCT                                                              SEQUENCING
 47| 13    ABC-123   GF       123101    ACME        13      1         ABC1234567   AP483910   TRNSCPTN   Transcription   NORMALIZED       -                        -             -                        GRCh38.p12             ACTB    GENE WITH   NM_001101.5                             ACME    RNA      TARGETED        DIFFERENCES    1          VISIT   1         2018-   2
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:99-99` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:97 (score 0.879)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  99| | 12 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 12 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | GENETIC TRANSCRIPTION INDICATOR | yes | | yes | | | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
~~~~

### 127. `ig34_p0226_a021` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:9066 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 13 | ABC-123 | GF | 123101 | 13 | 3 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 0.056299177 | | 0.056299177 | 0.056299177 | | GRCH38g12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | | 2018-09-18 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 47-51 行 (自动定位, 词覆盖 0.974; 版式以原 PDF 为准):

~~~~
 46|                                    250                                                                              INDICATOR                                                                                                       PRODUCT                                                              SEQUENCING
 47| 13    ABC-123   GF       123101    ACME        13      1         ABC1234567   AP483910   TRNSCPTN   Transcription   NORMALIZED       -                        -             -                        GRCh38.p12             ACTB    GENE WITH   NM_001101.5                             ACME    RNA      TARGETED        DIFFERENCES    1          VISIT   1         2018-   2
 48|                                    GenePanel                                                                        LEVEL            0.056299177              0.056299177   0.056299177                                             PROTEIN                                                              TRANSCRIPTOME   OF LOG2                   1                 09-18
 49|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      INTENSITIES
 50|                                                                                                                                                                                                                                                                                                                          FORMULA
 51| 14    ABC-123   GF       123101    ACME        14      1         ABC1234567   AP483910   TRNSCPTN   Transcription   NORMALIZED       -                        -             -                        GRCh38.p12             GAPDH   GENE WITH   NM_001256799.3                          ACME    RNA      TARGETED        DIFFERENCES    1          VISIT   1         2018-   2
 52|                                    GenePanel                                                                        LEVEL            0.046787999              0.046787999   0.046787999                                             PROTEIN                                                              TRANSCRIPTOME   OF LOG2                   1                 09-18
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:100-101` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:98 (score 0.974)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 100| | 13 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 13 | 1 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | -0.056299177 | | -0.056299177 | -0.056299177 | | GRCh38.p12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
 101| | 14 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 14 | 1 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | -0.046787999 | | -0.046787999 | -0.046787999 | | GRCh38.p12 | | GAPDH | GENE WITH PROTEIN PRODUCT | NM_001256799.3 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
~~~~

### 128. `ig34_p0226_a022` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:9079 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 14 | ABC-123 | GF | 123101 | 14 | 3 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 0.046787999 | | 0.046787999 | 0.046787999 | | GRCH38g12 | GAPDH | GENE WITH PROTEIN PRODUCT | NM_001256799.3 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | | 2018-09-18 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 49-52 行 (自动定位, 词覆盖 0.974; 版式以原 PDF 为准):

~~~~
 48|                                    GenePanel                                                                        LEVEL            0.056299177              0.056299177   0.056299177                                             PROTEIN                                                              TRANSCRIPTOME   OF LOG2                   1                 09-18
 49|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      INTENSITIES
 50|                                                                                                                                                                                                                                                                                                                          FORMULA
 51| 14    ABC-123   GF       123101    ACME        14      1         ABC1234567   AP483910   TRNSCPTN   Transcription   NORMALIZED       -                        -             -                        GRCh38.p12             GAPDH   GENE WITH   NM_001256799.3                          ACME    RNA      TARGETED        DIFFERENCES    1          VISIT   1         2018-   2
 52|                                    GenePanel                                                                        LEVEL            0.046787999              0.046787999   0.046787999                                             PROTEIN                                                              TRANSCRIPTOME   OF LOG2                   1                 09-18
 53|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      INTENSITIES
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:101-101` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:99 (score 0.974)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 101| | 14 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 14 | 1 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | -0.046787999 | | -0.046787999 | -0.046787999 | | GRCh38.p12 | | GAPDH | GENE WITH PROTEIN PRODUCT | NM_001256799.3 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
~~~~

### 129. `ig34_p0226_a023` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:9092 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 15 | ABC-123 | GF | 123101 | 15 | 2 | ABC1234567 | AP483910 | GENESIG | Gene Signature | GENETIC TRANSCRIPTION INDICATOR | LOW | | LOW | | GRCH38g12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | GENE SIGNATURE | 1 | VISIT 1 | | 2018-09-18 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 46-56 行 (自动定位, 词覆盖 0.97; 版式以原 PDF 为准):

~~~~
 45|                                    GenePanel                                                                        TRANSCRIPTION                                                                                                   PROTEIN                                                              TRANSCRIPTOME                             1                 09-18
 46|                                    250                                                                              INDICATOR                                                                                                       PRODUCT                                                              SEQUENCING
 47| 13    ABC-123   GF       123101    ACME        13      1         ABC1234567   AP483910   TRNSCPTN   Transcription   NORMALIZED       -                        -             -                        GRCh38.p12             ACTB    GENE WITH   NM_001101.5                             ACME    RNA      TARGETED        DIFFERENCES    1          VISIT   1         2018-   2
 48|                                    GenePanel                                                                        LEVEL            0.056299177              0.056299177   0.056299177                                             PROTEIN                                                              TRANSCRIPTOME   OF LOG2                   1                 09-18
 49|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      INTENSITIES
 50|                                                                                                                                                                                                                                                                                                                          FORMULA
 51| 14    ABC-123   GF       123101    ACME        14      1         ABC1234567   AP483910   TRNSCPTN   Transcription   NORMALIZED       -                        -             -                        GRCh38.p12             GAPDH   GENE WITH   NM_001256799.3                          ACME    RNA      TARGETED        DIFFERENCES    1          VISIT   1         2018-   2
 52|                                    GenePanel                                                                        LEVEL            0.046787999              0.046787999   0.046787999                                             PROTEIN                                                              TRANSCRIPTOME   OF LOG2                   1                 09-18
 53|                                    250                                                                                                                                                                                              PRODUCT                                                              SEQUENCING      INTENSITIES
 54|                                                                                                                                                                                                                                                                                                                          FORMULA
 55| 15    ABC-123   GF       123101    ACME        15      2         ABC1234567   AP483910   GENESIG    Gene            GENETIC          LOW                      LOW                                    GRCh38.p12             ACTB    GENE WITH   NM_001101.5                             ACME    RNA      TARGETED        IFN-1 GENE     1          VISIT   1         2018-   2
 56|                                    GenePanel                                                        Signature       TRANSCRIPTION                                                                                                   PROTEIN                                                              TRANSCRIPTOME   SIGNATURE                 1                 09-18
 57|                                    250                                                                              INTERPRETATION                                                                                                  PRODUCT                                                              SEQUENCING
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:99-102` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:100 (score 0.97)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  99| | 12 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 12 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | GENETIC TRANSCRIPTION INDICATOR | yes | | yes | | | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
 100| | 13 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 13 | 1 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | -0.056299177 | | -0.056299177 | -0.056299177 | | GRCh38.p12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
 101| | 14 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 14 | 1 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | -0.046787999 | | -0.046787999 | -0.046787999 | | GRCh38.p12 | | GAPDH | GENE WITH PROTEIN PRODUCT | NM_001256799.3 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
 102| | 15 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 15 | 2 | ABC1234567 | AP483910 | GENESIG | Gene Signature | GENETIC TRANSCRIPTION INTERPRETATION | LOW | | LOW | | | GRCh38.p12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | IFN-1 GENE SIGNATURE | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
~~~~

### 130. `ig34_p0226_a024` — supp:TRIAGE_ATOM_ERR

- PDF 页 226 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:9105 (lane B pack_016; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 16 | ABC-123 | GF | 123101 | 16 | 3 | ABC1234567 | AP483910 | GENESIG | Gene Signature | GENETIC TRANSCRIPTION SCORE | | | 1.120819661 | 1.120819661 | | GRCH38g12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | 8N-1 GENE SIGNATURE | 1 | VISIT 1 | | 2018-09-18 | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt` 第 55-58 行 (自动定位, 词覆盖 0.914; 版式以原 PDF 为准):

~~~~
 54|                                                                                                                                                                                                                                                                                                                          FORMULA
 55| 15    ABC-123   GF       123101    ACME        15      2         ABC1234567   AP483910   GENESIG    Gene            GENETIC          LOW                      LOW                                    GRCh38.p12             ACTB    GENE WITH   NM_001101.5                             ACME    RNA      TARGETED        IFN-1 GENE     1          VISIT   1         2018-   2
 56|                                    GenePanel                                                        Signature       TRANSCRIPTION                                                                                                   PROTEIN                                                              TRANSCRIPTOME   SIGNATURE                 1                 09-18
 57|                                    250                                                                              INTERPRETATION                                                                                                  PRODUCT                                                              SEQUENCING
 58| 16    ABC-123   GF       123101    ACME        16      3         ABC1234567   AP483910   GENESIG    Gene            SCORE            -                        -             -                        GRCh38.p12             ACTB    GENE WITH   NM_001101.5                             ACME    RNA      TARGETED        IFN-1 GENE     1          VISIT   1         2018-   2
 59|                                    GenePanel                                                        Signature                        1.126819661              1.126819661   1.126819661                                             PROTEIN                                                              TRANSCRIPTOME   SIGNATURE                 1                 09-18
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:102-103` (来源: near triage kb_loc knowledge_base/domains/GF/examples.md:101 (score 0.914)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 102| | 15 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 15 | 2 | ABC1234567 | AP483910 | GENESIG | Gene Signature | GENETIC TRANSCRIPTION INTERPRETATION | LOW | | LOW | | | GRCh38.p12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | IFN-1 GENE SIGNATURE | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
 103| | 16 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 16 | 3 | ABC1234567 | AP483910 | GENESIG | Gene Signature | SCORE | -1.126819661 | | -1.126819661 | -1.126819661 | | GRCh38.p12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | IFN-1 GENE SIGNATURE | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
~~~~

### 131. `ig34_p0389_a012` — supp:TRIAGE_ATOM_ERR

- PDF 页 389 · 原子类型 TABLE_ROW · 所在节 `§7.2.1 Trial Arms (TA) – Example 1`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:7628 (lane B pack_014; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | EX1 | TA | P | Placebo | 2 | RI | Run-In | | | RUN-IN |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0389.txt` 第 27-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26| 1        EX1       TA       P       Placebo   1         SCRN   Screen                                        SCREENING
 27| 2        EX1       TA       P       Placebo   2         RI     Run-In      Randomized to Placebo             RUN-IN
 28| 3        EX1       TA       P       Placebo   3         P      Placebo                                       TREATMENT
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:123` (来源: triage kb_loc knowledge_base/domains/TA/examples.md:123 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 121|         S[Screen]
 122|     end
 123|     subgraph RE["Run-In Epoch"]
 124|         RI[Run-In]
 125|     end
~~~~

### 132. `ig34_p0389_a013` — supp:TRIAGE_ATOM_ERR

- PDF 页 389 · 原子类型 TABLE_ROW · 所在节 `§7.2.1 Trial Arms (TA) – Example 1`
- triage 类 **ATOM_ERR** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T1 triage ATOM_ERR (writer, reviewed=True); 出处 `.work/10_tier_b_repair/work/triage_merged.json:7641 (lane B pack_014; T1.3 reviewer 100%)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | EX1 | TA | P | Placebo | 3 | P | Placebo | Randomized to Placebo | | TREATMENT |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0389.txt` 第 27-28 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26| 1        EX1       TA       P       Placebo   1         SCRN   Screen                                        SCREENING
 27| 2        EX1       TA       P       Placebo   2         RI     Run-In      Randomized to Placebo             RUN-IN
 28| 3        EX1       TA       P       Placebo   3         P      Placebo                                       TREATMENT
 29| 4        EX1       TA       A       A         1         SCRN   Screen                                        SCREENING
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:124` (来源: triage kb_loc knowledge_base/domains/TA/examples.md:124 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 122|     end
 123|     subgraph RE["Run-In Epoch"]
 124|         RI[Run-In]
 125|     end
 126|     subgraph TE["Treatment Epoch"]
~~~~

