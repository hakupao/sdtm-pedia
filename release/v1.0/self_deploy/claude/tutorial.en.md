# Claude Project Administrator Guide

This guide is for administrators who need to configure or maintain an SDTM Pedia Claude Project. Most end users only need access to a Project that has already been configured by their team.

## When To Use This Guide

- Your team needs a shared entry point for more complex SDTM standards lookup.
- You want to maintain one approved SDTM Pedia instance in Claude Projects.
- You need to add the release package knowledge files and project instructions to Claude.

## Prerequisites

- An account and organization role that can create Claude Projects.
- Access to this release package's `system_prompt.md` and `uploads/` folder.
- Confirmation that your organization permits the relevant materials to be used in Claude under its data-security requirements.

## Deployment Steps

1. Create a new Project in Claude.
2. Paste the full contents of `system_prompt.md` into Project instructions.
3. Upload all 19 Markdown files from `uploads/` to Project knowledge.
4. Save the Project and set its name, description, and access permissions.
5. Use a few standard questions to confirm that variable definitions, domain boundaries, and cross-domain explanations work as expected.

## Suggested Name

Recommended:

> SDTM Pedia - Internal Reference

The description should state that this is an SDTM standards lookup aid and does not replace CDISC publications or internal SOPs.

## Basic Verification

After deployment, confirm that it can:

- Explain key AE-domain variables and their usage attributes.
- Distinguish common domain boundaries such as LB, MB, and IS.
- Treat non-standard variables or datasets cautiously.
- Provide reviewable support in its answer.

If answers are off, first check that Project instructions are complete, all 19 knowledge files were uploaded, and filenames were not changed.

## Team Sharing

Before sharing, confirm:

- Who can access the Project.
- Who can modify instructions or knowledge files.
- Whether project-confidential, patient-level, or non-deidentified data are prohibited.
- Whether users need a short usage-boundary note.

Limit edit access to a small number of maintainers to avoid accidental configuration changes.

## Maintenance

- Create an administrator test Project before updating the official instance.
- After verification, replace the instructions or knowledge files in the official instance.
- Keep an update record with date, maintainer, change summary, and basic verification result.

## Boundary of Use

The Claude Project instance is an SDTM lookup and explanation aid. Formal submissions, medical coding, project-level mapping, and quality control still require responsible review under your organization's process.
