# Prepared design handoff check (2026-10-13)

## Observed problem and change

The user reported that starting a large prepared task led to many more questions and a long design phase. The prior skill text allowed `prepare-task` to mark a ticket `ready` without design approval, while `start-task` still invoked the applicable Superpowers design gate. This was a rule-level handoff gap; the particular live project ticket and the agent's questions were not available for inspection here.

The revised instructions make preparation resolve material product and architecture choices, record approval and scope, and link separate design and plan artifacts when applicable. `start-task` performs a focused freshness check, reuses valid recorded decisions, and asks only about new blocking contradictions. An unsupported legacy `ready` ticket returns to preparation before dependent implementation.

## Checks performed

- Reviewed the current `prepare-task` and `start-task` skill text and related design docs for the contradictory `ready` and design approval rules.
- Ran `quick_validate.py` on both edited skills; both reported `Skill is valid!`.
- Ran `git diff --check` and checked the final changed-file list before commit.

Two disposable-repository agent scenarios were attempted for the old handoff, but both agents stopped with a service usage-limit error before returning observations. No RED or GREEN agent behavior result is claimed. Structural validation cannot establish that a future Codex session will ask fewer questions. A realistic prepared-ticket execution remains to be tested when agent execution is available.
