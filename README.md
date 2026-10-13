# Codex workflow

This repository holds reusable Codex skills and their development context:

- `skills/setup-project/` — project onboarding, documentation update, read-only audit, and approved repair (`doctor` or `doctor tasks`).
- `skills/prepare-task/` — evidence-backed task tickets in an existing project vault, including decomposition of large requests.
- `skills/start-task/` — Fast/Full task routing, acceptance criteria, Superpowers coordination, and evidence-backed completion.
- `PROJECT_CONTEXT.md` — project goals, architectural decisions, and evidence limits.
- `DOCUMENTATION_STANDARD.md` — project `AGENTS.md` and Obsidian-compatible documentation standard.
- `NEXT_STEPS.md` — current roadmap.

The preferred task handoff is `$prepare-task <request>` in the target repository, followed by bare `$start-task` to choose from recent open tickets or task groups, or `$start-task <ticket-name-or-Tasks-relative-path>` to open one directly. Preparation resolves material requirements and design decisions and links approved design artifacts when needed. `start-task` reuses those decisions after checking current evidence. Large tasks use `Tasks/<task>/00-main.md` and numbered child tickets. `$start-task <task-folder>` starts the first open child in the main ticket's current order without a child-selection prompt; `00-main.md` coordinates the group and is never an implementation task. Verified local completion marks a child `done`; after all children are done, a separate group invocation verifies the overall integration criteria. Direct `$start-task <request>` remains supported when the request clearly asks for new work. Context files are secondary to current source and test evidence; `start-task` requires installed Superpowers for procedures that apply to a task.
