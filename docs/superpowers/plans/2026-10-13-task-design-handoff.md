# Prepared Task Design Handoff Implementation Plan

> **For agentic workers:** Apply the design in `docs/superpowers/specs/2026-10-13-task-design-handoff.md` and verify each changed skill before completion.

**Goal:** Move material design decisions into preparation and prevent repeated questions at task start.

**Architecture:** Keep the existing vault and ticket status model. Record approval and scope in tickets with links to separate design and plan artifacts; use a focused freshness check when execution begins.

**Tech Stack:** Markdown Codex skills and project documentation.

---

### Task 1: Preparation contract

- [x] Update `skills/prepare-task/SKILL.md` so `ready` requires resolved blocking requirements and applicable design approval.
- [x] Require approval evidence and scope, with shared decisions linked from child tickets.
- [x] Move material design discussion and the invoked Superpowers design/planning handoff into preparation while preserving implementation boundaries.

### Task 2: Execution handoff

- [x] Update `skills/start-task/SKILL.md` to reuse recorded decisions and applicable plans after a focused freshness check.
- [x] Route missing approval or new blocking contradictions back to preparation without repeating the full interview.
- [x] Preserve Fast/Full, implementation, verification, and DoD gates.

### Task 3: Verify

- [x] Update user-facing documentation and record test limitations.
- [x] Run skill validators and `git diff --check`; inspect the final diff.
