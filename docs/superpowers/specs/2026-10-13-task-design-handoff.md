# Prepared task design handoff

Status: approved in conversation on 2026-10-13. This refines the `prepare-task` and `start-task` handoff without changing the vault ticket layout.

## Responsibility

`prepare-task` resolves material requirements, product behavior, public contracts, and substantial architecture before handing a ticket to implementation. It researches the project, recommends a concrete choice, and asks the user only for decisions that cannot responsibly be made by the agent. Related blocking choices may be presented together; routine reversible technical details do not each require a question.

When creative design requires Superpowers `brainstorming`, preparation completes its design approval. When `writing-plans` applies, preparation writes a separate implementation plan and obtains user approval before the ticket is handed to execution. Approved designs and plans remain separate artifacts linked from the relevant main or child ticket. A ticket records the reviewed artifact, its scope or revision, and the user's approval; a proposed or merely saved artifact is not approval. A child may inherit a main ticket's approval only when its scope is covered. A ticket is `ready` only when its requirements and required design and plan gates are resolved. Preparation does not implement or verify application code.

Once those decisions and any required plan are prepared, preparation presents one concise “Что будет сделано” summary of the intended outcome in no more than five bullets and links the full plan for review. The user can correct global omissions or the plan before the new or explicitly re-prepared ticket becomes `ready`. Preparation records acceptance of the scope and plan revision and applies corrections to affected tickets; no reply leaves the ticket in `draft`. This final review does not replace a required design approval or turn plan approval into authorization to implement. Existing `ready` tickets are not automatically downgraded solely because they predate this review step; `start-task` still checks for required approval before execution.

`start-task` performs a focused freshness check against current instructions, linked decisions and plan, relevant source, and tests. It reuses still-applicable approved decisions and plan without asking for plan approval again. It chooses Fast/Full and performs implementation, tests, review, and DoD checks. Routine implementation choices within the approved scope do not require a new plan approval. Material drift or a legacy `ready` ticket without required approval returns to preparation with the precise gap; status alone never proves approval. A direct task request without a prepared ticket still follows applicable Superpowers planning gates during `start-task`.

## Verification

Check the skill structure with `quick_validate.py`, inspect the diff for conflicting instructions, and exercise a realistic ready group and a missing-approval group when agent testing is available. The latter must pause before implementation; the former must proceed without repeat design questions. Do not claim interactive agent behavior from static checks alone.
