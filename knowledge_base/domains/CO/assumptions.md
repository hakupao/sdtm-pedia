# CO — Assumptions

1. The Comments special-purpose domain provides a solution for submitting free-text comments related to data in 1 or more SDTM domains (as described in Section 8.5, Relating Comments to a Parent Domain) or collected on a separate CRF page dedicated to comments. Comments are generally not responses to specific questions; instead, comments usually consist of voluntary free-text or unsolicited observations.

2. Although the structure for the Comments domain in the SDTM is "One record per comment", USUBJID is required in the comments domain for human clinical trials, so the structure of the Comments domain in the SDTMIG is "One record per comment per subject."

3. The CO dataset accommodates 3 sources of comments:
   a. Those unrelated to a specific domain or parent record(s), in which case the values of the variables RDOMAIN, IDVAR, and IDVARVAL are null. CODTC should be populated if captured. See Example 1, row 1.
   b. Those related to a domain but not to specific parent record(s), in which case the value of the variable RDOMAIN is set to the DOMAIN code of the parent domain and the variables IDVAR and IDVARVAL are null. CODTC should be populated if captured. See Example 1, row 2.
   c. Those related to a specific parent record or group of parent records, in which case the value of the variable RDOMAIN is set to the DOMAIN code of the parent record(s) and the variables IDVAR and IDVARVAL are populated with the key variable name and value of the parent record(s). Assumptions for populating IDVAR and IDVARVAL are further described in Section 8.5, Relating Comments to a Parent Domain. CODTC should be null because the timing of the parent record(s) is inherited by the comment record. See Example 1, rows 3-5.

4. When the comment text is longer than 200 characters, the first 200 characters of the comment will be in COVAL, the next 200 in COVAL1, and additional text stored as needed to COVALn. See Example 1, rows 3-4. Additional information about how to relate comments to parent SDTM records is provided in Section 8.5, Relating Comments to a Parent Domain.

5. The variable COREF may be null unless it is used to identify the source of the comment. See Example 1, rows 1 and 5.

6. Identifier variables and Timing variables may be added to the CO domain, but the following qualifiers would generally not be used in CO: --GRPID, --REFID, --SPID, TAETORD, --TPT, --TPTNUM, --ELTM, --TPTREF, --RFTDTC.
