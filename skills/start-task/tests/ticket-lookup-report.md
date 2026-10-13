# Ticket reference lookup — 2026-10-13

## Baseline

An agent inspected the previous `start-task` instructions against a disposable Git project with `AGENTS.md`, a vault, and `Tasks/api/records-csv-export.md`. The short name `records-csv-export` followed the direct-request route. `api/records-csv-export.md` could not resolve without the vault prefix. This was a reading of the instructions in a fixture, not an installed-skill invocation.

## Updated skill: agent exercise

A separate agent followed the updated instructions in a disposable Git repository. It reported:

| Input or condition | Observed route |
| --- | --- |
| `api/records-csv-export.md` | Selected the ticket under the project's Tasks directory. |
| Explicit repository-relative full path | Selected the same ticket. |
| `records-csv-export` with duplicate filenames in separate subdirectories | Listed both candidates and waited for a choice. |
| `records-csv-expor` | Reported ticket not found, suggested nearby names, and waited. |
| `../outside/secret.md` | Rejected traversal. |
| `linked/secret.md` through a junction outside Tasks | Rejected the escaped path. |
| Clear imperative request for new work | Used the direct-request route. |

The agent reported unchanged ticket hashes and unchanged `git status --short` before and after the read-only lookup. It did not implement any fixture task or edit this repository's skill files.

## Validation and limits

`quick_validate.py` accepted both `start-task` and `prepare-task` skill structure. `git diff --check` passed. The exercise checked how an agent applies the Markdown instructions; it did not test editor autocomplete, skill discovery, or a built-in ticket resolver. Distinguishing a short ticket title from a direct natural-language request remains a semantic judgment. Suggestions never select a ticket automatically.
