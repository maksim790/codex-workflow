# Large-request decomposition — 2026-10-13

## Baseline

An agent applied the prior `prepare-task` instructions in a disposable Git repository at `C:\Users\maksimbell\AppData\Local\Temp\prepare-large-baseline-a5e208185b41445aaa1ba3a3bd796e7c`. A request for a separate notifications service produced one `needs-decision` ticket and no child tickets. The ticket recorded undecided interaction, data ownership, and deployment without inventing their answers. Its eight relative links resolved. A repeated attempt with the same path stopped before writing; the existing ticket, ADR, and human note were unchanged.

## Updated instructions: agent exercises

An agent applied the updated skill in two separate disposable Git repositories under `C:\Users\MAKSIM~1\AppData\Local\Temp\prepare-task-large-forward-a5426adc0c1f4069a28b535ee6b0849d`:

| Fixture | Observed result |
| --- | --- |
| Service boundary and data ownership undecided | One main `create-notifications-service.md` ticket with status `needs-decision` and a labeled proposed breakdown; no child files. |
| Accepted ADR establishes async `OrderCreated`, Orders ownership of order/contact data, and Notifications ownership of delivery state | One `ready` main ticket and three `ready` child tickets for event publication, consumption, and integration. The main ticket names the dependency order and first unblocked child. |

The agent checked bidirectional main/child links and all other relative links. Existing ADR and human-note SHA-256 hashes stayed unchanged in both fixtures. Each fixture began with a clean Git status and ended with only `?? docs/vault/12-Development/`, containing the newly written task files. Parent inspection confirmed the settled fixture's criteria follow the accepted ADR; exact provider and deployment commands remain implementation choices or unknowns.

This is an agent exercise of Markdown instructions, not deterministic enforcement by Codex or an end-to-end implementation run. No application source was changed, and application tests were not run.

## `start-task` parent handoff

Before the handoff change, an agent read the `ready` main ticket with the previous `start-task` instructions. They did not require child selection, so the whole parent could be treated as one executable task. The test was read-only; Git status and the main ticket hash were unchanged.

After the change, a separate agent resolved the same main ticket, read all three children, and identified `publish-order-created-event.md` as the first child without dependencies. It stopped to wait for the user's selection instead of starting the parent. Git status and SHA-256 hashes of all four tickets matched before and after. This validates the instruction route in the fixture, not a completed child implementation.
