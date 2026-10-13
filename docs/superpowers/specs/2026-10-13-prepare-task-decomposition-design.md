# Large-task decomposition for `prepare-task`

Status: approved in conversation on 2026-10-13. The user chose one main ticket followed by smaller linked tasks after architectural decisions are settled.

## Behavior

For a local, independently verifiable request, `prepare-task` keeps creating one ticket. For work spanning several meaningful deliverables or boundaries, it creates `Tasks/<task-slug>/00-main.md` and child tickets `01-<slug>.md`, `02-<slug>.md`, and so on in that folder. The main ticket records the overall outcome, shared constraints, architecture questions and decisions, integration acceptance criteria, and an ordered breakdown.

When a decision determines the proposed boundaries, the skill writes only the main ticket with status `needs-decision` and a **proposed** breakdown. It asks for the blocking decision and does not create child tickets that would encode a guessed architecture. A subsequent explicit request to continue preparation can update the main ticket and create children after the decision is recorded.

When the boundaries are supported by repository evidence and user decisions, the same invocation may create the main ticket and child tickets together. Each child has one verifiable outcome, task-specific criteria, dependencies, and links to the main ticket; the main ticket links back to children. Split by deliverable or contract, not by file, framework layer, or an arbitrary ticket count. Do not duplicate shared requirements across tickets. The main ticket is coordination and final integration context; it is never an implementation task.

The two-digit prefix records the initial suggested sequence. The ordered list in `00-main.md` is the current display order, while explicit dependencies control what can start. If the sequence changes, update the list without automatically renaming files or breaking links. Existing flat tickets are not migrated without a separate request. When bare `$start-task` falls back to listing, it shows a group as one open entry rather than filling its five-entry list with children.

## Completion

A ticket uses `done` only after its acceptance criteria and applicable global, project, and task DoD checks pass, or a known mandatory exception is explicitly accepted and recorded. `start-task` records a completion timestamp and concise evidence (checks/results and relevant code or diff references) in the ticket, then reports the next child. A failed, blocked, or unrun mandatory check leaves the ticket open. A main ticket becomes `done` only when required children are done and its overall integration criteria are verified; completing the last child alone does not close the main ticket. Selecting the group after all children are done starts that final **verification only**. `done` describes verified local task work, not a commit, merge, deployment, or publication.

## Safety and handoff

New tickets must live inside the established vault and Tasks directory. Check every destination before writing; an existing path blocks that file and requires a user choice. Preserve existing tickets, ADRs, and human notes. A new ticket is authorized by `$prepare-task`; changes to agreed requirements in an existing ticket still require approval. Verify links, read back all written tickets, and inspect the diff. Report the first child and the group invocation `$start-task <task-folder>`; this starts that child without a separate selection. If it is blocked, the ordinary decision/dependency gate still applies. Creating tickets does not authorize implementation or publication.
