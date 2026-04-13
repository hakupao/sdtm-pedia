# TE — Assumptions

The Trial Elements (TE) dataset contains the definitions of the elements that appear in the Trial Arms (TA) dataset. An element may appear multiple times in the TA table because it appears either (1) in multiple arms, (2) multiple times within an arm, or (3) both. However, an element will appear only once in the TE table.

Each row in the TE dataset may be thought of as representing a "unique element" in the same sense of "unique" as a CRF template page for a collecting certain type of data referred to as "unique page."

An element is a building block for creating study cells, and an arm is composed of study cells. Trial elements represent an interval of time that serves a purpose in the trial and are associated with certain activities affecting the subject. "Week 2 to week 4" is not a valid trial element.

1. There are no gaps between elements. The instant one element ends, the next element begins. A subject spends no time "between" elements.

2. The ELEMENT (Description of the Element) variable usually indicates the treatment being administered during an element, or, if no treatment is being administered, the other activities that are the purpose of this period of time (e.g., "Screening", "Follow-up", "Washout"). In some cases, this time period may be quite passive (e.g., "Rest"; "Wait, for disease episode").

3. The TESTRL (Rule for Start of Element) variable identifies the event that marks the transition into this element. For elements that involve treatment, this is the start of treatment.

4. For elements that do not involve treatment, TESTRL can be more difficult to define. For washout and follow-up elements, which always follow treatment elements, the start of the element may be defined relative to the end of a preceding treatment. For example, a washout period might be defined as starting 24 or 48 hours after the last dose of drug for the preceding treatment element or epoch. This definition is not totally independent of the TA dataset, because it relies on knowing where in the trial design the element is used, and that it always follows a treatment element. Defining a clear starting point for the start of a non-treatment element that always follows another non-treatment element can be particularly difficult. The transition may be defined by a decision-making activity such as enrollment or randomization.

5. TESTRL for a treatment element may be thought of as "active" whereas the start rule for a non-treatment element—particularly a follow-up or washout element—may be "passive." The start of a treatment element will not occur until a dose is given, no matter how long that dose is delayed. Once the last dose is given, the start of a subsequent non-treatment element is inevitable, as long as another dose is not given.

6. Note that the date/time of the event described in TESTRL will be used to populate the date/times in the Subject Elements (SE) dataset, so the date/time of the event should be captured in the CRF.

7. Specifying TESTRL for an element that serves the first element of an arm in the TA dataset involves defining the start of the trial. In the examples in this document, obtaining informed consent has been used as "Trial Entry."

8. TESTRL should be expressed without referring to arm. If the element appears in more than 1 arm in the TA dataset, then the element description (ELEMENT) **must not** refer to any arms.

9. TESTRL should be expressed without referring to epoch. If the element appears in more than 1 epoch in the TA dataset, then the Element description (ELEMENT) **must not** refer to any epochs.

10. For a blinded trial, it is useful to describe TESTRL in terms that separate the properties of the event that are visible to blinded participants from the properties that are visible only to those who are unblinded. For treatment elements in blinded trials, wording such as the following is suitable: "First dose of study drug for a treatment epoch, where study drug is X."

11. Element end rules are rather different from element start rules. The actual end of one element is the beginning of the next element. Thus, the element end rule does not give the conditions under which an element does end, but the conditions under which it should end or is planned to end.

12. At least 1 of TEENRL and TEDUR must be populated. Both may be populated.

13. TEENRL describes the circumstances under which a subject should leave this element. Element end rules may depend on a variety of conditions. For instance, a typical criterion for ending a rest element between oncology chemotherapy-treatment element would be, "15 days after start of element and WBC counts have recovered." The TA dataset, not the TE dataset, describes where the subject moves next, so TEENRL must be expressed without referring to arm.

14. TEDUR serves the same purpose as TEENRL for the special (but very common) case of an element with a fixed duration. TEDUR is expressed in ISO 8601 format. For example, a TEDUR value of P6W is equivalent to a TEENRL of "6 weeks after the start of the element."

15. Note that elements that have different start and end rules are different elements and must have different values of ELEMENT and ETCD. For instance, elements that involve the same treatment but have different durations are different elements. The same applies to non-treatment elements.
