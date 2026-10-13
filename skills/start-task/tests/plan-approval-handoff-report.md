# Plan approval handoff check (2026-10-14)

## Baseline

The pre-change skill text did not require `prepare-task` to record user approval of a written implementation plan before marking a ticket `ready`. `start-task` could create or revise a plan when the linked one was missing or unsuitable. This baseline was established by reading `git show HEAD` instructions in a disposable Git fixture; it was an instruction-level test, not a full agent execution.

## Agent forward checks

Agents applied the revised skills in disposable Git repositories, without touching the workflow repository or global Codex settings:

| Case | Observed behavior |
| --- | --- |
| Group with simulated user approval of exact plan v1 and final scope review | Bare/group handoff selected child `01` without asking whether the plan was acceptable again. The agent followed TDD: one expected failing test before the change, then `python -m unittest discover -s tests` passed 2/2. It marked only child `01` `done` with completion evidence; `00-main.md` and child `02` hashes stayed unchanged. `git diff --check` passed. |
| `ready` group with merely linked, unapproved plan | The agent identified the missing plan and scope approval, returned to `prepare-task`, and made no file changes. Git status and SHA-256 snapshots remained unchanged. |
| Material drift from approved local-file plan to remote-only code and architecture | The agent identified the conflict and returned the affected scope to preparation, without substituting a new plan or asking for repeat approval at `start-task`. All 10 fixture hashes and Git status stayed unchanged. |
| Direct multi-step request without a prepared ticket; routine tactical choice inside approved scope | The direct request retained normal `writing-plans` routing. The tactical choice proceeded without a new approval question. These were read-only routing checks. |

The preparation and user approvals in these fixtures were **simulated**. The tests show agent interpretation and one concrete child implementation, not a real multi-turn Codex UI run of `prepare-task` followed by `start-task`. `quick_validate.py` and `git diff --check` verify format and diff hygiene, not conversational behavior.
