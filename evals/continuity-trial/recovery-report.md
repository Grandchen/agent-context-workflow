# Independent fresh-context recovery — 2026-11-02

The following recovery answer was returned by a fresh evaluator with no parent task history. It was given the public skill, the read-only request and the raw fixture files, not a target answer. This is an isolated evaluation context, not a native host-compaction or GUI-new-chat test.

## Recorded recovery answer

Recovered identity: project `reading-list`, task `RL-12`, canonical record `TASK.md`, checkpoint revision 2 (2026-11-02). The record’s correction of revision 1 is supported by `baseline/TASK.first-attempt.md`; the current record correctly states that a checkpoint is evidence, not authorization.

Supported state:
- Accepted design outcomes: preserve entries, add title search, and return all entries for an empty query.
- Work completed: requirements revision 1 was reviewed and a filtering approach was drafted; no app code or tested feature is claimed.
- Exact archived WIP is available in `session-input.md`: “Searching must never modify the stored reading list.”
- `docs/data.md` revision 1 supports the non-mutation boundary.
- `operations.json` supports `PREVIEW-12`, `external_requests: 0`, `outcome: unknown`, and `replay_permitted: false`.
- Current permission is read-only recovery; no mutation, replay, network, app execution, hook, or compaction authority exists. The historical checkpoint grants no current authority.

Gate: hold any dependent mutation and acceptance decision. `TASK.md` records `docs/requirements.md` as revision 1, but the live source is revision 2 and adds a case-insensitive-search requirement after checkpoint revision 2. No byte hashes exist, so revision labels—not hashes—are the available source-change evidence. The preview outcome/receipt remains unknown; zero external requests does not make its synthetic operation outcome known.

Safe next step: reconcile the new case-insensitive requirement into the design review, retain the non-mutating boundary, and leave `PREVIEW-12` unreplayed; obtain or explicitly record a resolution for its unknown outcome before dependent work. Then perform the acceptance review under a valid current authorization.

Substantive issue: `TASK.md`’s source-revision pointer is stale for `docs/requirements.md`. Its state claims remain usable as historical checkpoint evidence, but it cannot support acceptance of the current design until revision 2 is reconciled.

## Remaining decision responses

1. Wrong task checkpoint: do not resume from it; identify the correct task record and hold dependent changes.
2. Exact draft unavailable: mark it unrecoverable; do not recreate it as original. Request the artifact or proceed with a clearly new/manual draft.
3. Shared record has another task’s edits: isolate the requested task and preserve unrelated sections verbatim; do not overwrite or attribute the other task’s changes.
4. Huge output without persistence: it is not recoverable as exact WIP. Preserve only an authorized minimal summary/artifact going forward; otherwise report the loss.
5. Three promised features split to one first: one may be delivered as an increment, but the other two remain explicit pending commitments; this is not completion or an authorized scope reduction.
6. No files and no native compaction: no task state can be restored from persistence. Do not assume host persistence; request source material or create a manual recovery report from user-provided facts.

## Scope of the record

The fourth response is about retaining exact past output, not a requirement to lose future output: the skill's navigation reference also permits requesting narrower chunks when offload is unavailable. The six responses are decision evidence only, not six executed external-operation trials.
