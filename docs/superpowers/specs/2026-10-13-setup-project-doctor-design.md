# `setup-project doctor` design

Status: approved in conversation on 2026-10-13. The user chose repair modes for documentation and Tasks, with no task-status changes.

## Commands and boundaries

- `$setup-project doctor` diagnoses and proposes focused repairs for project instructions and the existing vault: broken local links, navigation, and structural inconsistencies supported by current repository evidence. It does not invent architectural facts or replace `update` for semantic documentation changes.
- `$setup-project doctor tasks` limits discovery and repairs to the established Tasks directory and references to its tickets. It compares the current `prepare-task` convention when available. It can migrate a clearly linked flat parent/child set into `Tasks/<task>/00-main.md`, `01-...md`, etc., number the children of an existing unnumbered group when order is explicit, repair links after moves, and reconcile a recorded order with explicit dependencies. It does not infer a group or dependency from similar names alone.
- `$setup-project audit` remains strictly read-only. Both doctor forms first inspect and prepare a file-by-file proposal, then wait for explicit approval before writing. Approval covers only listed moves, creations, edits, and deletions; a scope change needs renewed approval.

## Task repair rules

Preserve `Status`, `Created`, `Completed`, completion evidence, acceptance criteria, user notes, and ADR history. In particular, doctor never infers `done` from code or check results and never changes task statuses. If a ticket's completion appears inconsistent, report it for separate task review without repairing the status.

For migration, require evidence of the parent/child relationship and current order in links or ticket text. Check canonical source and destination paths, symlink/junction escapes, collisions, Git state, and references before proposing moves. Do not migrate ambiguous or user-modified groups by guesswork. The numbered filenames record the initial order; the main ticket's list holds current order and explicit dependencies govern execution. Preserve existing groups that already work.

## Verification

Before and after approved repairs, run the bundled read-only Markdown validator when available. For Tasks, also inspect all moved ticket paths, bidirectional group links, order/dependency consistency, and references from other repository Markdown. Verify `git diff` and status, and compare task metadata before and after. Report unresolved or unsupported link forms, unexecuted checks, and any remaining findings. Do not modify application code, install dependencies, commit, push, or publish.
