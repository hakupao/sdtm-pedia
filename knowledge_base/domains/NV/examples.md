# NV — Examples

## Example 1

This example demonstrates the SDTM-based modeling of nervous system information collected and generated from separate positron emission tomography (PET) or PET/computed tomography (PET/CT) procedures.

For this study, measures for standard uptake value ratios (SUVRs) were taken from 3 PET or PET/CT scans. SPDEVID shows the scanner used. NVLNKID can be used to link to the imaging procedure record in the Procedures domain (PRLNKID), as well as to the tracer administration record in the Procedure Agents domain (AGLNKID). AGLNKID would be used to determine which tracer uptake is being measured (SUVR), and therefore to which biomarker the findings pertain. NVDTC corresponds to the date of the PET or PET/CT procedure from which these results were obtained.

**Rows 1-2:** Show the SUVR findings based on a PET/CT scan for a subject.
**Rows 3-4:** Show the SUVR findings based on a PET/CT scan for a subject.
**Rows 5-6:** Show the SUVR findings based on a fluorodeoxyglucose (FDG)-PET scan for a subject.

**nv.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | NVSEQ | NVREFID | NVLNKID | NVTESTCD | NVTEST | NVORRES | NVORRESU | NVSTRESC | NVSTRESN | NVSTRESU | NVLOC | NVDIR | NVMETHOD | VISITNUM | NVDTC |
|-----|---------|--------|---------|---------|-------|---------|---------|----------|--------|---------|----------|----------|----------|----------|-------|-------|----------|----------|-------|
| 1 | ABC123 | NV | AD01-101 | 22 | 1 | 1236 | 03 | SUVR | Standard Uptake Value Ratio | 0.95 | RATIO | 0.95 | 0.95 | RATIO | PRECUNEUS | | PET/CT SCAN | 1 | 2012-05-22 |
| 2 | ABC123 | NV | AD01-101 | 22 | 2 | 1236 | 03 | SUVR | Standard Uptake Value Ratio | 1.17 | RATIO | 1.17 | 1.17 | RATIO | CINGULATE CORTEX | POSTERIOR | PET/CT SCAN | 1 | 2012-05-22 |
| 3 | ABC123 | NV | AD01-102 | 22 | 1 | 1237 | 04 | SUVR | Standard Uptake Value Ratio | 1.21 | RATIO | 1.21 | 1.21 | RATIO | PRECUNEUS | | PET/CT SCAN | 1 | 2012-05-22 |
| 4 | ABC123 | NV | AD01-102 | 22 | 2 | 1237 | 04 | SUVR | Standard Uptake Value Ratio | 1.78 | RATIO | 1.78 | 1.78 | RATIO | CINGULATE CORTEX | POSTERIOR | PET/CT SCAN | 1 | 2012-05-22 |
| 5 | ABC123 | NV | AD01-103 | 44 | 1 | 1238 | 05 | SUVR | Standard Uptake Value Ratio | 1.52 | RATIO | 1.52 | 1.52 | RATIO | PRECUNEUS | | FDGPET | 1 | 2012-05-22 |
| 6 | ABC123 | NV | AD01-103 | 44 | 2 | 1238 | 05 | SUVR | Standard Uptake Value Ratio | 1.63 | RATIO | 1.63 | 1.63 | RATIO | CINGULATE CORTEX | POSTERIOR | FDGPET | 1 | 2012-05-22 |

The reference region used for the SUVR tests shown is represented in a supplemental qualifiers dataset.

**suppnv.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|
| 1 | ABC123 | NV | AD01-101 | NVSEQ | 1 | REFREG | Reference Region | CEREBELLUM |
| 2 | ABC123 | NV | AD01-101 | NVSEQ | 2 | REFREG | Reference Region | CEREBELLUM |
| 3 | ABC123 | NV | AD01-102 | NVSEQ | 1 | REFREG | Reference Region | CEREBELLUM |
| 4 | ABC123 | NV | AD01-102 | NVSEQ | 2 | REFREG | Reference Region | CEREBELLUM |
| 5 | ABC123 | NV | AD01-103 | NVSEQ | 1 | REFREG | Reference Region | PONS |
| 6 | ABC123 | NV | AD01-103 | NVSEQ | 2 | REFREG | Reference Region | PONS |

The RELREC table displays the dataset relationship that links procedure to multiple NV domain records — specifically how an individual AG administration record related to a scan is linked to multiple NV domain records. The RELREC table uses --LNKID to relate the PR and AG domains to each other and to NV, and --REFID to relate NV and Device in Use (DU).

In this example, the sponsor has maintained 2 sets of reference identifiers (REFID values) for the specific purpose of being able to relate records across multiple domains. Because the SDTMIG-MD advocates the use of --REFID to link a group of settings to the results obtained from the reading or interpretation of the test (see SDTMIG-MD, Device-in-Use (DU) domain assumptions), --LNKID has been used to establish the relationships between the procedure, the substance administered during the procedure, and the results obtained from the procedure. --LNKID is unique for each procedure for each subject, so datasets may be related to each other as a whole.

**Rows 1-2:** Show the relationship between the scan, represented in PR, and the radiolabel tracer used, represented in AG. There is only 1 tracer administration for each scan, and only 1 scan for each tracer administration, so the relationship is one-to-one.
**Rows 3-4:** Show the relationship between the scan, represented in PR, and the SUVR results obtained from the scan, represented in NV. Each scan yields 2 results, so the relationship is one-to-many.
**Rows 5-6:** Show the relationship between the radiolabel tracer used and the SUVR results for each scan. This relationship may seem indirect, but it is not: The choice of radiolabel has the potential to affect the results obtained. Because the relationship between PR and AG is one-to-one and the relationship between PR and NV is one-to-many, the relationship between AG and NV must be one-to-many.
**Rows 7-8:** Show the relationship between the SUVR results and the specific settings for the device used for each scan. There is more than 1 result from each scan, and more than 1 setting for each scan, so the relationship is many-to-many. This relationship is unusual and challenging to manage in a join/merge, and only represents the concept of this relationship.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC123 | PR | | PRLNKID | | ONE | 6 |
| 2 | ABC123 | AG | | AGLNKID | | ONE | 6 |
| 3 | ABC123 | PR | | PRLNKID | | ONE | 7 |
| 4 | ABC123 | NV | | NVLNKID | | MANY | 7 |
| 5 | ABC123 | AG | | AGLNKID | | ONE | 8 |
| 6 | ABC123 | NV | | NVLNKID | | MANY | 8 |
| 7 | ABC123 | NV | | NVLNKID | | MANY | 9 |
| 8 | ABC123 | DU | | DULNKID | | MANY | 9 |

## Example 2

This example shows how to represent components of a pattern-reversal visual evoked-potential (VEP) test elicited by checkerboard stimuli for a subject with optic neuritis. VEPs are detected via an EEG using leads that are placed on the back of the subject's head. It is important to note that the nature of VEP testing is such that NVMETHOD should be equal to "EEG", and that NVCAT should be equal to "VISUAL EVOKED POTENTIAL". Several latencies from each eye — including N75, P100, and N145, as well as the P100 peak-to-peak amplitude (75-100) — are collected and should be represented in NVTESTCD/NVTEST. Details about the VEP equipment including the checkerboard size should be represented in the appropriate device domains. To interpret, each VEP component is compared against normative values established by the laboratory using healthy controls.

In this example, a VEP component is considered abnormal if it falls outside of 3 standard deviations from the normative lab mean. These low and high values are stored in NVORNRLO and NVORNRHI, respectively, and the interpretation of each VEP component is represented in NVNRIND. In addition to interpreting each VEP component as normal or abnormal, the overall test for each eye may have an interpretation. In this scenario, NVTESTCD/NVTEST should be equal to "INTP" (Interpretation) and NVORRES should represent whether the overall test in each eye is normal or abnormal. NVGRPID links the each VEP component to the overall interpretation.

The NV domain should be used to represent the VEP latencies, P100 peak-to-peak amplitude, and their interpretations. SPDEVID allows the results to be related to both the VEP testing device and the checkerboard size.

**Rows 1-4:** Show the VEP measurements for the right eye.
**Row 5:** Shows that when all the components of right eye VEP are considered together (NVGRPID=1), the overall test is interpreted as abnormal.
**Rows 6-9:** Show the VEP measurements for the left eye.
**Row 10:** Shows that when all the components of left eye VEP are considered together (NVGRPID=2), the overall test is interpreted as abnormal.

**nv.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | FOCID | NVSEQ | NVGRPID | NVTESTCD | NVTEST | NVCAT | NVORRES | NVORRESU | NVSTRESC | NVSTRESN | NVSTRESU | NVORNRLO | NVORNRHI | NVNRIND | NVLOC | NVLAT | NVMETHOD | VISITNUM | NVDTC |
|-----|---------|--------|---------|---------|-------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|----------|----------|---------|-------|-------|----------|----------|-------|
| 1 | MS123 | NV | MS01-01 | 123 | OD | 1 | 1 | N75LAT | N75 Latency | VISUAL EVOKED POTENTIAL | 79.8 | msec | 79.8 | 79.8 | msec | 54.68 | 94 | NORMAL | EYE | RIGHT | EEG | 1 | 2013-02-08 |
| 2 | MS123 | NV | MS01-01 | 123 | OD | 2 | 1 | P100LAT | P100 Latency | VISUAL EVOKED POTENTIAL | 129 | msec | 129 | 129 | msec | 76.75 | 113.71 | ABNORMAL | EYE | RIGHT | EEG | 1 | 2013-02-08 |
| 3 | MS123 | NV | MS01-01 | 123 | OD | 3 | 1 | N145LAT | N145 Latency | VISUAL EVOKED POTENTIAL | 181 | msec | 181 | 181 | msec | 114.27 | 156.03 | ABNORMAL | EYE | RIGHT | EEG | 1 | 2013-02-08 |
| 4 | MS123 | NV | MS01-01 | 123 | OD | 4 | 1 | P100AMP | P100 Amplitude | VISUAL EVOKED POTENTIAL | 5.02 | uV | 5.02 | 5.02 | uV | 5.26 | 12.64 | ABNORMAL | EYE | RIGHT | EEG | 1 | 2013-02-08 |
| 5 | MS123 | NV | MS01-01 | 123 | OD | 5 | 1 | INTP | Interpretation | VISUAL EVOKED POTENTIAL | ABNORMAL | | ABNORMAL | | | | | | EYE | RIGHT | EEG | 1 | 2013-02-08 |
| 6 | MS123 | NV | MS01-01 | 123 | OS | 6 | 2 | N75LAT | N75 Latency | VISUAL EVOKED POTENTIAL | 83.8 | msec | 83.8 | 83.8 | msec | 54.42 | 95.1 | NORMAL | EYE | LEFT | EEG | 1 | 2013-02-08 |
| 7 | MS123 | NV | MS01-01 | 123 | OS | 7 | 2 | P100LAT | P100 Latency | VISUAL EVOKED POTENTIAL | 126 | msec | 126 | 126 | msec | 76.9 | 115.78 | ABNORMAL | EYE | LEFT | EEG | 1 | 2013-02-08 |
| 8 | MS123 | NV | MS01-01 | 123 | OS | 8 | 2 | N145LAT | N145 Latency | VISUAL EVOKED POTENTIAL | 160 | msec | 160 | 160 | msec | 115.65 | 157.65 | ABNORMAL | EYE | LEFT | EEG | 1 | 2013-02-08 |
| 9 | MS123 | NV | MS01-01 | 123 | OS | 9 | 2 | P100AMP | P100 Amplitude | VISUAL EVOKED POTENTIAL | 4.37 | uV | 4.37 | 4.37 | uV | 4.78 | 12.7 | ABNORMAL | EYE | LEFT | EEG | 1 | 2013-02-08 |
| 10 | MS123 | NV | MS01-01 | 123 | OS | 10 | 2 | INTP | Interpretation | VISUAL EVOKED POTENTIAL | ABNORMAL | | ABNORMAL | | | | | | EYE | LEFT | EEG | 1 | 2013-02-08 |

Information about the VEP device is not shown. Identifying information would be represented using the DI domain, and any properties of the device that may change between assessments would be represented in the DO and DU domains. See the SDTMIG-MD for examples of these domains.
