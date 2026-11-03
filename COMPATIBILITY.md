# Compatibility and evidence

No host adapter is bundled in v0.1.0-preview. Supported manual mechanics and observed behavior must not be confused with native integration.

| Surface/capability | Required facility | Current status |
|---|---|---|
| Agent Skills format | SKILL.md and relative references | 2026-11-02 actual-root subset packaging/link check passed; not full YAML validation |
| Manual selection/checkpoint proposal | Agent can read the instructions and supplied sources | Six initial decision responses plus phase-2 synthetic checkpoint/recovery trial; not an automatic runtime guarantee |
| Actual checkpoint persistence | Authorized project file read/write | 2026-11-02 synthetic task record actually written/read back; first wording issue retained and corrected in revision 2. No automatic persistence claim |
| Fresh-context recovery | Current record and source access | 2026-11-02 fresh evaluation actor with no parent task history recovered files read-only and detected changed source/unknown outcome; not a real GUI new-chat/native-compaction test |
| Fresh Codex CLI invocation | Existing login plus permitted source reads | 2026-11-02 one actual CLI run attempted; first required read blocked by execution policy, recovery incomplete. Not a successful host test; see [attempt](evals/cli-host-trial/README.md) |
| Codex native compaction/hooks | Actual version, event support, configuration/trust and exact commands | Not implemented or tested |
| Claude Code native hooks | Actual version, setup and trusted commands | Not implemented or tested |
| Pi native timeline/compaction | Actual native extension/tools | Not implemented or tested |
| Chat-only surface | User supplies sources, manually copies checkpoint | Designed; no file-write or automatic trigger claim |

Tool permission metadata does not grant permission. Formats may be portable while runtime behavior is not. If a needed capability is unavailable, report the limitation and use the manual contract where possible; do not silently call an unrelated tool.

Hooks, when added, must be separately installed/tested and remain optional. Multiple handlers can run for an event; task-state writes require concurrency and readback handling, not an assumption of a single writer.
