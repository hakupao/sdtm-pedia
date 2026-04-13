# EG — Assumptions

1. EGREFID is intended to store an identifier (e.g., UUID) for the associated ECG tracing. EGXFN is intended to store the name of and path to the electrocardiogram (ECG) waveform file when it is submitted.

2. There are separate codelists for tests and results based on regular 10-second ECGs and for tests and results based on Holter monitoring.
   a. Associations between some ECG abnormality tests and response codelists are described in the ECG codeable (available at https://www.cdisc.org/standards/terminology/controlled-terminology).

3. For non-individual ECG beat data and for aggregate ECG parameter results (e.g., "QT interval", "RR", "PR", "QRS"), EGREFID is populated for all unique ECGs, so that submitted SDTM data can be matched to the actual ECGs stored in the ECG warehouse. Therefore, this variable is expected for these types of records.

4. For individual-beat parameter results, waveform data will not be stored in the warehouse, so there will be no associated identifier for these beats.

5. The method for QT interval correction is specified in the test name by controlled terminology: EGTESTCD = "QTCFAG" and EGTEST = "QTcF Interval, Aggregate" is used for Fridericia's formula; EGTESTCD = "QTCBAG" and EGTEST = "QTcB Interval, Aggregate", is used for Bazett's formula.

6. EGBEATNO is used to differentiate between beats in beat-to-beat records.

7. EGREPNUM is used to differentiate between multiple repetitions of a test within a given time frame.

8. EGNRIND can be added to indicate where a result falls with respect to reference range defined by EGORNRLO and EGORNRHI. Examples: "HIGH", "LOW". Clinical significance would be represented as described in Section 4.5.5, Clinical Significance for Findings Observation Class Data, in EGCLSIG (see also EG Example 1).

9. When "QTcF Interval, Aggregate" or "QTcB Interval, Aggregate" is derived by the sponsor, the derived flag (EGDRVFL) is set to "Y". However, when the "QTcF Interval, Aggregate" or "QTcB Interval, Aggregate" is received from a central provider or vendor, the value would go into EGORRES and EGDRVFL would be null (see Section 4.1.8.1, Origin Metadata for Variables).

10. If this domain is used in conjunction with the ECG QT Correction Model Data (QT) domain:
    a. For each QT correction method used in the study, values of EGTESTCD and EGTEST are assigned at the study level.
    b. The sponsor should assign values for EGTESTCD/EGTEST appropriately with clear documentation on what each test code represents. For example, if the protocol calls for computing the top two best fit models, the sponsor could choose to name the top best fit model QTCIAG1 and the second best fit model QTCIAG2, in rank order.

11. Any identifiers, timing variables, or findings general observation-class qualifiers may be added to the EG domain, but the following qualifiers would not generally be used: --MODIFY, --BODSYS, --SPEC, --SPCCND, --FAST, --SEV. It is recommended that --LOINC not be used.
