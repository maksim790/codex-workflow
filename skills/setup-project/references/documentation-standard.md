# Project documentation standard (Obsidian-compatible)

## Philosophy

`AGENTS.md` is short operational guidance, `<vault>/Home.md` is a knowledge map, and topical Markdown pages contain durable architecture and domain knowledge. `docs/` is the default vault. Store docs with code in Git. Use normal relative Markdown links (`[Inventory](06-Modules/Inventory.md)`) so Codex, GitHub and Obsidian can navigate. Avoid WikiLinks as the only link mechanism. Use Mermaid for evidence-backed diagrams. Never store credentials or customer data.

## Twelve areas (create only evidenced pages)

| Area | Purpose | Typical pages / questions |
| --- | --- | --- |
| `01-Project` | Scope, product goals, system boundaries, glossary | Overview, goals, stakeholders, constraints, terms |
| `02-Architecture` | C4-inspired context, containers, components and runtime interactions | System-Context, Containers, Components, Runtime-Flows |
| `03-Domain` | Business concepts, invariants, state transitions, user journeys | Domain-Model, Business-Rules, Workflows/* |
| `04-Data` | Data ownership, consistency, migration strategy, retention | Data-Architecture, Data-Models, Consistency, Migrations |
| `05-Interfaces` | APIs, events, contracts, integrations and compatibility | API-Overview, Events-and-Messaging, External-Integrations |
| `06-Modules` | Detailed responsibility and boundary of each significant module | One page per module |
| `07-Engineering` | Conventions, patterns, error handling, testing, dependency policy | Coding-Conventions, Error-Handling, Testing-Strategy |
| `08-Security` | Trust boundaries, authN/authZ, secrets policy, threat assumptions | Authentication, Authorization, Data-Protection, Threats |
| `09-Infrastructure` | Environments, CI/CD, deployment, observability, runbooks | Environments, Deployment, CI-CD, Observability, Operations |
| `10-Quality` | Nonfunctional targets, reliability, performance, risk/limitations | Quality-Attributes, Performance, Reliability, Known-Risks |
| `11-Decisions` | ADR index and design decision history | ADR-Index, ADR-NNNN-Title |
| `12-Development` | Developer onboarding and operational run commands | Local-Setup, Repository-Structure, Contribution-Guide |

`<vault>/Home.md` must link to existing entry pages only; don't create empty category indexes. Domain data rules belong in `03-Domain`; database details belong in `04-Data`; individual module ownership belongs in `06-Modules`. Link across pages to avoid repetition.

## Evidence and source of truth

- Attach `Sources` links to non-obvious architecture claims using paths relative to the Markdown page; these can point back into the repository. An existing code path is evidence of implementation, not of product intent.
- OpenAPI/GraphQL schemas are authoritative for machine-readable interface details; migrations/schema are authoritative for implemented database structures; CI files and package scripts for commands. Docs explain why, boundaries, invariants and relationships.
- When docs and code disagree: report as a conflict, do not silently prefer either as business truth.
- Use statuses where useful: `Verified`, `Inferred`, `Needs confirmation`. For absent features use `Not found in inspected files`, not `Does not exist`.
- Don't fabricate ADR history or measurable SLOs.

## Minimum useful coverage

For a small project: `Home.md`, project overview and one architecture/engineering overview if evidenced. For multi-app projects: system context, container view, domain essentials, key modules, testing/deploy/navigation. Large projects may need all areas, but never empty boilerplate.

## Diagram conventions

- C4-style system context: people, external systems and trust/organizational boundary.
- Container view: independently running deployables and data stores.
- Component view: only for complex internal modules; don't diagram every class.
- Sequence: important cross-boundary request/job flows.
- State: lifecycle with real invariants.
- ER diagram: business-relevant entities and constraints, not auto-copied full database.
- Use Mermaid in fenced `mermaid` blocks. Names and arrows must match code/config evidence.

## Updating with tasks

Docs updates are required only when changes affect a documented contract, module boundary, business invariant, architecture, security assumption, deployment procedure, or meaningful runbook. Cosmetic changes should not trigger churn. An ADR records a substantial *new decision*, not every code change. Preserve historical ADRs: supersede them explicitly.

## Documentation health criteria

- `Home.md` exists and links to useful pages; links resolve.
- No empty template pages, stale placeholders, or unsupported claims presented as fact.
- Clear path from project overview to affected module and relevant decision.
- DoD gates reference executable real commands, or explicitly mark unavailable.
- Changes are reviewable in Git diffs.
