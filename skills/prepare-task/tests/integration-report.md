# `prepare-task` integration evidence — 2026-10-13

## Scope and limits

All project fixtures were disposable Git repositories under the system temporary directory. The real `codex-workflow` repository was not used as a target project. Agent behavior and script results are distinguished below. The full action traces were not archived, so this is a concise evidence report rather than a replayable transcript.

## Baseline without `prepare-task`

A separate agent created a small Python records API, `AGENTS.md`, and an Obsidian-compatible vault, then prepared a CSV export ticket without the new skill. It wrote `docs/tasks/CSV export endpoint.md` and a Home link. It treated active-only export as a provisional default even though the user's archive policy was undecided. A second read-only baseline of the pre-change `start-task` instructions found no explicit requirement to read an exact ticket path or distinguish its provisional criteria from approved ones.

## Skill-enabled agent runs

| Scenario | Observed result |
| --- | --- |
| Prepare CSV export ticket in a fresh vault | Agent created one ticket at `docs/12-Development/Tasks/records-csv-export.md`, status `needs-decision`. It linked source, architecture and project instructions; recorded archive inclusion and public route as open questions; did not implement application code. |
| Hand the explicit path to `start-task` | Agent read that exact ticket, compared it with current code and vault, chose Full because a public contract and product rule were unresolved, and made no implementation change. |

Fixture repository: `C:\Users\maksimbell\AppData\Local\Temp\prepare-task-forward-a480e5bcb3064df6b0778baa94a17be1`. Ticket SHA-256 after preparation: `E353461723CD934029242A7CB38093AC4FF51092BF6BE45D3358C05BEB83EA6E`. Its Git status was `?? docs/12-Development/` before and after the handoff. Parent independently checked the hash, Git status, and ran `setup-project/scripts/validate-docs.py` against the fixture: **0 errors, 0 warnings**. This validator checks links/navigation, not the semantic quality of acceptance criteria.

The preparation agent surfaced one gap: the instructions did not explicitly say to record every known open question while asking them one at a time. That sentence was added to `SKILL.md` after the run. No second full agent preparation run was made for that wording change.

## Direct edge-case checks

Another agent applied the current instructions in separate disposable fixtures. The intended ticket path already existed in one: it stopped and asked whether to update or choose another name. The existing file's SHA-256 stayed `153D8FFB40D2FD77AC5BF82230F46B0B6B94790B9B7468C52EF04A2BB000143C`, Git status stayed unchanged, and no duplicate ticket appeared. In a fixture without a discoverable vault, it requested the vault path or suggested `$setup-project init`; no `docs` tree appeared and Git status stayed unchanged. A nested Codex CLI attempt for these edge cases was blocked by file-access policy, so these are direct instruction checks, **not** completed independent CLI agent runs.

## Format and installation checks

- `skill-creator/scripts/quick_validate.py` reported `Skill is valid!` for both `prepare-task` and the modified `start-task`. The global Python environment lacked PyYAML; the successful validation used an existing local copy via process-local `PYTHONPATH`, without changing global packages.
- `git diff --check` passed for tracked changes. The new untracked skill and spec files were inspected separately.
- A local junction at `C:\Users\maksimbell\.agents\skills\prepare-task` points to this repository's skill. A fresh ephemeral, read-only Codex CLI session reported `prepare-task` discoverable at that path. No global Codex config was edited.

## Remaining limits

No test has followed a `ready` ticket through complete implementation and DoD, or exercised every kind of stale ticket and vault path. The current evidence supports ticket creation, the ambiguous handoff gate, collision avoidance by direct instruction check, link validity in one fixture, and discovery. Pilot the two-step workflow on a real, low-risk task before treating all repository shapes as covered.
