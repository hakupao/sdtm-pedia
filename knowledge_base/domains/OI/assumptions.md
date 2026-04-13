# OI — Assumptions

A special-purpose domain containing information that identifies levels of taxonomic nomenclature of microbes or parasites that have been either experimentally determined in the course of a study or are previously known, as in the case of lab strains used as reference in the study.

The biological classification of a non-host organism typically stops at the taxonomic rank of "species." Scientific taxonomic nomenclature below the rank of species is not clearly defined, lacks a globally accepted standard terminology, and is frequently organism-dependent. Therefore, the OI domain addresses organism taxonomy with a series of parameters that name the taxa appropriate to the organism and the granularity with which the organism has been identified in the particular study.

1. Non-host organisms include viruses and organisms such as pathogens or parasites, but also non-pathogenic organisms such as normal intestinal flora. Non-host organism identifiers are not to be used for host species identification (e.g., for animals used in preclinical studies), nor should they be used to represent other, non-taxonomy characteristics of non-host species (e.g., drug susceptibility, growth rates).

2. NHOID is sponsor-defined, with the following constraints:
    a. A unique NHOID must represent a unique identity as represented in its combination of OIPARMCD/OIVAL pairs. If 2 organisms share the same first 2 levels of taxonomy with regard to OIPARMCD/OIVAL, but 1 is identified to a third level and the other is not, they should be assigned 2 unique NHOIDs.
    b. Study sponsors should populate NHOID with intuitive name values based on either
        i. the name of the organism as reported by a lab or specified by the investigator, or
        ii. published references/databases where applicable and appropriate (e.g., when reference strain H77 is used in a HCV study, NHOID for this strain should be populated with "H77" or "HCV1a-H77").

3. NHOID can be used in any domain where observations about these organisms are being represented, allowing end users to determine what is known about the organism's identity by merging on NHOID, or by otherwise referring to the OI domain.

4. OIPARMCD and OIPARM must represent parameters for the identification of non-host organisms with regard to nomenclature only.
    a. Mostly, this will represent taxonomic ranks (i.e., species) as well as commonly used grouping terms (taxa that are not officially ranked, e.g., subtype, group, strain).
    b. They may also include other nomenclature terms that are less widely known but are used frequently for organism identification in a specific field of study (e.g., spoligotype in tuberculosis).
    c. They should be listed in the OI dataset in hierarchical order of least to most specific with increasing OISEQ values.

5. Variables not listed in the OI domain specification table should not be used in OI data sets.
