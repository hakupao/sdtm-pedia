# tools/git-hooks/

Project-local git hooks (tracked in repo, opt-in install).

## Install (one-time)

```bash
git config core.hooksPath tools/git-hooks
```

This points git at this directory for all hooks. Run from repo root.

To revert: `git config --unset core.hooksPath`

## Hooks

### pre-commit

**Warning-only** (never blocks the commit). Current checks:

- **Trilingual tutorial lockstep** — if you stage a change to
  `release/v*/self_deploy/<platform>/tutorial.<lang>.md` but not the
  matching `en` / `ja` / `zh` siblings, prints a warning to stderr.
  Reason: external tutorials should stay in sync across the three
  languages. The warning is *not* a blocker — just a reminder.

## Adding new checks

Append to `pre-commit`. Keep checks warning-only (`exit 0`) unless there is
a strong reason to block. Use `pass --no-verify` as the user-side escape.
