# start-task

Reusable Codex skill for development tasks in an existing Git repository. It chooses Fast or Full from repository evidence, records acceptance criteria, coordinates installed Superpowers skills, and reports verification against global, project, and task DoD.

## Install and use

Copy or link this directory to a Codex-discoverable skills location such as `~/.agents/skills/start-task/`, then refresh skill discovery if necessary. Invoke in the target repository's Codex chat:

```text
Use $start-task to show the five newest tickets in this project's vault.
Use $start-task to fix the reported bug in this repository.
Use $start-task Full to change the public API and its consumers.
$start-task export-records
$start-task api/export-records.md
$start-task notifications-service
$start-task notifications-service/01-event-contract.md
```

Bare `$start-task` lists up to five recent open standalone tickets or task groups and waits for the user's selection. A ticket can be specified by title, filename, group name, or a path relative to the project's Tasks directory; an explicit repository path also works. Ambiguous matches require selection, and missing references show suggestions without starting work. The user may request Fast or Full for a concrete task, but the skill escalates Fast when repository evidence reveals Full risk. For the two-step workflow, `$prepare-task` first creates tickets in the project's existing vault; `start-task` then rechecks the named or selected ticket against current source before implementation. Clearly phrased direct task requests remain supported. `setup-project` remains responsible for first-time documentation setup and read-only audits. The skill does not perform external publication merely because implementation is complete.

Selecting a task group starts the first open child in its main ticket's current order without asking the user to choose a child. Each invocation handles one child; unmet decisions or dependencies still pause its implementation. `00-main.md` is never an implementation task, even when named directly. After all children are done, selecting the group performs only the final integration verification.

After verified local completion, `start-task` marks the selected ticket `done` and records completion evidence. A grouped main ticket closes only after required children and its integration criteria are verified.

Design: [`docs/superpowers/specs/2026-10-13-start-task-design.md`](../../docs/superpowers/specs/2026-10-13-start-task-design.md).
