# `start-task` design

Status: **approved design implemented in `skills/start-task/`**. See `skills/start-task/tests/integration-report.md` for observed behavior and remaining test limits.

## Goal and scope

`start-task` is a reusable Codex skill that turns a concrete development request into an evidence-backed implementation and verification workflow in the active Git repository. It coordinates existing Codex and Superpowers capabilities; it does not replace them or make project-specific decisions for every repository.

The skill supports implementation, bug fixes, refactoring, and documentation changes. Repository onboarding and read-only architecture audits remain the responsibility of `setup-project`.

## Architectural choice

Three viable shapes were considered:

| Shape | Benefit | Cost |
| --- | --- | --- |
| Thin orchestrator using installed Superpowers (recommended) | One source of truth for design, planning, testing, review, and worktrees | Runtime depends on available skills; behavior can change when Superpowers updates |
| Self-contained workflow | Predictable and portable | Duplicates Superpowers and requires maintaining equivalent safeguards |
| Fixed script pipeline | Deterministic checks | Cannot reliably resolve ambiguous requirements or adapt to different repositories |

The recommended shape follows the existing decision to reuse Superpowers. The initial implementation should be instruction-only, with no project-specific command runner, new global configuration, or automatic GitHub mutation.

## Inputs and discovery

The user supplies a task and may optionally name a repository, mode (`Fast` or `Full`), constraints, and acceptance criteria. The default target is the active repository. Before choosing a mode, the agent checks Git status, relevant `AGENTS.md` files, nearby documentation, affected source and tests, and available project verification commands. It does not infer that uncommitted changes are disposable.

If project `AGENTS.md` or documentation is missing, the agent reports the gap and uses repository evidence for the current task. It may suggest `setup-project init` or `audit`, but must not silently create a vault as a side effect of task execution.

## Routing: Fast and Full

Choose the mode after initial repository inspection, before implementation:

1. If the user requests Full, use Full. If the user requests Fast, check the same risk triggers below; explain any necessary escalation.
2. Use **Full** when any trigger is present: an unresolved product decision; a public API or other consumer-facing contract change; a migration or change in data ownership; authentication, authorization, privacy, or secrets impact; concurrency or cross-process behavior; a substantial architecture or deployment change; or coordinated edits across module boundaries. A change touching several files inside one module does not by itself trigger Full.
3. Use **Fast** only when the expected behavior is clear, the affected boundary is local, the change is reversible, and no Full trigger remains after inspection. A new feature may qualify if it remains small and its design has been approved where Superpowers requires approval.
4. If the evidence is insufficient to decide, inspect the relevant code and contracts first. If material risk remains unresolved, choose Full and record why. During execution, reassess when scope changes and escalate if a Full trigger appears.

Record the chosen mode and the decisive evidence in the task contract. The mode controls planning depth, isolation and verification scope; it does not change permission or quality gates.

| Fast | Full |
| --- | --- |
| One localized area, clear expected behavior, no contract or data migration, no security or concurrency impact, and no unresolved product decision. Typical cases: a contained bug fix, text/UI adjustment, or narrow refactor. A small new feature can stay Fast only after any required design approval and only if its scope remains local. | Cross-module change, new or breaking interface or data flow, concurrency, migration, security/privacy impact, unclear requirements, significant architecture, or an implementation whose dependencies cannot be understood locally. |
| Record the task contract in the working conversation; a short design or plan still appears when an applicable Superpowers skill requires it. | Save a design and implementation plan with checkpoints when the applicable Superpowers skills require them. |
| Run focused checks and inspect the affected diff. | Decide on isolation, run relevant broader checks, and obtain independent review when available and authorized. |

The user may request either mode. The agent explains any safety-driven escalation from Fast to Full. When risk is uncertain, choose Full. A task can escalate during execution when new evidence reveals broader impact; pause only the affected implementation, preserve work already done, revise the plan, and continue independent safe work. Full mode is not automatic permission to create subagents, mutate production state, or publish.

Fast does **not** waive applicable Superpowers requirements. For example, creative feature work still uses `brainstorming` and its design approval gate; a multi-step implementation still uses `writing-plans`; code changes follow `test-driven-development` where applicable. Fast means narrow scope, concise artifacts where the invoked skill permits them, and focused verification. If a required skill's own procedure needs a larger artifact or approval, follow that procedure even in Fast. Do not claim Fast saved steps that the installed skills require.

## Task contract and Definition of Done

Before implementation, record the requested outcome, affected area, explicit constraints, acceptance criteria, chosen mode and rationale, and any unresolved assumptions. Simple criteria may be derived from the request and code. Ask the user to settle ambiguous product behavior, breaking contracts, or substantial architecture before dependent work.

The completion check has three layers:

1. **Global:** acceptance criteria met; no unrelated changes; appropriate verification and review; documentation updated when documented behavior changes; honest report.
2. **Project:** applicable checks from `AGENTS.md`, package scripts, CI, and approved project DoD. Distinguish an approved mandatory gate from a useful command discovered in the repository.
3. **Task:** concrete behavior, failure cases, compatibility, and evidence specific to the request.

If there is no project `AGENTS.md` or approved project DoD, continue with the available source and CI evidence, state `project DoD: unspecified`, and propose `setup-project` separately. This absence alone does not block task completion. A **known mandatory** check that fails or cannot run prevents a clean completion claim until fixed or explicitly accepted by the user as an exception. A discovered but unapproved check is reported as recommended or unverified; do not silently promote it to a mandatory policy. Report every applicable check as passed, failed, blocked, or not run, with the command or evidence used. Do not silently relax an agreed criterion.

## Execution and Superpowers integration

The orchestrator selects skills by their installed names and trigger conditions; it must not copy their procedures into its own `SKILL.md`.

| Need | Installed Superpowers skill |
| --- | --- |
| New behavior or meaningful design choice | `brainstorming` |
| Multi-step implementation | `writing-plans` |
| Isolated implementation | `using-git-worktrees` |
| Plan execution, when applicable | `executing-plans` or `subagent-driven-development` if the user authorized delegation |
| Code change and failing checks | `test-driven-development`, `systematic-debugging` |
| Review and evidence before completion | `requesting-code-review` when available and authorized; `receiving-code-review`; `verification-before-completion` |
| Branch completion options | `finishing-a-development-branch` |

The installed Superpowers manifest currently reports version **5.1.3**. Names and availability must be checked at invocation time, because a later install may differ. The agent preserves any stronger requirements in an invoked skill, including design approval and worktree consent. A platform-provided worktree mechanism takes precedence over manually creating one when the worktree skill requires it.

If a required Superpowers skill is unavailable, the agent reports the missing skill and stops work that depends on its required gate or procedure; it may continue independent discovery or documentation. It does not silently substitute an invented workflow. If independent review is unavailable or delegation is not authorized, the agent performs a transparent self-review, labels it as such, and marks independent review `not run`. This is a limitation, not evidence that an independent reviewer approved the change. The user decides whether that limitation is acceptable when independent review was a required project or task gate.

## Human gates and external effects

The agent requests a decision before acting on ambiguous business behavior, breaking public contracts, major architectural changes, destructive data operations, production actions, or a required exception to DoD. Existing staged/unstaged work is preserved unless its treatment is part of the user's request.

Local implementation and reversible verification follow the task authorization and the active environment's permissions. Commit, push, PR creation, merge, and deployment require explicit user authorization for that action or clear earlier authorization in the current task. The skill may prepare a reviewable diff, test report, commit message, and PR description before requesting the final external action. Superpowers branch-completion guidance presents options; it does not itself authorize a selection.

## Failure and stop conditions

On a failing test or review finding: diagnose the cause, make the smallest justified correction, and rerun affected checks. Replan when the cause invalidates assumptions. When a required decision or check is unavailable, stop only dependent work, continue independent safe work, and report the unresolved gate. Stop the repair loop when repeated attempts make no meaningful progress. There is no fixed retry count in the agreed architecture; the agent must show the blocker and avoid an indefinite loop.

## Output contract

At completion or pause, report: task and mode; files changed; acceptance criteria and DoD status; commands actually run and results; review findings and disposition; documentation changes; unresolved risks or unknowns; Git state; and the exact user action needed next, if any. Distinguish implemented behavior from proposed work and tests from agent judgment.

## Acceptance tests for the skill

| Scenario | Required observation from an agent run |
| --- | --- |
| Fast: localized UI fix in a disposable Git repository | Agent states why the change qualifies as Fast, records observable acceptance criteria, makes only the relevant change, runs focused checks, reviews the diff, and leaves publication untouched. If the request introduces new behavior, verify any required Superpowers design approval occurs before dependent writes. |
| Full: concurrency-sensitive backend change in a separate disposable Git repository | Agent chooses or escalates to Full, records the risk and acceptance criteria, follows the applicable design/plan gates, makes an isolation decision, adds a test that would catch the failure, runs relevant checks, and reports review results accurately. |
| Ambiguous breaking contract | Agent identifies the product decision, presents a concrete proposal, and makes no dependent implementation change before approval; independent safe discovery may continue. |
| Known mandatory check unavailable or failing | Agent records the exact command and failure/blocker, continues safe independent work, and does not claim full completion without a fix or approved exception. |
| No approved project DoD | Agent uses verified repository commands as evidence, reports `project DoD: unspecified`, and does not invent mandatory gates or block solely for missing onboarding. |
| Missing required Superpowers skill or independent reviewer | Agent does not invent a replacement for a required skill; if only independent review is unavailable, it labels self-review and `independent review: not run`. |
| Existing Git changes and external actions | Hashes and Git status of pre-existing user files remain stable unless the task explicitly covers them. No push, PR, merge, or deployment occurs without authorization. |

Capture the prompts, approval points, tool/action trace, resulting diff, check output, and final report for each run. Use deterministic scripts to assert file and Git invariants, but evaluate mode choice, approval order, and claims from the agent trace. Validate the skill's frontmatter and references with supported tooling. Do not use a passing static check as proof of agent behavior.

## Adopted design decisions

- A local commit requires explicit authorization for that action or clear authorization earlier in the task.
- A creative feature may remain Fast after its required Superpowers design approval when the resulting change is localized and low risk.
- A missing project DoD does not block implementation; report `project DoD: unspecified`. Only a **known mandatory** check can block a clean completion claim.
