# Resume gates

Before a dependent mutation, verify:

1. project and task identity, checkpoint revision, and canonical record changes;
2. governing-source changes, missing sources, and the meaning of any hashes;
3. current permissions and whether a same-scope approval is still valid;
4. unknown or externally changed effects, including actions whose outcome was never received.

If identity is wrong, a source changed materially, or an effect is unknown, hold dependent work and report the gate. Safe independent work may continue only when its scope is clear. Do not replay commands or external effects and do not extend an old approval to a new scope.

Checkpoint-only recovery is valid: resume only from what the record states and mark everything else unknown. A fresh session, compaction, or host persistence is not assumed. If exact WIP was not archived, do not regenerate it as original; offer a manual next step or request the missing artifact.
