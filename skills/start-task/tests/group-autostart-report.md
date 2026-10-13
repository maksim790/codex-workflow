# Group autostart integration check (2026-10-13)

## Scope and method

The change makes `$start-task <task-folder>` select the first open child from the current ordered list in `00-main.md` without asking which child to choose. `00-main.md` remains coordination and final verification only. The checks below used disposable Git repositories under the Windows temporary directory, not this workflow repository. They exercised agent interpretation of the skill text; they did not test Codex UI skill discovery or dispatch.

## RED baseline

An agent applied the previous `start-task` instructions to a disposable group with `00-main.md`, `01-contract.md`, and `02-service.md`. The previous text stopped before selecting a child and allowed an explicit whole-parent request to implement `00-main.md` as a task. The fixture remained read-only: Git status and hashes of five files did not change.

## GREEN execution

An agent applied the revised skill to a fresh group `count-validation` with child `01-range-check.md` before `02-docs.md`. `$start-task count-validation` went directly to `01` without a child-choice prompt. The agent wrote a regression test for an inverted range; it failed before the code change, then passed after a focused guard was added. The project check `python -B -m unittest discover -s tests -v` passed 2/2 tests. Only the application file, test file, and child `01` changed. The agent set `01` to `done` with completion evidence; `00-main.md` and `02-docs.md` were unchanged (`git diff --exit-code` on both returned 0). `git diff --check` passed.

## Routing edge cases

Agents used separate disposable Git fixtures for these read-only cases:

| Invocation/state | Observed route |
| --- | --- |
| Explicit `group/00-main.md`, including a request to do the whole parent | First open child `01`; no implementation under `00` |
| Group directory with `01` done and `02` ready | Child `02` directly |
| First child `needs-decision` | Stop at that child's decision; do not skip to `02` |
| First child has an unmet dependency | Stop at the dependency; do not skip to `02` |
| All children done, main still open | Overall integration verification only |
| Main `needs-decision`, no agreed child tickets | Stop at preparation/decision gate; do not treat the empty list as completed |
| Main already done | Read-only; no repeated verification or closure |

For all seven routing fixtures, `git status --porcelain=v1` was empty before and after, and full-file SHA-256 snapshots matched. These are agent routing checks, not application implementation tests. The empty-list and already-done checks used the final revised skill text.

## Structural checks and limits

`quick_validate.py` reported `Skill is valid!` for both `start-task` and the related `prepare-task` skill. `git diff --check` passed. These script checks establish skill structure and diff formatting, not behavior. The execution fixture establishes one concrete agent implementation route; other routing cases were read-only. UI autocomplete, skill dispatch, and a real project's multi-child integration remain untested by this change.
