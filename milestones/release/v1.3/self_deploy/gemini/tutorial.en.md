# Gemini Gem Administrator Guide

This guide is for administrators who need to configure or maintain an SDTM Pedia Gemini Gem. Most end users only need access to a Gem that has already been configured by their team.

## When To Use This Guide

- Your team wants an SDTM lookup entry point in Gemini.
- You need to maintain one approved Gem configuration.
- You need to add the release package instructions and knowledge files to a Gemini Gem.

## Prerequisites

- A Google account or Workspace role that can create and configure Gemini Gems.
- Access to this release package's `system_prompt.md` and `uploads/` folder.
- Confirmation that your organization permits the relevant materials to be used in Gemini under its data-security requirements.

## Deployment Steps

1. Create a new Gem in Gemini.
2. Paste the full contents of `system_prompt.md` into Gem instructions.
3. Add the 4 Markdown files from `uploads/` as knowledge files.
4. Save the Gem and set its name, description, and sharing permissions.
5. Use a few standard questions to confirm that variable definitions, domain boundaries, and cross-topic explanations work as expected.

## Suggested Name

Recommended:

> SDTM Pedia - Internal Reference

The description should state that this is an SDTM standards lookup aid and does not replace CDISC publications or internal SOPs.

## Basic Verification

After deployment, confirm that it can:

- Explain the meaning and usage attributes of `AESER`.
- Distinguish appropriate use cases for `LB`, `MB`, and `IS`.
- Treat deprecated concepts or non-existent variables cautiously.
- Provide reviewable support in its answer.

If answers are clearly off, first check that instructions are complete, all 4 knowledge files were added, and sharing settings are correct.

## Team Sharing

Before sharing, confirm:

- Whether access scope follows organization policy.
- Who can edit the Gem.
- Whether project-confidential, patient-level, or non-deidentified data are prohibited.
- Whether users need a short usage-boundary note.

Keep configuration management with a small number of maintainers; most users should only use the Gem.

## Maintenance

- Create an administrator test Gem before updating the official instance.
- After verification, update the official instance.
- Record update date, maintainer, change summary, and basic verification result.

## Boundary of Use

The Gemini Gem instance is an SDTM lookup and explanation aid. Formal submissions, medical coding, project-level mapping, and quality control still require responsible review under your organization's process.
