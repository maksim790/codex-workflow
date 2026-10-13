# Start Task Implementation Plan

> **For agentic workers:** Use the approved design in `docs/superpowers/specs/2026-10-13-start-task-design.md`. Execute tasks in order and verify each before continuing.

**Goal:** Add a reusable `start-task` Codex skill that selects Fast/Full from repository evidence and coordinates installed Superpowers without weakening its gates.

**Architecture:** Keep `skills/start-task/SKILL.md` concise and instruction-only. Put mode and reporting details in one referenced document only if the entrypoint becomes unwieldy. Preserve `setup-project` as the onboarding/audit skill.

**Tech Stack:** Markdown skill files, Git, Python standard-library checks, disposable Git repositories, available agent execution tools.

---

### Task 1: Record baseline scenarios

**Files:** Temporary fixtures outside the repository; `skills/start-task/tests/` if a reusable check is justified.

- [x] Create a localized Fast task, a concurrency-sensitive Full task, and an unavailable-check gate task in separate disposable Git repositories.
- [x] Run the agent without `start-task` and record observable mode/risk, verification, and Git behavior. Complete action traces were not exported; see the integration report.
- [x] Identify the smallest missing decisions the skill must teach.

### Task 2: Add the skill

**Files:** Create `skills/start-task/SKILL.md`, `skills/start-task/README.md` only if installation guidance is needed.

- [x] Write frontmatter with `name: start-task` and a discriminating description.
- [x] Route Fast/Full using the design's ordered risk rules, recording mode and evidence.
- [x] State the task contract, three DoD layers, mandatory-check behavior, Superpowers routing, approval gates, failure loop, and output contract without copying other skills' procedures.
- [x] Ensure the skill does not authorize subagents, GitHub actions, or production operations by itself.

### Task 3: Validate metadata and behavior

**Files:** Add narrow reusable tests under `skills/start-task/tests/` only for objective invariants; keep agent traces in ignored temporary fixtures.

- [x] Run `skill-creator` quick validation with process-local PyYAML; it reported `Skill is valid!`.
- [x] Run Fast, Full, and gate scenarios with the skill explicitly invoked; inspect agent reports, resulting diffs, and parent verification output. Full traces were not archived.
- [x] Verify fixture Git changes, absence of unapproved external actions in agent reports, and honest blocked mandatory-check reporting.
- [x] Correct independent review findings and run the affected contract-gate scenario.

### Task 4: Reconcile repository documentation

**Files:** Update `README.md`, `NEXT_STEPS.md`, `PROJECT_CONTEXT.md`, and the approved design if implementation reveals a genuine mismatch.

- [x] Document installation and the evidence level of tests without claiming script checks prove agent behavior.
- [x] Run `git diff --cached --check` and inspect the complete diff and Git status.
- [x] Leave changes local and reviewable; do not push or create a PR without user authorization.
