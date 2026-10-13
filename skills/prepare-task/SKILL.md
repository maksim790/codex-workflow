---
name: prepare-task
description: Use when a user wants to turn a development request, including a large multi-part request, into task tickets in an existing setup-project Obsidian-compatible vault before starting implementation. Do not use to implement the tickets or onboard a repository without a vault.
---

# Prepare Task

Create a reviewable Markdown task ticket in the target Git repository's existing project vault. For a large request, create a main ticket and linked, verifiable child tickets when their boundaries are settled. The user later passes a ticket's title, filename, or Tasks-relative path to `$start-task`. A ticket records the requested outcome and evidence-backed acceptance contract; it is not an implementation plan, ADR, architecture page, or proof that checks ran.

## Locate and inspect

1. Use the active Git repository unless the user names another target. Inspect `git status --short` and preserve existing staged, unstaged, and untracked work. Read applicable `AGENTS.md`, its documentation navigation, and the existing vault `Home.md`. Confirm the vault path from project evidence. If the vault is absent or ambiguous, ask for the path or suggest `$setup-project init`; do not create a parallel `docs/` tree.
2. Read only task-relevant vault pages, ADRs, source, tests, interface schemas, and command definitions. Treat code as evidence of current behavior, not proof of desired product rules. Distinguish explicit user requirements, verified repository facts with source links, inferences, and unresolved choices. Do not run unknown scripts, install dependencies, expose secrets, or alter application code.
3. Select an existing project Tasks directory if one is established; otherwise use `<vault>/12-Development/Tasks`. Put a standalone ticket at `<Tasks>/<descriptive-slug>.md`; use the grouped layout below for a new large task. Each path must resolve inside the intended vault and repository, including through symlinks or junctions. Use portable, distinct names. Do not create an index or empty taxonomy pages solely for tickets. Check every planned destination before writing; if a ticket or group path exists and the user has not requested its update, stop and ask whether to continue it or use a new name. Do not overwrite it, silently create a duplicate, or move existing flat tickets into groups without a separate request.

## Write the ticket

Use ordinary relative Markdown links so the ticket works in Obsidian, GitHub, and other Markdown readers. Include these essentials:

- **Title, creation time, and status:** Record `Created: YYYY-MM-DDTHH:MM:SSZ` using the current UTC time when first writing the ticket, and preserve that value on later updates. New tickets use status `draft`, `needs-decision`, or `ready`; `done` is set by `$start-task` only after verified completion. `ready` means no known blocking requirements question, not approval of an implementation or proof of verification.
- **Goal:** the observable outcome and stated reason. Do not invent business intent.
- **Request and evidence:** summarize explicit user requirements and link to relevant code, tests, contracts, vault pages, and project instructions. Label inferences; report code/documentation conflicts rather than resolving them by guesswork.
- **Scope and constraints:** what is included, important exclusions, compatibility boundaries, and user restrictions. Omit exclusions that add no clarity.
- **Acceptance criteria:** numbered, observable outcomes and meaningful error or boundary cases. Do not encode an unapproved product choice as a criterion, even provisionally.
- **Architecture and contracts:** only task-relevant current boundaries and likely impact. Link to durable documentation instead of copying it; mark proposed changes and decisions as proposed.
- **Verification plan:** applicable approved project DoD gates and task-specific checks with actual command/source evidence where known. Label all as planned, unavailable, or unknown; never imply they passed.
- **Open questions and decisions:** record material unresolved choices with consequences and user decisions when supplied. Omit this section when none remain.

Keep the ticket concise for local tasks; add detail for consequential changes. Omit empty optional sections and invented placeholders. Record all known material open questions in the ticket, but ask the user one focused question at a time. A material unanswered question makes status `needs-decision`. You may write a useful draft while awaiting an answer, but do not mark it `ready` or invent the answer. Record an answer as a user decision, then adjust affected criteria and status. Do not run Superpowers implementation procedures or choose a final Fast/Full mode here; `$start-task` does that against current evidence.

## Large requests

Keep one ticket when the request has one independently verifiable outcome. When it spans several substantial deliverables or boundaries, such as a new service plus contracts, data ownership, consumer integration, and deployment, prepare a main coordination ticket and smaller child tickets. Split by verifiable outcome and dependency, not by source file, technical layer, or a fixed number of tickets.

For a **new** large task, create `<Tasks>/<task-slug>/00-main.md`. Put children in the same folder as `01-<slug>.md`, `02-<slug>.md`, and so on. The two-digit prefix records the initial suggested order; the ordered list in `00-main.md` shows the current order. Explicit dependencies, not filename numbers, determine what can start. Do not rename existing files merely because the order changes; update the main list and links instead. Keep established flat tickets where they are unless the user separately requests a migration.

1. Identify the main ticket as coordination work. Put the overall goal, shared constraints, architecture decisions, integration acceptance criteria, and proposed sequence in it. If an unresolved product or architecture decision determines child boundaries, write **only** this main ticket as `needs-decision`. Label the breakdown as proposed, ask for the blocking decision, and do not create children that assume its answer.
2. Once the relevant boundaries are supported by repository evidence and explicit user decisions, create numbered child tickets for the agreed deliverables. Each child states its own outcome, scope, observable criteria, meaningful failure cases, verification plan, and dependencies. Link to the main ticket for shared decisions instead of copying them. Link each child from the main ticket and check both directions. A child with its own unresolved question stays `needs-decision`. Do not invent a dependency merely from numbering.
3. Order children by dependency and identify the first one to start. The main ticket coordinates the overall result and final integration; it is not an implementation task. Recommend `$start-task <task-folder>` to start the first open child without a separate selection. If that child has a blocking question or unmet dependency, `$start-task` pauses its implementation. If the user later asks to continue a `needs-decision` main ticket, reread it and current evidence before proposing focused updates and creating children. Preserve agreed requirements; obtain approval before changing them.

Writing a **new** ticket is authorized by the user's invocation of this skill. For a requested update to an existing ticket, inspect its content and Git state, propose the focused changes, and obtain approval before altering agreed requirements or decisions. Preserve unrelated human notes and existing ADRs.

## Handoff

Read every written ticket back, check relative links and Git diff, and report paths, statuses, evidence used, unresolved questions, and unverified assumptions. For a decomposed request, report the dependency order and the first child. Give `$start-task <task-folder>` as the handoff; a standalone ticket still uses `$start-task <filename-or-Tasks-relative-path>`. Do not claim code was implemented, tests passed, or the tickets were approved merely because files exist. Do not commit, push, create a PR, merge, or deploy without authorization for that action.
