# setup-project — reusable Codex skill

A repository-agnostic onboarding and architecture documentation skill. Modes: `init`, `update`, `audit`.

## Install

Copy this entire `setup-project/` directory to a Codex-discoverable skills directory such as `~/.agents/skills/setup-project/` (or a project-specific `.agents/skills/setup-project/`). Restart or refresh Codex skills discovery as necessary. Invocation is **`$setup-project init`**, **`$setup-project update`**, or **`$setup-project audit`**; not necessarily a built-in slash command.

The skill does not require Superpowers for setup, but fits into the planned Superpowers-based development workflow. Review third-party skills and scripts before enabling them.

## What it does

- `init`: inspect repo, propose and (after explicit approval) create concise `AGENTS.md` and an adaptive `docs/` Markdown vault.
- `update`: compare docs and code, propose targeted changes, apply only after approval.
- `audit`: evidence-based **read-only** discrepancy and broken-link report.
- It proposes a **project-specific Definition of Done**; developers approve mandatory checks.

The 12-section documentation taxonomy is a guide, not 12 folders to create unconditionally. Obsidian is optional; `docs/` is plain Markdown.

## Validator

Standalone, read-only, Python 3.9+:

```bash
python -B ~/.agents/skills/setup-project/scripts/validate-docs.py --root . --vault docs
python -B ~/.agents/skills/setup-project/scripts/validate-docs.py --root . --vault docs --format json
```

Exit 1 for broken local Markdown links, unreadable Markdown, or missing vault/Home; exit 0 otherwise (warnings are nonblocking). Relative Markdown links, basic heading anchors, and whether Home links to an existing vault page are checked. It does not follow external URLs or verify semantic architectural correctness, Obsidian WikiLinks, images, or sophisticated Markdown extensions. It does not modify the repository.

## Safety

Never auto-approve writes, destructive migrations, source-code changes or dependency installation. Treat generated architecture documentation as a proposal requiring evidence review. `audit` makes no changes. `update` preserves existing documentation unless approved.

## Files

- `SKILL.md` — orchestration instructions
- `references/documentation-standard.md` — 12 areas and documentation quality rules
- `references/templates.md` — adaptable template outlines
- `scripts/validate-docs.py` — read-only validation utility
