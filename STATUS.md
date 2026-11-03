# Preview status

Version: v0.1.0-preview. Original instructions and synthetic examples, MIT licensed.

## Available workflow

Task grounding, existing-index navigation and targeted source reads, long-output filtering and authorized offload pointers, state/evidence separation, milestone checkpoint/readback, context reconstruction and verification before resuming, and conditional host compaction/isolation with manual fallback.

The core has no required database, service, API, other Skill or personal workflow dependency.

## Observed evidence

- Subset metadata/relative-link/public-marker checks passed; these are not full YAML or secret audits.
- Ten local tests passed: packaging failure detection plus deterministic synthetic file invariants. The fixture helpers are not a production checkpoint engine or proof of model behavior.
- A synthetic task record was actually written/read back. An authority-attribution error in the first attempt is retained; the corrected second revision preserved commitments, exact saved work and an unrelated record.
- A fresh evaluator recovered that synthetic task, detected a deliberate source revision change and retained an unknown operation without replay. See [trial](evals/continuity-trial/README.md).
- One actual Codex CLI attempt was blocked at required local file reading; recovery did not complete. Exit code zero was not treated as success. See [host attempt](evals/cli-host-trial/README.md).

## Not verified

Desktop GUI new-chat recovery, native compaction/hooks, cross-host behavior and measured quality/time/token gains remain unverified. The official full YAML quick validator was not run successfully because its dependency was unavailable; the independent checker reports a subset only.

No automatic persistence, lossless recovery, larger model window or universal compatibility is promised. See [compatibility](COMPATIBILITY.md) and [detailed observations](evals/RESULTS.md).
