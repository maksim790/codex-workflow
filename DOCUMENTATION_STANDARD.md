# Documentation Standard — Project `AGENTS.md` + Obsidian-compatible Vault

This is a cross-project **design standard**, not a claim that any specific repository contains all sections. Apply selectively and ground documentation in source evidence.

## Project `AGENTS.md`: seven short responsibilities

1. **Project Identity** — name, purpose, `docs/Home.md` (or actual docs location).
2. **Documentation Navigation** — where to find domain/module/ADR knowledge; read task-relevant docs, not entire vault.
3. **Architecture Guardrails** — verified, actionable module constraints and approval gates.
4. **Development Commands** — actual install/test/typecheck/lint/build commands and package scope; never fabricate.
5. **Verification Requirements** — project-specific DoD and how to report blocked checks.
6. **Documentation Maintenance** — triggers for docs and ADR updates.
7. **Project-specific Restrictions** — policies derived from project reality.

Keep global workflow rules in global Codex instructions/skills; avoid duplication. For large monorepos, add scoped `AGENTS.md` files only when necessary.

## Vault taxonomy

`docs/Home.md` is the navigation hub. Preferred categories and example subjects:

| Folder | Responsibility |
|---|---|
| `01-Project/` | product goals, scope, stakeholders, constraints, glossary |
| `02-Architecture/` | overall architecture, C4 context/container/component views, runtime flows |
| `03-Domain/` | domain model, invariants, business rules, workflows, state diagrams |
| `04-Data/` | data ownership, stores, consistency, migrations, retention |
| `05-Interfaces/` | APIs, events, messages, third-party integrations, compatibility |
| `06-Modules/` | per-module responsibilities, boundaries, code links, dependencies, error cases |
| `07-Engineering/` | coding conventions, error handling, dependency policy, testing strategy |
| `08-Security/` | authentication, authorization, threat boundaries, secrets policy, privacy |
| `09-Infrastructure/` | environments, deployment, CI/CD, observability, operational runbooks |
| `10-Quality/` | quality attributes, measurable performance/reliability goals, known risks |
| `11-Decisions/` | ADR index and dated decisions, supersession history |
| `12-Development/` | local setup, repository guide, contributing practices |

Create only files supported by evidence; don't generate empty directory trees merely to match taxonomy. Use portable relative Markdown links. Obsidian must not be required to understand the documentation.

## Module note contract

A module page should describe, when known: purpose; responsibilities; things it explicitly does *not* own; code entry points; internals; dependencies; interfaces; data ownership; domain invariants; expected errors; relevant tests; related docs/ADRs. Don't repeat literal code or entire generated API/schema files.

## Diagrams and structured sources

Prefer simple text diagrams/Mermaid for context and sequence/state flows where useful. Use C4 levels proportionally; an ERD only if necessary. Link to authoritative Prisma/SQL/OpenAPI/infra-as-code sources rather than copying their generated structures. Do not fabricate historical architectural reasoning.

## Maintenance and verification

- Docs and source changes should go together in PRs when documented behavior changes.
- Respect existing human-authored notes and historical ADR decisions; document supersession instead of rewriting history.
- Check relative links, key navigation, and claim-source consistency.
- No sensitive credentials/tokens or production data in docs.
- `audit` should produce evidence-based findings without writes.
