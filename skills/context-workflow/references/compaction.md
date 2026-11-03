# Compaction and isolation decisions

Assess recoverability from the current record, source revisions, and exact archived WIP. Do not invent a token threshold, telemetry, or a promise that compaction will help.

- If the host exposes a verified compaction or isolation operation and the current task authorizes it, use only its documented capability and record the outcome.
- Otherwise, make a manual checkpoint, save authorized exact work, narrow the next read set, or return a bounded handoff. No native operation is required for the portable core.
- Context compaction or a fresh session does not undo external effects, create receipts, or make unknown outcomes safe to replay.
- Delegation is optional. Use it only when the host and task authorize it, return bounded sources/results, and keep one writer for task state. Do not create a mandatory agent framework.
