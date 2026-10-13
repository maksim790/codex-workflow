# Bare `$start-task` ticket listing — 2026-10-13

This records the earlier unconditional-list behavior. The current skill first checks for a usable handoff from `prepare-task` in the same conversation; see [context handoff check](context-handoff-report.md).

## Baseline

In a disposable Git repository with `AGENTS.md`, `docs/Home.md`, and seven task tickets, the pre-change `start-task` instructions did not list tickets for a bare invocation. The agent asked for a task description or exact ticket path. No fixture files changed during the invocation.

## Skill-enabled agent behavior

The updated skill was exercised in the same disposable repository with seven tickets in `docs/12-Development/Tasks`. Six tickets carried valid `Created` UTC timestamps, including two on the same day; one legacy ticket lacked `Created` and had an older modification time. Bare `$start-task` showed the list **before asking for input**:

1. `golf.md` — ready — `2026-10-12T17:00:00Z`
2. `foxtrot.md` — ready — `2026-10-12T09:00:00Z`
3. `echo.md` — ready — `2026-10-11T08:00:00Z`
4. `delta.md` — ready — `2026-10-09T08:00:00Z`
5. `charlie.md` — ready — `2026-10-07T08:00:00Z`

Each displayed entry also included its fixture goal and repository-relative ticket path. Git status remained `?? AGENTS.md` and `?? docs/`, and all seven ticket SHA-256 hashes matched the pre-list snapshot. Selecting `1` opened the exact `golf.md` ticket. Its deliberately vague fixture goal and missing acceptance criteria caused Full routing and a requirements decision gate; no implementation followed. This was agent behavior, not a completed end-to-end task execution.

In a targeted follow-up, the legacy `alpha.md` ticket's file modification time was set later than the explicit `Created` values without changing its contents. Bare `$start-task` then showed exactly five entries: `alpha.md` first with **approximately 2026-10-13T18:00:00Z (file modification time)**, followed by golf, foxtrot, echo, and delta. Git status and all seven ticket hashes stayed unchanged during listing. This exercises the labeled fallback, while also illustrating that modification time is only an approximation of creation order.

Separately, an agent used the updated `prepare-task` instructions in another disposable Git repository. It created one ticket with `Created: 2026-10-13T11:54:40Z` and `Status: ready`. The timestamp parsed as UTC with seconds; relative links resolved; tracked project files stayed unchanged. Preserving `Created` on a later ticket update was not exercised.

## Format and limits

`skill-creator/scripts/quick_validate.py` returned `Skill is valid!` for both modified skills using a process-local PyYAML copy. `git diff --check` passed. The tests above were direct agent instruction runs in disposable repositories; full action traces were not archived. They show list ordering, no-input display, read-only behavior, and selected-ticket handoff. They do not prove behavior in every vault layout or complete implementation after ticket selection.
