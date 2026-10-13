# Grouped tickets and completion — 2026-10-13

## Baseline

An agent applied the previous `prepare-task` instructions in a disposable Git repository at `C:\Users\MAKSIM~1\AppData\Local\Temp\prepare-task-layout-baseline-9b518ad5aac245909b57245174e9386b`. It created a main ticket and three children as four flat files directly under `Tasks`. The parent listed their sequence, but no group folder or `00`/`01` filename prefixes existed. The previous skills had only `draft`, `needs-decision`, and `ready`; `start-task` reported completion but did not close tickets.

## Grouped preparation

An agent applied the revised `prepare-task` in two disposable Git repositories under `C:\Users\maksimbell\AppData\Local\Temp\prepare-group-forward-ef22232ae6b34cb8932ae8f338c155c7`.

| Fixture | Files and result |
| --- | --- |
| Accepted notifications-service boundary | Created `Tasks/notifications-service/00-main.md`, `01-event-contract.md`, `02-service-delivery.md`, and `03-orders-integration.md`. All were `ready`. The main ticket gave the current order; children recorded explicit dependencies. |
| Service boundary undecided | Created only `Tasks/notifications-service/00-main.md`, status `needs-decision`, with a proposed breakdown and blocking question. |

The agent checked 20 relative links in the decided fixture, including links in both directions between main and children. Existing ADR and human-note hashes did not change. In both repositories Git status gained only the new Tasks directory. No application code or tests were run during ticket preparation.

## Selection and child closure

In disposable repository `C:\Users\maksimbell\AppData\Local\Temp\start-task-forward-70077436f3214e93aa02b14624dede6e`, an agent applied the revised `start-task`. Bare selection displayed the group once alongside an open standalone ticket and excluded a `done` standalone ticket. Group selection identified `01` as the first unblocked child. The agent added a regression test for a small fixture task; its first run failed as expected, then the implementation passed the mandatory `python -m unittest discover -s tests` command (2/2 tests). It set child `01` to `done`, preserved `Created`, added `Completed` and completion evidence, left the main ticket open, and reported child `02` next.

In a separate fixture, a mandatory three-test run failed (one failure). Child `02` and the main ticket stayed `ready`; their hashes did not change.

## Main closure

The first `start-task` instruction had an ambiguity: it always asked for a child when the main ticket was selected, even after all children were `done`. A focused rule was added and re-tested.

In `C:\Users\maksimbell\AppData\Local\Temp\start-task-parent-success-d0604a07d75c413abe1a2e9337f3da13`, both children were `done`, the main ticket's behavior and documentation criteria were checked, and fresh mandatory tests passed (2/2). Selecting `00-main.md` then set it to `done`, preserved `Created`, and recorded `Completed` plus evidence. In `C:\Users\maksimbell\AppData\Local\Temp\start-task-parent-failed-265f0fabb312497192e8179c479f2c91`, an integration test failed (one of three); the main ticket remained `ready`, with no `Completed` field and unchanged hash.

These are agent executions of Markdown instructions and fixture tests, not execution by a deterministic Codex skill engine. No real project source, global Codex settings, remote repository, or PR was changed.
