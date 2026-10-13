# Codex workflow roadmap

## Current baseline

- [x] `setup-project` is implemented, committed, installed locally, and pushed to `origin/main` by user request.
- [x] Disposable repositories and assertions cover `init`, `update`, and `audit`; see `PROJECT_CONTEXT.md` for exactly what the retained artifacts prove.
- [x] Add `setup-project doctor` and `doctor tasks` with proposal-before-write repair flow and no task-status changes; see `skills/setup-project/tests/doctor-report.md` for focused agent evidence.
- [x] `.gitignore` excludes local integration fixtures, Python caches, virtual environments, and local `.env` files.
- [ ] Reconcile and commit these handoff documents; they were staged separately from the skill.

## Known `setup-project` follow-up

- [ ] Preserve a concise integration report or trace that distinguishes actual agent decisions from Python artifact checks, if this evidence is needed for a future release claim.
- [ ] Check frontmatter with supported tooling when the required dependency is available; do not equate inspection with an official validator pass.
- [ ] Revisit WikiLinks and advanced Markdown parsing only if a real project requires them.

## `start-task` baseline

- [x] Inspect installed Superpowers 5.1.3 manifest and skill entry points in this Codex environment.
- [x] Specify Fast/Full routing, escalation policy, approval points, and stop conditions in `docs/superpowers/specs/2026-10-13-start-task-design.md`.
- [x] Implement an instruction-only orchestration skill with task criteria and global/project/task DoD.
- [x] Route to installed Superpowers skills without copying their procedures.
- [x] Exercise Fast UI, Full concurrent backend, and blocked mandatory-check cases with agents in disposable repositories; see `skills/start-task/tests/integration-report.md` for evidence and limits.
- [ ] Add a targeted scenario for absent Superpowers or absent project DoD if those conditions arise in use.
- [x] Install `start-task` via a junction in `~/.agents/skills/start-task` and verify discovery in a fresh read-only Codex CLI session.

## Ticket preparation and handoff

- [x] Approve the `prepare-task` design: one ticket in an existing project vault, then explicit `$start-task <path-to-ticket>`.
- [x] Add `prepare-task` and explicit ticket-path handling in `start-task`.
- [x] Finish the disposable-repository agent scenarios and record what they actually demonstrate in `skills/prepare-task/tests/integration-report.md`.
- [x] Verify installation and discovery of `prepare-task` without changing global Codex settings.
- [x] Make bare `$start-task` list the five newest vault tickets; see `skills/start-task/tests/recent-ticket-report.md` for observed behavior and limits.
- [x] Resolve ticket names and Tasks-relative paths without requiring the vault prefix; see `skills/start-task/tests/ticket-lookup-report.md` for evidence and limits.
- [x] Let `prepare-task` break large requests into a main ticket and linked child tickets after architecture decisions; see `skills/prepare-task/tests/decomposition-report.md` for agent evidence and limits.
- [x] Store new large requests in numbered task groups and close verified tickets with evidence; see `skills/prepare-task/tests/grouped-ticket-report.md` for the focused test record.
- [x] Route a selected task folder to its first open child without another selection; reserve `00-main.md` for coordination and final verification. See `skills/start-task/tests/group-autostart-report.md` for focused evidence and limits.
- [ ] Pilot the two-step workflow on a real, low-risk project task when one is available.

## Example opening prompt to Codex

> Read `PROJECT_CONTEXT.md`, `DOCUMENTATION_STANDARD.md`, and `NEXT_STEPS.md`, then inspect the actual repository and `git status`. Read the `start-task` integration report for its evidence limits and check current behavior before claiming new results. Do not overwrite existing work or publish without my instruction.
