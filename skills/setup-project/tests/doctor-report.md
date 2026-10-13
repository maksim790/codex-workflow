# `setup-project doctor` agent exercises — 2026-10-13

## Baseline

In disposable Git repository `C:\Users\maksimbell\AppData\Local\Temp\setup-project-doctor-baseline-2b4a75007f6a49e78de8c3e52391018b`, an agent read the previous skill. It found no `doctor` or `doctor tasks` mode and made no repair. A separate read-only validator call found one broken Home link, but no flat-task-group finding. Git status remained clean and all eight tracked file hashes matched before and after.

## General doctor

An agent created disposable repository `C:\Users\maksimbell\AppData\Local\Temp\setup-project-doctor-general-8370744e6e6b45c6839e8064f3e0252e`. First invocation ran the read-only validator and proposed one exact change in `docs/Home.md`: replace a broken link to `02-Architecture/Old-Overview.md` with a verified existing `02-Architecture/Overview.md`. No file or Git status changed before the separate simulated fixture approval. After that approval, it applied only the link edit; validator output changed from one error to **0 errors, 0 warnings**. The architecture page with an ambiguous SQLite statement and a ticket marked `done` remained byte-identical. Git status showed only ` M docs/Home.md`.

## Tasks doctor

In disposable repository `C:\Users\maksimbell\AppData\Local\Temp\doctor-tasks-forward-070b746f72ee4bf5873b60db7666bfd7`, an agent found a linked flat parent and two children with explicit order and dependency. Its first invocation proposed three moves into `Tasks/export-records/{00-main,01-export-contract,02-export-endpoint}.md` and eleven link-target rewrites in moved tickets and inbound Markdown. All 13 file hashes and clean Git status stayed unchanged before the separate simulated fixture approval.

After that approval, the agent made only those moves and link edits. It checked all 15 relative Markdown links in the fixture; all resolved. The bundled validator reported **0 errors, 0 warnings**. The main ticket retained `ready` and `Created`; the completed child retained `done`, `Created`, `Completed`, and completion evidence; the other child retained `ready` and `Created`. An unrelated completion-looking ticket remained `ready` with an unchanged hash. ADR and human-note prose was preserved, with only necessary link targets changed. Git status showed the three old paths deleted, the new group directory untracked, and five inbound Markdown files modified; no changes were staged.

In a separate edge fixture at `C:\Users\maksimbell\AppData\Local\Temp\doctor-tasks-edge-058eac5baecc4a678f76b8f580716ced`, similarly named flat files had no parent/child links or established order, and the likely group path already existed for another effort. The agent declined to propose a migration or status change. All six file hashes and clean Git status stayed unchanged.

An additional baseline in `C:\Users\MAKSIM~1\AppData\Local\Temp\setup-doctor-baseline-6c75881aba0a4208a2299b781c005a55` found that the first doctor wording repaired a broken link but did not clearly number children already inside a group folder. The skill was narrowed to cover this case when `00-main.md` gives explicit order. The agent then proposed two renames and link rewrites without changing any file before simulated fixture approval. After approval, it moved `define-api.md` to `01-define-api.md` and `implement-service.md` to `02-implement-service.md`, repaired the main/child links and a broken architecture link, and re-ran validation: **1 error before, 0 errors and 0 warnings after**. A byte comparison confirmed that ticket bodies differed only by those link targets; status, dates, completion evidence, criteria, and notes were preserved. Git status showed modified main, deleted old child paths, and untracked numbered child paths; nothing was staged.

The migration fixture's CRLF rewritten lines caused plain `git diff --check` to flag trailing whitespace under its Git configuration. `git -c core.whitespace=cr-at-eol diff --check` passed; this is a fixture whitespace caveat, not evidence of a semantic repair defect.

## Limits

These were agent executions of Markdown instructions in temporary projects, with a separately simulated approval for each repair. They do not prove an executable migration engine or automatic Codex mode parser. The validator checks Markdown navigation, not ticket grouping, order, dependencies, or semantic correctness; those were checked by the agent and fixture assertions. No application code, global Codex settings, commit, push, or PR was changed.
