# Public manual-continuity trial

Date: 2026-11-02. Package: public `context-workflow` v0.1.0-preview, not a personal installed method. All materials are synthetic; there is no implemented reading-list app and no real preview service.

## What actually happened

1. A fresh executor read [checkpoint-request.md](checkpoint-request.md), used the public checkpoint contract, minimally updated the existing [TASK.md](TASK.md), and read the write back. An unrelated task section and all three commitments were preserved.
2. Review found an authority-attribution error: the first write said the checkpoint authorized an update. The current user request actually authorized it. The unmodified first attempt is retained in [baseline/TASK.first-attempt.md](baseline/TASK.first-attempt.md).
3. A corrective write produced checkpoint revision 2 and read it back. It attributes authority to the current checkpoint request and preserves the original failure/correction history. This is success after one correction, not a first-pass perfect result.
4. The test author visibly changed [docs/requirements.md](docs/requirements.md) from revision 1 to revision 2, adding case-insensitive search. The original source is retained in [baseline/requirements.v1.md](baseline/requirements.v1.md). The checkpoint was not backfilled.
5. A fresh evaluator, with no parent task history or expected answer, received [resume-request.md](resume-request.md) and the current files. It recovered the task/commitments/exact draft, detected source drift and held dependent actions, while preserving the unknown synthetic outcome. Its [recorded answer](recovery-report.md) is retained.

The original task record is in [baseline/TASK.initial.md](baseline/TASK.initial.md); exact available session wording is in [session-input.md](session-input.md). [operations.json](operations.json) remains outcome unknown with zero external requests and replay forbidden.

## Evidence levels

- Actual local checkpoint writes/readback: performed, including a documented correction.
- Recovery from a fresh evaluation context: performed read-only.
- Native compaction, real GUI new-chat lifecycle, automatic persistence/thresholds, cross-host execution and measured performance: not tested.
- Six additional scenario answers: retained as decision responses, not executed effect tests.

These fixtures remain stale on purpose so drift detection can be reproduced. Do not update TASK.md to claim current-source acceptance or resolve the synthetic receipt.
