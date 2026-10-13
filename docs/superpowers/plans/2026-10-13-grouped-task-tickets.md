# Grouped Task Tickets Implementation Plan

> **For agentic workers:** Apply `superpowers:writing-skills` to each skill edit. Steps use checkbox syntax for tracking. Keep all evaluation artifacts in disposable Git fixtures; do not commit or publish without user authorization.

**Goal:** Store a large task and ordered children in one Tasks subdirectory and close verified tickets with evidence.

**Architecture:** `prepare-task` creates `Tasks/<task-slug>/00-main.md` and numbered children when boundaries are settled. `start-task` groups the picker, resolves tickets as before, and writes `done` with completion evidence only after applicable DoD gates pass. Existing flat tickets remain valid.

**Tech Stack:** Codex Skills Markdown, Obsidian-compatible Markdown, disposable Git repositories, skill format validation.

---

### Task 1: Observe baseline

**Files:** Existing `skills/prepare-task/SKILL.md`, `skills/start-task/SKILL.md`; disposable fixture.

- [x] Run an agent scenario for a large agreed request and inspect ticket layout.
- [x] Check whether verified execution currently closes a child or parent ticket.

### Task 2: Define grouped tickets

**Files:** `skills/prepare-task/SKILL.md`, `docs/superpowers/specs/2026-10-13-prepare-task-decomposition-design.md`.

- [x] Specify new group path, `00-main.md`, two-digit child prefixes, current order in the main ticket, and dependencies as the execution gate.
- [x] Preserve single-ticket requests and existing flat tickets; prohibit silent migration or overwrites.
- [x] Forward-test undecided and agreed large requests in disposable repositories and inspect links and unchanged existing files.

### Task 3: Select and close tickets

**Files:** `skills/start-task/SKILL.md`, `skills/start-task/README.md`.

- [x] Make bare selection list recent active task groups or standalone tickets, with a drill-down to children.
- [x] Define `done` and completion evidence after acceptance criteria and mandatory checks; leave blocked tickets open.
- [x] Close the main ticket only after required children and integration criteria pass; forward-test selection and closing decisions without modifying real project code.

### Task 4: Verify and document

**Files:** `skills/prepare-task/tests/grouped-ticket-report.md`, `README.md`, `PROJECT_CONTEXT.md`, `NEXT_STEPS.md`.

- [x] Record agent behavior separately from format and link checks.
- [x] Run `quick_validate.py` for both skills and `git diff --check`; inspect final Git status.
