# Setup Project Doctor Implementation Plan

> **For agentic workers:** Use `superpowers:writing-skills` to baseline and forward-test the skill change. Steps use checkbox syntax. Keep fixtures outside the real repository and do not commit or publish without user authorization.

**Goal:** Add `doctor` and `doctor tasks` repair modes to `setup-project` while preserving task statuses and the approval gate.

**Architecture:** The skill remains an instruction-driven workflow. Doctor first inspects and validates, prepares exact file moves and edits, waits for approval, then applies only that scope and verifies it. No new script is needed because safe group discovery and semantic ambiguity require agent judgment.

**Tech Stack:** Codex Skills Markdown, existing read-only Python validator, disposable Git fixtures.

---

### Task 1: Baseline

**Files:** Existing `skills/setup-project/SKILL.md`; temporary Git fixture.

- [x] Exercise unsupported `doctor` and `doctor tasks` invocations and record read-only outcomes.

### Task 2: Skill and documentation

**Files:** `skills/setup-project/SKILL.md`, `skills/setup-project/README.md`, `README.md`, `PROJECT_CONTEXT.md`, `NEXT_STEPS.md`.

- [x] Add command routing and approval-scoped repair procedure.
- [x] Add Tasks migration and link repair rules while preserving all status and completion metadata.
- [x] State boundaries between doctor, update, and audit without changing existing modes.

### Task 3: Forward exercises

**Files:** Disposable Git fixtures; `skills/setup-project/tests/doctor-report.md`.

- [x] Verify proposal-only invocation leaves hashes and Git status unchanged.
- [x] With simulated explicit approval, migrate a linked flat group, fix references, preserve statuses and notes, and validate links.
- [x] Verify ambiguous groups and completion-looking `ready` tickets are not silently changed.
- [x] Verify general doctor can propose and repair one unambiguous navigation/link issue without semantic rewrite.

### Task 4: Final checks

**Files:** Updated skill and report.

- [x] Run skill format validation, existing validator tests if affected, `git diff --check`, and inspect Git status.
