# `start-task` integration exercise — 2026-10-13

Three disposable Git repositories were created with `integration_fixtures.py` under the Windows temporary directory. Three agents handled the tasks without `start-task`; three fresh agents then handled equivalent tasks after reading `skills/start-task/SKILL.md` explicitly. These were real agent runs, but complete tool traces were not exported into this repository. The statements below distinguish agent reports from commands independently rerun by the parent agent.

| Scenario | Baseline without skill | With skill |
| --- | --- | --- |
| Fast UI copy | Agent corrected `Savee` to `Save`, but did not run the project-mandated unittest command. | Agent chose Fast, stated a concrete criterion, observed the existing test fail before the edit, corrected the label, ran the mandated test, and reported one passing test. |
| Full concurrent counter | Agent fixed the race and added a reproducing test, but did not explicitly report Fast/Full routing. | Agent chose Full despite the prompt's suggestion to skip tests, because concurrent access is a Full trigger. It reported a red test (`15 != 0`), then a lock-protected fix, two passing tests, and preservation of the return contract. |
| Unavailable project gate | Baseline agent correctly reported that a missing mandatory test directory prevented full readiness. | Agent chose Fast for the localized bug fix, added tests and fixed behavior, but reported the mandatory `missing-tests` check as blocked and did not claim full DoD completion. |

Independent parent verification in the skill-enabled fixtures:

- `fast`: `python -m unittest discover -s tests` — 1 test, OK; `git diff --check` — exit 0; only `index.html` had a tracked change before parent verification.
- `full`: `python -m unittest discover -s tests` — 2 tests, OK; `git diff --check` — exit 0; tracked changes were `counter.py` and `tests/test_counter.py`; `notes.md` stayed unchanged. The added test uses concurrent threads and a slow subtraction to expose lost updates.
- `gate`: `python -m unittest discover` — 2 tests, OK; `python -m unittest discover -s missing-tests` — exit 1 with `ImportError: Start directory is not importable`; `git diff --check` — exit 0. The new `test_app.py` was untracked in the disposable repo.
- Parent verification without `-B` generated Python `__pycache__` directories in temporary fixtures. The reusable fixture generator now includes `.gitignore` rules for these caches; the earlier fixture status snapshots should be interpreted with that limitation.
- Agents made no commits or GitHub changes in these runs. The parent inspected the resulting diffs and status; the complete action traces and approval ordering were not independently archived.

Two additional disposable `contract` repositories tested a public API change. In the first prompt, the user explicitly delegated choosing the v2 shape; the agent chose `{"items": [...]}`, preserved the v1 list by default, added tests, and reported that no HTTP router existed to expose version selection. This is evidence of delegated design choice, not a test of the approval gate. In the second prompt, the shape and compatibility policy were left unresolved without delegation. The agent selected Full, named both missing decisions, made no changes, and stopped dependent implementation. Parent verification found clean Git status, no diff, and only the baseline commit in that fixture.

The exercise supports Fast/Full routing, project test selection, honest blocked-gate reporting, and one ambiguous-contract stop in these examples. It does not establish behavior for every repository, absent Superpowers, absent project DoD, or every approval gate. Complete tool/action traces were not archived, so approval ordering cannot be claimed as fully verified. Those remain cases for later targeted tests if the skill changes or these conditions arise in real use.

The `skill-creator` `quick_validate.py` returned `Skill is valid!` with PyYAML supplied through a temporary process-local `PYTHONPATH`. A fresh, ephemeral, read-only Codex CLI session subsequently reported that `start-task` was discoverable at `C:\Users\maksimbell\.agents\skills\start-task\SKILL.md`. That discovery check made no project file changes; it did not exercise implementation behavior.
