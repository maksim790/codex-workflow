# Adaptable templates

These are scaffolds, not mandatory output files. Omit unsupported claims and sections. Never emit literal TODO placeholders as verified facts.

## Project AGENTS.md

```markdown
# Project instructions — <project name>

## Project identity
<one or two sentences; source: ...>

## Documentation navigation
Start at [Project Knowledge Base](docs/Home.md). Replace `docs/` with the selected vault path. Before changes, read relevant module, domain, interface and ADR pages; verify assertions against code. Read only task-relevant pages.

## Architecture guardrails
<only confirmed project-specific constraints>

## Development commands
- Install: `<verified command>`
- Tests: `<verified command>`
- Lint/typecheck/build: `<verified commands>`
Clearly indicate unverified or unavailable commands.

## Verification requirements
<mandatory checks by scope and conditional checks; agreed by developer>
Do not claim checks succeeded without observed results.

## Documentation maintenance
Update affected architecture/domain/API/operation notes with behavioral changes; preserve ADR history.

## Project-specific restrictions
<confirmed constraints, security and environment boundaries>
```

## <vault>/Home.md

```markdown
# <Project> — knowledge base

**Purpose:** <verified description>

## Start here
- [Project overview](01-Project/Overview.md)
- [Architecture overview](02-Architecture/Overview.md)

## Domain and modules
- [Module name](06-Modules/Module-Name.md)

## Engineering and operations
- [Development guide](12-Development/Local-Setup.md)

## Architecture decisions
- [ADR index](11-Decisions/ADR-Index.md)

## Known gaps
<unknowns and conflicting information, with evidence>
```
Only include links to files actually created or present.

## Architecture overview

```markdown
# Architecture overview

## System boundaries
<scope, people, external services>

## Major deployables and storage
<apps, services, data stores>

## Key interactions
<runtime behaviors and links to workflows>

## Constraints and tradeoffs
<verified rules; link ADRs>

## Diagram
~~~mermaid
flowchart LR
  A[Client] --> B[Service]
~~~

## Sources
- [Repository config](../../path/to/source)
```
Include the diagram only if its contents are supported by evidence.

## Module page (`06-Modules/Name.md`)

```markdown
# Module: <Name>

## Purpose and responsibilities
...
## Boundaries and non-responsibilities
...
## Code location and entrypoints
...
## Internal architecture
...
## Dependencies
...
## Public interfaces/events
...
## Data ownership and invariants
...
## Business rules and workflows
...
## Failure behavior
...
## Testing and verification
...
## Related documentation
...
## Sources
- [Relevant source](../../path/to/source)
```

## ADR (`11-Decisions/ADR-NNNN-Title.md`)

```markdown
# ADR-NNNN: <Decision>

- Status: Proposed | Accepted | Superseded
- Date: YYYY-MM-DD
- Decision makers: <only known participants>

## Context
...
## Considered alternatives
...
## Decision
...
## Consequences
...
## Validation and review triggers
...
## Related records
...
```
Only create a historical ADR when contemporaneous evidence exists, otherwise state the current architecture without retroactive rationale.

## Project Definition of Done

```markdown
# Project verification policy

## Mandatory for every change
- <test / type / lint with real commands>

## Conditional checks
- Database schema changed -> <migration/integration checks>
- Public API changed -> <contract tests / compatibility review>
- Auth/data access changed -> <security checks>

## Unavailable or blocked checks
- <reason and risk>

## Approval
- Proposed by: Codex
- Approved by: <human, date>
```
Keep detailed strategy in `07-Engineering/Testing-Strategy.md`, and link it from AGENTS.md.
