# Recent Task Tickets Implementation Plan

> **For agentic workers:** Use the applicable Superpowers execution and verification skills. Steps use checkbox syntax for tracking.

**Goal:** Make bare `$start-task` show five newest project vault tickets before asking the user to choose one.

**Architecture:** `prepare-task` writes a stable UTC creation timestamp into new tickets. `start-task` discovers tickets in the established vault task directory, sorts by that timestamp with an explicitly approximate fallback for legacy files, and pauses after a read-only numbered list. Explicit ticket paths and direct task descriptions retain existing behavior.

**Tech Stack:** Codex Skills Markdown, Obsidian-compatible Markdown, disposable Git fixtures.

---

### Task 1: Baseline

**Files:** Existing `skills/start-task/SKILL.md`; disposable fixture only.

- [x] Create seven dated tickets in a temporary Git repository with an existing vault.
- [x] Invoke bare `$start-task` under the current instructions and record that no list is offered.

### Task 2: Skill changes

**Files:** Modify `skills/prepare-task/SKILL.md`, `skills/start-task/SKILL.md`, `skills/start-task/README.md` and the relevant design docs.

- [x] Add `Created: YYYY-MM-DDTHH:MM:SSZ` to new tickets without changing it on ticket updates.
- [x] Add a no-argument discovery branch before task execution: find the vault, rank tickets, display at most five, and wait for selection without writing.
- [x] Keep explicit path and direct request routes intact.

### Task 3: Verify and report

**Files:** Update `skills/prepare-task/tests/integration-report.md` or add a focused report if behavior warrants one; update roadmap as needed.

- [x] Run a skill-enabled agent scenario with more than five tickets, including same-day timestamps and a legacy ticket.
- [x] Verify displayed order, paths, status, read-only Git state, and selection behavior; report agent evidence separately from deterministic checks.
- [x] Run skill format validation and diff checks; do not commit or publish.
