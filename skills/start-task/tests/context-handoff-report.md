# Bare start-task conversation handoff (2026-10-13)

## Baseline and change

The user's live observation and the earlier [recent-ticket report](recent-ticket-report.md) show the old bare `$start-task` rule: it always listed the newest open tickets, including unrelated `ready` tickets. The new rule first uses an unambiguous, still-current `prepare-task` handoff from this conversation and active repository. When none exists, it lists unfinished tickets and waits for selection.

## Agent forward checks

Agents applied the revised skill to disposable Git fixtures under the Windows temporary directory. These were instruction-driven routing checks, not Codex UI dispatch or application implementation.

| Context | Observed route |
| --- | --- |
| Current-conversation handoff names a ready group; newer unrelated ready tickets exist | Selected that group and its first open child `01-contract.md`, without showing the unrelated tickets or asking for a child choice |
| No handoff in this conversation, or handoff exists only in another chat/repository | Listed unfinished tickets by `Created` and waited for selection; excluded `done` |
| Current-conversation handoff names `draft` or `needs-decision` | Kept that ticket selected and paused at its gate, without switching to another ready ticket |
| User selected another task after preparation, or the prepared ticket is already `done` | Did not auto-start the old handoff; listed unfinished tickets and waited for selection |

The first fixture's seven SHA-256 file hashes and Git status matched before and after. In the fallback fixture, four ticket hashes and Git status also matched. The handoff context was supplied as a test scenario; a real sequential invocation of `prepare-task` followed by bare `start-task` was not run. File timestamps alone are not treated as conversation context.
