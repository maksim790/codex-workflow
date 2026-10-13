# `prepare-task` design

Status: approved in conversation on 2026-10-13 and implemented. See `skills/prepare-task/tests/integration-report.md` for observed behavior and limits.

This records the original single-ticket design. Large-request decomposition was added later; see [large-task decomposition](2026-10-13-prepare-task-decomposition-design.md) for current behavior in that case.

## Purpose

`prepare-task` turns a user's development request into one reviewable Markdown ticket in the target repository's existing Obsidian-compatible vault. It prepares requirements before implementation. The user later invokes `$start-task` with that ticket's name or path; `start-task` validates the ticket against current repository evidence and executes it.

The ticket is a task contract. It is not an architecture encyclopedia, ADR, Superpowers design, implementation plan, or record of tests already run.

## Location and invocation

- The target is the active Git repository unless the user specifies another one.
- Locate the project vault through applicable `AGENTS.md`, existing documentation navigation, and `Home.md`. Do not silently create a vault or switch to an unrelated `docs/` directory when the intended vault is unclear. Ask for the path if evidence is insufficient.
- Default ticket path: `<vault>/12-Development/Tasks/<descriptive-slug>.md`. Respect an existing project task directory or user-specified path within the vault. Do not create an index or empty taxonomy sections just to store one ticket.
- A ticket is created on explicit `$prepare-task <request>` invocation. The request authorizes writing the new ticket, not overwriting an existing one or editing source code. Existing tickets require an explicit update request and focused diff.
- The user later invokes `$start-task <ticket-name-or-Tasks-relative-path>` in the same project. Explicit repository-relative or absolute paths also work. Clearly phrased direct requests to `start-task` remain possible, but the documented two-step path uses a ticket.

## Ticket content

Use Markdown headings and ordinary relative links that work in Obsidian, GitHub, and other Markdown readers. Include only relevant optional details; never generate empty sections or placeholder claims.

1. **Title and status:** `draft`, `needs-decision`, or `ready`. `ready` means there is no known blocking requirements question, not that implementation or verification has occurred.
   Record `Created: YYYY-MM-DDTHH:MM:SSZ` as a UTC timestamp when the ticket is first written; preserve it on later updates. This provides a stable order for the no-argument `$start-task` picker.
2. **Goal:** observable outcome and reason given by the user; do not invent a business goal.
3. **Request and evidence:** distinguish explicit user requirements, observed repository facts with source links, and inferences. Code proves current behavior, not desired business behavior.
4. **Scope and constraints:** included changes, meaningful exclusions, compatibility or security constraints, and known pre-existing work to preserve.
5. **Acceptance criteria:** numbered, observable outcomes and meaningful failure cases. Avoid prescribing an implementation in place of a result.
6. **Affected contracts and architecture:** only task-relevant boundaries, source links, and potential impacts. Record a proposal or unresolved choice as such; link to vault architecture pages and ADRs rather than duplicating them.
7. **Verification plan:** project DoD gates and task-specific checks known from inspected instructions/configuration, marked `planned`, `unavailable`, or `unknown`; no claim of execution.
8. **Open questions and decisions:** material questions, options and consequences when known, plus explicit user decisions. Omit this section when none remain.

## Preparation behavior

1. Inspect Git status, applicable project instructions, vault navigation, relevant architecture/domain/interface/ADR notes, source, tests, and CI or package commands. Avoid secrets and unknown scripts. Follow source links only as evidence.
2. Distill the task into the ticket fields. Ask focused questions for material uncertainty before marking the ticket `ready`. If a decision is unavailable, save a useful `needs-decision` draft with the unresolved choice; do not guess.
3. Check the target path and existing Git changes before writing. Create only the ticket and required parent directory; do not overwrite a different ticket or casually rewrite human notes. On a requested update, show the relevant diff and preserve agreed decisions unless the user changes them.
4. Check ticket links and inspect the resulting diff. Report the path, status, evidence inspected, unresolved decisions, and the `$start-task <filename-or-Tasks-relative-path>` invocation when ready.

## `start-task` handoff

When invoked with a ticket reference, `start-task` resolves it within the project's Tasks directory, reads the selected file, confirms it remains inside the target repository and intended vault, and treats it as the task's proposed contract. An existing explicit path takes precedence; ambiguous matches require selection, and missing names show suggestions without starting implementation. It checks status, acceptance criteria, unresolved decisions, relevant source and project instructions. It does not treat the ticket as higher priority than the user's current message or current code. A `needs-decision` or materially stale ticket blocks only dependent implementation; the agent asks for the missing decision or updates the ticket with authorization. A `ready` ticket still undergoes normal Fast/Full routing, applicable Superpowers gates, and three-layer DoD verification.

When invoked with only `$start-task`, the agent immediately lists the five newest tickets from the project vault task directory and waits for a number or ticket reference. It performs no task implementation or file write during discovery. Clearly phrased direct task descriptions keep their existing route. Tickets lacking a valid `Created` timestamp use file modification time as an approximate fallback and are labeled accordingly.

## Verification scenarios

- New task in a small vault: one ticket appears under the vault with evidence-linked, testable criteria and no empty sections or unrelated edits.
- Ambiguous product rule: the ticket records the unresolved choice and is not marked `ready`; no behavior is invented.
- Existing path or pre-existing user changes: no silent overwrite or unrelated mutation.
- Handoff: `start-task` uses the named ticket, checks it against current evidence, and does not silently implement unresolved or stale requirements.
- Missing vault: preparation asks for the actual path rather than constructing a parallel documentation tree.
