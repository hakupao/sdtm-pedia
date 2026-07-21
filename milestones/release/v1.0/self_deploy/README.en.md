# Administrator Deployment Guide Index

This directory is for administrators who need to configure or maintain SDTM Pedia platform instances. Most end users only need access to a Claude Project, ChatGPT GPT, Gemini Gem, or NotebookLM notebook that has already been configured by their team.

## When To Read This Directory

- Your team does not yet have an entry point and needs an administrator to create one.
- You need to maintain access permissions, instructions, and knowledge files consistently inside an organization.
- You need to update or replace an existing instance.
- You need to verify that an instance can answer basic SDTM lookup questions.

## Platform Guides

| Platform | Guide | Best Fit |
| --- | --- | --- |
| Claude Projects | [claude/tutorial.en.md](./claude/tutorial.en.md) | Complex standards explanation and cross-domain reasoning. |
| ChatGPT GPTs | [chatgpt/tutorial.en.md](./chatgpt/tutorial.en.md) | Team daily lookup and a familiar ChatGPT entry point. |
| Gemini Gems | [gemini/tutorial.en.md](./gemini/tutorial.en.md) | Longer-context synthesis and exploratory comparison. |
| NotebookLM | [notebooklm/tutorial.en.md](./notebooklm/tutorial.en.md) | Strict source boundaries and citation review. |

## Shared Principles

- Use the instruction file and `uploads/` contents from the matching platform directory in this release package.
- Do not rewrite instruction text or rename knowledge files unless you are deliberately maintaining a new version.
- Confirm your organization's data security, patient privacy, and access-permission requirements before sharing.
- Give edit access only to a small number of maintainers; most users should have use-only access.
- After updates, use a few standard questions to confirm variable-definition, domain-boundary, and controlled-terminology lookup.

## Boundary of Use

The deployed platform instance remains an SDTM lookup aid. It does not replace CDISC publications, medical judgment, project-level mapping review, or internal quality processes.
