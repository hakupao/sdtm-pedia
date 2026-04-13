# PE — Assumptions

1. PE findings reflect the presence or absence of physical signs of disease or abnormality observed during a general physical examination. Multiple body systems are assessed during a physical examination, often starting at the head and ending at the toes, where the body is evaluated by inspection, palpation (feeling with the hands), percussion (tapping with fingers), and auscultation (listening). The examination often includes macro assessments (e.g., normal/abnormal) of appearance, general health, behavior, and body system review from head to toe.
   a. Evaluation of targeted body systems (e.g., cardiovascular, ophthalmic, reproductive) as part of therapeutic specific assessments should be represented in the appropriate body system domain (e.g., CV, OE, RP, respectively).
   b. See CDASHIG Section 8.3.11, PE - Physical Examination (available at https://www.cdisc.org/standards/foundational/cdash/), for additional collection guidance.

2. Abnormalities observed during a physical examination may be encoded. When collected/reported as a PE finding, the verbatim value is represented in PEORRES and the encoded value in PESTRESC. When collected/reported as medical history or an adverse event, the verbatim value is represented in MHTERM or AETERM and the encoded value is represented in MHDECOD or AEDECOD, respectively.

3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the PE domain, but the following qualifiers would generally not be used: --XFN, --NAM, --LOINC, --FAST, --TOX, --TOXGR.
