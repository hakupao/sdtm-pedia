# NotebookLM Administrator Guide

This guide is for administrators who need to configure or maintain an SDTM Pedia NotebookLM instance. Most end users only need access to a notebook that has already been configured by their team.

## When To Use This Guide

- Your team wants stricter source boundaries and easier citation review.
- You need to maintain an SDTM Pedia notebook in NotebookLM.
- You need to add this release package's instructions and source files to NotebookLM.

## Prerequisites

- A Google account or organization role that can create and share NotebookLM notebooks.
- Access to this release package's `instructions.md` and `uploads/` folder.
- Confirmation that your organization permits the relevant materials to be used in NotebookLM under its data-security requirements.

## Deployment Steps

1. Create a new notebook in NotebookLM.
2. Add the 42 source Markdown files from `uploads/` to the notebook. Do not upload inventory or instruction files as sources.
3. Wait for file processing to complete and check that the source list is complete.
4. Add the full contents of `instructions.md` to the Chat Custom mode / custom instructions area.
5. Use a few standard questions to confirm that variable definitions, domain boundaries, and citation review work as expected.
6. Set sharing scope according to organization policy.

## Suggested Name

Recommended:

> SDTM Pedia - Internal Reference

The description should state that this is an SDTM standards lookup aid and does not replace CDISC publications or internal SOPs.

## Basic Verification

After deployment, confirm that it can:

- Explain the meaning and usage attributes of `AESER`.
- Answer common controlled terminology questions such as `LBNRIND`.
- Distinguish appropriate use cases for `LB`, `MB`, and `IS`.
- Show or point to reviewable sources in its answer.

If an answer cannot find content that should clearly be present, first check source completeness, file processing status, and whether the Custom mode instructions are complete.

## Team Sharing

Before sharing, confirm:

- Whether the link or invitation scope follows organization policy.
- Who can edit the notebook or sources.
- Whether project-confidential, patient-level, or non-deidentified data are prohibited.
- Whether ordinary users need a note that the notebook is for reference lookup only.

## Maintenance

- Copy an administrator test notebook before updating sources.
- Repeat basic verification after updates.
- Record update date, maintainer, change summary, and verification result.

## Boundary of Use

NotebookLM is best when strict source boundaries and citation review matter. It is still an SDTM lookup aid and does not replace CDISC official materials, medical judgment, or internal quality processes.
