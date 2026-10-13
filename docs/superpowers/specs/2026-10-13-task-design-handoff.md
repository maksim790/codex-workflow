# Prepared task design handoff

Status: approved in conversation on 2026-10-13. This refines the `prepare-task` and `start-task` handoff without changing the vault ticket layout.

## Responsibility

`prepare-task` resolves material requirements, product behavior, public contracts, and substantial architecture before handing a ticket to implementation. It researches the project, recommends a concrete choice, and asks the user only for decisions that cannot responsibly be made by the agent. Related blocking choices may be presented together; routine reversible technical details do not each require a question.

When creative design requires Superpowers `brainstorming`, preparation completes its design approval and planning handoff. Approved designs and plans remain separate artifacts linked from the relevant main or child ticket. A ticket records the approved decision, its scope, and the evidence of user approval; a proposed design is never treated as approved. A child may inherit a main ticket's decision only when its scope is covered. A ticket is `ready` only when its requirements and design gates needed to start are resolved. Preparation does not implement or verify application code.

`start-task` performs a focused freshness check against current instructions, linked decisions, relevant source, and tests. It reuses still-applicable approved decisions and plans without reopening the same questions or restarting design. It chooses Fast/Full and performs implementation, tests, review, and DoD checks. It asks for a new decision only when current evidence or changed scope makes a recorded decision inadequate. A legacy `ready` ticket without required approval is returned to preparation with the precise gap; status alone never proves approval.

## Verification

Check the skill structure with `quick_validate.py`, inspect the diff for conflicting instructions, and exercise a realistic ready group and a missing-approval group when agent testing is available. The latter must pause before implementation; the former must proceed without repeat design questions. Do not claim interactive agent behavior from static checks alone.
