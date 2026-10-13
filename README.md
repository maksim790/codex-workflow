# Codex workflow

Reusable Codex skills for documenting a repository, preparing development tickets, and implementing them. Tickets live in the project's Obsidian-compatible Markdown vault; source code and current tests remain the evidence for how the project works.

## Quick start

After installing the skills (see below), run these in a Codex chat opened in the **target project's Git repository**, not in this skills repository:

```text
$setup-project init
$prepare-task Create a notification service for order events
$start-task
```

1. **Set up the project once.** `$setup-project init` inspects the repository and proposes `AGENTS.md`, a documentation vault, and project Definition of Done checks. It writes the proposed files only after approval. An existing project with a vault can start at step 2.
2. **Prepare the task.** `$prepare-task <request>` researches relevant code and docs, creates a ticket, and breaks a large request into ordered child tickets. It resolves material requirements and design decisions, presents any required implementation plan for approval, then shows a short “Что будет сделано” summary for final scope correction. A new ticket becomes `ready` only after its applicable approvals are recorded.
3. **Execute the ticket.** Bare `$start-task` in the **same conversation** uses the most recent unambiguous, still-current `prepare-task` handoff for this repository. In another conversation, pass the ticket or group name explicitly. `start-task` checks that any approved plan still fits current evidence, implements the selected work, runs applicable checks, and marks the verified ticket `done`.

## Commands and arguments

These are **skill invocations in chat**, not built-in terminal commands or a fixed CLI parser. Text after the skill name supplies a mode, ticket reference, or natural-language request.

| Invocation | What it does |
| --- | --- |
| `$setup-project init` | Propose initial `AGENTS.md`, vault, and project DoD; write after approval. |
| `$setup-project update` | Compare code and documentation; propose and apply approved updates. |
| `$setup-project audit` | Report documentation drift and broken links without changing files. |
| `$setup-project doctor` | Propose repairs to verified documentation structure or links; apply after file-by-file approval. |
| `$setup-project doctor tasks` | Repair task-file structure and references after approval; never change task status. |
| `$prepare-task <request>` | Create a ticket, or a `00-main.md` group with numbered child tickets for a large request. |
| `$prepare-task Update the existing group <name> ...` | Rework a named existing task group without silently replacing agreed requirements or human notes. |
| `$start-task` | Start the current-conversation prepared ticket; otherwise list up to five unfinished tickets and wait for selection. |
| `$start-task <name-or-path>` | Start a ticket by title, filename, group name, or path relative to the vault's Tasks directory. |
| `$start-task Full <request>` | Request Full mode for a direct task. Fast may be requested too, but `start-task` escalates it when risk requires Full. |

Examples of ticket references:

```text
$start-task notifications-service
$start-task notifications-service/01-event-contract.md
$start-task 01-event-contract
```

If a reference is ambiguous or missing, `start-task` shows candidates and waits; it does not guess or turn the unmatched text into a new task. A bare invocation without a usable handoff lists unfinished tickets, including `ready` tickets. `ready` means *prepared for implementation*; only `done` means *verified as completed*.

## Large tasks and status

Large requests are stored as `Tasks/<task-name>/00-main.md` plus `01-...md`, `02-...md`, and later children. The current order comes from `00-main.md`; explicit dependencies still gate what can start. Invoking the group starts its first unfinished child without another child-selection prompt. One invocation handles one child. `00-main.md` coordinates the group and is never an implementation ticket; after all children are `done`, invoke the group for final integration verification.

| Status | Meaning |
| --- | --- |
| `draft` | Ticket is being prepared or awaits final scope/plan review. |
| `needs-decision` | A material requirement, design, or plan decision blocks the affected work. |
| `ready` | Preparation and applicable approvals are recorded; implementation has not been verified. |
| `done` | `start-task` verified acceptance criteria and mandatory Definition of Done checks and recorded completion evidence. |

`start-task` reuses an approved plan without asking for its approval again. If the plan is missing, unapproved, or materially stale, it returns the affected work to `prepare-task`. Routine implementation choices within the approved scope do not require another plan review. Direct requests to `$start-task <request>` remain supported without a ticket.

## Installation and safeguards

Copy or link each skill directory under a Codex-discoverable location such as `~/.agents/skills/`, then refresh skill discovery. See [setup-project](skills/setup-project/README.md) and [start-task](skills/start-task/README.md) for skill-specific notes. `start-task` uses installed Superpowers procedures when applicable.

`setup-project audit` is read-only. `doctor tasks` never infers or sets `done`. Preparation does not implement the ticket. Completion of local work does not by itself authorize a commit, push, PR, merge, or deployment.

Project context: [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) · [DOCUMENTATION_STANDARD.md](DOCUMENTATION_STANDARD.md) · [NEXT_STEPS.md](NEXT_STEPS.md).
