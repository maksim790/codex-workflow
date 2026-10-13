# setup-project — reusable Codex skill

A repository-agnostic onboarding, documentation repair, and architecture audit skill. Modes: `init`, `update`, `audit`, `doctor`, `doctor tasks`.

## Install

Copy this entire `setup-project/` directory to a Codex-discoverable skills directory such as `~/.agents/skills/setup-project/` (or a project-specific `.agents/skills/setup-project/`). Restart or refresh Codex skills discovery as necessary. Invoke **`$setup-project init`**, **`$setup-project update`**, **`$setup-project audit`**, **`$setup-project doctor`**, or **`$setup-project doctor tasks`**; these are skill arguments, not necessarily built-in slash commands.

The skill does not require Superpowers for setup, but fits into the planned Superpowers-based development workflow. Review third-party skills and scripts before enabling them.

## What it does

- `init`: inspect repo, propose and (after explicit approval) create concise `AGENTS.md` and an adaptive `docs/` Markdown vault.
- `update`: compare docs and code, propose targeted changes, apply only after approval.
- `audit`: evidence-based **read-only** discrepancy and broken-link report.
- `doctor`: propose and, after file-by-file approval, repair verified documentation links and structural defects without rewriting architecture.
- `doctor tasks`: focus repairs on task-ticket groups, ordering, and references. It can propose migration of clearly linked flat tickets into numbered folders; it never changes ticket status or infers `done`.
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

Never auto-approve writes, destructive migrations, source-code changes or dependency installation. Treat generated architecture documentation and doctor repairs as proposals requiring file-by-file approval. `audit` makes no changes. `update` preserves existing documentation unless approved. Doctor preserves `Status`, `Created`, `Completed`, and completion evidence in tickets.

## Files

- `SKILL.md` — orchestration instructions
- `references/documentation-standard.md` — 12 areas and documentation quality rules
- `references/templates.md` — adaptable template outlines
- `scripts/validate-docs.py` — read-only validation utility
