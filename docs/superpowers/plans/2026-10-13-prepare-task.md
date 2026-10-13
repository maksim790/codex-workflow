# Prepare Task Implementation Plan

> **For agentic workers:** Use applicable Superpowers execution and verification skills. Steps use checkbox syntax for tracking.

**Goal:** Add a reusable `prepare-task` skill that writes an evidence-backed task ticket into a setup-project vault and teach `start-task` to consume an explicit ticket path.

**Architecture:** An instruction-only skill owns ticket preparation and Markdown structure. `start-task` remains the executor and performs a fresh evidence check at handoff. No global configuration or generated project code is required.

**Tech Stack:** Codex Skills Markdown, Markdown vault, Python standard library for optional fixture assertions.

---

### Task 1: Establish baseline and ticket contract

**Files:** Create `skills/prepare-task/SKILL.md`; optionally create a focused ticket-format reference only if the entrypoint becomes unwieldy.

- [x] Run a realistic temporary-repository baseline without the new skill and record observed gaps.
- [x] Write `SKILL.md` with frontmatter, vault discovery, evidence rules, ticket fields, ambiguity handling, file safety, and handoff output.
- [x] Validate frontmatter and links with available skill validation tooling.

### Task 2: Connect `start-task`

**Files:** Modify `skills/start-task/SKILL.md` and `skills/start-task/README.md`.

- [x] Baseline the requested ticket-path behavior before editing.
- [x] Add exact-path ticket loading and current-evidence/status checks without changing direct-task routing.
- [x] Verify no contradiction with Fast/Full and DoD rules.

### Task 3: Exercise the workflow

**Files:** Create `skills/prepare-task/tests/integration-report.md` only if needed to retain meaningful evidence; update `README.md`, `PROJECT_CONTEXT.md`, and `NEXT_STEPS.md` for current state.

- [x] Run skill-enabled preparation in a disposable Git repository with an existing vault.
- [x] Inspect ticket content and Git state; check ambiguous and existing-file behavior.
- [x] Run a ticket-path handoff scenario and inspect `start-task` decisions.
- [x] Report which claims come from agent behavior versus script or static checks, and leave publication untouched.
