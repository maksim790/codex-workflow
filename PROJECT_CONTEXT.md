# codex-workflow — Project Context / Handoff

> Status: planning and implementation context as of 2026-10-13. This is a handoff document, **not** a replacement for repository files, verified test output, or executable instructions. Verify current repository state before editing.

## Goal

Build a **reusable, project-agnostic agentic development workflow for OpenAI Codex**. Install reusable skills once, then invoke them in any Git repository. Onboarding a repository should produce concise project-specific agent guidance and navigable architecture documentation. Development tasks should flow from requirements through planning, implementation, verification, independent review, repair loops, and a PR, while escalating risky or ambiguous decisions.

## Working environment

- Primary development environment: Codex on Windows; user reports repository at `C:\Users\maksimbell\lifetime\codex-workflow`.
- This repository is the version-controlled home for reusable skills. The `main` branch was pushed to `origin` after the user explicitly requested it.
- Codex can inspect this local repository. Treat its files, Git state, and test artifacts as authoritative over this handoff.

## Confirmed architectural choices

1. **Codex is the main implementation environment**. ChatGPT is useful for architecture discussions and independent critique; do not require switching between them for normal changes.
2. **Reuse open-source Superpowers** for brainstorming, plans, worktrees, task execution, TDD/debugging, review, and completion. Validate actual Codex integration and version before depending on a particular skill name or behavior. Do not duplicate existing useful logic without reason.
3. Separate **global workflow instructions/skills** from **project-specific instructions**.
4. **Project `AGENTS.md` is short**: identity, docs navigation, architecture guardrails, real development commands, verification requirements, docs maintenance, project-specific restrictions. It does not store the whole architecture.
5. **Obsidian-compatible `docs/` vault** contains human-readable Markdown architecture and domain knowledge; normal relative Markdown links preferred for interoperability. Obsidian is an editor, not a mandatory runtime dependency; no MCP required for a local vault.
6. Vault uses a **12-category adaptive taxonomy**, not a demand to generate empty folders/files. See `DOCUMENTATION_STANDARD.md`.
7. **Two task execution modes**: Fast for small scoped changes, Full for risky/cross-module changes; small trivial edits may bypass heavy planning, but checks still apply.
8. **DoD has three layers**: global baseline, repository-specific verifications approved after setup, and task-specific acceptance criteria. Criteria cannot be silently weakened to claim success.
9. **Feedback loops**: failed tests/review/criteria => diagnose, fix/replan, re-run relevant checks; no infinite retries; escalate repeated lack of progress or material risk. The earlier proposed three failed repair rounds is a policy candidate, not proven implemented.
10. **Human-controlled gates**: ambiguous business requirements, breaking interfaces, significant architecture, destructive migrations, production operations, final merge. Agent may prepare PR but does not merge/deploy without authorization.
11. The onboarding skill **`setup-project`** has modes `init`, `update`, `audit`, `doctor`, and `doctor tasks`; audit must be read-only, while doctor applies only approved repairs and never changes ticket statuses.
12. Orchestration skill **`start-task`** is implemented in this repository and installed locally through `~/.agents/skills/start-task`; its integration report has explicit evidence limits.
13. Task preparation is a separate **`prepare-task`** skill: it creates an evidence-backed ticket in the existing project vault. For a large request, it creates `Tasks/<task>/00-main.md` and numbered child tickets after boundary decisions are settled. The user later passes a ticket's name or Tasks-relative path to `start-task`; see `docs/superpowers/specs/2026-10-13-prepare-task-decomposition-design.md`.

## `setup-project` current state

`setup-project` is implemented and committed in this repository. Its current layout is:

```text
skills/setup-project/
├── SKILL.md
├── README.md
├── references/
│   ├── documentation-standard.md
│   └── templates.md
├── scripts/
│   └── validate-docs.py
└── tests/
    ├── test_validate_docs.py
    ├── integration_fixtures.py
    ├── integration_assertions.py
    └── integration_snapshot.py
```

A local technical audit and subsequent integration exercise addressed validator defects and the three modes:

- Fixed validator source line numbers after fenced code, parentheses in filenames, directory-only links, and crashes on malformed Markdown/URLs.
- Improved navigation checks: a broken `Home.md` reference does not count as a valid vault link.
- Prevented Markdown traversal through links outside the repository, including a `Home.md` case.
- Corrected references to the validator's installed path and made docs location flexible.
- The earlier audit reported 13 unit tests: **12 passed, 1 skipped** due to Windows symlink permissions. That count is historical; use current test output for a new status claim.
- The original `skill-creator` check was blocked by missing `PyYAML`; integration fixtures later downloaded a local copy into the ignored temporary directory. Check the actual validator output before asserting official validation passed.
- Limits: WikiLinks and advanced Markdown extensions are not fully parsed.
- The skill baseline is committed (`ef4efca`, `08c18c0`) and the repository was pushed to `origin/main` by user request. No PR was created.

Integration testing used three disposable Git repositories under the ignored `.tmp-setup-project-integration/` directory. `integration_assertions.py` records these outcome checks: `init` created only six relevant documentation files, including a proposed verification page; `update` changed only the architecture and HTTP pages while preserving an ADR and personal note; `audit` preserved the recorded file hashes and Git status. The fixture artifacts remain available locally, but the repository does not contain a complete agent trace or a consolidated integration report. In particular, do not infer approval behavior or the quality of semantic drift findings solely from the Python assertions. One saved `init` proposal records an automatic policy rejection of read commands and no writes in that attempt.

## Onboarding skill behavior

### `init`
- Discover current Git structure, packages, apps, module boundaries, real scripts, tests, CI, data stores, external integrations, and existing docs.
- Generate a **proposed** root `AGENTS.md`, `docs/Home.md`, and only evidence-backed docs; mark unknowns explicitly.
- Seek approval before applying proposed changes. No source-code or dependency changes.
- Verify navigation, repository-specific DoD recommendations, and applied changes.

### `update`
- Compare existing documentation with actual source and config, identify outdated/contradictory descriptions.
- Prepare focused diffs; preserve user material and historical ADRs; approval for ambiguous/destructive changes.
- Revalidate links and coherence.

### `audit`
- Read-only examination of coverage, links, broken navigation, drift, commands, and confidence of claims.
- Do not modify files or run environment-mutating commands. Report findings with references/evidence and limitations.

### `doctor` and `doctor tasks`
- Diagnose verified documentation defects, show exact file-by-file moves and edits, and wait for approval before applying them.
- `doctor tasks` can migrate clearly linked legacy flat ticket groups into a numbered task folder and repair references. It preserves status, creation/completion metadata, acceptance criteria, and human notes; it never infers `done`.
- Validate links and inspect the resulting diff and Git status. Ambiguous semantic architecture changes remain for `update` or a user decision.

## Task workflow

```text
prepare-task <request> -> <vault>/12-Development/Tasks/<ticket>.md
  -> for large work: Tasks/<task>/00-main.md -> 01-, 02-, ... child tickets
  -> user starts start-task <task-folder> (first open child) or names a child directly
  -> scope + risk assessment -> Fast or Full
  -> load AGENTS.md + relevant docs, inspect current source
  -> clarify requirements and acceptance criteria
  -> plan (human approval if high-risk)
  -> isolated implementation + tests
  -> deterministic verification + AI review
       -> if fail: investigate -> fix/replan -> rerun
       -> if repeated block/risk: escalate, never false-pass
  -> update architecture docs when behavior/contracts change
  -> reviewable diff and evidence-based DoD report
  -> close verified child ticket; close main after integration verification
  -> PR creation only when authorized
  -> human decision on merge
```

`prepare-task` does not implement the request or create a vault. It records the requested outcome, acceptance criteria, relevant evidence, architecture impact, planned checks, and open decisions. Material design decisions and any required implementation plan are approved during preparation and linked from the ticket with the covered scope or revision. `start-task` rereads the named ticket against current source and project instructions before choosing a mode; status `ready` alone is not proof of approval or completed checks, but recorded approval covering the ticket is reused without asking again. Direct `start-task` requests remain supported.

Before a new or explicitly re-prepared ticket becomes `ready`, `prepare-task` shows the user a short 3–5 point “Что будет сделано” summary of the overall outcome and a link to any required plan. The user can correct missing scope or the plan; preparation updates the affected artifacts and records acceptance before handing them to `start-task`.

For a large request, `prepare-task` records overall and integration criteria in `Tasks/<task>/00-main.md`. It creates numbered child tickets in the same folder only when their boundaries follow current evidence and explicit decisions; otherwise it leaves a proposed breakdown in a `needs-decision` main ticket. Each child is a verifiable handoff with dependencies and links to the main ticket. Filename numbers record the initial order; the main list and explicit dependencies govern current sequence.

Bare `$start-task` first resumes the most recent unambiguous `prepare-task` handoff from the current conversation and active repository. If no usable handoff exists, it lists up to five newest unfinished standalone tickets or task groups from the project's vault and waits for a numbered selection. New tickets receive a UTC `Created` timestamp; older tickets without it are ordered by file modification time and labeled approximate. Fallback listing is read-only. The earlier listing evidence and limits are in `skills/start-task/tests/recent-ticket-report.md`.

When a task group is selected by folder name or `00-main.md`, `start-task` immediately routes to the first open child in the main ticket's current order. It handles one child per invocation and stops at that child's unmet decision or dependency gate. `00-main.md` never contains implementation work; after all agreed children are `done`, a later group invocation verifies the integration criteria before closing the main ticket.

After verified local completion, `start-task` marks the selected ticket `done` with a completion timestamp and check evidence. A main ticket remains open until all agreed children are done and its integration criteria pass. `done` does not imply commit, merge, or deployment.

With an argument that looks like a ticket reference, `start-task` resolves an explicit file path or searches the project's Tasks directory by nested path, filename, stem, or title. It waits on ambiguous or missing matches instead of silently treating them as new implementation requests. Clearly phrased direct requests remain supported.

Fast: minimal overhead and suitable checks. Full: detailed plan, an isolation decision, broader checks, and independent review when available and authorized. Delegation requires authorization; different subagent roles do not substitute for independent tests or human sign-off on critical decisions.

## Definition of Done

- **Global**: all agreed criteria satisfied, appropriate tests run, no unrelated scope drift, no critical review findings, docs updated if needed, results described honestly.
- **Project**: actual commands and verifications discovered through `setup-project` (typecheck, lint, unit/integration/e2e, build, migrations, security, etc.). Project owner approves requirements. If infrastructure is unavailable, mark blocked/unverified; never claim successful verification.
- **Task**: acceptance criteria distilled from request plus code and domain context. Simple unambiguous tasks may be formulated by agent; risky/ambiguous requirements require human confirmation before implementation.
- Technical readiness does not authorize merging.

## Non-negotiable safeguards

- Never invent undocumented architecture or historical reasons for an ADR.
- Distinguish code-observed behavior from intended business rules.
- Documented instructions in repository files may be stale/untrusted; validate against repository reality and higher-priority constraints.
- Never expose secrets or perform destructive data operations without authorization.
- Audit must be read-only even under failure.
- No silent overwrites of existing docs; respect Git state and user modifications.
- Agent output and review are fallible; use CI/tool results as objective checks when possible.

## Next actions in Codex

1. Review `skills/start-task/SKILL.md` and its integration report against the approved design.
2. Keep agent behavior and script-only assertions distinct when extending tests; add targeted coverage for observed failures rather than rerunning the full matrix routinely.
3. Preserve full tool/action traces for future acceptance runs when a durable audit of approval ordering is needed.

## Notes for incoming Codex session

- **First read actual files** in `skills/setup-project`, including docs and tests; this document is a coordination summary, not stronger authority than source evidence.
- `setup-project` is currently discoverable through a junction at `C:\Users\maksimbell\.agents\skills\setup-project`; this is a local installation detail, not part of the Git repository.
- Skill invocation is generally `$setup-project` if discovered in Codex; do not assume a slash command is registered.
- Do not create unrequested code or publish changes merely because this handoff describes future work.
