# ChatGPT GPT Administrator Guide

This guide is for administrators who need to configure or maintain an SDTM Pedia ChatGPT instance. Most end users only need access to a GPT that has already been configured by their team.

## When To Use This Guide

- Your team needs a shared SDTM lookup entry point.
- You want to maintain one organization-approved GPT configuration.
- You need to add SDTM Pedia knowledge files to a custom GPT.

## Prerequisites

- A ChatGPT account or organization role that can create custom GPTs.
- Access to this release package's `system_prompt.md` and `uploads/` folder.
- Awareness of your organization's AI tool, data security, and sharing policies.

## Deployment Steps

1. Create a new custom GPT in ChatGPT.
2. Paste the full contents of `system_prompt.md` into the Instructions area.
3. Add all 9 Markdown files from `uploads/` to the Knowledge area.
4. Save the GPT and set its name, description, and access permissions according to your organization's policy.
5. Use a few standard questions to confirm that the instance can answer SDTM variable, domain-boundary, and controlled-terminology questions.

## Suggested Name

Use a clear, non-misleading name, for example:

> SDTM Pedia - Internal Reference

The description should state that this is an SDTM standards lookup aid and does not replace CDISC publications or internal SOPs.

## Basic Verification

After deployment, confirm at minimum that it can:

- Explain the meaning, Core attribute, and controlled terminology for `AESER`.
- Distinguish appropriate use cases for `LB`, `MB`, and `IS`.
- Treat non-existent or non-applicable premises cautiously instead of inventing unsupported answers.

If answers are clearly off, first check that the Instructions are complete, all 9 knowledge files were uploaded, and the sharing settings were saved.

## Team Sharing

Before sharing, confirm:

- Whether access is limited to team members.
- Who can edit the GPT configuration.
- Whether users are prohibited from entering project-confidential, patient-level, or non-deidentified data.
- Whether a usage-boundary note should be included for the team.

Give edit access only to a small number of maintainers; most users should have use-only access.

## Maintenance

- Test updates in an administrator copy before replacing the team instance.
- Record the update date, maintainer, and summary of changes.
- If a standards-content issue is found, check CDISC official sources before updating the release package.

## Boundary of Use

This GPT is an SDTM lookup aid. Formal submissions, medical coding, project-level mapping, and quality control still require responsible review under your organization's process.
