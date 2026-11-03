# Negative file/recovery trial

Status: deterministic synthetic fixture evidence, 2026-11-02.

This trial covers four failure invariants that were previously only described
as decision answers:

1. A forced replacement failure leaves the canonical record byte-for-byte at
   its baseline and cleans the pending file.
2. Malformed and wrong-task records are rejected before a dependent write.
3. A stale writer detects a concurrent modification and leaves the newer
   shared record intact.
4. An unknown synthetic operation outcome remains unknown and is not replayable,
   even when the recorded external-request count is zero.

The tests are in `../test_negative_trial.py` and use only Python's standard
library plus disposable temporary directories. No production checkpoint engine,
agent, host compaction API, network, or external operation is invoked. The
helpers model fixture setup and invariant checks; passing them does not prove
that a live agent will make the same decisions.

## Verification

Run from the project root:

```text
python -B -m unittest evals.test_negative_trial
```

The bounded run on 2026-11-02 passed all five tests. This is file/invariant
evidence only; live model semantics, GUI new-session behavior, native
compaction, and cross-host recovery remain untested.
